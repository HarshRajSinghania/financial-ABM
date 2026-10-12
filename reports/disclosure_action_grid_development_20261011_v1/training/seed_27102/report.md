# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27102
Run ID: `49da5478a81e9acc7aee29803e04d1cba4bec81ba99a01df11a969f93d4841d7`
Result fingerprint: `2fa0f47d73d9b39634a8bb7bb97b808e377c0bc17a286314548d39f24dcd17c5`

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
    "equal_weight_sd": -0.6272142857142826,
    "equal_weight_raw": -9.408214285714235,
    "fixed_start_cap_weight_sd": -0.605771617186523,
    "fixed_start_cap_weight_raw": -9.086574257797844,
    "end_cap_weight_sd": -0.6272266363356742,
    "end_cap_weight_raw": -9.408399545035113
  },
  "full_period_change": {
    "equal_weight_sd": -0.9814047619047571,
    "equal_weight_raw": -14.721071428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9304837962962917,
    "inflation_mean_sd": 0.5466908068783068
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3251666666666699,
    "equal_weight_raw": 4.877500000000047,
    "fixed_start_cap_weight_sd": 0.3466093351944292,
    "fixed_start_cap_weight_raw": 5.199140027916439,
    "end_cap_weight_sd": 0.3251543160452785,
    "end_cap_weight_raw": 4.877314740679178
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6590476190476157,
      "change_raw": -9.885714285714235,
      "decay_adjusted_gain_sd": 0.2933333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6596031746031714,
      "change_raw": -9.894047619047571,
      "decay_adjusted_gain_sd": 0.292777777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.6057142857142824,
      "change_raw": -9.085714285714236,
      "decay_adjusted_gain_sd": 0.34666666666666984
    },
    "large_minus_small_sd": -0.05333333333333323,
    "large_minus_small_raw": -0.7999999999999985
  },
  "inflation": {
    "initial_mean_sd": 0.2700833333333333,
    "final_mean_sd": 0.5719166666666667,
    "mean_sd": 0.43933825978351376,
    "mean_absolute_raw_gap": 6.590073896752706,
    "final_absolute_raw_gap": 8.578750000000001,
    "mean_range_fraction": 0.06590073896752706
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.42,
    "initial_wealth_share": 0.32614586589926237,
    "final_wealth_share": 0.40903739607884254
  },
  "pricing_slope": {
    "mean": -0.005747217104422321,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.23597369015293537,
    "real_improvement_cost": 0.20638545893336324,
    "washing_cost": 0.029588231219572127,
    "fine_transfer": 0.034628322058704405,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.27060201221163976,
    "resource_cost_fraction_initial_cap": 0.007865789671764514,
    "private_net_outflow_fraction_initial_cap": 0.009020067073721327,
    "fine_transfer_fraction_initial_cap": 0.0011542774019568137,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0030501706553179393,
    "unapplied_final_day_resource_cost": 0.00380405253172802
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 41.33935437326868,
    "beneficial_raw_gain_per_resource_cost": 620.0903155990301,
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
    "accrued_cost": 2.9747018272305366,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.001488648959940081,
    "accrued_cost_fraction_initial_cap": 0.09915672757435123,
    "mean_contract_rate": 0.04074891019101367,
    "maximum_ledger_error": 5.251604272976662e-20
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
    "maximum_relative_cash_error": 1.2108954448895668e-15,
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
      "minimum": -0.1760915762354818,
      "maximum": 0.015341064954002046,
      "mean": -0.09808811790167196,
      "median": -0.11629942887808298,
      "quantile_05": -0.16706296314836372,
      "quantile_95": 0.0014731127064410324
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
      "minimum": 0.22477478559339978,
      "maximum": 0.7932539595566986,
      "mean": 0.5171911607442966,
      "median": 0.5731472645948021,
      "quantile_05": 0.2579760036929099,
      "quantile_95": 0.7534141302983766
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
        "daily_volatility": 0.01930444949105354,
        "excess_kurtosis": 16.996680700550577,
        "return_acf_1": -0.15461811546904908,
        "abs_return_acf_1": 0.29024557774066073,
        "abs_return_acf_5": 0.3169195188602796,
        "abs_return_acf_20": 0.34348895018729675,
        "quantile_01": -0.053781963867837915,
        "quantile_99": 0.04678470993557653,
        "hill_tail_index": 2.7082112878658995
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.0194234605250733,
        "excess_kurtosis": 6.318007646318151,
        "return_acf_1": -0.134186084686049,
        "abs_return_acf_1": 0.3417527663125236,
        "abs_return_acf_5": 0.25909732144051184,
        "abs_return_acf_20": 0.34020661671285757,
        "quantile_01": -0.060745615399982134,
        "quantile_99": 0.05102433204834822,
        "hill_tail_index": 4.064111637064043
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01811453929234187,
        "excess_kurtosis": 14.702484772939844,
        "return_acf_1": -0.12114816075876786,
        "abs_return_acf_1": 0.3778678342830793,
        "abs_return_acf_5": 0.3225079882209942,
        "abs_return_acf_20": 0.3969555787530179,
        "quantile_01": -0.062390936642893205,
        "quantile_99": 0.05523035664720445,
        "hill_tail_index": 2.2169018266647655
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0178489243534347,
        "excess_kurtosis": 5.601309132662076,
        "return_acf_1": -0.13871887750457557,
        "abs_return_acf_1": 0.34691704140217927,
        "abs_return_acf_5": 0.22143439356075714,
        "abs_return_acf_20": 0.34760408920874186,
        "quantile_01": -0.05712801560379978,
        "quantile_99": 0.046323001678037636,
        "hill_tail_index": 3.2324141221239517
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020448021031875045,
        "excess_kurtosis": 24.03297520100671,
        "return_acf_1": -0.14273934872546504,
        "abs_return_acf_1": 0.3806587520237315,
        "abs_return_acf_5": 0.28684441849122017,
        "abs_return_acf_20": 0.3754463263502282,
        "quantile_01": -0.06309860560313438,
        "quantile_99": 0.048758671187480215,
        "hill_tail_index": 2.1590504891608204
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01799055959121702,
        "excess_kurtosis": 5.263512929084053,
        "return_acf_1": -0.09852843699049901,
        "abs_return_acf_1": 0.27007460813098555,
        "abs_return_acf_5": 0.2015864857652264,
        "abs_return_acf_20": 0.18148688052483966,
        "quantile_01": -0.05421799581361122,
        "quantile_99": 0.049423980074033196,
        "hill_tail_index": 2.8572461956244957
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019946057009334116,
        "excess_kurtosis": 27.383022261623417,
        "return_acf_1": 0.004712020625329183,
        "abs_return_acf_1": 0.3343332840016183,
        "abs_return_acf_5": 0.3263643613999297,
        "abs_return_acf_20": 0.33058399182053355,
        "quantile_01": -0.06369494312667091,
        "quantile_99": 0.049881205625505846,
        "hill_tail_index": 2.2385014201309152
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018754815051060292,
        "excess_kurtosis": 15.32417552775696,
        "return_acf_1": -0.03994123667236935,
        "abs_return_acf_1": 0.4226723292571931,
        "abs_return_acf_5": 0.37566520103379186,
        "abs_return_acf_20": 0.3804753213867169,
        "quantile_01": -0.05967929568067086,
        "quantile_99": 0.0442792357771316,
        "hill_tail_index": 1.836628507680155
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019175304810785054,
        "excess_kurtosis": 17.228116939373397,
        "return_acf_1": -0.15208834692763845,
        "abs_return_acf_1": 0.3554922259445672,
        "abs_return_acf_5": 0.3499224905302552,
        "abs_return_acf_20": 0.35759580502899696,
        "quantile_01": -0.06502126176094335,
        "quantile_99": 0.05297702335328032,
        "hill_tail_index": 2.236549652991745
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020578146971173945,
        "excess_kurtosis": 27.35140993919358,
        "return_acf_1": -0.16342481741175915,
        "abs_return_acf_1": 0.39972687463122397,
        "abs_return_acf_5": 0.38347070017321144,
        "abs_return_acf_20": 0.36866756591670596,
        "quantile_01": -0.07625740646808546,
        "quantile_99": 0.05000352096178218,
        "hill_tail_index": 1.8995759326201005
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020807525965677497,
        "excess_kurtosis": 11.01756969351865,
        "return_acf_1": -0.1760915762354818,
        "abs_return_acf_1": 0.45316340153485973,
        "abs_return_acf_5": 0.49548608189059173,
        "abs_return_acf_20": 0.3346189899165505,
        "quantile_01": -0.06147889280867331,
        "quantile_99": 0.07244927122082327,
        "hill_tail_index": 2.7338319613253868
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018970190436203883,
        "excess_kurtosis": 16.716713460997518,
        "return_acf_1": -0.05509558648793291,
        "abs_return_acf_1": 0.44624643559323435,
        "abs_return_acf_5": 0.3483895390179131,
        "abs_return_acf_20": 0.37481994055637163,
        "quantile_01": -0.062413164638933705,
        "quantile_99": 0.047783701693435404,
        "hill_tail_index": 2.061879633774711
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01925414612905899,
        "excess_kurtosis": 4.29503351479486,
        "return_acf_1": -0.09702842643650499,
        "abs_return_acf_1": 0.28813679170287665,
        "abs_return_acf_5": 0.3248571713076403,
        "abs_return_acf_20": 0.23433631625969026,
        "quantile_01": -0.05083169963100473,
        "quantile_99": 0.06342644219272738,
        "hill_tail_index": 4.028843054931409
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018587532870007452,
        "excess_kurtosis": 3.393699005847699,
        "return_acf_1": -0.07672469926653608,
        "abs_return_acf_1": 0.3090753595490404,
        "abs_return_acf_5": 0.26090190352998033,
        "abs_return_acf_20": 0.27932749480943714,
        "quantile_01": -0.05829028137831683,
        "quantile_99": 0.0521152834355426,
        "hill_tail_index": 4.126469832191303
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017551880845629083,
        "excess_kurtosis": 5.702837463035902,
        "return_acf_1": -0.13286500409021657,
        "abs_return_acf_1": 0.28987426653454657,
        "abs_return_acf_5": 0.3070071911904805,
        "abs_return_acf_20": 0.24227452990870058,
        "quantile_01": -0.04794798450362162,
        "quantile_99": 0.05181695421658146,
        "hill_tail_index": 3.770812358742082
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019002011954340717,
        "excess_kurtosis": 10.561252434091983,
        "return_acf_1": -0.11858702066902894,
        "abs_return_acf_1": 0.4005599117702222,
        "abs_return_acf_5": 0.36121917514435553,
        "abs_return_acf_20": 0.3801868791587464,
        "quantile_01": -0.06427457714328023,
        "quantile_99": 0.051136566224145835,
        "hill_tail_index": 2.8695417050752403
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020864303522339738,
        "excess_kurtosis": 6.503503056037321,
        "return_acf_1": -0.17003962784194926,
        "abs_return_acf_1": 0.4631058047327338,
        "abs_return_acf_5": 0.42987710232109855,
        "abs_return_acf_20": 0.3169374641744619,
        "quantile_01": -0.0708513495385051,
        "quantile_99": 0.06749767429411081,
        "hill_tail_index": 3.9843176470578454
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017107209703967452,
        "excess_kurtosis": 18.273844883290955,
        "return_acf_1": -0.024904265859955234,
        "abs_return_acf_1": 0.35211536674304883,
        "abs_return_acf_5": 0.2702923651066613,
        "abs_return_acf_20": 0.31675157636747425,
        "quantile_01": -0.043386376069485026,
        "quantile_99": 0.041386724390791475,
        "hill_tail_index": 1.9770242197440757
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019329825103410032,
        "excess_kurtosis": 23.19805778361614,
        "return_acf_1": 0.015341064954002046,
        "abs_return_acf_1": 0.41384192316950685,
        "abs_return_acf_5": 0.3578453966396519,
        "abs_return_acf_20": 0.3653266627341965,
        "quantile_01": -0.05547187442768734,
        "quantile_99": 0.0448348029309008,
        "hill_tail_index": 1.8422981325154482
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019175702518096603,
        "excess_kurtosis": 7.302799480074524,
        "return_acf_1": -0.04342963628123627,
        "abs_return_acf_1": 0.35627406145118506,
        "abs_return_acf_5": 0.38891110801998363,
        "abs_return_acf_20": 0.29414931184085624,
        "quantile_01": -0.06448984403322659,
        "quantile_99": 0.05565705165167131,
        "hill_tail_index": 3.15943301281838
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018195379222760044,
        "excess_kurtosis": 10.0929072738097,
        "return_acf_1": -0.1409587029244041,
        "abs_return_acf_1": 0.37047947205944215,
        "abs_return_acf_5": 0.30183173278874115,
        "abs_return_acf_20": 0.367509312448066,
        "quantile_01": -0.05914203227882525,
        "quantile_99": 0.04760668845141207,
        "hill_tail_index": 2.8162594182055196
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020659520673725094,
        "excess_kurtosis": 27.756113133162206,
        "return_acf_1": -0.05025108461351122,
        "abs_return_acf_1": 0.4703043272184617,
        "abs_return_acf_5": 0.36220708066661284,
        "abs_return_acf_20": 0.39743251613662123,
        "quantile_01": -0.06736156094622558,
        "quantile_99": 0.049252965039324664,
        "hill_tail_index": 1.7888355852725677
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01694353663051315,
        "excess_kurtosis": 9.752090335115632,
        "return_acf_1": -0.11401183708713701,
        "abs_return_acf_1": 0.35831073354743714,
        "abs_return_acf_5": 0.2919819658385086,
        "abs_return_acf_20": 0.2914301955286384,
        "quantile_01": -0.046764654471613695,
        "quantile_99": 0.04294278144238197,
        "hill_tail_index": 2.21083105822146
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018766469831948695,
        "excess_kurtosis": 12.571451749021156,
        "return_acf_1": -0.03249289908867126,
        "abs_return_acf_1": 0.4532877002988903,
        "abs_return_acf_5": 0.3359727855124531,
        "abs_return_acf_20": 0.4502516544648411,
        "quantile_01": -0.05847063945490464,
        "quantile_99": 0.04920095204623474,
        "hill_tail_index": 2.330919972982049
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017780087957283728,
        "excess_kurtosis": 4.338787637796473,
        "return_acf_1": -0.1252622352263992,
        "abs_return_acf_1": 0.3157957894605101,
        "abs_return_acf_5": 0.2789854488197193,
        "abs_return_acf_20": 0.21001864550935623,
        "quantile_01": -0.050322746807923244,
        "quantile_99": 0.049286579603853756,
        "hill_tail_index": 3.454422931422028
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018988335964911795,
        "excess_kurtosis": 13.809776353000704,
        "return_acf_1": -0.10496675519743355,
        "abs_return_acf_1": 0.42736836528824473,
        "abs_return_acf_5": 0.3348123896345834,
        "abs_return_acf_20": 0.38782049258095036,
        "quantile_01": -0.06140193371378292,
        "quantile_99": 0.05667664897608736,
        "hill_tail_index": 2.4611288506547093
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.016916953362690022,
        "excess_kurtosis": 5.190798735384119,
        "return_acf_1": -0.06688507137106936,
        "abs_return_acf_1": 0.2727937049467305,
        "abs_return_acf_5": 0.2474154959052729,
        "abs_return_acf_20": 0.219186744227299,
        "quantile_01": -0.04887627236969062,
        "quantile_99": 0.05157450188910113,
        "hill_tail_index": 3.561281878569192
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020538303005403585,
        "excess_kurtosis": 31.04042500476455,
        "return_acf_1": -0.13383741417379483,
        "abs_return_acf_1": 0.4458458182465728,
        "abs_return_acf_5": 0.37696678974869413,
        "abs_return_acf_20": 0.35749085135802305,
        "quantile_01": -0.0682724840172259,
        "quantile_99": 0.044873246814604896,
        "hill_tail_index": 1.8845293721001037
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018741640421487304,
        "excess_kurtosis": 17.34922554773497,
        "return_acf_1": -0.0024855525277555513,
        "abs_return_acf_1": 0.3482226249631546,
        "abs_return_acf_5": 0.3006093468420841,
        "abs_return_acf_20": 0.34958470316475854,
        "quantile_01": -0.05075420853340531,
        "quantile_99": 0.04286852602809217,
        "hill_tail_index": 1.8987098772128292
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019488126723457604,
        "excess_kurtosis": 15.32477904874797,
        "return_acf_1": -0.15138580210429925,
        "abs_return_acf_1": 0.44436504786043296,
        "abs_return_acf_5": 0.3759540071858638,
        "abs_return_acf_20": 0.4411908931917313,
        "quantile_01": -0.06142426536266113,
        "quantile_99": 0.053478912943330306,
        "hill_tail_index": 2.571602250151395
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
