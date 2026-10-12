"""Independently verify a saved disclosure Q-learning smoke archive."""

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
PRIORITY = np.array([2, 0, 1])
ATOL, RTOL = 5e-13, 5e-12
FIELDS = (
    "true_goodness", "inflation", "impact_share", "impact_wealth_share", "pricing_slope",
    "actions", "amounts", "detections", "cost_fraction", "penalty_fraction", "subsidy_fraction",
    "financing_rate", "financing_cost", "financing_value_adjustment", "public_signal",
    "planning_signal", "disclosure_error", "audit_selected", "audit_publications", "verified_goodness",
    "action_due_day", "applied_resource_cost", "applied_fine", "applied_subsidy", "learning_states",
    "learning_groups", "valid_actions", "learning_rewards", "learning_transition", "unvisited_state",
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


def coverage(groups, states, mask, counts, unseen=None):
    visits, legal = np.zeros((6, 81), dtype=np.int64), np.zeros((6, 81, 3), dtype=np.int64)
    for group, state, allowed in zip(groups[1:].reshape(-1), states[1:].reshape(-1), mask[1:].reshape(-1, 3)):
        visits[group, state] += 1
        legal[group, state] += allowed.astype(np.int64)
    total = int(visits.sum())
    missing = None if unseen is None else int(np.asarray(unseen)[1:].sum())
    fraction = missing / total if missing is not None and total else None
    insufficient = []
    if counts is not None:
        common = (visits > 0) & (visits >= .01 * total)
        for group, state, action in np.argwhere(common[:, :, None] & (legal > 0) & (counts < 20)):
            insufficient.append({"group": int(group), "state": int(state), "action": int(action),
                                 "count": int(counts[group, state, action])})
    return {"visits": visits.tolist(), "legal_action_visits": legal.tolist(), "decisions": total,
            "unseen_state_decisions": missing, "unseen_state_fraction": fraction,
            "common_state_undercovered_actions": insufficient,
            "status": "PASS" if fraction is not None and fraction <= .05 and not insufficient else "FAIL"}


def replay_attributes(arrays, manifest, checks):
    cfg, domain, schedule = manifest["config"], manifest["domain"], manifest["policy"]
    n, last, step = cfg["n_firms"], cfg["trading_days"], cfg["firm_decision_interval"]
    periods = last // step + 1
    actions, amounts, prices = arrays["actions"], arrays["amounts"], arrays["market_prices"]
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
    masks = np.zeros((periods, n, 3), dtype=bool)
    selected_history = np.zeros((periods, n), dtype=np.int64)
    caught_history, publication_history = selected_history.copy(), selected_history.copy()
    verified_history = np.zeros((periods, n))
    capacity_ok = True
    exposure = cfg["financing_exposure_fraction"] * prices[0]
    discrete = cfg["firm_policy"] != "npv"
    fraction = manifest.get("learning", {}).get("metadata", {}).get("contract", {}).get("candidate_fraction", .01)
    delta = fraction * domain["max_change_per_period"]
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
            real_amount, wash_amount = np.minimum(delta, real_room), np.minimum(delta, report_room)
            offered = np.column_stack((real_amount, wash_amount, np.zeros(n)))
            masks[period] = offered > 0
            masks[period, :, 2] = True
            choice = actions[period]
            expected_amounts[period] = offered[np.arange(n), choice] if discrete else amounts[period]
            capacity_ok &= bool(np.all(amounts[period] >= 0) and np.all(amounts[period] <= domain["max_change_per_period"] + ATOL)
                                and np.all(amounts[period, choice == 0] <= real_room[choice == 0] + ATOL)
                                and np.all(amounts[period, choice == 1] <= report_room[choice == 1] + ATOL)
                                and np.all(amounts[period, choice == 2] == 0))
            c = cost_scale * np.exp(domain["cost_level_elasticity"] * goodness)
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
        checks.check("selected_action_is_legal", np.all(np.take_along_axis(masks[1:], actions[1:, :, None], axis=2)))
    return {"states": states, "groups": groups, "masks": masks, "firm_seed": firm_seed,
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


def replay_table(arrays, manifest, input_table, output_table, reconstructed, rewards, checks):
    values, counts, payload = input_table
    q, visits = values.copy(), counts.copy()
    n, cfg, learning = manifest["config"]["n_firms"], manifest["config"], manifest["learning"]
    states, groups, mask = reconstructed["states"], reconstructed["groups"], reconstructed["masks"]
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
                key = (int(groups[period - 1, firm]), int(states[period - 1, firm]), int(arrays["actions"][period - 1, firm]))
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
            probability = epsilon * allowed / allowed.sum(axis=1, keepdims=True) + (1 - epsilon) * best / best.sum(axis=1, keepdims=True)
            selected[period] = np.minimum((rng.random(n)[:, None] >= probability.cumsum(axis=1)).sum(axis=1), 2)
        else:
            selected[period] = PRIORITY[np.argmax(option[:, PRIORITY], axis=1)]
            selected[period, unseen[period]] = 2
    checks.array("ql_actions_from_table_mask_and_separate_rng", arrays["actions"], selected, exact=True)
    checks.array("unvisited_state_from_preselection_counts", arrays["unvisited_state"], unseen, exact=True)
    checks.array("independent_synchronous_td_final_Q", output_table[0], q)
    checks.array("independent_td_final_counts", output_table[1], visits, exact=True)
    checks.check("table_hyperparameters_match_manifest", payload["learning_rate"] == alpha and payload["discount"] == learning["discount"])
    if not training:
        checks.array("frozen_values_unchanged", output_table[0], values, exact=True)
        checks.array("frozen_counts_unchanged", output_table[1], counts, exact=True)
        checks.check("frozen_epsilon_zero", epsilon == 0)
    return coverage(groups, states, mask, output_table[1], unseen)


def compare_learning_report(report, coverage_report, money, arrays, manifest, checks):
    cfg, last, step = manifest["config"], manifest["config"]["trading_days"], manifest["config"]["firm_decision_interval"]
    for key in ("visits", "legal_action_visits", "decisions", "unseen_state_decisions", "unseen_state_fraction", "common_state_undercovered_actions"):
        checks.check("reported_coverage_" + key, report["coverage"][key] == coverage_report[key])
    applicable = cfg["firm_policy"] == "q_learning" and not manifest["learning"]["training"]
    checks.check("reported_coverage_status", report["coverage"]["status"] == (coverage_report["status"] if applicable else "not_applicable"))
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
                 and manifest["source_hashes"] == experiment["contract"]["source_hashes"])
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
                         and table[2]["format_version"] == 1)
        checks.check("initial_table_content_identity", table_identity(*table_before[:2]) == manifest["learning"]["initial_table_fingerprint"])
        coverage_report = replay_table(arrays, manifest, table_before, table_after, reconstructed, money["rewards"], checks)
    elif cfg["firm_policy"] == "npv_discrete":
        coverage_report = coverage(reconstructed["groups"], reconstructed["states"], reconstructed["masks"], None)
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
              "gates": {key: validation[key]["status"] for key in ("mechanical", "stylized", "empirical_calibration")},
              "coverage": coverage_report, "actions_real_wash_maintain": np.bincount(arrays["actions"][1:].ravel(), minlength=3).tolist(),
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
    return result, inputs, {"manifest": manifest, "arrays": arrays, "before": table_before, "after": table_after}


def verify_archive(archive):
    archive = archive.resolve()
    checks, inputs, cache, runs = Checks(), {}, {}, []
    experiment, summary = read_json(archive / "experiment.json"), read_json(archive / "summary.json")
    for name in ("experiment.json", "summary.json", "initial_model.npz", "frozen_model.npz"):
        path = archive / name
        if path.is_file():
            inputs[str(path)] = digest(path)
    identity = {key: value for key, value in experiment.items() if key != "experiment_id"}
    checks.check("experiment_identity", hashlib.sha256(canonical(identity)).hexdigest() == experiment["experiment_id"] == summary["experiment_id"])
    checks.check("single_baseline_development_scope", experiment["purpose"] == summary["purpose"] == "development"
                 and experiment["policy"]["intervention"] is None)
    budget = experiment["budget"]
    checks.check("fixed_smoke_budget", budget["training_seeds"] == [25001, 25002] and budget["validation_seeds"] == [25101, 25102]
                 and budget["validation_rules"] == ["q_learning", "npv_discrete", "npv"])
    checks.check("fixed_market_scale", experiment["config"]["n_investors"] == 150 and experiment["config"]["n_firms"] == 30
                 and experiment["config"]["trading_days"] == 1800 and experiment["config"]["burn_in_days"] == 600)
    checks.check("seed_partitions", not set(budget["training_seeds"]) & set(budget["validation_seeds"])
                 and not set(budget["training_seeds"] + budget["validation_seeds"]) & set(range(20261101, 20261131)))
    checks.check("summary_budget_and_contract", summary["budget"] == budget and summary["contract"] == experiment["contract"])
    expected = {(phase, seed, mode) for phase, seeds, modes in (("training", budget["training_seeds"], ["q_learning"]),
                                                               ("validation", budget["validation_seeds"], budget["validation_rules"]))
                for seed in seeds for mode in modes}
    actual = [(record["phase"], record["seed"], record["firm_policy"]) for record in summary["records"]]
    checks.check("all_planned_runs_retained_once", set(actual) == expected and len(actual) == len(expected))
    checks.check("summary_completion_truthful", (summary["status"] == "complete") ==
                 (len(actual) == len(expected) and all(record["status"] == "complete" for record in summary["records"])))
    for record in summary["records"]:
        folder = (archive / record["path"]).resolve()
        checks.check("run_path_within_archive:" + record["path"], folder.is_relative_to(archive.resolve()))
        try:
            result, files, detail = verify_run(folder, record, experiment)
            runs.append(result)
            inputs.update(files)
            if detail is not None:
                cache[(record["phase"], record["seed"], record["firm_policy"])] = detail
        except Exception as error:
            runs.append({"path": record["path"], "archive_status": record["status"], "verification_status": "FAIL",
                         "error_type": type(error).__name__, "error": str(error)})
    initial = read_table(archive / "initial_model.npz")
    checks.check("initial_model_sha256", digest(archive / "initial_model.npz") == summary["initial_model_sha256"])
    checks.array("initial_zero_Q", initial[0], np.zeros((6, 81, 3)), exact=True)
    checks.array("initial_zero_counts", initial[1], np.zeros((6, 81, 3), dtype=np.int64), exact=True)
    checks.check("initial_metadata_contract", initial[2]["metadata"]["contract"] == experiment["contract"])
    previous = initial
    for index, seed in enumerate(budget["training_seeds"]):
        row = cache.get(("training", seed, "q_learning"))
        if row is None:
            checks.check("training_lineage:" + str(seed), False, "Training archive incomplete; no substitute seed.")
            continue
        checks.array("lineage_input_Q:" + str(seed), row["before"][0], previous[0], exact=True)
        checks.array("lineage_input_counts:" + str(seed), row["before"][1], previous[1], exact=True)
        metadata = row["manifest"]["learning"]["metadata"]
        checks.check("training_lineage_metadata:" + str(seed), metadata["completed_training_seeds"] == budget["training_seeds"][:index]
                     and metadata["experiment_id"] == experiment["experiment_id"]
                     and row["manifest"]["learning"]["epsilon"] == budget["epsilon_by_world"][index])
        previous = row["after"]
    frozen = read_table(archive / "frozen_model.npz")
    checks.check("frozen_model_sha256", digest(archive / "frozen_model.npz") == summary["frozen_model_sha256"])
    checks.array("last_training_to_frozen_Q", frozen[0], previous[0], exact=True)
    checks.array("last_training_to_frozen_counts", frozen[1], previous[1], exact=True)
    checks.check("frozen_semantic_identity", table_identity(*frozen[:2]) == summary["frozen_table_fingerprint"])
    checks.check("frozen_metadata_lineage", frozen[2]["metadata"]["completed_training_seeds"] == budget["training_seeds"] == summary["completed_training_seeds"]
                 and frozen[2]["metadata"]["phase"] == "frozen")
    pooled_visits, pooled_legal, unseen, worlds = np.zeros((6, 81), dtype=np.int64), np.zeros((6, 81, 3), dtype=np.int64), 0, []
    for seed in budget["validation_seeds"]:
        row = cache.get(("validation", seed, "q_learning"))
        if row is None:
            checks.check("frozen_evaluation_present:" + str(seed), False)
            continue
        for tag in ("before", "after"):
            checks.array("frozen_eval_" + tag + "_Q:" + str(seed), row[tag][0], frozen[0], exact=True)
            checks.array("frozen_eval_" + tag + "_counts:" + str(seed), row[tag][1], frozen[1], exact=True)
            checks.check("frozen_eval_" + tag + "_metadata:" + str(seed), row[tag][2]["metadata"] == frozen[2]["metadata"])
        cov = coverage(row["arrays"]["learning_groups"], row["arrays"]["learning_states"], row["arrays"]["valid_actions"],
                       frozen[1], row["arrays"]["unvisited_state"])
        pooled_visits += np.asarray(cov["visits"])
        pooled_legal += np.asarray(cov["legal_action_visits"])
        unseen += cov["unseen_state_decisions"]
        worlds.append({"seed": seed, "status": cov["status"], "unseen_state_fraction": cov["unseen_state_fraction"],
                       "undercovered_actions": cov["common_state_undercovered_actions"]})
        for mode in ("npv_discrete", "npv"):
            reference = cache.get(("validation", seed, mode))
            if reference is not None:
                for field in ("market_prices", "market_intrinsic_values", "true_goodness", "inflation"):
                    checks.array("paired_initial_" + mode + "_" + field + ":" + str(seed), reference["arrays"][field][0], row["arrays"][field][0], exact=True)
                checks.array("paired_audit_random_selection:" + str(seed) + ":" + mode, reference["arrays"]["audit_selected"], row["arrays"]["audit_selected"], exact=True)
    total = int(pooled_visits.sum())
    fraction = unseen / total if total else None
    common = (pooled_visits > 0) & (pooled_visits >= .01 * total)
    undercovered = [{"group": int(g), "state": int(s), "action": int(a), "count": int(frozen[1][g, s, a])}
                    for g, s, a in np.argwhere(common[:, :, None] & (pooled_legal > 0) & (frozen[1] < 20))]
    gate = "PASS" if len(worlds) == len(budget["validation_seeds"]) and fraction is not None and fraction <= .05 and not undercovered and all(row["status"] == "PASS" for row in worlds) else "FAIL"
    reported = summary["validation"]["coverage"]
    checks.array("pooled_coverage_visits", reported.get("visits", []), pooled_visits, exact=True)
    checks.array("pooled_coverage_legal_visits", reported.get("legal_action_visits", []), pooled_legal, exact=True)
    checks.check("pooled_coverage_gate_preserved", reported["status"] == gate and reported.get("unseen_state_decisions") == unseen
                 and reported.get("unseen_state_fraction") == fraction)
    for path, before in inputs.items():
        checks.check("archive_unchanged:" + str(Path(path).relative_to(archive)), digest(Path(path)) == before)
    complete = len(runs) == len(expected) and all(row["archive_status"] == "complete" for row in runs)
    good = checks.passed and all(row["verification_status"] == "PASS" for row in runs)
    return {"status": "PASS" if good and complete else "FAIL" if not good else "INCOMPLETE",
            "scope": "Independent archive verification, two-world single-baseline development smoke only.",
            "generated_utc": datetime.now(timezone.utc).isoformat(), "archive": str(archive),
            "verification_code_sha256": digest(Path(__file__)), "input_hashes": inputs,
            "verifier_python": platform.python_version(), "verifier_numpy": np.__version__,
            "numeric_tolerances": {"absolute": ATOL, "relative": RTOL, "value_anchor_absolute": 2e-11,
                                   "exact": ["file/content hashes", "lineage arrays", "counts", "actions", "state/group/masks", "next-day monetary ledgers"]},
            "checks": checks.rows, "runs": runs,
            "coverage_gate": {"status": gate, "decisions": total, "unseen_state_decisions": unseen,
                              "unseen_state_fraction": fraction, "worlds": worlds, "pooled_undercovered_actions": undercovered},
            "discrete_capacity_vs_decay": {
                "candidate_fraction": experiment["contract"]["candidate_fraction"],
                "delta_sd": experiment["contract"]["candidate_fraction"] * experiment["domain"]["max_change_per_period"],
                "decision_days": experiment["config"]["firm_decision_interval"],
                "maximum_real_improvement_sd_per_year": experiment["contract"]["candidate_fraction"] * experiment["domain"]["max_change_per_period"] * YEAR / experiment["config"]["firm_decision_interval"],
                "assumed_decay_sd_per_year": experiment["domain"]["natural_decay"],
                "scope": "Interior steady-state upper bound before implementation-delay losses; lower-bound decay clipping changes net realized losses.",
            },
            "limitations": ["No market simulations or ABM implementation functions were called by this verifier.",
                            "Recorded actions, seeded attribute/fundamental draws, daily accounting and synchronous TD were independently replayed.",
                            "Local investor-demand derivatives and NPV optimal selection cannot be independently reconstructed without investor holdings; only candidate feasibility, size, cost and delays are verified.",
                            "Fines identify a dated audit of aggregate inflation, not an identifiable single previous washing action.",
                            "A two-world smoke budget cannot establish training sufficiency, full M4 acceptance, empirical validity, policy ranking, lifetime profit or social welfare.",
                            "Coverage and mechanical failures are retained independently of archive-integrity status; reserved seeds were not used."]}


def write_interpretation(report, path):
    failed = [row["name"] for row in report["checks"] if row["status"] != "PASS"]
    lines = ["# Q-learning 冒烟归档独立核验", "", f"核验完整性：**{report['status']}**。范围是单一 baseline、2个训练世界及2个验证种子的三规则开发冒烟；不代表 M4 已验收。", "",
             f"归档：`{report['archive']}`。核验代码 SHA256：`{report['verification_code_sha256']}`。", "",
             "核验未调用市场、学习更新或 runner 实现，也未额外运行市场。逐文件检查源码/工件哈希和身份，重建属性/在途项目、次日实际金额、融资合同与价值锚、逐窗口奖励，并从初表手写同步 TD 和独立探索随机流重算最终 Q/计数。", "",
             "| 阶段/种子/规则 | 归档核验 | 市场机械门槛 | 覆盖门槛 | 真实/虚报/维持次数 |", "| --- | --- | --- | --- | --- |"]
    for run in report["runs"]:
        label = f"{run.get('phase', '')}/{run.get('seed', '')}/{run.get('rule', run['path'])}"
        cover = run.get("coverage")
        status = cover["status"] if cover is not None and run.get("rule") == "q_learning" and run.get("phase") == "validation" else "不适用"
        lines.append(f"| {label} | {run['verification_status']} | {run.get('gates', {}).get('mechanical', '未完成')} | {status} | {run.get('actions_real_wash_maintain', '未完成')} |")
    gate = report["coverage_gate"]
    capacity = report["discrete_capacity_vs_decay"]
    lines.extend(["", f"冻结验证覆盖门槛：**{gate['status']}**；总决策{gate['decisions']}，未访问状态比例{gate['unseen_state_fraction']}。每个世界与合并样本都按原≤5%未访问、≥1%常见状态各合法动作至少20条训练记录核验；未通过不能自动归为实现错误，也没有替换种子或调低门槛。", "",
                  f"离散可行集存在先验限制：固定rho={capacity['candidate_fraction']}，单次最大真实改善{capacity['delta_sd']} SD，每{capacity['decision_days']}日一次，即全部选择真实改善也最多{capacity['maximum_real_improvement_sd_per_year']} SD/年；领域假设自然衰减为{capacity['assumed_decay_sd_per_year']} SD/年。上界未计实施等待，下界处衰减裁剪另算。因此内部区间的净下降已受到幅度约束强烈预定，不能解释为QL不会投资或政策无效，也不能把与continuous NPV的数量级差异当作同可行集算法效应。归档中实际改善增量与实际衰减已分项重算，本轮不修改rho迫使结果转正。下一开发合同需先论证幅度/网格相对衰减和收益成本的可行性。", "",
                  "成本/补贴由其决策事件识别；罚金由核查事件识别，聚合虚报不伪造单次行动来源。末日尚未应用金额和项目责任单列，不构造终止奖励，不当作已经完成的终生利润。连续 NPV 缺少新增日账字段时，从原决策比例与决策价独立重建；指标窗口按承诺日，学习奖励按应用日，两者不能混称同一成本时点。", "",
                  "结果归档未保留全部投资者持仓，因此本核验不声称独立验证局部需求导数或离散 NPV 最优排序；共同候选、实际成本、容量、生效日及 QL 实际奖励/表更新可以独立核对。", "",
                  "Q值允许绝对5e-13、相对5e-12的浮点容限；价值锚累计运算绝对容限2e-11。哈希、动作、状态、计数、谱系和次日金额逐位核对。任何市场失败均保留，未使用20261101..20261130正式保留种子。", ""])
    if failed:
        lines.extend(["存在未通过的全局核验项：", "", *["- " + name for name in failed], ""])
    for run in report["runs"]:
        problems = [row["name"] for row in run.get("checks", []) if row["status"] != "PASS"]
        if problems or run.get("error"):
            lines.extend([f"归档 `{run['path']}` 的异常：{problems or run['error']}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", nargs="?", type=Path, default=Path("reports/disclosure_q_learning_smoke_20261011_v1"))
    args = parser.parse_args()
    output = Path(__file__).resolve().parent
    try:
        report = verify_archive(args.archive)
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
