"""Independently replay the archived multi-amplitude development budget."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from statistics import NormalDist

import numpy as np


YEAR = 252
ATOL, RTOL = 5e-13, 5e-12
GATES = ("mechanical", "stylized", "return_acf", "cross_asset_correlation", "empirical_calibration")
FIELDS = (
    "true_goodness", "inflation", "impact_share", "impact_wealth_share", "pricing_slope",
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "financing_rate", "financing_cost", "financing_value_adjustment", "public_signal",
    "planning_signal", "disclosure_error", "audit_selected", "audit_publications", "verified_goodness",
    "action_due_day", "applied_resource_cost", "applied_fine", "applied_subsidy", "learning_states",
    "learning_groups", "valid_actions", "learning_rewards", "learning_transition", "unvisited_state", "learning_choices",
)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_arrays(path):
    with np.load(path, allow_pickle=False) as arrays:
        return {name: arrays[name].copy() for name in arrays.files}


def read_table(path):
    arrays = read_arrays(path)
    return arrays["values"], arrays["counts"], json.loads(str(arrays["metadata"].item()))


def table_identity(values, counts):
    h = hashlib.sha256()
    for value in (values, counts):
        array = np.ascontiguousarray(value)
        h.update(str((array.dtype.str, array.shape)).encode("ascii"))
        h.update(array.tobytes())
    return h.hexdigest()


class Checks:
    def __init__(self):
        self.rows = []

    def check(self, name, condition, detail=None):
        row = {"name": name, "status": "PASS" if bool(condition) else "FAIL"}
        if detail is not None:
            row["detail"] = detail
        self.rows.append(row)

    def array(self, name, actual, expected, *, exact=False, atol=ATOL, rtol=RTOL):
        actual, expected = np.asarray(actual), np.asarray(expected)
        same_shape = actual.shape == expected.shape
        good = same_shape and (np.array_equal(actual, expected, equal_nan=True) if exact else
                               np.allclose(actual, expected, atol=atol, rtol=rtol, equal_nan=True))
        finite = np.isfinite(actual) & np.isfinite(expected) if same_shape else np.array([], dtype=bool)
        error = float(np.max(np.abs(actual[finite].astype(float) - expected[finite].astype(float)), initial=0)) if same_shape else None
        self.check(name, good, {"actual_shape": list(actual.shape), "expected_shape": list(expected.shape),
                                "maximum_absolute_error": error, "comparison": "exact" if exact else "tolerant"})

    @property
    def passed(self):
        return all(row["status"] == "PASS" for row in self.rows)


def result_identity(arrays):
    h = hashlib.sha256(str(int(arrays["market_burn_in_days"])).encode("ascii"))
    for name in ("prices", "intrinsic_values", "size_class", "equity_share", "mean_depth_fraction",
                 "gross_volume", "price_cap_hits", "total_cash"):
        array = np.ascontiguousarray(arrays["market_" + name])
        h.update(str(array.dtype).encode("ascii"))
        h.update(str(array.shape).encode("ascii"))
        h.update(array.tobytes())
    result = hashlib.sha256(h.hexdigest().encode("ascii"))
    for name in FIELDS:
        if name in arrays:
            array = np.ascontiguousarray(arrays[name])
            result.update(str(array.dtype).encode("ascii"))
            result.update(array.tobytes())
    return result.hexdigest()


def regime_at(schedule, day):
    return schedule["intervention"] if schedule["intervention"] is not None and day >= schedule["start_day"] else schedule["baseline"]


def catalog(fractions):
    kinds = np.array([0, 1, 2] + [kind for _ in fractions[1:] for kind in (0, 1)], dtype=np.int64)
    amplitudes = np.array([fractions[0], fractions[0], 0.0] + [value for value in fractions[1:] for _ in (0, 1)])
    priority = np.array([2] + np.flatnonzero(kinds == 0).tolist() + np.flatnonzero(kinds == 1).tolist())
    return kinds, amplitudes, priority


def coverage_counts(visits, legal, counts, group_unseen, kinds, *, training=False):
    total, group_totals = int(visits.sum()), visits.sum(axis=1)
    missing = None if group_unseen is None else int(np.sum(group_unseen))
    fraction = missing / total if missing is not None and total else None
    undercovered, group_undercovered = [], []
    if counts is not None:
        for group in range(6):
            for state in range(81):
                if not visits[group, state]:
                    continue
                for choice in range(len(kinds)):
                    if not legal[group, state, choice] or counts[group, state, choice] >= 20:
                        continue
                    row = {"group": group, "state": state, "choice_index": choice,
                           "action": int(kinds[choice]), "count": int(counts[group, state, choice])}
                    if visits[group, state] >= .01 * total:
                        undercovered.append(row.copy())
                    if visits[group, state] >= .01 * group_totals[group]:
                        group_undercovered.append(row.copy())
    reports = []
    for group, group_total in enumerate(group_totals):
        group_missing = None if group_unseen is None else int(group_unseen[group])
        share = group_missing / int(group_total) if group_missing is not None and group_total else None
        status = "not_observed" if not group_total else (
            "not_applicable" if training or counts is None else (
                "PASS" if share is not None and share <= .05
                and not any(row["group"] == group for row in group_undercovered) else "FAIL"))
        reports.append({"group": group, "size_class": group % 3, "policy_epoch": group // 3,
                        "decisions": int(group_total), "unseen_state_decisions": group_missing,
                        "unseen_state_fraction": share, "status": status})
    global_status = "not_applicable" if training or counts is None else (
        "PASS" if fraction is not None and fraction <= .05 and not undercovered else "FAIL")
    return {"visits": visits.tolist(), "legal_action_visits": legal.tolist(), "decisions": total,
            "unseen_state_decisions": missing, "unseen_state_fraction": fraction,
            "common_state_minimum_action_count": 20, "common_state_share_threshold": .01,
            "common_state_undercovered_actions": undercovered,
            "group_common_state_undercovered_actions": group_undercovered,
            "group_common_state_share_threshold": .01, "maximum_unseen_state_fraction": .05,
            "groups": reports, "global_status": global_status,
            "status": "FAIL" if any(row["status"] == "FAIL" for row in reports) else global_status}


def coverage(groups, states, mask, counts, kinds, unseen=None, *, training=False):
    visits = np.zeros((6, 81), dtype=np.int64)
    legal = np.zeros((6, 81, len(kinds)), dtype=np.int64)
    group_unseen = None if unseen is None else np.zeros(6, dtype=np.int64)
    missing_flags = np.zeros(groups[1:].size, dtype=bool) if unseen is None else unseen[1:].reshape(-1)
    for group, state, allowed, missing in zip(groups[1:].reshape(-1), states[1:].reshape(-1),
                                             mask[1:].reshape(-1, len(kinds)), missing_flags):
        visits[group, state] += 1
        legal[group, state] += allowed.astype(np.int64)
        if group_unseen is not None:
            group_unseen[group] += int(missing)
    return coverage_counts(visits, legal, counts, group_unseen, kinds, training=training)


def replay_attributes(arrays, manifest, checks):
    cfg, domain, schedule = manifest["config"], manifest["domain"], manifest["policy"]
    n, last, step = cfg["n_firms"], cfg["trading_days"], cfg["firm_decision_interval"]
    periods = last // step + 1
    actions, amounts, prices = arrays["actions"], arrays["amounts"], arrays["market_prices"]
    fractions = cfg.get("firm_action_fractions", [.01])
    kinds, amplitudes, priority = catalog(fractions)
    choices = arrays.get("learning_choices", actions)
    bounds = sorted(domain["direction"] * (value - domain["initial_mean"]) / domain["initial_sd"]
                    for value in (domain["raw_lower"], domain["raw_upper"]))
    attribute_seed, audit_seed, _, _, firm_seed = np.random.SeedSequence([cfg["seed"], 1]).spawn(5)
    rng, audit_rng = np.random.default_rng(attribute_seed), np.random.default_rng(audit_seed)
    empirical = domain.get("initial_empirical_distribution")
    if empirical:
        support, frequencies = np.asarray(empirical, dtype=float).T
        raw = rng.choice(support, size=n, p=frequencies / frequencies.sum())
        goodness = domain["direction"] * (raw - domain["initial_mean"]) / domain["initial_sd"]
    else:
        normal = NormalDist()
        samples = rng.uniform(normal.cdf(bounds[0]), normal.cdf(bounds[1]), n)
        goodness = np.array([normal.inv_cdf(value) for value in samples])
    cost_scale = (domain["real_cost_scale"] * np.asarray(domain["size_cost_multipliers"])[arrays["market_size_class"]]
                  * rng.lognormal(-.5 * domain["real_cost_log_sd"]**2, domain["real_cost_log_sd"], n))
    inflation, pending = np.zeros(n), []
    true_history, infl_history = np.empty((last + 1, n)), np.empty((last + 1, n))
    true_history[0], infl_history[0] = goodness, inflation
    cost, fine, subsidy, expected_amounts = (np.zeros((periods, n)) for _ in range(4))
    expected_due = np.full((periods, n), -1, dtype=np.int64)
    groups, states = np.full((periods, n), -1, dtype=np.int64), np.full((periods, n), -1, dtype=np.int64)
    masks = np.zeros((periods, n, len(kinds)), dtype=bool)
    selected_history = np.zeros((periods, n), dtype=np.int64)
    caught_history, publication_history = selected_history.copy(), selected_history.copy()
    verified_history = np.zeros((periods, n))
    capacity_ok = True
    exposure = cfg["financing_exposure_fraction"] * prices[0]
    discrete = cfg["firm_policy"] != "npv"
    if discrete:
        checks.check("multi_amplitude_choices_archived", len(kinds) == 3 or "learning_choices" in arrays)
        checks.check("internal_choice_indices", choices.shape == actions.shape and np.issubdtype(choices.dtype, np.integer)
                     and np.all((choices >= 0) & (choices < len(kinds))))
        checks.array("internal_choices_map_to_semantic_actions", actions, kinds[choices], exact=True)
    delta = amplitudes * domain["max_change_per_period"]
    duplicate_slots = anchor_exclusions = maintain_exclusions = 0
    realized_real, realized_decay = np.zeros(n), np.zeros(n)
    window_real, window_decay = np.zeros(n), np.zeros(n)
    for day in range(1, last + 1):
        before_decay = goodness.copy()
        goodness = np.maximum(goodness - domain["natural_decay"] / YEAR, bounds[0])
        realized_decay += before_decay - goodness
        if day > cfg["burn_in_days"]:
            window_decay += before_decay - goodness
        remaining = []
        for due, kind, firms, values in pending:
            if due > day:
                remaining.append((due, kind, firms, values))
            elif kind == 0:
                before_improvement = goodness[firms].copy()
                goodness[firms] = np.minimum(goodness[firms] + values, bounds[1])
                np.add.at(realized_real, firms, goodness[firms] - before_improvement)
                if day > cfg["burn_in_days"]:
                    np.add.at(window_real, firms, goodness[firms] - before_improvement)
            else:
                inflation[firms] += values
        pending = remaining
        inflation = np.maximum(np.minimum(inflation, bounds[1] - goodness), 0)
        if day % step == 0:
            period, regime = day // step, regime_at(schedule, day)
            selected = audit_rng.random(n) < regime["audit_probability"]
            caught = selected & (inflation > 0)
            selected_history[period], caught_history[period] = selected, caught
            fine[period] = np.where(caught, regime["penalty"] * inflation, 0)
            inflation[caught] = 0
            published = selected & regime.get("publish_audit_results", False)
            publication_history[period] = published
            verified_history[period, published] = goodness[published]
            real_room, report_room = bounds[1] - goodness, bounds[1] - goodness - inflation
            earliest = np.full(n, np.inf)
            for due, kind, firms, values in pending:
                if kind == 0:
                    np.subtract.at(real_room, firms, values)
                np.subtract.at(report_room, firms, values)
                np.minimum.at(earliest, firms, due - day)
            real_room, report_room = np.maximum(real_room, 0), np.maximum(report_room, 0)
            choice = actions[period]
            offered = np.zeros((n, len(kinds)))
            for column, kind in enumerate(kinds):
                if kind != 2:
                    offered[:, column] = np.minimum(delta[column], real_room if kind == 0 else report_room)
            legal = offered > 0
            legal[:, 2] = True
            for kind in (0, 1):
                columns = np.flatnonzero(kinds == kind)
                for previous, current in zip(columns, columns[1:]):
                    duplicates = legal[:, current] & (offered[:, current] == offered[:, previous])
                    duplicate_slots += int(duplicates.sum())
                    legal[:, current] &= ~duplicates
            c = cost_scale * np.exp(domain["cost_level_elasticity"] * goodness)
            candidate_costs = np.zeros_like(offered)
            candidate_subsidies = np.zeros_like(offered)
            for column, kind in enumerate(kinds):
                if kind != 2:
                    scale = c if kind == 0 else domain["wash_cost_ratio"] * c
                    candidate_costs[:, column] = scale * offered[:, column]**2
                if kind == 0:
                    candidate_subsidies[:, column] = regime["subsidy"] * offered[:, column]
            if discrete:
                # Pre-trade settlement clears prior monetary commitments; V_t is replayed below.
                known_change = (candidate_subsidies - candidate_costs - fine[period, :, None]) * prices[day, :, None]
                ratio = 1.0 + known_change / arrays["market_intrinsic_values"][day, :, None]
                positive_anchor = np.isfinite(ratio) & (ratio > 0)
                anchor_exclusions += int((legal & ~positive_anchor).sum())
                maintain_exclusions += int((~positive_anchor[:, 2]).sum())
                legal &= positive_anchor
                masks[period] = legal
                expected_amounts[period] = offered[np.arange(n), choices[period]]
            else:
                expected_amounts[period] = amounts[period]
            capacity_ok &= bool(np.all(amounts[period] >= 0) and np.all(amounts[period] <= domain["max_change_per_period"] + ATOL)
                                and np.all(amounts[period, choice == 0] <= real_room[choice == 0] + ATOL)
                                and np.all(amounts[period, choice == 1] <= report_room[choice == 1] + ATOL)
                                and np.all(amounts[period, choice == 2] == 0))
            cost[period] = np.select([choice == 0, choice == 1],
                                     [c * amounts[period]**2, domain["wash_cost_ratio"] * c * amounts[period]**2], 0)
            subsidy[period] = np.where(choice == 0, regime["subsidy"] * amounts[period], 0)
            stage = np.where(np.isfinite(earliest), 2, 0)
            stage[(earliest <= step) | (fine[period] * prices[day] != 0)] = 1
            features = (exposure / (exposure + prices[day]), inflation, np.log(c / domain["real_cost_scale"]), stage)
            thresholds = ((.25, .5), (1e-12, domain["max_change_per_period"]), (-.5, .5), (.5, 1.5))
            states[period] = sum(np.searchsorted(threshold, feature, side="right") * weight
                                 for feature, threshold, weight in zip(features, thresholds, (27, 9, 3, 1)))
            groups[period] = arrays["market_size_class"] + 3 * int(schedule["intervention"] is not None and day >= schedule["start_day"])
            wash_delay = regime.get("disclosure_delay_days")
            wash_delay = domain["disclosure_delay_days"] if wash_delay is None else wash_delay
            for kind, delay in ((0, domain["implementation_delay_days"]), (1, wash_delay)):
                firms = np.flatnonzero(choice == kind)
                if firms.size:
                    due = day + max(1, delay)
                    expected_due[period, firms] = due
                    pending.append((due, kind, firms, amounts[period, firms]))
        true_history[day], infl_history[day] = goodness, inflation
    checks.array("true_attribute_and_delays", arrays["true_goodness"], true_history)
    checks.array("inflation_audit_and_delays", arrays["inflation"], infl_history)
    checks.array("audit_rng_and_selection", arrays["audit_selected"], selected_history, exact=True)
    checks.array("detections", arrays["detections"], caught_history, exact=True)
    checks.array("publications", arrays["audit_publications"], publication_history, exact=True)
    checks.array("verified_true_attribute", arrays["verified_goodness"], verified_history)
    checks.array("candidate_resource_cost", arrays["cost_fraction"], cost, atol=1e-15)
    checks.array("candidate_subsidy", arrays["subsidy_fraction"], subsidy, atol=1e-15)
    checks.array("audit_penalty_fraction", arrays["penalty_fraction"], fine, atol=1e-15)
    checks.array("action_due_dates", arrays["action_due_day"], expected_due, exact=True)
    checks.check("action_capacities", capacity_ok)
    checks.check("action_indices", np.all((actions >= 0) & (actions <= 2)))
    if discrete:
        checks.array("shared_fixed_candidate_amounts", amounts, expected_amounts)
        checks.array("legal_candidates", arrays["valid_actions"], masks, exact=True)
        checks.array("audit_after_pending_state", arrays["learning_states"], states, exact=True)
        checks.array("actual_policy_epoch", arrays["learning_groups"], groups, exact=True)
        checks.check("at_least_one_legal_candidate", np.all(masks[1:].any(axis=2)))
        checks.check("selected_action_is_legal", np.all(np.take_along_axis(masks[1:], choices[1:, :, None], axis=2)))
    return {"states": states, "groups": groups, "masks": masks, "firm_seed": firm_seed,
            "choices": choices, "kinds": kinds, "priority": priority,
            "duplicate_clipped_slots_removed": duplicate_slots, "value_anchor_slots_removed": anchor_exclusions,
            "maintain_illegal_decisions": maintain_exclusions,
            "pending": pending, "cost_fraction": cost, "fine_fraction": fine, "subsidy_fraction": subsidy,
            "gross_realized_gain_full_by_firm": realized_real.tolist(), "actual_decay_loss_full_by_firm": realized_decay.tolist(),
            "gross_realized_gain_window_by_firm": window_real.tolist(), "actual_decay_loss_window_by_firm": window_decay.tolist()}


def replay_financing_and_ledger(arrays, manifest, reconstructed, checks):
    cfg, n = manifest["config"], manifest["config"]["n_firms"]
    last, step, prices = cfg["trading_days"], cfg["firm_decision_interval"], arrays["market_prices"]
    exposure = cfg["financing_exposure_fraction"] * prices[0]
    initial_rate = cfg["risk_free_rate"] + cfg["financing_spread"] * exposure / (exposure + prices[0])
    rates = np.empty_like(prices)
    rates[0] = initial_rate
    for day in range(1, last + 1):
        rates[day] = (cfg["risk_free_rate"] + cfg["financing_spread"] * exposure / (exposure + prices[day - 1])
                      if day % cfg["financing_repricing_interval"] == 0 else rates[day - 1])
    fees, saving = exposure * rates / YEAR, exposure * (initial_rate - rates) / YEAR
    fees[0], saving[0] = 0, 0
    checks.array("locked_contract_uses_lagged_quote", arrays["financing_rate"], rates)
    checks.array("actual_fee_accrual", arrays["financing_cost"], fees)
    checks.array("actual_fee_baseline_adjustment", arrays["financing_value_adjustment"], saving)
    ledger, tail = {}, {}
    for key, fraction_name, recorded_name in (("resource_cost", "cost_fraction", "applied_resource_cost"),
                                              ("fine", "penalty_fraction", "applied_fine"),
                                              ("subsidy", "subsidy_fraction", "applied_subsidy")):
        applied = np.zeros_like(prices)
        unapplied = np.zeros(n)
        for period in range(1, arrays["actions"].shape[0]):
            day = period * step
            money = arrays[fraction_name][period] * prices[day]
            if day + 1 <= last:
                applied[day + 1] += money
            else:
                unapplied += money
        ledger[key], tail[key] = applied, unapplied.tolist()
        if recorded_name in arrays:
            checks.array(recorded_name + "_once_next_day_fixed_money", arrays[recorded_name], applied, exact=True)
        else:
            checks.check(recorded_name + "_legacy_npv_absent", cfg["firm_policy"] == "npv")
    _, _, fundamental_seed, _ = np.random.SeedSequence(cfg["seed"]).spawn(4)
    rng, value = np.random.default_rng(fundamental_seed), arrays["market_intrinsic_values"][0].copy()
    predicted_values = np.empty_like(prices)
    predicted_values[0] = value
    sigma, rho = cfg["fundamental_volatility"] / np.sqrt(YEAR), cfg["fundamental_common_correlation"]
    drift = (cfg["fundamental_drift"] - .5 * cfg["fundamental_volatility"]**2) / YEAR
    for day in range(1, last + 1):
        shock = np.sqrt(rho) * rng.standard_normal() + np.sqrt(1 - rho) * rng.standard_normal(n)
        value = value * np.exp(drift + sigma * shock)
        value += ledger["subsidy"][day] - ledger["resource_cost"][day] - ledger["fine"][day]
        value += saving[day]
        predicted_values[day] = value
    checks.array("value_anchor_applies_money_once_after_fundamentals", arrays["market_intrinsic_values"],
                 predicted_values, atol=2e-11)
    net = saving - ledger["resource_cost"] - ledger["fine"] + ledger["subsidy"]
    rewards = np.full(arrays["actions"].shape, np.nan)
    transitions = np.zeros(arrays["actions"].shape, dtype=bool)
    discounts = np.exp(-cfg["firm_discount_rate"] * np.arange(1, step + 1) / YEAR)
    for period in range(2, rewards.shape[0]):
        day = period * step
        rewards[period] = discounts @ net[day - step + 1:day + 1] / prices[0]
        transitions[period] = True
    if cfg["firm_policy"] != "npv":
        checks.array("reward_from_actual_ledger_only", arrays["learning_rewards"], rewards)
        checks.array("complete_windows_no_initial_or_fake_tail", arrays["learning_transition"], transitions, exact=True)
    ledger["financing_adjustment"] = saving
    return {"ledger": ledger, "net": net, "rewards": rewards, "transitions": transitions,
            "unapplied": tail, "discounted_net": np.exp(-cfg["firm_discount_rate"] * np.arange(last + 1) / YEAR) @ net / prices[0]}


def kind_probabilities(eligible, kinds):
    probabilities = np.zeros(eligible.shape, dtype=float)
    for firm, row in enumerate(eligible):
        available = [np.flatnonzero(row & (kinds == kind)) for kind in (0, 1, 2)]
        available = [columns for columns in available if len(columns)]
        for columns in available:
            probabilities[firm, columns] = 1.0 / len(available) / len(columns)
    return probabilities


def replay_table(arrays, manifest, input_table, output_table, reconstructed, rewards, checks):
    values, counts, payload = input_table
    q, visits = values.copy(), counts.copy()
    n, cfg, learning = manifest["config"]["n_firms"], manifest["config"], manifest["learning"]
    states, groups, mask = reconstructed["states"], reconstructed["groups"], reconstructed["masks"]
    kinds, priority, choices = reconstructed["kinds"], reconstructed["priority"], reconstructed["choices"]
    training, epsilon, alpha = learning["training"], learning["epsilon"], learning["learning_rate"]
    rng = np.random.default_rng(reconstructed["firm_seed"])
    gamma = np.exp(-cfg["firm_discount_rate"] * cfg["firm_decision_interval"] / YEAR)
    unseen = np.zeros(arrays["actions"].shape, dtype=bool)
    selected = np.full(arrays["actions"].shape, 2, dtype=np.int64)
    for period in range(1, selected.shape[0]):
        if training and period > 1:
            old = q.copy()
            future = np.max(np.where(mask[period], old[groups[period], states[period]], -np.inf), axis=1)
            targets = rewards[period] + gamma * future
            by_key = {}
            for firm in range(n):
                key = (int(groups[period - 1, firm]), int(states[period - 1, firm]), int(choices[period - 1, firm]))
                by_key.setdefault(key, []).append(float(targets[firm]))
            for key in sorted(by_key):
                mean = math.fsum(sorted(by_key[key])) / len(by_key[key])
                q[key] = old[key] + alpha * (mean - old[key])
                visits[key] += len(by_key[key])
        unseen[period] = visits[groups[period], states[period]].sum(axis=1) == 0
        allowed = mask[period]
        option = np.where(allowed, q[groups[period], states[period]], -np.inf)
        if training:
            best = allowed & (option == option.max(axis=1, keepdims=True))
            if len(kinds) == 3:
                probability = epsilon * allowed / allowed.sum(axis=1, keepdims=True) + (1 - epsilon) * best / best.sum(axis=1, keepdims=True)
            else:
                probability = epsilon * kind_probabilities(allowed, kinds) + (1 - epsilon) * kind_probabilities(best, kinds)
            last_legal = np.max(np.where(allowed, np.arange(len(kinds)), -1), axis=1)
            selected[period] = np.minimum((rng.random(n)[:, None] >= probability.cumsum(axis=1)).sum(axis=1), last_legal)
        else:
            selected[period] = priority[np.argmax(option[:, priority], axis=1)]
            fallback = priority[np.argmax(allowed[:, priority], axis=1)]
            selected[period, unseen[period]] = fallback[unseen[period]]
    checks.array("ql_internal_choices_from_hierarchical_sampling_and_separate_rng", choices, selected, exact=True)
    checks.array("ql_semantic_actions_from_internal_choices", arrays["actions"], kinds[selected], exact=True)
    checks.array("unvisited_state_from_preselection_counts", arrays["unvisited_state"], unseen, exact=True)
    checks.array("independent_synchronous_td_final_Q", output_table[0], q)
    checks.array("independent_td_final_counts", output_table[1], visits, exact=True)
    checks.check("table_hyperparameters_match_manifest", payload["learning_rate"] == alpha and payload["discount"] == learning["discount"])
    if not training:
        checks.array("frozen_values_unchanged", output_table[0], values, exact=True)
        checks.array("frozen_counts_unchanged", output_table[1], counts, exact=True)
        checks.check("frozen_epsilon_zero", epsilon == 0)
    return coverage(groups, states, mask, output_table[1], kinds, unseen, training=training)


def compare_learning_report(report, coverage_report, money, arrays, manifest, checks):
    cfg, last, step = manifest["config"], manifest["config"]["trading_days"], manifest["config"]["firm_decision_interval"]
    for key in coverage_report:
        checks.check("reported_coverage_" + key, report["coverage"][key] == coverage_report[key])
    for key, value in money["ledger"].items():
        checks.array("reported_ledger_total_" + key, report["ledger"]["totals_by_firm"][key], value.sum(axis=0))
    checks.array("reported_discounted_private_ledger", report["ledger"]["discounted_net_by_initial_cap"], money["discounted_net"])
    checks.check("reported_transition_count", report["ledger"]["completed_transitions"] == int(money["transitions"].sum()))
    pending = [{"decision_day": int(period * step), "firm": int(firm), "action": int(arrays["actions"][period, firm]),
                "due_day": int(arrays["action_due_day"][period, firm]), "amount": float(arrays["amounts"][period, firm])}
               for period, firm in np.argwhere(arrays["action_due_day"] > last)]
    tail = report["tail"]
    checks.check("reported_pending_projects", tail["pending_projects"] == pending)
    checks.check("reported_tail_decision_and_window", tail["last_decision_day"] == (last // step * step or None)
                 and tail["unclosed_decisions"] == (cfg["n_firms"] if last >= step else 0)
                 and tail["observed_days_of_unclosed_window"] == (last % step if last >= step else 0))
    for key, value in money["unapplied"].items():
        checks.array("reported_unapplied_" + key, tail["unapplied_next_day_commitments"][key], value, exact=True)
    checks.array("reported_outstanding_inflation", tail["outstanding_inflation"], arrays["inflation"][-1], exact=True)


def verify_run(folder, record, experiment):
    checks = Checks()
    manifest = read_json(folder / "manifest.json")
    inputs = {str(folder / "manifest.json"): digest(folder / "manifest.json")}
    identity = {key: manifest[key] for key in ("schema_version", "config", "domain", "policy", "source_hashes", "python_version", "numpy_version")}
    if "learning" in manifest:
        identity["learning"] = manifest["learning"]
    checks.check("canonical_run_identity", hashlib.sha256(canonical(identity)).hexdigest() == manifest["run_id"])
    checks.check("record_manifest_status", record["status"] == manifest["status"])
    checks.check("record_seed_and_rule", manifest["config"]["seed"] == record["seed"] and manifest["config"]["firm_policy"] == record["firm_policy"])
    environment = dict(manifest["config"])
    environment.pop("seed")
    environment.pop("firm_policy")
    checks.check("frozen_environment_and_source", environment == experiment["contract"]["config"]
                 and manifest["domain"] == experiment["contract"]["domain"] and manifest["policy"] == experiment["contract"]["policy"]
                 and manifest["source_hashes"] == experiment["contract"]["source_hashes"]
                 and manifest["python_version"] == experiment["contract"]["python_version"]
                 and manifest["numpy_version"] == experiment["contract"]["numpy_version"])
    with zipfile.ZipFile(folder / "source.zip") as archive:
        checks.check("source_zip_exact_manifest_members", len(archive.namelist()) == len(set(archive.namelist()))
                     and set(archive.namelist()) == set(manifest["source_hashes"]))
        for name, expected in manifest["source_hashes"].items():
            checks.check("source_member:" + name, hashlib.sha256(archive.read(name)).hexdigest() == expected)
    for name, expected in manifest.get("artifacts", {}).items():
        path = folder / name
        checks.check("artifact:" + name, path.is_file() and digest(path) == expected)
        if path.is_file():
            inputs[str(path)] = digest(path)
    if manifest["status"] != "complete":
        checkpoint = manifest.get("failed_learning_checkpoint", {})
        if checkpoint.get("path"):
            path = folder / checkpoint["path"]
            checks.check("failed_checkpoint_retained", digest(path) == checkpoint["sha256"])
            inputs[str(path)] = digest(path)
        return {"path": record["path"], "archive_status": manifest["status"], "verification_status": "INCOMPLETE",
                "checks": checks.rows, "error": manifest.get("error")}, inputs, None
    checks.check("record_artifact_hashes", record["artifacts"] == manifest["artifacts"])
    required = {"source.zip", "result.npz", "metrics.json", "validation.json"}
    if manifest["config"]["firm_policy"] != "npv":
        required.add("learning.json")
    if manifest["config"]["firm_policy"] == "q_learning":
        required.update(("input_model.npz", "output_model.npz"))
    checks.check("required_artifact_hashes_present", required <= set(manifest["artifacts"]))
    arrays = read_arrays(folder / "result.npz")
    checks.check("result_content_fingerprint", result_identity(arrays) == manifest["result_fingerprint"] == record["result_fingerprint"])
    cfg = manifest["config"]
    periods, n = cfg["trading_days"] // cfg["firm_decision_interval"] + 1, cfg["n_firms"]
    checks.check("result_dimensions", arrays["market_prices"].shape == (cfg["trading_days"] + 1, n)
                 and arrays["actions"].shape == (periods, n))
    checks.check("recorded_numpy_version", manifest["numpy_version"] == np.__version__)
    reconstructed = replay_attributes(arrays, manifest, checks)
    money = replay_financing_and_ledger(arrays, manifest, reconstructed, checks)
    table_before = table_after = None
    if cfg["firm_policy"] == "q_learning":
        table_before, table_after = read_table(folder / "input_model.npz"), read_table(folder / "output_model.npz")
        for tag, table in (("input", table_before), ("output", table_after)):
            checks.check(tag + "_metadata", table[2]["metadata"] == manifest["learning"]["metadata"]
                         and table[2]["format_version"] == (1 if len(reconstructed["kinds"]) == 3 else 2))
            checks.check(tag + "_dynamic_table_shape_and_dtype", table[0].shape == table[1].shape == (6, 81, len(reconstructed["kinds"]))
                         and table[0].dtype == np.float64 and table[1].dtype == np.int64
                         and np.isfinite(table[0]).all() and np.all(table[1] >= 0))
        checks.check("learning_metadata_frozen_contract", manifest["learning"]["metadata"]["contract"] == experiment["contract"])
        checks.check("initial_table_content_identity", table_identity(*table_before[:2]) == manifest["learning"]["initial_table_fingerprint"])
        coverage_report = replay_table(arrays, manifest, table_before, table_after, reconstructed, money["rewards"], checks)
        expected_updates = int(money["transitions"].sum()) if manifest["learning"]["training"] else 0
        checks.check("count_increment_equals_completed_transitions", int(table_after[1].sum() - table_before[1].sum()) == expected_updates)
    elif cfg["firm_policy"] == "npv_discrete":
        coverage_report = coverage(reconstructed["groups"], reconstructed["states"], reconstructed["masks"], None, reconstructed["kinds"])
    else:
        coverage_report = None
    if coverage_report is not None:
        report = read_json(folder / "learning.json")
        compare_learning_report(report, coverage_report, money, arrays, manifest, checks)
        if table_before is not None:
            checks.check("reported_table_identities", report["initial_table_fingerprint"] == table_identity(*table_before[:2])
                         and report["final_table_fingerprint"] == table_identity(*table_after[:2])
                         and report["final_transition_count"] == int(table_after[1].sum()))
    metrics = read_json(folder / "metrics.json")
    days = np.arange(periods) * cfg["firm_decision_interval"]
    selected = days > cfg["burn_in_days"]
    commitments = {key: float((arrays[name][selected] * arrays["market_prices"][days[selected]]).sum())
                   for key, name in (("resource_cost", "cost_fraction"), ("fine_transfer", "penalty_fraction"), ("subsidy_transfer", "subsidy_fraction"))}
    for key, value in commitments.items():
        checks.array("metrics_commitment_cost_" + key, metrics["costs"][key], value)
    checks.array("metrics_true_change", metrics["true_change"]["equal_weight_sd"],
                 (arrays["true_goodness"][-1] - arrays["true_goodness"][cfg["burn_in_days"]]).mean())
    validation = read_json(folder / "validation.json")
    prices, values = arrays["market_prices"], arrays["market_intrinsic_values"]
    expected_cash = arrays["market_total_cash"][0] + np.r_[0, np.cumsum(cfg["cash_flow_yield"] * values[1:].sum(axis=1) / YEAR)]
    cash_error = float(np.max(np.abs(arrays["market_total_cash"] - expected_cash) / np.abs(expected_cash)))
    share_error = float(np.abs(arrays["market_maximum_share_error"]).max())
    tolerance = validation["mechanical"]["conservation_tolerance"]
    mechanical_checks = {"finite_positive_prices": bool(np.all(np.isfinite(prices) & (prices > 0))),
                         "finite_positive_intrinsic_values": bool(np.all(np.isfinite(values) & (values > 0))),
                         "no_price_caps": bool(np.all(arrays["market_price_cap_hits"] == 0)),
                         "cash_conservation": bool(cash_error <= tolerance), "share_conservation": bool(share_error <= tolerance)}
    checks.check("mechanical_gate_recomputed", mechanical_checks == validation["mechanical"]["checks"])
    checks.check("mechanical_status_retains_failure", validation["mechanical"]["status"] == ("PASS" if all(mechanical_checks.values()) else "FAIL"))
    checks.array("mechanical_cap_hits", validation["mechanical"]["price_cap_hits"], arrays["market_price_cap_hits"].sum(), exact=True)
    for name in ("metrics", "validation", "learning"):
        if name in record:
            checks.check("summary_embedded_" + name, record[name] == read_json(folder / (name + ".json")))
    result = {"path": record["path"], "phase": record["phase"], "seed": record["seed"], "rule": record["firm_policy"],
              "archive_status": "complete", "verification_status": "PASS" if checks.passed else "FAIL", "checks": checks.rows,
              "gates": {key: validation[key]["status"] for key in GATES},
              "coverage": coverage_report, "actions_real_wash_maintain": np.bincount(arrays["actions"][1:].ravel(), minlength=3).tolist(),
              "internal_choice_counts": None if coverage_report is None else np.bincount(reconstructed["choices"][1:].ravel(), minlength=len(reconstructed["kinds"])).tolist(),
              "duplicate_clipped_slots_removed": reconstructed["duplicate_clipped_slots_removed"],
              "value_anchor_slots_removed": reconstructed["value_anchor_slots_removed"],
              "maintain_illegal_decisions": reconstructed["maintain_illegal_decisions"],
              "completed_transition_count": int(money["transitions"].sum()) if coverage_report is not None else 0,
              "ledger_source": "decision fractions and prices independently replayed" if cfg["firm_policy"] == "npv" else "daily recorded and independently replayed",
              "totals_applied": {key: float(value.sum()) for key, value in money["ledger"].items()},
              "commitments_in_metric_window": commitments, "unapplied_final_day_by_firm": money["unapplied"],
              "true_change_equal_weight_sd": float(metrics["true_change"]["equal_weight_sd"]),
              "gross_realized_gain_window_mean_sd": float(np.mean(reconstructed["gross_realized_gain_window_by_firm"])),
              "actual_decay_loss_window_mean_sd": float(np.mean(reconstructed["actual_decay_loss_window_by_firm"])),
              "pending_project_count": sum(len(item[2]) for item in reconstructed["pending"])}
    checks.array("net_transition_is_gross_gain_minus_actual_decay", result["true_change_equal_weight_sd"],
                 result["gross_realized_gain_window_mean_sd"] - result["actual_decay_loss_window_mean_sd"])
    result["verification_status"] = "PASS" if checks.passed else "FAIL"
    initial = {field: arrays[field][0].copy() for field in ("market_prices", "market_intrinsic_values", "true_goodness", "inflation")}
    return result, inputs, {"manifest": manifest, "initial": initial, "audit_selected": arrays["audit_selected"].copy(),
                            "coverage": coverage_report, "before": table_before, "after": table_after}


def pooled_coverage(rows, counts, kinds):
    visits = np.zeros((6, 81), dtype=np.int64)
    legal = np.zeros((6, 81, len(kinds)), dtype=np.int64)
    group_unseen = np.zeros(6, dtype=np.int64)
    worlds, undercovered, group_undercovered = [], [], []
    for seed, report in rows:
        seen, allowed = np.asarray(report["visits"]), np.asarray(report["legal_action_visits"])
        missing = np.array([seen[group, counts[group].sum(axis=1) == 0].sum() for group in range(6)])
        world = coverage_counts(seen, allowed, counts, missing, kinds)
        worlds.append({"seed": seed, **{key: world[key] for key in (
            "decisions", "unseen_state_decisions", "unseen_state_fraction", "global_status", "groups", "status")}})
        for target, key in ((undercovered, "common_state_undercovered_actions"),
                            (group_undercovered, "group_common_state_undercovered_actions")):
            target.extend({"seed": seed, **item} for item in world[key])
        visits += seen
        legal += allowed
        group_unseen += missing
    pooled = coverage_counts(visits, legal, counts, group_unseen, kinds)
    for target, key in ((undercovered, "common_state_undercovered_actions"),
                        (group_undercovered, "group_common_state_undercovered_actions")):
        target.extend({"seed": None, **item} for item in pooled[key])
    global_status = "PASS" if pooled["global_status"] == "PASS" and not undercovered and all(
        world["global_status"] == "PASS" for world in worlds) else "FAIL"
    return {**pooled, "global_status": global_status,
            "status": "PASS" if global_status == "PASS" and not group_undercovered
            and all(group["status"] != "FAIL" for group in pooled["groups"])
            and all(world["status"] == "PASS" for world in worlds) else "FAIL",
            "scope": "Global and each observed size/policy-epoch group must pass in every validation world and pooled.",
            "common_state_undercovered_actions": undercovered,
            "group_common_state_undercovered_actions": group_undercovered, "worlds": worlds}


def verify_archive(archive, spec_path):
    archive, spec_path = archive.resolve(), spec_path.resolve()
    checks, inputs, cache, runs = Checks(), {}, {}, []
    experiment, summary = read_json(archive / "experiment.json"), read_json(archive / "summary.json")
    declared, requested = read_json(archive / "declared_spec.json"), read_json(spec_path)
    top_manifest = read_json(archive / "summary_manifest.json")
    for name in ("experiment.json", "summary.json", "declared_spec.json", "summary_manifest.json", "initial_model.npz", "frozen_model.npz"):
        path = archive / name
        if path.is_file():
            inputs[str(path)] = digest(path)
    inputs[str(spec_path)] = digest(spec_path)
    checks.check("declared_spec_matches_fixed_input", declared == requested)
    checks.check("top_level_manifest_identity", top_manifest["experiment_id"] == summary["experiment_id"]
                 and top_manifest["status"] == summary["status"]
                 and top_manifest["source_hashes"] == experiment["contract"]["source_hashes"])
    for name, expected_hash in top_manifest["artifacts"].items():
        path = archive / name
        checks.check("top_artifact:" + name, path.is_file() and digest(path) == expected_hash)
        if path.is_file():
            inputs[str(path)] = digest(path)
    identity = {key: value for key, value in experiment.items() if key != "experiment_id"}
    checks.check("experiment_identity", hashlib.sha256(canonical(identity)).hexdigest() == experiment["experiment_id"] == summary["experiment_id"])
    checks.check("single_baseline_development_scope", experiment["purpose"] == summary["purpose"] == declared["purpose"] == "development"
                 and experiment["policy"]["intervention"] is None
                 and experiment["comparison_scope"] == summary["comparison_scope"] == "within_scenario_algorithm_comparison")
    budget, contract = experiment["budget"], experiment["contract"]
    fractions = experiment["config"].get("firm_action_fractions", [.01])
    kinds, _, _ = catalog(fractions)
    shape = (6, 81, len(kinds))
    checks.check("fixed_budget_matches_declaration", all(budget[key] == declared[key] for key in (
        "training_seeds", "validation_seeds", "reserved_seeds"))
        and budget["training_worlds"] == len(budget["training_seeds"])
        and budget["validation_worlds_per_rule"] == len(budget["validation_seeds"])
        and budget["validation_rules"] == ["q_learning", "npv_discrete", "npv"])
    checks.check("fixed_market_matches_declaration", all(experiment["config"].get(key) == value for key, value in declared["market"].items()))
    checks.check("dynamic_action_contract", contract["version"] == 2 and contract["candidate_fractions"] == fractions
                 and contract["choice_kinds"] == kinds.tolist()
                 and contract["exploration"] == "uniform_legal_kind_then_uniform_legal_amplitude"
                 and contract["feasibility"] == "positive_value_anchor_after_known_commitments_v1"
                 and budget["initial_table"]["shape"] == list(shape))
    checks.array("epsilon_fixed_linear_schedule", budget["epsilon_by_world"], np.linspace(1.0, .1, len(budget["training_seeds"])), exact=True)
    checks.check("seed_partitions", len(set(budget["training_seeds"])) == len(budget["training_seeds"])
                 and len(set(budget["validation_seeds"])) == len(budget["validation_seeds"])
                 and not set(budget["training_seeds"]) & set(budget["validation_seeds"])
                 and not set(budget["training_seeds"] + budget["validation_seeds"]) & set(budget["reserved_seeds"]))
    checks.check("summary_budget_and_contract", summary["budget"] == budget and summary["contract"] == contract)
    expected = [("training", seed, "q_learning") for seed in budget["training_seeds"]] + [
        ("validation", seed, mode) for seed in budget["validation_seeds"] for mode in budget["validation_rules"]]
    actual = [(record["phase"], record["seed"], record["firm_policy"]) for record in summary["records"]]
    checks.check("all_planned_runs_retained_once_in_order", actual == expected)
    complete = actual == expected and all(record["status"] == "complete" for record in summary["records"])
    checks.check("summary_completion_truthful", (summary["status"] == "complete") == complete)
    checks.check("research_claims_remain_pending", summary["claim_support"] == summary["m4_status"] == "pending")
    for index, record in enumerate(summary["records"]):
        folder = (archive / record["path"]).resolve()
        inside = folder.is_relative_to(archive)
        checks.check("run_path_within_archive:" + record["path"], inside)
        try:
            if not inside:
                raise ValueError("run path escapes archive")
            result, files, detail = verify_run(folder, record, experiment)
            runs.append(result)
            inputs.update(files)
            if detail is not None:
                cache[(record["phase"], record["seed"], record["firm_policy"])] = detail
        except Exception as error:
            runs.append({"path": record["path"], "phase": record["phase"], "seed": record["seed"], "rule": record["firm_policy"],
                         "archive_status": record["status"], "verification_status": "FAIL", "error_type": type(error).__name__, "error": str(error)})
        print(json.dumps({"verified_run": index + 1, "planned_runs": len(expected), "path": record["path"],
                          "status": runs[-1]["verification_status"]}), flush=True)
    initial = read_table(archive / "initial_model.npz")
    checks.check("initial_model_sha256", digest(archive / "initial_model.npz") == summary["initial_model_sha256"])
    checks.array("initial_zero_Q", initial[0], np.zeros(shape), exact=True)
    checks.array("initial_zero_counts", initial[1], np.zeros(shape, dtype=np.int64), exact=True)
    checks.check("initial_metadata_contract_and_budget", initial[2]["metadata"]["contract"] == contract
                 and initial[2]["metadata"]["budget"] == budget and initial[2]["metadata"]["completed_training_seeds"] == [])
    previous = initial
    for index, seed in enumerate(budget["training_seeds"]):
        row = cache.get(("training", seed, "q_learning"))
        if row is None:
            checks.check("training_lineage:" + str(seed), False, "Training archive incomplete; no substitute seed.")
            continue
        checks.array("lineage_input_Q:" + str(seed), row["before"][0], previous[0], exact=True)
        checks.array("lineage_input_counts:" + str(seed), row["before"][1], previous[1], exact=True)
        metadata, learning = row["manifest"]["learning"]["metadata"], row["manifest"]["learning"]
        checks.check("training_lineage_metadata:" + str(seed), metadata["completed_training_seeds"] == budget["training_seeds"][:index]
                     and metadata["experiment_id"] == experiment["experiment_id"] and metadata["budget"] == budget
                     and metadata["phase"] == "training" and learning["training"] is True
                     and learning["learning_rate"] == budget["learning_rate"]
                     and metadata["epsilon"] == learning["epsilon"] == budget["epsilon_by_world"][index])
        previous = row["after"]
    frozen_path = archive / "frozen_model.npz"
    coverage_gate = {"status": "incomplete", "reason": "Not every planned frozen evaluation completed."}
    frozen = read_table(frozen_path) if frozen_path.is_file() else None
    checks.check("frozen_model_present", frozen is not None)
    if frozen is not None:
        checks.check("frozen_model_sha256", digest(frozen_path) == summary["frozen_model_sha256"])
        checks.array("last_training_to_frozen_Q", frozen[0], previous[0], exact=True)
        checks.array("last_training_to_frozen_counts", frozen[1], previous[1], exact=True)
        checks.check("frozen_semantic_identity", table_identity(*frozen[:2]) == summary["frozen_table_fingerprint"])
        checks.check("frozen_metadata_lineage", frozen[2]["metadata"]["completed_training_seeds"] == budget["training_seeds"] == summary["completed_training_seeds"]
                     and frozen[2]["metadata"]["phase"] == "frozen" and frozen[2]["metadata"]["contract"] == contract
                     and frozen[2]["metadata"]["budget"] == budget)
        validation_rows = []
        for seed in budget["validation_seeds"]:
            row = cache.get(("validation", seed, "q_learning"))
            checks.check("frozen_evaluation_present:" + str(seed), row is not None)
            if row is None:
                continue
            for tag in ("before", "after"):
                checks.array("frozen_eval_" + tag + "_Q:" + str(seed), row[tag][0], frozen[0], exact=True)
                checks.array("frozen_eval_" + tag + "_counts:" + str(seed), row[tag][1], frozen[1], exact=True)
                checks.check("frozen_eval_" + tag + "_metadata:" + str(seed), row[tag][2]["metadata"] == frozen[2]["metadata"])
            cov = row["coverage"]
            seen = np.asarray(cov["visits"])
            unseen_from_frozen = int(seen[frozen[1].sum(axis=2) == 0].sum())
            checks.check("frozen_counts_define_unseen:" + str(seed), unseen_from_frozen == cov["unseen_state_decisions"])
            validation_rows.append((seed, cov))
            for mode in ("npv_discrete", "npv"):
                reference = cache.get(("validation", seed, mode))
                checks.check("paired_comparator_present:" + str(seed) + ":" + mode, reference is not None)
                if reference is not None:
                    for field in row["initial"]:
                        checks.array("paired_initial_" + mode + "_" + field + ":" + str(seed), reference["initial"][field], row["initial"][field], exact=True)
                    checks.array("paired_audit_random_selection:" + str(seed) + ":" + mode, reference["audit_selected"], row["audit_selected"], exact=True)
        if len(validation_rows) == len(budget["validation_seeds"]):
            coverage_gate = pooled_coverage(validation_rows, frozen[1], kinds)
        expected_transition_count = len(budget["training_seeds"]) * experiment["config"]["n_firms"] * max(
            0, experiment["config"]["trading_days"] // experiment["config"]["firm_decision_interval"] - 1)
        checks.check("fixed_budget_transition_count", int(frozen[1].sum()) == expected_transition_count)
    reported = summary["validation"]["coverage"]
    for key, value in coverage_gate.items():
        checks.check("pooled_coverage_" + key, reported.get(key) == value)
    gate_summary = {}
    for name in GATES:
        statuses = [{"phase": row["phase"], "seed": row["seed"], "firm_policy": row["rule"],
                     "status": row.get("gates", {}).get(name, "incomplete")} for row in runs]
        values = [row["status"] for row in statuses]
        status = "FAIL" if "FAIL" in values else (
            "incomplete" if len(values) != len(expected) or "incomplete" in values else
            "PASS" if values and all(value == "PASS" for value in values) else "pending")
        gate_summary[name] = {"status": status, "runs": statuses}
        checks.check("summary_preserves_" + name, summary["validation"][name] == gate_summary[name])
    for path, before in inputs.items():
        path = Path(path)
        label = str(path.relative_to(archive)) if path.is_relative_to(archive) else str(path)
        checks.check("input_unchanged:" + label, digest(path) == before)
    good = checks.passed and all(row["verification_status"] == "PASS" for row in runs)
    cfg, domain = experiment["config"], experiment["domain"]
    return {"status": "PASS" if good and complete else "FAIL" if not good else "INCOMPLETE",
            "scope": "Independent replay of every declared single-baseline development world; no market simulations.",
            "generated_utc": datetime.now(timezone.utc).isoformat(), "archive": str(archive),
            "verification_code_sha256": digest(Path(__file__)), "input_hashes": inputs,
            "verifier_python": platform.python_version(), "verifier_numpy": np.__version__,
            "numeric_tolerances": {"absolute": ATOL, "relative": RTOL, "value_anchor_absolute": 2e-11,
                                   "exact": ["file/content hashes", "lineage arrays", "counts", "internal/semantic actions", "state/group/masks", "next-day monetary ledgers"]},
            "declared_worlds": len(expected), "training_worlds": len(budget["training_seeds"]),
            "validation_seeds": budget["validation_seeds"], "action_fractions": fractions, "choice_kinds": kinds.tolist(),
            "independently_replayed_training_transitions": sum(row.get("completed_transition_count", 0) for row in runs if row.get("phase") == "training"),
            "checks": checks.rows, "runs": runs, "market_gates": gate_summary, "coverage_gate": coverage_gate,
            "discrete_capacity_vs_decay": {
                "minimum_candidate_sd": min(fractions) * domain["max_change_per_period"],
                "maximum_candidate_sd": max(fractions) * domain["max_change_per_period"],
                "decision_days": cfg["firm_decision_interval"],
                "maximum_real_improvement_sd_per_year": max(fractions) * domain["max_change_per_period"] * YEAR / cfg["firm_decision_interval"],
                "assumed_decay_sd_per_year": domain["natural_decay"],
                "scope": "Interior steady-state feasibility bound before implementation delays, costs, optimal choices or lower-bound clipping; no prediction of realized improvement."},
            "limitations": ["No market simulations or ABM implementation functions were called by this verifier.",
                            "Every archived Q-learning choice, seeded attribute/fundamental draw, daily ledger, completed-window reward and synchronous TD update is independently replayed; model lineage and frozen evaluations are checked exactly.",
                            "Local investor-demand derivatives and NPV optimal selection cannot be independently reconstructed without investor holdings; only candidate feasibility, size, cost, delays and realized accounting are verified for NPV.",
                            "Public/planning disclosure signals are content-fingerprinted here, not independently replayed; separate information-mechanism verification covers their timing.",
                            "Share conservation uses the archived maximum-share-error diagnostic because holdings are absent; stylized/serial/correlation gates are preserved, not independently re-estimated.",
                            "Fines identify a dated audit of aggregate inflation, not an identifiable single previous washing action.",
                            "Development coverage is checked in every observed size/policy-epoch group and globally, per world and pooled. Unobserved groups remain not_observed; development and coverage PASS do not establish full M4 acceptance or empirical validity.",
                            "Market failures and pending empirical/serial-correlation checks remain separate from archive-integrity status; no seed replacement, adaptive training budget, policy ranking, lifetime-profit or social-welfare claim is made."]}


def write_interpretation(report, path):
    failed = [row["name"] for row in report["checks"] if row["status"] != "PASS"]
    completed = sum(row["archive_status"] == "complete" for row in report["runs"])
    verified = sum(row["verification_status"] == "PASS" for row in report["runs"])
    gate, capacity = report["coverage_gate"], report["discrete_capacity_vs_decay"]
    lines = ["# 多幅度动作集归档独立核验", "",
             f"归档核验：**{report['status']}**。已归档{completed}/{report['declared_worlds']}个世界，独立复算通过{verified}个；这是开发实验，不代表 M4 或经验校准已验收。", "",
             f"归档：`{report['archive']}`。核验代码 SHA256：`{report['verification_code_sha256']}`。所有输入哈希与逐项结果见同目录 `verification.json`。", "",
             f"固定预算为{report['training_worlds']}个顺序训练世界，随后{len(report['validation_seeds'])}个新种子分别评估冻结QL、同网格离散NPV和连续NPV。没有替换种子、增补训练或重新模拟。网格为{report['action_fractions']}，内部选项共{len(report['choice_kinds'])}个；外部仍为真实改善、虚报、维持三种语义。", "",
             f"核验独立重建初始属性、自然衰减、项目到期、审计随机流、容量及clip去重、价值锚合法性、状态与组别；手写类型/幅度两层抽样和同步TD，复算{report['independently_replayed_training_transitions']}条训练转移。逐世界检查Q与计数谱系，验证世界输入和输出均与最终冻结表逐位一致。未调用被测市场、更新、候选或汇总函数。", "",
             "所有世界的完整核验结果都保留在JSON；下表仅列18个预定验证世界：", "",
             "| 种子/规则 | 归档核验 | 市场机械门槛 | 覆盖门槛 | 真实/虚报/维持次数 |",
             "| --- | --- | --- | --- | --- |"]
    for run in report["runs"]:
        if run.get("phase") != "validation":
            continue
        cover = run.get("coverage")
        status = cover["status"] if cover is not None and run.get("rule") == "q_learning" else "不适用"
        lines.append(f"| {run.get('seed', '')}/{run.get('rule', run['path'])} | {run['verification_status']} | {run.get('gates', {}).get('mechanical', '未完成')} | {status} | {run.get('actions_real_wash_maintain', '未完成')} |")
    lines.extend(["", "市场与研究门槛单独保留：", ""])
    for name, item in report["market_gates"].items():
        failures = sum(row["status"] == "FAIL" for row in item["runs"])
        pending = sum(row["status"] not in ("PASS", "FAIL") for row in item["runs"])
        lines.append(f"- {name}：**{item['status']}**；失败{failures}个，待定或未完成{pending}个。")
    lines.extend(["", f"冻结验证覆盖门槛：**{gate['status']}**；决策{gate.get('decisions')}，未访问状态比例{gate.get('unseen_state_fraction')}。每个世界与合并样本均检查全局和每个已观察的规模/政策阶段组：未访问比例≤5%，出现占比≥1%的常见状态，每个实际合法内部选项至少20条训练记录。未观察到的组明确保留not_observed。", "",
                  "| 合并组 | 决策 | 未访问比例 | 覆盖状态 |", "| --- | --- | --- | --- |"])
    for group in gate.get("groups", []):
        lines.append(f"| size={group['size_class']}, epoch={group['policy_epoch']} | {group['decisions']} | {group['unseen_state_fraction']} | {group['status']} |")
    lines.extend(["", f"动作数学边界：最小/最大候选为{capacity['minimum_candidate_sd']}/{capacity['maximum_candidate_sd']} SD，每{capacity['decision_days']}日决策。内部稳态下全选最大真实改善的供给上界为{capacity['maximum_real_improvement_sd_per_year']} SD/年，假定衰减为{capacity['assumed_decay_sd_per_year']} SD/年。这只是可行性边界；实施延迟、成本收益、容量、自然衰减的未校准假设和部分可观察状态仍会改变行为，不保证净改善，也不构成政策效果。", "",
                  "实际账目按决策价锁定承诺金额并在次日应用一次，独立复算融资合同费率、相对初始费率的价值调整、价值锚与已闭窗口奖励。资源成本、罚金和补贴分别保留；奖励未使用NPV得分。指标成本按承诺日，学习奖励按应用日。末日未应用金额、未闭窗口、在途项目及存量虚报单列，不能视为完整终生利润或社会福利。", "",
                  "归档未保存全部投资者持仓，因此不声称独立复算局部需求导数或NPV最优排序；对NPV核对共同候选可行性、幅度、成本、生效日和实际账目。公开/规划信号本次检查内容指纹，时序另有信息机制归档核验。共享场景专属Q表可能已通过bootstrap反映未来政策，故本实验仅作单场景算法比较，不识别跨场景政策因果。", "",
                  "Q值允许绝对5e-13、相对5e-12的浮点容限；价值锚累计运算绝对容限2e-11。文件与内容哈希、动作、状态、合法集、计数、谱系和次日金额逐位核对。归档核验通过不会覆盖市场FAIL、覆盖FAIL或经验验证pending；保留种子分区也按冻结规格检查。", ""])
    if failed:
        lines.extend(["未通过的全局核验项：", "", *["- " + name for name in failed], ""])
    for run in report["runs"]:
        problems = [row["name"] for row in run.get("checks", []) if row["status"] != "PASS"]
        if problems or run.get("error"):
            lines.extend([f"归档 `{run['path']}` 的异常：{problems or run['error']}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", nargs="?", type=Path, default=Path("reports/disclosure_action_grid_development_20261011_v1"))
    parser.add_argument("--spec", type=Path, default=Path("configs/disclosure_action_grid_development_v1.json"))
    args = parser.parse_args()
    output = Path(__file__).resolve().parent
    try:
        report = verify_archive(args.archive, args.spec)
    except Exception as error:
        report = {"status": "INCOMPLETE", "generated_utc": datetime.now(timezone.utc).isoformat(),
                  "archive": str(args.archive), "verification_code_sha256": digest(Path(__file__)),
                  "error_type": type(error).__name__, "error": str(error)}
    (output / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    if "runs" in report:
        write_interpretation(report, output / "interpretation.md")
    else:
        (output / "interpretation.md").write_text(f"# 核验尚未完成\n\n{report['error_type']}: {report['error']}\n\n不作通过或研究结论。\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "runs": len(report.get("runs", [])),
                      "coverage_gate": report.get("coverage_gate", {}).get("status")}, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
