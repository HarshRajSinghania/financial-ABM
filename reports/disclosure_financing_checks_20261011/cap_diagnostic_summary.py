"""Derive cap diagnostics from preserved outputs, without another market replay."""

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
REPORT = Path(__file__).with_name("cap_diagnostic.json")
diagnostic = json.loads(REPORT.read_text(encoding="utf-8"))
bare, large = diagnostic["replays"]
event = bare["cap_events"][0]
cfg = bare["config"]
flow_gain = (cfg["permanent_impact_fraction"] + (1 - cfg["permanent_impact_fraction"]) / event["depth_fraction"]) * cfg["price_impact"] / cfg["liquidity_fraction"]
investor_flow = flow_gain * event["net_investor_shares"]
noise_flow = flow_gain * event["net_noise_shares"]
derived = {"diagnostic_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
           "bare_event_contemporaneous_flow_decomposition": {
               "log_move_per_net_share": flow_gain,
               "investor_current_flow": investor_flow, "noise_current_flow": noise_flow,
               "prior_transient_and_expected_flow_memory": event["raw_move"] - investor_flow - noise_flow - event["components"]["news"] - event["components"]["inventory_skew"],
               "identity": "raw = investor current flow + noise current flow + prior memory + news + inventory skew"},
           "archive_volatility_state": [], "archive_hashes_match_original_manifests": True}
for row in diagnostic["archive_scan"]:
    path = ROOT / row["archive"]["path"]
    manifest = json.loads(path.with_name("manifest.json").read_text(encoding="utf-8"))
    derived["archive_hashes_match_original_manifests"] &= row["archive"]["sha256"] == manifest["artifacts"]["result.npz"]
    if row["seed"] != 23002 or row["scenario"] not in (
        "market_B", "zero_financing_exposure", "zero_financing_spread", "zero_impact_B"
    ):
        continue
    config = manifest["config"]
    with np.load(path, allow_pickle=False) as arrays:
        prices = arrays["market_prices"]
        mean_depth = arrays["market_mean_depth_fraction"]
    returns = np.diff(np.log(prices), axis=0)
    variance = np.full(config["n_firms"], config["initial_asset_volatility"]**2 / 252)
    reference = variance.copy()
    for moves in returns[:359]:
        variance = config["variance_ewma_decay"] * variance + (1 - config["variance_ewma_decay"]) * moves**2
        reference = config["reference_variance_decay"] * reference + (1 - config["reference_variance_decay"]) * moves**2
    ratio = float(np.sqrt(variance[12] / reference[12]))
    derived["archive_volatility_state"].append({"scenario": row["scenario"],
        "pre_day360_volatility_ratio_asset12": ratio,
        "noise_volatility_multiplier_asset12": min(ratio, 4)**config["noise_volatility_exponent"],
        "mean_depth_day360": float(mean_depth[360]),
        "cap_boundary_returns_after_day600": int(np.count_nonzero(np.isclose(np.abs(returns[600:]), config["max_log_return"], atol=1e-12, rtol=0)))})
null_root = ROOT / "reports/disclosure_financing_development_20261011_v1"
with np.load(null_root / "zero_financing_exposure/seed_23002/attempt_001/result.npz", allow_pickle=False) as left, np.load(
    null_root / "zero_financing_spread/seed_23002/attempt_001/result.npz", allow_pickle=False
) as right:
    derived["null_pricing_diagnostic_equal_including_nan"] = bool(np.array_equal(left["pricing_slope"], right["pricing_slope"], equal_nan=True))
derived["summary_code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path(__file__).with_name("cap_diagnostic_derived.json").write_text(
    json.dumps(derived, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8"
)
print(json.dumps(derived, indent=2))
