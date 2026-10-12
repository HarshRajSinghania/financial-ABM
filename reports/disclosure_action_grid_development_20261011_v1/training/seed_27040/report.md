# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27040
Run ID: `d028b42039798dfa826b2a06f8596bcb78692093d34fe143fed544f4941ae752`
Result fingerprint: `991920adb6b7d6d0d572744599201dbd781094ff4b15c79c4988f5cbf86465a3`

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
    "equal_weight_sd": -0.5787142857142825,
    "equal_weight_raw": -8.680714285714238,
    "fixed_start_cap_weight_sd": -0.5800812738784449,
    "fixed_start_cap_weight_raw": -8.701219108176675,
    "end_cap_weight_sd": -0.5711496717284577,
    "end_cap_weight_raw": -8.567245075926866
  },
  "full_period_change": {
    "equal_weight_sd": -0.8548214285714236,
    "equal_weight_raw": -12.822321428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8043693783068739,
    "inflation_mean_sd": 0.6099494047619048
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.37087103252381265,
    "equal_weight_raw": 5.563065487857191,
    "fixed_start_cap_weight_sd": 0.37173907489752495,
    "fixed_start_cap_weight_raw": 5.576086123462873,
    "end_cap_weight_sd": 0.3806235282920558,
    "end_cap_weight_raw": 5.709352924380836
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5057142857142826,
      "change_raw": -7.585714285714238,
      "decay_adjusted_gain_sd": 0.4466666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.645158730158727,
      "change_raw": -9.677380952380906,
      "decay_adjusted_gain_sd": 0.30722222222222545
    },
    "small": {
      "count": 18,
      "change_sd": -0.5576587301587268,
      "change_raw": -8.364880952380902,
      "decay_adjusted_gain_sd": 0.39006283198413016
    },
    "large_minus_small_sd": 0.05194444444444424,
    "large_minus_small_raw": 0.7791666666666636
  },
  "inflation": {
    "initial_mean_sd": 0.24191666666666667,
    "final_mean_sd": 0.6375833333333333,
    "mean_sd": 0.47570573133499866,
    "mean_absolute_raw_gap": 7.13558597002498,
    "final_absolute_raw_gap": 9.563749999999999,
    "mean_range_fraction": 0.0713558597002498
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.3933333333333333,
    "initial_wealth_share": 0.47168988553175895,
    "final_wealth_share": 0.4872561749954686
  },
  "pricing_slope": {
    "mean": -0.003760885292157988,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.11109237615943016,
    "real_improvement_cost": 0.09149980483965214,
    "washing_cost": 0.01959257131977803,
    "fine_transfer": 0.0042597588141800894,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11535213497361024,
    "resource_cost_fraction_initial_cap": 0.003703079205314338,
    "private_net_outflow_fraction_initial_cap": 0.0038450711657870076,
    "fine_transfer_fraction_initial_cap": 0.00014199196047266964,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0031345367569812006,
    "unapplied_final_day_resource_cost": 0.00023767812918167315
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 100.15206587846426,
    "beneficial_raw_gain_per_resource_cost": 1502.2809881769638,
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
    "accrued_cost": 3.2404138248007257,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.2642233486102489,
    "accrued_cost_fraction_initial_cap": 0.10801379416002417,
    "mean_contract_rate": 0.04415430951286354,
    "maximum_ledger_error": 1.8973538018496328e-19
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
    "maximum_relative_cash_error": 1.391363236705005e-15,
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
      "minimum": -0.23419130810358094,
      "maximum": -0.07980842544318366,
      "mean": -0.1508909540465094,
      "median": -0.15250106189230067,
      "quantile_05": -0.20794894577720746,
      "quantile_95": -0.08430071093953272
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
      "minimum": 0.2232276132158741,
      "maximum": 0.7784284550646908,
      "mean": 0.5856231372578192,
      "median": 0.6448376445061698,
      "quantile_05": 0.3019563504410926,
      "quantile_95": 0.7488564747173023
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
        "daily_volatility": 0.01751915040689154,
        "excess_kurtosis": 10.990928132210597,
        "return_acf_1": -0.08136321727162847,
        "abs_return_acf_1": 0.32914318256807634,
        "abs_return_acf_5": 0.369077362757529,
        "abs_return_acf_20": 0.2394877891838578,
        "quantile_01": -0.05470950029217632,
        "quantile_99": 0.04116128295883464,
        "hill_tail_index": 2.8649262938933875
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01671839930783741,
        "excess_kurtosis": 6.229665809715021,
        "return_acf_1": -0.14284124298162656,
        "abs_return_acf_1": 0.2553687986024672,
        "abs_return_acf_5": 0.29603039999430747,
        "abs_return_acf_20": 0.18688425438359957,
        "quantile_01": -0.04856884429119666,
        "quantile_99": 0.04400058355590785,
        "hill_tail_index": 3.615904941834432
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01778608453348494,
        "excess_kurtosis": 15.191813654836889,
        "return_acf_1": -0.18956812792376646,
        "abs_return_acf_1": 0.4280088061070779,
        "abs_return_acf_5": 0.3547643600908342,
        "abs_return_acf_20": 0.28569358030530156,
        "quantile_01": -0.05346127471001135,
        "quantile_99": 0.04167756544081575,
        "hill_tail_index": 2.2428474494717583
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018137039961014137,
        "excess_kurtosis": 6.340258213762782,
        "return_acf_1": -0.15709156947001468,
        "abs_return_acf_1": 0.3578884833442451,
        "abs_return_acf_5": 0.26601636057050465,
        "abs_return_acf_20": 0.2517521198008179,
        "quantile_01": -0.05550821652350958,
        "quantile_99": 0.046773055011053416,
        "hill_tail_index": 2.5796189698423024
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01983905612565057,
        "excess_kurtosis": 5.137005893028556,
        "return_acf_1": -0.23419130810358094,
        "abs_return_acf_1": 0.4092561272694237,
        "abs_return_acf_5": 0.4521814916105772,
        "abs_return_acf_20": 0.29432395316038956,
        "quantile_01": -0.060300053133554306,
        "quantile_99": 0.05758046137010976,
        "hill_tail_index": 3.746873786311348
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017489187583150583,
        "excess_kurtosis": 7.658908340347336,
        "return_acf_1": -0.14390625631856152,
        "abs_return_acf_1": 0.2537183554870541,
        "abs_return_acf_5": 0.27004430193740186,
        "abs_return_acf_20": 0.20254785691498645,
        "quantile_01": -0.04948778953961215,
        "quantile_99": 0.04290803250766483,
        "hill_tail_index": 2.6006622232968715
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019509436936960643,
        "excess_kurtosis": 15.261110529201776,
        "return_acf_1": -0.1442464157481065,
        "abs_return_acf_1": 0.44472688499068197,
        "abs_return_acf_5": 0.37083852491579333,
        "abs_return_acf_20": 0.346921012030558,
        "quantile_01": -0.06086694437326983,
        "quantile_99": 0.046041223200387754,
        "hill_tail_index": 2.2065525422488723
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.016399552700621052,
        "excess_kurtosis": 6.241525111655164,
        "return_acf_1": -0.13152384721923338,
        "abs_return_acf_1": 0.2505660080920886,
        "abs_return_acf_5": 0.25418732129878585,
        "abs_return_acf_20": 0.19275241630421075,
        "quantile_01": -0.04795848616522888,
        "quantile_99": 0.042815113393489625,
        "hill_tail_index": 2.8440847231039
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019132059353017462,
        "excess_kurtosis": 17.639256745885017,
        "return_acf_1": -0.20273923470508337,
        "abs_return_acf_1": 0.3821993852784048,
        "abs_return_acf_5": 0.4173881581533046,
        "abs_return_acf_20": 0.34601362603174585,
        "quantile_01": -0.0635454660981572,
        "quantile_99": 0.04603779836438197,
        "hill_tail_index": 2.276399749024404
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016680403203213234,
        "excess_kurtosis": 7.013469114175162,
        "return_acf_1": -0.16107862254335664,
        "abs_return_acf_1": 0.22915739667102888,
        "abs_return_acf_5": 0.2914885864253279,
        "abs_return_acf_20": 0.21125161011847957,
        "quantile_01": -0.048453934913610164,
        "quantile_99": 0.04209366164873563,
        "hill_tail_index": 2.3749529278659396
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017936960348255197,
        "excess_kurtosis": 4.678204319459097,
        "return_acf_1": -0.1808834281671119,
        "abs_return_acf_1": 0.33429201990129664,
        "abs_return_acf_5": 0.35560548727853103,
        "abs_return_acf_20": 0.19286196386773877,
        "quantile_01": -0.05410862481283561,
        "quantile_99": 0.05151420646863387,
        "hill_tail_index": 3.5682139391416823
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017043131030726206,
        "excess_kurtosis": 9.131045856363333,
        "return_acf_1": -0.2122114366543999,
        "abs_return_acf_1": 0.31988503042201394,
        "abs_return_acf_5": 0.35213103027681014,
        "abs_return_acf_20": 0.26486412648365454,
        "quantile_01": -0.05072888588295442,
        "quantile_99": 0.04558530792917797,
        "hill_tail_index": 2.6521958095260305
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01798412746201619,
        "excess_kurtosis": 13.802670490503509,
        "return_acf_1": -0.16266598209253003,
        "abs_return_acf_1": 0.416057708007206,
        "abs_return_acf_5": 0.30960260169914655,
        "abs_return_acf_20": 0.30125763813004847,
        "quantile_01": -0.05810926569352858,
        "quantile_99": 0.0422007472261758,
        "hill_tail_index": 2.0441437359907813
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016964394346648308,
        "excess_kurtosis": 9.558909657483008,
        "return_acf_1": -0.18825094305418444,
        "abs_return_acf_1": 0.32692036084687687,
        "abs_return_acf_5": 0.29736599072933223,
        "abs_return_acf_20": 0.25335158350907877,
        "quantile_01": -0.050290865798558425,
        "quantile_99": 0.04105052802966594,
        "hill_tail_index": 2.4009357565659175
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01787558172387028,
        "excess_kurtosis": 7.989516945305692,
        "return_acf_1": -0.15470981951586144,
        "abs_return_acf_1": 0.3206713275810138,
        "abs_return_acf_5": 0.37894264731792837,
        "abs_return_acf_20": 0.26310294867495154,
        "quantile_01": -0.05372745878032172,
        "quantile_99": 0.05315403120249632,
        "hill_tail_index": 3.3663588701793214
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.015105135631880777,
        "excess_kurtosis": 4.483479843350875,
        "return_acf_1": -0.19174349047626418,
        "abs_return_acf_1": 0.18948668794767912,
        "abs_return_acf_5": 0.19258567487753156,
        "abs_return_acf_20": 0.13583489290735085,
        "quantile_01": -0.03737115295834494,
        "quantile_99": 0.036345436200502165,
        "hill_tail_index": 3.0024602466569132
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018077995371026792,
        "excess_kurtosis": 13.645472135890113,
        "return_acf_1": -0.10518932252780944,
        "abs_return_acf_1": 0.4169491122565678,
        "abs_return_acf_5": 0.391788541005328,
        "abs_return_acf_20": 0.2700303740707383,
        "quantile_01": -0.05499568721574545,
        "quantile_99": 0.04274593522629397,
        "hill_tail_index": 1.858000370191913
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017146987090869197,
        "excess_kurtosis": 6.075940891905301,
        "return_acf_1": -0.18360741620820206,
        "abs_return_acf_1": 0.2792169188403385,
        "abs_return_acf_5": 0.2862837515842378,
        "abs_return_acf_20": 0.26651215295779307,
        "quantile_01": -0.053846551592820195,
        "quantile_99": 0.049332993975729544,
        "hill_tail_index": 3.384227494228888
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016733798239978764,
        "excess_kurtosis": 11.820541463708462,
        "return_acf_1": -0.10495212537167876,
        "abs_return_acf_1": 0.20443145414765349,
        "abs_return_acf_5": 0.27770527688575175,
        "abs_return_acf_20": 0.21200227410102265,
        "quantile_01": -0.0498064187210383,
        "quantile_99": 0.04121027253998065,
        "hill_tail_index": 2.28205279844859
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01578206130825905,
        "excess_kurtosis": 4.216110837982344,
        "return_acf_1": -0.09774183801105754,
        "abs_return_acf_1": 0.24607422633520734,
        "abs_return_acf_5": 0.20834291766539725,
        "abs_return_acf_20": 0.21654529443374346,
        "quantile_01": -0.04475570590742077,
        "quantile_99": 0.04314325856699031,
        "hill_tail_index": 4.0702650266587685
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016107637537823256,
        "excess_kurtosis": 11.026287082236585,
        "return_acf_1": -0.13496494269643816,
        "abs_return_acf_1": 0.2538942879404096,
        "abs_return_acf_5": 0.24286344197565507,
        "abs_return_acf_20": 0.19319010746376927,
        "quantile_01": -0.04474885146671961,
        "quantile_99": 0.03862737775806852,
        "hill_tail_index": 2.383432759328426
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017981423783622247,
        "excess_kurtosis": 8.713504045642608,
        "return_acf_1": -0.16859382747535961,
        "abs_return_acf_1": 0.30256492765948095,
        "abs_return_acf_5": 0.26302054240445866,
        "abs_return_acf_20": 0.23868407565997593,
        "quantile_01": -0.05702067428355967,
        "quantile_99": 0.04628426333427819,
        "hill_tail_index": 2.476129906852641
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018620835047499257,
        "excess_kurtosis": 18.427266951890036,
        "return_acf_1": -0.08789098097808232,
        "abs_return_acf_1": 0.38629486422702863,
        "abs_return_acf_5": 0.36893826358369103,
        "abs_return_acf_20": 0.2801629837624794,
        "quantile_01": -0.05306619527677481,
        "quantile_99": 0.04113295592875377,
        "hill_tail_index": 1.7876827797752286
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016633281668858916,
        "excess_kurtosis": 6.566743269526199,
        "return_acf_1": -0.1278922443660629,
        "abs_return_acf_1": 0.3038453673403916,
        "abs_return_acf_5": 0.21260813389001468,
        "abs_return_acf_20": 0.14820615919555163,
        "quantile_01": -0.04477674551358555,
        "quantile_99": 0.04282132644578982,
        "hill_tail_index": 2.6554291975884032
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020195517172293467,
        "excess_kurtosis": 18.11625368076316,
        "return_acf_1": -0.1502923042687399,
        "abs_return_acf_1": 0.3971590743433319,
        "abs_return_acf_5": 0.42781806059069477,
        "abs_return_acf_20": 0.30672241958662694,
        "quantile_01": -0.07788736928691843,
        "quantile_99": 0.05243038452074919,
        "hill_tail_index": 1.587650824281805
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017912077620799504,
        "excess_kurtosis": 14.441358465595169,
        "return_acf_1": -0.07980842544318366,
        "abs_return_acf_1": 0.3688510664133782,
        "abs_return_acf_5": 0.33826063897303627,
        "abs_return_acf_20": 0.3505989508997449,
        "quantile_01": -0.06137329555490705,
        "quantile_99": 0.04342924219323184,
        "hill_tail_index": 2.1106387933026336
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017937489619253434,
        "excess_kurtosis": 5.4383979243412455,
        "return_acf_1": -0.1590668264886615,
        "abs_return_acf_1": 0.22023927898789503,
        "abs_return_acf_5": 0.24729282579056977,
        "abs_return_acf_20": 0.2217199338477862,
        "quantile_01": -0.0529648632597361,
        "quantile_99": 0.04884444221137531,
        "hill_tail_index": 3.6829301445829916
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01751487629124559,
        "excess_kurtosis": 8.71211838097858,
        "return_acf_1": -0.16496044789630435,
        "abs_return_acf_1": 0.2962483739645566,
        "abs_return_acf_5": 0.2931208369420409,
        "abs_return_acf_20": 0.2033779017325981,
        "quantile_01": -0.05175192347735869,
        "quantile_99": 0.04180835172592634,
        "hill_tail_index": 2.277199596869163
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017306418342674178,
        "excess_kurtosis": 7.284907608875315,
        "return_acf_1": -0.13896372199625864,
        "abs_return_acf_1": 0.26673500377924586,
        "abs_return_acf_5": 0.22174613011849578,
        "abs_return_acf_20": 0.24067527182257278,
        "quantile_01": -0.05050732228916565,
        "quantile_99": 0.046496910637642615,
        "hill_tail_index": 2.9452409583142356
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017880708315987745,
        "excess_kurtosis": 10.728301833485165,
        "return_acf_1": -0.14378925542213306,
        "abs_return_acf_1": 0.3887142667361277,
        "abs_return_acf_5": 0.3713185578245526,
        "abs_return_acf_20": 0.3008799836796579,
        "quantile_01": -0.054094363525058094,
        "quantile_99": 0.04811709597949572,
        "hill_tail_index": 2.5321404286891354
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
