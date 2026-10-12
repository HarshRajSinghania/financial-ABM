# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27022
Run ID: `d32d729cbb39b247b480a0fd3437bbd98267790a53d4476f5333ac5e8ad9982c`
Result fingerprint: `f50c3acaf89e87ca602e30b8369fc132bcc9994e12a4c6dd68d814143768059d`

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
    "equal_weight_sd": -0.5229642857142826,
    "equal_weight_raw": -7.844464285714238,
    "fixed_start_cap_weight_sd": -0.5454939930778795,
    "fixed_start_cap_weight_raw": -8.182409896168195,
    "end_cap_weight_sd": -0.5260567381881099,
    "end_cap_weight_raw": -7.890851072821649
  },
  "full_period_change": {
    "equal_weight_sd": -0.8042380952380906,
    "equal_weight_raw": -12.06357142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7739619708994664,
    "inflation_mean_sd": 0.38809656084656086
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.42941666666666983,
    "equal_weight_raw": 6.441250000000049,
    "fixed_start_cap_weight_sd": 0.40688695930307256,
    "fixed_start_cap_weight_raw": 6.103304389546088,
    "end_cap_weight_sd": 0.4263242141928424,
    "end_cap_weight_raw": 6.394863212892636
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5190476190476159,
      "change_raw": -7.7857142857142385,
      "decay_adjusted_gain_sd": 0.43333333333333646
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5268253968253935,
      "change_raw": -7.902380952380903,
      "decay_adjusted_gain_sd": 0.4255555555555587
    },
    "small": {
      "count": 18,
      "change_sd": -0.5216865079365047,
      "change_raw": -7.825297619047571,
      "decay_adjusted_gain_sd": 0.4306944444444476
    },
    "large_minus_small_sd": 0.0026388888888888573,
    "large_minus_small_raw": 0.03958333333333286
  },
  "inflation": {
    "initial_mean_sd": 0.15183333333333332,
    "final_mean_sd": 0.4045,
    "mean_sd": 0.29640396891479326,
    "mean_absolute_raw_gap": 4.446059533721899,
    "final_absolute_raw_gap": 6.067500000000002,
    "mean_range_fraction": 0.04446059533721899
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.22666666666666666,
    "initial_wealth_share": 0.25783057996678016,
    "final_wealth_share": 0.2418026120775108
  },
  "pricing_slope": {
    "mean": -0.0021429376972964985,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.3380877503761982,
    "real_improvement_cost": 0.28070331515967334,
    "washing_cost": 0.05738443521652486,
    "fine_transfer": 0.01557421520705908,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3536619655832573,
    "resource_cost_fraction_initial_cap": 0.011269591679206607,
    "private_net_outflow_fraction_initial_cap": 0.011788732186108576,
    "fine_transfer_fraction_initial_cap": 0.0005191405069019694,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002823872319058237,
    "unapplied_final_day_resource_cost": 0.01680381926774688
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 38.10401289507068,
    "beneficial_raw_gain_per_resource_cost": 571.5601934260602,
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
    "accrued_cost": 2.82203893457838,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.15415154161209604,
    "accrued_cost_fraction_initial_cap": 0.094067964485946,
    "mean_contract_rate": 0.03903514159481791,
    "maximum_ledger_error": 4.2351647362715017e-20
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
    "maximum_relative_cash_error": 1.0667247604308469e-15,
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
      "minimum": -0.1827349860203893,
      "maximum": 0.03929140325891313,
      "mean": -0.11163833989652333,
      "median": -0.1165402427587808,
      "quantile_05": -0.1729631872270623,
      "quantile_95": -0.047339722015510066
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
      "minimum": 0.26755526057178647,
      "maximum": 0.7720418067596948,
      "mean": 0.47918374331509245,
      "median": 0.45490034983240474,
      "quantile_05": 0.32962315109200835,
      "quantile_95": 0.6860338951928165
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
        "daily_volatility": 0.01653607680655121,
        "excess_kurtosis": 4.65533445642175,
        "return_acf_1": -0.0697964607708645,
        "abs_return_acf_1": 0.2463396041650824,
        "abs_return_acf_5": 0.32035246280500435,
        "abs_return_acf_20": 0.27309283749952107,
        "quantile_01": -0.05191552990808137,
        "quantile_99": 0.04959794516703656,
        "hill_tail_index": 4.132991677467414
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01611290129961161,
        "excess_kurtosis": 5.9837656299165705,
        "return_acf_1": -0.14929872774669795,
        "abs_return_acf_1": 0.3382206648715365,
        "abs_return_acf_5": 0.3530082714568368,
        "abs_return_acf_20": 0.2675075430880961,
        "quantile_01": -0.050314696082915326,
        "quantile_99": 0.04456944979191599,
        "hill_tail_index": 3.3859645193881156
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016277162652023773,
        "excess_kurtosis": 3.568499742076483,
        "return_acf_1": -0.08588118283247566,
        "abs_return_acf_1": 0.3163729593867915,
        "abs_return_acf_5": 0.23921941352707696,
        "abs_return_acf_20": 0.2032046869853005,
        "quantile_01": -0.04507678983689136,
        "quantile_99": 0.04550131132886958,
        "hill_tail_index": 4.748080124147218
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018499709725078254,
        "excess_kurtosis": 5.908205793756144,
        "return_acf_1": -0.06348570023452672,
        "abs_return_acf_1": 0.40452586213186065,
        "abs_return_acf_5": 0.29126600696869664,
        "abs_return_acf_20": 0.26391652192914566,
        "quantile_01": -0.05507474806420038,
        "quantile_99": 0.051740077749831116,
        "hill_tail_index": 3.0393745946631556
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017254172153331176,
        "excess_kurtosis": 7.293890559867583,
        "return_acf_1": -0.06505566963565401,
        "abs_return_acf_1": 0.29854337831099415,
        "abs_return_acf_5": 0.3014361184673061,
        "abs_return_acf_20": 0.25126161560639837,
        "quantile_01": -0.05539302474318496,
        "quantile_99": 0.04522022927918518,
        "hill_tail_index": 3.255163634236528
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015043620779804884,
        "excess_kurtosis": 2.56724798125109,
        "return_acf_1": -0.05117740633765656,
        "abs_return_acf_1": 0.21716122844682162,
        "abs_return_acf_5": 0.2285660177818729,
        "abs_return_acf_20": 0.23241671656919963,
        "quantile_01": -0.04080677554905596,
        "quantile_99": 0.040865176612455444,
        "hill_tail_index": 4.433538777694347
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016077766193841766,
        "excess_kurtosis": 6.286844665252577,
        "return_acf_1": -0.11736315925150173,
        "abs_return_acf_1": 0.24890481720841756,
        "abs_return_acf_5": 0.20078944268244805,
        "abs_return_acf_20": 0.19774519780628294,
        "quantile_01": -0.0517999016707442,
        "quantile_99": 0.03998919047344355,
        "hill_tail_index": 2.384736199319621
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.016394632804964407,
        "excess_kurtosis": 5.023452893580494,
        "return_acf_1": -0.13833902513118437,
        "abs_return_acf_1": 0.3553073572163664,
        "abs_return_acf_5": 0.22340975723573736,
        "abs_return_acf_20": 0.26962221751184895,
        "quantile_01": -0.049942156078313135,
        "quantile_99": 0.040467861449636516,
        "hill_tail_index": 3.649295097483051
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017785607251459418,
        "excess_kurtosis": 8.579172048720602,
        "return_acf_1": -0.089606681995799,
        "abs_return_acf_1": 0.3245247876270623,
        "abs_return_acf_5": 0.20389501415233527,
        "abs_return_acf_20": 0.21840324315924242,
        "quantile_01": -0.06082401136661457,
        "quantile_99": 0.044728044465911755,
        "hill_tail_index": 3.645395507967029
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016634825640773777,
        "excess_kurtosis": 3.0567583593380556,
        "return_acf_1": -0.1412642477824572,
        "abs_return_acf_1": 0.2655684359415891,
        "abs_return_acf_5": 0.2736860746011407,
        "abs_return_acf_20": 0.1725646482939952,
        "quantile_01": -0.04815940519198946,
        "quantile_99": 0.04567722061365297,
        "hill_tail_index": 5.026767489509148
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016736672943115437,
        "excess_kurtosis": 5.268935153749377,
        "return_acf_1": -0.15034804502982685,
        "abs_return_acf_1": 0.3501421667436822,
        "abs_return_acf_5": 0.32853725775114284,
        "abs_return_acf_20": 0.24457808547658558,
        "quantile_01": -0.05234571971838921,
        "quantile_99": 0.042554620547524076,
        "hill_tail_index": 3.091256717023844
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01692266315380256,
        "excess_kurtosis": 10.422090194999651,
        "return_acf_1": -0.08892832199541456,
        "abs_return_acf_1": 0.3465671681391211,
        "abs_return_acf_5": 0.33056986970627594,
        "abs_return_acf_20": 0.26054938824250223,
        "quantile_01": -0.04920154903389495,
        "quantile_99": 0.0451616897480118,
        "hill_tail_index": 3.1123157609819314
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020151701731704236,
        "excess_kurtosis": 9.279172960623788,
        "return_acf_1": 0.03929140325891313,
        "abs_return_acf_1": 0.41382306592303225,
        "abs_return_acf_5": 0.32623045358973796,
        "abs_return_acf_20": 0.3818576548461897,
        "quantile_01": -0.061125326812059545,
        "quantile_99": 0.06354255657845025,
        "hill_tail_index": 3.0315746798363343
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017886716747403573,
        "excess_kurtosis": 9.405305757826516,
        "return_acf_1": -0.15200023510458963,
        "abs_return_acf_1": 0.43655327116273684,
        "abs_return_acf_5": 0.4204327213041625,
        "abs_return_acf_20": 0.29664442907664446,
        "quantile_01": -0.05240913984213137,
        "quantile_99": 0.05604201696325116,
        "hill_tail_index": 2.896473070192125
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015970040426891537,
        "excess_kurtosis": 4.220410269334761,
        "return_acf_1": -0.09031798243487599,
        "abs_return_acf_1": 0.26523598808729587,
        "abs_return_acf_5": 0.2809178329881043,
        "abs_return_acf_20": 0.2896251301058541,
        "quantile_01": -0.04460968062654423,
        "quantile_99": 0.04549089974197064,
        "hill_tail_index": 3.482056432618548
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016993308367215385,
        "excess_kurtosis": 4.7128243655273305,
        "return_acf_1": -0.11294529571397618,
        "abs_return_acf_1": 0.31779992287808595,
        "abs_return_acf_5": 0.28286498356485545,
        "abs_return_acf_20": 0.22858747333608317,
        "quantile_01": -0.04548565543475945,
        "quantile_99": 0.04666982262893965,
        "hill_tail_index": 3.335322482684841
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017694448543282476,
        "excess_kurtosis": 13.1639396917823,
        "return_acf_1": -0.04419979847920835,
        "abs_return_acf_1": 0.420405125850618,
        "abs_return_acf_5": 0.3516595980522321,
        "abs_return_acf_20": 0.2335974885335831,
        "quantile_01": -0.05538261718256341,
        "quantile_99": 0.04570753095109428,
        "hill_tail_index": 1.892123848905217
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020545015470993574,
        "excess_kurtosis": 24.03032390677036,
        "return_acf_1": -0.16217708014460464,
        "abs_return_acf_1": 0.47761938666257425,
        "abs_return_acf_5": 0.3913861036870546,
        "abs_return_acf_20": 0.2828640815707899,
        "quantile_01": -0.06253669549224143,
        "quantile_99": 0.05980295892813222,
        "hill_tail_index": 3.0589527313830724
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.015839739448952686,
        "excess_kurtosis": 3.3840049472959572,
        "return_acf_1": -0.1827349860203893,
        "abs_return_acf_1": 0.22434995520466844,
        "abs_return_acf_5": 0.26620347761318924,
        "abs_return_acf_20": 0.24953188495656548,
        "quantile_01": -0.04025259756718912,
        "quantile_99": 0.04537738641750489,
        "hill_tail_index": 3.1680405869514914
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019021081646011535,
        "excess_kurtosis": 9.860161834238642,
        "return_acf_1": -0.1430962846027722,
        "abs_return_acf_1": 0.37346281173094054,
        "abs_return_acf_5": 0.33880179750679923,
        "abs_return_acf_20": 0.26000575679934707,
        "quantile_01": -0.05649860535464638,
        "quantile_99": 0.054316236542192455,
        "hill_tail_index": 2.8797505909961063
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01717447203198608,
        "excess_kurtosis": 6.684013003801333,
        "return_acf_1": -0.09664638681790817,
        "abs_return_acf_1": 0.28602215232568295,
        "abs_return_acf_5": 0.2817120511109282,
        "abs_return_acf_20": 0.24517330859297237,
        "quantile_01": -0.05340515259787588,
        "quantile_99": 0.04649685282996066,
        "hill_tail_index": 2.9963290746505704
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01740594757163873,
        "excess_kurtosis": 5.447099842948109,
        "return_acf_1": -0.14572201480316807,
        "abs_return_acf_1": 0.305603819530952,
        "abs_return_acf_5": 0.2640348685244367,
        "abs_return_acf_20": 0.24662639074021708,
        "quantile_01": -0.05817199074281055,
        "quantile_99": 0.04702601193537656,
        "hill_tail_index": 3.2439813861912024
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01683944508071864,
        "excess_kurtosis": 9.793574354642866,
        "return_acf_1": -0.1803530785849339,
        "abs_return_acf_1": 0.3278534109494217,
        "abs_return_acf_5": 0.3335409365030793,
        "abs_return_acf_20": 0.20486426528195995,
        "quantile_01": -0.050968489695216355,
        "quantile_99": 0.04459622764911414,
        "hill_tail_index": 3.1796648500613216
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01699027592967382,
        "excess_kurtosis": 5.55499870385222,
        "return_acf_1": -0.11571732626605986,
        "abs_return_acf_1": 0.32005172804612536,
        "abs_return_acf_5": 0.27334748135266024,
        "abs_return_acf_20": 0.21346797489781819,
        "quantile_01": -0.04585668606580983,
        "quantile_99": 0.039725998248676536,
        "hill_tail_index": 3.299946642540965
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017602241635720557,
        "excess_kurtosis": 4.173028548631801,
        "return_acf_1": -0.13904305720267746,
        "abs_return_acf_1": 0.3698950983215274,
        "abs_return_acf_5": 0.26306638797249515,
        "abs_return_acf_20": 0.2694171761633793,
        "quantile_01": -0.05075532310317424,
        "quantile_99": 0.05396930660502448,
        "hill_tail_index": 4.248633137422588
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.015964769556263032,
        "excess_kurtosis": 8.514646384871757,
        "return_acf_1": -0.12870504225136872,
        "abs_return_acf_1": 0.1723457747372433,
        "abs_return_acf_5": 0.21311935274300578,
        "abs_return_acf_20": 0.23418090902956235,
        "quantile_01": -0.04289571782976726,
        "quantile_99": 0.037364637411446966,
        "hill_tail_index": 2.3207030705857794
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01738632985138996,
        "excess_kurtosis": 6.125647444194637,
        "return_acf_1": -0.07087417881503286,
        "abs_return_acf_1": 0.37700551793877946,
        "abs_return_acf_5": 0.42503072369080375,
        "abs_return_acf_20": 0.3684997257476902,
        "quantile_01": -0.054590825952449844,
        "quantile_99": 0.04821934505066719,
        "hill_tail_index": 3.407464803789101
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0220267592653404,
        "excess_kurtosis": 18.326187906627094,
        "return_acf_1": -0.15766517928887025,
        "abs_return_acf_1": 0.48475525621162285,
        "abs_return_acf_5": 0.40092964772241546,
        "abs_return_acf_20": 0.37251115162279574,
        "quantile_01": -0.07440926414751624,
        "quantile_99": 0.06239639781747854,
        "hill_tail_index": 2.272983698365349
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01999648099810145,
        "excess_kurtosis": 14.057688244956118,
        "return_acf_1": -0.16393109778966367,
        "abs_return_acf_1": 0.47288220163388334,
        "abs_return_acf_5": 0.33356668668033407,
        "abs_return_acf_20": 0.347856989740371,
        "quantile_01": -0.06368397176937246,
        "quantile_99": 0.0563941651214611,
        "hill_tail_index": 3.4197256297368854
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.015072411216263699,
        "excess_kurtosis": 1.3374695731839434,
        "return_acf_1": -0.0917679470904552,
        "abs_return_acf_1": 0.17771916607676577,
        "abs_return_acf_5": 0.09751792882383822,
        "abs_return_acf_20": 0.1701082313770497,
        "quantile_01": -0.039512858971271846,
        "quantile_99": 0.04132184233808452,
        "hill_tail_index": 7.20002408415193
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
