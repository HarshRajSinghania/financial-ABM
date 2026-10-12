# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27089
Run ID: `a42aed010cb18eec90158c5a6b79b97b36c91862bb0fe7ff0f4065e305e404a3`
Result fingerprint: `6eb6e7dbea66907ae8f5afb46ee6e6a0d6a6fbef79836efeb318ae1200763853`

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
    "equal_weight_sd": -0.5537198147174283,
    "equal_weight_raw": -8.305797220761423,
    "fixed_start_cap_weight_sd": -0.4608518329057169,
    "fixed_start_cap_weight_raw": -6.912777493585752,
    "end_cap_weight_sd": -0.48512198590948924,
    "end_cap_weight_raw": -7.276829788642338
  },
  "full_period_change": {
    "equal_weight_sd": -0.895160290907903,
    "equal_weight_raw": -13.427404363618544
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8493490979121864,
    "inflation_mean_sd": 0.5335277777777778
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.387586127090481,
    "equal_weight_raw": 5.813791906357214,
    "fixed_start_cap_weight_sd": 0.4485149066579152,
    "fixed_start_cap_weight_raw": 6.72772359986873,
    "end_cap_weight_sd": 0.4321245152733303,
    "end_cap_weight_raw": 6.481867729099953
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.31660290907907296,
      "change_raw": -4.749043636186094,
      "decay_adjusted_gain_sd": 0.5324603174603197
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5323809523809493,
      "change_raw": -7.98571428571424,
      "decay_adjusted_gain_sd": 0.4200000000000031
    },
    "small": {
      "count": 18,
      "change_sd": -0.6039087301587269,
      "change_raw": -9.058630952380904,
      "decay_adjusted_gain_sd": 0.34723349224074673
    },
    "large_minus_small_sd": 0.28730582107965397,
    "large_minus_small_raw": 4.3095873161948095
  },
  "inflation": {
    "initial_mean_sd": 0.3070833333333333,
    "final_mean_sd": 0.5559166666666666,
    "mean_sd": 0.43257223147377194,
    "mean_absolute_raw_gap": 6.488583472106578,
    "final_absolute_raw_gap": 8.338750000000001,
    "mean_range_fraction": 0.06488583472106578
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.4533333333333333,
    "initial_wealth_share": 0.2588696330565813,
    "final_wealth_share": 0.5546813618742134
  },
  "pricing_slope": {
    "mean": -0.0017407617283609783,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.1867625878289713,
    "real_improvement_cost": 0.14636169908543012,
    "washing_cost": 0.04040088874354116,
    "fine_transfer": 0.03363619764016061,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.22039878546913189,
    "resource_cost_fraction_initial_cap": 0.006225419594299043,
    "private_net_outflow_fraction_initial_cap": 0.0073466261823043975,
    "fine_transfer_fraction_initial_cap": 0.0011212065880053539,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0002806223764055131,
    "unapplied_final_day_resource_cost": 0.01279780175585137
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 62.258635136082205,
    "beneficial_raw_gain_per_resource_cost": 933.8795270412331,
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
    "accrued_cost": 2.7025546676123473,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.2736358085781293,
    "accrued_cost_fraction_initial_cap": 0.09008515558707826,
    "mean_contract_rate": 0.038102523507573566,
    "maximum_ledger_error": 9.486769009248164e-20
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
    "maximum_relative_cash_error": 1.4191342547503013e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.25417652497464444,
      "maximum": -0.05667425513099459,
      "mean": -0.1484263298695243,
      "median": -0.14687797204167966,
      "quantile_05": -0.21000979647167972,
      "quantile_95": -0.06591365231241399
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
      "minimum": 0.2743315350338632,
      "maximum": 0.7400594630196657,
      "mean": 0.5150413606068317,
      "median": 0.494285648147031,
      "quantile_05": 0.3346559067739424,
      "quantile_95": 0.7014084240349557
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
        "daily_volatility": 0.016220284651171486,
        "excess_kurtosis": 4.799723674241148,
        "return_acf_1": -0.11968303217750319,
        "abs_return_acf_1": 0.3182342666525913,
        "abs_return_acf_5": 0.24804330634131097,
        "abs_return_acf_20": 0.2864580141926828,
        "quantile_01": -0.0506002603462399,
        "quantile_99": 0.040950260970335835,
        "hill_tail_index": 2.9573277243291343
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016338516238333795,
        "excess_kurtosis": 7.653192573704844,
        "return_acf_1": -0.1850228705666373,
        "abs_return_acf_1": 0.34976576975519,
        "abs_return_acf_5": 0.30595965056884755,
        "abs_return_acf_20": 0.2936100311257028,
        "quantile_01": -0.05425934878747512,
        "quantile_99": 0.037190371377546175,
        "hill_tail_index": 2.263378187059953
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017425448433131676,
        "excess_kurtosis": 9.870774896518723,
        "return_acf_1": -0.12065669417331283,
        "abs_return_acf_1": 0.41360624286328257,
        "abs_return_acf_5": 0.3567502516795156,
        "abs_return_acf_20": 0.3472272048447049,
        "quantile_01": -0.05441346737100838,
        "quantile_99": 0.039642326113725264,
        "hill_tail_index": 1.9727252619466036
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01705678518650849,
        "excess_kurtosis": 8.506665267668232,
        "return_acf_1": -0.2149856007627718,
        "abs_return_acf_1": 0.4111053685540035,
        "abs_return_acf_5": 0.34532225336176114,
        "abs_return_acf_20": 0.21193210869015067,
        "quantile_01": -0.046171907006243185,
        "quantile_99": 0.04850511287085873,
        "hill_tail_index": 2.8658254530988416
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01655684730374263,
        "excess_kurtosis": 7.131926902776936,
        "return_acf_1": -0.06445597428955491,
        "abs_return_acf_1": 0.24333328618755753,
        "abs_return_acf_5": 0.29146093573048104,
        "abs_return_acf_20": 0.22849210518041183,
        "quantile_01": -0.05395362739499719,
        "quantile_99": 0.048562802753447626,
        "hill_tail_index": 4.2345257115674295
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015678881529902877,
        "excess_kurtosis": 2.9062279417189396,
        "return_acf_1": -0.18705735313407695,
        "abs_return_acf_1": 0.25306466654792853,
        "abs_return_acf_5": 0.21627820664120234,
        "abs_return_acf_20": 0.132881193760332,
        "quantile_01": -0.03969773750248167,
        "quantile_99": 0.04257779625238465,
        "hill_tail_index": 3.731883496468947
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.015423381488918846,
        "excess_kurtosis": 2.991066797751066,
        "return_acf_1": -0.14136809241177117,
        "abs_return_acf_1": 0.20088030397000078,
        "abs_return_acf_5": 0.15550852556838454,
        "abs_return_acf_20": 0.1920725801899426,
        "quantile_01": -0.04344418329427189,
        "quantile_99": 0.03830269409350002,
        "hill_tail_index": 3.516879440736742
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015400774113071261,
        "excess_kurtosis": 2.5196867718649703,
        "return_acf_1": -0.1160306362514602,
        "abs_return_acf_1": 0.2705109769282609,
        "abs_return_acf_5": 0.30088008225117696,
        "abs_return_acf_20": 0.27037134216668796,
        "quantile_01": -0.03821942278243832,
        "quantile_99": 0.04473073346017426,
        "hill_tail_index": 3.4793020083357713
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01508274739403863,
        "excess_kurtosis": 3.3469934354544284,
        "return_acf_1": -0.12087088169572914,
        "abs_return_acf_1": 0.23009621665108818,
        "abs_return_acf_5": 0.23400218051979943,
        "abs_return_acf_20": 0.2345669541424019,
        "quantile_01": -0.05007569709882083,
        "quantile_99": 0.03605030590962169,
        "hill_tail_index": 3.286836739573016
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016424981660611633,
        "excess_kurtosis": 7.071716474993092,
        "return_acf_1": -0.11961811929418868,
        "abs_return_acf_1": 0.27544360367943954,
        "abs_return_acf_5": 0.2753629558572398,
        "abs_return_acf_20": 0.3393469603884702,
        "quantile_01": -0.06345639805616565,
        "quantile_99": 0.04048414914906656,
        "hill_tail_index": 2.2826598121589035
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01568797702347583,
        "excess_kurtosis": 7.7254188720713035,
        "return_acf_1": -0.05667425513099459,
        "abs_return_acf_1": 0.30941343509359265,
        "abs_return_acf_5": 0.25159065987360557,
        "abs_return_acf_20": 0.269453625416361,
        "quantile_01": -0.046787040295177613,
        "quantile_99": 0.041420648244835406,
        "hill_tail_index": 2.6468251882931155
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015462767997971305,
        "excess_kurtosis": 4.400640746291862,
        "return_acf_1": -0.20290263627663543,
        "abs_return_acf_1": 0.20957838945260393,
        "abs_return_acf_5": 0.15009829729513466,
        "abs_return_acf_20": 0.20001655774640298,
        "quantile_01": -0.04616031713629819,
        "quantile_99": 0.03556678544493802,
        "hill_tail_index": 2.9518712770442512
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.014921129864633842,
        "excess_kurtosis": 2.9146809066144517,
        "return_acf_1": -0.17883184361157972,
        "abs_return_acf_1": 0.2263459236209834,
        "abs_return_acf_5": 0.1967671436781322,
        "abs_return_acf_20": 0.19343400954694628,
        "quantile_01": -0.041950062273524914,
        "quantile_99": 0.03758906675580932,
        "hill_tail_index": 3.3007064154769314
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.015693496662912323,
        "excess_kurtosis": 5.64452752773051,
        "return_acf_1": -0.1965645966474257,
        "abs_return_acf_1": 0.2677921634902317,
        "abs_return_acf_5": 0.26770515655540844,
        "abs_return_acf_20": 0.2800785519177566,
        "quantile_01": -0.045063496517861644,
        "quantile_99": 0.038590125557611,
        "hill_tail_index": 3.1292944589974425
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017139803161132075,
        "excess_kurtosis": 15.054703284610937,
        "return_acf_1": -0.16222570748041773,
        "abs_return_acf_1": 0.4037816859707222,
        "abs_return_acf_5": 0.33057840577275605,
        "abs_return_acf_20": 0.27813707745037913,
        "quantile_01": -0.047621673262334414,
        "quantile_99": 0.04097011627837943,
        "hill_tail_index": 2.122668076551301
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018507879849985524,
        "excess_kurtosis": 25.420854430053073,
        "return_acf_1": -0.25417652497464444,
        "abs_return_acf_1": 0.4639988332412525,
        "abs_return_acf_5": 0.3505309540073345,
        "abs_return_acf_20": 0.2618681140262057,
        "quantile_01": -0.058336377882281625,
        "quantile_99": 0.04513945333372276,
        "hill_tail_index": 1.9275515296859895
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.015205771707265303,
        "excess_kurtosis": 1.1782749720779888,
        "return_acf_1": -0.17769463111433398,
        "abs_return_acf_1": 0.189554096809727,
        "abs_return_acf_5": 0.14579613712707504,
        "abs_return_acf_20": 0.16549455743350444,
        "quantile_01": -0.04126108809972496,
        "quantile_99": 0.04032080665588473,
        "hill_tail_index": 5.709469463092982
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016323281982125105,
        "excess_kurtosis": 12.428782703557635,
        "return_acf_1": -0.10283671699003197,
        "abs_return_acf_1": 0.2645873168729968,
        "abs_return_acf_5": 0.3404851537533433,
        "abs_return_acf_20": 0.228193292008081,
        "quantile_01": -0.04435763806782167,
        "quantile_99": 0.03839541999565356,
        "hill_tail_index": 2.40477149768034
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017002196811069854,
        "excess_kurtosis": 8.643266657566418,
        "return_acf_1": -0.1342134066771369,
        "abs_return_acf_1": 0.24300297064762355,
        "abs_return_acf_5": 0.25045264979217646,
        "abs_return_acf_20": 0.27804768826214327,
        "quantile_01": -0.05967339259958683,
        "quantile_99": 0.03862538466472683,
        "hill_tail_index": 2.961552685285092
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016589522786011668,
        "excess_kurtosis": 6.856943816184527,
        "return_acf_1": -0.13853013627680033,
        "abs_return_acf_1": 0.34404115165939403,
        "abs_return_acf_5": 0.3305381162106326,
        "abs_return_acf_20": 0.32829278374479226,
        "quantile_01": -0.0538864564516845,
        "quantile_99": 0.04075088087287899,
        "hill_tail_index": 2.4160560286344306
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.015545692478751911,
        "excess_kurtosis": 3.1712971031380075,
        "return_acf_1": -0.15522692864380744,
        "abs_return_acf_1": 0.20315739772327074,
        "abs_return_acf_5": 0.25208168022978394,
        "abs_return_acf_20": 0.15483591367402164,
        "quantile_01": -0.038007783844846925,
        "quantile_99": 0.037112510929126936,
        "hill_tail_index": 3.417453988266987
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.015481803873710424,
        "excess_kurtosis": 2.9172579768688784,
        "return_acf_1": -0.0787575099746423,
        "abs_return_acf_1": 0.2631278677853234,
        "abs_return_acf_5": 0.18839222905050373,
        "abs_return_acf_20": 0.2146370448266994,
        "quantile_01": -0.0439101016817636,
        "quantile_99": 0.04156439160151749,
        "hill_tail_index": 4.192310230160331
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.015835178030717767,
        "excess_kurtosis": 4.195434104979062,
        "return_acf_1": -0.13490699444619303,
        "abs_return_acf_1": 0.16150672000055355,
        "abs_return_acf_5": 0.20023784309817722,
        "abs_return_acf_20": 0.17083052333895435,
        "quantile_01": -0.049396091853274156,
        "quantile_99": 0.04006012351573503,
        "hill_tail_index": 3.5183002694569128
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01674483134229822,
        "excess_kurtosis": 2.387873334808197,
        "return_acf_1": -0.18738584457136395,
        "abs_return_acf_1": 0.21189711082326898,
        "abs_return_acf_5": 0.18265958611255867,
        "abs_return_acf_20": 0.19969280346093105,
        "quantile_01": -0.04782906513214225,
        "quantile_99": 0.043662826149343734,
        "hill_tail_index": 4.6749015480054785
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01677447305248638,
        "excess_kurtosis": 8.172228996506595,
        "return_acf_1": -0.15238785167158814,
        "abs_return_acf_1": 0.396167650666239,
        "abs_return_acf_5": 0.3060768467737954,
        "abs_return_acf_20": 0.38058615034213844,
        "quantile_01": -0.049696057353962236,
        "quantile_99": 0.045561488116802266,
        "hill_tail_index": 2.568906883642686
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01587101944721302,
        "excess_kurtosis": 2.7514171358590787,
        "return_acf_1": -0.1705176729548284,
        "abs_return_acf_1": 0.23323350829234257,
        "abs_return_acf_5": 0.24939902319007196,
        "abs_return_acf_20": 0.20594682625874353,
        "quantile_01": -0.044684608683669844,
        "quantile_99": 0.046042349260066645,
        "hill_tail_index": 3.8736553325866168
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01514950716078118,
        "excess_kurtosis": 4.280900281703424,
        "return_acf_1": -0.06769525878479728,
        "abs_return_acf_1": 0.28407164742254387,
        "abs_return_acf_5": 0.22519409252459097,
        "abs_return_acf_20": 0.27553604439765744,
        "quantile_01": -0.047767700261951714,
        "quantile_99": 0.03784104038805638,
        "hill_tail_index": 2.8287352547329605
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02021807996207822,
        "excess_kurtosis": 10.853491098282978,
        "return_acf_1": -0.19095529949990347,
        "abs_return_acf_1": 0.4248828839067545,
        "abs_return_acf_5": 0.39642196766459725,
        "abs_return_acf_20": 0.2843156164484889,
        "quantile_01": -0.06190716589153682,
        "quantile_99": 0.06549880641037131,
        "hill_tail_index": 2.936437649840514
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01771967868956834,
        "excess_kurtosis": 5.286988967326911,
        "return_acf_1": -0.20392825789367833,
        "abs_return_acf_1": 0.4243975489417138,
        "abs_return_acf_5": 0.36388417780803106,
        "abs_return_acf_20": 0.2985726402730116,
        "quantile_01": -0.05287323829434837,
        "quantile_99": 0.056955787598476575,
        "hill_tail_index": 3.717114364624509
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.015083084462623849,
        "excess_kurtosis": 7.082208950963523,
        "return_acf_1": -0.11662856770792,
        "abs_return_acf_1": 0.23818331533144088,
        "abs_return_acf_5": 0.25090515369736976,
        "abs_return_acf_20": 0.2568165526448872,
        "quantile_01": -0.03615220479540826,
        "quantile_99": 0.038624357090566615,
        "hill_tail_index": 3.1407676792949197
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
