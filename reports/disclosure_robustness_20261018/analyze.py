"""Robustness checks analysis (research contract 20.21). Read-only on both archives.

  python analyze.py robust_v1 [--stage-f <stage F confirmatory archive>]   # judgments, tables
  python analyze.py check_v1 --pipeline-only                                # development seeds: checks only

Writes <run>_analysis.json and <run>_tables.md next to this script (the pipeline-only mode writes
<run>_pipeline.json). Every contrast is a per-seed paired difference over the stage F confirmatory seeds
41001-41030, including contrasts against stage F scenarios; inference is the runner's paired 95% t interval,
not adjusted for multiplicity (exploratory).
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from _no_wmi import prefill_uname

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
prefill_uname()  # importing scipy.stats can block on a hung WMI service (see _no_wmi.py)
from abm.disclosure.experiments import paired_statistics  # noqa: E402
from abm.disclosure.financing import financing_signal_factors  # noqa: E402

SWITCH, PERIOD, START = 1201, 60, 1200
WINDOW_PERIODS = slice(START // PERIOD + 1, None)   # decision days in (1200, 3500]
POST_SWITCH_PERIODS = slice(SWITCH // PERIOD + 1, None)
TRUE = "true_change.equal_weight_sd"
INFLATION = "inflation.mean_sd"
REVERSIONS = {0.32: "rev0p32_", 0.5: "rev0p5_"}
POLICIES = ("B", "I", "F", "IF")
P_SCENARIOS = ("B", "I", "F", "IF", "F_0x", "F_2x", "F_8x")
W_SCENARIOS = ("B", "I_0p3", "I", "I_0p8", "F")
W_TAU = {"B": 0.1, "I_0p3": 0.3, "I": 0.6, "I_0p8": 0.8}
SETTINGS = {**{f"R{k:g}": [p + name for name in POLICIES] for k, p in REVERSIONS.items()},
            "P": ["rep_" + name for name in P_SCENARIOS], "W": ["wlog_" + name for name in W_SCENARIOS]}
WASH_LOG_SD = float(np.log(2))


# -- loading ------------------------------------------------------------------

def load(run: Path) -> tuple[dict, dict]:
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    rows: dict = {}
    for record in summary["records"]:
        rows.setdefault(record["scenario"], {})[record["seed"]] = record
    return summary, rows


def metric(record: dict, key: str) -> float:
    value = record["metrics"]
    for part in key.split("."):
        value = value[part]
    return float(value)


def complete(record: dict | None) -> bool:
    return bool(record) and record["status"] == "complete"


def core_valid(record: dict) -> bool:
    return complete(record) and all(record["validation"][gate]["status"] == "PASS" for gate in ("mechanical", "stylized"))


class Arrays:
    """Cached result arrays of completed trials (compact archives keep actions, inflation and w)."""

    def __init__(self, runs: dict[str, Path]):
        self.runs, self.cache = runs, {}

    def get(self, archive: str, record: dict) -> dict:
        key = (archive, record["scenario"], record["seed"])
        if key not in self.cache:
            with np.load(self.runs[archive] / record["path"] / "result.npz") as data:
                self.cache[key] = {name: data[name] for name in (
                    "actions", "inflation", "financing_rate", "market_price_cap_hits", "wash_cost_ratio")
                    if name in data.files}
        return self.cache[key]


def stat(values: list[float]) -> dict:
    out = paired_statistics(values, 0.95)
    return {key: out[key] for key in ("mean", "standard_error", "ci_low", "ci_high", "p_value", "n")}


def per_seed(cells: dict, plus: str, minus: str, key: str, seeds: list[int], valid_only: bool = False) -> dict:
    values = {}
    for seed in seeds:
        a, b = cells[plus].get(seed), cells[minus].get(seed)
        if complete(a) and complete(b) and (not valid_only or (core_valid(a) and core_valid(b))):
            values[seed] = metric(a, key) - metric(b, key)
    return values


def difference(a: dict, b: dict) -> dict:
    common = sorted(set(a) & set(b))
    return stat([a[s] - b[s] for s in common])


def ranking(i_f: dict, f_b: dict) -> str:
    if i_f["ci_low"] > 0 and f_b["ci_low"] > 0:
        return "holds"
    if i_f["mean"] > 0 and f_b["mean"] > 0:
        return "direction_only"
    return "not_consistent"


# -- per-run descriptions -------------------------------------------------------

def describe(arrays: Arrays, archive: str, records: list[dict]) -> dict:
    done = [r for r in records if complete(r)]
    shares, by_size, continuation, inflation, change, washing_seeds = [], {s: [] for s in ("large", "mid", "small")}, [], [], [], 0
    for r in done:
        actions = r["metrics"]["actions"]
        shares.append(actions["wash"] / actions["decisions"])
        for size, value in actions["wash_share_by_size"].items():
            by_size[size].append(value)
        washing_seeds += actions["wash"] > 0
        data = arrays.get(archive, r)
        wash = data["actions"][WINDOW_PERIODS] == 1
        stock = data["inflation"][::PERIOD][WINDOW_PERIODS] > 0
        if wash.any():
            continuation.append(float((wash & stock).sum() / wash.sum()))
        inflation.append(metric(r, INFLATION))
        change.append(metric(r, TRUE))
    return {"complete": len(done), "core_valid": sum(core_valid(r) for r in done),
            "true_change": float(np.mean(change)), "inflation_mean": float(np.mean(inflation)),
            "wash_share": float(np.mean(shares)), "wash_share_by_size": {k: float(np.mean(v)) for k, v in by_size.items()},
            "seeds_with_washing": int(washing_seeds),
            "continuation_share_of_washing": float(np.mean(continuation)) if continuation else None,
            "core_validation_failures": [
                {"scenario": r["scenario"], "seed": r["seed"], "price_cap_hits": r["validation"]["mechanical"]["price_cap_hits"],
                 "first_cap_day": first_cap_day(arrays.get(archive, r))} for r in done if not core_valid(r)]}


def first_cap_day(data: dict) -> int | None:
    hits = np.flatnonzero(data["market_price_cap_hits"])
    return int(hits[0]) if hits.size else None


# -- pipeline checks ---------------------------------------------------------------

def pipeline_checks(run: Path, summary: dict, rows: dict, arrays: Arrays) -> dict:
    seeds = summary_seeds(summary)
    windows = {(r["metrics"]["window"]["start_day"], r["metrics"]["window"]["end_day"])
               for scenario in rows.values() for r in scenario.values() if complete(r)}
    counts: Counter = Counter()
    for record in summary["records"]:
        for attempt in record["attempts"]:
            if attempt["status"] != "complete":
                manifest = run / attempt["path"] / "manifest.json"
                kind = (json.loads(manifest.read_text(encoding="utf-8")).get("error_type", "unknown")
                        if manifest.exists() else "no manifest")
                counts[f"{attempt['status']}: {kind}"] += 1
    pairing = {}
    for setting, names in SETTINGS.items():
        compared = differing = 0
        for seed in seeds:
            series = [arrays.get("new", rows[name][seed]) for name in names if complete(rows[name].get(seed))]
            series = [(d["inflation"][:SWITCH], d["financing_rate"][:SWITCH], d["actions"][:SWITCH // PERIOD + 1]) for d in series]
            for other in series[1:]:
                compared += 1
                differing += not all(np.array_equal(x, y) for x, y in zip(series[0], other))
        pairing[setting] = {"pairs_compared": compared, "pairs_differing_before_switch": differing}
    ratios = {}
    for seed in seeds:
        drawn = [arrays.get("new", rows[name][seed])["wash_cost_ratio"] for name in SETTINGS["W"] if complete(rows[name].get(seed))]
        ratios[seed] = {"identical_across_scenarios": all(np.array_equal(drawn[0], d) for d in drawn[1:]),
                        "mean": float(drawn[0].mean()), "log_sd": float(np.log(drawn[0]).std(ddof=1)),
                        "min": float(drawn[0].min()), "max": float(drawn[0].max())}
    others = [arrays.get("new", rows[name][seed]) for name in SETTINGS["R0.32"] + SETTINGS["P"]
              for seed in seeds if complete(rows[name].get(seed))]
    return {"experiment_id": summary["experiment_id"], "planned": summary["planned_trials"],
            "complete": summary["complete_trials"],
            "failed": [{"scenario": r["scenario"], "seed": r["seed"], "error": r.get("error")}
                       for r in summary["records"] if r["status"] != "complete"],
            "attempts_not_complete": dict(sorted(counts.items())),
            "failing_core_validation": summary["trials_failing_core_validation"],
            "metric_windows": sorted(windows), "pre_switch_pairing": pairing,
            "wash_cost_ratios": ratios,
            "wash_cost_ratio_absent_outside_group_W": all("wash_cost_ratio" not in d for d in others)}


def summary_seeds(summary: dict) -> list[int]:
    return sorted({r["seed"] for r in summary["records"]})


# -- groups ----------------------------------------------------------------------------

def magnitude(new: dict, low: dict, high: dict) -> dict:
    point, lo, hi = np.mean(list(new.values())), np.mean(list(low.values())), np.mean(list(high.values()))
    vs_low, vs_high = difference(new, low), difference(new, high)
    if point < lo:
        verdict = "below_lower_end" + ("_resolved" if vs_low["ci_high"] < 0 else "")
    elif point > hi:
        verdict = "above_upper_end" + ("_resolved" if vs_high["ci_low"] > 0 else "")
    else:
        verdict = "within"
    return {"verdict": verdict, "lower_end": float(lo), "upper_end": float(hi), "minus_lower_end": vs_low,
            "minus_upper_end": vs_high}


def group_r(new: dict, old: dict, arrays: Arrays, seeds: list[int]) -> dict:
    out = {}
    lower = {name: old[f"decay0_{name}"] for name in POLICIES}
    upper = {name: old[name] for name in POLICIES}
    for kappa, prefix in REVERSIONS.items():
        cells = {name: new[prefix + name] for name in POLICIES}
        contrasts, valid_only, magnitudes = {}, {}, {}
        for plus, minus in (("I", "B"), ("F", "B"), ("I", "F"), ("IF", "B")):
            label = f"{plus}_minus_{minus}"
            values = per_seed(cells, plus, minus, TRUE, seeds)
            contrasts[label] = {"true_change": stat(list(values.values())),
                                "inflation": stat(list(per_seed(cells, plus, minus, INFLATION, seeds).values()))}
            valid_only[label] = stat(list(per_seed(cells, plus, minus, TRUE, seeds, valid_only=True).values()))
            if label != "IF_minus_B":
                magnitudes[label] = magnitude(values, per_seed(lower, plus, minus, TRUE, seeds),
                                              per_seed(upper, plus, minus, TRUE, seeds))
        i_washing = sum(complete(cells["I"].get(s)) and cells["I"][s]["metrics"]["actions"]["wash"] > 0 for s in seeds)
        out[str(kappa)] = {
            "scenarios": {name: describe(arrays, "new", [cells[name].get(s) for s in seeds]) for name in POLICIES},
            "contrasts": contrasts, "contrasts_core_valid_only": valid_only,
            "R1_ranking": ranking(contrasts["I_minus_F"]["true_change"], contrasts["F_minus_B"]["true_change"]),
            "R1_ranking_core_valid_only": ranking(valid_only["I_minus_F"], valid_only["F_minus_B"]),
            "R2_magnitude": magnitudes,
            "R3_prediction": {"seeds_with_washing_under_I": int(i_washing), "seeds": len(seeds),
                              "verdict": "holds" if i_washing == len(seeds) else "fails"}}
    out["comparators"] = {
        "lower_end_decay0": {name: describe(arrays, "stage_f", [old[f"decay0_{name}"].get(s) for s in seeds]) for name in POLICIES},
        "upper_end_main": {name: describe(arrays, "stage_f", [old[name].get(s) for s in seeds]) for name in POLICIES}}
    return out


def group_p(new: dict, old: dict, arrays: Arrays, seeds: list[int]) -> dict:
    cells = {name: new["rep_" + name] for name in P_SCENARIOS}
    contrasts, valid_only = {}, {}
    for plus, minus in (("I", "B"), ("F", "B"), ("I", "F"), ("IF", "B")):
        label = f"{plus}_minus_{minus}"
        contrasts[label] = {"true_change": stat(list(per_seed(cells, plus, minus, TRUE, seeds).values())),
                            "inflation": stat(list(per_seed(cells, plus, minus, INFLATION, seeds).values()))}
        valid_only[label] = stat(list(per_seed(cells, plus, minus, TRUE, seeds, valid_only=True).values()))
    i_f = contrasts["I_minus_F"]["true_change"]
    p1 = "holds" if i_f["ci_low"] > 0 else "direction_only" if i_f["mean"] > 0 else "not_consistent"

    def ladder(source: dict) -> dict:
        steps = {"0_to_1": ("B", "F_0x"), "1_to_2": ("F_2x", "B"), "2_to_4": ("F", "F_2x"), "4_to_8": ("F_8x", "F")}
        values = {label: per_seed(source, plus, minus, TRUE, seeds) for label, (plus, minus) in steps.items()}
        wash = {name: np.mean([r["metrics"]["actions"]["wash"] / r["metrics"]["actions"]["decisions"]
                               for r in source[name].values() if complete(r)]) for name in ("F_0x", "B", "F_2x", "F", "F_8x")}
        doubling = ["1_to_2", "2_to_4", "4_to_8"]
        means = [float(np.mean(list(values[k].values()))) for k in doubling]
        successive = [difference(values[a], values[b]) for a, b in zip(doubling, doubling[1:])]
        return {"increments": {k: stat(list(v.values())) for k, v in values.items()},
                "wash_share": {k: float(v) for k, v in wash.items()},
                "wash_share_drop": {"0_to_1": float(wash["F_0x"] - wash["B"]), "1_to_2": float(wash["B"] - wash["F_2x"]),
                                    "2_to_4": float(wash["F_2x"] - wash["F"]), "4_to_8": float(wash["F"] - wash["F_8x"])},
                "doubling_increment_means": means,
                "successive_increment_differences": successive,
                "P2_verdict": "still_diminishing" if means[0] > means[1] > means[2] else "not_diminishing",
                "every_step_resolved": all(s["ci_low"] > 0 for s in successive)}

    old_cells = {name: old[name] for name in P_SCENARIOS}
    versus = {}
    for name in P_SCENARIOS:
        a = {s: r for s, r in cells[name].items() if complete(r)}
        b = {s: r for s, r in old_cells[name].items() if complete(r)}
        share = lambda r: r["metrics"]["actions"]["wash"] / r["metrics"]["actions"]["decisions"]
        versus[name] = {"wash_share": difference({s: share(r) for s, r in a.items()}, {s: share(r) for s, r in b.items()}),
                        "true_change": difference({s: metric(r, TRUE) for s, r in a.items()}, {s: metric(r, TRUE) for s, r in b.items()})}
    return {"scenarios": {name: describe(arrays, "new", [cells[name].get(s) for s in seeds]) for name in P_SCENARIOS},
            "stage_f_per_case": {name: describe(arrays, "stage_f", [old_cells[name].get(s) for s in seeds]) for name in P_SCENARIOS},
            "contrasts": contrasts, "contrasts_core_valid_only": valid_only, "P1_I_minus_F": p1,
            "P1_ranking": ranking(i_f, contrasts["F_minus_B"]["true_change"]),
            "P1_ranking_core_valid_only": ranking(valid_only["I_minus_F"], valid_only["F_minus_B"]),
            "P2_ladder_per_report": ladder(cells), "P2_ladder_per_case_stage_f": ladder(old_cells),
            "P3_per_report_minus_per_case": versus}


def threshold_ratio() -> float:
    real, _, wash, _ = financing_signal_factors(
        np.full(1, .05), decision_day=0, horizon_days=1260, repricing_interval=60, period_days=60,
        implementation_delay=120, disclosure_delay=20, audit_probability=.01, transparency=.1)
    return float(real[0] / wash[0])


def group_w(new: dict, old: dict, arrays: Arrays, seeds: list[int]) -> dict:
    cells = {name: new["wlog_" + name] for name in W_SCENARIOS}
    ratio = threshold_ratio()
    describe_rows = {name: describe(arrays, "new", [cells[name].get(s) for s in seeds]) for name in W_SCENARIOS}
    stops = {}
    for name in ("I", "I_0p8"):
        counts = [cells[name][s]["metrics"]["actions"]["wash"] for s in seeds if complete(cells[name].get(s))]
        stops[name] = {"tau": W_TAU[name], "wash_decisions_total": int(sum(counts)),
                       "seeds_with_washing": int(sum(c > 0 for c in counts)),
                       "mean_wash_share": describe_rows[name]["wash_share"],
                       "verdict": "stops" if sum(counts) == 0 else "does_not_stop"}
    eligibility = {}
    for name in ("I_0p3", "I", "I_0p8"):
        tau = W_TAU[name]
        eligible_washes = washes = 0
        eligible_firms, exceptions = [], []
        for seed in seeds:
            record = cells[name].get(seed)
            if not complete(record):
                continue
            data = arrays.get("new", record)
            firm_threshold = 1 - np.sqrt(data["wash_cost_ratio"]) * ratio
            eligible = firm_threshold > tau
            wash = data["actions"][POST_SWITCH_PERIODS] == 1
            washes += int(wash.sum())
            eligible_washes += int((wash & eligible[None, :]).sum())
            eligible_firms.append(float(eligible.mean()))
            for period, firm in np.argwhere(wash & ~eligible[None, :]):
                exceptions.append({"seed": seed, "decision_day": int((period + POST_SWITCH_PERIODS.start) * PERIOD),
                                   "firm": int(firm), "w": float(data["wash_cost_ratio"][firm]),
                                   "firm_threshold": float(firm_threshold[firm])})
        eligibility[name] = {"tau": tau, "post_switch_wash_decisions": washes,
                             "share_by_firms_with_threshold_above_tau": eligible_washes / washes if washes else None,
                             "mean_share_of_firms_with_threshold_above_tau": float(np.mean(eligible_firms)),
                             "exceptions": exceptions[:50], "exception_count": len(exceptions)}
    shares = [describe_rows[name]["wash_share"] for name in ("B", "I_0p3", "I", "I_0p8")]
    gradual = all(a > b for a, b in zip(shares, shares[1:])) and shares[2] > 0
    determined = all(e["share_by_firms_with_threshold_above_tau"] is None or e["share_by_firms_with_threshold_above_tau"] >= .99
                     for e in eligibility.values())
    contrasts, versus = {}, {}
    for plus, minus in (("I", "B"), ("F", "B"), ("I", "F"), ("I_0p3", "B"), ("I_0p8", "B")):
        contrasts[f"{plus}_minus_{minus}"] = stat(list(per_seed(cells, plus, minus, TRUE, seeds).values()))
    valid_only = {k: stat(list(per_seed(cells, *k.split("_minus_"), TRUE, seeds, valid_only=True).values()))
                  for k in ("I_minus_F", "F_minus_B")}
    homogeneous = {name: old[name] for name in W_SCENARIOS}
    for name in W_SCENARIOS:
        share = lambda r: r["metrics"]["actions"]["wash"] / r["metrics"]["actions"]["decisions"]
        a = {s: r for s, r in cells[name].items() if complete(r)}
        b = {s: r for s, r in homogeneous[name].items() if complete(r)}
        versus[name] = {"wash_share": difference({s: share(r) for s, r in a.items()}, {s: share(r) for s, r in b.items()}),
                        "true_change": difference({s: metric(r, TRUE) for s, r in a.items()}, {s: metric(r, TRUE) for s, r in b.items()})}
    for plus in ("I", "I_0p3", "I_0p8", "F"):
        new_effect = per_seed(cells, plus, "B", TRUE, seeds)
        old_effect = per_seed(homogeneous, plus, "B", TRUE, seeds)
        versus[name_effect(plus)] = difference(new_effect, old_effect)
    return {"threshold_ratio_A_r_over_A_w": ratio, "scenarios": describe_rows,
            "stage_f_homogeneous": {name: describe(arrays, "stage_f", [homogeneous[name].get(s) for s in seeds]) for name in W_SCENARIOS},
            "W1_stop_above_threshold": {**stops, "verdict": "holds" if all(s["verdict"] == "stops" for s in stops.values()) else "fails"},
            "W2_gradual": {"mean_wash_shares_B_0p3_0p6_0p8": shares, "gradual": gradual, "eligibility": eligibility,
                           "determined_by_firms_with_threshold_above_tau": determined},
            "W3_contrasts": contrasts, "W3_contrasts_core_valid_only": valid_only,
            "W3_ranking": ranking(contrasts["I_minus_F"], contrasts["F_minus_B"]),
            "W3_ranking_core_valid_only": ranking(valid_only["I_minus_F"], valid_only["F_minus_B"]),
            "W3_heterogeneous_minus_homogeneous": versus}


def name_effect(plus: str) -> str:
    return f"effect_{plus}_minus_B"


# -- tables -------------------------------------------------------------------------------

def fmt(value: float, digits: int = 3) -> str:
    return f"{value:+.{digits}f}".replace("-", "−")


def interval(s: dict, digits: int = 3) -> str:
    return f"{fmt(s['mean'], digits)} [{fmt(s['ci_low'], digits)}, {fmt(s['ci_high'], digits)}]"


RANKING = {"holds": "成立", "direction_only": "仅点估计成立", "not_consistent": "不成立"}
MAGNITUDE = {"within": "区间内", "below_lower_end": "低于下端", "below_lower_end_resolved": "可分辨地低于下端",
             "above_upper_end": "高于上端", "above_upper_end_resolved": "可分辨地高于上端"}


def tables(result: dict) -> list[str]:
    r, p, w = result["R"], result["P"], result["W"]
    out = ["# 稳健性补充表格（robust_v1）", "", f"experiment_id `{result['pipeline_checks']['experiment_id']}`", "",
           "## R 组：向截面均值回归（政策窗口真实变化，SD，配对 95% t 区间）", "",
           "| 设定 | I − B | F − B | I − F | IF − B | R1 排序 |", "|---|---|---|---|---|---|"]
    for kappa in ("0.32", "0.5"):
        c = r[kappa]["contrasts"]
        out.append(f"| κ = {kappa} | " + " | ".join(interval(c[k]["true_change"]) for k in ("I_minus_B", "F_minus_B", "I_minus_F", "IF_minus_B"))
                   + f" | {RANKING[r[kappa]['R1_ranking']]} |")
    out += ["", "R2：与统一衰减区间的比较（点估计；括号内为与该端点的逐种子配对差）", "",
            "| κ | 对比 | 下端（0） | 上端（0.2） | 回归 | 减下端 | 减上端 | 判定 |", "|---|---|---:|---:|---:|---|---|---|"]
    for kappa in ("0.32", "0.5"):
        for label, m in r[kappa]["R2_magnitude"].items():
            point = r[kappa]["contrasts"][label]["true_change"]["mean"]
            out.append(f"| {kappa} | {label.replace('_minus_', ' − ')} | {fmt(m['lower_end'])} | {fmt(m['upper_end'])} | {fmt(point)} | "
                       f"{interval(m['minus_lower_end'])} | {interval(m['minus_upper_end'])} | {MAGNITUDE[m['verdict']]} |")
    out += ["", "描述：政策窗口漂绿决策占比、平均虚报与真实变化", "",
            "| 设定 | B 漂绿 | I 漂绿 | F 漂绿 | IF 漂绿 | B 平均虚报 | B 真实变化 | B 中继续已有案件的漂绿 | I 中有漂绿的种子 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    rows = [("统一衰减 0", r["comparators"]["lower_end_decay0"]), ("统一衰减 0.2", r["comparators"]["upper_end_main"])]
    rows += [(f"κ = {k}", r[k]["scenarios"]) for k in ("0.32", "0.5")]
    for label, s in rows:
        cont = s["B"]["continuation_share_of_washing"]
        out.append(f"| {label} | " + " | ".join(f"{s[n]['wash_share']:.1%}" for n in POLICIES) +
                   f" | {s['B']['inflation_mean']:.3f} | {fmt(s['B']['true_change'])} | {'—' if cont is None else f'{cont:.0%}'} | {s['I']['seeds_with_washing']}/30 |")
    out += ["", "## P 组：每份虚假报告各罚一笔", "",
            "| 对比 | 按报告计罚 | 一案一罚（阶段 F） |", "|---|---|---|"]
    stage_f = result["P_stage_f_contrasts"]
    for k in ("I_minus_B", "F_minus_B", "I_minus_F", "IF_minus_B"):
        out.append(f"| {k.replace('_minus_', ' − ')} | {interval(p['contrasts'][k]['true_change'])} | {interval(stage_f[k])} |")
    out.append(f"| P1 I > F | {RANKING[p['P1_I_minus_F']]}；排序 {RANKING[p['P1_ranking']]} | |")
    out += ["", "剂量梯度（真实变化增量，SD；漂绿决策占比）", "",
            "| 记账 | 0× 漂绿 | 1× | 2× | 4× | 8× | 0→1 | 1→2 | 2→4 | 4→8 | P2 |", "|---|---:|---:|---:|---:|---:|---|---|---|---|---|"]
    for label, ladder in (("按报告", p["P2_ladder_per_report"]), ("一案一罚", p["P2_ladder_per_case_stage_f"])):
        ws = ladder["wash_share"]
        out.append(f"| {label} | " + " | ".join(f"{ws[n]:.1%}" for n in ("F_0x", "B", "F_2x", "F", "F_8x")) + " | " +
                   " | ".join(interval(ladder["increments"][k]) for k in ("0_to_1", "1_to_2", "2_to_4", "4_to_8")) +
                   f" | {'仍递减' if ladder['P2_verdict'] == 'still_diminishing' else '不再递减'}"
                   f"{'，逐段可分辨' if ladder['every_step_resolved'] else ''} |")
    out += ["", "P3：按报告减一案一罚（同名场景，逐种子配对）", "",
            "| 场景 | 漂绿占比差 | 真实变化差 | 继续已有案件的漂绿（按报告 / 一案一罚） | 大 / 中 / 小企业漂绿（按报告） |", "|---|---|---|---|---|"]
    for name in P_SCENARIOS:
        v, a, b = p["P3_per_report_minus_per_case"][name], p["scenarios"][name], p["stage_f_per_case"][name]
        pct = lambda x: "—" if x is None else f"{x:.0%}"
        size = a["wash_share_by_size"]
        out.append(f"| {name} | {interval(v['wash_share'])} | {interval(v['true_change'])} | "
                   f"{pct(a['continuation_share_of_washing'])} / {pct(b['continuation_share_of_washing'])} | "
                   f"{size['large']:.0%} / {size['mid']:.0%} / {size['small']:.0%} |")
    out += ["", "## W 组：异质漂绿成本比例（σ = ln 2）", "",
            "| 场景 | τ | 漂绿占比（异质 / w = 0.2） | 有漂绿的种子 | 门槛高于 τ 的企业比例 | 切换后漂绿中来自这些企业的比例 | 相对 B 的真实变化（异质） | 异质减同质 |",
            "|---|---:|---|---:|---:|---:|---|---|"]
    for name in ("B", "I_0p3", "I", "I_0p8"):
        s, h = w["scenarios"][name], w["stage_f_homogeneous"][name]
        e = w["W2_gradual"]["eligibility"].get(name)
        effect = w["W3_contrasts"].get(f"{name}_minus_B")
        delta = w["W3_heterogeneous_minus_homogeneous"].get(name_effect(name))
        out.append(f"| {name} | {W_TAU[name]:g} | {s['wash_share']:.1%} / {h['wash_share']:.1%} | {s['seeds_with_washing']}/30 | "
                   f"{'—' if e is None else format(e['mean_share_of_firms_with_threshold_above_tau'], '.1%')} | "
                   f"{'—' if e is None or e['share_by_firms_with_threshold_above_tau'] is None else format(e['share_by_firms_with_threshold_above_tau'], '.1%')} | "
                   f"{'—' if effect is None else interval(effect)} | {'—' if delta is None else interval(delta)} |")
    out += ["", f"W1：{'仍成立' if w['W1_stop_above_threshold']['verdict'] == 'holds' else '不成立'}；"
            f"W2 渐进下降：{'是' if w['W2_gradual']['gradual'] else '否'}；由门槛高于 τ 的企业决定："
            f"{'是' if w['W2_gradual']['determined_by_firms_with_threshold_above_tau'] else '否'}", "",
            "| W3 对比 | 异质 w | w = 0.2（阶段 F） |", "|---|---|---|"]
    for k in ("I_minus_B", "F_minus_B", "I_minus_F"):
        out.append(f"| {k.replace('_minus_', ' − ')} | {interval(w['W3_contrasts'][k])} | {interval(result['W_stage_f_contrasts'][k])} |")
    out.append(f"| 排序 I > F > B | {RANKING[w['W3_ranking']]} | |")
    out += ["", "## 核心验证未通过的运行", "", "| 场景 | 种子 | 截断次数 | 首次截断日 |", "|---|---:|---:|---:|"]
    for f in result["core_validation_failures"]:
        out.append(f"| {f['scenario']} | {f['seed']} | {f['price_cap_hits']} | {f['first_cap_day'] if f['first_cap_day'] is not None else '—'} |")
    out += ["", "剔除核心验证失败的种子后：", "",
            f"- R1：κ = 0.32 {RANKING[r['0.32']['R1_ranking_core_valid_only']]}，κ = 0.5 {RANKING[r['0.5']['R1_ranking_core_valid_only']]}",
            f"- P1 排序：{RANKING[p['P1_ranking_core_valid_only']]}（I − F {interval(p['contrasts_core_valid_only']['I_minus_F'])}，n = {p['contrasts_core_valid_only']['I_minus_F']['n']}）",
            f"- W3 排序：{RANKING[w['W3_ranking_core_valid_only']]}"]
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run")
    parser.add_argument("--stage-f", type=Path, default=ROOT / "reports" / "disclosure_stage_f_20261014" / "confirmatory_v1")
    parser.add_argument("--pipeline-only", action="store_true")
    args = parser.parse_args()
    run = HERE / args.run
    summary, rows = load(run)
    arrays = Arrays({"new": run, "stage_f": args.stage_f})
    checks = pipeline_checks(run, summary, rows, arrays)
    if args.pipeline_only:
        (HERE / f"{args.run}_pipeline.json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(json.dumps({k: v for k, v in checks.items() if k != "wash_cost_ratios"}, indent=2))
        return
    seeds = summary_seeds(summary)
    assert seeds == list(range(41001, 41031))
    stage_f_summary, old = load(args.stage_f)
    result = {"pipeline_checks": checks, "stage_f_experiment_id": stage_f_summary["experiment_id"],
              "R": group_r(rows, old, arrays, seeds), "P": group_p(rows, old, arrays, seeds),
              "W": group_w(rows, old, arrays, seeds)}
    result["P_stage_f_contrasts"] = {f"{a}_minus_{b}": stat(list(per_seed(old, a, b, TRUE, seeds).values()))
                                     for a, b in (("I", "B"), ("F", "B"), ("I", "F"), ("IF", "B"))}
    result["W_stage_f_contrasts"] = {f"{a}_minus_{b}": stat(list(per_seed(old, a, b, TRUE, seeds).values()))
                                     for a, b in (("I", "B"), ("F", "B"), ("I", "F"))}
    result["core_validation_failures"] = sorted(
        [{"scenario": r["scenario"], "seed": r["seed"], "price_cap_hits": r["validation"]["mechanical"]["price_cap_hits"],
          "first_cap_day": first_cap_day(arrays.get("new", r))}
         for scenario in rows.values() for r in scenario.values() if complete(r) and not core_valid(r)],
        key=lambda f: (f["scenario"], f["seed"]))
    result["inference"] = ("Paired 95% t intervals across the 30 seeds; no multiplicity adjustment (exploratory). "
                           "All completed runs are used; core-validation failures are kept and reported separately.")
    (HERE / f"{args.run}_analysis.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                                                    encoding="utf-8", newline="\n")
    (HERE / f"{args.run}_tables.md").write_text("\n".join(tables(result)) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"pipeline": {k: checks[k] for k in ("planned", "complete", "failing_core_validation", "pre_switch_pairing")},
                      "R1": {k: result["R"][k]["R1_ranking"] for k in ("0.32", "0.5")},
                      "P1": result["P"]["P1_I_minus_F"], "P2": result["P"]["P2_ladder_per_report"]["P2_verdict"],
                      "W1": result["W"]["W1_stop_above_threshold"]["verdict"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
