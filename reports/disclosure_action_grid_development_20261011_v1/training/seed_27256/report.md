# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27256
Run ID: `d23cc944d6da02f13cf5d2fe09f4d9f373c983b55a43fd7044ee8237356e8bbc`
Result fingerprint: `366ac6ba5250568c1be52a7909232a412337866b3b22eedb76718786f1d6546e`

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
    "equal_weight_sd": -0.8052142857142826,
    "equal_weight_raw": -12.078214285714239,
    "fixed_start_cap_weight_sd": -0.7644815329553282,
    "fixed_start_cap_weight_raw": -11.467222994329921,
    "end_cap_weight_sd": -0.7686767779438268,
    "end_cap_weight_raw": -11.530151669157403
  },
  "full_period_change": {
    "equal_weight_sd": -1.2033214285714238,
    "equal_weight_raw": -18.049821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1256335978835932,
    "inflation_mean_sd": 0.5227486772486774
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.14625852358381847,
    "equal_weight_raw": 2.1938778537572765,
    "fixed_start_cap_weight_sd": 0.18738263049991608,
    "fixed_start_cap_weight_raw": 2.81073945749874,
    "end_cap_weight_sd": 0.1833336997193591,
    "end_cap_weight_raw": 2.750005495790386
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7823809523809494,
      "change_raw": -11.735714285714241,
      "decay_adjusted_gain_sd": 0.17000000000000304
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6673809523809493,
      "change_raw": -10.01071428571424,
      "decay_adjusted_gain_sd": 0.28500000000000303
    },
    "small": {
      "count": 18,
      "change_sd": -0.8779365079365047,
      "change_raw": -13.16904761904757,
      "decay_adjusted_gain_sd": 0.07293087263969536
    },
    "large_minus_small_sd": 0.09555555555555528,
    "large_minus_small_raw": 1.4333333333333291
  },
  "inflation": {
    "initial_mean_sd": 0.22375,
    "final_mean_sd": 0.51375,
    "mean_sd": 0.36682660283097424,
    "mean_absolute_raw_gap": 5.502399042464614,
    "final_absolute_raw_gap": 7.70625,
    "mean_range_fraction": 0.05502399042464614
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.20666666666666667,
    "initial_wealth_share": 0.15056238184456056,
    "final_wealth_share": 0.2033545068221983
  },
  "pricing_slope": {
    "mean": -0.0010099436462543917,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.02804846375203862,
    "real_improvement_cost": 0.01674560221400948,
    "washing_cost": 0.01130286153802914,
    "fine_transfer": 0.013992764882580127,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.042041228634618746,
    "resource_cost_fraction_initial_cap": 0.0009349487917346205,
    "private_net_outflow_fraction_initial_cap": 0.0014013742878206245,
    "fine_transfer_fraction_initial_cap": 0.0004664254960860041,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010103532247007908,
    "unapplied_final_day_resource_cost": 0.0008453682860468651
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 156.43479608381912,
    "beneficial_raw_gain_per_resource_cost": 2346.5219412572865,
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
    "accrued_cost": 2.925307789265846,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.05088268692463099,
    "accrued_cost_fraction_initial_cap": 0.09751025964219484,
    "mean_contract_rate": 0.041006292374734736,
    "maximum_ledger_error": 6.098637220230962e-20
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
    "maximum_relative_cash_error": 2.770023728203318e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.23792786483994785,
      "maximum": -0.10168874232463157,
      "mean": -0.1893877486009412,
      "median": -0.18988569453788834,
      "quantile_05": -0.237115735660959,
      "quantile_95": -0.1136946458805535
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
      "minimum": 0.40200407823846285,
      "maximum": 0.8054549065619413,
      "mean": 0.6597219992925804,
      "median": 0.6683434544830363,
      "quantile_05": 0.5173975744789995,
      "quantile_95": 0.7735799268355705
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
        "daily_volatility": 0.018361756043346642,
        "excess_kurtosis": 9.663805695189362,
        "return_acf_1": -0.20622759698284873,
        "abs_return_acf_1": 0.41776650089247586,
        "abs_return_acf_5": 0.373536769159275,
        "abs_return_acf_20": 0.24497794877924176,
        "quantile_01": -0.06489840685203604,
        "quantile_99": 0.046945015649242736,
        "hill_tail_index": 2.4238841935775586
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019691006443287522,
        "excess_kurtosis": 7.470963069407835,
        "return_acf_1": -0.17039300499140791,
        "abs_return_acf_1": 0.34749327969077975,
        "abs_return_acf_5": 0.363299360066621,
        "abs_return_acf_20": 0.2673851326107489,
        "quantile_01": -0.06263183835513739,
        "quantile_99": 0.062204075166725256,
        "hill_tail_index": 3.879840686682332
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018618560261137337,
        "excess_kurtosis": 5.97055754796137,
        "return_acf_1": -0.19822402122054217,
        "abs_return_acf_1": 0.45730126686206873,
        "abs_return_acf_5": 0.4129629170679777,
        "abs_return_acf_20": 0.3327164904182634,
        "quantile_01": -0.05310773677074885,
        "quantile_99": 0.05374788665209909,
        "hill_tail_index": 3.27978192189994
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02224842808677042,
        "excess_kurtosis": 9.675757973485416,
        "return_acf_1": -0.20178425634197114,
        "abs_return_acf_1": 0.47817950182479096,
        "abs_return_acf_5": 0.525825793559484,
        "abs_return_acf_20": 0.3802746410900682,
        "quantile_01": -0.07420390179172409,
        "quantile_99": 0.06858233652027039,
        "hill_tail_index": 3.300415744854903
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02111268852280731,
        "excess_kurtosis": 8.77100828147994,
        "return_acf_1": -0.19005850253770235,
        "abs_return_acf_1": 0.45593781255116933,
        "abs_return_acf_5": 0.4347034623170456,
        "abs_return_acf_20": 0.3382596669480711,
        "quantile_01": -0.06859468317292747,
        "quantile_99": 0.059588367469661126,
        "hill_tail_index": 2.9839246667510095
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01935546304610032,
        "excess_kurtosis": 8.679936331722374,
        "return_acf_1": -0.1806994740131372,
        "abs_return_acf_1": 0.2764285058445567,
        "abs_return_acf_5": 0.27923210012698474,
        "abs_return_acf_20": 0.2725879006079576,
        "quantile_01": -0.06444351776148738,
        "quantile_99": 0.05665244598430557,
        "hill_tail_index": 3.508984115112546
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018637698796904703,
        "excess_kurtosis": 6.60801508550842,
        "return_acf_1": -0.23718637441406426,
        "abs_return_acf_1": 0.37492792529127794,
        "abs_return_acf_5": 0.4071296163610661,
        "abs_return_acf_20": 0.2743876494307248,
        "quantile_01": -0.06324770197211244,
        "quantile_99": 0.04613379705369604,
        "hill_tail_index": 2.805470438194369
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022631240086238517,
        "excess_kurtosis": 17.13522743247466,
        "return_acf_1": -0.10168874232463157,
        "abs_return_acf_1": 0.4324261239657582,
        "abs_return_acf_5": 0.4224055400167773,
        "abs_return_acf_20": 0.3270508785180235,
        "quantile_01": -0.0687608158272268,
        "quantile_99": 0.06717448957697615,
        "hill_tail_index": 3.158562527678165
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022646098958888704,
        "excess_kurtosis": 17.00546673841273,
        "return_acf_1": -0.20635586828544816,
        "abs_return_acf_1": 0.592905366344951,
        "abs_return_acf_5": 0.44915588122829125,
        "abs_return_acf_20": 0.3354293179970459,
        "quantile_01": -0.07038756154145691,
        "quantile_99": 0.06350223646406483,
        "hill_tail_index": 2.8421733590781044
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0201462623278313,
        "excess_kurtosis": 6.3010090350029095,
        "return_acf_1": -0.23792786483994785,
        "abs_return_acf_1": 0.44956091346354704,
        "abs_return_acf_5": 0.4206262664355424,
        "abs_return_acf_20": 0.3675705846920977,
        "quantile_01": -0.06424112347609962,
        "quantile_99": 0.06538237650276901,
        "hill_tail_index": 4.493878621425429
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02071237846028851,
        "excess_kurtosis": 9.635072859111242,
        "return_acf_1": -0.18770005565466544,
        "abs_return_acf_1": 0.47236741699924606,
        "abs_return_acf_5": 0.45912677836840593,
        "abs_return_acf_20": 0.2651290757773882,
        "quantile_01": -0.07012411366789886,
        "quantile_99": 0.05824592992960662,
        "hill_tail_index": 3.1030942819114644
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020832870986977392,
        "excess_kurtosis": 8.510070020308671,
        "return_acf_1": -0.15519771974513868,
        "abs_return_acf_1": 0.4083665497929846,
        "abs_return_acf_5": 0.3144523306452014,
        "abs_return_acf_20": 0.3070447920945408,
        "quantile_01": -0.07312596238124826,
        "quantile_99": 0.060335243161158944,
        "hill_tail_index": 3.6925320283416405
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021838736347742284,
        "excess_kurtosis": 8.078789494665088,
        "return_acf_1": -0.23702939940716372,
        "abs_return_acf_1": 0.4884805793053852,
        "abs_return_acf_5": 0.43831514753637874,
        "abs_return_acf_20": 0.2973344528950682,
        "quantile_01": -0.07742266228324789,
        "quantile_99": 0.06504014249434881,
        "hill_tail_index": 3.30284737178981
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02063921227976377,
        "excess_kurtosis": 9.254631243723425,
        "return_acf_1": -0.10389078715837141,
        "abs_return_acf_1": 0.40133871392536236,
        "abs_return_acf_5": 0.40470853772641857,
        "abs_return_acf_20": 0.3084305492354626,
        "quantile_01": -0.06273321750780206,
        "quantile_99": 0.06714081271339806,
        "hill_tail_index": 3.2974146177243835
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020815427121420055,
        "excess_kurtosis": 9.612139926961108,
        "return_acf_1": -0.18766016534221042,
        "abs_return_acf_1": 0.3725110398977615,
        "abs_return_acf_5": 0.3271977392656728,
        "abs_return_acf_20": 0.3150175917314719,
        "quantile_01": -0.0757734784428948,
        "quantile_99": 0.06000060363899756,
        "hill_tail_index": 3.7409969837681043
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019101133225583086,
        "excess_kurtosis": 8.135330126310558,
        "return_acf_1": -0.1724837764973088,
        "abs_return_acf_1": 0.2798512038906381,
        "abs_return_acf_5": 0.31442826988145695,
        "abs_return_acf_20": 0.3142080916798743,
        "quantile_01": -0.05885036118530243,
        "quantile_99": 0.05037800683497711,
        "hill_tail_index": 3.334375699191315
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020681707717915387,
        "excess_kurtosis": 7.3730954510247795,
        "return_acf_1": -0.23498028939629023,
        "abs_return_acf_1": 0.4864131680384807,
        "abs_return_acf_5": 0.4635067172255304,
        "abs_return_acf_20": 0.315057197778973,
        "quantile_01": -0.0729230757445524,
        "quantile_99": 0.06260588662979259,
        "hill_tail_index": 3.7959427696750554
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.023066824532902992,
        "excess_kurtosis": 12.028079723823746,
        "return_acf_1": -0.18287239563705202,
        "abs_return_acf_1": 0.5205620412062331,
        "abs_return_acf_5": 0.43399896140316546,
        "abs_return_acf_20": 0.33666718886860614,
        "quantile_01": -0.07882210008825062,
        "quantile_99": 0.06455689989026885,
        "hill_tail_index": 3.0068780548710925
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020646647101972372,
        "excess_kurtosis": 7.648552727809751,
        "return_acf_1": -0.20616046026309195,
        "abs_return_acf_1": 0.49242778245342234,
        "abs_return_acf_5": 0.48569879871154703,
        "abs_return_acf_20": 0.3387329891435226,
        "quantile_01": -0.0695752506811862,
        "quantile_99": 0.06366253371703529,
        "hill_tail_index": 3.625780748616949
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02049864785123175,
        "excess_kurtosis": 10.56513001530285,
        "return_acf_1": -0.20807080475151943,
        "abs_return_acf_1": 0.3937376802618308,
        "abs_return_acf_5": 0.35128613841921824,
        "abs_return_acf_20": 0.2606644616134908,
        "quantile_01": -0.06639195746484687,
        "quantile_99": 0.05546035797574904,
        "hill_tail_index": 3.692784429236156
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02250889566875171,
        "excess_kurtosis": 10.718765615643994,
        "return_acf_1": -0.18361180022160234,
        "abs_return_acf_1": 0.49705139103563456,
        "abs_return_acf_5": 0.49326065287256254,
        "abs_return_acf_20": 0.3154919814006557,
        "quantile_01": -0.0727192158904829,
        "quantile_99": 0.07206457504114401,
        "hill_tail_index": 3.332333890462224
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020013273712784517,
        "excess_kurtosis": 10.16438077383978,
        "return_acf_1": -0.2077952236417618,
        "abs_return_acf_1": 0.35563256121834164,
        "abs_return_acf_5": 0.33457473186406356,
        "abs_return_acf_20": 0.2872422851043616,
        "quantile_01": -0.06616294634804384,
        "quantile_99": 0.05278345378353737,
        "hill_tail_index": 2.8885018833642278
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021857410756218238,
        "excess_kurtosis": 10.46632883942321,
        "return_acf_1": -0.18902154581634478,
        "abs_return_acf_1": 0.503423413006121,
        "abs_return_acf_5": 0.4419857903718272,
        "abs_return_acf_20": 0.3255479182798732,
        "quantile_01": -0.07264426583185458,
        "quantile_99": 0.05921224097077107,
        "hill_tail_index": 3.0819708597996636
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023064730021429267,
        "excess_kurtosis": 17.84252221445695,
        "return_acf_1": -0.17834149600144314,
        "abs_return_acf_1": 0.4851506348883368,
        "abs_return_acf_5": 0.45794525144134335,
        "abs_return_acf_20": 0.3090287984404562,
        "quantile_01": -0.0742604144453698,
        "quantile_99": 0.06580456110095316,
        "hill_tail_index": 2.6334347631135087
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019977648709611696,
        "excess_kurtosis": 9.304256840885147,
        "return_acf_1": -0.12567713987433146,
        "abs_return_acf_1": 0.3953426377078188,
        "abs_return_acf_5": 0.3938877589507468,
        "abs_return_acf_20": 0.27744650588021086,
        "quantile_01": -0.0665735715769171,
        "quantile_99": 0.04592831246523859,
        "hill_tail_index": 3.6423361027479912
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02144350362276573,
        "excess_kurtosis": 16.05052634080613,
        "return_acf_1": -0.18971288653807433,
        "abs_return_acf_1": 0.34818498377075413,
        "abs_return_acf_5": 0.3857186553327705,
        "abs_return_acf_20": 0.2826300048363709,
        "quantile_01": -0.07069168436406682,
        "quantile_99": 0.057754502885130884,
        "hill_tail_index": 2.6589321002794097
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021074615090641857,
        "excess_kurtosis": 10.614590134162878,
        "return_acf_1": -0.2253834900417777,
        "abs_return_acf_1": 0.46843258673786997,
        "abs_return_acf_5": 0.41995329592276937,
        "abs_return_acf_20": 0.366463339813294,
        "quantile_01": -0.06365192167754909,
        "quantile_99": 0.06537794155851581,
        "hill_tail_index": 3.129206298457377
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020640688399101405,
        "excess_kurtosis": 9.438272839776701,
        "return_acf_1": -0.1986861746925321,
        "abs_return_acf_1": 0.40737924531411757,
        "abs_return_acf_5": 0.39695825071295937,
        "abs_return_acf_20": 0.3086575576420395,
        "quantile_01": -0.07193013225218405,
        "quantile_99": 0.06509078351764833,
        "hill_tail_index": 3.6292173106518484
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020789508538722152,
        "excess_kurtosis": 10.601897462240931,
        "return_acf_1": -0.14075072564230973,
        "abs_return_acf_1": 0.41888329826755477,
        "abs_return_acf_5": 0.43767445102115465,
        "abs_return_acf_20": 0.27187581434911723,
        "quantile_01": -0.062364499680458034,
        "quantile_99": 0.06015170868157961,
        "hill_tail_index": 2.8503622756666624
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021805992948846255,
        "excess_kurtosis": 12.581533266523618,
        "return_acf_1": -0.23606041575354594,
        "abs_return_acf_1": 0.4966874993563061,
        "abs_return_acf_5": 0.42259769589010876,
        "abs_return_acf_20": 0.3401112710767249,
        "quantile_01": -0.07308020922735928,
        "quantile_99": 0.06199304032427649,
        "hill_tail_index": 2.6584683991458014
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
