# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27303
Run ID: `e92b09d8fb8f943c44f2a4fc18b9fc04afd4c9e84104690b277282bb0e0fce11`
Result fingerprint: `2b088d30a9f7f835ba3b94a9474156e2a9e7df171a906f11d5ec9db35c432da8`

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
    "equal_weight_sd": -0.842714285714283,
    "equal_weight_raw": -12.640714285714244,
    "fixed_start_cap_weight_sd": -0.810378071652729,
    "fixed_start_cap_weight_raw": -12.155671074790934,
    "end_cap_weight_sd": -0.8301493109190949,
    "end_cap_weight_raw": -12.452239663786427
  },
  "full_period_change": {
    "equal_weight_sd": -1.2444047619047576,
    "equal_weight_raw": -18.666071428571364
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.160401455026451,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.10966666666666934,
    "equal_weight_raw": 1.64500000000004,
    "fixed_start_cap_weight_sd": 0.14200288072822323,
    "fixed_start_cap_weight_raw": 2.1300432109233487,
    "end_cap_weight_sd": 0.12223164146185744,
    "end_cap_weight_raw": 1.833474621927862
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5148809523809488,
      "change_raw": -7.723214285714231,
      "decay_adjusted_gain_sd": 0.43750000000000355
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8993253968253941,
      "change_raw": -13.489880952380911,
      "decay_adjusted_gain_sd": 0.05305555555555827
    },
    "small": {
      "count": 18,
      "change_sd": -0.8690476190476165,
      "change_raw": -13.035714285714247,
      "decay_adjusted_gain_sd": 0.08333333333333583
    },
    "large_minus_small_sd": 0.35416666666666774,
    "large_minus_small_raw": 5.312500000000016
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
    "initial_wealth_share": 0.1804447901060483,
    "final_wealth_share": 0.17909398825210102
  },
  "pricing_slope": {
    "mean": -0.0010748700561207553,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.0002390886953290937,
    "real_improvement_cost": 0.0002390886953290937,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0002390886953290937,
    "resource_cost_fraction_initial_cap": 7.96962317763646e-06,
    "private_net_outflow_fraction_initial_cap": 7.96962317763646e-06,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 1.9236790277222748e-05,
    "unapplied_final_day_resource_cost": 1.3854818177003924e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 13760.583684107518,
    "beneficial_raw_gain_per_resource_cost": 206408.7552616128,
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
    "accrued_cost": 2.981800712218976,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.0056102360285001825,
    "accrued_cost_fraction_initial_cap": 0.0993933570739659,
    "mean_contract_rate": 0.040222264985099426,
    "maximum_ledger_error": 9.486769009248164e-20
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
    "maximum_relative_cash_error": 2.5566230946298818e-15,
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
      "minimum": -0.2356342094511504,
      "maximum": -0.008313081342785762,
      "mean": -0.11846606383960633,
      "median": -0.12060323469149642,
      "quantile_05": -0.20661605228084648,
      "quantile_95": -0.017733129304489864
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
      "minimum": 0.24533917069959502,
      "maximum": 0.7368055607619011,
      "mean": 0.4545241639956795,
      "median": 0.43238682041211707,
      "quantile_05": 0.29677423931184727,
      "quantile_95": 0.667230756413979
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
        "daily_volatility": 0.01816127099952844,
        "excess_kurtosis": 3.010131387797953,
        "return_acf_1": -0.15115776380706095,
        "abs_return_acf_1": 0.29283115291165257,
        "abs_return_acf_5": 0.3431853081615716,
        "abs_return_acf_20": 0.2676928480237854,
        "quantile_01": -0.050026294381466725,
        "quantile_99": 0.055839672355458,
        "hill_tail_index": 4.858287219083228
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019228149239207216,
        "excess_kurtosis": 7.76274801904248,
        "return_acf_1": -0.21530008016556798,
        "abs_return_acf_1": 0.3635319664565173,
        "abs_return_acf_5": 0.34187461213996134,
        "abs_return_acf_20": 0.35892360534949663,
        "quantile_01": -0.05943343953425258,
        "quantile_99": 0.05647274822288552,
        "hill_tail_index": 3.1651324093343014
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018154942360344768,
        "excess_kurtosis": 4.983939056849644,
        "return_acf_1": -0.18253549494042065,
        "abs_return_acf_1": 0.327684271930985,
        "abs_return_acf_5": 0.26179119966460546,
        "abs_return_acf_20": 0.2614431010378745,
        "quantile_01": -0.05585168252315994,
        "quantile_99": 0.04889139797761162,
        "hill_tail_index": 3.8017648023194055
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016953220887459985,
        "excess_kurtosis": 4.601129687450433,
        "return_acf_1": -0.12373493646057046,
        "abs_return_acf_1": 0.2459515713462977,
        "abs_return_acf_5": 0.30938951798299374,
        "abs_return_acf_20": 0.23108200051110994,
        "quantile_01": -0.04691993588543786,
        "quantile_99": 0.049824803954715655,
        "hill_tail_index": 3.35793209286788
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01775373639336582,
        "excess_kurtosis": 5.82356788213068,
        "return_acf_1": -0.15774949757785153,
        "abs_return_acf_1": 0.2930244858558592,
        "abs_return_acf_5": 0.3273593320661684,
        "abs_return_acf_20": 0.2786912160072558,
        "quantile_01": -0.05476805366898368,
        "quantile_99": 0.052731575037420576,
        "hill_tail_index": 3.50509308195708
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018390576055185223,
        "excess_kurtosis": 5.093124850332883,
        "return_acf_1": -0.15165244892537016,
        "abs_return_acf_1": 0.34027111282468214,
        "abs_return_acf_5": 0.3069031766108098,
        "abs_return_acf_20": 0.28017317707763895,
        "quantile_01": -0.05244448249504342,
        "quantile_99": 0.04563063041080577,
        "hill_tail_index": 2.968425871444777
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.015954953980630456,
        "excess_kurtosis": 5.645002978002662,
        "return_acf_1": -0.10554339211860157,
        "abs_return_acf_1": 0.3163406921169087,
        "abs_return_acf_5": 0.32902509370335564,
        "abs_return_acf_20": 0.31410861783762073,
        "quantile_01": -0.0375840049339368,
        "quantile_99": 0.04738952000544185,
        "hill_tail_index": 2.8072874579942395
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017290669194095224,
        "excess_kurtosis": 3.3748662431371104,
        "return_acf_1": -0.14777930666384378,
        "abs_return_acf_1": 0.2970601555302764,
        "abs_return_acf_5": 0.24132696460050898,
        "abs_return_acf_20": 0.2004033943813937,
        "quantile_01": -0.045424717171689104,
        "quantile_99": 0.0418128103103779,
        "hill_tail_index": 3.045940083578515
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017781866728467065,
        "excess_kurtosis": 5.699446239981738,
        "return_acf_1": -0.1724521753913323,
        "abs_return_acf_1": 0.30609345493621193,
        "abs_return_acf_5": 0.24463008218981772,
        "abs_return_acf_20": 0.2385378217341078,
        "quantile_01": -0.04909715707758818,
        "quantile_99": 0.05242292979750369,
        "hill_tail_index": 3.5635960458038207
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018175771955313964,
        "excess_kurtosis": 6.513414098701222,
        "return_acf_1": -0.10764183953097668,
        "abs_return_acf_1": 0.20732554917871368,
        "abs_return_acf_5": 0.26786297872100523,
        "abs_return_acf_20": 0.26358210347031225,
        "quantile_01": -0.053480746259866,
        "quantile_99": 0.05004230564611805,
        "hill_tail_index": 3.21725198325572
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017668731167267804,
        "excess_kurtosis": 2.2461346634664183,
        "return_acf_1": -0.10756296747413795,
        "abs_return_acf_1": 0.2896105356195273,
        "abs_return_acf_5": 0.2511679904675588,
        "abs_return_acf_20": 0.19570268445336986,
        "quantile_01": -0.04858591375542034,
        "quantile_99": 0.0475073167021847,
        "hill_tail_index": 4.150449639113656
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01513864389644817,
        "excess_kurtosis": 4.121816590954686,
        "return_acf_1": -0.008313081342785762,
        "abs_return_acf_1": 0.29506386278081814,
        "abs_return_acf_5": 0.29666072622634465,
        "abs_return_acf_20": 0.261456139361426,
        "quantile_01": -0.04524753054705678,
        "quantile_99": 0.04077088769766476,
        "hill_tail_index": 3.9934803842318227
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019064178199503654,
        "excess_kurtosis": 3.4547284757213284,
        "return_acf_1": -0.13567379507551106,
        "abs_return_acf_1": 0.29527687528884855,
        "abs_return_acf_5": 0.33720631166591136,
        "abs_return_acf_20": 0.3428760155895019,
        "quantile_01": -0.05719848507928521,
        "quantile_99": 0.05226178666502627,
        "hill_tail_index": 6.053927726076418
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018485456037468352,
        "excess_kurtosis": 5.104773014650375,
        "return_acf_1": -0.10722376654585493,
        "abs_return_acf_1": 0.33823010485834754,
        "abs_return_acf_5": 0.2983056683299005,
        "abs_return_acf_20": 0.2774034820250947,
        "quantile_01": -0.05211045975654024,
        "quantile_99": 0.05509924903071795,
        "hill_tail_index": 4.6219875139927735
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020405176019778055,
        "excess_kurtosis": 6.925343140247996,
        "return_acf_1": -0.10692089630086898,
        "abs_return_acf_1": 0.42254591963142074,
        "abs_return_acf_5": 0.49129775428144873,
        "abs_return_acf_20": 0.3635552532761641,
        "quantile_01": -0.0676444925581101,
        "quantile_99": 0.06372836611360888,
        "hill_tail_index": 3.9751220145161623
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0186377509016332,
        "excess_kurtosis": 12.934354898165887,
        "return_acf_1": -0.03700520083290492,
        "abs_return_acf_1": 0.41096757621479046,
        "abs_return_acf_5": 0.4215877565336838,
        "abs_return_acf_20": 0.34922436550944985,
        "quantile_01": -0.05557037565425082,
        "quantile_99": 0.054161329022978634,
        "hill_tail_index": 2.972504021609234
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01927118346724116,
        "excess_kurtosis": 9.293980047710093,
        "return_acf_1": -0.19600224042174244,
        "abs_return_acf_1": 0.38557664522376456,
        "abs_return_acf_5": 0.39581819856983186,
        "abs_return_acf_20": 0.2572636891636812,
        "quantile_01": -0.057155871198030624,
        "quantile_99": 0.06570336302180116,
        "hill_tail_index": 3.180782156633846
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019372622017153344,
        "excess_kurtosis": 7.760624857676083,
        "return_acf_1": -0.2356342094511504,
        "abs_return_acf_1": 0.38284508130253286,
        "abs_return_acf_5": 0.33112580695647365,
        "abs_return_acf_20": 0.27694983865860934,
        "quantile_01": -0.06408063767028797,
        "quantile_99": 0.05318435858838891,
        "hill_tail_index": 3.0806358773102565
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.0172996407261227,
        "excess_kurtosis": 20.05104805359158,
        "return_acf_1": -0.1178777369730686,
        "abs_return_acf_1": 0.31119156752924276,
        "abs_return_acf_5": 0.3667905142457787,
        "abs_return_acf_20": 0.25820455536576803,
        "quantile_01": -0.04408017479903359,
        "quantile_99": 0.04727258379311036,
        "hill_tail_index": 2.981209521962502
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01947975682890805,
        "excess_kurtosis": 5.9515345894947185,
        "return_acf_1": -0.057344206199575545,
        "abs_return_acf_1": 0.31710578729599387,
        "abs_return_acf_5": 0.3204561521573618,
        "abs_return_acf_20": 0.2374857992718934,
        "quantile_01": -0.06314337742433555,
        "quantile_99": 0.06521005142826417,
        "hill_tail_index": 3.3648056936179356
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018874956885846145,
        "excess_kurtosis": 8.863301059581193,
        "return_acf_1": -0.12972678199362925,
        "abs_return_acf_1": 0.36103406732548815,
        "abs_return_acf_5": 0.330169501708128,
        "abs_return_acf_20": 0.3310333453562096,
        "quantile_01": -0.05235976676042684,
        "quantile_99": 0.05441866911765981,
        "hill_tail_index": 2.917074241685817
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018256854426932326,
        "excess_kurtosis": 8.097846661861237,
        "return_acf_1": -0.12476109599162828,
        "abs_return_acf_1": 0.3565065907822008,
        "abs_return_acf_5": 0.3850867511668133,
        "abs_return_acf_20": 0.3489516647433726,
        "quantile_01": -0.059120680762345945,
        "quantile_99": 0.046000516891773965,
        "hill_tail_index": 2.894493467401409
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018491762218571222,
        "excess_kurtosis": 5.307991936033231,
        "return_acf_1": -0.08019469158355744,
        "abs_return_acf_1": 0.3234547257862796,
        "abs_return_acf_5": 0.30676336208627,
        "abs_return_acf_20": 0.22228522662131336,
        "quantile_01": -0.05742494743779049,
        "quantile_99": 0.059718691871851894,
        "hill_tail_index": 4.723561039414312
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018126534655491997,
        "excess_kurtosis": 4.294047844601419,
        "return_acf_1": -0.16152740775917554,
        "abs_return_acf_1": 0.36013415466303583,
        "abs_return_acf_5": 0.343140806284982,
        "abs_return_acf_20": 0.2923831820551254,
        "quantile_01": -0.05238032503654426,
        "quantile_99": 0.05034488135159729,
        "hill_tail_index": 3.7234267024392094
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01853596283082753,
        "excess_kurtosis": 4.761887660473394,
        "return_acf_1": -0.022098896055254714,
        "abs_return_acf_1": 0.27588103890416316,
        "abs_return_acf_5": 0.33055208711931156,
        "abs_return_acf_20": 0.2650439483085057,
        "quantile_01": -0.0530878781405338,
        "quantile_99": 0.054657134309868814,
        "hill_tail_index": 3.158285565029404
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017339812424790012,
        "excess_kurtosis": 14.071927575221174,
        "return_acf_1": -0.014161138326591306,
        "abs_return_acf_1": 0.3715566973867749,
        "abs_return_acf_5": 0.38190354097503315,
        "abs_return_acf_20": 0.32432232740137545,
        "quantile_01": -0.048028532628737554,
        "quantile_99": 0.042446085022955965,
        "hill_tail_index": 1.8590527662204126
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018866470587388856,
        "excess_kurtosis": 4.975264044892849,
        "return_acf_1": -0.0956685982917961,
        "abs_return_acf_1": 0.3759478478062029,
        "abs_return_acf_5": 0.30351634654910487,
        "abs_return_acf_20": 0.32877684837732535,
        "quantile_01": -0.056372395738519446,
        "quantile_99": 0.05794493969136311,
        "hill_tail_index": 3.315846081523982
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018962088030765035,
        "excess_kurtosis": 3.9509750577247313,
        "return_acf_1": -0.08191995037656795,
        "abs_return_acf_1": 0.23266203064416674,
        "abs_return_acf_5": 0.2629793353107128,
        "abs_return_acf_20": 0.2709591044345143,
        "quantile_01": -0.05985809351992341,
        "quantile_99": 0.06005987482697961,
        "hill_tail_index": 5.186763033406784
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01794771671852689,
        "excess_kurtosis": 3.5060288520667973,
        "return_acf_1": -0.12332873240992424,
        "abs_return_acf_1": 0.245912041362553,
        "abs_return_acf_5": 0.3180107500897977,
        "abs_return_acf_20": 0.2298505808893837,
        "quantile_01": -0.051233931644865074,
        "quantile_99": 0.04618142266491089,
        "hill_tail_index": 4.86471285264187
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01940166808682373,
        "excess_kurtosis": 5.232562293180532,
        "return_acf_1": -0.09548958620086873,
        "abs_return_acf_1": 0.39371687644322206,
        "abs_return_acf_5": 0.37544727102451825,
        "abs_return_acf_20": 0.3179244471842634,
        "quantile_01": -0.06348395057063004,
        "quantile_99": 0.05901989167072785,
        "hill_tail_index": 4.027393004886646
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

Firm policy: npv_discrete
Training: False
Coverage status: not_applicable
Unseen state share: None
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
