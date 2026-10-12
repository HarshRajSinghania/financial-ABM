# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27114
Run ID: `037383cb82831af237d1292f5c900ce279f234ce32be4f8b0481ebdd76865fad`
Result fingerprint: `7125ba0820ef726ed2bd3b7b06eb02c11b101a0926a38de69cda20ecb3046232`

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
    "equal_weight_sd": -0.631630952380949,
    "equal_weight_raw": -9.474464285714237,
    "fixed_start_cap_weight_sd": -0.6569770382149088,
    "fixed_start_cap_weight_raw": -9.854655573223635,
    "end_cap_weight_sd": -0.6344235824014377,
    "end_cap_weight_raw": -9.51635373602157
  },
  "full_period_change": {
    "equal_weight_sd": -0.9778214285714238,
    "equal_weight_raw": -14.667321428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9429500661375616,
    "inflation_mean_sd": 0.6327738095238095
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.30915646483740383,
    "equal_weight_raw": 4.637346972561057,
    "fixed_start_cap_weight_sd": 0.2907484575648336,
    "fixed_start_cap_weight_raw": 4.3612268634725035,
    "end_cap_weight_sd": 0.3114399246120751,
    "end_cap_weight_raw": 4.6715988691811265
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7282142857142825,
      "change_raw": -10.923214285714238,
      "decay_adjusted_gain_sd": 0.22416666666666973
    },
    "mid": {
      "count": 9,
      "change_sd": -0.656269841269838,
      "change_raw": -9.84404761904757,
      "decay_adjusted_gain_sd": 0.28696304987756605
    },
    "small": {
      "count": 18,
      "change_sd": -0.6032142857142825,
      "change_raw": -9.048214285714238,
      "decay_adjusted_gain_sd": 0.33441813867911185
    },
    "large_minus_small_sd": -0.125,
    "large_minus_small_raw": -1.875
  },
  "inflation": {
    "initial_mean_sd": 0.29975,
    "final_mean_sd": 0.6544166666666665,
    "mean_sd": 0.48348966139328337,
    "mean_absolute_raw_gap": 7.252344920899252,
    "final_absolute_raw_gap": 9.816250000000002,
    "mean_range_fraction": 0.07252344920899252
  },
  "impact": {
    "initial_share": 0.22,
    "final_share": 0.24,
    "initial_wealth_share": 0.24627932996696522,
    "final_wealth_share": 0.24609257422450462
  },
  "pricing_slope": {
    "mean": 0.00013355392795089325,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.09327547305541309,
    "real_improvement_cost": 0.0666028953180738,
    "washing_cost": 0.026672577737339297,
    "fine_transfer": 0.01482004183727659,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10809551489268968,
    "resource_cost_fraction_initial_cap": 0.003109182435180437,
    "private_net_outflow_fraction_initial_cap": 0.0036031838297563234,
    "fine_transfer_fraction_initial_cap": 0.0004940013945758864,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0020888308510698303,
    "unapplied_final_day_resource_cost": 0.00013558989747558021
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 99.43336271918133,
    "beneficial_raw_gain_per_resource_cost": 1491.50044078772,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 2.964281999313269,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.011908476877206621,
    "accrued_cost_fraction_initial_cap": 0.098809399977109,
    "mean_contract_rate": 0.041282926780535516,
    "maximum_ledger_error": 7.115076756936123e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.5273135347621475e-15,
    "maximum_absolute_share_error": 1.7763568394002505e-15,
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
      "minimum": -0.243064902682727,
      "maximum": 0.03433107911721326,
      "mean": -0.09635087626812909,
      "median": -0.10498563901675254,
      "quantile_05": -0.23179411703993957,
      "quantile_95": 0.02007709957932973
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
      "minimum": 0.2253377709383086,
      "maximum": 0.8431727251243426,
      "mean": 0.5637966831788683,
      "median": 0.5753720587591966,
      "quantile_05": 0.28327145646518237,
      "quantile_95": 0.7650547904697265
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
        "daily_volatility": 0.017316263853155375,
        "excess_kurtosis": 7.026312704876039,
        "return_acf_1": -0.050329900192775105,
        "abs_return_acf_1": 0.30171993548231785,
        "abs_return_acf_5": 0.28449488377929205,
        "abs_return_acf_20": 0.27524187865030303,
        "quantile_01": -0.05681493167723551,
        "quantile_99": 0.04128927489216605,
        "hill_tail_index": 2.376722134327746
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018779700156071725,
        "excess_kurtosis": 10.33966659010759,
        "return_acf_1": 0.03433107911721326,
        "abs_return_acf_1": 0.4060837472936339,
        "abs_return_acf_5": 0.42287353897735525,
        "abs_return_acf_20": 0.28881312755039296,
        "quantile_01": -0.056787756525634364,
        "quantile_99": 0.05725719661625084,
        "hill_tail_index": 2.670710072174866
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.027111403087647916,
        "excess_kurtosis": 29.60467854827136,
        "return_acf_1": -0.23699070512499182,
        "abs_return_acf_1": 0.40191466560470046,
        "abs_return_acf_5": 0.3739810067625185,
        "abs_return_acf_20": 0.29848739251702405,
        "quantile_01": -0.0795119954333454,
        "quantile_99": 0.062341056856540185,
        "hill_tail_index": 1.726416793239977
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019613556085358357,
        "excess_kurtosis": 12.963367242426926,
        "return_acf_1": 0.00013681322018413588,
        "abs_return_acf_1": 0.39560761806103856,
        "abs_return_acf_5": 0.3540575546021481,
        "abs_return_acf_20": 0.28911719903708144,
        "quantile_01": -0.05606832022239932,
        "quantile_99": 0.06472874868132221,
        "hill_tail_index": 3.1651602216665924
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.028508895334403074,
        "excess_kurtosis": 20.81113790007576,
        "return_acf_1": -0.22124103723594263,
        "abs_return_acf_1": 0.47057407536115065,
        "abs_return_acf_5": 0.421522646364201,
        "abs_return_acf_20": 0.339895085454734,
        "quantile_01": -0.0971904729820453,
        "quantile_99": 0.07938286374683806,
        "hill_tail_index": 2.3543892433553397
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01808174463496994,
        "excess_kurtosis": 5.207620149235645,
        "return_acf_1": -0.051702867923332806,
        "abs_return_acf_1": 0.3973031177470836,
        "abs_return_acf_5": 0.34257173751303327,
        "abs_return_acf_20": 0.28831262461888474,
        "quantile_01": -0.05772533976447635,
        "quantile_99": 0.05177025408575238,
        "hill_tail_index": 3.5529240824585564
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017539143265993484,
        "excess_kurtosis": 5.274824579647941,
        "return_acf_1": 0.033317791722712986,
        "abs_return_acf_1": 0.3000160317001286,
        "abs_return_acf_5": 0.29353207477659155,
        "abs_return_acf_20": 0.238398089452041,
        "quantile_01": -0.056464488303755486,
        "quantile_99": 0.051153152406762034,
        "hill_tail_index": 3.068965804795588
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019650105444126622,
        "excess_kurtosis": 9.385154254726807,
        "return_acf_1": -0.010978415655251787,
        "abs_return_acf_1": 0.36865832597494297,
        "abs_return_acf_5": 0.38622674274350266,
        "abs_return_acf_20": 0.28779807077650943,
        "quantile_01": -0.06369253519145951,
        "quantile_99": 0.05133808791721059,
        "hill_tail_index": 2.9083736528671276
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02496951613592122,
        "excess_kurtosis": 18.75725059686313,
        "return_acf_1": -0.1927239146605125,
        "abs_return_acf_1": 0.41798767608259985,
        "abs_return_acf_5": 0.38474706519276697,
        "abs_return_acf_20": 0.2933430413711444,
        "quantile_01": -0.08316597858405489,
        "quantile_99": 0.07130921737214267,
        "hill_tail_index": 2.450286232954133
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02600589726202641,
        "excess_kurtosis": 18.89940904824919,
        "return_acf_1": -0.11364971648734426,
        "abs_return_acf_1": 0.37436206732431954,
        "abs_return_acf_5": 0.4216961534369824,
        "abs_return_acf_20": 0.2905534995910666,
        "quantile_01": -0.0902634051401126,
        "quantile_99": 0.0707318090816296,
        "hill_tail_index": 2.4841899582771667
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022296715771785672,
        "excess_kurtosis": 14.115622043753604,
        "return_acf_1": -0.14851845510482495,
        "abs_return_acf_1": 0.4084803270214113,
        "abs_return_acf_5": 0.3980845415342755,
        "abs_return_acf_20": 0.3203968165076707,
        "quantile_01": -0.07688163379355023,
        "quantile_99": 0.0672255536905963,
        "hill_tail_index": 2.5787411247767875
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019122221007692796,
        "excess_kurtosis": 9.355544252393935,
        "return_acf_1": -0.030576130168949448,
        "abs_return_acf_1": 0.3527659749148513,
        "abs_return_acf_5": 0.35786531491277107,
        "abs_return_acf_20": 0.26759386037785904,
        "quantile_01": -0.05406953145381752,
        "quantile_99": 0.05801005326548347,
        "hill_tail_index": 2.713055968905945
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.027663791045129383,
        "excess_kurtosis": 32.40975210735188,
        "return_acf_1": -0.243064902682727,
        "abs_return_acf_1": 0.4869319422907796,
        "abs_return_acf_5": 0.45712296204427827,
        "abs_return_acf_20": 0.3040467733482831,
        "quantile_01": -0.08570111504803493,
        "quantile_99": 0.07008232508144006,
        "hill_tail_index": 2.324085138984663
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01842925126136298,
        "excess_kurtosis": 4.726556511665432,
        "return_acf_1": 0.000984768301759667,
        "abs_return_acf_1": 0.39437294153846786,
        "abs_return_acf_5": 0.3966993476073131,
        "abs_return_acf_20": 0.3030387173896406,
        "quantile_01": -0.06659842403652551,
        "quantile_99": 0.05648569036096703,
        "hill_tail_index": 4.843772543726551
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02432422802778114,
        "excess_kurtosis": 24.944522859655855,
        "return_acf_1": -0.16734588080493787,
        "abs_return_acf_1": 0.3845880944032614,
        "abs_return_acf_5": 0.36144362115136486,
        "abs_return_acf_20": 0.3954426962961684,
        "quantile_01": -0.0848710751966018,
        "quantile_99": 0.06833842047028828,
        "hill_tail_index": 1.933076966362935
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.024435887804288632,
        "excess_kurtosis": 19.855866950563897,
        "return_acf_1": -0.1503763696990448,
        "abs_return_acf_1": 0.3753249095454004,
        "abs_return_acf_5": 0.40583845248901784,
        "abs_return_acf_20": 0.3082738624787385,
        "quantile_01": -0.07954560319255687,
        "quantile_99": 0.05804039733406139,
        "hill_tail_index": 2.1410895876215514
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.024537713709082826,
        "excess_kurtosis": 14.815718533671024,
        "return_acf_1": -0.12047622366343193,
        "abs_return_acf_1": 0.39250408362588385,
        "abs_return_acf_5": 0.41820685615540754,
        "abs_return_acf_20": 0.3639623178580877,
        "quantile_01": -0.09050417170124993,
        "quantile_99": 0.07428874553385093,
        "hill_tail_index": 2.9891155769353306
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019091747422893473,
        "excess_kurtosis": 6.849772988353761,
        "return_acf_1": -0.13232873689041807,
        "abs_return_acf_1": 0.34024271773654013,
        "abs_return_acf_5": 0.38930500103889176,
        "abs_return_acf_20": 0.2896573536198816,
        "quantile_01": -0.06733651375693703,
        "quantile_99": 0.05491300064286363,
        "hill_tail_index": 3.17247013173648
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017096249440002056,
        "excess_kurtosis": 5.200872148312529,
        "return_acf_1": 0.003894031404083719,
        "abs_return_acf_1": 0.270322767517893,
        "abs_return_acf_5": 0.25107563886928563,
        "abs_return_acf_20": 0.25834741563755476,
        "quantile_01": -0.057048321822758416,
        "quantile_99": 0.05025792524923128,
        "hill_tail_index": 3.2812332885828934
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024281720503185326,
        "excess_kurtosis": 14.620582326630402,
        "return_acf_1": -0.20098192537437945,
        "abs_return_acf_1": 0.42047234337741246,
        "abs_return_acf_5": 0.41252078794599856,
        "abs_return_acf_20": 0.3361442225609825,
        "quantile_01": -0.07083454111055865,
        "quantile_99": 0.0654236355274519,
        "hill_tail_index": 2.14544516048003
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02040656118643905,
        "excess_kurtosis": 12.541106233162196,
        "return_acf_1": -0.021372509119037625,
        "abs_return_acf_1": 0.37836659886258717,
        "abs_return_acf_5": 0.34900694407427446,
        "abs_return_acf_20": 0.2600362220871037,
        "quantile_01": -0.0667836775323975,
        "quantile_99": 0.05822978987808558,
        "hill_tail_index": 2.5879851586060174
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.027042540776396205,
        "excess_kurtosis": 18.946183141445097,
        "return_acf_1": -0.2254427316026535,
        "abs_return_acf_1": 0.4105410646936581,
        "abs_return_acf_5": 0.37623869358806816,
        "abs_return_acf_20": 0.31017200754774893,
        "quantile_01": -0.1080568267718977,
        "quantile_99": 0.07192790137202076,
        "hill_tail_index": 2.265817290109864
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02377388682657854,
        "excess_kurtosis": 17.880116311515287,
        "return_acf_1": -0.05568991397017626,
        "abs_return_acf_1": 0.37054861802598327,
        "abs_return_acf_5": 0.3606529386887746,
        "abs_return_acf_20": 0.3154500692172788,
        "quantile_01": -0.08846268217278999,
        "quantile_99": 0.058549170794925685,
        "hill_tail_index": 1.9573379600855276
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01653365992178492,
        "excess_kurtosis": 5.049560269673368,
        "return_acf_1": -0.003961807724336418,
        "abs_return_acf_1": 0.27136488882105925,
        "abs_return_acf_5": 0.21943583054246482,
        "abs_return_acf_20": 0.19986042098346588,
        "quantile_01": -0.04860538164561981,
        "quantile_99": 0.04177013428524869,
        "hill_tail_index": 3.3872577736505463
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017349059218132745,
        "excess_kurtosis": 5.270102031075503,
        "return_acf_1": -0.08518431030714912,
        "abs_return_acf_1": 0.2561949369201077,
        "abs_return_acf_5": 0.30217436989857593,
        "abs_return_acf_20": 0.2050009381520129,
        "quantile_01": -0.05149184261579701,
        "quantile_99": 0.04998438128679135,
        "hill_tail_index": 3.9124708040528655
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019613588053224246,
        "excess_kurtosis": 7.693007084652056,
        "return_acf_1": -0.12461740200483674,
        "abs_return_acf_1": 0.36989812289230467,
        "abs_return_acf_5": 0.4122831603943039,
        "abs_return_acf_20": 0.2755471591637624,
        "quantile_01": -0.06431358823428432,
        "quantile_99": 0.060872840123108354,
        "hill_tail_index": 3.55082624483592
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020384405088346283,
        "excess_kurtosis": 11.392939968769573,
        "return_acf_1": -0.009962152318183565,
        "abs_return_acf_1": 0.3618314772579386,
        "abs_return_acf_5": 0.3383013356347795,
        "abs_return_acf_20": 0.34640176193093786,
        "quantile_01": -0.06425650392000389,
        "quantile_99": 0.0552712548209577,
        "hill_tail_index": 3.0076692707144614
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022364739488551347,
        "excess_kurtosis": 8.701695754025712,
        "return_acf_1": -0.10849136428831747,
        "abs_return_acf_1": 0.41985651463647067,
        "abs_return_acf_5": 0.39787563280112787,
        "abs_return_acf_20": 0.36577844708412555,
        "quantile_01": -0.08060318227824993,
        "quantile_99": 0.07138856267834649,
        "hill_tail_index": 3.676167289258992
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02515733298996125,
        "excess_kurtosis": 16.315742789521,
        "return_acf_1": -0.10147991374518761,
        "abs_return_acf_1": 0.44264908665639396,
        "abs_return_acf_5": 0.3997606198653714,
        "abs_return_acf_20": 0.36729632113903654,
        "quantile_01": -0.08938907384249296,
        "quantile_99": 0.0704202196175168,
        "hill_tail_index": 2.817880684567368
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022521732450644812,
        "excess_kurtosis": 15.849324730511974,
        "return_acf_1": -0.1557034850610839,
        "abs_return_acf_1": 0.378153311187183,
        "abs_return_acf_5": 0.33809514004564845,
        "abs_return_acf_20": 0.2762782296197405,
        "quantile_01": -0.08261979202983318,
        "quantile_99": 0.05559936969844782,
        "hill_tail_index": 2.356414733746349
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
