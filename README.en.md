<p align="center">
  <img src=".github/assets/disclosure-cover.svg" alt="Financial ABM: policy meets markets. A multi-agent artificial market for ESG transition and greenwashing. The right side is a structural schematic, not live data." width="100%">
</p>

<p align="center">
  <a href="https://github.com/kanzaler123/financial-ABM/actions/workflows/tests.yml"><img src="https://github.com/kanzaler123/financial-ABM/actions/workflows/tests.yml/badge.svg?branch=master" alt="Code tests (not model acceptance)"></a>
  <a href="https://github.com/kanzaler123/financial-ABM/actions/workflows/showcase.yml"><img src="https://github.com/kanzaler123/financial-ABM/actions/workflows/showcase.yml/badge.svg?branch=master" alt="Showcase build"></a>
</p>

<p align="center">
  <b>Why do firms greenwash, and which policies actually drive real ESG transition?</b><br>
  Multi-agent artificial market · evolving investor types · firm disclosure game · policy experiments · auditable evidence
</p>

<p align="center"><a href="README.md"><b>中文</b></a> · <a href="docs/README.md"><b>Docs index (Chinese)</b></a></p>

---

> [!NOTE]
> **Research in progress.** The market layer is built and audited, and the empirical starting point is calibrated to the CSI 300. The agent layer and the formal policy experiments are the current focus. Every finding below carries an evidence label; **there are no confirmed policy results yet.**

## The question

Most ESG research asks backward-looking correlation questions: do high-ESG firms earn more, or borrow more cheaply? Those methods struggle to explain **how** a transition happens, and they cannot compare policies that were never tried.

This project builds an artificial financial market in which heterogeneous investors and firms interact, learn and evolve, and then treats policy as a controlled variable:

> **Under joint pressure from policy and markets, how efficient is the ESG transition, and what path does it take?**

1. **Which policy works better?** Information policies (transparency) versus enforcement policies (fines), compared at equal expected penalties.
2. **How strong is the market's own engine?** Can impact investors drive a transition by “voting with their feet”? Do policies amplify or replace that force?
3. **Do large and small firms differ?** Is there an “ESG divide” in how fast norms spread by firm size?
4. **When does the market fall into a greenwashing trap?** Phase diagrams separating transition success, failure and greenwashing traps.

## Agents

| Agent | Count | Behaviour |
|---|---|---|
| **Profit-maximizing investors (PM)** | part of 1,000 investors | Mean–variance allocation; ESG has no utility value |
| **Impact investors (II)** | part of 1,000 investors | Utility includes a taste for *reported* ESG. Investors imitate the better-performing type each quarter, so the II share evolves |
| **Firms** | 200, in large / mid / small tiers | Each period: **real improvement** (costly, delayed), **greenwashing** (cheap, fast, may be audited) or **maintain**. NPV-rational or Q-learning modes |
| **Regulator** | 1 | Transparency, audit probability, fines and subsidies; policies can switch on any date |
| **Market maker and noise flow** | — | Multi-asset quasi order book with price impact, volatility-dependent depth, and daily cash and share conservation |

The disclosure game, a true attribute versus a reported attribute, is not specific to ESG. **A domain is a JSON file**; the core code contains no domain vocabulary, and a test enforces that. Bundled domains: [ESG](configs/domains/esg.json), [AI-washing](configs/domains/ai_washing.json), [WBA social](configs/domains/wba_social_2023.json).

**Game-theoretic benchmarks.** Each layer maps to a classic game: firm vs regulator (inspection game), firm vs investors (signaling: pooling vs separating), investor population (evolutionary game and replicator dynamics), regulator as a Stackelberg leader. The simulation tests whether boundedly rational, learning agents reach these equilibria, and where they get stuck.

## What we have found so far

**[Fact]** checked against primary sources · **[Diagnosis]** reproducible analysis of model behaviour · **[Dev]** small-scale, few-seed observation · **[Open]** identified but unresolved

- **[Fact] Statutory fines barely register for large Chinese firms.** China's Securities Law (Art. 197(2)) caps fines for false disclosure at CNY 10 million, about 0.01% of the median CSI 300 market cap. The 2024 exchange sustainability-reporting guidelines provide only disciplinary measures, with no fines. Whether greenwashing in ESG reports falls under Art. 197 is unclear. [Evidence table](docs/disclosure_empirical_magnitudes_20261012.md)
- **[Diagnosis] Our firms never greenwashed, and we found out why.** In the development runs, the expected fine was 14.5× the gross gain from washing (median). Mapped to real magnitudes, the model's fine was about 50× the legal cap and the financing benefit 10–30× too small. Without the fine, washing beats real improvement in every recorded decision. [Diagnosis](reports/disclosure_wash_diagnosis_20261012/README.md)
- **[Diagnosis] The transparency threshold is all-or-nothing.** With no fine, every firm washes below transparency ≈ 0.565 and none does above it, a consequence of homogeneous discounting and timing that the formal design must address.
- **[Dev] Impact investors push real improvement.** Across three initialization settings, the market-preference effect is positive: about +1.7 to +2.5 score points over the measurement window (3 seeds, wide intervals).
- **[Open] Investor evolution may be mostly drift.** In a zero-taste control, where both types behave identically, the impact-investor share still rose. That mechanism is the market's “own engine”, so it will be diagnosed against replicator dynamics next.

## Roadmap

- [x] Single-asset market foundation (Stage 1): frozen v15 formal acceptance 22/22
- [x] Multi-asset market: 60 fixed worlds audited, 57 PASS / 3 FAIL (kept on record); order-flow replay reproduced 60/60 bit for bit
- [x] Empirical start: CSI 300 ESG scores, half-year book equity and market caps, 300/300 each
- [x] Greenwashing-condition diagnosis and evidence review
- [ ] Firm game with capped lump-sum fines, plus inspection-game propositions
- [ ] Investor evolution: selection versus drift, benchmarked on replicator dynamics
- [ ] Learning firms: do boundedly rational firms *learn* to greenwash?
- [ ] New agents: risk-based regulator, assurance providers, rating disagreement
- [ ] Formal experiments: information vs enforcement, phase diagrams, size divide (fresh seeds, design frozen before running)
- [ ] In-browser policy sandbox (GitHub Pages)

## Research standards

Key settings are fixed in a [research contract](docs/disclosure_research_contract.md) before any policy experiment that uses them. Failures are kept, not deleted. Evidence directories are stored byte for byte, so the recorded SHA-256 values can be checked directly. Every empirical parameter cites its source and evidence level. Vendor data (Huazheng, Eastmoney and others) has no open redistribution licence and is not included; collection scripts and hash manifests are.

**Build on it.** Write a domain JSON for another disclosure problem (carbon, earnings management, AI-washing), or a spec in [`configs/`](configs) with your own scenarios and paired comparisons. Citation: [CITATION.cff](CITATION.cff).

## Quick start

```sh
python -m venv .venv
python -m pip install -c requirements-lock.txt -e ".[all,dev]"
python -m pytest
python -m abm.disclosure.experiments --spec configs/disclosure_financing_development_v1.json --output runs/financing_dev --workers 4
```

The single-asset Stage 1–3 application (web and desktop observatory, SEC 8-K information factors, interactive showcase) is described in the [Chinese README](README.md) and [OPERATIONS.md](OPERATIONS.md).

---

<sub>Financial ABM · Research prototype. Inspectable mechanisms, traceable evidence. Not investment advice.</sub>
