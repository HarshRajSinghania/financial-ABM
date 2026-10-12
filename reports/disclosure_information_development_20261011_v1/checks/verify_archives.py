"""Read archived arrays and inputs; do not import or run the market model."""

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DECISION_FIELDS = {
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "audit_selected", "audit_publications", "verified_goodness", "action_due_day",
}
MARKET_FINGERPRINT_FIELDS = (
    "prices", "intrinsic_values", "size_class", "equity_share", "mean_depth_fraction",
    "gross_volume", "price_cap_hits", "total_cash",
)
DISCLOSURE_FINGERPRINT_FIELDS = (
    "true_goodness", "inflation", "impact_share", "impact_wealth_share", "pricing_slope",
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "financing_rate", "financing_cost", "financing_value_adjustment", "public_signal",
    "planning_signal", "disclosure_error", "audit_selected", "audit_publications",
    "verified_goodness", "action_due_day",
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity_hash(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def fingerprint(arrays):
    market = hashlib.sha256(str(int(arrays["market_burn_in_days"])).encode("ascii"))
    for name in MARKET_FINGERPRINT_FIELDS:
        array = np.ascontiguousarray(arrays["market_" + name])
        market.update(str(array.dtype).encode("ascii"))
        market.update(str(array.shape).encode("ascii"))
        market.update(array.tobytes())
    result = hashlib.sha256(market.hexdigest().encode("ascii"))
    for name in DISCLOSURE_FINGERPRINT_FIELDS:
        array = np.ascontiguousarray(arrays[name])
        result.update(str(array.dtype).encode("ascii"))
        result.update(array.tobytes())
    return result.hexdigest()


def compare(expected, actual):
    expected, actual = np.asarray(expected), np.asarray(actual)
    if expected.shape != actual.shape or expected.dtype != actual.dtype:
        return {"status": "FAIL", "expected_shape": list(expected.shape), "actual_shape": list(actual.shape),
                "expected_dtype": str(expected.dtype), "actual_dtype": str(actual.dtype)}
    byte_shape = expected.shape + (expected.dtype.itemsize,)
    same = (np.ascontiguousarray(expected).view(np.uint8).reshape(byte_shape)
            == np.ascontiguousarray(actual).view(np.uint8).reshape(byte_shape)).all(axis=-1)
    if bool(np.all(same)):
        return {"status": "PASS", "mismatches": 0, "maximum_absolute_error": 0.0}
    finite = np.isfinite(expected) & np.isfinite(actual)
    difference = np.abs(np.asarray(expected, dtype=float) - np.asarray(actual, dtype=float))
    return {"status": "FAIL", "mismatches": int(np.count_nonzero(~same)),
            "first_indices": np.argwhere(~same)[:5].tolist(),
            "maximum_absolute_error": float(np.max(difference[finite])) if finite.any() else None}


def regime_at(policy, day):
    return policy["intervention"] if policy["intervention"] is not None and day >= policy["start_day"] else policy["baseline"]


def verify_mechanisms(arrays, manifest):
    config, domain, policy = (manifest[name] for name in ("config", "domain", "policy"))
    days, firms, interval = config["trading_days"], config["n_firms"], config["firm_decision_interval"]
    bounds = domain["direction"] * (np.array([domain["raw_lower"], domain["raw_upper"]]) - domain["initial_mean"]) / domain["initial_sd"]
    low, high = sorted(bounds)
    expected_due = np.full_like(arrays["action_due_day"], -1)
    projects = {}
    for period in range(1, arrays["actions"].shape[0]):
        decision = period * interval
        regime = regime_at(policy, decision)
        delay = regime["disclosure_delay_days"]
        if delay is None:
            delay = domain["disclosure_delay_days"]
        for action, lag in ((0, domain["implementation_delay_days"]), (1, delay)):
            active = arrays["actions"][period] == action
            due = decision + max(1, lag)
            expected_due[period, active] = due
            projects.setdefault(due, []).append((action, active, arrays["amounts"][period]))
    expected_goodness = np.empty_like(arrays["true_goodness"])
    expected_pre = np.empty_like(arrays["inflation"])
    expected_post = np.empty_like(arrays["inflation"])
    expected_error = np.empty_like(arrays["disclosure_error"])
    expected_public = np.empty_like(arrays["public_signal"])
    expected_planning = np.empty_like(arrays["planning_signal"])
    expected_selected = np.zeros_like(arrays["audit_selected"])
    expected_detections = np.zeros_like(arrays["detections"])
    expected_publications = np.zeros_like(arrays["audit_publications"])
    expected_verified = np.zeros_like(arrays["verified_goodness"])
    expected_penalties = np.zeros_like(arrays["penalty_fraction"])
    seeds = np.random.SeedSequence([config["seed"], 1]).spawn(4)
    error_rng, audit_rng = np.random.default_rng(seeds[3]), np.random.default_rng(seeds[1])
    expected_goodness[0] = arrays["true_goodness"][0]
    expected_pre[0] = expected_post[0] = arrays["inflation"][0]
    snapshot = np.zeros(firms)
    expires = np.zeros(firms, dtype=int)
    snapshot_days = 0
    for day in range(days + 1):
        regime = regime_at(policy, day)
        expected_error[day] = regime["disclosure_noise_sd"] * error_rng.standard_normal(firms)
        if day > 0:
            # Commitments retain the date fixed at their own decision day.
            expected_goodness[day] = np.maximum(expected_goodness[day - 1] - domain["natural_decay"] / 252, low)
            expected_pre[day] = expected_post[day - 1]
            for action, active, amounts in projects.get(day, []):
                if action == 0:
                    expected_goodness[day, active] = np.minimum(expected_goodness[day, active] + amounts[active], high)
                else:
                    expected_pre[day, active] += amounts[active]
            expected_pre[day] = np.maximum(np.minimum(expected_pre[day], high - arrays["true_goodness"][day]), 0.0)
            expected_post[day] = expected_pre[day]
        if day > 1 and (day - 1) % interval == 0:
            observation = day - 1
            period = observation // interval
            published = expected_publications[period].astype(bool)
            snapshot[published] = expected_verified[period, published]
            expires[published] = observation + interval
        certified = expires >= day if day > 0 else np.zeros(firms, dtype=bool)
        snapshot_days += int(certified.sum())
        expected_public[day] = arrays["true_goodness"][day] + (1 - regime["transparency"]) * expected_pre[day] + expected_error[day]
        expected_public[day, certified] = snapshot[certified]
        if day > 0 and day % interval == 0:
            period = day // interval
            selected = audit_rng.random(firms) < regime["audit_probability"]
            caught = selected & (expected_pre[day] > 0)
            expected_selected[period] = selected
            expected_detections[period] = caught
            expected_post[day, caught] = 0.0
            expected_publications[period] = selected & regime["publish_audit_results"]
            published = expected_publications[period].astype(bool)
            expected_verified[period, published] = arrays["true_goodness"][day, published]
            expected_penalties[period] = np.where(caught, regime["penalty"] * expected_pre[day], 0.0)
        expected_planning[day] = arrays["true_goodness"][day] + (1 - regime["transparency"]) * expected_post[day] + expected_error[day]
        expected_planning[day, certified] = snapshot[certified]
    checks = {name: compare(expected, arrays[actual]) for name, expected, actual in (
        ("new_commitment_due_day", expected_due, "action_due_day"),
        ("true_state_from_decay_and_due_improvements", expected_goodness, "true_goodness"),
        ("post_audit_inflation_from_due_wash", expected_post, "inflation"),
        ("daily_error_independent_rng_replay", expected_error, "disclosure_error"),
        ("audit_selection_independent_rng_replay", expected_selected, "audit_selected"),
        ("detections_from_pre_audit_stock", expected_detections, "detections"),
        ("audit_publication_events", expected_publications, "audit_publications"),
        ("dated_verified_snapshot_values", expected_verified, "verified_goodness"),
        ("fine_from_pre_audit_stock", expected_penalties, "penalty_fraction"),
        ("trading_signal_from_pre_audit_stock", expected_public, "public_signal"),
        ("planning_signal_from_post_audit_stock", expected_planning, "planning_signal"),
    )}
    checks["valid_action_codes_and_amounts"] = {"status": "PASS" if (
        np.isin(arrays["actions"], (0, 1, 2)).all()
        and np.all(arrays["amounts"][arrays["actions"] == 2] == 0)
        and np.all(arrays["amounts"][arrays["actions"] != 2] > 0)
    ) else "FAIL"}
    return checks, snapshot_days


def main():
    frozen, summary = read_json(ROOT / "experiment.json"), read_json(ROOT / "summary.json")
    summary_manifest = read_json(ROOT / "summary_manifest.json")
    experiment_checks = {
        "experiment_identity": identity_hash({key: value for key, value in frozen.items() if key != "experiment_id"}) == frozen["experiment_id"],
        "summary_hash": sha256(ROOT / "summary.json") == summary_manifest["summary_sha256"],
        "summary_identity": summary["experiment_id"] == summary_manifest["experiment_id"] == frozen["experiment_id"],
        "completed_grid": len(summary["records"]) == summary["complete_trials"] == summary["planned_trials"] == 24,
        "records_match_grid": {(row["scenario"], row["seed"]) for row in summary["records"]}
                              == {(row["name"], seed) for row in frozen["scenarios"] for seed in frozen["spec"]["seeds"]},
    }
    scenarios = {item["name"]: item for item in frozen["scenarios"]}
    loaded, trials, pairs = {}, [], []
    for record in summary["records"]:
        folder = ROOT / record["path"]
        manifest = read_json(folder / "manifest.json")
        metrics, validation = read_json(folder / "metrics.json"), read_json(folder / "validation.json")
        artifact_checks = {name: sha256(folder / name) == expected for name, expected in manifest["artifacts"].items()}
        with ZipFile(folder / "source.zip") as archive:
            source_checks = {name: hashlib.sha256(archive.read(name)).hexdigest() == expected
                             for name, expected in frozen["source_hashes"].items()}
            source_checks["exact_source_file_set"] = set(archive.namelist()) == set(frozen["source_hashes"])
        scenario = scenarios[record["scenario"]]
        expected_config = {**scenario["config"], "seed": record["seed"]}
        identity = {"schema_version": 1, "config": expected_config, "domain": scenario["domain"],
                    "policy": scenario["policy"], "source_hashes": frozen["source_hashes"],
                    "python_version": frozen["python_version"], "numpy_version": frozen["numpy_version"]}
        identity_checks = {
            "run_id": identity_hash(identity) == manifest["run_id"],
            "frozen_inputs": all(manifest[name] == identity[name] for name in identity),
            "summary_metrics_match_archive": metrics == record["metrics"],
            "summary_validation_matches_archive": validation == record["validation"],
            "status_complete": record["status"] == manifest["status"] == "complete",
        }
        with np.load(folder / "result.npz", allow_pickle=False) as archive:
            arrays = {name: archive[name].copy() for name in archive.files}
        identity_checks["result_fingerprint"] = fingerprint(arrays) == manifest["result_fingerprint"] == record["result_fingerprint"]
        mechanisms, snapshot_days = verify_mechanisms(arrays, manifest)
        interval, burn = expected_config["firm_decision_interval"], expected_config["burn_in_days"]
        decision_days = np.arange(arrays["actions"].shape[0]) * interval
        real_rows, post_rows = decision_days > 0, decision_days > burn
        counts = lambda mask: {label: int(np.count_nonzero(arrays["actions"][mask] == code))
                               for code, label in ((0, "improve"), (1, "wash"), (2, "maintain"))}
        core = {name: validation[name]["status"] for name in ("mechanical", "stylized")}
        trial = {"scenario": record["scenario"], "seed": record["seed"], "path": record["path"],
                 "manifest_sha256": sha256(folder / "manifest.json"), "artifact_checks": artifact_checks,
                 "source_files_checked": len(frozen["source_hashes"]), "source_checks_pass": all(source_checks.values()),
                 "identity_checks": identity_checks, "mechanism_checks": mechanisms,
                 "counts": {"all_decisions": counts(real_rows), "decisions_after_day_600": counts(post_rows),
                            "detections": int(arrays["detections"].sum()), "publications": int(arrays["audit_publications"].sum()),
                            "publications_first_visible_by_end": int(arrays["audit_publications"][decision_days + 1 <= expected_config["trading_days"]].sum()),
                            "publications_pending_after_end": int(arrays["audit_publications"][decision_days + 1 > expected_config["trading_days"]].sum()),
                            "certified_firm_days": snapshot_days},
                 "validation": {**core, **{name: validation[name]["status"] for name in (
                     "return_acf", "cross_asset_correlation", "empirical_calibration")}},
                 "archived_metrics": {name: metrics[name] for name in ("true_change", "inflation")}}
        trial["mechanism_status"] = "PASS" if all(value["status"] == "PASS" for value in mechanisms.values()) else "FAIL"
        trial["archive_status"] = "PASS" if all(artifact_checks.values()) and all(source_checks.values()) and all(identity_checks.values()) else "FAIL"
        trials.append(trial)
        loaded[record["scenario"], record["seed"]] = (arrays, manifest)
    for comparison in frozen["spec"]["comparisons"]:
        baseline = next(name for name, weight in comparison["weights"].items() if weight == -1)
        changed = next(name for name, weight in comparison["weights"].items() if weight == 1)
        for seed in frozen["spec"]["seeds"]:
            before, bm = loaded[baseline, seed]
            after, am = loaded[changed, seed]
            burn, interval = bm["config"]["burn_in_days"], bm["config"]["firm_decision_interval"]
            prefix = {}
            for name in before:
                limit = burn // interval + 1 if name in DECISION_FIELDS else burn + 1
                a, b = before[name], after[name]
                if name not in DECISION_FIELDS and (a.ndim == 0 or a.shape[0] != bm["config"]["trading_days"] + 1):
                    prefix[name] = compare(a, b)
                else:
                    prefix[name] = compare(a[:limit], b[:limit])
            fixed = ("audit_probability", "penalty", "subsidy", "transparency")
            policy_fixed = (bm["config"] == am["config"] and bm["domain"] == am["domain"]
                            and bm["policy"]["baseline"] == am["policy"]["baseline"]
                            and all(regime_at(bm["policy"], day)[key] == regime_at(am["policy"], day)[key]
                                    for day in (0, burn, burn + 1) for key in fixed))
            differences = {}
            for name in ("market_prices", "public_signal", "planning_signal", "true_goodness", "inflation", "actions", "amounts"):
                start = burn // interval + 1 if name in DECISION_FIELDS else burn + 1
                a, b = before[name][start:], after[name][start:]
                differences[name] = {"different_entries": int(np.count_nonzero(a != b)),
                                     "maximum_absolute_difference": float(np.max(np.abs(a - b)))}
            pairs.append({"comparison": comparison["name"], "seed": seed, "history_through_day": burn,
                          "all_archived_prefix_fields_equal": all(value["status"] == "PASS" for value in prefix.values()),
                          "prefix_field_checks": prefix, "audit_selection_equal_full_run": bool(np.array_equal(before["audit_selected"], after["audit_selected"])),
                          "enforcement_transfer_transparency_and_financing_fixed": policy_fixed,
                          "after_policy_differences": differences})
    scenario_counts = []
    for name in scenarios:
        rows = [trial for trial in trials if trial["scenario"] == name]
        scenario_counts.append({"scenario": name, "seeds": len(rows),
            "actions_all_decisions": {label: sum(row["counts"]["all_decisions"][label] for row in rows) for label in ("improve", "wash", "maintain")},
            "actions_after_day_600": {label: sum(row["counts"]["decisions_after_day_600"][label] for row in rows) for label in ("improve", "wash", "maintain")},
            "detections": sum(row["counts"]["detections"] for row in rows),
            "publications": sum(row["counts"]["publications"] for row in rows),
            "publications_first_visible_by_end": sum(row["counts"]["publications_first_visible_by_end"] for row in rows),
            "publications_pending_after_end": sum(row["counts"]["publications_pending_after_end"] for row in rows),
            "core_failed_trials": sum(any(row["validation"][key] != "PASS" for key in ("mechanical", "stylized")) for row in rows)})
    validation_counts = {name: {status: sum(row["validation"][name] == status for row in trials)
                               for status in sorted({row["validation"][name] for row in trials})}
                         for name in ("mechanical", "stylized", "return_acf", "cross_asset_correlation", "empirical_calibration")}
    experiment_checks["archived_core_failure_count"] = summary["trials_failing_core_validation"] == sum(row["core_failed_trials"] for row in scenario_counts)
    passed = all(experiment_checks.values()) and all(trial["archive_status"] == trial["mechanism_status"] == "PASS" for trial in trials) and len(pairs) == 18 and all(
        pair["all_archived_prefix_fields_equal"] and pair["audit_selection_equal_full_run"] and pair["enforcement_transfer_transparency_and_financing_fixed"] for pair in pairs)
    result = {"status": "PASS" if passed else "FAIL", "verification_kind": "archive_integrity_and_information_mechanism_reconstruction",
              "experiment_id": frozen["experiment_id"], "purpose": summary["purpose"],
              "claim_support": summary["claim_support"], "market_simulations_performed": 0,
              "verifier_sha256": sha256(Path(__file__)), "input_hashes": {name: sha256(ROOT / name) for name in ("experiment.json", "summary.json", "summary_manifest.json")},
              "experiment_checks": experiment_checks, "trials_checked": len(trials), "paired_comparisons_checked": len(pairs),
              "daily_firm_observations_checked": sum((row["config"]["trading_days"] + 1) * row["config"]["n_firms"] for _, row in loaded.values()),
              "array_comparison": "Exact dtype, shape and per-entry bytes, including signed zero and NaN payloads; no tolerance or filled observations.",
              "reconstruction": {"inflation": "Previous post-audit stock plus each due wash commitment in decision order, bounded by high minus archived current goodness; selected positive stock clears after trading.",
                "signal": "Pre-audit stock for immutable trading signal; post-audit stock for planning; identical replayed daily error. Public snapshot observed at a is used on a+1 through a+D only.",
                "error": "Independent replay of SeedSequence([seed,1]).spawn(4)[3]; all days including day0 and sigma0 consume n_firms standard normals.",
                "initial_state": "Initial true goodness and inflation are conditioned on the archived day0 state; subsequent real changes and decay are reconstructed.",
                "source": "Only archived inputs, arrays and source bytes are read. No simulation, NPV or market/statistical re-estimation is invoked."},
              "core_failed_trials": sum(row["core_failed_trials"] for row in scenario_counts),
              "validation_status_counts": validation_counts,
              "empirical_calibration": next(iter(validation_counts["empirical_calibration"])) if len(validation_counts["empirical_calibration"]) == 1 else "mixed",
              "limitations": ["Three development seeds per scenario, not the 30-seed confirmatory requirement.",
                "Mechanism PASS cannot override market FAIL or pending empirical calibration.", "Independent error replay verifies the recorded noise process, not its empirical realism.",
                "Disclosure delay changes new inflated-report projects only; reporting frequency and private investor signals are not modeled."],
              "scenario_counts": scenario_counts, "trials": trials, "pairs": pairs}
    (ROOT / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("status", "trials_checked", "paired_comparisons_checked", "daily_firm_observations_checked", "core_failed_trials", "empirical_calibration")}, indent=2))
    for row in scenario_counts:
        print(json.dumps(row, ensure_ascii=False))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
