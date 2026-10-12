"""Frozen finite-grid development matching to five already-inspected public stocks."""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import os
import platform
import sys
import time
import traceback
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
from abm.disclosure.harness import CrossSectionMarket, MAXIMUM_LOG_MISPRICING
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
LABELS = ("IBM", "Intel", "3M", "Microsoft", "Citigroup")
GRID = {"rebalance_speed": (.25, .375, .5), "order_flow_memory": (.3, .5, .7, .9),
        "noise_flow_scale": (.002, .003)}
SEEDS = (62001, 62002, 62003)
PUBLIC_PANEL = "data/processed/disclosure_market_public_20261011/tsay_five_company_daily_returns.csv"
PUBLIC_MANIFEST = "data/raw/disclosure_market_public_20261011/tsay_download_manifest.json"


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


def hashes():
    return {name: sha256_file(ROOT / name) for name in CORE}


def array_hash(values):
    values = np.ascontiguousarray(values)
    digest = hashlib.sha256(str(values.dtype).encode() + str(values.shape).encode())
    digest.update(values.tobytes())
    return digest.hexdigest()


def distribution(values):
    values = np.asarray(values)
    finite = values[np.isfinite(values)]
    return {"count": values.size, "finite_count": finite.size,
            "mean": float(finite.mean()) if finite.size else None,
            "positive_count": int((finite > 0).sum()),
            "quantiles": dict(zip(("min", "p05", "median", "p95", "max"),
                                   np.quantile(finite, (0, .05, .5, .95, 1)).tolist())) if finite.size else None}


def public_target():
    source = json.loads((ROOT / PUBLIC_MANIFEST).read_text(encoding="utf-8"))
    assert sha256_file(ROOT / PUBLIC_PANEL) == source["transformed_panel"]["sha256"]
    assert all(sha256_file(ROOT / item["path"]) == item["sha256"] for item in source["files"])
    with (ROOT / PUBLIC_PANEL).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    by = {label: {row["date"]: float(row["simple_total_return"]) for row in rows
                  if row["author_company_label"] == label} for label in LABELS}
    first, last = max(min(item) for item in by.values()), min(max(item) for item in by.values())
    dates = [day for day in by[LABELS[0]] if first <= day <= last]
    assert all([day for day in by[label] if first <= day <= last] == dates for label in LABELS)
    values = np.column_stack([[by[label][day] for day in dates] for label in LABELS])
    assert np.all(np.isfinite(values)) and np.all(values >= -1)
    moments = np.array([compute_moments(values[:, index]) for index in range(len(LABELS))])
    rng = np.random.default_rng(61731)
    draws, block_length, size = 200, 20, len(dates)
    samples = np.empty((draws, len(MOMENT_NAMES)))
    for draw in range(draws):
        starts = rng.integers(0, size, size=-(-size // block_length))
        index = ((starts[:, None] + np.arange(block_length)) % size).ravel()[:size]
        samples[draw] = np.mean([compute_moments(values[index, stock]) for stock in range(len(LABELS))], axis=0)
    covariance = np.cov(samples, rowvar=False)
    assert np.all(np.diag(covariance) > 0)
    cfg = MarketConfig()
    lower = float(np.expm1(-cfg.max_log_return))
    upper = float(np.expm1(cfg.max_log_return) + cfg.cash_flow_yield / TRADING_DAYS_PER_YEAR
                  * np.exp(MAXIMUM_LOG_MISPRICING + cfg.max_log_return))
    outside = [{"company": label, "date": dates[day], "return": float(values[day, stock])}
               for stock, label in enumerate(LABELS) for day in range(size)
               if values[day, stock] < lower or values[day, stock] > upper]
    return {"role": "Already-inspected five-stock development target, never untouched holdout",
            "source_panel": PUBLIC_PANEL, "source_panel_sha256": sha256_file(ROOT / PUBLIC_PANEL),
            "source_manifest": PUBLIC_MANIFEST, "source_manifest_sha256": sha256_file(ROOT / PUBLIC_MANIFEST),
            "raw_files": [{"path": row["path"], "sha256": row["sha256"]} for row in source["files"]],
            "license_and_sampling": {"license": source["license"], "sampling_limits": source["sampling_limits"]},
            "companies": list(LABELS), "first_date": first, "last_date": last, "dates": dates,
            "observations_per_company": size, "total_company_days": size * len(LABELS),
            "window_rule": "Latest first date and earliest last date across the preselected five files. Require identical observed trading-date lists in that interval; no deletion, imputation or winsorization.",
            "return_definition": "Decimal simple daily total returns including dividends, per Tsay Chapter 1 section 1.2.5 and Table 1.2; original second-column values, no extra dividends or adjustment",
            "observation_operator": "Compute all nine moments separately for each company, then take the equal-company mean; never compute moments of a pooled series or a stock basket",
            "moment_names": list(MOMENT_NAMES), "per_company_moments": moments, "mean_moments": moments.mean(axis=0),
            "per_company_mean_return": values.mean(axis=0), "covariance": covariance,
            "standard_errors": np.sqrt(np.diag(covariance)),
            "bootstrap": {"draws": draws, "block_length_trading_days": block_length, "seed": 61731,
                          "method": "Circular time-block resampling with the same date index for all five stocks, preserving same-day cross-company dependence; conditional on these selected firms. Only descriptive scaling, no confidence/acceptance test."},
            "fixed_support_constraint": {"price_log_return_cap": cfg.max_log_return,
                                         "log_price_to_value_guard": MAXIMUM_LOG_MISPRICING,
                                         "holder_total_return_lower_bound": lower, "holder_total_return_upper_bound": upper,
                                         "derivation": "D>=0 gives r_total>=exp(-c)-1; |log(P[t]/V[t])|<=g gives D/P[t-1]<=(yield/252)*exp(g+c). Bound applies to days satisfying the model guard, and is deliberately loose.",
                                         "observations_outside_support": outside,
                                         "interpretation": "Fixed-cap model cannot reproduce these four observations. This is a support mismatch, not a proof that nine summary moments cannot be approximately matched."}}


def candidate_id(overrides):
    return f"r{round(overrides['rebalance_speed'] * 1000):03d}_m{round(overrides['order_flow_memory'] * 100):02d}_n{round(overrides['noise_flow_scale'] * 100000):03d}"


def freeze():
    path = DIRECTORY / "freeze.json"
    if path.exists():
        raise FileExistsError("freeze already exists and cannot be overwritten")
    target = public_target()
    base = MarketConfig(n_investors=1000, n_firms=200, trading_days=1000 + target["observations_per_company"],
                        burn_in_days=1000)
    overrides = [dict(zip(GRID, values)) for values in itertools.product(*GRID.values())]
    baseline = {name: getattr(base, name) for name in GRID}
    overrides.sort(key=lambda item: item != baseline)
    candidates = [{"id": candidate_id(item), "overrides": item,
                   "configs": [replace(base, seed=seed, **item).to_dict() for seed in SEEDS]} for item in overrides]
    payload = {"schema_version": 1, "purpose": "exploratory_development_grid_not_empirical_acceptance",
               "created_at_utc": datetime.now(UTC).isoformat(), "grid": GRID, "seeds": SEEDS,
               "candidates": candidates, "candidate_count": 24, "maximum_market_attempts": 72,
               "baseline_candidate": candidate_id(baseline), "target": target,
               "source_hashes": hashes(), "script_sha256": sha256_file(Path(__file__)),
               "source_scope": "Thirteen bare-market, validator, moments, hash and process-tuning files. Parallel disclosure game/domain/financing/policy/metrics/report edits are not dependencies of these simulations.",
               "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": version("scipy"), "blas_threads": 1},
               "estimated_cost_before_run": {"basis": "Prior full-size 7539-day bare-market development run took 3.28 seconds of market time. Proportional 6592-day estimate plus moment/serialization overhead, concurrent machine load uncertain.",
                                             "estimated_market_seconds": 72 * 3.28 * base.trading_days / 7539,
                                             "estimated_total_minutes": [6, 10], "disk_megabytes_expected": [10, 50]},
               "mechanism_hypotheses": {"rebalance_speed": "Lower speed weakens synchronized portfolio adjustment and price-demand feedback; may change volatility and all ACF/tail moments.",
                                        "order_flow_memory": "Higher persistence slows the estimate subtracted from the transient order-flow channel. This changes lagged flow response; memory=1's fixed-zero expectation is outside this predeclared grid.",
                                        "noise_flow_scale": "1.5x baseline demand shock amplitude tests under-dispersion and tail/stability costs jointly with ACF; fixed Gaussian fundamentals and volatility-feedback parameters remain unchanged."},
               "return_definitions": {"price": "P[t]/P[t-1]-1; descriptive sensitivity only because the empirical data are total returns",
                                      "holder_total": "(P[t]-P[t-1]+cash_flow_yield*V[t]/252)/P[t-1]; current model's gross daily holder return including external cash; no invented ex-dividend price correction",
                                      "economic_limit": "V may be a continuing ex-dividend value anchor. Payment without mechanically reducing V/P is not by itself proof of double counting; payout/valuation economic interpretation is unestimated."},
               "acceptance_rules": {"mechanical": "Every candidate, seed, company and day: finite positive P/V, zero official price caps over burn-in and measurement, relative cash error and maximum absolute company-share error <=1e-8.",
                                    "stylized": "Every company in every completed seed: all nine finite moments, excess kurtosis>0, abs-return ACF1>0. Report price and holder-total separately; these are generic signs, not empirical calibration gates.",
                                    "empirical": "No empirical PASS, p-value or fitted-threshold gate. Report every nine-moment residual, every company distribution, seed variability and support mismatch. Five selected, already-seen stocks are a conditional development sample.",
                                    "descriptive_score": "Sum over nine moments of ((mean simulated per-company holder-total moment minus target mean) / fixed target time-bootstrap SE)^2. No chi-square interpretation, optimization, winner/default promotion or candidate selection. Monte Carlo SE from three seeds separately reported, not used to lower the score.",
                                    "failure": "Preserve running/failed/capped records and count them. No replacement runs/seeds, no survivor-mean acceptance. Any missing/failed seed makes candidate-level mean matching score unavailable.",
                                    "selection": "None. Full fixed grid, no adaptive search. Explicit illustrative configurations are selected before results, not winners."},
               "illustrative_candidates": ["r500_m30_n200", "r250_m30_n200", "r500_m70_n200", "r375_m70_n300"],
               "pairing": "Same seed and fixed non-grid parameters share firm/investor initialization and independent fundamental/noise RNG streams. Compare full intrinsic-value path hashes across completed candidates for each seed; failed/capped outcomes remain visible. Pairing is for this bare market, not a general promise for policy-game stochastic clocks.",
               "limits": ["Company units now match, but author-selected five large/long-lived historical stocks do not identify a representative 200-firm universe or its heterogeneity.",
                          "All five full histories already inspected. This matched common window is development data, not an untouched temporal or company holdout.",
                          "Three dev seeds reveal local Monte Carlo variability; they do not establish unique structural parameter identification or independent empirical validation.",
                          "Same-period shocks common to selected stocks, absent entry/exit/delisting and unknown permanent IDs remain limitations.",
                          "Fixed price support and external-dividend economic mapping cannot be repaired by tuning this grid."]}
    payload["freeze_id"] = hashlib.sha256(canonical_json_bytes(clean(payload))).hexdigest()
    write_json(path, payload)
    write_json(DIRECTORY / "target_public_five_stocks.json", target)


def run_trial(frozen, candidate, config):
    path = DIRECTORY / f"trial_{candidate['id']}_{config['seed']}.json"
    if path.exists():
        record = json.loads(path.read_text(encoding="utf-8"))
        assert record["freeze_id"] == frozen["freeze_id"] and record["config"] == config
        return record
    record = {"freeze_id": frozen["freeze_id"], "candidate": candidate["id"], "seed": config["seed"],
              "config": config, "status": "running", "started_at_utc": datetime.now(UTC).isoformat()}
    write_json(path, record)
    started = time.perf_counter()
    market = None
    try:
        cfg = MarketConfig.from_dict(config)
        market = CrossSectionMarket(cfg)
        result = market.run()
        market_seconds = time.perf_counter() - started
        validation = validate_market(result, cfg)
        price_moments = np.array([[asset["moments"][name] for name in MOMENT_NAMES]
                                  for asset in validation["moments_per_asset"]], dtype=float)
        price_returns = np.diff(result.prices, axis=0) / result.prices[:-1]
        dividend_yields = cfg.cash_flow_yield * result.intrinsic_values[1:] / TRADING_DAYS_PER_YEAR / result.prices[:-1]
        total_returns = price_returns + dividend_yields
        total_moments = np.array([compute_moments(total_returns[cfg.burn_in_days:, asset]) for asset in range(cfg.n_firms)])
        total_checks = {"finite_nine_moments": bool(np.all(np.isfinite(total_moments))),
                        "positive_excess_kurtosis_every_company": bool(np.all(total_moments[:, 1] > 0)),
                        "positive_abs_return_acf1_every_company": bool(np.all(total_moments[:, 3] > 0))}
        dividends = cfg.cash_flow_yield * result.intrinsic_values[1:].sum(axis=1) / TRADING_DAYS_PER_YEAR
        expected_cash = result.total_cash[0] + np.r_[0., np.cumsum(dividends)]
        cash_error = np.abs(result.total_cash - expected_cash) / np.abs(expected_cash)
        all_log_returns = result.log_returns(include_burn_in=True)
        artifact = path.with_suffix(".npz")
        with artifact.with_suffix(".npz.tmp").open("wb") as stream:
            np.savez_compressed(stream, price_moments=price_moments, holder_total_moments=total_moments,
                                day=np.arange(cfg.trading_days + 1), relative_cash_error=cash_error,
                                maximum_absolute_company_share_error=result.maximum_share_error,
                                price_caps_by_day=result.price_cap_hits,
                                maximum_absolute_log_price_return_by_company=np.max(np.abs(all_log_returns), axis=0),
                                log_price_boundary_touches_by_company=np.sum(np.abs(np.abs(all_log_returns) - cfg.max_log_return) < 1e-12, axis=0),
                                measured_minimum_price_return_by_company=price_returns[cfg.burn_in_days:].min(axis=0),
                                measured_maximum_price_return_by_company=price_returns[cfg.burn_in_days:].max(axis=0),
                                measured_minimum_holder_total_return_by_company=total_returns[cfg.burn_in_days:].min(axis=0),
                                measured_maximum_holder_total_return_by_company=total_returns[cfg.burn_in_days:].max(axis=0),
                                measured_mean_dividend_yield_by_company=dividend_yields[cfg.burn_in_days:].mean(axis=0))
        artifact.with_suffix(".npz.tmp").replace(artifact)
        record.update(status="completed", market_seconds=market_seconds,
                      completed_days=cfg.trading_days, artifact=artifact.name, artifact_sha256=sha256_file(artifact),
                      result_fingerprint=result.fingerprint(), intrinsic_value_path_sha256=array_hash(result.intrinsic_values),
                      mechanical=validation["mechanical"], price_stylized=validation["stylized"],
                      holder_total_stylized={"status": "PASS" if all(total_checks.values()) else "FAIL", "checks": total_checks},
                      cap_hits_full=int(result.price_cap_hits.sum()), cap_hits_burn_in=int(result.price_cap_hits[:cfg.burn_in_days + 1].sum()),
                      cap_hits_measurement=int(result.price_cap_hits[cfg.burn_in_days + 1:].sum()),
                      price_cap_boundary_touches_scope="Per-company absolute log-return boundary within 1e-12 is diagnostic; official clipped-raw counts are saved separately by day.",
                      maximum_absolute_log_mispricing=float(np.max(np.abs(np.log(result.prices / result.intrinsic_values)))),
                      price_mean_moments=price_moments.mean(axis=0), holder_total_mean_moments=total_moments.mean(axis=0),
                      price_moment_distributions={name: distribution(price_moments[:, index]) for index, name in enumerate(MOMENT_NAMES)},
                      holder_total_moment_distributions={name: distribution(total_moments[:, index]) for index, name in enumerate(MOMENT_NAMES)},
                      mean_company_price_return=float(price_returns[cfg.burn_in_days:].mean()),
                      mean_company_holder_total_return=float(total_returns[cfg.burn_in_days:].mean()),
                      mean_company_dividend_yield=float(dividend_yields[cfg.burn_in_days:].mean()),
                      raw_paths_saved=False, raw_path_reproduction="Re-execute exact config/seed with frozen core sources; all per-company nine moments and full-day ledger/cap diagnostics are saved in NPZ.")
    except BaseException as error:
        record.update(status="failed", completed_days=market.next_day_index if market is not None else 0,
                      exception_type=type(error).__name__, error=traceback.format_exc(),
                      cap_hits_full=None, mechanical={"status": "FAIL", "reason": "Simulation or diagnostics did not complete"})
        if market is not None:
            record["partial_diagnostics"] = {
                "completed_prefix_days": market.next_day_index,
                "cap_hits_observed_in_initialized_counters": int(market.price_cap_hits.sum()),
                "nonzero_cap_days": np.flatnonzero(market.price_cap_hits).tolist(),
                "current_prices": market.prices,
                "current_intrinsic_values": market.firms.intrinsic_value,
                "completed_prefix_total_cash": market.total_cash[:market.next_day_index + 1],
                "completed_prefix_maximum_absolute_company_share_error": market.maximum_share_error[:market.next_day_index + 1],
                "scope": "Completed prefix excludes the failing day; current state and initialized cap counters may include a partially executed failing day. Future cap-counter zero slots are not evidence of completion."}
        if isinstance(error, (KeyboardInterrupt, SystemExit)):
            raise
    finally:
        record["total_elapsed_seconds"] = time.perf_counter() - started
        record["source_hashes_after"] = hashes()
        record["core_sources_unchanged"] = record["source_hashes_after"] == frozen["source_hashes"]
        write_json(path, record)
    return record


def summarize(frozen, records):
    target = np.array(frozen["target"]["mean_moments"])
    se = np.array(frozen["target"]["standard_errors"])
    candidates = {}
    lookup = {(row["candidate"], row["seed"]): row for row in records}
    for candidate in frozen["candidates"]:
        trials = [lookup.get((candidate["id"], seed)) for seed in SEEDS]
        completed = [row for row in trials if row is not None and row["status"] == "completed"]
        group = {"overrides": candidate["overrides"], "scheduled_seeds": list(SEEDS),
                 "trial_statuses": {seed: row["status"] if row else "not_started" for seed, row in zip(SEEDS, trials)},
                 "completed_seeds": len(completed), "all_trials_completed": len(completed) == len(SEEDS),
                 "all_trials_mechanical_pass": len(completed) == len(SEEDS) and all(row["mechanical"]["status"] == "PASS" for row in completed),
                 "all_company_price_stylized_pass": len(completed) == len(SEEDS) and all(row["price_stylized"]["status"] == "PASS" for row in completed),
                 "all_company_holder_total_stylized_pass": len(completed) == len(SEEDS) and all(row["holder_total_stylized"]["status"] == "PASS" for row in completed),
                 "caps_completed_trials": sum(row["cap_hits_full"] for row in completed),
                 "failed_or_missing_trial_count": len(SEEDS) - len(completed), "empirical_acceptance": "pending"}
        if len(completed) == len(SEEDS):
            for definition in ("price", "holder_total"):
                means = np.array([row[f"{definition}_mean_moments"] for row in trials])
                mean = means.mean(axis=0)
                group[definition] = {"mean_moments": mean, "mean_by_seed": means,
                                     "seed_standard_deviation": means.std(axis=0, ddof=1),
                                     "monte_carlo_standard_error": means.std(axis=0, ddof=1) / np.sqrt(len(SEEDS)),
                                     "difference_from_target": mean - target,
                                     "difference_over_fixed_target_bootstrap_se": (mean - target) / se,
                                     "descriptive_squared_scaled_error": float(np.sum(((mean - target) / se) ** 2)),
                                     "comparison_role": "Conditional development total-return matching" if definition == "holder_total" else "Definition-mismatched sensitivity: target includes dividends"}
        else:
            group["mean_matching_scores"] = None
        candidates[candidate["id"]] = group
    pairing = {str(seed): {"completed_candidates": len(rows := [row for row in records if row["seed"] == seed and row["status"] == "completed"]),
                           "unique_intrinsic_value_path_hashes": sorted({row["intrinsic_value_path_sha256"] for row in rows}),
                           "all_completed_candidates_share_fundamentals": len({row["intrinsic_value_path_sha256"] for row in rows}) == 1}
               for seed in SEEDS}
    contrasts = []
    for name, levels in GRID.items():
        reference = getattr(MarketConfig(), name)
        for candidate in frozen["candidates"]:
            value = candidate["overrides"][name]
            if value == reference:
                continue
            control = dict(candidate["overrides"], **{name: reference})
            control_id = candidate_id(control)
            pairs = []
            for seed in SEEDS:
                treated, baseline = lookup.get((candidate["id"], seed)), lookup.get((control_id, seed))
                complete = treated is not None and baseline is not None and treated["status"] == baseline["status"] == "completed"
                pairs.append({"seed": seed, "both_completed": complete,
                              "both_mechanical_pass": complete and treated["mechanical"]["status"] == baseline["mechanical"]["status"] == "PASS",
                              "holder_total_moment_delta": np.array(treated["holder_total_mean_moments"]) - np.array(baseline["holder_total_mean_moments"]) if complete else None})
            contrasts.append({"parameter": name, "value": value, "reference_value": reference,
                              "candidate": candidate["id"], "control": control_id, "pairs": pairs,
                              "mean_delta": np.mean([row["holder_total_moment_delta"] for row in pairs], axis=0) if all(row["both_completed"] for row in pairs) else None})
    summary = {"freeze_id": frozen["freeze_id"], "target": frozen["target"], "moment_names": list(MOMENT_NAMES),
               "scheduled_market_runs": 72, "attempted_market_runs": len(records),
               "completed_market_runs": sum(row["status"] == "completed" for row in records),
               "failed_market_runs": sum(row["status"] == "failed" for row in records),
               "candidates": candidates, "paired_parameter_contrasts": contrasts, "pairing_audit": pairing,
               "source_hashes_after": hashes(), "core_sources_unchanged": hashes() == frozen["source_hashes"],
               "script_sha256": sha256_file(Path(__file__)), "selection": "none", "defaults_changed": False,
               "empirical_acceptance": "pending", "economic_total_return_mapping": "unestimated",
               "trial_files": [{"candidate": row["candidate"], "seed": row["seed"], "status": row["status"],
                                "path": f"trial_{row['candidate']}_{row['seed']}.json",
                                "sha256": sha256_file(DIRECTORY / f"trial_{row['candidate']}_{row['seed']}.json")}
                               for row in records]}
    assert summary["core_sources_unchanged"]
    write_json(DIRECTORY / "results.json", summary)
    lines = ["# 五股公开收益的有界开发匹配（2026-10-11）", "",
             "本轮24个预先固定候选×3个开发种子62001–62003；1000投资者、200公司，6592日含1000日预热。仅这5个已见历史样本的开发匹配，不是代表性个股实证校准，不是未触碰留出验收。没有自动选赢家、改默认值、使用正式保留种子或旧sealed检验。", "",
             "真实窗口按5份原文件的共同首末日固定为1986-10-30至2008-12-31，共5592个交易日、每股相同日期表。先逐公司计算九矩，再对公司等权平均；不把公司聚合成篮子。5股与模型200家公司仍有样本构成和异质性差异。", "",
             "真实数据含股息；主表用模型价格变化加当日外部分红的持有期收益。价格收益仅为定义不完全匹配的敏感性对照。V可以解释为持续经营的除息价值锚，没有机械扣V/P不等于已证明重复计量；本轮不虚构额外除息调整，经济分红/估值映射仍未估计。", "",
             f"冻结身份 `{frozen['freeze_id']}`；尝试 {len(records)}/72，完成 {summary['completed_market_runs']}，失败 {summary['failed_market_runs']}；核心依赖前后一致：{summary['core_sources_unchanged']}。", "",
             "| 候选 | 完成 | 所有试验机械通过 | 所有公司厚尾/absACF正 | cap合计（已完成） | 九矩描述差距 | 含股息rACF1 | 日波动率 |", "|---|---:|---|---|---:|---:|---:|---:|"]
    for name, group in candidates.items():
        score = group.get("holder_total", {})
        mean = score.get("mean_moments")
        metrics = f"{score['descriptive_squared_scaled_error']:.4f} | {mean[2]:.6f} | {mean[0]:.6f}" if mean is not None else "incomplete | — | —"
        lines.append(f"| {name} | {group['completed_seeds']}/3 | {group['all_trials_mechanical_pass']} | {group['all_company_holder_total_stylized_pass']} | {group['caps_completed_trials']} | {metrics} |")
    lines.extend(["", "候选ID：r=rebalance_speed×1000，m=order_flow_memory×100，n=noise_flow_scale×100000。九矩差距只用固定真实时间block-bootstrap标准误作描述尺度，不是χ²统计量或验收线；3种子Monte Carlo误差另报。任何失败/缺少种子均不提供均值匹配分数，触发cap的试验始终保留。", "",
                  "| 矩 | 5股目标 | r500_m30_n200 | r250_m30_n200 | r500_m70_n200 | r375_m70_n300 |", "|---|---:|---:|---:|---:|---:|"])
    for index, name in enumerate(MOMENT_NAMES):
        values = [f"{candidates[item]['holder_total']['mean_moments'][index]:.6g}" if "holder_total" in candidates[item] else "incomplete" for item in frozen["illustrative_candidates"]]
        lines.append(f"| {name} | {target[index]:.6g} | " + " | ".join(values) + " |")
    lines.extend(["", "四列示例在运行前已指定，不能理解为胜者；24候选全部九矩、每种子结果、标准化残差与逐参数同种子对照见results.json。每次trial JSON和NPZ保留全部200公司的价格/含股息九矩及分布、全程每日现金/股份误差、cap与逐公司边界触碰诊断。机械门槛按所有种子/公司/日取AND，均值不能替代。", "",
                  "固定支持集限制：±0.3日log价格截断、非负股息和|log(P/V)|≤5约束意味着含股息日收益宽松范围约[−0.25918,0.38961]。共同窗有4个真实观察在界外：3M/Microsoft在1987-10-19，Citigroup在2008-11-20/24；其中最高+0.578249。本轮参数网格不能生成这些观察，即使九矩接近仍存在尾部结构差异。", "",
                  "配对只限本次bare market：相同seed下所有已完成候选的完整内在价值路径哈希应一致，记录在pairing_audit；不把这一性质推广为政策博弈中任意分支的随机流完全对齐。改信息/融资/政策模块不在这13个真正依赖源码哈希中。", "",
                  "参数解释是局部比较静态，不是唯一结构识别：调再平衡会改变需求反馈；调memory改变暂时冲击中的预期流扣除；调noise同时改变波动、尾部、流动性及cap风险。若rACF改善但其他矩或稳定性恶化，不能仅凭rACF接近换默认值。", "",
                  "数据为[芝大作者教材的五个选例](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)，[Wiley官方章节](https://catalogimages.wiley.com/images/db/pdf/9780470414354.excerpt.pdf)确认CRSP收益含股息。样本偏大型长寿公司、止于2008年，缺永久ID及完整退市覆盖；公开下载不等于已获得CRSP原始数据开放再分发权。原下载快照/哈希/许可局限均在冻结target中保留。", "",
                  "复现：现有venv Python -B reproduce_calibration.py --freeze-only创建新冻结；默认执行未开始的预定试验，已有running/failed记录只保留不补跑；--summarize-only仅核验已有记录和NPZ再生成结果，不运行市场。单写者锁避免并发续跑。不得覆盖旧freeze或既有实验档案。"])
    (DIRECTORY / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-only", action="store_true")
    parser.add_argument("--summarize-only", action="store_true")
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
    assert sha256_file(ROOT / PUBLIC_PANEL) == frozen["target"]["source_panel_sha256"]
    assert sha256_file(ROOT / PUBLIC_MANIFEST) == frozen["target"]["source_manifest_sha256"]
    assert len(frozen["candidates"]) * len(SEEDS) == frozen["maximum_market_attempts"] == 72
    lock = DIRECTORY / ".writer.lock"
    with lock.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"pid": os.getpid(), "freeze_id": frozen["freeze_id"]}))
    records = []
    try:
        disable_power_throttling()
        for candidate in frozen["candidates"]:
            for config in candidate["configs"]:
                assert hashes() == frozen["source_hashes"]
                path = DIRECTORY / f"trial_{candidate['id']}_{config['seed']}.json"
                if args.summarize_only and not path.exists():
                    continue
                record = run_trial(frozen, candidate, config)
                if record["status"] == "completed":
                    assert sha256_file(DIRECTORY / record["artifact"]) == record["artifact_sha256"]
                records.append(record)
                if not args.summarize_only:
                    print(f"{len(records)}/72 {candidate['id']} seed={config['seed']} {record['status']} caps={record.get('cap_hits_full')} elapsed={record.get('total_elapsed_seconds', 0):.3f}s", flush=True)
        summarize(frozen, records)
    finally:
        lock.unlink()


if __name__ == "__main__":
    main()
