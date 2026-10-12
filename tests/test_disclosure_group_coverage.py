from types import SimpleNamespace

import numpy as np
import pytest

from abm.disclosure import runner, training
from abm.disclosure.config import MarketConfig
from abm.tabular import CompanyQLearner


FRACTIONS = (.01, .02, .04, .08, .16, .32, .64, 1.)
CHOICES = 17


def visits_at(values):
    visits = np.zeros((6, 81), dtype=np.int64)
    for key, value in values.items():
        visits[key] = value
    return visits


def validation_record(seed, visits, counts, legal=None):
    if legal is None:
        legal = np.repeat(visits[:, :, None], CHOICES, axis=2)
    missing = int(visits[counts.sum(axis=2) == 0].sum())
    return {
        "seed": seed, "phase": "validation", "firm_policy": "q_learning", "status": "complete",
        "learning": {"coverage": {
            "visits": visits.tolist(), "legal_action_visits": legal.tolist(),
            "decisions": int(visits.sum()), "unseen_state_decisions": missing, "status": "PASS",
        }},
    }


def single_report(visits, counts, *, training_mode=False, has_learner=True):
    coordinates = np.argwhere(visits > 0)
    repetitions = visits[visits > 0]
    groups = np.repeat(coordinates[:, 0], repetitions)
    states = np.repeat(coordinates[:, 1], repetitions)
    firms = len(groups)
    zeros = np.zeros((2, firms))
    unseen = counts.sum(axis=2) == 0
    result = SimpleNamespace(
        learning_groups=np.vstack((np.full(firms, -1), groups)),
        learning_states=np.vstack((np.full(firms, -1), states)),
        valid_actions=np.ones((2, firms, CHOICES), dtype=bool),
        unvisited_state=np.vstack((np.zeros(firms, dtype=bool), unseen[groups, states])) if has_learner else None,
        financing_value_adjustment=zeros, applied_resource_cost=zeros, applied_fine=zeros,
        applied_subsidy=zeros, action_due_day=zeros, actions=np.full((2, firms), 2), amounts=zeros,
        cost_fraction=zeros, penalty_fraction=zeros, subsidy_fraction=zeros, inflation=zeros,
        learning_transition=np.zeros((2, firms), dtype=bool), learning_update=None,
        market=SimpleNamespace(prices=np.ones((2, firms))),
    )
    config = MarketConfig(n_investors=30, n_firms=firms, trading_days=1, burn_in_days=0,
                          firm_decision_interval=1, firm_policy="q_learning", firm_action_fractions=FRACTIONS)
    learner = CompanyQLearner(groups=6, actions=CHOICES) if has_learner else None
    if learner is not None:
        learner.counts[:] = counts
    return runner.learning_report(result, config, learner, training=training_mode)["coverage"]


@pytest.fixture(autouse=True)
def forbid_market_runs(monkeypatch):
    monkeypatch.setattr(runner.DisclosureMarket, "run", lambda self: pytest.fail("coverage tests must not simulate"))


@pytest.mark.parametrize("choice", [0, 16])
@pytest.mark.parametrize("group", [0, 3])
def test_group_common_state_cannot_hide_below_global_one_percent(choice, group):
    visits = visits_at({(group, 0): 99, (group, 1): 1, (1, 0): 900})
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    counts[group, 1, choice] = 19
    local = single_report(visits, counts)
    pooled = training._coverage([validation_record(41, visits, counts)], counts, 1)
    for report in (local, pooled):
        assert report["global_status"] == "PASS"
        assert report["common_state_undercovered_actions"] == []
        assert report["status"] == "FAIL"
        assert report["groups"][group]["status"] == "FAIL"
        assert report["groups"][group]["policy_epoch"] == group // 3
        assert report["groups"][group]["size_class"] == group % 3
        assert all(item["group"] == group and item["state"] == 1
                   and item["choice_index"] == choice and item["count"] == 19
                   for item in report["group_common_state_undercovered_actions"])
    assert {item["seed"] for item in pooled["group_common_state_undercovered_actions"]} == {41, None}
    assert pooled["worlds"][0]["global_status"] == "PASS"
    assert pooled["worlds"][0]["groups"][group]["status"] == "FAIL"


@pytest.mark.parametrize("missing,expected", [(50, "PASS"), (60, "FAIL")])
def test_group_unseen_limit_uses_group_denominator_and_includes_five_percent(missing, expected):
    values = {(0, 0): 1000 - missing, (1, 0): 9000}
    values.update({(0, state): missing // 10 for state in range(1, 11)})
    visits = visits_at(values)
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    counts[0, 1:11] = 0
    local = single_report(visits, counts)
    pooled = training._coverage([validation_record(42, visits, counts)], counts, 1)
    for report in (local, pooled):
        assert report["global_status"] == "PASS"
        assert report["unseen_state_fraction"] == missing / 10000
        assert report["group_common_state_undercovered_actions"] == []
        assert report["groups"][0]["unseen_state_fraction"] == missing / 1000
        assert report["groups"][0]["status"] == expected
        assert report["status"] == expected


@pytest.mark.parametrize("rare,expected", [(99, "PASS"), (100, "FAIL")])
def test_group_common_state_threshold_includes_one_percent(rare, expected):
    visits = visits_at({(0, 0): 10000 - rare, (0, 1): rare, (1, 0): 90000})
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    counts[0, 1, 16] = 19
    report = training._coverage([validation_record(43, visits, counts)], counts, 1)
    assert report["global_status"] == "PASS"
    assert report["groups"][0]["status"] == expected
    assert report["status"] == expected


def test_pooled_success_does_not_erase_a_world_group_failure():
    first = visits_at({(0, 0): 99, (0, 1): 1, (1, 0): 900})
    second = visits_at({(0, 0): 100, (1, 0): 900})
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    counts[0, 1, 16] = 19
    report = training._coverage([validation_record(44, first, counts), validation_record(45, second, counts)], counts, 2)
    assert report["global_status"] == "PASS"
    assert report["groups"][0]["status"] == "PASS"
    assert [world["status"] for world in report["worlds"]] == ["FAIL", "PASS"]
    assert report["status"] == "FAIL"
    assert [item["seed"] for item in report["group_common_state_undercovered_actions"]] == [44]


def test_pooled_group_checks_union_of_legal_choices():
    first = visits_at({(0, 0): 98, (0, 1): 2, (1, 0): 900})
    second = visits_at({(0, 0): 199, (0, 1): 1, (1, 0): 1800})
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    counts[0, 1, 16] = 19
    first_legal = np.repeat(first[:, :, None], CHOICES, axis=2)
    first_legal[0, 1, 16] = 0
    report = training._coverage([validation_record(46, first, counts, first_legal),
                                 validation_record(47, second, counts)], counts, 2)
    assert report["global_status"] == "PASS"
    assert all(world["status"] == "PASS" for world in report["worlds"])
    assert report["groups"][0]["status"] == report["status"] == "FAIL"
    assert [item["seed"] for item in report["group_common_state_undercovered_actions"]] == [None]


def test_unobserved_groups_do_not_fail_an_observed_group_at_twenty_records():
    visits = visits_at({(4, 0): 100})
    counts = np.full((6, 81, CHOICES), 20, dtype=np.int64)
    for report in (single_report(visits, counts),
                   training._coverage([validation_record(48, visits, counts)], counts, 1)):
        assert report["status"] == "PASS"
        assert report["groups"][4]["status"] == "PASS"
        assert all(group["status"] == "not_observed" and group["unseen_state_fraction"] is None
                   for group in report["groups"] if group["group"] != 4)


@pytest.mark.parametrize("has_learner,training_mode", [(False, False), (True, True)])
def test_training_and_nonlearner_coverage_remain_not_applicable(has_learner, training_mode):
    visits = visits_at({(0, 0): 100})
    counts = np.zeros((6, 81, CHOICES), dtype=np.int64)
    report = single_report(visits, counts, training_mode=training_mode, has_learner=has_learner)
    assert report["status"] == report["global_status"] == "not_applicable"
    assert report["groups"][0]["status"] == "not_applicable"
    assert report["groups"][1]["status"] == "not_observed"
