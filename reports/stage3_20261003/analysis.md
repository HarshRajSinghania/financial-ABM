# 第三阶段：真实数据、信息因子与实验比较

2026-10-03（Asia/Singapore）。按当前三阶段计划完成第三阶段的本地功能与工程验证。
子代理均使用 GPT-6.1-sol / max。没有调用模型中的 LLM API，没有改动历史正式验收记录。

本次通过的是数据来源、信息时序、开关、守恒、重建和界面契约；不等于真实市场校准、
因果效应估计或当前源码的一阶段正式统计验收。历史 v15 的 22/22 仍只对应其冻结源码。

## 已完成的步骤

| 内容 | 验证结果 | 证据 |
| --- | --- | --- |
| 原始数据快照 | SEC、ALFRED、Alpha Vantage 示例、13F 四类真实样本；下载元数据及全部文件哈希核对通过 | `data_verification.json` |
| SEC 信息因子 | 原始文件、来源时间、实际进入会话时间可追溯；下一会话进入，传播到 500 名交易者 | `final_run_verification.json` |
| 独立开关 | 规则订单、Bandit、企业 Q、图、因子各可关闭；停用三阶段恢复旧执行路径 | `tests/test_stage3.py` |
| 规模与守恒 | 500 个规则 Agent × 252 个日频会话；价格正值、现金非负、无截断命中 | `rules_final_run.txt` |
| 归档重建 | 源码与输入共 34 个哈希一致；最终运行重建后完整指纹相同 | `rebuild_final_run.txt`、`final_run_verification.json` |
| 日志与回放 | 252 条 JSONL、Parquet、DuckDB 遥测逐条相同；无未来到达消息 | `final_run_verification.json` |
| 完整 Python 回归 | **323 passed**，退出码 0；1 条已有 FastAPI/httpx 弃用提示 | `tests_final.txt`、`tests_final.xml` |
| 前端 | 12 项测试、构建、静态检查；浏览器比较、筛选、回放和导出检查 | `web-tests.txt`、`web-build.txt`、`web-lint.txt`、`comparison-browser-check.json` |

新增测试覆盖错误输入不遗留空日志、失败记录写入出错仍通知界面、重建前拒绝篡改、
原始输入删除后用归档重建，以及显示队列已满时持久化事件不丢失。修复限于这些新功能所需路径。

## 真实样本与时间边界

| 数据 | 本地快照 | 实际验证范围 |
| --- | --- | --- |
| SEC 8-K | `data/raw/sec/20261002T172220Z/` | 原始索引与正文，accession `0001384905-24-000043` |
| ALFRED GDP | `data/raw/alfred/20261002T172555Z/` | 17 条，历史版本 `2024-07-15`，列名 `GDP_20240715` |
| Alpha Vantage IBM | `data/raw/alpha_vantage/20261002T172555Z/` | 官方公开 demo 的 100 条原始日线，2026-05-11 至 2026-10-01 |
| SEC 13F | `data/raw/sec_13f/20261002T172658Z/` | 1,944 条持股记录，报告期 2026-03-31，接受时间 2026-05-15 |

上述路径以仓库根目录为起点。快照记录原始响应、下载 UTC 时间、来源 URL、版本、
时间范围和 SHA256，写入接口拒绝覆盖已有目录。`data/prepared/sec_8k_factor_events.json`
由 SEC 元数据产生，运行归档包含原始文件和准备后的事件。

SEC 示例的[官方索引](https://www.sec.gov/Archives/edgar/data/1384905/000138490524000043/0001384905-24-000043-index.html)
给出接受时间 2024-08-01 16:33:57，核对为 UTC−04:00，即 20:33:57 UTC。
示例截止点为 20:00 UTC，事件在 **2024-08-02 20:00 UTC** 的第 2 会话进入模型，
随后按图的延迟与信任传播。第 1 会话与因子关闭对照的价格一致，第 2 会话开始出现差异。

接受时间是公开可用时间的代理，未独立测量网页传播延迟。`available_at` 保留该来源时间，
`session_available_at` 记录进入模型的时点。事件来源和原始 accession 保留在消息中。
文件对应的公司映射为示例 `company-0`，不代表模拟资产已经匹配该公司的真实价格或资产负债表。

`log_change=0.01` 是人为给定的信息冲击参数，未从文件内容估计，不是实际公告收益率。
该参数通过公开信息、交易者观察及报价通道作用，不直接改写投资者现金或持仓。
首个插件只实现 `information` 渠道；其他渠道明确报错，未冒充已实现基本面、偏好或监管插件。

ALFRED 的[历史版本 CSV](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=GDP&vintage_date=2024-07-15&cosd=2020-01-01&coed=2024-07-15)
只提供日期级 vintage，未填造盘中发布时间。Alpha Vantage 样本来自[官方示例文档](https://www.alphavantage.co/documentation/)，
是未调整日线，不是完整市场历史或幸存者偏差已处理的数据。
[13F 原始信息表](https://www.sec.gov/Archives/edgar/data/869178/000093041326001636/infotable.xml)
只转换成机构—证券持股记录，不进入社交、信任或信息传播网络。

SEC REST submissions 实网请求返回 403；companyfacts、FRED JSON 与生产 Alpha Vantage
接口目前通过夹具验证，不能声称其生产凭据路径已完成实网验证。此次 ALFRED CSV、Alpha Vantage
demo 和 SEC 文件下载均来自官方公开入口。CRSP/WRDS 仍需获授权账户；可选 EPA 未接入。

## 运行与对照

最终默认配置为 `configs/stage3.json`，种子 20261003，500 个规则 Agent，企业学习与 Bandit
关闭，图与信息因子开启。252 个会话从 2024-08-01 到 2025-07-18，默认只跳过周末，
固定使用 20:00 UTC，标记为 `synthetic_weekdays_fixed_offset`。这是模拟年度；真实交易所
假日、夏令时和提前收市须通过显式 `session_dates` 配置，当前示例没有声称采用真实交易日历。

| 运行 | 种子 | 因子 / 图 / 学习 | 期末模拟价格 |
| --- | ---: | --- | ---: |
| `stage3_rules_final_20261003` | 20261003 | 开 / 开 / 关 | 111.745997 |
| `stage3_factor_off_20261003` | 20261003 | 关 / 开 / 关 | 110.691626 |
| `stage3_graph_off_20261003` | 20261003 | 开 / 关 / 关 | 111.780067 |
| `stage3_learning_20261003` | 20261003 | 开 / 开 / 开 | 144.850180 |
| `stage3_seed2_20261003` | 20261004 | 开 / 开 / 关 | 131.577762 |
| `stage3_seed3_20261003` | 20261005 | 开 / 开 / 关 | 80.330506 |

所有运行均完成 500 人 × 252 会话，截断命中为 0。学习运行完成 12 个 Bandit 窗口和
4 个企业 Q 窗口。上述单条结果和三个种子用于功能对照，不足以证明学习提高收益或给出
稳定的经济效应；它们也没有替代预注册多种子统计实验。

最终规则运行最大现金误差 `8.940696716308594e-8`，最大股份误差 `7.275957614183426e-11`。
其市场指纹为 `79d3868381d063e6a4495c9edc0115697589f31c80df4469ec841c35c1ac136c`。
最终完整运行及重建指纹均为：

`e7dad050ec0b58e7dd94ffb53bcb63ac95620b1b3afc04c08fc04cce8e2628bf`

对照批次先于最后的“初始化校验后才创建日志”修复完成，保留其各自源码归档与指纹，
不覆盖旧产物。最终源码已重跑规则规模运行，并核实所有状态数组与修复前逐项精确一致；
最终重建也在当前源码上通过。历史对照的源码身份不同，重建时需使用其自己的归档源码。
详见 `scenario_runs.json`、`final_run_verification.json`。

新重建入口只处理已启用三阶段且完成的运行。它验证配置、种子、全部数据/源码哈希和结果指纹；
当前源码不匹配时拒绝自动执行旧源码。恢复归档源码应在独立工作目录进行。失败的运行保留
起止时间和错误记录，不声称可以从中途恢复学习状态，也不保证跨数值平台的原始字节指纹相同。

## 比较界面与导出

在本地 Web 的 **Analysis / 分析** 页面选择多个已完成实验，可按指标、仿真天数区间及
回放截止点比较。共用纵坐标，缺失值保留为空白；导出的 CSV/JSON 保存种子、配置与指纹。
已有单运行的策略和守恒图仍保留。

实际浏览器检查使用本地真实 Stage 3 运行，核对导出值与保存的遥测一致；中英文切换、
回放推进、390px 手机布局和控制台检查均通过。PNG 和 SVG 动画均实际打开验证；
SVG 是从左到右循环揭示已筛选曲线的动画，不是视频录像或新的模拟轨迹。

- 图片：`comparison-export.png`
- 动画：`comparison-animation.svg`
- 筛选数据：`comparison-filtered.csv`、`comparison-filtered.json`
- 浏览器记录：`comparison-browser-check.json`；首末帧 `animation-first-frame.png`、`animation-last-frame.png`
- 桌面/手机截图：`comparison-en.png`、`comparison-zh.png`、`comparison-mobile.png`

## 复现入口

在仓库根目录使用已有虚拟环境，输出目录必须是新目录：

```powershell
.\.venv\Scripts\python.exe -m abm.runner --config configs/stage3.json --output runs/my_stage3
.\.venv\Scripts\python.exe -m abm.runner --rebuild runs/my_stage3 --output runs/my_stage3_rebuilt
.\.venv\Scripts\python.exe -m abm.data_sources --help
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m abm.web --open
```

前端构建和使用方法见根目录 `OPERATIONS.md`。PPO 启用条件尚未满足，未添加 PPO、
多资产或 LLM Agent，也未部署公网服务。
