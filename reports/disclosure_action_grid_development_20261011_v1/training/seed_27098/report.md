# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27098
Run ID: `29a37e8ae9b215d2e654511e922b80e07f91d3b1ba0106b43a37421776af4f08`
Result fingerprint: `a487b39abdeb127d22902ce203a9f6cf439239ddd4a7282aa1a8e56e07ee4f1b`

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
    "equal_weight_sd": -0.5457976190476158,
    "equal_weight_raw": -8.186964285714236,
    "fixed_start_cap_weight_sd": -0.52357813980547,
    "fixed_start_cap_weight_raw": -7.853672097082054,
    "end_cap_weight_sd": -0.5090422718867365,
    "end_cap_weight_raw": -7.635634078301047
  },
  "full_period_change": {
    "equal_weight_sd": -0.9073214285714238,
    "equal_weight_raw": -13.609821428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8517926587301542,
    "inflation_mean_sd": 0.5025839947089947
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4065833333333365,
    "equal_weight_raw": 6.098750000000048,
    "fixed_start_cap_weight_sd": 0.42880281257548214,
    "fixed_start_cap_weight_raw": 6.432042188632231,
    "end_cap_weight_sd": 0.44333868049421576,
    "end_cap_weight_raw": 6.650080207413235
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5407142857142824,
      "change_raw": -8.110714285714236,
      "decay_adjusted_gain_sd": 0.4116666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5240476190476158,
      "change_raw": -7.860714285714236,
      "decay_adjusted_gain_sd": 0.42833333333333656
    },
    "small": {
      "count": 18,
      "change_sd": -0.5575198412698381,
      "change_raw": -8.362797619047571,
      "decay_adjusted_gain_sd": 0.3948611111111142
    },
    "large_minus_small_sd": 0.01680555555555574,
    "large_minus_small_raw": 0.2520833333333361
  },
  "inflation": {
    "initial_mean_sd": 0.20791666666666664,
    "final_mean_sd": 0.5218333333333333,
    "mean_sd": 0.3891480710519012,
    "mean_absolute_raw_gap": 5.837221065778518,
    "final_absolute_raw_gap": 7.8275,
    "mean_range_fraction": 0.05837221065778518
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.24,
    "initial_wealth_share": 0.2390500846620104,
    "final_wealth_share": 0.26298974531525937
  },
  "pricing_slope": {
    "mean": -0.000978295330837381,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.07565261700989069,
    "real_improvement_cost": 0.06796762776770568,
    "washing_cost": 0.007684989242185021,
    "fine_transfer": 0.008663940797889607,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0843165578077803,
    "resource_cost_fraction_initial_cap": 0.00252175390032969,
    "private_net_outflow_fraction_initial_cap": 0.0028105519269260104,
    "fine_transfer_fraction_initial_cap": 0.00028879802659632025,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00279627769806429,
    "unapplied_final_day_resource_cost": 0.003410449449041895
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 161.23037750836056,
    "beneficial_raw_gain_per_resource_cost": 2418.4556626254084,
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
    "accrued_cost": 3.3858816705357793,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.40969119434530316,
    "accrued_cost_fraction_initial_cap": 0.11286272235119266,
    "mean_contract_rate": 0.04634500663959834,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 1.2684687277427555e-15,
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
      "minimum": -0.19048274977660049,
      "maximum": -0.026980304609392443,
      "mean": -0.09981146128335219,
      "median": -0.10008299672153642,
      "quantile_05": -0.16278611256146727,
      "quantile_95": -0.03163414839483144
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
      "minimum": 0.25167370848649506,
      "maximum": 0.7801469872579626,
      "mean": 0.45024202304523403,
      "median": 0.4049483433060507,
      "quantile_05": 0.2778317397700282,
      "quantile_95": 0.7185016631828229
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
        "daily_volatility": 0.018229283784226676,
        "excess_kurtosis": 9.378490144853144,
        "return_acf_1": -0.07116097821895248,
        "abs_return_acf_1": 0.27887103035143856,
        "abs_return_acf_5": 0.28329096857589053,
        "abs_return_acf_20": 0.2907726590624738,
        "quantile_01": -0.06056615767812477,
        "quantile_99": 0.051715547354734895,
        "hill_tail_index": 2.711460593346021
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01950782640497431,
        "excess_kurtosis": 9.118307991611536,
        "return_acf_1": -0.035498167442113704,
        "abs_return_acf_1": 0.29669316827812797,
        "abs_return_acf_5": 0.3256996577627168,
        "abs_return_acf_20": 0.2940231302282896,
        "quantile_01": -0.057174454515518676,
        "quantile_99": 0.060600372347027635,
        "hill_tail_index": 3.7278275442168924
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018499134423021608,
        "excess_kurtosis": 5.512809004153127,
        "return_acf_1": -0.16725532461685158,
        "abs_return_acf_1": 0.3066568623626856,
        "abs_return_acf_5": 0.35347342924215286,
        "abs_return_acf_20": 0.2724105799548025,
        "quantile_01": -0.05159030300063658,
        "quantile_99": 0.05806083359657919,
        "hill_tail_index": 3.2755712292875074
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02055971425291987,
        "excess_kurtosis": 7.755654619732399,
        "return_acf_1": -0.14324858531186438,
        "abs_return_acf_1": 0.31884576667774017,
        "abs_return_acf_5": 0.3845076095489138,
        "abs_return_acf_20": 0.34173233693205546,
        "quantile_01": -0.06381471408517844,
        "quantile_99": 0.0590050384373333,
        "hill_tail_index": 3.199315644002568
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018234283867296558,
        "excess_kurtosis": 8.772489131615902,
        "return_acf_1": -0.11610989125721469,
        "abs_return_acf_1": 0.28597219751130487,
        "abs_return_acf_5": 0.2186929456705187,
        "abs_return_acf_20": 0.21772299841526233,
        "quantile_01": -0.061478921665229676,
        "quantile_99": 0.04691075256607331,
        "hill_tail_index": 2.7695913375366765
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021093648812784065,
        "excess_kurtosis": 9.319053193616394,
        "return_acf_1": -0.19048274977660049,
        "abs_return_acf_1": 0.3821448116607742,
        "abs_return_acf_5": 0.2869087566465805,
        "abs_return_acf_20": 0.3724229266614184,
        "quantile_01": -0.0780385806629476,
        "quantile_99": 0.05763116720256791,
        "hill_tail_index": 2.8627310506542285
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020807985305269557,
        "excess_kurtosis": 7.611269975648655,
        "return_acf_1": -0.13102223966038334,
        "abs_return_acf_1": 0.3829089369176669,
        "abs_return_acf_5": 0.3779714834716354,
        "abs_return_acf_20": 0.3142918354673574,
        "quantile_01": -0.06642923867627597,
        "quantile_99": 0.06520148662144391,
        "hill_tail_index": 3.602988642970232
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019540207874949863,
        "excess_kurtosis": 11.457552680813121,
        "return_acf_1": -0.09029363925359488,
        "abs_return_acf_1": 0.3798190065713156,
        "abs_return_acf_5": 0.35092276899349195,
        "abs_return_acf_20": 0.30116614178499346,
        "quantile_01": -0.06602531741837578,
        "quantile_99": 0.046873905625105995,
        "hill_tail_index": 3.127995611558752
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018220769219432154,
        "excess_kurtosis": 4.350534597180794,
        "return_acf_1": -0.10035205526964489,
        "abs_return_acf_1": 0.2280319469029164,
        "abs_return_acf_5": 0.2484357410254112,
        "abs_return_acf_20": 0.2818905124310552,
        "quantile_01": -0.056515935085612375,
        "quantile_99": 0.05293836131803283,
        "hill_tail_index": 4.188838215373768
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018923521131820796,
        "excess_kurtosis": 13.037663541737754,
        "return_acf_1": -0.05994478685239843,
        "abs_return_acf_1": 0.25246533372091445,
        "abs_return_acf_5": 0.29226865662140233,
        "abs_return_acf_20": 0.27898939451572125,
        "quantile_01": -0.06009887570505886,
        "quantile_99": 0.04779404946239963,
        "hill_tail_index": 2.4964512795461022
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01685080281701601,
        "excess_kurtosis": 8.344273422634176,
        "return_acf_1": -0.11401699084952736,
        "abs_return_acf_1": 0.3203954930409139,
        "abs_return_acf_5": 0.35304556993831265,
        "abs_return_acf_20": 0.24750312233765445,
        "quantile_01": -0.04708711416860946,
        "quantile_99": 0.04559006905522153,
        "hill_tail_index": 3.513788157090348
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019083334628734554,
        "excess_kurtosis": 5.180625406985406,
        "return_acf_1": -0.10695741499607123,
        "abs_return_acf_1": 0.2289291068909688,
        "abs_return_acf_5": 0.28197075612837064,
        "abs_return_acf_20": 0.24722855949082373,
        "quantile_01": -0.060023298963440545,
        "quantile_99": 0.05307904309269179,
        "hill_tail_index": 3.734492701081485
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018585854702682914,
        "excess_kurtosis": 16.099761291357467,
        "return_acf_1": -0.026980304609392443,
        "abs_return_acf_1": 0.3590016250405865,
        "abs_return_acf_5": 0.4283455570200863,
        "abs_return_acf_20": 0.30642476909614413,
        "quantile_01": -0.047790584839470324,
        "quantile_99": 0.04764322989531017,
        "hill_tail_index": 1.7232126619437647
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02142831546359406,
        "excess_kurtosis": 11.034311956385022,
        "return_acf_1": -0.14490552297385081,
        "abs_return_acf_1": 0.4280437309576348,
        "abs_return_acf_5": 0.38085562255378463,
        "abs_return_acf_20": 0.3315229272870309,
        "quantile_01": -0.07153563150863639,
        "quantile_99": 0.05748679629976685,
        "hill_tail_index": 2.182641201819705
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01863497969998785,
        "excess_kurtosis": 3.3738427805926463,
        "return_acf_1": -0.10857077013184666,
        "abs_return_acf_1": 0.3069764231692776,
        "abs_return_acf_5": 0.3288354823508514,
        "abs_return_acf_20": 0.2653441588960272,
        "quantile_01": -0.057492805854093436,
        "quantile_99": 0.06088040568746219,
        "hill_tail_index": 5.698107312613813
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016922230257357045,
        "excess_kurtosis": 4.426663632566709,
        "return_acf_1": -0.08803330762240819,
        "abs_return_acf_1": 0.17360252552697286,
        "abs_return_acf_5": 0.14249172715257177,
        "abs_return_acf_20": 0.2118067137375313,
        "quantile_01": -0.044075136332455,
        "quantile_99": 0.04511947720331043,
        "hill_tail_index": 3.441274904023503
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01830553125332734,
        "excess_kurtosis": 11.735943749673561,
        "return_acf_1": -0.031145950918353198,
        "abs_return_acf_1": 0.25273205835686374,
        "abs_return_acf_5": 0.34865791535565593,
        "abs_return_acf_20": 0.240289202849404,
        "quantile_01": -0.0533173867513049,
        "quantile_99": 0.043697013344374945,
        "hill_tail_index": 2.983125389781483
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02084744599170398,
        "excess_kurtosis": 21.527347471639256,
        "return_acf_1": -0.032230834199415956,
        "abs_return_acf_1": 0.30378134469188434,
        "abs_return_acf_5": 0.30685940403934975,
        "abs_return_acf_20": 0.24877628485168699,
        "quantile_01": -0.05870516403477714,
        "quantile_99": 0.05355242046290161,
        "hill_tail_index": 2.5882328088451505
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018860037164993217,
        "excess_kurtosis": 7.045236173259731,
        "return_acf_1": -0.08452075378140463,
        "abs_return_acf_1": 0.2568594424405508,
        "abs_return_acf_5": 0.301279860496583,
        "abs_return_acf_20": 0.2691544924988696,
        "quantile_01": -0.05593734447284976,
        "quantile_99": 0.06088677344723144,
        "hill_tail_index": 3.3982103930506535
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01982943689825709,
        "excess_kurtosis": 11.439379898961606,
        "return_acf_1": -0.0794990551017636,
        "abs_return_acf_1": 0.2750194908121308,
        "abs_return_acf_5": 0.28961457833479476,
        "abs_return_acf_20": 0.3666586807347336,
        "quantile_01": -0.06079721195726181,
        "quantile_99": 0.060950803033111546,
        "hill_tail_index": 2.5673303436070576
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020839883419700632,
        "excess_kurtosis": 10.290796720268505,
        "return_acf_1": -0.14552183118434678,
        "abs_return_acf_1": 0.3170958622452221,
        "abs_return_acf_5": 0.31292076843773325,
        "abs_return_acf_20": 0.24776710064344298,
        "quantile_01": -0.07133389123074209,
        "quantile_99": 0.051552499563806316,
        "hill_tail_index": 2.6954477187381904
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01974566252845361,
        "excess_kurtosis": 9.125433771052199,
        "return_acf_1": -0.11543200793084511,
        "abs_return_acf_1": 0.25881662789484045,
        "abs_return_acf_5": 0.3025914911399902,
        "abs_return_acf_20": 0.2519972883499794,
        "quantile_01": -0.06383120141920176,
        "quantile_99": 0.05321104165590304,
        "hill_tail_index": 2.8762280980287964
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020050392425580557,
        "excess_kurtosis": 5.49603495286903,
        "return_acf_1": -0.09586044649411272,
        "abs_return_acf_1": 0.26537769297228214,
        "abs_return_acf_5": 0.31113210536018343,
        "abs_return_acf_20": 0.29446626166590667,
        "quantile_01": -0.05883705929202661,
        "quantile_99": 0.06432280874125192,
        "hill_tail_index": 3.8337412836406033
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019482303231906743,
        "excess_kurtosis": 12.229841565034798,
        "return_acf_1": -0.04178763253222416,
        "abs_return_acf_1": 0.28891224036203067,
        "abs_return_acf_5": 0.30466274647587055,
        "abs_return_acf_20": 0.26586644666783427,
        "quantile_01": -0.06256528235440198,
        "quantile_99": 0.052222911451385925,
        "hill_tail_index": 3.4191127202827643
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021702587542891373,
        "excess_kurtosis": 10.928968036053208,
        "return_acf_1": -0.15732374227155313,
        "abs_return_acf_1": 0.343182262056393,
        "abs_return_acf_5": 0.3800289147396824,
        "abs_return_acf_20": 0.3491014192226906,
        "quantile_01": -0.07862920773034632,
        "quantile_99": 0.056946575504913596,
        "hill_tail_index": 2.9015843262290364
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020332812570841425,
        "excess_kurtosis": 11.956009761807866,
        "return_acf_1": -0.10886165334447158,
        "abs_return_acf_1": 0.3561017849294297,
        "abs_return_acf_5": 0.3888436542258408,
        "abs_return_acf_20": 0.273129301173155,
        "quantile_01": -0.06417444083208966,
        "quantile_99": 0.05634947666250189,
        "hill_tail_index": 2.1240713282077626
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022632050348394515,
        "excess_kurtosis": 11.030211196477458,
        "return_acf_1": -0.15537644358790628,
        "abs_return_acf_1": 0.39892908378079805,
        "abs_return_acf_5": 0.319273176958191,
        "abs_return_acf_20": 0.36012874785280247,
        "quantile_01": -0.07743433030977345,
        "quantile_99": 0.06982549793603797,
        "hill_tail_index": 3.40864530384026
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019688097653825672,
        "excess_kurtosis": 10.342687433908525,
        "return_acf_1": -0.07498541417132808,
        "abs_return_acf_1": 0.28377825305330906,
        "abs_return_acf_5": 0.2774071409438873,
        "abs_return_acf_20": 0.30149779680810673,
        "quantile_01": -0.052951220314260056,
        "quantile_99": 0.04763800323764531,
        "hill_tail_index": 2.354647400716413
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01586716403400093,
        "excess_kurtosis": 5.136479987767565,
        "return_acf_1": -0.09981393817342794,
        "abs_return_acf_1": 0.25598035904847255,
        "abs_return_acf_5": 0.20739786020056636,
        "abs_return_acf_20": 0.13535626705941678,
        "quantile_01": -0.04063131362822238,
        "quantile_99": 0.04387307586789792,
        "hill_tail_index": 2.8575940842116796
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022572633997900073,
        "excess_kurtosis": 13.109776607299796,
        "return_acf_1": -0.07715140596669681,
        "abs_return_acf_1": 0.4844967800291393,
        "abs_return_acf_5": 0.42540789118396155,
        "abs_return_acf_20": 0.3517485347693025,
        "quantile_01": -0.08082691976461971,
        "quantile_99": 0.07995208963009316,
        "hill_tail_index": 3.2589472321012907
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
