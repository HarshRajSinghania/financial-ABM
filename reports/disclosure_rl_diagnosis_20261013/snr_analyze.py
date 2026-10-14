"""Stage D.1: read runs/snr_*.npz and estimate action effects against reward noise.

For horizons H (in 60-day periods), G = sum_{k=1..H} gamma^(k-1) r[p+k] is the learner's own discounted
reward after the choice at period p. Choices are randomized, so OLS of G on choice dummies with
group x state fixed effects estimates causal effects relative to maintain. Standard errors cluster by firm.
Effects are in basis points of the firm's initial market cap, the learner's reward unit.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
GAMMA = float(np.exp(-.05 * 60 / 252))
HORIZONS = (1, 4, 10, 20)
MAINTAIN = 2


def load() -> dict:
    blocks: dict[str, list] = {key: [] for key in ("G", "choice", "cell", "firm", "npv_gap", "size", "kind", "period")}
    blocks.update({f"G{h}": [] for h in HORIZONS})
    for world, path in enumerate(sorted((HERE / "runs").glob("snr_*.npz"))):
        with np.load(path) as data:
            rewards, transition, choices = data["rewards"], data["transition"], data["choices"]
            groups, states, size, kinds = data["groups"], data["states"], data["size"], data["kinds"]
            scale = data["decision_prices"] / data["initial_prices"]  # values are fractions of current price
            gap_all = (data["npv_values"] - data["npv_values"][:, :, [MAINTAIN]]) * scale[:, :, None]
            valid = data["valid"]
        periods, firms = rewards.shape
        last = periods - 1 - max(HORIZONS)
        for p in range(1, last + 1):
            if not transition[p + 1:p + max(HORIZONS) + 1].all():
                raise ValueError("missing transition inside the horizon")
            for h in HORIZONS:
                weights = GAMMA ** np.arange(h)
                blocks[f"G{h}"].append(weights @ rewards[p + 1:p + h + 1])
            blocks["choice"].append(choices[p])
            blocks["cell"].append(groups[p] * 81 + states[p])
            blocks["firm"].append(world * firms + np.arange(firms))
            blocks["npv_gap"].append(np.where(valid[p], gap_all[p - 1], np.nan))
            blocks["size"].append(size)
            blocks["kind"].append(kinds[p])
            blocks["period"].append(np.full(firms, p))
    out = {key: np.concatenate(value) if key != "npv_gap" else np.vstack(value) for key, value in blocks.items() if value}
    return out


def within(y: np.ndarray, cell: np.ndarray) -> np.ndarray:
    _, inverse = np.unique(cell, return_inverse=True)
    means = np.bincount(inverse, y) / np.bincount(inverse)
    return y - means[inverse]


def effects(y: np.ndarray, choice: np.ndarray, cell: np.ndarray, firm: np.ndarray, choices: int = 17) -> dict:
    columns = [a for a in range(choices) if a != MAINTAIN]
    X = np.column_stack([within((choice == a).astype(float), cell) for a in columns])
    yw = within(y, cell)
    xtx_inv = np.linalg.inv(X.T @ X)
    beta = xtx_inv @ X.T @ yw
    resid = yw - X @ beta
    _, inverse = np.unique(firm, return_inverse=True)
    scores = np.zeros((inverse.max() + 1, X.shape[1]))
    np.add.at(scores, inverse, X * resid[:, None])
    cov = xtx_inv @ (scores.T @ scores) @ xtx_inv
    se = np.sqrt(np.diag(cov))
    counts = np.array([(choice == a).sum() for a in columns])
    return {"choices": columns, "beta_bp": (beta * 1e4).tolist(), "se_bp": (se * 1e4).tolist(),
            "observations_per_choice": counts.tolist(),
            # SE scaled to one observation of that choice: noise a learner faces per sample
            "per_sample_sd_bp": (se * np.sqrt(counts) * 1e4).tolist(),
            "residual_sd_bp": float(resid.std() * 1e4)}


def main() -> None:
    data = load()
    result: dict = {"observations": int(data["choice"].size), "gamma_per_period": GAMMA, "horizons_periods": HORIZONS}
    result["reward_sd_bp"] = {f"H{h}": float(data[f"G{h}"].std() * 1e4) for h in HORIZONS}
    result["within_cell_sd_bp"] = {f"H{h}": float(within(data[f"G{h}"], data["cell"]).std() * 1e4) for h in HORIZONS}
    result["effects"] = {f"H{h}": effects(data[f"G{h}"], data["choice"], data["cell"], data["firm"]) for h in HORIZONS}
    # NPV-implied gap of each choice relative to maintain, at the same decisions (bp of initial cap).
    gap = data["npv_gap"]
    result["npv_gap_mean_bp"] = [float(np.nanmean(gap[:, a]) * 1e4) for a in range(17)]
    best = np.nanmax(gap, axis=1)
    result["npv_best_minus_maintain_bp_quantiles"] = np.quantile(best * 1e4, [.1, .25, .5, .75, .9]).tolist()
    for label, cls in (("large", 0), ("mid", 1), ("small", 2)):
        use = data["size"] == cls
        result[f"npv_best_minus_maintain_bp_median_{label}"] = float(np.median(best[use]) * 1e4)
        result[f"within_cell_sd_H20_bp_{label}"] = float(within(data["G20"][use], data["cell"][use]).std() * 1e4)
    # Samples per (cell, choice) for a two-sided 5% test to tell the NPV-best gap from zero:
    # n = (2 * 1.96 * sd / gap)^2 for a difference of two sample means with equal n.
    sd = within(data["G20"], data["cell"]).std()
    med = np.median(best)
    result["samples_needed_median_gap"] = float((2 * 1.96 * sd / med) ** 2) if med > 0 else None
    for q in (.75, .9):
        value = np.quantile(best, q)
        result[f"samples_needed_gap_q{int(q * 100)}"] = float((2 * 1.96 * sd / value) ** 2)
    (HERE / "snr_analysis.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    short = {k: v for k, v in result.items() if k != "effects"}
    print(json.dumps(short, indent=2))
    for h in ("H1", "H20"):
        e = result["effects"][h]
        print(h, "residual sd", round(e["residual_sd_bp"], 3))
        for a, b, s, n in zip(e["choices"], e["beta_bp"], e["se_bp"], e["observations_per_choice"]):
            print(f"  choice {a:2d}  effect {b:9.4f} bp  se {s:7.4f}  n {n}  npv gap {result['npv_gap_mean_bp'][a]:9.4f}")


if __name__ == "__main__":
    main()
