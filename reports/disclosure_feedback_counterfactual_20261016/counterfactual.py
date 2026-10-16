"""Feedback counterfactual (research contract 20.17): what the full stage F model adds to its own firm rule.

  .venv/Scripts/python.exe reports/disclosure_feedback_counterfactual_20261016/counterfactual.py check
  .venv/Scripts/python.exe reports/disclosure_feedback_counterfactual_20261016/counterfactual.py run --workers 16 [--shard 0/2]
  .venv/Scripts/python.exe reports/disclosure_feedback_counterfactual_20261016/counterfactual.py analyze

A firm's decision in the full model reads its financing benefit B and market cap P, its own state and the
policy, and nothing else; the audit draw is the same for every policy of a seed. So, given the B and P paths
and the audit draw, the firm side can be replayed without the investor market (``replay``). The replay of a
run's own paths must reproduce that run exactly; that is the identity check behind the decomposition.

(1) run, phase 1: the full model for the 12 scenarios of blocks A (market on), C (equal costs) and E (no
    decay) on the confirmatory seeds 41001-41030, recording B, P and the audit draw at every decision. Each
    result fingerprint must equal the stage F archive's. Paths go to work/paths (local, regenerable).
(2) run, phase 2: for each market setting and seed, every policy of the setting is replayed with B and P
    taken from that setting's baseline run (B, eqcost_B, decay0_B) in five forms:
      Rbase  the baseline's path, decision by decision: no response of B or P to the policy;
      M2     per-firm means before the switch (decisions 60-1200) and in the policy window (1260-3480);
      M      per-firm policy-window means throughout;
      S      the day-1200 values throughout (the stage G sandbox; its audits came from Mulberry32);
      Mhom   one cross-firm B, the mean of M's values, with M's market caps.
    The full model minus Rbase is the feedback from the policy to B and P (prices, investor evolution and
    the firms' reports acting through the investors); Rbase - M2, M2 - M and M - S split the remaining
    gap between the full model and the stage G simplification into the time path of B and P.
(3) analyze: paired 95% t intervals over the 30 seeds for each contrast in each form and for the steps
    between forms, plus the qualitative stage F findings in each form. Full-model values come from the
    stage F archive (identical to the reruns where both exist).

Writes results.json, analysis.json and tables.md next to this script; per-task records stay in work/.
Needs the stage F confirmatory archive and the CSI 300 domain file, which stay local.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import replace
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "showcase" / "sandbox"))

from abm.disclosure.experiments import _inputs, freeze_spec  # noqa: E402
from abm.disclosure.firms import SIZE_CLASS_NAMES  # noqa: E402
from abm.disclosure.game import IMPROVE, INFLATE, MAINTAIN, AttributeState, DisclosureMarket  # noqa: E402
from abm.disclosure.metrics import compute_metrics  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402
import reference  # noqa: E402
from reference import SandboxFirms, decide  # noqa: E402

SPEC = ROOT / "configs" / "disclosure_stage_f_confirmatory_v1.json"
ARCHIVE = ROOT / "reports" / "disclosure_stage_f_20261014" / "confirmatory_v1"
DEV_ARCHIVE = ROOT / "reports" / "disclosure_stage_f_20261014" / "development_v1"
EXPERIMENT_ID = "90ee860663d4e081d9de4c73bcec40de9083902166c6e470d8f430e562d85d57"
SEEDS = list(range(41001, 41031))
CHECK_SEED = 33001
WORK = HERE / "work"
INTERVAL, DAYS, START, SWITCH_PERIOD = 60, 3500, 1200, 20  # decisions 60..1200 are periods 1..20
WINDOW = slice(START // INTERVAL + 1, DAYS // INTERVAL + 1)  # decisions in (1200, 3500]: periods 21..58
PRE = slice(1, SWITCH_PERIOD + 1)
TERMINAL_DAYS = 252
SETTINGS = {
    "main": ("B", ["B", "I", "F", "IF", "I_0p3", "I_0p5", "I_0p7", "I_0p8", "F_0x", "F_2x", "F_8x", "P_1x", "P_2x", "P_4x"]),
    "eqcost": ("eqcost_B", ["eqcost_B", "eqcost_I", "eqcost_F", "eqcost_IF"]),
    "decay0": ("decay0_B", ["decay0_B", "decay0_I", "decay0_F", "decay0_IF"]),
}
RECORDED = ["B", "I", "F", "IF", "eqcost_B", "eqcost_I", "eqcost_F", "eqcost_IF", "decay0_B", "decay0_I", "decay0_F", "decay0_IF"]
VARIANTS = ("Rbase", "M2", "M", "S", "Mhom")
SOURCES = ("full", "own", *VARIANTS)
STEPS = (("feedback", "full", "Rbase"), ("within_phase_path", "Rbase", "M2"), ("pre_switch_level", "M2", "M"),
         ("snapshot_level", "M", "S"), ("total", "full", "S"), ("b_heterogeneity", "M", "Mhom"))
METRICS = ("true_change", "full_period_change", "wash", "improve", "wash_large", "wash_mid", "wash_small",
           "inflation_mean", "terminal_inflation", "size_gap")


# -- full model with recorded decision inputs --------------------------------------

class PathMarket(DisclosureMarket):
    """The full disclosure market, recording read only what each decision saw: B and the market cap."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        decisions = self.config.trading_days // self.config.firm_decision_interval + 1
        self.benefit_path = np.full((decisions, self.config.n_firms), np.nan)
        self.price_path_at_decision = np.full((decisions, self.config.n_firms), np.nan)
        self.initial_goodness = self.attributes.goodness.copy()
        self._period: int | None = None

    def marginal_financing_saving(self):
        value = super().marginal_financing_saving()
        if self._period is not None:
            self.benefit_path[self._period] = value
        return value

    def _audit_and_decide(self, day: int, period: int) -> None:
        self._period = period
        self.price_path_at_decision[period] = self.prices
        super()._audit_and_decide(day, period)
        self._period = None


# -- replay of the firm side ------------------------------------------------------------

def replay(firms: dict, domain, schedule, benefit, price, audit) -> dict:
    """Days 1..3500 of the full model's firm side, with B, market cap and audit draws given per decision.

    ``benefit`` and ``price`` are (decisions + 1, firms) arrays indexed by period = day // 60 (row 0 unused);
    ``audit`` holds the full model's audit selections. The daily order follows ``DisclosureMarket``: decay
    and due actions, then on decision days the audit (detected inflation removed) and the NPV decision.
    """
    size_class, initial, cost_scale = firms["size_class"], firms["initial_goodness"], firms["cost_scale"]
    n = size_class.size
    state = AttributeState(goodness=initial.copy(), inflation=np.zeros(n), cost_scale=cost_scale.copy(),
                           ceiling=domain.observation_ceiling)
    true, inflation = np.empty((DAYS + 1, n)), np.empty((DAYS + 1, n))
    true[0], inflation[0] = state.goodness, state.inflation
    actions = np.full((DAYS // INTERVAL + 1, n), MAINTAIN, dtype=np.int64)
    amounts = np.zeros(actions.shape)
    for day in range(1, DAYS + 1):
        state.advance(day, domain)
        if day % INTERVAL == 0:
            period = day // INTERVAL
            regime = schedule.at(day)
            caught = audit[period] & (state.inflation > 0)
            state.inflation[caught] = 0.0
            inputs = SandboxFirms(size_class, initial, cost_scale, market_cap=price[period], benefit=benefit[period])
            choices, wash_due = decide(state, inputs, domain, regime, day)
            improve = np.flatnonzero(choices.actions == IMPROVE)
            inflate = np.flatnonzero(choices.actions == INFLATE)
            state.schedule(day + max(1, domain.implementation_delay_days), IMPROVE, improve, choices.amounts[improve])
            state.schedule(wash_due, INFLATE, inflate, choices.amounts[inflate])
            actions[period], amounts[period] = choices.actions, choices.amounts
        true[day], inflation[day] = state.goodness, state.inflation
    return {"true": true, "inflation": inflation, "actions": actions, "amounts": amounts}


def window_metrics(true, inflation, actions, size_class) -> dict:
    """The stage F metrics this study compares, computed as ``compute_metrics`` does."""
    change = true[DAYS] - true[START]
    window = actions[WINDOW]
    washing = window == INFLATE
    large, small = size_class == 0, size_class == 2
    return {
        "true_change": float(change.mean()),
        "full_period_change": float((true[DAYS] - true[0]).mean()),
        "wash": float(washing.mean()),
        "improve": float((window == IMPROVE).mean()),
        **{f"wash_{name}": float(washing[:, size_class == index].mean()) for index, name in enumerate(SIZE_CLASS_NAMES)},
        "inflation_mean": float(inflation[START:].mean()),
        "terminal_inflation": float(inflation[DAYS + 1 - TERMINAL_DAYS:].mean()),
        "size_gap": float(change[large].mean() - change[small].mean()),
    }


def archive_metrics(metrics: dict) -> dict:
    """The same metrics from a stage F ``metrics.json``."""
    actions = metrics["actions"]
    return {
        "true_change": metrics["true_change"]["equal_weight_sd"],
        "full_period_change": metrics["full_period_change"]["equal_weight_sd"],
        "wash": actions["wash"] / actions["decisions"],
        "improve": actions["improve"] / actions["decisions"],
        **{f"wash_{name}": actions["wash_share_by_size"][name] for name in SIZE_CLASS_NAMES},
        "inflation_mean": metrics["inflation"]["mean_sd"],
        "terminal_inflation": metrics["terminal_year"]["inflation_mean_sd"],
        "size_gap": metrics["size"]["large_minus_small_sd"],
    }


def max_difference(a: dict, b: dict) -> float:
    return max(abs(a[key] - b[key]) for key in METRICS)


def by_size(values, size_class) -> list[float]:
    return [float(values[size_class == index].mean()) for index in range(3)]


# -- phase 1: full-model runs ----------------------------------------------------------------

def record_task(scenario: dict, seed: int, expected_fingerprint: str, out: str) -> dict:
    started = time.perf_counter()
    name = scenario["name"]
    try:
        config, domain, policy = _inputs(scenario, seed)
        settings = (config.firm_decision_interval, config.financing_horizon_days, config.financing_repricing_interval,
                    config.firm_discount_rate, config.trading_days, config.burn_in_days, config.firm_policy)
        sandbox = (reference.DECISION_INTERVAL, reference.HORIZON_DAYS, reference.REPRICING_INTERVAL,
                   reference.DISCOUNT_RATE, DAYS, START, "npv")
        if settings != sandbox:
            raise ValueError(f"market settings {settings} differ from the replay's {sandbox}")
        market = PathMarket(config, domain, policy)
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

        reported = archive_metrics(compute_metrics(result, config, domain))
        full = window_metrics(np.asarray(result.true_goodness), np.asarray(result.inflation), np.asarray(result.actions), size_class)
        own = replay(firms, domain, policy, benefit, price, audit)
        own_metrics = window_metrics(own["true"], own["inflation"], own["actions"], size_class)
        impact = np.asarray(result.impact_share)
        return {
            "status": "complete", "scenario": name, "seed": seed, "run_id": market.run_id,
            "fingerprint": fingerprint, "fingerprint_matches_stage_f": fingerprint == expected_fingerprint,
            "seconds": round(time.perf_counter() - started, 1),
            "full": reported, "metric_function_max_difference": max_difference(full, reported),
            "own_replay": {
                "metrics": own_metrics,
                "actions_identical": bool(np.array_equal(own["actions"], result.actions)),
                "amounts_max_abs": float(np.abs(own["amounts"] - result.amounts).max()),
                "true_max_abs": float(np.abs(own["true"] - result.true_goodness).max()),
                "inflation_max_abs": float(np.abs(own["inflation"] - result.inflation).max()),
                "metrics_max_difference": max_difference(own_metrics, reported),
            },
            "audit_sha256": hashlib.sha256(np.ascontiguousarray(audit).tobytes()).hexdigest(),
            "benefit": {"pre_mean": float(benefit[PRE].mean()), "window_mean": float(benefit[WINDOW].mean()),
                        "snapshot_mean": float(benefit[SWITCH_PERIOD].mean()),
                        "pre_by_size": by_size(benefit[PRE].mean(axis=0), size_class),
                        "window_by_size": by_size(benefit[WINDOW].mean(axis=0), size_class),
                        "by_decision": [float(v) for v in benefit[1:].mean(axis=1)]},
            "price": {"snapshot_mean": float(price[SWITCH_PERIOD].mean()), "window_mean": float(price[WINDOW].mean()),
                      "window_by_size": by_size(price[WINDOW].mean(axis=0), size_class)},
            "impact_share": {"day_0": float(impact[0]), "day_1200": float(impact[START]), "day_3500": float(impact[DAYS])},
        }
    except Exception as error:  # kept as a failed record, never retried silently
        return {"status": "failed", "scenario": name, "seed": seed, "error_type": type(error).__name__,
                "error": str(error), "traceback": traceback.format_exc(), "seconds": round(time.perf_counter() - started, 1)}


# -- phase 2: replays from the baseline paths ----------------------------------------------------

def variant_paths(benefit, price) -> dict:
    def two_phase(values):
        out = np.empty_like(values)
        out[:SWITCH_PERIOD + 1] = values[PRE].mean(axis=0)
        out[SWITCH_PERIOD + 1:] = values[WINDOW].mean(axis=0)
        return out

    def constant(row):
        return np.broadcast_to(row, benefit.shape).copy()

    window_b, window_p = benefit[WINDOW].mean(axis=0), price[WINDOW].mean(axis=0)
    return {
        "Rbase": (benefit, price),
        "M2": (two_phase(benefit), two_phase(price)),
        "M": (constant(window_b), constant(window_p)),
        "S": (constant(benefit[SWITCH_PERIOD]), constant(price[SWITCH_PERIOD])),
        "Mhom": (np.full(benefit.shape, window_b.mean()), constant(window_p)),
    }


def replay_task(setting: str, seed: int, scenarios: dict, out: str) -> dict:
    started = time.perf_counter()
    base, names = SETTINGS[setting]
    try:
        with np.load(Path(out) / "paths" / base / f"seed_{seed}.npz") as data:
            benefit, price, audit = data["benefit"], data["price"], data["audit"]
            firms = {key: data[key] for key in ("size_class", "initial_goodness", "cost_scale")}
        paths = variant_paths(benefit, price)
        rows = {}
        for name in names:
            config, domain, policy = _inputs(scenarios[name], seed)
            rows[name] = {}
            for variant, (b, p) in paths.items():
                run = replay(firms, domain, policy, b, p, audit)
                rows[name][variant] = window_metrics(run["true"], run["inflation"], run["actions"], firms["size_class"])
        return {"status": "complete", "setting": setting, "seed": seed, "base": base, "metrics": rows,
                "seconds": round(time.perf_counter() - started, 1)}
    except Exception as error:
        return {"status": "failed", "setting": setting, "seed": seed, "error_type": type(error).__name__,
                "error": str(error), "traceback": traceback.format_exc(), "seconds": round(time.perf_counter() - started, 1)}


# -- orchestration ---------------------------------------------------------------------------------

def archive_records(archive: Path) -> dict:
    summary = json.loads((archive / "summary.json").read_text(encoding="utf-8"))
    return summary, {(r["scenario"], r["seed"]): r for r in summary["records"]}


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=1, allow_nan=False) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(path)


def log(message: str) -> None:
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}", flush=True)


def execute(seeds: list[int], recorded: list[str], settings: list[str], archive: Path, out: Path, workers: int) -> None:
    frozen = freeze_spec(SPEC)
    summary, records = archive_records(archive)
    if frozen["experiment_id"] != EXPERIMENT_ID and archive == ARCHIVE:
        raise RuntimeError("the frozen stage F identity changed; the reruns would not be stage F")
    scenarios = {row["name"]: row for row in frozen["scenarios"]}
    log(f"experiment_id {frozen['experiment_id']}; archive {archive.name} ({summary['experiment_id'][:12]}); "
        f"{len(seeds)} seeds, {len(recorded)} recorded scenarios, settings {settings}, {workers} workers")
    record_dir, replay_dir = out / "records", out / "replays"
    jobs = [(name, seed) for name in recorded for seed in seeds
            if not (record_dir / f"{name}__{seed}.json").exists()]
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers, initializer=disable_power_throttling) as pool:
        futures = [pool.submit(record_task, scenarios[name], seed, records[(name, seed)]["result_fingerprint"], str(out))
                   for name, seed in jobs]
        for count, future in enumerate(as_completed(futures), 1):
            row = future.result()
            write_json(record_dir / f"{row['scenario']}__{row['seed']}.json", row)
            note = (f"fingerprint {'ok' if row['fingerprint_matches_stage_f'] else 'MISMATCH'}, "
                    f"own replay actions {'identical' if row['own_replay']['actions_identical'] else 'DIFFER'}"
                    if row["status"] == "complete" else f"FAILED {row['error_type']}: {row['error']}")
            log(f"record {count}/{len(jobs)} {row['scenario']} {row['seed']} {row['seconds']} s; {note}")
        log(f"phase 1 done in {time.perf_counter() - started:.0f} s")
        jobs = [(setting, seed) for setting in settings for seed in seeds
                if not (replay_dir / f"{setting}__{seed}.json").exists()]
        futures = [pool.submit(replay_task, setting, seed, scenarios, str(out)) for setting, seed in jobs]
        for count, future in enumerate(as_completed(futures), 1):
            row = future.result()
            write_json(replay_dir / f"{row['setting']}__{row['seed']}.json", row)
            note = "ok" if row["status"] == "complete" else f"FAILED {row['error_type']}: {row['error']}"
            log(f"replay {count}/{len(jobs)} {row['setting']} {row['seed']} {row['seconds']} s; {note}")
    log(f"all done in {time.perf_counter() - started:.0f} s")


def check() -> None:
    """Pipeline check on development seed 33001: identities and timing only, no effect estimates."""
    disable_power_throttling()
    # (a) The replay with constant inputs and Mulberry32 audits is the sandbox's simulate().
    sandbox = json.loads((ROOT / "showcase" / "data" / "sandbox_firms.json").read_text(encoding="utf-8"))["domains"]["esg"]
    exported = reference.firms_from(sandbox["firms"])
    domain = reference.domain_from(sandbox)
    baseline = {**sandbox["baseline_policy"], "disclosure_delay_days": None}
    schedule = reference.schedule_from({"baseline": baseline, "intervention": {**baseline, "transparency": 0.6}, "start_day": 1201})
    for decay in (0.2, 0.0):
        expected = reference.simulate(exported, domain, schedule, natural_decay=decay, audit_seed=7)
        rng = reference.Mulberry32(7)
        audit = np.zeros((DAYS // INTERVAL + 1, exported.size_class.size), dtype=bool)
        for period in range(1, DAYS // INTERVAL + 1):
            audit[period] = rng.uniforms(exported.size_class.size) < schedule.at(period * INTERVAL).audit_probability
        firms = {"size_class": exported.size_class, "initial_goodness": exported.initial_goodness, "cost_scale": exported.cost_scale}
        shape = (DAYS // INTERVAL + 1, exported.size_class.size)
        run = replay(firms, replace(domain, natural_decay=decay), schedule, np.broadcast_to(exported.benefit, shape),
                     np.broadcast_to(exported.market_cap, shape), audit)
        same = np.array_equal(run["actions"][1:], expected["actions"]) and np.array_equal(run["true"][1:].mean(axis=1), expected["mean_goodness"][1:])
        log(f"replay with constant inputs equals reference.simulate (decay {decay}): {same}")
        if not same:
            raise SystemExit("replay differs from the sandbox reference")
    # (b) Development seed: rerun B and I, replay the main setting.
    out = HERE / "work_check"
    execute([CHECK_SEED], ["B", "I"], ["main"], DEV_ARCHIVE, out, workers=2)
    for name in ("B", "I"):
        row = json.loads((out / "records" / f"{name}__{CHECK_SEED}.json").read_text(encoding="utf-8"))
        if row["status"] != "complete":
            raise SystemExit(f"{name} failed: {row['error']}")
        own = row["own_replay"]
        log(f"{name}: fingerprint matches development archive {row['fingerprint_matches_stage_f']}; metric function "
            f"max diff {row['metric_function_max_difference']:.1e}; own replay actions identical {own['actions_identical']}, "
            f"amounts {own['amounts_max_abs']:.1e}, true {own['true_max_abs']:.1e}, inflation {own['inflation_max_abs']:.1e}")
    row = json.loads((out / "replays" / f"main__{CHECK_SEED}.json").read_text(encoding="utf-8"))
    base = json.loads((out / "records" / f"B__{CHECK_SEED}.json").read_text(encoding="utf-8"))
    log(f"replay task {row['status']} in {row['seconds']} s; Rbase on B equals the full B run: "
        f"{max_difference(row['metrics']['B']['Rbase'], base['full']) == 0}")


# -- analysis --------------------------------------------------------------------------------------------

CONTRASTS = {  # name: (weights, metric)
    "I_minus_B": ({"I": 1, "B": -1}, "true_change"),
    "F_minus_B": ({"F": 1, "B": -1}, "true_change"),
    "I_minus_F": ({"I": 1, "F": -1}, "true_change"),
    "IF_minus_I": ({"IF": 1, "I": -1}, "true_change"),
    "decay0_I_minus_B": ({"decay0_I": 1, "decay0_B": -1}, "true_change"),
    "decay0_F_minus_B": ({"decay0_F": 1, "decay0_B": -1}, "true_change"),
    "decay0_I_minus_F": ({"decay0_I": 1, "decay0_F": -1}, "true_change"),
    "eqcost_I_minus_B": ({"eqcost_I": 1, "eqcost_B": -1}, "true_change"),
    "eqcost_F_minus_B": ({"eqcost_F": 1, "eqcost_B": -1}, "true_change"),
    "eqcost_I_minus_F": ({"eqcost_I": 1, "eqcost_F": -1}, "true_change"),
    **{f"I_{tag}_minus_B": ({f"I_{tag}": 1, "B": -1}, "true_change") for tag in ("0p3", "0p5", "0p7", "0p8")},
    "fine_0_to_1x": ({"B": 1, "F_0x": -1}, "true_change"),
    "fine_1_to_2x": ({"F_2x": 1, "B": -1}, "true_change"),
    "fine_2_to_4x": ({"F": 1, "F_2x": -1}, "true_change"),
    "fine_4_to_8x": ({"F_8x": 1, "F": -1}, "true_change"),
    "P_1x_minus_fixed_1x": ({"P_1x": 1, "B": -1}, "true_change"),
    "P_2x_minus_fixed_2x": ({"P_2x": 1, "F_2x": -1}, "true_change"),
    "P_4x_minus_fixed_4x": ({"P_4x": 1, "F": -1}, "true_change"),
    "I_minus_B_terminal_inflation": ({"I": 1, "B": -1}, "terminal_inflation"),
    "F_minus_B_terminal_inflation": ({"F": 1, "B": -1}, "terminal_inflation"),
    "I_minus_B_size_gap": ({"I": 1, "B": -1}, "size_gap"),
    "B_minus_eqcost_B_size_gap": ({"B": 1, "eqcost_B": -1}, "size_gap"),
}
HEADLINE = ("I_minus_B", "F_minus_B", "I_minus_F", "decay0_I_minus_B", "decay0_F_minus_B", "decay0_I_minus_F")
LEVELS = {  # scenario levels reported in every form
    "wash": ["B", "I_0p3", "I_0p5", "I", "I_0p7", "I_0p8", "F_0x", "F_2x", "F", "F_8x", "P_1x", "P_2x", "P_4x",
             "eqcost_B", "decay0_B", "decay0_F"],
    "terminal_inflation": ["B", "I", "F", "IF", "decay0_B", "decay0_I", "decay0_F"],
    "size_gap": ["B", "I", "F", "eqcost_B", "eqcost_I", "P_1x", "P_4x", "decay0_B"],
    "true_change": ["B", "I", "F", "IF", "decay0_B", "decay0_I", "eqcost_B"],
    "inflation_mean": ["B", "I", "F", "decay0_B"],
}


def interval(values) -> dict:
    values = np.asarray(values, dtype=np.float64)
    n = values.size
    mean = float(values.mean())
    half = float(stats.t.ppf(0.975, n - 1) * values.std(ddof=1) / np.sqrt(n)) if n > 1 else float("nan")
    return {"mean": mean, "ci_low": mean - half, "ci_high": mean + half, "n": int(n)}


def collect(out: Path) -> dict:
    """values[source][scenario][metric] -> per-seed list in SEEDS order."""
    summary, records = archive_records(ARCHIVE)
    if summary["experiment_id"] != EXPERIMENT_ID:
        raise RuntimeError("unexpected stage F archive")
    scenarios = sorted({name for _, names in SETTINGS.values() for name in names})
    values = {source: {name: {metric: [] for metric in METRICS} for name in scenarios} for source in SOURCES}
    checks = {"fingerprints_matching": 0, "recorded_runs": 0, "failed": [], "own_actions_identical": 0,
              "own_max_abs": {"amounts": 0.0, "true": 0.0, "inflation": 0.0, "metrics": 0.0},
              "rerun_vs_archive_metrics_max": 0.0, "metric_function_max": 0.0, "audit_draws_shared": True,
              "rbase_on_baseline_equals_full_max": 0.0, "core_validation_failures": {}}
    reruns = {}
    for seed in SEEDS:
        audits = set()
        for name in RECORDED:
            row = json.loads((out / "records" / f"{name}__{seed}.json").read_text(encoding="utf-8"))
            if row["status"] != "complete":
                checks["failed"].append(f"record {name} {seed}: {row['error']}")
                continue
            reruns[(name, seed)] = row
            checks["recorded_runs"] += 1
            checks["fingerprints_matching"] += row["fingerprint_matches_stage_f"]
            own = row["own_replay"]
            checks["own_actions_identical"] += own["actions_identical"]
            for key in ("amounts", "true", "inflation"):
                checks["own_max_abs"][key] = max(checks["own_max_abs"][key], own[f"{key}_max_abs"])
            checks["own_max_abs"]["metrics"] = max(checks["own_max_abs"]["metrics"], own["metrics_max_difference"])
            checks["metric_function_max"] = max(checks["metric_function_max"], row["metric_function_max_difference"])
            checks["rerun_vs_archive_metrics_max"] = max(
                checks["rerun_vs_archive_metrics_max"], max_difference(row["full"], archive_metrics(records[(name, seed)]["metrics"])))
            audits.add(row["audit_sha256"])
        checks["audit_draws_shared"] &= len(audits) == 1
    replays = {}
    for setting, (base, _) in SETTINGS.items():
        for seed in SEEDS:
            row = json.loads((out / "replays" / f"{setting}__{seed}.json").read_text(encoding="utf-8"))
            if row["status"] != "complete":
                checks["failed"].append(f"replay {setting} {seed}: {row['error']}")
                continue
            replays[(setting, seed)] = row
            checks["rbase_on_baseline_equals_full_max"] = max(
                checks["rbase_on_baseline_equals_full_max"], max_difference(row["metrics"][base]["Rbase"], reruns[(base, seed)]["full"]))
    if checks["failed"]:
        raise RuntimeError(f"incomplete tasks: {checks['failed']}")
    setting_of = {name: setting for setting, (_, names) in SETTINGS.items() for name in names}
    for name in scenarios:
        for seed in SEEDS:
            record = records[(name, seed)]
            failing = [gate for gate in ("mechanical", "stylized") if record["validation"][gate]["status"] != "PASS"]
            if failing:
                checks["core_validation_failures"].setdefault(name, []).append(seed)
            full = archive_metrics(record["metrics"])
            own = reruns[(name, seed)]["own_replay"]["metrics"] if (name, seed) in reruns else None
            forms = replays[(setting_of[name], seed)]["metrics"][name]
            for metric in METRICS:
                values["full"][name][metric].append(full[metric])
                values["own"][name][metric].append(own[metric] if own else None)
                for variant in VARIANTS:
                    values[variant][name][metric].append(forms[variant][metric])
    for source in SOURCES:  # drop the own replay where no rerun exists
        for name in scenarios:
            if None in values[source][name]["true_change"]:
                values[source][name] = None
    return {"values": values, "checks": checks, "reruns": reruns}


def contrast_values(values: dict, source: str, weights: dict, metric: str):
    if any(values[source][name] is None for name in weights):
        return None
    return sum(weight * np.asarray(values[source][name][metric]) for name, weight in weights.items())


def descriptive_feedback(reruns: dict) -> dict:
    """How B, market caps and the impact-investor share respond to each policy (recorded scenarios)."""
    out = {}
    for setting, (base, names) in SETTINGS.items():
        for name in names:
            if name == base or name not in RECORDED:
                continue
            ratio, ratio_size, price, impact = [], [], [], []
            for seed in SEEDS:
                own, ref = reruns[(name, seed)], reruns[(base, seed)]
                ratio.append(own["benefit"]["window_mean"] / ref["benefit"]["window_mean"] - 1)
                ratio_size.append([a / b - 1 for a, b in zip(own["benefit"]["window_by_size"], ref["benefit"]["window_by_size"])])
                price.append(own["price"]["window_mean"] / ref["price"]["window_mean"] - 1)
                impact.append(own["impact_share"]["day_3500"] - ref["impact_share"]["day_3500"])
            out[name] = {"base": base, "window_b_relative": interval(ratio),
                         "window_b_relative_by_size": [interval(column) for column in zip(*ratio_size)],
                         "window_price_relative": interval(price), "impact_share_day_3500_difference": interval(impact)}
    for base in ("B", "eqcost_B", "decay0_B"):
        rows = [reruns[(base, seed)] for seed in SEEDS]
        out[f"{base}_levels"] = {
            "pre_mean": interval([r["benefit"]["pre_mean"] for r in rows]),
            "snapshot_mean": interval([r["benefit"]["snapshot_mean"] for r in rows]),
            "window_mean": interval([r["benefit"]["window_mean"] for r in rows]),
            "window_by_size": [interval(column) for column in zip(*(r["benefit"]["window_by_size"] for r in rows))],
            "by_decision_mean": [float(v) for v in np.mean([r["benefit"]["by_decision"] for r in rows], axis=0)],
            "impact_share": {day: interval([r["impact_share"][day] for r in rows]) for day in ("day_0", "day_1200", "day_3500")},
        }
    return out


def qualitative(values: dict, source: str) -> dict | None:
    v = values[source]
    if any(v[name] is None for name in ("B", "I", "F", "IF", "I_0p3", "I_0p5", "I_0p7", "I_0p8", "F_0x")):
        return None

    def mean(name, metric="true_change"):
        return float(np.mean(v[name][metric]))

    def seeds_ordered(prefix):
        i, f, b = (np.asarray(v[prefix + p]["true_change"]) for p in ("I", "F", "B"))
        return int(((i > f) & (f > b)).sum())

    fines = ["F_0x", "B", "F_2x", "F", "F_8x"]
    effect = {tau: mean(name) - mean("B") for tau, name in (("0.3", "I_0p3"), ("0.5", "I_0p5"), ("0.6", "I"),
                                                              ("0.7", "I_0p7"), ("0.8", "I_0p8"))}
    gains = [mean(b) - mean(a) for a, b in zip(fines, fines[1:])]
    return {
        "ordering_I_F_B": {"main_mean": mean("I") > mean("F") > mean("B"), "main_seeds": seeds_ordered(""),
                           "decay0_mean": mean("decay0_I") > mean("decay0_F") > mean("decay0_B"),
                           "decay0_seeds": seeds_ordered("decay0_"),
                           "eqcost_mean": mean("eqcost_I") > mean("eqcost_F") > mean("eqcost_B"),
                           "eqcost_seeds": seeds_ordered("eqcost_")},
        "threshold": {"wash_by_tau": {tau: mean(name, "wash") for tau, name in (("0.1", "B"), ("0.3", "I_0p3"), ("0.5", "I_0p5"),
                                                                             ("0.6", "I"), ("0.7", "I_0p7"), ("0.8", "I_0p8"))},
                      "no_washing_from_0.6": all(np.max(v[name]["wash"]) == 0 for name in ("I", "I_0p7", "I_0p8")),
                      "washing_below_0.6": all(np.min(v[name]["wash"]) > 0 for name in ("I_0p3", "I_0p5")),
                      "effect_by_tau": effect,
                      "plateau_share": (effect["0.8"] - effect["0.6"]) / effect["0.6"] if effect["0.6"] else None},
        "IF_equals_I": float(np.max(np.abs(np.asarray(v["IF"]["true_change"]) - np.asarray(v["I"]["true_change"])))),
        "fines": {"wash_by_multiple": {m: mean(name, "wash") for m, name in zip(("0", "1", "2", "4", "8"), fines)},
                  "true_change_gain_per_step": dict(zip(("0->1", "1->2", "2->4", "4->8"), gains)),
                  "diminishing": all(a > b for a, b in zip(gains, gains[1:]))},
        "size": {"gap_B": mean("B", "size_gap"), "gap_eqcost_B": mean("eqcost_B", "size_gap"), "gap_I": mean("I", "size_gap"),
                 "gap_reversed_by_I": mean("B", "size_gap") < 0 < mean("I", "size_gap"),
                 "equal_costs_widen_gap": mean("eqcost_B", "size_gap") < mean("B", "size_gap"),
                 "wash_large_small_B": [mean("B", "wash_large"), mean("B", "wash_small")],
                 "proportional_large_below_small": {k: [mean(f"P_{k}", "wash_large"), mean(f"P_{k}", "wash_small")]
                                                    for k in ("1x", "2x", "4x")}},
    }


def analyze(out: Path) -> None:
    gathered = collect(out)
    values, checks = gathered["values"], gathered["checks"]
    contrasts = {}
    for name, (weights, metric) in CONTRASTS.items():
        row = {"weights": weights, "metric": metric, "forms": {}, "steps": {}}
        series = {source: contrast_values(values, source, weights, metric) for source in SOURCES}
        for source, series_values in series.items():
            if series_values is not None:
                row["forms"][source] = interval(series_values)
        for step, plus, minus in STEPS:
            row["steps"][step] = interval(series[plus] - series[minus])
        contrasts[name] = row
    levels = {metric: {name: {source: interval(values[source][name][metric]) for source in SOURCES if values[source][name] is not None}
                       for name in names} for metric, names in LEVELS.items()}
    analysis = {
        "schema_version": 1, "generated_by": "reports/disclosure_feedback_counterfactual_20261016/counterfactual.py",
        "contract": "docs/disclosure_research_contract.md 20.17", "stage_f_experiment_id": EXPERIMENT_ID,
        "seeds": f"{SEEDS[0]}-{SEEDS[-1]}", "window": [START, DAYS],
        "forms": {"full": "stage F archive", "own": "replay of the run's own B, market cap and audit draws (identity check)",
                  "Rbase": "baseline run's B and market-cap path", "M2": "per-firm pre-switch and window means of the baseline path",
                  "M": "per-firm window means", "S": "day-1200 snapshot values (stage G)", "Mhom": "one cross-firm B, per-firm window-mean caps"},
        "steps": {step: f"{plus} - {minus}" for step, plus, minus in STEPS},
        "interval": "paired 95% t interval over seeds", "checks": checks,
        "contrasts": contrasts, "levels": levels,
        "qualitative": {source: qualitative(values, source) for source in SOURCES},
        "feedback_channels": descriptive_feedback(gathered["reruns"]),
    }
    write_json(HERE / "analysis.json", analysis)
    write_json(HERE / "results.json", {"schema_version": 1, "seeds": SEEDS, "metrics": list(METRICS),
                                       "note": "values[form][scenario][metric] = per-seed list in seed order",
                                       "values": values})
    write_tables(analysis)
    log("wrote analysis.json, results.json and tables.md")


def fmt(row: dict | None, digits: int = 3, percent: bool = False) -> str:
    if row is None:
        return "—"
    if percent:
        return f"{row['mean']:.1%}"
    return f"{row['mean']:+.{digits}f} [{row['ci_low']:+.{digits}f}, {row['ci_high']:+.{digits}f}]"


def write_tables(analysis: dict) -> None:
    c = analysis["checks"]
    lines = ["# 反馈反事实：完整表格", "", "由 counterfactual.py analyze 生成。种子 41001–41030，配对 95% t 区间。"
             "形式：full 完整模型（阶段 F 档案）；own 用本运行自身的 B、市值与核查抽样重放；Rbase 用同市场设定基准运行的路径；"
             "M2 切换前与政策窗口两段均值；M 窗口均值；S 第 1200 日快照（阶段 G 的简化）；Mhom 所有企业同一个 B。", "",
             "## 检查", "",
             f"- 重跑 {c['recorded_runs']} 个，指纹与阶段 F 档案一致 {c['fingerprints_matching']} 个；自身路径重放行动逐期相同 "
             f"{c['own_actions_identical']} 个，幅度、真实水平、虚报的最大绝对差 {c['own_max_abs']['amounts']:.1e}、"
             f"{c['own_max_abs']['true']:.1e}、{c['own_max_abs']['inflation']:.1e}，指标最大差 {c['own_max_abs']['metrics']:.1e}。",
             f"- 指标函数与 compute_metrics 的最大差 {c['metric_function_max']:.1e}；重跑与档案指标的最大差 {c['rerun_vs_archive_metrics_max']:.1e}；"
             f"同一种子各场景的核查抽样相同：{c['audit_draws_shared']}；基准场景上 Rbase 与完整模型的最大差 {c['rbase_on_baseline_equals_full_max']:.1e}。",
             f"- 核心验证失败的运行（保留在统计中）：{ {k: len(v) for k, v in c['core_validation_failures'].items()} }。", ""]
    lines += ["## 对比：各形式的值", "", "| 对比 | 指标 | full | own | Rbase | M2 | M | S | Mhom |", "|---|---|---|---|---|---|---|---|---|"]
    for name, row in analysis["contrasts"].items():
        lines.append(f"| {name} | {row['metric']} | " + " | ".join(fmt(row["forms"].get(s)) for s in SOURCES) + " |")
    lines += ["", "## 对比：形式之间的差（配对）", "",
              "| 对比 | 反馈 full−Rbase | 阶段内路径 Rbase−M2 | 切换前水平 M2−M | 快照水平 M−S | 合计 full−S | B 异质性 M−Mhom |",
              "|---|---|---|---|---|---|---|"]
    for name, row in analysis["contrasts"].items():
        lines.append(f"| {name} | " + " | ".join(fmt(row["steps"][step]) for step, _, _ in STEPS) + " |")
    lines += ["", "## 场景水平", ""]
    for metric, rows in analysis["levels"].items():
        percent = metric == "wash"
        lines += [f"**{metric}**", "", "| 场景 | " + " | ".join(SOURCES) + " |", "|---|" + "---|" * len(SOURCES)]
        for name, forms in rows.items():
            lines.append(f"| {name} | " + " | ".join(fmt(forms.get(s), percent=percent) for s in SOURCES) + " |")
        lines.append("")
    lines += ["## 阶段 F 定性结论在各形式中", "", "```json", json.dumps(analysis["qualitative"], ensure_ascii=False, indent=1), "```", "",
              "## 反馈通道（描述）", "", "```json", json.dumps(analysis["feedback_channels"], ensure_ascii=False, indent=1), "```", ""]
    (HERE / "tables.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("check", "run", "analyze"))
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--shard", default="0/1", help="i/n: run every n-th seed from the i-th; shards share work/")
    args = parser.parse_args()
    disable_power_throttling()
    if args.command == "check":
        check()
    elif args.command == "run":
        index, count = (int(part) for part in args.shard.split("/"))
        execute(SEEDS[index::count], RECORDED, list(SETTINGS), ARCHIVE, WORK, args.workers)
    else:
        analyze(WORK)


if __name__ == "__main__":
    main()
