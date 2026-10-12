# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27182
Run ID: `e8f5594fa57c57ff2a51620e2f31eb6d6274984a8381f4c25aad890667bf7864`
Result fingerprint: `782c96291ad5b2871e267d2a7d8c890d6a49430b5c34bd3f1a3a256320d69d5d`

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
    "equal_weight_sd": -0.7752976190476157,
    "equal_weight_raw": -11.629464285714237,
    "fixed_start_cap_weight_sd": -0.7803336503190349,
    "fixed_start_cap_weight_raw": -11.705004754785527,
    "end_cap_weight_sd": -0.7739282624849884,
    "end_cap_weight_raw": -11.608923937274822
  },
  "full_period_change": {
    "equal_weight_sd": -1.1857380952380903,
    "equal_weight_raw": -17.786071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.094844907407403,
    "inflation_mean_sd": 0.4442123015873016
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.17708333333333648,
    "equal_weight_raw": 2.656250000000047,
    "fixed_start_cap_weight_sd": 0.17204730206191737,
    "fixed_start_cap_weight_raw": 2.5807095309287607,
    "end_cap_weight_sd": 0.17845268989596413,
    "end_cap_weight_raw": 2.676790348439462
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7023809523809491,
      "change_raw": -10.535714285714237,
      "decay_adjusted_gain_sd": 0.25000000000000316
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8343253968253934,
      "change_raw": -12.514880952380901,
      "decay_adjusted_gain_sd": 0.11805555555555881
    },
    "small": {
      "count": 18,
      "change_sd": -0.7579365079365048,
      "change_raw": -11.369047619047572,
      "decay_adjusted_gain_sd": 0.19444444444444747
    },
    "large_minus_small_sd": 0.05555555555555569,
    "large_minus_small_raw": 0.8333333333333354
  },
  "inflation": {
    "initial_mean_sd": 0.2520833333333333,
    "final_mean_sd": 0.4679166666666667,
    "mean_sd": 0.3633343741326673,
    "mean_absolute_raw_gap": 5.4500156119900085,
    "final_absolute_raw_gap": 7.01875,
    "mean_range_fraction": 0.054500156119900084
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.36666666666666664,
    "initial_wealth_share": 0.2950981173563638,
    "final_wealth_share": 0.4031864858558252
  },
  "pricing_slope": {
    "mean": -0.001490001045190721,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.06100949413806573,
    "real_improvement_cost": 0.04693682828992542,
    "washing_cost": 0.014072665848140306,
    "fine_transfer": 0.018609192701306735,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07961868683937247,
    "resource_cost_fraction_initial_cap": 0.0020336498046021906,
    "private_net_outflow_fraction_initial_cap": 0.0026539562279790816,
    "fine_transfer_fraction_initial_cap": 0.000620306423376891,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0007249501332153155,
    "unapplied_final_day_resource_cost": 0.0014494286757106385
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 87.07661119067465,
    "beneficial_raw_gain_per_resource_cost": 1306.1491678601199,
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
    "accrued_cost": 2.7603623280463516,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.21582814814412515,
    "accrued_cost_fraction_initial_cap": 0.09201207760154503,
    "mean_contract_rate": 0.038620952979147305,
    "maximum_ledger_error": 7.453889935837843e-20
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
    "price_cap_hits": 3,
    "maximum_relative_cash_error": 1.3373719076774528e-15,
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
      "minimum": -0.2519245809703604,
      "maximum": -0.013084012479058485,
      "mean": -0.13483044110771789,
      "median": -0.1347733854287843,
      "quantile_05": -0.22887003401957487,
      "quantile_95": -0.044373836758974834
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
      "minimum": 0.26059673550603635,
      "maximum": 0.7643445250122375,
      "mean": 0.45749749570320264,
      "median": 0.4260328650707556,
      "quantile_05": 0.3090543213684254,
      "quantile_95": 0.700020474523104
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
        "daily_volatility": 0.01677065923258614,
        "excess_kurtosis": 10.860892029985699,
        "return_acf_1": -0.13585284569254208,
        "abs_return_acf_1": 0.25066659118216633,
        "abs_return_acf_5": 0.3514888163228098,
        "abs_return_acf_20": 0.24123944680930645,
        "quantile_01": -0.04730097056416684,
        "quantile_99": 0.04147995644086228,
        "hill_tail_index": 2.911644706641956
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02052115223047301,
        "excess_kurtosis": 10.410858379650273,
        "return_acf_1": -0.2368979490259314,
        "abs_return_acf_1": 0.456046082851939,
        "abs_return_acf_5": 0.5223522592387441,
        "abs_return_acf_20": 0.31693525134173245,
        "quantile_01": -0.07257023248487926,
        "quantile_99": 0.06191842202032035,
        "hill_tail_index": 2.8112766048867615
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01898396708801977,
        "excess_kurtosis": 12.949470633857358,
        "return_acf_1": -0.17770593508809499,
        "abs_return_acf_1": 0.4185801202688001,
        "abs_return_acf_5": 0.39118323822313184,
        "abs_return_acf_20": 0.2261603775903932,
        "quantile_01": -0.05424713648220778,
        "quantile_99": 0.05289366178232101,
        "hill_tail_index": 2.8137199717248453
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0167614119422819,
        "excess_kurtosis": 3.6638331208129813,
        "return_acf_1": -0.10607769630376564,
        "abs_return_acf_1": 0.23377185546821788,
        "abs_return_acf_5": 0.2576120692293454,
        "abs_return_acf_20": 0.17846594600066013,
        "quantile_01": -0.049374864515959634,
        "quantile_99": 0.04941614194917856,
        "hill_tail_index": 4.769828576042844
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016922084521152,
        "excess_kurtosis": 13.859162435343467,
        "return_acf_1": -0.2190581379006947,
        "abs_return_acf_1": 0.29700401657342856,
        "abs_return_acf_5": 0.28579057873421,
        "abs_return_acf_20": 0.20624915276293862,
        "quantile_01": -0.05015000304025788,
        "quantile_99": 0.03902188968608914,
        "hill_tail_index": 2.330659636437757
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017112837555638225,
        "excess_kurtosis": 14.138614347913737,
        "return_acf_1": -0.1107902960748081,
        "abs_return_acf_1": 0.405106377028032,
        "abs_return_acf_5": 0.2841784795803747,
        "abs_return_acf_20": 0.22636549717743967,
        "quantile_01": -0.04453829339433266,
        "quantile_99": 0.041683707001760946,
        "hill_tail_index": 2.0577822775765946
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020125186755345945,
        "excess_kurtosis": 27.141082797415663,
        "return_acf_1": -0.17972553228227559,
        "abs_return_acf_1": 0.33484791618630855,
        "abs_return_acf_5": 0.46458410915937115,
        "abs_return_acf_20": 0.20982093110834416,
        "quantile_01": -0.05807058735317433,
        "quantile_99": 0.051199134818075004,
        "hill_tail_index": 2.247467481032501
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015153062002967812,
        "excess_kurtosis": 3.360349144185074,
        "return_acf_1": -0.11279685473249947,
        "abs_return_acf_1": 0.2213552783531017,
        "abs_return_acf_5": 0.23628397658489173,
        "abs_return_acf_20": 0.11305557089843563,
        "quantile_01": -0.04427601640842471,
        "quantile_99": 0.03835159475108624,
        "hill_tail_index": 3.0670708240585998
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01803770899623907,
        "excess_kurtosis": 18.805226992875916,
        "return_acf_1": -0.13369392516502657,
        "abs_return_acf_1": 0.34183881025651386,
        "abs_return_acf_5": 0.3873199244694279,
        "abs_return_acf_20": 0.235655862520935,
        "quantile_01": -0.05093728894805435,
        "quantile_99": 0.03945812058578196,
        "hill_tail_index": 1.7202397431326362
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01952061313172693,
        "excess_kurtosis": 33.63760578527872,
        "return_acf_1": -0.1957053667599134,
        "abs_return_acf_1": 0.4296274001659687,
        "abs_return_acf_5": 0.2992266033391196,
        "abs_return_acf_20": 0.21905833897606006,
        "quantile_01": -0.042696750126067204,
        "quantile_99": 0.0438043176177218,
        "hill_tail_index": 1.6897904488332076
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017735841384310908,
        "excess_kurtosis": 2.9865591886087657,
        "return_acf_1": -0.15493183672222027,
        "abs_return_acf_1": 0.21379314162867316,
        "abs_return_acf_5": 0.23902586382642477,
        "abs_return_acf_20": 0.23170252549722942,
        "quantile_01": -0.04954883412641869,
        "quantile_99": 0.04742132834649056,
        "hill_tail_index": 3.4310045645261704
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015616696091570981,
        "excess_kurtosis": 2.6687694460179685,
        "return_acf_1": -0.06930911531177222,
        "abs_return_acf_1": 0.13275732517919192,
        "abs_return_acf_5": 0.17039395815144076,
        "abs_return_acf_20": 0.1672601695406709,
        "quantile_01": -0.04038737093703707,
        "quantile_99": 0.04370974696061008,
        "hill_tail_index": 3.7829773089100613
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01634442688933499,
        "excess_kurtosis": 11.207638448053812,
        "return_acf_1": -0.013084012479058485,
        "abs_return_acf_1": 0.2565667228224592,
        "abs_return_acf_5": 0.2255001207777707,
        "abs_return_acf_20": 0.15367650010398623,
        "quantile_01": -0.0375018788550786,
        "quantile_99": 0.03781345927806975,
        "hill_tail_index": 2.111671388287179
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01596228074894165,
        "excess_kurtosis": 2.241782081506236,
        "return_acf_1": -0.12075442524384722,
        "abs_return_acf_1": 0.2109911034472027,
        "abs_return_acf_5": 0.23269479807959667,
        "abs_return_acf_20": 0.19767340859751495,
        "quantile_01": -0.041323165808150986,
        "quantile_99": 0.04930859601839103,
        "hill_tail_index": 4.7426165646105956
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01489719122332006,
        "excess_kurtosis": 5.376681501114115,
        "return_acf_1": -0.1138307720778807,
        "abs_return_acf_1": 0.20769423711166138,
        "abs_return_acf_5": 0.26985824986239426,
        "abs_return_acf_20": 0.22180062692575336,
        "quantile_01": -0.038054365754304854,
        "quantile_99": 0.03348256813557443,
        "hill_tail_index": 2.6490693086152812
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0160391450487171,
        "excess_kurtosis": 13.45331751860051,
        "return_acf_1": -0.16746170707760194,
        "abs_return_acf_1": 0.33301223838469085,
        "abs_return_acf_5": 0.3830230917592995,
        "abs_return_acf_20": 0.27876656112064785,
        "quantile_01": -0.04319435425601349,
        "quantile_99": 0.03489179179258385,
        "hill_tail_index": 1.9816718177943173
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01492799541814258,
        "excess_kurtosis": 1.594559399318423,
        "return_acf_1": -0.07851146846013292,
        "abs_return_acf_1": 0.17524965869031503,
        "abs_return_acf_5": 0.14198876847255448,
        "abs_return_acf_20": 0.15810246874477762,
        "quantile_01": -0.040372082473073195,
        "quantile_99": 0.0366630435204447,
        "hill_tail_index": 4.9976202953416955
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019138368976751412,
        "excess_kurtosis": 26.05754872056536,
        "return_acf_1": -0.1650541727411591,
        "abs_return_acf_1": 0.4260313645329763,
        "abs_return_acf_5": 0.42799115739083543,
        "abs_return_acf_20": 0.27886656235291285,
        "quantile_01": -0.05277046293430328,
        "quantile_99": 0.05789165904384479,
        "hill_tail_index": 2.8423600873458086
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.015704586891611,
        "excess_kurtosis": 2.9358634420916365,
        "return_acf_1": -0.04876961987833679,
        "abs_return_acf_1": 0.2939276105434549,
        "abs_return_acf_5": 0.2710105570924657,
        "abs_return_acf_20": 0.16742952272993347,
        "quantile_01": -0.042884478401847295,
        "quantile_99": 0.04457307867775141,
        "hill_tail_index": 3.952667444460762
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01689724785244562,
        "excess_kurtosis": 24.010756793288856,
        "return_acf_1": -0.18967505926957576,
        "abs_return_acf_1": 0.48581961018589254,
        "abs_return_acf_5": 0.44996540955792974,
        "abs_return_acf_20": 0.18257333852191476,
        "quantile_01": -0.04313110055596037,
        "quantile_99": 0.03886573398296321,
        "hill_tail_index": 1.85480863110667
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017655421886524393,
        "excess_kurtosis": 30.778756260671585,
        "return_acf_1": -0.2519245809703604,
        "abs_return_acf_1": 0.2975779499119062,
        "abs_return_acf_5": 0.3308867828657406,
        "abs_return_acf_20": 0.12754791282758715,
        "quantile_01": -0.03940459232066999,
        "quantile_99": 0.037167884131182764,
        "hill_tail_index": 1.8964389703829359
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016436771216475275,
        "excess_kurtosis": 4.550720397502706,
        "return_acf_1": -0.1319331917947326,
        "abs_return_acf_1": 0.2478340419480941,
        "abs_return_acf_5": 0.23692546340066184,
        "abs_return_acf_20": 0.1116241770302429,
        "quantile_01": -0.04558678315728237,
        "quantile_99": 0.04721218580607037,
        "hill_tail_index": 2.927696158834099
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.016408356871568896,
        "excess_kurtosis": 6.779099159507995,
        "return_acf_1": -0.1397045242907997,
        "abs_return_acf_1": 0.28573904816002554,
        "abs_return_acf_5": 0.28115931436409414,
        "abs_return_acf_20": 0.22281241642527916,
        "quantile_01": -0.04676966711269721,
        "quantile_99": 0.04532367678936682,
        "hill_tail_index": 3.3515480787807763
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.014102325066516489,
        "excess_kurtosis": 3.701490952579884,
        "return_acf_1": -0.10134435162924037,
        "abs_return_acf_1": 0.2550203724394761,
        "abs_return_acf_5": 0.2703617851797132,
        "abs_return_acf_20": 0.21977977969108006,
        "quantile_01": -0.03543359410833705,
        "quantile_99": 0.03424640734888418,
        "hill_tail_index": 2.9501821789283964
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.014944355832847613,
        "excess_kurtosis": 3.4928862322154117,
        "return_acf_1": -0.12288158790458749,
        "abs_return_acf_1": 0.22756392596799796,
        "abs_return_acf_5": 0.2585506873652581,
        "abs_return_acf_20": 0.19480017953369155,
        "quantile_01": -0.043849128031895106,
        "quantile_99": 0.033302394377758275,
        "hill_tail_index": 3.3900554790178252
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.014281252186893335,
        "excess_kurtosis": 2.64937217988921,
        "return_acf_1": -0.04077728693404228,
        "abs_return_acf_1": 0.14989810864943615,
        "abs_return_acf_5": 0.16922188250927467,
        "abs_return_acf_20": 0.15666302469015086,
        "quantile_01": -0.038159065780680325,
        "quantile_99": 0.03603107236105268,
        "hill_tail_index": 4.447552586151292
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01505888525583993,
        "excess_kurtosis": 4.4307778515787275,
        "return_acf_1": -0.05471647164052876,
        "abs_return_acf_1": 0.22073219940599623,
        "abs_return_acf_5": 0.24567517553922824,
        "abs_return_acf_20": 0.2734624861962603,
        "quantile_01": -0.04074462427394369,
        "quantile_99": 0.04088852068476351,
        "hill_tail_index": 3.4097776635011345
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01727365279315026,
        "excess_kurtosis": 6.955078939715314,
        "return_acf_1": -0.19148796733083875,
        "abs_return_acf_1": 0.40189775535377986,
        "abs_return_acf_5": 0.38079974548779705,
        "abs_return_acf_20": 0.2811238552073284,
        "quantile_01": -0.05438881288579622,
        "quantile_99": 0.05105538608560596,
        "hill_tail_index": 2.8994619681376697
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016889579627129784,
        "excess_kurtosis": 17.426697522153084,
        "return_acf_1": -0.142536590771698,
        "abs_return_acf_1": 0.3146994686821714,
        "abs_return_acf_5": 0.30373073236009246,
        "abs_return_acf_20": 0.16580543504673398,
        "quantile_01": -0.050428746992752474,
        "quantile_99": 0.03578002595616531,
        "hill_tail_index": 1.7922613723070262
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01902414808778967,
        "excess_kurtosis": 21.35898587998747,
        "return_acf_1": -0.13791995167757048,
        "abs_return_acf_1": 0.4968117508556235,
        "abs_return_acf_5": 0.3985308678608009,
        "abs_return_acf_20": 0.32634717663042073,
        "quantile_01": -0.055181774296202434,
        "quantile_99": 0.048458367256589925,
        "hill_tail_index": 2.1212887157730096
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
