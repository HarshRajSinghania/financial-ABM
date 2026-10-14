"""Calibration check under the pairwise imitation rule (research contract section 18.6).

Same seeds, tastes and tolerances as verify_saturation.py (section 17.5), with signal saturation on and
``imitation_rule="pairwise"``. Only pre-policy pricing is read.
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace
from pathlib import Path

import numpy as np

import calibrate
from abm.disclosure.policy import PolicySchedule

HERE = Path(__file__).resolve().parent
BASE_SETTING = calibrate.setting
CHECKS = {"main_28bp": (0.0635, 28.0, 2.8), "lower_7bp": (0.021, 7.0, 0.7)}


def pairwise_setting(taste, seed, fixed_fine):
    config, domain, _ = BASE_SETTING(taste, seed, fixed_fine)
    domain = replace(domain, signal_saturation=True)
    return replace(config, imitation_rule="pairwise"), domain, PolicySchedule.constant(domain)


def run_pairwise(taste, seed, fixed_fine):
    calibrate.setting = pairwise_setting
    return calibrate.run_one(taste, seed, fixed_fine)


def main():
    calibration = json.loads((HERE / "calibration.json").read_text(encoding="utf-8"))
    fixed_fine = calibration["fixed_fine"]["model_units"]
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    jobs = [(label, taste, seed) for label, (taste, _, _) in CHECKS.items() for seed in calibrate.SEEDS]
    with ProcessPoolExecutor(max_workers=len(jobs)) as pool:
        runs = list(pool.map(run_pairwise, [job[1] for job in jobs], [job[2] for job in jobs], [fixed_fine] * len(jobs)))
    results = {}
    for label, (taste, target, tolerance) in CHECKS.items():
        group = [run for (name, _, _), run in zip(jobs, runs) if name == label]
        decisions = [row for run in group for row in run["decisions"]]
        median_bp = float(-np.median([row["yield_slope"] for row in decisions]) * 1e4)
        results[label] = {
            "taste_median": taste, "status": [run["status"] for run in group],
            "yield_slope_median_bp": -median_bp, "target_bp": -target, "tolerance_bp": tolerance,
            "within_tolerance": abs(median_bp - target) <= tolerance,
            "yield_slope_by_seed_bp": [float(np.median([row["yield_slope"] for row in run["decisions"]]) * 1e4)
                                       for run in group],
            "impact_share_day_1200_by_seed": [run["decisions"][-1]["impact_share"] for run in group],
            "price_cap_hits": [run.get("price_cap_hits") for run in group],
            "fingerprints": [run.get("fingerprint") for run in group],
        }
    keep = all(row["within_tolerance"] for row in results.values())
    payload = {"rule": "research contract section 18.6", "signal_saturation": True, "imitation_rule": "pairwise",
               "calibration_sha256": calibrate.sha(HERE / "calibration.json"), "script_sha256": calibrate.sha(Path(__file__)),
               "seeds": list(calibrate.SEEDS), "results": results,
               "decision": "keep taste_median 0.0635 and 0.021" if keep else "outside tolerance: re-interpolate"}
    with (HERE / "verification_pairwise.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({key: {k: v for k, v in row.items() if k != "fingerprints"} for key, row in results.items()}, indent=1))
    print(payload["decision"])


if __name__ == "__main__":
    main()
