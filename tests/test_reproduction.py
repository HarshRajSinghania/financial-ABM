"""Archived Stage 3 reconstruction and failed-run provenance."""

import json
import queue
from dataclasses import replace
from pathlib import Path

import pytest

from abm.reproduction import rebuild_run, record_run_failure
from abm.stage2 import load_simulation_config
from abm.stage3 import Stage3Config, Stage3Harness

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def archived_run(tmp_path, monkeypatch):
    monkeypatch.setattr("abm.visualization.create_stage1_visualizations", lambda *args: None)
    events = tmp_path / "events.json"
    events.write_text(json.dumps({"events": [{
        "factor_id": "filing-1", "event_time": "2026-01-05T22:00:00+00:00",
        "available_at": "2026-01-05T22:00:00+00:00", "source": "https://www.sec.gov/example",
        "targets": ["company-0"], "channel": "information", "true_value": {"log_change": 0.01},
        "observed_message": "Synthetic filing fixture", "uncertainty": 0.0, "persistence": 1,
    }]}), encoding="utf-8")
    payload = load_simulation_config(ROOT / "configs/stage2_five_nodes.json").to_dict()
    payload.update(stage3_enabled=True, factors_enabled=True, factor_events_path=str(events),
                   start_date="2026-01-05", session_cutoff="21:00:00+00:00", graph_fixture="",
                   population_size=4, company_count=1, trading_days=4)
    config = Stage3Config.from_dict(payload)
    result = Stage3Harness(config, code_revision="rebuild-test").run()
    output = tmp_path / "original"
    result.write(output, config, code_revision="rebuild-test")
    return output, events, config, result


def test_rebuild_uses_archived_inputs_when_original_is_missing(archived_run, tmp_path):
    original, events, _, expected = archived_run
    events.unlink()
    rebuilt = rebuild_run(original, tmp_path / "rebuilt")
    assert rebuilt.fingerprint() == expected.fingerprint()
    assert rebuilt.telemetry_events == expected.telemetry_events
    manifest = json.loads((tmp_path / "rebuilt/run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["started_at"] and manifest["ended_at"]
    assert manifest["failures"] == []


@pytest.mark.parametrize("target", ["data", "source", "config", "identity"])
def test_rebuild_rejects_tampered_archive(archived_run, tmp_path, target):
    original, _, _, _ = archived_run
    if target in {"data", "source"}:
        archive = json.loads((original / "reproducibility.json").read_text(encoding="utf-8"))
        relative = next(iter(archive[f"{target}_files"].values()))
        path = original / relative
        path.write_bytes(path.read_bytes() + b"\n")
    else:
        path = original / ("config.json" if target == "config" else "run_manifest.json")
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["seed" if target == "config" else "run_id"] = 123 if target == "config" else "invalid"
        path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="mismatch"):
        rebuild_run(original, tmp_path / "rejected")
    assert not (tmp_path / "rejected").exists()


def test_failure_manifest_preserves_identity_and_completed_progress(archived_run, tmp_path):
    _, _, config, _ = archived_run
    harness = Stage3Harness(replace(config, trading_days=2), code_revision="failure-test")
    harness.step(0)
    record_run_failure(harness, harness.config, tmp_path / "failed", RuntimeError("test interruption"))
    manifest = json.loads((tmp_path / "failed/run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["run_id"] == harness.manifest.run_id
    assert manifest["failures"] == ["RuntimeError: test interruption"]
    assert manifest["ended_at"] >= manifest["started_at"]
    assert not (tmp_path / "failed/summary.json").exists()


def test_rejected_rebuild_does_not_leave_a_journal(archived_run, tmp_path, monkeypatch):
    original, _, _, _ = archived_run
    extra = tmp_path / "new_source.py"
    extra.write_text("", encoding="utf-8")
    source_files = Stage3Harness._manifest_data_files
    monkeypatch.setattr(Stage3Harness, "_manifest_data_files",
                        lambda self: {**source_files(self), "source:new_source.py": extra})
    for _ in range(2):
        with pytest.raises(ValueError, match="identity mismatch"):
            rebuild_run(original, tmp_path / "rejected")
    assert not (tmp_path / ".rejected.events.jsonl").exists()
    assert not (tmp_path / "rejected").exists()


def test_live_failure_is_delivered_when_failure_archive_cannot_be_written(archived_run, tmp_path, monkeypatch):
    from abm.run_service import controlled_run_worker

    _, _, config, _ = archived_run
    original_step = Stage3Harness.step

    def fail_second_day(self, index):
        if index == 1:
            raise RuntimeError("simulation interrupted")
        return original_step(self, index)

    def fail_archive(*args):
        raise OSError("archive unavailable")

    monkeypatch.setattr(Stage3Harness, "step", fail_second_day)
    monkeypatch.setattr("abm.reproduction.record_run_failure", fail_archive)
    completion = queue.Queue()
    controlled_run_worker(config.to_dict(), str(tmp_path / "failed-live"),
                          queue.Queue(), queue.Queue(), completion)
    status = completion.get_nowait()
    assert status["state"] == "failed"
    assert status["current_day"] == 1
    assert "simulation interrupted" in status["error"]
    assert "archive unavailable" in status["error"]
