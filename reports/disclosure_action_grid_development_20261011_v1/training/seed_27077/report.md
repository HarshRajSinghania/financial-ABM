# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27077
Run ID: `bd6a3500ee56d5efbc087fc7b72edb0d23e7dcd57c849fc0587f73936e75a277`
Result fingerprint: `7a626f28a6ea9839ce8297f1b3c1af0e972274e93c07f5f63eb14174fb9437ed`

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
    "equal_weight_sd": -0.5552976190476159,
    "equal_weight_raw": -8.329464285714236,
    "fixed_start_cap_weight_sd": -0.5378579947922372,
    "fixed_start_cap_weight_raw": -8.067869921883556,
    "end_cap_weight_sd": -0.5400104281025957,
    "end_cap_weight_raw": -8.100156421538935
  },
  "full_period_change": {
    "equal_weight_sd": -0.8959047619047571,
    "equal_weight_raw": -13.438571428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8437718253968208,
    "inflation_mean_sd": 0.5729804894179894
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.39708333333333656,
    "equal_weight_raw": 5.956250000000049,
    "fixed_start_cap_weight_sd": 0.41452295758871505,
    "fixed_start_cap_weight_raw": 6.217844363830726,
    "end_cap_weight_sd": 0.4123705242783567,
    "end_cap_weight_raw": 6.185557864175351
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.599047619047616,
      "change_raw": -8.985714285714241,
      "decay_adjusted_gain_sd": 0.35333333333333633
    },
    "mid": {
      "count": 9,
      "change_sd": -0.557658730158727,
      "change_raw": -8.364880952380906,
      "decay_adjusted_gain_sd": 0.3947222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.5468253968253936,
      "change_raw": -8.202380952380903,
      "decay_adjusted_gain_sd": 0.4055555555555587
    },
    "large_minus_small_sd": -0.0522222222222225,
    "large_minus_small_raw": -0.7833333333333375
  },
  "inflation": {
    "initial_mean_sd": 0.25675,
    "final_mean_sd": 0.6036666666666667,
    "mean_sd": 0.44411906744379687,
    "mean_absolute_raw_gap": 6.661786011656952,
    "final_absolute_raw_gap": 9.055,
    "mean_range_fraction": 0.06661786011656952
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.24373562321614872,
    "final_wealth_share": 0.3108454869376869
  },
  "pricing_slope": {
    "mean": -0.0009464759453931299,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.10300760635887299,
    "real_improvement_cost": 0.07486487438592046,
    "washing_cost": 0.02814273197295252,
    "fine_transfer": 0.03855188840195535,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.14155949476082835,
    "resource_cost_fraction_initial_cap": 0.003433586878629099,
    "private_net_outflow_fraction_initial_cap": 0.004718649825360944,
    "fine_transfer_fraction_initial_cap": 0.0012850629467318446,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002587441660004501,
    "unapplied_final_day_resource_cost": 0.0024809211866588386
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 115.64679950427724,
    "beneficial_raw_gain_per_resource_cost": 1734.7019925641584,
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
    "accrued_cost": 3.0868932822132513,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.11070280602277434,
    "accrued_cost_fraction_initial_cap": 0.10289644274044168,
    "mean_contract_rate": 0.04296009665006803,
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
    "maximum_relative_cash_error": 1.7309907292054305e-15,
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
      "minimum": -0.18530312907822974,
      "maximum": -0.08767739168126058,
      "mean": -0.13089807400723363,
      "median": -0.13350548046603614,
      "quantile_05": -0.16427935081922523,
      "quantile_95": -0.09438857640650779
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
      "minimum": 0.30846714140705445,
      "maximum": 0.8197535198840675,
      "mean": 0.6192053507770524,
      "median": 0.6349263831187433,
      "quantile_05": 0.41022519453361384,
      "quantile_95": 0.787553389984481
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
        "daily_volatility": 0.02081658688107923,
        "excess_kurtosis": 9.8095252770448,
        "return_acf_1": -0.18530312907822974,
        "abs_return_acf_1": 0.4014543189345819,
        "abs_return_acf_5": 0.34913039590073147,
        "abs_return_acf_20": 0.3036650293977915,
        "quantile_01": -0.07997794582495833,
        "quantile_99": 0.048457576151818706,
        "hill_tail_index": 2.2917264599532596
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024336101999904894,
        "excess_kurtosis": 16.721785944020024,
        "return_acf_1": -0.14480427108275776,
        "abs_return_acf_1": 0.4202732185950345,
        "abs_return_acf_5": 0.4372760538466251,
        "abs_return_acf_20": 0.40874156129241024,
        "quantile_01": -0.08190143450600451,
        "quantile_99": 0.07968963075203014,
        "hill_tail_index": 2.702828929541068
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022600562471529004,
        "excess_kurtosis": 8.744230314630464,
        "return_acf_1": -0.13559640543454687,
        "abs_return_acf_1": 0.4571378966456757,
        "abs_return_acf_5": 0.44170218895361796,
        "abs_return_acf_20": 0.39031872115009947,
        "quantile_01": -0.08969510666289292,
        "quantile_99": 0.06438545443353921,
        "hill_tail_index": 3.4996475831375666
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02190828832500237,
        "excess_kurtosis": 9.464344782551628,
        "return_acf_1": -0.15563444976605714,
        "abs_return_acf_1": 0.38977823488867497,
        "abs_return_acf_5": 0.36086684016466003,
        "abs_return_acf_20": 0.32534944368465,
        "quantile_01": -0.09080254016266041,
        "quantile_99": 0.05442472999744095,
        "hill_tail_index": 2.7621520790284104
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022665756814086436,
        "excess_kurtosis": 9.464130041121301,
        "return_acf_1": -0.15997172093688247,
        "abs_return_acf_1": 0.4677057165150358,
        "abs_return_acf_5": 0.3742667819832624,
        "abs_return_acf_20": 0.3654006180249756,
        "quantile_01": -0.07846335759917708,
        "quantile_99": 0.06266011724661068,
        "hill_tail_index": 3.0871453935978486
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02033996313561259,
        "excess_kurtosis": 7.361888637874545,
        "return_acf_1": -0.10241770871384707,
        "abs_return_acf_1": 0.398430182623696,
        "abs_return_acf_5": 0.3887087779923999,
        "abs_return_acf_20": 0.3228179406111687,
        "quantile_01": -0.06947881140296001,
        "quantile_99": 0.05438192412082186,
        "hill_tail_index": 3.486152565839433
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022282643518763873,
        "excess_kurtosis": 10.785786066586546,
        "return_acf_1": -0.12775682147889103,
        "abs_return_acf_1": 0.4009840107603569,
        "abs_return_acf_5": 0.3897507375420829,
        "abs_return_acf_20": 0.28725844619310154,
        "quantile_01": -0.07820524288866416,
        "quantile_99": 0.0580379209548459,
        "hill_tail_index": 3.205463062905784
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020254182798712297,
        "excess_kurtosis": 6.793272932365873,
        "return_acf_1": -0.13384891691350664,
        "abs_return_acf_1": 0.3894558563073355,
        "abs_return_acf_5": 0.3969583115959036,
        "abs_return_acf_20": 0.3644411884379337,
        "quantile_01": -0.07105365387170089,
        "quantile_99": 0.05359227133184765,
        "hill_tail_index": 3.343450646569453
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019582364161589077,
        "excess_kurtosis": 14.438213436216781,
        "return_acf_1": -0.13969435224558388,
        "abs_return_acf_1": 0.32703129278364995,
        "abs_return_acf_5": 0.3227906689954222,
        "abs_return_acf_20": 0.28316392304811,
        "quantile_01": -0.05185178029383169,
        "quantile_99": 0.054491868487243,
        "hill_tail_index": 2.4143694138039797
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020477581926858647,
        "excess_kurtosis": 7.037068633253838,
        "return_acf_1": -0.124802603514704,
        "abs_return_acf_1": 0.3848515737097103,
        "abs_return_acf_5": 0.37168889105798614,
        "abs_return_acf_20": 0.319337013268528,
        "quantile_01": -0.07391354211900901,
        "quantile_99": 0.06519609408462299,
        "hill_tail_index": 4.533189527858898
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022032691739673173,
        "excess_kurtosis": 9.604670915595237,
        "return_acf_1": -0.10441613561121099,
        "abs_return_acf_1": 0.41594487228659677,
        "abs_return_acf_5": 0.4011833364107255,
        "abs_return_acf_20": 0.3085815110621452,
        "quantile_01": -0.07010018271978076,
        "quantile_99": 0.055266949780197555,
        "hill_tail_index": 2.31543309250073
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022396995933899492,
        "excess_kurtosis": 9.306421973502102,
        "return_acf_1": -0.14131839894997925,
        "abs_return_acf_1": 0.48222673610682365,
        "abs_return_acf_5": 0.4138876690691223,
        "abs_return_acf_20": 0.31890311277550754,
        "quantile_01": -0.08079220845562976,
        "quantile_99": 0.06785152309992913,
        "hill_tail_index": 3.5921448338999538
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020565617861925407,
        "excess_kurtosis": 10.839206325283667,
        "return_acf_1": -0.15279828137493756,
        "abs_return_acf_1": 0.44946523757645196,
        "abs_return_acf_5": 0.4092282552231983,
        "abs_return_acf_20": 0.2850252879455279,
        "quantile_01": -0.0665051951799765,
        "quantile_99": 0.04877363035570504,
        "hill_tail_index": 2.3547721212286494
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018391984825674484,
        "excess_kurtosis": 6.986486413273688,
        "return_acf_1": -0.09201415161207205,
        "abs_return_acf_1": 0.27980218451008,
        "abs_return_acf_5": 0.19408596251713345,
        "abs_return_acf_20": 0.2509713629548267,
        "quantile_01": -0.05119957038271754,
        "quantile_99": 0.05136734330676327,
        "hill_tail_index": 2.83055291633856
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02153995554055551,
        "excess_kurtosis": 22.258606157360223,
        "return_acf_1": -0.08767739168126058,
        "abs_return_acf_1": 0.37564342232111886,
        "abs_return_acf_5": 0.3503264159863393,
        "abs_return_acf_20": 0.27814586262771784,
        "quantile_01": -0.06230686934958004,
        "quantile_99": 0.0489413595076983,
        "hill_tail_index": 2.0143859496063254
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021103371067833443,
        "excess_kurtosis": 14.784254177372645,
        "return_acf_1": -0.11267509685875661,
        "abs_return_acf_1": 0.39064504588110904,
        "abs_return_acf_5": 0.36933077262984204,
        "abs_return_acf_20": 0.28626738065819407,
        "quantile_01": -0.0732455428557651,
        "quantile_99": 0.06816288915192337,
        "hill_tail_index": 2.8922124331385897
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02155752143890327,
        "excess_kurtosis": 7.921568172981491,
        "return_acf_1": -0.10260228671927395,
        "abs_return_acf_1": 0.38454244427157963,
        "abs_return_acf_5": 0.4439329142559733,
        "abs_return_acf_20": 0.3188729679493378,
        "quantile_01": -0.07903508680334485,
        "quantile_99": 0.05757897027880605,
        "hill_tail_index": 4.544032222869538
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.023080777692023845,
        "excess_kurtosis": 11.211148192327974,
        "return_acf_1": -0.11311215231808137,
        "abs_return_acf_1": 0.38985955565113056,
        "abs_return_acf_5": 0.3700041699689211,
        "abs_return_acf_20": 0.3333454520574501,
        "quantile_01": -0.07572065777002245,
        "quantile_99": 0.06937296552632127,
        "hill_tail_index": 2.9199511017955317
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023248476488597156,
        "excess_kurtosis": 14.823645067207579,
        "return_acf_1": -0.14907366597329,
        "abs_return_acf_1": 0.41720549699181025,
        "abs_return_acf_5": 0.4498622135710179,
        "abs_return_acf_20": 0.3434331569973051,
        "quantile_01": -0.06821881943659752,
        "quantile_99": 0.0699253039092792,
        "hill_tail_index": 2.6581620557574723
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02089798378992337,
        "excess_kurtosis": 9.769849817710657,
        "return_acf_1": -0.15833967428216328,
        "abs_return_acf_1": 0.4358527372230258,
        "abs_return_acf_5": 0.44104465830330636,
        "abs_return_acf_20": 0.36731930425791093,
        "quantile_01": -0.07307193470699143,
        "quantile_99": 0.058583927348727485,
        "hill_tail_index": 2.800072585062904
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02038522299072742,
        "excess_kurtosis": 8.038647028635332,
        "return_acf_1": -0.10849095366363457,
        "abs_return_acf_1": 0.38829702322791,
        "abs_return_acf_5": 0.44872058412029,
        "abs_return_acf_20": 0.3746535962881576,
        "quantile_01": -0.06777837694584936,
        "quantile_99": 0.05366106794680071,
        "hill_tail_index": 2.990777661257074
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022123181774773293,
        "excess_kurtosis": 10.427949740728257,
        "return_acf_1": -0.11657305028478697,
        "abs_return_acf_1": 0.34269386108844774,
        "abs_return_acf_5": 0.3220223740495481,
        "abs_return_acf_20": 0.31845793801852545,
        "quantile_01": -0.08262032835347975,
        "quantile_99": 0.06228450377800068,
        "hill_tail_index": 3.224469637455694
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021763457212427506,
        "excess_kurtosis": 8.700529781318055,
        "return_acf_1": -0.16780377526841475,
        "abs_return_acf_1": 0.4316931346212708,
        "abs_return_acf_5": 0.35163211653601856,
        "abs_return_acf_20": 0.3565620816727934,
        "quantile_01": -0.08531429987384007,
        "quantile_99": 0.05869184963469573,
        "hill_tail_index": 2.967921966839891
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020481580447441083,
        "excess_kurtosis": 7.125963418406684,
        "return_acf_1": -0.15706258769748804,
        "abs_return_acf_1": 0.35384008816878104,
        "abs_return_acf_5": 0.32207051584462143,
        "abs_return_acf_20": 0.30874767990012564,
        "quantile_01": -0.06582000439471221,
        "quantile_99": 0.05165365918419314,
        "hill_tail_index": 3.023890181074697
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01904501097758657,
        "excess_kurtosis": 5.7837810547364725,
        "return_acf_1": -0.10743926517777476,
        "abs_return_acf_1": 0.3743038815146335,
        "abs_return_acf_5": 0.28766101989520576,
        "abs_return_acf_20": 0.2532831665302985,
        "quantile_01": -0.0614240431961509,
        "quantile_99": 0.05283613540764154,
        "hill_tail_index": 3.640165969735678
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018198104678489663,
        "excess_kurtosis": 9.402261130925595,
        "return_acf_1": -0.13316204401856563,
        "abs_return_acf_1": 0.3240695694892707,
        "abs_return_acf_5": 0.2745593195271285,
        "abs_return_acf_20": 0.30571805599465723,
        "quantile_01": -0.05132633616707066,
        "quantile_99": 0.04799373324710623,
        "hill_tail_index": 2.918966796076811
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02260353821589124,
        "excess_kurtosis": 10.488212889277731,
        "return_acf_1": -0.13617827391987103,
        "abs_return_acf_1": 0.4398489753416521,
        "abs_return_acf_5": 0.41902730845415864,
        "abs_return_acf_20": 0.3032586008785497,
        "quantile_01": -0.0805451648947305,
        "quantile_99": 0.07003692474806945,
        "hill_tail_index": 3.1099323273897883
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022169233814174197,
        "excess_kurtosis": 8.41885318991574,
        "return_acf_1": -0.12570919044165585,
        "abs_return_acf_1": 0.41045118487596505,
        "abs_return_acf_5": 0.3655207034314078,
        "abs_return_acf_20": 0.3476311245064811,
        "quantile_01": -0.08740666795721508,
        "quantile_99": 0.0627994550265777,
        "hill_tail_index": 3.6969287676594003
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020311561878451238,
        "excess_kurtosis": 7.977275256645777,
        "return_acf_1": -0.1533748140435226,
        "abs_return_acf_1": 0.38025202392489144,
        "abs_return_acf_5": 0.3419466790499237,
        "abs_return_acf_20": 0.3357302410974893,
        "quantile_01": -0.07348819473515648,
        "quantile_99": 0.05600828848584257,
        "hill_tail_index": 2.915477413940614
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019898059988275058,
        "excess_kurtosis": 7.852080149523415,
        "return_acf_1": -0.09729065115526256,
        "abs_return_acf_1": 0.41951645776585694,
        "abs_return_acf_5": 0.3959741060434271,
        "abs_return_acf_20": 0.3608416789524164,
        "quantile_01": -0.06573703386841322,
        "quantile_99": 0.06025674130597449,
        "hill_tail_index": 3.4418572636126172
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
