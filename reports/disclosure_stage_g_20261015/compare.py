"""Stage G.3(b): the cost of simplification. Simplified dynamics against the full stage F model.

  .venv/Scripts/python.exe reports/disclosure_stage_g_20261015/compare.py

For B, I, F and IF with uniform natural decay 0 and 0.2 SD/year, the sandbox's simplified dynamics
(showcase/sandbox/reference.py: the 200 snapshot firms, B and market cap fixed, no investor market)
run 30 audit seeds. They are set against two full-model references: the same seed (51001) and the
same firms (full_model_seed51001.json), and the stage F confirmatory means over seeds 41001-41030.
The decay-0 scenarios of the full model have no decay from day 0; so do the simplified runs, which
apply the chosen decay to all 14 years. Metrics follow stage F: days 1200-3500, decisions in
(1200, 3500].

Writes showcase/data/simplification.json and simplification_tables.md next to this script.
"""

from __future__ import annotations

import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "showcase" / "sandbox"))

from abm.platform_tuning import disable_power_throttling  # noqa: E402
from reference import domain_from, firms_from, schedule_from, simulate, window_metrics  # noqa: E402

F1 = 4.5614908036639594e-05
AUDIT_SEEDS = list(range(1, 31))
POLICIES = {"B": {}, "I": {"transparency": 0.6}, "F": {"fixed_fine": 4 * F1}, "IF": {"transparency": 0.6, "fixed_fine": 4 * F1}}
DECAYS = {"0.2": 0.2, "0": 0.0}
METRICS = ("true_change_sd", "wash_share", "inflation_mean_sd")


def schedule(baseline: dict, changes: dict) -> dict:
    if not changes:
        return {"baseline": baseline, "intervention": None, "start_day": 0}
    return {"baseline": baseline, "intervention": {**baseline, **changes}, "start_day": 1201}


def run(policy: str, decay: float, seed: int) -> tuple[str, float, int, dict]:
    disable_power_throttling()
    sandbox = json.loads((ROOT / "showcase" / "data" / "sandbox_firms.json").read_text(encoding="utf-8"))
    payload = sandbox["domains"]["esg"]
    firms = firms_from(payload["firms"])
    baseline = {**payload["baseline_policy"], "disclosure_delay_days": None}
    result = simulate(firms, domain_from(payload), schedule_from(schedule(baseline, POLICIES[policy])),
                      natural_decay=decay, audit_seed=seed)
    return policy, decay, seed, window_metrics(result, firms)


def summary(values: list[float]) -> dict:
    array = np.asarray(values)
    return {"mean": float(array.mean()), "min": float(array.min()), "max": float(array.max())}


def main() -> None:
    disable_power_throttling()
    jobs = [(policy, decay, seed) for policy in POLICIES for decay in DECAYS.values() for seed in AUDIT_SEEDS]
    with ProcessPoolExecutor(max_workers=12, initializer=disable_power_throttling) as pool:
        results = list(pool.map(run, *zip(*jobs)))
    simplified: dict = {}
    for policy, decay, seed, metrics in results:
        simplified.setdefault((policy, decay), []).append(metrics)
    full = json.loads((HERE / "full_model_seed51001.json").read_text(encoding="utf-8"))["runs"]
    stage_f = json.loads((ROOT / "showcase" / "data" / "stage_f.json").read_text(encoding="utf-8"))
    stage_keys = {"true_change_sd": "true_change", "wash_share": "wash", "inflation_mean_sd": "inflation_mean"}

    rows = {}
    for label, decay in DECAYS.items():
        prefix = "" if decay else "decay0_"
        for policy in POLICIES:
            runs = simplified[(policy, decay)]
            rows[f"{label}|{policy}"] = {
                "policy": policy, "natural_decay": decay,
                "simplified": {key: summary([m[key] for m in runs]) for key in METRICS},
                "full_same_seed": {key: full[prefix + policy]["metrics"][key] for key in METRICS},
                "stage_f_mean": {key: stage_f["scenarios"][prefix + policy][stage_keys[key]] for key in METRICS},
            }
    contrasts = {}
    for label, decay in DECAYS.items():
        prefix = "" if decay else "decay0_"
        for plus, minus in (("I", "B"), ("F", "B"), ("I", "F")):
            name = f"{plus}_minus_{minus}"
            paired = [a["true_change_sd"] - b["true_change_sd"]
                      for a, b in zip(simplified[(plus, decay)], simplified[(minus, decay)])]
            stage_name = f"{prefix}{name}"
            if stage_name in stage_f["secondary"]:
                reference = stage_f["secondary"][stage_name]
            elif name == "I_minus_F" and not decay:
                reference = stage_f["secondary"]["decay0_I_minus_F"]
            else:  # I - F with decay: the primary contrast P2
                p2 = next(row for row in stage_f["primary"] if row["name"] == "P2_I_minus_F")
                reference = {key: p2[key] for key in ("mean", "ci_low", "ci_high", "n")}
            contrasts[f"{label}|{name}"] = {
                "natural_decay": decay, "contrast": name, "simplified": summary(paired),
                "full_same_seed": full[prefix + plus]["metrics"]["true_change_sd"] - full[prefix + minus]["metrics"]["true_change_sd"],
                "stage_f": reference,
            }
    payload = {
        "schema_version": 1, "generated_by": "reports/disclosure_stage_g_20261015/compare.py",
        "audit_seeds": f"{AUDIT_SEEDS[0]}-{AUDIT_SEEDS[-1]}", "full_model_seed": 51001,
        "metric_window": [1200, 3500], "rows": rows, "contrasts": contrasts,
        "note": "Simplified: sandbox dynamics on the 200 snapshot firms, mean (min-max) over 30 audit seeds. "
                "Full same seed: one full-model run per scenario with the same firms. Stage F: mean over 30 seeds.",
    }
    out = ROOT / "showcase" / "data" / "simplification.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1, allow_nan=False) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {out.relative_to(ROOT).as_posix()}")

    lines = ["# 简化的代价：沙盘简化动态与完整模型", "",
             "由 compare.py 生成。简化：沙盘动态，200 家快照企业，30 个核查种子的均值（括号内为范围）。"
             "完整（同种子）：同一批企业的完整模型，每个场景一次运行。阶段 F：确认性实验 30 个种子的均值。"
             "窗口为第 1200–3500 日。", "",
             "| 衰减 | 场景 | 真实变化：简化 | 完整（同种子） | 阶段 F | 漂绿占比：简化 | 完整 | 阶段 F | 平均虚报：简化 | 完整 | 阶段 F |",
             "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for row in rows.values():
        s, f, g = row["simplified"], row["full_same_seed"], row["stage_f_mean"]
        lines.append(f"| {row['natural_decay']:g} | {row['policy']} | {s['true_change_sd']['mean']:+.3f} | {f['true_change_sd']:+.3f} "
                     f"| {g['true_change_sd']:+.3f} | {s['wash_share']['mean']:.1%} | {f['wash_share']:.1%} | {g['wash_share']:.1%} "
                     f"| {s['inflation_mean_sd']['mean']:.2f} | {f['inflation_mean_sd']:.2f} | {g['inflation_mean_sd']:.2f} |")
    lines += ["", "政策效应（真实变化，SD）：", "",
              "| 衰减 | 对比 | 简化：均值（30 个核查种子的范围） | 完整（同种子） | 阶段 F [95% 区间] |",
              "|---|---|---:|---:|---:|"]
    for row in contrasts.values():
        s, r = row["simplified"], row["stage_f"]
        lines.append(f"| {row['natural_decay']:g} | {row['contrast'].replace('_minus_', ' − ')} "
                     f"| {s['mean']:+.3f}（{s['min']:+.3f} 到 {s['max']:+.3f}） | {row['full_same_seed']:+.3f} "
                     f"| {r['mean']:+.3f} [{r['ci_low']:+.3f}, {r['ci_high']:+.3f}] |")
    tables = HERE / "simplification_tables.md"
    tables.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {tables.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
