"""Benchmark return models scored with the same moments as the ABM.

* ``iid_t``: independent Student-t returns, fitted by maximum likelihood. It has
  fat tails but no volatility clustering, so it marks the floor any dynamic
  model should beat.
* ``garch_t``: GARCH(1,1) with Student-t innovations, the standard statistical
  benchmark, fitted by pooled maximum likelihood across the training
  industries with per-industry variance targeting.
* ``ham``: the Franke-Westerhoff (2012) DCA-HPM heterogeneous-agent model, a
  small structural ABM, calibrated by the same MSM routine as the Stage 1
  market and with the same number of free parameters.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Sequence

import numpy as np
from numpy.typing import NDArray

from .french49 import French49Dataset, IndustrySplit, parse_french49_zip
from .msm import (
    MOMENT_NAMES,
    EmpiricalTarget,
    ParameterSpace,
    calibrate,
    compute_moments,
    empirical_target,
    objective,
)
from .platform_tuning import disable_power_throttling

FloatArray = NDArray[np.float64]
SIMULATION_BURN_IN = 500


def _training_series(dataset: French49Dataset, industries: Sequence[str]) -> list[FloatArray]:
    index = {name: position for position, name in enumerate(dataset.industries)}
    series = []
    for industry in industries:
        values = dataset.returns[:, index[industry]]
        values = values[np.isfinite(values)]
        series.append(values - values.mean())
    return series


def _student_t_logpdf(standardized: FloatArray, scale: FloatArray, nu: float) -> FloatArray:
    """Log density of a unit-variance Student-t, rescaled by ``scale``."""
    from scipy.special import gammaln

    constant = gammaln((nu + 1.0) / 2.0) - gammaln(nu / 2.0) - 0.5 * np.log(np.pi * (nu - 2.0))
    return constant - np.log(scale) - (nu + 1.0) / 2.0 * np.log1p(standardized**2 / (nu - 2.0))


def _unit_variance_t(rng: np.random.Generator, nu: float, size: int | tuple[int, ...]) -> FloatArray:
    return rng.standard_t(nu, size=size) * np.sqrt((nu - 2.0) / nu)


def fit_iid_t(series: Sequence[FloatArray]) -> dict[str, float]:
    """Pooled MLE of the tail parameter with each industry's own scale."""
    from scipy.optimize import minimize_scalar

    standardized = [values / values.std() for values in series]

    def negative_log_likelihood(nu: float) -> float:
        return -float(
            sum(np.sum(_student_t_logpdf(z, np.ones_like(z), nu)) for z in standardized)
        )

    outcome = minimize_scalar(negative_log_likelihood, bounds=(2.05, 60.0), method="bounded")
    return {"nu": float(outcome.x), "log_likelihood": -float(outcome.fun)}


def garch_variance_path(residuals: FloatArray, omega: float, alpha: float, beta: float) -> FloatArray:
    """Conditional variances of a GARCH(1,1), started at the sample variance."""
    from scipy.signal import lfilter

    squared = residuals**2
    variance = np.empty_like(squared)
    variance[0] = squared.mean()
    # sigma2_t = omega + alpha * e_{t-1}^2 + beta * sigma2_{t-1}
    driven = omega + alpha * squared[:-1]
    variance[1:], _ = lfilter([1.0], [1.0, -beta], driven, zi=[beta * variance[0]])
    return variance


def fit_garch_t(series: Sequence[FloatArray]) -> dict[str, float]:
    """Pooled GARCH(1,1)-t MLE with shared (alpha, beta, nu).

    Each industry keeps its own unconditional variance through variance
    targeting, omega_i = var_i * (1 - alpha - beta).
    """
    from scipy.optimize import minimize

    def unpack(raw: FloatArray) -> tuple[float, float, float]:
        alpha = 1.0 / (1.0 + np.exp(-raw[0]))
        persistence = 1.0 / (1.0 + np.exp(-raw[1]))
        beta = (1.0 - alpha) * persistence
        nu = 2.05 + np.exp(raw[2])
        return alpha, beta, nu

    def negative_log_likelihood(raw: FloatArray) -> float:
        alpha, beta, nu = unpack(raw)
        total = 0.0
        for values in series:
            omega = values.var() * (1.0 - alpha - beta)
            variance = garch_variance_path(values, omega, alpha, beta)
            scale = np.sqrt(variance)
            total += float(np.sum(_student_t_logpdf(values / scale, scale, nu)))
        return -total

    start = np.array([np.log(0.08 / 0.92), np.log(0.9 / 0.1), np.log(6.0)])
    outcome = minimize(negative_log_likelihood, start, method="Nelder-Mead",
                       options={"xatol": 1e-4, "fatol": 1e-3, "maxfev": 2000})
    alpha, beta, nu = unpack(outcome.x)
    return {
        "alpha": float(alpha),
        "beta": float(beta),
        "nu": float(nu),
        "persistence": float(alpha + beta),
        "log_likelihood": -float(outcome.fun),
        "converged": bool(outcome.success),
    }


def simulate_iid_t(
    nu: float, volatility: float, *, observations: int, seeds: Sequence[int]
) -> FloatArray:
    rows = []
    for seed in seeds:
        returns = volatility * _unit_variance_t(np.random.default_rng(seed), nu, observations)
        rows.append(compute_moments(returns))
    return np.array(rows)


def simulate_garch_t(
    alpha: float,
    beta: float,
    nu: float,
    volatility: float,
    *,
    observations: int,
    seeds: Sequence[int],
) -> FloatArray:
    omega = volatility**2 * (1.0 - alpha - beta)
    rows = []
    for seed in seeds:
        shocks = _unit_variance_t(np.random.default_rng(seed), nu, SIMULATION_BURN_IN + observations)
        returns = np.empty_like(shocks)
        variance = volatility**2
        previous = 0.0
        for day, shock in enumerate(shocks):
            variance = omega + alpha * previous**2 + beta * variance
            previous = np.sqrt(variance) * shock
            returns[day] = previous
        rows.append(compute_moments(returns[SIMULATION_BURN_IN:]))
    return np.array(rows)


# Franke and Westerhoff (2012), DCA-HPM. The market-maker reaction mu is
# fixed at 0.01 as in the original paper; the remaining seven are free.
HAM_PARAMETER_SPACE = ParameterSpace.from_dict(
    {
        "phi": (0.01, 0.5),
        "chi": (0.1, 3.0),
        "sigma_f": (0.1, 3.0),
        "sigma_c": (0.5, 5.0),
        "alpha_0": (-1.5, 1.0),
        "alpha_n": (0.0, 2.5),
        "alpha_p": (0.0, 40.0),
    }
)
HAM_MU = 0.01


def simulate_ham_returns(theta: FloatArray, *, observations: int, seed: int) -> FloatArray:
    phi, chi, sigma_f, sigma_c, alpha_0, alpha_n, alpha_p = (float(value) for value in theta)
    total = SIMULATION_BURN_IN + observations
    rng = np.random.default_rng(seed)
    fundamental_noise = sigma_f * rng.standard_normal(total)
    chartist_noise = sigma_c * rng.standard_normal(total)
    log_price = np.zeros(total + 1)
    share_fundamental = 0.5
    attractiveness = 0.0
    previous_price = 0.0
    for day in range(total):
        price = log_price[day]
        fundamental_demand = phi * (0.0 - price) + fundamental_noise[day]
        chartist_demand = chi * (price - previous_price) + chartist_noise[day]
        log_price[day + 1] = price + HAM_MU * (
            share_fundamental * fundamental_demand
            + (1.0 - share_fundamental) * chartist_demand
        )
        attractiveness = alpha_0 + alpha_n * (2.0 * share_fundamental - 1.0) + alpha_p * price**2
        share_fundamental = 1.0 / (1.0 + np.exp(-np.clip(attractiveness, -50.0, 50.0)))
        previous_price = price
    log_returns = np.diff(log_price)[SIMULATION_BURN_IN:]
    return np.expm1(log_returns)


class HamSimulator:
    def __init__(self, *, observations: int, seeds: Sequence[int]) -> None:
        self.observations = observations
        self.seeds = tuple(seeds)

    def __call__(self, thetas: FloatArray) -> FloatArray:
        thetas = np.atleast_2d(np.asarray(thetas, dtype=np.float64))
        output = np.full((len(thetas), len(self.seeds), len(MOMENT_NAMES)), np.nan)
        for row, theta in enumerate(thetas):
            for column, seed in enumerate(self.seeds):
                returns = simulate_ham_returns(theta, observations=self.observations, seed=seed)
                if np.all(np.isfinite(returns)) and np.all(returns > -1.0):
                    try:
                        output[row, column] = compute_moments(returns)
                    except ValueError:
                        pass
        return output


def fit_baselines(
    dataset: French49Dataset,
    split: IndustrySplit,
    target: EmpiricalTarget,
    *,
    seeds: Sequence[int],
    screen_points: int,
    refine_starts: int,
    refine_evaluations: int,
) -> dict[str, object]:
    series = _training_series(dataset, split.train)
    volatility = float(target.moments[MOMENT_NAMES.index("daily_volatility")])
    iid = fit_iid_t(series)
    garch = fit_garch_t(series)
    ham = calibrate(
        HamSimulator(observations=target.observations, seeds=seeds),
        HAM_PARAMETER_SPACE,
        target,
        screen_points=screen_points,
        refine_starts=refine_starts,
        refine_evaluations=refine_evaluations,
        progress=lambda message: print(f"ham {message}", flush=True),
    )
    return {
        "volatility_target": volatility,
        "iid_t": {**iid, "train": objective(
            simulate_iid_t(iid["nu"], volatility, observations=target.observations, seeds=seeds), target)},
        "garch_t": {**garch, "train": objective(
            simulate_garch_t(garch["alpha"], garch["beta"], garch["nu"], volatility,
                             observations=target.observations, seeds=seeds), target)},
        "ham": {"mu": HAM_MU, **{key: ham[key] for key in ("parameter_names", "bounds", "best_theta", "best", "refinements")}},
    }


def baseline_moments(
    fitted: dict[str, object],
    *,
    observations: int,
    seeds: Sequence[int],
) -> dict[str, FloatArray]:
    """Simulated per-seed moments of every fitted baseline."""
    volatility = float(fitted["volatility_target"])
    iid, garch, ham = fitted["iid_t"], fitted["garch_t"], fitted["ham"]
    return {
        "iid_t": simulate_iid_t(iid["nu"], volatility, observations=observations, seeds=seeds),
        "garch_t": simulate_garch_t(garch["alpha"], garch["beta"], garch["nu"], volatility,
                                    observations=observations, seeds=seeds),
        "ham": HamSimulator(observations=observations, seeds=seeds)(np.array(ham["best_theta"]))[0],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--split", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="MSM report directory")
    parser.add_argument("--start", type=date.fromisoformat, default=date(2000, 1, 1))
    parser.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    parser.add_argument("--seeds", type=int, nargs="+", default=list(range(20261201, 20261211)))
    parser.add_argument("--screen-points", type=int, default=256)
    parser.add_argument("--refine-starts", type=int, default=3)
    parser.add_argument("--refine-evaluations", type=int, default=80)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    disable_power_throttling()
    destination = args.output / "baselines.json"
    if destination.exists():
        raise FileExistsError(destination)
    dataset = parse_french49_zip(args.archive).between(args.start, args.end)
    split = IndustrySplit.from_json(args.split)
    target = empirical_target(dataset, split.train)
    fitted = fit_baselines(
        dataset, split, target,
        seeds=args.seeds,
        screen_points=args.screen_points,
        refine_starts=args.refine_starts,
        refine_evaluations=args.refine_evaluations,
    )
    fitted["seeds"] = list(args.seeds)
    fitted["moment_names"] = list(MOMENT_NAMES)
    args.output.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(fitted, indent=2) + "\n")
    print(json.dumps({name: fitted[name]["train"]["j"] if "train" in fitted[name] else fitted[name]["best"]["j"]
                      for name in ("iid_t", "garch_t", "ham")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
