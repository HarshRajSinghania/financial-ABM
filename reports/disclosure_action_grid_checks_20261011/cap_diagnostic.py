"""Read completed archives only; reconstruct accounting and depth, never a market."""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile

import numpy as np


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
ARCHIVE = ROOT / "reports/disclosure_action_grid_development_20261011_v1"
ATOL = 1e-12
SIZE_NAMES = ("large", "mid", "small")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def statistics(values):
    a = np.asarray(values, dtype=float)
    if not a.size:
        return {"count": 0}
    assert np.isfinite(a).all()
    return {"count": int(a.size), "minimum": float(a.min()),
            "quantile_05": float(np.quantile(a, .05)), "median": float(np.median(a)),
            "mean": float(a.mean()), "quantile_95": float(np.quantile(a, .95)),
            "maximum": float(a.max())}


EVENTS = ("asset_resource_cost", "asset_fine", "asset_subsidy",
          "any_firm_resource_cost", "any_firm_fine", "any_firm_subsidy",
          "asset_scheduled_real_arrival", "asset_scheduled_wash_arrival",
          "any_firm_scheduled_real_arrival", "any_firm_scheduled_wash_arrival",
          "financing_repricing_before_quote", "decision_and_audit_after_quote",
          "asset_audit_selected_after_quote", "asset_detection_after_quote")


def aggregate(rows, worlds):
    return {
        "worlds": len(worlds), "worlds_with_caps": len({r["world"] for r in rows}),
        "cap_hits": len(rows), "during_burn_in": sum(r["during_burn_in"] for r in rows),
        "events": {key: sum(r["events"][key] for r in rows) for key in EVENTS},
        "without_any_firm_applied_cost_fine_or_subsidy": sum(
            not any(r["events"][key] for key in
                    ("any_firm_resource_cost", "any_firm_fine", "any_firm_subsidy")) for r in rows),
        "without_any_scheduled_project_arrival": sum(
            not (r["events"]["any_firm_scheduled_real_arrival"] or
                 r["events"]["any_firm_scheduled_wash_arrival"]) for r in rows),
        "news_alone_reaches_cap_in_observed_direction": sum(
            r["quote"]["signed_news_toward_cap"] >= r["quote"]["cap_limit"] for r in rows),
        "remaining_quote_required_above_half_cap": sum(
            r["quote"]["signed_remaining_quote_strict_lower_bound"] > .5 * r["quote"]["cap_limit"]
            for r in rows),
        "signed_news_toward_cap": statistics([r["quote"]["signed_news_toward_cap"] for r in rows]),
        "signed_exogenous_news_toward_cap": statistics(
            [r["quote"]["signed_exogenous_news_toward_cap"] for r in rows]),
        "signed_commitment_news_toward_cap": statistics(
            [r["quote"]["signed_commitment_news_toward_cap"] for r in rows]),
        "signed_financing_news_toward_cap": statistics(
            [r["quote"]["signed_financing_news_toward_cap"] for r in rows]),
        "signed_remaining_quote_strict_lower_bound": statistics(
            [r["quote"]["signed_remaining_quote_strict_lower_bound"] for r in rows]),
        "reconstructed_asset_depth_fraction": statistics([r["depth"]["asset_fraction"] for r in rows]),
    }


def main():
    paths = sorted(ARCHIVE.glob("**/manifest.json"))
    assert len(paths) == 274, len(paths)
    summary_path = ARCHIVE / "summary.json"
    summary_bytes = summary_path.read_bytes()
    assert json.loads(summary_bytes)["status"] == "complete"
    review = json.loads((OUT / "review.json").read_text(encoding="utf-8"))
    reviewed = review["reviewed_source_sha256"]
    current_before = {name: sha((ROOT / name).read_bytes()) for name in reviewed}
    assert current_before == reviewed
    runs, hits, verified_source_zips = [], [], {}
    common_source = None
    first_example = None
    for number, path in enumerate(paths, 1):
        raw = {name: (path.parent / name).read_bytes() for name in
               ("manifest.json", "result.npz", "validation.json", "source.zip")}
        hashes = {name: sha(data) for name, data in raw.items()}
        manifest = json.loads(raw["manifest.json"])
        assert manifest["status"] == "complete", str(path)
        for name in ("result.npz", "validation.json", "source.zip"):
            assert hashes[name] == manifest["artifacts"][name], (str(path), name)
        source_hashes = manifest["source_hashes"]
        assert {"src/" + name: value for name, value in source_hashes.items()
                if "src/" + name in reviewed} == reviewed
        if common_source is None:
            common_source = source_hashes
        assert source_hashes == common_source, str(path)
        if hashes["source.zip"] not in verified_source_zips:
            with zipfile.ZipFile(io.BytesIO(raw["source.zip"])) as z:
                archived = {name: sha(z.read(name)) for name in z.namelist()}
            assert archived == source_hashes, str(path)
            verified_source_zips[hashes["source.zip"]] = True
        validation = json.loads(raw["validation.json"])
        with np.load(io.BytesIO(raw["result.npz"]), allow_pickle=False) as z:
            d = {name: z[name] for name in z.files}
        cfg, domain = manifest["config"], manifest["domain"]
        stage = path.relative_to(ARCHIVE).parts[0]
        rule = cfg["firm_policy"]
        prices, values = d["market_prices"], d["market_intrinsic_values"]
        days, assets = prices.shape[0] - 1, prices.shape[1]
        returns = np.zeros_like(prices)
        returns[1:] = np.log(prices[1:] / prices[:-1])
        cap_flags = np.isclose(np.abs(returns), cfg["max_log_return"], rtol=0, atol=ATOL)
        cap_flags[0] = False
        archived_caps = d["market_price_cap_hits"]
        assert np.array_equal(cap_flags.sum(axis=1), archived_caps), str(path)
        assert int(archived_caps.sum()) == validation["mechanical"]["price_cap_hits"]

        # Legacy continuous NPV has no daily ledgers; reconstruct the same next-day entry.
        costs = np.zeros_like(values)
        fines, subsidies = costs.copy(), costs.copy()
        real_arrivals, wash_arrivals = costs.copy(), costs.copy()
        interval = cfg["firm_decision_interval"]
        for period in range(1, d["actions"].shape[0]):
            decision_day = period * interval
            if decision_day < days:
                for target, key in ((costs, "cost_fraction"), (fines, "penalty_fraction"),
                                    (subsidies, "subsidy_fraction")):
                    target[decision_day + 1] += d[key][period] * prices[decision_day]
            for firm in range(assets):
                due = int(d["action_due_day"][period, firm])
                if 1 <= due <= days:
                    kind = int(d["actions"][period, firm])
                    assert kind in (0, 1)
                    (real_arrivals if kind == 0 else wash_arrivals)[due, firm] += d["amounts"][period, firm]
        ledger_source = "reconstructed_fraction_times_decision_close_price_applied_next_day"
        if "applied_resource_cost" in d:
            for actual, reconstructed in ((d["applied_resource_cost"], costs),
                                           (d["applied_fine"], fines),
                                           (d["applied_subsidy"], subsidies)):
                assert np.allclose(actual, reconstructed, rtol=1e-12, atol=1e-15), str(path)
            costs, fines, subsidies = (d["applied_resource_cost"], d["applied_fine"], d["applied_subsidy"])
            ledger_source = "archived_daily_ledgers_crosschecked_against_next_day_reconstruction"

        financing = d["financing_value_adjustment"]
        after_commitment = values - financing
        exogenous_values = after_commitment + costs + fines - subsidies
        assert (exogenous_values > 0).all() and (after_commitment > 0).all()
        news = np.zeros_like(values)
        exogenous, commitment, funding = news.copy(), news.copy(), news.copy()
        news[1:] = np.log(values[1:] / values[:-1])
        exogenous[1:] = np.log(exogenous_values[1:] / values[:-1])
        commitment[1:] = np.log(after_commitment[1:] / exogenous_values[1:])
        funding[1:] = np.log(values[1:] / after_commitment[1:])
        news_error = float(np.max(np.abs(news - exogenous - commitment - funding)))
        assert news_error < 1e-12

        # Reconstruct only book variance/depth from archived returns, without initializing a book.
        variance = np.full(assets, cfg["initial_asset_volatility"] ** 2 / 252)
        reference = variance.copy()
        depth = np.ones(assets)
        depth_path = np.ones_like(prices)
        stress_path = np.zeros_like(prices)
        variance_ratio = np.ones_like(prices)
        for day in range(1, days + 1):
            variance_ratio[day] = variance / reference
            stress = np.clip(np.sqrt(variance_ratio[day]) - cfg["liquidity_stress_threshold"], 0, 1)
            target = np.maximum(cfg["minimum_liquidity_fraction"],
                                np.exp(-cfg["liquidity_volatility_sensitivity"] * stress))
            depth += cfg["depth_resilience"] * (target - depth)
            np.maximum(depth, cfg["minimum_liquidity_fraction"], out=depth)
            depth_path[day], stress_path[day] = depth, stress
            squared = returns[day] ** 2
            variance = cfg["variance_ewma_decay"] * variance + (1 - cfg["variance_ewma_decay"]) * squared
            reference = cfg["reference_variance_decay"] * reference + (1 - cfg["reference_variance_decay"]) * squared
        depth_error = float(np.max(np.abs(depth_path.mean(axis=1) - d["market_mean_depth_fraction"])))
        assert depth_error < 1e-12, (str(path), depth_error)
        world = {"path": path.parent.relative_to(ROOT).as_posix(), "seed": cfg["seed"],
                 "stage": stage, "rule": rule, "run_id": manifest["run_id"],
                 "artifact_sha256": hashes, "cap_hits": int(archived_caps.sum()),
                 "mechanical": validation["mechanical"], "stylized_status": validation["stylized"]["status"],
                 "ledger_source": ledger_source, "cap_identification_daily_count_match": True,
                 "maximum_mean_depth_reconstruction_error": depth_error,
                 "maximum_news_decomposition_error": news_error,
                 "asset_days_by_size": {name: int((d["market_size_class"] == index).sum()) * days
                                        for index, name in enumerate(SIZE_NAMES)}}
        runs.append(world)
        for day, firm in np.argwhere(cap_flags):
            day, firm = int(day), int(firm)
            sign = 1 if returns[day, firm] > 0 else -1
            decision_today = day % interval == 0
            p = day // interval
            prior_p = (day - 1) // interval
            asset_cost, asset_fine, asset_subsidy = (float(a[day, firm]) for a in (costs, fines, subsidies))
            event = {
                "asset_resource_cost": asset_cost > 0, "asset_fine": asset_fine > 0,
                "asset_subsidy": asset_subsidy > 0,
                "any_firm_resource_cost": bool(np.any(costs[day] > 0)),
                "any_firm_fine": bool(np.any(fines[day] > 0)),
                "any_firm_subsidy": bool(np.any(subsidies[day] > 0)),
                "asset_scheduled_real_arrival": bool(real_arrivals[day, firm] > 0),
                "asset_scheduled_wash_arrival": bool(wash_arrivals[day, firm] > 0),
                "any_firm_scheduled_real_arrival": bool(np.any(real_arrivals[day] > 0)),
                "any_firm_scheduled_wash_arrival": bool(np.any(wash_arrivals[day] > 0)),
                "financing_repricing_before_quote": day % cfg["financing_repricing_interval"] == 0,
                "decision_and_audit_after_quote": decision_today,
                "asset_audit_selected_after_quote": bool(decision_today and d["audit_selected"][p, firm]),
                "asset_detection_after_quote": bool(decision_today and d["detections"][p, firm]),
            }
            scale = sign * cfg["news_pass_through"]
            row = {"world": world["path"], "seed": cfg["seed"], "stage": stage, "rule": rule,
                   "day": day, "firm_index_zero_based": firm,
                   "size": SIZE_NAMES[int(d["market_size_class"][firm])],
                   "direction": "up" if sign > 0 else "down", "during_burn_in": day <= cfg["burn_in_days"],
                   "observed_log_return": float(returns[day, firm]), "events": event,
                   "accounting": {"resource_cost": asset_cost, "fine": asset_fine,
                                  "subsidy": asset_subsidy, "financing_adjustment": float(financing[day, firm]),
                                  "prior_intrinsic_value": float(values[day - 1, firm]),
                                  "intrinsic_value": float(values[day, firm]),
                                  "exogenous_log_news": float(exogenous[day, firm]),
                                  "commitment_log_news": float(commitment[day, firm]),
                                  "financing_log_news": float(funding[day, firm]),
                                  "total_log_news": float(news[day, firm]), "ledger_source": ledger_source},
                   "quote": {"cap_limit": cfg["max_log_return"],
                             "news_log_return_contribution": float(cfg["news_pass_through"] * news[day, firm]),
                             "signed_news_toward_cap": float(scale * news[day, firm]),
                             "signed_exogenous_news_toward_cap": float(scale * exogenous[day, firm]),
                             "signed_commitment_news_toward_cap": float(scale * commitment[day, firm]),
                             "signed_financing_news_toward_cap": float(scale * funding[day, firm]),
                             "signed_remaining_quote_strict_lower_bound": float(cfg["max_log_return"] - scale * news[day, firm])},
                   "depth": {"asset_fraction": float(depth_path[day, firm]),
                             "market_mean_fraction": float(d["market_mean_depth_fraction"][day]),
                             "prequote_variance_over_reference": float(variance_ratio[day, firm]),
                             "stress": float(stress_path[day, firm])},
                   "signals": {"prior_public_signal": float(d["public_signal"][day - 1, firm]),
                               "public_signal": float(d["public_signal"][day, firm]),
                               "goodness_after_close": float(d["true_goodness"][day, firm]),
                               "inflation_after_close": float(d["inflation"][day, firm])},
                   "scheduled_arrival_amount_sd": {"real": float(real_arrivals[day, firm]),
                                                   "wash": float(wash_arrivals[day, firm])},
                   "prior_decision": None}
            if prior_p >= 1:
                row["prior_decision"] = {"day": prior_p * interval,
                                         "semantic_action": int(d["actions"][prior_p, firm]),
                                         "amount_sd": float(d["amounts"][prior_p, firm]),
                                         "due_day": int(d["action_due_day"][prior_p, firm])}
                if "learning_choices" in d:
                    row["prior_decision"]["raw_choice"] = int(d["learning_choices"][prior_p, firm])
            hits.append(row)
            if stage == "training" and cfg["seed"] == 27001:
                first_example = {"hit": row, "prior_decisions_for_same_asset": []}
                for q in range(1, prior_p + 1):
                    decision_day = q * interval
                    due = int(d["action_due_day"][q, firm])
                    first_example["prior_decisions_for_same_asset"].append({
                        "decision_day": decision_day, "raw_choice": int(d["learning_choices"][q, firm]),
                        "semantic_action": int(d["actions"][q, firm]), "amount_sd": float(d["amounts"][q, firm]),
                        "due_day": due, "cost_fraction": float(d["cost_fraction"][q, firm]),
                        "resource_cost_next_day": float(costs[decision_day + 1, firm]),
                        "public_signal_before_due": float(d["public_signal"][due - 1, firm]) if 1 <= due <= days else None,
                        "public_signal_on_due": float(d["public_signal"][due, firm]) if 1 <= due <= days else None})
        for name, old_hash in hashes.items():
            assert sha((path.parent / name).read_bytes()) == old_hash, (str(path), name, "changed during read")
        if number % 32 == 0:
            print(f"read {number}/{len(paths)} archives; identified {len(hits)} hits", flush=True)
    current_after = {name: sha((ROOT / name).read_bytes()) for name in reviewed}
    assert current_after == current_before
    assert summary_path.read_bytes() == summary_bytes
    assert first_example is not None
    strata = {}
    for stage in ("training", "validation"):
        ws = [w for w in runs if w["stage"] == stage]
        rs = [r for r in hits if r["stage"] == stage]
        strata[stage] = aggregate(rs, ws)
        strata[stage]["rules"] = {}
        for rule in sorted({w["rule"] for w in ws}):
            rule_worlds = [w for w in ws if w["rule"] == rule]
            rule_rows = [r for r in rs if r["rule"] == rule]
            item = aggregate(rule_rows, rule_worlds)
            item["size_and_direction"] = {}
            for size in SIZE_NAMES:
                denominator = sum(w["asset_days_by_size"][size] for w in rule_worlds)
                item["size_and_direction"][size] = {"asset_days": denominator, "directions": {}}
                for direction in ("up", "down"):
                    selected = [r for r in rule_rows if r["size"] == size and r["direction"] == direction]
                    a = aggregate(selected, rule_worlds)
                    a["hits_per_million_asset_days"] = 1e6 * len(selected) / denominator if denominator else None
                    item["size_and_direction"][size]["directions"][direction] = a
            strata[stage]["rules"][rule] = item
    result = {"schema_version": 1, "scope": "read_only_completed_274_archives",
              "market_initializations": 0, "market_runs": 0,
              "archive_root": ARCHIVE.relative_to(ROOT).as_posix(), "archive_status": "complete",
              "summary_sha256": sha(summary_bytes), "script_sha256": sha(Path(__file__).read_bytes()),
              "reviewed_six_source_sha256_before": current_before,
              "reviewed_six_source_sha256_after": current_after,
              "common_archived_source_sha256": common_source,
              "verified_unique_source_zips": len(verified_source_zips),
              "prior_separate_financing_diagnostic": {
                  "path": "reports/disclosure_financing_checks_20261011/cap_diagnostic.md",
                  "sha256": sha((ROOT / "reports/disclosure_financing_checks_20261011/cap_diagnostic.md").read_bytes()),
                  "scope": "Superseded earlier financing archive; earlier bare-market prefix cap shows a possible baseline mechanism, not attribution of current 274 worlds. No repetition of its simulations."},
              "methods": {
                  "cap_location": "abs(log(P[t]/P[t-1])) equals configured cap, rtol=0, atol=1e-12; require exact daily hit-count match",
                  "news": "V_exogenous=V[t]-financing_adjustment+cost+fine-subsidy; telescope log(V_exogenous/V[t-1]), log((V[t]-financing_adjustment)/V_exogenous), log(V[t]/(V[t]-financing_adjustment))",
                  "remaining_bound": "s*remaining_raw_quote > cap-s*news_pass_through*log(V[t]/V[t-1]), s=sign(observed clipped return)",
                  "depth": "recur archived pricing EWMA variance/reference and depth equations from saved returns; compare saved daily cross-asset mean",
                  "timing": "project arrivals, next-day commitments and financing repricing precede quote; same-day firm decision/audit follows quote",
                  "scheduled_arrivals": "sum positive scheduled amounts whose saved due_day equals quote day; clipping can reduce realized increment",
                  "event_counts": "each event counted once per capped asset-day; overlapping events are not mutually exclusive",
                  "inference": "descriptive accounting diagnosis, no threshold changes, candidate selection, fitting or counterfactual simulations"},
              "overall": aggregate(hits, runs), "by_stage": strata,
              "first_seed_27001": first_example, "worlds": runs, "hits": hits,
              "limits": [
                  "Full investor/noise holdings, raw prequote net order flow, maker inventory, transient impact and expected-flow states were not archived.",
                  "Remaining quote is a signed combined lower bound; it cannot be separated exactly into permanent, transient and inventory channels.",
                  "Executed whole-market gross volume follows final-price cash caps; it is not firm-specific signed prequote flow.",
                  "No same-day corporate news does not exclude delayed action effects through public signals, tastes, holdings or other firms.",
                  "Same-day decision/audit is after quote; coincidence does not make that day's new choice or audit the cause of its quote.",
                  "All training worlds and all three validation rules remain included, including mechanical failures and burn-in caps.",
                  "Finite simulation samples and no counterfactual run cannot identify a unique root cause or justify algorithm/policy effectiveness."]}
    (OUT / "cap_diagnostic.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    lines = ["# 274份冻结归档：价格截断只读诊断", "",
             f"已核对{len(runs)}个complete世界、{len(hits)}次截断；0次新增市场运行。全部result、validation和source.zip与各自manifest哈希一致，六源文件前后未变。逐日截断资产数与归档price_cap_hits完全一致（绝对浮点容差1e-12，rtol=0）。", "",
             "|阶段/规则|世界|有截断世界|截断次数|预热期次数|无任何公司成本/罚款/补贴入账的截断|新闻不足半幅，其他报价项必超半幅|",
             "|---|---:|---:|---:|---:|---:|---:|"]
    for stage, group in strata.items():
        for rule, a in group["rules"].items():
            lines.append(f"|{stage}/{rule}|{a['worlds']}|{a['worlds_with_caps']}|{a['cap_hits']}|{a['during_burn_in']}|{a['without_any_firm_applied_cost_fine_or_subsidy']}|{a['remaining_quote_required_above_half_cap']}|")
    a = result["overall"]
    lines += ["", "以下事件按截断资产日计数，可重叠。决策与核查发生在当日收盘报价之后，不能用同日巧合倒置因果；成本/罚款/补贴在下一交易日进入价值锚。连续NPV没有日账字段，已按决策日fraction×收盘价格重建，离散规则日账另作交叉核对。", ""]
    labels = {"asset_resource_cost": "本公司当日成本", "asset_fine": "本公司当日罚款", "asset_subsidy": "本公司当日补贴",
              "asset_scheduled_real_arrival": "本公司真实项目预定实施", "asset_scheduled_wash_arrival": "本公司虚报预定到期",
              "financing_repricing_before_quote": "报价前融资重定价", "decision_and_audit_after_quote": "报价后决策/核查",
              "asset_audit_selected_after_quote": "报价后本公司被核查", "asset_detection_after_quote": "报价后本公司被查出"}
    lines += [f"- {label}：{a['events'][key]}次。" for key, label in labels.items()]
    bound = a["signed_remaining_quote_strict_lower_bound"]
    news_stats = a["signed_news_toward_cap"]
    lines += ["", f"沿截断方向的新闻报价贡献中位数{news_stats['median']:.6g}，5%–95%分位{news_stats['quantile_05']:.6g}至{news_stats['quantile_95']:.6g}。其余报价合成项严格下界中位数{bound['median']:.6g}；{a['remaining_quote_required_above_half_cap']}/{a['cap_hits']}次必须由其余项提供超过半个截断幅度。该合成项包含永久订单冲击、暂时冲击变化和做市商库存倾斜，不能把下界直接等同实际订单流。", "",
              "|阶段/规则|规模|涨截断|跌截断|资产日分母|", "|---|---|---:|---:|---:|"]
    for stage, group in strata.items():
        for rule, a in group["rules"].items():
            for size, x in a["size_and_direction"].items():
                lines.append(f"|{stage}/{rule}|{size}|{x['directions']['up']['cap_hits']}|{x['directions']['down']['cap_hits']}|{x['asset_days']}|")
    h = first_example["hit"]
    q = h["quote"]
    lines += ["", f"首个种子27001：第{h['day']}天，0基公司index={h['firm_index_zero_based']}，涨截断；该日处于预热期，无任何公司成本/罚款/补贴入账，无项目预定到期，也不是决策/核查或融资重定价日。本公司持续融资调整{h['accounting']['financing_adjustment']:.10g}，总新闻log变动{h['accounting']['total_log_news']:.10g}，新闻报价项{q['news_log_return_contribution']:.10g}；其余报价项必须>{q['signed_remaining_quote_strict_lower_bound']:.10g}。由保存收益递推本资产深度为{h['depth']['asset_fraction']:.10g}，市场均值{h['depth']['market_mean_fraction']:.10g}。", "",
              "该公司第240天虚报投入.16初始SD，第260天到期，距截断15天；之前投入不能据此排除。首种子只排除‘同日大支出/罚款/融资新闻直接占主导’这一解释，没有将全部截断证明为与企业行为无关。市场报价的订单/暂时冲击/库存通道及企业大投入的间接传导仍需保留对照检验，不能直接据此提高截断阈值。", "",
              "已读早期disclosure_financing_checks_20261011/cap_diagnostic.md。该独立旧诊断曾用bare市场前缀复现23002的截断，说明基础市场本身可产生类似事件；它针对已标superseded的另一归档，不能当作当前274世界的直接因果分解。本次没有重复其模拟。", "",
              "完整持仓、预报价有符号净订单、库存和暂时/预期流状态未归档，不能完全分解报价，也不能从已执行的全市场gross_volume反推出本公司报价前净流。本诊断没有重新生成轨迹、改变默认参数或挑选种子；训练与验证所有失败、预热期截断均保留，不支持算法/政策效果或经验校准通过的结论。逐hit账目、时序、方向、规模及所有输入哈希见cap_diagnostic.json。", ""]
    (OUT / "cap_diagnostic.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"worlds": len(runs), "hits": len(hits), "stages": {
        stage: {"worlds": x["worlds"], "worlds_with_caps": x["worlds_with_caps"], "cap_hits": x["cap_hits"]}
        for stage, x in strata.items()}, "outputs": ["cap_diagnostic.json", "cap_diagnostic.md"]}))


if __name__ == "__main__":
    main()
