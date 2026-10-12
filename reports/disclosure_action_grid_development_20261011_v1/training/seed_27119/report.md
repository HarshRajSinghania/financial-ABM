# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27119
Run ID: `84bb4795941572a188e8f71fe986a58f47a7da126c9fb99bfbd3ee1947053cdd`
Result fingerprint: `24494777ae8d17474d93303a130cf7cb166bf32bf0853482255dd0f4a103be08`

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
    "equal_weight_sd": -0.6670476190476158,
    "equal_weight_raw": -10.005714285714236,
    "fixed_start_cap_weight_sd": -0.7203508467062936,
    "fixed_start_cap_weight_raw": -10.805262700594403,
    "end_cap_weight_sd": -0.7185090202143541,
    "end_cap_weight_raw": -10.777635303215309
  },
  "full_period_change": {
    "equal_weight_sd": -1.0550714285714238,
    "equal_weight_raw": -15.826071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.012985780423276,
    "inflation_mean_sd": 0.6308935185185186
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2853333333333366,
    "equal_weight_raw": 4.280000000000048,
    "fixed_start_cap_weight_sd": 0.23203010567465845,
    "fixed_start_cap_weight_raw": 3.480451585119877,
    "end_cap_weight_sd": 0.2338719321665984,
    "end_cap_weight_raw": 3.5080789824989753
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7823809523809492,
      "change_raw": -11.735714285714238,
      "decay_adjusted_gain_sd": 0.17000000000000312
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6479365079365047,
      "change_raw": -9.71904761904757,
      "decay_adjusted_gain_sd": 0.3044444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.6573809523809492,
      "change_raw": -9.860714285714238,
      "decay_adjusted_gain_sd": 0.29500000000000326
    },
    "large_minus_small_sd": -0.125,
    "large_minus_small_raw": -1.875
  },
  "inflation": {
    "initial_mean_sd": 0.40325,
    "final_mean_sd": 0.6778333333333334,
    "mean_sd": 0.5469729392173189,
    "mean_absolute_raw_gap": 8.204594088259784,
    "final_absolute_raw_gap": 10.167500000000002,
    "mean_range_fraction": 0.08204594088259784
  },
  "impact": {
    "initial_share": 0.43333333333333335,
    "final_share": 0.6333333333333333,
    "initial_wealth_share": 0.4157680242459088,
    "final_wealth_share": 0.5898879871111588
  },
  "pricing_slope": {
    "mean": -0.0034988677407862593,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.12150099949258683,
    "real_improvement_cost": 0.11333334472686953,
    "washing_cost": 0.008167654765717298,
    "fine_transfer": 0.004434280000878246,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12593527949346509,
    "resource_cost_fraction_initial_cap": 0.004050033316419561,
    "private_net_outflow_fraction_initial_cap": 0.004197842649782169,
    "fine_transfer_fraction_initial_cap": 0.0001478093333626082,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0015079687994248275,
    "unapplied_final_day_resource_cost": 0.004844264284539644
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 70.45209533870847,
    "beneficial_raw_gain_per_resource_cost": 1056.7814300806274,
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
    "accrued_cost": 2.7989490813984492,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.1772413947920277,
    "accrued_cost_fraction_initial_cap": 0.09329830271328164,
    "mean_contract_rate": 0.03986236958366848,
    "maximum_ledger_error": 8.470329472543003e-20
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
    "maximum_relative_cash_error": 1.913068471307112e-15,
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
      "minimum": -0.26081237288593895,
      "maximum": -0.019105003327220232,
      "mean": -0.15159058662864408,
      "median": -0.1454642551268325,
      "quantile_05": -0.24725646087155145,
      "quantile_95": -0.06639276923936828
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
      "minimum": 0.233870550032125,
      "maximum": 0.8160032859275015,
      "mean": 0.5137821282720824,
      "median": 0.5060023549503978,
      "quantile_05": 0.3040259536186365,
      "quantile_95": 0.7535896109764443
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
        "daily_volatility": 0.01656280256368045,
        "excess_kurtosis": 4.0575723475264684,
        "return_acf_1": -0.1489553490153438,
        "abs_return_acf_1": 0.28168524201821216,
        "abs_return_acf_5": 0.1908820349411058,
        "abs_return_acf_20": 0.26492168943186917,
        "quantile_01": -0.0458090208100898,
        "quantile_99": 0.05435770246285402,
        "hill_tail_index": 4.049028864923807
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020234474510916766,
        "excess_kurtosis": 7.07250813820794,
        "return_acf_1": -0.06018338792015844,
        "abs_return_acf_1": 0.35579199170257986,
        "abs_return_acf_5": 0.38375182839387073,
        "abs_return_acf_20": 0.3411631514306089,
        "quantile_01": -0.06473972313855157,
        "quantile_99": 0.06034967749207769,
        "hill_tail_index": 3.3096894925774976
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01841120935378702,
        "excess_kurtosis": 9.455750822691696,
        "return_acf_1": -0.10039362931737374,
        "abs_return_acf_1": 0.35866316800875303,
        "abs_return_acf_5": 0.3763118838448631,
        "abs_return_acf_20": 0.2669531393820511,
        "quantile_01": -0.053641960980973666,
        "quantile_99": 0.04942504163623978,
        "hill_tail_index": 2.925326948819881
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017619216400894436,
        "excess_kurtosis": 16.31787488860031,
        "return_acf_1": -0.19045863508082553,
        "abs_return_acf_1": 0.4314248780135608,
        "abs_return_acf_5": 0.3061103277284408,
        "abs_return_acf_20": 0.24211215098717753,
        "quantile_01": -0.04546139614810485,
        "quantile_99": 0.03719435246042992,
        "hill_tail_index": 1.658354519478801
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01782195966428145,
        "excess_kurtosis": 25.24688124211748,
        "return_acf_1": -0.11594113213439898,
        "abs_return_acf_1": 0.3427419511926421,
        "abs_return_acf_5": 0.2970952939707739,
        "abs_return_acf_20": 0.20671397234701672,
        "quantile_01": -0.04516973920901054,
        "quantile_99": 0.03718281650475486,
        "hill_tail_index": 1.742486910359845
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015993038994259388,
        "excess_kurtosis": 5.766554863150651,
        "return_acf_1": -0.11270420434414262,
        "abs_return_acf_1": 0.22890252180011186,
        "abs_return_acf_5": 0.26693709221163414,
        "abs_return_acf_20": 0.23554590938391232,
        "quantile_01": -0.042552227530599354,
        "quantile_99": 0.04785703019895673,
        "hill_tail_index": 2.32296375554203
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.014949307600638182,
        "excess_kurtosis": 1.9757165775743575,
        "return_acf_1": -0.11666987122134757,
        "abs_return_acf_1": 0.2512767560303127,
        "abs_return_acf_5": 0.21747167663816858,
        "abs_return_acf_20": 0.17580489101193952,
        "quantile_01": -0.036933935046324244,
        "quantile_99": 0.04581917591171957,
        "hill_tail_index": 4.602303118140115
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.016517817444606557,
        "excess_kurtosis": 2.050999321642175,
        "return_acf_1": -0.14662327208094753,
        "abs_return_acf_1": 0.21441852921735527,
        "abs_return_acf_5": 0.23200099360798898,
        "abs_return_acf_20": 0.22959930380643465,
        "quantile_01": -0.046990679500053194,
        "quantile_99": 0.04698300946872671,
        "hill_tail_index": 5.1448869343535595
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020327926989551316,
        "excess_kurtosis": 11.387523522789591,
        "return_acf_1": -0.20893780238830162,
        "abs_return_acf_1": 0.46625412638590324,
        "abs_return_acf_5": 0.45291132931852957,
        "abs_return_acf_20": 0.33776116119162514,
        "quantile_01": -0.06544348666076773,
        "quantile_99": 0.048886835339243886,
        "hill_tail_index": 2.745554779303634
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018848064715576214,
        "excess_kurtosis": 16.281668574121934,
        "return_acf_1": -0.09832942714387988,
        "abs_return_acf_1": 0.3331540702540606,
        "abs_return_acf_5": 0.3057867153958619,
        "abs_return_acf_20": 0.3055510199106961,
        "quantile_01": -0.042958537362916764,
        "quantile_99": 0.05657202926549837,
        "hill_tail_index": 2.0315013010493876
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01636741574829318,
        "excess_kurtosis": 12.167423210643944,
        "return_acf_1": -0.10039094956607691,
        "abs_return_acf_1": 0.33901887546097753,
        "abs_return_acf_5": 0.285920840376437,
        "abs_return_acf_20": 0.1349880553741159,
        "quantile_01": -0.04067088690854883,
        "quantile_99": 0.04024119427327408,
        "hill_tail_index": 2.561643241586551
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01714615592956474,
        "excess_kurtosis": 6.498545383756024,
        "return_acf_1": -0.08642178275751318,
        "abs_return_acf_1": 0.2203040080867459,
        "abs_return_acf_5": 0.23995316396179467,
        "abs_return_acf_20": 0.2041307960718276,
        "quantile_01": -0.0457799126286493,
        "quantile_99": 0.04736617744906279,
        "hill_tail_index": 3.0731804215747878
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01984294651708367,
        "excess_kurtosis": 9.030845435046643,
        "return_acf_1": -0.14430523817271748,
        "abs_return_acf_1": 0.36008238324603825,
        "abs_return_acf_5": 0.37262096639269854,
        "abs_return_acf_20": 0.26174249717852627,
        "quantile_01": -0.05764232178382746,
        "quantile_99": 0.06654071146538525,
        "hill_tail_index": 3.936379717861934
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019742602593983142,
        "excess_kurtosis": 14.749024892511184,
        "return_acf_1": -0.231248367578291,
        "abs_return_acf_1": 0.5533447567409189,
        "abs_return_acf_5": 0.43655403238635443,
        "abs_return_acf_20": 0.370432248028454,
        "quantile_01": -0.07592040819207228,
        "quantile_99": 0.049948674483685736,
        "hill_tail_index": 2.215973894705533
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020415244933587925,
        "excess_kurtosis": 24.507097154401016,
        "return_acf_1": -0.23736227996282797,
        "abs_return_acf_1": 0.46655075795677875,
        "abs_return_acf_5": 0.36982770290138894,
        "abs_return_acf_20": 0.24426171369290983,
        "quantile_01": -0.05193420266320128,
        "quantile_99": 0.054375261064037055,
        "hill_tail_index": 1.898130066052264
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018416251796463043,
        "excess_kurtosis": 5.827957482888829,
        "return_acf_1": -0.073982013073958,
        "abs_return_acf_1": 0.2613893606788647,
        "abs_return_acf_5": 0.23047549998472983,
        "abs_return_acf_20": 0.26342133818776275,
        "quantile_01": -0.051872912876632815,
        "quantile_99": 0.04739439654712492,
        "hill_tail_index": 3.3953023918616805
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019010738429117758,
        "excess_kurtosis": 15.363682197527108,
        "return_acf_1": -0.21924391366456247,
        "abs_return_acf_1": 0.5420035715194608,
        "abs_return_acf_5": 0.4844281462841209,
        "abs_return_acf_20": 0.3577480184086875,
        "quantile_01": -0.06773553790759732,
        "quantile_99": 0.05200713978309711,
        "hill_tail_index": 2.2864838206566604
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019936324981976075,
        "excess_kurtosis": 19.54262266949938,
        "return_acf_1": -0.25221990940474925,
        "abs_return_acf_1": 0.5014634045791333,
        "abs_return_acf_5": 0.4194121936565603,
        "abs_return_acf_20": 0.23832348541789203,
        "quantile_01": -0.05076166001012218,
        "quantile_99": 0.049680889667819174,
        "hill_tail_index": 2.05530023367631
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02067757661724378,
        "excess_kurtosis": 25.45001029554997,
        "return_acf_1": -0.21262097915671752,
        "abs_return_acf_1": 0.52128463363766,
        "abs_return_acf_5": 0.3797639871388093,
        "abs_return_acf_20": 0.27992136414746327,
        "quantile_01": -0.0632812397642012,
        "quantile_99": 0.04776793595193241,
        "hill_tail_index": 1.7144373571512614
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016515128098450835,
        "excess_kurtosis": 7.3903902715750736,
        "return_acf_1": -0.12756215049318312,
        "abs_return_acf_1": 0.2883010920089736,
        "abs_return_acf_5": 0.21476226001276896,
        "abs_return_acf_20": 0.16465062834006527,
        "quantile_01": -0.03939531507526321,
        "quantile_99": 0.04346149912142209,
        "hill_tail_index": 2.346443612936001
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02177182067866559,
        "excess_kurtosis": 27.01265197051016,
        "return_acf_1": -0.26081237288593895,
        "abs_return_acf_1": 0.5780030489443777,
        "abs_return_acf_5": 0.47068612434011214,
        "abs_return_acf_20": 0.37069064105497374,
        "quantile_01": -0.07096985235021404,
        "quantile_99": 0.05209412953904409,
        "hill_tail_index": 1.8042439098363696
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017719239254963604,
        "excess_kurtosis": 9.408717557682904,
        "return_acf_1": -0.17144305343198807,
        "abs_return_acf_1": 0.4357525675762483,
        "abs_return_acf_5": 0.43929576700973755,
        "abs_return_acf_20": 0.34246259588220296,
        "quantile_01": -0.0542818237836523,
        "quantile_99": 0.04628957134389036,
        "hill_tail_index": 2.184345461796787
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.016285450289961,
        "excess_kurtosis": 3.4684733416610545,
        "return_acf_1": -0.08334699472675122,
        "abs_return_acf_1": 0.22817108698638702,
        "abs_return_acf_5": 0.20103648380694292,
        "abs_return_acf_20": 0.20502161499938498,
        "quantile_01": -0.04876485541701907,
        "quantile_99": 0.04452515538311506,
        "hill_tail_index": 4.167884841586736
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01911066537914993,
        "excess_kurtosis": 12.125855081167083,
        "return_acf_1": -0.12257660370415546,
        "abs_return_acf_1": 0.2873656191419674,
        "abs_return_acf_5": 0.3453832474423633,
        "abs_return_acf_20": 0.25969590110916474,
        "quantile_01": -0.0556087381259454,
        "quantile_99": 0.05460915731683374,
        "hill_tail_index": 2.0493297118279354
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020838660555141508,
        "excess_kurtosis": 9.793726351968829,
        "return_acf_1": -0.22031134661317436,
        "abs_return_acf_1": 0.48383412698512773,
        "abs_return_acf_5": 0.5154389041950015,
        "abs_return_acf_20": 0.3966480791552518,
        "quantile_01": -0.06841634329176842,
        "quantile_99": 0.06925667626097412,
        "hill_tail_index": 3.369371385284092
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020301294868411413,
        "excess_kurtosis": 18.080184453059026,
        "return_acf_1": -0.15858734838061272,
        "abs_return_acf_1": 0.4710572730972754,
        "abs_return_acf_5": 0.5172920043432315,
        "abs_return_acf_20": 0.36844637353857057,
        "quantile_01": -0.06454072188908215,
        "quantile_99": 0.05952230671774606,
        "hill_tail_index": 1.9518035221374805
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018328164431497294,
        "excess_kurtosis": 9.049020589900616,
        "return_acf_1": -0.12344429345494289,
        "abs_return_acf_1": 0.3260066505905293,
        "abs_return_acf_5": 0.2667203237226621,
        "abs_return_acf_20": 0.2459273137345718,
        "quantile_01": -0.05946277583440236,
        "quantile_99": 0.04994491088476294,
        "hill_tail_index": 2.51587965544533
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016640653229883243,
        "excess_kurtosis": 24.505274646760167,
        "return_acf_1": -0.019105003327220232,
        "abs_return_acf_1": 0.3887373583407241,
        "abs_return_acf_5": 0.2983204220589489,
        "abs_return_acf_20": 0.1697097753091507,
        "quantile_01": -0.047185811007471774,
        "quantile_99": 0.03938192321548245,
        "hill_tail_index": 2.017789187075074
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02021746405876804,
        "excess_kurtosis": 14.535423858644005,
        "return_acf_1": -0.24119002377542081,
        "abs_return_acf_1": 0.5740910722296093,
        "abs_return_acf_5": 0.48634884857633737,
        "abs_return_acf_20": 0.3710508633986877,
        "quantile_01": -0.07360373763723378,
        "quantile_99": 0.05461502338885708,
        "hill_tail_index": 2.010955062467847
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016772362334595572,
        "excess_kurtosis": 7.31475662469694,
        "return_acf_1": -0.1623462640818015,
        "abs_return_acf_1": 0.3599866209253272,
        "abs_return_acf_5": 0.2683496933262607,
        "abs_return_acf_20": 0.28823195766335535,
        "quantile_01": -0.0529535599394558,
        "quantile_99": 0.03908514829100792,
        "hill_tail_index": 2.4245329756985012
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
