# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27003
Run ID: `8d1179ea8127ac3bc4b4207cf10ec67b0624af1b6d9e133261c8e37e38fc2fe6`
Result fingerprint: `f318bf512351fe2417e6f673aca0ae747c042599049f694a76abef7d9b8d9045`

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
    "equal_weight_sd": -0.48438095238094914,
    "equal_weight_raw": -7.265714285714236,
    "fixed_start_cap_weight_sd": -0.45548766482608655,
    "fixed_start_cap_weight_raw": -6.832314972391298,
    "end_cap_weight_sd": -0.4570885854065698,
    "end_cap_weight_raw": -6.856328781098548
  },
  "full_period_change": {
    "equal_weight_sd": -0.7526547619047572,
    "equal_weight_raw": -11.289821428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7223945105820061,
    "inflation_mean_sd": 0.5732083333333333
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4680000000000033,
    "equal_weight_raw": 7.020000000000048,
    "fixed_start_cap_weight_sd": 0.4968932875548658,
    "fixed_start_cap_weight_raw": 7.453399313322986,
    "end_cap_weight_sd": 0.49529236697438267,
    "end_cap_weight_raw": 7.429385504615741
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.542380952380949,
      "change_raw": -8.135714285714235,
      "decay_adjusted_gain_sd": 0.4100000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4001587301587269,
      "change_raw": -6.0023809523809035,
      "decay_adjusted_gain_sd": 0.5522222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.5168253968253935,
      "change_raw": -7.752380952380903,
      "decay_adjusted_gain_sd": 0.43555555555555864
    },
    "large_minus_small_sd": -0.025555555555555443,
    "large_minus_small_raw": -0.38333333333333164
  },
  "inflation": {
    "initial_mean_sd": 0.20000000000000004,
    "final_mean_sd": 0.6114166666666667,
    "mean_sd": 0.42258097418817653,
    "mean_absolute_raw_gap": 6.338714612822647,
    "final_absolute_raw_gap": 9.171249999999999,
    "mean_range_fraction": 0.06338714612822648
  },
  "impact": {
    "initial_share": 0.18666666666666668,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.2755797502879339,
    "final_wealth_share": 0.35214121225068323
  },
  "pricing_slope": {
    "mean": -0.002231110829261606,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.10555524390579196,
    "real_improvement_cost": 0.08048850910036737,
    "washing_cost": 0.02506673480542459,
    "fine_transfer": 0.007045849705224366,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11260109361101633,
    "resource_cost_fraction_initial_cap": 0.0035185081301930664,
    "private_net_outflow_fraction_initial_cap": 0.0037533697870338785,
    "fine_transfer_fraction_initial_cap": 0.00023486165684081224,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.006382544188196855,
    "unapplied_final_day_resource_cost": 0.0036205256075599016
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 133.01091902673065,
    "beneficial_raw_gain_per_resource_cost": 1995.1637854009598,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 3.0997903711180848,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.12359989492760876,
    "accrued_cost_fraction_initial_cap": 0.10332634570393619,
    "mean_contract_rate": 0.04219740153813603,
    "maximum_ledger_error": 1.1180834903756764e-19
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
    "maximum_relative_cash_error": 1.521953636331777e-15,
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
      "minimum": -0.23168161578605515,
      "maximum": -0.074453351972715,
      "mean": -0.14589693288999073,
      "median": -0.15162273629538392,
      "quantile_05": -0.20393692170760794,
      "quantile_95": -0.08729746957070024
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
      "minimum": 0.29215789475639176,
      "maximum": 0.7359336436485296,
      "mean": 0.46046543950674623,
      "median": 0.4281470231916093,
      "quantile_05": 0.3225342820080718,
      "quantile_95": 0.6523927459700051
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
        "daily_volatility": 0.016447624139870096,
        "excess_kurtosis": 4.518881048327727,
        "return_acf_1": -0.15551372724219384,
        "abs_return_acf_1": 0.36210634309008854,
        "abs_return_acf_5": 0.33366336187580503,
        "abs_return_acf_20": 0.3242247133216405,
        "quantile_01": -0.04789165406871377,
        "quantile_99": 0.04036093822079341,
        "hill_tail_index": 3.492308733256829
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.014740073501654401,
        "excess_kurtosis": 3.642422909845563,
        "return_acf_1": -0.12929854361212256,
        "abs_return_acf_1": 0.29869920155708723,
        "abs_return_acf_5": 0.279040040363803,
        "abs_return_acf_20": 0.20100233332536618,
        "quantile_01": -0.03613798539179477,
        "quantile_99": 0.039977704189150455,
        "hill_tail_index": 3.1210224550606758
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016550558030575722,
        "excess_kurtosis": 6.388133541065693,
        "return_acf_1": -0.23168161578605515,
        "abs_return_acf_1": 0.36998448051708455,
        "abs_return_acf_5": 0.38492915923665894,
        "abs_return_acf_20": 0.3242067359435234,
        "quantile_01": -0.05115940457265382,
        "quantile_99": 0.04435258336570134,
        "hill_tail_index": 3.143773172916484
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01898052624914298,
        "excess_kurtosis": 5.174837256301668,
        "return_acf_1": -0.09604775827440497,
        "abs_return_acf_1": 0.2888265790442137,
        "abs_return_acf_5": 0.2762618285575574,
        "abs_return_acf_20": 0.27266670589558684,
        "quantile_01": -0.054000821244982546,
        "quantile_99": 0.050182342498652326,
        "hill_tail_index": 3.119605470460249
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.014877232472921156,
        "excess_kurtosis": 0.7826837575468697,
        "return_acf_1": -0.12329478272807809,
        "abs_return_acf_1": 0.09377001734169835,
        "abs_return_acf_5": 0.1000194773964255,
        "abs_return_acf_20": 0.038109510031027055,
        "quantile_01": -0.036177890541373756,
        "quantile_99": 0.035762030924490686,
        "hill_tail_index": 6.072255003466806
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016180832035257078,
        "excess_kurtosis": 5.67506462177635,
        "return_acf_1": -0.17070008719716293,
        "abs_return_acf_1": 0.27042370421201023,
        "abs_return_acf_5": 0.32447173978135796,
        "abs_return_acf_20": 0.21152371036566175,
        "quantile_01": -0.047173629391279746,
        "quantile_99": 0.04250119556920752,
        "hill_tail_index": 3.1564902870718314
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017534766787218273,
        "excess_kurtosis": 6.9284070954282075,
        "return_acf_1": -0.1722527979050368,
        "abs_return_acf_1": 0.2954491728955833,
        "abs_return_acf_5": 0.31474736636099043,
        "abs_return_acf_20": 0.2118147769162825,
        "quantile_01": -0.053123689496486354,
        "quantile_99": 0.04432723918706836,
        "hill_tail_index": 3.2210177948390473
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01605221236805945,
        "excess_kurtosis": 5.891075775620768,
        "return_acf_1": -0.1780137077234011,
        "abs_return_acf_1": 0.2840287156812884,
        "abs_return_acf_5": 0.35115052497078786,
        "abs_return_acf_20": 0.2753028420114756,
        "quantile_01": -0.052428603760056564,
        "quantile_99": 0.04428109092235237,
        "hill_tail_index": 2.932059764010683
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018543284189204777,
        "excess_kurtosis": 5.755131899538677,
        "return_acf_1": -0.15764210405551304,
        "abs_return_acf_1": 0.3999077271813164,
        "abs_return_acf_5": 0.35044312792886184,
        "abs_return_acf_20": 0.3010903267478544,
        "quantile_01": -0.05339636671399543,
        "quantile_99": 0.04561576953172806,
        "hill_tail_index": 2.7520140383545315
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016503813222729022,
        "excess_kurtosis": 6.636373039715128,
        "return_acf_1": -0.1755949816629124,
        "abs_return_acf_1": 0.35978519393635405,
        "abs_return_acf_5": 0.37809072862748366,
        "abs_return_acf_20": 0.3346437106229845,
        "quantile_01": -0.05421893852894176,
        "quantile_99": 0.0471254878877776,
        "hill_tail_index": 2.906132622583752
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018867050083332643,
        "excess_kurtosis": 3.250947727184461,
        "return_acf_1": -0.08453321431613811,
        "abs_return_acf_1": 0.3410478807887598,
        "abs_return_acf_5": 0.2830260841990405,
        "abs_return_acf_20": 0.23969852837390074,
        "quantile_01": -0.05931167453503256,
        "quantile_99": 0.049247866298081526,
        "hill_tail_index": 4.213743621963213
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019796204764198338,
        "excess_kurtosis": 6.790400952042866,
        "return_acf_1": -0.12860907175486197,
        "abs_return_acf_1": 0.3588285224907279,
        "abs_return_acf_5": 0.3475459565101918,
        "abs_return_acf_20": 0.3120903473114675,
        "quantile_01": -0.06061881186233186,
        "quantile_99": 0.058436905572666946,
        "hill_tail_index": 2.73709520691367
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018330723598161465,
        "excess_kurtosis": 9.991423946085808,
        "return_acf_1": -0.2174766761392917,
        "abs_return_acf_1": 0.38300411553536756,
        "abs_return_acf_5": 0.4093178455123137,
        "abs_return_acf_20": 0.36756571806685256,
        "quantile_01": -0.061002490341460325,
        "quantile_99": 0.04736154394133369,
        "hill_tail_index": 2.0711508327741304
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01727208504857328,
        "excess_kurtosis": 4.603272828466734,
        "return_acf_1": -0.1083069444955375,
        "abs_return_acf_1": 0.25061327060191557,
        "abs_return_acf_5": 0.1482462818377638,
        "abs_return_acf_20": 0.20692194364020947,
        "quantile_01": -0.045649234491485134,
        "quantile_99": 0.05023501948793998,
        "hill_tail_index": 3.1111554520113716
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015826124822035263,
        "excess_kurtosis": 6.474479475237418,
        "return_acf_1": -0.1821566621953297,
        "abs_return_acf_1": 0.2391817687589764,
        "abs_return_acf_5": 0.26794422502803616,
        "abs_return_acf_20": 0.2101424845970135,
        "quantile_01": -0.042086647087331557,
        "quantile_99": 0.038631038147280666,
        "hill_tail_index": 2.7322354029523495
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016879973092979672,
        "excess_kurtosis": 7.453756294234903,
        "return_acf_1": -0.11389817280270365,
        "abs_return_acf_1": 0.31793178511677445,
        "abs_return_acf_5": 0.31510241058928967,
        "abs_return_acf_20": 0.3084485482576275,
        "quantile_01": -0.052739594344205235,
        "quantile_99": 0.041271217246694226,
        "hill_tail_index": 3.128074958771584
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017910637914988814,
        "excess_kurtosis": 4.55224390182153,
        "return_acf_1": -0.156850610372728,
        "abs_return_acf_1": 0.3033722501962427,
        "abs_return_acf_5": 0.26899118846704057,
        "abs_return_acf_20": 0.2667169779835066,
        "quantile_01": -0.059025405907038045,
        "quantile_99": 0.05038985654397699,
        "hill_tail_index": 4.130507490554231
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01620819662028763,
        "excess_kurtosis": 5.620969500703545,
        "return_acf_1": -0.17778557835069733,
        "abs_return_acf_1": 0.3119263190909156,
        "abs_return_acf_5": 0.30945511340233595,
        "abs_return_acf_20": 0.30203450993298553,
        "quantile_01": -0.04426648905918892,
        "quantile_99": 0.04371235622063832,
        "hill_tail_index": 2.6653913171299326
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017012314112436876,
        "excess_kurtosis": 3.4742799205272554,
        "return_acf_1": -0.16393700891099988,
        "abs_return_acf_1": 0.2092314184413803,
        "abs_return_acf_5": 0.2428421380766842,
        "abs_return_acf_20": 0.19821798905548538,
        "quantile_01": -0.04709955811089862,
        "quantile_99": 0.050442660359181796,
        "hill_tail_index": 4.296068553959354
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019055381839707095,
        "excess_kurtosis": 5.647107670661645,
        "return_acf_1": -0.13608580587346142,
        "abs_return_acf_1": 0.3844743651637746,
        "abs_return_acf_5": 0.3765483417529895,
        "abs_return_acf_20": 0.33442560791849363,
        "quantile_01": -0.06021167057714434,
        "quantile_99": 0.048487940858042075,
        "hill_tail_index": 3.344100417823398
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017657373553879804,
        "excess_kurtosis": 2.1505415907171983,
        "return_acf_1": -0.0994374605642463,
        "abs_return_acf_1": 0.25357769376323847,
        "abs_return_acf_5": 0.18103676433180138,
        "abs_return_acf_20": 0.24002976461275485,
        "quantile_01": -0.05065757531588607,
        "quantile_99": 0.048913490011532404,
        "hill_tail_index": 5.656643978166771
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02132843199239479,
        "excess_kurtosis": 10.613763929000548,
        "return_acf_1": -0.09067600377072059,
        "abs_return_acf_1": 0.4052644120432346,
        "abs_return_acf_5": 0.35969005331418685,
        "abs_return_acf_20": 0.3596428684504955,
        "quantile_01": -0.06800032104034988,
        "quantile_99": 0.057853862850045686,
        "hill_tail_index": 2.4787838633184514
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018851776609200226,
        "excess_kurtosis": 3.5371055063334698,
        "return_acf_1": -0.17359362387635585,
        "abs_return_acf_1": 0.36367901898817534,
        "abs_return_acf_5": 0.28691291094226296,
        "abs_return_acf_20": 0.2531117525887634,
        "quantile_01": -0.05987499721214887,
        "quantile_99": 0.054332777945798195,
        "hill_tail_index": 4.265393757304217
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018878807927295963,
        "excess_kurtosis": 4.529084443129259,
        "return_acf_1": -0.18738833295777227,
        "abs_return_acf_1": 0.3620182070181103,
        "abs_return_acf_5": 0.3221169451064115,
        "abs_return_acf_20": 0.272298725857472,
        "quantile_01": -0.0567772554842837,
        "quantile_99": 0.05684699737604285,
        "hill_tail_index": 4.6610024632118
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017114310585419068,
        "excess_kurtosis": 2.8557360432383962,
        "return_acf_1": -0.10509001356626241,
        "abs_return_acf_1": 0.2268719623696406,
        "abs_return_acf_5": 0.23225534193934763,
        "abs_return_acf_20": 0.1976604285733619,
        "quantile_01": -0.048221784061972854,
        "quantile_99": 0.04743786777525328,
        "hill_tail_index": 4.745751473473296
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017432825565472317,
        "excess_kurtosis": 15.671032937172058,
        "return_acf_1": -0.13627119722382824,
        "abs_return_acf_1": 0.40022480787904735,
        "abs_return_acf_5": 0.38496799045920627,
        "abs_return_acf_20": 0.20553535348868085,
        "quantile_01": -0.04031193809790245,
        "quantile_99": 0.04726113013663933,
        "hill_tail_index": 1.9961291427694599
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01891905721109445,
        "excess_kurtosis": 6.1128896958436965,
        "return_acf_1": -0.074453351972715,
        "abs_return_acf_1": 0.26334647170478204,
        "abs_return_acf_5": 0.26313805494377435,
        "abs_return_acf_20": 0.24414372953690003,
        "quantile_01": -0.06446883706463068,
        "quantile_99": 0.04918924364496501,
        "hill_tail_index": 3.2102752375626573
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016254660498037823,
        "excess_kurtosis": 4.498033252625493,
        "return_acf_1": -0.1809745426747804,
        "abs_return_acf_1": 0.28146207079475793,
        "abs_return_acf_5": 0.21703577772104343,
        "abs_return_acf_20": 0.18699133929119693,
        "quantile_01": -0.04162872733814822,
        "quantile_99": 0.03894098521958302,
        "hill_tail_index": 3.003104929792009
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01668048566325097,
        "excess_kurtosis": 4.683482550725571,
        "return_acf_1": -0.12161186334583626,
        "abs_return_acf_1": 0.2173158683281002,
        "abs_return_acf_5": 0.2614067738027336,
        "abs_return_acf_20": 0.1809391824766768,
        "quantile_01": -0.04808590739745638,
        "quantile_99": 0.04242680942897837,
        "hill_tail_index": 2.871678374409778
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017086102475552426,
        "excess_kurtosis": 4.34356604426377,
        "return_acf_1": -0.14773174534857397,
        "abs_return_acf_1": 0.24479468995773623,
        "abs_return_acf_5": 0.27511484387160917,
        "abs_return_acf_20": 0.18680451875625262,
        "quantile_01": -0.04961863380495133,
        "quantile_99": 0.04563747952033408,
        "hill_tail_index": 3.5774508553986544
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
Unseen state share: 0.012222222222222223
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
