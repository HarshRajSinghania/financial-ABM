import json
from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest

from abm.disclosure import MarketConfig
from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.game import MAINTAIN, run_disclosure
from abm.disclosure.runner import load_result, render_run, run_and_archive


DOMAIN_PATH = Path("configs/domains/ai_washing.json")


def test_ai_washing_domain_loads_with_explicit_exploratory_provenance():
    payload = json.loads(DOMAIN_PATH.read_text(encoding="utf-8"))
    domain = load_domain(DOMAIN_PATH)
    assert domain.name == "ai_washing"
    assert domain.goodness_bounds == pytest.approx((-2.0, 3.0))
    assert domain.to_goodness(np.array([0.6]))[0] == pytest.approx(1.0)
    assert domain.size_cost_multipliers == (1.0, 1.0, 1.0)
    assert domain.label("wash") == "夸大AI披露"
    assert DomainSpec.from_dict(domain.to_dict()) == domain
    assert "exploratory" in payload["_note"].lower()
    assert "uncalibrated" in payload["_note"].lower()
    assert payload["_sources"] == [
        "https://www.sec.gov/newsroom/press-releases/2024-36",
        "https://www.sec.gov/newsroom/speeches-statements/sec-chair-gary-gensler-ai-washing",
    ]


def test_ai_washing_runs_through_archive_metrics_validation_and_rendering(tmp_path):
    domain = load_domain(DOMAIN_PATH)
    config = MarketConfig(
        n_firms=9, n_investors=24, trading_days=240, burn_in_days=60,
        initial_impact_share=0.6,
    )
    destination = tmp_path / "ai_run"
    manifest = run_and_archive(config, domain, destination, purpose="generality_smoke")
    assert manifest["status"] == "complete"
    assert manifest["domain"] == domain.to_dict()
    result = load_result(destination / "result.npz")
    assert result.fingerprint() == manifest["result_fingerprint"]
    assert result.true_goodness.shape == (241, 9)
    assert np.any(result.actions != MAINTAIN)
    raw_true = domain.to_raw(result.true_goodness)
    raw_report = domain.to_raw(result.true_goodness + result.inflation)
    assert np.all((raw_true >= domain.raw_lower) & (raw_true <= domain.raw_upper))
    assert np.all((raw_report >= domain.raw_lower) & (raw_report <= domain.raw_upper))
    metrics = json.loads((destination / "metrics.json").read_text(encoding="utf-8"))
    assert metrics["diagnostics"]["finite_metrics"]
    assert metrics["true_change"]["equal_weight_raw"] == pytest.approx(
        domain.initial_sd * metrics["true_change"]["equal_weight_sd"]
    )
    validation = json.loads((destination / "validation.json").read_text(encoding="utf-8"))
    assert validation["mechanical"]["checks"]["cash_conservation"]
    assert validation["mechanical"]["checks"]["share_conservation"]
    assert validation["empirical_calibration"]["status"] == "pending"
    report = (destination / "report.md").read_bytes()
    assert b"ai_washing" in report
    assert render_run(destination).read_bytes() == report


def test_domain_labels_do_not_change_the_market_mechanism():
    domain = load_domain(DOMAIN_PATH)
    renamed = replace(
        domain, name="alternative_domain", attribute_label="Alternative attribute",
        unit="alternative index", action_labels={"improve": "Build", "wash": "Overstate", "maintain": "Hold"},
    )
    config = MarketConfig(n_firms=6, n_investors=16, trading_days=80, burn_in_days=20, initial_impact_share=0.6)
    assert run_disclosure(config, domain).fingerprint() == run_disclosure(config, renamed).fingerprint()
