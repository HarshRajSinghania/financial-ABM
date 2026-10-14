"""Re-interpolation under the pairwise imitation rule (research contract section 18.6).

verify_pairwise.py found the main value outside its tolerance (-24.6 bp at taste 0.0635), so the main value is
recalibrated with the procedure of calibrate.py: the same taste grid and calibration seeds, log-log
interpolation of the pre-policy dividend-yield slope median, then a verification run at the interpolated
taste. Signal saturation is on. The lower value (0.021, -6.8 bp) stayed within tolerance and is kept.
Only pre-policy pricing is read.
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

import calibrate
import verify_pairwise

HERE = Path(__file__).resolve().parent


def run(taste, seed, fixed_fine):
    return verify_pairwise.run_pairwise(taste, seed, fixed_fine)


def main():
    calibration = json.loads((HERE / "calibration.json").read_text(encoding="utf-8"))
    fixed_fine = calibration["fixed_fine"]["model_units"]
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    jobs = [(taste, seed) for taste in calibrate.TASTES for seed in calibrate.SEEDS]
    with ProcessPoolExecutor(max_workers=6) as pool:
        runs = list(pool.map(run, [job[0] for job in jobs], [job[1] for job in jobs], [fixed_fine] * len(jobs)))
    table, implied = calibrate.summarize(runs)
    main_taste = round(implied["yield_slope"]["target_28bp"], 4)
    with ProcessPoolExecutor(max_workers=3) as pool:
        verification = list(pool.map(run, [main_taste] * 3, calibrate.SEEDS, [fixed_fine] * 3))
    slopes = [row["yield_slope"] for item in verification for row in item["decisions"]]
    payload = {
        "rule": "research contract section 18.6", "signal_saturation": True, "imitation_rule": "pairwise",
        "script_sha256": calibrate.sha(Path(__file__)), "seeds": list(calibrate.SEEDS), "tastes": list(calibrate.TASTES),
        "summary": table, "implied_taste_median": implied,
        "main": {"taste_median": main_taste, "yield_slope_median_bp": float(np.median(slopes) * 1e4),
                 "yield_slope_by_seed_bp": [float(np.median([row["yield_slope"] for row in item["decisions"]]) * 1e4)
                                            for item in verification],
                 "fingerprints": [item["fingerprint"] for item in verification]},
        "lower": {"taste_median": 0.021, "kept": "within tolerance in verification_pairwise.json"},
        "scan_fingerprints": {f"{run_['taste']}_{run_['seed']}": run_.get("fingerprint") for run_ in runs},
    }
    with (HERE / "calibration_pairwise.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"implied": implied, "main": payload["main"]}, indent=1))


if __name__ == "__main__":
    main()
