from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure import MarketConfig, run_market
from abm.disclosure.config import TRADING_DAYS_PER_YEAR
from abm.disclosure.firms import LARGE, MID, SMALL, FirmUniverse
from abm.disclosure.harness import CrossSectionMarket, MarketDivergedError, _cap_buys_to_cash

SMALL_MARKET = MarketConfig(n_investors=120, n_firms=20, trading_days=300, burn_in_days=50)


def test_config_rejects_invalid_values_and_unknown_keys():
    with pytest.raises(ValueError):
        MarketConfig(size_class_shares=(0.5, 0.5, 0.5))
    with pytest.raises(ValueError):
        MarketConfig(burn_in_days=2500, trading_days=2500)
    with pytest.raises(ValueError):
        MarketConfig(investor_float_share=0.99, noise_float_share=0.05)
    with pytest.raises(ValueError):
        MarketConfig.from_dict({"not_a_field": 1})
    round_trip = MarketConfig.from_dict(SMALL_MARKET.to_dict())
    assert round_trip == SMALL_MARKET


def test_size_classes_follow_configured_shares_by_value_rank():
    firms = FirmUniverse.initialize(MarketConfig(), np.random.default_rng(1))
    counts = np.bincount(firms.size_class, minlength=3)
    assert tuple(counts) == (20, 60, 120)
    assert firms.intrinsic_value[firms.size_class == LARGE].min() >= firms.intrinsic_value[firms.size_class == MID].max()
    assert firms.intrinsic_value[firms.size_class == MID].min() >= firms.intrinsic_value[firms.size_class == SMALL].max()


def test_runs_are_reproducible_and_seed_sensitive():
    first = run_market(SMALL_MARKET)
    assert first.fingerprint() == run_market(SMALL_MARKET).fingerprint()
    assert first.fingerprint() != run_market(replace(SMALL_MARKET, seed=SMALL_MARKET.seed + 1)).fingerprint()


def test_shares_and_cash_are_conserved_with_dividends():
    market = CrossSectionMarket(SMALL_MARKET)
    initial_shares = market.investors.holdings.sum(axis=0) + market.noise_holdings + market.market_maker_inventory
    initial_share_error = float(np.max(np.abs(initial_shares - 1.0)))
    assert market.maximum_share_error[0] == initial_share_error
    result = market.run()
    assert result.maximum_share_error[0] == initial_share_error
    assert result.maximum_share_error.max() < 1e-10
    expected = market.initial_total_cash + market.dividends_paid
    assert result.total_cash[-1] == pytest.approx(expected, rel=1e-10)
    assert market.dividends_paid > 0
    assert np.all(market.investors.cash >= -1e-10)
    assert np.all(market.investors.holdings >= -1e-12)


def test_dividends_pay_holders_pro_rata():
    market = CrossSectionMarket(SMALL_MARKET)
    cash_before = market.investors.cash.copy()
    market._pay_dividends()
    per_share = SMALL_MARKET.cash_flow_yield * market.firms.intrinsic_value / TRADING_DAYS_PER_YEAR
    np.testing.assert_allclose(market.investors.cash - cash_before, market.investors.holdings @ per_share)


def test_purchases_are_capped_at_available_cash():
    prices = np.array([2.0, 4.0])
    orders = np.array([[3.0, -1.0], [1.0, 1.0], [0.0, -2.0]])
    cash = np.array([1.0, 100.0, -1e-15])
    capped = _cap_buys_to_cash(orders, cash, prices, cost=0.0)
    np.testing.assert_allclose(capped[0], [2.5, -1.0])
    np.testing.assert_allclose(capped[1], orders[1])
    np.testing.assert_allclose(capped[2], orders[2])
    assert np.all(np.isfinite(capped))


def test_equal_utilities_hold_the_market_portfolio():
    market = CrossSectionMarket(replace(SMALL_MARKET, rebalance_speed=1.0))
    investors, prices = market.investors, market.prices
    who = np.arange(investors.size)
    wealth = investors.wealth(prices)
    equity_share = 0.7
    investors.holdings[:] = np.outer(equity_share * wealth / prices.sum(), np.ones(prices.size))
    investors.cash[:] = wealth * (1 - equity_share)
    market_return = SMALL_MARKET.risk_free_rate + equity_share * investors.risk_aversion * 0.04
    orders = np.vstack([
        investors.desired_orders(
            who[i:i + 1],
            prices=prices,
            expected_returns=np.full(prices.size, 0.08),
            annual_market_covariance=np.full(prices.size, 0.04),
            market_expected_return=float(market_return[i]),
            market_annual_variance=0.04,
            attribute=np.zeros(prices.size),
            config=market.config,
        )
        for i in range(investors.size)
    ])
    np.testing.assert_allclose(orders, 0.0, atol=1e-12)


def test_unstable_feedback_is_reported_not_silently_returned():
    unstable = replace(SMALL_MARKET, price_impact=6.0, noise_flow_scale=0.03, choice_intensity_median=40.0)
    with pytest.raises(MarketDivergedError):
        run_market(unstable)


def test_noise_account_can_be_switched_off():
    market = CrossSectionMarket(replace(SMALL_MARKET, noise_flow_scale=0.0))
    holdings = market.noise_holdings.copy()
    market.run()
    np.testing.assert_array_equal(market.noise_holdings, holdings)


def test_noise_flow_scales_with_relative_volatility():
    orders = {}
    for exponent in (0.0, 1.0):
        market = CrossSectionMarket(replace(SMALL_MARKET, noise_volatility_exponent=exponent))
        market.book.variance = 4.0 * market.book.reference_variance
        orders[exponent] = market._noise_orders()
    np.testing.assert_allclose(orders[1.0], 2.0 * orders[0.0])
