# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27132
Run ID: `aaa916ac6fefff303e303fb4ed81a05acab967b8adb9f205e5655d21f784de0b`
Result fingerprint: `49a8151115de1ea1325e52f79e8b7a948750e6a02dfb186ac663355d061c9aa0`

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
    "equal_weight_sd": -0.6661321921624245,
    "equal_weight_raw": -9.991982882436366,
    "fixed_start_cap_weight_sd": -0.6218215789393319,
    "fixed_start_cap_weight_raw": -9.32732368408998,
    "end_cap_weight_sd": -0.6278972991701564,
    "end_cap_weight_raw": -9.418459487552344
  },
  "full_period_change": {
    "equal_weight_sd": -1.017322668352899,
    "equal_weight_raw": -15.259840025293487
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9556763153672607,
    "inflation_mean_sd": 0.7405757275132275
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2557380952380982,
    "equal_weight_raw": 3.8360714285714725,
    "fixed_start_cap_weight_sd": 0.3231239258402733,
    "fixed_start_cap_weight_raw": 4.8468588876041006,
    "end_cap_weight_sd": 0.31744046138880755,
    "end_cap_weight_raw": 4.761606920832112
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5765476190476156,
      "change_raw": -8.648214285714234,
      "decay_adjusted_gain_sd": 0.37583333333333674
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5937698412698382,
      "change_raw": -8.906547619047574,
      "decay_adjusted_gain_sd": 0.3586111111111141
    },
    "small": {
      "count": 18,
      "change_sd": -0.7172441297945189,
      "change_raw": -10.758661946917783,
      "decay_adjusted_gain_sd": 0.18428571428571716
    },
    "large_minus_small_sd": 0.14069651074690326,
    "large_minus_small_raw": 2.110447661203549
  },
  "inflation": {
    "initial_mean_sd": 0.31,
    "final_mean_sd": 0.7169166666666665,
    "mean_sd": 0.611986053288926,
    "mean_absolute_raw_gap": 9.179790799333889,
    "final_absolute_raw_gap": 10.75375,
    "mean_range_fraction": 0.09179790799333888
  },
  "impact": {
    "initial_share": 0.2,
    "final_share": 0.35333333333333333,
    "initial_wealth_share": 0.15201228831838384,
    "final_wealth_share": 0.3274855949089463
  },
  "pricing_slope": {
    "mean": -0.000668350509240151,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.042684553215793654,
    "real_improvement_cost": 0.03416498913930267,
    "washing_cost": 0.008519564076490982,
    "fine_transfer": 0.04019563939852647,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08288019261432011,
    "resource_cost_fraction_initial_cap": 0.0014228184405264551,
    "private_net_outflow_fraction_initial_cap": 0.0027626730871440036,
    "fine_transfer_fraction_initial_cap": 0.001339854646617549,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0014630412284085972,
    "unapplied_final_day_resource_cost": 0.0023573015554431754
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 179.74049812249615,
    "beneficial_raw_gain_per_resource_cost": 2696.107471837442,
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
    "accrued_cost": 3.0714413720819334,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.09525089589145708,
    "accrued_cost_fraction_initial_cap": 0.10238137906939777,
    "mean_contract_rate": 0.04127034451776976,
    "maximum_ledger_error": 1.3552527156068805e-19
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
    "maximum_relative_cash_error": 2.6145576011842743e-15,
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
      "minimum": -0.18533629431199042,
      "maximum": 0.046302520117824986,
      "mean": -0.0840598099674193,
      "median": -0.09430797406920323,
      "quantile_05": -0.1332096269220979,
      "quantile_95": -0.002408498381082617
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
      "minimum": 0.218464114776893,
      "maximum": 0.7874703531430761,
      "mean": 0.5144166884759785,
      "median": 0.524232230165544,
      "quantile_05": 0.3050612067531074,
      "quantile_95": 0.6955257404157572
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
        "daily_volatility": 0.017635346713503478,
        "excess_kurtosis": 25.04111377127867,
        "return_acf_1": -0.1160060682938851,
        "abs_return_acf_1": 0.3373210644828638,
        "abs_return_acf_5": 0.31092819471058386,
        "abs_return_acf_20": 0.20316598869938307,
        "quantile_01": -0.041443314313819736,
        "quantile_99": 0.043913473813245216,
        "hill_tail_index": 2.1510703528648034
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.015574622144985426,
        "excess_kurtosis": 5.700223472173159,
        "return_acf_1": -0.1125712337440451,
        "abs_return_acf_1": 0.37078050322036776,
        "abs_return_acf_5": 0.32540835706212157,
        "abs_return_acf_20": 0.18719237305907044,
        "quantile_01": -0.04304940837922339,
        "quantile_99": 0.04372269051274376,
        "hill_tail_index": 3.5219672298982325
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018896042069602544,
        "excess_kurtosis": 12.301356287875649,
        "return_acf_1": -0.0785720753358775,
        "abs_return_acf_1": 0.2959975923536909,
        "abs_return_acf_5": 0.27882485785895544,
        "abs_return_acf_20": 0.1974115256083782,
        "quantile_01": -0.053809864418203936,
        "quantile_99": 0.0442581716945027,
        "hill_tail_index": 2.3968553866756372
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022244194091556667,
        "excess_kurtosis": 14.240835920038744,
        "return_acf_1": -0.055961567177343116,
        "abs_return_acf_1": 0.39745860188146526,
        "abs_return_acf_5": 0.4747571441356446,
        "abs_return_acf_20": 0.2832756973440847,
        "quantile_01": -0.07668488917208358,
        "quantile_99": 0.06562220124172014,
        "hill_tail_index": 2.887725547370979
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019421114327515112,
        "excess_kurtosis": 14.670165026438763,
        "return_acf_1": -0.09774231387518051,
        "abs_return_acf_1": 0.42609763681819607,
        "abs_return_acf_5": 0.3077698528673417,
        "abs_return_acf_20": 0.41075527792004196,
        "quantile_01": -0.065907622032427,
        "quantile_99": 0.05406677234131819,
        "hill_tail_index": 2.2690444173252335
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.014665910614719783,
        "excess_kurtosis": 2.329539105532267,
        "return_acf_1": -0.11066364867375669,
        "abs_return_acf_1": 0.23975067075709902,
        "abs_return_acf_5": 0.2008149758901166,
        "abs_return_acf_20": 0.19890698893518335,
        "quantile_01": -0.04172397445966016,
        "quantile_99": 0.04033524234856448,
        "hill_tail_index": 3.12413801103196
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016346016029227042,
        "excess_kurtosis": 6.823258972672438,
        "return_acf_1": -0.11414117062815929,
        "abs_return_acf_1": 0.3152611619782498,
        "abs_return_acf_5": 0.2918456019124382,
        "abs_return_acf_20": 0.18387007057256022,
        "quantile_01": -0.04751672854702428,
        "quantile_99": 0.0379080076317266,
        "hill_tail_index": 3.384420249271135
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02012794168182987,
        "excess_kurtosis": 14.692086811085836,
        "return_acf_1": -0.060448660287190856,
        "abs_return_acf_1": 0.38186623954721083,
        "abs_return_acf_5": 0.34015490619135946,
        "abs_return_acf_20": 0.2422989002800571,
        "quantile_01": -0.07203138195772621,
        "quantile_99": 0.05475935155188282,
        "hill_tail_index": 2.7433760254690416
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019739312600975615,
        "excess_kurtosis": 9.848343979497821,
        "return_acf_1": -0.09174301117264004,
        "abs_return_acf_1": 0.4850312739429204,
        "abs_return_acf_5": 0.4618981348631218,
        "abs_return_acf_20": 0.2985696568196397,
        "quantile_01": -0.07218610357627285,
        "quantile_99": 0.04854735260537024,
        "hill_tail_index": 2.421156092072446
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021183971131241906,
        "excess_kurtosis": 14.803446622855486,
        "return_acf_1": -0.12083233145652487,
        "abs_return_acf_1": 0.5508712991908483,
        "abs_return_acf_5": 0.45031796402715696,
        "abs_return_acf_20": 0.2685816100477987,
        "quantile_01": -0.07956143546152704,
        "quantile_99": 0.057392593214513656,
        "hill_tail_index": 2.301684673570667
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01740834347283491,
        "excess_kurtosis": 6.38352368602493,
        "return_acf_1": -0.12221407768486466,
        "abs_return_acf_1": 0.3245756848123421,
        "abs_return_acf_5": 0.3365638667286794,
        "abs_return_acf_20": 0.23761772349923135,
        "quantile_01": -0.049959831840874276,
        "quantile_99": 0.05112401634166385,
        "hill_tail_index": 3.3015058602823415
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01755757480368831,
        "excess_kurtosis": 5.134461195812889,
        "return_acf_1": -0.14220598538892512,
        "abs_return_acf_1": 0.2943125090009723,
        "abs_return_acf_5": 0.21513654323979745,
        "abs_return_acf_20": 0.20163202728303142,
        "quantile_01": -0.04780706298424338,
        "quantile_99": 0.04845854962356346,
        "hill_tail_index": 3.566820649843352
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019028267392619192,
        "excess_kurtosis": 8.99769672777255,
        "return_acf_1": -0.06217092084800971,
        "abs_return_acf_1": 0.4200115367685186,
        "abs_return_acf_5": 0.3352145273993022,
        "abs_return_acf_20": 0.2575125000381104,
        "quantile_01": -0.05798280485212857,
        "quantile_99": 0.0508820187588771,
        "hill_tail_index": 3.254525277340207
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023710003773643424,
        "excess_kurtosis": 24.95453637001904,
        "return_acf_1": 0.008694880345952635,
        "abs_return_acf_1": 0.35968125264778594,
        "abs_return_acf_5": 0.4064444333499106,
        "abs_return_acf_20": 0.28585945319079575,
        "quantile_01": -0.0814932640918518,
        "quantile_99": 0.0662252307426028,
        "hill_tail_index": 2.5026204053937424
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017875939025731282,
        "excess_kurtosis": 9.841571021245162,
        "return_acf_1": -0.09687293696576642,
        "abs_return_acf_1": 0.3419551316761068,
        "abs_return_acf_5": 0.28232314501158906,
        "abs_return_acf_20": 0.23851127816108297,
        "quantile_01": -0.054677628479254295,
        "quantile_99": 0.05029316737560044,
        "hill_tail_index": 3.706492924696201
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018746049095077655,
        "excess_kurtosis": 17.66598935236161,
        "return_acf_1": -0.10432879040700552,
        "abs_return_acf_1": 0.5012372977166041,
        "abs_return_acf_5": 0.4219952465406748,
        "abs_return_acf_20": 0.3093641261030756,
        "quantile_01": -0.06014998472647743,
        "quantile_99": 0.04368278145934445,
        "hill_tail_index": 1.7576775588649214
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020510345543503446,
        "excess_kurtosis": 24.05170928454558,
        "return_acf_1": -0.037706653538920165,
        "abs_return_acf_1": 0.4440459308051302,
        "abs_return_acf_5": 0.35194881133953304,
        "abs_return_acf_20": 0.3135740641084171,
        "quantile_01": -0.06069795401070169,
        "quantile_99": 0.0491121781755311,
        "hill_tail_index": 1.7075269205608512
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02055429497577038,
        "excess_kurtosis": 17.68140539909019,
        "return_acf_1": -0.08675491245656666,
        "abs_return_acf_1": 0.4585421307949491,
        "abs_return_acf_5": 0.47960542512425497,
        "abs_return_acf_20": 0.25885205605164563,
        "quantile_01": -0.07092220847819504,
        "quantile_99": 0.056621996651724134,
        "hill_tail_index": 3.0115631366433595
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017922902821204238,
        "excess_kurtosis": 18.242116889283192,
        "return_acf_1": -0.10812827259830347,
        "abs_return_acf_1": 0.300477137487954,
        "abs_return_acf_5": 0.31057645130587247,
        "abs_return_acf_20": 0.24232370966572092,
        "quantile_01": -0.05053331291813244,
        "quantile_99": 0.04576748455552346,
        "hill_tail_index": 2.370463985297287
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020788094147061714,
        "excess_kurtosis": 11.501471291988905,
        "return_acf_1": -0.037897756987851854,
        "abs_return_acf_1": 0.37820431697481205,
        "abs_return_acf_5": 0.41045161835557653,
        "abs_return_acf_20": 0.31384193024483015,
        "quantile_01": -0.07506972529022851,
        "quantile_99": 0.04937671556691488,
        "hill_tail_index": 2.6522965120576987
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0169342238373581,
        "excess_kurtosis": 10.38052967128481,
        "return_acf_1": -0.05239084021423148,
        "abs_return_acf_1": 0.433101233268696,
        "abs_return_acf_5": 0.4180719281128153,
        "abs_return_acf_20": 0.3520659877948085,
        "quantile_01": -0.05475634604252732,
        "quantile_99": 0.03985147025261427,
        "hill_tail_index": 2.4520837429646574
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019839504653979004,
        "excess_kurtosis": 23.414803933210813,
        "return_acf_1": -0.12083325062514694,
        "abs_return_acf_1": 0.5256289975349677,
        "abs_return_acf_5": 0.4338450942575407,
        "abs_return_acf_20": 0.26874612587535407,
        "quantile_01": -0.0652821022086345,
        "quantile_99": 0.0433668202467087,
        "hill_tail_index": 1.7515951009615853
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018601648518278804,
        "excess_kurtosis": 9.09441157961774,
        "return_acf_1": -0.0914585669163677,
        "abs_return_acf_1": 0.39460411521726685,
        "abs_return_acf_5": 0.3063828511679479,
        "abs_return_acf_20": 0.2626551245974838,
        "quantile_01": -0.06709418039944962,
        "quantile_99": 0.052116163756738276,
        "hill_tail_index": 2.7374402828110322
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01852144626805652,
        "excess_kurtosis": 14.734823294969402,
        "return_acf_1": -0.015979294603014435,
        "abs_return_acf_1": 0.45744048619642297,
        "abs_return_acf_5": 0.40376723576392054,
        "abs_return_acf_20": 0.319916209076539,
        "quantile_01": -0.07118043214790118,
        "quantile_99": 0.05299380774822502,
        "hill_tail_index": 2.3936414630714746
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01633502979583042,
        "excess_kurtosis": 6.123758460855942,
        "return_acf_1": -0.18533629431199042,
        "abs_return_acf_1": 0.31439136297963477,
        "abs_return_acf_5": 0.25145250316338763,
        "abs_return_acf_20": 0.19505962128940982,
        "quantile_01": -0.05064896038223064,
        "quantile_99": 0.045027768326380266,
        "hill_tail_index": 3.264617456877623
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02027035538997089,
        "excess_kurtosis": 37.2069791874988,
        "return_acf_1": -0.10665444311398387,
        "abs_return_acf_1": 0.4731044650896694,
        "abs_return_acf_5": 0.38163927478559906,
        "abs_return_acf_20": 0.2071088339625401,
        "quantile_01": -0.05116486057431517,
        "quantile_99": 0.04047302317361177,
        "hill_tail_index": 1.6070621575385289
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01838752651220791,
        "excess_kurtosis": 14.36144302334452,
        "return_acf_1": -0.04634565935984886,
        "abs_return_acf_1": 0.44804396800084917,
        "abs_return_acf_5": 0.35921148166428324,
        "abs_return_acf_20": 0.2771863585314623,
        "quantile_01": -0.06177938012897698,
        "quantile_99": 0.038094432579082044,
        "hill_tail_index": 1.9780946509349606
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017207183360484216,
        "excess_kurtosis": 9.212553066332848,
        "return_acf_1": -0.1159938316869927,
        "abs_return_acf_1": 0.2982236817477128,
        "abs_return_acf_5": 0.3343920488425484,
        "abs_return_acf_20": 0.25851478536772515,
        "quantile_01": -0.05307965124344652,
        "quantile_99": 0.04261779038373763,
        "hill_tail_index": 2.6962220789451927
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019203352653069314,
        "excess_kurtosis": 9.008669379474673,
        "return_acf_1": 0.046302520117824986,
        "abs_return_acf_1": 0.4165277948685489,
        "abs_return_acf_5": 0.34829924304295234,
        "abs_return_acf_20": 0.2621026770506495,
        "quantile_01": -0.06380761283949465,
        "quantile_99": 0.04911754098115415,
        "hill_tail_index": 2.366772454512842
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017126886903784274,
        "excess_kurtosis": 7.64912104926379,
        "return_acf_1": -0.08483713113396407,
        "abs_return_acf_1": 0.2980620073214296,
        "abs_return_acf_5": 0.3162177301889527,
        "abs_return_acf_20": 0.255905599505486,
        "quantile_01": -0.05247272075665986,
        "quantile_99": 0.04430418736603811,
        "hill_tail_index": 2.8700157560252215
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
