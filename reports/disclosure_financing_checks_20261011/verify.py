"""Verify archived financing cash flows, controls and intervention pairing."""
import argparse
import json
from pathlib import Path
import numpy as np
from abm.manifest import sha256_file
from abm.disclosure.experiments import collect_records


def verify(destination):
    destination = Path(destination)
    frozen = json.loads((destination / "experiment.json").read_text(encoding="utf-8"))
    records = collect_records(destination, frozen)
    assert len(records) == len(frozen["spec"]["seeds"]) * len(frozen["scenarios"])
    assert all(row["status"] == "complete" for row in records)
    paths = {}
    maximum_fee_error = maximum_adjustment_error = maximum_decay_error = maximum_rate_error = maximum_value_error = 0.0
    null_trials = 0
    null_names = {"zero_financing_exposure", "zero_financing_spread", "zero_impact_B", "zero_taste_zero_policy"}
    for row in records:
        name, seed = row["scenario"], row["seed"]
        attempt = destination / row["path"]
        manifest = json.loads((attempt / "manifest.json").read_text(encoding="utf-8"))
        cfg, domain = manifest["config"], manifest["domain"]
        with np.load(attempt / "result.npz", allow_pickle=False) as result:
            arrays = {key: result[key] for key in result.files}
        paths[name, seed] = arrays
        exposure = cfg["financing_exposure_fraction"] * arrays["market_prices"][0]
        rate = arrays["financing_rate"]
        expected = rate[0].copy()
        for day in range(1, len(rate)):
            if day % cfg["financing_repricing_interval"] == 0:
                expected = cfg["risk_free_rate"] + cfg["financing_spread"] * exposure / (exposure + arrays["market_prices"][day - 1])
            maximum_rate_error = max(maximum_rate_error, float(np.max(np.abs(rate[day] - expected))))
            np.testing.assert_allclose(rate[day], expected, rtol=0, atol=1e-14)
            if day % cfg["financing_repricing_interval"] != 0:
                np.testing.assert_array_equal(rate[day], rate[day - 1])
        fundamental_seed = np.random.SeedSequence(cfg["seed"]).spawn(4)[2]
        rng = np.random.default_rng(fundamental_seed)
        rho = cfg["fundamental_common_correlation"]
        drift = (cfg["fundamental_drift"] - .5 * cfg["fundamental_volatility"]**2) / 252
        sigma = cfg["fundamental_volatility"] / np.sqrt(252)
        for day in range(1, len(rate)):
            shocks = np.sqrt(rho) * rng.standard_normal() + np.sqrt(1-rho) * rng.standard_normal(cfg["n_firms"])
            expected_value = arrays["market_intrinsic_values"][day-1] * np.exp(drift + sigma * shocks)
            if day > 1 and (day-1) % cfg["firm_decision_interval"] == 0:
                period = (day-1) // cfg["firm_decision_interval"]
                commitment = arrays["subsidy_fraction"][period] - arrays["cost_fraction"][period] - arrays["penalty_fraction"][period]
                expected_value += commitment * arrays["market_prices"][day-1]
            expected_value += arrays["financing_value_adjustment"][day]
            maximum_value_error = max(maximum_value_error, float(np.max(np.abs(expected_value-arrays["market_intrinsic_values"][day]))))
            np.testing.assert_allclose(arrays["market_intrinsic_values"][day], expected_value, rtol=0, atol=1e-12)
        fee_error = np.max(np.abs(arrays["financing_cost"][1:] - exposure * rate[1:] / 252))
        adjustment_error = np.max(np.abs(arrays["financing_value_adjustment"][1:] - exposure * (rate[0] - rate[1:]) / 252))
        maximum_fee_error = max(maximum_fee_error, float(fee_error))
        maximum_adjustment_error = max(maximum_adjustment_error, float(adjustment_error))
        assert fee_error <= 1e-12 and adjustment_error <= 1e-12
        if name in null_names or name.startswith("zero_taste_"):
            assert np.all(arrays["actions"] == 2)
            assert np.all(arrays["amounts"] == 0) and np.all(arrays["inflation"] == 0)
            lower = min(domain["direction"] * (raw - domain["initial_mean"]) / domain["initial_sd"] for raw in [domain["raw_lower"], domain["raw_upper"]])
            expected_true = np.maximum(arrays["true_goodness"][0] - np.arange(len(rate))[:, None] * domain["natural_decay"] / 252, lower)
            error = float(np.max(np.abs(arrays["true_goodness"] - expected_true)))
            maximum_decay_error = max(maximum_decay_error, error)
            assert error < 1e-10
            null_trials += 1
    state_keys = ["market_prices", "market_intrinsic_values", "true_goodness", "inflation", "impact_share", "impact_wealth_share", "pricing_slope", "financing_rate", "financing_cost", "financing_value_adjustment"]
    decision_keys = ["actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction"]
    pairs = 0
    for seed in frozen["spec"]["seeds"]:
        for prefix, policies in [("market", ["I", "F", "IF"]), ("zero_taste", ["I", "F", "IF"]), ("equal_cost", ["I", "F"])]:
            baseline = paths[prefix + "_B", seed]
            for policy in policies:
                trial = paths[prefix + "_" + policy, seed]
                for key in state_keys:
                    np.testing.assert_array_equal(trial[key][:601], baseline[key][:601])
                for key in decision_keys:
                    np.testing.assert_array_equal(trial[key][:11], baseline[key][:11])
                pairs += 1
    core_failures = [dict(scenario=row["scenario"], seed=row["seed"]) for row in records
                     if any(row["validation"][gate]["status"] != "PASS" for gate in ["mechanical", "stylized"])]
    report = {"status": "PARTIAL" if core_failures else "PASS", "mechanism_verification": "PASS",
              "core_market_validation": "FAIL" if core_failures else "PASS",
              "experiment_id": frozen["experiment_id"], "trials": len(records),
              "null_control_trials": null_trials, "paired_policy_histories_through_day_600": pairs,
              "maximum_value_error": maximum_value_error, "maximum_rate_error": maximum_rate_error, "maximum_fee_error": maximum_fee_error, "maximum_adjustment_error": maximum_adjustment_error,
              "maximum_decay_error": maximum_decay_error, "core_validation_failures": core_failures,
              "experiment_sha256": sha256_file(destination / "experiment.json"),
              "summary_sha256": sha256_file(destination / "summary.json"), "verifier_sha256": sha256_file(Path(__file__)),
              "scope": "Implementation and development-path verification only; accrued fees are not cash payments, empirical calibration or policy evidence."}
    (destination / "financing_verification.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps(report))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment")
    verify(parser.parse_args().experiment)
