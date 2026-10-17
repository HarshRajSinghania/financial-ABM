# GitHub 展示层 · Financial ABM

独立于 `web/` 的静态站点，不连接 FastAPI，不在构建时运行模拟。两个页面：

| 页面 | 内容 |
|---|---|
| `_site/index.html`（首页） | 漂绿政策沙盘（计划阶段 G）：首屏作战台回放面板 ② 的 14 年简化动态（企业球、决策频谱、事件流、核查日志，标注为非研究结果）；面板 ① 企业单期决策，面板 ② 简化动态（无市场反馈，非研究结果），面板 ③ 阶段 F 完整模型结果。默认英文，可切换中文；ESG / AI-washing 切换 |
| `_site/stage1/index.html` | 阶段 1 展厅：历史 v13/v14 机制报告（原首页，内容不变），默认英文，可切换中文 |

## 预览

在项目根目录执行：

```sh
python showcase/build.py --output _site
python -m http.server 8080 --directory _site
```

访问 `http://localhost:8080`，也可以直接打开 `_site/index.html`。输出内联全部 CSS、JavaScript 与数据，没有 CDN、在线字体、遥测或外部图表库。构建只用 Python 3.12+ 标准库。

## 沙盘的数据与一致性

| 文件 | 来源 |
|---|---|
| `data/sandbox_firms.json` | [导出脚本](../reports/disclosure_stage_g_20261015/export.py)：新种子 51001 按阶段 F 主设定运行，第 1200 日快照 200 家合成企业；AI-washing 领域同样快照 |
| `data/stage_f.json` | 从已提交的 `confirmatory_v1_analysis.json` 复制，附 `experiment_id`、SHA-256 与提交号 |
| `data/simplification.json` | [对照脚本](../reports/disclosure_stage_g_20261015/compare.py)：简化动态与完整模型的差距（“简化的代价”） |
| `sandbox/core.js` | 决策核心与简化动态，移植自 `src/abm/disclosure` 与 `sandbox/reference.py` |
| `sandbox/fixtures/*.json` | [夹具脚本](../reports/disclosure_stage_g_20261015/fixtures.py)：由 Python 模型代码生成的期望值 |

构建会核对 `stage_f.json` 与分析文件的 SHA-256、导出时的阶段 F 配置和 AI-washing 领域文件，任何一处变化都会拒绝构建。企业字段只允许模型自己的数值列，不含任何真实公司信息。

```sh
node showcase/sandbox/check_core.js          # JavaScript 与 Python 逐项一致（相对误差 ≤ 1e-12）
python -m unittest discover -s showcase -p 'test_*.py'
python -m pytest tests/test_sandbox_reference.py   # 夹具仍与当前模型代码一致（需要安装 abm）
```

`sandbox/reference.py` 放在 `src/abm` 之外：包内源码哈希是每个冻结实验身份的一部分。

## GitHub Pages

线上地址：[https://kanzaler123.github.io/financial-ABM/](https://kanzaler123.github.io/financial-ABM/)。Pages 已于 2026-10-16 启用（Source: GitHub Actions），`GitHub showcase` 工作流在 master 更新时部署 `_site`。未启用 Pages 时，CI 仍验证页面并提供名为 `github-showcase` 的离线产物；PR 只构建检查，不发布。

## 阶段 1 展厅的数据约定

`build.py` 从三个已提交的历史 v13/v14 `mechanism_report.json` 读取原始数据，保留报告代码版本、SHA-256 和源文件链接，不重算模拟。2026-08-14 正式归档为 18/22，开发与 holdout 各为 22/22；此后[冻结 v15](../reports/stage1_iter6_20260926/formal/final_decision.json)于 2026-09-26 正式验收 22/22。分布图使用跨种子中位数与 Q10–Q90，不是时序数据或置信区间。

## 修改入口

| 文件 | 内容 |
|---|---|
| `sandbox/index.html`、`styles.css` | 首页结构与样式 |
| `sandbox/i18n.js` | 中英文案；`test_showcase.py` 检查两种语言的键一致，并检查模板中没有未接入切换的中文 |
| `sandbox/app.js` | 政策调节、作战台回放、图表与交互（模型计算都在 `core.js`） |
| `sandbox/desk.js` | 作战台的绘制：企业球（canvas）、决策频谱、智能体角色与迷你走势线；只画图，不含文案和模型计算 |
| `stage1/` | 阶段 1 展厅的模板、样式与脚本；文案在 `stage1/i18n.js` |
| `build.py` | 数据核对与离线单页构建 |
| `test_showcase.py` | 数据与静态构建回归 |
