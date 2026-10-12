import hashlib
import json
import zipfile

import pytest

from abm.disclosure import runner
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain


@pytest.fixture
def archived_run(tmp_path):
    config = MarketConfig(n_investors=30, n_firms=6, trading_days=450, burn_in_days=50,
                          initial_impact_share=0.2)
    output = tmp_path / "run"
    manifest = runner.run_and_archive(config, load_domain("configs/domains/esg.json"), output)
    return output, manifest


def test_archive_round_trip_and_source_hashes(archived_run):
    output, manifest = archived_run
    assert manifest["status"] == "complete"
    assert runner.load_result(output / "result.npz").fingerprint() == manifest["result_fingerprint"]
    with zipfile.ZipFile(output / "source.zip") as archive:
        assert set(archive.namelist()) == set(manifest["source_hashes"])
        for name, digest in manifest["source_hashes"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
    validation = json.loads((output / "validation.json").read_text())
    assert validation["mechanical"]["checks"]["cash_conservation"]
    assert validation["mechanical"]["checks"]["share_conservation"]
    assert validation["mechanical"]["price_cap_hits"] == int(
        runner.load_result(output / "result.npz").market.price_cap_hits.sum()
    )
    assert validation["empirical_calibration"]["status"] == "pending"


def test_render_only_never_simulates(archived_run, monkeypatch):
    output, _ = archived_run
    expected = (output / "report.md").read_bytes()
    (output / "report.md").unlink()

    def forbidden(*args, **kwargs):
        pytest.fail("render-only tried to simulate")

    monkeypatch.setattr(runner.DisclosureMarket, "run", forbidden)
    assert runner.main(["--output", str(output), "--render-only"]) == 0
    assert (output / "report.md").read_bytes() == expected


def test_render_rejects_changed_artifact(archived_run):
    output, _ = archived_run
    (output / "metrics.json").write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="archive hash mismatch: metrics.json"):
        runner.render_run(output)


def test_archive_never_overwrites_existing_output(tmp_path):
    sentinel = tmp_path / "sentinel.txt"
    sentinel.write_text("keep", encoding="utf-8")
    with pytest.raises(FileExistsError):
        runner.run_and_archive(MarketConfig(), load_domain("configs/domains/esg.json"), tmp_path)
    assert sentinel.read_text() == "keep"
    assert not (tmp_path / "manifest.json").exists()


def test_failure_records_failed_status(tmp_path, monkeypatch):
    def fail(*args, **kwargs):
        raise RuntimeError("controlled simulation failure")

    monkeypatch.setattr(runner.DisclosureMarket, "run", fail)
    output = tmp_path / "failed"
    with pytest.raises(RuntimeError, match="controlled simulation failure"):
        runner.run_and_archive(MarketConfig(), load_domain("configs/domains/esg.json"), output)
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["status"] == "failed"
    assert manifest["error_type"] == "RuntimeError"
    assert not (output / "result.npz").exists()


def test_report_failure_preserves_completed_simulation(tmp_path, monkeypatch):
    def fail(*args, **kwargs):
        raise OSError("report locked")

    monkeypatch.setattr(runner, "render_run", fail)
    output = tmp_path / "report_failure"
    config = MarketConfig(n_firms=6, n_investors=20, trading_days=40, burn_in_days=0)
    with pytest.raises(OSError, match="report locked"):
        runner.run_and_archive(config, load_domain("configs/domains/esg.json"), output)
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["status"] == "complete"
    assert runner.load_result(output / "result.npz").fingerprint() == manifest["result_fingerprint"]
