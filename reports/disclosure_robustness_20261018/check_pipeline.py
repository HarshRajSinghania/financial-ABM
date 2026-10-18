"""Pipeline checks that need full result arrays (contract 20.21), on development seed 33001 only.

  python check_pipeline.py

Reruns rev0p32_B, rev0p5_B and rep_B from configs/disclosure_robustness_check_v1.json, and decay0_B from the
stage F scenario they derive from, with full archives in work_check/pipeline/ (local only). Checks:
  R  the cross-sectional mean of true values moves only through actions (reversion and shocks keep it), and
     the cross-sectional SD stays near its initial level instead of collapsing;
  P  every detection is charged a whole number (at least one) of fixed fines, and more than one somewhere.
No effect estimates are computed. Writes check_pipeline.json.
"""

from __future__ import annotations

import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
SEED = 33001
NAMES = ("rev0p32_B", "rev0p5_B", "rep_B", "decay0_B")


def rerun(scenario: dict, destination: str) -> None:
    from abm.disclosure.experiments import _inputs
    from abm.disclosure.runner import run_and_archive
    from abm.platform_tuning import disable_power_throttling

    disable_power_throttling()
    config, domain, policy = _inputs(scenario, SEED)
    run_and_archive(config, domain, destination, policy, archive="full")


def main() -> None:
    from abm.disclosure.experiments import freeze_spec
    from abm.disclosure.runner import load_result

    frozen = freeze_spec(ROOT / "configs" / "disclosure_robustness_check_v1.json")
    rows = {row["name"]: row for row in frozen["scenarios"]}
    decay0 = json.loads(json.dumps(rows["rev0p32_B"]))
    decay0["name"] = "decay0_B"
    decay0["domain"].pop("natural_reversion")
    rows["decay0_B"] = decay0
    work = HERE / "work_check" / "pipeline"
    work.mkdir(parents=True, exist_ok=True)
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    with ProcessPoolExecutor(max_workers=len(NAMES)) as pool:
        for future in [pool.submit(rerun, rows[name], str(work / name)) for name in NAMES if not (work / name / "result.npz").exists()]:
            future.result()
    results = {name: load_result(work / name / "result.npz") for name in NAMES}
    out: dict = {"seed": SEED, "R": {}, "P": {}}
    for name in ("rev0p32_B", "rev0p5_B", "decay0_B"):
        result = results[name]
        true = result.true_goodness
        landed = np.zeros(true.shape[0])
        for period, firm in np.argwhere(result.actions == 0):
            due = result.action_due_day[period, firm]
            if due < true.shape[0]:
                landed[due] += result.amounts[period, firm]
        # Mean change not explained by landed improvements (the upper bound caps none here).
        residual = np.diff(true.mean(axis=1)) - landed[1:] / true.shape[1]
        out["R"][name] = {"cross_section_sd": {str(d): float(true[d].std()) for d in (0, 1200, 2400, 3500)},
                          "max_abs_mean_change_not_from_improvements": float(np.abs(residual).max()),
                          "uniform_decay_per_day": 0.0}
    rep = results["rep_B"]
    fine = rep_fine(frozen)
    prices = rep.market.prices[::frozen["scenarios"][0]["config"]["firm_decision_interval"]]
    counts = rep.penalty_fraction * prices / fine
    caught = rep.detections.astype(bool)
    rounded = np.round(counts)
    out["P"] = {"detections": int(caught.sum()), "max_deviation_from_whole_fines": float(np.abs(counts - rounded).max()),
                "all_detections_at_least_one_fine": bool(np.all(rounded[caught] >= 1)),
                "no_fine_without_detection": bool(np.all(counts[~caught] == 0)),
                "fines_per_detection": {str(int(k)): int(v) for k, v in zip(*np.unique(rounded[caught], return_counts=True))}}
    out["passed"] = (all(r["max_abs_mean_change_not_from_improvements"] < 1e-9 for r in out["R"].values())
                     and all(r["cross_section_sd"]["3500"] > .5 for r in out["R"].values())
                     and out["P"]["max_deviation_from_whole_fines"] < 1e-6 and out["P"]["all_detections_at_least_one_fine"]
                     and out["P"]["no_fine_without_detection"])
    (HERE / "check_pipeline.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(out, indent=2))


def rep_fine(frozen: dict) -> float:
    row = next(r for r in frozen["scenarios"] if r["name"] == "rep_B")
    return float(row["policy"]["baseline"]["fixed_fine"])


if __name__ == "__main__":
    main()
