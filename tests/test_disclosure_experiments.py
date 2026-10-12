import json
from pathlib import Path

import numpy as np
import pytest

from abm.disclosure import experiments
from abm.disclosure import runner


@pytest.fixture
def spec_path(tmp_path):
    payload = {
        "name": "pipeline-test", "purpose": "development",
        "domain": str(Path("configs/domains/esg.json").resolve()),
        "market": {"n_investors": 24, "n_firms": 6, "trading_days": 450, "burn_in_days": 50,
                   "initial_impact_share": 0.2},
        "seeds": [101, 102],
        "scenarios": [{"name": "base"}, {"name": "info", "policy": {
            "start_day": 51, "changes": {"transparency": 0.6}}}],
        "comparisons": [{"name": "info_minus_base", "weights": {"info": 1, "base": -1}, "primary": True}],
        "analysis": {"primary_metric": "true_change.equal_weight_sd",
                     "metrics": ["true_change.equal_weight_sd", "costs.resource_cost"], "confidence_level": 0.95},
    }
    path = tmp_path / "spec.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_freeze_retains_domain_provenance_and_resolves_inputs(spec_path):
    frozen = experiments.freeze_spec(spec_path)
    assert "_note" in frozen["raw_domain"]
    assert frozen["scenarios"][1]["policy"]["intervention"]["transparency"] == 0.6
    assert frozen["scenarios"][0]["config"]["firm_policy"] == "npv"


def test_initial_noise_and_later_reduction_share_pre_policy_history(spec_path):
    payload = json.loads(spec_path.read_text())
    payload["market"]["trading_days"] = 120
    payload["scenarios"] = [
        {"name": "base", "policy": {"baseline": {"disclosure_noise_sd": 0.3}}},
        {"name": "info", "policy": {"baseline": {"disclosure_noise_sd": 0.3},
                                  "start_day": 51, "changes": {"disclosure_noise_sd": 0.0}}},
    ]
    spec_path.write_text(json.dumps(payload))
    frozen = experiments.freeze_spec(spec_path)
    baseline, intervention = [experiments._inputs(row, 101) for row in frozen["scenarios"]]
    assert baseline[2].at(120).disclosure_noise_sd == 0.3
    assert intervention[2].at(50) == baseline[2].at(50)
    assert intervention[2].at(51).disclosure_noise_sd == 0
    base = runner.DisclosureMarket(*baseline).run()
    info = runner.DisclosureMarket(*intervention).run()
    np.testing.assert_array_equal(base.market.prices[:51], info.market.prices[:51])
    np.testing.assert_array_equal(base.public_signal[:51], info.public_signal[:51])
    assert not np.array_equal(base.public_signal[51:], info.public_signal[51:])
    assert not np.array_equal(base.market.prices[51:], info.market.prices[51:])
    payload["scenarios"][0]["policy"]["baseline"]["disclosure_noise_sd"] = 0.4
    spec_path.write_text(json.dumps(payload))
    assert experiments.freeze_spec(spec_path)["experiment_id"] != frozen["experiment_id"]


def test_confirmatory_run_cannot_use_development_seed_count(spec_path):
    payload = json.loads(spec_path.read_text())
    payload["purpose"] = "confirmatory"
    spec_path.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="at least 30"):
        experiments.freeze_spec(spec_path)


def test_paired_statistics_use_seed_differences():
    result = experiments.paired_statistics([1.0, 2.0, 3.0], 0.95)
    assert result["mean"] == 2.0
    assert result["standard_error"] == pytest.approx(1 / np.sqrt(3))
    assert result["ci_low"] == pytest.approx(-0.484137711719546)
    assert experiments.paired_statistics([0.0, 0.0], 0.95)["p_value"] == 1.0


def test_experiment_pairing_resume_and_render_only(spec_path, tmp_path, monkeypatch):
    output = tmp_path / "experiment"
    report = experiments.run_experiment(spec_path, output)
    expected_report = report.read_bytes()
    summary = json.loads((output / "summary.json").read_text())
    assert summary["complete_trials"] == summary["planned_trials"] == 4
    by_trial = {(row["scenario"], row["seed"]): row for row in summary["records"]}
    expected_differences = [by_trial[("info", seed)]["metrics"]["true_change"]["equal_weight_sd"]
                            - by_trial[("base", seed)]["metrics"]["true_change"]["equal_weight_sd"]
                            for seed in (101, 102)]
    actual = summary["comparisons"][0]["metrics"]["true_change.equal_weight_sd"]
    assert actual["paired_values"] == expected_differences
    assert actual["holm_p_value"] == actual["p_value"]
    for seed in (101, 102):
        base = runner.load_result(output / f"base/seed_{seed}/attempt_001/result.npz")
        info = runner.load_result(output / f"info/seed_{seed}/attempt_001/result.npz")
        np.testing.assert_array_equal(base.market.prices[:51], info.market.prices[:51])
        np.testing.assert_array_equal(base.true_goodness[:51], info.true_goodness[:51])

    def forbidden(*args, **kwargs):
        pytest.fail("completed trials were simulated again")

    monkeypatch.setattr(experiments, "_run_trial", forbidden)
    assert experiments.run_experiment(spec_path, output, resume=True).read_bytes() == expected_report
    monkeypatch.setattr(experiments, "analyze", forbidden)
    monkeypatch.setattr(experiments, "_inputs", forbidden)
    assert experiments.main(["--output", str(output), "--render-only"]) == 0
    assert report.read_bytes() == expected_report


def test_resume_rejects_modified_design(spec_path, tmp_path):
    output = tmp_path / "experiment"
    experiments.run_experiment(spec_path, output)
    payload = json.loads(spec_path.read_text())
    payload["market"]["taste_median"] = 0.04
    spec_path.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="different inputs"):
        experiments.run_experiment(spec_path, output, resume=True)


def test_failed_seed_stays_incomplete_and_retry_keeps_attempt(spec_path, tmp_path, monkeypatch):
    output = tmp_path / "experiment"
    original = experiments.run_and_archive

    def fail_one(config, *args, **kwargs):
        if config.seed == 102:
            raise RuntimeError("controlled failure")
        return original(config, *args, **kwargs)

    monkeypatch.setattr(experiments, "run_and_archive", fail_one)
    experiments.run_experiment(spec_path, output)
    summary = json.loads((output / "summary.json").read_text())
    assert summary["status"] == "incomplete"
    metric = summary["comparisons"][0]["metrics"]["true_change.equal_weight_sd"]
    assert metric["missing_seeds"] == [102]
    assert "mean" not in metric
    assert metric["holm_p_value"] is None
    monkeypatch.setattr(experiments, "run_and_archive", original)
    experiments.run_experiment(spec_path, output, resume=True)
    resumed = json.loads((output / "summary.json").read_text())
    assert resumed["status"] == "complete"
    for row in resumed["records"]:
        assert [item["status"] for item in row["attempts"]] == (
            ["failed", "complete"] if row["seed"] == 102 else ["complete"]
        )


def test_holm_family_and_no_firm_pseudoreplication(spec_path):
    frozen = experiments.freeze_spec(spec_path)
    frozen["spec"]["comparisons"].append({"name": "base_level", "weights": {"base": 1}, "primary": True})
    rows = [{"scenario": scenario, "seed": seed, "status": "complete",
             "metrics": {"true_change": {"equal_weight_sd": value}, "costs": {"resource_cost": value}},
             "validation": {"mechanical": {"status": "PASS"}, "stylized": {"status": "PASS"}}}
            for scenario, seed, value in [("base", 101, 1), ("base", 102, 2), ("info", 101, 3), ("info", 102, 5)]]
    summary = experiments.analyze(frozen, rows)
    metrics = [item["metrics"]["true_change.equal_weight_sd"] for item in summary["comparisons"]]
    metrics.sort(key=lambda item: item["p_value"])
    assert all(item["n"] == 2 for item in metrics)
    assert metrics[0]["holm_p_value"] == pytest.approx(min(1, metrics[0]["p_value"] * 2))
    assert metrics[1]["holm_p_value"] >= metrics[0]["holm_p_value"]


def test_later_failed_attempt_does_not_hide_completed_trial(spec_path, tmp_path):
    output = tmp_path / "experiment"
    experiments.run_experiment(spec_path, output)
    first = output / "base/seed_101/attempt_001"
    later = first.with_name("attempt_002")
    later.mkdir()
    manifest = json.loads((first / "manifest.json").read_text())
    runner.write_json(later / "manifest.json", {"run_id": manifest["run_id"], "status": "failed", "error": "failed retry"})
    experiments.run_experiment(spec_path, output, resume=True)
    summary = json.loads((output / "summary.json").read_text())
    assert summary["complete_trials"] == 4
    row = next(row for row in summary["records"] if row["scenario"] == "base" and row["seed"] == 101)
    assert [attempt["status"] for attempt in row["attempts"]] == ["complete", "failed"]
    assert row["path"].endswith("attempt_001")


def test_experiment_refuses_concurrent_writer(spec_path, tmp_path):
    output = tmp_path / "experiment"
    output.mkdir()
    with experiments._experiment_lock(output):
        with pytest.raises(OSError):
            experiments.run_experiment(spec_path, output, resume=True)
    assert not (output / "experiment.json").exists()
