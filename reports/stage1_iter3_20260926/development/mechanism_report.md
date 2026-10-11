# Stage 1 mechanism validation

- Protocol: `stage1-mechanism-development-v10`
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
| `full_volatility_in_daily_range` | `0.02216115761047789` | `{"maximum": 0.03, "minimum": 0.005}` | 100.0% | none |
| `full_return_autocorrelation_near_zero_across_lags` | `0.13529363171429282` | `0.2` | 100.0% | none |
| `full_volatility_clustering_has_decay` | `0.24372545057709372` | `0.03` | 100.0% | none |
| `full_heavier_than_gaussian` | `3.366895235201725` | `0.1` | 100.0% | none |
| `full_volume_volatility_relation_positive` | `0.33348365545365866` | `0.05` | 100.0% | none |
| `full_price_discovery_bounded` | `0.08085671955549854` | `0.1` | 75.0% | 20261101, 20261102, 20261104, 20261107, 20261115 |
| `endogenous_liquidity_feedback_increases_tail_weight` | `3.0345878282931933` | `0.05` | 100.0% | none |
| `public_news_marginal_response` | `10.639345789426264` | `1.0` | 100.0% | none |
| `public_news_independent_response` | `8.323273460607123` | `1.0` | 100.0% | none |
| `agent_information_marginal_response` | `1.4496036638907728` | `1.0` | 85.0% | 20261102, 20261104, 20261117 |
| `agent_information_independent_response` | `1.0963493933170803` | `1.0` | 90.0% | 20261103, 20261115 |
| `empty_information_baseline_is_weakest_discovery` | `10.1448820118754` | `1.0` | 100.0% | none |
| `value_only_remains_active` | `0.012547172583968513` | `0.001` | 100.0% | none |
| `trend_only_remains_active` | `0.03041797455506492` | `0.002` | 100.0% | none |
| `noise_only_remains_active` | `0.019557438874928695` | `0.003` | 100.0% | none |
| `value_only_avoids_pathological_return_predictability` | `0.08577526293937512` | `0.25` | 100.0% | none |
| `trend_only_avoids_pathological_return_predictability` | `0.001592614347418223` | `0.25` | 100.0% | none |
| `noise_only_avoids_pathological_return_predictability` | `0.010230802440346217` | `0.25` | 100.0% | none |
| `independent_signals_avoids_pathological_return_predictability` | `0.05622927079728601` | `0.25` | 100.0% | none |
| `fixed_participation_avoids_pathological_return_predictability` | `0.06697070727776469` | `0.25` | 100.0% | none |
| `fixed_liquidity_avoids_pathological_return_predictability` | `0.01726103197533422` | `0.25` | 100.0% | none |
| `liquidity_stress_avoids_pathological_return_predictability` | `0.14249522433003828` | `0.25` | 95.0% | 20261114 |
| `spread_and_depth_are_finite` | `7.107007185663394` | `{"maximum": 25.0, "minimum": 1.0}` | 100.0% | none |
| `liquidity_stress_increases_clustering` | `0.13707096684244663` | `0.0` | 100.0% | none |
| `logit_imitation_fires_and_tracks_fitness` | `6300.0` | `150.0` | 100.0% | none |
| `logit_market_remains_active_and_bounded` | `0.027052582143899846` | `{"maximum": 0.04, "minimum": 0.005}` | 100.0% | none |
| `persistent_order_flow_is_observable` | `0.45660181096713914` | `0.05` | 100.0% | none |

## Scenario medians

| Scenario | Volatility | Return ACF | |Return| ACF | Excess kurtosis | Volume-|return| corr | Price gap |
|---|---:|---:|---:|---:|---:|---:|
| full | 0.022161 | -0.038081 | 0.243725 | 3.366895 | 0.333484 | 0.080857 |
| no_direct_news | 0.018119 | -0.021687 | 0.549556 | 14.874248 | 0.732906 | 0.727928 |
| no_agent_information | 0.021842 | 0.007942 | 0.236692 | 2.408188 | 0.329740 | 0.091001 |
| no_information_channels | 0.018418 | 0.005176 | 0.558292 | 14.046157 | 0.739674 | 0.812486 |
| value_only | 0.012547 | -0.085775 | 0.034658 | 1.985904 | 0.384808 | 0.048857 |
| trend_only | 0.030418 | -0.001593 | 0.447789 | 14.578236 | 0.589636 | 0.108315 |
| noise_only | 0.019557 | 0.010231 | 0.339084 | 14.928455 | 0.590209 | 0.135768 |
| no_logit | 0.022161 | -0.038081 | 0.243725 | 3.366895 | 0.333484 | 0.080857 |
| no_activity_persistence | 0.022207 | -0.036889 | 0.246150 | 3.284224 | 0.328633 | 0.084025 |
| independent_signals | 0.011963 | -0.056229 | 0.033232 | 0.146737 | 0.025822 | 0.100241 |
| fixed_participation | 0.023098 | -0.066971 | 0.167339 | 2.203215 | 0.289658 | 0.081505 |
| fixed_liquidity | 0.018158 | -0.017261 | 0.085750 | 0.365996 | 0.182966 | 0.067903 |
| liquidity_stress | 0.037283 | -0.142495 | 0.384809 | 6.149796 | 0.556829 | 0.080059 |
| concentrated_wealth | 0.022274 | -0.048372 | 0.238518 | 3.775323 | 0.341513 | 0.085970 |
| garch_t_control | 0.022035 | -0.070789 | 0.364168 | 7.898054 | 0.435325 | 0.077022 |
| logit_learning | 0.027053 | 0.079784 | 0.287868 | 3.372507 | 0.406520 | 0.067389 |

## Full-market structural metrics

| Metric | Median |
|---|---:|
| Maximum absolute return ACF, lags 1–20 | 0.135294 |
| Absolute-return ACF(5) | 0.230562 |
| Absolute-return ACF(20) | 0.067795 |
| Absolute-return ACF(50) | -0.053045 |
| Volume ACF(1) | 0.884018 |
| OFI ACF(1) | 0.456602 |
| OFI-return correlation | 0.556552 |
| Mean spread (bps) | 7.107007 |
| Three-sigma tail fraction | 0.012200 |
| Return skewness | -0.223938 |
| Leverage correlation, r(t) vs |r|(t+1) | 0.023965 |
| Crash-day fraction, r < -5% | 0.017600 |
| Bubble-day fraction, log gap > 10% | 0.000000 |
| Maximum drawdown | 0.403390 |
| Final wealth Gini | 0.224122 |

The GARCH-t scenario is an explicitly exogenous stress control. It is not counted as evidence that Agent interaction generated fat tails or volatility clustering.
