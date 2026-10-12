# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27047
Run ID: `5009e1290ef17df62c904a871303267eb8d4d9e4234d3d73936d32a9d6b3fb2b`
Result fingerprint: `9f082bed5f0f56b850110a316f572df455c0fd2dbcef5fb578492e774f072328`

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
    "equal_weight_sd": -0.48205158730158426,
    "equal_weight_raw": -7.230773809523763,
    "fixed_start_cap_weight_sd": -0.4817054809978137,
    "fixed_start_cap_weight_raw": -7.225582214967206,
    "end_cap_weight_sd": -0.47032054856885075,
    "end_cap_weight_raw": -7.05480822853276
  },
  "full_period_change": {
    "equal_weight_sd": -0.8059857768820188,
    "equal_weight_raw": -12.089786653230282
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7722668615381036,
    "inflation_mean_sd": 0.5186445105820107
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4385833333333363,
    "equal_weight_raw": 6.578750000000046,
    "fixed_start_cap_weight_sd": 0.45036465636437956,
    "fixed_start_cap_weight_raw": 6.7554698454656945,
    "end_cap_weight_sd": 0.46348316752137175,
    "end_cap_weight_raw": 6.952247512820575
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5448809523809494,
      "change_raw": -8.17321428571424,
      "decay_adjusted_gain_sd": 0.407500000000003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.442380952380949,
      "change_raw": -6.635714285714235,
      "decay_adjusted_gain_sd": 0.5100000000000032
    },
    "small": {
      "count": 18,
      "change_sd": -0.49141534391534086,
      "change_raw": -7.371230158730113,
      "decay_adjusted_gain_sd": 0.40805555555555856
    },
    "large_minus_small_sd": -0.053465608465608494,
    "large_minus_small_raw": -0.8019841269841275
  },
  "inflation": {
    "initial_mean_sd": 0.2524166666666667,
    "final_mean_sd": 0.5600833333333333,
    "mean_sd": 0.43327511795725787,
    "mean_absolute_raw_gap": 6.499126769358868,
    "final_absolute_raw_gap": 8.401250000000003,
    "mean_range_fraction": 0.06499126769358868
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.4,
    "initial_wealth_share": 0.3158914046852667,
    "final_wealth_share": 0.46120934754830895
  },
  "pricing_slope": {
    "mean": -0.0024029932398316766,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.3427441392872203,
    "real_improvement_cost": 0.30867069327754426,
    "washing_cost": 0.03407344600967599,
    "fine_transfer": 0.013459464162921366,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3562036034501417,
    "resource_cost_fraction_initial_cap": 0.011424804642907344,
    "private_net_outflow_fraction_initial_cap": 0.011873453448338057,
    "fine_transfer_fraction_initial_cap": 0.0004486488054307122,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001835957901763445,
    "unapplied_final_day_resource_cost": 0.0003395626258605053
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 38.3886943402235,
    "beneficial_raw_gain_per_resource_cost": 575.8304151033525,
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
    "accrued_cost": 2.8651733183747443,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.11101715781573224,
    "accrued_cost_fraction_initial_cap": 0.09550577727915814,
    "mean_contract_rate": 0.039965738742457894,
    "maximum_ledger_error": 6.564505341220828e-20
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
    "maximum_relative_cash_error": 1.237491898111909e-15,
    "maximum_absolute_share_error": 1.6653345369377348e-15,
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
      "minimum": -0.1521839111766602,
      "maximum": -0.014601938650045075,
      "mean": -0.10090920326414493,
      "median": -0.10766526712566458,
      "quantile_05": -0.1467566303871187,
      "quantile_95": -0.05468585021634573
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
      "minimum": 0.2732500282634075,
      "maximum": 0.7655307384801935,
      "mean": 0.5325566354745231,
      "median": 0.5267221512996514,
      "quantile_05": 0.36831283346355576,
      "quantile_95": 0.7033772881781797
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
        "daily_volatility": 0.017994650375576765,
        "excess_kurtosis": 6.623645309660153,
        "return_acf_1": -0.1521839111766602,
        "abs_return_acf_1": 0.3269342750932607,
        "abs_return_acf_5": 0.21873487494246804,
        "abs_return_acf_20": 0.2375518079996809,
        "quantile_01": -0.0560292282478934,
        "quantile_99": 0.044615950594489674,
        "hill_tail_index": 3.0597990004220503
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019303025619925127,
        "excess_kurtosis": 7.607400059431221,
        "return_acf_1": -0.071763651341768,
        "abs_return_acf_1": 0.2991411196576819,
        "abs_return_acf_5": 0.3047921658278125,
        "abs_return_acf_20": 0.2884612399360631,
        "quantile_01": -0.06400852073121667,
        "quantile_99": 0.05515897171929922,
        "hill_tail_index": 3.0615837811396798
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021484736292093565,
        "excess_kurtosis": 12.940714614975166,
        "return_acf_1": -0.12181534426128006,
        "abs_return_acf_1": 0.4382593748130785,
        "abs_return_acf_5": 0.41626376529805237,
        "abs_return_acf_20": 0.32228477386016435,
        "quantile_01": -0.06740773895925123,
        "quantile_99": 0.0599733488322722,
        "hill_tail_index": 2.6917116076834797
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017394800664602087,
        "excess_kurtosis": 6.691557593079491,
        "return_acf_1": -0.13096686475457844,
        "abs_return_acf_1": 0.2871509126086559,
        "abs_return_acf_5": 0.2658823018133114,
        "abs_return_acf_20": 0.2723143390644144,
        "quantile_01": -0.05393699099969012,
        "quantile_99": 0.048847508372500084,
        "hill_tail_index": 2.7464574155013683
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018142355781901754,
        "excess_kurtosis": 5.581905362335599,
        "return_acf_1": -0.11570171546378392,
        "abs_return_acf_1": 0.3565302370958524,
        "abs_return_acf_5": 0.19004376488816305,
        "abs_return_acf_20": 0.2319509545384282,
        "quantile_01": -0.052264982852243,
        "quantile_99": 0.051202694135167384,
        "hill_tail_index": 3.042575022506156
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0202271843252318,
        "excess_kurtosis": 10.670907939831213,
        "return_acf_1": -0.09954949352167124,
        "abs_return_acf_1": 0.387448696560034,
        "abs_return_acf_5": 0.301679548549162,
        "abs_return_acf_20": 0.30436224850623134,
        "quantile_01": -0.07113318353769864,
        "quantile_99": 0.05242997994018844,
        "hill_tail_index": 2.975898387459157
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021523519790862852,
        "excess_kurtosis": 6.439654695047139,
        "return_acf_1": -0.09150522671863619,
        "abs_return_acf_1": 0.3623133194893054,
        "abs_return_acf_5": 0.3261108507676712,
        "abs_return_acf_20": 0.301962699605015,
        "quantile_01": -0.07370222121595024,
        "quantile_99": 0.07213701258403156,
        "hill_tail_index": 4.673964864412738
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02105552053161387,
        "excess_kurtosis": 8.091762480670425,
        "return_acf_1": -0.11379053718166009,
        "abs_return_acf_1": 0.33795996620080515,
        "abs_return_acf_5": 0.32546751080901914,
        "abs_return_acf_20": 0.3140813193610378,
        "quantile_01": -0.06840398467608362,
        "quantile_99": 0.06065790439249154,
        "hill_tail_index": 2.8106131690746103
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017699871816657813,
        "excess_kurtosis": 5.444747110976442,
        "return_acf_1": -0.07850638879507535,
        "abs_return_acf_1": 0.3412201198488588,
        "abs_return_acf_5": 0.28306869602759965,
        "abs_return_acf_20": 0.2511101859556028,
        "quantile_01": -0.05381107429770457,
        "quantile_99": 0.052045781324366484,
        "hill_tail_index": 3.198564379576727
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022455674462785607,
        "excess_kurtosis": 10.852642575068872,
        "return_acf_1": -0.07326975296526748,
        "abs_return_acf_1": 0.4767486452776066,
        "abs_return_acf_5": 0.44469180954976206,
        "abs_return_acf_20": 0.3766555509285475,
        "quantile_01": -0.06901705663638345,
        "quantile_99": 0.08075278849858548,
        "hill_tail_index": 2.6976091118761003
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020724530629609557,
        "excess_kurtosis": 7.273484131170758,
        "return_acf_1": -0.14130869166225854,
        "abs_return_acf_1": 0.39039774965267043,
        "abs_return_acf_5": 0.33306402214989766,
        "abs_return_acf_20": 0.27709240724302536,
        "quantile_01": -0.06325359570478128,
        "quantile_99": 0.05123903137998477,
        "hill_tail_index": 3.1801063954128446
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02134822495831912,
        "excess_kurtosis": 7.677708817341156,
        "return_acf_1": -0.08469185899714092,
        "abs_return_acf_1": 0.4034241474396564,
        "abs_return_acf_5": 0.3328779863161797,
        "abs_return_acf_20": 0.288387737849844,
        "quantile_01": -0.07768579269781865,
        "quantile_99": 0.060772912272536776,
        "hill_tail_index": 3.3403363006761815
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017143646963603203,
        "excess_kurtosis": 4.738710604168512,
        "return_acf_1": -0.05801114328050706,
        "abs_return_acf_1": 0.2620716260924466,
        "abs_return_acf_5": 0.19080537085096705,
        "abs_return_acf_20": 0.15577544734027335,
        "quantile_01": -0.05141365088600142,
        "quantile_99": 0.04808361067543429,
        "hill_tail_index": 4.524944776803252
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019096156916031216,
        "excess_kurtosis": 6.713390067543406,
        "return_acf_1": -0.014601938650045075,
        "abs_return_acf_1": 0.3586187368944487,
        "abs_return_acf_5": 0.3539487531168104,
        "abs_return_acf_20": 0.2914632891535266,
        "quantile_01": -0.05852730661026934,
        "quantile_99": 0.05466930995950922,
        "hill_tail_index": 2.710086953505301
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017906888852338675,
        "excess_kurtosis": 3.8064062544111694,
        "return_acf_1": -0.1060659588429384,
        "abs_return_acf_1": 0.35903959444103534,
        "abs_return_acf_5": 0.28057230369881103,
        "abs_return_acf_20": 0.24514776866371685,
        "quantile_01": -0.06035123112471711,
        "quantile_99": 0.04811254924725022,
        "hill_tail_index": 5.0135288465600025
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019628660955635518,
        "excess_kurtosis": 14.779044382105827,
        "return_acf_1": -0.14565151977678112,
        "abs_return_acf_1": 0.45527759741295976,
        "abs_return_acf_5": 0.2921927348443909,
        "abs_return_acf_20": 0.20986417953846453,
        "quantile_01": -0.057930460113859474,
        "quantile_99": 0.052923330088738674,
        "hill_tail_index": 3.2882780208043494
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02036403190843957,
        "excess_kurtosis": 9.183466173980184,
        "return_acf_1": -0.12471975766419237,
        "abs_return_acf_1": 0.42132208312300606,
        "abs_return_acf_5": 0.2505205789370513,
        "abs_return_acf_20": 0.2644806756685227,
        "quantile_01": -0.06102526196930751,
        "quantile_99": 0.05806875642498968,
        "hill_tail_index": 3.4515989113226397
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021551881660323353,
        "excess_kurtosis": 14.99109683103481,
        "return_acf_1": -0.06704372954990058,
        "abs_return_acf_1": 0.48577758764428897,
        "abs_return_acf_5": 0.3321798577882044,
        "abs_return_acf_20": 0.2511975864448695,
        "quantile_01": -0.07060516523617387,
        "quantile_99": 0.05726110391434533,
        "hill_tail_index": 2.4589117985576507
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01945661935561815,
        "excess_kurtosis": 10.224484058634092,
        "return_acf_1": -0.13223769962426227,
        "abs_return_acf_1": 0.38237076454393815,
        "abs_return_acf_5": 0.2870657529104203,
        "abs_return_acf_20": 0.24505168447657566,
        "quantile_01": -0.05690862730514449,
        "quantile_99": 0.051760660785142534,
        "hill_tail_index": 2.9273902699271375
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018189940388382744,
        "excess_kurtosis": 3.5554188169032344,
        "return_acf_1": -0.05753880469678983,
        "abs_return_acf_1": 0.2200383603180583,
        "abs_return_acf_5": 0.1725290315687921,
        "abs_return_acf_20": 0.20283279865688622,
        "quantile_01": -0.05516366707784165,
        "quantile_99": 0.05570620198838474,
        "hill_tail_index": 4.442746487609659
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01896183894152361,
        "excess_kurtosis": 6.941605125812281,
        "return_acf_1": -0.11129044884688677,
        "abs_return_acf_1": 0.3734284730570929,
        "abs_return_acf_5": 0.3619392042364765,
        "abs_return_acf_20": 0.2842866869738462,
        "quantile_01": -0.05324903161720784,
        "quantile_99": 0.052514836777518586,
        "hill_tail_index": 3.623899851395104
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01928684236741135,
        "excess_kurtosis": 7.9771439729274825,
        "return_acf_1": -0.08330094220498023,
        "abs_return_acf_1": 0.4005200420057973,
        "abs_return_acf_5": 0.2496310028249699,
        "abs_return_acf_20": 0.3045885252538569,
        "quantile_01": -0.061917023269393086,
        "quantile_99": 0.05028980237812223,
        "hill_tail_index": 2.767579166199394
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01674899604064567,
        "excess_kurtosis": 5.715084521973148,
        "return_acf_1": -0.1128213231090276,
        "abs_return_acf_1": 0.37683883903455706,
        "abs_return_acf_5": 0.2692789680031601,
        "abs_return_acf_20": 0.23571266706159327,
        "quantile_01": -0.05476233018122355,
        "quantile_99": 0.04535154914476818,
        "hill_tail_index": 3.560313029545898
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023906150362964364,
        "excess_kurtosis": 23.770607142977735,
        "return_acf_1": -0.13947716490122938,
        "abs_return_acf_1": 0.4547217997915378,
        "abs_return_acf_5": 0.3929872114667073,
        "abs_return_acf_20": 0.3376200355126941,
        "quantile_01": -0.07697371786813911,
        "quantile_99": 0.06937902725858575,
        "hill_tail_index": 2.339127642901262
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019835254828175566,
        "excess_kurtosis": 6.142493852992942,
        "return_acf_1": -0.07395356373367767,
        "abs_return_acf_1": 0.3070794094239431,
        "abs_return_acf_5": 0.24916994935225317,
        "abs_return_acf_20": 0.32130209986461755,
        "quantile_01": -0.06803422056821559,
        "quantile_99": 0.055614913404900906,
        "hill_tail_index": 4.102788351466337
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021166917661497368,
        "excess_kurtosis": 7.751300237219555,
        "return_acf_1": -0.14593106490243765,
        "abs_return_acf_1": 0.5306612115517622,
        "abs_return_acf_5": 0.39769901070947505,
        "abs_return_acf_20": 0.38807672630175816,
        "quantile_01": -0.06897356326086283,
        "quantile_99": 0.07045143113482452,
        "hill_tail_index": 3.9972038933794196
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01664381466431025,
        "excess_kurtosis": 6.901964828559581,
        "return_acf_1": -0.05235161473234598,
        "abs_return_acf_1": 0.2856970681281648,
        "abs_return_acf_5": 0.18983463781683516,
        "abs_return_acf_20": 0.26167336819322157,
        "quantile_01": -0.0497846753537904,
        "quantile_99": 0.04484815923626262,
        "hill_tail_index": 3.899257328989206
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017338029850458778,
        "excess_kurtosis": 6.034788106348991,
        "return_acf_1": -0.07052931810377155,
        "abs_return_acf_1": 0.3062795900534622,
        "abs_return_acf_5": 0.2574747700313772,
        "abs_return_acf_20": 0.25127858323666863,
        "quantile_01": -0.05263760513059063,
        "quantile_99": 0.04561052410688632,
        "hill_tail_index": 3.4037249531227816
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019046374253743868,
        "excess_kurtosis": 7.139403416294526,
        "return_acf_1": -0.1474320930564032,
        "abs_return_acf_1": 0.41173159071972365,
        "abs_return_acf_5": 0.3443901025018262,
        "abs_return_acf_20": 0.27938280135301824,
        "quantile_01": -0.05838538892406012,
        "quantile_99": 0.05278926648527293,
        "hill_tail_index": 3.348661250139675
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017374879087939152,
        "excess_kurtosis": 5.808830868963838,
        "return_acf_1": -0.10926457540839077,
        "abs_return_acf_1": 0.30566609803615535,
        "abs_return_acf_5": 0.20849837719611747,
        "abs_return_acf_20": 0.18247393624245395,
        "quantile_01": -0.05292819282329017,
        "quantile_99": 0.04370035507512816,
        "hill_tail_index": 4.090911326117983
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
