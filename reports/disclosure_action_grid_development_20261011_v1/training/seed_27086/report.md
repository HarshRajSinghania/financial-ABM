# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27086
Run ID: `cef146e697fb6d7312bad30cb56e9e5d3fa64b99bc5b8a56517b142b03e63540`
Result fingerprint: `6a795df2f03924e3c7dd5511dd0f01b440c67fa8dd01b8f2ee9c8ada213a5d05`

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
    "equal_weight_sd": -0.5967976190476157,
    "equal_weight_raw": -8.951964285714238,
    "fixed_start_cap_weight_sd": -0.5899965588088868,
    "fixed_start_cap_weight_raw": -8.849948382133306,
    "end_cap_weight_sd": -0.5917766531265793,
    "end_cap_weight_raw": -8.876649796898688
  },
  "full_period_change": {
    "equal_weight_sd": -0.9440714285714237,
    "equal_weight_raw": -14.161071428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8941048280423236,
    "inflation_mean_sd": 0.7717969576719577
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3555833333333365,
    "equal_weight_raw": 5.333750000000048,
    "fixed_start_cap_weight_sd": 0.3623843935720655,
    "fixed_start_cap_weight_raw": 5.435765903580983,
    "end_cap_weight_sd": 0.36060429925437304,
    "end_cap_weight_raw": 5.409064488815596
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6315476190476157,
      "change_raw": -9.473214285714235,
      "decay_adjusted_gain_sd": 0.32083333333333663
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5729365079365046,
      "change_raw": -8.59404761904757,
      "decay_adjusted_gain_sd": 0.3794444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.6029365079365048,
      "change_raw": -9.044047619047571,
      "decay_adjusted_gain_sd": 0.34944444444444756
    },
    "large_minus_small_sd": -0.02861111111111092,
    "large_minus_small_raw": -0.4291666666666638
  },
  "inflation": {
    "initial_mean_sd": 0.33866666666666667,
    "final_mean_sd": 0.7975833333333333,
    "mean_sd": 0.6001992089925063,
    "mean_absolute_raw_gap": 9.002988134887593,
    "final_absolute_raw_gap": 11.96375,
    "mean_range_fraction": 0.09002988134887593
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.29333333333333333,
    "initial_wealth_share": 0.26220264760018064,
    "final_wealth_share": 0.3554488974271263
  },
  "pricing_slope": {
    "mean": -0.0014280685038150663,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.07460902381655164,
    "real_improvement_cost": 0.05482186925150166,
    "washing_cost": 0.019787154565049994,
    "fine_transfer": 0.015889976804527202,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.09049900062107885,
    "resource_cost_fraction_initial_cap": 0.0024869674605517214,
    "private_net_outflow_fraction_initial_cap": 0.003016633354035962,
    "fine_transfer_fraction_initial_cap": 0.0005296658934842401,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007384809820457212,
    "unapplied_final_day_resource_cost": 0.0016297583377846744
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 142.97868346634988,
    "beneficial_raw_gain_per_resource_cost": 2144.680251995248,
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
    "accrued_cost": 3.1803595149495676,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.20416903875909098,
    "accrued_cost_fraction_initial_cap": 0.10601198383165225,
    "mean_contract_rate": 0.04527414445557289,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "maximum_relative_cash_error": 2.4106345222644918e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.22288012482852532,
      "maximum": -0.022693059533514102,
      "mean": -0.10936503142499203,
      "median": -0.11890395743175586,
      "quantile_05": -0.14497000682309066,
      "quantile_95": -0.05066928227254437
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
      "minimum": 0.34718683370302106,
      "maximum": 0.7793022207792139,
      "mean": 0.6500180581149163,
      "median": 0.663831704905937,
      "quantile_05": 0.501609141311433,
      "quantile_95": 0.740173415273003
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
        "daily_volatility": 0.018398597599078307,
        "excess_kurtosis": 10.339067005020551,
        "return_acf_1": -0.09048376697105091,
        "abs_return_acf_1": 0.30150416877364644,
        "abs_return_acf_5": 0.3671798193062597,
        "abs_return_acf_20": 0.2162322812551508,
        "quantile_01": -0.05478409438713874,
        "quantile_99": 0.04749835472318738,
        "hill_tail_index": 3.010044942863282
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018301921766778074,
        "excess_kurtosis": 6.203754296174726,
        "return_acf_1": -0.1456253793689808,
        "abs_return_acf_1": 0.3067492852793741,
        "abs_return_acf_5": 0.27118174502086256,
        "abs_return_acf_20": 0.23565618212044923,
        "quantile_01": -0.05560320940362526,
        "quantile_99": 0.05074019653318027,
        "hill_tail_index": 3.0136952954580227
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020906263865137636,
        "excess_kurtosis": 10.049636317591768,
        "return_acf_1": -0.07475490717596596,
        "abs_return_acf_1": 0.39756456920560895,
        "abs_return_acf_5": 0.39721682056115665,
        "abs_return_acf_20": 0.33212540972434645,
        "quantile_01": -0.0666468289266272,
        "quantile_99": 0.0493792741053649,
        "hill_tail_index": 2.7747435054298615
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018098166261026127,
        "excess_kurtosis": 8.120365336780672,
        "return_acf_1": -0.10651905197579327,
        "abs_return_acf_1": 0.3484160587932947,
        "abs_return_acf_5": 0.3150273566814452,
        "abs_return_acf_20": 0.21375343671133717,
        "quantile_01": -0.05835582143705384,
        "quantile_99": 0.04794056289075716,
        "hill_tail_index": 3.095539859160399
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019468978898723455,
        "excess_kurtosis": 7.019612121184252,
        "return_acf_1": -0.11816987387018742,
        "abs_return_acf_1": 0.3382151967279609,
        "abs_return_acf_5": 0.3676277719145477,
        "abs_return_acf_20": 0.24728202238881677,
        "quantile_01": -0.06077631968021492,
        "quantile_99": 0.04826976161796489,
        "hill_tail_index": 3.1103501524542807
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01856017508228677,
        "excess_kurtosis": 4.875974253984419,
        "return_acf_1": -0.06159703858970725,
        "abs_return_acf_1": 0.3249579022093298,
        "abs_return_acf_5": 0.3237333050467236,
        "abs_return_acf_20": 0.24420958126730885,
        "quantile_01": -0.054750757481731444,
        "quantile_99": 0.05430005674237939,
        "hill_tail_index": 3.7567430187320032
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021267484446878253,
        "excess_kurtosis": 11.18151714803383,
        "return_acf_1": -0.22288012482852532,
        "abs_return_acf_1": 0.3776567681953022,
        "abs_return_acf_5": 0.49843946556664026,
        "abs_return_acf_20": 0.314195179113165,
        "quantile_01": -0.06854123908496594,
        "quantile_99": 0.0606954668995423,
        "hill_tail_index": 3.111382277788348
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02038796407125308,
        "excess_kurtosis": 8.974597707411874,
        "return_acf_1": -0.05509555548115907,
        "abs_return_acf_1": 0.3969863224426294,
        "abs_return_acf_5": 0.3950986949574637,
        "abs_return_acf_20": 0.34292966930862306,
        "quantile_01": -0.0618711042284695,
        "quantile_99": 0.053491779034348194,
        "hill_tail_index": 2.7927586959071693
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0185560462255318,
        "excess_kurtosis": 6.2673238684606645,
        "return_acf_1": -0.12857589816220175,
        "abs_return_acf_1": 0.23640261316923816,
        "abs_return_acf_5": 0.3425222698655545,
        "abs_return_acf_20": 0.20440598489320394,
        "quantile_01": -0.060159734092341904,
        "quantile_99": 0.05093002648551005,
        "hill_tail_index": 3.218223151006736
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0183735205314453,
        "excess_kurtosis": 5.332151717866401,
        "return_acf_1": -0.12294152761954467,
        "abs_return_acf_1": 0.2691223399533973,
        "abs_return_acf_5": 0.3131091387700328,
        "abs_return_acf_20": 0.23592661140679708,
        "quantile_01": -0.0573225584971113,
        "quantile_99": 0.048918477431019645,
        "hill_tail_index": 2.3685501621077445
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018908847770597374,
        "excess_kurtosis": 4.57800956499145,
        "return_acf_1": -0.10195161876864654,
        "abs_return_acf_1": 0.33865566341364484,
        "abs_return_acf_5": 0.3672791193130514,
        "abs_return_acf_20": 0.2396213660705776,
        "quantile_01": -0.05797354735800028,
        "quantile_99": 0.045414100166140794,
        "hill_tail_index": 3.447080382999129
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01862701242571389,
        "excess_kurtosis": 5.187787364910363,
        "return_acf_1": -0.13242338717083263,
        "abs_return_acf_1": 0.26107115089628324,
        "abs_return_acf_5": 0.23932139932734436,
        "abs_return_acf_20": 0.20112443255960838,
        "quantile_01": -0.050559564226638765,
        "quantile_99": 0.047506973156946374,
        "hill_tail_index": 3.4264925175323775
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02024864956543805,
        "excess_kurtosis": 7.775577543038938,
        "return_acf_1": -0.12042229129302792,
        "abs_return_acf_1": 0.32740948567613376,
        "abs_return_acf_5": 0.37244246390831576,
        "abs_return_acf_20": 0.28081032778646864,
        "quantile_01": -0.0677022670371333,
        "quantile_99": 0.055893795183991166,
        "hill_tail_index": 2.9224679762601227
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018284399318452396,
        "excess_kurtosis": 4.643784040903846,
        "return_acf_1": -0.07086665691413352,
        "abs_return_acf_1": 0.2805246244910628,
        "abs_return_acf_5": 0.3367839489381151,
        "abs_return_acf_20": 0.2196487453762171,
        "quantile_01": -0.05330162921444231,
        "quantile_99": 0.04420418954055755,
        "hill_tail_index": 3.1603988340502247
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0182168386453561,
        "excess_kurtosis": 6.325891029372315,
        "return_acf_1": -0.1357936103157952,
        "abs_return_acf_1": 0.2855755381657188,
        "abs_return_acf_5": 0.31168249990751873,
        "abs_return_acf_20": 0.22193500807085842,
        "quantile_01": -0.05809156915432343,
        "quantile_99": 0.0468428057892317,
        "hill_tail_index": 2.945648254029509
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020124663899461638,
        "excess_kurtosis": 13.396516944780426,
        "return_acf_1": -0.1386428264526261,
        "abs_return_acf_1": 0.4083960164953767,
        "abs_return_acf_5": 0.2659027969950778,
        "abs_return_acf_20": 0.22777383463408532,
        "quantile_01": -0.06038040020384658,
        "quantile_99": 0.06122785104879446,
        "hill_tail_index": 2.918145305546158
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017736070477121637,
        "excess_kurtosis": 10.297350311064097,
        "return_acf_1": -0.07970328759578026,
        "abs_return_acf_1": 0.2863315776425057,
        "abs_return_acf_5": 0.3203595425070195,
        "abs_return_acf_20": 0.2076886779060832,
        "quantile_01": -0.05470314592080753,
        "quantile_99": 0.04193211321894929,
        "hill_tail_index": 2.305931178376346
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01918719755756143,
        "excess_kurtosis": 7.450272652332835,
        "return_acf_1": -0.12531857821787692,
        "abs_return_acf_1": 0.2826326344938642,
        "abs_return_acf_5": 0.4119739723926365,
        "abs_return_acf_20": 0.21188111498376413,
        "quantile_01": -0.056493267207974415,
        "quantile_99": 0.05297199343523847,
        "hill_tail_index": 3.1673289392088084
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018406221076725404,
        "excess_kurtosis": 8.79911591053995,
        "return_acf_1": -0.04704778601095049,
        "abs_return_acf_1": 0.35915100657767207,
        "abs_return_acf_5": 0.3550760608191318,
        "abs_return_acf_20": 0.29540138706097885,
        "quantile_01": -0.056047259725058064,
        "quantile_99": 0.04721820166399815,
        "hill_tail_index": 2.8232574111312707
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019630280961858947,
        "excess_kurtosis": 7.2642043855606,
        "return_acf_1": -0.1315138468170696,
        "abs_return_acf_1": 0.3262040887261416,
        "abs_return_acf_5": 0.4027730803592824,
        "abs_return_acf_20": 0.3259350390217571,
        "quantile_01": -0.05907904403922755,
        "quantile_99": 0.05384595915256729,
        "hill_tail_index": 3.423755918027904
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017660571729144692,
        "excess_kurtosis": 4.711707286643344,
        "return_acf_1": -0.10539016496872734,
        "abs_return_acf_1": 0.34237125861388246,
        "abs_return_acf_5": 0.31277586908224475,
        "abs_return_acf_20": 0.30135284042162896,
        "quantile_01": -0.05718786963408092,
        "quantile_99": 0.050822883241852336,
        "hill_tail_index": 4.254171634777354
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018975201907984306,
        "excess_kurtosis": 5.251598075317686,
        "return_acf_1": -0.12192026477360622,
        "abs_return_acf_1": 0.31013126418315945,
        "abs_return_acf_5": 0.3207244178453861,
        "abs_return_acf_20": 0.23251590567314243,
        "quantile_01": -0.05540284282568687,
        "quantile_99": 0.058914313134821,
        "hill_tail_index": 2.8874503548656407
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019507237223745408,
        "excess_kurtosis": 8.61672782651329,
        "return_acf_1": -0.09021164148485782,
        "abs_return_acf_1": 0.36948325473712024,
        "abs_return_acf_5": 0.3844408411058528,
        "abs_return_acf_20": 0.2520489397563811,
        "quantile_01": -0.0590023734770239,
        "quantile_99": 0.05135073722842006,
        "hill_tail_index": 3.470603772223521
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01929864788133341,
        "excess_kurtosis": 6.006235343166882,
        "return_acf_1": -0.022693059533514102,
        "abs_return_acf_1": 0.27645215127870293,
        "abs_return_acf_5": 0.22527404006611879,
        "abs_return_acf_20": 0.261729768159771,
        "quantile_01": -0.06609729894575178,
        "quantile_99": 0.05771222678130996,
        "hill_tail_index": 3.794763328799886
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018136493813099862,
        "excess_kurtosis": 8.354517227997526,
        "return_acf_1": -0.11963804099332428,
        "abs_return_acf_1": 0.21743459587280534,
        "abs_return_acf_5": 0.2994743734567773,
        "abs_return_acf_20": 0.21495364352458063,
        "quantile_01": -0.05987177203250321,
        "quantile_99": 0.04299530344121519,
        "hill_tail_index": 3.292882885749088
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01887490334929944,
        "excess_kurtosis": 7.020705528726539,
        "return_acf_1": -0.11582602824297081,
        "abs_return_acf_1": 0.32240048073866356,
        "abs_return_acf_5": 0.31602702915616115,
        "abs_return_acf_20": 0.2193113523436715,
        "quantile_01": -0.061151692036270425,
        "quantile_99": 0.05707625597433097,
        "hill_tail_index": 3.7913954259809426
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01982624242580152,
        "excess_kurtosis": 6.104848887277077,
        "return_acf_1": -0.14130027545454388,
        "abs_return_acf_1": 0.3281027907807095,
        "abs_return_acf_5": 0.34866798272191546,
        "abs_return_acf_20": 0.2615540883097185,
        "quantile_01": -0.05286381469111716,
        "quantile_99": 0.057085082209992234,
        "hill_tail_index": 2.8938781408328778
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02073138019873219,
        "excess_kurtosis": 12.42728649991077,
        "return_acf_1": -0.08784990196428234,
        "abs_return_acf_1": 0.365618903773198,
        "abs_return_acf_5": 0.4196328826460416,
        "abs_return_acf_20": 0.291550812295587,
        "quantile_01": -0.069306452255802,
        "quantile_99": 0.05313450063545263,
        "hill_tail_index": 2.4134465514056567
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01803426438645266,
        "excess_kurtosis": 4.2140761870708605,
        "return_acf_1": -0.14416899593366939,
        "abs_return_acf_1": 0.2932622003954469,
        "abs_return_acf_5": 0.2772731702246186,
        "abs_return_acf_20": 0.20731742527342178,
        "quantile_01": -0.05366467196573173,
        "quantile_99": 0.04945938102520562,
        "hill_tail_index": 3.1362814345044527
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018125656548115054,
        "excess_kurtosis": 4.416451535314045,
        "return_acf_1": -0.1216255558004093,
        "abs_return_acf_1": 0.3082179342326862,
        "abs_return_acf_5": 0.2934336916819891,
        "abs_return_acf_20": 0.22312222509310758,
        "quantile_01": -0.052581803875536945,
        "quantile_99": 0.053651091824644385,
        "hill_tail_index": 3.7933943836163517
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
