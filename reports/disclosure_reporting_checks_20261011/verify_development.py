"""Independently reconstruct archived reporting paths without importing ABM."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "reports/disclosure_reporting_development_20261011_v1"
EXPERIMENT_ID = "01176fafb9c42d3eb49b7661938b2ef21ae1bd62885fafbf156ad23bb6c2e20b"
DECISION_FIELDS = {
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "audit_selected", "audit_publications", "verified_goodness", "action_due_day",
    "learning_states", "learning_groups", "valid_actions", "learning_rewards",
    "learning_transition", "unvisited_state", "learning_choices",
}
MARKET_FIELDS = ("prices", "intrinsic_values", "size_class", "equity_share", "mean_depth_fraction",
                 "gross_volume", "price_cap_hits", "total_cash")
DISCLOSURE_FIELDS = (
    "true_goodness", "inflation", "impact_share", "impact_wealth_share", "pricing_slope",
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "financing_rate", "financing_cost", "financing_value_adjustment", "public_signal",
    "planning_signal", "disclosure_error", "audit_selected", "audit_publications",
    "verified_goodness", "action_due_day", "applied_resource_cost", "applied_fine", "applied_subsidy",
    "learning_states", "learning_groups", "valid_actions", "learning_rewards", "learning_transition",
    "unvisited_state", "learning_choices",
)
GATES = ("mechanical", "stylized", "return_acf", "cross_asset_correlation", "empirical_calibration")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode("utf-8")).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def compare(expected, actual):
    expected, actual = np.asarray(expected), np.asarray(actual)
    if expected.shape != actual.shape or expected.dtype != actual.dtype:
        return {"status": "FAIL", "expected_shape": list(expected.shape), "actual_shape": list(actual.shape),
                "expected_dtype": str(expected.dtype), "actual_dtype": str(actual.dtype)}
    if expected.tobytes() == actual.tobytes():
        return {"status": "PASS", "entries": int(expected.size), "mismatches": 0}
    shape = expected.shape + (expected.dtype.itemsize,)
    same = (np.ascontiguousarray(expected).view(np.uint8).reshape(shape)
            == np.ascontiguousarray(actual).view(np.uint8).reshape(shape)).all(axis=-1)
    finite = np.isfinite(expected) & np.isfinite(actual)
    return {"status": "FAIL", "entries": int(expected.size), "mismatches": int((~same).sum()),
            "first_indices": np.argwhere(~same)[:5].tolist(),
            "maximum_absolute_error": float(np.max(np.abs(expected[finite].astype(float) - actual[finite].astype(float)))) if finite.any() else None}


def fingerprint(arrays):
    market = hashlib.sha256(str(int(arrays["market_burn_in_days"])).encode("ascii"))
    for name in MARKET_FIELDS:
        array = np.ascontiguousarray(arrays["market_" + name])
        market.update(str(array.dtype).encode("ascii"))
        market.update(str(array.shape).encode("ascii"))
        market.update(array.tobytes())
    result = hashlib.sha256(market.hexdigest().encode("ascii"))
    for name in DISCLOSURE_FIELDS:
        if name in arrays:
            array = np.ascontiguousarray(arrays[name])
            result.update(str(array.dtype).encode("ascii"))
            result.update(array.tobytes())
    return result.hexdigest()


def regime_at(policy, day):
    return policy["intervention"] if policy["intervention"] is not None and day >= policy["start_day"] else policy["baseline"]


def reconstruct(arrays, manifest):
    config, domain, policy = (manifest[name] for name in ("config", "domain", "policy"))
    days, firms, period = config["trading_days"], config["n_firms"], config["firm_decision_interval"]
    window_start = policy["start_day"]
    low, high = sorted(domain["direction"] * (np.array([domain["raw_lower"], domain["raw_upper"]])
                                              - domain["initial_mean"]) / domain["initial_sd"])
    expected = {name: np.zeros_like(arrays[name]) for name in (
        "true_goodness", "inflation", "disclosure_error", "public_signal", "planning_signal",
        "audit_selected", "detections", "audit_publications", "verified_goodness", "penalty_fraction",
    )}
    expected_due = np.full_like(arrays["action_due_day"], -1)
    goodness, inflation = arrays["true_goodness"][0].copy(), arrays["inflation"][0].copy()
    seeds = np.random.SeedSequence([config["seed"], 1]).spawn(4)
    error_rng, audit_rng = np.random.default_rng(seeds[3]), np.random.default_rng(seeds[1])
    pending = []
    snapshot, expires = np.zeros(firms), np.zeros(firms, dtype=np.int64)
    regular_days = []
    counts = {"window_start_day": window_start, "window_end_day": days,
              "selected_close_updates_window": 0, "selected_close_updates_on_regular_days_window": 0,
              "selected_close_updates_off_calendar_window": 0, "selected_updates_changing_report_window": 0,
              "certified_company_days_all": 0, "certified_company_days_window": 0}
    feasible = True
    for day in range(days + 1):
        regime = regime_at(policy, day)
        error = regime["disclosure_noise_sd"] * error_rng.standard_normal(firms)
        expected["disclosure_error"][day] = error
        if day:
            goodness = np.maximum(goodness - domain["natural_decay"] / 252, low)
            outstanding = []
            for due, kind, indices, amounts in pending:
                if due > day:
                    outstanding.append((due, kind, indices, amounts))
                elif kind == 0:
                    goodness[indices] = np.minimum(goodness[indices] + amounts, high)
                else:
                    inflation[indices] += amounts
            pending = outstanding
            inflation = np.maximum(np.minimum(inflation, high - goodness), 0.0)
        if day > 1 and (day - 1) % period == 0:
            previous = (day - 1) // period
            published = expected["audit_publications"][previous].astype(bool)
            snapshot[published] = expected["verified_goodness"][previous, published]
            expires[published] = day - 1 + period
        certified = expires >= day if day else np.zeros(firms, dtype=bool)
        counts["certified_company_days_all"] += int(certified.sum())
        if day >= window_start:
            counts["certified_company_days_window"] += int(certified.sum())
        regular = day == 0 or day % regime["reporting_interval_days"] == 0
        if regular:
            report = goodness + (1.0 - regime["transparency"]) * inflation + error
            regular_days.append(day)
        trade = report.copy()
        trade[certified] = snapshot[certified]
        expected["public_signal"][day] = trade
        if day and day % period == 0:
            row = day // period
            selected = audit_rng.random(firms) < regime["audit_probability"]
            caught = selected & (inflation > 0)
            expected["audit_selected"][row] = selected
            expected["detections"][row] = caught
            expected["penalty_fraction"][row] = np.where(caught, regime["penalty"] * inflation, 0.0)
            inflation[caught] = 0.0
            old_report = report.copy()
            report[selected] = (goodness + (1.0 - regime["transparency"]) * inflation)[selected] + error[selected]
            published = selected & regime["publish_audit_results"]
            expected["audit_publications"][row] = published
            expected["verified_goodness"][row, published] = goodness[published]
            if day >= window_start:
                counts["selected_close_updates_window"] += int(selected.sum())
                counts["selected_close_updates_on_regular_days_window"] += int(selected.sum()) if regular else 0
                counts["selected_close_updates_off_calendar_window"] += int(selected.sum()) if not regular else 0
                counts["selected_updates_changing_report_window"] += int(np.count_nonzero(report[selected] != old_report[selected]))
            real_cap, wash_cap = high - goodness, high - goodness - inflation
            for _, kind, indices, amounts in pending:
                if kind == 0:
                    np.subtract.at(real_cap, indices, amounts)
                np.subtract.at(wash_cap, indices, amounts)
            actions, amounts = arrays["actions"][row], arrays["amounts"][row]
            feasible &= bool(np.isfinite(amounts).all() and np.isin(actions, (0, 1, 2)).all()
                             and np.all(amounts[actions == 2] == 0)
                             and np.all(amounts[actions != 2] > 0)
                             and np.all(amounts <= domain["max_change_per_period"]))
            delay = regime["disclosure_delay_days"]
            delay = domain["disclosure_delay_days"] if delay is None else delay
            for kind, lag, capacity in ((0, domain["implementation_delay_days"], real_cap), (1, delay, wash_cap)):
                indices = np.flatnonzero(actions == kind)
                feasible &= bool(np.all(amounts[indices] <= np.maximum(capacity[indices], 0.0)))
                due = day + max(1, lag)
                expected_due[row, indices] = due
                if indices.size:
                    pending.append((due, kind, indices, amounts[indices].copy()))
        planning = report.copy()
        planning[certified] = snapshot[certified]
        expected["planning_signal"][day] = planning
        expected["true_goodness"][day] = goodness
        expected["inflation"][day] = inflation
    checks = {name: compare(value, arrays[name]) for name, value in expected.items()}
    checks["action_due_day"] = compare(expected_due, arrays["action_due_day"])
    checks["action_codes_amounts_and_reserved_capacity"] = {"status": "PASS" if feasible else "FAIL"}
    counts["regular_publication_days_all"] = regular_days
    counts["regular_publication_days_window"] = [day for day in regular_days if day >= window_start]
    counts["regular_publication_count_window"] = len(counts["regular_publication_days_window"])
    counts["regular_report_company_updates_window"] = firms * counts["regular_publication_count_window"]
    decision_days = np.arange(arrays["actions"].shape[0]) * period
    window_rows = decision_days >= window_start
    counts["actions_window"] = {label: int(np.count_nonzero(arrays["actions"][window_rows] == kind))
                                for kind, label in ((0, "improve"), (1, "wash"), (2, "maintain"))}
    counts["detections_window"] = int(arrays["detections"][window_rows].sum())
    counts["publications_window"] = int(arrays["audit_publications"][window_rows].sum())
    counts["publications_pending_after_end"] = int(arrays["audit_publications"][decision_days + 1 > days].sum())
    return checks, counts


def verify_trial(record, frozen, protected):
    folder = (ROOT / record["path"]).resolve()
    assert folder.is_relative_to(ROOT)
    manifest_path = folder / "manifest.json"
    protected[manifest_path] = sha(manifest_path)
    manifest = read_json(manifest_path)
    scenario = next(item for item in frozen["scenarios"] if item["name"] == record["scenario"])
    identity = {"schema_version": 1, "config": {**scenario["config"], "seed": record["seed"]},
                "domain": scenario["domain"], "policy": scenario["policy"], "source_hashes": frozen["source_hashes"],
                "python_version": frozen["python_version"], "numpy_version": frozen["numpy_version"]}
    identity_checks = {"frozen_inputs": all(manifest.get(name) == value for name, value in identity.items()),
                       "run_id": identity_hash(identity) == manifest["run_id"],
                       "status_complete": record["status"] == manifest["status"] == "complete",
                       "expected_artifact_set": set(manifest.get("artifacts", {})) == {"source.zip", "result.npz", "metrics.json", "validation.json"}}
    artifact_checks = {}
    for name, expected in manifest.get("artifacts", {}).items():
        path = (folder / name).resolve()
        assert path.is_relative_to(folder)
        protected[path] = sha(path)
        artifact_checks[name] = protected[path] == expected
    trial = {"scenario": record["scenario"], "seed": record["seed"], "path": record["path"],
             "manifest_sha256": protected[manifest_path], "identity_checks": identity_checks,
             "artifact_checks": artifact_checks}
    if record["status"] != "complete" or manifest["status"] != "complete":
        return {**trial, "archive_status": "FAIL", "mechanism_status": "not_checked",
                "error": manifest.get("error"), "validation": {}}, None
    with ZipFile(folder / "source.zip") as archive:
        source_checks = {name: hashlib.sha256(archive.read(name)).hexdigest() == value
                         for name, value in frozen["source_hashes"].items()}
        source_checks["exact_file_set"] = (len(archive.namelist()) == len(frozen["source_hashes"])
                                           and set(archive.namelist()) == set(frozen["source_hashes"]))
    metrics, validation = read_json(folder / "metrics.json"), read_json(folder / "validation.json")
    identity_checks["summary_metrics"] = metrics == record["metrics"]
    identity_checks["summary_validation"] = validation == record["validation"]
    with np.load(folder / "result.npz", allow_pickle=False) as archive:
        arrays = {name: archive[name].copy() for name in archive.files}
    identity_checks["result_fingerprint"] = fingerprint(arrays) == manifest["result_fingerprint"] == record["result_fingerprint"]
    checks, counts = reconstruct(arrays, manifest)
    trial.update({"source_checks": source_checks, "source_files_checked": len(frozen["source_hashes"]),
                  "mechanism_checks": checks, "counts": counts,
                  "validation": {name: validation[name]["status"] for name in GATES},
                  "archived_metrics": {name: metrics[name] for name in ("true_change", "inflation")}})
    trial["archive_status"] = "PASS" if all(identity_checks.values()) and all(artifact_checks.values()) and all(source_checks.values()) else "FAIL"
    trial["mechanism_status"] = "PASS" if all(check["status"] == "PASS" for check in checks.values()) else "FAIL"
    return trial, (arrays, manifest)


def verify_pairs(frozen, loaded):
    pairs = []
    for contrast in frozen["spec"]["comparisons"]:
        baseline = next(name for name, weight in contrast["weights"].items() if weight == -1)
        changed = next(name for name, weight in contrast["weights"].items() if weight == 1)
        for seed in frozen["spec"]["seeds"]:
            if (baseline, seed) not in loaded or (changed, seed) not in loaded:
                pairs.append({"comparison": contrast["name"], "seed": seed, "status": "FAIL", "reason": "missing completed path"})
                continue
            before, bm = loaded[baseline, seed]
            after, am = loaded[changed, seed]
            start, period = bm["policy"]["start_day"], bm["config"]["firm_decision_interval"]
            prefix = {}
            same_fields = set(before) == set(after)
            for name in sorted(set(before) & set(after)):
                a, b = before[name], after[name]
                if name in DECISION_FIELDS:
                    prefix[name] = compare(a[:(start - 1) // period + 1], b[:(start - 1) // period + 1])
                elif a.ndim and a.shape[0] == bm["config"]["trading_days"] + 1:
                    prefix[name] = compare(a[:start], b[:start])
                else:
                    prefix[name] = compare(a, b)
            fixed = ("audit_probability", "penalty", "subsidy", "transparency", "disclosure_noise_sd", "disclosure_delay_days")
            policy_fixed = (bm["config"] == am["config"] and bm["domain"] == am["domain"]
                            and bm["policy"]["baseline"] == am["policy"]["baseline"]
                            and bm["policy"]["start_day"] == am["policy"]["start_day"]
                            and all(regime_at(bm["policy"], day)[key] == regime_at(am["policy"], day)[key]
                                    for day in (0, start - 1, start) for key in fixed))
            audit = compare(before["audit_selected"], after["audit_selected"])
            error = compare(before["disclosure_error"], after["disclosure_error"])
            differences = {}
            for name in ("market_prices", "public_signal", "planning_signal", "true_goodness", "inflation", "actions", "amounts"):
                first = (start - 1) // period + 1 if name in DECISION_FIELDS else start
                a, b = before[name][first:], after[name][first:]
                differences[name] = {"different_entries": int(np.count_nonzero(a != b)),
                                     "maximum_absolute_difference": float(np.max(np.abs(a - b)))}
            passed = same_fields and policy_fixed and all(value["status"] == "PASS" for value in prefix.values()) and audit["status"] == error["status"] == "PASS"
            pairs.append({"comparison": contrast["name"], "seed": seed, "status": "PASS" if passed else "FAIL",
                          "history_through_day": start - 1, "same_field_set": same_fields,
                          "prefix_checks": prefix, "full_audit_selection": audit, "full_daily_errors": error,
                          "other_instruments_domain_and_market_inputs_fixed": policy_fixed,
                          "after_policy_differences": differences})
    return pairs


def main():
    output, interpretation = HERE / "development_verification.json", HERE / "development_interpretation.md"
    if output.exists() or interpretation.exists():
        raise FileExistsError("Verification outputs already exist; preserve this attempt.")
    protected = {ROOT / name: sha(ROOT / name) for name in ("experiment.json", "summary.json", "summary_manifest.json")}
    frozen, summary, summary_manifest = (read_json(ROOT / name) for name in ("experiment.json", "summary.json", "summary_manifest.json"))
    expected_grid = {(item["name"], seed) for item in frozen["scenarios"] for seed in frozen["spec"]["seeds"]}
    checks = {
        "experiment_identity": identity_hash({key: value for key, value in frozen.items() if key != "experiment_id"}) == frozen["experiment_id"] == EXPERIMENT_ID,
        "summary_hash": protected[ROOT / "summary.json"] == summary_manifest["summary_sha256"],
        "summary_identity": summary["experiment_id"] == summary_manifest["experiment_id"] == frozen["experiment_id"],
        "planned_18_trials": len(expected_grid) == len(summary["records"]) == summary["planned_trials"] == 18,
        "completed_grid": summary["complete_trials"] == 18 and all(row["status"] == "complete" for row in summary["records"]),
        "records_match_grid": {(row["scenario"], row["seed"]) for row in summary["records"]} == expected_grid,
        "source_file_count": len(frozen["source_hashes"]) == 52,
    }
    report = {"status": "running", "created_utc": datetime.now(timezone.utc).isoformat(),
              "verification_kind": "archival_integrity_and_reporting_mechanism_reconstruction",
              "verifier_sha256": sha(Path(__file__)), "experiment_id": frozen["experiment_id"],
              "purpose": summary["purpose"], "claim_support": summary["claim_support"],
              "market_simulations_performed": 0, "experiment_checks": checks, "trials": [], "pairs": []}
    write_json(output, report)
    loaded = {}
    active = None
    try:
        for record in summary["records"]:
            active = record["path"]
            trial, data = verify_trial(record, frozen, protected)
            report["trials"].append(trial)
            if data is not None:
                loaded[record["scenario"], record["seed"]] = data
            write_json(output, report)
        report["pairs"] = verify_pairs(frozen, loaded)
        counts = {name: {status: sum(trial["validation"].get(name, "not_checked") == status for trial in report["trials"])
                         for status in sorted({trial["validation"].get(name, "not_checked") for trial in report["trials"]})}
                  for name in GATES}
        core_failed = sum(any(trial["validation"].get(gate) != "PASS" for gate in ("mechanical", "stylized")) for trial in report["trials"])
        checks["core_failure_count_preserved"] = core_failed == summary["trials_failing_core_validation"]
        checks["original_archives_unchanged"] = all(path.is_file() and sha(path) == value for path, value in protected.items())
        checks["verifier_unchanged"] = sha(Path(__file__)) == report["verifier_sha256"]
        planned_pairs = len(frozen["spec"]["comparisons"]) * len(frozen["spec"]["seeds"])
        checks["complete_pair_count"] = len(report["pairs"]) == planned_pairs == 21
        passed = (all(checks.values()) and all(trial["archive_status"] == trial["mechanism_status"] == "PASS" for trial in report["trials"])
                  and all(pair["status"] == "PASS" for pair in report["pairs"]))
        report.update({"status": "PASS" if passed else "FAIL", "trials_checked": len(report["trials"]),
                       "completed_paths_reconstructed": len(loaded), "paired_comparisons_checked": len(report["pairs"]),
                       "daily_firm_observations_checked": sum((manifest["config"]["trading_days"] + 1) * manifest["config"]["n_firms"] for _, manifest in loaded.values()),
                       "input_hashes": {path.relative_to(ROOT).as_posix(): value for path, value in protected.items()},
                       "validation_status_counts": counts, "core_failed_trials": core_failed,
                       "reconstruction": {"initial_state": "Conditioned on archived day0 g and w; subsequent states use daily decay and committed actions with due dates independently calculated at commitment.",
                                          "ordinary_report": "Global calendar from the active regime; held report includes its publication-day error. Selected audits update only that firm's report after clearing, with that day's fixed error.",
                                          "audit_timing": "Trading uses pre-audit stock; planning uses post-audit updated reports. Previously available certificates override both; today's new certificate starts tomorrow and expires after D days.",
                                          "random_streams": "Independent SeedSequence([seed,1]).spawn(4) replay, stream1 audits and stream3 daily errors; every day including day0 and sigma0 consumes a full error vector.",
                                          "counts": "Window counts include days start_day through trading_days. Every selected close report counts as an extra update even on regular days or if its numeric value is unchanged; off-calendar and value-changing subsets are separate."},
                       "limitations": ["No market, NPV optimizer, financing ledger, statistical test or empirical calibration is rerun; archived action choices are inputs, not independently validated optimal choices.",
                                       "Three previously inspected development seeds are not confirmatory or independent validation.",
                                       "Synchronous global publication phase is fixed; report frequency changes noise persistence and information age as well as project visibility.",
                                       "Audits concern completed records before investor publication and require ordinary updates; this is a modeling assumption, not a statutory fact.",
                                       "Mechanism PASS does not override market or coverage FAIL, pending empirical calibration, or unknown implementation costs."]})
        write_json(output, report)
        lines = [f"# 报告频率开发档案独立核验：{report['status']}", "",
                 f"实验身份 `{report['experiment_id']}`。核对 {len(report['trials'])} 档、{len(report['pairs'])} 对比较、{report['daily_firm_observations_checked']:,} 个公司日；新增市场运行 0。",
                 "",
                 "逐档验证输入身份、全部工件和源码 ZIP 哈希，并独立重建衰减、到期行动、核查清零、普通报告缓存及有限期认证。政策前全部存档字段按字节比较，整程核查选中与每日潜在误差流须相同。",
                 "",
                 f"市场核心门槛失败 {core_failed} 档。原门槛状态保留：`{json.dumps(counts, ensure_ascii=False)}`。机制核验通过不能消除市场失败或经验校准待定。",
                 "",
                 "下表窗口为601日至1800日；常规发布数按每家公司日历计，核查更新和认证覆盖按公司计。核查更新含常规发布日的第二次收盘更新，括号中为非发布日更新。", "",
                 "| 场景 | 种子 | 常规发布次数 | 核查额外更新（非发布日） | 认证覆盖公司日 |",
                 "|---|---:|---:|---:|---:|"]
        for trial in report["trials"]:
            if "counts" in trial:
                value = trial["counts"]
                lines.append(f"| {trial['scenario']} | {trial['seed']} | {value['regular_publication_count_window']} | {value['selected_close_updates_window']}（{value['selected_close_updates_off_calendar_window']}） | {value['certified_company_days_window']} |")
        lines += ["", "完整字段检查、实际价格/信号差异、动作数量及哈希见 development_verification.json。", "",
                  "三个种子已在此前开发阶段检查过；本次不是独立验证，也不检验政策排序。共同日历相位固定，频率同时改变噪声持久性和信息时效。行动选择、局部融资预测和经济账目未在此脚本重新求解；监管实施成本仍未知。"]
        interpretation.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(json.dumps({name: report[name] for name in ("status", "trials_checked", "paired_comparisons_checked", "daily_firm_observations_checked", "core_failed_trials")}), flush=True)
        if not passed:
            raise SystemExit(1)
    except BaseException as error:
        if report["status"] == "running":
            report["status"] = "FAIL"
            report["error"] = {"archive": active, "type": type(error).__name__, "message": str(error)}
            write_json(output, report)
        raise


if __name__ == "__main__":
    main()
