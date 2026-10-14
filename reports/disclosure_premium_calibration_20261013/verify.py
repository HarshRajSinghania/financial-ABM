"""Verification runs at the tastes interpolated by calibrate.py for the chosen statistic.

The research decision (2026-10-13, before any policy or washing result was produced): the target is the
cross-sectional dividend-yield slope ``pricing_slope``, median over pre-policy decision days and seeds.
Reruns the same calibration seeds at the interpolated main and lower-sensitivity tastes.
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

import calibrate

HERE = Path(__file__).resolve().parent


def main():
    calibration = json.loads((HERE / "calibration.json").read_text(encoding="utf-8"))
    implied = calibration["implied_taste_median"]["yield_slope"]
    tastes = {"main_28bp": round(implied["target_28bp"], 4), "lower_7bp": round(implied["lower_7bp"], 4)}
    fixed_fine = calibration["fixed_fine"]["model_units"]
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    jobs = [(label, taste, seed) for label, taste in tastes.items() for seed in calibrate.SEEDS]
    with ProcessPoolExecutor(max_workers=len(jobs)) as pool:
        runs = list(pool.map(calibrate.run_one, [job[1] for job in jobs], [job[2] for job in jobs],
                             [fixed_fine] * len(jobs)))
    results = {}
    for label, taste in tastes.items():
        group = [run for (name, _, _), run in zip(jobs, runs) if name == label]
        slopes = [row["yield_slope"] for run in group for row in run["decisions"]]
        results[label] = {
            "taste_median": taste, "status": [run["status"] for run in group],
            "yield_slope_median_bp": float(np.median(slopes) * 1e4),
            "yield_slope_by_seed_bp": [float(np.median([row["yield_slope"] for row in run["decisions"]]) * 1e4)
                                       for run in group],
            "rate_slope_median_bp": float(np.median([row["rate_slope"] for run in group for row in run["decisions"]]) * 1e4),
            "local_rate_response_median_bp": float(np.median(np.concatenate(
                [row["local_rate_response_by_firm"] for run in group for row in run["decisions"]])) * 1e4),
            "log_price_premium_slope_median": float(np.median([row["log_price_premium_slope"]
                                                               for run in group for row in run["decisions"]])),
            "price_cap_hits": [run.get("price_cap_hits") for run in group],
            "fingerprints": [run.get("fingerprint") for run in group],
        }
    payload = {"decision": "pricing_slope (dividend-yield cross-sectional OLS slope), chosen before any policy or washing result",
               "calibration_sha256": calibrate.sha(HERE / "calibration.json"), "script_sha256": calibrate.sha(Path(__file__)),
               "seeds": list(calibrate.SEEDS), "results": results}
    with (HERE / "verification.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
