from copy import deepcopy

import pytest

from abm.disclosure.report import render_charts


def test_charts_render_archived_estimates_and_preserve_inputs(tmp_path):
    pytest.importorskip("matplotlib")
    frozen = {"spec": {"purpose": "development", "analysis": {"confidence_level": .95}}}
    summary = {
        "purpose": "development", "status": "incomplete", "claim_support": "pending",
        "trials_failing_core_validation": 1,
        "comparisons": [
            {"name": "information_minus_baseline", "metrics": {
                "true_change.equal_weight_sd": {
                    "status": "complete", "mean": .2, "ci_low": -.1, "ci_high": .5, "n": 3,
                },
            }},
            {"name": "penalty_minus_baseline", "metrics": {
                "true_change.equal_weight_sd": {"status": "incomplete", "n_available": 1, "n_planned": 3},
            }},
        ],
        "scenarios": [
            {"name": "baseline", "metrics": {
                "true_change.equal_weight_sd": {"status": "complete", "mean": -.1, "n": 3},
                "costs.resource_cost_fraction_initial_cap": {"status": "complete", "mean": .02, "n": 3},
                "size.large_minus_small_sd": {
                    "status": "complete", "mean": -.2, "ci_low": -.3, "ci_high": -.1, "n": 3,
                },
            }},
            {"name": "information", "metrics": {
                "true_change.equal_weight_sd": {"status": "complete", "mean": .1, "n": 1},
                "costs.resource_cost_fraction_initial_cap": {"status": "complete", "mean": .03, "n": 1},
                "size.large_minus_small_sd": {"status": "complete", "mean": .05, "n": 1},
            }},
            {"name": "penalty", "metrics": {
                "true_change.equal_weight_sd": {"status": "incomplete", "n_available": 1, "n_planned": 3},
                "costs.resource_cost_fraction_initial_cap": {"status": "incomplete", "n_available": 1, "n_planned": 3},
                "size.large_minus_small_sd": {"status": "incomplete", "n_available": 1, "n_planned": 3},
            }},
        ],
    }
    original = deepcopy((frozen, summary))
    paths = render_charts(tmp_path / "figures", frozen, summary)
    assert len(paths) == len(set(paths)) == 6
    assert {path.rsplit(".", 1)[1] for path in paths} == {"png", "pdf"}
    for path in paths:
        content = (tmp_path / "figures" / path).read_bytes()
        assert len(content) > 1000
        assert content.startswith(b"\x89PNG\r\n\x1a\n" if path.endswith(".png") else b"%PDF-")
    assert (frozen, summary) == original
