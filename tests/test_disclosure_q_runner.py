from dataclasses import replace
import json

import numpy as np
import pytest

from abm.disclosure import runner
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.learning import load_frozen, save_frozen, table_fingerprint
from abm.disclosure.policy import PolicySchedule
from abm.tabular import CompanyQLearner


@pytest.fixture
def learning_inputs():
    config = MarketConfig(n_investors=30, n_firms=6, trading_days=180, burn_in_days=0,
                          initial_impact_share=.2, firm_policy="q_learning")
    domain = load_domain("configs/domains/esg.json")
    policy = PolicySchedule.constant(domain)
    metadata = {"contract": runner.learning_contract(config, domain, policy), "purpose": "unit_test"}
    return config, domain, policy, metadata


def baseline_model(path, config, domain, policy, *, coverage_target=0, invalid=None):
    learner = CompanyQLearner(groups=6, actions=2 * len(config.firm_action_fractions) + 1)
    learner.values[0, 0, 2] = .5
    learner.counts[0, 0, 2] = config.n_firms * (config.trading_days // config.firm_decision_interval - 1)
    initial = {"shape": list(learner.values.shape), "values": 0.0, "counts": 0,
               "values_dtype": "float64", "counts_dtype": "int64"}
    metadata = {"phase": "frozen", "completed_training_seeds": [1001], "initial_table": initial,
                "contract": runner.learning_contract(config, domain, PolicySchedule(policy.baseline), coverage_target=coverage_target),
                "budget": {"training_seeds": [1001], "validation_seeds": [1002], "reserved_seeds": [1003],
                           "training_worlds": 1, "learning_rate": .1, "initial_table": initial}}
    if invalid == "phase":
        metadata["phase"] = "training"
    elif invalid == "incomplete":
        metadata["completed_training_seeds"] = []
    elif invalid == "intervention":
        metadata["contract"]["policy"]["intervention"] = metadata["contract"]["policy"]["baseline"]
    elif invalid == "existing_common":
        metadata["common_prepolicy"] = {}
    elif invalid == "config":
        metadata["contract"]["config"]["n_investors"] += 1
    elif invalid == "domain":
        metadata["contract"]["domain"]["name"] = "other"
    elif invalid == "grid":
        metadata["contract"]["candidate_fractions"] = [.02]
    elif invalid == "source":
        metadata["contract"]["source_hashes"] = {"changed": "changed"}
    elif invalid == "post":
        learner.values[3, 0, 0] = 1
    elif invalid == "counts":
        learner.counts[0, 0, 2] += 1
    elif invalid == "seeds":
        metadata["budget"]["validation_seeds"] = [1001]
    elif invalid == "initial":
        initial["values"] = 1.0
    digest = save_frozen(path, learner, metadata)
    return path, digest


def test_train_archive_freeze_evaluate_and_render(tmp_path, learning_inputs, monkeypatch):
    config, domain, policy, metadata = learning_inputs
    learner = CompanyQLearner(groups=6, epsilon=1)
    trained = tmp_path / "train"
    train = runner.run_and_archive(config, domain, trained, policy, learner=learner,
                                   training=True, learning_metadata=metadata)
    initial, _ = load_frozen(trained / "input_model.npz")
    frozen, frozen_metadata = load_frozen(trained / "output_model.npz")
    assert initial.counts.sum() == 0
    assert frozen.counts.sum() == 12
    assert np.array_equal(frozen.values, learner.values)
    assert train["learning"]["training"] is True
    result = runner.load_result(trained / "result.npz")
    assert result.fingerprint() == train["result_fingerprint"]
    assert result.coverage_forced is None
    assert result.learning_update is None
    with np.load(trained / "result.npz", allow_pickle=False) as arrays:
        assert "coverage_forced" not in arrays
        assert "learning_update" not in arrays
    report = json.loads((trained / "learning.json").read_text())
    assert "quota_exploration" not in report
    assert "coverage_target" not in metadata["contract"]
    assert "common_prepolicy_sha256" not in metadata["contract"]
    assert report["ledger"]["completed_transitions"] == 12
    assert report["tail"]["unclosed_decisions"] == 6
    assert sum(map(sum, report["coverage"]["visits"])) == 18
    np.testing.assert_array_equal(
        report["tail"]["unapplied_next_day_commitments"]["resource_cost"],
        result.cost_fraction[-1] * result.market.prices[-1],
    )
    evaluated = tmp_path / "eval"
    evaluation = runner.run_and_archive(replace(config, seed=config.seed + 1), domain, evaluated, policy,
                                        learner=frozen, learning_metadata=frozen_metadata)
    assert evaluation["learning"]["training"] is False
    after, _ = load_frozen(evaluated / "output_model.npz")
    np.testing.assert_array_equal(after.values, frozen.values)
    np.testing.assert_array_equal(after.counts, frozen.counts)
    expected = (evaluated / "report.md").read_bytes()
    monkeypatch.setattr(runner.DisclosureMarket, "run", lambda self: pytest.fail("render simulated"))
    runner.render_run(evaluated)
    assert (evaluated / "report.md").read_bytes() == expected
    (evaluated / "output_model.npz").write_bytes(b"changed")
    with pytest.raises(ValueError, match="archive hash mismatch: output_model"):
        runner.render_run(evaluated)


def test_learning_contract_rejects_wrong_market_and_mutable_evaluation(tmp_path, learning_inputs):
    config, domain, policy, metadata = learning_inputs
    learner = CompanyQLearner(groups=6)
    with pytest.raises(ValueError, match="contract mismatch"):
        runner.run_and_archive(replace(config, n_firms=7), domain, tmp_path / "wrong", policy,
                               learner=learner, training=True, learning_metadata=metadata)
    with pytest.raises(ValueError, match="evaluation requires frozen"):
        runner.run_and_archive(config, domain, tmp_path / "mutable", policy,
                               learner=learner, learning_metadata=metadata)
    with pytest.raises(ValueError, match="explicit learner"):
        runner.run_and_archive(config, domain, tmp_path / "missing", policy)
    assert not list(tmp_path.iterdir())


def test_failed_training_preserves_partial_table(tmp_path, learning_inputs, monkeypatch):
    config, domain, policy, metadata = learning_inputs
    learner = CompanyQLearner(groups=6)

    def fail(market):
        market.learner.counts[0, 0, 0] = 2
        raise RuntimeError("training stopped")

    monkeypatch.setattr(runner.DisclosureMarket, "run", fail)
    with pytest.raises(RuntimeError, match="training stopped"):
        runner.run_and_archive(config, domain, tmp_path / "failed", policy,
                               learner=learner, training=True, learning_metadata=metadata)
    manifest = json.loads((tmp_path / "failed" / "manifest.json").read_text())
    assert manifest["status"] == "failed"
    checkpoint = manifest["failed_learning_checkpoint"]
    assert checkpoint["resumable"] is False
    saved, _ = load_frozen(tmp_path / "failed" / checkpoint["path"], expected_sha256=checkpoint["sha256"])
    assert saved.counts[0, 0, 0] == 2


def test_failed_checkpoint_does_not_hide_original_failure(tmp_path, learning_inputs, monkeypatch):
    config, domain, policy, metadata = learning_inputs
    learner = CompanyQLearner(groups=6)

    def fail(market):
        market.learner.values[0, 0, 0] = np.nan
        raise RuntimeError("original failure")

    monkeypatch.setattr(runner.DisclosureMarket, "run", fail)
    with pytest.raises(RuntimeError, match="original failure"):
        runner.run_and_archive(config, domain, tmp_path / "failed", policy,
                               learner=learner, training=True, learning_metadata=metadata)
    manifest = json.loads((tmp_path / "failed" / "manifest.json").read_text())
    assert manifest["status"] == "failed"
    assert manifest["error"] == "original failure"
    assert "invalid Q table" in manifest["failed_learning_checkpoint"]["error"]


def test_coverage_counts_every_legal_action_in_common_states(tmp_path, learning_inputs):
    config, domain, policy, _ = learning_inputs
    result = runner.DisclosureMarket(replace(config, firm_policy="npv_discrete"), domain, policy).run()
    learner = CompanyQLearner(groups=6)
    learner.counts[:] = 20
    group, state = result.learning_groups[1, 0], result.learning_states[1, 0]
    learner.counts[group, state, 1] = 0
    report = runner.learning_report(result, config, learner, training=False)
    assert any(item["group"] == group and item["state"] == state and item["action"] == 1
               for item in report["coverage"]["common_state_undercovered_actions"])


def test_multi_amplitude_archive_preserves_choice_indices_and_rejects_same_size_wrong_grid(tmp_path, learning_inputs):
    config, domain, policy, _ = learning_inputs
    config = replace(config, firm_action_fractions=(.01, .5, 1.))
    metadata = {"contract": runner.learning_contract(config, domain, policy)}
    learner = CompanyQLearner(groups=6, actions=7, epsilon=1)
    output = tmp_path / "multiple"
    manifest = runner.run_and_archive(config, domain, output, policy, learner=learner,
                                      training=True, learning_metadata=metadata)
    result = runner.load_result(output / "result.npz")
    assert result.learning_choices.shape == result.actions.shape
    assert result.valid_actions.shape[-1] == 7
    assert result.fingerprint() == manifest["result_fingerprint"]
    report = json.loads((output / "learning.json").read_text())
    assert np.asarray(report["coverage"]["legal_action_visits"]).shape == (6, 81, 7)
    frozen, frozen_metadata = load_frozen(output / "output_model.npz")
    assert frozen.counts.sum() == 12
    with pytest.raises(ValueError, match="contract mismatch"):
        runner.run_and_archive(replace(config, firm_action_fractions=(.01, .4, 1.)), domain,
                               tmp_path / "wrong_grid", policy, learner=frozen, learning_metadata=frozen_metadata)
    assert not (tmp_path / "wrong_grid").exists()


def test_quota_archive_binds_option_and_aligns_forced_choices_with_later_td(tmp_path, learning_inputs):
    config, domain, policy, _ = learning_inputs
    config = replace(config, firm_action_fractions=(.01, .02, .04, .08, .16, .32, .64, 1.))
    metadata = {"contract": runner.learning_contract(config, domain, policy, coverage_target=20)}
    learner = CompanyQLearner(groups=6, actions=17, epsilon=0)
    folder = tmp_path / "quota"
    manifest = runner.run_and_archive(config, domain, folder, policy, learner=learner,
                                      training=True, learning_metadata=metadata, coverage_target=20)
    assert manifest["learning"]["coverage_target"] == 20
    result = runner.load_result(folder / "result.npz")
    assert result.fingerprint() == manifest["result_fingerprint"]
    assert result.coverage_forced[1:3].all()
    assert not result.coverage_forced[[0, 3]].any()
    report = json.loads((folder / "learning.json").read_text())
    quota = report["quota_exploration"]
    assert quota["target"] == 20
    assert quota["forced_decisions"] == quota["completed_forced_transitions"] == 12
    assert quota["unsettled_forced_decisions"] == 0
    assert quota["updated_transition_samples"] == learner.counts.sum() == 12
    frozen, restored = load_frozen(folder / "output_model.npz")
    assert restored == metadata
    with pytest.raises(ValueError, match="contract mismatch"):
        runner.run_and_archive(config, domain, tmp_path / "wrong", policy, learner=frozen,
                               learning_metadata=restored)
    assert not (tmp_path / "wrong").exists()
    evaluated = tmp_path / "evaluated"
    runner.run_and_archive(config, domain, evaluated, policy, learner=frozen,
                           learning_metadata=restored, coverage_target=20)
    after, _ = load_frozen(evaluated / "output_model.npz")
    np.testing.assert_array_equal(after.values, frozen.values)
    np.testing.assert_array_equal(after.counts, frozen.counts)
    assert runner.load_result(evaluated / "result.npz").coverage_forced is None
    evaluation = json.loads((evaluated / "learning.json").read_text())["quota_exploration"]
    assert evaluation["forced_decisions"] == evaluation["updated_transition_samples"] == 0


@pytest.mark.parametrize("invalid", ["phase", "incomplete", "intervention", "existing_common", "config",
                                     "domain", "grid", "source", "post", "counts", "seeds", "initial"])
def test_common_prepolicy_rejects_invalid_source_provenance(tmp_path, learning_inputs, invalid):
    config, domain, policy, _ = learning_inputs
    path, digest = baseline_model(tmp_path / "source.npz", config, domain, policy, invalid=invalid)
    with pytest.raises(ValueError, match="common pre-policy"):
        runner.load_common_prepolicy(path, digest, config, domain, policy)


def test_common_prepolicy_runner_checks_hash_prefix_and_seed_lineage_before_output(tmp_path, learning_inputs):
    config, domain, policy, _ = learning_inputs
    policy = policy.with_intervention(61)
    path, digest = baseline_model(tmp_path / "source.npz", config, domain, policy)
    with pytest.raises(ValueError, match="hash mismatch"):
        runner.load_common_prepolicy(path, "0" * 64, config, domain, policy)
    source, origin = runner.load_common_prepolicy(path, digest, config, domain, policy)
    learner = CompanyQLearner(groups=6)
    metadata = {"contract": runner.learning_contract(config, domain, policy, common_prepolicy_sha256=digest)}
    with pytest.raises(ValueError, match="source model"):
        runner.run_and_archive(config, domain, tmp_path / "bare_sha", policy, learner=learner, training=True,
                               learning_metadata=metadata, common_prepolicy_sha256=digest)
    metadata["common_prepolicy"] = origin
    with pytest.raises(ValueError, match="table or provenance mismatch"):
        runner.run_and_archive(config, domain, tmp_path / "wrong_prefix", policy, learner=learner, training=True,
                               learning_metadata=metadata, common_prepolicy_sha256=digest)
    learner.values[:3], learner.counts[:3] = source.values[:3], source.counts[:3]
    with pytest.raises(ValueError, match="seed lineage overlaps"):
        runner.run_and_archive(replace(config, seed=1002), domain, tmp_path / "seen_seed", policy,
                               learner=learner, training=True, learning_metadata=metadata, common_prepolicy_sha256=digest)
    assert not any((tmp_path / name).exists() for name in ("bare_sha", "wrong_prefix", "seen_seed"))


def test_common_prepolicy_archive_separates_completed_windows_and_actual_learning(tmp_path, learning_inputs):
    config, domain, policy, _ = learning_inputs
    config = replace(config, firm_action_fractions=(.01, .02, .04, .08, .16, .32, .64, 1.))
    policy = policy.with_intervention(61)
    path, digest = baseline_model(tmp_path / "source.npz", config, domain, policy, coverage_target=20)
    source, origin = runner.load_common_prepolicy(path, digest, config, domain, policy, coverage_target=20)
    learner = CompanyQLearner(groups=6, actions=17, epsilon=1)
    learner.values[:3], learner.counts[:3] = source.values[:3], source.counts[:3]
    metadata = {"contract": runner.learning_contract(config, domain, policy, coverage_target=20,
                                                     common_prepolicy_sha256=digest), "common_prepolicy": origin}
    folder = tmp_path / "conditional"
    manifest = runner.run_and_archive(config, domain, folder, policy, learner=learner, training=True,
                                      learning_metadata=metadata, coverage_target=20, common_prepolicy_sha256=digest)
    result = runner.load_result(folder / "result.npz")
    assert manifest["learning"]["common_prepolicy_sha256"] == digest
    assert result.learning_transition[2:4].all()
    assert not result.learning_update[:3].any()
    assert result.learning_update[3].all()
    assert result.coverage_forced[2].all()
    assert not result.coverage_forced[[0, 1, 3]].any()
    assert learner.counts[3:].sum() == 6
    assert table_fingerprint(learner, prefix_groups=3) == origin["table_fingerprint"]
    report = json.loads((folder / "learning.json").read_text())
    assert report["ledger"]["completed_transitions"] == 12
    assert report["conditional_deployment"]["updated_transition_samples"] == 6
    assert report["conditional_deployment"]["excluded_completed_transition_samples"] == 6
    assert report["quota_exploration"]["completed_forced_transitions"] == 6
    assert report["quota_exploration"]["updated_transition_samples"] == 6
    frozen, restored = load_frozen(folder / "output_model.npz")
    evaluated = tmp_path / "conditional_eval"
    runner.run_and_archive(config, domain, evaluated, policy, learner=frozen, learning_metadata=restored,
                           coverage_target=20, common_prepolicy_sha256=digest)
    assert not runner.load_result(evaluated / "result.npz").learning_update.any()
