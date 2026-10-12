"""Cross-variant description of the three CSI300 development grids (main setting and two controls).

Reads only the archived experiment outputs; writes comparison.json. No new simulation.
SD metrics are not comparable across observation links, so cross-variant contrasts use raw-score metrics.
"""

import hashlib
import json
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VARIANTS = ("quantile_copula", "quantile_independent", "linear")
SEEDS = (23001, 23002, 23003)
RAW_METRICS = ("true_change.equal_weight_raw", "full_period_change.equal_weight_raw", "size.large_minus_small_raw")
CONTRASTS = {"market_effect": {"market_B": 1, "zero_taste_B": -1},
             "size_cost_assumption_effect": {"market_B": 1, "equal_cost_B": -1}}
ACTIONS = ("improve", "wash", "maintain")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metric(metrics, dotted):
    value = metrics
    for key in dotted.split("."):
        value = value[key]
    return value


def interval(values):
    values = np.asarray(values, dtype=float)
    mean = float(values.mean())
    if values.size < 2 or np.all(values == values[0]):
        return {"mean": mean, "ci_low": mean, "ci_high": mean, "n": int(values.size)}
    half = stats.t.ppf(.975, values.size - 1) * values.std(ddof=1) / np.sqrt(values.size)
    return {"mean": mean, "ci_low": mean - half, "ci_high": mean + half, "n": int(values.size)}


def main():
    inputs, records, domains = {}, {}, {}
    for variant in VARIANTS:
        directory = ROOT / f"reports/disclosure_csi300_{variant}_development_20261012_v1"
        summary_path = directory / "summary.json"
        inputs[summary_path.relative_to(ROOT).as_posix()] = sha(summary_path)
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        assert summary["complete_trials"] == summary["planned_trials"] == 45
        records[variant] = {(row["scenario"], row["seed"]): row for row in summary["records"]}
        spec = json.loads((directory / "experiment.json").read_text(encoding="utf-8"))
        domains[variant] = spec["raw_domain"]

    failing = {variant: sorted(f"{s}/{seed}" for (s, seed), row in rows.items()
                               if row["validation"]["mechanical"]["status"] != "PASS")
               for variant, rows in records.items()}

    behaviour = {}
    for variant in VARIANTS:
        domain = domains[variant]
        linear_upper = (domain["raw_upper"] - domain["initial_mean"]) / domain["initial_sd"]
        counts = np.zeros(3, dtype=np.int64)
        at_ceiling_start, at_ceiling_end, near_end = [], [], []
        for (scenario, seed), row in records[variant].items():
            with np.load(ROOT / f"reports/disclosure_csi300_{variant}_development_20261012_v1" / row["path"] / "result.npz") as bundle:
                actions = bundle["actions"]
                true = bundle["true_goodness"]
            counts += np.bincount(actions.ravel(), minlength=3)
            if scenario == "market_B":
                upper = linear_upper if variant == "linear" else 6.0
                at_ceiling_start.append(float(np.mean(true[0] >= upper - 1e-12)))
                at_ceiling_end.append(float(np.mean(true[-1] >= upper - 1e-12)))
                near_end.append(float(np.mean(true[-1] >= upper - .25)))
        behaviour[variant] = {
            "firm_decisions_by_action_all_trials": dict(zip(ACTIONS, counts.tolist())),
            "goodness_upper_bound": linear_upper if variant == "linear" else 6.0,
            "market_B_share_at_upper_bound_day0": at_ceiling_start,
            "market_B_share_at_upper_bound_final": at_ceiling_end,
            "market_B_share_within_0.25sd_of_bound_final": near_end,
        }

    scenario_raw = {variant: {scenario: {name: interval([metric(records[variant][(scenario, seed)]["metrics"], name)
                                                        for seed in SEEDS]) for name in RAW_METRICS}
                              for scenario in ("market_B", "zero_taste_B", "equal_cost_B")}
                    for variant in VARIANTS}
    within = {variant: {contrast: {name: interval([sum(weight * metric(records[variant][(scenario, seed)]["metrics"], name)
                                                       for scenario, weight in weights.items()) for seed in SEEDS])
                                   for name in RAW_METRICS}
                        for contrast, weights in CONTRASTS.items()}
              for variant in VARIANTS}
    across = {}
    for control in ("quantile_independent", "linear"):
        for contrast, weights in CONTRASTS.items():
            for name in RAW_METRICS:
                differences = [sum(weight * (metric(records["quantile_copula"][(s, seed)]["metrics"], name)
                                             - metric(records[control][(s, seed)]["metrics"], name))
                                   for s, weight in weights.items()) for seed in SEEDS]
                across.setdefault(f"quantile_copula_minus_{control}", {}).setdefault(contrast, {})[name] = interval(differences)

    payload = {
        "inputs": inputs, "script_sha256": sha(Path(__file__)),
        "interpretation_limits": [
            "Development grid: 150 investors, 30 firms, 1800 days, three already-observed seeds; not confirmatory.",
            "Raw-score metrics only across variants; the quantile link is nonlinear, so raw changes depend on the starting level.",
            "Paired t intervals over three seeds, unadjusted; parameter and model uncertainty excluded.",
            "Mechanism and cost parameters are uncalibrated assumptions inherited from esg.json."],
        "mechanical_failures": failing,
        "identical_failure_sets": len({tuple(value) for value in failing.values()}) == 1,
        "firm_behaviour": behaviour,
        "scenario_raw_metrics": scenario_raw,
        "within_variant_contrasts_raw": within,
        "across_variant_paired_differences_raw": across,
    }
    with (HERE / "comparison.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({key: payload[key] for key in ("identical_failure_sets", "firm_behaviour")}, indent=1))


if __name__ == "__main__":
    main()
