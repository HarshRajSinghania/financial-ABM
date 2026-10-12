"""One frozen development run and an explicit synthetic-basket observation operator."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import platform
import sys
import time
import traceback
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path

for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[name] = "1"

DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[1]
PROCESSED = ROOT / "data/processed/disclosure_market_public_20261011"
sys.path.insert(0, str(ROOT / "src"))

import numpy as np

from abm.disclosure.config import MarketConfig, TRADING_DAYS_PER_YEAR
from abm.disclosure.harness import CrossSectionMarket, CrossSectionResult
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


def clean(value):
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def write_json(path, payload):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(clean(payload), ensure_ascii=False, indent=2,
                                    allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def freeze():
    path = DIRECTORY / "freeze.json"
    if path.exists():
        raise FileExistsError("freeze already exists; it cannot be replaced")
    target_path = ROOT / "reports/msm_v1_20261011/target_train.json"
    target = json.loads(target_path.read_text(encoding="utf-8"))
    assert target["moment_names"] == list(MOMENT_NAMES)
    config = MarketConfig(seed=61001, n_investors=1000, n_firms=200,
                          trading_days=1000 + target["observations"], burn_in_days=1000)
    groups = np.array_split(np.random.default_rng(61729).permutation(config.n_firms), 29)
    payload = {
        "schema_version": 1, "created_at_utc": datetime.now(UTC).isoformat(),
        "purpose": "development_observation_operator_check_not_empirical_calibration",
        "maximum_market_attempts": 1, "config": config.to_dict(),
        "mapping_seed": 61729, "baskets": [group.tolist() for group in groups],
        "mapping_rule": "Fixed independent permutation, split into 29 anonymous baskets; no target values, simulated outcomes or SIC labels used to choose membership. Company IDs are zero-based.",
        "selection_rule": "No parameter, mapping or seed selection; preserve failures and interruptions, no replacement run.",
        "return_definition": {
            "dividend": "D[t,i] = cash_flow_yield * intrinsic_values[t,i] / 252, paid after day-t trading to day-t holders",
            "company_total": "(P[t,i] - P[t-1,i] + D[t,i]) / P[t-1,i]",
            "basket_total": "sum_i_in_basket(P[t,i] - P[t-1,i] + D[t,i]) / sum_i_in_basket(P[t-1,i])",
            "weights": "Prior-close market-cap weights; one model share per company; fixed membership. Gross daily returns with same-day reinvestment for a chained total-return index, excluding investor transaction costs.",
            "measurement_days": [config.burn_in_days + 1, config.trading_days],
        },
        "core_gate": "Every company and every day: finite positive prices and intrinsic values, zero caps, relative cash and maximum absolute company-share errors <= 1e-8. Per-series moments, kurtosis and absolute-return ACF are reported individually; no empirical fit threshold.",
        "source_hashes": hashes(), "script_sha256": sha256_file(Path(__file__)),
        "source_scope": "Actual M1 market, validation, moment, hashing and process-tuning dependencies. Unused disclosure game/metrics/report/experiments sources excluded.",
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": version("scipy"), "blas_threads": 1},
        "target": {"path": target_path.relative_to(ROOT).as_posix(),
                   "sha256": sha256_file(target_path), "data": target,
                   "role": "Previously used training target, not untouched evaluation data. 29 French SIC industry value-weighted portfolios, 6539 daily observations, 2000-01-03 through 2025-12-31; original raw data and validation/test targets are not re-read.",
                   "source": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html"},
    }
    payload["freeze_id"] = hashlib.sha256(canonical_json_bytes(payload)).hexdigest()
    write_json(path, payload)


def basket_returns(prices, dividends, groups):
    price = np.column_stack([np.diff(prices[:, group], axis=0).sum(axis=1)
                             / prices[:-1, group].sum(axis=1) for group in groups])
    total = price + np.column_stack([dividends[:, group].sum(axis=1)
                                     / prices[:-1, group].sum(axis=1) for group in groups])
    return price, total


def operator_checks():
    prices = np.array([[10., 20., 30.], [11., 18., 33.], [12., 19., 32.]])
    dividends = np.array([[.1, .2, .3], [.2, .1, .4]])
    price, total = basket_returns(prices, dividends, [[0, 2], [1]])
    expected = np.array([[(44. + .4) / 40. - 1., (18. + .2) / 20. - 1.],
                         [(44. + .6) / 44. - 1., (19. + .1) / 18. - 1.]])
    assert np.allclose(total, expected, rtol=0, atol=3e-16)
    weights = prices[:-1, [0, 2]] / prices[:-1, [0, 2]].sum(axis=1)[:, None]
    firm_total = (np.diff(prices, axis=0) + dividends) / prices[:-1]
    error = float(np.max(np.abs((weights * firm_total[:, [0, 2]]).sum(axis=1) - total[:, 0])))
    assert error < 3e-16 and np.allclose(price[:, 1], np.diff(prices[:, 1]) / prices[:-1, 1])
    return {"status": "PASS", "scope": "Hand-calculated two-day, three-company accounting fixture; not another market simulation", "maximum_weight_identity_error": error}


def dividend_probe(market):
    probe = copy.deepcopy(market)
    prices, values = probe.prices.copy(), probe.firms.intrinsic_value.copy()
    before = probe._total_cash()
    expected = probe.config.cash_flow_yield * values / TRADING_DAYS_PER_YEAR
    investor_cash = probe.investors.cash.copy()
    probe._pay_dividends()
    investor_error = float(np.max(np.abs(probe.investors.cash - investor_cash - probe.investors.holdings @ expected)))
    cash_error = abs(probe._total_cash() - before - expected.sum())
    assert np.array_equal(prices, probe.prices) and np.array_equal(values, probe.firms.intrinsic_value)
    assert cash_error / abs(before) < 1e-12 and investor_error < 1e-10
    return {"status": "PASS", "scope": "One payment on a deep copy of the completed market; original run and its RNG are untouched",
            "per_share_dividend": expected, "price_unchanged": bool(np.array_equal(prices, probe.prices)),
            "intrinsic_value_unchanged": bool(np.array_equal(values, probe.firms.intrinsic_value)),
            "maximum_investor_cash_absolute_error": investor_error,
            "aggregate_cash_absolute_error": float(cash_error),
            "payment_timing": "Day-t intrinsic values, after day-t trading; no separate record, ex-dividend or payment dates",
            "economic_interpretation": "Payment explicitly injects external cash and has no mechanical ex-dividend price/value reduction. P-change plus D is the accounting total return of this model, but correct cum/ex-dividend valuation and possible economic double counting remain unresolved; absence of an explicit price drop alone does not prove double counting."}


def series_summary(returns, target):
    moments = np.array([compute_moments(returns[:, index]) for index in range(returns.shape[1])])
    mean = moments.mean(axis=0)
    distributions = {name: {"finite_count": int(np.isfinite(moments[:, index]).sum()),
                            "minimum": float(moments[:, index].min()), "median": float(np.median(moments[:, index])),
                            "maximum": float(moments[:, index].max()),
                            "quantile_05": float(np.quantile(moments[:, index], .05)),
                            "quantile_95": float(np.quantile(moments[:, index], .95))}
                     for index, name in enumerate(MOMENT_NAMES)}
    per_series = [{"series_id": index, "moments": row, "finite_nine_moments": bool(np.all(np.isfinite(row))),
                   "positive_excess_kurtosis": bool(row[1] > 0), "positive_abs_return_acf_1": bool(row[3] > 0)}
                  for index, row in enumerate(moments)]
    return {"series_count": returns.shape[1], "observations_per_series": returns.shape[0],
            "per_series": per_series, "distributions": distributions, "mean_moments": mean,
            "difference_from_training_mean": mean - np.array(target["moments"]),
            "difference_over_old_training_se_descriptive_only": (mean - np.array(target["moments"])) / np.array(target["standard_errors"]),
            "all_series_finite_nine_moments": all(row["finite_nine_moments"] for row in per_series),
            "all_series_positive_excess_kurtosis": all(row["positive_excess_kurtosis"] for row in per_series),
            "all_series_positive_abs_return_acf_1": all(row["positive_abs_return_acf_1"] for row in per_series)}


def analyze(frozen, record):
    path = ROOT / record["simulation_file"]
    assert sha256_file(path) == record["simulation_sha256"]
    with np.load(path, allow_pickle=False) as saved:
        result = CrossSectionResult(burn_in_days=frozen["config"]["burn_in_days"],
                                    **{name: saved[name] for name in saved.files})
    config = MarketConfig.from_dict(frozen["config"])
    groups = frozen["baskets"]
    assert sorted(index for group in groups for index in group) == list(range(config.n_firms))
    dividends = config.cash_flow_yield * result.intrinsic_values[1:] / TRADING_DAYS_PER_YEAR
    price, total = basket_returns(result.prices, dividends, groups)
    company_price = np.diff(result.prices, axis=0) / result.prices[:-1]
    company_total = company_price + dividends / result.prices[:-1]
    weighted_total = np.column_stack([(company_total[:, group] * result.prices[:-1, group]).sum(axis=1)
                                     / result.prices[:-1, group].sum(axis=1) for group in groups])
    operator_error = float(np.max(np.abs(weighted_total - total)))
    assert operator_error < 1e-14
    start = config.burn_in_days
    expected_cash = result.total_cash[0] + np.r_[0., np.cumsum(dividends.sum(axis=1))]
    cash_error = np.abs(result.total_cash - expected_cash) / np.abs(expected_cash)
    processed = PROCESSED / "basket_returns_61001.npz"
    with processed.with_suffix(".npz.tmp").open("wb") as stream:
        np.savez_compressed(stream, day=np.arange(start + 1, config.trading_days + 1),
                            price_returns=price[start:], total_returns=total[start:],
                            market_cap_before=np.column_stack([result.prices[:-1, group].sum(axis=1) for group in groups])[start:])
    processed.with_suffix(".npz.tmp").replace(processed)
    definitions = {"company_price": company_price, "company_total": company_total,
                   "basket_price": price, "basket_total": total}
    summary = {"freeze_id": frozen["freeze_id"], "status": "completed_development_diagnostic",
               "empirical_calibration": "pending", "maximum_market_attempts": 1, "attempted_market_runs": 1,
               "source_hashes_after": hashes(), "core_sources_unchanged": hashes() == frozen["source_hashes"],
               "script_sha256": sha256_file(Path(__file__)), "market_record": record,
               "target": frozen["target"], "moment_names": list(MOMENT_NAMES), "baskets": groups,
               "mechanical_and_company_price_stylized": validate_market(result, config),
               "operator_fixture": operator_checks(), "maximum_full_path_weight_identity_error": operator_error,
               "dividend_timing_check": {"all_days_reconstructed_cash_relative_error_maximum": float(cash_error.max()),
                                         "measurement_first_payment_day": start + 1, "measurement_last_payment_day": config.trading_days,
                                         "ex_dividend_probe": record["dividend_probe"]},
               "return_summaries": {name: series_summary(values[start:], frozen["target"]["data"])
                                    for name, values in definitions.items()},
               "processed_returns": {"path": processed.relative_to(ROOT).as_posix(), "sha256": sha256_file(processed)},
               "limitations": ["Anonymous 6-7-company synthetic baskets have no SIC exposure structure, economic sector shocks or matching sector membership; equal basket counts do not make these French industries.",
                               "The old target already fitted defaults. Differences in old bootstrap-SE units are descriptive, not new z-tests or acceptance gates; one reused development seed is not independent validation.",
                               "No firm entry, exit, delisting, splits or dynamic shares; model survivorship is structural. French portfolios have real constituent sizes and annual SIC reclassification.",
                               "Market dividends are external daily transfers with no explicit ex-dividend price or intrinsic-value reduction. Accounting total-return construction does not solve the economic payout/valuation definition.",
                               "Neither target mapping nor parameters selected, no raw French data or sealed holdout read, no formal seeds run."]}
    assert summary["core_sources_unchanged"]
    write_json(DIRECTORY / "results.json", summary)
    lines = ["# M1 公开数据与组合观察口径（开发诊断）", "",
             "保留200家模拟公司，固定随机分组为29个匿名 synthetic basket；不将这些篮子称为SIC行业。仅开发种子61001，1000投资者，7539日含1000日预热，6539个测量收益。没有校准、改默认值、选择分组或运行正式种子/保留检验。", "",
             "每个篮子收益用前一日市值作权重：sum(P[t]−P[t−1]+D[t])/sum(P[t−1])，D[t]=0.05×V[t]/252。股息归当日交易后的持有人；链式总收益指数采用当日再投资，忽略交易费用。同时保留纯价格收益作为诊断。", "",
             "[French官方说明](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html)按SIC把真实上市公司归入行业组合。当前模型没有行业暴露结构、行业冲击或年度行业重构，每篮子仅6–7家公司；这项工作修正了‘先聚合收益再算矩’的观察操作，仍未建立经验行业可比性。", "",
             f"冻结身份：`{frozen['freeze_id']}`。核心依赖前后相同：{summary['core_sources_unchanged']}；市场运行耗时 {record['elapsed_seconds']:.3f} 秒。机械门槛：{summary['mechanical_and_company_price_stylized']['mechanical']['status']}，公司价格风格门槛：{summary['mechanical_and_company_price_stylized']['stylized']['status']}；经验校准仍为 pending。", "",
             "| 矩 | 旧训练目标 | 公司价格均值 | 公司含股息均值 | 篮子价格均值 | 篮子含股息均值 |", "|---|---:|---:|---:|---:|---:|"]
    for index, name in enumerate(MOMENT_NAMES):
        values = [summary["return_summaries"][key]["mean_moments"][index] for key in definitions]
        lines.append(f"| {name} | {frozen['target']['data']['moments'][index]:.6g} | " + " | ".join(f"{value:.6g}" for value in values) + " |")
    lines.extend(["", "全部200家公司及29个篮子的九矩、各系列门槛和分布保存在results.json；不以均值替代逐系列检查，未给任意经验门槛。旧目标为已参与拟合的29个行业训练目标；旧bootstrap标准误归一差值仅描述，不能当新显著性检验。", "",
                  f"全程现金重建最大相对误差 {cash_error.max():.3g}，股份最大绝对误差 {np.max(result.maximum_share_error):.3g}，价格cap合计 {result.price_cap_hits.sum()}；全路径两种篮子公式最大误差 {operator_error:.3g}。", "",
                  "股息检查：复制完成市场后单独支付一次，价格和内在价值均未改变；现金增加与当日V/252口径一致。源码的支付时钟没有单独记录日、除息日与到账日。外生分红没有显式扣除企业价值，因此经济层面的分红/估值闭合与潜在重复计入收益仍未解决；单凭没有机械除息下跌也不能证明重复计入。当前‘价格变化+股息’只忠实描述模型持有人得到的会计收益。", "",
                  "模拟公司全程存在，无上市、退市或股份变动，具有结构性幸存者限制。匿名小篮子和真实行业规模、行业冲击不同；篮子矩接近或远离训练目标均不能证明个股市场校准通过/失败。后续应先固定个股数据及筛选规则，或建立可解释的模拟行业结构，再冻结新的校准与留出设计。", "",
                  "复现使用现有venv运行本目录reproduce_baskets.py：--freeze-only仅创建新冻结；默认读取冻结，已有completed记录只重做观察操作，不再模拟；running/failed记录停止。--analyze-saved强制只读取已存模拟路径。原始模拟路径与两种篮子收益在data/processed/disclosure_market_public_20261011，可独立重算。来源许可与候选个股数据核查另见public_sources.json/public_sources.md。"])
    (DIRECTORY / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-only", action="store_true")
    parser.add_argument("--analyze-saved", action="store_true")
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
    assert sha256_file(ROOT / frozen["target"]["path"]) == frozen["target"]["sha256"]
    record_path = DIRECTORY / "market_attempt_61001.json"
    if record_path.exists():
        record = json.loads(record_path.read_text(encoding="utf-8"))
        assert record["freeze_id"] == frozen["freeze_id"] and record["status"] == "completed"
    else:
        if args.analyze_saved:
            raise FileNotFoundError("No saved completed market attempt")
        PROCESSED.mkdir(parents=True, exist_ok=True)
        record = {"freeze_id": frozen["freeze_id"], "config": frozen["config"], "status": "running",
                  "started_at_utc": datetime.now(UTC).isoformat(), "power_throttling_disabled": disable_power_throttling()}
        write_json(record_path, record)
        started = time.perf_counter()
        try:
            market = CrossSectionMarket(MarketConfig.from_dict(frozen["config"]))
            result = market.run()
            record["elapsed_seconds"] = time.perf_counter() - started
            path = PROCESSED / "market_61001.npz"
            with path.with_suffix(".npz.tmp").open("wb") as stream:
                np.savez_compressed(stream, **{name: getattr(result, name) for name in result.__dataclass_fields__ if name != "burn_in_days"})
            path.with_suffix(".npz.tmp").replace(path)
            record.update(status="completed", simulation_file=path.relative_to(ROOT).as_posix(),
                          simulation_sha256=sha256_file(path), result_fingerprint=result.fingerprint(),
                          dividend_probe=dividend_probe(market), source_hashes_after=hashes())
            assert record["source_hashes_after"] == frozen["source_hashes"]
        except BaseException:
            record.update(status="failed", elapsed_seconds=time.perf_counter() - started, error=traceback.format_exc())
            write_json(record_path, record)
            raise
        write_json(record_path, record)
    analyze(frozen, record)


if __name__ == "__main__":
    main()
