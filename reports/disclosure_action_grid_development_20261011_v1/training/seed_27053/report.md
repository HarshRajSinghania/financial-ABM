# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27053
Run ID: `b63be5b2f2d5329c4f92aa72af317d5dc48337207b8a9ca61b77139931191e17`
Result fingerprint: `bae34c84c42859b79afeedd8896d5efcb3858bbf6ecac6eb731bff25ab8f07c2`

A completed simulation is not evidence of empirical calibration or a policy ranking.

## Metrics

```json
{
  "window": {
    "start_day": 600,
    "end_day": 1800,
    "elapsed_days": 1200,
    "state_observations": 1201,
    "decision_observations": 20,
    "decision_days": [
      660,
      720,
      780,
      840,
      900,
      960,
      1020,
      1080,
      1140,
      1200,
      1260,
      1320,
      1380,
      1440,
      1500,
      1560,
      1620,
      1680,
      1740,
      1800
    ],
    "cost_basis": "Commitments in (start_day, end_day] at decision-day prices; applied the following day.",
    "interpretation": "Descriptive changes include delayed pre-window actions, not causal returns on in-window decisions."
  },
  "true_change": {
    "equal_weight_sd": -0.5870476190476157,
    "equal_weight_raw": -8.805714285714236,
    "fixed_start_cap_weight_sd": -0.600680298350652,
    "fixed_start_cap_weight_raw": -9.01020447525978,
    "end_cap_weight_sd": -0.6160201274716379,
    "end_cap_weight_raw": -9.24030191207457
  },
  "full_period_change": {
    "equal_weight_sd": -0.9170714285714238,
    "equal_weight_raw": -13.756071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8623707010581966,
    "inflation_mean_sd": 0.6470922619047619
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.36533333333333656,
    "equal_weight_raw": 5.480000000000048,
    "fixed_start_cap_weight_sd": 0.35170065403030043,
    "fixed_start_cap_weight_raw": 5.275509810454507,
    "end_cap_weight_sd": 0.33636082490931446,
    "end_cap_weight_raw": 5.045412373639717
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5423809523809493,
      "change_raw": -8.13571428571424,
      "decay_adjusted_gain_sd": 0.4100000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7132142857142825,
      "change_raw": -10.698214285714236,
      "decay_adjusted_gain_sd": 0.2391666666666699
    },
    "small": {
      "count": 18,
      "change_sd": -0.5314087301587269,
      "change_raw": -7.9711309523809035,
      "decay_adjusted_gain_sd": 0.4209722222222254
    },
    "large_minus_small_sd": -0.010972222222222383,
    "large_minus_small_raw": -0.16458333333333575
  },
  "inflation": {
    "initial_mean_sd": 0.3248333333333333,
    "final_mean_sd": 0.6495833333333335,
    "mean_sd": 0.5169757840688316,
    "mean_absolute_raw_gap": 7.754636761032473,
    "final_absolute_raw_gap": 9.743750000000002,
    "mean_range_fraction": 0.07754636761032473
  },
  "impact": {
    "initial_share": 0.44,
    "final_share": 0.5,
    "initial_wealth_share": 0.6049060912117076,
    "final_wealth_share": 0.6694689927576637
  },
  "pricing_slope": {
    "mean": -0.003449245952110827,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.8244877313626271,
    "real_improvement_cost": 0.802648523482526,
    "washing_cost": 0.02183920788010133,
    "fine_transfer": 0.017128614316384905,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.841616345679012,
    "resource_cost_fraction_initial_cap": 0.027482924378754235,
    "private_net_outflow_fraction_initial_cap": 0.0280538781893004,
    "fine_transfer_fraction_initial_cap": 0.0005709538105461635,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0017036620963001114,
    "unapplied_final_day_resource_cost": 0.00042874771492419937
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 13.293102593396453,
    "beneficial_raw_gain_per_resource_cost": 199.3965389009468,
    "undefined_reason": null
  },
  "diagnostics": {
    "status": "ok",
    "missing_size_classes": [],
    "pricing_slope_missing_observations": 0,
    "finite_metrics": true
  },
  "financing": {
    "status": "modeled_accrual",
    "interpretation": "Accrued financing fees, not payments or cash-solvency evidence; value adjustment is relative to the initial contract.",
    "fixed_exposure": 15.0,
    "accrued_cost": 2.930771263042846,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.04541921314763078,
    "accrued_cost_fraction_initial_cap": 0.09769237543476154,
    "mean_contract_rate": 0.0413313197606431,
    "maximum_ledger_error": 5.082197683525802e-20
  }
}
```

## Validation

```json
{
  "n_assets": 30,
  "observations": 1200,
  "burn_in_days": 600,
  "mechanical": {
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 4,
    "maximum_relative_cash_error": 1.6756807491444047e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
    "conservation_tolerance": 1e-08,
    "cash_error_measure": "relative to expected cash; absolute if expected cash is zero",
    "share_error_measure": "daily maximum absolute error across all assets"
  },
  "stylized": {
    "status": "PASS",
    "checks": {
      "all_assets_have_finite_moments": true,
      "all_assets_positive_excess_kurtosis": true,
      "all_assets_positive_abs_return_acf_1": true
    },
    "failed_assets": {
      "nonfinite_moments": [],
      "nonpositive_excess_kurtosis": [],
      "nonpositive_abs_return_acf_1": []
    }
  },
  "return_acf": {
    "status": "pending",
    "statistics": {
      "finite_count": 30,
      "minimum": -0.21941313765706025,
      "maximum": 0.006136521893303661,
      "mean": -0.11647693869534921,
      "median": -0.12921109884145238,
      "quantile_05": -0.2111900411557523,
      "quantile_95": -0.03851261486175285
    },
    "target": null,
    "tolerance": null,
    "threshold_source": null,
    "deviation_statistics": null,
    "failed_assets": null
  },
  "cross_asset_correlation": {
    "status": "pending",
    "statistics": {
      "finite_count": 435,
      "minimum": 0.1474110000778573,
      "maximum": 0.8381503841011128,
      "mean": 0.43163224409242773,
      "median": 0.34429120259606805,
      "quantile_05": 0.1900648693702324,
      "quantile_95": 0.7881584184890692
    },
    "pair_count": 435,
    "bounds": null,
    "threshold_source": null,
    "violating_pair_count": null
  },
  "moments_per_asset": [
    {
      "asset": 0,
      "moments": {
        "daily_volatility": 0.020736910313955196,
        "excess_kurtosis": 25.622758471076214,
        "return_acf_1": -0.1317003490154498,
        "abs_return_acf_1": 0.5929917623425408,
        "abs_return_acf_5": 0.41579919225060846,
        "abs_return_acf_20": 0.44542535495722974,
        "quantile_01": -0.07000361107637537,
        "quantile_99": 0.0481122773565357,
        "hill_tail_index": 1.595821408355971
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018392799705006537,
        "excess_kurtosis": 4.992690425577439,
        "return_acf_1": -0.15927451791422073,
        "abs_return_acf_1": 0.3740886663032494,
        "abs_return_acf_5": 0.31499320510395845,
        "abs_return_acf_20": 0.29900317186692227,
        "quantile_01": -0.051951801556060814,
        "quantile_99": 0.06187559118098698,
        "hill_tail_index": 3.872152706326861
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018853829234255524,
        "excess_kurtosis": 5.839303885781925,
        "return_acf_1": -0.20371240941030877,
        "abs_return_acf_1": 0.35144774568216697,
        "abs_return_acf_5": 0.34479172749854037,
        "abs_return_acf_20": 0.3471134874737477,
        "quantile_01": -0.053958558293494406,
        "quantile_99": 0.05709837842769582,
        "hill_tail_index": 3.9622326523821862
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021064186074618484,
        "excess_kurtosis": 24.375113908305405,
        "return_acf_1": -0.0491802149940836,
        "abs_return_acf_1": 0.38277467556727646,
        "abs_return_acf_5": 0.30619137375430816,
        "abs_return_acf_20": 0.405528967338366,
        "quantile_01": -0.06495993109652463,
        "quantile_99": 0.05004100672858862,
        "hill_tail_index": 1.8574390652245765
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019909953773196255,
        "excess_kurtosis": 10.43435662180501,
        "return_acf_1": -0.179168879008869,
        "abs_return_acf_1": 0.4065419517046579,
        "abs_return_acf_5": 0.36111641172978,
        "abs_return_acf_20": 0.3482083626706769,
        "quantile_01": -0.055234306086229056,
        "quantile_99": 0.05837569131647512,
        "hill_tail_index": 2.943550372627802
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021504352388367863,
        "excess_kurtosis": 27.488055684056963,
        "return_acf_1": -0.09103859012962424,
        "abs_return_acf_1": 0.46351503337814665,
        "abs_return_acf_5": 0.359505934909104,
        "abs_return_acf_20": 0.4441228738009115,
        "quantile_01": -0.062359092693289674,
        "quantile_99": 0.05360170561232833,
        "hill_tail_index": 2.026804579093278
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02652663303317498,
        "excess_kurtosis": 27.719715047780664,
        "return_acf_1": -0.062410047026411626,
        "abs_return_acf_1": 0.5405696206179357,
        "abs_return_acf_5": 0.3910469601480672,
        "abs_return_acf_20": 0.5096227403583463,
        "quantile_01": -0.10141015678637508,
        "quantile_99": 0.07056757966530197,
        "hill_tail_index": 1.803882578133029
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020741951679713624,
        "excess_kurtosis": 10.50449397260485,
        "return_acf_1": -0.2173081034929334,
        "abs_return_acf_1": 0.4390037120124273,
        "abs_return_acf_5": 0.44619680502956643,
        "abs_return_acf_20": 0.32275754588073524,
        "quantile_01": -0.06095524510478994,
        "quantile_99": 0.0660962965508014,
        "hill_tail_index": 3.530296521667003
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01866988470789604,
        "excess_kurtosis": 5.506758315675894,
        "return_acf_1": -0.13420726937047978,
        "abs_return_acf_1": 0.32632180689892026,
        "abs_return_acf_5": 0.37725134504330265,
        "abs_return_acf_20": 0.26023704434206313,
        "quantile_01": -0.05404325481188322,
        "quantile_99": 0.058441683673112914,
        "hill_tail_index": 3.842691348713431
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021962424060744203,
        "excess_kurtosis": 24.46511364233019,
        "return_acf_1": -0.21941313765706025,
        "abs_return_acf_1": 0.3799795258425736,
        "abs_return_acf_5": 0.3693630619280997,
        "abs_return_acf_20": 0.36687412391943547,
        "quantile_01": -0.07286898241923918,
        "quantile_99": 0.06287109191197575,
        "hill_tail_index": 2.2676814464029045
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02309938929549248,
        "excess_kurtosis": 24.356549146799498,
        "return_acf_1": -0.12240087139841628,
        "abs_return_acf_1": 0.3523730082437878,
        "abs_return_acf_5": 0.2924405008147663,
        "abs_return_acf_20": 0.41026815090490937,
        "quantile_01": -0.07997451286880454,
        "quantile_99": 0.06666131606851092,
        "hill_tail_index": 2.3041047854259786
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02177334526328439,
        "excess_kurtosis": 17.228975645096117,
        "return_acf_1": -0.1305291301043366,
        "abs_return_acf_1": 0.4395623485951141,
        "abs_return_acf_5": 0.36148704947142934,
        "abs_return_acf_20": 0.43821860641722615,
        "quantile_01": -0.07471050380847859,
        "quantile_99": 0.060698104925516194,
        "hill_tail_index": 2.8621038968076684
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021475168101608877,
        "excess_kurtosis": 13.362755352039905,
        "return_acf_1": -0.12596147772404273,
        "abs_return_acf_1": 0.4460751821706325,
        "abs_return_acf_5": 0.4027390147783757,
        "abs_return_acf_20": 0.45735036587006433,
        "quantile_01": -0.06341983651502939,
        "quantile_99": 0.0572244211872213,
        "hill_tail_index": 2.966108149055083
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022126895620787415,
        "excess_kurtosis": 22.17705987817895,
        "return_acf_1": -0.14402785277285968,
        "abs_return_acf_1": 0.4498263683444724,
        "abs_return_acf_5": 0.40378560814477715,
        "abs_return_acf_20": 0.5162956192477054,
        "quantile_01": -0.0660546748209363,
        "quantile_99": 0.06700594122535809,
        "hill_tail_index": 2.035668961265256
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02221921573031221,
        "excess_kurtosis": 15.336250818485745,
        "return_acf_1": -0.09539603380872216,
        "abs_return_acf_1": 0.42870611675945297,
        "abs_return_acf_5": 0.3420987672188728,
        "abs_return_acf_20": 0.4209363621739467,
        "quantile_01": -0.06822006469857808,
        "quantile_99": 0.06082214169195725,
        "hill_tail_index": 2.42791945679545
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021482888654016968,
        "excess_kurtosis": 23.04582503108785,
        "return_acf_1": -0.05900011021545404,
        "abs_return_acf_1": 0.4609086179203011,
        "abs_return_acf_5": 0.41090916868432725,
        "abs_return_acf_20": 0.41512905445540554,
        "quantile_01": -0.06526685006399467,
        "quantile_99": 0.05096618877178859,
        "hill_tail_index": 1.8486419869798567
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020293156097677872,
        "excess_kurtosis": 27.0933805632765,
        "return_acf_1": -0.07853664801971394,
        "abs_return_acf_1": 0.47607731655203883,
        "abs_return_acf_5": 0.3490420036532608,
        "abs_return_acf_20": 0.4183938025564313,
        "quantile_01": -0.053591903305409416,
        "quantile_99": 0.052384000405179126,
        "hill_tail_index": 1.8058500450561528
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01867942044584823,
        "excess_kurtosis": 5.225369335631292,
        "return_acf_1": -0.13654344649759997,
        "abs_return_acf_1": 0.34859967049651236,
        "abs_return_acf_5": 0.3585386782630851,
        "abs_return_acf_20": 0.2976918427497032,
        "quantile_01": -0.055681302826505116,
        "quantile_99": 0.0616972977189723,
        "hill_tail_index": 3.851203050547138
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02328174287358701,
        "excess_kurtosis": 28.889846600870843,
        "return_acf_1": 0.006136521893303661,
        "abs_return_acf_1": 0.5630559575262954,
        "abs_return_acf_5": 0.3049457202672659,
        "abs_return_acf_20": 0.43910897530652604,
        "quantile_01": -0.0721008325626806,
        "quantile_99": 0.0558934825471004,
        "hill_tail_index": 1.7576026751728357
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018060381456389413,
        "excess_kurtosis": 4.054822970232858,
        "return_acf_1": -0.15139355593381715,
        "abs_return_acf_1": 0.30630668273078054,
        "abs_return_acf_5": 0.2669916426109957,
        "abs_return_acf_20": 0.3241110557492584,
        "quantile_01": -0.054013570007415856,
        "quantile_99": 0.06021678945204286,
        "hill_tail_index": 5.065490996344579
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019023400230241787,
        "excess_kurtosis": 13.12341990016212,
        "return_acf_1": -0.10738164730901234,
        "abs_return_acf_1": 0.4423366194473827,
        "abs_return_acf_5": 0.29518049624303844,
        "abs_return_acf_20": 0.4212230882094951,
        "quantile_01": -0.05680206113798458,
        "quantile_99": 0.04764693794628254,
        "hill_tail_index": 2.4477553790109776
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018344375043239346,
        "excess_kurtosis": 5.134152332800205,
        "return_acf_1": -0.12789306757856814,
        "abs_return_acf_1": 0.32402182975042243,
        "abs_return_acf_5": 0.35614320908759745,
        "abs_return_acf_20": 0.30573496949172574,
        "quantile_01": -0.05283639268768095,
        "quantile_99": 0.0542758286382225,
        "hill_tail_index": 3.796752619781721
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021213528609175237,
        "excess_kurtosis": 9.097724679728824,
        "return_acf_1": -0.14928178470063042,
        "abs_return_acf_1": 0.4085677584409979,
        "abs_return_acf_5": 0.3793694761070023,
        "abs_return_acf_20": 0.3711836331995691,
        "quantile_01": -0.0693022245212267,
        "quantile_99": 0.06171026033606429,
        "hill_tail_index": 3.5608587770979563
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019905524681575,
        "excess_kurtosis": 5.022896096228752,
        "return_acf_1": -0.13463246162458106,
        "abs_return_acf_1": 0.3448547834533981,
        "abs_return_acf_5": 0.34979669709233535,
        "abs_return_acf_20": 0.3922927504313067,
        "quantile_01": -0.06386901731213535,
        "quantile_99": 0.06407731412541694,
        "hill_tail_index": 4.818387384634275
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018865627840936403,
        "excess_kurtosis": 4.384752231348451,
        "return_acf_1": -0.14280449130132447,
        "abs_return_acf_1": 0.3390999737332501,
        "abs_return_acf_5": 0.30886677206814317,
        "abs_return_acf_20": 0.34268794582774675,
        "quantile_01": -0.05651334695931173,
        "quantile_99": 0.05939499362125584,
        "hill_tail_index": 4.5596964881722455
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.024027334114247085,
        "excess_kurtosis": 32.451909485389336,
        "return_acf_1": -0.07155679018170381,
        "abs_return_acf_1": 0.5650427768783208,
        "abs_return_acf_5": 0.3691672823347363,
        "abs_return_acf_20": 0.49921600831904783,
        "quantile_01": -0.0770101481528351,
        "quantile_99": 0.05932842492565388,
        "hill_tail_index": 1.793765168655927
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023242537994710325,
        "excess_kurtosis": 12.949785746060888,
        "return_acf_1": -0.0611062139960971,
        "abs_return_acf_1": 0.4758446400452429,
        "abs_return_acf_5": 0.37986688556880555,
        "abs_return_acf_20": 0.4217484763677407,
        "quantile_01": -0.08330599389145121,
        "quantile_99": 0.06993695511895533,
        "hill_tail_index": 2.5132706624189534
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020845365790803084,
        "excess_kurtosis": 25.690020511788184,
        "return_acf_1": -0.053327814007365366,
        "abs_return_acf_1": 0.4121654865106231,
        "abs_return_acf_5": 0.38906938812375824,
        "abs_return_acf_20": 0.43255740442713886,
        "quantile_01": -0.06841031287641733,
        "quantile_99": 0.04701677101447604,
        "hill_tail_index": 1.9962523010982003
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02057788758292768,
        "excess_kurtosis": 9.218139779159289,
        "return_acf_1": -0.13147318917024836,
        "abs_return_acf_1": 0.3905502488099782,
        "abs_return_acf_5": 0.3942943765880908,
        "abs_return_acf_20": 0.3337942129663823,
        "quantile_01": -0.06578684779924918,
        "quantile_99": 0.06139185765027521,
        "hill_tail_index": 3.370890046617715
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01946420697330472,
        "excess_kurtosis": 4.186697166934381,
        "return_acf_1": -0.029784578389845773,
        "abs_return_acf_1": 0.302946058082085,
        "abs_return_acf_5": 0.31595765004622706,
        "abs_return_acf_20": 0.220216714674754,
        "quantile_01": -0.057621734798908614,
        "quantile_99": 0.057992007288321074,
        "hill_tail_index": 4.579887098740714
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```

## Learning diagnostics

Firm policy: q_learning
Training: True
Coverage status: not_applicable
Unseen state share: 0.0
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
