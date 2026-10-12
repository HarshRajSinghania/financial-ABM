"""Held-out model comparison and mechanism ablations for an MSM calibration.

Run once after ``abm-calibrate-msm`` and ``abm-baselines`` have written
``calibration.json`` and ``baselines.json``. Every model is simulated with the
same fresh evaluation seeds, disjoint from the calibration seeds, and scored
with the same objective against training, validation and sealed test
industries. Ablations switch one mechanism off at the calibrated parameters
and are paired seed by seed, so their confidence intervals exclude the
common simulation noise.
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace
from datetime import date
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np
from numpy.typing import NDArray

from .baselines import baseline_moments
from .config import load_stage1_config
from .french49 import IndustrySplit, parse_french49_zip
from .mechanism_validation import build_scenarios
from .config import Stage1Config
from .harness import run_stage1
from .msm import (
    DEFAULT_PARAMETER_SPACE,
    MOMENT_NAMES,
    compute_moments,
    empirical_target,
    objective,
)
from .platform_tuning import disable_power_throttling

FloatArray = NDArray[np.float64]

EVALUATION_SEEDS = tuple(range(20261301, 20261351))
ABLATIONS = (
    "fixed_liquidity",
    "fixed_participation",
    "no_activity_persistence",
    "independent_signals",
)
MODEL_LABELS = {
    "abm": "Stage 1 ABM (MSM)",
    "ham": "Franke-Westerhoff HAM (MSM)",
    "garch_t": "GARCH(1,1)-t (MLE)",
    "iid_t": "i.i.d. Student-t (MLE)",
}
MOMENT_LABELS = {
    "daily_volatility": "Daily volatility",
    "excess_kurtosis": "Excess kurtosis",
    "return_acf_1": "Return ACF(1)",
    "abs_return_acf_1": "|Return| ACF(1)",
    "abs_return_acf_5": "|Return| ACF(5)",
    "abs_return_acf_20": "|Return| ACF(20)",
    "quantile_01": "1% quantile",
    "quantile_99": "99% quantile",
    "hill_tail_index": "Hill tail index",
}


def _scenario_path(config: Stage1Config, burn_in_days: int) -> tuple[FloatArray, int]:
    """Moments and evaluation-window price-cap hits of one simulated path.

    A capped day truncates the return distribution, so the report counts
    them rather than letting a clamp pass for an endogenous tail.
    """
    result = run_stage1(config)
    returns = result.prices[1:] / result.prices[:-1] - 1.0
    cap_hits = sum(int(audit.price_cap_hit) for audit in result.daily_audits[burn_in_days:])
    try:
        return compute_moments(returns[burn_in_days:]), cap_hits
    except ValueError:
        return np.full(len(MOMENT_NAMES), np.nan), cap_hits


def paired_effect(full: FloatArray, ablated: FloatArray) -> dict[str, dict[str, float]]:
    """Mean ablated-minus-full change per moment with a paired 95% interval."""
    from scipy.stats import t as student_t

    valid = np.all(np.isfinite(full), axis=1) & np.all(np.isfinite(ablated), axis=1)
    full, ablated = full[valid], ablated[valid]
    differences = ablated - full
    count = differences.shape[0]
    if count < 2:
        raise ValueError("paired effects need at least two valid seeds")
    half_width = student_t.ppf(0.975, count - 1) * differences.std(axis=0, ddof=1) / np.sqrt(count)
    effects = {}
    for column, name in enumerate(MOMENT_NAMES):
        base = float(full[:, column].mean())
        change = float(differences[:, column].mean())
        effects[name] = {
            "full": base,
            "ablated": float(ablated[:, column].mean()),
            "difference": change,
            "ci_low": change - float(half_width[column]),
            "ci_high": change + float(half_width[column]),
            "relative_change": change / base if base != 0 else float("nan"),
        }
    return {"paired_seeds": int(count), "moments": effects}


def build_report(
    *,
    calibration: Mapping[str, object],
    baselines: Mapping[str, object],
    config_path: Path,
    archive: Path,
    split_path: Path,
    start: date,
    end: date,
    seeds: Sequence[int],
    workers: int,
) -> dict[str, object]:
    dataset = parse_french49_zip(archive).between(start, end)
    split = IndustrySplit.from_json(split_path)
    targets = {
        "train": empirical_target(dataset, split.train),
        "validation": empirical_target(dataset, split.validation),
        "test": empirical_target(dataset, split.test),
    }
    observations = targets["train"].observations
    space = DEFAULT_PARAMETER_SPACE
    if list(calibration["parameter_names"]) != list(space.names):
        raise ValueError("calibration parameters do not match the current parameter space")
    theta = np.array(calibration["best_theta"], dtype=np.float64)
    calibrated = space.apply(load_stage1_config(config_path), theta)
    scenarios = build_scenarios(calibrated)
    names = ("full",) + ABLATIONS
    configs = [
        replace(scenarios[name], seed=seed, trading_days=calibrated.burn_in_days + observations)
        for name in names
        for seed in seeds
    ]
    with ProcessPoolExecutor(max_workers=workers, initializer=disable_power_throttling) as executor:
        paths = list(executor.map(_scenario_path, configs, [calibrated.burn_in_days] * len(configs)))
    simulated = np.vstack([moments for moments, _ in paths])
    cap_hits = np.array([hits for _, hits in paths])
    by_scenario = {
        name: simulated[index * len(seeds) : (index + 1) * len(seeds)]
        for index, name in enumerate(names)
    }
    price_cap_hits = {
        name: int(cap_hits[index * len(seeds) : (index + 1) * len(seeds)].sum())
        for index, name in enumerate(names)
    }
    model_moments = {"abm": by_scenario["full"], **baseline_moments(
        baselines, observations=observations, seeds=seeds)}
    comparison = {
        model: {group: objective(moments, target) for group, target in targets.items()}
        for model, moments in model_moments.items()
    }
    return {
        "moment_names": list(MOMENT_NAMES),
        "evaluation_seeds": list(seeds),
        "observations": observations,
        "period": [str(dataset.dates[0]), str(dataset.dates[-1])],
        "calibrated_parameters": dict(zip(space.names, theta.tolist(), strict=True)),
        "calibration_standard_errors": dict(zip(
            space.names, calibration["standard_errors"]["standard_errors"], strict=True)),
        "targets": {
            group: {
                "industries": list(target.industries),
                "moments": target.moments.tolist(),
                "standard_errors": target.standard_errors.tolist(),
            }
            for group, target in targets.items()
        },
        "comparison": comparison,
        "model_mean_moments": {
            model: np.nanmean(moments, axis=0).tolist() for model, moments in model_moments.items()
        },
        "ablations": {
            name: paired_effect(by_scenario["full"], by_scenario[name]) for name in ABLATIONS
        },
        "price_cap_hits": price_cap_hits,
    }


def write_figures(report: Mapping[str, object], output: Path) -> list[str]:
    import matplotlib

    matplotlib.use("Agg")
    from matplotlib import pyplot as plt

    written = []
    models = list(MODEL_LABELS)
    labels = [MOMENT_LABELS[name] for name in MOMENT_NAMES]
    positions = np.arange(len(MOMENT_NAMES))
    width = 0.8 / len(models)
    figure, axis = plt.subplots(figsize=(12, 5), constrained_layout=True)
    for offset, model in enumerate(models):
        t_values = report["comparison"][model]["test"]["t_statistics"]
        axis.bar(positions + (offset - (len(models) - 1) / 2) * width, t_values, width,
                 label=f"{MODEL_LABELS[model]}  J={report['comparison'][model]['test']['j']:.1f}")
    axis.axhspan(-2, 2, color="0.9", zorder=0)
    axis.axhline(0, color="0.3", linewidth=0.8)
    axis.set_xticks(positions, labels, rotation=30, ha="right")
    axis.set_ylabel("t-statistic vs. held-out industries")
    axis.set_title("Moment fit on sealed test industries (shaded band: |t| < 2)")
    axis.legend(frameon=False, fontsize=9)
    for suffix in ("png", "svg"):
        path = output / f"model_fit_test.{suffix}"
        figure.savefig(path, dpi=160)
        written.append(path.name)
    plt.close(figure)

    shown = ("excess_kurtosis", "abs_return_acf_1", "abs_return_acf_20", "hill_tail_index")
    figure, axes = plt.subplots(1, len(shown), figsize=(14, 4), constrained_layout=True)
    for axis, moment in zip(axes, shown, strict=True):
        effects = [report["ablations"][name]["moments"][moment] for name in ABLATIONS]
        changes = np.array([effect["difference"] for effect in effects])
        errors = np.array([[change - effect["ci_low"] for change, effect in zip(changes, effects, strict=True)],
                           [effect["ci_high"] - change for change, effect in zip(changes, effects, strict=True)]])
        axis.barh(np.arange(len(ABLATIONS)), changes, xerr=errors, color="#4c78a8", capsize=3)
        axis.axvline(0, color="0.3", linewidth=0.8)
        axis.set_yticks(np.arange(len(ABLATIONS)), ABLATIONS if axis is axes[0] else [])
        axis.set_title(f"{MOMENT_LABELS[moment]}\n(full model: {effects[0]['full']:.3f})")
        axis.set_xlabel("change when switched off")
    for suffix in ("png", "svg"):
        path = output / f"ablations.{suffix}"
        figure.savefig(path, dpi=160)
        written.append(path.name)
    plt.close(figure)
    return written


def _markdown_cell(text: str) -> str:
    return text.replace("|", r"\|")


def write_markdown(report: Mapping[str, object], output: Path) -> None:
    lines = [
        "# MSM calibration: held-out comparison and ablations",
        "",
        f"Daily French 49 industry returns, {report['period'][0]} to {report['period'][1]} "
        f"({report['observations']} days). Each model is simulated with "
        f"{len(report['evaluation_seeds'])} evaluation seeds disjoint from the calibration seeds. "
        "J is the sum of squared per-moment t-statistics (9 moments); lower is better.",
        "",
        "## Model comparison (J)",
        "",
        "| Model | Train | Validation | Test |",
        "|---|---:|---:|---:|",
    ]
    for model, label in MODEL_LABELS.items():
        scores = report["comparison"][model]
        lines.append(f"| {label} | {scores['train']['j']:.1f} | "
                     f"{scores['validation']['j']:.1f} | {scores['test']['j']:.1f} |")
    lines += ["", "## Moments on the test industries", "",
              "| Moment | Data (± s.e.) | " + " | ".join(MODEL_LABELS.values()) + " |",
              "|---|---:|" + "---:|" * len(MODEL_LABELS)]
    target = report["targets"]["test"]
    for index, name in enumerate(MOMENT_NAMES):
        row = f"| {_markdown_cell(MOMENT_LABELS[name])} | {target['moments'][index]:.4f} ± {target['standard_errors'][index]:.4f} |"
        for model in MODEL_LABELS:
            row += f" {report['model_mean_moments'][model][index]:.4f} |"
        lines.append(row)
    lines += ["", "## Calibrated ABM parameters", "", "| Parameter | Estimate | s.e. |", "|---|---:|---:|"]
    for name, value in report["calibrated_parameters"].items():
        lines.append(f"| `{name}` | {value:.4f} | {report['calibration_standard_errors'][name]:.4f} |")
    lines += ["", "## Ablations at the calibrated parameters", "",
              "Change in the moment when one mechanism is switched off, paired by seed (95% CI).", "",
              "| Ablation | Excess kurtosis | "
              + " | ".join(_markdown_cell(MOMENT_LABELS[name]) for name in ("abs_return_acf_1", "abs_return_acf_20"))
              + " | Hill index |",
              "|---|---:|---:|---:|---:|"]
    for name in ABLATIONS:
        cells = []
        for moment in ("excess_kurtosis", "abs_return_acf_1", "abs_return_acf_20", "hill_tail_index"):
            effect = report["ablations"][name]["moments"][moment]
            cells.append(f"{effect['difference']:+.3f} [{effect['ci_low']:+.3f}, {effect['ci_high']:+.3f}]")
        lines.append(f"| `{name}` | " + " | ".join(cells) + " |")
    hits = report["price_cap_hits"]
    lines += ["", "Evaluation-window days on which the ±max_log_return price clamp bound, summed over seeds: "
              + ", ".join(f"`{name}` {count}" for name, count in hits.items()) + "."]
    lines += ["", "![Model fit](model_fit_test.png)", "", "![Ablations](ablations.png)", ""]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--split", type=Path)
    parser.add_argument("--start", type=date.fromisoformat, default=date(2000, 1, 1))
    parser.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="redraw figures and report.md from an existing comparison.json",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    disable_power_throttling()
    destination = args.report_dir / "comparison.json"
    if args.render_only:
        report = json.loads(destination.read_text(encoding="utf-8"))
        write_figures(report, args.report_dir)
        write_markdown(report, args.report_dir)
        return 0
    missing = [name for name in ("config", "archive", "split") if getattr(args, name) is None]
    if missing:
        raise SystemExit(f"missing required options: {', '.join('--' + name for name in missing)}")
    if destination.exists():
        raise FileExistsError(f"{destination} exists; the sealed test is scored only once")
    report = build_report(
        calibration=json.loads((args.report_dir / "calibration.json").read_text(encoding="utf-8")),
        baselines=json.loads((args.report_dir / "baselines.json").read_text(encoding="utf-8")),
        config_path=args.config,
        archive=args.archive,
        split_path=args.split,
        start=args.start,
        end=args.end,
        seeds=EVALUATION_SEEDS,
        workers=args.workers,
    )
    with destination.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(report, indent=2) + "\n")
    write_figures(report, args.report_dir)
    write_markdown(report, args.report_dir)
    print((args.report_dir / "report.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
