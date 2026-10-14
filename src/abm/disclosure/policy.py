"""Regulatory regime and its schedule.

Instruments act through distinct channels:

* ``audit_probability`` – chance per decision period that a firm's report is
  checked; a detected inflation is removed and fined;
* ``penalty`` – fine per standard deviation of detected inflation, as a
  fraction of market cap;
* ``fixed_fine`` – a lump-sum fine per detected case in model money units
  (mean initial firm value = 1), whatever the amount inflated. One audit
  that finds inflation closes one case, so inflation added to a report that
  is already inflated and undetected adds no fixed fine;
* ``transparency`` – weight investors put on the true attribute rather than
  the report (``signal = true + (1 - transparency) * inflation``);
* ``subsidy`` – payment per standard deviation of real improvement, as a
  fraction of market cap;
* disclosure error and delay, and dated audit publications, affect the
  public signal separately from the audit and fine instruments.

In this model, reports follow a global publication calendar. Each checked
firm also updates its ordinary report at close, separately from certification.

Audit probability also determines how long inflated reports survive, so
equal probability-times-penalty does not hold either their value or the
discounted fine constant. A transparency comparison keeps audit probability,
penalty and subsidy individually fixed.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from math import isfinite
from typing import Any

from .domain import DomainSpec


@dataclass(frozen=True, slots=True)
class PolicyRegime:
    audit_probability: float
    penalty: float
    transparency: float
    subsidy: float
    disclosure_noise_sd: float = 0.0
    disclosure_delay_days: int | None = None
    publish_audit_results: bool = False
    reporting_interval_days: int = 1
    fixed_fine: float = 0.0

    def __post_init__(self) -> None:
        if not 0 <= self.audit_probability <= 1 or not 0 <= self.transparency <= 1:
            raise ValueError("audit_probability and transparency must be in [0, 1]")
        if self.penalty < 0 or self.subsidy < 0:
            raise ValueError("penalty and subsidy must be nonnegative")
        if not isfinite(self.fixed_fine) or self.fixed_fine < 0:
            raise ValueError("fixed_fine must be finite and nonnegative")
        if not isfinite(self.disclosure_noise_sd) or self.disclosure_noise_sd < 0:
            raise ValueError("disclosure_noise_sd must be finite and nonnegative")
        if self.disclosure_delay_days is not None and (
            type(self.disclosure_delay_days) is not int or self.disclosure_delay_days < 0
        ):
            raise ValueError("disclosure_delay_days must be a nonnegative integer or None")
        if type(self.publish_audit_results) is not bool:
            raise ValueError("publish_audit_results must be boolean")
        if type(self.reporting_interval_days) is not int or self.reporting_interval_days < 1:
            raise ValueError("reporting_interval_days must be a positive integer")

    @classmethod
    def baseline(cls, domain: DomainSpec) -> "PolicyRegime":
        return cls(
            audit_probability=domain.baseline_audit_probability,
            penalty=domain.baseline_penalty,
            transparency=domain.baseline_transparency,
            subsidy=domain.baseline_subsidy,
            fixed_fine=domain.baseline_fixed_fine,
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialized regime; a zero fixed fine is omitted so earlier identities are unchanged."""
        payload = asdict(self)
        if not self.fixed_fine:
            payload.pop("fixed_fine")
        return payload


@dataclass(frozen=True, slots=True)
class PolicySchedule:
    """A baseline regime and one optional switch at ``start_day``."""

    baseline: PolicyRegime
    intervention: PolicyRegime | None = None
    start_day: int = 0

    def __post_init__(self) -> None:
        if self.start_day < 0:
            raise ValueError("start_day must be nonnegative")

    def at(self, day: int) -> PolicyRegime:
        if self.intervention is not None and day >= self.start_day:
            return self.intervention
        return self.baseline

    def to_dict(self) -> dict[str, Any]:
        return {"baseline": self.baseline.to_dict(),
                "intervention": None if self.intervention is None else self.intervention.to_dict(),
                "start_day": self.start_day}

    @classmethod
    def constant(cls, domain: DomainSpec) -> "PolicySchedule":
        return cls(baseline=PolicyRegime.baseline(domain))

    def with_intervention(self, start_day: int, **changes: float | bool | None) -> "PolicySchedule":
        return replace(self, intervention=replace(self.baseline, **changes), start_day=start_day)

    def with_information_intervention(
        self, start_day: int, *, transparency: float | None = None,
        disclosure_noise_sd: float | None = None, disclosure_delay_days: int | None = None,
        publish_audit_results: bool | None = None,
        reporting_interval_days: int | None = None,
    ) -> "PolicySchedule":
        """Change information instruments, retaining audit, fine and subsidy."""
        changes = {name: value for name, value in {
            "transparency": transparency, "disclosure_noise_sd": disclosure_noise_sd,
            "disclosure_delay_days": disclosure_delay_days, "publish_audit_results": publish_audit_results,
            "reporting_interval_days": reporting_interval_days,
        }.items() if value is not None}
        return self.with_intervention(start_day, **changes)
