# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27088
Run ID: `21ced6b5c266031c26e73eb4eb600fbe94736b8a59ba75e46f95685861c80517`
Result fingerprint: `737e85aa465d51dbe8b93b950e1b0bb40f3ab7140ac42568f21af3cd6446d62c`

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
    "equal_weight_sd": -0.653880952380949,
    "equal_weight_raw": -9.808214285714238,
    "fixed_start_cap_weight_sd": -0.681031801556935,
    "fixed_start_cap_weight_raw": -10.215477023354023,
    "end_cap_weight_sd": -0.6665032953224661,
    "end_cap_weight_raw": -9.997549429836987
  },
  "full_period_change": {
    "equal_weight_sd": -0.9937380952380904,
    "equal_weight_raw": -14.906071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9280310846560802,
    "inflation_mean_sd": 0.5392423941798943
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2985000000000031,
    "equal_weight_raw": 4.477500000000047,
    "fixed_start_cap_weight_sd": 0.27134915082401756,
    "fixed_start_cap_weight_raw": 4.070237262360262,
    "end_cap_weight_sd": 0.28587765705848645,
    "end_cap_weight_raw": 4.288164855877298
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5165476190476158,
      "change_raw": -7.748214285714237,
      "decay_adjusted_gain_sd": 0.4358333333333366
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7434920634920602,
      "change_raw": -11.152380952380904,
      "decay_adjusted_gain_sd": 0.208888888888892
    },
    "small": {
      "count": 18,
      "change_sd": -0.6319642857142825,
      "change_raw": -9.479464285714238,
      "decay_adjusted_gain_sd": 0.32041666666666985
    },
    "large_minus_small_sd": 0.11541666666666672,
    "large_minus_small_raw": 1.7312500000000008
  },
  "inflation": {
    "initial_mean_sd": 0.2685833333333333,
    "final_mean_sd": 0.5628333333333334,
    "mean_sd": 0.43032153760754926,
    "mean_absolute_raw_gap": 6.4548230641132385,
    "final_absolute_raw_gap": 8.442499999999999,
    "mean_range_fraction": 0.06454823064113238
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.3,
    "initial_wealth_share": 0.25596845459474477,
    "final_wealth_share": 0.313912935543519
  },
  "pricing_slope": {
    "mean": -0.0009998708808651989,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.0931937346429082,
    "real_improvement_cost": 0.06498829991003277,
    "washing_cost": 0.02820543473287542,
    "fine_transfer": 0.011873527332280507,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1050672619751887,
    "resource_cost_fraction_initial_cap": 0.0031064578214302745,
    "private_net_outflow_fraction_initial_cap": 0.0035022420658396246,
    "fine_transfer_fraction_initial_cap": 0.0003957842444093504,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.012120772285017862,
    "unapplied_final_day_resource_cost": 0.00221602815249111
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 96.09015063419335,
    "beneficial_raw_gain_per_resource_cost": 1441.3522595129002,
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
    "accrued_cost": 3.0146573463873296,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.03846687019685357,
    "accrued_cost_fraction_initial_cap": 0.10048857821291102,
    "mean_contract_rate": 0.040738724591261335,
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
    "maximum_relative_cash_error": 1.9002061477554723e-15,
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
      "minimum": -0.21198398795282053,
      "maximum": -0.01890359222133247,
      "mean": -0.1389640210071504,
      "median": -0.1425984259478454,
      "quantile_05": -0.20704066924914222,
      "quantile_95": -0.06849966043639197
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
      "minimum": 0.29004425903407804,
      "maximum": 0.7443471685045271,
      "mean": 0.5025038966027142,
      "median": 0.5171641885172573,
      "quantile_05": 0.3210120354585327,
      "quantile_95": 0.7119076943059671
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
        "daily_volatility": 0.018792971761257906,
        "excess_kurtosis": 4.346303960441028,
        "return_acf_1": -0.10471371022988749,
        "abs_return_acf_1": 0.2997412458902392,
        "abs_return_acf_5": 0.3550783707858003,
        "abs_return_acf_20": 0.30464685822086135,
        "quantile_01": -0.05271462757270586,
        "quantile_99": 0.0586681158914141,
        "hill_tail_index": 4.032560461080553
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01857980123635581,
        "excess_kurtosis": 8.255170997971309,
        "return_acf_1": -0.15246955022527608,
        "abs_return_acf_1": 0.42219736258612317,
        "abs_return_acf_5": 0.37582271804563777,
        "abs_return_acf_20": 0.3144596460933141,
        "quantile_01": -0.06228779296392937,
        "quantile_99": 0.05206752154401212,
        "hill_tail_index": 3.3004789515523076
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01713500803716373,
        "excess_kurtosis": 8.170064010284733,
        "return_acf_1": -0.12130181569032865,
        "abs_return_acf_1": 0.387407597426018,
        "abs_return_acf_5": 0.3406644929911772,
        "abs_return_acf_20": 0.3307324741536496,
        "quantile_01": -0.05126611376900637,
        "quantile_99": 0.04315836387454708,
        "hill_tail_index": 2.695969232065865
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019869488829352938,
        "excess_kurtosis": 10.39895529240252,
        "return_acf_1": -0.21198398795282053,
        "abs_return_acf_1": 0.5176270733673294,
        "abs_return_acf_5": 0.4180613537982836,
        "abs_return_acf_20": 0.3682199108070032,
        "quantile_01": -0.0628165807555119,
        "quantile_99": 0.051812672337689866,
        "hill_tail_index": 2.805727971812173
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018279841895817158,
        "excess_kurtosis": 7.183725025296242,
        "return_acf_1": -0.21021744922745453,
        "abs_return_acf_1": 0.4059759513190217,
        "abs_return_acf_5": 0.3176786321634176,
        "abs_return_acf_20": 0.28748408178504786,
        "quantile_01": -0.05847481874156359,
        "quantile_99": 0.0487248829285972,
        "hill_tail_index": 3.1100849817825695
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01677297025891826,
        "excess_kurtosis": 4.910558145715143,
        "return_acf_1": -0.10857079843688919,
        "abs_return_acf_1": 0.29564266945812856,
        "abs_return_acf_5": 0.2197347966760136,
        "abs_return_acf_20": 0.16756039698512531,
        "quantile_01": -0.05104226274027337,
        "quantile_99": 0.043493575804272336,
        "hill_tail_index": 3.3275301313335865
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019236437573990295,
        "excess_kurtosis": 6.411605355932391,
        "return_acf_1": -0.1254500124086214,
        "abs_return_acf_1": 0.35391625162216,
        "abs_return_acf_5": 0.36450253383633807,
        "abs_return_acf_20": 0.3080153736258506,
        "quantile_01": -0.059045537468874205,
        "quantile_99": 0.0481231289658699,
        "hill_tail_index": 3.452740169185038
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020904505806432064,
        "excess_kurtosis": 11.792894388928698,
        "return_acf_1": -0.1426414886674265,
        "abs_return_acf_1": 0.4508211443902387,
        "abs_return_acf_5": 0.3958879576057132,
        "abs_return_acf_20": 0.34218983456102814,
        "quantile_01": -0.0719437970456305,
        "quantile_99": 0.05052835838580349,
        "hill_tail_index": 2.524498595707253
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017307984130961282,
        "excess_kurtosis": 8.01575286159053,
        "return_acf_1": -0.0583774015484584,
        "abs_return_acf_1": 0.3380513204329768,
        "abs_return_acf_5": 0.30574138036471893,
        "abs_return_acf_20": 0.3759254882135574,
        "quantile_01": -0.04447338170416467,
        "quantile_99": 0.04683780469002481,
        "hill_tail_index": 2.814088653810292
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01861517563100906,
        "excess_kurtosis": 7.566747959706916,
        "return_acf_1": -0.14255536322826423,
        "abs_return_acf_1": 0.3819177438725681,
        "abs_return_acf_5": 0.2883097164883094,
        "abs_return_acf_20": 0.2682066825672569,
        "quantile_01": -0.06299239542989399,
        "quantile_99": 0.04816490096438214,
        "hill_tail_index": 3.3426933011029925
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019450545348929312,
        "excess_kurtosis": 6.6402206748941754,
        "return_acf_1": -0.09480214339593211,
        "abs_return_acf_1": 0.3747998154360314,
        "abs_return_acf_5": 0.3923880982615782,
        "abs_return_acf_20": 0.33156861932653914,
        "quantile_01": -0.06477880909489815,
        "quantile_99": 0.05658841506461981,
        "hill_tail_index": 3.8263124015729417
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01983151557616246,
        "excess_kurtosis": 7.905076759542437,
        "return_acf_1": -0.1516614597437101,
        "abs_return_acf_1": 0.4411376215905941,
        "abs_return_acf_5": 0.380341188421772,
        "abs_return_acf_20": 0.3143051010571076,
        "quantile_01": -0.06210134714563232,
        "quantile_99": 0.058378935384243796,
        "hill_tail_index": 3.264637486727888
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01769996379190276,
        "excess_kurtosis": 5.950798240884815,
        "return_acf_1": -0.18001762043561123,
        "abs_return_acf_1": 0.4156053604770535,
        "abs_return_acf_5": 0.3464271417991485,
        "abs_return_acf_20": 0.30767163843161444,
        "quantile_01": -0.056455461293464224,
        "quantile_99": 0.04652944200910237,
        "hill_tail_index": 2.661085130330278
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01880846122956224,
        "excess_kurtosis": 6.639769072211891,
        "return_acf_1": -0.14291721826663495,
        "abs_return_acf_1": 0.3844585921810609,
        "abs_return_acf_5": 0.29884259615103764,
        "abs_return_acf_20": 0.29509803001021606,
        "quantile_01": -0.06365421452571544,
        "quantile_99": 0.0499293280003761,
        "hill_tail_index": 3.2724755807352666
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02007349750108415,
        "excess_kurtosis": 12.328665440169752,
        "return_acf_1": -0.15239326089597835,
        "abs_return_acf_1": 0.44738657768868484,
        "abs_return_acf_5": 0.42583680064040785,
        "abs_return_acf_20": 0.2597917047300585,
        "quantile_01": -0.060321163295181966,
        "quantile_99": 0.04889383296043863,
        "hill_tail_index": 2.240737021275884
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019361913594281785,
        "excess_kurtosis": 5.464482498284818,
        "return_acf_1": -0.08087131018831065,
        "abs_return_acf_1": 0.37454149439513207,
        "abs_return_acf_5": 0.3743877085472081,
        "abs_return_acf_20": 0.3106295234887313,
        "quantile_01": -0.05810228695216906,
        "quantile_99": 0.05953121090833526,
        "hill_tail_index": 4.678161254269931
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01831008757012366,
        "excess_kurtosis": 7.211447524129863,
        "return_acf_1": -0.16831038039045235,
        "abs_return_acf_1": 0.3476566340051232,
        "abs_return_acf_5": 0.3448920697880506,
        "abs_return_acf_20": 0.3501918613086141,
        "quantile_01": -0.05794546383304048,
        "quantile_99": 0.05148831303981296,
        "hill_tail_index": 3.11736817757279
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02059061042433393,
        "excess_kurtosis": 9.449599972770766,
        "return_acf_1": -0.17477867092036792,
        "abs_return_acf_1": 0.45701179760790994,
        "abs_return_acf_5": 0.4619534305456145,
        "abs_return_acf_20": 0.3830825457664581,
        "quantile_01": -0.0713699306238432,
        "quantile_99": 0.05494262366773505,
        "hill_tail_index": 2.4651867580619937
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019833746811407475,
        "excess_kurtosis": 6.496189192330128,
        "return_acf_1": -0.17312689213667423,
        "abs_return_acf_1": 0.38321017741980684,
        "abs_return_acf_5": 0.3896105544590162,
        "abs_return_acf_20": 0.3633352813275454,
        "quantile_01": -0.06219015990786531,
        "quantile_99": 0.05265405555055922,
        "hill_tail_index": 3.898768181030555
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019028153543584322,
        "excess_kurtosis": 6.508139437191764,
        "return_acf_1": -0.19945083567029312,
        "abs_return_acf_1": 0.38562229437631346,
        "abs_return_acf_5": 0.33376349483565765,
        "abs_return_acf_20": 0.27015972392484244,
        "quantile_01": -0.06122701511206542,
        "quantile_99": 0.05857328131548675,
        "hill_tail_index": 3.37786632664675
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017321282218209583,
        "excess_kurtosis": 10.56357088339154,
        "return_acf_1": -0.12709608468535338,
        "abs_return_acf_1": 0.31544308724724063,
        "abs_return_acf_5": 0.33309016875553216,
        "abs_return_acf_20": 0.23749657186430842,
        "quantile_01": -0.05677121655357809,
        "quantile_99": 0.0441254320104867,
        "hill_tail_index": 2.9500989316846513
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017785760862434396,
        "excess_kurtosis": 6.898528982955771,
        "return_acf_1": -0.09410575749200109,
        "abs_return_acf_1": 0.3322037124546216,
        "abs_return_acf_5": 0.2675642197836885,
        "abs_return_acf_20": 0.2310453884032954,
        "quantile_01": -0.056038516489171804,
        "quantile_99": 0.04907150459302464,
        "hill_tail_index": 2.6868996979927777
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01908479393793541,
        "excess_kurtosis": 8.607009482373668,
        "return_acf_1": -0.10497756682536935,
        "abs_return_acf_1": 0.3380310095133096,
        "abs_return_acf_5": 0.3320855570492503,
        "abs_return_acf_20": 0.3224213421828258,
        "quantile_01": -0.06003036006214894,
        "quantile_99": 0.05147116015966289,
        "hill_tail_index": 3.243595753633785
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01923567770136976,
        "excess_kurtosis": 19.919664148303607,
        "return_acf_1": -0.1924834016567904,
        "abs_return_acf_1": 0.4173696603268337,
        "abs_return_acf_5": 0.37132287730987673,
        "abs_return_acf_20": 0.27925854486363205,
        "quantile_01": -0.05443458242386833,
        "quantile_99": 0.05045511204172591,
        "hill_tail_index": 3.0077333523922722
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018901151022183593,
        "excess_kurtosis": 10.35920214539491,
        "return_acf_1": -0.14521554905670475,
        "abs_return_acf_1": 0.3785515026534318,
        "abs_return_acf_5": 0.27320112592037304,
        "abs_return_acf_20": 0.23087154915678457,
        "quantile_01": -0.0515453964724955,
        "quantile_99": 0.04868662649016227,
        "hill_tail_index": 2.5822611068884043
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02120714057535531,
        "excess_kurtosis": 9.195323800981141,
        "return_acf_1": -0.12826267274330802,
        "abs_return_acf_1": 0.40177398299246914,
        "abs_return_acf_5": 0.44562829090542594,
        "abs_return_acf_20": 0.3595963013011547,
        "quantile_01": -0.07422031009054869,
        "quantile_99": 0.06421369173498327,
        "hill_tail_index": 3.2507459353276213
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018778348751385454,
        "excess_kurtosis": 5.383781569145285,
        "return_acf_1": -0.20315793816453828,
        "abs_return_acf_1": 0.4520620121428492,
        "abs_return_acf_5": 0.3361266841558736,
        "abs_return_acf_20": 0.339545584729279,
        "quantile_01": -0.058181310528123836,
        "quantile_99": 0.05186166804872709,
        "hill_tail_index": 3.573586783201846
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01698810883647681,
        "excess_kurtosis": 10.760305537698013,
        "return_acf_1": -0.01890359222133247,
        "abs_return_acf_1": 0.3724224459668618,
        "abs_return_acf_5": 0.3936590838324177,
        "abs_return_acf_20": 0.32472461610887327,
        "quantile_01": -0.04740992512758795,
        "quantile_99": 0.0464383972518085,
        "hill_tail_index": 2.3106408799911375
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020020529981976884,
        "excess_kurtosis": 10.55983503882435,
        "return_acf_1": -0.13552940896282548,
        "abs_return_acf_1": 0.4237569375494141,
        "abs_return_acf_5": 0.3260909680009975,
        "abs_return_acf_20": 0.2608874756873212,
        "quantile_01": -0.06752608799811319,
        "quantile_99": 0.05347539553356483,
        "hill_tail_index": 3.5586842429328818
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017956747283538445,
        "excess_kurtosis": 7.384207369952049,
        "return_acf_1": -0.12257728874689708,
        "abs_return_acf_1": 0.30096285661477845,
        "abs_return_acf_5": 0.3137937904661078,
        "abs_return_acf_20": 0.3261027221375298,
        "quantile_01": -0.05509620955181426,
        "quantile_99": 0.04867976112866061,
        "hill_tail_index": 3.124648177167861
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
