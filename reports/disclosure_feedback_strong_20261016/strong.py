"""Feedback in stronger markets (research contract 20.18): the 20.17 decomposition in three phase map 1 cells.

  .venv/Scripts/python.exe reports/disclosure_feedback_strong_20261016/strong.py check
  .venv/Scripts/python.exe reports/disclosure_feedback_strong_20261016/strong.py run --workers 8
  .venv/Scripts/python.exe reports/disclosure_feedback_strong_20261016/strong.py analyze

The method is contract 20.17's, unchanged; the replay, the metric function and the five no-feedback forms are
imported from its counterfactual.py. Only the market settings differ: stage F phase map 1 cells taste_median x
initial II probability 0.1448 x 0.8, 0.1448 x 0.2 and 0.0724 x 0.8, where stage F ran only the baseline B.

(1) run, phase 1: the full model for B, I (transparency 0.6) and F (fixed fine 4x) in each cell on the
    confirmatory seeds 41001-41030 (configs/disclosure_feedback_strong_v1.json), recording B, the market cap
    and the audit draw at every decision. Each cell's B must reproduce the stage F archive's fingerprint for
    pm1_<cell>; every run's own-path replay must reproduce the run. Paths go to work/paths (local).
(2) run, phase 2: each cell's B, I and F replayed from that cell's B paths in the forms Rbase, M2, M, S, Mhom.
(3) analyze: per cell, the feedback term (full - Rbase) of I - B, F - B and I - F with paired 95% t intervals,
    its share of the full-model effect, the class fixed in contract 20.18, and the paired difference from the
    main setting's feedback term (contract 20.17, same seeds).

Writes results.json, analysis.json and tables.md next to this script; per-task records stay in work/. A failed
record is moved to work/failed/ before its task is run again, never deleted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import shutil
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path


def _no_wmi(*args, **kwargs):
    raise OSError("WMI not queried")


# The machine's WMI service hangs since 2026-10-16 and Python 3.12's platform module would wait on it forever
# when numpy is imported; its own fallback reads the environment and no identity depends on it. Single-threaded
# BLAS as the stage F runner sets it: a multithreaded OpenBLAS pool commits about 0.75 GB per process. Both are
# set before numpy loads, here and in every spawned worker (which re-runs this module's top level).
platform._wmi_query = _no_wmi
for _name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[_name] = "1"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COUNTERFACTUAL = ROOT / "reports" / "disclosure_feedback_counterfactual_20261016"

_cf_spec = importlib.util.spec_from_file_location("feedback_counterfactual", COUNTERFACTUAL / "counterfactual.py")
cf = importlib.util.module_from_spec(_cf_spec)
sys.modules["feedback_counterfactual"] = cf
_cf_spec.loader.exec_module(cf)

import numpy as np  # noqa: E402

from abm.disclosure.experiments import _inputs, freeze_spec  # noqa: E402
from abm.disclosure.metrics import compute_metrics  # noqa: E402
from abm.disclosure.validate import validate_market  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

SPEC = ROOT / "configs" / "disclosure_feedback_strong_v1.json"
EXPERIMENT_ID = "17b7394fec7624476ee622a836c320b5af97aea8db65b9ca411b0b477e2372aa"
CELLS = ("t0p1448_s0p8", "t0p1448_s0p2", "t0p0724_s0p8")
CELL_LABELS = {"t0p1448_s0p8": "taste 0.1448 × II 0.8", "t0p1448_s0p2": "taste 0.1448 × II 0.2",
               "t0p0724_s0p8": "taste 0.0724 × II 0.8", "main": "主设定 taste 0.0724 × II 0.2"}
POLICIES = ("B", "I", "F")
SEEDS = cf.SEEDS
CHECK_SEED = cf.CHECK_SEED
WORK = HERE / "work"
INTERVAL, DAYS, SWITCH_PERIOD = cf.INTERVAL, cf.DAYS, cf.SWITCH_PERIOD
PRE, WINDOW = cf.PRE, cf.WINDOW
VARIANTS, SOURCES, STEPS, METRICS = cf.VARIANTS, cf.SOURCES, cf.STEPS, cf.METRICS
CONTRASTS = {  # name: (plus, minus, metric); the first three are judged (contract 20.18), the rest descriptive
    "I_minus_B": ("I", "B", "true_change"),
    "F_minus_B": ("F", "B", "true_change"),
    "I_minus_F": ("I", "F", "true_change"),
    "I_minus_B_size_gap": ("I", "B", "size_gap"),
    "F_minus_B_terminal_inflation": ("F", "B", "terminal_inflation"),
}
JUDGED = ("I_minus_B", "F_minus_B", "I_minus_F")


def peak_commit_gb() -> float | None:
    """This process's peak commit (private bytes) so far, for sizing the worker count."""
    if sys.platform != "win32":
        return None
    import ctypes
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
            (name, ctypes.c_size_t) for name in ("PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
                                                 "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage",
                                                 "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage")]

    try:
        counters = Counters()
        counters.cb = ctypes.sizeof(Counters)
        kernel32 = ctypes.windll.kernel32
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        kernel32.K32GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
        if not kernel32.K32GetProcessMemoryInfo(kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb):
            return None
        return round(counters.PeakPagefileUsage / 2**30, 2)
    except Exception:  # a measurement, never a reason to lose a run
        return None


# -- phase 1: full-model runs ----------------------------------------------------------------

def record_task(scenario: dict, seed: int, expected_fingerprint: str | None, out: str) -> dict:
    """counterfactual.record_task with core validation, a pre-switch digest and the worker's peak commit."""
    started = time.perf_counter()
    name = scenario["name"]
    try:
        config, domain, policy = _inputs(scenario, seed)
        market = cf.PathMarket(config, domain, policy)
        result = market.run()
        fingerprint = result.fingerprint()
        size_class = np.asarray(result.market.size_class)
        audit = np.asarray(result.audit_selected).astype(bool)
        firms = {"size_class": size_class, "initial_goodness": market.initial_goodness,
                 "cost_scale": market.attributes.cost_scale.copy()}
        benefit, price = market.benefit_path, market.price_path_at_decision
        benefit[0], price[0] = benefit[1], price[1]  # day 0 has no decision
        path = Path(out) / "paths" / name / f"seed_{seed}.npz"
        path.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(path, benefit=benefit, price=price, audit=audit, **firms)

        reported = cf.archive_metrics(compute_metrics(result, config, domain))
        full = cf.window_metrics(np.asarray(result.true_goodness), np.asarray(result.inflation), np.asarray(result.actions), size_class)
        own = cf.replay(firms, domain, policy, benefit, price, audit)
        own_metrics = cf.window_metrics(own["true"], own["inflation"], own["actions"], size_class)
        validation = validate_market(result.market, config)
        caps = np.flatnonzero(np.asarray(result.market.price_cap_hits) > 0)
        actions = np.asarray(result.actions)
        pre = hashlib.sha256()
        for array in (actions[:SWITCH_PERIOD + 1], np.asarray(result.amounts)[:SWITCH_PERIOD + 1],
                      benefit[1:SWITCH_PERIOD + 1], price[1:SWITCH_PERIOD + 1]):
            pre.update(np.ascontiguousarray(array).tobytes())
        impact = np.asarray(result.impact_share)
        return {
            "status": "complete", "scenario": name, "seed": seed, "run_id": market.run_id, "fingerprint": fingerprint,
            "expected_fingerprint": expected_fingerprint,
            "fingerprint_matches_stage_f": None if expected_fingerprint is None else fingerprint == expected_fingerprint,
            "seconds": round(time.perf_counter() - started, 1), "worker_peak_commit_gb": peak_commit_gb(),
            "core_validation": {gate: validation[gate]["status"] for gate in ("mechanical", "stylized")},
            "first_price_cap_day": int(caps[0]) if caps.size else None,
            "pre_switch_sha256": pre.hexdigest(),
            "full": reported, "metric_function_max_difference": cf.max_difference(full, reported),
            "own_replay": {
                "metrics": own_metrics,
                "actions_identical": bool(np.array_equal(own["actions"], actions)),
                "amounts_max_abs": float(np.abs(own["amounts"] - result.amounts).max()),
                "true_max_abs": float(np.abs(own["true"] - result.true_goodness).max()),
                "inflation_max_abs": float(np.abs(own["inflation"] - result.inflation).max()),
                "metrics_max_difference": cf.max_difference(own_metrics, reported),
            },
            "audit_sha256": hashlib.sha256(np.ascontiguousarray(audit).tobytes()).hexdigest(),
            "benefit": {"pre_mean": float(benefit[PRE].mean()), "window_mean": float(benefit[WINDOW].mean()),
                        "snapshot_mean": float(benefit[SWITCH_PERIOD].mean()),
                        "pre_by_size": cf.by_size(benefit[PRE].mean(axis=0), size_class),
                        "window_by_size": cf.by_size(benefit[WINDOW].mean(axis=0), size_class),
                        "by_decision": [float(v) for v in benefit[1:].mean(axis=1)]},
            "price": {"snapshot_mean": float(price[SWITCH_PERIOD].mean()), "window_mean": float(price[WINDOW].mean()),
                      "window_by_size": cf.by_size(price[WINDOW].mean(axis=0), size_class)},
            "impact_share": {"day_0": float(impact[0]), "day_1200": float(impact[cf.START]), "day_3500": float(impact[DAYS])},
        }
    except Exception as error:  # kept as a failed record, never retried silently
        return {"status": "failed", "scenario": name, "seed": seed, "error_type": type(error).__name__,
                "error": str(error), "traceback": traceback.format_exc(), "seconds": round(time.perf_counter() - started, 1),
                "worker_peak_commit_gb": peak_commit_gb()}


# -- phase 2: replays from each cell's baseline paths ------------------------------------------------

def replay_task(cell: str, seed: int, scenarios: dict, out: str) -> dict:
    started = time.perf_counter()
    try:
        with np.load(Path(out) / "paths" / f"{cell}_B" / f"seed_{seed}.npz") as data:
            benefit, price, audit = data["benefit"], data["price"], data["audit"]
            firms = {key: data[key] for key in ("size_class", "initial_goodness", "cost_scale")}
        paths = cf.variant_paths(benefit, price)
        rows = {}
        for policy in POLICIES:
            name = f"{cell}_{policy}"
            config, domain, schedule = _inputs(scenarios[name], seed)
            rows[name] = {}
            for variant, (b, p) in paths.items():
                run = cf.replay(firms, domain, schedule, b, p, audit)
                rows[name][variant] = cf.window_metrics(run["true"], run["inflation"], run["actions"], firms["size_class"])
        return {"status": "complete", "setting": cell, "seed": seed, "base": f"{cell}_B", "metrics": rows,
                "seconds": round(time.perf_counter() - started, 1)}
    except Exception as error:
        return {"status": "failed", "setting": cell, "seed": seed, "error_type": type(error).__name__,
                "error": str(error), "traceback": traceback.format_exc(), "seconds": round(time.perf_counter() - started, 1)}


# -- orchestration ---------------------------------------------------------------------------------

def pending(path: Path, failed_dir: Path) -> bool:
    """True when the task still has to run; an earlier failed record is moved aside, not deleted."""
    if not path.exists():
        return True
    if json.loads(path.read_text(encoding="utf-8"))["status"] == "complete":
        return False
    failed_dir.mkdir(parents=True, exist_ok=True)
    attempt = 1
    while (failed_dir / f"{path.stem}__attempt{attempt}.json").exists():
        attempt += 1
    shutil.move(str(path), failed_dir / f"{path.stem}__attempt{attempt}.json")
    return True


def execute(seeds: list[int], cells: list[str], policies: tuple[str, ...], archive: Path, out: Path, workers: int,
            *, frozen_id: str | None = EXPERIMENT_ID) -> None:
    frozen = freeze_spec(SPEC)
    if frozen_id is not None and frozen["experiment_id"] != frozen_id:
        raise RuntimeError(f"experiment_id {frozen['experiment_id']} differs from the frozen {frozen_id}")
    stage_f = freeze_spec(cf.SPEC)
    if stage_f["experiment_id"] != cf.EXPERIMENT_ID:
        raise RuntimeError("the stage F identity no longer reproduces; source or environment changed")
    _, records = cf.archive_records(archive)
    scenarios = {row["name"]: row for row in frozen["scenarios"]}
    cf.log(f"experiment_id {frozen['experiment_id']}; stage F {stage_f['experiment_id'][:12]} reproduces; archive "
           f"{archive.name}; {len(seeds)} seeds, cells {cells}, policies {policies}, {workers} workers")
    record_dir, replay_dir, failed_dir = out / "records", out / "replays", out / "failed"
    jobs = [(f"{cell}_{policy}", seed) for cell in cells for policy in policies for seed in seeds
            if pending(record_dir / f"{cell}_{policy}__{seed}.json", failed_dir)]
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers, initializer=disable_power_throttling) as pool:
        futures = []
        for name, seed in jobs:
            cell, policy = name.rsplit("_", 1)
            expected = records[(f"pm1_{cell}", seed)]["result_fingerprint"] if policy == "B" else None
            futures.append(pool.submit(record_task, scenarios[name], seed, expected, str(out)))
        for count, future in enumerate(as_completed(futures), 1):
            row = future.result()
            cf.write_json(record_dir / f"{row['scenario']}__{row['seed']}.json", row)
            if row["status"] == "complete":
                match = row["fingerprint_matches_stage_f"]
                note = (f"fingerprint {'n/a' if match is None else 'ok' if match else 'MISMATCH'}, own replay actions "
                        f"{'identical' if row['own_replay']['actions_identical'] else 'DIFFER'}, core "
                        f"{row['core_validation']['mechanical']}/{row['core_validation']['stylized']}")
            else:
                note = f"FAILED {row['error_type']}: {row['error']}"
            cf.log(f"record {count}/{len(jobs)} {row['scenario']} {row['seed']} {row['seconds']} s, "
                   f"worker peak {row['worker_peak_commit_gb']} GB; {note}")
        cf.log(f"phase 1 done in {time.perf_counter() - started:.0f} s")
        ready = [(cell, seed) for cell in cells for seed in seeds
                 if all((record_dir / f"{cell}_{policy}__{seed}.json").exists() for policy in POLICIES)]
        jobs = [(cell, seed) for cell, seed in ready if pending(replay_dir / f"{cell}__{seed}.json", failed_dir)]
        futures = [pool.submit(replay_task, cell, seed, scenarios, str(out)) for cell, seed in jobs]
        for count, future in enumerate(as_completed(futures), 1):
            row = future.result()
            cf.write_json(replay_dir / f"{row['setting']}__{row['seed']}.json", row)
            note = "ok" if row["status"] == "complete" else f"FAILED {row['error_type']}: {row['error']}"
            cf.log(f"replay {count}/{len(jobs)} {row['setting']} {row['seed']} {row['seconds']} s; {note}")
    cf.log(f"all done in {time.perf_counter() - started:.0f} s")


def check() -> None:
    """Pipeline check on development seed 33001 (one cell, all three policies): identities, time and memory only."""
    out = HERE / "work_check"
    cell = CELLS[0]
    execute([CHECK_SEED], [cell], POLICIES, cf.DEV_ARCHIVE, out, workers=3, frozen_id=None)
    rows = {}
    for policy in POLICIES:
        row = json.loads((out / "records" / f"{cell}_{policy}__{CHECK_SEED}.json").read_text(encoding="utf-8"))
        if row["status"] != "complete":
            raise SystemExit(f"{cell}_{policy} failed: {row['error']}")
        rows[policy] = row
        own = row["own_replay"]
        cf.log(f"{cell}_{policy}: fingerprint vs development archive {row['fingerprint_matches_stage_f']}; metric "
               f"function max diff {row['metric_function_max_difference']:.1e}; own replay actions identical "
               f"{own['actions_identical']}, amounts {own['amounts_max_abs']:.1e}, true {own['true_max_abs']:.1e}, "
               f"inflation {own['inflation_max_abs']:.1e}; core {row['core_validation']}; {row['seconds']} s; "
               f"worker peak commit {row['worker_peak_commit_gb']} GB")
    cf.log(f"pre-switch digests identical across policies: {len({r['pre_switch_sha256'] for r in rows.values()}) == 1}; "
           f"audit draws identical: {len({r['audit_sha256'] for r in rows.values()}) == 1}")
    row = json.loads((out / "replays" / f"{cell}__{CHECK_SEED}.json").read_text(encoding="utf-8"))
    cf.log(f"replay task {row['status']} in {row['seconds']} s; Rbase on B equals the full B run: "
           f"{cf.max_difference(row['metrics'][f'{cell}_B']['Rbase'], rows['B']['full']) == 0}")


# -- analysis --------------------------------------------------------------------------------------------

def classify(feedback: dict, effect: dict) -> dict:
    """Contract 20.18: the 20.17 reading, plus a class for feedback clearly larger than in the main setting."""
    if effect["ci_low"] <= 0 <= effect["ci_high"]:
        share = None
    else:
        share = feedback["mean"] / effect["mean"]
    if feedback["ci_low"] <= 0 <= feedback["ci_high"] or (share is not None and abs(share) < 0.1):
        label = "none"
    elif share is None:
        label = "share undefined"
    elif abs(share) < 0.2:
        label = "about a tenth"
    else:
        label = "clearly larger"
    return {"share": share, "class": label}


def collect(out: Path) -> dict:
    """values[source][scenario][metric] -> per-seed list in SEEDS order, plus the checks."""
    _, archive = cf.archive_records(cf.ARCHIVE)
    names = [f"{cell}_{policy}" for cell in CELLS for policy in POLICIES]
    values = {source: {name: {metric: [] for metric in METRICS} for name in names} for source in SOURCES}
    checks = {"recorded_runs": 0, "failed": [], "b_fingerprints_matching_stage_f": 0, "b_runs": 0,
              "b_metrics_vs_archive_max": 0.0, "own_actions_identical": 0,
              "own_max_abs": {"amounts": 0.0, "true": 0.0, "inflation": 0.0, "metrics": 0.0},
              "metric_function_max": 0.0, "audit_draws_shared_per_seed": True, "pre_switch_identical_per_cell": True,
              "rbase_on_baseline_equals_full_max": 0.0, "core_validation_failures": {}, "worker_peak_commit_gb_max": 0.0,
              "seconds_median": None}
    records, seconds = {}, []
    for seed in SEEDS:
        audits = set()
        for name in names:
            row = json.loads((out / "records" / f"{name}__{seed}.json").read_text(encoding="utf-8"))
            if row["status"] != "complete":
                checks["failed"].append(f"record {name} {seed}: {row['error']}")
                continue
            records[(name, seed)] = row
            checks["recorded_runs"] += 1
            seconds.append(row["seconds"])
            checks["worker_peak_commit_gb_max"] = max(checks["worker_peak_commit_gb_max"], row["worker_peak_commit_gb"] or 0.0)
            if name.endswith("_B"):
                checks["b_runs"] += 1
                checks["b_fingerprints_matching_stage_f"] += bool(row["fingerprint_matches_stage_f"])
                checks["b_metrics_vs_archive_max"] = max(checks["b_metrics_vs_archive_max"], cf.max_difference(
                    row["full"], cf.archive_metrics(archive[(f"pm1_{name[:-2]}", seed)]["metrics"])))
            own = row["own_replay"]
            checks["own_actions_identical"] += own["actions_identical"]
            for key in ("amounts", "true", "inflation"):
                checks["own_max_abs"][key] = max(checks["own_max_abs"][key], own[f"{key}_max_abs"])
            checks["own_max_abs"]["metrics"] = max(checks["own_max_abs"]["metrics"], own["metrics_max_difference"])
            checks["metric_function_max"] = max(checks["metric_function_max"], row["metric_function_max_difference"])
            audits.add(row["audit_sha256"])
            if any(status != "PASS" for status in row["core_validation"].values()):
                checks["core_validation_failures"].setdefault(name, []).append([seed, row["first_price_cap_day"]])
        checks["audit_draws_shared_per_seed"] &= len(audits) == 1
        for cell in CELLS:
            digests = {records[(f"{cell}_{p}", seed)]["pre_switch_sha256"] for p in POLICIES if (f"{cell}_{p}", seed) in records}
            checks["pre_switch_identical_per_cell"] &= len(digests) == 1
    replays = {}
    for cell in CELLS:
        for seed in SEEDS:
            row = json.loads((out / "replays" / f"{cell}__{seed}.json").read_text(encoding="utf-8"))
            if row["status"] != "complete":
                checks["failed"].append(f"replay {cell} {seed}: {row['error']}")
                continue
            replays[(cell, seed)] = row
            checks["rbase_on_baseline_equals_full_max"] = max(
                checks["rbase_on_baseline_equals_full_max"],
                cf.max_difference(row["metrics"][f"{cell}_B"]["Rbase"], records[(f"{cell}_B", seed)]["full"]))
    if checks["failed"]:
        raise RuntimeError(f"incomplete tasks: {checks['failed']}")
    checks["seconds_median"] = float(np.median(seconds))
    for cell in CELLS:
        for policy in POLICIES:
            name = f"{cell}_{policy}"
            for seed in SEEDS:
                row, forms = records[(name, seed)], replays[(cell, seed)]["metrics"][name]
                for metric in METRICS:
                    values["full"][name][metric].append(row["full"][metric])
                    values["own"][name][metric].append(row["own_replay"]["metrics"][metric])
                    for variant in VARIANTS:
                        values[variant][name][metric].append(forms[variant][metric])
    return {"values": values, "checks": checks, "records": records}


def main_setting() -> dict:
    """Per-seed values of the main setting (contract 20.17), cells renamed main_B/I/F."""
    stored = json.loads((COUNTERFACTUAL / "results.json").read_text(encoding="utf-8"))
    if stored["seeds"] != SEEDS:
        raise RuntimeError("the 20.17 results use other seeds")
    return {source: {f"main_{p}": stored["values"][source][p] for p in POLICIES} for source in SOURCES}


def contrast(values: dict, source: str, cell: str, plus: str, minus: str, metric: str) -> np.ndarray:
    return np.asarray(values[source][f"{cell}_{plus}"][metric]) - np.asarray(values[source][f"{cell}_{minus}"][metric])


def channels(records: dict) -> dict:
    """How each cell's B, market caps and impact-investor share respond to I and F (cf. 20.17 section 5)."""
    out = {}
    for cell in CELLS:
        base = [records[(f"{cell}_B", seed)] for seed in SEEDS]
        row = {"B_levels": {
            "pre_mean": cf.interval([r["benefit"]["pre_mean"] for r in base]),
            "snapshot_mean": cf.interval([r["benefit"]["snapshot_mean"] for r in base]),
            "window_mean": cf.interval([r["benefit"]["window_mean"] for r in base]),
            "window_by_size": [cf.interval(c) for c in zip(*(r["benefit"]["window_by_size"] for r in base))],
            "by_decision_mean": [float(v) for v in np.mean([r["benefit"]["by_decision"] for r in base], axis=0)],
            "impact_share": {day: cf.interval([r["impact_share"][day] for r in base]) for day in ("day_0", "day_1200", "day_3500")},
        }}
        for policy in ("I", "F"):
            own = [records[(f"{cell}_{policy}", seed)] for seed in SEEDS]
            row[policy] = {
                "window_b_relative": cf.interval([o["benefit"]["window_mean"] / b["benefit"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "window_b_relative_by_size": [cf.interval(c) for c in zip(*(
                    [x / y - 1 for x, y in zip(o["benefit"]["window_by_size"], b["benefit"]["window_by_size"])] for o, b in zip(own, base)))],
                "window_price_relative": cf.interval([o["price"]["window_mean"] / b["price"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "impact_share_day_3500_difference": cf.interval([o["impact_share"]["day_3500"] - b["impact_share"]["day_3500"] for o, b in zip(own, base)]),
            }
        out[cell] = row
    return out


def analyze(out: Path) -> None:
    gathered = collect(out)
    values, checks, records = gathered["values"], gathered["checks"], gathered["records"]
    main = main_setting()
    for source in SOURCES:
        values[source].update(main[source])
    failing = {cell: sorted({seed for p in POLICIES for seed, _ in checks["core_validation_failures"].get(f"{cell}_{p}", [])})
               for cell in CELLS}
    rows = {}
    for cell in ("main", *CELLS):
        rows[cell] = {}
        keep = np.array([seed not in failing.get(cell, []) for seed in SEEDS])
        for name, (plus, minus, metric) in CONTRASTS.items():
            series = {source: contrast(values, source, cell, plus, minus, metric) for source in SOURCES}
            row = {"forms": {source: cf.interval(s) for source, s in series.items()},
                   "steps": {step: cf.interval(series[a] - series[b]) for step, a, b in STEPS}}
            feedback = series["full"] - series["Rbase"]
            row.update(classify(row["steps"]["feedback"], row["forms"]["full"]))
            if cell != "main":
                main_feedback = contrast(values, "full", "main", plus, minus, metric) - contrast(values, "Rbase", "main", plus, minus, metric)
                row["feedback_minus_main"] = cf.interval(feedback - main_feedback)
                row["full_minus_main"] = cf.interval(series["full"] - contrast(values, "full", "main", plus, minus, metric))
                if not keep.all():
                    row["core_validation_pass_only"] = {
                        "n": int(keep.sum()), "full": cf.interval(series["full"][keep]), "feedback": cf.interval(feedback[keep]),
                        **classify(cf.interval(feedback[keep]), cf.interval(series["full"][keep]))}
            rows[cell][name] = row
        ordering = {}
        for source in ("full", "Rbase", "M", "S"):
            i, f, b = (np.asarray(values[source][f"{cell}_{p}"]["true_change"]) for p in ("I", "F", "B"))
            ordering[source] = {"mean": bool(i.mean() > f.mean() > b.mean()), "seeds": int(((i > f) & (f > b)).sum())}
        rows[cell]["ordering_I_F_B"] = ordering
    clearly = [(cell, name) for cell in CELLS for name in JUDGED if rows[cell][name]["class"] == "clearly larger"]
    ordering_changed = [cell for cell in CELLS if rows[cell]["ordering_I_F_B"]["full"]["mean"] != rows[cell]["ordering_I_F_B"]["Rbase"]["mean"]]
    levels = {name: {metric: {source: cf.interval(values[source][name][metric]) for source in ("full", "Rbase")}
                     for metric in ("true_change", "wash", "wash_large", "wash_small", "terminal_inflation", "size_gap")}
              for name in [f"{c}_{p}" for c in ("main", *CELLS) for p in POLICIES]}
    analysis = {
        "schema_version": 1, "generated_by": "reports/disclosure_feedback_strong_20261016/strong.py",
        "contract": "docs/disclosure_research_contract.md 20.18", "experiment_id": EXPERIMENT_ID,
        "main_setting_source": "reports/disclosure_feedback_counterfactual_20261016/results.json (contract 20.17)",
        "seeds": f"{SEEDS[0]}-{SEEDS[-1]}", "window": [cf.START, DAYS], "cells": CELL_LABELS,
        "interval": "paired 95% t interval over seeds", "steps": {step: f"{a} - {b}" for step, a, b in STEPS},
        "classes": {"none": "feedback interval contains 0 or |share| < 0.1 (20.17 reading)",
                    "about a tenth": "0.1 <= |share| < 0.2", "clearly larger": "|share| >= 0.2",
                    "share undefined": "full-model effect interval contains 0; absolute feedback reported"},
        "checks": checks, "core_validation_failing_seeds": failing, "contrasts": rows, "levels": levels,
        "verdict": {"clearly_larger": clearly, "ordering_changed_by_feedback": ordering_changed,
                    "reading": ("feedback clearly larger than in the main setting in " + ", ".join(f"{c} {n}" for c, n in clearly))
                    if clearly else "in no tested cell is feedback clearly larger than in the main setting (|share| < 0.2 everywhere)"},
        "feedback_channels": channels(records),
        "main_feedback_channels": {key: json.loads((COUNTERFACTUAL / "analysis.json").read_text(encoding="utf-8"))["feedback_channels"][key]
                                   for key in ("I", "F", "B_levels")},
    }
    cf.write_json(HERE / "analysis.json", analysis)
    cf.write_json(HERE / "results.json", {"schema_version": 1, "seeds": SEEDS, "metrics": list(METRICS),
                                          "note": "values[form][scenario][metric] = per-seed list in seed order; main_* from contract 20.17",
                                          "values": values})
    write_tables(analysis)
    cf.log("wrote analysis.json, results.json and tables.md")


def fmt(row: dict | None, digits: int = 3) -> str:
    return cf.fmt(row, digits)


def share(value: float | None) -> str:
    return "—" if value is None else f"{value:+.0%}"


def write_tables(analysis: dict) -> None:
    c = analysis["checks"]
    lines = ["# 更强市场中的反馈：完整表格", "", "由 strong.py analyze 生成。种子 41001–41030，配对 95% t 区间，未作多重校正。"
             "主设定（taste 0.0724 × II 0.2）的逐种子值取自契约 20.17 的 results.json。", "",
             "## 检查", "",
             f"- 完整运行 {c['recorded_runs']} 个；各格点 B 的指纹与阶段 F 档案 pm1_<格点> 一致 {c['b_fingerprints_matching_stage_f']}/{c['b_runs']}，"
             f"指标与档案最大差 {c['b_metrics_vs_archive_max']:.1e}。",
             f"- 自身路径重放行动逐期相同 {c['own_actions_identical']} 个；幅度、真实水平、虚报最大绝对差 {c['own_max_abs']['amounts']:.1e}、"
             f"{c['own_max_abs']['true']:.1e}、{c['own_max_abs']['inflation']:.1e}，指标最大差 {c['own_max_abs']['metrics']:.1e}；"
             f"指标函数与 compute_metrics 最大差 {c['metric_function_max']:.1e}。",
             f"- 同一种子 9 个场景的核查抽样相同：{c['audit_draws_shared_per_seed']}；同一格点三种政策切换前逐位相同：{c['pre_switch_identical_per_cell']}；"
             f"B 上 Rbase 与完整模型最大差 {c['rbase_on_baseline_equals_full_max']:.1e}。",
             f"- 单个运行耗时中位数 {c['seconds_median']:.0f} 秒；worker 峰值提交内存最大 {c['worker_peak_commit_gb_max']} GB。",
             f"- 核心验证失败（[种子, 首次价格截断日]）：{json.dumps(c['core_validation_failures'])}。", "",
             "## 反馈项（完整 − Rbase）与占比", "",
             "| 设定 | 对比 | 完整模型 | Rbase | 反馈 | 占比 | 分类 | 反馈 − 主设定反馈 |", "|---|---|---|---|---|---:|---|---|"]
    for cell, rows in analysis["contrasts"].items():
        for name in CONTRASTS:
            row = rows[name]
            lines.append(f"| {analysis['cells'][cell]} | {name} | {fmt(row['forms']['full'])} | {fmt(row['forms']['Rbase'])} | "
                         f"{fmt(row['steps']['feedback'])} | {share(row['share'])} | {row['class']} | {fmt(row.get('feedback_minus_main'))} |")
    lines += ["", "## 剔除核心验证失败种子之后", "", "| 设定 | 对比 | n | 完整模型 | 反馈 | 占比 | 分类 |", "|---|---|---:|---|---|---:|---|"]
    for cell, rows in analysis["contrasts"].items():
        for name in CONTRASTS:
            row = rows[name].get("core_validation_pass_only")
            if row:
                lines.append(f"| {analysis['cells'][cell]} | {name} | {row['n']} | {fmt(row['full'])} | {fmt(row['feedback'])} | "
                             f"{share(row['share'])} | {row['class']} |")
    lines += ["", "## 分解（配对）", "",
              "| 设定 | 对比 | 反馈 full−Rbase | 阶段内路径 Rbase−M2 | 切换前水平 M2−M | 快照水平 M−S | 合计 full−S | B 异质性 M−Mhom |",
              "|---|---|---|---|---|---|---|---|"]
    for cell, rows in analysis["contrasts"].items():
        for name in CONTRASTS:
            lines.append(f"| {analysis['cells'][cell]} | {name} | " + " | ".join(fmt(rows[name]["steps"][s]) for s, _, _ in STEPS) + " |")
    lines += ["", "## 完整模型效应相对主设定（配对）", "", "| 设定 | 对比 | 完整 − 主设定完整 |", "|---|---|---|"]
    for cell in CELLS:
        for name in CONTRASTS:
            lines.append(f"| {analysis['cells'][cell]} | {name} | {fmt(analysis['contrasts'][cell][name]['full_minus_main'])} |")
    lines += ["", "## 排序 I > F > B（均值 / 逐种子计数）", "", "| 设定 | full | Rbase | M | S |", "|---|---|---|---|---|"]
    for cell, rows in analysis["contrasts"].items():
        o = rows["ordering_I_F_B"]
        lines.append(f"| {analysis['cells'][cell]} | " + " | ".join(f"{o[s]['mean']} / {o[s]['seeds']}" for s in ("full", "Rbase", "M", "S")) + " |")
    lines += ["", "## 判定", "", f"- {analysis['verdict']['reading']}",
              f"- 反馈改变均值排序的格点：{analysis['verdict']['ordering_changed_by_feedback'] or '无'}", "",
              "## 场景水平（完整 / Rbase）", "", "```json", json.dumps(analysis["levels"], ensure_ascii=False, indent=1), "```", "",
              "## 反馈通道（描述）", "", "```json", json.dumps(analysis["feedback_channels"], ensure_ascii=False, indent=1), "```", "",
              "主设定（契约 20.17）：", "", "```json", json.dumps(analysis["main_feedback_channels"], ensure_ascii=False, indent=1), "```", ""]
    (HERE / "tables.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("check", "run", "analyze"))
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    disable_power_throttling()
    if args.command == "check":
        check()
    elif args.command == "run":
        execute(SEEDS, list(CELLS), POLICIES, cf.ARCHIVE, WORK, args.workers)
    else:
        analyze(WORK)


if __name__ == "__main__":
    main()
