"""Reproduce corrected development paths from their archived source package."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import zipfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


root = Path(__file__).resolve().parents[2]
experiment = root / "reports/disclosure_financing_development_20261011_v2"
phase_archive = root / "reports/disclosure_phase_development_20261011_v2"
first = experiment / "market_B/seed_23001/attempt_001"
manifest = json.loads((first / "manifest.json").read_text(encoding="utf-8"))
assert digest(first / "source.zip") == manifest["artifacts"]["source.zip"]
with tempfile.TemporaryDirectory(prefix="abm-disclosure-reproduce-") as temporary:
    temporary = Path(temporary).resolve()
    source = temporary / "source"
    with zipfile.ZipFile(first / "source.zip") as archive:
        assert set(archive.namelist()) == set(manifest["source_hashes"])
        for name, expected in manifest["source_hashes"].items():
            target = (source / name).resolve()
            target.relative_to(source.resolve())
            content = archive.read(name)
            assert hashlib.sha256(content).hexdigest() == expected
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    sys.path.insert(0, str(source))
    from abm.disclosure.config import MarketConfig
    from abm.disclosure.domain import DomainSpec
    from abm.disclosure.game import DisclosureMarket
    from abm.disclosure.policy import PolicyRegime, PolicySchedule
    from abm.disclosure.runner import load_result, render_run
    from abm.disclosure import phase

    checks = []
    for seed in (23001, 23002):
        trial = experiment / f"market_B/seed_{seed}/attempt_001"
        entry = json.loads((trial / "manifest.json").read_text(encoding="utf-8"))
        assert entry["source_hashes"] == manifest["source_hashes"]
        for name, expected in entry["artifacts"].items():
            assert digest(trial / name) == expected
        policy = entry["policy"]
        schedule = PolicySchedule(
            PolicyRegime(**policy["baseline"]),
            None if policy["intervention"] is None else PolicyRegime(**policy["intervention"]),
            policy["start_day"],
        )
        result = DisclosureMarket(MarketConfig(**entry["config"]), DomainSpec(**entry["domain"]), schedule).run()
        assert result.fingerprint() == entry["result_fingerprint"]
        assert load_result(trial / "result.npz").fingerprint() == result.fingerprint()
        checks.append({"seed": seed, "fingerprint": result.fingerprint(), "serial_matches_archived_parallel": True,
                       "archived_validation": json.loads((trial / "validation.json").read_text())["mechanical"]["status"]})

    def forbidden(*args, **kwargs):
        raise AssertionError("render-only attempted simulation or classification")

    DisclosureMarket.run = forbidden
    phase.analyze_phase = forbidden
    run_copy = temporary / "single"
    run_copy.mkdir()
    for name in ("manifest.json", *manifest["artifacts"]):
        shutil.copyfile(first / name, run_copy / name)
    render_run(run_copy)
    assert digest(run_copy / "report.md") == digest(first / "report.md")
    phase_manifest = json.loads((phase_archive / "phase_manifest.json").read_text(encoding="utf-8"))
    phase_copy = temporary / "phase"
    for name in ("phase_manifest.json", "phase_analysis.json", *phase_manifest["inputs_sha256"]):
        target = (phase_copy / name).resolve()
        target.relative_to(phase_copy.resolve())
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(phase_archive / name, target)
    phase.render_phase(phase_copy)
    assert digest(phase_copy / "phase_report.md") == digest(phase_archive / "phase_report.md")
    assert digest(phase_copy / "phase_analysis.json") == phase_manifest["analysis_sha256"]
    for name in ("phase_G.png", "phase_W.png"):
        assert digest(phase_copy / name) == digest(phase_archive / name)
    report = {
        "status": "PASS", "scope": "Reproducibility only; original market failures remain failures.",
        "trials": checks, "single_run_render_guard": "PASS", "phase_render_guard": "PASS",
        "phase_report_and_png_identical": True, "original_inputs_unchanged": True,
        "experiment_sha256": digest(experiment / "experiment.json"),
        "phase_manifest_sha256": digest(phase_archive / "phase_manifest.json"),
        "script_sha256": digest(Path(__file__)),
    }
    for name, expected in manifest["artifacts"].items():
        assert digest(first / name) == expected
    for name, expected in phase_manifest["inputs_sha256"].items():
        assert digest(phase_archive / name) == expected
    (experiment / "reproducibility.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))
