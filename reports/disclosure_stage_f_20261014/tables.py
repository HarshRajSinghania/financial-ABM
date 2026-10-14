"""Stage F: turn <run>_analysis.json and the grid's summary.json into the markdown tables of the report.

  python tables.py confirmatory_v1   # writes confirmatory_v1_tables.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAMES = {"real_improvement": "真实改善", "washing_trap": "漂绿陷阱", "low_low": "低改善低虚报",
         "mixed": "混合", "uncertain": "不确定"}


def fmt(value, digits=3, sign=True):
    if value is None:
        return "—"
    return f"{value:+.{digits}f}" if sign else f"{value:.{digits}f}"


def interval(stat: dict, digits=3) -> str:
    if stat.get("status") != "complete":
        return "不完整"
    return f"{fmt(stat['mean'], digits)} [{fmt(stat['ci_low'], digits)}, {fmt(stat['ci_high'], digits)}]"


def scenario_rows(table: dict, names: list[str], label=None) -> list[str]:
    lines = ["| 场景 | 真实变化（SD） | 漂绿决策占比 | 大 / 中 / 小企业漂绿占比 | 平均虚报（SD） | 大减小真实变化 | 核心验证通过 |",
             "|---|---:|---:|---|---:|---:|---:|"]
    for name in names:
        row = table[name]
        lines.append(f"| {label(name) if label else name} | {fmt(row['true_change'])} | {row['wash']:.1%} | "
                     f"{row['wash_large']:.0%} / {row['wash_mid']:.0%} / {row['wash_small']:.0%} | "
                     f"{row['inflation_mean']:.2f} | {fmt(row['size_gap'])} | {row['core_valid']}/{row['runs']} |")
    return lines


def phase_rows(cells: dict, x_name: str, y_name: str, key: str) -> list[str]:
    xs = sorted({float(k.split("|")[0]) for k in cells})
    ys = sorted({float(k.split("|")[1]) for k in cells})
    lines = [f"| {x_name} \\ {y_name} | " + " | ".join(f"{y:g}" for y in ys) + " |", "|---|" + "---|" * len(ys)]
    for x in xs:
        row = []
        for y in ys:
            cell = cells[f"{x}|{y}"]
            entry = cell["classes"][key]
            dominant = NAMES[entry["dominant"]]
            counts = entry["counts"]
            row.append(f"{dominant}（{counts['real_improvement']}/{counts['washing_trap']}/{counts['low_low']}/{counts['mixed']}）")
        lines.append(f"| {x:g} | " + " | ".join(row) + " |")
    return lines


def main(name: str) -> None:
    analysis = json.loads((HERE / f"{name}_analysis.json").read_text(encoding="utf-8"))
    table, secondary = analysis["scenarios"], analysis["secondary"]
    out = [f"# 阶段 F 表格（{name}）", "", f"experiment_id `{analysis['experiment_id']}`", "", "## 主要问题", "",
           "| 问题 | 指标 | 均值 [95% 区间] | 未校正 p | Holm p | n |", "|---|---|---|---:|---:|---:|"]
    for row in analysis["primary"]:
        out.append(f"| {row['name']} | `{row['metric']}` | {fmt(row['mean'])} [{fmt(row['ci_low'])}, {fmt(row['ci_high'])}] | "
                   f"{row['p_value']:.3g} | {row['holm_p_value']:.3g} | {row['n']} |")
    blocks = [("A. 主比较（市场开启）", ["B", "I", "F", "IF"]), ("A. 主比较（市场关闭）", ["off_B", "off_I", "off_F", "off_IF"]),
              ("B. 透明度剂量", ["B", "I_0p3", "I_0p5", "I", "I_0p7", "I_0p8"]),
              ("B. 定额罚款剂量", ["F_0x", "B", "F_2x", "F", "F_8x"]), ("B. 比例罚剂量", ["P_1x", "P_2x", "P_4x"]),
              ("C. 等成本", ["eqcost_B", "eqcost_I", "eqcost_F", "eqcost_IF"]),
              ("D. 零假设对照", ["zeroII_B", "null_control"]), ("E. 无衰减", ["decay0_B", "decay0_I", "decay0_F", "decay0_IF"]),
              ("F. 初始化对照", ["indep_B", "indep_I", "indep_F", "booksd_B", "booksd_I", "booksd_F"])]
    for title, names in blocks:
        out += ["", f"## {title}", ""] + scenario_rows(table, names)
    out += ["", "## 辅助对比（真实变化，SD，未校正区间）", "", "| 对比 | 真实变化 | 平均虚报 | 大减小 |", "|---|---|---|---|"]
    for comparison, metrics in secondary.items():
        out.append(f"| {comparison} | {interval(metrics['true_change.equal_weight_sd'])} | "
                   f"{interval(metrics['inflation.mean_sd'])} | {interval(metrics['size.large_minus_small_sd'])} |")
    for title, key, x_name, y_name in (("相图 1：偏好强度 × 初始 II 概率（基准政策）", "phase_map_1_taste_by_share", "taste", "II 概率"),
                                       ("相图 2：漂绿成本比例 × 透明度", "phase_map_2_wash_cost_by_tau", "w", "τ")):
        cells = analysis[key]
        for variant in ("decay_adjusted", "original"):
            out += ["", f"## {title}，G 口径：{'扣除衰减' if variant == 'decay_adjusted' else '原口径'}，阈值 0.25", "",
                    "括号内为真实改善 / 漂绿陷阱 / 低改善低虚报 / 混合的种子数。", ""]
            out += phase_rows(cells, x_name, y_name, f"{variant}_g0.25_w0.25")
    out += ["", "## τ*(w) 预测核对（相图 2）", "", "| w | τ | τ*(w) | 预测 | 末年平均虚报 | 漂绿决策占比 |", "|---:|---:|---:|---|---:|---:|"]
    for row in analysis["tau_star_check"]:
        out.append(f"| {row['w']:g} | {row['tau']:g} | {row['tau_star']:.2f} | {'漂绿' if row['predicted_washing'] else '不漂绿'} | "
                   f"{row['terminal_w']:.3f} | {row['wash_share']:.1%} |")
    (HERE / f"{name}_tables.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(HERE / f"{name}_tables.md")


if __name__ == "__main__":
    main(sys.argv[1])
