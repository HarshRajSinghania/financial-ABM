from dataclasses import fields, replace

import numpy as np
import pytest

from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.game import IMPROVE, INFLATE, MAINTAIN, DisclosureMarket
from abm.disclosure.learning import load_frozen, save_frozen, table_fingerprint
from abm.disclosure.policy import PolicySchedule
from abm.tabular import CompanyQLearner


DOMAIN = load_domain("configs/domains/esg.json")
CONFIG = MarketConfig(seed=25019, n_investors=24, n_firms=6, trading_days=35, burn_in_days=5,
                      firm_decision_interval=10, imitation_interval=10, initial_impact_share=.5)


def learner_for(action=MAINTAIN, *, groups=3, training=False, epsilon=0, learning_rate=.1):
    learner = CompanyQLearner(groups=groups, epsilon=epsilon, learning_rate=learning_rate)
    learner.values.fill(-1)
    learner.values[:, :, MAINTAIN] = 0
    learner.values[:, :, action] = 2
    learner.counts[:] = 1
    if not training:
        learner.values.flags.writeable = learner.counts.flags.writeable = False
    return learner


def test_learning_mode_requires_explicit_compatible_training_or_frozen_table():
    cfg = replace(CONFIG, firm_policy="q_learning")
    with pytest.raises(ValueError, match="explicit"):
        DisclosureMarket(cfg, DOMAIN)
    with pytest.raises(ValueError, match="only valid"):
        DisclosureMarket(CONFIG, DOMAIN, learner=learner_for())
    with pytest.raises(ValueError, match="only valid"):
        DisclosureMarket(replace(CONFIG, firm_policy="npv_discrete"), DOMAIN, training=True)
    with pytest.raises(ValueError, match="readonly"):
        DisclosureMarket(cfg, DOMAIN, learner=learner_for(training=True))
    with pytest.raises(ValueError, match="epsilon"):
        DisclosureMarket(cfg, DOMAIN, learner=learner_for(epsilon=.1))
    with pytest.raises(ValueError, match="writable"):
        DisclosureMarket(cfg, DOMAIN, learner=learner_for(), training=True)
    policy = PolicySchedule.constant(DOMAIN).with_intervention(20, transparency=.6)
    with pytest.raises(ValueError, match="six"):
        DisclosureMarket(cfg, DOMAIN, policy, learner=learner_for())
    DisclosureMarket(cfg, DOMAIN, policy, learner=learner_for(groups=6))
    assert MarketConfig.from_dict(replace(CONFIG, firm_policy="npv_discrete").to_dict()).firm_policy == "npv_discrete"


def test_continuous_npv_preserves_preintegration_fingerprint():
    cfg = replace(CONFIG, trading_days=70, burn_in_days=10)
    policy = PolicySchedule.constant(DOMAIN).with_intervention(
        31, transparency=.6, disclosure_noise_sd=.02, publish_audit_results=True,
    )
    market = DisclosureMarket(cfg, DOMAIN, policy)
    result = market.run()
    assert market.run_id == "d98180f15b3b0b7f2d380f71e3e37865589a30cf85d7eb02826fe67a7a283b90"
    assert result.fingerprint() == "8f5c1433b49c1e29c08958e9a5446661e2a3df7fc17a4e7739a9ed516555c953"
    assert result.applied_resource_cost is None
    assert result.learning_states is None
    assert result.learning_transition is None


def test_quota_marks_only_training_choices_with_a_complete_following_window():
    config = replace(CONFIG, firm_policy="q_learning", firm_action_fractions=(.01, .5, 1.))
    learner = CompanyQLearner(groups=3, actions=7, epsilon=0)
    result = DisclosureMarket(config, DOMAIN, learner=learner, training=True,
                              coverage_target=20).run()
    assert result.coverage_forced.shape == result.actions.shape
    assert result.coverage_forced[1:3].all()
    assert not result.coverage_forced[[0, 3]].any()
    assert result.learning_transition[2:4].all()
    assert learner.counts.sum() == 12


def test_quota_does_not_change_frozen_evaluation_or_consume_rng():
    config = replace(CONFIG, firm_policy="q_learning")
    ordinary = DisclosureMarket(config, DOMAIN, learner=learner_for())
    learner = learner_for()
    quota = DisclosureMarket(config, DOMAIN, learner=learner, coverage_target=20)
    before = table_fingerprint(learner), quota.firm_rng.bit_generator.state
    first, second = ordinary.run(), quota.run()
    assert first.fingerprint() == second.fingerprint()
    assert first.coverage_forced is second.coverage_forced is None
    assert table_fingerprint(learner) == before[0]
    assert quota.firm_rng.bit_generator.state == before[1]


def test_common_prefix_is_greedy_without_rng_quota_or_updates():
    config = replace(CONFIG, trading_days=25, firm_policy="q_learning")
    policy = PolicySchedule.constant(DOMAIN).with_intervention(21)
    learner = learner_for(groups=6, training=True, epsilon=1)
    market = DisclosureMarket(config, DOMAIN, policy, learner=learner, training=True,
                              coverage_target=20, common_prepolicy_sha256="a" * 64)
    before, rng = table_fingerprint(learner), market.firm_rng.bit_generator.state
    result = market.run()
    np.testing.assert_array_equal(result.actions[1:], MAINTAIN)
    assert result.learning_transition[2].all()
    assert not result.learning_update.any()
    assert not result.coverage_forced.any()
    assert table_fingerprint(learner) == before
    assert market.firm_rng.bit_generator.state == rng


def test_common_prefix_pairs_every_history_and_only_learns_post_switch_sources():
    config = replace(CONFIG, trading_days=55, firm_policy="q_learning",
                     firm_action_fractions=(.01, .02, .04, .08, .16, .32, .64, 1.))
    results = []
    for policy in (PolicySchedule.constant(DOMAIN).with_intervention(21),
                   PolicySchedule.constant(DOMAIN).with_intervention(21, transparency=.9)):
        learner = CompanyQLearner(groups=6, actions=17, epsilon=1)
        learner.values[:3, :, MAINTAIN] = 1
        learner.counts[:3] = 1
        prefix = table_fingerprint(learner, prefix_groups=3)
        result = DisclosureMarket(config, DOMAIN, policy, learner=learner, training=True,
                                  coverage_target=20, common_prepolicy_sha256="a" * 64).run()
        assert table_fingerprint(learner, prefix_groups=3) == prefix
        assert learner.counts[3:].sum() == 12
        assert result.learning_update[4:6].all()
        assert not result.learning_update[:4].any()
        assert result.learning_transition[2:6].all()
        assert result.coverage_forced[3:5].all()
        assert not result.coverage_forced[[0, 1, 2, 5]].any()
        assert np.isfinite(result.learning_rewards[3]).all()
        results.append(result)
    first, second = results
    for item in fields(first):
        if item.name == "market":
            continue
        left, right = getattr(first, item.name), getattr(second, item.name)
        if left is None:
            assert right is None
        else:
            end = 21 if left.shape[0] == config.trading_days + 1 else 3
            np.testing.assert_array_equal(left[:end], right[:end])
    for item in fields(first.market):
        left, right = getattr(first.market, item.name), getattr(second.market, item.name)
        if isinstance(left, np.ndarray) and left.shape[0] == config.trading_days + 1:
            np.testing.assert_array_equal(left[:21], right[:21])
        else:
            np.testing.assert_array_equal(left, right)


def test_common_prefix_requires_an_explicit_switch_even_for_baseline():
    config = replace(CONFIG, firm_policy="q_learning")
    with pytest.raises(ValueError, match="explicit policy switch"):
        DisclosureMarket(config, DOMAIN, learner=learner_for(groups=6), common_prepolicy_sha256="a" * 64)


@pytest.mark.parametrize("action", [IMPROVE, INFLATE])
@pytest.mark.parametrize("delay", [13, 25])
def test_discrete_rules_share_candidates_execution_and_delayed_application(action, delay, monkeypatch):
    domain = replace(DOMAIN, natural_decay=0, cost_level_elasticity=0,
                     baseline_audit_probability=0, baseline_penalty=0,
                     baseline_transparency=1.0 if action == IMPROVE else 0.0,
                     implementation_delay_days=delay, disclosure_delay_days=2)
    discrete = DisclosureMarket(replace(CONFIG, firm_policy="npv_discrete"), domain)
    q_market = DisclosureMarket(replace(CONFIG, firm_policy="q_learning"), domain,
                                learner=learner_for(action, training=True), training=True)
    delta = domain.max_change_per_period * .01
    for market in (discrete, q_market):
        market.attributes.goodness[0] = domain.goodness_bounds[1] - delta / 2
        monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.ones(CONFIG.n_firms))
    results = discrete.run(), q_market.run()
    first, second = results
    for name in ("actions", "amounts", "cost_fraction", "subsidy_fraction", "action_due_day",
                 "true_goodness", "inflation", "valid_actions", "learning_states", "learning_groups",
                 "applied_resource_cost", "applied_fine", "applied_subsidy"):
        np.testing.assert_array_equal(getattr(first, name), getattr(second, name))
    np.testing.assert_array_equal(first.market.prices, second.market.prices)
    np.testing.assert_allclose(first.amounts[1], [delta / 2] + [delta] * (CONFIG.n_firms - 1))
    np.testing.assert_array_equal(first.actions[1], action)
    due = 10 + (delay if action == IMPROVE else 2)
    np.testing.assert_array_equal(first.action_due_day[1], due)
    np.testing.assert_array_equal(first.applied_resource_cost[10], 0)
    np.testing.assert_array_equal(first.applied_resource_cost[11], first.cost_fraction[1] * first.market.prices[10])
    np.testing.assert_array_equal(first.learning_states[1] % 3, 0)
    if action == IMPROVE:
        np.testing.assert_allclose(first.true_goodness[due] - first.true_goodness[due - 1], first.amounts[1])
        np.testing.assert_array_equal(first.learning_states[2, 1:] % 3, 1 if delay == 13 else 2)
    else:
        np.testing.assert_allclose(first.inflation[due] - first.inflation[due - 1], first.amounts[1])
    assert first.unvisited_state is None


def test_audit_fine_is_visible_before_action_but_reward_starts_on_application_day():
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=1, baseline_penalty=.01)
    cfg = replace(CONFIG, firm_policy="q_learning", financing_exposure_fraction=0)
    market = DisclosureMarket(cfg, domain, learner=learner_for())
    market.attributes.inflation[:] = .1
    result = market.run()
    fine = .01 * .1 * result.market.prices[10]
    np.testing.assert_array_equal(result.learning_states[1] % 3, 1)
    np.testing.assert_array_equal(result.learning_states[2] % 3, 0)
    np.testing.assert_array_equal(result.applied_fine[10], 0)
    np.testing.assert_allclose(result.applied_fine[11], fine)
    np.testing.assert_allclose(result.applied_fine.sum(axis=0), fine)
    assert np.isnan(result.learning_rewards[1]).all()
    assert not result.learning_transition[1].any()
    np.testing.assert_allclose(result.learning_rewards[2],
                               -fine * np.exp(-cfg.firm_discount_rate / 252) / result.market.prices[0])
    np.testing.assert_array_equal(result.learning_rewards[3], 0)


def test_new_audit_liability_is_not_charged_to_the_already_closed_window():
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=1,
                     baseline_penalty=.01, disclosure_delay_days=2)
    cfg = replace(CONFIG, firm_policy="q_learning", financing_exposure_fraction=0)
    result = DisclosureMarket(cfg, domain, learner=learner_for(INFLATE)).run()
    prices, rate = result.market.prices, cfg.firm_discount_rate
    first_cost = result.cost_fraction[1] * prices[10]
    fine = domain.baseline_penalty * result.amounts[1] * prices[20]
    np.testing.assert_array_equal(result.learning_states[2] % 3, 1)
    np.testing.assert_array_equal(result.applied_fine[20], 0)
    np.testing.assert_allclose(result.applied_fine[21], fine)
    np.testing.assert_allclose(result.learning_rewards[2], -first_cost * np.exp(-rate / 252) / prices[0])
    second_cost = result.cost_fraction[2] * prices[20]
    np.testing.assert_allclose(result.learning_rewards[3], -(second_cost + fine) * np.exp(-rate / 252) / prices[0])


def test_state_uses_gross_known_cash_and_all_pending_projects():
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=0)
    market = DisclosureMarket(replace(CONFIG, firm_policy="q_learning"), domain, learner=learner_for())
    firms = np.arange(CONFIG.n_firms)
    market.attributes.schedule(1000, IMPROVE, firms, np.full(CONFIG.n_firms, .001))
    market.pending_resource_cost[:] = .1
    market.pending_subsidy[:] = .1
    np.testing.assert_array_equal(market.pending_value_change, 0)
    market._audit_and_decide(10, 1)
    np.testing.assert_array_equal(market.learning_state_history[1] % 3, 1)
    assert market.attributes.pending[0][0] == 1000


def test_last_complete_window_bootstraps_and_partial_tail_does_not_update():
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=0)
    cfg = replace(CONFIG, firm_policy="q_learning", financing_exposure_fraction=0,
                  n_firms=1, n_investors=6)
    learner = learner_for(training=True, learning_rate=1)
    initial_count = int(learner.counts.sum())
    result = DisclosureMarket(cfg, domain, learner=learner, training=True).run()
    assert learner.counts.sum() - initial_count == 2
    np.testing.assert_array_equal(result.learning_transition[:, 0], [False, False, True, True])
    state = result.learning_states[1, 0]
    group = result.learning_groups[1, 0]
    np.testing.assert_array_equal(result.learning_states[1:, 0], state)
    gamma = np.exp(-cfg.firm_discount_rate * cfg.firm_decision_interval / 252)
    assert learner.values[group, state, MAINTAIN] == pytest.approx(2 * gamma**2)
    assert learner.values[group, state, MAINTAIN] > 0


def test_policy_epoch_changes_only_when_active_and_bootstraps_the_next_group():
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=0)
    cfg = replace(CONFIG, firm_policy="q_learning", financing_exposure_fraction=0, trading_days=30)
    policy = PolicySchedule.constant(domain).with_intervention(25, transparency=.6)
    learner = learner_for(groups=6, training=True, learning_rate=1)
    learner.values[:3, :, MAINTAIN] = 1
    learner.values[3:, :, MAINTAIN] = 7
    result = DisclosureMarket(cfg, domain, policy, learner=learner, training=True).run()
    groups = result.market.size_class
    np.testing.assert_array_equal(result.learning_groups[1], groups)
    np.testing.assert_array_equal(result.learning_groups[2], groups)
    np.testing.assert_array_equal(result.learning_groups[3], groups + 3)
    gamma = np.exp(-cfg.firm_discount_rate * cfg.firm_decision_interval / 252)
    for group, state in set(zip(groups, result.learning_states[2])):
        assert learner.values[group, state, MAINTAIN] == pytest.approx(7 * gamma)


def test_firm_exploration_does_not_consume_the_four_old_random_streams():
    domain = replace(DOMAIN, natural_decay=0)
    cfg = replace(CONFIG, trading_days=65, financing_exposure_fraction=0)
    original = DisclosureMarket(cfg, domain)
    learning = DisclosureMarket(replace(cfg, firm_policy="q_learning"), domain,
                                learner=learner_for(training=True, epsilon=1), training=True)
    for market in (original, learning):
        market.attributes.goodness[:] = domain.goodness_bounds[1]
    streams = ("attribute_rng", "audit_rng", "learning_rng", "signal_rng", "fundamental_rng", "noise_rng")
    for name in streams:
        assert getattr(original, name).bit_generator.state == getattr(learning, name).bit_generator.state
    firm_before = learning.firm_rng.bit_generator.state
    first, second = original.run(), learning.run()
    assert first.market.fingerprint() == second.market.fingerprint()
    np.testing.assert_array_equal(first.impact_share, second.impact_share)
    for name in streams:
        assert getattr(original, name).bit_generator.state == getattr(learning, name).bit_generator.state
    assert learning.firm_rng.bit_generator.state != firm_before
    np.testing.assert_array_equal(second.actions, MAINTAIN)


def test_frozen_market_evaluation_never_updates_or_draws_exploration(tmp_path):
    learner = learner_for(IMPROVE, training=True)
    learner.counts.fill(0)
    path = tmp_path / "frozen.npz"
    save_frozen(path, learner, {"reward": "actual ledger"})
    frozen, _ = load_frozen(path)
    before = table_fingerprint(frozen)
    market = DisclosureMarket(replace(CONFIG, firm_policy="q_learning"), DOMAIN, learner=frozen)
    rng_before = market.firm_rng.bit_generator.state
    result = market.run()
    assert table_fingerprint(frozen) == before
    assert market.firm_rng.bit_generator.state == rng_before
    np.testing.assert_array_equal(result.actions, MAINTAIN)
    assert result.unvisited_state[1:].all()
    assert result.learning_transition[2:].all()


def test_changing_candidate_npv_cannot_change_ql_realized_reward(monkeypatch):
    cfg = replace(CONFIG, firm_policy="q_learning", financing_repricing_interval=5)
    results = []
    for predicted in (0, 100):
        market = DisclosureMarket(cfg, DOMAIN, learner=learner_for())
        monkeypatch.setattr(market, "marginal_financing_saving",
                            lambda value=predicted: np.full(CONFIG.n_firms, value))
        results.append(market.run())
    first, second = results
    np.testing.assert_array_equal(first.market.prices, second.market.prices)
    np.testing.assert_array_equal(first.actions, second.actions)
    np.testing.assert_array_equal(first.learning_rewards, second.learning_rewards)
    discounts = np.exp(-cfg.firm_discount_rate * np.arange(1, 11) / 252)
    expected = discounts @ first.financing_value_adjustment[11:21] / first.market.prices[0]
    np.testing.assert_allclose(first.learning_rewards[2], expected)


def test_applied_money_keeps_decision_amount_and_is_booked_once(monkeypatch):
    cfg = replace(CONFIG, firm_policy="npv_discrete", financing_exposure_fraction=0)
    domain = replace(DOMAIN, natural_decay=0, baseline_audit_probability=1,
                     baseline_penalty=.01, baseline_subsidy=.001)
    market = DisclosureMarket(cfg, domain)
    market.attributes.inflation[:] = .1
    monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.ones(CONFIG.n_firms))
    market._audit_and_decide(10, 1)
    cost = market.cost_history[1] * market.prices
    fine = market.penalty_history[1] * market.prices
    subsidy = market.subsidy_history[1] * market.prices
    committed = market.pending_value_change.copy()
    market.prices *= 100
    market.firms.intrinsic_value[:] = 200
    market._pre_trade(11)
    np.testing.assert_array_equal(market.firms.intrinsic_value, 200 + committed)
    np.testing.assert_array_equal(market.applied_resource_cost_history[11], cost)
    np.testing.assert_array_equal(market.applied_fine_history[11], fine)
    np.testing.assert_array_equal(market.applied_subsidy_history[11], subsidy)
    market._pre_trade(12)
    np.testing.assert_array_equal(market.applied_resource_cost_history[12], 0)
    np.testing.assert_array_equal(market.applied_fine_history[12], 0)
    np.testing.assert_array_equal(market.applied_subsidy_history[12], 0)


def test_ql_run_identity_includes_initial_table_counts_hyperparameters_and_mode():
    cfg = replace(CONFIG, firm_policy="q_learning")
    first, second = learner_for(training=True), learner_for(training=True)
    baseline = DisclosureMarket(cfg, DOMAIN, learner=first, training=True).run_id
    assert DisclosureMarket(cfg, DOMAIN, learner=second, training=True).run_id == baseline
    second.counts[0, 0, 0] += 1
    assert DisclosureMarket(cfg, DOMAIN, learner=second, training=True).run_id != baseline
    second = learner_for(training=True, learning_rate=.2)
    assert DisclosureMarket(cfg, DOMAIN, learner=second, training=True).run_id != baseline
    first.values.flags.writeable = first.counts.flags.writeable = False
    assert DisclosureMarket(cfg, DOMAIN, learner=first).run_id != baseline


@pytest.mark.parametrize("choice,kind", [(15, IMPROVE), (16, INFLATE)])
def test_multiple_amplitudes_preserve_semantic_actions_and_update_selected_column(choice, kind, monkeypatch):
    fractions = (.01, .02, .04, .08, .16, .32, .64, 1.)
    cfg = replace(CONFIG, firm_policy="q_learning", firm_action_fractions=fractions)
    domain = replace(DOMAIN, natural_decay=0, cost_level_elasticity=0,
                     baseline_audit_probability=0, baseline_penalty=0,
                     baseline_transparency=1. if kind == IMPROVE else 0.,
                     implementation_delay_days=2, disclosure_delay_days=2)
    learner = CompanyQLearner(groups=3, actions=17, epsilon=0, learning_rate=.1)
    learner.values[:, :, choice] = 1
    market = DisclosureMarket(cfg, domain, learner=learner, training=True)
    market.attributes.goodness[:] = 0
    monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.ones(cfg.n_firms))
    result = market.run()
    comparator = DisclosureMarket(replace(cfg, firm_policy="npv_discrete"), domain)
    comparator.attributes.goodness[:] = 0
    monkeypatch.setattr(comparator, "marginal_financing_saving", lambda: np.ones(cfg.n_firms))
    compared = comparator.run()
    for name in ("actions", "learning_choices", "amounts", "valid_actions", "cost_fraction", "action_due_day"):
        np.testing.assert_array_equal(getattr(result, name), getattr(compared, name))
    np.testing.assert_array_equal(result.market.prices, compared.market.prices)
    np.testing.assert_array_equal(result.actions[1:], kind)
    np.testing.assert_array_equal(result.learning_choices[1:], choice)
    np.testing.assert_array_equal(result.amounts[1:], domain.max_change_per_period)
    assert result.valid_actions.shape == (4, 6, 17)
    assert learner.counts[:, :, choice].sum() == 12
    assert learner.counts.sum() == 12
    np.testing.assert_array_equal(result.applied_resource_cost[11], result.cost_fraction[1] * result.market.prices[10])


@pytest.mark.parametrize("mode", ["npv_discrete", "q_learning"])
def test_known_value_commitments_mask_expensive_candidates_but_allow_subsidized_rescue(mode, monkeypatch):
    cfg = replace(CONFIG, firm_policy=mode, firm_action_fractions=(.01, 1.))
    domain = replace(DOMAIN, cost_level_elasticity=0, baseline_audit_probability=0)
    learner = None
    if mode == "q_learning":
        learner = CompanyQLearner(groups=3, actions=5, epsilon=0)
        learner.values[:, :, 3] = 100
        learner.values.flags.writeable = learner.counts.flags.writeable = False
    market = DisclosureMarket(cfg, domain, learner=learner)
    monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.zeros(cfg.n_firms))
    market.attributes.goodness[:] = 0
    market.attributes.cost_scale[:] = .05
    market.firms.intrinsic_value[:] = 1
    market.prices[:] = 1000
    args = (10, 1, market.policy.baseline, np.zeros(cfg.n_firms, dtype=bool),
            np.zeros(cfg.n_firms), np.ones(cfg.n_firms), np.ones(cfg.n_firms))
    market._discrete_decision(*args)
    assert not market.valid_action_history[1, :, 3].any()
    assert np.all(market.choice_history[1] != 3)

    market.pending_value_change[:] = -1.01
    with pytest.raises(ValueError, match="no feasible firm action"):
        market._discrete_decision(*args)
    regime = replace(market.policy.baseline, subsidy=.1)
    choice = market._discrete_decision(10, 1, regime, *args[3:])
    assert not market.valid_action_history[1, :, MAINTAIN].any()
    np.testing.assert_array_equal(choice.actions, IMPROVE)
    assert np.all(1 + market.pending_value_change + (choice.subsidy_fraction - choice.cost_fraction) * market.prices > 0)
