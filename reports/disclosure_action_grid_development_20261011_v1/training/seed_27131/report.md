# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27131
Run ID: `1c3be72cf45fcaed2d24153a180e50f2fcc26803d5266727e02b7c16915fdc9e`
Result fingerprint: `5017d6f2f0884e12bb11d763bc1fbe1f75349bb494c7c2fff189d1ea7b811273`

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
    "equal_weight_sd": -0.6667976190476159,
    "equal_weight_raw": -10.001964285714239,
    "fixed_start_cap_weight_sd": -0.6898870069074823,
    "fixed_start_cap_weight_raw": -10.348305103612235,
    "end_cap_weight_sd": -0.6746646498393024,
    "end_cap_weight_raw": -10.119969747589534
  },
  "full_period_change": {
    "equal_weight_sd": -1.0737380952380904,
    "equal_weight_raw": -16.106071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0164193121693077,
    "inflation_mean_sd": 0.6445333994708995
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.28558333333333646,
    "equal_weight_raw": 4.283750000000047,
    "fixed_start_cap_weight_sd": 0.26249394547347005,
    "fixed_start_cap_weight_raw": 3.9374091821020514,
    "end_cap_weight_sd": 0.2777163025416498,
    "end_cap_weight_raw": 4.1657445381247475
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6407142857142823,
      "change_raw": -9.610714285714236,
      "decay_adjusted_gain_sd": 0.31166666666667003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6462698412698382,
      "change_raw": -9.694047619047574,
      "decay_adjusted_gain_sd": 0.3061111111111143
    },
    "small": {
      "count": 18,
      "change_sd": -0.681408730158727,
      "change_raw": -10.221130952380905,
      "decay_adjusted_gain_sd": 0.27097222222222533
    },
    "large_minus_small_sd": 0.0406944444444447,
    "large_minus_small_raw": 0.6104166666666705
  },
  "inflation": {
    "initial_mean_sd": 0.2819166666666667,
    "final_mean_sd": 0.655416666666667,
    "mean_sd": 0.5117808076602831,
    "mean_absolute_raw_gap": 7.676712114904246,
    "final_absolute_raw_gap": 9.83125,
    "mean_range_fraction": 0.07676712114904247
  },
  "impact": {
    "initial_share": 0.16,
    "final_share": 0.22,
    "initial_wealth_share": 0.162952658002663,
    "final_wealth_share": 0.2238911040416709
  },
  "pricing_slope": {
    "mean": -0.0013657418187413358,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.03698104521979835,
    "real_improvement_cost": 0.03176694748128342,
    "washing_cost": 0.005214097738514922,
    "fine_transfer": 0.003931748508415117,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.040912793728213465,
    "resource_cost_fraction_initial_cap": 0.0012327015073266116,
    "private_net_outflow_fraction_initial_cap": 0.0013637597909404487,
    "fine_transfer_fraction_initial_cap": 0.00013105828361383723,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0036512785603255004,
    "unapplied_final_day_resource_cost": 0.004501467219405541
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 231.67273799533808,
    "beneficial_raw_gain_per_resource_cost": 3475.0910699300716,
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
    "fixed_exposure": 15.000000000000002,
    "accrued_cost": 3.2634397304170517,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.28724925422657493,
    "accrued_cost_fraction_initial_cap": 0.10878132434723504,
    "mean_contract_rate": 0.04507859478931731,
    "maximum_ledger_error": 8.809142651444724e-20
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
    "maximum_relative_cash_error": 1.4755525961260601e-15,
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
      "minimum": -0.20038277264896545,
      "maximum": -0.08147713705805153,
      "mean": -0.14689547934384045,
      "median": -0.14798481038467043,
      "quantile_05": -0.19165537699874663,
      "quantile_95": -0.09559838198879532
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
      "minimum": 0.2911869846405733,
      "maximum": 0.780920484232595,
      "mean": 0.5904486737556077,
      "median": 0.5991123070507218,
      "quantile_05": 0.3708043754944405,
      "quantile_95": 0.7341094955209926
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
        "daily_volatility": 0.01770076501652099,
        "excess_kurtosis": 4.1286815230245715,
        "return_acf_1": -0.1412175307843228,
        "abs_return_acf_1": 0.2767995926358918,
        "abs_return_acf_5": 0.29709642035660555,
        "abs_return_acf_20": 0.20641690794243545,
        "quantile_01": -0.0468701632336588,
        "quantile_99": 0.046731884318289216,
        "hill_tail_index": 3.6284775076688383
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021869888292543823,
        "excess_kurtosis": 7.569636804603418,
        "return_acf_1": -0.101085008983232,
        "abs_return_acf_1": 0.4142879932351033,
        "abs_return_acf_5": 0.43174831779403444,
        "abs_return_acf_20": 0.3256328311449842,
        "quantile_01": -0.07403748269066174,
        "quantile_99": 0.0672849089551297,
        "hill_tail_index": 3.4447943158444887
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017936375652596648,
        "excess_kurtosis": 5.914999822697666,
        "return_acf_1": -0.12236810520208058,
        "abs_return_acf_1": 0.30702187791311253,
        "abs_return_acf_5": 0.2742772025781029,
        "abs_return_acf_20": 0.2644797737193402,
        "quantile_01": -0.05904131145734438,
        "quantile_99": 0.045412025944422174,
        "hill_tail_index": 3.8709880980244624
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02122622036080657,
        "excess_kurtosis": 11.536765152163513,
        "return_acf_1": -0.15873544838393977,
        "abs_return_acf_1": 0.42324758234163223,
        "abs_return_acf_5": 0.2618934727625954,
        "abs_return_acf_20": 0.2677780572947017,
        "quantile_01": -0.07173581377346144,
        "quantile_99": 0.053970891003567834,
        "hill_tail_index": 2.3571262062512366
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019143715824024105,
        "excess_kurtosis": 5.148272765505132,
        "return_acf_1": -0.17193715566289242,
        "abs_return_acf_1": 0.35038186008816236,
        "abs_return_acf_5": 0.30064833856335743,
        "abs_return_acf_20": 0.2471945925466431,
        "quantile_01": -0.05346268576557672,
        "quantile_99": 0.051202305262910884,
        "hill_tail_index": 3.2990046999935885
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020395057902826464,
        "excess_kurtosis": 5.302211530005017,
        "return_acf_1": -0.1745148335406041,
        "abs_return_acf_1": 0.4006973361336192,
        "abs_return_acf_5": 0.3592214344618225,
        "abs_return_acf_20": 0.2596100303727044,
        "quantile_01": -0.0658553657679891,
        "quantile_99": 0.06277971401922751,
        "hill_tail_index": 4.64510931421736
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019814521605214328,
        "excess_kurtosis": 8.045527471194827,
        "return_acf_1": -0.09110932353880162,
        "abs_return_acf_1": 0.327197263627359,
        "abs_return_acf_5": 0.3338988494510004,
        "abs_return_acf_20": 0.2898706636475849,
        "quantile_01": -0.06466646531398046,
        "quantile_99": 0.06250587029749781,
        "hill_tail_index": 3.2797784686414544
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020069267922608967,
        "excess_kurtosis": 8.437318803349692,
        "return_acf_1": -0.13626446581171664,
        "abs_return_acf_1": 0.42360964755571895,
        "abs_return_acf_5": 0.43883044815473043,
        "abs_return_acf_20": 0.251184647932193,
        "quantile_01": -0.07260729937003933,
        "quantile_99": 0.05244784464431141,
        "hill_tail_index": 3.042772726108703
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018118089723510176,
        "excess_kurtosis": 2.206703832219765,
        "return_acf_1": -0.13673288588160862,
        "abs_return_acf_1": 0.3087196294657252,
        "abs_return_acf_5": 0.2558986497400705,
        "abs_return_acf_20": 0.23007834620575432,
        "quantile_01": -0.053358991265037035,
        "quantile_99": 0.046740695557539944,
        "hill_tail_index": 5.307562801113815
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02259256462076582,
        "excess_kurtosis": 9.119928395774611,
        "return_acf_1": -0.15475208998501805,
        "abs_return_acf_1": 0.41926639783071906,
        "abs_return_acf_5": 0.42831422281335896,
        "abs_return_acf_20": 0.30739305808834005,
        "quantile_01": -0.08176344637527584,
        "quantile_99": 0.06594772862796455,
        "hill_tail_index": 2.9742109158704113
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020043271249251482,
        "excess_kurtosis": 7.617729132465872,
        "return_acf_1": -0.1725716043673338,
        "abs_return_acf_1": 0.3566315562598629,
        "abs_return_acf_5": 0.2860232032315704,
        "abs_return_acf_20": 0.30141216704654017,
        "quantile_01": -0.07020079419538802,
        "quantile_99": 0.05917986123119244,
        "hill_tail_index": 3.294326735336585
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018656841753272233,
        "excess_kurtosis": 6.397249354126808,
        "return_acf_1": -0.11176187411446038,
        "abs_return_acf_1": 0.42595497029976553,
        "abs_return_acf_5": 0.4062818260720198,
        "abs_return_acf_20": 0.28345216044997895,
        "quantile_01": -0.056364912578419135,
        "quantile_99": 0.05538141652200947,
        "hill_tail_index": 2.9343910104368836
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01914510440875647,
        "excess_kurtosis": 6.848473779691005,
        "return_acf_1": -0.11584600989860441,
        "abs_return_acf_1": 0.3747386339957334,
        "abs_return_acf_5": 0.36881502703484903,
        "abs_return_acf_20": 0.30688004748669634,
        "quantile_01": -0.05897236609388851,
        "quantile_99": 0.052532767301561915,
        "hill_tail_index": 3.334065876442439
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019598031483890645,
        "excess_kurtosis": 10.148534160242464,
        "return_acf_1": -0.18119846934647665,
        "abs_return_acf_1": 0.31185734786636365,
        "abs_return_acf_5": 0.28335054006635,
        "abs_return_acf_20": 0.2628398244947117,
        "quantile_01": -0.06349213881834895,
        "quantile_99": 0.05740924305461674,
        "hill_tail_index": 2.45439728133526
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021609653366298567,
        "excess_kurtosis": 11.474759983350598,
        "return_acf_1": -0.12473802705106327,
        "abs_return_acf_1": 0.42527395062464035,
        "abs_return_acf_5": 0.3974106666885265,
        "abs_return_acf_20": 0.30161883410766593,
        "quantile_01": -0.07874014631725021,
        "quantile_99": 0.06082945421687431,
        "hill_tail_index": 3.6122716202451026
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020041750646616667,
        "excess_kurtosis": 4.6603494367467375,
        "return_acf_1": -0.1937545220006477,
        "abs_return_acf_1": 0.4258257078089676,
        "abs_return_acf_5": 0.4024470735080695,
        "abs_return_acf_20": 0.34077094055816043,
        "quantile_01": -0.06626870195316092,
        "quantile_99": 0.06429467940557936,
        "hill_tail_index": 4.516452127178708
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021084540805456166,
        "excess_kurtosis": 6.478635114935871,
        "return_acf_1": -0.10944609921162932,
        "abs_return_acf_1": 0.3996100637780373,
        "abs_return_acf_5": 0.30135313163373356,
        "abs_return_acf_20": 0.32942975563999977,
        "quantile_01": -0.06787560747891364,
        "quantile_99": 0.05703434833909102,
        "hill_tail_index": 3.532448925157902
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018132301109794406,
        "excess_kurtosis": 5.3962053769382585,
        "return_acf_1": -0.17101483617224372,
        "abs_return_acf_1": 0.34263348062629945,
        "abs_return_acf_5": 0.20470464344452174,
        "abs_return_acf_20": 0.20879388175703537,
        "quantile_01": -0.061656338895225295,
        "quantile_99": 0.05154829467744474,
        "hill_tail_index": 3.5238355692183827
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01938169195392026,
        "excess_kurtosis": 7.767346810012073,
        "return_acf_1": -0.16219950417404494,
        "abs_return_acf_1": 0.400152426394454,
        "abs_return_acf_5": 0.32692916983445786,
        "abs_return_acf_20": 0.2217364196165501,
        "quantile_01": -0.0628647839295214,
        "quantile_99": 0.05852047897078173,
        "hill_tail_index": 3.349969609296093
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020009113851497645,
        "excess_kurtosis": 7.460839862738791,
        "return_acf_1": -0.08147713705805153,
        "abs_return_acf_1": 0.3339825976475237,
        "abs_return_acf_5": 0.34792452677327756,
        "abs_return_acf_20": 0.23306260116974203,
        "quantile_01": -0.06752804307977274,
        "quantile_99": 0.05768762497959593,
        "hill_tail_index": 3.3812659846440094
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016278256194232767,
        "excess_kurtosis": 2.450374575502039,
        "return_acf_1": -0.18908975532975644,
        "abs_return_acf_1": 0.17644505669142313,
        "abs_return_acf_5": 0.20647993485464297,
        "abs_return_acf_20": 0.06028120249003547,
        "quantile_01": -0.042116485102698324,
        "quantile_99": 0.03811536983093028,
        "hill_tail_index": 3.626165464950992
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019799799924183493,
        "excess_kurtosis": 9.851288277105896,
        "return_acf_1": -0.17658496472386068,
        "abs_return_acf_1": 0.4187188734382885,
        "abs_return_acf_5": 0.4175243279906975,
        "abs_return_acf_20": 0.31011007069900104,
        "quantile_01": -0.07803511440061833,
        "quantile_99": 0.05236633777025038,
        "hill_tail_index": 2.486542674976999
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017668395906482847,
        "excess_kurtosis": 7.4076415141963565,
        "return_acf_1": -0.20038277264896545,
        "abs_return_acf_1": 0.33830179177479797,
        "abs_return_acf_5": 0.27414976840548927,
        "abs_return_acf_20": 0.24775371806065694,
        "quantile_01": -0.04823104398250544,
        "quantile_99": 0.04041485974578229,
        "hill_tail_index": 3.28437034253461
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019399103831058237,
        "excess_kurtosis": 6.107945543030702,
        "return_acf_1": -0.13786807369030343,
        "abs_return_acf_1": 0.4037097473498933,
        "abs_return_acf_5": 0.38809522004925207,
        "abs_return_acf_20": 0.2608725574207663,
        "quantile_01": -0.06147074073417393,
        "quantile_99": 0.053002192300280214,
        "hill_tail_index": 3.5307789266178853
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018265403727227895,
        "excess_kurtosis": 7.52627734168925,
        "return_acf_1": -0.16265275322214123,
        "abs_return_acf_1": 0.3625282666335399,
        "abs_return_acf_5": 0.2760779511250234,
        "abs_return_acf_20": 0.21620977902618274,
        "quantile_01": -0.05416008816891442,
        "quantile_99": 0.03988747728143643,
        "hill_tail_index": 2.346177392869156
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020304302946538136,
        "excess_kurtosis": 11.38771243625861,
        "return_acf_1": -0.13853032147070812,
        "abs_return_acf_1": 0.39166866415351353,
        "abs_return_acf_5": 0.37956038006859577,
        "abs_return_acf_20": 0.27106198576813073,
        "quantile_01": -0.06298541267949498,
        "quantile_99": 0.05939093653413551,
        "hill_tail_index": 2.4375125256969645
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018759330365787023,
        "excess_kurtosis": 4.703875831395875,
        "return_acf_1": -0.16539673297393412,
        "abs_return_acf_1": 0.3408928237040024,
        "abs_return_acf_5": 0.34622822887546584,
        "abs_return_acf_20": 0.27142405544774995,
        "quantile_01": -0.061212246668419505,
        "quantile_99": 0.04980241630767235,
        "hill_tail_index": 4.013061274843977
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018565504329487684,
        "excess_kurtosis": 3.832108281161924,
        "return_acf_1": -0.13637999647480914,
        "abs_return_acf_1": 0.32111905903497173,
        "abs_return_acf_5": 0.33601323051738735,
        "abs_return_acf_20": 0.28488184808453776,
        "quantile_01": -0.056474948861298134,
        "quantile_99": 0.05388053675776803,
        "hill_tail_index": 4.010488932518198
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0209206254653994,
        "excess_kurtosis": 8.153509689514044,
        "return_acf_1": -0.11913147818367359,
        "abs_return_acf_1": 0.38986205788746847,
        "abs_return_acf_5": 0.34642959919520916,
        "abs_return_acf_20": 0.30680512328996123,
        "quantile_01": -0.07391417156830375,
        "quantile_99": 0.0594897082479824,
        "hill_tail_index": 3.582948674713794
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01906279998643424,
        "excess_kurtosis": 3.7828573801601024,
        "return_acf_1": -0.16812260042828955,
        "abs_return_acf_1": 0.3260135922378173,
        "abs_return_acf_5": 0.30737132898738107,
        "abs_return_acf_20": 0.25400029765741894,
        "quantile_01": -0.05864098877966577,
        "quantile_99": 0.053587270924863865,
        "hill_tail_index": 3.640930272033258
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
