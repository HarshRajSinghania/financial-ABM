# X 线程草稿（由你发布）

草稿，由你发布。数字与[阶段 F 报告](../disclosure_stage_f_20261014/README.md)一致，量级按研究契约第 20.14 条以“自然衰减 0 到 0.2 SD/年”的区间表述。沙盘链接已替换为 GitHub Pages 地址。按 X 的计数规则（链接计 23，中文每字计 2），替换链接后每条都不超过 280。

## English

**1/7**
Why do firms greenwash, and which policy stops it: heavier fines, or making the truth easier to see?

I built a multi-agent artificial market to test it: 1,000 investors, 200 firms, a regulator. Pre-registered, 1,770 simulated worlds. Thread 🧵

**2/7**
Firms choose each period between real ESG improvement (costly, slow), inflating their report (cheap, fast, might be audited), or doing nothing. Impact investors pay more for good reported ESG, which lowers firms' financing costs. That is the incentive to look green.

**3/7**
Result 1: the ordering is robust. Information policy (transparency) > penalty policy (fines) > baseline, across 30 paired seeds and every robustness control.

The magnitude is a range: +0.04 to +0.33 SD for information vs baseline, depending on an uncalibrated decay assumption.

**4/7**
Result 2: transparency has a threshold. Above τ* ≈ 0.57, greenwashing stops entirely and fines stop mattering. A closed-form prediction from an inspection game called the threshold correctly in all 16 grid cells.

**5/7**
Result 3 (assuming 0.2 SD/yr decay): fixed fines lose bite fast. No fine to CNY 10 m (China's statutory cap) cuts greenwashing decisions from 91% to 22%; 2×, 4×, 8× the fine: 16%, 13%, 13%. A firm already hiding a case adds new inflation to it and faces no new fine.

**6/7**
Result 4: the size gap comes from greenwashing, not costs. A CNY 10 m fine is noise for a giant: large firms greenwash in 66% of decisions vs 6% for small ones (same decay assumption). And none of this works without investor preference: no green taste, no effect from any policy.

**7/7**
Try it in your browser: set transparency, fines and audits; watch 200 synthetic firms decide. The rule matches the Python model to 1e-12, and the page shows where the simplification falls short.
https://kanzaler123.github.io/financial-ABM/
Code, pre-registration, all numbers: https://github.com/kanzaler123/financial-ABM

## 中文

**1/7**
企业为什么会漂绿？哪种政策更能阻止它：罚得更重，还是让人看得更清？我做了一个多智能体人工市场来检验：1000 名投资者、200 家企业、一个监管者。设计预先登记，共 1770 个模拟世界。🧵

**2/7**
企业每期在三者中选择：真实改善 ESG（贵、慢），在报告里虚报（便宜、快，可能被查），或者不动。影响力投资者愿意为好看的 ESG 披露付更高的价格，从而降低企业的融资成本，这就是“看起来绿”的激励。

**3/7**
结论一：排序稳健。信息政策（透明度）> 惩罚政策（罚款）> 基准，在 30 个配对种子和所有稳健性对照下都成立。量级是一个区间：信息政策比基准高 0.04 到 0.33 个标准差，取决于一个尚未校准的衰减假设。

**4/7**
结论二：透明度有门槛。超过 τ* ≈ 0.57 后，漂绿完全停止，罚款也不再起作用。检查博弈推出的闭式预测，在 16 个格点上全部判断正确。

**5/7**
结论三（假设每年衰减 0.2 个标准差）：定额罚款的威慑很快见顶。从不罚到罚 1000 万元（法定上限），漂绿决策占比从 91% 降到 22%；罚 2、4、8 倍，只降到 16%、13%、13%。已有案件没被查出的企业，新虚报并入旧案，不再面对新的罚款。

**6/7**
结论四：规模鸿沟来自漂绿，而不是成本。1000 万元对大企业不痛不痒：大企业 66% 的决策在漂绿，小企业只有 6%（同一衰减假设）。而这一切都以投资者偏好为前提：没有绿色偏好，任何政策都没有效果。

**7/7**
可以在浏览器里试：调节透明度、罚款和核查，看 200 家合成企业怎么选。决策规则与 Python 模型一致到 10⁻¹²，页面也写明了简化在哪里失真。
https://kanzaler123.github.io/financial-ABM/
代码、预登记和每个数字的出处：https://github.com/kanzaler123/financial-ABM
