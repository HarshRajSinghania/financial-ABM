# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27107
Run ID: `50d9327bf3be889a5fbd56e116e667c19ff86d68630890a1273145941a731e61`
Result fingerprint: `b95795b7542ddbda59d05f07c96ef35527d2c417028ebfe5662a59359cce7d37`

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
    "equal_weight_sd": -0.6302976190476158,
    "equal_weight_raw": -9.45446428571424,
    "fixed_start_cap_weight_sd": -0.6859845788236192,
    "fixed_start_cap_weight_raw": -10.289768682354284,
    "end_cap_weight_sd": -0.6679772160112727,
    "end_cap_weight_raw": -10.019658240169091
  },
  "full_period_change": {
    "equal_weight_sd": -0.9490714285714239,
    "equal_weight_raw": -14.236071428571359
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8856008597883553,
    "inflation_mean_sd": 0.4972589285714286
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.31782441793972555,
    "equal_weight_raw": 4.767366269095884,
    "fixed_start_cap_weight_sd": 0.25789276574635706,
    "fixed_start_cap_weight_raw": 3.868391486195356,
    "end_cap_weight_sd": 0.2725369115854215,
    "end_cap_weight_raw": 4.088053673781322
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7315476190476159,
      "change_raw": -10.973214285714239,
      "decay_adjusted_gain_sd": 0.17824417939722792
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6290476190476159,
      "change_raw": -9.435714285714237,
      "decay_adjusted_gain_sd": 0.3233333333333366
    },
    "small": {
      "count": 18,
      "change_sd": -0.6140476190476158,
      "change_raw": -9.210714285714237,
      "decay_adjusted_gain_sd": 0.33833333333333643
    },
    "large_minus_small_sd": -0.11750000000000005,
    "large_minus_small_raw": -1.7625000000000006
  },
  "inflation": {
    "initial_mean_sd": 0.19175,
    "final_mean_sd": 0.5219166666666667,
    "mean_sd": 0.3669027893422148,
    "mean_absolute_raw_gap": 5.503541840133223,
    "final_absolute_raw_gap": 7.82875,
    "mean_range_fraction": 0.05503541840133223
  },
  "impact": {
    "initial_share": 0.18666666666666668,
    "final_share": 0.3466666666666667,
    "initial_wealth_share": 0.16169579042109944,
    "final_wealth_share": 0.26190311099571856
  },
  "pricing_slope": {
    "mean": -0.0016268588488298232,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.15454559378844085,
    "real_improvement_cost": 0.10037434179173371,
    "washing_cost": 0.054171251996707144,
    "fine_transfer": 0.006356515917523835,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1609021097059647,
    "resource_cost_fraction_initial_cap": 0.005151519792948029,
    "private_net_outflow_fraction_initial_cap": 0.00536340365686549,
    "fine_transfer_fraction_initial_cap": 0.00021188386391746117,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00399494600707907,
    "unapplied_final_day_resource_cost": 0.003351183744983981
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 61.69527260184439,
    "beneficial_raw_gain_per_resource_cost": 925.4290890276658,
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
    "accrued_cost": 2.869192678734901,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.10699779745557539,
    "accrued_cost_fraction_initial_cap": 0.09563975595783004,
    "mean_contract_rate": 0.03972720959439165,
    "maximum_ledger_error": 1.4230153513872246e-19
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
    "maximum_relative_cash_error": 2.698359475205704e-15,
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
      "minimum": -0.24469240930922787,
      "maximum": 0.0009035856372591015,
      "mean": -0.13906887513465177,
      "median": -0.14291119507526426,
      "quantile_05": -0.2264840898985955,
      "quantile_95": -0.06110304013732882
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
      "minimum": 0.3969520994950642,
      "maximum": 0.8075008589636292,
      "mean": 0.6204076978468535,
      "median": 0.6589025046224133,
      "quantile_05": 0.4290906101432853,
      "quantile_95": 0.7677891861433346
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
        "daily_volatility": 0.02042182623152209,
        "excess_kurtosis": 8.477062973934792,
        "return_acf_1": -0.20456880643209593,
        "abs_return_acf_1": 0.4072696799767412,
        "abs_return_acf_5": 0.3408799518630532,
        "abs_return_acf_20": 0.233833134351107,
        "quantile_01": -0.06686276664676397,
        "quantile_99": 0.05050543562231733,
        "hill_tail_index": 2.6515360655834224
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019251025716917468,
        "excess_kurtosis": 9.236585676175972,
        "return_acf_1": -0.17580290711050212,
        "abs_return_acf_1": 0.5065481454158444,
        "abs_return_acf_5": 0.3955580610703083,
        "abs_return_acf_20": 0.27182099908209834,
        "quantile_01": -0.0644317300129398,
        "quantile_99": 0.05462627632143132,
        "hill_tail_index": 3.0894660740081448
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02096196672314013,
        "excess_kurtosis": 15.964117432758538,
        "return_acf_1": -0.11563732600214686,
        "abs_return_acf_1": 0.5048457880178098,
        "abs_return_acf_5": 0.44152595041921117,
        "abs_return_acf_20": 0.31750224238474734,
        "quantile_01": -0.07187651151100366,
        "quantile_99": 0.051022775372512125,
        "hill_tail_index": 2.6840168237469815
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02061720431670431,
        "excess_kurtosis": 11.175049785905152,
        "return_acf_1": -0.21950695706423867,
        "abs_return_acf_1": 0.4930848632336302,
        "abs_return_acf_5": 0.3967536889118981,
        "abs_return_acf_20": 0.2608719933394896,
        "quantile_01": -0.07460292260496673,
        "quantile_99": 0.06412170489681362,
        "hill_tail_index": 3.116296961641075
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020070041354974866,
        "excess_kurtosis": 9.450177177666529,
        "return_acf_1": -0.16745399512182615,
        "abs_return_acf_1": 0.4178851786580251,
        "abs_return_acf_5": 0.4235513436177232,
        "abs_return_acf_20": 0.2712726971252131,
        "quantile_01": -0.0714263398438651,
        "quantile_99": 0.052315464835973394,
        "hill_tail_index": 3.086112359617588
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019959476209162476,
        "excess_kurtosis": 8.026962142278474,
        "return_acf_1": -0.14675318412941862,
        "abs_return_acf_1": 0.38445128117745675,
        "abs_return_acf_5": 0.3733473969583724,
        "abs_return_acf_20": 0.31786892502333325,
        "quantile_01": -0.061615232787064676,
        "quantile_99": 0.05637582390242514,
        "hill_tail_index": 3.197340420502294
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016617521793655905,
        "excess_kurtosis": 4.8959026500834035,
        "return_acf_1": -0.06972635809885201,
        "abs_return_acf_1": 0.25563098976846155,
        "abs_return_acf_5": 0.2755286726594691,
        "abs_return_acf_20": 0.21637468240891236,
        "quantile_01": -0.04607084880708073,
        "quantile_99": 0.04943380481760106,
        "hill_tail_index": 3.5724220372527125
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.016354397848778172,
        "excess_kurtosis": 3.6539856000836437,
        "return_acf_1": -0.1354497139949728,
        "abs_return_acf_1": 0.24545266308758823,
        "abs_return_acf_5": 0.21333264671645444,
        "abs_return_acf_20": 0.18311582184573935,
        "quantile_01": -0.042101758535455204,
        "quantile_99": 0.04728325208308498,
        "hill_tail_index": 3.910651667341277
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01988524263803418,
        "excess_kurtosis": 8.333224166266561,
        "return_acf_1": -0.14789966936492738,
        "abs_return_acf_1": 0.4620974021674443,
        "abs_return_acf_5": 0.40372460428202545,
        "abs_return_acf_20": 0.3095999647708059,
        "quantile_01": -0.07788691469076814,
        "quantile_99": 0.05409661076559808,
        "hill_tail_index": 2.414929339372147
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020768804291185536,
        "excess_kurtosis": 10.882716789481337,
        "return_acf_1": -0.16410887783942854,
        "abs_return_acf_1": 0.4669569139696017,
        "abs_return_acf_5": 0.4415696579760266,
        "abs_return_acf_20": 0.2981109283657779,
        "quantile_01": -0.06798022779500457,
        "quantile_99": 0.058503069545518,
        "hill_tail_index": 3.0186176129897944
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019067096664869467,
        "excess_kurtosis": 7.483044320894132,
        "return_acf_1": -0.10078561722247577,
        "abs_return_acf_1": 0.31155157241278475,
        "abs_return_acf_5": 0.3463552064580601,
        "abs_return_acf_20": 0.21295776373780348,
        "quantile_01": -0.06387838192609209,
        "quantile_99": 0.04775223742677266,
        "hill_tail_index": 3.021776826741369
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017219005058349928,
        "excess_kurtosis": 4.8218445986089815,
        "return_acf_1": -0.10405913793097858,
        "abs_return_acf_1": 0.26860845386697874,
        "abs_return_acf_5": 0.2755700540303785,
        "abs_return_acf_20": 0.268517707986675,
        "quantile_01": -0.049160139002835924,
        "quantile_99": 0.048977044103690304,
        "hill_tail_index": 4.105147839436984
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017128640134644206,
        "excess_kurtosis": 4.004744423350998,
        "return_acf_1": -0.09890214694167791,
        "abs_return_acf_1": 0.3049953539435938,
        "abs_return_acf_5": 0.24284441362699635,
        "abs_return_acf_20": 0.16257795787069898,
        "quantile_01": -0.04312044580078067,
        "quantile_99": 0.051862624652762764,
        "hill_tail_index": 4.2875395919378825
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020429851013479182,
        "excess_kurtosis": 12.86910601867096,
        "return_acf_1": -0.15779679377712982,
        "abs_return_acf_1": 0.46772859711252146,
        "abs_return_acf_5": 0.4399546114212002,
        "abs_return_acf_20": 0.28487539232156495,
        "quantile_01": -0.07504777730480687,
        "quantile_99": 0.0585279792080135,
        "hill_tail_index": 2.5571435634629913
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01849552678861974,
        "excess_kurtosis": 8.981170373162234,
        "return_acf_1": -0.1340272960445031,
        "abs_return_acf_1": 0.35577570018339777,
        "abs_return_acf_5": 0.3556534929515198,
        "abs_return_acf_20": 0.23278822806426205,
        "quantile_01": -0.06682251810438548,
        "quantile_99": 0.04653317616083893,
        "hill_tail_index": 2.6554876978734274
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020775616045487975,
        "excess_kurtosis": 11.481557506144755,
        "return_acf_1": -0.17318680557899088,
        "abs_return_acf_1": 0.4473005712310883,
        "abs_return_acf_5": 0.4562636591578459,
        "abs_return_acf_20": 0.2823545804441219,
        "quantile_01": -0.07140341248225822,
        "quantile_99": 0.056381556488102946,
        "hill_tail_index": 2.5059453706052546
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02002617865651359,
        "excess_kurtosis": 15.800859255473402,
        "return_acf_1": -0.1390692060211099,
        "abs_return_acf_1": 0.41032065604507534,
        "abs_return_acf_5": 0.3799147821049941,
        "abs_return_acf_20": 0.22610249160618517,
        "quantile_01": -0.05915502893900012,
        "quantile_99": 0.04984965584396881,
        "hill_tail_index": 2.437556509927827
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021576511668523334,
        "excess_kurtosis": 12.984758844000522,
        "return_acf_1": -0.15388378169318417,
        "abs_return_acf_1": 0.46880203313964824,
        "abs_return_acf_5": 0.4286426150068841,
        "abs_return_acf_20": 0.2662359965149477,
        "quantile_01": -0.0789694686187366,
        "quantile_99": 0.05458078355497266,
        "hill_tail_index": 2.334185807691162
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021102804626146984,
        "excess_kurtosis": 7.1331989113327054,
        "return_acf_1": -0.24469240930922787,
        "abs_return_acf_1": 0.5395596735258362,
        "abs_return_acf_5": 0.49303409535723836,
        "abs_return_acf_20": 0.3232325457166753,
        "quantile_01": -0.07466310519352766,
        "quantile_99": 0.062470672315772684,
        "hill_tail_index": 3.5254095443104445
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021169409216858674,
        "excess_kurtosis": 9.844865544496614,
        "return_acf_1": -0.23219265312670562,
        "abs_return_acf_1": 0.4431360534354726,
        "abs_return_acf_5": 0.41644946404935895,
        "abs_return_acf_20": 0.3309665393611672,
        "quantile_01": -0.08308556638248223,
        "quantile_99": 0.05528692728078464,
        "hill_tail_index": 2.6343335338599205
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02137328581599311,
        "excess_kurtosis": 26.214696022792783,
        "return_acf_1": -0.16122830588960543,
        "abs_return_acf_1": 0.49411114392326094,
        "abs_return_acf_5": 0.38232327144411715,
        "abs_return_acf_20": 0.20148617433978588,
        "quantile_01": -0.060504668176381754,
        "quantile_99": 0.0453649312308996,
        "hill_tail_index": 2.0882926833830857
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01722944474405139,
        "excess_kurtosis": 5.396116600540452,
        "return_acf_1": -0.09077303461775846,
        "abs_return_acf_1": 0.30113604732261423,
        "abs_return_acf_5": 0.35594909542643033,
        "abs_return_acf_20": 0.1894259939768417,
        "quantile_01": -0.0503608263567128,
        "quantile_99": 0.04273942844545388,
        "hill_tail_index": 3.3521086720451465
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02312312079836918,
        "excess_kurtosis": 16.823487273049796,
        "return_acf_1": -0.16230271422098005,
        "abs_return_acf_1": 0.4808643612177725,
        "abs_return_acf_5": 0.4124482129418268,
        "abs_return_acf_20": 0.3522651396185191,
        "quantile_01": -0.08181371484941365,
        "quantile_99": 0.05785589315692861,
        "hill_tail_index": 2.2380701154815044
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.014951172851042907,
        "excess_kurtosis": 2.906339527650111,
        "return_acf_1": 0.0009035856372591015,
        "abs_return_acf_1": 0.18841452637332748,
        "abs_return_acf_5": 0.2079678312975508,
        "abs_return_acf_20": 0.17941076072226592,
        "quantile_01": -0.040660568228007406,
        "quantile_99": 0.04200334333195117,
        "hill_tail_index": 4.812296255499728
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015964960571301826,
        "excess_kurtosis": 3.3499968496533086,
        "return_acf_1": -0.05404759816880977,
        "abs_return_acf_1": 0.2548974958072226,
        "abs_return_acf_5": 0.27773238839675063,
        "abs_return_acf_20": 0.23256223610758855,
        "quantile_01": -0.04492573250346335,
        "quantile_99": 0.04342441046836022,
        "hill_tail_index": 3.818636720308432
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019668760872238022,
        "excess_kurtosis": 8.866914258554004,
        "return_acf_1": -0.11732929976801476,
        "abs_return_acf_1": 0.440054377490068,
        "abs_return_acf_5": 0.32885003864731277,
        "abs_return_acf_20": 0.2318477886325587,
        "quantile_01": -0.06488323286799394,
        "quantile_99": 0.049143155939079204,
        "hill_tail_index": 2.477974288419461
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.016687121470197252,
        "excess_kurtosis": 6.046098211456407,
        "return_acf_1": -0.07614358201226404,
        "abs_return_acf_1": 0.3440291451134841,
        "abs_return_acf_5": 0.2975289725078082,
        "abs_return_acf_20": 0.18538371396401626,
        "quantile_01": -0.05103902867235235,
        "quantile_99": 0.043405974889924676,
        "hill_tail_index": 4.455081946209311
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01909388467320468,
        "excess_kurtosis": 11.58302773586336,
        "return_acf_1": -0.07289008393057575,
        "abs_return_acf_1": 0.37078585117896484,
        "abs_return_acf_5": 0.3470205894626937,
        "abs_return_acf_20": 0.2394920008056626,
        "quantile_01": -0.06436941375807734,
        "quantile_99": 0.048604335121691454,
        "hill_tail_index": 2.340304630945036
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01934094347810946,
        "excess_kurtosis": 11.575558432384915,
        "return_acf_1": -0.13551210664722782,
        "abs_return_acf_1": 0.3567139376210277,
        "abs_return_acf_5": 0.2961370275834407,
        "abs_return_acf_20": 0.23360052370356305,
        "quantile_01": -0.05851097255431489,
        "quantile_99": 0.05241927819576483,
        "hill_tail_index": 3.521624423978599
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02170860008033891,
        "excess_kurtosis": 13.775353243962574,
        "return_acf_1": -0.21723947161718368,
        "abs_return_acf_1": 0.45950675174061734,
        "abs_return_acf_5": 0.40986132058291147,
        "abs_return_acf_20": 0.3056214742514793,
        "quantile_01": -0.0760010117594371,
        "quantile_99": 0.061442255663614435,
        "hill_tail_index": 2.6547258523565023
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
