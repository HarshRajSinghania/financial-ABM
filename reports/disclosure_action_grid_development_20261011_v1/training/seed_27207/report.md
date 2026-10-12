# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27207
Run ID: `b5f2e7366f25fd7782a3cc6c6f9f243fc3f4ef13046e4ba3181e472ed2d2093d`
Result fingerprint: `3af2dbcc7da70a364c208d87d13f67337539d36bdafb8d27064be8e393ccba4d`

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
    "equal_weight_sd": -0.7901309523809492,
    "equal_weight_raw": -11.851964285714237,
    "fixed_start_cap_weight_sd": -0.7686060422109929,
    "fixed_start_cap_weight_raw": -11.529090633164891,
    "end_cap_weight_sd": -0.7505049088867857,
    "end_cap_weight_raw": -11.257573633301789
  },
  "full_period_change": {
    "equal_weight_sd": -1.220321428571424,
    "equal_weight_raw": -18.30482142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.146147817460313,
    "inflation_mean_sd": 0.8118495370370371
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.16225000000000314,
    "equal_weight_raw": 2.4337500000000465,
    "fixed_start_cap_weight_sd": 0.1837749101699595,
    "fixed_start_cap_weight_raw": 2.7566236525493926,
    "end_cap_weight_sd": 0.2018760434941664,
    "end_cap_weight_raw": 3.0281406524124956
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7332142857142827,
      "change_raw": -10.99821428571424,
      "decay_adjusted_gain_sd": 0.21916666666666954
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8140476190476159,
      "change_raw": -12.21071428571424,
      "decay_adjusted_gain_sd": 0.13833333333333628
    },
    "small": {
      "count": 18,
      "change_sd": -0.7876587301587269,
      "change_raw": -11.814880952380904,
      "decay_adjusted_gain_sd": 0.1647222222222254
    },
    "large_minus_small_sd": 0.054444444444444184,
    "large_minus_small_raw": 0.8166666666666628
  },
  "inflation": {
    "initial_mean_sd": 0.39691666666666664,
    "final_mean_sd": 0.7980833333333333,
    "mean_sd": 0.6401996253122398,
    "mean_absolute_raw_gap": 9.602994379683597,
    "final_absolute_raw_gap": 11.971249999999998,
    "mean_range_fraction": 0.09602994379683598
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.29333333333333333,
    "initial_wealth_share": 0.2540942840753689,
    "final_wealth_share": 0.28564613454128895
  },
  "pricing_slope": {
    "mean": -0.004934828032115138,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.04310677321777065,
    "real_improvement_cost": 0.026401371535950676,
    "washing_cost": 0.016705401681819974,
    "fine_transfer": 0.02376678364813264,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0668735568659033,
    "resource_cost_fraction_initial_cap": 0.0014368924405923549,
    "private_net_outflow_fraction_initial_cap": 0.002229118562196776,
    "fine_transfer_fraction_initial_cap": 0.0007922261216044212,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00872811501286628,
    "unapplied_final_day_resource_cost": 0.00021571899417511826
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 112.91728971245475,
    "beneficial_raw_gain_per_resource_cost": 1693.7593456868212,
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
    "accrued_cost": 3.118537827421675,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.14234735123119854,
    "accrued_cost_fraction_initial_cap": 0.10395126091405582,
    "mean_contract_rate": 0.04301457561954593,
    "maximum_ledger_error": 7.453889935837843e-20
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
    "maximum_relative_cash_error": 1.1162434087581672e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.1819345900711741,
      "maximum": -0.023005279286099693,
      "mean": -0.10661770947000775,
      "median": -0.10091237778215495,
      "quantile_05": -0.1713436944696542,
      "quantile_95": -0.06471319221736678
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
      "minimum": 0.2114693863543373,
      "maximum": 0.8055757651138017,
      "mean": 0.5795436380657265,
      "median": 0.6566257064359562,
      "quantile_05": 0.25290278909941316,
      "quantile_95": 0.7556328134791279
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
        "daily_volatility": 0.020950759170769846,
        "excess_kurtosis": 9.915011553112407,
        "return_acf_1": -0.129628660521522,
        "abs_return_acf_1": 0.3151415626529908,
        "abs_return_acf_5": 0.35225010793314687,
        "abs_return_acf_20": 0.2097153980328043,
        "quantile_01": -0.07391392290086345,
        "quantile_99": 0.05854786768389054,
        "hill_tail_index": 2.6626674458950874
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019296060842819117,
        "excess_kurtosis": 6.930704534169287,
        "return_acf_1": -0.09381164766340556,
        "abs_return_acf_1": 0.3416034108079898,
        "abs_return_acf_5": 0.3658381228713757,
        "abs_return_acf_20": 0.26225182415226034,
        "quantile_01": -0.06445924200331643,
        "quantile_99": 0.05903438113274075,
        "hill_tail_index": 3.570197524227893
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01933601185381386,
        "excess_kurtosis": 2.929849862626245,
        "return_acf_1": -0.06911157054876736,
        "abs_return_acf_1": 0.22593330771724857,
        "abs_return_acf_5": 0.3230198180307216,
        "abs_return_acf_20": 0.22376930605487755,
        "quantile_01": -0.05253047881284954,
        "quantile_99": 0.05342312628583084,
        "hill_tail_index": 4.424440546229925
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020841574110323793,
        "excess_kurtosis": 10.962258910150952,
        "return_acf_1": -0.10057989051346951,
        "abs_return_acf_1": 0.32103674534842475,
        "abs_return_acf_5": 0.4419910141948544,
        "abs_return_acf_20": 0.24060681149085533,
        "quantile_01": -0.07084577313711234,
        "quantile_99": 0.05335093957061193,
        "hill_tail_index": 2.2597360091875074
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02055284374543325,
        "excess_kurtosis": 3.0733975981187838,
        "return_acf_1": -0.09251517338596667,
        "abs_return_acf_1": 0.3392998350509496,
        "abs_return_acf_5": 0.31231703751798157,
        "abs_return_acf_20": 0.2918334652301775,
        "quantile_01": -0.05806614649432144,
        "quantile_99": 0.0657937324267933,
        "hill_tail_index": 6.294615614861623
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01966084539087331,
        "excess_kurtosis": 9.06008997672396,
        "return_acf_1": -0.10124486505084038,
        "abs_return_acf_1": 0.36368786930711955,
        "abs_return_acf_5": 0.41124794182408414,
        "abs_return_acf_20": 0.2638487863497482,
        "quantile_01": -0.057903663962461306,
        "quantile_99": 0.05919435646899649,
        "hill_tail_index": 2.8002299191257802
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02132972002239061,
        "excess_kurtosis": 10.636591531053773,
        "return_acf_1": -0.11457419309947539,
        "abs_return_acf_1": 0.36244253829697753,
        "abs_return_acf_5": 0.4055452789187823,
        "abs_return_acf_20": 0.28836984080460426,
        "quantile_01": -0.07304183249663879,
        "quantile_99": 0.0666593384363454,
        "hill_tail_index": 3.2802150946197504
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01851596608811295,
        "excess_kurtosis": 9.966212040062617,
        "return_acf_1": -0.13153267798186555,
        "abs_return_acf_1": 0.30483734064071566,
        "abs_return_acf_5": 0.3293957674033549,
        "abs_return_acf_20": 0.28522622057032043,
        "quantile_01": -0.05068858929673751,
        "quantile_99": 0.056617692234139066,
        "hill_tail_index": 3.096875867014647
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019835236501738473,
        "excess_kurtosis": 8.850414918053527,
        "return_acf_1": -0.07534854516706599,
        "abs_return_acf_1": 0.3334866874658092,
        "abs_return_acf_5": 0.3587234514278384,
        "abs_return_acf_20": 0.1976529078665429,
        "quantile_01": -0.0676604936432301,
        "quantile_99": 0.050443937822103685,
        "hill_tail_index": 3.3169116983459186
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020191974493422648,
        "excess_kurtosis": 7.777950272125624,
        "return_acf_1": -0.09107801128288767,
        "abs_return_acf_1": 0.40326924675472914,
        "abs_return_acf_5": 0.3869627727341287,
        "abs_return_acf_20": 0.30661103428328573,
        "quantile_01": -0.06865812109999818,
        "quantile_99": 0.06086274607373792,
        "hill_tail_index": 3.1144041917140464
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01941141770474834,
        "excess_kurtosis": 7.866765278229872,
        "return_acf_1": -0.11106887813183644,
        "abs_return_acf_1": 0.3614381331444249,
        "abs_return_acf_5": 0.41912125332863803,
        "abs_return_acf_20": 0.2802510496034421,
        "quantile_01": -0.06719354798487191,
        "quantile_99": 0.04967915689845627,
        "hill_tail_index": 2.783786350066632
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017723812741582353,
        "excess_kurtosis": 5.329414922585151,
        "return_acf_1": -0.09915798715246227,
        "abs_return_acf_1": 0.2628524519383706,
        "abs_return_acf_5": 0.32011650312537127,
        "abs_return_acf_20": 0.2551619480974491,
        "quantile_01": -0.04604783670597823,
        "quantile_99": 0.05301946613593111,
        "hill_tail_index": 3.2753175397674075
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01850627421103189,
        "excess_kurtosis": 5.183161388303079,
        "return_acf_1": -0.1209883899688193,
        "abs_return_acf_1": 0.27622145656788666,
        "abs_return_acf_5": 0.3059828982985568,
        "abs_return_acf_20": 0.2797165078957102,
        "quantile_01": -0.045312854020692954,
        "quantile_99": 0.055650551414996884,
        "hill_tail_index": 2.8656229727939446
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019186051193767716,
        "excess_kurtosis": 5.619408475123212,
        "return_acf_1": -0.11053282651518746,
        "abs_return_acf_1": 0.30222113743051987,
        "abs_return_acf_5": 0.3399769729490054,
        "abs_return_acf_20": 0.34708749600964545,
        "quantile_01": -0.06640115265192471,
        "quantile_99": 0.05962387527995801,
        "hill_tail_index": 4.021847148493088
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020145827092915205,
        "excess_kurtosis": 9.768227717275952,
        "return_acf_1": -0.1819345900711741,
        "abs_return_acf_1": 0.40110599614525005,
        "abs_return_acf_5": 0.3471083675978747,
        "abs_return_acf_20": 0.240156262594001,
        "quantile_01": -0.0635691674407121,
        "quantile_99": 0.052621714346323435,
        "hill_tail_index": 2.9587386685984947
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021970736739174143,
        "excess_kurtosis": 12.571979235151105,
        "return_acf_1": -0.08783635099566067,
        "abs_return_acf_1": 0.3841961318521044,
        "abs_return_acf_5": 0.4389705088847732,
        "abs_return_acf_20": 0.2591886088964557,
        "quantile_01": -0.0763161548054506,
        "quantile_99": 0.0608386778416968,
        "hill_tail_index": 2.39461538676791
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018704908657612134,
        "excess_kurtosis": 8.279594730888931,
        "return_acf_1": -0.023005279286099693,
        "abs_return_acf_1": 0.2672625340274651,
        "abs_return_acf_5": 0.36290185747489273,
        "abs_return_acf_20": 0.19147209764061357,
        "quantile_01": -0.05642948521552412,
        "quantile_99": 0.0421429028975504,
        "hill_tail_index": 2.475951912312087
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020552133709641734,
        "excess_kurtosis": 7.322226707412291,
        "return_acf_1": -0.06397212566670285,
        "abs_return_acf_1": 0.3679612569485216,
        "abs_return_acf_5": 0.385544844019747,
        "abs_return_acf_20": 0.28930803378193526,
        "quantile_01": -0.07288203440503109,
        "quantile_99": 0.0583777442781382,
        "hill_tail_index": 2.9249922800448527
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020185863878248934,
        "excess_kurtosis": 7.483210847213023,
        "return_acf_1": -0.0656189402237338,
        "abs_return_acf_1": 0.2740745287626181,
        "abs_return_acf_5": 0.3947313736858651,
        "abs_return_acf_20": 0.25506616964084095,
        "quantile_01": -0.06763075988345099,
        "quantile_99": 0.04876340564416442,
        "hill_tail_index": 2.554477710100474
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020163014989116285,
        "excess_kurtosis": 9.138328761181537,
        "return_acf_1": -0.12068847389668352,
        "abs_return_acf_1": 0.3420151395740079,
        "abs_return_acf_5": 0.4032860760339268,
        "abs_return_acf_20": 0.2771464859888919,
        "quantile_01": -0.074506742606119,
        "quantile_99": 0.04837598149933096,
        "hill_tail_index": 2.60291450305053
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02068084986852436,
        "excess_kurtosis": 8.533408414139894,
        "return_acf_1": -0.06850529759947045,
        "abs_return_acf_1": 0.3249101894064382,
        "abs_return_acf_5": 0.40019099829948546,
        "abs_return_acf_20": 0.27984592450541934,
        "quantile_01": -0.06606163725462881,
        "quantile_99": 0.05449775024085587,
        "hill_tail_index": 3.1587332267689874
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020066173762767956,
        "excess_kurtosis": 9.097332599594507,
        "return_acf_1": -0.1308507001283285,
        "abs_return_acf_1": 0.31246812425476156,
        "abs_return_acf_5": 0.34164237491094945,
        "abs_return_acf_20": 0.24237937376182286,
        "quantile_01": -0.07329511578161842,
        "quantile_99": 0.05704944420026971,
        "hill_tail_index": 2.766316218651101
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022018254620877493,
        "excess_kurtosis": 10.276225220456826,
        "return_acf_1": -0.08828409428326969,
        "abs_return_acf_1": 0.35689469017155023,
        "abs_return_acf_5": 0.4615219132934272,
        "abs_return_acf_20": 0.3156540866096998,
        "quantile_01": -0.076113513882736,
        "quantile_99": 0.06422732541029982,
        "hill_tail_index": 3.1186816869195733
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020947735548298815,
        "excess_kurtosis": 12.42428100168538,
        "return_acf_1": -0.10527791757844042,
        "abs_return_acf_1": 0.4148131425168565,
        "abs_return_acf_5": 0.3889646861938164,
        "abs_return_acf_20": 0.2439903675569198,
        "quantile_01": -0.07518144971884286,
        "quantile_99": 0.06049560864056002,
        "hill_tail_index": 2.5453222681652887
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019487044769367162,
        "excess_kurtosis": 5.091071442174124,
        "return_acf_1": -0.18134719307124395,
        "abs_return_acf_1": 0.3360262273251107,
        "abs_return_acf_5": 0.2698649913428503,
        "abs_return_acf_20": 0.26544479815676064,
        "quantile_01": -0.062375728711000035,
        "quantile_99": 0.06189389531343828,
        "hill_tail_index": 3.705415455659426
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020483014244827062,
        "excess_kurtosis": 10.69752720606637,
        "return_acf_1": -0.15328276753326356,
        "abs_return_acf_1": 0.42194733357317993,
        "abs_return_acf_5": 0.3614361015739072,
        "abs_return_acf_20": 0.27193611927258077,
        "quantile_01": -0.06637162402868217,
        "quantile_99": 0.0558323557849788,
        "hill_tail_index": 2.799980000323765
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01988328049133344,
        "excess_kurtosis": 13.14707994471015,
        "return_acf_1": -0.09393338019355726,
        "abs_return_acf_1": 0.1995809385054546,
        "abs_return_acf_5": 0.26369376203834105,
        "abs_return_acf_20": 0.19513686782389314,
        "quantile_01": -0.06871619621523174,
        "quantile_99": 0.04994108165288723,
        "hill_tail_index": 2.3460028667850903
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019773538375465666,
        "excess_kurtosis": 9.006681857698435,
        "return_acf_1": -0.1591171961788223,
        "abs_return_acf_1": 0.37762824377254967,
        "abs_return_acf_5": 0.345130204991541,
        "abs_return_acf_20": 0.22430076163156165,
        "quantile_01": -0.06034669620016292,
        "quantile_99": 0.05682037915756553,
        "hill_tail_index": 3.6233376377710473
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020377288070190024,
        "excess_kurtosis": 12.398880517545614,
        "return_acf_1": -0.14770424215497868,
        "abs_return_acf_1": 0.41630280235029987,
        "abs_return_acf_5": 0.38593143880625586,
        "abs_return_acf_20": 0.26646093493726886,
        "quantile_01": -0.0667638222842768,
        "quantile_99": 0.061884458241073206,
        "hill_tail_index": 3.0488061894350373
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01998307633759909,
        "excess_kurtosis": 8.706466973922296,
        "return_acf_1": -0.08599941825523098,
        "abs_return_acf_1": 0.3117538921504738,
        "abs_return_acf_5": 0.3692891912582611,
        "abs_return_acf_20": 0.22898891400344643,
        "quantile_01": -0.0584987982435433,
        "quantile_99": 0.051962292792574145,
        "hill_tail_index": 2.4657229557803557
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
