# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27097
Run ID: `0894836efeef029ca4162bc0642fb7cd8f26be17e8a090f86adad66433e42860`
Result fingerprint: `bcb2d2c3ce7cad0423c70e7d9828e932fc11a6dc93f5af8d68d5f675ce276a8a`

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
    "equal_weight_sd": -0.6310169715549123,
    "equal_weight_raw": -9.465254573323685,
    "fixed_start_cap_weight_sd": -0.6163127052252799,
    "fixed_start_cap_weight_raw": -9.2446905783792,
    "end_cap_weight_sd": -0.5769356220838087,
    "end_cap_weight_raw": -8.654034331257128
  },
  "full_period_change": {
    "equal_weight_sd": -0.982707447745387,
    "equal_weight_raw": -14.740611716180805
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9355848255483603,
    "inflation_mean_sd": 0.6228571428571428
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.29707142857143154,
    "equal_weight_raw": 4.456071428571475,
    "fixed_start_cap_weight_sd": 0.3284652012211406,
    "fixed_start_cap_weight_raw": 4.92697801831711,
    "end_cap_weight_sd": 0.36666033930005404,
    "end_cap_weight_raw": 5.4999050895008095
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6715476190476158,
      "change_raw": -10.073214285714238,
      "decay_adjusted_gain_sd": 0.28083333333333654
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6321031746031713,
      "change_raw": -9.48154761904757,
      "decay_adjusted_gain_sd": 0.320277777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.6237187621153324,
      "change_raw": -9.355781431729985,
      "decay_adjusted_gain_sd": 0.2881746031746062
    },
    "large_minus_small_sd": -0.04782885693228345,
    "large_minus_small_raw": -0.7174328539842517
  },
  "inflation": {
    "initial_mean_sd": 0.29100000000000004,
    "final_mean_sd": 0.6618333333333333,
    "mean_sd": 0.4726812378573412,
    "mean_absolute_raw_gap": 7.090218567860116,
    "final_absolute_raw_gap": 9.9275,
    "mean_range_fraction": 0.07090218567860117
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.24769645686263603,
    "final_wealth_share": 0.2711492517426101
  },
  "pricing_slope": {
    "mean": -0.0018074325590864836,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.4828371079186606,
    "real_improvement_cost": 0.4541334504935589,
    "washing_cost": 0.028703657425101732,
    "fine_transfer": 0.004157003516932718,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.4869941114355933,
    "resource_cost_fraction_initial_cap": 0.01609457026395535,
    "private_net_outflow_fraction_initial_cap": 0.01623313704785311,
    "fine_transfer_fraction_initial_cap": 0.00013856678389775727,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.009579477577652502,
    "unapplied_final_day_resource_cost": 0.0062718310742865616
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 18.457866454299737,
    "beneficial_raw_gain_per_resource_cost": 276.867996814496,
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
    "accrued_cost": 2.990037721607969,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.013847245417492611,
    "accrued_cost_fraction_initial_cap": 0.09966792405359895,
    "mean_contract_rate": 0.040580382492186165,
    "maximum_ledger_error": 7.792703114739563e-20
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
    "maximum_relative_cash_error": 2.7377946215690355e-15,
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
      "minimum": -0.27200111241916314,
      "maximum": -0.0526001424388282,
      "mean": -0.1652448590907885,
      "median": -0.16731220777089112,
      "quantile_05": -0.249694907698598,
      "quantile_95": -0.07131370163309506
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
      "minimum": 0.27584182287636705,
      "maximum": 0.7915215711642943,
      "mean": 0.498956659358751,
      "median": 0.46202627329794926,
      "quantile_05": 0.31108170782215744,
      "quantile_95": 0.7386276453378395
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
        "daily_volatility": 0.02132553961890404,
        "excess_kurtosis": 10.163791783559658,
        "return_acf_1": -0.24996627880342556,
        "abs_return_acf_1": 0.4404495129126408,
        "abs_return_acf_5": 0.4541632962928897,
        "abs_return_acf_20": 0.3324892924790465,
        "quantile_01": -0.08364052484913054,
        "quantile_99": 0.06632584800784054,
        "hill_tail_index": 3.01411929991147
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019767553462237835,
        "excess_kurtosis": 7.94342232333215,
        "return_acf_1": -0.0526001424388282,
        "abs_return_acf_1": 0.39095335783713925,
        "abs_return_acf_5": 0.4004897438167909,
        "abs_return_acf_20": 0.29594943052143885,
        "quantile_01": -0.07247213276108237,
        "quantile_99": 0.05162967627732923,
        "hill_tail_index": 2.771155856543549
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01857179292851923,
        "excess_kurtosis": 5.231888084793301,
        "return_acf_1": -0.20945296950679101,
        "abs_return_acf_1": 0.37627272062513256,
        "abs_return_acf_5": 0.31950931337779453,
        "abs_return_acf_20": 0.2842566649433651,
        "quantile_01": -0.05675736953894949,
        "quantile_99": 0.053273266670822036,
        "hill_tail_index": 3.462619129138165
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018047656676371825,
        "excess_kurtosis": 10.316602505854894,
        "return_acf_1": -0.18483733745340433,
        "abs_return_acf_1": 0.26751763032042286,
        "abs_return_acf_5": 0.2275325784783123,
        "abs_return_acf_20": 0.24236163887627427,
        "quantile_01": -0.04981177230365669,
        "quantile_99": 0.05171856374327847,
        "hill_tail_index": 3.3246336959897373
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.023313455228334518,
        "excess_kurtosis": 13.693750593732787,
        "return_acf_1": -0.19646960640366137,
        "abs_return_acf_1": 0.43119665748454794,
        "abs_return_acf_5": 0.45169239593451155,
        "abs_return_acf_20": 0.37812027886868077,
        "quantile_01": -0.0829682626494812,
        "quantile_99": 0.06359578910522899,
        "hill_tail_index": 2.589558357878385
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022632407472452605,
        "excess_kurtosis": 12.664028412112872,
        "return_acf_1": -0.1266795803661784,
        "abs_return_acf_1": 0.36668386835977457,
        "abs_return_acf_5": 0.382252005988017,
        "abs_return_acf_20": 0.4181119195768621,
        "quantile_01": -0.07869884997896921,
        "quantile_99": 0.06733611642010162,
        "hill_tail_index": 2.4816372802275386
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019166200672025204,
        "excess_kurtosis": 5.842674228863238,
        "return_acf_1": -0.12535318748016616,
        "abs_return_acf_1": 0.3062083344446631,
        "abs_return_acf_5": 0.2719762528068954,
        "abs_return_acf_20": 0.2763665747633022,
        "quantile_01": -0.061027074572732674,
        "quantile_99": 0.05064722783675815,
        "hill_tail_index": 3.5845513965932905
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018110042204286945,
        "excess_kurtosis": 4.275484263641584,
        "return_acf_1": -0.14010382350196793,
        "abs_return_acf_1": 0.2859071679739611,
        "abs_return_acf_5": 0.29485003226114237,
        "abs_return_acf_20": 0.18568040394142094,
        "quantile_01": -0.05595294290895381,
        "quantile_99": 0.05017894042390026,
        "hill_tail_index": 3.6946263043957894
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022330878815046737,
        "excess_kurtosis": 9.730752614625498,
        "return_acf_1": -0.27200111241916314,
        "abs_return_acf_1": 0.5223425339729517,
        "abs_return_acf_5": 0.49106981117397897,
        "abs_return_acf_20": 0.3957168431364699,
        "quantile_01": -0.07534748196660966,
        "quantile_99": 0.07074889839028235,
        "hill_tail_index": 3.3997083638415226
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021409762561193094,
        "excess_kurtosis": 10.563983455438741,
        "return_acf_1": -0.1705733656098626,
        "abs_return_acf_1": 0.3931624791891794,
        "abs_return_acf_5": 0.4683637505503666,
        "abs_return_acf_20": 0.33115152131068787,
        "quantile_01": -0.08490428720453262,
        "quantile_99": 0.06532685000170467,
        "hill_tail_index": 2.8711411164512
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018350476814589168,
        "excess_kurtosis": 7.686409394409571,
        "return_acf_1": -0.17565477333292212,
        "abs_return_acf_1": 0.26868744220233887,
        "abs_return_acf_5": 0.25006175154753285,
        "abs_return_acf_20": 0.22655668795657002,
        "quantile_01": -0.05471316360693714,
        "quantile_99": 0.04567507898340088,
        "hill_tail_index": 2.823262331557235
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01808339046893291,
        "excess_kurtosis": 5.188897561117898,
        "return_acf_1": -0.11828885082694121,
        "abs_return_acf_1": 0.31776622337675114,
        "abs_return_acf_5": 0.2956873321500948,
        "abs_return_acf_20": 0.25811695643441473,
        "quantile_01": -0.05121845642404813,
        "quantile_99": 0.05402273756457706,
        "hill_tail_index": 3.4134159383323213
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02142421913193291,
        "excess_kurtosis": 10.70866543525007,
        "return_acf_1": -0.21933514050145866,
        "abs_return_acf_1": 0.38531770051883263,
        "abs_return_acf_5": 0.42484174957789134,
        "abs_return_acf_20": 0.32260756315230515,
        "quantile_01": -0.07751705487890165,
        "quantile_99": 0.05890815410580877,
        "hill_tail_index": 2.6475916885846877
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02033264007013243,
        "excess_kurtosis": 8.579058134882416,
        "return_acf_1": -0.2493632319038088,
        "abs_return_acf_1": 0.4651256968164435,
        "abs_return_acf_5": 0.45386449498505255,
        "abs_return_acf_20": 0.40609787024273164,
        "quantile_01": -0.0672233090946382,
        "quantile_99": 0.054277452143265646,
        "hill_tail_index": 2.92418330573901
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021243676895027003,
        "excess_kurtosis": 5.6176966284790435,
        "return_acf_1": -0.17431920152216449,
        "abs_return_acf_1": 0.3152985883233828,
        "abs_return_acf_5": 0.37326788614246237,
        "abs_return_acf_20": 0.30840234563786245,
        "quantile_01": -0.06948557064886489,
        "quantile_99": 0.05546697532324545,
        "hill_tail_index": 3.779621991659949
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021766272687545225,
        "excess_kurtosis": 8.72861621466214,
        "return_acf_1": -0.21235297079565765,
        "abs_return_acf_1": 0.40035593957256954,
        "abs_return_acf_5": 0.41577684912453433,
        "abs_return_acf_20": 0.3559856939134862,
        "quantile_01": -0.06580384338397524,
        "quantile_99": 0.06236223870806288,
        "hill_tail_index": 3.7539519319801475
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022663646211002798,
        "excess_kurtosis": 13.649269833208187,
        "return_acf_1": -0.18103793298677584,
        "abs_return_acf_1": 0.4099433712482952,
        "abs_return_acf_5": 0.4790595929818982,
        "abs_return_acf_20": 0.38089797360784666,
        "quantile_01": -0.07947424933481675,
        "quantile_99": 0.06332224603937447,
        "hill_tail_index": 2.4243971241524602
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01845424149973061,
        "excess_kurtosis": 4.505851877164231,
        "return_acf_1": -0.08217022450402157,
        "abs_return_acf_1": 0.2952887683930739,
        "abs_return_acf_5": 0.3159111384223827,
        "abs_return_acf_20": 0.22599183406092746,
        "quantile_01": -0.05615738534092812,
        "quantile_99": 0.04634140830606895,
        "hill_tail_index": 3.79323504508732
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018088171168325062,
        "excess_kurtosis": 3.695137089506739,
        "return_acf_1": -0.1614104489482225,
        "abs_return_acf_1": 0.33197106219499833,
        "abs_return_acf_5": 0.2786486161330932,
        "abs_return_acf_20": 0.2898785187095727,
        "quantile_01": -0.05040576122577628,
        "quantile_99": 0.04738518935319742,
        "hill_tail_index": 3.6635916625557923
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01948709219472269,
        "excess_kurtosis": 4.6385821644818925,
        "return_acf_1": -0.17858740885695606,
        "abs_return_acf_1": 0.3698969630358364,
        "abs_return_acf_5": 0.326123245992852,
        "abs_return_acf_20": 0.28252852117092825,
        "quantile_01": -0.059995830471683234,
        "quantile_99": 0.05873417929744095,
        "hill_tail_index": 3.977983423942215
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020555408727194975,
        "excess_kurtosis": 4.692888940967699,
        "return_acf_1": -0.12196415661546463,
        "abs_return_acf_1": 0.2736363927605165,
        "abs_return_acf_5": 0.30339778751951363,
        "abs_return_acf_20": 0.3155492334615212,
        "quantile_01": -0.061110175688699774,
        "quantile_99": 0.061385651200037535,
        "hill_tail_index": 4.63349589256238
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01930306068520315,
        "excess_kurtosis": 10.879995405383118,
        "return_acf_1": -0.1640510499319196,
        "abs_return_acf_1": 0.38064974062098134,
        "abs_return_acf_5": 0.3866714237335038,
        "abs_return_acf_20": 0.2134154552318864,
        "quantile_01": -0.05175531111678856,
        "quantile_99": 0.05185588334039556,
        "hill_tail_index": 2.0307927615946357
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022665766750148895,
        "excess_kurtosis": 11.626958358125627,
        "return_acf_1": -0.2273882393916361,
        "abs_return_acf_1": 0.4263382296264771,
        "abs_return_acf_5": 0.43021177159404467,
        "abs_return_acf_20": 0.3598694215567271,
        "quantile_01": -0.07672023609508925,
        "quantile_99": 0.07603014884344395,
        "hill_tail_index": 2.6742057856889203
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01967504437619682,
        "excess_kurtosis": 7.23780495362729,
        "return_acf_1": -0.1377934820123529,
        "abs_return_acf_1": 0.43691832536211445,
        "abs_return_acf_5": 0.36227973016907666,
        "abs_return_acf_20": 0.31236382096588305,
        "quantile_01": -0.06923106697425228,
        "quantile_99": 0.05182378371918625,
        "hill_tail_index": 3.1579930610614753
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017997435768009086,
        "excess_kurtosis": 4.514442051543368,
        "return_acf_1": -0.14145628660735757,
        "abs_return_acf_1": 0.2629193863482472,
        "abs_return_acf_5": 0.24358835411771507,
        "abs_return_acf_20": 0.2531723592708337,
        "quantile_01": -0.050902016549389195,
        "quantile_99": 0.046749109718458,
        "hill_tail_index": 3.5961121711325195
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019772864114792996,
        "excess_kurtosis": 6.5788178401873925,
        "return_acf_1": -0.1809088715690775,
        "abs_return_acf_1": 0.37252046023205354,
        "abs_return_acf_5": 0.4103206085097419,
        "abs_return_acf_20": 0.348329165121186,
        "quantile_01": -0.07052499840463303,
        "quantile_99": 0.0582809843242127,
        "hill_tail_index": 3.9397338783185036
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.0185582012948459,
        "excess_kurtosis": 9.978074012858867,
        "return_acf_1": -0.13428821964501322,
        "abs_return_acf_1": 0.37899350967031264,
        "abs_return_acf_5": 0.3253315084103052,
        "abs_return_acf_20": 0.23999108850515313,
        "quantile_01": -0.05565756403476141,
        "quantile_99": 0.05008911777453391,
        "hill_tail_index": 2.9926402295489756
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018350345252933203,
        "excess_kurtosis": 3.701408439294214,
        "return_acf_1": -0.14636584928112198,
        "abs_return_acf_1": 0.3604844451010131,
        "abs_return_acf_5": 0.35341366035581795,
        "abs_return_acf_20": 0.3306384636596919,
        "quantile_01": -0.056729888227727454,
        "quantile_99": 0.047113901366107984,
        "hill_tail_index": 3.392238374402991
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018749962634681108,
        "excess_kurtosis": 10.340812869377608,
        "return_acf_1": -0.16014093749590483,
        "abs_return_acf_1": 0.3642003979804117,
        "abs_return_acf_5": 0.4034854786822082,
        "abs_return_acf_20": 0.2556139002440297,
        "quantile_01": -0.057448780400082784,
        "quantile_99": 0.04638398676275628,
        "hill_tail_index": 2.70125772605169
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019588802536236186,
        "excess_kurtosis": 5.547293334961267,
        "return_acf_1": -0.0624310920114278,
        "abs_return_acf_1": 0.3457178790745445,
        "abs_return_acf_5": 0.400935485705606,
        "abs_return_acf_20": 0.31778044429036867,
        "quantile_01": -0.06864371872367196,
        "quantile_99": 0.055773401857582415,
        "hill_tail_index": 3.3630904091950224
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
