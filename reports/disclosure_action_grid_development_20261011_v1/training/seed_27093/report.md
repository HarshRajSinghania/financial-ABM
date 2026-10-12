# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27093
Run ID: `36a187838e88310a624850a927bc5f8d88e1e7e9504e20f032cfb899e9e2924f`
Result fingerprint: `50a191acbcc6a24c131c14489b35637c7e874e5ea897b4623c59a5637699b43c`

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
    "equal_weight_sd": -0.5775476190476159,
    "equal_weight_raw": -8.663214285714236,
    "fixed_start_cap_weight_sd": -0.595895611813411,
    "fixed_start_cap_weight_raw": -8.938434177201167,
    "end_cap_weight_sd": -0.5874184738988819,
    "end_cap_weight_raw": -8.811277108483226
  },
  "full_period_change": {
    "equal_weight_sd": -0.947404761904757,
    "equal_weight_raw": -14.211071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8758931878306834,
    "inflation_mean_sd": 0.5639054232804233
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3748333333333365,
    "equal_weight_raw": 5.6225000000000485,
    "fixed_start_cap_weight_sd": 0.35648534056754133,
    "fixed_start_cap_weight_raw": 5.347280108513119,
    "end_cap_weight_sd": 0.3649624784820703,
    "end_cap_weight_raw": 5.474437177231053
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7282142857142825,
      "change_raw": -10.923214285714238,
      "decay_adjusted_gain_sd": 0.2241666666666697
    },
    "mid": {
      "count": 9,
      "change_sd": -0.461269841269838,
      "change_raw": -6.91904761904757,
      "decay_adjusted_gain_sd": 0.4911111111111144
    },
    "small": {
      "count": 18,
      "change_sd": -0.6105753968253935,
      "change_raw": -9.158630952380904,
      "decay_adjusted_gain_sd": 0.34180555555555875
    },
    "large_minus_small_sd": -0.11763888888888896,
    "large_minus_small_raw": -1.7645833333333343
  },
  "inflation": {
    "initial_mean_sd": 0.25383333333333336,
    "final_mean_sd": 0.5707500000000001,
    "mean_sd": 0.41254433805162366,
    "mean_absolute_raw_gap": 6.188165070774355,
    "final_absolute_raw_gap": 8.561250000000001,
    "mean_range_fraction": 0.06188165070774355
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.35976449042032715,
    "final_wealth_share": 0.3872705303306848
  },
  "pricing_slope": {
    "mean": -0.004362456805883765,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.08985579296971069,
    "real_improvement_cost": 0.06610001628711462,
    "washing_cost": 0.023755776682596062,
    "fine_transfer": 0.0035268519561203965,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0933826449258311,
    "resource_cost_fraction_initial_cap": 0.0029951930989903564,
    "private_net_outflow_fraction_initial_cap": 0.0031127548308610364,
    "fine_transfer_fraction_initial_cap": 0.00011756173187067989,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.006909207106510499,
    "unapplied_final_day_resource_cost": 0.007161243258726581
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 125.14496426280105,
    "beneficial_raw_gain_per_resource_cost": 1877.174463942016,
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
    "accrued_cost": 2.8994014128845356,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": 0.07678906330594033,
    "accrued_cost_fraction_initial_cap": 0.09664671376281785,
    "mean_contract_rate": 0.040798347619262536,
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
    "maximum_relative_cash_error": 1.8146220394114012e-15,
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
      "minimum": -0.22330571105218852,
      "maximum": -0.0758202392741271,
      "mean": -0.14280284308279592,
      "median": -0.1437984644059786,
      "quantile_05": -0.2089470475795624,
      "quantile_95": -0.07994138800305677
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
      "minimum": 0.19860473179152566,
      "maximum": 0.8012553630705374,
      "mean": 0.621137033614684,
      "median": 0.6571446333458983,
      "quantile_05": 0.33485444540551873,
      "quantile_95": 0.7624685149510664
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
        "daily_volatility": 0.02168589746342236,
        "excess_kurtosis": 8.768041639146308,
        "return_acf_1": -0.12549461213682916,
        "abs_return_acf_1": 0.48371608505702407,
        "abs_return_acf_5": 0.414118610042924,
        "abs_return_acf_20": 0.3534319945496575,
        "quantile_01": -0.07039022527978725,
        "quantile_99": 0.0670110099669596,
        "hill_tail_index": 3.6140650565649852
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02109970418840119,
        "excess_kurtosis": 11.16832743250563,
        "return_acf_1": -0.22330571105218852,
        "abs_return_acf_1": 0.4879104602342099,
        "abs_return_acf_5": 0.45825708809994603,
        "abs_return_acf_20": 0.33163023740300523,
        "quantile_01": -0.06979484589933321,
        "quantile_99": 0.0642397898262541,
        "hill_tail_index": 3.0439071669664397
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016681517663933994,
        "excess_kurtosis": 4.257370339758358,
        "return_acf_1": -0.08138007495727995,
        "abs_return_acf_1": 0.23646284037503387,
        "abs_return_acf_5": 0.23425182573784012,
        "abs_return_acf_20": 0.21089345771045337,
        "quantile_01": -0.04730994640308907,
        "quantile_99": 0.04716762377029223,
        "hill_tail_index": 3.7134246594406135
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020671263241834454,
        "excess_kurtosis": 4.609104080508484,
        "return_acf_1": -0.13397851484380457,
        "abs_return_acf_1": 0.38184806212665884,
        "abs_return_acf_5": 0.3994606782346226,
        "abs_return_acf_20": 0.2963454651766451,
        "quantile_01": -0.06769501993472612,
        "quantile_99": 0.06038880618331678,
        "hill_tail_index": 4.845919988164172
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02245964411961043,
        "excess_kurtosis": 20.297400288742217,
        "return_acf_1": -0.1686110709844926,
        "abs_return_acf_1": 0.4743000015462553,
        "abs_return_acf_5": 0.4535793714103314,
        "abs_return_acf_20": 0.2951275519688445,
        "quantile_01": -0.07375894416343091,
        "quantile_99": 0.04987345292550282,
        "hill_tail_index": 1.9631269438143564
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017565192433509836,
        "excess_kurtosis": 3.852457674782011,
        "return_acf_1": -0.10550186421426275,
        "abs_return_acf_1": 0.25404079113847977,
        "abs_return_acf_5": 0.2827452228877318,
        "abs_return_acf_20": 0.3267839947578082,
        "quantile_01": -0.05238333856665496,
        "quantile_99": 0.04955308376835157,
        "hill_tail_index": 4.206220021317883
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021185795932635382,
        "excess_kurtosis": 9.535117529462804,
        "return_acf_1": -0.12985149096088935,
        "abs_return_acf_1": 0.47917425719799334,
        "abs_return_acf_5": 0.3977017964598144,
        "abs_return_acf_20": 0.2981816507034236,
        "quantile_01": -0.08034363073349325,
        "quantile_99": 0.05414834879944142,
        "hill_tail_index": 2.706648104081481
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017872182607066044,
        "excess_kurtosis": 4.603839323801776,
        "return_acf_1": -0.10313981635137642,
        "abs_return_acf_1": 0.3287273431533397,
        "abs_return_acf_5": 0.3117639567440817,
        "abs_return_acf_20": 0.22997454177068913,
        "quantile_01": -0.05645036839149778,
        "quantile_99": 0.04715436105331677,
        "hill_tail_index": 4.104044803628541
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022017209896741774,
        "excess_kurtosis": 14.462846296267664,
        "return_acf_1": -0.17003823154089973,
        "abs_return_acf_1": 0.49430794060615735,
        "abs_return_acf_5": 0.4325922588770752,
        "abs_return_acf_20": 0.2927004380372872,
        "quantile_01": -0.07891817658854577,
        "quantile_99": 0.052535978491254784,
        "hill_tail_index": 3.098049840051622
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01812777599256954,
        "excess_kurtosis": 5.241970548567945,
        "return_acf_1": -0.20518889832319234,
        "abs_return_acf_1": 0.3931036928698361,
        "abs_return_acf_5": 0.36127281776098136,
        "abs_return_acf_20": 0.2430954317446633,
        "quantile_01": -0.05398340412068643,
        "quantile_99": 0.044712817941958465,
        "hill_tail_index": 3.1969087901436772
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016435032354149542,
        "excess_kurtosis": 5.581640764116365,
        "return_acf_1": -0.12963274214625795,
        "abs_return_acf_1": 0.3029524647716446,
        "abs_return_acf_5": 0.2774990112541862,
        "abs_return_acf_20": 0.25339826600722515,
        "quantile_01": -0.05620101892995204,
        "quantile_99": 0.039792143496770405,
        "hill_tail_index": 4.3002731214892265
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01990326379795494,
        "excess_kurtosis": 11.031768028742505,
        "return_acf_1": -0.1416020802829494,
        "abs_return_acf_1": 0.3232871278436553,
        "abs_return_acf_5": 0.37894268043053153,
        "abs_return_acf_20": 0.32503015569057503,
        "quantile_01": -0.06884375822262939,
        "quantile_99": 0.05992161904293459,
        "hill_tail_index": 2.7496214352166373
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019007584389595836,
        "excess_kurtosis": 9.623891304137768,
        "return_acf_1": -0.09016557990986614,
        "abs_return_acf_1": 0.35018223996876324,
        "abs_return_acf_5": 0.34157028233302006,
        "abs_return_acf_20": 0.20745914255677342,
        "quantile_01": -0.05729450450597253,
        "quantile_99": 0.04897410592528967,
        "hill_tail_index": 3.243684182212901
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01957447953467951,
        "excess_kurtosis": 5.87435916356911,
        "return_acf_1": -0.19299522047658307,
        "abs_return_acf_1": 0.3197718257615111,
        "abs_return_acf_5": 0.3045734799510611,
        "abs_return_acf_20": 0.3033885355611094,
        "quantile_01": -0.05861835196114286,
        "quantile_99": 0.05726167076770829,
        "hill_tail_index": 3.8477439290749382
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01638472148809268,
        "excess_kurtosis": 3.3114263609295795,
        "return_acf_1": -0.0758202392741271,
        "abs_return_acf_1": 0.24649053503482624,
        "abs_return_acf_5": 0.2982196990922782,
        "abs_return_acf_20": 0.24000449530953713,
        "quantile_01": -0.05369287328029664,
        "quantile_99": 0.03829806667451258,
        "hill_tail_index": 3.453228264658142
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020482327503981455,
        "excess_kurtosis": 8.198560088227367,
        "return_acf_1": -0.1570249831531475,
        "abs_return_acf_1": 0.407787492024581,
        "abs_return_acf_5": 0.3471329378881023,
        "abs_return_acf_20": 0.27402175171810006,
        "quantile_01": -0.06600800796717417,
        "quantile_99": 0.058465808503673,
        "hill_tail_index": 2.8911800667674177
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02090869180648202,
        "excess_kurtosis": 26.07000273559878,
        "return_acf_1": -0.2120218969711379,
        "abs_return_acf_1": 0.421738306605873,
        "abs_return_acf_5": 0.2509213972328197,
        "abs_return_acf_20": 0.25135655798262974,
        "quantile_01": -0.05853289977435786,
        "quantile_99": 0.053114590024559497,
        "hill_tail_index": 2.365688330411825
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02064545923925907,
        "excess_kurtosis": 8.848641873491623,
        "return_acf_1": -0.07876428049505597,
        "abs_return_acf_1": 0.4456552232469958,
        "abs_return_acf_5": 0.4199948670297392,
        "abs_return_acf_20": 0.3477119257871149,
        "quantile_01": -0.07667956738962735,
        "quantile_99": 0.05791341588496937,
        "hill_tail_index": 3.1279757204503897
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02080598277904858,
        "excess_kurtosis": 10.28372512283903,
        "return_acf_1": -0.16761524557181823,
        "abs_return_acf_1": 0.44965008131663475,
        "abs_return_acf_5": 0.4910961617395722,
        "abs_return_acf_20": 0.3392320648703071,
        "quantile_01": -0.07880248525928146,
        "quantile_99": 0.06085698210110835,
        "hill_tail_index": 3.0462226352211963
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021935755569950175,
        "excess_kurtosis": 13.956801191301121,
        "return_acf_1": -0.15178755283480275,
        "abs_return_acf_1": 0.47827896584577034,
        "abs_return_acf_5": 0.39147480247776517,
        "abs_return_acf_20": 0.23441820813171932,
        "quantile_01": -0.07460869567708435,
        "quantile_99": 0.05753195539905591,
        "hill_tail_index": 2.365022155811242
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021738280103913092,
        "excess_kurtosis": 11.640492521550675,
        "return_acf_1": -0.1797292318451444,
        "abs_return_acf_1": 0.4471738078234971,
        "abs_return_acf_5": 0.36754533850503995,
        "abs_return_acf_20": 0.30849561231542816,
        "quantile_01": -0.07173839662677661,
        "quantile_99": 0.06310676460809453,
        "hill_tail_index": 2.881883649608293
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018005247089973656,
        "excess_kurtosis": 4.5123997026966025,
        "return_acf_1": -0.16168633164211357,
        "abs_return_acf_1": 0.3427088545262982,
        "abs_return_acf_5": 0.34770179831140974,
        "abs_return_acf_20": 0.2913914860743315,
        "quantile_01": -0.05156721457873463,
        "quantile_99": 0.05295585999107789,
        "hill_tail_index": 3.7399756863114986
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01923020363198725,
        "excess_kurtosis": 7.24649537691808,
        "return_acf_1": -0.12464140087115715,
        "abs_return_acf_1": 0.37564658170083476,
        "abs_return_acf_5": 0.3735702080518403,
        "abs_return_acf_20": 0.3510982280878412,
        "quantile_01": -0.05884486879304658,
        "quantile_99": 0.0509201071776337,
        "hill_tail_index": 3.2657257291788593
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01814843735011906,
        "excess_kurtosis": 5.941551378036008,
        "return_acf_1": -0.11559336036312755,
        "abs_return_acf_1": 0.39213951211365894,
        "abs_return_acf_5": 0.30497103556875077,
        "abs_return_acf_20": 0.2659481693137733,
        "quantile_01": -0.05236062128616821,
        "quantile_99": 0.05299594137083913,
        "hill_tail_index": 2.9400597988060264
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021924773172265963,
        "excess_kurtosis": 12.484257949715506,
        "return_acf_1": -0.1656489423027082,
        "abs_return_acf_1": 0.5026506563864109,
        "abs_return_acf_5": 0.4622192363402016,
        "abs_return_acf_20": 0.3339906083325888,
        "quantile_01": -0.07511264983269578,
        "quantile_99": 0.05759534116917327,
        "hill_tail_index": 3.031848191078729
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.024234389439883198,
        "excess_kurtosis": 20.7820028162871,
        "return_acf_1": -0.18587499642091038,
        "abs_return_acf_1": 0.5744895660805845,
        "abs_return_acf_5": 0.48261446210146225,
        "abs_return_acf_20": 0.24648362095905388,
        "quantile_01": -0.07458192172335845,
        "quantile_99": 0.06648679220598308,
        "hill_tail_index": 2.549726281881797
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022819354983380738,
        "excess_kurtosis": 13.002606867726122,
        "return_acf_1": -0.1459948485290078,
        "abs_return_acf_1": 0.4721325611219995,
        "abs_return_acf_5": 0.4671476167170516,
        "abs_return_acf_20": 0.29583062592461923,
        "quantile_01": -0.07827382434020372,
        "quantile_99": 0.06551898218394284,
        "hill_tail_index": 2.6906400534203763
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021874194476262716,
        "excess_kurtosis": 11.554333178808525,
        "return_acf_1": -0.1566400266617541,
        "abs_return_acf_1": 0.4682100716219004,
        "abs_return_acf_5": 0.47820730716801985,
        "abs_return_acf_20": 0.3570957020052176,
        "quantile_01": -0.07316719004542876,
        "quantile_99": 0.06650194205045788,
        "hill_tail_index": 3.541278331994591
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018980807231397074,
        "excess_kurtosis": 7.829012589411489,
        "return_acf_1": -0.11496970545804786,
        "abs_return_acf_1": 0.4349196940979473,
        "abs_return_acf_5": 0.38411590141746343,
        "abs_return_acf_20": 0.24324322729022188,
        "quantile_01": -0.0623313592387735,
        "quantile_99": 0.051088854914019266,
        "hill_tail_index": 3.6585861863141163
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02114586836091309,
        "excess_kurtosis": 26.023522483286374,
        "return_acf_1": -0.08938634190894508,
        "abs_return_acf_1": 0.45273859913454445,
        "abs_return_acf_5": 0.4341670347425507,
        "abs_return_acf_20": 0.27387011478478746,
        "quantile_01": -0.07507301922235628,
        "quantile_99": 0.052860344753375546,
        "hill_tail_index": 1.8319876784825386
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
