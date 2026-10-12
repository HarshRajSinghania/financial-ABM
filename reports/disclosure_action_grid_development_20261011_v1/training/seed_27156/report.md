# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27156
Run ID: `53035fe04c49d033186e77f93ed56a7f9169603969790c070253cfd023918dc5`
Result fingerprint: `a744f315a7392617121bccc2bbb2228ed439712267f29f8511b950e547290ae1`

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
    "equal_weight_sd": -0.6509642857142826,
    "equal_weight_raw": -9.764464285714235,
    "fixed_start_cap_weight_sd": -0.6969488401328443,
    "fixed_start_cap_weight_raw": -10.454232601992665,
    "end_cap_weight_sd": -0.6735792352972929,
    "end_cap_weight_raw": -10.103688529459395
  },
  "full_period_change": {
    "equal_weight_sd": -1.020404761904757,
    "equal_weight_raw": -15.306071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9692490079365035,
    "inflation_mean_sd": 0.555699074074074
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.30141666666666983,
    "equal_weight_raw": 4.521250000000047,
    "fixed_start_cap_weight_sd": 0.25543211224810797,
    "fixed_start_cap_weight_raw": 3.831481683721619,
    "end_cap_weight_sd": 0.27880171708365936,
    "end_cap_weight_raw": 4.182025756254891
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7615476190476159,
      "change_raw": -11.42321428571424,
      "decay_adjusted_gain_sd": 0.19083333333333638
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6418253968253935,
      "change_raw": -9.627380952380904,
      "decay_adjusted_gain_sd": 0.31055555555555875
    },
    "small": {
      "count": 18,
      "change_sd": -0.6371031746031713,
      "change_raw": -9.55654761904757,
      "decay_adjusted_gain_sd": 0.315277777777781
    },
    "large_minus_small_sd": -0.12444444444444458,
    "large_minus_small_raw": -1.8666666666666687
  },
  "inflation": {
    "initial_mean_sd": 0.29041666666666666,
    "final_mean_sd": 0.5802500000000002,
    "mean_sd": 0.43853615043019706,
    "mean_absolute_raw_gap": 6.578042256452956,
    "final_absolute_raw_gap": 8.703750000000003,
    "mean_range_fraction": 0.06578042256452955
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.19333333333333333,
    "initial_wealth_share": 0.152445693542504,
    "final_wealth_share": 0.16444099253143854
  },
  "pricing_slope": {
    "mean": 0.0001945089471240827,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.12279362919390763,
    "real_improvement_cost": 0.10484342016442078,
    "washing_cost": 0.017950209029486856,
    "fine_transfer": 0.0023886706902917004,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12518229988419932,
    "resource_cost_fraction_initial_cap": 0.004093120973130254,
    "private_net_outflow_fraction_initial_cap": 0.004172743329473311,
    "fine_transfer_fraction_initial_cap": 7.962235634305668e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001005367543438619,
    "unapplied_final_day_resource_cost": 0.000153760394576462
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 73.63981388416147,
    "beneficial_raw_gain_per_resource_cost": 1104.597208262422,
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
    "accrued_cost": 2.9788196206604747,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.002629144469998141,
    "accrued_cost_fraction_initial_cap": 0.09929398735534915,
    "mean_contract_rate": 0.04018289800394253,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "price_cap_hits": 4,
    "maximum_relative_cash_error": 1.838105500508272e-15,
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
      "minimum": -0.21506760501682098,
      "maximum": -0.0037496580438467313,
      "mean": -0.1255250223140504,
      "median": -0.13350315876983554,
      "quantile_05": -0.2062738590726988,
      "quantile_95": -0.025238398442477574
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
      "minimum": 0.2027477366408254,
      "maximum": 0.7986897229463816,
      "mean": 0.5772456727355235,
      "median": 0.6808491125025024,
      "quantile_05": 0.26144097035886116,
      "quantile_95": 0.7723466417027558
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
        "daily_volatility": 0.018941280499980735,
        "excess_kurtosis": 8.176290062463952,
        "return_acf_1": -0.007278137035267419,
        "abs_return_acf_1": 0.3126392793561086,
        "abs_return_acf_5": 0.3282397510432105,
        "abs_return_acf_20": 0.24016304021692508,
        "quantile_01": -0.062097792307915525,
        "quantile_99": 0.051609602240564566,
        "hill_tail_index": 3.3151336467779693
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02046702269305804,
        "excess_kurtosis": 13.408493884444173,
        "return_acf_1": -0.11324715851300862,
        "abs_return_acf_1": 0.4002175564270757,
        "abs_return_acf_5": 0.4684473584737173,
        "abs_return_acf_20": 0.38773931224551456,
        "quantile_01": -0.0630050622629418,
        "quantile_99": 0.06072849602110709,
        "hill_tail_index": 3.3990788658974207
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019365535564353335,
        "excess_kurtosis": 15.77623851256866,
        "return_acf_1": -0.1536354698051264,
        "abs_return_acf_1": 0.45109678372262396,
        "abs_return_acf_5": 0.3698729163477064,
        "abs_return_acf_20": 0.32707230120915176,
        "quantile_01": -0.0639463528535534,
        "quantile_99": 0.052427550267489874,
        "hill_tail_index": 2.3018117468950465
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021908257187450948,
        "excess_kurtosis": 14.036334440391201,
        "return_acf_1": -0.04718982905128974,
        "abs_return_acf_1": 0.35887832004039594,
        "abs_return_acf_5": 0.3506437783640585,
        "abs_return_acf_20": 0.26966252000566726,
        "quantile_01": -0.06773916731148998,
        "quantile_99": 0.06618417025177857,
        "hill_tail_index": 2.8126503130516665
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02015549848652954,
        "excess_kurtosis": 11.367212993126698,
        "return_acf_1": -0.1284465359001923,
        "abs_return_acf_1": 0.44031703020663593,
        "abs_return_acf_5": 0.4599297124233771,
        "abs_return_acf_20": 0.336271587921094,
        "quantile_01": -0.08234531799664264,
        "quantile_99": 0.04650571558312218,
        "hill_tail_index": 2.015768328334997
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01833323031508284,
        "excess_kurtosis": 11.018206160228674,
        "return_acf_1": -0.13229870442686992,
        "abs_return_acf_1": 0.3972456809718524,
        "abs_return_acf_5": 0.3623292724316319,
        "abs_return_acf_20": 0.3214071012434191,
        "quantile_01": -0.059115168265648235,
        "quantile_99": 0.045491235995136776,
        "hill_tail_index": 2.481189502593316
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019281565695332226,
        "excess_kurtosis": 13.36106132021608,
        "return_acf_1": -0.16182422146348352,
        "abs_return_acf_1": 0.4274192660238662,
        "abs_return_acf_5": 0.36002287831076185,
        "abs_return_acf_20": 0.2840409381629689,
        "quantile_01": -0.0702785861804112,
        "quantile_99": 0.047148442333211575,
        "hill_tail_index": 2.2177750418692384
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019946806670218382,
        "excess_kurtosis": 14.25867999025115,
        "return_acf_1": -0.214653417961168,
        "abs_return_acf_1": 0.5074139695292731,
        "abs_return_acf_5": 0.39230408409972756,
        "abs_return_acf_20": 0.34715221289807613,
        "quantile_01": -0.0643015630472054,
        "quantile_99": 0.05762130161165303,
        "hill_tail_index": 2.9879020603124244
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021017047139304065,
        "excess_kurtosis": 21.243281230302898,
        "return_acf_1": -0.13605577683877712,
        "abs_return_acf_1": 0.446733029009715,
        "abs_return_acf_5": 0.46871086174890725,
        "abs_return_acf_20": 0.3532050249155964,
        "quantile_01": -0.07485956879634578,
        "quantile_99": 0.05232514678500066,
        "hill_tail_index": 1.7327041241565644
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01845017390549899,
        "excess_kurtosis": 4.211828785128147,
        "return_acf_1": -0.10032503723088489,
        "abs_return_acf_1": 0.28559324173163153,
        "abs_return_acf_5": 0.32532589188084804,
        "abs_return_acf_20": 0.24581673149101518,
        "quantile_01": -0.05530012568715478,
        "quantile_99": 0.04782034670762551,
        "hill_tail_index": 4.441612628742287
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01934933193296313,
        "excess_kurtosis": 7.201927488376363,
        "return_acf_1": -0.1506358155918565,
        "abs_return_acf_1": 0.36964626065673145,
        "abs_return_acf_5": 0.3719049531590474,
        "abs_return_acf_20": 0.29761489961375887,
        "quantile_01": -0.07333620007522028,
        "quantile_99": 0.056081347977447016,
        "hill_tail_index": 3.0891474921428994
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020947319995363856,
        "excess_kurtosis": 14.249023712215838,
        "return_acf_1": -0.16422772438489883,
        "abs_return_acf_1": 0.4221219352763416,
        "abs_return_acf_5": 0.3731934907923715,
        "abs_return_acf_20": 0.3342887252818269,
        "quantile_01": -0.06781445209771941,
        "quantile_99": 0.058126265533501496,
        "hill_tail_index": 2.9738486652790335
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019210565428168062,
        "excess_kurtosis": 17.8297350782589,
        "return_acf_1": -0.21506760501682098,
        "abs_return_acf_1": 0.3973164549511383,
        "abs_return_acf_5": 0.3839618476592263,
        "abs_return_acf_20": 0.29673790228755054,
        "quantile_01": -0.060384800761896694,
        "quantile_99": 0.04560101838873636,
        "hill_tail_index": 1.9128433635202882
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01812328343112394,
        "excess_kurtosis": 3.5587125584685833,
        "return_acf_1": -0.055065585173656666,
        "abs_return_acf_1": 0.27003883637996523,
        "abs_return_acf_5": 0.30914975500502545,
        "abs_return_acf_20": 0.2469964828390783,
        "quantile_01": -0.05613834813932794,
        "quantile_99": 0.05627408402807048,
        "hill_tail_index": 4.8546614500544045
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0205313266721648,
        "excess_kurtosis": 20.768280260496233,
        "return_acf_1": -0.13524858147565008,
        "abs_return_acf_1": 0.5103158176045594,
        "abs_return_acf_5": 0.4724664659773117,
        "abs_return_acf_20": 0.43568273491947873,
        "quantile_01": -0.06870377808935033,
        "quantile_99": 0.05693321383851232,
        "hill_tail_index": 2.904468042263615
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018655845651889075,
        "excess_kurtosis": 12.892401156495307,
        "return_acf_1": -0.1347076131128012,
        "abs_return_acf_1": 0.32402983166533583,
        "abs_return_acf_5": 0.29775503454051117,
        "abs_return_acf_20": 0.26981179314986015,
        "quantile_01": -0.06348383227763381,
        "quantile_99": 0.047917070987498006,
        "hill_tail_index": 2.512446302276406
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.016666685443073682,
        "excess_kurtosis": 9.106785039246143,
        "return_acf_1": -0.08079516720083237,
        "abs_return_acf_1": 0.28573092109314197,
        "abs_return_acf_5": 0.2955517694974379,
        "abs_return_acf_20": 0.21001149663767285,
        "quantile_01": -0.05224336025731754,
        "quantile_99": 0.0391663395863995,
        "hill_tail_index": 3.2039835692157848
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01970771811719133,
        "excess_kurtosis": 19.932948359493082,
        "return_acf_1": -0.13486175501927217,
        "abs_return_acf_1": 0.44009851069269457,
        "abs_return_acf_5": 0.39437255241254476,
        "abs_return_acf_20": 0.29424223032225083,
        "quantile_01": -0.06230087756917418,
        "quantile_99": 0.0471738788113079,
        "hill_tail_index": 1.9575623733528276
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01805558228208678,
        "excess_kurtosis": 11.351674390534377,
        "return_acf_1": -0.1538236788579314,
        "abs_return_acf_1": 0.3425757878892901,
        "abs_return_acf_5": 0.3344761209955115,
        "abs_return_acf_20": 0.28144541137493473,
        "quantile_01": -0.05273992133304508,
        "quantile_99": 0.04999862817023917,
        "hill_tail_index": 2.4511724558474475
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01880630206543716,
        "excess_kurtosis": 10.652394576375366,
        "return_acf_1": -0.12773831915239445,
        "abs_return_acf_1": 0.32423496146170866,
        "abs_return_acf_5": 0.31954731300391775,
        "abs_return_acf_20": 0.30282063069934606,
        "quantile_01": -0.059503330599441635,
        "quantile_99": 0.04591072585614063,
        "hill_tail_index": 3.1540148261490857
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01860153620639211,
        "excess_kurtosis": 12.822499520156585,
        "return_acf_1": -0.13041386078660186,
        "abs_return_acf_1": 0.31254106838840096,
        "abs_return_acf_5": 0.4045465980338529,
        "abs_return_acf_20": 0.24890251201788793,
        "quantile_01": -0.05567638071904481,
        "quantile_99": 0.0442530919238456,
        "hill_tail_index": 2.2997247360739004
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02006741840680946,
        "excess_kurtosis": 10.879062521459552,
        "return_acf_1": -0.1841184642147782,
        "abs_return_acf_1": 0.4973320385970744,
        "abs_return_acf_5": 0.4193731311351537,
        "abs_return_acf_20": 0.35853453209626673,
        "quantile_01": -0.071460431812683,
        "quantile_99": 0.05569184782724213,
        "hill_tail_index": 3.037208262063717
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018446328720510267,
        "excess_kurtosis": 6.091192210324866,
        "return_acf_1": -0.07927944544350606,
        "abs_return_acf_1": 0.2620568037611027,
        "abs_return_acf_5": 0.3385166099167958,
        "abs_return_acf_20": 0.2962703017355787,
        "quantile_01": -0.0597315779117297,
        "quantile_99": 0.05711676718086782,
        "hill_tail_index": 3.5737876329598124
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01931842261338921,
        "excess_kurtosis": 4.3163873344765245,
        "return_acf_1": -0.09170059183056851,
        "abs_return_acf_1": 0.35068763973281697,
        "abs_return_acf_5": 0.3320684365807103,
        "abs_return_acf_20": 0.27393203696406093,
        "quantile_01": -0.061478551051109734,
        "quantile_99": 0.05839103798477647,
        "hill_tail_index": 5.47060398014822
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018873032410163908,
        "excess_kurtosis": 17.35921090750087,
        "return_acf_1": -0.1494972741714291,
        "abs_return_acf_1": 0.3652851070594206,
        "abs_return_acf_5": 0.3328524311896376,
        "abs_return_acf_20": 0.33281433783558,
        "quantile_01": -0.06074649670542392,
        "quantile_99": 0.052277498891107894,
        "hill_tail_index": 2.238317991193734
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020101367949479705,
        "excess_kurtosis": 15.155700624145354,
        "return_acf_1": -0.1571615114285108,
        "abs_return_acf_1": 0.4336345393114779,
        "abs_return_acf_5": 0.37874748573332767,
        "abs_return_acf_20": 0.325067756440226,
        "quantile_01": -0.07057273048453126,
        "quantile_99": 0.05936193572972467,
        "hill_tail_index": 2.226830306503264
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018478914883807377,
        "excess_kurtosis": 18.011612903618545,
        "return_acf_1": -0.1317170197148807,
        "abs_return_acf_1": 0.28177278550454454,
        "abs_return_acf_5": 0.3612161507456376,
        "abs_return_acf_20": 0.23357072406506377,
        "quantile_01": -0.05323419985683216,
        "quantile_99": 0.043189435954091505,
        "hill_tail_index": 2.1254765927634867
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019190383977562248,
        "excess_kurtosis": 16.747113459444986,
        "return_acf_1": -0.19603217598679204,
        "abs_return_acf_1": 0.4409735538658911,
        "abs_return_acf_5": 0.3868695353900211,
        "abs_return_acf_20": 0.2909193349167771,
        "quantile_01": -0.06366183878611319,
        "quantile_99": 0.0441503892232526,
        "hill_tail_index": 2.3600750232854013
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018859692447800044,
        "excess_kurtosis": 17.08232841928823,
        "return_acf_1": -0.09495453458841602,
        "abs_return_acf_1": 0.34874672273325935,
        "abs_return_acf_5": 0.37928955688388855,
        "abs_return_acf_20": 0.2826342032757638,
        "quantile_01": -0.06263733375342873,
        "quantile_99": 0.04663649309122872,
        "hill_tail_index": 2.1600530487361937
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019976047688048698,
        "excess_kurtosis": 9.749413511757078,
        "return_acf_1": -0.0037496580438467313,
        "abs_return_acf_1": 0.35834827441446376,
        "abs_return_acf_5": 0.4439138510517898,
        "abs_return_acf_20": 0.285299748689728,
        "quantile_01": -0.057521121797698735,
        "quantile_99": 0.05564494199956344,
        "hill_tail_index": 2.92625554637723
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
