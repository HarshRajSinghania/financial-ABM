# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27211
Run ID: `738231a7d787befc8a3d205f9659068fcb85a7b0c806e93c69daa786b58b8360`
Result fingerprint: `2f4e65b5f46aae04aedde4d0e89daf162aa366a9369fc910a0b56004517b3ff5`

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
    "equal_weight_sd": -0.7667976190476157,
    "equal_weight_raw": -11.501964285714235,
    "fixed_start_cap_weight_sd": -0.7266009815538438,
    "fixed_start_cap_weight_raw": -10.899014723307658,
    "end_cap_weight_sd": -0.7534994354937097,
    "end_cap_weight_raw": -11.302491532405648
  },
  "full_period_change": {
    "equal_weight_sd": -1.195654761904757,
    "equal_weight_raw": -17.934821428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1198902116402072,
    "inflation_mean_sd": 0.8849920634920635
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1782839746152341,
    "equal_weight_raw": 2.6742596192285117,
    "fixed_start_cap_weight_sd": 0.222847013392191,
    "fixed_start_cap_weight_raw": 3.342705200882864,
    "end_cap_weight_sd": 0.1963543717519239,
    "end_cap_weight_raw": 2.9453155762788588
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6457142857142825,
      "change_raw": -9.685714285714237,
      "decay_adjusted_gain_sd": 0.3066666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7693253968253935,
      "change_raw": -11.539880952380901,
      "decay_adjusted_gain_sd": 0.1830555555555588
    },
    "small": {
      "count": 18,
      "change_sd": -0.7857142857142825,
      "change_raw": -11.785714285714237,
      "decay_adjusted_gain_sd": 0.1545010688031658
    },
    "large_minus_small_sd": 0.14,
    "large_minus_small_raw": 2.1
  },
  "inflation": {
    "initial_mean_sd": 0.2813333333333333,
    "final_mean_sd": 0.9525833333333332,
    "mean_sd": 0.6528234110463503,
    "mean_absolute_raw_gap": 9.792351165695253,
    "final_absolute_raw_gap": 14.28875,
    "mean_range_fraction": 0.09792351165695252
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.29333333333333333,
    "initial_wealth_share": 0.31875162138826657,
    "final_wealth_share": 0.3366629711225193
  },
  "pricing_slope": {
    "mean": -0.0017381617985849924,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.7999236460076057,
    "real_improvement_cost": 0.7392642644235801,
    "washing_cost": 0.06065938158402569,
    "fine_transfer": 0.0064152842595242175,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.8063389302671299,
    "resource_cost_fraction_initial_cap": 0.026664121533586858,
    "private_net_outflow_fraction_initial_cap": 0.026877964342237663,
    "fine_transfer_fraction_initial_cap": 0.00021384280865080726,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.20139099667733878,
    "unapplied_final_day_resource_cost": 0.002420073393691399
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 6.686287203974176,
    "beneficial_raw_gain_per_resource_cost": 100.29430805961266,
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
    "accrued_cost": 2.886538200688514,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.08965227550196225,
    "accrued_cost_fraction_initial_cap": 0.09621794002295046,
    "mean_contract_rate": 0.040776596283996075,
    "maximum_ledger_error": 3.7269449679189215e-20
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
    "maximum_relative_cash_error": 1.976352894500564e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.19914630586385595,
      "maximum": -0.02025841723053292,
      "mean": -0.1273032589311189,
      "median": -0.13052087719399874,
      "quantile_05": -0.19756049719678595,
      "quantile_95": -0.02436300048383873
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
      "minimum": 0.29711244921446395,
      "maximum": 0.74029458026847,
      "mean": 0.4814097808752355,
      "median": 0.4554626616332613,
      "quantile_05": 0.3422761438103279,
      "quantile_95": 0.6863869381400113
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
        "daily_volatility": 0.018713289388147012,
        "excess_kurtosis": 3.4994714464612393,
        "return_acf_1": -0.13027754499254915,
        "abs_return_acf_1": 0.2734508506931669,
        "abs_return_acf_5": 0.31107546880108344,
        "abs_return_acf_20": 0.342758944028637,
        "quantile_01": -0.05984034295766219,
        "quantile_99": 0.052180334076460805,
        "hill_tail_index": 4.802768527489947
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016194282740694923,
        "excess_kurtosis": 4.262223276276959,
        "return_acf_1": -0.1156742220976017,
        "abs_return_acf_1": 0.21481458995370212,
        "abs_return_acf_5": 0.2164219250516434,
        "abs_return_acf_20": 0.1903590347227232,
        "quantile_01": -0.04815812719885369,
        "quantile_99": 0.038204539465100544,
        "hill_tail_index": 3.0460024353648087
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017889753120574458,
        "excess_kurtosis": 5.785832924481289,
        "return_acf_1": -0.17255678072614292,
        "abs_return_acf_1": 0.34966378338173343,
        "abs_return_acf_5": 0.2956287863994514,
        "abs_return_acf_20": 0.23375959768250545,
        "quantile_01": -0.05250488560619724,
        "quantile_99": 0.04850663524140414,
        "hill_tail_index": 3.7278572657859996
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01600601176666402,
        "excess_kurtosis": 2.3137938925485164,
        "return_acf_1": -0.19751805030918648,
        "abs_return_acf_1": 0.19346303608663892,
        "abs_return_acf_5": 0.1952025830101517,
        "abs_return_acf_20": 0.1504174639235802,
        "quantile_01": -0.04808872305574726,
        "quantile_99": 0.04149645583188519,
        "hill_tail_index": 4.850276458573127
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018635584015188753,
        "excess_kurtosis": 5.64113942020731,
        "return_acf_1": -0.10001533869512258,
        "abs_return_acf_1": 0.34751826627520654,
        "abs_return_acf_5": 0.3182067226394657,
        "abs_return_acf_20": 0.28817564069504226,
        "quantile_01": -0.05818004491523702,
        "quantile_99": 0.05496587997985849,
        "hill_tail_index": 4.088947023607321
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017829955205955244,
        "excess_kurtosis": 4.116121580786293,
        "return_acf_1": -0.14557142526458902,
        "abs_return_acf_1": 0.28748237313049657,
        "abs_return_acf_5": 0.31321578876738665,
        "abs_return_acf_20": 0.2755793345559086,
        "quantile_01": -0.05962542365310472,
        "quantile_99": 0.0439794819171459,
        "hill_tail_index": 3.9538211698187595
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01740222037692467,
        "excess_kurtosis": 4.4522225575739895,
        "return_acf_1": -0.10483796077795068,
        "abs_return_acf_1": 0.2865931971685317,
        "abs_return_acf_5": 0.30477221441887686,
        "abs_return_acf_20": 0.2210632569995837,
        "quantile_01": -0.060460902688086474,
        "quantile_99": 0.04723180192398794,
        "hill_tail_index": 3.293933781935065
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017645691944814808,
        "excess_kurtosis": 10.044505750724289,
        "return_acf_1": -0.13907223492383,
        "abs_return_acf_1": 0.2637044523413345,
        "abs_return_acf_5": 0.39483019088189014,
        "abs_return_acf_20": 0.24519798648445917,
        "quantile_01": -0.047365593926212105,
        "quantile_99": 0.045998231477291415,
        "hill_tail_index": 2.3611937884128946
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01649856736426937,
        "excess_kurtosis": 2.6435917971093312,
        "return_acf_1": -0.18737450180151838,
        "abs_return_acf_1": 0.18149227181447533,
        "abs_return_acf_5": 0.24548938274055723,
        "abs_return_acf_20": 0.19657727730136057,
        "quantile_01": -0.04945148709692074,
        "quantile_99": 0.04126459034021667,
        "hill_tail_index": 3.6477187769710557
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019661951153168756,
        "excess_kurtosis": 3.9774826866381225,
        "return_acf_1": -0.12110862181329404,
        "abs_return_acf_1": 0.33876195501111583,
        "abs_return_acf_5": 0.27756333213401146,
        "abs_return_acf_20": 0.26774981632542816,
        "quantile_01": -0.059220627701023654,
        "quantile_99": 0.05375659160887703,
        "hill_tail_index": 3.6700418811293134
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018713007734554952,
        "excess_kurtosis": 5.877191588335744,
        "return_acf_1": -0.19914630586385595,
        "abs_return_acf_1": 0.3865312089704874,
        "abs_return_acf_5": 0.27441353949181785,
        "abs_return_acf_20": 0.23081191391075645,
        "quantile_01": -0.06203013386461919,
        "quantile_99": 0.05115484830260158,
        "hill_tail_index": 4.125785099762021
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017110988830184946,
        "excess_kurtosis": 4.229955427110629,
        "return_acf_1": -0.17091931507858102,
        "abs_return_acf_1": 0.2968312119058319,
        "abs_return_acf_5": 0.32399132154845717,
        "abs_return_acf_20": 0.2186173795571466,
        "quantile_01": -0.05701969565697653,
        "quantile_99": 0.041609244289144295,
        "hill_tail_index": 3.7370512160883114
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01706019594131284,
        "excess_kurtosis": 4.451134258186777,
        "return_acf_1": -0.08646575147371587,
        "abs_return_acf_1": 0.3413253918427998,
        "abs_return_acf_5": 0.3095377883786144,
        "abs_return_acf_20": 0.21623889037458013,
        "quantile_01": -0.04923298625913161,
        "quantile_99": 0.04485598550137086,
        "hill_tail_index": 3.1092842763770894
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01733214817918636,
        "excess_kurtosis": 9.474832250917064,
        "return_acf_1": -0.14742261195812983,
        "abs_return_acf_1": 0.34521545734795345,
        "abs_return_acf_5": 0.34236460146044223,
        "abs_return_acf_20": 0.22428593408444172,
        "quantile_01": -0.05389150712815271,
        "quantile_99": 0.044428791812516195,
        "hill_tail_index": 2.9558571123344457
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01909651702442547,
        "excess_kurtosis": 5.460751921162853,
        "return_acf_1": -0.19759522646845823,
        "abs_return_acf_1": 0.44664108036924716,
        "abs_return_acf_5": 0.3118882615574116,
        "abs_return_acf_20": 0.26241063654210317,
        "quantile_01": -0.05675841844537067,
        "quantile_99": 0.057108010378427915,
        "hill_tail_index": 3.593902893390238
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019074140395927093,
        "excess_kurtosis": 12.877582688227085,
        "return_acf_1": -0.027407950828587564,
        "abs_return_acf_1": 0.41605591238361944,
        "abs_return_acf_5": 0.3217377607272531,
        "abs_return_acf_20": 0.27892429886405207,
        "quantile_01": -0.05808007229466565,
        "quantile_99": 0.05488606113359503,
        "hill_tail_index": 2.9466723833493393
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.016870037306740512,
        "excess_kurtosis": 17.147709424055712,
        "return_acf_1": -0.08271806963528258,
        "abs_return_acf_1": 0.3921570267204281,
        "abs_return_acf_5": 0.32227899977396895,
        "abs_return_acf_20": 0.2953314592013721,
        "quantile_01": -0.04142540487992211,
        "quantile_99": 0.042582583723572785,
        "hill_tail_index": 2.2127994995506466
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01871365181567506,
        "excess_kurtosis": 4.186529207606533,
        "return_acf_1": -0.11243447420828717,
        "abs_return_acf_1": 0.3277303627220226,
        "abs_return_acf_5": 0.2614585713927316,
        "abs_return_acf_20": 0.2895678443440055,
        "quantile_01": -0.06115871092721072,
        "quantile_99": 0.049147537334121076,
        "hill_tail_index": 3.7900013579828418
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017592825742980597,
        "excess_kurtosis": 7.280000876607895,
        "return_acf_1": -0.08843858641895146,
        "abs_return_acf_1": 0.2540638426821938,
        "abs_return_acf_5": 0.35627938738864845,
        "abs_return_acf_20": 0.2152330214428107,
        "quantile_01": -0.05793593029980617,
        "quantile_99": 0.05133910493663894,
        "hill_tail_index": 3.8298215768256387
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017040022547546784,
        "excess_kurtosis": 6.205236617935174,
        "return_acf_1": -0.13076420939544836,
        "abs_return_acf_1": 0.3556684699726201,
        "abs_return_acf_5": 0.28773683186830346,
        "abs_return_acf_20": 0.2212933925977374,
        "quantile_01": -0.049837412645091006,
        "quantile_99": 0.04484068695891112,
        "hill_tail_index": 3.5960469072961936
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01680349176931438,
        "excess_kurtosis": 2.53038042301291,
        "return_acf_1": -0.15351415554350437,
        "abs_return_acf_1": 0.2117067469407495,
        "abs_return_acf_5": 0.261738085522102,
        "abs_return_acf_20": 0.1840178257437541,
        "quantile_01": -0.0457627470913703,
        "quantile_99": 0.04248239841458426,
        "hill_tail_index": 4.718441882725883
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.015919616532851424,
        "excess_kurtosis": 7.648958417408455,
        "return_acf_1": -0.12084202491034522,
        "abs_return_acf_1": 0.2785841722871806,
        "abs_return_acf_5": 0.21108511799443516,
        "abs_return_acf_20": 0.2039116285362691,
        "quantile_01": -0.03863893561988194,
        "quantile_99": 0.04187486905926202,
        "hill_tail_index": 2.4394331051532703
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017678674246684078,
        "excess_kurtosis": 13.00254688815998,
        "return_acf_1": -0.02025841723053292,
        "abs_return_acf_1": 0.38998386052813666,
        "abs_return_acf_5": 0.25697295582606344,
        "abs_return_acf_20": 0.23132852505083012,
        "quantile_01": -0.05553834027118337,
        "quantile_99": 0.04746391869520077,
        "hill_tail_index": 2.3283679743129766
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019698245645218816,
        "excess_kurtosis": 15.37033473555573,
        "return_acf_1": -0.02187167747449874,
        "abs_return_acf_1": 0.4051512350913995,
        "abs_return_acf_5": 0.34492775029457434,
        "abs_return_acf_20": 0.23613491178501053,
        "quantile_01": -0.047296775188501096,
        "quantile_99": 0.047425484748227636,
        "hill_tail_index": 1.895732129290434
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01850483693346956,
        "excess_kurtosis": 3.5335924415609368,
        "return_acf_1": -0.0903317426095592,
        "abs_return_acf_1": 0.3099039153446112,
        "abs_return_acf_5": 0.21248163504354922,
        "abs_return_acf_20": 0.2392159868106746,
        "quantile_01": -0.059982264795656826,
        "quantile_99": 0.04473882865304673,
        "hill_tail_index": 3.450934842175476
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016303241093563382,
        "excess_kurtosis": 4.86557819649141,
        "return_acf_1": -0.14597070090414954,
        "abs_return_acf_1": 0.23421069592416852,
        "abs_return_acf_5": 0.21824893284334435,
        "abs_return_acf_20": 0.16307189728559798,
        "quantile_01": -0.04719166407630195,
        "quantile_99": 0.03962053556765148,
        "hill_tail_index": 2.729032401540096
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017354642808315168,
        "excess_kurtosis": 3.643384839579271,
        "return_acf_1": -0.1143061985570712,
        "abs_return_acf_1": 0.251580998604576,
        "abs_return_acf_5": 0.26972930028810194,
        "abs_return_acf_20": 0.2476214237295566,
        "quantile_01": -0.05303107842866488,
        "quantile_99": 0.04429058546477599,
        "hill_tail_index": 4.013585477441112
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017490114931300003,
        "excess_kurtosis": 3.4405312569409237,
        "return_acf_1": -0.1541867117414831,
        "abs_return_acf_1": 0.2978454454507255,
        "abs_return_acf_5": 0.24510658507030547,
        "abs_return_acf_20": 0.26393521204676706,
        "quantile_01": -0.05340819993721894,
        "quantile_99": 0.04724354002448547,
        "hill_tail_index": 5.019202439831401
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.015990465855281254,
        "excess_kurtosis": 4.4887462173015695,
        "return_acf_1": -0.1711127097754426,
        "abs_return_acf_1": 0.2941377178739104,
        "abs_return_acf_5": 0.256217758055635,
        "abs_return_acf_20": 0.2438882836895498,
        "quantile_01": -0.04827831253605785,
        "quantile_99": 0.0411351792755036,
        "hill_tail_index": 3.698344361450844
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018646273287309435,
        "excess_kurtosis": 5.099916025587392,
        "return_acf_1": -0.169384246455897,
        "abs_return_acf_1": 0.3422793028436924,
        "abs_return_acf_5": 0.3618592397045526,
        "abs_return_acf_20": 0.29074087406557975,
        "quantile_01": -0.057349159043551624,
        "quantile_99": 0.05321159448085738,
        "hill_tail_index": 3.9247311861678633
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
