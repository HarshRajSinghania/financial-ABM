# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27043
Run ID: `73e87c08eda6e71a216c6d3760277cc57da80b2045c8ed2da2c53cc3426d2be7`
Result fingerprint: `79fc9e1095c01d9b2bd072975d01eb9147e7cde9518f168fe93ae5215b6919b3`

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
    "equal_weight_sd": -0.5745476190476158,
    "equal_weight_raw": -8.618214285714236,
    "fixed_start_cap_weight_sd": -0.585352541417456,
    "fixed_start_cap_weight_raw": -8.780288121261838,
    "end_cap_weight_sd": -0.5868208929587468,
    "end_cap_weight_raw": -8.802313394381201
  },
  "full_period_change": {
    "equal_weight_sd": -0.8838214285714237,
    "equal_weight_raw": -13.257321428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.865128637566133,
    "inflation_mean_sd": 0.7135618386243386
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.37783333333333663,
    "equal_weight_raw": 5.66750000000005,
    "fixed_start_cap_weight_sd": 0.36702841096349637,
    "fixed_start_cap_weight_raw": 5.505426164452445,
    "end_cap_weight_sd": 0.36556005942220565,
    "end_cap_weight_raw": 5.483400891333084
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5132142857142824,
      "change_raw": -7.698214285714236,
      "decay_adjusted_gain_sd": 0.43916666666667
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6976587301587269,
      "change_raw": -10.464880952380904,
      "decay_adjusted_gain_sd": 0.2547222222222255
    },
    "small": {
      "count": 18,
      "change_sd": -0.5232142857142824,
      "change_raw": -7.848214285714236,
      "decay_adjusted_gain_sd": 0.42916666666667
    },
    "large_minus_small_sd": 0.010000000000000009,
    "large_minus_small_raw": 0.15000000000000013
  },
  "inflation": {
    "initial_mean_sd": 0.25125000000000003,
    "final_mean_sd": 0.749,
    "mean_sd": 0.5126511240632807,
    "mean_absolute_raw_gap": 7.68976686094921,
    "final_absolute_raw_gap": 11.234999999999998,
    "mean_range_fraction": 0.0768976686094921
  },
  "impact": {
    "initial_share": 0.32666666666666666,
    "final_share": 0.36,
    "initial_wealth_share": 0.3327225031727382,
    "final_wealth_share": 0.3799939078745814
  },
  "pricing_slope": {
    "mean": -0.0035559590982974453,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.11552178464964774,
    "real_improvement_cost": 0.08181817961651068,
    "washing_cost": 0.033703605033137074,
    "fine_transfer": 0.021194105704810593,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.13671589035445833,
    "resource_cost_fraction_initial_cap": 0.0038507261549882584,
    "private_net_outflow_fraction_initial_cap": 0.004557196345148611,
    "fine_transfer_fraction_initial_cap": 0.0007064701901603532,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0197067271609505,
    "unapplied_final_day_resource_cost": 0.00040309450995407593
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 98.12002155590541,
    "beneficial_raw_gain_per_resource_cost": 1471.8003233385812,
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
    "accrued_cost": 3.144688332392586,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.16849785620210994,
    "accrued_cost_fraction_initial_cap": 0.1048229444130862,
    "mean_contract_rate": 0.04295817091449466,
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.0737437749900078e-15,
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
      "minimum": -0.21651943157464348,
      "maximum": 0.027344835976868168,
      "mean": -0.12342395153274976,
      "median": -0.12657702950760824,
      "quantile_05": -0.19513351177777408,
      "quantile_95": -0.05889783379855483
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
      "minimum": 0.24407602363847306,
      "maximum": 0.7700776778018588,
      "mean": 0.5136263886414316,
      "median": 0.5027521570005709,
      "quantile_05": 0.3268412396525347,
      "quantile_95": 0.7205442529469146
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
        "daily_volatility": 0.0184848500936438,
        "excess_kurtosis": 5.9411302167696345,
        "return_acf_1": -0.0944734741247605,
        "abs_return_acf_1": 0.3925108899130609,
        "abs_return_acf_5": 0.3217916029163382,
        "abs_return_acf_20": 0.25210846129875336,
        "quantile_01": -0.05419215712890301,
        "quantile_99": 0.051506608589183864,
        "hill_tail_index": 3.2236957624412867
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024995825476717852,
        "excess_kurtosis": 22.273097342399534,
        "return_acf_1": 0.027344835976868168,
        "abs_return_acf_1": 0.47772742919166494,
        "abs_return_acf_5": 0.5378896462699839,
        "abs_return_acf_20": 0.36549745868119965,
        "quantile_01": -0.08401977366325475,
        "quantile_99": 0.07791260700343881,
        "hill_tail_index": 2.379518878184011
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017632963168681594,
        "excess_kurtosis": 2.685445304802232,
        "return_acf_1": -0.10715212634200398,
        "abs_return_acf_1": 0.18185393970871344,
        "abs_return_acf_5": 0.1995367369196821,
        "abs_return_acf_20": 0.22735581828262988,
        "quantile_01": -0.04505683907086182,
        "quantile_99": 0.04244468194630636,
        "hill_tail_index": 3.6586183291040575
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018690389301034456,
        "excess_kurtosis": 10.098565914259117,
        "return_acf_1": -0.15197950798600243,
        "abs_return_acf_1": 0.43794564610435177,
        "abs_return_acf_5": 0.3844927501630667,
        "abs_return_acf_20": 0.3961135876092706,
        "quantile_01": -0.058599600166404746,
        "quantile_99": 0.056460809809418575,
        "hill_tail_index": 3.022887991040815
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02116575271051914,
        "excess_kurtosis": 5.144515079404782,
        "return_acf_1": -0.13432056762462044,
        "abs_return_acf_1": 0.4105062307387635,
        "abs_return_acf_5": 0.4238611336981658,
        "abs_return_acf_20": 0.3516778122113907,
        "quantile_01": -0.06779353450589093,
        "quantile_99": 0.05833324148946388,
        "hill_tail_index": 4.558484360283156
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01983709880327888,
        "excess_kurtosis": 7.468732786285431,
        "return_acf_1": -0.09992657375318485,
        "abs_return_acf_1": 0.3451367334730699,
        "abs_return_acf_5": 0.35064687610234124,
        "abs_return_acf_20": 0.2843959285904493,
        "quantile_01": -0.065819780783889,
        "quantile_99": 0.05335894623312145,
        "hill_tail_index": 3.737863898854837
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01903490215737717,
        "excess_kurtosis": 5.297403459416319,
        "return_acf_1": -0.09207774401984972,
        "abs_return_acf_1": 0.36392287950874896,
        "abs_return_acf_5": 0.3381507386982104,
        "abs_return_acf_20": 0.3433295245440128,
        "quantile_01": -0.057350764623652656,
        "quantile_99": 0.053643291832915684,
        "hill_tail_index": 3.4448790912884157
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018924446875910866,
        "excess_kurtosis": 4.467364831803267,
        "return_acf_1": -0.09523654472152743,
        "abs_return_acf_1": 0.3229813534356097,
        "abs_return_acf_5": 0.26250300126619525,
        "abs_return_acf_20": 0.23103349792962768,
        "quantile_01": -0.05547957482988147,
        "quantile_99": 0.05529673870440654,
        "hill_tail_index": 3.7531631367209872
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02057558217181104,
        "excess_kurtosis": 5.965841916830801,
        "return_acf_1": -0.11075366137494849,
        "abs_return_acf_1": 0.3697968284471409,
        "abs_return_acf_5": 0.35642871801881365,
        "abs_return_acf_20": 0.3599565593981378,
        "quantile_01": -0.0651598164774381,
        "quantile_99": 0.05973947357334382,
        "hill_tail_index": 3.616217977663637
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0204942899869412,
        "excess_kurtosis": 5.933955769699159,
        "return_acf_1": -0.18013292345523446,
        "abs_return_acf_1": 0.4263611188305082,
        "abs_return_acf_5": 0.44083855289429497,
        "abs_return_acf_20": 0.38155676124855414,
        "quantile_01": -0.06816671226388328,
        "quantile_99": 0.05816650730756945,
        "hill_tail_index": 4.234086329730606
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019021352080796743,
        "excess_kurtosis": 4.5376817390612265,
        "return_acf_1": -0.13632773949810392,
        "abs_return_acf_1": 0.34813840984881445,
        "abs_return_acf_5": 0.289173489656314,
        "abs_return_acf_20": 0.312274650344092,
        "quantile_01": -0.05665889949376036,
        "quantile_99": 0.051500340416091424,
        "hill_tail_index": 3.262153416930337
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019491993948321407,
        "excess_kurtosis": 9.072606641876906,
        "return_acf_1": -0.14027931113738532,
        "abs_return_acf_1": 0.4201169304873584,
        "abs_return_acf_5": 0.3505059331498856,
        "abs_return_acf_20": 0.3117978549147444,
        "quantile_01": -0.06755882013154499,
        "quantile_99": 0.05506942628801346,
        "hill_tail_index": 2.8372449885912063
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021750828296645836,
        "excess_kurtosis": 8.42922274095814,
        "return_acf_1": -0.12036831945435623,
        "abs_return_acf_1": 0.395551519021986,
        "abs_return_acf_5": 0.4443843664179989,
        "abs_return_acf_20": 0.3278926895664087,
        "quantile_01": -0.06902402619574294,
        "quantile_99": 0.06320820096577781,
        "hill_tail_index": 3.3152906943219222
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02079046788545616,
        "excess_kurtosis": 6.870404463371058,
        "return_acf_1": -0.15714947900549922,
        "abs_return_acf_1": 0.39113879003434304,
        "abs_return_acf_5": 0.38539015178880676,
        "abs_return_acf_20": 0.29074506623507845,
        "quantile_01": -0.06312968586542013,
        "quantile_99": 0.06412769853139956,
        "hill_tail_index": 4.084696001821338
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017993577418089372,
        "excess_kurtosis": 3.870717860876236,
        "return_acf_1": -0.17279080668968333,
        "abs_return_acf_1": 0.28925275961409763,
        "abs_return_acf_5": 0.2786160395409313,
        "abs_return_acf_20": 0.27032759022661845,
        "quantile_01": -0.05661002863099637,
        "quantile_99": 0.048935788769327956,
        "hill_tail_index": 3.906676965280824
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016898958122145185,
        "excess_kurtosis": 5.568674234888563,
        "return_acf_1": -0.11364476206919892,
        "abs_return_acf_1": 0.251692625646955,
        "abs_return_acf_5": 0.2854437240694945,
        "abs_return_acf_20": 0.2505847085597544,
        "quantile_01": -0.0450835657303356,
        "quantile_99": 0.04599071383558785,
        "hill_tail_index": 3.829245078720177
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022350121839759575,
        "excess_kurtosis": 26.80113536060465,
        "return_acf_1": -0.06861200647704184,
        "abs_return_acf_1": 0.3414535429717792,
        "abs_return_acf_5": 0.4399682784679341,
        "abs_return_acf_20": 0.22199143884489653,
        "quantile_01": -0.06511822744699292,
        "quantile_99": 0.056225864955442406,
        "hill_tail_index": 2.1497471542421343
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019202714674078154,
        "excess_kurtosis": 7.147435670745711,
        "return_acf_1": -0.08225056967369375,
        "abs_return_acf_1": 0.36475949587449985,
        "abs_return_acf_5": 0.35588641867126486,
        "abs_return_acf_20": 0.2945607026681543,
        "quantile_01": -0.05970300567650793,
        "quantile_99": 0.04642212637101868,
        "hill_tail_index": 2.619206350966434
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01871406971855245,
        "excess_kurtosis": 13.639479639990043,
        "return_acf_1": -0.20477412885315247,
        "abs_return_acf_1": 0.4446555000613424,
        "abs_return_acf_5": 0.41250221124498293,
        "abs_return_acf_20": 0.39253697216089367,
        "quantile_01": -0.057369119409023256,
        "quantile_99": 0.04570728800241023,
        "hill_tail_index": 1.8643096675184962
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020025784163941164,
        "excess_kurtosis": 14.589064890353825,
        "return_acf_1": -0.1626763597085215,
        "abs_return_acf_1": 0.33301725599054194,
        "abs_return_acf_5": 0.3386281952712694,
        "abs_return_acf_20": 0.2780233800322265,
        "quantile_01": -0.057837117011411684,
        "quantile_99": 0.05398998265333194,
        "hill_tail_index": 2.4167275190057445
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02037466187977199,
        "excess_kurtosis": 5.728081982281731,
        "return_acf_1": -0.11534187745625601,
        "abs_return_acf_1": 0.43349907102725166,
        "abs_return_acf_5": 0.3640886024857694,
        "abs_return_acf_20": 0.40343911109810127,
        "quantile_01": -0.0622465513769798,
        "quantile_99": 0.05934081315261246,
        "hill_tail_index": 3.311135568950911
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018197913545728774,
        "excess_kurtosis": 9.852184696711245,
        "return_acf_1": -0.05426934605331713,
        "abs_return_acf_1": 0.4634397744113972,
        "abs_return_acf_5": 0.4019005122590832,
        "abs_return_acf_20": 0.39159214580282736,
        "quantile_01": -0.06164059396089489,
        "quantile_99": 0.0504798513116758,
        "hill_tail_index": 2.3269908233919168
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017396835654921623,
        "excess_kurtosis": 8.466764129591299,
        "return_acf_1": -0.06455487437606751,
        "abs_return_acf_1": 0.41217341673429725,
        "abs_return_acf_5": 0.37299204018958904,
        "abs_return_acf_20": 0.3421501628852502,
        "quantile_01": -0.04731411746732406,
        "quantile_99": 0.042493497638159294,
        "hill_tail_index": 2.3952882481056648
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018524577862060684,
        "excess_kurtosis": 3.042351961997653,
        "return_acf_1": -0.21651943157464348,
        "abs_return_acf_1": 0.2913650758416358,
        "abs_return_acf_5": 0.30033227603132173,
        "abs_return_acf_20": 0.2896604494518912,
        "quantile_01": -0.05638127499755941,
        "quantile_99": 0.0498489598400929,
        "hill_tail_index": 4.12186811507048
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01773701019401046,
        "excess_kurtosis": 2.332514715313814,
        "return_acf_1": -0.13711503341331238,
        "abs_return_acf_1": 0.21945908378509463,
        "abs_return_acf_5": 0.22236004813874805,
        "abs_return_acf_20": 0.2338991506294647,
        "quantile_01": -0.05039121585442847,
        "quantile_99": 0.044989644799493814,
        "hill_tail_index": 4.162892207579438
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019710136685626975,
        "excess_kurtosis": 6.272660419686417,
        "return_acf_1": -0.13956381378349358,
        "abs_return_acf_1": 0.32064685568901263,
        "abs_return_acf_5": 0.31472446917722124,
        "abs_return_acf_20": 0.2870142741582195,
        "quantile_01": -0.05698368660555197,
        "quantile_99": 0.058527730195609154,
        "hill_tail_index": 3.6413031782167624
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022130416778094512,
        "excess_kurtosis": 9.773568965202134,
        "return_acf_1": -0.11554206684561297,
        "abs_return_acf_1": 0.46020807215027904,
        "abs_return_acf_5": 0.3970646342806435,
        "abs_return_acf_20": 0.3062933614675352,
        "quantile_01": -0.07749307286506842,
        "quantile_99": 0.06408770859643059,
        "hill_tail_index": 2.5997678638439123
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01834661472174599,
        "excess_kurtosis": 2.7488999400685534,
        "return_acf_1": -0.13278573956086023,
        "abs_return_acf_1": 0.27337007853782586,
        "abs_return_acf_5": 0.23341989083883516,
        "abs_return_acf_20": 0.21207740024192057,
        "quantile_01": -0.05900768141738529,
        "quantile_99": 0.05164641512220721,
        "hill_tail_index": 5.148542294556159
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020500318236633373,
        "excess_kurtosis": 16.468994478785,
        "return_acf_1": -0.1833505353523116,
        "abs_return_acf_1": 0.36872612050762993,
        "abs_return_acf_5": 0.3807869989191453,
        "abs_return_acf_20": 0.3057319857540785,
        "quantile_01": -0.06063536190948157,
        "quantile_99": 0.05554195152728127,
        "hill_tail_index": 3.2285799477660175
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01879326218476105,
        "excess_kurtosis": 5.816007335280654,
        "return_acf_1": -0.14609405757471775,
        "abs_return_acf_1": 0.36642034106490123,
        "abs_return_acf_5": 0.3791117243165234,
        "abs_return_acf_20": 0.31261208239129246,
        "quantile_01": -0.05757104714535179,
        "quantile_99": 0.05577223600348898,
        "hill_tail_index": 4.040403503512442
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
