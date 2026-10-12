# MSM calibration: held-out comparison and ablations

Daily French 49 industry returns, 2000-01-03 to 2025-12-31 (6539 days). Each model is simulated with 50 evaluation seeds disjoint from the calibration seeds. J is the sum of squared per-moment t-statistics (9 moments); lower is better.

## Model comparison (J)

| Model | Train | Validation | Test |
|---|---:|---:|---:|
| Stage 1 ABM (MSM) | 10.0 | 10.7 | 12.6 |
| Franke-Westerhoff HAM (MSM) | 9.3 | 18.7 | 13.2 |
| GARCH(1,1)-t (MLE) | 4.8 | 13.0 | 4.8 |
| i.i.d. Student-t (MLE) | 258.7 | 302.1 | 237.7 |

## Moments on the test industries

| Moment | Data (± s.e.) | Stage 1 ABM (MSM) | Franke-Westerhoff HAM (MSM) | GARCH(1,1)-t (MLE) | i.i.d. Student-t (MLE) |
|---|---:|---:|---:|---:|---:|
| Daily volatility | 0.0171 ± 0.0008 | 0.0156 | 0.0162 | 0.0164 | 0.0165 |
| Excess kurtosis | 9.0012 ± 2.8628 | 5.6050 | 5.6869 | 11.6372 | 18.0999 |
| Return ACF(1) | -0.0316 ± 0.0223 | -0.0329 | 0.0074 | -0.0026 | 0.0026 |
| \|Return\| ACF(1) | 0.2464 ± 0.0357 | 0.3008 | 0.3012 | 0.2397 | -0.0025 |
| \|Return\| ACF(5) | 0.2486 ± 0.0321 | 0.3084 | 0.2791 | 0.2312 | -0.0024 |
| \|Return\| ACF(20) | 0.1823 ± 0.0168 | 0.1650 | 0.2084 | 0.1910 | -0.0003 |
| 1% quantile | -0.0460 ± 0.0031 | -0.0436 | -0.0480 | -0.0445 | -0.0442 |
| 99% quantile | 0.0467 ± 0.0029 | 0.0464 | 0.0497 | 0.0446 | 0.0440 |
| Hill tail index | 3.3443 ± 0.3813 | 3.5466 | 3.6394 | 3.3740 | 3.1254 |

## Calibrated ABM parameters

| Parameter | Estimate | s.e. |
|---|---:|---:|
| `fundamental_volatility` | 0.0068 | 0.0021 |
| `price_impact` | 0.6203 | 0.2348 |
| `liquidity_volatility_sensitivity` | 2.4553 | 5.8671 |
| `activity_volatility_sensitivity` | 1.3302 | 4.5477 |
| `noise_scale` | 2.8692 | 3.1529 |
| `demand_volatility_exponent` | 0.6175 | 0.4990 |
| `transient_impact_decay` | 0.9190 | 1.3336 |

## Ablations at the calibrated parameters

Change in the moment when one mechanism is switched off, paired by seed (95% CI).

| Ablation | Excess kurtosis | \|Return\| ACF(1) | \|Return\| ACF(20) | Hill index |
|---|---:|---:|---:|---:|
| `fixed_liquidity` | -4.877 [-5.116, -4.637] | -0.186 [-0.192, -0.180] | -0.110 [-0.115, -0.105] | +2.459 [+2.334, +2.585] |
| `fixed_participation` | -1.372 [-1.586, -1.158] | -0.053 [-0.058, -0.048] | -0.007 [-0.012, -0.002] | +0.419 [+0.327, +0.512] |
| `no_activity_persistence` | -0.158 [-0.320, +0.004] | -0.002 [-0.006, +0.001] | -0.000 [-0.003, +0.003] | -0.006 [-0.061, +0.048] |
| `independent_signals` | -5.548 [-5.790, -5.306] | -0.247 [-0.254, -0.240] | -0.163 [-0.170, -0.156] | +3.558 [+3.425, +3.692] |

Evaluation-window days on which the ±max_log_return price clamp bound, summed over seeds: `full` 0, `fixed_liquidity` 0, `fixed_participation` 0, `no_activity_persistence` 0, `independent_signals` 0.

![Model fit](model_fit_test.png)

![Ablations](ablations.png)
