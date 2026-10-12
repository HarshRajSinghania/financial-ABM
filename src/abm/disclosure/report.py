"""Scientific figures from archived disclosure experiment summaries."""

from __future__ import annotations

from math import isfinite
from pathlib import Path


def render_charts(destination: Path, frozen: dict, summary: dict) -> list[str]:
    """Render saved estimates and intervals without simulation or inference."""
    from matplotlib import rc_context
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    confidence = 100 * frozen["spec"]["analysis"]["confidence_level"]
    metric = "true_change.equal_weight_sd"
    caption = (
        f"{summary['purpose']} | results: {summary['status']} | claims: {summary['claim_support']}"
        f" | core-validation failures: {summary['trials_failing_core_validation']}\n"
        "Local valuation proxy; empirical policy conclusions pending. Seed uncertainty only."
    )
    files = []

    def save(figure, name):
        for extension in ("png", "pdf"):
            filename = f"{name}.{extension}"
            figure.savefig(destination / filename, dpi=300, bbox_inches="tight")
            files.append(filename)
        figure.clear()

    def intervals(rows, title, name, description):
        figure = Figure(figsize=(7.5, max(3.5, .34 * len(rows) + 2.1)))
        FigureCanvasAgg(figure)
        axis = figure.subplots()
        labels = []
        for index, (label, estimate) in enumerate(rows):
            label = label.replace("_", " ")
            mean = estimate.get("mean")
            if estimate.get("status") != "complete" or mean is None or not isfinite(mean):
                labels.append(f"{label} [missing]")
                continue
            count = estimate.get("n", 0)
            low, high = estimate.get("ci_low"), estimate.get("ci_high")
            if count >= 2 and low is not None and high is not None and isfinite(low) and isfinite(high) and low <= mean <= high:
                axis.errorbar(mean, index, xerr=[[mean - low], [high - mean]],
                              fmt="o", capsize=3, color="#0072B2")
                labels.append(f"{label} [n={count}]")
            else:
                axis.plot(mean, index, "o", color="#0072B2")
                labels.append(f"{label} [n={count}; CI unavailable]")
        axis.set_yticks(range(len(labels)), labels)
        axis.invert_yaxis()
        axis.axvline(0, color=".5", linestyle="--", linewidth=.8)
        axis.set_xlabel("Real attribute change (initial SD)")
        axis.set_title(title)
        figure.text(.02, .02, f"{description}\n{caption}", fontsize=8, va="bottom")
        figure.subplots_adjust(left=.39, right=.97, top=.88, bottom=.24)
        save(figure, name)

    with rc_context({"font.family": "DejaVu Sans", "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": .18, "pdf.fonttype": 42}):
        comparisons = [
            (row["name"], row["metrics"].get(metric, {})) for row in summary["comparisons"]
            if row.get("primary_metric", metric) == metric
        ]
        intervals(comparisons, "Selected contrasts: real attribute change", "policy_effects",
                  f"Saved paired-seed means and {confidence:g}% t intervals; intervals are unadjusted.")

        figure = Figure(figsize=(8.5, 4.5))
        FigureCanvasAgg(figure)
        axis = figure.subplots()
        colors = ("#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#000000")
        markers = ("o", "s", "^")
        for index, row in enumerate(summary["scenarios"]):
            cost = row["metrics"].get("costs.resource_cost_fraction_initial_cap", {})
            change = row["metrics"].get(metric, {})
            x, y = cost.get("mean"), change.get("mean")
            label = row["name"].replace("_", " ")
            if cost.get("status") == change.get("status") == "complete" and x is not None and y is not None and isfinite(x) and isfinite(y):
                axis.scatter(100 * x, y, color=colors[index % len(colors)],
                             marker=markers[(index // len(colors)) % len(markers)], label=label)
            else:
                axis.plot([], [], "x", color=".6", label=f"{label} [missing]")
        axis.axhline(0, color=".5", linestyle="--", linewidth=.8)
        axis.set_xlabel("Committed resource expenditure (% of day-0 total market cap)")
        axis.set_ylabel("Real attribute change (initial SD)")
        axis.set_title("Scenario means: expenditure and real change")
        axis.legend(loc="center left", bbox_to_anchor=(1.02, .5), frameon=False, fontsize=8)
        figure.text(.02, .02, f"Descriptive policy-window changes and commitments; no causal efficiency ratio.\n{caption}",
                    fontsize=8, va="bottom")
        figure.subplots_adjust(left=.10, right=.69, top=.88, bottom=.26)
        save(figure, "resource_cost_vs_improvement")

        gaps = [(row["name"], row["metrics"].get("size.large_minus_small_sd", {}))
                for row in summary["scenarios"]]
        intervals(gaps, "Scenario size gap: large minus small", "size_improvement_gap",
                  f"Saved single-scenario seed means and {confidence:g}% t intervals; intervals are unadjusted.")
    return files
