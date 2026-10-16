"""Decay grid analysis (research contract 20.16). Read-only on both grid directories.

  python analyze.py    # writes grid_v1_analysis.json and grid_v1_tables.md next to this script

Five uniform natural-decay grid points: 0 (stage F block E, decay0_*), 0.05, 0.1, 0.15 (this grid) and 0.2
(stage F main setting, B/I/F/IF). All five share the stage F confirmatory seeds 41001-41030, so every contrast,
including the change of a contrast between two grid points, is a per-seed paired difference. Inference is the
runner's paired 95% t interval; nothing is adjusted for multiplicity (exploratory, contract 20.16).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from abm.disclosure.experiments import paired_statistics  # noqa: E402

STAGE_F = ROOT / "reports" / "disclosure_stage_f_20261014" / "confirmatory_v1"
GRID = HERE / "grid_v1"
SWITCH = 1201
POLICIES = ("B", "I", "F", "IF")
# Grid point -> (archive, scenario prefix). The 0.2 point is the stage F main setting.
POINTS = {0.0: (STAGE_F, "decay0_"), 0.05: (GRID, "decay0p05_"), 0.1: (GRID, "decay0p1_"),
          0.15: (GRID, "decay0p15_"), 0.2: (STAGE_F, "")}
JUDGED = (("I", "B"), ("F", "B"), ("I", "F"))   # contract 20.16: ranking and monotonicity are judged on these
DESCRIBED = (("IF", "B"),)
METRICS = {"true_change": "true_change.equal_weight_sd", "inflation": "inflation.mean_sd"}


def metric(record: dict, key: str) -> float:
    value = record["metrics"]
    for part in key.split("."):
        value = value[part]
    return float(value)


def load(run: Path) -> tuple[dict, dict]:
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    rows: dict = {}
    for record in summary["records"]:
        rows.setdefault(record["scenario"], {})[record["seed"]] = record
    return summary, rows


def core_valid(record: dict) -> bool:
    return record["status"] == "complete" and all(
        record["validation"][gate]["status"] == "PASS" for gate in ("mechanical", "stylized"))


def first_cap_day(run: Path, record: dict) -> int | None:
    with np.load(run / record["path"] / "result.npz") as data:
        hits = np.flatnonzero(data["market_price_cap_hits"])
    return int(hits[0]) if hits.size else None


def stat(values: list[float]) -> dict:
    out = paired_statistics(values, 0.95)
    return {key: out[key] for key in ("mean", "standard_error", "ci_low", "ci_high", "p_value", "n")}


def contrast(cells: dict, plus: str, minus: str, key: str, seeds: list[int], valid_only: bool = False) -> tuple[dict, dict]:
    values = {}
    for seed in seeds:
        a, b = cells[plus].get(seed), cells[minus].get(seed)
        if not (a and b and a["status"] == "complete" and b["status"] == "complete"):
            continue
        if valid_only and not (core_valid(a) and core_valid(b)):
            continue
        values[seed] = metric(a, key) - metric(b, key)
    return stat(list(values.values())), values


def ranking(stats: dict) -> str:
    i_f, f_b = stats["I_minus_F"], stats["F_minus_B"]
    if i_f["ci_low"] > 0 and f_b["ci_low"] > 0:
        return "holds"            # I > F > B, both adjacent intervals above 0 (I - B > 0 follows)
    if i_f["mean"] > 0 and f_b["mean"] > 0:
        return "direction_only"   # point estimates in order, at least one interval includes 0
    return "not_consistent"


def main() -> None:
    grid_summary, grid_rows = load(GRID)
    stage_f_summary, stage_f_rows = load(STAGE_F)
    archives = {GRID: grid_rows, STAGE_F: stage_f_rows}
    seeds = sorted({r["seed"] for r in grid_summary["records"]})
    assert seeds == list(range(41001, 41031))

    # Pipeline checks on the new grid only (the endpoints were checked in stage F, contract 20.13).
    windows = {(r["metrics"]["window"]["start_day"], r["metrics"]["window"]["end_day"])
               for scenario in grid_rows.values() for r in scenario.values() if r["status"] == "complete"}
    pairing = {}
    for point, (run, prefix) in POINTS.items():
        if run is not GRID:
            continue
        compared = differing = 0
        for seed in seeds:
            arrays = []
            for name in POLICIES:
                record = grid_rows[prefix + name][seed]
                if record["status"] != "complete":
                    continue
                with np.load(GRID / record["path"] / "result.npz") as data:
                    arrays.append((data["inflation"][:SWITCH], data["financing_rate"][:SWITCH],
                                   data["actions"][:SWITCH // 60 + 1]))
            for other in arrays[1:]:
                compared += 1
                differing += not all(np.array_equal(x, y) for x, y in zip(arrays[0], other))
        pairing[str(point)] = {"pairs_compared": compared, "pairs_differing_before_switch": differing}
    checks = {"experiment_id": grid_summary["experiment_id"], "stage_f_experiment_id": stage_f_summary["experiment_id"],
              "planned": grid_summary["planned_trials"], "complete": grid_summary["complete_trials"],
              "failed": [{"scenario": r["scenario"], "seed": r["seed"], "error": r.get("error")}
                         for r in grid_summary["records"] if r["status"] != "complete"],
              "failing_core_validation": grid_summary["trials_failing_core_validation"],
              "metric_windows": sorted(windows), "pre_switch_pairing": pairing}

    points = {}
    for point, (run, prefix) in POINTS.items():
        cells = {name: archives[run][prefix + name] for name in POLICIES}
        scenarios = {}
        for name in POLICIES:
            done = [cells[name][s] for s in seeds if cells[name].get(s, {}).get("status") == "complete"]
            invalid = [r for r in done if not core_valid(r)]
            decisions = [r["metrics"]["actions"] for r in done]
            scenarios[name] = {
                "scenario": prefix + name, "complete": len(done), "core_valid": len(done) - len(invalid),
                "true_change": float(np.mean([metric(r, METRICS["true_change"]) for r in done])),
                "inflation_mean": float(np.mean([metric(r, METRICS["inflation"]) for r in done])),
                "wash_share": float(np.mean([a["wash"] / a["decisions"] for a in decisions])),
                "improve_share": float(np.mean([a["improve"] / a["decisions"] for a in decisions])),
                "core_validation_failures": [
                    {"seed": r["seed"], "mechanical": r["validation"]["mechanical"]["status"],
                     "stylized": r["validation"]["stylized"]["status"],
                     "price_cap_hits": r["validation"]["mechanical"]["price_cap_hits"],
                     "first_cap_day": first_cap_day(run, r)} for r in invalid],
            }
        contrasts, valid_only, per_seed = {}, {}, {}
        for plus, minus in JUDGED + DESCRIBED:
            label = f"{plus}_minus_{minus}"
            contrasts[label] = {}
            for short, key in METRICS.items():
                contrasts[label][short], values = contrast(cells, plus, minus, key, seeds)
                if short == "true_change":
                    per_seed[label] = values
            valid_only[label], _ = contrast(cells, plus, minus, METRICS["true_change"], seeds, valid_only=True)
            contrasts[label]["core_validation_pass"] = all(
                core_valid(cells[name][s]) for name in (plus, minus) for s in seeds)
        points[str(point)] = {"scenarios": scenarios, "contrasts": contrasts,
                              "contrasts_core_valid_only": valid_only,
                              "ranking": ranking({k: v["true_change"] for k, v in contrasts.items()}),
                              "ranking_core_valid_only": ranking(valid_only), "_per_seed": per_seed}

    # Monotonicity (contract 20.16): change of each judged contrast between adjacent grid points, paired by seed.
    order = sorted(POINTS)
    monotonic = {}
    for plus, minus in JUDGED:
        label = f"{plus}_minus_{minus}"
        steps = []
        for low, high in zip(order, order[1:]):
            a, b = points[str(high)]["_per_seed"][label], points[str(low)]["_per_seed"][label]
            common = sorted(set(a) & set(b))
            steps.append({"from": low, "to": high, **stat([a[s] - b[s] for s in common])})
        signs = {np.sign(step["mean"]) for step in steps}
        monotonic[label] = {
            "means": [points[str(p)]["contrasts"][label]["true_change"]["mean"] for p in order], "steps": steps,
            "monotone": len(signs) == 1 and 0 not in signs,
            "direction": "increasing" if signs == {1.0} else "decreasing" if signs == {-1.0} else "mixed",
            "every_step_resolved": all(step["ci_low"] > 0 or step["ci_high"] < 0 for step in steps)}
    for point in points.values():
        del point["_per_seed"]

    result = {"pipeline_checks": checks, "grid_points": order, "points": points, "monotonicity": monotonic,
              "inference": "Paired 95% t intervals across the 30 seeds; no multiplicity adjustment (exploratory). "
                           "All completed runs are used; core-validation failures are kept and reported separately."}
    (HERE / "grid_v1_analysis.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                                                encoding="utf-8", newline="\n")
    (HERE / "grid_v1_tables.md").write_text("\n".join(tables(result)) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"pipeline_checks": checks,
                      "ranking": {p: points[p]["ranking"] for p in points},
                      "monotonicity": {k: {x: v[x] for x in ("monotone", "direction", "every_step_resolved")}
                                       for k, v in monotonic.items()}}, indent=2))


def fmt(value: float, digits: int = 3) -> str:
    return f"{value:+.{digits}f}".replace("-", "−")


def interval(s: dict, digits: int = 3) -> str:
    return f"{fmt(s['mean'], digits)} [{fmt(s['ci_low'], digits)}, {fmt(s['ci_high'], digits)}]"


def tables(result: dict) -> list[str]:
    order, points = result["grid_points"], result["points"]
    source = {0.0: "阶段 F E 块", 0.05: "本补充", 0.1: "本补充", 0.15: "本补充", 0.2: "阶段 F 主设定"}
    ranking_names = {"holds": "成立", "direction_only": "仅点估计成立", "not_consistent": "不成立"}
    out = ["# 衰减格点表格（grid_v1）", "", f"experiment_id `{result['pipeline_checks']['experiment_id']}`", "",
           "## 真实变化的对比（第 1200–3500 日，SD，配对 95% t 区间，未校正）", "",
           "| 衰减（SD/年） | 来源 | I − B | F − B | I − F | IF − B | 排序 I > F > B |",
           "|---:|---|---|---|---|---|---|"]
    for p in order:
        c = points[str(p)]["contrasts"]
        out.append(f"| {p:g} | {source[p]} | " + " | ".join(interval(c[k]["true_change"]) for k in (
            "I_minus_B", "F_minus_B", "I_minus_F", "IF_minus_B")) + f" | {ranking_names[points[str(p)]['ranking']]} |")
    out += ["", "## 基准场景与平均虚报", "",
            "| 衰减 | B 漂绿占比 | F 漂绿占比 | I 漂绿占比 | B 平均虚报（SD） | B 真实变化（SD） | I − B 平均虚报（SD） |",
            "|---:|---:|---:|---:|---:|---:|---|"]
    for p in order:
        s, c = points[str(p)]["scenarios"], points[str(p)]["contrasts"]
        out.append(f"| {p:g} | {s['B']['wash_share']:.1%} | {s['F']['wash_share']:.1%} | {s['I']['wash_share']:.1%} | "
                   f"{s['B']['inflation_mean']:.3f} | {fmt(s['B']['true_change'])} | {interval(c['I_minus_B']['inflation'])} |")
    out += ["", "## 相邻格点之间对比的变化（按种子配对）", "", "| 对比 | 0 → 0.05 | 0.05 → 0.1 | 0.1 → 0.15 | 0.15 → 0.2 | 单调 |",
            "|---|---|---|---|---|---|"]
    for label, row in result["monotonicity"].items():
        verdict = ("是，递增" if row["direction"] == "increasing" else "是，递减" if row["direction"] == "decreasing"
                   else "否") + ("，每段区间都不含 0" if row["every_step_resolved"] else "")
        out.append(f"| {label.replace('_minus_', ' − ')} | " + " | ".join(interval(s) for s in row["steps"]) + f" | {verdict} |")
    out += ["", "## 核心验证", "", "| 衰减 | 场景 | 种子 | 机械 | 风格事实 | 截断次数 | 首次截断日 |", "|---:|---|---:|---|---|---:|---:|"]
    for p in order:
        for name, s in points[str(p)]["scenarios"].items():
            for f in s["core_validation_failures"]:
                out.append(f"| {p:g} | {s['scenario']} | {f['seed']} | {f['mechanical']} | {f['stylized']} | "
                           f"{f['price_cap_hits']} | {f['first_cap_day'] if f['first_cap_day'] is not None else '—'} |")
    out += ["", "## 剔除核心验证失败的种子后（真实变化）", "", "| 衰减 | I − B | F − B | I − F | 排序 |", "|---:|---|---|---|---|"]
    for p in order:
        v = points[str(p)]["contrasts_core_valid_only"]
        out.append(f"| {p:g} | " + " | ".join(f"{interval(v[k])}（n = {v[k]['n']}）" for k in (
            "I_minus_B", "F_minus_B", "I_minus_F")) + f" | {ranking_names[points[str(p)]['ranking_core_valid_only']]} |")
    return out


if __name__ == "__main__":
    main()
