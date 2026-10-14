"""Stage B before and after signal saturation: same design, seeds and doses (research contract section 17.6).

Reads the archived outputs of both versions (grid tables, instrumented diagnosis, saturation statistics)
and the archived result.npz files for the share of firm-days whose traded signal sits at the ceiling.
No simulation is run. Writes comparison.json.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = HERE.parent / "disclosure_fixed_fine_diagnosis_20261013"
GRIDS = {"v1_unsaturated": ROOT / "reports/disclosure_csi300_fixed_fine_development_20261013_v1",
         "v2_saturated": ROOT / "reports/disclosure_csi300_fixed_fine_saturated_development_20261013_v1"}
OUTPUTS = {"v1_unsaturated": V1, "v2_saturated": HERE}
SCENARIO_METRICS = ("actions.wash", "actions.firms_washing", "inflation.mean_sd", "true_change.equal_weight_sd",
                    "actions.detections", "actions.wash_share_by_size.large", "actions.wash_share_by_size.small",
                    "size.large_minus_small_sd")
COMPARISONS = ("market_effect", "information_minus_penalty", "market_policy_interaction", "residual_size_gap",
               "information_minus_baseline", "penalty_minus_baseline", "fixed_minus_proportional_baseline",
               "zero_fine_minus_baseline", "information_low_minus_baseline", "information_mid_minus_baseline",
               "penalty_low_minus_baseline")
CEILING_SCENARIOS = ("market_B", "market_F", "market_I", "zero_fine_B")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(version: str, name: str) -> dict:
    return json.loads((OUTPUTS[version] / name).read_text(encoding="utf-8"))


def ceiling_shares(grid: Path, ceiling: float, seeds) -> dict:
    """Policy-window shares of firm-days: traded signal at the ceiling; inflated reports near it."""
    shares = {}
    for scenario in CEILING_SCENARIOS:
        counts = {"signal": 0, "inflated": 0, **{distance: 0 for distance in ("0.1", "0.25", "0.5")}}
        total, gaps, stocks = 0, [], []
        for seed in seeds:
            with np.load(grid / scenario / f"seed_{seed}" / "attempt_001" / "result.npz") as bundle:
                signal = bundle["public_signal"][1201:]
                truth, inflation = bundle["true_goodness"][1201:], bundle["inflation"][1201:]
                inflated = inflation > 0
                distance = ceiling - (truth + inflation)
                counts["signal"] += int((signal >= ceiling - 1e-12).sum())
                counts["inflated"] += int(inflated.sum())
                for key in ("0.1", "0.25", "0.5"):
                    counts[key] += int((inflated & (distance <= float(key))).sum())
                total += signal.size
                near = inflated & (distance <= 0.25)
                gaps.append(float((ceiling - truth)[near].mean()) if near.any() else None)
                stocks.append(float(inflation[inflated].mean()) if inflated.any() else None)
        inflated_days = counts["inflated"]
        shares[scenario] = {
            "signal_at_or_above_ceiling": counts["signal"] / total,
            "inflated_firm_days": inflated_days / total,
            "inflated_report_within_sd_of_ceiling": {key: counts[key] / inflated_days if inflated_days else None
                                                     for key in ("0.1", "0.25", "0.5")},
            "mean_inflation_when_inflated_by_seed": stocks,
            "mean_truth_gap_to_ceiling_when_inflated_report_within_0.25_by_seed": gaps,
        }
    return shares


def main():
    tables = {version: load(version, "grid_tables.json") for version in OUTPUTS}
    diagnosis = {version: load(version, "diagnosis.json") for version in OUTPUTS}
    saturation = {version: load(version, "saturation.json") for version in OUTPUTS}
    ceiling = saturation["v2_saturated"]["latent_score_of_raw_maximum"]
    scenarios = {}
    for name in tables["v1_unsaturated"]["scenarios"]:
        scenarios[name] = {metric: {version: tables[version]["scenarios"][name].get(metric) for version in OUTPUTS}
                           for metric in SCENARIO_METRICS}
    comparisons = {}
    for name in COMPARISONS:
        comparisons[name] = {version: {metric: tables[version]["comparisons"][name].get(metric)
                                       for metric in ("true_change.equal_weight_sd", "inflation.mean_sd", "actions.wash",
                                                      "full_period_change.equal_weight_sd", "size.large_minus_small_sd")}
                             for version in OUTPUTS}
    decisions = {}
    for version in OUTPUTS:
        report = diagnosis[version]["report"]
        decisions[version] = {
            name: {"replicated_actions_match": entry["replicated_actions_match"],
                   "policy_window": entry["summary"]["policy_window"],
                   "size_gradient": entry.get("size_gradient"),
                   "frontiers": [{"label": row["label"], "curve": row["curve"]} for row in entry.get("conditional_frontiers", [])]}
            for name, entry in report.items()}
    seeds = json.loads((GRIDS["v2_saturated"] / "experiment.json").read_text(encoding="utf-8"))["spec"]["seeds"]
    payload = {
        "script_sha256": sha(Path(__file__)), "ceiling_latent": ceiling,
        "sources": {version: {"grid_experiment_id": tables[version]["experiment_id"],
                              "grid_summary_sha256": tables[version]["summary_sha256"],
                              "grid_tables_sha256": sha(OUTPUTS[version] / "grid_tables.json"),
                              "diagnosis_sha256": sha(OUTPUTS[version] / "diagnosis.json"),
                              "saturation_sha256": sha(OUTPUTS[version] / "saturation.json"),
                              "trials": [tables[version]["complete_trials"], tables[version]["planned_trials"]],
                              "trials_failing_core_validation": tables[version]["trials_failing_core_validation"]}
                    for version in OUTPUTS},
        "ceiling_shares_policy_window": {version: ceiling_shares(GRIDS[version], ceiling, seeds) for version in GRIDS},
        "saturation": {version: saturation[version]["report"] for version in OUTPUTS},
        "scenarios": scenarios, "comparisons": comparisons, "decisions": decisions,
        "scope": "Development seeds 28101-28103; paired intervals unadjusted; no simulation.",
    }
    (HERE / "comparison.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                          encoding="utf-8")
    print(json.dumps(payload["ceiling_shares_policy_window"], indent=1))


if __name__ == "__main__":
    main()
