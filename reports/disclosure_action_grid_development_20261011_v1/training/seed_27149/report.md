# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27149
Run ID: `1cf41764c31cfb89eae5d0ab02963379bbc98761ce12c5212a28cd148fd1c110`
Result fingerprint: `4a712e3334f2fa49da1d6e4c9ae2e5f2762eadfdd8dd888ef934628ab6502031`

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
    "equal_weight_sd": -0.7576309523809489,
    "equal_weight_raw": -11.364464285714236,
    "fixed_start_cap_weight_sd": -0.7108589637397571,
    "fixed_start_cap_weight_raw": -10.662884456096357,
    "end_cap_weight_sd": -0.7152851704165994,
    "end_cap_weight_raw": -10.729277556248993
  },
  "full_period_change": {
    "equal_weight_sd": -1.1369047619047572,
    "equal_weight_raw": -17.05357142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0494652777777733,
    "inflation_mean_sd": 0.6547275132275132
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19475000000000317,
    "equal_weight_raw": 2.921250000000047,
    "fixed_start_cap_weight_sd": 0.24152198864119515,
    "fixed_start_cap_weight_raw": 3.6228298296179275,
    "end_cap_weight_sd": 0.23709578196435271,
    "end_cap_weight_raw": 3.556436729465291
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7523809523809492,
      "change_raw": -11.285714285714237,
      "decay_adjusted_gain_sd": 0.20000000000000315
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7243253968253937,
      "change_raw": -10.864880952380904,
      "decay_adjusted_gain_sd": 0.22805555555555873
    },
    "small": {
      "count": 18,
      "change_sd": -0.7751587301587269,
      "change_raw": -11.627380952380904,
      "decay_adjusted_gain_sd": 0.1772222222222254
    },
    "large_minus_small_sd": 0.022777777777777786,
    "large_minus_small_raw": 0.3416666666666668
  },
  "inflation": {
    "initial_mean_sd": 0.3625,
    "final_mean_sd": 0.6718333333333333,
    "mean_sd": 0.5525938107132945,
    "mean_absolute_raw_gap": 8.288907160699418,
    "final_absolute_raw_gap": 10.077499999999999,
    "mean_range_fraction": 0.08288907160699419
  },
  "impact": {
    "initial_share": 0.16,
    "final_share": 0.25333333333333335,
    "initial_wealth_share": 0.20756476833399679,
    "final_wealth_share": 0.26943970646383053
  },
  "pricing_slope": {
    "mean": -0.0015144448808568837,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.09735808007484054,
    "real_improvement_cost": 0.08014716499078389,
    "washing_cost": 0.01721091508405664,
    "fine_transfer": 0.04032853584002678,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1376866159148673,
    "resource_cost_fraction_initial_cap": 0.0032452693358280167,
    "private_net_outflow_fraction_initial_cap": 0.004589553863828908,
    "fine_transfer_fraction_initial_cap": 0.0013442845280008922,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.021823082039217186,
    "unapplied_final_day_resource_cost": 0.003919158942557342
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 60.010427439703854,
    "beneficial_raw_gain_per_resource_cost": 900.1564115955578,
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
    "fixed_exposure": 15.000000000000005,
    "accrued_cost": 2.5414791178776084,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.4347113583128688,
    "accrued_cost_fraction_initial_cap": 0.08471597059592025,
    "mean_contract_rate": 0.036766261463241294,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 3.558251915546058e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.20947477773877218,
      "maximum": -0.04673869556789487,
      "mean": -0.13301553924514203,
      "median": -0.1391551076872921,
      "quantile_05": -0.18177060502392367,
      "quantile_95": -0.07579404407937539
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
      "minimum": 0.2649569587754697,
      "maximum": 0.8275023344661838,
      "mean": 0.5559693381961724,
      "median": 0.5829200784371589,
      "quantile_05": 0.33529445774898403,
      "quantile_95": 0.7317317393622319
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
        "daily_volatility": 0.021642277385520294,
        "excess_kurtosis": 14.21698254507653,
        "return_acf_1": -0.17387438231638647,
        "abs_return_acf_1": 0.4317312579708609,
        "abs_return_acf_5": 0.3825724613597873,
        "abs_return_acf_20": 0.31833963561363526,
        "quantile_01": -0.06497789723450322,
        "quantile_99": 0.058645717609747745,
        "hill_tail_index": 2.5322303644659945
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020025389548053156,
        "excess_kurtosis": 11.635731725457282,
        "return_acf_1": -0.11395261861930261,
        "abs_return_acf_1": 0.28467235717056494,
        "abs_return_acf_5": 0.27941531813080595,
        "abs_return_acf_20": 0.19471120440699352,
        "quantile_01": -0.056101880672634684,
        "quantile_99": 0.05083295918947432,
        "hill_tail_index": 2.7376215379807602
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020247048537601012,
        "excess_kurtosis": 8.115794933761741,
        "return_acf_1": -0.1480949163642643,
        "abs_return_acf_1": 0.3198363835338412,
        "abs_return_acf_5": 0.38989049791063013,
        "abs_return_acf_20": 0.2304873932153525,
        "quantile_01": -0.06791332364413072,
        "quantile_99": 0.061399425434574724,
        "hill_tail_index": 3.5718125192629104
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021645418500248745,
        "excess_kurtosis": 9.041846366514575,
        "return_acf_1": -0.13174988931363726,
        "abs_return_acf_1": 0.39913368830921064,
        "abs_return_acf_5": 0.43445788169853605,
        "abs_return_acf_20": 0.29050678267691127,
        "quantile_01": -0.07232159575614397,
        "quantile_99": 0.05476882725171119,
        "hill_tail_index": 2.7957354240771153
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016961870343930017,
        "excess_kurtosis": 2.868624740930369,
        "return_acf_1": -0.14950492779826596,
        "abs_return_acf_1": 0.29648264104107386,
        "abs_return_acf_5": 0.25546150823387853,
        "abs_return_acf_20": 0.1672585873139441,
        "quantile_01": -0.05266390436158621,
        "quantile_99": 0.04374834918052104,
        "hill_tail_index": 4.160744473031407
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02085942555914776,
        "excess_kurtosis": 11.592478187951578,
        "return_acf_1": -0.15252702863447146,
        "abs_return_acf_1": 0.427155791445628,
        "abs_return_acf_5": 0.36423441007452756,
        "abs_return_acf_20": 0.3243061004966175,
        "quantile_01": -0.05932075133150519,
        "quantile_99": 0.06521471583827944,
        "hill_tail_index": 3.144053434893427
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01749939753237364,
        "excess_kurtosis": 5.757908307303026,
        "return_acf_1": -0.04673869556789487,
        "abs_return_acf_1": 0.2413156574799383,
        "abs_return_acf_5": 0.24269964663622676,
        "abs_return_acf_20": 0.21541563724163967,
        "quantile_01": -0.05423994935276394,
        "quantile_99": 0.05212398296642989,
        "hill_tail_index": 3.0234398697958693
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020361777331182846,
        "excess_kurtosis": 14.345884683055896,
        "return_acf_1": -0.20947477773877218,
        "abs_return_acf_1": 0.4958643414034918,
        "abs_return_acf_5": 0.37335419977087725,
        "abs_return_acf_20": 0.24584037074645843,
        "quantile_01": -0.055686120675722414,
        "quantile_99": 0.05401047491082025,
        "hill_tail_index": 2.3766848605645015
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019549723932737555,
        "excess_kurtosis": 8.83352232563495,
        "return_acf_1": -0.13922363552589084,
        "abs_return_acf_1": 0.34868376505132787,
        "abs_return_acf_5": 0.30838390473571375,
        "abs_return_acf_20": 0.27756224046905453,
        "quantile_01": -0.06757712463302537,
        "quantile_99": 0.05154981744940103,
        "hill_tail_index": 2.828529697067193
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017764890814671204,
        "excess_kurtosis": 4.3917283251735455,
        "return_acf_1": -0.1297068789859323,
        "abs_return_acf_1": 0.27656479474523954,
        "abs_return_acf_5": 0.24240201657405205,
        "abs_return_acf_20": 0.2732778211196579,
        "quantile_01": -0.05289380899662869,
        "quantile_99": 0.0443223217660434,
        "hill_tail_index": 3.2500605641242926
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020358368294592016,
        "excess_kurtosis": 9.585061539541362,
        "return_acf_1": -0.08785952451330743,
        "abs_return_acf_1": 0.32113932525881705,
        "abs_return_acf_5": 0.28286611258162825,
        "abs_return_acf_20": 0.1769047014130875,
        "quantile_01": -0.06421524287209812,
        "quantile_99": 0.05502215446087739,
        "hill_tail_index": 2.788410188190771
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01943308065054773,
        "excess_kurtosis": 6.940909215219962,
        "return_acf_1": -0.14570832246343896,
        "abs_return_acf_1": 0.38163319667301066,
        "abs_return_acf_5": 0.37432448317507433,
        "abs_return_acf_20": 0.2893806528616638,
        "quantile_01": -0.06635262537286524,
        "quantile_99": 0.055226989341866144,
        "hill_tail_index": 2.8149094496825042
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02179567776685194,
        "excess_kurtosis": 11.794695237372055,
        "return_acf_1": -0.08148159763248501,
        "abs_return_acf_1": 0.406298698209958,
        "abs_return_acf_5": 0.39826191675985195,
        "abs_return_acf_20": 0.26495408362447526,
        "quantile_01": -0.07741061819626364,
        "quantile_99": 0.05521011512493278,
        "hill_tail_index": 2.773621434518337
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021973444472094417,
        "excess_kurtosis": 9.220075640230734,
        "return_acf_1": -0.15257118504574546,
        "abs_return_acf_1": 0.3961746660704776,
        "abs_return_acf_5": 0.4572938565997195,
        "abs_return_acf_20": 0.21744071365866227,
        "quantile_01": -0.07417740015318751,
        "quantile_99": 0.05820530873814848,
        "hill_tail_index": 3.4235526972103876
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01871990933381651,
        "excess_kurtosis": 8.563385368859418,
        "return_acf_1": -0.1422386538631105,
        "abs_return_acf_1": 0.24922919017492473,
        "abs_return_acf_5": 0.33316996300209883,
        "abs_return_acf_20": 0.1628817023143174,
        "quantile_01": -0.06143103161493103,
        "quantile_99": 0.04995264881628153,
        "hill_tail_index": 3.7915529682012443
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023012958051736337,
        "excess_kurtosis": 14.946624948558735,
        "return_acf_1": -0.13908657984869338,
        "abs_return_acf_1": 0.3736808038059377,
        "abs_return_acf_5": 0.41089437481135493,
        "abs_return_acf_20": 0.24897782839809973,
        "quantile_01": -0.07814128779657714,
        "quantile_99": 0.061530407646022675,
        "hill_tail_index": 2.4611671810047504
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02190704074328876,
        "excess_kurtosis": 10.986230723548925,
        "return_acf_1": -0.10298969592918052,
        "abs_return_acf_1": 0.36981330630822123,
        "abs_return_acf_5": 0.36643713469868167,
        "abs_return_acf_20": 0.18947943583773336,
        "quantile_01": -0.075166519173314,
        "quantile_99": 0.05869362152672291,
        "hill_tail_index": 2.7198373096423025
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018434481108565083,
        "excess_kurtosis": 12.763130106388381,
        "return_acf_1": -0.11951774652038281,
        "abs_return_acf_1": 0.35875804632039837,
        "abs_return_acf_5": 0.3038617286700833,
        "abs_return_acf_20": 0.3053051706434071,
        "quantile_01": -0.05788461528974615,
        "quantile_99": 0.050194170406068286,
        "hill_tail_index": 2.1980181209464265
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019282598427942055,
        "excess_kurtosis": 4.628646424930636,
        "return_acf_1": -0.13504174519601145,
        "abs_return_acf_1": 0.3347419832401573,
        "abs_return_acf_5": 0.2803294676034301,
        "abs_return_acf_20": 0.2087633853584514,
        "quantile_01": -0.056888075107490735,
        "quantile_99": 0.0470191406130249,
        "hill_tail_index": 3.078070214092572
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02336908806056875,
        "excess_kurtosis": 11.396338615164456,
        "return_acf_1": -0.12475261589635614,
        "abs_return_acf_1": 0.45778366658343667,
        "abs_return_acf_5": 0.4290884642566769,
        "abs_return_acf_20": 0.3103738897553876,
        "quantile_01": -0.08371044435288809,
        "quantile_99": 0.06495586812103782,
        "hill_tail_index": 2.8559055851123167
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023864167252532785,
        "excess_kurtosis": 13.11702404969024,
        "return_acf_1": -0.087375752458064,
        "abs_return_acf_1": 0.4411032884656714,
        "abs_return_acf_5": 0.4579462013265858,
        "abs_return_acf_20": 0.26790977252607306,
        "quantile_01": -0.08312364190067255,
        "quantile_99": 0.06455478078868752,
        "hill_tail_index": 2.522651863411528
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024701215875578192,
        "excess_kurtosis": 15.85084362480196,
        "return_acf_1": -0.16744160165794153,
        "abs_return_acf_1": 0.4680019643646257,
        "abs_return_acf_5": 0.47955806220002545,
        "abs_return_acf_20": 0.288171032825533,
        "quantile_01": -0.09092162067909594,
        "quantile_99": 0.06944720407510989,
        "hill_tail_index": 2.9364843162570113
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020200118656918113,
        "excess_kurtosis": 6.7881643419921325,
        "return_acf_1": -0.11022030458027583,
        "abs_return_acf_1": 0.39856841320235054,
        "abs_return_acf_5": 0.2888524313871487,
        "abs_return_acf_20": 0.1606760761794577,
        "quantile_01": -0.07038860530079477,
        "quantile_99": 0.05089541291873237,
        "hill_tail_index": 2.9464204904944378
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020166148644566867,
        "excess_kurtosis": 9.569325805914486,
        "return_acf_1": -0.11240789263622193,
        "abs_return_acf_1": 0.2645207644847073,
        "abs_return_acf_5": 0.33612170897820315,
        "abs_return_acf_20": 0.12886798448084075,
        "quantile_01": -0.06920022076525993,
        "quantile_99": 0.05613476410582129,
        "hill_tail_index": 3.053245660059767
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023440947176964537,
        "excess_kurtosis": 14.178822498238638,
        "return_acf_1": -0.1747747074638293,
        "abs_return_acf_1": 0.423584181905829,
        "abs_return_acf_5": 0.4862547683221673,
        "abs_return_acf_20": 0.3163014204084031,
        "quantile_01": -0.07697713894000895,
        "quantile_99": 0.061882735978907685,
        "hill_tail_index": 2.5001232383746728
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021924224153808167,
        "excess_kurtosis": 11.815188429594182,
        "return_acf_1": -0.07114059117228563,
        "abs_return_acf_1": 0.36616145869503514,
        "abs_return_acf_5": 0.4329758830885029,
        "abs_return_acf_20": 0.1891164278919623,
        "quantile_01": -0.07269095998782946,
        "quantile_99": 0.054791906983696397,
        "hill_tail_index": 2.7057526168517936
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020502901847532624,
        "excess_kurtosis": 10.21390880866731,
        "return_acf_1": -0.18749452120945542,
        "abs_return_acf_1": 0.43296682430152333,
        "abs_return_acf_5": 0.3505886321928798,
        "abs_return_acf_20": 0.22679908209312857,
        "quantile_01": -0.0747034539836722,
        "quantile_99": 0.056035636247587936,
        "hill_tail_index": 2.9311161081403996
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017693994020238597,
        "excess_kurtosis": 8.359550734981674,
        "return_acf_1": -0.14755582870895656,
        "abs_return_acf_1": 0.24425293046349544,
        "abs_return_acf_5": 0.3308530316430548,
        "abs_return_acf_20": 0.2149844416649532,
        "quantile_01": -0.05644119877894044,
        "quantile_99": 0.04898920171275527,
        "hill_tail_index": 2.8877812221231167
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021479518554531403,
        "excess_kurtosis": 18.728510467036756,
        "return_acf_1": -0.14477759438490762,
        "abs_return_acf_1": 0.32908031033265156,
        "abs_return_acf_5": 0.4000419018778808,
        "abs_return_acf_20": 0.20186277451604204,
        "quantile_01": -0.05980586052465447,
        "quantile_99": 0.05533041980109276,
        "hill_tail_index": 3.274405411295053
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01979724699657997,
        "excess_kurtosis": 8.838859802431392,
        "return_acf_1": -0.16118196530879292,
        "abs_return_acf_1": 0.3899747486234928,
        "abs_return_acf_5": 0.39980996777361916,
        "abs_return_acf_20": 0.18664227087289417,
        "quantile_01": -0.06919379324929266,
        "quantile_99": 0.05900918734857355,
        "hill_tail_index": 3.8645311939312825
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
