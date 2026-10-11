# Stage 1 mechanism validation

- Protocol: `stage1-mechanism-development-v9`
- Frozen seeds: `20`
- Decision: `FAIL`

## Gate checks

- [x] `full_runs_without_price_cap`
- [x] `cash_conservation`
- [x] `share_conservation`
- [x] `full_volatility_in_daily_range`
- [x] `full_return_autocorrelation_near_zero_across_lags`
- [x] `full_volatility_clustering_has_decay`
- [x] `full_heavier_than_gaussian`
- [x] `endogenous_liquidity_feedback_increases_tail_weight`
- [x] `full_volume_volatility_relation_positive`
- [ ] `full_price_discovery_bounded`
- [x] `public_news_channel_has_paired_price_response`
- [x] `agent_information_channel_has_paired_price_response`
- [x] `empty_information_baseline_is_weakest_discovery`
- [x] `single_strategy_markets_remain_active`
- [x] `ablations_avoid_pathological_return_predictability`
- [x] `fixed_population_has_no_strategy_turnover`
- [x] `logit_imitation_fires_and_tracks_fitness`
- [x] `logit_market_remains_active_and_bounded`
- [x] `persistent_order_flow_is_observable`
- [x] `spread_and_depth_are_finite`
- [x] `liquidity_stress_increases_clustering`
- [x] `garch_control_is_labelled_exogenous`

## Gate evidence

| Check | Observed | Threshold | Pass rate | Failed seeds |
|---|---:|---:|---:|---|
| `full_volatility_in_daily_range` | `0.021827130295302144` | `{"maximum": 0.03, "minimum": 0.005}` | 100.0% | none |
| `full_return_autocorrelation_near_zero_across_lags` | `0.1485240302439142` | `0.2` | 100.0% | none |
| `full_volatility_clustering_has_decay` | `0.23515861869905363` | `0.03` | 100.0% | none |
| `full_heavier_than_gaussian` | `2.4787111654465277` | `0.1` | 100.0% | none |
| `full_volume_volatility_relation_positive` | `0.31799426564714733` | `0.05` | 100.0% | none |
| `full_price_discovery_bounded` | `0.07455443445114751` | `0.1` | 60.0% | 20261102, 20261104, 20261106, 20261107, 20261113, 20261115, 20261116, 20261117 |
| `endogenous_liquidity_feedback_increases_tail_weight` | `2.180365220897449` | `0.05` | 100.0% | none |
| `public_news_marginal_response` | `10.417753226941544` | `1.0` | 100.0% | none |
| `public_news_independent_response` | `8.323273460607123` | `1.0` | 100.0% | none |
| `agent_information_marginal_response` | `1.3789055955030554` | `1.0` | 80.0% | 20261102, 20261104, 20261106, 20261117 |
| `agent_information_independent_response` | `1.0671247161424895` | `1.0` | 80.0% | 20261103, 20261111, 20261112, 20261118 |
| `empty_information_baseline_is_weakest_discovery` | `10.582735603655628` | `1.0` | 100.0% | none |
| `value_only_remains_active` | `0.01275286569889459` | `0.001` | 100.0% | none |
| `trend_only_remains_active` | `0.03041797455506492` | `0.002` | 100.0% | none |
| `noise_only_remains_active` | `0.019557438874928695` | `0.003` | 100.0% | none |
| `value_only_avoids_pathological_return_predictability` | `0.08801910395953064` | `0.25` | 100.0% | none |
| `trend_only_avoids_pathological_return_predictability` | `0.001592614347418223` | `0.25` | 100.0% | none |
| `noise_only_avoids_pathological_return_predictability` | `0.010230802440346217` | `0.25` | 100.0% | none |
| `independent_signals_avoids_pathological_return_predictability` | `0.06573628047350527` | `0.25` | 100.0% | none |
| `fixed_participation_avoids_pathological_return_predictability` | `0.07584373506029818` | `0.25` | 100.0% | none |
| `fixed_liquidity_avoids_pathological_return_predictability` | `0.020584403329060925` | `0.25` | 100.0% | none |
| `liquidity_stress_avoids_pathological_return_predictability` | `0.1328585131079199` | `0.25` | 100.0% | none |
| `spread_and_depth_are_finite` | `7.130431179596123` | `{"maximum": 25.0, "minimum": 1.0}` | 100.0% | none |
| `liquidity_stress_increases_clustering` | `0.14116389748346325` | `0.0` | 100.0% | none |
| `logit_imitation_fires_and_tracks_fitness` | `6300.0` | `150.0` | 100.0% | none |
| `logit_market_remains_active_and_bounded` | `0.026614514350848613` | `{"maximum": 0.04, "minimum": 0.005}` | 100.0% | none |
| `persistent_order_flow_is_observable` | `0.4417629470424885` | `0.05` | 100.0% | none |

## Scenario medians

| Scenario | Volatility | Return ACF | |Return| ACF | Excess kurtosis | Volume-|return| corr | Price gap |
|---|---:|---:|---:|---:|---:|---:|
| full | 0.021827 | -0.035669 | 0.235159 | 2.478711 | 0.317994 | 0.074554 |
| no_direct_news | 0.017781 | -0.023458 | 0.562875 | 13.810098 | 0.738095 | 0.795251 |
| no_agent_information | 0.021842 | 0.007942 | 0.236692 | 2.408188 | 0.329740 | 0.091001 |
| no_information_channels | 0.018418 | 0.005176 | 0.558292 | 14.046157 | 0.739674 | 0.812486 |
| value_only | 0.012753 | -0.088019 | 0.043463 | 0.164572 | 0.183097 | 0.059775 |
| trend_only | 0.030418 | -0.001593 | 0.447789 | 14.578236 | 0.589636 | 0.108315 |
| noise_only | 0.019557 | 0.010231 | 0.339084 | 14.928455 | 0.590209 | 0.135768 |
| no_logit | 0.021827 | -0.035669 | 0.235159 | 2.478711 | 0.317994 | 0.074554 |
| no_activity_persistence | 0.021875 | -0.034603 | 0.228951 | 2.366523 | 0.313551 | 0.070548 |
| independent_signals | 0.012031 | -0.065736 | 0.032297 | 0.077386 | 0.025054 | 0.127601 |
| fixed_participation | 0.022857 | -0.075844 | 0.162251 | 1.463722 | 0.274269 | 0.085957 |
| fixed_liquidity | 0.018131 | -0.020584 | 0.078982 | 0.259014 | 0.161674 | 0.078372 |
| liquidity_stress | 0.036132 | -0.132859 | 0.378324 | 4.732928 | 0.528481 | 0.071243 |
| concentrated_wealth | 0.022105 | -0.034549 | 0.229826 | 2.593717 | 0.316251 | 0.090923 |
| garch_t_control | 0.021832 | -0.053415 | 0.351602 | 5.367208 | 0.427045 | 0.086285 |
| logit_learning | 0.026615 | 0.078190 | 0.280091 | 3.143817 | 0.398151 | 0.082184 |

## Full-market structural metrics

| Metric | Median |
|---|---:|
| Maximum absolute return ACF, lags 1–20 | 0.148524 |
| Absolute-return ACF(5) | 0.225544 |
| Absolute-return ACF(20) | 0.066850 |
| Absolute-return ACF(50) | -0.054388 |
| Volume ACF(1) | 0.884830 |
| OFI ACF(1) | 0.441763 |
| OFI-return correlation | 0.572149 |
| Mean spread (bps) | 7.130431 |
| Three-sigma tail fraction | 0.011800 |
| Return skewness | -0.012612 |
| Leverage correlation, r(t) vs |r|(t+1) | 0.007860 |
| Crash-day fraction, r < -5% | 0.017400 |
| Bubble-day fraction, log gap > 10% | 0.000000 |
| Maximum drawdown | 0.391466 |
| Final wealth Gini | 0.224782 |

The GARCH-t scenario is an explicitly exogenous stress control. It is not counted as evidence that Agent interaction generated fat tails or volatility clustering.
