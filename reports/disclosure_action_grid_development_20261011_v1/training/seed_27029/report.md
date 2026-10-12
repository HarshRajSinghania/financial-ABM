# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27029
Run ID: `db1f979fd82a135bc9264c2caee99363aba7e4cfd25f0de54053f5edef61e14c`
Result fingerprint: `0d88828ab74defe43ef57acacc5edc9deb22668ddf13797b43a30096d6078e88`

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
    "equal_weight_sd": -0.5401309523809491,
    "equal_weight_raw": -8.101964285714239,
    "fixed_start_cap_weight_sd": -0.4582769590231926,
    "fixed_start_cap_weight_raw": -6.87415438534789,
    "end_cap_weight_sd": -0.46038076752095447,
    "end_cap_weight_raw": -6.905711512814314
  },
  "full_period_change": {
    "equal_weight_sd": -0.8527380952380904,
    "equal_weight_raw": -12.791071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7952255291005246,
    "inflation_mean_sd": 0.5317566137566138
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.41225000000000306,
    "equal_weight_raw": 6.183750000000047,
    "fixed_start_cap_weight_sd": 0.49410399335775973,
    "fixed_start_cap_weight_raw": 7.411559900366397,
    "end_cap_weight_sd": 0.4920001848599979,
    "end_cap_weight_raw": 7.380002772899968
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.34571428571428253,
      "change_raw": -5.185714285714238,
      "decay_adjusted_gain_sd": 0.6066666666666696
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5943253968253938,
      "change_raw": -8.914880952380907,
      "decay_adjusted_gain_sd": 0.3580555555555587
    },
    "small": {
      "count": 18,
      "change_sd": -0.5454365079365047,
      "change_raw": -8.18154761904757,
      "decay_adjusted_gain_sd": 0.4069444444444476
    },
    "large_minus_small_sd": 0.19972222222222213,
    "large_minus_small_raw": 2.995833333333332
  },
  "inflation": {
    "initial_mean_sd": 0.17191666666666666,
    "final_mean_sd": 0.54575,
    "mean_sd": 0.3979190258118235,
    "mean_absolute_raw_gap": 5.968785387177353,
    "final_absolute_raw_gap": 8.18625,
    "mean_range_fraction": 0.05968785387177353
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.43333333333333335,
    "initial_wealth_share": 0.375349362841436,
    "final_wealth_share": 0.45167404543778217
  },
  "pricing_slope": {
    "mean": -0.0012824478793319503,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.17035800279556904,
    "real_improvement_cost": 0.14522283633094918,
    "washing_cost": 0.02513516646461982,
    "fine_transfer": 0.020194906695383336,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.19055290949095238,
    "resource_cost_fraction_initial_cap": 0.005678600093185634,
    "private_net_outflow_fraction_initial_cap": 0.006351763649698413,
    "fine_transfer_fraction_initial_cap": 0.0006731635565127779,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0070354494876554005,
    "unapplied_final_day_resource_cost": 0.005086085649546617
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 72.59711781689053,
    "beneficial_raw_gain_per_resource_cost": 1088.956767253358,
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
    "accrued_cost": 2.7542797266548633,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.221910749535613,
    "accrued_cost_fraction_initial_cap": 0.09180932422182878,
    "mean_contract_rate": 0.03857093070598448,
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
    "maximum_relative_cash_error": 1.5397199860171936e-15,
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
      "minimum": -0.25516859958534766,
      "maximum": -0.016871696754546393,
      "mean": -0.13959923412880262,
      "median": -0.13235283284944088,
      "quantile_05": -0.24428738912442788,
      "quantile_95": -0.04458973246005389
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
      "minimum": 0.26096628678749156,
      "maximum": 0.7596884623620845,
      "mean": 0.4410383820429508,
      "median": 0.41057115759784524,
      "quantile_05": 0.2922658878784177,
      "quantile_95": 0.6651999873685772
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
        "daily_volatility": 0.015790207212996586,
        "excess_kurtosis": 8.224378359246971,
        "return_acf_1": -0.026570183634646253,
        "abs_return_acf_1": 0.252693345929008,
        "abs_return_acf_5": 0.20212087735582754,
        "abs_return_acf_20": 0.1952711132161025,
        "quantile_01": -0.038101141356892944,
        "quantile_99": 0.04236245449085575,
        "hill_tail_index": 2.711099860185506
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020655767366539523,
        "excess_kurtosis": 5.978875287914171,
        "return_acf_1": -0.08201186479483696,
        "abs_return_acf_1": 0.3271236675836379,
        "abs_return_acf_5": 0.3670153334066164,
        "abs_return_acf_20": 0.3112069775879722,
        "quantile_01": -0.062235780083257274,
        "quantile_99": 0.06121031669228471,
        "hill_tail_index": 3.627613568830338
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01649506538912401,
        "excess_kurtosis": 4.1033342063659255,
        "return_acf_1": -0.20210374865003045,
        "abs_return_acf_1": 0.2806679750380517,
        "abs_return_acf_5": 0.2620751899498198,
        "abs_return_acf_20": 0.22353059831289848,
        "quantile_01": -0.0488211736583155,
        "quantile_99": 0.04228898055851314,
        "hill_tail_index": 2.594581182641853
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022044791100663715,
        "excess_kurtosis": 9.32036851151513,
        "return_acf_1": -0.0707270230317294,
        "abs_return_acf_1": 0.4365663315311323,
        "abs_return_acf_5": 0.38147515454801456,
        "abs_return_acf_20": 0.37032280243824645,
        "quantile_01": -0.07372490154565435,
        "quantile_99": 0.0763022630742995,
        "hill_tail_index": 3.8255960901774784
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01621780015982974,
        "excess_kurtosis": 3.0394878769841496,
        "return_acf_1": -0.15274714298869263,
        "abs_return_acf_1": 0.22297667159140797,
        "abs_return_acf_5": 0.22064148684634002,
        "abs_return_acf_20": 0.1981231917486164,
        "quantile_01": -0.0429202053121038,
        "quantile_99": 0.04437860987340375,
        "hill_tail_index": 4.835681113011599
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019592779647303535,
        "excess_kurtosis": 15.908496147274114,
        "return_acf_1": -0.23141564311165289,
        "abs_return_acf_1": 0.48154230443929796,
        "abs_return_acf_5": 0.2824174998340041,
        "abs_return_acf_20": 0.22223820504093625,
        "quantile_01": -0.06416819905728491,
        "quantile_99": 0.0483373392534087,
        "hill_tail_index": 2.511332029335383
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.014864235133876516,
        "excess_kurtosis": 4.524531091683172,
        "return_acf_1": -0.09386289360318449,
        "abs_return_acf_1": 0.23663065797934635,
        "abs_return_acf_5": 0.17412866824425888,
        "abs_return_acf_20": 0.15508270456186074,
        "quantile_01": -0.03637740293338391,
        "quantile_99": 0.03776404507615816,
        "hill_tail_index": 3.877474657817096
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02137105415394783,
        "excess_kurtosis": 17.428848379778557,
        "return_acf_1": -0.25516859958534766,
        "abs_return_acf_1": 0.42053283741305625,
        "abs_return_acf_5": 0.43276924053947335,
        "abs_return_acf_20": 0.23881702238247482,
        "quantile_01": -0.0671497622005332,
        "quantile_99": 0.06097310859677565,
        "hill_tail_index": 2.0476368467354065
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01916860842222731,
        "excess_kurtosis": 8.4958875773942,
        "return_acf_1": -0.1693550967211965,
        "abs_return_acf_1": 0.375343829972936,
        "abs_return_acf_5": 0.384110384719557,
        "abs_return_acf_20": 0.2330753573781276,
        "quantile_01": -0.06103857172075402,
        "quantile_99": 0.05569855264247705,
        "hill_tail_index": 3.484680483325201
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02038117199210756,
        "excess_kurtosis": 9.869250265675104,
        "return_acf_1": -0.016871696754546393,
        "abs_return_acf_1": 0.37679526444020855,
        "abs_return_acf_5": 0.4135937321110438,
        "abs_return_acf_20": 0.2858071409712622,
        "quantile_01": -0.06282995453583488,
        "quantile_99": 0.058956007139628654,
        "hill_tail_index": 2.8617787853895185
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017094189526652027,
        "excess_kurtosis": 3.0253359028926567,
        "return_acf_1": -0.23832785505756068,
        "abs_return_acf_1": 0.24943070690121713,
        "abs_return_acf_5": 0.1959949797712541,
        "abs_return_acf_20": 0.21568981260846706,
        "quantile_01": -0.044952374644113766,
        "quantile_99": 0.049637880981481114,
        "hill_tail_index": 4.083769124209952
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017510653966279377,
        "excess_kurtosis": 6.751759301336461,
        "return_acf_1": -0.1325981134908901,
        "abs_return_acf_1": 0.33872147801400015,
        "abs_return_acf_5": 0.22752926551238975,
        "abs_return_acf_20": 0.3637203927180349,
        "quantile_01": -0.048709711180684574,
        "quantile_99": 0.0503429541157733,
        "hill_tail_index": 3.4041912431242096
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01783615508181254,
        "excess_kurtosis": 15.749190356697362,
        "return_acf_1": -0.13996620715423855,
        "abs_return_acf_1": 0.33944170557433473,
        "abs_return_acf_5": 0.2506483152644571,
        "abs_return_acf_20": 0.18417003029480683,
        "quantile_01": -0.058223742750664734,
        "quantile_99": 0.04187501714341901,
        "hill_tail_index": 2.0608077755468415
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.014290905852704696,
        "excess_kurtosis": 1.1086628351848002,
        "return_acf_1": -0.13210755220799164,
        "abs_return_acf_1": 0.15015136628300513,
        "abs_return_acf_5": 0.11087423908961205,
        "abs_return_acf_20": 0.14666107882752566,
        "quantile_01": -0.03520419486802955,
        "quantile_99": 0.03474077781374605,
        "hill_tail_index": 4.752639935533455
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016982338578657153,
        "excess_kurtosis": 5.331031456505347,
        "return_acf_1": -0.13922580220330202,
        "abs_return_acf_1": 0.263554981510976,
        "abs_return_acf_5": 0.17359057328690763,
        "abs_return_acf_20": 0.1891900800291769,
        "quantile_01": -0.04980787950415545,
        "quantile_99": 0.04703182367474193,
        "hill_tail_index": 3.4965548694755153
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01956979423822406,
        "excess_kurtosis": 7.479429490611546,
        "return_acf_1": -0.2121898454661309,
        "abs_return_acf_1": 0.4418401958931596,
        "abs_return_acf_5": 0.36155006528129385,
        "abs_return_acf_20": 0.24056077142880763,
        "quantile_01": -0.06228064018473273,
        "quantile_99": 0.06109435861749864,
        "hill_tail_index": 2.7874794414570694
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018876592492998615,
        "excess_kurtosis": 8.552351829263635,
        "return_acf_1": -0.17295828778109565,
        "abs_return_acf_1": 0.3514111738615409,
        "abs_return_acf_5": 0.38855087782412046,
        "abs_return_acf_20": 0.32841014876771757,
        "quantile_01": -0.05772505468202372,
        "quantile_99": 0.05272415186997574,
        "hill_tail_index": 3.155914597612113
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018031580871880296,
        "excess_kurtosis": 6.549360197877851,
        "return_acf_1": -0.1069460734745186,
        "abs_return_acf_1": 0.32615140076736393,
        "abs_return_acf_5": 0.2931101149415358,
        "abs_return_acf_20": 0.203523402759659,
        "quantile_01": -0.054226805210396994,
        "quantile_99": 0.05663227608158059,
        "hill_tail_index": 3.61675354243725
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01961995379736318,
        "excess_kurtosis": 9.930405001576643,
        "return_acf_1": -0.18598698856738421,
        "abs_return_acf_1": 0.32838943144392285,
        "abs_return_acf_5": 0.3103391405346824,
        "abs_return_acf_20": 0.24757753045135036,
        "quantile_01": -0.06373684354196225,
        "quantile_99": 0.05908538409435285,
        "hill_tail_index": 3.210206188740096
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016886467275821132,
        "excess_kurtosis": 3.3108263429259344,
        "return_acf_1": -0.161131395193733,
        "abs_return_acf_1": 0.24092626478582427,
        "abs_return_acf_5": 0.26190709246091853,
        "abs_return_acf_20": 0.15771458883641792,
        "quantile_01": -0.046489181578272754,
        "quantile_99": 0.05031144799040216,
        "hill_tail_index": 3.9906615257550495
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02024093405937858,
        "excess_kurtosis": 8.943708941040564,
        "return_acf_1": -0.06661362546888519,
        "abs_return_acf_1": 0.44489410357758097,
        "abs_return_acf_5": 0.37501409595812285,
        "abs_return_acf_20": 0.35383981632451905,
        "quantile_01": -0.060236089569576566,
        "quantile_99": 0.05526718225303003,
        "hill_tail_index": 3.1091778994690022
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017468280479737933,
        "excess_kurtosis": 5.914547419378476,
        "return_acf_1": -0.24916337154277376,
        "abs_return_acf_1": 0.29070120597325483,
        "abs_return_acf_5": 0.20516847192366056,
        "abs_return_acf_20": 0.24363797633130513,
        "quantile_01": -0.04157237524068379,
        "quantile_99": 0.05358539138555371,
        "hill_tail_index": 2.5492509432798744
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.014764689511193484,
        "excess_kurtosis": 4.119005384617264,
        "return_acf_1": -0.12348399761970213,
        "abs_return_acf_1": 0.2567524455485089,
        "abs_return_acf_5": 0.16826674915005055,
        "abs_return_acf_20": 0.21028201685519135,
        "quantile_01": -0.039041625921521286,
        "quantile_99": 0.03446729483948348,
        "hill_tail_index": 3.378036900569187
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01877925775372366,
        "excess_kurtosis": 20.881070712064727,
        "return_acf_1": -0.10826715757177231,
        "abs_return_acf_1": 0.36724950253394584,
        "abs_return_acf_5": 0.2994444149696413,
        "abs_return_acf_20": 0.3076804969874279,
        "quantile_01": -0.050287979426691304,
        "quantile_99": 0.04853429550400533,
        "hill_tail_index": 2.064638762010548
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02036799641874767,
        "excess_kurtosis": 6.796323521749912,
        "return_acf_1": -0.1557144339131321,
        "abs_return_acf_1": 0.5306958472746854,
        "abs_return_acf_5": 0.3666510710328631,
        "abs_return_acf_20": 0.3325915504511667,
        "quantile_01": -0.0659016548733927,
        "quantile_99": 0.06638754476067765,
        "hill_tail_index": 3.7165947749721173
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018840092131330463,
        "excess_kurtosis": 6.2957983579694865,
        "return_acf_1": -0.11672573611169196,
        "abs_return_acf_1": 0.4633583383362568,
        "abs_return_acf_5": 0.31517734384232776,
        "abs_return_acf_20": 0.3182962028027179,
        "quantile_01": -0.06188504111163466,
        "quantile_99": 0.053226766904097424,
        "hill_tail_index": 2.7996364479168308
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01812069317720327,
        "excess_kurtosis": 5.2343170550712514,
        "return_acf_1": -0.13205497404468075,
        "abs_return_acf_1": 0.3047696041019798,
        "abs_return_acf_5": 0.2998131920893765,
        "abs_return_acf_20": 0.23641106034850637,
        "quantile_01": -0.045974525045814035,
        "quantile_99": 0.05121967889706251,
        "hill_tail_index": 2.930870814274304
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017378587496575452,
        "excess_kurtosis": 6.132321939263832,
        "return_acf_1": -0.11395631080408757,
        "abs_return_acf_1": 0.30834989696710075,
        "abs_return_acf_5": 0.24992667654820902,
        "abs_return_acf_20": 0.22964731940532163,
        "quantile_01": -0.048564519578836944,
        "quantile_99": 0.049221186672045614,
        "hill_tail_index": 3.98867288882838
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018853949182828036,
        "excess_kurtosis": 7.31746284064784,
        "return_acf_1": -0.08531174781578164,
        "abs_return_acf_1": 0.34810219905890916,
        "abs_return_acf_5": 0.3119710549243436,
        "abs_return_acf_20": 0.30876259525713945,
        "quantile_01": -0.059840015908534355,
        "quantile_99": 0.04864414517916564,
        "hill_tail_index": 2.7503898802216433
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021004217182446685,
        "excess_kurtosis": 6.115931541336316,
        "return_acf_1": -0.11441365549886244,
        "abs_return_acf_1": 0.4606288957222544,
        "abs_return_acf_5": 0.3414857071916454,
        "abs_return_acf_20": 0.29663681529780456,
        "quantile_01": -0.06632073006956812,
        "quantile_99": 0.06329685682232031,
        "hill_tail_index": 3.9705795480510506
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
