# WBA 公开 CSI 数据接入与质量报告

状态：原始文件已获取，CSV 已解析并核对；未进行 ABM 参数估计，未匹配 SEC 财务。日期：2026-10-11。用户已授权在导师数据尚未确定时先使用公开数据推进。本次只写入指定的 raw、processed、reports 三个目录。

## 来源、版本与许可

来源为 [WBA 官方数据页](https://www.worldbenchmarkingalliance.org/latest/core-social-indicator-assessments-2000-largest-and-most-influential-companies-globally) 的公开 Excel 下载。页面日期为 2024-04-17，文件名注明 April 2024 version 2，工作簿内部修改时间为 2024-04-08T10:33:57Z。URL 中的 2026-07 及服务器 2026-07-01 修改时间是托管信息，不能改写为 2026 年评估。

- 文件：data/raw/disclosure_public_20261011/wba_csi_assessments_2021_2023_april2024_v2.xlsx。
- 下载完成 UTC：2026-10-11T07:08:28.6588013Z；官方服务器响应日期：2026-10-11T07:08:26Z。
- 大小：17,540,532 bytes。
- SHA-256：6e94e0d739c5efc69a86e1b9d70e8480bad66e6521b9287a1feb0f613f13abda。

工作簿 Introduction!B23 及 [WBA 版权说明](https://www.worldbenchmarkingalliance.org/disclaimer) 标为 CC BY 4.0。使用时注明 World Benchmarking Alliance、原始链接、版本与本次转换；保留来源，转换没有获得 WBA 的认可背书。

常规下载最初出现 TLS 失败和 HTTP 520；标准下载客户端随后从同一公开链接取得 HTTP 200。没有登录、注册、发信或使用联系邮箱。原始 HTTP 响应和来源清单保留在 raw 目录。

## 工作簿与解析结果

| 原表 | 输出 | 记录/行数 | 用途 |
|---|---|---:|---|
| 1. Introduction | introduction_grid.csv | 24 | 说明、评分和许可；保留 Excel 行列位置 |
| 2. Methodology | methodology_grid.csv | 52 | 指标与元素说明；保留 Excel 行列位置 |
| 3. Latest indicator scores | latest_indicator_scores.csv | 1,728 | 公司元数据、18 个指标及总分，共 26 原字段 |
| 4. Latest element scores | latest_element_scores.csv | 1,728 | 公司元数据、指标分数与 46 个元素，共 72 原字段 |
| 5. Latest full assessment | latest_full_assessment.csv | 79,488 | 公司×元素评分、说明与证据，共 10 原字段 |

所有表均为可见表。数据 CSV 使用原表表头，包括尾随空格；没有改列名、填缺失、纠错或去重。前两表加 `_excel_row` 与列字母以保留说明的位置；数据表上方的合并标题、原行号规则及隐藏信息写入 workbook_structure.json。CSV 为 UTF-8 BOM，数字保留 XML 原值；富文本只保留文字，合并格式和公式另存。当前文件没有公式、缺缓存公式或 Excel 错误值。原 Excel 是完整原件。

原件 ZIP CRC、CSV 记录数及以下数据关系已核对：

- 1,728 个唯一 WBA ID；没有重复 WBA ID 或规范化公司名。
- 两张评分表共有字段逐值一致，差异为 0。
- 总分等于 18 个原始指标列之和，差异为 0。CSI 4 和 CSI 5 的列已含双权重，不再乘二。
- 长表的 `(WBA ID, Year, Indicator element)` 79,488 个键均唯一，每家 46 个元素；分数和年份与元素宽表一致，差异为 0。
- 所有指标分数在说明的边界内；总分理论范围 0—20，观测范围 0—15.5。

## 年份、样本与缺失

本文件已按 WBA 的规则只保留每家公司的最近一次 CSI 评估。它是混合评估年份的最新记录集，既不是各公司 2021—2023 的面板，也不是同年截面。不能用年均分之差推断公司进步。

| 评估年份 | 公司数 | 总分均值 | 总分总体 SD | 中位数 |
|---|---:|---:|---:|---:|
| 2021 | 51 | 4.1078 | 3.4773 | 3.5 |
| 2022 | 642 | 3.8248 | 3.1603 | 3.5 |
| 2023 | 1,035 | 5.3855 | 3.8593 | 5.0 |
| 混合年份，仅作描述 | 1,728 | 4.7679 | 3.6824 | 4.5 |

样本涉及 82 个国家、38 个行业。它是 WBA 选取的大型或有影响力机构，不代表上市公司随机总体，包含不同法律与经营实体。源表没有 benchmark membership 字段；方法页明确金融系统基准对 CSI 3 和 5a 有不同要求。选定年份后仍须核对基准与实体可比性。

公司表仅 ISIN 列有空白：394/1,728（22.80%）；其余公司元数据和评分未见空白。ISIN 非空 1,334 行、唯一值 1,320 个。不能用没有 ISIN 推断没有上市。

| 标识问题 | 数量 | 处理 |
|---|---:|---|
| ISIN 空白 | 394 行 | 保留空白，不补造编号 |
| ISIN 格式或校验异常 | 2 行 | 原值保留、单列待核实 |
| 非空 ISIN 重复 | 5 组、19 行 | 禁止直接一对一合并 |

两条异常原值为 Aldi Süd 的 DEXXXXXALDI0、Bidcorp 的 ZAE 000216537。重复值 CA92143B1004 同时出现于 11 家不同名称公司；其余四组各有两家。合法校验位也不证明编号确实属于该法律实体。完整问题行见 identifier_issues.csv；未经核实，不把重复值直接认定为同一集团或自动删除。

长表分数包括 Met=17,474、Unmet=61,657、Not Applicable=344、Partially Met=13。Not Applicable 是原评估状态，不能变成零分或任意缺失。证据文本空白 39,957 行、Reference 空白 33,009 行、Link 空白 32,745 行、Explanation 空白 264 行；空证据与 Unmet 不是同一个概念。本次不爬取证据链接，也不将长表文字当作独立审计真值。

## 能用于什么

在明确限定为社会维度并选好年份、机构与基准后，可以用评分离散分布、零分质量、分位数和元素状态作为初始化分布的候选经验依据。2023 年有 1,035 条评分，但可成功匹配的上市企业数量尚未核实。当前配置仍未改变，以上没有自动写回 ESG 均值、标准差或成本参数。

CSI 覆盖人权、体面工作和商业道德。它不是环境—社会—治理的综合 ESG 分，也不是潜在真实能力、实际违规或虚报幅度。评分基于披露和证据，信息缺口本身可能影响得分。不能据此估计真实改善成本、漂绿成本、审计概率、信息政策效果、自然衰减、投资者偏好或融资传导；这些需要另外的数据、识别或透明的假设。

不采用将 CSI 线性放大为 0—100 后称综合 ESG 的做法，不把混合年度均值当作历史趋势，不由缺失 ISIN 推断私人企业。后续 SEC 匹配和财务抽取规则见 sec_access_plan.md。

## 复现与审查

本目录的 fetch_public_sources.ps1 记录官方链接和下载元数据；已有本地文件只更新清单，不覆写原件。parse_wba_csi.py 仅使用 Python 标准库，核验固定原件哈希后解析、生成质量摘要及 output_manifest.json。运行方式：在仓库根目录用可用 Python 执行 reports/disclosure_public_data_20261011/parse_wba_csi.py。

quality_summary.json 是完整结构化统计，column_quality.csv 给出原字段空白和常见值，workbook_structure.json 保留各表结构，output_manifest.json 记录原始文件、解析代码、报告与输出的 SHA-256。清单自身不递归哈希。SEC 文档已通过网页工具核实；本地下载收到 HTTP 403，未获得相应 HTML 原件，不能冒充已保存成功。

验收范围是数据获取、保真解析与质量审查。研究校准、CIK 实体确认、财务匹配、融资机制与正式结果均保持未完成。
