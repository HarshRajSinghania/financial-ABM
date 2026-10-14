"""Compact run archives (stage F): same fingerprint and metrics as a full archive, smaller result.npz."""

import json
from pathlib import Path

import numpy as np
import pytest

from abm.disclosure import experiments, runner
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain


def _config():
    return MarketConfig(n_investors=24, n_firms=6, trading_days=200, burn_in_days=50, initial_impact_share=.2)


def test_compact_archive_keeps_fingerprint_metrics_and_render(tmp_path):
    domain = load_domain("configs/domains/esg.json")
    full = runner.run_and_archive(_config(), domain, tmp_path / "full")
    compact = runner.run_and_archive(_config(), domain, tmp_path / "compact", archive="compact")
    assert compact["result_fingerprint"] == full["result_fingerprint"]
    assert compact["run_id"] == full["run_id"]
    assert compact["compact_archive"]["omitted_result_arrays"] == list(runner.COMPACT_OMITTED)
    assert "compact_archive" not in full
    for name in ("metrics.json", "validation.json"):
        assert (tmp_path / "full" / name).read_bytes() == (tmp_path / "compact" / name).read_bytes()
    with np.load(tmp_path / "compact" / "result.npz") as kept, np.load(tmp_path / "full" / "result.npz") as every:
        assert set(every.files) - set(kept.files) == set(runner.COMPACT_OMITTED)
        for name in kept.files:
            np.testing.assert_array_equal(kept[name], every[name])
    runner.render_run(tmp_path / "compact")
    with pytest.raises(KeyError):
        runner.load_result(tmp_path / "compact" / "result.npz")


def test_unknown_archive_modes_are_rejected(tmp_path):
    with pytest.raises(ValueError, match="archive"):
        runner.run_and_archive(_config(), load_domain("configs/domains/esg.json"), tmp_path / "x", archive="tiny")
    with pytest.raises(ValueError, match="omit"):
        runner.save_result(tmp_path / "r.npz", _tiny_result(), omit=("nonexistent",))


def _tiny_result():
    from abm.disclosure.game import DisclosureMarket
    return DisclosureMarket(MarketConfig(n_investors=12, n_firms=3, trading_days=70, burn_in_days=10,
                                         initial_impact_share=.2), load_domain("configs/domains/esg.json")).run()


def _spec(tmp_path, archive):
    payload = {
        "name": "compact-test", "purpose": "development", "archive": archive,
        "domain": str(Path("configs/domains/esg.json").resolve()),
        "market": {"n_investors": 24, "n_firms": 6, "trading_days": 200, "burn_in_days": 50,
                   "initial_impact_share": 0.2},
        "seeds": [101, 102],
        "scenarios": [{"name": "base"}, {"name": "info", "policy": {"start_day": 51, "changes": {"transparency": 0.6}}}],
        "comparisons": [{"name": "info_minus_base", "weights": {"info": 1, "base": -1}, "primary": True}],
        "analysis": {"primary_metric": "true_change.equal_weight_sd",
                     "metrics": ["true_change.equal_weight_sd"], "confidence_level": 0.95},
    }
    path = tmp_path / f"spec_{archive}.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_compact_experiment_matches_full_experiment_and_resumes(tmp_path):
    full = experiments.run_experiment(_spec(tmp_path, "full"), tmp_path / "full", workers=1)
    compact = experiments.run_experiment(_spec(tmp_path, "compact"), tmp_path / "compact", workers=1)
    summaries = [json.loads((path.parent / "summary.json").read_text(encoding="utf-8")) for path in (full, compact)]
    assert [row["result_fingerprint"] for row in summaries[0]["records"]] == [
        row["result_fingerprint"] for row in summaries[1]["records"]]
    assert summaries[0]["comparisons"][0]["metrics"] == summaries[1]["comparisons"][0]["metrics"]
    experiments.run_experiment(_spec(tmp_path, "compact"), tmp_path / "compact", workers=1, resume=True)
    assert len(list((tmp_path / "compact" / "base" / "seed_101").glob("attempt_*"))) == 1


def test_spec_rejects_unknown_archive_mode(tmp_path):
    with pytest.raises(ValueError, match="archive"):
        experiments.freeze_spec(_spec(tmp_path, "tiny"))
