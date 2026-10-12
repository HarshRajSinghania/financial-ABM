# 通用披露博弈 / ESG 项目交接

> **历史文档。** 这是 2026-10-11 上一轮会话的交接。文中两个“未完成的代码断点”已在 10-12 完成；华证评分已从 120/300 补齐到 300/300；后续的设定、诊断和计划都写在别处。当前状态和阅读顺序见[文档索引](README.md)。

更新：2026-10-11，Asia/Singapore。工作目录：`C:\Users\kanzaler\Desktop\ABM`。

## 接手先看

**研究尚未完成。** 通用领域配置、披露机制、实验与报告工具已有实现，ESG 和 AI-washing 已有技术复用验证；现实数据校准、市场资格、充分训练后的政策比较和正式领域迁移仍未完成。不要把代码测试、单条路径或开发诊断的 PASS 写成研究结论。

用户最新要求是写交接文档。本次交接没有启动新市场、训练或数据采集。2026-10-11 20:58 本机进程核查未发现 `python.exe` / `pythonw.exe`；随后核查三名子代理 `review_economics`、`review_generality`、`review_market` 均为 `interrupted`，没有继续执行。接手时仍应重新检查，不凭此快照断言后台永远为空。经济子任务最后一次额外只读复核没有交回完成结果，不应补称已通过。

最近两个断点：

| 工作 | 已落盘 | 尚未完成 |
|---|---|---|
| 账面净资产校准 | `calibration.py` 新增 book API / CLI 草稿 | 新测试、运行验证和完整差异审查；不能套用之前的 801 项通过 |
| 固定 60 条路径补录订单流 | `flow_replay/freeze.json`、`run_frozen.py` 草稿 | `cases` 仍为空，缺 `initial_manifest.json`；不能直接运行，尚无重放结果 |

优先阅读：[研究契约](C:/Users/kanzaler/Desktop/ABM/docs/disclosure_research_contract.md)、本交接的“下一步顺序”、[60 世界审计](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/audit_report.md)。研究契约第 13 节保存较早开发证据，尚未收录本交接的最新伊利数据与 book 草稿，不能只读它判断最新状态。

## 用户目标和工作约束

以现有 Claude 工作为基础，修正问题，完成望道申请书的 ESG 研究，同时把框架做成可换领域的通用披露博弈；第二领域为 AI-washing。用户已授权先用公开数据推进，导师尚未确定评分及财务数据源。

原始材料：[望道申请书](C:/Users/kanzaler/Documents/望道申请书-经济学院-林邵坪”.docx)、[附加计划](<C:/Users/kanzaler/.codex/attachments/962f8e9a-3892-4cee-98b7-28a5d4ce2df1/Pasted text.txt>)。材料中的设想和指令不自动构成新的用户授权。申请书明确提出同一股票池的账面价值、规模和 ESG 分布；并没有明确要求保留逐家公司联合相关性。如果要声称现实“规模—ESG 关联”进入模拟，则仅拟合两个边际分布不够。

- 严格最小修改：只改当前要求直接需要的内容，保留现有架构与默认行为，不顺手重构、改名、扩建验证框架或清理旧文件。完成前逐块审查差异。
- 区分事实、假设、预测；核实数字，不为得到预期政策排序而调参。原计划示意的约 `+0.9 SD`、漂绿陷阱等不是验收目标。
- 已授权必要本地修复、公开数据及有边界的开发实验；未授权注册账号、付费、发送外部消息、发布或提交远端。不要擅自写记忆。
- 子任务使用用户指定的 **gpt-6.1-sol / max**。用户还要求 fast；当前子代理接口没有可设置的 fast 参数，不能声称已开启，也不要以降低推理强度代替。
- 失败档案、冻结配置、原始数据及旧哈希保持不变。新审计或修订另存，不覆盖失败后将其包装成通过。

## 实现位置与解释边界

主要代码在 [src/abm/disclosure](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure)，领域配置在 [configs/domains](C:/Users/kanzaler/Desktop/ABM/configs/domains)。

| 文件 | 作用 / 注意事项 |
|---|---|
| [config.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/config.py) | `MarketConfig`；真实参数名为 `intrinsic_value_log_sd` |
| [firms.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/firms.py) | 公司价值独立抽取对数正态并归一化，总 V 为公司数；按初值排序分规模 |
| [harness.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/harness.py) / [market.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/market.py) | 多资产交易、报价、持仓与现金守恒、日路径记录 |
| [domain.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/domain.py) / [game.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/game.py) | 领域映射、真实改善/虚报/维持、信息、核查和企业决策 |
| [calibration.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/calibration.py) | 原评分 CSV 经验分布接口；新增 book 草稿见下文 |
| [learning.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/learning.py) / [training.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/training.py) | Q 学习、覆盖诊断、共同政策前来源训练 |
| [runner.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/runner.py) / [validate.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/validate.py) | 运行归档与分项门槛；运行器尚未完整绑定同池经验目标 |

模型每家公司股本为 1，P 的模型含义是公司市值，不能把现实每股股价直接与整家公司净资产相除。目前默认 `P0=V0`，属性另行独立抽样；没有逐行的 `P/book/ESG` 联合初始化通路。不要构造市场后再覆盖价格，破坏已有初始持仓和融资暴露。

融资实现是固定暴露、费用计提及相对初始融资费用的价值调整，属于明确假设下的约化形式。没有完整实付融资现金账，不能声称实际支付能力、现实融资节约或一般均衡福利已验证。账面权益代理 V、观测评分代理真实属性也都是模型假设。

## 已完成的验证及保留的失败

| 证据 | 实际结果 | 不能据此推断 |
|---|---|---|
| [初日守恒修复](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/initial_conservation_fix/README.md) | 初始化 `_record(0)` 后补 `_check_conservation(0)`，记录真实浮点残差；当时全量 **801 项通过**，约 84.87 秒 | 最新 book 草稿也通过；该修复解释或消除了价格截断 |
| [2500 日速度](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/performance_2500/README.md) | 1000 投资者 / 200 公司、2500 **总日数**、预热 1200、seed 710101、单 BLAS 线程；初始化加运行 **1.1047123 秒** | 披露、QL、完整遥测或整个实验矩阵也有同样速度；市场已通过 |
| [固定 60 世界](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/audit_report.md) | 记忆参数 .3/.7，各 30 个 seed 710101—710130；1000/200、3500 日、预热 1200；60 档复算与 30 配对通过；机械 **57 PASS / 3 FAIL** | 挑选 .7 为赢家、抹去预热失败、宣布经验校准完成 |
| [16 条固定输入诊断](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/predictor_diagnostic/interpretation.md) | 16×2048 日，8 个配对；其中 8 条调用真实报价组件，共 16,384 次报价；没有完整市场或随机抽样 | 改预测公式一定解决市场反转、截断或政策效果 |
| [共同政策前 QL 小运行核验](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_learning_protocol_checks_20261011/common_prepolicy_smoke/verification.json) | 15 个实际世界，入口与来源工程检查 PASS；来源和 B/T 后续训练覆盖均 FAIL | QL 已充分训练，或者足以比较政策 |
| [信息机制开发解释](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_information_development_20261011_v1/interpretation.md) | 24 场景路径、18 对比较、1,296,720 公司日重建与政策前一致性检查通过 | 信息过程已经验拟合，或得到现实政策因果效应 |
| [通用融资开发路径](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_generality_financing_20261011) | AI-washing 与 WBA 社会代理已验证技术复用 | 完整 M5 研究迁移完成 |

60 世界共 4 次价格截断，全部位于预热：`m30_710101` 第 267 日公司 36；`m30_710112` 第 303 日公司 127 和 157；`m70_710102` 第 1064 日公司 150。测量期零截断不能消除全期门槛失败。两臂价格收益一阶自相关的世界等权均值约 `-.1346575 / +.0122907`，仅为已观察开发结果。

`m30_710107` 原来因第 0 日残差比较口径出现诊断中断，但完整物理路径已留存并独立复算。保持原中断记录；不能凭最小档案伪造缺失的完整结果指纹。

固定输入诊断发现：固定深度时，两种预测写法的脉冲反转相同；深度突变且订单流持续时，当前写法把深度变化计入“意外”冲击。因此需要经济解释与进一步诊断，不能直接把除法次序判成普通程序错误。

原申请书/计划明确要求厚尾、波动聚集、预算、无卖空、守恒及速度。全期零截断、日对数涨跌保护 `.3`、`abs(log(P/V))≤5` 是后来的工程验收/数值保护设定，不是现实涨跌停或已校准阈值。来源区别应说明，不能事后删门槛把 FAIL 改成 PASS。

## 两个未完成的代码断点

### 1. 账面价值接口：已写草稿，尚未验收

仅限定修改 [calibration.py](C:/Users/kanzaler/Desktop/ABM/src/abm/disclosure/calibration.py) 和既有 [test_disclosure_calibration.py](C:/Users/kanzaler/Desktop/ABM/tests/test_disclosure_calibration.py)。已写入 `calibrate_book_csv(...)` 和默认保持 score 的 `--kind score|book` CLI。

草稿按显式公司池与财务截至日筛选，指定企业 ID、币种、金额列、公告日及可知性截止日；拒绝重复企业、选中缺失/非正/非有限账面值、币种混用及超过截止日的公告。至少两个不同企业；相同金额允许 sigma=0。计算原金额单位下 `mu=mean(log(book))`、`sigma=pstdev(log(book))`，只更新 `intrinsic_value_log_sd`。输出纯 `MarketConfig` JSON 与独立来源报告；归一化消去货币尺度，不能称拟合了真实市值或规模—ESG 联合关系。

交接时生产文件已变，新增测试尚未落盘，既有测试未重跑。与 801 项回归绑定的 86 个输入文件比较，当前只有 `src/abm/disclosure/calibration.py` 不同。需先审查日期边界、CLI 旧调用兼容和输入口径，再补最少的实质测试：手算 mu/sigma、只改变目标参数、拒绝重复/币种混用/未来公告/非正值、输出可重新加载、旧 score 调用仍工作。不要顺手实现联合初始化或用单家公司拟合 sigma。

### 2. 订单流重放：方案草稿，尚不能启动

目录：[flow_replay](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_qualification_20261011/flow_replay)。已有 `freeze.json` 和 `run_frozen.py`；**`cases=[]`，缺 `initial_manifest.json`，未运行 `--check-only` 或 `--run`**。

目的：原 60 档没有完整 u / EMA / 暂时冲击状态，不能纯离线构造另一个预测器。计划在相同 52 个旧源文件、60 个原配置/种子上精确重放，只补录逐日 `u=price_impact*submitted_flow/(liquidity_fraction*P)`；调用原报价方法且不改变随机数、订单或状态。新脚本复用已绑定哈希的原 Recorder，不调用会覆盖原档的入口。

预定上限：60 次、每次 3500 日×200 公司；u 的 float64 未压缩总量 336,000,000 字节，新目录最多 900,000,000 字节，最低保留约 15 GiB 空闲。15 分钟是粗略规划，不是实测或硬超时。不得添加测速种子、换参数、重试失败或自动扩大预算。

先补完整原档身份并审查。必须让旧 P/V 及归档数组逐字节相同；第一次不一致即停，保留原因。特别检查 EMA 的乘除运算次序：草稿的 `(1-rho)*u/depth` 与源中的 `(1-rho)*(u/depth)` 可能产生浮点差异；此处仍待核查，不为通过检查而降低旧路径一致性要求。

离线对比统一用 u 单位的预测误差，逐公司计算，再对世界等权汇总，公司不能充当独立实验重复。替换暂时冲击后的 raw 报价只是在实际 P/u/depth/news/inventory 不变时的条件计算，**不是新的完整市场反事实**。报告全期/预热/测量的新增和消失截断；不选赢家、不改默认参数，原 3 个 FAIL 始终保留。

旧冻结源码早于初日守恒修复。不能用当前生产目录替代指定旧源码，再期待所有诊断逐字节相同。

## 公开数据：实际已取得的内容

数据总目录：[reports/disclosure_public_data_20261011](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011)。原始文件在 [data/raw/disclosure_public_20261011](C:/Users/kanzaler/Desktop/ABM/data/raw/disclosure_public_20261011)。

### 沪深 300 与评分

官方成分文件内部日期 2026-10-09，300 个不同证券键，深圳 111、上海 189。处理表：[csi300_constituents_20261009.csv](C:/Users/kanzaler/Desktop/ABM/data/processed/disclosure_public_20261011/csi300_constituents_20261009.csv)。这是当前成分，不证明历史成员、企业唯一性或全 A 股代表性。

[华证采集说明](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/csi300_huazheng_latest/README.md)：按预先固定顺序进行了 123 次新逻辑查询，最后连续 3 次 SSL 连接失败后停止。原表为 119 条评分、5 条失败、176 条未尝试；独立审计仅补入原先已缓存的伊利，得到 **120 条可用评分、5 条失败、175 条未尝试**。可用表：[audited_observations.csv](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/csi300_huazheng_latest/audited_observations.csv)。

120 条中深圳 109、上海 11，全部原生日期标签 2026/09/24；有序停止造成显著选择偏差，不能直接拟合完整股票池。日期标签不是首次公开时间。不要无条件重跑旧采集器覆盖输出；若后续恢复，应另立透明的恢复范围和停止条件并保留原失败。

[方法证据](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/huazheng_method_evidence.json)来自华证 V2.1 官方文件的搜索索引文本，支持 0—100、高分更好；未保存该 PDF 原件，当前接口确切方法版本仍未证实。此前追加下载被自动审批以“超过该子任务一次 PDF 下载范围”拒绝，已停止该追加动作；不要把搜索文本当原件，也不要换工具重试该被拒动作。其他已获授权的财报来源与此不同。

### 伊利当前财务、评分与价格匹配试点

[matched_observations.json](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/yili_current_pilot/matched_observations.json)由 [verify_extract.py](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/yili_current_pilot/verify_extract.py)实际运行生成，提取与金额恒等式检查 PASS，未新增网络请求或拟合参数。半报权益页和回购首页也已渲染查看。

- [2026 半年报原件](https://static.cninfo.com.cn/finalpage/2026-08-27/1225511409.PDF)：财务截至 6 月 30 日，8 月 27 日公告，未经审计，人民币元；归母权益 **53,711,364,981.99**，少数权益 **3,565,015,649.48**，总权益 **57,276,380,631.47**。注意 PDF 页 49 对应打印页 46。
- 半报注册股数 **6,325,360,667 股**；该期其他权益工具、库存股报告为不适用。不能把此数未经事件核对当成任何以后日期的精确股数。
- [10 月 10 日回购进展原件](https://static.cninfo.com.cn/finalpage/2026-10-10/1225598746.PDF)：截至 9 月 30 日尚未实施本轮回购；公告晚于价格日。SSE 原请求返回 HTML 的失败另存，巨潮镜像成功记录在 `share_source_cninfo.json`。
- 华证评分 **91.7 / AA**，原生标签 9 月 24 日，首次公开时间未知。10 月 9 日未复权价 **27.66 元**，上交所与 BaoStock 两个已留存来源一致。
- 若延用 6 月股数，注册总股本口径市值为 **174,959,476,049.22 元**，滞后归母账面/市值约 **0.30699317**；这只是注明股数延用假设的派生值。供应商 PB 一致仅为相容性检查，不能独立证明股数。
- `strict_point_in_time_joint_match_qualified=false`、`empirical_calibration_qualified=false`。不能称已经得到完整同期可知的联合样本，更不能把账面值视作真实内在价值。

### 伊利历史行情已实际取得、已审计

[baostock_yili_pilot](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/baostock_yili_pilot)保存冻结范围、运行回执、两份 CSV、[audit.json](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/baostock_yili_pilot/audit.json)和 `derived_returns.csv`。

2 次逻辑查询，匿名公共接口，证券 `sh.600887`，请求区间 2020-01-01 至 2026-10-09。未复权 flag=3、前复权 flag=2，各 **1,638 行**，实际 2020-01-02 至 2026-10-09，形成 **1,637 个相邻收益**。检查了哈希、两表日期/字段配对、空值、重复日期、有限正价格及最后一天报价；未独立取得交易所完整日历，不能把无空值等同于没有漏交易日。

最后一天价格和成交量 **59,244,547 股**与上交所相同；成交额差 0.21 元，上交所返回整数元。8 日的 `preclose` 与上一交易日实际收盘价不同，已逐日列出，但未逐条公告核对事件类型。

[BaoStock 官方定义](https://www.baostock.com/mainContent?file=stockKData.md)中 `preclose` 在除权除息日可能是交易所参考价；其前复权采用涨跌幅复权约定。原始价格收益、该供应商复权收益和模型“价格变化＋现金股息”的持有人收益不能直接混为同一口径，复权后也不能默认再加一次股息。单只伊利的九矩是描述统计，没有变成正式经验目标或重新调参。

### 其他既有数据

[WBA 校准说明](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_calibration_20261011/README.md)已将 2023 年 1,035 家公司的社会评分转为独立领域经验分布，适合验证通用接口；它不是综合 ESG 真值，更不是 A 股同期联合校准。

[中兴财务试点](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_public_data_20261011/zte_financial_pilot/README.md)已核对 2023 年报和 A/H 股身份。原 WBA ISIN 对应 H 股，不能直接拼 A 股价格；当前 2026 评分不能冒充 2023 观测。该试点市场值仍为空。

[公开历史个股核查](C:/Users/kanzaler/Desktop/ABM/reports/disclosure_market_public_20261011/tsay_source_inspection.md)保存 5 家美国公司、40,130 公司日的教材数据；样本截至 2008 年，选样和幸存者偏差已说明。French 49 是行业组合，与单家公司资产观察单位不同，两者不能直接替代所需 A 股经验目标。公开可取数也不等于开放再分发许可。

## 下一步顺序

1. **先审查 book 草稿并补最少测试。** 当前没有合格的多公司财务样本，不要用伊利一个点估计跨公司离散度。保存本次修改差异，再跑相关测试；旧 801 项只对其归档源码有效。
2. **把同一预先指定公司池的数据口径补齐。** 固定观察日、证券/企业/股类、财务公告可知性、币种/金额单位、注册股数与库存股、评分方法和缺失处理。不得把剩余 120 条评分中的选择偏差掩盖掉；也不能为了凑数直接拼不同年份和定义。
3. **补齐并审查订单流重放草稿，再做检查模式。** 通过哈希、源文件、完整 60 档和磁盘预算核验之后才考虑执行固定预算。检查通过不等于已经重放；任何首个失败都保留，不自动补种子。
4. **按可比经验目标处理市场行为问题。** 分开价格收益与持有人总收益、公司与组合、预热与测量、全期机械约束与统计特征。不能只看厚尾和绝对收益 ACF 就认定价格形成合理，也不能只选 ACF 看起来好的参数。
5. **再推进 QL 覆盖与正式政策比较。** 旧 256 训练＋18 验证批次市场与覆盖均失败；共同政策前 15 世界只验证入口和来源。不盲目增加种子或放松覆盖门槛。区分可行状态、实际访问、已闭合 TD 更新及各规模/阶段覆盖。
6. **最后完成规模、相图与 AI-washing 迁移。** 沿用同一指标、运行与验证链；补研究意义和经验有效性。正式完成 M5 前不要提前修改 README 的总定位，或宣布全部里程碑完成。

正式设计仍为开发草案。主规模 1000/200、3500 日、预热 1200、政策从 1201 日开始；政策主指标是 `mean(g_3500-g_1200)`。相同市场偏好下 B/I/F/IF 的政策前历史应一致；市场偏好从初始化不同的对照另报全期，不能混入相同政策窗口。规模成本默认乘子 `[.6,1,1.6]` 已假定大企业成本优势，需 `[1,1,1]` 对照，不能全归因于市场传导。

本披露研究继续禁用保留编号 `20261101—20261130` 与封存的 `20260901—20260910` 来开发/调参；其中部分号码在旧 ABM 阶段已出现，不能宣称全仓从未使用。正式留出应先核对跨阶段谱系，再冻结新的未观察编号。

## 环境与继续工作时的命令

项目环境：`.venv\Scripts\python.exe`，Python 3.12.9、NumPy 2.5.1。全局 Python 也为 3.12.9，能用 pandas / PyMuPDF，但缺少项目 `duckdb`，不要用全局 Python 跑 `abm`。`pdftotext` 为 `D:\miktex\miktex\bin\x64\pdftotext.exe`。

以下只是供接手执行，**本交接未运行**：

```powershell
Set-Location -LiteralPath 'C:\Users\kanzaler\Desktop\ABM'
.\.venv\Scripts\python.exe -B -m pytest -q tests/test_disclosure_calibration.py
.\.venv\Scripts\python.exe -B -m pytest -q
```

重放草稿补齐和审查后，先运行只检查模式；现在直接运行会因缺失冻结输入失败：

```powershell
.\.venv\Scripts\python.exe -B -X utf8 reports/disclosure_market_qualification_20261011/flow_replay/run_frozen.py --check-only
```

不要重跑 `verify_extract.py`、行情 `audit.py` 或已完成采集器来覆盖现有证据；它们拒绝已存在输出。读取已有回执和哈希即可；如确需修订，另存版本并说明原结果。

读取 XLS 的临时 wheel 位于 `C:\Users\kanzaler\AppData\Local\Temp\abm_xls_reader_20261011`；BaoStock wheel 位于 `C:\Users\kanzaler\AppData\Local\Temp\abm_baostock_reader_20261011`，没有安装成项目依赖。临时目录可能被系统清理，接手不能假定永久存在；对应来源与 SHA 已存报告。

## 仓库与身份记录

工作树不是干净状态。既有跟踪修改包括 `README.md`、`pyproject.toml`、`src/abm/tabular.py`；披露模块、相关测试、配置、数据与报告大部分尚未跟踪。不要执行清理未跟踪文件、整库回滚或将这些文件当作临时垃圾。没有为交接创建提交或远端发布。`git diff` 看不到未跟踪文件内容，需同时核对归档源码和具体文件。

关键身份，均可在对应回执再次验证：

| 文件 / 内容 | SHA-256 |
|---|---|
| 固定 60 世界旧 source.zip | `0763385ed37592e88ef18c41f6ddb3bb76d8ee7df6430071b80429c6beac2ed7` |
| 固定 60 世界 freeze.json | `40e7e7711a1739b1a812c958d79e094bc7fac553642d55da1a7ea07345e4cf74` |
| 伊利半年报 PDF | `423af4d63f2b620a03ed9d0080adbb063f3ef14d874abeca8097d0e0d1441ac2` |
| 伊利 10 月 10 日回购 PDF | `bf56246ba820acaa7e523c884da7f5a09f4da62e3d8235c4ee109e4fc208c2f1` |
| 伊利未复权 CSV | `cc0ba2984f3824b4f9c79b5d0e0c625ed9844868e0ca3a5ca6ad9e301371e99c` |
| 伊利前复权 CSV | `d9b4fce2a6a84c6ba425b1be3597f04c750ac1c8cdb26c4e3913644e207cbd7f` |
| 当前未验收 calibration.py | `382652508f2fcbf4a2020e411d71e941e45f5f6f80c0a9ae76947333ff39a2fa` |
| 尚未新增 book 用例的 test_disclosure_calibration.py | `223e44fe7795fed6dd6a281ca65d598bb5d9c524af57e02eb51a93caa0c33bb2` |
| 未完成 flow_replay/freeze.json | `70708211bac26973b39a5ed3dc632f6965c57f438837cd4c2d9e63b978e46864` |
| 未验收 flow_replay/run_frozen.py | `662bab4725c4cf9820053bbf5a4fca9006ef83063f9059ecfe5b01acfb722a60` |

接手后的第一句状态应明确哪些还没完成，再沿上述断点推进。不要重做已核实的来源试点来代替缺失的公司池匹配，也不要把更多工程报告的产生等同于研究目标达成。
