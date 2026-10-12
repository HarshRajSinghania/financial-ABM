# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27009
Run ID: `33353bf6755580811d2a1335f10a69eb2fe58fd3cd07aef5160d111789d9521f`
Result fingerprint: `d82e144c78b873dcf8794649e75adcd0f6fd736ec56a311ce26a14e605011ab8`

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
    "equal_weight_sd": -0.5036393366156557,
    "equal_weight_raw": -7.554590049234836,
    "fixed_start_cap_weight_sd": -0.5265623314711676,
    "fixed_start_cap_weight_raw": -7.898434972067514,
    "end_cap_weight_sd": -0.5193089621495783,
    "end_cap_weight_raw": -7.789634432243676
  },
  "full_period_change": {
    "equal_weight_sd": -0.7594131461394638,
    "equal_weight_raw": -11.391197192091957
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.714227283831578,
    "inflation_mean_sd": 0.5665201719576719
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.43657936507936823,
    "equal_weight_raw": 6.5486904761905205,
    "fixed_start_cap_weight_sd": 0.3711509790197104,
    "fixed_start_cap_weight_raw": 5.567264685295658,
    "end_cap_weight_sd": 0.3767259571597585,
    "end_cap_weight_raw": 5.650889357396378
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5441314613946816,
      "change_raw": -8.161971920920225,
      "decay_adjusted_gain_sd": 0.28662698412698634
    },
    "mid": {
      "count": 9,
      "change_sd": -0.532658730158727,
      "change_raw": -7.989880952380905,
      "decay_adjusted_gain_sd": 0.41972222222222527
    },
    "small": {
      "count": 18,
      "change_sd": -0.48238095238094914,
      "change_raw": -7.235714285714237,
      "decay_adjusted_gain_sd": 0.4700000000000032
    },
    "large_minus_small_sd": -0.06175050901373247,
    "large_minus_small_raw": -0.926257635205987
  },
  "inflation": {
    "initial_mean_sd": 0.23241666666666666,
    "final_mean_sd": 0.6214166666666667,
    "mean_sd": 0.4278807243963364,
    "mean_absolute_raw_gap": 6.4182108659450465,
    "final_absolute_raw_gap": 9.321249999999997,
    "mean_range_fraction": 0.06418210865945047
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.32,
    "initial_wealth_share": 0.2853332793293715,
    "final_wealth_share": 0.3226175037291152
  },
  "pricing_slope": {
    "mean": -0.0027057669498304956,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.29753557835260513,
    "real_improvement_cost": 0.2506268449695204,
    "washing_cost": 0.0469087333830847,
    "fine_transfer": 0.020959113037778126,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3184946913903833,
    "resource_cost_fraction_initial_cap": 0.009917852611753503,
    "private_net_outflow_fraction_initial_cap": 0.010616489713012775,
    "fine_transfer_fraction_initial_cap": 0.0006986371012592708,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008642713429844023,
    "unapplied_final_day_resource_cost": 0.027707385972749826
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 44.01954557804018,
    "beneficial_raw_gain_per_resource_cost": 660.2931836706026,
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
    "accrued_cost": 2.6639498017239465,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.31224067446653,
    "accrued_cost_fraction_initial_cap": 0.08879832672413154,
    "mean_contract_rate": 0.03776967300636184,
    "maximum_ledger_error": 4.404571325722362e-20
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
    "maximum_relative_cash_error": 3.152513122552771e-15,
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
      "minimum": -0.2027977307002209,
      "maximum": -0.03309332190130161,
      "mean": -0.08721074328655018,
      "median": -0.08045633517896167,
      "quantile_05": -0.164122355400809,
      "quantile_95": -0.03546293490410879
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
      "minimum": 0.2759283974541285,
      "maximum": 0.7523062311608726,
      "mean": 0.45650298432731273,
      "median": 0.4180180873823312,
      "quantile_05": 0.3080088781052006,
      "quantile_95": 0.6702666664720952
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
        "daily_volatility": 0.018439960343494596,
        "excess_kurtosis": 16.73929623748534,
        "return_acf_1": -0.04808049458247375,
        "abs_return_acf_1": 0.4257685118114511,
        "abs_return_acf_5": 0.36006747396509636,
        "abs_return_acf_20": 0.3799697137952706,
        "quantile_01": -0.05495222208633675,
        "quantile_99": 0.048307007440281505,
        "hill_tail_index": 2.3122785262190098
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.015510006228288811,
        "excess_kurtosis": 6.060349848609091,
        "return_acf_1": -0.0729013532929157,
        "abs_return_acf_1": 0.42263962722896103,
        "abs_return_acf_5": 0.3322503356239505,
        "abs_return_acf_20": 0.2872193815882597,
        "quantile_01": -0.05003699833027922,
        "quantile_99": 0.038086487177632126,
        "hill_tail_index": 3.0130548045469157
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016650075699337782,
        "excess_kurtosis": 8.0954599865751,
        "return_acf_1": -0.0919318503735401,
        "abs_return_acf_1": 0.38458037505085213,
        "abs_return_acf_5": 0.2636430697485084,
        "abs_return_acf_20": 0.22044920800022205,
        "quantile_01": -0.04792216904082119,
        "quantile_99": 0.0420845554179307,
        "hill_tail_index": 2.9476445240022286
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018425551768951977,
        "excess_kurtosis": 5.993587515912644,
        "return_acf_1": -0.09665716488084934,
        "abs_return_acf_1": 0.3075968550413318,
        "abs_return_acf_5": 0.22802961029794883,
        "abs_return_acf_20": 0.29052119994492887,
        "quantile_01": -0.05939476791378091,
        "quantile_99": 0.04860732349575292,
        "hill_tail_index": 3.30204747602158
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.015173180368010145,
        "excess_kurtosis": 5.126316924013599,
        "return_acf_1": -0.037870315592006536,
        "abs_return_acf_1": 0.2249374392750126,
        "abs_return_acf_5": 0.2311974209476362,
        "abs_return_acf_20": 0.12160351912044981,
        "quantile_01": -0.03642427000498488,
        "quantile_99": 0.04581819574057049,
        "hill_tail_index": 2.7916623024150784
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015997980076583637,
        "excess_kurtosis": 6.776531148644722,
        "return_acf_1": -0.06332305231279241,
        "abs_return_acf_1": 0.328227328217203,
        "abs_return_acf_5": 0.2597716038428639,
        "abs_return_acf_20": 0.24325291908041707,
        "quantile_01": -0.04789882709591733,
        "quantile_99": 0.04220024416474364,
        "hill_tail_index": 2.7002300028734885
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018751683274880568,
        "excess_kurtosis": 11.68297860140529,
        "return_acf_1": -0.10835216916529034,
        "abs_return_acf_1": 0.4053787333774838,
        "abs_return_acf_5": 0.35480209263102247,
        "abs_return_acf_20": 0.348416344122701,
        "quantile_01": -0.058543342304348656,
        "quantile_99": 0.052206425092778126,
        "hill_tail_index": 2.7517727644842083
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.016598481136756604,
        "excess_kurtosis": 4.340701251354004,
        "return_acf_1": -0.054429988646567395,
        "abs_return_acf_1": 0.3579085386917759,
        "abs_return_acf_5": 0.33317837446532783,
        "abs_return_acf_20": 0.2339527585555264,
        "quantile_01": -0.0553283168216182,
        "quantile_99": 0.050794338203051,
        "hill_tail_index": 3.656974475508296
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.014566570363592126,
        "excess_kurtosis": 3.9972971549841043,
        "return_acf_1": -0.06458325445261347,
        "abs_return_acf_1": 0.24242747276137377,
        "abs_return_acf_5": 0.26274841064204735,
        "abs_return_acf_20": 0.19643319714224958,
        "quantile_01": -0.04254795991681738,
        "quantile_99": 0.034838739181073636,
        "hill_tail_index": 3.3277979725876916
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01602256814865542,
        "excess_kurtosis": 5.422779995458001,
        "return_acf_1": -0.0972621938075507,
        "abs_return_acf_1": 0.33156687927307504,
        "abs_return_acf_5": 0.25848265665423215,
        "abs_return_acf_20": 0.2652484859862606,
        "quantile_01": -0.044556314438251456,
        "quantile_99": 0.042460455045456674,
        "hill_tail_index": 3.7961006822899948
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01806021401125536,
        "excess_kurtosis": 7.022995070662885,
        "return_acf_1": -0.1659024871767908,
        "abs_return_acf_1": 0.4157319155765019,
        "abs_return_acf_5": 0.3823838707114723,
        "abs_return_acf_20": 0.2720371835611094,
        "quantile_01": -0.05076711448960304,
        "quantile_99": 0.0488247662648452,
        "hill_tail_index": 3.1124587812074584
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019211005600654103,
        "excess_kurtosis": 10.393073912802926,
        "return_acf_1": -0.2027977307002209,
        "abs_return_acf_1": 0.3615420551932461,
        "abs_return_acf_5": 0.3541753705764941,
        "abs_return_acf_20": 0.25894910527313664,
        "quantile_01": -0.05501436416941027,
        "quantile_99": 0.05596020635048169,
        "hill_tail_index": 2.792985359043489
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01950465658224862,
        "excess_kurtosis": 9.525121777183882,
        "return_acf_1": -0.13630122540849018,
        "abs_return_acf_1": 0.3431972797636997,
        "abs_return_acf_5": 0.40921958451970886,
        "abs_return_acf_20": 0.2513485468182783,
        "quantile_01": -0.05656403265704271,
        "quantile_99": 0.05454298944130172,
        "hill_tail_index": 2.696425889056849
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01689646736626607,
        "excess_kurtosis": 3.3104297108164538,
        "return_acf_1": -0.06553800852129982,
        "abs_return_acf_1": 0.26081787625547764,
        "abs_return_acf_5": 0.22176237964343842,
        "abs_return_acf_20": 0.2736389034410174,
        "quantile_01": -0.05070717513919035,
        "quantile_99": 0.04556633084420409,
        "hill_tail_index": 3.192409921774741
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016744796088967742,
        "excess_kurtosis": 5.055290533171217,
        "return_acf_1": -0.09346957867525232,
        "abs_return_acf_1": 0.34920223951448726,
        "abs_return_acf_5": 0.2608866904011448,
        "abs_return_acf_20": 0.23450846360544828,
        "quantile_01": -0.047188571171959716,
        "quantile_99": 0.0471669060422537,
        "hill_tail_index": 3.9317773640255385
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.015939380721604852,
        "excess_kurtosis": 3.9807656512016685,
        "return_acf_1": -0.08327397054863181,
        "abs_return_acf_1": 0.31639213386660375,
        "abs_return_acf_5": 0.23441536320533854,
        "abs_return_acf_20": 0.267898914940929,
        "quantile_01": -0.047626374455869126,
        "quantile_99": 0.038923672951569406,
        "hill_tail_index": 2.9944235138465998
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01866170574557772,
        "excess_kurtosis": 7.780225860482577,
        "return_acf_1": -0.09759575435385343,
        "abs_return_acf_1": 0.3375030961000748,
        "abs_return_acf_5": 0.314317532711294,
        "abs_return_acf_20": 0.2826544280170055,
        "quantile_01": -0.051909183451797986,
        "quantile_99": 0.0491112069133832,
        "hill_tail_index": 2.7170689336456393
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019325643765259602,
        "excess_kurtosis": 5.394662693862514,
        "return_acf_1": -0.11263849456538567,
        "abs_return_acf_1": 0.30915021353165234,
        "abs_return_acf_5": 0.31697433977137834,
        "abs_return_acf_20": 0.23212225203016856,
        "quantile_01": -0.06550823058177963,
        "quantile_99": 0.05140536622059144,
        "hill_tail_index": 3.893416423073929
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017439028038494075,
        "excess_kurtosis": 5.452902843237746,
        "return_acf_1": -0.03349325979582879,
        "abs_return_acf_1": 0.37007403338840333,
        "abs_return_acf_5": 0.36899434396139774,
        "abs_return_acf_20": 0.36497464726212525,
        "quantile_01": -0.05740610381391202,
        "quantile_99": 0.04682327039434483,
        "hill_tail_index": 3.824937341442459
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01926160878466882,
        "excess_kurtosis": 6.759841468358543,
        "return_acf_1": -0.04967721143489116,
        "abs_return_acf_1": 0.39242099423513505,
        "abs_return_acf_5": 0.29832741409576746,
        "abs_return_acf_20": 0.2966758061168218,
        "quantile_01": -0.06083467289098119,
        "quantile_99": 0.0596619834371238,
        "hill_tail_index": 3.3570270885682736
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018628852287954988,
        "excess_kurtosis": 6.936688063454346,
        "return_acf_1": -0.05991119628700156,
        "abs_return_acf_1": 0.27727251343334075,
        "abs_return_acf_5": 0.23914003698025366,
        "abs_return_acf_20": 0.3247908258215603,
        "quantile_01": -0.05657276374771287,
        "quantile_99": 0.05761353180311678,
        "hill_tail_index": 3.826131770583167
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016858512594479118,
        "excess_kurtosis": 3.1937168976259125,
        "return_acf_1": -0.14742295624029342,
        "abs_return_acf_1": 0.34705767034605794,
        "abs_return_acf_5": 0.2669071563159319,
        "abs_return_acf_20": 0.25831328363769895,
        "quantile_01": -0.04705150703911128,
        "quantile_99": 0.04621638546420701,
        "hill_tail_index": 4.130152748378683
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01987237469363031,
        "excess_kurtosis": 7.910302135478602,
        "return_acf_1": -0.09079090412806053,
        "abs_return_acf_1": 0.3306680797006324,
        "abs_return_acf_5": 0.34384069580957666,
        "abs_return_acf_20": 0.2889535268260642,
        "quantile_01": -0.06270129514559178,
        "quantile_99": 0.060789470865606945,
        "hill_tail_index": 2.8333161102994646
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01554188354611409,
        "excess_kurtosis": 1.938821030943437,
        "return_acf_1": -0.1148301932282956,
        "abs_return_acf_1": 0.23427668882543806,
        "abs_return_acf_5": 0.18545872003575928,
        "abs_return_acf_20": 0.14456264582051948,
        "quantile_01": -0.039978012976121954,
        "quantile_99": 0.04391660166010923,
        "hill_tail_index": 5.334200829926373
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01976194779272467,
        "excess_kurtosis": 6.874880005233647,
        "return_acf_1": -0.05503343139619932,
        "abs_return_acf_1": 0.41986305368254084,
        "abs_return_acf_5": 0.35876800299395273,
        "abs_return_acf_20": 0.29072258731556555,
        "quantile_01": -0.06223179032258676,
        "quantile_99": 0.055601119889196894,
        "hill_tail_index": 3.682207108409805
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016583547640381655,
        "excess_kurtosis": 4.241862574646372,
        "return_acf_1": -0.06123025893806656,
        "abs_return_acf_1": 0.19998281714597307,
        "abs_return_acf_5": 0.18427323759843012,
        "abs_return_acf_20": 0.19489829524526953,
        "quantile_01": -0.04396475118975987,
        "quantile_99": 0.04764057087675767,
        "hill_tail_index": 4.235721432997415
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015210207076447952,
        "excess_kurtosis": 3.6280038858118226,
        "return_acf_1": -0.07763869980929151,
        "abs_return_acf_1": 0.33051213372474075,
        "abs_return_acf_5": 0.3025625260725403,
        "abs_return_acf_20": 0.27340687835240424,
        "quantile_01": -0.04624109165461784,
        "quantile_99": 0.0436199146900363,
        "hill_tail_index": 3.460515019962517
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016819369001958302,
        "excess_kurtosis": 3.2155398350712376,
        "return_acf_1": -0.16194663878572016,
        "abs_return_acf_1": 0.21898377781626252,
        "abs_return_acf_5": 0.2540613172975217,
        "abs_return_acf_20": 0.24400500566877126,
        "quantile_01": -0.045264926154249714,
        "quantile_99": 0.05178965813955465,
        "hill_tail_index": 4.21582498510354
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016729509728235295,
        "excess_kurtosis": 5.734237316717897,
        "return_acf_1": -0.03834513959502984,
        "abs_return_acf_1": 0.27991820050270944,
        "abs_return_acf_5": 0.25854960559032636,
        "abs_return_acf_20": 0.2587037074368376,
        "quantile_01": -0.04668979407480964,
        "quantile_99": 0.0417680056280696,
        "hill_tail_index": 3.414960727241455
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021428437399663686,
        "excess_kurtosis": 12.032115625774743,
        "return_acf_1": -0.03309332190130161,
        "abs_return_acf_1": 0.47023118103158795,
        "abs_return_acf_5": 0.41216527741071496,
        "abs_return_acf_20": 0.36930663999838376,
        "quantile_01": -0.06125772466318884,
        "quantile_99": 0.0795138030159545,
        "hill_tail_index": 2.824083103872995
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
