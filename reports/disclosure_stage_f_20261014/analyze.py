"""Stage F analysis (research contract section 20). Reads one finished grid directory, read-only.

  python analyze.py development_v1     # pipeline checks plus every table, from the development seeds
  python analyze.py confirmatory_v1

Writes <run>_analysis.json next to this script. Inference for the comparisons comes from the grid's own
summary.json (paired t, Holm for the four primary contrasts); this script adds the pipeline checks, wash
shares, dose-response tables, the phase classifications (section 20.5) and the tau*(w) check (20.6).
"""

from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SWITCH = 1201
POLICY_SETS = {  # scenarios sharing a market setting, whose histories must agree before the switch
    "main_on": ["B", "I", "F", "IF", "I_0p3", "I_0p5", "I_0p7", "I_0p8", "F_0x", "F_2x", "F_8x", "P_1x", "P_2x", "P_4x"],
    "main_off": ["off_B", "off_I", "off_F", "off_IF"],
    "eqcost": ["eqcost_B", "eqcost_I", "eqcost_F", "eqcost_IF"],
    "decay0": ["decay0_B", "decay0_I", "decay0_F", "decay0_IF"],
    "indep": ["indep_B", "indep_I", "indep_F"],
    "booksd": ["booksd_B", "booksd_I", "booksd_F"],
    **{f"pm2_w{w}": [f"pm2_w{w}_tau{t}" for t in ("0p1", "0p3", "0p6", "0p8")] for w in ("0p05", "0p1", "0p4")},
}
PHASE_MAP_1 = {(taste, share): name for (taste, share), name in {
    **{(t, s): f"pm1_t{tl}_s{sl}" for (t, tl), (s, sl) in product(
        ((0.0, "0"), (0.0362, "0p0362"), (0.0724, "0p0724"), (0.1448, "0p1448")),
        ((0.0, "0"), (0.2, "0p2"), (0.5, "0p5"), (0.8, "0p8")))},
    (0.0724, 0.2): "B", (0.0, 0.2): "off_B", (0.0724, 0.0): "zeroII_B"}.items()}
PHASE_MAP_2 = {(w, tau): (f"pm2_w{wl}_tau{tl}" if w != 0.2 else {"0p1": "B", "0p3": "I_0p3", "0p6": "I", "0p8": "I_0p8"}[tl])
               for (w, wl), (tau, tl) in product(((0.05, "0p05"), (0.1, "0p1"), (0.2, "0p2"), (0.4, "0p4")),
                                                 ((0.1, "0p1"), (0.3, "0p3"), (0.6, "0p6"), (0.8, "0p8")))}
A_W_OVER_A_R = 1.03  # stage B diagnosis (contract 20.6)
THRESHOLDS = (0.125, 0.25, 0.5)
CLASSES = ("real_improvement", "washing_trap", "low_low", "mixed")


def tau_star(w: float) -> float:
    return 1 - np.sqrt(w) / A_W_OVER_A_R


def classify(g: float, w: float, g_cut: float, w_cut: float) -> str:
    if g >= g_cut:
        return "mixed" if w >= w_cut else "real_improvement"
    return "washing_trap" if w >= w_cut else "low_low"


def load(run: Path) -> tuple[dict, dict]:
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    rows = {}
    for record in summary["records"]:
        rows.setdefault(record["scenario"], {})[record["seed"]] = record
    return summary, rows


def core_valid(record: dict) -> bool:
    return record["status"] == "complete" and all(
        record["validation"][gate]["status"] == "PASS" for gate in ("mechanical", "stylized"))


def wash_shares(record: dict) -> dict:
    actions = record["metrics"]["actions"]
    return {"wash": actions["wash"] / actions["decisions"], "improve": actions["improve"] / actions["decisions"],
            **{f"wash_{size}": value for size, value in actions["wash_share_by_size"].items()}}


def pipeline_checks(run: Path, summary: dict, rows: dict) -> dict:
    checks: dict = {"planned": summary["planned_trials"], "complete": summary["complete_trials"],
                    "failing_core_validation": summary["trials_failing_core_validation"]}
    windows = {(r["metrics"]["window"]["start_day"], r["metrics"]["window"]["end_day"])
               for scenario in rows.values() for r in scenario.values() if r["status"] == "complete"}
    checks["metric_windows"] = sorted(windows)
    null = [r for r in rows.get("null_control", {}).values() if r["status"] == "complete"]
    checks["null_control"] = {
        "runs": len(null),
        "any_action_in_window": any(r["metrics"]["actions"]["improve"] + r["metrics"]["actions"]["wash"] > 0 for r in null),
        "max_inflation_mean_sd": max((r["metrics"]["inflation"]["mean_sd"] for r in null), default=None),
        "max_resource_cost": max((r["metrics"]["costs"]["resource_cost"] for r in null), default=None)}
    pairing = {}
    for label, names in POLICY_SETS.items():
        mismatches = 0
        compared = 0
        seeds = sorted(set.intersection(*(set(rows.get(name, {})) for name in names)))
        for seed in seeds:
            arrays = []
            for name in names:
                record = rows[name][seed]
                if record["status"] != "complete":
                    continue
                with np.load(run / record["path"] / "result.npz") as data:
                    arrays.append((data["inflation"][:SWITCH], data["financing_rate"][:SWITCH],
                                   data["actions"][:SWITCH // 60 + 1]))
            for other in arrays[1:]:
                compared += 1
                mismatches += not all(np.array_equal(a, b) for a, b in zip(arrays[0], other))
        pairing[label] = {"pairs_compared": compared, "pairs_differing_before_switch": mismatches}
    checks["pre_switch_pairing"] = pairing
    return checks


def scenario_table(rows: dict) -> dict:
    table = {}
    for name, seeds in rows.items():
        done = [r for r in seeds.values() if r["status"] == "complete"]
        if not done:
            continue
        shares = [wash_shares(r) for r in done]
        table[name] = {
            "runs": len(done), "core_valid": sum(core_valid(r) for r in done),
            "true_change": float(np.mean([r["metrics"]["true_change"]["equal_weight_sd"] for r in done])),
            "inflation_mean": float(np.mean([r["metrics"]["inflation"]["mean_sd"] for r in done])),
            "size_gap": float(np.mean([r["metrics"]["size"]["large_minus_small_sd"] for r in done])),
            "terminal_g": float(np.mean([r["metrics"]["terminal_year"]["change_from_initial_sd"] for r in done])),
            "terminal_g_decay_adjusted": float(np.mean([r["metrics"]["terminal_year"]["decay_adjusted_from_initial_sd"] for r in done])),
            "terminal_w": float(np.mean([r["metrics"]["terminal_year"]["inflation_mean_sd"] for r in done])),
            "price_cap_runs": sum(r["validation"]["mechanical"]["status"] != "PASS" for r in done),
            **{key: float(np.mean([s[key] for s in shares])) for key in shares[0]},
        }
    return table


def phase(rows: dict, grid: dict) -> dict:
    out = {}
    for (x, y), name in grid.items():
        valid = [r for r in rows.get(name, {}).values() if core_valid(r)]
        cell = {"scenario": name, "valid_runs": len(valid),
                "excluded_runs": len(rows.get(name, {})) - len(valid), "classes": {}}
        for g_key, g_label in (("decay_adjusted_from_initial_sd", "decay_adjusted"), ("change_from_initial_sd", "original")):
            for g_cut, w_cut in product(THRESHOLDS, THRESHOLDS):
                labels = [classify(r["metrics"]["terminal_year"][g_key], r["metrics"]["terminal_year"]["inflation_mean_sd"],
                                   g_cut, w_cut) for r in valid]
                counts = {c: labels.count(c) for c in CLASSES}
                top = max(counts, key=counts.get) if labels else None
                cell["classes"][f"{g_label}_g{g_cut}_w{w_cut}"] = {
                    "counts": counts, "dominant": top if labels and counts[top] >= 0.8 * len(labels) else "uncertain"}
        out[f"{x}|{y}"] = cell
    return out


def tau_star_check(table: dict) -> list[dict]:
    rows = []
    for (w, tau), name in PHASE_MAP_2.items():
        if name not in table:
            continue
        rows.append({"w": w, "tau": tau, "tau_star": round(float(tau_star(w)), 3), "predicted_washing": bool(tau < tau_star(w)),
                     "terminal_w": table[name]["terminal_w"], "wash_share": table[name]["wash"]})
    return rows


def main(name: str) -> None:
    run = HERE / name
    summary, rows = load(run)
    table = scenario_table(rows)
    result = {
        "experiment_id": summary["experiment_id"], "purpose": summary["purpose"],
        "pipeline_checks": pipeline_checks(run, summary, rows),
        "primary": [{"name": c["name"], **{k: c["metrics"][c.get("primary_metric", "true_change.equal_weight_sd")][k]
                                           for k in ("mean", "ci_low", "ci_high", "p_value", "holm_p_value", "n")
                                           if k in c["metrics"][c.get("primary_metric", "true_change.equal_weight_sd")]},
                     "metric": c.get("primary_metric", "true_change.equal_weight_sd"),
                     "core_validation_pass": c["core_validation_pass"]}
                    for c in summary["comparisons"] if c.get("primary")],
        "secondary": {c["name"]: {metric: {k: v for k, v in c["metrics"][metric].items() if k != "paired_values"}
                                  for metric in ("true_change.equal_weight_sd", "inflation.mean_sd", "size.large_minus_small_sd")}
                      for c in summary["comparisons"] if not c.get("primary")},
        "scenarios": table,
        "phase_map_1_taste_by_share": phase(rows, PHASE_MAP_1),
        "phase_map_2_wash_cost_by_tau": phase(rows, PHASE_MAP_2),
        "tau_star_check": tau_star_check(table),
    }
    (HERE / f"{name}_analysis.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"pipeline_checks": result["pipeline_checks"], "primary": result["primary"]}, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
