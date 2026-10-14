"""Stage D.1: read-only diagnosis of the archived 256-world multi-amplitude Q-learning run.

Separates three candidate causes of the coverage failure: state/action space size,
training amount, and the reward's signal-to-noise ratio. Reads only archived arrays.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "reports" / "disclosure_action_grid_development_20261011_v1"
OUT = Path(__file__).resolve().parent / "archive_diagnosis.json"
ALPHA = .1
DISCOUNT = .05
PERIOD = 60


def _window_sum(daily: np.ndarray, start: int, end: int) -> np.ndarray:
    weights = np.exp(-DISCOUNT * np.arange(1, end - start + 1) / 252)
    return weights @ daily[start + 1:end + 1]


def main() -> None:
    summary = json.loads((ARCHIVE / "summary.json").read_text(encoding="utf-8"))
    seeds = summary["budget"]["training_seeds"]
    rows = []  # group, state, choice, reward, financing part, ledger part, world index
    counts_by_world = []
    for index, seed in enumerate(seeds):
        with np.load(ARCHIVE / "training" / f"seed_{seed}" / "result.npz") as data:
            groups, states, choices = data["learning_groups"], data["learning_states"], data["learning_choices"]
            rewards, transition = data["learning_rewards"], data["learning_transition"]
            cap = data["market_prices"][0]
            adjustment = data["financing_value_adjustment"]
            ledger = data["applied_subsidy"] - data["applied_resource_cost"] - data["applied_fine"]
        periods = groups.shape[0]
        for period in range(2, periods):
            if not transition[period].all():
                continue
            end = period * PERIOD
            start = end - PERIOD
            financing = _window_sum(adjustment, start, end) / cap
            own = _window_sum(ledger, start, end) / cap
            if not np.allclose(financing + own, rewards[period], rtol=1e-9, atol=1e-15):
                raise ValueError("reward decomposition does not reproduce the archived reward")
            rows.append(np.column_stack((groups[period - 1], states[period - 1], choices[period - 1],
                                         rewards[period], financing, own,
                                         np.full(groups.shape[1], index))))
        counts_by_world.append(len(rows))
    data = np.vstack(rows)
    group, state, choice = data[:, 0].astype(int), data[:, 1].astype(int), data[:, 2].astype(int)
    reward, financing, own, world = data[:, 3], data[:, 4], data[:, 5], data[:, 6].astype(int)
    result: dict = {"archive": ARCHIVE.relative_to(ROOT).as_posix(), "transitions": int(reward.size),
                    "training_worlds": len(seeds)}

    # 1. Reward scale and what the firm's own choice can move.
    result["reward_scale_bp_of_initial_cap"] = {
        "reward_sd": float(reward.std() * 1e4), "financing_part_sd": float(financing.std() * 1e4),
        "own_ledger_part_sd": float(own.std() * 1e4),
        "financing_part_mean": float(financing.mean() * 1e4), "own_ledger_part_mean": float(own.mean() * 1e4),
    }
    # Common (same world, same period) component of the financing part.
    period_key = world * 1000 + (np.arange(reward.size) // 30) % 1000
    _, inverse = np.unique(period_key, return_inverse=True)
    period_mean = np.bincount(inverse, financing) / np.bincount(inverse)
    common = period_mean[inverse]
    result["financing_common_share_of_variance"] = float(common.var() / financing.var())

    # 2. Within (group, state): how much reward variance the choice explains (one-way ANOVA).
    cells = []
    for g in range(3):
        for s in range(81):
            member = (group == g) & (state == s)
            if member.sum() < 200:
                continue
            r = reward[member]
            c = choice[member]
            present = [a for a in range(17) if (c == a).sum() >= 10]
            if len(present) < 3:
                continue
            means = np.array([r[c == a].mean() for a in present])
            sizes = np.array([(c == a).sum() for a in present])
            within = np.sqrt(sum(((r[c == a] - r[c == a].mean()) ** 2).sum() for a in present) / (sizes.sum() - len(present)))
            between = np.sum(sizes * (means - r[np.isin(c, present)].mean()) ** 2) / (len(present) - 1)
            f_stat = between / within**2
            own_means = np.array([own[member][c == a].mean() for a in present])
            cells.append({"group": g, "state": s, "transitions": int(member.sum()), "choices": len(present),
                          "within_sd_bp": float(within * 1e4), "f_statistic": float(f_stat),
                          "choice_mean_range_bp": float(np.ptp(means) * 1e4),
                          "own_ledger_mean_range_bp": float(np.ptp(own_means) * 1e4)})
    result["anova_cells"] = cells
    if cells:
        result["anova_summary"] = {
            "cells": len(cells),
            "median_f": float(np.median([c["f_statistic"] for c in cells])),
            "median_within_sd_bp": float(np.median([c["within_sd_bp"] for c in cells])),
            "median_choice_mean_range_bp": float(np.median([c["choice_mean_range_bp"] for c in cells])),
            "median_own_ledger_mean_range_bp": float(np.median([c["own_ledger_mean_range_bp"] for c in cells])),
        }

    # 3. Constant step size: stationary SD of a Q estimate is sqrt(alpha/(2-alpha)) * reward SD,
    # i.e. an effective sample size (2-alpha)/alpha regardless of the training budget.
    with np.load(ARCHIVE / "frozen_model.npz") as frozen:
        values, counts = frozen["values"], frozen["counts"]
    floor = np.sqrt(ALPHA / (2 - ALPHA))
    gaps = []
    for g in range(3):
        for s in range(81):
            trained = counts[g, s] >= 20
            if trained.sum() < 2:
                continue
            q = np.sort(values[g, s, trained])[::-1]
            member = (group == g) & (state == s)
            sd = reward[member].std() if member.sum() > 1 else np.nan
            gaps.append({"group": g, "state": s, "top_gap_bp": float((q[0] - q[1]) * 1e4),
                         "q_range_bp": float((q[0] - q[-1]) * 1e4),
                         "noise_floor_bp": float(floor * sd * 1e4)})
    result["constant_step_noise_floor"] = {
        "alpha": ALPHA, "effective_samples": (2 - ALPHA) / ALPHA, "sd_multiplier": float(floor),
        "states": len(gaps),
        "median_top_gap_bp": float(np.median([x["top_gap_bp"] for x in gaps])),
        "median_q_range_bp": float(np.median([x["q_range_bp"] for x in gaps])),
        "median_noise_floor_bp": float(np.nanmedian([x["noise_floor_bp"] for x in gaps])),
        "share_range_below_floor": float(np.mean([x["q_range_bp"] < x["noise_floor_bp"] for x in gaps])),
    }

    # 4. Occupancy: how concentrated the training visits are, and the N >= 20 K necessary condition.
    occupancy = []
    for g in range(3):
        visits = np.bincount(state[group == g], minlength=81)
        share = np.sort(visits)[::-1] / visits.sum()
        occupancy.append({"group": g, "transitions": int(visits.sum()), "states_visited": int((visits > 0).sum()),
                          "states_for_90pct": int(np.searchsorted(np.cumsum(share), .9) + 1),
                          "states_below_340_visits": int(((visits > 0) & (visits < 340)).sum()),
                          "share_of_transitions_in_states_below_340": float(visits[(visits > 0) & (visits < 340)].sum() / visits.sum())})
    result["occupancy"] = occupancy

    # 5. Training amount: share of (group, state, choice) cells with >= 20 updates after k worlds,
    # among states that hold >= 1% of their group's transitions.
    curve = []
    for k in (16, 32, 64, 128, 192, 256):
        use = world < k
        tally = np.zeros((3, 81, 17), dtype=np.int64)
        np.add.at(tally, (group[use], state[use], choice[use]), 1)
        total = tally.sum(axis=2)
        common = total >= .01 * total.sum(axis=1, keepdims=True)
        need = common[:, :, None] & np.ones(17, dtype=bool)
        curve.append({"worlds": k, "share_common_cells_ge20": float((tally[need] >= 20).mean()),
                      "large_firm_share": float((tally[0][need[0]] >= 20).mean()),
                      "median_cell_count_large": float(np.median(tally[0][need[0]]))})
    result["coverage_learning_curve"] = curve
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "anova_cells"}, indent=2))


if __name__ == "__main__":
    main()
