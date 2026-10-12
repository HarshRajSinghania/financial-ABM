# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27250
Run ID: `31b45ec5532b205fe9da4908d846e4454961d8e26fa231a4eb69dedc19a94847`
Result fingerprint: `01e8354489fb24a2fe7509391f84143c78ab7ea731685068ea1a6578d66838f7`

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
    "equal_weight_sd": -0.8234642857142824,
    "equal_weight_raw": -12.351964285714239,
    "fixed_start_cap_weight_sd": -0.8774244107319489,
    "fixed_start_cap_weight_raw": -13.161366160979233,
    "end_cap_weight_sd": -0.8791825047464012,
    "end_cap_weight_raw": -13.18773757119602
  },
  "full_period_change": {
    "equal_weight_sd": -1.2867380952380902,
    "equal_weight_raw": -19.301071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2048277116402073,
    "inflation_mean_sd": 0.5788032407407409
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1289166666666699,
    "equal_weight_raw": 1.933750000000048,
    "fixed_start_cap_weight_sd": 0.07495654164900326,
    "fixed_start_cap_weight_raw": 1.1243481247350486,
    "end_cap_weight_sd": 0.07319844763455097,
    "end_cap_weight_raw": 1.0979767145182646
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.9073809523809494,
      "change_raw": -13.610714285714241,
      "decay_adjusted_gain_sd": 0.04500000000000295
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8954365079365049,
      "change_raw": -13.431547619047572,
      "decay_adjusted_gain_sd": 0.056944444444447635
    },
    "small": {
      "count": 18,
      "change_sd": -0.7734920634920601,
      "change_raw": -11.602380952380901,
      "decay_adjusted_gain_sd": 0.17888888888889215
    },
    "large_minus_small_sd": -0.13388888888888928,
    "large_minus_small_raw": -2.008333333333339
  },
  "inflation": {
    "initial_mean_sd": 0.34975000000000006,
    "final_mean_sd": 0.5706666666666668,
    "mean_sd": 0.4983422148209825,
    "mean_absolute_raw_gap": 7.475133222314739,
    "final_absolute_raw_gap": 8.56,
    "mean_range_fraction": 0.0747513322231474
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.2952569248480898,
    "final_wealth_share": 0.3349793641654931
  },
  "pricing_slope": {
    "mean": -0.0022191811845080254,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.017823643091606275,
    "real_improvement_cost": 0.008158312014708416,
    "washing_cost": 0.00966533107689786,
    "fine_transfer": 0.039039578881113896,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.056863221972720174,
    "resource_cost_fraction_initial_cap": 0.0005941214363868758,
    "private_net_outflow_fraction_initial_cap": 0.0018954407324240057,
    "fine_transfer_fraction_initial_cap": 0.00130131929603713,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00436518884579246,
    "unapplied_final_day_resource_cost": 0.0002994368684704806
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 216.98706488469952,
    "beneficial_raw_gain_per_resource_cost": 3254.8059732704924,
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
    "accrued_cost": 2.794712047150314,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.18147842904016315,
    "accrued_cost_fraction_initial_cap": 0.0931570682383438,
    "mean_contract_rate": 0.038713178924617286,
    "maximum_ledger_error": 9.232659125071874e-20
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
    "maximum_relative_cash_error": 1.367262062440475e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.22952611810270657,
      "maximum": -0.08158062422044882,
      "mean": -0.14249576887381252,
      "median": -0.13598648565107574,
      "quantile_05": -0.1999722678697275,
      "quantile_95": -0.10374565288424548
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
      "minimum": 0.2459674123463321,
      "maximum": 0.7965451069316112,
      "mean": 0.4848325748277152,
      "median": 0.42447257552847045,
      "quantile_05": 0.27780171477909416,
      "quantile_95": 0.7474526380885143
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
        "daily_volatility": 0.018346861244383606,
        "excess_kurtosis": 10.957865737275293,
        "return_acf_1": -0.13818738738958922,
        "abs_return_acf_1": 0.3038083750616965,
        "abs_return_acf_5": 0.32449030554483216,
        "abs_return_acf_20": 0.3188152486662246,
        "quantile_01": -0.062314861593538176,
        "quantile_99": 0.03938186425682471,
        "hill_tail_index": 2.7801425751021407
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018389697637472606,
        "excess_kurtosis": 15.657481503095553,
        "return_acf_1": -0.1749744648438572,
        "abs_return_acf_1": 0.37094046945167214,
        "abs_return_acf_5": 0.4019202529380677,
        "abs_return_acf_20": 0.2688125107753967,
        "quantile_01": -0.05997904563960958,
        "quantile_99": 0.042261207484968685,
        "hill_tail_index": 2.0839956942065316
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020046336526819405,
        "excess_kurtosis": 8.378592261302082,
        "return_acf_1": -0.11275524609176583,
        "abs_return_acf_1": 0.43719737491413824,
        "abs_return_acf_5": 0.38160189140158823,
        "abs_return_acf_20": 0.3085762342098847,
        "quantile_01": -0.0621360675348234,
        "quantile_99": 0.062054228455381874,
        "hill_tail_index": 3.345641193062629
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017053045682224627,
        "excess_kurtosis": 11.633731529787367,
        "return_acf_1": -0.11198995400961168,
        "abs_return_acf_1": 0.22912819491080766,
        "abs_return_acf_5": 0.29405918576045825,
        "abs_return_acf_20": 0.1891074826763023,
        "quantile_01": -0.05187688700062547,
        "quantile_99": 0.040669838610358215,
        "hill_tail_index": 2.372203772482706
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01914105201729944,
        "excess_kurtosis": 24.904233387126375,
        "return_acf_1": -0.1550306820558155,
        "abs_return_acf_1": 0.372480468309541,
        "abs_return_acf_5": 0.3775895374112441,
        "abs_return_acf_20": 0.23670934700109247,
        "quantile_01": -0.06623044006334033,
        "quantile_99": 0.04200460815073805,
        "hill_tail_index": 2.1166251700018983
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019162671179384035,
        "excess_kurtosis": 15.142261350384484,
        "return_acf_1": -0.15191522924978956,
        "abs_return_acf_1": 0.33991267263853453,
        "abs_return_acf_5": 0.37212318344465856,
        "abs_return_acf_20": 0.27617555606036054,
        "quantile_01": -0.06470840935216557,
        "quantile_99": 0.044173370138497293,
        "hill_tail_index": 2.6336674815478553
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02039479307719427,
        "excess_kurtosis": 24.119975971129687,
        "return_acf_1": -0.1614426953586383,
        "abs_return_acf_1": 0.3655025554149071,
        "abs_return_acf_5": 0.4639563777401726,
        "abs_return_acf_20": 0.195665047151805,
        "quantile_01": -0.06694211059675573,
        "quantile_99": 0.0550689360777258,
        "hill_tail_index": 2.1112285170978717
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018093137042797462,
        "excess_kurtosis": 8.388466295452774,
        "return_acf_1": -0.18927755209073724,
        "abs_return_acf_1": 0.3917882413767208,
        "abs_return_acf_5": 0.43302751981906706,
        "abs_return_acf_20": 0.33314545065876594,
        "quantile_01": -0.060246973040590845,
        "quantile_99": 0.04642454820886007,
        "hill_tail_index": 3.040089211882895
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01935951590348151,
        "excess_kurtosis": 7.090816474260661,
        "return_acf_1": -0.08158062422044882,
        "abs_return_acf_1": 0.41151019706534503,
        "abs_return_acf_5": 0.4569914313358528,
        "abs_return_acf_20": 0.29715910461981593,
        "quantile_01": -0.06087862588152584,
        "quantile_99": 0.05324474002018506,
        "hill_tail_index": 3.176262275935961
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01871027717213873,
        "excess_kurtosis": 19.055888049690076,
        "return_acf_1": -0.15787676046093085,
        "abs_return_acf_1": 0.31821790519172566,
        "abs_return_acf_5": 0.40605310892634533,
        "abs_return_acf_20": 0.1988132273407293,
        "quantile_01": -0.05773972425640195,
        "quantile_99": 0.044787028857625165,
        "hill_tail_index": 2.1966940957278918
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019399160491251417,
        "excess_kurtosis": 4.984166428158415,
        "return_acf_1": -0.12975076644690675,
        "abs_return_acf_1": 0.41082455104068666,
        "abs_return_acf_5": 0.3235168795837017,
        "abs_return_acf_20": 0.29739631821703505,
        "quantile_01": -0.06301892990404563,
        "quantile_99": 0.0596112478269867,
        "hill_tail_index": 3.59447053024015
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019257084515942074,
        "excess_kurtosis": 4.294511894056732,
        "return_acf_1": -0.13579701240534386,
        "abs_return_acf_1": 0.40150534255708686,
        "abs_return_acf_5": 0.38413728904521793,
        "abs_return_acf_20": 0.36368252392954387,
        "quantile_01": -0.06760172214795987,
        "quantile_99": 0.05483969879765011,
        "hill_tail_index": 4.65220337974196
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02060544242351156,
        "excess_kurtosis": 23.63028276567986,
        "return_acf_1": -0.1667087976221182,
        "abs_return_acf_1": 0.48662307656523085,
        "abs_return_acf_5": 0.48688556556404405,
        "abs_return_acf_20": 0.32839575738967564,
        "quantile_01": -0.06686135198626755,
        "quantile_99": 0.04621537500272005,
        "hill_tail_index": 1.9025000505954042
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01747899204492508,
        "excess_kurtosis": 3.632807906009261,
        "return_acf_1": -0.10533901425216081,
        "abs_return_acf_1": 0.35056613093037176,
        "abs_return_acf_5": 0.32017225024599444,
        "abs_return_acf_20": 0.282318028470536,
        "quantile_01": -0.05484762975871145,
        "quantile_99": 0.04782557184149171,
        "hill_tail_index": 4.00969308082867
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02002510321225657,
        "excess_kurtosis": 5.841533256654268,
        "return_acf_1": -0.13617595889680764,
        "abs_return_acf_1": 0.38304067524274915,
        "abs_return_acf_5": 0.37029763614511335,
        "abs_return_acf_20": 0.26183572935330973,
        "quantile_01": -0.06401278368249486,
        "quantile_99": 0.05613920233872244,
        "hill_tail_index": 3.7880263124264846
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020648711865655194,
        "excess_kurtosis": 6.888094528006322,
        "return_acf_1": -0.19258611811482465,
        "abs_return_acf_1": 0.4614904744227373,
        "abs_return_acf_5": 0.45570252667828454,
        "abs_return_acf_20": 0.37906587285946436,
        "quantile_01": -0.06871884247890539,
        "quantile_99": 0.06049610195794394,
        "hill_tail_index": 3.6912535172325116
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02173209204447813,
        "excess_kurtosis": 12.531639127670047,
        "return_acf_1": -0.20601548130555708,
        "abs_return_acf_1": 0.5064105416859398,
        "abs_return_acf_5": 0.4888924294172494,
        "abs_return_acf_20": 0.3230878901638768,
        "quantile_01": -0.07333318321722622,
        "quantile_99": 0.05835063175097146,
        "hill_tail_index": 2.214700469492728
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01926558365639052,
        "excess_kurtosis": 6.995316650808897,
        "return_acf_1": -0.10964427917586134,
        "abs_return_acf_1": 0.4682606642079491,
        "abs_return_acf_5": 0.34951894853894505,
        "abs_return_acf_20": 0.25110415396820873,
        "quantile_01": -0.055371142082768,
        "quantile_99": 0.0554302827584765,
        "hill_tail_index": 3.4361875391235137
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01878127184662769,
        "excess_kurtosis": 5.25647549212839,
        "return_acf_1": -0.12138193718493552,
        "abs_return_acf_1": 0.3810560896387652,
        "abs_return_acf_5": 0.3749286657335765,
        "abs_return_acf_20": 0.2883496429570843,
        "quantile_01": -0.06007897060020153,
        "quantile_99": 0.049549826459974425,
        "hill_tail_index": 4.498771650301822
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020570158268946398,
        "excess_kurtosis": 6.305990324631775,
        "return_acf_1": -0.12518565228148062,
        "abs_return_acf_1": 0.4863943551724766,
        "abs_return_acf_5": 0.4376927456208505,
        "abs_return_acf_20": 0.334124200444716,
        "quantile_01": -0.0722821231328655,
        "quantile_99": 0.06500010023395643,
        "hill_tail_index": 3.3039810451444467
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01971891968019419,
        "excess_kurtosis": 6.888499216009031,
        "return_acf_1": -0.10945233107231059,
        "abs_return_acf_1": 0.41087360868611084,
        "abs_return_acf_5": 0.4362313732619593,
        "abs_return_acf_20": 0.3229337920073535,
        "quantile_01": -0.061347995184390804,
        "quantile_99": 0.0596022178674177,
        "hill_tail_index": 3.2625849394100155
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01866363473108057,
        "excess_kurtosis": 15.071858857542285,
        "return_acf_1": -0.11823305669154854,
        "abs_return_acf_1": 0.304107179261059,
        "abs_return_acf_5": 0.3437237609547492,
        "abs_return_acf_20": 0.16649266719201694,
        "quantile_01": -0.06251885769035785,
        "quantile_99": 0.04718907441807882,
        "hill_tail_index": 2.3126895746439535
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022491061742696963,
        "excess_kurtosis": 8.888843886147958,
        "return_acf_1": -0.10244199358322381,
        "abs_return_acf_1": 0.505878593433765,
        "abs_return_acf_5": 0.4215032745666889,
        "abs_return_acf_20": 0.40916558942773495,
        "quantile_01": -0.06966607863544687,
        "quantile_99": 0.06557416242135021,
        "hill_tail_index": 3.719848053457625
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01976376589981693,
        "excess_kurtosis": 10.861246343839591,
        "return_acf_1": -0.15613953432107586,
        "abs_return_acf_1": 0.4068133566624446,
        "abs_return_acf_5": 0.3760476391079295,
        "abs_return_acf_20": 0.3060624357872947,
        "quantile_01": -0.06038895617135686,
        "quantile_99": 0.05842807405910165,
        "hill_tail_index": 2.8599634674424514
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0215743535416464,
        "excess_kurtosis": 8.106390563493335,
        "return_acf_1": -0.22952611810270657,
        "abs_return_acf_1": 0.5419092673871932,
        "abs_return_acf_5": 0.40194496971742893,
        "abs_return_acf_20": 0.34350829977786934,
        "quantile_01": -0.06838113859078311,
        "quantile_99": 0.06667067149251364,
        "hill_tail_index": 3.7095304903657795
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017918573613244754,
        "excess_kurtosis": 4.755671849631123,
        "return_acf_1": -0.17740148000654413,
        "abs_return_acf_1": 0.39911426793483157,
        "abs_return_acf_5": 0.3012757972053676,
        "abs_return_acf_20": 0.23888376154473615,
        "quantile_01": -0.0531200021178692,
        "quantile_99": 0.047296651469528,
        "hill_tail_index": 3.6730894628824937
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019726861442216793,
        "excess_kurtosis": 5.388244953057827,
        "return_acf_1": -0.14364968516335905,
        "abs_return_acf_1": 0.38491691560527563,
        "abs_return_acf_5": 0.3850831558111649,
        "abs_return_acf_20": 0.28703014021954637,
        "quantile_01": -0.05998776316552878,
        "quantile_99": 0.060081667071284796,
        "hill_tail_index": 3.9445556897259437
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018962022784502784,
        "excess_kurtosis": 5.6623468756438005,
        "return_acf_1": -0.13059903827671848,
        "abs_return_acf_1": 0.4149090737876232,
        "abs_return_acf_5": 0.34142492551546005,
        "abs_return_acf_20": 0.29520880987376935,
        "quantile_01": -0.061743731748093285,
        "quantile_99": 0.055205590573646865,
        "hill_tail_index": 5.115054786984301
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01957900987705237,
        "excess_kurtosis": 5.015060890859978,
        "return_acf_1": -0.1308293966657126,
        "abs_return_acf_1": 0.42741674270151964,
        "abs_return_acf_5": 0.3353030530499033,
        "abs_return_acf_20": 0.29145003753684107,
        "quantile_01": -0.05953426790231572,
        "quantile_99": 0.050305081298487146,
        "hill_tail_index": 3.1854083319188584
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02049381666124695,
        "excess_kurtosis": 9.881030333601242,
        "return_acf_1": -0.1129848188739955,
        "abs_return_acf_1": 0.44398277026084043,
        "abs_return_acf_5": 0.34188856722371685,
        "abs_return_acf_20": 0.3236143234359975,
        "quantile_01": -0.06837239151638498,
        "quantile_99": 0.053751989939173954,
        "hill_tail_index": 2.79291603091872
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
