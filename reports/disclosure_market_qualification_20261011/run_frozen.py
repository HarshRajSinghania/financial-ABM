"""Run the fixed sixty bare-market qualification worlds on archived sources."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import shutil
import sys
import time
import traceback
import zipfile

THREAD_VARIABLES = ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS", "NUMEXPR_NUM_THREADS")
for variable in THREAD_VARIABLES:
    os.environ[variable] = "1"
sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC_PATH = HERE / "freeze.json"
SPEC = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
SOURCE = HERE / "isolated_src"


class GlobalStop(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise GlobalStop(message)


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def prepare_sources():
    provenance = SPEC["source"]
    archive = ROOT / provenance["archive"]
    require(sha(archive) == provenance["archive_sha256"], "Source archive identity changed")
    expected = provenance["source_hashes"]
    with zipfile.ZipFile(archive) as bundle:
        require(set(bundle.namelist()) == set(expected), "Unexpected archive members")
        for name, digest in expected.items():
            parts = PurePosixPath(name).parts
            require(parts and parts[0] == "abm" and ".." not in parts, "Unsafe archive member")
            data = bundle.read(name)
            require(hashlib.sha256(data).hexdigest() == digest, "Archived source hash differs: " + name)
            target = SOURCE.joinpath(*parts)
            if target.exists():
                require(sha(target) == digest, "Isolated source changed: " + name)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as stream:
                    stream.write(data)
    return expected


SOURCE_HASHES = prepare_sources()
require(not any(name == "abm" or name.startswith("abm.") for name in sys.modules), "abm imported before isolation")
sys.path.insert(0, str(SOURCE))

import numpy as np

from abm.disclosure import harness
from abm.disclosure.config import MarketConfig, TRADING_DAYS_PER_YEAR
from abm.disclosure.harness import CrossSectionMarket
from abm.disclosure.market import CrossSectionBook
from abm.disclosure.validate import validate_market
from abm.msm import MOMENT_NAMES, compute_moments
from abm.platform_tuning import disable_power_throttling


def clean(value):
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, (np.floating, float)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.bool_):
        return bool(value)
    return value


def write_json(path, value, *, exclusive=False):
    content = json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if exclusive:
        with path.open("x", encoding="utf-8") as stream:
            stream.write(content)
    else:
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(path)


def array_sha(array):
    array = np.ascontiguousarray(array)
    return hashlib.sha256(str(array.dtype).encode() + str(array.shape).encode() + array.tobytes()).hexdigest()


def distribution(values):
    values = np.asarray(values)
    finite = values[np.isfinite(values)]
    return {"count": int(values.size), "finite_count": int(finite.size),
            "mean": float(finite.mean()) if finite.size else None,
            "minimum": float(finite.min()) if finite.size else None,
            "quantile_05": float(np.quantile(finite, .05)) if finite.size else None,
            "median": float(np.median(finite)) if finite.size else None,
            "quantile_95": float(np.quantile(finite, .95)) if finite.size else None,
            "maximum": float(finite.max()) if finite.size else None}


def verify_sources(contract=None):
    for name, digest in SOURCE_HASHES.items():
        require(sha(SOURCE / name) == digest, "Isolated source changed: " + name)
    require(sha(ROOT / SPEC["source"]["archive"]) == SPEC["source"]["archive_sha256"], "Source zip changed")
    for name, module in tuple(sys.modules.items()):
        if name == "abm" or name.startswith("abm."):
            filename = getattr(module, "__file__", None)
            if filename:
                path = Path(filename).resolve()
                require(path.is_relative_to(SOURCE), "Non-isolated abm import: " + name)
                relative = path.relative_to(SOURCE).as_posix()
                require(relative in SOURCE_HASHES and sha(path) == SOURCE_HASHES[relative], "Imported source identity differs: " + name)
    if contract is not None:
        require(sha(SPEC_PATH) == contract["spec_sha256"], "Frozen spec changed")
        require(sha(Path(__file__)) == contract["launcher_sha256"], "Launcher changed")
        require(sha(HERE / "initial_manifest.json") == contract["initial_manifest_sha256"], "Initial manifest changed")
        require(sha(HERE / "seed_lineage.json") == contract["seed_lineage_sha256"], "Seed lineage receipt changed")


def resource_check():
    used = sum(path.stat().st_size for path in HERE.rglob("*") if path.is_file())
    budget = SPEC["storage"]
    require(used <= budget["maximum_directory_bytes"], "Archive exceeds frozen storage budget")
    free = shutil.disk_usage(HERE).free
    require(free - (budget["maximum_directory_bytes"] - used) >= budget["minimum_free_bytes"],
            "Insufficient disk space for remaining frozen budget plus reserve")
    return {"directory_bytes": used, "free_bytes": free, "minimum_free_bytes": budget["minimum_free_bytes"]}


class Recorder:
    def __init__(self, market):
        self.market, self.cfg = market, market.config
        shape = (self.cfg.trading_days + 1, self.cfg.n_firms)
        self.data = {name: np.full(shape, np.nan) for name in SPEC["storage"]["float64_paths"]}
        self.data["cap"] = np.zeros(shape, dtype=bool)
        for name in ("total_cash", "expected_total_cash", "minimum_investor_cash", "minimum_investor_holding"):
            self.data[name] = np.full(shape[0], np.nan)
        for name in ("state_recorded", "quote_recorded", "settlement_recorded", "step_completed"):
            self.data[name] = np.zeros(shape[0], dtype=bool)
        self.data["exogenous_day_digest"] = np.zeros(shape[0], dtype="S32")
        limit = SPEC["storage"]["maximum_detailed_events_per_world"]
        self.events = np.full((limit, len(SPEC["storage"]["event_float_fields"])), np.nan)
        self.event_index = np.zeros((limit, 4), dtype=np.int64)
        self.event_count = self.total_events = self.day = 0
        self.cash_calls = []
        self.step_seconds = self.inner_recording_seconds = self.state_recording_seconds = 0.0
        fields = ("cash", "holdings", "investor_type", "taste", "risk_aversion", "decision_interval", "decision_offset", "choice_intensity")
        self.initialization_hash = hashlib.sha256(json.dumps({
            "prices": array_sha(market.prices), "values": array_sha(market.firms.intrinsic_value),
            "size_class": array_sha(market.firms.size_class),
            "investors": {name: array_sha(getattr(market.investors, name)) for name in fields},
        }, sort_keys=True).encode()).hexdigest()
        self.schedule_hash = array_sha(np.c_[market.investors.decision_interval, market.investors.decision_offset])
        self.record_state(0)

    def record_state(self, day):
        started = time.perf_counter()
        m, data = self.market, self.data
        data["prices"][day], data["intrinsic_values"][day] = m.prices, m.firms.intrinsic_value
        data["share_error"][day] = m.investors.holdings.sum(axis=0) + m.noise_holdings + m.market_maker_inventory - 1
        data["total_cash"][day] = m._total_cash()
        data["expected_total_cash"][day] = m.initial_total_cash + m.dividends_paid
        data["minimum_investor_cash"][day] = m.investors.cash.min()
        data["minimum_investor_holding"][day] = m.investors.holdings.min()
        if not data["quote_recorded"][day]:
            data["depth_fraction"][day] = m.book.depth_fraction
            data["feedback_volatility_ratio"][day] = np.sqrt(m.book.variance / m.book.reference_variance)
        digest = hashlib.sha256()
        digest.update(json.dumps({"fundamental": m.fundamental_rng.bit_generator.state,
                                  "noise": m.noise_rng.bit_generator.state}, sort_keys=True).encode())
        digest.update(np.ascontiguousarray(m.firms.intrinsic_value).tobytes())
        digest.update(np.asarray([m.noise_common], dtype=np.float64).tobytes())
        digest.update(np.ascontiguousarray(m.noise_idiosyncratic).tobytes())
        data["exogenous_day_digest"][day] = digest.digest()
        data["state_recorded"][day] = True
        self.state_recording_seconds += time.perf_counter() - started

    def __enter__(self):
        self.original = (CrossSectionMarket.step, CrossSectionBook.price_moves, harness._cap_buys_to_cash)
        original_step, original_moves, original_cap = self.original

        def capture_cap(orders, cash, prices, cost):
            result = original_cap(orders, cash, prices, cost)
            computed = time.perf_counter()
            self.cash_calls.append(result.sum(axis=0))
            self.inner_recording_seconds += time.perf_counter() - computed
            return result

        def capture_moves(book, net_flow_value, market_cap, news, inventory_gap):
            started = time.perf_counter()
            cfg, data, day = self.cfg, self.data, self.day
            transient_before, expected_before = book.transient_impact.copy(), book.expected_flow_impact.copy()
            depth_before = book.depth_fraction.copy()
            ratio = np.sqrt(book.variance / book.reference_variance)
            before_call = time.perf_counter()
            moves, capped = original_moves(book, net_flow_value, market_cap, news, inventory_gap)
            after_call = time.perf_counter()
            flow = cfg.price_impact * net_flow_value / (cfg.liquidity_fraction * market_cap)
            raw = cfg.news_pass_through * news + cfg.permanent_impact_fraction * flow + book.transient_impact - transient_before + cfg.market_maker_inventory_skew * inventory_gap
            require(np.array_equal(moves, np.clip(raw, -cfg.max_log_return, cfg.max_log_return), equal_nan=True), "Quote recorder differs from source")
            require(np.array_equal(capped, moves != raw) and len(self.cash_calls) == 2, "Unexpected quote/cash-call contract")
            data["raw"][day], data["log_moves"][day], data["cap"][day] = raw, moves, capped
            data["depth_fraction"][day], data["feedback_volatility_ratio"][day] = book.depth_fraction, ratio
            data["quote_recorded"][day] = True
            assets = np.flatnonzero(capped)
            self.total_events += assets.size
            for asset in assets[:self.events.shape[0] - self.event_count]:
                i = self.event_count
                direction = int(np.sign(raw[asset])) if np.isfinite(raw[asset]) else 0
                self.event_index[i] = day, asset, self.market.firms.size_class[asset], direction
                self.events[i] = (
                    cfg.news_pass_through * news[asset], cfg.permanent_impact_fraction * flow[asset],
                    book.transient_impact[asset] - transient_before[asset], cfg.market_maker_inventory_skew * inventory_gap[asset],
                    raw[asset], moves[asset], depth_before[asset], book.depth_fraction[asset], ratio[asset],
                    book.variance[asset], book.reference_variance[asset], expected_before[asset], book.expected_flow_impact[asset],
                    transient_before[asset], book.transient_impact[asset], self.cash_calls[0][asset], self.cash_calls[1][asset],
                    np.nan, np.nan, min(ratio[asset], 4.0) ** cfg.noise_volatility_exponent,
                    self.market.market_maker_inventory[asset], self.market.noise_holdings[asset],
                    self.market.prices[asset], self.market.firms.intrinsic_value[asset],
                )
                self.event_count += 1
            self.inner_recording_seconds += time.perf_counter() - started - (after_call - before_call)
            return moves, capped

        def capture_step(market, day_index):
            self.day, self.cash_calls = day_index + 1, []
            first_event = self.event_count
            started = time.perf_counter()
            try:
                original_step(market, day_index)
                self.data["step_completed"][self.day] = True
            finally:
                self.step_seconds += time.perf_counter() - started
                if len(self.cash_calls) == 4:
                    self.data["settlement_recorded"][self.day] = True
                    for i in range(first_event, self.event_count):
                        asset = self.event_index[i, 1]
                        self.events[i, 17:19] = self.cash_calls[2][asset], self.cash_calls[3][asset]
                self.record_state(self.day)

        CrossSectionMarket.step, CrossSectionBook.price_moves, harness._cap_buys_to_cash = capture_step, capture_moves, capture_cap
        return self

    def __exit__(self, *_):
        CrossSectionMarket.step, CrossSectionBook.price_moves, harness._cap_buys_to_cash = self.original


def load_record(case, contract):
    path = HERE / (case["id"] + ".json")
    if not path.exists():
        return None
    record = json.loads(path.read_text(encoding="utf-8"))
    require(record["contract"] == contract and record["config"] == case["config"], "Case identity differs: " + case["id"])
    require(record["status"] in ("completed", "failed"), "Unresolved earlier attempt: " + case["id"])
    if record.get("artifact"):
        require(sha(HERE / record["artifact"]) == record["artifact_sha256"], "Artifact hash differs: " + case["id"])
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
        require(np.allclose(np.abs(recorder.data["share_error"]).max(axis=1), result.maximum_share_error, rtol=0, atol=1e-15), "Per-asset share record differs")
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
    arms, pairs = {}, {}
    for arm in SPEC["arms"]:
        rows = [row for row in records if row["arm"] == arm["id"]]
        completed = [row for row in rows if row["status"] == "completed"]
        stats = {"scheduled_worlds": 30, "completed_worlds": len(completed),
                 "failed_worlds": sum(row["status"] == "failed" for row in rows),
                 "mechanical_pass_worlds": sum(row["validation"]["mechanical"]["status"] == "PASS" for row in completed),
                 "mechanical_fail_worlds": sum(row["validation"]["mechanical"]["status"] == "FAIL" for row in completed),
                 "mechanical_unassessed_worlds": 30 - len(completed),
                 "all_worlds_mechanical_pass": len(completed) == 30 and all(row["validation"]["mechanical"]["status"] == "PASS" for row in completed),
                 "all_worlds_price_stylized_pass": len(completed) == 30 and all(row["validation"]["stylized"]["status"] == "PASS" for row in completed),
                 "all_worlds_holder_total_stylized_pass": len(completed) == 30 and all(row["holder_total_stylized"]["status"] == "PASS" for row in completed),
                 "observed_caps_including_failed_prefixes": sum(row.get("cap_hits_full_observed", 0) for row in rows)}
        for name in ("price", "holder_total"):
            stats[name + "_mean_moments"] = np.mean(np.asarray([row[name + "_mean_moments"] for row in completed], dtype=float), axis=0) if len(completed) == 30 else None
            values = np.concatenate([np.asarray(row[name + "_moments_by_company"], dtype=float) for row in completed]) if completed else np.empty((0, len(MOMENT_NAMES)))
            stats[name + "_company_distributions_completed_worlds"] = {key: distribution(values[:, i]) for i, key in enumerate(MOMENT_NAMES)}
        arms[arm["id"]] = stats
    for seed in SPEC["budget"]["seeds"]:
        rows = {row["arm"]: row for row in records if row["seed"] == seed}
        pair = check_pair(next(case for case in SPEC["cases"] if case["seed"] == seed), rows["m30"], contract)
        if all(row["status"] == "completed" for row in rows.values()):
            for name in ("price", "holder_total"):
                delta = np.asarray(rows["m70"][name + "_moments_by_company"], dtype=float) - np.asarray(rows["m30"][name + "_moments_by_company"], dtype=float)
                pair[name + "_company_moment_delta_m70_minus_m30"] = delta
                pair[name + "_world_mean_delta_m70_minus_m30"] = delta.mean(axis=0)
        pairs[seed] = pair
    terminal = all(row["status"] in ("completed", "failed") for row in records)
    summary = {"contract": contract, "status": "complete" if terminal else "incomplete", "scheduled_worlds": 60,
               "completed_worlds": sum(row["status"] == "completed" for row in records),
               "failed_worlds": sum(row["status"] == "failed" for row in records), "arms": arms, "pairs": pairs,
               "moment_names": MOMENT_NAMES, "measurement_days": 2300,
               "return_acf": "pending", "cross_asset_correlation": "pending", "empirical_calibration": "pending", "automatic_winner": None,
               "records": [{key: row.get(key) for key in ("case", "seed", "arm", "status", "completed_days", "artifact_sha256",
                            "cap_hits_full_observed", "detailed_events_saved", "detailed_events_omitted", "validation", "holder_total_stylized",
                            "market_step_compute_seconds_estimate", "market_run_wall_seconds_including_telemetry", "archive_write_wall_seconds", "total_wall_seconds")}
                           for row in records], "limits": SPEC["limits"]}
    write_json(HERE / "summary.json", summary)
    lines = ["# 固定双假设市场资格检查", "", f"预定60世界；完成归档/诊断{summary['completed_worlds']}，运行/诊断中断{summary['failed_worlds']}，状态{summary['status']}。status=completed仍可能机械FAIL；status=failed表示运行或诊断中断。测量窗口2300日。rACF、相关性与实证校准仍pending；没有自动选赢家。", "",
             "|模型|完成/30|运行中断|机械PASS|机械FAIL|机械未评|全部机械门槛|全部公司价格风格事实|含股息风格事实|所有已观察cap|", "|---|---:|---:|---:|---:|---:|---|---|---|---:|"]
    for name, row in arms.items():
        lines.append(f"|{name}|{row['completed_worlds']}|{row['failed_worlds']}|{row['mechanical_pass_worlds']}|{row['mechanical_fail_worlds']}|{row['mechanical_unassessed_worlds']}|{row['all_worlds_mechanical_pass']}|{row['all_worlds_price_stylized_pass']}|{row['all_worlds_holder_total_stylized_pass']}|{row['observed_caps_including_failed_prefixes']}|")
    for name in ("price", "holder_total"):
        lines += ["", name + "：公司等权、世界等权；缺少任何完整世界时不提供臂均值。", "", "|矩|m30|m70|", "|---|---:|---:|"]
        for i, key in enumerate(MOMENT_NAMES):
            cells = [f"{arms[arm][name + '_mean_moments'][i]:.7g}" if arms[arm][name + "_mean_moments"] is not None else "pending" for arm in ("m30", "m70")]
            lines.append("|" + "|".join([key] + cells) + "|")
    lines += ["", "逐公司九矩、分布、逐种子配对差及失败前缀见JSON/NPZ。门槛按全部世界、资产与日取AND；6000公司样本不等于6000独立世界。cap不终止世界，也不追加世界。", "",
              "7条float64路径保存完整P/V、raw、log move、有符号股份误差、深度与报价前波动率/参考波动率比。cap记录完整；详细事件仅保留最早4096条并报告省略数。失败日的部分状态由标记区分，不伪装完整交易日。", "",
              "含股息收益=P[t]/P[t-1]-1+yield*V[t]/(252*P[t-1])；未补造除息调整。bare市场不含披露决策、QL、核查或企业支出，旧包中的相关版本不由此得到验收。", "",
              "±0.3是当前报价截断协议，未获得真实涨跌幅制度解释。带记录器的单线程计时及相减市场计算估计不替代原2500测量日<60秒性能条款。", ""]
    (HERE / "report.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(HERE / "summary_manifest.json", {"contract": contract, "summary_sha256": sha(HERE / "summary.json"),
                                                "report_sha256": sha(HERE / "report.md"),
                                                "case_json_sha256": {row["case"]: sha(HERE / (row["case"] + ".json")) for row in records if row["status"] != "not_started"}})
    return summary


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--check-only", action="store_true")
    modes.add_argument("--summarize-only", action="store_true")
    args = parser.parse_args()
    require(platform.python_version() == SPEC["runtime"]["python_version"] and np.__version__ == SPEC["runtime"]["numpy_version"], "Runtime version differs")
    require(sha(Path(__file__)) == SPEC["launcher_sha256"], "Launcher differs from frozen spec")
    cases = SPEC["cases"]
    require(len(cases) == len({row["id"] for row in cases}) == 60, "Expected exactly sixty unique cases")
    require(SPEC["budget"]["seeds"] == list(range(710101, 710131)), "Unexpected seed set")
    base = SPEC["base_config"]
    for seed in SPEC["budget"]["seeds"]:
        pair = [row for row in cases if row["seed"] == seed]
        require({row["arm"] for row in pair} == {"m30", "m70"} and len(pair) == 2, "Unexpected pair")
        for case in pair:
            expected = dict(base, seed=seed, order_flow_memory=.3 if case["arm"] == "m30" else .7)
            require(case["config"] == expected, "Case differs from fixed hypothesis")
            cfg = MarketConfig.from_dict(case["config"])
            require((cfg.n_investors, cfg.n_firms, cfg.trading_days, cfg.burn_in_days, cfg.max_log_return) == (1000, 200, 3500, 1200, .3), "Unexpected scale or cap")
    initial = json.loads((HERE / "initial_manifest.json").read_text(encoding="utf-8"))
    require(initial["spec_sha256"] == sha(SPEC_PATH) and initial["launcher_sha256"] == sha(Path(__file__)), "Initial identity differs")
    require(initial["seed_lineage_sha256"] == sha(HERE / "seed_lineage.json"), "Seed lineage identity differs")
    contract = {"spec_sha256": sha(SPEC_PATH), "launcher_sha256": sha(Path(__file__)),
                "initial_manifest_sha256": sha(HERE / "initial_manifest.json"), "seed_lineage_sha256": sha(HERE / "seed_lineage.json"),
                "source_zip_sha256": SPEC["source"]["archive_sha256"], "python_version": platform.python_version(), "numpy_version": np.__version__}
    verify_sources(contract)
    storage = resource_check()
    launch = HERE / "launch_manifest.json"
    if launch.exists():
        require(json.loads(launch.read_text(encoding="utf-8"))["contract"] == contract, "Earlier launch identity differs")
    if not args.run and not args.summarize_only:
        write_json(HERE / "preflight.json", {"status": "ready_for_review", "contract": contract, "configurations": 60,
                                            "market_initializations": 0, "market_runs": 0, "isolated_source_files": len(SOURCE_HASHES),
                                            "measurement_days": 2300, "storage": storage})
        print("Preflight ready for review: sixty frozen configurations; zero market initializations and runs")
        return
    lock = HERE / "writer.lock"
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.write(descriptor, str(os.getpid()).encode())
        if not launch.exists():
            write_json(launch, {"contract": contract, "started_utc": datetime.now(UTC).isoformat(),
                                "thread_environment": {name: os.environ[name] for name in THREAD_VARIABLES}}, exclusive=True)
        if args.run:
            disable_power_throttling()
            for case in cases:
                run_case(case, contract)
        summary = summarize(contract)
        verify_sources(contract)
        resource_check()
        print(json.dumps({"status": summary["status"], "completed_worlds": summary["completed_worlds"], "failed_worlds": summary["failed_worlds"], "automatic_winner": None}))
    except BaseException as error:
        write_json(HERE / "global_stop.json", {"contract": contract, "stopped_utc": datetime.now(UTC).isoformat(),
                                              "exception_type": type(error).__name__, "error": traceback.format_exc(), "automatic_extra_worlds": 0})
        raise
    finally:
        os.close(descriptor)
        lock.unlink()


if __name__ == "__main__":
    main()
