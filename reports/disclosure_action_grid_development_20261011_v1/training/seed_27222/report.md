# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27222
Run ID: `b67b1186c6a5f3437cf2c10b5118f7743c1a209d348976491c319d09d449aad3`
Result fingerprint: `6bae073e6d79f2943ab4e2f4a156e55825871f0f89d94a95332f7b97c75bde72`

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
    "equal_weight_sd": -0.670547619047616,
    "equal_weight_raw": -10.058214285714238,
    "fixed_start_cap_weight_sd": -0.6653653145179727,
    "fixed_start_cap_weight_raw": -9.980479717769589,
    "end_cap_weight_sd": -0.6605944273522946,
    "end_cap_weight_raw": -9.90891641028442
  },
  "full_period_change": {
    "equal_weight_sd": -1.0728214285714237,
    "equal_weight_raw": -16.092321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.012465608465604,
    "inflation_mean_sd": 0.5446011904761905
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2818333333333365,
    "equal_weight_raw": 4.227500000000047,
    "fixed_start_cap_weight_sd": 0.28701563786297973,
    "fixed_start_cap_weight_raw": 4.305234567944696,
    "end_cap_weight_sd": 0.2917865250286576,
    "end_cap_weight_raw": 4.376797875429863
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6265476190476158,
      "change_raw": -9.398214285714237,
      "decay_adjusted_gain_sd": 0.3258333333333366
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6823809523809492,
      "change_raw": -10.235714285714238,
      "decay_adjusted_gain_sd": 0.2700000000000031
    },
    "small": {
      "count": 18,
      "change_sd": -0.6719642857142827,
      "change_raw": -10.07946428571424,
      "decay_adjusted_gain_sd": 0.28041666666666976
    },
    "large_minus_small_sd": 0.04541666666666688,
    "large_minus_small_raw": 0.6812500000000032
  },
  "inflation": {
    "initial_mean_sd": 0.31416666666666665,
    "final_mean_sd": 0.5900833333333334,
    "mean_sd": 0.44230648071051903,
    "mean_absolute_raw_gap": 6.634597210657786,
    "final_absolute_raw_gap": 8.851249999999999,
    "mean_range_fraction": 0.06634597210657786
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.23369390159477618,
    "final_wealth_share": 0.3267721606579278
  },
  "pricing_slope": {
    "mean": -0.0015715137840064323,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.035783190545075894,
    "real_improvement_cost": 0.02922413658336711,
    "washing_cost": 0.006559053961708783,
    "fine_transfer": 0.00518690824969131,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.04097009879476721,
    "resource_cost_fraction_initial_cap": 0.0011927730181691962,
    "private_net_outflow_fraction_initial_cap": 0.0013656699598255733,
    "fine_transfer_fraction_initial_cap": 0.00017289694165637694,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0002664755304123838,
    "unapplied_final_day_resource_cost": 0.00040833041053827773
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 236.2841286986239,
    "beneficial_raw_gain_per_resource_cost": 3544.2619304793584,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 3.3171845882024846,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.34099411201200747,
    "accrued_cost_fraction_initial_cap": 0.11057281960674946,
    "mean_contract_rate": 0.04571450879957233,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "maximum_relative_cash_error": 1.0385571915034296e-15,
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
      "minimum": -0.1863727810457844,
      "maximum": -0.04767544767606725,
      "mean": -0.1246900442992885,
      "median": -0.1264012389220338,
      "quantile_05": -0.155347144741443,
      "quantile_95": -0.0889984905966986
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
      "minimum": 0.35762306232451285,
      "maximum": 0.7870586449203536,
      "mean": 0.5909103619621882,
      "median": 0.6066604661077343,
      "quantile_05": 0.4071515875829858,
      "quantile_95": 0.7537704524281641
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
        "daily_volatility": 0.019889868417248,
        "excess_kurtosis": 6.770690194948173,
        "return_acf_1": -0.11518028800893927,
        "abs_return_acf_1": 0.3965667985207715,
        "abs_return_acf_5": 0.26758084702359625,
        "abs_return_acf_20": 0.22795882680599802,
        "quantile_01": -0.05981458757911551,
        "quantile_99": 0.0543261905544398,
        "hill_tail_index": 3.875990672044184
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02002226000056316,
        "excess_kurtosis": 4.289616960451182,
        "return_acf_1": -0.10688028892240771,
        "abs_return_acf_1": 0.2511883881506189,
        "abs_return_acf_5": 0.3244124671182231,
        "abs_return_acf_20": 0.22898564586671658,
        "quantile_01": -0.06452517459142094,
        "quantile_99": 0.05452163846296409,
        "hill_tail_index": 3.5920437411939337
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02010793838304594,
        "excess_kurtosis": 7.1468400611682625,
        "return_acf_1": -0.08948822022665881,
        "abs_return_acf_1": 0.2651575911862104,
        "abs_return_acf_5": 0.3541978826652813,
        "abs_return_acf_20": 0.2052081513171232,
        "quantile_01": -0.059926676597719095,
        "quantile_99": 0.05172793959640648,
        "hill_tail_index": 3.066226814789124
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019478344249769172,
        "excess_kurtosis": 5.112939691207112,
        "return_acf_1": -0.15694807464341148,
        "abs_return_acf_1": 0.2581670621481127,
        "abs_return_acf_5": 0.3247693015748435,
        "abs_return_acf_20": 0.22809976288073866,
        "quantile_01": -0.058368638415861505,
        "quantile_99": 0.05056869574471403,
        "hill_tail_index": 3.1541152125082683
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020772293279944433,
        "excess_kurtosis": 4.32265773713552,
        "return_acf_1": -0.08859780271764024,
        "abs_return_acf_1": 0.3001135035141834,
        "abs_return_acf_5": 0.2606843584584849,
        "abs_return_acf_20": 0.2244005004927019,
        "quantile_01": -0.0601999533899139,
        "quantile_99": 0.047503407584113026,
        "hill_tail_index": 3.8919600149165356
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019475051995505137,
        "excess_kurtosis": 5.093721144440025,
        "return_acf_1": -0.13059291500138645,
        "abs_return_acf_1": 0.2612102509752486,
        "abs_return_acf_5": 0.2710818595600564,
        "abs_return_acf_20": 0.23731819928562115,
        "quantile_01": -0.05568029133094717,
        "quantile_99": 0.04602984112701777,
        "hill_tail_index": 3.1245867146230926
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02085135652053546,
        "excess_kurtosis": 3.8815194331490694,
        "return_acf_1": -0.09678781484598092,
        "abs_return_acf_1": 0.32450654924949157,
        "abs_return_acf_5": 0.3408080907232336,
        "abs_return_acf_20": 0.2718649619995935,
        "quantile_01": -0.06423201977134567,
        "quantile_99": 0.05479133086110062,
        "hill_tail_index": 3.9613549212444794
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020772342205919336,
        "excess_kurtosis": 8.78851212506438,
        "return_acf_1": -0.14481137712165762,
        "abs_return_acf_1": 0.370465094353025,
        "abs_return_acf_5": 0.3659605727830451,
        "abs_return_acf_20": 0.3412722636205863,
        "quantile_01": -0.06797476764345695,
        "quantile_99": 0.05593862007989284,
        "hill_tail_index": 2.9889877258474638
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01809392672426783,
        "excess_kurtosis": 9.968898622901296,
        "return_acf_1": -0.12404665768129056,
        "abs_return_acf_1": 0.34422762048593675,
        "abs_return_acf_5": 0.30282570034758394,
        "abs_return_acf_20": 0.24219317488721542,
        "quantile_01": -0.050331162189088195,
        "quantile_99": 0.04753188420866186,
        "hill_tail_index": 3.151450968881105
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020867775346046995,
        "excess_kurtosis": 20.735191627799168,
        "return_acf_1": -0.12621578474621764,
        "abs_return_acf_1": 0.44002352596438965,
        "abs_return_acf_5": 0.412118402177926,
        "abs_return_acf_20": 0.3309670287210922,
        "quantile_01": -0.06223080163538898,
        "quantile_99": 0.048018464701831125,
        "hill_tail_index": 2.1779112526740323
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018658037091728575,
        "excess_kurtosis": 8.068787771451928,
        "return_acf_1": -0.11622245479616716,
        "abs_return_acf_1": 0.40398212929775795,
        "abs_return_acf_5": 0.3450770451311684,
        "abs_return_acf_20": 0.31220718304413136,
        "quantile_01": -0.07030110770877075,
        "quantile_99": 0.04853113529093264,
        "hill_tail_index": 2.483347899492384
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021844686888991726,
        "excess_kurtosis": 6.346491096778209,
        "return_acf_1": -0.04767544767606725,
        "abs_return_acf_1": 0.29609019275677084,
        "abs_return_acf_5": 0.40285828901797927,
        "abs_return_acf_20": 0.3003684993903582,
        "quantile_01": -0.06706056925416891,
        "quantile_99": 0.06607256912043141,
        "hill_tail_index": 3.571139451219127
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02117643592219726,
        "excess_kurtosis": 6.3229723448325625,
        "return_acf_1": -0.1249344366261831,
        "abs_return_acf_1": 0.32366194299290346,
        "abs_return_acf_5": 0.31642676973196837,
        "abs_return_acf_20": 0.23833349700692724,
        "quantile_01": -0.0686569097234763,
        "quantile_99": 0.05819152634865323,
        "hill_tail_index": 3.647852598087822
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019295042810685073,
        "excess_kurtosis": 14.277028576839069,
        "return_acf_1": -0.1436504035291589,
        "abs_return_acf_1": 0.41753851226941435,
        "abs_return_acf_5": 0.39542727258056287,
        "abs_return_acf_20": 0.33399835163930713,
        "quantile_01": -0.06811843489828553,
        "quantile_99": 0.04900250480897259,
        "hill_tail_index": 2.717702364575117
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019324343696288215,
        "excess_kurtosis": 14.283062345025758,
        "return_acf_1": -0.12935277133156656,
        "abs_return_acf_1": 0.39650129605520174,
        "abs_return_acf_5": 0.2921186841995062,
        "abs_return_acf_20": 0.3170027120134247,
        "quantile_01": -0.05379119628886127,
        "quantile_99": 0.05116012422496462,
        "hill_tail_index": 3.328479232180662
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019956513756256827,
        "excess_kurtosis": 3.725348362687952,
        "return_acf_1": -0.15339045263903708,
        "abs_return_acf_1": 0.2773093458116403,
        "abs_return_acf_5": 0.28752310663821035,
        "abs_return_acf_20": 0.23510244555541146,
        "quantile_01": -0.05713630737748654,
        "quantile_99": 0.055960567083955345,
        "hill_tail_index": 4.200606670567304
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02009209824991705,
        "excess_kurtosis": 12.07727271171321,
        "return_acf_1": -0.1863727810457844,
        "abs_return_acf_1": 0.4179769686408468,
        "abs_return_acf_5": 0.3325603788534011,
        "abs_return_acf_20": 0.27268754462957223,
        "quantile_01": -0.0580660228991066,
        "quantile_99": 0.05236587323795829,
        "hill_tail_index": 2.767309212131038
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021064375085419536,
        "excess_kurtosis": 7.473706242994172,
        "return_acf_1": -0.12658669309784998,
        "abs_return_acf_1": 0.3890632913298468,
        "abs_return_acf_5": 0.37805434605081617,
        "abs_return_acf_20": 0.3008835510232966,
        "quantile_01": -0.07447345160682958,
        "quantile_99": 0.05925725965644533,
        "hill_tail_index": 2.9711971679446316
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020562653002752146,
        "excess_kurtosis": 5.290558733866659,
        "return_acf_1": -0.1218380445124324,
        "abs_return_acf_1": 0.30173181243329616,
        "abs_return_acf_5": 0.36488283521030107,
        "abs_return_acf_20": 0.26531884293155333,
        "quantile_01": -0.06928890516379856,
        "quantile_99": 0.057604196942585166,
        "hill_tail_index": 3.8055220506369047
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019309046815306777,
        "excess_kurtosis": 3.25944573714066,
        "return_acf_1": -0.12130719474919102,
        "abs_return_acf_1": 0.28417932226679343,
        "abs_return_acf_5": 0.33139654143079034,
        "abs_return_acf_20": 0.19923479437852132,
        "quantile_01": -0.060653481068655014,
        "quantile_99": 0.0541269880202147,
        "hill_tail_index": 5.362763264987897
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019642550093984926,
        "excess_kurtosis": 5.265606977688677,
        "return_acf_1": -0.12785542288652677,
        "abs_return_acf_1": 0.28923230769306496,
        "abs_return_acf_5": 0.2819274767772007,
        "abs_return_acf_20": 0.19387831176476492,
        "quantile_01": -0.05884685453907201,
        "quantile_99": 0.04733752103840234,
        "hill_tail_index": 3.6186758002402026
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02072830234803861,
        "excess_kurtosis": 4.56402831024459,
        "return_acf_1": -0.13382184796607605,
        "abs_return_acf_1": 0.2956905522915345,
        "abs_return_acf_5": 0.3384098670997316,
        "abs_return_acf_20": 0.28689124305030406,
        "quantile_01": -0.06472049202181479,
        "quantile_99": 0.060960030147461805,
        "hill_tail_index": 4.647173797248601
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01934993477634111,
        "excess_kurtosis": 11.591222020989905,
        "return_acf_1": -0.11272085138220936,
        "abs_return_acf_1": 0.4476696365575836,
        "abs_return_acf_5": 0.38232753053675456,
        "abs_return_acf_20": 0.27919938160861907,
        "quantile_01": -0.0606780184212333,
        "quantile_99": 0.04992377140538857,
        "hill_tail_index": 2.922358968922164
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019875213230520123,
        "excess_kurtosis": 20.307306019094895,
        "return_acf_1": -0.12396704551328855,
        "abs_return_acf_1": 0.5344328041073014,
        "abs_return_acf_5": 0.36677141454283807,
        "abs_return_acf_20": 0.2726696705636278,
        "quantile_01": -0.057377275665748705,
        "quantile_99": 0.050935240967160324,
        "hill_tail_index": 2.430908659399175
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020159399810110886,
        "excess_kurtosis": 4.452765771343181,
        "return_acf_1": -0.12795012648853082,
        "abs_return_acf_1": 0.34049388407391884,
        "abs_return_acf_5": 0.29820045815499024,
        "abs_return_acf_20": 0.2465719645486035,
        "quantile_01": -0.0668529945683403,
        "quantile_99": 0.05564532585491894,
        "hill_tail_index": 3.95755361175046
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019546633919498502,
        "excess_kurtosis": 3.84522350866916,
        "return_acf_1": -0.13743032681224526,
        "abs_return_acf_1": 0.30864748413735654,
        "abs_return_acf_5": 0.34836210280198926,
        "abs_return_acf_20": 0.2664042940570318,
        "quantile_01": -0.05808983884732204,
        "quantile_99": 0.05830949417166941,
        "hill_tail_index": 4.754945247290752
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020322756693934015,
        "excess_kurtosis": 12.320999599093248,
        "return_acf_1": -0.1284915602859237,
        "abs_return_acf_1": 0.47052870042664313,
        "abs_return_acf_5": 0.3992274916830131,
        "abs_return_acf_20": 0.3597551101202679,
        "quantile_01": -0.07521938874841441,
        "quantile_99": 0.06178060470902176,
        "hill_tail_index": 2.3671838536141183
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01980673974033713,
        "excess_kurtosis": 12.603369611196415,
        "return_acf_1": -0.13779851963791723,
        "abs_return_acf_1": 0.4012627603117967,
        "abs_return_acf_5": 0.31480850548170364,
        "abs_return_acf_20": 0.26485368178685903,
        "quantile_01": -0.05266702809339933,
        "quantile_99": 0.053658650199906524,
        "hill_tail_index": 2.6768208687002946
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01984436932604632,
        "excess_kurtosis": 11.123943964035728,
        "return_acf_1": -0.11835160097636757,
        "abs_return_acf_1": 0.3866787769717293,
        "abs_return_acf_5": 0.4348578559449394,
        "abs_return_acf_20": 0.37478286010250894,
        "quantile_01": -0.07120652307540486,
        "quantile_99": 0.05227697570439968,
        "hill_tail_index": 2.337825887149014
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019456840566340505,
        "excess_kurtosis": 4.737756711743969,
        "return_acf_1": -0.14143412311054082,
        "abs_return_acf_1": 0.2562224307173591,
        "abs_return_acf_5": 0.31853779331466736,
        "abs_return_acf_20": 0.2290194157530115,
        "quantile_01": -0.05689092769993585,
        "quantile_99": 0.05763223593397285,
        "hill_tail_index": 3.43136336202281
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
