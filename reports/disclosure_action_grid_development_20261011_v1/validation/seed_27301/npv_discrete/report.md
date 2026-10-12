# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27301
Run ID: `f34d1680dfdb519f7d9a0bc5fec77c791e60087dca1f990e927d8e2abb403c99`
Result fingerprint: `2ef31cf5243587d09053301ca13b1ff06a0437f4330e9ae63ccd9dfa0a31e830`

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
    "equal_weight_sd": -0.6536309523809489,
    "equal_weight_raw": -9.804464285714232,
    "fixed_start_cap_weight_sd": -0.646440240995136,
    "fixed_start_cap_weight_raw": -9.696603614927042,
    "end_cap_weight_sd": -0.6627432092825859,
    "end_cap_weight_raw": -9.94114813923879
  },
  "full_period_change": {
    "equal_weight_sd": -1.0238214285714236,
    "equal_weight_raw": -15.357321428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9577996031745983,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.29875000000000346,
    "equal_weight_raw": 4.481250000000052,
    "fixed_start_cap_weight_sd": 0.30594071138581624,
    "fixed_start_cap_weight_raw": 4.589110670787245,
    "end_cap_weight_sd": 0.2896377430983665,
    "end_cap_weight_raw": 4.344566146475498
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7215476190476159,
      "change_raw": -10.823214285714238,
      "decay_adjusted_gain_sd": 0.23083333333333647
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5132142857142821,
      "change_raw": -7.698214285714231,
      "decay_adjusted_gain_sd": 0.43916666666667037
    },
    "small": {
      "count": 18,
      "change_sd": -0.7125198412698378,
      "change_raw": -10.687797619047567,
      "decay_adjusted_gain_sd": 0.23986111111111452
    },
    "large_minus_small_sd": -0.009027777777778079,
    "large_minus_small_raw": -0.13541666666667118
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.26666666666666666,
    "initial_wealth_share": 0.3500138348321637,
    "final_wealth_share": 0.3681015077781472
  },
  "pricing_slope": {
    "mean": -0.0018890329994473432,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.0012509682508912035,
    "real_improvement_cost": 0.0012509682508912035,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0012509682508912035,
    "resource_cost_fraction_initial_cap": 4.1698941696373454e-05,
    "private_net_outflow_fraction_initial_cap": 4.1698941696373454e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 7.215132161806532e-05,
    "unapplied_final_day_resource_cost": 5.404175525915096e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 7164.450411603268,
    "beneficial_raw_gain_per_resource_cost": 107466.75617404903,
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
    "accrued_cost": 2.9097894128544968,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.06640106333597981,
    "accrued_cost_fraction_initial_cap": 0.09699298042848323,
    "mean_contract_rate": 0.0404727033627043,
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
    "maximum_relative_cash_error": 2.967743984093489e-15,
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
      "minimum": -0.20013946979455313,
      "maximum": 0.0402185455748402,
      "mean": -0.10495928641679873,
      "median": -0.1123423378399725,
      "quantile_05": -0.157470783992221,
      "quantile_95": -0.01254390767028803
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
      "minimum": 0.2514944117956185,
      "maximum": 0.746170433851144,
      "mean": 0.42342687380734406,
      "median": 0.3720664312854191,
      "quantile_05": 0.28510525928510455,
      "quantile_95": 0.6898380329544492
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
        "daily_volatility": 0.019357101755640396,
        "excess_kurtosis": 9.411492732100973,
        "return_acf_1": -0.1329184606740935,
        "abs_return_acf_1": 0.33648357890821773,
        "abs_return_acf_5": 0.39074083897728684,
        "abs_return_acf_20": 0.263572221646,
        "quantile_01": -0.052446511522728924,
        "quantile_99": 0.05880215824202212,
        "hill_tail_index": 2.692832038789325
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020490776164588758,
        "excess_kurtosis": 14.49537786260364,
        "return_acf_1": -0.15801052246160402,
        "abs_return_acf_1": 0.3667107648392693,
        "abs_return_acf_5": 0.35568340839519924,
        "abs_return_acf_20": 0.20851007963988216,
        "quantile_01": -0.06627229803756914,
        "quantile_99": 0.06081495751524137,
        "hill_tail_index": 1.899829431909693
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018434225728830057,
        "excess_kurtosis": 5.39894677528684,
        "return_acf_1": -0.12980039699467885,
        "abs_return_acf_1": 0.3298747815978295,
        "abs_return_acf_5": 0.3347492446830453,
        "abs_return_acf_20": 0.28379617899511306,
        "quantile_01": -0.058798634721522004,
        "quantile_99": 0.061684834179282236,
        "hill_tail_index": 5.032470137857911
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016698255802202203,
        "excess_kurtosis": 8.990530912675327,
        "return_acf_1": -0.11478790178855716,
        "abs_return_acf_1": 0.37078174993696106,
        "abs_return_acf_5": 0.3508528734687673,
        "abs_return_acf_20": 0.29361203046923184,
        "quantile_01": -0.04651199895677979,
        "quantile_99": 0.040591059775729035,
        "hill_tail_index": 3.532699246909238
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01986522555607523,
        "excess_kurtosis": 9.056137502646607,
        "return_acf_1": -0.15338049618713176,
        "abs_return_acf_1": 0.330605354447499,
        "abs_return_acf_5": 0.315878046843537,
        "abs_return_acf_20": 0.27859844474785506,
        "quantile_01": -0.06111709421934845,
        "quantile_99": 0.055507281898131554,
        "hill_tail_index": 2.622144300237551
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01959532295527684,
        "excess_kurtosis": 6.83936035969427,
        "return_acf_1": -0.12262877321439566,
        "abs_return_acf_1": 0.36938798305213416,
        "abs_return_acf_5": 0.34084689196670837,
        "abs_return_acf_20": 0.20586552453543341,
        "quantile_01": -0.06329510494256152,
        "quantile_99": 0.05469175579943512,
        "hill_tail_index": 2.8495753454950323
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016371333394992943,
        "excess_kurtosis": 8.733179099059793,
        "return_acf_1": -0.05812716194157367,
        "abs_return_acf_1": 0.3141123301783814,
        "abs_return_acf_5": 0.22385601662968396,
        "abs_return_acf_20": 0.2951806480532589,
        "quantile_01": -0.04207774308583688,
        "quantile_99": 0.039732232265444596,
        "hill_tail_index": 2.6954831174705505
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01781404886302588,
        "excess_kurtosis": 13.920426455866355,
        "return_acf_1": 0.021730244899347256,
        "abs_return_acf_1": 0.36340514032183985,
        "abs_return_acf_5": 0.2810016785911179,
        "abs_return_acf_20": 0.3435287828872641,
        "quantile_01": -0.05513181887029198,
        "quantile_99": 0.04905653693376567,
        "hill_tail_index": 2.018324924798978
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017507851902759525,
        "excess_kurtosis": 7.577693407298529,
        "return_acf_1": -0.10989677389138784,
        "abs_return_acf_1": 0.2712820851562061,
        "abs_return_acf_5": 0.29460313135877275,
        "abs_return_acf_20": 0.21011271850833813,
        "quantile_01": -0.052421465082163124,
        "quantile_99": 0.0547777855924624,
        "hill_tail_index": 3.053180878573954
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023543196570675738,
        "excess_kurtosis": 12.550348032835712,
        "return_acf_1": -0.1442778039242217,
        "abs_return_acf_1": 0.37154197361235136,
        "abs_return_acf_5": 0.45204665101632874,
        "abs_return_acf_20": 0.2604539296114965,
        "quantile_01": -0.07207824255706831,
        "quantile_99": 0.08503148646680674,
        "hill_tail_index": 3.030682505744394
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018386422954429757,
        "excess_kurtosis": 5.17359085233166,
        "return_acf_1": -0.15681110364075285,
        "abs_return_acf_1": 0.2658861648356787,
        "abs_return_acf_5": 0.25765420210216755,
        "abs_return_acf_20": 0.2270645554869184,
        "quantile_01": -0.056103131232097765,
        "quantile_99": 0.054061543577490385,
        "hill_tail_index": 3.5928570431973976
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018996737657717814,
        "excess_kurtosis": 5.019563136006603,
        "return_acf_1": -0.09383100320945288,
        "abs_return_acf_1": 0.3399048167828544,
        "abs_return_acf_5": 0.25367931200448,
        "abs_return_acf_20": 0.16919166074204964,
        "quantile_01": -0.05538930035985495,
        "quantile_99": 0.056826862235203945,
        "hill_tail_index": 4.451701112353802
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017503142698996475,
        "excess_kurtosis": 5.243083423593058,
        "return_acf_1": -0.1314471650231047,
        "abs_return_acf_1": 0.33994548851728484,
        "abs_return_acf_5": 0.24809243517699806,
        "abs_return_acf_20": 0.3035357095461491,
        "quantile_01": -0.05199477122747514,
        "quantile_99": 0.053525110921259,
        "hill_tail_index": 4.042806628833264
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.0193815479281815,
        "excess_kurtosis": 7.176778181748354,
        "return_acf_1": -0.0807235657056335,
        "abs_return_acf_1": 0.3865367634319555,
        "abs_return_acf_5": 0.3257390702840252,
        "abs_return_acf_20": 0.2735127700660233,
        "quantile_01": -0.055965190382732684,
        "quantile_99": 0.05640979629091661,
        "hill_tail_index": 2.841903130598372
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017486320165100183,
        "excess_kurtosis": 6.820374731847748,
        "return_acf_1": -0.14460076467448513,
        "abs_return_acf_1": 0.3934495804083393,
        "abs_return_acf_5": 0.3523481102578983,
        "abs_return_acf_20": 0.2499138403370967,
        "quantile_01": -0.05518565459158663,
        "quantile_99": 0.0519332225264656,
        "hill_tail_index": 3.703916137659759
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020356431124120025,
        "excess_kurtosis": 7.678277798988537,
        "return_acf_1": -0.20013946979455313,
        "abs_return_acf_1": 0.400357971286883,
        "abs_return_acf_5": 0.397025351140086,
        "abs_return_acf_20": 0.2899948232826122,
        "quantile_01": -0.06501281291096415,
        "quantile_99": 0.060481812992383005,
        "hill_tail_index": 3.358317706097219
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019035485983304793,
        "excess_kurtosis": 3.7759267294580603,
        "return_acf_1": -0.10255223082770462,
        "abs_return_acf_1": 0.3574753926447241,
        "abs_return_acf_5": 0.31477924685572517,
        "abs_return_acf_20": 0.26957527090326555,
        "quantile_01": -0.05629160809772819,
        "quantile_99": 0.05625248178508487,
        "hill_tail_index": 4.184174836822686
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018624621972682144,
        "excess_kurtosis": 5.2473614517591916,
        "return_acf_1": -0.06692442074175405,
        "abs_return_acf_1": 0.2833386053682253,
        "abs_return_acf_5": 0.25289448476257553,
        "abs_return_acf_20": 0.21342396456201998,
        "quantile_01": -0.05814832259244238,
        "quantile_99": 0.054700806337357244,
        "hill_tail_index": 4.28460086713897
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018017726598158493,
        "excess_kurtosis": 10.546921023367982,
        "return_acf_1": -0.14259215649268026,
        "abs_return_acf_1": 0.32999863804958074,
        "abs_return_acf_5": 0.365011143986586,
        "abs_return_acf_20": 0.2734407220624848,
        "quantile_01": -0.04975805254739192,
        "quantile_99": 0.052156954112738886,
        "hill_tail_index": 3.216764489965309
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017525953008885976,
        "excess_kurtosis": 7.352718929703457,
        "return_acf_1": -0.09381969007300818,
        "abs_return_acf_1": 0.36367089485185367,
        "abs_return_acf_5": 0.32180812320781993,
        "abs_return_acf_20": 0.2424251190672294,
        "quantile_01": -0.05446924673066434,
        "quantile_99": 0.05069726565979181,
        "hill_tail_index": 3.7311429840571226
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016078577451758547,
        "excess_kurtosis": 5.8822141538524715,
        "return_acf_1": -0.12282346405234801,
        "abs_return_acf_1": 0.21945628033712478,
        "abs_return_acf_5": 0.21243778490279433,
        "abs_return_acf_20": 0.18372862759904632,
        "quantile_01": -0.04437539741533727,
        "quantile_99": 0.043968573784763355,
        "hill_tail_index": 2.953838684962279
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01926225703919576,
        "excess_kurtosis": 8.14896060083217,
        "return_acf_1": -0.10029639024357756,
        "abs_return_acf_1": 0.3831215694730113,
        "abs_return_acf_5": 0.33312770101740236,
        "abs_return_acf_20": 0.2853361562429658,
        "quantile_01": -0.06561499672524337,
        "quantile_99": 0.0585548933157759,
        "hill_tail_index": 3.9230989385572665
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01824226038991104,
        "excess_kurtosis": 16.995475260511544,
        "return_acf_1": -0.05443453858873067,
        "abs_return_acf_1": 0.40432541092122604,
        "abs_return_acf_5": 0.43653319887845304,
        "abs_return_acf_20": 0.2847152741418149,
        "quantile_01": -0.04819640120633003,
        "quantile_99": 0.04776780497346305,
        "hill_tail_index": 2.6805851876026927
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018677267454202708,
        "excess_kurtosis": 5.067062051228913,
        "return_acf_1": -0.06114650671464801,
        "abs_return_acf_1": 0.3431273528643583,
        "abs_return_acf_5": 0.34591531550306165,
        "abs_return_acf_20": 0.28556454438665224,
        "quantile_01": -0.05837225851015774,
        "quantile_99": 0.0517388362620482,
        "hill_tail_index": 3.1986330513723997
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01923234642364228,
        "excess_kurtosis": 8.8145819447831,
        "return_acf_1": -0.15334954967735373,
        "abs_return_acf_1": 0.3166406328145257,
        "abs_return_acf_5": 0.34477928616113906,
        "abs_return_acf_20": 0.24141955787484234,
        "quantile_01": -0.04980164414265145,
        "quantile_99": 0.055914038350563564,
        "hill_tail_index": 2.503185392611735
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019708216948043696,
        "excess_kurtosis": 6.412744117433503,
        "return_acf_1": -0.08789386688304497,
        "abs_return_acf_1": 0.29005028496399904,
        "abs_return_acf_5": 0.2921984858972516,
        "abs_return_acf_20": 0.2348136505612672,
        "quantile_01": -0.057018403207995706,
        "quantile_99": 0.05593463370914056,
        "hill_tail_index": 3.1035647418226313
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018851947310941735,
        "excess_kurtosis": 10.026416098489056,
        "return_acf_1": -0.07606436216516979,
        "abs_return_acf_1": 0.32954477630078916,
        "abs_return_acf_5": 0.24867553843331017,
        "abs_return_acf_20": 0.27665821912789884,
        "quantile_01": -0.06197617794955627,
        "quantile_99": 0.05239184469525518,
        "hill_tail_index": 3.0869812601170823
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016742657932188192,
        "excess_kurtosis": 3.4782123623695256,
        "return_acf_1": -0.09569135394165161,
        "abs_return_acf_1": 0.2635889940261306,
        "abs_return_acf_5": 0.2413270474334768,
        "abs_return_acf_20": 0.18094874505306835,
        "quantile_01": -0.048164535799389924,
        "quantile_99": 0.0416989096800605,
        "hill_tail_index": 3.616228126567159
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018310503638045074,
        "excess_kurtosis": 6.841332380941367,
        "return_acf_1": -0.12175748945085103,
        "abs_return_acf_1": 0.3299709711883797,
        "abs_return_acf_5": 0.36068223956963175,
        "abs_return_acf_20": 0.29950319363948485,
        "quantile_01": -0.05008569163129405,
        "quantile_99": 0.04945782648018053,
        "hill_tail_index": 2.7981021714491123
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01902753611924682,
        "excess_kurtosis": 12.562570068948547,
        "return_acf_1": 0.0402185455748402,
        "abs_return_acf_1": 0.4581183827528667,
        "abs_return_acf_5": 0.3159001473175075,
        "abs_return_acf_20": 0.4066287572888088,
        "quantile_01": -0.05890820922652825,
        "quantile_99": 0.06119075577616813,
        "hill_tail_index": 2.1760972152790314
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

Firm policy: npv_discrete
Training: False
Coverage status: not_applicable
Unseen state share: None
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
