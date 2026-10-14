"""Stage D.1: how large are action effects relative to reward noise, in the current main setting?

Runs fully exploring Q-learning worlds (epsilon = 1, so the choice is randomized: uniform over legal kinds,
then over legal amplitudes) under the baseline policy. Records each decision's state, choice, realized
period rewards, and the shared-grid NPV candidate values. Because choices are random, regressing the
discounted sum of a firm's next H period rewards on its current choice (with group x state fixed effects)
estimates each choice's causal effect on the learner's own reward, with its sampling noise.

Usage: python snr_probe.py [--workers 8]
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(HERE))

from abm.disclosure import game  # noqa: E402
from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.game import DisclosureMarket  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402
from abm.tabular import CompanyQLearner  # noqa: E402
from probe import DOMAIN_PATH, GRID, MAIN  # noqa: E402

SEEDS = tuple(range(30101, 30109))
RUNS = HERE / "runs"


def run_world(seed: int) -> str:
    domain = load_domain(DOMAIN_PATH)
    config = MarketConfig(seed=seed, firm_policy="q_learning", firm_action_fractions=GRID, **MAIN)
    learner = CompanyQLearner(groups=6, actions=2 * len(GRID) + 1, epsilon=1.0, learning_rate=.1)
    market = DisclosureMarket(config, domain, PolicySchedule.constant(domain), learner=learner, training=True)
    values, prices = [], []
    original = game.discrete_candidates

    def wrapped(**kwargs):
        result = original(**kwargs)
        values.append(result.values.copy())
        prices.append(market.prices.copy())
        return result

    game.discrete_candidates = wrapped
    try:
        result = market.run()
    finally:
        game.discrete_candidates = original
    path = RUNS / f"snr_{seed}.npz"
    np.savez_compressed(
        path, npv_values=np.stack(values), decision_prices=np.stack(prices), initial_prices=result.market.prices[0],
        groups=result.learning_groups, states=result.learning_states, choices=result.learning_choices,
        valid=result.valid_actions, rewards=result.learning_rewards, transition=result.learning_transition,
        kinds=result.actions, amounts=result.amounts, size=market.firms.size_class,
    )
    return str(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    RUNS.mkdir(exist_ok=True)
    with ProcessPoolExecutor(args.workers, initializer=disable_power_throttling) as pool:
        for path in pool.map(run_world, SEEDS):
            print(path, flush=True)


if __name__ == "__main__":
    main()
