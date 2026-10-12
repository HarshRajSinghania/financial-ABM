import json
from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure.config import TRADING_DAYS_PER_YEAR, MarketConfig
from abm.disclosure.harness import CrossSectionResult
from abm.disclosure.validate import validate_market


@pytest.fixture
def clustered_market():
    config = MarketConfig(n_investors=10, n_firms=3, trading_days=600, burn_in_days=0)
    rng = np.random.default_rng(2)
    volatility = np.repeat([0.005, 0.025] * 3, 100)
    returns = volatility[:, None] * (0.5 * rng.standard_normal((600, 1)) + np.sqrt(0.75) * rng.standard_normal((600, 3)))
    prices = np.vstack([np.ones(3), np.exp(np.cumsum(returns, axis=0))])
    values = prices.copy()
    cash = 10.0 + np.r_[0.0, np.cumsum(config.cash_flow_yield * values[1:].sum(axis=1) / TRADING_DAYS_PER_YEAR)]
    result = CrossSectionResult(
        burn_in_days=0, prices=prices, intrinsic_values=values, size_class=np.arange(3),
        equity_share=np.full(601, 0.7), mean_depth_fraction=np.ones(601), gross_volume=np.zeros(601),
        price_cap_hits=np.zeros(601, dtype=np.int64), total_cash=cash, maximum_share_error=np.zeros(601),
    )
    return config, result


def test_market_validation_separates_core_gates_from_empirical_acceptance(clustered_market):
    config, result = clustered_market
    report = validate_market(result, config)
    assert report["mechanical"]["status"] == "PASS"
    assert report["stylized"]["status"] == "PASS"
    assert report["return_acf"]["status"] == "pending"
    assert report["cross_asset_correlation"]["status"] == "pending"
    assert report["cross_asset_correlation"]["pair_count"] == 3
    assert report["cross_asset_correlation"]["statistics"]["finite_count"] == 3
    assert report["empirical_calibration"]["status"] == "pending"
    assert len(report["moments_per_asset"]) == config.n_firms
    json.dumps(report, allow_nan=False)


def test_one_failed_asset_cannot_hide_behind_positive_average_moments(clustered_market):
    config, result = clustered_market
    prices = result.prices.copy()
    prices[1:, 2] = np.exp(np.cumsum(np.tile([0.01, -0.01], 300)))
    report = validate_market(replace(result, prices=prices), config)
    assert np.mean([asset["moments"]["excess_kurtosis"] for asset in report["moments_per_asset"]]) > 0
    assert report["mechanical"]["status"] == "PASS"
    assert report["stylized"]["status"] == "FAIL"
    assert report["stylized"]["failed_assets"]["nonpositive_excess_kurtosis"] == [2]
    assert report["stylized"]["failed_assets"]["nonpositive_abs_return_acf_1"] == [2]


@pytest.mark.parametrize("field,check", [
    ("total_cash", "cash_conservation"),
    ("maximum_share_error", "share_conservation"),
    ("price_cap_hits", "no_price_caps"),
])
def test_mechanical_checks_cover_intermediate_days(clustered_market, field, check):
    config, result = clustered_market
    path = getattr(result, field).copy()
    path[100] += 1
    report = validate_market(replace(result, **{field: path}), config)
    assert report["mechanical"]["status"] == "FAIL"
    assert report["mechanical"]["checks"][check] is False


@pytest.mark.parametrize("thresholds,diagnostic", [
    ({"return_acf_target": 0.0, "return_acf_tolerance": 0.0}, "return_acf"),
    ({"correlation_bounds": (0.9999, 1.0)}, "cross_asset_correlation"),
])
def test_only_explicit_diagnostic_thresholds_add_gates(clustered_market, thresholds, diagnostic):
    config, result = clustered_market
    report = validate_market(result, config, **thresholds)
    assert report[diagnostic]["status"] == "FAIL"
    assert report[diagnostic]["threshold_source"] == "caller_supplied"
    assert report["stylized"]["status"] == "FAIL"
    assert report["empirical_calibration"]["status"] == "pending"


def test_nonfinite_asset_fails_and_remains_strict_json(clustered_market):
    config, result = clustered_market
    prices = result.prices.copy()
    prices[100, 2] = np.nan
    report = validate_market(replace(result, prices=prices), config)
    assert report["mechanical"]["status"] == "FAIL"
    assert report["stylized"]["failed_assets"]["nonfinite_moments"] == [2]
    assert all(value is None for value in report["moments_per_asset"][2]["moments"].values())
    json.dumps(report, allow_nan=False)
