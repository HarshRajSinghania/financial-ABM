# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27113
Run ID: `ca2e2e9c0b863bef239388266904afec07f83c70fd6b0eebfbe3a657a3fd33fa`
Result fingerprint: `719245eb2319f395183d1d716bb517fa8899700744d60812837e61480f872ec4`

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
    "equal_weight_sd": -0.6064642857142827,
    "equal_weight_raw": -9.096964285714238,
    "fixed_start_cap_weight_sd": -0.6314620953088739,
    "fixed_start_cap_weight_raw": -9.471931429633107,
    "end_cap_weight_sd": -0.6213998372718768,
    "end_cap_weight_raw": -9.320997559078151
  },
  "full_period_change": {
    "equal_weight_sd": -0.8882380952380905,
    "equal_weight_raw": -13.323571428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8308799603174559,
    "inflation_mean_sd": 0.5701947751322751
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.34591666666666987,
    "equal_weight_raw": 5.188750000000046,
    "fixed_start_cap_weight_sd": 0.3209188570720787,
    "fixed_start_cap_weight_raw": 4.813782856081179,
    "end_cap_weight_sd": 0.33098111510907546,
    "end_cap_weight_raw": 4.964716726636133
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6682142857142827,
      "change_raw": -10.02321428571424,
      "decay_adjusted_gain_sd": 0.28416666666666973
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5309920634920603,
      "change_raw": -7.964880952380905,
      "decay_adjusted_gain_sd": 0.42138888888889203
    },
    "small": {
      "count": 18,
      "change_sd": -0.633908730158727,
      "change_raw": -9.508630952380905,
      "decay_adjusted_gain_sd": 0.3184722222222253
    },
    "large_minus_small_sd": -0.0343055555555557,
    "large_minus_small_raw": -0.5145833333333355
  },
  "inflation": {
    "initial_mean_sd": 0.3295833333333333,
    "final_mean_sd": 0.5668333333333333,
    "mean_sd": 0.4796906744379683,
    "mean_absolute_raw_gap": 7.195360116569526,
    "final_absolute_raw_gap": 8.502499999999998,
    "mean_range_fraction": 0.07195360116569526
  },
  "impact": {
    "initial_share": 0.2,
    "final_share": 0.20666666666666667,
    "initial_wealth_share": 0.1588476332813764,
    "final_wealth_share": 0.1536601155037583
  },
  "pricing_slope": {
    "mean": -3.206467517451617e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.10357512244141985,
    "real_improvement_cost": 0.08652392373188347,
    "washing_cost": 0.017051198709536385,
    "fine_transfer": 0.008149106834178695,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11172422927559855,
    "resource_cost_fraction_initial_cap": 0.0034525040813806612,
    "private_net_outflow_fraction_initial_cap": 0.003724140975853285,
    "fine_transfer_fraction_initial_cap": 0.0002716368944726231,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007181248155085485,
    "unapplied_final_day_resource_cost": 0.000312690078613395
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 100.19297834641146,
    "beneficial_raw_gain_per_resource_cost": 1502.894675196172,
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
    "accrued_cost": 2.9770583797714587,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.0008679035809822187,
    "accrued_cost_fraction_initial_cap": 0.09923527932571528,
    "mean_contract_rate": 0.04198235197634382,
    "maximum_ledger_error": 1.4230153513872246e-19
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
    "maximum_relative_cash_error": 2.0026458566702764e-15,
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
      "minimum": -0.24937702242700788,
      "maximum": -0.09416438907856402,
      "mean": -0.18342094255167218,
      "median": -0.1795472509189988,
      "quantile_05": -0.2404102401527904,
      "quantile_95": -0.112686357469921
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
      "minimum": 0.274899358111242,
      "maximum": 0.7745387893067537,
      "mean": 0.526872151809007,
      "median": 0.5229281508966317,
      "quantile_05": 0.3351551287556046,
      "quantile_95": 0.7199620762437571
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
        "daily_volatility": 0.0185860899761285,
        "excess_kurtosis": 6.739671000840726,
        "return_acf_1": -0.21674088986956797,
        "abs_return_acf_1": 0.35500910843756917,
        "abs_return_acf_5": 0.23799954123888872,
        "abs_return_acf_20": 0.16474643802170913,
        "quantile_01": -0.061467486022405905,
        "quantile_99": 0.05556335963321671,
        "hill_tail_index": 2.8694162806243457
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020698055816715053,
        "excess_kurtosis": 7.81583547214661,
        "return_acf_1": -0.232118996661042,
        "abs_return_acf_1": 0.46026436076325666,
        "abs_return_acf_5": 0.37833521651391316,
        "abs_return_acf_20": 0.36978392566372825,
        "quantile_01": -0.06901216645421904,
        "quantile_99": 0.06105423983123845,
        "hill_tail_index": 4.502383829277277
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01925448570777675,
        "excess_kurtosis": 3.4092687010775258,
        "return_acf_1": -0.18073783608197322,
        "abs_return_acf_1": 0.19627885113723675,
        "abs_return_acf_5": 0.24256124727425918,
        "abs_return_acf_20": 0.21775913133592573,
        "quantile_01": -0.05343952374371868,
        "quantile_99": 0.054061049157763,
        "hill_tail_index": 4.188920088115206
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016402955515904358,
        "excess_kurtosis": 4.509629256012284,
        "return_acf_1": -0.13332229359609662,
        "abs_return_acf_1": 0.2387954110675177,
        "abs_return_acf_5": 0.18772926914908694,
        "abs_return_acf_20": 0.22125132729403352,
        "quantile_01": -0.047370730736213416,
        "quantile_99": 0.04875247123014528,
        "hill_tail_index": 3.0991931394939467
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021113337134067288,
        "excess_kurtosis": 5.262469040692801,
        "return_acf_1": -0.24937702242700788,
        "abs_return_acf_1": 0.4079754610881376,
        "abs_return_acf_5": 0.39150949924280476,
        "abs_return_acf_20": 0.3488517631294181,
        "quantile_01": -0.07227427300402549,
        "quantile_99": 0.05227507482436837,
        "hill_tail_index": 4.178885636923689
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02084763105415517,
        "excess_kurtosis": 11.869247901302934,
        "return_acf_1": -0.21595207231703767,
        "abs_return_acf_1": 0.35687123706701696,
        "abs_return_acf_5": 0.3256042227748731,
        "abs_return_acf_20": 0.30935110248402525,
        "quantile_01": -0.06706156999872488,
        "quantile_99": 0.057211197106376545,
        "hill_tail_index": 2.8332538125387763
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019425646857064115,
        "excess_kurtosis": 6.784139698210197,
        "return_acf_1": -0.1550473746563267,
        "abs_return_acf_1": 0.32723487069303636,
        "abs_return_acf_5": 0.32781426150873133,
        "abs_return_acf_20": 0.2758973306868033,
        "quantile_01": -0.06591470251889535,
        "quantile_99": 0.057001073396454716,
        "hill_tail_index": 4.25293845444185
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018154133267234692,
        "excess_kurtosis": 6.462533193208142,
        "return_acf_1": -0.20733101197377815,
        "abs_return_acf_1": 0.3703598504471702,
        "abs_return_acf_5": 0.31980954875010775,
        "abs_return_acf_20": 0.22416357715397514,
        "quantile_01": -0.05457178734812669,
        "quantile_99": 0.04686853124779079,
        "hill_tail_index": 3.8649677293228653
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021820337786578225,
        "excess_kurtosis": 6.506115378485918,
        "return_acf_1": -0.20849187394472335,
        "abs_return_acf_1": 0.5012587504387651,
        "abs_return_acf_5": 0.42236430039352413,
        "abs_return_acf_20": 0.3236305539200294,
        "quantile_01": -0.0645312444699044,
        "quantile_99": 0.06171941032067146,
        "hill_tail_index": 3.4092229977267183
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020171527062282764,
        "excess_kurtosis": 11.609342132919407,
        "return_acf_1": -0.19890507636283197,
        "abs_return_acf_1": 0.4030882268309648,
        "abs_return_acf_5": 0.3312603844335795,
        "abs_return_acf_20": 0.276330818278023,
        "quantile_01": -0.06956216248002772,
        "quantile_99": 0.05751926333254354,
        "hill_tail_index": 3.0854153693799633
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01931073660974569,
        "excess_kurtosis": 5.509643099166572,
        "return_acf_1": -0.09580240973032257,
        "abs_return_acf_1": 0.38550351327065485,
        "abs_return_acf_5": 0.32724041139622295,
        "abs_return_acf_20": 0.2994520425762917,
        "quantile_01": -0.05935851999222334,
        "quantile_99": 0.05563193822979464,
        "hill_tail_index": 4.205351570400694
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021269023902274403,
        "excess_kurtosis": 9.443057382984321,
        "return_acf_1": -0.23558354096781572,
        "abs_return_acf_1": 0.4464683489826038,
        "abs_return_acf_5": 0.32323353763644647,
        "abs_return_acf_20": 0.34642815081679507,
        "quantile_01": -0.06981084512055961,
        "quantile_99": 0.0602501343704632,
        "hill_tail_index": 2.9738056363549124
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017780634444059303,
        "excess_kurtosis": 6.414276711568171,
        "return_acf_1": -0.17542779347643386,
        "abs_return_acf_1": 0.329399116971805,
        "abs_return_acf_5": 0.2778255690271417,
        "abs_return_acf_20": 0.2628511767110381,
        "quantile_01": -0.05427141986407578,
        "quantile_99": 0.04704071866999249,
        "hill_tail_index": 3.380436023665779
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018628387686181233,
        "excess_kurtosis": 2.9039281643241406,
        "return_acf_1": -0.15294354591516837,
        "abs_return_acf_1": 0.25723529907481313,
        "abs_return_acf_5": 0.30637258526451117,
        "abs_return_acf_20": 0.2689815068020658,
        "quantile_01": -0.05222397364561662,
        "quantile_99": 0.05148759498464484,
        "hill_tail_index": 4.750179567000602
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019714847320087367,
        "excess_kurtosis": 7.2921606733864515,
        "return_acf_1": -0.15943224627880612,
        "abs_return_acf_1": 0.33349286189454913,
        "abs_return_acf_5": 0.3460486748488178,
        "abs_return_acf_20": 0.29940497240234837,
        "quantile_01": -0.06779528542686906,
        "quantile_99": 0.055391985115876785,
        "hill_tail_index": 2.958559733313199
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021334297001775433,
        "excess_kurtosis": 9.193035237185793,
        "return_acf_1": -0.2054818622240336,
        "abs_return_acf_1": 0.4836212605913663,
        "abs_return_acf_5": 0.428313939784767,
        "abs_return_acf_20": 0.3195936792616005,
        "quantile_01": -0.07065551977745041,
        "quantile_99": 0.06101001678243439,
        "hill_tail_index": 2.7712120151869666
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017415190250469236,
        "excess_kurtosis": 4.148994639243897,
        "return_acf_1": -0.1377312574668021,
        "abs_return_acf_1": 0.27762638199678596,
        "abs_return_acf_5": 0.2204061650189935,
        "abs_return_acf_20": 0.1729616214126537,
        "quantile_01": -0.051752252847602855,
        "quantile_99": 0.05112694459890626,
        "hill_tail_index": 3.9015366887807885
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020990867651365087,
        "excess_kurtosis": 6.429183530382206,
        "return_acf_1": -0.09416438907856402,
        "abs_return_acf_1": 0.4386628674273386,
        "abs_return_acf_5": 0.3483983678427955,
        "abs_return_acf_20": 0.35081155629871613,
        "quantile_01": -0.06983518071733105,
        "quantile_99": 0.06199425157899938,
        "hill_tail_index": 3.736378982751016
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019101196117637494,
        "excess_kurtosis": 5.235432320104314,
        "return_acf_1": -0.15225263825113966,
        "abs_return_acf_1": 0.33704059513983553,
        "abs_return_acf_5": 0.29108948532827233,
        "abs_return_acf_20": 0.250912579671759,
        "quantile_01": -0.06105912486094966,
        "quantile_99": 0.05443871004359443,
        "hill_tail_index": 4.16423753761531
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018349366483817884,
        "excess_kurtosis": 8.99491474988311,
        "return_acf_1": -0.21532336234939747,
        "abs_return_acf_1": 0.37312305704123616,
        "abs_return_acf_5": 0.24761157708807113,
        "abs_return_acf_20": 0.22548419243520287,
        "quantile_01": -0.05705848481529729,
        "quantile_99": 0.049922645835448844,
        "hill_tail_index": 2.8686664713919026
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01635355796530215,
        "excess_kurtosis": 7.648255137876767,
        "return_acf_1": -0.16651953517404736,
        "abs_return_acf_1": 0.3090751912166385,
        "abs_return_acf_5": 0.2350039898666929,
        "abs_return_acf_20": 0.18763153807665822,
        "quantile_01": -0.05019829552972889,
        "quantile_99": 0.04181318935498972,
        "hill_tail_index": 2.40071272878633
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02090399312290392,
        "excess_kurtosis": 4.915694450727971,
        "return_acf_1": -0.24205857310093568,
        "abs_return_acf_1": 0.4032196299200749,
        "abs_return_acf_5": 0.3127127395103809,
        "abs_return_acf_20": 0.27302749061012943,
        "quantile_01": -0.07395446271930503,
        "quantile_99": 0.05676023681896845,
        "hill_tail_index": 3.361827178925682
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01614733378570557,
        "excess_kurtosis": 3.9139548270779896,
        "return_acf_1": -0.17835666575602438,
        "abs_return_acf_1": 0.21557606670451507,
        "abs_return_acf_5": 0.12185604962911133,
        "abs_return_acf_20": 0.1701023681257727,
        "quantile_01": -0.046071571664235554,
        "quantile_99": 0.04122934396840331,
        "hill_tail_index": 3.7710333844633928
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019472506850468606,
        "excess_kurtosis": 5.626103665461988,
        "return_acf_1": -0.23839561099394616,
        "abs_return_acf_1": 0.36108531673899524,
        "abs_return_acf_5": 0.2538978532259969,
        "abs_return_acf_20": 0.2301631354165232,
        "quantile_01": -0.0642533495672929,
        "quantile_99": 0.05673155480720167,
        "hill_tail_index": 3.987877062365871
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02082005841207384,
        "excess_kurtosis": 6.334048186033245,
        "return_acf_1": -0.2331553228378673,
        "abs_return_acf_1": 0.3519814334809694,
        "abs_return_acf_5": 0.3495298469971791,
        "abs_return_acf_20": 0.25755915443411775,
        "quantile_01": -0.0626289734456322,
        "quantile_99": 0.054700911240228405,
        "hill_tail_index": 2.896821451464423
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021828700766578085,
        "excess_kurtosis": 9.148792740959221,
        "return_acf_1": -0.17111919648934323,
        "abs_return_acf_1": 0.35923901110855816,
        "abs_return_acf_5": 0.36724535066515274,
        "abs_return_acf_20": 0.34320901860875835,
        "quantile_01": -0.08094242438338467,
        "quantile_99": 0.06234028345317103,
        "hill_tail_index": 3.0826356630264873
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019931288265236314,
        "excess_kurtosis": 7.778303384194878,
        "return_acf_1": -0.1885837191138775,
        "abs_return_acf_1": 0.37181814600353486,
        "abs_return_acf_5": 0.28445671846695,
        "abs_return_acf_20": 0.29627331100772814,
        "quantile_01": -0.06531141072274738,
        "quantile_99": 0.05294775484238105,
        "hill_tail_index": 3.016444586082437
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019191645961396966,
        "excess_kurtosis": 9.448861760608203,
        "return_acf_1": -0.1707231749838576,
        "abs_return_acf_1": 0.42778295400196886,
        "abs_return_acf_5": 0.3981713080288481,
        "abs_return_acf_20": 0.27338335217946824,
        "quantile_01": -0.06458924093704788,
        "quantile_99": 0.05154298986441995,
        "hill_tail_index": 2.6062005231833076
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01856063438907717,
        "excess_kurtosis": 6.43798139761344,
        "return_acf_1": -0.1356879493254956,
        "abs_return_acf_1": 0.3057832583205959,
        "abs_return_acf_5": 0.287773655350527,
        "abs_return_acf_20": 0.1816819377534348,
        "quantile_01": -0.06589389346090668,
        "quantile_99": 0.05162255326794182,
        "hill_tail_index": 3.11714960038259
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020483424797730305,
        "excess_kurtosis": 8.416255665989095,
        "return_acf_1": -0.15586103514590316,
        "abs_return_acf_1": 0.40185062281181283,
        "abs_return_acf_5": 0.4109078950552829,
        "abs_return_acf_20": 0.32917236195162203,
        "quantile_01": -0.06695406172002766,
        "quantile_99": 0.053921799295194264,
        "hill_tail_index": 3.1519664968493943
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
