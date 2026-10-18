"""Optional settings for the contract 20.21 robustness checks: reverting true values,
one fixed fine per inflated report, and firm-level wash cost ratios. Defaults keep earlier runs."""

from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure import MarketConfig
from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.financing import financing_signal_factors
from abm.disclosure.game import (
    IMPROVE,
    INFLATE,
    MAINTAIN,
    AttributeState,
    DisclosureMarket,
    expected_natural_path,
    npv_choices,
    real_persistence,
)
from abm.disclosure.learning import discrete_candidates
from abm.disclosure.metrics import compute_metrics
from abm.disclosure.policy import PolicyRegime, PolicySchedule

ESG = load_domain("configs/domains/esg.json")
SMALL = MarketConfig(n_investors=60, n_firms=6, trading_days=130, burn_in_days=10, initial_impact_share=.5)
REGIME = PolicyRegime(audit_probability=.01, penalty=0., transparency=.1, subsidy=0.)
BENEFIT, COST = np.array([5e-4]), np.array([.05])
COMMON = dict(cost_of_capital=np.full(1, .05), domain=ESG, period_days=60)


def factors(persistence=None, **changes):
    options = dict(decision_day=0, horizon_days=1260, repricing_interval=60, period_days=60,
                   implementation_delay=ESG.implementation_delay_days, disclosure_delay=ESG.disclosure_delay_days,
                   audit_probability=.01, transparency=.1)
    options.update(changes)
    return financing_signal_factors(np.full(1, .05), real_persistence=persistence, **options)


# -- defaults ---------------------------------------------------------------

def test_defaults_are_omitted_from_identities_and_validated():
    payload = ESG.to_dict()
    assert "natural_reversion" not in payload and "wash_cost_log_sd" not in payload
    assert replace(ESG, natural_reversion=0., wash_cost_log_sd=0.) == ESG
    assert DisclosureMarket(SMALL, replace(ESG, natural_reversion=0.)).run_id == DisclosureMarket(SMALL, ESG).run_id
    assert DisclosureMarket(SMALL, replace(ESG, natural_reversion=.3)).run_id != DisclosureMarket(SMALL, ESG).run_id
    changed = replace(ESG, natural_reversion=.3, wash_cost_log_sd=.7)
    assert DomainSpec.from_dict(changed.to_dict()) == changed
    for name in ("natural_reversion", "wash_cost_log_sd"):
        for bad in (-.1, np.nan):
            with pytest.raises(ValueError, match=name):
                replace(ESG, **{name: bad})
    assert "fixed_fine_basis" not in REGIME.to_dict()
    per_report = replace(REGIME, fixed_fine=1e-4, fixed_fine_basis="report")
    assert per_report.to_dict()["fixed_fine_basis"] == "report"
    assert PolicyRegime(**per_report.to_dict()) == per_report
    with pytest.raises(ValueError, match="fixed_fine_basis"):
        replace(REGIME, fixed_fine_basis="period")
    schedule = PolicySchedule(per_report).with_intervention(100, transparency=.6)
    assert schedule.at(100).fixed_fine_basis == "report"


def test_default_initialization_draws_nothing_new():
    plain = AttributeState.initialize(ESG, np.array([0, 1, 2, 2]), np.random.default_rng(5))
    assert plain.wash_cost_ratio is None and plain.shock_rng is None
    np.testing.assert_array_equal(plain.false_reports, 0)
    spread = AttributeState.initialize(replace(ESG, wash_cost_log_sd=.7), np.array([0, 1, 2, 2]), np.random.default_rng(5))
    # Firm ratios are drawn last: the other initial draws are those of a common ratio.
    np.testing.assert_array_equal(spread.goodness, plain.goodness)
    np.testing.assert_array_equal(spread.cost_scale, plain.cost_scale)
    result = DisclosureMarket(SMALL, ESG).run()
    assert result.wash_cost_ratio is None


# -- reverting true values ---------------------------------------------------

def test_reversion_shrinks_deviations_and_adds_demeaned_shocks():
    domain = replace(ESG, natural_decay=0., natural_reversion=.5, initial_sd=5.)
    goodness = np.array([-1., 0., .5, 2.5])
    state = AttributeState(goodness.copy(), np.zeros(4), np.ones(4), shock_rng=np.random.default_rng(3))
    state.advance(1, domain)
    shock = np.random.default_rng(3).standard_normal(4)
    retention = np.exp(-.5 / 252)
    expected = goodness.mean() + retention * (goodness - goodness.mean()) + np.sqrt(1 - retention**2) * (shock - shock.mean())
    np.testing.assert_allclose(state.goodness, expected, rtol=0, atol=1e-15)
    assert state.goodness.mean() == pytest.approx(goodness.mean(), abs=1e-15)
    with pytest.raises(ValueError, match="shock"):
        AttributeState(goodness.copy(), np.zeros(4), np.ones(4)).advance(1, domain)


def test_reversion_keeps_the_cross_section_stationary_without_actions():
    domain = replace(ESG, natural_decay=0., natural_reversion=.5, initial_sd=5.)
    rng = np.random.default_rng(11)
    state = AttributeState(rng.standard_normal(4000), np.zeros(4000), np.ones(4000), shock_rng=rng)
    start = state.goodness.copy()
    for day in range(1, 5 * 252 + 1):
        state.advance(day, domain)
    assert state.goodness.mean() == pytest.approx(start.mean(), abs=1e-12)
    assert state.goodness.var() == pytest.approx(start.var(), rel=.06)
    # Five years at 0.5 per year: correlation with the start is exp(-2.5).
    assert np.corrcoef(start, state.goodness)[0, 1] == pytest.approx(np.exp(-2.5), abs=.04)


def test_expected_path_is_the_shock_free_reversion():
    domain = replace(ESG, natural_decay=0., natural_reversion=.4)
    initial = np.array([-1., 0., 2.])
    path = expected_natural_path(domain, initial, np.array([0, 252, 504]))
    np.testing.assert_allclose(path[0], initial)
    np.testing.assert_allclose(path[1:], initial.mean() + np.exp(-.4 * np.array([[1.], [2.]])) * (initial - initial.mean()),
                               rtol=1e-12)
    plain = expected_natural_path(ESG, initial, np.array([252]))
    np.testing.assert_allclose(plain[0], np.maximum(initial - ESG.natural_decay, ESG.goodness_bounds[0]))


def test_persistence_discounts_the_real_annuity_but_not_the_displaced_loss():
    assert real_persistence(ESG, 200, 1260) is None
    domain = replace(ESG, natural_reversion=.32)
    persistence = real_persistence(domain, 200, 1260)
    assert persistence[0] == 1 and persistence[-1] == pytest.approx(1 / 200 + 199 / 200 * np.exp(-.32 * 1260 / 252))
    base = factors()
    np.testing.assert_allclose(factors(np.ones(1261)), base, rtol=1e-14)
    real, displaced, wash, fine = factors(persistence)
    times = np.arange(1, 1261)
    quoted = times // 60 * 60 - 1
    due = ESG.implementation_delay_days
    brute = np.sum((quoted >= due) * persistence[np.maximum(quoted - due, 0)] * np.exp(-.05 * times / 252)) / 252
    assert real[0] == pytest.approx(brute, rel=1e-13)
    assert real[0] < base[0][0]
    # Displaced inflation does not come back; wash survival and detection do not depend on reversion.
    assert real[0] - displaced[0] == pytest.approx(base[0][0] - base[1][0], rel=1e-13)
    np.testing.assert_array_equal(wash, base[2])
    np.testing.assert_array_equal(fine, base[3])
    with pytest.raises(ValueError, match="daily reports"):
        factors(persistence, publish_audit_results=True)
    with pytest.raises(ValueError, match="daily reports"):
        factors(persistence, reporting_interval_days=20)
    with pytest.raises(ValueError, match="daily reports"):
        DisclosureMarket(SMALL, domain, PolicySchedule.constant(domain).with_information_intervention(
            60, reporting_interval_days=20))


def test_reversion_raises_the_transparency_threshold_to_its_closed_form():
    domain = replace(ESG, natural_reversion=.5)
    persistence = real_persistence(domain, 200, 1260)
    real, _, wash, _ = factors(persistence)
    threshold = 1 - np.sqrt(ESG.wash_cost_ratio) * real[0] / wash[0]
    plain_real, _, plain_wash, _ = factors()
    assert threshold > 1 - np.sqrt(ESG.wash_cost_ratio) * plain_real[0] / plain_wash[0] + .2
    benefit = np.array([2e-4])
    for transparency, action in ((threshold - 1e-3, INFLATE), (threshold + 1e-3, IMPROVE)):
        regime = replace(REGIME, transparency=transparency)
        choice = npv_choices(benefit=benefit, marginal_cost=COST, regime=regime, real_persistence=persistence, **COMMON)
        assert choice.actions[0] == action
        assert choice.amounts[0] < ESG.max_change_per_period


def test_no_action_run_with_reversion_has_zero_mean_change_and_zero_decay_adjusted_gain():
    domain = replace(ESG, natural_decay=0., natural_reversion=.5, initial_sd=5.)
    config = replace(SMALL, taste_median=0.)
    market = DisclosureMarket(config, domain)
    result = market.run()
    assert np.all(result.actions == MAINTAIN)
    assert result.true_goodness.std(axis=0).max() > 0
    np.testing.assert_allclose(result.true_goodness.mean(axis=1), result.true_goodness[0].mean(), rtol=0, atol=1e-13)
    metrics = compute_metrics(result, config, domain)
    assert metrics["true_change"]["equal_weight_sd"] == pytest.approx(0, abs=1e-13)
    assert metrics["decay_adjusted_gain"]["equal_weight_sd"] == pytest.approx(0, abs=1e-13)
    assert metrics["terminal_year"]["decay_adjusted_from_initial_sd"] == pytest.approx(0, abs=1e-13)


# -- one fixed fine per inflated report --------------------------------------

class NoAudit:
    def random(self, size):
        return np.ones(size)


def market_with_benefit(basis="case", policy="npv", benefit=2e-3, trading_days=SMALL.trading_days, **domain_changes):
    config = replace(SMALL, firm_policy=policy, firm_action_fractions=(1.,) if policy == "npv_discrete" else (.01,),
                     trading_days=trading_days)
    domain = replace(ESG, natural_decay=0., **domain_changes)
    regime = replace(PolicyRegime.baseline(domain), fixed_fine_basis=basis)
    market = DisclosureMarket(config, domain, PolicySchedule(regime))
    market.marginal_financing_saving = lambda: np.full(SMALL.n_firms, benefit)
    market.attributes.cost_scale[:] = .05
    market.attributes.goodness[:] = 0.
    return market


def test_reports_are_counted_on_disclosure_and_cleared_with_the_stock():
    state = AttributeState(np.zeros(3), np.array([.1, 0., .2]), np.ones(3), false_reports=np.array([1, 0, 2]))
    state.schedule(5, INFLATE, np.array([0, 1, 2]), np.array([.1, .1, 0.]))
    state.advance(4, ESG)
    np.testing.assert_array_equal(state.false_reports, [1, 0, 2])
    state.advance(5, ESG)
    np.testing.assert_array_equal(state.false_reports, [2, 1, 2])
    # Real improvement up to the report bound clears the stock without an audit.
    state.schedule(6, IMPROVE, np.array([2]), np.array([10.]))
    state.advance(6, ESG)
    np.testing.assert_array_equal(state.false_reports, [2, 1, 0])


@pytest.mark.parametrize("policy", ["npv", "npv_discrete"])
def test_detection_charges_one_fixed_fine_per_report(policy):
    fine = 3e-3
    market = market_with_benefit("report", policy, baseline_audit_probability=1., baseline_penalty=0.,
                                 baseline_fixed_fine=fine)
    market.attributes.inflation[:] = [0., .01, .5, 0., .2, 0.]
    market.attributes.false_reports[:] = [0, 1, 3, 0, 2, 0]
    market._audit_and_decide(60, 1)
    np.testing.assert_allclose(market.penalty_history[1] * market.prices, fine * np.array([0, 1, 3, 0, 2, 0]), rtol=1e-12)
    np.testing.assert_array_equal(market.attributes.false_reports, 0)
    case = market_with_benefit("case", policy, baseline_audit_probability=1., baseline_penalty=0., baseline_fixed_fine=fine)
    case.attributes.inflation[:] = [0., .01, .5, 0., .2, 0.]
    case.attributes.false_reports[:] = [0, 1, 3, 0, 2, 0]
    case._audit_and_decide(60, 1)
    np.testing.assert_allclose(case.penalty_history[1] * case.prices, fine * np.array([0, 1, 1, 0, 1, 0]), rtol=1e-12)


@pytest.mark.parametrize("policy", ["npv", "npv_discrete"])
def test_inflation_joining_an_open_case_pays_its_own_fine_per_report(policy):
    open_case = np.array([.3, .3, .3, 0., 0., 0.])
    markets = {basis: market_with_benefit(basis, policy, baseline_penalty=0., baseline_fixed_fine=1.)
               for basis in ("case", "report")}
    for market in markets.values():
        market.audit_rng = NoAudit()
        market.attributes.inflation[:] = open_case
        market.attributes.false_reports[:] = [1, 1, 1, 0, 0, 0]
        market._audit_and_decide(60, 1)
    np.testing.assert_array_equal(markets["case"].action_history[1, :3], INFLATE)
    assert not np.any(markets["report"].action_history[1] == INFLATE)


class AuditOnDay240:
    """Decision days 60, 120 and 180 pass unchecked; every firm is checked on day 240."""

    def __init__(self):
        self.calls = 0

    def random(self, size):
        self.calls += 1
        return np.zeros(size) if self.calls == 4 else np.ones(size)


@pytest.mark.parametrize("basis", ["case", "report"])
def test_run_charges_the_reports_accumulated_before_detection(basis):
    fine = 1e-6
    market = market_with_benefit(basis, trading_days=300, baseline_penalty=0., baseline_fixed_fine=fine)
    market.audit_rng = AuditOnDay240()
    result = market.run()
    washes = (result.actions[1:4] == INFLATE).sum(axis=0)
    assert washes.max() == 3
    np.testing.assert_array_equal(result.detections[4], washes > 0)
    charged = result.penalty_fraction[4] * result.market.prices[240] / fine
    np.testing.assert_allclose(charged, washes if basis == "report" else (washes > 0), rtol=1e-9)


# -- firm-level wash cost ratios --------------------------------------------

def test_firm_ratios_are_a_mean_preserving_lognormal():
    domain = replace(ESG, wash_cost_log_sd=np.log(2))
    state = AttributeState.initialize(domain, np.zeros(200000, dtype=np.int64), np.random.default_rng(1))
    assert state.wash_cost_ratio.mean() == pytest.approx(ESG.wash_cost_ratio, rel=.01)
    assert np.log(state.wash_cost_ratio).std() == pytest.approx(np.log(2), rel=.01)
    result = DisclosureMarket(SMALL, replace(domain, wash_cost_ratio=.2)).run()
    assert result.wash_cost_ratio.shape == (SMALL.n_firms,)


def test_firm_ratios_set_firm_thresholds():
    ratios = np.array([.05, .2, .4])
    real, _, wash, _ = factors()
    thresholds = 1 - np.sqrt(ratios) * real[0] / wash[0]
    common = dict(benefit=np.full(3, 2e-4), marginal_cost=np.full(3, .05), cost_of_capital=np.full(3, .05),
                  domain=ESG, period_days=60)
    regime = replace(REGIME, transparency=float(np.mean(thresholds[:2])))
    choices = npv_choices(regime=regime, wash_cost_ratio=ratios, **common)
    np.testing.assert_array_equal(choices.actions, [INFLATE, IMPROVE, IMPROVE])
    for index, ratio in enumerate(ratios):
        alone = npv_choices(regime=regime, **{**common, "domain": replace(ESG, wash_cost_ratio=float(ratio))})
        assert choices.actions[index] == alone.actions[index]
        assert choices.amounts[index] == alone.amounts[index]


def test_discrete_candidates_accept_firm_ratios():
    common = dict(improve_capacity=np.array([.25, .25]), inflate_capacity=np.array([.25, .25]),
                  marginal_cost=np.array([.05, .05]), max_change_per_period=.25, subsidy=0.,
                  real_value_per_sd=np.full(2, .01), displaced_real_value_per_sd=np.full(2, .001),
                  wash_value_per_sd=np.full(2, .02), fine_value_per_sd=np.zeros(2), amplitude_fractions=(.1, 1.))
    mixed = discrete_candidates(wash_cost_ratio=np.array([.1, .4]), **common)
    for index, ratio in enumerate((.1, .4)):
        alone = discrete_candidates(wash_cost_ratio=ratio, **common)
        np.testing.assert_array_equal(mixed.values[index], alone.values[index])
        np.testing.assert_array_equal(mixed.cost_fraction[index], alone.cost_fraction[index])
    for bad in (np.array([.1]), np.array([.1, 0.]), np.array([.1, np.nan])):
        with pytest.raises(ValueError, match="ratios"):
            discrete_candidates(wash_cost_ratio=bad, **common)
