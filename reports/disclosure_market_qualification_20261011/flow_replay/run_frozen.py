"""Recover flow from sixty exact archived-path replays, then diagnose forecasts."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import time
import traceback

for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
sys.dont_write_bytecode = True

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = json.loads((HERE / "freeze.json").read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def clean(value):
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, np.ndarray)):
        return [clean(item) for item in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, (int, np.integer)):
        return int(value)
    return value


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def equal_bytes(actual, expected, message):
    require(actual.dtype == expected.dtype and actual.shape == expected.shape and np.ascontiguousarray(actual).tobytes() == np.ascontiguousarray(expected).tobytes(), message)


def check_source(parent):
    source = ROOT / SPEC["source"]["isolated_directory"]
    expected = parent["source"]["source_hashes"]
    require({path.relative_to(source).as_posix() for path in source.rglob("*.py")} == set(expected), "Source member set differs")
    for name, digest in expected.items():
        require(sha(source / name) == digest, "Source changed: " + name)


def resource_check():
    used = sum(path.stat().st_size for path in HERE.rglob("*") if path.is_file())
    budget = SPEC["budget"]
    require(used <= budget["maximum_directory_bytes"], "Replay directory exceeds900MB")
    require(shutil.disk_usage(HERE).free - (budget["maximum_directory_bytes"] - used) >= budget["minimum_free_bytes"], "Insufficient disk reserve")


def preflight():
    initial = json.loads((HERE / "initial_manifest.json").read_text(encoding="utf-8"))
    for name, digest in initial["files"].items():
        require(sha(HERE / name) == digest, "Diagnostic freeze changed: " + name)
    for name in ("parent_freeze", "parent_launcher", "parent_audit", "archive"):
        require(sha(ROOT / SPEC["source"][name]) == SPEC["source"][name + "_sha256"], "Reference identity differs: " + name)
    parent = json.loads((ROOT / SPEC["source"]["parent_freeze"]).read_text(encoding="utf-8"))
    require([(row["id"], row["arm"], row["seed"]) for row in SPEC["cases"]] == [(row["id"], row["arm"], row["seed"]) for row in parent["cases"]], "Replay cases differ")
    require(len(SPEC["cases"]) == SPEC["budget"]["replays"] == 60, "Replay budget differs")
    for case, original in zip(SPEC["cases"], parent["cases"]):
        for name in ("json", "npz"):
            require(sha(ROOT / case[name]) == case[name + "_sha256"], "Original archive changed: " + case[name])
        record = json.loads((ROOT / case["json"]).read_text(encoding="utf-8"))
        require(record["config"] == original["config"] and record["status"] == case["original_status"], "Original config/status differs: " + case["id"])
        require(original["config"]["trading_days"] == 3500 and original["config"]["n_firms"] == 200 and original["config"]["burn_in_days"] == 1200, "Original dimensions differ")
    require(platform.python_version() == SPEC["runtime"]["python_version"] and np.__version__ == SPEC["runtime"]["numpy_version"], "Runtime differs")
    check_source(parent)
    resource_check()
    return parent


def error_metrics(errors):
    left, right = errors[:-1], errors[1:]
    left, right = left - left.mean(axis=0), right - right.mean(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        acf = (left * right).sum(axis=0) / np.sqrt((left**2).sum(axis=0) * (right**2).sum(axis=0))
    return np.column_stack(((errors**2).mean(axis=0), np.abs(errors).mean(axis=0), acf))


def offline(u, reference, source_m, source_t, cfg):
    depth, observed_raw = reference["depth_fraction"][1:], reference["raw"][1:]
    rho, p, decay = cfg.order_flow_memory, cfg.permanent_impact_fraction, cfg.transient_impact_decay
    m, q, ti, tf = (np.zeros(cfg.n_firms) for _ in range(4))
    ei, ef, delta_i, delta_f = (np.empty_like(u) for _ in range(4))
    for t in range(u.shape[0]):
        ei[t], ef[t] = u[t] - depth[t] * m, u[t] - q
        si, sf = u[t] / depth[t] - m, (u[t] - q) / depth[t]
        m = rho * m + (1 - rho) * u[t] / depth[t]
        q = rho * q + (1 - rho) * u[t]
        previous_i, previous_f = ti, tf
        ti, tf = decay * ti + (1 - p) * si, decay * tf + (1 - p) * sf
        equal_bytes(m, source_m[t], "Offline source EMA mismatch day " + str(t + 1))
        equal_bytes(ti, source_t[t], "Offline source transient mismatch day " + str(t + 1))
        delta_i[t], delta_f[t] = ti - previous_i, tf - previous_f
    require(np.isfinite(ei).all() and np.isfinite(ef).all(), "Nonfinite offline errors")
    current, alternative = error_metrics(ei[cfg.burn_in_days:]), error_metrics(ef[cfg.burn_in_days:])
    conditional_raw = observed_raw + delta_f - delta_i
    require(np.isfinite(conditional_raw).all(), "Nonfinite conditional quote")
    original_cap = reference["cap"][1:]
    conditional_cap = np.clip(conditional_raw, -cfg.max_log_return, cfg.max_log_return) != conditional_raw
    masks = {"original": original_cap, "conditional": conditional_cap, "retained": original_cap & conditional_cap, "disappeared": original_cap & ~conditional_cap, "newly_added": ~original_cap & conditional_cap}
    counts = {phase: {name: int(mask[window].sum()) for name, mask in masks.items()} for phase, window in (("full", slice(None)), ("burn", slice(0, cfg.burn_in_days)), ("measurement", slice(cfg.burn_in_days, None)))}
    events = []
    for index, values in zip(reference["detailed_event_index"], reference["detailed_events"]):
        day, asset = int(index[0]), int(index[1])
        t = day - 1
        events.append({"day": day, "asset": asset, "original_raw": float(observed_raw[t, asset]), "conditional_raw": float(conditional_raw[t, asset]), "depth": float(depth[t, asset]), "u": float(u[t, asset]), "current_error_u_units": float(ei[t, asset]), "alternative_error_u_units": float(ef[t, asset]), "current_native_surprise": float(ei[t, asset] / depth[t, asset]), "alternative_native_surprise": float(ef[t, asset] / depth[t, asset]), "current_transient_change": float(delta_i[t, asset]), "alternative_transient_change": float(delta_f[t, asset]), "original_news_quote": float(values[0]), "original_permanent_quote": float(values[1]), "original_inventory_quote": float(values[3]), "conditional_cap": bool(conditional_cap[t, asset])})
    return {"source_state_check": "bytewise PASS all3500x200", "metric_names": ["MSE", "MAE", "lag1_ACF"], "current_by_company": current, "alternative_by_company": alternative, "current_world_mean": current.mean(axis=0), "alternative_world_mean": alternative.mean(axis=0), "world_difference_alternative_minus_current": (alternative - current).mean(axis=0), "defined_companies_current": np.isfinite(current).sum(axis=0), "defined_companies_alternative": np.isfinite(alternative).sum(axis=0), "conditional_cap_counts": counts, "original_cap_events": events, "conditional_near_threshold_count": int((np.abs(np.abs(conditional_raw) - cfg.max_log_return) <= 1e-12).sum()), "conditional_threshold_tolerance_role": "flag only; exact clipping classification unchanged"}


def run_one(case, original, parent, module):
    started = time.perf_counter()
    row = {"case": case["id"], "arm": case["arm"], "seed": case["seed"], "original_status": case["original_status"], "original_mechanical_status": case["original_mechanical_status"], "audited_mechanical_status": case["audited_mechanical_status"], "status": "running", "quoted_days": 0, "observed_input_days": 0, "completed_steps": 0}
    cfg = module.MarketConfig.from_dict(original["config"])
    u = np.empty((cfg.trading_days, cfg.n_firms))
    source_m, source_t = np.empty_like(u), np.empty_like(u)
    market = recorder = None
    observed = quoted = 0
    try:
        check_source(parent)
        module.verify_sources()
        for name in ("json", "npz"):
            require(sha(ROOT / case[name]) == case[name + "_sha256"], "Original file changed: " + case[name])
        record = json.loads((ROOT / case["json"]).read_text(encoding="utf-8"))
        with np.load(ROOT / case["npz"], allow_pickle=False) as bundle:
            reference = {name: bundle[name] for name in bundle.files}
        require(len(reference) == 23, "Original NPZ member count differs")
        market = module.CrossSectionMarket(cfg)
        recorder = module.Recorder(market)
        require(recorder.initialization_hash == record["initialization_sha256"] and recorder.schedule_hash == record["decision_schedule_sha256"], "Replay initialization/schedule differs")
        with recorder:
            wrapped = module.CrossSectionBook.price_moves

            def capture_u(book, net_flow_value, market_cap, news, inventory_gap):
                nonlocal observed, quoted
                t = observed
                require(t < cfg.trading_days, "Extra quote beyond fixed budget")
                u[t] = cfg.price_impact * net_flow_value / (cfg.liquidity_fraction * market_cap)
                observed += 1
                equal_bytes(market_cap, reference["prices"][t], "Reference P differs day " + str(t + 1))
                equal_bytes(market.firms.intrinsic_value, reference["intrinsic_values"][t + 1], "V differs day " + str(t + 1))
                moves, capped = wrapped(book, net_flow_value, market_cap, news, inventory_gap)
                quoted += 1
                source_m[t], source_t[t] = book.expected_flow_impact, book.transient_impact
                for name, values in (("raw", recorder.data["raw"][t + 1]), ("log_moves", moves), ("depth_fraction", book.depth_fraction), ("cap", capped)):
                    equal_bytes(values, reference[name][t + 1], "Quote differs " + name + " day " + str(t + 1))
                equal_bytes(market_cap * np.exp(moves), reference["prices"][t + 1], "Next P differs day " + str(t + 1))
                return moves, capped

            module.CrossSectionBook.price_moves = capture_u
            replay_started = time.perf_counter()
            try:
                result = market.run()
            finally:
                module.CrossSectionBook.price_moves = wrapped
            row["replay_wall_seconds_including_telemetry"] = time.perf_counter() - replay_started
        require(observed == quoted == market.next_day_index == cfg.trading_days, "Incomplete replay")
        equal_bytes(result.prices, reference["prices"], "Result P differs")
        equal_bytes(result.intrinsic_values, reference["intrinsic_values"], "Result V differs")
        compared = []
        for name, values in recorder.data.items():
            equal_bytes(values, reference[name], "Original NPZ differs: " + name)
            compared.append(name)
        price_validation = module.validate_market(result, cfg)
        price_moments = np.array([[asset["moments"][name] for name in module.MOMENT_NAMES] for asset in price_validation["moments_per_asset"]], dtype=float)
        price_returns = np.expm1(np.diff(np.log(result.prices), axis=0))
        holder = price_returns + cfg.cash_flow_yield * result.intrinsic_values[1:] / module.TRADING_DAYS_PER_YEAR / result.prices[:-1]
        holder_moments = np.full((cfg.n_firms, len(module.MOMENT_NAMES)), np.nan)
        for asset in range(cfg.n_firms):
            if np.all(np.isfinite(holder[:, asset])):
                try:
                    holder_moments[asset] = module.compute_moments(holder[cfg.burn_in_days:, asset])
                except ValueError:
                    pass
        remaining = {"day": np.arange(cfg.trading_days + 1), "size_class": market.firms.size_class, "detailed_event_index": recorder.event_index[:recorder.event_count], "detailed_events": recorder.events[:recorder.event_count], "price_moments": price_moments, "holder_total_moments": holder_moments}
        for name, values in remaining.items():
            equal_bytes(values, reference[name], "Original NPZ differs: " + name)
            compared.append(name)
        require(set(compared) == set(reference), "Uncompared NPZ arrays")
        fingerprint = result.fingerprint()
        require(record.get("result_fingerprint") is None or fingerprint == record["result_fingerprint"], "Original result fingerprint differs")
        row.update(bitwise_arrays=compared, replay_fingerprint=fingerprint, original_fingerprint_check="unavailable in original interrupted record" if record.get("result_fingerprint") is None else "PASS")
        statistics_started = time.perf_counter()
        row["offline"] = offline(u, reference, source_m, source_t, cfg)
        row["offline_wall_seconds"] = time.perf_counter() - statistics_started
        row["status"] = "completed"
    except BaseException as exc:
        row.update(status="interrupted", original_error=type(exc).__name__ + ": " + str(exc), traceback=traceback.format_exc())
    row.update(observed_input_days=observed, quoted_days=quoted, completed_steps=market.next_day_index if market is not None else 0)
    if observed:
        artifact = HERE / (case["id"] + "_u.npz")
        with artifact.open("xb") as stream:
            np.savez_compressed(stream, u=u[:observed])
        row.update(u_artifact=artifact.name, u_artifact_sha256=sha(artifact), u_array_sha256=module.array_sha(u[:observed]))
    row["total_wall_seconds"] = time.perf_counter() - started
    write_json(HERE / (case["id"] + ".json"), row)
    resource_check()
    return row


def summarize(rows, status):
    arms = {}
    for arm in ("m30", "m70"):
        selected = [row for row in rows if row["arm"] == arm and row["status"] == "completed"]
        values = {"completed_replays": len(selected), "scheduled_replays": 30}
        if len(selected) == 30:
            for kind in ("current_world_mean", "alternative_world_mean", "world_difference_alternative_minus_current"):
                values[kind] = np.asarray([row["offline"][kind] for row in selected], dtype=float).mean(axis=0)
            values["world_values"] = [{"case": row["case"], "current": row["offline"]["current_world_mean"], "alternative": row["offline"]["alternative_world_mean"], "difference": row["offline"]["world_difference_alternative_minus_current"]} for row in selected]
            values["conditional_cap_counts"] = {phase: {kind: sum(row["offline"]["conditional_cap_counts"][phase][kind] for row in selected) for kind in ("original", "conditional", "retained", "disappeared", "newly_added")} for phase in ("full", "burn", "measurement")}
        arms[arm] = values
    return {"status": status, "initial_manifest_sha256": sha(HERE / "initial_manifest.json"), "scheduled_replays": 60, "completed_replays": sum(row["status"] == "completed" for row in rows), "interrupted_replays": sum(row["status"] == "interrupted" for row in rows), "additional_seed_designs": 0, "metric_names": ["MSE", "MAE", "lag1_ACF"], "arms": arms, "world_statuses": [{key: row.get(key) for key in ("case", "status", "original_status", "original_mechanical_status", "audited_mechanical_status", "observed_input_days", "quoted_days", "completed_steps", "original_error")} for row in rows], "interpretation": SPEC["offline"]["interpretation"], "conditional_scope": SPEC["offline"]["conditional_raw"], "legacy_evidence": SPEC["legacy_evidence"]}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    args = parser.parse_args()
    parent = preflight()
    if args.check_only:
        print(json.dumps({"preflight": "PASS", "original_worlds": 60, "source_files": 52, "market_initializations": 0, "replays_started": 0}))
        return 0
    require(not any(HERE.glob("*_u.npz")) and not (HERE / "summary.json").exists() and not (HERE / "global_stop.json").exists(), "Existing evidence; no automatic retry")
    with (HERE / "run.lock").open("x", encoding="utf-8") as stream:
        stream.write(str(os.getpid()))
    rows, status = [], "running"
    try:
        require(not any(name == "abm" or name.startswith("abm.") for name in sys.modules), "ABM imported before isolation")
        module_spec = importlib.util.spec_from_file_location("qualification_replay_reference", ROOT / SPEC["source"]["parent_launcher"])
        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_spec.name] = module
        module_spec.loader.exec_module(module)
        for case, original in zip(SPEC["cases"], parent["cases"]):
            row = run_one(case, original, parent, module)
            rows.append(row)
            write_json(HERE / "summary.json", summarize(rows, "running"))
            print(json.dumps({"case": row["case"], "status": row["status"], "quoted_days": row["quoted_days"]}), flush=True)
            require(row["status"] == "completed", row["case"] + " " + str(row.get("original_error")))
        preflight()
        status = "PASS"
    except BaseException as exc:
        status = "interrupted"
        write_json(HERE / "global_stop.json", {"original_error": type(exc).__name__ + ": " + str(exc), "traceback": traceback.format_exc(), "replays_saved": len(rows), "no_retry": True})
    finally:
        write_json(HERE / "summary.json", summarize(rows, status))
        (HERE / "run.lock").unlink()
    summary = summarize(rows, status)
    lines = ["# 固定60条原路径流量重放", "", "重放/归档检查状态：" + status + "。完成" + str(summary["completed_replays"]) + "/60，中断" + str(summary["interrupted_replays"]) + "；未新增种子设计。原记录及机械失败保留。", "", "每家公司使用完整2300测量日，再等权聚合公司和30世界；公司不是独立重复。误差都使用同一u单位，未定义统计量保留null。", "", "条件raw只替换暂时冲击差，固定已经实现的P/u/depth/news/inventory；不是完整市场反事实、市场验收或默认选择。", "", "|arm|完成|current世界等权 MSE/MAE/ACF|alternative世界等权 MSE/MAE/ACF|", "|---|---:|---|---|"]
    for arm, values in summary["arms"].items():
        lines.append("|" + arm + "|" + str(values["completed_replays"]) + "|" + str(clean(values.get("current_world_mean"))) + "|" + str(clean(values.get("alternative_world_mean"))) + "|")
    lines += ["", "全部公司统计、原4次cap的条件分解、全程/预热/测量新增与消失cap数保存在各世界JSON和summary.json；唯一新增完整路径为u。", "", SPEC["offline"]["interpretation"]]
    (HERE / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    outputs = sorted(path for path in HERE.iterdir() if path.name not in {"freeze.json", "run_frozen.py", "initial_manifest.json", "manifest.json"} and path.is_file())
    write_json(HERE / "manifest.json", {"initial_manifest_sha256": sha(HERE / "initial_manifest.json"), "status": status, "outputs": {path.name: sha(path) for path in outputs}})
    resource_check()
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
