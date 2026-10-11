"""Session-cutoff factors, independent switches, and archived run inputs."""

import json
from dataclasses import fields, replace
from datetime import datetime
from pathlib import Path

import numpy as np
import pytest

from abm.manifest import sha256_file
from abm.schemas import FactorEvent
from abm.stage2 import Stage2Config, create_market_harness, simulation_config_from_dict
from abm.stage3 import SnapshotInformationPlugin, Stage3Config, Stage3Harness

ROOT = Path(__file__).resolve().parents[1]


def _config(**changes):
    base = Stage2Config.from_dict(json.loads((ROOT / "configs/stage2_five_nodes.json").read_text(encoding="utf-8")))
    values = {field.name: getattr(base, field.name) for field in fields(Stage2Config)}
    values.update(graph_fixture="", trading_days=5, bandit_enabled=False,
                  company_learning_enabled=False, factors_enabled=False, start_date="2024-01-05")
    values.update(changes)
    return Stage3Config(**values)


def _event(at="2024-01-05T21:00:01+00:00", **changes):
    instant = datetime.fromisoformat(at)
    values = dict(factor_id="sec-8k-one", event_time=instant, available_at=instant,
                  source="https://www.sec.gov/Archives/edgar/data/example/8-k.htm",
                  targets=("company-0",), channel="information", true_value={"log_change": .02},
                  observed_message="8-K filing; magnitude is a disclosed scenario parameter.",
                  uncertainty=0.0, persistence=1)
    values.update(changes)
    return FactorEvent(**values)


def _snapshot(tmp_path, events):
    path = tmp_path / "factor_events.json"
    path.write_text(json.dumps({"events": [event.to_dict() for event in events]}), encoding="utf-8")
    return str(path)


def test_config_round_trip_and_explicit_session_offsets():
    config = _config(trading_days=2, session_dates=("2024-03-08T21:00:00+00:00", "2024-03-11T20:00:00+00:00"))
    assert simulation_config_from_dict(config.to_dict()) == config
    result = create_market_harness(config).run()
    assert result.stage3_audit["session_cutoffs"] == list(config.session_dates)
    assert result.stage3_audit["calendar"] == "explicit_sessions"
    with pytest.raises(ValueError, match="UTC offset"):
        _config(session_cutoff="21:00:00")
    with pytest.raises(ValueError, match="timezone-aware"):
        _config(trading_days=1, session_dates=("2024-01-05T21:00:00",))
    with pytest.raises(TypeError, match="array of strings"):
        Stage3Config.from_dict({**config.to_dict(), "session_dates": "2024-03-08"})


@pytest.mark.parametrize("learning", [False, True])
def test_disabled_stage3_exactly_recovers_stage2(learning):
    config = _config(stage3_enabled=False, bandit_enabled=learning, company_learning_enabled=learning)
    expected = create_market_harness(config.stage2_config()).run()
    actual = create_market_harness(config).run()
    assert actual.fingerprint() == expected.fingerprint()
    assert actual.telemetry_events == expected.telemetry_events


def test_after_close_filing_waits_for_next_session_and_propagates(tmp_path):
    config = _config(factors_enabled=True, factor_events_path=_snapshot(tmp_path, [_event()]))
    first = create_market_harness(config).run()
    second = create_market_harness(config).run()
    assert first.fingerprint() == second.fingerprint()
    frames = [json.loads(event.payload["stage2_json"]) for event in first.telemetry_events]
    assert frames[0]["session_cutoff"] == "2024-01-05T21:00:00+00:00"
    assert frames[1]["session_cutoff"] == "2024-01-08T21:00:00+00:00"
    assert frames[0]["factor_events"] == []
    assert frames[1]["factor_events"][0]["available_at"] == "2024-01-05T21:00:01+00:00"
    factor_messages = [m for m in frames[1]["messages"] if m["content_type"] == "factor_information"]
    assert len(factor_messages) == 1
    assert factor_messages[0]["available_at"] == frames[1]["session_cutoff"]
    assert factor_messages[0]["payload"]["source_available_at"] == "2024-01-05T21:00:01+00:00"
    arrivals = [d for frame in frames for d in frame["arrivals"] if d["content_type"] == "factor_information"]
    assert {d["target_id"] for d in arrivals} == {"trader-0", "trader-1", "trader-2", "trader-3"}
    assert all(d["path"][0] == "company-0" for d in arrivals)
    for frame in frames:
        cutoff = datetime.fromisoformat(frame["session_cutoff"])
        assert all(datetime.fromisoformat(delivery["available_at"]) <= cutoff for delivery in frame["arrivals"])


def test_future_factor_has_no_market_effect_before_available_cutoff(tmp_path):
    event = _event("2024-01-09T21:00:01+00:00")
    config = _config(factors_enabled=True, factor_events_path=_snapshot(tmp_path, [event]))
    enabled, disabled = create_market_harness(config).run(), create_market_harness(replace(config, factors_enabled=False)).run()
    np.testing.assert_array_equal(enabled.prices[:4], disabled.prices[:4])
    for actual, baseline in zip(enabled.telemetry_events[:3], disabled.telemetry_events[:3], strict=True):
        assert actual.payload == baseline.payload
    assert not np.array_equal(enabled.prices[4:], disabled.prices[4:])
    assert enabled.stage3_audit["emitted_events"] == 1


def test_factor_off_restores_empty_factor_market_on_same_calendar(tmp_path):
    config = _config(factors_enabled=True, factor_events_path=_snapshot(tmp_path, []))
    enabled, disabled = create_market_harness(config).run(), create_market_harness(replace(config, factors_enabled=False)).run()
    np.testing.assert_array_equal(enabled.prices, disabled.prices)
    assert [e.payload for e in enabled.telemetry_events] == [e.payload for e in disabled.telemetry_events]
    assert enabled.stage2_manifest.enabled_plugins == ("snapshot_information_v1",)
    assert disabled.stage2_manifest.enabled_plugins == ()


def test_stage2_master_switch_disables_learners_and_graph_in_stage3():
    config = _config(stage2_enabled=False, bandit_enabled=True, company_learning_enabled=True)
    assert not config.bandit_enabled and not config.company_learning_enabled and not config.graph_enabled
    result = Stage3Harness(config).run()
    assert result.stage2_manifest.agent_models == {"traders": "fixed_rules", "companies": "fixed_maintain"}
    assert all(json.loads(event.payload["stage2_json"])["arrivals"] == [] for event in result.telemetry_events)


def test_rules_switch_suppresses_trades_while_learning_and_messages_continue(tmp_path):
    config = _config(trading_days=60, rules_enabled=False, bandit_enabled=True,
                     company_learning_enabled=True, factors_enabled=True,
                     factor_events_path=_snapshot(tmp_path, [_event()]))
    result = Stage3Harness(config).run()
    assert np.all(result.volumes == 0) and np.all(result.submitted_net_demand == 0)
    assert result.stage2_audit["trader_reward_windows"] == 3
    assert result.stage2_audit["company_reward_windows"] == 1
    frames = [json.loads(event.payload["stage2_json"]) for event in result.telemetry_events]
    assert all(all(order == 0 for order in frame["submitted_orders"]) for frame in frames)
    assert any(frame["arrivals"] for frame in frames)
    assert result.stage3_audit["emitted_events"] == 1


@pytest.mark.parametrize("bandit,company", [(False, False), (True, False), (False, True), (True, True)])
def test_graph_and_each_learner_switch_work_independently(bandit, company):
    result = create_market_harness(_config(trading_days=60, bandit_enabled=bandit,
                                         company_learning_enabled=company)).run()
    assert sum(sum(sum(row) for row in group) for group in result.stage2_audit["bandit_counts"]) == (12 if bandit else 0)
    assert sum(sum(sum(row) for row in group) for group in result.stage2_audit["q_counts"]) == (1 if company else 0)
    frames = [json.loads(event.payload["stage2_json"]) for event in result.telemetry_events]
    assert any(frame["arrivals"] for frame in frames)
    no_graph = create_market_harness(_config(graph_enabled=False, bandit_enabled=bandit,
                                            company_learning_enabled=company)).run()
    assert all(json.loads(event.payload["stage2_json"])["arrivals"] == [] for event in no_graph.telemetry_events)


def test_private_factor_fields_are_research_only(tmp_path):
    path = _snapshot(tmp_path, [_event("2024-01-05T20:00:00+00:00", true_value={"log_change": .01, "private_fundamental": 1e12})])
    harness = Stage3Harness(_config(factors_enabled=True, factor_events_path=path))
    harness.run()
    frame = json.loads(harness.telemetry_events[0].payload["stage2_json"])
    factor = next(message for message in frame["messages"] if message["content_type"] == "factor_information")
    assert "private_fundamental" not in factor["payload"]
    assert not hasattr(harness.policy.last_observation, "fundamental_value")
    assert frame["factor_events"][0]["true_value"]["private_fundamental"] == 1e12


@pytest.mark.parametrize("change,match", [({"channel": "fundamental"}, "information channel"),
                                          ({"true_value": {"log_change": float("nan")}}, "finite"),
                                          ({"event_time": datetime(2024, 1, 5), "available_at": datetime(2024, 1, 5)}, "timezone-aware")])
def test_unsupported_or_unverifiable_factor_fails_closed(tmp_path, change, match):
    path = _snapshot(tmp_path, [_event(**change)])
    with pytest.raises(ValueError, match=match):
        SnapshotInformationPlugin(path)


def test_manifest_archives_rebuild_when_original_inputs_are_gone(tmp_path):
    path = _snapshot(tmp_path, [_event()])
    provenance = tmp_path / "manifest.json"
    provenance.write_text('{"source":"SEC"}', encoding="utf-8")
    config = _config(factors_enabled=True, factor_events_path=path, factor_data_files=(str(provenance),))
    result = Stage3Harness(config, code_revision="test-revision").run()
    output = result.write(tmp_path / "run", config, code_revision="test-revision")
    archive = json.loads((output / "reproducibility.json").read_text(encoding="utf-8"))
    manifest = result.stage2_manifest
    assert manifest.started_at.tzinfo is not None and manifest.ended_at >= manifest.started_at
    assert manifest.enabled_plugins == ("snapshot_information_v1",)
    assert set(archive["source_files"]) | set(archive["data_files"]) == set(manifest.data_sha256)
    for logical, relative in {**archive["source_files"], **archive["data_files"]}.items():
        assert sha256_file(output / relative) == manifest.data_sha256[logical]
    Path(path).unlink()
    provenance.unlink()
    overrides = {archive["original_paths"][logical]: output / relative for logical, relative in archive["data_files"].items()}
    rebuilt = Stage3Harness(config, code_revision="test-revision", data_file_overrides=overrides).run()
    assert rebuilt.fingerprint() == result.fingerprint()
    assert rebuilt.stage2_manifest.run_id == manifest.run_id


def test_stage3_full_queue_drops_display_only_and_replay_matches(tmp_path):
    import queue
    from abm.telemetry import NonBlockingQueueSink, read_telemetry
    config = _config(factors_enabled=True, factor_events_path=_snapshot(tmp_path, [_event()]))
    output = tmp_path / "run"
    journal = tmp_path / ".run.events.jsonl"
    sink = NonBlockingQueueSink(queue.Queue(maxsize=1))
    result = Stage3Harness(config, sink, event_log=journal).run()
    assert sink.dropped_count == config.trading_days - 1
    assert result.fingerprint() == Stage3Harness(config).run().fingerprint()
    assert read_telemetry(output) == result.telemetry_events
    result.write(output, config)
    assert read_telemetry(output) == result.telemetry_events
    persisted = tuple(json.loads(line) for line in (output / "events.jsonl").read_text(encoding="utf-8").splitlines())
    assert persisted == tuple(event.to_dict() for event in result.telemetry_events)


def test_500_rule_agents_finish_252_sessions_without_learning_or_leak(tmp_path):
    config = _config(population_size=500, trading_days=252, company_count=1, seed=621,
                     factors_enabled=True, factor_events_path=_snapshot(tmp_path, [_event()]))
    result = Stage3Harness(config).run()
    assert len(result.daily_audits) == 252
    assert result.summary()["population_size"] == 500
    assert result.summary()["maximum_absolute_cash_error"] < 1e-6
    assert result.summary()["maximum_absolute_share_error"] < 1e-6
    assert np.all(result.prices > 0) and np.all(result.final_agent_cash >= 0)
    assert result.stage3_audit["emitted_events"] == 1
    assert result.stage2_audit["trader_reward_windows"] == result.stage2_audit["company_reward_windows"] == 0


@pytest.mark.parametrize("invalid", ["target", "provenance"])
def test_invalid_inputs_do_not_block_retry_with_an_empty_journal(tmp_path, invalid):
    path = _snapshot(tmp_path, [_event(targets=("company-99",) if invalid == "target" else ("company-0",))])
    provenance = tmp_path / "missing.json"
    config = _config(factors_enabled=True, factor_events_path=path,
                     factor_data_files=(str(provenance),) if invalid == "provenance" else ())
    journal = tmp_path / ".run.events.jsonl"
    for _ in range(2):
        with pytest.raises(ValueError if invalid == "target" else FileNotFoundError):
            Stage3Harness(config, event_log=journal)
    assert not journal.exists()
    if invalid == "target":
        _snapshot(tmp_path, [_event()])
    else:
        provenance.write_text('{}', encoding="utf-8")
    assert len(Stage3Harness(config, event_log=journal).run().daily_audits) == config.trading_days
