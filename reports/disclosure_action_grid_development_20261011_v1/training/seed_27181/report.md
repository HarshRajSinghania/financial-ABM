# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27181
Run ID: `1252d3f0776fa010232909f6a2d886fbbb9951ed45e10ed2653a6898ef0e2c41`
Result fingerprint: `3b30e9349753657ac4b224d87092b277ba9ac2f6860a159f6f8cd11ed791bb5d`

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
    "equal_weight_sd": -0.7647261904761874,
    "equal_weight_raw": -11.470892857142813,
    "fixed_start_cap_weight_sd": -0.7820223863073893,
    "fixed_start_cap_weight_raw": -11.730335794610841,
    "end_cap_weight_sd": -0.7982311380013015,
    "end_cap_weight_raw": -11.973467070019522
  },
  "full_period_change": {
    "equal_weight_sd": -1.1291004709100112,
    "equal_weight_raw": -16.93650706365017
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0486270991539017,
    "inflation_mean_sd": 0.5580684523809523
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1456362000490491,
    "equal_weight_raw": 2.184543000735736,
    "fixed_start_cap_weight_sd": 0.15258001811980884,
    "fixed_start_cap_weight_raw": 2.288700271797133,
    "end_cap_weight_sd": 0.1405193302169465,
    "end_cap_weight_raw": 2.1077899532541973
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8407142857142826,
      "change_raw": -12.61071428571424,
      "decay_adjusted_gain_sd": 0.11166666666666965
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6946031746031713,
      "change_raw": -10.41904761904757,
      "decay_adjusted_gain_sd": 0.22353601074550056
    },
    "small": {
      "count": 18,
      "change_sd": -0.7871230158730128,
      "change_raw": -11.806845238095192,
      "decay_adjusted_gain_sd": 0.11234788359788661
    },
    "large_minus_small_sd": -0.05359126984126983,
    "large_minus_small_raw": -0.8038690476190474
  },
  "inflation": {
    "initial_mean_sd": 0.2971666666666667,
    "final_mean_sd": 0.5831666666666667,
    "mean_sd": 0.4558491534832084,
    "mean_absolute_raw_gap": 6.837737302248126,
    "final_absolute_raw_gap": 8.7475,
    "mean_range_fraction": 0.06837737302248126
  },
  "impact": {
    "initial_share": 0.41333333333333333,
    "final_share": 0.46,
    "initial_wealth_share": 0.4548074105566245,
    "final_wealth_share": 0.5117204721524371
  },
  "pricing_slope": {
    "mean": -0.002414178912349391,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.01979022343067658,
    "real_improvement_cost": 0.013083969453026192,
    "washing_cost": 0.006706253977650385,
    "fine_transfer": 0.007456038831594356,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.027246262262270934,
    "resource_cost_fraction_initial_cap": 0.000659674114355886,
    "private_net_outflow_fraction_initial_cap": 0.000908208742075698,
    "fine_transfer_fraction_initial_cap": 0.0002485346277198119,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 6.013368709572988e-05,
    "unapplied_final_day_resource_cost": 0.00025193062884455036
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 220.76991787263032,
    "beneficial_raw_gain_per_resource_cost": 3311.548768089455,
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
    "accrued_cost": 3.1672162764398495,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.19102580024937382,
    "accrued_cost_fraction_initial_cap": 0.10557387588132833,
    "mean_contract_rate": 0.04422621368436463,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 1.0185389543680194e-15,
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
      "minimum": -0.2919727965049716,
      "maximum": -0.12079789566585537,
      "mean": -0.1987060226663015,
      "median": -0.20233497594383054,
      "quantile_05": -0.27101220986320956,
      "quantile_95": -0.15061820550523547
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
      "minimum": 0.4369939840394187,
      "maximum": 0.807054400104124,
      "mean": 0.6534425661883994,
      "median": 0.6602784703936121,
      "quantile_05": 0.5256881063152296,
      "quantile_95": 0.7535632297939023
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
        "daily_volatility": 0.018686653203970994,
        "excess_kurtosis": 7.6281909709783005,
        "return_acf_1": -0.20722434298180226,
        "abs_return_acf_1": 0.34315043706631504,
        "abs_return_acf_5": 0.37471148704441204,
        "abs_return_acf_20": 0.33118150709316274,
        "quantile_01": -0.06181572310518156,
        "quantile_99": 0.0530129221106663,
        "hill_tail_index": 2.766359275575052
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02000121707037063,
        "excess_kurtosis": 12.4399277930834,
        "return_acf_1": -0.2919727965049716,
        "abs_return_acf_1": 0.39618345314704145,
        "abs_return_acf_5": 0.4215011127969514,
        "abs_return_acf_20": 0.35364092684376947,
        "quantile_01": -0.06386075308370147,
        "quantile_99": 0.05400967188548553,
        "hill_tail_index": 2.335289355329583
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021577445230577717,
        "excess_kurtosis": 8.641125543202062,
        "return_acf_1": -0.16477821676089804,
        "abs_return_acf_1": 0.40731594677955835,
        "abs_return_acf_5": 0.40263365863088385,
        "abs_return_acf_20": 0.3152225223557623,
        "quantile_01": -0.06913667018674675,
        "quantile_99": 0.06516970704748373,
        "hill_tail_index": 3.477510336730708
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02063974469618709,
        "excess_kurtosis": 6.039932641485976,
        "return_acf_1": -0.24564696524523738,
        "abs_return_acf_1": 0.32599489389831,
        "abs_return_acf_5": 0.39021050234431864,
        "abs_return_acf_20": 0.4031112688468137,
        "quantile_01": -0.07618041503773121,
        "quantile_99": 0.05935426304637652,
        "hill_tail_index": 4.352629869719467
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018769455926566394,
        "excess_kurtosis": 9.366384252464206,
        "return_acf_1": -0.15894634938567126,
        "abs_return_acf_1": 0.36262647448797075,
        "abs_return_acf_5": 0.3789724840289837,
        "abs_return_acf_20": 0.3437350987240055,
        "quantile_01": -0.05028921162099059,
        "quantile_99": 0.05696402463882748,
        "hill_tail_index": 2.3532769757856777
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02050837629462155,
        "excess_kurtosis": 8.323648829805046,
        "return_acf_1": -0.15250188116175506,
        "abs_return_acf_1": 0.4222115680056513,
        "abs_return_acf_5": 0.38463909750007896,
        "abs_return_acf_20": 0.2724590754943573,
        "quantile_01": -0.07149146807866101,
        "quantile_99": 0.05923266083458742,
        "hill_tail_index": 2.360420734787457
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01874755971978809,
        "excess_kurtosis": 10.834739013139757,
        "return_acf_1": -0.19385873482132954,
        "abs_return_acf_1": 0.34172076123992096,
        "abs_return_acf_5": 0.34223666896535865,
        "abs_return_acf_20": 0.2183227537546348,
        "quantile_01": -0.0517975906160934,
        "quantile_99": 0.0514501952968513,
        "hill_tail_index": 2.4117317464374675
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018894798668544523,
        "excess_kurtosis": 6.850361292766463,
        "return_acf_1": -0.1742175305893464,
        "abs_return_acf_1": 0.29067192105554174,
        "abs_return_acf_5": 0.2893278231765602,
        "abs_return_acf_20": 0.23647323048728874,
        "quantile_01": -0.05214956538004439,
        "quantile_99": 0.05373597527526234,
        "hill_tail_index": 3.2936145343255996
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0185465421178086,
        "excess_kurtosis": 10.10623251431258,
        "return_acf_1": -0.15502338061911383,
        "abs_return_acf_1": 0.32245629026731715,
        "abs_return_acf_5": 0.30032162486790304,
        "abs_return_acf_20": 0.2541634767776501,
        "quantile_01": -0.05717028438617373,
        "quantile_99": 0.05154636237592097,
        "hill_tail_index": 2.898099822129351
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01996444425508685,
        "excess_kurtosis": 5.9181800413800545,
        "return_acf_1": -0.1506957317095384,
        "abs_return_acf_1": 0.34970933751234196,
        "abs_return_acf_5": 0.3245468675891687,
        "abs_return_acf_20": 0.2648891669339809,
        "quantile_01": -0.06392065393372084,
        "quantile_99": 0.05578011072204677,
        "hill_tail_index": 3.874424801995253
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02252657877656259,
        "excess_kurtosis": 8.262514851269497,
        "return_acf_1": -0.20076451450834262,
        "abs_return_acf_1": 0.43123673234379534,
        "abs_return_acf_5": 0.4196850655866374,
        "abs_return_acf_20": 0.2637938166800946,
        "quantile_01": -0.0678601924253176,
        "quantile_99": 0.06829388729130169,
        "hill_tail_index": 2.8205067746638823
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02026172671770592,
        "excess_kurtosis": 6.575565391018923,
        "return_acf_1": -0.2793071252392495,
        "abs_return_acf_1": 0.3982000606743852,
        "abs_return_acf_5": 0.39260893508436856,
        "abs_return_acf_20": 0.30661951199766924,
        "quantile_01": -0.07410431449190928,
        "quantile_99": 0.0616732643516811,
        "hill_tail_index": 3.3901102305847743
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019443401621822443,
        "excess_kurtosis": 11.391925394668354,
        "return_acf_1": -0.15055477497444214,
        "abs_return_acf_1": 0.33290884617423366,
        "abs_return_acf_5": 0.3530030147829956,
        "abs_return_acf_20": 0.21805989359793795,
        "quantile_01": -0.05163641000477445,
        "quantile_99": 0.051395976010632664,
        "hill_tail_index": 2.475473477584655
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021583207380296645,
        "excess_kurtosis": 13.378521276213593,
        "return_acf_1": -0.26087397995916073,
        "abs_return_acf_1": 0.37574350557983366,
        "abs_return_acf_5": 0.36731015478595147,
        "abs_return_acf_20": 0.33166245638341657,
        "quantile_01": -0.0555749708749889,
        "quantile_99": 0.05781633962189647,
        "hill_tail_index": 2.4915481977814267
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018672048912658657,
        "excess_kurtosis": 12.005585921792893,
        "return_acf_1": -0.12079789566585537,
        "abs_return_acf_1": 0.3422483252722658,
        "abs_return_acf_5": 0.3536559809402118,
        "abs_return_acf_20": 0.29758394451612474,
        "quantile_01": -0.06515374041948666,
        "quantile_99": 0.053050756396734296,
        "hill_tail_index": 2.1770985871665602
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02038192945111868,
        "excess_kurtosis": 8.301718814411498,
        "return_acf_1": -0.23027453926307312,
        "abs_return_acf_1": 0.39898712984834256,
        "abs_return_acf_5": 0.4594276119613052,
        "abs_return_acf_20": 0.26433527520584216,
        "quantile_01": -0.05754982327611457,
        "quantile_99": 0.056675650110181094,
        "hill_tail_index": 3.4428968716699924
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018671251732855818,
        "excess_kurtosis": 10.44120603540519,
        "return_acf_1": -0.20188995605849472,
        "abs_return_acf_1": 0.3271024837599862,
        "abs_return_acf_5": 0.2532346062683018,
        "abs_return_acf_20": 0.24839002518245148,
        "quantile_01": -0.059719137731073124,
        "quantile_99": 0.047326011086646025,
        "hill_tail_index": 2.091638071877312
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020575780388544577,
        "excess_kurtosis": 17.1672249726303,
        "return_acf_1": -0.18067144176921227,
        "abs_return_acf_1": 0.32558202538410563,
        "abs_return_acf_5": 0.35209371179176013,
        "abs_return_acf_20": 0.2415319285392,
        "quantile_01": -0.06660933758648664,
        "quantile_99": 0.049649196099188414,
        "hill_tail_index": 1.832244854455707
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020770935992560267,
        "excess_kurtosis": 2.707066976539335,
        "return_acf_1": -0.2187154405601822,
        "abs_return_acf_1": 0.2968368585761504,
        "abs_return_acf_5": 0.3002571925888039,
        "abs_return_acf_20": 0.29371811738122605,
        "quantile_01": -0.06643895937998151,
        "quantile_99": 0.054733618996039665,
        "hill_tail_index": 4.253002141843491
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02087835835214999,
        "excess_kurtosis": 12.235044424868256,
        "return_acf_1": -0.2027799958291664,
        "abs_return_acf_1": 0.3409813348338477,
        "abs_return_acf_5": 0.3195448611926514,
        "abs_return_acf_20": 0.21636488125284992,
        "quantile_01": -0.05840779320429903,
        "quantile_99": 0.05688975059627902,
        "hill_tail_index": 2.435709440983138
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018588049904527795,
        "excess_kurtosis": 5.118473123824817,
        "return_acf_1": -0.16382644014781722,
        "abs_return_acf_1": 0.29393746441189944,
        "abs_return_acf_5": 0.2826623461043781,
        "abs_return_acf_20": 0.1951367006781656,
        "quantile_01": -0.05672516008959915,
        "quantile_99": 0.055126086897952106,
        "hill_tail_index": 4.201954795571564
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018235465693187073,
        "excess_kurtosis": 10.534553136287917,
        "return_acf_1": -0.2447207211064701,
        "abs_return_acf_1": 0.32602993038374367,
        "abs_return_acf_5": 0.372935851141957,
        "abs_return_acf_20": 0.20057831442845273,
        "quantile_01": -0.05894318531013183,
        "quantile_99": 0.049889767954589256,
        "hill_tail_index": 3.0248989730528906
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019988581197716456,
        "excess_kurtosis": 5.755543970068892,
        "return_acf_1": -0.21810187823799446,
        "abs_return_acf_1": 0.4191677065174099,
        "abs_return_acf_5": 0.3997012320620277,
        "abs_return_acf_20": 0.30367221562264046,
        "quantile_01": -0.06803691005814545,
        "quantile_99": 0.05612071734850841,
        "hill_tail_index": 3.9346013664621635
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018534900573188295,
        "excess_kurtosis": 7.404151267254859,
        "return_acf_1": -0.21724444442977553,
        "abs_return_acf_1": 0.3456759939280721,
        "abs_return_acf_5": 0.27734953779499943,
        "abs_return_acf_20": 0.22960132170302358,
        "quantile_01": -0.0574246516566947,
        "quantile_99": 0.05217915832778567,
        "hill_tail_index": 3.5681143747648245
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021483779047648068,
        "excess_kurtosis": 6.718754078564597,
        "return_acf_1": -0.21924765637976334,
        "abs_return_acf_1": 0.4020022589440087,
        "abs_return_acf_5": 0.3589070062983306,
        "abs_return_acf_20": 0.2714621693361241,
        "quantile_01": -0.07504143398229832,
        "quantile_99": 0.060213276498246406,
        "hill_tail_index": 2.870177644534127
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022214020709703842,
        "excess_kurtosis": 6.188007362694426,
        "return_acf_1": -0.20712677923911552,
        "abs_return_acf_1": 0.38739665390170813,
        "abs_return_acf_5": 0.37923264560596265,
        "abs_return_acf_20": 0.23975246646507015,
        "quantile_01": -0.07672375312609003,
        "quantile_99": 0.06487557292348872,
        "hill_tail_index": 4.048893407485151
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021434537617151802,
        "excess_kurtosis": 8.417020123616718,
        "return_acf_1": -0.1794542770039989,
        "abs_return_acf_1": 0.3856003517360444,
        "abs_return_acf_5": 0.34056380720695734,
        "abs_return_acf_20": 0.2703715856354504,
        "quantile_01": -0.06673159866557359,
        "quantile_99": 0.06182546640042401,
        "hill_tail_index": 3.23791594879814
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017051742977097523,
        "excess_kurtosis": 8.3527578271793,
        "return_acf_1": -0.15844657417057748,
        "abs_return_acf_1": 0.22606682372422945,
        "abs_return_acf_5": 0.2960174774218415,
        "abs_return_acf_20": 0.18380383274778947,
        "quantile_01": -0.04713439405946577,
        "quantile_99": 0.04107154975743696,
        "hill_tail_index": 2.5176321988156114
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02037269752991659,
        "excess_kurtosis": 6.433796821325416,
        "return_acf_1": -0.20531084221565554,
        "abs_return_acf_1": 0.35379970402469557,
        "abs_return_acf_5": 0.35897703991304053,
        "abs_return_acf_20": 0.3045011644534094,
        "quantile_01": -0.060913220917839066,
        "quantile_99": 0.06053190048392997,
        "hill_tail_index": 3.506583437607697
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021171400756135876,
        "excess_kurtosis": 9.746712838812346,
        "return_acf_1": -0.20620547345103468,
        "abs_return_acf_1": 0.33224344017708646,
        "abs_return_acf_5": 0.30156552338791864,
        "abs_return_acf_20": 0.27135002459315344,
        "quantile_01": -0.07140095775926711,
        "quantile_99": 0.061232209671096306,
        "hill_tail_index": 3.505681660272346
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
