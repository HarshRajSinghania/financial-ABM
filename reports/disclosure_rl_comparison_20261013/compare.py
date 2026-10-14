"""Stage D.2: read-only comparison of the archived runs (research contract section 19.3-19.4).

Reads runs/<scenario>/summary.json and each validation run's metrics.json / validation.json. Writes
comparison.json: coverage verdicts, per-scenario means, paired policy effects with 95% t intervals,
the M4 consistency checks, and training counts against the D.1 sample-size estimate.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs" / "v2"
D1 = HERE.parent / "disclosure_rl_diagnosis_20261013" / "snr_analysis.json"
SCENARIOS = ("B", "I", "F", "IF")
RULES = ("q_learning", "npv_discrete", "npv")
CONTRASTS = (("I", "B"), ("F", "B"), ("IF", "B"), ("I", "F"))
SIZES = ("large", "mid", "small")


def interval(values: np.ndarray) -> dict:
    mean = float(values.mean())
    half = float(stats.t.ppf(.975, values.size - 1) * values.std(ddof=1) / np.sqrt(values.size))
    return {"mean": mean, "low": mean - half, "high": mean + half, "n": int(values.size),
            "t_p": float(stats.ttest_1samp(values, 0).pvalue)}


def outcomes(folder: Path) -> dict:
    metrics = json.loads((folder / "metrics.json").read_text(encoding="utf-8"))
    validation = json.loads((folder / "validation.json").read_text(encoding="utf-8"))
    actions = metrics["actions"]
    return {"true_change": metrics["true_change"]["equal_weight_sd"],
            "wash_share": actions["wash"] / actions["decisions"],
            "improve_share": actions["improve"] / actions["decisions"],
            "inflation_mean": metrics["inflation"]["mean_sd"],
            **{f"wash_share_{size}": actions["wash_share_by_size"][size] for size in SIZES},
            **{f"true_change_{size}": metrics["size"][size]["change_sd"] for size in SIZES},
            "mechanical": validation["mechanical"]["status"],
            "max_cost_fraction": float(np.load(folder / "result.npz")["cost_fraction"].max())}


def coverage_summary(summary: dict) -> dict:
    coverage = summary["validation"]["coverage"]
    keys = ("status", "global_status", "decisions", "unseen_state_fraction")
    return {**{key: coverage.get(key) for key in keys},
            "groups": [{key: group[key] for key in ("group", "decisions", "unseen_state_fraction", "status")}
                       for group in coverage.get("groups", [])],
            "worlds": [{key: world[key] for key in ("seed", "unseen_state_fraction", "global_status", "status")}
                       for world in coverage.get("worlds", [])],
            "undercovered_global": len(coverage.get("common_state_undercovered_actions", [])),
            "undercovered_group": len(coverage.get("group_common_state_undercovered_actions", []))}


def training_counts(name: str, summary: dict) -> dict:
    """Training counts of the legal choices the coverage gate checks, against the D.1 requirement."""
    with np.load(RUNS / name / "frozen_model.npz") as model:
        counts = model["counts"]
    coverage = summary["validation"]["coverage"]
    visits = np.asarray(coverage["visits"])
    legal = np.asarray(coverage["legal_action_visits"])
    totals = visits.sum(axis=1, keepdims=True)
    common = (visits > 0) & (visits >= .01 * np.maximum(totals, 1))
    checked = counts[common[:, :, None] & (legal > 0)]
    need = json.loads(D1.read_text(encoding="utf-8"))
    return {"checked_cells": int(checked.size),
            "count_quantiles": np.quantile(checked, [0, .1, .5, .9]).tolist() if checked.size else None,
            "samples_needed_median_gap": need["samples_needed_median_gap"],
            "samples_needed_gap_q90": need["samples_needed_gap_q90"],
            "share_cells_reaching_q90_requirement": float((checked >= need["samples_needed_gap_q90"]).mean()) if checked.size else None}


def main() -> None:
    result: dict = {"coverage": {}, "training_counts": {}, "runs": {}, "means": {}, "effects": {}, "m4": {}}
    baseline = json.loads((RUNS / "baseline" / "summary.json").read_text(encoding="utf-8"))
    result["coverage"]["baseline"] = coverage_summary(baseline)
    result["training_counts"]["baseline"] = training_counts("baseline", baseline)
    seeds = None
    for name in SCENARIOS:
        summary = json.loads((RUNS / name / "summary.json").read_text(encoding="utf-8"))
        result["coverage"][name] = coverage_summary(summary)
        result["training_counts"][name] = training_counts(name, summary)
        seeds = summary["budget"]["validation_seeds"] if seeds is None else seeds
        if summary["budget"]["validation_seeds"] != seeds:
            raise ValueError("scenarios must share validation seeds")
        result["runs"][name] = {rule: [outcomes(RUNS / name / "validation" / f"seed_{seed}" / rule) for seed in seeds]
                                for rule in RULES}
    fields = [key for key in result["runs"]["B"]["npv"][0] if key not in ("mechanical", "max_cost_fraction")]
    # Contract 19.7: the 1% budget binds only shared-grid rules; check it never binds continuous NPV either.
    result["max_cost_fraction"] = {rule: max(row["max_cost_fraction"] for name in SCENARIOS for row in result["runs"][name][rule])
                                   for rule in RULES}
    for rule in RULES:
        result["means"][rule] = {name: {key: float(np.mean([row[key] for row in result["runs"][name][rule]]))
                                        for key in fields} for name in SCENARIOS}
        result["effects"][rule] = {}
        for left, right in CONTRASTS:
            result["effects"][rule][f"{left}-{right}"] = {
                key: interval(np.array([a[key] - b[key] for a, b in zip(result["runs"][left][rule], result["runs"][right][rule])]))
                for key in ("true_change", "wash_share", "inflation_mean")}
    for other in ("npv_discrete", "npv"):
        q = result["effects"]["q_learning"]["I-F"]["true_change"]["mean"]
        o = result["effects"][other]["I-F"]["true_change"]["mean"]
        rank_q = sorted(SCENARIOS, key=lambda name: -result["means"]["q_learning"][name]["true_change"])
        rank_o = sorted(SCENARIOS, key=lambda name: -result["means"][other][name]["true_change"])
        result["m4"][f"q_learning_vs_{other}"] = {"I_minus_F_sign_agrees": bool(np.sign(q) == np.sign(o)),
                                                 "ranking_q_learning": rank_q, f"ranking_{other}": rank_o,
                                                 "ranking_agrees": rank_q == rank_o}
    result["mechanical_fail"] = {name: {rule: [row["mechanical"] for row in result["runs"][name][rule]].count("FAIL")
                                        for rule in RULES} for name in SCENARIOS}
    (HERE / "comparison.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("m4", "mechanical_fail", "max_cost_fraction")}, indent=2))
    for rule in RULES:
        print(rule)
        for name in SCENARIOS:
            row = result["means"][rule][name]
            print(f"  {name:3s} true {row['true_change']:+.3f}  wash {row['wash_share']:.3f}  infl {row['inflation_mean']:.3f}")
        for contrast, values in result["effects"][rule].items():
            e = values["true_change"]
            print(f"  {contrast:5s} true {e['mean']:+.3f} [{e['low']:+.3f}, {e['high']:+.3f}]")


if __name__ == "__main__":
    main()
