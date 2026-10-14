"""Acceptance tests, drift decomposition, signal-to-noise and the replicator benchmark (contract section 18).

Reads runs.json and the per-period records in runs/ written by diagnose.py; no simulation. Expected switching
flows use each period's recorded advantage and shares: with p+ = min(1, k adv+) and p- = min(1, k adv-),
the type-mean rule moves m[(1-s)p+ - s p-] investors into impact investing, which splits into a selection
part m(p+ - p-)/2 and a size-asymmetry part m(1/2 - s)(p+ + p-); the pairwise rule moves
m N s(1-s)/(N-1) (p+ - p-). Writes analysis.json.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure.experiments import paired_statistics  # noqa: E402

INTENSITY, REVIEW_SHARE = 100.0, 0.1
PAIRS = (("type_mean_taste_0.2", "type_mean_zero_0.2"), ("pairwise_taste_0.2", "pairwise_zero_0.2"),
         ("pairwise_annual_taste_0.2", "pairwise_annual_zero_0.2"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval(values) -> dict:
    stats = paired_statistics([float(value) for value in values], 0.95)
    return {key: stats[key] for key in ("mean", "ci_low", "ci_high", "p_value", "n")} | {
        "contains_zero": stats["ci_low"] <= 0 <= stats["ci_high"]}


def expected_flows(record: dict, data: dict, investors: int) -> dict:
    reviewed = max(1, int(round(REVIEW_SHARE * investors)))
    s, advantage = data["share"], data["advantage"]
    valid = np.isfinite(advantage)
    up = np.minimum(1.0, INTENSITY * np.maximum(advantage, 0.0))
    down = np.minimum(1.0, INTENSITY * np.maximum(-advantage, 0.0))
    up[~valid] = down[~valid] = 0.0
    realized = float((data["to_impact"] - data["to_profit"]).sum() / investors)
    if record["rule"] == "type_mean":
        selection = reviewed * (up - down) / 2
        asymmetry = reviewed * (0.5 - s) * (up + down)
        return {"realized": realized, "expected": float((selection + asymmetry).sum() / investors),
                "selection": float(selection.sum() / investors), "asymmetry": float(asymmetry.sum() / investors)}
    selection = reviewed * investors * s * (1 - s) / (investors - 1) * (up - down)
    return {"realized": realized, "expected": float(selection.sum() / investors),
            "selection": float(selection.sum() / investors), "asymmetry": 0.0}


def clustered_ols(x: np.ndarray, y: np.ndarray, groups: np.ndarray) -> dict:
    design = np.column_stack((np.ones_like(x), x))
    inverse = np.linalg.inv(design.T @ design)
    beta = inverse @ design.T @ y
    residual = y - design @ beta
    meat = np.zeros((2, 2))
    for group in np.unique(groups):
        score = design[groups == group].T @ residual[groups == group]
        meat += np.outer(score, score)
    covariance = inverse @ meat @ inverse
    root = -beta[0] / beta[1] if beta[1] != 0 else None
    return {"intercept": float(beta[0]), "slope": float(beta[1]),
            "intercept_se": float(np.sqrt(covariance[0, 0])), "slope_se": float(np.sqrt(covariance[1, 1])),
            "zero_at_share": float(root) if root is not None else None,
            "zero_inside_unit_interval": bool(root is not None and 0 <= root <= 1 and beta[1] < 0),
            "periods": int(y.size), "runs": int(np.unique(groups).size)}


def main():
    payload = json.loads((HERE / "runs.json").read_text(encoding="utf-8"))
    investors = payload["market"]["n_investors"]
    records = payload["records"]
    data = {}
    for record in records:
        path = HERE / "runs" / record["artifact"]
        if sha(path) != record["artifact_sha256"]:
            raise ValueError(f"record hash mismatch: {path.name}")
        with np.load(path) as bundle:
            data[(record["label"], record["seed"])] = {key: bundle[key] for key in bundle.files}
    cells = {}
    for cell in payload["cells"]:
        rows = [record for record in records if record["label"] == cell["label"]]
        change = [row["share"]["day_3500"] - row["share"]["day_0"] for row in rows]
        wealth_change = [row["wealth_share"]["day_3500"] - row["wealth_share"]["day_0"] for row in rows]
        flows = [expected_flows(row, data[(row["label"], row["seed"])], investors) for row in rows]
        periods = [data[(row["label"], row["seed"])] for row in rows]
        advantage = np.concatenate([item["advantage"] for item in periods])
        error = np.concatenate([item["standard_error"] for item in periods])
        valid = np.isfinite(advantage) & np.isfinite(error) & (error > 0)
        z = advantage[valid] / error[valid]
        cells[cell["label"]] = {
            **cell, "seeds": len(rows), "price_cap_hits": sum(row["price_cap_hits"] for row in rows),
            "share_change": interval(change), "wealth_share_change": interval(wealth_change),
            "policy_window_share_change": interval([row["share"]["day_3500"] - row["share"]["day_1200"] for row in rows]),
            "flows_mean_over_seeds": {key: float(np.mean([item[key] for item in flows]))
                                      for key in ("realized", "expected", "selection", "asymmetry")},
            "advantage": {"mean": float(advantage[valid].mean()), "sd": float(advantage[valid].std(ddof=1)),
                          "mean_absolute": float(np.abs(advantage[valid]).mean()),
                          "signal_to_noise": float(advantage[valid].mean() / advantage[valid].std(ddof=1)),
                          "mean_standard_error": float(error[valid].mean()),
                          "share_periods_abs_z_above_1.96": float((np.abs(z) > 1.96).mean()),
                          "periods": int(valid.sum())},
        }
    paired = {}
    for treated, control in PAIRS:
        by_seed = {row["seed"]: row for row in records if row["label"] == control}
        differences = [row["share"]["day_3500"] - row["share"]["day_0"]
                       - (by_seed[row["seed"]]["share"]["day_3500"] - by_seed[row["seed"]]["share"]["day_0"])
                       for row in records if row["label"] == treated]
        wealth = [row["wealth_share"]["day_3500"] - row["wealth_share"]["day_0"]
                  - (by_seed[row["seed"]]["wealth_share"]["day_3500"] - by_seed[row["seed"]]["wealth_share"]["day_0"])
                  for row in records if row["label"] == treated]
        paired[f"{treated}_minus_{control}"] = {"share_change": interval(differences), "wealth_share_change": interval(wealth)}
    benchmark = {}
    for name, labels in (("pairwise_taste", ("pairwise_taste_0.2", "pairwise_taste_0.5", "pairwise_taste_0.8")),
                         ("pairwise_zero", ("pairwise_zero_0.2", "pairwise_zero_0.5", "pairwise_zero_0.8"))):
        shares, advantages, groups = [], [], []
        for index, record in enumerate(row for row in records if row["label"] in labels):
            item = data[(record["label"], record["seed"])]
            valid = np.isfinite(item["advantage"])
            shares.append(item["share"][valid])
            advantages.append(item["advantage"][valid])
            groups.append(np.full(valid.sum(), index))
        x, y, g = np.concatenate(shares), np.concatenate(advantages), np.concatenate(groups)
        bins = []
        for low in np.arange(0, 1, .1):
            member = (x >= low) & (x < low + .1)
            if member.sum() >= 20:
                bins.append({"share_low": float(low), "periods": int(member.sum()), "mean_advantage": float(y[member].mean()),
                             "se": float(y[member].std(ddof=1) / np.sqrt(member.sum()))})
        benchmark[name] = {"ols_clustered_by_run": clustered_ols(x, y, g), "binned": bins}
    acceptance = {
        "a_pairwise_zero_taste_no_drift": all(cells[f"pairwise_zero_{share}"]["share_change"]["contains_zero"]
                                              for share in ("0.2", "0.5", "0.8")),
        "b_pairwise_taste_distinguishable": not paired["pairwise_taste_0.2_minus_pairwise_zero_0.2"]["share_change"]["contains_zero"],
    }
    result = {"contract": "research contract section 18", "script_sha256": sha(Path(__file__)),
              "runs_sha256": sha(HERE / "runs.json"), "instrumentation_checks": payload["instrumentation_checks"],
              "acceptance": acceptance, "cells": cells, "paired": paired, "replicator_benchmark": benchmark,
              "scope": "Development seeds 29001-29020; 95% t intervals across seeds, unadjusted; expected flows "
                       "condition on the realized advantages and shares of each run."}
    (HERE / "analysis.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                        encoding="utf-8")
    print(json.dumps({"acceptance": acceptance,
                      "share_change": {key: [round(value["share_change"][k], 4) for k in ("mean", "ci_low", "ci_high")]
                                       for key, value in cells.items()},
                      "paired": {key: [round(value["share_change"][k], 4) for k in ("mean", "ci_low", "ci_high")]
                                 for key, value in paired.items()}}, indent=1))


if __name__ == "__main__":
    main()
