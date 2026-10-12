"""Independent deterministic checks; no market initialization or simulation."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import runner, training
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.learning import realized_rewards, table_fingerprint
from abm.disclosure.policy import PolicySchedule
from abm.tabular import CompanyQLearner


def rng_compatibility():
    old = np.random.SeedSequence([25019, 1]).spawn(4)
    new = np.random.SeedSequence([25019, 1]).spawn(5)
    for previous, current in zip(old, new[:4], strict=True):
        np.testing.assert_array_equal(np.random.default_rng(previous).random(100),
                                      np.random.default_rng(current).random(100))
    return {"existing_streams": 4, "draws_per_stream": 100}


def reward_windows():
    savings, costs, fines, subsidies = [np.zeros((181, 2)) for _ in range(4)]
    savings[1:] = [.003, .005]
    costs[61] = [.4, .7]
    fines[121] = [.2, .1]
    subsidies[61] = [.1, .2]
    cap, rate = np.array([2., 3.]), .05
    reward = lambda start, end: realized_rewards(savings, costs, fines, subsidies, cap,
                                                start_day=start, end_day=end,
                                                annual_discount_rate=rate)
    earlier, later = reward(60, 120), reward(120, 180)
    np.testing.assert_allclose(earlier + np.exp(-rate * 60 / 252) * later, reward(60, 180),
                               rtol=1e-14, atol=1e-16)
    daily = np.exp(-rate * np.arange(1, 61) / 252).sum() * savings[1] / cap
    np.testing.assert_allclose(earlier, daily + np.exp(-rate / 252) * (-costs[61] + subsidies[61]) / cap)
    np.testing.assert_allclose(later, daily - np.exp(-rate / 252) * fines[121] / cap)
    return {"previous_window_reward": earlier.tolist(), "new_window_reward": later.tolist(),
            "fine_application_day": 121, "older_project_savings_continue": True}


def coverage_masks_and_worlds():
    config = MarketConfig(n_investors=6, n_firms=2, trading_days=120, burn_in_days=0,
                          firm_policy="q_learning")
    learner = CompanyQLearner(groups=6)
    learner.counts.fill(20)
    learner.counts[0, 0, 1] = 0
    daily, periods = np.zeros((121, 2)), np.zeros((3, 2))
    masks = np.ones((3, 2, 3), dtype=bool)
    masks[:, :, 1] = False
    masks[2, 0, 1] = True
    result = SimpleNamespace(
        learning_groups=periods.astype(np.int64), learning_states=periods.astype(np.int64),
        valid_actions=masks, unvisited_state=np.zeros((3, 2), dtype=bool),
        financing_value_adjustment=daily, applied_resource_cost=daily,
        applied_fine=daily, applied_subsidy=daily, learning_transition=periods.astype(bool),
        action_due_day=np.full((3, 2), -1), actions=np.full((3, 2), 2), amounts=periods,
        cost_fraction=periods, penalty_fraction=periods, subsidy_fraction=periods,
        market=SimpleNamespace(prices=np.ones((121, 2))), inflation=daily,
    )
    first = runner.learning_report(result, config, learner, training=False)["coverage"]
    assert first["status"] == "FAIL"
    assert first["common_state_undercovered_actions"] == [{"group": 0, "state": 0, "action": 1, "count": 0}]
    masks[:, :, 1] = False
    assert runner.learning_report(result, config, learner, training=False)["coverage"]["status"] == "PASS"
    counts = np.full((6, 81, 3), 20, dtype=np.int64)
    counts[0, 1] = 0
    records = []
    for seed, state, number in ((25101, 0, 1000), (25102, 1, 10)):
        visits, legal = np.zeros((6, 81), dtype=np.int64), np.zeros((6, 81, 3), dtype=np.int64)
        visits[0, state], legal[0, state] = number, number
        records.append({"phase": "validation", "firm_policy": "q_learning", "status": "complete", "seed": seed,
                        "learning": {"coverage": {"visits": visits.tolist(), "legal_action_visits": legal.tolist(),
                                                   "decisions": number, "unseen_state_decisions": number if state else 0}}})
    pooled = training._coverage(records, counts, 2)
    assert pooled["unseen_state_fraction"] < .05 and pooled["status"] == "FAIL"
    assert [world["status"] for world in pooled["worlds"]] == ["PASS", "FAIL"]
    return {"mask_union_detects_unselected_legal_action": True, "never_legal_action_excluded": True,
            "pooled_unseen_fraction": pooled["unseen_state_fraction"], "individual_world_failure_retained": True}


def model_and_environment_identity():
    config = MarketConfig()
    domain = load_domain(ROOT / "configs/domains/esg.json")
    policy = PolicySchedule.constant(domain)
    contract = runner.learning_contract(config, domain, policy)
    assert runner.learning_contract(replace(config, seed=config.seed + 1, firm_policy="q_learning"), domain, policy) == contract
    assert runner.learning_contract(replace(config, firm_discount_rate=.06), domain, policy) != contract
    assert runner.learning_contract(config, replace(domain, natural_decay=domain.natural_decay + .001), policy) != contract
    assert runner.learning_contract(config, domain, policy.with_intervention(601, transparency=.6)) != contract
    assert contract["python_version"] == platform.python_version() and contract["numpy_version"] == np.__version__
    learner = CompanyQLearner(groups=6)
    original = table_fingerprint(learner)
    learner.counts[0, 0, 0] = 1
    assert table_fingerprint(learner) != original
    learner.counts.fill(0)
    learner.counts = learner.counts.astype(np.int32)
    assert table_fingerprint(learner) != original
    return {"excluded_fields": ["seed", "firm_policy"], "environment_domain_policy_runtime_bound": True,
            "table_counts_and_dtype_bound": True}


def main():
    path = Path(__file__).with_name("checks.json")
    if path.exists():
        raise FileExistsError(path)
    before = runner.source_hashes()
    results = []
    for check in (rng_compatibility, reward_windows, coverage_masks_and_worlds, model_and_environment_identity):
        try:
            results.append({"name": check.__name__, "status": "PASS", "details": check()})
        except Exception as error:
            results.append({"name": check.__name__, "status": "FAIL", "error_type": type(error).__name__, "error": str(error)})
    after = runner.source_hashes()
    passed = before == after and all(row["status"] == "PASS" for row in results)
    payload = {"status": "PASS" if passed else "FAIL", "scope": "deterministic component and synthetic archival fixtures",
               "market_initializations": 0, "market_runs": 0, "source_hashes_before": before, "source_hashes_after": after,
               "source_unchanged": before == after, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "python_version": platform.python_version(), "numpy_version": np.__version__, "checks": results,
               "limitations": ["No market training, frozen-table validation or empirical acceptance was run."]}
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": payload["status"], "checks": [{"name": row["name"], "status": row["status"]} for row in results]}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
