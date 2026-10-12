# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27060
Run ID: `719025119745b199d524b288a95327985072f0f629c6fb6411cf1b0d16117dd3`
Result fingerprint: `6b4759fee7b1b28c89eb528b4f26f52afe1ec207206c5b95292be0f228f6fb6a`

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
    "equal_weight_sd": -0.5207976190476159,
    "equal_weight_raw": -7.811964285714239,
    "fixed_start_cap_weight_sd": -0.44054192276784265,
    "fixed_start_cap_weight_raw": -6.6081288415176385,
    "end_cap_weight_sd": -0.34368853723103343,
    "end_cap_weight_raw": -5.155328058465501
  },
  "full_period_change": {
    "equal_weight_sd": -0.8559047619047571,
    "equal_weight_raw": -12.838571428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8094632936507892,
    "inflation_mean_sd": 0.7249811507936507
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4315833333333365,
    "equal_weight_raw": 6.473750000000049,
    "fixed_start_cap_weight_sd": 0.5118390296131095,
    "fixed_start_cap_weight_raw": 7.677585444196641,
    "end_cap_weight_sd": 0.608692415149919,
    "end_cap_weight_raw": 9.130386227248785
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.037380952380949205,
      "change_raw": -0.5607142857142381,
      "decay_adjusted_gain_sd": 0.9150000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6143253968253937,
      "change_raw": -9.214880952380906,
      "decay_adjusted_gain_sd": 0.33805555555555866
    },
    "small": {
      "count": 18,
      "change_sd": -0.5546031746031714,
      "change_raw": -8.319047619047572,
      "decay_adjusted_gain_sd": 0.39777777777778095
    },
    "large_minus_small_sd": 0.5172222222222222,
    "large_minus_small_raw": 7.758333333333334
  },
  "inflation": {
    "initial_mean_sd": 0.2578333333333333,
    "final_mean_sd": 0.7534166666666666,
    "mean_sd": 0.544103594227033,
    "mean_absolute_raw_gap": 8.161553913405495,
    "final_absolute_raw_gap": 11.301250000000003,
    "mean_range_fraction": 0.08161553913405495
  },
  "impact": {
    "initial_share": 0.38,
    "final_share": 0.4066666666666667,
    "initial_wealth_share": 0.37869201386186885,
    "final_wealth_share": 0.4573123226071397
  },
  "pricing_slope": {
    "mean": -0.0004413349083379553,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.17789516157345572,
    "real_improvement_cost": 0.1542802447724263,
    "washing_cost": 0.023614916801029395,
    "fine_transfer": 0.0053230484272971165,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.18321821000075283,
    "resource_cost_fraction_initial_cap": 0.005929838719115189,
    "private_net_outflow_fraction_initial_cap": 0.00610727366669176,
    "fine_transfer_fraction_initial_cap": 0.0001774349475765705,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0035570930019966,
    "unapplied_final_day_resource_cost": 0.0035351177825656355
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 72.78163096444794,
    "beneficial_raw_gain_per_resource_cost": 1091.724464466719,
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
    "accrued_cost": 2.8790117525679513,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.09717872362252587,
    "accrued_cost_fraction_initial_cap": 0.09596705841893169,
    "mean_contract_rate": 0.03979583376057879,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 2.2011148480082437e-15,
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
      "minimum": -0.1980632453844512,
      "maximum": 0.018844626617245813,
      "mean": -0.12743108276528495,
      "median": -0.13901671791846504,
      "quantile_05": -0.19432033324697884,
      "quantile_95": -0.041772203187745126
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
      "minimum": 0.40928776767745245,
      "maximum": 0.820893430574385,
      "mean": 0.6347085524663829,
      "median": 0.6388469067454574,
      "quantile_05": 0.48535487682282547,
      "quantile_95": 0.7637280675244579
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
        "daily_volatility": 0.01683941208527187,
        "excess_kurtosis": 3.168384869855566,
        "return_acf_1": -0.1318123879467773,
        "abs_return_acf_1": 0.2333738995366918,
        "abs_return_acf_5": 0.2280504326897044,
        "abs_return_acf_20": 0.27432632876874347,
        "quantile_01": -0.04932831233468719,
        "quantile_99": 0.04886658035851147,
        "hill_tail_index": 4.054514920688241
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02055780603947499,
        "excess_kurtosis": 8.989431957953096,
        "return_acf_1": 0.018844626617245813,
        "abs_return_acf_1": 0.3860304954909485,
        "abs_return_acf_5": 0.32739732336307076,
        "abs_return_acf_20": 0.36597547017965776,
        "quantile_01": -0.06057750813070253,
        "quantile_99": 0.0698726292022413,
        "hill_tail_index": 3.9753352055989475
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022350186145367712,
        "excess_kurtosis": 12.302228240438241,
        "return_acf_1": -0.16581739219528752,
        "abs_return_acf_1": 0.48394462408485467,
        "abs_return_acf_5": 0.47602462018575553,
        "abs_return_acf_20": 0.3210357742843114,
        "quantile_01": -0.07128293978197736,
        "quantile_99": 0.06191126383510597,
        "hill_tail_index": 3.0636306572827627
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02091199647131391,
        "excess_kurtosis": 8.877865923078526,
        "return_acf_1": -0.15034008992166648,
        "abs_return_acf_1": 0.3746783339657536,
        "abs_return_acf_5": 0.4338804437345364,
        "abs_return_acf_20": 0.3956377643445142,
        "quantile_01": -0.06752638634714732,
        "quantile_99": 0.055617511934866366,
        "hill_tail_index": 3.5040589717362574
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020659685280349158,
        "excess_kurtosis": 13.284302831810052,
        "return_acf_1": -0.13306762679314404,
        "abs_return_acf_1": 0.40441750951204203,
        "abs_return_acf_5": 0.3629542627384498,
        "abs_return_acf_20": 0.31152449413591093,
        "quantile_01": -0.05257069920352026,
        "quantile_99": 0.05374816917634297,
        "hill_tail_index": 2.633028772195273
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019208142992993997,
        "excess_kurtosis": 6.917271940358839,
        "return_acf_1": -0.07720498500531316,
        "abs_return_acf_1": 0.32034853010303144,
        "abs_return_acf_5": 0.2969680054444662,
        "abs_return_acf_20": 0.2780813701078531,
        "quantile_01": -0.06289432850682129,
        "quantile_99": 0.046584734349716606,
        "hill_tail_index": 4.632972867099886
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020399604046382958,
        "excess_kurtosis": 10.873636076487696,
        "return_acf_1": -0.18531391865315192,
        "abs_return_acf_1": 0.424249299262626,
        "abs_return_acf_5": 0.3866813794641779,
        "abs_return_acf_20": 0.3157690786212765,
        "quantile_01": -0.06572723699715763,
        "quantile_99": 0.05944630390918145,
        "hill_tail_index": 3.303511491393337
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021557344918546252,
        "excess_kurtosis": 7.921799308457352,
        "return_acf_1": -0.19005567926880507,
        "abs_return_acf_1": 0.43693439517039967,
        "abs_return_acf_5": 0.4400601075449733,
        "abs_return_acf_20": 0.3837110906509902,
        "quantile_01": -0.07559066883487858,
        "quantile_99": 0.06025614233677472,
        "hill_tail_index": 3.0252218621254325
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01962150280478365,
        "excess_kurtosis": 6.654639260653495,
        "return_acf_1": -0.18846993212116145,
        "abs_return_acf_1": 0.32934777109921926,
        "abs_return_acf_5": 0.326590633090359,
        "abs_return_acf_20": 0.27736575422058624,
        "quantile_01": -0.07285773192615107,
        "quantile_99": 0.0453608664046602,
        "hill_tail_index": 3.3931222171427073
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016122689342318954,
        "excess_kurtosis": 4.320008083648143,
        "return_acf_1": -0.14176790463533334,
        "abs_return_acf_1": 0.28561485887864174,
        "abs_return_acf_5": 0.25185134092856304,
        "abs_return_acf_20": 0.23518850426496057,
        "quantile_01": -0.041197731268416936,
        "quantile_99": 0.04115909837268273,
        "hill_tail_index": 3.2004920227593954
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02073801973987975,
        "excess_kurtosis": 6.647690074644403,
        "return_acf_1": -0.16794766901047223,
        "abs_return_acf_1": 0.33718720036138466,
        "abs_return_acf_5": 0.32780723918897947,
        "abs_return_acf_20": 0.3639658223116601,
        "quantile_01": -0.07918395898987614,
        "quantile_99": 0.05314177040456705,
        "hill_tail_index": 3.1233892985146063
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021308933576515036,
        "excess_kurtosis": 8.553870598175086,
        "return_acf_1": -0.09047453895789008,
        "abs_return_acf_1": 0.4724197570603216,
        "abs_return_acf_5": 0.3830205201110689,
        "abs_return_acf_20": 0.4150021793441897,
        "quantile_01": -0.08031318130491467,
        "quantile_99": 0.061240210488418725,
        "hill_tail_index": 3.104005103138972
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02227867398975692,
        "excess_kurtosis": 9.420421397436348,
        "return_acf_1": -0.1414918462776403,
        "abs_return_acf_1": 0.48044778252524484,
        "abs_return_acf_5": 0.4469668984310715,
        "abs_return_acf_20": 0.4000865497177068,
        "quantile_01": -0.08722580366012694,
        "quantile_99": 0.06063916550534688,
        "hill_tail_index": 2.690361066929702
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020377776002735947,
        "excess_kurtosis": 4.944754617104442,
        "return_acf_1": -0.11128719501415034,
        "abs_return_acf_1": 0.3581843637564195,
        "abs_return_acf_5": 0.35264658464002346,
        "abs_return_acf_20": 0.3206153078806613,
        "quantile_01": -0.06630828310133162,
        "quantile_99": 0.05807090578146165,
        "hill_tail_index": 3.830703171346377
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.025039200996326005,
        "excess_kurtosis": 10.188355932472895,
        "return_acf_1": -0.19780959559275738,
        "abs_return_acf_1": 0.46585518637136863,
        "abs_return_acf_5": 0.4841093974595149,
        "abs_return_acf_20": 0.3915109325978313,
        "quantile_01": -0.09712288407273696,
        "quantile_99": 0.08230978208173986,
        "hill_tail_index": 3.4073936166227914
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020102807184067765,
        "excess_kurtosis": 8.1404049398122,
        "return_acf_1": -0.09942216804108465,
        "abs_return_acf_1": 0.435698278024654,
        "abs_return_acf_5": 0.3853643081241167,
        "abs_return_acf_20": 0.39272647885093875,
        "quantile_01": -0.057254831157490596,
        "quantile_99": 0.058765613624167705,
        "hill_tail_index": 3.005646262094504
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02064325617103498,
        "excess_kurtosis": 4.644130644142259,
        "return_acf_1": -0.15421187705481404,
        "abs_return_acf_1": 0.3816699061615928,
        "abs_return_acf_5": 0.34145335751653055,
        "abs_return_acf_20": 0.3542462816659175,
        "quantile_01": -0.06969827376470387,
        "quantile_99": 0.05911737012679775,
        "hill_tail_index": 5.656810313492953
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021412374567154766,
        "excess_kurtosis": 10.741347043852826,
        "return_acf_1": -0.08016123046995115,
        "abs_return_acf_1": 0.49823982982647197,
        "abs_return_acf_5": 0.46699959617636927,
        "abs_return_acf_20": 0.3058432930964934,
        "quantile_01": -0.07189423512184767,
        "quantile_99": 0.06155529032395072,
        "hill_tail_index": 2.9109528209332414
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020343818879643403,
        "excess_kurtosis": 6.703711711071602,
        "return_acf_1": -0.0831324724544826,
        "abs_return_acf_1": 0.4654396834202542,
        "abs_return_acf_5": 0.5081585732589781,
        "abs_return_acf_20": 0.34591004713245965,
        "quantile_01": -0.07597196822260553,
        "quantile_99": 0.05957350140743314,
        "hill_tail_index": 3.954291209751793
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01654929876257971,
        "excess_kurtosis": 9.848754103610764,
        "return_acf_1": -0.18522752614198143,
        "abs_return_acf_1": 0.31019533563612217,
        "abs_return_acf_5": 0.2879417925889876,
        "abs_return_acf_20": 0.3036575592763022,
        "quantile_01": -0.045160205303033336,
        "quantile_99": 0.03910608246646107,
        "hill_tail_index": 2.5914991671848004
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.024488766549709884,
        "excess_kurtosis": 10.621583386741843,
        "return_acf_1": -0.1365415895592898,
        "abs_return_acf_1": 0.41605169047431717,
        "abs_return_acf_5": 0.4843446976549056,
        "abs_return_acf_20": 0.39760764411496596,
        "quantile_01": -0.08046659647411362,
        "quantile_99": 0.06452769473780871,
        "hill_tail_index": 2.491814329485032
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02078389653793336,
        "excess_kurtosis": 5.282073759838658,
        "return_acf_1": -0.16728968333791774,
        "abs_return_acf_1": 0.38306502448407587,
        "abs_return_acf_5": 0.35633957967966734,
        "abs_return_acf_20": 0.34737387076340737,
        "quantile_01": -0.06962133365986527,
        "quantile_99": 0.05993191881312398,
        "hill_tail_index": 4.935641227131415
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01952343192915725,
        "excess_kurtosis": 7.683417754875563,
        "return_acf_1": -0.1980632453844512,
        "abs_return_acf_1": 0.3805633640572747,
        "abs_return_acf_5": 0.3416860434275412,
        "abs_return_acf_20": 0.30719796569520325,
        "quantile_01": -0.06425221847950924,
        "quantile_99": 0.05459854308385356,
        "hill_tail_index": 3.0249189613494183
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020779531541768363,
        "excess_kurtosis": 8.536723386553785,
        "return_acf_1": -0.10823898909065988,
        "abs_return_acf_1": 0.3415488901946974,
        "abs_return_acf_5": 0.33540439829810975,
        "abs_return_acf_20": 0.3557746620062374,
        "quantile_01": -0.0624266656001887,
        "quantile_99": 0.05413222130547451,
        "hill_tail_index": 2.5691389236768196
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020646145338086248,
        "excess_kurtosis": 9.487507030192969,
        "return_acf_1": -0.09721106290938093,
        "abs_return_acf_1": 0.36855932089342197,
        "abs_return_acf_5": 0.397874000864127,
        "abs_return_acf_20": 0.3287642619677387,
        "quantile_01": -0.06086160153338109,
        "quantile_99": 0.06605276823129516,
        "hill_tail_index": 3.292658342507146
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01884741486080597,
        "excess_kurtosis": 13.020681913091785,
        "return_acf_1": -0.08292763368714713,
        "abs_return_acf_1": 0.35764939342822955,
        "abs_return_acf_5": 0.3136274015408948,
        "abs_return_acf_20": 0.29700617579267324,
        "quantile_01": -0.05343974087369984,
        "quantile_99": 0.05607196893571485,
        "hill_tail_index": 2.7071441747924294
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01938353238942082,
        "excess_kurtosis": 4.703503611397538,
        "return_acf_1": -0.14383654356836145,
        "abs_return_acf_1": 0.35680065369438346,
        "abs_return_acf_5": 0.3471147161249529,
        "abs_return_acf_20": 0.2532689548448623,
        "quantile_01": -0.06584390815056868,
        "quantile_99": 0.05330919253759129,
        "hill_tail_index": 4.745064602895595
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02088911032587721,
        "excess_kurtosis": 9.513138487199473,
        "return_acf_1": -0.14795641639337384,
        "abs_return_acf_1": 0.43809165998276856,
        "abs_return_acf_5": 0.3275857035843268,
        "abs_return_acf_20": 0.2907703843992498,
        "quantile_01": -0.0703007970224492,
        "quantile_99": 0.06406281815376287,
        "hill_tail_index": 3.453382662846703
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018254989220986343,
        "excess_kurtosis": 6.720332957018259,
        "return_acf_1": -0.036590436475384035,
        "abs_return_acf_1": 0.35449549147450465,
        "abs_return_acf_5": 0.26383960479911606,
        "abs_return_acf_20": 0.2424478098988178,
        "quantile_01": -0.05097053202699843,
        "quantile_99": 0.05293514269237286,
        "hill_tail_index": 3.360364533424896
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021152915924308433,
        "excess_kurtosis": 7.783915106400835,
        "return_acf_1": -0.04810547361396417,
        "abs_return_acf_1": 0.39566628289129835,
        "abs_return_acf_5": 0.4206762995964017,
        "abs_return_acf_20": 0.3570300472118916,
        "quantile_01": -0.06714238085498563,
        "quantile_99": 0.06627195574645667,
        "hill_tail_index": 3.8829731656892084
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
