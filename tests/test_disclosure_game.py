import re
from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest

from abm.disclosure import MarketConfig
from abm.disclosure.config import TRADING_DAYS_PER_YEAR
from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.financing import financing_discount_factors, financing_signal_factors
from abm.disclosure.game import (
    IMPROVE,
    INFLATE,
    MAINTAIN,
    AttributeState,
    DisclosureMarket,
    npv_choices,
    pricing_slope,
    run_disclosure,
)
from abm.disclosure.harness import _cap_buys_to_cash
from abm.disclosure.investors import IMPACT_INVESTOR
from abm.disclosure.market import CrossSectionBook
from abm.disclosure.policy import PolicyRegime, PolicySchedule

ESG = load_domain("configs/domains/esg.json")
SMALL = MarketConfig(n_investors=150, n_firms=30, trading_days=400, burn_in_days=100, initial_impact_share=0.2)


def _regime(**changes):
    base = PolicyRegime(audit_probability=0.02, penalty=0.01, transparency=0.1, subsidy=0.0)
    return replace(base, **changes)


def test_goodness_is_signed_and_standardized():
    lower_is_better = replace(ESG, direction=-1)
    assert ESG.to_goodness(np.array([65.0]))[0] == pytest.approx(1.0)
    assert lower_is_better.to_goodness(np.array([65.0]))[0] == pytest.approx(-1.0)
    np.testing.assert_allclose(lower_is_better.to_raw(lower_is_better.to_goodness(np.array([12.0, 80.0]))), [12.0, 80.0])
    low, high = lower_is_better.goodness_bounds
    assert low < 0 < high


def test_domain_validation_rejects_bad_specs():
    with pytest.raises(ValueError):
        replace(ESG, direction=0)
    with pytest.raises(ValueError):
        replace(ESG, baseline_transparency=1.5)
    with pytest.raises(ValueError):
        DomainSpec.from_dict({**ESG.to_dict(), "colour": "green"})


def test_npv_choice_matches_brute_force_optimum():
    benefit = np.array([0.04, 0.02, 0.0])
    k = np.full(3, 0.06)
    cost = np.array([0.05, 0.3, 0.05])
    regime = _regime()
    choices = npv_choices(benefit=benefit, cost_of_capital=k, marginal_cost=cost, regime=regime,
                          domain=ESG, period_days=60)
    grid = np.linspace(0, ESG.max_change_per_period, 20001)
    real, wash, detection = financing_discount_factors(
        k, decision_day=0, horizon_days=1260, repricing_interval=60, period_days=60,
        implementation_delay=ESG.implementation_delay_days,
        disclosure_delay=ESG.disclosure_delay_days, audit_probability=regime.audit_probability,
    )
    for i in range(3):
        improve_gain = benefit[i] * real[i]
        wash_gain = max(benefit[i] * 0.9 * wash[i] - regime.penalty * detection[i], 0.0)
        best = max(
            (improve_gain * grid - cost[i] * grid**2).max(),
            (wash_gain * grid - ESG.wash_cost_ratio * cost[i] * grid**2).max(),
            0.0,
        )
        assert choices.npv[i] == pytest.approx(best, abs=1e-8)
    assert choices.actions[2] == MAINTAIN and choices.amounts[2] == 0.0


@pytest.mark.parametrize("report_capacity", [0.0, 0.04])
@pytest.mark.parametrize("transparency", [0.0, 0.5, 1.0])
@pytest.mark.parametrize("subsidy", [0.0, 0.02])
def test_improvement_replacing_inflation_matches_observed_signal_brute_force(report_capacity, transparency, subsidy):
    domain = replace(ESG, natural_decay=0.0)
    regime = _regime(transparency=transparency, subsidy=subsidy)
    benefit, k, cost = 0.04, 0.06, 0.2
    goodness = domain.goodness_bounds[1] - 0.5
    inflation = 0.5 - report_capacity
    before = AttributeState(np.array([goodness]), np.array([inflation]), np.array([cost]))
    signal_before = before.observed(transparency)[0]
    choices = npv_choices(
        benefit=np.array([benefit]), cost_of_capital=np.array([k]), marginal_cost=np.array([cost]),
        regime=regime, domain=domain, period_days=60,
        improve_capacity=np.array([0.5]), inflate_capacity=np.array([report_capacity]),
    )
    improve_grid = np.linspace(0.0, domain.max_change_per_period, 20001)
    inflate_grid = np.linspace(0.0, report_capacity, 20001)
    improved = AttributeState(np.full(improve_grid.size, goodness), np.full(improve_grid.size, inflation),
                              np.full(improve_grid.size, cost))
    improved.schedule(1, IMPROVE, np.arange(improve_grid.size), improve_grid)
    improved.advance(1, domain)
    inflated = AttributeState(np.full(inflate_grid.size, goodness), np.full(inflate_grid.size, inflation),
                             np.full(inflate_grid.size, cost))
    inflated.schedule(1, INFLATE, np.arange(inflate_grid.size), inflate_grid)
    inflated.advance(1, domain)
    real, displaced, wash, detection = financing_signal_factors(
        np.array([k]), decision_day=0, horizon_days=1260, repricing_interval=60, period_days=60,
        implementation_delay=domain.implementation_delay_days,
        disclosure_delay=domain.disclosure_delay_days, audit_probability=regime.audit_probability,
        transparency=regime.transparency,
    )
    improve_values = (
        benefit * real[0]
        * (improved.observed(transparency) - signal_before)
        + benefit * (displaced[0] - transparency * real[0]) * np.maximum(improve_grid - report_capacity, 0.0)
        + subsidy * improve_grid - cost * improve_grid**2
    )
    inflate_values = (
        benefit * wash[0] * (inflated.observed(transparency) - signal_before)
        - regime.penalty * inflate_grid * detection[0]
        - domain.wash_cost_ratio * cost * inflate_grid**2
    )
    best = np.array([improve_values.max(), inflate_values.max(), 0.0])
    action = int(np.argmax(best)) if best.max() > 1e-9 else MAINTAIN
    amount = improve_grid[improve_values.argmax()] if action == IMPROVE else (
        inflate_grid[inflate_values.argmax()] if action == INFLATE else 0.0
    )
    assert choices.actions[0] == action
    assert choices.npv[0] == pytest.approx(best.max(), abs=1e-8)
    assert choices.amounts[0] == pytest.approx(amount, abs=domain.max_change_per_period / 20000 + 1e-8)
    if report_capacity == 0.0 and transparency == 0.0 and subsidy == 0.0:
        assert choices.actions[0] == IMPROVE
        assert choices.cost_fraction[0] > 0.0
    if transparency == 1.0:
        assert choices.actions[0] == IMPROVE
        assert choices.amounts[0] > 0.0


def test_changes_are_capped_per_period():
    choices = npv_choices(benefit=np.array([10.0]), cost_of_capital=np.array([0.06]),
                          marginal_cost=np.array([0.01]), regime=_regime(), domain=ESG, period_days=60)
    assert choices.amounts[0] == ESG.max_change_per_period


def test_npv_choices_respect_remaining_attribute_capacity():
    common = dict(benefit=np.full(3, 10.0), cost_of_capital=np.full(3, 0.06),
                  marginal_cost=np.full(3, 0.01), domain=ESG, period_days=60)
    improve = npv_choices(regime=_regime(transparency=1.0),
                          improve_capacity=np.array([0.0, 0.08, 0.4]), inflate_capacity=np.zeros(3), **common)
    np.testing.assert_array_equal(improve.actions, [MAINTAIN, IMPROVE, IMPROVE])
    np.testing.assert_allclose(improve.amounts, [0.0, 0.08, ESG.max_change_per_period])
    assert improve.cost_fraction[0] == 0.0
    inflate = npv_choices(regime=_regime(audit_probability=0.0, transparency=0.0),
                          improve_capacity=np.zeros(3), inflate_capacity=np.array([0.0, 0.05, 0.4]), **common)
    np.testing.assert_array_equal(inflate.actions, [MAINTAIN, INFLATE, INFLATE])
    np.testing.assert_allclose(inflate.amounts, [0.0, 0.05, ESG.max_change_per_period])
    assert inflate.cost_fraction[0] == 0.0


def test_transparency_and_penalty_act_through_different_channels():
    common = dict(benefit=np.array([0.05]), cost_of_capital=np.array([0.06]),
                  marginal_cost=np.array([0.5]), domain=ESG, period_days=60)
    weak = npv_choices(regime=_regime(audit_probability=0.0, transparency=0.0), **common)
    assert weak.actions[0] == INFLATE
    seen_through = npv_choices(regime=_regime(audit_probability=0.0, transparency=1.0), **common)
    assert seen_through.actions[0] != INFLATE
    # With report headroom, transparency leaves genuine improvement's value untouched.
    improve_only = dict(common, marginal_cost=np.array([0.05]))
    assert npv_choices(regime=_regime(transparency=1.0), **improve_only).npv[0] == pytest.approx(
        npv_choices(regime=_regime(transparency=0.0), **improve_only).npv[0])


def test_improvements_and_inflation_arrive_after_their_delays():
    state = AttributeState(goodness=np.zeros(2), inflation=np.zeros(2), cost_scale=np.ones(2))
    domain = replace(ESG, natural_decay=0.0)
    state.schedule(10, IMPROVE, np.array([0]), np.array([0.2]))
    state.schedule(5, INFLATE, np.array([1]), np.array([0.3]))
    state.advance(4, domain)
    assert state.goodness[0] == 0 and state.inflation[1] == 0
    state.advance(5, domain)
    assert state.inflation[1] == pytest.approx(0.3)
    state.advance(10, domain)
    assert state.goodness[0] == pytest.approx(0.2)
    np.testing.assert_allclose(state.observed(transparency=1.0), state.goodness)


def test_reports_cannot_exceed_the_scale():
    high = ESG.goodness_bounds[1]
    state = AttributeState(goodness=np.array([high - 0.1]), inflation=np.zeros(1), cost_scale=np.ones(1))
    state.schedule(1, INFLATE, np.array([0]), np.array([1.0]))
    state.advance(1, replace(ESG, natural_decay=0.0))
    assert state.goodness[0] + state.inflation[0] == pytest.approx(high)


def test_narrow_initial_distribution_has_no_clipped_boundary_mass():
    domain = replace(ESG, raw_lower=49.25, raw_upper=50.75)
    state = AttributeState.initialize(domain, np.zeros(2000, dtype=np.int64), np.random.default_rng(7))
    low, high = domain.goodness_bounds
    assert np.all(state.goodness > low)
    assert np.all(state.goodness < high)


def test_attribute_signal_keeps_initial_standard_deviation_units():
    market = DisclosureMarket(SMALL, ESG)
    market.attributes.goodness[:] = np.linspace(-1.0, 1.0, SMALL.n_firms)
    market.attributes.inflation[:] = 0.2
    market._prepare_signals(1)
    expected = market.attributes.observed(ESG.baseline_transparency)
    np.testing.assert_allclose(market.attribute_signal(), expected)
    market.attributes.goodness += 0.5
    market._prepare_signals(2)
    np.testing.assert_allclose(market.attribute_signal(), expected + 0.5)


@pytest.mark.parametrize("pending", [False, True])
def test_firms_do_not_pay_for_improvements_beyond_capacity(pending):
    domain = replace(ESG, natural_decay=0.0, baseline_transparency=1.0, baseline_subsidy=0.01)
    market = DisclosureMarket(SMALL, domain)
    high = domain.goodness_bounds[1]
    market.attributes.goodness[:] = high - (0.1 if pending else 0.0)
    if pending:
        market.attributes.schedule(120, IMPROVE, np.arange(SMALL.n_firms), np.full(SMALL.n_firms, 0.1))
    market._audit_and_decide(60, 1)
    np.testing.assert_array_equal(market.action_history[1], MAINTAIN)
    np.testing.assert_array_equal(market.amount_history[1], 0.0)
    np.testing.assert_array_equal(market.cost_history[1], 0.0)
    np.testing.assert_array_equal(market.subsidy_history[1], 0.0)


def test_pricing_slope_recovers_a_linear_premium():
    z = np.random.default_rng(1).standard_normal(500)
    k = 0.06 - 0.002 * z
    assert pricing_slope(k, z) == pytest.approx(-0.002)


def test_audit_records_pricing_slope_against_the_pre_audit_signal():
    domain = replace(ESG, baseline_audit_probability=1.0, baseline_transparency=0.0)
    market = DisclosureMarket(SMALL, domain)
    market.attributes.goodness[:] = np.linspace(-1.0, 1.0, SMALL.n_firms)
    market.attributes.inflation[:] = np.linspace(0.0, 0.6, SMALL.n_firms)
    market._prepare_signals(60)
    k = 0.06 - 0.002 * market.attribute_signal()
    market.prices[:] = SMALL.cash_flow_yield * market.firms.intrinsic_value / k
    expected = pricing_slope(market.cost_of_capital(), market.attribute_signal())
    market._audit_and_decide(60, 1)
    assert market.slope_history[60] == pytest.approx(expected)
    np.testing.assert_array_equal(market.attributes.inflation, 0.0)


@pytest.mark.parametrize("seed", range(20))
@pytest.mark.parametrize("zero_policy", [False, True])
def test_without_impact_investors_or_policy_firms_only_decay(seed, zero_policy):
    config = replace(SMALL, seed=seed, initial_impact_share=0.0)
    domain = replace(ESG, baseline_audit_probability=0.0, baseline_penalty=0.0,
                     baseline_transparency=0.0, baseline_subsidy=0.0) if zero_policy else ESG
    result = run_disclosure(config, domain)
    assert np.all(result.actions == MAINTAIN)
    assert np.all(result.inflation == 0.0)
    assert np.all(result.cost_fraction == 0.0)
    years = config.trading_days / 252
    drop = result.true_goodness[0] - result.true_goodness[-1]
    low = domain.goodness_bounds[0]
    expected = np.minimum(domain.natural_decay * years, result.true_goodness[0] - low)
    np.testing.assert_allclose(drop, expected, atol=1e-9)


def test_impact_investors_create_a_signal_premium_and_firms_respond():
    config = replace(SMALL, n_firms=100, n_investors=300, trading_days=1000, initial_impact_share=0.6)
    result = run_disclosure(config, ESG)
    slopes = result.pricing_slope[~np.isnan(result.pricing_slope)]
    assert slopes[1:].mean() < 0
    assert np.any(result.actions != MAINTAIN)


def test_positive_preference_supports_real_improvement_without_subsidy():
    domain = replace(ESG, natural_decay=0.0, baseline_audit_probability=0.0, baseline_penalty=0.0,
                     baseline_transparency=1.0, baseline_subsidy=0.0)
    result = run_disclosure(replace(SMALL, initial_impact_share=0.6), domain)
    assert np.any(result.actions == IMPROVE)
    assert not np.any(result.actions == INFLATE)
    assert result.true_goodness[-1].mean() > result.true_goodness[0].mean()
    assert result.cost_fraction.sum() > 0.0


def test_marginal_signal_value_is_zero_without_preference_or_price_impact():
    market = DisclosureMarket(replace(SMALL, initial_impact_share=0.0), ESG)
    np.testing.assert_array_equal(market.marginal_signal_value(), 0.0)
    market = DisclosureMarket(replace(SMALL, initial_impact_share=1.0, price_impact=0.0), ESG)
    np.testing.assert_array_equal(market.marginal_signal_value(), 0.0)


def test_positive_preference_has_positive_marginal_value_without_changing_state():
    market = DisclosureMarket(replace(SMALL, initial_impact_share=1.0), ESG)
    arrays = [market.prices, market.firms.intrinsic_value, market.investors.cash, market.investors.holdings,
              market.investors.taste, market.attributes.goodness, market.attributes.inflation,
              market.book.variance, market.book.reference_variance, market.book.transient_impact,
              market.book.expected_flow_impact, market.market_covariance]
    before = [array.copy() for array in arrays]
    rngs = [market.fundamental_rng, market.noise_rng, market.attribute_rng, market.audit_rng, market.learning_rng]
    rng_before = [rng.bit_generator.state for rng in rngs]
    values = market.marginal_signal_value()
    assert np.all(values >= 0.0)
    assert np.any(values > 0.0)
    for actual, expected in zip(arrays, before, strict=True):
        np.testing.assert_array_equal(actual, expected)
    assert [rng.bit_generator.state for rng in rngs] == rng_before
    assert market.next_day_index == 0


def test_marginal_signal_value_matches_budget_constrained_permanent_quote_change():
    config = replace(SMALL, initial_impact_share=1.0, permanent_impact_fraction=1.0, rebalance_speed=0.2)
    market = DisclosureMarket(config, ESG)
    market.investors.cash[:] = 0.0
    market.investors.risk_aversion[:] = 0.5
    values = market.marginal_signal_value()
    who = np.arange(config.n_investors)
    expected_returns = market.expected_returns()
    cap_weights = market.prices / market.prices.sum()
    quotes = []
    epsilon = 1e-4
    for change in (0.0, epsilon):
        signal = market.attribute_signal().copy()
        signal[0] += change
        orders = market.investors.desired_orders(
            who, prices=market.prices, expected_returns=expected_returns,
            annual_market_covariance=market.market_covariance * TRADING_DAYS_PER_YEAR,
            market_expected_return=float(cap_weights @ expected_returns),
            market_annual_variance=market.allocation_market_variance * TRADING_DAYS_PER_YEAR,
            attribute=signal, config=config,
        )
        orders = np.maximum(orders, -market.investors.holdings)
        orders = _cap_buys_to_cash(orders, market.investors.cash, market.prices, config.transaction_cost_rate)
        book = CrossSectionBook.initialize(config, config.initial_asset_volatility**2 / TRADING_DAYS_PER_YEAR)
        quote, capped = book.price_moves(orders.sum(axis=0) * market.prices, market.prices,
                                        np.zeros(config.n_firms), np.zeros(config.n_firms))
        assert not np.any(capped)
        quotes.append(quote)
    assert values[0] == pytest.approx((quotes[1][0] - quotes[0][0]) / epsilon, rel=1e-7, abs=1e-10)


def test_equal_performance_leaves_types_unchanged():
    market = DisclosureMarket(SMALL, ESG)
    types = market.investors.investor_type.copy()
    market.window_wealth = market.investors.wealth(market.prices)
    market._imitate()
    np.testing.assert_array_equal(market.investors.investor_type, types)


def test_imitation_moves_towards_the_better_type():
    market = DisclosureMarket(SMALL, ESG)
    impact = market.investors.investor_type == IMPACT_INVESTOR
    market.window_wealth = market.investors.wealth(market.prices) / np.where(impact, 1.05, 1.0)
    before = impact.mean()
    market._imitate()
    after = (market.investors.investor_type == IMPACT_INVESTOR).mean()
    assert after > before
    assert np.all(market.investors.taste[market.investors.investor_type != IMPACT_INVESTOR] == 0)


def test_disclosure_runs_are_reproducible():
    assert run_disclosure(SMALL, ESG).fingerprint() == run_disclosure(SMALL, ESG).fingerprint()


def test_run_id_includes_domain_and_policy():
    market = DisclosureMarket(SMALL, ESG)
    assert market.run_id == DisclosureMarket(SMALL, ESG, PolicySchedule.constant(ESG)).run_id
    assert market.run_id != DisclosureMarket(SMALL, replace(ESG, real_cost_scale=0.1)).run_id
    policy = PolicySchedule.constant(ESG).with_intervention(100, transparency=0.8)
    assert market.run_id != DisclosureMarket(SMALL, ESG, policy).run_id


def test_lower_is_better_domain_runs_as_a_raw_score_mirror():
    mirrored_domain = replace(ESG, name="intensity", attribute_label="Resource intensity", direction=-1)
    result = run_disclosure(SMALL, ESG)
    mirrored = run_disclosure(SMALL, mirrored_domain)
    np.testing.assert_array_equal(result.market.prices, mirrored.market.prices)
    np.testing.assert_array_equal(result.true_goodness, mirrored.true_goodness)
    np.testing.assert_array_equal(result.inflation, mirrored.inflation)
    np.testing.assert_array_equal(result.actions, mirrored.actions)
    np.testing.assert_allclose(ESG.to_raw(result.true_goodness) + mirrored_domain.to_raw(mirrored.true_goodness),
                               2 * ESG.initial_mean)


def test_policy_schedule_switches_regime():
    schedule = PolicySchedule.constant(ESG).with_intervention(100, transparency=0.8)
    assert schedule.at(99).transparency == ESG.baseline_transparency
    assert schedule.at(100).transparency == 0.8


def test_information_intervention_changes_only_transparency():
    baseline = PolicySchedule.constant(ESG)
    schedule = baseline.with_information_intervention(100, transparency=0.8)
    assert schedule.at(99) == baseline.baseline
    assert schedule.at(100) == replace(baseline.baseline, transparency=0.8)


def test_core_modules_name_no_domain():
    banned = re.compile(r"\b(esg|green\w*|carbon|emission\w*|ai[-_ ]washing)\b", re.IGNORECASE)
    for path in Path("src/abm/disclosure").glob("*.py"):
        assert not banned.search(path.read_text(encoding="utf-8")), path.name
