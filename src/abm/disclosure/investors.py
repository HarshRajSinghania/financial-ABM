"""Heterogeneous investors with a two-level allocation rule.

1. Equity versus cash: the Merton share (E[R_m] - r_f) / (gamma * var_m),
   clipped to [0, max_equity_share]. When market volatility rises every
   investor wants less equity, which is a source of correlated selling.
2. Across assets: a softmax tilt away from market-cap weights,
   w_i proportional to cap_i * exp(intensity * U_i), with
   U_i = E[R_i] - gamma * cov(r_i, r_m) + taste * attribute_i.
   The risk term is the marginal mean-variance cost of an asset inside a
   diversified portfolio. Using the asset's own variance instead (the
   per-asset reading of E[R] - gamma/2 Var) lets one volatile asset drive
   its own weight to zero and its price into a self-reinforcing collapse.
   With equal utilities everyone holds the market portfolio, which keeps the
   rule consistent with a fixed supply of shares.

Only investors whose decision day it is trade; they move a fraction
``rebalance_speed`` of the way from current to target holdings.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .config import MarketConfig

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

PROFIT_MAXIMIZER, IMPACT_INVESTOR = 0, 1


@dataclass(slots=True)
class InvestorPopulation:
    cash: FloatArray
    holdings: FloatArray
    investor_type: IntArray
    taste: FloatArray
    risk_aversion: FloatArray
    decision_interval: IntArray
    decision_offset: IntArray
    choice_intensity: FloatArray

    @classmethod
    def initialize(
        cls,
        config: MarketConfig,
        rng: np.random.Generator,
        market_cap: FloatArray,
    ) -> "InvestorPopulation":
        n = config.n_investors
        sigma = config.investor_wealth_log_sd
        wealth_share = rng.lognormal(-0.5 * sigma**2, sigma, n)
        wealth_share /= wealth_share.sum()
        # Investors jointly own investor_float_share of every firm, split by
        # wealth, and hold enough cash to start at initial_equity_share.
        holdings = np.outer(wealth_share, np.full(market_cap.size, config.investor_float_share))
        equity_value = holdings @ market_cap
        cash = equity_value * (1 - config.initial_equity_share) / config.initial_equity_share
        risk_aversion = np.maximum(
            rng.normal(config.risk_aversion_mean, config.risk_aversion_sd, n),
            config.risk_aversion_min,
        )
        interval = np.clip(
            np.rint(rng.lognormal(np.log(config.decision_interval_median), config.decision_interval_log_sd, n)),
            1,
            config.decision_interval_max,
        ).astype(np.int64)
        offset = (rng.random(n) * interval).astype(np.int64)
        intensity = rng.lognormal(np.log(config.choice_intensity_median), config.choice_intensity_log_sd, n)
        return cls(
            cash=cash,
            holdings=holdings,
            investor_type=np.zeros(n, dtype=np.int64),
            taste=np.zeros(n),
            risk_aversion=risk_aversion,
            decision_interval=interval,
            decision_offset=offset,
            choice_intensity=intensity,
        )

    @property
    def size(self) -> int:
        return int(self.cash.size)

    def deciding(self, day: int) -> IntArray:
        return np.flatnonzero((day - self.decision_offset) % self.decision_interval == 0)

    def wealth(self, prices: FloatArray) -> FloatArray:
        return self.cash + self.holdings @ prices

    def desired_orders(
        self,
        who: IntArray,
        *,
        prices: FloatArray,
        expected_returns: FloatArray,
        annual_market_covariance: FloatArray,
        market_expected_return: float,
        market_annual_variance: float,
        attribute: FloatArray,
        config: MarketConfig,
    ) -> FloatArray:
        """Share orders, shape (len(who), n_firms), before any constraint."""
        gamma = self.risk_aversion[who]
        equity_share = np.clip(
            (market_expected_return - config.risk_free_rate) / (gamma * market_annual_variance),
            0.0,
            config.max_equity_share,
        )
        utility = (
            expected_returns[None, :]
            - gamma[:, None] * annual_market_covariance[None, :]
            + self.taste[who, None] * attribute[None, :]
        )
        scaled = self.choice_intensity[who, None] * utility
        scaled -= scaled.max(axis=1, keepdims=True)
        tilt = prices[None, :] * np.exp(scaled)
        weights = tilt / tilt.sum(axis=1, keepdims=True)
        wealth = self.cash[who] + self.holdings[who] @ prices
        target_value = (wealth * equity_share)[:, None] * weights
        current_value = self.holdings[who] * prices[None, :]
        return config.rebalance_speed * (target_value - current_value) / prices[None, :]
