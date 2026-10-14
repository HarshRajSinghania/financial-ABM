"""Post-hoc supplement, not fixed in research contract section 18.3: the pairwise rule at the recalibrated taste.

Section 18.6 moved the main taste to 0.0724 under the pairwise rule after the diagnosis design was fixed at
0.0635. This reruns the pairwise, initial-probability-0.2 cell at 0.0724 on the same seeds and pairs it with
the archived zero-taste cell from runs.json. Run after diagnose.py; writes runs_supplement.json.
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import diagnose
from abm.disclosure.experiments import paired_statistics
from abm.platform_tuning import disable_power_throttling

HERE = Path(__file__).resolve().parent
CELL = ("pairwise_taste0724_0.2", "pairwise", 0.0724, 0.2, 60)
CONTROL = "pairwise_zero_0.2"


def main():
    disable_power_throttling()
    base = json.loads((HERE / "runs.json").read_text(encoding="utf-8"))
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    hashes = diagnose.source_hashes()
    if hashes != base["source_hashes"]:
        raise RuntimeError("source differs from the diagnosis run")
    with ProcessPoolExecutor(max_workers=len(diagnose.SEEDS), initializer=disable_power_throttling) as pool:
        records = list(pool.map(diagnose.run_cell, *zip(*[(*CELL, seed) for seed in diagnose.SEEDS])))
    control = {row["seed"]: row for row in base["records"] if row["label"] == CONTROL}
    change = [row["share"]["day_3500"] - row["share"]["day_0"] for row in records]
    paired = [value - (control[row["seed"]]["share"]["day_3500"] - control[row["seed"]]["share"]["day_0"])
              for value, row in zip(change, records)]
    wealth = [row["wealth_share"]["day_3500"] - row["wealth_share"]["day_0"]
              - (control[row["seed"]]["wealth_share"]["day_3500"] - control[row["seed"]]["wealth_share"]["day_0"])
              for row in records]
    summary = {name: {key: stats[key] for key in ("mean", "ci_low", "ci_high", "p_value", "n")}
               for name, stats in (("share_change", paired_statistics(change, .95)),
                                   ("paired_share_change_minus_zero_taste", paired_statistics(paired, .95)),
                                   ("paired_wealth_share_change_minus_zero_taste", paired_statistics(wealth, .95)))}
    payload = {"status": "post hoc supplement; not part of the section 18.3 design", "cell": dict(zip(
                   ("label", "rule", "taste_median", "initial_probability", "imitation_interval"), CELL)),
               "control": CONTROL, "script_sha256": diagnose.sha(Path(__file__)), "source_hashes": hashes,
               "runs_json_sha256": diagnose.sha(HERE / "runs.json"), "summary": summary, "records": records}
    with (HERE / "runs_supplement.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
