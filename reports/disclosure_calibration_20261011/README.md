# 通用 CSV 领域分布接入

状态：CSV 到经验分布配置的接入已实现；仅校准观测代理的初始边际分布，其他经济参数未识别。默认 esg.json 未修改。WBA 原件与保真 CSV 的来源、许可及标识问题仍见 ../disclosure_public_data_20261011/README.md。

## 接口与默认兼容

入口为 `python -m abm.disclosure.calibration`。必须显式给出 CSV 数值列、年份筛选或 `--all-rows`、理论上下界、方向、单位、领域名及属性名称。非分布参数从指定领域模板继承，并逐项列为假设；模板中的领域动作文字不跨领域自动继承。

DomainSpec 仅新增可选 initial_empirical_distribution，为 `(原始分值, 出现次数)`。非空时按频数有放回抽样，再映射到 goodness；空值时使用原来的截断正态抽样，旧领域序列化不新增空字段。经验分布的 initial_mean 和 initial_sd 必须与频数加权总体矩一致，否则拒绝配置。

goodness = direction × (raw - fixed_initial_mean) / fixed_initial_sd。初始 SD 固定为观测样本总体 SD，不能随每日状态或抽中的公司再估计。direction=-1 时方向反转，理论上下界仍为原始单位。抽样维持离散支持与零质量；有限数量公司样本的实际频数仍有随机波动，不承诺每条路径严格复制原样本比例。

CSV 表头按原值精确指定，不自动把其他列猜成评分。选中样本的空白评分可排除且计数；非数值、非有限或理论边界外评分直接报错；重复表头、缺列、没有有效队列及零方差队列也报错。不会静默修补异常、改用其他年份或把 Not Applicable 变成零。

## WBA 2023 演示

使用 latest_indicator_scores.csv，数值列 `CSI Total (out of 20)`，年份列 `YEAR `（末尾有一个空格），筛选 `2023`。理论边界 0—20、方向 +1；这些是显式领域映射，不是由观测最大值推定。

| 项目 | 结果 |
|---|---:|
| 原公司记录 | 1,728 |
| 年份不符排除 | 693 |
| 入选评分缺失 | 0 |
| 纳入 | 1,035 |
| 离散支持个数 | 32 |
| 观测范围 | 0—15.5 |
| 总体均值 | 5.385507246376812 |
| 固定总体 SD | 3.8592611002995967 |
| 零分频数 | 128（12.3671%） |

输出为 configs/domains/wba_social_2023.json；详细来源、CSV/Excel 哈希、筛选、样本统计、代码与输出哈希及未识别参数见本目录 wba_social_2023_calibration.json。

调用示例如下。入口拒绝覆盖已有输出；再次复现时为两个输出选择新文件名。

```powershell
python -m abm.disclosure.calibration `
  --csv data/processed/disclosure_public_20261011/latest_indicator_scores.csv `
  --value-column 'CSI Total (out of 20)' --year-column 'YEAR ' --year 2023 `
  --raw-lower 0 --raw-upper 20 --direction 1 `
  --unit 'CSI social observed proxy points, 0-20' `
  --name wba_social_2023 --attribute-label 'WBA CSI social observed proxy' `
  --template configs/domains/esg.json `
  --source-url 'https://www.worldbenchmarkingalliance.org/latest/core-social-indicator-assessments-2000-largest-and-most-influential-companies-globally' `
  --raw-source data/raw/disclosure_public_20261011/wba_csi_assessments_2021_2023_april2024_v2.xlsx `
  --output-domain configs/domains/wba_social_2023.json `
  --report reports/disclosure_calibration_20261011/wba_social_2023_calibration.json
```

## 研究边界

WBA CSI 是社会维度的公开证据评分代理。把这些分数初始化为模拟的 true state，并设初始 inflation=0，是显式假设；数据没有识别真实能力与夸大披露的分解，也不能称真实综合 ESG 已校准。

这次没有拟合公司身份、规模—评分联合分布或纵向变化。2023 年队列仍来自不同基准，金融系统基准存在不同元素要求，不能仅因年份相同便宣称方法完全可比。未用 ISIN 自动匹配公司或 SEC 财务。

成本水平与离散度、规模乘子、自然衰减、成本弹性、行动容量、虚报成本比、实施与披露延迟、核查、罚金、透明度和补贴均继承模板假设。投资者偏好、学习、价格冲击、融资传导和政策因果作用也没有由此数据识别。

边界映射、正负方向、可重现、离散支持与零质量、默认行为兼容、误选列/年份、缺失和异常处理及 CLI 来源输出均有对应测试。测试通过证明实现符合这些规则，不证明其经济假设或政策结论成立。
