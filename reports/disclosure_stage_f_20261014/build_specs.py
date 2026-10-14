"""Stage F: write the development and confirmatory grid specs (research contract section 20).

Both specs share every scenario, comparison and analysis setting; only name, purpose and seeds differ.
Writes configs/disclosure_stage_f_development_v1.json and configs/disclosure_stage_f_confirmatory_v1.json.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
F1 = 4.5614908036639594e-05      # 1000 万元 fixed fine in model units (contract 16.2)
P1 = F1                          # proportional fine per SD equal to F1 for an average firm (contract 20.2)
TASTE = 0.0724                   # contract 18.6
BOOK_SIGMA = 1.2984286951303177  # contract 14, pre-declared control
SWITCH = 1201

MARKET = {
    "n_investors": 1000, "n_firms": 200, "trading_days": 3500, "burn_in_days": 1200,
    "initial_impact_share": 0.2, "taste_median": TASTE, "imitation_rule": "pairwise",
    "financing_exposure_fraction": 0.5, "financing_spread": 0.05, "financing_repricing_interval": 60,
    "financing_horizon_days": 1260, "firm_discount_rate": 0.05, "intrinsic_value_log_sd": 0.9151544344205937,
}
POLICIES = {"B": {}, "I": {"transparency": 0.6}, "F": {"fixed_fine": 4 * F1},
            "IF": {"transparency": 0.6, "fixed_fine": 4 * F1}}


def scenario(name: str, changes: dict | None = None, *, market: dict | None = None, domain: dict | None = None,
             baseline: dict | None = None) -> dict:
    row: dict = {"name": name}
    if market:
        row["market"] = market
    if domain:
        row["domain"] = domain
    policy: dict = {}
    if baseline:
        policy["baseline"] = baseline
    if changes:
        policy.update({"start_day": SWITCH, "changes": changes})
    if policy:
        row["policy"] = policy
    return row


def label(value: float) -> str:
    return f"{value:g}".replace(".", "p")


def scenarios() -> list[dict]:
    rows = []
    # A. Main comparison: market on and off (taste 0, initial II probability kept at 0.2).
    for name, changes in POLICIES.items():
        rows.append(scenario(name, changes))
    for name, changes in POLICIES.items():
        rows.append(scenario(f"off_{name}", changes, market={"taste_median": 0.0}))
    # B. Dose-response: transparency, fixed fine multiples, proportional fine multiples (fixed fine removed).
    for tau in (0.3, 0.5, 0.7, 0.8):
        rows.append(scenario(f"I_{label(tau)}", {"transparency": tau}))
    for multiple in (0, 2, 8):
        rows.append(scenario(f"F_{multiple}x", {"fixed_fine": multiple * F1}))
    for multiple in (1, 2, 4):
        rows.append(scenario(f"P_{multiple}x", {"fixed_fine": 0.0, "penalty": multiple * P1}))
    # C. Size identification: equal cost multipliers.
    for name, changes in POLICIES.items():
        rows.append(scenario(f"eqcost_{name}", changes, domain={"size_cost_multipliers": [1.0, 1.0, 1.0]}))
    # D. Null controls.
    rows.append(scenario("zeroII_B", market={"initial_impact_share": 0.0}))
    rows.append(scenario("null_control", market={"taste_median": 0.0},
                         baseline={"audit_probability": 0.0, "transparency": 0.0, "fixed_fine": 0.0, "penalty": 0.0}))
    # E. Decay sensitivity.
    for name, changes in POLICIES.items():
        rows.append(scenario(f"decay0_{name}", changes, domain={"natural_decay": 0.0}))
    # F. Initialization controls (contract 14): independent copula, book-equity value dispersion.
    for name in ("B", "I", "F"):
        rows.append(scenario(f"indep_{name}", POLICIES[name], domain={"initial_size_rank_correlation": 0.0}))
    for name in ("B", "I", "F"):
        rows.append(scenario(f"booksd_{name}", POLICIES[name], market={"intrinsic_value_log_sd": BOOK_SIGMA}))
    # G. Phase map 1: taste x initial II probability under B. Reuses B, off_B and zeroII_B.
    reused = {(TASTE, 0.2), (0.0, 0.2), (TASTE, 0.0)}
    for taste in (0.0, TASTE / 2, TASTE, 2 * TASTE):
        for share in (0.0, 0.2, 0.5, 0.8):
            if (taste, share) not in reused:
                rows.append(scenario(f"pm1_t{label(round(taste, 4))}_s{label(share)}",
                                     market={"taste_median": taste, "initial_impact_share": share}))
    # H. Phase map 2: wash cost ratio x transparency (switch at 1201). Reuses w = 0.2: B, I_0p3, I, I_0p8.
    for ratio in (0.05, 0.1, 0.4):
        for tau in (0.1, 0.3, 0.6, 0.8):
            changes = None if tau == 0.1 else {"transparency": tau}
            rows.append(scenario(f"pm2_w{label(ratio)}_tau{label(tau)}", changes, domain={"wash_cost_ratio": ratio}))
    return rows


def comparisons() -> list[dict]:
    rows = [
        {"name": "P1_market_full_period", "weights": {"B": 1, "off_B": -1}, "primary": True,
         "primary_metric": "full_period_change.equal_weight_sd"},
        {"name": "P2_I_minus_F", "weights": {"I": 1, "F": -1}, "primary": True},
        {"name": "P3_interaction", "weights": {"IF": 1, "B": -1, "off_IF": -1, "off_B": 1}, "primary": True},
        {"name": "P4_size_cost_gap", "weights": {"B": 1, "eqcost_B": -1}, "primary": True,
         "primary_metric": "size.large_minus_small_sd"},
    ]

    def add(name, plus, minus):
        rows.append({"name": name, "weights": {plus: 1, minus: -1}})

    for prefix in ("", "off_", "eqcost_", "decay0_"):
        for policy in ("I", "F", "IF"):
            add(f"{prefix}{policy}_minus_B", f"{prefix}{policy}", f"{prefix}B")
    for prefix in ("off_", "eqcost_", "decay0_", "indep_", "booksd_"):
        add(f"{prefix}I_minus_F", f"{prefix}I", f"{prefix}F")
    for prefix in ("indep_", "booksd_"):
        for policy in ("I", "F"):
            add(f"{prefix}{policy}_minus_B", f"{prefix}{policy}", f"{prefix}B")
    for tau in (0.3, 0.5, 0.7, 0.8):
        add(f"I_{label(tau)}_minus_B", f"I_{label(tau)}", "B")
    for multiple in (0, 2, 8):
        add(f"F_{multiple}x_minus_B", f"F_{multiple}x", "B")
    for multiple in (1, 2, 4):
        add(f"P_{multiple}x_minus_B", f"P_{multiple}x", "B")
    add("P_1x_minus_fixed_1x", "P_1x", "B")
    add("P_2x_minus_fixed_2x", "P_2x", "F_2x")
    add("P_4x_minus_fixed_4x", "P_4x", "F")
    add("F_size_cost_gap", "F", "eqcost_F")
    add("decay0_B_minus_B", "decay0_B", "B")
    return rows


METRICS = [
    "true_change.equal_weight_sd", "true_change.fixed_start_cap_weight_sd", "decay_adjusted_gain.equal_weight_sd",
    "full_period_change.equal_weight_sd", "inflation.mean_sd", "size.large_minus_small_sd",
    "terminal_year.change_from_initial_sd", "terminal_year.decay_adjusted_from_initial_sd",
    "terminal_year.inflation_mean_sd", "costs.resource_cost_fraction_initial_cap",
    "costs.private_net_outflow_fraction_initial_cap", "costs.fine_transfer_fraction_initial_cap",
    "impact.final_share",
]


def spec(purpose: str, seeds: list[int]) -> dict:
    return {
        "name": f"disclosure_stage_f_{purpose}_v1", "purpose": purpose, "archive": "compact",
        "_note": "Plan stage F (research contract section 20). Development and confirmatory specs differ only in "
                 "name, purpose and seeds; the development run checks the pipeline and may not change the design.",
        "domain": "domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json",
        "market": MARKET, "seeds": seeds, "scenarios": scenarios(), "comparisons": comparisons(),
        "analysis": {"primary_metric": "true_change.equal_weight_sd", "metrics": METRICS, "confidence_level": 0.95},
    }


def main() -> None:
    for purpose, seeds in (("development", [33001, 33002, 33003]), ("confirmatory", list(range(41001, 41031)))):
        path = ROOT / "configs" / f"disclosure_stage_f_{purpose}_v1.json"
        path.write_text(json.dumps(spec(purpose, seeds), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(path, len(spec(purpose, seeds)["scenarios"]), "scenarios", len(comparisons()), "comparisons")


if __name__ == "__main__":
    main()
