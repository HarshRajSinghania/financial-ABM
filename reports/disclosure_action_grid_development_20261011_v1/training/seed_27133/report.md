# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27133
Run ID: `39b627e343f8ce440fc68657a1ffc2651c8521e3b6003ecb55a06ae336308bda`
Result fingerprint: `ee87cc5d6a12d02b39ac7504143b53f3cb2701442a95dcf313281ffabc86724b`

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
    "equal_weight_sd": -0.6567142857142824,
    "equal_weight_raw": -9.850714285714236,
    "fixed_start_cap_weight_sd": -0.5894608693152218,
    "fixed_start_cap_weight_raw": -8.841913039728325,
    "end_cap_weight_sd": -0.5619287212441412,
    "end_cap_weight_raw": -8.42893081866212
  },
  "full_period_change": {
    "equal_weight_sd": -1.0034880952380905,
    "equal_weight_raw": -15.052321428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9384755291005247,
    "inflation_mean_sd": 0.5293888888888889
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2956666666666699,
    "equal_weight_raw": 4.435000000000048,
    "fixed_start_cap_weight_sd": 0.3629200830657304,
    "fixed_start_cap_weight_raw": 5.443801245985957,
    "end_cap_weight_sd": 0.3904522311368111,
    "end_cap_weight_raw": 5.856783467052166
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.4973809523809492,
      "change_raw": -7.460714285714238,
      "decay_adjusted_gain_sd": 0.455000000000003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6193253968253937,
      "change_raw": -9.289880952380905,
      "decay_adjusted_gain_sd": 0.33305555555555866
    },
    "small": {
      "count": 18,
      "change_sd": -0.7019642857142825,
      "change_raw": -10.529464285714237,
      "decay_adjusted_gain_sd": 0.25041666666666995
    },
    "large_minus_small_sd": 0.20458333333333328,
    "large_minus_small_raw": 3.068749999999999
  },
  "inflation": {
    "initial_mean_sd": 0.28075,
    "final_mean_sd": 0.5738333333333333,
    "mean_sd": 0.4247575631418262,
    "mean_absolute_raw_gap": 6.371363447127395,
    "final_absolute_raw_gap": 8.6075,
    "mean_range_fraction": 0.06371363447127396
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.35333333333333333,
    "initial_wealth_share": 0.33034706646097617,
    "final_wealth_share": 0.36815895005948224
  },
  "pricing_slope": {
    "mean": -0.00266835292896931,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.055612874324153794,
    "real_improvement_cost": 0.03626554504293587,
    "washing_cost": 0.019347329281217913,
    "fine_transfer": 0.003393743034911309,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0590066173590651,
    "resource_cost_fraction_initial_cap": 0.0018537624774717933,
    "private_net_outflow_fraction_initial_cap": 0.00196688724530217,
    "fine_transfer_fraction_initial_cap": 0.00011312476783037698,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.014711740374293654,
    "unapplied_final_day_resource_cost": 0.0009988908555100566
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 159.49544251748335,
    "beneficial_raw_gain_per_resource_cost": 2392.4316377622504,
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
    "accrued_cost": 3.4227391657174233,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.44654868952694676,
    "accrued_cost_fraction_initial_cap": 0.11409130552391412,
    "mean_contract_rate": 0.04504568268711461,
    "maximum_ledger_error": 1.6263032587282567e-19
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
    "maximum_relative_cash_error": 1.3521717185915399e-15,
    "maximum_absolute_share_error": 1.3322676295501878e-15,
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
      "minimum": -0.2905784268825364,
      "maximum": -0.10106530473332377,
      "mean": -0.18209946362395066,
      "median": -0.1796329639720299,
      "quantile_05": -0.25101459581351476,
      "quantile_95": -0.11544516543471493
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
      "minimum": 0.26185323262950777,
      "maximum": 0.8072833218629525,
      "mean": 0.45141913220432767,
      "median": 0.41345331146778047,
      "quantile_05": 0.2907556701083822,
      "quantile_95": 0.7345375732679361
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
        "daily_volatility": 0.020241944213119187,
        "excess_kurtosis": 5.8683162336087555,
        "return_acf_1": -0.17041730246722764,
        "abs_return_acf_1": 0.3402979308301605,
        "abs_return_acf_5": 0.31606953298241125,
        "abs_return_acf_20": 0.2392972832553692,
        "quantile_01": -0.06509863877764879,
        "quantile_99": 0.0581169156005558,
        "hill_tail_index": 3.5477415666700254
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021203302842642307,
        "excess_kurtosis": 10.256006191513249,
        "return_acf_1": -0.15503984869007997,
        "abs_return_acf_1": 0.39180863433463936,
        "abs_return_acf_5": 0.33001144301531754,
        "abs_return_acf_20": 0.29029902395739315,
        "quantile_01": -0.06791297635006269,
        "quantile_99": 0.05727747935368899,
        "hill_tail_index": 2.7583435991744656
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02268705324560577,
        "excess_kurtosis": 9.621458518167579,
        "return_acf_1": -0.2594410200561493,
        "abs_return_acf_1": 0.4334102012318729,
        "abs_return_acf_5": 0.37977516329975697,
        "abs_return_acf_20": 0.3582294544866278,
        "quantile_01": -0.08086213100247731,
        "quantile_99": 0.06386705527693597,
        "hill_tail_index": 3.140796445930356
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018559793174366263,
        "excess_kurtosis": 10.484498929754348,
        "return_acf_1": -0.10106530473332377,
        "abs_return_acf_1": 0.31186299968134285,
        "abs_return_acf_5": 0.36187446917488225,
        "abs_return_acf_20": 0.2872337862065062,
        "quantile_01": -0.054084208692042425,
        "quantile_99": 0.04560698873394492,
        "hill_tail_index": 2.374818686319548
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01768717813001696,
        "excess_kurtosis": 3.4054487278905885,
        "return_acf_1": -0.24071563285029482,
        "abs_return_acf_1": 0.3112488364829815,
        "abs_return_acf_5": 0.2519482981624909,
        "abs_return_acf_20": 0.18966815429012343,
        "quantile_01": -0.05334483154223573,
        "quantile_99": 0.049820917649646836,
        "hill_tail_index": 4.749781911669942
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021963771107075862,
        "excess_kurtosis": 8.349759704894996,
        "return_acf_1": -0.2358673248596032,
        "abs_return_acf_1": 0.3775088231939096,
        "abs_return_acf_5": 0.3404760345654804,
        "abs_return_acf_20": 0.3118478280407432,
        "quantile_01": -0.06913028509543645,
        "quantile_99": 0.056741331360346085,
        "hill_tail_index": 2.3534581321983876
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020026906751100314,
        "excess_kurtosis": 6.202107463553034,
        "return_acf_1": -0.22973992102929913,
        "abs_return_acf_1": 0.4311780756890047,
        "abs_return_acf_5": 0.3538825818752833,
        "abs_return_acf_20": 0.3080704501228701,
        "quantile_01": -0.06778050316654761,
        "quantile_99": 0.057516242914203104,
        "hill_tail_index": 3.4040587959466078
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017553337267666377,
        "excess_kurtosis": 4.698331123433518,
        "return_acf_1": -0.15173486110131243,
        "abs_return_acf_1": 0.33999525375166656,
        "abs_return_acf_5": 0.26585800266279525,
        "abs_return_acf_20": 0.2754857913493382,
        "quantile_01": -0.049371502846412146,
        "quantile_99": 0.0508963708935623,
        "hill_tail_index": 3.8066577131143635
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02324010465055977,
        "excess_kurtosis": 6.901340213973098,
        "return_acf_1": -0.18031780113444423,
        "abs_return_acf_1": 0.4210778275611276,
        "abs_return_acf_5": 0.3814772049208803,
        "abs_return_acf_20": 0.35009556941182557,
        "quantile_01": -0.0859315644669956,
        "quantile_99": 0.06914336634265077,
        "hill_tail_index": 5.39013240470123
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019476680158289805,
        "excess_kurtosis": 4.999647419051478,
        "return_acf_1": -0.12283509137728739,
        "abs_return_acf_1": 0.3454720357282921,
        "abs_return_acf_5": 0.34669916037718085,
        "abs_return_acf_20": 0.2330097715163819,
        "quantile_01": -0.06585277721889173,
        "quantile_99": 0.053966412143273676,
        "hill_tail_index": 3.444114470072992
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020659138252771582,
        "excess_kurtosis": 4.6007442489879695,
        "return_acf_1": -0.18349730701730993,
        "abs_return_acf_1": 0.39733086617303714,
        "abs_return_acf_5": 0.4046083258139898,
        "abs_return_acf_20": 0.32659511762554044,
        "quantile_01": -0.061078696422171425,
        "quantile_99": 0.06736183093443054,
        "hill_tail_index": 4.563324131361882
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021696214449231536,
        "excess_kurtosis": 3.6207494838730137,
        "return_acf_1": -0.17894812680961558,
        "abs_return_acf_1": 0.3358401362546074,
        "abs_return_acf_5": 0.32804571002776933,
        "abs_return_acf_20": 0.30766965448665934,
        "quantile_01": -0.06624934577793325,
        "quantile_99": 0.057123670026589225,
        "hill_tail_index": 4.303524036302006
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019946606193183992,
        "excess_kurtosis": 5.157217359567921,
        "return_acf_1": -0.14994331209557152,
        "abs_return_acf_1": 0.33601375814062767,
        "abs_return_acf_5": 0.3333767520889429,
        "abs_return_acf_20": 0.25313436938787387,
        "quantile_01": -0.06660472212109658,
        "quantile_99": 0.05628563998842916,
        "hill_tail_index": 3.4692362465632054
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023345698449510337,
        "excess_kurtosis": 10.960014213210377,
        "return_acf_1": -0.18565279889508485,
        "abs_return_acf_1": 0.46094487559488256,
        "abs_return_acf_5": 0.4296764478282077,
        "abs_return_acf_20": 0.3659106206018637,
        "quantile_01": -0.08482165944433909,
        "quantile_99": 0.079410788012847,
        "hill_tail_index": 5.164684917699879
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.023506559599818642,
        "excess_kurtosis": 9.022798711255255,
        "return_acf_1": -0.21471520434270328,
        "abs_return_acf_1": 0.44935882756728446,
        "abs_return_acf_5": 0.4296339525437428,
        "abs_return_acf_20": 0.32634066521187477,
        "quantile_01": -0.08648222789701986,
        "quantile_99": 0.06901719893237786,
        "hill_tail_index": 3.7891694227633
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0205804245038966,
        "excess_kurtosis": 10.543192639046346,
        "return_acf_1": -0.23024082578071614,
        "abs_return_acf_1": 0.4105904725828018,
        "abs_return_acf_5": 0.36923209206016394,
        "abs_return_acf_20": 0.4049399430596396,
        "quantile_01": -0.06008343990015195,
        "quantile_99": 0.05869282814155878,
        "hill_tail_index": 3.323360620653954
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020506055559006205,
        "excess_kurtosis": 4.128696561454702,
        "return_acf_1": -0.18726790221672662,
        "abs_return_acf_1": 0.35227575639919717,
        "abs_return_acf_5": 0.3372181135857841,
        "abs_return_acf_20": 0.29960710790988443,
        "quantile_01": -0.06153646457360888,
        "quantile_99": 0.054271382976029674,
        "hill_tail_index": 3.922780782489569
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018438298599915904,
        "excess_kurtosis": 7.5695818428715445,
        "return_acf_1": -0.10944393277603173,
        "abs_return_acf_1": 0.36965528919524876,
        "abs_return_acf_5": 0.36133294189623205,
        "abs_return_acf_20": 0.27645000806579834,
        "quantile_01": -0.060290257841031474,
        "quantile_99": 0.04156024023578881,
        "hill_tail_index": 2.590125079733324
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02311899286811526,
        "excess_kurtosis": 8.502228327546009,
        "return_acf_1": -0.2905784268825364,
        "abs_return_acf_1": 0.4780940814418635,
        "abs_return_acf_5": 0.39734833856184104,
        "abs_return_acf_20": 0.34143891088674194,
        "quantile_01": -0.07852835745215417,
        "quantile_99": 0.07462237049704391,
        "hill_tail_index": 4.54402745360392
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01769666564141739,
        "excess_kurtosis": 4.835029083914566,
        "return_acf_1": -0.17318790959718,
        "abs_return_acf_1": 0.3140514286156543,
        "abs_return_acf_5": 0.2856132544062557,
        "abs_return_acf_20": 0.1702111690219433,
        "quantile_01": -0.05374703045439654,
        "quantile_99": 0.05705688504878428,
        "hill_tail_index": 4.0584234196842175
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0159543682230119,
        "excess_kurtosis": 2.804958408373574,
        "return_acf_1": -0.168163001651452,
        "abs_return_acf_1": 0.26527750009199247,
        "abs_return_acf_5": 0.22882999981377736,
        "abs_return_acf_20": 0.21224542918378134,
        "quantile_01": -0.04191143374051614,
        "quantile_99": 0.042856181597830084,
        "hill_tail_index": 3.8518012879224433
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020229963631198757,
        "excess_kurtosis": 6.464155323422682,
        "return_acf_1": -0.1227800053508832,
        "abs_return_acf_1": 0.4089252829749477,
        "abs_return_acf_5": 0.3996028410419011,
        "abs_return_acf_20": 0.32951600975144046,
        "quantile_01": -0.06562080739206107,
        "quantile_99": 0.06069342886413674,
        "hill_tail_index": 3.9381535895248136
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021642728406795,
        "excess_kurtosis": 9.652626018354459,
        "return_acf_1": -0.14929372046168915,
        "abs_return_acf_1": 0.40681480887956134,
        "abs_return_acf_5": 0.4084054097589759,
        "abs_return_acf_20": 0.30844106713228225,
        "quantile_01": -0.06671577637917672,
        "quantile_99": 0.06146877211323936,
        "hill_tail_index": 3.205775907106303
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02018488995517209,
        "excess_kurtosis": 5.608758115950932,
        "return_acf_1": -0.24020304690448063,
        "abs_return_acf_1": 0.37204547654450676,
        "abs_return_acf_5": 0.258542431920104,
        "abs_return_acf_20": 0.26325092994734345,
        "quantile_01": -0.06912587969271,
        "quantile_99": 0.05248161207148971,
        "hill_tail_index": 3.144618836045159
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01831652029127272,
        "excess_kurtosis": 6.290677052441453,
        "return_acf_1": -0.1410801509504444,
        "abs_return_acf_1": 0.3833367555827075,
        "abs_return_acf_5": 0.3634586347142631,
        "abs_return_acf_20": 0.26139429301479017,
        "quantile_01": -0.055308254225151614,
        "quantile_99": 0.054365966446257234,
        "hill_tail_index": 4.184189792181806
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019757110017580546,
        "excess_kurtosis": 4.726441885865188,
        "return_acf_1": -0.2018149711619572,
        "abs_return_acf_1": 0.343901843445858,
        "abs_return_acf_5": 0.36263828247625995,
        "abs_return_acf_20": 0.27310415028401447,
        "quantile_01": -0.06488946102386638,
        "quantile_99": 0.04785142745974821,
        "hill_tail_index": 2.7202175370113877
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02084629462957006,
        "excess_kurtosis": 9.232182924182785,
        "return_acf_1": -0.20664166074752793,
        "abs_return_acf_1": 0.37347659901685165,
        "abs_return_acf_5": 0.3258848894985614,
        "abs_return_acf_20": 0.3222358735276313,
        "quantile_01": -0.064671584206117,
        "quantile_99": 0.05948289106388555,
        "hill_tail_index": 2.627287615750683
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022197468701714244,
        "excess_kurtosis": 7.103246955686272,
        "return_acf_1": -0.1480584726421524,
        "abs_return_acf_1": 0.3995312513371075,
        "abs_return_acf_5": 0.33109985018906446,
        "abs_return_acf_20": 0.3262025644977097,
        "quantile_01": -0.06635793700517814,
        "quantile_99": 0.07147843689596943,
        "hill_tail_index": 3.892766329073266
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021719339014861658,
        "excess_kurtosis": 5.559213013766904,
        "return_acf_1": -0.1966052317019796,
        "abs_return_acf_1": 0.4442314902277531,
        "abs_return_acf_5": 0.3998421748012542,
        "abs_return_acf_20": 0.3601145436184019,
        "quantile_01": -0.07247713211179452,
        "quantile_99": 0.06447557200584952,
        "hill_tail_index": 3.5617671547137646
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021298598012131627,
        "excess_kurtosis": 14.4717386765452,
        "return_acf_1": -0.13769379243345534,
        "abs_return_acf_1": 0.38058714220421375,
        "abs_return_acf_5": 0.3056288281604987,
        "abs_return_acf_20": 0.30085256028772583,
        "quantile_01": -0.06075227428691421,
        "quantile_99": 0.05561684798247753,
        "hill_tail_index": 2.5637307851823685
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
