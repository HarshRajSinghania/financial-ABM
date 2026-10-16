"""Decay grid figure: the three judged contrasts against uniform natural decay (contract 20.16).

  python plot.py    # reads grid_v1_analysis.json, writes decay_grid_magnitudes.png
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES = (("I_minus_B", "I − B", "#2a78d6", -0.002), ("F_minus_B", "F − B", "#eb6834", 0.0),
          ("I_minus_F", "I − F", "#1baf7a", 0.002))   # reference categorical slots 1-3, fixed order


def main() -> None:
    result = json.loads((HERE / "grid_v1_analysis.json").read_text(encoding="utf-8"))
    order = result["grid_points"]
    plt.rcParams.update({"font.family": "Microsoft YaHei", "axes.unicode_minus": False, "font.size": 10})
    fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=200, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for key, name, color, dodge in SERIES:
        stats = [result["points"][str(p)]["contrasts"][key]["true_change"] for p in order]
        means = [s["mean"] for s in stats]
        xs = [p + dodge for p in order]
        errors = [[m - s["ci_low"] for m, s in zip(means, stats)], [s["ci_high"] - m for m, s in zip(means, stats)]]
        ax.errorbar(xs, means, yerr=errors, color=color, linewidth=2, marker="o", markersize=6,
                    markeredgecolor=SURFACE, markeredgewidth=1.5, capsize=3, elinewidth=1.2, label=name, zorder=3)
        ax.annotate(f"{name}  {means[-1]:+.3f}".replace("-", "−"), (order[-1] + dodge, means[-1]),
                    xytext=(10, 0), textcoords="offset points", va="center", color=INK, fontsize=9)
    ax.axhline(0, color=INK_2, linewidth=0.8, zorder=1)
    ax.set_xticks(order, [f"{p:g}" + ("\n阶段 F 无衰减" if p == 0 else "\n阶段 F 主设定" if p == 0.2 else "\n本补充")
                          for p in order], color=INK_2)
    ax.set_xlim(-0.015, 0.245)
    ax.set_xlabel("统一自然衰减（SD/年）", color=INK_2)
    ax.set_ylabel("政策窗口内真实变化之差（SD）", color=INK_2)
    ax.tick_params(colors=INK_2, length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.legend(loc="upper left", frameon=False, labelcolor=INK)
    ax.set_title("政策效应的量级随统一自然衰减的变化", loc="left", color=INK, fontsize=12, pad=18)
    ax.text(0, 1.02, "第 1200–3500 日，30 个配对种子（41001–41030）的均值；误差线为配对 95% t 区间，未作多重校正",
            transform=ax.transAxes, color=INK_2, fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE / "decay_grid_magnitudes.png", facecolor=SURFACE)
    print(HERE / "decay_grid_magnitudes.png")


if __name__ == "__main__":
    main()
