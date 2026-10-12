# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720111
Run ID: `3ad64e611ef967e4141d01625bfde9ac41dad02da9438de72b74e9a7536b10bd`
Result fingerprint: `d572a70ee22a7943c30d26d5ede19edbffd1dac87ffd2ea0c1077463d136c0e5`

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
    "equal_weight_sd": -0.8396349206349176,
    "equal_weight_raw": -12.594523809523764,
    "fixed_start_cap_weight_sd": -0.8854087377325898,
    "fixed_start_cap_weight_raw": -13.281131065988847,
    "end_cap_weight_sd": -0.8918531656968421,
    "end_cap_weight_raw": -13.377797485452636
  },
  "full_period_change": {
    "equal_weight_sd": -1.3005622421729681,
    "equal_weight_raw": -19.50843363259452
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2191014313054116,
    "inflation_mean_sd": 0.18922189153439153
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.08100000000000301,
    "equal_weight_raw": 1.2150000000000452,
    "fixed_start_cap_weight_sd": 0.05808258333952259,
    "fixed_start_cap_weight_raw": 0.8712387500928389,
    "end_cap_weight_sd": 0.055604424852194106,
    "end_cap_weight_raw": 0.8340663727829116
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.952380952380949,
      "change_raw": -14.285714285714235,
      "decay_adjusted_gain_sd": 3.2566542055671257e-15
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8284920634920606,
      "change_raw": -12.42738095238091,
      "decay_adjusted_gain_sd": 0.12388888888889173
    },
    "small": {
      "count": 18,
      "change_sd": -0.8264153439153409,
      "change_raw": -12.396230158730113,
      "decay_adjusted_gain_sd": 0.07305555555555861
    },
    "large_minus_small_sd": -0.12596560846560811,
    "large_minus_small_raw": -1.8894841269841218
  },
  "inflation": {
    "initial_mean_sd": 0.11166666666666666,
    "final_mean_sd": 0.19491666666666674,
    "mean_sd": 0.15527053844018873,
    "mean_absolute_raw_gap": 2.329058076602831,
    "final_absolute_raw_gap": 2.923749999999999,
    "mean_range_fraction": 0.023290580766028312
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.3333333333333333,
    "initial_wealth_share": 0.4073306951285049,
    "final_wealth_share": 0.4143195323506442
  },
  "pricing_slope": {
    "mean": -0.002054019508265832,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.0014133496070169152,
    "real_improvement_cost": 0.0004262522436159589,
    "washing_cost": 0.0009870973634009562,
    "fine_transfer": 0.003247468300099878,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.004660817907116793,
    "resource_cost_fraction_initial_cap": 4.711165356723052e-05,
    "private_net_outflow_fraction_initial_cap": 0.00015536059690389315,
    "fine_transfer_fraction_initial_cap": 0.00010824894333666262,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00023971841988634562,
    "unapplied_final_day_resource_cost": 4.068454951442821e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 1719.3198257075028,
    "beneficial_raw_gain_per_resource_cost": 25789.797385612543,
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
    "accrued_cost": 3.049222731835102,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.07303225564462604,
    "accrued_cost_fraction_initial_cap": 0.10164075772783676,
    "mean_contract_rate": 0.0426144885540465,
    "maximum_ledger_error": 1.3552527156068805e-19
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
    "maximum_relative_cash_error": 1.2550001824304925e-15,
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
      "minimum": -0.2621084041015419,
      "maximum": -0.08765389713405418,
      "mean": -0.16404394554943455,
      "median": -0.16485868682256985,
      "quantile_05": -0.22033186217643014,
      "quantile_95": -0.10042815512753984
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
      "minimum": 0.43772673480878066,
      "maximum": 0.8030000318567871,
      "mean": 0.6399620744298846,
      "median": 0.6427454609203848,
      "quantile_05": 0.5167474587037458,
      "quantile_95": 0.7421597405359284
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
        "daily_volatility": 0.021833023725932994,
        "excess_kurtosis": 15.508651432222305,
        "return_acf_1": -0.2621084041015419,
        "abs_return_acf_1": 0.4069413680867025,
        "abs_return_acf_5": 0.4441049027666059,
        "abs_return_acf_20": 0.2557633461251723,
        "quantile_01": -0.06998206617035574,
        "quantile_99": 0.055280200111443675,
        "hill_tail_index": 2.3305662397457234
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018870821759673907,
        "excess_kurtosis": 11.318779623852075,
        "return_acf_1": -0.16201036322795972,
        "abs_return_acf_1": 0.31591487736748314,
        "abs_return_acf_5": 0.38075047757424035,
        "abs_return_acf_20": 0.24027217434209666,
        "quantile_01": -0.06289802497650673,
        "quantile_99": 0.04388994842891114,
        "hill_tail_index": 2.3623362775047876
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021480441903060345,
        "excess_kurtosis": 3.104158458445304,
        "return_acf_1": -0.1541152237008248,
        "abs_return_acf_1": 0.32673751316546873,
        "abs_return_acf_5": 0.3038347823175698,
        "abs_return_acf_20": 0.31520638075789625,
        "quantile_01": -0.06548600855526972,
        "quantile_99": 0.06572237719768345,
        "hill_tail_index": 4.03909161186977
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019535426955625025,
        "excess_kurtosis": 4.233790970500579,
        "return_acf_1": -0.18600263177824536,
        "abs_return_acf_1": 0.25158028429769796,
        "abs_return_acf_5": 0.27851899943828495,
        "abs_return_acf_20": 0.147673065359615,
        "quantile_01": -0.06677265928783038,
        "quantile_99": 0.05037710369358116,
        "hill_tail_index": 3.942427455298813
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02094270838763757,
        "excess_kurtosis": 11.836529869143414,
        "return_acf_1": -0.10147377703835637,
        "abs_return_acf_1": 0.2894089076700822,
        "abs_return_acf_5": 0.332992515956742,
        "abs_return_acf_20": 0.2383601676948283,
        "quantile_01": -0.07512376708817596,
        "quantile_99": 0.054340864508181166,
        "hill_tail_index": 2.4764194941210103
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02105161754327869,
        "excess_kurtosis": 8.449425020650109,
        "return_acf_1": -0.21354952444064365,
        "abs_return_acf_1": 0.2796840057071439,
        "abs_return_acf_5": 0.29159111136813226,
        "abs_return_acf_20": 0.21824708446615318,
        "quantile_01": -0.06824762871413306,
        "quantile_99": 0.05044215927164916,
        "hill_tail_index": 3.0299806673741063
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01859202982821257,
        "excess_kurtosis": 5.5892233726229,
        "return_acf_1": -0.21340585971817363,
        "abs_return_acf_1": 0.24083708237680457,
        "abs_return_acf_5": 0.23255619671566513,
        "abs_return_acf_20": 0.15305185111206873,
        "quantile_01": -0.05877169070675258,
        "quantile_99": 0.05525344092014458,
        "hill_tail_index": 4.025529265879987
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01882810105127466,
        "excess_kurtosis": 4.692776896587269,
        "return_acf_1": -0.19240119366892885,
        "abs_return_acf_1": 0.3115356148728509,
        "abs_return_acf_5": 0.3049922197905382,
        "abs_return_acf_20": 0.21319574780975448,
        "quantile_01": -0.06009037770666336,
        "quantile_99": 0.05187750874642458,
        "hill_tail_index": 3.7942022460628397
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020492217447446094,
        "excess_kurtosis": 12.499477917211692,
        "return_acf_1": -0.2258810475966191,
        "abs_return_acf_1": 0.3449973637153096,
        "abs_return_acf_5": 0.35950159642791346,
        "abs_return_acf_20": 0.2761605561781637,
        "quantile_01": -0.06649386519002111,
        "quantile_99": 0.05186392266947962,
        "hill_tail_index": 2.1756969940418234
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019601205239709638,
        "excess_kurtosis": 4.11506135362955,
        "return_acf_1": -0.1945626907588491,
        "abs_return_acf_1": 0.27116137618078867,
        "abs_return_acf_5": 0.30707592924145516,
        "abs_return_acf_20": 0.23505105243143762,
        "quantile_01": -0.06425696002407479,
        "quantile_99": 0.05797819079875582,
        "hill_tail_index": 4.871432386362408
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021639152811358107,
        "excess_kurtosis": 16.903905214964784,
        "return_acf_1": -0.20060967547792236,
        "abs_return_acf_1": 0.2652118334824417,
        "abs_return_acf_5": 0.36445632938909495,
        "abs_return_acf_20": 0.24615231053793485,
        "quantile_01": -0.07549991271346093,
        "quantile_99": 0.04488556498976742,
        "hill_tail_index": 2.5740613911711163
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02047015500588005,
        "excess_kurtosis": 3.7661707021813875,
        "return_acf_1": -0.1721689889529997,
        "abs_return_acf_1": 0.2977030873397282,
        "abs_return_acf_5": 0.28899968967602646,
        "abs_return_acf_20": 0.21731590341197343,
        "quantile_01": -0.05899249123084687,
        "quantile_99": 0.057105093689896726,
        "hill_tail_index": 4.624263441159139
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020121679149740765,
        "excess_kurtosis": 13.019386964575084,
        "return_acf_1": -0.18429235874874156,
        "abs_return_acf_1": 0.2888804023431442,
        "abs_return_acf_5": 0.32932112064504393,
        "abs_return_acf_20": 0.18139063253321214,
        "quantile_01": -0.06773095098665734,
        "quantile_99": 0.050105381682325326,
        "hill_tail_index": 3.0311945351898606
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02054088587515822,
        "excess_kurtosis": 4.0438982197059525,
        "return_acf_1": -0.15800423487817,
        "abs_return_acf_1": 0.29462005596947843,
        "abs_return_acf_5": 0.2543966020105654,
        "abs_return_acf_20": 0.25368958848649165,
        "quantile_01": -0.06361072550643775,
        "quantile_99": 0.055266507359355004,
        "hill_tail_index": 5.250775526611815
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021673376273854045,
        "excess_kurtosis": 4.261642259527835,
        "return_acf_1": -0.1831294955659015,
        "abs_return_acf_1": 0.40827015529239064,
        "abs_return_acf_5": 0.39846110825555375,
        "abs_return_acf_20": 0.32161334291864835,
        "quantile_01": -0.06904094627898659,
        "quantile_99": 0.06315988769569954,
        "hill_tail_index": 4.286403501466393
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019452853230519904,
        "excess_kurtosis": 5.0247765304912235,
        "return_acf_1": -0.08765389713405418,
        "abs_return_acf_1": 0.3383124485958356,
        "abs_return_acf_5": 0.31904839746322905,
        "abs_return_acf_20": 0.22935578928416817,
        "quantile_01": -0.07416705909232085,
        "quantile_99": 0.05551080450227074,
        "hill_tail_index": 3.6306685960332192
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019278799678826647,
        "excess_kurtosis": 6.7633252752627175,
        "return_acf_1": -0.1274502421623688,
        "abs_return_acf_1": 0.3099940846805227,
        "abs_return_acf_5": 0.29922653132417704,
        "abs_return_acf_20": 0.25154857735256964,
        "quantile_01": -0.05949620462485514,
        "quantile_99": 0.054846330996469794,
        "hill_tail_index": 3.3399733923862573
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02011193071354065,
        "excess_kurtosis": 5.752527289058783,
        "return_acf_1": -0.12216480482363887,
        "abs_return_acf_1": 0.33618356830821244,
        "abs_return_acf_5": 0.23564119207735357,
        "abs_return_acf_20": 0.21716274429485857,
        "quantile_01": -0.07073555622089339,
        "quantile_99": 0.058643496961413945,
        "hill_tail_index": 3.8052112863678786
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019942494224962012,
        "excess_kurtosis": 3.455240094341928,
        "return_acf_1": -0.18203036148678972,
        "abs_return_acf_1": 0.3056522052412819,
        "abs_return_acf_5": 0.32800028116418234,
        "abs_return_acf_20": 0.25949207259531887,
        "quantile_01": -0.05947060968116137,
        "quantile_99": 0.05225284016784598,
        "hill_tail_index": 4.156607383211556
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01942152760784664,
        "excess_kurtosis": 7.756639461432117,
        "return_acf_1": -0.09957264629141722,
        "abs_return_acf_1": 0.32930550570695827,
        "abs_return_acf_5": 0.3481954362365955,
        "abs_return_acf_20": 0.2333056419922061,
        "quantile_01": -0.07222799547434261,
        "quantile_99": 0.05117210679617133,
        "hill_tail_index": 2.578598544125016
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020089047053531883,
        "excess_kurtosis": 8.173414575985115,
        "return_acf_1": -0.12384592607653219,
        "abs_return_acf_1": 0.38591627216887453,
        "abs_return_acf_5": 0.2944124607462612,
        "abs_return_acf_20": 0.2608426195007901,
        "quantile_01": -0.06612751527484179,
        "quantile_99": 0.058438339123385905,
        "hill_tail_index": 3.227302697337762
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02104000661666359,
        "excess_kurtosis": 4.934237228654277,
        "return_acf_1": -0.1566795653472537,
        "abs_return_acf_1": 0.35076301334970256,
        "abs_return_acf_5": 0.2960825882782678,
        "abs_return_acf_20": 0.2579125696905637,
        "quantile_01": -0.07120303108202074,
        "quantile_99": 0.055437030141461695,
        "hill_tail_index": 3.970158877925692
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02133395027525677,
        "excess_kurtosis": 3.449760519956322,
        "return_acf_1": -0.1444771854201863,
        "abs_return_acf_1": 0.29327563542953405,
        "abs_return_acf_5": 0.29038409015403993,
        "abs_return_acf_20": 0.22946568440565598,
        "quantile_01": -0.06742511604428489,
        "quantile_99": 0.06527824733476327,
        "hill_tail_index": 5.7566177533499285
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02134513219470994,
        "excess_kurtosis": 4.133478252720032,
        "return_acf_1": -0.15472258773299793,
        "abs_return_acf_1": 0.3392665698220804,
        "abs_return_acf_5": 0.3354664636673362,
        "abs_return_acf_20": 0.24521813098248205,
        "quantile_01": -0.06598636194325616,
        "quantile_99": 0.0620504857148638,
        "hill_tail_index": 4.609669017259303
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02106659675553775,
        "excess_kurtosis": 6.453469730145576,
        "return_acf_1": -0.1766470531167326,
        "abs_return_acf_1": 0.3374278836788203,
        "abs_return_acf_5": 0.33585365267891515,
        "abs_return_acf_20": 0.21929140680135198,
        "quantile_01": -0.0696275878358803,
        "quantile_99": 0.06272158796253631,
        "hill_tail_index": 4.2561574956766135
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019838034802455703,
        "excess_kurtosis": 7.244121994658947,
        "return_acf_1": -0.10505042738621967,
        "abs_return_acf_1": 0.3886851882277605,
        "abs_return_acf_5": 0.40569057065122793,
        "abs_return_acf_20": 0.260565378189198,
        "quantile_01": -0.07167770662189415,
        "quantile_99": 0.04976084652092316,
        "hill_tail_index": 3.3768752935997726
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01885684855609488,
        "excess_kurtosis": 5.103348228951514,
        "return_acf_1": -0.16770701041717997,
        "abs_return_acf_1": 0.31633841222378956,
        "abs_return_acf_5": 0.3076174016558051,
        "abs_return_acf_20": 0.231638429039081,
        "quantile_01": -0.06287553043245027,
        "quantile_99": 0.04844808822541556,
        "hill_tail_index": 3.8050398529777736
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02070230260814556,
        "excess_kurtosis": 3.7201290848521955,
        "return_acf_1": -0.1319491262468637,
        "abs_return_acf_1": 0.3506953633328254,
        "abs_return_acf_5": 0.36546737021289627,
        "abs_return_acf_20": 0.2573780499239359,
        "quantile_01": -0.06315348525914398,
        "quantile_99": 0.05890298320227693,
        "hill_tail_index": 4.863817168524647
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02143957921308627,
        "excess_kurtosis": 4.698533682051946,
        "return_acf_1": -0.15607032130715276,
        "abs_return_acf_1": 0.3248470540596843,
        "abs_return_acf_5": 0.3074676286736082,
        "abs_return_acf_20": 0.3141906073909476,
        "quantile_01": -0.06616540676898391,
        "quantile_99": 0.05749918927931658,
        "hill_tail_index": 3.9333345701939533
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02188935462378044,
        "excess_kurtosis": 4.412173984419395,
        "return_acf_1": -0.1815817418797718,
        "abs_return_acf_1": 0.30127145301768266,
        "abs_return_acf_5": 0.29531296668845586,
        "abs_return_acf_20": 0.2698702728032593,
        "quantile_01": -0.07247372867456713,
        "quantile_99": 0.06216634758685354,
        "hill_tail_index": 5.059959148267604
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
Training: False
Coverage status: FAIL
Unseen state share: 0.07888888888888888
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
