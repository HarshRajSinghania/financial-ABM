"""Feedback channels (research contract 20.19): investor evolution versus price and demand response.

  .venv/Scripts/python.exe reports/disclosure_feedback_channels_20261017/channels.py check
  .venv/Scripts/python.exe reports/disclosure_feedback_channels_20261017/channels.py run --workers 16
  .venv/Scripts/python.exe reports/disclosure_feedback_channels_20261017/channels.py analyze

Contract 20.18 found the feedback term (full model - Rbase) of F - B at +0.049 SD (31% of the effect) and of I - F at
-0.073 (-18%) in phase map 1 cell taste_median 0.1448 x initial II probability 0.2. The feedback has two channels:
the impact-investor share responds to the policy (investor evolution), and, with any given population, prices and
demand respond to the firms' changed reports. A third form between the full model and Rbase separates them:

  frozen  the full model under the policy, but after every imitation step the investor types (and so the tastes)
          are set to those of the same seed's baseline run B at that step. Prices, wealth, holdings and demand
          respond to the policy; the composition of the investor population cannot.

full - frozen is the evolution channel (including its interaction with the price response), frozen - Rbase the
price and demand channel at the baseline population; the two add up to the feedback term. Only
DisclosureMarket._imitate assigns investor types, its learning generator is used by nothing else after
initialization, and demand reads the types only through taste = latent taste x [impact investor]; the subclasses
below therefore freeze evolution without touching src/abm. Under B the frozen run must reproduce the B run bit for
bit (identity check).

(1) run, phase 1: the cell's B on seeds 41001-41030 with the investor types recorded after every imitation step
    (configs/disclosure_feedback_strong_v1.json, contract 20.18's spec). Each must reproduce the stage F archive's
    fingerprint for pm1_<cell>.
(2) run, phase 2: the frozen form of B, I (transparency 0.6) and F (fixed fine 4x) on the same seeds, each with its
    seed's recorded B types. Frozen B must reproduce the B fingerprint.
(3) analyze: per contrast, the full, frozen and Rbase values (full and Rbase per seed from contract 20.18's
    results.json, same seeds), the two channels with paired 95% t intervals, their shares and the classes fixed in
    contract 20.19.

Writes results.json, analysis.json and tables.md next to this script; per-task records and type paths stay in work/
(local, regenerable). A failed record is moved to work/failed/ before its task is run again, never deleted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path


def _no_wmi(*args, **kwargs):
    raise OSError("WMI not queried")


# As in contract 20.18's strong.py: the machine's WMI service hangs and Python 3.12's platform module would wait on it
# when numpy is imported; single-threaded BLAS keeps each worker's commit small. Both are set before numpy loads,
# here and in every spawned worker (which re-runs this module's top level).
platform._wmi_query = _no_wmi
for _name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[_name] = "1"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STRONG = ROOT / "reports" / "disclosure_feedback_strong_20261016"

_strong_spec = importlib.util.spec_from_file_location("feedback_strong", STRONG / "strong.py")
strong = importlib.util.module_from_spec(_strong_spec)
sys.modules["feedback_strong"] = strong
_strong_spec.loader.exec_module(strong)
cf = strong.cf

import numpy as np  # noqa: E402

from abm.disclosure.experiments import _inputs, freeze_spec  # noqa: E402
from abm.disclosure.investors import IMPACT_INVESTOR, PROFIT_MAXIMIZER  # noqa: E402
from abm.disclosure.metrics import compute_metrics  # noqa: E402
from abm.disclosure.validate import validate_market  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

CELL = "t0p1448_s0p2"
CELL_LABEL = "taste 0.1448 × II 0.2"
POLICIES = ("B", "I", "F")
SEEDS, CHECK_SEED = cf.SEEDS, cf.CHECK_SEED
DAYS, START, SWITCH_PERIOD, PRE, WINDOW = cf.DAYS, cf.START, cf.SWITCH_PERIOD, cf.PRE, cf.WINDOW
METRICS = cf.METRICS
WORK = HERE / "work"
FORMS = ("full", "frozen", "Rbase")
CHANNELS = (("feedback", "full", "Rbase"), ("evolution", "full", "frozen"), ("price_demand", "frozen", "Rbase"))
CONTRASTS = {  # name: (plus, minus, metric); the first two are judged (contract 20.19), the rest descriptive
    "F_minus_B": ("F", "B", "true_change"),
    "I_minus_F": ("I", "F", "true_change"),
    "I_minus_B": ("I", "B", "true_change"),
    "F_minus_B_terminal_inflation": ("F", "B", "terminal_inflation"),
    "I_minus_B_size_gap": ("I", "B", "size_gap"),
}
JUDGED = ("F_minus_B", "I_minus_F")


# -- markets ------------------------------------------------------------------------------------------------

class TypeRecordingMarket(cf.PathMarket):
    """PathMarket that also records the investor types after every imitation step (row 0: initial). Reads only."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        steps = self.config.trading_days // self.config.imitation_interval + 1
        self.type_path = np.full((steps, self.config.n_investors), -1, dtype=np.int8)
        self.type_path[0] = self.investors.investor_type
        self._day = 0

    def _post_trade(self, day: int) -> None:
        self._day = day
        super()._post_trade(day)

    def _imitate(self) -> None:
        super()._imitate()
        self.type_path[self._day // self.config.imitation_interval] = self.investors.investor_type


class FrozenEvolutionMarket(TypeRecordingMarket):
    """The full market, with the investor types after every imitation step replaced by a given run's.

    The run's own imitation step still runs first, from the given run's types, so the learning generator advances
    exactly as in the given run; its result is then overwritten. ``own_differs[k]`` counts the investors whose type
    the run's own step k would have set differently, and ``own_net[k]`` the net number it would have made impact
    investors: the pressure on the population that freezing removes.
    """

    def __init__(self, *args, type_path, **kwargs):
        super().__init__(*args, **kwargs)
        if type_path.shape != self.type_path.shape or not np.array_equal(type_path[0], self.type_path[0]):
            raise ValueError("the given type path does not belong to this seed and population")
        self.frozen_types = type_path
        self.own_differs = np.zeros(type_path.shape[0], dtype=np.int64)
        self.own_net = np.zeros(type_path.shape[0], dtype=np.int64)

    def _imitate(self) -> None:
        super()._imitate()
        step = self._day // self.config.imitation_interval
        own, frozen = self.type_path[step], self.frozen_types[step]
        self.own_differs[step] = int((own != frozen).sum())
        self.own_net[step] = int((own == IMPACT_INVESTOR).sum()) - int((frozen == IMPACT_INVESTOR).sum())
        is_impact = frozen == IMPACT_INVESTOR
        self.investors.investor_type[:] = np.where(is_impact, IMPACT_INVESTOR, PROFIT_MAXIMIZER)
        self.investors.taste[:] = self.latent_taste * is_impact
        self.type_path[step] = frozen


def sha256(array) -> str:
    return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()


# -- runs ---------------------------------------------------------------------------------------------------

def run_task(form: str, scenario: dict, seed: int, expected_fingerprint: str | None, out: str) -> dict:
    """One full-model run: ``record`` (B, types recorded) or ``frozen`` (types from the seed's recorded B run)."""
    started = time.perf_counter()
    name = scenario["name"]
    try:
        config, domain, policy = _inputs(scenario, seed)
        if form == "record":
            market = TypeRecordingMarket(config, domain, policy)
        else:
            with np.load(Path(out) / "types" / f"seed_{seed}.npz") as data:
                market = FrozenEvolutionMarket(config, domain, policy, type_path=data["type_path"])
        result = market.run()
        fingerprint = result.fingerprint()
        steps = np.arange(market.type_path.shape[0]) * config.imitation_interval
        if (market.type_path[(steps > 0) & (steps <= config.trading_days)] < 0).any():
            raise RuntimeError("an imitation step was not recorded")
        size_class = np.asarray(result.market.size_class)
        audit = np.asarray(result.audit_selected).astype(bool)
        firms = {"size_class": size_class, "initial_goodness": market.initial_goodness,
                 "cost_scale": market.attributes.cost_scale.copy()}
        benefit, price = market.benefit_path, market.price_path_at_decision
        benefit[0], price[0] = benefit[1], price[1]  # day 0 has no decision
        path = Path(out) / "paths" / f"{form}_{name}" / f"seed_{seed}.npz"
        path.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(path, benefit=benefit, price=price, audit=audit, **firms)
        if form == "record":
            types = Path(out) / "types" / f"seed_{seed}.npz"
            types.parent.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(types, type_path=market.type_path)

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
        impact, impact_wealth = np.asarray(result.impact_share), np.asarray(result.impact_wealth_share)
        row = {
            "status": "complete", "form": form, "scenario": name, "seed": seed, "run_id": market.run_id,
            "fingerprint": fingerprint, "expected_fingerprint": expected_fingerprint,
            "fingerprint_matches": None if expected_fingerprint is None else fingerprint == expected_fingerprint,
            "seconds": round(time.perf_counter() - started, 1), "worker_peak_commit_gb": strong.peak_commit_gb(),
            "core_validation": {gate: validation[gate]["status"] for gate in ("mechanical", "stylized")},
            "first_price_cap_day": int(caps[0]) if caps.size else None,
            "pre_switch_sha256": pre.hexdigest(), "audit_sha256": sha256(audit),
            "latent_taste_sha256": sha256(market.latent_taste), "impact_share_sha256": sha256(impact),
            "type_path_sha256": sha256(market.type_path),
            "full": reported, "metric_function_max_difference": cf.max_difference(full, reported),
            "own_replay": {
                "metrics": own_metrics,
                "actions_identical": bool(np.array_equal(own["actions"], actions)),
                "amounts_max_abs": float(np.abs(own["amounts"] - result.amounts).max()),
                "true_max_abs": float(np.abs(own["true"] - result.true_goodness).max()),
                "inflation_max_abs": float(np.abs(own["inflation"] - result.inflation).max()),
                "metrics_max_difference": cf.max_difference(own_metrics, reported),
            },
            "benefit": {"pre_mean": float(benefit[PRE].mean()), "window_mean": float(benefit[WINDOW].mean()),
                        "window_by_size": cf.by_size(benefit[WINDOW].mean(axis=0), size_class),
                        "by_decision": [float(v) for v in benefit[1:].mean(axis=1)]},
            "price": {"window_mean": float(price[WINDOW].mean()),
                      "window_by_size": cf.by_size(price[WINDOW].mean(axis=0), size_class)},
            "impact_share": {"day_0": float(impact[0]), "day_1200": float(impact[START]), "day_3500": float(impact[DAYS])},
            "impact_wealth_share": {"day_1200": float(impact_wealth[START]), "day_3500": float(impact_wealth[DAYS])},
        }
        if form == "frozen":
            post = (steps > START) & (steps <= config.trading_days)
            row["own_step"] = {
                "n_investors": config.n_investors,
                "pre_switch_differs_total": int(market.own_differs[steps <= START].sum()),
                "post_switch_differs_total": int(market.own_differs[post].sum()),
                "post_switch_net_total": int(market.own_net[post].sum()),
                "post_switch_steps": int(post.sum()),
                "differs_by_step": [int(v) for v in market.own_differs],
                "net_by_step": [int(v) for v in market.own_net],
            }
        return row
    except Exception as error:  # kept as a failed record, never retried silently
        return {"status": "failed", "form": form, "scenario": name, "seed": seed, "error_type": type(error).__name__,
                "error": str(error), "traceback": traceback.format_exc(), "seconds": round(time.perf_counter() - started, 1),
                "worker_peak_commit_gb": strong.peak_commit_gb()}


# -- orchestration ------------------------------------------------------------------------------------------

def record_path(out: Path, form: str, policy: str, seed: int) -> Path:
    return out / "records" / f"{form}_{CELL}_{policy}__{seed}.json"


def complete(path: Path) -> dict | None:
    if not path.exists():
        return None
    row = json.loads(path.read_text(encoding="utf-8"))
    return row if row["status"] == "complete" else None


def execute(seeds: list[int], archive: Path, out: Path, workers: int) -> None:
    frozen_spec = freeze_spec(strong.SPEC)
    if frozen_spec["experiment_id"] != strong.EXPERIMENT_ID:
        raise RuntimeError(f"experiment_id {frozen_spec['experiment_id']} differs from contract 20.18's {strong.EXPERIMENT_ID}")
    stage_f = freeze_spec(cf.SPEC)
    if stage_f["experiment_id"] != cf.EXPERIMENT_ID:
        raise RuntimeError("the stage F identity no longer reproduces; source or environment changed")
    _, records = cf.archive_records(archive)
    scenarios = {row["name"]: row for row in frozen_spec["scenarios"]}
    cf.log(f"experiment_id {frozen_spec['experiment_id']}; stage F {stage_f['experiment_id'][:12]} reproduces; archive "
           f"{archive.name}; cell {CELL}; {len(seeds)} seeds; {workers} workers")
    failed_dir = out / "failed"
    started = time.perf_counter()

    def report(row: dict, count: int, total: int) -> None:
        cf.write_json(record_path(out, row["form"], row["scenario"].rsplit("_", 1)[1], row["seed"]), row)
        if row["status"] == "complete":
            match = row["fingerprint_matches"]
            note = (f"fingerprint {'n/a' if match is None else 'ok' if match else 'MISMATCH'}, own replay actions "
                    f"{'identical' if row['own_replay']['actions_identical'] else 'DIFFER'}, core "
                    f"{row['core_validation']['mechanical']}/{row['core_validation']['stylized']}")
            if row["form"] == "frozen":
                note += f", own step differs after switch {row['own_step']['post_switch_differs_total']}"
        else:
            note = f"FAILED {row['error_type']}: {row['error']}"
        cf.log(f"{row['form']} {count}/{total} {row['scenario']} {row['seed']} {row['seconds']} s, "
               f"worker peak {row['worker_peak_commit_gb']} GB; {note}")

    with ProcessPoolExecutor(max_workers=workers, initializer=disable_power_throttling) as pool:
        jobs = [seed for seed in seeds if strong.pending(record_path(out, "record", "B", seed), failed_dir)]
        futures = [pool.submit(run_task, "record", scenarios[f"{CELL}_B"], seed,
                               records[(f"pm1_{CELL}", seed)]["result_fingerprint"], str(out)) for seed in jobs]
        for count, future in enumerate(as_completed(futures), 1):
            report(future.result(), count, len(futures))
        cf.log(f"phase 1 done in {time.perf_counter() - started:.0f} s")
        futures = []
        for seed in seeds:
            base = complete(record_path(out, "record", "B", seed))
            if base is None:
                continue
            for policy in POLICIES:
                if strong.pending(record_path(out, "frozen", policy, seed), failed_dir):
                    expected = base["fingerprint"] if policy == "B" else None
                    futures.append(pool.submit(run_task, "frozen", scenarios[f"{CELL}_{policy}"], seed, expected, str(out)))
        for count, future in enumerate(as_completed(futures), 1):
            report(future.result(), count, len(futures))
    cf.log(f"all done in {time.perf_counter() - started:.0f} s")


def check() -> None:
    """Pipeline check on development seed 33001: identities, time and memory only, no effect estimates."""
    out = HERE / "work_check"
    execute([CHECK_SEED], cf.DEV_ARCHIVE, out, workers=3)
    base = complete(record_path(out, "record", "B", CHECK_SEED))
    if base is None:
        raise SystemExit("the B record failed")
    cf.log(f"record B: fingerprint vs development archive pm1_{CELL} {base['fingerprint_matches']}; own replay actions "
           f"identical {base['own_replay']['actions_identical']}; core {base['core_validation']}; {base['seconds']} s; "
           f"worker peak commit {base['worker_peak_commit_gb']} GB")
    for policy in POLICIES:
        row = complete(record_path(out, "frozen", policy, CHECK_SEED))
        if row is None:
            raise SystemExit(f"frozen {policy} failed")
        own, step = row["own_replay"], row["own_step"]
        cf.log(f"frozen {policy}: impact-share path equals B's {row['impact_share_sha256'] == base['impact_share_sha256']}; "
               f"latent tastes equal {row['latent_taste_sha256'] == base['latent_taste_sha256']}; pre-switch equals B's "
               f"{row['pre_switch_sha256'] == base['pre_switch_sha256']}; audits equal {row['audit_sha256'] == base['audit_sha256']}; "
               f"own step differs before / after switch {step['pre_switch_differs_total']} / {step['post_switch_differs_total']}; "
               f"own replay actions identical {own['actions_identical']}, amounts {own['amounts_max_abs']:.1e}, true "
               f"{own['true_max_abs']:.1e}, inflation {own['inflation_max_abs']:.1e}; core {row['core_validation']}; "
               f"{row['seconds']} s; worker peak commit {row['worker_peak_commit_gb']} GB")
    frozen_b = complete(record_path(out, "frozen", "B", CHECK_SEED))
    cf.log(f"identity: frozen B fingerprint equals the B run's {frozen_b['fingerprint'] == base['fingerprint']}; "
           f"metrics max difference {cf.max_difference(frozen_b['full'], base['full']):.1e}")


# -- analysis -----------------------------------------------------------------------------------------------

def collect(out: Path) -> dict:
    stored = json.loads((STRONG / "results.json").read_text(encoding="utf-8"))
    if stored["seeds"] != SEEDS:
        raise RuntimeError("the 20.18 results use other seeds")
    values = {"full": {p: stored["values"]["full"][f"{CELL}_{p}"] for p in POLICIES},
              "Rbase": {p: stored["values"]["Rbase"][f"{CELL}_{p}"] for p in POLICIES},
              "frozen": {p: {metric: [] for metric in METRICS} for p in POLICIES}}
    checks = {"failed": [], "record_runs": 0, "record_fingerprints_matching_stage_f": 0, "record_vs_20_18_full_max": 0.0,
              "frozen_runs": 0, "frozen_B_fingerprints_equal_B": 0, "frozen_B_vs_B_metrics_max": 0.0,
              "frozen_B_own_step_differs_total": 0, "impact_share_paths_equal_B": 0, "latent_tastes_equal_B": 0,
              "pre_switch_equal_B": 0, "audits_equal_B": 0, "pre_switch_own_step_differs_total": 0,
              "own_actions_identical": 0, "own_max_abs": {"amounts": 0.0, "true": 0.0, "inflation": 0.0, "metrics": 0.0},
              "metric_function_max": 0.0, "core_validation_failures": {}, "seconds_median": None,
              "worker_peak_commit_gb_max": 0.0}
    rows, seconds = {}, []
    for seed in SEEDS:
        base = complete(record_path(out, "record", "B", seed))
        if base is None:
            checks["failed"].append(f"record B {seed}")
            continue
        rows[("record", "B", seed)] = base
        checks["record_runs"] += 1
        checks["record_fingerprints_matching_stage_f"] += bool(base["fingerprint_matches"])
        checks["record_vs_20_18_full_max"] = max(checks["record_vs_20_18_full_max"], max(
            abs(base["full"][m] - values["full"]["B"][m][SEEDS.index(seed)]) for m in METRICS))
        for policy in POLICIES:
            row = complete(record_path(out, "frozen", policy, seed))
            if row is None:
                checks["failed"].append(f"frozen {policy} {seed}")
                continue
            rows[("frozen", policy, seed)] = row
            checks["frozen_runs"] += 1
            checks["impact_share_paths_equal_B"] += row["impact_share_sha256"] == base["impact_share_sha256"]
            checks["latent_tastes_equal_B"] += row["latent_taste_sha256"] == base["latent_taste_sha256"]
            checks["pre_switch_equal_B"] += row["pre_switch_sha256"] == base["pre_switch_sha256"]
            checks["audits_equal_B"] += row["audit_sha256"] == base["audit_sha256"]
            checks["pre_switch_own_step_differs_total"] += row["own_step"]["pre_switch_differs_total"]
            if policy == "B":
                checks["frozen_B_fingerprints_equal_B"] += row["fingerprint"] == base["fingerprint"]
                checks["frozen_B_vs_B_metrics_max"] = max(checks["frozen_B_vs_B_metrics_max"], cf.max_difference(row["full"], base["full"]))
                checks["frozen_B_own_step_differs_total"] += row["own_step"]["post_switch_differs_total"]
    for (form, policy, seed), row in rows.items():
        seconds.append(row["seconds"])
        checks["worker_peak_commit_gb_max"] = max(checks["worker_peak_commit_gb_max"], row["worker_peak_commit_gb"] or 0.0)
        own = row["own_replay"]
        checks["own_actions_identical"] += own["actions_identical"]
        for key in ("amounts", "true", "inflation"):
            checks["own_max_abs"][key] = max(checks["own_max_abs"][key], own[f"{key}_max_abs"])
        checks["own_max_abs"]["metrics"] = max(checks["own_max_abs"]["metrics"], own["metrics_max_difference"])
        checks["metric_function_max"] = max(checks["metric_function_max"], row["metric_function_max_difference"])
        if any(status != "PASS" for status in row["core_validation"].values()):
            checks["core_validation_failures"].setdefault(f"{form}_{policy}", []).append([seed, row["first_price_cap_day"]])
    if checks["failed"]:
        raise RuntimeError(f"incomplete tasks: {checks['failed']}")
    require_identities(checks, "record_vs_20_18_full_max")
    checks["seconds_median"] = float(np.median(seconds))
    for policy in POLICIES:
        for seed in SEEDS:
            for metric in METRICS:
                values["frozen"][policy][metric].append(rows[("frozen", policy, seed)]["full"][metric])
    return {"values": values, "checks": checks, "rows": rows}


def identity_failures(checks: dict, record_vs_full: str) -> list[str]:
    """The identities the channel arithmetic rests on (contracts 20.19 and 20.20), each required exactly.

    Without them frozen - Rbase and full - frozen are not the two channels: a record B that misses the archive's
    fingerprint or the stored full-model B, a frozen B that is not B, or a frozen run whose type path, tastes, audits or
    pre-switch path differ from B's mixes other changes into the split. Core validation (price caps) is not an identity
    here; contracts 20.19 and 20.20 keep those runs and report a robustness check without them.
    """
    n = len(SEEDS)
    counts = {"record_runs": n, "record_fingerprints_matching_stage_f": n, "frozen_runs": n * len(POLICIES),
              "frozen_B_fingerprints_equal_B": n, "impact_share_paths_equal_B": n * len(POLICIES),
              "latent_tastes_equal_B": n * len(POLICIES), "pre_switch_equal_B": n * len(POLICIES),
              "audits_equal_B": n * len(POLICIES), "own_actions_identical": n * (1 + len(POLICIES)),
              "frozen_B_own_step_differs_total": 0, "pre_switch_own_step_differs_total": 0}
    zeros = {record_vs_full: checks[record_vs_full], "frozen_B_vs_B_metrics_max": checks["frozen_B_vs_B_metrics_max"],
             "metric_function_max": checks["metric_function_max"],
             **{f"own_max_abs.{key}": value for key, value in checks["own_max_abs"].items()}}
    return ([f"{key} = {checks[key]}, expected {want}" for key, want in counts.items() if checks[key] != want]
            + [f"{key} = {value:.3e}, expected 0" for key, value in zeros.items() if value != 0.0])


def require_identities(checks: dict, record_vs_full: str) -> None:
    """Stop before any channel, class or attribution is computed when an identity fails."""
    failures = identity_failures(checks, record_vs_full)
    if failures:
        raise RuntimeError("identity checks failed, no channels computed:\n  " + "\n  ".join(failures))


def excludes_zero(row: dict) -> bool:
    return not row["ci_low"] <= 0 <= row["ci_high"]


def attribute(evolution: dict, price_demand: dict) -> dict:
    """Contract 20.19: which channel carries the feedback term."""
    e, d = excludes_zero(evolution), excludes_zero(price_demand)
    share = None
    if not e and not d:
        label = "neither identifiable"
    elif e and not d:
        label = "evolution"
    elif d and not e:
        label = "price and demand"
    elif np.sign(evolution["mean"]) != np.sign(price_demand["mean"]):
        label = "opposite signs"
    else:
        share = evolution["mean"] / (evolution["mean"] + price_demand["mean"])
        label = "mainly evolution" if share >= 2 / 3 else "mainly price and demand" if share <= 1 / 3 else "both"
    return {"label": label, "evolution_share_of_feedback": share}


READING = {
    "evolution": "supports 20.18's reading: the feedback runs through investor evolution",
    "mainly evolution": "supports 20.18's reading: the feedback runs mainly through investor evolution",
    "both": "partly supports 20.18's reading: both channels contribute substantially",
    "mainly price and demand": "does not support 20.18's reading: the feedback runs mainly through prices and demand, not investor evolution",
    "price and demand": "does not support 20.18's reading: the feedback runs through prices and demand; investor evolution has no identifiable part",
    "opposite signs": "the two channels act in opposite directions",
    "neither identifiable": "neither channel is identifiable on its own",
}


def contrast_rows(values: dict, keep: np.ndarray | None = None) -> dict:
    out = {}
    for name, (plus, minus, metric) in CONTRASTS.items():
        series = {form: np.asarray(values[form][plus][metric]) - np.asarray(values[form][minus][metric]) for form in FORMS}
        if keep is not None:
            series = {form: s[keep] for form, s in series.items()}
        parts = {channel: series[a] - series[b] for channel, a, b in CHANNELS}
        row = {"forms": {form: cf.interval(s) for form, s in series.items()},
               "channels": {channel: cf.interval(s) for channel, s in parts.items()},
               "sum_identity_max_abs": float(np.abs(parts["feedback"] - parts["evolution"] - parts["price_demand"]).max())}
        row["classes"] = {channel: strong.classify(row["channels"][channel], row["forms"]["full"]) for channel, _, _ in CHANNELS}
        row["attribution"] = attribute(row["channels"]["evolution"], row["channels"]["price_demand"])
        feedback = row["channels"]["feedback"]
        row["evolution_over_feedback"] = row["channels"]["evolution"]["mean"] / feedback["mean"] if excludes_zero(feedback) else None
        out[name] = row
    return out


def channel_description(rows: dict) -> dict:
    """How B, market caps and the impact-investor population respond to I and F, full model versus frozen."""
    full_rows = {}
    for policy in POLICIES:
        for seed in SEEDS:
            path = STRONG / "work" / "records" / f"{CELL}_{policy}__{seed}.json"
            full_rows[(policy, seed)] = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    have_full = all(row is not None for row in full_rows.values())
    out = {"full_model_source": "contract 20.18 records (local work/)" if have_full else "unavailable"}
    base = [rows[("record", "B", seed)] for seed in SEEDS]
    for policy in ("I", "F"):
        frozen = [rows[("frozen", policy, seed)] for seed in SEEDS]
        forms = {"frozen": frozen, **({"full": [full_rows[(policy, seed)] for seed in SEEDS]} if have_full else {})}
        row = {}
        for form, own in forms.items():
            row[form] = {
                "window_b_relative": cf.interval([o["benefit"]["window_mean"] / b["benefit"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "window_b_relative_by_size": [cf.interval(c) for c in zip(*(
                    [x / y - 1 for x, y in zip(o["benefit"]["window_by_size"], b["benefit"]["window_by_size"])] for o, b in zip(own, base)))],
                "window_price_relative": cf.interval([o["price"]["window_mean"] / b["price"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "impact_share_day_3500_difference": cf.interval([o["impact_share"]["day_3500"] - b["impact_share"]["day_3500"] for o, b in zip(own, base)]),
            }
        row["frozen"]["impact_wealth_share_day_3500_difference"] = cf.interval(
            [o["impact_wealth_share"]["day_3500"] - b["impact_wealth_share"]["day_3500"] for o, b in zip(frozen, base)])
        n_investors = 1000
        row["frozen"]["own_step"] = {
            "post_switch_differs_per_step": cf.interval([o["own_step"]["post_switch_differs_total"] / o["own_step"]["post_switch_steps"] for o in frozen]),
            "post_switch_net_share_per_step": cf.interval([o["own_step"]["post_switch_net_total"] / o["own_step"]["post_switch_steps"] / n_investors for o in frozen]),
        }
        out[policy] = row
    out["B_levels"] = {"window_mean": cf.interval([b["benefit"]["window_mean"] for b in base]),
                       "impact_share": {day: cf.interval([b["impact_share"][day] for b in base]) for day in ("day_0", "day_1200", "day_3500")}}
    return out


def analyze(out: Path) -> None:
    gathered = collect(out)
    values, checks, rows = gathered["values"], gathered["checks"], gathered["rows"]
    contrasts = contrast_rows(values)
    earlier = json.loads((STRONG / "analysis.json").read_text(encoding="utf-8"))["core_validation_failing_seeds"][CELL]
    failing = sorted(set(earlier) | {seed for runs in checks["core_validation_failures"].values() for seed, _ in runs})
    keep = np.array([seed not in failing for seed in SEEDS])
    robust = contrast_rows(values, keep) if not keep.all() else None
    ordering = {}
    for form in FORMS:
        i, f, b = (np.asarray(values[form][p]["true_change"]) for p in ("I", "F", "B"))
        ordering[form] = {"mean": bool(i.mean() > f.mean() > b.mean()), "seeds": int(((i > f) & (f > b)).sum())}
    levels = {p: {metric: {form: cf.interval(values[form][p][metric]) for form in FORMS}
                  for metric in ("true_change", "wash", "terminal_inflation", "size_gap")} for p in POLICIES}
    analysis = {
        "schema_version": 1, "generated_by": "reports/disclosure_feedback_channels_20261017/channels.py",
        "contract": "docs/disclosure_research_contract.md 20.19", "experiment_id": strong.EXPERIMENT_ID,
        "cell": CELL, "cell_label": CELL_LABEL, "seeds": f"{SEEDS[0]}-{SEEDS[-1]}", "window": [START, DAYS],
        "forms": {"full": "full model (contract 20.18 results.json)",
                  "frozen": "full model with the investor types after every imitation step set to the seed's B run's",
                  "Rbase": "firm-side replay with the B run's B, market caps and audits (contract 20.18 results.json)"},
        "channels": {channel: f"{a} - {b}" for channel, a, b in CHANNELS},
        "interval": "paired 95% t interval over seeds",
        "classes": {"channel classes": "contract 20.18 thresholds on the channel's share of the full-model effect",
                    "attribution": "contract 20.19: by which channel intervals exclude 0 and the evolution share of the feedback (2/3, 1/3)"},
        "checks": checks, "core_validation_failing_seeds": failing, "contrasts": contrasts,
        "core_validation_pass_only": {"n": int(keep.sum()), "contrasts": robust} if robust else None,
        "ordering_I_F_B": ordering, "levels": levels,
        "verdict": {name: {"attribution": contrasts[name]["attribution"]["label"],
                           "reading": READING[contrasts[name]["attribution"]["label"]]} for name in JUDGED},
        "feedback_channels": channel_description(rows),
    }
    cf.write_json(HERE / "analysis.json", analysis)
    cf.write_json(HERE / "results.json", {"schema_version": 1, "seeds": SEEDS, "metrics": list(METRICS),
                                          "note": "values[form][policy][metric] = per-seed list in seed order; full and Rbase from contract 20.18",
                                          "values": values})
    write_tables(analysis)
    cf.log("wrote analysis.json, results.json and tables.md")


def share(value: float | None) -> str:
    return "—" if value is None else f"{value:+.0%}"


def write_tables(analysis: dict) -> None:
    c, fmt = analysis["checks"], cf.fmt
    lines = ["# 反馈的两个通道：完整表格", "", f"由 channels.py analyze 生成。格点 {CELL_LABEL}，种子 41001–41030，配对 95% t 区间，未作多重校正。"
             "完整模型与 Rbase 的逐种子值取自契约 20.18 的 results.json；冻结形式为本分析的运行。", "",
             "## 检查", "",
             f"- 记录运行（B）{c['record_runs']} 个，指纹与阶段 F 档案 pm1_{CELL} 一致 {c['record_fingerprints_matching_stage_f']} 个；"
             f"指标与 20.18 完整模型的最大差 {c['record_vs_20_18_full_max']:.1e}。",
             f"- 冻结运行 {c['frozen_runs']} 个；冻结 B 的指纹等于 B {c['frozen_B_fingerprints_equal_B']}/30，指标最大差 {c['frozen_B_vs_B_metrics_max']:.1e}，"
             f"冻结 B 中本运行自身模仿与基准不同的累计人次 {c['frozen_B_own_step_differs_total']}。",
             f"- 影响力投资者占比逐日路径等于 B：{c['impact_share_paths_equal_B']}/{c['frozen_runs']}；潜在偏好相同 {c['latent_tastes_equal_B']}；"
             f"切换前逐位相同 {c['pre_switch_equal_B']}；核查抽样相同 {c['audits_equal_B']}；切换前自身模仿与基准不同的累计人次 {c['pre_switch_own_step_differs_total']}。",
             f"- 自身路径重放行动逐期相同 {c['own_actions_identical']} 个；幅度、真实水平、虚报最大绝对差 {c['own_max_abs']['amounts']:.1e}、"
             f"{c['own_max_abs']['true']:.1e}、{c['own_max_abs']['inflation']:.1e}，指标最大差 {c['own_max_abs']['metrics']:.1e}；"
             f"指标函数与 compute_metrics 最大差 {c['metric_function_max']:.1e}。",
             f"- 单个运行耗时中位数 {c['seconds_median']:.0f} 秒；worker 峰值提交内存最大 {c['worker_peak_commit_gb_max']} GB。",
             f"- 核心验证失败（[种子, 首次价格截断日]）：{json.dumps(c['core_validation_failures'])}；剔除用的种子 {analysis['core_validation_failing_seeds']}。", "",
             "## 各形式的值", "", "| 对比 | 完整模型 | 冻结演化 | Rbase |", "|---|---|---|---|"]
    for name, row in analysis["contrasts"].items():
        lines.append(f"| {name} | " + " | ".join(fmt(row["forms"][form]) for form in FORMS) + " |")
    lines += ["", "## 两个通道", "",
              "| 对比 | 反馈 完整−Rbase | 演化 完整−冻结 | 价格与需求 冻结−Rbase | 演化占效应 | 价格需求占效应 | 演化 / 反馈 | 归属 |",
              "|---|---|---|---|---:|---:|---:|---|"]
    for name, row in analysis["contrasts"].items():
        ch, cl = row["channels"], row["classes"]
        lines.append(f"| {name} | {fmt(ch['feedback'])} | {fmt(ch['evolution'])} | {fmt(ch['price_demand'])} | "
                     f"{share(cl['evolution']['share'])} ({cl['evolution']['class']}) | {share(cl['price_demand']['share'])} "
                     f"({cl['price_demand']['class']}) | {share(row['evolution_over_feedback'])} | {row['attribution']['label']} |")
    robust = analysis["core_validation_pass_only"]
    if robust:
        lines += ["", f"## 剔除核心验证失败种子之后（n = {robust['n']}）", "",
                  "| 对比 | 反馈 | 演化 | 价格与需求 | 演化 / 反馈 | 归属 |", "|---|---|---|---|---:|---|"]
        for name, row in robust["contrasts"].items():
            ch = row["channels"]
            lines.append(f"| {name} | {fmt(ch['feedback'])} | {fmt(ch['evolution'])} | {fmt(ch['price_demand'])} | "
                         f"{share(row['evolution_over_feedback'])} | {row['attribution']['label']} |")
    lines += ["", "## 排序 I > F > B（均值 / 逐种子计数）", "", "| 完整 | 冻结 | Rbase |", "|---|---|---|",
              "| " + " | ".join(f"{analysis['ordering_I_F_B'][f]['mean']} / {analysis['ordering_I_F_B'][f]['seeds']}" for f in FORMS) + " |",
              "", "## 判定", ""]
    for name, verdict in analysis["verdict"].items():
        lines.append(f"- {name}：{verdict['attribution']}；{verdict['reading']}")
    lines += ["", "## 场景水平", "", "```json", json.dumps(analysis["levels"], ensure_ascii=False, indent=1), "```", "",
              "## 反馈通道（描述）", "", "```json", json.dumps(analysis["feedback_channels"], ensure_ascii=False, indent=1), "```", ""]
    (HERE / "tables.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("check", "run", "analyze"))
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()
    disable_power_throttling()
    if args.command == "check":
        check()
    elif args.command == "run":
        execute(SEEDS, cf.ARCHIVE, WORK, args.workers)
    else:
        analyze(WORK)


if __name__ == "__main__":
    main()
