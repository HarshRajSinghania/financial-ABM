'use strict';
// Greenwashing policy sandbox: page logic. Model arithmetic lives in core.js (cross-checked
// against Python); this file only reads levers, calls the core and draws the results.
(() => {
  const core = globalThis.SandboxCore;
  const TEXT = globalThis.SandboxText;
  const $ = id => document.getElementById(id);
  const SVG = 'http://www.w3.org/2000/svg';
  const REPO = 'https://github.com/kanzaler123/financial-ABM';

  let payload = null;
  try { payload = JSON.parse($('sandbox-data').textContent); } catch (error) { payload = null; }
  if (!payload || !payload.firms || !core || !TEXT) { $('load-error').hidden = false; return; }
  const { firms: firmData, stage_f: stageF, simplification } = payload;
  const domains = firmData.domains;
  const F1 = domains.esg.baseline_policy.fixed_fine;     // CNY 10 m in model money units
  const YUAN_PER_UNIT = 1e7 / F1;                        // one unit = the CSI 300 mean market cap
  const BP = 1e-4;
  const SNAPSHOT_DAY = firmData.snapshot_day;
  const ACTIONS = [
    { key: 'actionImprove', color: 'var(--improve)' },
    { key: 'actionWash', color: 'var(--wash)' },
    { key: 'actionMaintain', color: 'var(--neutral)' },
  ];
  const SIZES = ['sizeLarge', 'sizeMid', 'sizeSmall'];

  // -- language ------------------------------------------------------------------------
  const query = new URLSearchParams(location.search);
  const storage = { get: () => { try { return localStorage.getItem('abm-lang'); } catch (e) { return null; } },
    set: value => { try { localStorage.setItem('abm-lang', value); } catch (e) { /* file:// may refuse */ } } };
  let lang = ['zh', 'en'].includes(query.get('lang')) ? query.get('lang') : storage.get() === 'en' ? 'en' : 'zh';
  const t = (key, vars = {}) => String(TEXT[lang][key] ?? TEXT.zh[key] ?? key)
    .replace(/\{(\w+)\}/g, (_, name) => (name in vars ? String(vars[name]) : `{${name}}`));
  const minus = s => s.replace('-', '−');
  const fixed = (x, d) => minus(Number(x).toFixed(d));
  const signed = (x, d = 3) => (x > 0 ? '+' : x < 0 ? '−' : '±') + Math.abs(x).toFixed(d);
  const pct = (x, d = 1) => `${(100 * x).toFixed(d)}%`;
  const grouped = x => Math.round(x).toLocaleString(lang === 'zh' ? 'zh-CN' : 'en-US');
  const wan = v => { const a = Math.abs(v); return a >= 100 ? fixed(v, 0) : a >= 10 ? fixed(v, 1) : a >= 0.01 || a === 0 ? fixed(v, 2) : minus(v.toPrecision(2)); };
  const sci = p => {
    if (p >= 1e-3) return p.toFixed(3);
    const exponent = Math.floor(Math.log10(p));
    const digits = { '-': '⁻', 0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹' };
    return `${(p / 10 ** exponent).toFixed(0)}×10${String(exponent).replace(/./g, c => digits[c])}`;
  };

  // -- small DOM and SVG helpers -------------------------------------------------------------
  const node = (tag, className, text) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = String(text);
    return element;
  };
  const svgNode = (tag, attrs = {}, parent = null, text) => {
    const element = document.createElementNS(SVG, tag);
    for (const [name, value] of Object.entries(attrs)) element.setAttribute(name, String(value));
    if (text !== undefined) element.textContent = String(text);
    if (parent) parent.append(element);
    return element;
  };
  const scale = (d0, d1, r0, r1) => value => r0 + (value - d0) / (d1 - d0 || 1) * (r1 - r0);
  const niceStep = (span, count) => {
    const raw = span / Math.max(count, 1);
    const magnitude = 10 ** Math.floor(Math.log10(raw || 1));
    return [1, 2, 2.5, 5, 10].map(m => m * magnitude).find(step => step >= raw) ?? 10 * magnitude;
  };
  const ticks = (lo, hi, count = 5) => {
    const step = niceStep(hi - lo, count);
    const start = Math.ceil(lo / step - 1e-9) * step;
    const values = [];
    for (let v = start; v <= hi + step * 1e-9; v += step) values.push(Math.abs(v) < step * 1e-9 ? 0 : v);
    return { values, step };
  };
  const decimals = step => Math.max(0, -Math.floor(Math.log10(step) + 1e-9));
  const frame = (container, width, height, margin) => {
    container.replaceChildren();
    const svg = svgNode('svg', { viewBox: `0 0 ${width} ${height}`, role: 'img' }, container);
    return { svg, left: margin[3], right: width - margin[1], top: margin[0], bottom: height - margin[2], width, height };
  };
  const yAxis = (f, y, lo, hi, count, format) => {
    const grid = svgNode('g', { class: 'grid' }, f.svg);
    const { values, step } = ticks(lo, hi, count);
    for (const v of values) {
      svgNode('line', { x1: f.left, x2: f.right, y1: y(v), y2: y(v) }, grid);
      svgNode('text', { x: f.left - 8, y: y(v) + 4, 'text-anchor': 'end' }, f.svg, format ? format(v) : fixed(v, decimals(step)));
    }
  };
  const xAxis = (f, x, values, format) => {
    for (const v of values) svgNode('text', { x: x(v), y: f.bottom + 16, 'text-anchor': 'middle' }, f.svg, format(v));
    svgNode('line', { x1: f.left, x2: f.right, y1: f.bottom, y2: f.bottom, class: 'baseline' }, f.svg);
  };
  const pointer = (svg, event) => {
    const box = svg.getBoundingClientRect();
    const view = svg.viewBox.baseVal;
    return { x: (event.clientX - box.left) * view.width / box.width, y: (event.clientY - box.top) * view.height / box.height };
  };
  const legend = (container, items) => {
    container.replaceChildren();
    for (const item of items) {
      const entry = node('span');
      const key = node('i', item.line ? 'key-line' : 'key-dot');
      key.style.background = item.color;
      entry.append(key, document.createTextNode(item.label));
      container.append(entry);
    }
  };
  const table = (headers, rows, numeric = []) => {
    const element = node('table');
    const head = element.createTHead().insertRow();
    headers.forEach((label, i) => { const th = node('th', numeric.includes(i) ? 'num' : '', label); th.scope = 'col'; head.append(th); });
    const body = element.createTBody();
    for (const row of rows) {
      const tr = body.insertRow();
      row.forEach((cell, i) => {
        const td = tr.insertCell();
        if (numeric.includes(i)) td.className = 'num';
        if (cell instanceof Node) td.append(cell); else td.textContent = String(cell);
      });
    }
    const wrapper = node('div', 'table-scroll');
    wrapper.append(element);
    return wrapper;
  };

  // -- tooltip -------------------------------------------------------------------------
  const tip = $('tooltip');
  const showTip = (event, title, rows) => {
    tip.replaceChildren(node('div', 'tt-title', title));
    for (const row of rows) {
      const line = node('div', 'tt-row');
      if (row.color) { const key = node('i', 'key-line'); key.style.background = row.color; line.append(key); }
      line.append(node('strong', '', row.value), node('span', '', row.label ?? ''));
      tip.append(line);
    }
    tip.hidden = false;
    const box = tip.getBoundingClientRect();
    const x = event.clientX ?? (event.target.getBoundingClientRect().right);
    const y = event.clientY ?? (event.target.getBoundingClientRect().top);
    tip.style.left = `${Math.min(x + 14, innerWidth - box.width - 8)}px`;
    tip.style.top = `${Math.min(y + 14, innerHeight - box.height - 8)}px`;
  };
  const hideTip = () => { tip.hidden = true; };

  // -- levers ----------------------------------------------------------------------------
  const state = { domain: 'esg', levers: null, firm: null, seed: 1 };
  const domain = () => domains[state.domain];
  const baselineRegime = d => ({ ...d.baseline_policy, disclosure_delay_days: null });
  const policyLevers = d => ({ tau: d.baseline_policy.transparency, fixed: d.baseline_policy.fixed_fine / F1,
    prop: d.baseline_policy.penalty, audit: d.baseline_policy.audit_probability });
  const PRESETS = {
    B: () => ({}), I: () => ({ tau: 0.6 }), F: () => ({ fixed: 4 }), IF: () => ({ tau: 0.6, fixed: 4 }), zero: () => ({ fixed: 0, prop: 0 }),
  };
  const presetLevers = name => ({ ...policyLevers(domain()), ...PRESETS[name]() });
  const regime = () => ({ audit_probability: state.levers.audit, penalty: state.levers.prop, transparency: state.levers.tau,
    subsidy: 0, fixed_fine: state.levers.fixed * F1, disclosure_delay_days: null });
  // The proportional fine slider is logarithmic: 0, then 0.1 to 100 basis points per SD.
  const propFromPosition = k => (k <= 0 ? 0 : 1e-5 * 10 ** ((k - 1) * 3 / 89));
  const positionFromProp = p => (p <= 0 ? 0 : Math.min(90, Math.max(1, Math.round(1 + Math.log10(p / 1e-5) * 89 / 3))));
  const sameLevers = (a, b) => ['tau', 'fixed', 'prop', 'audit'].every(key => Math.abs(a[key] - b[key]) < 1e-15);

  const syncLevers = () => {
    const l = state.levers;
    $('lever-tau').value = l.tau; $('lever-fixed').value = l.fixed; $('lever-prop').value = positionFromProp(l.prop);
    $('lever-audit').value = l.audit; $('lever-decay').value = l.decay;
    $('out-tau').textContent = l.tau.toFixed(2);
    $('out-fixed').textContent = t('leverFixedValue', { x: l.fixed % 1 ? l.fixed.toFixed(1) : l.fixed.toFixed(0) });
    $('out-prop').textContent = t('leverPropValue', { x: l.prop ? Number((l.prop / BP).toPrecision(2)).toString() : '0' });
    $('out-audit').textContent = t('leverAuditValue', { x: (100 * l.audit).toFixed(1) });
    $('out-decay').textContent = t('leverDecayValue', { x: l.decay.toFixed(2) });
    const star = core.tauStar(domain(), domain().market, regime());
    const tick = $('tau-star-tick');
    tick.hidden = !(star > 0 && star < 1);
    tick.style.left = `${100 * star}%`;
    $('tau-star-note').textContent = tick.hidden ? '' : t('leverTauStar', { tau: star.toFixed(2) });
    for (const button of document.querySelectorAll('[data-preset]')) {
      button.setAttribute('aria-pressed', String(sameLevers(l, presetLevers(button.dataset.preset))));
    }
    for (const button of document.querySelectorAll('[data-domain]')) button.setAttribute('aria-pressed', String(button.dataset.domain === state.domain));
    $('ai-note').hidden = state.domain !== 'ai_washing';
  };
  const onLever = (id, apply) => $(id).addEventListener('input', event => { apply(Number(event.target.value)); update(); });
  onLever('lever-tau', v => { state.levers.tau = v; });
  onLever('lever-fixed', v => { state.levers.fixed = v; });
  onLever('lever-prop', v => { state.levers.prop = propFromPosition(v); });
  onLever('lever-audit', v => { state.levers.audit = v; });
  onLever('lever-decay', v => { state.levers.decay = v; });
  for (const button of document.querySelectorAll('[data-preset]')) {
    button.addEventListener('click', () => { state.levers = { ...presetLevers(button.dataset.preset), decay: state.levers.decay }; update(); });
  }
  for (const button of document.querySelectorAll('[data-domain]')) {
    button.addEventListener('click', () => { if (button.dataset.domain !== state.domain) setDomain(button.dataset.domain); });
  }

  // -- panel 1: one decision period ----------------------------------------------------------
  const snapshotState = d => core.createState(d.firms.goodness, d.firms.inflation, d.firms.cost_scale, d.firms.pending);
  const decideAll = (d, r) => core.decide(snapshotState(d), d.firms, d, d.market, r, SNAPSHOT_DAY);
  const capYi = (d, i) => d.firms.market_cap[i] * YUAN_PER_UNIT / 1e8;
  const toWan = (d, i, fraction) => fraction * d.firms.market_cap[i] * YUAN_PER_UNIT / 1e4;
  const agreement = {};
  const defaultFirm = d => {
    const washer = d.firms.full_model_decision.actions.findIndex((a, i) => a === core.INFLATE && d.firms.size_class[i] === 0);
    return washer >= 0 ? washer : Math.max(0, d.firms.size_class.indexOf(0));
  };
  let decision = null;

  const renderScatter = (d, choices) => {
    const container = $('scatter');
    const f = frame(container, 640, 330, [12, 16, 40, 54]);
    f.svg.setAttribute('aria-label', t('scatterTitle'));
    f.svg.setAttribute('tabindex', '0');
    const caps = d.firms.market_cap.map((_, i) => Math.log10(capYi(d, i)));
    const benefits = d.firms.benefit.map(b => b / BP);
    const xLo = Math.floor(Math.min(...caps) * 4) / 4, xHi = Math.ceil(Math.max(...caps) * 4) / 4;
    const yHi = ticks(0, Math.max(...benefits) * 1.05, 5).values.at(-1) || 1;
    const x = scale(xLo, xHi, f.left, f.right), y = scale(0, yHi, f.bottom, f.top);
    yAxis(f, y, 0, yHi, 5);
    const decades = [];
    for (let k = Math.ceil(xLo); k <= xHi; k++) decades.push(k);
    xAxis(f, x, decades, k => grouped(10 ** k));
    svgNode('text', { x: f.right, y: f.bottom + 34, 'text-anchor': 'end', class: 'axis-title' }, f.svg, t('scatterX'));
    svgNode('text', { x: f.left, y: f.top - 2, class: 'axis-title' }, f.svg, t('scatterY'));
    const points = caps.map((c, i) => ({ i, px: x(c), py: y(benefits[i]) }));
    const dots = svgNode('g', {}, f.svg);
    for (const p of points) {
      const dot = svgNode('circle', { cx: p.px, cy: p.py, r: 4.5, class: 'dot' }, dots);
      dot.style.fill = ACTIONS[choices[p.i].action].color;
    }
    const s = points[state.firm];
    svgNode('circle', { cx: s.px, cy: s.py, r: 8.5, class: 'selected-ring' }, f.svg);
    const nearest = event => {
      const at = pointer(f.svg, event);
      let best = null, distance = 24 * 24;
      for (const p of points) {
        const dd = (p.px - at.x) ** 2 + (p.py - at.y) ** 2;
        if (dd < distance) { distance = dd; best = p; }
      }
      return best;
    };
    f.svg.addEventListener('pointermove', event => {
      const p = nearest(event);
      if (!p) { hideTip(); f.svg.style.cursor = 'default'; return; }
      f.svg.style.cursor = 'pointer';
      const c = choices[p.i];
      showTip(event, t('firmOption', { id: String(p.i + 1).padStart(3, '0'), size: t(SIZES[d.firms.size_class[p.i]]), cap: grouped(capYi(d, p.i)) }), [
        { color: ACTIONS[c.action].color, value: c.action === core.MAINTAIN ? t('actionMaintain') : t('factAmount', { action: t(ACTIONS[c.action].key), x: c.amount.toFixed(3) }) },
        { value: (d.firms.benefit[p.i] / BP).toFixed(2), label: t('factBenefit') },
      ]);
    });
    f.svg.addEventListener('pointerleave', hideTip);
    f.svg.addEventListener('click', event => { const p = nearest(event); if (p) selectFirm(p.i); });
    f.svg.addEventListener('keydown', event => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      selectFirm((state.firm + (event.key === 'ArrowRight' ? 1 : -1) + points.length) % points.length);
      $('scatter').querySelector('svg').focus();
    });
  };

  const renderSizeBars = (d, choices) => {
    const container = $('size-bars');
    container.replaceChildren();
    SIZES.forEach((key, k) => {
      const members = choices.filter((_, i) => d.firms.size_class[i] === k);
      const counts = [0, 0, 0];
      for (const c of members) counts[c.action] += 1;
      const row = node('div', 'size-row');
      const bar = node('div', 'bar');
      counts.forEach((count, a) => {
        if (!count) return;
        const segment = node('span');
        segment.style.flex = String(count);
        segment.style.background = ACTIONS[a].color;
        segment.title = `${t(ACTIONS[a].key)} ${count}`;
        bar.append(segment);
      });
      row.append(node('span', '', `${t(key)} · ${members.length}`), bar,
        node('span', 'counts', counts.map((count, a) => `${t(ACTIONS[a].key)} ${count}`).filter((_, a) => counts[a] || a < 2).join(' · ')));
      container.append(row);
    });
  };

  const valueCurves = (d, i, r, factors, room, probability) => {
    const b = d.firms.benefit[i];
    const mc = d.firms.cost_scale[i] * Math.exp(d.cost_level_elasticity * d.firms.goodness[i]);
    const cap = d.max_change_per_period;
    const improveCap = Math.min(Math.max(room.improve[i], 0), cap);
    const inflateCap = Math.min(Math.max(room.inflate[i], 0), cap);
    const washCost = d.wash_cost_ratio * mc;
    const gain = Math.max(b * (1 - r.transparency) * factors.wash - r.penalty * factors.fine, 0);
    const newCase = probability ? r.fixed_fine / d.firms.market_cap[i] * probability[i] : 0;
    const improve = delta => (delta <= inflateCap
      ? b * factors.real * delta
      : b * factors.real * inflateCap + b * factors.displaced * (delta - inflateCap)) + r.subsidy * delta - mc * delta * delta;
    const wash = delta => gain * delta - washCost * delta * delta - (delta > 0 ? newCase * factors.fine : 0);
    return { improve, wash, improveCap, inflateCap, newCaseValue: newCase * factors.fine };
  };

  const renderFirm = (d, choices, factors, room, probability) => {
    const i = state.firm, c = choices[i], r = regime();
    const facts = $('firm-facts');
    facts.replaceChildren();
    const fact = (label, value) => { const item = node('div'); item.append(node('dt', '', label), node('dd', '', value)); facts.append(item); };
    fact(t('factSize'), t(SIZES[d.firms.size_class[i]]));
    fact(t('factCap'), t('factCapValue', { x: grouped(capYi(d, i)) }));
    fact(t('factBenefit'), t('factBenefitValue', { x: (d.firms.benefit[i] / BP).toFixed(2) }));
    fact(t('factCost'), d.firms.cost_scale[i].toFixed(4));
    fact(t('factGoodness'), t('factSdValue', { x: signed(d.firms.goodness[i], 2) }));
    fact(t('factInflation'), t('factSdValue', { x: d.firms.inflation[i].toFixed(2) }));
    fact(t('factChoice'), c.action === core.MAINTAIN ? t('actionMaintain') : t('factAmount', { action: t(ACTIONS[c.action].key), x: c.amount.toFixed(3) }));

    const curves = valueCurves(d, i, r, factors, room, probability);
    const container = $('npv-chart');
    const f = frame(container, 560, 250, [16, 18, 40, 58]);
    f.svg.setAttribute('aria-label', t('npvTitle'));
    const xHi = Math.max(curves.improveCap, curves.inflateCap, 0.01);
    const samples = 120;
    const series = [
      { key: 'improve', cap: curves.improveCap, fn: curves.improve, color: ACTIONS[0].color, best: c.improveAmount, label: t('npvImproveBest') },
      { key: 'wash', cap: curves.inflateCap, fn: curves.wash, color: ACTIONS[1].color, best: c.inflateAmount, label: t('npvWashBest') },
    ].map(s => ({ ...s, points: Array.from({ length: samples + 1 }, (_, k) => { const delta = s.cap * k / samples; return [delta, toWan(d, i, s.fn(delta))]; }) }));
    const values = series.flatMap(s => s.points.slice(1).map(p => p[1])).concat([0]);
    let yLo = Math.min(...values), yHi = Math.max(...values);
    if (yHi - yLo < 1e-9) { yHi = 1; yLo = -1; }
    const pad = (yHi - yLo) * 0.08;
    const yTicks = ticks(yLo - pad, yHi + pad, 5);
    yLo = Math.min(yLo - pad, yTicks.values[0]); yHi = Math.max(yHi + pad, yTicks.values.at(-1));
    const x = scale(0, xHi, f.left, f.right), y = scale(yLo, yHi, f.bottom, f.top);
    yAxis(f, y, yLo, yHi, 5, v => wan(v));
    xAxis(f, x, ticks(0, xHi, 5).values, v => v.toFixed(decimals(niceStep(xHi, 5))));
    svgNode('line', { x1: f.left, x2: f.right, y1: y(0), y2: y(0), class: 'baseline' }, f.svg);
    svgNode('text', { x: f.right, y: y(0) - 6, 'text-anchor': 'end' }, f.svg, t('npvMaintain'));
    svgNode('text', { x: f.right, y: f.bottom + 34, 'text-anchor': 'end', class: 'axis-title' }, f.svg, t('npvX'));
    svgNode('text', { x: f.left, y: f.top - 4, class: 'axis-title' }, f.svg, t('npvY'));
    for (const s of series) {
      if (s.cap <= 0) continue;
      // A fixed fine is a jump at Δ > 0: the curve starts just right of zero.
      const path = s.points.map(([delta, value], k) => `${k ? 'L' : 'M'}${x(delta).toFixed(1)},${y(k === 0 && s.key === 'wash' ? toWan(d, i, s.fn(1e-12)) : value).toFixed(1)}`).join('');
      const line = svgNode('path', { d: path, fill: 'none', 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, f.svg);
      line.style.stroke = s.color;
    }
    for (const s of series) {
      if (s.best <= 0) continue;
      const value = toWan(d, i, s.fn(s.best));
      const chosen = (s.key === 'improve' && c.action === core.IMPROVE) || (s.key === 'wash' && c.action === core.INFLATE);
      const dot = svgNode('circle', { cx: x(s.best), cy: y(value), r: chosen ? 5.5 : 4.5, class: 'dot' }, f.svg);
      dot.style.fill = s.color;
      if (chosen) svgNode('circle', { cx: x(s.best), cy: y(value), r: 9, class: 'selected-ring' }, f.svg);
      const right = x(s.best) > (f.left + f.right) / 2;
      svgNode('text', { x: x(s.best) + (right ? -12 : 12), y: y(value) - 10, 'text-anchor': right ? 'end' : 'start', class: 'label' }, f.svg,
        `${s.label} Δ=${s.best.toFixed(3)} · ${wan(value)}`);
    }
    const hit = svgNode('rect', { x: f.left, y: f.top, width: f.right - f.left, height: f.bottom - f.top, class: 'hit' }, f.svg);
    const cross = svgNode('line', { y1: f.top, y2: f.bottom, class: 'crosshair', visibility: 'hidden' }, f.svg);
    hit.addEventListener('pointermove', event => {
      const delta = Math.min(Math.max((pointer(f.svg, event).x - f.left) / (f.right - f.left) * xHi, 0), xHi);
      cross.setAttribute('x1', x(delta)); cross.setAttribute('x2', x(delta)); cross.setAttribute('visibility', 'visible');
      showTip(event, `Δ = ${delta.toFixed(3)} SD`, series.filter(s => delta <= s.cap + 1e-12 && s.cap > 0)
        .map(s => ({ color: s.color, value: wan(toWan(d, i, s.fn(delta))), label: t(s.key === 'improve' ? 'actionImprove' : 'actionWash') })));
    });
    hit.addEventListener('pointerleave', () => { cross.setAttribute('visibility', 'hidden'); hideTip(); });

    const best = { v: toWan(d, i, c.values[0]), w: toWan(d, i, c.values[1]) };
    const why = $('firm-why');
    why.replaceChildren();
    const main = c.action === core.IMPROVE ? t('whyImprove', { a: c.amount.toFixed(3), v: wan(best.v), w: wan(best.w) })
      : c.action === core.INFLATE ? t('whyWash', { a: c.amount.toFixed(3), v: wan(best.v), w: wan(best.w) }) : t('whyMaintain');
    why.append(document.createTextNode(main));
    const notes = [];
    const star = core.tauStar(d, d.market, r);
    if (r.transparency >= star && c.action !== core.INFLATE) notes.push(t('whyTau', { tau: r.transparency.toFixed(2), star: star.toFixed(2) }));
    if (r.fixed_fine > 0 && d.firms.inflation[i] > 0) notes.push(t('whyJoin'));
    else if (r.fixed_fine > 0 && curves.newCaseValue > 0) notes.push(t('whyFine', { f: wan(toWan(d, i, curves.newCaseValue)) }));
    if (curves.inflateCap < 0.05) notes.push(t('whyCap', { x: curves.inflateCap.toFixed(3) }));
    for (const note of notes) why.append(node('span', '', note));
  };

  const renderDecision = () => {
    const d = domain(), r = regime();
    const { choices, factors, room, probability } = decideAll(d, r);
    decision = { choices, factors, room, probability };
    const counts = [0, 0, 0];
    for (const c of choices) counts[c.action] += 1;
    $('decision-summary').textContent = t('p1Summary', { improve: counts[0], wash: counts[1], maintain: counts[2] });
    legend($('action-legend'), ACTIONS.map(a => ({ label: t(a.key), color: a.color })));
    legend($('npv-legend'), ACTIONS.slice(0, 2).map(a => ({ label: t(a.key), color: a.color, line: true })));
    if (!(state.domain in agreement)) {
      const base = decideAll(d, baselineRegime(d)).choices;
      const recorded = d.firms.full_model_decision;
      agreement[state.domain] = base.filter((c, i) => c.action !== recorded.actions[i]
        || Math.abs(c.amount - recorded.amounts[i]) > 1e-12 * Math.max(Math.abs(recorded.amounts[i]), 1e-300)).length;
    }
    const check = $('agreement');
    check.replaceChildren();
    const mismatches = agreement[state.domain];
    check.append(node('span', mismatches ? 'bad' : 'ok', mismatches ? '!' : '✓'),
      document.createTextNode(mismatches ? t('p1Disagreement', { n: mismatches }) : t('p1Agreement')));
    const select = $('firm-select');
    if (select.options.length !== choices.length || select.dataset.lang !== lang || select.dataset.domain !== state.domain) {
      select.replaceChildren(...choices.map((_, i) => {
        const option = node('option', '', t('firmOption', { id: String(i + 1).padStart(3, '0'), size: t(SIZES[d.firms.size_class[i]]), cap: grouped(capYi(d, i)) }));
        option.value = String(i);
        return option;
      }));
      select.dataset.lang = lang; select.dataset.domain = state.domain;
    }
    select.value = String(state.firm);
    renderScatter(d, choices);
    renderSizeBars(d, choices);
    renderFirm(d, choices, factors, room, probability);
  };
  const selectFirm = i => {
    state.firm = i;
    $('firm-select').value = String(i);
    renderScatter(domain(), decision.choices);
    renderFirm(domain(), decision.choices, decision.factors, decision.room, decision.probability);
  };
  $('firm-select').addEventListener('change', event => selectFirm(Number(event.target.value)));

  // -- panel 2: simplified dynamics ----------------------------------------------------------
  const baselineRuns = new Map();
  const simulate = (d, intervention, decay, seed) => core.simulate(d.firms, d, d.market,
    intervention ? { baseline: baselineRegime(d), intervention, start_day: d.market.burn_in_days + 1 } : { baseline: baselineRegime(d), intervention: null, start_day: 0 },
    { naturalDecay: decay, auditSeed: seed });
  const baselineRun = (d, decay, seed) => {
    const key = `${state.domain}|${decay}|${seed}`;
    if (!baselineRuns.has(key)) {
      if (baselineRuns.size > 24) baselineRuns.clear();
      baselineRuns.set(key, simulate(d, null, decay, seed));
    }
    return baselineRuns.get(key);
  };

  const lineChart = (container, series, label, format) => {
    const f = frame(container, 560, 230, [14, 16, 34, 50]);
    f.svg.setAttribute('aria-label', label);
    f.svg.setAttribute('tabindex', '0');
    const days = series[0].values.length - 1;
    const step = 5;
    const all = series.flatMap(s => Array.from(s.values));
    let lo = Math.min(...all), hi = Math.max(...all);
    const pad = (hi - lo || 1) * 0.08;
    const yT = ticks(lo - pad, hi + pad, 4);
    lo = Math.min(lo - pad, yT.values[0]); hi = Math.max(hi + pad, yT.values.at(-1));
    const x = scale(0, days, f.left, f.right), y = scale(lo, hi, f.bottom, f.top);
    yAxis(f, y, lo, hi, 4);
    const years = [];
    for (let year = 0; year * 252 <= days; year += 2) years.push(year * 252);
    xAxis(f, x, years, v => String(v / 252));
    svgNode('text', { x: f.right, y: f.bottom + 30, 'text-anchor': 'end', class: 'axis-title' }, f.svg, t('chartYears'));
    const switchDay = domain().market.burn_in_days + 1;
    svgNode('line', { x1: x(switchDay), x2: x(switchDay), y1: f.top, y2: f.bottom, class: 'annotation' }, f.svg);
    svgNode('text', { x: x(switchDay) + 6, y: f.top + 10, class: 'annotation-text' }, f.svg, t('chartSwitch'));
    for (const s of [...series].reverse()) {
      const sampled = [];
      for (let day = 0; day < days; day += step) sampled.push(day);
      sampled.push(days);
      const path = sampled.map((day, k) => `${k ? 'L' : 'M'}${x(day).toFixed(1)},${y(s.values[day]).toFixed(1)}`).join('');
      const line = svgNode('path', { d: path, fill: 'none', 'stroke-width': 2, 'stroke-linejoin': 'round' }, f.svg);
      line.style.stroke = s.color;
    }
    const end = series[0];
    svgNode('circle', { cx: x(days), cy: y(end.values[days]), r: 4, class: 'dot' }, f.svg).style.fill = end.color;
    svgNode('text', { x: x(days) - 8, y: y(end.values[days]) - 9, 'text-anchor': 'end', class: 'label' }, f.svg, format(end.values[days]));
    const cross = svgNode('line', { y1: f.top, y2: f.bottom, class: 'crosshair', visibility: 'hidden' }, f.svg);
    const hit = svgNode('rect', { x: f.left, y: f.top, width: f.right - f.left, height: f.bottom - f.top, class: 'hit' }, f.svg);
    let focusDay = days;
    const show = (event, day) => {
      cross.setAttribute('x1', x(day)); cross.setAttribute('x2', x(day)); cross.setAttribute('visibility', 'visible');
      showTip(event, `${t('chartYears')} ${(day / 252).toFixed(1)} · day ${day}`, series.map(s => ({ color: s.color, value: format(s.values[day]), label: s.label })));
    };
    hit.addEventListener('pointermove', event => {
      const day = Math.round(Math.min(Math.max((pointer(f.svg, event).x - f.left) / (f.right - f.left), 0), 1) * days);
      show(event, day);
    });
    hit.addEventListener('pointerleave', () => { cross.setAttribute('visibility', 'hidden'); hideTip(); });
    f.svg.addEventListener('keydown', event => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      focusDay = Math.min(days, Math.max(0, focusDay + (event.key === 'ArrowRight' ? 60 : -60)));
      const box = f.svg.getBoundingClientRect();
      show({ clientX: box.left + (x(focusDay) / f.width) * box.width, clientY: box.top + 20 }, focusDay);
    });
    f.svg.addEventListener('blur', () => { cross.setAttribute('visibility', 'hidden'); hideTip(); });
  };

  const renderDynamics = () => {
    const d = domain(), decay = state.levers.decay, seed = state.seed;
    const run = simulate(d, regime(), decay, seed);
    const base = baselineRun(d, decay, seed);
    const start = d.market.burn_in_days, end = d.market.trading_days;
    const m = core.windowMetrics(run, d.firms, start, end), mb = core.windowMetrics(base, d.firms, start, end);
    const tiles = $('dynamics-tiles');
    tiles.replaceChildren();
    const tile = (label, value, sub) => {
      const item = node('div', 'tile');
      item.append(node('p', 'tile-label', label), node('p', 'tile-value', value), node('p', 'tile-sub', sub));
      tiles.append(item);
    };
    tile(t('tileChange'), `${signed(m.true_change_sd, 2)} SD`,
      `${t('tileVsBase', { x: signed(mb.true_change_sd, 2) })} · ${t('tileDelta', { x: signed(m.true_change_sd - mb.true_change_sd, 3) })}`);
    tile(t('tileWash'), pct(m.wash_share), t('tileVsBase', { x: pct(mb.wash_share) }));
    tile(t('tileInflation'), `${m.inflation_mean_sd.toFixed(2)} SD`, t('tileVsBase', { x: mb.inflation_mean_sd.toFixed(2) }));
    const policy = { label: t('legendPolicy'), color: 'var(--improve)' }, baseline = { label: t('legendBaseline'), color: 'var(--neutral)' };
    legend($('dynamics-legend'), [{ ...policy, line: true }, { ...baseline, line: true }]);
    lineChart($('chart-goodness'), [{ ...policy, values: run.meanGoodness }, { ...baseline, values: base.meanGoodness }], t('chartGoodness'), v => signed(v, 2));
    lineChart($('chart-inflation'), [{ ...policy, values: run.meanInflation }, { ...baseline, values: base.meanInflation }], t('chartInflation'), v => v.toFixed(2));
    const rows = [];
    for (let year = 0; year * 252 <= end; year++) {
      const day = year * 252;
      rows.push([year, signed(run.meanGoodness[day], 3), signed(base.meanGoodness[day], 3), run.meanInflation[day].toFixed(3), base.meanInflation[day].toFixed(3)]);
    }
    rows.push([(end / 252).toFixed(1), signed(run.meanGoodness[end], 3), signed(base.meanGoodness[end], 3), run.meanInflation[end].toFixed(3), base.meanInflation[end].toFixed(3)]);
    $('dynamics-table').replaceChildren(table([t('tableYear'), `${t('chartGoodness')} · ${policy.label}`, baseline.label,
      `${t('chartInflation')} · ${policy.label}`, baseline.label], rows, [1, 2, 3, 4]));
  };
  $('audit-seed').addEventListener('change', event => {
    const value = Math.floor(Number(event.target.value));
    state.seed = Number.isFinite(value) && value >= 1 && value <= 4294967295 ? value : 1;
    event.target.value = state.seed;
    update();
  });
  $('seed-next').addEventListener('click', () => { state.seed = state.seed % 4294967295 + 1; $('audit-seed').value = state.seed; update(); });

  const renderCost = () => {
    const container = $('cost-tables');
    container.replaceChildren();
    const range = s => { const cell = node('span', '', signed(s.mean, 3)); cell.append(node('span', 'range', `${signed(s.min, 3)} … ${signed(s.max, 3)}`)); return cell; };
    const rows = Object.values(simplification.rows).map(row => [
      row.natural_decay.toString(), row.policy, range(row.simplified.true_change_sd), signed(row.full_same_seed.true_change_sd, 3),
      signed(row.stage_f_mean.true_change_sd, 3), pct(row.simplified.wash_share.mean), pct(row.full_same_seed.wash_share), pct(row.stage_f_mean.wash_share),
    ]);
    container.append(table([t('costDecay'), t('costScenario'), `${t('costMetric')} · ${t('costSimplified')}`, t('costFull'), t('costStageF'),
      `${t('costWash')} · ${t('costSimplified')}`, t('costFull'), t('costStageF')], rows, [2, 3, 4, 5, 6, 7]));
    const contrasts = Object.values(simplification.contrasts).map(row => [
      row.natural_decay.toString(), row.contrast.replace('_minus_', ' − '), range(row.simplified), signed(row.full_same_seed, 3),
      `${signed(row.stage_f.mean, 3)} [${signed(row.stage_f.ci_low, 3)}, ${signed(row.stage_f.ci_high, 3)}]`,
    ]);
    container.append(table([t('costDecay'), t('costContrast'), t('costSimplified'), t('costFull'), t('costStageF')], contrasts, [2, 3, 4]));
  };

  // -- panel 3: stage F results --------------------------------------------------------------
  const primary = name => stageF.primary.find(row => row.name === name);
  const bracketRows = () => [
    { key: 'contrastIB', low: stageF.secondary.decay0_I_minus_B, high: stageF.secondary.I_minus_B },
    { key: 'contrastFB', low: stageF.secondary.decay0_F_minus_B, high: stageF.secondary.F_minus_B },
    { key: 'contrastIF', low: stageF.secondary.decay0_I_minus_F, high: primary('P2_I_minus_F') },
  ];
  const ends = [{ key: 'bracketLow', field: 'low', color: 'var(--mixed)' }, { key: 'bracketHigh', field: 'high', color: 'var(--improve)' }];

  const renderBracket = () => {
    const rows = bracketRows();
    legend($('bracket-legend'), ends.map(e => ({ label: t(e.key), color: e.color })));
    const f = frame($('bracket-chart'), 600, 64 + rows.length * 62, [10, 26, 34, 180]);
    f.svg.setAttribute('aria-label', t('bracketTitle'));
    const hi = Math.max(...rows.map(r => r.high.ci_high)) * 1.12;
    const x = scale(0, hi, f.left, f.right);
    const grid = svgNode('g', { class: 'grid' }, f.svg);
    const xt = ticks(0, hi, 5);
    for (const v of xt.values) {
      svgNode('line', { x1: x(v), x2: x(v), y1: f.top, y2: f.bottom }, grid);
      svgNode('text', { x: x(v), y: f.bottom + 16, 'text-anchor': 'middle' }, f.svg, v.toFixed(decimals(xt.step)));
    }
    svgNode('line', { x1: x(0), x2: x(0), y1: f.top, y2: f.bottom, class: 'baseline' }, f.svg);
    svgNode('text', { x: f.right, y: f.bottom + 32, 'text-anchor': 'end', class: 'axis-title' }, f.svg, 'SD');
    rows.forEach((row, k) => {
      const cy = f.top + 30 + k * 62;
      svgNode('text', { x: 8, y: cy + 4, class: 'label' }, f.svg, t(row.key));
      svgNode('line', { x1: x(row.low.mean), x2: x(row.high.mean), y1: cy, y2: cy, 'stroke-width': 2 }, f.svg).style.stroke = 'var(--axis)';
      for (const e of ends) {
        const v = row[e.field];
        svgNode('line', { x1: x(v.ci_low), x2: x(v.ci_high), y1: cy, y2: cy, 'stroke-width': 1.5 }, f.svg).style.stroke = e.color;
        for (const edge of [v.ci_low, v.ci_high]) svgNode('line', { x1: x(edge), x2: x(edge), y1: cy - 5, y2: cy + 5, 'stroke-width': 1.5 }, f.svg).style.stroke = e.color;
        const dot = svgNode('circle', { cx: x(v.mean), cy, r: 5, class: 'dot' }, f.svg);
        dot.style.fill = e.color;
        svgNode('text', { x: x(v.mean), y: cy + (e.field === 'low' ? 22 : -12), 'text-anchor': 'middle', class: 'label' }, f.svg, signed(v.mean, 3));
        const hit = svgNode('circle', { cx: x(v.mean), cy, r: 13, class: 'hit' }, f.svg);
        const tipRows = () => [{ color: e.color, value: `${signed(v.mean, 3)} [${signed(v.ci_low, 3)}, ${signed(v.ci_high, 3)}]`, label: t(e.key) }];
        hit.addEventListener('pointermove', event => showTip(event, t(row.key), tipRows()));
        hit.addEventListener('pointerleave', hideTip);
      }
    });
    $('bracket-table').replaceChildren(table([t('costContrast'), t('bracketLow'), t('bracketHigh')], rows.map(row => [t(row.key),
      ...ends.map(e => `${signed(row[e.field].mean, 3)} [${signed(row[e.field].ci_low, 3)}, ${signed(row[e.field].ci_high, 3)}]`)]), [1, 2]));
  };

  const renderPrimary = () => {
    $('primary-table').replaceChildren(table([t('primaryQuestion'), t('primaryEstimate'), t('primaryHolm')], stageF.primary.map(row => [
      t(row.name), `${signed(row.mean, 3)} [${signed(row.ci_low, 3)}, ${signed(row.ci_high, 3)}]`, sci(row.holm_p_value),
    ]), [1, 2]));
  };

  const doseChart = (container, title, points, yLabel) => {
    container.replaceChildren(node('h4', '', title));
    const holder = node('div', 'chart');
    container.append(holder);
    const f = frame(holder, 360, 200, [16, 14, 34, 46]);
    f.svg.setAttribute('aria-label', title);
    const xs = points.map(p => p.x), ys = points.flatMap(p => [p.lo ?? p.y, p.hi ?? p.y, 0]);
    const xLo = Math.min(...xs), xHi = Math.max(...xs);
    let yLo = Math.min(...ys), yHi = Math.max(...ys);
    const pad = (yHi - yLo) * 0.12;
    yLo -= pad; yHi += pad;
    const yT = ticks(yLo, yHi, 4);
    const xPad = (xHi - xLo) * 0.06;
    const x = scale(xLo - xPad, xHi + xPad, f.left, f.right), y = scale(yLo, yHi, f.bottom, f.top);
    yAxis(f, y, yLo, yHi, 4, v => v.toFixed(decimals(yT.step)));
    xAxis(f, x, xs, v => points.find(p => p.x === v).label);
    svgNode('line', { x1: f.left, x2: f.right, y1: y(0), y2: y(0), class: 'baseline' }, f.svg);
    svgNode('text', { x: f.left, y: f.top - 4, class: 'axis-title' }, f.svg, yLabel);
    const path = points.map((p, k) => `${k ? 'L' : 'M'}${x(p.x).toFixed(1)},${y(p.y).toFixed(1)}`).join('');
    svgNode('path', { d: path, fill: 'none', 'stroke-width': 2 }, f.svg).style.stroke = 'var(--improve)';
    for (const p of points) {
      if (p.lo !== undefined) svgNode('line', { x1: x(p.x), x2: x(p.x), y1: y(p.lo), y2: y(p.hi), 'stroke-width': 1.5 }, f.svg).style.stroke = 'var(--improve)';
      svgNode('circle', { cx: x(p.x), cy: y(p.y), r: 4.5, class: 'dot' }, f.svg).style.fill = 'var(--improve)';
      const hit = svgNode('circle', { cx: x(p.x), cy: y(p.y), r: 13, class: 'hit' }, f.svg);
      hit.addEventListener('pointermove', event => showTip(event, `${title}: ${p.label}`, [
        { color: 'var(--improve)', value: `${signed(p.y, 3)}${p.lo !== undefined ? ` [${signed(p.lo, 3)}, ${signed(p.hi, 3)}]` : ''}`, label: 'SD' },
        { value: pct(p.wash), label: t('doseWash') }]));
      hit.addEventListener('pointerleave', hideTip);
    }
    container.append(table([title, 'SD', t('doseWash')], points.map(p => [p.label, signed(p.y, 3), pct(p.wash)]), [1, 2]));
  };

  const renderDose = () => {
    const s = stageF.secondary, sc = stageF.scenarios;
    const ci = row => ({ y: row.mean, lo: row.ci_low, hi: row.ci_high });
    const grid = $('dose-grid');
    grid.replaceChildren();
    const cells = [node('div'), node('div'), node('div')];
    grid.append(...cells);
    doseChart(cells[0], t('doseTau'), [
      { x: 0.1, label: '0.1', y: 0, wash: sc.B.wash },
      ...[['0.3', 'I_0p3'], ['0.5', 'I_0p5'], ['0.6', 'I'], ['0.7', 'I_0p7'], ['0.8', 'I_0p8']].map(([label, name]) => ({
        x: Number(label), label, ...ci(s[`${name}_minus_B`]), wash: sc[name].wash })),
    ], t('doseY'));
    doseChart(cells[1], t('doseFixed'), [
      { x: 0, label: '0×', ...ci(s.F_0x_minus_B), wash: sc.F_0x.wash }, { x: 1, label: '1×', y: 0, wash: sc.B.wash },
      { x: 2, label: '2×', ...ci(s.F_2x_minus_B), wash: sc.F_2x.wash }, { x: 4, label: '4×', ...ci(s.F_minus_B), wash: sc.F.wash },
      { x: 8, label: '8×', ...ci(s.F_8x_minus_B), wash: sc.F_8x.wash },
    ], t('doseY'));
    doseChart(cells[2], t('doseProp'), [1, 2, 4].map(k => ({ x: k, label: `${k}×`, ...ci(s[`P_${k}x_minus_fixed_${k}x`]), wash: sc[`P_${k}x`].wash })), t('doseYProp'));
  };

  const CLASS = {
    real_improvement: ['classReal', 'class-real'], washing_trap: ['classTrap', 'class-trap'], low_low: ['classLow', 'class-low'],
    mixed: ['classMixed', 'class-mixed'], uncertain: ['classUncertain', 'class-uncertain'],
  };
  const phaseTable = (rowsLabel, colsLabel, rowValues, colValues, cell) => {
    const element = node('table', 'phase-table');
    const head = element.createTHead().insertRow();
    const corner = node('th', '', `${rowsLabel} \\ ${colsLabel}`);
    head.append(corner);
    for (const c of colValues) { const th = node('th', '', String(c)); th.scope = 'col'; head.append(th); }
    const body = element.createTBody();
    for (const r of rowValues) {
      const tr = body.insertRow();
      const th = node('th', '', String(r)); th.scope = 'row'; tr.append(th);
      for (const c of colValues) tr.append(cell(r, c));
    }
    return element;
  };
  const renderPhase = () => {
    const star = Object.fromEntries(stageF.tau_star_check.map(row => [`${row.w}|${row.tau}`, row]));
    $('phase2').replaceChildren(phaseTable(t('phaseW'), t('phaseTau'), [0.05, 0.1, 0.2, 0.4], [0.1, 0.3, 0.6, 0.8], (w, tau) => {
      const entry = stageF.phase_map_2[`${w}|${tau}`];
      const check = star[`${w}|${tau}`];
      const dominant = entry.decay_adjusted.dominant;
      const td = node('td', CLASS[dominant][1], t(CLASS[dominant][0]));
      const previous = [0.1, 0.3, 0.6, 0.8][[0.1, 0.3, 0.6, 0.8].indexOf(tau) - 1];
      if (!check.predicted_washing && (previous === undefined || star[`${w}|${previous}`].predicted_washing)) td.classList.add('threshold');
      const correct = (check.wash_share > 0) === check.predicted_washing;
      td.append(node('small', '', `${pct(check.wash_share)} · ${t(check.predicted_washing ? 'predictedYes' : 'predictedNo')} ${correct ? '✓' : '✗'}`));
      td.title = `τ*(${w}) = ${check.tau_star.toFixed(2)}`;
      return td;
    }));
    // Keys as written by the stage F analysis: taste|initial share.
    $('phase1').replaceChildren(phaseTable(t('phaseTaste'), t('phaseShare'), ['0.0', '0.0362', '0.0724', '0.1448'], ['0.0', '0.2', '0.5', '0.8'], (taste, share) => {
      const entry = stageF.phase_map_1[`${taste}|${share}`];
      const dominant = entry.decay_adjusted.dominant;
      const td = node('td', CLASS[dominant][1], t(CLASS[dominant][0]));
      const counts = entry.decay_adjusted.counts;
      td.append(node('small', '', `${counts.real_improvement}/${counts.washing_trap}/${counts.low_low}/${counts.mixed}`));
      return td;
    }));
  };

  const renderProvenance = () => {
    const source = stageF.source;
    const list = $('provenance');
    list.replaceChildren();
    const fact = (label, value, href) => {
      const item = node('div');
      const dd = node('dd');
      if (href) { const link = node('a', '', value); link.href = href; dd.append(link); } else dd.textContent = value;
      item.append(node('dt', '', label), dd);
      list.append(item);
    };
    fact(t('provExperiment'), `experiment_id ${source.experiment_id.slice(0, 12)}…${source.experiment_id.slice(-4)}`);
    fact(t('provRuns'), t('provRunsValue', { runs: source.runs, planned: source.planned, seeds: source.seeds }));
    fact(t('provCommit'), source.commit.slice(0, 7));
    fact(t('provFile'), `${source.path} · sha256 ${source.sha256.slice(0, 12)}…`, `${REPO}/blob/master/${source.path}`);
    fact(t('provReport'), source.report, `${REPO}/blob/master/${source.report}`);
    fact(t('provContract'), 'docs/disclosure_research_contract.md §20', `${REPO}/blob/master/docs/disclosure_research_contract.md`);
  };

  const renderResults = () => {
    const ai = state.domain === 'ai_washing';
    $('results-ai').hidden = !ai;
    $('results-body').hidden = ai;
    if (ai) return;
    renderBracket(); renderPrimary(); renderDose(); renderPhase(); renderProvenance();
  };

  // -- page text and orchestration -------------------------------------------------------------
  const renderHero = () => {
    const w02 = stageF.tau_star_check.find(row => row.w === 0.2);
    $('finding2-value').textContent = t('finding2Value', { tau: w02.tau_star.toFixed(2) });
    $('finding3-value').textContent = t('finding3Value', {
      lo: stageF.secondary.decay0_I_minus_B.mean.toFixed(2), hi: stageF.secondary.I_minus_B.mean.toFixed(2) });
  };
  const applyText = () => {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.title = t('pageTitle');
    for (const element of document.querySelectorAll('[data-i18n]')) element.textContent = t(element.dataset.i18n);
    for (const element of document.querySelectorAll('[data-i18n-aria]')) element.setAttribute('aria-label', t(element.dataset.i18nAria));
    // Carry the language to the stage 1 exhibit, which shares the 'abm-lang' preference.
    for (const element of document.querySelectorAll('[data-lang-link]')) element.setAttribute('href', `${element.dataset.langLink}?lang=${lang}`);
    $('lang-toggle').setAttribute('lang', lang === 'zh' ? 'en' : 'zh');
    renderHero();
  };
  // Coalesce slider events into one render per frame; the timer covers hidden tabs, where
  // animation frames do not fire.
  let pending = false;
  const flush = () => {
    if (!pending) return;
    pending = false;
    renderDecision();
    renderDynamics();
  };
  const update = () => {
    syncLevers();
    if (pending) return;
    pending = true;
    requestAnimationFrame(flush);
    setTimeout(flush, 120);
  };
  const setDomain = key => {
    state.domain = key;
    const d = domain();
    state.levers = { ...policyLevers(d), decay: d.natural_decay };
    state.firm = defaultFirm(d);
    renderResults();
    update();
  };
  $('lang-toggle').addEventListener('click', () => {
    lang = lang === 'zh' ? 'en' : 'zh';
    storage.set(lang);
    applyText(); renderCost(); renderResults(); update();
  });
  document.querySelectorAll('.segmented').forEach(group => group.addEventListener('keydown', event => {
    if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
    const buttons = [...group.querySelectorAll('button')];
    const i = buttons.indexOf(document.activeElement);
    if (i < 0) return;
    event.preventDefault();
    buttons[(i + (event.key === 'ArrowRight' ? 1 : -1) + buttons.length) % buttons.length].focus();
  }));
  addEventListener('scroll', hideTip, { passive: true });

  applyText();
  renderCost();
  setDomain('esg');
})();
