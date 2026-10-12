from dataclasses import fields, replace
from itertools import product

import numpy as np
import pytest

from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.financing import financing_signal_factors
from abm.disclosure.game import IMPROVE, INFLATE, MAINTAIN, DisclosureMarket, npv_choices
from abm.disclosure.policy import PolicyRegime, PolicySchedule
from abm.disclosure.runner import load_result, save_result
from abm.tabular import CompanyQLearner


DOMAIN = load_domain("configs/domains/esg.json")
CONFIG = MarketConfig(n_investors=36, n_firms=6, trading_days=90, burn_in_days=30,
                      seed=31701, initial_impact_share=1.0, firm_decision_interval=6,
                      financing_repricing_interval=6, financing_horizon_days=36)
INFORMATION_FIELDS = ("public_signal", "planning_signal", "disclosure_error", "audit_selected",
                      "audit_publications", "verified_goodness", "action_due_day")


def test_information_intervention_keeps_enforcement_and_transfer_instruments_fixed():
    baseline = PolicySchedule(PolicyRegime(.3, .04, .1, .02, disclosure_noise_sd=.4))
    schedule = baseline.with_information_intervention(
        31, transparency=.6, disclosure_noise_sd=0.0, disclosure_delay_days=0,
        publish_audit_results=True, reporting_interval_days=7,
    )
    assert schedule.at(30) == baseline.baseline
    regime = schedule.at(31)
    assert (regime.audit_probability, regime.penalty, regime.subsidy) == (.3, .04, .02)
    assert (regime.transparency, regime.disclosure_noise_sd, regime.disclosure_delay_days,
            regime.publish_audit_results, regime.reporting_interval_days) == (.6, 0.0, 0, True, 7)


@pytest.mark.parametrize("changes", [
    {"disclosure_noise_sd": -1.0}, {"disclosure_noise_sd": float("inf")},
    {"disclosure_noise_sd": float("nan")}, {"disclosure_delay_days": -1},
    {"disclosure_delay_days": 1.5}, {"disclosure_delay_days": True},
    {"publish_audit_results": 1},
    {"reporting_interval_days": 0}, {"reporting_interval_days": -1},
    {"reporting_interval_days": 1.5}, {"reporting_interval_days": True},
])
def test_information_parameters_reject_invalid_units(changes):
    with pytest.raises(ValueError):
        replace(PolicyRegime.baseline(DOMAIN), **changes)


def test_daily_error_is_fixed_and_close_correction_does_not_rewrite_trading_signal():
    config = replace(CONFIG, firm_decision_interval=4, financing_exposure_fraction=0.0)
    domain = replace(DOMAIN, natural_decay=0.0)
    regime = PolicyRegime(1.0, 0.0, .2, 0.0, disclosure_noise_sd=.4)
    market = DisclosureMarket(config, domain, PolicySchedule(regime))
    market.attributes.goodness[:] = 0.0
    market.attributes.inflation[:] = .3
    market._prepare_signals(4)
    trading = market.signal_z(4)
    error = market.disclosure_error_history[4].copy()
    rng_state = market.signal_rng.bit_generator.state
    assert np.ptp(error) > 0
    for _ in range(3):
        np.testing.assert_array_equal(market.attribute_signal(), trading)
        market.marginal_signal_value()
    assert market.signal_rng.bit_generator.state == rng_state
    market._audit_and_decide(4, 1)
    np.testing.assert_array_equal(market.signal_z(4), trading)
    np.testing.assert_array_equal(market.disclosure_error_history[4], error)
    np.testing.assert_allclose(market.attribute_signal(), error)
    np.testing.assert_allclose(trading - market.attribute_signal(), .24)
    assert market.signal_rng.bit_generator.state == rng_state
    np.testing.assert_array_equal(market.action_history[1], MAINTAIN)
    with pytest.raises(ValueError, match="not been prepared"):
        market.signal_z(5)


def test_future_error_stream_is_not_used_by_current_npv():
    policy = PolicySchedule(PolicyRegime(.5, .01, .2, 0.0, disclosure_noise_sd=.4,
                                         publish_audit_results=True))
    first = DisclosureMarket(CONFIG, DOMAIN, policy)
    second = DisclosureMarket(CONFIG, DOMAIN, policy)
    for market in (first, second):
        market._prepare_signals(6)
    second.signal_rng.standard_normal(100)
    for market in (first, second):
        market._audit_and_decide(6, 1)
    np.testing.assert_array_equal(first.planning_signal_history[6], second.planning_signal_history[6])
    np.testing.assert_array_equal(first.action_history[1], second.action_history[1])
    np.testing.assert_array_equal(first.amount_history[1], second.amount_history[1])


def test_public_snapshot_is_dated_finite_and_survives_publication_switch_off():
    config = replace(CONFIG, firm_decision_interval=4, financing_exposure_fraction=0.0)
    domain = replace(DOMAIN, natural_decay=0.0)
    baseline = PolicyRegime(1.0, 0.0, .2, 0.0, disclosure_noise_sd=.4,
                            publish_audit_results=True)
    policy = PolicySchedule(baseline).with_information_intervention(6, publish_audit_results=False)
    market = DisclosureMarket(config, domain, policy)
    market.attributes.goodness[:] = np.linspace(-.5, .5, config.n_firms)
    market._prepare_signals(4)
    old_signal = market.signal_z(4)
    snapshot = market.attributes.goodness.copy()
    market._audit_and_decide(4, 1)
    np.testing.assert_array_equal(market.detection_history[1], 0)
    np.testing.assert_array_equal(market.audit_selected_history[1], 1)
    np.testing.assert_array_equal(market.publication_history[1], 1)
    np.testing.assert_array_equal(market.signal_z(4), old_signal)
    market._pre_trade(5)
    np.testing.assert_array_equal(market.attribute_signal(), snapshot)
    market.attributes.goodness += .2
    for day in (6, 7, 8):
        market._pre_trade(day)
        np.testing.assert_array_equal(market.attribute_signal(), snapshot)
    market._audit_and_decide(8, 2)
    np.testing.assert_array_equal(market.publication_history[2], 0)
    market._pre_trade(9)
    np.testing.assert_array_equal(market.attribute_signal(),
                                  market.attributes.goodness + market.disclosure_error_history[9])


def test_publication_switch_on_does_not_publish_earlier_private_audit():
    config = replace(CONFIG, firm_decision_interval=4, financing_exposure_fraction=0.0)
    baseline = PolicyRegime(1.0, 0.0, .2, 0.0, disclosure_noise_sd=.4)
    policy = PolicySchedule(baseline).with_information_intervention(6, publish_audit_results=True)
    market = DisclosureMarket(config, replace(DOMAIN, natural_decay=0.0), policy)
    market._audit_and_decide(4, 1)
    market._pre_trade(6)
    np.testing.assert_array_equal(market.publication_history[1], 0)
    np.testing.assert_array_equal(market.attribute_signal(),
                                  market.attributes.goodness + market.disclosure_error_history[6])


@pytest.mark.parametrize("kind", [IMPROVE, INFLATE])
@pytest.mark.parametrize("due", [5, 8])
def test_completed_projects_wait_for_the_global_report_calendar(kind, due):
    config = replace(CONFIG, financing_exposure_fraction=0.0)
    domain = replace(DOMAIN, natural_decay=0.0)
    policy = PolicySchedule(PolicyRegime(0.0, 0.0, 0.0, 0.0, reporting_interval_days=4))
    market = DisclosureMarket(config, domain, policy)
    market.attributes.goodness[:] = 0.0
    for day in range(1, 5):
        market._pre_trade(day)
    market.attributes.schedule(due, kind, np.arange(config.n_firms), np.full(config.n_firms, .1))
    for day in range(5, 9):
        market._pre_trade(day)
        actual = market.attributes.goodness if kind == IMPROVE else market.attributes.inflation
        np.testing.assert_array_equal(actual, .1 if day >= due else 0.0)
        np.testing.assert_array_equal(market.signal_z(day), .1 if day == 8 else 0.0)


def test_selected_checks_refresh_only_the_checked_reports_at_close(monkeypatch):
    config = replace(CONFIG, firm_decision_interval=4, financing_exposure_fraction=0.0)
    regime = PolicyRegime(.5, 0.0, .2, 0.0, disclosure_noise_sd=.4, reporting_interval_days=7)
    market = DisclosureMarket(config, replace(DOMAIN, natural_decay=0.0), PolicySchedule(regime))
    for day in range(1, 4):
        market._pre_trade(day)
    market.attributes.goodness[:] = np.linspace(-.4, .4, config.n_firms)
    market.attributes.inflation[:3] = .2
    market._pre_trade(4)
    trading = market.signal_z(4)
    selected = np.random.default_rng(1).random(config.n_firms) < .5
    monkeypatch.setattr(market, "audit_rng", np.random.default_rng(1))
    assert selected[:3].any() and selected[3:].any() and (~selected).any()
    expected = trading.copy()
    expected[selected] = market.attributes.goodness[selected] + market.disclosure_error_history[4, selected]
    market._audit_and_decide(4, 1)
    np.testing.assert_array_equal(market.signal_z(4), trading)
    np.testing.assert_array_equal(market.attribute_signal(), expected)
    np.testing.assert_array_equal(market.audit_selected_history[1], selected)
    np.testing.assert_array_equal(market.detection_history[1, 3:], 0)
    market._pre_trade(5)
    np.testing.assert_array_equal(market.attribute_signal(), expected)


@pytest.mark.parametrize("interval", [3, 7])
def test_reporting_switch_uses_global_multiples_and_keeps_pending_due_dates(interval):
    config = replace(CONFIG, financing_exposure_fraction=0.0)
    baseline = PolicyRegime(0.0, 0.0, 0.0, 0.0, reporting_interval_days=4)
    policy = PolicySchedule(baseline).with_information_intervention(5, reporting_interval_days=interval)
    market = DisclosureMarket(config, replace(DOMAIN, natural_decay=0.0), policy)
    market.attributes.goodness[:] = 0.0
    for day in range(1, 5):
        market._pre_trade(day)
    market.attributes.schedule(6, IMPROVE, np.arange(config.n_firms), np.full(config.n_firms, .1))
    market._pre_trade(5)
    assert market.attributes.pending[0][0] == 6
    np.testing.assert_array_equal(market.attribute_signal(), 0.0)
    first_report = 6 if interval == 3 else 7
    for day in range(6, first_report + 1):
        market._pre_trade(day)
        np.testing.assert_array_equal(market.attributes.goodness, .1)
        np.testing.assert_array_equal(market.attribute_signal(), .1 if day == first_report else 0.0)


def test_report_holds_its_quality_and_error_until_refresh_without_skipping_noise_draws():
    config = replace(CONFIG, financing_exposure_fraction=0.0)
    domain = replace(DOMAIN, natural_decay=0.0)
    baseline = PolicyRegime(0.0, 0.0, 0.0, 0.0, disclosure_noise_sd=.4, reporting_interval_days=4)
    policy = PolicySchedule(baseline).with_information_intervention(5, transparency=1.0, disclosure_noise_sd=0.0)
    market = DisclosureMarket(config, domain, policy)
    control = DisclosureMarket(config, domain, PolicySchedule(baseline))
    market.attributes.goodness[:] = 0.0
    market.attributes.inflation[:] = .2
    for day in range(1, 5):
        market._pre_trade(day)
        control._pre_trade(day)
    report = market.signal_z(4)
    np.testing.assert_array_equal(report, .2 + market.disclosure_error_history[4])
    for day in range(5, 9):
        market._pre_trade(day)
        control._pre_trade(day)
        np.testing.assert_array_equal(market.disclosure_error_history[day], 0.0)
        np.testing.assert_array_equal(market.attribute_signal(), report if day < 8 else 0.0)
    assert market.signal_rng.bit_generator.state == control.signal_rng.bit_generator.state


def test_certificate_expiry_returns_to_the_report_updated_while_it_was_hidden():
    config = replace(CONFIG, firm_decision_interval=4, financing_exposure_fraction=0.0)
    baseline = PolicyRegime(1.0, 0.0, .2, 0.0, disclosure_noise_sd=.4,
                            publish_audit_results=True, reporting_interval_days=6)
    policy = PolicySchedule(baseline).with_intervention(6, audit_probability=0.0, publish_audit_results=False)
    market = DisclosureMarket(config, replace(DOMAIN, natural_decay=0.0), policy)
    market.attributes.goodness[:] = 0.0
    for day in range(1, 5):
        market._pre_trade(day)
    market._audit_and_decide(4, 1)
    market.attributes.goodness[:] = .2
    for day in (5, 6):
        market._pre_trade(day)
        np.testing.assert_array_equal(market.attribute_signal(), 0.0)
    held_report = .2 + market.disclosure_error_history[6]
    market.attributes.goodness[:] = .3
    for day in (7, 8):
        market._pre_trade(day)
        np.testing.assert_array_equal(market.attribute_signal(), 0.0)
    market._audit_and_decide(8, 2)
    np.testing.assert_array_equal(market.attribute_signal(), 0.0)
    market._pre_trade(9)
    np.testing.assert_array_equal(market.attribute_signal(), held_report)


@pytest.mark.parametrize("firm_policy", ["npv", "npv_discrete"])
def test_firm_rules_do_not_value_reports_beyond_the_financing_horizon(firm_policy, monkeypatch):
    config = replace(CONFIG, firm_policy=firm_policy, financing_horizon_days=10)
    domain = replace(DOMAIN, natural_decay=0.0, implementation_delay_days=1, disclosure_delay_days=1)
    actions = []
    for interval in (1, 100):
        policy = PolicySchedule(PolicyRegime(0.0, 0.0, 0.0, 0.0, reporting_interval_days=interval))
        market = DisclosureMarket(config, domain, policy)
        market.attributes.goodness[:] = 0.0
        monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.full(config.n_firms, .1))
        market._audit_and_decide(6, 1)
        actions.append(market.action_history[1].copy())
    assert np.any(actions[0] != MAINTAIN)
    np.testing.assert_array_equal(actions[1], MAINTAIN)


@pytest.mark.parametrize("firm_policy,field_count", [("npv", 31), ("npv_discrete", 40), ("q_learning", 41)])
def test_daily_reporting_preserves_legacy_result_arrays(firm_policy, field_count, tmp_path, monkeypatch):
    fractions = (.01,) if firm_policy == "npv" else (.01, .25, 1.0)
    config = replace(CONFIG, firm_policy=firm_policy, firm_action_fractions=fractions)
    domain = replace(DOMAIN, natural_decay=0.0, implementation_delay_days=3, disclosure_delay_days=2)
    policy = PolicySchedule(PolicyRegime(.5, 0.0, .1, 0.0, disclosure_noise_sd=.4)).with_information_intervention(
        31, transparency=.6, publish_audit_results=True,
    )
    assert policy.baseline.reporting_interval_days == 1
    options = {}
    if firm_policy == "q_learning":
        learner = CompanyQLearner(groups=6, actions=2 * len(fractions) + 1, epsilon=0.0)
        learner.values[:, :, INFLATE] = 1.0
        learner.counts.fill(1)
        learner.values.flags.writeable = learner.counts.flags.writeable = False
        options["learner"] = learner
    market = DisclosureMarket(config, domain, policy, **options)
    reference = DisclosureMarket(config, domain, policy, **options)

    def legacy_public_signal(day):
        signal = reference.attributes.observed(reference.policy.at(day).transparency) + reference.disclosure_error_history[day]
        period = (day - 1) // config.firm_decision_interval
        if period >= 0:
            public = reference.publication_history[period].astype(bool)
            signal[public] = reference.verified_goodness_history[period, public]
        return signal

    monkeypatch.setattr(reference, "_public_signal", legacy_public_signal)
    save_result(tmp_path / "actual.npz", market.run())
    save_result(tmp_path / "legacy.npz", reference.run())
    with np.load(tmp_path / "actual.npz") as actual, np.load(tmp_path / "legacy.npz") as legacy:
        assert set(actual.files) == set(legacy.files)
        assert len(actual.files) == field_count
        for name in actual.files:
            assert actual[name].dtype == legacy[name].dtype
            assert actual[name].shape == legacy[name].shape
            assert actual[name].tobytes() == legacy[name].tobytes(), name


@pytest.mark.parametrize("new_delay", [0, 20])
def test_delay_changes_only_new_projects_and_zero_delay_means_next_day(new_delay, monkeypatch):
    config = replace(CONFIG, firm_decision_interval=4, financing_repricing_interval=3,
                     financing_horizon_days=40)
    domain = replace(DOMAIN, natural_decay=0.0, implementation_delay_days=120,
                     disclosure_delay_days=10)
    baseline = PolicyRegime(0.0, 0.0, 0.0, 0.0)
    policy = PolicySchedule(baseline).with_information_intervention(9, disclosure_delay_days=new_delay)
    market = DisclosureMarket(config, domain, policy)
    market.attributes.goodness[:] = 0.0
    monkeypatch.setattr(market, "marginal_financing_saving", lambda: np.full(config.n_firms, .1))
    market._audit_and_decide(4, 1)
    market._audit_and_decide(8, 2)
    old_projects = [(due, kind, firms.copy(), amounts.copy())
                    for due, kind, firms, amounts in market.attributes.pending]
    assert [item[0] for item in old_projects] == [14, 18]
    market._audit_and_decide(12, 3)
    new_due = 12 + max(1, new_delay)
    np.testing.assert_array_equal(market.action_history[3], INFLATE)
    np.testing.assert_array_equal(market.action_due_history[3], new_due)
    for old, current in zip(old_projects, market.attributes.pending[:2]):
        assert old[:2] == current[:2]
        np.testing.assert_array_equal(old[2], current[2])
        np.testing.assert_array_equal(old[3], current[3])
    np.testing.assert_array_equal(market.attribute_signal(), 0)
    market._pre_trade(13)
    expected = market.amount_history[3] if new_delay == 0 else np.zeros(config.n_firms)
    np.testing.assert_array_equal(market.attribute_signal(), expected)
    market._pre_trade(14)
    np.testing.assert_allclose(market.attribute_signal(), expected + market.amount_history[1])
    assert any(due == 18 for due, *_ in market.attributes.pending)
    if new_delay == 20:
        assert any(due == 32 for due, *_ in market.attributes.pending)


def _enumerated_signal_factors(*, probability, publish, implementation_delay,
                               disclosure_delay, known=False, rate=.08, horizon=16,
                               transparency=.2):
    decision, period, repricing = 4, 4, 3
    real_due = decision + max(1, implementation_delay)
    wash_due = decision + max(1, disclosure_delay)
    audits = list(range(decision + period, decision + horizon + 1, period))
    answer = np.zeros(3)
    for path in product((False, True), repeat=len(audits)):
        chance = np.prod([probability if checked else 1 - probability for checked in path])
        old_alive, wash_alive = True, False
        certificate = decision if publish and known else None
        signals = {}
        for day in range(decision + 1, decision + horizon + 1):
            if day == wash_due:
                wash_alive = True
            real_active = day >= real_due
            certified = certificate is not None and certificate < day <= certificate + period
            if certified:
                real_signal = float(certificate >= real_due)
                signals[day] = (real_signal, real_signal, 0.0)
            else:
                signals[day] = (float(real_active),
                                float(real_active) * (1 - (1 - transparency) * old_alive),
                                float(wash_alive))
            if day in audits and path[audits.index(day)]:
                old_alive = wash_alive = False
                if publish:
                    certificate = day
        for day in range(decision + 1, decision + horizon + 1):
            reprice = max([0] + [d for d in range(1, day + 1) if d % repricing == 0])
            quote = reprice - 1
            if quote in signals:
                answer += chance * np.asarray(signals[quote]) * np.exp(-rate * (day - decision) / 252) / 252
    return answer


@pytest.mark.parametrize("probability", [0.0, .35, 1.0])
@pytest.mark.parametrize("publish", [False, True])
@pytest.mark.parametrize("delays", [(1, 0), (5, 6)])
def test_signal_annuity_matches_independent_audit_path_enumeration(probability, publish, delays):
    implementation, disclosure = delays
    actual = financing_signal_factors(
        np.array([.08]), decision_day=4, horizon_days=16, repricing_interval=3,
        period_days=4, implementation_delay=implementation, disclosure_delay=disclosure,
        audit_probability=probability, transparency=.2, publish_audit_results=publish,
    )
    expected = _enumerated_signal_factors(probability=probability, publish=publish,
                                          implementation_delay=implementation,
                                          disclosure_delay=disclosure)
    np.testing.assert_allclose(np.array(actual[:3])[:, 0], expected, atol=1e-14)
    first_audit = next(day for day in range(8, 100, 4) if day >= 4 + max(1, disclosure))
    fine = sum(probability * (1 - probability)**index *
               np.exp(-.08 * (first_audit - 4 + 4 * index) / 252) for index in range(20000))
    assert actual[3][0] == pytest.approx(fine, abs=1e-12)


def test_known_snapshot_uses_its_observation_date_and_fine_survives_short_horizon():
    actual = financing_signal_factors(
        np.array([.08]), decision_day=4, horizon_days=16, repricing_interval=3,
        period_days=4, implementation_delay=1, disclosure_delay=6, audit_probability=.35,
        transparency=.2, publish_audit_results=True, published_now=np.array([True]),
    )
    expected = _enumerated_signal_factors(probability=.35, publish=True,
                                          implementation_delay=1, disclosure_delay=6, known=True)
    np.testing.assert_allclose([actual[0][0], actual[2][0]], expected[[0, 2]], atol=1e-14)
    short = financing_signal_factors(
        np.array([.08]), decision_day=4, horizon_days=1, repricing_interval=3,
        period_days=4, implementation_delay=1, disclosure_delay=6, audit_probability=.35,
        transparency=.2, publish_audit_results=True, published_now=np.array([True]),
    )
    np.testing.assert_array_equal(np.array(short[:3]), 0)
    assert short[3][0] > 0


@pytest.mark.parametrize("publish", [False, True])
def test_real_action_displacing_old_inflation_uses_the_same_future_audit_prediction(publish):
    domain = replace(DOMAIN, implementation_delay_days=1, disclosure_delay_days=0,
                     max_change_per_period=.25)
    regime = PolicyRegime(.35, 0.0, .2, 0.0, publish_audit_results=publish)
    expected = _enumerated_signal_factors(probability=.35, publish=publish,
                                          implementation_delay=1, disclosure_delay=0)
    choices = npv_choices(
        benefit=np.array([.04]), cost_of_capital=np.array([.08]), marginal_cost=np.array([.005]),
        regime=regime, domain=domain, period_days=4, improve_capacity=np.array([.25]),
        inflate_capacity=np.array([0.0]), decision_day=4, horizon_days=16, repricing_interval=3,
    )
    grid = np.linspace(0.0, .25, 100001)
    values = .04 * expected[1] * grid - .005 * grid**2
    assert expected[1] > .2 * expected[0]
    assert choices.actions[0] == IMPROVE
    assert choices.amounts[0] == pytest.approx(grid[np.argmax(values)], abs=2.5e-6)
    assert choices.npv[0] == pytest.approx(values.max(), abs=1e-12)


@pytest.mark.parametrize("publish", [False, True])
def test_future_audit_exposes_real_gain_even_when_transparency_and_report_capacity_are_zero(publish):
    domain = replace(DOMAIN, implementation_delay_days=1, disclosure_delay_days=0)
    regime = PolicyRegime(.35, 0.0, 0.0, 0.0, publish_audit_results=publish)
    expected = _enumerated_signal_factors(probability=.35, publish=publish,
                                          implementation_delay=1, disclosure_delay=0,
                                          transparency=0.0)
    choices = npv_choices(
        benefit=np.array([.04]), cost_of_capital=np.array([.08]), marginal_cost=np.array([.005]),
        regime=regime, domain=domain, period_days=4, improve_capacity=np.array([.25]),
        inflate_capacity=np.array([0.0]), decision_day=4, horizon_days=16, repricing_interval=3,
    )
    assert expected[1] > 0
    assert choices.actions[0] == IMPROVE
    amount = min(.25, .04 * expected[1] / .01)
    assert choices.amounts[0] == pytest.approx(amount)
    assert choices.npv[0] == pytest.approx(.04 * expected[1] * amount - .005 * amount**2)


@pytest.fixture(scope="module")
def paired_information_runs():
    domain = replace(DOMAIN, natural_decay=0.0, implementation_delay_days=100,
                     disclosure_delay_days=4)
    baseline = PolicySchedule(PolicyRegime(.5, 0.0, .1, 0.0, disclosure_noise_sd=.4))
    changes = {"noise": {"disclosure_noise_sd": 0.0},
               "delay": {"disclosure_delay_days": 0},
               "publication": {"publish_audit_results": True},
               "frequency": {"reporting_interval_days": 7}}
    runs = {"baseline": DisclosureMarket(CONFIG, domain, baseline).run()}
    for name, change in changes.items():
        policy = baseline.with_information_intervention(31, **change)
        runs[name] = DisclosureMarket(CONFIG, domain, policy).run()
    return runs


@pytest.mark.parametrize("name", ["noise", "delay", "publication", "frequency"])
def test_information_changes_have_real_market_effects_and_paired_prepolicy_history(name, paired_information_runs):
    baseline, changed = paired_information_runs["baseline"], paired_information_runs[name]
    for item in fields(baseline.market):
        before, after = getattr(baseline.market, item.name), getattr(changed.market, item.name)
        if isinstance(before, np.ndarray) and before.shape[0] == CONFIG.trading_days + 1:
            np.testing.assert_array_equal(before[:31], after[:31])
    for key in ("true_goodness", "inflation", "public_signal", "planning_signal", "disclosure_error"):
        np.testing.assert_array_equal(getattr(baseline, key)[:31], getattr(changed, key)[:31])
    for key in ("actions", "amounts", "cost_fraction", "penalty_fraction", "subsidy_fraction"):
        np.testing.assert_array_equal(getattr(baseline, key)[:6], getattr(changed, key)[:6])
    np.testing.assert_array_equal(baseline.audit_selected, changed.audit_selected)
    assert not np.array_equal(baseline.market.prices[31:], changed.market.prices[31:])
    assert not np.array_equal(baseline.public_signal[31:], changed.public_signal[31:])
    assert not np.array_equal(baseline.amounts[6:], changed.amounts[6:])
    if name == "delay":
        active = changed.actions[6] == INFLATE
        assert active.any()
        np.testing.assert_array_equal(changed.action_due_day[6, active], 37)
        np.testing.assert_array_equal(baseline.action_due_day[6, active], 40)
    if name == "publication":
        np.testing.assert_array_equal(changed.public_signal[31:37], baseline.public_signal[31:37])
        assert changed.audit_publications[6].any()
    if name == "frequency":
        np.testing.assert_array_equal(baseline.disclosure_error, changed.disclosure_error)


@pytest.mark.parametrize("changes", [{"financing_exposure_fraction": 0.0}, {"financing_spread": 0.0},
                                     {"taste_median": 0.0}])
def test_information_instruments_do_not_create_a_residual_quote_reward(changes):
    config = replace(CONFIG, **changes)
    policy = PolicySchedule(PolicyRegime(.5, 0.0, .1, 0.0, disclosure_noise_sd=.4,
                                         disclosure_delay_days=0, publish_audit_results=True))
    market = DisclosureMarket(config, DOMAIN, policy)
    market._audit_and_decide(6, 1)
    np.testing.assert_array_equal(market.action_history[1], MAINTAIN)
    np.testing.assert_array_equal(market.cost_history[1], 0)


def test_new_information_history_roundtrip_and_missing_legacy_history(tmp_path, paired_information_runs):
    result = paired_information_runs["publication"]
    save_result(tmp_path / "result.npz", result)
    restored = load_result(tmp_path / "result.npz")
    assert restored.fingerprint() == result.fingerprint()
    for name in INFORMATION_FIELDS:
        np.testing.assert_array_equal(getattr(restored, name), getattr(result, name))
    legacy = replace(result, **dict.fromkeys(INFORMATION_FIELDS))
    save_result(tmp_path / "legacy.npz", legacy)
    restored = load_result(tmp_path / "legacy.npz")
    assert restored.fingerprint() == legacy.fingerprint()
    assert all(getattr(restored, name) is None for name in INFORMATION_FIELDS)
