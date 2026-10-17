"""Feedback channels in the main setting (research contract 20.20): contract 20.19's decomposition at taste 0.0724 x II 0.2.

  .venv/Scripts/python.exe reports/disclosure_feedback_channels_main_20261017/channels_main.py check
  .venv/Scripts/python.exe reports/disclosure_feedback_channels_main_20261017/channels_main.py run --workers 16
  .venv/Scripts/python.exe reports/disclosure_feedback_channels_main_20261017/channels_main.py analyze

Contract 20.17 found the feedback term (full model - Rbase) of I - B in the main setting at -0.008 [-0.022, +0.007] SD,
not identifiable. Contract 20.19 split the same term in cell taste 0.1448 x II 0.2 into an investor evolution channel
(-0.086) and a price and demand channel (+0.062) that nearly cancel. This script repeats 20.19's frozen-evolution
decomposition in the main setting, to see whether its near-zero net is also two opposing channels. The market
subclasses, the run task and the channel arithmetic are imported from 20.19's channels.py unchanged; only the market
setting (stage F's own scenarios B, I, F) and the sources of the full-model and Rbase values differ.

(1) run, phase 1: B on seeds 41001-41030 with the investor types recorded after every imitation step
    (configs/disclosure_stage_f_confirmatory_v1.json). Each must reproduce the stage F archive's B fingerprint.
(2) run, phase 2: the frozen form of B, I (transparency 0.6) and F (fixed fine 4x) on the same seeds, each with its
    seed's recorded B types. Frozen B must reproduce the B fingerprint.
(3) analyze: per contrast, the full, frozen and Rbase values (full and Rbase per seed from contract 20.17's
    results.json, same seeds), the two channels with paired 95% t intervals, their shares, the classes and attribution
    of contract 20.19, the answer for I - B fixed in contract 20.20, and the paired difference of every channel from
    20.19's cell (same seeds).

Writes results.json, analysis.json and tables.md next to this script; per-task records and type paths stay in work/
(local, regenerable). A failed record is moved to work/failed/ before its task is run again, never deleted.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path


def _no_wmi(*args, **kwargs):
    raise OSError("WMI not queried")


# As in contract 20.19's channels.py: the machine's WMI service hangs and Python 3.12's platform module would wait on it
# when numpy is imported; single-threaded BLAS keeps each worker's commit small. Both are set before numpy loads,
# here and in every spawned worker (which re-runs this module's top level and so imports channels.py again).
platform._wmi_query = _no_wmi
for _name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[_name] = "1"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CELL_DIR = ROOT / "reports" / "disclosure_feedback_channels_20261017"

_channels_spec = importlib.util.spec_from_file_location("feedback_channels", CELL_DIR / "channels.py")
ch = importlib.util.module_from_spec(_channels_spec)
sys.modules["feedback_channels"] = ch
_channels_spec.loader.exec_module(ch)
strong, cf = ch.strong, ch.cf

import numpy as np  # noqa: E402

from abm.disclosure.experiments import freeze_spec  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

SETTING_LABEL = "主设定 taste 0.0724 × II 0.2"
CELL_LABEL = ch.CELL_LABEL
POLICIES, FORMS, CHANNELS, CONTRASTS = ch.POLICIES, ch.FORMS, ch.CHANNELS, ch.CONTRASTS
SEEDS, CHECK_SEED, METRICS = ch.SEEDS, ch.CHECK_SEED, ch.METRICS
WORK = HERE / "work"
QUESTION = "I_minus_B"  # the contrast contract 20.20 answers
JUDGED = ("I_minus_B", "F_minus_B", "I_minus_F")  # attributed and written separately; the other two are descriptive


# -- orchestration ------------------------------------------------------------------------------------------

def record_path(out: Path, form: str, policy: str, seed: int) -> Path:
    return out / "records" / f"{form}_{policy}__{seed}.json"


def execute(seeds: list[int], archive: Path, out: Path, workers: int) -> None:
    spec = freeze_spec(cf.SPEC)
    if spec["experiment_id"] != cf.EXPERIMENT_ID:
        raise RuntimeError("the stage F identity no longer reproduces; source or environment changed")
    _, records = cf.archive_records(archive)
    scenarios = {row["name"]: row for row in spec["scenarios"]}
    cf.log(f"experiment_id {spec['experiment_id']} (stage F) reproduces; archive {archive.name}; main setting; "
           f"{len(seeds)} seeds; {workers} workers")
    failed_dir = out / "failed"
    started = time.perf_counter()

    def report(row: dict, count: int, total: int) -> None:
        cf.write_json(record_path(out, row["form"], row["scenario"], row["seed"]), row)
        if row["status"] == "complete":
            match = row["fingerprint_matches"]
            note = (f"fingerprint {'n/a' if match is None else 'ok' if match else 'MISMATCH'}, own replay actions "
                    f"{'identical' if row['own_replay']['actions_identical'] else 'DIFFER'}, core "
                    f"{row['core_validation']['mechanical']}/{row['core_validation']['stylized']}")
            if row["form"] == "frozen":
                note += f", own step differs after switch {row['own_step']['post_switch_differs_total']}"
        else:
            note = f"FAILED {row['error_type']}: {row['error']}"
        cf.log(f"{row['form']} {count}/{total} {row['scenario']} {row['seed']} {row['seconds']} s, "
               f"worker peak {row['worker_peak_commit_gb']} GB; {note}")

    with ProcessPoolExecutor(max_workers=workers, initializer=disable_power_throttling) as pool:
        jobs = [seed for seed in seeds if strong.pending(record_path(out, "record", "B", seed), failed_dir)]
        futures = [pool.submit(ch.run_task, "record", scenarios["B"], seed, records[("B", seed)]["result_fingerprint"], str(out))
                   for seed in jobs]
        for count, future in enumerate(as_completed(futures), 1):
            report(future.result(), count, len(futures))
        cf.log(f"phase 1 done in {time.perf_counter() - started:.0f} s")
        futures = []
        for seed in seeds:
            base = ch.complete(record_path(out, "record", "B", seed))
            if base is None:
                continue
            for policy in POLICIES:
                if strong.pending(record_path(out, "frozen", policy, seed), failed_dir):
                    expected = base["fingerprint"] if policy == "B" else None
                    futures.append(pool.submit(ch.run_task, "frozen", scenarios[policy], seed, expected, str(out)))
        for count, future in enumerate(as_completed(futures), 1):
            report(future.result(), count, len(futures))
    cf.log(f"all done in {time.perf_counter() - started:.0f} s")


def check() -> None:
    """Pipeline check on development seed 33001: identities, time and memory only, no effect estimates."""
    out = HERE / "work_check"
    execute([CHECK_SEED], cf.DEV_ARCHIVE, out, workers=3)
    base = ch.complete(record_path(out, "record", "B", CHECK_SEED))
    if base is None:
        raise SystemExit("the B record failed")
    cf.log(f"record B: fingerprint vs development archive B {base['fingerprint_matches']}; own replay actions "
           f"identical {base['own_replay']['actions_identical']}; core {base['core_validation']}; {base['seconds']} s; "
           f"worker peak commit {base['worker_peak_commit_gb']} GB")
    for policy in POLICIES:
        row = ch.complete(record_path(out, "frozen", policy, CHECK_SEED))
        if row is None:
            raise SystemExit(f"frozen {policy} failed")
        own, step = row["own_replay"], row["own_step"]
        cf.log(f"frozen {policy}: impact-share path equals B's {row['impact_share_sha256'] == base['impact_share_sha256']}; "
               f"latent tastes equal {row['latent_taste_sha256'] == base['latent_taste_sha256']}; pre-switch equals B's "
               f"{row['pre_switch_sha256'] == base['pre_switch_sha256']}; audits equal {row['audit_sha256'] == base['audit_sha256']}; "
               f"own step differs before / after switch {step['pre_switch_differs_total']} / {step['post_switch_differs_total']}; "
               f"own replay actions identical {own['actions_identical']}, amounts {own['amounts_max_abs']:.1e}, true "
               f"{own['true_max_abs']:.1e}, inflation {own['inflation_max_abs']:.1e}; core {row['core_validation']}; "
               f"{row['seconds']} s; worker peak commit {row['worker_peak_commit_gb']} GB")
    frozen_b = ch.complete(record_path(out, "frozen", "B", CHECK_SEED))
    cf.log(f"identity: frozen B fingerprint equals the B run's {frozen_b['fingerprint'] == base['fingerprint']}; "
           f"metrics max difference {cf.max_difference(frozen_b['full'], base['full']):.1e}")


# -- analysis -----------------------------------------------------------------------------------------------

def collect(out: Path) -> dict:
    stored = json.loads((cf.HERE / "results.json").read_text(encoding="utf-8"))
    if stored["seeds"] != SEEDS:
        raise RuntimeError("the 20.17 results use other seeds")
    values = {"full": {p: stored["values"]["full"][p] for p in POLICIES},
              "Rbase": {p: stored["values"]["Rbase"][p] for p in POLICIES},
              "frozen": {p: {metric: [] for metric in METRICS} for p in POLICIES}}
    checks = {"failed": [], "record_runs": 0, "record_fingerprints_matching_stage_f": 0, "record_vs_20_17_full_max": 0.0,
              "frozen_runs": 0, "frozen_B_fingerprints_equal_B": 0, "frozen_B_vs_B_metrics_max": 0.0,
              "frozen_B_own_step_differs_total": 0, "impact_share_paths_equal_B": 0, "latent_tastes_equal_B": 0,
              "pre_switch_equal_B": 0, "audits_equal_B": 0, "pre_switch_own_step_differs_total": 0,
              "own_actions_identical": 0, "own_max_abs": {"amounts": 0.0, "true": 0.0, "inflation": 0.0, "metrics": 0.0},
              "metric_function_max": 0.0, "core_validation_failures": {}, "seconds_median": None,
              "worker_peak_commit_gb_max": 0.0}
    rows, seconds = {}, []
    for seed in SEEDS:
        base = ch.complete(record_path(out, "record", "B", seed))
        if base is None:
            checks["failed"].append(f"record B {seed}")
            continue
        rows[("record", "B", seed)] = base
        checks["record_runs"] += 1
        checks["record_fingerprints_matching_stage_f"] += bool(base["fingerprint_matches"])
        checks["record_vs_20_17_full_max"] = max(checks["record_vs_20_17_full_max"], max(
            abs(base["full"][m] - values["full"]["B"][m][SEEDS.index(seed)]) for m in METRICS))
        for policy in POLICIES:
            row = ch.complete(record_path(out, "frozen", policy, seed))
            if row is None:
                checks["failed"].append(f"frozen {policy} {seed}")
                continue
            rows[("frozen", policy, seed)] = row
            checks["frozen_runs"] += 1
            checks["impact_share_paths_equal_B"] += row["impact_share_sha256"] == base["impact_share_sha256"]
            checks["latent_tastes_equal_B"] += row["latent_taste_sha256"] == base["latent_taste_sha256"]
            checks["pre_switch_equal_B"] += row["pre_switch_sha256"] == base["pre_switch_sha256"]
            checks["audits_equal_B"] += row["audit_sha256"] == base["audit_sha256"]
            checks["pre_switch_own_step_differs_total"] += row["own_step"]["pre_switch_differs_total"]
            if policy == "B":
                checks["frozen_B_fingerprints_equal_B"] += row["fingerprint"] == base["fingerprint"]
                checks["frozen_B_vs_B_metrics_max"] = max(checks["frozen_B_vs_B_metrics_max"], cf.max_difference(row["full"], base["full"]))
                checks["frozen_B_own_step_differs_total"] += row["own_step"]["post_switch_differs_total"]
    for (form, policy, seed), row in rows.items():
        seconds.append(row["seconds"])
        checks["worker_peak_commit_gb_max"] = max(checks["worker_peak_commit_gb_max"], row["worker_peak_commit_gb"] or 0.0)
        own = row["own_replay"]
        checks["own_actions_identical"] += own["actions_identical"]
        for key in ("amounts", "true", "inflation"):
            checks["own_max_abs"][key] = max(checks["own_max_abs"][key], own[f"{key}_max_abs"])
        checks["own_max_abs"]["metrics"] = max(checks["own_max_abs"]["metrics"], own["metrics_max_difference"])
        checks["metric_function_max"] = max(checks["metric_function_max"], row["metric_function_max_difference"])
        if any(status != "PASS" for status in row["core_validation"].values()):
            checks["core_validation_failures"].setdefault(f"{form}_{policy}", []).append([seed, row["first_price_cap_day"]])
    if checks["failed"]:
        raise RuntimeError(f"incomplete tasks: {checks['failed']}")
    checks["seconds_median"] = float(np.median(seconds))
    for policy in POLICIES:
        for seed in SEEDS:
            for metric in METRICS:
                values["frozen"][policy][metric].append(rows[("frozen", policy, seed)]["full"][metric])
    return {"values": values, "checks": checks, "rows": rows}


def channel_series(values: dict, plus: str, minus: str, metric: str) -> dict:
    series = {form: np.asarray(values[form][plus][metric]) - np.asarray(values[form][minus][metric]) for form in FORMS}
    return {"effect": series["full"], **{channel: series[a] - series[b] for channel, a, b in CHANNELS}}


ANSWER = {  # contract 20.20: is the near-zero I - B feedback of the main setting two opposing channels?
    "yes": "yes: two identifiable channels of opposite sign, each at least a tenth of the effect, cancel as in the 20.19 cell",
    "partly": "partly: both channels are identifiable and of opposite sign, but at least one is below a tenth of the effect",
    "no, one channel": "no: only one channel is identifiable",
    "no, same sign": "no: both channels are identifiable and of the same sign",
    "no, neither": "no: neither channel is identifiable on its own; the near-zero net is not a cancellation of identifiable channels",
}
ATTRIBUTION_TEXT = {
    "evolution": "the feedback runs through investor evolution",
    "mainly evolution": "the feedback runs mainly through investor evolution",
    "both": "both channels contribute substantially",
    "mainly price and demand": "the feedback runs mainly through prices and demand",
    "price and demand": "the feedback runs through prices and demand; investor evolution has no identifiable part",
    "opposite signs": "the two channels act in opposite directions",
    "neither identifiable": "neither channel is identifiable on its own",
}


def answer(row: dict) -> dict:
    """Contract 20.20's answer for I - B, from 20.19's attribution and 20.18's classes."""
    label = row["attribution"]["label"]
    evolution, price_demand = row["channels"]["evolution"]["mean"], row["channels"]["price_demand"]["mean"]
    if label == "opposite signs":
        tenth = all(row["classes"][channel]["class"] != "none" for channel in ("evolution", "price_demand"))
        key = "yes" if tenth else "partly"
    elif label in ("evolution", "price and demand"):
        key = "no, one channel"
    elif label == "neither identifiable":
        key = "no, neither"
    else:
        key = "no, same sign"
    return {"answer": key, "reading": ANSWER[key], "attribution": label,
            "directions_as_in_cell": bool(evolution < 0 < price_demand)}


def compare_with_cell(main_values: dict, keep: np.ndarray | None = None) -> dict:
    """The 20.19 cell's channels (recomputed from its results.json) and the paired main - cell difference per seed."""
    cell_values = json.loads((CELL_DIR / "results.json").read_text(encoding="utf-8"))
    if cell_values["seeds"] != SEEDS:
        raise RuntimeError("the 20.19 results use other seeds")
    cell_values = cell_values["values"]
    out = {}
    for name, (plus, minus, metric) in CONTRASTS.items():
        main, cell = channel_series(main_values, plus, minus, metric), channel_series(cell_values, plus, minus, metric)
        if keep is not None:
            main, cell = {k: v[keep] for k, v in main.items()}, {k: v[keep] for k, v in cell.items()}
        out[name] = {"main_minus_cell": {part: cf.interval(main[part] - cell[part]) for part in main},
                     "cell": {part: cf.interval(cell[part]) for part in cell}}
    return out


def cell_reproduction(cell_rows: dict) -> float:
    """Largest difference between 20.19's stored contrasts and the same arithmetic on its results.json."""
    stored = json.loads((CELL_DIR / "analysis.json").read_text(encoding="utf-8"))["contrasts"]
    return max(abs(stored[name][group][part][key] - row[group][part][key])
               for name, row in cell_rows.items() for group in ("forms", "channels")
               for part in row[group] for key in ("mean", "ci_low", "ci_high"))


def channel_description(rows: dict) -> dict:
    """How B, market caps and the impact-investor population respond to I and F, full model versus frozen."""
    full_rows = {}
    for policy in POLICIES:
        for seed in SEEDS:
            path = cf.WORK / "records" / f"{policy}__{seed}.json"
            full_rows[(policy, seed)] = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    have_full = all(row is not None for row in full_rows.values())
    out = {"full_model_source": "contract 20.17 records (local work/)" if have_full else "unavailable"}
    base = [rows[("record", "B", seed)] for seed in SEEDS]
    for policy in ("I", "F"):
        frozen = [rows[("frozen", policy, seed)] for seed in SEEDS]
        forms = {"frozen": frozen, **({"full": [full_rows[(policy, seed)] for seed in SEEDS]} if have_full else {})}
        row = {}
        for form, own in forms.items():
            row[form] = {
                "window_b_relative": cf.interval([o["benefit"]["window_mean"] / b["benefit"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "window_b_relative_by_size": [cf.interval(c) for c in zip(*(
                    [x / y - 1 for x, y in zip(o["benefit"]["window_by_size"], b["benefit"]["window_by_size"])] for o, b in zip(own, base)))],
                "window_price_relative": cf.interval([o["price"]["window_mean"] / b["price"]["window_mean"] - 1 for o, b in zip(own, base)]),
                "impact_share_day_3500_difference": cf.interval([o["impact_share"]["day_3500"] - b["impact_share"]["day_3500"] for o, b in zip(own, base)]),
            }
        row["frozen"]["impact_wealth_share_day_3500_difference"] = cf.interval(
            [o["impact_wealth_share"]["day_3500"] - b["impact_wealth_share"]["day_3500"] for o, b in zip(frozen, base)])
        row["frozen"]["own_step"] = {
            "post_switch_differs_per_step": cf.interval([o["own_step"]["post_switch_differs_total"] / o["own_step"]["post_switch_steps"] for o in frozen]),
            "post_switch_net_share_per_step": cf.interval([o["own_step"]["post_switch_net_total"] / o["own_step"]["post_switch_steps"]
                                                           / o["own_step"]["n_investors"] for o in frozen]),
        }
        out[policy] = row
    out["B_levels"] = {"window_mean": cf.interval([b["benefit"]["window_mean"] for b in base]),
                       "impact_share": {day: cf.interval([b["impact_share"][day] for b in base]) for day in ("day_0", "day_1200", "day_3500")}}
    return out


def analyze(out: Path, dest: Path = HERE) -> None:
    gathered = collect(out)
    values, checks, rows = gathered["values"], gathered["checks"], gathered["rows"]
    contrasts = ch.contrast_rows(values)
    earlier = json.loads((cf.HERE / "analysis.json").read_text(encoding="utf-8"))["checks"]["core_validation_failures"]
    failing = sorted({seed for p in POLICIES for seed in earlier.get(p, [])}
                     | {seed for runs in checks["core_validation_failures"].values() for seed, _ in runs})
    keep = np.array([seed not in failing for seed in SEEDS])
    robust = ch.contrast_rows(values, keep) if not keep.all() else None
    cell_rows = ch.contrast_rows(json.loads((CELL_DIR / "results.json").read_text(encoding="utf-8"))["values"])
    ordering = {}
    for form in FORMS:
        i, f, b = (np.asarray(values[form][p]["true_change"]) for p in ("I", "F", "B"))
        ordering[form] = {"mean": bool(i.mean() > f.mean() > b.mean()), "seeds": int(((i > f) & (f > b)).sum())}
    levels = {p: {metric: {form: cf.interval(values[form][p][metric]) for form in FORMS}
                  for metric in ("true_change", "wash", "terminal_inflation", "size_gap")} for p in POLICIES}
    analysis = {
        "schema_version": 1, "generated_by": "reports/disclosure_feedback_channels_main_20261017/channels_main.py",
        "contract": "docs/disclosure_research_contract.md 20.20", "stage_f_experiment_id": cf.EXPERIMENT_ID,
        "setting": SETTING_LABEL, "seeds": f"{SEEDS[0]}-{SEEDS[-1]}", "window": [cf.START, cf.DAYS],
        "forms": {"full": "full model (contract 20.17 results.json, from the stage F archive)",
                  "frozen": "full model with the investor types after every imitation step set to the seed's B run's",
                  "Rbase": "firm-side replay with the B run's B, market caps and audits (contract 20.17 results.json)"},
        "channels": {channel: f"{a} - {b}" for channel, a, b in CHANNELS},
        "interval": "paired 95% t interval over seeds",
        "classes": {"channel classes": "contract 20.18 thresholds on the channel's share of the full-model effect",
                    "attribution": "contract 20.19: by which channel intervals exclude 0 and the evolution share of the feedback (2/3, 1/3)",
                    "answer": "contract 20.20, for I - B: yes / partly / no (one channel, same sign, neither)"},
        "checks": checks, "core_validation_failing_seeds": failing, "contrasts": contrasts,
        "core_validation_pass_only": {"n": int(keep.sum()), "contrasts": robust,
                                      "answer": answer(robust[QUESTION]),
                                      "comparison_with_cell": compare_with_cell(values, keep)} if robust else None,
        "ordering_I_F_B": ordering, "levels": levels,
        "answer": answer(contrasts[QUESTION]),
        "verdict": {name: {"attribution": contrasts[name]["attribution"]["label"],
                           "reading": ATTRIBUTION_TEXT[contrasts[name]["attribution"]["label"]]} for name in JUDGED},
        "comparison_with_cell": {"cell": CELL_LABEL, "source": "reports/disclosure_feedback_channels_20261017/results.json (contract 20.19)",
                                 "cell_contrasts_reproduce_20_19_max_difference": cell_reproduction(cell_rows),
                                 "cell_contrasts": {name: {"channels": row["channels"], "classes": row["classes"],
                                                           "attribution": row["attribution"]["label"]} for name, row in cell_rows.items()},
                                 "cell_answer_by_20_20_rule": answer(cell_rows[QUESTION]),
                                 "paired": compare_with_cell(values)},
        "feedback_channels": channel_description(rows),
        "cell_feedback_channels": json.loads((CELL_DIR / "analysis.json").read_text(encoding="utf-8"))["feedback_channels"],
    }
    cf.write_json(dest / "analysis.json", analysis)
    cf.write_json(dest / "results.json", {"schema_version": 1, "seeds": SEEDS, "metrics": list(METRICS),
                                          "note": "values[form][policy][metric] = per-seed list in seed order; full and Rbase from contract 20.17",
                                          "values": values})
    write_tables(analysis, dest)
    cf.log("wrote analysis.json, results.json and tables.md")


def share(value: float | None) -> str:
    return "—" if value is None else f"{value:+.0%}"


def write_tables(analysis: dict, dest: Path) -> None:
    c, fmt = analysis["checks"], cf.fmt
    lines = ["# 主设定中反馈的两个通道：完整表格", "", f"由 channels_main.py analyze 生成。{SETTING_LABEL}，种子 41001–41030，配对 95% t 区间，未作多重校正。"
             "完整模型与 Rbase 的逐种子值取自契约 20.17 的 results.json；冻结形式为本分析的运行。", "",
             "## 检查", "",
             f"- 记录运行（B）{c['record_runs']} 个，指纹与阶段 F 档案 B 一致 {c['record_fingerprints_matching_stage_f']} 个；"
             f"指标与 20.17 完整模型的最大差 {c['record_vs_20_17_full_max']:.1e}。",
             f"- 冻结运行 {c['frozen_runs']} 个；冻结 B 的指纹等于 B {c['frozen_B_fingerprints_equal_B']}/30，指标最大差 {c['frozen_B_vs_B_metrics_max']:.1e}，"
             f"冻结 B 中本运行自身模仿与基准不同的累计人次 {c['frozen_B_own_step_differs_total']}。",
             f"- 影响力投资者占比逐日路径等于 B：{c['impact_share_paths_equal_B']}/{c['frozen_runs']}；潜在偏好相同 {c['latent_tastes_equal_B']}；"
             f"切换前逐位相同 {c['pre_switch_equal_B']}；核查抽样相同 {c['audits_equal_B']}；切换前自身模仿与基准不同的累计人次 {c['pre_switch_own_step_differs_total']}。",
             f"- 自身路径重放行动逐期相同 {c['own_actions_identical']} 个；幅度、真实水平、虚报最大绝对差 {c['own_max_abs']['amounts']:.1e}、"
             f"{c['own_max_abs']['true']:.1e}、{c['own_max_abs']['inflation']:.1e}，指标最大差 {c['own_max_abs']['metrics']:.1e}；"
             f"指标函数与 compute_metrics 最大差 {c['metric_function_max']:.1e}。",
             f"- 单个运行耗时中位数 {c['seconds_median']:.0f} 秒；worker 峰值提交内存最大 {c['worker_peak_commit_gb_max']} GB。",
             f"- 核心验证失败（[种子, 首次价格截断日]）：{json.dumps(c['core_validation_failures'])}；剔除用的种子 {analysis['core_validation_failing_seeds']}。",
             f"- 用 20.19 的 results.json 重算该格点的对比，与其 analysis.json 的最大差 "
             f"{analysis['comparison_with_cell']['cell_contrasts_reproduce_20_19_max_difference']:.1e}。", "",
             "## 各形式的值", "", "| 对比 | 完整模型 | 冻结演化 | Rbase |", "|---|---|---|---|"]
    for name, row in analysis["contrasts"].items():
        lines.append(f"| {name} | " + " | ".join(fmt(row["forms"][form]) for form in FORMS) + " |")
    lines += ["", "## 两个通道", "",
              "| 对比 | 反馈 完整−Rbase | 演化 完整−冻结 | 价格与需求 冻结−Rbase | 演化占效应 | 价格需求占效应 | 演化 / 反馈 | 归属 |",
              "|---|---|---|---|---:|---:|---:|---|"]
    for name, row in analysis["contrasts"].items():
        parts, cl = row["channels"], row["classes"]
        lines.append(f"| {name} | {fmt(parts['feedback'])} | {fmt(parts['evolution'])} | {fmt(parts['price_demand'])} | "
                     f"{share(cl['evolution']['share'])} ({cl['evolution']['class']}) | {share(cl['price_demand']['share'])} "
                     f"({cl['price_demand']['class']}) | {share(row['evolution_over_feedback'])} | {row['attribution']['label']} |")
    a = analysis["answer"]
    lines += ["", "## 契约 20.20 的问题：I − B 的近零净反馈是否也是两个方向相反的通道", "",
              f"- 回答：**{a['answer']}**（{a['reading']}）；归属 {a['attribution']}；方向与 20.19 格点相同（E < 0 < D）：{a['directions_as_in_cell']}",
              f"- 同一规则用于 20.19 格点：{analysis['comparison_with_cell']['cell_answer_by_20_20_rule']['answer']}", ""]
    for name, verdict in analysis["verdict"].items():
        lines.append(f"- {name}：{verdict['attribution']}；{verdict['reading']}")
    robust = analysis["core_validation_pass_only"]
    if robust:
        lines += ["", f"## 剔除核心验证失败种子之后（n = {robust['n']}）", "",
                  "| 对比 | 反馈 | 演化 | 价格与需求 | 演化 / 反馈 | 归属 |", "|---|---|---|---|---:|---|"]
        for name, row in robust["contrasts"].items():
            parts = row["channels"]
            lines.append(f"| {name} | {fmt(parts['feedback'])} | {fmt(parts['evolution'])} | {fmt(parts['price_demand'])} | "
                         f"{share(row['evolution_over_feedback'])} | {row['attribution']['label']} |")
        lines += ["", f"- I − B 的回答：{robust['answer']['answer']}"]
    comparison = analysis["comparison_with_cell"]
    lines += ["", f"## 与 20.19 格点（{CELL_LABEL}）比较", "",
              "| 对比 | 通道 | 主设定 | 格点 | 主设定 − 格点（配对） | 主设定占效应 | 格点占效应 |", "|---|---|---|---|---|---:|---:|"]
    for name, row in analysis["contrasts"].items():
        cell = comparison["cell_contrasts"][name]
        for part, label in (("feedback", "反馈"), ("evolution", "演化 E"), ("price_demand", "价格与需求 D")):
            lines.append(f"| {name} | {label} | {fmt(row['channels'][part])} | {fmt(cell['channels'][part])} | "
                         f"{fmt(comparison['paired'][name]['main_minus_cell'][part])} | {share(row['classes'][part]['share'])} | "
                         f"{share(cell['classes'][part]['share'])} |")
    lines += ["", "| 对比 | 完整模型效应：主设定 − 格点（配对） |", "|---|---|"]
    for name in analysis["contrasts"]:
        lines.append(f"| {name} | {fmt(comparison['paired'][name]['main_minus_cell']['effect'])} |")
    lines += ["", "## 排序 I > F > B（均值 / 逐种子计数）", "", "| 完整 | 冻结 | Rbase |", "|---|---|---|",
              "| " + " | ".join(f"{analysis['ordering_I_F_B'][f]['mean']} / {analysis['ordering_I_F_B'][f]['seeds']}" for f in FORMS) + " |",
              "", "## 场景水平", "", "```json", json.dumps(analysis["levels"], ensure_ascii=False, indent=1), "```", "",
              "## 反馈通道（描述）", "", "```json", json.dumps(analysis["feedback_channels"], ensure_ascii=False, indent=1), "```", ""]
    (dest / "tables.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("check", "run", "analyze"))
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()
    disable_power_throttling()
    if args.command == "check":
        check()
    elif args.command == "run":
        execute(SEEDS, cf.ARCHIVE, WORK, args.workers)
    else:
        analyze(WORK)


if __name__ == "__main__":
    main()
