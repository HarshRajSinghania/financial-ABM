# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27110
Run ID: `fe02655defa802e38bbf24264adce0a99746636616437597410ba64cfd0431ec`
Result fingerprint: `d3d006d607c3e14b171af3ce4519142f37f8f5f3478e3a47360aa27ca3f2ff48`

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
    "equal_weight_sd": -0.6452976190476157,
    "equal_weight_raw": -9.679464285714237,
    "fixed_start_cap_weight_sd": -0.5287673280794564,
    "fixed_start_cap_weight_raw": -7.9315099211918465,
    "end_cap_weight_sd": -0.573945750419909,
    "end_cap_weight_raw": -8.609186256298635
  },
  "full_period_change": {
    "equal_weight_sd": -1.0063214285714237,
    "equal_weight_raw": -15.094821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9565800264550219,
    "inflation_mean_sd": 0.6158832671957672
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.30708333333333654,
    "equal_weight_raw": 4.606250000000047,
    "fixed_start_cap_weight_sd": 0.42361362430149635,
    "fixed_start_cap_weight_raw": 6.354204364522441,
    "end_cap_weight_sd": 0.3784352019610431,
    "end_cap_weight_raw": 5.676528029415646
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.4590476190476158,
      "change_raw": -6.885714285714237,
      "decay_adjusted_gain_sd": 0.49333333333333657
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6576587301587269,
      "change_raw": -9.864880952380904,
      "decay_adjusted_gain_sd": 0.29472222222222544
    },
    "small": {
      "count": 18,
      "change_sd": -0.6701587301587268,
      "change_raw": -10.052380952380902,
      "decay_adjusted_gain_sd": 0.2822222222222254
    },
    "large_minus_small_sd": 0.21111111111111103,
    "large_minus_small_raw": 3.166666666666665
  },
  "inflation": {
    "initial_mean_sd": 0.26875,
    "final_mean_sd": 0.653,
    "mean_sd": 0.45990396891479324,
    "mean_absolute_raw_gap": 6.8985595337218975,
    "final_absolute_raw_gap": 9.794999999999998,
    "mean_range_fraction": 0.06898559533721897
  },
  "impact": {
    "initial_share": 0.19333333333333333,
    "final_share": 0.14666666666666667,
    "initial_wealth_share": 0.16257513665254314,
    "final_wealth_share": 0.12654595741693453
  },
  "pricing_slope": {
    "mean": -0.002111614181301363,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.06410969094793736,
    "real_improvement_cost": 0.04839782424031719,
    "washing_cost": 0.015711866707620172,
    "fine_transfer": 0.006577861663472063,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07068755261140942,
    "resource_cost_fraction_initial_cap": 0.002136989698264579,
    "private_net_outflow_fraction_initial_cap": 0.0023562517537136477,
    "fine_transfer_fraction_initial_cap": 0.00021926205544906877,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.019846701124151236,
    "unapplied_final_day_resource_cost": 0.0008535352839630639
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 143.69902371673334,
    "beneficial_raw_gain_per_resource_cost": 2155.485355751,
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
    "accrued_cost": 3.4407806185684935,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.4645901423780172,
    "accrued_cost_fraction_initial_cap": 0.11469268728561646,
    "mean_contract_rate": 0.04869777654881928,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 40,
    "maximum_relative_cash_error": 2.128685726400539e-15,
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
      "minimum": -0.42176960669064534,
      "maximum": -0.14206634745477154,
      "mean": -0.22029775744908367,
      "median": -0.21963592413536573,
      "quantile_05": -0.297336261212505,
      "quantile_95": -0.1538166049028417
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
      "minimum": -0.2293546337114586,
      "maximum": 0.8597469022750502,
      "mean": 0.6762026171043148,
      "median": 0.7565773672976468,
      "quantile_05": -0.16321142859461893,
      "quantile_95": 0.8286059811993782
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
        "daily_volatility": 0.024502589462672763,
        "excess_kurtosis": 10.19705879439529,
        "return_acf_1": -0.23833192680636647,
        "abs_return_acf_1": 0.4992710357429716,
        "abs_return_acf_5": 0.4023303209271029,
        "abs_return_acf_20": 0.34078235429283577,
        "quantile_01": -0.09211612851170886,
        "quantile_99": 0.07309244128519655,
        "hill_tail_index": 3.254734176767635
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024154512899859346,
        "excess_kurtosis": 8.978642405429007,
        "return_acf_1": -0.224607705089734,
        "abs_return_acf_1": 0.397966199508333,
        "abs_return_acf_5": 0.3846677164511319,
        "abs_return_acf_20": 0.3536112906658107,
        "quantile_01": -0.08671718357410459,
        "quantile_99": 0.07240021891743961,
        "hill_tail_index": 3.517633223549719
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.024975613828889524,
        "excess_kurtosis": 8.882298681194246,
        "return_acf_1": -0.2759162797830476,
        "abs_return_acf_1": 0.4923795033813122,
        "abs_return_acf_5": 0.4665054542635181,
        "abs_return_acf_20": 0.4105696068849796,
        "quantile_01": -0.09785383795899322,
        "quantile_99": 0.07198049903533658,
        "hill_tail_index": 4.242286488744623
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.023766484304788053,
        "excess_kurtosis": 11.549291780507179,
        "return_acf_1": -0.22556925562258448,
        "abs_return_acf_1": 0.45210635498042673,
        "abs_return_acf_5": 0.45982272611869307,
        "abs_return_acf_20": 0.35311995422958004,
        "quantile_01": -0.08980698586988488,
        "quantile_99": 0.060112718692605614,
        "hill_tail_index": 2.294571444039401
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.08082771917169242,
        "excess_kurtosis": 8.30560308332405,
        "return_acf_1": -0.42176960669064534,
        "abs_return_acf_1": 0.6716773353316319,
        "abs_return_acf_5": 0.6254430213456745,
        "abs_return_acf_20": 0.5009187541020801,
        "quantile_01": -0.2591817793182821,
        "quantile_99": 0.34985880757600313,
        "hill_tail_index": 5.078352103384481
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.025452526638579193,
        "excess_kurtosis": 11.960962353945831,
        "return_acf_1": -0.23318539593656218,
        "abs_return_acf_1": 0.5314419354718879,
        "abs_return_acf_5": 0.49857957713733353,
        "abs_return_acf_20": 0.35545476291408257,
        "quantile_01": -0.09573574475518101,
        "quantile_99": 0.06630946650646523,
        "hill_tail_index": 3.5405651807067056
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.025179431950583635,
        "excess_kurtosis": 11.36928529398788,
        "return_acf_1": -0.20477697329071234,
        "abs_return_acf_1": 0.48743201042670736,
        "abs_return_acf_5": 0.4980424048355069,
        "abs_return_acf_20": 0.3923277944044253,
        "quantile_01": -0.0929657674742095,
        "quantile_99": 0.07592860058842128,
        "hill_tail_index": 3.7018662025530102
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.026050578569299637,
        "excess_kurtosis": 10.808015477776705,
        "return_acf_1": -0.18127856585480576,
        "abs_return_acf_1": 0.4785544845490912,
        "abs_return_acf_5": 0.539543146750797,
        "abs_return_acf_20": 0.3689070391567499,
        "quantile_01": -0.11079201002565475,
        "quantile_99": 0.07224753742218958,
        "hill_tail_index": 2.7806702527071097
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02946708265126375,
        "excess_kurtosis": 13.517496974248669,
        "return_acf_1": -0.14206634745477154,
        "abs_return_acf_1": 0.5421564060617373,
        "abs_return_acf_5": 0.5510433514368249,
        "abs_return_acf_20": 0.35506739294172046,
        "quantile_01": -0.11121576030657426,
        "quantile_99": 0.09278753126603655,
        "hill_tail_index": 2.6820207650200714
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.025141330347524582,
        "excess_kurtosis": 11.378545811391906,
        "return_acf_1": -0.18411663919247623,
        "abs_return_acf_1": 0.5073369684417218,
        "abs_return_acf_5": 0.4342798844622966,
        "abs_return_acf_20": 0.33212534474787225,
        "quantile_01": -0.10635124771862375,
        "quantile_99": 0.0696114026312878,
        "hill_tail_index": 2.659227960628413
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02668110549016358,
        "excess_kurtosis": 13.21129288126646,
        "return_acf_1": -0.2483828252150628,
        "abs_return_acf_1": 0.473806557422663,
        "abs_return_acf_5": 0.4769575167023303,
        "abs_return_acf_20": 0.3456297415535957,
        "quantile_01": -0.11247886305727883,
        "quantile_99": 0.07468063709056758,
        "hill_tail_index": 2.898702554859234
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.025256598570401502,
        "excess_kurtosis": 10.896912592768395,
        "return_acf_1": -0.22250262293370873,
        "abs_return_acf_1": 0.49662974985999225,
        "abs_return_acf_5": 0.4582800859813256,
        "abs_return_acf_20": 0.3715388534190284,
        "quantile_01": -0.10527948318655812,
        "quantile_99": 0.0697832147493858,
        "hill_tail_index": 3.3305509774347546
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024458168718684014,
        "excess_kurtosis": 9.333068602367366,
        "return_acf_1": -0.16457527869799918,
        "abs_return_acf_1": 0.4954746807490545,
        "abs_return_acf_5": 0.5356878940658425,
        "abs_return_acf_20": 0.3777528727513084,
        "quantile_01": -0.10058471951287262,
        "quantile_99": 0.0656535697983156,
        "hill_tail_index": 3.20377662795392
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02709861301084314,
        "excess_kurtosis": 13.709327960719733,
        "return_acf_1": -0.16246949525902657,
        "abs_return_acf_1": 0.5398813210608981,
        "abs_return_acf_5": 0.545178968758144,
        "abs_return_acf_20": 0.40710955740196514,
        "quantile_01": -0.10962370076397472,
        "quantile_99": 0.08080908879437522,
        "hill_tail_index": 2.640063357371584
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.023513746999174964,
        "excess_kurtosis": 8.488444165895858,
        "return_acf_1": -0.22545032477736712,
        "abs_return_acf_1": 0.44374661496627743,
        "abs_return_acf_5": 0.4628220566935348,
        "abs_return_acf_20": 0.34034826924869505,
        "quantile_01": -0.090638888095557,
        "quantile_99": 0.06072947246814227,
        "hill_tail_index": 3.5103591420067195
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02538723599308029,
        "excess_kurtosis": 10.776805758702293,
        "return_acf_1": -0.16466082757875078,
        "abs_return_acf_1": 0.5012188242316374,
        "abs_return_acf_5": 0.4949351756021474,
        "abs_return_acf_20": 0.3990947467761751,
        "quantile_01": -0.09017508518980553,
        "quantile_99": 0.07888240678891514,
        "hill_tail_index": 3.329161516038849
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02512296825553977,
        "excess_kurtosis": 11.671390797469748,
        "return_acf_1": -0.18736228700220567,
        "abs_return_acf_1": 0.4505134857797934,
        "abs_return_acf_5": 0.4835456126625073,
        "abs_return_acf_20": 0.3622605886139869,
        "quantile_01": -0.09196599532436342,
        "quantile_99": 0.07666054533006142,
        "hill_tail_index": 3.3216505436607373
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.024716231022014628,
        "excess_kurtosis": 14.207177981673865,
        "return_acf_1": -0.2764466638329973,
        "abs_return_acf_1": 0.4975916981799302,
        "abs_return_acf_5": 0.4484817507361346,
        "abs_return_acf_20": 0.3756501332695246,
        "quantile_01": -0.09593816449967091,
        "quantile_99": 0.06287133255610157,
        "hill_tail_index": 2.2526519310667497
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02296545470885258,
        "excess_kurtosis": 7.972951889188723,
        "return_acf_1": -0.26321882944524544,
        "abs_return_acf_1": 0.4005715120900321,
        "abs_return_acf_5": 0.39680236644322625,
        "abs_return_acf_20": 0.35161327487845156,
        "quantile_01": -0.08253020114442705,
        "quantile_99": 0.06868110428536216,
        "hill_tail_index": 3.0823895169808844
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024351801984599384,
        "excess_kurtosis": 10.764230342753354,
        "return_acf_1": -0.23980706485101697,
        "abs_return_acf_1": 0.4450394059587645,
        "abs_return_acf_5": 0.4002930871563353,
        "abs_return_acf_20": 0.3902224437018092,
        "quantile_01": -0.08599686532410154,
        "quantile_99": 0.06954924313111939,
        "hill_tail_index": 2.701402426613778
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02526668896435052,
        "excess_kurtosis": 9.416734938995067,
        "return_acf_1": -0.14673696733869038,
        "abs_return_acf_1": 0.45391768773180063,
        "abs_return_acf_5": 0.49696626261668886,
        "abs_return_acf_20": 0.32533230600817786,
        "quantile_01": -0.08738319191729685,
        "quantile_99": 0.08048840029938095,
        "hill_tail_index": 4.037257599824964
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024536263914383925,
        "excess_kurtosis": 12.92883642307089,
        "return_acf_1": -0.19227689135739845,
        "abs_return_acf_1": 0.4392005744568891,
        "abs_return_acf_5": 0.3684910507579795,
        "abs_return_acf_20": 0.3421731867400855,
        "quantile_01": -0.08576767324075185,
        "quantile_99": 0.060680091092640345,
        "hill_tail_index": 2.3220516825858746
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02431323740710854,
        "excess_kurtosis": 8.332468466655147,
        "return_acf_1": -0.24621369655215114,
        "abs_return_acf_1": 0.5127129323660421,
        "abs_return_acf_5": 0.5124416047194046,
        "abs_return_acf_20": 0.42656261386103744,
        "quantile_01": -0.09227061551526654,
        "quantile_99": 0.06581039734413578,
        "hill_tail_index": 3.345281441500042
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.025106274264770963,
        "excess_kurtosis": 11.62783483906901,
        "return_acf_1": -0.19508754509582635,
        "abs_return_acf_1": 0.4171324281702872,
        "abs_return_acf_5": 0.4165058583349361,
        "abs_return_acf_20": 0.3482133905408622,
        "quantile_01": -0.09729815743199548,
        "quantile_99": 0.062353865772705123,
        "hill_tail_index": 2.5326334566301294
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.022845300827777894,
        "excess_kurtosis": 8.203349712015306,
        "return_acf_1": -0.1660701733804884,
        "abs_return_acf_1": 0.4796678045874261,
        "abs_return_acf_5": 0.4582711745605787,
        "abs_return_acf_20": 0.3139824485297775,
        "quantile_01": -0.08643610851518407,
        "quantile_99": 0.0663133986043325,
        "hill_tail_index": 3.6373260940568546
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.025001611018918325,
        "excess_kurtosis": 9.510454912579727,
        "return_acf_1": -0.1947775735331485,
        "abs_return_acf_1": 0.46771925349673915,
        "abs_return_acf_5": 0.42604390002737386,
        "abs_return_acf_20": 0.3943845795350643,
        "quantile_01": -0.09305671253516529,
        "quantile_99": 0.07440567163713441,
        "hill_tail_index": 3.501669059290624
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.024825986722774248,
        "excess_kurtosis": 11.012734451279309,
        "return_acf_1": -0.21676922533702273,
        "abs_return_acf_1": 0.48844175807288975,
        "abs_return_acf_5": 0.4579795407049632,
        "abs_return_acf_20": 0.3888730148859421,
        "quantile_01": -0.09780073776736371,
        "quantile_99": 0.07164320730218436,
        "hill_tail_index": 3.054287381898053
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02520925449253247,
        "excess_kurtosis": 10.453762544525368,
        "return_acf_1": -0.213734985668686,
        "abs_return_acf_1": 0.4264174790028237,
        "abs_return_acf_5": 0.4927523223698997,
        "abs_return_acf_20": 0.34562532953108854,
        "quantile_01": -0.09678811276903311,
        "quantile_99": 0.07564674552602735,
        "hill_tail_index": 2.980596548929268
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02628063049315017,
        "excess_kurtosis": 13.015223967466554,
        "return_acf_1": -0.2363429999164561,
        "abs_return_acf_1": 0.52409734057158,
        "abs_return_acf_5": 0.5125019900487572,
        "abs_return_acf_20": 0.38505140526470394,
        "quantile_01": -0.08311082850169664,
        "quantile_99": 0.0824728504948371,
        "hill_tail_index": 2.394379535981092
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.030419819985934335,
        "excess_kurtosis": 22.241772582237395,
        "return_acf_1": -0.31442774997755674,
        "abs_return_acf_1": 0.5538655735122562,
        "abs_return_acf_5": 0.43776395013231717,
        "abs_return_acf_20": 0.33325464719416437,
        "quantile_01": -0.1091765725888769,
        "quantile_99": 0.10036218921179911,
        "hill_tail_index": 2.375394693947907
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
