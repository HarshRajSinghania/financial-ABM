# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27116
Run ID: `fad07788e925342dd8fbe8d040108c47fe357e121959ab8a3a563715e9f7fcc9`
Result fingerprint: `443a17d86e3724bbe79a520244eaf92fb0071fb07f4f7133c49e02e122c1e821`

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
    "equal_weight_sd": -0.6637089811394735,
    "equal_weight_raw": -9.955634717092103,
    "fixed_start_cap_weight_sd": -0.6846173409557614,
    "fixed_start_cap_weight_raw": -10.26926011433642,
    "end_cap_weight_sd": -0.6657733025229363,
    "end_cap_weight_raw": -9.986599537844041
  },
  "full_period_change": {
    "equal_weight_sd": -0.9898994573299482,
    "equal_weight_raw": -14.848491859949224
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9281564332684722,
    "inflation_mean_sd": 0.5763806216931217
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2654166666666698,
    "equal_weight_raw": 3.9812500000000473,
    "fixed_start_cap_weight_sd": 0.2586854494547309,
    "fixed_start_cap_weight_raw": 3.8802817418209625,
    "end_cap_weight_sd": 0.28073208661122534,
    "end_cap_weight_raw": 4.210981299168381
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7232142857142826,
      "change_raw": -10.848214285714239,
      "decay_adjusted_gain_sd": 0.22916666666666985
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6668253968253935,
      "change_raw": -10.002380952380904,
      "decay_adjusted_gain_sd": 0.2855555555555587
    },
    "small": {
      "count": 18,
      "change_sd": -0.6522332225340455,
      "change_raw": -9.783498338010682,
      "decay_adjusted_gain_sd": 0.261388888888892
    },
    "large_minus_small_sd": -0.07098106318023711,
    "large_minus_small_raw": -1.0647159477035566
  },
  "inflation": {
    "initial_mean_sd": 0.30733333333333335,
    "final_mean_sd": 0.5944999999999999,
    "mean_sd": 0.47548112683874555,
    "mean_absolute_raw_gap": 7.132216902581183,
    "final_absolute_raw_gap": 8.917499999999999,
    "mean_range_fraction": 0.07132216902581183
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.4066666666666667,
    "initial_wealth_share": 0.30755251448532583,
    "final_wealth_share": 0.42051907146280504
  },
  "pricing_slope": {
    "mean": -0.0027208429484293353,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.08441572489481594,
    "real_improvement_cost": 0.057990327371687196,
    "washing_cost": 0.026425397523128728,
    "fine_transfer": 0.012808909534379576,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.09722463442919552,
    "resource_cost_fraction_initial_cap": 0.002813857496493865,
    "private_net_outflow_fraction_initial_cap": 0.003240821147639851,
    "fine_transfer_fraction_initial_cap": 0.0004269636511459859,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003345826006833672,
    "unapplied_final_day_resource_cost": 0.0012957655910409637
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 94.32484303038994,
    "beneficial_raw_gain_per_resource_cost": 1414.8726454558491,
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
    "accrued_cost": 2.683109708853304,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.2930807673371727,
    "accrued_cost_fraction_initial_cap": 0.08943699029511014,
    "mean_contract_rate": 0.03769494723068582,
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
    "maximum_relative_cash_error": 1.691280727342981e-15,
    "maximum_absolute_share_error": 1.6653345369377348e-15,
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
      "minimum": -0.21822444967852972,
      "maximum": -0.0591921364889458,
      "mean": -0.14575905834233047,
      "median": -0.14983178236623473,
      "quantile_05": -0.21317471438323268,
      "quantile_95": -0.06903469682060297
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
      "minimum": 0.240329808148835,
      "maximum": 0.8321174512069766,
      "mean": 0.5939329163015302,
      "median": 0.6076050806849557,
      "quantile_05": 0.28208501130346864,
      "quantile_95": 0.7968464846793534
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
        "daily_volatility": 0.019487915472192377,
        "excess_kurtosis": 7.882361706344849,
        "return_acf_1": -0.17005308588640033,
        "abs_return_acf_1": 0.4288369772003296,
        "abs_return_acf_5": 0.37438358324158494,
        "abs_return_acf_20": 0.28889626534696355,
        "quantile_01": -0.06564312846147827,
        "quantile_99": 0.05318479914417287,
        "hill_tail_index": 3.2203086798023275
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020662254123199122,
        "excess_kurtosis": 10.444091157961147,
        "return_acf_1": -0.14934291621490212,
        "abs_return_acf_1": 0.4596092631544288,
        "abs_return_acf_5": 0.4227465221984479,
        "abs_return_acf_20": 0.26529840185904496,
        "quantile_01": -0.08176843899054169,
        "quantile_99": 0.05449752909340042,
        "hill_tail_index": 2.983198878050858
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020855312693618334,
        "excess_kurtosis": 9.381291887018646,
        "return_acf_1": -0.21822444967852972,
        "abs_return_acf_1": 0.3890355489618582,
        "abs_return_acf_5": 0.2896766085482792,
        "abs_return_acf_20": 0.29546988769154725,
        "quantile_01": -0.07309540563951462,
        "quantile_99": 0.05717851245266937,
        "hill_tail_index": 2.838850730276641
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019472730383311064,
        "excess_kurtosis": 8.160214401355859,
        "return_acf_1": -0.11657742972311319,
        "abs_return_acf_1": 0.33722360940654705,
        "abs_return_acf_5": 0.41720179855491835,
        "abs_return_acf_20": 0.35661279713322735,
        "quantile_01": -0.06743057192427394,
        "quantile_99": 0.05091611685128301,
        "hill_tail_index": 2.6414908486112263
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024036996446364426,
        "excess_kurtosis": 15.534712082837814,
        "return_acf_1": -0.1877316734661209,
        "abs_return_acf_1": 0.466995943122591,
        "abs_return_acf_5": 0.44794508674378586,
        "abs_return_acf_20": 0.30985224529936833,
        "quantile_01": -0.09903442574577812,
        "quantile_99": 0.06401833366613187,
        "hill_tail_index": 2.6960824117941726
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022608972961721725,
        "excess_kurtosis": 13.491855292317197,
        "return_acf_1": -0.1689426605169519,
        "abs_return_acf_1": 0.4528793861430939,
        "abs_return_acf_5": 0.44172069346635195,
        "abs_return_acf_20": 0.33718225637594645,
        "quantile_01": -0.07764902096876632,
        "quantile_99": 0.06437038218295973,
        "hill_tail_index": 2.411730229444629
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018822988748975148,
        "excess_kurtosis": 7.6216259729137406,
        "return_acf_1": -0.1254732290780263,
        "abs_return_acf_1": 0.40446495597096027,
        "abs_return_acf_5": 0.3451945900217073,
        "abs_return_acf_20": 0.2731727784988401,
        "quantile_01": -0.06051093129676345,
        "quantile_99": 0.050723591168068856,
        "hill_tail_index": 3.592344967581115
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020945842311221343,
        "excess_kurtosis": 5.244322615943933,
        "return_acf_1": -0.0674201833293282,
        "abs_return_acf_1": 0.31847263426210143,
        "abs_return_acf_5": 0.28845556263569205,
        "abs_return_acf_20": 0.31231547033875356,
        "quantile_01": -0.06311789445741152,
        "quantile_99": 0.06702054236376419,
        "hill_tail_index": 6.179166582355832
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022503338639058065,
        "excess_kurtosis": 14.997871368848617,
        "return_acf_1": -0.21447473395268277,
        "abs_return_acf_1": 0.512691212991984,
        "abs_return_acf_5": 0.460957321522812,
        "abs_return_acf_20": 0.2449830884275917,
        "quantile_01": -0.08045608765638713,
        "quantile_99": 0.05426696067217171,
        "hill_tail_index": 2.1727016166871738
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019860430513435962,
        "excess_kurtosis": 4.808184062772278,
        "return_acf_1": -0.11267308809299133,
        "abs_return_acf_1": 0.3293800283415348,
        "abs_return_acf_5": 0.3403935016817338,
        "abs_return_acf_20": 0.3383307754311246,
        "quantile_01": -0.05730149696161612,
        "quantile_99": 0.04807607900054235,
        "hill_tail_index": 3.7044735240467093
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01870421758377498,
        "excess_kurtosis": 3.0991156405158353,
        "return_acf_1": -0.10790674921418035,
        "abs_return_acf_1": 0.33539843045456247,
        "abs_return_acf_5": 0.28038597011414285,
        "abs_return_acf_20": 0.219402188158079,
        "quantile_01": -0.059051993780773346,
        "quantile_99": 0.049371700883028384,
        "hill_tail_index": 4.388602667584391
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020202832246684867,
        "excess_kurtosis": 6.083851031524928,
        "return_acf_1": -0.14894709339908294,
        "abs_return_acf_1": 0.40179175203004,
        "abs_return_acf_5": 0.34611439663435223,
        "abs_return_acf_20": 0.30366187922634963,
        "quantile_01": -0.07437758068222304,
        "quantile_99": 0.05270537327556453,
        "hill_tail_index": 3.477124415208428
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022916812507765432,
        "excess_kurtosis": 13.225346975950544,
        "return_acf_1": -0.1686974335019816,
        "abs_return_acf_1": 0.4710948045201634,
        "abs_return_acf_5": 0.4700013234838759,
        "abs_return_acf_20": 0.28540176725819677,
        "quantile_01": -0.08177883401214471,
        "quantile_99": 0.06200845516915297,
        "hill_tail_index": 3.087169518984268
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023812258185749273,
        "excess_kurtosis": 12.268870008796972,
        "return_acf_1": -0.21158580157612705,
        "abs_return_acf_1": 0.5015587044511423,
        "abs_return_acf_5": 0.45314530086315247,
        "abs_return_acf_20": 0.33360993472274647,
        "quantile_01": -0.098221745902217,
        "quantile_99": 0.07267679113455754,
        "hill_tail_index": 3.360928669869817
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02232911141891177,
        "excess_kurtosis": 14.05391465186328,
        "return_acf_1": -0.1598395152055353,
        "abs_return_acf_1": 0.4755000892194531,
        "abs_return_acf_5": 0.472165531545803,
        "abs_return_acf_20": 0.2944377258426322,
        "quantile_01": -0.07924567965283465,
        "quantile_99": 0.059582433826135615,
        "hill_tail_index": 2.2564046666939777
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02165100947456358,
        "excess_kurtosis": 9.816414200535503,
        "return_acf_1": -0.19729088638173878,
        "abs_return_acf_1": 0.4484794867335851,
        "abs_return_acf_5": 0.46431650215806003,
        "abs_return_acf_20": 0.2652220726126514,
        "quantile_01": -0.0808015787329838,
        "quantile_99": 0.060129257134170985,
        "hill_tail_index": 2.353876272475436
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.0226820721179074,
        "excess_kurtosis": 12.597687825378067,
        "return_acf_1": -0.15855436789499766,
        "abs_return_acf_1": 0.458654286607528,
        "abs_return_acf_5": 0.48510523894194046,
        "abs_return_acf_20": 0.28350875154947913,
        "quantile_01": -0.08295024683512335,
        "quantile_99": 0.05515402932016877,
        "hill_tail_index": 2.8136417888672214
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021620735179498363,
        "excess_kurtosis": 10.902300196264196,
        "return_acf_1": -0.15771629325144784,
        "abs_return_acf_1": 0.42511851239536697,
        "abs_return_acf_5": 0.42021580352992266,
        "abs_return_acf_20": 0.3860239114703211,
        "quantile_01": -0.07612561070673672,
        "quantile_99": 0.0571811203515035,
        "hill_tail_index": 2.609968683785715
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02337550788010497,
        "excess_kurtosis": 15.398718158146803,
        "return_acf_1": -0.109918184962262,
        "abs_return_acf_1": 0.4607015605501707,
        "abs_return_acf_5": 0.4754650076449927,
        "abs_return_acf_20": 0.29483225968761856,
        "quantile_01": -0.08979163201428676,
        "quantile_99": 0.08072473614990353,
        "hill_tail_index": 3.663424762913273
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021684713616237885,
        "excess_kurtosis": 12.033089515644976,
        "return_acf_1": -0.12433265840273819,
        "abs_return_acf_1": 0.45492309847303963,
        "abs_return_acf_5": 0.41621500735141637,
        "abs_return_acf_20": 0.2542910796347454,
        "quantile_01": -0.07838019719376375,
        "quantile_99": 0.05416595340342686,
        "hill_tail_index": 3.2263981851997436
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021072228638729443,
        "excess_kurtosis": 9.357651506328315,
        "return_acf_1": -0.1528199535751147,
        "abs_return_acf_1": 0.40263400546598016,
        "abs_return_acf_5": 0.41938110712134646,
        "abs_return_acf_20": 0.26401988973397306,
        "quantile_01": -0.06915289602511873,
        "quantile_99": 0.05794909100647152,
        "hill_tail_index": 2.791240314251908
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02167826409823156,
        "excess_kurtosis": 10.698835107218947,
        "return_acf_1": -0.1929054176891926,
        "abs_return_acf_1": 0.49543815264997054,
        "abs_return_acf_5": 0.41502217340923175,
        "abs_return_acf_20": 0.32606028352313216,
        "quantile_01": -0.07597503747657529,
        "quantile_99": 0.06795982445990215,
        "hill_tail_index": 3.4655933428264594
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022350268950879153,
        "excess_kurtosis": 11.057904799033125,
        "return_acf_1": -0.13460267959334138,
        "abs_return_acf_1": 0.4778175677816607,
        "abs_return_acf_5": 0.4689721428747539,
        "abs_return_acf_20": 0.30724714038848105,
        "quantile_01": -0.07913701569098855,
        "quantile_99": 0.06636162619613319,
        "hill_tail_index": 3.874360072477864
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02408462421240519,
        "excess_kurtosis": 20.64251520868085,
        "return_acf_1": -0.14624959251589661,
        "abs_return_acf_1": 0.509609209771753,
        "abs_return_acf_5": 0.43275687052407363,
        "abs_return_acf_20": 0.3186407782915909,
        "quantile_01": -0.07702035493353789,
        "quantile_99": 0.0627170461946796,
        "hill_tail_index": 2.469916958693439
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020298019996781155,
        "excess_kurtosis": 4.359937211588564,
        "return_acf_1": -0.07100799108771656,
        "abs_return_acf_1": 0.30039214123335184,
        "abs_return_acf_5": 0.30345651610686514,
        "abs_return_acf_20": 0.2577582529342871,
        "quantile_01": -0.053518557907279225,
        "quantile_99": 0.06247363218728418,
        "hill_tail_index": 3.9496767057008744
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022064210557618966,
        "excess_kurtosis": 9.348144166144094,
        "return_acf_1": -0.08380818132536168,
        "abs_return_acf_1": 0.37656802567734526,
        "abs_return_acf_5": 0.44322378853842664,
        "abs_return_acf_20": 0.2782532993267876,
        "quantile_01": -0.07710940730715349,
        "quantile_99": 0.06263060832352925,
        "hill_tail_index": 3.097598147560656
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02134610475861248,
        "excess_kurtosis": 10.347074995623949,
        "return_acf_1": -0.18069504916523654,
        "abs_return_acf_1": 0.41573609494070723,
        "abs_return_acf_5": 0.44178584358415807,
        "abs_return_acf_20": 0.35570229230910905,
        "quantile_01": -0.07158311398955382,
        "quantile_99": 0.05672044071766445,
        "hill_tail_index": 3.76819863427948
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020797615927982363,
        "excess_kurtosis": 14.088538162161257,
        "return_acf_1": -0.12546766658240227,
        "abs_return_acf_1": 0.42600139537085735,
        "abs_return_acf_5": 0.4694842624704232,
        "abs_return_acf_20": 0.25527533735429486,
        "quantile_01": -0.062313384975654446,
        "quantile_99": 0.06473117459734254,
        "hill_tail_index": 2.6121667038325693
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019535227574209814,
        "excess_kurtosis": 6.661094026836281,
        "return_acf_1": -0.0591921364889458,
        "abs_return_acf_1": 0.36809459000209804,
        "abs_return_acf_5": 0.2929016317634099,
        "abs_return_acf_20": 0.24892349963552712,
        "quantile_01": -0.05605480781141405,
        "quantile_99": 0.06181438737478673,
        "hill_tail_index": 2.8317172125420114
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01862346102752183,
        "excess_kurtosis": 5.367746394739761,
        "return_acf_1": -0.15032064851756732,
        "abs_return_acf_1": 0.410076366588261,
        "abs_return_acf_5": 0.3608692717737246,
        "abs_return_acf_20": 0.33067599293768796,
        "quantile_01": -0.05548127696706933,
        "quantile_99": 0.05705986391946857,
        "hill_tail_index": 3.755717037467912
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
