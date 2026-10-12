# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27015
Run ID: `ec4531abf1f241ccbed14d73efe5be482b3cfed6e95380ea4fd2d254c0997026`
Result fingerprint: `65d2351d48bbb6ed5d3c5cc1942b6a99f47c6c7a3cb373de9e9993bc6fd09c4a`

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
    "equal_weight_sd": -0.4414642857142825,
    "equal_weight_raw": -6.621964285714238,
    "fixed_start_cap_weight_sd": -0.41412089963964904,
    "fixed_start_cap_weight_raw": -6.211813494594735,
    "end_cap_weight_sd": -0.40975960089099805,
    "end_cap_weight_raw": -6.1463940133649695
  },
  "full_period_change": {
    "equal_weight_sd": -0.7168214285714237,
    "equal_weight_raw": -10.752321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.6728025793650749,
    "inflation_mean_sd": 0.5316861772486773
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5109166666666698,
    "equal_weight_raw": 7.6637500000000465,
    "fixed_start_cap_weight_sd": 0.5382600527413033,
    "fixed_start_cap_weight_raw": 8.07390079111955,
    "end_cap_weight_sd": 0.5426213514899543,
    "end_cap_weight_raw": 8.139320272349316
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.25488095238094904,
      "change_raw": -3.8232142857142355,
      "decay_adjusted_gain_sd": 0.6975000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.3482142857142825,
      "change_raw": -5.223214285714237,
      "decay_adjusted_gain_sd": 0.6041666666666698
    },
    "small": {
      "count": 18,
      "change_sd": -0.5191865079365048,
      "change_raw": -7.787797619047572,
      "decay_adjusted_gain_sd": 0.43319444444444755
    },
    "large_minus_small_sd": 0.26430555555555574,
    "large_minus_small_raw": 3.9645833333333362
  },
  "inflation": {
    "initial_mean_sd": 0.20525000000000002,
    "final_mean_sd": 0.5518333333333333,
    "mean_sd": 0.4076715237302248,
    "mean_absolute_raw_gap": 6.115072855953372,
    "final_absolute_raw_gap": 8.277500000000002,
    "mean_range_fraction": 0.06115072855953372
  },
  "impact": {
    "initial_share": 0.37333333333333335,
    "final_share": 0.37333333333333335,
    "initial_wealth_share": 0.43168289668840504,
    "final_wealth_share": 0.42827430924187965
  },
  "pricing_slope": {
    "mean": -0.0020922987660020867,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.12286818669138866,
    "real_improvement_cost": 0.10969206812045143,
    "washing_cost": 0.013176118570937236,
    "fine_transfer": 0.01021071509324302,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.13307890178463166,
    "resource_cost_fraction_initial_cap": 0.004095606223046289,
    "private_net_outflow_fraction_initial_cap": 0.004435963392821056,
    "fine_transfer_fraction_initial_cap": 0.0003403571697747674,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003186656535049811,
    "unapplied_final_day_resource_cost": 0.013557841857409877
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 124.74750716797497,
    "beneficial_raw_gain_per_resource_cost": 1871.2126075196247,
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
    "accrued_cost": 3.036636600325167,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.06044612413469089,
    "accrued_cost_fraction_initial_cap": 0.10122122001083891,
    "mean_contract_rate": 0.04219548797997449,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 7,
    "maximum_relative_cash_error": 1.3870838819880612e-15,
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
      "minimum": -0.3532797254543919,
      "maximum": -0.11517428179616962,
      "mean": -0.19574880188753488,
      "median": -0.19346463988622864,
      "quantile_05": -0.2619594205568313,
      "quantile_95": -0.1304021597840332
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
      "minimum": 0.3279609818007887,
      "maximum": 0.8213344715767221,
      "mean": 0.6425367111907032,
      "median": 0.654466165407717,
      "quantile_05": 0.4515177938220546,
      "quantile_95": 0.780398456514097
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
        "daily_volatility": 0.02203805904918733,
        "excess_kurtosis": 11.30884665235068,
        "return_acf_1": -0.15638323343803678,
        "abs_return_acf_1": 0.40769804025659095,
        "abs_return_acf_5": 0.401647347018016,
        "abs_return_acf_20": 0.38331067299939825,
        "quantile_01": -0.07332856343917174,
        "quantile_99": 0.05603688339208408,
        "hill_tail_index": 2.9798862140493174
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01986901991435666,
        "excess_kurtosis": 12.456915829750946,
        "return_acf_1": -0.11517428179616962,
        "abs_return_acf_1": 0.28307171887677446,
        "abs_return_acf_5": 0.30803088065803186,
        "abs_return_acf_20": 0.24489884874954715,
        "quantile_01": -0.06530686512054495,
        "quantile_99": 0.05849738969356747,
        "hill_tail_index": 3.085978942764781
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021325353498397003,
        "excess_kurtosis": 11.86794656727241,
        "return_acf_1": -0.20195274008781638,
        "abs_return_acf_1": 0.47625501613193794,
        "abs_return_acf_5": 0.46387335878677366,
        "abs_return_acf_20": 0.3036383287586375,
        "quantile_01": -0.0703403362926204,
        "quantile_99": 0.06521141824262004,
        "hill_tail_index": 2.75312739475506
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022796798277160017,
        "excess_kurtosis": 13.226351803222386,
        "return_acf_1": -0.20156952450329643,
        "abs_return_acf_1": 0.4753826467158668,
        "abs_return_acf_5": 0.43105379248416287,
        "abs_return_acf_20": 0.3979830601090681,
        "quantile_01": -0.07642499827907254,
        "quantile_99": 0.07531147514203139,
        "hill_tail_index": 4.460736509407421
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022009642943886444,
        "excess_kurtosis": 12.78098182094471,
        "return_acf_1": -0.19227993482680272,
        "abs_return_acf_1": 0.3500220138410591,
        "abs_return_acf_5": 0.3089785879549417,
        "abs_return_acf_20": 0.3094420784963949,
        "quantile_01": -0.06812140001714724,
        "quantile_99": 0.05462020019177812,
        "hill_tail_index": 2.394098310560515
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020670995307770605,
        "excess_kurtosis": 7.313729379815605,
        "return_acf_1": -0.2050311397914912,
        "abs_return_acf_1": 0.35877148583365814,
        "abs_return_acf_5": 0.3728626092498964,
        "abs_return_acf_20": 0.2666004989732429,
        "quantile_01": -0.06719017584531169,
        "quantile_99": 0.06778004124690228,
        "hill_tail_index": 3.4995346055426686
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02161659325524108,
        "excess_kurtosis": 10.772993382224334,
        "return_acf_1": -0.19969224603191676,
        "abs_return_acf_1": 0.3355185022299784,
        "abs_return_acf_5": 0.3382869814809329,
        "abs_return_acf_20": 0.32716582575382147,
        "quantile_01": -0.07092810418573721,
        "quantile_99": 0.06069876898685102,
        "hill_tail_index": 2.700375586861013
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02225515507810894,
        "excess_kurtosis": 12.73456553487608,
        "return_acf_1": -0.14864363091420665,
        "abs_return_acf_1": 0.2916564891336638,
        "abs_return_acf_5": 0.3804246757610964,
        "abs_return_acf_20": 0.320800515999783,
        "quantile_01": -0.06656552625514663,
        "quantile_99": 0.067183463636392,
        "hill_tail_index": 2.7413128198941163
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021161764928129677,
        "excess_kurtosis": 10.610002465577617,
        "return_acf_1": -0.17435134036411776,
        "abs_return_acf_1": 0.36130886453057465,
        "abs_return_acf_5": 0.3506208480675337,
        "abs_return_acf_20": 0.2879240817717916,
        "quantile_01": -0.07477447773674066,
        "quantile_99": 0.062168294674850376,
        "hill_tail_index": 3.6482959898428495
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021035085635070266,
        "excess_kurtosis": 10.224447163595523,
        "return_acf_1": -0.1816313843025529,
        "abs_return_acf_1": 0.34605316769683764,
        "abs_return_acf_5": 0.34135432145588107,
        "abs_return_acf_20": 0.26251770153836534,
        "quantile_01": -0.06167646900665169,
        "quantile_99": 0.05139092673421932,
        "hill_tail_index": 2.777458350328916
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021286737417789317,
        "excess_kurtosis": 10.303582270698415,
        "return_acf_1": -0.26343211784122406,
        "abs_return_acf_1": 0.369683570054886,
        "abs_return_acf_5": 0.30623654456228727,
        "abs_return_acf_20": 0.2399668371363776,
        "quantile_01": -0.06663478502308388,
        "quantile_99": 0.05784850366624909,
        "hill_tail_index": 2.7890022007193607
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02249113543754425,
        "excess_kurtosis": 16.796319639411514,
        "return_acf_1": -0.1897592474883644,
        "abs_return_acf_1": 0.39990227592501465,
        "abs_return_acf_5": 0.3820286115716784,
        "abs_return_acf_20": 0.34768581688820455,
        "quantile_01": -0.07315511752582349,
        "quantile_99": 0.056938734049457325,
        "hill_tail_index": 2.1385876195040034
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02726350059278625,
        "excess_kurtosis": 18.029054529444572,
        "return_acf_1": -0.3532797254543919,
        "abs_return_acf_1": 0.5041927844193775,
        "abs_return_acf_5": 0.425970846465533,
        "abs_return_acf_20": 0.33724896142750044,
        "quantile_01": -0.08880299029531924,
        "quantile_99": 0.0994218890649436,
        "hill_tail_index": 3.0566626898567217
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01969054536005936,
        "excess_kurtosis": 5.792239699082721,
        "return_acf_1": -0.19147471600624608,
        "abs_return_acf_1": 0.31253635001096236,
        "abs_return_acf_5": 0.3413190996262039,
        "abs_return_acf_20": 0.3035319415946033,
        "quantile_01": -0.05837769661778171,
        "quantile_99": 0.05987490228199199,
        "hill_tail_index": 4.075270408902399
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022656034902632793,
        "excess_kurtosis": 11.894239321204731,
        "return_acf_1": -0.20188784640134566,
        "abs_return_acf_1": 0.4287837685843501,
        "abs_return_acf_5": 0.29782413217838055,
        "abs_return_acf_20": 0.3366242013300393,
        "quantile_01": -0.06690881539928614,
        "quantile_99": 0.06378764620621155,
        "hill_tail_index": 2.79291095465181
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021959566832789705,
        "excess_kurtosis": 10.147866760631548,
        "return_acf_1": -0.2601594572092402,
        "abs_return_acf_1": 0.43692206377905685,
        "abs_return_acf_5": 0.42972202514477575,
        "abs_return_acf_20": 0.31271859756983467,
        "quantile_01": -0.07499812565985445,
        "quantile_99": 0.06304866175527109,
        "hill_tail_index": 2.8165898024222376
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02141815812632212,
        "excess_kurtosis": 9.96087846460876,
        "return_acf_1": -0.11547731976843656,
        "abs_return_acf_1": 0.3504307264909863,
        "abs_return_acf_5": 0.3564954630358698,
        "abs_return_acf_20": 0.2829676243578397,
        "quantile_01": -0.06485698783472059,
        "quantile_99": 0.059867720706544704,
        "hill_tail_index": 3.0297676122753114
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020602253611426185,
        "excess_kurtosis": 11.85406289228427,
        "return_acf_1": -0.19657145309617022,
        "abs_return_acf_1": 0.3178223212059328,
        "abs_return_acf_5": 0.3834753794856798,
        "abs_return_acf_20": 0.28579114743542294,
        "quantile_01": -0.058422641355836726,
        "quantile_99": 0.05464996075500603,
        "hill_tail_index": 3.0565705062281334
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023247534009526446,
        "excess_kurtosis": 15.231462973969652,
        "return_acf_1": -0.17821000685000676,
        "abs_return_acf_1": 0.3392074233443811,
        "abs_return_acf_5": 0.3900975735366054,
        "abs_return_acf_20": 0.3331742391589308,
        "quantile_01": -0.0757646869332011,
        "quantile_99": 0.065535389208931,
        "hill_tail_index": 2.542283255638052
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021136685805302317,
        "excess_kurtosis": 6.7790632879555,
        "return_acf_1": -0.2118169805130879,
        "abs_return_acf_1": 0.2964391614175917,
        "abs_return_acf_5": 0.2465336456842114,
        "abs_return_acf_20": 0.23621475758717483,
        "quantile_01": -0.06115303618436579,
        "quantile_99": 0.0692730149167875,
        "hill_tail_index": 3.539374192439245
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02085406586526153,
        "excess_kurtosis": 15.197961659512895,
        "return_acf_1": -0.19464934494565453,
        "abs_return_acf_1": 0.3578829750189916,
        "abs_return_acf_5": 0.3832068849222304,
        "abs_return_acf_20": 0.3065037261630204,
        "quantile_01": -0.06928543456769215,
        "quantile_99": 0.05309742955949849,
        "hill_tail_index": 2.6955412358990647
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020055292721214295,
        "excess_kurtosis": 7.325883191316608,
        "return_acf_1": -0.18099493249480714,
        "abs_return_acf_1": 0.25714262114596087,
        "abs_return_acf_5": 0.31757949344720565,
        "abs_return_acf_20": 0.22787223230393183,
        "quantile_01": -0.06102303428346401,
        "quantile_99": 0.05281618253356158,
        "hill_tail_index": 3.838052659213497
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023742904540208006,
        "excess_kurtosis": 19.93896726840082,
        "return_acf_1": -0.22228762709428843,
        "abs_return_acf_1": 0.41565348298822313,
        "abs_return_acf_5": 0.46499592650336047,
        "abs_return_acf_20": 0.34888066156341685,
        "quantile_01": -0.07339482690682313,
        "quantile_99": 0.057699110562779266,
        "hill_tail_index": 2.015205929336602
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022152737082136914,
        "excess_kurtosis": 13.226546896251907,
        "return_acf_1": -0.15679249435202752,
        "abs_return_acf_1": 0.3367023157678266,
        "abs_return_acf_5": 0.38357530014882113,
        "abs_return_acf_20": 0.3507273558444047,
        "quantile_01": -0.07026688680547798,
        "quantile_99": 0.05593154420392294,
        "hill_tail_index": 2.4840490890656306
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021312262831547128,
        "excess_kurtosis": 10.220799710174695,
        "return_acf_1": -0.24174268015805042,
        "abs_return_acf_1": 0.3128114735227449,
        "abs_return_acf_5": 0.3655283234702553,
        "abs_return_acf_20": 0.3216410849104496,
        "quantile_01": -0.07242788681388303,
        "quantile_99": 0.06726466460661296,
        "hill_tail_index": 3.601332237261788
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02095837744778446,
        "excess_kurtosis": 11.23127526404443,
        "return_acf_1": -0.23165269208851796,
        "abs_return_acf_1": 0.44625518206810594,
        "abs_return_acf_5": 0.46900240516848585,
        "abs_return_acf_20": 0.3100251825137292,
        "quantile_01": -0.06948735607021439,
        "quantile_99": 0.06626406490424491,
        "hill_tail_index": 3.27029455138839
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021801350369228922,
        "excess_kurtosis": 10.32287031856372,
        "return_acf_1": -0.16253758641855798,
        "abs_return_acf_1": 0.3201944295010369,
        "abs_return_acf_5": 0.3435600339182187,
        "abs_return_acf_20": 0.3172519659727928,
        "quantile_01": -0.07012345551252695,
        "quantile_99": 0.05980168154906362,
        "hill_tail_index": 3.284246599718335
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02011367113411161,
        "excess_kurtosis": 7.326276298954241,
        "return_acf_1": -0.20841693274736772,
        "abs_return_acf_1": 0.39207014929173917,
        "abs_return_acf_5": 0.36307850738455943,
        "abs_return_acf_20": 0.31182352691015813,
        "quantile_01": -0.0628229468390294,
        "quantile_99": 0.05856756819377225,
        "hill_tail_index": 3.8610150978686
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019687783707907146,
        "excess_kurtosis": 10.990890256686228,
        "return_acf_1": -0.1567599758522346,
        "abs_return_acf_1": 0.32657184715580606,
        "abs_return_acf_5": 0.37730061874214216,
        "abs_return_acf_20": 0.23260692594500543,
        "quantile_01": -0.0625637738550392,
        "quantile_99": 0.05352289070970419,
        "hill_tail_index": 2.780520520208262
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022504004763318024,
        "excess_kurtosis": 17.083170075670363,
        "return_acf_1": -0.17785146378961883,
        "abs_return_acf_1": 0.37589545875507857,
        "abs_return_acf_5": 0.42531193651957,
        "abs_return_acf_20": 0.31388097799908277,
        "quantile_01": -0.06828892591330313,
        "quantile_99": 0.07061510846697834,
        "hill_tail_index": 2.629300806339399
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
