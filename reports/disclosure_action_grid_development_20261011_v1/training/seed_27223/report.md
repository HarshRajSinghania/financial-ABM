# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27223
Run ID: `29ac0c2503c7d5b18b6fb1a761f8881025816541d3a3879b25ea9dc0947ee1ae`
Result fingerprint: `23fd1fe7c599bbc34babeab939199c5f9013921c7de5e777befc8bd05a465e3c`

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
    "equal_weight_sd": -0.6854642857142824,
    "equal_weight_raw": -10.281964285714235,
    "fixed_start_cap_weight_sd": -0.7119788802833895,
    "fixed_start_cap_weight_raw": -10.679683204250844,
    "end_cap_weight_sd": -0.7110651787516066,
    "end_cap_weight_raw": -10.665977681274098
  },
  "full_period_change": {
    "equal_weight_sd": -1.0890714285714236,
    "equal_weight_raw": -16.336071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0300347222222177,
    "inflation_mean_sd": 0.6275016534391535
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.26691666666666986,
    "equal_weight_raw": 4.003750000000048,
    "fixed_start_cap_weight_sd": 0.2404020720975631,
    "fixed_start_cap_weight_raw": 3.6060310814634464,
    "end_cap_weight_sd": 0.2413157736293457,
    "end_cap_weight_raw": 3.6197366044401855
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7565476190476158,
      "change_raw": -11.348214285714237,
      "decay_adjusted_gain_sd": 0.19583333333333655
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7715476190476157,
      "change_raw": -11.573214285714236,
      "decay_adjusted_gain_sd": 0.18083333333333648
    },
    "small": {
      "count": 18,
      "change_sd": -0.6305753968253937,
      "change_raw": -9.458630952380904,
      "decay_adjusted_gain_sd": 0.3218055555555588
    },
    "large_minus_small_sd": -0.12597222222222215,
    "large_minus_small_raw": -1.8895833333333323
  },
  "inflation": {
    "initial_mean_sd": 0.3570833333333334,
    "final_mean_sd": 0.6262500000000001,
    "mean_sd": 0.5007934360255343,
    "mean_absolute_raw_gap": 7.511901540383014,
    "final_absolute_raw_gap": 9.39375,
    "mean_range_fraction": 0.07511901540383013
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.3,
    "initial_wealth_share": 0.2218949629194593,
    "final_wealth_share": 0.3277948254805964
  },
  "pricing_slope": {
    "mean": 0.00136460260053438,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.03990576964352363,
    "real_improvement_cost": 0.034288219938252484,
    "washing_cost": 0.005617549705271157,
    "fine_transfer": 0.027036161760705252,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06694193140422888,
    "resource_cost_fraction_initial_cap": 0.0013301923214507874,
    "private_net_outflow_fraction_initial_cap": 0.0022313977134742957,
    "fine_transfer_fraction_initial_cap": 0.0009012053920235082,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0006077425114886636,
    "unapplied_final_day_resource_cost": 0.02042493125020725
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 200.66020707107563,
    "beneficial_raw_gain_per_resource_cost": 3009.9031060661346,
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
    "accrued_cost": 3.165017628239557,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.18882715204908002,
    "accrued_cost_fraction_initial_cap": 0.10550058760798522,
    "mean_contract_rate": 0.042786420614328025,
    "maximum_ledger_error": 1.0672615135404184e-19
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
    "maximum_relative_cash_error": 1.5270448246061702e-15,
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
      "minimum": -0.2402493310595885,
      "maximum": -0.0765570212869743,
      "mean": -0.1661751702610639,
      "median": -0.1722429162169521,
      "quantile_05": -0.2126906243737678,
      "quantile_95": -0.11833671735324702
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
      "minimum": 0.20986340507708395,
      "maximum": 0.8230466920318708,
      "mean": 0.49603811844340245,
      "median": 0.4725749855136259,
      "quantile_05": 0.2668710089112267,
      "quantile_95": 0.7590022796477773
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
        "daily_volatility": 0.01940369132197,
        "excess_kurtosis": 3.5778772078685535,
        "return_acf_1": -0.19394190627589253,
        "abs_return_acf_1": 0.315979323246183,
        "abs_return_acf_5": 0.29607441970455356,
        "abs_return_acf_20": 0.2078149095468761,
        "quantile_01": -0.05730232674595128,
        "quantile_99": 0.05938523595231898,
        "hill_tail_index": 4.1117397340459245
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020771267718875445,
        "excess_kurtosis": 6.959590554404082,
        "return_acf_1": -0.1940027390387369,
        "abs_return_acf_1": 0.3205192631887936,
        "abs_return_acf_5": 0.31853913856034616,
        "abs_return_acf_20": 0.23695439120873568,
        "quantile_01": -0.0688928487469197,
        "quantile_99": 0.055338683319021836,
        "hill_tail_index": 3.1140063595402596
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01914614708926738,
        "excess_kurtosis": 3.652867563932362,
        "return_acf_1": -0.2142235861522892,
        "abs_return_acf_1": 0.29702343518975033,
        "abs_return_acf_5": 0.29405432932070524,
        "abs_return_acf_20": 0.2156725753179297,
        "quantile_01": -0.05331933778519222,
        "quantile_99": 0.0526711290583887,
        "hill_tail_index": 4.538825284346349
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022378272217103003,
        "excess_kurtosis": 9.42090450130953,
        "return_acf_1": -0.18109634727031645,
        "abs_return_acf_1": 0.39413218908362474,
        "abs_return_acf_5": 0.3946866020636286,
        "abs_return_acf_20": 0.30121822472711285,
        "quantile_01": -0.07185455329088894,
        "quantile_99": 0.06509120064927745,
        "hill_tail_index": 2.415904020283469
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022114924938908622,
        "excess_kurtosis": 10.924796577234607,
        "return_acf_1": -0.1746480261945233,
        "abs_return_acf_1": 0.33666575236002927,
        "abs_return_acf_5": 0.39302973206534003,
        "abs_return_acf_20": 0.23433987195965894,
        "quantile_01": -0.08112819838987015,
        "quantile_99": 0.060142748925787096,
        "hill_tail_index": 2.9653377182624747
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02038286732888499,
        "excess_kurtosis": 5.867274119132317,
        "return_acf_1": -0.1639723624693873,
        "abs_return_acf_1": 0.26691779984929886,
        "abs_return_acf_5": 0.2865752936968674,
        "abs_return_acf_20": 0.1866134346157447,
        "quantile_01": -0.056232536266852096,
        "quantile_99": 0.06154033760124894,
        "hill_tail_index": 3.230413087931344
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023132289424542606,
        "excess_kurtosis": 8.823863989712802,
        "return_acf_1": -0.13904721711441778,
        "abs_return_acf_1": 0.37597623858913565,
        "abs_return_acf_5": 0.36335691926351593,
        "abs_return_acf_20": 0.3329242485970504,
        "quantile_01": -0.07950706912158997,
        "quantile_99": 0.07524135914223112,
        "hill_tail_index": 3.4381745207743606
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02173740855768238,
        "excess_kurtosis": 8.928962959679154,
        "return_acf_1": -0.1542193670314944,
        "abs_return_acf_1": 0.4297393823651541,
        "abs_return_acf_5": 0.3217764027675296,
        "abs_return_acf_20": 0.2880637604441763,
        "quantile_01": -0.07239524349712345,
        "quantile_99": 0.05935232516152455,
        "hill_tail_index": 2.499628041537493
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.024006493062736896,
        "excess_kurtosis": 14.489689705623611,
        "return_acf_1": -0.17530193553818813,
        "abs_return_acf_1": 0.44901766791183406,
        "abs_return_acf_5": 0.33208947884647727,
        "abs_return_acf_20": 0.284048088860754,
        "quantile_01": -0.07007467482114657,
        "quantile_99": 0.0665913970099892,
        "hill_tail_index": 2.5265768186190463
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022517914414348885,
        "excess_kurtosis": 9.779032430206815,
        "return_acf_1": -0.17376055393189702,
        "abs_return_acf_1": 0.4243277305997723,
        "abs_return_acf_5": 0.44899050008287167,
        "abs_return_acf_20": 0.3235782621758125,
        "quantile_01": -0.0755853700930849,
        "quantile_99": 0.06233929242993829,
        "hill_tail_index": 3.291193510501099
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.023600655555671295,
        "excess_kurtosis": 6.172437208308935,
        "return_acf_1": -0.19884087981381043,
        "abs_return_acf_1": 0.3999880837448457,
        "abs_return_acf_5": 0.3829039266815882,
        "abs_return_acf_20": 0.30055627281023023,
        "quantile_01": -0.08317716772011585,
        "quantile_99": 0.060528426663629904,
        "hill_tail_index": 3.558191795425205
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01903120225638922,
        "excess_kurtosis": 5.3589491522610775,
        "return_acf_1": -0.15689397687906914,
        "abs_return_acf_1": 0.22958230291155535,
        "abs_return_acf_5": 0.2927276593159392,
        "abs_return_acf_20": 0.22250602442530473,
        "quantile_01": -0.061454084501321365,
        "quantile_99": 0.050909061218251526,
        "hill_tail_index": 2.9780072053622373
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020310806784720623,
        "excess_kurtosis": 7.618899091035971,
        "return_acf_1": -0.1536036264852855,
        "abs_return_acf_1": 0.37250269072136855,
        "abs_return_acf_5": 0.3197206485318083,
        "abs_return_acf_20": 0.28639689477549163,
        "quantile_01": -0.0595309623004374,
        "quantile_99": 0.06787639330264228,
        "hill_tail_index": 2.7540259807608716
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021999722108281244,
        "excess_kurtosis": 11.285991567948965,
        "return_acf_1": -0.17437170821410003,
        "abs_return_acf_1": 0.4055308048933789,
        "abs_return_acf_5": 0.4099370883703188,
        "abs_return_acf_20": 0.2575189166860444,
        "quantile_01": -0.07069092421957743,
        "quantile_99": 0.06125299186689802,
        "hill_tail_index": 2.695918924229526
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022877082358139927,
        "excess_kurtosis": 11.410049484062274,
        "return_acf_1": -0.2108170044222416,
        "abs_return_acf_1": 0.36719674720283896,
        "abs_return_acf_5": 0.33910663919112255,
        "abs_return_acf_20": 0.2877634379822864,
        "quantile_01": -0.07362477788334192,
        "quantile_99": 0.06639077729076584,
        "hill_tail_index": 2.7503944019414344
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.024627199597061788,
        "excess_kurtosis": 12.166741697851673,
        "return_acf_1": -0.13985556868185872,
        "abs_return_acf_1": 0.4434875673751941,
        "abs_return_acf_5": 0.3470302100907803,
        "abs_return_acf_20": 0.3194403855798936,
        "quantile_01": -0.07918310950989763,
        "quantile_99": 0.06892120125813232,
        "hill_tail_index": 2.5339211976737483
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022101315810856132,
        "excess_kurtosis": 8.641620867467417,
        "return_acf_1": -0.18148773401527898,
        "abs_return_acf_1": 0.325409233883363,
        "abs_return_acf_5": 0.3519407043545797,
        "abs_return_acf_20": 0.3411920565131984,
        "quantile_01": -0.07807096704820075,
        "quantile_99": 0.05813499054531177,
        "hill_tail_index": 3.321922557194397
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022704636016940994,
        "excess_kurtosis": 7.71092967846905,
        "return_acf_1": -0.1483583814514464,
        "abs_return_acf_1": 0.4002491907936897,
        "abs_return_acf_5": 0.3413300174786756,
        "abs_return_acf_20": 0.2833006157972145,
        "quantile_01": -0.08713719364707659,
        "quantile_99": 0.06278188790185353,
        "hill_tail_index": 3.0440704965490775
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022762642303696057,
        "excess_kurtosis": 14.642468418192319,
        "return_acf_1": -0.17307273479951368,
        "abs_return_acf_1": 0.26878287641193693,
        "abs_return_acf_5": 0.35771462905027573,
        "abs_return_acf_20": 0.25728424916386095,
        "quantile_01": -0.07983911628678209,
        "quantile_99": 0.054899226940946566,
        "hill_tail_index": 2.1851535048406467
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02530035307428193,
        "excess_kurtosis": 13.228986784882895,
        "return_acf_1": -0.15791411771225172,
        "abs_return_acf_1": 0.4433221298895693,
        "abs_return_acf_5": 0.37180821445996753,
        "abs_return_acf_20": 0.28499370539836627,
        "quantile_01": -0.08380955872238482,
        "quantile_99": 0.06390874282660236,
        "hill_tail_index": 2.463026149973
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01868876183011206,
        "excess_kurtosis": 8.729341621811448,
        "return_acf_1": -0.19878941145208853,
        "abs_return_acf_1": 0.3837775530178266,
        "abs_return_acf_5": 0.30560438043389965,
        "abs_return_acf_20": 0.2627845965045673,
        "quantile_01": -0.05352784142737833,
        "quantile_99": 0.04969468653338194,
        "hill_tail_index": 2.5462809144594374
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022917906048939313,
        "excess_kurtosis": 11.438457937121175,
        "return_acf_1": -0.17141309763439053,
        "abs_return_acf_1": 0.429839786589427,
        "abs_return_acf_5": 0.3565083319911878,
        "abs_return_acf_20": 0.2518436865289964,
        "quantile_01": -0.08214949322971889,
        "quantile_99": 0.06467605737891388,
        "hill_tail_index": 2.5666381838813597
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021522845668452643,
        "excess_kurtosis": 10.89243733407485,
        "return_acf_1": -0.1542421372737401,
        "abs_return_acf_1": 0.3770644974159669,
        "abs_return_acf_5": 0.336189951983451,
        "abs_return_acf_20": 0.24771434631914335,
        "quantile_01": -0.06040615497051891,
        "quantile_99": 0.06576731391774857,
        "hill_tail_index": 3.275888413587437
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0233284099087697,
        "excess_kurtosis": 10.021932147053322,
        "return_acf_1": -0.2402493310595885,
        "abs_return_acf_1": 0.4077405488692938,
        "abs_return_acf_5": 0.3129328743358488,
        "abs_return_acf_20": 0.24951349384081853,
        "quantile_01": -0.07950503697611375,
        "quantile_99": 0.06579959685296673,
        "hill_tail_index": 3.0859531140648926
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.022211156822156235,
        "excess_kurtosis": 10.216107252265322,
        "return_acf_1": -0.1417374580318135,
        "abs_return_acf_1": 0.32171779571062653,
        "abs_return_acf_5": 0.2668153205834078,
        "abs_return_acf_20": 0.3104025422175358,
        "quantile_01": -0.0725512152273856,
        "quantile_99": 0.05309983789072121,
        "hill_tail_index": 2.7727671765331365
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020039960769631507,
        "excess_kurtosis": 16.840741041945535,
        "return_acf_1": -0.0765570212869743,
        "abs_return_acf_1": 0.37201416533706383,
        "abs_return_acf_5": 0.3439372849477126,
        "abs_return_acf_20": 0.2688570635022798,
        "quantile_01": -0.04666539462782232,
        "quantile_99": 0.06628473032424591,
        "hill_tail_index": 1.8889359841882647
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017960360112256456,
        "excess_kurtosis": 8.662669601117376,
        "return_acf_1": -0.11568659437374856,
        "abs_return_acf_1": 0.20456327596884052,
        "abs_return_acf_5": 0.18242904968688325,
        "abs_return_acf_20": 0.19995532497309149,
        "quantile_01": -0.04530491839296061,
        "quantile_99": 0.054361201152156695,
        "hill_tail_index": 2.9264375355756185
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021492313556810406,
        "excess_kurtosis": 9.345490095140294,
        "return_acf_1": -0.1324137332440544,
        "abs_return_acf_1": 0.4104382711645221,
        "abs_return_acf_5": 0.3143387355270218,
        "abs_return_acf_20": 0.28849814827012904,
        "quantile_01": -0.06951859828719108,
        "quantile_99": 0.07384320968476042,
        "hill_tail_index": 2.9943471940321835
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022790955989433814,
        "excess_kurtosis": 7.677071293290837,
        "return_acf_1": -0.17316079343310775,
        "abs_return_acf_1": 0.3836325694000915,
        "abs_return_acf_5": 0.3703076824805433,
        "abs_return_acf_20": 0.3765756153863515,
        "quantile_01": -0.08004985464186087,
        "quantile_99": 0.07040292745743137,
        "hill_tail_index": 3.8222215488793014
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.024519628385753153,
        "excess_kurtosis": 12.039612803187062,
        "return_acf_1": -0.12157575655041178,
        "abs_return_acf_1": 0.43219890770392894,
        "abs_return_acf_5": 0.4047242894881469,
        "abs_return_acf_20": 0.2801727420883813,
        "quantile_01": -0.08883533390192679,
        "quantile_99": 0.07281056583646264,
        "hill_tail_index": 2.573318900548487
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
