# Disclosure-market run

Purpose: development
Domain: esg
Seed: 25102
Run ID: `af4a8bf099bbede474fccfe2e2b197416e7423791fc42533c3422b3fa10dfc47`
Result fingerprint: `51a70fb13eceefc57da2501d91215d3c2c1c6b40cf8991ffa940f34f8f8c9805`

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
    "equal_weight_sd": -0.9343809523809495,
    "equal_weight_raw": -14.01571428571424,
    "fixed_start_cap_weight_sd": -0.9364938812193603,
    "fixed_start_cap_weight_raw": -14.047408218290403,
    "end_cap_weight_sd": -0.9345156029531526,
    "end_cap_weight_raw": -14.017734044297288
  },
  "full_period_change": {
    "equal_weight_sd": -1.4059047619047573,
    "equal_weight_raw": -21.08857142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.3093826058201015,
    "inflation_mean_sd": 0.002326058201058201
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.018000000000002896,
    "equal_weight_raw": 0.2700000000000434,
    "fixed_start_cap_weight_sd": 0.015887071161592017,
    "fixed_start_cap_weight_raw": 0.23830606742388022,
    "end_cap_weight_sd": 0.01786534942779957,
    "end_cap_weight_raw": 0.2679802414169936
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.952380952380949,
      "change_raw": -14.285714285714235,
      "decay_adjusted_gain_sd": 3.23815048849004e-15
    },
    "mid": {
      "count": 9,
      "change_sd": -0.918214285714283,
      "change_raw": -13.773214285714245,
      "decay_adjusted_gain_sd": 0.03416666666666927
    },
    "small": {
      "count": 18,
      "change_sd": -0.9394642857142826,
      "change_raw": -14.091964285714239,
      "decay_adjusted_gain_sd": 0.012916666666669649
    },
    "large_minus_small_sd": -0.012916666666666354,
    "large_minus_small_raw": -0.19374999999999531
  },
  "inflation": {
    "initial_mean_sd": 0.0013333333333333333,
    "final_mean_sd": 0.002333333333333333,
    "mean_sd": 0.0017157923952262003,
    "mean_absolute_raw_gap": 0.025736885928392815,
    "final_absolute_raw_gap": 0.03499999999999967,
    "mean_range_fraction": 0.00025736885928392814
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.3859028487988339,
    "final_wealth_share": 0.43775532824052704
  },
  "pricing_slope": {
    "mean": -0.001337406009577064,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 2.797741291771368e-05,
    "real_improvement_cost": 2.7257164861542603e-05,
    "washing_cost": 7.202480561710731e-07,
    "fine_transfer": 4.5538401768333104e-05,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 7.351581468604678e-05,
    "resource_cost_fraction_initial_cap": 9.325804305904557e-07,
    "private_net_outflow_fraction_initial_cap": 2.450527156201558e-06,
    "fine_transfer_fraction_initial_cap": 1.517946725611103e-06,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 3.2169372479239873e-06,
    "unapplied_final_day_resource_cost": 1.1708432320700863e-06
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 19301.28427486553,
    "beneficial_raw_gain_per_resource_cost": 289519.26412298303,
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
    "accrued_cost": 2.9434961076550588,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.032694368535418565,
    "accrued_cost_fraction_initial_cap": 0.09811653692183525,
    "mean_contract_rate": 0.04008710227853896,
    "maximum_ledger_error": 6.268043809681823e-20
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
    "maximum_relative_cash_error": 1.968083141863449e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.26729740016314,
      "maximum": -0.05237088098772196,
      "mean": -0.1661100045224889,
      "median": -0.17083099079119002,
      "quantile_05": -0.24446521928128334,
      "quantile_95": -0.0798489122213274
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
      "minimum": 0.17699037589486338,
      "maximum": 0.8465760716403817,
      "mean": 0.5316068623620391,
      "median": 0.6207330063505458,
      "quantile_05": 0.22722691360524952,
      "quantile_95": 0.8046202664028128
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
        "daily_volatility": 0.02329787743369156,
        "excess_kurtosis": 35.91309158654101,
        "return_acf_1": -0.24285566484292476,
        "abs_return_acf_1": 0.4908992998159891,
        "abs_return_acf_5": 0.42242456080708435,
        "abs_return_acf_20": 0.40116751358968894,
        "quantile_01": -0.07570912073060207,
        "quantile_99": 0.049352562475860624,
        "hill_tail_index": 1.808531612422161
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019297633494314206,
        "excess_kurtosis": 8.8478390631209,
        "return_acf_1": -0.07549825496355736,
        "abs_return_acf_1": 0.43217422263557137,
        "abs_return_acf_5": 0.39303293025034564,
        "abs_return_acf_20": 0.2824575446353115,
        "quantile_01": -0.056919711328604,
        "quantile_99": 0.053718703997695294,
        "hill_tail_index": 3.294205968153443
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019907522479911156,
        "excess_kurtosis": 25.838073470367124,
        "return_acf_1": -0.2261125556928373,
        "abs_return_acf_1": 0.4178679945764651,
        "abs_return_acf_5": 0.3052757618070872,
        "abs_return_acf_20": 0.27633676963724135,
        "quantile_01": -0.06619550840907101,
        "quantile_99": 0.04033160584902767,
        "hill_tail_index": 1.5256973111420165
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02102400366567811,
        "excess_kurtosis": 16.5739133972214,
        "return_acf_1": -0.24146934273476728,
        "abs_return_acf_1": 0.369129344758932,
        "abs_return_acf_5": 0.32006100886973265,
        "abs_return_acf_20": 0.28447879773358054,
        "quantile_01": -0.07189401336502572,
        "quantile_99": 0.053430627965445156,
        "hill_tail_index": 1.9567528364767612
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018569387658516293,
        "excess_kurtosis": 5.452423888887035,
        "return_acf_1": -0.12216914153414658,
        "abs_return_acf_1": 0.30888205626735676,
        "abs_return_acf_5": 0.27396969111631364,
        "abs_return_acf_20": 0.2976596774014883,
        "quantile_01": -0.05856192074737428,
        "quantile_99": 0.05032162859768631,
        "hill_tail_index": 3.4074378973056665
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018827990562475486,
        "excess_kurtosis": 4.535574649030741,
        "return_acf_1": -0.10633861809757231,
        "abs_return_acf_1": 0.3214770750837039,
        "abs_return_acf_5": 0.31086434204530733,
        "abs_return_acf_20": 0.1865567792946189,
        "quantile_01": -0.05990101891312259,
        "quantile_99": 0.05119786298768737,
        "hill_tail_index": 3.839992748335213
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019302944080298253,
        "excess_kurtosis": 6.543295712202143,
        "return_acf_1": -0.17179264683572784,
        "abs_return_acf_1": 0.3076949339601115,
        "abs_return_acf_5": 0.310230511191469,
        "abs_return_acf_20": 0.31837195963222964,
        "quantile_01": -0.06107425927280135,
        "quantile_99": 0.04919165550769242,
        "hill_tail_index": 2.7923919156636874
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02427454497820114,
        "excess_kurtosis": 29.51685091276508,
        "return_acf_1": -0.20402111907523454,
        "abs_return_acf_1": 0.5059845366899586,
        "abs_return_acf_5": 0.41352546634211546,
        "abs_return_acf_20": 0.4047773940910478,
        "quantile_01": -0.08221586414073129,
        "quantile_99": 0.05884255225707047,
        "hill_tail_index": 1.985113038557988
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020657851501027814,
        "excess_kurtosis": 10.90693593566934,
        "return_acf_1": -0.18346836009231124,
        "abs_return_acf_1": 0.423711636900634,
        "abs_return_acf_5": 0.3200494947200674,
        "abs_return_acf_20": 0.32214012431057465,
        "quantile_01": -0.06785216556614179,
        "quantile_99": 0.05907063269528817,
        "hill_tail_index": 2.8896588049565355
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022140328316476394,
        "excess_kurtosis": 15.39772027521607,
        "return_acf_1": -0.13584812206931157,
        "abs_return_acf_1": 0.4547801432941117,
        "abs_return_acf_5": 0.4443806557625096,
        "abs_return_acf_20": 0.39421125549160596,
        "quantile_01": -0.07777839220802114,
        "quantile_99": 0.05706972022025201,
        "hill_tail_index": 2.6328187375154615
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022725531477608037,
        "excess_kurtosis": 23.863216412803027,
        "return_acf_1": -0.15796035295520394,
        "abs_return_acf_1": 0.3135007135513005,
        "abs_return_acf_5": 0.2605624070857572,
        "abs_return_acf_20": 0.187299877594813,
        "quantile_01": -0.06810614152701579,
        "quantile_99": 0.05338815772380293,
        "hill_tail_index": 2.052767025640346
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02007962277526828,
        "excess_kurtosis": 20.234979435730832,
        "return_acf_1": -0.13262527271002195,
        "abs_return_acf_1": 0.36825449341540833,
        "abs_return_acf_5": 0.33973807450907934,
        "abs_return_acf_20": 0.3012848747364652,
        "quantile_01": -0.06561238773167283,
        "quantile_99": 0.05448018866503902,
        "hill_tail_index": 2.114928846528797
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024340327172898336,
        "excess_kurtosis": 28.376275250586446,
        "return_acf_1": -0.24578212745812217,
        "abs_return_acf_1": 0.5120652624856115,
        "abs_return_acf_5": 0.41278243908989787,
        "abs_return_acf_20": 0.412014891675666,
        "quantile_01": -0.06852977265215981,
        "quantile_99": 0.06819245065831092,
        "hill_tail_index": 2.1128414414723604
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021957255430864,
        "excess_kurtosis": 36.025012005184855,
        "return_acf_1": -0.21800386684153605,
        "abs_return_acf_1": 0.48435436394464226,
        "abs_return_acf_5": 0.44229346662006985,
        "abs_return_acf_20": 0.2863567325024773,
        "quantile_01": -0.07672525230116892,
        "quantile_99": 0.04850398980734237,
        "hill_tail_index": 1.6210566547062764
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02323155879714821,
        "excess_kurtosis": 19.6000495468127,
        "return_acf_1": -0.12482017169238083,
        "abs_return_acf_1": 0.3944381059918768,
        "abs_return_acf_5": 0.4055405971151127,
        "abs_return_acf_20": 0.2834889802623011,
        "quantile_01": -0.08050590853437548,
        "quantile_99": 0.06105522289631025,
        "hill_tail_index": 2.071523910459706
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021400200002274123,
        "excess_kurtosis": 26.456241846028988,
        "return_acf_1": -0.16986933474665222,
        "abs_return_acf_1": 0.4225704082178415,
        "abs_return_acf_5": 0.3995406987765483,
        "abs_return_acf_20": 0.2775668486534784,
        "quantile_01": -0.07158356043120415,
        "quantile_99": 0.05819651150994944,
        "hill_tail_index": 2.1716076642880693
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023742976146259413,
        "excess_kurtosis": 29.57762677730853,
        "return_acf_1": -0.2316419206509871,
        "abs_return_acf_1": 0.5355618645171581,
        "abs_return_acf_5": 0.46184380617373316,
        "abs_return_acf_20": 0.36577610183613135,
        "quantile_01": -0.08193653600669167,
        "quantile_99": 0.05091705392170977,
        "hill_tail_index": 1.6872044792392498
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02150295102888689,
        "excess_kurtosis": 28.075227835468528,
        "return_acf_1": -0.1746892486729894,
        "abs_return_acf_1": 0.45410564494025524,
        "abs_return_acf_5": 0.44980185496311154,
        "abs_return_acf_20": 0.37258658152101676,
        "quantile_01": -0.07639334690179488,
        "quantile_99": 0.04590757899158125,
        "hill_tail_index": 1.542384877768216
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023279887353872788,
        "excess_kurtosis": 42.626232581048775,
        "return_acf_1": -0.26729740016314,
        "abs_return_acf_1": 0.5107878845891974,
        "abs_return_acf_5": 0.4005472328915162,
        "abs_return_acf_20": 0.3321806113826738,
        "quantile_01": -0.07773486506361826,
        "quantile_99": 0.055285367121185855,
        "hill_tail_index": 1.6847593042428006
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0186407362049445,
        "excess_kurtosis": 5.840911007466735,
        "return_acf_1": -0.08516638220304627,
        "abs_return_acf_1": 0.4048270293869919,
        "abs_return_acf_5": 0.35131615364320845,
        "abs_return_acf_20": 0.30396316072619073,
        "quantile_01": -0.05750098935100393,
        "quantile_99": 0.04738540159965841,
        "hill_tail_index": 2.9862722645780178
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02071223623765812,
        "excess_kurtosis": 8.714055914787986,
        "return_acf_1": -0.09948114681006974,
        "abs_return_acf_1": 0.3331743377573848,
        "abs_return_acf_5": 0.3723116544867823,
        "abs_return_acf_20": 0.29524413532837585,
        "quantile_01": -0.06038830946224175,
        "quantile_99": 0.06208667987817206,
        "hill_tail_index": 4.0510534582875914
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021690115686799023,
        "excess_kurtosis": 12.552934854246056,
        "return_acf_1": -0.05237088098772196,
        "abs_return_acf_1": 0.3456715224896083,
        "abs_return_acf_5": 0.34956811158432133,
        "abs_return_acf_20": 0.25472426201312615,
        "quantile_01": -0.06051596031971354,
        "quantile_99": 0.06744419151439897,
        "hill_tail_index": 2.25086411403828
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023105061052365154,
        "excess_kurtosis": 25.77793510114606,
        "return_acf_1": -0.14559054953187353,
        "abs_return_acf_1": 0.44320102932424627,
        "abs_return_acf_5": 0.302622731822546,
        "abs_return_acf_20": 0.22854854102046074,
        "quantile_01": -0.0869786485497797,
        "quantile_99": 0.06556944358366569,
        "hill_tail_index": 2.2204942095429554
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01978713843531386,
        "excess_kurtosis": 34.651851992771356,
        "return_acf_1": -0.1720106637038471,
        "abs_return_acf_1": 0.3378789139022518,
        "abs_return_acf_5": 0.2834961388270948,
        "abs_return_acf_20": 0.22497355616046139,
        "quantile_01": -0.05940926176217795,
        "quantile_99": 0.04108346161352679,
        "hill_tail_index": 1.5745895810231325
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019364315688720785,
        "excess_kurtosis": 18.592711909966294,
        "return_acf_1": -0.1759021001684122,
        "abs_return_acf_1": 0.3616461523270632,
        "abs_return_acf_5": 0.3631544885393901,
        "abs_return_acf_20": 0.24031583416829275,
        "quantile_01": -0.060863595417909463,
        "quantile_99": 0.052807006230162226,
        "hill_tail_index": 2.5718050750731534
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022199457673955595,
        "excess_kurtosis": 27.25659563806335,
        "return_acf_1": -0.18238605005118722,
        "abs_return_acf_1": 0.4457995314531934,
        "abs_return_acf_5": 0.35635011707401576,
        "abs_return_acf_20": 0.25437099442466987,
        "quantile_01": -0.0725780707510256,
        "quantile_99": 0.050398636416287834,
        "hill_tail_index": 1.8872951077504134
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015894711154939897,
        "excess_kurtosis": 3.4508096016734315,
        "return_acf_1": -0.16795608317192467,
        "abs_return_acf_1": 0.27690089197639606,
        "abs_return_acf_5": 0.32181956683765833,
        "abs_return_acf_20": 0.18219180472101357,
        "quantile_01": -0.046271306027326445,
        "quantile_99": 0.04456017434687329,
        "hill_tail_index": 4.041254420619157
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0228048362325108,
        "excess_kurtosis": 23.46936436095813,
        "return_acf_1": -0.11851613936777441,
        "abs_return_acf_1": 0.3700401040541115,
        "abs_return_acf_5": 0.398957115301719,
        "abs_return_acf_20": 0.256564260546622,
        "quantile_01": -0.0926020656984345,
        "quantile_99": 0.056423969686347594,
        "hill_tail_index": 1.8058146353080775
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017474960584922487,
        "excess_kurtosis": 2.7497791543522343,
        "return_acf_1": -0.1453559940412148,
        "abs_return_acf_1": 0.2622273607086903,
        "abs_return_acf_5": 0.28570214277341904,
        "abs_return_acf_20": 0.16715351289141864,
        "quantile_01": -0.05381831971372489,
        "quantile_99": 0.04455506667737353,
        "hill_tail_index": 4.084146186150989
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.023144881604645194,
        "excess_kurtosis": 30.216019979376924,
        "return_acf_1": -0.20630062380817046,
        "abs_return_acf_1": 0.5277768990226497,
        "abs_return_acf_5": 0.5190522343168781,
        "abs_return_acf_20": 0.2766369800089013,
        "quantile_01": -0.08351237817405914,
        "quantile_99": 0.052406629271501165,
        "hill_tail_index": 1.6057506849493546
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
Training: False
Coverage status: FAIL
Unseen state share: 0.14
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
