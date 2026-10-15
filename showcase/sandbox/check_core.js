'use strict';
// Cross-language check: node showcase/sandbox/check_core.js
// Expected values come from the Python model (reports/disclosure_stage_g_20261015/fixtures.py).
// Choices must match exactly. Decision values must agree to a relative error of 1e-12. Per-period
// means in the dynamics are O(1) SD sums of 200 firms, so they are compared relative to max(|x|, 1).
const fs = require('fs');
const path = require('path');
const core = require('./core.js');

const TOLERANCE = 1e-12;
const here = __dirname;
const read = file => JSON.parse(fs.readFileSync(path.join(here, file), 'utf8'));
const cases = read('fixtures/core_cases.json');
const dynamics = read('fixtures/dynamics_cases.json');
const sandbox = read('../data/sandbox_firms.json');

const failures = [];
let worst = 0, compared = 0;
const relative = (a, b) => (a === b ? 0 : Math.abs(a - b) / Math.max(Math.abs(a), Math.abs(b)));
const close = (label, actual, expected, scale = 0) => {
  const error = a => (a === expected ? 0 : Math.abs(a - expected) / Math.max(Math.abs(a), Math.abs(expected), scale));
  const e = error(actual);
  compared += 1;
  worst = Math.max(worst, e);
  if (!(e <= TOLERANCE)) failures.push(`${label}: ${actual} vs ${expected} (relative error ${e.toExponential(2)})`);
};
const same = (label, actual, expected) => {
  compared += 1;
  if (actual !== expected) failures.push(`${label}: ${actual} vs ${expected}`);
};

// Generator.
for (const row of cases.prng) {
  const random = core.mulberry32(row.seed);
  row.values.forEach((value, k) => same(`prng ${row.seed}[${k}]`, random(), value));
}

// Single-period NPV decisions.
let decisions = 0;
cases.decisions.forEach((c, r) => {
  const factors = core.financingFactors({
    rate: c.discount_rate, decisionDay: c.decision_day, horizonDays: c.horizon_days,
    repricingInterval: c.repricing_interval, periodDays: c.period_days,
    implementationDelay: c.domain.implementation_delay_days,
    disclosureDelay: c.regime.disclosure_delay_days ?? c.domain.disclosure_delay_days,
    auditProbability: c.regime.audit_probability, transparency: c.regime.transparency,
  });
  ['real', 'displaced', 'wash', 'fine'].forEach((key, k) => close(`regime ${r} ${key}`, factors[key], c.expected.factors[k]));
  c.inputs.benefit.forEach((benefit, i) => {
    const choice = core.npvChoice({
      benefit, marginalCost: c.inputs.marginal_cost[i], improveCapacity: c.inputs.improve_capacity[i],
      inflateCapacity: c.inputs.inflate_capacity[i],
      newCaseFine: c.inputs.new_case_fine === null ? null : c.inputs.new_case_fine[i],
    }, c.regime, c.domain, factors);
    const label = `regime ${r} firm ${i}`;
    same(`${label} action`, choice.action, c.expected.actions[i]);
    close(`${label} amount`, choice.amount, c.expected.amounts[i]);
    close(`${label} npv`, choice.npv, c.expected.npv[i]);
    close(`${label} cost`, choice.costFraction, c.expected.cost_fraction[i]);
    close(`${label} subsidy`, choice.subsidyFraction, c.expected.subsidy_fraction[i]);
    decisions += 1;
  });
});

// New-case probability of the fixed fine.
cases.new_case.forEach((c, r) => {
  const result = core.newCaseProbability(c.inflation, c.pending, c.decision_day, c.wash_due, c.period_days, c.audit_probability);
  c.expected.forEach((value, i) => close(`new case ${r} firm ${i}`, result[i], value));
});

// The snapshot state: the port must take the decision the full model took on that day.
const domains = sandbox.domains;
for (const [key, d] of Object.entries(domains)) {
  const state = core.createState(d.firms.goodness, d.firms.inflation, d.firms.cost_scale, d.firms.pending);
  const regime = { ...d.baseline_policy, disclosure_delay_days: null };
  const { choices } = core.decide(state, d.firms, d, d.market, regime, sandbox.snapshot_day);
  choices.forEach((choice, i) => {
    same(`${key} snapshot firm ${i} action`, choice.action, d.firms.full_model_decision.actions[i]);
    close(`${key} snapshot firm ${i} amount`, choice.amount, d.firms.full_model_decision.amounts[i]);
  });
}

// Simplified dynamics, period by period.
let periods = 0;
for (const run of dynamics.runs) {
  const d = domains[run.domain];
  const result = core.simulate(d.firms, d, d.market, run.policy, { naturalDecay: run.natural_decay, auditSeed: run.audit_seed });
  run.periods.forEach((p, k) => {
    const label = `${run.domain}/${run.name} day ${p.day}`;
    same(`${label} day`, result.decisionDays[k], p.day);
    same(`${label} actions`, Array.from(result.actions[k]).join(''), p.actions);
    same(`${label} detections`, result.detections[k].reduce((s, v) => s + v, 0), p.detections);
    close(`${label} amount sum`, result.amounts[k].reduce((s, v) => s + v, 0), p.amount_sum, 1e-300);
    close(`${label} fine sum`, result.fines[k].reduce((s, v) => s + v, 0), p.fine_sum, 1e-300);
    close(`${label} mean goodness`, result.meanGoodness[p.day], p.mean_goodness, 1);
    close(`${label} mean inflation`, result.meanInflation[p.day], p.mean_inflation, 1);
    periods += 1;
  });
  run.final_goodness.forEach((value, i) => close(`${run.name} final goodness ${i}`, result.finalGoodness[i], value, 1));
  run.final_inflation.forEach((value, i) => close(`${run.name} final inflation ${i}`, result.finalInflation[i], value, 1));
  const metrics = core.windowMetrics(result, d.firms, d.market.burn_in_days, d.market.trading_days);
  for (const key of ['true_change_sd', 'inflation_mean_sd', 'wash_share', 'large_minus_small_sd', 'resource_cost_fraction_initial_cap']) {
    close(`${run.name} ${key}`, metrics[key], run.metrics[key], 1);
  }
}

console.log(`decisions ${decisions}, dynamics periods ${periods}, values compared ${compared}, worst relative error ${worst.toExponential(2)}`);
if (failures.length) {
  console.error(`${failures.length} mismatches:\n${failures.slice(0, 20).join('\n')}`);
  process.exit(1);
}
console.log('sandbox core matches the Python model');
