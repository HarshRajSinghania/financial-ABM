# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27237
Run ID: `20d085500b44e93907126ef0b1e5607231d2feb667eae6650795c876455f3ed4`
Result fingerprint: `29eda952b4504c80dea908e1fe21642a17a0c4fc78d6cee5852778c6e80bea57`

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
    "equal_weight_sd": -0.7678809523809492,
    "equal_weight_raw": -11.518214285714235,
    "fixed_start_cap_weight_sd": -0.7886330931744322,
    "fixed_start_cap_weight_raw": -11.82949639761648,
    "end_cap_weight_sd": -0.769033928697085,
    "end_cap_weight_raw": -11.535508930456274
  },
  "full_period_change": {
    "equal_weight_sd": -1.1949880952380905,
    "equal_weight_raw": -17.924821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1258240740740697,
    "inflation_mean_sd": 0.46875396825396826
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.18450000000000324,
    "equal_weight_raw": 2.767500000000048,
    "fixed_start_cap_weight_sd": 0.16374785920652013,
    "fixed_start_cap_weight_raw": 2.456217888097801,
    "end_cap_weight_sd": 0.1833470236838673,
    "end_cap_weight_raw": 2.750205355258011
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8198809523809493,
      "change_raw": -12.29821428571424,
      "decay_adjusted_gain_sd": 0.13250000000000306
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7807142857142826,
      "change_raw": -11.71071428571424,
      "decay_adjusted_gain_sd": 0.17166666666666966
    },
    "small": {
      "count": 18,
      "change_sd": -0.7527976190476158,
      "change_raw": -11.291964285714236,
      "decay_adjusted_gain_sd": 0.19958333333333664
    },
    "large_minus_small_sd": -0.0670833333333335,
    "large_minus_small_raw": -1.0062500000000023
  },
  "inflation": {
    "initial_mean_sd": 0.19333333333333336,
    "final_mean_sd": 0.5064166666666666,
    "mean_sd": 0.3435190813211213,
    "mean_absolute_raw_gap": 5.152786219816819,
    "final_absolute_raw_gap": 7.596249999999999,
    "mean_range_fraction": 0.05152786219816819
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.34,
    "initial_wealth_share": 0.39823737691855987,
    "final_wealth_share": 0.3784481260063142
  },
  "pricing_slope": {
    "mean": -0.0027547247366810695,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.05506775857124657,
    "real_improvement_cost": 0.04578577865535362,
    "washing_cost": 0.009281979915892954,
    "fine_transfer": 0.0032256151667163506,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05829337373796292,
    "resource_cost_fraction_initial_cap": 0.0018355919523748853,
    "private_net_outflow_fraction_initial_cap": 0.0019431124579320969,
    "fine_transfer_fraction_initial_cap": 0.00010752050555721167,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0007297707770879486,
    "unapplied_final_day_resource_cost": 0.002320606672425427
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 100.51253480453401,
    "beneficial_raw_gain_per_resource_cost": 1507.68802206801,
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
    "accrued_cost": 3.3268912828060433,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.350700806615566,
    "accrued_cost_fraction_initial_cap": 0.11089637609353475,
    "mean_contract_rate": 0.04530672134758448,
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
    "maximum_relative_cash_error": 2.0272715829299103e-15,
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
      "minimum": -0.18222389214275453,
      "maximum": -0.057298929910310714,
      "mean": -0.12687610425102339,
      "median": -0.13124140402376278,
      "quantile_05": -0.16486610932918058,
      "quantile_95": -0.07024572940921182
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
      "minimum": 0.29001134452937677,
      "maximum": 0.7913373709675139,
      "mean": 0.6138019345599827,
      "median": 0.6393206563263841,
      "quantile_05": 0.37989206095371103,
      "quantile_95": 0.7622236512120439
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
        "daily_volatility": 0.0229092375094825,
        "excess_kurtosis": 10.704989556858958,
        "return_acf_1": -0.15652865198514604,
        "abs_return_acf_1": 0.3964782386460534,
        "abs_return_acf_5": 0.429864886899633,
        "abs_return_acf_20": 0.3303624167692615,
        "quantile_01": -0.07133619263579379,
        "quantile_99": 0.07672416996150459,
        "hill_tail_index": 2.976498259533933
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017804305873697242,
        "excess_kurtosis": 6.7996637414572465,
        "return_acf_1": -0.06104587924042987,
        "abs_return_acf_1": 0.29948870458996335,
        "abs_return_acf_5": 0.32899238391900054,
        "abs_return_acf_20": 0.24360166034771874,
        "quantile_01": -0.052696648221941124,
        "quantile_99": 0.048085689541816565,
        "hill_tail_index": 3.2183916584838816
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021353364240827562,
        "excess_kurtosis": 9.242572745714202,
        "return_acf_1": -0.13012542831982554,
        "abs_return_acf_1": 0.329072510196801,
        "abs_return_acf_5": 0.3712437494923261,
        "abs_return_acf_20": 0.3061066390013313,
        "quantile_01": -0.07041973805141491,
        "quantile_99": 0.06567405533506138,
        "hill_tail_index": 3.777758673623963
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0192360109646311,
        "excess_kurtosis": 5.022620316455381,
        "return_acf_1": -0.10236800724825824,
        "abs_return_acf_1": 0.3028946489085978,
        "abs_return_acf_5": 0.3226341134760796,
        "abs_return_acf_20": 0.21357229583491646,
        "quantile_01": -0.06076329953069712,
        "quantile_99": 0.05508925777326578,
        "hill_tail_index": 4.202209029391147
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02175368166550206,
        "excess_kurtosis": 8.120645042194548,
        "return_acf_1": -0.13420666561982386,
        "abs_return_acf_1": 0.3581325457333662,
        "abs_return_acf_5": 0.3692713623274366,
        "abs_return_acf_20": 0.3680650584045992,
        "quantile_01": -0.06843477726242185,
        "quantile_99": 0.061375831860029824,
        "hill_tail_index": 3.301711042206095
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018343736061974102,
        "excess_kurtosis": 2.9172889693445994,
        "return_acf_1": -0.1507755360212031,
        "abs_return_acf_1": 0.28245405262952133,
        "abs_return_acf_5": 0.2747058271229976,
        "abs_return_acf_20": 0.2353707054075021,
        "quantile_01": -0.053186094489824795,
        "quantile_99": 0.0518398047534797,
        "hill_tail_index": 4.5183363270931425
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020262258413032544,
        "excess_kurtosis": 5.276544988416555,
        "return_acf_1": -0.13960525674423918,
        "abs_return_acf_1": 0.3196305242911628,
        "abs_return_acf_5": 0.35936196302568946,
        "abs_return_acf_20": 0.27740060568406977,
        "quantile_01": -0.06406087327635783,
        "quantile_99": 0.052423493563477,
        "hill_tail_index": 3.728198311294923
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021824148803602225,
        "excess_kurtosis": 8.243212783445014,
        "return_acf_1": -0.14482927998887196,
        "abs_return_acf_1": 0.32965030968410547,
        "abs_return_acf_5": 0.3399894939120194,
        "abs_return_acf_20": 0.23869437781783467,
        "quantile_01": -0.07108939815792834,
        "quantile_99": 0.06928349810683249,
        "hill_tail_index": 3.7288230794047763
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020583921840118057,
        "excess_kurtosis": 8.387681799823774,
        "return_acf_1": -0.057298929910310714,
        "abs_return_acf_1": 0.4076322293924152,
        "abs_return_acf_5": 0.35510714037450203,
        "abs_return_acf_20": 0.2902989531511232,
        "quantile_01": -0.06440938664925348,
        "quantile_99": 0.05706834833241584,
        "hill_tail_index": 2.6897740452512626
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021498823354694163,
        "excess_kurtosis": 8.96983254132771,
        "return_acf_1": -0.10494119221494266,
        "abs_return_acf_1": 0.36747665410134156,
        "abs_return_acf_5": 0.3481582728187366,
        "abs_return_acf_20": 0.2914141234252518,
        "quantile_01": -0.07410443740073329,
        "quantile_99": 0.06026375437013121,
        "hill_tail_index": 2.739698787509046
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020289758678897013,
        "excess_kurtosis": 5.493261076549816,
        "return_acf_1": -0.13141791063998606,
        "abs_return_acf_1": 0.40004145874609787,
        "abs_return_acf_5": 0.34291523316009975,
        "abs_return_acf_20": 0.3354607563700919,
        "quantile_01": -0.06748339188443014,
        "quantile_99": 0.06746905645751655,
        "hill_tail_index": 4.8570749900310375
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019900627865475896,
        "excess_kurtosis": 5.595433782897768,
        "return_acf_1": -0.11921612955940494,
        "abs_return_acf_1": 0.2752219202014707,
        "abs_return_acf_5": 0.3122173827387592,
        "abs_return_acf_20": 0.2401918263676736,
        "quantile_01": -0.06551193153198234,
        "quantile_99": 0.05933631753585591,
        "hill_tail_index": 3.4426790087410684
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021006642336495827,
        "excess_kurtosis": 9.503961816558713,
        "return_acf_1": -0.09765827080669823,
        "abs_return_acf_1": 0.40417028590743526,
        "abs_return_acf_5": 0.4003285736218416,
        "abs_return_acf_20": 0.30430515521214707,
        "quantile_01": -0.06100685176220601,
        "quantile_99": 0.06182254106706511,
        "hill_tail_index": 3.0069161613734963
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020198442319971796,
        "excess_kurtosis": 4.285652422785697,
        "return_acf_1": -0.1673086370123155,
        "abs_return_acf_1": 0.4085537212634241,
        "abs_return_acf_5": 0.394976191234363,
        "abs_return_acf_20": 0.34080278401830233,
        "quantile_01": -0.0666128652915837,
        "quantile_99": 0.06697620112741832,
        "hill_tail_index": 6.657368839568145
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020136804991461237,
        "excess_kurtosis": 6.018099221580304,
        "return_acf_1": -0.15352730831862127,
        "abs_return_acf_1": 0.37310584931338237,
        "abs_return_acf_5": 0.38956142981541464,
        "abs_return_acf_20": 0.2729743285741237,
        "quantile_01": -0.056146595360585555,
        "quantile_99": 0.06817710375377761,
        "hill_tail_index": 3.048957498877483
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02108186988662722,
        "excess_kurtosis": 7.959293245698557,
        "return_acf_1": -0.11933662948332148,
        "abs_return_acf_1": 0.40380825793553404,
        "abs_return_acf_5": 0.40925039777984634,
        "abs_return_acf_20": 0.32006026465067455,
        "quantile_01": -0.081461333680729,
        "quantile_99": 0.0578670754369703,
        "hill_tail_index": 2.930295902975128
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01686065182884135,
        "excess_kurtosis": 4.966147510038719,
        "return_acf_1": -0.14744219862185498,
        "abs_return_acf_1": 0.34642285493400504,
        "abs_return_acf_5": 0.2776361263972844,
        "abs_return_acf_20": 0.20648723767667632,
        "quantile_01": -0.044575676037271,
        "quantile_99": 0.05027658473613759,
        "hill_tail_index": 3.962556532855033
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01640886410172514,
        "excess_kurtosis": 2.1556883302355283,
        "return_acf_1": -0.14163751421387705,
        "abs_return_acf_1": 0.22342381177169465,
        "abs_return_acf_5": 0.23006336420595483,
        "abs_return_acf_20": 0.19471489200870876,
        "quantile_01": -0.04343408646999133,
        "quantile_99": 0.04905561379414991,
        "hill_tail_index": 3.5741371332030973
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01969735744151914,
        "excess_kurtosis": 4.245816623223764,
        "return_acf_1": -0.14889460658039466,
        "abs_return_acf_1": 0.3585629291809128,
        "abs_return_acf_5": 0.39500909639140375,
        "abs_return_acf_20": 0.3430758622506287,
        "quantile_01": -0.062064182581427374,
        "quantile_99": 0.055309641242363136,
        "hill_tail_index": 3.518106489199246
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021042371093142945,
        "excess_kurtosis": 14.278058457321734,
        "return_acf_1": -0.13106489740753946,
        "abs_return_acf_1": 0.34582804276304624,
        "abs_return_acf_5": 0.3066279833012473,
        "abs_return_acf_20": 0.2722776047544703,
        "quantile_01": -0.07068475349346193,
        "quantile_99": 0.06160843229256663,
        "hill_tail_index": 3.9332461968453676
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023213206396362884,
        "excess_kurtosis": 10.395967782120758,
        "return_acf_1": -0.14584180257400978,
        "abs_return_acf_1": 0.3781398676412244,
        "abs_return_acf_5": 0.44200108498318,
        "abs_return_acf_20": 0.3450748600505074,
        "quantile_01": -0.07579367074518323,
        "quantile_99": 0.07534060475444081,
        "hill_tail_index": 3.6243267246522537
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019644770714879495,
        "excess_kurtosis": 4.887879535635712,
        "return_acf_1": -0.08148999072661185,
        "abs_return_acf_1": 0.30348353687970897,
        "abs_return_acf_5": 0.33564797273811264,
        "abs_return_acf_20": 0.27860277111374104,
        "quantile_01": -0.06318444853724312,
        "quantile_99": 0.06112362153680552,
        "hill_tail_index": 3.997468840565415
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02104080378750324,
        "excess_kurtosis": 8.103585844855825,
        "return_acf_1": -0.1307038871182144,
        "abs_return_acf_1": 0.4072806279862959,
        "abs_return_acf_5": 0.40562625381160217,
        "abs_return_acf_20": 0.29921978197942123,
        "quantile_01": -0.07541565213223445,
        "quantile_99": 0.06024337489964374,
        "hill_tail_index": 3.444875253330077
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02147681483911634,
        "excess_kurtosis": 8.837782461066494,
        "return_acf_1": -0.10730808346729193,
        "abs_return_acf_1": 0.35634420008168377,
        "abs_return_acf_5": 0.398270160365227,
        "abs_return_acf_20": 0.3242002225571794,
        "quantile_01": -0.07714983052233503,
        "quantile_99": 0.06646139078783303,
        "hill_tail_index": 3.8201576556721397
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021717199015883693,
        "excess_kurtosis": 8.363848634495367,
        "return_acf_1": -0.1375788637305277,
        "abs_return_acf_1": 0.46498577803626373,
        "abs_return_acf_5": 0.43377050832322206,
        "abs_return_acf_20": 0.36907338160508635,
        "quantile_01": -0.0745352645318212,
        "quantile_99": 0.06810335764201843,
        "hill_tail_index": 3.758298998019354
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02045251880505235,
        "excess_kurtosis": 8.018466172087214,
        "return_acf_1": -0.12579278075103612,
        "abs_return_acf_1": 0.34885474589712673,
        "abs_return_acf_5": 0.31596602868181584,
        "abs_return_acf_20": 0.2921163953447173,
        "quantile_01": -0.06841384691354294,
        "quantile_99": 0.059131544647697126,
        "hill_tail_index": 3.3389196763218796
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017326267968096772,
        "excess_kurtosis": 4.321796736469755,
        "return_acf_1": -0.10867751710298267,
        "abs_return_acf_1": 0.17896550559976881,
        "abs_return_acf_5": 0.19991460426067614,
        "abs_return_acf_20": 0.20360780053366245,
        "quantile_01": -0.042265799416683666,
        "quantile_99": 0.048865463602633566,
        "hill_tail_index": 3.3703970290490495
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020584611299373064,
        "excess_kurtosis": 7.4008275453516195,
        "return_acf_1": -0.16188079771646016,
        "abs_return_acf_1": 0.37393525605372707,
        "abs_return_acf_5": 0.3646470460934496,
        "abs_return_acf_20": 0.31441456274198903,
        "quantile_01": -0.06970318411737383,
        "quantile_99": 0.06613860310613462,
        "hill_tail_index": 4.634417596687426
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02029698167506135,
        "excess_kurtosis": 8.521219066728445,
        "return_acf_1": -0.08555658226374838,
        "abs_return_acf_1": 0.34866703973412055,
        "abs_return_acf_5": 0.35205984523857636,
        "abs_return_acf_20": 0.2879499293439043,
        "quantile_01": -0.06997472399062775,
        "quantile_99": 0.055617791256522844,
        "hill_tail_index": 3.5556658414257254
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020606649121205987,
        "excess_kurtosis": 8.78917742971696,
        "return_acf_1": -0.18222389214275453,
        "abs_return_acf_1": 0.3180275042429718,
        "abs_return_acf_5": 0.3007822419490997,
        "abs_return_acf_20": 0.270843872935856,
        "quantile_01": -0.06203954354883725,
        "quantile_99": 0.05866170027336738,
        "hill_tail_index": 4.302405527822511
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
