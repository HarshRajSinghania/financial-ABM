'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const repo = 'https://github.com/kanzaler123/financial-ABM';
  const TEXT = globalThis.ExhibitText;
  // The language choice is shared with the sandbox home page.
  const query = new URLSearchParams(location.search);
  const storage = {
    get: () => { try { return localStorage.getItem('abm-lang'); } catch { return null; } },
    set: value => { try { localStorage.setItem('abm-lang', value); } catch { /* file:// may refuse */ } },
  };
  let lang = ['zh', 'en'].includes(query.get('lang')) ? query.get('lang') : storage.get() === 'zh' ? 'zh' : 'en';
  const t = (key, vars = {}) => String(TEXT[lang][key] ?? TEXT.zh[key] ?? key)
    .replace(/\{(\w+)\}/g, (_, name) => (name in vars ? String(vars[name]) : `{${name}}`));
  const known = key => key in TEXT.zh;
  const txt = (id, value) => { $(id).textContent = String(value); };
  const node = (tag, className, text) => {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = String(text);
    return el;
  };
  const fmt = (v, percent = false) => Number.isFinite(v)
    ? percent ? `${(v * 100).toFixed(2)}%` : v.toFixed(3)
    : t('notRecorded');
  const applyText = () => {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.title = t('pageTitle');
    document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t(el.dataset.i18n); });
    document.querySelectorAll('[data-i18n-aria]').forEach(el => el.setAttribute('aria-label', t(el.dataset.i18nAria)));
    // Mixed content (text plus an icon or tag): only the first text node is translated.
    document.querySelectorAll('[data-i18n-text]').forEach(el => {
      const text = [...el.childNodes].find(n => n.nodeType === Node.TEXT_NODE && n.nodeValue.trim());
      if (!text) return;
      const [, lead, , tail] = text.nodeValue.match(/^(\s*)([\s\S]*?)(\s*)$/);
      text.nodeValue = lead + t(el.dataset.i18nText) + tail;
    });
    document.querySelectorAll('[data-lang-link]').forEach(el => el.setAttribute('href', `${el.dataset.langLink}?lang=${lang}`));
    $('lang-toggle').setAttribute('lang', lang === 'zh' ? 'en' : 'zh');
  };
  applyText();

  const stepFiles = ['harness.py', 'policies.py', 'policies.py', 'microstructure.py', 'settlement.py', 'harness.py'];
  let selectedStep = 0;
  const renderStep = () => {
    txt('step-number', String(selectedStep + 1).padStart(2, '0'));
    txt('step-title', t(`step${selectedStep + 1}Title`)); txt('step-description', t(`step${selectedStep + 1}Text`));
    $('step-source').href = `${repo}/blob/master/src/abm/${stepFiles[selectedStep]}`;
  };
  document.querySelectorAll('[data-step]').forEach(button => button.addEventListener('click', () => {
    selectedStep = Number(button.dataset.step);
    document.querySelectorAll('[data-step]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    renderStep();
  }));
  document.querySelectorAll('.pipeline, .segmented').forEach(group => group.addEventListener('keydown', event => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    const buttons = [...group.querySelectorAll('button')];
    const i = buttons.indexOf(document.activeElement);
    if (i < 0) return;
    event.preventDefault();
    const j = event.key === 'Home' ? 0 : event.key === 'End' ? buttons.length - 1
      : (i + (event.key === 'ArrowRight' ? 1 : -1) + buttons.length) % buttons.length;
    buttons[j].focus(); buttons[j].click();
  }));
  // Decorative topology only: these are not sampled agents or telemetry.
  const svgNS = 'http://www.w3.org/2000/svg';
  const colors = ['#c6f590', '#75d8df', '#bca5eb'];
  for (let i = 0; i < 48; i++) {
    const a = i * 2.3999632297, r = 97 + (i % 9) * 12;
    const x = 280 + Math.cos(a) * r * 1.06, y = 247 + Math.sin(a) * r * .88;
    if (i % 3 === 0) {
      const line = document.createElementNS(svgNS, 'line');
      for (const [k, v] of Object.entries({x1:280, y1:247, x2:x, y2:y, stroke:colors[i % 3], 'stroke-opacity':.13})) line.setAttribute(k, String(v));
      $('field').append(line);
    }
    const dot = document.createElementNS(svgNS, 'circle');
    for (const [k, v] of Object.entries({cx:x, cy:y, r:i % 6 === 0 ? 3.5 : 2, fill:colors[i % 3], class:'field-dot'})) dot.setAttribute(k, String(v));
    dot.style.animationDelay = `${-(i % 7)}s`;
    $('field').append(dot);
  }
  const motion = $('motion-toggle');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const syncMotion = () => {
    if (reduced.matches) { document.body.classList.add('motion-paused'); motion.disabled = true; motion.textContent = t('motionReduced'); motion.setAttribute('aria-pressed', 'true'); }
    else { motion.disabled = false; motion.textContent = document.body.classList.contains('motion-paused') ? t('motionResume') : t('motionPause'); }
  };
  syncMotion(); reduced.addEventListener('change', syncMotion);
  motion.addEventListener('click', () => {
    const paused = document.body.classList.toggle('motion-paused');
    motion.setAttribute('aria-pressed', String(paused)); motion.textContent = paused ? t('motionResume') : t('motionPause');
  });
  $('copy-command').addEventListener('click', async () => {
    try {
      if (!navigator.clipboard) throw new Error('clipboard unavailable');
      await navigator.clipboard.writeText($('preview-command').textContent);
      txt('copy-feedback', t('copyDone'));
    } catch {
      const range = document.createRange(); range.selectNodeContents($('preview-command'));
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      txt('copy-feedback', t('copySelected'));
    }
  });
  // Metric keys and whether each is a percentage; labels and notes live in i18n.js.
  const percentMetrics = {
    daily_volatility: true, absolute_return_acf_1: false, excess_kurtosis: false, mean_absolute_log_price_gap: false,
  };
  const scenarioOrder = [
    'full', 'no_direct_news', 'no_agent_information', 'no_information_channels', 'value_only', 'trend_only', 'noise_only',
    'no_logit', 'no_activity_persistence', 'independent_signals', 'fixed_participation', 'fixed_liquidity',
    'liquidity_stress', 'concentrated_wealth', 'garch_t_control', 'logit_learning',
  ];
  const scenarioName = key => (known(`scenario_${key}`) ? t(`scenario_${key}`) : key);
  const scenarioNote = key => (known(`scenarioNote_${key}`) ? t(`scenarioNote_${key}`) : '');
  const checkName = key => (known(`check_${key}`) ? t(`check_${key}`) : key);
  const checkNote = key => (known(`checkNote_${key}`) ? t(`checkNote_${key}`) : t('checkMissing'));
  let snapshot, current, selectedScenario = 'full', selectedGate = null, loaded = false;
  $('lang-toggle').addEventListener('click', () => {
    lang = lang === 'zh' ? 'en' : 'zh';
    storage.set(lang);
    applyText(); renderStep(); syncMotion(); txt('copy-feedback', '');
    if (loaded) renderReport();
  });
  renderStep();
  try {
    snapshot = JSON.parse($('showcase-data').textContent);
    if (!Array.isArray(snapshot.reports) || snapshot.reports.length !== 3) throw new Error('missing reports');
    current = snapshot.reports.find(r => r.id === 'formal');
    if (!current) throw new Error('missing formal report');
  } catch (error) {
    $('load-error').hidden = false;
    document.querySelectorAll('[data-report], #metric-select, #failed-only, #download-data').forEach(e => { e.disabled = true; });
    return;
  }
  function fact(parent, label, value) {
    const row = node('div', 'gate-fact'); row.append(node('span', '', label), node('b', '', value)); parent.append(row);
  }
  function sourceUrl(name) { return `${repo}/blob/${snapshot.source_commit}/${current.path}/${name}`; }
  function renderScenarioDetail() {
    const key = $('metric-select').value, percent = percentMetrics[key];
    const stats = current.summary[selectedScenario][key];
    const detail = $('scenario-detail'); detail.replaceChildren();
    detail.append(node('strong', '', `${scenarioName(selectedScenario)} / ${t(`metric_${key}`)}`));
    detail.append(node('div', '', t('scenarioDetail', {
      desc: scenarioNote(selectedScenario), median: fmt(stats.median, percent), q10: fmt(stats.q10, percent), q90: fmt(stats.q90, percent),
    })));
  }
  function renderChart() {
    const key = $('metric-select').value, percent = percentMetrics[key];
    txt('metric-explanation', t(`metricNote_${key}`));
    const rows = scenarioOrder.filter(s => current.summary[s]);
    const min = Math.min(0, ...rows.map(s => current.summary[s][key].q10));
    const max = Math.max(0, ...rows.map(s => current.summary[s][key].q90));
    const width = max - min || 1;
    const pos = v => Math.max(0, Math.min(100, (v - min) / width * 100));
    txt('scale-min', fmt(min, percent)); txt('scale-max', fmt(max, percent));
    const chart = $('scenario-chart'); chart.replaceChildren();
    for (const name of rows) {
      const stats = current.summary[name][key];
      const row = node('button', `scenario-row${name === 'garch_t_control' ? ' exogenous' : ''}`);
      row.type = 'button'; row.dataset.scenario = name;
      row.setAttribute('aria-pressed', String(name === selectedScenario));
      row.setAttribute('aria-label', t('scenarioAria', {
        name: scenarioName(name), median: fmt(stats.median, percent), q10: fmt(stats.q10, percent), q90: fmt(stats.q90, percent),
      }));
      const distribution = node('span', 'distribution'); distribution.setAttribute('aria-hidden', 'true');
      const interval = node('span', 'interval'); interval.style.left = `${pos(stats.q10)}%`; interval.style.width = `${pos(stats.q90) - pos(stats.q10)}%`;
      const median = node('span', 'median'); median.style.left = `${pos(stats.median)}%`;
      if (min < 0 && max > 0) { const zero = node('span', 'zero'); zero.style.left = `${pos(0)}%`; distribution.append(zero); }
      distribution.append(interval, median);
      row.append(node('span', 'scenario-name', scenarioName(name)), distribution, node('span', 'numeric', fmt(stats.median, percent)));
      row.addEventListener('click', () => {
        selectedScenario = name;
        chart.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === row)));
        renderScenarioDetail();
      });
      chart.append(row);
    }
    renderScenarioDetail();
  }
  function renderGateDetail() {
    if (!selectedGate) return;
    const passed = current.checks[selectedGate];
    txt('gate-detail-label', passed ? 'CHECK / PASSED' : 'CHECK / NOT PASSED');
    txt('gate-title', checkName(selectedGate)); txt('gate-key', selectedGate); txt('gate-description', checkNote(selectedGate));
    const facts = $('gate-facts'); facts.replaceChildren();
    const evidence = current.evidence[selectedGate];
    if (evidence) {
      if (Number.isFinite(evidence.pass_rate)) fact(facts, t('factPassRate'), `${(evidence.pass_rate * 100).toFixed(0)}%`);
      if (evidence.observed !== undefined) fact(facts, t('factObserved'), typeof evidence.observed === 'number' ? fmt(evidence.observed) : JSON.stringify(evidence.observed));
      if (evidence.threshold !== undefined) fact(facts, t('factThreshold'), JSON.stringify(evidence.threshold));
      if (Array.isArray(evidence.failed_seeds)) fact(facts, t('factFailedSeeds'), String(evidence.failed_seeds.length));
    } else {
      fact(facts, t('factRawResult'), passed ? 'PASS' : 'FAIL');
      facts.append(node('p', '', t('evidenceMissing')));
    }
    $('gate-source').href = sourceUrl('mechanism_report.json');
  }
  function renderGates() {
    const entries = Object.entries(current.checks);
    const filtered = entries.filter(([, passed]) => !$('failed-only').checked || !passed);
    if (!filtered.some(([key]) => key === selectedGate)) selectedGate = filtered.find(([, passed]) => !passed)?.[0] || filtered[0]?.[0] || null;
    const matrix = $('gate-matrix'); matrix.replaceChildren();
    filtered.forEach(([key, passed]) => {
      const b = node('button', passed ? '' : 'failed'); b.type = 'button';
      b.append(node('span', '', String(entries.findIndex(([k]) => k === key) + 1).padStart(2, '0')), node('span', 'check-symbol', passed ? '✓' : '×'));
      b.setAttribute('aria-label', t('gateAria', { name: checkName(key), status: t(passed ? 'passed' : 'notPassed') }));
      b.setAttribute('aria-pressed', String(key === selectedGate)); b.title = checkName(key);
      b.addEventListener('click', () => { selectedGate = key; matrix.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b))); renderGateDetail(); });
      matrix.append(b);
    });
    $('gate-empty').hidden = filtered.length !== 0;
    document.querySelector('.gate-detail').hidden = !selectedGate;
    renderGateDetail();
  }
  function renderReport() {
    const passed = Object.values(current.checks).filter(Boolean).length, total = Object.keys(current.checks).length;
    const failed = total - passed;
    document.querySelectorAll('[data-report]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.report === current.id)));
    txt('kpi-gates', `${passed} / ${total}`);
    txt('kpi-decision', current.id === 'formal' ? t(failed ? 'decisionFormalFail' : 'decisionFormalPass') : t('decisionOther'));
    txt('kpi-seeds', current.seeds); txt('kpi-days', current.config.trading_days - current.config.burn_in_days);
    txt('kpi-burn', t('burnIn', { days: current.config.burn_in_days }));
    txt('kpi-scenarios', Object.keys(current.summary).length);
    txt('kpi-runs', t('runs', { runs: current.seeds * Object.keys(current.summary).length }));
    txt('gate-count', `${passed}/${total}`); $('gate-ring').style.setProperty('--progress', `${passed / total * 100}%`);
    txt('gate-status', failed ? t('gatesFailed', { n: failed }) : t('gatesAllPassed')); $('gate-status').classList.toggle('warn', failed > 0);
    txt('gate-summary', current.id === 'formal' ? t('gateSummaryFormal') : t('gateSummaryOther'));
    $('report-source').href = sourceUrl('mechanism_report.md');
    txt('report-version', current.protocol); txt('report-revision', t('revision', { x: current.code_revision }));
    txt('report-hash', t('reportHash', { x: current.sha256 }));
    const config = $('config-info'); config.replaceChildren();
    fact(config, t('configTraders'), current.config.population_size);
    fact(config, t('configShares'), ['value', 'trend', 'noise'].map(k => fmt(current.config.strategy_shares[k], true)).join(' / '));
    fact(config, t('configLearning'), t(current.config.learning_enabled ? 'learningOn' : 'learningOff'));
    fact(config, t('configStage'), current.stage);
    fact(config, t('configStatistic'), t('configStatisticValue'));
    renderChart(); renderGates();
  }
  document.querySelectorAll('[data-report]').forEach(button => button.addEventListener('click', () => {
    current = snapshot.reports.find(r => r.id === button.dataset.report);
    selectedGate = null; renderReport();
  }));
  $('metric-select').addEventListener('change', renderChart);
  $('failed-only').addEventListener('change', renderGates);
  $('download-data').addEventListener('click', () => {
    const blob = new Blob([JSON.stringify(snapshot, null, 2)], {type:'application/json'});
    const url = URL.createObjectURL(blob), link = node('a');
    link.href = url; link.download = 'financial-abm-archived-showcase.json';
    document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  loaded = true;
  renderReport();
})();
