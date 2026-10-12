# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27236
Run ID: `2386f59e725c4890949a2af13e860be096907f2a1f2b858926c891631af160b9`
Result fingerprint: `6c00036781116cd8d3bbf040a622a04e785604c78c022591c3f6ca1737d39d2b`

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
    "equal_weight_sd": -0.8420829802094113,
    "equal_weight_raw": -12.631244703141167,
    "fixed_start_cap_weight_sd": -0.8628417106990215,
    "fixed_start_cap_weight_raw": -12.942625660485326,
    "end_cap_weight_sd": -0.8791994289165206,
    "end_cap_weight_raw": -13.187991433747808
  },
  "full_period_change": {
    "equal_weight_sd": -1.288356789733219,
    "equal_weight_raw": -19.325351845998288
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2069845454651418,
    "inflation_mean_sd": 0.3873955026455027
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1000833333333364,
    "equal_weight_raw": 1.501250000000046,
    "fixed_start_cap_weight_sd": 0.08639862550760793,
    "fixed_start_cap_weight_raw": 1.29597938261412,
    "end_cap_weight_sd": 0.07065546940015385,
    "end_cap_weight_raw": 1.0598320410023079
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8640476190476161,
      "change_raw": -12.960714285714241,
      "decay_adjusted_gain_sd": 0.08833333333333619
    },
    "mid": {
      "count": 9,
      "change_sd": -0.9027766006980449,
      "change_raw": -13.541649010470673,
      "decay_adjusted_gain_sd": 0.015555555555558312
    },
    "small": {
      "count": 18,
      "change_sd": -0.8080753968253936,
      "change_raw": -12.121130952380904,
      "decay_adjusted_gain_sd": 0.14430555555555877
    },
    "large_minus_small_sd": -0.05597222222222242,
    "large_minus_small_raw": -0.8395833333333363
  },
  "inflation": {
    "initial_mean_sd": 0.24425,
    "final_mean_sd": 0.39683333333333337,
    "mean_sd": 0.3474744657230086,
    "mean_absolute_raw_gap": 5.212116985845129,
    "final_absolute_raw_gap": 5.9525,
    "mean_range_fraction": 0.05212116985845129
  },
  "impact": {
    "initial_share": 0.32666666666666666,
    "final_share": 0.3933333333333333,
    "initial_wealth_share": 0.31406960024952696,
    "final_wealth_share": 0.35564564820923583
  },
  "pricing_slope": {
    "mean": 0.00020226265806093792,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.015124093870789508,
    "real_improvement_cost": 0.009488293240181831,
    "washing_cost": 0.005635800630607677,
    "fine_transfer": 0.036612875411088965,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05173696928187847,
    "resource_cost_fraction_initial_cap": 0.0005041364623596503,
    "private_net_outflow_fraction_initial_cap": 0.0017245656427292825,
    "fine_transfer_fraction_initial_cap": 0.001220429180369632,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 9.087796362695276e-05,
    "unapplied_final_day_resource_cost": 0.00017109187618073198
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 198.5242901592329,
    "beneficial_raw_gain_per_resource_cost": 2977.8643523884934,
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
    "accrued_cost": 2.920919353433853,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.05527112275662411,
    "accrued_cost_fraction_initial_cap": 0.0973639784477951,
    "mean_contract_rate": 0.04138817024014385,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 2.3178667400566735e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.22295372447362194,
      "maximum": -0.012336751853478115,
      "mean": -0.14031799327298303,
      "median": -0.1410911521375105,
      "quantile_05": -0.20652039567493094,
      "quantile_95": -0.0544381662522241
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
      "minimum": 0.22510307964627482,
      "maximum": 0.7678974907108418,
      "mean": 0.46943308021546937,
      "median": 0.4332883588283547,
      "quantile_05": 0.288139450092993,
      "quantile_95": 0.6973523352940326
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
        "daily_volatility": 0.024070781799195726,
        "excess_kurtosis": 12.628649532872698,
        "return_acf_1": -0.13803890423433748,
        "abs_return_acf_1": 0.36568537587722927,
        "abs_return_acf_5": 0.33203916439438397,
        "abs_return_acf_20": 0.3277022024718184,
        "quantile_01": -0.0795780375510644,
        "quantile_99": 0.06807968114355864,
        "hill_tail_index": 3.0950869071174627
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017565853120485028,
        "excess_kurtosis": 6.445641688132582,
        "return_acf_1": -0.1597810070458467,
        "abs_return_acf_1": 0.33957419880549017,
        "abs_return_acf_5": 0.20991468372232172,
        "abs_return_acf_20": 0.2628893889051945,
        "quantile_01": -0.0477687965333425,
        "quantile_99": 0.052159519750272686,
        "hill_tail_index": 2.9397799245932528
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016472103177621135,
        "excess_kurtosis": 9.56829392247202,
        "return_acf_1": -0.11983687314784999,
        "abs_return_acf_1": 0.33626379932562717,
        "abs_return_acf_5": 0.31921901142748266,
        "abs_return_acf_20": 0.2584501815933333,
        "quantile_01": -0.048895517477682955,
        "quantile_99": 0.05103485296597908,
        "hill_tail_index": 2.3663093142768656
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022051887103810147,
        "excess_kurtosis": 15.583022161125822,
        "return_acf_1": -0.11743944126238995,
        "abs_return_acf_1": 0.32344809234332894,
        "abs_return_acf_5": 0.23405011433327166,
        "abs_return_acf_20": 0.2975051491827597,
        "quantile_01": -0.07175346033808952,
        "quantile_99": 0.06011861217040693,
        "hill_tail_index": 2.2258425862420768
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01892340995753202,
        "excess_kurtosis": 10.009858242765626,
        "return_acf_1": -0.09309315681652967,
        "abs_return_acf_1": 0.3223670889863175,
        "abs_return_acf_5": 0.32221881338534514,
        "abs_return_acf_20": 0.2820106708563692,
        "quantile_01": -0.06636720084623765,
        "quantile_99": 0.05445152373589941,
        "hill_tail_index": 3.0733642737462463
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016381557932357942,
        "excess_kurtosis": 5.730638225506965,
        "return_acf_1": -0.08497999034054877,
        "abs_return_acf_1": 0.2667721577849069,
        "abs_return_acf_5": 0.20035434298785304,
        "abs_return_acf_20": 0.21175566578692223,
        "quantile_01": -0.046763287311112116,
        "quantile_99": 0.04201516814740754,
        "hill_tail_index": 3.520719652219926
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018840942752512246,
        "excess_kurtosis": 7.855780694180121,
        "return_acf_1": -0.15535526404944164,
        "abs_return_acf_1": 0.3829137043126111,
        "abs_return_acf_5": 0.35016200660441377,
        "abs_return_acf_20": 0.3086291980934589,
        "quantile_01": -0.0600975844069505,
        "quantile_99": 0.050736062442675076,
        "hill_tail_index": 2.7634876170807647
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015848934619368007,
        "excess_kurtosis": 6.594104605977789,
        "return_acf_1": -0.11692136528566921,
        "abs_return_acf_1": 0.2886575375219517,
        "abs_return_acf_5": 0.3033455196131922,
        "abs_return_acf_20": 0.26797252294722546,
        "quantile_01": -0.04366593379845138,
        "quantile_99": 0.04365476694948747,
        "hill_tail_index": 3.1616377421883115
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018453227954911874,
        "excess_kurtosis": 7.342069863352284,
        "return_acf_1": -0.1598637642112484,
        "abs_return_acf_1": 0.3159305918989782,
        "abs_return_acf_5": 0.24520721445512283,
        "abs_return_acf_20": 0.26644767809816483,
        "quantile_01": -0.054643009385203146,
        "quantile_99": 0.04793213265778233,
        "hill_tail_index": 2.6840432364036526
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016521128796470195,
        "excess_kurtosis": 10.203704436653505,
        "return_acf_1": -0.22295372447362194,
        "abs_return_acf_1": 0.3909137836621762,
        "abs_return_acf_5": 0.27585776998769196,
        "abs_return_acf_20": 0.23892519010185484,
        "quantile_01": -0.049545763713261026,
        "quantile_99": 0.039921607414833325,
        "hill_tail_index": 2.3258427790910865
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020444976428384175,
        "excess_kurtosis": 13.474801448505108,
        "return_acf_1": -0.012336751853478115,
        "abs_return_acf_1": 0.36842805510009163,
        "abs_return_acf_5": 0.4437319387931316,
        "abs_return_acf_20": 0.25280559365027366,
        "quantile_01": -0.06583698879583075,
        "quantile_99": 0.05928621366591843,
        "hill_tail_index": 2.432711873595377
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017485049090204798,
        "excess_kurtosis": 14.68899151551178,
        "return_acf_1": -0.11155600542887523,
        "abs_return_acf_1": 0.30429421242857374,
        "abs_return_acf_5": 0.3101020660049043,
        "abs_return_acf_20": 0.2023566724426453,
        "quantile_01": -0.05373098436435297,
        "quantile_99": 0.04970373448940052,
        "hill_tail_index": 2.6698018411370694
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01758888977349041,
        "excess_kurtosis": 11.318054590130439,
        "return_acf_1": -0.1983538751900451,
        "abs_return_acf_1": 0.34434778210546363,
        "abs_return_acf_5": 0.26483249235060974,
        "abs_return_acf_20": 0.21668415402800614,
        "quantile_01": -0.05255834076118916,
        "quantile_99": 0.05134684212964562,
        "hill_tail_index": 2.925822135117954
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01703919125577201,
        "excess_kurtosis": 8.8655694962632,
        "return_acf_1": -0.09919123544245023,
        "abs_return_acf_1": 0.265791083461345,
        "abs_return_acf_5": 0.2673158300740992,
        "abs_return_acf_20": 0.3086574602617682,
        "quantile_01": -0.04494136770038361,
        "quantile_99": 0.036497204775423696,
        "hill_tail_index": 2.3167968950040048
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015656755711507903,
        "excess_kurtosis": 4.814423305212038,
        "return_acf_1": -0.17036076585621374,
        "abs_return_acf_1": 0.2627587221837943,
        "abs_return_acf_5": 0.1601199623703925,
        "abs_return_acf_20": 0.17855311992693265,
        "quantile_01": -0.04077840719116095,
        "quantile_99": 0.03865067877925347,
        "hill_tail_index": 3.247091694267012
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01916680304691065,
        "excess_kurtosis": 7.542757056553613,
        "return_acf_1": -0.2132020942534739,
        "abs_return_acf_1": 0.40622620451131297,
        "abs_return_acf_5": 0.34354122515000407,
        "abs_return_acf_20": 0.286147779161172,
        "quantile_01": -0.06784274931628226,
        "quantile_99": 0.0575974860357574,
        "hill_tail_index": 2.789847733944122
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01806037154060478,
        "excess_kurtosis": 12.623082151614845,
        "return_acf_1": -0.1905431062504164,
        "abs_return_acf_1": 0.39569390625555734,
        "abs_return_acf_5": 0.2705552877028986,
        "abs_return_acf_20": 0.2923560952563064,
        "quantile_01": -0.050458568342621496,
        "quantile_99": 0.05035317277602221,
        "hill_tail_index": 2.476894942908708
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018164232066405626,
        "excess_kurtosis": 4.949948856101264,
        "return_acf_1": -0.1321885408645439,
        "abs_return_acf_1": 0.29882557214132455,
        "abs_return_acf_5": 0.22918627524911592,
        "abs_return_acf_20": 0.25206665451619775,
        "quantile_01": -0.05731998681727882,
        "quantile_99": 0.04755046196433056,
        "hill_tail_index": 2.821359413713246
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020475763080013868,
        "excess_kurtosis": 8.438738128822374,
        "return_acf_1": -0.16836394238752664,
        "abs_return_acf_1": 0.35464296276241697,
        "abs_return_acf_5": 0.29192797194404907,
        "abs_return_acf_20": 0.28955267573993726,
        "quantile_01": -0.06659055545065434,
        "quantile_99": 0.061014825156354154,
        "hill_tail_index": 2.833485274970781
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01603325360750638,
        "excess_kurtosis": 15.806561166564528,
        "return_acf_1": -0.05075095878150149,
        "abs_return_acf_1": 0.2777743484163392,
        "abs_return_acf_5": 0.29847189515673717,
        "abs_return_acf_20": 0.21574668907063946,
        "quantile_01": -0.04074834040883378,
        "quantile_99": 0.0413693399052875,
        "hill_tail_index": 2.9406907757315164
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01711293171841001,
        "excess_kurtosis": 4.491422444132586,
        "return_acf_1": -0.19584946711008905,
        "abs_return_acf_1": 0.2728310844725715,
        "abs_return_acf_5": 0.19500385045213856,
        "abs_return_acf_20": 0.2461870811175616,
        "quantile_01": -0.04721525549864842,
        "quantile_99": 0.04495538903350249,
        "hill_tail_index": 3.1459793680711616
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01659426037845239,
        "excess_kurtosis": 5.450919349129753,
        "return_acf_1": -0.1909839680329728,
        "abs_return_acf_1": 0.3078858382561478,
        "abs_return_acf_5": 0.15551407167052378,
        "abs_return_acf_20": 0.1656610551472929,
        "quantile_01": -0.04902657422598159,
        "quantile_99": 0.04324124815460934,
        "hill_tail_index": 3.5157351977536724
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017530973902008026,
        "excess_kurtosis": 9.041749375277917,
        "return_acf_1": -0.058944753160885016,
        "abs_return_acf_1": 0.2469720051404867,
        "abs_return_acf_5": 0.26404812398416005,
        "abs_return_acf_20": 0.3210570895071356,
        "quantile_01": -0.0431914999867687,
        "quantile_99": 0.046225472386709904,
        "hill_tail_index": 3.0007119355713043
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021071440231881837,
        "excess_kurtosis": 6.5349291981829385,
        "return_acf_1": -0.13476216145356767,
        "abs_return_acf_1": 0.3237720155306553,
        "abs_return_acf_5": 0.31324288046142007,
        "abs_return_acf_20": 0.34868707589191367,
        "quantile_01": -0.06847897924284142,
        "quantile_99": 0.05342892479983803,
        "hill_tail_index": 3.3602190129064264
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015767671145884652,
        "excess_kurtosis": 4.337364745308508,
        "return_acf_1": -0.1965897065765517,
        "abs_return_acf_1": 0.2863564246505483,
        "abs_return_acf_5": 0.24649325186912385,
        "abs_return_acf_20": 0.23844547849672185,
        "quantile_01": -0.0528494700925986,
        "quantile_99": 0.03874428181441389,
        "hill_tail_index": 2.6438360504879537
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01667470534350324,
        "excess_kurtosis": 5.58309212167967,
        "return_acf_1": -0.16795248167791324,
        "abs_return_acf_1": 0.36101168830739383,
        "abs_return_acf_5": 0.25881277499216154,
        "abs_return_acf_20": 0.26104550427011436,
        "quantile_01": -0.04609621167214042,
        "quantile_99": 0.04323899739905688,
        "hill_tail_index": 3.0824023431824616
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021888005615456303,
        "excess_kurtosis": 14.216297262052226,
        "return_acf_1": -0.16364709464658828,
        "abs_return_acf_1": 0.3375282649812589,
        "abs_return_acf_5": 0.29194217478955325,
        "abs_return_acf_20": 0.3157950183616733,
        "quantile_01": -0.07220915486062542,
        "quantile_99": 0.06814673973313849,
        "hill_tail_index": 2.8229963759372887
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017350273285989974,
        "excess_kurtosis": 2.501130736889568,
        "return_acf_1": -0.13017380881954574,
        "abs_return_acf_1": 0.25977611319020805,
        "abs_return_acf_5": 0.17606541385373128,
        "abs_return_acf_20": 0.18329290636120688,
        "quantile_01": -0.0458338740492225,
        "quantile_99": 0.043170891649263514,
        "hill_tail_index": 4.60759845038164
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02220269414744748,
        "excess_kurtosis": 11.674405242376112,
        "return_acf_1": -0.11138218949468519,
        "abs_return_acf_1": 0.42250045529739094,
        "abs_return_acf_5": 0.34721191380962846,
        "abs_return_acf_20": 0.35756560117882963,
        "quantile_01": -0.07611969642592045,
        "quantile_99": 0.06718628565231519,
        "hill_tail_index": 3.3677714098933818
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01739850296209351,
        "excess_kurtosis": 10.540095776775592,
        "return_acf_1": -0.14414340004068352,
        "abs_return_acf_1": 0.4568159449381526,
        "abs_return_acf_5": 0.35751820647191984,
        "abs_return_acf_20": 0.2938989642102212,
        "quantile_01": -0.05351362350908533,
        "quantile_99": 0.045370523241728467,
        "hill_tail_index": 2.235947819774923
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
