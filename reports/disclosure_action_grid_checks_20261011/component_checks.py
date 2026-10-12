"""Read-only component probes, including a static decision-hook fixture; no market runs."""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.game import DisclosureMarket
from abm.disclosure.learning import action_kinds, batch_update, choose_actions, discrete_candidates, load_frozen, npv_discrete, save_frozen
from abm.disclosure.policy import PolicyRegime, PolicySchedule
from abm.tabular import CompanyQLearner

FOLDER = Path(__file__).resolve().parent
GRID = tuple(json.loads((FOLDER / "math_spec.json").read_text(encoding="utf-8"))["action_fractions"])
SOURCES = ["src/abm/disclosure/config.py", "src/abm/disclosure/learning.py", "src/abm/disclosure/game.py", "src/abm/tabular.py"]


def hashes():
    return {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in SOURCES}


def config_and_layout():
    external = list(GRID)
    config = MarketConfig(firm_action_fractions=external)
    external.append(1.5)
    assert config.firm_action_fractions == GRID and isinstance(config.firm_action_fractions, tuple)
    assert "firm_action_fractions" not in MarketConfig().to_dict()
    assert MarketConfig.from_dict(config.to_dict()) == config
    expected = np.array([0, 1, 2] + [0, 1] * 7)
    np.testing.assert_array_equal(action_kinds(17), expected)
    return {"choice_count": 17, "semantic_count": 3, "choice_kinds": expected.tolist(),
            "external_list_detached": True, "legacy_default_serialization_omits_grid": True}


def candidates_and_dedup():
    capacities = np.array([0., .001, .0025, .003, .02, .03, .25])
    offered = discrete_candidates(improve_capacity=capacities, inflate_capacity=capacities / 2,
                                  marginal_cost=.05, max_change_per_period=.25, wash_cost_ratio=.2,
                                  subsidy=0., real_value_per_sd=0., displaced_real_value_per_sd=0.,
                                  wash_value_per_sd=0., fine_value_per_sd=0., amplitude_fractions=GRID)
    assert offered.amounts.shape == (capacities.size, 17)
    for row, capacity in enumerate(capacities):
        for kind, bound in ((0, capacity), (1, capacity / 2)):
            columns = np.flatnonzero(offered.kinds == kind)
            expected = np.minimum(np.asarray(GRID) * .25, bound)
            np.testing.assert_array_equal(offered.amounts[row, columns], expected)
            keep = (expected > 0) & np.r_[True, expected[1:] != expected[:-1]]
            np.testing.assert_array_equal(offered.valid_actions[row, columns], keep)
            legal = offered.amounts[row, columns[keep]]
            assert np.unique(legal).size == legal.size
    assert np.all(offered.valid_actions[:, 2])
    assert np.all(offered.values[:, offered.kinds != 2] <= 0)
    return {"capacity_contexts": capacities.tolist(), "both_kinds_keep_lowest_duplicate_index": True,
            "negative_npv_positive_capacity_actions_remain_legal": True}


class QuantileRng:
    def random(self, size):
        return (np.arange(size) + .5) / size


def exploration_and_compatibility():
    size = 18000
    groups, states = np.zeros(size, dtype=np.int64), np.zeros(size, dtype=np.int64)
    kinds = action_kinds(17)
    valid = np.zeros((size, 17), dtype=bool)
    valid[:, [0, 1, 2, 3, 4, 5]] = True
    learner = CompanyQLearner(groups=6, actions=17)
    learner.values[0, 0, [0, 3, 4]] = 1
    errors = []
    for maintain in (True, False):
        valid[:, 2] = maintain
        for epsilon in (0., .4, 1.):
            learner.epsilon = epsilon
            best = valid[0] & (learner.values[0, 0] == learner.values[0, 0, valid[0]].max())
            probabilities = np.zeros(17)
            for weight, mask in ((epsilon, valid[0]), (1 - epsilon, best)):
                present = [kind for kind in range(3) if mask[kinds == kind].any()]
                for kind in present:
                    members = np.flatnonzero(mask & (kinds == kind))
                    probabilities[members] += weight / len(present) / members.size
            selected = choose_actions(learner, groups, states, valid, QuantileRng(), training=True)
            assert valid[np.arange(size), selected].all()
            observed = np.bincount(selected, minlength=17) / size
            error = float(np.max(np.abs(observed - probabilities)))
            assert error <= 1 / size + 1e-14
            errors.append(error)
    legacy = CompanyQLearner(groups=6, epsilon=.27)
    legacy.values[0, 0] = [1., 2., 0.]
    oldmask = np.ones((1001, 3), dtype=bool)
    oldmask[::3, 0], oldmask[1::3, 1] = False, False
    oldvalues = np.where(oldmask, legacy.values[0, 0], -np.inf)
    best = oldmask & (oldvalues == oldvalues.max(axis=1, keepdims=True))
    probabilities = legacy.epsilon * oldmask / oldmask.sum(axis=1, keepdims=True) + (1 - legacy.epsilon) * best / best.sum(axis=1, keepdims=True)
    expected = np.minimum((np.random.default_rng(913).random(1001)[:, None] >= probabilities.cumsum(axis=1)).sum(axis=1), 2)
    actual = choose_actions(legacy, groups[:1001], states[:1001], oldmask, np.random.default_rng(913), training=True)
    np.testing.assert_array_equal(actual, expected)
    return {"hierarchical_exploration_and_tie_contexts": 6, "quantiles_per_context": size,
            "maximum_probability_error": max(errors), "legacy_draws_exact": actual.size}


def frozen_table_and_dynamic_update():
    learner = CompanyQLearner(groups=6, actions=17, learning_rate=1.)
    learner.values[3, 1, 16], learner.values[3, 1, 9] = 99., 4.
    mask = np.zeros((1, 17), dtype=bool)
    mask[0, 9] = True
    batch_update(learner, np.array([0]), np.array([0]), np.array([0]), np.array([16]), np.array([1.]),
                 np.array([3]), np.array([1]), mask, elapsed_days=60, annual_discount_rate=.05,
                 terminated=np.array([False]))
    np.testing.assert_allclose(learner.values[0, 0, 16], 1 + np.exp(-.05 * 60 / 252) * 4)
    assert learner.counts[0, 0, 16] == 1
    metadata = {"grid": list(GRID), "role": "deterministic_component_fixture"}
    original = {"grid": list(GRID), "role": metadata["role"]}
    path = FOLDER / "component_frozen17.npz"
    digest = save_frozen(path, learner, metadata)
    metadata["grid"].append(1.5)
    restored, loaded = load_frozen(path, original, expected_sha256=digest)
    assert loaded == original and restored.values.shape == (6, 81, 17)
    assert not restored.values.flags.writeable and not restored.counts.flags.writeable and restored.epsilon == 0
    before = (restored.values.copy(), restored.counts.copy())
    legal = np.zeros((1, 17), dtype=bool)
    legal[0, [3, 4, 15]] = True
    assert choose_actions(restored, np.array([0]), np.array([2]), legal, None, training=False)[0] == 3
    np.testing.assert_array_equal(restored.values, before[0])
    np.testing.assert_array_equal(restored.counts, before[1])
    return {"masked_illegal_high_q_excluded": True, "choice_16_updated": True,
            "frozen_file_sha256": digest, "unvisited_without_maintain_selects_first_legal": True,
            "saved_metadata_detached_from_caller": True}


def decision_hook_value_anchor():
    domain = load_domain(ROOT / "configs/domains/esg.json")
    n = 3
    rows, paired_masks = [], []
    for mode, subsidy, pending, fine in (("npv_discrete", .01, 0., .00002),
                                         ("q_learning", .01, 0., .00002),
                                         ("npv_discrete", .01, -.00003, 0.),
                                         ("npv_discrete", 0., 0., .00002)):
        cfg = MarketConfig(n_investors=6, n_firms=n, trading_days=60, burn_in_days=0,
                           firm_policy=mode, firm_action_fractions=GRID)
        regime = replace(PolicyRegime.baseline(domain), subsidy=subsidy)
        learner = None
        if mode == "q_learning":
            learner = CompanyQLearner(groups=6, actions=17, epsilon=0)
            learner.values.flags.writeable = learner.counts.flags.writeable = False
        fixture = SimpleNamespace(
            config=cfg, domain=domain, policy=PolicySchedule.constant(domain), learner=learner, training=False,
            attributes=SimpleNamespace(inflation=np.zeros(n), pending=[], marginal_cost=lambda _: np.full(n, .05)),
            firms=SimpleNamespace(intrinsic_value=np.full(n, .00001), size_class=np.zeros(n, dtype=np.int64)),
            prices=np.ones(n), pending_value_change=np.full(n, pending), financing_exposure=np.zeros(n),
            pending_resource_cost=np.zeros(n), pending_fine=np.zeros(n), pending_subsidy=np.zeros(n),
            marginal_financing_saving=lambda: np.zeros(n), learning_state_history=np.zeros((2, n), dtype=np.int64),
            learning_group_history=np.zeros((2, n), dtype=np.int64), valid_action_history=np.zeros((2, n, 17), dtype=bool),
            choice_history=np.zeros((2, n), dtype=np.int64), unvisited_state_history=np.zeros((2, n), dtype=bool))
        try:
            choices = DisclosureMarket._discrete_decision(fixture, 60, 1, regime, np.zeros(n, dtype=bool),
                                                          np.full(n, fine), np.full(n, .25), np.full(n, .25))
        except ValueError as error:
            assert subsidy == 0 and "no feasible firm action" in str(error)
            rows.append({"mode": mode, "subsidy": subsidy, "all_invalid_rejected": True})
            continue
        assert subsidy > 0 and not fixture.valid_action_history[1, :, 2].any()
        if fine:
            paired_masks.append(fixture.valid_action_history[1].copy())
        raw = fixture.choice_history[1]
        np.testing.assert_array_equal(choices.actions, action_kinds(17)[raw])
        assert np.all(choices.actions == 0) and fixture.valid_action_history[1, np.arange(n), raw].all()
        anchor = .00001 + pending + choices.subsidy_fraction - choices.cost_fraction - fine
        assert np.all(anchor > 0)
        rows.append({"mode": mode, "subsidy": subsidy, "pending_value": pending,
                     "fine": fine, "choice_indices": raw.tolist(), "semantic_actions": choices.actions.tolist(),
                     "post_commitment_value_anchors": anchor.tolist(), "maintain_invalid": True})
    np.testing.assert_array_equal(paired_masks[0], paired_masks[1])
    return {"static_contexts": rows, "same_mask_for_ql_and_npv": True}


def main():
    output = FOLDER / "component_checks.json"
    if output.exists():
        raise FileExistsError(output)
    before = hashes()
    checks = []
    for probe in (config_and_layout, candidates_and_dedup, exploration_and_compatibility,
                  frozen_table_and_dynamic_update, decision_hook_value_anchor):
        try:
            checks.append({"name": probe.__name__, "status": "PASS", "details": probe()})
        except Exception as error:
            checks.append({"name": probe.__name__, "status": "FAIL", "error_type": type(error).__name__, "error": str(error)})
    after = hashes()
    payload = {"status": "PASS" if before == after and all(row["status"] == "PASS" for row in checks) else "FAIL",
               "scope": "component functions and static decision-hook contexts", "market_initializations": 0,
               "market_runs": 0, "source_hashes_before": before, "source_hashes_after": after,
               "source_unchanged": before == after, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "checks": checks, "pending_review": ["runner/training group coverage after owner freeze", "market-level acceptance"]}
    with output.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": payload["status"], "checks": [{"name": row["name"], "status": row["status"]} for row in checks]}))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
