# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27128
Run ID: `a5693db5dea2de2124bb21cd1b965771830c4f7ffb0bf4ce196cb851aeba60a2`
Result fingerprint: `560e66c51e14becccd01a83184cf74247ef2dcfda5e5b8283d04efae839a93bd`

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
    "equal_weight_sd": -0.7006309523809492,
    "equal_weight_raw": -10.50946428571424,
    "fixed_start_cap_weight_sd": -0.6521323148322015,
    "fixed_start_cap_weight_raw": -9.781984722483022,
    "end_cap_weight_sd": -0.6650064917908138,
    "end_cap_weight_raw": -9.975097376862209
  },
  "full_period_change": {
    "equal_weight_sd": -1.044404761904757,
    "equal_weight_raw": -15.666071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9900046296296251,
    "inflation_mean_sd": 0.5702040343915344
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2517500000000032,
    "equal_weight_raw": 3.776250000000047,
    "fixed_start_cap_weight_sd": 0.3002486375487509,
    "fixed_start_cap_weight_raw": 4.503729563231264,
    "end_cap_weight_sd": 0.28737446059013805,
    "end_cap_weight_raw": 4.310616908852069
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6348809523809492,
      "change_raw": -9.523214285714237,
      "decay_adjusted_gain_sd": 0.3175000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5590476190476159,
      "change_raw": -8.385714285714238,
      "decay_adjusted_gain_sd": 0.3933333333333365
    },
    "small": {
      "count": 18,
      "change_sd": -0.7823809523809492,
      "change_raw": -11.735714285714238,
      "decay_adjusted_gain_sd": 0.17000000000000318
    },
    "large_minus_small_sd": 0.14749999999999996,
    "large_minus_small_raw": 2.2124999999999995
  },
  "inflation": {
    "initial_mean_sd": 0.2678333333333333,
    "final_mean_sd": 0.5867500000000001,
    "mean_sd": 0.44715244240910357,
    "mean_absolute_raw_gap": 6.707286636136553,
    "final_absolute_raw_gap": 8.80125,
    "mean_range_fraction": 0.06707286636136553
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.25333333333333335,
    "initial_wealth_share": 0.22791023247077588,
    "final_wealth_share": 0.20419043760871125
  },
  "pricing_slope": {
    "mean": -0.00261107571879241,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999982,
    "resource_cost": 0.1395633520485811,
    "real_improvement_cost": 0.119450874920306,
    "washing_cost": 0.020112477128275106,
    "fine_transfer": 0.003462627462306026,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.14302597951088714,
    "resource_cost_fraction_initial_cap": 0.004652111734952707,
    "private_net_outflow_fraction_initial_cap": 0.004767532650362907,
    "fine_transfer_fraction_initial_cap": 0.00011542091541020095,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0022382221627555055,
    "unapplied_final_day_resource_cost": 0.00014444637925957641
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 54.11520925186089,
    "beneficial_raw_gain_per_resource_cost": 811.7281387779134,
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
    "fixed_exposure": 14.999999999999991,
    "accrued_cost": 2.982093811730257,
    "baseline_accrued_cost": 2.976190476190474,
    "value_adjustment": -0.00590333553978202,
    "accrued_cost_fraction_initial_cap": 0.0994031270576753,
    "mean_contract_rate": 0.040525746227777465,
    "maximum_ledger_error": 2.270048298641525e-19
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
    "maximum_relative_cash_error": 1.4309406726503066e-15,
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
      "minimum": -0.2273704874797222,
      "maximum": -0.020881417426496133,
      "mean": -0.12583626328541878,
      "median": -0.114364491656058,
      "quantile_05": -0.22207618412793317,
      "quantile_95": -0.027361575912087408
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
      "minimum": 0.20498578640346865,
      "maximum": 0.787051321869546,
      "mean": 0.45512102769992036,
      "median": 0.40743665612118335,
      "quantile_05": 0.25811566772783073,
      "quantile_95": 0.7372270872784709
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
        "daily_volatility": 0.020900462018060534,
        "excess_kurtosis": 7.4081399307102345,
        "return_acf_1": -0.2273704874797222,
        "abs_return_acf_1": 0.4968653755769433,
        "abs_return_acf_5": 0.39085617039262266,
        "abs_return_acf_20": 0.4063787302824094,
        "quantile_01": -0.06905279307705592,
        "quantile_99": 0.06804792472177688,
        "hill_tail_index": 3.8027389701781176
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018391104881326188,
        "excess_kurtosis": 10.52450532781042,
        "return_acf_1": -0.08545671324344839,
        "abs_return_acf_1": 0.2612193517276019,
        "abs_return_acf_5": 0.17822881561818718,
        "abs_return_acf_20": 0.27432043287181335,
        "quantile_01": -0.04806591224349987,
        "quantile_99": 0.06144619660905129,
        "hill_tail_index": 2.1927066438596547
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021453489153896454,
        "excess_kurtosis": 13.387191554759355,
        "return_acf_1": -0.19399154989252876,
        "abs_return_acf_1": 0.4563807476718864,
        "abs_return_acf_5": 0.4747770460280234,
        "abs_return_acf_20": 0.24198618215215328,
        "quantile_01": -0.07540402898132172,
        "quantile_99": 0.06091907920642251,
        "hill_tail_index": 2.8206445341974535
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019452619800946258,
        "excess_kurtosis": 14.958678704575668,
        "return_acf_1": -0.19246470284501077,
        "abs_return_acf_1": 0.38407679336282424,
        "abs_return_acf_5": 0.46045504574021534,
        "abs_return_acf_20": 0.3042528933330941,
        "quantile_01": -0.057475093640879694,
        "quantile_99": 0.04667761840278371,
        "hill_tail_index": 2.776262554588597
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017642639744130634,
        "excess_kurtosis": 6.793910201436642,
        "return_acf_1": -0.0828322526652776,
        "abs_return_acf_1": 0.3157571805795677,
        "abs_return_acf_5": 0.30952234565532966,
        "abs_return_acf_20": 0.2671883884613647,
        "quantile_01": -0.05311936794846417,
        "quantile_99": 0.05551695553746109,
        "hill_tail_index": 2.6062290648236943
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019484300405881047,
        "excess_kurtosis": 7.304984940925449,
        "return_acf_1": -0.029953140693410818,
        "abs_return_acf_1": 0.3915027320987603,
        "abs_return_acf_5": 0.36306854253287885,
        "abs_return_acf_20": 0.3027802597657916,
        "quantile_01": -0.06876636000681702,
        "quantile_99": 0.0569655972881835,
        "hill_tail_index": 3.296142942879574
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02173182688336171,
        "excess_kurtosis": 8.789704920026182,
        "return_acf_1": -0.22191113913953955,
        "abs_return_acf_1": 0.47929241908768505,
        "abs_return_acf_5": 0.42676282511296665,
        "abs_return_acf_20": 0.38673453745359376,
        "quantile_01": -0.0680043965835281,
        "quantile_99": 0.07497895113767461,
        "hill_tail_index": 3.29639468439428
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01915331891116997,
        "excess_kurtosis": 4.7380823448878555,
        "return_acf_1": -0.06631427929922033,
        "abs_return_acf_1": 0.32343628940411145,
        "abs_return_acf_5": 0.32265414353445515,
        "abs_return_acf_20": 0.2946292970803537,
        "quantile_01": -0.06000415465993957,
        "quantile_99": 0.05596783952161129,
        "hill_tail_index": 4.180747171382222
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02172493571887392,
        "excess_kurtosis": 13.683504246470552,
        "return_acf_1": -0.025241204727368228,
        "abs_return_acf_1": 0.46841742040834705,
        "abs_return_acf_5": 0.5125581205578791,
        "abs_return_acf_20": 0.31293735235776676,
        "quantile_01": -0.07351153223118574,
        "quantile_99": 0.06602898064236674,
        "hill_tail_index": 2.7522349055897397
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022558829924239913,
        "excess_kurtosis": 14.752146171448349,
        "return_acf_1": -0.22049174470974586,
        "abs_return_acf_1": 0.49537196649747567,
        "abs_return_acf_5": 0.47768018353913266,
        "abs_return_acf_20": 0.3798406366961659,
        "quantile_01": -0.07448104613395148,
        "quantile_99": 0.07244160126436161,
        "hill_tail_index": 2.839044219095168
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016987576816725795,
        "excess_kurtosis": 4.122901243973474,
        "return_acf_1": -0.14402729147404963,
        "abs_return_acf_1": 0.2679978789215854,
        "abs_return_acf_5": 0.17501142992718788,
        "abs_return_acf_20": 0.16726855084970813,
        "quantile_01": -0.048663200075145095,
        "quantile_99": 0.04927606262663038,
        "hill_tail_index": 4.130337425595922
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018809731763490628,
        "excess_kurtosis": 13.836003491069697,
        "return_acf_1": -0.020881417426496133,
        "abs_return_acf_1": 0.41960726882298655,
        "abs_return_acf_5": 0.46320388530801976,
        "abs_return_acf_20": 0.2464355702490528,
        "quantile_01": -0.0571723519092243,
        "quantile_99": 0.04854068412305556,
        "hill_tail_index": 2.097930510501361
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019368369209715585,
        "excess_kurtosis": 8.074950314113716,
        "return_acf_1": -0.08525805609354017,
        "abs_return_acf_1": 0.3267843752813735,
        "abs_return_acf_5": 0.3468527954596705,
        "abs_return_acf_20": 0.2900094586691485,
        "quantile_01": -0.057763638340217825,
        "quantile_99": 0.05458362763135875,
        "hill_tail_index": 3.063912559840326
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01844359829404651,
        "excess_kurtosis": 3.8801334028636605,
        "return_acf_1": -0.09215042470607276,
        "abs_return_acf_1": 0.2633078634055328,
        "abs_return_acf_5": 0.2712586596597644,
        "abs_return_acf_20": 0.23194019479565947,
        "quantile_01": -0.049279936938041,
        "quantile_99": 0.052248344423343494,
        "hill_tail_index": 4.114647136570282
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0192484344929213,
        "excess_kurtosis": 10.342325719602995,
        "return_acf_1": -0.10714913465407304,
        "abs_return_acf_1": 0.3489504988190609,
        "abs_return_acf_5": 0.3827160059240581,
        "abs_return_acf_20": 0.38248310487248294,
        "quantile_01": -0.07004855286431148,
        "quantile_99": 0.05346738158333613,
        "hill_tail_index": 3.2743341638404777
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018020317902942125,
        "excess_kurtosis": 10.763337871345426,
        "return_acf_1": -0.03187490401893682,
        "abs_return_acf_1": 0.3044586864289696,
        "abs_return_acf_5": 0.37994900417978156,
        "abs_return_acf_20": 0.23271285744535436,
        "quantile_01": -0.054638096881810115,
        "quantile_99": 0.046782931536175104,
        "hill_tail_index": 2.223758669319179
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019614162286117332,
        "excess_kurtosis": 6.618064032550242,
        "return_acf_1": -0.22221122093661888,
        "abs_return_acf_1": 0.43843744991930056,
        "abs_return_acf_5": 0.36862490059560354,
        "abs_return_acf_20": 0.33243072753657094,
        "quantile_01": -0.0580145362992372,
        "quantile_99": 0.06083095989500814,
        "hill_tail_index": 3.2353640304848894
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01995164281115849,
        "excess_kurtosis": 11.577694727595247,
        "return_acf_1": -0.20286753632822008,
        "abs_return_acf_1": 0.43794994718834923,
        "abs_return_acf_5": 0.3354432022008834,
        "abs_return_acf_20": 0.31375364102194264,
        "quantile_01": -0.06190040085605422,
        "quantile_99": 0.053353306141391256,
        "hill_tail_index": 2.8894445593310616
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.024130681620749047,
        "excess_kurtosis": 22.675293068580196,
        "return_acf_1": -0.20967684815789997,
        "abs_return_acf_1": 0.48325519779595194,
        "abs_return_acf_5": 0.4487612949124289,
        "abs_return_acf_20": 0.3489950994357847,
        "quantile_01": -0.07888941330497658,
        "quantile_99": 0.07025613804627531,
        "hill_tail_index": 2.384031881933824
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01791470486786527,
        "excess_kurtosis": 11.088309227226215,
        "return_acf_1": -0.15122725006198615,
        "abs_return_acf_1": 0.3729907134595554,
        "abs_return_acf_5": 0.3336425596090412,
        "abs_return_acf_20": 0.20142640078109333,
        "quantile_01": -0.04911183454461807,
        "quantile_99": 0.04655434376792829,
        "hill_tail_index": 2.8450225260729365
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022660815775958815,
        "excess_kurtosis": 21.398462537231865,
        "return_acf_1": -0.12316307026122156,
        "abs_return_acf_1": 0.4136719305984928,
        "abs_return_acf_5": 0.4730589894848949,
        "abs_return_acf_20": 0.2155161370652679,
        "quantile_01": -0.08559624982182626,
        "quantile_99": 0.06341861397274252,
        "hill_tail_index": 2.4468845813579105
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018380761698632477,
        "excess_kurtosis": 13.19716830271534,
        "return_acf_1": -0.07014911143021584,
        "abs_return_acf_1": 0.4063514548488898,
        "abs_return_acf_5": 0.43219542706978237,
        "abs_return_acf_20": 0.24518402449380827,
        "quantile_01": -0.06083473693657654,
        "quantile_99": 0.046331617352743985,
        "hill_tail_index": 2.336191618548403
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019344070590391595,
        "excess_kurtosis": 9.115607850949594,
        "return_acf_1": -0.132961586839465,
        "abs_return_acf_1": 0.3301286935215443,
        "abs_return_acf_5": 0.31248861238814024,
        "abs_return_acf_20": 0.2754977683332467,
        "quantile_01": -0.05328394708682231,
        "quantile_99": 0.05637829000603831,
        "hill_tail_index": 3.280378801924511
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01934961417241802,
        "excess_kurtosis": 6.570960999248051,
        "return_acf_1": -0.13720224947649137,
        "abs_return_acf_1": 0.3656232528438612,
        "abs_return_acf_5": 0.3904956114114541,
        "abs_return_acf_20": 0.29234160669633413,
        "quantile_01": -0.05665749802977717,
        "quantile_99": 0.05921570906639625,
        "hill_tail_index": 2.8289843410395474
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01976385292547301,
        "excess_kurtosis": 11.946897255422352,
        "return_acf_1": -0.09358790700208983,
        "abs_return_acf_1": 0.35593530886128233,
        "abs_return_acf_5": 0.4870629098692277,
        "abs_return_acf_20": 0.2582064746834124,
        "quantile_01": -0.06163579796407926,
        "quantile_99": 0.04464882630853556,
        "hill_tail_index": 2.104237386434828
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016873574819588517,
        "excess_kurtosis": 5.719101234149937,
        "return_acf_1": -0.16290831410184828,
        "abs_return_acf_1": 0.29669760587166805,
        "abs_return_acf_5": 0.3147477227779682,
        "abs_return_acf_20": 0.30026572576845684,
        "quantile_01": -0.04825980154760537,
        "quantile_99": 0.044534003796722864,
        "hill_tail_index": 3.3741743614503124
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018739453572980097,
        "excess_kurtosis": 8.167059729291324,
        "return_acf_1": -0.1096485143345303,
        "abs_return_acf_1": 0.3548694300762819,
        "abs_return_acf_5": 0.3954582126735479,
        "abs_return_acf_20": 0.3617918833402479,
        "quantile_01": -0.061619768756578215,
        "quantile_99": 0.05508650397194411,
        "hill_tail_index": 3.128376982460689
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018098260715999286,
        "excess_kurtosis": 4.221701029664632,
        "return_acf_1": -0.11508682421586867,
        "abs_return_acf_1": 0.27179724875050765,
        "abs_return_acf_5": 0.3052509481944753,
        "abs_return_acf_20": 0.29935130263188003,
        "quantile_01": -0.058383856955371384,
        "quantile_99": 0.05322073080949945,
        "hill_tail_index": 4.484926944633889
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02117904623463055,
        "excess_kurtosis": 24.783239798315115,
        "return_acf_1": -0.11364215909624731,
        "abs_return_acf_1": 0.4741145014353956,
        "abs_return_acf_5": 0.44916961481854684,
        "abs_return_acf_20": 0.22447502803776023,
        "quantile_01": -0.059224390993622325,
        "quantile_99": 0.050819867334721776,
        "hill_tail_index": 2.075663440152017
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01805024907339885,
        "excess_kurtosis": 5.567441098517355,
        "return_acf_1": -0.10338686325141888,
        "abs_return_acf_1": 0.2994512587144641,
        "abs_return_acf_5": 0.332282452208331,
        "abs_return_acf_20": 0.32161684228552934,
        "quantile_01": -0.06216786050283753,
        "quantile_99": 0.04759884895844146,
        "hill_tail_index": 3.3428332824544067
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
