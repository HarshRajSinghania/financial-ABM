# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27066
Run ID: `af47976693254c38e3f31c866b284baeeacd8e48cba1be7382039ad47d653e45`
Result fingerprint: `9b1b31125fa9910e353f77d72e374ca9a8ec53a4372d47c563967af6698d6065`

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
    "equal_weight_sd": -0.5472120787382012,
    "equal_weight_raw": -8.208181181073018,
    "fixed_start_cap_weight_sd": -0.5409736496482888,
    "fixed_start_cap_weight_raw": -8.114604744724332,
    "end_cap_weight_sd": -0.5373714261200507,
    "end_cap_weight_raw": -8.06057139180076
  },
  "full_period_change": {
    "equal_weight_sd": -0.9096525549286757,
    "equal_weight_raw": -13.644788323930136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8597910530201148,
    "inflation_mean_sd": 0.5142083333333334
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.39433333333333637,
    "equal_weight_raw": 5.915000000000045,
    "fixed_start_cap_weight_sd": 0.4002374488901649,
    "fixed_start_cap_weight_raw": 6.0035617333524725,
    "end_cap_weight_sd": 0.3958445650980345,
    "end_cap_weight_raw": 5.9376684764705185
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5490476190476158,
      "change_raw": -8.235714285714236,
      "decay_adjusted_gain_sd": 0.4033333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5271031746031714,
      "change_raw": -7.90654761904757,
      "decay_adjusted_gain_sd": 0.425277777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.5569606074208138,
      "change_raw": -8.354409111312206,
      "decay_adjusted_gain_sd": 0.37736111111111403
    },
    "large_minus_small_sd": 0.007912988373197982,
    "large_minus_small_raw": 0.11869482559796973
  },
  "inflation": {
    "initial_mean_sd": 0.23808333333333334,
    "final_mean_sd": 0.5355833333333334,
    "mean_sd": 0.4127592978073827,
    "mean_absolute_raw_gap": 6.191389467110741,
    "final_absolute_raw_gap": 8.033750000000001,
    "mean_range_fraction": 0.06191389467110741
  },
  "impact": {
    "initial_share": 0.25333333333333335,
    "final_share": 0.28,
    "initial_wealth_share": 0.32398158098231367,
    "final_wealth_share": 0.309983611279535
  },
  "pricing_slope": {
    "mean": -0.0008527388632781435,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.3093495233935556,
    "real_improvement_cost": 0.29462442515139975,
    "washing_cost": 0.014725098242155777,
    "fine_transfer": 0.020056858021090196,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3294063814146458,
    "resource_cost_fraction_initial_cap": 0.010311650779785185,
    "private_net_outflow_fraction_initial_cap": 0.010980212713821526,
    "fine_transfer_fraction_initial_cap": 0.0006685619340363398,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008818806303362282,
    "unapplied_final_day_resource_cost": 0.007139450483586993
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 38.241532976114925,
    "beneficial_raw_gain_per_resource_cost": 573.6229946417238,
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
    "accrued_cost": 3.0350951022589188,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.05890462606844219,
    "accrued_cost_fraction_initial_cap": 0.10116983674196395,
    "mean_contract_rate": 0.04250682831658109,
    "maximum_ledger_error": 6.268043809681823e-20
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
    "maximum_relative_cash_error": 1.1188816683641175e-15,
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
      "minimum": -0.20636101566907655,
      "maximum": -0.04260368421658227,
      "mean": -0.13344857091028434,
      "median": -0.13540545756797182,
      "quantile_05": -0.18917135017264106,
      "quantile_95": -0.05820450488131809
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
      "minimum": 0.3066469972288034,
      "maximum": 0.7714002060505049,
      "mean": 0.5243730011290332,
      "median": 0.5309830363487082,
      "quantile_05": 0.343775991082349,
      "quantile_95": 0.7209720174666803
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
        "daily_volatility": 0.020752690685070654,
        "excess_kurtosis": 11.594437045214406,
        "return_acf_1": -0.09905276345921465,
        "abs_return_acf_1": 0.334337638903868,
        "abs_return_acf_5": 0.44308076030336385,
        "abs_return_acf_20": 0.3032574901731486,
        "quantile_01": -0.05802247757709835,
        "quantile_99": 0.058617324540245715,
        "hill_tail_index": 2.4188739574727594
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.015724311939017122,
        "excess_kurtosis": 4.3763987924925125,
        "return_acf_1": -0.12702077351046798,
        "abs_return_acf_1": 0.2672179221837237,
        "abs_return_acf_5": 0.2580113897546962,
        "abs_return_acf_20": 0.19564255982275888,
        "quantile_01": -0.04121766879009042,
        "quantile_99": 0.04279021936353924,
        "hill_tail_index": 3.2617218208096754
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01856789863746136,
        "excess_kurtosis": 5.380669860677095,
        "return_acf_1": -0.11527503394250292,
        "abs_return_acf_1": 0.2889502288101887,
        "abs_return_acf_5": 0.35009450591756447,
        "abs_return_acf_20": 0.26316717068777035,
        "quantile_01": -0.058732906250306,
        "quantile_99": 0.04771611199387615,
        "hill_tail_index": 3.891055720463903
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01830668151409947,
        "excess_kurtosis": 3.0067367418286777,
        "return_acf_1": -0.10636672769680848,
        "abs_return_acf_1": 0.2791059986808769,
        "abs_return_acf_5": 0.31948243139184557,
        "abs_return_acf_20": 0.18579144722904728,
        "quantile_01": -0.0524879657995284,
        "quantile_99": 0.04526865684964694,
        "hill_tail_index": 4.003060537995543
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.014992047239903843,
        "excess_kurtosis": 3.990976372155986,
        "return_acf_1": -0.09626550204618463,
        "abs_return_acf_1": 0.2188795805449323,
        "abs_return_acf_5": 0.21032545285797621,
        "abs_return_acf_20": 0.15553972802018698,
        "quantile_01": -0.03686399728208212,
        "quantile_99": 0.03666961139377788,
        "hill_tail_index": 2.7132103886932213
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01811934014033278,
        "excess_kurtosis": 8.958738237178414,
        "return_acf_1": -0.20636101566907655,
        "abs_return_acf_1": 0.2533824508325481,
        "abs_return_acf_5": 0.2878329663830209,
        "abs_return_acf_20": 0.22233876111221773,
        "quantile_01": -0.059532545422475595,
        "quantile_99": 0.04544393132855101,
        "hill_tail_index": 2.810433674360653
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01771020426718646,
        "excess_kurtosis": 2.8463525714157445,
        "return_acf_1": -0.17793257822548839,
        "abs_return_acf_1": 0.26765667516715563,
        "abs_return_acf_5": 0.3507879218873036,
        "abs_return_acf_20": 0.25445562989914583,
        "quantile_01": -0.04779590707838255,
        "quantile_99": 0.052236542677299144,
        "hill_tail_index": 4.695847110202206
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01965469410819963,
        "excess_kurtosis": 4.763940202101345,
        "return_acf_1": -0.16328089642004825,
        "abs_return_acf_1": 0.3184062553897918,
        "abs_return_acf_5": 0.35468701740609904,
        "abs_return_acf_20": 0.3135954968995954,
        "quantile_01": -0.06278087701618623,
        "quantile_99": 0.05425875927398878,
        "hill_tail_index": 4.097701133719372
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01823981377481099,
        "excess_kurtosis": 2.5140774716580996,
        "return_acf_1": -0.1258491187006765,
        "abs_return_acf_1": 0.3190518346654769,
        "abs_return_acf_5": 0.3125195804619542,
        "abs_return_acf_20": 0.2968334815831309,
        "quantile_01": -0.053160904492363166,
        "quantile_99": 0.049378628086833055,
        "hill_tail_index": 4.806812065668574
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017862463262987748,
        "excess_kurtosis": 3.8433449595080402,
        "return_acf_1": -0.18531235002516144,
        "abs_return_acf_1": 0.33633863774393785,
        "abs_return_acf_5": 0.27828438581846243,
        "abs_return_acf_20": 0.2700292697013678,
        "quantile_01": -0.05707854887886907,
        "quantile_99": 0.05086428215612372,
        "hill_tail_index": 4.373561806084642
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.0174262876868991,
        "excess_kurtosis": 3.3423143627839087,
        "return_acf_1": -0.16935768364442205,
        "abs_return_acf_1": 0.2914556764438315,
        "abs_return_acf_5": 0.29186201574652926,
        "abs_return_acf_20": 0.25656734251796914,
        "quantile_01": -0.050327433874908595,
        "quantile_99": 0.05087134666930601,
        "hill_tail_index": 4.501983263796697
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019427487532527824,
        "excess_kurtosis": 6.902993947175505,
        "return_acf_1": -0.1013527489069099,
        "abs_return_acf_1": 0.33486464524228093,
        "abs_return_acf_5": 0.3367878343481594,
        "abs_return_acf_20": 0.2912374241281583,
        "quantile_01": -0.057341229803098075,
        "quantile_99": 0.05302317679314586,
        "hill_tail_index": 2.90077472256702
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02039560789029637,
        "excess_kurtosis": 20.189305740705922,
        "return_acf_1": -0.12116893880953085,
        "abs_return_acf_1": 0.36453622502387995,
        "abs_return_acf_5": 0.3173920053171149,
        "abs_return_acf_20": 0.2566955042896894,
        "quantile_01": -0.06206039143625219,
        "quantile_99": 0.05528674711536593,
        "hill_tail_index": 2.656368889317959
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01858627501490283,
        "excess_kurtosis": 3.162322553900478,
        "return_acf_1": -0.19232871392966983,
        "abs_return_acf_1": 0.35602622993875044,
        "abs_return_acf_5": 0.37127102804662404,
        "abs_return_acf_20": 0.31449048393802836,
        "quantile_01": -0.055426867516766065,
        "quantile_99": 0.048494768014901435,
        "hill_tail_index": 3.462290814776253
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01671312752356425,
        "excess_kurtosis": 2.4911683089840677,
        "return_acf_1": -0.166340904295921,
        "abs_return_acf_1": 0.28064956002725183,
        "abs_return_acf_5": 0.25924815453378164,
        "abs_return_acf_20": 0.17165902524025853,
        "quantile_01": -0.05040415200881546,
        "quantile_99": 0.04295342716840929,
        "hill_tail_index": 3.686558438618956
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017973216916596136,
        "excess_kurtosis": 8.339531887867809,
        "return_acf_1": -0.04260368421658227,
        "abs_return_acf_1": 0.34373749478541266,
        "abs_return_acf_5": 0.35075041485863206,
        "abs_return_acf_20": 0.30573262497438225,
        "quantile_01": -0.051692991987817904,
        "quantile_99": 0.049455824696243836,
        "hill_tail_index": 2.387717402505115
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01792721185933975,
        "excess_kurtosis": 6.760129656576559,
        "return_acf_1": -0.176123655802275,
        "abs_return_acf_1": 0.3279505771089442,
        "abs_return_acf_5": 0.3561748683049891,
        "abs_return_acf_20": 0.29198424075415,
        "quantile_01": -0.05470532859961725,
        "quantile_99": 0.05142735962356873,
        "hill_tail_index": 3.790407381758306
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017810064107578107,
        "excess_kurtosis": 4.322671856376978,
        "return_acf_1": -0.045943173392528285,
        "abs_return_acf_1": 0.26863425182749545,
        "abs_return_acf_5": 0.31474684126005986,
        "abs_return_acf_20": 0.20495246954521162,
        "quantile_01": -0.052743300987021915,
        "quantile_99": 0.04810241548109927,
        "hill_tail_index": 3.485470506358834
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01872605964599267,
        "excess_kurtosis": 5.302996099888617,
        "return_acf_1": -0.13662456519490124,
        "abs_return_acf_1": 0.3526388164207129,
        "abs_return_acf_5": 0.3479621636211993,
        "abs_return_acf_20": 0.3117109735717219,
        "quantile_01": -0.06099067252774707,
        "quantile_99": 0.05205249844428766,
        "hill_tail_index": 3.472476737645094
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01738440163332064,
        "excess_kurtosis": 5.701890902661123,
        "return_acf_1": -0.15293257048998665,
        "abs_return_acf_1": 0.2922951585406281,
        "abs_return_acf_5": 0.29608640779130396,
        "abs_return_acf_20": 0.24106995562173333,
        "quantile_01": -0.0481938200261697,
        "quantile_99": 0.04284671877775318,
        "hill_tail_index": 3.2515682973635958
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01922429673394286,
        "excess_kurtosis": 9.390605048167423,
        "return_acf_1": -0.14384779029516542,
        "abs_return_acf_1": 0.30731428748225126,
        "abs_return_acf_5": 0.3793213507045569,
        "abs_return_acf_20": 0.3065729304059721,
        "quantile_01": -0.05795958847104539,
        "quantile_99": 0.05384322769193805,
        "hill_tail_index": 2.7640419079989007
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018173609282380546,
        "excess_kurtosis": 5.989559245749119,
        "return_acf_1": -0.1341863499410424,
        "abs_return_acf_1": 0.26423957813492055,
        "abs_return_acf_5": 0.2791527675404319,
        "abs_return_acf_20": 0.22386155870703045,
        "quantile_01": -0.0566869500553155,
        "quantile_99": 0.05073089134988392,
        "hill_tail_index": 3.600942298865842
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01771320684342098,
        "excess_kurtosis": 7.392570831996558,
        "return_acf_1": -0.10615504883727964,
        "abs_return_acf_1": 0.33329945478814155,
        "abs_return_acf_5": 0.3382591923867967,
        "abs_return_acf_20": 0.252659409451061,
        "quantile_01": -0.05156198895303852,
        "quantile_99": 0.048125989522202234,
        "hill_tail_index": 3.2791121881750795
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017731290600218372,
        "excess_kurtosis": 4.443800592651827,
        "return_acf_1": -0.13288135588898783,
        "abs_return_acf_1": 0.22834512953241207,
        "abs_return_acf_5": 0.33279774740156504,
        "abs_return_acf_20": 0.2247866983783082,
        "quantile_01": -0.05693024773183489,
        "quantile_99": 0.04465467465675792,
        "hill_tail_index": 3.590271485639499
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017791050564317935,
        "excess_kurtosis": 3.720105905402912,
        "return_acf_1": -0.07319057670094992,
        "abs_return_acf_1": 0.2657458044258719,
        "abs_return_acf_5": 0.25178858158261763,
        "abs_return_acf_20": 0.2128272505111191,
        "quantile_01": -0.05147576931901765,
        "quantile_99": 0.05005635785044071,
        "hill_tail_index": 4.540221417106338
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01854049622856538,
        "excess_kurtosis": 7.525225788501583,
        "return_acf_1": -0.1453703707812185,
        "abs_return_acf_1": 0.34313933978002686,
        "abs_return_acf_5": 0.35845195381055917,
        "abs_return_acf_20": 0.30895509160380663,
        "quantile_01": -0.06256352646795058,
        "quantile_99": 0.047607708220660044,
        "hill_tail_index": 3.217838686017608
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02064207421021396,
        "excess_kurtosis": 25.91282054692224,
        "return_acf_1": -0.11556626076785902,
        "abs_return_acf_1": 0.29247810237670174,
        "abs_return_acf_5": 0.3194749865466698,
        "abs_return_acf_20": 0.2660836648292239,
        "quantile_01": -0.05797977094435466,
        "quantile_99": 0.05072993134689981,
        "hill_tail_index": 1.9550427411275795
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01866000127212762,
        "excess_kurtosis": 14.055618227580783,
        "return_acf_1": -0.13897679955738265,
        "abs_return_acf_1": 0.3044660228428771,
        "abs_return_acf_5": 0.2586029558955971,
        "abs_return_acf_20": 0.24443887594427066,
        "quantile_01": -0.05421363972404195,
        "quantile_99": 0.04105304304922934,
        "hill_tail_index": 2.3415157916318785
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016895487605403253,
        "excess_kurtosis": 4.4101399897173845,
        "return_acf_1": -0.1604067128179025,
        "abs_return_acf_1": 0.312694684724816,
        "abs_return_acf_5": 0.26200094981023075,
        "abs_return_acf_20": 0.22009370746129178,
        "quantile_01": -0.04921964279192302,
        "quantile_99": 0.04430603611257255,
        "hill_tail_index": 3.8006583181916627
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01889855508652104,
        "excess_kurtosis": 4.631773089721607,
        "return_acf_1": -0.14538246334238505,
        "abs_return_acf_1": 0.3029785796032131,
        "abs_return_acf_5": 0.37605237370367395,
        "abs_return_acf_20": 0.26276421315094206,
        "quantile_01": -0.055491120020395045,
        "quantile_99": 0.0493351454989259,
        "hill_tail_index": 4.664109341215256
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
