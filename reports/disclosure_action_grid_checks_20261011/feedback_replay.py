"""Instrument frozen development replays and require unchanged original results."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys
import tempfile
import time
import zipfile

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, payload):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, allow_nan=False, indent=2)
        handle.write("\n")


def replay(folder, snapshot, output_name):
    from abm.disclosure import harness
    from abm.disclosure.config import MarketConfig
    from abm.disclosure.domain import DomainSpec
    from abm.disclosure.game import DisclosureMarket
    from abm.disclosure.investors import InvestorPopulation
    from abm.disclosure.learning import load_frozen, table_fingerprint
    from abm.disclosure.market import CrossSectionBook
    from abm.disclosure.policy import PolicyRegime, PolicySchedule
    from abm.disclosure.runner import run_identity, save_result, source_hashes

    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "complete"
    assert manifest["source_hashes"] == source_hashes()
    assert manifest["python_version"] == platform.python_version()
    assert manifest["numpy_version"] == np.__version__
    hashes = {name: sha(folder / name) for name in manifest["artifacts"]}
    assert hashes == manifest["artifacts"]
    manifest_hash = sha(folder / "manifest.json")
    cfg = MarketConfig.from_dict(manifest["config"])
    assert cfg.trading_days == 1800 and cfg.noise_flow_scale > 0
    p = manifest["policy"]
    policy = PolicySchedule(PolicyRegime(**p["baseline"]),
                            PolicyRegime(**p["intervention"]) if p["intervention"] else None, p["start_day"])
    learning = manifest.get("learning") or {}
    learner = None
    if learning:
        learner, _ = load_frozen(folder / "input_model.npz")
        assert table_fingerprint(learner) == learning["initial_table_fingerprint"]
        if learning["training"]:
            learner.values, learner.counts = learner.values.copy(), learner.counts.copy()
        learner.epsilon = learning["epsilon"]
        assert learner.learning_rate == learning["learning_rate"] and learner.discount == learning["discount"]
    market = DisclosureMarket(cfg, DomainSpec.from_dict(manifest["domain"]), policy,
                              learner=learner, training=learning.get("training", False))
    assert run_identity(cfg, market.domain, policy, learning=manifest.get("learning"))["run_id"] == manifest["run_id"]
    names = ("raw", "moves", "news", "permanent_flow", "transient_change", "inventory_skew",
             "depth_fraction", "variance_ratio", "expected_flow_before", "transient_before",
             "noise_amplification", "investor_submitted", "noise_submitted", "investor_executed",
             "noise_executed", "submitted_net", "executed_net", "static_raw_at_executed_flow")
    arrays = {name: np.zeros((cfg.trading_days, cfg.n_firms)) for name in names}
    arrays["capped"] = np.zeros((cfg.trading_days, cfg.n_firms), dtype=bool)
    arrays["deciding_wealth_share"] = np.zeros(cfg.trading_days)
    arrays["deciding_count"] = np.zeros(cfg.trading_days, dtype=np.int64)
    arrays["allocation_market_variance"] = np.zeros(cfg.trading_days)
    state = {}
    original_cap = harness._cap_buys_to_cash
    original_orders = InvestorPopulation.desired_orders
    original_moves = CrossSectionBook.price_moves

    def capture_cap(orders, cash, prices, cost):
        result = original_cap(orders, cash, prices, cost)
        state["cash_calls"].append(result.copy())
        return result

    def capture_orders(self, who, **kwargs):
        result = original_orders(self, who, **kwargs)
        if "who" in state:
            return result
        row = state["row"]
        wealth = self.wealth(kwargs["prices"])
        arrays["deciding_wealth_share"][row] = wealth[who].sum() / wealth.sum()
        arrays["deciding_count"][row] = who.size
        arrays["allocation_market_variance"][row] = kwargs["market_annual_variance"]
        state.update(who=who.copy(), wealth=wealth)
        return result

    def capture_moves(self, net_flow_value, market_cap, news, inventory_gap):
        row = state["row"]
        before = self.transient_impact.copy()
        expected = self.expected_flow_impact.copy()
        ratio = np.sqrt(self.variance / self.reference_variance)
        moves, capped = original_moves(self, net_flow_value, market_cap, news, inventory_gap)
        flow = cfg.price_impact * net_flow_value / (cfg.liquidity_fraction * market_cap)
        raw = (cfg.news_pass_through * news + cfg.permanent_impact_fraction * flow
               + self.transient_impact - before + cfg.market_maker_inventory_skew * inventory_gap)
        assert np.array_equal(moves, np.clip(raw, -cfg.max_log_return, cfg.max_log_return))
        assert np.array_equal(capped, moves != raw)
        values = {"raw": raw, "moves": moves, "capped": capped,
                  "news": cfg.news_pass_through * news,
                  "permanent_flow": cfg.permanent_impact_fraction * flow,
                  "transient_change": self.transient_impact - before,
                  "inventory_skew": cfg.market_maker_inventory_skew * inventory_gap,
                  "depth_fraction": self.depth_fraction, "variance_ratio": ratio,
                  "noise_amplification": np.minimum(ratio, 4.0) ** cfg.noise_volatility_exponent,
                  "expected_flow_before": expected, "transient_before": before,
                  "submitted_net": net_flow_value / market_cap}
        for name, value in values.items():
            arrays[name][row] = value
        return moves, capped

    harness._cap_buys_to_cash = capture_cap
    InvestorPopulation.desired_orders = capture_orders
    CrossSectionBook.price_moves = capture_moves
    events = []
    started = time.perf_counter()
    try:
        for row in range(cfg.trading_days):
            state.clear()
            state.update(row=row, cash_calls=[])
            inventory_before = market.market_maker_inventory.copy()
            market.step(row)
            submitted, noise_submitted, executed, noise_executed = state["cash_calls"]
            assert submitted.shape == executed.shape == (state["who"].size, cfg.n_firms)
            assert noise_submitted.shape == noise_executed.shape == (1, cfg.n_firms)
            arrays["investor_submitted"][row] = submitted.sum(axis=0)
            arrays["noise_submitted"][row] = noise_submitted[0]
            arrays["investor_executed"][row] = executed.sum(axis=0)
            arrays["noise_executed"][row] = noise_executed[0]
            net = executed.sum(axis=0) + noise_executed[0]
            arrays["executed_net"][row] = net
            np.testing.assert_allclose(arrays["submitted_net"][row], submitted.sum(axis=0) + noise_submitted[0], rtol=1e-13, atol=1e-15)
            np.testing.assert_allclose(net, inventory_before - market.market_maker_inventory, rtol=1e-13, atol=1e-15)
            flow = cfg.price_impact * net / cfg.liquidity_fraction
            before = arrays["transient_before"][row]
            transient = (cfg.transient_impact_decay * before + (1 - cfg.permanent_impact_fraction)
                         * (flow / arrays["depth_fraction"][row] - arrays["expected_flow_before"][row]))
            arrays["static_raw_at_executed_flow"][row] = (arrays["news"][row] + cfg.permanent_impact_fraction * flow
                                                         + transient - before + arrays["inventory_skew"][row])
            for asset in np.flatnonzero(arrays["capped"][row]):
                who = state["who"]
                ranks = np.argsort(-np.abs(submitted[:, asset]))[:5]
                events.append({"day": row + 1, "asset_zero_based": int(asset),
                               "size_class": int(market.firms.size_class[asset]),
                               **{name: float(arrays[name][row, asset]) for name in names},
                               "deciding_count": int(arrays["deciding_count"][row]),
                               "deciding_wealth_share": float(arrays["deciding_wealth_share"][row]),
                               "allocation_market_variance": float(arrays["allocation_market_variance"][row]),
                               "top_investor_submitted_orders": [
                                   {"investor_zero_based": int(who[j]), "submitted_shares": float(submitted[j, asset]),
                                    "executed_shares": float(executed[j, asset]),
                                    "wealth_share": float(state["wealth"][who[j]] / state["wealth"].sum()),
                                    "decision_interval": int(market.investors.decision_interval[who[j]]),
                                    "decision_offset": int(market.investors.decision_offset[who[j]])} for j in ranks]})
        result = market.run()
    finally:
        harness._cap_buys_to_cash = original_cap
        InvestorPopulation.desired_orders = original_orders
        CrossSectionBook.price_moves = original_moves
    assert result.fingerprint() == manifest["result_fingerprint"]
    fresh = snapshot / (output_name + "_result.npz")
    save_result(fresh, result)
    with np.load(fresh, allow_pickle=False) as new, np.load(folder / "result.npz", allow_pickle=False) as old:
        assert set(new.files) == set(old.files)
        for name in old.files:
            assert new[name].dtype == old[name].dtype and new[name].shape == old[name].shape
            assert new[name].tobytes() == old[name].tobytes(), name
        fields = len(old.files)
    if learner is not None:
        final_model, _ = load_frozen(folder / "output_model.npz")
        assert table_fingerprint(learner) == table_fingerprint(final_model)
    assert arrays["capped"].sum() == result.market.price_cap_hits.sum() == len(events)
    assert np.array_equal(arrays["capped"].sum(axis=1), result.market.price_cap_hits[1:])
    assert hashes == {name: sha(folder / name) for name in hashes}
    assert manifest_hash == sha(folder / "manifest.json")
    target = HERE / (output_name + ".npz")
    with target.open("xb") as handle:
        np.savez_compressed(handle, **arrays)
    delta = arrays["static_raw_at_executed_flow"] - arrays["raw"]
    return {"archive": folder.relative_to(ROOT).as_posix(), "status": "PASS", "seed": cfg.seed,
            "rule": cfg.firm_policy, "training": learning.get("training", False),
            "elapsed_seconds": time.perf_counter() - started, "result_fingerprint": result.fingerprint(),
            "bitwise_equal_fields": fields, "final_table_equal": learner is not None,
            "source_hashes": manifest["source_hashes"], "manifest_sha256": manifest_hash,
            "original_artifact_hashes": hashes, "telemetry": {"name": target.name, "sha256": sha(target)},
            "cap_count": len(events), "caps": events,
            "all_days": {"maximum_absolute_raw": float(np.abs(arrays["raw"]).max()),
                         "maximum_submitted_executed_difference": float(np.abs(arrays["submitted_net"] - arrays["executed_net"]).max()),
                         "maximum_static_quote_difference": float(np.abs(delta).max()),
                         "static_executed_flow_cap_count": int((np.abs(arrays["static_raw_at_executed_flow"]) > cfg.max_log_return).sum())},
            "original_archives_unchanged": True}


def main():
    spec_path = HERE / "feedback_replay_spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    archive = ROOT / spec["archive"]
    summary_manifest = archive / "summary_manifest.json"
    summary = json.loads(summary_manifest.read_text(encoding="utf-8"))
    assert summary["experiment_id"] == spec["experiment_id"]
    stamp = {"created_utc": datetime.now(timezone.utc).isoformat(), "spec_sha256": sha(spec_path),
             "script_sha256": sha(Path(__file__)), "summary_manifest_sha256": sha(summary_manifest), "specification": spec}
    write(HERE / "feedback_replay_manifest.json", stamp)
    with tempfile.TemporaryDirectory(prefix="abm-feedback-source-") as temporary:
        snapshot = Path(temporary).resolve()
        with zipfile.ZipFile(archive / spec["cases"][0] / "source.zip") as z:
            assert set(z.namelist()) == set(summary["source_hashes"])
            for name in z.namelist():
                payload = z.read(name)
                assert hashlib.sha256(payload).hexdigest() == summary["source_hashes"][name]
                path = snapshot / name
                assert path.resolve().is_relative_to(snapshot)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(payload)
        sys.path.insert(0, str(snapshot))
        from abm.disclosure.runner import source_hashes
        assert source_hashes() == summary["source_hashes"]
        cases = []
        for index, case in enumerate(spec["cases"]):
            outcome = replay(archive / case, snapshot, f"feedback_replay_{index + 1:02d}")
            cases.append(outcome)
            print(json.dumps({"completed": index + 1, "planned": len(spec["cases"]), "case": case,
                              "status": outcome["status"], "caps": outcome["cap_count"]}), flush=True)
        assert source_hashes() == summary["source_hashes"]
    assert stamp["spec_sha256"] == sha(spec_path) and stamp["script_sha256"] == sha(Path(__file__))
    assert stamp["summary_manifest_sha256"] == sha(summary_manifest)
    write(HERE / "feedback_replay.json", {"status": "PASS", "manifest": stamp, "cases": cases,
          "limitations": ["Cases were chosen after failures; this is not an independent incidence estimate.",
                          "Static executed-flow quotes hold other state fixed and do not solve clearing or a path counterfactual.",
                          "Bitwise reproduction validates telemetry, not economic realism or the failed no-cap gate."]})


if __name__ == "__main__":
    main()
