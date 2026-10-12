"""One observed-seed, serial bare-market benchmark; no additional worlds."""
from __future__ import annotations

import time

SCRIPT_STARTED = time.perf_counter()

import csv
import ctypes
from dataclasses import fields
from datetime import UTC, datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import traceback
import zipfile

THREAD_VARIABLES = ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS", "NUMEXPR_NUM_THREADS")
THREAD_ENVIRONMENT_BEFORE = {name: os.environ.get(name) for name in THREAD_VARIABLES}
for name in THREAD_VARIABLES:
    os.environ[name] = "1"
sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np

from abm.disclosure.config import MarketConfig
from abm.disclosure.harness import CrossSectionMarket
from abm.disclosure.validate import validate_market
from abm.platform_tuning import disable_power_throttling

INPUTS = {
    "reports/disclosure_market_qualification_20261011/m30_710101.json": "a4f7fa71ce92e7712470bf2caf15f7a6e2c10ed7e79f77816b3acceb776e2397",
    "reports/disclosure_market_qualification_20261011/m30_710101.npz": "b6e1513e4f704506b323bd883e4a8577456f92a773bd315dcd18e87c6b48ae19",
    "reports/disclosure_market_qualification_20261011/initial_conservation_fix/regression.json": "a47a31ced90c20a5bc15a92d881391b3fcf5037c9751d0d1533aa4574fc8509d",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def sources():
    return {path.relative_to(ROOT / "src").as_posix(): sha(path)
            for path in sorted((ROOT / "src" / "abm").rglob("*.py"))}


def write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def python_processes():
    listing = subprocess.run(["tasklist", "/FO", "CSV", "/NH"], check=True, capture_output=True, text=True)
    return [{"image": row[0], "pid": int(row[1])} for row in csv.reader(listing.stdout.splitlines())
            if len(row) > 1 and row[0].lower() in ("python.exe", "pythonw.exe", "pypy.exe", "pypy3.exe")]


def blas_runtime():
    libraries = list((Path(np.__file__).resolve().parent.parent / "numpy.libs").glob("libscipy_openblas64_*.dll"))
    require(len(libraries) == 1, "Expected the recorded Windows NumPy OpenBLAS library")
    function = ctypes.CDLL(str(libraries[0])).scipy_openblas_get_num_threads64_
    function.argtypes = []
    function.restype = ctypes.c_int
    return {"library": str(libraries[0]), "sha256": sha(libraries[0]), "num_threads": function()}


def main():
    for name in ("manifest.json", "source.zip", "result.npz", "validation.json", "result.json"):
        require(not (HERE / name).exists(), "Refusing to overwrite or resume: " + name)
    require(sys.platform == "win32", "This frozen timing launcher targets the recorded Windows host")
    require({name: sha(ROOT / name) for name in INPUTS} == INPUTS, "Frozen input changed")
    source_before = sources()
    regression = json.loads((ROOT / next(name for name in INPUTS if name.endswith("regression.json"))).read_text(encoding="utf-8"))
    expected = {name.removeprefix("src/"): digest for name, digest in regression["input_sha256"].items()
                if name.startswith("src/abm/")}
    require(regression["status"] == "PASS" and regression["source_and_tests_unchanged"], "Full regression did not pass")
    require(source_before == expected, "Current source differs from the passing full regression")
    original = json.loads((ROOT / next(name for name in INPUTS if name.endswith("710101.json"))).read_text(encoding="utf-8"))
    require(original["status"] == "completed" and original["arm"] == "m30", "Wrong reference world")
    config = MarketConfig.from_dict({**original["config"], "trading_days": 2500})
    require((config.seed, config.n_investors, config.n_firms, config.burn_in_days, config.order_flow_memory)
            == (710101, 1000, 200, 1200, .3), "Unexpected benchmark configuration")
    require(config.to_dict() == {**original["config"], "trading_days": 2500}, "Only trading_days may change")
    launcher_processes = {os.getpid(), os.getppid()}
    peers_before = python_processes()
    require(all(row["pid"] in launcher_processes for row in peers_before), "Other Python processes must finish before timing")
    blas_before = blas_runtime()
    require(blas_before["num_threads"] == 1, "NumPy BLAS is not single-threaded")
    power_tuning = disable_power_throttling()
    launcher_sha = sha(Path(__file__))
    manifest = {
        "schema_version": 1, "created_utc": datetime.now(UTC).isoformat(),
        "purpose": "single_observed_seed_bare_core_performance_only", "launcher_sha256": launcher_sha,
        "budget": {"worlds": 1, "warmup_worlds": 0, "extra_worlds": 0, "processes": 1, "seed": 710101},
        "config": config.to_dict(), "input_sha256": INPUTS, "source_hashes": source_before,
        "requirement": {"source": "original attached implementation plan, line 70",
                        "attachment_sha256": "3a7d50d95b5ba65c3cedd6849f62297eee5e05053a7a504f4baf450b4d4b16a5",
                        "n_investors": 1000, "n_firms": 200, "total_trading_days": 2500, "strict_seconds_limit": 60},
        "timing_scope": "Primary gate includes CrossSectionMarket construction plus its unchanged run(), including built-in daily histories, conservation checks and returned array copies. Imports, source/input hashing, source snapshot, environment checks, validation, reference comparison, compression and file writes are outside the gate. No Recorder, monkey patch, warmup, retry, parallel worlds or service is used.",
        "environment": {"python_version": sys.version, "executable": sys.executable, "executable_sha256": sha(Path(sys.executable)),
                        "numpy_version": np.__version__, "numpy_build": np.show_config(mode="dicts"),
                        "platform": platform.platform(), "processor": platform.processor(), "logical_cpu_count": os.cpu_count(),
                        "pid": os.getpid(), "launcher_parent_pid": os.getppid(), "python_processes_before": peers_before,
                        "thread_environment_before": THREAD_ENVIRONMENT_BEFORE,
                        "thread_environment": {name: os.environ[name] for name in THREAD_VARIABLES},
                        "blas_before": blas_before, "power_throttling_disabled": power_tuning,
                        "ABM_KEEP_POWER_THROTTLING": os.environ.get("ABM_KEEP_POWER_THROTTLING"),
                        "perf_counter_resolution": time.get_clock_info("perf_counter").resolution},
    }
    write_json(HERE / "manifest.json", manifest)
    report = {"status": "running", "market_initializations": 0, "market_runs": 0,
              "performance": {"status": "pending"}, "market_qualification": "not_established_by_this_benchmark",
              "fresh_seed_validation": False, "timings": {}, "manifest_sha256": sha(HERE / "manifest.json")}
    market = None
    try:
        with zipfile.ZipFile(HERE / "source.zip", "x", compression=zipfile.ZIP_DEFLATED) as bundle:
            for name, digest in source_before.items():
                data = (ROOT / "src" / name).read_bytes()
                require(hashlib.sha256(data).hexdigest() == digest, "Source changed while snapshotting: " + name)
                bundle.writestr(name, data)
        report["timings"]["script_preflight_wall_seconds"] = time.perf_counter() - SCRIPT_STARTED
        report["market_initializations"] = 1
        cpu_started = time.process_time()
        core_started = time.perf_counter()
        market = CrossSectionMarket(config)
        setup_finished = time.perf_counter()
        setup_cpu_finished = time.process_time()
        report["market_runs"] = 1
        result = market.run()
        run_finished = time.perf_counter()
        run_cpu_finished = time.process_time()
        report["timings"].update(setup_wall_seconds=setup_finished - core_started,
                                 simulate_wall_seconds=run_finished - setup_finished,
                                 core_wall_seconds=run_finished - core_started,
                                 setup_cpu_seconds=setup_cpu_finished - cpu_started,
                                 simulate_cpu_seconds=run_cpu_finished - setup_cpu_finished)
        validation_started = time.perf_counter()
        require(market.next_day_index == 2500, "Market did not complete all 2500 days")
        require(np.all(market.investors.investor_type == 0) and np.all(market.investors.taste == 0), "Expected bare profit maximizers")
        validation = validate_market(result, config)
        report["validation"] = validation
        report["result_fingerprint"] = result.fingerprint()
        comparisons = {}
        with np.load(ROOT / next(name for name in INPUTS if name.endswith(".npz")), allow_pickle=False) as reference:
            for name in ("prices", "intrinsic_values"):
                current = np.ascontiguousarray(getattr(result, name))
                archived = np.ascontiguousarray(reference[name][:2501])
                comparisons[name] = {"status": "PASS" if current.dtype == archived.dtype and current.shape == archived.shape
                                     and current.tobytes() == archived.tobytes() else "FAIL",
                                     "shape": list(current.shape), "dtype": str(current.dtype),
                                     "current_bytes_sha256": hashlib.sha256(current.tobytes()).hexdigest(),
                                     "reference_bytes_sha256": hashlib.sha256(archived.tobytes()).hexdigest()}
        report["reference_prefix"] = {"first_day": 0, "last_day": 2500, "arrays": comparisons,
                                      "scope": "Exact price and intrinsic-value bytes, not the old 3500-day result fingerprint or unarchived final states."}
        arrays = {field.name: np.asarray(getattr(result, field.name)) for field in fields(result)}
        report["array_sha256"] = {name: {"dtype": str(value.dtype), "shape": list(value.shape),
                                          "bytes_sha256": hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()}
                                   for name, value in arrays.items()}
        report["timings"]["validation_and_reference_wall_seconds"] = time.perf_counter() - validation_started
        write_started = time.perf_counter()
        with (HERE / "result.npz").open("xb") as stream:
            np.savez_compressed(stream, **arrays)
        write_json(HERE / "validation.json", validation)
        report["timings"]["archive_write_wall_seconds"] = time.perf_counter() - write_started
        report["artifacts"] = {name: sha(HERE / name) for name in ("manifest.json", "source.zip", "result.npz", "validation.json")}
        after_started = time.perf_counter()
        source_after = sources()
        input_after = {name: sha(ROOT / name) for name in INPUTS}
        imported = {name: Path(module.__file__).resolve() for name, module in tuple(sys.modules.items())
                    if (name == "abm" or name.startswith("abm.")) and getattr(module, "__file__", None)}
        imported_match = all(path.is_relative_to(ROOT / "src") and
                             source_before.get(path.relative_to(ROOT / "src").as_posix()) == sha(path)
                             for path in imported.values())
        peers_after, blas_after = python_processes(), blas_runtime()
        checks = {"sources_match_passing_regression_and_unchanged": source_after == source_before,
                  "original_archives_and_regression_unchanged": input_after == INPUTS,
                  "launcher_unchanged": sha(Path(__file__)) == launcher_sha,
                  "imports_match_recorded_current_source": imported_match,
                  "reference_price_and_value_bytes_match": all(row["status"] == "PASS" for row in comparisons.values()),
                  "single_blas_thread": blas_after == blas_before and blas_after["num_threads"] == 1,
                  "no_other_python_except_launcher_parent_at_final_check": all(row["pid"] in launcher_processes for row in peers_after)}
        report.update(status="complete", completed_days=market.next_day_index, source_hashes_after=source_after,
                      input_sha256_after=input_after, python_processes_after=peers_after, blas_after=blas_after,
                      imported_abm_modules={name: str(path) for name, path in imported.items()},
                      integrity={"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks})
        core_seconds = report["timings"]["core_wall_seconds"]
        report["performance"] = {"status": ("PASS" if core_seconds < 60 else "FAIL") if all(checks.values()) else "invalid",
                                 "metric": "setup_plus_simulate_wall_seconds", "seconds": core_seconds, "strict_limit": 60,
                                 "single_host_single_observed_seed_only": True}
        report["timings"]["post_run_integrity_wall_seconds"] = time.perf_counter() - after_started
    except BaseException as error:
        report.update(status="failed", error_type=type(error).__name__, error=traceback.format_exc(),
                      completed_days=market.next_day_index if market is not None else 0, resumable=False)
        write_json(HERE / "result.json", report)
        raise
    report["limitations"] = ["One previously observed seed measures this host and frozen configuration; no new-seed market qualification or policy evidence.",
                             "The 2500 days include 1200 burn-in days, leaving 1300 return observations for descriptive validation.",
                             "Mechanical, stylized, return-ACF, correlation and empirical statuses are retained independently of timing.",
                             "Process snapshots reject other Python work at two checks, allowing the benchmark and its immediate launcher parent (including the Windows venv redirector); unrelated system load is not controlled.",
                             "Final report serialization and interpreter startup are outside the measured core and archive-write intervals."]
    report["finished_utc"] = datetime.now(UTC).isoformat()
    report["timings"]["script_wall_before_final_report_seconds"] = time.perf_counter() - SCRIPT_STARTED
    write_json(HERE / "result.json", report)
    print(json.dumps({"status": report["status"], "performance": report["performance"], "integrity": report["integrity"]["status"],
                      "mechanical": report["validation"]["mechanical"]["status"], "stylized": report["validation"]["stylized"]["status"],
                      "result_fingerprint": report["result_fingerprint"]}), flush=True)
    return 0 if report["integrity"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
