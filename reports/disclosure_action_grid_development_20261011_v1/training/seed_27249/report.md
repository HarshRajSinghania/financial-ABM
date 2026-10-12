# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27249
Run ID: `47580fb15e5bdeddcfa8b0aadcf6f20be59cd8c079490489891628b7b7d9e4a5`
Result fingerprint: `45e175e9bb8fd4aabb8612d1dcba8d2199a90056a7483b57fa4ca2a91b5c21bf`

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
    "equal_weight_sd": -0.8208015873015841,
    "equal_weight_raw": -12.312023809523765,
    "fixed_start_cap_weight_sd": -0.8014431550049471,
    "fixed_start_cap_weight_raw": -12.02164732507421,
    "end_cap_weight_sd": -0.7696346287677137,
    "end_cap_weight_raw": -11.544519431515704
  },
  "full_period_change": {
    "equal_weight_sd": -1.2496291395193144,
    "equal_weight_raw": -18.744437092789717
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1593751712653468,
    "inflation_mean_sd": 0.40733498677248675
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.09983333333333629,
    "equal_weight_raw": 1.497500000000045,
    "fixed_start_cap_weight_sd": 0.14761079479929634,
    "fixed_start_cap_weight_raw": 2.214161921989445,
    "end_cap_weight_sd": 0.17972525216104596,
    "end_cap_weight_raw": 2.695878782415689
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5857142857142827,
      "change_raw": -8.785714285714242,
      "decay_adjusted_gain_sd": 0.3666666666666696
    },
    "mid": {
      "count": 9,
      "change_sd": -0.9021031746031716,
      "change_raw": -13.531547619047574,
      "decay_adjusted_gain_sd": 0.05027777777778088
    },
    "small": {
      "count": 18,
      "change_sd": -0.8193320105820077,
      "change_raw": -12.289980158730115,
      "decay_adjusted_gain_sd": 0.08013888888889181
    },
    "large_minus_small_sd": 0.23361772486772492,
    "large_minus_small_raw": 3.504265873015874
  },
  "inflation": {
    "initial_mean_sd": 0.2765,
    "final_mean_sd": 0.4265833333333333,
    "mean_sd": 0.3424825839578129,
    "mean_absolute_raw_gap": 5.137238759367194,
    "final_absolute_raw_gap": 6.398749999999999,
    "mean_range_fraction": 0.051372387593671937
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.16,
    "initial_wealth_share": 0.1636597755262957,
    "final_wealth_share": 0.12457645195686222
  },
  "pricing_slope": {
    "mean": -0.0003428252229689098,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.031464895339196004,
    "real_improvement_cost": 0.02385282798592689,
    "washing_cost": 0.00761206735326911,
    "fine_transfer": 0.007256380197680238,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.038721275536876244,
    "resource_cost_fraction_initial_cap": 0.001048829844639867,
    "private_net_outflow_fraction_initial_cap": 0.0012907091845625418,
    "fine_transfer_fraction_initial_cap": 0.00024187933992267466,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0013543563760167576,
    "unapplied_final_day_resource_cost": 0.002404263115702536
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 95.18544294247816,
    "beneficial_raw_gain_per_resource_cost": 1427.7816441371724,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 3.162537169516529,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.18634669332605358,
    "accrued_cost_fraction_initial_cap": 0.105417905650551,
    "mean_contract_rate": 0.04354592701875987,
    "maximum_ledger_error": 5.039846036163087e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 2.5051381594790124e-15,
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
      "minimum": -0.2584966922896033,
      "maximum": -0.058555662328021896,
      "mean": -0.17121548277937368,
      "median": -0.17328793454674196,
      "quantile_05": -0.2401390099988925,
      "quantile_95": -0.10079013840482097
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
      "minimum": 0.09893397589347218,
      "maximum": 0.7945352834877437,
      "mean": 0.503729613331256,
      "median": 0.5157771113459653,
      "quantile_05": 0.1918968355291123,
      "quantile_95": 0.7477368115977993
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
        "daily_volatility": 0.030256511070915645,
        "excess_kurtosis": 27.740606175484857,
        "return_acf_1": -0.2584966922896033,
        "abs_return_acf_1": 0.5317730765125201,
        "abs_return_acf_5": 0.41126727442141586,
        "abs_return_acf_20": 0.3621052213657895,
        "quantile_01": -0.09898906431382148,
        "quantile_99": 0.08158282106106748,
        "hill_tail_index": 2.0350040635770767
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021779434569789355,
        "excess_kurtosis": 12.906742534457614,
        "return_acf_1": -0.058555662328021896,
        "abs_return_acf_1": 0.4418902756199629,
        "abs_return_acf_5": 0.3221802505974756,
        "abs_return_acf_20": 0.2607175960599963,
        "quantile_01": -0.07501100370766473,
        "quantile_99": 0.06425038447286965,
        "hill_tail_index": 2.59490640815374
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02219885954417737,
        "excess_kurtosis": 12.821878987919318,
        "return_acf_1": -0.12273687317735782,
        "abs_return_acf_1": 0.38964943925528894,
        "abs_return_acf_5": 0.36584871506577643,
        "abs_return_acf_20": 0.34338611775827294,
        "quantile_01": -0.0701631912016071,
        "quantile_99": 0.0675670152821717,
        "hill_tail_index": 2.91169339722311
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0218323416183934,
        "excess_kurtosis": 10.304415212049088,
        "return_acf_1": -0.22724008009608995,
        "abs_return_acf_1": 0.4192865627900657,
        "abs_return_acf_5": 0.36508499064101807,
        "abs_return_acf_20": 0.39258014423947696,
        "quantile_01": -0.07386136194184485,
        "quantile_99": 0.06712649798577217,
        "hill_tail_index": 3.1559474566332337
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024867988256054234,
        "excess_kurtosis": 14.399442023152897,
        "return_acf_1": -0.18688316346433567,
        "abs_return_acf_1": 0.471792966049335,
        "abs_return_acf_5": 0.437826956477515,
        "abs_return_acf_20": 0.29141831398274026,
        "quantile_01": -0.08941969546125163,
        "quantile_99": 0.06039507455015509,
        "hill_tail_index": 2.2725976411890505
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02200219562765401,
        "excess_kurtosis": 7.8153893135387715,
        "return_acf_1": -0.17324676331111757,
        "abs_return_acf_1": 0.4366307998046883,
        "abs_return_acf_5": 0.3698409051231596,
        "abs_return_acf_20": 0.39352233087725447,
        "quantile_01": -0.07113104125232866,
        "quantile_99": 0.06003937377401372,
        "hill_tail_index": 3.1549275161035064
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0244503806364266,
        "excess_kurtosis": 19.837950605160568,
        "return_acf_1": -0.1093140533361325,
        "abs_return_acf_1": 0.4374837528803011,
        "abs_return_acf_5": 0.39243005643401974,
        "abs_return_acf_20": 0.3006998359591939,
        "quantile_01": -0.06582940989002713,
        "quantile_99": 0.0776438173669505,
        "hill_tail_index": 2.5514057946218816
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022862165780897278,
        "excess_kurtosis": 9.71971156771905,
        "return_acf_1": -0.1578288591897981,
        "abs_return_acf_1": 0.4104119325605638,
        "abs_return_acf_5": 0.3770552354559934,
        "abs_return_acf_20": 0.3531147639796262,
        "quantile_01": -0.07559922638186108,
        "quantile_99": 0.06287698975767585,
        "hill_tail_index": 3.820869089064255
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019757443547219908,
        "excess_kurtosis": 8.061366570121875,
        "return_acf_1": -0.17332910578236632,
        "abs_return_acf_1": 0.4330385329559538,
        "abs_return_acf_5": 0.32074260143142963,
        "abs_return_acf_20": 0.2733362622878108,
        "quantile_01": -0.05860283464916093,
        "quantile_99": 0.05304388699640822,
        "hill_tail_index": 2.7930063143811226
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02168388500195181,
        "excess_kurtosis": 15.908186791919718,
        "return_acf_1": -0.21448368974615933,
        "abs_return_acf_1": 0.5185340340012026,
        "abs_return_acf_5": 0.3540372318867309,
        "abs_return_acf_20": 0.3036918068216081,
        "quantile_01": -0.07064305602248692,
        "quantile_99": 0.05305772022497443,
        "hill_tail_index": 2.4720370796118654
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02154982885037998,
        "excess_kurtosis": 5.494812006757277,
        "return_acf_1": -0.1499147271441207,
        "abs_return_acf_1": 0.30999456671813685,
        "abs_return_acf_5": 0.29969462433712035,
        "abs_return_acf_20": 0.29915719472858987,
        "quantile_01": -0.06987979412271032,
        "quantile_99": 0.056704422242298914,
        "hill_tail_index": 3.383996132729907
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020801819312367395,
        "excess_kurtosis": 8.637738219356565,
        "return_acf_1": -0.1678038781124871,
        "abs_return_acf_1": 0.36726297588670437,
        "abs_return_acf_5": 0.3911062962180849,
        "abs_return_acf_20": 0.32224717842442346,
        "quantile_01": -0.07279931930938832,
        "quantile_99": 0.06295053531114589,
        "hill_tail_index": 3.2211458764773826
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020429803109397602,
        "excess_kurtosis": 7.189948957755131,
        "return_acf_1": -0.13924888148966055,
        "abs_return_acf_1": 0.31864792891542865,
        "abs_return_acf_5": 0.28892274049394917,
        "abs_return_acf_20": 0.2894114905516711,
        "quantile_01": -0.0626327499828317,
        "quantile_99": 0.05325212266521794,
        "hill_tail_index": 3.1099131073589796
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02337542026706554,
        "excess_kurtosis": 11.521354107036007,
        "return_acf_1": -0.13281694313988518,
        "abs_return_acf_1": 0.35733693005092104,
        "abs_return_acf_5": 0.3112618200395024,
        "abs_return_acf_20": 0.3413833710076275,
        "quantile_01": -0.0784869182916432,
        "quantile_99": 0.06563358898461963,
        "hill_tail_index": 2.7690862167582195
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022745819681075308,
        "excess_kurtosis": 12.993597138882851,
        "return_acf_1": -0.14880161350693907,
        "abs_return_acf_1": 0.4499463345335661,
        "abs_return_acf_5": 0.3464539091571061,
        "abs_return_acf_20": 0.40356862992124115,
        "quantile_01": -0.08399755243629556,
        "quantile_99": 0.05719611938344783,
        "hill_tail_index": 2.2803221821664237
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020838699338013564,
        "excess_kurtosis": 13.924230726179655,
        "return_acf_1": -0.18529790883385955,
        "abs_return_acf_1": 0.40721863932824703,
        "abs_return_acf_5": 0.29250388957377066,
        "abs_return_acf_20": 0.31510098184885,
        "quantile_01": -0.06134005121423574,
        "quantile_99": 0.05281227618785173,
        "hill_tail_index": 2.5731205985484427
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022688132852468377,
        "excess_kurtosis": 6.194571285471149,
        "return_acf_1": -0.22781828166189894,
        "abs_return_acf_1": 0.4495233659111991,
        "abs_return_acf_5": 0.43403006561313995,
        "abs_return_acf_20": 0.3550565829207605,
        "quantile_01": -0.07632907465436523,
        "quantile_99": 0.07986078335419465,
        "hill_tail_index": 3.9485143241631095
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02131121466424584,
        "excess_kurtosis": 11.42297855456671,
        "return_acf_1": -0.2319572293578452,
        "abs_return_acf_1": 0.3681928292840855,
        "abs_return_acf_5": 0.33118960628093486,
        "abs_return_acf_20": 0.31845380249104455,
        "quantile_01": -0.07285328328531203,
        "quantile_99": 0.061010371822503885,
        "hill_tail_index": 3.1751466986612034
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022279779987621966,
        "excess_kurtosis": 11.372791653832031,
        "return_acf_1": -0.18773472481040718,
        "abs_return_acf_1": 0.41193952955376323,
        "abs_return_acf_5": 0.32960955580027507,
        "abs_return_acf_20": 0.4363261429304958,
        "quantile_01": -0.06779446125750654,
        "quantile_99": 0.059331229788440194,
        "hill_tail_index": 2.6704365993864227
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021778309910349177,
        "excess_kurtosis": 7.534137366437186,
        "return_acf_1": -0.17539989663526503,
        "abs_return_acf_1": 0.3562388443290543,
        "abs_return_acf_5": 0.30335390437249465,
        "abs_return_acf_20": 0.3074889978157624,
        "quantile_01": -0.07860009587083822,
        "quantile_99": 0.05887119280129924,
        "hill_tail_index": 3.141170523334741
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022806053475033037,
        "excess_kurtosis": 8.416989315125408,
        "return_acf_1": -0.1333305502773561,
        "abs_return_acf_1": 0.37108018021103645,
        "abs_return_acf_5": 0.37032696095508,
        "abs_return_acf_20": 0.38146477593838574,
        "quantile_01": -0.0902083837924359,
        "quantile_99": 0.06523056350571214,
        "hill_tail_index": 3.245492020307404
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024085862285299256,
        "excess_kurtosis": 19.871341049601735,
        "return_acf_1": -0.14084638792712684,
        "abs_return_acf_1": 0.3846765556302638,
        "abs_return_acf_5": 0.2834505300269694,
        "abs_return_acf_20": 0.36662299162535444,
        "quantile_01": -0.0754388677416571,
        "quantile_99": 0.06876158621625333,
        "hill_tail_index": 2.335690397695886
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02088870947903862,
        "excess_kurtosis": 5.105217937996372,
        "return_acf_1": -0.18523601337592327,
        "abs_return_acf_1": 0.4573596424796075,
        "abs_return_acf_5": 0.35384701508560684,
        "abs_return_acf_20": 0.3541364923233243,
        "quantile_01": -0.06685447339524761,
        "quantile_99": 0.05734508582511188,
        "hill_tail_index": 3.6583941422033215
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02784938851671456,
        "excess_kurtosis": 17.52245259799018,
        "return_acf_1": -0.24065859978812346,
        "abs_return_acf_1": 0.5503892792364466,
        "abs_return_acf_5": 0.5033697590111879,
        "abs_return_acf_20": 0.37752507116470935,
        "quantile_01": -0.10029971719160112,
        "quantile_99": 0.08732381838672629,
        "hill_tail_index": 2.6238457814000653
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02038007641007909,
        "excess_kurtosis": 5.727958023123847,
        "return_acf_1": -0.14703116280539197,
        "abs_return_acf_1": 0.3513217750173582,
        "abs_return_acf_5": 0.29367864964623736,
        "abs_return_acf_20": 0.31698117304955026,
        "quantile_01": -0.057698940100113616,
        "quantile_99": 0.057341896096579935,
        "hill_tail_index": 3.154624662409977
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.0209991021237053,
        "excess_kurtosis": 10.103371101109262,
        "return_acf_1": -0.1741336792408258,
        "abs_return_acf_1": 0.35967782313000196,
        "abs_return_acf_5": 0.25191293641773876,
        "abs_return_acf_20": 0.36395485334244754,
        "quantile_01": -0.07413819235421448,
        "quantile_99": 0.0553543668877903,
        "hill_tail_index": 2.361010080860562
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022891576032778402,
        "excess_kurtosis": 13.495963998425179,
        "return_acf_1": -0.147885810764093,
        "abs_return_acf_1": 0.36787202466967156,
        "abs_return_acf_5": 0.35601637930331326,
        "abs_return_acf_20": 0.27038584124864223,
        "quantile_01": -0.06788572152663085,
        "quantile_99": 0.06580027297714644,
        "hill_tail_index": 2.482326138580193
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022193456681665794,
        "excess_kurtosis": 16.658996524880926,
        "return_acf_1": -0.09381602618829328,
        "abs_return_acf_1": 0.36421917353312017,
        "abs_return_acf_5": 0.26754387858225576,
        "abs_return_acf_20": 0.3434107336584366,
        "quantile_01": -0.0658567123170182,
        "quantile_99": 0.05260261444250009,
        "hill_tail_index": 2.2735965282672255
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023207963374313596,
        "excess_kurtosis": 13.813193020472088,
        "return_acf_1": -0.20511326978867217,
        "abs_return_acf_1": 0.48501981259925153,
        "abs_return_acf_5": 0.387259849161347,
        "abs_return_acf_20": 0.28605502573005054,
        "quantile_01": -0.07988101157716564,
        "quantile_99": 0.0692364421271141,
        "hill_tail_index": 2.515996872358382
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02237713393912439,
        "excess_kurtosis": 17.823713352204074,
        "return_acf_1": -0.2395039558120547,
        "abs_return_acf_1": 0.49424991555574393,
        "abs_return_acf_5": 0.3662758306943103,
        "abs_return_acf_20": 0.32801061236886286,
        "quantile_01": -0.07375757858657475,
        "quantile_99": 0.05318347891429395,
        "hill_tail_index": 2.4207339250268975
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
