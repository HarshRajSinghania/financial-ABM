# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27069
Run ID: `1b1cc2dd055848767de3cbbb03fc9b7df00ef716ce3e4e9af40204edb3b0298f`
Result fingerprint: `65e0b93e750807721d97f1bea7aa1eb55f71234c17530880a192ead646ad48ea`

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
    "equal_weight_sd": -0.5369642857142825,
    "equal_weight_raw": -8.054464285714237,
    "fixed_start_cap_weight_sd": -0.5425462495737509,
    "fixed_start_cap_weight_raw": -8.138193743606264,
    "end_cap_weight_sd": -0.5337366663465063,
    "end_cap_weight_raw": -8.006049995197593
  },
  "full_period_change": {
    "equal_weight_sd": -0.8927380952380904,
    "equal_weight_raw": -13.391071428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8604970238095192,
    "inflation_mean_sd": 0.6605724206349206
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4078945078856378,
    "equal_weight_raw": 6.1184176182845675,
    "fixed_start_cap_weight_sd": 0.3992319216206666,
    "fixed_start_cap_weight_raw": 5.9884788243100004,
    "end_cap_weight_sd": 0.404244150237181,
    "end_cap_weight_raw": 6.063662253557714
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5632142857142823,
      "change_raw": -8.448214285714235,
      "decay_adjusted_gain_sd": 0.38916666666666994
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5432142857142825,
      "change_raw": -8.148214285714237,
      "decay_adjusted_gain_sd": 0.3840928040632299
    },
    "small": {
      "count": 18,
      "change_sd": -0.5294642857142827,
      "change_raw": -7.941964285714241,
      "decay_adjusted_gain_sd": 0.4229166666666698
    },
    "large_minus_small_sd": -0.033749999999999614,
    "large_minus_small_raw": -0.5062499999999942
  },
  "inflation": {
    "initial_mean_sd": 0.2353333333333333,
    "final_mean_sd": 0.672,
    "mean_sd": 0.5033349986122676,
    "mean_absolute_raw_gap": 7.550024979184014,
    "final_absolute_raw_gap": 10.080000000000004,
    "mean_range_fraction": 0.07550024979184014
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.42,
    "initial_wealth_share": 0.1943648352859397,
    "final_wealth_share": 0.3769864797868127
  },
  "pricing_slope": {
    "mean": -0.0031630852667031183,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.09024264511634644,
    "real_improvement_cost": 0.07709576621434183,
    "washing_cost": 0.01314687890200463,
    "fine_transfer": 0.03259133805761158,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12283398317395802,
    "resource_cost_fraction_initial_cap": 0.003008088170544881,
    "private_net_outflow_fraction_initial_cap": 0.0040944661057986005,
    "fine_transfer_fraction_initial_cap": 0.0010863779352537192,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0013949948735341863,
    "unapplied_final_day_resource_cost": 0.00558150003607633
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 135.5992526680999,
    "beneficial_raw_gain_per_resource_cost": 2033.9887900214985,
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
    "fixed_exposure": 15.000000000000002,
    "accrued_cost": 3.0694987931219986,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.0933083169315215,
    "accrued_cost_fraction_initial_cap": 0.10231662643739994,
    "mean_contract_rate": 0.04246695255230453,
    "maximum_ledger_error": 8.216219588366713e-20
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
    "price_cap_hits": 6,
    "maximum_relative_cash_error": 2.5365448403948603e-15,
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
      "minimum": -0.16576560071230678,
      "maximum": -0.016632826285265346,
      "mean": -0.0840378539087522,
      "median": -0.09104372969059724,
      "quantile_05": -0.12976915605989936,
      "quantile_95": -0.0292256796785012
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
      "minimum": 0.3487771368852953,
      "maximum": 0.7885235017728561,
      "mean": 0.5955970994929404,
      "median": 0.6239048113259507,
      "quantile_05": 0.3967956621457478,
      "quantile_95": 0.7494622847029796
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
        "daily_volatility": 0.017836364569380116,
        "excess_kurtosis": 11.19483562865001,
        "return_acf_1": -0.04518378636198756,
        "abs_return_acf_1": 0.33646880517935984,
        "abs_return_acf_5": 0.3438134374141788,
        "abs_return_acf_20": 0.23014456960363275,
        "quantile_01": -0.05231711944482908,
        "quantile_99": 0.05009224608398393,
        "hill_tail_index": 2.81973633215115
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019901279804326467,
        "excess_kurtosis": 8.65295940500418,
        "return_acf_1": -0.1306373066447068,
        "abs_return_acf_1": 0.38087538529989484,
        "abs_return_acf_5": 0.32569002293890903,
        "abs_return_acf_20": 0.37032046693468046,
        "quantile_01": -0.06322782601647069,
        "quantile_99": 0.062472860134032124,
        "hill_tail_index": 3.020326533247822
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017800834383717844,
        "excess_kurtosis": 9.483400328650939,
        "return_acf_1": -0.1178062599427933,
        "abs_return_acf_1": 0.2967940361468354,
        "abs_return_acf_5": 0.19963919087989648,
        "abs_return_acf_20": 0.18813985669371208,
        "quantile_01": -0.05526226277336084,
        "quantile_99": 0.03881007104417557,
        "hill_tail_index": 2.2177705581955496
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016398987484014423,
        "excess_kurtosis": 7.252435211419572,
        "return_acf_1": -0.09616586911953451,
        "abs_return_acf_1": 0.2690342632786351,
        "abs_return_acf_5": 0.20477841069711916,
        "abs_return_acf_20": 0.2401959223175688,
        "quantile_01": -0.046497217780161894,
        "quantile_99": 0.040576846010609714,
        "hill_tail_index": 3.201976009151944
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018621463936360532,
        "excess_kurtosis": 10.418048352168784,
        "return_acf_1": -0.0664220457418666,
        "abs_return_acf_1": 0.34639466868894575,
        "abs_return_acf_5": 0.3418252590905095,
        "abs_return_acf_20": 0.22930597088236604,
        "quantile_01": -0.057280393066503614,
        "quantile_99": 0.05481608242690545,
        "hill_tail_index": 3.0454501698677214
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016874191871604573,
        "excess_kurtosis": 6.759779836984947,
        "return_acf_1": -0.16576560071230678,
        "abs_return_acf_1": 0.3778764480450956,
        "abs_return_acf_5": 0.30436656864972683,
        "abs_return_acf_20": 0.2516181707503524,
        "quantile_01": -0.056491852799752565,
        "quantile_99": 0.04581708826428407,
        "hill_tail_index": 2.70490486339961
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018572975634097204,
        "excess_kurtosis": 5.077034317807085,
        "return_acf_1": -0.0522130473755189,
        "abs_return_acf_1": 0.35849330797891854,
        "abs_return_acf_5": 0.2920550590232305,
        "abs_return_acf_20": 0.2054704047936162,
        "quantile_01": -0.054629294884179655,
        "quantile_99": 0.05510860109478652,
        "hill_tail_index": 4.088603645909913
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01743520588042983,
        "excess_kurtosis": 4.574182650224017,
        "return_acf_1": -0.11370886521849823,
        "abs_return_acf_1": 0.27605699549986507,
        "abs_return_acf_5": 0.2911667350143008,
        "abs_return_acf_20": 0.22460070125741557,
        "quantile_01": -0.0556969453043945,
        "quantile_99": 0.049280634021146276,
        "hill_tail_index": 3.508271133000461
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018830584216124567,
        "excess_kurtosis": 13.527285987784687,
        "return_acf_1": -0.093346308471108,
        "abs_return_acf_1": 0.43989280506616757,
        "abs_return_acf_5": 0.45672216001547317,
        "abs_return_acf_20": 0.3047231129395748,
        "quantile_01": -0.06258829039419081,
        "quantile_99": 0.04666761427690265,
        "hill_tail_index": 2.1124875400012666
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018481151480602715,
        "excess_kurtosis": 11.386553493745993,
        "return_acf_1": -0.06527525488930383,
        "abs_return_acf_1": 0.413613489048272,
        "abs_return_acf_5": 0.3764465261910531,
        "abs_return_acf_20": 0.3083139703421181,
        "quantile_01": -0.07261622909329875,
        "quantile_99": 0.04376525068373461,
        "hill_tail_index": 1.787733566982004
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019235395145033512,
        "excess_kurtosis": 15.463506901305756,
        "return_acf_1": -0.08994417274560741,
        "abs_return_acf_1": 0.41729952818735044,
        "abs_return_acf_5": 0.3619190308569078,
        "abs_return_acf_20": 0.2894399388138598,
        "quantile_01": -0.057845700260628685,
        "quantile_99": 0.04076001205048743,
        "hill_tail_index": 1.7804298837623735
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017789288914471083,
        "excess_kurtosis": 5.360673568552944,
        "return_acf_1": -0.09593306200800826,
        "abs_return_acf_1": 0.2178603435256842,
        "abs_return_acf_5": 0.17075629146758317,
        "abs_return_acf_20": 0.17995212402380145,
        "quantile_01": -0.05666527658030272,
        "quantile_99": 0.044891736947790924,
        "hill_tail_index": 2.9388883048688546
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017865371337470782,
        "excess_kurtosis": 10.124886936980268,
        "return_acf_1": -0.09214328663558705,
        "abs_return_acf_1": 0.3311075009235906,
        "abs_return_acf_5": 0.3021583646867227,
        "abs_return_acf_20": 0.35198752884931617,
        "quantile_01": -0.05507453979482729,
        "quantile_99": 0.04399389070321779,
        "hill_tail_index": 2.5541371477143486
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017566705790921785,
        "excess_kurtosis": 11.234661735893363,
        "return_acf_1": -0.10546537078373984,
        "abs_return_acf_1": 0.21670130383888614,
        "abs_return_acf_5": 0.23927392917574816,
        "abs_return_acf_20": 0.21638664329866825,
        "quantile_01": -0.048194916916972204,
        "quantile_99": 0.04505510021708834,
        "hill_tail_index": 2.3021902837730175
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0207300924971355,
        "excess_kurtosis": 22.695098521296345,
        "return_acf_1": -0.050466752138666214,
        "abs_return_acf_1": 0.3876118480816957,
        "abs_return_acf_5": 0.3299341832942814,
        "abs_return_acf_20": 0.3269343329197793,
        "quantile_01": -0.07088380382438202,
        "quantile_99": 0.050051773096628074,
        "hill_tail_index": 1.7230938577312398
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018015319255135574,
        "excess_kurtosis": 6.712221683984911,
        "return_acf_1": -0.10392487956381309,
        "abs_return_acf_1": 0.325238740742913,
        "abs_return_acf_5": 0.27554707374017207,
        "abs_return_acf_20": 0.30848268912686716,
        "quantile_01": -0.061504334436976074,
        "quantile_99": 0.042931556377094796,
        "hill_tail_index": 2.6221071857765708
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01550846000744988,
        "excess_kurtosis": 6.462092283574213,
        "return_acf_1": -0.062009385266331596,
        "abs_return_acf_1": 0.17247644074318835,
        "abs_return_acf_5": 0.114434872263271,
        "abs_return_acf_20": 0.12316639399609848,
        "quantile_01": -0.041389539729915895,
        "quantile_99": 0.03387794293406212,
        "hill_tail_index": 2.8078483683488344
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017413503947259767,
        "excess_kurtosis": 5.8148142080192855,
        "return_acf_1": -0.10408309478073967,
        "abs_return_acf_1": 0.22634798340088627,
        "abs_return_acf_5": 0.2259133984961883,
        "abs_return_acf_20": 0.31298948022994805,
        "quantile_01": -0.043310900246411994,
        "quantile_99": 0.04805142076371446,
        "hill_tail_index": 3.1964445610737955
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018293331033486054,
        "excess_kurtosis": 12.729757273161391,
        "return_acf_1": -0.08367318734448242,
        "abs_return_acf_1": 0.2520308440518932,
        "abs_return_acf_5": 0.23505996621421796,
        "abs_return_acf_20": 0.23834101528025023,
        "quantile_01": -0.05519650009693842,
        "quantile_99": 0.045162056225322315,
        "hill_tail_index": 2.52554669469032
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017613389249478757,
        "excess_kurtosis": 9.475189804566867,
        "return_acf_1": -0.049864194839463624,
        "abs_return_acf_1": 0.31000522042221984,
        "abs_return_acf_5": 0.3046283950895307,
        "abs_return_acf_20": 0.2272991870246238,
        "quantile_01": -0.04907386163293231,
        "quantile_99": 0.039317148210891814,
        "hill_tail_index": 2.2401670963918145
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016968916134056725,
        "excess_kurtosis": 10.141887482049967,
        "return_acf_1": -0.12028369587925146,
        "abs_return_acf_1": 0.25615385667666485,
        "abs_return_acf_5": 0.26765112601458874,
        "abs_return_acf_20": 0.2263590444142018,
        "quantile_01": -0.04364449523979894,
        "quantile_99": 0.03896898084811632,
        "hill_tail_index": 2.398534055783606
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017288470999529622,
        "excess_kurtosis": 11.667228800682057,
        "return_acf_1": -0.024430871126822292,
        "abs_return_acf_1": 0.18553160505986768,
        "abs_return_acf_5": 0.1763045880921515,
        "abs_return_acf_20": 0.1747062097370001,
        "quantile_01": -0.05295501386871595,
        "quantile_99": 0.03988679397742695,
        "hill_tail_index": 2.3892519613584473
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01959784646297347,
        "excess_kurtosis": 12.027631214019387,
        "return_acf_1": -0.0868556880849663,
        "abs_return_acf_1": 0.3451138991227002,
        "abs_return_acf_5": 0.37504193302731387,
        "abs_return_acf_20": 0.2859689443390018,
        "quantile_01": -0.061914295126923494,
        "quantile_99": 0.04639906699001678,
        "hill_tail_index": 2.4227640302761158
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01859142941746034,
        "excess_kurtosis": 12.298273248535157,
        "return_acf_1": -0.04240474416974255,
        "abs_return_acf_1": 0.29261542167690485,
        "abs_return_acf_5": 0.3005498868280258,
        "abs_return_acf_20": 0.2494334922839185,
        "quantile_01": -0.06986366522956244,
        "quantile_99": 0.04238956900968311,
        "hill_tail_index": 2.0203460590032685
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01650274969579592,
        "excess_kurtosis": 3.8397935852216625,
        "return_acf_1": -0.09739421977591904,
        "abs_return_acf_1": 0.20156873281227858,
        "abs_return_acf_5": 0.19145989956881615,
        "abs_return_acf_20": 0.20302199901063514,
        "quantile_01": -0.039220287937418434,
        "quantile_99": 0.046356474415700816,
        "hill_tail_index": 3.2230144682025865
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01952185833872803,
        "excess_kurtosis": 15.587530408855201,
        "return_acf_1": -0.03508600124166424,
        "abs_return_acf_1": 0.3312934738175923,
        "abs_return_acf_5": 0.30181050811785554,
        "abs_return_acf_20": 0.25445986025891504,
        "quantile_01": -0.05113674220858425,
        "quantile_99": 0.04659706068919913,
        "hill_tail_index": 2.1077906739749093
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01995841443037458,
        "excess_kurtosis": 10.413487347800913,
        "return_acf_1": -0.09844279464560446,
        "abs_return_acf_1": 0.29146456442782126,
        "abs_return_acf_5": 0.27675172113468927,
        "abs_return_acf_20": 0.2749036390089171,
        "quantile_01": -0.06070302109998727,
        "quantile_99": 0.059392685569642,
        "hill_tail_index": 2.789569574988037
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01843529970412593,
        "excess_kurtosis": 9.08560951114905,
        "return_acf_1": -0.08686496234635296,
        "abs_return_acf_1": 0.27671781399338957,
        "abs_return_acf_5": 0.2272148392336932,
        "abs_return_acf_20": 0.1611818051905441,
        "quantile_01": -0.0534412026253888,
        "quantile_99": 0.04762081909424259,
        "hill_tail_index": 3.051444124338883
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016666187760706025,
        "excess_kurtosis": 5.980261030450064,
        "return_acf_1": -0.016632826285265346,
        "abs_return_acf_1": 0.21541432835957708,
        "abs_return_acf_5": 0.1455370510716752,
        "abs_return_acf_20": 0.17844861281735838,
        "quantile_01": -0.04842634678666733,
        "quantile_99": 0.04289825399520117,
        "hill_tail_index": 3.175682174353282
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018302355025542755,
        "excess_kurtosis": 11.424816716819718,
        "return_acf_1": -0.1287080831229125,
        "abs_return_acf_1": 0.34992940723743515,
        "abs_return_acf_5": 0.3315647809149193,
        "abs_return_acf_20": 0.31505846546115107,
        "quantile_01": -0.06551137857837823,
        "quantile_99": 0.03966445690178168,
        "hill_tail_index": 1.970436188301038
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
