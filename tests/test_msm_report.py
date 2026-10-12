import numpy as np
import pytest

from abm.msm import MOMENT_NAMES
from abm.msm_report import ABLATIONS, MODEL_LABELS, paired_effect, write_figures, write_markdown

pytest.importorskip("scipy")
pytest.importorskip("matplotlib")


def test_paired_effect_reports_mean_change_and_interval():
    rng = np.random.default_rng(1)
    full = rng.normal(1.0, 0.5, size=(40, len(MOMENT_NAMES)))
    ablated = full - 0.2 + rng.normal(0.0, 0.01, size=full.shape)
    effect = paired_effect(full, ablated)["moments"]["excess_kurtosis"]
    assert effect["difference"] == pytest.approx(-0.2, abs=0.01)
    assert effect["ci_low"] < effect["difference"] < effect["ci_high"]
    assert effect["ci_high"] - effect["ci_low"] < 0.02


def test_paired_effect_drops_failed_seeds():
    full = np.ones((3, len(MOMENT_NAMES)))
    ablated = np.ones((3, len(MOMENT_NAMES)))
    ablated[0] = np.nan
    assert paired_effect(full, ablated)["paired_seeds"] == 2


def _synthetic_report():
    k = len(MOMENT_NAMES)
    score = {"j": 3.0, "t_statistics": [0.5] * k, "simulated_moments": [0.1] * k, "failed_paths": 0}
    effect = {"full": 1.0, "ablated": 0.5, "difference": -0.5, "ci_low": -0.6,
              "ci_high": -0.4, "relative_change": -0.5}
    return {
        "moment_names": list(MOMENT_NAMES),
        "evaluation_seeds": [1, 2],
        "observations": 100,
        "period": ["2000-01-03", "2025-12-31"],
        "calibrated_parameters": {"noise_scale": 1.0},
        "calibration_standard_errors": {"noise_scale": 0.1},
        "targets": {group: {"industries": [], "moments": [0.1] * k, "standard_errors": [0.01] * k}
                    for group in ("train", "validation", "test")},
        "comparison": {model: {group: score for group in ("train", "validation", "test")}
                       for model in MODEL_LABELS},
        "model_mean_moments": {model: [0.1] * k for model in MODEL_LABELS},
        "ablations": {name: {"paired_seeds": 2, "moments": {moment: effect for moment in MOMENT_NAMES}}
                      for name in ABLATIONS},
        "price_cap_hits": {"full": 0, **{name: 0 for name in ABLATIONS}},
    }


def test_report_renders_figures_and_markdown(tmp_path):
    report = _synthetic_report()
    written = write_figures(report, tmp_path)
    write_markdown(report, tmp_path)
    assert {"model_fit_test.png", "ablations.svg"} <= set(written)
    text = (tmp_path / "report.md").read_text(encoding="utf-8")
    assert "| Stage 1 ABM (MSM) | 3.0 | 3.0 | 3.0 |" in text
    assert "`fixed_liquidity`" in text
    assert r"| \|Return\| ACF(1) |" in text
    for line in text.splitlines():
        if line.startswith("| Ablation"):
            assert line.replace(r"\|", "").count("|") == 6
        if line.startswith(r"| \|Return\| ACF"):
            assert line.replace(r"\|", "").count("|") == 3 + len(MODEL_LABELS)
