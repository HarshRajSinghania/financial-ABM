# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27012
Run ID: `e46ad54795fad49ee2f3d25b8a6875d77a0f48f7f4a0088f47e614b75aaaced3`
Result fingerprint: `2dd833b2a3382894e35ba443a8b6e095ddb4ecf20f9a959c1b52f8bd1bbf6459`

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
    "equal_weight_sd": -0.5461309523809491,
    "equal_weight_raw": -8.191964285714239,
    "fixed_start_cap_weight_sd": -0.5644925993802239,
    "fixed_start_cap_weight_raw": -8.467388990703359,
    "end_cap_weight_sd": -0.5605388251206258,
    "end_cap_weight_raw": -8.408082376809382
  },
  "full_period_change": {
    "equal_weight_sd": -0.8256547619047571,
    "equal_weight_raw": -12.384821428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7849037698412653,
    "inflation_mean_sd": 0.5696200396825396
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3980111823005766,
    "equal_weight_raw": 5.970167734508648,
    "fixed_start_cap_weight_sd": 0.38399175384848383,
    "fixed_start_cap_weight_raw": 5.759876307727256,
    "end_cap_weight_sd": 0.3877262408798662,
    "end_cap_weight_raw": 5.815893613197994
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6265476190476159,
      "change_raw": -9.39821428571424,
      "decay_adjusted_gain_sd": 0.3258333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.610158730158727,
      "change_raw": -9.152380952380906,
      "decay_adjusted_gain_sd": 0.3422222222222253
    },
    "small": {
      "count": 18,
      "change_sd": -0.5007142857142824,
      "change_raw": -7.510714285714236,
      "decay_adjusted_gain_sd": 0.4379353038342921
    },
    "large_minus_small_sd": -0.12583333333333346,
    "large_minus_small_raw": -1.887500000000002
  },
  "inflation": {
    "initial_mean_sd": 0.23783333333333337,
    "final_mean_sd": 0.6083333333333333,
    "mean_sd": 0.4286733277824036,
    "mean_absolute_raw_gap": 6.4300999167360535,
    "final_absolute_raw_gap": 9.124999999999998,
    "mean_range_fraction": 0.06430099916736054
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.28,
    "initial_wealth_share": 0.24425469205264652,
    "final_wealth_share": 0.3621817140309455
  },
  "pricing_slope": {
    "mean": 0.00018334105476529777,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.11386574681036685,
    "real_improvement_cost": 0.09388905187434328,
    "washing_cost": 0.019976694936023588,
    "fine_transfer": 0.010617064164748488,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12448281097511533,
    "resource_cost_fraction_initial_cap": 0.003795524893678896,
    "private_net_outflow_fraction_initial_cap": 0.004149427032503846,
    "fine_transfer_fraction_initial_cap": 0.0003539021388249497,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007113882392490018,
    "unapplied_final_day_resource_cost": 0.013332976369307104
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 104.86327805764846,
    "beneficial_raw_gain_per_resource_cost": 1572.949170864727,
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
    "accrued_cost": 2.9027644968104998,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.07342597937997619,
    "accrued_cost_fraction_initial_cap": 0.09675881656035001,
    "mean_contract_rate": 0.04068494864745653,
    "maximum_ledger_error": 7.623296525288703e-20
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
    "price_cap_hits": 9,
    "maximum_relative_cash_error": 1.83628092720666e-15,
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
      "minimum": -0.3421362633585045,
      "maximum": -0.05563819402185508,
      "mean": -0.17219223391863,
      "median": -0.16872228925290314,
      "quantile_05": -0.27419731500208555,
      "quantile_95": -0.09479683521091706
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
      "minimum": 0.12667033010775744,
      "maximum": 0.8340008089322317,
      "mean": 0.6674410759111944,
      "median": 0.7291629167882187,
      "quantile_05": 0.22714487334314307,
      "quantile_95": 0.8099228010654539
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
        "daily_volatility": 0.023957142950218363,
        "excess_kurtosis": 25.08144518009615,
        "return_acf_1": -0.17855857651853355,
        "abs_return_acf_1": 0.45175847372655636,
        "abs_return_acf_5": 0.38409998585492655,
        "abs_return_acf_20": 0.2690523357816017,
        "quantile_01": -0.08191830394597076,
        "quantile_99": 0.06373157551093094,
        "hill_tail_index": 2.2745814968888256
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02212005628601574,
        "excess_kurtosis": 13.743121965315318,
        "return_acf_1": -0.20875676391952952,
        "abs_return_acf_1": 0.44351969774646993,
        "abs_return_acf_5": 0.3931634003092863,
        "abs_return_acf_20": 0.33486448180565315,
        "quantile_01": -0.06498608808247279,
        "quantile_99": 0.05871132602905127,
        "hill_tail_index": 2.56351013640858
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02295110538422858,
        "excess_kurtosis": 28.117874328664016,
        "return_acf_1": -0.16774749891221125,
        "abs_return_acf_1": 0.4323298864228807,
        "abs_return_acf_5": 0.351131705175062,
        "abs_return_acf_20": 0.36544470701162746,
        "quantile_01": -0.06977893866100253,
        "quantile_99": 0.05102022429582557,
        "hill_tail_index": 1.8101252355414241
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.023030989688122293,
        "excess_kurtosis": 21.350379910388998,
        "return_acf_1": -0.19540313099777482,
        "abs_return_acf_1": 0.47671615919028887,
        "abs_return_acf_5": 0.4643751853651389,
        "abs_return_acf_20": 0.31678253548814617,
        "quantile_01": -0.06839469169782547,
        "quantile_99": 0.06199688445773364,
        "hill_tail_index": 2.4755194296947445
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021646950501570828,
        "excess_kurtosis": 26.909186232720696,
        "return_acf_1": -0.21433863346830456,
        "abs_return_acf_1": 0.3945622588060599,
        "abs_return_acf_5": 0.3470576047338597,
        "abs_return_acf_20": 0.2980237366269974,
        "quantile_01": -0.056363887559043487,
        "quantile_99": 0.05421998314032719,
        "hill_tail_index": 2.419494803527446
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02264503142241077,
        "excess_kurtosis": 22.810457821354305,
        "return_acf_1": -0.16969707959359503,
        "abs_return_acf_1": 0.33656371959776604,
        "abs_return_acf_5": 0.29813696495228487,
        "abs_return_acf_20": 0.20696225289230272,
        "quantile_01": -0.059241217162265915,
        "quantile_99": 0.059744720164325485,
        "hill_tail_index": 2.669981968193423
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.024430099771469854,
        "excess_kurtosis": 26.377581215563083,
        "return_acf_1": -0.1539920929131582,
        "abs_return_acf_1": 0.4679574142736226,
        "abs_return_acf_5": 0.5166004316719537,
        "abs_return_acf_20": 0.30527256551369136,
        "quantile_01": -0.07405733872836617,
        "quantile_99": 0.06158665597251735,
        "hill_tail_index": 2.5008330942386907
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02310344562133391,
        "excess_kurtosis": 28.38740282546223,
        "return_acf_1": -0.17700708496365178,
        "abs_return_acf_1": 0.37405395524241153,
        "abs_return_acf_5": 0.3927908628950094,
        "abs_return_acf_20": 0.27427761108359267,
        "quantile_01": -0.06340723594975425,
        "quantile_99": 0.058445151080460306,
        "hill_tail_index": 2.3256414141800335
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022978095192211955,
        "excess_kurtosis": 28.865654410169107,
        "return_acf_1": -0.09749636201558522,
        "abs_return_acf_1": 0.3677944712182307,
        "abs_return_acf_5": 0.352439269916507,
        "abs_return_acf_20": 0.22605423229418112,
        "quantile_01": -0.07341539245853856,
        "quantile_99": 0.05657207609920118,
        "hill_tail_index": 1.8959115485042128
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.025335401801732157,
        "excess_kurtosis": 24.17483299326981,
        "return_acf_1": -0.18685502221270045,
        "abs_return_acf_1": 0.424089263359175,
        "abs_return_acf_5": 0.4295961166590248,
        "abs_return_acf_20": 0.3710991665946618,
        "quantile_01": -0.07374398022461884,
        "quantile_99": 0.06589467979905655,
        "hill_tail_index": 2.3107210787185704
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02030932566743314,
        "excess_kurtosis": 10.177977913363163,
        "return_acf_1": -0.18212643894932184,
        "abs_return_acf_1": 0.3623959346929952,
        "abs_return_acf_5": 0.3904161204108966,
        "abs_return_acf_20": 0.26744949835951587,
        "quantile_01": -0.05345174649609112,
        "quantile_99": 0.05790598030812695,
        "hill_tail_index": 2.7105103624489457
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02388574462532209,
        "excess_kurtosis": 25.90240186118108,
        "return_acf_1": -0.3421362633585045,
        "abs_return_acf_1": 0.4535187678859365,
        "abs_return_acf_5": 0.42649934948355833,
        "abs_return_acf_20": 0.4407862306307183,
        "quantile_01": -0.07646370806102905,
        "quantile_99": 0.08274970098778715,
        "hill_tail_index": 2.8912387274073184
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022694275127576526,
        "excess_kurtosis": 22.747743927858675,
        "return_acf_1": -0.19113164236033806,
        "abs_return_acf_1": 0.4071311259251338,
        "abs_return_acf_5": 0.35277913706486075,
        "abs_return_acf_20": 0.26096152427107916,
        "quantile_01": -0.06393427820395958,
        "quantile_99": 0.04668834643944358,
        "hill_tail_index": 1.69556921441881
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022035598421778515,
        "excess_kurtosis": 35.227969348971584,
        "return_acf_1": -0.13428305902406254,
        "abs_return_acf_1": 0.4196578983251183,
        "abs_return_acf_5": 0.38247494754909434,
        "abs_return_acf_20": 0.24576734450020576,
        "quantile_01": -0.056439726172808895,
        "quantile_99": 0.04933980499145725,
        "hill_tail_index": 1.7118946221962315
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021251396758928804,
        "excess_kurtosis": 21.42099335685132,
        "return_acf_1": -0.05563819402185508,
        "abs_return_acf_1": 0.35574432086722974,
        "abs_return_acf_5": 0.3372382323161804,
        "abs_return_acf_20": 0.24535320607152447,
        "quantile_01": -0.05794161509722232,
        "quantile_99": 0.05586676811583803,
        "hill_tail_index": 2.540088215279722
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022068713769493032,
        "excess_kurtosis": 19.697443946306787,
        "return_acf_1": -0.12787382627164628,
        "abs_return_acf_1": 0.3690656041268616,
        "abs_return_acf_5": 0.36240231248321936,
        "abs_return_acf_20": 0.2667677452135382,
        "quantile_01": -0.06651500305611782,
        "quantile_99": 0.05914489556444037,
        "hill_tail_index": 2.786888694465896
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.0228879322208978,
        "excess_kurtosis": 29.658565744612538,
        "return_acf_1": -0.24389046425975924,
        "abs_return_acf_1": 0.3836297578880211,
        "abs_return_acf_5": 0.3652153309494331,
        "abs_return_acf_20": 0.2174624774006596,
        "quantile_01": -0.06605468237696915,
        "quantile_99": 0.05544186128051329,
        "hill_tail_index": 2.349087782856087
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02248951352991803,
        "excess_kurtosis": 22.329975841541966,
        "return_acf_1": -0.1561549655848925,
        "abs_return_acf_1": 0.43302126341506014,
        "abs_return_acf_5": 0.44634500796437043,
        "abs_return_acf_20": 0.18336463260138014,
        "quantile_01": -0.0729499800796202,
        "quantile_99": 0.05021417458091965,
        "hill_tail_index": 1.942390087894287
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02092728272109153,
        "excess_kurtosis": 5.914624073840917,
        "return_acf_1": -0.14725047174847286,
        "abs_return_acf_1": 0.30064065827311437,
        "abs_return_acf_5": 0.2603171163525751,
        "abs_return_acf_20": 0.29297825475494355,
        "quantile_01": -0.06352617128745859,
        "quantile_99": 0.05810753236829464,
        "hill_tail_index": 3.268360575881926
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02623668865405352,
        "excess_kurtosis": 36.61136564736687,
        "return_acf_1": -0.29899382924580714,
        "abs_return_acf_1": 0.42620948174193396,
        "abs_return_acf_5": 0.3466169589297968,
        "abs_return_acf_20": 0.4314065536831199,
        "quantile_01": -0.07890736801698058,
        "quantile_99": 0.083902707504529,
        "hill_tail_index": 2.5656831921650562
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02456193524312119,
        "excess_kurtosis": 20.634901879646506,
        "return_acf_1": -0.14901450855113926,
        "abs_return_acf_1": 0.4458465650674292,
        "abs_return_acf_5": 0.44260460421786313,
        "abs_return_acf_20": 0.2774964103269169,
        "quantile_01": -0.07916368786003992,
        "quantile_99": 0.05907095760413277,
        "hill_tail_index": 2.2932081757490876
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02117631132123225,
        "excess_kurtosis": 25.59455340426781,
        "return_acf_1": -0.13246905145427282,
        "abs_return_acf_1": 0.34869820714758176,
        "abs_return_acf_5": 0.3329544691270372,
        "abs_return_acf_20": 0.1673212201589863,
        "quantile_01": -0.05278863799917799,
        "quantile_99": 0.05560131649271573,
        "hill_tail_index": 2.065921285498066
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020312959351245257,
        "excess_kurtosis": 6.924658189495146,
        "return_acf_1": -0.20230331866836718,
        "abs_return_acf_1": 0.3693751412712949,
        "abs_return_acf_5": 0.286610968621259,
        "abs_return_acf_20": 0.2726784842483511,
        "quantile_01": -0.06027886663934168,
        "quantile_99": 0.05906699682808822,
        "hill_tail_index": 3.375848231336493
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022460357698922857,
        "excess_kurtosis": 34.91301185568312,
        "return_acf_1": -0.16127390891745302,
        "abs_return_acf_1": 0.39365038787108525,
        "abs_return_acf_5": 0.37380665700376126,
        "abs_return_acf_20": 0.24744401664112337,
        "quantile_01": -0.04932554872773028,
        "quantile_99": 0.050140357078013904,
        "hill_tail_index": 1.8137690695244204
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.024217739408828865,
        "excess_kurtosis": 25.2362427314711,
        "return_acf_1": -0.17331420478151102,
        "abs_return_acf_1": 0.4279218806789063,
        "abs_return_acf_5": 0.3949195663444401,
        "abs_return_acf_20": 0.2244770427080986,
        "quantile_01": -0.07623955409538231,
        "quantile_99": 0.05709235213004605,
        "hill_tail_index": 2.323074399795645
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021132173182461744,
        "excess_kurtosis": 21.68368037568324,
        "return_acf_1": -0.1401063796164266,
        "abs_return_acf_1": 0.2783646389674288,
        "abs_return_acf_5": 0.34125317447794457,
        "abs_return_acf_20": 0.22087789618470557,
        "quantile_01": -0.05278953763810448,
        "quantile_99": 0.06192090400301275,
        "hill_tail_index": 2.193036492820909
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02291554216407318,
        "excess_kurtosis": 18.0709304735767,
        "return_acf_1": -0.1599604331981148,
        "abs_return_acf_1": 0.36933978144359353,
        "abs_return_acf_5": 0.3539988005576898,
        "abs_return_acf_20": 0.2948438595907947,
        "quantile_01": -0.06786039852253249,
        "quantile_99": 0.05740724625846933,
        "hill_tail_index": 2.702735158261181
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022468866015330886,
        "excess_kurtosis": 27.95884791835648,
        "return_acf_1": -0.13751944077437758,
        "abs_return_acf_1": 0.35682204734459644,
        "abs_return_acf_5": 0.35809963539376577,
        "abs_return_acf_20": 0.26934764432639946,
        "quantile_01": -0.06947132313282546,
        "quantile_99": 0.05286919523007023,
        "hill_tail_index": 1.9359899595840293
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02374051433784747,
        "excess_kurtosis": 31.190070287242264,
        "return_acf_1": -0.09258813146164308,
        "abs_return_acf_1": 0.4487054729521097,
        "abs_return_acf_5": 0.4067874070235829,
        "abs_return_acf_20": 0.2581511989851418,
        "quantile_01": -0.07333933953307654,
        "quantile_99": 0.06085447908525118,
        "hill_tail_index": 1.921650229094652
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02175097102551408,
        "excess_kurtosis": 24.964041788732168,
        "return_acf_1": -0.1878862397958905,
        "abs_return_acf_1": 0.4022062848851571,
        "abs_return_acf_5": 0.448000555043845,
        "abs_return_acf_20": 0.16314425811904787,
        "quantile_01": -0.053209872408241876,
        "quantile_99": 0.05145990491302115,
        "hill_tail_index": 2.0119404478443563
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
Unseen state share: 0.0022222222222222222
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
