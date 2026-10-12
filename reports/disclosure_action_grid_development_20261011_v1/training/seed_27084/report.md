# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27084
Run ID: `973ba4f0d919ae753d8eff4f4143d2a0ba7134bde21d12bf23a6e4e1c93f2e5e`
Result fingerprint: `922878872f5b345483f41d9ad9a539c2b1b9ce6ccabd191517bc2d91f1fbf16b`

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
    "equal_weight_sd": -0.5893809523809492,
    "equal_weight_raw": -8.840714285714236,
    "fixed_start_cap_weight_sd": -0.6453305885842134,
    "fixed_start_cap_weight_raw": -9.679958828763201,
    "end_cap_weight_sd": -0.6379089121911209,
    "end_cap_weight_raw": -9.568633682866812
  },
  "full_period_change": {
    "equal_weight_sd": -0.9103214285714237,
    "equal_weight_raw": -13.654821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8381577380952336,
    "inflation_mean_sd": 0.7263762312265571
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.35596100664929137,
    "equal_weight_raw": 5.3394150997393695,
    "fixed_start_cap_weight_sd": 0.30308360658037653,
    "fixed_start_cap_weight_raw": 4.5462540987056475,
    "end_cap_weight_sd": 0.311870171899191,
    "end_cap_weight_raw": 4.678052578487865
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.804880952380949,
      "change_raw": -12.073214285714236,
      "decay_adjusted_gain_sd": 0.1475000000000032
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5434920634920604,
      "change_raw": -8.152380952380906,
      "decay_adjusted_gain_sd": 0.40597823915886094
    },
    "small": {
      "count": 18,
      "change_sd": -0.5764087301587268,
      "change_raw": -8.646130952380902,
      "decay_adjusted_gain_sd": 0.36569589150272125
    },
    "large_minus_small_sd": -0.2284722222222222,
    "large_minus_small_raw": -3.427083333333333
  },
  "inflation": {
    "initial_mean_sd": 0.3296666666666666,
    "final_mean_sd": 0.7550885328138589,
    "mean_sd": 0.565752828443399,
    "mean_absolute_raw_gap": 8.486292426650987,
    "final_absolute_raw_gap": 11.326327992207883,
    "mean_range_fraction": 0.08486292426650988
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.23333333333333334,
    "initial_wealth_share": 0.1756960746186884,
    "final_wealth_share": 0.14631558935585484
  },
  "pricing_slope": {
    "mean": -0.001237008853089356,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.6555818436825689,
    "real_improvement_cost": 0.48761383984320616,
    "washing_cost": 0.16796800383936272,
    "fine_transfer": 0.030810714033920487,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.6863925577164893,
    "resource_cost_fraction_initial_cap": 0.021852728122752293,
    "private_net_outflow_fraction_initial_cap": 0.022879751923882974,
    "fine_transfer_fraction_initial_cap": 0.0010270238011306828,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004047826883274775,
    "unapplied_final_day_resource_cost": 0.059340278867949875
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 16.28908778115796,
    "beneficial_raw_gain_per_resource_cost": 244.3363167173694,
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
    "accrued_cost": 2.8396926624934897,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.13649781369698685,
    "accrued_cost_fraction_initial_cap": 0.09465642208311631,
    "mean_contract_rate": 0.03951599245446957,
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
    "maximum_relative_cash_error": 1.6812985090688668e-15,
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
      "minimum": -0.20698768027775669,
      "maximum": -0.01205191469447196,
      "mean": -0.13961867915216386,
      "median": -0.14830775209439323,
      "quantile_05": -0.17337385810427908,
      "quantile_95": -0.07974779396841183
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
      "minimum": 0.25239137886256496,
      "maximum": 0.7758886382285056,
      "mean": 0.4462086283447553,
      "median": 0.4130570417620452,
      "quantile_05": 0.29055899119942874,
      "quantile_95": 0.7142237836304484
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
        "daily_volatility": 0.0189334147709759,
        "excess_kurtosis": 3.7460703484221165,
        "return_acf_1": -0.15511058944549216,
        "abs_return_acf_1": 0.2208107198083145,
        "abs_return_acf_5": 0.24222550129816542,
        "abs_return_acf_20": 0.2234382602634117,
        "quantile_01": -0.062301927706615724,
        "quantile_99": 0.04875654236053836,
        "hill_tail_index": 4.1049521098926665
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018495691808761882,
        "excess_kurtosis": 5.05843769002915,
        "return_acf_1": -0.15698275607092996,
        "abs_return_acf_1": 0.24377109142646625,
        "abs_return_acf_5": 0.24981368918108374,
        "abs_return_acf_20": 0.2506842475941499,
        "quantile_01": -0.05475974865312178,
        "quantile_99": 0.054251075542779394,
        "hill_tail_index": 3.895546716606056
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01831419837486553,
        "excess_kurtosis": 7.2307182553199585,
        "return_acf_1": -0.17383494220862486,
        "abs_return_acf_1": 0.2622858832419221,
        "abs_return_acf_5": 0.2147777691250663,
        "abs_return_acf_20": 0.24978020965518583,
        "quantile_01": -0.05273016401608158,
        "quantile_99": 0.04311848822559387,
        "hill_tail_index": 2.425875666872602
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01943147384068142,
        "excess_kurtosis": 4.749132398746479,
        "return_acf_1": -0.13822600679169614,
        "abs_return_acf_1": 0.19804433020795933,
        "abs_return_acf_5": 0.2578923684078905,
        "abs_return_acf_20": 0.22987300803924013,
        "quantile_01": -0.06421731831063962,
        "quantile_99": 0.055705760346425444,
        "hill_tail_index": 3.645660749059628
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01899356237528077,
        "excess_kurtosis": 5.271599619691019,
        "return_acf_1": -0.16190774469104163,
        "abs_return_acf_1": 0.3153613862488459,
        "abs_return_acf_5": 0.33481458507515455,
        "abs_return_acf_20": 0.27778521044650967,
        "quantile_01": -0.05885287949090407,
        "quantile_99": 0.0602828613389367,
        "hill_tail_index": 3.585407870527743
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019027132377237167,
        "excess_kurtosis": 7.123703711977502,
        "return_acf_1": -0.1437281503508619,
        "abs_return_acf_1": 0.3271687471879401,
        "abs_return_acf_5": 0.27815220900223186,
        "abs_return_acf_20": 0.2257256060034003,
        "quantile_01": -0.05816572914034004,
        "quantile_99": 0.05139746223365116,
        "hill_tail_index": 3.0448250054683337
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01732076239899225,
        "excess_kurtosis": 2.433476974915826,
        "return_acf_1": -0.10624724463442536,
        "abs_return_acf_1": 0.23008567713622535,
        "abs_return_acf_5": 0.24987181911821546,
        "abs_return_acf_20": 0.17736897566994486,
        "quantile_01": -0.05255619886484928,
        "quantile_99": 0.04236657928340756,
        "hill_tail_index": 3.5338920812676586
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01763755074311533,
        "excess_kurtosis": 7.074640753169103,
        "return_acf_1": -0.154693681303299,
        "abs_return_acf_1": 0.369068994748381,
        "abs_return_acf_5": 0.24938860463605347,
        "abs_return_acf_20": 0.2665321429501999,
        "quantile_01": -0.04724100179230936,
        "quantile_99": 0.04913741068132686,
        "hill_tail_index": 3.438931158746318
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01765404560799618,
        "excess_kurtosis": 4.594004750263043,
        "return_acf_1": -0.1241369836742874,
        "abs_return_acf_1": 0.31846382634584913,
        "abs_return_acf_5": 0.280682788749316,
        "abs_return_acf_20": 0.22420431808222527,
        "quantile_01": -0.05032711001810755,
        "quantile_99": 0.05011368583431002,
        "hill_tail_index": 4.07624366877795
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02115797428876296,
        "excess_kurtosis": 8.67561955363189,
        "return_acf_1": -0.14545850939140423,
        "abs_return_acf_1": 0.35691968944379027,
        "abs_return_acf_5": 0.37269442779504797,
        "abs_return_acf_20": 0.30279143387123053,
        "quantile_01": -0.07770126048605566,
        "quantile_99": 0.062266221742512826,
        "hill_tail_index": 3.3542433535951295
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02066475135583688,
        "excess_kurtosis": 8.085647893106358,
        "return_acf_1": -0.16524432333061898,
        "abs_return_acf_1": 0.37568685934974905,
        "abs_return_acf_5": 0.3653869130261632,
        "abs_return_acf_20": 0.28981210170762045,
        "quantile_01": -0.06722779127526493,
        "quantile_99": 0.06524825645753866,
        "hill_tail_index": 3.851007438693624
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019751680599201116,
        "excess_kurtosis": 5.735327400690313,
        "return_acf_1": -0.1421936530055346,
        "abs_return_acf_1": 0.40636859035184136,
        "abs_return_acf_5": 0.28558736116565153,
        "abs_return_acf_20": 0.27063967102561926,
        "quantile_01": -0.06271035100437636,
        "quantile_99": 0.05312863339466874,
        "hill_tail_index": 3.614883826523858
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018153519019083714,
        "excess_kurtosis": 4.9852282338748095,
        "return_acf_1": -0.058066425241673256,
        "abs_return_acf_1": 0.38385600621040644,
        "abs_return_acf_5": 0.37776791643778423,
        "abs_return_acf_20": 0.32336295818784555,
        "quantile_01": -0.060240352446860525,
        "quantile_99": 0.04720728869062772,
        "hill_tail_index": 3.109996362888946
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020296405273300677,
        "excess_kurtosis": 7.717392380210725,
        "return_acf_1": -0.12038468765245507,
        "abs_return_acf_1": 0.29454641486687977,
        "abs_return_acf_5": 0.28535783851249097,
        "abs_return_acf_20": 0.24466035529034708,
        "quantile_01": -0.06775753360265498,
        "quantile_99": 0.058201451546767466,
        "hill_tail_index": 2.9132669233639477
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01882257135627684,
        "excess_kurtosis": 4.612222903158383,
        "return_acf_1": -0.1636971651124661,
        "abs_return_acf_1": 0.3094339905570643,
        "abs_return_acf_5": 0.3282875629938552,
        "abs_return_acf_20": 0.26687456406564236,
        "quantile_01": -0.054451038648226896,
        "quantile_99": 0.057156186385634515,
        "hill_tail_index": 4.136499324302572
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01677265851123812,
        "excess_kurtosis": 11.206199840814337,
        "return_acf_1": -0.11653571286296206,
        "abs_return_acf_1": 0.41166684782721136,
        "abs_return_acf_5": 0.3631937566144256,
        "abs_return_acf_20": 0.3501601052249941,
        "quantile_01": -0.04504085529493305,
        "quantile_99": 0.04797328247499104,
        "hill_tail_index": 2.154307825062597
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019143858502819733,
        "excess_kurtosis": 6.431331713712028,
        "return_acf_1": -0.15772634948509748,
        "abs_return_acf_1": 0.32034836154478435,
        "abs_return_acf_5": 0.3145694074232189,
        "abs_return_acf_20": 0.2901010226128259,
        "quantile_01": -0.06320770577612835,
        "quantile_99": 0.05151290773414998,
        "hill_tail_index": 2.787781570994668
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020553287558666672,
        "excess_kurtosis": 7.81086220620573,
        "return_acf_1": -0.15462155605915726,
        "abs_return_acf_1": 0.41328659227491876,
        "abs_return_acf_5": 0.4265920463817245,
        "abs_return_acf_20": 0.2792371853277846,
        "quantile_01": -0.06548391948665541,
        "quantile_99": 0.05996680574587752,
        "hill_tail_index": 2.865271057611064
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018197030842133838,
        "excess_kurtosis": 5.155666285568104,
        "return_acf_1": -0.1709585646825312,
        "abs_return_acf_1": 0.4011717401813618,
        "abs_return_acf_5": 0.2982441804129199,
        "abs_return_acf_20": 0.25486322062154476,
        "quantile_01": -0.05338808929357754,
        "quantile_99": 0.0483949200135633,
        "hill_tail_index": 3.3581665186674043
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021349348518501007,
        "excess_kurtosis": 16.337270600844423,
        "return_acf_1": -0.20698768027775669,
        "abs_return_acf_1": 0.48961483806162764,
        "abs_return_acf_5": 0.5125890132749457,
        "abs_return_acf_20": 0.3893621733688671,
        "quantile_01": -0.06544113896178301,
        "quantile_99": 0.0634253118408463,
        "hill_tail_index": 2.1340150724009184
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018142658740129224,
        "excess_kurtosis": 4.548873049525866,
        "return_acf_1": -0.15632724721975388,
        "abs_return_acf_1": 0.22354513508966756,
        "abs_return_acf_5": 0.2508376703803907,
        "abs_return_acf_20": 0.173619636920127,
        "quantile_01": -0.05768636001708746,
        "quantile_99": 0.05234195808478333,
        "hill_tail_index": 3.2010865590229973
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020062331423810177,
        "excess_kurtosis": 12.308626061322256,
        "return_acf_1": -0.10992649861976837,
        "abs_return_acf_1": 0.3907392393555865,
        "abs_return_acf_5": 0.3177716458233044,
        "abs_return_acf_20": 0.23302066307287858,
        "quantile_01": -0.055208072738148165,
        "quantile_99": 0.044210070093304805,
        "hill_tail_index": 2.0311338044880176
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017507294674606325,
        "excess_kurtosis": 5.057455440662368,
        "return_acf_1": -0.15115699479738226,
        "abs_return_acf_1": 0.290414785455182,
        "abs_return_acf_5": 0.31488769959571894,
        "abs_return_acf_20": 0.23820460172339544,
        "quantile_01": -0.05354919356643221,
        "quantile_99": 0.042268366072254676,
        "hill_tail_index": 3.37412707805005
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020745014584593442,
        "excess_kurtosis": 10.719794680046343,
        "return_acf_1": -0.17281031086563425,
        "abs_return_acf_1": 0.48411409240253583,
        "abs_return_acf_5": 0.38176683581971793,
        "abs_return_acf_20": 0.2986816249619248,
        "quantile_01": -0.06782267826781557,
        "quantile_99": 0.06020139399500611,
        "hill_tail_index": 2.4546479939783588
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019141505534854004,
        "excess_kurtosis": 7.373859660572599,
        "return_acf_1": -0.12693406407875424,
        "abs_return_acf_1": 0.4252592281742146,
        "abs_return_acf_5": 0.38559120605822333,
        "abs_return_acf_20": 0.3255858866665353,
        "quantile_01": -0.06378758907489614,
        "quantile_99": 0.053427839016101576,
        "hill_tail_index": 3.3797197487896025
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02109818165233909,
        "excess_kurtosis": 10.119659486774196,
        "return_acf_1": -0.11969134963343463,
        "abs_return_acf_1": 0.4128117785160287,
        "abs_return_acf_5": 0.33772853816472403,
        "abs_return_acf_20": 0.33914918062248894,
        "quantile_01": -0.07732758716442766,
        "quantile_99": 0.054165715804742755,
        "hill_tail_index": 2.7872229616255573
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018487358623954328,
        "excess_kurtosis": 5.7202273918346656,
        "return_acf_1": -0.13762402133182317,
        "abs_return_acf_1": 0.3379312567848395,
        "abs_return_acf_5": 0.25675731584485667,
        "abs_return_acf_20": 0.23492076883031893,
        "quantile_01": -0.05735970675519236,
        "quantile_99": 0.05169657728582228,
        "hill_tail_index": 3.926822534680921
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02100717255897402,
        "excess_kurtosis": 8.767171907022295,
        "return_acf_1": -0.1550062285875737,
        "abs_return_acf_1": 0.4334119169496853,
        "abs_return_acf_5": 0.4525906047659817,
        "abs_return_acf_20": 0.3640421367653837,
        "quantile_01": -0.06661446530937257,
        "quantile_99": 0.05975951289443526,
        "hill_tail_index": 2.935110640627499
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019533685027161136,
        "excess_kurtosis": 8.400953017671375,
        "return_acf_1": -0.1302890184640043,
        "abs_return_acf_1": 0.27559561602411925,
        "abs_return_acf_5": 0.2718554804849302,
        "abs_return_acf_20": 0.28003359398441485,
        "quantile_01": -0.05708478373555458,
        "quantile_99": 0.046854262457478375,
        "hill_tail_index": 2.116671591994252
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016507577656930835,
        "excess_kurtosis": 5.410218358704112,
        "return_acf_1": -0.01205191469447196,
        "abs_return_acf_1": 0.2934066380254225,
        "abs_return_acf_5": 0.2282879631163057,
        "abs_return_acf_20": 0.2471388932021562,
        "quantile_01": -0.042533611627361606,
        "quantile_99": 0.04438336183849989,
        "hill_tail_index": 2.6661552332907084
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
