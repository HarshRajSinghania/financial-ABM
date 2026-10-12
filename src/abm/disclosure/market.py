"""Per-asset price formation with depth that thins as volatility rises.

This is the vector form of the Stage 1 quasi order book: each asset's depth
is a fraction of its market capitalisation, and that fraction falls when the
asset's realised volatility rises above its slow-moving reference. Market makers
pass public news about intrinsic value into quotes. A fraction of the flow
impact (net order value over reference depth) is permanent; the rest follows
the surprise in order flow, is scaled up when depth thins, and decays, as in
the Stage 1 book.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .config import MarketConfig

FloatArray = NDArray[np.float64]


@dataclass(slots=True)
class CrossSectionBook:
    config: MarketConfig
    variance: FloatArray
    reference_variance: FloatArray
    depth_fraction: FloatArray
    transient_impact: FloatArray
    expected_flow_impact: FloatArray

    @classmethod
    def initialize(cls, config: MarketConfig, daily_variance: float) -> "CrossSectionBook":
        size = config.n_firms
        return cls(
            config=config,
            variance=np.full(size, daily_variance),
            reference_variance=np.full(size, daily_variance),
            depth_fraction=np.ones(size),
            transient_impact=np.zeros(size),
            expected_flow_impact=np.zeros(size),
        )

    def price_moves(
        self,
        net_flow_value: FloatArray,
        market_cap: FloatArray,
        news: FloatArray,
        inventory_gap: FloatArray,
    ) -> tuple[FloatArray, FloatArray]:
        """Log price changes for one day; returns (moves, capped).

        ``inventory_gap`` is the market maker's target minus actual inventory;
        a short market maker (positive gap) raises quotes to win shares back.
        """
        cfg = self.config
        stress = np.clip(
            np.sqrt(self.variance / self.reference_variance) - cfg.liquidity_stress_threshold,
            0.0,
            1.0,
        )
        target = np.maximum(
            cfg.minimum_liquidity_fraction,
            np.exp(-cfg.liquidity_volatility_sensitivity * stress),
        )
        self.depth_fraction += cfg.depth_resilience * (target - self.depth_fraction)
        np.maximum(self.depth_fraction, cfg.minimum_liquidity_fraction, out=self.depth_fraction)
        # Permanent impact uses the reference depth; only the transient part
        # sees the volatility-dependent depth (the Stage 1 v15 structure).
        # Letting depth scale the permanent part as well makes the liquidity
        # spiral unstable: depth then falls to its floor after any shock and
        # stays there until the slow reference variance catches up.
        reference_depth = cfg.liquidity_fraction * market_cap
        flow_impact = cfg.price_impact * net_flow_value / reference_depth
        surprise = flow_impact / self.depth_fraction - self.expected_flow_impact
        self.expected_flow_impact = (
            cfg.order_flow_memory * self.expected_flow_impact
            + (1 - cfg.order_flow_memory) * flow_impact / self.depth_fraction
        )
        transient_before = self.transient_impact
        self.transient_impact = (
            cfg.transient_impact_decay * transient_before + (1 - cfg.permanent_impact_fraction) * surprise
        )
        raw = (
            cfg.news_pass_through * news
            + cfg.permanent_impact_fraction * flow_impact
            + self.transient_impact
            - transient_before
            + cfg.market_maker_inventory_skew * inventory_gap
        )
        moves = np.clip(raw, -cfg.max_log_return, cfg.max_log_return)
        return moves, moves != raw

    def record_returns(self, log_returns: FloatArray) -> None:
        cfg = self.config
        squared = log_returns**2
        self.variance = cfg.variance_ewma_decay * self.variance + (1 - cfg.variance_ewma_decay) * squared
        self.reference_variance = (
            cfg.reference_variance_decay * self.reference_variance
            + (1 - cfg.reference_variance_decay) * squared
        )
