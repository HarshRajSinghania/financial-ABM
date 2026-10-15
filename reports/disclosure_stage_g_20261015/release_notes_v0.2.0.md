# v0.2.0 Release 说明（草稿）

草稿，尚未发布。发布前需要你逐项确认：推送、启用 GitHub Pages、打 tag `v0.2.0`、发布 Release。Zenodo DOI 由你在 Zenodo 上操作。下方英文部分可直接作为 GitHub Release 正文。

---

## Financial ABM v0.2.0: stage F results and a browser policy sandbox

A multi-agent artificial market for ESG disclosure and greenwashing policy. This release adds the pre-registered confirmatory experiment (stage F) and an in-browser policy sandbox.

### Stage F: confirmatory policy experiment

59 scenarios × 30 paired seeds (41001–41030), 1,770 worlds at contract scale (1,000 investors, 200 firms, 3,500 trading days). The design, seeds and primary questions were committed before the run (`2b08f65`). Firms use a continuous NPV rule. All conclusions are conditional on the model.

- **Ordering:** information policy > penalty policy > baseline, at both ends of natural decay (0 and 0.2 SD/year) and in every robustness control.
- **Magnitudes are a range** because natural decay is uncalibrated: information vs baseline +0.04 to +0.33 SD; penalty vs baseline +0.005 to +0.13 SD; information vs penalty +0.035 to +0.21 SD (policy window, days 1200–3500).
- **Four primary questions supported** (Holm p < 10⁻¹³): market preference raises the full-period true level (+0.79 SD); information beats penalty; policy effects exist only with market preference; the size gap moves with the cost multipliers.
- **Transparency threshold:** above τ* ≈ 0.57 greenwashing stops; the inspection-game prediction held in 16/16 grid cells.
- Under the 0.2 SD/year decay assumption: fixed fines show diminishing marginal deterrence, and the large–small gap comes from greenwashing by large firms, not from costs.

Report: `reports/disclosure_stage_f_20261014/README.md` (Chinese). Contract: `docs/disclosure_research_contract.md` §20.

### Browser policy sandbox (`showcase/`)

- **Panel ①, firm decision:** 200 anonymous synthetic firms (fresh seed 51001, day-1200 snapshot) choose under the policy you set. The JavaScript decision core matches the Python model on 1,200 random inputs, with identical choices and relative errors of at most 10⁻¹². Under the baseline policy it reproduces the full model's day-1200 decision for every firm.
- **Panel ②, simplified dynamics (no market feedback, not a research result):** 14 years with fixed financing benefits and market caps. It agrees with the Python reference period by period, and the page reports its distance from the full model ("cost of simplification").
- **Panel ③, full-model results:** stage F numbers with experiment id, file hash and commit.
- Chinese/English switch, ESG and AI-washing (illustrative) domains, offline single file, no external dependencies. The stage 1 exhibit moves to `stage1/`.

### Reproduce

```sh
python -m pip install -c requirements-lock.txt -e ".[all,dev]"
python reports/disclosure_stage_g_20261015/export.py     # about 2 min with 9 workers
python reports/disclosure_stage_g_20261015/fixtures.py
python reports/disclosure_stage_g_20261015/compare.py
node showcase/sandbox/check_core.js
python showcase/build.py --output _site
```

### Limits

NPV firms only (learning firms did not pass stage D); audit intensity, targeted audits and implementation costs are not modelled; magnitudes depend on uncalibrated natural decay, and mean reversion is not covered by the reported range.

---

## 中文摘要

- 阶段 F 确认性实验：排序“信息 > 惩罚 > 基准”在自然衰减两端都成立；量级以区间报告（信息相对基准 +0.04 到 +0.33 SD）；四个主要问题都得到支持；透明度门槛 τ* ≈ 0.57 的预测 16/16 成立。
- 浏览器政策沙盘：企业单期决策（与 Python 逐项一致）、无市场反馈的简化动态（标明非研究结果，附“简化的代价”）、阶段 F 结果（附出处）；中英切换，ESG / AI-washing 切换。
- `CITATION.cff` 与 `pyproject.toml` 版本升到 0.2.0。
