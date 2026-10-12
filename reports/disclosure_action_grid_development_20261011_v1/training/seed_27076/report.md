# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27076
Run ID: `8a381e6ceab3fcafb8bfe0bde4d702ac99943423ef928e5e29fcde1cac5e62de`
Result fingerprint: `f49261d32ab5a32f58896882648cc539dabb1d886d9777ef5a253ab658bd7d1d`

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
    "equal_weight_sd": -0.5005476190476158,
    "equal_weight_raw": -7.508214285714237,
    "fixed_start_cap_weight_sd": -0.5581945435112016,
    "fixed_start_cap_weight_raw": -8.372918152668026,
    "end_cap_weight_sd": -0.5917151274167317,
    "end_cap_weight_raw": -8.875726911250974
  },
  "full_period_change": {
    "equal_weight_sd": -0.8253214285714237,
    "equal_weight_raw": -12.379821428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7852017195767151,
    "inflation_mean_sd": 0.5893349867724867
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4518333333333365,
    "equal_weight_raw": 6.777500000000048,
    "fixed_start_cap_weight_sd": 0.3941864088697507,
    "fixed_start_cap_weight_raw": 5.91279613304626,
    "end_cap_weight_sd": 0.3606658249642206,
    "end_cap_weight_raw": 5.40998737446331
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5807142857142825,
      "change_raw": -8.710714285714237,
      "decay_adjusted_gain_sd": 0.37166666666666986
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4434920634920603,
      "change_raw": -6.652380952380904,
      "decay_adjusted_gain_sd": 0.508888888888892
    },
    "small": {
      "count": 18,
      "change_sd": -0.5157142857142826,
      "change_raw": -7.735714285714239,
      "decay_adjusted_gain_sd": 0.4366666666666698
    },
    "large_minus_small_sd": -0.06499999999999995,
    "large_minus_small_raw": -0.9749999999999992
  },
  "inflation": {
    "initial_mean_sd": 0.25549999999999995,
    "final_mean_sd": 0.6245833333333334,
    "mean_sd": 0.4493821121287816,
    "mean_absolute_raw_gap": 6.740731681931724,
    "final_absolute_raw_gap": 9.368750000000002,
    "mean_range_fraction": 0.06740731681931723
  },
  "impact": {
    "initial_share": 0.25333333333333335,
    "final_share": 0.3333333333333333,
    "initial_wealth_share": 0.2614464779524225,
    "final_wealth_share": 0.34610778307155105
  },
  "pricing_slope": {
    "mean": -0.0009062900169696221,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.09079981144892617,
    "real_improvement_cost": 0.08145164336996043,
    "washing_cost": 0.009348168078965723,
    "fine_transfer": 0.004584726457664596,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.09538453790659077,
    "resource_cost_fraction_initial_cap": 0.0030266603816308728,
    "private_net_outflow_fraction_initial_cap": 0.003179484596886359,
    "fine_transfer_fraction_initial_cap": 0.00015282421525548656,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.010474456555236527,
    "unapplied_final_day_resource_cost": 0.0012754189409519424
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 149.28445096633953,
    "beneficial_raw_gain_per_resource_cost": 2239.266764495093,
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
    "accrued_cost": 3.212587931034528,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.23639745484405214,
    "accrued_cost_fraction_initial_cap": 0.10708626436781762,
    "mean_contract_rate": 0.04496019975523433,
    "maximum_ledger_error": 9.486769009248164e-20
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
    "maximum_relative_cash_error": 1.335270061072367e-15,
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
      "minimum": -0.2152564603255922,
      "maximum": -0.08464832423870532,
      "mean": -0.16370630630428615,
      "median": -0.15927778860741476,
      "quantile_05": -0.21046389553809378,
      "quantile_95": -0.09779626975783542
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
      "minimum": 0.3080480303003912,
      "maximum": 0.7908198621797157,
      "mean": 0.6037129960355336,
      "median": 0.6268826345786342,
      "quantile_05": 0.37950980321109307,
      "quantile_95": 0.7508807243241948
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
        "daily_volatility": 0.018987992951883394,
        "excess_kurtosis": 14.426141455051152,
        "return_acf_1": -0.15635018814782053,
        "abs_return_acf_1": 0.32083587195072205,
        "abs_return_acf_5": 0.3214773393577652,
        "abs_return_acf_20": 0.20443179889597157,
        "quantile_01": -0.06412279043732615,
        "quantile_99": 0.043248316361915395,
        "hill_tail_index": 2.0387676398648
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018877094449620612,
        "excess_kurtosis": 12.321038753367429,
        "return_acf_1": -0.1614710258152784,
        "abs_return_acf_1": 0.3086638528573049,
        "abs_return_acf_5": 0.34347853632229336,
        "abs_return_acf_20": 0.24366685773390248,
        "quantile_01": -0.057491457598007244,
        "quantile_99": 0.0461656096925962,
        "hill_tail_index": 2.3887038662580524
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018537028027281886,
        "excess_kurtosis": 18.70794835391458,
        "return_acf_1": -0.20527117231471212,
        "abs_return_acf_1": 0.42564042604850566,
        "abs_return_acf_5": 0.362958670112272,
        "abs_return_acf_20": 0.3053709919114146,
        "quantile_01": -0.05687043217955009,
        "quantile_99": 0.03603311913936857,
        "hill_tail_index": 1.6287189926112116
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01879730487559398,
        "excess_kurtosis": 8.810546146352587,
        "return_acf_1": -0.1769178158357813,
        "abs_return_acf_1": 0.3614240086355547,
        "abs_return_acf_5": 0.34544501632283453,
        "abs_return_acf_20": 0.23640826156073513,
        "quantile_01": -0.0635425575839161,
        "quantile_99": 0.05147551270799691,
        "hill_tail_index": 2.869956130394566
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017235027219699047,
        "excess_kurtosis": 6.3995877855524075,
        "return_acf_1": -0.1448379933976974,
        "abs_return_acf_1": 0.3619686269336951,
        "abs_return_acf_5": 0.30386965826248913,
        "abs_return_acf_20": 0.2542187894659704,
        "quantile_01": -0.05751701709163816,
        "quantile_99": 0.044546713669603465,
        "hill_tail_index": 3.013541019664975
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020713692366092436,
        "excess_kurtosis": 12.100316518067988,
        "return_acf_1": -0.17611718669596446,
        "abs_return_acf_1": 0.35088263574656864,
        "abs_return_acf_5": 0.4357717815459306,
        "abs_return_acf_20": 0.3136165878129735,
        "quantile_01": -0.07056701330442323,
        "quantile_99": 0.05791142803412022,
        "hill_tail_index": 2.668419696910115
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018884965483009292,
        "excess_kurtosis": 6.376717631952751,
        "return_acf_1": -0.20096692999005797,
        "abs_return_acf_1": 0.27540178565066337,
        "abs_return_acf_5": 0.3097757519745444,
        "abs_return_acf_20": 0.22384020382644995,
        "quantile_01": -0.05937502654375588,
        "quantile_99": 0.05578117881481948,
        "hill_tail_index": 3.1646544294223697
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020366035392876822,
        "excess_kurtosis": 7.012517881294398,
        "return_acf_1": -0.11703196772889886,
        "abs_return_acf_1": 0.33235048002982504,
        "abs_return_acf_5": 0.35250747863771237,
        "abs_return_acf_20": 0.24124198469304864,
        "quantile_01": -0.07399129215077314,
        "quantile_99": 0.050600932746049994,
        "hill_tail_index": 2.8627597832422267
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018859380844195663,
        "excess_kurtosis": 8.043180207280086,
        "return_acf_1": -0.14710909133365463,
        "abs_return_acf_1": 0.28877693836147406,
        "abs_return_acf_5": 0.3130764390240062,
        "abs_return_acf_20": 0.17727381230442385,
        "quantile_01": -0.0536404251648847,
        "quantile_99": 0.04781255811645646,
        "hill_tail_index": 2.9512214830460857
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018750275307213387,
        "excess_kurtosis": 17.87674628957606,
        "return_acf_1": -0.1952590843489375,
        "abs_return_acf_1": 0.49190142849856516,
        "abs_return_acf_5": 0.3953484467151366,
        "abs_return_acf_20": 0.24836946327260628,
        "quantile_01": -0.0551930720821343,
        "quantile_99": 0.043107008211830763,
        "hill_tail_index": 1.7679347081024044
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016723358287159564,
        "excess_kurtosis": 5.110087362880126,
        "return_acf_1": -0.2093651013660218,
        "abs_return_acf_1": 0.26856007712252905,
        "abs_return_acf_5": 0.24137308734554866,
        "abs_return_acf_20": 0.18592026753415924,
        "quantile_01": -0.0518891780682245,
        "quantile_99": 0.04066265382311105,
        "hill_tail_index": 3.1219322053225547
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020201834493782128,
        "excess_kurtosis": 14.873231910703321,
        "return_acf_1": -0.16575577519070187,
        "abs_return_acf_1": 0.4117570447549794,
        "abs_return_acf_5": 0.43168862652532003,
        "abs_return_acf_20": 0.2683058861453737,
        "quantile_01": -0.07176078853335344,
        "quantile_99": 0.05122453999955462,
        "hill_tail_index": 2.2469940268883244
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018902671642423593,
        "excess_kurtosis": 10.01165180587658,
        "return_acf_1": -0.19746223434236415,
        "abs_return_acf_1": 0.3858897319984348,
        "abs_return_acf_5": 0.35091107235330893,
        "abs_return_acf_20": 0.26649578672543034,
        "quantile_01": -0.06241696665811454,
        "quantile_99": 0.04339493281041198,
        "hill_tail_index": 2.9688983867707575
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019162961440665986,
        "excess_kurtosis": 4.078231266373526,
        "return_acf_1": -0.10511240518707263,
        "abs_return_acf_1": 0.28194332347049184,
        "abs_return_acf_5": 0.3152054982342784,
        "abs_return_acf_20": 0.22843936357998504,
        "quantile_01": -0.06409396993535865,
        "quantile_99": 0.05404608009750421,
        "hill_tail_index": 4.294715231012328
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01985173621545646,
        "excess_kurtosis": 7.338492377812697,
        "return_acf_1": -0.10869665644486387,
        "abs_return_acf_1": 0.31998377757403973,
        "abs_return_acf_5": 0.33800720737255746,
        "abs_return_acf_20": 0.2884851821361634,
        "quantile_01": -0.06855007552707537,
        "quantile_99": 0.054484613743153026,
        "hill_tail_index": 3.043054679406346
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020778457740960467,
        "excess_kurtosis": 11.02078410390038,
        "return_acf_1": -0.15401639548109325,
        "abs_return_acf_1": 0.31190452913499284,
        "abs_return_acf_5": 0.3725831397927784,
        "abs_return_acf_20": 0.28802559236287223,
        "quantile_01": -0.07505870094159206,
        "quantile_99": 0.05026148773314155,
        "hill_tail_index": 2.385603598718757
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019555293007656016,
        "excess_kurtosis": 11.194832889148769,
        "return_acf_1": -0.20835992940770912,
        "abs_return_acf_1": 0.33504103037456073,
        "abs_return_acf_5": 0.29145571663801173,
        "abs_return_acf_20": 0.26751754841430136,
        "quantile_01": -0.055676849295209586,
        "quantile_99": 0.04762043040534941,
        "hill_tail_index": 2.0545656204433618
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01975326512154189,
        "excess_kurtosis": 11.597042492589948,
        "return_acf_1": -0.1740786966395969,
        "abs_return_acf_1": 0.47581155369204403,
        "abs_return_acf_5": 0.4755823241652588,
        "abs_return_acf_20": 0.30444412217250405,
        "quantile_01": -0.07888972999278672,
        "quantile_99": 0.049043017905008604,
        "hill_tail_index": 2.5444273665191584
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018712622778414834,
        "excess_kurtosis": 10.502770268977237,
        "return_acf_1": -0.15488282013542098,
        "abs_return_acf_1": 0.32095246902078944,
        "abs_return_acf_5": 0.2940938860568719,
        "abs_return_acf_20": 0.2397020524586378,
        "quantile_01": -0.06198851731044393,
        "quantile_99": 0.043100407742306376,
        "hill_tail_index": 2.307040088557987
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01844164384911464,
        "excess_kurtosis": 10.59304874453129,
        "return_acf_1": -0.09181034077027765,
        "abs_return_acf_1": 0.36770797337222944,
        "abs_return_acf_5": 0.31073138595757643,
        "abs_return_acf_20": 0.22934252696332877,
        "quantile_01": -0.05632054990198822,
        "quantile_99": 0.047430992023217586,
        "hill_tail_index": 2.51155087499715
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0171539077971086,
        "excess_kurtosis": 7.716636710946636,
        "return_acf_1": -0.12406600645808337,
        "abs_return_acf_1": 0.2574488465106502,
        "abs_return_acf_5": 0.2556868430648369,
        "abs_return_acf_20": 0.16419287124073959,
        "quantile_01": -0.05151731233347234,
        "quantile_99": 0.04335535866741902,
        "hill_tail_index": 2.9963915323415993
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020440994773235147,
        "excess_kurtosis": 11.327797597306738,
        "return_acf_1": -0.2069544011485427,
        "abs_return_acf_1": 0.35166381486553333,
        "abs_return_acf_5": 0.36122747880509315,
        "abs_return_acf_20": 0.26654764673882775,
        "quantile_01": -0.07225109171014224,
        "quantile_99": 0.05375220670174986,
        "hill_tail_index": 2.685290577787805
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01988912669022968,
        "excess_kurtosis": 8.416149258415931,
        "return_acf_1": -0.20533896842696708,
        "abs_return_acf_1": 0.3404101331009999,
        "abs_return_acf_5": 0.3393865927466567,
        "abs_return_acf_20": 0.2623603045381714,
        "quantile_01": -0.06414335142608055,
        "quantile_99": 0.049493003423759854,
        "hill_tail_index": 3.184296269020705
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01998862158833441,
        "excess_kurtosis": 7.1969160881260255,
        "return_acf_1": -0.08464832423870532,
        "abs_return_acf_1": 0.37441680462990745,
        "abs_return_acf_5": 0.36411882164204856,
        "abs_return_acf_20": 0.2721169807808262,
        "quantile_01": -0.061527416948756686,
        "quantile_99": 0.053852947850110515,
        "hill_tail_index": 2.856977902184145
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019194410835243533,
        "excess_kurtosis": 10.877091404980744,
        "return_acf_1": -0.15515326460305287,
        "abs_return_acf_1": 0.348173435564206,
        "abs_return_acf_5": 0.34227584209309897,
        "abs_return_acf_20": 0.22240998760790293,
        "quantile_01": -0.0686175758903356,
        "quantile_99": 0.052793046445817844,
        "hill_tail_index": 3.10649943220048
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01962264365340179,
        "excess_kurtosis": 15.35717238752111,
        "return_acf_1": -0.15515152699807833,
        "abs_return_acf_1": 0.3584681067294992,
        "abs_return_acf_5": 0.3336647825521978,
        "abs_return_acf_20": 0.22585392796597253,
        "quantile_01": -0.05610269495463371,
        "quantile_99": 0.04677780664997535,
        "hill_tail_index": 2.425733232664544
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019552717787680744,
        "excess_kurtosis": 22.402916397719356,
        "return_acf_1": -0.2152564603255922,
        "abs_return_acf_1": 0.36089826656789453,
        "abs_return_acf_5": 0.370452332788826,
        "abs_return_acf_20": 0.2332589647317504,
        "quantile_01": -0.05716653715073034,
        "quantile_99": 0.04504822515093344,
        "hill_tail_index": 2.789976319500542
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01763676548042493,
        "excess_kurtosis": 9.18434748677604,
        "return_acf_1": -0.14529996600447836,
        "abs_return_acf_1": 0.2845686167686071,
        "abs_return_acf_5": 0.2767401344267631,
        "abs_return_acf_20": 0.20024919220799692,
        "quantile_01": -0.06052486486763377,
        "quantile_99": 0.04262519315099998,
        "hill_tail_index": 2.688921251380783
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020021786025613914,
        "excess_kurtosis": 9.415826152677903,
        "return_acf_1": -0.21136290895160723,
        "abs_return_acf_1": 0.36576547523201464,
        "abs_return_acf_5": 0.28962109868135877,
        "abs_return_acf_20": 0.20114199936308524,
        "quantile_01": -0.06787353615972676,
        "quantile_99": 0.047035134106763195,
        "hill_tail_index": 2.513305058109741
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020741307078750888,
        "excess_kurtosis": 11.05521873148183,
        "return_acf_1": -0.15708455139955113,
        "abs_return_acf_1": 0.3885814573373974,
        "abs_return_acf_5": 0.3916524444169636,
        "abs_return_acf_20": 0.2816498461045623,
        "quantile_01": -0.07803110478575134,
        "quantile_99": 0.05672071520995443,
        "hill_tail_index": 2.645972073326371
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
