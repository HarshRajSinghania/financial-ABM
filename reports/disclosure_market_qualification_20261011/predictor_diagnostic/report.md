# 固定预测器公式诊断

公式检查状态：PASS。已存路径16/16；市场运行0、RNG调用0。

外生强制深度/方差隔离了预测器公式；未调用record_returns，不是动态深度市场反事实，也不提供ACF、实证校准或市场稳定性验收。

|输入|memory|预测器|状态|首日raw|次日raw|累计raw|cap|
|---|---:|---|---|---:|---:|---:|---:|
|pulse_depth1|0.3|impact_ema|completed|0.01|-0.0037316399999999996|0.004859999999999984|0|
|pulse_depth1|0.3|flow_ema_current_depth|completed|0.01|-0.0037316399999999996|0.004859999999999984|0|
|pulse_depth_floor|0.3|impact_ema|completed|0.021993333333333333|-0.0124388|0.004860000000000001|0|
|pulse_depth_floor|0.3|flow_ema_current_depth|completed|0.021993333333333333|-0.0124388|0.004860000000000004|0|
|constant_depth_steps|0.3|impact_ema|completed|0.00486|0.004860000000000001|9.953279999999951|0|
|constant_depth_steps|0.3|flow_ema_current_depth|completed|0.00486|0.004860000000000001|9.953280000000149|0|
|zero_depth_steps|0.3|impact_ema|completed|0.0|0.0|0.0|0|
|zero_depth_steps|0.3|flow_ema_current_depth|completed|0.0|0.0|0.0|0|
|pulse_depth1|0.7|impact_ema|completed|0.01|-0.00167564|0.004859999999999985|0|
|pulse_depth1|0.7|flow_ema_current_depth|completed|0.01|-0.00167564|0.004859999999999985|0|
|pulse_depth_floor|0.7|impact_ema|completed|0.021993333333333333|-0.0055854666666666705|0.00485999999999997|0|
|pulse_depth_floor|0.7|flow_ema_current_depth|completed|0.021993333333333333|-0.0055854666666666705|0.00485999999999997|0|
|constant_depth_steps|0.7|impact_ema|completed|0.00486|0.00486|9.953279999999916|0|
|constant_depth_steps|0.7|flow_ema_current_depth|completed|0.00486|0.00486|9.953280000000149|0|
|zero_depth_steps|0.7|impact_ema|completed|0.0|0.0|0.0|0|
|zero_depth_steps|0.7|flow_ema_current_depth|completed|0.0|0.0|0.0|0|

全部raw/clipped、预测器及暂时状态和累计路径见16条预声明NPZ；中断时只保存已观察前缀。配对JSON包含深度独生残差及两个深度切换日。无自动赢家、默认推广、重试或追加。
