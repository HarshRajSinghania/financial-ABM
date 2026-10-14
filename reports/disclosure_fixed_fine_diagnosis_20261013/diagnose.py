"""Stage B instrumented diagnosis: does washing occur, does it rise with size, is the transparency transition gradual?

Re-runs selected trials of the stage B development grid with a read-only wrapper around ``npv_choices`` and
records every decision's inputs, the probability that a new report opens a case, and the firm's market cap.
Each instrumented run's result fingerprint must equal the archived one, and the recorded inputs must
reproduce every archived choice. Frontiers recompute the choice on fixed recorded states (no feedback, no new
market path); closed forms are the propositions in docs/disclosure_inspection_propositions.md. Nothing here
changes a parameter.

Usage: python diagnose.py [--workers N]   (writes runs/*.npz and diagnosis.json; refuses to overwrite)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import game  # noqa: E402
from abm.disclosure.experiments import _inputs  # noqa: E402
from abm.disclosure.financing import financing_signal_factors  # noqa: E402

GRID = ROOT / "reports/disclosure_csi300_fixed_fine_development_20261013_v1"
SCENARIOS = ("market_B", "market_I", "market_F", "proportional_B", "equal_cost_B")
POLICY_START = 1201
SIZE_NAMES = ("large", "mid", "small")
FIELDS = ("decision_day", "size_class", "price", "benefit", "marginal_cost", "real", "displaced", "wash",
          "detection", "transparency", "penalty", "fixed_fine", "subsidy", "opens_case", "case_fine",
          "improve_cap", "inflate_cap", "action", "amount")
TAU_GRID = np.round(np.arange(0.0, 0.7001, 0.025), 3)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def instrumented(scenario: dict, seed: int, expected: str) -> dict:
    config, domain, policy = _inputs(scenario, seed)
    market = game.DisclosureMarket(config, domain, policy)
    original, rows = game.npv_choices, []

    def wrapped(**kwargs):
        regime, dom = kwargs["regime"], kwargs["domain"]
        delay = dom.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
        day, size = kwargs["decision_day"], kwargs["benefit"].size
        real, displaced, wash, detection = financing_signal_factors(
            kwargs["cost_of_capital"], decision_day=day, horizon_days=kwargs["horizon_days"],
            repricing_interval=kwargs["repricing_interval"], period_days=kwargs["period_days"],
            implementation_delay=dom.implementation_delay_days, disclosure_delay=delay,
            audit_probability=regime.audit_probability, transparency=regime.transparency,
            publish_audit_results=regime.publish_audit_results, published_now=kwargs["published_now"],
            reporting_interval_days=regime.reporting_interval_days)
        opens = game.new_case_probability(market.attributes.inflation, market.attributes.pending, decision_day=day,
                                          wash_due=day + max(1, delay), period_days=kwargs["period_days"],
                                          audit_probability=regime.audit_probability)
        choices = original(**kwargs)
        cap = dom.max_change_per_period
        case_fine = kwargs.get("new_case_fine")
        rows.append({
            "decision_day": np.full(size, day, dtype=float), "size_class": market.firms.size_class.astype(float),
            "price": market.prices.copy(), "benefit": np.array(kwargs["benefit"], dtype=float),
            "marginal_cost": np.array(kwargs["marginal_cost"], dtype=float),
            "real": np.asarray(real, dtype=float), "displaced": np.asarray(displaced, dtype=float),
            "wash": np.asarray(wash, dtype=float), "detection": np.broadcast_to(detection, (size,)).astype(float),
            "transparency": np.full(size, regime.transparency), "penalty": np.full(size, regime.penalty),
            "fixed_fine": np.full(size, regime.fixed_fine), "subsidy": np.full(size, regime.subsidy),
            "opens_case": opens, "case_fine": np.zeros(size) if case_fine is None else np.array(case_fine, dtype=float),
            "improve_cap": np.clip(kwargs["improve_capacity"], 0.0, cap),
            "inflate_cap": np.clip(kwargs["inflate_capacity"], 0.0, cap),
            "action": choices.actions.astype(float), "amount": choices.amounts.copy(),
        })
        return choices

    game.npv_choices = wrapped
    try:
        result = market.run()
    finally:
        game.npv_choices = original
    if result.fingerprint() != expected:
        raise RuntimeError(f"instrumented run differs from archive: {scenario['name']} {seed}")
    target = HERE / "runs" / f"{scenario['name']}_{seed}.npz"
    stacked = {field: np.stack([row[field] for row in rows]) for field in FIELDS}
    with target.open("xb") as handle:
        np.savez_compressed(handle, wash_cost_ratio=np.array(domain.wash_cost_ratio), **stacked)
    return {"scenario": scenario["name"], "seed": seed, "fingerprint_matches_archive": True,
            "decision_days": len(rows), "artifact": target.name, "artifact_sha256": sha(target)}


def load(name: str, seeds) -> dict:
    data = []
    for seed in seeds:
        with np.load(HERE / "runs" / f"{name}_{seed}.npz") as bundle:
            data.append({key: bundle[key] for key in bundle.files})
    merged = {field: np.concatenate([item[field] for item in data]) for field in FIELDS}
    merged["wash_cost_ratio"] = float(data[0]["wash_cost_ratio"])
    merged["action"] = merged["action"].astype(np.int64)
    merged["size_class"] = merged["size_class"].astype(np.int64)
    # Old-inflation annuity behind the displaced branch, so it can follow a changed transparency.
    with np.errstate(divide="ignore", invalid="ignore"):
        merged["old_survival"] = np.where(merged["transparency"] < 1,
                                          (merged["real"] - merged["displaced"]) / (1 - merged["transparency"]), 0.0)
    return merged


def replicate(r, *, transparency=None, fine=None, penalty=None):
    """The npv_choices formulas on recorded inputs; ``fine`` replaces the fixed fine in money units."""
    b, c, w, s = r["benefit"], r["marginal_cost"], r["wash_cost_ratio"], r["subsidy"]
    tau = r["transparency"] if transparency is None else np.full_like(b, transparency)
    p = r["penalty"] if penalty is None else np.full_like(b, penalty)
    case_fine = r["case_fine"] if fine is None else fine * r["opens_case"] / r["price"]
    improve_benefit = b * r["real"]
    improve_gain = improve_benefit + s
    inflate_gain = np.maximum(b * (1 - tau) * r["wash"] - p * r["detection"], 0.0)
    wash_cost = w * c
    displaced_benefit = b * (r["real"] - (1 - tau) * r["old_survival"])
    displaced_gain = displaced_benefit + s
    improve_amount = np.minimum(r["improve_cap"], np.maximum(np.minimum(improve_gain / (2 * c), r["inflate_cap"]),
                                                            displaced_gain / (2 * c)))
    inflate_amount = np.minimum(inflate_gain / (2 * wash_cost), r["inflate_cap"])
    real_value = (improve_benefit * np.minimum(improve_amount, r["inflate_cap"])
                  + displaced_benefit * np.maximum(improve_amount - r["inflate_cap"], 0.0))
    wash_value = (inflate_gain * inflate_amount - wash_cost * inflate_amount**2
                  - np.where(inflate_amount > 0, case_fine * r["detection"], 0.0))
    values = np.stack((real_value + s * improve_amount - c * improve_amount**2, wash_value, np.zeros_like(b)), axis=-1)
    actions = np.argmax(values, axis=-1)
    actions[np.take_along_axis(values, actions[..., None], -1)[..., 0] <= game.MINIMUM_NPV] = game.MAINTAIN
    return actions


def closed_forms(r):
    """Proposition 1 size threshold and Proposition 2 firm threshold (s = 0, p = 0, interior)."""
    b, c, w = r["benefit"], r["marginal_cost"], r["wash_cost_ratio"]
    fine = r["fixed_fine"] * r["opens_case"] / r["price"]
    with np.errstate(divide="ignore", invalid="ignore"):
        tau_firm = 1 - np.sqrt(w) * np.sqrt(r["real"]**2 + 4 * c * fine * r["detection"] / b**2) / r["wash"]
        tau_common = 1 - np.sqrt(w) * r["real"] / r["wash"]
        bracket = (1 - r["transparency"])**2 * r["wash"]**2 / w - r["real"]**2
        size_threshold = np.where(bracket > 0, 4 * c * r["fixed_fine"] * r["detection"] / (b**2 * bracket), np.inf)
    return tau_firm, tau_common, size_threshold


def quantiles(x, mask):
    x = x[mask & np.isfinite(x)]
    return None if x.size == 0 else {str(q): float(np.quantile(x, q / 100)) for q in (5, 25, 50, 75, 95)}


def share(mask, within):
    n = int(within.sum())
    return None if n == 0 else float((mask & within).sum() / n)


def scenario_summary(r):
    day, action, size, opens = r["decision_day"], r["action"], r["size_class"], r["opens_case"]
    rows = {}
    for label, window in (("pre_policy", (day > 0) & (day < POLICY_START)), ("policy_window", day >= POLICY_START)):
        wash = action == game.INFLATE
        rows[label] = {
            "firm_decisions": int(window.sum()),
            "wash": int((wash & window).sum()), "improve": int((window & (action == game.IMPROVE)).sum()),
            "wash_share": share(wash, window),
            "wash_share_by_size": {name: share(wash, window & (size == index)) for index, name in enumerate(SIZE_NAMES)},
            "wash_share_opening_a_case": share(wash, window & (opens == 1)),
            "wash_share_joining_an_open_case": share(wash, window & (opens == 0)),
            "decisions_with_open_case": int((window & (opens == 0)).sum()),
        }
    return rows


def size_gradient(r):
    window = r["decision_day"] >= POLICY_START
    first = window & (r["opens_case"] == 1)
    wash = r["action"] == game.INFLATE
    log_cap = np.log(r["price"])
    edges = np.quantile(log_cap[first], np.linspace(0, 1, 11))
    deciles = []
    for low, high in zip(edges[:-1], edges[1:]):
        member = first & (log_cap >= low) & (log_cap <= high)
        deciles.append({"log_cap_low": float(low), "log_cap_high": float(high), "decisions": int(member.sum()),
                        "wash_share": share(wash, member)})
    _, tau_common, threshold = closed_forms(r)
    predicted = first & (r["transparency"] < tau_common) & (r["price"] > threshold)
    # The closed form needs both unconstrained amounts inside their caps.
    wash_amount = (r["benefit"] * (1 - r["transparency"]) * r["wash"] - r["penalty"] * r["detection"]) / (
        2 * r["wash_cost_ratio"] * r["marginal_cost"])
    improve_amount = (r["benefit"] * r["real"] + r["subsidy"]) / (2 * r["marginal_cost"])
    interior = (first & (wash_amount < r["inflate_cap"]) & (improve_amount < r["improve_cap"])
                & (improve_amount <= r["inflate_cap"]))
    fine_share = r["fixed_fine"] / r["price"]
    return {
        "scope": "Policy-window decisions that would open a new case (no undetected inflation).",
        "wash_share_by_log_cap_decile": deciles,
        "fine_over_cap_by_size": {name: quantiles(fine_share, window & (r["size_class"] == index))
                                  for index, name in enumerate(SIZE_NAMES)},
        "proposition_1_threshold_over_cap_by_size": {
            name: quantiles(threshold / r["price"], first & (r["size_class"] == index)) for index, name in enumerate(SIZE_NAMES)},
        "proposition_1_agreement": share(predicted == wash, first),
        "interior_share": share(interior, first),
        "proposition_1_agreement_interior": share(predicted == wash, interior),
    }


def frontier(r, *, label, fine=None, penalty=None, mask=None):
    window = r["decision_day"] >= POLICY_START
    if mask is not None:
        window &= mask
    curve = []
    for tau in TAU_GRID:
        actions = replicate(r, transparency=tau, fine=fine, penalty=penalty)
        curve.append({"transparency": float(tau), "wash_share": share(actions == game.INFLATE, window)})
    shares = np.array([row["wash_share"] for row in curve])
    top = shares[0]
    crossing = {}
    for level in (.9, .5, .1):
        below = np.flatnonzero(shares <= level * top) if top else np.array([], dtype=int)
        crossing[str(level)] = float(TAU_GRID[below[0]]) if below.size else None
    return {"label": label, "decisions": int(window.sum()), "curve": curve,
            "first_transparency_at_or_below_fraction_of_zero_transparency_share": crossing}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    frozen = json.loads((GRID / "experiment.json").read_text(encoding="utf-8"))
    summary = json.loads((GRID / "summary.json").read_text(encoding="utf-8"))
    archived = {(row["scenario"], row["seed"]): row for row in summary["records"]}
    scenarios = {row["name"]: row for row in frozen["scenarios"]}
    seeds = frozen["spec"]["seeds"]
    (HERE / "runs").mkdir(exist_ok=False)
    jobs = [(scenarios[name], seed, archived[(name, seed)]["result_fingerprint"]) for name in SCENARIOS for seed in seeds]
    for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
        os.environ[name] = "1"
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        runs = list(pool.map(instrumented, *zip(*jobs)))
    report = {}
    for name in SCENARIOS:
        r = load(name, seeds)
        replicated = replicate(r)
        entry = {"replicated_actions_match": bool(np.array_equal(replicated, r["action"])),
                 "summary": scenario_summary(r)}
        if name in ("market_B", "equal_cost_B"):
            entry["size_gradient"] = size_gradient(r)
        if name == "market_B":
            tau_firm, tau_common, _ = closed_forms(r)
            window = r["decision_day"] >= POLICY_START
            entry["transparency_thresholds"] = {
                "common_threshold": quantiles(tau_common, window),
                "firm_threshold_opening_a_case_by_size": {
                    size_name: quantiles(tau_firm, window & (r["opens_case"] == 1) & (r["size_class"] == index))
                    for index, size_name in enumerate(SIZE_NAMES)},
            }
            fine = float(r["fixed_fine"][0, 0])
            entry["conditional_frontiers"] = [
                frontier(r, label="fixed fine as recorded, all decisions"),
                frontier(r, label="fixed fine as recorded, decisions opening a case", mask=r["opens_case"] == 1),
                frontier(r, label="fixed fine x4, decisions opening a case", fine=4 * fine, mask=r["opens_case"] == 1),
                frontier(r, label="no fine, all decisions", fine=0.0),
                frontier(r, label="proportional penalty 0.005 and no fixed fine, all decisions", fine=0.0, penalty=0.005),
            ]
        report[name] = entry
    payload = {
        "grid": GRID.relative_to(ROOT).as_posix(), "grid_experiment_id": frozen["experiment_id"],
        "grid_summary_sha256": sha(GRID / "summary.json"), "script_sha256": sha(Path(__file__)),
        "seeds": seeds, "runs": runs, "report": report,
        "scope": ("Conditional on realized states of archived development runs. Frontiers hold each recorded state, "
                  "annuity and capacity fixed and recompute only that decision; they are not market counterfactuals, "
                  "equilibria or calibration targets. Closed forms assume interior amounts, zero subsidy and no "
                  "proportional penalty."),
    }
    with (HERE / "diagnosis.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False, default=float)
        handle.write("\n")
    print(json.dumps({name: {"match": entry["replicated_actions_match"], **entry["summary"]["policy_window"]}
                      for name, entry in report.items()}, indent=1))


if __name__ == "__main__":
    main()
