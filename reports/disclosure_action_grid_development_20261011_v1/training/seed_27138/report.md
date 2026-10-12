# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27138
Run ID: `82a713353c77887b0058079e437e5f0b9cc3c597b0bdabc5c5f4eef7e2802833`
Result fingerprint: `2097c219890f249a7fc0fecc700ca02d64c68a42d17af7a9b0039f1b15f99e1f`

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
    "equal_weight_sd": -0.7548809523809493,
    "equal_weight_raw": -11.323214285714235,
    "fixed_start_cap_weight_sd": -0.7529800868615656,
    "fixed_start_cap_weight_raw": -11.294701302923484,
    "end_cap_weight_sd": -0.7581580013405936,
    "end_cap_weight_raw": -11.372370020108907
  },
  "full_period_change": {
    "equal_weight_sd": -1.1112380952380903,
    "equal_weight_raw": -16.668571428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0372268518518473,
    "inflation_mean_sd": 0.7430562169312169
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19750000000000315,
    "equal_weight_raw": 2.9625000000000465,
    "fixed_start_cap_weight_sd": 0.19940086551938668,
    "fixed_start_cap_weight_raw": 2.9910129827908007,
    "end_cap_weight_sd": 0.19422295104035872,
    "end_cap_weight_raw": 2.9133442656053807
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7540476190476157,
      "change_raw": -11.310714285714237,
      "decay_adjusted_gain_sd": 0.19833333333333658
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7440476190476158,
      "change_raw": -11.160714285714239,
      "decay_adjusted_gain_sd": 0.2083333333333365
    },
    "small": {
      "count": 18,
      "change_sd": -0.7604365079365046,
      "change_raw": -11.40654761904757,
      "decay_adjusted_gain_sd": 0.19194444444444755
    },
    "large_minus_small_sd": 0.006388888888888888,
    "large_minus_small_raw": 0.09583333333333333
  },
  "inflation": {
    "initial_mean_sd": 0.37066666666666664,
    "final_mean_sd": 0.7762500000000002,
    "mean_sd": 0.5476654870940882,
    "mean_absolute_raw_gap": 8.214982306411324,
    "final_absolute_raw_gap": 11.643750000000002,
    "mean_range_fraction": 0.08214982306411324
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.36,
    "initial_wealth_share": 0.2975005106761883,
    "final_wealth_share": 0.40263563288548543
  },
  "pricing_slope": {
    "mean": 9.815380583654363e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.03145365100511415,
    "real_improvement_cost": 0.02107096751566967,
    "washing_cost": 0.010382683489444485,
    "fine_transfer": 0.010768173310525783,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.042221824315639936,
    "resource_cost_fraction_initial_cap": 0.0010484550335038048,
    "private_net_outflow_fraction_initial_cap": 0.0014073941438546643,
    "fine_transfer_fraction_initial_cap": 0.0003589391103508593,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0012581009840818087,
    "unapplied_final_day_resource_cost": 0.0006668939142896939
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 188.3724086287067,
    "beneficial_raw_gain_per_resource_cost": 2825.5861294306005,
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
    "accrued_cost": 2.895898363186154,
    "baseline_accrued_cost": 2.976190476190478,
    "value_adjustment": 0.0802921130043231,
    "accrued_cost_fraction_initial_cap": 0.09652994543953844,
    "mean_contract_rate": 0.04059000529445511,
    "maximum_ledger_error": 4.912791094074942e-20
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
    "maximum_relative_cash_error": 1.261763160332762e-15,
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
      "minimum": -0.17038309908955815,
      "maximum": 0.013097478844819363,
      "mean": -0.097604524271197,
      "median": -0.10488941923303442,
      "quantile_05": -0.16212770551320665,
      "quantile_95": -0.020672061363321798
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
      "minimum": 0.23121813478310022,
      "maximum": 0.8018843513704331,
      "mean": 0.5176872174273747,
      "median": 0.5136064077074625,
      "quantile_05": 0.27667711405074846,
      "quantile_95": 0.7512101644241262
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
        "daily_volatility": 0.018108367841456627,
        "excess_kurtosis": 6.859280665267807,
        "return_acf_1": -0.15361431113265614,
        "abs_return_acf_1": 0.47062280829691194,
        "abs_return_acf_5": 0.4044812255914699,
        "abs_return_acf_20": 0.36419532485380984,
        "quantile_01": -0.06353968997477318,
        "quantile_99": 0.04869640080964717,
        "hill_tail_index": 3.367543928199079
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019646626770281343,
        "excess_kurtosis": 7.469995356998901,
        "return_acf_1": -0.15707241079581163,
        "abs_return_acf_1": 0.2889870481735058,
        "abs_return_acf_5": 0.37495274088663805,
        "abs_return_acf_20": 0.32093607072553987,
        "quantile_01": -0.059181718738694225,
        "quantile_99": 0.05998410459046301,
        "hill_tail_index": 3.79408391136727
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018026871087390758,
        "excess_kurtosis": 10.722937762648405,
        "return_acf_1": -0.08170484378215663,
        "abs_return_acf_1": 0.37302637286467194,
        "abs_return_acf_5": 0.33883361492005887,
        "abs_return_acf_20": 0.25263440513889807,
        "quantile_01": -0.059414199850507374,
        "quantile_99": 0.04054956693616254,
        "hill_tail_index": 2.708898171424793
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020299849181892506,
        "excess_kurtosis": 31.445451769314495,
        "return_acf_1": 0.013097478844819363,
        "abs_return_acf_1": 0.5223183216532482,
        "abs_return_acf_5": 0.4560775445472398,
        "abs_return_acf_20": 0.35474459989996165,
        "quantile_01": -0.06863571499992605,
        "quantile_99": 0.04821686280348906,
        "hill_tail_index": 1.9768804549995882
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016796310369623507,
        "excess_kurtosis": 9.591047624824997,
        "return_acf_1": -0.11366542180361582,
        "abs_return_acf_1": 0.3049873682371677,
        "abs_return_acf_5": 0.342722307892412,
        "abs_return_acf_20": 0.22331096950572976,
        "quantile_01": -0.04754852193966041,
        "quantile_99": 0.03907746677617317,
        "hill_tail_index": 2.552854892745665
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01873540699199299,
        "excess_kurtosis": 9.470637657882826,
        "return_acf_1": -0.0601853394578665,
        "abs_return_acf_1": 0.424814783441617,
        "abs_return_acf_5": 0.3588983735172248,
        "abs_return_acf_20": 0.3050979334948292,
        "quantile_01": -0.05985438047911337,
        "quantile_99": 0.05478864213671653,
        "hill_tail_index": 3.314115092439092
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020255279247609587,
        "excess_kurtosis": 21.704297168014477,
        "return_acf_1": -0.10525171094036694,
        "abs_return_acf_1": 0.5282393974292819,
        "abs_return_acf_5": 0.4355504569869958,
        "abs_return_acf_20": 0.34271697929031475,
        "quantile_01": -0.055473695408669366,
        "quantile_99": 0.05440259829437239,
        "hill_tail_index": 1.5416507447358248
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019840232333283924,
        "excess_kurtosis": 9.802849107546836,
        "return_acf_1": -0.07917352091905923,
        "abs_return_acf_1": 0.3815767625676035,
        "abs_return_acf_5": 0.3639926670415094,
        "abs_return_acf_20": 0.34446296903516616,
        "quantile_01": -0.058946922515340026,
        "quantile_99": 0.059141416827241805,
        "hill_tail_index": 2.965971786208183
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02098919282338927,
        "excess_kurtosis": 18.8452041146411,
        "return_acf_1": -0.017334073357324856,
        "abs_return_acf_1": 0.5110393393405724,
        "abs_return_acf_5": 0.4323029947818484,
        "abs_return_acf_20": 0.39829134242457487,
        "quantile_01": -0.06961284091531507,
        "quantile_99": 0.05686823411960877,
        "hill_tail_index": 2.124393006160412
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016161610915572357,
        "excess_kurtosis": 5.746663072865012,
        "return_acf_1": -0.05127166942702988,
        "abs_return_acf_1": 0.3332316156115258,
        "abs_return_acf_5": 0.39132399050824435,
        "abs_return_acf_20": 0.32087486689835365,
        "quantile_01": -0.04641991494117272,
        "quantile_99": 0.040749185730007374,
        "hill_tail_index": 2.7233713931235144
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01943528004543268,
        "excess_kurtosis": 18.323667110418864,
        "return_acf_1": -0.08593501631069961,
        "abs_return_acf_1": 0.4495992728505258,
        "abs_return_acf_5": 0.38027962318506703,
        "abs_return_acf_20": 0.3403239732257732,
        "quantile_01": -0.06004909330180982,
        "quantile_99": 0.044734822870419015,
        "hill_tail_index": 1.7023197967278565
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01693104803712143,
        "excess_kurtosis": 6.9073276486198765,
        "return_acf_1": -0.06356404920733556,
        "abs_return_acf_1": 0.2944358670272358,
        "abs_return_acf_5": 0.3177459674312321,
        "abs_return_acf_20": 0.2343265120417383,
        "quantile_01": -0.05055132727554748,
        "quantile_99": 0.0419596973889542,
        "hill_tail_index": 2.8567487544096326
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017034112546745892,
        "excess_kurtosis": 8.481161247809668,
        "return_acf_1": -0.10820225082401999,
        "abs_return_acf_1": 0.2899443145679425,
        "abs_return_acf_5": 0.29395943985290013,
        "abs_return_acf_20": 0.20926236302592,
        "quantile_01": -0.04465555152815369,
        "quantile_99": 0.051750140974528874,
        "hill_tail_index": 3.347174329044993
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01937276000609436,
        "excess_kurtosis": 17.52915144929817,
        "return_acf_1": -0.10968403038988368,
        "abs_return_acf_1": 0.5024273517937102,
        "abs_return_acf_5": 0.4354745954375467,
        "abs_return_acf_20": 0.37158144770333135,
        "quantile_01": -0.061614175320565984,
        "quantile_99": 0.04929166869810709,
        "hill_tail_index": 2.0264952074623537
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01763509740972722,
        "excess_kurtosis": 10.223220936473432,
        "return_acf_1": -0.05342315776974988,
        "abs_return_acf_1": 0.4068830281446596,
        "abs_return_acf_5": 0.3887462900921742,
        "abs_return_acf_20": 0.35342894140513864,
        "quantile_01": -0.06252882883660202,
        "quantile_99": 0.04291576417786189,
        "hill_tail_index": 2.1606193404147116
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019040556329308615,
        "excess_kurtosis": 6.164084113972571,
        "return_acf_1": -0.16626385573652988,
        "abs_return_acf_1": 0.29171362963477426,
        "abs_return_acf_5": 0.34679907312591984,
        "abs_return_acf_20": 0.27407924441263054,
        "quantile_01": -0.05792743182722668,
        "quantile_99": 0.05693645078646725,
        "hill_tail_index": 4.245659590945504
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018691546681185684,
        "excess_kurtosis": 13.171606475726296,
        "return_acf_1": -0.12332578046970019,
        "abs_return_acf_1": 0.43212369290087144,
        "abs_return_acf_5": 0.4164828945383556,
        "abs_return_acf_20": 0.3301767931404006,
        "quantile_01": -0.0720649753600028,
        "quantile_99": 0.04624285631396548,
        "hill_tail_index": 3.088978478919578
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.015598257139159728,
        "excess_kurtosis": 1.8070374493758017,
        "return_acf_1": -0.09648819296596027,
        "abs_return_acf_1": 0.1590562376289255,
        "abs_return_acf_5": 0.19749106346689835,
        "abs_return_acf_20": 0.17647949322539555,
        "quantile_01": -0.04198146735506251,
        "quantile_99": 0.04198458415116019,
        "hill_tail_index": 4.833696406987607
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021189013361670124,
        "excess_kurtosis": 22.313080349078035,
        "return_acf_1": -0.09017541758014584,
        "abs_return_acf_1": 0.550647666172916,
        "abs_return_acf_5": 0.5482140581220982,
        "abs_return_acf_20": 0.39052496429047373,
        "quantile_01": -0.07652707231198713,
        "quantile_99": 0.06092054446069576,
        "hill_tail_index": 2.328172647972334
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019244664931639614,
        "excess_kurtosis": 12.7602617238122,
        "return_acf_1": -0.07879175460696453,
        "abs_return_acf_1": 0.42771040087426615,
        "abs_return_acf_5": 0.4076352628658798,
        "abs_return_acf_20": 0.3350281483283694,
        "quantile_01": -0.06360161237600628,
        "quantile_99": 0.04826085649194902,
        "hill_tail_index": 2.8594662232460575
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017329860544049606,
        "excess_kurtosis": 11.881778360531499,
        "return_acf_1": -0.12573099076639585,
        "abs_return_acf_1": 0.3933354448934336,
        "abs_return_acf_5": 0.3187712505690564,
        "abs_return_acf_20": 0.21237051169880278,
        "quantile_01": -0.0577697316914662,
        "quantile_99": 0.03803726539460907,
        "hill_tail_index": 1.9264913501431402
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018110372593274335,
        "excess_kurtosis": 2.9965983015446387,
        "return_acf_1": -0.14637112952554357,
        "abs_return_acf_1": 0.2821381685902969,
        "abs_return_acf_5": 0.26614772744085907,
        "abs_return_acf_20": 0.1823307301787551,
        "quantile_01": -0.049360924712299616,
        "quantile_99": 0.04613046824067409,
        "hill_tail_index": 3.7754393170970006
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01784111393452779,
        "excess_kurtosis": 7.636262293751615,
        "return_acf_1": -0.10867857538111213,
        "abs_return_acf_1": 0.3096234833147572,
        "abs_return_acf_5": 0.3568001791517189,
        "abs_return_acf_20": 0.3077085478206669,
        "quantile_01": -0.054008913363760035,
        "quantile_99": 0.04477990050576436,
        "hill_tail_index": 2.4673511964069132
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018523856934380842,
        "excess_kurtosis": 24.25663518160337,
        "return_acf_1": -0.024751824481762462,
        "abs_return_acf_1": 0.44247668033096643,
        "abs_return_acf_5": 0.3370006368771935,
        "abs_return_acf_20": 0.24922892107926717,
        "quantile_01": -0.06091403025517878,
        "quantile_99": 0.04345808742118976,
        "hill_tail_index": 1.817086447633364
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01951780132441559,
        "excess_kurtosis": 14.363843017939306,
        "return_acf_1": -0.07539010343031297,
        "abs_return_acf_1": 0.4974470441360522,
        "abs_return_acf_5": 0.4494808184037165,
        "abs_return_acf_20": 0.4039460584927876,
        "quantile_01": -0.06938220831004246,
        "quantile_99": 0.06040994901040895,
        "hill_tail_index": 3.0327702619174683
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01640753953387346,
        "excess_kurtosis": 5.5524130344162135,
        "return_acf_1": -0.14200394615478257,
        "abs_return_acf_1": 0.30748811835605655,
        "abs_return_acf_5": 0.3146768397482908,
        "abs_return_acf_20": 0.2781635400395449,
        "quantile_01": -0.0505105338132062,
        "quantile_99": 0.04637480834048775,
        "hill_tail_index": 3.7502946303567173
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018906692711173526,
        "excess_kurtosis": 5.682145944213989,
        "return_acf_1": -0.17038309908955815,
        "abs_return_acf_1": 0.37008912455624693,
        "abs_return_acf_5": 0.29518614237314433,
        "abs_return_acf_20": 0.2801942497637031,
        "quantile_01": -0.06532238748588569,
        "quantile_99": 0.05433529332492431,
        "hill_tail_index": 4.717037695692767
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017676907455695577,
        "excess_kurtosis": 7.326010796316563,
        "return_acf_1": -0.10452712752570191,
        "abs_return_acf_1": 0.37959904915572307,
        "abs_return_acf_5": 0.2750247809987837,
        "abs_return_acf_20": 0.2459412313572891,
        "quantile_01": -0.05487665168933834,
        "quantile_99": 0.049383887064769455,
        "hill_tail_index": 3.6314099109788343
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018272924227350586,
        "excess_kurtosis": 4.368224824052066,
        "return_acf_1": -0.1293968555607241,
        "abs_return_acf_1": 0.34100336936364484,
        "abs_return_acf_5": 0.3793561616654493,
        "abs_return_acf_20": 0.2703685895592277,
        "quantile_01": -0.06294683268744365,
        "quantile_99": 0.05039851726623368,
        "hill_tail_index": 4.285166103961618
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01578744629955721,
        "excess_kurtosis": 4.288369252661267,
        "return_acf_1": -0.11887274758795899,
        "abs_return_acf_1": 0.2162584989986831,
        "abs_return_acf_5": 0.2555965061146573,
        "abs_return_acf_20": 0.1979149877386627,
        "quantile_01": -0.04220665287314009,
        "quantile_99": 0.03971547882292251,
        "hill_tail_index": 3.2165395562393795
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
