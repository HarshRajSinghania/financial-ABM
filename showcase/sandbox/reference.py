"""Python reference for the browser sandbox: full-model snapshots and simplified dynamics.

The simplified dynamics keep the full model's firm side: the continuous NPV
decision (``npv_choices``), the new-case probability of the fixed fine,
capacities including pending actions, delayed real improvements and reports,
natural decay and random audits every decision period. They drop the investor
market. Each firm's financing benefit B (annual fee saving per SD over market
cap) and its market cap stay at a snapshot value, so preferences, prices and
financing never respond to what firms do. Results are illustrations of the
decision layer, not research results.

``showcase/sandbox/core.js`` ports this module; the cross-language fixtures
require the two to agree period by period. Audits draw from ``Mulberry32``,
which both languages implement bit for bit.

This module sits outside ``src/abm`` on purpose: the package's source hashes
are part of every frozen experiment identity.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.firms import SIZE_CLASS_NAMES
from abm.disclosure.game import IMPROVE, INFLATE, MAINTAIN, AttributeState, DisclosureMarket, new_case_probability, npv_choices
from abm.disclosure.policy import PolicyRegime, PolicySchedule

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

SNAPSHOT_DAY = 1200
SWITCH_DAY = 1201
TRADING_DAYS = 3500
DECISION_INTERVAL = 60
HORIZON_DAYS = 1260
REPRICING_INTERVAL = 60
DISCOUNT_RATE = 0.05
MASK = 0xFFFFFFFF


def _imul(a: int, b: int) -> int:
    return (a * b) & MASK


class Mulberry32:
    """32-bit generator shared with JavaScript; ``random()`` returns k / 2**32."""

    def __init__(self, seed: int):
        if type(seed) is not int or not 0 <= seed <= MASK:
            raise ValueError("seed must be an unsigned 32-bit integer")
        self.state = seed

    def random(self) -> float:
        self.state = (self.state + 0x6D2B79F5) & MASK
        t = self.state
        t = _imul(t ^ (t >> 15), t | 1)
        t = ((t + _imul(t ^ (t >> 7), t | 61)) & MASK) ^ t
        return ((t ^ (t >> 14)) & MASK) / 4294967296

    def uniforms(self, size: int) -> FloatArray:
        return np.fromiter((self.random() for _ in range(size)), dtype=np.float64, count=size)


# -- snapshots of the full model ------------------------------------------------

class _SnapshotTaken(Exception):
    pass


class SnapshotMarket(DisclosureMarket):
    """Full disclosure market that records one decision day's inputs, read only.

    The record holds the post-audit state that the firm decision sees: true
    level, inflation, pending actions, market cap and the financing benefit B,
    together with the decision the full model took. Reading the state does not
    change the run, so the result equals an ordinary ``DisclosureMarket`` run.
    """

    def __init__(self, *args, snapshot_day: int = SNAPSHOT_DAY, stop_after_snapshot: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        if self.config.firm_policy != "npv":
            raise ValueError("snapshots describe the continuous NPV rule")
        if snapshot_day <= 0 or snapshot_day % self.config.firm_decision_interval:
            raise ValueError("the snapshot day must be a positive decision day")
        self.snapshot_day = snapshot_day
        self.stop_after_snapshot = stop_after_snapshot
        self.snapshot: dict | None = None
        self.initial_goodness = self.attributes.goodness.copy()
        self.benefit_history: dict[int, FloatArray] = {}
        self._day = -1

    def marginal_financing_saving(self) -> FloatArray:
        value = super().marginal_financing_saving()
        self.benefit_history[self._day] = value.copy()
        return value

    def _audit_and_decide(self, day: int, period: int) -> None:
        self._day = day
        if day != self.snapshot_day:
            super()._audit_and_decide(day, period)
            return
        state = self.attributes
        goodness, inflation = state.goodness.copy(), state.inflation.copy()
        pending = [(due, kind, firms.copy(), amounts.copy()) for due, kind, firms, amounts in state.pending]
        prices = self.prices.copy()
        super()._audit_and_decide(day, period)
        inflation[self.detection_history[period].astype(bool)] = 0.0
        self.snapshot = {
            "day": day, "goodness": goodness, "inflation": inflation, "pending": pending, "prices": prices,
            "benefit": self.benefit_history[day].copy(), "actions": self.action_history[period].copy(),
            "amounts": self.amount_history[period].copy(),
        }

    def _post_trade(self, day: int) -> None:
        super()._post_trade(day)
        if self.stop_after_snapshot and day == self.snapshot_day:
            raise _SnapshotTaken


def take_snapshot(market: SnapshotMarket):
    """Run the market; returns the full result, or None if it stopped at the snapshot."""
    try:
        return market.run()
    except _SnapshotTaken:
        return None


# -- simplified dynamics -----------------------------------------------------------

@dataclass(frozen=True, slots=True)
class SandboxFirms:
    """Fixed firm inputs of the simplified dynamics (one row per firm)."""

    size_class: IntArray
    initial_goodness: FloatArray
    cost_scale: FloatArray
    market_cap: FloatArray
    benefit: FloatArray

    def __post_init__(self) -> None:
        n = self.size_class.size
        for name in ("initial_goodness", "cost_scale", "market_cap", "benefit"):
            value = getattr(self, name)
            if value.shape != (n,) or not np.isfinite(value).all():
                raise ValueError(f"{name} must hold one finite value per firm")
        if (self.cost_scale <= 0).any() or (self.market_cap <= 0).any() or (self.benefit < 0).any():
            raise ValueError("costs and market caps must be positive and benefits nonnegative")


def decision_capacities(state: AttributeState, report_bound: float) -> tuple[FloatArray, FloatArray]:
    """Room up to the highest report, net of pending actions (as in ``DisclosureMarket``)."""
    improve_capacity = report_bound - state.goodness
    inflate_capacity = report_bound - state.goodness - state.inflation
    for _, kind, firms, amounts in state.pending:
        if kind == IMPROVE:
            np.subtract.at(improve_capacity, firms, amounts)
        np.subtract.at(inflate_capacity, firms, amounts)
    return improve_capacity, inflate_capacity


def decide(state: AttributeState, firms: SandboxFirms, domain: DomainSpec, regime: PolicyRegime, day: int,
           published: NDArray[np.bool_] | None = None):
    """One period's NPV choices for every firm, with the full model's inputs except B and price."""
    if regime.publish_audit_results or regime.reporting_interval_days != 1:
        raise ValueError("the sandbox supports unpublished audits and daily reports only")
    improve_capacity, inflate_capacity = decision_capacities(state, domain.report_bound)
    disclosure_delay = domain.disclosure_delay_days if regime.disclosure_delay_days is None else regime.disclosure_delay_days
    wash_due = day + max(1, disclosure_delay)
    new_case_fine = None
    if regime.fixed_fine:
        new_case_fine = regime.fixed_fine / firms.market_cap * new_case_probability(
            state.inflation, state.pending, decision_day=day, wash_due=wash_due,
            period_days=DECISION_INTERVAL, audit_probability=regime.audit_probability,
        )
    choices = npv_choices(
        benefit=firms.benefit, cost_of_capital=np.full(firms.benefit.size, DISCOUNT_RATE),
        marginal_cost=state.marginal_cost(domain), regime=regime, domain=domain,
        period_days=DECISION_INTERVAL, improve_capacity=improve_capacity, inflate_capacity=inflate_capacity,
        horizon_days=HORIZON_DAYS, repricing_interval=REPRICING_INTERVAL, decision_day=day,
        published_now=np.zeros(firms.benefit.size, dtype=bool) if published is None else published,
        new_case_fine=new_case_fine,
    )
    return choices, wash_due


def simulate(firms: SandboxFirms, domain: DomainSpec, schedule: PolicySchedule, *, natural_decay: float,
             audit_seed: int, trading_days: int = TRADING_DAYS, window_start: int = SNAPSHOT_DAY) -> dict:
    """Days 1..trading_days from the initial true levels, with no inflation or pending actions.

    The event order per day follows ``DisclosureMarket``: decay and due actions
    first; on decision days the audit (fine on the detected stock, which is
    removed), then the decision. Penalties and costs are recorded as market-cap
    fractions at the fixed snapshot cap; they do not feed back on anything.
    """
    domain = replace(domain, natural_decay=natural_decay)
    n = firms.size_class.size
    state = AttributeState(goodness=firms.initial_goodness.copy(), inflation=np.zeros(n),
                           cost_scale=firms.cost_scale.copy(), ceiling=domain.observation_ceiling)
    rng = Mulberry32(audit_seed)
    decisions = trading_days // DECISION_INTERVAL
    mean_goodness = np.empty(trading_days + 1)
    mean_inflation = np.empty(trading_days + 1)
    mean_goodness[0], mean_inflation[0] = state.goodness.mean(), 0.0
    actions = np.full((decisions, n), MAINTAIN, dtype=np.int64)
    amounts = np.zeros((decisions, n))
    detections = np.zeros((decisions, n), dtype=bool)
    resource_cost = np.zeros((decisions, n))
    fines = np.zeros((decisions, n))
    goodness_at = {}
    for day in range(1, trading_days + 1):
        state.advance(day, domain)
        if day % DECISION_INTERVAL == 0:
            period = day // DECISION_INTERVAL - 1
            regime = schedule.at(day)
            selected = rng.uniforms(n) < regime.audit_probability
            caught = selected & (state.inflation > 0)
            fines[period] = np.where(caught, regime.penalty * state.inflation + regime.fixed_fine / firms.market_cap, 0.0)
            state.inflation[caught] = 0.0
            choices, wash_due = decide(state, firms, domain, regime, day, selected & regime.publish_audit_results)
            improve = np.flatnonzero(choices.actions == IMPROVE)
            inflate = np.flatnonzero(choices.actions == INFLATE)
            state.schedule(day + max(1, domain.implementation_delay_days), IMPROVE, improve, choices.amounts[improve])
            state.schedule(wash_due, INFLATE, inflate, choices.amounts[inflate])
            actions[period], amounts[period] = choices.actions, choices.amounts
            detections[period], resource_cost[period] = caught, choices.cost_fraction
        mean_goodness[day], mean_inflation[day] = state.goodness.mean(), state.inflation.mean()
        if day in (window_start, trading_days):
            goodness_at[day] = state.goodness.copy()
    return {
        "decision_days": (np.arange(decisions) + 1) * DECISION_INTERVAL, "actions": actions, "amounts": amounts,
        "detections": detections, "resource_cost_fraction": resource_cost, "fine_fraction": fines,
        "mean_goodness": mean_goodness, "mean_inflation": mean_inflation, "goodness_at": goodness_at,
        "final_goodness": state.goodness.copy(), "final_inflation": state.inflation.copy(),
    }


def window_metrics(run: dict, firms: SandboxFirms, *, start_day: int = SNAPSHOT_DAY, end_day: int = TRADING_DAYS) -> dict:
    """Stage F's window metrics for one simplified run (days start..end, decisions in (start, end])."""
    change = run["goodness_at"][end_day] - run["goodness_at"][start_day]
    selected = (run["decision_days"] > start_day) & (run["decision_days"] <= end_day)
    washing = run["actions"][selected] == INFLATE
    large, small = firms.size_class == 0, firms.size_class == 2
    money = run["resource_cost_fraction"][selected] * firms.market_cap
    return {
        "true_change_sd": float(change.mean()),
        "inflation_mean_sd": float(run["mean_inflation"][start_day:end_day + 1].mean()),
        "wash_share": float(washing.mean()),
        "wash_share_by_size": {name: float(washing[:, firms.size_class == index].mean())
                               for index, name in enumerate(SIZE_CLASS_NAMES)},
        "large_minus_small_sd": float(change[large].mean() - change[small].mean()),
        "resource_cost_fraction_initial_cap": float(money.sum() / firms.market_cap.sum()),
    }


# -- shared loaders for fixtures and tests -------------------------------------------

def regime_from(payload: dict) -> PolicyRegime:
    return PolicyRegime(**payload)


def schedule_from(payload: dict) -> PolicySchedule:
    intervention = payload.get("intervention")
    return PolicySchedule(regime_from(payload["baseline"]), regime_from(intervention) if intervention else None,
                          payload.get("start_day", 0))


def firms_from(payload: dict) -> SandboxFirms:
    return SandboxFirms(
        size_class=np.asarray(payload["size_class"], dtype=np.int64),
        initial_goodness=np.asarray(payload["initial_goodness"], dtype=np.float64),
        cost_scale=np.asarray(payload["cost_scale"], dtype=np.float64),
        market_cap=np.asarray(payload["market_cap"], dtype=np.float64),
        benefit=np.asarray(payload["benefit"], dtype=np.float64),
    )


def snapshot_state(payload: dict, domain: DomainSpec) -> AttributeState:
    """The post-audit state the full model's firms decided on at the snapshot day."""
    return AttributeState(
        goodness=np.asarray(payload["goodness"], dtype=np.float64),
        inflation=np.asarray(payload["inflation"], dtype=np.float64),
        cost_scale=np.asarray(payload["cost_scale"], dtype=np.float64),
        pending=[(item["due_day"], item["kind"], np.asarray(item["firms"], dtype=np.int64),
                  np.asarray(item["amounts"], dtype=np.float64)) for item in payload["pending"]],
        ceiling=domain.observation_ceiling,
    )


DOMAIN_FILES = {"esg": "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json",
                "ai_washing": "configs/domains/ai_washing.json"}


def load_domains(root: str | Path) -> dict[str, DomainSpec]:
    return {key: load_domain(Path(root) / path) for key, path in DOMAIN_FILES.items()}
