# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27082
Run ID: `3f118f725ad4bc8fc16c56f5a0594a9163e2a73c0fd72f3b691f77847a4e8eec`
Result fingerprint: `8a3643d1b58d70c761b165b359f83aec28ca8bd32e2b98d2db09c46e525e6951`

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
    "equal_weight_sd": -0.6087142857142825,
    "equal_weight_raw": -9.13071428571424,
    "fixed_start_cap_weight_sd": -0.6102495397569216,
    "fixed_start_cap_weight_raw": -9.153743096353825,
    "end_cap_weight_sd": -0.6266980970502902,
    "end_cap_weight_raw": -9.400471455754356
  },
  "full_period_change": {
    "equal_weight_sd": -0.8959047619047572,
    "equal_weight_raw": -13.438571428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8503597883597839,
    "inflation_mean_sd": 0.609281746031746
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.32970343346236747,
    "equal_weight_raw": 4.945551501935511,
    "fixed_start_cap_weight_sd": 0.3323882533820168,
    "fixed_start_cap_weight_raw": 4.985823800730252,
    "end_cap_weight_sd": 0.31962047970163265,
    "end_cap_weight_raw": 4.794307195524486
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5023809523809492,
      "change_raw": -7.535714285714238,
      "decay_adjusted_gain_sd": 0.45000000000000306
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7015476190476159,
      "change_raw": -10.523214285714237,
      "decay_adjusted_gain_sd": 0.2508333333333364
    },
    "small": {
      "count": 18,
      "change_sd": -0.580019841269838,
      "change_raw": -8.70029761904757,
      "decay_adjusted_gain_sd": 0.3490890557706102
    },
    "large_minus_small_sd": 0.07763888888888881,
    "large_minus_small_raw": 1.1645833333333322
  },
  "inflation": {
    "initial_mean_sd": 0.28750000000000003,
    "final_mean_sd": 0.6421666666666667,
    "mean_sd": 0.5013076602830975,
    "mean_absolute_raw_gap": 7.519614904246462,
    "final_absolute_raw_gap": 9.6325,
    "mean_range_fraction": 0.07519614904246462
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.36,
    "initial_wealth_share": 0.2787959405211252,
    "final_wealth_share": 0.386668914398802
  },
  "pricing_slope": {
    "mean": -0.0035469912570600184,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.12326145078686337,
    "real_improvement_cost": 0.10679491458136214,
    "washing_cost": 0.016466536205501224,
    "fine_transfer": 0.009677402400674192,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.13293885318753756,
    "resource_cost_fraction_initial_cap": 0.004108715026228779,
    "private_net_outflow_fraction_initial_cap": 0.004431295106251252,
    "fine_transfer_fraction_initial_cap": 0.00032258008002247307,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0004285228798333064,
    "unapplied_final_day_resource_cost": 0.00039383840735948743
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 80.24490171687295,
    "beneficial_raw_gain_per_resource_cost": 1203.6735257530943,
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
    "fixed_exposure": 15.0,
    "accrued_cost": 2.7586692485167683,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.21752122767370785,
    "accrued_cost_fraction_initial_cap": 0.09195564161722561,
    "mean_contract_rate": 0.03865901830959461,
    "maximum_ledger_error": 7.284483346386983e-20
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
    "price_cap_hits": 5,
    "maximum_relative_cash_error": 1.8448229871350143e-15,
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
      "minimum": -0.20637181555269785,
      "maximum": -0.057982592379070885,
      "mean": -0.11858918554606589,
      "median": -0.11235771550338725,
      "quantile_05": -0.17133665752706434,
      "quantile_95": -0.06565680304973816
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
      "minimum": 0.39034252421840454,
      "maximum": 0.771557912718878,
      "mean": 0.6167669810627423,
      "median": 0.6307702947971819,
      "quantile_05": 0.45471061783562366,
      "quantile_95": 0.7365972168247892
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
        "daily_volatility": 0.017414840767272333,
        "excess_kurtosis": 5.730323500474567,
        "return_acf_1": -0.14621003306327643,
        "abs_return_acf_1": 0.3124750122046215,
        "abs_return_acf_5": 0.3199154507964191,
        "abs_return_acf_20": 0.21640785328553733,
        "quantile_01": -0.05520609527146723,
        "quantile_99": 0.04532943157284211,
        "hill_tail_index": 3.1279370634388504
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01951421014023654,
        "excess_kurtosis": 8.538065741857723,
        "return_acf_1": -0.16219020865377523,
        "abs_return_acf_1": 0.40367982806653313,
        "abs_return_acf_5": 0.3890589630977989,
        "abs_return_acf_20": 0.2883383340740037,
        "quantile_01": -0.06062662103058926,
        "quantile_99": 0.05905407251658373,
        "hill_tail_index": 3.4997621049913192
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01469610025531907,
        "excess_kurtosis": 1.977278225826006,
        "return_acf_1": -0.09535040590744859,
        "abs_return_acf_1": 0.2597121822781242,
        "abs_return_acf_5": 0.2413653244046782,
        "abs_return_acf_20": 0.17809672995963918,
        "quantile_01": -0.040824599750369436,
        "quantile_99": 0.0422393154596291,
        "hill_tail_index": 5.541480955877363
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019673440283167802,
        "excess_kurtosis": 7.734727044543348,
        "return_acf_1": -0.09093745535430105,
        "abs_return_acf_1": 0.4207428191216899,
        "abs_return_acf_5": 0.39105761716541093,
        "abs_return_acf_20": 0.34333223189172696,
        "quantile_01": -0.06432259300315366,
        "quantile_99": 0.0548376533302258,
        "hill_tail_index": 3.26581224065498
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01898361841739375,
        "excess_kurtosis": 7.5978011998524995,
        "return_acf_1": -0.08433042095781272,
        "abs_return_acf_1": 0.2800465023936275,
        "abs_return_acf_5": 0.32908866132349623,
        "abs_return_acf_20": 0.2975030339334685,
        "quantile_01": -0.06302720402503358,
        "quantile_99": 0.053368489683109255,
        "hill_tail_index": 3.0703809522526617
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02159467222910692,
        "excess_kurtosis": 10.003166302745525,
        "return_acf_1": -0.09556806997066443,
        "abs_return_acf_1": 0.34879072597644956,
        "abs_return_acf_5": 0.403871563166732,
        "abs_return_acf_20": 0.3232143572995174,
        "quantile_01": -0.06732619480016348,
        "quantile_99": 0.0662023659285473,
        "hill_tail_index": 2.941921565465849
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018661309894527717,
        "excess_kurtosis": 7.00478129983423,
        "return_acf_1": -0.09769289740283398,
        "abs_return_acf_1": 0.30724123107013285,
        "abs_return_acf_5": 0.39915131192935227,
        "abs_return_acf_20": 0.26273919325759965,
        "quantile_01": -0.06623979304962763,
        "quantile_99": 0.05301112311069533,
        "hill_tail_index": 3.134992739741894
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020149537603277784,
        "excess_kurtosis": 7.078125443637605,
        "return_acf_1": -0.14652509674000452,
        "abs_return_acf_1": 0.40259723735442715,
        "abs_return_acf_5": 0.3614824973967862,
        "abs_return_acf_20": 0.3251990867935075,
        "quantile_01": -0.06253361208799725,
        "quantile_99": 0.05464351899209494,
        "hill_tail_index": 3.20130839769469
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020921267060696032,
        "excess_kurtosis": 10.432145328476762,
        "return_acf_1": -0.12217840583124585,
        "abs_return_acf_1": 0.3295014571794101,
        "abs_return_acf_5": 0.4084477466362641,
        "abs_return_acf_20": 0.30096175752738813,
        "quantile_01": -0.07734531744205254,
        "quantile_99": 0.05927539288699023,
        "hill_tail_index": 3.376073231860486
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019037145630025516,
        "excess_kurtosis": 6.283509056165974,
        "return_acf_1": -0.15869940489606427,
        "abs_return_acf_1": 0.38017229746488485,
        "abs_return_acf_5": 0.3856087764016892,
        "abs_return_acf_20": 0.30447614142116336,
        "quantile_01": -0.061610277275043784,
        "quantile_99": 0.050765054581788496,
        "hill_tail_index": 3.497268333559103
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017772613041350544,
        "excess_kurtosis": 4.411849091700927,
        "return_acf_1": -0.14712287130546353,
        "abs_return_acf_1": 0.3453080493996148,
        "abs_return_acf_5": 0.31290605782059416,
        "abs_return_acf_20": 0.2210841687017296,
        "quantile_01": -0.05701933181722914,
        "quantile_99": 0.04803750911197251,
        "hill_tail_index": 3.9599982384869525
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018258504935011147,
        "excess_kurtosis": 4.916515912409627,
        "return_acf_1": -0.11566837740121018,
        "abs_return_acf_1": 0.2906448091598821,
        "abs_return_acf_5": 0.3557672885893684,
        "abs_return_acf_20": 0.2246623996805064,
        "quantile_01": -0.05793336151956113,
        "quantile_99": 0.047503335705845834,
        "hill_tail_index": 3.4191342163788727
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01689619805953606,
        "excess_kurtosis": 3.8061153664946366,
        "return_acf_1": -0.20637181555269785,
        "abs_return_acf_1": 0.2804617300297683,
        "abs_return_acf_5": 0.2533212990739437,
        "abs_return_acf_20": 0.2628048828711561,
        "quantile_01": -0.05133678797538961,
        "quantile_99": 0.04728745990866255,
        "hill_tail_index": 4.393222370991775
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018374146082071077,
        "excess_kurtosis": 6.236384095329777,
        "return_acf_1": -0.1711104950547553,
        "abs_return_acf_1": 0.3734075941289303,
        "abs_return_acf_5": 0.38542142501989674,
        "abs_return_acf_20": 0.25781809376324333,
        "quantile_01": -0.0555146374506534,
        "quantile_99": 0.054965370045843044,
        "hill_tail_index": 3.9808231105106624
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01937353533010401,
        "excess_kurtosis": 7.012342144028549,
        "return_acf_1": -0.07349560069596646,
        "abs_return_acf_1": 0.3528698060264425,
        "abs_return_acf_5": 0.3863196254631868,
        "abs_return_acf_20": 0.27025919548184124,
        "quantile_01": -0.06598416180345454,
        "quantile_99": 0.052285821002917135,
        "hill_tail_index": 3.3968071613261173
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017681803505785833,
        "excess_kurtosis": 4.180280884533007,
        "return_acf_1": -0.06540553232879666,
        "abs_return_acf_1": 0.267721077918067,
        "abs_return_acf_5": 0.28005917466128666,
        "abs_return_acf_20": 0.2823355872256544,
        "quantile_01": -0.05342890677757871,
        "quantile_99": 0.04985631336362876,
        "hill_tail_index": 4.3226181524035265
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01886535855707106,
        "excess_kurtosis": 6.106528149338494,
        "return_acf_1": -0.12363604250081787,
        "abs_return_acf_1": 0.2831686935764776,
        "abs_return_acf_5": 0.30522190013653316,
        "abs_return_acf_20": 0.2527714762439459,
        "quantile_01": -0.057717586860538204,
        "quantile_99": 0.050662983799938034,
        "hill_tail_index": 2.8253043166495173
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019375201959286343,
        "excess_kurtosis": 7.643480907904589,
        "return_acf_1": -0.15246309147918127,
        "abs_return_acf_1": 0.3886954456563209,
        "abs_return_acf_5": 0.4047159191388567,
        "abs_return_acf_20": 0.3122962126574353,
        "quantile_01": -0.0629200433545314,
        "quantile_99": 0.055972443610590804,
        "hill_tail_index": 3.354466369133693
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018433971546472062,
        "excess_kurtosis": 7.63073061114418,
        "return_acf_1": -0.17152169954986263,
        "abs_return_acf_1": 0.32863664964692063,
        "abs_return_acf_5": 0.3509107119468224,
        "abs_return_acf_20": 0.23496428299425162,
        "quantile_01": -0.05184723912573293,
        "quantile_99": 0.0543052717373015,
        "hill_tail_index": 2.958601086700223
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019467821104876833,
        "excess_kurtosis": 9.123404878263242,
        "return_acf_1": -0.1269053937790256,
        "abs_return_acf_1": 0.4136362328500181,
        "abs_return_acf_5": 0.39172116000001983,
        "abs_return_acf_20": 0.293101934340999,
        "quantile_01": -0.06160829919255679,
        "quantile_99": 0.05114741001864042,
        "hill_tail_index": 2.7509887793877454
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019797664918169932,
        "excess_kurtosis": 7.053332659401196,
        "return_acf_1": -0.10769211539600658,
        "abs_return_acf_1": 0.3457410890326344,
        "abs_return_acf_5": 0.38133754376778556,
        "abs_return_acf_20": 0.2933969682109871,
        "quantile_01": -0.07144148300729092,
        "quantile_99": 0.05604589961634384,
        "hill_tail_index": 3.110889180119866
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019554588146292014,
        "excess_kurtosis": 5.9370934531553825,
        "return_acf_1": -0.11706685962038575,
        "abs_return_acf_1": 0.26389997642220375,
        "abs_return_acf_5": 0.3719752717640297,
        "abs_return_acf_20": 0.31683073388126204,
        "quantile_01": -0.06402249347717753,
        "quantile_99": 0.052106410576108604,
        "hill_tail_index": 4.503633510621167
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019894665307535697,
        "excess_kurtosis": 10.1826947154783,
        "return_acf_1": -0.09747818270976548,
        "abs_return_acf_1": 0.29878583220999855,
        "abs_return_acf_5": 0.3756847207538493,
        "abs_return_acf_20": 0.2853345895416758,
        "quantile_01": -0.07172659150717242,
        "quantile_99": 0.05722343162808625,
        "hill_tail_index": 2.992519499995911
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019774505848739944,
        "excess_kurtosis": 8.10527511824701,
        "return_acf_1": -0.10287443816899414,
        "abs_return_acf_1": 0.3314504206980418,
        "abs_return_acf_5": 0.39180592001586306,
        "abs_return_acf_20": 0.2922137988182166,
        "quantile_01": -0.06400676672555206,
        "quantile_99": 0.05248959685948329,
        "hill_tail_index": 3.043101956403899
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015382307100202507,
        "excess_kurtosis": 2.4879925625984534,
        "return_acf_1": -0.10904705360556431,
        "abs_return_acf_1": 0.20391235521691717,
        "abs_return_acf_5": 0.2153702328623967,
        "abs_return_acf_20": 0.13073399618250123,
        "quantile_01": -0.039604080850178434,
        "quantile_99": 0.0428002120113262,
        "hill_tail_index": 3.975465862312447
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018332096931676645,
        "excess_kurtosis": 6.499683307674179,
        "return_acf_1": -0.06596391170866665,
        "abs_return_acf_1": 0.2683589701459215,
        "abs_return_acf_5": 0.37695366054783963,
        "abs_return_acf_20": 0.20665400357697755,
        "quantile_01": -0.06224197488406669,
        "quantile_99": 0.04799468600550828,
        "hill_tail_index": 3.2160091298089952
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015791871015801033,
        "excess_kurtosis": 2.3425168041446263,
        "return_acf_1": -0.10258977998372885,
        "abs_return_acf_1": 0.2135062934132744,
        "abs_return_acf_5": 0.1865388302503565,
        "abs_return_acf_20": 0.16991065764909175,
        "quantile_01": -0.04514246942791923,
        "quantile_99": 0.03869717695137745,
        "hill_tail_index": 4.344452414039038
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019088965798190607,
        "excess_kurtosis": 7.139777291986684,
        "return_acf_1": -0.07959358555042159,
        "abs_return_acf_1": 0.39729401529756075,
        "abs_return_acf_5": 0.36168448125679004,
        "abs_return_acf_20": 0.2642348992991891,
        "quantile_01": -0.05870521168807559,
        "quantile_99": 0.054838630406609225,
        "hill_tail_index": 3.9742401333521107
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021340041628292953,
        "excess_kurtosis": 11.937204588823498,
        "return_acf_1": -0.057982592379070885,
        "abs_return_acf_1": 0.48206388453731847,
        "abs_return_acf_5": 0.4780671565895707,
        "abs_return_acf_20": 0.3228864564296857,
        "quantile_01": -0.07736366098039757,
        "quantile_99": 0.05701207587303197,
        "hill_tail_index": 2.6889800340917955
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01805327362882451,
        "excess_kurtosis": 5.173975905494977,
        "return_acf_1": -0.16400372883416825,
        "abs_return_acf_1": 0.31210439653119204,
        "abs_return_acf_5": 0.2628734699418572,
        "abs_return_acf_20": 0.2495656223773688,
        "quantile_01": -0.05315929834798469,
        "quantile_99": 0.04709962632741199,
        "hill_tail_index": 3.094187800801083
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
