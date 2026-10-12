# 公开来源核查与口径选择

当前已落实两件事：给既有French训练摘要增加明确的模拟组合观察算子；另保存芝大作者公开的5个个股日总收益样本。前者仍是匿名小篮子，后者仍是教材便利样本，均不能标为代表性个股市场的正式校准通过。

| 来源 | 核查结论 | 当前用途或缺口 |
|---|---|---|
| [French 49官方说明](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html) | 按SIC重构的行业投资组合 | 只读旧29行业训练摘要；模拟篮子没有行业结构，不能冒充SIC行业 |
| [Tsay芝大作者配套数据](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)与[Wiley官方章节](https://catalogimages.wiley.com/images/db/pdf/9780470414354.excerpt.pdf) | 5家公司，40,130个公司日；章节明确含股息，单位与样本数核验通过 | 可做个股口径开发检查；样本非随机，止于2008年；再分发许可未明确 |
| [SEC MIDAS方法](https://www.sec.gov/featured-topics/market-structure-analytics/market-activity-report-methodology) | 包含CRSP closing price变量，不能断言“没有日价” | 实际下载字段、复权、分红和退市处理未核实，尚不能构成日总收益 |
| [Nasdaq历史报价](https://www.nasdaq.com/market-activity/quotes/historical) | 有公开个股价格页面 | 不等于完整历史总体或明确含股息的开放批量面板 |
| [SHARADAR SEP说明](https://data.nasdaq.com/databases/SEP/documentation?anchor=sample-data) | 完整产品付费，免费样本有限 | 未创建账号或下载，不作为无账号完整数据 |
| [FINC585仓库](https://github.com/joseparreiras/finc585) | README实际指向dsi指数表 | 观察单位错误，不当成个股样本 |
| [JKP作者访问指南](https://jkpfactors.com/ctf/dataset-access) | 个股日收益表存在，但要求WRDS和CRSP权限 | 公开因子收益与个股数据访问应分开；没有账号数据冒充公开原始面板 |
| [猪企事件研究复制包V3](https://data.mendeley.com/datasets/tn56tsgpnh/3) | 25家事件/行业筛选公司；落地页可读 | 匿名文件清单请求403；未下载，含股息/复权字段仍待查，未绕过限制 |

原始作者文件、官方章节口径证据和下载哈希在新raw目录；提取的公司日面板及模拟路径在新processed目录。完整逐来源证据、许可状态和局限在public_sources.json；下载与转换核查在tsay_source_inspection.md/json及fetch_tsay.py。

许可应区分公开访问、学术研究使用和重新发布。Tsay作者提供无需账号的下载，但未找到明确开放再分发条款；不从公开URL推导CRSP原始数据可自由发布。JKP分发数据标CC BY-NC 4.0，但其个股接口仍要求底层数据库权限。事件包V2标CC BY 4.0，不能据此凭空确认尚未下载的V3文件和Yahoo调整定义。

本轮唯一市场运行仅验收固定观察操作。9矩公司均值与组合均值有实质差异，聚合并未自动修复负ACF；这不是按旧目标选择分组的理由。下一步应先决定可辩护的研究总体：如使用这5家，只能明确为历史教学样本开发研究；如主张代表性个股校准，应获取有许可、永久ID、退市覆盖和分红定义的更全面面板，并在看留出数据前冻结筛选、时间窗和全部矩门槛。
