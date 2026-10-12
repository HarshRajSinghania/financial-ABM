"""Firms as tradeable assets: intrinsic value, size class and cash-flow yield."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .config import TRADING_DAYS_PER_YEAR, MarketConfig

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

LARGE, MID, SMALL = 0, 1, 2
SIZE_CLASS_NAMES = ("large", "mid", "small")


@dataclass(slots=True)
class FirmUniverse:
    """Each firm has one share outstanding, so its price is its market cap."""

    intrinsic_value: FloatArray
    size_class: IntArray

    @classmethod
    def initialize(cls, config: MarketConfig, rng: np.random.Generator) -> "FirmUniverse":
        sigma = config.intrinsic_value_log_sd
        values = rng.lognormal(mean=-0.5 * sigma**2, sigma=sigma, size=config.n_firms)
        values *= config.n_firms / values.sum()
        rank = np.empty(config.n_firms, dtype=np.int64)
        rank[np.argsort(-values, kind="stable")] = np.arange(config.n_firms)
        cut_large, cut_mid = np.cumsum(config.size_class_shares[:2]) * config.n_firms
        size_class = np.where(rank < cut_large, LARGE, np.where(rank < cut_mid, MID, SMALL))
        return cls(intrinsic_value=values, size_class=size_class.astype(np.int64))

    @property
    def size(self) -> int:
        return int(self.intrinsic_value.size)

    def evolve(self, config: MarketConfig, rng: np.random.Generator) -> FloatArray:
        """Advance intrinsic values one day; returns the log changes."""
        daily_sigma = config.fundamental_volatility / np.sqrt(TRADING_DAYS_PER_YEAR)
        drift = (config.fundamental_drift - 0.5 * config.fundamental_volatility**2) / TRADING_DAYS_PER_YEAR
        rho = config.fundamental_common_correlation
        shocks = np.sqrt(rho) * rng.standard_normal() + np.sqrt(1 - rho) * rng.standard_normal(self.size)
        changes = drift + daily_sigma * shocks
        self.intrinsic_value *= np.exp(changes)
        return changes
