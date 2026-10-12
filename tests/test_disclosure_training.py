import hashlib
import json
from dataclasses import asdict, replace

import numpy as np
import pytest

from abm.disclosure import training
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.learning import load_frozen, save_frozen, table_fingerprint
from abm.disclosure.policy import PolicySchedule
from abm.tabular import CompanyQLearner


CONFIG = MarketConfig(n_investors=20, n_firms=6, trading_days=180, burn_in_days=60)
DOMAIN = load_domain("configs/domains/esg.json")
POLICY = PolicySchedule.constant(DOMAIN)


class ArchiveHarness:
    def __init__(self):
        self.calls = []
        self.fail = None
        self.error_type = RuntimeError
        self.market_failure = None
        self.unseen = False
        self.undercovered = False
        self.mutate_frozen = False

    def run(self, config, domain, output, policy, *, purpose, learner=None, training=False,
            learning_metadata=None, coverage_target=0, common_prepolicy_sha256=None):
        phase = "training" if training else "validation"
        key = (phase, config.seed, config.firm_policy)
        output.mkdir(parents=True, exist_ok=False)
        experiment = next(parent for parent in output.parents if (parent / "experiment.json").exists())
        assert (experiment / "initial_model.npz").exists()
        self.calls.append({"key": key, "learner_id": id(learner) if learner is not None else None,
                           "epsilon": learner.epsilon if learner is not None else None,
                           "count_before": int(learner.counts.sum()) if learner is not None else None,
                           "writeable": learner.values.flags.writeable if learner is not None else None,
                           "metadata": learning_metadata, "coverage_target": coverage_target,
                           "common_prepolicy_sha256": common_prepolicy_sha256})
        if training:
            group = 3 if common_prepolicy_sha256 is not None else 0
            learner.values[group, 0, 0] += 1
            learner.counts[group, 0] += 10
            if self.undercovered:
                learner.counts[0, 0] = [20, 19, 20]
        if key == self.fail:
            (output / "manifest.json").write_text(json.dumps({"status": "failed", "seed": config.seed}), encoding="utf-8")
            raise self.error_type("controlled world failure")
        if self.mutate_frozen and learner is not None and not training:
            learner.counts.flags.writeable = True
            learner.counts[0, 0, 0] += 1
            learner.counts.flags.writeable = False
        validation = {"mechanical": {"status": "PASS"}, "stylized": {"status": "PASS"},
                      "return_acf": {"status": "pending"}, "cross_asset_correlation": {"status": "pending"},
                      "empirical_calibration": {"status": "pending"}}
        if key == self.market_failure:
            validation["stylized"]["status"] = "FAIL"
        payloads = {"metrics.json": {"true_change": {"equal_weight_sd": 0.0}},
                    "validation.json": validation}
        if config.firm_policy != "npv":
            visits = np.zeros((6, 81), dtype=np.int64)
            legal = np.zeros((6, 81, 2 * len(config.firm_action_fractions) + 1), dtype=np.int64)
            visits[0, 0] = 90 if self.unseen and not training else 100
            legal[0, 0] = visits[0, 0]
            missing = 0
            if self.unseen and not training:
                visits[0, 1] = legal[0, 1, 2] = 10
                missing = 10
            payloads["learning.json"] = {
                "coverage": {"visits": visits.tolist(), "legal_action_visits": legal.tolist(),
                             "decisions": 100, "unseen_state_decisions": missing,
                             "status": "PASS", "unseen_state_fraction": missing / 100},
                "ledger": {"resource_cost": 1.0, "scope": "observed private ledger"},
                "tail": {"unclosed_decisions": 6, "pending_projects": [{"due_day": 240}]},
            }
        artifacts = {}
        for name, payload in payloads.items():
            path = output / name
            path.write_text(json.dumps(payload), encoding="utf-8")
            artifacts[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest = {"status": "complete", "run_id": str(key), "result_fingerprint": str(key),
                    "artifacts": artifacts}
        (output / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


@pytest.fixture
def archive_harness(monkeypatch):
    harness = ArchiveHarness()

    def contract(config, domain, policy, *, coverage_target=0, common_prepolicy_sha256=None):
        config_dict = config.to_dict()
        config_dict.pop("seed")
        config_dict.pop("firm_policy")
        payload = {"version": 1, "candidate_fraction": .01, "groups": 6, "config": config_dict,
                   "domain": domain.to_dict(), "policy": asdict(policy), "source_hashes": {"fixture": "frozen"}}
        if coverage_target:
            payload["coverage_target"] = coverage_target
        if common_prepolicy_sha256 is not None:
            payload["common_prepolicy_sha256"] = common_prepolicy_sha256
        return payload

    monkeypatch.setattr(training.runner, "learning_contract", contract)
    monkeypatch.setattr(training.runner, "run_and_archive", harness.run)
    return harness


def run_budget(path, *, train=(101, 102, 103), valid=(201, 202), reserved=(301,)):
    return training.train_and_evaluate(CONFIG, DOMAIN, POLICY, path, training_seeds=train,
                                       validation_seeds=valid, reserved_seeds=reserved)


def make_common_model(path):
    learner = CompanyQLearner(groups=6)
    learner.values[0, 0, 2] = .5
    learner.counts[0, 0, 2] = 12
    initial = {"shape": [6, 81, 3], "values": 0.0, "counts": 0,
               "values_dtype": "float64", "counts_dtype": "int64"}
    metadata = {"phase": "frozen", "completed_training_seeds": [901], "initial_table": initial,
                "contract": training.runner.learning_contract(CONFIG, DOMAIN, POLICY),
                "budget": {"training_seeds": [901], "validation_seeds": [902], "reserved_seeds": [903],
                           "training_worlds": 1, "learning_rate": .1, "initial_table": initial}}
    return save_frozen(path, learner, metadata)


def test_shared_training_table_linear_epsilon_and_frozen_paired_rules(tmp_path, archive_harness):
    output = tmp_path / "budget"
    result = run_budget(output)
    calls = archive_harness.calls
    trained = calls[:3]
    assert [row["epsilon"] for row in trained] == pytest.approx([1, .55, .1])
    assert len({row["learner_id"] for row in trained}) == 1
    assert [row["count_before"] for row in trained] == [0, 30, 60]
    assert [row["key"] for row in calls[3:]] == [
        ("validation", seed, mode) for seed in (201, 202) for mode in ("q_learning", "npv_discrete", "npv")]
    evaluated = [row for row in calls[3:] if row["key"][2] == "q_learning"]
    assert all(row["epsilon"] == 0 and row["writeable"] is False for row in evaluated)
    assert all(row["count_before"] == 90 for row in evaluated)
    initial, initial_metadata = load_frozen(output / "initial_model.npz")
    frozen, metadata = load_frozen(output / "frozen_model.npz", expected_sha256=result["frozen_model_sha256"])
    assert np.count_nonzero(initial.values) == np.count_nonzero(initial.counts) == 0
    assert initial_metadata["completed_training_seeds"] == []
    assert metadata["completed_training_seeds"] == [101, 102, 103]
    assert metadata["budget"]["reserved_seeds"] == [301]
    assert metadata["contract"] == result["contract"]
    assert frozen.values[0, 0, 0] == 3
    np.testing.assert_array_equal(frozen.counts[0, 0], 30)
    assert table_fingerprint(frozen) == result["frozen_table_fingerprint"]
    assert result["status"] == "complete"
    assert result["validation"]["coverage"]["status"] == "PASS"
    assert result["validation"]["mechanical"]["status"] == "PASS"
    for gate in ("return_acf", "cross_asset_correlation", "empirical_calibration"):
        assert result["validation"][gate]["status"] == "pending"
    assert result["m4_status"] == result["claim_support"] == "pending"
    assert result["comparison_scope"] == "within_scenario_algorithm_comparison"
    assert result["records"][0]["learning"]["ledger"]["resource_cost"] == 1
    assert result["records"][0]["learning"]["tail"]["pending_projects"] == [{"due_day": 240}]
    spec = json.loads((output / "experiment.json").read_text())
    assert spec["budget"]["initial_table"]["shape"] == [6, 81, 3]
    assert spec["contract"]["source_hashes"] == {"fixture": "frozen"}


def test_single_training_world_uses_epsilon_one(tmp_path, archive_harness):
    result = run_budget(tmp_path / "one", train=(101,), valid=(201,))
    assert archive_harness.calls[0]["epsilon"] == 1
    assert result["budget"]["epsilon_by_world"] == [1]
    assert result["validation"]["coverage"]["status"] == "FAIL"


def test_quota_option_is_frozen_and_only_sent_to_q_worlds(tmp_path, archive_harness):
    output = tmp_path / "quota"
    result = training.train_and_evaluate(CONFIG, DOMAIN, POLICY, output, training_seeds=(101, 102),
                                         validation_seeds=(201,), coverage_target=20)
    frozen, metadata = load_frozen(output / "frozen_model.npz")
    assert result["budget"]["coverage_target"] == metadata["budget"]["coverage_target"] == 20
    assert result["contract"]["coverage_target"] == metadata["contract"]["coverage_target"] == 20
    assert frozen.counts.sum() == 60
    assert [row["coverage_target"] for row in archive_harness.calls] == [20, 20, 20, 0, 0]
    spec = json.loads((output / "experiment.json").read_text())
    assert spec["contract"]["coverage_target"] == spec["budget"]["coverage_target"] == 20


@pytest.mark.parametrize("target", [-1, True, 1.5])
def test_invalid_quota_stops_before_output_or_world(tmp_path, archive_harness, target):
    output = tmp_path / "invalid_quota"
    with pytest.raises(ValueError, match="coverage_target"):
        training.train_and_evaluate(CONFIG, DOMAIN, POLICY, output, training_seeds=(101,),
                                    validation_seeds=(201,), coverage_target=target)
    assert not output.exists()
    assert not archive_harness.calls


def test_common_prefix_budget_copies_real_prefix_counts_and_starts_post_table_at_zero(tmp_path, archive_harness):
    path = tmp_path / "common.npz"
    digest = make_common_model(path)
    source, _ = load_frozen(path)
    output = tmp_path / "conditional"
    result = training.train_and_evaluate(CONFIG, DOMAIN, POLICY.with_intervention(61), output,
                                         training_seeds=(101, 102), validation_seeds=(201,),
                                         reserved_seeds=(301,), common_prepolicy_model=path,
                                         common_prepolicy_sha256=digest)
    initial, _ = load_frozen(output / "initial_model.npz")
    frozen, metadata = load_frozen(output / "frozen_model.npz")
    np.testing.assert_array_equal(initial.values[:3], source.values[:3])
    np.testing.assert_array_equal(initial.counts[:3], source.counts[:3])
    assert not initial.values[3:].any() and not initial.counts[3:].any()
    np.testing.assert_array_equal(frozen.values[:3], source.values[:3])
    np.testing.assert_array_equal(frozen.counts[:3], source.counts[:3])
    assert frozen.counts[3:].sum() == 60
    assert metadata["common_prepolicy"]["sha256"] == digest
    assert metadata["common_prepolicy"]["training_seeds"] == [901]
    assert metadata["common_prepolicy"]["validation_seeds"] == [902]
    assert metadata["common_prepolicy"]["table_fingerprint"] == table_fingerprint(source, prefix_groups=3)
    assert metadata["initial_table"]["post_counts"] == 0
    assert result["comparison_scope"] == "conditional_strategy_deployment"
    assert [row["common_prepolicy_sha256"] for row in archive_harness.calls] == [digest, digest, digest, None, None]
    assert json.loads((output / "experiment.json").read_text(encoding="utf-8"))["common_prepolicy"] == metadata["common_prepolicy"]


@pytest.mark.parametrize("train,valid,reserved", [((901,), (201,), (301,)), ((101,), (902,), (301,)),
                                                  ((101,), (201,), (901,)), ((903,), (201,), (301,))])
def test_common_source_seed_lineage_cannot_reenter_the_current_budget(tmp_path, archive_harness, train, valid, reserved):
    path = tmp_path / "common.npz"
    digest = make_common_model(path)
    output = tmp_path / "overlap"
    with pytest.raises(ValueError, match="seed lineage overlaps"):
        training.train_and_evaluate(CONFIG, DOMAIN, POLICY.with_intervention(61), output,
                                    training_seeds=train, validation_seeds=valid, reserved_seeds=reserved,
                                    common_prepolicy_model=path, common_prepolicy_sha256=digest)
    assert not output.exists()
    assert not archive_harness.calls


@pytest.mark.parametrize("model,digest", [("missing.npz", None), (None, "a" * 64)])
def test_common_source_path_and_digest_must_be_given_together(tmp_path, archive_harness, model, digest):
    output = tmp_path / "missing_common"
    with pytest.raises(ValueError, match="supplied together"):
        training.train_and_evaluate(CONFIG, DOMAIN, POLICY.with_intervention(61), output,
                                    training_seeds=(101,), validation_seeds=(201,),
                                    common_prepolicy_model=model, common_prepolicy_sha256=digest)
    assert not output.exists()
    assert not archive_harness.calls


@pytest.mark.parametrize("train,valid,reserved", [
    ((), (201,), ()), ((101,), (), ()), ((101, 101), (201,), ()),
    ((101,), (201, 201), ()), ((101,), (101,), ()),
    ((True,), (201,), ()), ((-1,), (201,), ()), ((1.5,), (201,), ()),
    ((101,), (201,), (101,)), ((101,), (201,), (201,)),
    ((101,), (201,), (301, 301)),
])
def test_invalid_seed_plan_is_rejected_before_any_world(tmp_path, archive_harness, train, valid, reserved):
    output = tmp_path / "invalid"
    with pytest.raises(ValueError):
        run_budget(output, train=train, valid=valid, reserved=reserved)
    assert not output.exists()
    assert not archive_harness.calls


def test_existing_output_is_not_overwritten(tmp_path, archive_harness):
    sentinel = tmp_path / "keep.txt"
    sentinel.write_text("keep")
    with pytest.raises(FileExistsError):
        run_budget(tmp_path)
    assert sentinel.read_text() == "keep"
    assert not archive_harness.calls


@pytest.mark.parametrize("error_type", [RuntimeError, KeyboardInterrupt])
def test_training_failure_preserves_partial_table_and_completed_worlds_then_stops(tmp_path, archive_harness, error_type):
    archive_harness.fail = ("training", 102, "q_learning")
    archive_harness.error_type = error_type
    output = tmp_path / "failed"
    with pytest.raises(error_type, match="controlled world failure"):
        run_budget(output)
    assert len(archive_harness.calls) == 2
    summary = json.loads((output / "summary.json").read_text())
    assert summary["status"] == ("interrupted" if error_type is KeyboardInterrupt else "failed")
    assert summary["completed_training_seeds"] == [101]
    assert summary["records"][-1]["status"] == "failed"
    assert summary["resumable"] is False
    with np.load(output / "failed_training_state.npz", allow_pickle=False) as state:
        assert state["values"][0, 0, 0] == 2
        np.testing.assert_array_equal(state["counts"][0, 0], 20)
    assert not (output / "frozen_model.npz").exists()
    with pytest.raises(FileExistsError):
        run_budget(output)


def test_checkpoint_error_does_not_mask_training_failure_or_leave_running_summary(tmp_path, archive_harness, monkeypatch):
    archive_harness.fail = ("training", 102, "q_learning")
    original = np.savez_compressed

    def save(handle, **arrays):
        if "failed_training_state" in str(handle.name):
            raise OSError("checkpoint locked")
        return original(handle, **arrays)

    monkeypatch.setattr(training.np, "savez_compressed", save)
    output = tmp_path / "locked"
    with pytest.raises(RuntimeError, match="controlled world failure"):
        run_budget(output)
    summary = json.loads((output / "summary.json").read_text())
    assert summary["status"] == "failed"
    assert summary["error_type"] == "RuntimeError"
    assert summary["failed_checkpoint_error"]["error_type"] == "OSError"


def test_validation_world_failure_preserves_all_other_predeclared_comparators(tmp_path, archive_harness):
    archive_harness.fail = ("validation", 201, "q_learning")
    result = run_budget(tmp_path / "validation_failure")
    assert len(archive_harness.calls) == 9
    assert result["status"] == "incomplete"
    failed = [row for row in result["records"] if row["status"] == "failed"]
    assert len(failed) == 1 and failed[0]["seed"] == 201
    assert result["validation"]["coverage"]["status"] == "incomplete"
    assert result["validation"]["mechanical"]["status"] == "incomplete"


def test_market_validation_failure_is_kept_separate_from_coverage_and_completion(tmp_path, archive_harness):
    archive_harness.market_failure = ("validation", 201, "npv_discrete")
    result = run_budget(tmp_path / "market_failure")
    assert result["status"] == "complete"
    assert result["validation"]["mechanical"]["status"] == "PASS"
    assert result["validation"]["stylized"]["status"] == "FAIL"
    assert result["validation"]["coverage"]["status"] == "PASS"
    assert result["validation"]["empirical_calibration"]["status"] == "pending"
    assert result["claim_support"] == "pending"


@pytest.mark.parametrize("problem", ["unseen", "undercovered"])
def test_coverage_uses_archived_visits_and_training_counts_even_if_report_labels_pass(tmp_path, archive_harness, problem):
    setattr(archive_harness, problem, True)
    result = run_budget(tmp_path / problem)
    coverage = result["validation"]["coverage"]
    assert coverage["status"] == "FAIL"
    assert coverage["common_state_undercovered_actions"]
    assert result["m4_status"] == "pending"
    if problem == "unseen":
        assert coverage["unseen_state_fraction"] == .1
    else:
        assert coverage["unseen_state_fraction"] == 0
        assert any(row["action"] == 1 and row["count"] == 19 for row in coverage["common_state_undercovered_actions"])


def test_frozen_table_mutation_aborts_evaluation_without_changing_saved_model(tmp_path, archive_harness):
    archive_harness.mutate_frozen = True
    output = tmp_path / "mutation"
    with pytest.raises(RuntimeError, match="changed the frozen"):
        run_budget(output)
    summary = json.loads((output / "summary.json").read_text())
    assert summary["status"] == "failed"
    assert len(archive_harness.calls) == 4
    frozen, _ = load_frozen(output / "frozen_model.npz", expected_sha256=summary["frozen_model_sha256"])
    np.testing.assert_array_equal(frozen.counts[0, 0], 30)


def test_source_contract_change_stops_before_another_training_world(tmp_path, archive_harness, monkeypatch):
    original = training.runner.learning_contract
    calls = 0

    def contract(*args):
        nonlocal calls
        calls += 1
        payload = original(*args)
        if calls > 2:
            payload["source_hashes"] = {"fixture": "changed"}
        return payload

    monkeypatch.setattr(training.runner, "learning_contract", contract)
    output = tmp_path / "source_change"
    with pytest.raises(RuntimeError, match="contract changed"):
        run_budget(output)
    assert len(archive_harness.calls) == 1
    summary = json.loads((output / "summary.json").read_text())
    assert summary["completed_training_seeds"] == [101]
    assert summary["status"] == "failed"


@pytest.mark.parametrize("target", [0, 20])
@pytest.mark.parametrize("common", [False, True])
def test_cli_passes_generic_reserved_seeds_and_file_inputs(tmp_path, monkeypatch, target, common):
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(CONFIG.to_dict()), encoding="utf-8")
    captured = {}

    def execute(config, domain, policy, output, **kwargs):
        captured.update(kwargs)
        assert config == CONFIG and domain == DOMAIN and policy is None
        return {"status": "complete", "validation": {"coverage": {"status": "FAIL"}}}

    monkeypatch.setattr(training, "train_and_evaluate", execute)
    assert training.main(["--config", str(config_path), "--domain", "configs/domains/esg.json",
                          "--output", str(tmp_path / "cli"), "--training-seeds", "101", "102",
                          "--validation-seeds", "201", "--reserved-seeds", "301", "302"]
                         + (["--coverage-target", str(target)] if target else [])
                         + (["--common-prepolicy-model", str(tmp_path / "common.npz"),
                             "--common-prepolicy-sha256", "a" * 64] if common else [])) == 0
    expected = {"training_seeds": [101, 102], "validation_seeds": [201], "reserved_seeds": [301, 302]}
    if target:
        expected["coverage_target"] = target
    if common:
        expected.update({"common_prepolicy_model": tmp_path / "common.npz", "common_prepolicy_sha256": "a" * 64})
    assert captured == expected


def test_coverage_uses_internal_choice_columns_when_maintain_is_infeasible():
    counts = np.full((6, 81, 5), 20, dtype=np.int64)
    counts[0, 0, 3] = 19
    visits = np.zeros((6, 81), dtype=np.int64)
    visits[0, 0] = 100
    allowed = np.zeros_like(counts)
    allowed[0, 0, 3] = 100
    records = [{"phase": "validation", "firm_policy": "q_learning", "status": "complete", "seed": 901,
                "learning": {"coverage": {"visits": visits.tolist(), "legal_action_visits": allowed.tolist(),
                                           "decisions": 100, "unseen_state_decisions": 0}}}]
    report = training._coverage(records, counts, 1)
    assert report["status"] == "FAIL"
    assert all(item["choice_index"] == 3 and item["action"] == 0
               for item in report["common_state_undercovered_actions"])
    counts[0, 0, 3] = 20
    assert training._coverage(records, counts, 1)["status"] == "PASS"


def test_multi_amplitude_budget_freezes_full_table_and_per_choice_coverage(tmp_path, archive_harness):
    cfg = replace(CONFIG, firm_action_fractions=(.01, .02, .04, .08, .16, .32, .64, 1.))
    result = training.train_and_evaluate(cfg, DOMAIN, POLICY, tmp_path / "grid", training_seeds=(101, 102),
                                         validation_seeds=(201,), reserved_seeds=(301,))
    frozen, metadata = load_frozen(tmp_path / "grid/frozen_model.npz")
    assert frozen.values.shape == (6, 81, 17)
    assert metadata["initial_table"]["shape"] == [6, 81, 17]
    assert frozen.counts.sum() == 340
    assert result["validation"]["coverage"]["status"] == "PASS"
    assert np.asarray(result["validation"]["coverage"]["legal_action_visits"]).shape == (6, 81, 17)
