# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720202
Run ID: `31da9086a200bd3a3cad6901189a93d2dd97c8c33cfe0b7a26abd7201894c55d`
Result fingerprint: `467bfc71581ea8c4e989bc2323dc4c7d3fc4c6d6e71472c66b7151490c4d485e`

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
    "equal_weight_sd": -0.4091309523809492,
    "equal_weight_raw": -6.136964285714238,
    "fixed_start_cap_weight_sd": -0.4742875112437265,
    "fixed_start_cap_weight_raw": -7.1143126686558995,
    "end_cap_weight_sd": -0.4777607736664487,
    "end_cap_weight_raw": -7.16641160499673
  },
  "full_period_change": {
    "equal_weight_sd": -0.8677380952380903,
    "equal_weight_raw": -13.016071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8609930555555512,
    "inflation_mean_sd": 0.6483022486772487
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5312705671783854,
    "equal_weight_raw": 7.969058507675781,
    "fixed_start_cap_weight_sd": 0.46957604865224467,
    "fixed_start_cap_weight_raw": 7.043640729783672,
    "end_cap_weight_sd": 0.4612055561938325,
    "end_cap_weight_raw": 6.9180833429074875
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6065476190476161,
      "change_raw": -9.098214285714242,
      "decay_adjusted_gain_sd": 0.3458333333333363
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4629365079365048,
      "change_raw": -6.944047619047573,
      "decay_adjusted_gain_sd": 0.4894444444444475
    },
    "small": {
      "count": 18,
      "change_sd": -0.34932539682539354,
      "change_raw": -5.239880952380903,
      "decay_adjusted_gain_sd": 0.5830898341861959
    },
    "large_minus_small_sd": -0.2572222222222226,
    "large_minus_small_raw": -3.8583333333333387
  },
  "inflation": {
    "initial_mean_sd": 0.13233333333333333,
    "final_mean_sd": 0.6962499999999999,
    "mean_sd": 0.4104409519844574,
    "mean_absolute_raw_gap": 6.156614279766861,
    "final_absolute_raw_gap": 10.443749999999998,
    "mean_range_fraction": 0.06156614279766861
  },
  "impact": {
    "initial_share": 0.15333333333333332,
    "final_share": 0.17333333333333334,
    "initial_wealth_share": 0.13484363009899442,
    "final_wealth_share": 0.12518739326713488
  },
  "pricing_slope": {
    "mean": 0.00036731827242253055,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.19490635784249766,
    "real_improvement_cost": 0.1602854148868832,
    "washing_cost": 0.03462094295561444,
    "fine_transfer": 0.01854235103717096,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2134487088796686,
    "resource_cost_fraction_initial_cap": 0.006496878594749921,
    "private_net_outflow_fraction_initial_cap": 0.007114956962655619,
    "fine_transfer_fraction_initial_cap": 0.0006180783679056986,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 8.454378927442366e-05,
    "unapplied_final_day_resource_cost": 0.0019389654929870658
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 81.77320222786695,
    "beneficial_raw_gain_per_resource_cost": 1226.5980334180042,
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
    "accrued_cost": 2.8065190099411215,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.16967146624935556,
    "accrued_cost_fraction_initial_cap": 0.09355063366470404,
    "mean_contract_rate": 0.03841607284778935,
    "maximum_ledger_error": 6.437450399132683e-20
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
    "maximum_relative_cash_error": 2.8718922080765033e-15,
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
      "minimum": -0.19635043986416584,
      "maximum": -0.056987246785441315,
      "mean": -0.11671849483047418,
      "median": -0.11806025053113911,
      "quantile_05": -0.16892964505283778,
      "quantile_95": -0.060792624721767184
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
      "minimum": 0.25880840749452494,
      "maximum": 0.786291973118343,
      "mean": 0.4789617476881136,
      "median": 0.4262245968634871,
      "quantile_05": 0.30424097709015074,
      "quantile_95": 0.7334699850752682
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
        "daily_volatility": 0.018237467886861904,
        "excess_kurtosis": 14.016552153705621,
        "return_acf_1": -0.1451327740362563,
        "abs_return_acf_1": 0.2414539978140959,
        "abs_return_acf_5": 0.3768745176419929,
        "abs_return_acf_20": 0.2207312694983626,
        "quantile_01": -0.047286795498215274,
        "quantile_99": 0.05225619307522007,
        "hill_tail_index": 2.6735067881184
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019185514019557134,
        "excess_kurtosis": 5.290633565901333,
        "return_acf_1": -0.1000622467254804,
        "abs_return_acf_1": 0.41162436837839406,
        "abs_return_acf_5": 0.36566784657850954,
        "abs_return_acf_20": 0.3016982256528393,
        "quantile_01": -0.05986800784135777,
        "quantile_99": 0.06336339170383153,
        "hill_tail_index": 4.187868604069823
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.014845679777617412,
        "excess_kurtosis": 6.620658607684502,
        "return_acf_1": -0.16560225165727044,
        "abs_return_acf_1": 0.21764719264945473,
        "abs_return_acf_5": 0.1561042516489239,
        "abs_return_acf_20": 0.1886734945486448,
        "quantile_01": -0.032431220878658386,
        "quantile_99": 0.03488531360960232,
        "hill_tail_index": 3.0149989432398927
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018654721868989425,
        "excess_kurtosis": 4.514214011806272,
        "return_acf_1": -0.07697665593412957,
        "abs_return_acf_1": 0.2451334784154794,
        "abs_return_acf_5": 0.2607823040255898,
        "abs_return_acf_20": 0.22070649017427238,
        "quantile_01": -0.055274799328369095,
        "quantile_99": 0.05015077574887679,
        "hill_tail_index": 3.4361350274988025
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01877607457513043,
        "excess_kurtosis": 18.355724869916035,
        "return_acf_1": -0.056987246785441315,
        "abs_return_acf_1": 0.4937318764140568,
        "abs_return_acf_5": 0.4090354126441994,
        "abs_return_acf_20": 0.27865159098068876,
        "quantile_01": -0.04672465608081169,
        "quantile_99": 0.048416833902455006,
        "hill_tail_index": 1.756003933987211
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016419710812865692,
        "excess_kurtosis": 2.268688315122799,
        "return_acf_1": -0.1436579318115392,
        "abs_return_acf_1": 0.265321372170843,
        "abs_return_acf_5": 0.2855665716339887,
        "abs_return_acf_20": 0.2251916184799073,
        "quantile_01": -0.04499649310255892,
        "quantile_99": 0.04301405435586005,
        "hill_tail_index": 5.336795776061051
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01703736572480977,
        "excess_kurtosis": 8.720575164674699,
        "return_acf_1": -0.059366887986420695,
        "abs_return_acf_1": 0.40169915642919607,
        "abs_return_acf_5": 0.34225265529219556,
        "abs_return_acf_20": 0.2353690079310163,
        "quantile_01": -0.051490629074786486,
        "quantile_99": 0.04545550448987666,
        "hill_tail_index": 2.475371079421906
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020751154614618076,
        "excess_kurtosis": 7.623603660864115,
        "return_acf_1": -0.08619052972679951,
        "abs_return_acf_1": 0.30972965177976053,
        "abs_return_acf_5": 0.4133467896709859,
        "abs_return_acf_20": 0.3231798560130992,
        "quantile_01": -0.07100512726114416,
        "quantile_99": 0.05970543974361911,
        "hill_tail_index": 3.2091589529884943
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016229279553882887,
        "excess_kurtosis": 2.47522781808307,
        "return_acf_1": -0.11236471190197828,
        "abs_return_acf_1": 0.25688695548782664,
        "abs_return_acf_5": 0.26621853221424885,
        "abs_return_acf_20": 0.19831909958125576,
        "quantile_01": -0.04976189800062159,
        "quantile_99": 0.04139056407385867,
        "hill_tail_index": 3.8227672815367013
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021994078499778278,
        "excess_kurtosis": 9.660688979473324,
        "return_acf_1": -0.08946303821353056,
        "abs_return_acf_1": 0.34243378339873143,
        "abs_return_acf_5": 0.3983614217440451,
        "abs_return_acf_20": 0.3670421464677642,
        "quantile_01": -0.07712878799277269,
        "quantile_99": 0.06307820402109342,
        "hill_tail_index": 2.6535027920504075
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018900766364896286,
        "excess_kurtosis": 6.250548950609078,
        "return_acf_1": -0.10234015136976826,
        "abs_return_acf_1": 0.3008376080784072,
        "abs_return_acf_5": 0.25779511356816676,
        "abs_return_acf_20": 0.2942288639089434,
        "quantile_01": -0.05425520706745903,
        "quantile_99": 0.05656101926035062,
        "hill_tail_index": 2.833058751664186
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018323223254625057,
        "excess_kurtosis": 4.082712928580967,
        "return_acf_1": -0.1288685953650924,
        "abs_return_acf_1": 0.31460517415936384,
        "abs_return_acf_5": 0.2878917913430085,
        "abs_return_acf_20": 0.2629921517685506,
        "quantile_01": -0.05091954737370522,
        "quantile_99": 0.05165714704885004,
        "hill_tail_index": 3.5733331624851883
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018865631689671078,
        "excess_kurtosis": 5.017973973886656,
        "return_acf_1": -0.07477423979262568,
        "abs_return_acf_1": 0.2780275016650984,
        "abs_return_acf_5": 0.3507245920831074,
        "abs_return_acf_20": 0.3056551786544824,
        "quantile_01": -0.06563478117156374,
        "quantile_99": 0.058077265689690856,
        "hill_tail_index": 3.955322217070504
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01764398991211094,
        "excess_kurtosis": 4.272157477829414,
        "return_acf_1": -0.17165205783102924,
        "abs_return_acf_1": 0.24214655367765966,
        "abs_return_acf_5": 0.2930340740856504,
        "abs_return_acf_20": 0.2551589491784537,
        "quantile_01": -0.047429766723492,
        "quantile_99": 0.05164547643590816,
        "hill_tail_index": 3.948507778345657
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01912478933028378,
        "excess_kurtosis": 8.576421804759041,
        "return_acf_1": -0.09763283198919025,
        "abs_return_acf_1": 0.2672334386134231,
        "abs_return_acf_5": 0.2816930434693021,
        "abs_return_acf_20": 0.2333013662664271,
        "quantile_01": -0.06473264602014078,
        "quantile_99": 0.0541232929214398,
        "hill_tail_index": 3.530283818256793
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0191915428331691,
        "excess_kurtosis": 9.609740182787306,
        "return_acf_1": -0.11920043324461765,
        "abs_return_acf_1": 0.392511027961378,
        "abs_return_acf_5": 0.3506965362383201,
        "abs_return_acf_20": 0.2414528381385244,
        "quantile_01": -0.05859891170417211,
        "quantile_99": 0.0614015684580968,
        "hill_tail_index": 2.892894836329711
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019183429161252426,
        "excess_kurtosis": 7.925490383227354,
        "return_acf_1": -0.06453674304339822,
        "abs_return_acf_1": 0.2784437530246153,
        "abs_return_acf_5": 0.3216030085953182,
        "abs_return_acf_20": 0.2164815300400131,
        "quantile_01": -0.05332264986211977,
        "quantile_99": 0.0514160362296909,
        "hill_tail_index": 2.9250735858659893
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01998284276519489,
        "excess_kurtosis": 10.20385116900788,
        "return_acf_1": -0.15181144921463535,
        "abs_return_acf_1": 0.27959769831578485,
        "abs_return_acf_5": 0.313643841365117,
        "abs_return_acf_20": 0.3317386594692526,
        "quantile_01": -0.06407108536263813,
        "quantile_99": 0.05760345258494339,
        "hill_tail_index": 3.246682629028639
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01933477250881527,
        "excess_kurtosis": 5.00524119513879,
        "return_acf_1": -0.10376474645313857,
        "abs_return_acf_1": 0.36641983303490133,
        "abs_return_acf_5": 0.36548132335441486,
        "abs_return_acf_20": 0.30983434623864925,
        "quantile_01": -0.061262496446545835,
        "quantile_99": 0.05743192071331279,
        "hill_tail_index": 4.599494233508914
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016267082883469425,
        "excess_kurtosis": 5.6335114031675335,
        "return_acf_1": -0.11984636680977222,
        "abs_return_acf_1": 0.33527716921833245,
        "abs_return_acf_5": 0.35365838843879327,
        "abs_return_acf_20": 0.263689347956911,
        "quantile_01": -0.04810695073058674,
        "quantile_99": 0.042929084388404586,
        "hill_tail_index": 3.042501899183644
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020505673389263495,
        "excess_kurtosis": 14.457462132363133,
        "return_acf_1": -0.06253519184274621,
        "abs_return_acf_1": 0.3159034879795019,
        "abs_return_acf_5": 0.306603997669179,
        "abs_return_acf_20": 0.3897924154026687,
        "quantile_01": -0.06531358428427801,
        "quantile_99": 0.05980452391151177,
        "hill_tail_index": 2.8454910955215778
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021149345461739747,
        "excess_kurtosis": 9.067940831791338,
        "return_acf_1": -0.10047320431380823,
        "abs_return_acf_1": 0.3596565225759082,
        "abs_return_acf_5": 0.4121670932291643,
        "abs_return_acf_20": 0.3241428099410888,
        "quantile_01": -0.0667499063713672,
        "quantile_99": 0.07541391730740976,
        "hill_tail_index": 3.041492006216417
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018304139068126113,
        "excess_kurtosis": 4.518621495024353,
        "return_acf_1": -0.14327718815263218,
        "abs_return_acf_1": 0.30168299285391464,
        "abs_return_acf_5": 0.3545257404529658,
        "abs_return_acf_20": 0.16410381329988305,
        "quantile_01": -0.05178769608640142,
        "quantile_99": 0.04778018120145889,
        "hill_tail_index": 3.393839479475476
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017094371601998275,
        "excess_kurtosis": 7.233756188293814,
        "return_acf_1": -0.15243511519872474,
        "abs_return_acf_1": 0.24606430122770415,
        "abs_return_acf_5": 0.2722323783921758,
        "abs_return_acf_20": 0.22934949631291093,
        "quantile_01": -0.050018157351844804,
        "quantile_99": 0.045781552216782734,
        "hill_tail_index": 3.0083407899705135
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01890026560675069,
        "excess_kurtosis": 13.625397982274155,
        "return_acf_1": -0.11692006781766057,
        "abs_return_acf_1": 0.3007458747482789,
        "abs_return_acf_5": 0.4157873399087721,
        "abs_return_acf_20": 0.3011822759077038,
        "quantile_01": -0.060595950185515585,
        "quantile_99": 0.05117743246836361,
        "hill_tail_index": 3.4966917126347066
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01661353103499382,
        "excess_kurtosis": 3.8118560823442325,
        "return_acf_1": -0.19635043986416584,
        "abs_return_acf_1": 0.3017703194019898,
        "abs_return_acf_5": 0.2300445468383836,
        "abs_return_acf_20": 0.1997337135952805,
        "quantile_01": -0.04143272255090167,
        "quantile_99": 0.04510460751490826,
        "hill_tail_index": 3.3370553287623594
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017837577364740793,
        "excess_kurtosis": 5.184957401091571,
        "return_acf_1": -0.1529766133339629,
        "abs_return_acf_1": 0.3258302457507993,
        "abs_return_acf_5": 0.3016313308876665,
        "abs_return_acf_20": 0.2655936827974677,
        "quantile_01": -0.05565368981712541,
        "quantile_99": 0.05280059977939706,
        "hill_tail_index": 3.231991793138939
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01836027798561031,
        "excess_kurtosis": 6.4182744944310635,
        "return_acf_1": -0.12665121867449544,
        "abs_return_acf_1": 0.3514542543261511,
        "abs_return_acf_5": 0.3437792081839761,
        "abs_return_acf_20": 0.2942279286649115,
        "quantile_01": -0.0584399008980594,
        "quantile_99": 0.05306400747282642,
        "hill_tail_index": 4.290369309335297
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019925960567628926,
        "excess_kurtosis": 7.816583674249843,
        "return_acf_1": -0.1345728529110239,
        "abs_return_acf_1": 0.33055035629206453,
        "abs_return_acf_5": 0.3948813770941516,
        "abs_return_acf_20": 0.320144380717553,
        "quantile_01": -0.06516488579613086,
        "quantile_99": 0.05735317668076587,
        "hill_tail_index": 2.899657279231522
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02164724778937683,
        "excess_kurtosis": 14.241049701894912,
        "return_acf_1": -0.14513106291289088,
        "abs_return_acf_1": 0.4017835118422301,
        "abs_return_acf_5": 0.4146552673397578,
        "abs_return_acf_20": 0.3554489920095338,
        "quantile_01": -0.06972000499870998,
        "quantile_99": 0.06597538540711502,
        "hill_tail_index": 2.3058840975827635
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
Unseen state share: 0.04555555555555556
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
