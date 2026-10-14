"""Compact tables from the archived stage B development grid (no simulation, no reclassification).

Reads summary.json and experiment.json of the grid, checks the summary hash recorded by the runner, and writes
grid_tables.json with per-scenario means and paired comparisons for the metrics the stage B acceptance needs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GRID = ROOT / "reports/disclosure_csi300_fixed_fine_development_20261013_v1"
METRICS = ("actions.wash", "actions.firms_washing", "actions.detections", "inflation.mean_sd",
           "true_change.equal_weight_sd", "actions.improve", "costs.fine_transfer", "size.large_minus_small_sd",
           "actions.wash_share_by_size.large", "actions.wash_share_by_size.mid", "actions.wash_share_by_size.small",
           "pricing_slope.mean", "full_period_change.equal_weight_sd")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((GRID / "summary_manifest.json").read_text(encoding="utf-8"))
    if sha(GRID / "summary.json") != manifest["summary_sha256"]:
        raise ValueError("grid summary hash mismatch")
    summary = json.loads((GRID / "summary.json").read_text(encoding="utf-8"))
    records = summary["records"]
    validation = {}
    for row in records:
        if row["status"] != "complete":
            validation.setdefault("not_complete", []).append([row["scenario"], row["seed"], row["status"]])
            continue
        for gate in ("mechanical", "stylized"):
            if row["validation"][gate]["status"] != "PASS":
                validation.setdefault(f"{gate}_fail", []).append([row["scenario"], row["seed"]])
    scenarios = {}
    for scenario in summary["scenarios"]:
        scenarios[scenario["name"]] = {metric: (scenario["metrics"][metric].get("mean")
                                                if scenario["metrics"][metric]["status"] == "complete" else None)
                                       for metric in METRICS if metric in scenario["metrics"]}
        values = {}
        for row in records:
            if row["scenario"] == scenario["name"] and row["status"] == "complete":
                for metric in ("actions.wash", "inflation.mean_sd"):
                    value = row["metrics"]
                    for part in metric.split("."):
                        value = value[part]
                    values.setdefault(metric, []).append(value)
        scenarios[scenario["name"]]["by_seed"] = values
    comparisons = {}
    for comparison in summary["comparisons"]:
        comparisons[comparison["name"]] = {
            "weights": comparison["weights"], "primary": comparison.get("primary", False),
            "core_validation_pass": comparison["core_validation_pass"],
            **{metric: ({key: comparison["metrics"][metric][key] for key in ("mean", "ci_low", "ci_high", "p_value", "n")}
                        | ({"holm_p_value": comparison["metrics"][metric]["holm_p_value"]}
                           if "holm_p_value" in comparison["metrics"][metric] else {})
                        if comparison["metrics"][metric]["status"] == "complete" else {"status": "incomplete"})
               for metric in METRICS if metric in comparison["metrics"]},
        }
    payload = {"grid": GRID.relative_to(ROOT).as_posix(), "experiment_id": summary["experiment_id"],
               "summary_sha256": manifest["summary_sha256"], "script_sha256": sha(Path(__file__)),
               "complete_trials": summary["complete_trials"], "planned_trials": summary["planned_trials"],
               "trials_failing_core_validation": summary["trials_failing_core_validation"],
               "validation": validation, "scenarios": scenarios, "comparisons": comparisons,
               "inference": summary["inference"]}
    (HERE / "grid_tables.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                           encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("complete_trials", "planned_trials", "trials_failing_core_validation",
                                                     "validation")}, indent=1))


if __name__ == "__main__":
    main()
