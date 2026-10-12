# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27004
Run ID: `2f6d71bee2ab7efc768bcc077008b26bc78a16269cec6ea9b63e57bb83f5145e`
Result fingerprint: `a78aa5ce304b42b5b4ab7842e39a5b7ee27ee9a6b0f16559b534b72fda6443b3`

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
    "equal_weight_sd": -0.4719642857142824,
    "equal_weight_raw": -7.079464285714236,
    "fixed_start_cap_weight_sd": -0.5400546092773081,
    "fixed_start_cap_weight_raw": -8.100819139159622,
    "end_cap_weight_sd": -0.5353935022795577,
    "end_cap_weight_raw": -8.030902534193368
  },
  "full_period_change": {
    "equal_weight_sd": -0.8294880952380903,
    "equal_weight_raw": -12.442321428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7959070767195723,
    "inflation_mean_sd": 0.5028475529100529
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4804166666666699,
    "equal_weight_raw": 7.206250000000048,
    "fixed_start_cap_weight_sd": 0.4123263431036444,
    "fixed_start_cap_weight_raw": 6.184895146554666,
    "end_cap_weight_sd": 0.41698745010139454,
    "end_cap_weight_raw": 6.2548117515209185
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6123809523809493,
      "change_raw": -9.185714285714239,
      "decay_adjusted_gain_sd": 0.34000000000000313
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5340476190476158,
      "change_raw": -8.010714285714236,
      "decay_adjusted_gain_sd": 0.4183333333333365
    },
    "small": {
      "count": 18,
      "change_sd": -0.41751984126983804,
      "change_raw": -6.2627976190475705,
      "decay_adjusted_gain_sd": 0.5348611111111143
    },
    "large_minus_small_sd": -0.1948611111111112,
    "large_minus_small_raw": -2.922916666666668
  },
  "inflation": {
    "initial_mean_sd": 0.18191666666666667,
    "final_mean_sd": 0.4935833333333334,
    "mean_sd": 0.3974564945878435,
    "mean_absolute_raw_gap": 5.961847418817652,
    "final_absolute_raw_gap": 7.4037500000000005,
    "mean_range_fraction": 0.05961847418817652
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.28,
    "initial_wealth_share": 0.3412451148042172,
    "final_wealth_share": 0.29551976349048537
  },
  "pricing_slope": {
    "mean": -0.001998980746628925,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.19188331403991438,
    "real_improvement_cost": 0.1500366961972399,
    "washing_cost": 0.041846617842674474,
    "fine_transfer": 0.04278045960795475,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2346637736478691,
    "resource_cost_fraction_initial_cap": 0.0063961104679971445,
    "private_net_outflow_fraction_initial_cap": 0.007822125788262302,
    "fine_transfer_fraction_initial_cap": 0.001426015320265158,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0038607937019588005,
    "unapplied_final_day_resource_cost": 0.003967065760238169
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 75.11075192813324,
    "beneficial_raw_gain_per_resource_cost": 1126.6612789219987,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 2.832723684124654,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.14346679206582247,
    "accrued_cost_fraction_initial_cap": 0.0944241228041551,
    "mean_contract_rate": 0.038712056872279924,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.657518096393919e-15,
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
      "minimum": -0.1834822349240314,
      "maximum": -0.01583988720369643,
      "mean": -0.09634529375993063,
      "median": -0.10240449197874085,
      "quantile_05": -0.17035432666726813,
      "quantile_95": -0.017676065716356163
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
      "minimum": 0.45861462048978496,
      "maximum": 0.7950356539437023,
      "mean": 0.6621682367637735,
      "median": 0.678020138113505,
      "quantile_05": 0.5140915915171407,
      "quantile_95": 0.7519950523682066
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
        "daily_volatility": 0.01921601631165934,
        "excess_kurtosis": 12.589891963300355,
        "return_acf_1": -0.1233501815466284,
        "abs_return_acf_1": 0.36632068164799625,
        "abs_return_acf_5": 0.4709392278300105,
        "abs_return_acf_20": 0.2518854181898746,
        "quantile_01": -0.05928099806851194,
        "quantile_99": 0.053503020469243955,
        "hill_tail_index": 2.6383227469616384
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019627816092840342,
        "excess_kurtosis": 6.930309244327672,
        "return_acf_1": -0.1158690421354865,
        "abs_return_acf_1": 0.3639975474853682,
        "abs_return_acf_5": 0.3771526906280167,
        "abs_return_acf_20": 0.31858928535436803,
        "quantile_01": -0.061652595674881634,
        "quantile_99": 0.05607021598022998,
        "hill_tail_index": 3.134079804571897
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01840982719409516,
        "excess_kurtosis": 6.812971598981738,
        "return_acf_1": -0.07699220026639389,
        "abs_return_acf_1": 0.3856451981145489,
        "abs_return_acf_5": 0.4007705416454342,
        "abs_return_acf_20": 0.2755571355877531,
        "quantile_01": -0.06068403291497401,
        "quantile_99": 0.052420734979795894,
        "hill_tail_index": 3.141934800153615
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020058941478778396,
        "excess_kurtosis": 12.50575170079979,
        "return_acf_1": -0.13340337375656425,
        "abs_return_acf_1": 0.4678004744559651,
        "abs_return_acf_5": 0.45135650306971703,
        "abs_return_acf_20": 0.30177792720101626,
        "quantile_01": -0.07789485849852298,
        "quantile_99": 0.05223447346095494,
        "hill_tail_index": 2.179582654819378
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019272384456497038,
        "excess_kurtosis": 6.671940983925891,
        "return_acf_1": -0.1409331372017734,
        "abs_return_acf_1": 0.39388658044742453,
        "abs_return_acf_5": 0.40252640039370224,
        "abs_return_acf_20": 0.3219932490798497,
        "quantile_01": -0.06369411207179106,
        "quantile_99": 0.05149009630510547,
        "hill_tail_index": 2.9612664977570478
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01704154567810678,
        "excess_kurtosis": 6.107192451782073,
        "return_acf_1": -0.045341657976410196,
        "abs_return_acf_1": 0.3215054346849717,
        "abs_return_acf_5": 0.3001934734802699,
        "abs_return_acf_20": 0.26598910991302976,
        "quantile_01": -0.05139446170567867,
        "quantile_99": 0.046903115954988146,
        "hill_tail_index": 3.990635310191553
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018094514389840884,
        "excess_kurtosis": 5.365693448424214,
        "return_acf_1": -0.14442228569416712,
        "abs_return_acf_1": 0.4056303750374774,
        "abs_return_acf_5": 0.40367633406365444,
        "abs_return_acf_20": 0.3030354113333494,
        "quantile_01": -0.055975633327603296,
        "quantile_99": 0.0571177770247383,
        "hill_tail_index": 4.132247179786169
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018996825436772283,
        "excess_kurtosis": 6.144896300028137,
        "return_acf_1": -0.07501668433404061,
        "abs_return_acf_1": 0.32859890029142186,
        "abs_return_acf_5": 0.3427396827254654,
        "abs_return_acf_20": 0.2283709987848455,
        "quantile_01": -0.0579443552289651,
        "quantile_99": 0.048788202751887236,
        "hill_tail_index": 3.8067339756331653
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01758222212671111,
        "excess_kurtosis": 3.2297022864837395,
        "return_acf_1": -0.14718363487393898,
        "abs_return_acf_1": 0.30173234668581506,
        "abs_return_acf_5": 0.27839893838115215,
        "abs_return_acf_20": 0.19082723321941966,
        "quantile_01": -0.051822837628746864,
        "quantile_99": 0.05121833492496212,
        "hill_tail_index": 4.030129780232255
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020723516455624928,
        "excess_kurtosis": 11.896223682106227,
        "return_acf_1": -0.11221303869572748,
        "abs_return_acf_1": 0.3932698738745353,
        "abs_return_acf_5": 0.4629943598452138,
        "abs_return_acf_20": 0.2709709861351391,
        "quantile_01": -0.07119321767022738,
        "quantile_99": 0.05477468132018159,
        "hill_tail_index": 2.5326766219288186
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01994620617688179,
        "excess_kurtosis": 10.82529119164361,
        "return_acf_1": -0.15433007821059402,
        "abs_return_acf_1": 0.476945252563094,
        "abs_return_acf_5": 0.5051009792194068,
        "abs_return_acf_20": 0.3106247552941572,
        "quantile_01": -0.06675257307720187,
        "quantile_99": 0.05856423040695859,
        "hill_tail_index": 3.592774790871869
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020497341072680638,
        "excess_kurtosis": 9.026135745175157,
        "return_acf_1": -0.10677377872614838,
        "abs_return_acf_1": 0.36229623205099154,
        "abs_return_acf_5": 0.3961113563406354,
        "abs_return_acf_20": 0.28322392815770203,
        "quantile_01": -0.07313708539144974,
        "quantile_99": 0.055948449035667036,
        "hill_tail_index": 2.6049078724050543
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01808496283426204,
        "excess_kurtosis": 10.407216239212206,
        "return_acf_1": -0.019072439964630095,
        "abs_return_acf_1": 0.4598646400669225,
        "abs_return_acf_5": 0.483305601054028,
        "abs_return_acf_20": 0.31489514351557046,
        "quantile_01": -0.058328711074335314,
        "quantile_99": 0.05184181087705511,
        "hill_tail_index": 3.5990349295624857
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017604559369839644,
        "excess_kurtosis": 10.644384961143068,
        "return_acf_1": -0.01583988720369643,
        "abs_return_acf_1": 0.36431064893166926,
        "abs_return_acf_5": 0.37871015558574,
        "abs_return_acf_20": 0.22158078818296642,
        "quantile_01": -0.05424757713940015,
        "quantile_99": 0.04382922035153181,
        "hill_tail_index": 2.706186527223874
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019663294292710024,
        "excess_kurtosis": 7.1632540355665615,
        "return_acf_1": -0.17117515923974955,
        "abs_return_acf_1": 0.40488757010903703,
        "abs_return_acf_5": 0.3868275151639728,
        "abs_return_acf_20": 0.27837099406560867,
        "quantile_01": -0.06519978613358947,
        "quantile_99": 0.05667731195969033,
        "hill_tail_index": 3.1047504039106615
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022213217004661685,
        "excess_kurtosis": 11.425667670012098,
        "return_acf_1": -0.16935108685645753,
        "abs_return_acf_1": 0.4977236894075856,
        "abs_return_acf_5": 0.49883897235722846,
        "abs_return_acf_20": 0.30901298271453265,
        "quantile_01": -0.07675862159415917,
        "quantile_99": 0.06916845826670863,
        "hill_tail_index": 3.253351439074206
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02077231659842799,
        "excess_kurtosis": 9.749041468869107,
        "return_acf_1": -0.11264769347422483,
        "abs_return_acf_1": 0.4476002160317199,
        "abs_return_acf_5": 0.4442642968653788,
        "abs_return_acf_20": 0.3221515112029131,
        "quantile_01": -0.06721897408852227,
        "quantile_99": 0.06047541516717365,
        "hill_tail_index": 3.4221373694535098
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019448897258852803,
        "excess_kurtosis": 9.003746065748999,
        "return_acf_1": -0.016533577695041116,
        "abs_return_acf_1": 0.40923850240571763,
        "abs_return_acf_5": 0.40002612426948797,
        "abs_return_acf_20": 0.24086272769862768,
        "quantile_01": -0.06236415149800531,
        "quantile_99": 0.05475731778298227,
        "hill_tail_index": 3.6207927320624727
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021628578390122357,
        "excess_kurtosis": 22.54060528299505,
        "return_acf_1": -0.06253933516441898,
        "abs_return_acf_1": 0.41789451107645353,
        "abs_return_acf_5": 0.46610700287722134,
        "abs_return_acf_20": 0.23632449405494294,
        "quantile_01": -0.06656768381573608,
        "quantile_99": 0.06222350244285445,
        "hill_tail_index": 2.326953783780597
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0220105250067549,
        "excess_kurtosis": 16.583055868597043,
        "return_acf_1": -0.11110384622760965,
        "abs_return_acf_1": 0.35912706531778393,
        "abs_return_acf_5": 0.45757265188938123,
        "abs_return_acf_20": 0.26319603013284093,
        "quantile_01": -0.06396272435133195,
        "quantile_99": 0.05512922059476765,
        "hill_tail_index": 2.226963810230096
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016566928793860892,
        "excess_kurtosis": 2.2759872764090936,
        "return_acf_1": -0.09285194056709688,
        "abs_return_acf_1": 0.2098718467105148,
        "abs_return_acf_5": 0.24595586170097938,
        "abs_return_acf_20": 0.18828380576579684,
        "quantile_01": -0.047446090080446604,
        "quantile_99": 0.04516380631386137,
        "hill_tail_index": 5.113073973082945
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018244965581550178,
        "excess_kurtosis": 10.206498459614146,
        "return_acf_1": -0.08428901339061942,
        "abs_return_acf_1": 0.3257335259408,
        "abs_return_acf_5": 0.3278870361716302,
        "abs_return_acf_20": 0.18256440331904522,
        "quantile_01": -0.060402623860775786,
        "quantile_99": 0.0445759697061662,
        "hill_tail_index": 2.6455967701042673
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01975535256307952,
        "excess_kurtosis": 9.877655492977798,
        "return_acf_1": -0.023543562459582727,
        "abs_return_acf_1": 0.39210312481214715,
        "abs_return_acf_5": 0.3688793616727565,
        "abs_return_acf_20": 0.22574615154830485,
        "quantile_01": -0.06102110437744309,
        "quantile_99": 0.05420824300015199,
        "hill_tail_index": 3.28406675526597
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018968391531069873,
        "excess_kurtosis": 9.554053849911742,
        "return_acf_1": -0.032318914926864444,
        "abs_return_acf_1": 0.37620215529954765,
        "abs_return_acf_5": 0.3740275804230347,
        "abs_return_acf_20": 0.254244169889188,
        "quantile_01": -0.0682242619394477,
        "quantile_99": 0.048114867309224346,
        "hill_tail_index": 3.0283380612541277
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0170717913997153,
        "excess_kurtosis": 5.611305753141776,
        "return_acf_1": -0.09980232359496201,
        "abs_return_acf_1": 0.27378017822926654,
        "abs_return_acf_5": 0.29750108110622714,
        "abs_return_acf_20": 0.22357261387636587,
        "quantile_01": -0.05416827835657695,
        "quantile_99": 0.04785905097173272,
        "hill_tail_index": 3.411025029846877
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019867165964002086,
        "excess_kurtosis": 10.61382372204835,
        "return_acf_1": -0.10500666036251971,
        "abs_return_acf_1": 0.4038923948812674,
        "abs_return_acf_5": 0.4384333113570484,
        "abs_return_acf_20": 0.19063663398574526,
        "quantile_01": -0.06943872244273099,
        "quantile_99": 0.05742422082006766,
        "hill_tail_index": 2.7905065382064587
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020098598041703334,
        "excess_kurtosis": 17.489109100036487,
        "return_acf_1": -0.09613450250865563,
        "abs_return_acf_1": 0.3455497154300343,
        "abs_return_acf_5": 0.388310192535017,
        "abs_return_acf_20": 0.25238214706131346,
        "quantile_01": -0.06771903491595879,
        "quantile_99": 0.049973025536812266,
        "hill_tail_index": 2.5230515234470072
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017647883995300186,
        "excess_kurtosis": 3.1330162543584663,
        "return_acf_1": -0.1834822349240314,
        "abs_return_acf_1": 0.33613893793503075,
        "abs_return_acf_5": 0.3276594385884066,
        "abs_return_acf_20": 0.26932445195202726,
        "quantile_01": -0.05185134832398518,
        "quantile_99": 0.050043956598939926,
        "hill_tail_index": 4.439096699990043
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018409592314319646,
        "excess_kurtosis": 12.257144509434537,
        "return_acf_1": -0.043923510008200405,
        "abs_return_acf_1": 0.3532815316312412,
        "abs_return_acf_5": 0.30911612286028145,
        "abs_return_acf_20": 0.15166445628786115,
        "quantile_01": -0.05641023461996861,
        "quantile_99": 0.04615946884307725,
        "hill_tail_index": 2.5665494049582676
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019335744161096194,
        "excess_kurtosis": 11.971733201980385,
        "return_acf_1": -0.07491403081168424,
        "abs_return_acf_1": 0.4426896529292137,
        "abs_return_acf_5": 0.43611546498628584,
        "abs_return_acf_20": 0.2264881518554158,
        "quantile_01": -0.07031972790442527,
        "quantile_99": 0.05635981233476724,
        "hill_tail_index": 3.1218792362410084
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
Unseen state share: 0.017777777777777778
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
