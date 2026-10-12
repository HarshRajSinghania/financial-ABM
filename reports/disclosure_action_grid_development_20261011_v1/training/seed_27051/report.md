# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27051
Run ID: `ac4356c01eeeb1e3ad20a417cdd03166707eeae15c0914a4c5deba74ac761bab`
Result fingerprint: `ce92a0e6ae3fa8b4120f1dc6b19b4f7346f81f52bd4cbf2caf6d988c0f220e06`

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
    "equal_weight_sd": -0.6240476190476159,
    "equal_weight_raw": -9.36071428571424,
    "fixed_start_cap_weight_sd": -0.6237037098112983,
    "fixed_start_cap_weight_raw": -9.355555647169476,
    "end_cap_weight_sd": -0.6303019124678051,
    "end_cap_weight_raw": -9.454528687017076
  },
  "full_period_change": {
    "equal_weight_sd": -0.9457380952380903,
    "equal_weight_raw": -14.186071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8801157407407363,
    "inflation_mean_sd": 0.6111183862433863
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3283333333333365,
    "equal_weight_raw": 4.925000000000048,
    "fixed_start_cap_weight_sd": 0.32867724256965386,
    "fixed_start_cap_weight_raw": 4.930158638544808,
    "end_cap_weight_sd": 0.3220790399131471,
    "end_cap_weight_raw": 4.831185598697207
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5740476190476157,
      "change_raw": -8.610714285714236,
      "decay_adjusted_gain_sd": 0.3783333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6801587301587269,
      "change_raw": -10.202380952380903,
      "decay_adjusted_gain_sd": 0.2722222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.6043253968253937,
      "change_raw": -9.064880952380905,
      "decay_adjusted_gain_sd": 0.34805555555555867
    },
    "large_minus_small_sd": 0.03027777777777796,
    "large_minus_small_raw": 0.4541666666666694
  },
  "inflation": {
    "initial_mean_sd": 0.2509166666666667,
    "final_mean_sd": 0.572,
    "mean_sd": 0.4687429919511519,
    "mean_absolute_raw_gap": 7.031144879267278,
    "final_absolute_raw_gap": 8.58,
    "mean_range_fraction": 0.07031144879267277
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.18894670764962335,
    "final_wealth_share": 0.3037069294526792
  },
  "pricing_slope": {
    "mean": -0.0023907672721178485,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.12563488836064984,
    "real_improvement_cost": 0.10502836926835757,
    "washing_cost": 0.020606519092292275,
    "fine_transfer": 0.01735010954107833,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.14298499790172817,
    "resource_cost_fraction_initial_cap": 0.004187829612021662,
    "private_net_outflow_fraction_initial_cap": 0.004766166596724273,
    "fine_transfer_fraction_initial_cap": 0.000578336984702611,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0032138404816267232,
    "unapplied_final_day_resource_cost": 0.002541238978222084
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 78.4017889340141,
    "beneficial_raw_gain_per_resource_cost": 1176.0268340102116,
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
    "accrued_cost": 2.829480169533047,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.14671030665742918,
    "accrued_cost_fraction_initial_cap": 0.09431600565110157,
    "mean_contract_rate": 0.039725877479801865,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "maximum_relative_cash_error": 1.620217162752377e-15,
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
      "minimum": -0.15249990796426646,
      "maximum": -0.0004200288459688446,
      "mean": -0.08224038398569997,
      "median": -0.08254741809962254,
      "quantile_05": -0.1430549380909998,
      "quantile_95": -0.0174278710655008
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
      "minimum": 0.2603033376849697,
      "maximum": 0.794264454078594,
      "mean": 0.4825078417270276,
      "median": 0.44113880910104275,
      "quantile_05": 0.3129036276653381,
      "quantile_95": 0.7245735065485759
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
        "daily_volatility": 0.02206783469777807,
        "excess_kurtosis": 14.287197620264951,
        "return_acf_1": -0.08307608094161763,
        "abs_return_acf_1": 0.3798085507003617,
        "abs_return_acf_5": 0.3564910920854039,
        "abs_return_acf_20": 0.23871495266882506,
        "quantile_01": -0.07112997819490516,
        "quantile_99": 0.05656951001778228,
        "hill_tail_index": 2.532425301649781
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020734584341608193,
        "excess_kurtosis": 8.700086683550659,
        "return_acf_1": -0.08310481792567674,
        "abs_return_acf_1": 0.4479459659726355,
        "abs_return_acf_5": 0.4202745155088021,
        "abs_return_acf_20": 0.2752757700148857,
        "quantile_01": -0.0713119359712829,
        "quantile_99": 0.05514636121074452,
        "hill_tail_index": 4.240996162987801
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02020490404442061,
        "excess_kurtosis": 10.821361607593975,
        "return_acf_1": -0.058161598683570646,
        "abs_return_acf_1": 0.4005881091140476,
        "abs_return_acf_5": 0.40823467745237335,
        "abs_return_acf_20": 0.29182005325648114,
        "quantile_01": -0.06688754512562615,
        "quantile_99": 0.0504873104321027,
        "hill_tail_index": 2.5789023090364145
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017898162872230904,
        "excess_kurtosis": 7.286248789956984,
        "return_acf_1": -0.06213867390174693,
        "abs_return_acf_1": 0.29641152477699034,
        "abs_return_acf_5": 0.33499553598714754,
        "abs_return_acf_20": 0.271589735356641,
        "quantile_01": -0.05224847813192834,
        "quantile_99": 0.0468289759366976,
        "hill_tail_index": 3.005813142564127
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018875109236462153,
        "excess_kurtosis": 4.279870498793701,
        "return_acf_1": -0.049525668275801696,
        "abs_return_acf_1": 0.2885011212615538,
        "abs_return_acf_5": 0.3275774407358737,
        "abs_return_acf_20": 0.32514406158976156,
        "quantile_01": -0.05942668443083427,
        "quantile_99": 0.053967413681233284,
        "hill_tail_index": 4.930372557632715
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021766712931011463,
        "excess_kurtosis": 13.965572422447252,
        "return_acf_1": -0.12944759229657743,
        "abs_return_acf_1": 0.43459704951716216,
        "abs_return_acf_5": 0.3924578988339528,
        "abs_return_acf_20": 0.3287943237227428,
        "quantile_01": -0.06568636698197962,
        "quantile_99": 0.06121972074271493,
        "hill_tail_index": 2.7198853973047536
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019650219325840535,
        "excess_kurtosis": 8.701744903387258,
        "return_acf_1": -0.07790211276669569,
        "abs_return_acf_1": 0.40742165971535543,
        "abs_return_acf_5": 0.3739239196075789,
        "abs_return_acf_20": 0.3792109628772283,
        "quantile_01": -0.06333691803789507,
        "quantile_99": 0.06055744392013397,
        "hill_tail_index": 2.976835084222021
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018579196488548385,
        "excess_kurtosis": 8.401600226516969,
        "return_acf_1": -0.08113099894813046,
        "abs_return_acf_1": 0.31138906816540285,
        "abs_return_acf_5": 0.31988971336462674,
        "abs_return_acf_20": 0.2620225805206597,
        "quantile_01": -0.05719834482020129,
        "quantile_99": 0.05571263402201389,
        "hill_tail_index": 2.8978485879939693
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021638296545937317,
        "excess_kurtosis": 28.004307488212064,
        "return_acf_1": -0.04245825043464131,
        "abs_return_acf_1": 0.4746159713069238,
        "abs_return_acf_5": 0.43475537242458173,
        "abs_return_acf_20": 0.23571052737909237,
        "quantile_01": -0.05536585235915406,
        "quantile_99": 0.05510645507770936,
        "hill_tail_index": 1.7437553375856407
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021469277799431752,
        "excess_kurtosis": 14.839133460606899,
        "return_acf_1": -0.0004200288459688446,
        "abs_return_acf_1": 0.380532879987092,
        "abs_return_acf_5": 0.37273736056776174,
        "abs_return_acf_20": 0.23167035639003272,
        "quantile_01": -0.0700972548088564,
        "quantile_99": 0.07221011115596705,
        "hill_tail_index": 2.5102329115301827
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019817756604730254,
        "excess_kurtosis": 7.826748913388631,
        "return_acf_1": -0.06882763419367494,
        "abs_return_acf_1": 0.3720320332691058,
        "abs_return_acf_5": 0.41325278578521324,
        "abs_return_acf_20": 0.313236372478429,
        "quantile_01": -0.05668321018314797,
        "quantile_99": 0.06098932253870536,
        "hill_tail_index": 3.283495061923687
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019405601495944308,
        "excess_kurtosis": 7.498540776763235,
        "return_acf_1": -0.09072931034175907,
        "abs_return_acf_1": 0.2760830999223861,
        "abs_return_acf_5": 0.30735950571715315,
        "abs_return_acf_20": 0.3290580001451661,
        "quantile_01": -0.06249955488253403,
        "quantile_99": 0.06364033868471748,
        "hill_tail_index": 3.6850355787463838
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021659432501024256,
        "excess_kurtosis": 11.278153575885147,
        "return_acf_1": -0.02228792164373656,
        "abs_return_acf_1": 0.40148800883108426,
        "abs_return_acf_5": 0.3802584819573029,
        "abs_return_acf_20": 0.32398678820046767,
        "quantile_01": -0.08292796214345083,
        "quantile_99": 0.052733761706416096,
        "hill_tail_index": 2.468563670037605
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02106889082166128,
        "excess_kurtosis": 6.655323943391899,
        "return_acf_1": -0.10448911280483454,
        "abs_return_acf_1": 0.40391463027721924,
        "abs_return_acf_5": 0.38814345558427665,
        "abs_return_acf_20": 0.3077688801748276,
        "quantile_01": -0.07273638773532169,
        "quantile_99": 0.06420471912055584,
        "hill_tail_index": 4.1561502048603
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0198408150875934,
        "excess_kurtosis": 6.670848455136182,
        "return_acf_1": -0.10964342168703808,
        "abs_return_acf_1": 0.33882020223676795,
        "abs_return_acf_5": 0.35222109297452786,
        "abs_return_acf_20": 0.22527273417782986,
        "quantile_01": -0.055804317324318335,
        "quantile_99": 0.06121862428994605,
        "hill_tail_index": 2.954860476415103
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02090595861002315,
        "excess_kurtosis": 8.11026564572299,
        "return_acf_1": -0.09977235269284804,
        "abs_return_acf_1": 0.41119471110725936,
        "abs_return_acf_5": 0.38121421239781533,
        "abs_return_acf_20": 0.27442322553069537,
        "quantile_01": -0.06870634423415393,
        "quantile_99": 0.05823246271714126,
        "hill_tail_index": 2.3885833518062594
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019371369829754407,
        "excess_kurtosis": 8.95722927325381,
        "return_acf_1": -0.07296826746360036,
        "abs_return_acf_1": 0.43588984351671894,
        "abs_return_acf_5": 0.41261004589566086,
        "abs_return_acf_20": 0.2896613481914529,
        "quantile_01": -0.06607025453973032,
        "quantile_99": 0.055174416915855076,
        "hill_tail_index": 3.669563828487092
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02032636219617325,
        "excess_kurtosis": 4.133162371371636,
        "return_acf_1": -0.12853157420719064,
        "abs_return_acf_1": 0.3538851891742454,
        "abs_return_acf_5": 0.37726811133795946,
        "abs_return_acf_20": 0.3507359075448891,
        "quantile_01": -0.06060122875337157,
        "quantile_99": 0.06587632743331566,
        "hill_tail_index": 4.9591334399279186
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020689407826883402,
        "excess_kurtosis": 18.746359970396302,
        "return_acf_1": -0.0882176240786778,
        "abs_return_acf_1": 0.42666194665187585,
        "abs_return_acf_5": 0.3304908919085673,
        "abs_return_acf_20": 0.33673085807613007,
        "quantile_01": -0.06762339630684865,
        "quantile_99": 0.05333122440819594,
        "hill_tail_index": 2.163918350283178
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017829175703337072,
        "excess_kurtosis": 17.435657545397575,
        "return_acf_1": -0.10220110787462015,
        "abs_return_acf_1": 0.30047017430191125,
        "abs_return_acf_5": 0.2631666643650624,
        "abs_return_acf_20": 0.20827374633443918,
        "quantile_01": -0.04979309189271699,
        "quantile_99": 0.035220927368990934,
        "hill_tail_index": 1.9422502099650196
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020592614629409273,
        "excess_kurtosis": 21.788323914765623,
        "return_acf_1": -0.092482099132203,
        "abs_return_acf_1": 0.460568093596434,
        "abs_return_acf_5": 0.4122936675623573,
        "abs_return_acf_20": 0.31273025529643217,
        "quantile_01": -0.05855591717988933,
        "quantile_99": 0.047356443220586575,
        "hill_tail_index": 1.863303496762137
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022353114658809684,
        "excess_kurtosis": 16.60605133272246,
        "return_acf_1": -0.11622570988799148,
        "abs_return_acf_1": 0.529207488098098,
        "abs_return_acf_5": 0.34616732856756366,
        "abs_return_acf_20": 0.24741995740979392,
        "quantile_01": -0.06825318194441145,
        "quantile_99": 0.05958450193218415,
        "hill_tail_index": 2.592473832127244
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018819739083750564,
        "excess_kurtosis": 5.722036986548305,
        "return_acf_1": -0.06315717010574745,
        "abs_return_acf_1": 0.32737158261251675,
        "abs_return_acf_5": 0.31208309400029466,
        "abs_return_acf_20": 0.2900790669955195,
        "quantile_01": -0.05544308446566051,
        "quantile_99": 0.062051472594515114,
        "hill_tail_index": 4.427085229272962
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01900385115614016,
        "excess_kurtosis": 4.437768508050291,
        "return_acf_1": -0.15249990796426646,
        "abs_return_acf_1": 0.3477363227165824,
        "abs_return_acf_5": 0.36652668806849736,
        "abs_return_acf_20": 0.31382585516599826,
        "quantile_01": -0.05865408365240104,
        "quantile_99": 0.05182512801754942,
        "hill_tail_index": 4.491030899097061
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02108937978635365,
        "excess_kurtosis": 8.179713951084898,
        "return_acf_1": -0.06159050565759931,
        "abs_return_acf_1": 0.43493505611518224,
        "abs_return_acf_5": 0.3684458970493258,
        "abs_return_acf_20": 0.2892798685145641,
        "quantile_01": -0.07039219521951351,
        "quantile_99": 0.06914727729382777,
        "hill_tail_index": 3.7500455074198173
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02193303790268397,
        "excess_kurtosis": 20.286876827934275,
        "return_acf_1": -0.04486849027240503,
        "abs_return_acf_1": 0.4950809117473101,
        "abs_return_acf_5": 0.42751820434390575,
        "abs_return_acf_20": 0.3020751159277064,
        "quantile_01": -0.06840205666251511,
        "quantile_99": 0.0549192830469559,
        "hill_tail_index": 2.1192951125963218
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02186905886069419,
        "excess_kurtosis": 5.546713152208859,
        "return_acf_1": -0.14180857789794254,
        "abs_return_acf_1": 0.31057928239071747,
        "abs_return_acf_5": 0.36469276003757817,
        "abs_return_acf_20": 0.33442732316438883,
        "quantile_01": -0.0650840202842807,
        "quantile_99": 0.06745524965906374,
        "hill_tail_index": 3.473395552653329
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018474207254755615,
        "excess_kurtosis": 6.244227070788536,
        "return_acf_1": -0.08201875525762746,
        "abs_return_acf_1": 0.3503501316068536,
        "abs_return_acf_5": 0.3665850581995716,
        "abs_return_acf_20": 0.34988502013267925,
        "quantile_01": -0.05480589807937835,
        "quantile_99": 0.04825265055147751,
        "hill_tail_index": 3.417435653666535
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022319249108139583,
        "excess_kurtosis": 7.772492472401842,
        "return_acf_1": -0.14407468733986487,
        "abs_return_acf_1": 0.40570321802137677,
        "abs_return_acf_5": 0.393011646911105,
        "abs_return_acf_20": 0.31448990012206596,
        "quantile_01": -0.06880619622533829,
        "quantile_99": 0.06154858778622926,
        "hill_tail_index": 2.985681577551264
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019515488432887595,
        "excess_kurtosis": 5.177823554120872,
        "return_acf_1": -0.013451466046944227,
        "abs_return_acf_1": 0.35742032929215467,
        "abs_return_acf_5": 0.39521479754579236,
        "abs_return_acf_20": 0.357246031146761,
        "quantile_01": -0.054090545159280565,
        "quantile_99": 0.05920125779713593,
        "hill_tail_index": 4.072394412492686
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
