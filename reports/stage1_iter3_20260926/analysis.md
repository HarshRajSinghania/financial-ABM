# 第一阶段第三轮：价值型订单方向约束

固定诊断已完成40/40次：baseline与candidate各20个相同开发种子，预热1000日、评价2500日。20条baseline的全部指标及指纹均精确复现第二轮full；两个场景只改变`value_order_constraint`。本报告以**全部20个配对**为主要依据，不只挑选原来的8个失败种子。

候选规则确实清除了价值信号反向的自愿成交，但价格发现通过数仅从12/20升至15/20，仍低于16/20门槛；同时出现更大的持仓敞口和目标偏差。因此不能以订单规则实现正确或平均gap改善代替阶段验收。320次开发矩阵已完成，结果为21/22，详见末节；尚未取得新的独立留出与正式验收结论，第一阶段未完成，不能进入第二阶段。

证据来自[固定诊断与全20配对](/C:/Users/kanzaler/Desktop/ABM/reports/stage1_iter3_20260926/value_direction/diagnostics.json)、其daily和reconstruction目录。新增[敞口审计数据](/C:/Users/kanzaler/Desktop/ABM/reports/stage1_iter3_20260926/analysis_data.json)保存了从日表计算的逐种子soft目标超额、容差、峰值日期及逐日新闻一致性检查。金额均为模型名义金额；除说明为合计或极值外，日表统计使用评价窗、各种子等权。

## 订单映射：机械约束有效，但大量意向反复被取消

下表为20种子评价窗合计。计数是agent-day事件，不是不同交易者人数；正负信号按原policy的`value_signal`严格符号判断，零单与反向单分开。

| 方向 | baseline实际自愿成交次数 | candidate约束前次数 | candidate约束后／风控后／成交次数 | candidate取消股数 | 取消名义额（百万，开盘价） |
|---|---:|---:|---:|---:|---:|
| 正价值信号、自愿卖出 | 5,605,609 | 11,358,993 | 0／0／0 | 11,910,308.88 | 3464.061 |
| 负价值信号、自愿买入 | 1,158,558 | 1,995,479 | 0／0／0 | 2,811,883.22 | 271.779 |

candidate取消了13,354,472个反向订单事件，约占20,000,000个价值型agent-day的66.77%。对应的正信号零自愿单从约束前2,099,443增加到13,458,436，负信号零自愿单从693,154增加到2,688,633，增量分别与被取消事件数精确相同。规则没有把不活跃的零单误记为反向成交。由于目标与实际持仓已经分离，同一潜在调整可能多日重复出现；累计取消名义额不是实际交易额，也不是一次性释放的需求。

实际价值型总提交名义额的20种子均值为每条路径1194.665万→493.314万，下降58.71%，20/20均下降。趋势型为6357.698万→6294.086万，噪声型为11205.189万→11119.023万。价值型交易收缩显著强于其他类型；仅看“反向单归零”会遗漏这一行为变化。

强制补仓没有被归入自愿买单或阻断。baseline价值型政策强制cover为0；candidate出现2,823次、411.957384股，**全部集中在种子20261112**，其政策强制股数与实际成交的该部分精确一致，价值型结算新增cover仍为0。两场景还分别有噪声型政策cover 25,937／22,356次、结算增量cover 323／310次，趋势型两类均为0。政策cover仅指原卖出／零单风控分支产生的补仓；结算增量单独记录，不把原本自愿的正买单重新归因为强制补仓。

价值型提交与成交股数在两场景的评价窗内逐日完全一致，全部40次的实际持仓变化与成交股数最大误差仅3.55e−15股。提交金额按开盘价、成交金额按成交价估值，金额不同不能当成未成交。订单映射属于实现证据；**不能将取消流量乘以冲击参数，声称得到价格变化的因果贡献**。

## 价格会计：改善有限，而且并非所有种子受益

20/20对的`public_news_impact`及`fundamental_value`在全部3500日均逐元素精确一致；不是仅比较新闻累计均值或终值。下表为全20种子统计。

| 指标 | baseline | candidate |
|---|---:|---:|
| mean absolute gap≤0.1的种子数 | 12/20 | 15/20 |
| mean absolute gap的种子均值 | 0.083998 | 0.075941 |
| mean absolute gap的种子中位数 | 0.074554 | 0.080857 |
| g1000均值 | −0.042769 | −0.040543 |
| 评价期mean signed gap均值 | −0.063401 | −0.056191 |
| g3500均值 | −0.115620 | −0.092187 |
| 最大回撤的种子均值 | 0.391512 | 0.401603 |
| 全路径价格限幅命中 | 0 | 0 |

mean absolute gap在12个种子改善、8个恶化；均值变好而中位数变差，不能称为普遍改善。原失败8个种子中20261106、20261113、20261116、20261117转为通过，但原通过种子20261101从0.076825恶化到0.104119并转为失败。最明显的改善来自20261107（0.184737→0.128130），改善后仍不通过。最大回撤在17/20种子上升，均值增加0.010092。g1000和最终signed gap的配对变化均各有10正、10负，平均改善不能替代逐种子审查。

价格水平重构从第1日累计，未在预热结束时重置。下表是累计分量在评价窗内的均值，不是评价窗净增量；初始gap及初始暂态均为0。

| 有符号累计分量 | baseline | candidate | candidate−baseline |
|---|---:|---:|---:|
| 信息残差：(α−1)Σnews，α=0.95 | −0.041779 | −0.041779 | 0 |
| 永久冲击 | −0.019998 | −0.012344 | +0.007654 |
| 暂态状态相对初始值的变化 | −0.001624 | −0.002068 | −0.000444 |
| 限幅调整 | 0 | 0 | 0 |
| 合计：mean signed gap | −0.063401 | −0.056191 | +0.007210 |

永久项在12/20对上升、8/20下降。这里记录的是完整路径的会计差异，不是把各分量绝对值当成mean absolute gap的可加贡献。最大逐日收益分解误差3.21e−16，最大gap重构误差1.23e−14；财富恒等式的最大绝对误差5.96e−8。机械会计成立不表示研究机制已经通过。

## 实际敞口：约束抑制平仓，目标偏差扩大

价值组有400名交易者。本轮每人的名义soft目标上限尺度为2750，合计110万；该上限来自以初始reference wealth计的目标，并不等于当期财富或硬风控额度。实际gross持仓、实际net持仓和逐人正向超额是不同量。

| 价值型指标 | baseline | candidate |
|---|---:|---:|
| 组总gross名义敞口的评价均值 | 763,608.06 | 986,444.54 |
| 上述gross均值／400 | 1,909.02 | 2,466.11 |
| 组总net名义敞口的评价均值 | 727,214.77 | 942,764.89 |
| 成交后组总绝对目标偏差的评价均值 | 779.46 | 227,677.45 |
| 组财富的评价均值 | 5,035,847.75 | 5,084,509.31 |
| 组最终财富的种子均值 | 5,475,491.83 | 5,701,732.45 |
| 组内正向超额／目标总额的评价均值 | 0.587% | 16.456% |
| 存在组内正向超额的评价日比例 | 29.748% | 57.068% |
| 组内正向超额／目标总额的全样本峰值 | 19.266% | 213.803% |

实际gross敞口在17/20种子增长、3/20下降；成交后绝对目标偏差在20/20增长，均值约为baseline的292倍。组财富均值只在15/20改善，最终财富只在14/20改善，不能据平均财富上升忽略其余种子与回撤代价。组平均gross持仓低于2750，仍可能与部分交易者显著超出soft目标同时存在。

正向超额按日表恒等式计算：`positive_excess_shares = actual_position_before_shares − position_limit_shares + buy_position_capacity_shares = Σmax(position_i − limit_i, 0)`，再乘当日开盘价。`limit_i`包含既有position_cap截断。原始计算的最小浮点负值为−1.09e−11股，金额计算将负值截为0；“存在超额日”使用1e−9股容差。这里统计的是**组内正向超额总额及日期比例，不是超限交易者人数**，也不等于违反硬性现金、杠杆或结算规则。

candidate峰值来自20261107的第3276日。已独立核对同一天：价值组net与gross均为3,451,831.20，目标总额1,100,000，正向超额2,351,831.20，因此超额率为213.803%；另由实际net／目标总额得到3.138028倍，组均每人持仓8,629.58。两种比率分别计算，未把超额率直接冒充实际敞口比率。该种子整个评价窗每天均存在正向超额，平均超额率80.487%，而价格发现仍不通过。

现有规则只按价值方向删去自愿订单，没有同时使实际持仓跟随目标收缩。这与重复取消调整、实际敞口增长和目标偏差积累相一致，但本轮未单独干预这些中间机制，不能把对应差异称为独立机制贡献。下一轮评审应同时考察方向一致性、持仓调整与敞口后果；当前证据不支持只因反向成交消失便接受候选机制。

## 320次开发矩阵：21/22，统计未通过

固定16场景×20种子全部完成。诊断退出码0；开发命令退出码1表示统计门槛未通过，未发生工程中断。全部360次预注册长运行完成，没有追加种子、参数扫描、留出或正式验收。完整结果见`development/mechanism_report.json`、`development/per_seed_metrics.csv`及`verification.json`。

| 检查 | 结果 |
|---|---|
| `ablations_avoid_pathological_return_predictability` | PASS |
| `agent_information_channel_has_paired_price_response` | PASS |
| `cash_conservation` | PASS |
| `empty_information_baseline_is_weakest_discovery` | PASS |
| `endogenous_liquidity_feedback_increases_tail_weight` | PASS |
| `fixed_population_has_no_strategy_turnover` | PASS |
| `full_heavier_than_gaussian` | PASS |
| `full_price_discovery_bounded` | FAIL |
| `full_return_autocorrelation_near_zero_across_lags` | PASS |
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

唯一失败为价格发现：均值绝对log gap≤0.1的种子为15/20，低于至少16/20。失败种子为20261101、20261102、20261104、20261107、20261115。

两项Agent信息渠道配对证据仍通过：边际响应17/20（85%，中位比值1.449604），独立响应18/20（90%，中位比值1.096349），分别高于上一轮的16/20。其余21项统计门槛通过并不消除上文敞口累积的代价。

工程与一致性核验：完整测试122项通过；最后补充的诊断断言对应工具子集24项复测通过。baseline20条的全部29项指标及指纹与第二轮full精确相同；candidate20条的全部29项指标与本次开发full精确相同。no_agent_information、no_information_channels、trend_only、noise_only各20条指标与旧开发结果逐值相同。输入/受保护文件34项及源码与测试30项哈希全部未变。

新的正式验收尚未进行；`stage1_complete=false`、`may_enter_stage2=false`。本轮候选仍未满足开发门槛，且存在持仓累积代价，结果提交ChatGPT独立审阅后再决定下一步。
