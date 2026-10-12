# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27306
Run ID: `4254da31c1106bc28f3aafb11fcada2ede04dda612a4a9c1ea69c86505d54f14`
Result fingerprint: `5c46ebdf76fef365828bd7a99ec96efc8d50fe8a676ce73920174f8672df01fb`

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
    "equal_weight_sd": -0.8985476190476158,
    "equal_weight_raw": -13.478214285714234,
    "fixed_start_cap_weight_sd": -0.8590114966129259,
    "fixed_start_cap_weight_raw": -12.885172449193888,
    "end_cap_weight_sd": -0.864425362059981,
    "end_cap_weight_raw": -12.966380430899713
  },
  "full_period_change": {
    "equal_weight_sd": -1.365404761904757,
    "equal_weight_raw": -20.481071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.274668981481477,
    "inflation_mean_sd": 0.3440357142857143
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.053833333333336605,
    "equal_weight_raw": 0.807500000000049,
    "fixed_start_cap_weight_sd": 0.09336945576802659,
    "fixed_start_cap_weight_raw": 1.4005418365203992,
    "end_cap_weight_sd": 0.08795559032097133,
    "end_cap_weight_raw": 1.3193338548145699
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7290476190476157,
      "change_raw": -10.935714285714235,
      "decay_adjusted_gain_sd": 0.22333333333333663
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8740476190476156,
      "change_raw": -13.110714285714234,
      "decay_adjusted_gain_sd": 0.07833333333333659
    },
    "small": {
      "count": 18,
      "change_sd": -0.9390476190476158,
      "change_raw": -14.085714285714237,
      "decay_adjusted_gain_sd": 0.013333333333336602
    },
    "large_minus_small_sd": 0.21000000000000008,
    "large_minus_small_raw": 3.1500000000000012
  },
  "inflation": {
    "initial_mean_sd": 0.21400000000000002,
    "final_mean_sd": 0.35208333333333347,
    "mean_sd": 0.29216382181515405,
    "mean_absolute_raw_gap": 4.382457327227311,
    "final_absolute_raw_gap": 5.281250000000001,
    "mean_range_fraction": 0.043824573272273105
  },
  "impact": {
    "initial_share": 0.4533333333333333,
    "final_share": 0.5066666666666667,
    "initial_wealth_share": 0.4575523110953896,
    "final_wealth_share": 0.5785539292847667
  },
  "pricing_slope": {
    "mean": -0.0026731127522707536,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.006810434239673598,
    "real_improvement_cost": 0.0011317414137999582,
    "washing_cost": 0.005678692825873639,
    "fine_transfer": 0.005997612726989758,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.012808046966663355,
    "resource_cost_fraction_initial_cap": 0.0002270144746557866,
    "private_net_outflow_fraction_initial_cap": 0.00042693489888877853,
    "fine_transfer_fraction_initial_cap": 0.0001999204242329919,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0014583678226614582,
    "unapplied_final_day_resource_cost": 7.415569761118733e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 237.1361271785072,
    "beneficial_raw_gain_per_resource_cost": 3557.041907677608,
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
    "accrued_cost": 3.0515113698136584,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.07532089362318185,
    "accrued_cost_fraction_initial_cap": 0.10171704566045528,
    "mean_contract_rate": 0.043005321442855904,
    "maximum_ledger_error": 7.538593230563273e-20
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
    "maximum_relative_cash_error": 1.8669929516909007e-15,
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
      "minimum": -0.16301679799571595,
      "maximum": -0.03827545247543843,
      "mean": -0.09515688967031824,
      "median": -0.09120032674486123,
      "quantile_05": -0.15054273167637414,
      "quantile_95": -0.0508335546919048
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
      "minimum": 0.5931418775644224,
      "maximum": 0.8022816476693564,
      "mean": 0.7281305472196024,
      "median": 0.7358050692015815,
      "quantile_05": 0.6557070000824987,
      "quantile_95": 0.7737428810050907
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
        "daily_volatility": 0.01984169670521219,
        "excess_kurtosis": 4.98461692289144,
        "return_acf_1": -0.104816243950318,
        "abs_return_acf_1": 0.30518788570526617,
        "abs_return_acf_5": 0.328871680793158,
        "abs_return_acf_20": 0.30870311565269626,
        "quantile_01": -0.06572486197156986,
        "quantile_99": 0.05968928302691261,
        "hill_tail_index": 5.340583556333259
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019919582856348823,
        "excess_kurtosis": 5.952892805983341,
        "return_acf_1": -0.16301679799571595,
        "abs_return_acf_1": 0.4196107761493323,
        "abs_return_acf_5": 0.3847180258540034,
        "abs_return_acf_20": 0.2057535356853614,
        "quantile_01": -0.06617223114264222,
        "quantile_99": 0.05444954588017048,
        "hill_tail_index": 4.466196792785287
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020706952059757956,
        "excess_kurtosis": 9.481278878046764,
        "return_acf_1": -0.14707956382336876,
        "abs_return_acf_1": 0.42867318860180187,
        "abs_return_acf_5": 0.3604384076655118,
        "abs_return_acf_20": 0.20942329821581093,
        "quantile_01": -0.07295841866799128,
        "quantile_99": 0.05104647287236133,
        "hill_tail_index": 2.683697347344332
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01949350270532487,
        "excess_kurtosis": 8.156454209252118,
        "return_acf_1": -0.09590421332700973,
        "abs_return_acf_1": 0.3130721456304497,
        "abs_return_acf_5": 0.3291051930259173,
        "abs_return_acf_20": 0.2333396164605398,
        "quantile_01": -0.06121105883240413,
        "quantile_99": 0.049241142242233284,
        "hill_tail_index": 3.1308972251867555
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020791729242676252,
        "excess_kurtosis": 4.754112790979389,
        "return_acf_1": -0.09153618945108946,
        "abs_return_acf_1": 0.4553711388051684,
        "abs_return_acf_5": 0.4186563457080206,
        "abs_return_acf_20": 0.3292506589228714,
        "quantile_01": -0.06799770922265909,
        "quantile_99": 0.05431036001032124,
        "hill_tail_index": 4.925637296313361
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019543265513829993,
        "excess_kurtosis": 4.505788550563593,
        "return_acf_1": -0.11194250817964957,
        "abs_return_acf_1": 0.30158292999180253,
        "abs_return_acf_5": 0.39306477651381966,
        "abs_return_acf_20": 0.2485914692351335,
        "quantile_01": -0.06981599691350565,
        "quantile_99": 0.05495505006304809,
        "hill_tail_index": 4.159822736045995
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020342815031437967,
        "excess_kurtosis": 5.473903003469626,
        "return_acf_1": -0.1416529684452847,
        "abs_return_acf_1": 0.32811345246732604,
        "abs_return_acf_5": 0.38656751878827217,
        "abs_return_acf_20": 0.2949589321563543,
        "quantile_01": -0.06758297180315524,
        "quantile_99": 0.06017541583622967,
        "hill_tail_index": 4.5264433468694705
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01965504872520168,
        "excess_kurtosis": 7.497664414609504,
        "return_acf_1": -0.04705895277870193,
        "abs_return_acf_1": 0.3445243862315642,
        "abs_return_acf_5": 0.3864789419248647,
        "abs_return_acf_20": 0.2087175159819151,
        "quantile_01": -0.06646489893811648,
        "quantile_99": 0.05724493559302145,
        "hill_tail_index": 2.901591206113876
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01796086997251466,
        "excess_kurtosis": 4.746642813291022,
        "return_acf_1": -0.06354440337720758,
        "abs_return_acf_1": 0.28316955649933157,
        "abs_return_acf_5": 0.2921667631162903,
        "abs_return_acf_20": 0.2424620991105425,
        "quantile_01": -0.05614138223304603,
        "quantile_99": 0.04508459503281171,
        "hill_tail_index": 3.8279681068297156
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020355779600685558,
        "excess_kurtosis": 6.792341873693658,
        "return_acf_1": -0.09086446403863299,
        "abs_return_acf_1": 0.41946743866827935,
        "abs_return_acf_5": 0.39075974885662695,
        "abs_return_acf_20": 0.24947519171102925,
        "quantile_01": -0.07020447262862846,
        "quantile_99": 0.05883244649215713,
        "hill_tail_index": 3.825672452449622
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019408705690945174,
        "excess_kurtosis": 4.272527828324306,
        "return_acf_1": -0.13025761084655785,
        "abs_return_acf_1": 0.28342429822402426,
        "abs_return_acf_5": 0.42517545833632137,
        "abs_return_acf_20": 0.30289413904229767,
        "quantile_01": -0.06005631963936805,
        "quantile_99": 0.057624327896393435,
        "hill_tail_index": 5.3202945569056785
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020477015417195377,
        "excess_kurtosis": 5.809625536140171,
        "return_acf_1": -0.12253065411919065,
        "abs_return_acf_1": 0.41276447066338817,
        "abs_return_acf_5": 0.3835091923088653,
        "abs_return_acf_20": 0.2851143696788997,
        "quantile_01": -0.06950856248587059,
        "quantile_99": 0.05310965894867856,
        "hill_tail_index": 3.3501699859875194
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022226023554467293,
        "excess_kurtosis": 9.184233087235521,
        "return_acf_1": -0.05544695703026382,
        "abs_return_acf_1": 0.48244811670527216,
        "abs_return_acf_5": 0.5069046963984053,
        "abs_return_acf_20": 0.32126554680613945,
        "quantile_01": -0.08490873821266283,
        "quantile_99": 0.06595223561093749,
        "hill_tail_index": 3.273411864573757
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02001134115582827,
        "excess_kurtosis": 7.282362761647072,
        "return_acf_1": -0.08335124329912659,
        "abs_return_acf_1": 0.3742561370092995,
        "abs_return_acf_5": 0.3212451171666946,
        "abs_return_acf_20": 0.22203618979129447,
        "quantile_01": -0.06113697306371093,
        "quantile_99": 0.051090033045633115,
        "hill_tail_index": 3.6197776770197496
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020190267324874816,
        "excess_kurtosis": 8.240984159872525,
        "return_acf_1": -0.13384757312801018,
        "abs_return_acf_1": 0.3314573898834214,
        "abs_return_acf_5": 0.4104275476081857,
        "abs_return_acf_20": 0.261798765307975,
        "quantile_01": -0.07035066860361625,
        "quantile_99": 0.05195647434442721,
        "hill_tail_index": 3.662067768498875
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0191913294423272,
        "excess_kurtosis": 5.209978484104562,
        "return_acf_1": -0.06808008118751005,
        "abs_return_acf_1": 0.3272579379787646,
        "abs_return_acf_5": 0.36400428024733006,
        "abs_return_acf_20": 0.32494548811691676,
        "quantile_01": -0.06436229306292336,
        "quantile_99": 0.048264779908609404,
        "hill_tail_index": 3.334348216094786
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020673025033629895,
        "excess_kurtosis": 7.173546688622643,
        "return_acf_1": -0.07440166392811841,
        "abs_return_acf_1": 0.3585837745482499,
        "abs_return_acf_5": 0.36191226876368476,
        "abs_return_acf_20": 0.2511015402825637,
        "quantile_01": -0.07333535448742017,
        "quantile_99": 0.06078121881879819,
        "hill_tail_index": 3.736080526037829
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019191519008738913,
        "excess_kurtosis": 4.574833814952026,
        "return_acf_1": -0.061919865125009056,
        "abs_return_acf_1": 0.36741009462062874,
        "abs_return_acf_5": 0.3336238600161335,
        "abs_return_acf_20": 0.1745567451324444,
        "quantile_01": -0.06379210101696735,
        "quantile_99": 0.049823334079128985,
        "hill_tail_index": 4.204427643588134
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018779497877931487,
        "excess_kurtosis": 6.864450607560141,
        "return_acf_1": -0.09036885234915552,
        "abs_return_acf_1": 0.33461756564139605,
        "abs_return_acf_5": 0.3680536417319953,
        "abs_return_acf_20": 0.20906055175859775,
        "quantile_01": -0.055727086643687154,
        "quantile_99": 0.049902000133569345,
        "hill_tail_index": 3.2998618717978223
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020243271029663543,
        "excess_kurtosis": 5.639607811341907,
        "return_acf_1": -0.08014608815618016,
        "abs_return_acf_1": 0.31126244387578267,
        "abs_return_acf_5": 0.42791756275317144,
        "abs_return_acf_20": 0.3536614211253594,
        "quantile_01": -0.06031712342874819,
        "quantile_99": 0.06056550807003038,
        "hill_tail_index": 4.0017096259771945
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018978139456129507,
        "excess_kurtosis": 5.705891875560978,
        "return_acf_1": -0.07529906035346272,
        "abs_return_acf_1": 0.29646838206277903,
        "abs_return_acf_5": 0.3781088924716068,
        "abs_return_acf_20": 0.2151926397959376,
        "quantile_01": -0.05900398428257395,
        "quantile_99": 0.05231366434043126,
        "hill_tail_index": 3.367817937733103
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021951453181712745,
        "excess_kurtosis": 12.247077775943726,
        "return_acf_1": -0.11762872444603087,
        "abs_return_acf_1": 0.42695228550926917,
        "abs_return_acf_5": 0.4101724338738403,
        "abs_return_acf_20": 0.2152090918192547,
        "quantile_01": -0.07280389630979538,
        "quantile_99": 0.06755747853739598,
        "hill_tail_index": 2.1317742096779266
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02161909106469579,
        "excess_kurtosis": 9.287199311965436,
        "return_acf_1": -0.1533762326470149,
        "abs_return_acf_1": 0.4254518423756385,
        "abs_return_acf_5": 0.3965137122411464,
        "abs_return_acf_20": 0.300418555567693,
        "quantile_01": -0.0785668694602249,
        "quantile_99": 0.06354441337341027,
        "hill_tail_index": 3.49435918131504
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02031114261062038,
        "excess_kurtosis": 4.041412725630676,
        "return_acf_1": -0.10697940639632882,
        "abs_return_acf_1": 0.34442436913890867,
        "abs_return_acf_5": 0.404055869504018,
        "abs_return_acf_20": 0.29877014490927195,
        "quantile_01": -0.06366334586128772,
        "quantile_99": 0.058590479375020675,
        "hill_tail_index": 4.853664592907731
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01944291211776555,
        "excess_kurtosis": 5.363802936392911,
        "return_acf_1": -0.05826695973343974,
        "abs_return_acf_1": 0.3069649297582671,
        "abs_return_acf_5": 0.39912138276163805,
        "abs_return_acf_20": 0.32821942164836965,
        "quantile_01": -0.06465133588724796,
        "quantile_99": 0.058547278462943525,
        "hill_tail_index": 4.422881677025516
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01915271148119959,
        "excess_kurtosis": 5.4290053479977995,
        "return_acf_1": -0.11570867466793673,
        "abs_return_acf_1": 0.34012690281841007,
        "abs_return_acf_5": 0.3114614764445347,
        "abs_return_acf_20": 0.20462205831036023,
        "quantile_01": -0.06183677064926794,
        "quantile_99": 0.052926778657257874,
        "hill_tail_index": 3.2831672636999913
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02170427522796411,
        "excess_kurtosis": 6.92160164501796,
        "return_acf_1": -0.03827545247543843,
        "abs_return_acf_1": 0.4069013054186152,
        "abs_return_acf_5": 0.40932983453411925,
        "abs_return_acf_20": 0.33690532047562866,
        "quantile_01": -0.07327984466580546,
        "quantile_99": 0.05540311876878133,
        "hill_tail_index": 3.1060959785610214
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0189855367951242,
        "excess_kurtosis": 4.398271335128955,
        "return_acf_1": -0.05816394867897242,
        "abs_return_acf_1": 0.3164927093752119,
        "abs_return_acf_5": 0.3378757941398913,
        "abs_return_acf_20": 0.2143643998330967,
        "quantile_01": -0.061251610100252755,
        "quantile_99": 0.05055376661858894,
        "hill_tail_index": 3.8702645719527076
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020213031881454548,
        "excess_kurtosis": 6.1654632548798425,
        "return_acf_1": -0.10165672616376574,
        "abs_return_acf_1": 0.43851662531800123,
        "abs_return_acf_5": 0.4032754154337331,
        "abs_return_acf_20": 0.21893111304724439,
        "quantile_01": -0.06955919314761619,
        "quantile_99": 0.0537823713789751,
        "hill_tail_index": 3.2371454396322576
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019254793416009625,
        "excess_kurtosis": 5.640480722063867,
        "return_acf_1": -0.07158461001105618,
        "abs_return_acf_1": 0.32908763790810036,
        "abs_return_acf_5": 0.32063633398166663,
        "abs_return_acf_20": 0.22399329533439405,
        "quantile_01": -0.06262747912931399,
        "quantile_99": 0.05455068127485402,
        "hill_tail_index": 3.5020194413872567
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
Unseen state share: 0.0
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
