"""Independently audit frozen archives with NumPy and the standard library."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import traceback
import zipfile

for variable in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = "1"

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EXPECTED_FILES = {
    "freeze.json": "40e7e7711a1739b1a812c958d79e094bc7fac553642d55da1a7ea07345e4cf74",
    "run_frozen.py": "37562ed7f426991143e47723f2d99eb2a139add379deb20be1a7ac3cdefdb36e",
    "initial_manifest.json": "8d99c849c0d187234e804fe52bef2b9b66c6fc90f5abab0c467dcd3fefe23e68",
    "seed_lineage.json": "2cbf27f928a8db95c6fb19e35f1043d3c16f8cf109157a2e2089f3ccae2611d6",
    "continuation.json": "d0f1f5cd23367ea5c8568b0892ee4aeb17740bedfb8116d84572d81110b9b42b",
    "continue_frozen.py": "465b50923ad08d65bb00ec8f49a543b8bfd4bdb4a15ad5f4641e72c44d7c8616",
    "continuation_run_case.diff": "81334288bb6bc01be5c85672fff132db1b34729581cae98e305f8612915bb0aa",
}
MOMENT_NAMES = (
    "daily_volatility", "excess_kurtosis", "return_acf_1", "abs_return_acf_1",
    "abs_return_acf_5", "abs_return_acf_20", "quantile_01", "quantile_99", "hill_tail_index",
)
PATH_NAMES = (
    "prices", "intrinsic_values", "raw", "log_moves", "share_error",
    "depth_fraction", "feedback_volatility_ratio",
)
FLAG_NAMES = ("state_recorded", "quote_recorded", "settlement_recorded", "step_completed")
CASH_NAMES = ("total_cash", "expected_total_cash", "minimum_investor_cash", "minimum_investor_holding")
CONSERVATION_TOLERANCE = 1e-8
MAXIMUM_LOG_MISPRICING = 5.0
QUOTE_ATOL = 2e-12
ARITHMETIC_ATOL = 2e-12
ARITHMETIC_RTOL = 2e-11
MOMENT_ATOL = 2e-10
MOMENT_RTOL = 2e-10
SPECIAL_CASE = "m30_710107"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def array_sha(array):
    array = np.ascontiguousarray(array)
    return hashlib.sha256(str(array.dtype).encode() + str(array.shape).encode() + array.tobytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def clean(value):
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.bool_):
        return bool(value)
    return value


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def distribution(values):
    values = np.asarray(values, dtype=float)
    finite = values[np.isfinite(values)]
    return {
        "count": int(values.size), "finite_count": int(finite.size),
        "minimum": float(finite.min()) if finite.size else None,
        "quantile_05": float(np.quantile(finite, .05)) if finite.size else None,
        "median": float(np.median(finite)) if finite.size else None,
        "quantile_95": float(np.quantile(finite, .95)) if finite.size else None,
        "maximum": float(finite.max()) if finite.size else None,
        "mean": float(finite.mean()) if finite.size else None,
    }


class Checks:
    def __init__(self):
        self.items = {}

    def add(self, name, passed, **evidence):
        self.items[name] = dict(status="PASS" if bool(passed) else "FAIL", **evidence)

    def close(self, name, actual, expected, *, atol=ARITHMETIC_ATOL, rtol=ARITHMETIC_RTOL):
        if actual is None and np.asarray(expected).shape == ():
            self.add(name, not np.isfinite(expected), json_null_for_nonfinite=True)
            return
        actual, expected = np.asarray(actual, dtype=float), np.asarray(expected, dtype=float)
        if actual.shape != expected.shape:
            self.add(name, False, actual_shape=actual.shape, expected_shape=expected.shape)
            return
        with np.errstate(all="ignore"):
            matches = np.isclose(actual, expected, atol=atol, rtol=rtol, equal_nan=True)
            difference = np.abs(actual - expected)
        finite = difference[np.isfinite(difference)]
        bad = np.argwhere(~matches)
        self.add(name, np.all(matches), atol=atol, rtol=rtol,
                 mismatches=int(bad.shape[0]), first_mismatches=bad[:10],
                 maximum_finite_absolute_difference=float(finite.max()) if finite.size else None)

    def result(self):
        return {"status": "PASS" if all(row["status"] == "PASS" for row in self.items.values()) else "FAIL",
                "checks": self.items}


def autocorrelation(values, lag):
    first, second = values[:-lag], values[lag:]
    valid = np.isfinite(first) & np.isfinite(second)
    first, second = first[valid], second[valid]
    if first.size < 2:
        raise ValueError("Not enough finite lagged pairs")
    first, second = first - first.mean(), second - second.mean()
    denominator = np.sqrt(np.dot(first, first) * np.dot(second, second))
    return 0.0 if denominator == 0 else float(np.clip(np.dot(first, second) / denominator, -1, 1))


def nine_moments(values):
    finite = values[np.isfinite(values)]
    if finite.size < 250:
        raise ValueError("Not enough finite observations")
    magnitudes = np.sort(np.abs(finite - finite.mean()))[::-1]
    tail_size = int(.025 * finite.size)
    if tail_size < 10 or magnitudes[tail_size] <= 0:
        raise ValueError("Hill tail threshold unavailable")
    with np.errstate(all="ignore"):
        hill = np.divide(1.0, np.mean(np.log(magnitudes[:tail_size] / magnitudes[tail_size])))
        standardized = (finite - finite.mean()) / np.std(finite, ddof=0)
        return np.array((
            np.std(finite, ddof=1), np.mean(standardized**4) - 3,
            autocorrelation(values, 1), autocorrelation(np.abs(values), 1),
            autocorrelation(np.abs(values), 5), autocorrelation(np.abs(values), 20),
            np.quantile(finite, .01), np.quantile(finite, .99), hill,
        ), dtype=np.float64)


def moment_matrix(returns, burn, *, check_full_period=False):
    matrix = np.full((returns.shape[1], len(MOMENT_NAMES)), np.nan)
    for asset in range(returns.shape[1]):
        sample = returns[burn:, asset]
        valid = returns[:, asset] if check_full_period else sample
        if np.all(np.isfinite(valid)):
            try:
                matrix[asset] = nine_moments(sample)
            except ValueError:
                pass
    return matrix


def stylized(matrix):
    finite = np.all(np.isfinite(matrix), axis=1)
    tails = np.isfinite(matrix[:, 1]) & (matrix[:, 1] > 0)
    clustering = np.isfinite(matrix[:, 3]) & (matrix[:, 3] > 0)
    return {
        "status": "PASS" if np.all(finite & tails & clustering) else "FAIL",
        "checks": {"all_assets_have_finite_moments": bool(finite.all()),
                   "all_assets_positive_excess_kurtosis": bool(tails.all()),
                   "all_assets_positive_abs_return_acf_1": bool(clustering.all())},
        "failed_assets": {"nonfinite_moments": np.flatnonzero(~finite),
                          "nonpositive_excess_kurtosis": np.flatnonzero(~tails),
                          "nonpositive_abs_return_acf_1": np.flatnonzero(~clustering)},
    }


def lineage():
    checks = Checks()
    hashes = {}
    for name, digest in EXPECTED_FILES.items():
        actual = sha(HERE / name)
        hashes[name] = actual
        checks.add("frozen:" + name, actual == digest)
    spec, continuation = read_json(HERE / "freeze.json"), read_json(HERE / "continuation.json")
    original = continuation["original_contract"]
    new = dict(original, spec_sha256=hashes["continuation.json"], launcher_sha256=hashes["continue_frozen.py"],
               original_spec_sha256=hashes["freeze.json"], original_launcher_sha256=hashes["run_frozen.py"],
               continuation_version=1)
    checks.add("no_abm_import", not any(name == "abm" or name.startswith("abm.") for name in sys.modules))
    checks.add("no_writer_lock", not any((HERE / name).exists() for name in ("writer.lock", "continuation_writer.lock")))
    checks.add("runtime", platform.python_version() == spec["runtime"]["python_version"] and np.__version__ == spec["runtime"]["numpy_version"])
    checks.add("fixed_case_count", len(spec["cases"]) == 60 and len({row["id"] for row in spec["cases"]}) == 60)
    checks.add("fixed_seed_list", spec["budget"]["seeds"] == list(range(710101, 710131)))
    checks.add("fixed_arms", spec["arms"][0]["id"] == "m30" and spec["arms"][0]["order_flow_memory"] == .3
               and spec["arms"][1]["id"] == "m70" and spec["arms"][1]["order_flow_memory"] == .7)
    checks.add("preserved_and_remaining_partition",
               continuation["preserved_case_ids"] == [row["id"] for row in spec["cases"][:13]]
               and continuation["remaining_case_ids"] == [row["id"] for row in spec["cases"][13:]]
               and continuation["remaining_market_world_budget"] == 47 and continuation["logical_world_budget"] == 60)
    checks.add("original_contract", original == read_json(HERE / "launch_manifest.json")["contract"]
               and original["spec_sha256"] == hashes["freeze.json"] and original["launcher_sha256"] == hashes["run_frozen.py"]
               and original["initial_manifest_sha256"] == hashes["initial_manifest.json"]
               and original["seed_lineage_sha256"] == hashes["seed_lineage.json"])
    checks.add("new_contract", new == read_json(HERE / "continuation_launch_manifest.json")["contract"])
    initial = read_json(HERE / "initial_manifest.json")
    checks.add("initial_manifest", initial["spec_sha256"] == hashes["freeze.json"]
               and initial["launcher_sha256"] == hashes["run_frozen.py"]
               and initial["seed_lineage_sha256"] == hashes["seed_lineage.json"]
               and initial["market_initializations"] == 0 and initial["market_runs"] == 0)
    for name, digest in continuation["preserved_files"].items():
        hashes[name] = sha(HERE / name)
        checks.add("preserved:" + name, hashes[name] == digest)
    for name in ("preflight.json", "continuation_preflight.json"):
        receipt = read_json(HERE / name)
        hashes[name] = sha(HERE / name)
        checks.add("zero_initialization:" + name, receipt["market_initializations"] == 0 and receipt["market_runs"] == 0)
    source = ROOT / spec["source"]["archive"]
    hashes[spec["source"]["archive"]] = sha(source)
    checks.add("source_zip", hashes[spec["source"]["archive"]] == spec["source"]["archive_sha256"]
               == original["source_zip_sha256"] == "0763385ed37592e88ef18c41f6ddb3bb76d8ee7df6430071b80429c6beac2ed7")
    with zipfile.ZipFile(source) as bundle:
        source_hashes = spec["source"]["source_hashes"]
        checks.add("source_members", len(bundle.namelist()) == len(source_hashes) and set(bundle.namelist()) == set(source_hashes))
        for name, digest in source_hashes.items():
            checks.add("zip_member:" + name, hashlib.sha256(bundle.read(name)).hexdigest() == digest)
            relative = "isolated_src/" + name
            hashes[relative] = sha(HERE / relative)
            checks.add("isolated_member:" + name, hashes[relative] == digest)
    for case in spec["cases"]:
        expected_config = dict(spec["base_config"], seed=case["seed"], order_flow_memory=.3 if case["arm"] == "m30" else .7)
        checks.add("config:" + case["id"], case["config"] == expected_config
                   and case["id"] == case["arm"] + "_" + str(case["seed"])
                   and case["seed"] in spec["budget"]["seeds"])
    manifest = read_json(HERE / "continuation_summary_manifest.json")
    summary = read_json(HERE / "continuation_summary.json")
    checks.add("summary_identity", manifest["contract"] == new == summary["contract"])
    checks.add("summary_case_set", set(manifest["case_json_sha256"]) == {row["id"] for row in spec["cases"]})
    for name, key in (("continuation_summary.json", "summary_sha256"), ("continuation_report.md", "report_sha256")):
        hashes[name] = sha(HERE / name)
        checks.add("summary_hash:" + name, hashes[name] == manifest[key])
    for name in ("launch_manifest.json", "continuation_launch_manifest.json", "continuation_summary_manifest.json", "global_stop.json"):
        hashes[name] = sha(HERE / name)
    checks.add("no_unplanned_case_records", {path.stem for path in HERE.glob("m[37]0_*.json")} == {row["id"] for row in spec["cases"]})
    checks.add("no_unplanned_case_archives", {path.stem for path in HERE.glob("m[37]0_*.npz")} <= {row["id"] for row in spec["cases"]})
    return spec, continuation, original, new, checks, hashes, manifest, summary


def check_events(data, config, spec, checks, variance_at_event, reference_at_event, depth_before_event):
    index, events = data["detailed_event_index"], data["detailed_events"]
    fields = spec["storage"]["event_float_fields"]
    cap_index = np.argwhere(data["cap"])
    limit = spec["storage"]["maximum_detailed_events_per_world"]
    expected_saved = min(len(cap_index), limit)
    checks.add("detailed_event_shape_dtype", index.shape == (expected_saved, 4) and index.dtype == np.dtype("int64")
               and events.shape == (expected_saved, len(fields)) and events.dtype == np.dtype("float64"))
    if index.shape != (expected_saved, 4) or events.shape != (expected_saved, len(fields)):
        return {"total_events": len(cap_index), "saved_events": len(index), "omitted_events": len(cap_index) - len(index)}
    checks.add("detailed_event_selection", np.array_equal(index[:, :2], cap_index[:limit]))
    if not expected_saved:
        return {"total_events": len(cap_index), "saved_events": 0, "omitted_events": len(cap_index)}
    days, assets = index[:, 0], index[:, 1]
    raw = data["raw"][days, assets]
    directions = np.zeros(raw.shape, dtype=np.int64)
    finite = np.isfinite(raw)
    directions[finite] = np.sign(raw[finite]).astype(np.int64)
    checks.add("event_size_and_direction", np.array_equal(index[:, 2], data["size_class"][assets])
               and np.array_equal(index[:, 3], directions))
    value = {name: events[:, i] for i, name in enumerate(fields)}
    old_price = data["prices"][days - 1, assets]
    current_value = data["intrinsic_values"][days, assets]
    with np.errstate(all="ignore"):
        news = config["news_pass_through"] * np.log(current_value / data["intrinsic_values"][days - 1, assets])
        flow = config["price_impact"] * (value["investor_submitted"] + value["noise_submitted"]) * old_price / (config["liquidity_fraction"] * old_price)
        expected_flow = config["order_flow_memory"] * value["expected_flow_before"] + (1 - config["order_flow_memory"]) * flow / value["depth_after"]
        transient = config["transient_impact_decay"] * value["transient_before"] + (1 - config["permanent_impact_fraction"]) * (flow / value["depth_after"] - value["expected_flow_before"])
        inventory = config["market_maker_inventory_skew"] * (1 - config["investor_float_share"] - config["noise_float_share"] - value["maker_inventory_before"])
    for name, expected in (
        ("raw_quote", raw), ("log_move", data["log_moves"][days, assets]),
        ("old_price", old_price), ("current_intrinsic_value", current_value),
        ("news_quote", news), ("permanent_quote", config["permanent_impact_fraction"] * flow),
        ("transient_after", transient), ("transient_change", value["transient_after"] - value["transient_before"]),
        ("expected_flow_after", expected_flow), ("inventory_quote", inventory),
        ("depth_after", data["depth_fraction"][days, assets]),
        ("feedback_volatility_ratio", data["feedback_volatility_ratio"][days, assets]),
        ("variance_prequote", variance_at_event), ("reference_variance_prequote", reference_at_event),
        ("depth_before", depth_before_event),
        ("noise_amplification", np.minimum(value["feedback_volatility_ratio"], 4.0) ** config["noise_volatility_exponent"]),
    ):
        checks.close("event:" + name, value[name], expected)
    checks.close("event:component_sum", value["raw_quote"],
                 value["news_quote"] + value["permanent_quote"] + value["transient_change"] + value["inventory_quote"],
                 atol=QUOTE_ATOL, rtol=0)
    settled = data["settlement_recorded"][days]
    checks.add("event_execution_stage", np.all(np.isnan(events[~settled, 17:19])))
    differences = events[settled, 17:19] - events[settled, 15:17]
    return {"total_events": len(cap_index), "saved_events": expected_saved, "omitted_events": len(cap_index) - expected_saved,
            "submitted_executed_differences": distribution(differences),
            "submitted_executed_unequal_elements": int(np.count_nonzero(differences)),
            "settled_execution_snapshots_all_finite": bool(np.isfinite(events[settled, 17:19]).all()),
            "limitation": "Stored event snapshots permit arithmetic decomposition, not a path counterfactual or reconstruction of unarchived holdings/orders."}


def feedback_checks(data, config, checks):
    n, assets = data["prices"].shape
    fast = np.full(assets, config["initial_asset_volatility"]**2 / 252)
    reference, depth = fast.copy(), np.ones(assets)
    expected_ratio = np.full((n, assets), np.nan)
    expected_depth = np.full((n, assets), np.nan)
    expected_ratio[0], expected_depth[0] = 1.0, 1.0
    index = data["detailed_event_index"]
    variance_event, reference_event, depth_before_event = (np.full(index.shape[0], np.nan) for _ in range(3))
    for day in range(1, n):
        if not data["quote_recorded"][day]:
            continue
        with np.errstate(all="ignore"):
            ratio = np.sqrt(fast / reference)
            stress = np.clip(ratio - config["liquidity_stress_threshold"], 0, 1)
            target = np.maximum(config["minimum_liquidity_fraction"], np.exp(-config["liquidity_volatility_sensitivity"] * stress))
            event_rows = np.flatnonzero(index[:, 0] == day)
            event_assets = index[event_rows, 1]
            variance_event[event_rows], reference_event[event_rows] = fast[event_assets], reference[event_assets]
            depth_before_event[event_rows] = depth[event_assets]
            depth += config["depth_resilience"] * (target - depth)
            np.maximum(depth, config["minimum_liquidity_fraction"], out=depth)
            expected_ratio[day], expected_depth[day] = ratio, depth
            if data["step_completed"][day]:
                squared = data["log_moves"][day]**2
                fast = config["variance_ewma_decay"] * fast + (1 - config["variance_ewma_decay"]) * squared
                reference = config["reference_variance_decay"] * reference + (1 - config["reference_variance_decay"]) * squared
    mask = data["quote_recorded"].copy()
    mask[0] = True
    checks.close("ewma_feedback_ratio", data["feedback_volatility_ratio"][mask], expected_ratio[mask])
    checks.close("recursive_depth", data["depth_fraction"][mask], expected_depth[mask])
    return variance_event, reference_event, depth_before_event


def audit_case(case, contract, continuation, spec, summary_manifest):
    checks = Checks()
    path = HERE / (case["id"] + ".json")
    record = read_json(path)
    input_hashes = {path.name: sha(path)}
    checks.add("terminal_identity", record["case"] == case["id"] and record["config"] == case["config"]
               and record["contract"] == contract and record["status"] in ("completed", "failed"))
    checks.add("summary_case_hash", summary_manifest["case_json_sha256"].get(case["id"]) == input_hashes[path.name])
    output = {"case": case["id"], "arm": case["arm"], "seed": case["seed"],
              "original_status": record["status"], "provenance": "original" if case["id"] in continuation["preserved_case_ids"] else "continuation",
              "contract": record["contract"], "input_hashes": input_hashes,
              "result_fingerprint_reconstruction": "unavailable: equity_share and gross_volume are not archived",
              "recorded_result_fingerprint": record.get("result_fingerprint"),
              "stored_initialization_sha256": record.get("initialization_sha256"),
              "stored_decision_schedule_sha256": record.get("decision_schedule_sha256")}
    if not record.get("artifact"):
        checks.add("no_artifact_only_for_failed_initialization", record["status"] == "failed" and record["completed_days"] == 0)
        output.update(artifact_audit=checks.result(), full_physical_path=False,
                      mechanical={"status": "insufficient"}, price_stylized={"status": "pending"}, holder_total_stylized={"status": "pending"})
        return output, record
    checks.add("artifact_name", record["artifact"] == case["id"] + ".npz")
    artifact = HERE / (case["id"] + ".npz")
    input_hashes[artifact.name] = sha(artifact)
    checks.add("artifact_hash", input_hashes[artifact.name] == record["artifact_sha256"])
    with np.load(artifact, allow_pickle=False) as bundle:
        expected_keys = set(PATH_NAMES + FLAG_NAMES + CASH_NAMES + ("cap", "exogenous_day_digest", "day", "size_class",
                         "detailed_event_index", "detailed_events", "price_moments", "holder_total_moments"))
        checks.add("archive_members", set(bundle.files) == expected_keys)
        data = {name: bundle[name] for name in expected_keys}
    config = case["config"]
    n, assets = data["prices"].shape
    last, completed = n - 1, record["completed_days"]
    horizon, burn = config["trading_days"], config["burn_in_days"]
    valid_shapes = 1 <= n <= horizon + 1 and assets == config["n_firms"]
    for name in PATH_NAMES:
        valid_shapes &= data[name].shape == (n, assets) and data[name].dtype == np.dtype("float64")
    for name in FLAG_NAMES + CASH_NAMES + ("exogenous_day_digest", "day"):
        valid_shapes &= data[name].shape == (n,)
    valid_shapes &= data["cap"].shape == (n, assets) and data["cap"].dtype == np.dtype("bool")
    valid_shapes &= data["size_class"].shape == (assets,) and data["size_class"].dtype == np.dtype("int64")
    for name in FLAG_NAMES:
        valid_shapes &= data[name].dtype == np.dtype("bool")
    for name in CASH_NAMES:
        valid_shapes &= data[name].dtype == np.dtype("float64")
    valid_shapes &= data["exogenous_day_digest"].dtype == np.dtype("S32") and data["day"].dtype == np.dtype("int64")
    for name in ("price_moments", "holder_total_moments"):
        valid_shapes &= data[name].shape == (assets, len(MOMENT_NAMES)) and data[name].dtype == np.dtype("float64")
    checks.add("shapes_and_dtypes", valid_shapes)
    if not valid_shapes:
        raise ValueError("Archive shapes/dtypes do not match the frozen schema")
    checks.add("day_and_prefix", np.array_equal(data["day"], np.arange(n)) and last == record["observed_state_through_day"]
               and 0 <= completed <= horizon and completed <= last <= min(horizon, completed + 1)
               and record["simulation_completed"] == (completed == horizon))
    checks.add("size_classes", np.all(np.isin(data["size_class"], (0, 1, 2))))
    checks.add("all_observed_states_recorded", np.all(data["state_recorded"]))
    checks.add("step_prefix", not data["step_completed"][0] and np.all(data["step_completed"][1:completed + 1])
               and not np.any(data["step_completed"][completed + 1:]))
    checks.add("flags_order", not any(data[name][0] for name in ("quote_recorded", "settlement_recorded", "step_completed"))
               and np.all(~data["step_completed"] | (data["quote_recorded"] & data["settlement_recorded"] & data["state_recorded"]))
               and np.all(~data["settlement_recorded"] | data["quote_recorded"]))
    checks.add("day_zero_quote_sentinels", np.all(np.isnan(data["raw"][0])) and np.all(np.isnan(data["log_moves"][0])) and not data["cap"][0].any())
    checks.add("bare_initial_price_equals_value", np.array_equal(data["prices"][0], data["intrinsic_values"][0]))
    quote_days = np.flatnonzero(data["quote_recorded"])
    unquoted = ~data["quote_recorded"]
    checks.add("unquoted_sentinels", np.all(np.isnan(data["raw"][unquoted])) and np.all(np.isnan(data["log_moves"][unquoted]))
               and not np.any(data["cap"][unquoted]))
    clipped = np.clip(data["raw"][quote_days], -config["max_log_return"], config["max_log_return"])
    checks.close("raw_to_clip", data["log_moves"][quote_days], clipped, atol=0, rtol=0)
    checks.add("full_asset_day_cap_mask", np.array_equal(data["cap"][quote_days], clipped != data["raw"][quote_days]))
    with np.errstate(all="ignore"):
        expected_price = data["prices"][quote_days - 1] * np.exp(data["log_moves"][quote_days])
        actual_moves = np.log(data["prices"][quote_days]) - np.log(data["prices"][quote_days - 1])
    checks.close("clip_to_actual_price", data["prices"][quote_days], expected_price, atol=0, rtol=0)
    finite_moves = np.isfinite(actual_moves) & np.isfinite(data["log_moves"][quote_days])
    checks.close("actual_log_price_moves", actual_moves[finite_moves], data["log_moves"][quote_days][finite_moves], atol=QUOTE_ATOL, rtol=0)
    variance_event, reference_event, depth_before_event = feedback_checks(data, config, checks)
    events = check_events(data, config, spec, checks, variance_event, reference_event, depth_before_event)
    cap_daily = data["cap"].sum(axis=1)
    checks.add("cap_counts", record["cap_events_total"] == record["cap_hits_full_observed"] == int(cap_daily.sum())
               and record["detailed_events_saved"] == events["saved_events"] and record["detailed_events_omitted"] == events["omitted_events"]
               and record["cap_hits_burn_in_observed"] == int(data["cap"][:burn + 1].sum())
               and record["cap_hits_measurement_observed"] == int(data["cap"][burn + 1:].sum()))
    with np.errstate(all="ignore"):
        dividends = (config["cash_flow_yield"] * data["intrinsic_values"][1:] / 252).sum(axis=1)
        reconstructed_cash = data["total_cash"][0] + np.r_[0.0, np.cumsum(dividends)]
    paid_days = np.arange(min(completed, last) + 1)
    checks.close("recorded_expected_cash_from_values_completed_days", data["expected_total_cash"][paid_days], reconstructed_cash[paid_days])
    denominator = np.where(reconstructed_cash[paid_days] != 0, np.abs(reconstructed_cash[paid_days]), 1)
    with np.errstate(all="ignore"):
        cash_error = np.abs(data["total_cash"][paid_days] - reconstructed_cash[paid_days]) / denominator
        share_error = np.abs(data["share_error"])
        mispricing = np.abs(np.log(data["prices"] / data["intrinsic_values"]))
    maximum_cash_error, maximum_share_error = float(np.max(cash_error)), float(np.max(share_error))
    checks.close("stored_maximum_share_error", record["maximum_absolute_share_error_every_asset"], maximum_share_error, atol=1e-20, rtol=1e-12)
    recorded_denominator = np.where(data["expected_total_cash"] != 0, np.abs(data["expected_total_cash"]), 1)
    recorded_cash_error = np.max(np.abs(data["total_cash"] - data["expected_total_cash"]) / recorded_denominator)
    checks.close("stored_recorded_cash_error", record["maximum_relative_cash_error_every_observed_day"], recorded_cash_error, atol=1e-20, rtol=1e-12)
    full = n == horizon + 1 and completed == horizon and np.all(data["state_recorded"]) and np.all(data["step_completed"][1:])
    physical_checks = {
        "finite_positive_prices": bool(np.all(np.isfinite(data["prices"]) & (data["prices"] > 0))),
        "finite_positive_intrinsic_values": bool(np.all(np.isfinite(data["intrinsic_values"]) & (data["intrinsic_values"] > 0))),
        "no_price_caps": bool(not np.any(data["cap"])),
        "cash_conservation": bool(np.isfinite(maximum_cash_error) and maximum_cash_error <= CONSERVATION_TOLERANCE),
        "share_conservation": bool(np.isfinite(maximum_share_error) and maximum_share_error <= CONSERVATION_TOLERANCE),
        "initial_share_conservation": bool(np.isfinite(share_error[0]).all() and np.max(share_error[0]) <= CONSERVATION_TOLERANCE),
        "no_divergence": bool(np.isfinite(mispricing).all() and np.max(mispricing) <= MAXIMUM_LOG_MISPRICING),
        "nonnegative_investor_cash_with_original_tolerance": bool(np.isfinite(data["minimum_investor_cash"]).all()
             and np.all(data["minimum_investor_cash"] >= -CONSERVATION_TOLERANCE * data["total_cash"][0])),
        "nonshort_investor_holdings_with_original_tolerance": bool(np.isfinite(data["minimum_investor_holding"]).all()
             and np.all(data["minimum_investor_holding"] >= -CONSERVATION_TOLERANCE)),
    }
    mechanical = {"status": ("PASS" if all(physical_checks.values()) else "FAIL") if full else "insufficient",
                  "observed_prefix_status": "PASS" if all(physical_checks.values()) else "FAIL",
                  "checks": physical_checks, "full_horizon": bool(full), "maximum_relative_cash_error": maximum_cash_error,
                  "maximum_absolute_recorded_signed_share_error": maximum_share_error,
                  "cash_reconstructed_through_day": int(paid_days[-1]), "cash_initial_anchor": "archived total_cash[0]",
                  "partial_last_day_payment_stage": "not independently identifiable" if last > completed else None}
    matrices = {name: np.full((assets, len(MOMENT_NAMES)), np.nan) for name in ("price", "holder_total")}
    correlations = {}
    if full:
        with np.errstate(all="ignore"):
            price_returns = data["prices"][1:] / data["prices"][:-1] - 1
            total_returns = price_returns + config["cash_flow_yield"] * data["intrinsic_values"][1:] / 252 / data["prices"][:-1]
        matrices["price"] = moment_matrix(price_returns, burn)
        matrices["holder_total"] = moment_matrix(total_returns, burn, check_full_period=True)
        for name, matrix in matrices.items():
            checks.close(name + "_nine_moments_from_paths", data[name + "_moments"], matrix, atol=MOMENT_ATOL, rtol=MOMENT_RTOL)
            if record["status"] == "completed":
                checks.close(name + "_json_company_moments", np.asarray(record[name + "_moments_by_company"], dtype=float), matrix, atol=MOMENT_ATOL, rtol=MOMENT_RTOL)
                checks.close(name + "_json_mean_moments", np.asarray(record[name + "_mean_moments"], dtype=float), matrix.mean(axis=0), atol=MOMENT_ATOL, rtol=MOMENT_RTOL)
        for name, returns in (("price", price_returns), ("holder_total", total_returns)):
            with np.errstate(all="ignore"):
                correlation = np.corrcoef(returns[burn:], rowvar=False)
            correlations[name] = {"status": "pending", "pair_count": assets * (assets - 1) // 2,
                                  "statistics": distribution(correlation[np.triu_indices(assets, 1)])}
        if record["status"] == "completed":
            checks.add("declared_value_path_hash", record["intrinsic_value_path_sha256"] == array_sha(data["intrinsic_values"]))
            for name, expected in record["validation"]["mechanical"]["checks"].items():
                checks.add("declared_mechanical:" + name, name in physical_checks and expected == physical_checks.get(name))
            checks.add("declared_stylized", record["validation"]["stylized"]["status"] == stylized(matrices["price"])["status"])
            checks.add("declared_holder_total_stylized", record["holder_total_stylized"]["status"] == stylized(matrices["holder_total"])["status"])
            checks.add("pending_gates_preserved", all(record["validation"][name]["status"] == "pending"
                       for name in ("return_acf", "cross_asset_correlation", "empirical_calibration")))
            checks.add("declared_window", record["validation"]["observations"] == horizon - burn == 2300
                       and record["moment_window"]["return_observations"] == 2300)
    output.update(
        artifact_audit=checks.result(), full_physical_path=bool(full), completed_days=completed, observed_days=last,
        flags={name: {"true_count": int(data[name].sum()), "false_days": np.flatnonzero(~data[name])} for name in FLAG_NAMES},
        path_sha256={name: array_sha(data[name]) for name in PATH_NAMES + FLAG_NAMES + ("cap", "exogenous_day_digest")},
        path_finiteness={name: {"observations": int(data[name][data["quote_recorded"] if name in ("raw", "log_moves") else data["state_recorded"]].size),
                               "nonfinite_values": int(np.count_nonzero(~np.isfinite(data[name][data["quote_recorded"] if name in ("raw", "log_moves") else data["state_recorded"]])))} for name in PATH_NAMES},
        mechanical=mechanical, price_stylized=stylized(matrices["price"]) if full else {"status": "pending"},
        holder_total_stylized=stylized(matrices["holder_total"]) if full else {"status": "pending"},
        price_moments_by_company=matrices["price"], holder_total_moments_by_company=matrices["holder_total"],
        nine_moment_distributions={name: {key: distribution(matrix[:, i]) for i, key in enumerate(MOMENT_NAMES)} for name, matrix in matrices.items()},
        correlations=correlations, cap_daily_counts=cap_daily, cap_events=events,
        cap_count_full=int(data["cap"].sum()), cap_count_measurement=int(data["cap"][burn + 1:].sum()),
        share_max_absolute_error_by_company=np.max(share_error, axis=0),
        initial_signed_share_error={"minimum": float(data["share_error"][0].min()), "maximum": float(data["share_error"][0].max()),
                                    "maximum_absolute": float(share_error[0].max())},
        feedback_distributions={name: distribution(data[name][quote_days]) for name in ("depth_fraction", "feedback_volatility_ratio")},
        maximum_absolute_log_mispricing=distribution(mispricing)["maximum"],
        fingerprint_limit="The NPZ omits full equity_share and gross_volume; stored result fingerprints cannot be independently reconstructed.")
    return output, record


def pair_audit(seed, cases, records, results):
    checks = Checks()
    left, right = (next(row for row in cases if row["seed"] == seed and row["arm"] == arm) for arm in ("m30", "m70"))
    a_record, b_record = records[left["id"]], records[right["id"]]
    a_result, b_result = results[left["id"]], results[right["id"]]
    checks.add("same_configuration_except_memory",
               {k: v for k, v in left["config"].items() if k != "order_flow_memory"} ==
               {k: v for k, v in right["config"].items() if k != "order_flow_memory"})
    for name in ("initialization_sha256", "decision_schedule_sha256"):
        checks.add("recorded_digest_equality:" + name, a_record.get(name) is not None and a_record.get(name) == b_record.get(name))
    output = {"seed": seed, "left": left["id"], "right": right["id"], "difference": "m70 minus m30",
              "input_hashes": {left["id"]: a_result["input_hashes"], right["id"]: b_result["input_hashes"]}}
    if not a_record.get("artifact") or not b_record.get("artifact"):
        output.update(artifact_audit=checks.result(), status="insufficient")
        return output
    with np.load(HERE / a_record["artifact"], allow_pickle=False) as a, np.load(HERE / b_record["artifact"], allow_pickle=False) as b:
        prefix = min(a_record["completed_days"], b_record["completed_days"]) + 1
        checks.add("full_value_prefix", np.array_equal(a["intrinsic_values"][:prefix], b["intrinsic_values"][:prefix]))
        checks.add("full_exogenous_digest_prefix", np.array_equal(a["exogenous_day_digest"][:prefix], b["exogenous_day_digest"][:prefix]))
        checks.add("same_initial_prices_values_size", np.array_equal(a["prices"][0], b["prices"][0])
                   and np.array_equal(a["intrinsic_values"][0], b["intrinsic_values"][0]) and np.array_equal(a["size_class"], b["size_class"]))
        paths = {}
        for name in PATH_NAMES:
            observed = (a["quote_recorded"][:prefix] & b["quote_recorded"][:prefix]) if name in ("raw", "log_moves") else np.ones(prefix, dtype=bool)
            with np.errstate(all="ignore"):
                difference = b[name][:prefix][observed] - a[name][:prefix][observed]
            paths[name] = {"observations_compared": int(observed.sum()), "difference_sha256": array_sha(difference),
                           "maximum_absolute_difference_by_company": np.max(np.abs(difference), axis=0),
                           "mean_difference_by_company": np.mean(difference, axis=0), "last_difference_by_company": difference[-1]}
        with np.errstate(all="ignore"):
            log_gap = np.log(b["prices"][:prefix]) - np.log(a["prices"][:prefix])
        output["log_price_gap_by_company"] = {"mean": np.mean(log_gap, axis=0),
                                              "maximum_absolute": np.max(np.abs(log_gap), axis=0), "last": log_gap[-1]}
        output.update(prefix_days_compared=prefix - 1, full_horizon_compared=prefix == left["config"]["trading_days"] + 1,
                      path_differences_by_company=paths,
                      exogenous_path_sha256={"m30": array_sha(a["exogenous_day_digest"][:prefix]), "m70": array_sha(b["exogenous_day_digest"][:prefix])},
                      intrinsic_value_path_sha256={"m30": array_sha(a["intrinsic_values"][:prefix]), "m70": array_sha(b["intrinsic_values"][:prefix])})
    if a_result.get("full_physical_path") and b_result.get("full_physical_path"):
        differences = {}
        for name in ("price", "holder_total"):
            difference = np.asarray(b_result[name + "_moments_by_company"]) - np.asarray(a_result[name + "_moments_by_company"])
            differences[name] = {"by_company": difference,
                                 "world_mean_difference": difference.mean(axis=0),
                                 "distributions": {key: distribution(difference[:, i]) for i, key in enumerate(MOMENT_NAMES)}}
        output["nine_moment_differences"] = differences
    output.update(artifact_audit=checks.result(), status=checks.result()["status"],
                  limitation="Initialization/schedule and daily RNG digests are compared as archived claims; missing individual initial arrays/RNG states prevent recomputing those digests. Intrinsic value and initial price/size arrays are compared directly.")
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    spec, continuation, original, new, identity, hashes, summary_manifest, saved_summary = lineage()
    if args.check_only:
        print(json.dumps(clean({"status": identity.result()["status"], "identity": identity.result(), "auditor_sha256": sha(Path(__file__)),
                                "market_initializations": 0, "market_runs": 0, "abm_imports": 0}), ensure_ascii=False))
        return 0 if identity.result()["status"] == "PASS" else 1
    if identity.result()["status"] != "PASS":
        raise RuntimeError("Archive lineage preflight failed; use --check-only for all checks")
    hashes["audit_outputs.py"] = sha(Path(__file__))
    results, records = {}, {}
    for case in spec["cases"]:
        contract = original if case["id"] in continuation["preserved_case_ids"] else new
        try:
            output, record = audit_case(case, contract, continuation, spec, summary_manifest)
            results[case["id"]], records[case["id"]] = output, record
            hashes.update(output["input_hashes"])
        except Exception:
            path = HERE / (case["id"] + ".json")
            record = read_json(path) if path.exists() else {"case": case["id"], "arm": case["arm"], "status": "missing"}
            records[case["id"]] = record
            results[case["id"]] = {"case": case["id"], "arm": case["arm"], "seed": case["seed"],
                                   "original_status": record["status"], "artifact_audit": {"status": "FAIL", "error": traceback.format_exc()},
                                   "full_physical_path": False, "mechanical": {"status": "insufficient"},
                                   "price_stylized": {"status": "pending"}, "holder_total_stylized": {"status": "pending"},
                                   "input_hashes": {path.name: sha(path)} if path.exists() else {}}
        print(json.dumps({"case": case["id"], "archive_audit": results[case["id"]]["artifact_audit"]["status"],
                          "mechanical": results[case["id"]]["mechanical"]["status"]}), flush=True)
    pairs = {}
    for seed in spec["budget"]["seeds"]:
        try:
            pairs[seed] = pair_audit(seed, spec["cases"], records, results)
        except Exception:
            pairs[seed] = {"seed": seed, "status": "FAIL", "artifact_audit": {"status": "FAIL", "error": traceback.format_exc()}}
    stable = Checks()
    for name, digest in hashes.items():
        path = ROOT / name if name == spec["source"]["archive"] else HERE / name
        stable.add(name, sha(path) == digest)
    arms = {}
    for arm in ("m30", "m70"):
        rows = [row for row in results.values() if row["arm"] == arm]
        arms[arm] = {
            "scheduled_worlds": len(rows),
            "full_physical_paths": sum(row["full_physical_path"] for row in rows),
            "completed_original_diagnostics": sum(row["original_status"] == "completed" for row in rows),
            "interrupted_original_diagnostics": sum(row["original_status"] == "failed" for row in rows),
            "archive_audit_pass": sum(row["artifact_audit"]["status"] == "PASS" for row in rows),
            "archive_audit_fail": sum(row["artifact_audit"]["status"] == "FAIL" for row in rows),
            "mechanical_pass_worlds": sum(row["mechanical"]["status"] == "PASS" for row in rows),
            "mechanical_fail_worlds": sum(row["mechanical"]["status"] == "FAIL" for row in rows),
            "mechanical_unassessed_worlds": sum(row["mechanical"]["status"] == "insufficient" for row in rows),
            "price_stylized_pass_worlds": sum(row["price_stylized"]["status"] == "PASS" for row in rows),
            "price_stylized_fail_worlds": sum(row["price_stylized"]["status"] == "FAIL" for row in rows),
            "holder_total_stylized_pass_worlds": sum(row["holder_total_stylized"]["status"] == "PASS" for row in rows),
            "holder_total_stylized_fail_worlds": sum(row["holder_total_stylized"]["status"] == "FAIL" for row in rows),
            "cap_hits": sum(row.get("cap_count_full", 0) for row in rows),
            "cap_hits_measurement": sum(row.get("cap_count_measurement", 0) for row in rows),
        }
        full_rows = [row for row in rows if row["full_physical_path"]]
        arms[arm]["nine_moment_full_world_count"] = len(full_rows)
        arms[arm]["nine_moments"] = {}
        for name in ("price", "holder_total"):
            world_means = np.array([np.asarray(row[name + "_moments_by_company"]).mean(axis=0) for row in full_rows])
            arms[arm]["nine_moments"][name] = {
                "mean_of_company_means_by_world": world_means.mean(axis=0) if len(full_rows) else None,
                "world_mean_distributions": {key: distribution(world_means[:, i]) for i, key in enumerate(MOMENT_NAMES)} if len(full_rows) else None,
            }
    summary_checks = Checks()
    summary_checks.add("saved_full_market_count", saved_summary["full_market_paths"] == sum(row["full_physical_path"] for row in results.values()))
    summary_checks.add("saved_diagnostic_counts",
                       saved_summary["completed_diagnostics"] == sum(row["original_status"] == "completed" for row in results.values())
                       and saved_summary["interrupted_diagnostics"] == sum(row["original_status"] == "failed" for row in results.values()))
    for arm in ("m30", "m70"):
        summary_checks.add("saved_cap_count:" + arm, saved_summary["arms"][arm]["observed_caps_including_interrupted_diagnostics"] == arms[arm]["cap_hits"])
    audit_pass = (stable.result()["status"] == "PASS" and summary_checks.result()["status"] == "PASS"
                  and all(row["artifact_audit"]["status"] == "PASS" for row in results.values())
                  and all(row["status"] == "PASS" for row in pairs.values()))
    report = {
        "created_utc": datetime.now(UTC).isoformat(), "auditor_sha256": sha(Path(__file__)),
        "auditor_runtime": {"python": platform.python_version(), "numpy": np.__version__},
        "scope": "Independent archive arithmetic audit; no ABM imports, initialization or new market runs.",
        "artifact_audit_status": "PASS" if audit_pass else "FAIL",
        "identity": identity.result(), "unchanged_inputs_after_audit": stable.result(), "saved_summary_consistency": summary_checks.result(),
        "original_contract": original, "continuation_contract": new, "input_file_sha256": hashes,
        "moment_names": MOMENT_NAMES,
        "definitions": {
            "price_return": "P[t]/P[t-1]-1; direct ratio independently checks the recorded expm1(diff(log(P))) definition.",
            "holder_total_return": "price_return + cash_flow_yield*V[t]/252/P[t-1]; external dividend-inclusive holding-period return, no invented ex-dividend correction.",
            "measurement_window": "Daily returns from day1201 through3500, 2300 observations after burn1200.",
            "nine_moments": "ddof1 volatility; population-standardized excess kurtosis; Pearson lag1 return and lag1/5/20 abs return ACF; linear q.01/q.99; Hill top floor(.025*n) abs demeaned observations versus the next order statistic; minimum250 finite observations and10 tail points.",
            "cash": "Recorded initial total cash plus cumulative yield*current-day V/252 summed over all firms, on guaranteed completed days.",
            "shares": "Every signed recorded investor+noise+maker shares-minus-one residual, including actual day0. Full holdings are not archived, so holdings are not reconstructed.",
            "feedback": "Initial annual asset volatility squared/252; fast/reference EWMA of stored clipped moves squared; prequote sqrt(fast/reference); depth recursion with frozen stress clamp, floor and resilience.",
            "mechanical": "Frozen absolute shares/relative cash tolerance1e-8, no caps, positive finite P/V; original divergence guard abs(log(P/V))<=5 and recorded investor-minimum bounds. Full-path qualification requires all3500 steps.",
            "arithmetic_tolerances": {"quote_absolute": QUOTE_ATOL, "other_absolute": ARITHMETIC_ATOL,
                                      "other_relative": ARITHMETIC_RTOL, "moments_absolute": MOMENT_ATOL, "moments_relative": MOMENT_RTOL},
            "tolerance_role": "Arithmetic roundoff checks only; these do not replace or loosen any model acceptance threshold.",
        },
        "arms": arms, "worlds": list(results.values()), "pairs": pairs,
        "all_worlds_qualification": {
            "mechanical": "PASS" if all(row["mechanical"]["status"] == "PASS" for row in results.values()) else "FAIL",
            "price_stylized": "PASS" if all(row["price_stylized"]["status"] == "PASS" for row in results.values()) else "FAIL",
            "holder_total_stylized": "PASS" if all(row["holder_total_stylized"]["status"] == "PASS" for row in results.values()) else "FAIL",
        },
        "special_original_interruption": {"case": SPECIAL_CASE, "original_status": records[SPECIAL_CASE]["status"],
                                          "full_physical_path": results[SPECIAL_CASE]["full_physical_path"],
                                          "independently_recomputed_mechanical": results[SPECIAL_CASE]["mechanical"],
                                          "independently_recomputed_price_stylized": results[SPECIAL_CASE]["price_stylized"],
                                          "result_fingerprint": "unavailable; original result and status are not rewritten"},
        "return_acf": "pending; all per-company nine-moment values and paired differences reported",
        "cross_asset_correlation": "pending; descriptive pair distributions only",
        "empirical_calibration": "pending", "automatic_winner": None, "extra_worlds": 0,
        "limitations": [
            "Archive arithmetic integrity can PASS while a model mechanical/stylized gate FAILs.",
            "Recorded share residuals and initialization/RNG digests cannot be rebuilt from omitted holdings, individual initial arrays or RNG states.",
            "The full original CrossSectionResult fingerprint cannot be rebuilt without equity_share and gross_volume.",
            "Detailed event attribution is limited to the first4096 caps per world; cap masks/counts and core paths are complete.",
            "For a failed partial final day, quote/settlement flags do not prove dividends or EWMA were applied; cash reconstruction is gated to completed days.",
            "Frozen old source qualifies only the bare market; it does not qualify newer disclosure, financing or Q-learning code.",
            "The fixed two previously observed memory hypotheses are not chosen by this audit; no seed exclusion, added worlds or parameter fitting.",
        ],
    }
    report_path = HERE / "audit_validation.json"
    write_json(report_path, report)
    lines = ["# 固定60世界独立归档审计", "",
             f"归档算术审计：{report['artifact_audit_status']}。读取固定60档、30配对；ABM导入、初始化及新增市场运行均为0。", "",
             "归档一致性与模型门槛分别报告；机械FAIL不代表运行中断，也不会被剔除。", "",
             "|模型|完整路径|原诊断完成/中断|归档PASS/FAIL|机械PASS/FAIL/未评|价格风格PASS/FAIL|含外部股息风格PASS/FAIL|cap全程/测量期|",
             "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for arm, row in arms.items():
        lines.append(f"|{arm}|{row['full_physical_paths']}|{row['completed_original_diagnostics']}/{row['interrupted_original_diagnostics']}|{row['archive_audit_pass']}/{row['archive_audit_fail']}|{row['mechanical_pass_worlds']}/{row['mechanical_fail_worlds']}/{row['mechanical_unassessed_worlds']}|{row['price_stylized_pass_worlds']}/{row['price_stylized_fail_worlds']}|{row['holder_total_stylized_pass_worlds']}/{row['holder_total_stylized_fail_worlds']}|{row['cap_hits']}/{row['cap_hits_measurement']}|")
    lines += ["", "九矩均先按每世界200家公司平均，再对该臂完整世界等权平均；公司不是独立重复。", "",
              "|收益口径|矩|m30|m70|", "|---|---|---:|---:|"]
    for name in ("price", "holder_total"):
        a = arms["m30"]["nine_moments"][name]["mean_of_company_means_by_world"]
        b = arms["m70"]["nine_moments"][name]["mean_of_company_means_by_world"]
        if a is not None and b is not None:
            for i, key in enumerate(MOMENT_NAMES):
                lines.append(f"|{name}|{key}|{a[i]:.12g}|{b[i]:.12g}|")
    special = results[SPECIAL_CASE]
    lines += ["", f"原{SPECIAL_CASE}仍为诊断中断，完整物理路径={special['full_physical_path']}；独立机械复算={special['mechanical']['status']}，价格风格复算={special['price_stylized']['status']}。原JSON/NPZ/status不改，完整result fingerprint无法从最小归档重建。", "",
              "审计JSON保留每家公司两口径九矩、30配对全部公司差分、全部日cap计数、逐资产股份残差最大值、所有算术检查及输入哈希。股份检查使用已保存的实际有符号残差；不声称从未保存的全持仓重新结算。", "",
              "按当前日V重建外部股息现金；价格与含外部股息收益分开。收益ACF、相关性及实证校准仍pending，不自动选赢家。2300测量日与包含记录器/写盘的用时不能替代原2500日生产速度验收。", ""]
    (HERE / "audit_report.md").write_text("\n".join(lines), encoding="utf-8")
    used = sum(path.stat().st_size for path in HERE.rglob("*") if path.is_file())
    write_json(HERE / "audit_manifest.json", {
        "auditor_sha256": sha(Path(__file__)), "input_file_sha256": hashes,
        "validation_sha256": sha(report_path), "report_sha256": sha(HERE / "audit_report.md"),
        "directory_bytes_before_audit_manifest": used, "frozen_maximum_directory_bytes": spec["storage"]["maximum_directory_bytes"],
        "free_bytes": shutil.disk_usage(HERE).free, "frozen_minimum_free_bytes": spec["storage"]["minimum_free_bytes"],
        "market_initializations": 0, "market_runs": 0, "abm_imports": 0,
    })
    print(json.dumps({"artifact_audit_status": report["artifact_audit_status"], "worlds": len(results), "pairs": len(pairs),
                      "cap_hits": sum(row["cap_hits"] for row in arms.values()), "market_runs": 0}))
    return 0 if audit_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
