# Disclosure-market run

Purpose: development
Domain: esg
Seed: 25101
Run ID: `58baadae0c3df17e1053d337bf6d7d4d7049671ffaf677205ec968edd3531468`
Result fingerprint: `2c4c90d88a1b94c73b3f1127a611b6b9109923fb30d1419869ce6a53cbdb2104`

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
    "equal_weight_sd": -0.9407142857142826,
    "equal_weight_raw": -14.110714285714236,
    "fixed_start_cap_weight_sd": -0.937026955361782,
    "fixed_start_cap_weight_raw": -14.055404330426732,
    "end_cap_weight_sd": -0.9367535947722829,
    "end_cap_weight_raw": -14.05130392158424
  },
  "full_period_change": {
    "equal_weight_sd": -1.4130714285714239,
    "equal_weight_raw": -21.196071428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.314914021164017,
    "inflation_mean_sd": 0.0037500000000000003
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.011666666666669715,
    "equal_weight_raw": 0.17500000000004565,
    "fixed_start_cap_weight_sd": 0.015353997019170465,
    "fixed_start_cap_weight_raw": 0.230309955287557,
    "end_cap_weight_sd": 0.015627357608669786,
    "end_cap_weight_raw": 0.23441036413004682
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.952380952380949,
      "change_raw": -14.285714285714235,
      "decay_adjusted_gain_sd": 3.1826393372587822e-15
    },
    "mid": {
      "count": 9,
      "change_sd": -0.919325396825394,
      "change_raw": -13.78988095238091,
      "decay_adjusted_gain_sd": 0.03305555555555828
    },
    "small": {
      "count": 18,
      "change_sd": -0.9494642857142824,
      "change_raw": -14.241964285714236,
      "decay_adjusted_gain_sd": 0.0029166666666698535
    },
    "large_minus_small_sd": -0.0029166666666665675,
    "large_minus_small_raw": -0.04374999999999851
  },
  "inflation": {
    "initial_mean_sd": 0.002,
    "final_mean_sd": 0.0037500000000000003,
    "mean_sd": 0.0031338467943380515,
    "mean_absolute_raw_gap": 0.04700770191507056,
    "final_absolute_raw_gap": 0.05624999999999988,
    "mean_range_fraction": 0.0004700770191507056
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.24666666666666667,
    "initial_wealth_share": 0.22012869592943937,
    "final_wealth_share": 0.25235758072628833
  },
  "pricing_slope": {
    "mean": -0.0029002857599479863,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 1.101716387069307e-05,
    "real_improvement_cost": 1.0257280618247745e-05,
    "washing_cost": 7.59883252445325e-07,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 1.101716387069307e-05,
    "resource_cost_fraction_initial_cap": 3.67238795689769e-07,
    "private_net_outflow_fraction_initial_cap": 3.67238795689769e-07,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 1.0336426205001636e-06,
    "unapplied_final_day_resource_cost": 3.9796691446164236e-07
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 31768.61160530905,
    "beneficial_raw_gain_per_resource_cost": 476529.1740796358,
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
    "fixed_exposure": 14.999999999999998,
    "accrued_cost": 3.4334025358675433,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.4572120596770672,
    "accrued_cost_fraction_initial_cap": 0.11444675119558478,
    "mean_contract_rate": 0.04635237875819871,
    "maximum_ledger_error": 1.3552527156068805e-19
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
    "maximum_relative_cash_error": 1.4416362313468155e-15,
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
      "minimum": -0.21391683489140556,
      "maximum": -0.08046331385951411,
      "mean": -0.15480954842032527,
      "median": -0.14578488046361804,
      "quantile_05": -0.204223988862512,
      "quantile_95": -0.10267944344628306
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
      "minimum": 0.3131376601547985,
      "maximum": 0.7932720607339109,
      "mean": 0.5404177264434386,
      "median": 0.5525669395857868,
      "quantile_05": 0.3596553913530658,
      "quantile_95": 0.7312654314397605
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
        "daily_volatility": 0.017752364227245434,
        "excess_kurtosis": 3.0721424014127043,
        "return_acf_1": -0.20442505865189592,
        "abs_return_acf_1": 0.31572543045057555,
        "abs_return_acf_5": 0.2713235978950116,
        "abs_return_acf_20": 0.25419641770317764,
        "quantile_01": -0.050194441167572684,
        "quantile_99": 0.04823670361450954,
        "hill_tail_index": 3.9332574933989384
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018228158595251138,
        "excess_kurtosis": 5.784504619637628,
        "return_acf_1": -0.15350561523200035,
        "abs_return_acf_1": 0.23431249357084338,
        "abs_return_acf_5": 0.17940239788535384,
        "abs_return_acf_20": 0.15372324213442257,
        "quantile_01": -0.053561961325620064,
        "quantile_99": 0.0466992429570838,
        "hill_tail_index": 3.761081910913355
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020645392773706053,
        "excess_kurtosis": 9.636191374596857,
        "return_acf_1": -0.08046331385951411,
        "abs_return_acf_1": 0.3518877860206334,
        "abs_return_acf_5": 0.3957527842421969,
        "abs_return_acf_20": 0.2676777222659133,
        "quantile_01": -0.07072677399934182,
        "quantile_99": 0.0655005022479073,
        "hill_tail_index": 2.7935652409111444
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01856143428671841,
        "excess_kurtosis": 6.842369234183794,
        "return_acf_1": -0.19579448242645925,
        "abs_return_acf_1": 0.33336292437289167,
        "abs_return_acf_5": 0.33936167807536366,
        "abs_return_acf_20": 0.2557412701597766,
        "quantile_01": -0.06028497739632548,
        "quantile_99": 0.05658585720513471,
        "hill_tail_index": 3.533859928611699
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019380640278281756,
        "excess_kurtosis": 9.134671417492367,
        "return_acf_1": -0.148860270828278,
        "abs_return_acf_1": 0.319626886448193,
        "abs_return_acf_5": 0.2863945404654863,
        "abs_return_acf_20": 0.1826136618843183,
        "quantile_01": -0.050930175767278624,
        "quantile_99": 0.05074006121230277,
        "hill_tail_index": 3.1321813868196773
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01778754053729819,
        "excess_kurtosis": 3.2422536703848834,
        "return_acf_1": -0.1621546326756631,
        "abs_return_acf_1": 0.2772478859152499,
        "abs_return_acf_5": 0.250727835695852,
        "abs_return_acf_20": 0.26727117106036896,
        "quantile_01": -0.04803523303768604,
        "quantile_99": 0.05024320860794665,
        "hill_tail_index": 3.258522389055646
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017711281584500294,
        "excess_kurtosis": 22.665216411794265,
        "return_acf_1": -0.13720408969691597,
        "abs_return_acf_1": 0.2787074903080082,
        "abs_return_acf_5": 0.2946422583350378,
        "abs_return_acf_20": 0.12726622595723636,
        "quantile_01": -0.04771787386547592,
        "quantile_99": 0.04048491111519492,
        "hill_tail_index": 1.9892260721322974
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018736177559308825,
        "excess_kurtosis": 35.047450176758154,
        "return_acf_1": -0.14464676720986247,
        "abs_return_acf_1": 0.3249320839035659,
        "abs_return_acf_5": 0.3112343058347309,
        "abs_return_acf_20": 0.17450405062765004,
        "quantile_01": -0.045950912712660476,
        "quantile_99": 0.04039053353707576,
        "hill_tail_index": 2.061551354838032
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01870591663710026,
        "excess_kurtosis": 4.936742858358096,
        "return_acf_1": -0.21391683489140556,
        "abs_return_acf_1": 0.3623241174222663,
        "abs_return_acf_5": 0.3253284239790192,
        "abs_return_acf_20": 0.2665963181154541,
        "quantile_01": -0.051809721909579706,
        "quantile_99": 0.05193663480814878,
        "hill_tail_index": 3.8102983832208
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020899605857853453,
        "excess_kurtosis": 13.983626421504379,
        "return_acf_1": -0.1316614235894289,
        "abs_return_acf_1": 0.33203935936497686,
        "abs_return_acf_5": 0.34592946331382257,
        "abs_return_acf_20": 0.18518167812430217,
        "quantile_01": -0.06796995751247346,
        "quantile_99": 0.060460265140259435,
        "hill_tail_index": 3.214520824159528
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01946059751466843,
        "excess_kurtosis": 9.96683804471905,
        "return_acf_1": -0.20397823689770944,
        "abs_return_acf_1": 0.36192871412030075,
        "abs_return_acf_5": 0.27814562181783503,
        "abs_return_acf_20": 0.2315834429200144,
        "quantile_01": -0.06622631664410006,
        "quantile_99": 0.05956865544852577,
        "hill_tail_index": 2.9660503070042323
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01866872915990614,
        "excess_kurtosis": 29.24914777428142,
        "return_acf_1": -0.1449387745975055,
        "abs_return_acf_1": 0.40015638678314125,
        "abs_return_acf_5": 0.41043075582663563,
        "abs_return_acf_20": 0.18877839083717723,
        "quantile_01": -0.05456829854224836,
        "quantile_99": 0.037352883895898734,
        "hill_tail_index": 1.9593472517334487
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01762175517638165,
        "excess_kurtosis": 6.430172590973397,
        "return_acf_1": -0.12583322017842605,
        "abs_return_acf_1": 0.33945230115843555,
        "abs_return_acf_5": 0.23231219132218647,
        "abs_return_acf_20": 0.18326185583563392,
        "quantile_01": -0.05319360189036514,
        "quantile_99": 0.04632570662628931,
        "hill_tail_index": 3.579155573237286
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017923016999128894,
        "excess_kurtosis": 6.262445047359208,
        "return_acf_1": -0.17391342280738226,
        "abs_return_acf_1": 0.3012382867060666,
        "abs_return_acf_5": 0.22589768634156857,
        "abs_return_acf_20": 0.23379250965938728,
        "quantile_01": -0.04692660891259625,
        "quantile_99": 0.04686977691578248,
        "hill_tail_index": 2.4428725894286427
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018921307792513338,
        "excess_kurtosis": 15.32606686365552,
        "return_acf_1": -0.1430607714269633,
        "abs_return_acf_1": 0.31420137939876963,
        "abs_return_acf_5": 0.29914239023791467,
        "abs_return_acf_20": 0.20955961802602013,
        "quantile_01": -0.04666152467911273,
        "quantile_99": 0.04632638689158159,
        "hill_tail_index": 2.431633164388984
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018544110907695067,
        "excess_kurtosis": 29.62491296814006,
        "return_acf_1": -0.1833052806084508,
        "abs_return_acf_1": 0.3176616413110025,
        "abs_return_acf_5": 0.2864786664368388,
        "abs_return_acf_20": 0.14569225821572468,
        "quantile_01": -0.04123227801456342,
        "quantile_99": 0.04202263328429771,
        "hill_tail_index": 1.8097753579967004
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018012932792084685,
        "excess_kurtosis": 5.088512440350268,
        "return_acf_1": -0.08373544430180221,
        "abs_return_acf_1": 0.28449577423829664,
        "abs_return_acf_5": 0.34945800459910514,
        "abs_return_acf_20": 0.24442071678841573,
        "quantile_01": -0.05329982864828458,
        "quantile_99": 0.051054303359425485,
        "hill_tail_index": 4.009880520868333
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017654712552469084,
        "excess_kurtosis": 4.025044706987654,
        "return_acf_1": -0.1352066045355502,
        "abs_return_acf_1": 0.26709187358247455,
        "abs_return_acf_5": 0.29437620795653424,
        "abs_return_acf_20": 0.18415887377432566,
        "quantile_01": -0.04924809618365988,
        "quantile_99": 0.052622751066588605,
        "hill_tail_index": 3.781426100865207
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019217538866574548,
        "excess_kurtosis": 7.506654152304572,
        "return_acf_1": -0.12803867094905985,
        "abs_return_acf_1": 0.3875068973066974,
        "abs_return_acf_5": 0.2790860078478638,
        "abs_return_acf_20": 0.26473243920131845,
        "quantile_01": -0.06529737329287749,
        "quantile_99": 0.05396080783629449,
        "hill_tail_index": 2.929233438118589
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017707004641646845,
        "excess_kurtosis": 16.759967861752898,
        "return_acf_1": -0.16290688223319488,
        "abs_return_acf_1": 0.34235644324795284,
        "abs_return_acf_5": 0.32556140632054836,
        "abs_return_acf_20": 0.16718562274248272,
        "quantile_01": -0.048627454040509235,
        "quantile_99": 0.039556495393775065,
        "hill_tail_index": 2.0785275173840936
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01785622447450206,
        "excess_kurtosis": 6.198199086924554,
        "return_acf_1": -0.18012907824202926,
        "abs_return_acf_1": 0.38983506406232754,
        "abs_return_acf_5": 0.2662301430537607,
        "abs_return_acf_20": 0.1945726755552202,
        "quantile_01": -0.0539602053222328,
        "quantile_99": 0.052085563382073506,
        "hill_tail_index": 4.341633800280244
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018922368007041862,
        "excess_kurtosis": 28.05385321498255,
        "return_acf_1": -0.19644956936120037,
        "abs_return_acf_1": 0.2393836292494901,
        "abs_return_acf_5": 0.2789313791504662,
        "abs_return_acf_20": 0.16898875475115827,
        "quantile_01": -0.05808610686685729,
        "quantile_99": 0.0456482629259047,
        "hill_tail_index": 2.420261241346898
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018857008063579702,
        "excess_kurtosis": 17.57799657623913,
        "return_acf_1": -0.13372326874648513,
        "abs_return_acf_1": 0.3443290724062113,
        "abs_return_acf_5": 0.3429302810629421,
        "abs_return_acf_20": 0.19580651316657927,
        "quantile_01": -0.06138076004810839,
        "quantile_99": 0.05093684176756393,
        "hill_tail_index": 2.520835376917218
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018544319466330308,
        "excess_kurtosis": 6.0321143810594435,
        "return_acf_1": -0.13885526178375757,
        "abs_return_acf_1": 0.2580314035711275,
        "abs_return_acf_5": 0.27588528749743313,
        "abs_return_acf_20": 0.27194946053120667,
        "quantile_01": -0.05664511172795697,
        "quantile_99": 0.05342837944004032,
        "hill_tail_index": 2.6233304103166746
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019063667376831107,
        "excess_kurtosis": 12.655949539363021,
        "return_acf_1": -0.13446523794636678,
        "abs_return_acf_1": 0.22768357624733357,
        "abs_return_acf_5": 0.236068418136116,
        "abs_return_acf_20": 0.19173730021249968,
        "quantile_01": -0.06314474625688236,
        "quantile_99": 0.04768608612104696,
        "hill_tail_index": 2.7142422727383893
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01961626492345761,
        "excess_kurtosis": 3.9252735477836893,
        "return_acf_1": -0.14663098632973057,
        "abs_return_acf_1": 0.3164713749924157,
        "abs_return_acf_5": 0.32407013136561197,
        "abs_return_acf_20": 0.2855137554647822,
        "quantile_01": -0.05492542680543781,
        "quantile_99": 0.05617520531167206,
        "hill_tail_index": 4.1951993257745235
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01798682888520866,
        "excess_kurtosis": 26.618978757294038,
        "return_acf_1": -0.19532778709894005,
        "abs_return_acf_1": 0.2967702658960457,
        "abs_return_acf_5": 0.2531242641111472,
        "abs_return_acf_20": 0.17026594209365956,
        "quantile_01": -0.042516058270964885,
        "quantile_99": 0.04565414136928335,
        "hill_tail_index": 1.8853678730442849
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020493416610434228,
        "excess_kurtosis": 13.893904680362958,
        "return_acf_1": -0.14381290887120118,
        "abs_return_acf_1": 0.3335489903810919,
        "abs_return_acf_5": 0.27663770587630043,
        "abs_return_acf_20": 0.18275127102194888,
        "quantile_01": -0.05598880103182812,
        "quantile_99": 0.05604914932566224,
        "hill_tail_index": 2.4952629010912193
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019386023052636127,
        "excess_kurtosis": 7.712799380122615,
        "return_acf_1": -0.1319551945128372,
        "abs_return_acf_1": 0.2878135947932137,
        "abs_return_acf_5": 0.27944528955641074,
        "abs_return_acf_20": 0.24596371215094145,
        "quantile_01": -0.06100329346731366,
        "quantile_99": 0.053316796124937095,
        "hill_tail_index": 3.6162144373541762
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01969333894014238,
        "excess_kurtosis": 5.54276360442174,
        "return_acf_1": -0.18538736211974152,
        "abs_return_acf_1": 0.2886611608390557,
        "abs_return_acf_5": 0.2770502415665475,
        "abs_return_acf_20": 0.21469632956596665,
        "quantile_01": -0.05864677629828666,
        "quantile_99": 0.055380991837774285,
        "hill_tail_index": 3.5621787560624325
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
Training: False
Coverage status: FAIL
Unseen state share: 0.052222222222222225
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
