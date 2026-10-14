"""Imitation rules: the type-mean comparison drifts towards one half under noise; pairwise sampling does not."""

from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.game import DisclosureMarket, run_disclosure
from abm.disclosure.investors import IMPACT_INVESTOR

ESG = load_domain("configs/domains/esg.json")
LARGE = MarketConfig(seed=29999, n_investors=1000, n_firms=10, trading_days=10, burn_in_days=1, initial_impact_share=.2)


def test_rule_is_validated_and_serialized_only_when_not_default():
    with pytest.raises(ValueError, match="imitation_rule"):
        MarketConfig(imitation_rule="logit")
    assert "imitation_rule" not in MarketConfig().to_dict()
    pairwise = MarketConfig(imitation_rule="pairwise")
    assert pairwise.to_dict()["imitation_rule"] == "pairwise"
    assert MarketConfig.from_dict(pairwise.to_dict()) == pairwise


def changes(rule: str, sign: int, repeats: int) -> tuple[np.ndarray, int]:
    """II count changes after one review in which one type grew by 0.5% and the other by 0."""
    market = DisclosureMarket(replace(LARGE, imitation_rule=rule), ESG)
    types, tastes = market.investors.investor_type.copy(), market.investors.taste.copy()
    impact = types == IMPACT_INVESTOR
    wealth = market.investors.wealth(market.prices)
    better = impact if sign > 0 else ~impact
    out = []
    for repeat in range(repeats):
        market.investors.investor_type[:], market.investors.taste[:] = types, tastes
        market.window_wealth = wealth / np.where(better, 1.005, 1.0)
        market.learning_rng = np.random.default_rng([repeat, sign + 2])
        market._imitate()
        out.append(int((market.investors.investor_type == IMPACT_INVESTOR).sum() - impact.sum()))
    return np.asarray(out), int(impact.sum())


def test_type_mean_rule_drifts_towards_one_half_when_noise_is_symmetric():
    up, impact = changes("type_mean", +1, 400)
    down, _ = changes("type_mean", -1, 400)
    n, reviewed, probability = LARGE.n_investors, 100, .5
    drift = up.mean() + down.mean()
    expected = reviewed * probability * (n - 2 * impact) / n
    assert drift == pytest.approx(expected, abs=4 * np.hypot(up.std(), down.std()) / np.sqrt(400))
    assert drift > 20


def test_pairwise_rule_is_the_replicator_flow_with_no_drift_under_symmetric_noise():
    up, impact = changes("pairwise", +1, 400)
    down, _ = changes("pairwise", -1, 400)
    n, reviewed, probability = LARGE.n_investors, 100, .5
    # A profit maximiser imitates only when its sampled partner is an impact investor.
    expected_up = reviewed * (n - impact) / n * impact / (n - 1) * probability
    standard_error = np.hypot(up.std(), down.std()) / np.sqrt(400)
    assert up.mean() == pytest.approx(expected_up, abs=4 * up.std() / np.sqrt(400))
    assert up.mean() + down.mean() == pytest.approx(0.0, abs=4 * standard_error)


def test_pairwise_rule_keeps_types_when_performance_is_equal():
    market = DisclosureMarket(replace(LARGE, imitation_rule="pairwise"), ESG)
    types = market.investors.investor_type.copy()
    market.window_wealth = market.investors.wealth(market.prices)
    market._imitate()
    np.testing.assert_array_equal(market.investors.investor_type, types)


def test_pairwise_runs_are_reproducible_and_differ_from_the_default():
    config = MarketConfig(n_investors=150, n_firms=30, trading_days=400, burn_in_days=100, initial_impact_share=.2)
    pairwise = replace(config, imitation_rule="pairwise")
    first = run_disclosure(pairwise, ESG)
    assert first.fingerprint() == run_disclosure(pairwise, ESG).fingerprint()
    assert not np.array_equal(first.impact_share, run_disclosure(config, ESG).impact_share)
