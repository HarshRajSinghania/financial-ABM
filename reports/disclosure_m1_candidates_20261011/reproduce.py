"""Reproduce the frozen 18-run M1 development comparison without tuning."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
import time
from dataclasses import replace
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path

for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[name] = "1"

DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[1]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np

from abm.disclosure.config import MarketConfig, TRADING_DAYS_PER_YEAR
from abm.disclosure.harness import CrossSectionMarket
from abm.disclosure.market import CrossSectionBook
from abm.disclosure.validate import validate_market
from abm.manifest import canonical_json_bytes, sha256_file
from abm.msm import MOMENT_NAMES, compute_moments
from abm.platform_tuning import disable_power_throttling

CORE = (
    "src/abm/__init__.py", "src/abm/disclosure/__init__.py",
    "src/abm/disclosure/config.py", "src/abm/disclosure/firms.py",
    "src/abm/disclosure/investors.py", "src/abm/disclosure/market.py",
    "src/abm/disclosure/harness.py", "src/abm/disclosure/validate.py",
    "src/abm/manifest.py", "src/abm/schemas.py", "src/abm/msm.py",
    "src/abm/french49.py", "src/abm/platform_tuning.py",
)


def hashes():
    return {name: sha256_file(ROOT / name) for name in CORE}


def serializable(value):
    if isinstance(value, np.ndarray):
        return serializable(value.tolist())
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serializable(item) for item in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def write_json(path, payload):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(serializable(payload), ensure_ascii=False, indent=2,
                                    allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def distribution(values):
    finite = np.asarray(values)[np.isfinite(values)]
    return {"count": int(np.size(values)), "finite_count": int(finite.size),
            "mean": float(finite.mean()) if finite.size else None,
            "sd": float(finite.std(ddof=1)) if finite.size > 1 else None,
            "positive_count": int((finite > 0).sum()),
            "quantiles": dict(zip(("minimum", "p05", "p25", "median", "p75", "p95", "maximum"),
                                   np.quantile(finite, (0, .05, .25, .5, .75, .95, 1)).tolist())) if finite.size else None}


def memory_equivalence():
    config = MarketConfig(n_firms=3, n_investors=2, trading_days=10, burn_in_days=0,
                          order_flow_memory=1.0)
    book = CrossSectionBook.initialize(config, .001)
    transient = np.zeros(3)
    maximum_error = 0.0
    for flow in (np.array([.001, -.002, .003]), np.array([-.003, .002, .001]),
                 np.zeros(3), np.array([.002, .001, -.003])):
        moves, capped = book.price_moves(flow, np.ones(3), np.zeros(3), np.zeros(3))
        impact = config.price_impact * flow / config.liquidity_fraction
        updated = config.transient_impact_decay * transient + (1 - config.permanent_impact_fraction) * impact / book.depth_fraction
        expected = config.permanent_impact_fraction * impact + updated - transient
        maximum_error = max(maximum_error, float(np.max(np.abs(moves - expected))))
        assert not capped.any() and np.array_equal(book.expected_flow_impact, np.zeros(3))
        assert np.allclose(moves, expected, rtol=0, atol=1e-15)
        transient = updated
    return {"status": "PASS", "source": "src/abm/disclosure/market.py:34-93",
            "maximum_quote_error": maximum_error,
            "statement": "E0=0 and memory=1 imply Et=0; surprise equals flow/depth. Transient state still decays at the unchanged coefficient.",
            "probe_scope": "Four deterministic book updates; no additional full-market simulation."}


def freeze():
    target_path = ROOT / "reports/msm_v1_20261011/target_train.json"
    target = json.loads(target_path.read_text(encoding="utf-8"))
    assert target["moment_names"] == list(MOMENT_NAMES)
    candidates = {"baseline": {}, "rebalance_025": {"rebalance_speed": .25},
                  "expected_flow_fixed_zero": {"order_flow_memory": 1.0}}
    base = MarketConfig(n_investors=1000, n_firms=200, trading_days=3500, burn_in_days=1000)
    payload = {
        "schema_version": 1, "purpose": "development_candidate_diagnostic",
        "created_at_utc": datetime.now(UTC).isoformat(), "maximum_market_attempts": 18,
        "seeds": list(range(61001, 61007)), "candidates": candidates,
        "trials": [{"candidate": name, "seed": seed,
                    "config": replace(base, seed=seed, **overrides).to_dict()}
                   for seed in range(61001, 61007) for name, overrides in candidates.items()],
        "selection_rule": "No automatic winner, no parameter/default/source changes, no added or replacement seeds/runs. Preserve every failed/interrupted attempt; never use survivor means as acceptance.",
        "core_gate": "Every seed and every asset: finite positive prices/values, zero caps, relative cash and maximum absolute per-asset share errors <=1e-8, all nine finite moments, kurtosis>0 and abs-return ACF1>0. Empirical acceptance remains pending.",
        "return_definition": "Simple price returns expm1(diff(log(price))), 2500 observations after 1000-day burn-in; dividends excluded from return moments but included in cash reconstruction.",
        "moment_names": list(MOMENT_NAMES), "source_hashes": hashes(),
        "source_scope": "M1 execution, validation, moments, hashing and process tuning dependencies; unused Stage1 implementations and disclosure game/metrics/report/experiment sources are not core drift gates.",
        "script_sha256": sha256_file(Path(__file__)),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": version("scipy"), "blas_threads": 1},
        "memory_equivalence": memory_equivalence(),
        "target": {"path": target_path.relative_to(ROOT).as_posix(),
                   "sha256": sha256_file(target_path), "data": target,
                   "nature": "Existing training target, previously used to fit seven M1 defaults; deliberately reused for comparable development diagnostics. Not untouched/held-out data.",
                   "provenance": "French49 29 training industries, 6539 daily observations, 2000-2025; cached target created by abm.msm empirical_target with circular-block bootstrap defaults (block20, draws200, seed20261011). No empirical target is recomputed.",
                   "unit_limitation": "French49 observations are SIC industry portfolios; model assets are interpreted as single companies. Averaging company-asset moments is not portfolio construction or individual-stock empirical calibration.",
                   "official_source": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html",
                   "score_limitation": "Original target SEs describe 6539-day industry histories, not this 2500-day company panel. Normalized deviations/J are descriptive legacy diagnostics, not calibrated significance tests or release gates. Old M1 fit used 40 sampled assets, this comparison uses all 200."},
        "sealed_data_access": "Only the cached target_train.json is loaded; no raw empirical dataset, validation/test target, sealed test execution or formal 20261101..20261130 seeds are used.",
    }
    payload["freeze_id"] = hashlib.sha256(canonical_json_bytes(payload)).hexdigest()
    path = DIRECTORY / "freeze.json"
    if path.exists():
        raise FileExistsError(path)
    write_json(path, payload)


def run_trial(trial, frozen):
    record = {**trial, "freeze_id": frozen["freeze_id"], "status": "running",
              "source_hashes_before": hashes(), "script_sha256": sha256_file(Path(__file__))}
    path = DIRECTORY / f"trial_{trial['candidate']}_{trial['seed']}.json"
    write_json(path, record)
    config = MarketConfig.from_dict(trial["config"])
    started = time.perf_counter()
    market = None
    try:
        market = CrossSectionMarket(config)
        result = market.run()
        record["simulation_seconds"] = time.perf_counter() - started
        returns = np.expm1(result.log_returns())
        moments = np.asarray([compute_moments(returns[:, asset]) for asset in range(config.n_firms)])
        validation = validate_market(result, config, return_acf_target=frozen["target"]["data"]["moments"][2])
        dividend_path = config.cash_flow_yield * result.intrinsic_values[1:].sum(axis=1) / TRADING_DAYS_PER_YEAR
        expected_cash = result.total_cash[0] + np.r_[0., np.cumsum(dividend_path)]
        errors = np.abs(result.total_cash - expected_cash) / np.abs(expected_cash)
        record.update({"status": "complete", "result_fingerprint": result.fingerprint(),
                       "validation": validation, "per_asset_moments": moments,
                       "mean_moments": moments.mean(axis=0),
                       "per_asset_moment_distributions": {name: distribution(moments[:, index])
                                                          for index, name in enumerate(MOMENT_NAMES)},
                       "cash_relative_error_by_day": errors,
                       "maximum_absolute_share_error_by_day": result.maximum_share_error,
                       "price_cap_hits_by_day": result.price_cap_hits,
                       "maximum_absolute_log_mispricing": float(np.max(np.abs(np.log(result.prices / result.intrinsic_values)))),
                       "final_expected_flow_max_abs": float(np.max(np.abs(market.book.expected_flow_impact))),
                       "final_transient_impact_max_abs": float(np.max(np.abs(market.book.transient_impact)))})
    except Exception as error:
        record.update({"status": "failed", "error_type": type(error).__name__, "error": str(error),
                       "simulation_seconds": time.perf_counter() - started,
                       "completed_days": market.next_day_index if market is not None else 0})
    record["source_hashes_after"] = hashes()
    record["core_sources_unchanged"] = record["source_hashes_before"] == record["source_hashes_after"] == frozen["source_hashes"]
    if not record["core_sources_unchanged"]:
        record["status"] = "source_drift"
    record["total_diagnostic_seconds"] = time.perf_counter() - started
    write_json(path, record)
    print(json.dumps({"candidate": trial["candidate"], "seed": trial["seed"], "status": record["status"],
                      "seconds": round(record["simulation_seconds"], 3)}), flush=True)
    return record


def summarize(frozen, records, power_tuning):
    target = np.asarray(frozen["target"]["data"]["moments"])
    se = np.asarray(frozen["target"]["data"]["standard_errors"])
    groups = {}
    for name in frozen["candidates"]:
        rows = [row for row in records if row["candidate"] == name]
        complete = len(rows) == 6 and all(row["status"] == "complete" for row in rows)
        gate = complete and all(row["core_sources_unchanged"] and all(
            row["validation"][key]["status"] == "PASS" for key in ("mechanical", "stylized")) for row in rows)
        group = {"planned_seeds": 6, "completed_seeds": sum(row["status"] == "complete" for row in rows),
                 "all_trials_core_pass": bool(gate), "empirical_acceptance": "pending",
                 "failed_or_interrupted_seeds": [row["seed"] for row in rows if row["status"] != "complete"]}
        if complete:
            means = np.asarray([row["mean_moments"] for row in rows])
            standardized = (means.mean(axis=0) - target) / (se * np.sqrt(1 + 1 / len(rows)))
            group.update({"mean_moments": means.mean(axis=0), "between_seed_sd": means.std(axis=0, ddof=1),
                          "legacy_train_standardized_deviations": standardized,
                          "legacy_train_j": float(standardized @ standardized),
                          "maximum_relative_cash_error": max(row["validation"]["mechanical"]["maximum_relative_cash_error"] for row in rows),
                          "maximum_absolute_share_error": max(row["validation"]["mechanical"]["maximum_absolute_share_error"] for row in rows),
                          "total_price_cap_hits": sum(row["validation"]["mechanical"]["price_cap_hits"] for row in rows),
                          "all_seed_asset_distributions": {moment: distribution(np.concatenate([
                              np.asarray(row["per_asset_moments"])[:, index] for row in rows]))
                                                           for index, moment in enumerate(MOMENT_NAMES)},
                          "simulation_seconds": distribution([row["simulation_seconds"] for row in rows])})
        groups[name] = group
    baseline = {row["seed"]: row for row in records if row["candidate"] == "baseline"}
    paired = {}
    for name in ("rebalance_025", "expected_flow_fixed_zero"):
        rows = [row for row in records if row["candidate"] == name]
        if len(rows) == 6 and all(row["status"] == baseline[row["seed"]]["status"] == "complete" for row in rows):
            differences = np.asarray([np.asarray(row["mean_moments"]) - baseline[row["seed"]]["mean_moments"] for row in rows])
            paired[name] = {"seeds": [row["seed"] for row in rows], "per_seed_differences": differences,
                            "mean_difference": differences.mean(axis=0), "sd_difference": differences.std(axis=0, ddof=1)}
        else:
            paired[name] = {"status": "incomplete", "mean_difference": None}
    summary = {"freeze_id": frozen["freeze_id"], "purpose": frozen["purpose"],
               "attempted_market_runs": len(records), "maximum_market_attempts": 18,
               "source_hashes_after": hashes(), "core_sources_unchanged": hashes() == frozen["source_hashes"],
               "script_sha256": sha256_file(Path(__file__)), "power_throttling_disabled": power_tuning,
               "selection": "none", "default_parameters_changed": False, "empirical_acceptance": "pending",
               "moment_names": list(MOMENT_NAMES), "target": frozen["target"],
               "groups": groups, "paired_against_baseline": paired,
               "trial_files": [{"candidate": row["candidate"], "seed": row["seed"], "status": row["status"],
                                "path": f"trial_{row['candidate']}_{row['seed']}.json",
                                "sha256": sha256_file(DIRECTORY / f"trial_{row['candidate']}_{row['seed']}.json")}
                               for row in records]}
    write_json(DIRECTORY / "results.json", summary)
    lines = ["# M1 三候选开发诊断（2026-10-11）", "",
             "固定三候选 × 六开发种子61001–61006；1000投资者、200资产、3500日含1000日预热。仅开发诊断，不自动选胜者，未改源码或默认参数。", "",
             f"冻结身份：`{frozen['freeze_id']}`。18次边界内尝试数：{len(records)}；运行前后核心源码一致：{summary['core_sources_unchanged']}。", "",
             "order_flow_memory=1 从零初始化使预期流恒零，等价于去掉暂时通道的预期流扣除；transient decay 仍保留，四步确定性报价对照通过。", "",
             "| 候选 | 完成种子 | 全种子/全资产核心门槛 | 开发诊断J | 收益ACF1均值 | 峰度均值 | 绝对收益ACF1均值 | cap总数 |", "|---|---:|---|---:|---:|---:|---:|---:|"]
    for name, group in groups.items():
        if "mean_moments" in group:
            mean = group["mean_moments"]
            lines.append(f"| {name} | {group['completed_seeds']}/6 | {group['all_trials_core_pass']} | {group['legacy_train_j']:.4f} | {mean[2]:.6f} | {mean[1]:.6f} | {mean[3]:.6f} | {group['total_price_cap_hits']} |")
        else:
            lines.append(f"| {name} | {group['completed_seeds']}/6 | False | incomplete | — | — | — | — |")
    lines.extend(["", "| 矩 | 训练目标 | baseline | rebalance=.25 | 预期流恒零 |", "|---|---:|---:|---:|---:|"])
    for index, name in enumerate(MOMENT_NAMES):
        values = [f"{groups[candidate]['mean_moments'][index]:.6g}" if "mean_moments" in groups[candidate] else "incomplete" for candidate in groups]
        lines.append(f"| {name} | {target[index]:.6g} | {' | '.join(values)} |")
    lines.extend(["", "逐种子全部200资产的九矩、峰度/绝对收益ACF/收益ACF分布、全程现金误差、股份最大误差及每日cap在trial_*.json；跨种子差值、完整九矩及其标准化偏差在results.json。核心门槛逐资产逐种子取AND，均值和较低J均不等于验收。", "",
                  "训练目标已被用于拟合默认参数，本轮明确复用，不声称目标未触碰。它含6539日，当前模拟仅2500个收益；原bootstrap标准误不能直接充当本轮严格显著性门槛。诊断J沿用(diagonal SE × sqrt(1+1/6))归一公式，仅供描述；旧M1校准抽取40资产，本轮检查全部200资产，J也不能直接当作同样样本设计的复验。", "",
                  "[French官方说明](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html)将股票按SIC划入行业组合。当前模型资产被解释为公司，平均公司收益矩不是行业组合矩；九矩接近也不证明个股市场实证校准。后续需要匹配个股数据，或事先明确模拟组合构造与相同收益口径。", "",
                  "没有运行正式20261101–20261130种子，没有执行sealed empirical test，未重新读取原始经验数据计算目标。每项失败/中断保留且不补跑。运行时间在其他开发任务可并发的环境中测量，不作为隔离性能基准。", "",
                  "冻结选择规则为none；不按单个ACF或最小J替换默认值。任何后续机制选择仍需兼顾全部矩、逐资产稳定性与独立验证，并重新核验M2需求收益、零偏好控制及政策比较。", "",
                  "复现：先保留现有目录；在匹配freeze.json的源码与环境下复制本目录的freeze.json和reproduce.py到同层级的新输出目录，执行现有venv Python -B reproduce.py。脚本对已有trial文件只核验并跳过，running/failed记录不会自动重跑。"])
    (DIRECTORY / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-only", action="store_true")
    args = parser.parse_args()
    if args.freeze_only:
        freeze()
        return
    frozen = json.loads((DIRECTORY / "freeze.json").read_text(encoding="utf-8"))
    identity = {key: value for key, value in frozen.items() if key != "freeze_id"}
    assert hashlib.sha256(canonical_json_bytes(identity)).hexdigest() == frozen["freeze_id"]
    assert hashes() == frozen["source_hashes"] and sha256_file(Path(__file__)) == frozen["script_sha256"]
    assert platform.python_version() == frozen["environment"]["python"] and np.__version__ == frozen["environment"]["numpy"]
    assert version("scipy") == frozen["environment"]["scipy"]
    assert len(frozen["trials"]) == frozen["maximum_market_attempts"] == 18
    assert sha256_file(ROOT / frozen["target"]["path"]) == frozen["target"]["sha256"]
    power_tuning = disable_power_throttling()
    records = []
    for trial in frozen["trials"]:
        assert hashes() == frozen["source_hashes"]
        path = DIRECTORY / f"trial_{trial['candidate']}_{trial['seed']}.json"
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            assert record["freeze_id"] == frozen["freeze_id"] and record["config"] == trial["config"]
        else:
            record = run_trial(trial, frozen)
        records.append(record)
    summarize(frozen, records, power_tuning)


if __name__ == "__main__":
    main()
