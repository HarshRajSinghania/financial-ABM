"""The disclosure game on top of the multi-asset market.

Each firm has a true attribute and may inflate its report. Every decision
period firms choose among genuine improvement, inflating the report, or
neither. NPV policies compare discounted values; Q-learning uses realized
ledger rewards with the same discrete action candidates:

* market pricing of the signal: perturb one firm's signal while holding
  prices, wealth and expectations fixed. Its local permanent quote response
  predicts the reduction in a financing fee on fixed exposure F. The annual
  fee rate is rf + spread * F / (F + lagged market cap), locked between
  repricing dates. This pricing relationship is an explicit assumption;
* improve: discounted financing savings times visible improvement, plus subsidy,
  minus ``c * Delta^2``. Beyond the report's remaining capacity, real
  improvement replaces inflation, so only its ``transparency`` share is
  immediately visible. The optimum is piecewise quadratic;
* inflate: financing savings survive until an audit changes the quote used
  at the next repricing. Cash flows are discounted daily over an explicit
  finite horizon; the eventual fine remains a discounted liability.

Changes respect the period cap and remaining capacity including pending
actions. The dividend-yield proxy ``k_i = yield * V_i / P_i`` and its
cross-sectional slope are diagnostic only, not borrowing rates.

``c`` is the firm's marginal cost scale ``c_i * exp(eta * g_i)``. Costs,
fines and subsidies change intrinsic value and reach prices through the
market makers' news pass-through on the next trading day. Daily financing
fees are accrued, not paid from a cash account. Relative to the initial
fee already embedded in the value anchor, changes in fees adjust value
once. No separate quote gain is added to the firm's objective.

Investors imitate by pairwise proportional imitation (Schlag 1998): every
imitation period a fraction of investors reconsiders, and switches to the
other type with probability ``intensity * max(0, growth_other - growth_own)``
using the two types' mean wealth growth over the period. With equal
performance shares stay put. A logit re-draw (the application's rule) instead
pulls the impact share towards one half whenever performance is similar,
which would manufacture a "transition" out of the update rule itself.
"""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from statistics import NormalDist

import numpy as np
from numpy.typing import NDArray

from ..manifest import canonical_json_bytes
from ..tabular import CompanyQLearner
from .config import TRADING_DAYS_PER_YEAR, MarketConfig
from .domain import DomainSpec
from .financing import financing_signal_factors
from .harness import CrossSectionMarket, CrossSectionResult, _cap_buys_to_cash
from .investors import IMPACT_INVESTOR, PROFIT_MAXIMIZER
from .learning import batch_update, choose_actions, context_states, discrete_candidates, npv_discrete, realized_rewards, table_fingerprint
from .policy import PolicyRegime, PolicySchedule

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

IMPROVE, INFLATE, MAINTAIN = 0, 1, 2
ACTION_NAMES = ("improve", "wash", "maintain")
# A firm acts only if the best option is worth more than this fraction of
# its market cap, so floating-point noise does not count as a decision.
MINIMUM_NPV = 1e-9


@dataclass(slots=True)
class AttributeState:
    goodness: FloatArray
    inflation: FloatArray
    cost_scale: FloatArray
    pending: list[tuple[int, int, IntArray, FloatArray]] = field(default_factory=list)

    @classmethod
    def initialize(cls, domain: DomainSpec, size_class: IntArray, rng: np.random.Generator,
                   intrinsic_value: FloatArray | None = None) -> "AttributeState":
        size = size_class.size
        if domain.observation_link == "empirical_quantile":
            # Latent standard normal; the empirical raw marginal comes from the link.
            goodness = rng.standard_normal(size)
            rho = domain.initial_size_rank_correlation
            if rho:
                if intrinsic_value is None or np.shape(intrinsic_value) != (size,):
                    raise ValueError("a size rank correlation needs one intrinsic value per firm")
                log_value = np.log(intrinsic_value)
                spread = log_value.std()
                standardized = (log_value - log_value.mean()) / spread if spread > 0 else np.zeros(size)
                goodness = rho * standardized + np.sqrt(1 - rho**2) * goodness
            low, high = domain.goodness_bounds
            goodness = np.clip(goodness, low, high)
        elif domain.initial_empirical_distribution:
            support, counts = np.asarray(domain.initial_empirical_distribution, dtype=np.float64).T
            goodness = domain.to_goodness(rng.choice(support, size=size, p=counts / counts.sum()))
        else:
            low, high = domain.goodness_bounds
            normal = NormalDist()
            probabilities = rng.uniform(normal.cdf(low), normal.cdf(high), size)
            goodness = np.fromiter((normal.inv_cdf(p) for p in probabilities), dtype=np.float64, count=size)
        multipliers = np.asarray(domain.size_cost_multipliers)[size_class]
        dispersion = rng.lognormal(-0.5 * domain.real_cost_log_sd**2, domain.real_cost_log_sd, size)
        return cls(
            goodness=goodness,
            inflation=np.zeros(size),
            cost_scale=domain.real_cost_scale * multipliers * dispersion,
        )

    def observed(self, transparency: float) -> FloatArray:
        return self.goodness + (1.0 - transparency) * self.inflation

    def marginal_cost(self, domain: DomainSpec) -> FloatArray:
        return self.cost_scale * np.exp(domain.cost_level_elasticity * self.goodness)

    def schedule(self, due_day: int, kind: int, firms: IntArray, amounts: FloatArray) -> None:
        if firms.size:
            self.pending.append((due_day, kind, firms, amounts))

    def advance(self, day: int, domain: DomainSpec) -> None:
        """Natural decay, then improvements and inflations that fall due."""
        low, high = domain.goodness_bounds
        self.goodness = np.maximum(self.goodness - domain.natural_decay / TRADING_DAYS_PER_YEAR, low)
        remaining = []
        for item in self.pending:
            due_day, kind, firms, amounts = item
            if due_day > day:
                remaining.append(item)
            elif kind == IMPROVE:
                self.goodness[firms] = np.minimum(self.goodness[firms] + amounts, high)
            else:
                self.inflation[firms] += amounts
        self.pending = remaining
        # A report cannot exceed the scale's upper end.
        np.minimum(self.inflation, high - self.goodness, out=self.inflation)
        np.maximum(self.inflation, 0.0, out=self.inflation)


@dataclass(frozen=True, slots=True)
class FirmChoices:
    actions: IntArray
    amounts: FloatArray
    npv: FloatArray
    cost_fraction: FloatArray
    subsidy_fraction: FloatArray


def npv_choices(
    *,
    benefit: FloatArray,
    cost_of_capital: FloatArray,
    marginal_cost: FloatArray,
    regime: PolicyRegime,
    domain: DomainSpec,
    period_days: int,
    improve_capacity: FloatArray | None = None,
    inflate_capacity: FloatArray | None = None,
    horizon_days: int = 1260,
    repricing_interval: int = 60,
    decision_day: int = 0,
    published_now: NDArray[np.bool_] | None = None,
) -> FirmChoices:
    """Choose using annual financing savings per initial SD / current cap."""
    disclosure_delay = domain.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
    real_annuity, displaced_annuity, wash_annuity, detection = financing_signal_factors(
        cost_of_capital, decision_day=decision_day, horizon_days=horizon_days,
        repricing_interval=repricing_interval, period_days=period_days,
        implementation_delay=domain.implementation_delay_days,
        disclosure_delay=disclosure_delay, audit_probability=regime.audit_probability,
        transparency=regime.transparency, publish_audit_results=regime.publish_audit_results,
        published_now=published_now,
        reporting_interval_days=regime.reporting_interval_days,
    )
    improve_benefit = benefit * real_annuity
    improve_gain = improve_benefit + regime.subsidy
    inflate_gain = (
        benefit
        * (1.0 - regime.transparency)
        * wash_annuity
        - regime.penalty * detection
    )
    inflate_gain = np.maximum(inflate_gain, 0.0)
    wash_cost = domain.wash_cost_ratio * marginal_cost
    cap = domain.max_change_per_period
    improve_cap = cap if improve_capacity is None else np.clip(improve_capacity, 0.0, cap)
    inflate_cap = cap if inflate_capacity is None else np.clip(inflate_capacity, 0.0, cap)
    displaced_benefit = benefit * displaced_annuity
    displaced_gain = displaced_benefit + regime.subsidy
    improve_amount = np.minimum(improve_cap, np.maximum(
        np.minimum(improve_gain / (2.0 * marginal_cost), inflate_cap),
        displaced_gain / (2.0 * marginal_cost),
    ))
    inflate_amount = np.minimum(inflate_gain / (2.0 * wash_cost), inflate_cap)
    real_value = (improve_benefit * np.minimum(improve_amount, inflate_cap)
                  + displaced_benefit * np.maximum(improve_amount - inflate_cap, 0.0))
    values = np.column_stack((
        real_value + regime.subsidy * improve_amount - marginal_cost * improve_amount**2,
        inflate_gain * inflate_amount - wash_cost * inflate_amount**2,
        np.zeros_like(benefit),
    ))
    actions = np.argmax(values, axis=1)
    best = values[np.arange(actions.size), actions]
    actions[best <= MINIMUM_NPV] = MAINTAIN
    amounts = np.select([actions == IMPROVE, actions == INFLATE], [improve_amount, inflate_amount], 0.0)
    cost_fraction = np.select(
        [actions == IMPROVE, actions == INFLATE],
        [marginal_cost * amounts**2, wash_cost * amounts**2],
        0.0,
    )
    subsidy_fraction = np.where(actions == IMPROVE, regime.subsidy * amounts, 0.0)
    return FirmChoices(actions, amounts, np.where(actions == MAINTAIN, 0.0, best), cost_fraction, subsidy_fraction)


def pricing_slope(cost_of_capital: FloatArray, signal_z: FloatArray) -> float:
    """Diagnostic OLS slope of dividend yield on the fixed-scale signal."""
    centered = signal_z - signal_z.mean()
    variance = float(centered @ centered)
    if variance == 0:
        return 0.0
    return float(centered @ (cost_of_capital - cost_of_capital.mean()) / variance)


@dataclass(frozen=True, slots=True)
class DisclosureResult:
    market: CrossSectionResult
    true_goodness: FloatArray
    inflation: FloatArray
    impact_share: FloatArray
    impact_wealth_share: FloatArray
    pricing_slope: FloatArray
    actions: IntArray
    amounts: FloatArray
    detections: IntArray
    cost_fraction: FloatArray
    penalty_fraction: FloatArray
    subsidy_fraction: FloatArray
    financing_rate: FloatArray | None = None
    financing_cost: FloatArray | None = None
    financing_value_adjustment: FloatArray | None = None
    public_signal: FloatArray | None = None
    planning_signal: FloatArray | None = None
    disclosure_error: FloatArray | None = None
    audit_selected: IntArray | None = None
    audit_publications: IntArray | None = None
    verified_goodness: FloatArray | None = None
    action_due_day: IntArray | None = None
    applied_resource_cost: FloatArray | None = None
    applied_fine: FloatArray | None = None
    applied_subsidy: FloatArray | None = None
    learning_states: IntArray | None = None
    learning_groups: IntArray | None = None
    valid_actions: NDArray[np.bool_] | None = None
    learning_rewards: FloatArray | None = None
    learning_transition: NDArray[np.bool_] | None = None
    unvisited_state: NDArray[np.bool_] | None = None
    learning_choices: IntArray | None = None
    coverage_forced: NDArray[np.bool_] | None = None
    learning_update: NDArray[np.bool_] | None = None

    def fingerprint(self) -> str:
        digest = hashlib.sha256(self.market.fingerprint().encode("ascii"))
        for array in (
            self.true_goodness, self.inflation, self.impact_share, self.impact_wealth_share,
            self.pricing_slope, self.actions, self.amounts, self.detections,
            self.cost_fraction, self.penalty_fraction, self.subsidy_fraction,
            self.financing_rate, self.financing_cost, self.financing_value_adjustment,
            self.public_signal, self.planning_signal, self.disclosure_error,
            self.audit_selected, self.audit_publications, self.verified_goodness, self.action_due_day,
            self.applied_resource_cost, self.applied_fine, self.applied_subsidy,
            self.learning_states, self.learning_groups, self.valid_actions,
            self.learning_rewards, self.learning_transition, self.unvisited_state,
            self.learning_choices, self.coverage_forced, self.learning_update,
        ):
            if array is None:
                continue
            contiguous = np.ascontiguousarray(array)
            digest.update(str(contiguous.dtype).encode("ascii"))
            digest.update(contiguous.tobytes())
        return digest.hexdigest()


class DisclosureMarket(CrossSectionMarket):
    def __init__(
        self, config: MarketConfig, domain: DomainSpec, policy: PolicySchedule | None = None,
        *, learner: CompanyQLearner | None = None, training: bool = False, coverage_target: int = 0,
        common_prepolicy_sha256: str | None = None,
    ):
        policy = policy or PolicySchedule.constant(domain)
        if type(training) is not bool:
            raise ValueError("training must be boolean")
        if type(coverage_target) is not int or coverage_target < 0:
            raise ValueError("coverage_target must be a nonnegative integer")
        if common_prepolicy_sha256 is not None:
            if (not isinstance(common_prepolicy_sha256, str) or len(common_prepolicy_sha256) != 64
                    or any(char not in "0123456789abcdef" for char in common_prepolicy_sha256)):
                raise ValueError("common_prepolicy_sha256 must be a SHA256 digest")
            if policy.intervention is None or not 0 < policy.start_day <= config.trading_days:
                raise ValueError("common pre-policy deployment requires an explicit policy switch")
        if config.firm_policy == "q_learning":
            if not isinstance(learner, CompanyQLearner):
                raise ValueError("q_learning requires an explicit CompanyQLearner")
            action_count = 2 * len(config.firm_action_fractions) + 1
            if learner.values.shape not in ((3, 81, action_count), (6, 81, action_count)) or learner.counts.shape != learner.values.shape:
                raise ValueError("learner must have three or six groups of 81 states matching the action grid")
            if policy.intervention is not None and learner.values.shape[0] != 6:
                raise ValueError("a policy intervention requires six learner groups")
            if not np.isfinite(learner.values).all() or not np.issubdtype(learner.counts.dtype, np.integer) or np.any(learner.counts < 0):
                raise ValueError("learner values and visit counts must be valid")
            writable = learner.values.flags.writeable and learner.counts.flags.writeable
            if training and not writable:
                raise ValueError("training requires a writable learner")
            if not training and (learner.epsilon != 0 or learner.values.flags.writeable or learner.counts.flags.writeable):
                raise ValueError("evaluation requires readonly values/counts and epsilon zero")
        elif learner is not None or training or coverage_target or common_prepolicy_sha256 is not None:
            raise ValueError("learner and training are only valid for q_learning")
        super().__init__(config)
        self.domain = domain
        self.policy = policy
        self.learner = learner
        self.training = training
        self.coverage_target = coverage_target
        self.common_prepolicy_sha256 = common_prepolicy_sha256
        identity = {
            "config": config.to_dict(), "domain": domain.to_dict(), "policy": asdict(self.policy),
        }
        if learner is not None:
            identity["learning"] = {"training": training, "table_fingerprint": table_fingerprint(learner),
                                    "epsilon": learner.epsilon, "learning_rate": learner.learning_rate,
                                    "discount": learner.discount}
            if coverage_target:
                identity["learning"]["coverage_target"] = coverage_target
            if common_prepolicy_sha256 is not None:
                identity["learning"]["common_prepolicy_sha256"] = common_prepolicy_sha256
                identity["learning"]["prepolicy_protocol"] = "frozen_baseline_greedy_prefix_post_zero_v1"
        self.run_id = hashlib.sha256(canonical_json_bytes(identity)).hexdigest()
        attribute_seed, audit_seed, learning_seed, signal_seed, firm_seed = np.random.SeedSequence([config.seed, 1]).spawn(5)
        self.attribute_rng = np.random.default_rng(attribute_seed)
        self.audit_rng = np.random.default_rng(audit_seed)
        self.learning_rng = np.random.default_rng(learning_seed)
        self.signal_rng = np.random.default_rng(signal_seed)
        self.firm_rng = np.random.default_rng(firm_seed)
        self.attributes = AttributeState.initialize(domain, self.firms.size_class, self.attribute_rng,
                                                    intrinsic_value=self.firms.intrinsic_value)

        investors = self.investors
        self.latent_taste = config.taste_median * self.learning_rng.lognormal(
            0.0, config.taste_log_sd, investors.size
        )
        is_impact = self.learning_rng.random(investors.size) < config.initial_impact_share
        investors.investor_type[:] = np.where(is_impact, IMPACT_INVESTOR, PROFIT_MAXIMIZER)
        investors.taste[:] = self.latent_taste * is_impact
        self.window_wealth = investors.wealth(self.prices)
        self.pending_value_change = np.zeros(config.n_firms)
        self.financing_exposure = config.financing_exposure_fraction * self.prices.copy()
        self.contract_rate = self.quoted_financing_rate()
        self.initial_contract_rate = self.contract_rate.copy()

        days, firms = config.trading_days + 1, config.n_firms
        decisions = config.trading_days // config.firm_decision_interval + 1
        self.true_history = np.empty((days, firms))
        self.inflation_history = np.empty((days, firms))
        self.impact_share = np.empty(days)
        self.impact_wealth_share = np.empty(days)
        self.slope_history = np.full(days, np.nan)
        self.action_history = np.full((decisions, firms), MAINTAIN, dtype=np.int64)
        self.amount_history = np.zeros((decisions, firms))
        self.detection_history = np.zeros((decisions, firms), dtype=np.int64)
        self.cost_history = np.zeros((decisions, firms))
        self.penalty_history = np.zeros((decisions, firms))
        self.subsidy_history = np.zeros((decisions, firms))
        self.financing_rate_history = np.empty((days, firms))
        self.financing_rate_history[0] = self.contract_rate
        self.financing_cost_history = np.zeros((days, firms))
        self.financing_adjustment_history = np.zeros((days, firms))
        self.public_signal_history = np.empty((days, firms))
        self.planning_signal_history = np.empty((days, firms))
        self.disclosure_error_history = np.empty((days, firms))
        self.audit_selected_history = np.zeros((decisions, firms), dtype=np.int64)
        self.publication_history = np.zeros((decisions, firms), dtype=np.int64)
        self.verified_goodness_history = np.zeros((decisions, firms))
        self.action_due_history = np.full((decisions, firms), -1, dtype=np.int64)
        self.applied_resource_cost_history = None
        self.applied_fine_history = None
        self.applied_subsidy_history = None
        self.learning_state_history = None
        self.learning_group_history = None
        self.valid_action_history = None
        self.learning_reward_history = None
        self.learning_transition_history = None
        self.unvisited_state_history = None
        self.choice_history = None
        self.coverage_forced_history = None
        self.learning_update_history = None
        if config.firm_policy != "npv":
            self.pending_resource_cost = np.zeros(firms)
            self.pending_fine = np.zeros(firms)
            self.pending_subsidy = np.zeros(firms)
            self.applied_resource_cost_history = np.zeros((days, firms))
            self.applied_fine_history = np.zeros((days, firms))
            self.applied_subsidy_history = np.zeros((days, firms))
            self.learning_state_history = np.full((decisions, firms), -1, dtype=np.int64)
            self.learning_group_history = np.full((decisions, firms), -1, dtype=np.int64)
            self.valid_action_history = np.zeros((decisions, firms, 2 * len(config.firm_action_fractions) + 1), dtype=bool)
            self.choice_history = np.full((decisions, firms), MAINTAIN, dtype=np.int64)
            self.learning_reward_history = np.full((decisions, firms), np.nan)
            self.learning_transition_history = np.zeros((decisions, firms), dtype=bool)
            if learner is not None:
                self.unvisited_state_history = np.zeros((decisions, firms), dtype=bool)
                if training and coverage_target:
                    self.coverage_forced_history = np.zeros((decisions, firms), dtype=bool)
                if common_prepolicy_sha256 is not None:
                    self.learning_update_history = np.zeros((decisions, firms), dtype=bool)
        self.signal_day = -1
        self._prepare_signals(0)
        self._record_attributes(0)

    # -- signals and pricing -------------------------------------------------
    def signal_z(self, day: int) -> FloatArray:
        """Archived trading signal; future days cannot be queried."""
        if not 0 <= day <= self.signal_day:
            raise ValueError("public signal has not been prepared for that day")
        return self.public_signal_history[day].copy()

    def attribute_signal(self) -> FloatArray:
        """Current-stage public information from reports and dated audits."""
        return self.planning_signal_history[self.signal_day].copy()

    def _public_signal(self, day: int) -> FloatArray:
        signal = self.report_cache.copy()
        period = (day - 1) // self.config.firm_decision_interval
        if period >= 0:
            public = self.publication_history[period].astype(bool)
            signal[public] = self.verified_goodness_history[period, public]
        return signal

    def _prepare_signals(self, day: int) -> None:
        if day == self.signal_day:
            return
        if day < self.signal_day:
            raise ValueError("signal days must move forwards")
        regime = self.policy.at(day)
        self.disclosure_error_history[day] = regime.disclosure_noise_sd * self.signal_rng.standard_normal(self.config.n_firms)
        if day == 0 or day % regime.reporting_interval_days == 0:
            self.report_cache = self.attributes.observed(regime.transparency) + self.disclosure_error_history[day]
        self.public_signal_history[day] = self._public_signal(day)
        self.planning_signal_history[day] = self.public_signal_history[day]
        self.signal_day = day

    def cost_of_capital(self) -> FloatArray:
        """Dividend-yield diagnostic, separate from the financing contract."""
        return self.config.cash_flow_yield * self.firms.intrinsic_value / self.prices

    def quoted_financing_rate(self) -> FloatArray:
        return self.config.risk_free_rate + self.config.financing_spread * (
            self.financing_exposure / (self.financing_exposure + self.prices)
        )

    def marginal_financing_saving(self) -> FloatArray:
        """Annual fee saving per SD, normalized by current market cap."""
        exposure = self.financing_exposure
        rate_response = self.config.financing_spread * exposure * self.prices / (exposure + self.prices)**2
        return exposure / self.prices * rate_response * self.marginal_signal_value()

    def marginal_signal_value(self) -> FloatArray:
        """Local permanent quote response per initial SD, for one rebalance each."""
        cfg, investors = self.config, self.investors
        if cfg.rebalance_speed == 0:
            return np.zeros(cfg.n_firms)
        who = np.arange(investors.size)
        signal = self.attribute_signal()
        expected = self.expected_returns()
        arguments = dict(
            prices=self.prices,
            expected_returns=expected,
            annual_market_covariance=self.market_covariance * TRADING_DAYS_PER_YEAR,
            market_expected_return=float(self.prices @ expected / self.prices.sum()),
            market_annual_variance=self.allocation_market_variance * TRADING_DAYS_PER_YEAR,
            config=cfg,
        )
        baseline = investors.desired_orders(who, attribute=signal, **arguments)
        target_shares = np.maximum(baseline / cfg.rebalance_speed + investors.holdings, 0.0)
        target_values = target_shares * self.prices
        target_equity = target_values.sum(axis=1, keepdims=True)
        weights = np.divide(target_values, target_equity, out=np.zeros_like(target_values), where=target_equity > 0)
        baseline = cfg.rebalance_speed * (target_shares - investors.holdings)
        baseline = np.maximum(baseline, -investors.holdings)
        baseline = _cap_buys_to_cash(baseline, investors.cash, self.prices, cfg.transaction_cost_rate)
        response = np.empty(cfg.n_firms)
        increment = 1e-4
        relative_tilt = np.expm1(increment * investors.choice_intensity * investors.taste)
        for firm in range(cfg.n_firms):
            targets = target_shares / (1.0 + weights[:, firm] * relative_tilt)[:, None]
            targets[:, firm] *= 1.0 + relative_tilt
            orders = cfg.rebalance_speed * (targets - investors.holdings)
            orders = np.maximum(orders, -investors.holdings)
            orders = _cap_buys_to_cash(orders, investors.cash, self.prices, cfg.transaction_cost_rate)
            response[firm] = (orders[:, firm] - baseline[:, firm]).sum() / increment
        return np.maximum(response, 0.0) * cfg.price_impact * cfg.permanent_impact_fraction / cfg.liquidity_fraction

    # -- hooks ---------------------------------------------------------------
    def _pre_trade(self, day: int) -> FloatArray:
        self.attributes.advance(day, self.domain)
        value_before = self.firms.intrinsic_value.copy()
        self.firms.intrinsic_value += self.pending_value_change
        self.pending_value_change = np.zeros(self.config.n_firms)
        if np.any(self.firms.intrinsic_value <= 0) or not np.isfinite(self.firms.intrinsic_value).all():
            raise ValueError(f"firm expenditure exhausts the value anchor on day {day}")
        if self.applied_resource_cost_history is not None:
            self.applied_resource_cost_history[day] = self.pending_resource_cost
            self.applied_fine_history[day] = self.pending_fine
            self.applied_subsidy_history[day] = self.pending_subsidy
            self.pending_resource_cost.fill(0)
            self.pending_fine.fill(0)
            self.pending_subsidy.fill(0)
        if day % self.config.financing_repricing_interval == 0:
            self.contract_rate = self.quoted_financing_rate()
        fees = self.financing_exposure * self.contract_rate / TRADING_DAYS_PER_YEAR
        adjustment = self.financing_exposure * (self.initial_contract_rate - self.contract_rate) / TRADING_DAYS_PER_YEAR
        self.firms.intrinsic_value += adjustment
        if np.any(self.firms.intrinsic_value <= 0) or not np.isfinite(self.firms.intrinsic_value).all():
            raise ValueError(f"financing adjustment exhausts the value anchor on day {day}")
        changes = np.log(self.firms.intrinsic_value / value_before)
        self.financing_rate_history[day] = self.contract_rate
        self.financing_cost_history[day] = fees
        self.financing_adjustment_history[day] = adjustment
        self._prepare_signals(day)
        return changes

    def _post_trade(self, day: int) -> None:
        cfg = self.config
        if day % cfg.firm_decision_interval == 0:
            self._audit_and_decide(day, day // cfg.firm_decision_interval)
        if day % cfg.imitation_interval == 0:
            self._imitate()
        self._record_attributes(day)

    def _audit_and_decide(self, day: int, period: int) -> None:
        self._prepare_signals(day)
        regime = self.policy.at(day)
        state = self.attributes
        k = self.cost_of_capital()
        self.slope_history[day] = pricing_slope(k, self.signal_z(day))
        selected = self.audit_rng.random(state.inflation.size) < regime.audit_probability
        caught = selected & (state.inflation > 0)
        penalty = np.where(caught, regime.penalty * state.inflation, 0.0)
        state.inflation[caught] = 0.0
        self.report_cache[selected] = state.observed(regime.transparency)[selected] + self.disclosure_error_history[day, selected]
        published = selected & regime.publish_audit_results
        self.audit_selected_history[period] = selected
        self.publication_history[period] = published
        self.verified_goodness_history[period, published] = state.goodness[published]
        self.planning_signal_history[day] = self._public_signal(day)

        high = self.domain.goodness_bounds[1]
        improve_capacity = high - state.goodness
        inflate_capacity = high - state.goodness - state.inflation
        for _, kind, firms, amounts in state.pending:
            if kind == IMPROVE:
                np.subtract.at(improve_capacity, firms, amounts)
            np.subtract.at(inflate_capacity, firms, amounts)
        if self.config.firm_policy == "npv":
            choices = npv_choices(
                benefit=self.marginal_financing_saving(),
                cost_of_capital=np.full(self.config.n_firms, self.config.firm_discount_rate),
                marginal_cost=state.marginal_cost(self.domain),
                regime=regime,
                domain=self.domain,
                period_days=self.config.firm_decision_interval,
                improve_capacity=improve_capacity,
                inflate_capacity=inflate_capacity,
                horizon_days=self.config.financing_horizon_days,
                repricing_interval=self.config.financing_repricing_interval,
                decision_day=day,
                published_now=published,
            )
        else:
            choices = self._discrete_decision(day, period, regime, published, penalty,
                                              improve_capacity, inflate_capacity)
        improve = np.flatnonzero(choices.actions == IMPROVE)
        inflate = np.flatnonzero(choices.actions == INFLATE)
        real_due = day + max(1, self.domain.implementation_delay_days)
        disclosure_delay = self.domain.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
        wash_due = day + max(1, disclosure_delay)
        state.schedule(real_due, IMPROVE, improve, choices.amounts[improve])
        state.schedule(wash_due, INFLATE, inflate, choices.amounts[inflate])
        self.action_due_history[period, improve] = real_due
        self.action_due_history[period, inflate] = wash_due

        # Fractions of market cap become changes in intrinsic value.
        value_change = (choices.subsidy_fraction - choices.cost_fraction - penalty) * self.prices
        ratio = 1.0 + (value_change + self.pending_value_change) / self.firms.intrinsic_value
        if np.any(ratio <= 0) or not np.isfinite(ratio).all():
            raise ValueError(f"firm expenditure exhausts the value anchor on day {day}")
        self.pending_value_change += value_change
        if self.applied_resource_cost_history is not None:
            self.pending_resource_cost += choices.cost_fraction * self.prices
            self.pending_fine += penalty * self.prices
            self.pending_subsidy += choices.subsidy_fraction * self.prices

        self.action_history[period] = choices.actions
        self.amount_history[period] = choices.amounts
        self.detection_history[period] = caught
        self.cost_history[period] = choices.cost_fraction
        self.penalty_history[period] = penalty
        self.subsidy_history[period] = choices.subsidy_fraction

    def _discrete_decision(
        self, day: int, period: int, regime: PolicyRegime, published: NDArray[np.bool_],
        penalty: FloatArray, improve_capacity: FloatArray, inflate_capacity: FloatArray,
    ) -> FirmChoices:
        cfg, domain, state = self.config, self.domain, self.attributes
        disclosure_delay = domain.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
        real, displaced, wash, fine = financing_signal_factors(
            np.full(cfg.n_firms, cfg.firm_discount_rate), decision_day=day,
            horizon_days=cfg.financing_horizon_days, repricing_interval=cfg.financing_repricing_interval,
            period_days=cfg.firm_decision_interval, implementation_delay=domain.implementation_delay_days,
            disclosure_delay=disclosure_delay, audit_probability=regime.audit_probability,
            transparency=regime.transparency, publish_audit_results=regime.publish_audit_results,
            published_now=published,
            reporting_interval_days=regime.reporting_interval_days,
        )
        benefit = self.marginal_financing_saving()
        marginal_cost = state.marginal_cost(domain)
        candidates = discrete_candidates(
            improve_capacity=improve_capacity, inflate_capacity=inflate_capacity,
            marginal_cost=marginal_cost, max_change_per_period=domain.max_change_per_period,
            wash_cost_ratio=domain.wash_cost_ratio, subsidy=regime.subsidy,
            real_value_per_sd=benefit * real, displaced_real_value_per_sd=benefit * displaced,
            wash_value_per_sd=benefit * (1 - regime.transparency) * wash,
            fine_value_per_sd=regime.penalty * fine,
            amplitude_fractions=cfg.firm_action_fractions,
        )
        changes = (candidates.subsidy_fraction - candidates.cost_fraction - penalty[:, None]) * self.prices[:, None]
        ratio = 1.0 + (changes + self.pending_value_change[:, None]) / self.firms.intrinsic_value[:, None]
        candidates.valid_actions[:] &= np.isfinite(ratio) & (ratio > 0)
        if not candidates.valid_actions.any(axis=1).all():
            raise ValueError(f"no feasible firm action preserves the value anchor on day {day}")
        due = np.full(cfg.n_firms, np.inf)
        for due_day, _, firms, _ in state.pending:
            np.minimum.at(due, firms, due_day - day)
        due[~np.isfinite(due)] = -1
        known_cash = self.pending_resource_cost + self.pending_fine + self.pending_subsidy + penalty * self.prices
        states = context_states(
            financing_exposure=self.financing_exposure, prices=self.prices, inflation=state.inflation,
            marginal_cost=marginal_cost, real_cost_scale=domain.real_cost_scale,
            max_change_per_period=domain.max_change_per_period, pending_due_days=due,
            pending_cash_amount=known_cash, decision_days=cfg.firm_decision_interval,
        )
        epoch = int(self.policy.intervention is not None and day >= self.policy.start_day)
        groups = self.firms.size_class + 3 * epoch
        self.learning_state_history[period] = states
        self.learning_group_history[period] = groups
        self.valid_action_history[period] = candidates.valid_actions
        if period > 1:
            rewards = realized_rewards(
                self.financing_adjustment_history, self.applied_resource_cost_history,
                self.applied_fine_history, self.applied_subsidy_history, self.price_path[0],
                start_day=day - cfg.firm_decision_interval, end_day=day,
                annual_discount_rate=cfg.firm_discount_rate,
            )
            self.learning_reward_history[period] = rewards
            self.learning_transition_history[period] = True
            if self.training:
                if self.common_prepolicy_sha256 is None:
                    batch_update(
                        self.learner, np.arange(cfg.n_firms), self.learning_group_history[period - 1],
                        self.learning_state_history[period - 1], self.choice_history[period - 1], rewards,
                        groups, states, candidates.valid_actions, elapsed_days=cfg.firm_decision_interval,
                        annual_discount_rate=cfg.firm_discount_rate, terminated=np.zeros(cfg.n_firms, dtype=bool),
                    )
                else:
                    update = self.learning_group_history[period - 1] >= 3
                    self.learning_update_history[period] = update
                    if update.any():
                        batch_update(
                            self.learner, np.arange(cfg.n_firms)[update], self.learning_group_history[period - 1, update],
                            self.learning_state_history[period - 1, update], self.choice_history[period - 1, update], rewards[update],
                            groups[update], states[update], candidates.valid_actions[update], elapsed_days=cfg.firm_decision_interval,
                            annual_discount_rate=cfg.firm_discount_rate, terminated=np.zeros(int(update.sum()), dtype=bool),
                        )
        if self.learner is None:
            actions = npv_discrete(candidates, MINIMUM_NPV)
            values = candidates.values[np.arange(cfg.n_firms), actions]
        else:
            self.unvisited_state_history[period] = self.learner.counts[groups, states].sum(axis=1) == 0
            training = self.training and (self.common_prepolicy_sha256 is None or epoch == 1)
            actions = choose_actions(self.learner, groups, states, candidates.valid_actions,
                                     self.firm_rng if training else None, training=training,
                                     coverage_target=self.coverage_target if day + cfg.firm_decision_interval <= cfg.trading_days else 0,
                                     forced_choices=None if self.coverage_forced_history is None else self.coverage_forced_history[period])
            values = np.zeros(cfg.n_firms)
        rows = np.arange(cfg.n_firms)
        self.choice_history[period] = actions
        return FirmChoices(candidates.kinds[actions], candidates.amounts[rows, actions], values,
                           candidates.cost_fraction[rows, actions], candidates.subsidy_fraction[rows, actions])

    def _imitate(self) -> None:
        cfg, investors = self.config, self.investors
        wealth = investors.wealth(self.prices)
        growth = wealth / self.window_wealth - 1.0
        self.window_wealth = wealth
        impact = investors.investor_type == IMPACT_INVESTOR
        if impact.all() or not impact.any():
            return
        advantage = float(growth[impact].mean() - growth[~impact].mean())
        count = max(1, int(round(cfg.imitation_update_fraction * investors.size)))
        chosen = self.learning_rng.choice(investors.size, size=count, replace=False)
        own_advantage = np.where(impact[chosen], advantage, -advantage)
        switch_probability = np.clip(-cfg.imitation_intensity * own_advantage, 0.0, 1.0)
        switches = chosen[self.learning_rng.random(count) < switch_probability]
        becomes_impact = ~impact[switches]
        investors.investor_type[switches] = np.where(becomes_impact, IMPACT_INVESTOR, PROFIT_MAXIMIZER)
        investors.taste[switches] = self.latent_taste[switches] * becomes_impact

    def _record_attributes(self, day: int) -> None:
        investors = self.investors
        impact = investors.investor_type == IMPACT_INVESTOR
        wealth = investors.wealth(self.prices)
        self.true_history[day] = self.attributes.goodness
        self.inflation_history[day] = self.attributes.inflation
        self.impact_share[day] = float(impact.mean())
        self.impact_wealth_share[day] = float(wealth[impact].sum() / wealth.sum())

    def run(self) -> DisclosureResult:
        market = super().run()
        return DisclosureResult(
            market=market,
            true_goodness=self.true_history.copy(),
            inflation=self.inflation_history.copy(),
            impact_share=self.impact_share.copy(),
            impact_wealth_share=self.impact_wealth_share.copy(),
            pricing_slope=self.slope_history.copy(),
            actions=self.action_history.copy(),
            amounts=self.amount_history.copy(),
            detections=self.detection_history.copy(),
            cost_fraction=self.cost_history.copy(),
            penalty_fraction=self.penalty_history.copy(),
            subsidy_fraction=self.subsidy_history.copy(),
            financing_rate=self.financing_rate_history.copy(),
            financing_cost=self.financing_cost_history.copy(),
            financing_value_adjustment=self.financing_adjustment_history.copy(),
            public_signal=self.public_signal_history.copy(),
            planning_signal=self.planning_signal_history.copy(),
            disclosure_error=self.disclosure_error_history.copy(),
            audit_selected=self.audit_selected_history.copy(),
            audit_publications=self.publication_history.copy(),
            verified_goodness=self.verified_goodness_history.copy(),
            action_due_day=self.action_due_history.copy(),
            **{name: None if array is None else array.copy() for name, array in (
                ("applied_resource_cost", self.applied_resource_cost_history),
                ("applied_fine", self.applied_fine_history),
                ("applied_subsidy", self.applied_subsidy_history),
                ("learning_states", self.learning_state_history),
                ("learning_groups", self.learning_group_history),
                ("valid_actions", self.valid_action_history),
                ("learning_rewards", self.learning_reward_history),
                ("learning_transition", self.learning_transition_history),
                ("unvisited_state", self.unvisited_state_history),
                ("learning_choices", self.choice_history if len(self.config.firm_action_fractions) > 1 else None),
                ("coverage_forced", self.coverage_forced_history),
                ("learning_update", self.learning_update_history),
            )},
        )


def run_disclosure(config: MarketConfig, domain: DomainSpec, policy: PolicySchedule | None = None) -> DisclosureResult:
    return DisclosureMarket(config, domain, policy).run()
