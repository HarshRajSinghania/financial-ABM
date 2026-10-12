# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27196
Run ID: `53aa3134240b94822d753575393c6617016ae9c934c389c79da07d1419f6a666`
Result fingerprint: `1799d43232c828d1526aaaf45d13ceacd42a131eca1457ebb7f2ca5797a7e68e`

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
    "equal_weight_sd": -0.7434642857142826,
    "equal_weight_raw": -11.151964285714238,
    "fixed_start_cap_weight_sd": -0.7365848362477424,
    "fixed_start_cap_weight_raw": -11.048772543716133,
    "end_cap_weight_sd": -0.7440731707966289,
    "end_cap_weight_raw": -11.16109756194943
  },
  "full_period_change": {
    "equal_weight_sd": -1.1492380952380905,
    "equal_weight_raw": -17.23857142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0734007936507892,
    "inflation_mean_sd": 0.8649570105820105
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2089166666666697,
    "equal_weight_raw": 3.1337500000000458,
    "fixed_start_cap_weight_sd": 0.21579611613320998,
    "fixed_start_cap_weight_raw": 3.2369417419981503,
    "end_cap_weight_sd": 0.20830778158432334,
    "end_cap_weight_raw": 3.124616723764849
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5973809523809493,
      "change_raw": -8.960714285714241,
      "decay_adjusted_gain_sd": 0.3550000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.831269841269838,
      "change_raw": -12.46904761904757,
      "decay_adjusted_gain_sd": 0.12111111111111425
    },
    "small": {
      "count": 18,
      "change_sd": -0.723908730158727,
      "change_raw": -10.858630952380906,
      "decay_adjusted_gain_sd": 0.2284722222222252
    },
    "large_minus_small_sd": 0.12652777777777768,
    "large_minus_small_raw": 1.8979166666666654
  },
  "inflation": {
    "initial_mean_sd": 0.4336666666666667,
    "final_mean_sd": 0.9262499999999999,
    "mean_sd": 0.7165483624757147,
    "mean_absolute_raw_gap": 10.748225437135721,
    "final_absolute_raw_gap": 13.893749999999999,
    "mean_range_fraction": 0.10748225437135721
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.2866666666666667,
    "initial_wealth_share": 0.29739395852967954,
    "final_wealth_share": 0.32532210118096244
  },
  "pricing_slope": {
    "mean": -0.003951015514146906,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.06916857996303526,
    "real_improvement_cost": 0.04957098490184247,
    "washing_cost": 0.0195975950611928,
    "fine_transfer": 0.048759008015884904,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11792758797892017,
    "resource_cost_fraction_initial_cap": 0.002305619332101175,
    "private_net_outflow_fraction_initial_cap": 0.003930919599297339,
    "fine_transfer_fraction_initial_cap": 0.0016253002671961635,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0007411850656655251,
    "unapplied_final_day_resource_cost": 0.007280087498728409
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 90.61195131300279,
    "beneficial_raw_gain_per_resource_cost": 1359.1792696950417,
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
    "accrued_cost": 2.9538801053864177,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.02231037080405844,
    "accrued_cost_fraction_initial_cap": 0.09846267017954725,
    "mean_contract_rate": 0.0415413105177322,
    "maximum_ledger_error": 5.886878983417387e-20
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
    "price_cap_hits": 12,
    "maximum_relative_cash_error": 2.50754454985281e-15,
    "maximum_absolute_share_error": 2.3314683517128287e-15,
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
      "minimum": -0.20799740932423585,
      "maximum": 0.03682909439909535,
      "mean": -0.06699450826113393,
      "median": -0.0553001528797364,
      "quantile_05": -0.16882400756624497,
      "quantile_95": 0.0242286488072722
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
      "minimum": 0.3585821862920143,
      "maximum": 0.8700360942296855,
      "mean": 0.6365015111281537,
      "median": 0.6624680239796477,
      "quantile_05": 0.393416259737813,
      "quantile_95": 0.847256150167153
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
        "daily_volatility": 0.027912078725728193,
        "excess_kurtosis": 21.762405901610112,
        "return_acf_1": -0.029626530866195086,
        "abs_return_acf_1": 0.4373820365889301,
        "abs_return_acf_5": 0.32919260750885776,
        "abs_return_acf_20": 0.3455851098572975,
        "quantile_01": -0.10674670568134942,
        "quantile_99": 0.08525406449894204,
        "hill_tail_index": 2.5912324553659176
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.026893614193932824,
        "excess_kurtosis": 21.9275366722419,
        "return_acf_1": -0.06464207929818228,
        "abs_return_acf_1": 0.4202094804258366,
        "abs_return_acf_5": 0.28964851512613604,
        "abs_return_acf_20": 0.27299222698821457,
        "quantile_01": -0.08780528874777213,
        "quantile_99": 0.08063776377317391,
        "hill_tail_index": 2.4240741796935987
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02685485777944403,
        "excess_kurtosis": 31.541708985466357,
        "return_acf_1": 0.012288954489798375,
        "abs_return_acf_1": 0.41140689798998614,
        "abs_return_acf_5": 0.21353976909513891,
        "abs_return_acf_20": 0.20834827787503699,
        "quantile_01": -0.0848058526623064,
        "quantile_99": 0.05912813134015149,
        "hill_tail_index": 1.885644511080218
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.026387308351475642,
        "excess_kurtosis": 30.976310260804894,
        "return_acf_1": -0.014655267860577725,
        "abs_return_acf_1": 0.3578825095498822,
        "abs_return_acf_5": 0.263016503667031,
        "abs_return_acf_20": 0.24442662936814205,
        "quantile_01": -0.08261558874900976,
        "quantile_99": 0.06763435133724761,
        "hill_tail_index": 2.15113256466753
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.026532209214036585,
        "excess_kurtosis": 23.115621441530063,
        "return_acf_1": -0.045958226461290524,
        "abs_return_acf_1": 0.38868255732058155,
        "abs_return_acf_5": 0.27925518354010415,
        "abs_return_acf_20": 0.23134405106723108,
        "quantile_01": -0.09154033214483984,
        "quantile_99": 0.0790895256852617,
        "hill_tail_index": 2.586063944808664
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02790872004444023,
        "excess_kurtosis": 24.727645612651735,
        "return_acf_1": -0.08615428915133098,
        "abs_return_acf_1": 0.3717405205416358,
        "abs_return_acf_5": 0.2485731779128528,
        "abs_return_acf_20": 0.23480682408004874,
        "quantile_01": -0.09257859853379685,
        "quantile_99": 0.07754433974232139,
        "hill_tail_index": 2.2568856025002173
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023614373067033685,
        "excess_kurtosis": 13.776870893665897,
        "return_acf_1": -0.17074144614853493,
        "abs_return_acf_1": 0.423338136346786,
        "abs_return_acf_5": 0.31883199687597524,
        "abs_return_acf_20": 0.3086540539482654,
        "quantile_01": -0.0712028029453937,
        "quantile_99": 0.07013360543637673,
        "hill_tail_index": 2.9113230185768657
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.027358605193191256,
        "excess_kurtosis": 21.538620480964962,
        "return_acf_1": -0.034564426284832035,
        "abs_return_acf_1": 0.4325220704926794,
        "abs_return_acf_5": 0.3546243785480294,
        "abs_return_acf_20": 0.3068525683538725,
        "quantile_01": -0.11076139738362012,
        "quantile_99": 0.07920523731403435,
        "hill_tail_index": 2.015363324134163
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02287008857888164,
        "excess_kurtosis": 7.788429893171601,
        "return_acf_1": -0.06889441646866347,
        "abs_return_acf_1": 0.38950296056867934,
        "abs_return_acf_5": 0.32199080687144166,
        "abs_return_acf_20": 0.21831267471060894,
        "quantile_01": -0.07763979818729255,
        "quantile_99": 0.06637615772745505,
        "hill_tail_index": 2.9185058327922047
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02363060429374947,
        "excess_kurtosis": 7.799866909695563,
        "return_acf_1": -0.13202915368120507,
        "abs_return_acf_1": 0.3254933271996902,
        "abs_return_acf_5": 0.2624046780522953,
        "abs_return_acf_20": 0.20547350779136445,
        "quantile_01": -0.07242912945382689,
        "quantile_99": 0.07606889334174916,
        "hill_tail_index": 3.9866365039767917
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.028300444773322535,
        "excess_kurtosis": 21.81237018660011,
        "return_acf_1": -0.016856367352682495,
        "abs_return_acf_1": 0.4084166377589354,
        "abs_return_acf_5": 0.28122897452895956,
        "abs_return_acf_20": 0.2795497424983612,
        "quantile_01": -0.09723095863059898,
        "quantile_99": 0.0820568547527184,
        "hill_tail_index": 2.4240354142815264
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.027028439275578547,
        "excess_kurtosis": 22.76807990110734,
        "return_acf_1": 0.03399748961247817,
        "abs_return_acf_1": 0.3737610430836355,
        "abs_return_acf_5": 0.22607865252643808,
        "abs_return_acf_20": 0.2294394178027643,
        "quantile_01": -0.09350309040676874,
        "quantile_99": 0.06647535729795805,
        "hill_tail_index": 2.0994436057149892
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02727925498890924,
        "excess_kurtosis": 23.06869700354105,
        "return_acf_1": -0.02374363745598281,
        "abs_return_acf_1": 0.38957662649941666,
        "abs_return_acf_5": 0.27131440930876116,
        "abs_return_acf_20": 0.2536303470052885,
        "quantile_01": -0.09454159784961916,
        "quantile_99": 0.07172497666791912,
        "hill_tail_index": 2.158644934523151
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.026916587888840805,
        "excess_kurtosis": 17.195183317024508,
        "return_acf_1": -0.06658674293757398,
        "abs_return_acf_1": 0.32239457182164794,
        "abs_return_acf_5": 0.23927532400133472,
        "abs_return_acf_20": 0.26824118804124536,
        "quantile_01": -0.08368637197534831,
        "quantile_99": 0.07730840261176064,
        "hill_tail_index": 2.967368849813177
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.025645329759992234,
        "excess_kurtosis": 22.1826678384788,
        "return_acf_1": 0.006544778246231096,
        "abs_return_acf_1": 0.36883177953932167,
        "abs_return_acf_5": 0.25234313614710185,
        "abs_return_acf_20": 0.23782812321430558,
        "quantile_01": -0.08205512259986447,
        "quantile_99": 0.06114922372426034,
        "hill_tail_index": 2.077714858806124
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02732814563896495,
        "excess_kurtosis": 20.39836465634396,
        "return_acf_1": -0.042881591746956896,
        "abs_return_acf_1": 0.41020723522479213,
        "abs_return_acf_5": 0.34933041319304237,
        "abs_return_acf_20": 0.28576249603490195,
        "quantile_01": -0.09812090820714148,
        "quantile_99": 0.08033229403169967,
        "hill_tail_index": 2.988994854206643
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02203946971618898,
        "excess_kurtosis": 4.470552098586735,
        "return_acf_1": -0.1288620795778312,
        "abs_return_acf_1": 0.30223829134845676,
        "abs_return_acf_5": 0.21692714086632203,
        "abs_return_acf_20": 0.20877060420914295,
        "quantile_01": -0.06874614702894316,
        "quantile_99": 0.0637529378291814,
        "hill_tail_index": 4.02936525415059
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.024837038233074146,
        "excess_kurtosis": 9.041282241553782,
        "return_acf_1": -0.20799740932423585,
        "abs_return_acf_1": 0.4456770296118655,
        "abs_return_acf_5": 0.3490529735441078,
        "abs_return_acf_20": 0.31207529253796545,
        "quantile_01": -0.0861634275225007,
        "quantile_99": 0.0699968211195267,
        "hill_tail_index": 2.960704350843518
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.026717588333833094,
        "excess_kurtosis": 28.13907957347361,
        "return_acf_1": -0.009911684585489746,
        "abs_return_acf_1": 0.40881825729996163,
        "abs_return_acf_5": 0.22768749893848012,
        "abs_return_acf_20": 0.25966227719637186,
        "quantile_01": -0.0859020409660891,
        "quantile_99": 0.06805083247715311,
        "hill_tail_index": 2.260579472381284
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.025391238537315047,
        "excess_kurtosis": 11.32429209375452,
        "return_acf_1": -0.1116213519007561,
        "abs_return_acf_1": 0.368260186559448,
        "abs_return_acf_5": 0.31298636518971035,
        "abs_return_acf_20": 0.24639375136153255,
        "quantile_01": -0.08473537335909381,
        "quantile_99": 0.07053606692607704,
        "hill_tail_index": 3.5111653146054773
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.025013778676094965,
        "excess_kurtosis": 27.9629612675239,
        "return_acf_1": 0.007177070166764706,
        "abs_return_acf_1": 0.3626389513646914,
        "abs_return_acf_5": 0.26710003030605267,
        "abs_return_acf_20": 0.24658256706145398,
        "quantile_01": -0.071117172199717,
        "quantile_99": 0.05977082026361097,
        "hill_tail_index": 2.086692381025733
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02165829369445916,
        "excess_kurtosis": 9.185360252888307,
        "return_acf_1": -0.15191339501034146,
        "abs_return_acf_1": 0.34064271029382326,
        "abs_return_acf_5": 0.2934155751489219,
        "abs_return_acf_20": 0.18797377133359114,
        "quantile_01": -0.06821817551649839,
        "quantile_99": 0.061442596322729075,
        "hill_tail_index": 2.759835013759833
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022605600617320008,
        "excess_kurtosis": 8.25634561183776,
        "return_acf_1": -0.10788904895489221,
        "abs_return_acf_1": 0.363443043602914,
        "abs_return_acf_5": 0.3082186593295838,
        "abs_return_acf_20": 0.2745316219249652,
        "quantile_01": -0.06616253289951107,
        "quantile_99": 0.060918115064769816,
        "hill_tail_index": 3.031271912574144
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023473512662189593,
        "excess_kurtosis": 8.70086661486531,
        "return_acf_1": -0.15652376698518458,
        "abs_return_acf_1": 0.3826536609216836,
        "abs_return_acf_5": 0.3264800572191167,
        "abs_return_acf_20": 0.24271081596579083,
        "quantile_01": -0.07715248281269295,
        "quantile_99": 0.06837034867276887,
        "hill_tail_index": 3.872685975168005
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02668418895949774,
        "excess_kurtosis": 21.417561689344943,
        "return_acf_1": -0.10767680675194483,
        "abs_return_acf_1": 0.3789419071666353,
        "abs_return_acf_5": 0.2899583743363492,
        "abs_return_acf_20": 0.24763513472092366,
        "quantile_01": -0.08749955862557661,
        "quantile_99": 0.06819788667369026,
        "hill_tail_index": 2.4728040346201334
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.025954165393234255,
        "excess_kurtosis": 22.445915325270537,
        "return_acf_1": -0.07637048569663477,
        "abs_return_acf_1": 0.4098433658749433,
        "abs_return_acf_5": 0.3195161012625529,
        "abs_return_acf_20": 0.2636266618314718,
        "quantile_01": -0.08948096217538186,
        "quantile_99": 0.06369190227836209,
        "hill_tail_index": 2.4790152818340507
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.026636632925176488,
        "excess_kurtosis": 23.04055144377654,
        "return_acf_1": -0.042808732360507806,
        "abs_return_acf_1": 0.43183488960935024,
        "abs_return_acf_5": 0.31778967017031556,
        "abs_return_acf_20": 0.2692810788034943,
        "quantile_01": -0.09036642609430419,
        "quantile_99": 0.06549392501625051,
        "hill_tail_index": 2.4957830731788087
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.025562983553394356,
        "excess_kurtosis": 25.378070987191265,
        "return_acf_1": -0.04128322636533487,
        "abs_return_acf_1": 0.3668863217675703,
        "abs_return_acf_5": 0.26308092676313594,
        "abs_return_acf_20": 0.241076797775258,
        "quantile_01": -0.0702459692378597,
        "quantile_99": 0.06717909696827494,
        "hill_tail_index": 2.3717097016259676
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.027564845615803683,
        "excess_kurtosis": 27.04528554718293,
        "return_acf_1": 0.03682909439909535,
        "abs_return_acf_1": 0.35224992370191505,
        "abs_return_acf_5": 0.2929575759517735,
        "abs_return_acf_20": 0.20583633579469335,
        "quantile_01": -0.09552978887967778,
        "quantile_99": 0.0770868715022126,
        "hill_tail_index": 2.1994477620347404
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02401983234904947,
        "excess_kurtosis": 11.672563900465367,
        "return_acf_1": -0.1664804715212239,
        "abs_return_acf_1": 0.4227894655315394,
        "abs_return_acf_5": 0.3711826630950328,
        "abs_return_acf_20": 0.3021089696340368,
        "quantile_01": -0.07616294822878546,
        "quantile_99": 0.07454617019619998,
        "hill_tail_index": 2.897764884500155
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
