"""Signals that saturate at the best raw end (research contract section 17)."""

from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure import MarketConfig
from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.game import IMPROVE, INFLATE, MAINTAIN, AttributeState, DisclosureMarket

ESG = load_domain("configs/domains/esg.json")
SUPPORT = ((40.0, 3), (60.0, 4), (80.0, 2), (100.0, 1))
SMALL = MarketConfig(n_investors=60, n_firms=6, trading_days=130, burn_in_days=10, initial_impact_share=.5)


def quantile_domain(support=SUPPORT, **changes) -> DomainSpec:
    values, counts = np.asarray(support).T
    mean = float(np.average(values, weights=counts))
    sd = float(np.sqrt(np.average((values - mean)**2, weights=counts)))
    base = replace(ESG, initial_empirical_distribution=tuple((float(v), int(c)) for v, c in support),
                   initial_mean=mean, initial_sd=sd, observation_link="empirical_quantile")
    return replace(base, **changes)


SATURATED = quantile_domain(signal_saturation=True)
CEILING = SATURATED.observation_ceiling


def test_ceiling_is_the_latent_value_of_the_observed_best_end():
    plain = quantile_domain()
    assert plain.observation_ceiling is None and plain.report_bound == plain.goodness_bounds[1] == 6.0
    assert CEILING == pytest.approx(float(SATURATED.to_goodness(np.array([100.0]))[0]))
    assert 0 < CEILING < 6 and SATURATED.report_bound == CEILING
    # Every latent value above the ceiling reads as the raw maximum.
    np.testing.assert_array_equal(SATURATED.to_raw(np.array([CEILING, CEILING + .5, 6.0])), 100.0)
    assert "signal_saturation" not in plain.to_dict()
    assert DomainSpec.from_dict(SATURATED.to_dict()) == SATURATED
    # Lower is better: the best end is the raw minimum.
    lower_is_better = quantile_domain(support=((0.0, 1), (20.0, 4), (40.0, 3)), direction=-1, signal_saturation=True)
    assert lower_is_better.observation_ceiling == pytest.approx(float(lower_is_better.to_goodness(np.array([0.0]))[0]))
    assert 0 < lower_is_better.observation_ceiling < 6


def test_saturation_is_validated():
    with pytest.raises(ValueError, match="quantile link"):
        replace(ESG, signal_saturation=True)
    with pytest.raises(ValueError, match="best scale end"):
        quantile_domain(support=((40.0, 3), (60.0, 4), (90.0, 1)), signal_saturation=True)
    with pytest.raises(ValueError, match="worst scale end"):
        quantile_domain(support=((0.0, 1), (60.0, 4), (100.0, 1)), signal_saturation=True)
    with pytest.raises(ValueError, match="boolean"):
        quantile_domain(signal_saturation=1)


def test_signals_and_certificates_saturate_without_changing_values_below_the_ceiling():
    goodness = np.array([CEILING - 1.0, CEILING - .2, CEILING + .1, CEILING + 1.0])
    inflation = np.array([.3, .2, 0., 0.])
    plain = AttributeState(goodness.copy(), inflation.copy(), np.ones(4))
    capped = AttributeState(goodness.copy(), inflation.copy(), np.ones(4), ceiling=CEILING)
    signal = capped.observed(.1)
    np.testing.assert_array_equal(signal[:2], plain.observed(.1)[:2])
    # Firms above the observable maximum look the same.
    np.testing.assert_array_equal(signal[2:], CEILING)
    np.testing.assert_array_equal(capped.certified(np.array([0, 2, 3])), [goodness[0], CEILING, CEILING])


def test_reports_stop_at_the_observable_maximum_and_improvement_replaces_inflation():
    domain = replace(SATURATED, natural_decay=0.)
    state = AttributeState(np.array([CEILING - .3, CEILING - .3, CEILING + .5]), np.zeros(3), np.ones(3), ceiling=CEILING)
    state.schedule(1, INFLATE, np.array([0, 2]), np.array([.2, .2]))
    state.schedule(1, INFLATE, np.array([1]), np.array([.5]))
    state.advance(1, domain)
    np.testing.assert_allclose(state.inflation, [.2, .3, 0.])
    state.schedule(2, IMPROVE, np.array([0]), np.array([.25]))
    state.advance(2, domain)
    np.testing.assert_allclose(state.goodness[0] + state.inflation[0], CEILING)
    assert state.inflation[0] == pytest.approx(.05)
    # A true value drawn above the ceiling stays latent.
    assert state.goodness[2] == pytest.approx(CEILING + .5)


def market(benefit=2e-3, policy="npv", **domain_changes):
    config = replace(SMALL, firm_policy=policy, firm_action_fractions=(1.,) if policy == "npv_discrete" else (.01,))
    domain = replace(SATURATED, **{"natural_decay": 0., "baseline_audit_probability": 0., "baseline_penalty": 0.,
                                   **domain_changes})
    result = DisclosureMarket(config, domain)
    result.marginal_financing_saving = lambda: np.full(SMALL.n_firms, benefit)
    result.attributes.cost_scale[:] = .05
    return result


@pytest.mark.parametrize("policy", ["npv", "npv_discrete"])
def test_firms_choose_only_visible_changes(policy):
    item = market(policy=policy)
    item.attributes.goodness[:] = [CEILING - 1., CEILING - .05, CEILING, CEILING + .4, CEILING - 1., CEILING - .3]
    item.attributes.inflation[:] = [0., 0., 0., 0., .5, .3]
    item._audit_and_decide(60, 1)
    actions, amounts = item.action_history[1], item.amount_history[1]
    room = np.maximum(CEILING - item.attributes.goodness - item.attributes.inflation, 0)
    assert actions[0] == INFLATE and amounts[0] > .05
    assert np.all(amounts[actions == INFLATE] <= room[actions == INFLATE] + 1e-12)
    # At or above the ceiling nothing is visible; with inflation at the ceiling only
    # improvement that replaces it remains.
    np.testing.assert_array_equal(actions[[2, 3]], MAINTAIN)
    assert actions[5] != INFLATE
    assert actions[1] in (INFLATE, IMPROVE) and amounts[1] <= .05 + 1e-12


def test_published_audits_and_traded_signals_never_exceed_the_ceiling():
    item = market(baseline_audit_probability=1., baseline_transparency=0.)
    item.policy = replace(item.policy, baseline=replace(item.policy.baseline, publish_audit_results=True))
    item.attributes.goodness[:] = np.linspace(CEILING - 1.5, CEILING + 1., SMALL.n_firms)
    result = item.run()
    assert np.all(result.public_signal <= CEILING)
    assert np.all(result.planning_signal <= CEILING)
    assert np.all(result.verified_goodness <= CEILING)
    report = result.true_goodness + result.inflation
    assert np.all(report <= np.maximum(CEILING, result.true_goodness) + 1e-12)
    assert result.true_goodness[1].max() > CEILING


def test_saturation_off_keeps_the_previous_rules():
    plain = quantile_domain()
    assert replace(plain, signal_saturation=False) == plain
    item = DisclosureMarket(SMALL, plain)
    assert item.attributes.ceiling is None and item.report_bound == plain.goodness_bounds[1]
    assert DisclosureMarket(SMALL, plain).run_id != DisclosureMarket(SMALL, SATURATED).run_id
