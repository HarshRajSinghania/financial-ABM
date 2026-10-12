# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720201
Run ID: `ed2351d1c614a3e78bda87099d52288ab1d38e348d0340d5f9789cdc92368afe`
Result fingerprint: `41eab9e7cb14098e4e13365c2a26771f31026906e5a61844e33f8d90817de541`

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
    "equal_weight_sd": -0.39646428571428255,
    "equal_weight_raw": -5.946964285714239,
    "fixed_start_cap_weight_sd": -0.4079709278376381,
    "fixed_start_cap_weight_raw": -6.119563917564573,
    "end_cap_weight_sd": -0.43433450075610147,
    "end_cap_weight_raw": -6.51501751134152
  },
  "full_period_change": {
    "equal_weight_sd": -0.857571428571424,
    "equal_weight_raw": -12.86357142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8428115079365036,
    "inflation_mean_sd": 0.4987953042328042
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5425642586239103,
    "equal_weight_raw": 8.138463879358655,
    "fixed_start_cap_weight_sd": 0.5213820330059177,
    "fixed_start_cap_weight_raw": 7.820730495088766,
    "end_cap_weight_sd": 0.49516127701379664,
    "end_cap_weight_raw": 7.427419155206949
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5682142857142825,
      "change_raw": -8.523214285714237,
      "decay_adjusted_gain_sd": 0.3841666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.2851587301587271,
      "change_raw": -4.2773809523809065,
      "decay_adjusted_gain_sd": 0.6353870307441787
    },
    "small": {
      "count": 18,
      "change_sd": -0.4234920634920603,
      "change_raw": -6.352380952380905,
      "decay_adjusted_gain_sd": 0.5225524712233163
    },
    "large_minus_small_sd": -0.14472222222222214,
    "large_minus_small_raw": -2.170833333333332
  },
  "inflation": {
    "initial_mean_sd": 0.08291666666666668,
    "final_mean_sd": 0.5348333333333334,
    "mean_sd": 0.32046336386344715,
    "mean_absolute_raw_gap": 4.806950457951707,
    "final_absolute_raw_gap": 8.022499999999999,
    "mean_range_fraction": 0.04806950457951707
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.349767332479821,
    "final_wealth_share": 0.37739789867940127
  },
  "pricing_slope": {
    "mean": -0.0010046973368761506,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.09111577344041255,
    "real_improvement_cost": 0.08237897187167709,
    "washing_cost": 0.008736801568735457,
    "fine_transfer": 0.01853606796895159,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10965184140936414,
    "resource_cost_fraction_initial_cap": 0.0030371924480137513,
    "private_net_outflow_fraction_initial_cap": 0.0036550613803121375,
    "fine_transfer_fraction_initial_cap": 0.0006178689322983862,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 8.349591373717406e-05,
    "unapplied_final_day_resource_cost": 0.0004404468687404398
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 178.64006575504752,
    "beneficial_raw_gain_per_resource_cost": 2679.6009863257127,
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
    "accrued_cost": 3.071219844956876,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.09502936876639918,
    "accrued_cost_fraction_initial_cap": 0.10237399483189585,
    "mean_contract_rate": 0.04189354507187698,
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
    "maximum_relative_cash_error": 2.6716449166845313e-15,
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
      "minimum": -0.2762104364439775,
      "maximum": -0.08184635422075223,
      "mean": -0.18647189770009787,
      "median": -0.19762232556971504,
      "quantile_05": -0.24221846103547937,
      "quantile_95": -0.09954747296318678
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
      "minimum": 0.380814561052403,
      "maximum": 0.8334568005936516,
      "mean": 0.6487788226930775,
      "median": 0.6522727081374503,
      "quantile_05": 0.46596700761701365,
      "quantile_95": 0.79111301255161
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
        "daily_volatility": 0.022034745128049867,
        "excess_kurtosis": 7.004384161973839,
        "return_acf_1": -0.1426602557148368,
        "abs_return_acf_1": 0.43476653524886955,
        "abs_return_acf_5": 0.4424590821282313,
        "abs_return_acf_20": 0.3560884412257989,
        "quantile_01": -0.07930149488681736,
        "quantile_99": 0.06970155073431183,
        "hill_tail_index": 4.033815802185114
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02269392358142576,
        "excess_kurtosis": 10.66754888240036,
        "return_acf_1": -0.19738534234810023,
        "abs_return_acf_1": 0.4173106267273056,
        "abs_return_acf_5": 0.44992978030085157,
        "abs_return_acf_20": 0.31021140286132504,
        "quantile_01": -0.08153344488747355,
        "quantile_99": 0.06015128776071615,
        "hill_tail_index": 2.6031024040828123
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021498804880657897,
        "excess_kurtosis": 12.462609334475138,
        "return_acf_1": -0.23415186841565624,
        "abs_return_acf_1": 0.4531309283191837,
        "abs_return_acf_5": 0.4295447482578626,
        "abs_return_acf_20": 0.2995509850757366,
        "quantile_01": -0.06721897509699434,
        "quantile_99": 0.06322690698073527,
        "hill_tail_index": 2.5794122328328513
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02263985908567303,
        "excess_kurtosis": 11.692620368463944,
        "return_acf_1": -0.24433909949079902,
        "abs_return_acf_1": 0.41893452224831756,
        "abs_return_acf_5": 0.43233012391518305,
        "abs_return_acf_20": 0.32257862060495124,
        "quantile_01": -0.07927524659957451,
        "quantile_99": 0.07282434018550156,
        "hill_tail_index": 3.212745379669803
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02448466105230672,
        "excess_kurtosis": 12.19749078861741,
        "return_acf_1": -0.19878409014147014,
        "abs_return_acf_1": 0.41403996430779566,
        "abs_return_acf_5": 0.43194127021002116,
        "abs_return_acf_20": 0.3932878716952535,
        "quantile_01": -0.08934701452213537,
        "quantile_99": 0.07567666339863174,
        "hill_tail_index": 3.0650031581571153
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021952703682052155,
        "excess_kurtosis": 11.716093969991046,
        "return_acf_1": -0.19785930879132982,
        "abs_return_acf_1": 0.3925401602946636,
        "abs_return_acf_5": 0.47428740179523327,
        "abs_return_acf_20": 0.30562683250981065,
        "quantile_01": -0.07124710949692276,
        "quantile_99": 0.07037555971523443,
        "hill_tail_index": 3.2024205515099253
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02275574604759207,
        "excess_kurtosis": 10.619831298118655,
        "return_acf_1": -0.1357854241020455,
        "abs_return_acf_1": 0.36673062995142125,
        "abs_return_acf_5": 0.4199325056985761,
        "abs_return_acf_20": 0.3150525442321641,
        "quantile_01": -0.07949733196054407,
        "quantile_99": 0.07307594433367233,
        "hill_tail_index": 3.2453168062653335
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.025643885274379736,
        "excess_kurtosis": 11.885130679517784,
        "return_acf_1": -0.19918689934566927,
        "abs_return_acf_1": 0.47417367862766724,
        "abs_return_acf_5": 0.4659358412510743,
        "abs_return_acf_20": 0.3770640621616136,
        "quantile_01": -0.09681679123934422,
        "quantile_99": 0.07926468789053344,
        "hill_tail_index": 2.9999435069913645
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021939545282775606,
        "excess_kurtosis": 9.765632642002766,
        "return_acf_1": -0.17510122122661056,
        "abs_return_acf_1": 0.39287325801158773,
        "abs_return_acf_5": 0.37103168179908874,
        "abs_return_acf_20": 0.3055390395069033,
        "quantile_01": -0.06688926255577686,
        "quantile_99": 0.05990902462953937,
        "hill_tail_index": 2.6898739305701147
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02257932995298655,
        "excess_kurtosis": 11.392235899699605,
        "return_acf_1": -0.1839956846057256,
        "abs_return_acf_1": 0.44874881631554714,
        "abs_return_acf_5": 0.43849298743060233,
        "abs_return_acf_20": 0.3664945965218274,
        "quantile_01": -0.08010207301865695,
        "quantile_99": 0.06935411309630211,
        "hill_tail_index": 3.539855259305149
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02392279411374074,
        "excess_kurtosis": 11.043317159958526,
        "return_acf_1": -0.19814203497825167,
        "abs_return_acf_1": 0.4641827797339852,
        "abs_return_acf_5": 0.5003968900088043,
        "abs_return_acf_20": 0.4047491456200523,
        "quantile_01": -0.081193726835073,
        "quantile_99": 0.07325813234790456,
        "hill_tail_index": 3.369764981290291
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.023476495527394097,
        "excess_kurtosis": 33.84695251899502,
        "return_acf_1": -0.08184635422075223,
        "abs_return_acf_1": 0.5657700720224296,
        "abs_return_acf_5": 0.5388043586980821,
        "abs_return_acf_20": 0.24750703507371535,
        "quantile_01": -0.07428792105262358,
        "quantile_99": 0.05954666449715795,
        "hill_tail_index": 1.8416771760563355
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022585201367877228,
        "excess_kurtosis": 9.397399679768869,
        "return_acf_1": -0.22066092349128869,
        "abs_return_acf_1": 0.464210835838704,
        "abs_return_acf_5": 0.4325536514857483,
        "abs_return_acf_20": 0.38347084989181585,
        "quantile_01": -0.0871545705028651,
        "quantile_99": 0.07503981535870714,
        "hill_tail_index": 3.8010046058921017
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023885832804478823,
        "excess_kurtosis": 22.97373752228424,
        "return_acf_1": -0.23962656959008866,
        "abs_return_acf_1": 0.4165951771031715,
        "abs_return_acf_5": 0.38067553889065303,
        "abs_return_acf_20": 0.2410612591356867,
        "quantile_01": -0.07357315311722733,
        "quantile_99": 0.07630871005188242,
        "hill_tail_index": 2.7061746414494823
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024476504487067036,
        "excess_kurtosis": 11.985722707365436,
        "return_acf_1": -0.1887531550575769,
        "abs_return_acf_1": 0.47631754726077313,
        "abs_return_acf_5": 0.46495201599058966,
        "abs_return_acf_20": 0.3980040339208433,
        "quantile_01": -0.09409049064226051,
        "quantile_99": 0.07065766287367137,
        "hill_tail_index": 3.11660955665467
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02216216276361888,
        "excess_kurtosis": 13.92381590686647,
        "return_acf_1": -0.16350515506694452,
        "abs_return_acf_1": 0.5104529182667521,
        "abs_return_acf_5": 0.40677715362894024,
        "abs_return_acf_20": 0.3020744297511082,
        "quantile_01": -0.07482054864499689,
        "quantile_99": 0.06673362966196343,
        "hill_tail_index": 3.0242574942604414
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023603586965587748,
        "excess_kurtosis": 9.376290410635532,
        "return_acf_1": -0.22236625785473485,
        "abs_return_acf_1": 0.4530799426406523,
        "abs_return_acf_5": 0.4568279754003099,
        "abs_return_acf_20": 0.3780738131106073,
        "quantile_01": -0.09193008376603663,
        "quantile_99": 0.07311755931314515,
        "hill_tail_index": 3.3043046550902293
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.023136551258656293,
        "excess_kurtosis": 10.2740722312179,
        "return_acf_1": -0.15601655257392888,
        "abs_return_acf_1": 0.4172481869646291,
        "abs_return_acf_5": 0.4247010412159024,
        "abs_return_acf_20": 0.3423439524932202,
        "quantile_01": -0.0836739373526524,
        "quantile_99": 0.06526267697425037,
        "hill_tail_index": 2.9343123456107016
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02220927328304445,
        "excess_kurtosis": 9.41378688324918,
        "return_acf_1": -0.1116833143021261,
        "abs_return_acf_1": 0.44392775476993257,
        "abs_return_acf_5": 0.477534454689661,
        "abs_return_acf_20": 0.34740762972296574,
        "quantile_01": -0.07965288505198453,
        "quantile_99": 0.07164797195895438,
        "hill_tail_index": 3.0143775604326075
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.023555696091469052,
        "excess_kurtosis": 14.00633973503325,
        "return_acf_1": -0.21875185684611267,
        "abs_return_acf_1": 0.4533698322032174,
        "abs_return_acf_5": 0.4608946276527179,
        "abs_return_acf_20": 0.2833524582095613,
        "quantile_01": -0.07926795379364089,
        "quantile_99": 0.06733559699922961,
        "hill_tail_index": 2.2657526596325748
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021606029004500198,
        "excess_kurtosis": 11.2988003002602,
        "return_acf_1": -0.19958956808513542,
        "abs_return_acf_1": 0.4397879491847562,
        "abs_return_acf_5": 0.36627062795086296,
        "abs_return_acf_20": 0.36117304063054817,
        "quantile_01": -0.07041731973536611,
        "quantile_99": 0.05978948311783193,
        "hill_tail_index": 2.6579841433705473
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024460909367287658,
        "excess_kurtosis": 10.865827259802858,
        "return_acf_1": -0.18148569254395938,
        "abs_return_acf_1": 0.4502064213260651,
        "abs_return_acf_5": 0.4297160178115275,
        "abs_return_acf_20": 0.3365238664631348,
        "quantile_01": -0.0945788197890947,
        "quantile_99": 0.0825030063374113,
        "hill_tail_index": 3.72010759214625
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024920360317495973,
        "excess_kurtosis": 15.520596608205686,
        "return_acf_1": -0.2762104364439775,
        "abs_return_acf_1": 0.5749938240460459,
        "abs_return_acf_5": 0.4830975381527072,
        "abs_return_acf_20": 0.3224872896050049,
        "quantile_01": -0.0872853454480032,
        "quantile_99": 0.07272452440509324,
        "hill_tail_index": 2.48003132627273
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02491677382662141,
        "excess_kurtosis": 7.5523564421944585,
        "return_acf_1": -0.1681012834655489,
        "abs_return_acf_1": 0.47401959516989267,
        "abs_return_acf_5": 0.47808265284761686,
        "abs_return_acf_20": 0.3823824781280338,
        "quantile_01": -0.09147286331884046,
        "quantile_99": 0.0815031199629834,
        "hill_tail_index": 4.3056216399740075
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.025692147061516128,
        "excess_kurtosis": 12.089896010627829,
        "return_acf_1": -0.2284557187514527,
        "abs_return_acf_1": 0.4548414085219487,
        "abs_return_acf_5": 0.4209553302115226,
        "abs_return_acf_20": 0.34179710023105914,
        "quantile_01": -0.0915335659089604,
        "quantile_99": 0.06983305973523263,
        "hill_tail_index": 2.1249151343527988
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02359655330985505,
        "excess_kurtosis": 11.485610532167309,
        "return_acf_1": -0.15276603164117572,
        "abs_return_acf_1": 0.4815660754461495,
        "abs_return_acf_5": 0.44059309183465306,
        "abs_return_acf_20": 0.3519460397730364,
        "quantile_01": -0.09591800311531519,
        "quantile_99": 0.066537566070204,
        "hill_tail_index": 2.6509839482172315
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023501107550619887,
        "excess_kurtosis": 18.170838965481707,
        "return_acf_1": -0.17330318241473722,
        "abs_return_acf_1": 0.5236676365531671,
        "abs_return_acf_5": 0.46868575241944177,
        "abs_return_acf_20": 0.3669800825528028,
        "quantile_01": -0.07838275702057071,
        "quantile_99": 0.06448715130653072,
        "hill_tail_index": 2.2273985412662896
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0248249390733779,
        "excess_kurtosis": 12.642496456107226,
        "return_acf_1": -0.08961814823132722,
        "abs_return_acf_1": 0.4988846817653468,
        "abs_return_acf_5": 0.4636807209324628,
        "abs_return_acf_20": 0.378512580757683,
        "quantile_01": -0.10791084961940073,
        "quantile_99": 0.07803707310663174,
        "hill_tail_index": 2.844485082554762
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021981025719912405,
        "excess_kurtosis": 28.39734176363217,
        "return_acf_1": -0.20664519870829634,
        "abs_return_acf_1": 0.49828718711752557,
        "abs_return_acf_5": 0.4831421755347566,
        "abs_return_acf_20": 0.2747835438370449,
        "quantile_01": -0.06407453392393037,
        "quantile_99": 0.04610848252246641,
        "hill_tail_index": 1.5478533886833874
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02607905250278552,
        "excess_kurtosis": 11.811459230052503,
        "return_acf_1": -0.20738030255327713,
        "abs_return_acf_1": 0.5544210454527634,
        "abs_return_acf_5": 0.5133905469018858,
        "abs_return_acf_20": 0.41756014498760113,
        "quantile_01": -0.09663947587252616,
        "quantile_99": 0.09172037120457757,
        "hill_tail_index": 4.860615645287859
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
Unseen state share: 0.14444444444444443
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
