"""Check group-wise coverage using synthetic archives; no market initialization or runs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import runner, training
from abm.disclosure.config import MarketConfig
from abm.tabular import CompanyQLearner

FOLDER = Path(__file__).resolve().parent
GRID = tuple(json.loads((FOLDER / "math_spec.json").read_text(encoding="utf-8"))["action_fractions"])
SOURCES = ["src/abm/disclosure/config.py", "src/abm/disclosure/learning.py", "src/abm/tabular.py",
           "src/abm/disclosure/game.py", "src/abm/disclosure/runner.py", "src/abm/disclosure/training.py"]


def hashes():
    return {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in SOURCES}


def main():
    path = FOLDER / "group_checks.json"
    if path.exists():
        raise FileExistsError(path)
    before = hashes()
    n = 202
    config = MarketConfig(n_investors=6, n_firms=n, trading_days=60, burn_in_days=0,
                          firm_policy="q_learning", firm_action_fractions=GRID)
    daily, periods = np.zeros((61, n)), np.zeros((2, n))
    groups, states = periods.astype(np.int64), periods.astype(np.int64)
    groups[1, -1] = 1
    valid = np.zeros((2, n, 17), dtype=bool)
    valid[:, :, 2] = True
    valid[1, -1, 2], valid[1, -1, 16] = False, True
    result = SimpleNamespace(
        learning_groups=groups, learning_states=states, valid_actions=valid,
        unvisited_state=np.zeros((2, n), dtype=bool), financing_value_adjustment=daily,
        applied_resource_cost=daily, applied_fine=daily, applied_subsidy=daily,
        learning_transition=periods.astype(bool), action_due_day=np.full((2, n), -1),
        actions=np.full((2, n), 2), amounts=periods, cost_fraction=periods,
        penalty_fraction=periods, subsidy_fraction=periods,
        market=SimpleNamespace(prices=np.ones((61, n))), inflation=daily)
    learner = CompanyQLearner(groups=6, actions=17)
    learner.counts.fill(20)
    learner.counts[1, 0, 16] = 0
    rare_action = runner.learning_report(result, config, learner, training=False)["coverage"]
    assert rare_action["global_status"] == "PASS" and rare_action["status"] == "FAIL"
    assert rare_action["groups"][1]["status"] == "FAIL"
    assert rare_action["common_state_undercovered_actions"] == []
    assert rare_action["group_common_state_undercovered_actions"] == [
        {"group": 1, "state": 0, "choice_index": 16, "action": 1, "count": 0}]
    records = [{"phase": "validation", "firm_policy": "q_learning", "status": "complete", "seed": 27301,
                "learning": {"coverage": rare_action}}]
    groups[1, -1], valid[1, -1, 16], valid[1, -1, 2] = 0, False, True
    ordinary = runner.learning_report(result, config, learner, training=False)["coverage"]
    assert ordinary["status"] == "PASS" and ordinary["groups"][1]["status"] == "not_observed"
    records.append({"phase": "validation", "firm_policy": "q_learning", "status": "complete", "seed": 27302,
                    "learning": {"coverage": ordinary}})
    pooled = training._coverage(records, learner.counts, 2)
    assert pooled["global_status"] == "PASS" and pooled["status"] == "FAIL"
    assert [world["status"] for world in pooled["worlds"]] == ["FAIL", "PASS"]
    assert pooled["groups"][1]["status"] == "FAIL" and pooled["groups"][2]["status"] == "not_observed"
    learner.counts[1, 1] = 0
    groups[1, -1], states[1, -1], result.unvisited_state[1, -1] = 1, 1, True
    rare_unseen = runner.learning_report(result, config, learner, training=False)["coverage"]
    assert rare_unseen["global_status"] == "PASS" and rare_unseen["status"] == "FAIL"
    assert rare_unseen["groups"][1]["unseen_state_fraction"] == 1
    assert rare_unseen["unseen_state_fraction"] < .05
    after = hashes()
    assert before == after
    payload = {"status": "PASS", "market_initializations": 0, "market_runs": 0,
               "scope": "synthetic runner and pooled-training coverage fixtures", "source_unchanged": True,
               "source_hashes_before": before, "source_hashes_after": after,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "rare_group_share": 1 / n,
               "checks": {"rare_group_legal_amplitude_failure_survives_global_pass": True,
                          "raw_choice_16_reports_semantic_wash_1": True,
                          "pooled_pass_cannot_hide_one_world_group_failure": True,
                          "unobserved_groups_are_not_observed": True,
                          "rare_group_all_unseen_survives_small_global_unseen_fraction": True},
               "runner_action_case": rare_action, "pooled_case": pooled, "runner_unseen_case": rare_unseen}
    with path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": payload["status"], "rare_group_share": 1 / n,
                      "runner_global_status": rare_action["global_status"], "runner_status": rare_action["status"],
                      "pooled_global_status": pooled["global_status"], "pooled_status": pooled["status"]}))


if __name__ == "__main__":
    main()
