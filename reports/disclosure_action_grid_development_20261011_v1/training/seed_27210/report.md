# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27210
Run ID: `edf685f820ac2b1100bc80c7a08b9524a240532d14dd5fdc260b1758a6babd21`
Result fingerprint: `02fd3c2e2cb242f4233c7a342defa77407d292a8f5b805148c96d3969892628c`

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
    "equal_weight_sd": -0.7820476190476158,
    "equal_weight_raw": -11.730714285714233,
    "fixed_start_cap_weight_sd": -0.7824986316340723,
    "fixed_start_cap_weight_raw": -11.737479474511087,
    "end_cap_weight_sd": -0.7622543774274483,
    "end_cap_weight_raw": -11.433815661411725
  },
  "full_period_change": {
    "equal_weight_sd": -1.1625714285714237,
    "equal_weight_raw": -17.438571428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0987638888888844,
    "inflation_mean_sd": 0.8498531746031747
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1703333333333365,
    "equal_weight_raw": 2.5550000000000477,
    "fixed_start_cap_weight_sd": 0.16988232074687995,
    "fixed_start_cap_weight_raw": 2.5482348112031996,
    "end_cap_weight_sd": 0.19012657495350402,
    "end_cap_weight_raw": 2.8518986243025597
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8307142857142825,
      "change_raw": -12.460714285714237,
      "decay_adjusted_gain_sd": 0.12166666666666985
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6984920634920602,
      "change_raw": -10.477380952380903,
      "decay_adjusted_gain_sd": 0.25388888888889216
    },
    "small": {
      "count": 18,
      "change_sd": -0.8157142857142824,
      "change_raw": -12.235714285714236,
      "decay_adjusted_gain_sd": 0.13666666666666982
    },
    "large_minus_small_sd": -0.015000000000000124,
    "large_minus_small_raw": -0.22500000000000187
  },
  "inflation": {
    "initial_mean_sd": 0.4185833333333333,
    "final_mean_sd": 0.9158333333333335,
    "mean_sd": 0.6797675548154316,
    "mean_absolute_raw_gap": 10.196513322231473,
    "final_absolute_raw_gap": 13.737500000000002,
    "mean_range_fraction": 0.10196513322231474
  },
  "impact": {
    "initial_share": 0.16666666666666666,
    "final_share": 0.19333333333333333,
    "initial_wealth_share": 0.29108303178909445,
    "final_wealth_share": 0.17190137860385693
  },
  "pricing_slope": {
    "mean": -0.003229791674841563,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.05671752875548082,
    "real_improvement_cost": 0.037232028986663,
    "washing_cost": 0.019485499768817815,
    "fine_transfer": 0.015358626530434679,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0720761552859155,
    "resource_cost_fraction_initial_cap": 0.0018905842918493607,
    "private_net_outflow_fraction_initial_cap": 0.002402538509530517,
    "fine_transfer_fraction_initial_cap": 0.000511954217681156,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002844445008804479,
    "unapplied_final_day_resource_cost": 0.00203974169354862
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 90.09560381289175,
    "beneficial_raw_gain_per_resource_cost": 1351.4340571933762,
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
    "accrued_cost": 2.857545106944793,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.11864536924568336,
    "accrued_cost_fraction_initial_cap": 0.09525150356482644,
    "mean_contract_rate": 0.03944146300292841,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 39,
    "maximum_relative_cash_error": 1.7877487915398933e-15,
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
      "minimum": -0.22147908646840497,
      "maximum": -0.05482101492729651,
      "mean": -0.12111318960361335,
      "median": -0.12613144063130446,
      "quantile_05": -0.17240048023648938,
      "quantile_95": -0.06269696308264258
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
      "minimum": 0.4270652188736359,
      "maximum": 0.8526269141377707,
      "mean": 0.7469019163158694,
      "median": 0.7718423701344469,
      "quantile_05": 0.5707210819296137,
      "quantile_95": 0.8287007028638639
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
        "daily_volatility": 0.024768837778645733,
        "excess_kurtosis": 14.791013586789141,
        "return_acf_1": -0.14494285234867463,
        "abs_return_acf_1": 0.4633836262776806,
        "abs_return_acf_5": 0.48852988026561345,
        "abs_return_acf_20": 0.3214689997401424,
        "quantile_01": -0.0959735784406525,
        "quantile_99": 0.05983836099006872,
        "hill_tail_index": 2.005716899352387
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022193791758008792,
        "excess_kurtosis": 8.009229807386541,
        "return_acf_1": -0.10414817497131897,
        "abs_return_acf_1": 0.34279125145277367,
        "abs_return_acf_5": 0.39241980499493434,
        "abs_return_acf_20": 0.34098759248730987,
        "quantile_01": -0.07557179692798106,
        "quantile_99": 0.061441674481834484,
        "hill_tail_index": 3.190770763640931
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023635043648036577,
        "excess_kurtosis": 11.522307064746244,
        "return_acf_1": -0.10833024421453186,
        "abs_return_acf_1": 0.3995300614016169,
        "abs_return_acf_5": 0.423468122134197,
        "abs_return_acf_20": 0.3829819796768292,
        "quantile_01": -0.0795416283435294,
        "quantile_99": 0.07042349391488399,
        "hill_tail_index": 2.8884207995301696
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021544059595025002,
        "excess_kurtosis": 7.140780156697515,
        "return_acf_1": -0.14015857672155496,
        "abs_return_acf_1": 0.322346977185131,
        "abs_return_acf_5": 0.3603372447684907,
        "abs_return_acf_20": 0.2809001996084501,
        "quantile_01": -0.08118109966494644,
        "quantile_99": 0.059505079871101395,
        "hill_tail_index": 3.6939703381833153
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.023268769293061115,
        "excess_kurtosis": 11.415212138146954,
        "return_acf_1": -0.06788576411335537,
        "abs_return_acf_1": 0.36116118963332877,
        "abs_return_acf_5": 0.43853349503602207,
        "abs_return_acf_20": 0.31074070776112206,
        "quantile_01": -0.07956652516917795,
        "quantile_99": 0.06989844635885953,
        "hill_tail_index": 2.9106297990226637
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02602447198653735,
        "excess_kurtosis": 14.130642540185747,
        "return_acf_1": -0.11893359981370724,
        "abs_return_acf_1": 0.4157192417393731,
        "abs_return_acf_5": 0.5074248183091217,
        "abs_return_acf_20": 0.4051249642281446,
        "quantile_01": -0.08883066838313154,
        "quantile_99": 0.07878127010362393,
        "hill_tail_index": 2.8100761340208997
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.024062472972146393,
        "excess_kurtosis": 10.11377359574459,
        "return_acf_1": -0.06169938099888352,
        "abs_return_acf_1": 0.4320017737171442,
        "abs_return_acf_5": 0.4508489775008473,
        "abs_return_acf_20": 0.36582700647639677,
        "quantile_01": -0.0857015367272253,
        "quantile_99": 0.06684658617235563,
        "hill_tail_index": 2.703953916260646
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.0256238008550083,
        "excess_kurtosis": 16.504298179455663,
        "return_acf_1": -0.15827572834340617,
        "abs_return_acf_1": 0.4705514734159694,
        "abs_return_acf_5": 0.5018650338494798,
        "abs_return_acf_20": 0.33262253264824104,
        "quantile_01": -0.09443389050218819,
        "quantile_99": 0.07263561223536065,
        "hill_tail_index": 2.9821531790022044
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022480588366114655,
        "excess_kurtosis": 8.532713455816298,
        "return_acf_1": -0.13186022311759374,
        "abs_return_acf_1": 0.34695361572288064,
        "abs_return_acf_5": 0.33567564391360594,
        "abs_return_acf_20": 0.3207522832807296,
        "quantile_01": -0.08373939938045302,
        "quantile_99": 0.061567722591033075,
        "hill_tail_index": 3.317652728369896
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.026269483703449246,
        "excess_kurtosis": 14.714593525293008,
        "return_acf_1": -0.08764974106300827,
        "abs_return_acf_1": 0.44753209422882695,
        "abs_return_acf_5": 0.48861763011148174,
        "abs_return_acf_20": 0.35761670642573246,
        "quantile_01": -0.08779959838284114,
        "quantile_99": 0.07390250355094892,
        "hill_tail_index": 2.788198725672957
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021983980407628258,
        "excess_kurtosis": 7.990278035079257,
        "return_acf_1": -0.14822879453575702,
        "abs_return_acf_1": 0.3151893859874801,
        "abs_return_acf_5": 0.3688038129606695,
        "abs_return_acf_20": 0.35380624558250656,
        "quantile_01": -0.07604799343137675,
        "quantile_99": 0.0650349890219667,
        "hill_tail_index": 3.063668161299395
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022521179441144012,
        "excess_kurtosis": 7.861957623448156,
        "return_acf_1": -0.16447099377412272,
        "abs_return_acf_1": 0.33321739508667414,
        "abs_return_acf_5": 0.3701251245600715,
        "abs_return_acf_20": 0.2846233324060265,
        "quantile_01": -0.0814089145295253,
        "quantile_99": 0.07597994045371038,
        "hill_tail_index": 3.8896914193060534
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02653769832449992,
        "excess_kurtosis": 13.970819891342515,
        "return_acf_1": -0.17888824188751665,
        "abs_return_acf_1": 0.42240280846795086,
        "abs_return_acf_5": 0.46460959354515924,
        "abs_return_acf_20": 0.4128024159281531,
        "quantile_01": -0.09115454711087405,
        "quantile_99": 0.07862563853886322,
        "hill_tail_index": 2.889113641848962
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02584283259245644,
        "excess_kurtosis": 19.104789819154067,
        "return_acf_1": -0.11510639091636282,
        "abs_return_acf_1": 0.4124692901787356,
        "abs_return_acf_5": 0.4223825734147888,
        "abs_return_acf_20": 0.3698941925643472,
        "quantile_01": -0.08456092471097675,
        "quantile_99": 0.06779165821638064,
        "hill_tail_index": 2.196804811382979
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024645252089909867,
        "excess_kurtosis": 11.942426885544647,
        "return_acf_1": -0.10184100503096387,
        "abs_return_acf_1": 0.40631459467898323,
        "abs_return_acf_5": 0.449918539532029,
        "abs_return_acf_20": 0.31978053397223233,
        "quantile_01": -0.09306093433513883,
        "quantile_99": 0.06728459151396401,
        "hill_tail_index": 2.655125587238333
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022676143214004733,
        "excess_kurtosis": 7.123552429065187,
        "return_acf_1": -0.09771116410916186,
        "abs_return_acf_1": 0.3846799569206004,
        "abs_return_acf_5": 0.4516819587335521,
        "abs_return_acf_20": 0.3545046028640077,
        "quantile_01": -0.08388323780534283,
        "quantile_99": 0.06559371760168214,
        "hill_tail_index": 3.871707034754846
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02472259555618926,
        "excess_kurtosis": 12.938815164351514,
        "return_acf_1": -0.06391623007390364,
        "abs_return_acf_1": 0.3918782638653506,
        "abs_return_acf_5": 0.44799180068282135,
        "abs_return_acf_20": 0.3692118053742777,
        "quantile_01": -0.08241288198459706,
        "quantile_99": 0.06774168891727589,
        "hill_tail_index": 2.9786688105861936
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.026864591699320373,
        "excess_kurtosis": 16.036504721816684,
        "return_acf_1": -0.06852133907755799,
        "abs_return_acf_1": 0.3992480891217112,
        "abs_return_acf_5": 0.4425902909220921,
        "abs_return_acf_20": 0.37800490257108194,
        "quantile_01": -0.09503656677470905,
        "quantile_99": 0.07250989278729408,
        "hill_tail_index": 2.11545174657271
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022117688805756763,
        "excess_kurtosis": 7.709693206621825,
        "return_acf_1": -0.16118580945940703,
        "abs_return_acf_1": 0.3768458644994985,
        "abs_return_acf_5": 0.386055525252438,
        "abs_return_acf_20": 0.32921137100056663,
        "quantile_01": -0.0733216806863216,
        "quantile_99": 0.07687368304411306,
        "hill_tail_index": 3.6354505736800165
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02269578639217837,
        "excess_kurtosis": 6.574026639367418,
        "return_acf_1": -0.1383567438200326,
        "abs_return_acf_1": 0.3879336182896899,
        "abs_return_acf_5": 0.3628686499688963,
        "abs_return_acf_20": 0.36967559427334395,
        "quantile_01": -0.07770571053563521,
        "quantile_99": 0.069902673200376,
        "hill_tail_index": 4.149538439520661
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02415732825047173,
        "excess_kurtosis": 16.796472192546887,
        "return_acf_1": -0.22147908646840497,
        "abs_return_acf_1": 0.4604185500378466,
        "abs_return_acf_5": 0.36272866058503084,
        "abs_return_acf_20": 0.33975495453395055,
        "quantile_01": -0.07283609831066586,
        "quantile_99": 0.07846881215720627,
        "hill_tail_index": 3.016631848373449
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022385279571556532,
        "excess_kurtosis": 8.17516255820419,
        "return_acf_1": -0.14540548853415222,
        "abs_return_acf_1": 0.4115140673188707,
        "abs_return_acf_5": 0.3839972939736462,
        "abs_return_acf_20": 0.37528580002439876,
        "quantile_01": -0.0781565959045665,
        "quantile_99": 0.06601793270487576,
        "hill_tail_index": 3.8648328907686498
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024469857905343305,
        "excess_kurtosis": 11.569905999660296,
        "return_acf_1": -0.09855291560868297,
        "abs_return_acf_1": 0.4050756995796359,
        "abs_return_acf_5": 0.3809478337207618,
        "abs_return_acf_20": 0.3083366228547503,
        "quantile_01": -0.09079384206996463,
        "quantile_99": 0.06555743313643972,
        "hill_tail_index": 2.6649962544745764
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02283450274979467,
        "excess_kurtosis": 9.748321610568697,
        "return_acf_1": -0.08209158562434551,
        "abs_return_acf_1": 0.3660469773962284,
        "abs_return_acf_5": 0.3665132362229559,
        "abs_return_acf_20": 0.3984540301434475,
        "quantile_01": -0.0769876057567409,
        "quantile_99": 0.07351888077545146,
        "hill_tail_index": 3.9021132089561044
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0242559183781948,
        "excess_kurtosis": 12.905499160798588,
        "return_acf_1": -0.12628542417762414,
        "abs_return_acf_1": 0.4132280021959765,
        "abs_return_acf_5": 0.40696809946113544,
        "abs_return_acf_20": 0.3452857937910169,
        "quantile_01": -0.08614462699014216,
        "quantile_99": 0.06506701269820006,
        "hill_tail_index": 2.5963095881146465
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.026208447902515915,
        "excess_kurtosis": 15.96054765745033,
        "return_acf_1": -0.05482101492729651,
        "abs_return_acf_1": 0.4516827604114727,
        "abs_return_acf_5": 0.446110653870368,
        "abs_return_acf_20": 0.31685394265849587,
        "quantile_01": -0.09226546487043305,
        "quantile_99": 0.06963478704944612,
        "hill_tail_index": 2.2918963267943564
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02600885219000906,
        "excess_kurtosis": 16.089339248686937,
        "return_acf_1": -0.13801615101592538,
        "abs_return_acf_1": 0.4347616753074831,
        "abs_return_acf_5": 0.45479406551819523,
        "abs_return_acf_20": 0.465317453119621,
        "quantile_01": -0.07526720570758565,
        "quantile_99": 0.07248980480366245,
        "hill_tail_index": 2.5196618084469966
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.025015348630454397,
        "excess_kurtosis": 14.358630506936091,
        "return_acf_1": -0.12597745708498478,
        "abs_return_acf_1": 0.39170523662777074,
        "abs_return_acf_5": 0.4452073852594679,
        "abs_return_acf_20": 0.31815648444004424,
        "quantile_01": -0.08997891056127987,
        "quantile_99": 0.06581844894625838,
        "hill_tail_index": 2.5266487040242422
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02400600707089274,
        "excess_kurtosis": 12.241287039266494,
        "return_acf_1": -0.14803529849584462,
        "abs_return_acf_1": 0.4128216131231305,
        "abs_return_acf_5": 0.408265370106807,
        "abs_return_acf_20": 0.3199086688621478,
        "quantile_01": -0.08861466323971474,
        "quantile_99": 0.07048532973330117,
        "hill_tail_index": 2.787218504755592
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02264348739563816,
        "excess_kurtosis": 6.376263624096211,
        "return_acf_1": -0.13062026778031874,
        "abs_return_acf_1": 0.43085600218353637,
        "abs_return_acf_5": 0.4218191100241395,
        "abs_return_acf_20": 0.37028741052343916,
        "quantile_01": -0.07815191401203282,
        "quantile_99": 0.06815707879149088,
        "hill_tail_index": 5.3211608645290145
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
