"""Stage G.2-G.3: cross-language fixtures for the sandbox core (showcase/sandbox/core.js).

  .venv/Scripts/python.exe reports/disclosure_stage_g_20261015/fixtures.py

Every expected value comes from the Python model code: ``npv_choices``, ``financing_signal_factors``
and ``new_case_probability`` from src/abm/disclosure, and the simplified dynamics of
showcase/sandbox/reference.py on the exported snapshot firms. ``node showcase/sandbox/check_core.js``
must reproduce the choices exactly and every number to a relative error of 1e-12;
tests/test_sandbox_reference.py checks that the committed fixtures still match the model code.

Writes showcase/sandbox/fixtures/core_cases.json and dynamics_cases.json.
"""

from __future__ import annotations

import json
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "showcase" / "sandbox"))

from abm.disclosure.financing import financing_signal_factors  # noqa: E402
from abm.disclosure.game import new_case_probability, npv_choices  # noqa: E402
from abm.disclosure.policy import PolicyRegime  # noqa: E402
from reference import (  # noqa: E402
    Mulberry32, decide, domain_from, firms_from, schedule_from, simulate, snapshot_state, window_metrics,
)

OUT = ROOT / "showcase" / "sandbox" / "fixtures"
INPUT_SEED = 51002          # draws test inputs only; not a model run
REGIMES, FIRMS_PER_REGIME = 60, 20
F1 = 4.5614908036639594e-05  # 1000 万元 in model units (contract 16.2)


def floats(values) -> list:
    return [float(v) for v in np.asarray(values, dtype=np.float64).ravel()]


def regime_dict(regime: PolicyRegime) -> dict:
    return {"audit_probability": regime.audit_probability, "penalty": regime.penalty, "transparency": regime.transparency,
            "subsidy": regime.subsidy, "fixed_fine": regime.fixed_fine, "disclosure_delay_days": regime.disclosure_delay_days}


def log_uniform(rng, low, high, size=None):
    return np.exp(rng.uniform(np.log(low), np.log(high), size))


def decision_cases(rng, domain) -> list:
    cases = []
    for _ in range(REGIMES):
        period = int(rng.choice([20, 60, 90]))
        timing = {
            "period_days": period, "repricing_interval": int(rng.choice([20, 60, 120])),
            "horizon_days": int(rng.choice([252, 1260])),
            "decision_day": int(rng.integers(1, 59)) * period if rng.random() < 0.5 else int(rng.integers(0, 3500)),
            "discount_rate": 0.05 if rng.random() < 0.5 else float(rng.uniform(0.01, 0.15)),
        }
        case_domain = replace(domain, wash_cost_ratio=float(rng.uniform(0.05, 0.5)),
                              max_change_per_period=float(rng.uniform(0.05, 0.5)),
                              implementation_delay_days=int(rng.choice([0, 60, 120, 180])),
                              disclosure_delay_days=int(rng.choice([0, 10, 20, 90])))
        regime = PolicyRegime(
            audit_probability=float(rng.choice([0.0, 0.01, rng.uniform(0, 0.3)])),
            transparency=float(rng.choice([0.1, 0.6, rng.uniform(0, 1)])),
            penalty=0.0 if rng.random() < 0.5 else float(log_uniform(rng, 1e-6, 1e-2)),
            subsidy=0.0 if rng.random() < 0.7 else float(rng.uniform(0, 1e-3)),
            fixed_fine=0.0 if rng.random() < 0.4 else float(rng.uniform(0, 8 * F1)),
            disclosure_delay_days=None if rng.random() < 0.7 else int(rng.choice([1, 30, 120])),
        )
        n = FIRMS_PER_REGIME
        benefit = log_uniform(rng, 1e-6, 1e-2, n)
        benefit[rng.random(n) < 0.05] = 0.0
        marginal_cost = log_uniform(rng, 1e-3, 1.0, n)
        improve_capacity = rng.uniform(-0.1, 0.6, n)
        inflate_capacity = np.minimum(improve_capacity, rng.uniform(-0.1, 0.6, n))
        new_case_fine = None
        if regime.fixed_fine:
            probability = rng.choice([0.0, 1.0, rng.uniform()], size=n)
            new_case_fine = regime.fixed_fine / log_uniform(rng, 0.05, 20.0, n) * probability
        delay = case_domain.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
        rate = np.full(n, timing["discount_rate"])
        factors = financing_signal_factors(
            rate, decision_day=timing["decision_day"], horizon_days=timing["horizon_days"],
            repricing_interval=timing["repricing_interval"], period_days=period,
            implementation_delay=case_domain.implementation_delay_days, disclosure_delay=delay,
            audit_probability=regime.audit_probability, transparency=regime.transparency,
        )
        choices = npv_choices(
            benefit=benefit, cost_of_capital=rate, marginal_cost=marginal_cost, regime=regime, domain=case_domain,
            period_days=period, improve_capacity=improve_capacity, inflate_capacity=inflate_capacity,
            horizon_days=timing["horizon_days"], repricing_interval=timing["repricing_interval"],
            decision_day=timing["decision_day"], new_case_fine=new_case_fine,
        )
        cases.append({
            **timing, "regime": regime_dict(regime),
            "domain": {key: getattr(case_domain, key) for key in ("wash_cost_ratio", "max_change_per_period",
                                                                  "implementation_delay_days", "disclosure_delay_days")},
            "inputs": {"benefit": floats(benefit), "marginal_cost": floats(marginal_cost),
                       "improve_capacity": floats(improve_capacity), "inflate_capacity": floats(inflate_capacity),
                       "new_case_fine": None if new_case_fine is None else floats(new_case_fine)},
            "expected": {"factors": [float(f[0]) for f in factors], "actions": choices.actions.astype(int).tolist(),
                         "amounts": floats(choices.amounts), "npv": floats(choices.npv),
                         "cost_fraction": floats(choices.cost_fraction), "subsidy_fraction": floats(choices.subsidy_fraction)},
        })
    return cases


def new_case_cases(rng) -> list:
    cases = []
    for _ in range(100):
        n, period = 12, int(rng.choice([20, 60]))
        day = int(rng.integers(0, 40)) * period + int(rng.integers(0, period))
        wash_due = day + int(rng.choice([1, 20, 90, 200]))
        inflation = np.where(rng.random(n) < 0.5, rng.uniform(0, 1, n), 0.0)
        pending = []
        for _ in range(int(rng.integers(0, 5))):
            firms = np.sort(rng.choice(n, size=int(rng.integers(1, n)), replace=False))
            amounts = np.where(rng.random(firms.size) < 0.8, rng.uniform(0, 0.2, firms.size), 0.0)
            pending.append((day + int(rng.integers(-30, 250)), int(rng.integers(0, 2)), firms, amounts))
        audit = float(rng.choice([0.0, 0.01, 0.3]))
        expected = new_case_probability(inflation, pending, decision_day=day, wash_due=wash_due,
                                        period_days=period, audit_probability=audit)
        cases.append({"decision_day": day, "wash_due": wash_due, "period_days": period, "audit_probability": audit,
                      "inflation": floats(inflation),
                      "pending": [{"due_day": d, "kind": k, "firms": f.astype(int).tolist(), "amounts": floats(a)}
                                  for d, k, f, a in pending],
                      "expected": floats(expected)})
    return cases


def prng_cases() -> list:
    rows = []
    for seed in (0, 1, 51001, 2**32 - 1):
        rng = Mulberry32(seed)
        rows.append({"seed": seed, "values": [rng.random() for _ in range(1000)]})
    return rows


def dynamics_cases(sandbox: dict, domains: dict) -> dict:
    base = {key: dict(sandbox["domains"][key]["baseline_policy"], disclosure_delay_days=None) for key in domains}

    def schedule(key, **changes):
        if not changes:
            return {"baseline": base[key], "intervention": None, "start_day": 0}
        return {"baseline": base[key], "intervention": dict(base[key], **changes), "start_day": 1201}

    runs = [
        ("esg", "B", schedule("esg"), 0.2, 1), ("esg", "I", schedule("esg", transparency=0.6), 0.2, 1),
        ("esg", "F", schedule("esg", fixed_fine=4 * F1), 0.2, 7),
        ("esg", "IF", schedule("esg", transparency=0.6, fixed_fine=4 * F1), 0.0, 1),
        ("esg", "P_4x", schedule("esg", fixed_fine=0.0, penalty=4 * F1), 0.2, 3),
        ("esg", "B_decay0", schedule("esg"), 0.0, 2),
        ("esg", "audit_20pct", schedule("esg", audit_probability=0.2), 0.35, 5),
        ("esg", "subsidy", schedule("esg", subsidy=2e-4, transparency=0.3), 0.1, 11),
        ("ai_washing", "baseline", schedule("ai_washing"), 0.3, 1),
        ("ai_washing", "no_fine", schedule("ai_washing", penalty=0.0), 0.3, 4),
    ]
    traces = []
    for key, name, policy, decay, seed in runs:
        firms = firms_from(sandbox["domains"][key]["firms"])
        run = simulate(firms, domains[key], schedule_from(policy), natural_decay=decay, audit_seed=seed)
        periods = [{"day": int(day), "actions": "".join(map(str, run["actions"][k])),
                    "amount_sum": float(run["amounts"][k].sum()), "detections": int(run["detections"][k].sum()),
                    "fine_sum": float(run["fine_fraction"][k].sum()),
                    "mean_goodness": float(run["mean_goodness"][day]), "mean_inflation": float(run["mean_inflation"][day])}
                   for k, day in enumerate(run["decision_days"])]
        traces.append({"domain": key, "name": name, "policy": policy, "natural_decay": decay, "audit_seed": seed,
                       "periods": periods, "final_goodness": floats(run["final_goodness"]),
                       "final_inflation": floats(run["final_inflation"]), "metrics": window_metrics(run, firms)})
    # The reference decision on the snapshot state must equal the decision the full model took.
    for key in domains:
        payload = sandbox["domains"][key]
        choices, _ = decide(snapshot_state(payload["firms"], domains[key]), firms_from(payload["firms"]), domains[key],
                            schedule_from({"baseline": base[key]}).baseline, sandbox["snapshot_day"])
        recorded = payload["firms"]["full_model_decision"]
        if choices.actions.tolist() != recorded["actions"] or not np.allclose(choices.amounts, recorded["amounts"], rtol=1e-12, atol=0):
            raise RuntimeError(f"{key}: the reference decision differs from the full model's snapshot-day decision")
    return {"runs": traces}


def write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, separators=(",", ":"), allow_nan=False) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(ROOT).as_posix()} ({path.stat().st_size:,} bytes)")


def build() -> tuple[dict, dict]:
    sandbox = json.loads((ROOT / "showcase" / "data" / "sandbox_firms.json").read_text(encoding="utf-8"))
    # Exported domain parameters: the CSI 300 domain file is vendor-derived and not in the repository.
    domains = {key: domain_from(payload) for key, payload in sandbox["domains"].items()}
    rng = np.random.default_rng(INPUT_SEED)
    note = "Expected values from the Python model code; see reports/disclosure_stage_g_20261015/fixtures.py."
    core = {"schema_version": 1, "note": note, "input_seed": INPUT_SEED,
            "decisions": decision_cases(rng, domains["esg"]), "new_case": new_case_cases(rng), "prng": prng_cases()}
    return core, {"schema_version": 1, "note": note, **dynamics_cases(sandbox, domains)}


def main() -> None:
    core, dynamics = build()
    write(OUT / "core_cases.json", core)
    write(OUT / "dynamics_cases.json", dynamics)


if __name__ == "__main__":
    main()
