# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720211
Run ID: `7b647a3bb66f3fd741c9632a58a79446ba715f612aeea1c92970109bd999d2ee`
Result fingerprint: `1b6f2e2663420e018dc766a384b2c8900b5eb0071a2b2174f1bab3b3025bb1d1`

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
    "equal_weight_sd": -0.8550515873015843,
    "equal_weight_raw": -12.825773809523765,
    "fixed_start_cap_weight_sd": -0.8421656326939188,
    "fixed_start_cap_weight_raw": -12.63248449040878,
    "end_cap_weight_sd": -0.8450819749915487,
    "end_cap_weight_raw": -12.67622962487323
  },
  "full_period_change": {
    "equal_weight_sd": -1.3079781610058068,
    "equal_weight_raw": -19.619672415087102
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2227357668259131,
    "inflation_mean_sd": 0.22121560846560845
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.06591666666666954,
    "equal_weight_raw": 0.988750000000043,
    "fixed_start_cap_weight_sd": 0.08089950574347389,
    "fixed_start_cap_weight_raw": 1.2134925861521084,
    "end_cap_weight_sd": 0.07560398055922977,
    "end_cap_weight_raw": 1.1340597083884463
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8182142857142826,
      "change_raw": -12.27321428571424,
      "decay_adjusted_gain_sd": 0.1341666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8079497354497327,
      "change_raw": -12.119246031745991,
      "decay_adjusted_gain_sd": 0.03972222222222494
    },
    "small": {
      "count": 18,
      "change_sd": -0.8847420634920604,
      "change_raw": -13.271130952380906,
      "decay_adjusted_gain_sd": 0.06763888888889179
    },
    "large_minus_small_sd": 0.06652777777777785,
    "large_minus_small_raw": 0.9979166666666678
  },
  "inflation": {
    "initial_mean_sd": 0.1495833333333333,
    "final_mean_sd": 0.22274999999999998,
    "mean_sd": 0.19539779350541214,
    "mean_absolute_raw_gap": 2.9309669025811824,
    "final_absolute_raw_gap": 3.34125,
    "mean_range_fraction": 0.029309669025811825
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.3933333333333333,
    "initial_wealth_share": 0.15452125733035374,
    "final_wealth_share": 0.3286662613192479
  },
  "pricing_slope": {
    "mean": -0.0017663584044766852,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.0014221572969339595,
    "real_improvement_cost": 0.0006896240362481024,
    "washing_cost": 0.0007325332606858571,
    "fine_transfer": 0.004688331915143319,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.006110489212077279,
    "resource_cost_fraction_initial_cap": 4.7405243231131977e-05,
    "private_net_outflow_fraction_initial_cap": 0.00020368297373590927,
    "fine_transfer_fraction_initial_cap": 0.0001562777305047773,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 7.555522702814039e-05,
    "unapplied_final_day_resource_cost": 2.3927820385761816e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 1390.4931643380057,
    "beneficial_raw_gain_per_resource_cost": 20857.397465070084,
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
    "accrued_cost": 3.0177713694624604,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.04158089327198343,
    "accrued_cost_fraction_initial_cap": 0.100592378982082,
    "mean_contract_rate": 0.04219898525799944,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 4.916515775507967e-15,
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
      "minimum": -0.22401565316614083,
      "maximum": -0.07941275912329344,
      "mean": -0.13856563038428363,
      "median": -0.13219857934080914,
      "quantile_05": -0.1964982216417843,
      "quantile_95": -0.08311086455016377
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
      "minimum": 0.12650136290838707,
      "maximum": 0.8439238956557998,
      "mean": 0.5589763684713068,
      "median": 0.5903830513067075,
      "quantile_05": 0.2979756759717123,
      "quantile_95": 0.7411436095180529
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
        "daily_volatility": 0.019376484895444773,
        "excess_kurtosis": 7.796607251823783,
        "return_acf_1": -0.102337369684182,
        "abs_return_acf_1": 0.2792548059413656,
        "abs_return_acf_5": 0.38238319502025664,
        "abs_return_acf_20": 0.28492768788372874,
        "quantile_01": -0.06370515302639408,
        "quantile_99": 0.055917530514090576,
        "hill_tail_index": 3.1526645551959627
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024998511166222915,
        "excess_kurtosis": 12.945819354002385,
        "return_acf_1": -0.18755262147142754,
        "abs_return_acf_1": 0.4991500961601364,
        "abs_return_acf_5": 0.42495460755114967,
        "abs_return_acf_20": 0.37565524889200475,
        "quantile_01": -0.08902250886446177,
        "quantile_99": 0.07386782051761519,
        "hill_tail_index": 3.543810315740387
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01968030886486004,
        "excess_kurtosis": 8.639906344754548,
        "return_acf_1": -0.14124993808231506,
        "abs_return_acf_1": 0.3380821493619694,
        "abs_return_acf_5": 0.3892097041260477,
        "abs_return_acf_20": 0.35624108397446425,
        "quantile_01": -0.05894860006925493,
        "quantile_99": 0.05543171490924141,
        "hill_tail_index": 3.2162858310535447
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.026047312147303277,
        "excess_kurtosis": 17.926799199997465,
        "return_acf_1": -0.09334840358922483,
        "abs_return_acf_1": 0.5257458908051339,
        "abs_return_acf_5": 0.4961746482234482,
        "abs_return_acf_20": 0.43455417097094307,
        "quantile_01": -0.08559213854228989,
        "quantile_99": 0.09141643281275147,
        "hill_tail_index": 2.6509105766995966
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022587969671179528,
        "excess_kurtosis": 41.691240124852214,
        "return_acf_1": -0.19108893693508094,
        "abs_return_acf_1": 0.2806911411541155,
        "abs_return_acf_5": 0.1776237065344899,
        "abs_return_acf_20": 0.19301415039106712,
        "quantile_01": -0.05952796946308576,
        "quantile_99": 0.058836690976323706,
        "hill_tail_index": 3.55016722454568
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02339475769677157,
        "excess_kurtosis": 15.596263637163506,
        "return_acf_1": -0.09380090099786263,
        "abs_return_acf_1": 0.37879562349468776,
        "abs_return_acf_5": 0.34595265733885405,
        "abs_return_acf_20": 0.3166940978391896,
        "quantile_01": -0.07890110131830044,
        "quantile_99": 0.06402621641939614,
        "hill_tail_index": 2.7480152740890964
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.024074535663391284,
        "excess_kurtosis": 13.92490385674212,
        "return_acf_1": -0.11362908140957201,
        "abs_return_acf_1": 0.4557900037275991,
        "abs_return_acf_5": 0.38524124944877625,
        "abs_return_acf_20": 0.2967664071507156,
        "quantile_01": -0.0830105631866612,
        "quantile_99": 0.07707845995571531,
        "hill_tail_index": 3.712294860118315
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02133892712434811,
        "excess_kurtosis": 9.651052027191191,
        "return_acf_1": -0.22401565316614083,
        "abs_return_acf_1": 0.3495477597172876,
        "abs_return_acf_5": 0.3761257775874284,
        "abs_return_acf_20": 0.31943210361448005,
        "quantile_01": -0.0727922540276975,
        "quantile_99": 0.06781032750716703,
        "hill_tail_index": 2.9024369065975244
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019110787026827395,
        "excess_kurtosis": 12.15646241767398,
        "return_acf_1": -0.19009944943282078,
        "abs_return_acf_1": 0.3524946959473812,
        "abs_return_acf_5": 0.23955216109395255,
        "abs_return_acf_20": 0.29170511412984645,
        "quantile_01": -0.06463799669019854,
        "quantile_99": 0.053193734903596454,
        "hill_tail_index": 3.5451510551339402
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021104247422305485,
        "excess_kurtosis": 13.565327216736495,
        "return_acf_1": -0.08453216545862767,
        "abs_return_acf_1": 0.3238767312605097,
        "abs_return_acf_5": 0.3747505568903397,
        "abs_return_acf_20": 0.33284165896182955,
        "quantile_01": -0.06987449832807373,
        "quantile_99": 0.06328691519588144,
        "hill_tail_index": 2.8560361592588612
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02099411101924429,
        "excess_kurtosis": 14.074916855518929,
        "return_acf_1": -0.102448827093735,
        "abs_return_acf_1": 0.3787951658450992,
        "abs_return_acf_5": 0.39493217866488406,
        "abs_return_acf_20": 0.2916855608731955,
        "quantile_01": -0.06809477088163997,
        "quantile_99": 0.062374089855071986,
        "hill_tail_index": 3.084815014919352
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018463383624023052,
        "excess_kurtosis": 4.41338268421205,
        "return_acf_1": -0.11667685136015517,
        "abs_return_acf_1": 0.3314142863603999,
        "abs_return_acf_5": 0.3248860799537389,
        "abs_return_acf_20": 0.25360194339904335,
        "quantile_01": -0.055183562633516266,
        "quantile_99": 0.04974783488032868,
        "hill_tail_index": 3.3285759315635426
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017666623944938873,
        "excess_kurtosis": 4.775242472104415,
        "return_acf_1": -0.08194798198869328,
        "abs_return_acf_1": 0.22001924919988006,
        "abs_return_acf_5": 0.271733540166312,
        "abs_return_acf_20": 0.27947354326072726,
        "quantile_01": -0.05251255216053102,
        "quantile_99": 0.05027455068366247,
        "hill_tail_index": 4.680096107667814
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02490903661236181,
        "excess_kurtosis": 15.735881533240782,
        "return_acf_1": -0.1212443165530193,
        "abs_return_acf_1": 0.4772377290744637,
        "abs_return_acf_5": 0.44043637395964963,
        "abs_return_acf_20": 0.3842236429277195,
        "quantile_01": -0.0833106045684148,
        "quantile_99": 0.08284617076554168,
        "hill_tail_index": 2.49384324888863
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024169330227534005,
        "excess_kurtosis": 15.416895813938655,
        "return_acf_1": -0.1592534030622618,
        "abs_return_acf_1": 0.48912510505434004,
        "abs_return_acf_5": 0.44884247071113237,
        "abs_return_acf_20": 0.30973967194092616,
        "quantile_01": -0.0865220715728793,
        "quantile_99": 0.07909531976904602,
        "hill_tail_index": 3.9164923739267357
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021261956994257317,
        "excess_kurtosis": 11.14099700274388,
        "return_acf_1": -0.1863582364879143,
        "abs_return_acf_1": 0.3916615088257378,
        "abs_return_acf_5": 0.3532790902824263,
        "abs_return_acf_20": 0.2811644349879553,
        "quantile_01": -0.07586780763920517,
        "quantile_99": 0.06757877292790324,
        "hill_tail_index": 3.4816066870234414
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019874356842507202,
        "excess_kurtosis": 7.185951735586437,
        "return_acf_1": -0.13925169021667877,
        "abs_return_acf_1": 0.36977808677261165,
        "abs_return_acf_5": 0.36632519233902916,
        "abs_return_acf_20": 0.26879032633396094,
        "quantile_01": -0.06612403099216994,
        "quantile_99": 0.05637416399813737,
        "hill_tail_index": 3.305750708878781
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019931615593576306,
        "excess_kurtosis": 5.359210366465872,
        "return_acf_1": -0.17890884688031433,
        "abs_return_acf_1": 0.30456867299360246,
        "abs_return_acf_5": 0.3450385464652734,
        "abs_return_acf_20": 0.20747530071838385,
        "quantile_01": -0.06102054284777086,
        "quantile_99": 0.06113112210014648,
        "hill_tail_index": 4.033969242162163
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018088830665326294,
        "excess_kurtosis": 4.456163648223119,
        "return_acf_1": -0.1264088565146996,
        "abs_return_acf_1": 0.3133675655324492,
        "abs_return_acf_5": 0.2821015105759089,
        "abs_return_acf_20": 0.26599284038284177,
        "quantile_01": -0.056385488641081484,
        "quantile_99": 0.049340238663008025,
        "hill_tail_index": 4.004141416642756
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019179864203674055,
        "excess_kurtosis": 10.228798022025323,
        "return_acf_1": -0.1903590524182877,
        "abs_return_acf_1": 0.3665204917802441,
        "abs_return_acf_5": 0.3872321468866143,
        "abs_return_acf_20": 0.3255952443418711,
        "quantile_01": -0.0575181929238363,
        "quantile_99": 0.058025216595381936,
        "hill_tail_index": 2.744108763209706
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019988083805305937,
        "excess_kurtosis": 5.619821081288356,
        "return_acf_1": -0.11011360331590944,
        "abs_return_acf_1": 0.40154230781963757,
        "abs_return_acf_5": 0.36030809376089756,
        "abs_return_acf_20": 0.32901454119192863,
        "quantile_01": -0.06499040153413775,
        "quantile_99": 0.07272974147493477,
        "hill_tail_index": 3.59498641496237
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019273719869996944,
        "excess_kurtosis": 5.600391720949311,
        "return_acf_1": -0.09285183278313995,
        "abs_return_acf_1": 0.32949561831957436,
        "abs_return_acf_5": 0.3135633521106741,
        "abs_return_acf_20": 0.28679433327111997,
        "quantile_01": -0.06728222037511006,
        "quantile_99": 0.04574770065390145,
        "hill_tail_index": 4.534251031570644
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020193230055076727,
        "excess_kurtosis": 8.785585973942752,
        "return_acf_1": -0.14221489119883401,
        "abs_return_acf_1": 0.29021618232067,
        "abs_return_acf_5": 0.2947482294743688,
        "abs_return_acf_20": 0.27370480716375906,
        "quantile_01": -0.0705399988521813,
        "quantile_99": 0.05660009227092765,
        "hill_tail_index": 2.6868759193332314
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019701439562814102,
        "excess_kurtosis": 34.15230744443768,
        "return_acf_1": -0.1757475610823512,
        "abs_return_acf_1": 0.3059248644077571,
        "abs_return_acf_5": 0.19556601072335955,
        "abs_return_acf_20": 0.23280167015939765,
        "quantile_01": -0.05074634525618284,
        "quantile_99": 0.05224906704477624,
        "hill_tail_index": 2.9885272756108994
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.024536705282061658,
        "excess_kurtosis": 14.976914329651482,
        "return_acf_1": -0.16660981587058327,
        "abs_return_acf_1": 0.4002419439051908,
        "abs_return_acf_5": 0.4106320698842649,
        "abs_return_acf_20": 0.4229294598583989,
        "quantile_01": -0.07177466692017682,
        "quantile_99": 0.07004458159365044,
        "hill_tail_index": 2.8247676250788234
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019407675671014837,
        "excess_kurtosis": 11.257288688374059,
        "return_acf_1": -0.07941275912329344,
        "abs_return_acf_1": 0.2948824551498419,
        "abs_return_acf_5": 0.2917081046249901,
        "abs_return_acf_20": 0.23695831827015348,
        "quantile_01": -0.0625955607424394,
        "quantile_99": 0.04790531305142572,
        "hill_tail_index": 2.7453685106562156
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025265105148711945,
        "excess_kurtosis": 17.234486639784212,
        "return_acf_1": -0.20092400003817795,
        "abs_return_acf_1": 0.5166043396058363,
        "abs_return_acf_5": 0.3705842892940884,
        "abs_return_acf_20": 0.3346761051927781,
        "quantile_01": -0.09478945092186712,
        "quantile_99": 0.0719237798337715,
        "hill_tail_index": 3.1625029337454054
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02377149808353131,
        "excess_kurtosis": 11.825134533295337,
        "return_acf_1": -0.13141876464095534,
        "abs_return_acf_1": 0.49365765875501527,
        "abs_return_acf_5": 0.45833747469307295,
        "abs_return_acf_20": 0.32714595239186073,
        "quantile_01": -0.09003253490749967,
        "quantile_99": 0.06356452512695179,
        "hill_tail_index": 2.641730976973432
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021132871625193138,
        "excess_kurtosis": 7.92535562816337,
        "return_acf_1": -0.10018470663158763,
        "abs_return_acf_1": 0.33838215466164356,
        "abs_return_acf_5": 0.3310504754870778,
        "abs_return_acf_20": 0.30345597764584664,
        "quantile_01": -0.07337477126307611,
        "quantile_99": 0.06593877898235886,
        "hill_tail_index": 3.4887512451805662
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019634179802901726,
        "excess_kurtosis": 6.739116017912801,
        "return_acf_1": -0.13297839404066294,
        "abs_return_acf_1": 0.29250494265578636,
        "abs_return_acf_5": 0.3182266907497612,
        "abs_return_acf_20": 0.2428559441564655,
        "quantile_01": -0.05892923439142402,
        "quantile_99": 0.05662864851057871,
        "hill_tail_index": 3.7422737061265243
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
Training: False
Coverage status: FAIL
Unseen state share: 0.04555555555555556
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
