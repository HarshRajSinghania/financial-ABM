# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27142
Run ID: `b8c899283e5ff37618fc189ef886a4f7db4826f7b606290b58c2f1525f266a4f`
Result fingerprint: `442b945f6c8c09ee14f6b07f1ce81a41d27dd78e4962edf17e4b5779cfda2898`

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
    "equal_weight_sd": -0.7454078425261685,
    "equal_weight_raw": -11.181117637892532,
    "fixed_start_cap_weight_sd": -0.718100403518495,
    "fixed_start_cap_weight_raw": -10.77150605277743,
    "end_cap_weight_sd": -0.7088213451501922,
    "end_cap_weight_raw": -10.632320177252883
  },
  "full_period_change": {
    "equal_weight_sd": -1.1390983187166432,
    "equal_weight_raw": -17.086474780749647
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0770866659073717,
    "inflation_mean_sd": 0.6638121693121694
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19100000000000308,
    "equal_weight_raw": 2.8650000000000455,
    "fixed_start_cap_weight_sd": 0.20922750351338987,
    "fixed_start_cap_weight_raw": 3.1384125527008484,
    "end_cap_weight_sd": 0.22355779469148454,
    "end_cap_weight_raw": 3.3533669203722685
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.744047619047616,
      "change_raw": -11.160714285714239,
      "decay_adjusted_gain_sd": 0.20833333333333648
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6624705861983475,
      "change_raw": -9.937058792975213,
      "decay_adjusted_gain_sd": 0.2366666666666694
    },
    "small": {
      "count": 18,
      "change_sd": -0.7871031746031714,
      "change_raw": -11.80654761904757,
      "decay_adjusted_gain_sd": 0.16527777777778097
    },
    "large_minus_small_sd": 0.0430555555555554,
    "large_minus_small_raw": 0.645833333333331
  },
  "inflation": {
    "initial_mean_sd": 0.35783333333333345,
    "final_mean_sd": 0.6974166666666669,
    "mean_sd": 0.55075,
    "mean_absolute_raw_gap": 8.26125,
    "final_absolute_raw_gap": 10.46125,
    "mean_range_fraction": 0.0826125
  },
  "impact": {
    "initial_share": 0.19333333333333333,
    "final_share": 0.26,
    "initial_wealth_share": 0.21028163642701556,
    "final_wealth_share": 0.2562310014472065
  },
  "pricing_slope": {
    "mean": -0.0009073910899179066,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.04690265923845746,
    "real_improvement_cost": 0.04010943698493176,
    "washing_cost": 0.006793222253525706,
    "fine_transfer": 0.004138715001481044,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05104137423993851,
    "resource_cost_fraction_initial_cap": 0.0015634219746152485,
    "private_net_outflow_fraction_initial_cap": 0.0017013791413312833,
    "fine_transfer_fraction_initial_cap": 0.00013795716671603477,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002669748409388461,
    "unapplied_final_day_resource_cost": 0.0029261839087980183
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 122.16791314258414,
    "beneficial_raw_gain_per_resource_cost": 1832.5186971387623,
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
    "accrued_cost": 3.236543095768641,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.2603526195781644,
    "accrued_cost_fraction_initial_cap": 0.10788476985895469,
    "mean_contract_rate": 0.04521645359161006,
    "maximum_ledger_error": 7.115076756936123e-20
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
    "price_cap_hits": 12,
    "maximum_relative_cash_error": 2.226340636564453e-15,
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
      "minimum": -0.29019770993190436,
      "maximum": -0.06542695792537093,
      "mean": -0.1963567721319848,
      "median": -0.19240304848679302,
      "quantile_05": -0.2713077641906252,
      "quantile_95": -0.12273137152780755
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
      "minimum": 0.4367201171296631,
      "maximum": 0.8465492778788849,
      "mean": 0.6877268752345966,
      "median": 0.7080288789005439,
      "quantile_05": 0.48904078955961183,
      "quantile_95": 0.8250809058200612
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
        "daily_volatility": 0.02442615048239622,
        "excess_kurtosis": 12.431008670585324,
        "return_acf_1": -0.16651984171577883,
        "abs_return_acf_1": 0.5199098178024668,
        "abs_return_acf_5": 0.54816794512359,
        "abs_return_acf_20": 0.3154265417100251,
        "quantile_01": -0.09483695114630826,
        "quantile_99": 0.06917966789825229,
        "hill_tail_index": 3.11853964362618
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.026303633780385884,
        "excess_kurtosis": 25.640028647786373,
        "return_acf_1": -0.29019770993190436,
        "abs_return_acf_1": 0.4591348596396731,
        "abs_return_acf_5": 0.5147540943520229,
        "abs_return_acf_20": 0.27670036995036085,
        "quantile_01": -0.08984883757653818,
        "quantile_99": 0.06977175321363402,
        "hill_tail_index": 1.949713152160843
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021698947365019764,
        "excess_kurtosis": 13.188466700144478,
        "return_acf_1": -0.06542695792537093,
        "abs_return_acf_1": 0.4631515115511694,
        "abs_return_acf_5": 0.5113876247549495,
        "abs_return_acf_20": 0.34663908135355637,
        "quantile_01": -0.0749021394358624,
        "quantile_99": 0.07176533553617331,
        "hill_tail_index": 2.6166971581836105
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.025460960745253655,
        "excess_kurtosis": 21.16771170796658,
        "return_acf_1": -0.23365893671937157,
        "abs_return_acf_1": 0.4637594290075602,
        "abs_return_acf_5": 0.5182337568843355,
        "abs_return_acf_20": 0.2976427282071615,
        "quantile_01": -0.08844857269325519,
        "quantile_99": 0.07798665451808606,
        "hill_tail_index": 2.7324058742709916
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02547588683862933,
        "excess_kurtosis": 19.608269269752572,
        "return_acf_1": -0.18987242668856089,
        "abs_return_acf_1": 0.44035878330548894,
        "abs_return_acf_5": 0.5055363006098532,
        "abs_return_acf_20": 0.2785359166289086,
        "quantile_01": -0.08690046271721857,
        "quantile_99": 0.07192102210916304,
        "hill_tail_index": 2.361995977632043
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023472293038091608,
        "excess_kurtosis": 14.791051614692368,
        "return_acf_1": -0.15626934741034434,
        "abs_return_acf_1": 0.3959705831645934,
        "abs_return_acf_5": 0.4676492934433231,
        "abs_return_acf_20": 0.34160626992689386,
        "quantile_01": -0.0932099447237763,
        "quantile_99": 0.0679991201367832,
        "hill_tail_index": 2.8142858115238494
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020631486528054487,
        "excess_kurtosis": 10.56337884485191,
        "return_acf_1": -0.11213607458466207,
        "abs_return_acf_1": 0.3992554879210107,
        "abs_return_acf_5": 0.47273280174190924,
        "abs_return_acf_20": 0.23657486172111752,
        "quantile_01": -0.0728970550790944,
        "quantile_99": 0.06070640817191681,
        "hill_tail_index": 3.091066927693222
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.025579650591252053,
        "excess_kurtosis": 20.675099908006185,
        "return_acf_1": -0.16369946573480862,
        "abs_return_acf_1": 0.47392301882079707,
        "abs_return_acf_5": 0.515291399145925,
        "abs_return_acf_20": 0.27160151020602946,
        "quantile_01": -0.10191216141302609,
        "quantile_99": 0.06361817773394472,
        "hill_tail_index": 2.1705711525332725
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0273143231173092,
        "excess_kurtosis": 19.525467248652507,
        "return_acf_1": -0.22424075480043745,
        "abs_return_acf_1": 0.470412960718439,
        "abs_return_acf_5": 0.47482376104658824,
        "abs_return_acf_20": 0.2894734892459622,
        "quantile_01": -0.10383007505597174,
        "quantile_99": 0.0767138570789291,
        "hill_tail_index": 2.4413790765891235
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022640004833173914,
        "excess_kurtosis": 18.067826327815755,
        "return_acf_1": -0.21749464771428595,
        "abs_return_acf_1": 0.42565908518350093,
        "abs_return_acf_5": 0.4841072901578989,
        "abs_return_acf_20": 0.2264705575111062,
        "quantile_01": -0.07850493335094061,
        "quantile_99": 0.058020459336314945,
        "hill_tail_index": 2.351771241281227
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02389661307461348,
        "excess_kurtosis": 25.062235067474262,
        "return_acf_1": -0.1852930919784742,
        "abs_return_acf_1": 0.4204320975902068,
        "abs_return_acf_5": 0.5079090183233934,
        "abs_return_acf_20": 0.25217793013667456,
        "quantile_01": -0.08843936646284484,
        "quantile_99": 0.06725894625805867,
        "hill_tail_index": 2.1960253373125678
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02732564185458843,
        "excess_kurtosis": 20.886330376992554,
        "return_acf_1": -0.19047463181767707,
        "abs_return_acf_1": 0.4743310372370182,
        "abs_return_acf_5": 0.4405616173528636,
        "abs_return_acf_20": 0.28200673316095254,
        "quantile_01": -0.10322378499944594,
        "quantile_99": 0.0733025121099938,
        "hill_tail_index": 2.09981615156967
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02626868955024028,
        "excess_kurtosis": 19.942995732390482,
        "return_acf_1": -0.1911460581908915,
        "abs_return_acf_1": 0.5097083379162461,
        "abs_return_acf_5": 0.5345055897296528,
        "abs_return_acf_20": 0.2974775740813418,
        "quantile_01": -0.0920277668662912,
        "quantile_99": 0.06776939026033649,
        "hill_tail_index": 2.687667404944569
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.026528409701090445,
        "excess_kurtosis": 18.038651696587042,
        "return_acf_1": -0.14230690703347548,
        "abs_return_acf_1": 0.48419687186795685,
        "abs_return_acf_5": 0.5598387794610554,
        "abs_return_acf_20": 0.3120531889772164,
        "quantile_01": -0.0977111288584563,
        "quantile_99": 0.07981904507613923,
        "hill_tail_index": 2.2515128657190933
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02676330425100405,
        "excess_kurtosis": 19.106260336333335,
        "return_acf_1": -0.19366003878269453,
        "abs_return_acf_1": 0.4578781261397453,
        "abs_return_acf_5": 0.49452775017890344,
        "abs_return_acf_20": 0.3326481738643678,
        "quantile_01": -0.10058554541206617,
        "quantile_99": 0.07201932272251346,
        "hill_tail_index": 2.198592251504438
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023913338055123395,
        "excess_kurtosis": 29.908821872828476,
        "return_acf_1": -0.27879413428708993,
        "abs_return_acf_1": 0.47871008626711586,
        "abs_return_acf_5": 0.5337135417329519,
        "abs_return_acf_20": 0.3009049054497584,
        "quantile_01": -0.07596542365426326,
        "quantile_99": 0.05477392811571803,
        "hill_tail_index": 2.2025244398481227
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.027402227283220056,
        "excess_kurtosis": 23.62355303916501,
        "return_acf_1": -0.24785082743229467,
        "abs_return_acf_1": 0.5164187093857598,
        "abs_return_acf_5": 0.512586183694895,
        "abs_return_acf_20": 0.26160113312014655,
        "quantile_01": -0.08790995355922088,
        "quantile_99": 0.07210207800192336,
        "hill_tail_index": 2.0175393207686896
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021853854745592365,
        "excess_kurtosis": 31.056317877155188,
        "return_acf_1": -0.2557443928543537,
        "abs_return_acf_1": 0.4055472157214978,
        "abs_return_acf_5": 0.4764648982049251,
        "abs_return_acf_20": 0.21545991296292386,
        "quantile_01": -0.07214244815869097,
        "quantile_99": 0.05022330467804436,
        "hill_tail_index": 1.7634275812736069
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01969622029307039,
        "excess_kurtosis": 13.51173343949792,
        "return_acf_1": -0.1683447632840989,
        "abs_return_acf_1": 0.4062651764063172,
        "abs_return_acf_5": 0.4787712736964831,
        "abs_return_acf_20": 0.25151764352239864,
        "quantile_01": -0.057519715881649044,
        "quantile_99": 0.049875823746733466,
        "hill_tail_index": 2.310594765002853
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02493952424527738,
        "excess_kurtosis": 21.341990230201304,
        "return_acf_1": -0.1868795468770309,
        "abs_return_acf_1": 0.4268774079744935,
        "abs_return_acf_5": 0.4497282997630441,
        "abs_return_acf_20": 0.23336168298589435,
        "quantile_01": -0.09395252878267936,
        "quantile_99": 0.06884534384781497,
        "hill_tail_index": 2.512050256360354
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022891876675284816,
        "excess_kurtosis": 22.819402461853368,
        "return_acf_1": -0.2052194147196441,
        "abs_return_acf_1": 0.4367831329703611,
        "abs_return_acf_5": 0.49636304141446874,
        "abs_return_acf_20": 0.23951949401346775,
        "quantile_01": -0.0696480284084486,
        "quantile_99": 0.0632382050031366,
        "hill_tail_index": 2.1444262618998806
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024470709022499128,
        "excess_kurtosis": 27.745367149291397,
        "return_acf_1": -0.26215775629494603,
        "abs_return_acf_1": 0.4174943271518357,
        "abs_return_acf_5": 0.42431953245775433,
        "abs_return_acf_20": 0.22135615054149607,
        "quantile_01": -0.08708327210317084,
        "quantile_99": 0.05078228443127153,
        "hill_tail_index": 2.176996953232895
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.026353348752749906,
        "excess_kurtosis": 23.125885599293973,
        "return_acf_1": -0.20525175088834127,
        "abs_return_acf_1": 0.5004045086038917,
        "abs_return_acf_5": 0.5156066151436054,
        "abs_return_acf_20": 0.2909632879615161,
        "quantile_01": -0.09579814300013523,
        "quantile_99": 0.07135161490993315,
        "hill_tail_index": 2.4544521208597363
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02358500756067703,
        "excess_kurtosis": 13.046913722774889,
        "return_acf_1": -0.17840240129240037,
        "abs_return_acf_1": 0.37231544832596286,
        "abs_return_acf_5": 0.38400279469632026,
        "abs_return_acf_20": 0.2569262397412433,
        "quantile_01": -0.07974253168917397,
        "quantile_99": 0.06675461547845198,
        "hill_tail_index": 3.1148341460062734
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.028022030860320884,
        "excess_kurtosis": 15.932163924440513,
        "return_acf_1": -0.22095337045045838,
        "abs_return_acf_1": 0.4704796089027549,
        "abs_return_acf_5": 0.5123287110015396,
        "abs_return_acf_20": 0.28570482594494523,
        "quantile_01": -0.1087464062650627,
        "quantile_99": 0.07596787865787358,
        "hill_tail_index": 2.1944557606752437
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02764760105746977,
        "excess_kurtosis": 24.53643221473132,
        "return_acf_1": -0.24704161454020762,
        "abs_return_acf_1": 0.4286373930995611,
        "abs_return_acf_5": 0.49938414381686735,
        "abs_return_acf_20": 0.2783693098043391,
        "quantile_01": -0.10897817308942383,
        "quantile_99": 0.07324991947088681,
        "hill_tail_index": 2.0281819314811593
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020770030701602295,
        "excess_kurtosis": 14.581047941654749,
        "return_acf_1": -0.21296809319500437,
        "abs_return_acf_1": 0.4786894683770554,
        "abs_return_acf_5": 0.3692878511210179,
        "abs_return_acf_20": 0.2684242600360028,
        "quantile_01": -0.07011579071286513,
        "quantile_99": 0.06476647695618887,
        "hill_tail_index": 2.9732042976141884
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020660124301762554,
        "excess_kurtosis": 15.627951613286395,
        "return_acf_1": -0.13727447093573586,
        "abs_return_acf_1": 0.41055700067733797,
        "abs_return_acf_5": 0.453779819348657,
        "abs_return_acf_20": 0.2876976277476697,
        "quantile_01": -0.061619636226880194,
        "quantile_99": 0.05511704747297851,
        "hill_tail_index": 2.139566646266732
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02793253781181623,
        "excess_kurtosis": 24.782106731864964,
        "return_acf_1": -0.22574255697643816,
        "abs_return_acf_1": 0.4446334566173506,
        "abs_return_acf_5": 0.5080670326714385,
        "abs_return_acf_20": 0.27694251568591877,
        "quantile_01": -0.10527029608455414,
        "quantile_99": 0.07827451229701161,
        "hill_tail_index": 2.0320366776478664
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.024453548161547684,
        "excess_kurtosis": 15.16669074264967,
        "return_acf_1": -0.135681178902763,
        "abs_return_acf_1": 0.4927527088670062,
        "abs_return_acf_5": 0.4476037096561944,
        "abs_return_acf_20": 0.28269767394320394,
        "quantile_01": -0.08866908721201429,
        "quantile_99": 0.06486601376389352,
        "hill_tail_index": 1.8988836140465208
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
