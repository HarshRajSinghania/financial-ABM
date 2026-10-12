# 双反馈：固定12世界开发诊断

预定12世界，完成12；全部世界机械通过=False，逐公司价格厚尾/absACF通过=False。收益ACF、跨资产相关及经验校准仍pending。没有选赢家或改变默认参数。

|种子|臂|状态|cap(全期)|机械|价格stylized|
|---:|---|---|---:|---|---|
|27001|current|completed|1|FAIL|PASS|
|27001|no_noise_volatility_feedback|completed|0|PASS|PASS|
|27001|no_depth_volatility_feedback|completed|0|PASS|FAIL|
|27001|neither_volatility_feedback|completed|0|PASS|FAIL|
|27304|current|completed|7|FAIL|PASS|
|27304|no_noise_volatility_feedback|completed|0|PASS|PASS|
|27304|no_depth_volatility_feedback|completed|0|PASS|FAIL|
|27304|neither_volatility_feedback|completed|0|PASS|FAIL|
|27305|current|completed|2|FAIL|PASS|
|27305|no_noise_volatility_feedback|completed|0|PASS|PASS|
|27305|no_depth_volatility_feedback|completed|0|PASS|FAIL|
|27305|neither_volatility_feedback|completed|0|PASS|FAIL|

下表为各公司的矩先在世界内等权，再对三个种子等权。只有该臂三世界全部完成才提供均值；所有公司分布、失败明细和逐seed差值在summary.json。机械及stylized门槛按所有世界/资产/日取AND，不以均值验收。

|含外部分红的矩|current|no_noise_volatility_feedback|no_depth_volatility_feedback|neither_volatility_feedback|
|---|---:|---:|---:|---:|
|daily_volatility|0.02021746|0.01530609|0.01272043|0.01266278|
|excess_kurtosis|13.83295|1.38662|0.1808603|0.1687679|
|return_acf_1|-0.1403303|-0.1766347|-0.09914889|-0.1074312|
|abs_return_acf_1|0.3816094|0.1013108|0.05047707|0.0310273|
|abs_return_acf_5|0.3259866|0.05619325|0.02061319|0.00114925|
|abs_return_acf_20|0.3004261|0.05266634|0.003664825|-0.004028876|
|quantile_01|-0.06530112|-0.03842547|-0.02987434|-0.02947094|
|quantile_99|0.05447773|0.03562409|0.02964811|0.02940459|
|hill_tail_index|2.949143|5.163283|6.683677|6.543916|

每份NPZ保存完整价格/V、价格与含外部分红收益、30公司九矩、逐公司日深度/波动/报价分项/提交与执行流、噪声创新和库存修正、逐公司股份误差与现金账。失败仅保存已完成前缀及明确标记的部分失败日；未将未初始化未来行当作数据。

基线来自已核验的seed27001冻结source.zip，隔离副本及全部源码hash绑定freeze.json；full config只改两个预设反馈开关及seed，bare不运行企业/II/学习。三种子已在失败诊断中见过，本次不是独立验收样本，也不能替代1000/200规模或公开个股数据校准。价格收益与含外部分红收益口径分列；未增加虚构的除息调整。

静态depth=1分解仅用于提出机制假设，不等于本次路径结果。关闭反馈可能削弱波动/尾部，即使无cap或某个ACF接近也不能提升默认值；以前72次调memory的未解决矩差距仍保留。所有臂、失败和预热期cap均报告，不追加种子/候选或自动选胜者。原274档机械和覆盖FAIL不被本诊断改写。
