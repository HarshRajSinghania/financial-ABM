"""Explain v2 washing choices using its archived rules, without market reruns."""

from __future__ import annotations

import ast
import hashlib
import json
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
ARCHIVES = ROOT / "reports/disclosure_financing_development_20261011_v2"
OUTPUT = Path(__file__).with_suffix(".json")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archived_rules(manifest, path):
    namespace = {"np": np, "dataclass": dataclass, "__name__": __name__,
                 "TRADING_DAYS_PER_YEAR": 252, "IMPROVE": 0, "INFLATE": 1, "MAINTAIN": 2,
                 "MINIMUM_NPV": 1e-9}
    hashes = {}
    with zipfile.ZipFile(path) as archive:
        for filename, names in (("abm/disclosure/financing.py", {"financing_discount_factors"}),
                                ("abm/disclosure/game.py", {"FirmChoices", "npv_choices"})):
            raw = archive.read(filename)
            hashes[filename] = hashlib.sha256(raw).hexdigest()
            if hashes[filename] != manifest["source_hashes"][filename]:
                raise ValueError("archived rule hash does not match manifest")
            tree = ast.parse(raw.decode("utf-8"))
            selected = [ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)]
            selected += [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names]
            exec(compile(ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[])), filename, "exec"), namespace)
    return namespace, hashes


def main():
    first = ARCHIVES / "market_B/seed_23001/attempt_001/manifest.json"
    reference = json.loads(first.read_text(encoding="utf-8"))
    rules, hashes = archived_rules(reference, first.with_name("source.zip"))
    factors, choices = rules["financing_discount_factors"], rules["npv_choices"]
    totals = np.zeros(3, dtype=np.int64)
    rows, all_b, all_upper = [], [], []
    for path in sorted(ARCHIVES.glob("*/seed_*/attempt_001/result.npz")):
        manifest = json.loads(path.with_name("manifest.json").read_text(encoding="utf-8"))
        cfg, domain, policy = manifest["config"], manifest["domain"], manifest["policy"]
        if digest(path) != manifest["artifacts"]["result.npz"]:
            raise ValueError("result hash mismatch")
        if any(manifest["source_hashes"][key] != value for key, value in hashes.items()):
            raise ValueError("v2 archived rules differ across runs")
        with np.load(path, allow_pickle=False) as z:
            actions, amounts, costs = z["actions"][1:], z["amounts"][1:], z["cost_fraction"][1:]
            goodness, inflation = z["true_goodness"], z["inflation"]
            count = np.bincount(actions.ravel(), minlength=3)
            totals += count
            if np.any(inflation != 0):
                raise ValueError("the zero-inflation inversion premise is false")
            step = cfg["firm_decision_interval"]
            marginal = np.divide(costs, amounts**2, out=np.zeros_like(costs), where=amounts > 0)
            levels = goodness[np.arange(1, actions.shape[0] + 1) * step]
            recovered_scales = np.where(actions == 0, marginal * np.exp(-domain["cost_level_elasticity"] * levels), np.nan)
            scales = np.array([np.nanmedian(column) if np.any(np.isfinite(column)) else np.nan for column in recovered_scales.T])
            recovered, bounds, negative_gains, capacity_bound = [], [], [], 0
            active = all(cfg[key] > 0 for key in ("initial_impact_share", "taste_median", "financing_exposure_fraction", "financing_spread"))
            for index, action in enumerate(actions):
                day = (index + 1) * step
                regime = policy["intervention"] if policy["intervention"] is not None and day >= policy["start_day"] else policy["baseline"]
                real, wash, fine = (float(value[0]) for value in factors(
                    np.array([cfg["firm_discount_rate"]]), decision_day=day,
                    horizon_days=cfg["financing_horizon_days"], repricing_interval=cfg["financing_repricing_interval"],
                    period_days=step, implementation_delay=domain["implementation_delay_days"],
                    disclosure_delay=domain["disclosure_delay_days"], audit_probability=regime["audit_probability"],
                ))
                pending = np.zeros(cfg["n_firms"])
                for previous in range(index):
                    if (previous + 1) * step + max(1, domain["implementation_delay_days"]) > day:
                        pending += np.where(actions[previous] == 0, amounts[previous], 0)
                high = (domain["raw_upper"] - domain["initial_mean"]) / domain["initial_sd"]
                cap = np.minimum(domain["max_change_per_period"], np.maximum(high - levels[index] - pending, 0))
                interior = (action == 0) & (amounts[index] > 0) & (amounts[index] < cap - 1e-10)
                capacity_bound += int(np.count_nonzero((action == 0) & ~interior))
                b = (2 * costs[index, interior] / amounts[index, interior] - regime["subsidy"]) / real
                recovered.extend(b.tolist())
                negative_gains.extend((b * (1 - regime["transparency"]) * wash - regime["penalty"] * fine).tolist())
                for firm in np.flatnonzero((action == 2) & active):
                    if cap[firm] <= 0 or not np.isfinite(scales[firm]):
                        raise ValueError("cannot bound a non-interior maintained observation")
                    c = scales[firm] * np.exp(domain["cost_level_elasticity"] * levels[index, firm])
                    upper = max(0.0, (2 * np.sqrt(c * rules["MINIMUM_NPV"]) - regime["subsidy"]) / real)
                    bounds.append({"day": day, "firm_zero_based": int(firm), "benefit_upper_bound": float(upper),
                                   "wash_linear_gain_upper_bound": float(upper * (1 - regime["transparency"]) * wash - regime["penalty"] * fine)})
            all_b.extend(recovered)
            all_upper.extend(item["benefit_upper_bound"] for item in bounds)
            rows.append({"scenario": path.parents[2].name, "seed": cfg["seed"], "action_counts_real_wash_maintain": count.tolist(),
                         "max_inflation": float(inflation.max()), "interior_real_observations": len(recovered),
                         "capacity_bound_real_observations": capacity_bound,
                         "benefit_median": float(np.median(recovered)) if recovered else None,
                         "benefit_maximum": max(recovered) if recovered else None,
                         "wash_linear_gain_maximum": max(negative_gains) if negative_gains else None,
                         "maintain_bounds": bounds, "null_benefit_identically_zero_by_archived_rule": not active,
                         "result_sha256": digest(path), "manifest_sha256": digest(path.with_name("manifest.json"))})
    domain, cfg, baseline = reference["domain"], reference["config"], reference["policy"]["baseline"]
    real, wash, fine = (float(value[0]) for value in factors(
        np.array([cfg["firm_discount_rate"]]), decision_day=60,
        horizon_days=cfg["financing_horizon_days"], repricing_interval=cfg["financing_repricing_interval"],
        period_days=cfg["firm_decision_interval"], implementation_delay=domain["implementation_delay_days"],
        disclosure_delay=domain["disclosure_delay_days"], audit_probability=baseline["audit_probability"],
    ))
    thresholds = []
    for label in ("B", "I", "F", "IF"):
        policy_record = json.loads((ARCHIVES / f"market_{label}/seed_23001/attempt_001/manifest.json").read_text(encoding="utf-8"))["policy"]
        actual_regime = policy_record["intervention"] or policy_record["baseline"]
        transparency, penalty = actual_regime["transparency"], actual_regime["penalty"]
        q = (1 - transparency) * wash
        denominator = q - np.sqrt(domain["wash_cost_ratio"]) * real
        thresholds.append({"regime": label, "transparency": transparency, "penalty": penalty,
                           "positive_wash_b_threshold": penalty * fine / q,
                           "interior_wash_beats_real_b_threshold": penalty * fine / denominator if denominator > 0 else None,
                           "wash_can_beat_real_interior_with_nonnegative_subsidy": bool(denominator > 0)})
    candidates = []
    for label, b, penalty in (("observed_median", float(np.median(all_b)), .005),
                              ("observed_maximum", max(all_b), .005),
                              ("penalty_removed_at_observed_maximum", max(all_b), 0),
                              ("above_positive_threshold", thresholds[0]["positive_wash_b_threshold"] * 1.05, .005),
                              ("above_winner_threshold", thresholds[0]["interior_wash_beats_real_b_threshold"] * 1.05, .005)):
        result = choices(benefit=np.array([b]), cost_of_capital=np.array([cfg["firm_discount_rate"]]),
                         marginal_cost=np.array([.05]), regime=SimpleNamespace(**{**baseline, "penalty": penalty}),
                         domain=SimpleNamespace(**domain), period_days=cfg["firm_decision_interval"], decision_day=60)
        candidates.append({"case": label, "annual_benefit_per_sd": b, "penalty": penalty, "marginal_cost": .05,
                           "action": ("improve", "inflate", "maintain")[result.actions[0]],
                           "amount_sd": float(result.amounts[0]), "npv_fraction_current_cap": float(result.npv[0])})
    equality = []
    for seed in (23001, 23002, 23003):
        with np.load(ARCHIVES / f"market_B/seed_{seed}/attempt_001/result.npz", allow_pickle=False) as baseline_arrays:
            for scenario in ("market_I", "market_F", "market_IF"):
                with np.load(ARCHIVES / f"{scenario}/seed_{seed}/attempt_001/result.npz", allow_pickle=False) as treatment:
                    equality.append({"seed": seed, "scenario": scenario,
                                     "all_recorded_arrays_equal_including_nan": all(np.array_equal(baseline_arrays[key], treatment[key], equal_nan=True) for key in baseline_arrays.files)})
    report = {"status": "development_incentive_diagnostic_only", "generated_utc": datetime.now(timezone.utc).isoformat(),
              "archive_directory": ARCHIVES.relative_to(ROOT).as_posix(), "runs": len(rows),
              "total_action_counts_real_wash_maintain": totals.tolist(), "archived_rule_hashes": hashes,
              "discount_factors": {"real_annuity_years": real, "wash_annuity_years": wash, "eventual_fine_pv_factor": fine},
              "actual_baseline_config": cfg, "actual_baseline_domain": domain,
              "benefit_inversion": {"interior_count": len(all_b), "minimum": min(all_b), "median": float(np.median(all_b)),
                                    "quantile_95": float(np.quantile(all_b, .95)), "maximum": max(all_b),
                                    "maintain_bound_count": len(all_upper), "maximum_maintain_bound": max(all_upper, default=None),
                                    "formula": "b = (2 * resource_cost_fraction / amount - subsidy) / real_annuity; only positive interior real choices",
                                    "is_direct_recording_of_b": False},
              "thresholds": thresholds, "runs_detail": rows,
              "frozen_theoretical_candidate_checks": candidates,
              "policy_arrays_equality": equality,
              "limitations": ["Only the frozen v2 rules and three development seeds; no market reruns or parameter changes.",
                              "The candidate checks use c=.05 and capacity=.25; they are algebra checks, not estimated companies or policy experiments.",
                              "15 v2 runs fail the original no-price-cap gate; no confirmatory or empirical policy claim is licensed.",
                              "Interior FOC recovers b under the recorded model, not a causal or externally estimated financing effect."],
              "diagnostic_code_sha256": digest(Path(__file__))}
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"runs": len(rows), "actions": totals.tolist(), "factors": report["discount_factors"],
                      "benefit": report["benefit_inversion"], "candidates": candidates}, indent=2))


if __name__ == "__main__":
    main()
