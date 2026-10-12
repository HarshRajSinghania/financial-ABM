"""Continue only the remaining frozen worlds, preserving the stopped run."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
import importlib.util
import json
import os
from pathlib import Path
import platform
import time
import traceback

HERE = Path(__file__).resolve().parent
CONT_PATH = HERE / "continuation.json"
CONT = json.loads(CONT_PATH.read_text(encoding="utf-8"))
BASE_PATH = HERE / "run_frozen.py"


def file_sha(path):
    import hashlib
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


for name, digest in CONT["frozen_artifacts"].items():
    if file_sha(HERE / name) != digest:
        raise RuntimeError("Original frozen artifact changed: " + name)
module_spec = importlib.util.spec_from_file_location("qualification_original", BASE_PATH)
base = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(base)

np = base.np
SPEC = base.SPEC
MarketConfig, CrossSectionMarket, Recorder = base.MarketConfig, base.CrossSectionMarket, base.Recorder
validate_market, compute_moments = base.validate_market, base.compute_moments
TRADING_DAYS_PER_YEAR, MOMENT_NAMES = base.TRADING_DAYS_PER_YEAR, base.MOMENT_NAMES
GlobalStop, require = base.GlobalStop, base.require
sha, array_sha, distribution = base.sha, base.array_sha, base.distribution
write_json, resource_check = base.write_json, base.resource_check


def verify_sources(contract=None):
    base.verify_sources()
    for name, digest in CONT["frozen_artifacts"].items():
        require(sha(HERE / name) == digest, "Original frozen artifact changed: " + name)
    if contract is not None:
        require(sha(CONT_PATH) == contract["spec_sha256"], "Continuation spec changed")
        require(sha(Path(__file__)) == contract["launcher_sha256"], "Continuation launcher changed")


def verify_preserved():
    for name, digest in CONT["preserved_files"].items():
        require(sha(HERE / name) == digest, "Preserved stopped-run artifact changed: " + name)


def load_record(case, contract):
    path = HERE / (case["id"] + ".json")
    if not path.exists():
        return None
    record = json.loads(path.read_text(encoding="utf-8"))
    preserved = case["id"] in CONT["preserved_case_ids"]
    expected = CONT["original_contract"] if preserved else contract
    require(record["contract"] == expected and record["config"] == case["config"], "Case identity differs: " + case["id"])
    require(record["status"] in ("completed", "failed"), "Unresolved earlier attempt: " + case["id"])
    if preserved:
        require(sha(path) == CONT["preserved_files"][path.name], "Preserved case JSON changed")
    if record.get("artifact"):
        digest = sha(HERE / record["artifact"])
        require(digest == record["artifact_sha256"], "Artifact hash differs: " + case["id"])
        if preserved:
            require(digest == CONT["preserved_files"][record["artifact"]], "Preserved NPZ changed")
    return record


def check_pair(case, record, contract):
    other_case = next(row for row in SPEC["cases"] if row["seed"] == case["seed"] and row["arm"] != case["arm"])
    other = load_record(other_case, contract)
    if other is None or not record.get("initialization_sha256") or not other.get("initialization_sha256"):
        return {"status": "insufficient"}
    for field in ("initialization_sha256", "decision_schedule_sha256"):
        require(record[field] == other[field], "Paired initial inputs differ: " + field)
    if not record.get("artifact") or not other.get("artifact"):
        return {"status": "insufficient", "initialization_matches": True}
    with np.load(HERE / record["artifact"], allow_pickle=False) as a, np.load(HERE / other["artifact"], allow_pickle=False) as b:
        prefix = min(record["completed_days"], other["completed_days"]) + 1
        require(np.array_equal(a["exogenous_day_digest"][:prefix], b["exogenous_day_digest"][:prefix]), "Paired exogenous prefix differs")
        require(np.array_equal(a["intrinsic_values"][:prefix], b["intrinsic_values"][:prefix]), "Paired value prefix differs")
    return {"status": "PASS", "completed_prefix_days_compared": prefix - 1,
            "full_horizon_compared": prefix == SPEC["budget"]["trading_days"] + 1}


def run_case(case, contract):
    old = load_record(case, contract)
    if old is not None:
        check_pair(case, old, contract)
        return old
    verify_sources(contract)
    resource_check()
    path = HERE / (case["id"] + ".json")
    require(not (HERE / (case["id"] + ".npz")).exists(), "Unresolved artifact without final record")
    record = {"case": case["id"], "arm": case["arm"], "seed": case["seed"], "config": case["config"],
              "contract": contract, "status": "running", "started_utc": datetime.now(UTC).isoformat()}
    write_json(path, record, exclusive=True)
    started = time.perf_counter()
    market = recorder = None
    stop = None
    moments = {name: np.full((case["config"]["n_firms"], len(MOMENT_NAMES)), np.nan) for name in ("price", "holder_total")}
    try:
        initialize = time.perf_counter()
        market = CrossSectionMarket(MarketConfig.from_dict(case["config"]))
        record["market_initialization_seconds"] = time.perf_counter() - initialize
        require(np.all(market.investors.taste == 0) and np.all(market.investors.investor_type == 0), "Expected bare investors")
        recorder = Recorder(market)
        record["initialization_sha256"], record["decision_schedule_sha256"] = recorder.initialization_hash, recorder.schedule_hash
        other_case = next(row for row in SPEC["cases"] if row["seed"] == case["seed"] and row["arm"] != case["arm"])
        other = load_record(other_case, contract)
        if other is not None and other.get("initialization_sha256"):
            require(other["initialization_sha256"] == recorder.initialization_hash and other["decision_schedule_sha256"] == recorder.schedule_hash,
                    "Paired initialization differs before run")
        run_started = time.perf_counter()
        with recorder:
            result = market.run()
        record["market_run_wall_seconds_including_telemetry"] = time.perf_counter() - run_started
        statistics_started = time.perf_counter()
        validation = validate_market(result, market.config)
        initial_share_error = float(np.max(np.abs(recorder.data["share_error"][0])))
        validation["mechanical"]["checks"]["initial_share_conservation"] = bool(np.isfinite(initial_share_error) and initial_share_error <= base.harness.CONSERVATION_TOLERANCE)
        validation["mechanical"]["status"] = "PASS" if all(validation["mechanical"]["checks"].values()) else "FAIL"
        moments["price"] = np.array([[row["moments"][name] for name in MOMENT_NAMES] for row in validation["moments_per_asset"]], dtype=float)
        price_returns = np.expm1(np.diff(np.log(result.prices), axis=0))
        total_returns = price_returns + market.config.cash_flow_yield * result.intrinsic_values[1:] / TRADING_DAYS_PER_YEAR / result.prices[:-1]
        for asset in range(market.config.n_firms):
            if np.all(np.isfinite(total_returns[:, asset])):
                try:
                    moments["holder_total"][asset] = compute_moments(total_returns[market.config.burn_in_days:, asset])
                except ValueError:
                    pass
        require(np.array_equal(recorder.data["cap"].sum(axis=1), result.price_cap_hits), "Daily cap counts differ")
        require(np.all(recorder.data["step_completed"][1:]), "Completed world has incomplete telemetry")
        require(np.allclose(np.abs(recorder.data["share_error"][1:]).max(axis=1), result.maximum_share_error[1:], rtol=0, atol=1e-15), "Per-asset share record differs")
        require(np.allclose(np.diff(np.log(result.prices), axis=0), recorder.data["log_moves"][1:], rtol=0, atol=2e-12), "Price/move paths differ")
        record.update(status="completed", validation=validation, result_fingerprint=result.fingerprint(),
                      intrinsic_value_path_sha256=array_sha(result.intrinsic_values),
                      statistics_wall_seconds=time.perf_counter() - statistics_started)
        for name, values in moments.items():
            record[name + "_moments_by_company"] = values
            record[name + "_mean_moments"] = values.mean(axis=0)
            record[name + "_moment_distributions"] = {key: distribution(values[:, i]) for i, key in enumerate(MOMENT_NAMES)}
        total_checks = {"all_finite_nine_moments": bool(np.isfinite(moments["holder_total"]).all()),
                        "all_positive_excess_kurtosis": bool(np.all(moments["holder_total"][:, 1] > 0)),
                        "all_positive_abs_return_acf1": bool(np.all(moments["holder_total"][:, 3] > 0))}
        record["holder_total_stylized"] = {"status": "PASS" if all(total_checks.values()) else "FAIL", "checks": total_checks}
    except BaseException as error:
        record.update(status="failed", exception_type=type(error).__name__, error=traceback.format_exc(),
                      validation={"mechanical": {"status": "FAIL", "reason": "World or diagnostics incomplete"},
                                  "stylized": {"status": "pending"}, "return_acf": {"status": "pending"},
                                  "cross_asset_correlation": {"status": "pending"}, "empirical_calibration": {"status": "pending"}})
        if isinstance(error, (GlobalStop, KeyboardInterrupt, SystemExit)):
            stop = error
    write_json(path, dict(record, status="archiving", world_status=record["status"]))
    if recorder is not None:
        last = recorder.day
        data = {name: values[:last + 1] for name, values in recorder.data.items()}
        data.update(day=np.arange(last + 1), size_class=market.firms.size_class,
                    detailed_event_index=recorder.event_index[:recorder.event_count], detailed_events=recorder.events[:recorder.event_count],
                    price_moments=moments["price"], holder_total_moments=moments["holder_total"])
        record.update(completed_days=market.next_day_index, observed_state_through_day=last,
                      failure_partial_day=last if last > market.next_day_index else None,
                      simulation_completed=market.next_day_index == market.config.trading_days,
                      cap_events_total=int(recorder.total_events), detailed_events_saved=int(recorder.event_count),
                      detailed_events_omitted=int(recorder.total_events - recorder.event_count),
                      cap_hits_full_observed=int(data["cap"].sum()),
                      cap_hits_burn_in_observed=int(data["cap"][:market.config.burn_in_days + 1].sum()),
                      cap_hits_measurement_observed=int(data["cap"][market.config.burn_in_days + 1:].sum()),
                      market_step_wall_seconds_including_inner_telemetry=recorder.step_seconds,
                      inner_telemetry_wall_seconds=recorder.inner_recording_seconds,
                      market_step_compute_seconds_estimate=max(0.0, recorder.step_seconds - recorder.inner_recording_seconds),
                      state_recording_wall_seconds=recorder.state_recording_seconds,
                      maximum_absolute_share_error_every_asset=float(np.max(np.abs(data["share_error"]))),
                      depth_distribution=distribution(data["depth_fraction"][1:]),
                      feedback_volatility_ratio_distribution=distribution(data["feedback_volatility_ratio"][1:]),
                      maximum_absolute_raw_quote=distribution(np.abs(data["raw"]))["maximum"],
                      maximum_absolute_log_mispricing=distribution(np.abs(np.log(data["prices"] / data["intrinsic_values"])))["maximum"])
        denominator = np.where(data["expected_total_cash"] != 0, np.abs(data["expected_total_cash"]), 1.0)
        record["maximum_relative_cash_error_every_observed_day"] = float(np.max(np.abs(data["total_cash"] - data["expected_total_cash"]) / denominator))
        resource_check()
        archive_started = time.perf_counter()
        artifact = HERE / (case["id"] + ".npz")
        temporary = artifact.with_suffix(".npz.tmp")
        with temporary.open("xb") as stream:
            np.savez_compressed(stream, **data)
        require(temporary.stat().st_size <= SPEC["storage"]["maximum_world_artifact_bytes"], "World exceeds frozen artifact bound")
        temporary.replace(artifact)
        record.update(artifact=artifact.name, artifact_sha256=sha(artifact), archive_write_wall_seconds=time.perf_counter() - archive_started)
    else:
        record.update(completed_days=0, observed_state_through_day=None, artifact=None, simulation_completed=False)
    record["total_wall_seconds"] = time.perf_counter() - started
    record["moment_window"] = {"start_day": 1200, "end_day": 3500, "return_observations": 2300,
                               "full_horizon_available": record["status"] == "completed"}
    record["finished_utc"] = datetime.now(UTC).isoformat()
    write_json(path, record)
    verify_sources(contract)
    resource_check()
    pairing = check_pair(case, record, contract)
    print(json.dumps({"case": case["id"], "status": record["status"], "caps": record.get("cap_hits_full_observed"),
                      "mechanical": record["validation"]["mechanical"]["status"], "pairing": pairing["status"]}), flush=True)
    if stop is not None:
        raise stop
    return record


def summarize(contract):
    records = [load_record(case, contract) or {"case": case["id"], "seed": case["seed"], "arm": case["arm"], "status": "not_started"}
               for case in SPEC["cases"]]
    arms = {}
    for arm in SPEC["arms"]:
        rows = [row for row in records if row["arm"] == arm["id"]]
        completed = [row for row in rows if row["status"] == "completed"]
        arms[arm["id"]] = {
            "scheduled_worlds": 30, "completed_diagnostics": len(completed),
            "interrupted_diagnostics": sum(row["status"] == "failed" for row in rows),
            "full_market_paths": sum(bool(row.get("simulation_completed")) for row in rows),
            "mechanical_pass_worlds": sum(row["validation"]["mechanical"]["status"] == "PASS" for row in completed),
            "mechanical_fail_worlds": sum(row["validation"]["mechanical"]["status"] == "FAIL" for row in completed),
            "mechanical_unassessed_worlds": 30 - len(completed),
            "all_worlds_mechanical_pass": len(completed) == 30 and all(row["validation"]["mechanical"]["status"] == "PASS" for row in completed),
            "observed_caps_including_interrupted_diagnostics": sum(row.get("cap_hits_full_observed", 0) for row in rows),
        }
    pairs = {}
    for seed in SPEC["budget"]["seeds"]:
        case = next(row for row in SPEC["cases"] if row["seed"] == seed and row["arm"] == "m30")
        record = next(row for row in records if row["case"] == case["id"])
        pairs[seed] = check_pair(case, record, contract)
    summary = {"contract": contract, "status": "complete" if all(row["status"] in ("completed", "failed") for row in records) else "incomplete",
               "scheduled_worlds": 60, "preserved_worlds": 13, "continuation_world_budget": 47,
               "completed_diagnostics": sum(row["status"] == "completed" for row in records),
               "interrupted_diagnostics": sum(row["status"] == "failed" for row in records),
               "full_market_paths": sum(bool(row.get("simulation_completed")) for row in records),
               "arms": arms, "pairing": pairs,
               "records": [{key: row.get(key) for key in ("case", "arm", "seed", "status", "contract", "completed_days", "simulation_completed", "artifact", "artifact_sha256", "cap_hits_full_observed")}
                           for row in records],
               "original_diagnostic_interruption": CONT["diagnostic_interruption"],
               "return_acf": "pending", "cross_asset_correlation": "pending", "empirical_calibration": "pending", "automatic_winner": None,
               "independent_physical_and_nine_moment_audit": "pending; the original interrupted record remains unchanged"}
    write_json(HERE / "continuation_summary.json", summary)
    lines = ["# 固定市场资格检查：透明续跑", "",
             f"预定60世界，原13档保留，续跑仅余47档。现有完整市场路径{summary['full_market_paths']}，完成诊断{summary['completed_diagnostics']}，诊断中断{summary['interrupted_diagnostics']}。", "",
             "原m30_710107已完整运行3500日；日0股份误差1.3322676295501878e-15与参考初始化0比较触发记录器停止。原JSON、NPZ和中断状态保留；本次不重跑。独立物理门槛和九矩复核另报，原CrossSectionResult fingerprint无法从最小归档复原。", "",
             "|模型|完整市场路径|诊断完成|诊断中断|机械PASS|机械FAIL|机械未评|所有已观察cap|", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for arm, row in arms.items():
        lines.append(f"|{arm}|{row['full_market_paths']}|{row['completed_diagnostics']}|{row['interrupted_diagnostics']}|{row['mechanical_pass_worlds']}|{row['mechanical_fail_worlds']}|{row['mechanical_unassessed_worlds']}|{row['observed_caps_including_interrupted_diagnostics']}|")
    lines += ["", "新结果绑定续跑spec/入口hash；旧结果保持原contract。模型、配置、种子、门槛、归档口径和总60世界预算保持；没有补种子、重跑或选赢家。", "",
              "续跑只将记录器参考对照限定为实际核验过的日1..3500，并按原1e-8机械公差独立检查日0实际股份误差。收益ACF、相关性、实证校准及独立归档审计仍pending。", ""]
    (HERE / "continuation_report.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(HERE / "continuation_summary_manifest.json", {
        "contract": contract, "summary_sha256": sha(HERE / "continuation_summary.json"),
        "report_sha256": sha(HERE / "continuation_report.md"),
        "case_json_sha256": {row["case"]: sha(HERE / (row["case"] + ".json")) for row in records if row["status"] != "not_started"},
    })
    return summary


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check-only", action="store_true")
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--summarize-only", action="store_true")
    args = parser.parse_args()
    require(sha(Path(__file__)) == CONT["launcher_sha256"], "Continuation launcher identity differs")
    require(platform.python_version() == SPEC["runtime"]["python_version"] and np.__version__ == SPEC["runtime"]["numpy_version"], "Runtime differs")
    require(not (HERE / "writer.lock").exists(), "Original writer still active or unresolved")
    require(CONT["preserved_case_ids"] == [case["id"] for case in SPEC["cases"][:13]], "Unexpected preserved set")
    remaining = SPEC["cases"][13:]
    require(len(SPEC["cases"]) == 60 and len(remaining) == 47, "Unexpected total budget")
    require(CONT["remaining_case_ids"] == [case["id"] for case in remaining], "Unexpected continuation set")
    contract = dict(CONT["original_contract"], spec_sha256=sha(CONT_PATH), launcher_sha256=sha(Path(__file__)),
                    original_spec_sha256=CONT["frozen_artifacts"]["freeze.json"],
                    original_launcher_sha256=CONT["frozen_artifacts"]["run_frozen.py"],
                    continuation_version=1)
    verify_sources(contract)
    verify_preserved()
    storage = resource_check()
    launch = HERE / "continuation_launch_manifest.json"
    if launch.exists():
        require(json.loads(launch.read_text(encoding="utf-8"))["contract"] == contract, "Earlier continuation identity differs")
    for case in SPEC["cases"][:13]:
        require(load_record(case, contract) is not None, "Preserved case missing")
    for case in remaining:
        if load_record(case, contract) is None:
            require(not (HERE / (case["id"] + ".npz")).exists(), "Unresolved continuation artifact")
    if not args.run and not args.summarize_only:
        write_json(HERE / "continuation_preflight.json", {
            "status": "ready_for_review", "contract": contract, "preserved_worlds": 13, "remaining_worlds": 47,
            "total_world_budget": 60, "market_initializations": 0, "market_runs": 0, "storage": storage,
        })
        print("Continuation preflight ready for review: thirteen preserved worlds; only forty-seven remaining; zero initializations")
        return
    lock = HERE / "continuation_writer.lock"
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.write(descriptor, str(os.getpid()).encode())
        if not launch.exists():
            write_json(launch, {"contract": contract, "started_utc": datetime.now(UTC).isoformat(),
                                "thread_environment": {name: os.environ[name] for name in base.THREAD_VARIABLES}}, exclusive=True)
        if args.run:
            base.disable_power_throttling()
            for case in remaining:
                run_case(case, contract)
        summary = summarize(contract)
        verify_sources(contract)
        verify_preserved()
        resource_check()
        print(json.dumps({"status": summary["status"], "full_market_paths": summary["full_market_paths"],
                          "interrupted_diagnostics": summary["interrupted_diagnostics"], "automatic_extra_worlds": 0}))
    except BaseException as error:
        write_json(HERE / "continuation_global_stop.json", {"contract": contract, "stopped_utc": datetime.now(UTC).isoformat(),
                                                           "exception_type": type(error).__name__, "error": traceback.format_exc(), "automatic_extra_worlds": 0})
        raise
    finally:
        os.close(descriptor)
        lock.unlink()


if __name__ == "__main__":
    main()
