# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27137
Run ID: `e5b6525cb781ff899deb1e31e476b45884681337a928945ab492ba9819c81944`
Result fingerprint: `100eeaa69e541080acc83800467f95e8ee39fa997e2d24fa37ddb204fc44025d`

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
    "equal_weight_sd": -0.6573417731226392,
    "equal_weight_raw": -9.86012659683959,
    "fixed_start_cap_weight_sd": -0.6206365697991832,
    "fixed_start_cap_weight_raw": -9.309548546987745,
    "end_cap_weight_sd": -0.6105646265276783,
    "end_cap_weight_raw": -9.158469397915171
  },
  "full_period_change": {
    "equal_weight_sd": -1.024365582646447,
    "equal_weight_raw": -15.365483739696707
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9632880999656678,
    "inflation_mean_sd": 0.5748627645502645
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.28783333333333644,
    "equal_weight_raw": 4.317500000000048,
    "fixed_start_cap_weight_sd": 0.32067928290821185,
    "fixed_start_cap_weight_raw": 4.810189243623177,
    "end_cap_weight_sd": 0.3369288976979429,
    "end_cap_weight_raw": 5.053933465469142
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.46654761904761566,
      "change_raw": -6.998214285714235,
      "decay_adjusted_gain_sd": 0.4858333333333367
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6833614659643609,
      "change_raw": -10.250421989465414,
      "decay_adjusted_gain_sd": 0.24500000000000288
    },
    "small": {
      "count": 18,
      "change_sd": -0.6761309523809491,
      "change_raw": -10.141964285714236,
      "decay_adjusted_gain_sd": 0.27625000000000327
    },
    "large_minus_small_sd": 0.20958333333333345,
    "large_minus_small_raw": 3.1437500000000016
  },
  "inflation": {
    "initial_mean_sd": 0.2956666666666667,
    "final_mean_sd": 0.6131666666666666,
    "mean_sd": 0.4673298640022204,
    "mean_absolute_raw_gap": 7.009947960033306,
    "final_absolute_raw_gap": 9.197499999999998,
    "mean_range_fraction": 0.07009947960033305
  },
  "impact": {
    "initial_share": 0.44666666666666666,
    "final_share": 0.47333333333333333,
    "initial_wealth_share": 0.5180965176502268,
    "final_wealth_share": 0.5129532416504031
  },
  "pricing_slope": {
    "mean": 0.00022644220456808321,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.08003891770910196,
    "real_improvement_cost": 0.07224643215293981,
    "washing_cost": 0.0077924855561621416,
    "fine_transfer": 0.00863231770034017,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08867123540944213,
    "resource_cost_fraction_initial_cap": 0.0026679639236367315,
    "private_net_outflow_fraction_initial_cap": 0.002955707846981404,
    "fine_transfer_fraction_initial_cap": 0.0002877439233446723,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003764312190668352,
    "unapplied_final_day_resource_cost": 0.0010446769938732036
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 107.88501702863643,
    "beneficial_raw_gain_per_resource_cost": 1618.2752554295462,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 3.000049054461678,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.02385857827120075,
    "accrued_cost_fraction_initial_cap": 0.10000163514872258,
    "mean_contract_rate": 0.0415710123014784,
    "maximum_ledger_error": 9.147955830346444e-20
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
    "maximum_relative_cash_error": 1.6139115096731656e-15,
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
      "minimum": -0.2733858230031961,
      "maximum": -0.09796980299284376,
      "mean": -0.17686147398370625,
      "median": -0.17409914841593982,
      "quantile_05": -0.25915662810072526,
      "quantile_95": -0.10995519594000691
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
      "minimum": 0.08819066094644423,
      "maximum": 0.8565566879765953,
      "mean": 0.5080458853775708,
      "median": 0.5599115657735816,
      "quantile_05": 0.1522617020592408,
      "quantile_95": 0.8146652984005301
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
        "daily_volatility": 0.026290190153852245,
        "excess_kurtosis": 8.990501688172897,
        "return_acf_1": -0.1757820393329225,
        "abs_return_acf_1": 0.43090459212436105,
        "abs_return_acf_5": 0.43189954389662283,
        "abs_return_acf_20": 0.3674150358086065,
        "quantile_01": -0.09144928918163167,
        "quantile_99": 0.07575735290014422,
        "hill_tail_index": 2.840375663118871
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02812793520784258,
        "excess_kurtosis": 14.451699061242543,
        "return_acf_1": -0.26320288364124184,
        "abs_return_acf_1": 0.49845928644553944,
        "abs_return_acf_5": 0.4375463781728608,
        "abs_return_acf_20": 0.4121721187802922,
        "quantile_01": -0.09791228971912778,
        "quantile_99": 0.0867399834439692,
        "hill_tail_index": 2.9992693884881843
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.028379215640723446,
        "excess_kurtosis": 17.81866386945281,
        "return_acf_1": -0.2088890144125954,
        "abs_return_acf_1": 0.47651980777870706,
        "abs_return_acf_5": 0.42312168997747884,
        "abs_return_acf_20": 0.38957282025677875,
        "quantile_01": -0.11501947353049173,
        "quantile_99": 0.07362354480058333,
        "hill_tail_index": 2.5875945427627514
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018453828345857105,
        "excess_kurtosis": 3.466592358931055,
        "return_acf_1": -0.11988204461703911,
        "abs_return_acf_1": 0.2691241152549622,
        "abs_return_acf_5": 0.23581185414835146,
        "abs_return_acf_20": 0.23142452129365812,
        "quantile_01": -0.05166714688642999,
        "quantile_99": 0.05544001150726632,
        "hill_tail_index": 4.792504329350514
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018292765848027706,
        "excess_kurtosis": 2.653001279814011,
        "return_acf_1": -0.10224897965694041,
        "abs_return_acf_1": 0.20775322094575702,
        "abs_return_acf_5": 0.20063779432284296,
        "abs_return_acf_20": 0.21350582050693248,
        "quantile_01": -0.050826556728747516,
        "quantile_99": 0.0538369207665509,
        "hill_tail_index": 4.728228885508298
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02900836755042195,
        "excess_kurtosis": 17.0821855492066,
        "return_acf_1": -0.2733858230031961,
        "abs_return_acf_1": 0.5085066936085767,
        "abs_return_acf_5": 0.35199671558988327,
        "abs_return_acf_20": 0.39669130376410594,
        "quantile_01": -0.10649443262188045,
        "quantile_99": 0.08421425668824795,
        "hill_tail_index": 2.794740740121445
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02454526586760594,
        "excess_kurtosis": 11.935627419515438,
        "return_acf_1": -0.12260714150874737,
        "abs_return_acf_1": 0.5040230960615986,
        "abs_return_acf_5": 0.4842914206206398,
        "abs_return_acf_20": 0.4004682845889661,
        "quantile_01": -0.0863945901200468,
        "quantile_99": 0.06861165820510264,
        "hill_tail_index": 3.307833331501263
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020997904142861228,
        "excess_kurtosis": 28.773258412879876,
        "return_acf_1": -0.18875202740684485,
        "abs_return_acf_1": 0.36957551915703296,
        "abs_return_acf_5": 0.3427319866896193,
        "abs_return_acf_20": 0.3102445775800605,
        "quantile_01": -0.07552786496806307,
        "quantile_99": 0.04989324602830676,
        "hill_tail_index": 1.887384807290586
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.026700900860930868,
        "excess_kurtosis": 21.575505643149135,
        "return_acf_1": -0.17241625749895717,
        "abs_return_acf_1": 0.47620942234716085,
        "abs_return_acf_5": 0.3353281526456782,
        "abs_return_acf_20": 0.30321479898654236,
        "quantile_01": -0.08670381819416624,
        "quantile_99": 0.07288929764642006,
        "hill_tail_index": 2.3892959183169213
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021621452002795957,
        "excess_kurtosis": 22.72016766566789,
        "return_acf_1": -0.14678246514724486,
        "abs_return_acf_1": 0.34285909813443327,
        "abs_return_acf_5": 0.31092902524032434,
        "abs_return_acf_20": 0.26775829088094627,
        "quantile_01": -0.05938201367104279,
        "quantile_99": 0.05070004105350894,
        "hill_tail_index": 2.173670882677399
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021921902333119126,
        "excess_kurtosis": 10.176915191482575,
        "return_acf_1": -0.16190876934951923,
        "abs_return_acf_1": 0.4522290258067646,
        "abs_return_acf_5": 0.4017312677312696,
        "abs_return_acf_20": 0.3315174969277091,
        "quantile_01": -0.07568269199245435,
        "quantile_99": 0.06731366734242379,
        "hill_tail_index": 3.4091111576502318
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02185209201100042,
        "excess_kurtosis": 28.677839779297337,
        "return_acf_1": -0.15362853555163858,
        "abs_return_acf_1": 0.40277780198314816,
        "abs_return_acf_5": 0.38356650093661415,
        "abs_return_acf_20": 0.35095667573106354,
        "quantile_01": -0.0696523096480438,
        "quantile_99": 0.05137693379155484,
        "hill_tail_index": 1.7808491328305944
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.027195567858300265,
        "excess_kurtosis": 14.27347732026394,
        "return_acf_1": -0.2049435744452785,
        "abs_return_acf_1": 0.5162816342468681,
        "abs_return_acf_5": 0.42171159649762396,
        "abs_return_acf_20": 0.36859386357876606,
        "quantile_01": -0.0982945327523606,
        "quantile_99": 0.08116180184835446,
        "hill_tail_index": 2.8139574545060735
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02537365827246439,
        "excess_kurtosis": 11.029513705669114,
        "return_acf_1": -0.2225522407146969,
        "abs_return_acf_1": 0.4977734647106181,
        "abs_return_acf_5": 0.47507253527721127,
        "abs_return_acf_20": 0.3338579378988016,
        "quantile_01": -0.08974597698757676,
        "quantile_99": 0.07258129243444005,
        "hill_tail_index": 2.9157559460286597
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02558171784748179,
        "excess_kurtosis": 13.341162082285862,
        "return_acf_1": -0.18498685839137644,
        "abs_return_acf_1": 0.4640190554585578,
        "abs_return_acf_5": 0.3880542318596298,
        "abs_return_acf_20": 0.3303122527089279,
        "quantile_01": -0.09552737789982339,
        "quantile_99": 0.06618502384512616,
        "hill_tail_index": 2.503934328031771
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023919516305356915,
        "excess_kurtosis": 12.552985342818173,
        "return_acf_1": -0.15146935051932456,
        "abs_return_acf_1": 0.4817772275405777,
        "abs_return_acf_5": 0.3426832629049828,
        "abs_return_acf_20": 0.30327889814798203,
        "quantile_01": -0.08197137284594122,
        "quantile_99": 0.07066958130390764,
        "hill_tail_index": 2.8947581806161424
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.025905048631024503,
        "excess_kurtosis": 22.53681262119119,
        "return_acf_1": -0.1659141783225285,
        "abs_return_acf_1": 0.5355348786580121,
        "abs_return_acf_5": 0.48555924528969324,
        "abs_return_acf_20": 0.29205396675282236,
        "quantile_01": -0.09063534211317664,
        "quantile_99": 0.06702819578814215,
        "hill_tail_index": 2.0558781118464435
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017712088307106178,
        "excess_kurtosis": 5.6911931040815436,
        "return_acf_1": -0.09796980299284376,
        "abs_return_acf_1": 0.2393778765697785,
        "abs_return_acf_5": 0.2378339369751664,
        "abs_return_acf_20": 0.2983162480540679,
        "quantile_01": -0.053956398847313146,
        "quantile_99": 0.05248730623650616,
        "hill_tail_index": 3.059344865228375
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02673809460894784,
        "excess_kurtosis": 13.98157986867782,
        "return_acf_1": -0.1885775228652554,
        "abs_return_acf_1": 0.4706482037051755,
        "abs_return_acf_5": 0.4313278872380317,
        "abs_return_acf_20": 0.2910696229378011,
        "quantile_01": -0.10934619862326869,
        "quantile_99": 0.08152427496786253,
        "hill_tail_index": 2.911211819835734
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0204032943239441,
        "excess_kurtosis": 6.971386097460563,
        "return_acf_1": -0.13670768688813945,
        "abs_return_acf_1": 0.3710436052130121,
        "abs_return_acf_5": 0.3363046671670581,
        "abs_return_acf_20": 0.30773806547707666,
        "quantile_01": -0.06419962495257553,
        "quantile_99": 0.05992415319170463,
        "hill_tail_index": 4.001325386038388
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02223759858561357,
        "excess_kurtosis": 31.518051796047814,
        "return_acf_1": -0.2121662124086182,
        "abs_return_acf_1": 0.502864998567255,
        "abs_return_acf_5": 0.4709995777030869,
        "abs_return_acf_20": 0.38917141785440734,
        "quantile_01": -0.07386894444621482,
        "quantile_99": 0.05186450858197604,
        "hill_tail_index": 2.181519079009309
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.025621277107112272,
        "excess_kurtosis": 11.531395635671528,
        "return_acf_1": -0.20217025545663586,
        "abs_return_acf_1": 0.43316183554101545,
        "abs_return_acf_5": 0.3495436310797011,
        "abs_return_acf_20": 0.32193816186205143,
        "quantile_01": -0.08818755093557322,
        "quantile_99": 0.07059892668282979,
        "hill_tail_index": 2.4389041610093063
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017945387823284944,
        "excess_kurtosis": 3.0426272463835184,
        "return_acf_1": -0.15328462272069912,
        "abs_return_acf_1": 0.17643040935260887,
        "abs_return_acf_5": 0.14448795389832916,
        "abs_return_acf_20": 0.1960882293800995,
        "quantile_01": -0.05059486809253133,
        "quantile_99": 0.0518745039375275,
        "hill_tail_index": 4.2947519418330256
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018840143191508292,
        "excess_kurtosis": 5.346319473032089,
        "return_acf_1": -0.11937390473042142,
        "abs_return_acf_1": 0.2975990225806348,
        "abs_return_acf_5": 0.3080664689620432,
        "abs_return_acf_20": 0.24325898975864355,
        "quantile_01": -0.05822867268885935,
        "quantile_99": 0.05387070185226691,
        "hill_tail_index": 2.856123367002218
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017296519387131365,
        "excess_kurtosis": 2.427150734002254,
        "return_acf_1": -0.1616767680522322,
        "abs_return_acf_1": 0.2423307673902843,
        "abs_return_acf_5": 0.26269932561066106,
        "abs_return_acf_20": 0.22197895717792548,
        "quantile_01": -0.053327271289003955,
        "quantile_99": 0.04554643704486564,
        "hill_tail_index": 4.676742201646497
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02283706543098179,
        "excess_kurtosis": 4.231991403190132,
        "return_acf_1": -0.16233432736020817,
        "abs_return_acf_1": 0.2905516139512323,
        "abs_return_acf_5": 0.2864499569954959,
        "abs_return_acf_20": 0.24548251646138142,
        "quantile_01": -0.07257323035829313,
        "quantile_99": 0.06099331159086008,
        "hill_tail_index": 4.30044257184001
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025748083586490184,
        "excess_kurtosis": 12.307807192829335,
        "return_acf_1": -0.17718183214463407,
        "abs_return_acf_1": 0.4521217958653447,
        "abs_return_acf_5": 0.3815942441270431,
        "abs_return_acf_20": 0.36452533056428926,
        "quantile_01": -0.09945293213536825,
        "quantile_99": 0.06905472367016692,
        "hill_tail_index": 2.8582047239505397
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.024874699152282152,
        "excess_kurtosis": 11.778932586165771,
        "return_acf_1": -0.17691684693947646,
        "abs_return_acf_1": 0.4923524138520056,
        "abs_return_acf_5": 0.3747255218418096,
        "abs_return_acf_20": 0.36318398900836935,
        "quantile_01": -0.0861225488477866,
        "quantile_99": 0.07180500278041735,
        "hill_tail_index": 3.09381136098353
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02633851268884555,
        "excess_kurtosis": 12.444849688436316,
        "return_acf_1": -0.25421120466231606,
        "abs_return_acf_1": 0.5115922635235782,
        "abs_return_acf_5": 0.3925336553522853,
        "abs_return_acf_20": 0.35272555314225673,
        "quantile_01": -0.09594771260616278,
        "quantile_99": 0.08480235711327601,
        "hill_tail_index": 2.944024129541185
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.026051074216043083,
        "excess_kurtosis": 12.863550695698065,
        "return_acf_1": -0.24392104876961518,
        "abs_return_acf_1": 0.45159780822275647,
        "abs_return_acf_5": 0.3464580267222217,
        "abs_return_acf_20": 0.3166313630985335,
        "quantile_01": -0.09453301500944879,
        "quantile_99": 0.07858682775610075,
        "hill_tail_index": 2.6636992050973975
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
