from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest

from abm.disclosure import phase
from abm.disclosure.experiments import freeze_spec
from abm.manifest import canonical_json_bytes, sha256_file


SPEC = Path("configs/disclosure_phase_development_v1.json")


def _summary(frozen):
    seeds = frozen["spec"]["seeds"]
    records, scenarios = [], []
    for scenario in frozen["scenarios"]:
        config = scenario["config"]
        for seed in seeds:
            records.append({
                "scenario": scenario["name"], "seed": seed, "status": "complete",
                "validation": {"mechanical": {"status": "PASS"}, "stylized": {"status": "PASS"}},
                "metrics": {
                    "window": {"end_day": config["trading_days"]},
                    "terminal_year": {"start_day": config["trading_days"] - 251, "observations": 252,
                                      "complete_year": True, "change_from_initial_sd": .25,
                                      "inflation_mean_sd": .25},
                },
            })
        scenarios.append({"name": scenario["name"], "metrics": {
            key: {"status": "complete", "mean": mean, "ci_low": .1, "ci_high": .4, "n": len(seeds)}
            for key, mean in ((phase.RULES["G_metric"], .25), (phase.RULES["W_metric"], .25),
                              ("impact.initial_share", .2), ("impact.initial_wealth_share", .3))
        }})
    return {"experiment_id": frozen["experiment_id"], "purpose": frozen["spec"]["purpose"],
            "records": records, "scenarios": scenarios}


@pytest.fixture
def inputs():
    frozen = freeze_spec(SPEC)
    return frozen, _summary(frozen)


def _cutoff(cell, g=.25, w=.25):
    return next(row for row in cell["classifications"] if row["g_threshold"] == g and row["w_threshold"] == w)


def _write_archive(destination, frozen, summary):
    destination.mkdir()
    for name, payload in (("experiment.json", frozen), ("summary.json", summary)):
        (destination / name).write_text(json.dumps(payload, allow_nan=False), encoding="utf-8")
    (destination / "summary_manifest.json").write_text(json.dumps({
        "experiment_id": frozen["experiment_id"], "summary_sha256": sha256_file(destination / "summary.json"),
    }), encoding="utf-8")


def test_development_spec_fixes_full_grid_and_rule_contract(inputs):
    frozen, summary = inputs
    assert frozen["spec"]["phase_analysis"] == phase.RULES
    assert frozen["spec"]["seeds"] == [22001, 22002, 22003]
    assert len(frozen["scenarios"]) == 16
    assert len(summary["records"]) == 48
    config = frozen["scenarios"][0]["config"]
    assert [config[key] for key in ("n_investors", "n_firms", "trading_days", "burn_in_days")] == [150, 30, 1800, 600]
    assert config["taste_log_sd"] == .5
    assert set(phase.RULES["g_thresholds"]) == set(phase.RULES["w_thresholds"]) == {.125, .25, .5}


@pytest.mark.parametrize("g,w,expected", [
    (.25, .25, "mixed"), (.25, .249, "real_improvement"),
    (.249, .25, "inflation_trap"), (.249, .249, "low_change_low_inflation"),
])
def test_seed_classification_includes_threshold_equality(inputs, g, w, expected):
    frozen, summary = inputs
    terminal = summary["records"][0]["metrics"]["terminal_year"]
    terminal.update(change_from_initial_sd=g, inflation_mean_sd=w)
    before = deepcopy((frozen, summary))
    analysis = phase.analyze_phase(frozen, summary)
    assert (frozen, summary) == before
    cell = analysis["cells"][0]
    assert len(cell["classifications"]) == 9
    row = _cutoff(cell)
    assert row["seed_classes"]["22001"] == expected
    assert row["status"] == "development_only"
    assert row["dominant_state"] is None
    assert cell["continuous"]["G"] == {"status": "complete", "mean": .25, "ci_low": .1, "ci_high": .4, "n": 3}
    assert analysis["claim_support"] == "pending"


@pytest.mark.parametrize("seed_count,real_count,expected_status,expected_dominant", [
    (30, 24, "classified", "real_improvement"),
    (30, 23, "classified", "cross_seed_uncertain"),
    (29, 29, "insufficient_seeds", None),
])
def test_confirmatory_dominance_requires_thirty_seeds_and_eighty_percent(inputs, seed_count, real_count, expected_status, expected_dominant):
    frozen, _ = inputs
    frozen["spec"].update(purpose="confirmatory", seeds=list(range(1000, 1000 + seed_count)))
    summary = _summary(frozen)
    for i, row in enumerate(summary["records"][:seed_count]):
        row["metrics"]["terminal_year"].update(
            change_from_initial_sd=.3 if i < real_count else .1,
            inflation_mean_sd=.1 if i < real_count else .3,
        )
    row = _cutoff(phase.analyze_phase(frozen, summary)["cells"][0])
    assert row["status"] == expected_status
    assert row["dominant_state"] == expected_dominant
    assert row["counts"]["real_improvement"] == real_count
    assert row["proportions"]["real_improvement"] == real_count / seed_count


def test_missing_short_and_nonfinite_trials_remain_unclassified(inputs):
    frozen, summary = inputs
    summary["records"][0]["status"] = "missing"
    summary["records"][1]["metrics"]["terminal_year"].update(observations=251, complete_year=False)
    summary["records"][2]["metrics"]["terminal_year"]["change_from_initial_sd"] = float("nan")
    cell = phase.analyze_phase(frozen, summary)["cells"][0]
    assert [row["reason"] for row in cell["observations"]] == [
        "trial_missing", "incomplete_terminal_window", "invalid_terminal_metrics",
    ]
    assert cell["n_valid"] == 0
    assert cell["continuous"]["G"]["mean"] is None
    for row in cell["classifications"]:
        assert row["status"] == "incomplete"
        assert row["seed_classes"] == {}
        assert set(row["proportions"].values()) == {None}
        assert set(row["intervals"].values()) == {None}
    json.dumps(cell, allow_nan=False)


def test_incomplete_cell_uses_valid_seed_denominator_without_imputing_mean(inputs):
    frozen, summary = inputs
    summary["records"].pop(0)
    summary["records"][0]["metrics"]["terminal_year"]["start_day"] -= 1
    cell = phase.analyze_phase(frozen, summary)["cells"][0]
    assert cell["n_valid"] == 1
    assert cell["observations"][1]["reason"] == "terminal_window_mismatch"
    assert cell["continuous"]["W"]["mean"] is None
    row = _cutoff(cell)
    assert row["counts"]["mixed"] == 1
    assert row["proportions"]["mixed"] == 1
    assert row["intervals"]["mixed"] == pytest.approx([.20654931437723745, 1.])
    assert row["dominant_state"] is None


def test_mechanical_failure_excludes_seed_stylized_failure_blocks_confirmatory_label(inputs):
    frozen, _ = inputs
    frozen["spec"].update(purpose="confirmatory", seeds=list(range(30)))
    summary = _summary(frozen)
    summary["records"][0]["validation"]["stylized"]["status"] = "FAIL"
    cell = phase.analyze_phase(frozen, summary)["cells"][0]
    assert cell["n_valid"] == 30
    assert cell["core_validation_failures"] == 1
    assert _cutoff(cell)["status"] == "core_validation_failed"
    assert _cutoff(cell)["dominant_state"] is None
    summary["records"][0]["validation"]["mechanical"]["status"] = "FAIL"
    cell = phase.analyze_phase(frozen, summary)["cells"][0]
    assert cell["n_valid"] == 29
    assert cell["observations"][0]["reason"] == "mechanical_validation_failed"


@pytest.mark.parametrize("violation,match", [
    ("rules", "fixed version-1"), ("grid", "4-by-4"), ("policy", "constant baseline"),
    ("config", "differ only"), ("duplicate", "duplicate phase trial"),
])
def test_phase_rejects_changed_design_or_duplicate_trial(inputs, violation, match):
    frozen, summary = inputs
    if violation == "rules":
        frozen["spec"]["phase_analysis"]["dominant_fraction"] = .7
    elif violation == "grid":
        frozen["scenarios"].pop()
    elif violation == "policy":
        for row in frozen["scenarios"]:
            row["policy"]["intervention"] = {"transparency": .9}
    elif violation == "config":
        frozen["scenarios"][0]["config"]["n_firms"] = 60
    else:
        summary["records"].append(deepcopy(summary["records"][0]))
    with pytest.raises(ValueError, match=match):
        phase.analyze_phase(frozen, summary)


def test_archive_renders_actual_files_locks_inputs_and_never_reclassifies(inputs, tmp_path, monkeypatch):
    frozen, summary = inputs
    original = deepcopy((frozen, summary))
    destination = tmp_path / "phase"
    _write_archive(destination, frozen, summary)
    report = phase.archive_phase(destination)
    assert (frozen, summary) == original
    report_bytes = report.read_bytes()
    assert b"Development proportions are descriptive only" in report_bytes
    assert b"unadjusted across classes, cells and thresholds" in report_bytes
    analysis = json.loads((destination / "phase_analysis.json").read_text())
    assert len(analysis["cells"]) == 16
    assert sum(len(cell["classifications"]) for cell in analysis["cells"]) == 144
    manifest = json.loads((destination / "phase_manifest.json").read_text())
    assert manifest["rules_sha256"] == hashlib.sha256(canonical_json_bytes(phase.RULES)).hexdigest()
    assert manifest["analysis_source_sha256"] == sha256_file(Path(phase.__file__))
    for field in ("G", "W"):
        assert (destination / f"phase_{field}.png").read_bytes().startswith(b"\x89PNG")
        assert (destination / f"phase_{field}.pdf").read_bytes().startswith(b"%PDF")
    charts = json.loads((destination / "phase_charts_manifest.json").read_text())
    for name, digest in charts["artifacts"].items():
        assert sha256_file(destination / name) == digest

    def forbidden(*args, **kwargs):
        pytest.fail("rendering recomputed phase analysis")

    monkeypatch.setattr(phase, "analyze_phase", forbidden)
    assert phase.render_phase(destination).read_bytes() == report_bytes
    assert phase.archive_phase(destination).read_bytes() == report_bytes
    with (destination / "summary.json").open("a", encoding="utf-8") as stream:
        stream.write(" ")
    with pytest.raises(ValueError, match="phase input hash"):
        phase.render_phase(destination)


def test_archival_fallback_reads_hashed_trial_metrics(inputs, tmp_path, monkeypatch):
    frozen, summary = inputs
    row = summary["records"][0]
    metrics = row.pop("metrics")
    row["path"] = f"{row['scenario']}/seed_{row['seed']}/attempt_001"
    destination = tmp_path / "phase"
    _write_archive(destination, frozen, summary)
    trial = destination / row["path"]
    trial.mkdir(parents=True)
    (trial / "metrics.json").write_text(json.dumps(metrics), encoding="utf-8")
    scenario = frozen["scenarios"][0]
    identity = {"schema_version": 1, "config": {**scenario["config"], "seed": row["seed"]},
                "domain": scenario["domain"], "policy": scenario["policy"],
                "source_hashes": frozen["source_hashes"], "python_version": frozen["python_version"],
                "numpy_version": frozen["numpy_version"]}
    (trial / "manifest.json").write_text(json.dumps({
        **identity, "run_id": hashlib.sha256(canonical_json_bytes(identity)).hexdigest(),
        "status": "complete", "artifacts": {"metrics.json": sha256_file(trial / "metrics.json")},
    }), encoding="utf-8")
    monkeypatch.setattr(phase, "render_phase", lambda destination: Path(destination) / "phase_report.md")
    phase.archive_phase(destination)
    analysis = json.loads((destination / "phase_analysis.json").read_text())
    assert analysis["cells"][0]["n_valid"] == 3
    manifest = json.loads((destination / "phase_manifest.json").read_text())
    assert manifest["inputs_sha256"][row["path"] + "/metrics.json"] == sha256_file(trial / "metrics.json")
