# 文档索引

> **English summary.** This repository contains two lines of work. (1) A single-asset artificial stock market (Stage 1–3) with a frozen, audited Stage 1. (2) An in-progress multi-agent *disclosure game*: heterogeneous investors (profit-maximizing vs impact) trade 200 firms that choose between real improvement, greenwashing and doing nothing, under audits, fines and transparency policies. The domain (ESG, AI-washing, …) is a JSON config. The market layer is built and audited; the empirical starting point is calibrated to the CSI 300 (scores, book equity, market cap); the agent and policy layers are the current focus. Nothing here is a confirmed policy result yet — see “当前状态” below.

## 当前状态（2026-10-13）

| 层面 | 状态 |
|---|---|
| 多资产市场 | 已完成并冻结，只修 bug。60 个固定世界的审计结果为 57 PASS / 3 FAIL（保留记录）；订单流重放 60/60 逐字节复现 |
| 经验起点 | 沪深 300 的评分、半年报账面权益、市值三项都是 300/300；初始分布、规模相关和价值离散度都已校准 |
| 企业智能体（NPV） | 已实现。开发实验中企业从不漂绿；原因已查明：模型罚款约为法定上限的 50 倍，融资收益偏小 10–30 倍 |
| 企业智能体（强化学习） | 已实现，但训练覆盖不达标，未用于任何结论 |
| 投资者演化 | 已实现，但零偏好对照中影响力投资者占比仍上升，模仿可能主要是噪声漂移，待诊断 |
| 政策实验 | 只有开发规模的结果；正式实验尚未运行 |
| 全量测试 | 821 项通过 |

下一步见[现行计划](plan_20261013.md)的阶段 B：实现定额罚款，写出检查博弈的两个命题，确认漂绿会发生。

## 从哪里开始读

1. [现行计划](plan_20261013.md)：为什么从“拟真市场”转向“多智能体演化”，各阶段的验收标准，以及博弈论如何接入。
2. [研究契约](disclosure_research_contract.md)：研究规则和固定设定。第 14、15 节是最新的设定（2026-10-12/13）。
3. [经验量级检索](disclosure_empirical_magnitudes_20261012.md)：罚则、执法强度、ESG 融资成本的出处和换算，每条都标注了可信度。
4. 最新诊断：[漂绿条件诊断](../reports/disclosure_wash_diagnosis_20261012/README.md)、[主设定与对照的开发实验](../reports/disclosure_csi300_variants_20261012/README.md)、[沪深 300 同池联合样本](../reports/disclosure_public_data_20261011/csi300_joint_20261009/README.md)。

## 文档地图

**现行**：反映当前决定，会持续更新。**参考**：仍然有效的设计或技术说明。**历史**：保留作记录，部分内容已过时。

### 披露博弈研究

| 文档 | 内容 | 状态 |
|---|---|---|
| [plan_20261013.md](plan_20261013.md) | 智能体层的阶段计划与博弈论基准 | 现行 |
| [disclosure_research_contract.md](disclosure_research_contract.md) | 研究规则、指标、实验矩阵、固定设定；第 13 节是 2026-10-11 的证据快照 | 现行（开发草案） |
| [disclosure_empirical_magnitudes_20261012.md](disclosure_empirical_magnitudes_20261012.md) | 法条、执法数据、融资成本文献及换算到模型单位 | 现行 |
| [disclosure_information_design.md](disclosure_information_design.md) | 信息政策的最小机制设计与验收契约 | 参考 |
| [disclosure_q_learning_design.md](disclosure_q_learning_design.md) | 企业 Q-learning 的可比设计与训练预算 | 参考（覆盖未达标） |
| [disclosure_handoff_20261012.md](disclosure_handoff_20261012.md) | 2026-10-12 至 10-13 的进展记录 | 历史 |
| [disclosure_handoff_20261011.md](disclosure_handoff_20261011.md) | 2026-10-11 的项目交接 | 历史（部分已过时） |

### 单资产主应用（Stage 1–3）

| 文档 | 内容 | 状态 |
|---|---|---|
| [../README.md](../README.md)、[../OPERATIONS.md](../OPERATIONS.md) | 仓库入口与完整操作手册 | 现行 |
| [ABM三阶段开发计划_渐进式学习版.md](ABM三阶段开发计划_渐进式学习版.md) | 主应用的三阶段路线 | 参考 |
| [technical_report.md](technical_report.md) | Stage 1 矩估计校准技术报告（英文） | 参考 |
| [阶段1验收报告.md](阶段1验收报告.md) | Stage 1 状态报告（2026-08） | 历史 |
| [方案设计.md](方案设计.md)、[需求理解.md](需求理解.md)、[代码审查.md](代码审查.md) | 2026-07 早期的设计、范围与审查记录 | 历史 |

## 披露研究的代码结构

代码在 [`src/abm/disclosure/`](../src/abm/disclosure)，领域配置在 [`configs/domains/`](../configs/domains)。核心模块中不出现任何领域词汇，由测试强制检查。

| 模块 | 作用 |
|---|---|
| `config.py` | 市场配置 `MarketConfig` |
| `firms.py`、`market.py`、`investors.py`、`harness.py` | 企业价值与规模、多资产报价、两类投资者与模仿、逐日撮合与守恒检查 |
| `domain.py` | 领域映射：方向、量表、经验分布、分位数映射、规模 copula、成本与延迟 |
| `game.py`、`policy.py`、`financing.py` | 企业的三种行动、核查与罚款、政策时间表、融资信号与收益 |
| `learning.py`、`training.py` | 表格 Q-learning、训练与覆盖诊断 |
| `experiments.py`、`metrics.py`、`phase.py`、`report.py`、`runner.py` | 场景网格、配对比较、指标、相图、报告与单次运行归档 |
| `validate.py`、`calibration.py` | 市场检验；从 CSV 拟合评分分布、价值离散度和规模相关 |

## 主要报告

| 主题 | 报告 |
|---|---|
| 市场层 | [60 世界审计](../reports/disclosure_market_qualification_20261011/audit_report.md)、[订单流重放](../reports/disclosure_market_qualification_20261011/flow_replay/interpretation.md)、[初日守恒修复](../reports/disclosure_market_qualification_20261011/initial_conservation_fix/README.md)、[2500 日速度](../reports/disclosure_market_qualification_20261011/performance_2500/README.md)、[预测写法诊断](../reports/disclosure_market_qualification_20261011/predictor_diagnostic/interpretation.md)、[市场校准](../reports/disclosure_market_calibration_20261011/interpretation.md)、[公开行情核查](../reports/disclosure_market_public_20261011/report.md) |
| 数据与校准 | [公开数据总览](../reports/disclosure_public_data_20261011/README.md)、[华证评分快照](../reports/disclosure_public_data_20261011/csi300_huazheng_latest/README.md)、[沪深 300 联合样本](../reports/disclosure_public_data_20261011/csi300_joint_20261009/README.md)、[WBA 社会维度](../reports/disclosure_calibration_20261011/README.md)、[中兴财务试点](../reports/disclosure_public_data_20261011/zte_financial_pilot/README.md) |
| 机制开发实验 | [基础开发](../reports/disclosure_development_20261011_v1/report.md)、[融资 v2](../reports/disclosure_financing_development_20261011_v2/report.md)、[信息机制](../reports/disclosure_information_development_20261011_v1/interpretation.md)、[报告频率](../reports/disclosure_reporting_development_20261011_v1/report.md)、[相图 v2](../reports/disclosure_phase_development_20261011_v2/report.md)、[动作网格检查](../reports/disclosure_action_grid_checks_20261011/interpretation.md)、[Q-learning 检查](../reports/disclosure_q_learning_checks_20261011/interpretation.md)、[AI-washing 迁移](../reports/disclosure_generality_financing_20261011/ai_washing/report.md) |
| 最新诊断 | [主设定与对照](../reports/disclosure_csi300_variants_20261012/README.md)、[漂绿条件](../reports/disclosure_wash_diagnosis_20261012/README.md) |

开发实验都使用小规模和已经观察过的种子，只用于检查机制，不是政策结论。

## 仓库中没有的内容

- **供应商与教材原始数据**（华证、东方财富、BaoStock、巨潮、Tsay 教材数据）：没有开放再分发许可，不放入仓库。采集脚本和 hash 清单保留在 `reports/disclosure_public_data_20261011/`，可以重新取数并逐项核对。WBA 数据为 CC BY 4.0。
- **可以重新生成的大文件**：路径 npz、每个试验各存一份的源码包、训练好的 Q 表、超大审计 JSON，见 [`.gitignore`](../.gitignore)。
- **沪深 300 华证派生的领域文件和三个开发网格目录**：其中包含华证评分的汇总经验分布（不含公司身份），是否公开尚待确认，暂未推送。相关说明和比较结果已经公开，但其中指向这些文件的链接暂时无法打开。
- 研究证据目录按原始字节存储（见 [`.gitattributes`](../.gitattributes)），因此报告中记录的 SHA-256 可以直接核对。

## 运行

```bash
python -m pip install -e ".[all,dev]"
python -m pytest
python -m abm.disclosure.runner --domain configs/domains/esg.json --config <市场JSON> --output <新目录>
python -m abm.disclosure.experiments --spec configs/disclosure_financing_development_v1.json --output <新目录> --workers 4
```
