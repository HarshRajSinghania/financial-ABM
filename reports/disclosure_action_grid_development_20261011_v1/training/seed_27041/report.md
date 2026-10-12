# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27041
Run ID: `7eff6ae204cc709a87f4617987aca51e5413a73c66926059af5fb9e629f7feb4`
Result fingerprint: `37dd7f5d4b33963bf7790a84def94fafae460fce38f9794a02329161bc98ac04`

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
    "equal_weight_sd": -0.5912976190476158,
    "equal_weight_raw": -8.869464285714235,
    "fixed_start_cap_weight_sd": -0.5551045904489041,
    "fixed_start_cap_weight_raw": -8.326568856733562,
    "end_cap_weight_sd": -0.5406215448702649,
    "end_cap_weight_raw": -8.109323173053973
  },
  "full_period_change": {
    "equal_weight_sd": -0.9453214285714234,
    "equal_weight_raw": -14.179821428571351
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9111306216931171,
    "inflation_mean_sd": 0.7227043650793651
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.36108333333333653,
    "equal_weight_raw": 5.416250000000047,
    "fixed_start_cap_weight_sd": 0.397276361932048,
    "fixed_start_cap_weight_raw": 5.95914542898072,
    "end_cap_weight_sd": 0.4117594075106874,
    "end_cap_weight_raw": 6.176391112660314
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.47488095238094924,
      "change_raw": -7.123214285714239,
      "decay_adjusted_gain_sd": 0.47750000000000314
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6240476190476159,
      "change_raw": -9.360714285714238,
      "decay_adjusted_gain_sd": 0.3283333333333364
    },
    "small": {
      "count": 18,
      "change_sd": -0.5943253968253936,
      "change_raw": -8.914880952380905,
      "decay_adjusted_gain_sd": 0.35805555555555885
    },
    "large_minus_small_sd": 0.11944444444444441,
    "large_minus_small_raw": 1.791666666666666
  },
  "inflation": {
    "initial_mean_sd": 0.276,
    "final_mean_sd": 0.7463333333333334,
    "mean_sd": 0.5142850402442408,
    "mean_absolute_raw_gap": 7.714275603663613,
    "final_absolute_raw_gap": 11.194999999999999,
    "mean_range_fraction": 0.07714275603663613
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.35199944316815285,
    "final_wealth_share": 0.370591842372382
  },
  "pricing_slope": {
    "mean": -0.004092705880224376,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.06654391198559614,
    "real_improvement_cost": 0.05230822529502918,
    "washing_cost": 0.014235686690566959,
    "fine_transfer": 0.008149037132374118,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07469294911797027,
    "resource_cost_fraction_initial_cap": 0.002218130399519871,
    "private_net_outflow_fraction_initial_cap": 0.0024897649705990085,
    "fine_transfer_fraction_initial_cap": 0.00027163457107913725,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008353057083503186,
    "unapplied_final_day_resource_cost": 0.0011822826235516285
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 162.78724344226802,
    "beneficial_raw_gain_per_resource_cost": 2441.80865163402,
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
    "accrued_cost": 3.0925457844217723,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.1163553082312954,
    "accrued_cost_fraction_initial_cap": 0.10308485948072574,
    "mean_contract_rate": 0.04381993927697766,
    "maximum_ledger_error": 6.606856988583543e-20
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
    "maximum_relative_cash_error": 1.1720208303886378e-15,
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
      "minimum": -0.24399527966997347,
      "maximum": -0.03416922630844025,
      "mean": -0.14264746233854728,
      "median": -0.1420155006021923,
      "quantile_05": -0.18961052230498943,
      "quantile_95": -0.08394050185056195
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
      "minimum": 0.19366672101983032,
      "maximum": 0.8183252557873261,
      "mean": 0.6115262075137899,
      "median": 0.6637019194064435,
      "quantile_05": 0.2730255178088272,
      "quantile_95": 0.7731931757975237
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
        "daily_volatility": 0.02255988551083669,
        "excess_kurtosis": 11.883967419546268,
        "return_acf_1": -0.11004582980922947,
        "abs_return_acf_1": 0.39120311517406814,
        "abs_return_acf_5": 0.3849566338355508,
        "abs_return_acf_20": 0.31009964883028773,
        "quantile_01": -0.07837858291011422,
        "quantile_99": 0.060229015233379965,
        "hill_tail_index": 3.0612013508845735
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024569911600353017,
        "excess_kurtosis": 45.394746389190196,
        "return_acf_1": -0.1390765981793888,
        "abs_return_acf_1": 0.26843379791075417,
        "abs_return_acf_5": 0.42755623177205715,
        "abs_return_acf_20": 0.2150077010930371,
        "quantile_01": -0.05675924434271376,
        "quantile_99": 0.06874638188694343,
        "hill_tail_index": 1.9073994024447518
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02366227093017703,
        "excess_kurtosis": 10.86029802943179,
        "return_acf_1": -0.17846903956959106,
        "abs_return_acf_1": 0.2798090345525467,
        "abs_return_acf_5": 0.32492946187591304,
        "abs_return_acf_20": 0.2578758359346274,
        "quantile_01": -0.07998213244537448,
        "quantile_99": 0.06967357759824194,
        "hill_tail_index": 3.086543794298096
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021431777193063172,
        "excess_kurtosis": 10.264250716820857,
        "return_acf_1": -0.19302084820682927,
        "abs_return_acf_1": 0.31934289197781657,
        "abs_return_acf_5": 0.3196472726992661,
        "abs_return_acf_20": 0.27189300283020473,
        "quantile_01": -0.06616995437774265,
        "quantile_99": 0.058435853980728536,
        "hill_tail_index": 3.2247295455310416
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019261229989360116,
        "excess_kurtosis": 5.544854817571,
        "return_acf_1": -0.11092600245258089,
        "abs_return_acf_1": 0.3041101361004903,
        "abs_return_acf_5": 0.3116442781966794,
        "abs_return_acf_20": 0.24412159598421942,
        "quantile_01": -0.05464810091145713,
        "quantile_99": 0.060591770095112935,
        "hill_tail_index": 3.2435038168494548
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02087696909266439,
        "excess_kurtosis": 19.787966480253655,
        "return_acf_1": -0.17037499915425605,
        "abs_return_acf_1": 0.32273074495641835,
        "abs_return_acf_5": 0.35831766082097183,
        "abs_return_acf_20": 0.2871249262717119,
        "quantile_01": -0.06571781683860192,
        "quantile_99": 0.04297424671299765,
        "hill_tail_index": 2.175344875096215
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021685254663126752,
        "excess_kurtosis": 13.498091979585478,
        "return_acf_1": -0.18544234620274072,
        "abs_return_acf_1": 0.3006958385011175,
        "abs_return_acf_5": 0.34856018013403944,
        "abs_return_acf_20": 0.3445306294765622,
        "quantile_01": -0.07096883077437141,
        "quantile_99": 0.05779599971449247,
        "hill_tail_index": 3.0884686399231045
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022854015566059427,
        "excess_kurtosis": 15.671268349508075,
        "return_acf_1": -0.15320164577506395,
        "abs_return_acf_1": 0.3749348204642505,
        "abs_return_acf_5": 0.4537185339631557,
        "abs_return_acf_20": 0.3434402485383029,
        "quantile_01": -0.0779915864851486,
        "quantile_99": 0.0660496608209042,
        "hill_tail_index": 2.7845193230251795
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02170495276232355,
        "excess_kurtosis": 8.868556614730691,
        "return_acf_1": -0.1720080266752732,
        "abs_return_acf_1": 0.3211159588147191,
        "abs_return_acf_5": 0.35743023868756946,
        "abs_return_acf_20": 0.3162744588238992,
        "quantile_01": -0.072662068585058,
        "quantile_99": 0.06576019254742903,
        "hill_tail_index": 3.905343152945796
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02478904047399469,
        "excess_kurtosis": 16.847295291643793,
        "return_acf_1": -0.13110691456418708,
        "abs_return_acf_1": 0.353715876115605,
        "abs_return_acf_5": 0.4435170211929182,
        "abs_return_acf_20": 0.30774708672040324,
        "quantile_01": -0.07889409021072762,
        "quantile_99": 0.07314260442565843,
        "hill_tail_index": 2.6992459394901247
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021816180314130684,
        "excess_kurtosis": 8.999613548948313,
        "return_acf_1": -0.11698410055847122,
        "abs_return_acf_1": 0.36470850732822047,
        "abs_return_acf_5": 0.4156945037567138,
        "abs_return_acf_20": 0.297865584916191,
        "quantile_01": -0.0668687191869558,
        "quantile_99": 0.057968936242179275,
        "hill_tail_index": 3.0986426003826306
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022591594976473485,
        "excess_kurtosis": 6.42907214073076,
        "return_acf_1": -0.09018644421860057,
        "abs_return_acf_1": 0.41131420836379895,
        "abs_return_acf_5": 0.4414872650348964,
        "abs_return_acf_20": 0.3413722225408433,
        "quantile_01": -0.09426388919737128,
        "quantile_99": 0.07316967131664906,
        "hill_tail_index": 4.143232696176855
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022536283229829836,
        "excess_kurtosis": 9.107792692044859,
        "return_acf_1": -0.08646035144604113,
        "abs_return_acf_1": 0.381473736673318,
        "abs_return_acf_5": 0.4423784904713483,
        "abs_return_acf_20": 0.3310460271862863,
        "quantile_01": -0.08178080275555705,
        "quantile_99": 0.060835764214429336,
        "hill_tail_index": 2.9095344826475316
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020948692468509618,
        "excess_kurtosis": 18.754025615619526,
        "return_acf_1": -0.17596372627187992,
        "abs_return_acf_1": 0.33449109628372414,
        "abs_return_acf_5": 0.3297413775714395,
        "abs_return_acf_20": 0.270485932097615,
        "quantile_01": -0.061759400216321626,
        "quantile_99": 0.044181973016887345,
        "hill_tail_index": 2.0465817145484584
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02329792638289347,
        "excess_kurtosis": 8.755900894746059,
        "return_acf_1": -0.09255414334408583,
        "abs_return_acf_1": 0.35745794896140315,
        "abs_return_acf_5": 0.39422652681310977,
        "abs_return_acf_20": 0.3302794741097338,
        "quantile_01": -0.07961999196613768,
        "quantile_99": 0.07266907476700785,
        "hill_tail_index": 3.8152482097860556
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021158183395899068,
        "excess_kurtosis": 17.03492936273643,
        "return_acf_1": -0.24399527966997347,
        "abs_return_acf_1": 0.37024633325922235,
        "abs_return_acf_5": 0.327066742718295,
        "abs_return_acf_20": 0.3464235193312089,
        "quantile_01": -0.07341685444731469,
        "quantile_99": 0.05251989306870807,
        "hill_tail_index": 2.0152599970830734
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023422891710873365,
        "excess_kurtosis": 9.317287165123298,
        "return_acf_1": -0.08187880672698807,
        "abs_return_acf_1": 0.3806999372575663,
        "abs_return_acf_5": 0.4597848295878327,
        "abs_return_acf_20": 0.3336169232691458,
        "quantile_01": -0.08325208959556243,
        "quantile_99": 0.062342586221553704,
        "hill_tail_index": 2.8148943580241617
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02295960899348139,
        "excess_kurtosis": 10.636912970057423,
        "return_acf_1": -0.1256519542469997,
        "abs_return_acf_1": 0.34017560435618455,
        "abs_return_acf_5": 0.30258838202495203,
        "abs_return_acf_20": 0.2421560435259959,
        "quantile_01": -0.0734306361335832,
        "quantile_99": 0.06028162675970059,
        "hill_tail_index": 2.795276582569911
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023315504616371316,
        "excess_kurtosis": 13.611688793358748,
        "return_acf_1": -0.03416922630844025,
        "abs_return_acf_1": 0.43224627737198035,
        "abs_return_acf_5": 0.4974289059618238,
        "abs_return_acf_20": 0.3453214842313793,
        "quantile_01": -0.07573105771269296,
        "quantile_99": 0.06766968669407047,
        "hill_tail_index": 2.6739641346671164
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021271901699910195,
        "excess_kurtosis": 9.84231018491613,
        "return_acf_1": -0.14495440302499585,
        "abs_return_acf_1": 0.300852922873121,
        "abs_return_acf_5": 0.360435610763228,
        "abs_return_acf_20": 0.35836886083682856,
        "quantile_01": -0.0728293108788886,
        "quantile_99": 0.052125588584445076,
        "hill_tail_index": 2.8517923765242963
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020001739083412996,
        "excess_kurtosis": 13.548543620471698,
        "return_acf_1": -0.16665729431601953,
        "abs_return_acf_1": 0.2618537187491398,
        "abs_return_acf_5": 0.3916550545723243,
        "abs_return_acf_20": 0.3158292933905293,
        "quantile_01": -0.06368357767841668,
        "quantile_99": 0.059059518248224696,
        "hill_tail_index": 3.026753848268223
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021247961584400045,
        "excess_kurtosis": 9.96825834849595,
        "return_acf_1": -0.15209651283580003,
        "abs_return_acf_1": 0.2732539230425105,
        "abs_return_acf_5": 0.33208630313893595,
        "abs_return_acf_20": 0.2692065123364309,
        "quantile_01": -0.0668867048078803,
        "quantile_99": 0.05092604353906362,
        "hill_tail_index": 2.5177350591881287
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02021541392775343,
        "excess_kurtosis": 21.269634216615703,
        "return_acf_1": -0.13713830894227566,
        "abs_return_acf_1": 0.3560818987198175,
        "abs_return_acf_5": 0.39085884106070773,
        "abs_return_acf_20": 0.3956015480132888,
        "quantile_01": -0.06561986989032048,
        "quantile_99": 0.04434049197105922,
        "hill_tail_index": 1.7379739812543928
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020891082796500586,
        "excess_kurtosis": 11.154399357395429,
        "return_acf_1": -0.13831416068701177,
        "abs_return_acf_1": 0.3156828729019386,
        "abs_return_acf_5": 0.3741798566076881,
        "abs_return_acf_20": 0.2577847299676708,
        "quantile_01": -0.072804674450103,
        "quantile_99": 0.06465126815993733,
        "hill_tail_index": 3.213152589793886
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02214547631924144,
        "excess_kurtosis": 11.74956547188669,
        "return_acf_1": -0.1649354570254306,
        "abs_return_acf_1": 0.3858177865007604,
        "abs_return_acf_5": 0.37415104183341485,
        "abs_return_acf_20": 0.3252312576011314,
        "quantile_01": -0.0683277309774506,
        "quantile_99": 0.05646151589550982,
        "hill_tail_index": 2.1638947449905395
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022009046072870398,
        "excess_kurtosis": 11.77944024281817,
        "return_acf_1": -0.17540276685603473,
        "abs_return_acf_1": 0.3098379963572083,
        "abs_return_acf_5": 0.3750530137192368,
        "abs_return_acf_20": 0.32053513065491773,
        "quantile_01": -0.08400991483619001,
        "quantile_99": 0.06920315261508898,
        "hill_tail_index": 3.3466425353059317
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019663792063702543,
        "excess_kurtosis": 16.97092667874391,
        "return_acf_1": -0.1696530991586913,
        "abs_return_acf_1": 0.31267041295868825,
        "abs_return_acf_5": 0.3492730287095321,
        "abs_return_acf_20": 0.3902759749223644,
        "quantile_01": -0.06691981937873892,
        "quantile_99": 0.05284723864125864,
        "hill_tail_index": 2.5241181159484576
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020297274741335667,
        "excess_kurtosis": 6.172280835907067,
        "return_acf_1": -0.13774109773730644,
        "abs_return_acf_1": 0.3432934559556124,
        "abs_return_acf_5": 0.3948184455356247,
        "abs_return_acf_20": 0.32866915470961483,
        "quantile_01": -0.07404456970503986,
        "quantile_99": 0.05974774614393533,
        "hill_tail_index": 3.7226204718917484
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021051424599759592,
        "excess_kurtosis": 8.843777449154608,
        "return_acf_1": -0.12615948784793427,
        "abs_return_acf_1": 0.3095315678419782,
        "abs_return_acf_5": 0.3317394028337876,
        "abs_return_acf_20": 0.3235010387592582,
        "quantile_01": -0.0608644778922522,
        "quantile_99": 0.06922274159052763,
        "hill_tail_index": 4.007123203473007
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019638200701015896,
        "excess_kurtosis": 11.183893570462603,
        "return_acf_1": -0.1748549983442978,
        "abs_return_acf_1": 0.32013127183122575,
        "abs_return_acf_5": 0.34441178113797505,
        "abs_return_acf_20": 0.3107079382312364,
        "quantile_01": -0.060794485666730534,
        "quantile_99": 0.047674222115014916,
        "hill_tail_index": 2.2221684434597098
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
