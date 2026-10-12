"""Array and algebra checks of a fixed action grid; no model imports or market runs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


def main():
    folder = Path(__file__).resolve().parent
    spec_path = folder / "math_spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    path = folder / "math_checks.json"
    if path.exists():
        raise FileExistsError(path)
    fractions = np.asarray(spec["action_fractions"])
    amounts = fractions * spec["max_change_per_period_sd"]
    candidates = np.r_[0., amounts]
    ratios = amounts[1:] / amounts[:-1]
    assert np.all(ratios <= 2) and fractions[-1] == 1
    c = spec["quadratic_cost_coefficient"]
    intervals = []
    for low, high, ratio in zip(amounts[:-1], amounts[1:], ratios, strict=True):
        optimum = np.linspace(low, high, spec["points_per_interval"])
        linear = 2 * c * optimum
        continuous = c * optimum**2
        values = linear[:, None] * candidates - c * candidates**2
        best = values.max(axis=1)
        relative = (continuous - best) / continuous
        bound = ((ratio - 1) / (ratio + 1))**2
        assert np.all(relative <= bound + 1e-13)
        midpoint = (low + high) / 2
        midpoint_values = 2 * c * midpoint * candidates - c * candidates**2
        midpoint_loss = (c * midpoint**2 - midpoint_values.max()) / (c * midpoint**2)
        np.testing.assert_allclose(midpoint_loss, bound, rtol=1e-12, atol=1e-14)
        intervals.append({"lower_amount_sd": float(low), "upper_amount_sd": float(high),
                          "ratio": float(ratio), "relative_loss_bound": float(bound),
                          "sampled_maximum_relative_loss": float(relative.max()),
                          "worst_optimum_sd": float(midpoint)})
    first = amounts[0]
    optimum = np.linspace(0., first, spec["points_per_interval"])
    continuous = c * optimum**2
    values = 2 * c * optimum[:, None] * candidates - c * candidates**2
    regret = continuous - values.max(axis=1)
    absolute_bound = c * first**2 / 4
    assert np.all(regret <= absolute_bound + 1e-18)
    np.testing.assert_allclose(regret.max(), absolute_bound, rtol=1e-12)
    example = spec["report_capacity_counterexample"]
    room = example["report_capacity_sd"]
    real = example["real_value_per_sd"]
    displaced = example["displaced_real_value_per_sd"]
    subsidy = example["subsidy_per_sd"]
    kink_value = real * room + subsidy * room - c * room**2
    kink_values = real * np.minimum(candidates, room) + displaced * np.maximum(candidates - room, 0)
    kink_values += subsidy * candidates - c * candidates**2
    left_derivative, right_derivative = real + subsidy - 2 * c * room, displaced + subsidy - 2 * c * room
    assert left_derivative > 0 and right_derivative < 0
    kink_relative_loss = (kink_value - kink_values.max()) / kink_value
    np.testing.assert_allclose(kink_relative_loss, 7 / 27, rtol=1e-12)
    assert kink_relative_loss > 1 / 9
    years = spec["trading_days_per_year"] / spec["decision_interval_days"]
    old_input, full_input = amounts[0] * years, amounts[-1] * years
    decay = spec["natural_decay_sd_per_year"]
    payload = {
        "status": "PASS", "scope": "mathematical diagnostic, not model or research acceptance",
        "market_initializations": 0, "market_runs": 0,
        "spec_sha256": hashlib.sha256(spec_path.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "numpy_version": np.__version__, "fixed_amounts_sd": amounts.tolist(),
        "gross_annual_amount_upper_bounds": {
            "old_single_amplitude_sd": float(old_input), "full_grid_sd": float(full_input),
            "natural_decay_sd": decay, "old_share_of_decay": float(old_input / decay),
            "full_share_of_decay": float(full_input / decay),
            "old_interior_net_upper_bound_sd": float(old_input - decay),
            "full_interior_net_upper_bound_sd": float(full_input - decay),
            "interpretation": "Decision-quota upper bounds before delay, capacity, economic incentives or learning; not attainable equilibrium or predicted outcomes."},
        "smooth_quadratic": {"objective": "f(x)=a*x-c*x*x, c>0", "intervals": intervals,
                             "conditions": ["positive continuous optimum between two legal neighboring grid points",
                                            "neighboring legal amount ratio <=2", "maintain legal", "same smooth quadratic on the interval"],
                             "global_relative_guarantee_for_piecewise_objectives": False},
        "below_first_amount": {"first_amount_sd": float(first), "absolute_error_bound": float(absolute_bound),
                               "sampled_maximum_absolute_error": float(regret.max()),
                               "relative_error_may_equal_one": True,
                               "conditions": ["maintain legal", "0<=continuous optimum<=first legal amount", "same smooth quadratic"]},
        "report_capacity_counterexample": {
            **example, "cost_coefficient": c, "continuous_optimum_sd": room,
            "continuous_value": float(kink_value), "fixed_candidate_values": kink_values.tolist(),
            "best_grid_amounts_sd": candidates[np.isclose(kink_values, kink_values.max(), rtol=1e-12, atol=1e-16)].tolist(),
            "best_grid_value": float(kink_values.max()), "relative_loss": float(kink_relative_loss),
            "left_derivative_at_kink": left_derivative, "right_derivative_at_kink": right_derivative},
        "limits": ["No candidate generation uses an NPV optimum; only the fixed specification supplies candidate amounts.",
                   "Feasibility masks removing a bracketing point or maintain invalidate the stated bound assumptions.",
                   "An NPV minimum-value threshold adds at most that threshold to objective regret when maintain is legal.",
                   "Gross action capacity does not establish positive private NPV, algorithm quality or policy effectiveness."]}
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": payload["status"], "old_gross_sd_per_year": old_input,
                      "new_gross_sd_per_year": full_input, "subfirst_absolute_bound": absolute_bound,
                      "cap_kink_relative_loss": kink_relative_loss}))


if __name__ == "__main__":
    main()
