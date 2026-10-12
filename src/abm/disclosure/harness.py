"""Daily clock of the multi-asset market; the only place state changes.

Order of a trading day:
1. intrinsic values move; market makers pass the news into quotes;
2. investors whose decision day it is submit orders, the noise account
   submits its demand;
3. sales are capped at holdings and purchases at available cash, at the
   previous price;
4. each asset's price moves with its net order value over its depth;
5. trades execute at the new price; a buyer whose cash no longer covers the
   order is scaled down, and the market maker absorbs the executed net flow;
6. firms pay dividends to holders (the only external cash inflow);
7. shares and cash (initial plus cumulative dividends) are checked.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from ..manifest import canonical_json_bytes
from .config import TRADING_DAYS_PER_YEAR, MarketConfig
from .firms import FirmUniverse
from .investors import InvestorPopulation
from .market import CrossSectionBook

FloatArray = NDArray[np.float64]
CONSERVATION_TOLERANCE = 1e-8
# A price more than e^5 away from intrinsic value means the feedback loop
# has diverged; the run stops instead of producing meaningless paths.
MAXIMUM_LOG_MISPRICING = 5.0


class MarketDivergedError(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class CrossSectionResult:
    burn_in_days: int
    prices: FloatArray
    intrinsic_values: FloatArray
    size_class: NDArray[np.int64]
    equity_share: FloatArray
    mean_depth_fraction: FloatArray
    gross_volume: FloatArray
    price_cap_hits: NDArray[np.int64]
    total_cash: FloatArray
    maximum_share_error: FloatArray

    def log_returns(self, *, include_burn_in: bool = False) -> FloatArray:
        returns = np.diff(np.log(self.prices), axis=0)
        return returns if include_burn_in else returns[self.burn_in_days :]

    def fingerprint(self) -> str:
        digest = hashlib.sha256(str(self.burn_in_days).encode("ascii"))
        for array in (
            self.prices, self.intrinsic_values, self.size_class, self.equity_share,
            self.mean_depth_fraction, self.gross_volume, self.price_cap_hits, self.total_cash,
        ):
            contiguous = np.ascontiguousarray(array)
            digest.update(str(contiguous.dtype).encode("ascii"))
            digest.update(str(contiguous.shape).encode("ascii"))
            digest.update(contiguous.tobytes())
        return digest.hexdigest()


def _cap_buys_to_cash(orders: FloatArray, cash: FloatArray, prices: FloatArray, cost: float) -> FloatArray:
    """Scale each row's purchases so that cash after the trade is nonnegative."""
    buys = np.maximum(orders, 0.0)
    sells = np.minimum(orders, 0.0)
    buy_cost = (buys @ prices) * (1 + cost)
    available = cash - (sells @ prices) * (1 - cost)
    scale = np.ones_like(cash)
    short = (buy_cost > available) & (buy_cost > 0)
    scale[short] = np.maximum(available[short], 0.0) / buy_cost[short]
    return sells + buys * scale[:, None]


class CrossSectionMarket:
    def __init__(self, config: MarketConfig):
        self.config = config
        self.run_id = hashlib.sha256(canonical_json_bytes(config.to_dict())).hexdigest()
        firm_seed, investor_seed, fundamental_seed, noise_seed = np.random.SeedSequence(config.seed).spawn(4)
        self.fundamental_rng = np.random.default_rng(fundamental_seed)
        self.noise_rng = np.random.default_rng(noise_seed)
        self.firms = FirmUniverse.initialize(config, np.random.default_rng(firm_seed))
        self.prices = self.firms.intrinsic_value.copy()
        self.investors = InvestorPopulation.initialize(
            config, np.random.default_rng(investor_seed), self.prices
        )
        total_cap = float(self.prices.sum())
        self.noise_target = np.full(config.n_firms, config.noise_float_share)
        self.noise_holdings = self.noise_target.copy()
        self.noise_cash = config.noise_float_share * total_cap
        self.noise_common = 0.0
        self.noise_idiosyncratic = np.zeros(config.n_firms)
        self.market_maker_inventory = 1.0 - config.investor_float_share - self.noise_target
        self.market_maker_target = self.market_maker_inventory.copy()
        self.market_maker_cash = config.market_maker_cash_multiple * total_cap
        self.fees = 0.0
        self.dividends_paid = 0.0
        asset_variance = config.initial_asset_volatility**2 / TRADING_DAYS_PER_YEAR
        self.book = CrossSectionBook.initialize(config, asset_variance)
        self.market_variance = config.initial_market_volatility**2 / TRADING_DAYS_PER_YEAR
        self.allocation_market_variance = self.market_variance
        self.market_covariance = np.full(config.n_firms, self.market_variance)
        self.initial_total_cash = self._total_cash()

        days = config.trading_days
        self.price_path = np.empty((days + 1, config.n_firms))
        self.value_path = np.empty((days + 1, config.n_firms))
        self.equity_share = np.empty(days + 1)
        self.mean_depth_fraction = np.empty(days + 1)
        self.gross_volume = np.zeros(days + 1)
        self.price_cap_hits = np.zeros(days + 1, dtype=np.int64)
        self.total_cash = np.empty(days + 1)
        self.maximum_share_error = np.zeros(days + 1)
        self._record(0)
        self._check_conservation(0)
        self.next_day_index = 0

    def _total_cash(self) -> float:
        return float(self.investors.cash.sum() + self.noise_cash + self.market_maker_cash + self.fees)

    def _record(self, day: int) -> None:
        holdings_value = self.investors.holdings @ self.prices
        wealth = self.investors.cash + holdings_value
        self.price_path[day] = self.prices
        self.value_path[day] = self.firms.intrinsic_value
        self.equity_share[day] = float(holdings_value.sum() / wealth.sum())
        self.mean_depth_fraction[day] = float(self.book.depth_fraction.mean())
        self.total_cash[day] = self._total_cash()

    def expected_returns(self) -> FloatArray:
        cfg = self.config
        value_to_price = self.firms.intrinsic_value / self.prices
        return (
            cfg.cash_flow_yield * value_to_price
            + cfg.fundamental_drift
            + cfg.mispricing_reversion * np.log(value_to_price)
        )

    def _pre_trade(self, day: int) -> FloatArray:
        """Extra log changes of intrinsic value before trading (none here)."""
        return np.zeros(self.config.n_firms)

    def _post_trade(self, day: int) -> None:
        """End-of-day hook for subclasses (decisions, audits, learning)."""

    def attribute_signal(self) -> FloatArray:
        """Attribute values investors can see; none in the bare market."""
        return np.zeros(self.config.n_firms)

    def _pay_dividends(self) -> None:
        """Firms pay out cash_flow_yield of intrinsic value per year to holders.

        This is the only cash entering the market; without it, investors who
        sold to the market maker in a downturn could never buy back and prices
        would stay depressed.
        """
        per_share = self.config.cash_flow_yield * self.firms.intrinsic_value / TRADING_DAYS_PER_YEAR
        self.investors.cash += self.investors.holdings @ per_share
        self.noise_cash += float(self.noise_holdings @ per_share)
        self.market_maker_cash += float(self.market_maker_inventory @ per_share)
        self.dividends_paid += float(per_share.sum())

    def _noise_orders(self) -> FloatArray:
        cfg = self.config
        if cfg.noise_flow_scale == 0:
            return np.zeros(cfg.n_firms)
        phi, rho = cfg.noise_persistence, cfg.noise_common_correlation
        innovation = np.sqrt(1 - phi**2)
        self.noise_common = phi * self.noise_common + innovation * self.noise_rng.standard_normal()
        self.noise_idiosyncratic = (
            phi * self.noise_idiosyncratic + innovation * self.noise_rng.standard_normal(cfg.n_firms)
        )
        demand = np.sqrt(rho) * self.noise_common + np.sqrt(1 - rho) * self.noise_idiosyncratic
        if cfg.noise_volatility_exponent:
            ratio = np.minimum(np.sqrt(self.book.variance / self.book.reference_variance), 4.0)
            demand = demand * ratio**cfg.noise_volatility_exponent
        orders = cfg.noise_flow_scale * demand - cfg.noise_inventory_reversion * (
            self.noise_holdings - self.noise_target
        )
        orders = np.maximum(orders, -self.noise_holdings)
        return _cap_buys_to_cash(orders[None, :], np.array([self.noise_cash]), self.prices,
                                 cfg.transaction_cost_rate)[0]

    def step(self, day_index: int) -> None:
        cfg = self.config
        if day_index != self.next_day_index or day_index >= cfg.trading_days:
            raise RuntimeError("days must be stepped once each, in order")
        day = day_index + 1
        news = self.firms.evolve(cfg, self.fundamental_rng) + self._pre_trade(day)

        old_prices = self.prices.copy()
        expected = self.expected_returns()
        cap_weights = old_prices / old_prices.sum()
        who = self.investors.deciding(day)
        orders = self.investors.desired_orders(
            who,
            prices=old_prices,
            expected_returns=expected,
            annual_market_covariance=self.market_covariance * TRADING_DAYS_PER_YEAR,
            market_expected_return=float(cap_weights @ expected),
            market_annual_variance=self.allocation_market_variance * TRADING_DAYS_PER_YEAR,
            attribute=self.attribute_signal(),
            config=cfg,
        )
        orders = np.maximum(orders, -self.investors.holdings[who])
        orders = _cap_buys_to_cash(orders, self.investors.cash[who], old_prices, cfg.transaction_cost_rate)
        noise = self._noise_orders()

        net_shares = orders.sum(axis=0) + noise
        moves, capped = self.book.price_moves(
            net_shares * old_prices,
            old_prices,
            news,
            self.market_maker_target - self.market_maker_inventory,
        )
        self.prices = old_prices * np.exp(moves)

        orders = _cap_buys_to_cash(orders, self.investors.cash[who], self.prices, cfg.transaction_cost_rate)
        noise = _cap_buys_to_cash(noise[None, :], np.array([self.noise_cash]), self.prices,
                                  cfg.transaction_cost_rate)[0]
        cost = cfg.transaction_cost_rate
        investor_fees = (np.abs(orders) @ self.prices) * cost
        self.investors.cash[who] -= orders @ self.prices + investor_fees
        self.investors.holdings[who] += orders
        noise_fee = float(np.abs(noise) @ self.prices) * cost
        self.noise_cash -= float(noise @ self.prices) + noise_fee
        self.noise_holdings += noise
        executed = orders.sum(axis=0) + noise
        self.market_maker_inventory -= executed
        self.market_maker_cash += float(executed @ self.prices)
        self.fees += float(investor_fees.sum()) + noise_fee

        self._pay_dividends()
        self.book.record_returns(moves)
        market_return = float(cap_weights @ np.expm1(moves))
        market_log_return = np.log1p(market_return)
        squared_market_return = market_log_return**2
        self.market_covariance = (
            cfg.allocation_variance_decay * self.market_covariance
            + (1 - cfg.allocation_variance_decay) * moves * market_log_return
        )
        self.market_variance = (
            cfg.variance_ewma_decay * self.market_variance
            + (1 - cfg.variance_ewma_decay) * squared_market_return
        )
        self.allocation_market_variance = (
            cfg.allocation_variance_decay * self.allocation_market_variance
            + (1 - cfg.allocation_variance_decay) * squared_market_return
        )
        self.gross_volume[day] = float(np.abs(orders).sum(axis=0) @ self.prices + np.abs(noise) @ self.prices)
        self.price_cap_hits[day] = int(capped.sum())
        self._record(day)
        self._check_conservation(day)
        self._post_trade(day)
        self.next_day_index += 1

    def _check_conservation(self, day: int) -> None:
        mispricing = np.abs(np.log(self.prices / self.firms.intrinsic_value))
        if not np.all(np.isfinite(mispricing)) or mispricing.max() > MAXIMUM_LOG_MISPRICING:
            raise MarketDivergedError(f"prices diverged from intrinsic values on day {day}")
        expected_cash = self.initial_total_cash + self.dividends_paid
        cash_error = abs(self.total_cash[day] - expected_cash) / expected_cash
        shares = self.investors.holdings.sum(axis=0) + self.noise_holdings + self.market_maker_inventory
        share_error = float(np.max(np.abs(shares - 1.0)))
        self.maximum_share_error[day] = share_error
        if cash_error > CONSERVATION_TOLERANCE or share_error > CONSERVATION_TOLERANCE:
            raise RuntimeError(
                f"conservation violated on day {day}: cash {cash_error:.3g}, shares {share_error:.3g}"
            )
        if np.any(self.investors.cash < -CONSERVATION_TOLERANCE * self.initial_total_cash):
            raise RuntimeError(f"negative investor cash on day {day}")
        if np.any(self.investors.holdings < -CONSERVATION_TOLERANCE):
            raise RuntimeError(f"short investor position on day {day}")

    def run(self) -> CrossSectionResult:
        while self.next_day_index < self.config.trading_days:
            self.step(self.next_day_index)
        return CrossSectionResult(
            burn_in_days=self.config.burn_in_days,
            prices=self.price_path.copy(),
            intrinsic_values=self.value_path.copy(),
            size_class=self.firms.size_class.copy(),
            equity_share=self.equity_share.copy(),
            mean_depth_fraction=self.mean_depth_fraction.copy(),
            gross_volume=self.gross_volume.copy(),
            price_cap_hits=self.price_cap_hits.copy(),
            total_cash=self.total_cash.copy(),
            maximum_share_error=self.maximum_share_error.copy(),
        )


def run_market(config: MarketConfig) -> CrossSectionResult:
    return CrossSectionMarket(config).run()
