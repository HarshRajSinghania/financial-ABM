import hashlib
import json
from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure.config import MarketConfig
from abm.disclosure.learning import (
    action_kinds, batch_update, choose_actions, discrete_candidates, load_frozen,
    npv_discrete, save_frozen, table_fingerprint,
)
from abm.tabular import CompanyQLearner


GRID = (.01, .02, .04, .08, .16, .32, .64, 1.)


def offered(**changes):
    arguments = dict(improve_capacity=np.array([.25]), inflate_capacity=np.array([.25]),
                     marginal_cost=np.array([.05]), max_change_per_period=.25,
                     wash_cost_ratio=.2, subsidy=.005, real_value_per_sd=np.array([.001]),
                     displaced_real_value_per_sd=np.array([.0001]),
                     wash_value_per_sd=np.array([.0001]), fine_value_per_sd=np.array([.01]),
                     amplitude_fractions=GRID)
    return discrete_candidates(**{**arguments, **changes})


class QuantileRandom:
    def __init__(self):
        self.calls = []

    def random(self, size):
        self.calls.append(size)
        return (np.arange(size) + .5) / size


@pytest.mark.parametrize("action_count", [3, 17])
def test_fulfilled_quota_preserves_actions_and_exact_rng_stream(action_count):
    learner = CompanyQLearner(groups=1, actions=action_count, epsilon=.37)
    learner.values[:] = np.random.default_rng(91).normal(size=learner.values.shape)
    learner.counts[:] = 20
    groups, states = np.zeros(300, dtype=int), np.arange(300) % 3
    valid = np.random.default_rng(92).random((300, action_count)) > .3
    valid[:, 2] = True
    original_rng, quota_rng = np.random.default_rng(93), np.random.default_rng(93)
    original = choose_actions(learner, groups, states, valid, original_rng, training=True)
    forced = np.ones(300, dtype=bool)
    actual = choose_actions(learner, groups, states, valid, quota_rng, training=True,
                            coverage_target=20, forced_choices=forced)
    np.testing.assert_array_equal(actual, original)
    np.testing.assert_array_equal(quota_rng.random(30), original_rng.random(30))
    assert not forced.any()


def test_quota_balances_a_shared_batch_without_fabricating_completed_counts():
    learner = CompanyQLearner(groups=1, actions=17, epsilon=0)
    learner.values[:, :, 2] = 100
    values, counts = learner.values.copy(), learner.counts.copy()
    groups, states = np.zeros(34, dtype=int), np.zeros(34, dtype=int)
    valid, forced = np.ones((34, 17), dtype=bool), np.zeros(34, dtype=bool)
    actions = choose_actions(learner, groups, states, valid, np.random.default_rng(94),
                             training=True, coverage_target=20, forced_choices=forced)
    np.testing.assert_array_equal(np.bincount(actions, minlength=17), 2)
    assert forced.all()
    np.testing.assert_array_equal(learner.values, values)
    np.testing.assert_array_equal(learner.counts, counts)
    repeated = choose_actions(learner, groups, states, valid, np.random.default_rng(94),
                              training=True, coverage_target=20)
    np.testing.assert_array_equal(repeated, actions)
    batch_update(learner, np.arange(34), groups, states, actions, np.zeros(34), groups,
                 states, valid, elapsed_days=60, annual_discount_rate=.05,
                 terminated=np.ones(34, dtype=bool))
    np.testing.assert_array_equal(learner.counts[0, 0], 2)
    assert learner.counts.sum() == 34


def test_quota_uses_completed_counts_and_excludes_illegal_high_q_choices():
    learner = CompanyQLearner(groups=1, actions=17, epsilon=0)
    learner.counts[:] = 20
    learner.counts[0, 0, 15], learner.counts[0, 0, 16] = 5, 1
    learner.values[:, :, 2] = 1000
    learner.values[:, :, 15:17] = -100
    valid = np.zeros((4, 17), dtype=bool)
    valid[:, [15, 16]] = True
    actions = choose_actions(learner, np.zeros(4, dtype=int), np.zeros(4, dtype=int), valid,
                             np.random.default_rng(95), training=True, coverage_target=20)
    np.testing.assert_array_equal(actions, 16)
    assert learner.counts[0, 0, 16] == 1


def test_quota_ties_keep_kind_probabilities_after_capacity_deduplication():
    candidates = offered(improve_capacity=np.array([.001]), inflate_capacity=np.array([.004]))
    learner = CompanyQLearner(groups=30, actions=17, epsilon=0)
    rows = np.arange(2400)
    valid = np.repeat(candidates.valid_actions, rows.size, axis=0)
    forced, rng = np.zeros(rows.size, dtype=bool), QuantileRandom()
    actions = choose_actions(learner, rows // 81, rows % 81, valid, rng, training=True,
                             coverage_target=20, forced_choices=forced)
    assert rng.calls == [2400]
    assert forced.all()
    counts = np.bincount(actions, minlength=17)
    assert counts[0] == counts[2] == 800
    assert counts[1] == counts[4] == 400
    assert counts[~candidates.valid_actions[0]].sum() == 0


def test_quota_flag_records_branch_even_when_choice_matches_unforced_sample():
    learner = CompanyQLearner(groups=1, epsilon=0)
    valid = np.tile([False, False, True], (2, 1))
    forced = np.zeros(2, dtype=bool)
    actions = choose_actions(learner, np.zeros(2, dtype=int), np.zeros(2, dtype=int), valid,
                             np.random.default_rng(96), training=True, coverage_target=1,
                             forced_choices=forced)
    assert actions.tolist() == [2, 2]
    assert forced.tolist() == [True, False]
    assert learner.counts.sum() == 0


def test_quota_reservations_are_ordered_best_effort_for_different_legal_sets():
    learner = CompanyQLearner(groups=1, epsilon=0)
    groups, states = np.zeros(2, dtype=int), np.zeros(2, dtype=int)
    valid = np.array([[True, True, False], [True, False, False]])
    forced = np.zeros(2, dtype=bool)
    actions = choose_actions(learner, groups, states, valid, QuantileRandom(), training=True,
                             coverage_target=1, forced_choices=forced)
    assert actions.tolist() == [0, 0]
    assert forced.tolist() == [True, False]
    reversed_actions = choose_actions(learner, groups, states, valid[::-1], QuantileRandom(),
                                      training=True, coverage_target=1)
    assert reversed_actions.tolist() == [0, 1]
    assert learner.counts.sum() == 0


@pytest.mark.parametrize("target", [-1, True, 1.5])
def test_invalid_quota_rejected_before_rng_draw(target):
    learner, rng = CompanyQLearner(groups=1), QuantileRandom()
    with pytest.raises(ValueError, match="coverage_target"):
        choose_actions(learner, np.array([0]), np.array([0]), np.ones((1, 3), dtype=bool),
                       rng, training=True, coverage_target=target)
    assert not rng.calls


def test_default_config_omits_grid_and_nondefault_json_roundtrips():
    original = MarketConfig()
    assert original.firm_action_fractions == (.01,)
    assert "firm_action_fractions" not in original.to_dict()
    assert MarketConfig.from_dict(original.to_dict()) == original
    extended = replace(original, firm_action_fractions=GRID)
    payload = json.loads(json.dumps(extended.to_dict()))
    assert payload["firm_action_fractions"] == list(GRID)
    assert MarketConfig.from_dict(payload) == extended


def test_direct_config_grid_cannot_change_through_a_callers_list():
    fractions = [.01, .1]
    config = MarketConfig(firm_action_fractions=fractions)
    fractions.append(1.)
    assert config.firm_action_fractions == (.01, .1)
    assert config.to_dict()["firm_action_fractions"] == [.01, .1]


@pytest.mark.parametrize("fractions", [(), (0,), (-.1,), (.1, .1), (.5, .1), (1.01,), (.1, np.nan), (.1, np.inf)])
def test_invalid_grids_fail_in_config_and_standalone_candidates(fractions):
    with pytest.raises(ValueError, match="firm_action_fractions"):
        MarketConfig(firm_action_fractions=fractions)
    with pytest.raises(ValueError):
        offered(amplitude_fractions=fractions)


def test_default_three_action_component_fingerprints_are_unchanged():
    candidates = discrete_candidates(
        improve_capacity=np.array([.25, .001, 0, .2]),
        inflate_capacity=np.array([.25, .0005, 0, 0]),
        marginal_cost=np.array([.05, .2, .1, .03]), max_change_per_period=.25,
        wash_cost_ratio=.2, subsidy=.005,
        real_value_per_sd=np.array([.001, .02, 0, .01]),
        displaced_real_value_per_sd=np.array([.0001, .001, 0, .003]),
        wash_value_per_sd=np.array([.0001, .01, 0, .004]),
        fine_value_per_sd=np.array([.01, .003, 0, .02]),
    )
    digest = hashlib.sha256()
    for name in ("amounts", "cost_fraction", "subsidy_fraction", "values", "valid_actions"):
        digest.update(getattr(candidates, name).tobytes())
    assert digest.hexdigest() == "dd62f27410ab1f2101775b628795770d55b45f0b26a51ec25a37d34493609ea3"
    learner = CompanyQLearner(groups=1, epsilon=.37, learning_rate=.2)
    learner.values[0, 0] = [.1, .2, .2]
    learner.values[0, 1] = [.4, .1, .4]
    groups, states = np.zeros(300, dtype=int), np.arange(300) % 2
    masks = np.tile(np.array([[True, True, True], [True, False, True], [False, False, True]]), (100, 1))
    actions = choose_actions(learner, groups, states, masks, np.random.default_rng(71), training=True)
    assert hashlib.sha256(actions.tobytes()).hexdigest() == "a95d765988ec00c6af19c1b271e4937902b331dafc82314a8eb563ac296557fa"
    public_actions = learner.choose(groups, states, np.random.default_rng(72))
    assert hashlib.sha256(public_actions.tobytes()).hexdigest() == "aefe0ca0d01dba61c236b51836f20e1163ab65f7f39eb08eddad08370f942cd9"
    batch_update(learner, np.array([1, 2, 3]), np.zeros(3, dtype=int), np.array([0, 1, 1]),
                 np.array([0, 1, 2]), np.array([.3, -.1, .2]), np.zeros(3, dtype=int),
                 np.array([1, 0, 1]), masks[:3], elapsed_days=60, annual_discount_rate=.05,
                 terminated=np.array([False, False, True]))
    assert table_fingerprint(learner) == "ee7aba4a35de1a5b78a1fed3afcc33245466024a3d8bd25f197ea256f6589723"


def test_scalar_amplitude_interface_matches_singleton_grid():
    scalar = offered(amplitude_fraction=.2, amplitude_fractions=None)
    singleton = offered(amplitude_fractions=(.2,))
    for name in ("amounts", "cost_fraction", "subsidy_fraction", "values", "valid_actions", "kinds"):
        np.testing.assert_array_equal(getattr(scalar, name), getattr(singleton, name))


def test_seventeen_candidates_keep_amplitude_order_and_physical_units():
    candidates = offered()
    assert candidates.amounts.shape == candidates.values.shape == candidates.valid_actions.shape == (1, 17)
    assert candidates.kinds.tolist() == [0, 1, 2] + [0, 1] * 7
    np.testing.assert_array_equal(action_kinds(17), candidates.kinds)
    real, wash = np.flatnonzero(candidates.kinds == 0), np.flatnonzero(candidates.kinds == 1)
    np.testing.assert_allclose(candidates.amounts[0, real], np.array(GRID) * .25)
    np.testing.assert_allclose(candidates.amounts[0, wash], np.array(GRID) * .25)
    assert candidates.amounts[0, 2] == candidates.cost_fraction[0, 2] == 0
    assert candidates.cost_fraction[0, 15] == pytest.approx(.05 * .25**2)
    assert candidates.cost_fraction[0, 16] == pytest.approx(.2 * .05 * .25**2)
    assert candidates.subsidy_fraction[0, 15] == pytest.approx(.005 * .25)
    assert candidates.valid_actions.all()


def test_clipping_masks_repeated_physical_candidates_and_zero_capacity():
    candidates = offered(improve_capacity=np.array([.001, 0]), inflate_capacity=np.array([.004, 0]))
    assert np.flatnonzero(candidates.valid_actions[0]).tolist() == [0, 1, 2, 4]
    assert np.flatnonzero(candidates.valid_actions[1]).tolist() == [2]
    assert np.all(candidates.amounts[0, candidates.kinds == 0] == .001)
    assert np.all(candidates.amounts[0, np.flatnonzero(candidates.kinds == 1)[1:]] == .004)


@pytest.mark.parametrize("epsilon", [0, .37, 1])
def test_exploration_and_all_maximum_q_ties_share_probability_by_kind(epsilon):
    learner = CompanyQLearner(groups=1, epsilon=epsilon, actions=17)
    rng = QuantileRandom()
    size = 2400
    actions = choose_actions(learner, np.zeros(size, dtype=int), np.zeros(size, dtype=int),
                             np.ones((size, 17), dtype=bool), rng, training=True)
    counts = np.bincount(actions, minlength=17)
    assert counts[2] == 800
    np.testing.assert_array_equal(counts[np.arange(17) != 2], 100)
    assert rng.calls == [size]


def test_clipped_duplicate_washing_does_not_gain_sampling_mass():
    candidates = offered(amplitude_fractions=(.01, .1, 1), inflate_capacity=np.array([.0001]))
    learner = CompanyQLearner(groups=1, epsilon=1, actions=7)
    size = 900
    actions = choose_actions(learner, np.zeros(size, dtype=int), np.zeros(size, dtype=int),
                             np.repeat(candidates.valid_actions, size, axis=0), QuantileRandom(), training=True)
    assert np.bincount(actions, minlength=7).tolist() == [100, 300, 300, 100, 0, 100, 0]


def test_training_greedy_ties_are_hierarchical_before_epsilon_mixture():
    learner = CompanyQLearner(groups=1, epsilon=.4, actions=7)
    learner.values[0, 0, 2] = -1
    mask = np.array([[True, True, True, True, False, True, False]])
    size = 900
    actions = choose_actions(learner, np.zeros(size, dtype=int), np.zeros(size, dtype=int),
                             np.repeat(mask, size, axis=0), QuantileRandom(), training=True)
    assert np.bincount(actions, minlength=7).tolist() == [130, 390, 120, 130, 0, 130, 0]


@pytest.mark.parametrize("action_count", [3, 17])
def test_unvisited_evaluation_falls_back_to_first_legal_priority(action_count):
    learner = CompanyQLearner(groups=1, actions=action_count)
    learner.values[0, :, 1] = 100
    mask = np.zeros((3, action_count), dtype=bool)
    mask[0, :3] = True
    mask[1, :2] = True
    mask[2, 1] = True
    assert choose_actions(learner, np.zeros(3, dtype=int), np.arange(3), mask, None, training=False).tolist() == [2, 0, 1]


def test_frozen_evaluation_ties_prefer_maintain_then_real_amplitudes_then_wash():
    learner = CompanyQLearner(groups=1, actions=17)
    learner.counts[:] = 1
    mask = np.ones((4, 17), dtype=bool)
    mask[1:, 2] = False
    mask[2, 0] = False
    mask[3, action_kinds(17) == 0] = False
    assert choose_actions(learner, np.zeros(4, dtype=int), np.zeros(4, dtype=int), mask, None, training=False).tolist() == [2, 0, 3, 1]


def test_npvs_keep_feasible_negative_or_zero_actions_when_maintain_is_illegal():
    candidates = offered(improve_capacity=np.full(3, .25))
    values = np.full((3, 17), -1.)
    values[:, 2] = 0
    values[0, 15:17] = -.2
    values[1, :2] = 0
    mask = candidates.valid_actions.copy()
    mask[:2, 2] = False
    assert npv_discrete(replace(candidates, values=values, valid_actions=mask)).tolist() == [15, 0, 2]


def test_no_legal_candidate_fails_selection_and_next_state_update():
    learner = CompanyQLearner(groups=1, actions=17)
    mask = np.zeros((1, 17), dtype=bool)
    with pytest.raises(ValueError, match="at least one legal"):
        choose_actions(learner, np.array([0]), np.array([0]), mask, None, training=False)
    with pytest.raises(ValueError, match="at least one legal"):
        npv_discrete(replace(offered(), valid_actions=mask))
    with pytest.raises(ValueError, match="at least one legal"):
        batch_update(learner, np.array([0]), np.array([0]), np.array([0]), np.array([16]),
                     np.array([0.]), np.array([0]), np.array([0]), mask, elapsed_days=60,
                     annual_discount_rate=.05, terminated=np.array([False]))


def test_dynamic_batch_update_masks_next_actions_and_counts_internal_choices():
    learner = CompanyQLearner(groups=2, actions=17, learning_rate=1)
    learner.values[1, 1] = 1000
    learner.values[1, 1, 14] = .5
    mask = np.zeros((3, 17), dtype=bool)
    mask[:, 14] = True
    batch_update(learner, np.array([1, 2, 3]), np.zeros(3, dtype=int), np.array([0, 0, 1]),
                 np.array([16, 16, 3]), np.array([1., 3., -1.]), np.ones(3, dtype=int),
                 np.ones(3, dtype=int), mask, elapsed_days=60, annual_discount_rate=.05,
                 terminated=np.array([False, False, True]))
    assert learner.values[0, 0, 16] == pytest.approx(2 + .5 * np.exp(-.05 * 60 / 252))
    assert learner.counts[0, 0, 16] == 2
    assert learner.values[0, 1, 3] == -1
    assert learner.counts[0, 1, 3] == 1


def test_public_learner_supports_largest_choice_and_preserves_default_shape():
    assert CompanyQLearner().values.shape == (3, 81, 3)
    learner = CompanyQLearner(groups=1, epsilon=0, actions=17)
    learner.values[0, 0, 16] = 1
    assert learner.values.shape == learner.counts.shape == (1, 81, 17)
    assert learner.choose(np.array([0]), np.array([0]), np.random.default_rng(1)).tolist() == [16]


def test_multiamplitude_freeze_uses_format_two_and_readonly_dynamic_table(tmp_path):
    learner = CompanyQLearner(groups=6, epsilon=1, actions=17)
    learner.values[5, 80, 16] = .4
    learner.counts[5, 80, 16] = 21
    metadata = {"fractions": list(GRID), "kinds": action_kinds(17).tolist()}
    path = tmp_path / "multi.npz"
    sha = save_frozen(path, learner, metadata)
    with np.load(path, allow_pickle=False) as arrays:
        assert json.loads(str(arrays["metadata"].item()))["format_version"] == 2
    frozen, restored = load_frozen(path, metadata, expected_sha256=sha)
    assert restored == metadata and frozen.epsilon == 0
    assert frozen.values.shape == frozen.counts.shape == (6, 81, 17)
    assert not frozen.values.flags.writeable and not frozen.counts.flags.writeable
    assert table_fingerprint(frozen) == table_fingerprint(learner)
    assert choose_actions(frozen, np.array([5]), np.array([80]), np.ones((1, 17), dtype=bool), None, training=False).tolist() == [16]
    with pytest.raises(ValueError, match="frozen"):
        batch_update(frozen, np.array([0]), np.array([5]), np.array([80]), np.array([16]),
                     np.array([0.]), np.array([5]), np.array([80]), np.ones((1, 17), dtype=bool),
                     elapsed_days=60, annual_discount_rate=.05, terminated=np.array([False]))


def test_preexisting_format_one_table_is_readable_and_new_singleton_still_writes_one(tmp_path):
    values, counts = np.zeros((1, 81, 3)), np.zeros((1, 81, 3), dtype=np.int64)
    values[0, 0], counts[0, 0] = [1, 2, 0], [2, 3, 4]
    payload = '{"format_version":1,"metadata":{"legacy":true},"learning_rate":0.1,"discount":0.9}'
    path = tmp_path / "legacy.npz"
    np.savez_compressed(path, values=values, counts=counts, metadata=np.array(payload))
    frozen, metadata = load_frozen(path, {"legacy": True})
    assert metadata == {"legacy": True}
    np.testing.assert_array_equal(frozen.values, values)
    np.testing.assert_array_equal(frozen.counts, counts)
    assert not frozen.values.flags.writeable and not frozen.counts.flags.writeable
    new_path = tmp_path / "singleton.npz"
    save_frozen(new_path, CompanyQLearner(), {})
    with np.load(new_path, allow_pickle=False) as arrays:
        assert json.loads(str(arrays["metadata"].item()))["format_version"] == 1


@pytest.mark.parametrize("version,actions", [(1, 17), (2, 3), (3, 17), (2, 4)])
def test_freeze_format_must_match_semantic_action_count(tmp_path, version, actions):
    path = tmp_path / "invalid.npz"
    payload = {"format_version": version, "metadata": {}, "learning_rate": .1, "discount": .9}
    np.savez_compressed(path, values=np.zeros((1, 81, actions)),
                        counts=np.zeros((1, 81, actions), dtype=np.int64), metadata=np.array(json.dumps(payload)))
    with pytest.raises(ValueError, match="invalid frozen"):
        load_frozen(path)
