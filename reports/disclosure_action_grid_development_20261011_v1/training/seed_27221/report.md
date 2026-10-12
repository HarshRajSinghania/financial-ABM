# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27221
Run ID: `29b294a046587d9f33f30174259becea58abace0421a001a858eeb7a87b2e5d9`
Result fingerprint: `a2451ca33116e9e377cc0935beb51906ef41a00e1a0d6c9e5d3897a2f6cc09b3`

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
    "equal_weight_sd": -0.7437976190476159,
    "equal_weight_raw": -11.156964285714237,
    "fixed_start_cap_weight_sd": -0.7479515734576664,
    "fixed_start_cap_weight_raw": -11.219273601864993,
    "end_cap_weight_sd": -0.7474589573485605,
    "end_cap_weight_raw": -11.211884360228412
  },
  "full_period_change": {
    "equal_weight_sd": -1.195154761904757,
    "equal_weight_raw": -17.927321428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1162516534391487,
    "inflation_mean_sd": 0.6718478835978836
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.20672506522377193,
    "equal_weight_raw": 3.100875978356579,
    "fixed_start_cap_weight_sd": 0.20421554674314005,
    "fixed_start_cap_weight_raw": 3.063233201147101,
    "end_cap_weight_sd": 0.20464962935251776,
    "end_cap_weight_raw": 3.069744440287766
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7532142857142826,
      "change_raw": -11.29821428571424,
      "decay_adjusted_gain_sd": 0.19916666666666968
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7426587301587269,
      "change_raw": -11.139880952380903,
      "decay_adjusted_gain_sd": 0.20972222222222536
    },
    "small": {
      "count": 18,
      "change_sd": -0.7427976190476158,
      "change_raw": -11.141964285714236,
      "decay_adjusted_gain_sd": 0.2064862198173956
    },
    "large_minus_small_sd": -0.010416666666666852,
    "large_minus_small_raw": -0.15625000000000278
  },
  "inflation": {
    "initial_mean_sd": 0.3540833333333333,
    "final_mean_sd": 0.7043333333333331,
    "mean_sd": 0.5849078545656398,
    "mean_absolute_raw_gap": 8.773617818484597,
    "final_absolute_raw_gap": 10.565,
    "mean_range_fraction": 0.08773617818484597
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.36666666666666664,
    "initial_wealth_share": 0.13124236949888846,
    "final_wealth_share": 0.41591956610993647
  },
  "pricing_slope": {
    "mean": -0.004403547401836683,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.034598056872648025,
    "real_improvement_cost": 0.0193547036250885,
    "washing_cost": 0.015243353247559523,
    "fine_transfer": 0.009911560628552807,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.04450961750120083,
    "resource_cost_fraction_initial_cap": 0.0011532685624216007,
    "private_net_outflow_fraction_initial_cap": 0.0014836539167066942,
    "fine_transfer_fraction_initial_cap": 0.00033038535428509355,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002403848754582278,
    "unapplied_final_day_resource_cost": 0.005407426247102297
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 179.25145274895596,
    "beneficial_raw_gain_per_resource_cost": 2688.7717912343396,
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
    "accrued_cost": 3.205377132021544,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.22918665583106726,
    "accrued_cost_fraction_initial_cap": 0.10684590440071812,
    "mean_contract_rate": 0.04436535877422124,
    "maximum_ledger_error": 5.590417451878382e-20
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
    "maximum_relative_cash_error": 2.5074260187903013e-15,
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
      "minimum": -0.17557971051786808,
      "maximum": -0.018482422807716895,
      "mean": -0.09400666476867195,
      "median": -0.09610131553239333,
      "quantile_05": -0.1441471438925258,
      "quantile_95": -0.04025119010923782
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
      "minimum": 0.30459867293947285,
      "maximum": 0.8127201326443009,
      "mean": 0.5754904607625323,
      "median": 0.5934975044363547,
      "quantile_05": 0.35742947628524974,
      "quantile_95": 0.7506792453524923
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
        "daily_volatility": 0.020892179520079796,
        "excess_kurtosis": 10.997777834577846,
        "return_acf_1": -0.09073574116825095,
        "abs_return_acf_1": 0.39165828527958185,
        "abs_return_acf_5": 0.32466384514428903,
        "abs_return_acf_20": 0.33759465013255296,
        "quantile_01": -0.06475667585950066,
        "quantile_99": 0.05119538134700148,
        "hill_tail_index": 2.681605062216271
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021379077805991634,
        "excess_kurtosis": 9.817089510838304,
        "return_acf_1": -0.11137651744459191,
        "abs_return_acf_1": 0.452224972732848,
        "abs_return_acf_5": 0.3402827049319616,
        "abs_return_acf_20": 0.2961610231797404,
        "quantile_01": -0.07181867902158852,
        "quantile_99": 0.06176442040023755,
        "hill_tail_index": 3.161113580001823
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019208320714662584,
        "excess_kurtosis": 4.085759652000903,
        "return_acf_1": -0.09537705200559161,
        "abs_return_acf_1": 0.2538014089798928,
        "abs_return_acf_5": 0.24621138993545397,
        "abs_return_acf_20": 0.24991672984009158,
        "quantile_01": -0.04914601366938812,
        "quantile_99": 0.057569795543867985,
        "hill_tail_index": 3.181185756687818
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.023193317746520406,
        "excess_kurtosis": 10.138667689368074,
        "return_acf_1": -0.0500923598573415,
        "abs_return_acf_1": 0.4504476561074007,
        "abs_return_acf_5": 0.345403777053369,
        "abs_return_acf_20": 0.3280014810522838,
        "quantile_01": -0.08499056880241454,
        "quantile_99": 0.06566470362065603,
        "hill_tail_index": 2.8963154554819983
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02009366682235831,
        "excess_kurtosis": 6.800914606744849,
        "return_acf_1": -0.1301014795679191,
        "abs_return_acf_1": 0.3584455968251021,
        "abs_return_acf_5": 0.32309542042067607,
        "abs_return_acf_20": 0.3265619670661919,
        "quantile_01": -0.06260502936659366,
        "quantile_99": 0.05930941018223174,
        "hill_tail_index": 3.3138344045723764
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023194406422912116,
        "excess_kurtosis": 11.140931329674865,
        "return_acf_1": -0.05885687369438521,
        "abs_return_acf_1": 0.41350272147051886,
        "abs_return_acf_5": 0.44915925400349277,
        "abs_return_acf_20": 0.34951407519731775,
        "quantile_01": -0.08432561669691677,
        "quantile_99": 0.06527392301484587,
        "hill_tail_index": 2.7028658152576823
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019468259457709483,
        "excess_kurtosis": 6.513371796599374,
        "return_acf_1": -0.1423756487352115,
        "abs_return_acf_1": 0.3389987504051208,
        "abs_return_acf_5": 0.3282949493187945,
        "abs_return_acf_20": 0.22764154613982956,
        "quantile_01": -0.06974259822143412,
        "quantile_99": 0.05280812395687461,
        "hill_tail_index": 2.9342860096957555
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018858127287949354,
        "excess_kurtosis": 7.497865331382098,
        "return_acf_1": -0.13243633844104968,
        "abs_return_acf_1": 0.2919991646624524,
        "abs_return_acf_5": 0.28932957396141573,
        "abs_return_acf_20": 0.2536800054208903,
        "quantile_01": -0.059517765610950034,
        "quantile_99": 0.05436545777695258,
        "hill_tail_index": 2.7900016991390606
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017123143524521017,
        "excess_kurtosis": 8.188237989223804,
        "return_acf_1": -0.018482422807716895,
        "abs_return_acf_1": 0.206892042418712,
        "abs_return_acf_5": 0.23711675834750368,
        "abs_return_acf_20": 0.16178090980364104,
        "quantile_01": -0.052799038539644294,
        "quantile_99": 0.04377808834787265,
        "hill_tail_index": 2.5142127483824948
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.024392853065812053,
        "excess_kurtosis": 11.836074690868069,
        "return_acf_1": -0.05228965531033945,
        "abs_return_acf_1": 0.41999161057662154,
        "abs_return_acf_5": 0.44032795601975344,
        "abs_return_acf_20": 0.4066600589748445,
        "quantile_01": -0.0828812151901899,
        "quantile_99": 0.07733131563302675,
        "hill_tail_index": 2.9158079508491808
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01644441218706443,
        "excess_kurtosis": 2.3690219233157395,
        "return_acf_1": -0.0901945650430931,
        "abs_return_acf_1": 0.20448524506432494,
        "abs_return_acf_5": 0.17089204858859702,
        "abs_return_acf_20": 0.16296353293977592,
        "quantile_01": -0.04361201293204582,
        "quantile_99": 0.04290106430356315,
        "hill_tail_index": 3.5113726075819405
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019311810703551334,
        "excess_kurtosis": 6.793148535493829,
        "return_acf_1": -0.05987697708526654,
        "abs_return_acf_1": 0.35340386877174085,
        "abs_return_acf_5": 0.3344329571107015,
        "abs_return_acf_20": 0.28797631138645574,
        "quantile_01": -0.062307818737425684,
        "quantile_99": 0.04978422655768084,
        "hill_tail_index": 2.9309996231876236
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01900337815111758,
        "excess_kurtosis": 4.519241664543913,
        "return_acf_1": -0.1455965490212375,
        "abs_return_acf_1": 0.38340548243495537,
        "abs_return_acf_5": 0.3391550537688572,
        "abs_return_acf_20": 0.26794036880908795,
        "quantile_01": -0.06483303541925321,
        "quantile_99": 0.054380589283728964,
        "hill_tail_index": 3.849987560629036
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019113227529931727,
        "excess_kurtosis": 7.4434675658995,
        "return_acf_1": -0.12732177929137092,
        "abs_return_acf_1": 0.32497384958169667,
        "abs_return_acf_5": 0.32474920644931926,
        "abs_return_acf_20": 0.23794609980829648,
        "quantile_01": -0.05548748909061614,
        "quantile_99": 0.05548717552551975,
        "hill_tail_index": 2.8811387187649475
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022193325940908844,
        "excess_kurtosis": 9.012414827216592,
        "return_acf_1": -0.10843332423707497,
        "abs_return_acf_1": 0.5193016031683881,
        "abs_return_acf_5": 0.39596275547001825,
        "abs_return_acf_20": 0.3236587342037499,
        "quantile_01": -0.07718164442193695,
        "quantile_99": 0.06550709875145082,
        "hill_tail_index": 3.5038146322004873
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019716243455947264,
        "excess_kurtosis": 9.396138256165763,
        "return_acf_1": -0.07906920680230486,
        "abs_return_acf_1": 0.2951306785317065,
        "abs_return_acf_5": 0.24128496102498598,
        "abs_return_acf_20": 0.24402721602668412,
        "quantile_01": -0.05645186225816802,
        "quantile_99": 0.04977549384000066,
        "hill_tail_index": 2.8235899283976154
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022104836838593152,
        "excess_kurtosis": 12.565239248700358,
        "return_acf_1": -0.13242495143346597,
        "abs_return_acf_1": 0.39483639735004494,
        "abs_return_acf_5": 0.3266825043831517,
        "abs_return_acf_20": 0.3240813095955122,
        "quantile_01": -0.08296838726715171,
        "quantile_99": 0.053036329444805776,
        "hill_tail_index": 2.5884738845886215
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018287110144505698,
        "excess_kurtosis": 4.270460126039558,
        "return_acf_1": -0.032422967784314846,
        "abs_return_acf_1": 0.33019990522819614,
        "abs_return_acf_5": 0.3792258580937451,
        "abs_return_acf_20": 0.2965706287271398,
        "quantile_01": -0.05925548951319439,
        "quantile_99": 0.051576580248257155,
        "hill_tail_index": 4.088410999618727
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021143723326160848,
        "excess_kurtosis": 8.72421120456067,
        "return_acf_1": -0.11309051129660776,
        "abs_return_acf_1": 0.4532454997099186,
        "abs_return_acf_5": 0.4067696633030203,
        "abs_return_acf_20": 0.3446115881413825,
        "quantile_01": -0.06839648112096114,
        "quantile_99": 0.06644096706296561,
        "hill_tail_index": 3.364324632771815
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022766806587991007,
        "excess_kurtosis": 9.692573000487736,
        "return_acf_1": -0.09863895224877618,
        "abs_return_acf_1": 0.39872854020758436,
        "abs_return_acf_5": 0.3836082191265498,
        "abs_return_acf_20": 0.32936420478438105,
        "quantile_01": -0.06937037154605698,
        "quantile_99": 0.05875695202437245,
        "hill_tail_index": 2.8085592105156896
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01948954503149732,
        "excess_kurtosis": 6.667245503413655,
        "return_acf_1": -0.17557971051786808,
        "abs_return_acf_1": 0.3082897840504478,
        "abs_return_acf_5": 0.28231859232331624,
        "abs_return_acf_20": 0.2752204352223961,
        "quantile_01": -0.059098934926106364,
        "quantile_99": 0.05715382363105939,
        "hill_tail_index": 3.5916224544635096
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022119233090855863,
        "excess_kurtosis": 12.134483312252051,
        "return_acf_1": -0.054989494672603084,
        "abs_return_acf_1": 0.39195169697439236,
        "abs_return_acf_5": 0.35442683014109566,
        "abs_return_acf_20": 0.2698126588924049,
        "quantile_01": -0.07718489979763946,
        "quantile_99": 0.062261589125164496,
        "hill_tail_index": 2.746935193514093
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022813439060230617,
        "excess_kurtosis": 11.301622532440446,
        "return_acf_1": -0.051531042854148126,
        "abs_return_acf_1": 0.3998682645062001,
        "abs_return_acf_5": 0.4568893645476948,
        "abs_return_acf_20": 0.30783220760564844,
        "quantile_01": -0.08047274149505564,
        "quantile_99": 0.06188289076580231,
        "hill_tail_index": 2.7203963337160353
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01905083210470306,
        "excess_kurtosis": 4.728608923209364,
        "return_acf_1": -0.09682557905919505,
        "abs_return_acf_1": 0.27564971378554254,
        "abs_return_acf_5": 0.28398419858058327,
        "abs_return_acf_20": 0.24924449830872283,
        "quantile_01": -0.05527834686948851,
        "quantile_99": 0.054108063747873206,
        "hill_tail_index": 3.726123892668165
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01714053604854109,
        "excess_kurtosis": 14.905671064644107,
        "return_acf_1": -0.049819017395254676,
        "abs_return_acf_1": 0.3502261286780841,
        "abs_return_acf_5": 0.37120529846644673,
        "abs_return_acf_20": 0.3000147019841948,
        "quantile_01": -0.0440734586964123,
        "quantile_99": 0.0447795523213938,
        "hill_tail_index": 2.185279842031076
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021214626196729192,
        "excess_kurtosis": 8.733204007107917,
        "return_acf_1": -0.13521745472912844,
        "abs_return_acf_1": 0.376365263552878,
        "abs_return_acf_5": 0.3305867713955514,
        "abs_return_acf_20": 0.28412548187265124,
        "quantile_01": -0.0686417380914158,
        "quantile_99": 0.056634116602516,
        "hill_tail_index": 3.2947998640467535
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.0190827145891677,
        "excess_kurtosis": 6.982577717019831,
        "return_acf_1": -0.08560843930684897,
        "abs_return_acf_1": 0.26524356575049224,
        "abs_return_acf_5": 0.28018926197674393,
        "abs_return_acf_20": 0.25433439675014785,
        "quantile_01": -0.0651015223487958,
        "quantile_99": 0.0530721374700608,
        "hill_tail_index": 3.6186974366589117
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01933678208347924,
        "excess_kurtosis": 6.540722698811429,
        "return_acf_1": -0.11296405197692726,
        "abs_return_acf_1": 0.3108400135109721,
        "abs_return_acf_5": 0.2949186518639314,
        "abs_return_acf_20": 0.26264244171806167,
        "quantile_01": -0.05927220471536477,
        "quantile_99": 0.05017888631863089,
        "hill_tail_index": 2.976450159757916
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019881064909529376,
        "excess_kurtosis": 5.634154756857837,
        "return_acf_1": -0.12558248557888999,
        "abs_return_acf_1": 0.37487812585158936,
        "abs_return_acf_5": 0.3434328856251169,
        "abs_return_acf_20": 0.2975463674191423,
        "quantile_01": -0.06588993433561263,
        "quantile_99": 0.0596579337937528,
        "hill_tail_index": 4.2442064366516155
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021375198826122075,
        "excess_kurtosis": 8.959773858896167,
        "return_acf_1": -0.06288879369338442,
        "abs_return_acf_1": 0.4482657155197018,
        "abs_return_acf_5": 0.37144250259720013,
        "abs_return_acf_20": 0.3719816465157964,
        "quantile_01": -0.073833462129885,
        "quantile_99": 0.05441162000204365,
        "hill_tail_index": 2.6713399735682746
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
