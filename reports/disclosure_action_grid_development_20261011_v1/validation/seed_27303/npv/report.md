# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27303
Run ID: `fd78bd18df4ce401a2033d302545f0954b87d09edb21eb5fe3cf0892a93f9ac2`
Result fingerprint: `98771d571b9444e8a6235b30848dcf06aa8aa18330aca085d9578b4e764e2b1c`

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
    "equal_weight_sd": -0.8350119559825445,
    "equal_weight_raw": -12.525179339738168,
    "fixed_start_cap_weight_sd": -0.7994555601395299,
    "fixed_start_cap_weight_raw": -11.991833402092947,
    "end_cap_weight_sd": -0.8209059542789079,
    "end_cap_weight_raw": -12.313589314183622
  },
  "full_period_change": {
    "equal_weight_sd": -1.2358268859735446,
    "equal_weight_raw": -18.53740328960317
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1531283711842126,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11736899639840788,
    "equal_weight_raw": 1.7605349459761186,
    "fixed_start_cap_weight_sd": 0.15292539224142254,
    "fixed_start_cap_weight_raw": 2.2938808836213385,
    "end_cap_weight_sd": 0.1314749981020445,
    "end_cap_weight_raw": 1.972124971530668
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.48120326514689005,
      "change_raw": -7.218048977203351,
      "decay_adjusted_gain_sd": 0.4711776872340623
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8966761122055495,
      "change_raw": -13.450141683083244,
      "decay_adjusted_gain_sd": 0.05570484017540293
    },
    "small": {
      "count": 18,
      "change_sd": -0.8631479930103177,
      "change_raw": -12.947219895154767,
      "decay_adjusted_gain_sd": 0.08923295937063463
    },
    "large_minus_small_sd": 0.3819447278634277,
    "large_minus_small_raw": 5.729170917951415
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.2,
    "final_share": 0.2,
    "initial_wealth_share": 0.18044623542793095,
    "final_wealth_share": 0.17909475346738582
  },
  "pricing_slope": {
    "mean": -0.0010750225557464418,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.0002708087949109963,
    "real_improvement_cost": 0.0002708087949109963,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0002708087949109963,
    "resource_cost_fraction_initial_cap": 9.026959830366545e-06,
    "private_net_outflow_fraction_initial_cap": 9.026959830366545e-06,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 1.5956780995084218e-05,
    "unapplied_final_day_resource_cost": 1.6123373789962613e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 13002.05147735127,
    "beneficial_raw_gain_per_resource_cost": 195030.77216026906,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 2.981802989763932,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.00561251357345614,
    "accrued_cost_fraction_initial_cap": 0.0993934329921311,
    "mean_contract_rate": 0.040222392379243056,
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
    "maximum_relative_cash_error": 2.1384795606515755e-15,
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
      "minimum": -0.23563182018769366,
      "maximum": -0.008288318573512013,
      "mean": -0.11847431452791454,
      "median": -0.12068037382905805,
      "quantile_05": -0.2066250003279048,
      "quantile_95": -0.01779782544553085
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
      "minimum": 0.2453315610404868,
      "maximum": 0.7368528146004141,
      "mean": 0.45455254516896554,
      "median": 0.4323662885970192,
      "quantile_05": 0.2967719278457713,
      "quantile_95": 0.6671402650885817
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
        "daily_volatility": 0.018158875074429946,
        "excess_kurtosis": 3.0136148639490337,
        "return_acf_1": -0.15123037301649972,
        "abs_return_acf_1": 0.29294526760768347,
        "abs_return_acf_5": 0.34325044608912025,
        "abs_return_acf_20": 0.26765230764101666,
        "quantile_01": -0.050074140524031654,
        "quantile_99": 0.05581767742797077,
        "hill_tail_index": 4.863204501764479
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01922830321392241,
        "excess_kurtosis": 7.76296662658644,
        "return_acf_1": -0.21530804868799003,
        "abs_return_acf_1": 0.3635596930445135,
        "abs_return_acf_5": 0.34188352561559987,
        "abs_return_acf_20": 0.35893442687288657,
        "quantile_01": -0.05944052985464865,
        "quantile_99": 0.05651493277592221,
        "hill_tail_index": 3.161172025405535
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018155774230776835,
        "excess_kurtosis": 4.984521886698552,
        "return_acf_1": -0.1824898883286394,
        "abs_return_acf_1": 0.32769851351965534,
        "abs_return_acf_5": 0.26178831858718354,
        "abs_return_acf_20": 0.26150862591879953,
        "quantile_01": -0.05583974658988286,
        "quantile_99": 0.048876312701261304,
        "hill_tail_index": 3.796225719738366
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016952997750809867,
        "excess_kurtosis": 4.601458193337721,
        "return_acf_1": -0.12374322444813192,
        "abs_return_acf_1": 0.24593053471402282,
        "abs_return_acf_5": 0.30931597346400885,
        "abs_return_acf_20": 0.2310642734321818,
        "quantile_01": -0.04691529936402477,
        "quantile_99": 0.04981085565123562,
        "hill_tail_index": 3.3591983450043053
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01775581116866658,
        "excess_kurtosis": 5.832391597652759,
        "return_acf_1": -0.15786495699438002,
        "abs_return_acf_1": 0.2929908283543665,
        "abs_return_acf_5": 0.32733089105229224,
        "abs_return_acf_20": 0.2784899740764668,
        "quantile_01": -0.054739882801500585,
        "quantile_99": 0.052656861779185854,
        "hill_tail_index": 3.537045473210678
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01839096585485849,
        "excess_kurtosis": 5.093420195061022,
        "return_acf_1": -0.1516220131577376,
        "abs_return_acf_1": 0.340317163169949,
        "abs_return_acf_5": 0.30691118644617776,
        "abs_return_acf_20": 0.2801848470866741,
        "quantile_01": -0.05247125942845211,
        "quantile_99": 0.04566391953280063,
        "hill_tail_index": 2.96975375713113
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.015952995245045242,
        "excess_kurtosis": 5.642149622017852,
        "return_acf_1": -0.10560937141630171,
        "abs_return_acf_1": 0.3162373976402629,
        "abs_return_acf_5": 0.3287915449169162,
        "abs_return_acf_20": 0.31388886161898705,
        "quantile_01": -0.03757599836216232,
        "quantile_99": 0.04738907496711823,
        "hill_tail_index": 2.7994256147399685
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017291183472907364,
        "excess_kurtosis": 3.3749118634356865,
        "return_acf_1": -0.14776563988803146,
        "abs_return_acf_1": 0.2970328618336473,
        "abs_return_acf_5": 0.24133581176117144,
        "abs_return_acf_20": 0.20040460497633739,
        "quantile_01": -0.04541484027725967,
        "quantile_99": 0.04181357086516901,
        "hill_tail_index": 3.043192244524395
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01778167132763761,
        "excess_kurtosis": 5.701908636098217,
        "return_acf_1": -0.1724644009627091,
        "abs_return_acf_1": 0.30606790605395595,
        "abs_return_acf_5": 0.24463798683635982,
        "abs_return_acf_20": 0.2385129647739549,
        "quantile_01": -0.04911719144153585,
        "quantile_99": 0.052423470013314585,
        "hill_tail_index": 3.5618865882305273
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01817626768487517,
        "excess_kurtosis": 6.515539498129597,
        "return_acf_1": -0.10763469481799752,
        "abs_return_acf_1": 0.20730732102470484,
        "abs_return_acf_5": 0.2678413243405145,
        "abs_return_acf_20": 0.26357134481511124,
        "quantile_01": -0.05348173375323934,
        "quantile_99": 0.05005557833076575,
        "hill_tail_index": 3.214252019208247
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017679257234491316,
        "excess_kurtosis": 2.242760244504675,
        "return_acf_1": -0.10748389372946397,
        "abs_return_acf_1": 0.2898549871451564,
        "abs_return_acf_5": 0.2513434615230942,
        "abs_return_acf_20": 0.1959562900389921,
        "quantile_01": -0.048600737024847566,
        "quantile_99": 0.04749284039148229,
        "hill_tail_index": 4.1467347280694895
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015139378458934321,
        "excess_kurtosis": 4.120508449936791,
        "return_acf_1": -0.008288318573512013,
        "abs_return_acf_1": 0.2951756765748602,
        "abs_return_acf_5": 0.29680099092387613,
        "abs_return_acf_20": 0.2614969661822612,
        "quantile_01": -0.0452547493814838,
        "quantile_99": 0.04081875423788407,
        "hill_tail_index": 4.0032934109417475
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01906316197006348,
        "excess_kurtosis": 3.4539841574087493,
        "return_acf_1": -0.13569194404967508,
        "abs_return_acf_1": 0.2952537475202257,
        "abs_return_acf_5": 0.3371554330473272,
        "abs_return_acf_20": 0.34285322877703717,
        "quantile_01": -0.057218183047118044,
        "quantile_99": 0.052249525509371314,
        "hill_tail_index": 6.048205755904103
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01848518483565556,
        "excess_kurtosis": 5.104833188686314,
        "return_acf_1": -0.10721133260746027,
        "abs_return_acf_1": 0.33819251184923455,
        "abs_return_acf_5": 0.2982794896366777,
        "abs_return_acf_20": 0.2773818201059615,
        "quantile_01": -0.05213613884516711,
        "quantile_99": 0.05510780919398171,
        "hill_tail_index": 4.621632111749247
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020405868332628665,
        "excess_kurtosis": 6.924681817788718,
        "return_acf_1": -0.10690639871263154,
        "abs_return_acf_1": 0.4225274612094795,
        "abs_return_acf_5": 0.4913613632341752,
        "abs_return_acf_20": 0.3635979605649257,
        "quantile_01": -0.06762881229149593,
        "quantile_99": 0.06370889154602381,
        "hill_tail_index": 3.982630221629856
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018637228663677275,
        "excess_kurtosis": 12.929500751173748,
        "return_acf_1": -0.03696672035133078,
        "abs_return_acf_1": 0.4109867241142167,
        "abs_return_acf_5": 0.42153760613446156,
        "abs_return_acf_20": 0.349184352661082,
        "quantile_01": -0.05558083395852467,
        "quantile_99": 0.05416343420618169,
        "hill_tail_index": 2.9669852578677642
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01927185145424814,
        "excess_kurtosis": 9.295873474999976,
        "return_acf_1": -0.19601238566557838,
        "abs_return_acf_1": 0.3856002836028634,
        "abs_return_acf_5": 0.39583129237212883,
        "abs_return_acf_20": 0.25728363262377035,
        "quantile_01": -0.057156281096910476,
        "quantile_99": 0.06570427762725292,
        "hill_tail_index": 3.180494893892601
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01937219495148996,
        "excess_kurtosis": 7.75988690313612,
        "return_acf_1": -0.23563182018769366,
        "abs_return_acf_1": 0.3828196444469619,
        "abs_return_acf_5": 0.3310840969414392,
        "abs_return_acf_20": 0.27689829051149256,
        "quantile_01": -0.06408269173492355,
        "quantile_99": 0.05319324376236429,
        "hill_tail_index": 3.08127823790126
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017286596638709417,
        "excess_kurtosis": 19.883414018195637,
        "return_acf_1": -0.11802055887051109,
        "abs_return_acf_1": 0.3105061021302441,
        "abs_return_acf_5": 0.3658017308592123,
        "abs_return_acf_20": 0.25794843266779494,
        "quantile_01": -0.044053658872635654,
        "quantile_99": 0.047171702222773254,
        "hill_tail_index": 2.957845997071122
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019480040502157934,
        "excess_kurtosis": 5.954507089139188,
        "return_acf_1": -0.05728432635237669,
        "abs_return_acf_1": 0.31690586912388286,
        "abs_return_acf_5": 0.32032174619246556,
        "abs_return_acf_20": 0.23742912453550064,
        "quantile_01": -0.06315369693662241,
        "quantile_99": 0.06518303922807808,
        "hill_tail_index": 3.3648690329736692
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018873879698762017,
        "excess_kurtosis": 8.859550932015718,
        "return_acf_1": -0.12973834528651162,
        "abs_return_acf_1": 0.3609967084863876,
        "abs_return_acf_5": 0.33012992383100637,
        "abs_return_acf_20": 0.33095186883567823,
        "quantile_01": -0.05230985032410471,
        "quantile_99": 0.054443659132154675,
        "hill_tail_index": 2.9217501848530842
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018256495999441163,
        "excess_kurtosis": 8.095565914360158,
        "return_acf_1": -0.1247675330209303,
        "abs_return_acf_1": 0.356461012566509,
        "abs_return_acf_5": 0.3849980115208348,
        "abs_return_acf_20": 0.34892547257601,
        "quantile_01": -0.05912291281001337,
        "quantile_99": 0.045986993652863684,
        "hill_tail_index": 2.8995647399972073
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018493661563406674,
        "excess_kurtosis": 5.310396766486953,
        "return_acf_1": -0.0802327894952201,
        "abs_return_acf_1": 0.323550166705907,
        "abs_return_acf_5": 0.30688134755816804,
        "abs_return_acf_20": 0.22233139775709543,
        "quantile_01": -0.05742662302828258,
        "quantile_99": 0.05974042746336843,
        "hill_tail_index": 4.740540739413663
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018126073925036828,
        "excess_kurtosis": 4.294597439512487,
        "return_acf_1": -0.16152658660305447,
        "abs_return_acf_1": 0.3601714719713684,
        "abs_return_acf_5": 0.3432045241247276,
        "abs_return_acf_20": 0.2923979113001059,
        "quantile_01": -0.052377921858204377,
        "quantile_99": 0.050344814970132885,
        "hill_tail_index": 3.7207452566593924
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01853163723908705,
        "excess_kurtosis": 4.7470142149834915,
        "return_acf_1": -0.022188428501022005,
        "abs_return_acf_1": 0.27551623926586477,
        "abs_return_acf_5": 0.33019250917584103,
        "abs_return_acf_20": 0.26501417784357967,
        "quantile_01": -0.05302012511976568,
        "quantile_99": 0.05466473896172689,
        "hill_tail_index": 3.136291933108266
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017344680130758416,
        "excess_kurtosis": 14.0942877903848,
        "return_acf_1": -0.01420551385467441,
        "abs_return_acf_1": 0.3716665438497416,
        "abs_return_acf_5": 0.38231196652095795,
        "abs_return_acf_20": 0.3243838137752757,
        "quantile_01": -0.048069119568579705,
        "quantile_99": 0.04248400448213685,
        "hill_tail_index": 1.8571597779614069
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01886578904217238,
        "excess_kurtosis": 4.975484444305264,
        "return_acf_1": -0.09568782593264123,
        "abs_return_acf_1": 0.37595791119731,
        "abs_return_acf_5": 0.3035293440157852,
        "abs_return_acf_20": 0.3287772148682576,
        "quantile_01": -0.056365225964358584,
        "quantile_99": 0.05793948883454252,
        "hill_tail_index": 3.316480970261658
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018962721956811163,
        "excess_kurtosis": 3.9523305818086785,
        "return_acf_1": -0.08191397347174713,
        "abs_return_acf_1": 0.2326502555264669,
        "abs_return_acf_5": 0.2629855614395324,
        "abs_return_acf_20": 0.27093279698791506,
        "quantile_01": -0.05986250352719883,
        "quantile_99": 0.0600620597922108,
        "hill_tail_index": 5.182936650426779
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017947593016053597,
        "excess_kurtosis": 3.505218167642088,
        "return_acf_1": -0.12334018878760503,
        "abs_return_acf_1": 0.2458798998981961,
        "abs_return_acf_5": 0.3179943716120906,
        "abs_return_acf_20": 0.22983925574148736,
        "quantile_01": -0.051233313138272875,
        "quantile_99": 0.04618274537802703,
        "hill_tail_index": 4.863145721370743
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019401449161758066,
        "excess_kurtosis": 5.233651003444606,
        "return_acf_1": -0.09539794006537804,
        "abs_return_acf_1": 0.39375352869269503,
        "abs_return_acf_5": 0.37542071393485354,
        "abs_return_acf_20": 0.3177038993043998,
        "quantile_01": -0.06354281403920474,
        "quantile_99": 0.05901649141011603,
        "hill_tail_index": 4.0063247936990125
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
