# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27050
Run ID: `849d030ab7aeb225cc8cccc26855e3202bef6c77ace467de81ecfb1631c3902c`
Result fingerprint: `dc5098669bfa317c520cf0de6e7295f975e278e49b0f62fead628c075083d037`

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
    "equal_weight_sd": -0.5790476190476158,
    "equal_weight_raw": -8.685714285714237,
    "fixed_start_cap_weight_sd": -0.5329528548188573,
    "fixed_start_cap_weight_raw": -7.994292822282859,
    "end_cap_weight_sd": -0.5458046727326444,
    "end_cap_weight_raw": -8.187070090989668
  },
  "full_period_change": {
    "equal_weight_sd": -0.8670714285714237,
    "equal_weight_raw": -13.006071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8198032407407364,
    "inflation_mean_sd": 0.6197142857142859
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3733333333333364,
    "equal_weight_raw": 5.600000000000046,
    "fixed_start_cap_weight_sd": 0.419428097562095,
    "fixed_start_cap_weight_raw": 6.291421463431425,
    "end_cap_weight_sd": 0.40657627964830795,
    "end_cap_weight_raw": 6.098644194724619
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.47321428571428265,
      "change_raw": -7.098214285714239,
      "decay_adjusted_gain_sd": 0.4791666666666697
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6840476190476159,
      "change_raw": -10.260714285714238,
      "decay_adjusted_gain_sd": 0.2683333333333364
    },
    "small": {
      "count": 18,
      "change_sd": -0.5441865079365047,
      "change_raw": -8.16279761904757,
      "decay_adjusted_gain_sd": 0.4081944444444475
    },
    "large_minus_small_sd": 0.07097222222222205,
    "large_minus_small_raw": 1.0645833333333308
  },
  "inflation": {
    "initial_mean_sd": 0.23875,
    "final_mean_sd": 0.6895833333333332,
    "mean_sd": 0.44985532889258956,
    "mean_absolute_raw_gap": 6.747829933388843,
    "final_absolute_raw_gap": 10.343749999999998,
    "mean_range_fraction": 0.06747829933388844
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.34,
    "initial_wealth_share": 0.2704099850490244,
    "final_wealth_share": 0.3599535382786764
  },
  "pricing_slope": {
    "mean": -0.004477581433248889,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.04200178285075466,
    "real_improvement_cost": 0.03265111390212877,
    "washing_cost": 0.009350668948625893,
    "fine_transfer": 0.01877040301276635,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06077218586352101,
    "resource_cost_fraction_initial_cap": 0.0014000594283584888,
    "private_net_outflow_fraction_initial_cap": 0.002025739528784034,
    "fine_transfer_fraction_initial_cap": 0.000625680100425545,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00189640168013613,
    "unapplied_final_day_resource_cost": 0.001720516971995117
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 266.6553474598247,
    "beneficial_raw_gain_per_resource_cost": 3999.8302118973706,
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
    "accrued_cost": 3.105490645014584,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.129300168824108,
    "accrued_cost_fraction_initial_cap": 0.10351635483381948,
    "mean_contract_rate": 0.043872794556399905,
    "maximum_ledger_error": 1.8973538018496328e-19
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
    "maximum_relative_cash_error": 3.1896868126877613e-15,
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
      "minimum": -0.18186550684603578,
      "maximum": -0.05576534977134048,
      "mean": -0.12281405867426197,
      "median": -0.12472585692197416,
      "quantile_05": -0.1757013081922322,
      "quantile_95": -0.06981803656240235
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
      "minimum": 0.2616792685066859,
      "maximum": 0.8080345961570964,
      "mean": 0.48419305080941105,
      "median": 0.44502694492448835,
      "quantile_05": 0.2984165544364215,
      "quantile_95": 0.743072303045835
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
        "daily_volatility": 0.022513743533717667,
        "excess_kurtosis": 24.282595587817443,
        "return_acf_1": -0.12805872717031178,
        "abs_return_acf_1": 0.4961033152119525,
        "abs_return_acf_5": 0.48008381352632606,
        "abs_return_acf_20": 0.29563587205161446,
        "quantile_01": -0.07966177534435197,
        "quantile_99": 0.06021125977351581,
        "hill_tail_index": 1.990151178975177
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022362537200864178,
        "excess_kurtosis": 12.33044590909479,
        "return_acf_1": -0.12565699475845152,
        "abs_return_acf_1": 0.4173351493749902,
        "abs_return_acf_5": 0.3847797020323951,
        "abs_return_acf_20": 0.3070880207535687,
        "quantile_01": -0.07789592776166965,
        "quantile_99": 0.06423654093632689,
        "hill_tail_index": 2.6950601178672016
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018432761536961613,
        "excess_kurtosis": 10.19283242979546,
        "return_acf_1": -0.12645909925024734,
        "abs_return_acf_1": 0.28111891770591746,
        "abs_return_acf_5": 0.2662621488665117,
        "abs_return_acf_20": 0.24980619481813335,
        "quantile_01": -0.05654586398538534,
        "quantile_99": 0.04381484660544565,
        "hill_tail_index": 2.556631710006349
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018177707158892883,
        "excess_kurtosis": 8.652409593407638,
        "return_acf_1": -0.08844712591266063,
        "abs_return_acf_1": 0.4041392231310512,
        "abs_return_acf_5": 0.2551358695458525,
        "abs_return_acf_20": 0.15282931231641933,
        "quantile_01": -0.06216740607826196,
        "quantile_99": 0.04766224131610096,
        "hill_tail_index": 2.4558060965684856
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01996727324140698,
        "excess_kurtosis": 10.408026559525615,
        "return_acf_1": -0.0897352736419097,
        "abs_return_acf_1": 0.45870601763958563,
        "abs_return_acf_5": 0.2695220510920197,
        "abs_return_acf_20": 0.2209776950794803,
        "quantile_01": -0.06184208101277549,
        "quantile_99": 0.0520622043378401,
        "hill_tail_index": 2.219381183648115
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016103638929519958,
        "excess_kurtosis": 12.391713261116884,
        "return_acf_1": -0.16322512739631218,
        "abs_return_acf_1": 0.37508824383365963,
        "abs_return_acf_5": 0.2930398440349291,
        "abs_return_acf_20": 0.20178647469561464,
        "quantile_01": -0.045937864039884965,
        "quantile_99": 0.03796974171901658,
        "hill_tail_index": 2.0621923600945657
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.015890556371588784,
        "excess_kurtosis": 13.243850149422077,
        "return_acf_1": -0.09185383844830788,
        "abs_return_acf_1": 0.2877020974707436,
        "abs_return_acf_5": 0.2027482532143689,
        "abs_return_acf_20": 0.1144581806029094,
        "quantile_01": -0.04206333261521702,
        "quantile_99": 0.038480146000658494,
        "hill_tail_index": 2.4949079004206176
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021799187008070302,
        "excess_kurtosis": 7.489995108223944,
        "return_acf_1": -0.08193664383181826,
        "abs_return_acf_1": 0.46092156148612845,
        "abs_return_acf_5": 0.46283703873858534,
        "abs_return_acf_20": 0.3193547326509844,
        "quantile_01": -0.07778804402445122,
        "quantile_99": 0.06323967305629527,
        "hill_tail_index": 3.082744092110113
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022731258683289127,
        "excess_kurtosis": 11.246439456307646,
        "return_acf_1": -0.10266424317893999,
        "abs_return_acf_1": 0.5336071378151466,
        "abs_return_acf_5": 0.5362334770094636,
        "abs_return_acf_20": 0.37662561247812454,
        "quantile_01": -0.07497909469342333,
        "quantile_99": 0.05992182073471267,
        "hill_tail_index": 2.717818198745557
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02143791620380069,
        "excess_kurtosis": 5.803102147907106,
        "return_acf_1": -0.15044175554227882,
        "abs_return_acf_1": 0.398420127607223,
        "abs_return_acf_5": 0.3234931215943508,
        "abs_return_acf_20": 0.27103700443988293,
        "quantile_01": -0.06824600608961628,
        "quantile_99": 0.0569210539851744,
        "hill_tail_index": 3.7850423933879576
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022052790873884218,
        "excess_kurtosis": 12.70192642425826,
        "return_acf_1": -0.17140043822384698,
        "abs_return_acf_1": 0.48308857636141816,
        "abs_return_acf_5": 0.4547928629237751,
        "abs_return_acf_20": 0.3515139164190284,
        "quantile_01": -0.06488596321369448,
        "quantile_99": 0.05925653054231973,
        "hill_tail_index": 2.3530796434316748
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017937126689166374,
        "excess_kurtosis": 13.113329497450696,
        "return_acf_1": -0.12926894704649644,
        "abs_return_acf_1": 0.36684324648878636,
        "abs_return_acf_5": 0.37289794417420397,
        "abs_return_acf_20": 0.27961180602037355,
        "quantile_01": -0.05288399496078112,
        "quantile_99": 0.046559762445700696,
        "hill_tail_index": 3.320819752328089
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019701533938861496,
        "excess_kurtosis": 6.979950780279411,
        "return_acf_1": -0.15687623475037793,
        "abs_return_acf_1": 0.42404075625792065,
        "abs_return_acf_5": 0.3585579604068736,
        "abs_return_acf_20": 0.261636173511929,
        "quantile_01": -0.05751008316302111,
        "quantile_99": 0.055294114779460765,
        "hill_tail_index": 2.9479917459454503
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.015396575878047618,
        "excess_kurtosis": 3.719884614924144,
        "return_acf_1": -0.1137856328523131,
        "abs_return_acf_1": 0.17139598494471223,
        "abs_return_acf_5": 0.24773470741389647,
        "abs_return_acf_20": 0.10610057135729335,
        "quantile_01": -0.038515681868302266,
        "quantile_99": 0.04117035608048677,
        "hill_tail_index": 3.2310181567947414
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021810964141547682,
        "excess_kurtosis": 11.951011576039267,
        "return_acf_1": -0.13332067432832032,
        "abs_return_acf_1": 0.4369542191744,
        "abs_return_acf_5": 0.4233080289654324,
        "abs_return_acf_20": 0.25934885715340883,
        "quantile_01": -0.07332629814131399,
        "quantile_99": 0.05965275440842624,
        "hill_tail_index": 2.844792442861168
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.015225933733927149,
        "excess_kurtosis": 10.062522127685192,
        "return_acf_1": -0.08876252525770684,
        "abs_return_acf_1": 0.21886446232295378,
        "abs_return_acf_5": 0.23483182497888064,
        "abs_return_acf_20": 0.1859872235937684,
        "quantile_01": -0.036524229878541585,
        "quantile_99": 0.038682239536425425,
        "hill_tail_index": 2.6943672476627416
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.024642222085389246,
        "excess_kurtosis": 14.981928831187936,
        "return_acf_1": -0.1792202018027292,
        "abs_return_acf_1": 0.4902271970489326,
        "abs_return_acf_5": 0.44956483189694474,
        "abs_return_acf_20": 0.3090159578807694,
        "quantile_01": -0.08236566558309925,
        "quantile_99": 0.07003901820150318,
        "hill_tail_index": 2.599137162390014
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02269653759356507,
        "excess_kurtosis": 11.627531376936973,
        "return_acf_1": -0.17068951106821997,
        "abs_return_acf_1": 0.47937284109578615,
        "abs_return_acf_5": 0.5158244176128821,
        "abs_return_acf_20": 0.34569466282168365,
        "quantile_01": -0.07454898210324631,
        "quantile_99": 0.05772367937370577,
        "hill_tail_index": 2.5322545183193177
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.024050223301420894,
        "excess_kurtosis": 11.189202620371862,
        "return_acf_1": -0.10329669834243631,
        "abs_return_acf_1": 0.4716813169206247,
        "abs_return_acf_5": 0.4920316735698208,
        "abs_return_acf_20": 0.34210851476134374,
        "quantile_01": -0.08098754113102272,
        "quantile_99": 0.07953121580247748,
        "hill_tail_index": 3.405556292559781
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01776210643613041,
        "excess_kurtosis": 6.02363453671585,
        "return_acf_1": -0.08034991627934301,
        "abs_return_acf_1": 0.3270826327724396,
        "abs_return_acf_5": 0.28101321966081483,
        "abs_return_acf_20": 0.1635712888280207,
        "quantile_01": -0.053349854126225164,
        "quantile_99": 0.04804139031290398,
        "hill_tail_index": 3.0226142554987723
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016333508584868,
        "excess_kurtosis": 11.19551042636542,
        "return_acf_1": -0.15487038446395424,
        "abs_return_acf_1": 0.27737934913513296,
        "abs_return_acf_5": 0.27906017676271744,
        "abs_return_acf_20": 0.14441804370315114,
        "quantile_01": -0.040605562054824886,
        "quantile_99": 0.03850837524694909,
        "hill_tail_index": 1.9743580245619414
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016141503163475183,
        "excess_kurtosis": 4.431142614686764,
        "return_acf_1": -0.11257830943289764,
        "abs_return_acf_1": 0.31802582405371305,
        "abs_return_acf_5": 0.26477224846993036,
        "abs_return_acf_20": 0.11722234008696282,
        "quantile_01": -0.03978223565361501,
        "quantile_99": 0.04175568305812447,
        "hill_tail_index": 3.167181323030536
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02162258958026544,
        "excess_kurtosis": 11.82661108281668,
        "return_acf_1": -0.18186550684603578,
        "abs_return_acf_1": 0.5235744054259853,
        "abs_return_acf_5": 0.45103922156670917,
        "abs_return_acf_20": 0.3276393052264929,
        "quantile_01": -0.07803272783361981,
        "quantile_99": 0.05280736519835661,
        "hill_tail_index": 2.341624522778868
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017914978122028757,
        "excess_kurtosis": 9.902248500923479,
        "return_acf_1": -0.12458455446646838,
        "abs_return_acf_1": 0.33654846676915073,
        "abs_return_acf_5": 0.19835847346393454,
        "abs_return_acf_20": 0.1902171765661701,
        "quantile_01": -0.050898189856697904,
        "quantile_99": 0.04298621576285106,
        "hill_tail_index": 2.106887962019359
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.025917234093524255,
        "excess_kurtosis": 14.683293944966305,
        "return_acf_1": -0.10743160415781748,
        "abs_return_acf_1": 0.5205649707093936,
        "abs_return_acf_5": 0.4887456915303552,
        "abs_return_acf_20": 0.3749070645295604,
        "quantile_01": -0.09426958671016912,
        "quantile_99": 0.07925255441166275,
        "hill_tail_index": 2.7960818971523387
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.014421815520450288,
        "excess_kurtosis": 2.8970183092553254,
        "return_acf_1": -0.05576534977134048,
        "abs_return_acf_1": 0.16222215666803008,
        "abs_return_acf_5": 0.14581671234424817,
        "abs_return_acf_20": 0.09154562592142841,
        "quantile_01": -0.03414297104081284,
        "quantile_99": 0.03803352133450649,
        "hill_tail_index": 4.109303147943022
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02298220524951846,
        "excess_kurtosis": 6.545552000077427,
        "return_acf_1": -0.16308553036165835,
        "abs_return_acf_1": 0.4674964994533384,
        "abs_return_acf_5": 0.3763333839048076,
        "abs_return_acf_20": 0.36103590217536846,
        "quantile_01": -0.07490466773875386,
        "quantile_99": 0.06760565888773429,
        "hill_tail_index": 3.737493400733093
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016216096518933014,
        "excess_kurtosis": 3.537926540259777,
        "return_acf_1": -0.12272270820045508,
        "abs_return_acf_1": 0.2133761355453555,
        "abs_return_acf_5": 0.21733408508774127,
        "abs_return_acf_20": 0.17462382070573257,
        "quantile_01": -0.04293941913839047,
        "quantile_99": 0.04753924108736724,
        "hill_tail_index": 4.370611120032312
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022362293655812635,
        "excess_kurtosis": 17.208319865830543,
        "return_acf_1": -0.12486715937747994,
        "abs_return_acf_1": 0.4873551936921114,
        "abs_return_acf_5": 0.4762110319366976,
        "abs_return_acf_20": 0.330327594652986,
        "quantile_01": -0.06750931062868021,
        "quantile_99": 0.06512010689576075,
        "hill_tail_index": 2.297625605888434
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019852296356121513,
        "excess_kurtosis": 9.035142533293458,
        "return_acf_1": -0.06120104406672351,
        "abs_return_acf_1": 0.3721968235418525,
        "abs_return_acf_5": 0.34727501894167156,
        "abs_return_acf_20": 0.21695732746893648,
        "quantile_01": -0.06387003804902752,
        "quantile_99": 0.05036850381384459,
        "hill_tail_index": 2.795375172455739
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
