"""Stage D.1 probe: run time and discrete-candidate NPV values in the current main setting.

Runs one world per firm rule (baseline policy, main setting of contract sections 14-18) and records,
for every npv_discrete decision, the candidate values from the shared candidate builder. Read-only wrapper.

Usage: python probe.py --seed 30001 [--q]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import game  # noqa: E402
from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.game import DisclosureMarket  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402
from abm.tabular import CompanyQLearner  # noqa: E402

DOMAIN_PATH = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json"
MAIN = dict(n_investors=1000, n_firms=200, trading_days=3500, burn_in_days=1200,
            financing_exposure_fraction=0.5, financing_spread=0.05, financing_repricing_interval=60,
            financing_horizon_days=1260, firm_discount_rate=0.05, intrinsic_value_log_sd=0.9151544344205937,
            initial_impact_share=0.2, taste_median=0.0724, imitation_rule="pairwise")
GRID = (.01, .02, .04, .08, .16, .32, .64, 1.0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=30001)
    parser.add_argument("--q", action="store_true", help="also time one Q-learning training world")
    parser.add_argument("--grid", type=float, nargs="+", default=list(GRID))
    args = parser.parse_args()
    disable_power_throttling()
    domain = load_domain(DOMAIN_PATH)
    policy = PolicySchedule.constant(domain)
    recorded = []
    original = game.discrete_candidates

    def wrapped(**kwargs):
        result = original(**kwargs)
        recorded.append((result.values.copy(), result.valid_actions.copy(), result.kinds.copy()))
        return result

    game.discrete_candidates = wrapped
    timing = {}
    config = MarketConfig(seed=args.seed, firm_policy="npv_discrete", firm_action_fractions=tuple(args.grid), **MAIN)
    start = time.perf_counter()
    market = DisclosureMarket(config, domain, policy)
    result = market.run()
    timing["npv_discrete"] = time.perf_counter() - start
    game.discrete_candidates = original
    values = np.stack([v for v, _, _ in recorded])
    valid = np.stack([m for _, m, _ in recorded])
    kinds = recorded[0][2]
    masked = np.where(valid, values, -np.inf)
    best = masked.max(axis=2)
    maintain = values[:, :, 2]
    best_improve = np.where(valid & (kinds == 0), values, -np.inf).max(axis=2)
    best_wash = np.where(valid & (kinds == 1), values, -np.inf).max(axis=2)
    size = market.firms.size_class
    out = {"seed": args.seed, "grid": args.grid, "timing_seconds": timing,
           "actions_by_kind": np.bincount(result.actions.ravel(), minlength=3).tolist()}
    rows = {}
    for label, cls in (("large", 0), ("mid", 1), ("small", 2), ("all", None)):
        use = np.ones_like(best, dtype=bool) if cls is None else np.broadcast_to(size == cls, best.shape)
        gap = (best - maintain)[use] * 1e4
        rows[label] = {
            "best_minus_maintain_bp_quantiles": np.quantile(gap, [.1, .25, .5, .75, .9]).tolist(),
            "share_best_is_not_maintain": float((gap > 1e-5).mean()),
            "improve_minus_maintain_bp_median": float(np.median((best_improve - maintain)[use][np.isfinite(best_improve[use])]) * 1e4),
            "wash_minus_maintain_bp_median": float(np.median((best_wash - maintain)[use][np.isfinite(best_wash[use])]) * 1e4),
        }
    out["npv_values"] = rows
    if args.q:
        learner = CompanyQLearner(groups=6, actions=2 * len(args.grid) + 1, epsilon=1.0, learning_rate=.1)
        config = MarketConfig(seed=args.seed, firm_policy="q_learning", firm_action_fractions=tuple(args.grid), **MAIN)
        start = time.perf_counter()
        DisclosureMarket(config, domain, policy, learner=learner, training=True).run()
        timing["q_learning_training"] = time.perf_counter() - start
    print(json.dumps(out, indent=2))
    (HERE / f"probe_{args.seed}.json").write_text(json.dumps(out, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
