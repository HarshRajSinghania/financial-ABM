# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27039
Run ID: `5d73402d07d9145449deb16d274e2d48a5ceac5a50d8bdc8aa6bf9e02229e2b3`
Result fingerprint: `f0cd5415692c0195b5fd8e8674a85e9f36018cb2169430d95e8b7958fd325a50`

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
    "equal_weight_sd": -0.38929761904761584,
    "equal_weight_raw": -5.839464285714238,
    "fixed_start_cap_weight_sd": -0.23200627763273157,
    "fixed_start_cap_weight_raw": -3.480094164490973,
    "end_cap_weight_sd": -0.2570734464968569,
    "end_cap_weight_raw": -3.8561016974528544
  },
  "full_period_change": {
    "equal_weight_sd": -0.7097380952380905,
    "equal_weight_raw": -10.646071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.6649143518518473,
    "inflation_mean_sd": 0.5764371693121693
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5630833333333365,
    "equal_weight_raw": 8.446250000000047,
    "fixed_start_cap_weight_sd": 0.7203746747482205,
    "fixed_start_cap_weight_raw": 10.80562012122331,
    "end_cap_weight_sd": 0.6953075058840956,
    "end_cap_weight_raw": 10.42961258826143
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": 0.13928571428571737,
      "change_raw": 2.0892857142857606,
      "decay_adjusted_gain_sd": 1.0916666666666697
    },
    "mid": {
      "count": 9,
      "change_sd": -0.35821428571428243,
      "change_raw": -5.373214285714236,
      "decay_adjusted_gain_sd": 0.5941666666666698
    },
    "small": {
      "count": 18,
      "change_sd": -0.4929365079365048,
      "change_raw": -7.394047619047572,
      "decay_adjusted_gain_sd": 0.4594444444444476
    },
    "large_minus_small_sd": 0.6322222222222221,
    "large_minus_small_raw": 9.483333333333333
  },
  "inflation": {
    "initial_mean_sd": 0.2353333333333333,
    "final_mean_sd": 0.5703333333333334,
    "mean_sd": 0.43321149042464613,
    "mean_absolute_raw_gap": 6.498172356369691,
    "final_absolute_raw_gap": 8.555000000000001,
    "mean_range_fraction": 0.06498172356369691
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.41333333333333333,
    "initial_wealth_share": 0.1890820741397485,
    "final_wealth_share": 0.37673968208449726
  },
  "pricing_slope": {
    "mean": -0.003308413594696383,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.15650411005592635,
    "real_improvement_cost": 0.1392168481233642,
    "washing_cost": 0.01728726193256215,
    "fine_transfer": 0.022157552255343015,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.17866166231126937,
    "resource_cost_fraction_initial_cap": 0.00521680366853088,
    "private_net_outflow_fraction_initial_cap": 0.0059553887437089805,
    "fine_transfer_fraction_initial_cap": 0.0007385850751781007,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.009301127753751578,
    "unapplied_final_day_resource_cost": 0.013041744033828162
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 107.93646246072133,
    "beneficial_raw_gain_per_resource_cost": 1619.04693691082,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 3.089173150671059,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": -0.1129826744805829,
    "accrued_cost_fraction_initial_cap": 0.10297243835570198,
    "mean_contract_rate": 0.04214728253384485,
    "maximum_ledger_error": 7.792703114739563e-20
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
    "price_cap_hits": 21,
    "maximum_relative_cash_error": 1.438167871236288e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.40062216986903754,
      "maximum": -0.21002713990522476,
      "mean": -0.3019933620327649,
      "median": -0.30473403604199545,
      "quantile_05": -0.37841811010329784,
      "quantile_95": -0.21903727471251266
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
      "minimum": 0.2542502428045288,
      "maximum": 0.8760383263284057,
      "mean": 0.7536189989408119,
      "median": 0.7956897945604379,
      "quantile_05": 0.49073579154805086,
      "quantile_95": 0.8536811358683967
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
        "daily_volatility": 0.02708357206720711,
        "excess_kurtosis": 24.024973319292197,
        "return_acf_1": -0.3244064941551232,
        "abs_return_acf_1": 0.4348700148698249,
        "abs_return_acf_5": 0.3021339686396476,
        "abs_return_acf_20": 0.2408628077210342,
        "quantile_01": -0.116392273441835,
        "quantile_99": 0.06775505694082247,
        "hill_tail_index": 1.866779350219608
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.026861186380974227,
        "excess_kurtosis": 22.285974576704,
        "return_acf_1": -0.29449770651758134,
        "abs_return_acf_1": 0.4472495923953674,
        "abs_return_acf_5": 0.2896652518082714,
        "abs_return_acf_20": 0.22727035350271188,
        "quantile_01": -0.10098454503636074,
        "quantile_99": 0.06313376734932653,
        "hill_tail_index": 1.7295645932419048
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.025436029604034203,
        "excess_kurtosis": 33.58741209654729,
        "return_acf_1": -0.33652289004169916,
        "abs_return_acf_1": 0.4369010772350212,
        "abs_return_acf_5": 0.2981097476910842,
        "abs_return_acf_20": 0.2591613001593299,
        "quantile_01": -0.06478333022511358,
        "quantile_99": 0.056584191109673575,
        "hill_tail_index": 1.6226490800492583
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02484607730581282,
        "excess_kurtosis": 23.135078907784507,
        "return_acf_1": -0.22049841174158571,
        "abs_return_acf_1": 0.5297801025997528,
        "abs_return_acf_5": 0.34831155735875385,
        "abs_return_acf_20": 0.2906737948608259,
        "quantile_01": -0.09733042635108993,
        "quantile_99": 0.07122241428794544,
        "hill_tail_index": 2.574663471612601
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02367330098304095,
        "excess_kurtosis": 23.18982896248305,
        "return_acf_1": -0.2544968801128543,
        "abs_return_acf_1": 0.39669871734086587,
        "abs_return_acf_5": 0.22810933700003694,
        "abs_return_acf_20": 0.21062025649590949,
        "quantile_01": -0.09490342176605895,
        "quantile_99": 0.055097099886391776,
        "hill_tail_index": 1.726709213376652
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02722562789198182,
        "excess_kurtosis": 16.332720259980476,
        "return_acf_1": -0.35328254720123026,
        "abs_return_acf_1": 0.44630397891949,
        "abs_return_acf_5": 0.35022492281154066,
        "abs_return_acf_20": 0.3246472673197914,
        "quantile_01": -0.11367458732335226,
        "quantile_99": 0.07050060892693148,
        "hill_tail_index": 2.204435747586949
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023846116254283824,
        "excess_kurtosis": 25.119468855146238,
        "return_acf_1": -0.2664449743197746,
        "abs_return_acf_1": 0.4162387175131713,
        "abs_return_acf_5": 0.292835323127067,
        "abs_return_acf_20": 0.23047577596570915,
        "quantile_01": -0.07220427061855274,
        "quantile_99": 0.05595931443734109,
        "hill_tail_index": 1.7981852116525314
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.027303700532567927,
        "excess_kurtosis": 22.395124220530445,
        "return_acf_1": -0.27881676399879385,
        "abs_return_acf_1": 0.47682331725391397,
        "abs_return_acf_5": 0.3440096643347496,
        "abs_return_acf_20": 0.2517990655808964,
        "quantile_01": -0.10883992178346008,
        "quantile_99": 0.06252974615666898,
        "hill_tail_index": 1.8653149037116892
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02829199009692325,
        "excess_kurtosis": 21.448381794652192,
        "return_acf_1": -0.3335437004716261,
        "abs_return_acf_1": 0.4488064273681289,
        "abs_return_acf_5": 0.36368742949535576,
        "abs_return_acf_20": 0.2668400818637148,
        "quantile_01": -0.11130516189706274,
        "quantile_99": 0.06767177881262333,
        "hill_tail_index": 1.9042100234868211
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.025730510466996672,
        "excess_kurtosis": 33.838597293779685,
        "return_acf_1": -0.3193920537109504,
        "abs_return_acf_1": 0.4592742359915594,
        "abs_return_acf_5": 0.30788482769547537,
        "abs_return_acf_20": 0.20659998445450745,
        "quantile_01": -0.0737787673871616,
        "quantile_99": 0.0672814325853936,
        "hill_tail_index": 2.047547618162026
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.025414667051602013,
        "excess_kurtosis": 18.80144151422208,
        "return_acf_1": -0.2697932783272596,
        "abs_return_acf_1": 0.45949103763966626,
        "abs_return_acf_5": 0.34899794682156204,
        "abs_return_acf_20": 0.25858614005361685,
        "quantile_01": -0.10037854916556585,
        "quantile_99": 0.06530331062728584,
        "hill_tail_index": 2.489211284000578
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024950502751964157,
        "excess_kurtosis": 25.144501166840605,
        "return_acf_1": -0.2356104788303987,
        "abs_return_acf_1": 0.3819268785654812,
        "abs_return_acf_5": 0.3499331507938323,
        "abs_return_acf_20": 0.12870384239819524,
        "quantile_01": -0.09244067636113151,
        "quantile_99": 0.055266472019410616,
        "hill_tail_index": 1.6960028668893798
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.0265088985120172,
        "excess_kurtosis": 22.919524168923086,
        "return_acf_1": -0.29580346955370546,
        "abs_return_acf_1": 0.42782995384158756,
        "abs_return_acf_5": 0.27841041179431186,
        "abs_return_acf_20": 0.19374510488500862,
        "quantile_01": -0.12195147385471666,
        "quantile_99": 0.07404007707737689,
        "hill_tail_index": 1.871805286480477
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.027022016257840117,
        "excess_kurtosis": 23.35911585688804,
        "return_acf_1": -0.37290968724065904,
        "abs_return_acf_1": 0.4602167560678093,
        "abs_return_acf_5": 0.26701762542645124,
        "abs_return_acf_20": 0.18123678227552023,
        "quantile_01": -0.11548958669314109,
        "quantile_99": 0.07031997851043312,
        "hill_tail_index": 1.7042621248313385
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.025284738464795953,
        "excess_kurtosis": 32.74962116436632,
        "return_acf_1": -0.21784179896145286,
        "abs_return_acf_1": 0.39078223206447343,
        "abs_return_acf_5": 0.3198461228843341,
        "abs_return_acf_20": 0.19023138858067382,
        "quantile_01": -0.06618428209017686,
        "quantile_99": 0.06014783279668267,
        "hill_tail_index": 1.8997625532975309
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02672553489255819,
        "excess_kurtosis": 20.725207425663736,
        "return_acf_1": -0.2444434279846492,
        "abs_return_acf_1": 0.46372217713792124,
        "abs_return_acf_5": 0.3383596966491074,
        "abs_return_acf_20": 0.21018116184407767,
        "quantile_01": -0.11027619466864763,
        "quantile_99": 0.06147627781331715,
        "hill_tail_index": 2.025488788267495
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02694187284839679,
        "excess_kurtosis": 32.49608386835162,
        "return_acf_1": -0.3276200345516829,
        "abs_return_acf_1": 0.4840244010296033,
        "abs_return_acf_5": 0.3720525978014974,
        "abs_return_acf_20": 0.24010694017278167,
        "quantile_01": -0.08254287633885089,
        "quantile_99": 0.05815582343401241,
        "hill_tail_index": 1.6874668120934124
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.028276409376156733,
        "excess_kurtosis": 19.63126424034778,
        "return_acf_1": -0.3461780774306471,
        "abs_return_acf_1": 0.4947693206797331,
        "abs_return_acf_5": 0.3764788201158405,
        "abs_return_acf_20": 0.28231587343588266,
        "quantile_01": -0.11702257368473022,
        "quantile_99": 0.0648515861680923,
        "hill_tail_index": 1.815487236977349
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.026834967916318713,
        "excess_kurtosis": 25.187637063998743,
        "return_acf_1": -0.3787938342824275,
        "abs_return_acf_1": 0.43396119985989684,
        "abs_return_acf_5": 0.28426677566604247,
        "abs_return_acf_20": 0.18425066513132274,
        "quantile_01": -0.10780382176832005,
        "quantile_99": 0.060474441259684965,
        "hill_tail_index": 1.5775590956959642
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.026833205452799918,
        "excess_kurtosis": 23.667899000820597,
        "return_acf_1": -0.32752599928299275,
        "abs_return_acf_1": 0.36354319161481014,
        "abs_return_acf_5": 0.24673081325607626,
        "abs_return_acf_20": 0.1436940193694062,
        "quantile_01": -0.11482996904952725,
        "quantile_99": 0.05512702465082005,
        "hill_tail_index": 1.860419266083342
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0249658665340287,
        "excess_kurtosis": 31.332578831735383,
        "return_acf_1": -0.34053801580644744,
        "abs_return_acf_1": 0.41441410423369046,
        "abs_return_acf_5": 0.2538657296810059,
        "abs_return_acf_20": 0.17423869002196118,
        "quantile_01": -0.08506535437817406,
        "quantile_99": 0.050002613467692726,
        "hill_tail_index": 1.8016986004893192
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02703541270973685,
        "excess_kurtosis": 25.09554375395309,
        "return_acf_1": -0.3779588916621393,
        "abs_return_acf_1": 0.43826534583202553,
        "abs_return_acf_5": 0.29924382328653615,
        "abs_return_acf_20": 0.19151249001335538,
        "quantile_01": -0.10093204024012709,
        "quantile_99": 0.06176966263461305,
        "hill_tail_index": 1.7077592163792723
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02627475935137777,
        "excess_kurtosis": 26.186606128411984,
        "return_acf_1": -0.2756263612537174,
        "abs_return_acf_1": 0.43503808564002744,
        "abs_return_acf_5": 0.33259239080358116,
        "abs_return_acf_20": 0.287793087117717,
        "quantile_01": -0.09939137418178527,
        "quantile_99": 0.060837248255494136,
        "hill_tail_index": 1.8009703187981239
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02753108639705871,
        "excess_kurtosis": 24.589496356872527,
        "return_acf_1": -0.2485172088570469,
        "abs_return_acf_1": 0.4284845251487999,
        "abs_return_acf_5": 0.2850231656176821,
        "abs_return_acf_20": 0.17579047025055033,
        "quantile_01": -0.12307449622655538,
        "quantile_99": 0.06717035628789252,
        "hill_tail_index": 1.6578081519337278
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02660849375587331,
        "excess_kurtosis": 18.111456078839378,
        "return_acf_1": -0.356542385152789,
        "abs_return_acf_1": 0.45752790117591385,
        "abs_return_acf_5": 0.347762321357107,
        "abs_return_acf_20": 0.25665371837735584,
        "quantile_01": -0.1175966540252171,
        "quantile_99": 0.07644000738989677,
        "hill_tail_index": 2.257971912587356
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.024508416329628892,
        "excess_kurtosis": 27.8725758890416,
        "return_acf_1": -0.24244529544390292,
        "abs_return_acf_1": 0.4343941058486453,
        "abs_return_acf_5": 0.3020774632646252,
        "abs_return_acf_20": 0.22581671195614406,
        "quantile_01": -0.08767195924585616,
        "quantile_99": 0.055137803721777984,
        "hill_tail_index": 1.8835530010253803
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025189484017906466,
        "excess_kurtosis": 28.35668585709987,
        "return_acf_1": -0.29543628178526155,
        "abs_return_acf_1": 0.40893966093988005,
        "abs_return_acf_5": 0.3095424661545854,
        "abs_return_acf_20": 0.19905687534012395,
        "quantile_01": -0.09546239291656522,
        "quantile_99": 0.06229553475610917,
        "hill_tail_index": 1.7857175582043918
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.027369475827706827,
        "excess_kurtosis": 34.97680872838597,
        "return_acf_1": -0.40062216986903754,
        "abs_return_acf_1": 0.5373184080948199,
        "abs_return_acf_5": 0.3528853732196188,
        "abs_return_acf_20": 0.21525120106007636,
        "quantile_01": -0.08680515781709683,
        "quantile_99": 0.06403684264972676,
        "hill_tail_index": 1.988181731853594
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02477979797459634,
        "excess_kurtosis": 29.87949967461268,
        "return_acf_1": -0.3136646025302854,
        "abs_return_acf_1": 0.4220277479438585,
        "abs_return_acf_5": 0.25763502920194215,
        "abs_return_acf_20": 0.26035312209023526,
        "quantile_01": -0.07680893860437289,
        "quantile_99": 0.05436003528144548,
        "hill_tail_index": 1.8265467804225615
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.03272256042017382,
        "excess_kurtosis": 35.723785549530724,
        "return_acf_1": -0.21002713990522476,
        "abs_return_acf_1": 0.4336416007901159,
        "abs_return_acf_5": 0.425484026703022,
        "abs_return_acf_20": 0.2590816379059235,
        "quantile_01": -0.0882896268979543,
        "quantile_99": 0.09749143122330223,
        "hill_tail_index": 1.7967839268164647
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
