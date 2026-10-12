# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27079
Run ID: `19aaf23c01f343c23146382ad1458f6b261d7679de5bb443601645a4f449b095`
Result fingerprint: `de81ed3c1a1be73847658c3a83ca8ee2e44ee7573e96f4753b98a777f795be33`

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
    "equal_weight_sd": -0.5552413111214138,
    "equal_weight_raw": -8.32861966682121,
    "fixed_start_cap_weight_sd": -0.5325773487888807,
    "fixed_start_cap_weight_raw": -7.988660231833214,
    "end_cap_weight_sd": -0.5311349778241374,
    "end_cap_weight_raw": -7.96702466736206
  },
  "full_period_change": {
    "equal_weight_sd": -0.8946817873118885,
    "equal_weight_raw": -13.420226809678327
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8406454116505132,
    "inflation_mean_sd": 0.5517662037037037
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3608113009420041,
    "equal_weight_raw": 5.41216951413006,
    "fixed_start_cap_weight_sd": 0.37296836518585874,
    "fixed_start_cap_weight_raw": 5.594525477787879,
    "end_cap_weight_sd": 0.38144522539598485,
    "end_cap_weight_raw": 5.721678380939773
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5157142857142826,
      "change_raw": -7.735714285714239,
      "decay_adjusted_gain_sd": 0.4366666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5424710370713872,
      "change_raw": -8.137065556070809,
      "decay_adjusted_gain_sd": 0.3088888888888917
    },
    "small": {
      "count": 18,
      "change_sd": -0.5682142857142825,
      "change_raw": -8.523214285714237,
      "decay_adjusted_gain_sd": 0.37412994601444927
    },
    "large_minus_small_sd": 0.05249999999999988,
    "large_minus_small_raw": 0.7874999999999982
  },
  "inflation": {
    "initial_mean_sd": 0.24925000000000003,
    "final_mean_sd": 0.58825,
    "mean_sd": 0.3907701221204552,
    "mean_absolute_raw_gap": 5.861551831806827,
    "final_absolute_raw_gap": 8.82375,
    "mean_range_fraction": 0.05861551831806827
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.18666666666666668,
    "initial_wealth_share": 0.16824560822391968,
    "final_wealth_share": 0.140662933471162
  },
  "pricing_slope": {
    "mean": -0.00032437462236264205,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.5198987275607174,
    "real_improvement_cost": 0.43838997083349834,
    "washing_cost": 0.08150875672721898,
    "fine_transfer": 0.015979532853721688,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.5358782604144391,
    "resource_cost_fraction_initial_cap": 0.01732995758535725,
    "private_net_outflow_fraction_initial_cap": 0.017862608680481305,
    "fine_transfer_fraction_initial_cap": 0.0005326510951240563,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002159765288307147,
    "unapplied_final_day_resource_cost": 0.09539167000709867
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 20.82009140327427,
    "beneficial_raw_gain_per_resource_cost": 312.30137104911404,
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
    "accrued_cost": 2.9387524213294776,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.03743805486099884,
    "accrued_cost_fraction_initial_cap": 0.09795841404431593,
    "mean_contract_rate": 0.041320688642170686,
    "maximum_ledger_error": 5.759824041329242e-20
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
    "maximum_relative_cash_error": 2.2316448100191634e-15,
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
      "minimum": -0.19125958626127756,
      "maximum": -0.04519139119669925,
      "mean": -0.13927652500071197,
      "median": -0.14481162087616567,
      "quantile_05": -0.1892666653422031,
      "quantile_95": -0.07537765059622846
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
      "minimum": 0.21784456678143646,
      "maximum": 0.7628367794864911,
      "mean": 0.44247519995074397,
      "median": 0.4032579008648835,
      "quantile_05": 0.281474100119569,
      "quantile_95": 0.6814347472377332
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
        "daily_volatility": 0.01981134900015594,
        "excess_kurtosis": 10.696354044895719,
        "return_acf_1": -0.0965211256989153,
        "abs_return_acf_1": 0.43740395376004043,
        "abs_return_acf_5": 0.32089534760102456,
        "abs_return_acf_20": 0.34299481605720933,
        "quantile_01": -0.05243972617331244,
        "quantile_99": 0.06602748431174145,
        "hill_tail_index": 2.3016376870817297
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021240821311896217,
        "excess_kurtosis": 12.107424686186283,
        "return_acf_1": -0.10728839382325077,
        "abs_return_acf_1": 0.4049712084251213,
        "abs_return_acf_5": 0.44283576528523644,
        "abs_return_acf_20": 0.297355272870645,
        "quantile_01": -0.07095400599071075,
        "quantile_99": 0.05787944650044121,
        "hill_tail_index": 2.964080730334338
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018959688837008538,
        "excess_kurtosis": 11.407896187551293,
        "return_acf_1": -0.10609518016940128,
        "abs_return_acf_1": 0.35883558884998007,
        "abs_return_acf_5": 0.32091592453384243,
        "abs_return_acf_20": 0.3076240377135721,
        "quantile_01": -0.05633508614525776,
        "quantile_99": 0.05194681441154005,
        "hill_tail_index": 3.204830974327645
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01716317814005986,
        "excess_kurtosis": 12.502610838579667,
        "return_acf_1": -0.1815220912108124,
        "abs_return_acf_1": 0.3885580610003171,
        "abs_return_acf_5": 0.31705496222546453,
        "abs_return_acf_20": 0.229346886597822,
        "quantile_01": -0.05174630238899959,
        "quantile_99": 0.047856810095802574,
        "hill_tail_index": 2.566754225956359
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017071950832281586,
        "excess_kurtosis": 4.620876604524092,
        "return_acf_1": -0.1869697207148774,
        "abs_return_acf_1": 0.2736572018276461,
        "abs_return_acf_5": 0.2875266434000117,
        "abs_return_acf_20": 0.24625799833099205,
        "quantile_01": -0.045030414813437926,
        "quantile_99": 0.04858056270188523,
        "hill_tail_index": 2.718968609277875
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021032336091481724,
        "excess_kurtosis": 10.191299866000003,
        "return_acf_1": -0.1585825565793915,
        "abs_return_acf_1": 0.4555548039371868,
        "abs_return_acf_5": 0.40142825149073913,
        "abs_return_acf_20": 0.3133660359882073,
        "quantile_01": -0.07048429939559184,
        "quantile_99": 0.06444604269510872,
        "hill_tail_index": 2.585445436182871
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018918001774168584,
        "excess_kurtosis": 6.574983149740024,
        "return_acf_1": -0.10939601340641657,
        "abs_return_acf_1": 0.2088395992088702,
        "abs_return_acf_5": 0.3566891717790878,
        "abs_return_acf_20": 0.1949388607453552,
        "quantile_01": -0.05933970722193921,
        "quantile_99": 0.05533355544103176,
        "hill_tail_index": 4.437405125571083
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017505477650306574,
        "excess_kurtosis": 3.200857112095144,
        "return_acf_1": -0.13843814831504628,
        "abs_return_acf_1": 0.2136173057543774,
        "abs_return_acf_5": 0.21311471622562558,
        "abs_return_acf_20": 0.24862289513742744,
        "quantile_01": -0.05204017575730268,
        "quantile_99": 0.05205536111852146,
        "hill_tail_index": 4.351304273167466
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021390386365821388,
        "excess_kurtosis": 9.813290890519,
        "return_acf_1": -0.04519139119669925,
        "abs_return_acf_1": 0.39896846875262637,
        "abs_return_acf_5": 0.3491039122759145,
        "abs_return_acf_20": 0.2989291549671358,
        "quantile_01": -0.0646790835571303,
        "quantile_99": 0.060637209286250396,
        "hill_tail_index": 2.907715565838866
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02033734309326433,
        "excess_kurtosis": 14.689883312739646,
        "return_acf_1": -0.09000730495658539,
        "abs_return_acf_1": 0.3856112473958579,
        "abs_return_acf_5": 0.31833277400952537,
        "abs_return_acf_20": 0.3496121955438507,
        "quantile_01": -0.06265320629298782,
        "quantile_99": 0.062445489585401914,
        "hill_tail_index": 2.875122185468837
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019507598234394553,
        "excess_kurtosis": 8.518062090574649,
        "return_acf_1": -0.18316912543360492,
        "abs_return_acf_1": 0.4087718399525122,
        "abs_return_acf_5": 0.44163128440782184,
        "abs_return_acf_20": 0.2930585848025112,
        "quantile_01": -0.05492535913576374,
        "quantile_99": 0.06410535398588194,
        "hill_tail_index": 2.715085965693686
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019001368297430248,
        "excess_kurtosis": 4.893077114641745,
        "return_acf_1": -0.11064302630061638,
        "abs_return_acf_1": 0.29941908201136513,
        "abs_return_acf_5": 0.24872394137879147,
        "abs_return_acf_20": 0.26727235570118707,
        "quantile_01": -0.05573148403619352,
        "quantile_99": 0.05713323894674458,
        "hill_tail_index": 3.7782398913554287
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02006815780308798,
        "excess_kurtosis": 10.48903292701473,
        "return_acf_1": -0.14134620375282828,
        "abs_return_acf_1": 0.3423577766488844,
        "abs_return_acf_5": 0.3968181016753203,
        "abs_return_acf_20": 0.24403718256779242,
        "quantile_01": -0.06421289089413351,
        "quantile_99": 0.06358891982006719,
        "hill_tail_index": 2.6549180008326747
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02169277505186074,
        "excess_kurtosis": 11.431953753763429,
        "return_acf_1": -0.14573978831321058,
        "abs_return_acf_1": 0.44049940128717247,
        "abs_return_acf_5": 0.45546526788391056,
        "abs_return_acf_20": 0.3442109474254062,
        "quantile_01": -0.06389712620539174,
        "quantile_99": 0.056056502544658264,
        "hill_tail_index": 2.6799756809348554
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020054095213408226,
        "excess_kurtosis": 6.903160660764597,
        "return_acf_1": -0.1911459836736514,
        "abs_return_acf_1": 0.39342417999046075,
        "abs_return_acf_5": 0.3681407603293159,
        "abs_return_acf_20": 0.30206268290881766,
        "quantile_01": -0.053081356358619776,
        "quantile_99": 0.05709645674396936,
        "hill_tail_index": 2.8408142507418854
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02171076024427445,
        "excess_kurtosis": 7.089185792035995,
        "return_acf_1": -0.14101540809147228,
        "abs_return_acf_1": 0.49758794656029465,
        "abs_return_acf_5": 0.44168082546206416,
        "abs_return_acf_20": 0.3731374700489743,
        "quantile_01": -0.06989422542139938,
        "quantile_99": 0.07422626563188423,
        "hill_tail_index": 4.123885138024098
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021058632767803585,
        "excess_kurtosis": 9.596824885553511,
        "return_acf_1": -0.15369985330152502,
        "abs_return_acf_1": 0.5184483083729295,
        "abs_return_acf_5": 0.35875524010011245,
        "abs_return_acf_20": 0.4005964013546407,
        "quantile_01": -0.06942257135482656,
        "quantile_99": 0.07101277677836153,
        "hill_tail_index": 4.248268942284489
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018115626614842666,
        "excess_kurtosis": 14.388870578944669,
        "return_acf_1": -0.19125958626127756,
        "abs_return_acf_1": 0.3444782998472861,
        "abs_return_acf_5": 0.3332552280190322,
        "abs_return_acf_20": 0.3210171320178065,
        "quantile_01": -0.04821965129592662,
        "quantile_99": 0.055130201852010965,
        "hill_tail_index": 2.1439386769643503
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019149817752259327,
        "excess_kurtosis": 8.715032854127957,
        "return_acf_1": -0.1516770415920916,
        "abs_return_acf_1": 0.3272884897114235,
        "abs_return_acf_5": 0.361277754880134,
        "abs_return_acf_20": 0.30491240735486147,
        "quantile_01": -0.06214434519109442,
        "quantile_99": 0.05528185804302958,
        "hill_tail_index": 2.966312433019508
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020542837170454256,
        "excess_kurtosis": 10.075285485354572,
        "return_acf_1": -0.15375713152952933,
        "abs_return_acf_1": 0.4503511137727744,
        "abs_return_acf_5": 0.39686739579530084,
        "abs_return_acf_20": 0.3552157315463865,
        "quantile_01": -0.06273742663475267,
        "quantile_99": 0.056408300891956004,
        "hill_tail_index": 3.109637484039245
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02002288284968096,
        "excess_kurtosis": 5.9729043518439475,
        "return_acf_1": -0.14708115001413394,
        "abs_return_acf_1": 0.40075116169583713,
        "abs_return_acf_5": 0.38627150156816764,
        "abs_return_acf_20": 0.36377598306855496,
        "quantile_01": -0.05786905074716905,
        "quantile_99": 0.05849140269405112,
        "hill_tail_index": 3.334636527947956
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018090734460323818,
        "excess_kurtosis": 6.473823936196828,
        "return_acf_1": -0.1692377358419048,
        "abs_return_acf_1": 0.366236054693705,
        "abs_return_acf_5": 0.34490612827075556,
        "abs_return_acf_20": 0.26222067957070044,
        "quantile_01": -0.05063667531333454,
        "quantile_99": 0.04846140985681092,
        "hill_tail_index": 3.8038089430361146
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018657275224928896,
        "excess_kurtosis": 7.049722821107476,
        "return_acf_1": -0.14388345343912076,
        "abs_return_acf_1": 0.28812549185870623,
        "abs_return_acf_5": 0.27162219446340924,
        "abs_return_acf_20": 0.26660550888818396,
        "quantile_01": -0.05384122208159002,
        "quantile_99": 0.0520777710918931,
        "hill_tail_index": 3.296831760105685
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019761482563092514,
        "excess_kurtosis": 3.167243122053222,
        "return_acf_1": -0.12733802239126618,
        "abs_return_acf_1": 0.32415755132211893,
        "abs_return_acf_5": 0.28934354409730445,
        "abs_return_acf_20": 0.21391164077249286,
        "quantile_01": -0.05610018839064768,
        "quantile_99": 0.05325012572668941,
        "hill_tail_index": 4.0598305790176825
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01941917312445713,
        "excess_kurtosis": 5.643040689176443,
        "return_acf_1": -0.1624769242153657,
        "abs_return_acf_1": 0.38187526365146035,
        "abs_return_acf_5": 0.3274059636663136,
        "abs_return_acf_20": 0.2703414619177078,
        "quantile_01": -0.06097697045862734,
        "quantile_99": 0.05505647829789956,
        "hill_tail_index": 4.150949729897118
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01879159275665777,
        "excess_kurtosis": 8.903840416747201,
        "return_acf_1": -0.1855748540699619,
        "abs_return_acf_1": 0.3341873159402881,
        "abs_return_acf_5": 0.34920326205337654,
        "abs_return_acf_20": 0.2677048195526417,
        "quantile_01": -0.05450236602380713,
        "quantile_99": 0.04718125117186694,
        "hill_tail_index": 2.7007698339255803
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.016417392391212274,
        "excess_kurtosis": 7.05256543348216,
        "return_acf_1": -0.10676423535130394,
        "abs_return_acf_1": 0.3899021014297086,
        "abs_return_acf_5": 0.3844624562878109,
        "abs_return_acf_20": 0.2748522401835734,
        "quantile_01": -0.051869897024022,
        "quantile_99": 0.0446107212068879,
        "hill_tail_index": 3.011148955622419
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019266234412055855,
        "excess_kurtosis": 5.298844027548199,
        "return_acf_1": -0.16390392042973584,
        "abs_return_acf_1": 0.34332212846191523,
        "abs_return_acf_5": 0.2843390795251905,
        "abs_return_acf_20": 0.24225098992753363,
        "quantile_01": -0.059413570367344515,
        "quantile_99": 0.04809692824602048,
        "hill_tail_index": 2.765217677294178
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018814545019343386,
        "excess_kurtosis": 5.747965626826256,
        "return_acf_1": -0.12516244655506287,
        "abs_return_acf_1": 0.31456108086446893,
        "abs_return_acf_5": 0.3232669661073782,
        "abs_return_acf_20": 0.266822914920403,
        "quantile_01": -0.048302727850992794,
        "quantile_99": 0.05718403821967525,
        "hill_tail_index": 3.3647771778606597
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021066601752866534,
        "excess_kurtosis": 8.548289273003318,
        "return_acf_1": -0.06340793339229993,
        "abs_return_acf_1": 0.3982828020623759,
        "abs_return_acf_5": 0.41260226278974343,
        "abs_return_acf_20": 0.31556054178264714,
        "quantile_01": -0.06485642788145159,
        "quantile_99": 0.0666136523329816,
        "hill_tail_index": 3.1027554721003194
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
