"""Simulated method of moments (MSM) calibration against French 49 returns.

The empirical target is the average moment vector of a group of industries.
Its noise scale is the sampling covariance of one series of the same length,
estimated by a circular block bootstrap, so a simulated path is judged against
the uncertainty a single market history actually carries. The objective uses
a diagonal weight, which makes J the sum of squared per-moment t-statistics.

Fundamental shocks stay Gaussian during calibration, so any fat tails or
volatility clustering the fitted model shows must come from its endogenous
trading and liquidity mechanisms rather than from the exogenous input.
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import Executor, ProcessPoolExecutor
from dataclasses import dataclass, replace
from datetime import date
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np
from numpy.typing import NDArray

from .config import Stage1Config, load_stage1_config
from .french49 import French49Dataset, IndustrySplit, _autocorrelation, parse_french49_zip
from .harness import run_stage1
from .platform_tuning import disable_power_throttling

FloatArray = NDArray[np.float64]

MOMENT_NAMES = (
    "daily_volatility",
    "excess_kurtosis",
    "return_acf_1",
    "abs_return_acf_1",
    "abs_return_acf_5",
    "abs_return_acf_20",
    "quantile_01",
    "quantile_99",
    "hill_tail_index",
)
FAILED_SIMULATION_PENALTY = 1e6


def hill_tail_index(values: FloatArray, tail_fraction: float = 0.025) -> float:
    """Hill estimate of the tail exponent of absolute demeaned returns."""
    finite = values[np.isfinite(values)]
    magnitudes = np.sort(np.abs(finite - finite.mean()))[::-1]
    tail_size = int(tail_fraction * magnitudes.size)
    if tail_size < 10:
        raise ValueError("Hill estimator needs at least 10 tail observations")
    threshold = magnitudes[tail_size]
    if threshold <= 0:
        raise ValueError("Hill estimator threshold must be positive")
    return float(1.0 / np.mean(np.log(magnitudes[:tail_size] / threshold)))


def compute_moments(returns: FloatArray) -> FloatArray:
    """Return the calibration moment vector in ``MOMENT_NAMES`` order."""
    finite = returns[np.isfinite(returns)]
    if finite.size < 250:
        raise ValueError("at least 250 finite returns are required")
    standardized = (finite - finite.mean()) / finite.std()
    absolute = np.abs(returns)
    return np.array(
        (
            float(np.std(finite, ddof=1)),
            float(np.mean(standardized**4) - 3.0),
            _autocorrelation(returns, 1),
            _autocorrelation(absolute, 1),
            _autocorrelation(absolute, 5),
            _autocorrelation(absolute, 20),
            float(np.quantile(finite, 0.01)),
            float(np.quantile(finite, 0.99)),
            hill_tail_index(finite),
        ),
        dtype=np.float64,
    )


def block_bootstrap_moments(
    returns: FloatArray,
    *,
    block_length: int,
    draws: int,
    rng: np.random.Generator,
) -> FloatArray:
    """Moments of circular block-bootstrap resamples, shape ``(draws, k)``."""
    if block_length < 1 or draws < 2:
        raise ValueError("block_length must be positive and draws at least two")
    size = returns.size
    blocks = -(-size // block_length)
    offsets = np.arange(block_length)
    samples = np.empty((draws, len(MOMENT_NAMES)), dtype=np.float64)
    for draw in range(draws):
        starts = rng.integers(0, size, size=blocks)
        index = ((starts[:, None] + offsets[None, :]) % size).ravel()[:size]
        samples[draw] = compute_moments(returns[index])
    return samples


@dataclass(frozen=True, slots=True)
class EmpiricalTarget:
    industries: tuple[str, ...]
    observations: int
    moments: FloatArray
    covariance: FloatArray
    per_industry: FloatArray

    @property
    def standard_errors(self) -> FloatArray:
        return np.sqrt(np.diag(self.covariance))

    def to_dict(self) -> dict[str, object]:
        return {
            "moment_names": list(MOMENT_NAMES),
            "industries": list(self.industries),
            "observations": self.observations,
            "moments": self.moments.tolist(),
            "standard_errors": self.standard_errors.tolist(),
            "covariance": self.covariance.tolist(),
            "per_industry": {
                name: row.tolist()
                for name, row in zip(self.industries, self.per_industry, strict=True)
            },
        }


def empirical_target(
    dataset: French49Dataset,
    industries: Sequence[str],
    *,
    block_length: int = 20,
    draws: int = 200,
    seed: int = 20261011,
) -> EmpiricalTarget:
    index = {name: position for position, name in enumerate(dataset.industries)}
    missing = set(industries) - set(index)
    if missing:
        raise ValueError(f"unknown industries: {sorted(missing)}")
    rng = np.random.default_rng(seed)
    per_industry = []
    covariances = []
    for industry in industries:
        series = dataset.returns[:, index[industry]]
        series = series[np.isfinite(series)]
        per_industry.append(compute_moments(series))
        samples = block_bootstrap_moments(
            series, block_length=block_length, draws=draws, rng=rng
        )
        covariances.append(np.cov(samples, rowvar=False))
    per_industry_matrix = np.vstack(per_industry)
    return EmpiricalTarget(
        industries=tuple(industries),
        observations=int(dataset.returns.shape[0]),
        moments=per_industry_matrix.mean(axis=0),
        covariance=np.mean(covariances, axis=0),
        per_industry=per_industry_matrix,
    )


@dataclass(frozen=True, slots=True)
class ParameterSpace:
    names: tuple[str, ...]
    lower: FloatArray
    upper: FloatArray

    def __post_init__(self) -> None:
        if not self.names or len(set(self.names)) != len(self.names):
            raise ValueError("parameter names must be unique and nonempty")
        if self.lower.shape != (len(self.names),) or self.upper.shape != self.lower.shape:
            raise ValueError("bounds must match the parameter names")
        if np.any(self.lower >= self.upper):
            raise ValueError("every lower bound must be below its upper bound")

    @classmethod
    def from_dict(cls, bounds: Mapping[str, Sequence[float]]) -> "ParameterSpace":
        names = tuple(bounds)
        return cls(
            names=names,
            lower=np.array([float(bounds[name][0]) for name in names]),
            upper=np.array([float(bounds[name][1]) for name in names]),
        )

    def from_unit(self, unit: FloatArray) -> FloatArray:
        return self.lower + np.clip(unit, 0.0, 1.0) * (self.upper - self.lower)

    def to_unit(self, theta: FloatArray) -> FloatArray:
        return (np.asarray(theta, dtype=np.float64) - self.lower) / (self.upper - self.lower)

    def apply(self, config: Stage1Config, theta: FloatArray) -> Stage1Config:
        return replace(
            config,
            **{name: float(value) for name, value in zip(self.names, theta, strict=True)},
        )

    def to_dict(self) -> dict[str, list[float]]:
        return {
            name: [float(low), float(high)]
            for name, low, high in zip(self.names, self.lower, self.upper, strict=True)
        }


# Parameters chosen by a one-at-a-time sensitivity screen around the v15
# configuration: each moves at least one moment by several standard errors
# across its range. value_sensitivity and trend_sensitivity barely move any
# daily moment and are left fixed; minimum_liquidity_fraction is dropped as
# nearly collinear with liquidity_volatility_sensitivity. Exogenous fat-tail
# inputs (fundamental_shock_df, fundamental_arch/garch) are excluded on purpose.
DEFAULT_PARAMETER_SPACE = ParameterSpace.from_dict(
    {
        "fundamental_volatility": (0.003, 0.012),
        "price_impact": (0.2, 1.2),
        "liquidity_volatility_sensitivity": (0.0, 4.0),
        "activity_volatility_sensitivity": (0.0, 6.0),
        "noise_scale": (0.3, 3.0),
        "demand_volatility_exponent": (0.5, 1.5),
        "transient_impact_decay": (0.6, 0.99),
    }
)


def _simulate_path_moments(
    config: Stage1Config,
    burn_in_days: int,
) -> FloatArray:
    try:
        result = run_stage1(config)
        returns = result.prices[1:] / result.prices[:-1] - 1.0
        moments = compute_moments(returns[burn_in_days:])
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return np.full(len(MOMENT_NAMES), np.nan)
    return moments if np.all(np.isfinite(moments)) else np.full(len(MOMENT_NAMES), np.nan)


def simulate_configs(
    configs: Sequence[Stage1Config],
    burn_in_days: int,
    executor: Executor | None = None,
) -> FloatArray:
    """Post-burn-in moments of fully specified configurations, ``(n, k)``.

    Failed or non-finite paths come back as rows of NaN.
    """
    burn_ins = [burn_in_days] * len(configs)
    if executor is None:
        rows = list(map(_simulate_path_moments, configs, burn_ins))
    else:
        rows = list(executor.map(_simulate_path_moments, configs, burn_ins))
    return np.array(rows, dtype=np.float64).reshape(len(configs), len(MOMENT_NAMES))


SimulateFunction = Callable[[FloatArray], FloatArray]


class StageOneSimulator:
    """Map parameter vectors to simulated moments, ``(n, seeds, k)``.

    Every parameter vector reuses the same seeds (common random numbers),
    so objective differences reflect parameters rather than sampling noise.
    """

    def __init__(
        self,
        base_config: Stage1Config,
        space: ParameterSpace,
        *,
        seeds: Sequence[int],
        observations: int,
        executor: Executor | None = None,
    ) -> None:
        if not seeds:
            raise ValueError("at least one simulation seed is required")
        self.base_config = base_config
        self.space = space
        self.seeds = tuple(int(seed) for seed in seeds)
        self.burn_in_days = base_config.burn_in_days
        self.trading_days = base_config.burn_in_days + observations
        self.executor = executor
        self.evaluations = 0

    def config_for(self, theta: FloatArray, seed: int) -> Stage1Config:
        return replace(
            self.space.apply(self.base_config, theta),
            seed=seed,
            trading_days=self.trading_days,
        )

    def __call__(self, thetas: FloatArray) -> FloatArray:
        thetas = np.atleast_2d(np.asarray(thetas, dtype=np.float64))
        configs = [
            self.config_for(theta, seed) for theta in thetas for seed in self.seeds
        ]
        rows = simulate_configs(configs, self.burn_in_days, self.executor)
        self.evaluations += len(thetas)
        return rows.reshape(len(thetas), len(self.seeds), len(MOMENT_NAMES))


def objective(simulated: FloatArray, target: EmpiricalTarget) -> dict[str, object]:
    """Diagonal-weight MSM objective for one parameter vector.

    ``simulated`` has shape ``(seeds, k)``. The simulated mean carries its own
    Monte Carlo noise, hence the ``1 + 1/S`` variance inflation.
    """
    finite_rows = simulated[np.all(np.isfinite(simulated), axis=1)]
    if finite_rows.shape[0] < max(2, simulated.shape[0] // 2):
        return {
            "j": FAILED_SIMULATION_PENALTY,
            "failed_paths": int(simulated.shape[0] - finite_rows.shape[0]),
            "simulated_moments": None,
            "t_statistics": None,
        }
    mean = finite_rows.mean(axis=0)
    scale = target.standard_errors * np.sqrt(1.0 + 1.0 / finite_rows.shape[0])
    t_statistics = (mean - target.moments) / scale
    return {
        "j": float(np.sum(t_statistics**2)),
        "failed_paths": int(simulated.shape[0] - finite_rows.shape[0]),
        "simulated_moments": mean.tolist(),
        "t_statistics": t_statistics.tolist(),
    }


def calibrate(
    simulate: SimulateFunction,
    space: ParameterSpace,
    target: EmpiricalTarget,
    *,
    screen_points: int = 128,
    refine_starts: int = 3,
    refine_evaluations: int = 80,
    seed: int = 20261011,
    progress: Callable[[str], None] | None = None,
) -> dict[str, object]:
    """Sobol screen of the parameter box, then bounded Nelder-Mead refinement."""
    from scipy.optimize import minimize
    from scipy.stats import qmc

    history: list[dict[str, object]] = []

    def record(theta: FloatArray, simulated: FloatArray, phase: str) -> float:
        summary = objective(simulated, target)
        history.append({"phase": phase, "theta": theta.tolist(), **summary})
        return float(summary["j"])

    sampler = qmc.Sobol(d=len(space.names), scramble=True, seed=seed)
    unit_points = sampler.random(screen_points)
    thetas = np.vstack([space.from_unit(point) for point in unit_points])
    batch = 16
    for start in range(0, len(thetas), batch):
        chunk = thetas[start : start + batch]
        for theta, simulated in zip(chunk, simulate(chunk), strict=True):
            record(theta, simulated, "screen")
        if progress:
            best = min(float(row["j"]) for row in history)
            progress(f"screen {min(start + batch, len(thetas))}/{len(thetas)} best J={best:.2f}")

    screen_order = np.argsort([float(row["j"]) for row in history])
    refinements = []
    for rank, index in enumerate(screen_order[:refine_starts]):
        start_unit = space.to_unit(np.array(history[index]["theta"]))

        def unit_objective(unit: FloatArray, rank: int = rank) -> float:
            theta = space.from_unit(unit)
            return record(theta, simulate(theta[None, :])[0], f"refine-{rank}")

        outcome = minimize(
            unit_objective,
            start_unit,
            method="Nelder-Mead",
            bounds=[(0.0, 1.0)] * len(space.names),
            options={
                "maxfev": refine_evaluations,
                "xatol": 1e-3,
                "fatol": 1e-2,
                "initial_simplex": _initial_simplex(start_unit, 0.08),
            },
        )
        refinements.append(
            {
                "start_theta": space.from_unit(start_unit).tolist(),
                "theta": space.from_unit(outcome.x).tolist(),
                "j": float(outcome.fun),
                "evaluations": int(outcome.nfev),
                "message": str(outcome.message),
            }
        )
        if progress:
            progress(f"refine {rank + 1}/{refine_starts} J={outcome.fun:.2f}")

    best_row = min(history, key=lambda row: float(row["j"]))
    return {
        "parameter_names": list(space.names),
        "bounds": space.to_dict(),
        "best_theta": best_row["theta"],
        "best": best_row,
        "refinements": refinements,
        "history": history,
    }


def _initial_simplex(center: FloatArray, step: float) -> FloatArray:
    vertices = [center]
    for axis in range(center.size):
        vertex = center.copy()
        vertex[axis] += step if center[axis] + step <= 1.0 else -step
        vertices.append(vertex)
    return np.array(vertices)


def parameter_standard_errors(
    simulate: SimulateFunction,
    space: ParameterSpace,
    target: EmpiricalTarget,
    theta: FloatArray,
    *,
    relative_step: float = 0.05,
) -> dict[str, object]:
    """Sandwich standard errors from a central finite-difference Jacobian.

    With weight W and empirical covariance Omega the asymptotic covariance is
    (1 + 1/S) (D'WD)^-1 D'W Omega W D (D'WD)^-1.
    """
    theta = np.asarray(theta, dtype=np.float64)
    steps = relative_step * (space.upper - space.lower)
    points = []
    for axis in range(theta.size):
        for sign in (1.0, -1.0):
            point = theta.copy()
            point[axis] = np.clip(point[axis] + sign * steps[axis], space.lower[axis], space.upper[axis])
            points.append(point)
    simulated = simulate(np.vstack(points))
    seeds = simulated.shape[1]
    means = np.nanmean(simulated, axis=1)
    jacobian = np.empty((len(MOMENT_NAMES), theta.size))
    for axis in range(theta.size):
        upper, lower = points[2 * axis][axis], points[2 * axis + 1][axis]
        jacobian[:, axis] = (means[2 * axis] - means[2 * axis + 1]) / (upper - lower)
    weight = np.diag(1.0 / np.diag(target.covariance))
    bread = np.linalg.pinv(jacobian.T @ weight @ jacobian)
    meat = jacobian.T @ weight @ target.covariance @ weight @ jacobian
    covariance = (1.0 + 1.0 / seeds) * bread @ meat @ bread
    return {
        "standard_errors": np.sqrt(np.clip(np.diag(covariance), 0.0, None)).tolist(),
        "jacobian": jacobian.tolist(),
        "jacobian_condition_number": float(np.linalg.cond(jacobian.T @ weight @ jacobian)),
    }


def evaluate(
    simulate: SimulateFunction,
    theta: FloatArray,
    target: EmpiricalTarget,
) -> dict[str, object]:
    simulated = simulate(np.asarray(theta, dtype=np.float64)[None, :])[0]
    summary = objective(simulated, target)
    return {
        "theta": np.asarray(theta).tolist(),
        "target_moments": target.moments.tolist(),
        "target_standard_errors": target.standard_errors.tolist(),
        **summary,
        "per_seed_moments": simulated.tolist(),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--split", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--start", type=date.fromisoformat, default=date(2000, 1, 1))
    parser.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    parser.add_argument("--seeds", type=int, nargs="+", default=list(range(20261201, 20261211)))
    parser.add_argument("--screen-points", type=int, default=128)
    parser.add_argument("--refine-starts", type=int, default=3)
    parser.add_argument("--refine-evaluations", type=int, default=80)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--evaluate-test",
        action="store_true",
        help="score the calibrated parameters on the sealed test industries (run once)",
    )
    return parser


def _write_json(path: Path, payload: object) -> None:
    with path.open("x", encoding="utf-8") as destination:
        destination.write(json.dumps(payload, indent=2) + "\n")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    disable_power_throttling()
    dataset = parse_french49_zip(args.archive).between(args.start, args.end)
    split = IndustrySplit.from_json(args.split)
    base_config = load_stage1_config(args.config)
    space = DEFAULT_PARAMETER_SPACE

    if args.evaluate_test:
        calibration = json.loads((args.output / "calibration.json").read_text(encoding="utf-8"))
        theta = np.array(calibration["best_theta"])
        groups = {"train": split.train, "validation": split.validation, "test": split.test}
        destination = args.output / "evaluation.json"
        if destination.exists():
            raise FileExistsError(destination)
    else:
        args.output.mkdir(parents=True, exist_ok=False)
        groups = {"train": split.train}

    targets = {name: empirical_target(dataset, industries) for name, industries in groups.items()}
    with ProcessPoolExecutor(max_workers=args.workers, initializer=disable_power_throttling) as executor:
        simulator = StageOneSimulator(
            base_config,
            space,
            seeds=args.seeds,
            observations=targets["train"].observations,
            executor=executor,
        )
        if args.evaluate_test:
            _write_json(
                destination,
                {
                    "moment_names": list(MOMENT_NAMES),
                    "targets": {name: target.to_dict() for name, target in targets.items()},
                    "evaluations": {
                        name: evaluate(simulator, theta, target)
                        for name, target in targets.items()
                    },
                },
            )
            return 0
        _write_json(args.output / "target_train.json", targets["train"].to_dict())
        result = calibrate(
            simulator,
            space,
            targets["train"],
            screen_points=args.screen_points,
            refine_starts=args.refine_starts,
            refine_evaluations=args.refine_evaluations,
            progress=lambda message: print(message, flush=True),
        )
        theta = np.array(result["best_theta"])
        result["standard_errors"] = parameter_standard_errors(
            simulator, space, targets["train"], theta
        )
        result["base_config"] = str(args.config)
        result["seeds"] = list(simulator.seeds)
        result["observations"] = targets["train"].observations
        result["moment_names"] = list(MOMENT_NAMES)
        _write_json(args.output / "calibration.json", result)
    print(json.dumps({"best_j": result["best"]["j"], "best_theta": dict(zip(space.names, result["best_theta"]))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
