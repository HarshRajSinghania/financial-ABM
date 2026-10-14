"""Stage C: is the growth of impact investors selection or drift? (research contract section 18)

Runs the cells fixed in section 18.3 with a read-only wrapper around ``_imitate`` that records, every imitation
period, the impact share, the type-mean growth advantage and its standard error, and the switches in each
direction. Uninstrumented reruns of two worlds must reproduce their fingerprints. Writes runs/*.npz (local)
and runs.json; analyze.py turns them into the acceptance tests and decompositions.

Usage: python diagnose.py [--workers N]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.game import DisclosureMarket  # noqa: E402
from abm.disclosure.investors import IMPACT_INVESTOR  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.disclosure.runner import source_hashes  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

DOMAIN_PATH = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json"
SEEDS = tuple(range(29001, 29021))
TASTE = 0.0635
MARKET = dict(n_investors=1000, n_firms=200, trading_days=3500, burn_in_days=1200,
              financing_exposure_fraction=0.5, financing_spread=0.05, financing_repricing_interval=60,
              financing_horizon_days=1260, firm_discount_rate=0.05, intrinsic_value_log_sd=0.9151544344205937)
# (label, rule, taste_median, initial impact probability, imitation_interval)
CELLS = (
    ("type_mean_zero_0.2", "type_mean", 0.0, 0.2, 60), ("type_mean_zero_0.5", "type_mean", 0.0, 0.5, 60),
    ("type_mean_zero_0.8", "type_mean", 0.0, 0.8, 60), ("type_mean_taste_0.2", "type_mean", TASTE, 0.2, 60),
    ("pairwise_zero_0.2", "pairwise", 0.0, 0.2, 60), ("pairwise_zero_0.5", "pairwise", 0.0, 0.5, 60),
    ("pairwise_zero_0.8", "pairwise", 0.0, 0.8, 60), ("pairwise_taste_0.2", "pairwise", TASTE, 0.2, 60),
    ("pairwise_taste_0.5", "pairwise", TASTE, 0.5, 60), ("pairwise_taste_0.8", "pairwise", TASTE, 0.8, 60),
    ("pairwise_annual_zero_0.2", "pairwise", 0.0, 0.2, 252), ("pairwise_annual_taste_0.2", "pairwise", TASTE, 0.2, 252),
)
FIELDS = ("day", "impact_count", "share", "wealth_share", "advantage", "standard_error", "to_impact", "to_profit")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def setting(rule: str, taste: float, share: float, interval: int, seed: int):
    config = MarketConfig(seed=seed, taste_median=taste, initial_impact_share=share, imitation_rule=rule,
                          imitation_interval=interval, **MARKET)
    domain = load_domain(DOMAIN_PATH)
    return config, domain, PolicySchedule.constant(domain)


def run_cell(label: str, rule: str, taste: float, share: float, interval: int, seed: int, instrument: bool = True) -> dict:
    market = DisclosureMarket(*setting(rule, taste, share, interval, seed))
    rows = []
    if instrument:
        original = market._imitate

        def wrapped():
            investors = market.investors
            wealth = investors.wealth(market.prices)
            growth = wealth / market.window_wealth - 1.0
            impact = investors.investor_type == IMPACT_INVESTOR
            mixed = impact.any() and not impact.all()
            before = investors.investor_type.copy()
            original()
            after = investors.investor_type
            rows.append((market.signal_day, int(impact.sum()), float(impact.mean()), float(wealth[impact].sum() / wealth.sum()),
                         float(growth[impact].mean() - growth[~impact].mean()) if mixed else np.nan,
                         float(np.sqrt(growth[impact].var(ddof=1) / impact.sum() + growth[~impact].var(ddof=1) / (~impact).sum()))
                         if mixed and min(impact.sum(), (~impact).sum()) > 1 else np.nan,
                         int(((before != IMPACT_INVESTOR) & (after == IMPACT_INVESTOR)).sum()),
                         int(((before == IMPACT_INVESTOR) & (after != IMPACT_INVESTOR)).sum())))

        market._imitate = wrapped
    started = time.perf_counter()
    result = market.run()
    record = {"label": label, "rule": rule, "taste_median": taste, "initial_probability": share, "imitation_interval": interval,
              "seed": seed, "fingerprint": result.fingerprint(), "seconds": time.perf_counter() - started,
              "share": {"day_0": float(result.impact_share[0]), "day_1200": float(result.impact_share[1200]),
                        "day_3500": float(result.impact_share[-1])},
              "wealth_share": {"day_0": float(result.impact_wealth_share[0]), "day_1200": float(result.impact_wealth_share[1200]),
                               "day_3500": float(result.impact_wealth_share[-1])},
              "price_cap_hits": int(result.market.price_cap_hits.sum())}
    if instrument:
        target = HERE / "runs" / f"{label}_{seed}.npz"
        arrays = {field: np.array([row[index] for row in rows]) for index, field in enumerate(FIELDS)}
        with target.open("xb") as handle:
            np.savez_compressed(handle, **arrays)
        record.update(periods=len(rows), artifact=target.name, artifact_sha256=sha(target))
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    disable_power_throttling()
    (HERE / "runs").mkdir(exist_ok=False)
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    hashes = source_hashes()
    jobs = [(*cell, seed) for cell in CELLS for seed in SEEDS]
    records = []
    # Like experiments.py: background workers are otherwise slowed by Windows power throttling.
    with ProcessPoolExecutor(max_workers=args.workers, initializer=disable_power_throttling) as pool:
        futures = [pool.submit(run_cell, *job) for job in jobs]
        for future in as_completed(futures):
            record = future.result()
            records.append(record)
            print(record["label"], record["seed"], round(record["share"]["day_3500"], 3), round(record["seconds"]), flush=True)
    records.sort(key=lambda row: ([cell[0] for cell in CELLS].index(row["label"]), row["seed"]))
    checks = []
    for label in ("type_mean_zero_0.2", "pairwise_taste_0.2"):
        cell = next(cell for cell in CELLS if cell[0] == label)
        plain = run_cell(*cell, SEEDS[0], instrument=False)
        archived = next(row for row in records if row["label"] == label and row["seed"] == SEEDS[0])
        if plain["fingerprint"] != archived["fingerprint"]:
            raise RuntimeError(f"instrumentation changed the path: {label}")
        checks.append({"label": label, "seed": SEEDS[0], "fingerprint_matches": True})
    if source_hashes() != hashes:
        raise RuntimeError("source changed during the diagnosis")
    payload = {"contract": "research contract section 18", "script_sha256": sha(Path(__file__)),
               "source_hashes": hashes, "domain": {"path": DOMAIN_PATH.relative_to(ROOT).as_posix(), "sha256": sha(DOMAIN_PATH)},
               "market": MARKET, "seeds": list(SEEDS),
               "cells": [dict(zip(("label", "rule", "taste_median", "initial_probability", "imitation_interval"), cell))
                         for cell in CELLS],
               "instrumentation_checks": checks, "records": records}
    with (HERE / "runs.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


if __name__ == "__main__":
    main()
