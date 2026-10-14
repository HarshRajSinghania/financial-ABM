"""How much washing runs into caps the model does not price: the per-period change cap and the score ceiling.

Reads archived result.npz files of the stage B grid and the instrumented records in runs/. Under the latent
quantile link investors respond linearly to the latent report, while the observable score saturates at the raw
maximum (research contract section 14 lists that saturation as unmodelled). No simulation is run.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import diagnose

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOMAIN = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine.json"
SCENARIOS = ("market_B", "market_F", "market_I_mid", "equal_cost_B", "zero_fine_B")


def main():
    from abm.disclosure.domain import load_domain

    domain = load_domain(DOMAIN)
    # Latent reports above this map to the raw maximum.
    ceiling = float(domain.to_goodness(np.array([domain.raw_upper]))[0])
    frozen = json.loads((diagnose.GRID / "experiment.json").read_text(encoding="utf-8"))
    seeds = frozen["spec"]["seeds"]
    period = frozen["spec"]["market"].get("firm_decision_interval", 60)
    bound = domain.goodness_bounds[1]
    report = {}
    for name in SCENARIOS:
        firm_days, above_days, washes, above_washes, near_bound, final_inflation = 0, 0, 0, 0, 0, []
        for seed in seeds:
            with np.load(diagnose.GRID / name / f"seed_{seed}" / "attempt_001" / "result.npz") as bundle:
                latent = bundle["true_goodness"] + bundle["inflation"]
                days = np.arange(bundle["actions"].shape[0]) * period
                window = days >= diagnose.POLICY_START
                wash = bundle["actions"][window] == 1
                at_decision = latent[days[window]]
                firm_days += latent[diagnose.POLICY_START:].size
                above_days += int((latent[diagnose.POLICY_START:] > ceiling).sum())
                washes += int(wash.sum())
                above_washes += int((wash & (at_decision > ceiling)).sum())
                near_bound += int((wash & (at_decision > bound - domain.max_change_per_period)).sum())
                final_inflation.append(float(bundle["inflation"][-1].mean()))
        report[name] = {
            "firm_day_share_report_above_raw_maximum": above_days / firm_days,
            "wash_decisions": washes,
            "wash_share_made_with_report_above_raw_maximum": above_washes / washes if washes else None,
            "wash_share_within_one_cap_of_latent_bound": near_bound / washes if washes else None,
            "final_mean_inflation_sd": float(np.mean(final_inflation)),
        }
        if (HERE / "runs" / f"{name}_{seeds[0]}.npz").exists():
            r = diagnose.load(name, seeds)
            in_window = r["decision_day"] >= diagnose.POLICY_START
            wash = in_window & (r["action"] == 1)
            improve = in_window & (r["action"] == 0)
            cap = domain.max_change_per_period * (1 - 1e-12)
            report[name].update({
                "wash_share_at_period_cap": float((wash & (r["amount"] >= cap)).sum() / wash.sum()) if wash.any() else None,
                "wash_share_joining_an_open_case": float((wash & (r["opens_case"] == 0)).sum() / wash.sum()) if wash.any() else None,
                "mean_wash_amount_sd": float(r["amount"][wash].mean()) if wash.any() else None,
                "mean_improve_amount_sd": float(r["amount"][improve].mean()) if improve.any() else None,
            })
    payload = {"latent_score_of_raw_maximum": ceiling, "latent_numerical_bound": bound,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "grid_experiment_id": frozen["experiment_id"], "policy_window_start": diagnose.POLICY_START,
               "report": report}
    (HERE / "saturation.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                          encoding="utf-8")
    print(json.dumps(payload, indent=1))


if __name__ == "__main__":
    main()
