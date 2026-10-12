# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27224
Run ID: `a205a4e254c63afebfcbb7d09cdd07c48bd5f951dea3e934a29cef1745e94704`
Result fingerprint: `b1216811df3c745a304b7f2da465eab12242a607afcb7a1be73f9a77df3de7d3`

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
    "equal_weight_sd": -0.702614842660842,
    "equal_weight_raw": -10.539222639912627,
    "fixed_start_cap_weight_sd": -0.7475174324100338,
    "fixed_start_cap_weight_raw": -11.212761486150507,
    "end_cap_weight_sd": -0.7703730428659554,
    "end_cap_weight_raw": -11.555595642989328
  },
  "full_period_change": {
    "equal_weight_sd": -1.0620592749059157,
    "equal_weight_raw": -15.930889123588734
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9847332084722382,
    "inflation_mean_sd": 0.5772724867724868
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.20600000000000296,
    "equal_weight_raw": 3.0900000000000447,
    "fixed_start_cap_weight_sd": 0.1878182161374647,
    "fixed_start_cap_weight_raw": 2.8172732420619697,
    "end_cap_weight_sd": 0.17027486464765476,
    "end_cap_weight_raw": 2.554122969714822
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6307142857142826,
      "change_raw": -9.46071428571424,
      "decay_adjusted_gain_sd": 0.3216666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7507142857142826,
      "change_raw": -11.260714285714238,
      "decay_adjusted_gain_sd": 0.20166666666666963
    },
    "small": {
      "count": 18,
      "change_sd": -0.6905485472918814,
      "change_raw": -10.358228209378222,
      "decay_adjusted_gain_sd": 0.1888888888888918
    },
    "large_minus_small_sd": 0.05983426157759886,
    "large_minus_small_raw": 0.8975139236639829
  },
  "inflation": {
    "initial_mean_sd": 0.28141666666666665,
    "final_mean_sd": 0.60925,
    "mean_sd": 0.44653837080210934,
    "mean_absolute_raw_gap": 6.698075562031641,
    "final_absolute_raw_gap": 9.138749999999998,
    "mean_range_fraction": 0.06698075562031641
  },
  "impact": {
    "initial_share": 0.25333333333333335,
    "final_share": 0.4866666666666667,
    "initial_wealth_share": 0.3071488260309856,
    "final_wealth_share": 0.5581324529285729
  },
  "pricing_slope": {
    "mean": -0.001502895279186386,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.014970268925581728,
    "real_improvement_cost": 0.006367654919563596,
    "washing_cost": 0.008602614006018132,
    "fine_transfer": 0.008834510450360064,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.02380477937594179,
    "resource_cost_fraction_initial_cap": 0.0004990089641860576,
    "private_net_outflow_fraction_initial_cap": 0.0007934926458647264,
    "fine_transfer_fraction_initial_cap": 0.0002944836816786688,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00041271028598118936,
    "unapplied_final_day_resource_cost": 0.0014831150260035174
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 412.81823531169067,
    "beneficial_raw_gain_per_resource_cost": 6192.27352967536,
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
    "fixed_exposure": 14.999999999999998,
    "accrued_cost": 3.1478977670110115,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.17170729082053543,
    "accrued_cost_fraction_initial_cap": 0.10492992556703373,
    "mean_contract_rate": 0.04343424922125447,
    "maximum_ledger_error": 7.453889935837843e-20
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
    "maximum_relative_cash_error": 1.866526983719485e-15,
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
      "minimum": -0.17430623495779018,
      "maximum": 0.04312277945467468,
      "mean": -0.05730893133375608,
      "median": -0.04757568085211745,
      "quantile_05": -0.15415693128727306,
      "quantile_95": 0.032111585515081684
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
      "minimum": 0.2053544171126737,
      "maximum": 0.8379715492394272,
      "mean": 0.585039633083064,
      "median": 0.6980242620265171,
      "quantile_05": 0.2588025397255356,
      "quantile_95": 0.8032111898675758
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
        "daily_volatility": 0.024474531907448402,
        "excess_kurtosis": 15.860123927620045,
        "return_acf_1": -0.036775051702121905,
        "abs_return_acf_1": 0.46821087052439614,
        "abs_return_acf_5": 0.45152604954860254,
        "abs_return_acf_20": 0.3902842188250044,
        "quantile_01": -0.09596288609637994,
        "quantile_99": 0.07013537382322958,
        "hill_tail_index": 2.764213954964899
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02651151171643853,
        "excess_kurtosis": 13.612667296887473,
        "return_acf_1": -0.04630199073854291,
        "abs_return_acf_1": 0.4946617002956459,
        "abs_return_acf_5": 0.4031284791143726,
        "abs_return_acf_20": 0.40219720025597583,
        "quantile_01": -0.10719866579507413,
        "quantile_99": 0.07410950075161281,
        "hill_tail_index": 3.2382041856574983
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023259624668554243,
        "excess_kurtosis": 11.414813806756356,
        "return_acf_1": -0.12153338430988901,
        "abs_return_acf_1": 0.39975493651132804,
        "abs_return_acf_5": 0.2852014972581739,
        "abs_return_acf_20": 0.26032666494556006,
        "quantile_01": -0.08367350864882185,
        "quantile_99": 0.06244362279471217,
        "hill_tail_index": 2.898828845665425
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.025017833980628304,
        "excess_kurtosis": 13.870158145532056,
        "return_acf_1": -0.10717079028818223,
        "abs_return_acf_1": 0.5067178705548557,
        "abs_return_acf_5": 0.35189546336027233,
        "abs_return_acf_20": 0.42624340255934634,
        "quantile_01": -0.09960392915801157,
        "quantile_99": 0.06988353725326202,
        "hill_tail_index": 2.711515820715182
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024737421143004337,
        "excess_kurtosis": 9.964501699738351,
        "return_acf_1": -0.04915196875027746,
        "abs_return_acf_1": 0.522012448737123,
        "abs_return_acf_5": 0.4104492882531408,
        "abs_return_acf_20": 0.40587262791619083,
        "quantile_01": -0.09201180683927136,
        "quantile_99": 0.08404097617206421,
        "hill_tail_index": 4.6118975586119895
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020612985034198745,
        "excess_kurtosis": 9.398926903680003,
        "return_acf_1": -0.04736754356286093,
        "abs_return_acf_1": 0.37631668974996574,
        "abs_return_acf_5": 0.2798048907214543,
        "abs_return_acf_20": 0.30619489191504673,
        "quantile_01": -0.07643980856190676,
        "quantile_99": 0.05105335754130845,
        "hill_tail_index": 2.8936702292956675
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019287993799994747,
        "excess_kurtosis": 3.741706251049572,
        "return_acf_1": -0.1566083836040369,
        "abs_return_acf_1": 0.3329358591513241,
        "abs_return_acf_5": 0.24220939167488853,
        "abs_return_acf_20": 0.23531983080340607,
        "quantile_01": -0.05331627773410411,
        "quantile_99": 0.05423433509751945,
        "hill_tail_index": 4.145423361028664
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020259532467291654,
        "excess_kurtosis": 4.588967317119006,
        "return_acf_1": -0.15116071178900617,
        "abs_return_acf_1": 0.3045117904278749,
        "abs_return_acf_5": 0.28581404638025326,
        "abs_return_acf_20": 0.24535266015567006,
        "quantile_01": -0.06102688434281458,
        "quantile_99": 0.05695901774883004,
        "hill_tail_index": 3.517102041410568
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.024026568015930987,
        "excess_kurtosis": 11.7573695829415,
        "return_acf_1": -0.052053734294655006,
        "abs_return_acf_1": 0.5356802673452932,
        "abs_return_acf_5": 0.44113629569791907,
        "abs_return_acf_20": 0.4118455995824358,
        "quantile_01": -0.09138357305672982,
        "quantile_99": 0.0709409695444419,
        "hill_tail_index": 2.46799421402701
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02208483029396989,
        "excess_kurtosis": 8.380608192455616,
        "return_acf_1": -0.17430623495779018,
        "abs_return_acf_1": 0.447037903721313,
        "abs_return_acf_5": 0.3739535611912484,
        "abs_return_acf_20": 0.24664744632152039,
        "quantile_01": -0.07009641422769242,
        "quantile_99": 0.06436223363026584,
        "hill_tail_index": 3.483857800737649
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02625245581674885,
        "excess_kurtosis": 14.236896289992789,
        "return_acf_1": -0.01354379675424351,
        "abs_return_acf_1": 0.4879814968861853,
        "abs_return_acf_5": 0.4672472523907279,
        "abs_return_acf_20": 0.3529557128625649,
        "quantile_01": -0.09870533803376397,
        "quantile_99": 0.08094514783169643,
        "hill_tail_index": 3.759270581890894
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022663128540187878,
        "excess_kurtosis": 11.356415704095225,
        "return_acf_1": 0.020812814237041267,
        "abs_return_acf_1": 0.4270880849928907,
        "abs_return_acf_5": 0.35382321319283855,
        "abs_return_acf_20": 0.3510956343217965,
        "quantile_01": -0.08663527557855424,
        "quantile_99": 0.06033798370463224,
        "hill_tail_index": 2.9760779202788377
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.023002655204677584,
        "excess_kurtosis": 10.739736318300253,
        "return_acf_1": 0.022792145623546662,
        "abs_return_acf_1": 0.5142049922531728,
        "abs_return_acf_5": 0.40993077879244577,
        "abs_return_acf_20": 0.33703380219170875,
        "quantile_01": -0.09613485883803993,
        "quantile_99": 0.06038438963877157,
        "hill_tail_index": 2.9709545275796683
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.025378080981694542,
        "excess_kurtosis": 9.808311665968683,
        "return_acf_1": -0.014449298013574403,
        "abs_return_acf_1": 0.4559173838498761,
        "abs_return_acf_5": 0.39646080297622555,
        "abs_return_acf_20": 0.3730898014068451,
        "quantile_01": -0.10600839412856149,
        "quantile_99": 0.06393337267289323,
        "hill_tail_index": 2.62273474614306
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024065543248052004,
        "excess_kurtosis": 13.121023832606777,
        "return_acf_1": -0.06761824827195001,
        "abs_return_acf_1": 0.43430546899881045,
        "abs_return_acf_5": 0.3575041916555272,
        "abs_return_acf_20": 0.3602530184648858,
        "quantile_01": -0.08460043942836343,
        "quantile_99": 0.06287828522652254,
        "hill_tail_index": 2.7026329300505694
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02522852453952848,
        "excess_kurtosis": 15.215312253545683,
        "return_acf_1": -0.06977718397379046,
        "abs_return_acf_1": 0.48986854653226397,
        "abs_return_acf_5": 0.44458057928090255,
        "abs_return_acf_20": 0.341314937217607,
        "quantile_01": -0.09215361936945825,
        "quantile_99": 0.06574857626300415,
        "hill_tail_index": 2.715179094469709
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02404148248903863,
        "excess_kurtosis": 12.152462506377281,
        "return_acf_1": -0.0011283569989955324,
        "abs_return_acf_1": 0.5057526720068571,
        "abs_return_acf_5": 0.40090274239449636,
        "abs_return_acf_20": 0.32319041447427915,
        "quantile_01": -0.09195094370676235,
        "quantile_99": 0.06479546602608391,
        "hill_tail_index": 2.526572726872066
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.023868444079147597,
        "excess_kurtosis": 9.953819349234934,
        "return_acf_1": -0.09617320638324714,
        "abs_return_acf_1": 0.43688556354881564,
        "abs_return_acf_5": 0.3870487358170328,
        "abs_return_acf_20": 0.3882972971700909,
        "quantile_01": -0.09185895332389646,
        "quantile_99": 0.06381958635164306,
        "hill_tail_index": 3.6776882257554404
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.025382985241474476,
        "excess_kurtosis": 9.634432403635044,
        "return_acf_1": -0.04778381814137397,
        "abs_return_acf_1": 0.4410131710277584,
        "abs_return_acf_5": 0.3750563856606383,
        "abs_return_acf_20": 0.33258110567156324,
        "quantile_01": -0.0850876108933293,
        "quantile_99": 0.0731149707492872,
        "hill_tail_index": 3.134890849470783
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024128886905886576,
        "excess_kurtosis": 13.736297484102337,
        "return_acf_1": 0.018181039897993835,
        "abs_return_acf_1": 0.43221728744080035,
        "abs_return_acf_5": 0.4052393368243103,
        "abs_return_acf_20": 0.3868191489750789,
        "quantile_01": -0.08728331483758565,
        "quantile_99": 0.05670680898053844,
        "hill_tail_index": 3.1635947270404268
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0269288306250523,
        "excess_kurtosis": 13.336539369359244,
        "return_acf_1": 0.04312277945467468,
        "abs_return_acf_1": 0.5440740336464364,
        "abs_return_acf_5": 0.4024442207535062,
        "abs_return_acf_20": 0.4060862906670238,
        "quantile_01": -0.11540690964088071,
        "quantile_99": 0.07908545893675344,
        "hill_tail_index": 2.964286589240513
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.023792074161785,
        "excess_kurtosis": 21.0929254675202,
        "return_acf_1": -0.10057269747152198,
        "abs_return_acf_1": 0.4402833529824773,
        "abs_return_acf_5": 0.34850222306088596,
        "abs_return_acf_20": 0.3492713764930168,
        "quantile_01": -0.0917222864871142,
        "quantile_99": 0.0642542038404908,
        "hill_tail_index": 2.4570887362620017
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022613739144723043,
        "excess_kurtosis": 7.2579487864515375,
        "return_acf_1": -0.1434143826083377,
        "abs_return_acf_1": 0.3815406836128771,
        "abs_return_acf_5": 0.33245942559848524,
        "abs_return_acf_20": 0.32500063866624823,
        "quantile_01": -0.07028973207622854,
        "quantile_99": 0.0685178786802141,
        "hill_tail_index": 3.9649217243890407
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022680379789203044,
        "excess_kurtosis": 6.838243181655468,
        "return_acf_1": -0.11658057060897786,
        "abs_return_acf_1": 0.414580043146499,
        "abs_return_acf_5": 0.35163229484690717,
        "abs_return_acf_20": 0.3358406067032721,
        "quantile_01": -0.06752760547696374,
        "quantile_99": 0.0697469686881367,
        "hill_tail_index": 3.3331719467256016
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02529724675611823,
        "excess_kurtosis": 14.132789503138056,
        "return_acf_1": 0.0073975945804055036,
        "abs_return_acf_1": 0.5109752613987792,
        "abs_return_acf_5": 0.4434377742472989,
        "abs_return_acf_20": 0.3530803490522027,
        "quantile_01": -0.10193283236491156,
        "quantile_99": 0.06772683495153416,
        "hill_tail_index": 3.0349991625580204
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022721163342511952,
        "excess_kurtosis": 11.288786766461618,
        "return_acf_1": 0.039736581789974065,
        "abs_return_acf_1": 0.46415386214548315,
        "abs_return_acf_5": 0.4091010474583111,
        "abs_return_acf_20": 0.36867224989504177,
        "quantile_01": -0.08190025387547759,
        "quantile_99": 0.061944892178713434,
        "hill_tail_index": 3.3349148297221327
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022720893529783497,
        "excess_kurtosis": 11.043440807062337,
        "return_acf_1": -0.04447397130217137,
        "abs_return_acf_1": 0.48544112607025985,
        "abs_return_acf_5": 0.422664751577165,
        "abs_return_acf_20": 0.4188095774241739,
        "quantile_01": -0.08460923258627184,
        "quantile_99": 0.05701379157819232,
        "hill_tail_index": 2.70142659402446
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021632851869917622,
        "excess_kurtosis": 8.983272528688813,
        "return_acf_1": -0.04597853429168305,
        "abs_return_acf_1": 0.39255511490621164,
        "abs_return_acf_5": 0.32253855381423613,
        "abs_return_acf_20": 0.31042495977840157,
        "quantile_01": -0.0849070740847246,
        "quantile_99": 0.05505709533239139,
        "hill_tail_index": 3.2437602418987277
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022599406823214655,
        "excess_kurtosis": 9.516068070971887,
        "return_acf_1": -0.03591656855972856,
        "abs_return_acf_1": 0.45610219093416116,
        "abs_return_acf_5": 0.31667379235657633,
        "abs_return_acf_20": 0.38053870697318415,
        "quantile_01": -0.09337015612656327,
        "quantile_99": 0.06054584942509353,
        "hill_tail_index": 2.998555808089256
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01898907707519139,
        "excess_kurtosis": 4.834225032879757,
        "return_acf_1": -0.13147046821936015,
        "abs_return_acf_1": 0.3316482517301271,
        "abs_return_acf_5": 0.2513395072765532,
        "abs_return_acf_20": 0.25470830256464855,
        "quantile_01": -0.05830048303189843,
        "quantile_99": 0.052593289841041876,
        "hill_tail_index": 4.669442932698803
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
