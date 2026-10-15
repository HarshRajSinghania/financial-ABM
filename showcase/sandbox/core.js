'use strict';
// Sandbox decision core: a port of the firm side of src/abm/disclosure (game.py, financing.py)
// and of showcase/sandbox/reference.py. Cross-language fixtures hold it to the Python model:
// identical choices and relative errors of at most 1e-12. Supported regimes: unpublished
// audits and daily reports, the setting of every stage F scenario.
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.SandboxCore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, () => {
  const DAYS_PER_YEAR = 252;
  const IMPROVE = 0, INFLATE = 1, MAINTAIN = 2;
  const MINIMUM_NPV = 1e-9;

  // Mulberry32, bit for bit the same as reference.Mulberry32.
  const mulberry32 = seed => {
    let state = seed >>> 0;
    return () => {
      state = (state + 0x6D2B79F5) >>> 0;
      let t = state;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t = ((t + Math.imul(t ^ (t >>> 7), t | 61)) >>> 0) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };

  // financing.financing_signal_factors for one discount rate (publish_audit_results false,
  // reporting_interval_days 1): real and displaced-real annuities, wash survival, fine factor.
  const financingFactors = ({ rate, decisionDay, horizonDays, repricingInterval, periodDays,
    implementationDelay, disclosureDelay, auditProbability, transparency }) => {
    const realDue = decisionDay + Math.max(1, implementationDelay);
    const washDue = decisionDay + Math.max(1, disclosureDelay);
    const firstAudit = Math.floor((washDue + periodDays - 1) / periodDays) * periodDays;
    const decisionPeriod = Math.floor(decisionDay / periodDays);
    let real = 0, wash = 0, old = 0;
    for (let t = 1; t <= horizonDays; t++) {
      const quoted = Math.floor((decisionDay + t) / repricingInterval) * repricingInterval - 1;
      const discount = Math.exp(-t * rate / DAYS_PER_YEAR);
      const audits = Math.max(0, Math.floor((quoted - 1 - firstAudit) / periodDays) + 1);
      if (quoted >= realDue) {
        real += discount;
        const checks = Math.max(0, Math.floor((quoted - 1) / periodDays) - decisionPeriod);
        old += Math.pow(1 - auditProbability, checks) * discount;
      }
      if (quoted >= washDue) wash += Math.pow(1 - auditProbability, audits) * discount;
    }
    real /= DAYS_PER_YEAR;
    wash /= DAYS_PER_YEAR;
    const displaced = real - (1 - transparency) * (old / DAYS_PER_YEAR);
    const fine = auditProbability === 0 ? 0 : auditProbability * Math.exp(-rate * (firstAudit - decisionDay) / DAYS_PER_YEAR)
      / (1 - (1 - auditProbability) * Math.exp(-rate * periodDays / DAYS_PER_YEAR));
    return { real, displaced, wash, fine };
  };

  const checkRegime = regime => {
    if (regime.publish_audit_results || (regime.reporting_interval_days ?? 1) !== 1) {
      throw new Error('the sandbox supports unpublished audits and daily reports only');
    }
  };

  const disclosureDelay = (regime, domain) => regime.disclosure_delay_days ?? domain.disclosure_delay_days;

  const factorsFor = (regime, domain, market, decisionDay) => financingFactors({
    rate: market.firm_discount_rate, decisionDay, horizonDays: market.financing_horizon_days,
    repricingInterval: market.financing_repricing_interval, periodDays: market.firm_decision_interval,
    implementationDelay: domain.implementation_delay_days, disclosureDelay: disclosureDelay(regime, domain),
    auditProbability: regime.audit_probability, transparency: regime.transparency,
  });

  // game.npv_choices for one firm. newCaseFine is the fixed fine over market cap times the
  // probability that a new report opens a case, or null when there is no fixed fine.
  const npvChoice = ({ benefit, marginalCost, improveCapacity, inflateCapacity, newCaseFine = null }, regime, domain, factors) => {
    const improveBenefit = benefit * factors.real;
    const improveGain = improveBenefit + regime.subsidy;
    const inflateGain = Math.max(benefit * (1 - regime.transparency) * factors.wash - regime.penalty * factors.fine, 0);
    const washCost = domain.wash_cost_ratio * marginalCost;
    const cap = domain.max_change_per_period;
    const improveCap = Math.min(Math.max(improveCapacity, 0), cap);
    const inflateCap = Math.min(Math.max(inflateCapacity, 0), cap);
    const displacedBenefit = benefit * factors.displaced;
    const displacedGain = displacedBenefit + regime.subsidy;
    const improveAmount = Math.min(improveCap, Math.max(
      Math.min(improveGain / (2 * marginalCost), inflateCap), displacedGain / (2 * marginalCost)));
    const inflateAmount = Math.min(inflateGain / (2 * washCost), inflateCap);
    const realValue = improveBenefit * Math.min(improveAmount, inflateCap)
      + displacedBenefit * Math.max(improveAmount - inflateCap, 0);
    let washValue = inflateGain * inflateAmount - washCost * (inflateAmount * inflateAmount);
    if (newCaseFine !== null && inflateAmount > 0) washValue -= newCaseFine * factors.fine;
    const values = [realValue + regime.subsidy * improveAmount - marginalCost * (improveAmount * improveAmount), washValue, 0];
    let action = 0;
    for (let k = 1; k < 3; k++) if (values[k] > values[action]) action = k;
    const best = values[action];
    if (best <= MINIMUM_NPV) action = MAINTAIN;
    const amount = action === IMPROVE ? improveAmount : action === INFLATE ? inflateAmount : 0;
    const costFraction = action === IMPROVE ? marginalCost * (amount * amount) : action === INFLATE ? washCost * (amount * amount) : 0;
    return {
      action, amount, values, costFraction, subsidyFraction: action === IMPROVE ? regime.subsidy * amount : 0,
      npv: action === MAINTAIN ? 0 : best, improveAmount, inflateAmount,
    };
  };

  // game.new_case_probability: chance that inflation decided now opens a new case.
  const newCaseProbability = (inflation, pending, decisionDay, washDue, periodDays, auditProbability) => {
    const open = Float64Array.from(inflation, w => (w > 0 ? 1 : 0));
    const arrivals = new Map();
    for (const item of pending) {
      if (item.kind === INFLATE && decisionDay < item.due_day && item.due_day <= washDue) {
        const firms = item.firms.filter((_, j) => item.amounts[j] > 0);
        if (!arrivals.has(item.due_day)) arrivals.set(item.due_day, []);
        arrivals.get(item.due_day).push(firms);
      }
    }
    const days = new Set(arrivals.keys());
    for (let day = (Math.floor(decisionDay / periodDays) + 1) * periodDays; day < washDue; day += periodDays) days.add(day);
    for (const day of [...days].sort((a, b) => a - b)) {
      for (const firms of arrivals.get(day) ?? []) for (const i of firms) open[i] = 1;
      if (day % periodDays === 0 && day < washDue) for (let i = 0; i < open.length; i++) open[i] *= 1 - auditProbability;
    }
    return open.map(value => 1 - value);
  };

  // State as in game.AttributeState; pending items are {due_day, kind, firms, amounts}.
  const createState = (goodness, inflation, costScale, pending = []) => ({
    goodness: Float64Array.from(goodness), inflation: Float64Array.from(inflation),
    costScale: Float64Array.from(costScale),
    pending: pending.map(item => ({ due_day: item.due_day, kind: item.kind, firms: Int32Array.from(item.firms), amounts: Float64Array.from(item.amounts) })),
  });

  const advance = (state, day, domain, naturalDecay) => {
    const [low, high] = domain.goodness_bounds;
    const top = domain.observation_ceiling ?? high;
    const step = naturalDecay / DAYS_PER_YEAR;
    const { goodness: g, inflation: w } = state;
    for (let i = 0; i < g.length; i++) g[i] = Math.max(g[i] - step, low);
    const remaining = [];
    for (const item of state.pending) {
      if (item.due_day > day) { remaining.push(item); continue; }
      for (let j = 0; j < item.firms.length; j++) {
        const i = item.firms[j];
        if (item.kind === IMPROVE) g[i] = Math.min(g[i] + item.amounts[j], high);
        else w[i] += item.amounts[j];
      }
    }
    state.pending = remaining;
    for (let i = 0; i < w.length; i++) w[i] = Math.max(Math.min(w[i], top - g[i]), 0);
  };

  const capacities = (state, reportBound) => {
    const n = state.goodness.length;
    const improve = new Float64Array(n), inflate = new Float64Array(n);
    for (let i = 0; i < n; i++) {
      improve[i] = reportBound - state.goodness[i];
      inflate[i] = reportBound - state.goodness[i] - state.inflation[i];
    }
    for (const item of state.pending) {
      for (let j = 0; j < item.firms.length; j++) {
        if (item.kind === IMPROVE) improve[item.firms[j]] -= item.amounts[j];
        inflate[item.firms[j]] -= item.amounts[j];
      }
    }
    return { improve, inflate };
  };

  // reference.decide: every firm's choice this period, with B and market cap fixed.
  const decide = (state, firms, domain, market, regime, day) => {
    checkRegime(regime);
    const n = state.goodness.length;
    const room = capacities(state, domain.report_bound);
    const washDue = day + Math.max(1, disclosureDelay(regime, domain));
    const factors = factorsFor(regime, domain, market, day);
    const probability = regime.fixed_fine ? newCaseProbability(state.inflation, state.pending, day, washDue,
      market.firm_decision_interval, regime.audit_probability) : null;
    const choices = [];
    for (let i = 0; i < n; i++) {
      choices.push(npvChoice({
        benefit: firms.benefit[i], marginalCost: state.costScale[i] * Math.exp(domain.cost_level_elasticity * state.goodness[i]),
        improveCapacity: room.improve[i], inflateCapacity: room.inflate[i],
        newCaseFine: probability ? regime.fixed_fine / firms.market_cap[i] * probability[i] : null,
      }, regime, domain, factors));
    }
    return { choices, washDue, factors, room, probability };
  };

  const schedule = (state, dueDay, kind, choices) => {
    const firms = [], amounts = [];
    choices.forEach((choice, i) => { if (choice.action === kind) { firms.push(i); amounts.push(choice.amount); } });
    if (firms.length) state.pending.push({ due_day: dueDay, kind, firms: Int32Array.from(firms), amounts: Float64Array.from(amounts) });
  };

  const regimeAt = (policy, day) => (policy.intervention && day >= policy.start_day ? policy.intervention : policy.baseline);

  // reference.simulate: days 1..tradingDays from the initial true levels.
  const simulate = (firms, domain, market, policy, { naturalDecay, auditSeed, tradingDays = market.trading_days,
    windowStart = market.burn_in_days, onPeriod = null }) => {
    const n = firms.size_class.length;
    const state = createState(firms.initial_goodness, new Float64Array(n), firms.cost_scale);
    const random = mulberry32(auditSeed);
    const interval = market.firm_decision_interval;
    const decisions = Math.floor(tradingDays / interval);
    const meanGoodness = new Float64Array(tradingDays + 1), meanInflation = new Float64Array(tradingDays + 1);
    const actions = [], amounts = [], detections = [], resourceCost = [], fines = [];
    const mean = values => { let s = 0; for (const v of values) s += v; return s / values.length; };
    meanGoodness[0] = mean(state.goodness);
    const goodnessAt = {};
    for (let day = 1; day <= tradingDays; day++) {
      advance(state, day, domain, naturalDecay);
      if (day % interval === 0) {
        const regime = regimeAt(policy, day);
        const caught = new Uint8Array(n), fine = new Float64Array(n);
        for (let i = 0; i < n; i++) {
          if (random() < regime.audit_probability && state.inflation[i] > 0) {
            caught[i] = 1;
            fine[i] = regime.penalty * state.inflation[i] + regime.fixed_fine / firms.market_cap[i];
            state.inflation[i] = 0;
          }
        }
        const { choices, washDue } = decide(state, firms, domain, market, regime, day);
        schedule(state, day + Math.max(1, domain.implementation_delay_days), IMPROVE, choices);
        schedule(state, washDue, INFLATE, choices);
        actions.push(Int8Array.from(choices, c => c.action));
        amounts.push(Float64Array.from(choices, c => c.amount));
        resourceCost.push(Float64Array.from(choices, c => c.costFraction));
        detections.push(caught);
        fines.push(fine);
        if (onPeriod) onPeriod(day, state, choices);
      }
      meanGoodness[day] = mean(state.goodness);
      meanInflation[day] = mean(state.inflation);
      if (day === windowStart || day === tradingDays) goodnessAt[day] = Float64Array.from(state.goodness);
    }
    const decisionDays = Array.from({ length: decisions }, (_, k) => (k + 1) * interval);
    return { decisionDays, actions, amounts, detections, resourceCost, fines, meanGoodness, meanInflation, goodnessAt,
      finalGoodness: state.goodness, finalInflation: state.inflation };
  };

  // reference.window_metrics.
  const windowMetrics = (run, firms, startDay, endDay) => {
    const n = firms.size_class.length;
    const change = Float64Array.from(run.goodnessAt[endDay], (g, i) => g - run.goodnessAt[startDay][i]);
    const average = values => values.reduce((s, v) => s + v, 0) / values.length;
    let washes = 0, decisions = 0, inflation = 0, cost = 0;
    const bySize = [[0, 0], [0, 0], [0, 0]];
    run.decisionDays.forEach((day, k) => {
      if (day <= startDay || day > endDay) return;
      for (let i = 0; i < n; i++) {
        const wash = run.actions[k][i] === INFLATE ? 1 : 0;
        washes += wash; decisions += 1;
        bySize[firms.size_class[i]][0] += wash; bySize[firms.size_class[i]][1] += 1;
        cost += run.resourceCost[k][i] * firms.market_cap[i];
      }
    });
    for (let day = startDay; day <= endDay; day++) inflation += run.meanInflation[day];
    const members = k => [...change].filter((_, i) => firms.size_class[i] === k);
    return {
      true_change_sd: average([...change]),
      inflation_mean_sd: inflation / (endDay - startDay + 1),
      wash_share: decisions ? washes / decisions : 0,
      wash_share_by_size: { large: bySize[0][0] / bySize[0][1], mid: bySize[1][0] / bySize[1][1], small: bySize[2][0] / bySize[2][1] },
      large_minus_small_sd: average(members(0)) - average(members(2)),
      resource_cost_fraction_initial_cap: cost / firms.market_cap.reduce((s, v) => s + v, 0),
    };
  };

  // Proposition 2 threshold: with a case already open, washing stops once tau >= 1 - sqrt(w) * A_r / A_w.
  const tauStar = (domain, market, regime, day = market.burn_in_days) => {
    const factors = factorsFor({ ...regime, transparency: 0 }, domain, market, day);
    return 1 - Math.sqrt(domain.wash_cost_ratio) * factors.real / factors.wash;
  };

  return {
    DAYS_PER_YEAR, IMPROVE, INFLATE, MAINTAIN, MINIMUM_NPV, mulberry32, financingFactors, factorsFor, npvChoice,
    newCaseProbability, createState, advance, capacities, decide, schedule, regimeAt, simulate, windowMetrics, tauStar,
  };
});
