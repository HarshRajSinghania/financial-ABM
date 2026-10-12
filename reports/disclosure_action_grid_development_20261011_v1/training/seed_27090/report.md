# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27090
Run ID: `0c2bbc7f5ba82ea28f00a3b5acdaa6159031cba2269a7110fa466cae2bbe9624`
Result fingerprint: `2c1add150602e9049e28ed0394f44cd2017a7b35f1dc790a71c6405d7e1d8b2d`

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
    "equal_weight_sd": -0.6577976190476158,
    "equal_weight_raw": -9.866964285714236,
    "fixed_start_cap_weight_sd": -0.6683505822427509,
    "fixed_start_cap_weight_raw": -10.025258733641262,
    "end_cap_weight_sd": -0.6713130589496369,
    "end_cap_weight_raw": -10.069695884244553
  },
  "full_period_change": {
    "equal_weight_sd": -1.007404761904757,
    "equal_weight_raw": -15.111071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9593009259259214,
    "inflation_mean_sd": 0.7450988756613757
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.29023422496624085,
    "equal_weight_raw": 4.353513374493612,
    "fixed_start_cap_weight_sd": 0.2812176155038575,
    "fixed_start_cap_weight_raw": 4.218264232557863,
    "end_cap_weight_sd": 0.2778331109205139,
    "end_cap_weight_raw": 4.167496663807707
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6540476190476161,
      "change_raw": -9.81071428571424,
      "decay_adjusted_gain_sd": 0.29833333333333617
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6776587301587268,
      "change_raw": -10.164880952380901,
      "decay_adjusted_gain_sd": 0.2747222222222255
    },
    "small": {
      "count": 18,
      "change_sd": -0.6484920634920602,
      "change_raw": -9.727380952380903,
      "decay_adjusted_gain_sd": 0.29664037494373247
    },
    "large_minus_small_sd": -0.005555555555555869,
    "large_minus_small_raw": -0.08333333333333803
  },
  "inflation": {
    "initial_mean_sd": 0.25225,
    "final_mean_sd": 0.7747499999999998,
    "mean_sd": 0.5457297391063004,
    "mean_absolute_raw_gap": 8.185946086594504,
    "final_absolute_raw_gap": 11.62125,
    "mean_range_fraction": 0.08185946086594503
  },
  "impact": {
    "initial_share": 0.34,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.3185565902020096,
    "final_wealth_share": 0.36512357521267974
  },
  "pricing_slope": {
    "mean": 0.004081572152382832,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.084532853386687,
    "real_improvement_cost": 0.057288899721049835,
    "washing_cost": 0.027243953665637165,
    "fine_transfer": 0.004987144771496957,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08951999815818397,
    "resource_cost_fraction_initial_cap": 0.002817761779556234,
    "private_net_outflow_fraction_initial_cap": 0.0029839999386061327,
    "fine_transfer_fraction_initial_cap": 0.0001662381590498986,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004232855827622061,
    "unapplied_final_day_resource_cost": 0.006449744559625432
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 103.00168987739961,
    "beneficial_raw_gain_per_resource_cost": 1545.025348160994,
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
    "accrued_cost": 3.1147890649153984,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.13859858872492198,
    "accrued_cost_fraction_initial_cap": 0.10382630216384663,
    "mean_contract_rate": 0.04334405775545828,
    "maximum_ledger_error": 5.759824041329242e-20
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
    "maximum_relative_cash_error": 1.2786363095556493e-15,
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
      "minimum": -0.17676707220742743,
      "maximum": -0.017674593606302216,
      "mean": -0.08603168405504255,
      "median": -0.07294975299616958,
      "quantile_05": -0.14890717828744504,
      "quantile_95": -0.03690305775020394
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
      "minimum": 0.17050951695799166,
      "maximum": 0.8125731895333449,
      "mean": 0.5059329770775612,
      "median": 0.5793616174152306,
      "quantile_05": 0.20756065377973504,
      "quantile_95": 0.7829601201909542
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
        "daily_volatility": 0.018960841200331712,
        "excess_kurtosis": 3.787971550836172,
        "return_acf_1": -0.11167907619541356,
        "abs_return_acf_1": 0.3051620618272692,
        "abs_return_acf_5": 0.33148222462908117,
        "abs_return_acf_20": 0.2206122637736099,
        "quantile_01": -0.053052958650403444,
        "quantile_99": 0.04979722476907012,
        "hill_tail_index": 4.466061509760443
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.023120801649005686,
        "excess_kurtosis": 15.827883245347628,
        "return_acf_1": -0.11737277717714494,
        "abs_return_acf_1": 0.34543104348822823,
        "abs_return_acf_5": 0.4612399767324779,
        "abs_return_acf_20": 0.35625842869501817,
        "quantile_01": -0.08093191501573749,
        "quantile_99": 0.06750637403746165,
        "hill_tail_index": 2.6987891290066557
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022845111803272873,
        "excess_kurtosis": 13.847570510646108,
        "return_acf_1": -0.09864863553845345,
        "abs_return_acf_1": 0.3497206003924365,
        "abs_return_acf_5": 0.43717560765523966,
        "abs_return_acf_20": 0.3446967945676104,
        "quantile_01": -0.07848110973107508,
        "quantile_99": 0.05601448685143564,
        "hill_tail_index": 2.7641237677003607
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02395167650104569,
        "excess_kurtosis": 24.040728171376795,
        "return_acf_1": -0.03790732002703795,
        "abs_return_acf_1": 0.42382041251691016,
        "abs_return_acf_5": 0.48853838145205886,
        "abs_return_acf_20": 0.3688157360684223,
        "quantile_01": -0.09260880232537484,
        "quantile_99": 0.05513320255628038,
        "hill_tail_index": 2.7136541894364226
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02164016119722467,
        "excess_kurtosis": 13.955808737122403,
        "return_acf_1": -0.036081388614612464,
        "abs_return_acf_1": 0.38426758259450766,
        "abs_return_acf_5": 0.51078910523425,
        "abs_return_acf_20": 0.39695035193592215,
        "quantile_01": -0.07749977755529516,
        "quantile_99": 0.05503421495158253,
        "hill_tail_index": 3.3824882783621084
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02308703763573329,
        "excess_kurtosis": 15.783897636946502,
        "return_acf_1": -0.14177269094425923,
        "abs_return_acf_1": 0.3170440088954389,
        "abs_return_acf_5": 0.3721087850621219,
        "abs_return_acf_20": 0.3460020039584987,
        "quantile_01": -0.09069701899755361,
        "quantile_99": 0.05450157203367629,
        "hill_tail_index": 1.8193316419014594
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023887680730029486,
        "excess_kurtosis": 19.294110712017073,
        "return_acf_1": -0.17676707220742743,
        "abs_return_acf_1": 0.4774305274851107,
        "abs_return_acf_5": 0.4914886086115628,
        "abs_return_acf_20": 0.3725040779836784,
        "quantile_01": -0.08663868643932242,
        "quantile_99": 0.058640920403529924,
        "hill_tail_index": 2.270510669859236
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.023310298713121468,
        "excess_kurtosis": 16.38862643951853,
        "return_acf_1": -0.043691694329168,
        "abs_return_acf_1": 0.3922364022350516,
        "abs_return_acf_5": 0.456955380937742,
        "abs_return_acf_20": 0.3174036392618078,
        "quantile_01": -0.08581119843373738,
        "quantile_99": 0.06457833686488622,
        "hill_tail_index": 2.101580463675785
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019603872617782167,
        "excess_kurtosis": 5.000941000374592,
        "return_acf_1": -0.1491214735526164,
        "abs_return_acf_1": 0.3944301703052583,
        "abs_return_acf_5": 0.3776697177544815,
        "abs_return_acf_20": 0.399693996466606,
        "quantile_01": -0.05237811462765808,
        "quantile_99": 0.06450979522829925,
        "hill_tail_index": 3.3543835158500324
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019355683935088613,
        "excess_kurtosis": 4.888388893964616,
        "return_acf_1": -0.11732470048775924,
        "abs_return_acf_1": 0.30844830695477055,
        "abs_return_acf_5": 0.29019649705153416,
        "abs_return_acf_20": 0.24449758130241664,
        "quantile_01": -0.05767901524623606,
        "quantile_99": 0.06291306859981326,
        "hill_tail_index": 4.057135829917757
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019610496858119674,
        "excess_kurtosis": 7.927976855135764,
        "return_acf_1": -0.14766158921914851,
        "abs_return_acf_1": 0.30403827841542314,
        "abs_return_acf_5": 0.41270493129502417,
        "abs_return_acf_20": 0.29315834975051985,
        "quantile_01": -0.058819474003204364,
        "quantile_99": 0.06496744700595075,
        "hill_tail_index": 3.200576850637332
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02186189812289916,
        "excess_kurtosis": 17.957395727202563,
        "return_acf_1": -0.07161308034352284,
        "abs_return_acf_1": 0.28950790467932475,
        "abs_return_acf_5": 0.5089144550752698,
        "abs_return_acf_20": 0.36336872474623605,
        "quantile_01": -0.07038858179171845,
        "quantile_99": 0.0588111629815966,
        "hill_tail_index": 2.8172066042521284
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016220810496542618,
        "excess_kurtosis": 3.314478035997909,
        "return_acf_1": -0.038263609205873614,
        "abs_return_acf_1": 0.257117230672016,
        "abs_return_acf_5": 0.22442035825000314,
        "abs_return_acf_20": 0.21586345500249293,
        "quantile_01": -0.041297177869778025,
        "quantile_99": 0.046239249156347306,
        "hill_tail_index": 2.8104113598658467
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023544035335791105,
        "excess_kurtosis": 23.937439167873716,
        "return_acf_1": -0.06253273957723059,
        "abs_return_acf_1": 0.3942865436176446,
        "abs_return_acf_5": 0.5579348412191758,
        "abs_return_acf_20": 0.3564899707817086,
        "quantile_01": -0.07869051755514525,
        "quantile_99": 0.05314813306218871,
        "hill_tail_index": 2.116171445898473
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02484265664157781,
        "excess_kurtosis": 23.623883350152866,
        "return_acf_1": -0.13361234675005806,
        "abs_return_acf_1": 0.4414820821866988,
        "abs_return_acf_5": 0.5115390362777694,
        "abs_return_acf_20": 0.3712714899155155,
        "quantile_01": -0.08078883402711974,
        "quantile_99": 0.056447220063254054,
        "hill_tail_index": 1.999876970558515
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018007852832651553,
        "excess_kurtosis": 5.057716914418151,
        "return_acf_1": -0.06287120039843574,
        "abs_return_acf_1": 0.3330030501041719,
        "abs_return_acf_5": 0.34344208606440824,
        "abs_return_acf_20": 0.24855329734181353,
        "quantile_01": -0.051310998126507974,
        "quantile_99": 0.05102702944604155,
        "hill_tail_index": 3.699189417604288
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02218611042901743,
        "excess_kurtosis": 14.51578446676675,
        "return_acf_1": -0.05502964669311924,
        "abs_return_acf_1": 0.3635099140579671,
        "abs_return_acf_5": 0.4788148221219321,
        "abs_return_acf_20": 0.2962664763684491,
        "quantile_01": -0.07408696087139854,
        "quantile_99": 0.06613800232408702,
        "hill_tail_index": 2.724694510327638
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022757942361945734,
        "excess_kurtosis": 16.117258386320774,
        "return_acf_1": -0.050114987366192854,
        "abs_return_acf_1": 0.4041764052340826,
        "abs_return_acf_5": 0.4978068542582024,
        "abs_return_acf_20": 0.40544131019963137,
        "quantile_01": -0.08362369592544684,
        "quantile_99": 0.06615775356644105,
        "hill_tail_index": 2.8517664347323843
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022811294872286007,
        "excess_kurtosis": 17.720193061855614,
        "return_acf_1": -0.10522608103482121,
        "abs_return_acf_1": 0.3779478875243153,
        "abs_return_acf_5": 0.4490097532544461,
        "abs_return_acf_20": 0.40201539374027506,
        "quantile_01": -0.07632199602334705,
        "quantile_99": 0.050667327183898894,
        "hill_tail_index": 2.0125619565836153
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021527586806320807,
        "excess_kurtosis": 9.981837405457048,
        "return_acf_1": -0.04954008249023777,
        "abs_return_acf_1": 0.3278165586772804,
        "abs_return_acf_5": 0.4385350552287748,
        "abs_return_acf_20": 0.34339898216841336,
        "quantile_01": -0.07767291609843611,
        "quantile_99": 0.05581010087917349,
        "hill_tail_index": 4.039392833790987
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023062556234059586,
        "excess_kurtosis": 17.667378181353495,
        "return_acf_1": -0.1011975198898698,
        "abs_return_acf_1": 0.4198204562052536,
        "abs_return_acf_5": 0.44501303784635743,
        "abs_return_acf_20": 0.4102294120693766,
        "quantile_01": -0.08976227302535505,
        "quantile_99": 0.050219897332319026,
        "hill_tail_index": 1.834004658360024
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019367161346980168,
        "excess_kurtosis": 8.603460675737702,
        "return_acf_1": -0.14864526185223562,
        "abs_return_acf_1": 0.35034216886055575,
        "abs_return_acf_5": 0.3945662273775898,
        "abs_return_acf_20": 0.31609907490372835,
        "quantile_01": -0.05398585839861912,
        "quantile_99": 0.06397116395132785,
        "hill_tail_index": 2.644978809702504
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022779697098724072,
        "excess_kurtosis": 14.07242456764267,
        "return_acf_1": -0.08888919571537056,
        "abs_return_acf_1": 0.4005379948404928,
        "abs_return_acf_5": 0.4471041106013237,
        "abs_return_acf_20": 0.3448082743442322,
        "quantile_01": -0.08012932852741395,
        "quantile_99": 0.06553154034454697,
        "hill_tail_index": 2.7021556772468323
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02196871622380661,
        "excess_kurtosis": 11.843779698343866,
        "return_acf_1": -0.06364954852762678,
        "abs_return_acf_1": 0.43770833093930994,
        "abs_return_acf_5": 0.4961053196321018,
        "abs_return_acf_20": 0.4277753830751863,
        "quantile_01": -0.06792807677697164,
        "quantile_99": 0.05647796632117032,
        "hill_tail_index": 2.302733745872285
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021857230616164666,
        "excess_kurtosis": 18.549700412195833,
        "return_acf_1": -0.043469880705678435,
        "abs_return_acf_1": 0.324364653349944,
        "abs_return_acf_5": 0.45982544776618467,
        "abs_return_acf_20": 0.36281003040622445,
        "quantile_01": -0.06796779108502833,
        "quantile_99": 0.058048679351937936,
        "hill_tail_index": 2.579765468920258
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018433338506703482,
        "excess_kurtosis": 8.86693376294063,
        "return_acf_1": -0.14684097761412374,
        "abs_return_acf_1": 0.40384240688207446,
        "abs_return_acf_5": 0.3409005759558467,
        "abs_return_acf_20": 0.2373834138230776,
        "quantile_01": -0.05007347750418321,
        "quantile_99": 0.06389616619113611,
        "hill_tail_index": 2.7778694776051194
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02616052110108506,
        "excess_kurtosis": 20.307003264718293,
        "return_acf_1": -0.07428642564881632,
        "abs_return_acf_1": 0.42340473381916066,
        "abs_return_acf_5": 0.5196758917966243,
        "abs_return_acf_20": 0.421304627472107,
        "quantile_01": -0.0900155500438392,
        "quantile_99": 0.06425786262315533,
        "hill_tail_index": 2.3667316200608366
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02290129809396939,
        "excess_kurtosis": 15.944917408620785,
        "return_acf_1": -0.017674593606302216,
        "abs_return_acf_1": 0.3673829590805541,
        "abs_return_acf_5": 0.45685184449216537,
        "abs_return_acf_20": 0.3805042811077244,
        "quantile_01": -0.07580146984477523,
        "quantile_99": 0.058447023401825574,
        "hill_tail_index": 2.5361156823113378
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020088313551449296,
        "excess_kurtosis": 3.579392222537372,
        "return_acf_1": -0.0380535562874646,
        "abs_return_acf_1": 0.23770873119257988,
        "abs_return_acf_5": 0.34398350891368956,
        "abs_return_acf_20": 0.29121076969953574,
        "quantile_01": -0.05586577878238433,
        "quantile_99": 0.057310750644013565,
        "hill_tail_index": 4.090816071732841
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021987743776556705,
        "excess_kurtosis": 11.045884180022524,
        "return_acf_1": -0.0514113696512551,
        "abs_return_acf_1": 0.35107586695298726,
        "abs_return_acf_5": 0.43212198654472617,
        "abs_return_acf_20": 0.3614681295482462,
        "quantile_01": -0.07945298778248758,
        "quantile_99": 0.05523419636031142,
        "hill_tail_index": 2.7300889287845385
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
