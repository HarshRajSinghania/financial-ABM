"""Pre-policy financing premium as a function of taste_median (research contract section 15.4).

Runs the main setting's pre-policy window (days 0-1200, contract scale 1000 investors / 200 firms) for a
grid of taste medians on calibration-only seeds, with a read-only wrapper on ``marginal_financing_saving``.
At every pre-policy decision day it records three model counterparts of "financing-rate reduction per SD
of score":

* ``local_rate_response``: each firm's own forecast, spread * F P / (F + P)^2 * dlogP/dsignal, the
  quantity NPV firms act on (the 0.9 bp of the empirical-magnitudes note);
* ``rate_slope``: cross-sectional OLS slope of the quoted financing rate on the public signal;
* ``yield_slope``: cross-sectional OLS slope of the dividend yield yV/P on the public signal, the
  model's existing ``pricing_slope`` diagnostic.

The empirical target (28 bp per SD; 7 bp lower sensitivity) is a cross-sectional association of the
implied cost of equity with the rating, not a causal effect. Firm actions and inflation are not read:
the calibration does not look at any washing or policy outcome.

Usage: python calibrate.py [--workers N]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import replace
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.game import DisclosureMarket, pricing_slope  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402

DOMAIN_PATH = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula.json"
JOINT_CSV = ROOT / "data/processed/disclosure_public_20261012/csi300_joint_20261009.csv"
SEEDS = (28001, 28002, 28003)
TASTES = (0.02, 0.05, 0.1, 0.2, 0.4, 0.8)
TARGET, LOWER_TARGET = 0.0028, 0.0007
POLICY_START = 1201
FINE_YUAN = 1e7
MARKET = dict(
    n_investors=1000, n_firms=200, trading_days=POLICY_START - 1, burn_in_days=600,
    initial_impact_share=0.2, financing_exposure_fraction=0.5, financing_spread=0.05,
    financing_repricing_interval=60, financing_horizon_days=1260, firm_discount_rate=0.05,
    intrinsic_value_log_sd=0.9151544344205937,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mean_market_cap_yuan() -> float:
    import csv

    with JOINT_CSV.open(encoding="utf-8-sig", newline="") as handle:
        caps = [float(row["market_cap_cny"]) for row in csv.DictReader(handle)]
    if len(caps) != 300:
        raise ValueError("expected the 300-firm joint sample")
    return float(np.mean(caps))


def setting(taste: float, seed: int, fixed_fine: float):
    config = MarketConfig(seed=seed, taste_median=taste, **MARKET)
    domain = replace(load_domain(DOMAIN_PATH), baseline_penalty=0.0, baseline_fixed_fine=fixed_fine)
    return config, domain, PolicySchedule.constant(domain)


def ols_slope(y: np.ndarray, x: np.ndarray) -> float:
    centered = x - x.mean()
    return float(centered @ (y - y.mean()) / (centered @ centered))


def run_one(taste: float, seed: int, fixed_fine: float, instrument: bool = True) -> dict:
    config, domain, policy = setting(taste, seed, fixed_fine)
    market = DisclosureMarket(config, domain, policy)
    rows = []
    if instrument:
        original = market.marginal_financing_saving

        def wrapped():
            benefit = original()
            day = market.signal_day
            signal = market.signal_z(day)
            prices, values = market.prices, market.firms.intrinsic_value
            local = benefit * prices / market.financing_exposure
            rows.append({
                "day": day,
                "local_rate_response_median": float(np.median(local)),
                "local_rate_response_mean": float(local.mean()),
                "local_rate_response_by_firm": local.tolist(),
                "rate_slope": ols_slope(market.quoted_financing_rate(), signal),
                "yield_slope": pricing_slope(market.cost_of_capital(), signal),
                "log_price_premium_slope": ols_slope(np.log(prices / values), signal),
                "impact_share": float(market.impact_share[day - 1]),
                "impact_wealth_share": float(market.impact_wealth_share[day - 1]),
            })
            return benefit

        market.marginal_financing_saving = wrapped
    started = time.perf_counter()
    try:
        result = market.run()
    except Exception as error:  # a failed world is recorded, never dropped
        return {"taste": taste, "seed": seed, "status": "failed", "error": f"{type(error).__name__}: {error}",
                "decisions": rows}
    return {"taste": taste, "seed": seed, "status": "complete", "fingerprint": result.fingerprint(),
            "seconds": time.perf_counter() - started, "price_cap_hits": int(result.market.price_cap_hits.sum()),
            "max_abs_log_mispricing": float(np.abs(np.log(result.market.prices / result.market.intrinsic_values)).max()),
            "decisions": rows}


def interpolate(tastes, values, target):
    """Log-log interpolation of the taste at which a monotone statistic reaches the target."""
    tastes, values = np.asarray(tastes, float), np.asarray(values, float)
    ok = np.isfinite(values) & (values > 0)
    tastes, values = tastes[ok], values[ok]
    if tastes.size < 2 or not np.all(np.diff(values) > 0):
        return None
    if not values[0] <= target <= values[-1]:
        return None
    return float(np.exp(np.interp(np.log(target), np.log(values), np.log(tastes))))


def summarize(runs):
    by_taste = {}
    for run in runs:
        by_taste.setdefault(run["taste"], []).append(run)
    table = []
    for taste in sorted(by_taste):
        group = by_taste[taste]
        decisions = [row for run in group for row in run["decisions"]]
        late = [row for row in decisions if row["day"] >= 600]
        firm_level = np.concatenate([row["local_rate_response_by_firm"] for row in decisions])
        table.append({
            "taste_median": taste,
            "worlds": len(group), "failed_worlds": sum(run["status"] != "complete" for run in group),
            "price_cap_hits": sum(run.get("price_cap_hits", 0) for run in group),
            "max_abs_log_mispricing": max(run.get("max_abs_log_mispricing", np.nan) for run in group),
            "decision_days": len(decisions),
            "local_rate_response": {"median_firm_decision": float(np.median(firm_level)),
                                    "p5": float(np.quantile(firm_level, .05)), "p95": float(np.quantile(firm_level, .95)),
                                    "median_late_days": float(np.median([row["local_rate_response_median"] for row in late]))},
            "rate_slope": {"median_day": float(np.median([row["rate_slope"] for row in decisions])),
                           "median_late_days": float(np.median([row["rate_slope"] for row in late]))},
            "yield_slope": {"median_day": float(np.median([row["yield_slope"] for row in decisions])),
                            "median_late_days": float(np.median([row["yield_slope"] for row in late]))},
            "log_price_premium_slope": {"median_day": float(np.median([row["log_price_premium_slope"] for row in decisions])),
                                        "median_late_days": float(np.median([row["log_price_premium_slope"] for row in late]))},
            "impact_share_day_1200": float(np.mean([run["decisions"][-1]["impact_share"] for run in group if run["decisions"]])),
        })
    tastes = [row["taste_median"] for row in table]
    readings = {
        "local_rate_response": [row["local_rate_response"]["median_firm_decision"] for row in table],
        "rate_slope": [-row["rate_slope"]["median_day"] for row in table],
        "yield_slope": [-row["yield_slope"]["median_day"] for row in table],
    }
    implied = {name: {"target_28bp": interpolate(tastes, values, TARGET),
                      "lower_7bp": interpolate(tastes, values, LOWER_TARGET)} for name, values in readings.items()}
    return table, implied


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    cap = mean_market_cap_yuan()
    fixed_fine = FINE_YUAN / cap
    jobs = [(taste, seed) for taste in TASTES for seed in SEEDS]
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"  # inherited by the worker processes
    runs = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_one, taste, seed, fixed_fine): (taste, seed) for taste, seed in jobs}
        for future in as_completed(futures):
            run = future.result()
            runs.append(run)
            print(run["taste"], run["seed"], run["status"], round(run.get("seconds", 0), 1), flush=True)
    runs.sort(key=lambda run: (run["taste"], run["seed"]))
    # The wrapper is read-only: an uninstrumented rerun must reproduce the fingerprint.
    check = next(run for run in runs if run["status"] == "complete")
    plain = run_one(check["taste"], check["seed"], fixed_fine, instrument=False)
    if plain["fingerprint"] != check["fingerprint"]:
        raise RuntimeError("instrumentation changed the simulated path")
    table, implied = summarize(runs)
    payload = {
        "purpose": "calibration (development seeds only); research contract section 15.4",
        "script_sha256": sha(Path(__file__)),
        "domain": {"path": DOMAIN_PATH.relative_to(ROOT).as_posix(), "sha256": sha(DOMAIN_PATH),
                   "overrides": {"baseline_penalty": 0.0, "baseline_fixed_fine": fixed_fine}},
        "fixed_fine": {"yuan": FINE_YUAN, "mean_market_cap_yuan": cap, "model_units": fixed_fine,
                       "source_csv": {"path": JOINT_CSV.relative_to(ROOT).as_posix(), "sha256": sha(JOINT_CSV)}},
        "market": MARKET, "seeds": list(SEEDS), "tastes": list(TASTES), "policy_start": POLICY_START,
        "targets": {"main_bp": TARGET * 1e4, "lower_sensitivity_bp": LOWER_TARGET * 1e4},
        "instrumentation_check": {"taste": check["taste"], "seed": check["seed"], "fingerprint_matches": True},
        "summary": table, "implied_taste_median": implied,
        "runs": [{key: value for key, value in run.items() if key != "decisions"}
                 | {"decisions": [{key: value for key, value in row.items() if key != "local_rate_response_by_firm"}
                                  for row in run["decisions"]]} for run in runs],
        "scope": "Pre-policy pricing only; actions, inflation and policy outcomes were not read.",
    }
    with (HERE / "calibration.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"summary": [{key: row[key] for key in ("taste_median", "failed_worlds", "price_cap_hits")}
                                  | {"local": row["local_rate_response"]["median_firm_decision"],
                                     "rate": row["rate_slope"]["median_day"], "yield": row["yield_slope"]["median_day"]}
                                  for row in table], "implied": implied}, indent=1))


if __name__ == "__main__":
    main()
