# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27231
Run ID: `518e28d96a9b99ad357c8bed8b73323c8a5ecafc8bf259aece52f94814de2d5a`
Result fingerprint: `a6cc4c9d723ff65b5dd008501670876694cf519cb1d6acc403c2c1533c9c92d8`

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
    "equal_weight_sd": -0.7062142857142825,
    "equal_weight_raw": -10.593214285714236,
    "fixed_start_cap_weight_sd": -0.6595463535241496,
    "fixed_start_cap_weight_raw": -9.893195302862244,
    "end_cap_weight_sd": -0.6673021624511652,
    "end_cap_weight_raw": -10.009532436767481
  },
  "full_period_change": {
    "equal_weight_sd": -1.0943214285714236,
    "equal_weight_raw": -16.414821428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0098832671957625,
    "inflation_mean_sd": 0.6509173280423279
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2413079906659954,
    "equal_weight_raw": 3.6196198599899305,
    "fixed_start_cap_weight_sd": 0.28009979971166615,
    "fixed_start_cap_weight_raw": 4.201496995674994,
    "end_cap_weight_sd": 0.270513622701935,
    "end_cap_weight_raw": 4.057704340529025
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.3940476190476154,
      "change_raw": -5.910714285714231,
      "decay_adjusted_gain_sd": 0.5097465733265915
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8568253968253935,
      "change_raw": -12.852380952380903,
      "decay_adjusted_gain_sd": 0.09555555555555875
    },
    "small": {
      "count": 18,
      "change_sd": -0.6829365079365046,
      "change_raw": -10.244047619047569,
      "decay_adjusted_gain_sd": 0.2694444444444477
    },
    "large_minus_small_sd": 0.2888888888888892,
    "large_minus_small_raw": 4.3333333333333375
  },
  "inflation": {
    "initial_mean_sd": 0.2791666666666667,
    "final_mean_sd": 0.67675,
    "mean_sd": 0.4689412295309464,
    "mean_absolute_raw_gap": 7.034118442964195,
    "final_absolute_raw_gap": 10.151250000000001,
    "mean_range_fraction": 0.07034118442964195
  },
  "impact": {
    "initial_share": 0.18666666666666668,
    "final_share": 0.25333333333333335,
    "initial_wealth_share": 0.17768241276033825,
    "final_wealth_share": 0.24196495483325128
  },
  "pricing_slope": {
    "mean": -0.0019502607083744,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.02039103796947972,
    "real_improvement_cost": 0.015880386573019604,
    "washing_cost": 0.004510651396460116,
    "fine_transfer": 0.010677299300442583,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0310683372699223,
    "resource_cost_fraction_initial_cap": 0.0006797012656493237,
    "private_net_outflow_fraction_initial_cap": 0.001035611242330743,
    "fine_transfer_fraction_initial_cap": 0.00035590997668141934,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00021287253941700528,
    "unapplied_final_day_resource_cost": 0.0004734763622568585
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 355.02065813497046,
    "beneficial_raw_gain_per_resource_cost": 5325.309872024557,
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
    "fixed_exposure": 15.000000000000005,
    "accrued_cost": 2.994065751689469,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.017875275498991455,
    "accrued_cost_fraction_initial_cap": 0.09980219172298226,
    "mean_contract_rate": 0.04171528306031084,
    "maximum_ledger_error": 4.0657581468206416e-20
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
    "maximum_relative_cash_error": 2.537266044447087e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.2446590351018009,
      "maximum": -0.12075068430888526,
      "mean": -0.18878246889806422,
      "median": -0.19413388499486678,
      "quantile_05": -0.23491070762370844,
      "quantile_95": -0.12670581824974583
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
      "minimum": 0.13798528965937476,
      "maximum": 0.822640291658425,
      "mean": 0.5978277261657517,
      "median": 0.6663833746073196,
      "quantile_05": 0.20573578749958724,
      "quantile_95": 0.7895799251214649
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
        "daily_volatility": 0.023895196731306943,
        "excess_kurtosis": 10.203235071867994,
        "return_acf_1": -0.1248367808300354,
        "abs_return_acf_1": 0.4057782153989276,
        "abs_return_acf_5": 0.4494263790495838,
        "abs_return_acf_20": 0.2874391008411594,
        "quantile_01": -0.08816058552190278,
        "quantile_99": 0.07698071149585617,
        "hill_tail_index": 5.12441020314853
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02127628386067276,
        "excess_kurtosis": 5.569874172578277,
        "return_acf_1": -0.20026289444605175,
        "abs_return_acf_1": 0.3677179943916188,
        "abs_return_acf_5": 0.33849732488836154,
        "abs_return_acf_20": 0.2002225151815551,
        "quantile_01": -0.07785604945025396,
        "quantile_99": 0.05510182665709877,
        "hill_tail_index": 3.647911045971201
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02399295108576283,
        "excess_kurtosis": 7.357416389992942,
        "return_acf_1": -0.19438087248210717,
        "abs_return_acf_1": 0.3078013951212637,
        "abs_return_acf_5": 0.29793666161385496,
        "abs_return_acf_20": 0.26634524376109586,
        "quantile_01": -0.07439939550715644,
        "quantile_99": 0.06928502498944548,
        "hill_tail_index": 3.525529554892197
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02378907661844405,
        "excess_kurtosis": 8.93753488677379,
        "return_acf_1": -0.1903158349378112,
        "abs_return_acf_1": 0.4409663128889428,
        "abs_return_acf_5": 0.38531461004120227,
        "abs_return_acf_20": 0.3216253099687589,
        "quantile_01": -0.08842920918207983,
        "quantile_99": 0.06261962086383716,
        "hill_tail_index": 3.298225527847763
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01938099585913778,
        "excess_kurtosis": 8.353079588897062,
        "return_acf_1": -0.19762913935881052,
        "abs_return_acf_1": 0.30938222198099474,
        "abs_return_acf_5": 0.25241356893082967,
        "abs_return_acf_20": 0.22818965284488119,
        "quantile_01": -0.06805193956548382,
        "quantile_99": 0.0472500661518368,
        "hill_tail_index": 4.000116139267603
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020191903947214977,
        "excess_kurtosis": 4.433539394389427,
        "return_acf_1": -0.226752131008841,
        "abs_return_acf_1": 0.3188258729164803,
        "abs_return_acf_5": 0.30558022011601627,
        "abs_return_acf_20": 0.19129459548837932,
        "quantile_01": -0.07258643838612751,
        "quantile_99": 0.053608136989632404,
        "hill_tail_index": 4.554606236245132
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02216061367480037,
        "excess_kurtosis": 6.993868925744154,
        "return_acf_1": -0.16747420085451187,
        "abs_return_acf_1": 0.4192410448216506,
        "abs_return_acf_5": 0.35311294670724913,
        "abs_return_acf_20": 0.24363317245623403,
        "quantile_01": -0.08168461755287186,
        "quantile_99": 0.06071291294503816,
        "hill_tail_index": 4.178973200608869
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.024631021933614564,
        "excess_kurtosis": 20.1632523561301,
        "return_acf_1": -0.19388689750762642,
        "abs_return_acf_1": 0.3494751356625348,
        "abs_return_acf_5": 0.322330887861237,
        "abs_return_acf_20": 0.26834328895541115,
        "quantile_01": -0.08536197163128004,
        "quantile_99": 0.05853893974582215,
        "hill_tail_index": 2.335167830645535
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022544446809887417,
        "excess_kurtosis": 6.374488983895986,
        "return_acf_1": -0.2261518884372607,
        "abs_return_acf_1": 0.3913679729671369,
        "abs_return_acf_5": 0.3541389636748066,
        "abs_return_acf_20": 0.28081827023980516,
        "quantile_01": -0.08130760154867542,
        "quantile_99": 0.06056180322464742,
        "hill_tail_index": 3.591233939276285
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022244882894540248,
        "excess_kurtosis": 8.224429174043223,
        "return_acf_1": -0.2227310488124724,
        "abs_return_acf_1": 0.39847810554368607,
        "abs_return_acf_5": 0.3099950091557685,
        "abs_return_acf_20": 0.3013163431625493,
        "quantile_01": -0.08265879486992601,
        "quantile_99": 0.058428283466142,
        "hill_tail_index": 2.6505800464924705
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02306407894604078,
        "excess_kurtosis": 7.050579795396429,
        "return_acf_1": -0.17325240178949716,
        "abs_return_acf_1": 0.3561713038522761,
        "abs_return_acf_5": 0.4037552361349142,
        "abs_return_acf_20": 0.28623449488374364,
        "quantile_01": -0.0830743842749947,
        "quantile_99": 0.06845888792739935,
        "hill_tail_index": 4.331501357036212
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021497668305425995,
        "excess_kurtosis": 9.287912314122542,
        "return_acf_1": -0.17982668600441137,
        "abs_return_acf_1": 0.30740896284883,
        "abs_return_acf_5": 0.3677893058630595,
        "abs_return_acf_20": 0.24474296038704182,
        "quantile_01": -0.07999562840469544,
        "quantile_99": 0.056512647898548804,
        "hill_tail_index": 3.081988090717472
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02161580755049808,
        "excess_kurtosis": 10.301309454547203,
        "return_acf_1": -0.13449968397326825,
        "abs_return_acf_1": 0.24335794011716133,
        "abs_return_acf_5": 0.28321596600440113,
        "abs_return_acf_20": 0.23480220205995153,
        "quantile_01": -0.06338539132176431,
        "quantile_99": 0.05732959646053105,
        "hill_tail_index": 2.547573841109579
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02433048563400571,
        "excess_kurtosis": 11.718889249040961,
        "return_acf_1": -0.20744265463665437,
        "abs_return_acf_1": 0.4281948810668275,
        "abs_return_acf_5": 0.3995888060933164,
        "abs_return_acf_20": 0.2923544223853228,
        "quantile_01": -0.09648646855779101,
        "quantile_99": 0.07064382982689099,
        "hill_tail_index": 3.0840253817649477
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021828793513523903,
        "excess_kurtosis": 5.564029886756732,
        "return_acf_1": -0.17730266051575386,
        "abs_return_acf_1": 0.36708540929424927,
        "abs_return_acf_5": 0.3769351409996255,
        "abs_return_acf_20": 0.28584128303179973,
        "quantile_01": -0.0785059073520482,
        "quantile_99": 0.06154597740082994,
        "hill_tail_index": 4.678391555565346
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022172752317693452,
        "excess_kurtosis": 5.958814927535212,
        "return_acf_1": -0.21336310153905655,
        "abs_return_acf_1": 0.33876779696054565,
        "abs_return_acf_5": 0.3367401126550536,
        "abs_return_acf_20": 0.2478300673941132,
        "quantile_01": -0.08430696761710847,
        "quantile_99": 0.056305210125891854,
        "hill_tail_index": 3.05943184246273
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02350825622536988,
        "excess_kurtosis": 9.220361617149749,
        "return_acf_1": -0.19906080298593407,
        "abs_return_acf_1": 0.3908131147372368,
        "abs_return_acf_5": 0.4012869270026986,
        "abs_return_acf_20": 0.26374696556687305,
        "quantile_01": -0.08571486172490515,
        "quantile_99": 0.060892337251608177,
        "hill_tail_index": 3.351791895504244
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021024986443104726,
        "excess_kurtosis": 7.688497226262072,
        "return_acf_1": -0.2161823702755084,
        "abs_return_acf_1": 0.3234102903373989,
        "abs_return_acf_5": 0.2815286014888936,
        "abs_return_acf_20": 0.1791527711961818,
        "quantile_01": -0.06679343913597673,
        "quantile_99": 0.05529890184964498,
        "hill_tail_index": 3.567167178814331
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02304104227486847,
        "excess_kurtosis": 9.402560939317135,
        "return_acf_1": -0.164703934763381,
        "abs_return_acf_1": 0.4089321360802945,
        "abs_return_acf_5": 0.36632011805761466,
        "abs_return_acf_20": 0.27518055497088023,
        "quantile_01": -0.08175674519048474,
        "quantile_99": 0.06684692761864942,
        "hill_tail_index": 3.852960420220642
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02339222730168015,
        "excess_kurtosis": 10.115537545266656,
        "return_acf_1": -0.16676019490605512,
        "abs_return_acf_1": 0.4323902553142616,
        "abs_return_acf_5": 0.4125260866483981,
        "abs_return_acf_20": 0.3252922509315338,
        "quantile_01": -0.08196993465281735,
        "quantile_99": 0.0662316749547129,
        "hill_tail_index": 3.2783907559306145
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02223854820559251,
        "excess_kurtosis": 10.541267967108237,
        "return_acf_1": -0.12899019731828076,
        "abs_return_acf_1": 0.39325962680451343,
        "abs_return_acf_5": 0.3853733301376211,
        "abs_return_acf_20": 0.3347698822862001,
        "quantile_01": -0.07607180817974357,
        "quantile_99": 0.07148695657913964,
        "hill_tail_index": 3.6532546506396857
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02283594536525381,
        "excess_kurtosis": 8.867458048011859,
        "return_acf_1": -0.21470747925573588,
        "abs_return_acf_1": 0.38399927407008244,
        "abs_return_acf_5": 0.4257154187091055,
        "abs_return_acf_20": 0.2964339491803942,
        "quantile_01": -0.08514077094359501,
        "quantile_99": 0.05661260560332203,
        "hill_tail_index": 2.7605149934597404
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024300509502474636,
        "excess_kurtosis": 7.591456232181754,
        "return_acf_1": -0.21623197433539101,
        "abs_return_acf_1": 0.3827872193563364,
        "abs_return_acf_5": 0.4083670738658361,
        "abs_return_acf_20": 0.28361007428530727,
        "quantile_01": -0.08128627817794368,
        "quantile_99": 0.07235139575523307,
        "hill_tail_index": 4.890346643515956
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020668773151806173,
        "excess_kurtosis": 3.523523396286749,
        "return_acf_1": -0.2446590351018009,
        "abs_return_acf_1": 0.2694054399415206,
        "abs_return_acf_5": 0.21016168005235414,
        "abs_return_acf_20": 0.24051178582050492,
        "quantile_01": -0.05932962293583278,
        "quantile_99": 0.061336526377389816,
        "hill_tail_index": 4.431768203661989
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.022089721489769676,
        "excess_kurtosis": 8.245137978032602,
        "return_acf_1": -0.24158590667223637,
        "abs_return_acf_1": 0.3672020608583887,
        "abs_return_acf_5": 0.31659905139872013,
        "abs_return_acf_20": 0.2704999839135049,
        "quantile_01": -0.07336045451193962,
        "quantile_99": 0.05265864129376197,
        "hill_tail_index": 3.3591305817184387
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.024401656377216564,
        "excess_kurtosis": 11.267984651845785,
        "return_acf_1": -0.1797368010256067,
        "abs_return_acf_1": 0.44821606115138574,
        "abs_return_acf_5": 0.39663056175474853,
        "abs_return_acf_20": 0.3111570033169736,
        "quantile_01": -0.09424293912099603,
        "quantile_99": 0.06851598530654306,
        "hill_tail_index": 3.535178033278035
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022451920277630842,
        "excess_kurtosis": 5.6101614705744005,
        "return_acf_1": -0.1469288835178937,
        "abs_return_acf_1": 0.4205347498843338,
        "abs_return_acf_5": 0.35525514713632117,
        "abs_return_acf_20": 0.28895796752087805,
        "quantile_01": -0.07763849432926168,
        "quantile_99": 0.06421126652936711,
        "hill_tail_index": 4.474550406915991
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02147897580296808,
        "excess_kurtosis": 4.234323671688165,
        "return_acf_1": -0.17601687064597005,
        "abs_return_acf_1": 0.32321344211654945,
        "abs_return_acf_5": 0.2843248776490771,
        "abs_return_acf_20": 0.22542284970857082,
        "quantile_01": -0.06077121596378771,
        "quantile_99": 0.06738052013236484,
        "hill_tail_index": 5.647447441525551
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023013244793405524,
        "excess_kurtosis": 10.457167613474903,
        "return_acf_1": -0.12075068430888526,
        "abs_return_acf_1": 0.3484920832974288,
        "abs_return_acf_5": 0.4267028284827198,
        "abs_return_acf_20": 0.27112921425912107,
        "quantile_01": -0.08664206883954355,
        "quantile_99": 0.0637682422763211,
        "hill_tail_index": 3.4212082320858226
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.024594098365977642,
        "excess_kurtosis": 9.915702961681625,
        "return_acf_1": -0.21705005469507724,
        "abs_return_acf_1": 0.44418720327915173,
        "abs_return_acf_5": 0.39879988191169163,
        "abs_return_acf_20": 0.31678566945041425,
        "quantile_01": -0.09072941359463049,
        "quantile_99": 0.06325730216522524,
        "hill_tail_index": 2.716998724491979
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
