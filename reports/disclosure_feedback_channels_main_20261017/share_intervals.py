"""Supplementary, added after the contract 20.20 run: intervals for each channel's share of the full-model effect.

  .venv/Scripts/python.exe reports/disclosure_feedback_channels_main_20261017/share_intervals.py

Contracts 20.19 and 20.20 classify a channel by its point share (channel mean / full-model effect mean) against
the 10% and 20% thresholds. In the main setting the I - B price and demand share came out at 9.75%, next to the 10%
threshold, so this script adds a paired 95% interval for every share, in the main setting and in 20.19's cell. It is
descriptive and changes no class, attribution or answer. The interval is the ratio estimator's linearization: with
r = mean(c) / mean(e) and z_i = c_i - r e_i per seed, r +- t(0.975, n - 1) sd(z) / (sqrt(n) |mean(e)|).

Reads results.json here and in reports/disclosure_feedback_channels_20261017/; writes share_intervals.json.
"""

from __future__ import annotations

import json
import platform
import sys
from pathlib import Path


def _no_wmi(*args, **kwargs):
    raise OSError("WMI not queried")


platform._wmi_query = _no_wmi  # the machine's WMI service hangs; see channels_main.py

import numpy as np  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
CELL_DIR = HERE.parent / "disclosure_feedback_channels_20261017"
CONTRASTS = {"I_minus_B": ("I", "B", "true_change"), "F_minus_B": ("F", "B", "true_change"),
             "I_minus_F": ("I", "F", "true_change"), "F_minus_B_terminal_inflation": ("F", "B", "terminal_inflation"),
             "I_minus_B_size_gap": ("I", "B", "size_gap")}
CHANNELS = (("feedback", "full", "Rbase"), ("evolution", "full", "frozen"), ("price_demand", "frozen", "Rbase"))
EXCLUDED = [41016]  # core validation failures in the main setting (contract 20.17 and this run)


def share_interval(part: np.ndarray, effect: np.ndarray) -> dict:
    n = part.size
    ratio = part.mean() / effect.mean()
    z = part - ratio * effect
    half = stats.t.ppf(0.975, n - 1) * z.std(ddof=1) / (np.sqrt(n) * abs(effect.mean()))
    return {"share": float(ratio), "ci_low": float(ratio - half), "ci_high": float(ratio + half), "n": int(n)}


def shares(values: dict, keep: np.ndarray | None = None) -> dict:
    out = {}
    for name, (plus, minus, metric) in CONTRASTS.items():
        series = {form: np.asarray(values[form][plus][metric]) - np.asarray(values[form][minus][metric]) for form in ("full", "frozen", "Rbase")}
        if keep is not None:
            series = {form: s[keep] for form, s in series.items()}
        out[name] = {channel: share_interval(series[a] - series[b], series["full"]) for channel, a, b in CHANNELS}
    return out


def main() -> None:
    main_results = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
    cell_results = json.loads((CELL_DIR / "results.json").read_text(encoding="utf-8"))
    keep = np.array([seed not in EXCLUDED for seed in main_results["seeds"]])
    payload = {
        "schema_version": 1, "generated_by": "reports/disclosure_feedback_channels_main_20261017/share_intervals.py",
        "status": "supplementary, added after the contract 20.20 run; descriptive; changes no class, attribution or answer",
        "interval": "ratio estimator linearization: r +- t(0.975, n-1) sd(c - r e) / (sqrt(n) |mean(e)|), paired over seeds",
        "main": shares(main_results["values"]),
        "main_core_validation_pass_only": {"excluded_seeds": EXCLUDED, "shares": shares(main_results["values"], keep)},
        "cell_20_19": shares(cell_results["values"]),
    }
    sys.stdout.reconfigure(encoding="utf-8")
    (HERE / "share_intervals.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("| 对比 | 通道 | 主设定占效应 | 主设定（n = 29） | 格点占效应 |")
    print("|---|---|---|---|---|")
    for name in CONTRASTS:
        for channel, _, _ in CHANNELS:
            cells = [payload["main"][name][channel], payload["main_core_validation_pass_only"]["shares"][name][channel],
                     payload["cell_20_19"][name][channel]]
            print(f"| {name} | {channel} | " + " | ".join(f"{c['share']:+.1%} [{c['ci_low']:+.1%}, {c['ci_high']:+.1%}]" for c in cells) + " |")


if __name__ == "__main__":
    main()
