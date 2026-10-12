# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27230
Run ID: `7b25037b5e7235e8816ba90a23ccd364c90912e0141d550198543913cb544e4e`
Result fingerprint: `8b0a1191efa81b458958cdfebd6ddb4a1fb10288a88afe73bd2641b272d18b47`

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
    "equal_weight_sd": -0.613278693307189,
    "equal_weight_raw": -9.199180399607835,
    "fixed_start_cap_weight_sd": -0.5897202552269117,
    "fixed_start_cap_weight_raw": -8.845803828403678,
    "end_cap_weight_sd": -0.6113461654933494,
    "end_cap_weight_raw": -9.170192482400244
  },
  "full_period_change": {
    "equal_weight_sd": -1.037302502830997,
    "equal_weight_raw": -15.559537542464955
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9939442366850327,
    "inflation_mean_sd": 0.8108525132275133
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3177039465896583,
    "equal_weight_raw": 4.765559198844873,
    "fixed_start_cap_weight_sd": 0.3527078583213248,
    "fixed_start_cap_weight_raw": 5.290617874819872,
    "end_cap_weight_sd": 0.33060307380544757,
    "end_cap_weight_raw": 4.959046107081714
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5490476190476157,
      "change_raw": -8.235714285714234,
      "decay_adjusted_gain_sd": 0.40333333333333665
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6840476190476156,
      "change_raw": -10.260714285714233,
      "decay_adjusted_gain_sd": 0.2683333333333366
    },
    "small": {
      "count": 18,
      "change_sd": -0.5885994094802378,
      "change_raw": -8.828991142203567,
      "decay_adjusted_gain_sd": 0.32811768876053926
    },
    "large_minus_small_sd": 0.039551790432622136,
    "large_minus_small_raw": 0.593276856489332
  },
  "inflation": {
    "initial_mean_sd": 0.41200000000000003,
    "final_mean_sd": 0.8284166666666665,
    "mean_sd": 0.6367444490702193,
    "mean_absolute_raw_gap": 9.55116673605329,
    "final_absolute_raw_gap": 12.42625,
    "mean_range_fraction": 0.0955116673605329
  },
  "impact": {
    "initial_share": 0.22,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.15389510949959648,
    "final_wealth_share": 0.23161854408473256
  },
  "pricing_slope": {
    "mean": -0.0010310142618048168,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.08919794096795182,
    "real_improvement_cost": 0.06886587049020043,
    "washing_cost": 0.020332070477751388,
    "fine_transfer": 0.014657428916623635,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10385536988457546,
    "resource_cost_fraction_initial_cap": 0.002973264698931727,
    "private_net_outflow_fraction_initial_cap": 0.0034618456628191813,
    "fine_transfer_fraction_initial_cap": 0.0004885809638874544,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00066675304922586,
    "unapplied_final_day_resource_cost": 0.0009655067304318194
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 106.85356964814032,
    "beneficial_raw_gain_per_resource_cost": 1602.803544722105,
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
    "accrued_cost": 2.8343661946102428,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.1418242815802341,
    "accrued_cost_fraction_initial_cap": 0.09447887315367474,
    "mean_contract_rate": 0.039580248039702094,
    "maximum_ledger_error": 4.404571325722362e-20
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 8,
    "maximum_relative_cash_error": 4.519451139605927e-15,
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
      "minimum": -0.1681966546333161,
      "maximum": 0.011129402759801055,
      "mean": -0.07867079688362444,
      "median": -0.08164303457949694,
      "quantile_05": -0.156592123166673,
      "quantile_95": -0.018565323280688904
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
      "minimum": 0.2146563400034122,
      "maximum": 0.8160136077011525,
      "mean": 0.6152193557798444,
      "median": 0.6611248857577003,
      "quantile_05": 0.3362927875980193,
      "quantile_95": 0.7855908438470011
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
        "daily_volatility": 0.022593715500822766,
        "excess_kurtosis": 6.8720902021673975,
        "return_acf_1": -0.0930038534200643,
        "abs_return_acf_1": 0.41369924953020804,
        "abs_return_acf_5": 0.40184650311509273,
        "abs_return_acf_20": 0.33177750895114816,
        "quantile_01": -0.07916581622877095,
        "quantile_99": 0.06507432376615678,
        "hill_tail_index": 3.826734005256952
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.025724530512241172,
        "excess_kurtosis": 15.081391475675026,
        "return_acf_1": -0.04307237496049045,
        "abs_return_acf_1": 0.5182478259643651,
        "abs_return_acf_5": 0.561448181695712,
        "abs_return_acf_20": 0.3325756503279086,
        "quantile_01": -0.07357630992011867,
        "quantile_99": 0.0811667742565807,
        "hill_tail_index": 2.180483553903203
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021515677942698253,
        "excess_kurtosis": 27.84799582246576,
        "return_acf_1": -0.1314444417166599,
        "abs_return_acf_1": 0.4433285950927193,
        "abs_return_acf_5": 0.4870925217257355,
        "abs_return_acf_20": 0.3447209537032987,
        "quantile_01": -0.07753350554272802,
        "quantile_99": 0.05322431114854446,
        "hill_tail_index": 2.552888229460006
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019114757076979263,
        "excess_kurtosis": 30.637666092983494,
        "return_acf_1": -0.04134434194170705,
        "abs_return_acf_1": 0.2635309917347929,
        "abs_return_acf_5": 0.3221203134940605,
        "abs_return_acf_20": 0.21318716479387162,
        "quantile_01": -0.056772855275360655,
        "quantile_99": 0.04472989766569893,
        "hill_tail_index": 2.300967127430444
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02067319839652503,
        "excess_kurtosis": 23.724096496368176,
        "return_acf_1": -0.1071813222595518,
        "abs_return_acf_1": 0.3979905722934647,
        "abs_return_acf_5": 0.4450084560329276,
        "abs_return_acf_20": 0.3384908467290881,
        "quantile_01": -0.0702449928745266,
        "quantile_99": 0.046972496579680834,
        "hill_tail_index": 3.4564268009551373
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0200288275380677,
        "excess_kurtosis": 9.79611805579864,
        "return_acf_1": -0.06063441939211598,
        "abs_return_acf_1": 0.36413896696023185,
        "abs_return_acf_5": 0.3739466004014158,
        "abs_return_acf_20": 0.33281443725255727,
        "quantile_01": -0.0705736939691376,
        "quantile_99": 0.05089803030090594,
        "hill_tail_index": 2.8125937526159044
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020448597794505405,
        "excess_kurtosis": 35.14570189382978,
        "return_acf_1": -0.10071651319743109,
        "abs_return_acf_1": 0.44276213328941616,
        "abs_return_acf_5": 0.3814908939824726,
        "abs_return_acf_20": 0.36185042688191515,
        "quantile_01": -0.06884918045450725,
        "quantile_99": 0.04712248655563429,
        "hill_tail_index": 1.7861217540652081
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020400789455517945,
        "excess_kurtosis": 31.049168715201027,
        "return_acf_1": -0.04074683748335186,
        "abs_return_acf_1": 0.38318863870049147,
        "abs_return_acf_5": 0.42989616859409985,
        "abs_return_acf_20": 0.30049009797753745,
        "quantile_01": -0.059470278844386236,
        "quantile_99": 0.05419617751104748,
        "hill_tail_index": 1.749610141944715
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020003422869197367,
        "excess_kurtosis": 17.01509034142754,
        "return_acf_1": -0.10683098427608993,
        "abs_return_acf_1": 0.3523955510885798,
        "abs_return_acf_5": 0.370587730721389,
        "abs_return_acf_20": 0.2664884923780199,
        "quantile_01": -0.06414803553467607,
        "quantile_99": 0.05173657010410988,
        "hill_tail_index": 2.215218319578962
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01997820348905399,
        "excess_kurtosis": 30.21780146950543,
        "return_acf_1": -0.010531559654720527,
        "abs_return_acf_1": 0.3653354591314917,
        "abs_return_acf_5": 0.4616803940574391,
        "abs_return_acf_20": 0.3200866767779071,
        "quantile_01": -0.056065343811687415,
        "quantile_99": 0.0426891576530727,
        "hill_tail_index": 2.5929818329583454
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.0190898602008606,
        "excess_kurtosis": 21.290549079504906,
        "return_acf_1": -0.034211756216603606,
        "abs_return_acf_1": 0.28400162934420564,
        "abs_return_acf_5": 0.38339030507233063,
        "abs_return_acf_20": 0.2458337743080202,
        "quantile_01": -0.06243071388986359,
        "quantile_99": 0.04585915751195064,
        "hill_tail_index": 2.7412032698352022
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02075944951770146,
        "excess_kurtosis": 13.006326923874106,
        "return_acf_1": 0.011129402759801055,
        "abs_return_acf_1": 0.38114016339998674,
        "abs_return_acf_5": 0.4756516348486187,
        "abs_return_acf_20": 0.354613104023619,
        "quantile_01": -0.07450819549021287,
        "quantile_99": 0.04992561898342793,
        "hill_tail_index": 2.5343571452567706
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022008852616747593,
        "excess_kurtosis": 25.656670569336505,
        "return_acf_1": -0.16532439919052092,
        "abs_return_acf_1": 0.4266286767046144,
        "abs_return_acf_5": 0.48344522268757434,
        "abs_return_acf_20": 0.376543141983108,
        "quantile_01": -0.0804439657537973,
        "quantile_99": 0.06605502242563928,
        "hill_tail_index": 2.408221057895277
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022261076774077123,
        "excess_kurtosis": 11.566388547012226,
        "return_acf_1": -0.04199149487513968,
        "abs_return_acf_1": 0.3598935579487454,
        "abs_return_acf_5": 0.36782839415217033,
        "abs_return_acf_20": 0.2692391788641536,
        "quantile_01": -0.06814667051124354,
        "quantile_99": 0.06583836900078385,
        "hill_tail_index": 2.683848812725751
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020648903193522694,
        "excess_kurtosis": 14.622694459540671,
        "return_acf_1": -0.08319309530002535,
        "abs_return_acf_1": 0.3960325488676382,
        "abs_return_acf_5": 0.43712534236221195,
        "abs_return_acf_20": 0.3388390254027892,
        "quantile_01": -0.0655339030411906,
        "quantile_99": 0.054888987632986955,
        "hill_tail_index": 2.4073959860709944
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020876664567270834,
        "excess_kurtosis": 19.340753460582906,
        "return_acf_1": -0.1681966546333161,
        "abs_return_acf_1": 0.3995737717344039,
        "abs_return_acf_5": 0.4075131852581792,
        "abs_return_acf_20": 0.3143203096779826,
        "quantile_01": -0.08284866403769874,
        "quantile_99": 0.04938740428289628,
        "hill_tail_index": 3.141250541275352
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021939111237145544,
        "excess_kurtosis": 26.748782934919486,
        "return_acf_1": -0.06876294934432925,
        "abs_return_acf_1": 0.3927274168306955,
        "abs_return_acf_5": 0.4183979724978358,
        "abs_return_acf_20": 0.2689786176154523,
        "quantile_01": -0.07202967636154395,
        "quantile_99": 0.05575657984070318,
        "hill_tail_index": 2.0650307974985904
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02029972274783857,
        "excess_kurtosis": 25.60668978029867,
        "return_acf_1": -0.10721640223621513,
        "abs_return_acf_1": 0.3692345300202118,
        "abs_return_acf_5": 0.37257460314399393,
        "abs_return_acf_20": 0.23194431013349195,
        "quantile_01": -0.0691869838170961,
        "quantile_99": 0.04580784924055355,
        "hill_tail_index": 1.887110790311912
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021843712034760272,
        "excess_kurtosis": 25.03314996318931,
        "return_acf_1": -0.1459193413597478,
        "abs_return_acf_1": 0.43403040764224465,
        "abs_return_acf_5": 0.4417422893458465,
        "abs_return_acf_20": 0.3420473480518669,
        "quantile_01": -0.07916209534777678,
        "quantile_99": 0.0563884050422618,
        "hill_tail_index": 2.2570071362800292
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019166877094605184,
        "excess_kurtosis": 14.800713177330028,
        "return_acf_1": -0.028384367712427916,
        "abs_return_acf_1": 0.2996709675104803,
        "abs_return_acf_5": 0.3458522062918974,
        "abs_return_acf_20": 0.2283717505113914,
        "quantile_01": -0.060179983847535236,
        "quantile_99": 0.04672264528838855,
        "hill_tail_index": 2.538541924310802
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021623290936891394,
        "excess_kurtosis": 29.314978163157548,
        "return_acf_1": -0.0959048275064077,
        "abs_return_acf_1": 0.41533904367581126,
        "abs_return_acf_5": 0.46732725771998945,
        "abs_return_acf_20": 0.3742746494690857,
        "quantile_01": -0.0699340685929473,
        "quantile_99": 0.05742067387453474,
        "hill_tail_index": 1.8279358939983077
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01847215229026872,
        "excess_kurtosis": 25.936885148844862,
        "return_acf_1": -0.06805545755556905,
        "abs_return_acf_1": 0.2788759496887374,
        "abs_return_acf_5": 0.3541537361536305,
        "abs_return_acf_20": 0.25360527700476304,
        "quantile_01": -0.061886508962223856,
        "quantile_99": 0.04192187828918278,
        "hill_tail_index": 2.619116766276983
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02105302659427317,
        "excess_kurtosis": 28.04354671212451,
        "return_acf_1": -0.08188107521152516,
        "abs_return_acf_1": 0.31094049872850055,
        "abs_return_acf_5": 0.4172489283008882,
        "abs_return_acf_20": 0.37443189660299037,
        "quantile_01": -0.06315403884957749,
        "quantile_99": 0.05231734961530148,
        "hill_tail_index": 2.429185383702883
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019002333919207443,
        "excess_kurtosis": 41.68941563193811,
        "return_acf_1": -0.06682605813486524,
        "abs_return_acf_1": 0.3935054874660933,
        "abs_return_acf_5": 0.42917213947684885,
        "abs_return_acf_20": 0.28969520395734233,
        "quantile_01": -0.05355694834467987,
        "quantile_99": 0.03957383879733795,
        "hill_tail_index": 1.8565548827272025
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01975859191090805,
        "excess_kurtosis": 24.1546568454017,
        "return_acf_1": -0.10160889595046198,
        "abs_return_acf_1": 0.3305834332512353,
        "abs_return_acf_5": 0.3933380314303619,
        "abs_return_acf_20": 0.3214299986244709,
        "quantile_01": -0.06483046963004015,
        "quantile_99": 0.041055718406604276,
        "hill_tail_index": 2.34844218883875
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01778543409076215,
        "excess_kurtosis": 7.023749073277534,
        "return_acf_1": -0.08766554459711698,
        "abs_return_acf_1": 0.31000881728728713,
        "abs_return_acf_5": 0.29654483776364526,
        "abs_return_acf_20": 0.2947788179754068,
        "quantile_01": -0.056767676123695855,
        "quantile_99": 0.04964863251395673,
        "hill_tail_index": 3.531040494605876
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02250108846454609,
        "excess_kurtosis": 26.981919175062462,
        "return_acf_1": -0.06637506948231504,
        "abs_return_acf_1": 0.4305818209349498,
        "abs_return_acf_5": 0.4608636425333447,
        "abs_return_acf_20": 0.3536846479849961,
        "quantile_01": -0.07187799148942337,
        "quantile_99": 0.05481922180887168,
        "hill_tail_index": 1.9277790183534744
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020473586633442554,
        "excess_kurtosis": 23.56789829762841,
        "return_acf_1": -0.08140499394746872,
        "abs_return_acf_1": 0.34661181296038124,
        "abs_return_acf_5": 0.40333833016430465,
        "abs_return_acf_20": 0.31185891336567734,
        "quantile_01": -0.07727505265188352,
        "quantile_99": 0.050961828154606696,
        "hill_tail_index": 2.809417911702829
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01755828234711129,
        "excess_kurtosis": 12.85864781956052,
        "return_acf_1": -0.11290266006117945,
        "abs_return_acf_1": 0.31233597822208664,
        "abs_return_acf_5": 0.3504511216471405,
        "abs_return_acf_20": 0.21913183922423088,
        "quantile_01": -0.05007984135700562,
        "quantile_99": 0.04986723413270959,
        "hill_tail_index": 2.9814245079891633
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017830991714684805,
        "excess_kurtosis": 26.960945898157394,
        "return_acf_1": -0.029921617651116256,
        "abs_return_acf_1": 0.25095912962964617,
        "abs_return_acf_5": 0.2738747368923051,
        "abs_return_acf_20": 0.2532687822676754,
        "quantile_01": -0.05166100527741202,
        "quantile_99": 0.03777534995495412,
        "hill_tail_index": 2.319909094944391
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
