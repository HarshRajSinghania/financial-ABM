# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27104
Run ID: `5f0011749916dd0ef196eb6aaa4d40cdcb53fc5a2b492227ba987eb920c69f34`
Result fingerprint: `0c6c9a28db30923eb49fb646b7b32576706d1b821c3f83c166edb5907269b6a5`

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
    "equal_weight_sd": -0.5722142857142825,
    "equal_weight_raw": -8.583214285714238,
    "fixed_start_cap_weight_sd": -0.6050776201828741,
    "fixed_start_cap_weight_raw": -9.07616430274311,
    "end_cap_weight_sd": -0.6096581835727264,
    "end_cap_weight_raw": -9.144872753590898
  },
  "full_period_change": {
    "equal_weight_sd": -0.8904880952380904,
    "equal_weight_raw": -13.357321428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8439927248677204,
    "inflation_mean_sd": 0.6322569444444445
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.37523097908811825,
    "equal_weight_raw": 5.628464686321775,
    "fixed_start_cap_weight_sd": 0.3420422738941282,
    "fixed_start_cap_weight_raw": 5.130634108411924,
    "end_cap_weight_sd": 0.3382690592660424,
    "end_cap_weight_raw": 5.074035888990637
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6673809523809492,
      "change_raw": -10.010714285714238,
      "decay_adjusted_gain_sd": 0.2850000000000032
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5218253968253935,
      "change_raw": -7.827380952380903,
      "decay_adjusted_gain_sd": 0.41410326362705346
    },
    "small": {
      "count": 18,
      "change_sd": -0.5815476190476159,
      "change_raw": -8.723214285714239,
      "decay_adjusted_gain_sd": 0.37083333333333646
    },
    "large_minus_small_sd": -0.08583333333333332,
    "large_minus_small_raw": -1.2874999999999996
  },
  "inflation": {
    "initial_mean_sd": 0.3176666666666666,
    "final_mean_sd": 0.6605000000000001,
    "mean_sd": 0.5137639467110742,
    "mean_absolute_raw_gap": 7.706459200666113,
    "final_absolute_raw_gap": 9.907500000000002,
    "mean_range_fraction": 0.07706459200666113
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.5066666666666667,
    "initial_wealth_share": 0.20015795375624132,
    "final_wealth_share": 0.534610409734186
  },
  "pricing_slope": {
    "mean": -0.005470326649852671,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.10181609532809528,
    "real_improvement_cost": 0.052913904136554085,
    "washing_cost": 0.04890219119154119,
    "fine_transfer": 0.009728740077442503,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11154483540553778,
    "resource_cost_fraction_initial_cap": 0.0033938698442698436,
    "private_net_outflow_fraction_initial_cap": 0.0037181611801845936,
    "fine_transfer_fraction_initial_cap": 0.0003242913359147502,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.009573468992534062,
    "unapplied_final_day_resource_cost": 0.0003443135059574133
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 110.56139342575332,
    "beneficial_raw_gain_per_resource_cost": 1658.4209013862999,
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
    "accrued_cost": 3.3034493760943944,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.3272588999039183,
    "accrued_cost_fraction_initial_cap": 0.1101149792031465,
    "mean_contract_rate": 0.046276095152793996,
    "maximum_ledger_error": 7.623296525288703e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 2.2712697886148316e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.2519253441931283,
      "maximum": -0.128911822804805,
      "mean": -0.191416410275927,
      "median": -0.1960453883906223,
      "quantile_05": -0.24898126046569022,
      "quantile_95": -0.139370842139657
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
      "minimum": 0.6325991409522764,
      "maximum": 0.8830280834733696,
      "mean": 0.8265250392282563,
      "median": 0.8364618661969528,
      "quantile_05": 0.7111927008873842,
      "quantile_95": 0.8682375214856856
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
        "daily_volatility": 0.02879157466256449,
        "excess_kurtosis": 19.69641679015702,
        "return_acf_1": -0.1515850374023122,
        "abs_return_acf_1": 0.4787860609059034,
        "abs_return_acf_5": 0.4437898053368589,
        "abs_return_acf_20": 0.36121529286291276,
        "quantile_01": -0.11087315421629423,
        "quantile_99": 0.08322072657533039,
        "hill_tail_index": 2.64072864166919
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024626122154070083,
        "excess_kurtosis": 20.892249069546864,
        "return_acf_1": -0.24427151039425873,
        "abs_return_acf_1": 0.5165834274987519,
        "abs_return_acf_5": 0.43955214013644683,
        "abs_return_acf_20": 0.2903422830159763,
        "quantile_01": -0.08254855182301243,
        "quantile_99": 0.07437749969942108,
        "hill_tail_index": 2.353184278890676
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02808260300248381,
        "excess_kurtosis": 17.30012516011825,
        "return_acf_1": -0.18776126816368513,
        "abs_return_acf_1": 0.5656563013262365,
        "abs_return_acf_5": 0.48310536278865346,
        "abs_return_acf_20": 0.41397868638247665,
        "quantile_01": -0.11515752714100101,
        "quantile_99": 0.08868065317642718,
        "hill_tail_index": 2.92114320383777
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02859132247882505,
        "excess_kurtosis": 18.546502880462167,
        "return_acf_1": -0.1531051214765679,
        "abs_return_acf_1": 0.5786439061277074,
        "abs_return_acf_5": 0.45034378125506386,
        "abs_return_acf_20": 0.4075836972375746,
        "quantile_01": -0.10934146371351383,
        "quantile_99": 0.08449823386626187,
        "hill_tail_index": 2.813590160419604
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.025494848932109054,
        "excess_kurtosis": 19.872418348238046,
        "return_acf_1": -0.20466160570125436,
        "abs_return_acf_1": 0.5354949498497549,
        "abs_return_acf_5": 0.44571477652579167,
        "abs_return_acf_20": 0.3585544082458193,
        "quantile_01": -0.09437316542288565,
        "quantile_99": 0.08292579350137859,
        "hill_tail_index": 3.1546508536732003
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.028300272790146245,
        "excess_kurtosis": 24.562840828295478,
        "return_acf_1": -0.24569308578490898,
        "abs_return_acf_1": 0.5752890243204554,
        "abs_return_acf_5": 0.4765859135256551,
        "abs_return_acf_20": 0.3639996457515629,
        "quantile_01": -0.1050357359275717,
        "quantile_99": 0.08529718633354923,
        "hill_tail_index": 2.5997413096331776
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02579536175054003,
        "excess_kurtosis": 17.27571265937876,
        "return_acf_1": -0.2024861062050053,
        "abs_return_acf_1": 0.5012218431709546,
        "abs_return_acf_5": 0.4264213510281847,
        "abs_return_acf_20": 0.41571721019966407,
        "quantile_01": -0.10159304439021109,
        "quantile_99": 0.07476843748654295,
        "hill_tail_index": 2.645996138491905
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02820835205280608,
        "excess_kurtosis": 19.81763905164745,
        "return_acf_1": -0.19863403992462042,
        "abs_return_acf_1": 0.5512087459468337,
        "abs_return_acf_5": 0.4791542039741244,
        "abs_return_acf_20": 0.38213803873350766,
        "quantile_01": -0.10816940312132334,
        "quantile_99": 0.08992877882260782,
        "hill_tail_index": 2.5747404608797875
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.026924975340979613,
        "excess_kurtosis": 16.534481640906364,
        "return_acf_1": -0.18768748644444713,
        "abs_return_acf_1": 0.536593876951459,
        "abs_return_acf_5": 0.4739207072566805,
        "abs_return_acf_20": 0.40330042939403954,
        "quantile_01": -0.10096243597226273,
        "quantile_99": 0.0881022038064082,
        "hill_tail_index": 2.3686168599354924
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02561021246596949,
        "excess_kurtosis": 16.17051533654708,
        "return_acf_1": -0.25137276583961304,
        "abs_return_acf_1": 0.5243311450853562,
        "abs_return_acf_5": 0.5099699027561,
        "abs_return_acf_20": 0.3757511520111796,
        "quantile_01": -0.09196293040918573,
        "quantile_99": 0.07698918118062772,
        "hill_tail_index": 2.9567946790160367
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.024977531069729105,
        "excess_kurtosis": 14.869060897011764,
        "return_acf_1": -0.20023756914135182,
        "abs_return_acf_1": 0.5082814211927202,
        "abs_return_acf_5": 0.46058529375810814,
        "abs_return_acf_20": 0.42562757378249483,
        "quantile_01": -0.08903451807814891,
        "quantile_99": 0.08715686115355857,
        "hill_tail_index": 3.538679660622845
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.027318885277238386,
        "excess_kurtosis": 24.05258156476022,
        "return_acf_1": -0.1514552954949245,
        "abs_return_acf_1": 0.43886911400506984,
        "abs_return_acf_5": 0.43011582329403564,
        "abs_return_acf_20": 0.3621534814468931,
        "quantile_01": -0.09305717884808634,
        "quantile_99": 0.07285975897246509,
        "hill_tail_index": 2.2450972075149083
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02696464117686178,
        "excess_kurtosis": 20.289438004648062,
        "return_acf_1": -0.13824224221517903,
        "abs_return_acf_1": 0.541648202184325,
        "abs_return_acf_5": 0.44958234769283767,
        "abs_return_acf_20": 0.42319397292655336,
        "quantile_01": -0.09006052349223027,
        "quantile_99": 0.0911598550551961,
        "hill_tail_index": 2.489367464950854
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.027763631220726205,
        "excess_kurtosis": 17.43309871563773,
        "return_acf_1": -0.128911822804805,
        "abs_return_acf_1": 0.5253520099392085,
        "abs_return_acf_5": 0.47918977147318675,
        "abs_return_acf_20": 0.4545921707376633,
        "quantile_01": -0.10484516924367755,
        "quantile_99": 0.08337913193151868,
        "hill_tail_index": 2.8414776863466673
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.025649548216444846,
        "excess_kurtosis": 22.256691112354655,
        "return_acf_1": -0.15077542976871375,
        "abs_return_acf_1": 0.48116219052641995,
        "abs_return_acf_5": 0.42300451350865176,
        "abs_return_acf_20": 0.40695569607882454,
        "quantile_01": -0.09494950256354533,
        "quantile_99": 0.07017750696296737,
        "hill_tail_index": 2.4402944612560304
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.026721737296953728,
        "excess_kurtosis": 16.67278265133491,
        "return_acf_1": -0.2519253441931283,
        "abs_return_acf_1": 0.47423248960590914,
        "abs_return_acf_5": 0.43937918170019746,
        "abs_return_acf_20": 0.4337513635737829,
        "quantile_01": -0.10092525555913717,
        "quantile_99": 0.07294505215115309,
        "hill_tail_index": 2.548729525310382
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02659618140661553,
        "excess_kurtosis": 16.56510773728793,
        "return_acf_1": -0.1407502420473523,
        "abs_return_acf_1": 0.5013057150032023,
        "abs_return_acf_5": 0.492786275853549,
        "abs_return_acf_20": 0.43072517011587047,
        "quantile_01": -0.09243327690616555,
        "quantile_99": 0.0787806318135348,
        "hill_tail_index": 2.917154534070528
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.026181620644245736,
        "excess_kurtosis": 19.274901964771512,
        "return_acf_1": -0.18106460441382502,
        "abs_return_acf_1": 0.4814616457932784,
        "abs_return_acf_5": 0.34234113021780216,
        "abs_return_acf_20": 0.4052770494931591,
        "quantile_01": -0.10565964874655903,
        "quantile_99": 0.08447803383980375,
        "hill_tail_index": 2.5961756935961584
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02741706235166138,
        "excess_kurtosis": 20.015225013941684,
        "return_acf_1": -0.1993144387750723,
        "abs_return_acf_1": 0.49529764199444504,
        "abs_return_acf_5": 0.471973107783606,
        "abs_return_acf_20": 0.40320613426817314,
        "quantile_01": -0.09579709382346273,
        "quantile_99": 0.08073563665517905,
        "hill_tail_index": 2.3224839336783365
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.025458378364313635,
        "excess_kurtosis": 18.415082176098775,
        "return_acf_1": -0.22426669702672364,
        "abs_return_acf_1": 0.5042359812551452,
        "abs_return_acf_5": 0.43874738063673396,
        "abs_return_acf_20": 0.3542314364682961,
        "quantile_01": -0.09849275325018313,
        "quantile_99": 0.07056885409126312,
        "hill_tail_index": 2.619258214624959
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02641610061646373,
        "excess_kurtosis": 18.085259452340214,
        "return_acf_1": -0.1549870368022592,
        "abs_return_acf_1": 0.503895794301879,
        "abs_return_acf_5": 0.482255848296758,
        "abs_return_acf_20": 0.36566056266639996,
        "quantile_01": -0.10546869113867235,
        "quantile_99": 0.07153215297993384,
        "hill_tail_index": 2.5224283216478054
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02553475432104063,
        "excess_kurtosis": 16.892381929695397,
        "return_acf_1": -0.2244153283619153,
        "abs_return_acf_1": 0.46267776477685724,
        "abs_return_acf_5": 0.3767464801480404,
        "abs_return_acf_20": 0.4126792157287004,
        "quantile_01": -0.09271899108784701,
        "quantile_99": 0.07916539346404584,
        "hill_tail_index": 2.817268973816002
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02786995572741818,
        "excess_kurtosis": 20.8139490711542,
        "return_acf_1": -0.1445491528175214,
        "abs_return_acf_1": 0.5455144681218036,
        "abs_return_acf_5": 0.4399583874805608,
        "abs_return_acf_20": 0.42804219361419754,
        "quantile_01": -0.11567520797645314,
        "quantile_99": 0.07479995184308601,
        "hill_tail_index": 2.4543345726873325
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02885722260160303,
        "excess_kurtosis": 21.613701682360723,
        "return_acf_1": -0.21868670985618202,
        "abs_return_acf_1": 0.5202827176494552,
        "abs_return_acf_5": 0.5101628163585137,
        "abs_return_acf_20": 0.3932988650167498,
        "quantile_01": -0.11997763076112156,
        "quantile_99": 0.08874868015086933,
        "hill_tail_index": 2.586092827457217
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.025791671912851952,
        "excess_kurtosis": 19.748984009163216,
        "return_acf_1": -0.1934567368566242,
        "abs_return_acf_1": 0.49020475968168414,
        "abs_return_acf_5": 0.42585686365316205,
        "abs_return_acf_20": 0.40497591119032034,
        "quantile_01": -0.09118609991578568,
        "quantile_99": 0.07473438702218183,
        "hill_tail_index": 2.7468083860493393
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02534958801129543,
        "excess_kurtosis": 16.48468310839189,
        "return_acf_1": -0.2460583094531179,
        "abs_return_acf_1": 0.49500987668513785,
        "abs_return_acf_5": 0.4154312320598506,
        "abs_return_acf_20": 0.3977991843795441,
        "quantile_01": -0.09468051319747788,
        "quantile_99": 0.07916033913604846,
        "hill_tail_index": 2.6622951125554266
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025626863171866424,
        "excess_kurtosis": 15.581811278069406,
        "return_acf_1": -0.20432238349447024,
        "abs_return_acf_1": 0.5382874641936445,
        "abs_return_acf_5": 0.4226216382620027,
        "abs_return_acf_20": 0.3979918942288233,
        "quantile_01": -0.09432057078799717,
        "quantile_99": 0.07542873104731135,
        "hill_tail_index": 2.7076360397269963
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02735324274847783,
        "excess_kurtosis": 16.259777559049017,
        "return_acf_1": -0.1904187290303316,
        "abs_return_acf_1": 0.5186906398460602,
        "abs_return_acf_5": 0.47080606235368205,
        "abs_return_acf_20": 0.40694994814175406,
        "quantile_01": -0.10689942914474597,
        "quantile_99": 0.08130007134697669,
        "hill_tail_index": 3.15591374558067
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.027382064676069344,
        "excess_kurtosis": 21.94105517726101,
        "return_acf_1": -0.20173443714879313,
        "abs_return_acf_1": 0.5186933731642343,
        "abs_return_acf_5": 0.44584954493518864,
        "abs_return_acf_20": 0.3591350423593663,
        "quantile_01": -0.10779125273616787,
        "quantile_99": 0.0800185874806249,
        "hill_tail_index": 2.3581788677043583
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.027462441738208585,
        "excess_kurtosis": 15.460229456207731,
        "return_acf_1": -0.16966177123884735,
        "abs_return_acf_1": 0.527254461381563,
        "abs_return_acf_5": 0.45148210931366844,
        "abs_return_acf_20": 0.40473880125749895,
        "quantile_01": -0.10417550458586614,
        "quantile_99": 0.08877989257491962,
        "hill_tail_index": 3.315372774391336
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
