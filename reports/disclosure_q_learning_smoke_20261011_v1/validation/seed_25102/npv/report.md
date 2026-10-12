# Disclosure-market run

Purpose: development
Domain: esg
Seed: 25102
Run ID: `cfb5ed9e8308b76cf0fbde9336d018ef79f18af667aa332f6c0ea17c633f42c4`
Result fingerprint: `803fdf746e7fe898759546325a17f8d07ff1ac1a1599c7be9cc5763d256d207e`

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
    "equal_weight_sd": -0.733591796764029,
    "equal_weight_raw": -11.003876951460434,
    "fixed_start_cap_weight_sd": -0.6921798177256557,
    "fixed_start_cap_weight_raw": -10.38269726588484,
    "end_cap_weight_sd": -0.7029799513196268,
    "end_cap_weight_raw": -10.5446992697944
  },
  "full_period_change": {
    "equal_weight_sd": -1.1730102568309901,
    "equal_weight_raw": -17.59515385246485
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1062939625432682,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2187891556169235,
    "equal_weight_raw": 3.2818373342538525,
    "fixed_start_cap_weight_sd": 0.2602011346552966,
    "fixed_start_cap_weight_raw": 3.9030170198294507,
    "end_cap_weight_sd": 0.24940100106132548,
    "end_cap_weight_raw": 3.7410150159198805
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6697158091474816,
      "change_raw": -10.045737137212225,
      "decay_adjusted_gain_sd": 0.28266514323347075
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6510457315138694,
      "change_raw": -9.76568597270804,
      "decay_adjusted_gain_sd": 0.30133522086708303
    },
    "small": {
      "count": 18,
      "change_sd": -0.7855108273251998,
      "change_raw": -11.782662409877997,
      "decay_adjusted_gain_sd": 0.1668701250557525
    },
    "large_minus_small_sd": 0.1157950181777182,
    "large_minus_small_raw": 1.736925272665773
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.34,
    "final_share": 0.34,
    "initial_wealth_share": 0.39186521701389393,
    "final_wealth_share": 0.4735585794013585
  },
  "pricing_slope": {
    "mean": -0.0011360950379303912,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.001163349112268269,
    "real_improvement_cost": 0.001163349112268269,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.001163349112268269,
    "resource_cost_fraction_initial_cap": 3.877830374227562e-05,
    "private_net_outflow_fraction_initial_cap": 3.877830374227562e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 2.7388299618775143e-05,
    "unapplied_final_day_resource_cost": 9.801389025879161e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 5642.050695951464,
    "beneficial_raw_gain_per_resource_cost": 84630.76043927197,
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
    "fixed_exposure": 15.000000000000005,
    "accrued_cost": 2.9437792850365057,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.0324111911539718,
    "accrued_cost_fraction_initial_cap": 0.09812597616788349,
    "mean_contract_rate": 0.04008673442877557,
    "maximum_ledger_error": 6.606856988583543e-20
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
    "maximum_relative_cash_error": 1.7637546467829314e-15,
    "maximum_absolute_share_error": 2.6645352591003757e-15,
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
      "minimum": -0.2680223680185621,
      "maximum": -0.05295726332328468,
      "mean": -0.1671734633204715,
      "median": -0.16996536389820338,
      "quantile_05": -0.24493183943833838,
      "quantile_95": -0.08510392212446957
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
      "minimum": 0.17036241267735172,
      "maximum": 0.8471493462640656,
      "mean": 0.5326654855006892,
      "median": 0.6212356603409682,
      "quantile_05": 0.2224666980774423,
      "quantile_95": 0.8045808435274202
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
        "daily_volatility": 0.023310613531211624,
        "excess_kurtosis": 36.02249517434722,
        "return_acf_1": -0.24320084097828304,
        "abs_return_acf_1": 0.4907061047580616,
        "abs_return_acf_5": 0.4222190388265002,
        "abs_return_acf_20": 0.40257070989696986,
        "quantile_01": -0.07535831376969566,
        "quantile_99": 0.04910296824043431,
        "hill_tail_index": 1.828568318581405
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019242204196331016,
        "excess_kurtosis": 8.950562698956164,
        "return_acf_1": -0.07556275228145236,
        "abs_return_acf_1": 0.42602844078676116,
        "abs_return_acf_5": 0.3837001648418737,
        "abs_return_acf_20": 0.276811212557262,
        "quantile_01": -0.05988962479242263,
        "quantile_99": 0.05526636411903462,
        "hill_tail_index": 3.042620603180811
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019936021791128588,
        "excess_kurtosis": 25.887264052722827,
        "return_acf_1": -0.22695315494942278,
        "abs_return_acf_1": 0.4185108471279984,
        "abs_return_acf_5": 0.3065127068714023,
        "abs_return_acf_20": 0.2778224554000976,
        "quantile_01": -0.06555438608503825,
        "quantile_99": 0.04046534268338388,
        "hill_tail_index": 1.522052101490169
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021422133519185677,
        "excess_kurtosis": 15.26377628951149,
        "return_acf_1": -0.23779610670551826,
        "abs_return_acf_1": 0.3660110917010294,
        "abs_return_acf_5": 0.3166375253764759,
        "abs_return_acf_20": 0.28522386876021594,
        "quantile_01": -0.07188326083480223,
        "quantile_99": 0.0534115397813348,
        "hill_tail_index": 1.9620026912305573
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018367661350853267,
        "excess_kurtosis": 5.027283270965677,
        "return_acf_1": -0.12965411680682268,
        "abs_return_acf_1": 0.29146174247807477,
        "abs_return_acf_5": 0.2597935356413849,
        "abs_return_acf_20": 0.2901579374381306,
        "quantile_01": -0.05948030797469311,
        "quantile_99": 0.050110243550248935,
        "hill_tail_index": 3.3136893836358503
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01883831442650639,
        "excess_kurtosis": 4.4214728652132,
        "return_acf_1": -0.10735710308248107,
        "abs_return_acf_1": 0.319872530759287,
        "abs_return_acf_5": 0.30632841890976203,
        "abs_return_acf_20": 0.18601327151551722,
        "quantile_01": -0.05892082622796048,
        "quantile_99": 0.0520207508198178,
        "hill_tail_index": 3.990175903565289
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01904680568064945,
        "excess_kurtosis": 6.048753367764251,
        "return_acf_1": -0.16915916620804725,
        "abs_return_acf_1": 0.29821027062302147,
        "abs_return_acf_5": 0.3026980612218329,
        "abs_return_acf_20": 0.30254180714392614,
        "quantile_01": -0.057498043089342414,
        "quantile_99": 0.04849742324138939,
        "hill_tail_index": 2.8318285651990975
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.024315602730292565,
        "excess_kurtosis": 29.78247778690949,
        "return_acf_1": -0.20476921894512493,
        "abs_return_acf_1": 0.5067548026165529,
        "abs_return_acf_5": 0.4150896975307202,
        "abs_return_acf_20": 0.4049707427959416,
        "quantile_01": -0.08220507106243251,
        "quantile_99": 0.059014907280642785,
        "hill_tail_index": 1.958356131768436
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020710725494763705,
        "excess_kurtosis": 11.104500229880344,
        "return_acf_1": -0.18463357276724385,
        "abs_return_acf_1": 0.4237158725240782,
        "abs_return_acf_5": 0.319946328960399,
        "abs_return_acf_20": 0.3242941431394789,
        "quantile_01": -0.06685437134722753,
        "quantile_99": 0.05853274593043968,
        "hill_tail_index": 2.921369567639576
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022156500449890915,
        "excess_kurtosis": 15.452071283531897,
        "return_acf_1": -0.1363707970928097,
        "abs_return_acf_1": 0.45460939143830653,
        "abs_return_acf_5": 0.4444025877649667,
        "abs_return_acf_20": 0.3939009708409928,
        "quantile_01": -0.07763653696524359,
        "quantile_99": 0.057237977309480256,
        "hill_tail_index": 2.5983374525842104
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022718834906548878,
        "excess_kurtosis": 24.04461450225063,
        "return_acf_1": -0.15841743475656475,
        "abs_return_acf_1": 0.31379355489321425,
        "abs_return_acf_5": 0.26080448521873734,
        "abs_return_acf_20": 0.18637192176937742,
        "quantile_01": -0.06802108732400765,
        "quantile_99": 0.05376942354045751,
        "hill_tail_index": 2.0469174024992247
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020044522950449815,
        "excess_kurtosis": 20.1354117286543,
        "return_acf_1": -0.1326605327670881,
        "abs_return_acf_1": 0.36784162212910376,
        "abs_return_acf_5": 0.3386914680920268,
        "abs_return_acf_20": 0.3009227902013348,
        "quantile_01": -0.06573394939673653,
        "quantile_99": 0.05440147813778916,
        "hill_tail_index": 2.1000378042341263
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02438392385063303,
        "excess_kurtosis": 28.529415487735733,
        "return_acf_1": -0.24634811090565636,
        "abs_return_acf_1": 0.5127376162113825,
        "abs_return_acf_5": 0.4130613535564442,
        "abs_return_acf_20": 0.41093259677166993,
        "quantile_01": -0.06869958409969468,
        "quantile_99": 0.06806242676038139,
        "hill_tail_index": 2.133856207098625
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021970241824653278,
        "excess_kurtosis": 36.17629204576238,
        "return_acf_1": -0.21871846742849266,
        "abs_return_acf_1": 0.48413528551585006,
        "abs_return_acf_5": 0.44208914166299096,
        "abs_return_acf_20": 0.2868943171303535,
        "quantile_01": -0.07655989498991027,
        "quantile_99": 0.048255704162013746,
        "hill_tail_index": 1.6055899656943484
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.023215986935601132,
        "excess_kurtosis": 19.60476202086426,
        "return_acf_1": -0.1250430748544171,
        "abs_return_acf_1": 0.3929634644017449,
        "abs_return_acf_5": 0.40518476324320085,
        "abs_return_acf_20": 0.28266852264250836,
        "quantile_01": -0.07986239089862204,
        "quantile_99": 0.06093831266793058,
        "hill_tail_index": 2.0719524917706362
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02139241375819582,
        "excess_kurtosis": 26.389044667891156,
        "return_acf_1": -0.17077156158835954,
        "abs_return_acf_1": 0.42196334638380967,
        "abs_return_acf_5": 0.39867958781152724,
        "abs_return_acf_20": 0.2779468083560254,
        "quantile_01": -0.07155206534481046,
        "quantile_99": 0.058185284157551975,
        "hill_tail_index": 2.162059050332216
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023783588810276042,
        "excess_kurtosis": 29.77990993058981,
        "return_acf_1": -0.2333814574861343,
        "abs_return_acf_1": 0.5358134617244699,
        "abs_return_acf_5": 0.462683379961527,
        "abs_return_acf_20": 0.36614284272376374,
        "quantile_01": -0.08162478236761535,
        "quantile_99": 0.05153418452332503,
        "hill_tail_index": 1.6606978586669654
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021533277031621608,
        "excess_kurtosis": 28.11586557015084,
        "return_acf_1": -0.17519037557262487,
        "abs_return_acf_1": 0.45403785501086585,
        "abs_return_acf_5": 0.44988553909167694,
        "abs_return_acf_20": 0.3715687827541866,
        "quantile_01": -0.07624923208565125,
        "quantile_99": 0.046194885853150784,
        "hill_tail_index": 1.5240835771201187
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02331543543788716,
        "excess_kurtosis": 42.837203010538985,
        "return_acf_1": -0.2680223680185621,
        "abs_return_acf_1": 0.5110250738812511,
        "abs_return_acf_5": 0.4008589900065282,
        "abs_return_acf_20": 0.3321178386981297,
        "quantile_01": -0.07745928591379736,
        "quantile_99": 0.055088622028018945,
        "hill_tail_index": 1.6697912414474128
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01901084931198114,
        "excess_kurtosis": 6.3688623556053034,
        "return_acf_1": -0.09676535193260159,
        "abs_return_acf_1": 0.4258955893450057,
        "abs_return_acf_5": 0.3658086080249139,
        "abs_return_acf_20": 0.3084214952722157,
        "quantile_01": -0.0611959830895155,
        "quantile_99": 0.05324260973158988,
        "hill_tail_index": 3.105496779878741
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02038135215543421,
        "excess_kurtosis": 9.449228488216002,
        "return_acf_1": -0.10111417355120099,
        "abs_return_acf_1": 0.3273437759916756,
        "abs_return_acf_5": 0.37154447160604226,
        "abs_return_acf_20": 0.2878188692945367,
        "quantile_01": -0.05973582337557796,
        "quantile_99": 0.05677201363774702,
        "hill_tail_index": 3.739646917573999
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021650755202782323,
        "excess_kurtosis": 12.400039506023395,
        "return_acf_1": -0.05295726332328468,
        "abs_return_acf_1": 0.34590753747849456,
        "abs_return_acf_5": 0.3510512608428292,
        "abs_return_acf_20": 0.2551550921667482,
        "quantile_01": -0.06040014257766591,
        "quantile_99": 0.06705449289383346,
        "hill_tail_index": 2.320430815973273
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023080893340456352,
        "excess_kurtosis": 25.873935065257108,
        "return_acf_1": -0.14575670516879644,
        "abs_return_acf_1": 0.44286491439514053,
        "abs_return_acf_5": 0.30117279923876994,
        "abs_return_acf_20": 0.22804827119143145,
        "quantile_01": -0.08684488360224998,
        "quantile_99": 0.06546525952348772,
        "hill_tail_index": 2.2049502865557216
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01980388105649724,
        "excess_kurtosis": 34.84774163546715,
        "return_acf_1": -0.1729789964001934,
        "abs_return_acf_1": 0.3378605497676766,
        "abs_return_acf_5": 0.28301714859872673,
        "abs_return_acf_20": 0.224657179675139,
        "quantile_01": -0.059203829713425526,
        "quantile_99": 0.0411998753415534,
        "hill_tail_index": 1.5822070696915869
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019368064911562663,
        "excess_kurtosis": 18.61231081827366,
        "return_acf_1": -0.1760889535082918,
        "abs_return_acf_1": 0.36210644947020065,
        "abs_return_acf_5": 0.36316339671257564,
        "abs_return_acf_20": 0.24147001506774068,
        "quantile_01": -0.060676301763495595,
        "quantile_99": 0.05282240443142794,
        "hill_tail_index": 2.5375768705617507
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022198527611646302,
        "excess_kurtosis": 27.306523628405383,
        "return_acf_1": -0.18308878996767927,
        "abs_return_acf_1": 0.4459172580748015,
        "abs_return_acf_5": 0.35605269526912614,
        "abs_return_acf_20": 0.25466077676061427,
        "quantile_01": -0.07258032897100386,
        "quantile_99": 0.05034606012252864,
        "hill_tail_index": 1.8960493112335197
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015888873353825807,
        "excess_kurtosis": 3.3837734357132208,
        "return_acf_1": -0.16812210197731864,
        "abs_return_acf_1": 0.2773272653729185,
        "abs_return_acf_5": 0.3203141209032414,
        "abs_return_acf_20": 0.18052475176107474,
        "quantile_01": -0.045952426704697555,
        "quantile_99": 0.04455873372665603,
        "hill_tail_index": 4.151205734617529
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022855055965200117,
        "excess_kurtosis": 23.601524788585614,
        "return_acf_1": -0.11934675631983582,
        "abs_return_acf_1": 0.3716701287876011,
        "abs_return_acf_5": 0.3999467054501633,
        "abs_return_acf_20": 0.2583036776312118,
        "quantile_01": -0.09256619486684607,
        "quantile_99": 0.05627970453447199,
        "hill_tail_index": 1.7905315527174386
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017473729626678175,
        "excess_kurtosis": 2.65218831781387,
        "return_acf_1": -0.14682393937495714,
        "abs_return_acf_1": 0.2603281231374732,
        "abs_return_acf_5": 0.28133034989418493,
        "abs_return_acf_20": 0.16545797675223256,
        "quantile_01": -0.05358038721377794,
        "quantile_99": 0.044584114661213196,
        "hill_tail_index": 4.24411008865085
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02316010611168951,
        "excess_kurtosis": 30.358835001628883,
        "return_acf_1": -0.20815065489487963,
        "abs_return_acf_1": 0.5271042446717865,
        "abs_return_acf_5": 0.5180983894645954,
        "abs_return_acf_20": 0.2767435541599207,
        "quantile_01": -0.08327000038090074,
        "quantile_99": 0.05212660818157959,
        "hill_tail_index": 1.6276637452555203
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
