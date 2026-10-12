# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720211
Run ID: `be6231651dc2a75c34227f1900b5d5c5d35aa26b48d72e07f4867a0c75a59d17`
Result fingerprint: `72ba3e1cc3fd19ba7bc9ae2ad6b8c61f1401e0ec3626917107a0fbb0cbdf509f`

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
    "equal_weight_sd": -0.8944682539682509,
    "equal_weight_raw": -13.417023809523764,
    "fixed_start_cap_weight_sd": -0.8924956508607411,
    "fixed_start_cap_weight_raw": -13.387434762911116,
    "end_cap_weight_sd": -0.8904160958969539,
    "end_cap_weight_raw": -13.356241438454303
  },
  "full_period_change": {
    "equal_weight_sd": -1.3473948276724736,
    "equal_weight_raw": -20.210922415087104
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.254207327672474,
    "inflation_mean_sd": 0.2673849206349207
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.02650000000000298,
    "equal_weight_raw": 0.3975000000000447,
    "fixed_start_cap_weight_sd": 0.03056948757665156,
    "fixed_start_cap_weight_raw": 0.45854231364977344,
    "end_cap_weight_sd": 0.030255753434951755,
    "end_cap_weight_raw": 0.45383630152427623
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.9348809523809493,
      "change_raw": -14.02321428571424,
      "decay_adjusted_gain_sd": 0.017500000000002996
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8079497354497327,
      "change_raw": -12.119246031745991,
      "decay_adjusted_gain_sd": 0.03972222222222494
    },
    "small": {
      "count": 18,
      "change_sd": -0.9309920634920602,
      "change_raw": -13.964880952380904,
      "decay_adjusted_gain_sd": 0.021388888888891996
    },
    "large_minus_small_sd": -0.0038888888888890527,
    "large_minus_small_raw": -0.05833333333333579
  },
  "inflation": {
    "initial_mean_sd": 0.1495833333333333,
    "final_mean_sd": 0.27291666666666664,
    "mean_sd": 0.22088225090202612,
    "mean_absolute_raw_gap": 3.313233763530392,
    "final_absolute_raw_gap": 4.093750000000001,
    "mean_range_fraction": 0.03313233763530392
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.3933333333333333,
    "initial_wealth_share": 0.15452125733035374,
    "final_wealth_share": 0.3259207357843358
  },
  "pricing_slope": {
    "mean": -0.001681583212100273,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.0009441584779277283,
    "real_improvement_cost": 0.00022099968681959348,
    "washing_cost": 0.000723158791108135,
    "fine_transfer": 0.0047042163012246865,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.005648374779152415,
    "resource_cost_fraction_initial_cap": 3.14719492642576e-05,
    "private_net_outflow_fraction_initial_cap": 0.00018827915930508046,
    "fine_transfer_fraction_initial_cap": 0.00015680721004082286,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 7.555522702814039e-05,
    "unapplied_final_day_resource_cost": 1.8205957633677996e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 842.0196593955105,
    "beneficial_raw_gain_per_resource_cost": 12630.294890932659,
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
    "accrued_cost": 3.01714286458696,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.040952388396482874,
    "accrued_cost_fraction_initial_cap": 0.10057142881956532,
    "mean_contract_rate": 0.04218315400537139,
    "maximum_ledger_error": 8.809142651444724e-20
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
    "maximum_relative_cash_error": 6.2522928326272e-15,
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
      "minimum": -0.2236213328205565,
      "maximum": -0.07951459749371148,
      "mean": -0.13842545841232423,
      "median": -0.13502905836668105,
      "quantile_05": -0.1967424715168336,
      "quantile_95": -0.0827899359159674
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
      "minimum": 0.12579945952009408,
      "maximum": 0.8438781319014913,
      "mean": 0.5590151320402303,
      "median": 0.5901931055476292,
      "quantile_05": 0.296506882023065,
      "quantile_95": 0.7390624728129849
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
        "daily_volatility": 0.019375431309918457,
        "excess_kurtosis": 7.812545168103689,
        "return_acf_1": -0.10241605771134411,
        "abs_return_acf_1": 0.2787131339996524,
        "abs_return_acf_5": 0.3821728445062634,
        "abs_return_acf_20": 0.2842453753854455,
        "quantile_01": -0.06379888830380222,
        "quantile_99": 0.05569525483530715,
        "hill_tail_index": 3.1596685667848003
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02498728768310007,
        "excess_kurtosis": 13.017432916916782,
        "return_acf_1": -0.18752465748970057,
        "abs_return_acf_1": 0.4982674926148774,
        "abs_return_acf_5": 0.42255436741412894,
        "abs_return_acf_20": 0.37435450299338535,
        "quantile_01": -0.089173707206853,
        "quantile_99": 0.07436364494764253,
        "hill_tail_index": 3.490870027030941
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01967528825729791,
        "excess_kurtosis": 8.684804311725529,
        "return_acf_1": -0.14149353076963841,
        "abs_return_acf_1": 0.33809511228583083,
        "abs_return_acf_5": 0.3896734730396012,
        "abs_return_acf_20": 0.3561843020946792,
        "quantile_01": -0.05900765974905658,
        "quantile_99": 0.055275173952625156,
        "hill_tail_index": 3.228249648937024
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.026029452030763227,
        "excess_kurtosis": 17.888167740670337,
        "return_acf_1": -0.09355046244653815,
        "abs_return_acf_1": 0.5247898096683562,
        "abs_return_acf_5": 0.4954698448393781,
        "abs_return_acf_20": 0.4336934046707177,
        "quantile_01": -0.08566623508207993,
        "quantile_99": 0.09140540223454478,
        "hill_tail_index": 2.6693338929496986
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022667099393764933,
        "excess_kurtosis": 41.98868026015584,
        "return_acf_1": -0.19160118482313984,
        "abs_return_acf_1": 0.2814714883704758,
        "abs_return_acf_5": 0.17991816066812763,
        "abs_return_acf_20": 0.19357536773406941,
        "quantile_01": -0.05942484158955591,
        "quantile_99": 0.05944847091423116,
        "hill_tail_index": 3.5111700182104526
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02333337518682886,
        "excess_kurtosis": 15.522992995133762,
        "return_acf_1": -0.09422441798808576,
        "abs_return_acf_1": 0.3765703765912423,
        "abs_return_acf_5": 0.3433676109173743,
        "abs_return_acf_20": 0.3153569057015317,
        "quantile_01": -0.07909526290107456,
        "quantile_99": 0.06409582413667546,
        "hill_tail_index": 2.749088902656252
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02410264018365794,
        "excess_kurtosis": 13.866742641480798,
        "return_acf_1": -0.11325296229176499,
        "abs_return_acf_1": 0.4557587652246086,
        "abs_return_acf_5": 0.38561809882506365,
        "abs_return_acf_20": 0.29698588676820653,
        "quantile_01": -0.08274042395001538,
        "quantile_99": 0.07735807233737896,
        "hill_tail_index": 3.7458374816822784
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02136015315319639,
        "excess_kurtosis": 9.694177098663307,
        "return_acf_1": -0.2236213328205565,
        "abs_return_acf_1": 0.34989605949812264,
        "abs_return_acf_5": 0.37610371740445364,
        "abs_return_acf_20": 0.3195116444316969,
        "quantile_01": -0.07301977602944884,
        "quantile_99": 0.06777802421203658,
        "hill_tail_index": 2.8801221488685247
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01896614174436811,
        "excess_kurtosis": 11.611135535960178,
        "return_acf_1": -0.18375518091787843,
        "abs_return_acf_1": 0.3385231032611678,
        "abs_return_acf_5": 0.23460356303031604,
        "abs_return_acf_20": 0.29103108314623194,
        "quantile_01": -0.06498929183123789,
        "quantile_99": 0.052659275442896857,
        "hill_tail_index": 3.5902946738138075
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021053297789567275,
        "excess_kurtosis": 13.447494042757636,
        "return_acf_1": -0.08413071052937142,
        "abs_return_acf_1": 0.3217736761506445,
        "abs_return_acf_5": 0.3750825659881689,
        "abs_return_acf_20": 0.33350660840632174,
        "quantile_01": -0.06990880262750353,
        "quantile_99": 0.06261856862929552,
        "hill_tail_index": 2.8673644259466955
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020972872105717195,
        "excess_kurtosis": 14.156287309754656,
        "return_acf_1": -0.10229493488972477,
        "abs_return_acf_1": 0.37724198415121274,
        "abs_return_acf_5": 0.39514799987047305,
        "abs_return_acf_20": 0.2917406547905516,
        "quantile_01": -0.06808936766315783,
        "quantile_99": 0.062467170805683675,
        "hill_tail_index": 3.1275709069792965
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018443069911521406,
        "excess_kurtosis": 4.3948037209328445,
        "return_acf_1": -0.11613948040016486,
        "abs_return_acf_1": 0.3314124356349108,
        "abs_return_acf_5": 0.3257455976752753,
        "abs_return_acf_20": 0.2548870796717345,
        "quantile_01": -0.055224302345002335,
        "quantile_99": 0.04979253783689158,
        "hill_tail_index": 3.3290890924790038
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017660402215990464,
        "excess_kurtosis": 4.793954545981677,
        "return_acf_1": -0.08169293850500046,
        "abs_return_acf_1": 0.21911442910919085,
        "abs_return_acf_5": 0.27148589743958357,
        "abs_return_acf_20": 0.2791059688952594,
        "quantile_01": -0.05255533406751371,
        "quantile_99": 0.05029430094348082,
        "hill_tail_index": 4.596168758870796
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.024871699364087823,
        "excess_kurtosis": 15.692116542369618,
        "return_acf_1": -0.1216346854757039,
        "abs_return_acf_1": 0.4773162507052776,
        "abs_return_acf_5": 0.44060058120633994,
        "abs_return_acf_20": 0.38426874269099387,
        "quantile_01": -0.08346342038831883,
        "quantile_99": 0.08218818336471967,
        "hill_tail_index": 2.491152915417421
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024123613763610895,
        "excess_kurtosis": 15.37389904032446,
        "return_acf_1": -0.1592715903846567,
        "abs_return_acf_1": 0.4879345420853561,
        "abs_return_acf_5": 0.44761883776240113,
        "abs_return_acf_20": 0.3089184696523258,
        "quantile_01": -0.0859237548922697,
        "quantile_99": 0.07812205717638646,
        "hill_tail_index": 3.9223574651005424
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02126546644367554,
        "excess_kurtosis": 11.230023130462765,
        "return_acf_1": -0.18647640780856528,
        "abs_return_acf_1": 0.39134465252931666,
        "abs_return_acf_5": 0.35240690518457546,
        "abs_return_acf_20": 0.28014456780816455,
        "quantile_01": -0.0749845523388207,
        "quantile_99": 0.06753885104591764,
        "hill_tail_index": 3.4864427798882547
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019900668699430704,
        "excess_kurtosis": 7.210743041647122,
        "return_acf_1": -0.13849807401452224,
        "abs_return_acf_1": 0.3697963388320924,
        "abs_return_acf_5": 0.36704979877421934,
        "abs_return_acf_20": 0.2701069102692107,
        "quantile_01": -0.0655465666361471,
        "quantile_99": 0.05649411895845588,
        "hill_tail_index": 3.322396458255571
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01995192190115007,
        "excess_kurtosis": 5.362626354013461,
        "return_acf_1": -0.17812659490789046,
        "abs_return_acf_1": 0.3053192524922642,
        "abs_return_acf_5": 0.3463525365105295,
        "abs_return_acf_20": 0.2075457600818711,
        "quantile_01": -0.061012355909652455,
        "quantile_99": 0.06057014936437259,
        "hill_tail_index": 3.8711835028176753
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018052129505403094,
        "excess_kurtosis": 4.4459902323409715,
        "return_acf_1": -0.12665478239134934,
        "abs_return_acf_1": 0.3107523644125633,
        "abs_return_acf_5": 0.28018896583663155,
        "abs_return_acf_20": 0.26500396313169533,
        "quantile_01": -0.05588705550194238,
        "quantile_99": 0.04930200348118496,
        "hill_tail_index": 4.053023928926121
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019156271230165205,
        "excess_kurtosis": 10.317899540150941,
        "return_acf_1": -0.1918732115421277,
        "abs_return_acf_1": 0.3664030313850492,
        "abs_return_acf_5": 0.3880572043199881,
        "abs_return_acf_20": 0.325586456992099,
        "quantile_01": -0.056608877500961184,
        "quantile_99": 0.056317318036475446,
        "hill_tail_index": 2.77141997482822
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019947653606031776,
        "excess_kurtosis": 5.57458139129295,
        "return_acf_1": -0.10984878954099682,
        "abs_return_acf_1": 0.4009202799887223,
        "abs_return_acf_5": 0.35944784727913215,
        "abs_return_acf_20": 0.3306471384705298,
        "quantile_01": -0.06537789399434069,
        "quantile_99": 0.07156032329158457,
        "hill_tail_index": 3.6714947285982236
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019278978614640993,
        "excess_kurtosis": 5.607002613300283,
        "return_acf_1": -0.09235715052976569,
        "abs_return_acf_1": 0.33142431983183945,
        "abs_return_acf_5": 0.3143532809112459,
        "abs_return_acf_20": 0.2883415969398861,
        "quantile_01": -0.06695246103598278,
        "quantile_99": 0.04558231734472345,
        "hill_tail_index": 4.275945476782777
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020213072243560337,
        "excess_kurtosis": 8.855683172374238,
        "return_acf_1": -0.14224397804403746,
        "abs_return_acf_1": 0.2900665456909286,
        "abs_return_acf_5": 0.29472690490840436,
        "abs_return_acf_20": 0.2727920586284857,
        "quantile_01": -0.07057027722671723,
        "quantile_99": 0.05669514248777534,
        "hill_tail_index": 2.6754960225524047
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019544729965793727,
        "excess_kurtosis": 31.78858736369356,
        "return_acf_1": -0.17352078623636008,
        "abs_return_acf_1": 0.3017263667582431,
        "abs_return_acf_5": 0.1947695041860697,
        "abs_return_acf_20": 0.23525803842745927,
        "quantile_01": -0.050906955832105104,
        "quantile_99": 0.05293461388290005,
        "hill_tail_index": 2.951108626444698
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.024473361217939135,
        "excess_kurtosis": 14.793473216215315,
        "return_acf_1": -0.1663575447690378,
        "abs_return_acf_1": 0.3994694263140984,
        "abs_return_acf_5": 0.41011833529655267,
        "abs_return_acf_20": 0.4228908401845619,
        "quantile_01": -0.07138599525813734,
        "quantile_99": 0.06984192290962202,
        "hill_tail_index": 2.8669835502479852
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01936540166527768,
        "excess_kurtosis": 11.352670085039005,
        "return_acf_1": -0.07951459749371148,
        "abs_return_acf_1": 0.2939559679526042,
        "abs_return_acf_5": 0.2922737008578208,
        "abs_return_acf_20": 0.23628141747142747,
        "quantile_01": -0.06162007948344683,
        "quantile_99": 0.04768127533341988,
        "hill_tail_index": 2.79656446625846
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025224930179595824,
        "excess_kurtosis": 17.148611195232423,
        "return_acf_1": -0.20072641149613843,
        "abs_return_acf_1": 0.5163795279840476,
        "abs_return_acf_5": 0.3693595219824768,
        "abs_return_acf_20": 0.3338101598557508,
        "quantile_01": -0.09468898750915733,
        "quantile_99": 0.07159545650197649,
        "hill_tail_index": 3.205598533910444
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.023707417800540836,
        "excess_kurtosis": 11.724802251768105,
        "return_acf_1": -0.13170602802903594,
        "abs_return_acf_1": 0.492026447436401,
        "abs_return_acf_5": 0.4562613566385153,
        "abs_return_acf_20": 0.32592974258246077,
        "quantile_01": -0.08993054831398149,
        "quantile_99": 0.06224065321341579,
        "hill_tail_index": 2.673367092431158
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021107372202352453,
        "excess_kurtosis": 7.878455964970517,
        "return_acf_1": -0.09990317941859274,
        "abs_return_acf_1": 0.33825100443218287,
        "abs_return_acf_5": 0.3306818529289261,
        "abs_return_acf_20": 0.30366477945559084,
        "quantile_01": -0.07292104178363748,
        "quantile_99": 0.06561848573117508,
        "hill_tail_index": 3.493012027968173
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0195334042154055,
        "excess_kurtosis": 6.710402412152561,
        "return_acf_1": -0.13835208870432614,
        "abs_return_acf_1": 0.2906691210660954,
        "abs_return_acf_5": 0.31642194815138,
        "abs_return_acf_20": 0.23795152820119958,
        "quantile_01": -0.058816324852873,
        "quantile_99": 0.056789561633314216,
        "hill_tail_index": 3.5903220920386523
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
Unseen state share: 0.05555555555555555
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
