"""Why do NPV firms never wash? Record every decision's inputs in archived development runs and decompose.

Re-runs selected trials of the CSI300 main-setting development grid with a read-only wrapper around
``npv_choices``; each run's result fingerprint must equal the archived one. Decomposition and critical
values are conditional on the realized states, not new equilibria; nothing here changes a parameter.
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import game  # noqa: E402
from abm.disclosure.experiments import _inputs  # noqa: E402
from abm.disclosure.financing import financing_signal_factors  # noqa: E402

GRID = ROOT / "reports/disclosure_csi300_quantile_copula_development_20261012_v1"
SCENARIOS = ("market_B", "market_I", "market_F", "market_IF", "zero_taste_B")
SEEDS = (23001, 23002, 23003)
POLICY_START = 601
FIELDS = ("decision_day", "benefit", "marginal_cost", "real_annuity", "displaced_annuity", "wash_annuity",
          "detection", "transparency", "penalty", "subsidy", "audit_probability", "improve_cap", "inflate_cap",
          "action")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replicate(r):
    """Exact copy of the npv_choices value formulas, from recorded inputs."""
    b, c, w = r["benefit"], r["marginal_cost"], r["wash_cost_ratio"]
    improve_benefit = b * r["real_annuity"]
    improve_gain = improve_benefit + r["subsidy"]
    gross = b * (1.0 - r["transparency"]) * r["wash_annuity"]
    fine = r["penalty"] * r["detection"]
    inflate_gain = np.maximum(gross - fine, 0.0)
    wash_cost = w * c
    displaced_benefit = b * r["displaced_annuity"]
    displaced_gain = displaced_benefit + r["subsidy"]
    improve_amount = np.minimum(r["improve_cap"], np.maximum(np.minimum(improve_gain / (2 * c), r["inflate_cap"]),
                                                            displaced_gain / (2 * c)))
    inflate_amount = np.minimum(inflate_gain / (2 * wash_cost), r["inflate_cap"])
    real_value = (improve_benefit * np.minimum(improve_amount, r["inflate_cap"])
                  + displaced_benefit * np.maximum(improve_amount - r["inflate_cap"], 0.0))
    values = np.stack((real_value + r["subsidy"] * improve_amount - c * improve_amount**2,
                       inflate_gain * inflate_amount - wash_cost * inflate_amount**2, np.zeros_like(b)), axis=-1)
    actions = np.argmax(values, axis=-1)
    actions[np.take_along_axis(values, actions[..., None], -1)[..., 0] <= game.MINIMUM_NPV] = game.MAINTAIN
    return values, actions, gross, fine, improve_gain


def summarize(r, mask):
    values, actions, gross, fine, improve_gain = replicate(r)
    w = r["wash_cost_ratio"]
    sel = mask & np.isfinite(r["benefit"])
    n = int(sel.sum())
    positive_benefit = sel & (r["benefit"] > 0)
    wash_positive = sel & (gross > fine)
    # Unconstrained comparison: wash beats improve iff (gross - fine) > sqrt(w) * improve_gain.
    beats = wash_positive & (gross - fine > np.sqrt(w) * improve_gain)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(gross > 0, fine / gross, np.inf)
        critical_penalty = np.where(r["detection"] > 0, gross / r["detection"], np.inf)
        critical_penalty_to_beat = np.where(r["detection"] > 0, (gross - np.sqrt(w) * improve_gain) / r["detection"], np.nan)
        wash_beats_at_zero_fine = sel & (gross > np.sqrt(w) * improve_gain)
        zero_fine_ratio = np.where(improve_gain > 0, gross / (np.sqrt(w) * improve_gain), np.nan)

    def q(x, m):
        x = x[m & np.isfinite(x)]
        return None if x.size == 0 else {p: float(np.quantile(x, p / 100)) for p in (5, 25, 50, 75, 95)}

    return {
        "firm_decisions": n,
        "actions": {name: int(np.sum(sel & (r["action"] == index))) for index, name in enumerate(game.ACTION_NAMES)},
        "replicated_actions_match": bool(np.array_equal(actions[sel], r["action"][sel])),
        "share_benefit_positive": float(positive_benefit.sum() / n) if n else None,
        "share_expected_fine_at_least_gross_wash_benefit": float(np.sum(sel & ~(gross > fine)) / n) if n else None,
        "share_wash_gain_positive_but_dominated": float(np.sum(wash_positive & ~beats) / n) if n else None,
        "share_wash_would_beat_improve_unconstrained": float(beats.sum() / n) if n else None,
        "share_wash_would_beat_improve_if_fine_were_zero": float(wash_beats_at_zero_fine.sum() / n) if n else None,
        "quantiles": {
            "benefit_annual_saving_per_sd_over_cap": q(r["benefit"], sel),
            "gross_wash_benefit": q(gross, sel),
            "expected_fine": q(fine, sel),
            "fine_over_gross": q(ratio, sel),
            "penalty_at_which_gross_equals_fine": q(critical_penalty, sel),
            "penalty_below_which_wash_beats_improve": q(critical_penalty_to_beat, sel),
            "gross_wash_over_sqrt_w_improve_gain": q(zero_fine_ratio, sel),
            "wash_annuity_over_real_annuity": q(r["wash_annuity"] / r["real_annuity"], sel & (r["real_annuity"] > 0)),
            "detection_factor": q(r["detection"], sel),
            "marginal_cost": q(r["marginal_cost"], sel),
            "inflate_capacity": q(r["inflate_cap"], sel),
        },
    }


def main():
    OUT = HERE / "runs"
    OUT.mkdir(exist_ok=False)
    spec = json.loads((GRID / "experiment.json").read_text(encoding="utf-8"))
    archived = {(row["scenario"], row["seed"]): row for row in json.loads((GRID / "summary.json").read_text(encoding="utf-8"))["records"]}
    scenarios = {row["name"]: row for row in spec["scenarios"]}
    original = game.npv_choices
    pooled = {}
    runs = []
    for name in SCENARIOS:
        for seed in SEEDS:
            config, domain, policy = _inputs(scenarios[name], seed)
            records = []

            def wrapped(**kwargs):
                regime, dom = kwargs["regime"], kwargs["domain"]
                delay = dom.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
                factors = financing_signal_factors(
                    kwargs["cost_of_capital"], decision_day=kwargs["decision_day"], horizon_days=kwargs["horizon_days"],
                    repricing_interval=kwargs["repricing_interval"], period_days=kwargs["period_days"],
                    implementation_delay=dom.implementation_delay_days, disclosure_delay=delay,
                    audit_probability=regime.audit_probability, transparency=regime.transparency,
                    publish_audit_results=regime.publish_audit_results, published_now=kwargs["published_now"],
                    reporting_interval_days=regime.reporting_interval_days)
                choices = original(**kwargs)
                size = kwargs["benefit"].size
                cap = dom.max_change_per_period
                records.append({
                    "decision_day": np.full(size, kwargs["decision_day"], dtype=float),
                    "benefit": np.array(kwargs["benefit"], dtype=float), "marginal_cost": np.array(kwargs["marginal_cost"]),
                    "real_annuity": np.array(factors[0], dtype=float), "displaced_annuity": np.array(factors[1], dtype=float),
                    "wash_annuity": np.array(factors[2], dtype=float), "detection": np.broadcast_to(factors[3], (size,)).astype(float),
                    "transparency": np.full(size, regime.transparency), "penalty": np.full(size, regime.penalty),
                    "subsidy": np.full(size, regime.subsidy), "audit_probability": np.full(size, regime.audit_probability),
                    "improve_cap": np.clip(kwargs["improve_capacity"], 0.0, cap), "inflate_cap": np.clip(kwargs["inflate_capacity"], 0.0, cap),
                    "action": choices.actions.astype(float)})
                return choices

            game.npv_choices = wrapped
            try:
                result = game.run_disclosure(config, domain, policy)
            finally:
                game.npv_choices = original
            fingerprint = result.fingerprint()
            expected = archived[(name, seed)]["result_fingerprint"]
            if fingerprint != expected:
                raise RuntimeError(f"instrumented run differs from archive: {name} {seed}")
            stacked = {field: np.stack([row[field] for row in records]) for field in FIELDS}
            stacked["action"] = stacked["action"].astype(np.int64)
            target = OUT / f"{name}_{seed}.npz"
            with target.open("xb") as handle:
                np.savez_compressed(handle, **stacked)
            stacked["wash_cost_ratio"] = domain.wash_cost_ratio
            runs.append({"scenario": name, "seed": seed, "fingerprint_matches_archive": True, "decisions": len(records),
                         "artifact": target.name, "artifact_sha256": sha(target)})
            pooled.setdefault(name, []).append(stacked)
            print(name, seed, "fingerprint OK", flush=True)
    summary = {}
    for name, items in pooled.items():
        merged = {field: np.concatenate([item[field] for item in items]) for field in FIELDS}
        merged["wash_cost_ratio"] = items[0]["wash_cost_ratio"]
        merged["action"] = merged["action"].astype(np.int64)
        day = merged["decision_day"]
        summary[name] = {"all_decisions": summarize(merged, np.ones_like(day, dtype=bool)),
                         "policy_window_decisions": summarize(merged, day >= POLICY_START)}
    payload = {"grid": GRID.relative_to(ROOT).as_posix(), "grid_summary_sha256": sha(GRID / "summary.json"),
               "script_sha256": sha(Path(__file__)), "runs": runs, "summary": summary,
               "scope": "Conditional on realized states of the archived runs. Critical values hold other inputs fixed "
                        "and ignore capacity caps and feedback; they are not equilibrium predictions or tuning targets."}
    with (HERE / "diagnosis.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False, default=float)
        handle.write("\n")


if __name__ == "__main__":
    main()
