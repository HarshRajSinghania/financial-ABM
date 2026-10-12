# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27241
Run ID: `fe640f940afbdccdca626b750503ecc43df12c42e12bed7833a220c742b7eae2`
Result fingerprint: `2a00a0b8c349af0fafcece425aeea28b6271cfca31c2ba98955625d2fe8eee56`

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
    "equal_weight_sd": -0.6548809523809492,
    "equal_weight_raw": -9.823214285714236,
    "fixed_start_cap_weight_sd": -0.6372198336578313,
    "fixed_start_cap_weight_raw": -9.55829750486747,
    "end_cap_weight_sd": -0.6349919705201474,
    "end_cap_weight_raw": -9.52487955780221
  },
  "full_period_change": {
    "equal_weight_sd": -1.068821428571424,
    "equal_weight_raw": -16.032321428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0010658068783023,
    "inflation_mean_sd": 0.34281183862433867
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2975000000000033,
    "equal_weight_raw": 4.462500000000049,
    "fixed_start_cap_weight_sd": 0.31516111872312086,
    "fixed_start_cap_weight_raw": 4.727416780846813,
    "end_cap_weight_sd": 0.31738898186080505,
    "end_cap_weight_raw": 4.760834727912075
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8540476190476163,
      "change_raw": -12.810714285714244,
      "decay_adjusted_gain_sd": 0.0983333333333359
    },
    "mid": {
      "count": 9,
      "change_sd": -0.18238095238094876,
      "change_raw": -2.7357142857142316,
      "decay_adjusted_gain_sd": 0.7700000000000036
    },
    "small": {
      "count": 18,
      "change_sd": -0.8579365079365047,
      "change_raw": -12.86904761904757,
      "decay_adjusted_gain_sd": 0.09444444444444762
    },
    "large_minus_small_sd": 0.0038888888888883866,
    "large_minus_small_raw": 0.0583333333333258
  },
  "inflation": {
    "initial_mean_sd": 0.2914166666666667,
    "final_mean_sd": 0.3450833333333334,
    "mean_sd": 0.321877671384957,
    "mean_absolute_raw_gap": 4.8281650707743555,
    "final_absolute_raw_gap": 5.1762500000000005,
    "mean_range_fraction": 0.048281650707743554
  },
  "impact": {
    "initial_share": 0.25333333333333335,
    "final_share": 0.26,
    "initial_wealth_share": 0.2290070395965421,
    "final_wealth_share": 0.25491924620978634
  },
  "pricing_slope": {
    "mean": -0.0016334072509585809,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.07143918462167162,
    "real_improvement_cost": 0.06775514612767145,
    "washing_cost": 0.003684038494000171,
    "fine_transfer": 0.014930489960370838,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08636967458204246,
    "resource_cost_fraction_initial_cap": 0.00238130615405572,
    "private_net_outflow_fraction_initial_cap": 0.0028789891527347482,
    "fine_transfer_fraction_initial_cap": 0.0004976829986790279,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.000834112778798394,
    "unapplied_final_day_resource_cost": 6.57573728419035e-06
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 124.93143709947431,
    "beneficial_raw_gain_per_resource_cost": 1873.9715564921146,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 2.751282259636291,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.22490821655418633,
    "accrued_cost_fraction_initial_cap": 0.09170940865454301,
    "mean_contract_rate": 0.03863456121932328,
    "maximum_ledger_error": 6.098637220230962e-20
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.404311863996633e-15,
    "maximum_absolute_share_error": 1.6653345369377348e-15,
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
      "minimum": -0.20170659285388526,
      "maximum": -0.025066634154202943,
      "mean": -0.11956924906037011,
      "median": -0.11164107953370508,
      "quantile_05": -0.19173143700154524,
      "quantile_95": -0.04112884162808562
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
      "minimum": 0.3120625333279143,
      "maximum": 0.7365833827045867,
      "mean": 0.460170410351169,
      "median": 0.43438033344743326,
      "quantile_05": 0.34673284800653736,
      "quantile_95": 0.6599057280444816
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
        "daily_volatility": 0.017841237703105754,
        "excess_kurtosis": 4.139617949970119,
        "return_acf_1": -0.16899841362752488,
        "abs_return_acf_1": 0.2951173569406097,
        "abs_return_acf_5": 0.32270509729956837,
        "abs_return_acf_20": 0.26587865379948145,
        "quantile_01": -0.053197374655096843,
        "quantile_99": 0.05371232898308087,
        "hill_tail_index": 3.649649424705086
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01813682391386429,
        "excess_kurtosis": 7.079478422700181,
        "return_acf_1": -0.20170659285388526,
        "abs_return_acf_1": 0.416906982914151,
        "abs_return_acf_5": 0.373054731487212,
        "abs_return_acf_20": 0.23293586563077254,
        "quantile_01": -0.05311537776184775,
        "quantile_99": 0.05205053336521533,
        "hill_tail_index": 3.1084520944812284
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016415608726339338,
        "excess_kurtosis": 4.962724259105145,
        "return_acf_1": -0.055556414951339034,
        "abs_return_acf_1": 0.24430413301714865,
        "abs_return_acf_5": 0.2349693771779398,
        "abs_return_acf_20": 0.15517708820617004,
        "quantile_01": -0.04194568199722057,
        "quantile_99": 0.04327602435250729,
        "hill_tail_index": 3.5198739160482053
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.015643325147635494,
        "excess_kurtosis": 3.538363219282065,
        "return_acf_1": -0.09437299807187875,
        "abs_return_acf_1": 0.21512779861866785,
        "abs_return_acf_5": 0.18488825748265647,
        "abs_return_acf_20": 0.13917890871979613,
        "quantile_01": -0.04312027668617891,
        "quantile_99": 0.034427946463984234,
        "hill_tail_index": 3.1721263409468836
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016402021398881375,
        "excess_kurtosis": 4.274491641252374,
        "return_acf_1": -0.12607345554829,
        "abs_return_acf_1": 0.27295332184748405,
        "abs_return_acf_5": 0.19360615460248728,
        "abs_return_acf_20": 0.172705095084512,
        "quantile_01": -0.051676730842616724,
        "quantile_99": 0.04284780626817435,
        "hill_tail_index": 3.049481115279282
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018374890014552996,
        "excess_kurtosis": 4.6103380087002614,
        "return_acf_1": -0.09180216803282325,
        "abs_return_acf_1": 0.35851124309200066,
        "abs_return_acf_5": 0.2749111221677319,
        "abs_return_acf_20": 0.2105852451256571,
        "quantile_01": -0.05498543628620362,
        "quantile_99": 0.05112422010659912,
        "hill_tail_index": 3.248200801730599
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01832373509678433,
        "excess_kurtosis": 5.859770055047294,
        "return_acf_1": -0.09468074061551951,
        "abs_return_acf_1": 0.24103034787593622,
        "abs_return_acf_5": 0.2075395364936764,
        "abs_return_acf_20": 0.1957996029769154,
        "quantile_01": -0.053424298250637804,
        "quantile_99": 0.04682776617213143,
        "hill_tail_index": 3.3154281310163425
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019957129030042164,
        "excess_kurtosis": 5.903307394253751,
        "return_acf_1": -0.0293244634545145,
        "abs_return_acf_1": 0.34971540707280785,
        "abs_return_acf_5": 0.30888220742152883,
        "abs_return_acf_20": 0.2833901585812869,
        "quantile_01": -0.059574671767170434,
        "quantile_99": 0.06342253496443138,
        "hill_tail_index": 3.73632253799385
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017604448208532453,
        "excess_kurtosis": 3.9193256297997214,
        "return_acf_1": -0.11411851442645662,
        "abs_return_acf_1": 0.27580077140309284,
        "abs_return_acf_5": 0.2093919762337125,
        "abs_return_acf_20": 0.2716349580087493,
        "quantile_01": -0.051009830220120136,
        "quantile_99": 0.04783841611777455,
        "hill_tail_index": 3.889630629008413
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01726346335755489,
        "excess_kurtosis": 5.350891381522619,
        "return_acf_1": -0.16480578235819351,
        "abs_return_acf_1": 0.339055507015012,
        "abs_return_acf_5": 0.25197116859725566,
        "abs_return_acf_20": 0.22406023866281077,
        "quantile_01": -0.04929769481098196,
        "quantile_99": 0.043536635443358465,
        "hill_tail_index": 2.68690987720664
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01667351788651099,
        "excess_kurtosis": 2.738365966676046,
        "return_acf_1": -0.099820358343696,
        "abs_return_acf_1": 0.27383033799715495,
        "abs_return_acf_5": 0.25833564709270807,
        "abs_return_acf_20": 0.1925676121108467,
        "quantile_01": -0.045224159456642404,
        "quantile_99": 0.04570477132872469,
        "hill_tail_index": 3.956238504395952
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01646627528248284,
        "excess_kurtosis": 3.716697121781161,
        "return_acf_1": -0.12931957283938036,
        "abs_return_acf_1": 0.3114764088571217,
        "abs_return_acf_5": 0.24014371270461937,
        "abs_return_acf_20": 0.2574703079971557,
        "quantile_01": -0.047480757393423036,
        "quantile_99": 0.042507485778395915,
        "hill_tail_index": 4.010590597973443
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01651593593508648,
        "excess_kurtosis": 9.131824769257873,
        "return_acf_1": -0.07024914066912083,
        "abs_return_acf_1": 0.329549152942365,
        "abs_return_acf_5": 0.2909723623472508,
        "abs_return_acf_20": 0.23369654983034152,
        "quantile_01": -0.051332912289584434,
        "quantile_99": 0.04613248329466272,
        "hill_tail_index": 2.625263139020251
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017307431285396496,
        "excess_kurtosis": 3.4726755664858695,
        "return_acf_1": -0.17999203857268734,
        "abs_return_acf_1": 0.2873403329630539,
        "abs_return_acf_5": 0.22214128144122455,
        "abs_return_acf_20": 0.20038339003338437,
        "quantile_01": -0.05420172972389198,
        "quantile_99": 0.048599323702792734,
        "hill_tail_index": 4.1907025008711045
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016790042833405294,
        "excess_kurtosis": 2.162126510092331,
        "return_acf_1": -0.10123942432594206,
        "abs_return_acf_1": 0.31093214087190807,
        "abs_return_acf_5": 0.2625612972918743,
        "abs_return_acf_20": 0.15712228334693135,
        "quantile_01": -0.046116458397143005,
        "quantile_99": 0.044090111826705455,
        "hill_tail_index": 4.783739045482128
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01768962494368166,
        "excess_kurtosis": 5.845508942921985,
        "return_acf_1": -0.1670299800997948,
        "abs_return_acf_1": 0.3893789852486322,
        "abs_return_acf_5": 0.33357545567392827,
        "abs_return_acf_20": 0.19302945697127327,
        "quantile_01": -0.04678328092076593,
        "quantile_99": 0.044093428993661817,
        "hill_tail_index": 2.783711731120062
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01917211208731403,
        "excess_kurtosis": 9.76151279967376,
        "return_acf_1": -0.025066634154202943,
        "abs_return_acf_1": 0.31983116136788314,
        "abs_return_acf_5": 0.3173890071589006,
        "abs_return_acf_20": 0.2482857235297967,
        "quantile_01": -0.06283481352819055,
        "quantile_99": 0.05142832433048816,
        "hill_tail_index": 2.698533035778874
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016441631585686463,
        "excess_kurtosis": 3.255211390570242,
        "return_acf_1": -0.13436996828532224,
        "abs_return_acf_1": 0.22784738053211404,
        "abs_return_acf_5": 0.23795315795230487,
        "abs_return_acf_20": 0.1970098252298824,
        "quantile_01": -0.04636989767958748,
        "quantile_99": 0.040598257989420614,
        "hill_tail_index": 3.1766653275368597
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.015418830036281628,
        "excess_kurtosis": 4.2145447120641,
        "return_acf_1": -0.10517043899154174,
        "abs_return_acf_1": 0.19512557036089673,
        "abs_return_acf_5": 0.17615155519442,
        "abs_return_acf_20": 0.23284566318447955,
        "quantile_01": -0.037981136005668825,
        "quantile_99": 0.03666309435311423,
        "hill_tail_index": 3.217177724078369
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01790414979108161,
        "excess_kurtosis": 4.5131234337185395,
        "return_acf_1": -0.10359179775932041,
        "abs_return_acf_1": 0.3214609642154321,
        "abs_return_acf_5": 0.2769629605964338,
        "abs_return_acf_20": 0.19838443159780014,
        "quantile_01": -0.05256426167492325,
        "quantile_99": 0.04945962229721835,
        "hill_tail_index": 4.007517151426875
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019052612690607425,
        "excess_kurtosis": 7.130908095236995,
        "return_acf_1": -0.14216434013266768,
        "abs_return_acf_1": 0.36859378536414045,
        "abs_return_acf_5": 0.40698848340864324,
        "abs_return_acf_20": 0.25517746718153955,
        "quantile_01": -0.05445640765175013,
        "quantile_99": 0.05142576345493578,
        "hill_tail_index": 2.5349924316158217
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018956418654076282,
        "excess_kurtosis": 14.757584393330543,
        "return_acf_1": -0.10536923415939517,
        "abs_return_acf_1": 0.286786605036386,
        "abs_return_acf_5": 0.38965680392063695,
        "abs_return_acf_20": 0.21440305671787288,
        "quantile_01": -0.05940681607384212,
        "quantile_99": 0.04708795977982448,
        "hill_tail_index": 2.4264284855206673
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01649138353688009,
        "excess_kurtosis": 3.5426140256336343,
        "return_acf_1": -0.12133517022448324,
        "abs_return_acf_1": 0.2535930874141927,
        "abs_return_acf_5": 0.23861435983422827,
        "abs_return_acf_20": 0.22500035062138626,
        "quantile_01": -0.04518345624123172,
        "quantile_99": 0.0426057751908451,
        "hill_tail_index": 4.094314563141215
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01979195113908005,
        "excess_kurtosis": 7.530173143109915,
        "return_acf_1": -0.13616538303728282,
        "abs_return_acf_1": 0.31940638737468013,
        "abs_return_acf_5": 0.38675956082697693,
        "abs_return_acf_20": 0.2646506729296216,
        "quantile_01": -0.0589850933102769,
        "quantile_99": 0.05971603295561929,
        "hill_tail_index": 3.0410861470855863
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01842335828428801,
        "excess_kurtosis": 4.659996603521543,
        "return_acf_1": -0.15737200383899075,
        "abs_return_acf_1": 0.38215362326076363,
        "abs_return_acf_5": 0.3270029589907196,
        "abs_return_acf_20": 0.3292279585751315,
        "quantile_01": -0.05405198634514647,
        "quantile_99": 0.051927755569787765,
        "hill_tail_index": 4.227015356048294
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01675919218855851,
        "excess_kurtosis": 4.98352478353103,
        "return_acf_1": -0.10916364464095354,
        "abs_return_acf_1": 0.21572287569146342,
        "abs_return_acf_5": 0.20758543586847628,
        "abs_return_acf_20": 0.22316272010944319,
        "quantile_01": -0.0470951875053122,
        "quantile_99": 0.046355778232074346,
        "hill_tail_index": 3.5577808342043413
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01674904559997952,
        "excess_kurtosis": 3.8385725274342777,
        "return_acf_1": -0.14399004081071476,
        "abs_return_acf_1": 0.3318127709010695,
        "abs_return_acf_5": 0.3754348392843228,
        "abs_return_acf_20": 0.19466153425566793,
        "quantile_01": -0.051665913258605665,
        "quantile_99": 0.05158937623375429,
        "hill_tail_index": 4.804311310767763
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018642898892928236,
        "excess_kurtosis": 5.020517253190215,
        "return_acf_1": -0.10519870540622177,
        "abs_return_acf_1": 0.44199142855088974,
        "abs_return_acf_5": 0.3945413419908152,
        "abs_return_acf_20": 0.3106317719392706,
        "quantile_01": -0.052918606076552056,
        "quantile_99": 0.05855038073791096,
        "hill_tail_index": 3.1476998254194517
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017840041219039864,
        "excess_kurtosis": 2.9531757118287594,
        "return_acf_1": -0.20133639935242897,
        "abs_return_acf_1": 0.2615063339582979,
        "abs_return_acf_5": 0.2724945143121584,
        "abs_return_acf_20": 0.1913786449201879,
        "quantile_01": -0.051613966542736506,
        "quantile_99": 0.0502855440126769,
        "hill_tail_index": 4.30276136909477
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017186469186765738,
        "excess_kurtosis": 2.950875017223317,
        "return_acf_1": -0.10769365222653024,
        "abs_return_acf_1": 0.2395142657566142,
        "abs_return_acf_5": 0.1762063407244562,
        "abs_return_acf_20": 0.15270859074767634,
        "quantile_01": -0.05320752223490295,
        "quantile_99": 0.04211163238508372,
        "hill_tail_index": 3.6800290934261013
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
