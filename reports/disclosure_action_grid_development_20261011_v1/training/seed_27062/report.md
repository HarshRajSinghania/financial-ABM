# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27062
Run ID: `d6c57be187f049931b333b6c721e1b6c24da4341b2b25af009a374736ca75304`
Result fingerprint: `eadd48751ea9fa43af515d68840748e7c4bfbf099719495f0ebcd5adfc6cc6c9`

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
    "equal_weight_sd": -0.5905476190476157,
    "equal_weight_raw": -8.858214285714237,
    "fixed_start_cap_weight_sd": -0.5992293168361517,
    "fixed_start_cap_weight_raw": -8.988439752542277,
    "end_cap_weight_sd": -0.6020879478994019,
    "end_cap_weight_raw": -9.031319218491028
  },
  "full_period_change": {
    "equal_weight_sd": -0.9042380952380903,
    "equal_weight_raw": -13.563571428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8569705687830642,
    "inflation_mean_sd": 0.6868068783068784
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.36183333333333656,
    "equal_weight_raw": 5.42750000000005,
    "fixed_start_cap_weight_sd": 0.3531516355448006,
    "fixed_start_cap_weight_raw": 5.297274533172011,
    "end_cap_weight_sd": 0.3502930044815507,
    "end_cap_weight_raw": 5.2543950672232596
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6315476190476158,
      "change_raw": -9.473214285714237,
      "decay_adjusted_gain_sd": 0.3208333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5568253968253934,
      "change_raw": -8.352380952380901,
      "decay_adjusted_gain_sd": 0.39555555555555894
    },
    "small": {
      "count": 18,
      "change_sd": -0.6005753968253935,
      "change_raw": -9.008630952380903,
      "decay_adjusted_gain_sd": 0.3518055555555588
    },
    "large_minus_small_sd": -0.03097222222222229,
    "large_minus_small_raw": -0.46458333333333435
  },
  "inflation": {
    "initial_mean_sd": 0.2761666666666667,
    "final_mean_sd": 0.74975,
    "mean_sd": 0.4815110324729392,
    "mean_absolute_raw_gap": 7.222665487094089,
    "final_absolute_raw_gap": 11.246250000000002,
    "mean_range_fraction": 0.07222665487094089
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.21333333333333335,
    "initial_wealth_share": 0.1340206864979056,
    "final_wealth_share": 0.15037032371941478
  },
  "pricing_slope": {
    "mean": -0.00045626610215211997,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.17345236017932963,
    "real_improvement_cost": 0.14307847464939,
    "washing_cost": 0.030373885529939623,
    "fine_transfer": 0.0075279549736835165,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.18098031515301316,
    "resource_cost_fraction_initial_cap": 0.005781745339310988,
    "private_net_outflow_fraction_initial_cap": 0.006032677171767105,
    "fine_transfer_fraction_initial_cap": 0.0002509318324561172,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0007435196663070498,
    "unapplied_final_day_resource_cost": 0.006198158068286969
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 62.58202533985288,
    "beneficial_raw_gain_per_resource_cost": 938.7303800977932,
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
    "accrued_cost": 2.9549457441400127,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.02124473205046402,
    "accrued_cost_fraction_initial_cap": 0.09849819147133375,
    "mean_contract_rate": 0.041419912881545805,
    "maximum_ledger_error": 4.743384504624082e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 2.2520009184293465e-15,
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
      "minimum": -0.19854001166792706,
      "maximum": 0.00999615153813194,
      "mean": -0.09006664287853398,
      "median": -0.07963264815337337,
      "quantile_05": -0.16991592032248534,
      "quantile_95": -0.024192364659489242
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
      "minimum": 0.27490677032355915,
      "maximum": 0.8425300653682943,
      "mean": 0.4985434291477855,
      "median": 0.44336695449917957,
      "quantile_05": 0.30807226082289935,
      "quantile_95": 0.7774847082436968
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
        "daily_volatility": 0.021519027057227486,
        "excess_kurtosis": 7.0161065847647475,
        "return_acf_1": -0.16228889177504893,
        "abs_return_acf_1": 0.37146212998343947,
        "abs_return_acf_5": 0.4014639968138225,
        "abs_return_acf_20": 0.325013491567184,
        "quantile_01": -0.06058456842653931,
        "quantile_99": 0.06566859098091644,
        "hill_tail_index": 3.3216470125819715
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018768671639976236,
        "excess_kurtosis": 6.063882909599803,
        "return_acf_1": -0.1754589287369556,
        "abs_return_acf_1": 0.2988274307035345,
        "abs_return_acf_5": 0.29003122955555116,
        "abs_return_acf_20": 0.21170456413989622,
        "quantile_01": -0.05307318831659394,
        "quantile_99": 0.061048332713651225,
        "hill_tail_index": 3.2470366785694345
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021930130203586303,
        "excess_kurtosis": 11.133759566478007,
        "return_acf_1": -0.19854001166792706,
        "abs_return_acf_1": 0.3356289430083739,
        "abs_return_acf_5": 0.3636680521197562,
        "abs_return_acf_20": 0.3170764128721413,
        "quantile_01": -0.0763948689856729,
        "quantile_99": 0.058657674506591456,
        "hill_tail_index": 3.0190035768822936
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021167787830477194,
        "excess_kurtosis": 7.649165584001146,
        "return_acf_1": -0.10782344555250951,
        "abs_return_acf_1": 0.3630028544574546,
        "abs_return_acf_5": 0.366365208768844,
        "abs_return_acf_20": 0.3943194260529065,
        "quantile_01": -0.06806191359901051,
        "quantile_99": 0.059138820250389676,
        "hill_tail_index": 2.6957545927812743
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021139136671104623,
        "excess_kurtosis": 40.541182210989845,
        "return_acf_1": -0.021244689583924906,
        "abs_return_acf_1": 0.5432353872694454,
        "abs_return_acf_5": 0.3159882679229994,
        "abs_return_acf_20": 0.20364980563029442,
        "quantile_01": -0.050915976104087116,
        "quantile_99": 0.04063551437163573,
        "hill_tail_index": 1.4057837287852128
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01826909818003407,
        "excess_kurtosis": 35.64906250418523,
        "return_acf_1": -0.0444767471234877,
        "abs_return_acf_1": 0.3940849074655698,
        "abs_return_acf_5": 0.2073472852693052,
        "abs_return_acf_20": 0.14787711850549215,
        "quantile_01": -0.03976169533856807,
        "quantile_99": 0.039233793406234334,
        "hill_tail_index": 2.057759262349714
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020720528825893474,
        "excess_kurtosis": 11.04818568247036,
        "return_acf_1": -0.133948360909843,
        "abs_return_acf_1": 0.36510842833103074,
        "abs_return_acf_5": 0.4068799713059231,
        "abs_return_acf_20": 0.31759119605069536,
        "quantile_01": -0.07856291482171891,
        "quantile_99": 0.0661757900448119,
        "hill_tail_index": 2.6483289059132717
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020903199591847867,
        "excess_kurtosis": 9.680332131115966,
        "return_acf_1": -0.13918247074824444,
        "abs_return_acf_1": 0.34969614034201724,
        "abs_return_acf_5": 0.3690850948700889,
        "abs_return_acf_20": 0.3036362990892352,
        "quantile_01": -0.05758668036533823,
        "quantile_99": 0.05903132310970432,
        "hill_tail_index": 2.8197356490349583
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017703739343806455,
        "excess_kurtosis": 3.069735512395705,
        "return_acf_1": -0.16314113226035507,
        "abs_return_acf_1": 0.2598367817353752,
        "abs_return_acf_5": 0.32392664243183233,
        "abs_return_acf_20": 0.2389770576478364,
        "quantile_01": -0.05088051009388761,
        "quantile_99": 0.046821619536013125,
        "hill_tail_index": 3.841932268368164
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017939914780610914,
        "excess_kurtosis": 30.21974025282214,
        "return_acf_1": -0.03401783004135637,
        "abs_return_acf_1": 0.40214410420142865,
        "abs_return_acf_5": 0.22966551945085126,
        "abs_return_acf_20": 0.20635868140884223,
        "quantile_01": -0.05504435274766826,
        "quantile_99": 0.037929461165162895,
        "hill_tail_index": 1.9364932701020285
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01910882155313988,
        "excess_kurtosis": 35.76614676730401,
        "return_acf_1": -0.028223494035300317,
        "abs_return_acf_1": 0.34532866527085915,
        "abs_return_acf_5": 0.206383973283368,
        "abs_return_acf_20": 0.1270021082743064,
        "quantile_01": -0.05171276858319613,
        "quantile_99": 0.03512517423614377,
        "hill_tail_index": 1.6655978635195687
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020042103361009304,
        "excess_kurtosis": 5.729474012803095,
        "return_acf_1": -0.07043149394697942,
        "abs_return_acf_1": 0.322640572406206,
        "abs_return_acf_5": 0.28798928468900437,
        "abs_return_acf_20": 0.3055654459926166,
        "quantile_01": -0.0709745124453793,
        "quantile_99": 0.05697642909994096,
        "hill_tail_index": 3.586387875614005
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.0206300459306462,
        "excess_kurtosis": 26.895073011434324,
        "return_acf_1": -0.044195029938409076,
        "abs_return_acf_1": 0.4732264706109968,
        "abs_return_acf_5": 0.40001563579989863,
        "abs_return_acf_20": 0.2256229400860891,
        "quantile_01": -0.05766862842465304,
        "quantile_99": 0.04862542887328734,
        "hill_tail_index": 1.8592433952520873
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01990085400796254,
        "excess_kurtosis": 7.616122183069905,
        "return_acf_1": -0.1414976376478671,
        "abs_return_acf_1": 0.29611637152751114,
        "abs_return_acf_5": 0.3776411093560803,
        "abs_return_acf_20": 0.2787250144209222,
        "quantile_01": -0.06865918726584216,
        "quantile_99": 0.05326232241216199,
        "hill_tail_index": 2.5652982653971925
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019144065635273717,
        "excess_kurtosis": 2.755779360803488,
        "return_acf_1": -0.1076480393612791,
        "abs_return_acf_1": 0.26459063666511456,
        "abs_return_acf_5": 0.3424651443712488,
        "abs_return_acf_20": 0.2512239163407841,
        "quantile_01": -0.058850564463028776,
        "quantile_99": 0.04902510176128861,
        "hill_tail_index": 4.932628206804424
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020676928389993025,
        "excess_kurtosis": 40.63488451964358,
        "return_acf_1": -0.039875612753050405,
        "abs_return_acf_1": 0.4624756369920526,
        "abs_return_acf_5": 0.4055065916422306,
        "abs_return_acf_20": 0.21741779889671237,
        "quantile_01": -0.059230867463518265,
        "quantile_99": 0.048051251991769864,
        "hill_tail_index": 1.718860227060994
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021258994627404642,
        "excess_kurtosis": 35.47772057979694,
        "return_acf_1": -0.0503457192325268,
        "abs_return_acf_1": 0.4253560544155069,
        "abs_return_acf_5": 0.37303325485115074,
        "abs_return_acf_20": 0.23139346181508208,
        "quantile_01": -0.051516516341027094,
        "quantile_99": 0.04539426295622154,
        "hill_tail_index": 1.7442083529293575
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017875794828985724,
        "excess_kurtosis": 4.499563392079335,
        "return_acf_1": -0.15390036209425584,
        "abs_return_acf_1": 0.2367541245059293,
        "abs_return_acf_5": 0.18934819776450476,
        "abs_return_acf_20": 0.18496234880656454,
        "quantile_01": -0.05119007962351106,
        "quantile_99": 0.046717097420062755,
        "hill_tail_index": 3.2194027488327785
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016659552548532144,
        "excess_kurtosis": 19.65402285076552,
        "return_acf_1": -0.027795078640734498,
        "abs_return_acf_1": 0.322095905085619,
        "abs_return_acf_5": 0.22646742637490355,
        "abs_return_acf_20": 0.1344197710384659,
        "quantile_01": -0.049194867791375135,
        "quantile_99": 0.03812935849765143,
        "hill_tail_index": 2.2792705629214796
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020956892767968225,
        "excess_kurtosis": 9.005013270714032,
        "return_acf_1": -0.0870238160229415,
        "abs_return_acf_1": 0.3040561697484646,
        "abs_return_acf_5": 0.3523614394857962,
        "abs_return_acf_20": 0.38417499242810155,
        "quantile_01": -0.07316343621846243,
        "quantile_99": 0.05570231982961075,
        "hill_tail_index": 2.633843454964954
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018352417870720453,
        "excess_kurtosis": 5.373154363091119,
        "return_acf_1": -0.11234517016988647,
        "abs_return_acf_1": 0.2445473760746728,
        "abs_return_acf_5": 0.2729882412887963,
        "abs_return_acf_20": 0.21677600664789456,
        "quantile_01": -0.05398337624902093,
        "quantile_99": 0.04381289460978264,
        "hill_tail_index": 3.3758668765494924
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01805458397113328,
        "excess_kurtosis": 3.7797052920461125,
        "return_acf_1": -0.10635329496592896,
        "abs_return_acf_1": 0.25567337670867907,
        "abs_return_acf_5": 0.2557081732823919,
        "abs_return_acf_20": 0.20905763531068663,
        "quantile_01": -0.05003555288456497,
        "quantile_99": 0.048345917173747234,
        "hill_tail_index": 4.0993363812096675
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017139136727893228,
        "excess_kurtosis": 19.792686606256847,
        "return_acf_1": 0.00999615153813194,
        "abs_return_acf_1": 0.24309797483055978,
        "abs_return_acf_5": 0.20247946364097194,
        "abs_return_acf_20": 0.13527797898853963,
        "quantile_01": -0.05162214707553532,
        "quantile_99": 0.035702626246202476,
        "hill_tail_index": 2.008761698250336
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018788593100157142,
        "excess_kurtosis": 18.634414157191994,
        "return_acf_1": -0.06670899592680471,
        "abs_return_acf_1": 0.40014613806025007,
        "abs_return_acf_5": 0.23018061232862125,
        "abs_return_acf_20": 0.16461383826600678,
        "quantile_01": -0.0510439735079935,
        "quantile_99": 0.0453394172978441,
        "hill_tail_index": 2.4321499296659157
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02207809161613335,
        "excess_kurtosis": 34.348812054472596,
        "return_acf_1": -0.06383739869053343,
        "abs_return_acf_1": 0.5988209073926027,
        "abs_return_acf_5": 0.3857226341602469,
        "abs_return_acf_20": 0.25309888314369905,
        "quantile_01": -0.05467057004883744,
        "quantile_99": 0.04920548979105071,
        "hill_tail_index": 1.6666003049079146
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018105091343362165,
        "excess_kurtosis": 6.467156166834624,
        "return_acf_1": -0.0976696776213445,
        "abs_return_acf_1": 0.3085757434732514,
        "abs_return_acf_5": 0.213976943047397,
        "abs_return_acf_20": 0.1580171075761158,
        "quantile_01": -0.05261436712397904,
        "quantile_99": 0.04564941171685028,
        "hill_tail_index": 3.4225069500553498
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02293697930848013,
        "excess_kurtosis": 44.08474234599524,
        "return_acf_1": -0.0709556382317166,
        "abs_return_acf_1": 0.5672442354867795,
        "abs_return_acf_5": 0.36990206108223944,
        "abs_return_acf_20": 0.24552926057168806,
        "quantile_01": -0.06276127332839841,
        "quantile_99": 0.04073146861052148,
        "hill_tail_index": 1.467559042664068
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01803257141037066,
        "excess_kurtosis": 6.695836957649902,
        "return_acf_1": -0.07224148028380523,
        "abs_return_acf_1": 0.2802331781240035,
        "abs_return_acf_5": 0.2832806789728086,
        "abs_return_acf_20": 0.19633865378036333,
        "quantile_01": -0.061300067534604576,
        "quantile_99": 0.045906857196558265,
        "hill_tail_index": 3.0058757200706987
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01876768389522327,
        "excess_kurtosis": 3.3225322141375155,
        "return_acf_1": -0.1343892814486932,
        "abs_return_acf_1": 0.27385302420936136,
        "abs_return_acf_5": 0.32766504548846576,
        "abs_return_acf_20": 0.24888737981733638,
        "quantile_01": -0.056765220847324264,
        "quantile_99": 0.045226496826018155,
        "hill_tail_index": 3.5889768247199134
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02119386491170283,
        "excess_kurtosis": 27.194481081908318,
        "return_acf_1": -0.05643570848244193,
        "abs_return_acf_1": 0.4829760435298857,
        "abs_return_acf_5": 0.34105743846328723,
        "abs_return_acf_20": 0.3225660860851481,
        "quantile_01": -0.06139514569521642,
        "quantile_99": 0.04605797093507759,
        "hill_tail_index": 1.5788774699444266
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
