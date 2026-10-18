"""Figures for the working paper, read from committed analysis files only.

Run from the repository root:

    python paper/make_figures.py

Inputs (all tracked in git):
  reports/disclosure_stage_f_20261014/confirmatory_v1_analysis.json
  reports/disclosure_decay_grid_20261016/grid_v1_analysis.json

Outputs: paper/figures/fig_*.pdf (vector, for LaTeX) and fig_*.png (for
previews and social posts). Colours follow one rule across the paper:
information policy blue, fixed (per-case) fines orange, proportional fines
aqua. The palette passed the dataviz validator (light mode, all pairs).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STAGE_F = ROOT / "reports/disclosure_stage_f_20261014/confirmatory_v1_analysis.json"
DECAY = ROOT / "reports/disclosure_decay_grid_20261016/grid_v1_analysis.json"
OUT = ROOT / "paper/figures"

INFO = "#2a78d6"
FIXED = "#eb6834"
PROP = "#1baf7a"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e5e4df"
BLUE_RAMP = ["#f3f7fd", "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]

METRIC = "true_change.equal_weight_sd"

plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8.5,
    "axes.edgecolor": INK_2,
    "axes.labelcolor": INK,
    "xtick.color": INK_2,
    "ytick.color": INK_2,
    "text.color": INK,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "savefig.dpi": 220,
})


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def grid_y(ax) -> None:
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUT / f"{name}.png", bbox_inches="tight", metadata={"Software": None})
    plt.close(fig)


def contrast(stage_f: dict, name: str) -> tuple[float, float, float]:
    item = stage_f["secondary"][name][METRIC]
    return item["mean"], item["ci_low"], item["ci_high"]


def fig_decay(decay: dict) -> None:
    """Policy effects across the five uniform natural-decay settings."""
    points = decay["grid_points"]
    confirmatory = {0.0, 0.2}
    fig, ax = plt.subplots(figsize=(6.3, 3.0))
    for key, colour, label in (("I_minus_B", INFO, "Information ($\\tau$ = 0.6) − baseline"),
                               ("F_minus_B", FIXED, "Fixed fine 4× − baseline")):
        xs, ys, lo, hi = [], [], [], []
        for p in points:
            c = decay["points"][str(p)]["contrasts"][key]["true_change"]
            xs.append(p), ys.append(c["mean"]), lo.append(c["ci_low"]), hi.append(c["ci_high"])
        ax.plot(xs, ys, color=colour, linewidth=1.5, zorder=2)
        ax.vlines(xs, lo, hi, color=colour, linewidth=1.2, zorder=2)
        for x, y in zip(xs, ys):
            filled = x in confirmatory
            ax.plot(x, y, marker="o", markersize=6, zorder=3, color=colour,
                    markerfacecolor=colour if filled else "white", markeredgewidth=1.3)
        ax.annotate(label, (xs[-1], ys[-1]), xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=8.5, color=INK)
    ax.axhline(0, color=INK_2, linewidth=0.6)
    ax.set_xticks(points)
    ax.set_xticklabels([f"{p:g}" for p in points])
    ax.set_xlim(-0.01, 0.21)
    ax.set_xlabel("Natural decay of the true level without effort (SD per year)")
    ax.set_ylabel("Change in true level vs. baseline (SD)")
    grid_y(ax)
    ax.plot([], [], marker="o", color=INK_2, markerfacecolor=INK_2, linestyle="none", label="Confirmatory (pre-registered)")
    ax.plot([], [], marker="o", color=INK_2, markerfacecolor="white", linestyle="none", label="Exploratory supplement")
    ax.legend(loc="upper left", frameon=False, handletextpad=0.3)
    save(fig, "fig_decay")


def fig_frontier(stage_f: dict) -> None:
    """Washing share against the change in true level, for every tested dose."""
    sc = stage_f["scenarios"]
    base_x = 100 * sc["B"]["wash"]
    # Dose labels: (scenario, label, label offset in points). Empty labels are
    # covered by a neighbour's label; tau 0.6-0.8 all sit at zero washing.
    series = (
        ("Information (transparency $\\tau$)", INFO,
         [("B", "", None), ("I_0p3", "0.3", (6, 3)), ("I_0p5", "0.5", (6, 3)),
          ("I", "", None), ("I_0p7", "", None), ("I_0p8", "$\\tau$ = 0.6, 0.7, 0.8", (8, 4))]),
        ("Fixed fine per case", FIXED,
         [("F_0x", "0×", (0, 7)), ("B", "", None), ("F_2x", "2×", (7, -3)),
          ("F", "4×", (7, -3)), ("F_8x", "8×", (7, -1))]),
        ("Proportional fine", PROP,
         [("P_1x", "1×", (0, 7)), ("P_2x", "2×", (0, 7)), ("P_4x", "4×", (0, 7))]),
    )
    fig, ax = plt.subplots(figsize=(6.3, 3.6))
    for name, colour, doses in series:
        xs, ys, lo, hi = [], [], [], []
        for scenario, _, _ in doses:
            xs.append(100 * sc[scenario]["wash"])
            if scenario == "B":
                ys.append(0.0), lo.append(0.0), hi.append(0.0)
            else:
                m, l, h = contrast(stage_f, f"{scenario}_minus_B")
                ys.append(m), lo.append(l), hi.append(h)
        ax.plot(xs, ys, color=colour, linewidth=1.5, zorder=2, label=name)
        ax.vlines(xs, lo, hi, color=colour, linewidth=1.2, zorder=2)
        for (scenario, dose, offset), x, y in zip(doses, xs, ys):
            if scenario == "B":
                continue
            ax.plot(x, y, marker="o", markersize=5.5, color=colour, zorder=3)
            if dose:
                ha = "right" if offset[0] < 0 else ("left" if offset[0] > 0 else "center")
                ax.annotate(dose, (x, y), xytext=offset, textcoords="offset points", ha=ha,
                            va="bottom" if offset[1] > 0 else "center", fontsize=8, color=INK_2)
    ax.plot(base_x, 0, marker="o", markersize=7, color=INK, zorder=4)
    ax.annotate("Baseline\n($\\tau$ = 0.1, fixed fine 1×)", (base_x, 0), xytext=(10, -22), textcoords="offset points",
                fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.6))
    ax.axhline(0, color=INK_2, linewidth=0.6)
    ax.set_xlim(-3, 97)
    ax.set_xlabel("Share of firm decisions that inflate the report, policy window (%)")
    ax.set_ylabel("Change in true level vs. baseline (SD)")
    grid_y(ax)
    ax.legend(loc="lower left", frameon=False, handletextpad=0.4)
    save(fig, "fig_frontier")


def fig_threshold(stage_f: dict) -> None:
    """Washing share on the w x tau grid with the predicted threshold."""
    cells = stage_f["tau_star_check"]
    ws = sorted({c["w"] for c in cells})
    taus = sorted({c["tau"] for c in cells})
    value = {(c["w"], c["tau"]): 100 * c["wash_share"] for c in cells}
    star = {c["w"]: c["tau_star"] for c in cells}
    cmap = LinearSegmentedColormap.from_list("blue_ramp", BLUE_RAMP)
    vmax = 50.0
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    for i, w in enumerate(ws):
        for j, tau in enumerate(taus):
            v = value[(w, tau)]
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=cmap(min(v, vmax) / vmax), edgecolor="white", linewidth=2))
            ax.text(j + 0.5, i + 0.5, f"{v:.0f}%" if v >= 0.5 else "0",
                    ha="center", va="center", fontsize=9, color="white" if v > 28 else INK)
    # Predicted boundary: firms stop inflating once tau >= tau*(w).
    for i, w in enumerate(ws):
        j = sum(t < star[w] for t in taus)
        ax.plot([j, j], [i, i + 1], color=INK, linewidth=2.2, solid_capstyle="butt", zorder=5)
        if i + 1 < len(ws):
            j_next = sum(t < star[ws[i + 1]] for t in taus)
            if j_next != j:
                ax.plot([j, j_next], [i + 1, i + 1], color=INK, linewidth=2.2, solid_capstyle="butt", zorder=5)
    ax.set_xlim(0, len(taus))
    ax.set_ylim(0, len(ws))
    ax.set_xticks([j + 0.5 for j in range(len(taus))])
    ax.set_xticklabels([f"{t:g}" for t in taus])
    ax.set_yticks([i + 0.5 for i in range(len(ws))])
    ax.set_yticklabels([f"$w$ = {w:g}  ($\\tau^*$ = {star[w]:.2f})" for w in ws])
    ax.set_xlabel("Transparency $\\tau$ from day 1201")
    ax.tick_params(length=0)
    for side in ("left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.set_title("Share of decisions that inflate; line = predicted $\\tau^*(w)$", loc="left", fontsize=9, color=INK)
    save(fig, "fig_threshold")


def fig_size(stage_f: dict) -> None:
    """Washing share by size tier under fixed and proportional fines."""
    sc = stage_f["scenarios"]
    tiers = ("wash_large", "wash_mid", "wash_small")
    panels = (
        ("(a) Fixed fine per case", FIXED, [("B", "1×"), ("F_2x", "2×"), ("F", "4×"), ("F_8x", "8×")]),
        ("(b) Proportional fine (equal-amount reference)", PROP, [("P_1x", "1×"), ("P_2x", "2×"), ("P_4x", "4×")]),
    )
    markers = ("o", "s", "^", "D")
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 2.9), sharey=True)
    for ax, (title, colour, doses) in zip(axes, panels):
        for k, (scenario, dose) in enumerate(doses):
            ys = [100 * sc[scenario][t] for t in tiers]
            ax.plot(range(3), ys, color=colour, linewidth=1.5, marker=markers[k], markersize=5.5, zorder=3)
            # Large firms are where the doses spread out, so label that end.
            ax.annotate(dose, (0, ys[0]), xytext=(-8, 0), textcoords="offset points", ha="right",
                        va="center", fontsize=8, color=INK_2)
        ax.set_xticks(range(3))
        ax.set_xticklabels(["Large", "Mid", "Small"])
        ax.set_xlim(-0.5, 2.2)
        ax.set_title(title, loc="left", fontsize=9, color=INK)
        ax.set_xlabel("Firm size tier")
        grid_y(ax)
    axes[0].set_ylabel("Share of decisions that inflate (%)")
    axes[0].set_ylim(0, 100)
    save(fig, "fig_size")


def main() -> None:
    stage_f = load(STAGE_F)
    decay = load(DECAY)
    fig_decay(decay)
    fig_frontier(stage_f)
    fig_threshold(stage_f)
    fig_size(stage_f)
    print(f"wrote figures to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
