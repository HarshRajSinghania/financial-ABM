# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27219
Run ID: `a4f957bc93f2dc67648bb84ea3aaea5e6676ddd99fedf276d5dacc5c3478b647`
Result fingerprint: `da1aee7889051cc06f0945744c8e58d9a5943a7b970873557def61216ccb1687`

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
    "equal_weight_sd": -0.838797619047616,
    "equal_weight_raw": -12.581964285714236,
    "fixed_start_cap_weight_sd": -0.8409126040919702,
    "fixed_start_cap_weight_raw": -12.613689061379551,
    "end_cap_weight_sd": -0.833611453470469,
    "end_cap_weight_raw": -12.50417180205703
  },
  "full_period_change": {
    "equal_weight_sd": -1.2337380952380907,
    "equal_weight_raw": -18.50607142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.14500694444444,
    "inflation_mean_sd": 0.8371342592592591
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11358333333333649,
    "equal_weight_raw": 1.7037500000000478,
    "fixed_start_cap_weight_sd": 0.11146834828898224,
    "fixed_start_cap_weight_raw": 1.672025224334733,
    "end_cap_weight_sd": 0.11876949891048325,
    "end_cap_weight_raw": 1.781542483657249
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8573809523809491,
      "change_raw": -12.860714285714238,
      "decay_adjusted_gain_sd": 0.09500000000000318
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8115476190476159,
      "change_raw": -12.173214285714238,
      "decay_adjusted_gain_sd": 0.14083333333333653
    },
    "small": {
      "count": 18,
      "change_sd": -0.8493253968253937,
      "change_raw": -12.739880952380904,
      "decay_adjusted_gain_sd": 0.10305555555555873
    },
    "large_minus_small_sd": -0.008055555555555483,
    "large_minus_small_raw": -0.12083333333333224
  },
  "inflation": {
    "initial_mean_sd": 0.4168333333333333,
    "final_mean_sd": 0.8230000000000001,
    "mean_sd": 0.700489592006661,
    "mean_absolute_raw_gap": 10.507343880099915,
    "final_absolute_raw_gap": 12.344999999999997,
    "mean_range_fraction": 0.10507343880099915
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.21333333333333335,
    "initial_wealth_share": 0.3172336889999122,
    "final_wealth_share": 0.2946531971192978
  },
  "pricing_slope": {
    "mean": -0.001032169215753848,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.11540711500154155,
    "real_improvement_cost": 0.10526907862946022,
    "washing_cost": 0.01013803637208132,
    "fine_transfer": 0.016217520981246597,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.13162463598278815,
    "resource_cost_fraction_initial_cap": 0.003846903833384719,
    "private_net_outflow_fraction_initial_cap": 0.0043874878660929385,
    "fine_transfer_fraction_initial_cap": 0.00054058403270822,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003632109445872623,
    "unapplied_final_day_resource_cost": 0.0003855091616173862
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 29.5259092123963,
    "beneficial_raw_gain_per_resource_cost": 442.88863818594444,
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
    "accrued_cost": 2.860932200106844,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.11525827608363168,
    "accrued_cost_fraction_initial_cap": 0.09536440667022815,
    "mean_contract_rate": 0.0393429191230955,
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
    "maximum_relative_cash_error": 1.8535808304936276e-15,
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
      "minimum": -0.147859207073901,
      "maximum": 0.05188600487390366,
      "mean": -0.060565850775451825,
      "median": -0.06420645617542517,
      "quantile_05": -0.13606230337504407,
      "quantile_95": 0.04306569502978402
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
      "minimum": 0.27513419502860037,
      "maximum": 0.7415987038352245,
      "mean": 0.4903198559227912,
      "median": 0.4825049569483229,
      "quantile_05": 0.32674957566039003,
      "quantile_95": 0.6700837914394572
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
        "daily_volatility": 0.01706587125785369,
        "excess_kurtosis": 6.107019461308775,
        "return_acf_1": -0.06740944994869624,
        "abs_return_acf_1": 0.3081441309078133,
        "abs_return_acf_5": 0.3545607363767321,
        "abs_return_acf_20": 0.3092859822761436,
        "quantile_01": -0.05326795578323927,
        "quantile_99": 0.04498452169401142,
        "hill_tail_index": 2.9060771967602435
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01941665910040697,
        "excess_kurtosis": 12.156289770139567,
        "return_acf_1": 0.015059787802507454,
        "abs_return_acf_1": 0.38296879213148266,
        "abs_return_acf_5": 0.39566324692947025,
        "abs_return_acf_20": 0.221278343639094,
        "quantile_01": -0.06364091845608334,
        "quantile_99": 0.05145908018814277,
        "hill_tail_index": 2.4898950997436633
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02023968173705691,
        "excess_kurtosis": 10.926251136494304,
        "return_acf_1": 0.042016283169582704,
        "abs_return_acf_1": 0.43235987941800036,
        "abs_return_acf_5": 0.37568459165246787,
        "abs_return_acf_20": 0.2496953485083519,
        "quantile_01": -0.068081032290896,
        "quantile_99": 0.05956152797790694,
        "hill_tail_index": 3.2375825268010803
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019984993891680472,
        "excess_kurtosis": 10.854786273017737,
        "return_acf_1": 0.019645560156779058,
        "abs_return_acf_1": 0.3913718833901599,
        "abs_return_acf_5": 0.34223596469091827,
        "abs_return_acf_20": 0.2360657794754275,
        "quantile_01": -0.06261781788296793,
        "quantile_99": 0.05731177789372959,
        "hill_tail_index": 2.3472574512255617
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016797629637159087,
        "excess_kurtosis": 3.5608806939267614,
        "return_acf_1": -0.08389754348398495,
        "abs_return_acf_1": 0.23140322904345778,
        "abs_return_acf_5": 0.25802254656616475,
        "abs_return_acf_20": 0.22695924397274175,
        "quantile_01": -0.04727332203527914,
        "quantile_99": 0.04815486796885114,
        "hill_tail_index": 4.485167826889756
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017195475460892617,
        "excess_kurtosis": 7.061244096503424,
        "return_acf_1": -0.06570290062576185,
        "abs_return_acf_1": 0.34612194829378623,
        "abs_return_acf_5": 0.32018394556923135,
        "abs_return_acf_20": 0.18312949292504538,
        "quantile_01": -0.048072330237549886,
        "quantile_99": 0.05160910066876282,
        "hill_tail_index": 2.3225638890035336
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016533374854584233,
        "excess_kurtosis": 2.8177808246374534,
        "return_acf_1": -0.10506527889686547,
        "abs_return_acf_1": 0.3181714873258357,
        "abs_return_acf_5": 0.3219751494216583,
        "abs_return_acf_20": 0.2531558974309112,
        "quantile_01": -0.047321124203362236,
        "quantile_99": 0.04865405256862761,
        "hill_tail_index": 5.020251240034634
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01911315875507333,
        "excess_kurtosis": 12.040161348516401,
        "return_acf_1": -0.03812692381955292,
        "abs_return_acf_1": 0.3998772930465035,
        "abs_return_acf_5": 0.5077634460892325,
        "abs_return_acf_20": 0.3424435144552139,
        "quantile_01": -0.05869690347305602,
        "quantile_99": 0.054472104744640475,
        "hill_tail_index": 2.791588609332012
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019648561154152797,
        "excess_kurtosis": 10.633269560731863,
        "return_acf_1": -0.10430893051658108,
        "abs_return_acf_1": 0.45160788899649223,
        "abs_return_acf_5": 0.4349861501630856,
        "abs_return_acf_20": 0.3139881783951349,
        "quantile_01": -0.07437787389345286,
        "quantile_99": 0.0474446732553001,
        "hill_tail_index": 2.2587633886755993
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01668538032888982,
        "excess_kurtosis": 3.284754561583445,
        "return_acf_1": -0.11921791127821778,
        "abs_return_acf_1": 0.28068924328652134,
        "abs_return_acf_5": 0.24755201485656902,
        "abs_return_acf_20": 0.22959395994604231,
        "quantile_01": -0.052155471441372045,
        "quantile_99": 0.04415832901009954,
        "hill_tail_index": 4.4048009919898155
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01775064300936082,
        "excess_kurtosis": 9.516991781712115,
        "return_acf_1": 0.05188600487390366,
        "abs_return_acf_1": 0.32275442757524,
        "abs_return_acf_5": 0.2082016985730092,
        "abs_return_acf_20": 0.2236364770041715,
        "quantile_01": -0.04760861177631669,
        "quantile_99": 0.04815243959081481,
        "hill_tail_index": 2.1726288905690736
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017507815214049514,
        "excess_kurtosis": 1.755946148519505,
        "return_acf_1": -0.11194247074509599,
        "abs_return_acf_1": 0.17271404204810392,
        "abs_return_acf_5": 0.19541686712891645,
        "abs_return_acf_20": 0.2089123939613207,
        "quantile_01": -0.049101125102035355,
        "quantile_99": 0.04804308287127362,
        "hill_tail_index": 5.685894252034584
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017558858547840884,
        "excess_kurtosis": 5.9597964784950115,
        "return_acf_1": -0.05586935194096647,
        "abs_return_acf_1": 0.2469040497194645,
        "abs_return_acf_5": 0.27124218988173193,
        "abs_return_acf_20": 0.23633201938006407,
        "quantile_01": -0.0490047410715661,
        "quantile_99": 0.04914025967190452,
        "hill_tail_index": 3.3524126086655066
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01843122747652406,
        "excess_kurtosis": 5.498372044230043,
        "return_acf_1": -0.10094858311247193,
        "abs_return_acf_1": 0.24793471421016294,
        "abs_return_acf_5": 0.31875352897083736,
        "abs_return_acf_20": 0.17978484702690076,
        "quantile_01": -0.06423422385064226,
        "quantile_99": 0.050942404078330616,
        "hill_tail_index": 3.0689593937202377
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01661636719648298,
        "excess_kurtosis": 2.52474394050983,
        "return_acf_1": -0.1020028698667002,
        "abs_return_acf_1": 0.21084022078837492,
        "abs_return_acf_5": 0.22895958841666533,
        "abs_return_acf_20": 0.19409530942755318,
        "quantile_01": -0.04628240031386263,
        "quantile_99": 0.042097456649630896,
        "hill_tail_index": 5.417168625852896
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016001553958173487,
        "excess_kurtosis": 3.9935266153503823,
        "return_acf_1": -0.04153038767272719,
        "abs_return_acf_1": 0.24914252398155246,
        "abs_return_acf_5": 0.3076772161256015,
        "abs_return_acf_20": 0.2176537304013442,
        "quantile_01": -0.05283351914865155,
        "quantile_99": 0.04032180106226859,
        "hill_tail_index": 3.4544799637073433
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01803477513258772,
        "excess_kurtosis": 6.526509513689637,
        "return_acf_1": -0.13434503727009892,
        "abs_return_acf_1": 0.31204850569454634,
        "abs_return_acf_5": 0.2778519891881119,
        "abs_return_acf_20": 0.3024688349520057,
        "quantile_01": -0.052027389832154936,
        "quantile_99": 0.056316938574500076,
        "hill_tail_index": 2.9971946376451934
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01801993559069673,
        "excess_kurtosis": 4.147241708259865,
        "return_acf_1": -0.1374673392790901,
        "abs_return_acf_1": 0.28574776214100756,
        "abs_return_acf_5": 0.3352514010104786,
        "abs_return_acf_20": 0.20739690283357362,
        "quantile_01": -0.05781778987743582,
        "quantile_99": 0.04874008740967155,
        "hill_tail_index": 3.8566476773512446
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020037455169777337,
        "excess_kurtosis": 6.229353094361159,
        "return_acf_1": -0.147859207073901,
        "abs_return_acf_1": 0.4117598652584474,
        "abs_return_acf_5": 0.3819290318664746,
        "abs_return_acf_20": 0.3269379376710477,
        "quantile_01": -0.06481680081991356,
        "quantile_99": 0.05462174161155566,
        "hill_tail_index": 3.2098638752984114
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016508688294675253,
        "excess_kurtosis": 1.998103016861446,
        "return_acf_1": -0.08946134584479645,
        "abs_return_acf_1": 0.2128590170713042,
        "abs_return_acf_5": 0.2334513834143923,
        "abs_return_acf_20": 0.17841024008678655,
        "quantile_01": -0.04340415508559479,
        "quantile_99": 0.04342154738301114,
        "hill_tail_index": 4.418470210158592
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01844120606488601,
        "excess_kurtosis": 6.976643828564738,
        "return_acf_1": -0.05186527279829597,
        "abs_return_acf_1": 0.38453104246873865,
        "abs_return_acf_5": 0.3804527777109229,
        "abs_return_acf_20": 0.2748055131009544,
        "quantile_01": -0.05966663568573808,
        "quantile_99": 0.04731253562729062,
        "hill_tail_index": 2.7183840481677173
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020856196854280442,
        "excess_kurtosis": 10.030924781485913,
        "return_acf_1": -0.003754469957259757,
        "abs_return_acf_1": 0.34798698941086054,
        "abs_return_acf_5": 0.3555539125755923,
        "abs_return_acf_20": 0.28561267072251645,
        "quantile_01": -0.07742122090116721,
        "quantile_99": 0.05332399327743564,
        "hill_tail_index": 2.4284505668930207
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02056335981075046,
        "excess_kurtosis": 13.83125921525862,
        "return_acf_1": 0.0439243047335851,
        "abs_return_acf_1": 0.4843837004919741,
        "abs_return_acf_5": 0.40585131543693126,
        "abs_return_acf_20": 0.2500610442713523,
        "quantile_01": -0.06711833952593685,
        "quantile_99": 0.06011748810092171,
        "hill_tail_index": 2.4557515615455685
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017910661193755933,
        "excess_kurtosis": 7.84242212920679,
        "return_acf_1": -0.005305440774785322,
        "abs_return_acf_1": 0.26337626147816917,
        "abs_return_acf_5": 0.3349447863650425,
        "abs_return_acf_20": 0.24535045782753442,
        "quantile_01": -0.058550642681097644,
        "quantile_99": 0.04433266706371651,
        "hill_tail_index": 2.3151756215027004
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018709158793872666,
        "excess_kurtosis": 8.14259440623462,
        "return_acf_1": -0.13421789296039427,
        "abs_return_acf_1": 0.341377306567518,
        "abs_return_acf_5": 0.3434978230695959,
        "abs_return_acf_20": 0.3359035443959465,
        "quantile_01": -0.05681723740638788,
        "quantile_99": 0.05259936481732121,
        "hill_tail_index": 3.1777630273003648
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020119962861078117,
        "excess_kurtosis": 15.546529002855422,
        "return_acf_1": -0.03764245054578569,
        "abs_return_acf_1": 0.39535860631555714,
        "abs_return_acf_5": 0.57268934492902,
        "abs_return_acf_20": 0.23857618361239746,
        "quantile_01": -0.07198159547676952,
        "quantile_99": 0.054452617167961265,
        "hill_tail_index": 2.690714142295893
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02077861099860153,
        "excess_kurtosis": 7.3847022815527055,
        "return_acf_1": -0.05633915090867505,
        "abs_return_acf_1": 0.4038902114132815,
        "abs_return_acf_5": 0.41694722836109316,
        "abs_return_acf_20": 0.31399293925758254,
        "quantile_01": -0.07170254651551809,
        "quantile_99": 0.06618175869372138,
        "hill_tail_index": 3.3550901566476155
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017406142367745236,
        "excess_kurtosis": 9.631353903896448,
        "return_acf_1": -0.06271001172508847,
        "abs_return_acf_1": 0.3217080643717609,
        "abs_return_acf_5": 0.2739164832366987,
        "abs_return_acf_20": 0.21512887421724233,
        "quantile_01": -0.04974447677024209,
        "quantile_99": 0.04252722789591575,
        "hill_tail_index": 2.800081621352857
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01903367214870002,
        "excess_kurtosis": 7.201799734637973,
        "return_acf_1": -0.007426518796768918,
        "abs_return_acf_1": 0.33359029027652515,
        "abs_return_acf_5": 0.35300780023701367,
        "abs_return_acf_20": 0.2812899319635256,
        "quantile_01": -0.055044499096078746,
        "quantile_99": 0.05545372324798256,
        "hill_tail_index": 3.8073870401019496
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019382626627096684,
        "excess_kurtosis": 11.190087462277916,
        "return_acf_1": -0.12509072415735076,
        "abs_return_acf_1": 0.31220473242054375,
        "abs_return_acf_5": 0.4791618767385458,
        "abs_return_acf_20": 0.33078701970106295,
        "quantile_01": -0.06682380801645035,
        "quantile_99": 0.04938278677113161,
        "hill_tail_index": 2.643937798163008
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
