"""Run only the twelve frozen bare-market feedback diagnostics on isolated sources."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import sys
import time
import traceback
import zipfile

for variable in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[variable] = "1"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC_PATH = HERE / "freeze.json"
SPEC = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
SOURCE = HERE / "isolated_src"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def array_sha(array):
    array = np.ascontiguousarray(array)
    return hashlib.sha256(str(array.dtype).encode() + str(array.shape).encode() + array.tobytes()).hexdigest()


def clean(value):
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, (np.floating, float)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.bool_):
        return bool(value)
    return value


def write_json(path, value, *, exclusive=False):
    content = json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if exclusive:
        with path.open("x", encoding="utf-8") as stream:
            stream.write(content)
    else:
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(path)


def prepare_sources():
    baseline = SPEC["baseline_source"]
    original = ROOT / baseline["archive"]
    assert sha(original) == baseline["archive_sha256"]
    assert sha(ROOT / baseline["manifest"]) == baseline["manifest_sha256"]
    snapshot = HERE / baseline["isolated_copy"]
    assert sha(snapshot) == baseline["archive_sha256"]
    expected = baseline["all_archived_source_hashes"]
    with zipfile.ZipFile(snapshot) as bundle:
        assert set(bundle.namelist()) == set(expected)
        for name, expected_hash in expected.items():
            parts = PurePosixPath(name).parts
            assert parts and parts[0] == "abm" and ".." not in parts
            data = bundle.read(name)
            assert hashlib.sha256(data).hexdigest() == expected_hash
            target = SOURCE.joinpath(*parts)
            if target.exists():
                assert sha(target) == expected_hash
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as stream:
                    stream.write(data)
    return expected


SOURCE_HASHES = prepare_sources()
if any(name == "abm" or name.startswith("abm.") for name in sys.modules):
    raise RuntimeError("abm was imported before isolation")
sys.path.insert(0, str(SOURCE))

import numpy as np

from abm.disclosure import harness
from abm.disclosure.config import MarketConfig, TRADING_DAYS_PER_YEAR
from abm.disclosure.harness import CrossSectionMarket
from abm.disclosure.investors import InvestorPopulation
from abm.disclosure.market import CrossSectionBook
from abm.disclosure.validate import validate_market
from abm.msm import MOMENT_NAMES, compute_moments
from abm.platform_tuning import disable_power_throttling


def verify_source():
    observed = {name: sha(SOURCE / name) for name in SOURCE_HASHES}
    assert observed == SOURCE_HASHES
    for name, module in tuple(sys.modules.items()):
        if name == "abm" or name.startswith("abm."):
            filename = getattr(module, "__file__", None)
            if filename:
                path = Path(filename).resolve()
                assert path.is_relative_to(SOURCE), (name, str(path))
                relative = path.relative_to(SOURCE).as_posix()
                assert sha(path) == SOURCE_HASHES[relative]
    assert sha(ROOT / SPEC["baseline_source"]["archive"]) == SPEC["baseline_source"]["archive_sha256"]
    assert sha(ROOT / SPEC["baseline_source"]["manifest"]) == SPEC["baseline_source"]["manifest_sha256"]
    return observed


def distribution(values):
    values = np.asarray(values)
    finite = values[np.isfinite(values)]
    return {"count": int(values.size), "finite_count": int(finite.size),
            "mean": float(finite.mean()) if finite.size else None,
            "minimum": float(finite.min()) if finite.size else None,
            "quantile_05": float(np.quantile(finite, .05)) if finite.size else None,
            "median": float(np.median(finite)) if finite.size else None,
            "quantile_95": float(np.quantile(finite, .95)) if finite.size else None,
            "maximum": float(finite.max()) if finite.size else None}


class Recorder:
    def __init__(self, market, cfg):
        self.market, self.cfg = market, cfg
        shape = (cfg.trading_days + 1, cfg.n_firms)
        per_asset = ("raw", "moves", "news_quote", "permanent_flow", "transient_change", "inventory_quote",
                     "depth_before", "depth_fraction", "variance_before", "reference_variance_before",
                     "variance_after", "reference_variance_after", "volatility_ratio_before",
                     "expected_flow_before", "expected_flow_after", "transient_before", "transient_after",
                     "investor_submitted", "noise_submitted", "investor_executed", "noise_executed",
                     "noise_amplification", "noise_unamplified_demand", "noise_inventory_correction",
                     "noise_order_before_constraints", "noise_idiosyncratic_innovation",
                     "maker_inventory", "noise_holdings", "share_error_by_asset")
        self.data = {name: np.full(shape, np.nan) for name in per_asset}
        daily = ("noise_common_innovation", "noise_cash", "maker_cash", "deciding_count",
                 "deciding_wealth_share", "allocation_market_annual_variance",
                 "minimum_investor_cash", "minimum_investor_holding")
        self.data.update({name: np.full(cfg.trading_days + 1, np.nan) for name in daily})
        self.data.update({name: np.zeros(cfg.trading_days + 1, dtype=bool)
                          for name in ("quote_logged", "settlement_logged", "step_completed")})
        self.data["capped"] = np.zeros(shape, dtype=bool)
        self.day, self.cash_calls = 0, []
        self.record_state(0)
        self.data["depth_fraction"][0] = market.book.depth_fraction
        self.data["variance_after"][0] = market.book.variance
        self.data["reference_variance_after"][0] = market.book.reference_variance
        self.initialization_hash = array_sha(np.r_[market.prices, market.investors.cash,
                                                   market.investors.holdings.ravel()])
        self.schedule_hash = array_sha(np.c_[market.investors.decision_interval,
                                           market.investors.decision_offset])

    def record_state(self, day):
        m, data = self.market, self.data
        data["maker_inventory"][day] = m.market_maker_inventory
        data["noise_holdings"][day] = m.noise_holdings
        data["share_error_by_asset"][day] = m.investors.holdings.sum(axis=0) + m.noise_holdings + m.market_maker_inventory - 1
        data["noise_cash"][day], data["maker_cash"][day] = m.noise_cash, m.market_maker_cash
        data["minimum_investor_cash"][day] = m.investors.cash.min()
        data["minimum_investor_holding"][day] = m.investors.holdings.min()
        data["variance_after"][day] = m.book.variance
        data["reference_variance_after"][day] = m.book.reference_variance

    def __enter__(self):
        cfg, data = self.cfg, self.data
        self.original = (CrossSectionMarket.step, CrossSectionMarket._noise_orders,
                         InvestorPopulation.desired_orders, CrossSectionBook.price_moves, harness._cap_buys_to_cash)
        original_step, original_noise, original_orders, original_moves, original_cap = self.original

        def capture_cap(orders, cash, prices, cost):
            result = original_cap(orders, cash, prices, cost)
            self.cash_calls.append(result.copy())
            return result

        def capture_orders(investors, who, **kwargs):
            wealth = investors.wealth(kwargs["prices"])
            data["deciding_count"][self.day] = who.size
            data["deciding_wealth_share"][self.day] = wealth[who].sum() / wealth.sum()
            data["allocation_market_annual_variance"][self.day] = kwargs["market_annual_variance"]
            return original_orders(investors, who, **kwargs)

        def capture_noise(market):
            before_common = market.noise_common
            before_idiosyncratic = market.noise_idiosyncratic.copy()
            correction = -cfg.noise_inventory_reversion * (market.noise_holdings - market.noise_target)
            ratio = np.minimum(np.sqrt(market.book.variance / market.book.reference_variance), 4.0)
            amplification = ratio ** cfg.noise_volatility_exponent
            result = original_noise(market)
            innovation_scale = np.sqrt(1 - cfg.noise_persistence ** 2)
            demand = np.sqrt(cfg.noise_common_correlation) * market.noise_common + np.sqrt(1 - cfg.noise_common_correlation) * market.noise_idiosyncratic
            data["noise_common_innovation"][self.day] = (market.noise_common - cfg.noise_persistence * before_common) / innovation_scale
            data["noise_idiosyncratic_innovation"][self.day] = (market.noise_idiosyncratic - cfg.noise_persistence * before_idiosyncratic) / innovation_scale
            data["noise_amplification"][self.day] = amplification
            data["noise_unamplified_demand"][self.day] = demand
            data["noise_inventory_correction"][self.day] = correction
            data["noise_order_before_constraints"][self.day] = cfg.noise_flow_scale * demand * amplification + correction
            return result

        def capture_moves(book, net_flow_value, market_cap, news, inventory_gap):
            day = self.day
            previous_transient, previous_expected = book.transient_impact.copy(), book.expected_flow_impact.copy()
            data["depth_before"][day] = book.depth_fraction
            data["variance_before"][day], data["reference_variance_before"][day] = book.variance, book.reference_variance
            data["volatility_ratio_before"][day] = np.sqrt(book.variance / book.reference_variance)
            moves, capped = original_moves(book, net_flow_value, market_cap, news, inventory_gap)
            flow = cfg.price_impact * net_flow_value / (cfg.liquidity_fraction * market_cap)
            raw = cfg.news_pass_through * news + cfg.permanent_impact_fraction * flow + book.transient_impact - previous_transient + cfg.market_maker_inventory_skew * inventory_gap
            assert np.array_equal(moves, np.clip(raw, -cfg.max_log_return, cfg.max_log_return))
            assert np.array_equal(capped, moves != raw)
            assert len(self.cash_calls) == 2
            data["investor_submitted"][day] = self.cash_calls[0].sum(axis=0)
            data["noise_submitted"][day] = self.cash_calls[1][0]
            data["raw"][day], data["moves"][day], data["capped"][day] = raw, moves, capped
            data["news_quote"][day] = cfg.news_pass_through * news
            data["permanent_flow"][day] = cfg.permanent_impact_fraction * flow
            data["transient_change"][day] = book.transient_impact - previous_transient
            data["inventory_quote"][day] = cfg.market_maker_inventory_skew * inventory_gap
            data["depth_fraction"][day] = book.depth_fraction
            data["transient_before"][day], data["transient_after"][day] = previous_transient, book.transient_impact
            data["expected_flow_before"][day], data["expected_flow_after"][day] = previous_expected, book.expected_flow_impact
            data["quote_logged"][day] = True
            return moves, capped

        def capture_step(market, day_index):
            self.day, self.cash_calls = day_index + 1, []
            try:
                original_step(market, day_index)
                data["step_completed"][self.day] = True
            finally:
                if len(self.cash_calls) == 4:
                    data["investor_executed"][self.day] = self.cash_calls[2].sum(axis=0)
                    data["noise_executed"][self.day] = self.cash_calls[3][0]
                    data["settlement_logged"][self.day] = True
                self.record_state(self.day)

        CrossSectionMarket.step, CrossSectionMarket._noise_orders = capture_step, capture_noise
        InvestorPopulation.desired_orders, CrossSectionBook.price_moves = capture_orders, capture_moves
        harness._cap_buys_to_cash = capture_cap
        return self

    def __exit__(self, *_):
        CrossSectionMarket.step, CrossSectionMarket._noise_orders, InvestorPopulation.desired_orders, CrossSectionBook.price_moves, harness._cap_buys_to_cash = self.original


def run_case(case, contract):
    path = HERE / (case["id"] + ".json")
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        assert old["contract"] == contract and old["config"] == case["config"]
        if old.get("artifact"):
            assert sha(HERE / old["artifact"]) == old["artifact_sha256"]
        return old
    record = {"case": case["id"], "arm": case["arm"], "seed": case["seed"], "config": case["config"],
              "contract": contract, "status": "running", "started_utc": datetime.now(UTC).isoformat()}
    write_json(path, record, exclusive=True)
    started = time.perf_counter()
    market = recorder = result = None
    price_moments = np.full((case["config"]["n_firms"], len(MOMENT_NAMES)), np.nan)
    total_moments = price_moments.copy()
    interrupted = None
    try:
        verify_source()
        cfg = MarketConfig.from_dict(case["config"])
        market = CrossSectionMarket(cfg)
        assert np.all(market.investors.taste == 0) and np.all(market.investors.investor_type == 0)
        recorder = Recorder(market, cfg)
        record["initialization_sha256"], record["decision_schedule_sha256"] = recorder.initialization_hash, recorder.schedule_hash
        with recorder:
            result = market.run()
        record["market_and_telemetry_seconds"] = time.perf_counter() - started
        validation = validate_market(result, cfg)
        price_moments = np.array([[asset["moments"][name] for name in MOMENT_NAMES]
                                  for asset in validation["moments_per_asset"]], dtype=float)
        price_returns = np.expm1(np.diff(np.log(result.prices), axis=0))
        total_returns = price_returns + cfg.cash_flow_yield * result.intrinsic_values[1:] / TRADING_DAYS_PER_YEAR / result.prices[:-1]
        total_moments = np.array([compute_moments(total_returns[cfg.burn_in_days:, firm]) for firm in range(cfg.n_firms)])
        all_share_error = np.abs(recorder.data["share_error_by_asset"])
        assert np.array_equal(recorder.data["capped"].sum(axis=1), result.price_cap_hits)
        assert np.all(recorder.data["step_completed"][1:])
        assert np.allclose(all_share_error.max(axis=1), result.maximum_share_error, rtol=0, atol=1e-15)
        total_checks = {"all_finite_nine_moments": bool(np.isfinite(total_moments).all()),
                        "all_positive_excess_kurtosis": bool(np.all(total_moments[:, 1] > 0)),
                        "all_positive_abs_return_acf1": bool(np.all(total_moments[:, 3] > 0))}
        record.update(status="completed", validation=validation, result_fingerprint=result.fingerprint(),
                      intrinsic_value_path_sha256=array_sha(result.intrinsic_values),
                      noise_innovation_path_sha256=array_sha(np.c_[recorder.data["noise_common_innovation"][1:],
                                                                  recorder.data["noise_idiosyncratic_innovation"][1:]]),
                      price_moments_by_company=price_moments, holder_total_moments_by_company=total_moments,
                      price_mean_moments=price_moments.mean(axis=0), holder_total_mean_moments=total_moments.mean(axis=0),
                      price_moment_distributions={name: distribution(price_moments[:, i]) for i, name in enumerate(MOMENT_NAMES)},
                      holder_total_moment_distributions={name: distribution(total_moments[:, i]) for i, name in enumerate(MOMENT_NAMES)},
                      holder_total_stylized={"status": "PASS" if all(total_checks.values()) else "FAIL", "checks": total_checks},
                      cap_hits_full=int(result.price_cap_hits.sum()),
                      cap_hits_burn_in=int(result.price_cap_hits[:cfg.burn_in_days + 1].sum()),
                      cap_hits_measurement=int(result.price_cap_hits[cfg.burn_in_days + 1:].sum()),
                      maximum_absolute_raw_quote=float(np.nanmax(np.abs(recorder.data["raw"]))),
                      maximum_absolute_share_error_every_asset=float(all_share_error.max()),
                      measured_price_volatility_distribution=distribution(price_moments[:, 0]),
                      depth_distribution_all_asset_days=distribution(recorder.data["depth_fraction"][1:]),
                      prequote_volatility_ratio_distribution=distribution(recorder.data["volatility_ratio_before"][1:]))
    except BaseException as error:
        record.update(status="failed", exception_type=type(error).__name__, error=traceback.format_exc(),
                      validation={"mechanical": {"status": "FAIL", "reason": "World or diagnostics incomplete"},
                                  "stylized": {"status": "pending"}, "return_acf": {"status": "pending"},
                                  "cross_asset_correlation": {"status": "pending"},
                                  "empirical_calibration": {"status": "pending"}})
        if isinstance(error, (KeyboardInterrupt, SystemExit)):
            interrupted = error
    finally:
        if market is not None:
            completed = market.next_day_index
            record["completed_days"] = completed
            record["simulation_completed"] = completed == market.config.trading_days
            data = {"day": np.arange(completed + 1), "prices": market.price_path[:completed + 1],
                    "intrinsic_values": market.value_path[:completed + 1], "size_class": market.firms.size_class,
                    "equity_share": market.equity_share[:completed + 1],
                    "mean_depth_fraction": market.mean_depth_fraction[:completed + 1],
                    "gross_volume": market.gross_volume[:completed + 1],
                    "price_cap_hits_completed_prefix": market.price_cap_hits[:completed + 1],
                    "total_cash": market.total_cash[:completed + 1],
                    "maximum_absolute_share_error": market.maximum_share_error[:completed + 1],
                    "current_prices": market.prices, "current_intrinsic_values": market.firms.intrinsic_value,
                    "price_moments": price_moments, "holder_total_moments": total_moments}
            dividends = market.config.cash_flow_yield * data["intrinsic_values"][1:].sum(axis=1) / TRADING_DAYS_PER_YEAR
            expected_cash = data["total_cash"][0] + np.r_[0., np.cumsum(dividends)]
            data["expected_total_cash"] = expected_cash
            data["relative_cash_error"] = np.abs(data["total_cash"] - expected_cash) / np.where(expected_cash != 0, np.abs(expected_cash), 1)
            if completed:
                data["price_returns"] = np.expm1(np.diff(np.log(data["prices"]), axis=0))
                data["holder_total_returns"] = data["price_returns"] + market.config.cash_flow_yield * data["intrinsic_values"][1:] / TRADING_DAYS_PER_YEAR / data["prices"][:-1]
            if recorder is not None:
                stop = min(completed + 1, market.config.trading_days) + 1
                if completed == market.config.trading_days:
                    stop = completed + 1
                data.update({"telemetry_" + name: values[:stop] for name, values in recorder.data.items()})
                record["observed_quote_caps_including_partial_step"] = int(recorder.data["capped"][:stop].sum())
                record["failure_partial_day"] = completed + 1 if completed < market.config.trading_days else None
            artifact = HERE / (case["id"] + ".npz")
            with artifact.open("xb") as stream:
                np.savez_compressed(stream, **data)
            record["artifact"], record["artifact_sha256"] = artifact.name, sha(artifact)
        record["total_elapsed_seconds"] = time.perf_counter() - started
        record["finished_utc"] = datetime.now(UTC).isoformat()
        record["isolated_source_unchanged"] = verify_source() == SOURCE_HASHES
        assert sha(SPEC_PATH) == contract["spec_sha256"] and sha(Path(__file__)) == contract["launcher_sha256"]
        write_json(path, record)
    if interrupted is not None:
        raise interrupted
    print(json.dumps({"case": case["id"], "status": record["status"], "caps": record.get("cap_hits_full"),
                      "mechanical": record["validation"]["mechanical"]["status"]}), flush=True)
    return record


def summarize(contract):
    records = []
    for case in SPEC["cases"]:
        path = HERE / (case["id"] + ".json")
        if not path.exists():
            records.append({"case": case["id"], "seed": case["seed"], "arm": case["arm"], "status": "not_started"})
            continue
        record = json.loads(path.read_text(encoding="utf-8"))
        assert record["contract"] == contract and record["config"] == case["config"]
        if record.get("artifact"):
            assert sha(HERE / record["artifact"]) == record["artifact_sha256"]
        records.append(record)
    completed = [row for row in records if row["status"] == "completed"]
    paired, contrasts, arms = {}, {}, {}
    for seed in SPEC["budget"]["seeds"]:
        group = [row for row in records if row["seed"] == seed and row["status"] == "completed"]
        paired[seed] = {"completed_arms": len(group), "status": "insufficient"}
        if len(group) == 4:
            fields = ("initialization_sha256", "decision_schedule_sha256", "intrinsic_value_path_sha256", "noise_innovation_path_sha256")
            matches = {name: len({row[name] for row in group}) == 1 for name in fields}
            paired[seed] = {"completed_arms": 4, "status": "PASS" if all(matches.values()) else "FAIL", "checks": matches}
            by = {row["arm"]: row for row in group}
            contrasts[seed] = {}
            for definition in ("price", "holder_total"):
                key = definition + "_mean_moments"
                baseline = np.array(by["current"][key])
                contrasts[seed][definition] = {name: np.array(row[key]) - baseline for name, row in by.items() if name != "current"}
                contrasts[seed][definition]["factorial_interaction"] = np.array(by["neither_volatility_feedback"][key]) - np.array(by["no_noise_volatility_feedback"][key]) - np.array(by["no_depth_volatility_feedback"][key]) + baseline
    for arm in SPEC["arms"]:
        rows = [row for row in records if row["arm"] == arm["id"]]
        good = [row for row in rows if row["status"] == "completed"]
        a = {"scheduled_worlds": 3, "completed_worlds": len(good), "statuses": {row["seed"]: row["status"] for row in rows},
             "all_worlds_mechanical_pass": len(good) == 3 and all(row["validation"]["mechanical"]["status"] == "PASS" for row in good),
             "all_worlds_price_stylized_pass": len(good) == 3 and all(row["validation"]["stylized"]["status"] == "PASS" for row in good),
             "all_worlds_holder_total_stylized_pass": len(good) == 3 and all(row["holder_total_stylized"]["status"] == "PASS" for row in good),
             "observed_cap_hits_completed_worlds": sum(row["cap_hits_full"] for row in good),
             "price_mean_moments": None, "holder_total_mean_moments": None}
        if len(good) == 3:
            for definition in ("price", "holder_total"):
                a[definition + "_mean_moments"] = np.mean([row[definition + "_mean_moments"] for row in good], axis=0)
                all_moments = np.concatenate([np.asarray(row[definition + "_moments_by_company"]) for row in good])
                a[definition + "_moment_distributions"] = {name: distribution(all_moments[:, i]) for i, name in enumerate(MOMENT_NAMES)}
        arms[arm["id"]] = a
    payload = {"contract": contract, "purpose": SPEC["purpose"], "scheduled_worlds": 12,
               "completed_worlds": len(completed), "status": "complete" if all(row["status"] in ("completed", "failed") for row in records) else "incomplete",
               "all_worlds_mechanical_pass": len(completed) == 12 and all(row["validation"]["mechanical"]["status"] == "PASS" for row in completed),
               "all_worlds_price_stylized_pass": len(completed) == 12 and all(row["validation"]["stylized"]["status"] == "PASS" for row in completed),
               "return_acf": "pending", "cross_asset_correlation": "pending", "empirical_calibration": "pending",
               "moment_names": MOMENT_NAMES, "pairing": paired, "within_seed_moment_contrasts": contrasts,
               "arms": arms, "records": records, "automatic_winner": None,
               "limits": ["Three already-inspected seeds at 150 investors/30 firms are a conditional development diagnostic, not unseen validation or a population incidence sample.",
                          "Bare market contains no disclosure decisions, Q training, audit or firm expenditure; it does not identify the separate nine corporate cost-news caps.",
                          "Every company is one asset; company moments are never moments of pooled returns or an industry basket.",
                          "Price and externally dividend-inclusive holding-period returns are separate. Continuing ex-dividend anchor interpretation is unestimated.",
                          "Factorial contrasts are within-model conditional path comparisons, not real-market causal identification or default selection.",
                          "All failed worlds and burn-in caps remain in gates; missing/failed worlds cannot be replaced by successful-world means."]}
    write_json(HERE / "summary.json", payload)
    lines = ["# 双反馈：固定12世界开发诊断", "",
             f"预定12世界，完成{len(completed)}；全部世界机械通过={payload['all_worlds_mechanical_pass']}，逐公司价格厚尾/absACF通过={payload['all_worlds_price_stylized_pass']}。收益ACF、跨资产相关及经验校准仍pending。没有选赢家或改变默认参数。", "",
             "|种子|臂|状态|cap(全期)|机械|价格stylized|", "|---:|---|---|---:|---|---|"]
    for row in records:
        v = row.get("validation", {})
        lines.append(f"|{row['seed']}|{row['arm']}|{row['status']}|{row.get('cap_hits_full', '')}|{v.get('mechanical', {}).get('status', '')}|{v.get('stylized', {}).get('status', '')}|")
    lines += ["", "下表为各公司的矩先在世界内等权，再对三个种子等权。只有该臂三世界全部完成才提供均值；所有公司分布、失败明细和逐seed差值在summary.json。机械及stylized门槛按所有世界/资产/日取AND，不以均值验收。", "",
              "|含外部分红的矩|current|no_noise_volatility_feedback|no_depth_volatility_feedback|neither_volatility_feedback|", "|---|---:|---:|---:|---:|"]
    for i, name in enumerate(MOMENT_NAMES):
        cells = [f"{arms[a['id']]['holder_total_mean_moments'][i]:.7g}" if arms[a['id']]["holder_total_mean_moments"] is not None else "pending" for a in SPEC["arms"]]
        lines.append("|" + "|".join([name] + cells) + "|")
    lines += ["", "每份NPZ保存完整价格/V、价格与含外部分红收益、30公司九矩、逐公司日深度/波动/报价分项/提交与执行流、噪声创新和库存修正、逐公司股份误差与现金账。失败仅保存已完成前缀及明确标记的部分失败日；未将未初始化未来行当作数据。", "",
              "基线来自已核验的seed27001冻结source.zip，隔离副本及全部源码hash绑定freeze.json；full config只改两个预设反馈开关及seed，bare不运行企业/II/学习。三种子已在失败诊断中见过，本次不是独立验收样本，也不能替代1000/200规模或公开个股数据校准。价格收益与含外部分红收益口径分列；未增加虚构的除息调整。", "",
              "静态depth=1分解仅用于提出机制假设，不等于本次路径结果。关闭反馈可能削弱波动/尾部，即使无cap或某个ACF接近也不能提升默认值；以前72次调memory的未解决矩差距仍保留。所有臂、失败和预热期cap均报告，不追加种子/候选或自动选胜者。原274档机械和覆盖FAIL不被本诊断改写。", ""]
    (HERE / "report.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(HERE / "summary_manifest.json", {"contract": contract, "summary_sha256": sha(HERE / "summary.json"),
                                                "report_sha256": sha(HERE / "report.md"),
                                                "case_json_sha256": {row["case"]: sha(HERE / (row["case"] + ".json")) for row in records if (HERE / (row["case"] + ".json")).exists()}})
    return payload


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--check-only", action="store_true")
    modes.add_argument("--summarize-only", action="store_true")
    args = parser.parse_args()
    assert platform.python_version() == SPEC["baseline_source"]["python_version"]
    assert np.__version__ == SPEC["baseline_source"]["numpy_version"]
    assert len(SPEC["cases"]) == SPEC["budget"]["worlds"] == 12
    assert len({case["id"] for case in SPEC["cases"]}) == 12
    assert {case["seed"] for case in SPEC["cases"]} == {27001, 27304, 27305}
    configurations = [MarketConfig.from_dict(case["config"]) for case in SPEC["cases"]]
    assert all((cfg.n_investors, cfg.n_firms, cfg.trading_days, cfg.burn_in_days, cfg.max_log_return) == (150, 30, 1800, 600, .3) for cfg in configurations)
    verify_source()
    contract = {"spec_sha256": sha(SPEC_PATH), "launcher_sha256": sha(Path(__file__)),
                "source_zip_sha256": sha(HERE / "source.zip"),
                "python_version": platform.python_version(), "numpy_version": np.__version__}
    launch_path = HERE / "launch_manifest.json"
    if launch_path.exists():
        assert json.loads(launch_path.read_text(encoding="utf-8"))["contract"] == contract
    if not args.run and not args.summarize_only:
        write_json(HERE / "preflight.json", {"status": "PASS", "contract": contract, "market_initializations": 0,
                                            "market_runs": 0, "configurations": 12, "isolated_source_files": len(SOURCE_HASHES)})
        print("PASS preflight: twelve frozen configs, isolated archived sources; zero market initializations")
        return
    lock = HERE / "writer.lock"
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.write(descriptor, str(os.getpid()).encode())
        if not launch_path.exists():
            write_json(launch_path, {"contract": contract, "started_utc": datetime.now(UTC).isoformat(),
                                     "source_hashes": SOURCE_HASHES, "thread_environment": {name: os.environ[name] for name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS")}}, exclusive=True)
        if args.run:
            disable_power_throttling()
            for case in SPEC["cases"]:
                run_case(case, contract)
        report = summarize(contract)
        verify_source()
        print(json.dumps({"status": report["status"], "completed_worlds": report["completed_worlds"],
                          "all_worlds_mechanical_pass": report["all_worlds_mechanical_pass"], "automatic_winner": None}))
    finally:
        os.close(descriptor)
        lock.unlink()


if __name__ == "__main__":
    main()
