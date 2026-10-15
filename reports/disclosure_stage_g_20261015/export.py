"""Stage G.1: export the sandbox's synthetic firms and the stage F results the page shows.

  .venv/Scripts/python.exe reports/disclosure_stage_g_20261015/export.py

(a) One fresh seed (51001, unused in any earlier JSON record) runs the stage F main setting at
contract scale for B, I, F and IF, with and without natural decay (the same scenario definitions as
configs/disclosure_stage_f_confirmatory_v1.json). The B run records day 1200, the last decision before
the switch: for each of the 200 synthetic firms its size class, market cap, cost coefficient, financing
benefit B, true level and inflation, the pending actions, and the decision the full model took. The
model has no real companies; firms are numbered 1-200 in model order. The AI-washing domain gets the
same snapshot from its own baseline run, stopped at day 1200.
(b) Stage F results are copied from the committed confirmatory_v1_analysis.json with its experiment_id,
SHA-256 and last commit.

Writes showcase/data/sandbox_firms.json, showcase/data/stage_f.json and, next to this script,
full_model_seed51001.json (same-seed full-model metrics for the simplification table).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "showcase" / "sandbox"))

from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.experiments import _inputs, freeze_spec  # noqa: E402
from abm.disclosure.metrics import compute_metrics  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.disclosure.runner import run_identity  # noqa: E402
from abm.disclosure.validate import validate_market  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402
from reference import SNAPSHOT_DAY, SnapshotMarket, take_snapshot  # noqa: E402

SEED = 51001
SPEC = ROOT / "configs" / "disclosure_stage_f_confirmatory_v1.json"
ANALYSIS = ROOT / "reports" / "disclosure_stage_f_20261014" / "confirmatory_v1_analysis.json"
AI_DOMAIN = ROOT / "configs" / "domains" / "ai_washing.json"
SCENARIOS = ("B", "I", "F", "IF", "decay0_B", "decay0_I", "decay0_F", "decay0_IF")
SNAPSHOT_SOURCE = "B"
METRIC_KEYS = {
    "true_change_sd": "true_change.equal_weight_sd", "inflation_mean_sd": "inflation.mean_sd",
    "large_minus_small_sd": "size.large_minus_small_sd", "full_period_change_sd": "full_period_change.equal_weight_sd",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def floats(values) -> list:
    return [float(v) for v in np.asarray(values, dtype=np.float64)]


def lookup(metrics: dict, key: str):
    for part in key.split("."):
        metrics = metrics[part]
    return metrics


def snapshot_payload(market: SnapshotMarket) -> dict:
    snap = market.snapshot
    return {
        "size_class": market.firms.size_class.astype(int).tolist(),
        "market_cap": floats(snap["prices"]),
        "cost_scale": floats(market.attributes.cost_scale),
        "benefit": floats(snap["benefit"]),
        "initial_goodness": floats(market.initial_goodness),
        "goodness": floats(snap["goodness"]),
        "inflation": floats(snap["inflation"]),
        "pending": [{"due_day": int(due), "kind": int(kind), "firms": firms.astype(int).tolist(), "amounts": floats(amounts)}
                    for due, kind, firms, amounts in snap["pending"]],
        "full_model_decision": {"actions": snap["actions"].astype(int).tolist(), "amounts": floats(snap["amounts"])},
    }


def benefit_path(market: SnapshotMarket) -> dict:
    """Mean B by decision day and size class: how far the full model's B moves from the snapshot value."""
    size = market.firms.size_class
    return {str(day): {"mean": float(b.mean()), "by_size": [float(b[size == k].mean()) for k in range(3)]}
            for day, b in sorted(market.benefit_history.items())}


def run_scenario(name: str, scenario: dict) -> dict:
    disable_power_throttling()
    config, domain, policy = _inputs(scenario, SEED)
    started = time.perf_counter()
    market = SnapshotMarket(config, domain, policy, snapshot_day=SNAPSHOT_DAY)
    result = take_snapshot(market)
    metrics = compute_metrics(result, config, domain)
    validation = validate_market(result.market, config)
    actions = metrics["actions"]
    return {
        "scenario": name, "run_id": run_identity(config, domain, policy)["run_id"], "fingerprint": result.fingerprint(),
        "seconds": round(time.perf_counter() - started, 1),
        "validation": {gate: validation[gate]["status"] for gate in ("mechanical", "stylized")},
        "price_cap_hits": int(np.asarray(result.market.price_cap_hits).sum()),
        "metrics": {**{key: lookup(metrics, path) for key, path in METRIC_KEYS.items()},
                    "wash_share": actions["wash"] / actions["decisions"],
                    "wash_share_by_size": actions["wash_share_by_size"]},
        "snapshot": snapshot_payload(market), "benefit_by_decision_day": benefit_path(market),
    }


def run_ai_snapshot(market_config: dict) -> dict:
    disable_power_throttling()
    config = MarketConfig.from_dict({**market_config, "seed": SEED})
    domain = load_domain(AI_DOMAIN)
    policy = PolicySchedule.constant(domain)
    started = time.perf_counter()
    market = SnapshotMarket(config, domain, policy, snapshot_day=SNAPSHOT_DAY, stop_after_snapshot=True)
    if take_snapshot(market) is not None or market.snapshot is None:
        raise RuntimeError("AI-washing run did not stop at the snapshot")
    return {"scenario": "ai_washing_baseline", "run_id": run_identity(config, domain, policy)["run_id"],
            "seconds": round(time.perf_counter() - started, 1), "snapshot": snapshot_payload(market),
            "benefit_by_decision_day": benefit_path(market)}


def domain_payload(domain, config) -> dict:
    low, high = domain.goodness_bounds
    return {
        "name": domain.name, "attribute_label": domain.attribute_label, "unit": domain.unit,
        "natural_decay": domain.natural_decay, "real_cost_scale": domain.real_cost_scale,
        "size_cost_multipliers": list(domain.size_cost_multipliers), "cost_level_elasticity": domain.cost_level_elasticity,
        "max_change_per_period": domain.max_change_per_period, "wash_cost_ratio": domain.wash_cost_ratio,
        "implementation_delay_days": domain.implementation_delay_days, "disclosure_delay_days": domain.disclosure_delay_days,
        "goodness_bounds": [low, high], "observation_ceiling": domain.observation_ceiling, "report_bound": domain.report_bound,
        "baseline_policy": {"audit_probability": domain.baseline_audit_probability, "penalty": domain.baseline_penalty,
                            "transparency": domain.baseline_transparency, "subsidy": domain.baseline_subsidy,
                            "fixed_fine": domain.baseline_fixed_fine},
        "market": {"firm_decision_interval": config.firm_decision_interval, "financing_horizon_days": config.financing_horizon_days,
                   "financing_repricing_interval": config.financing_repricing_interval, "firm_discount_rate": config.firm_discount_rate,
                   "trading_days": config.trading_days, "burn_in_days": config.burn_in_days},
    }


def stage_f_payload() -> dict:
    analysis = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    main = "true_change.equal_weight_sd"
    keep_secondary = ["I_minus_B", "F_minus_B", "IF_minus_B", "decay0_I_minus_B", "decay0_F_minus_B", "decay0_IF_minus_B",
                      "decay0_I_minus_F", "I_0p3_minus_B", "I_0p5_minus_B", "I_0p7_minus_B", "I_0p8_minus_B",
                      "F_0x_minus_B", "F_2x_minus_B", "F_8x_minus_B", "P_1x_minus_fixed_1x", "P_2x_minus_fixed_2x",
                      "P_4x_minus_fixed_4x", "decay0_B_minus_B"]
    secondary = {}
    for name in keep_secondary:
        row = analysis["secondary"][name][main]
        secondary[name] = {key: row[key] for key in ("mean", "ci_low", "ci_high", "n")}
    keep_scenarios = ["B", "I", "F", "IF", "off_B", "decay0_B", "decay0_I", "decay0_F", "decay0_IF",
                      "I_0p3", "I_0p5", "I_0p7", "I_0p8", "F_0x", "F_2x", "F_8x", "P_1x", "P_2x", "P_4x"]
    scenarios = {name: {key: analysis["scenarios"][name][key] for key in
                        ("runs", "core_valid", "true_change", "inflation_mean", "size_gap", "wash", "wash_large", "wash_mid", "wash_small")}
                 for name in keep_scenarios}

    def phase(grid: dict) -> dict:
        return {cell: {"scenario": row["scenario"], "valid_runs": row["valid_runs"],
                       "decay_adjusted": row["classes"]["decay_adjusted_g0.25_w0.25"],
                       "original": row["classes"]["original_g0.25_w0.25"]} for cell, row in grid.items()}

    return {
        "schema_version": 1,
        "source": {"path": rel(ANALYSIS), "sha256": sha256(ANALYSIS), "commit": git("log", "-1", "--format=%H", "--", rel(ANALYSIS)),
                   "report": "reports/disclosure_stage_f_20261014/README.md",
                   "contract": "docs/disclosure_research_contract.md#20-阶段-f核心实验2026-10-14-固定先于任何本节的运行",
                   "experiment_id": analysis["experiment_id"], "purpose": analysis["purpose"],
                   "runs": analysis["pipeline_checks"]["complete"], "planned": analysis["pipeline_checks"]["planned"],
                   "seeds": "41001-41030", "metric": main, "window": [1200, 3500],
                   "interval": "paired 95% t interval across 30 seeds; Holm for the four primary contrasts"},
        "primary": analysis["primary"],
        "secondary": secondary,
        "scenarios": scenarios,
        "phase_map_1": phase(analysis["phase_map_1_taste_by_share"]),
        "phase_map_2": phase(analysis["phase_map_2_wash_cost_by_tau"]),
        "tau_star_check": analysis["tau_star_check"],
    }


def write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1, allow_nan=False) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {rel(path)} ({path.stat().st_size:,} bytes)")


def main() -> None:
    disable_power_throttling()
    frozen = freeze_spec(SPEC)
    scenarios = {row["name"]: row for row in frozen["scenarios"]}
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=len(SCENARIOS) + 1, initializer=disable_power_throttling) as pool:
        ai_future = pool.submit(run_ai_snapshot, frozen["spec"]["market"])
        futures = {name: pool.submit(run_scenario, name, scenarios[name]) for name in SCENARIOS}
        runs = {name: future.result() for name, future in futures.items()}
        ai = ai_future.result()
    print(f"9 runs in {time.perf_counter() - started:.0f} s; "
          + ", ".join(f"{name} {run.pop('seconds')} s" for name, run in [*runs.items(), ("ai_washing", ai)]))
    main_config, main_domain, _ = _inputs(scenarios["B"], SEED)
    ai_domain = load_domain(AI_DOMAIN)
    # Each run_id hashes the model source (src/abm); these two hashes cover the export code itself.
    reference = ROOT / "showcase" / "sandbox" / "reference.py"
    origin = {"generated_by": rel(Path(__file__)), "script_sha256": sha256(Path(__file__)),
              "reference": rel(reference), "reference_sha256": sha256(reference), "seed": SEED, "snapshot_day": SNAPSHOT_DAY,
              "experiment_spec": rel(SPEC), "experiment_spec_sha256": sha256(SPEC)}
    domains = {"esg": {"scenario": SNAPSHOT_SOURCE, "run_id": runs[SNAPSHOT_SOURCE]["run_id"],
                       **domain_payload(main_domain, main_config), "firms": runs[SNAPSHOT_SOURCE]["snapshot"]}}
    domains["ai_washing"] = {"scenario": ai["scenario"], "run_id": ai["run_id"], "domain_file": rel(AI_DOMAIN),
                             "domain_file_sha256": sha256(AI_DOMAIN), **domain_payload(ai_domain, main_config), "firms": ai["snapshot"]}
    write(ROOT / "showcase" / "data" / "sandbox_firms.json", {"schema_version": 1, **origin, "domains": domains})
    full = {name: {key: value for key, value in run.items() if key != "snapshot"} for name, run in runs.items()}
    write(HERE / "full_model_seed51001.json", {"schema_version": 1, **origin, "domain": main_domain.name,
                                               "runs": full, "ai_washing": {key: ai[key] for key in ("run_id", "benefit_by_decision_day")}})
    write(ROOT / "showcase" / "data" / "stage_f.json", stage_f_payload())


if __name__ == "__main__":
    main()
