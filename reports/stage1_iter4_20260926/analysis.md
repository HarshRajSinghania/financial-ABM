# ABM 第一阶段：第四轮开发实验总报告

第四轮固定实验已完成，开发验证为 **18/22，统计 FAIL**。第一阶段仍未完成，第二阶段尚未进入。本轮没有运行 holdout 或正式验收，也没有修改门槛或追加参数扫描。

预算优先恢复解决了上一轮方向约束造成的持续仓位超限，但候选 D 的价格发现和收益可预测性恶化，不能将其判为成功修复。预选方案始终为 D；C 的结果只作机制对照。

## 实现与执行证据

- 结构配置 `configs/stage1_structural_dev_v9.json` 相对 v8 仅增加 `value_inventory_control=budget_priority`；协议 v11 相对 v10 仅改版本和用途说明。仍为 1000 主体、3500 日、1000 日预热、2500 日评价、固定 20 个种子。
- 预算恢复位于方向约束之后、现金和保证金规则之前；仅作用于当前价值型主体，与活动抽样和信息敏感度独立。使用已有仓位预算与每日调仓上限，不改目标、账户、随机数消耗或结算优先级。订单区间投影与预注册持仓区间投影等价，并保留区间内订单的原始浮点值。
- 最后一次源码和测试编辑之后，完整测试 **171 passed**，退出码 **0**。旧刻画与学习开关金标继续通过；本轮无测试后源码编辑。
- **80/80** 四分支长期诊断完成，退出码 **0**；**320/320** 开发验证完成，退出码 **1**。该 1 对应统计 FAIL，未发现工程错误或未完成任务。400 个场景/种子组合与预注册逐项一致。
- A/B 对历史结果各 20 条 metrics 与 fingerprint 完全相同；D 的 20 条 metrics 与开发 full 场景完全相同；pure trend/noise 各 20 条与上一轮开发结果完全相同。
- 49 个输入、6 个保护源码和 32 个实现/测试文件的哈希全部保持。独立核验从 CSV 重算 summary/gate，与开发报告完全一致。

## 核心结果

A=无方向/无预算，B=仅方向，C=仅预算，D=方向＋预算。均覆盖全部 20 个种子。

| 分支 | 价格偏差达标 | mean abs(log(P/F)) 均值 | 原始收益最大 abs(ACF)≤0.2 |
|---|---:|---:|---:|
| A | 12/20 | 0.08399824 | 20/20 |
| B | 15/20 | 0.07594134 | 20/20 |
| C | 12/20 | 0.09481535 | 12/20 |
| D | 10/20 | 0.09943158 | 10/20 |

每项需至少 16/20 个种子达到相应阈值。收益 ACF 是原始收益在 lag 1–20 的自相关取绝对值，不能称为绝对收益自相关。

D−B 的价格误差为 0 改善、4 完全相同路径、16 恶化，均值增加 0.02349023；没有新增通过，失去 20261106、20261113、20261116、20261117、20261118 五个原先通过的种子。D−C 为 7 改善/13 恶化，D−A 为 2 改善/18 恶化，保留这些有利反例。

主体信息的边际价格响应为 14/20，配对比率中位数 1.10683346；独立响应为 10/20，中位数 1.00948741，均不足要求的 16/20。消融可预测性门槛中，fixed_participation 为 12/20、independent_signals 8/20、liquidity_stress 9/20、value_only 10/20；fixed_liquidity 为 18/20。

## 预算修复的效果与边界

按决策价格和决策限额计算，价值组日均成交后多头超额 B→D 从 180939.515728 降至 7.636041，最长单主体连续超限从 2500 日降至 1 日。D 仍有预算后组合单日超额峰值 82095.294561，单主体峰值 217.808358（seed 20261106、day 3151、agent 3）；这是受每日最大调仓约束限制的残余，不能宣称所有时点清零。收盘重新估值和重算限额后，D 日均超额为 1996.425696、最长连续 11 日。

所有 80 次运行中的价值组空头预算超额为零。代码和边界测试对称覆盖长短两侧，但这批开发路径没有充分触发空头预算纠偏，不能据零计数声称完成经验压力验收。

C 已将成交后日均超额降至 6.927375；D 的目标缺口在 20/20 个种子均大于 C。D 的价值组期末财富相对 B 均值减少约 35.95 万，但该组财富最大回撤均值从 9.61% 降至 7.75%。财富与价格最大回撤是不同对象，不能互换。

D 的正价值信号卖出实际成交合计 308300.633735 股归于预算恢复；负价值信号买入 411.957384 股归于保证金回补，全部发生在 seed 20261112；结算追加价值组回补为零。五阶段数量与金额核对通过。预算/保证金/其他是数量记账归属，不是可独立相加的价格因果贡献；组件事件计数可能重叠。

## 价格会计与解释

四分支公共新闻和基本面路径在 20/20 个种子的全部 3500 日逐元素相同。D−B 的评价期 signed gap 差为 -0.02349486，主要体现在永久冲击累计均值差 -0.02219657，暂时状态差约 -0.00129829；新闻累计差为零。seed 20261107 的 D−B g1000 为 +0.005651，但期末 gap 差为 -0.255738，其中永久累计差 -0.254545，不能只用 burn-in 偏差解释恶化。

80 条诊断全部没有价格截断命中。原诊断报告最大 gap 重建误差为 1.56819e-14，独立日表重建最大误差约 1.302e-14；二者均小于既定 1e-11 容差。最大日价格分解误差 3.20924e-16、成交与持仓变化误差 3.55271e-15、账户财富恒等式绝对误差 5.96046e-8。280000 条日记录、60 组配对均完成独立核对。

## 全部 22 项门槛

| 门槛 | 开发结果 |
|---|---|
| `ablations_avoid_pathological_return_predictability` | FAIL |
| `agent_information_channel_has_paired_price_response` | FAIL |
| `cash_conservation` | PASS |
| `empty_information_baseline_is_weakest_discovery` | PASS |
| `endogenous_liquidity_feedback_increases_tail_weight` | PASS |
| `fixed_population_has_no_strategy_turnover` | PASS |
| `full_heavier_than_gaussian` | PASS |
| `full_price_discovery_bounded` | FAIL |
| `full_return_autocorrelation_near_zero_across_lags` | FAIL |
| `full_runs_without_price_cap` | PASS |
| `full_volatility_clustering_has_decay` | PASS |
| `full_volatility_in_daily_range` | PASS |
| `full_volume_volatility_relation_positive` | PASS |
| `garch_control_is_labelled_exogenous` | PASS |
| `liquidity_stress_increases_clustering` | PASS |
| `logit_imitation_fires_and_tracks_fitness` | PASS |
| `logit_market_remains_active_and_bounded` | PASS |
| `persistent_order_flow_is_observable` | PASS |
| `public_news_channel_has_paired_price_response` | PASS |
| `share_conservation` | PASS |
| `single_strategy_markets_remain_active` | PASS |
| `spread_and_depth_are_finite` | PASS |

## 审核入口

- `verification.json`：主核验、真实退出码、批次和哈希。
- `independent_verification.json`：独立重算全部开发统计与门槛。
- `market_analysis.md` / `.json`：全 20 种子、三组配对、逐日价格会计、成交/财富及反例。
- `exposure_analysis.md` / `.json`：逐主体双向超额、四时点估值、峰值与持续期、五阶段订单及归属。
- `development/mechanism_report.json`、`gate_evidence.csv`、`final_decision.json`：320 次开发实验及判定。
- `preregistration.json`、`implementation_hashes.json`、`tests.txt`：预注册与工程验收依据。

统计失败应返回 ChatGPT 审核并形成下一轮明确 PLAN；本报告不授权新增扫描、改换候选、解除 holdout/正式封存或进入第二阶段。
