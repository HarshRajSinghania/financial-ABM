# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27117
Run ID: `2f23f78c375d258b982f0b0c86d08841cac33cfb8c44c64a08c3a9eadb831d66`
Result fingerprint: `1ed1f10f379f1a7b3ba62305f42104be5afcab75232c41064946f1b1669edef9`

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
    "equal_weight_sd": -0.6103809523809491,
    "equal_weight_raw": -9.155714285714238,
    "fixed_start_cap_weight_sd": -0.540663532900039,
    "fixed_start_cap_weight_raw": -8.109952993500585,
    "end_cap_weight_sd": -0.5724975991659483,
    "end_cap_weight_raw": -8.587463987489224
  },
  "full_period_change": {
    "equal_weight_sd": -0.975321428571424,
    "equal_weight_raw": -14.62982142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.913762235449731,
    "inflation_mean_sd": 0.6523505291005292
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3406131298815127,
    "equal_weight_raw": 5.109196948222688,
    "fixed_start_cap_weight_sd": 0.4109585047227126,
    "fixed_start_cap_weight_raw": 6.164377570840688,
    "end_cap_weight_sd": 0.3793048001716155,
    "end_cap_weight_raw": 5.689572002574232
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.39904761904761593,
      "change_raw": -5.985714285714239,
      "decay_adjusted_gain_sd": 0.5533333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.607658730158727,
      "change_raw": -9.114880952380904,
      "decay_adjusted_gain_sd": 0.34472222222222537
    },
    "small": {
      "count": 18,
      "change_sd": -0.6469642857142825,
      "change_raw": -9.704464285714238,
      "decay_adjusted_gain_sd": 0.3031052164691856
    },
    "large_minus_small_sd": 0.24791666666666662,
    "large_minus_small_raw": 3.718749999999999
  },
  "inflation": {
    "initial_mean_sd": 0.33,
    "final_mean_sd": 0.6868333333333335,
    "mean_sd": 0.5175910352484041,
    "mean_absolute_raw_gap": 7.763865528726062,
    "final_absolute_raw_gap": 10.302499999999998,
    "mean_range_fraction": 0.07763865528726062
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.3,
    "initial_wealth_share": 0.22481435343704453,
    "final_wealth_share": 0.2944423041224376
  },
  "pricing_slope": {
    "mean": -0.001154240790730927,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.06880821758047627,
    "real_improvement_cost": 0.059970624222557035,
    "washing_cost": 0.008837593357919234,
    "fine_transfer": 0.0027988248050938545,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07160704238557013,
    "resource_cost_fraction_initial_cap": 0.0022936072526825424,
    "private_net_outflow_fraction_initial_cap": 0.0023869014128523377,
    "fine_transfer_fraction_initial_cap": 9.329416016979516e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0008018254613903969,
    "unapplied_final_day_resource_cost": 0.0007269481969811503
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 148.505429376865,
    "beneficial_raw_gain_per_resource_cost": 2227.5814406529753,
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
    "accrued_cost": 3.0190499900977397,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.042859513907263336,
    "accrued_cost_fraction_initial_cap": 0.10063499966992467,
    "mean_contract_rate": 0.040976770639222365,
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
    "maximum_relative_cash_error": 2.2492913187428528e-15,
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
      "minimum": -0.1934347007526307,
      "maximum": 0.004116055863802005,
      "mean": -0.10155854957811125,
      "median": -0.10556521642977791,
      "quantile_05": -0.17812253810903117,
      "quantile_95": -0.025385615712520765
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
      "minimum": 0.38159186253590793,
      "maximum": 0.8101167654311984,
      "mean": 0.6530571460765696,
      "median": 0.678963075256611,
      "quantile_05": 0.48797928460630297,
      "quantile_95": 0.7662825651092061
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
        "daily_volatility": 0.021701302596182286,
        "excess_kurtosis": 9.140213047914092,
        "return_acf_1": -0.08972706530598631,
        "abs_return_acf_1": 0.4019861099269654,
        "abs_return_acf_5": 0.3804823286204243,
        "abs_return_acf_20": 0.35800565229855,
        "quantile_01": -0.06855680219525538,
        "quantile_99": 0.06474161406280603,
        "hill_tail_index": 3.375251397935868
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019897008000377633,
        "excess_kurtosis": 10.467803630421377,
        "return_acf_1": -0.06996699300880657,
        "abs_return_acf_1": 0.3468790614070185,
        "abs_return_acf_5": 0.34420902054882874,
        "abs_return_acf_20": 0.24954159865824319,
        "quantile_01": -0.05891565554213992,
        "quantile_99": 0.04931938746455926,
        "hill_tail_index": 2.537146725817813
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02126936741498748,
        "excess_kurtosis": 7.242418024281841,
        "return_acf_1": -0.06212193133878093,
        "abs_return_acf_1": 0.38405619693328086,
        "abs_return_acf_5": 0.41623822467698535,
        "abs_return_acf_20": 0.26998247376674334,
        "quantile_01": -0.0690307791068929,
        "quantile_99": 0.0630410872537694,
        "hill_tail_index": 4.004278524623992
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02054499211750004,
        "excess_kurtosis": 6.285689817288212,
        "return_acf_1": -0.11267268408280669,
        "abs_return_acf_1": 0.3348456596597833,
        "abs_return_acf_5": 0.34378816400043,
        "abs_return_acf_20": 0.2682873415049696,
        "quantile_01": -0.05967998548905079,
        "quantile_99": 0.06005452150213199,
        "hill_tail_index": 3.3073702294275096
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02116871926718189,
        "excess_kurtosis": 11.485551251314773,
        "return_acf_1": 0.004116055863802005,
        "abs_return_acf_1": 0.37227952439011497,
        "abs_return_acf_5": 0.4024623173110393,
        "abs_return_acf_20": 0.3342428468608808,
        "quantile_01": -0.08396526469232628,
        "quantile_99": 0.05635465373310596,
        "hill_tail_index": 2.429350548278605
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020138761667104772,
        "excess_kurtosis": 5.265832646711742,
        "return_acf_1": -0.1618591984555591,
        "abs_return_acf_1": 0.33767272908070917,
        "abs_return_acf_5": 0.36781461028462753,
        "abs_return_acf_20": 0.32586603682594517,
        "quantile_01": -0.06552582251974474,
        "quantile_99": 0.0577257202459744,
        "hill_tail_index": 4.261253292698285
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02170682989761393,
        "excess_kurtosis": 12.434070158934949,
        "return_acf_1": -0.062484922164738554,
        "abs_return_acf_1": 0.40373884378572394,
        "abs_return_acf_5": 0.40258814481648425,
        "abs_return_acf_20": 0.26057145245292157,
        "quantile_01": -0.07535423220157478,
        "quantile_99": 0.06435494005789162,
        "hill_tail_index": 2.937728021621262
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020018101706779878,
        "excess_kurtosis": 7.7893418369138185,
        "return_acf_1": -0.05531849484014004,
        "abs_return_acf_1": 0.26324632741790077,
        "abs_return_acf_5": 0.2902959095365569,
        "abs_return_acf_20": 0.2621463684659253,
        "quantile_01": -0.07138039199847326,
        "quantile_99": 0.055482745582705155,
        "hill_tail_index": 3.4079053279216307
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02063433578371285,
        "excess_kurtosis": 8.441485676884632,
        "return_acf_1": -0.05292911481967852,
        "abs_return_acf_1": 0.3904415783636288,
        "abs_return_acf_5": 0.44700257060499815,
        "abs_return_acf_20": 0.3239391096651744,
        "quantile_01": -0.07073980857363878,
        "quantile_99": 0.059736360786302754,
        "hill_tail_index": 4.217245667938572
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021072895986014462,
        "excess_kurtosis": 9.13287110819601,
        "return_acf_1": -0.1934347007526307,
        "abs_return_acf_1": 0.3613120749061307,
        "abs_return_acf_5": 0.34469863957665425,
        "abs_return_acf_20": 0.3438400858643893,
        "quantile_01": -0.06892956181455165,
        "quantile_99": 0.05618794577941221,
        "hill_tail_index": 3.354521586064981
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02253313493584261,
        "excess_kurtosis": 12.696294304882752,
        "return_acf_1": -0.12786550818090364,
        "abs_return_acf_1": 0.415146550145626,
        "abs_return_acf_5": 0.4065767572776728,
        "abs_return_acf_20": 0.3125584910871276,
        "quantile_01": -0.07658928187972057,
        "quantile_99": 0.0603265267977403,
        "hill_tail_index": 2.7005182061647655
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02174817363384803,
        "excess_kurtosis": 12.210859425969721,
        "return_acf_1": -0.1555126097292498,
        "abs_return_acf_1": 0.4241954124102923,
        "abs_return_acf_5": 0.3439704777113398,
        "abs_return_acf_20": 0.2906954696418483,
        "quantile_01": -0.07586008054929241,
        "quantile_99": 0.05824251730764625,
        "hill_tail_index": 2.583745825214993
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02382621895366973,
        "excess_kurtosis": 10.860706768602459,
        "return_acf_1": -0.12874586097223878,
        "abs_return_acf_1": 0.4528771535336724,
        "abs_return_acf_5": 0.42086162454794945,
        "abs_return_acf_20": 0.32819233642443313,
        "quantile_01": -0.08107651950624443,
        "quantile_99": 0.06918123281789144,
        "hill_tail_index": 3.552742119644275
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02037713942929275,
        "excess_kurtosis": 8.85745214684716,
        "return_acf_1": -0.1858231858447783,
        "abs_return_acf_1": 0.40736705721927324,
        "abs_return_acf_5": 0.4347399134926725,
        "abs_return_acf_20": 0.343043035408107,
        "quantile_01": -0.06819763121970442,
        "quantile_99": 0.06856122158607653,
        "hill_tail_index": 3.284146590177085
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022049694373915067,
        "excess_kurtosis": 11.856069343566688,
        "return_acf_1": -0.004096522768328345,
        "abs_return_acf_1": 0.5104768087355728,
        "abs_return_acf_5": 0.4643881043336915,
        "abs_return_acf_20": 0.3015901183281731,
        "quantile_01": -0.07077077707825395,
        "quantile_99": 0.06935457483793225,
        "hill_tail_index": 3.5361344895240223
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022653946216749387,
        "excess_kurtosis": 9.97650892560421,
        "return_acf_1": -0.1109035254990096,
        "abs_return_acf_1": 0.4492524976279351,
        "abs_return_acf_5": 0.3879434200516804,
        "abs_return_acf_20": 0.2871397318494726,
        "quantile_01": -0.0631625720651735,
        "quantile_99": 0.06750027288402421,
        "hill_tail_index": 3.2463336969764356
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02091795029556686,
        "excess_kurtosis": 8.19038241976547,
        "return_acf_1": -0.1499728148269553,
        "abs_return_acf_1": 0.3507079667955609,
        "abs_return_acf_5": 0.2670000156511572,
        "abs_return_acf_20": 0.3043107223913265,
        "quantile_01": -0.06180162314849949,
        "quantile_99": 0.058503981082157056,
        "hill_tail_index": 3.19520716620082
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019467999935895746,
        "excess_kurtosis": 9.828436206321681,
        "return_acf_1": -0.12989772476246345,
        "abs_return_acf_1": 0.34413412247059705,
        "abs_return_acf_5": 0.38527696781672044,
        "abs_return_acf_20": 0.20994918388707212,
        "quantile_01": -0.05849463587044117,
        "quantile_99": 0.05774049050363261,
        "hill_tail_index": 3.525860265160836
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022654897990022356,
        "excess_kurtosis": 10.750790421046908,
        "return_acf_1": -0.06009661241056994,
        "abs_return_acf_1": 0.4649200249096837,
        "abs_return_acf_5": 0.44313624098244253,
        "abs_return_acf_20": 0.30280360073230717,
        "quantile_01": -0.08463416401515535,
        "quantile_99": 0.0651709655690825,
        "hill_tail_index": 2.8068572638924634
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0189792005420645,
        "excess_kurtosis": 6.346020555640864,
        "return_acf_1": -0.1687106353208958,
        "abs_return_acf_1": 0.21140064815072104,
        "abs_return_acf_5": 0.19862865605279023,
        "abs_return_acf_20": 0.20982321738718904,
        "quantile_01": -0.053916287775696015,
        "quantile_99": 0.05076246425552128,
        "hill_tail_index": 3.7937756299133114
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018935202284075376,
        "excess_kurtosis": 7.906468645215682,
        "return_acf_1": -0.1020219802968735,
        "abs_return_acf_1": 0.29703142092890883,
        "abs_return_acf_5": 0.2742548951767229,
        "abs_return_acf_20": 0.25168065163693565,
        "quantile_01": -0.05917181047330176,
        "quantile_99": 0.05681350679222685,
        "hill_tail_index": 4.076897723432416
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018097270974871273,
        "excess_kurtosis": 4.3512578370331845,
        "return_acf_1": -0.10872815351407501,
        "abs_return_acf_1": 0.29820634133454693,
        "abs_return_acf_5": 0.29026600951890696,
        "abs_return_acf_20": 0.3001483790425195,
        "quantile_01": -0.060032736991749165,
        "quantile_99": 0.051317844324347356,
        "hill_tail_index": 3.822352459199827
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02038540440882644,
        "excess_kurtosis": 9.341372951689419,
        "return_acf_1": -0.05140561819986676,
        "abs_return_acf_1": 0.3486007281142168,
        "abs_return_acf_5": 0.34730571973358415,
        "abs_return_acf_20": 0.2724131801783098,
        "quantile_01": -0.06174418533737227,
        "quantile_99": 0.061278878809700746,
        "hill_tail_index": 3.3679753300258874
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02244827170902049,
        "excess_kurtosis": 7.567349294357209,
        "return_acf_1": -0.0930130083141091,
        "abs_return_acf_1": 0.5026516343129954,
        "abs_return_acf_5": 0.48531588243949136,
        "abs_return_acf_20": 0.40645996172987026,
        "quantile_01": -0.07519725093602206,
        "quantile_99": 0.07032076086796933,
        "hill_tail_index": 3.7757130834265156
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019703365654912767,
        "excess_kurtosis": 7.629894974573425,
        "return_acf_1": -0.1024201580803486,
        "abs_return_acf_1": 0.34650390596596264,
        "abs_return_acf_5": 0.3146949627331157,
        "abs_return_acf_20": 0.2884786787838235,
        "quantile_01": -0.05729193739379839,
        "quantile_99": 0.05949982052357764,
        "hill_tail_index": 3.170782562460593
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019471726848048126,
        "excess_kurtosis": 14.139074631616904,
        "return_acf_1": -0.13442863508338393,
        "abs_return_acf_1": 0.31097444549266856,
        "abs_return_acf_5": 0.34283353684260903,
        "abs_return_acf_20": 0.29009706002898034,
        "quantile_01": -0.06036895170529157,
        "quantile_99": 0.04841563940947193,
        "hill_tail_index": 3.5464510138338836
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022023258543823948,
        "excess_kurtosis": 9.2616917771114,
        "return_acf_1": -0.07685471279483844,
        "abs_return_acf_1": 0.4315139330111026,
        "abs_return_acf_5": 0.4541051720622332,
        "abs_return_acf_20": 0.3183584308101005,
        "quantile_01": -0.07876831941479842,
        "quantile_99": 0.06547891509029849,
        "hill_tail_index": 3.398480534430765
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019760282934229458,
        "excess_kurtosis": 8.04844669209476,
        "return_acf_1": -0.10871027477920722,
        "abs_return_acf_1": 0.4045853952656849,
        "abs_return_acf_5": 0.3110107134855185,
        "abs_return_acf_20": 0.29630095875210893,
        "quantile_01": -0.06932362439060841,
        "quantile_99": 0.059573476377251,
        "hill_tail_index": 3.515503262547993
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02149588290253639,
        "excess_kurtosis": 10.876102395304164,
        "return_acf_1": -0.11833954284898232,
        "abs_return_acf_1": 0.4325520033991382,
        "abs_return_acf_5": 0.40665958198337715,
        "abs_return_acf_20": 0.3108210512263253,
        "quantile_01": -0.07386977026403221,
        "quantile_99": 0.05293450374904775,
        "hill_tail_index": 2.6500999213183003
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02182143177567076,
        "excess_kurtosis": 10.16218343840803,
        "return_acf_1": -0.07281035421093407,
        "abs_return_acf_1": 0.37958312512187403,
        "abs_return_acf_5": 0.34522059763967566,
        "abs_return_acf_20": 0.3120893057419418,
        "quantile_01": -0.07002862697721855,
        "quantile_99": 0.06843713165906526,
        "hill_tail_index": 3.143900543875644
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
