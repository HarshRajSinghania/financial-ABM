"""Read archived cap events and replay two explicitly bounded development prefixes."""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import DomainSpec
from abm.disclosure.game import DisclosureMarket
from abm.disclosure.harness import CrossSectionMarket, _cap_buys_to_cash
from abm.disclosure.investors import InvestorPopulation
from abm.disclosure.market import CrossSectionBook


ROOT = Path(__file__).resolve().parents[2]
ARCHIVES = ROOT / "reports/disclosure_financing_development_20261011_v1"
OUTPUT = Path(__file__).with_suffix(".json")
PREFIX_DAYS = 400


def identity(path):
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def archive_scan():
    rows = []
    paths = {}
    for path in sorted(ARCHIVES.glob("*/seed_*/attempt_*/result.npz")):
        manifest = json.loads(path.with_name("manifest.json").read_text(encoding="utf-8"))
        validation = json.loads(path.with_name("validation.json").read_text(encoding="utf-8"))
        scenario, seed = path.parents[2].name, manifest["config"]["seed"]
        paths[(scenario, seed)] = path
        with np.load(path, allow_pickle=False) as arrays:
            days = np.flatnonzero(arrays["market_price_cap_hits"])
            row = {"scenario": scenario, "seed": seed, "mechanical": validation["mechanical"]["status"],
                   "mechanical_checks": validation["mechanical"]["checks"],
                   "total_cap_hits": int(arrays["market_price_cap_hits"].sum()), "cap_events": [],
                   "archive": identity(path)}
            for day in days:
                prices = arrays["market_prices"]
                moves = np.log(prices[day] / prices[day - 1])
                assets = np.flatnonzero(np.isclose(np.abs(moves), manifest["config"]["max_log_return"], atol=1e-12, rtol=0))
                for asset in assets:
                    row["cap_events"].append({"day": int(day), "asset_zero_based": int(asset),
                                              "log_return": float(moves[asset]), "initial_cap": float(prices[0, asset]),
                                              "previous_cap": float(prices[day - 1, asset]),
                                              "size_class": int(arrays["market_size_class"][asset])})
        rows.append(row)
    with np.load(paths[("zero_financing_exposure", 23002)], allow_pickle=False) as left, np.load(
        paths[("zero_financing_spread", 23002)], allow_pickle=False
    ) as right:
        comparison = {key: bool(np.array_equal(left[key], right[key])) for key in left.files if key in right.files}
        comparison["maximum_absolute_price_difference"] = float(np.max(np.abs(left["market_prices"] - right["market_prices"])))
    return rows, comparison


def replay(config, domain, *, bare):
    market = CrossSectionMarket(config) if bare else DisclosureMarket(config, domain)
    initial_wealth = market.investors.wealth(market.prices)
    initial_weights = initial_wealth / initial_wealth.sum()
    record = {"model": type(market).__name__, "config": config.to_dict(), "completed_days": 0,
              "initial_wealth_max_share": float(initial_weights.max()),
              "initial_wealth_hhi": float(initial_weights @ initial_weights),
              "initial_cap_min": float(market.prices.min()), "initial_cap_max": float(market.prices.max()),
              "daily_snapshots": [], "cap_events": [], "maximum_absolute_raw_move": 0.0}
    original_orders = InvestorPopulation.desired_orders
    original_moves = CrossSectionBook.price_moves
    state = {"day": 0}

    def capture_orders(self, who, **kwargs):
        orders = original_orders(self, who, **kwargs)
        prices = kwargs["prices"]
        constrained = _cap_buys_to_cash(np.maximum(orders, -self.holdings[who]), self.cash[who], prices,
                                      config.transaction_cost_rate)
        wealth = self.wealth(prices)
        state["orders"] = {"who": who.copy(), "constrained": constrained,
                           "wealth": wealth, "market_expected_return": kwargs["market_expected_return"],
                           "market_annual_variance": kwargs["market_annual_variance"]}
        return orders

    def capture_moves(self, net_flow_value, market_cap, news, inventory_gap):
        transient_before = self.transient_impact.copy()
        moves, capped = original_moves(self, net_flow_value, market_cap, news, inventory_gap)
        flow = config.price_impact * net_flow_value / (config.liquidity_fraction * market_cap)
        components = {"news": config.news_pass_through * news,
                      "permanent_flow": config.permanent_impact_fraction * flow,
                      "transient_change": self.transient_impact - transient_before,
                      "inventory_skew": config.market_maker_inventory_skew * inventory_gap}
        raw = sum(components.values())
        extreme = int(np.argmax(np.abs(raw)))
        if abs(raw[extreme]) > record["maximum_absolute_raw_move"]:
            record["maximum_absolute_raw_move"] = float(abs(raw[extreme]))
            record["maximum_raw_move_day"] = state["day"]
            record["maximum_raw_move_asset_zero_based"] = extreme
            record["maximum_raw_move_signed"] = float(raw[extreme])
        inspect = set(np.flatnonzero(capped).tolist())
        if state["day"] in (1, 359, 360, 361):
            inspect.add(12 if bare else extreme)
        for asset in sorted(inspect):
            orders = state["orders"]
            who, q, wealth = orders["who"], orders["constrained"][:, asset], orders["wealth"]
            net_investor = float(q.sum())
            net_total = float(net_flow_value[asset] / market_cap[asset])
            indices = np.argsort(-np.abs(q))[:5]
            snapshot = {"day": state["day"], "asset_zero_based": asset, "capped": bool(capped[asset]),
                        "raw_move": float(raw[asset]), "actual_move": float(moves[asset]),
                        "components": {key: float(values[asset]) for key, values in components.items()},
                        "previous_cap": float(market_cap[asset]), "depth_fraction": float(self.depth_fraction[asset]),
                        "net_investor_shares": net_investor, "net_noise_shares": net_total - net_investor,
                        "deciding_investors": int(who.size), "deciding_wealth_share": float(wealth[who].sum() / wealth.sum()),
                        "market_expected_return": float(orders["market_expected_return"]),
                        "allocation_market_annual_variance": float(orders["market_annual_variance"]),
                        "top_absolute_investor_orders": [
                            {"investor_zero_based": int(who[index]), "shares": float(q[index]),
                             "wealth_share": float(wealth[who[index]] / wealth.sum()),
                             "risk_aversion": float(market.investors.risk_aversion[who[index]]),
                             "decision_interval": int(market.investors.decision_interval[who[index]]),
                             "decision_offset": int(market.investors.decision_offset[who[index]])}
                            for index in indices],
                        "noise_holdings_before": float(market.noise_holdings[asset]),
                        "noise_inventory_target": float(market.noise_target[asset])}
            record["daily_snapshots"].append(snapshot)
            if capped[asset]:
                record["cap_events"].append(snapshot)
        return moves, capped

    InvestorPopulation.desired_orders = capture_orders
    CrossSectionBook.price_moves = capture_moves
    started = time.perf_counter()
    try:
        for day_index in range(PREFIX_DAYS):
            state["day"] = day_index + 1
            market.step(day_index)
            record["completed_days"] = day_index + 1
    except Exception as error:
        record["failure"] = {"type": type(error).__name__, "message": str(error)}
    finally:
        InvestorPopulation.desired_orders = original_orders
        CrossSectionBook.price_moves = original_moves
    record["elapsed_seconds"] = time.perf_counter() - started
    record["total_cap_hits"] = int(market.price_cap_hits[:record["completed_days"] + 1].sum())
    record["final_price_sha256"] = hashlib.sha256(market.prices.tobytes()).hexdigest()
    if not bare:
        record["action_count_before_final_day"] = int(np.count_nonzero(market.action_history[1:record["completed_days"] // config.firm_decision_interval + 1] != 2))
    return record


def main():
    rows, null_comparison = archive_scan()
    print(json.dumps({"archives": len(rows), "archive_cap_days": sorted({e["day"] for r in rows for e in r["cap_events"]})}), flush=True)
    manifest = json.loads((ARCHIVES / "market_B/seed_23002/attempt_001/manifest.json").read_text(encoding="utf-8"))
    config = MarketConfig.from_dict(manifest["config"])
    domain = DomainSpec.from_dict(manifest["domain"])
    bare = replay(config, domain, bare=True)
    print(json.dumps({"replay": "bare_150_30", "caps": bare["total_cap_hits"], "seconds": bare["elapsed_seconds"]}), flush=True)
    large = replay(replace(config, n_investors=1000, n_firms=200), domain, bare=False)
    print(json.dumps({"replay": "disclosure_1000_200", "caps": large["total_cap_hits"], "seconds": large["elapsed_seconds"]}), flush=True)
    report = {"status": "development_diagnostic_only", "generated_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "All 45 preserved v1 archives plus one 400-day bare prefix and one 400-day 1000/200 disclosure prefix of seed 23002. No parameter, cap, seed or archive change.",
              "v1_superseded_for_accounting_bug": True, "archive_scan": rows,
              "zero_exposure_vs_zero_spread_array_equality": null_comparison,
              "replays": [bare, large],
              "limitations": ["Size changes alter stochastic array draws and model class changes; two prefixes are not an identified population-size effect.",
                              "No inference about cap frequency across independent seeds or days beyond 400.",
                              "The original no-cap validation gate is retained; a burn-in cap is not silently excluded."],
              "source_files": [identity(path) for path in sorted((ROOT / "src/abm/disclosure").glob("*.py"))],
              "diagnostic_code": identity(Path(__file__))}
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
