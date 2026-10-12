# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27005
Run ID: `f17529556e2690990e8578d6ee686e1b41e39d796d1c248fdb13eb5a73daacbe`
Result fingerprint: `0802605ff2385fae4b664890fd92b368782bcabf3a15a3d3d7f255fecc2859d8`

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
    "equal_weight_sd": -0.5083793125941554,
    "equal_weight_raw": -7.625689688912331,
    "fixed_start_cap_weight_sd": -0.5083515635771088,
    "fixed_start_cap_weight_raw": -7.62527345365663,
    "end_cap_weight_sd": -0.5003888532865313,
    "end_cap_weight_raw": -7.505832799297969
  },
  "full_period_change": {
    "equal_weight_sd": -0.7986531221179634,
    "equal_weight_raw": -11.97979683176945
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7341150728579845,
    "inflation_mean_sd": 0.5966921296296297
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4356666666666697,
    "equal_weight_raw": 6.535000000000045,
    "fixed_start_cap_weight_sd": 0.4419487302134151,
    "fixed_start_cap_weight_raw": 6.629230953201226,
    "end_cap_weight_sd": 0.4501365242310665,
    "end_cap_weight_raw": 6.752047863465997
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5940476190476158,
      "change_raw": -8.910714285714237,
      "decay_adjusted_gain_sd": 0.3583333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5171031746031715,
      "change_raw": -7.756547619047572,
      "decay_adjusted_gain_sd": 0.43527777777778076
    },
    "small": {
      "count": 18,
      "change_sd": -0.4897393305140707,
      "change_raw": -7.346089957711061,
      "decay_adjusted_gain_sd": 0.448750000000003
    },
    "large_minus_small_sd": -0.10430828853354512,
    "large_minus_small_raw": -1.5646243280031769
  },
  "inflation": {
    "initial_mean_sd": 0.22966666666666669,
    "final_mean_sd": 0.6240833333333333,
    "mean_sd": 0.4267283513738551,
    "mean_absolute_raw_gap": 6.400925270607828,
    "final_absolute_raw_gap": 9.36125,
    "mean_range_fraction": 0.06400925270607828
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.38,
    "initial_wealth_share": 0.225116655282186,
    "final_wealth_share": 0.3660764434057862
  },
  "pricing_slope": {
    "mean": -0.0020643094312555307,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.17235278141917698,
    "real_improvement_cost": 0.15303636037612123,
    "washing_cost": 0.019316421043055722,
    "fine_transfer": 0.021993497229319914,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1943462786484969,
    "resource_cost_fraction_initial_cap": 0.005745092713972566,
    "private_net_outflow_fraction_initial_cap": 0.00647820928828323,
    "fine_transfer_fraction_initial_cap": 0.0007331165743106638,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005024632231406066,
    "unapplied_final_day_resource_cost": 0.007204428695613073
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 75.83283479604958,
    "beneficial_raw_gain_per_resource_cost": 1137.4925219407437,
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
    "accrued_cost": 3.1166485044798806,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.1404580282894043,
    "accrued_cost_fraction_initial_cap": 0.10388828348266269,
    "mean_contract_rate": 0.04390256373015787,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 2.406777163323203e-15,
    "maximum_absolute_share_error": 1.4432899320127035e-15,
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
      "minimum": -0.24408601880787353,
      "maximum": -0.08592336049269467,
      "mean": -0.17951614864320561,
      "median": -0.18920268065869003,
      "quantile_05": -0.2380400781413472,
      "quantile_95": -0.10437972030970945
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
      "minimum": 0.3154648964768674,
      "maximum": 0.7941177978686755,
      "mean": 0.5842719098843995,
      "median": 0.6360353948316896,
      "quantile_05": 0.37606023192286453,
      "quantile_95": 0.7482028247165046
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
        "daily_volatility": 0.019641173664860182,
        "excess_kurtosis": 5.611080464471863,
        "return_acf_1": -0.17356204035996792,
        "abs_return_acf_1": 0.3730487295735964,
        "abs_return_acf_5": 0.41249206112049347,
        "abs_return_acf_20": 0.29437004591344257,
        "quantile_01": -0.06676732991525729,
        "quantile_99": 0.05603349983848317,
        "hill_tail_index": 4.324312280891802
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.015887845717977064,
        "excess_kurtosis": 3.626201077180614,
        "return_acf_1": -0.12307953088139004,
        "abs_return_acf_1": 0.2623811977742024,
        "abs_return_acf_5": 0.16910029482412667,
        "abs_return_acf_20": 0.25197297893008846,
        "quantile_01": -0.0468454293400251,
        "quantile_99": 0.0382544921500484,
        "hill_tail_index": 3.7539104041366342
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017023966467183013,
        "excess_kurtosis": 8.67096416795996,
        "return_acf_1": -0.14584788634606558,
        "abs_return_acf_1": 0.3471063019077266,
        "abs_return_acf_5": 0.3462168013559914,
        "abs_return_acf_20": 0.30742714980326213,
        "quantile_01": -0.052086205473966946,
        "quantile_99": 0.043733891397127765,
        "hill_tail_index": 2.6438393407690857
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.015602870792084235,
        "excess_kurtosis": 3.2588651011821703,
        "return_acf_1": -0.11103676282689348,
        "abs_return_acf_1": 0.25171166308791215,
        "abs_return_acf_5": 0.16337298728487415,
        "abs_return_acf_20": 0.2237106075690142,
        "quantile_01": -0.04192364485561958,
        "quantile_99": 0.042362480955182635,
        "hill_tail_index": 4.112821502520113
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019526198403721377,
        "excess_kurtosis": 9.900416420678205,
        "return_acf_1": -0.20195543877483166,
        "abs_return_acf_1": 0.4145440262132987,
        "abs_return_acf_5": 0.41187319544676965,
        "abs_return_acf_20": 0.3499137750376388,
        "quantile_01": -0.05578306761758436,
        "quantile_99": 0.05740878965331895,
        "hill_tail_index": 2.907754733735762
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01942691760630922,
        "excess_kurtosis": 7.068062109444455,
        "return_acf_1": -0.22587513649208862,
        "abs_return_acf_1": 0.27468663220831807,
        "abs_return_acf_5": 0.3826711493670476,
        "abs_return_acf_20": 0.29089324341180817,
        "quantile_01": -0.05971400614374664,
        "quantile_99": 0.05380530796519474,
        "hill_tail_index": 3.159889796765735
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020392024341049534,
        "excess_kurtosis": 12.324422121511894,
        "return_acf_1": -0.20246314830106985,
        "abs_return_acf_1": 0.4224185218828185,
        "abs_return_acf_5": 0.47669219866909474,
        "abs_return_acf_20": 0.33391878362490535,
        "quantile_01": -0.06429004019270719,
        "quantile_99": 0.061341573227643935,
        "hill_tail_index": 3.2821131952252203
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01906179966046385,
        "excess_kurtosis": 5.914277601307232,
        "return_acf_1": -0.20189754246111,
        "abs_return_acf_1": 0.35635574401517844,
        "abs_return_acf_5": 0.31665499018647514,
        "abs_return_acf_20": 0.28216683926568287,
        "quantile_01": -0.06949965190085516,
        "quantile_99": 0.04936793708320718,
        "hill_tail_index": 3.1665728979114207
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021493141714778688,
        "excess_kurtosis": 11.674706567299017,
        "return_acf_1": -0.16329861593205522,
        "abs_return_acf_1": 0.3959240091739247,
        "abs_return_acf_5": 0.46102378630722995,
        "abs_return_acf_20": 0.3626961900325044,
        "quantile_01": -0.07066612775975863,
        "quantile_99": 0.05486730466548262,
        "hill_tail_index": 2.3370062970882786
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017347906580212548,
        "excess_kurtosis": 4.504259040567563,
        "return_acf_1": -0.09893304915928608,
        "abs_return_acf_1": 0.2688923033214004,
        "abs_return_acf_5": 0.2391827027925901,
        "abs_return_acf_20": 0.23450260241710347,
        "quantile_01": -0.04841731594806615,
        "quantile_99": 0.04318084142254027,
        "hill_tail_index": 3.30980993718411
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018382241817083537,
        "excess_kurtosis": 5.671251219685425,
        "return_acf_1": -0.19580657146129155,
        "abs_return_acf_1": 0.3453339124715909,
        "abs_return_acf_5": 0.31524641268197867,
        "abs_return_acf_20": 0.325998785708289,
        "quantile_01": -0.05966909622347911,
        "quantile_99": 0.04874162375520938,
        "hill_tail_index": 3.711455689543902
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018527233019272376,
        "excess_kurtosis": 7.547223056408024,
        "return_acf_1": -0.20364481971545376,
        "abs_return_acf_1": 0.3971528935570126,
        "abs_return_acf_5": 0.4099026962380663,
        "abs_return_acf_20": 0.29331512366139373,
        "quantile_01": -0.05778950136629891,
        "quantile_99": 0.045029372755606784,
        "hill_tail_index": 2.7416994197750544
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018838167949033365,
        "excess_kurtosis": 6.650972833883692,
        "return_acf_1": -0.19551006841733018,
        "abs_return_acf_1": 0.32206146942355846,
        "abs_return_acf_5": 0.33561637568593017,
        "abs_return_acf_20": 0.296196472252502,
        "quantile_01": -0.06377923902088052,
        "quantile_99": 0.046742905112704014,
        "hill_tail_index": 2.796141771937745
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019303941109552473,
        "excess_kurtosis": 4.876530080924555,
        "return_acf_1": -0.1823933222777081,
        "abs_return_acf_1": 0.367033217715181,
        "abs_return_acf_5": 0.3502411127114125,
        "abs_return_acf_20": 0.2782215600050101,
        "quantile_01": -0.0597358812862455,
        "quantile_99": 0.05621361871710711,
        "hill_tail_index": 3.5678344081575952
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01881438079895631,
        "excess_kurtosis": 5.531825033163175,
        "return_acf_1": -0.22408541683028171,
        "abs_return_acf_1": 0.3509872224934629,
        "abs_return_acf_5": 0.37838346714486065,
        "abs_return_acf_20": 0.28161595445911974,
        "quantile_01": -0.06170611897996824,
        "quantile_99": 0.05481197698934563,
        "hill_tail_index": 3.5866882979179815
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017757167261976584,
        "excess_kurtosis": 3.3122079582308643,
        "return_acf_1": -0.19417104483795902,
        "abs_return_acf_1": 0.3315571198617957,
        "abs_return_acf_5": 0.3731786632165472,
        "abs_return_acf_20": 0.25159773318538164,
        "quantile_01": -0.05534553001302196,
        "quantile_99": 0.04994127343336288,
        "hill_tail_index": 4.272501173484691
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017273293036051265,
        "excess_kurtosis": 3.108233070434985,
        "return_acf_1": -0.18380709507980547,
        "abs_return_acf_1": 0.22845821098307645,
        "abs_return_acf_5": 0.3033080994536398,
        "abs_return_acf_20": 0.199247952173279,
        "quantile_01": -0.0519787097179332,
        "quantile_99": 0.0493725115254123,
        "hill_tail_index": 4.523379008485475
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018099987760594783,
        "excess_kurtosis": 6.470020006105253,
        "return_acf_1": -0.18737721278473374,
        "abs_return_acf_1": 0.29597232922745625,
        "abs_return_acf_5": 0.32771789801431633,
        "abs_return_acf_20": 0.3097597115092584,
        "quantile_01": -0.05459174238266645,
        "quantile_99": 0.047925383756092635,
        "hill_tail_index": 3.0257430274800385
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016140671711647823,
        "excess_kurtosis": 6.311211085376641,
        "return_acf_1": -0.08592336049269467,
        "abs_return_acf_1": 0.3151912719362205,
        "abs_return_acf_5": 0.1881925982253638,
        "abs_return_acf_20": 0.22895855834787035,
        "quantile_01": -0.047664323316797,
        "quantile_99": 0.038464454686305896,
        "hill_tail_index": 2.5032682035798226
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019706024663359863,
        "excess_kurtosis": 7.926916272683323,
        "return_acf_1": -0.21605751703526133,
        "abs_return_acf_1": 0.3452707922363267,
        "abs_return_acf_5": 0.40389050016261613,
        "abs_return_acf_20": 0.37635243446402544,
        "quantile_01": -0.06778999064378664,
        "quantile_99": 0.05557757054357337,
        "hill_tail_index": 3.1394198264370465
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01969298874248519,
        "excess_kurtosis": 14.420430394446353,
        "return_acf_1": -0.16243699552413463,
        "abs_return_acf_1": 0.4130350454171783,
        "abs_return_acf_5": 0.39486030532945493,
        "abs_return_acf_20": 0.3145684755148262,
        "quantile_01": -0.06620357066971616,
        "quantile_99": 0.051158358689311324,
        "hill_tail_index": 2.6736018224794376
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.015267634829535966,
        "excess_kurtosis": 7.767486021858405,
        "return_acf_1": -0.14159312537198981,
        "abs_return_acf_1": 0.26289524136584874,
        "abs_return_acf_5": 0.27919216130758684,
        "abs_return_acf_20": 0.20067929509270555,
        "quantile_01": -0.03996268590360665,
        "quantile_99": 0.039827377758872524,
        "hill_tail_index": 2.852288504229719
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02029338591212259,
        "excess_kurtosis": 9.166476770661363,
        "return_acf_1": -0.21100912357223853,
        "abs_return_acf_1": 0.4544644813076481,
        "abs_return_acf_5": 0.4776847756383375,
        "abs_return_acf_20": 0.31666342740961195,
        "quantile_01": -0.06580064441850328,
        "quantile_99": 0.053880097130009075,
        "hill_tail_index": 2.8551931400514254
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020781921790707616,
        "excess_kurtosis": 11.169018772466853,
        "return_acf_1": -0.11310815668173245,
        "abs_return_acf_1": 0.3862716091849223,
        "abs_return_acf_5": 0.3843270052707548,
        "abs_return_acf_20": 0.2737036074415444,
        "quantile_01": -0.07044524424040324,
        "quantile_99": 0.056553182300868615,
        "hill_tail_index": 2.561035928523663
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015847314318148484,
        "excess_kurtosis": 8.455505783742318,
        "return_acf_1": -0.1568601667385891,
        "abs_return_acf_1": 0.3207791233035378,
        "abs_return_acf_5": 0.27267234081366487,
        "abs_return_acf_20": 0.25524286405332025,
        "quantile_01": -0.03986085634542882,
        "quantile_99": 0.0411734730030314,
        "hill_tail_index": 2.61632078881232
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021329176938845524,
        "excess_kurtosis": 11.270390599067413,
        "return_acf_1": -0.24408601880787353,
        "abs_return_acf_1": 0.43076993496535027,
        "abs_return_acf_5": 0.4514820318421252,
        "abs_return_acf_20": 0.3754084610006814,
        "quantile_01": -0.0648942187638196,
        "quantile_99": 0.057795579319807625,
        "hill_tail_index": 2.5272004167909023
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017602783013024387,
        "excess_kurtosis": 4.302319623721334,
        "return_acf_1": -0.19102814853264632,
        "abs_return_acf_1": 0.3182399477441317,
        "abs_return_acf_5": 0.32618759192000507,
        "abs_return_acf_20": 0.31460213445039403,
        "quantile_01": -0.056537548519562636,
        "quantile_99": 0.049469547344931926,
        "hill_tail_index": 4.267467973562861
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01736825445391303,
        "excess_kurtosis": 4.046940044198919,
        "return_acf_1": -0.17263713469545733,
        "abs_return_acf_1": 0.28354409525463936,
        "abs_return_acf_5": 0.3070912080403656,
        "abs_return_acf_20": 0.24395958576757854,
        "quantile_01": -0.05441007234342926,
        "quantile_99": 0.045825749409933565,
        "hill_tail_index": 4.195027114794744
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01937736166085075,
        "excess_kurtosis": 5.427736821463817,
        "return_acf_1": -0.23759926755978047,
        "abs_return_acf_1": 0.3502285531266707,
        "abs_return_acf_5": 0.37859786524270983,
        "abs_return_acf_20": 0.30395405192381614,
        "quantile_01": -0.05885435811361589,
        "quantile_99": 0.05644035102063679,
        "hill_tail_index": 4.04603186150603
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018580586309404016,
        "excess_kurtosis": 5.5770140108324,
        "return_acf_1": -0.23840074134444725,
        "abs_return_acf_1": 0.3720657441846453,
        "abs_return_acf_5": 0.36488382378189255,
        "abs_return_acf_20": 0.24504100454844524,
        "quantile_01": -0.05022995870794979,
        "quantile_99": 0.04790043696995002,
        "hill_tail_index": 3.1387010812808662
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
Unseen state share: 0.0011111111111111111
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
