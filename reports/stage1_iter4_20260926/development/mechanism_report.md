# Stage 1 mechanism validation

- Protocol: `stage1-mechanism-development-v11`
- Frozen seeds: `20`
- Decision: `FAIL`

## Gate checks

- [x] `full_runs_without_price_cap`
- [x] `cash_conservation`
- [x] `share_conservation`
- [x] `full_volatility_in_daily_range`
- [ ] `full_return_autocorrelation_near_zero_across_lags`
- [x] `full_volatility_clustering_has_decay`
- [x] `full_heavier_than_gaussian`
- [x] `endogenous_liquidity_feedback_increases_tail_weight`
- [x] `full_volume_volatility_relation_positive`
- [ ] `full_price_discovery_bounded`
- [x] `public_news_channel_has_paired_price_response`
- [ ] `agent_information_channel_has_paired_price_response`
- [x] `empty_information_baseline_is_weakest_discovery`
- [x] `single_strategy_markets_remain_active`
- [ ] `ablations_avoid_pathological_return_predictability`
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
| `full_volatility_in_daily_range` | `0.023747646928698754` | `{"maximum": 0.03, "minimum": 0.005}` | 95.0% | 20261115 |
| `full_return_autocorrelation_near_zero_across_lags` | `0.18250777715501826` | `0.2` | 50.0% | 20261102, 20261104, 20261106, 20261107, 20261113, 20261114, 20261115, 20261116, 20261117, 20261118 |
| `full_volatility_clustering_has_decay` | `0.343824864995248` | `0.03` | 100.0% | none |
| `full_heavier_than_gaussian` | `5.34400404098991` | `0.1` | 100.0% | none |
| `full_volume_volatility_relation_positive` | `0.3814898475787348` | `0.05` | 100.0% | none |
| `full_price_discovery_bounded` | `0.09802190297287627` | `0.1` | 50.0% | 20261101, 20261102, 20261104, 20261106, 20261107, 20261113, 20261115, 20261116, 20261117, 20261118 |
| `endogenous_liquidity_feedback_increases_tail_weight` | `5.022235935520229` | `0.05` | 100.0% | none |
| `public_news_marginal_response` | `8.702210158791853` | `1.0` | 100.0% | none |
| `public_news_independent_response` | `8.323273460607123` | `1.0` | 100.0% | none |
| `agent_information_marginal_response` | `1.1068334623805667` | `1.0` | 70.0% | 20261102, 20261104, 20261106, 20261107, 20261116, 20261117 |
| `agent_information_independent_response` | `1.009487410022355` | `1.0` | 50.0% | 20261102, 20261103, 20261104, 20261107, 20261109, 20261115, 20261117, 20261118, 20261119, 20261120 |
| `empty_information_baseline_is_weakest_discovery` | `8.689937310488787` | `1.0` | 100.0% | none |
| `value_only_remains_active` | `0.019046615001287383` | `0.001` | 100.0% | none |
| `trend_only_remains_active` | `0.03041797455506492` | `0.002` | 100.0% | none |
| `noise_only_remains_active` | `0.019557438874928695` | `0.003` | 100.0% | none |
| `value_only_avoids_pathological_return_predictability` | `0.5038639905857399` | `0.25` | 50.0% | 20261102, 20261104, 20261106, 20261107, 20261110, 20261111, 20261115, 20261116, 20261117, 20261119 |
| `trend_only_avoids_pathological_return_predictability` | `0.001592614347418223` | `0.25` | 100.0% | none |
| `noise_only_avoids_pathological_return_predictability` | `0.010230802440346217` | `0.25` | 100.0% | none |
| `independent_signals_avoids_pathological_return_predictability` | `0.40574876634441315` | `0.25` | 40.0% | 20261102, 20261104, 20261106, 20261107, 20261110, 20261111, 20261115, 20261116, 20261117, 20261118, 20261119, 20261120 |
| `fixed_participation_avoids_pathological_return_predictability` | `0.20660795981889388` | `0.25` | 60.0% | 20261102, 20261104, 20261107, 20261114, 20261115, 20261116, 20261117, 20261118 |
| `fixed_liquidity_avoids_pathological_return_predictability` | `0.0808976154666291` | `0.25` | 90.0% | 20261102, 20261117 |
| `liquidity_stress_avoids_pathological_return_predictability` | `0.3656600397662306` | `0.25` | 45.0% | 20261101, 20261102, 20261107, 20261113, 20261114, 20261115, 20261116, 20261117, 20261118, 20261119, 20261120 |
| `spread_and_depth_are_finite` | `7.174715337561048` | `{"maximum": 25.0, "minimum": 1.0}` | 100.0% | none |
| `liquidity_stress_increases_clustering` | `0.17780476298025044` | `0.0` | 85.0% | 20261104, 20261106, 20261114 |
| `logit_imitation_fires_and_tracks_fitness` | `6300.0` | `150.0` | 100.0% | none |
| `logit_market_remains_active_and_bounded` | `0.026764635799523366` | `{"maximum": 0.04, "minimum": 0.005}` | 100.0% | none |
| `persistent_order_flow_is_observable` | `0.4036011488935579` | `0.05` | 100.0% | none |

## Scenario medians

| Scenario | Volatility | Return ACF | |Return| ACF | Excess kurtosis | Volume-|return| corr | Price gap |
|---|---:|---:|---:|---:|---:|---:|
| full | 0.023748 | -0.182508 | 0.343825 | 5.344004 | 0.381490 | 0.098022 |
| no_direct_news | 0.022278 | -0.537707 | 0.704809 | 26.947361 | 0.754669 | 0.793627 |
| no_agent_information | 0.021842 | 0.007942 | 0.236692 | 2.408188 | 0.329740 | 0.091001 |
| no_information_channels | 0.018418 | 0.005176 | 0.558292 | 14.046157 | 0.739674 | 0.812486 |
| value_only | 0.019047 | -0.503864 | 0.471076 | 4.200821 | 0.672995 | 0.067276 |
| trend_only | 0.030418 | -0.001593 | 0.447789 | 14.578236 | 0.589636 | 0.108315 |
| noise_only | 0.019557 | 0.010231 | 0.339084 | 14.928455 | 0.590209 | 0.135768 |
| no_logit | 0.023748 | -0.182508 | 0.343825 | 5.344004 | 0.381490 | 0.098022 |
| no_activity_persistence | 0.023602 | -0.150650 | 0.318701 | 3.917522 | 0.375538 | 0.097559 |
| independent_signals | 0.014244 | -0.405749 | 0.374812 | 3.342120 | 0.113099 | 0.125942 |
| fixed_participation | 0.023831 | -0.206608 | 0.253807 | 2.828474 | 0.331180 | 0.109463 |
| fixed_liquidity | 0.018496 | -0.080898 | 0.099030 | 0.374053 | 0.184227 | 0.080269 |
| liquidity_stress | 0.042217 | -0.365660 | 0.504809 | 6.484410 | 0.583671 | 0.059178 |
| concentrated_wealth | 0.023403 | -0.227312 | 0.349005 | 4.876668 | 0.369039 | 0.099048 |
| garch_t_control | 0.023856 | -0.185912 | 0.466162 | 9.592393 | 0.492886 | 0.087614 |
| logit_learning | 0.026765 | 0.072147 | 0.288532 | 3.233612 | 0.407129 | 0.067613 |

## Full-market structural metrics

| Metric | Median |
|---|---:|
| Maximum absolute return ACF, lags 1–20 | 0.182508 |
| Absolute-return ACF(5) | 0.284946 |
| Absolute-return ACF(20) | 0.087998 |
| Absolute-return ACF(50) | -0.057576 |
| Volume ACF(1) | 0.863216 |
| OFI ACF(1) | 0.403601 |
| OFI-return correlation | 0.545302 |
| Mean spread (bps) | 7.174715 |
| Three-sigma tail fraction | 0.014400 |
| Return skewness | -0.315262 |
| Leverage correlation, r(t) vs |r|(t+1) | 0.029967 |
| Crash-day fraction, r < -5% | 0.019800 |
| Bubble-day fraction, log gap > 10% | 0.000000 |
| Maximum drawdown | 0.401980 |
| Final wealth Gini | 0.207028 |

The GARCH-t scenario is an explicitly exogenous stress control. It is not counted as evidence that Agent interaction generated fat tails or volatility clustering.
