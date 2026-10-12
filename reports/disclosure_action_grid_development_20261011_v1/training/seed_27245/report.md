# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27245
Run ID: `b26eaa5330a0bc33230f3e5a42a6a424fcab2effcfd50c12f0f5487388284000`
Result fingerprint: `a657c35c34398a553499a3e97fbf5ea4c3d2e03624336cdf4bf62cd951e42ad2`

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
    "equal_weight_sd": -0.8418809523809491,
    "equal_weight_raw": -12.628214285714234,
    "fixed_start_cap_weight_sd": -0.8008158472350264,
    "fixed_start_cap_weight_raw": -12.012237708525397,
    "end_cap_weight_sd": -0.8029806268714912,
    "end_cap_weight_raw": -12.044709403072366
  },
  "full_period_change": {
    "equal_weight_sd": -1.275904761904757,
    "equal_weight_raw": -19.138571428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1914619708994665,
    "inflation_mean_sd": 0.3587893518518519
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1063377062114381,
    "equal_weight_raw": 1.5950655931715716,
    "fixed_start_cap_weight_sd": 0.14668377869822186,
    "fixed_start_cap_weight_raw": 2.2002566804733283,
    "end_cap_weight_sd": 0.14538042255441536,
    "end_cap_weight_raw": 2.18070633831623
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7007142857142831,
      "change_raw": -10.510714285714245,
      "decay_adjusted_gain_sd": 0.2100437287810181
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7376587301587268,
      "change_raw": -11.064880952380904,
      "decay_adjusted_gain_sd": 0.21472222222222556
    },
    "small": {
      "count": 18,
      "change_sd": -0.917519841269838,
      "change_raw": -13.76279761904757,
      "decay_adjusted_gain_sd": 0.03486111111111434
    },
    "large_minus_small_sd": 0.21680555555555492,
    "large_minus_small_raw": 3.252083333333324
  },
  "inflation": {
    "initial_mean_sd": 0.27708333333333335,
    "final_mean_sd": 0.37516666666666665,
    "mean_sd": 0.30978365251179574,
    "mean_absolute_raw_gap": 4.646754787676937,
    "final_absolute_raw_gap": 5.6275,
    "mean_range_fraction": 0.04646754787676936
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.24,
    "initial_wealth_share": 0.2600839317102987,
    "final_wealth_share": 0.2866892975220475
  },
  "pricing_slope": {
    "mean": -0.0018067617391360857,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.015052964251751655,
    "real_improvement_cost": 0.0026892849474604488,
    "washing_cost": 0.012363679304291206,
    "fine_transfer": 0.012038567197918905,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.02709153144967056,
    "resource_cost_fraction_initial_cap": 0.0005017654750583885,
    "private_net_outflow_fraction_initial_cap": 0.000903051048322352,
    "fine_transfer_fraction_initial_cap": 0.0004012855732639635,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00024677682526868226,
    "unapplied_final_day_resource_cost": 4.6662896898986085e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 211.92710837481192,
    "beneficial_raw_gain_per_resource_cost": 3178.906625622179,
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
    "accrued_cost": 3.107544223051776,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.1313537468612995,
    "accrued_cost_fraction_initial_cap": 0.1035848074350592,
    "mean_contract_rate": 0.04379470583441898,
    "maximum_ledger_error": 4.0657581468206416e-20
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
    "maximum_relative_cash_error": 2.203241285306735e-15,
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
      "minimum": -0.24901550449734908,
      "maximum": -0.08155383592556378,
      "mean": -0.15113820556920796,
      "median": -0.14991442507973488,
      "quantile_05": -0.2056279491761619,
      "quantile_95": -0.09061026370478537
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
      "minimum": 0.2900484710095474,
      "maximum": 0.7140710503964682,
      "mean": 0.4583560604350439,
      "median": 0.4279458716971751,
      "quantile_05": 0.31989468310438385,
      "quantile_95": 0.6573514861730314
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
        "daily_volatility": 0.01731552585962478,
        "excess_kurtosis": 2.2736314072335366,
        "return_acf_1": -0.20415525563607248,
        "abs_return_acf_1": 0.24930116324685506,
        "abs_return_acf_5": 0.21598899789425344,
        "abs_return_acf_20": 0.2493904099998251,
        "quantile_01": -0.04851469555879255,
        "quantile_99": 0.04585603979062056,
        "hill_tail_index": 5.9024574236432805
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01768784747832113,
        "excess_kurtosis": 2.348032903952677,
        "return_acf_1": -0.13364982140775278,
        "abs_return_acf_1": 0.27950849499162533,
        "abs_return_acf_5": 0.26126423220356315,
        "abs_return_acf_20": 0.2520922146194566,
        "quantile_01": -0.05025969343187334,
        "quantile_99": 0.04582501855009276,
        "hill_tail_index": 4.046698269227028
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019832993908927957,
        "excess_kurtosis": 5.426407014497659,
        "return_acf_1": -0.18401497667573546,
        "abs_return_acf_1": 0.3811102018050545,
        "abs_return_acf_5": 0.40849477773043763,
        "abs_return_acf_20": 0.3480657912471246,
        "quantile_01": -0.061855572166716236,
        "quantile_99": 0.060676236555314435,
        "hill_tail_index": 4.453880130110738
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017217266659048585,
        "excess_kurtosis": 3.284400842277626,
        "return_acf_1": -0.24901550449734908,
        "abs_return_acf_1": 0.3178982164536003,
        "abs_return_acf_5": 0.2841828797759936,
        "abs_return_acf_20": 0.28064333362015464,
        "quantile_01": -0.04693432635351176,
        "quantile_99": 0.05291522984910455,
        "hill_tail_index": 4.410391124782583
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019957630277564628,
        "excess_kurtosis": 7.587774487295738,
        "return_acf_1": -0.20147413714710258,
        "abs_return_acf_1": 0.4333488179359108,
        "abs_return_acf_5": 0.4503109490120308,
        "abs_return_acf_20": 0.36041989140715225,
        "quantile_01": -0.06356395783319993,
        "quantile_99": 0.05996527456584793,
        "hill_tail_index": 3.240989848607461
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019681355446357848,
        "excess_kurtosis": 6.204416362658073,
        "return_acf_1": -0.11600138092647665,
        "abs_return_acf_1": 0.3365590534903261,
        "abs_return_acf_5": 0.3563498181732655,
        "abs_return_acf_20": 0.27668493150485873,
        "quantile_01": -0.060449001145359726,
        "quantile_99": 0.06007217369836413,
        "hill_tail_index": 3.1514544486621863
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01746504618210534,
        "excess_kurtosis": 3.3527101884985173,
        "return_acf_1": -0.1410347848952797,
        "abs_return_acf_1": 0.24035808406858067,
        "abs_return_acf_5": 0.23780685887640218,
        "abs_return_acf_20": 0.20374247477578064,
        "quantile_01": -0.04468599834262167,
        "quantile_99": 0.049808148933803136,
        "hill_tail_index": 3.3867568312417276
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017639744173933034,
        "excess_kurtosis": 14.537962738472814,
        "return_acf_1": -0.1356214452841737,
        "abs_return_acf_1": 0.3096826202181154,
        "abs_return_acf_5": 0.3727741352027031,
        "abs_return_acf_20": 0.32937410285583246,
        "quantile_01": -0.0534241192282697,
        "quantile_99": 0.04401321118613235,
        "hill_tail_index": 2.023433892906794
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016477395376745016,
        "excess_kurtosis": 2.2584907217489887,
        "return_acf_1": -0.18133799943235987,
        "abs_return_acf_1": 0.2519769075997444,
        "abs_return_acf_5": 0.22512047935240312,
        "abs_return_acf_20": 0.24835694180066628,
        "quantile_01": -0.047371127293668276,
        "quantile_99": 0.041347344684304434,
        "hill_tail_index": 4.06087780544254
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0181124210510346,
        "excess_kurtosis": 4.108548064556128,
        "return_acf_1": -0.09578239945112607,
        "abs_return_acf_1": 0.2223478245915329,
        "abs_return_acf_5": 0.31491349436649296,
        "abs_return_acf_20": 0.2682579979326916,
        "quantile_01": -0.05323354296561127,
        "quantile_99": 0.04933181271887004,
        "hill_tail_index": 3.648156302654627
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01811391310796294,
        "excess_kurtosis": 6.31320112132196,
        "return_acf_1": -0.08155383592556378,
        "abs_return_acf_1": 0.3932076890510715,
        "abs_return_acf_5": 0.340088250454727,
        "abs_return_acf_20": 0.3003838112252228,
        "quantile_01": -0.06012204759128868,
        "quantile_99": 0.05746386701018233,
        "hill_tail_index": 3.682574138319505
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01966092008002423,
        "excess_kurtosis": 8.444212328631666,
        "return_acf_1": -0.12411003946887447,
        "abs_return_acf_1": 0.4278577634207766,
        "abs_return_acf_5": 0.3876309226529034,
        "abs_return_acf_20": 0.3134978224832753,
        "quantile_01": -0.05687265927619273,
        "quantile_99": 0.056643224031001534,
        "hill_tail_index": 3.0305598455927987
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019694454153505712,
        "excess_kurtosis": 8.580457356220606,
        "return_acf_1": -0.15852259982493952,
        "abs_return_acf_1": 0.4100208930291657,
        "abs_return_acf_5": 0.39290892721328935,
        "abs_return_acf_20": 0.29441850608785936,
        "quantile_01": -0.05655518389849673,
        "quantile_99": 0.064131440456979,
        "hill_tail_index": 2.697573291998024
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016726188753734425,
        "excess_kurtosis": 2.1064756947974095,
        "return_acf_1": -0.20683288025441687,
        "abs_return_acf_1": 0.29205606383125454,
        "abs_return_acf_5": 0.3005660175707315,
        "abs_return_acf_20": 0.2203411563557176,
        "quantile_01": -0.04567654864409707,
        "quantile_99": 0.04092525270874987,
        "hill_tail_index": 3.920454956883452
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018163497748079762,
        "excess_kurtosis": 4.4894485434202975,
        "return_acf_1": -0.0863785162759611,
        "abs_return_acf_1": 0.33927697904025955,
        "abs_return_acf_5": 0.35506324371048403,
        "abs_return_acf_20": 0.23273447995737004,
        "quantile_01": -0.05221588634794998,
        "quantile_99": 0.05975335846069937,
        "hill_tail_index": 3.9561821847923193
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016312383031848524,
        "excess_kurtosis": 6.304529084069642,
        "return_acf_1": -0.20115551839006326,
        "abs_return_acf_1": 0.21081436522239702,
        "abs_return_acf_5": 0.18774285750947012,
        "abs_return_acf_20": 0.2560627232601961,
        "quantile_01": -0.04679064589547417,
        "quantile_99": 0.04181737189616722,
        "hill_tail_index": 2.7740899637266274
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01680781804846869,
        "excess_kurtosis": 6.498433770758632,
        "return_acf_1": -0.15016306058291842,
        "abs_return_acf_1": 0.3652921827450089,
        "abs_return_acf_5": 0.3258655702024524,
        "abs_return_acf_20": 0.24563444691516664,
        "quantile_01": -0.05344681024051083,
        "quantile_99": 0.049929604676697346,
        "hill_tail_index": 2.6649417840908995
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01557308638394886,
        "excess_kurtosis": 3.8864127741689023,
        "return_acf_1": -0.16755796571040413,
        "abs_return_acf_1": 0.19724178387766322,
        "abs_return_acf_5": 0.21686406972797895,
        "abs_return_acf_20": 0.25912197728322245,
        "quantile_01": -0.039908853992721864,
        "quantile_99": 0.04552266832376967,
        "hill_tail_index": 3.337717385042914
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01612476596736684,
        "excess_kurtosis": 5.588859955443839,
        "return_acf_1": -0.1717985429508285,
        "abs_return_acf_1": 0.32391373161319376,
        "abs_return_acf_5": 0.28182998255363495,
        "abs_return_acf_20": 0.2678174008542385,
        "quantile_01": -0.04621264661880903,
        "quantile_99": 0.052290732279758854,
        "hill_tail_index": 2.363465288968575
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01812190533626763,
        "excess_kurtosis": 4.689985092323779,
        "return_acf_1": -0.1637365640810448,
        "abs_return_acf_1": 0.39676853538320356,
        "abs_return_acf_5": 0.35703663250181933,
        "abs_return_acf_20": 0.2896324290469214,
        "quantile_01": -0.054450245424686,
        "quantile_99": 0.0486014288792549,
        "hill_tail_index": 3.3303429066324077
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020404333868346503,
        "excess_kurtosis": 16.628015679310586,
        "return_acf_1": -0.12772256829821707,
        "abs_return_acf_1": 0.33384649461103894,
        "abs_return_acf_5": 0.32154539743415783,
        "abs_return_acf_20": 0.24279641386643355,
        "quantile_01": -0.05349948190789994,
        "quantile_99": 0.05234024979668619,
        "hill_tail_index": 2.5776924610154257
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01975053813361023,
        "excess_kurtosis": 6.7017242472905725,
        "return_acf_1": -0.11364740930887463,
        "abs_return_acf_1": 0.3342042854248474,
        "abs_return_acf_5": 0.3161230809328419,
        "abs_return_acf_20": 0.19707939950291106,
        "quantile_01": -0.065459047578943,
        "quantile_99": 0.057239653598045066,
        "hill_tail_index": 3.4685330829247967
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01993682220132784,
        "excess_kurtosis": 7.570643054303332,
        "return_acf_1": -0.14966578957655133,
        "abs_return_acf_1": 0.35397312410154824,
        "abs_return_acf_5": 0.32733361133593564,
        "abs_return_acf_20": 0.32333897075026796,
        "quantile_01": -0.06508473550899602,
        "quantile_99": 0.05722816527805394,
        "hill_tail_index": 3.4779009594450763
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016503156265980277,
        "excess_kurtosis": 4.074107800593799,
        "return_acf_1": -0.11447352006977339,
        "abs_return_acf_1": 0.2935040307189245,
        "abs_return_acf_5": 0.30431712632288865,
        "abs_return_acf_20": 0.21765289018894882,
        "quantile_01": -0.04578608374868839,
        "quantile_99": 0.04416426819491122,
        "hill_tail_index": 3.236108303747982
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015554292739292992,
        "excess_kurtosis": 4.819281469143819,
        "return_acf_1": -0.14002216293527125,
        "abs_return_acf_1": 0.24875776930059265,
        "abs_return_acf_5": 0.30242129747952506,
        "abs_return_acf_20": 0.2598169403113902,
        "quantile_01": -0.0407689404414351,
        "quantile_99": 0.04022577775069363,
        "hill_tail_index": 2.993170843035171
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01793104663012464,
        "excess_kurtosis": 4.734568642239814,
        "return_acf_1": -0.12958450329171373,
        "abs_return_acf_1": 0.35829629204037694,
        "abs_return_acf_5": 0.3105268285708656,
        "abs_return_acf_20": 0.3553862845754506,
        "quantile_01": -0.056475342795362045,
        "quantile_99": 0.05253164026402496,
        "hill_tail_index": 3.8732973126262533
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021331765664874502,
        "excess_kurtosis": 6.000318870668526,
        "return_acf_1": -0.15809316724811923,
        "abs_return_acf_1": 0.3863219228015279,
        "abs_return_acf_5": 0.3845931562394005,
        "abs_return_acf_20": 0.346078009965943,
        "quantile_01": -0.061071755232979454,
        "quantile_99": 0.06817670815514701,
        "hill_tail_index": 3.5050610982961157
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01630782905796265,
        "excess_kurtosis": 2.786568728619497,
        "return_acf_1": -0.153585153018155,
        "abs_return_acf_1": 0.20259421900435162,
        "abs_return_acf_5": 0.20725197971982248,
        "abs_return_acf_20": 0.2149117997102911,
        "quantile_01": -0.045414330995832884,
        "quantile_99": 0.04059541501171519,
        "hill_tail_index": 3.946608420607425
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016955957871331407,
        "excess_kurtosis": 5.820373510460799,
        "return_acf_1": -0.15466975619183201,
        "abs_return_acf_1": 0.27306483587104885,
        "abs_return_acf_5": 0.2662254917335333,
        "abs_return_acf_20": 0.22351759514778294,
        "quantile_01": -0.05304970811384308,
        "quantile_99": 0.045472101945456735,
        "hill_tail_index": 3.267022746636328
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016090737650274804,
        "excess_kurtosis": 6.324135616376829,
        "return_acf_1": -0.1387849083192886,
        "abs_return_acf_1": 0.23767610296878047,
        "abs_return_acf_5": 0.24446319908832678,
        "abs_return_acf_20": 0.2364372809880186,
        "quantile_01": -0.043176278892448336,
        "quantile_99": 0.048147979473805766,
        "hill_tail_index": 2.9651264414489082
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
