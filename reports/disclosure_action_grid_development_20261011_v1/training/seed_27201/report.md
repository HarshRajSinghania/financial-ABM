# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27201
Run ID: `d2dc4a5e463229fe973ce24e20921f24589f38a7224c9c14bf5fba2eaf09b7ca`
Result fingerprint: `2e040b22c6433dab4062666f597cdee6d786d405d5d121017fec78171abf737b`

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
    "equal_weight_sd": -0.7388188207901261,
    "equal_weight_raw": -11.082282311851893,
    "fixed_start_cap_weight_sd": -0.6522178071936449,
    "fixed_start_cap_weight_raw": -9.783267107904674,
    "end_cap_weight_sd": -0.6552802143918083,
    "end_cap_weight_raw": -9.829203215877122
  },
  "full_period_change": {
    "equal_weight_sd": -1.1727592969806007,
    "equal_weight_raw": -17.59138945470901
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1024739361975875,
    "inflation_mean_sd": 0.4344646164021164
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.18332936507936798,
    "equal_weight_raw": 2.749940476190519,
    "fixed_start_cap_weight_sd": 0.2623946921283173,
    "fixed_start_cap_weight_raw": 3.93592038192476,
    "end_cap_weight_sd": 0.2548867697158476,
    "end_cap_weight_raw": 3.823301545737713
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5390476190476156,
      "change_raw": -8.085714285714234,
      "decay_adjusted_gain_sd": 0.4133333333333368
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6757532042864705,
      "change_raw": -10.136298064297057,
      "decay_adjusted_gain_sd": 0.18554232804233062
    },
    "small": {
      "count": 18,
      "change_sd": -0.8036468293323725,
      "change_raw": -12.054702439985588,
      "decay_adjusted_gain_sd": 0.14388888888889184
    },
    "large_minus_small_sd": 0.26459921028475697,
    "large_minus_small_raw": 3.9689881542713543
  },
  "inflation": {
    "initial_mean_sd": 0.26999999999999996,
    "final_mean_sd": 0.47600000000000003,
    "mean_sd": 0.3788781570913128,
    "mean_absolute_raw_gap": 5.683172356369692,
    "final_absolute_raw_gap": 7.140000000000001,
    "mean_range_fraction": 0.056831723563696916
  },
  "impact": {
    "initial_share": 0.15333333333333332,
    "final_share": 0.18666666666666668,
    "initial_wealth_share": 0.16085288976143292,
    "final_wealth_share": 0.1695679447215569
  },
  "pricing_slope": {
    "mean": -0.000463364690310391,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.05532917742822148,
    "real_improvement_cost": 0.04602591931632249,
    "washing_cost": 0.009303258111898997,
    "fine_transfer": 0.022061535398716796,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07739071282693827,
    "resource_cost_fraction_initial_cap": 0.0018443059142740498,
    "private_net_outflow_fraction_initial_cap": 0.0025796904275646095,
    "fine_transfer_fraction_initial_cap": 0.0007353845132905601,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002565763243270845,
    "unapplied_final_day_resource_cost": 0.0002001010711435391
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 99.4029047244744,
    "beneficial_raw_gain_per_resource_cost": 1491.043570867116,
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
    "accrued_cost": 2.7171335314173275,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.259056944773148,
    "accrued_cost_fraction_initial_cap": 0.09057111771391094,
    "mean_contract_rate": 0.03765608177105498,
    "maximum_ledger_error": 4.2351647362715017e-20
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
    "maximum_relative_cash_error": 1.4726520469860003e-15,
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
      "minimum": -0.2633777913046713,
      "maximum": -0.07057617902520695,
      "mean": -0.18752145465182363,
      "median": -0.20158444657960645,
      "quantile_05": -0.2520734256743707,
      "quantile_95": -0.09886329234739646
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
      "minimum": 0.27839369816932114,
      "maximum": 0.735004005819057,
      "mean": 0.4931364663166786,
      "median": 0.49668554864729425,
      "quantile_05": 0.30278307614627414,
      "quantile_95": 0.6923209104717202
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
        "daily_volatility": 0.018702572577520574,
        "excess_kurtosis": 3.3891212323576205,
        "return_acf_1": -0.21075751235217263,
        "abs_return_acf_1": 0.32460968120040334,
        "abs_return_acf_5": 0.2891524620375439,
        "abs_return_acf_20": 0.23616460870473172,
        "quantile_01": -0.054138731681250996,
        "quantile_99": 0.05181413997587704,
        "hill_tail_index": 4.611722720654662
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020990954018602476,
        "excess_kurtosis": 11.575091830740542,
        "return_acf_1": -0.09328566276436724,
        "abs_return_acf_1": 0.4085718944355875,
        "abs_return_acf_5": 0.41748494697820693,
        "abs_return_acf_20": 0.3417103495758737,
        "quantile_01": -0.06702940195486619,
        "quantile_99": 0.06547252562966968,
        "hill_tail_index": 3.0481336974284376
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.015241787444107643,
        "excess_kurtosis": 3.1426870915440555,
        "return_acf_1": -0.22770008707568337,
        "abs_return_acf_1": 0.23991075804111334,
        "abs_return_acf_5": 0.2057526205598681,
        "abs_return_acf_20": 0.16591028724168266,
        "quantile_01": -0.04029142904384575,
        "quantile_99": 0.03324564638025586,
        "hill_tail_index": 3.7719411330151438
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01676854381930293,
        "excess_kurtosis": 1.9092270047132498,
        "return_acf_1": -0.26080180039143497,
        "abs_return_acf_1": 0.30524287314212817,
        "abs_return_acf_5": 0.18546925642837397,
        "abs_return_acf_20": 0.1804756747002241,
        "quantile_01": -0.043975737502727576,
        "quantile_99": 0.044026733918898914,
        "hill_tail_index": 4.508762259200039
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018098847310415375,
        "excess_kurtosis": 7.151919477321714,
        "return_acf_1": -0.21853802366343947,
        "abs_return_acf_1": 0.37472908543074346,
        "abs_return_acf_5": 0.3430765594174715,
        "abs_return_acf_20": 0.2674455512014234,
        "quantile_01": -0.05738092667073397,
        "quantile_99": 0.05117376315267366,
        "hill_tail_index": 3.208790300251846
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019114467423459826,
        "excess_kurtosis": 3.3882398874705455,
        "return_acf_1": -0.2633777913046713,
        "abs_return_acf_1": 0.35889266593422225,
        "abs_return_acf_5": 0.3320654595217948,
        "abs_return_acf_20": 0.244719163535904,
        "quantile_01": -0.05889983494633898,
        "quantile_99": 0.052706134131086366,
        "hill_tail_index": 4.510057705061207
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01864062538194878,
        "excess_kurtosis": 4.6550960460371185,
        "return_acf_1": -0.19158525584647546,
        "abs_return_acf_1": 0.2710895737117099,
        "abs_return_acf_5": 0.23181484330683721,
        "abs_return_acf_20": 0.23875873989776436,
        "quantile_01": -0.055637951826774085,
        "quantile_99": 0.05113978371721161,
        "hill_tail_index": 3.580601377968591
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01748604424554935,
        "excess_kurtosis": 4.005912608989706,
        "return_acf_1": -0.19898903388956088,
        "abs_return_acf_1": 0.2628630444424567,
        "abs_return_acf_5": 0.18927861607245708,
        "abs_return_acf_20": 0.2814050631734398,
        "quantile_01": -0.05044429965055305,
        "quantile_99": 0.04512912483340228,
        "hill_tail_index": 3.817132639421173
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017889461992474362,
        "excess_kurtosis": 8.506966839439881,
        "return_acf_1": -0.16539610640268085,
        "abs_return_acf_1": 0.26257384477452445,
        "abs_return_acf_5": 0.2995636707456694,
        "abs_return_acf_20": 0.250164308042782,
        "quantile_01": -0.05402532991138245,
        "quantile_99": 0.04907078849866731,
        "hill_tail_index": 2.7658409844040825
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016071951082097323,
        "excess_kurtosis": 2.273066349893739,
        "return_acf_1": -0.21801189491160705,
        "abs_return_acf_1": 0.30204726551172795,
        "abs_return_acf_5": 0.21357166730805846,
        "abs_return_acf_20": 0.176789187667183,
        "quantile_01": -0.043788199081362354,
        "quantile_99": 0.04279272327392303,
        "hill_tail_index": 3.5489663742069957
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017850272915084366,
        "excess_kurtosis": 6.620875105047235,
        "return_acf_1": -0.2162374475864614,
        "abs_return_acf_1": 0.3067595100055048,
        "abs_return_acf_5": 0.23277413192411817,
        "abs_return_acf_20": 0.27085858996507184,
        "quantile_01": -0.05116770524699755,
        "quantile_99": 0.05338613120937321,
        "hill_tail_index": 3.482449149085926
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019151488419835282,
        "excess_kurtosis": 2.7987632370118973,
        "return_acf_1": -0.11579772420353247,
        "abs_return_acf_1": 0.3105899297886884,
        "abs_return_acf_5": 0.29941928554506975,
        "abs_return_acf_20": 0.2561938095717439,
        "quantile_01": -0.053884459627202085,
        "quantile_99": 0.052201740430028586,
        "hill_tail_index": 4.8498474038310135
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019161903768581286,
        "excess_kurtosis": 6.438864158222884,
        "return_acf_1": -0.18726147640644733,
        "abs_return_acf_1": 0.34033737512637163,
        "abs_return_acf_5": 0.32474162895419534,
        "abs_return_acf_20": 0.2988850365959006,
        "quantile_01": -0.05398698467787813,
        "quantile_99": 0.054911158886928574,
        "hill_tail_index": 4.6046203380046755
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017602701675282658,
        "excess_kurtosis": 4.33683047214491,
        "return_acf_1": -0.17887823832154773,
        "abs_return_acf_1": 0.29091599311252225,
        "abs_return_acf_5": 0.2764748488878208,
        "abs_return_acf_20": 0.24413369492920314,
        "quantile_01": -0.05776651452113316,
        "quantile_99": 0.04557876043898425,
        "hill_tail_index": 3.4366260036165857
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017370519773519843,
        "excess_kurtosis": 6.486036398520115,
        "return_acf_1": -0.17164653307625435,
        "abs_return_acf_1": 0.30323039640894683,
        "abs_return_acf_5": 0.24623243380912901,
        "abs_return_acf_20": 0.21180546152853644,
        "quantile_01": -0.04813152755114424,
        "quantile_99": 0.05480618821460014,
        "hill_tail_index": 3.817977218582186
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01836186131546639,
        "excess_kurtosis": 6.3997599318376555,
        "return_acf_1": -0.1601313765032819,
        "abs_return_acf_1": 0.2861646764736551,
        "abs_return_acf_5": 0.2850951545526199,
        "abs_return_acf_20": 0.2788757334329649,
        "quantile_01": -0.05556155807644806,
        "quantile_99": 0.05015047957104834,
        "hill_tail_index": 3.8599752154711386
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019211336436004783,
        "excess_kurtosis": 3.127478534853026,
        "return_acf_1": -0.139927127593278,
        "abs_return_acf_1": 0.26898608311057154,
        "abs_return_acf_5": 0.24349444269897486,
        "abs_return_acf_20": 0.26928147490044024,
        "quantile_01": -0.056341642535545286,
        "quantile_99": 0.05182439478689897,
        "hill_tail_index": 4.3213132282049385
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018111676948258097,
        "excess_kurtosis": 6.614166884775962,
        "return_acf_1": -0.22139380871197972,
        "abs_return_acf_1": 0.3601045511086331,
        "abs_return_acf_5": 0.3008165505395767,
        "abs_return_acf_20": 0.30715743722676586,
        "quantile_01": -0.05915353631466194,
        "quantile_99": 0.056293868956773775,
        "hill_tail_index": 3.463793468343862
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017920344465381197,
        "excess_kurtosis": 4.578359382952373,
        "return_acf_1": -0.20435708760197308,
        "abs_return_acf_1": 0.34390535585878595,
        "abs_return_acf_5": 0.3005674170125886,
        "abs_return_acf_20": 0.22618997272808133,
        "quantile_01": -0.05661940692548806,
        "quantile_99": 0.05348693847512816,
        "hill_tail_index": 4.200268312620199
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01841050485686659,
        "excess_kurtosis": 6.251930943869439,
        "return_acf_1": -0.24140541213129207,
        "abs_return_acf_1": 0.3263415438664014,
        "abs_return_acf_5": 0.30052912871075405,
        "abs_return_acf_20": 0.2866278139137809,
        "quantile_01": -0.0560830692140613,
        "quantile_99": 0.04980302234932879,
        "hill_tail_index": 2.950254302014712
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018477422163927976,
        "excess_kurtosis": 7.276291019581151,
        "return_acf_1": -0.15859032614233776,
        "abs_return_acf_1": 0.2744139176280546,
        "abs_return_acf_5": 0.24674949243433544,
        "abs_return_acf_20": 0.24158628064843868,
        "quantile_01": -0.057118241313560976,
        "quantile_99": 0.0536955094714147,
        "hill_tail_index": 2.800194628145848
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0187186877908537,
        "excess_kurtosis": 5.5036013840874904,
        "return_acf_1": -0.1980418551721767,
        "abs_return_acf_1": 0.3544268723207413,
        "abs_return_acf_5": 0.2296028271761811,
        "abs_return_acf_20": 0.20273222011552128,
        "quantile_01": -0.0638945636394767,
        "quantile_99": 0.05483631693078317,
        "hill_tail_index": 3.73571552636627
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01649975222275782,
        "excess_kurtosis": 2.783414596855377,
        "return_acf_1": -0.21369400668172034,
        "abs_return_acf_1": 0.23586815468991823,
        "abs_return_acf_5": 0.21334386894264357,
        "abs_return_acf_20": 0.13210608034557395,
        "quantile_01": -0.048783915241837235,
        "quantile_99": 0.04509625107935029,
        "hill_tail_index": 4.30353526065035
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01723489255812366,
        "excess_kurtosis": 4.40778416524553,
        "return_acf_1": -0.2055385112911195,
        "abs_return_acf_1": 0.28554426898529117,
        "abs_return_acf_5": 0.17619632707855132,
        "abs_return_acf_20": 0.23340512339670033,
        "quantile_01": -0.051733275749969505,
        "quantile_99": 0.04710233247200334,
        "hill_tail_index": 3.783377895346709
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018359922585656444,
        "excess_kurtosis": 2.9519836140210973,
        "return_acf_1": -0.21605767628580672,
        "abs_return_acf_1": 0.3228356232830114,
        "abs_return_acf_5": 0.26481578014186974,
        "abs_return_acf_20": 0.26424130120591316,
        "quantile_01": -0.05702642312515111,
        "quantile_99": 0.05481505499550854,
        "hill_tail_index": 5.252179794537158
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01780752533247224,
        "excess_kurtosis": 3.877208109829442,
        "return_acf_1": -0.20417985926965201,
        "abs_return_acf_1": 0.4170317847211978,
        "abs_return_acf_5": 0.32899861409876474,
        "abs_return_acf_20": 0.2878153993065542,
        "quantile_01": -0.05275829040559964,
        "quantile_99": 0.04830412697003798,
        "hill_tail_index": 3.980319850896241
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021089353470104544,
        "excess_kurtosis": 9.692364490499493,
        "return_acf_1": -0.10568039517109878,
        "abs_return_acf_1": 0.38940240693303146,
        "abs_return_acf_5": 0.44478952736131766,
        "abs_return_acf_20": 0.3520332528683481,
        "quantile_01": -0.06402021995688452,
        "quantile_99": 0.061307608876840766,
        "hill_tail_index": 2.7182159894641718
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021431471921208277,
        "excess_kurtosis": 10.38189067809141,
        "return_acf_1": -0.218757335064749,
        "abs_return_acf_1": 0.4006684744183772,
        "abs_return_acf_5": 0.3205710759002653,
        "abs_return_acf_20": 0.30557971498001046,
        "quantile_01": -0.06637032596480634,
        "quantile_99": 0.07522162837520331,
        "hill_tail_index": 2.572087677726674
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020458028693578805,
        "excess_kurtosis": 9.43540369200003,
        "return_acf_1": -0.07057617902520695,
        "abs_return_acf_1": 0.45620997700326377,
        "abs_return_acf_5": 0.413390677613448,
        "abs_return_acf_20": 0.33698738197709904,
        "quantile_01": -0.058876635532751985,
        "quantile_99": 0.05725525265669604,
        "hill_tail_index": 2.692606567998189
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021798555830867088,
        "excess_kurtosis": 9.112103174053942,
        "return_acf_1": -0.1490480947126997,
        "abs_return_acf_1": 0.368824011324495,
        "abs_return_acf_5": 0.4339022799763936,
        "abs_return_acf_20": 0.2759660891778656,
        "quantile_01": -0.0761027800159194,
        "quantile_99": 0.07380501676489483,
        "hill_tail_index": 3.8195091682168174
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
