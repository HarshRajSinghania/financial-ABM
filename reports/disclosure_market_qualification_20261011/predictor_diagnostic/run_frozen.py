"""Run sixteen frozen deterministic book-formula traces; never create a market."""
from __future__ import annotations

import argparse
from dataclasses import replace
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import traceback

for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
sys.dont_write_bytecode = True

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = json.loads((HERE / "freeze.json").read_text(encoding="utf-8"))


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def preflight():
    initial = json.loads((HERE / "initial_manifest.json").read_text(encoding="utf-8"))
    for name, digest in initial["files"].items():
        require(sha(HERE / name) == digest, "Frozen diagnostic changed: " + name)
    provenance = SPEC["source"]
    require(sha(ROOT / provenance["parent_freeze"]) == provenance["parent_freeze_sha256"], "Parent freeze changed")
    require(sha(ROOT / provenance["archive"]) == provenance["archive_sha256"], "Archived source changed")
    parent = json.loads((ROOT / provenance["parent_freeze"]).read_text(encoding="utf-8"))
    source = ROOT / provenance["isolated_directory"]
    expected = parent["source"]["source_hashes"]
    require({path.relative_to(source).as_posix() for path in source.rglob("*.py")} == set(expected), "Isolated source members differ")
    for name, digest in expected.items():
        require(sha(source / name) == digest, "Isolated source changed: " + name)
    require(expected["abm/disclosure/market.py"] == provenance["market_sha256"], "Book identity differs")
    require(expected["abm/disclosure/config.py"] == provenance["config_sha256"], "Config identity differs")
    for name, value in SPEC["parameters"].items():
        require(parent["base_config"][name] == value, "Inherited parameter differs: " + name)
    require(platform.python_version() == SPEC["runtime"]["python_version"] and np.__version__ == SPEC["runtime"]["numpy_version"], "Runtime differs")
    require(len(SPEC["memories"]) * len(SPEC["inputs"]) * len(SPEC["predictors"]) == SPEC["budget"]["array_traces"] == 16, "Trace budget differs")
    return parent, source, expected


def make_input(definition):
    count = SPEC["budget"]["days_per_trace"]
    arrays = []
    for key in ("flow_segments", "depth_segments"):
        values = np.full(count, np.nan)
        covered = np.zeros(count, dtype=bool)
        for start, end, value in definition[key]:
            require(1 <= start <= end <= count and not covered[start - 1:end].any(), "Invalid input segments")
            values[start - 1:end] = value
            covered[start - 1:end] = True
        require(covered.all() and np.isfinite(values).all(), "Incomplete input")
        arrays.append(values)
    require(np.isin(arrays[1], [1.0, SPEC["parameters"]["liquidity_fraction"]]).all(), "Unsupported controlled depth")
    return arrays


def close(actual, expected, message):
    require(np.allclose(actual, expected, atol=SPEC["checks"]["absolute_tolerance"], rtol=SPEC["checks"]["relative_tolerance"]), message)


def run_trace(base, book_class, memory, predictor, definition):
    case = memory["id"] + "_" + definition["id"] + "_" + predictor
    u, depth = make_input(definition)
    cfg = replace(base, n_firms=1, order_flow_memory=memory["value"])
    p, decay, rho = cfg.permanent_impact_fraction, cfg.transient_impact_decay, cfg.order_flow_memory
    state = definition["initial_flow_predictor"]
    if predictor == "impact_ema":
        state /= depth[0]
    transient = definition["initial_transient"]
    book = book_class.initialize(cfg, 1.0) if predictor == "impact_ema" else None
    if book is not None:
        book.expected_flow_impact[0], book.transient_impact[0] = state, transient
    names = ("surprise", "predictor_before", "predictor_after", "transient_before", "transient_after", "raw", "clipped")
    if book is not None:
        names += ("source_raw", "source_clipped", "source_depth", "source_predictor_after", "source_transient_after")
    paths = {name: np.full(u.size, np.nan) for name in names}
    observed, calls, error = 0, 0, None
    try:
        for t in range(u.size):
            paths["predictor_before"][t], paths["transient_before"][t] = state, transient
            surprise = u[t] / depth[t] - state if predictor == "impact_ema" else (u[t] - state) / depth[t]
            state = rho * state + (1 - rho) * (u[t] / depth[t] if predictor == "impact_ema" else u[t])
            previous = transient
            transient = decay * transient + (1 - p) * surprise
            raw = p * u[t] + transient - previous
            clipped = float(np.clip(raw, -cfg.max_log_return, cfg.max_log_return))
            paths["surprise"][t], paths["predictor_after"][t], paths["transient_after"][t] = surprise, state, transient
            paths["raw"][t], paths["clipped"][t] = raw, clipped
            observed = t + 1
            require(np.isfinite([surprise, state, transient, raw, clipped]).all(), case + " nonfinite formula day " + str(observed))
            if book is not None:
                book.depth_fraction[0], book.reference_variance[0] = depth[t], 1.0
                book.variance[0] = 0.0 if depth[t] == 1.0 else (cfg.liquidity_stress_threshold + 1.0) ** 2
                before = float(book.transient_impact[0])
                monetary = np.array([u[t] * cfg.liquidity_fraction / cfg.price_impact])
                moves, capped = book.price_moves(monetary, np.ones(1), np.zeros(1), np.zeros(1))
                calls += 1
                seen_flow = cfg.price_impact * monetary[0] / cfg.liquidity_fraction
                source_raw = p * seen_flow + book.transient_impact[0] - before
                source_values = [source_raw, moves[0], book.depth_fraction[0], book.expected_flow_impact[0], book.transient_impact[0]]
                for name, value in zip(names[-5:], source_values):
                    paths[name][t] = value
                close(source_values, [raw, clipped, depth[t], state, transient], case + " source mismatch day " + str(observed))
                require(bool(capped[0]) == (clipped != raw), case + " cap flag mismatch day " + str(observed))
        close(np.cumsum(paths["raw"]), p * np.cumsum(u) + paths["transient_after"] - definition["initial_transient"], case + " cumulative identity")
        if definition["id"].startswith("pulse_"):
            close(paths["raw"][:2], [u[0] * (p + (1 - p) / depth[0]), u[0] * (1 - p) / depth[0] * (decay + rho - 2)], case + " pulse identity")
        if definition["id"] == "zero_depth_steps":
            require(all(np.count_nonzero(paths[name]) == 0 for name in ("surprise", "raw", "clipped", "transient_after")), case + " zero-flow control")
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
    saved = {name: values[:observed] for name, values in paths.items()}
    saved.update(u=u[:observed], depth=depth[:observed])
    saved["cumulative_raw"], saved["cumulative_clipped"] = np.cumsum(saved["raw"]), np.cumsum(saved["clipped"])
    output = HERE / (case + ".npz")
    np.savez_compressed(output, **saved)
    entry = {"case": case, "memory": rho, "input": definition["id"], "predictor": predictor, "status": "completed" if error is None else "interrupted", "observed_days": observed, "book_quotes": calls, "error": error, "path_sha256": sha(output), "input_sha256": hashlib.sha256(u.tobytes() + depth.tobytes()).hexdigest(), "metrics": None}
    if error is None:
        pulse = definition["id"].startswith("pulse_")
        entry["metrics"] = {"raw_first": float(paths["raw"][0]), "raw_second": float(paths["raw"][1]), "clipped_first": float(paths["clipped"][0]), "clipped_second": float(paths["clipped"][1]), "raw_next_over_first_for_pulse": float(paths["raw"][1] / paths["raw"][0]) if pulse else None, "clipped_next_over_first_for_pulse": float(paths["clipped"][1] / paths["clipped"][0]) if pulse else None, "raw_first_per_pulse": float(paths["raw"][0] / u[0]) if pulse else None, "raw_second_per_pulse": float(paths["raw"][1] / u[0]) if pulse else None, "maximum_absolute_raw": float(np.abs(paths["raw"]).max()), "maximum_absolute_clipped": float(np.abs(paths["clipped"]).max()), "cap_count": int(np.count_nonzero(paths["raw"] != paths["clipped"])), "cumulative_raw": float(saved["cumulative_raw"][-1]), "cumulative_clipped": float(saved["cumulative_clipped"][-1]), "permanent_cumulative": float(p * u.sum()), "final_transient": float(transient)}
    return entry, saved


def compare_pair(current, alternative, definition):
    require(np.array_equal(current["u"], alternative["u"]) and np.array_equal(current["depth"], alternative["depth"]), "Paired inputs differ")
    if definition["id"].startswith("pulse_") or definition["id"] == "zero_depth_steps":
        for name in ("surprise", "transient_after", "raw", "clipped"):
            close(current[name], alternative[name], definition["id"] + " fixed-depth/zero equivalence")
    residual = current["surprise"] - alternative["surprise"]
    close(residual, alternative["predictor_before"] / current["depth"] - current["predictor_before"], "Depth residual identity")
    steps = np.flatnonzero(np.diff(current["depth"]) != 0) + 1
    if definition["id"] == "constant_depth_steps":
        for t in steps:
            close(residual[t], current["u"][t] * (1 / current["depth"][t] - 1 / current["depth"][t - 1]), "First depth-step residual")
    return {"status": "PASS", "input": definition["id"], "maximum_absolute_depth_surprise_residual": float(np.abs(residual).max()), "maximum_absolute_raw_difference": float(np.abs(current["raw"] - alternative["raw"]).max()), "maximum_absolute_clipped_difference": float(np.abs(current["clipped"] - alternative["clipped"]).max()), "final_cumulative_raw_difference": float(current["cumulative_raw"][-1] - alternative["cumulative_raw"][-1]), "depth_steps": [{"day": int(t + 1), "depth_before": float(current["depth"][t - 1]), "depth_after": float(current["depth"][t]), "current_surprise": float(current["surprise"][t]), "alternative_surprise": float(alternative["surprise"][t]), "depth_surprise_residual": float(residual[t])} for t in steps]}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    args = parser.parse_args()
    parent, source, expected = preflight()
    if args.check_only:
        print(json.dumps({"preflight": "PASS", "array_traces_initialized": 0, "books_initialized": 0, "market_worlds": 0, "source_members_verified": len(expected)}))
        return 0
    require(not any(HERE.glob("*.npz")) and not (HERE / "results.json").exists() and not (HERE / "global_stop.json").exists(), "Existing run evidence; no retry permitted")
    with (HERE / "run.lock").open("x", encoding="utf-8") as lock:
        lock.write(str(os.getpid()))
    result = {"status": "running", "scope": SPEC["purpose"], "initial_manifest_sha256": sha(HERE / "initial_manifest.json"), "cases": [], "pairs": [], "market_worlds": 0, "rng_api_calls": 0, "limits": SPEC["limits"]}
    try:
        require(not any(name == "abm" or name.startswith("abm.") for name in sys.modules), "ABM imported before isolation")
        sys.path.insert(0, str(source))
        from abm.disclosure.config import MarketConfig
        from abm.disclosure.market import CrossSectionBook
        for name, module in list(sys.modules.items()):
            if (name == "abm" or name.startswith("abm.")) and getattr(module, "__file__", None):
                path = Path(module.__file__).resolve()
                relative = path.relative_to(source.resolve()).as_posix()
                require(relative in expected and sha(path) == expected[relative], "Nonfrozen ABM import: " + name)
        base = MarketConfig.from_dict(parent["base_config"])
        for memory in SPEC["memories"]:
            for definition in SPEC["inputs"]:
                paired = []
                for predictor in SPEC["predictors"]:
                    entry, paths = run_trace(base, CrossSectionBook, memory, predictor, definition)
                    result["cases"].append(entry)
                    write_json(HERE / "results.json", result)
                    require(entry["error"] is None, entry["case"] + " " + str(entry["error"]))
                    paired.append(paths)
                pair = compare_pair(*paired, definition)
                pair["memory"] = memory["value"]
                result["pairs"].append(pair)
        preflight()
        require(len(result["cases"]) == 16 and len(result["pairs"]) == 8, "Final budget differs")
        result["status"] = "PASS"
    except Exception as exc:
        result["status"] = "interrupted"
        result["original_error"] = type(exc).__name__ + ": " + str(exc)
        write_json(HERE / "global_stop.json", {"error": result["original_error"], "traceback": traceback.format_exc(), "traces_saved": len(result["cases"]), "no_retry": True})
    finally:
        write_json(HERE / "results.json", result)
        (HERE / "run.lock").unlink()
    lines = ["# 固定预测器公式诊断", "", "公式检查状态：" + result["status"] + "。已存路径" + str(len(result["cases"])) + "/16；市场运行0、RNG调用0。", "", "外生强制深度/方差隔离了预测器公式；未调用record_returns，不是动态深度市场反事实，也不提供ACF、实证校准或市场稳定性验收。", "", "|输入|memory|预测器|状态|首日raw|次日raw|累计raw|cap|", "|---|---:|---|---|---:|---:|---:|---:|"]
    for entry in result["cases"]:
        metrics = entry["metrics"]
        values = [metrics[key] for key in ("raw_first", "raw_second", "cumulative_raw", "cap_count")] if metrics else [None] * 4
        lines.append("|" + "|".join(str(value) for value in [entry["input"], entry["memory"], entry["predictor"], entry["status"], *values]) + "|")
    lines += ["", "全部raw/clipped、预测器及暂时状态和累计路径见16条预声明NPZ；中断时只保存已观察前缀。配对JSON包含深度独生残差及两个深度切换日。无自动赢家、默认推广、重试或追加。"]
    (HERE / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    outputs = sorted(path for path in HERE.iterdir() if path.suffix == ".npz" or path.name in {"results.json", "report.md", "global_stop.json"})
    write_json(HERE / "manifest.json", {"initial_manifest_sha256": sha(HERE / "initial_manifest.json"), "outputs": {path.name: sha(path) for path in outputs}, "status": result["status"], "extra_traces": 0})
    print(json.dumps({"status": result["status"], "traces_saved": len(result["cases"]), "market_worlds": 0}))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
