# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27152
Run ID: `32d3219007808ed38ed22decabe07fda927da84124186150b1b93e614b630c0c`
Result fingerprint: `7cc4cc62bc91ce0b4a98ce6ba905e7750ce0f4f1673a50950eeeed68871dc19b`

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
    "equal_weight_sd": -0.6932976190476159,
    "equal_weight_raw": -10.399464285714236,
    "fixed_start_cap_weight_sd": -0.688990483772704,
    "fixed_start_cap_weight_raw": -10.334857256590562,
    "end_cap_weight_sd": -0.6993106146954996,
    "end_cap_weight_raw": -10.489659220432491
  },
  "full_period_change": {
    "equal_weight_sd": -1.074571428571424,
    "equal_weight_raw": -16.11857142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9966157407407363,
    "inflation_mean_sd": 0.7640003306878308
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2590833333333365,
    "equal_weight_raw": 3.886250000000047,
    "fixed_start_cap_weight_sd": 0.2633904686082483,
    "fixed_start_cap_weight_raw": 3.950857029123725,
    "end_cap_weight_sd": 0.25307033768545295,
    "end_cap_weight_raw": 3.796055065281794
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5940476190476157,
      "change_raw": -8.910714285714235,
      "decay_adjusted_gain_sd": 0.35833333333333656
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6998809523809492,
      "change_raw": -10.498214285714237,
      "decay_adjusted_gain_sd": 0.25250000000000306
    },
    "small": {
      "count": 18,
      "change_sd": -0.7065476190476159,
      "change_raw": -10.598214285714239,
      "decay_adjusted_gain_sd": 0.24583333333333648
    },
    "large_minus_small_sd": 0.11250000000000016,
    "large_minus_small_raw": 1.6875000000000022
  },
  "inflation": {
    "initial_mean_sd": 0.3919166666666667,
    "final_mean_sd": 0.7713333333333333,
    "mean_sd": 0.605864279766861,
    "mean_absolute_raw_gap": 9.087964196502915,
    "final_absolute_raw_gap": 11.57,
    "mean_range_fraction": 0.09087964196502915
  },
  "impact": {
    "initial_share": 0.19333333333333333,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.16273103391729413,
    "final_wealth_share": 0.27141301674264584
  },
  "pricing_slope": {
    "mean": -0.000569248108842498,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.08406444695187162,
    "real_improvement_cost": 0.06903594079124362,
    "washing_cost": 0.015028506160627994,
    "fine_transfer": 0.017644732773125553,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10170917972499718,
    "resource_cost_fraction_initial_cap": 0.0028021482317290543,
    "private_net_outflow_fraction_initial_cap": 0.0033903059908332394,
    "fine_transfer_fraction_initial_cap": 0.0005881577591041851,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0030778765441415346,
    "unapplied_final_day_resource_cost": 0.003380464689865166
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 92.45882512556096,
    "beneficial_raw_gain_per_resource_cost": 1386.8823768834145,
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
    "accrued_cost": 3.2166897045800824,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.2404992283896061,
    "accrued_cost_fraction_initial_cap": 0.10722299015266941,
    "mean_contract_rate": 0.04398255162639824,
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
    "maximum_relative_cash_error": 2.0817970576767243e-15,
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
      "minimum": -0.18347561638141194,
      "maximum": -0.01593003651937139,
      "mean": -0.10039718729711046,
      "median": -0.09344244779998745,
      "quantile_05": -0.16825731843338995,
      "quantile_95": -0.05895302959355186
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
      "minimum": 0.2670145791566758,
      "maximum": 0.8067525442599116,
      "mean": 0.5165607378462325,
      "median": 0.4988412828665079,
      "quantile_05": 0.3053571104341946,
      "quantile_95": 0.7650306491295559
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
        "daily_volatility": 0.018112202925733997,
        "excess_kurtosis": 5.993384908901156,
        "return_acf_1": -0.01593003651937139,
        "abs_return_acf_1": 0.34339737225704065,
        "abs_return_acf_5": 0.2936705888730041,
        "abs_return_acf_20": 0.2959596538319837,
        "quantile_01": -0.05708318352706023,
        "quantile_99": 0.05024554628322731,
        "hill_tail_index": 2.886438813788046
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021703751236241707,
        "excess_kurtosis": 7.0838424353899185,
        "return_acf_1": -0.0852795845215387,
        "abs_return_acf_1": 0.4111712660714243,
        "abs_return_acf_5": 0.3922993303198634,
        "abs_return_acf_20": 0.3608114410990406,
        "quantile_01": -0.07881372547439246,
        "quantile_99": 0.0572895511678312,
        "hill_tail_index": 3.072449305599083
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019644698262054654,
        "excess_kurtosis": 3.2001279355264005,
        "return_acf_1": -0.08842899899659021,
        "abs_return_acf_1": 0.28508862761050763,
        "abs_return_acf_5": 0.28952690728747277,
        "abs_return_acf_20": 0.31010739260963033,
        "quantile_01": -0.062379896756483574,
        "quantile_99": 0.053788479634134086,
        "hill_tail_index": 4.204998771733399
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017857256629821957,
        "excess_kurtosis": 8.69032309616243,
        "return_acf_1": -0.1197947554262978,
        "abs_return_acf_1": 0.3236319358165884,
        "abs_return_acf_5": 0.29918239449619755,
        "abs_return_acf_20": 0.188666159997547,
        "quantile_01": -0.05330186923652927,
        "quantile_99": 0.05170331644264537,
        "hill_tail_index": 2.7287135821275457
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02315517085960573,
        "excess_kurtosis": 8.552348376284328,
        "return_acf_1": -0.13119122093334698,
        "abs_return_acf_1": 0.4090897242807245,
        "abs_return_acf_5": 0.3826540106849128,
        "abs_return_acf_20": 0.3562776703458257,
        "quantile_01": -0.087008168334343,
        "quantile_99": 0.07760911460882963,
        "hill_tail_index": 4.959449610885819
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02249424433746414,
        "excess_kurtosis": 10.725936654875907,
        "return_acf_1": -0.08932615337784215,
        "abs_return_acf_1": 0.4373682243466062,
        "abs_return_acf_5": 0.4607939396254069,
        "abs_return_acf_20": 0.3015588291706027,
        "quantile_01": -0.07801471388576481,
        "quantile_99": 0.06290433251048452,
        "hill_tail_index": 2.8970855945220033
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023112985131792066,
        "excess_kurtosis": 12.489223359468111,
        "return_acf_1": -0.07523682382280093,
        "abs_return_acf_1": 0.47822349969375544,
        "abs_return_acf_5": 0.4657652324748796,
        "abs_return_acf_20": 0.35093138150837644,
        "quantile_01": -0.09131464508342399,
        "quantile_99": 0.06049394559404942,
        "hill_tail_index": 2.6298515718435738
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01886679636064739,
        "excess_kurtosis": 3.4558518213815645,
        "return_acf_1": -0.0996552857388245,
        "abs_return_acf_1": 0.29490410896892333,
        "abs_return_acf_5": 0.2721402992612127,
        "abs_return_acf_20": 0.2747108371419605,
        "quantile_01": -0.06031943664315353,
        "quantile_99": 0.05177729086028004,
        "hill_tail_index": 4.129551662075075
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017442088054562085,
        "excess_kurtosis": 2.7011233430625374,
        "return_acf_1": -0.11063137361074493,
        "abs_return_acf_1": 0.26932816862033626,
        "abs_return_acf_5": 0.27477657796344346,
        "abs_return_acf_20": 0.24910092503368017,
        "quantile_01": -0.041715498084525814,
        "quantile_99": 0.046584536371351154,
        "hill_tail_index": 3.983239792360117
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02134073569383371,
        "excess_kurtosis": 6.643091128189775,
        "return_acf_1": -0.09755874222213276,
        "abs_return_acf_1": 0.4225441692176809,
        "abs_return_acf_5": 0.3927378228303451,
        "abs_return_acf_20": 0.3467105890193928,
        "quantile_01": -0.0723108293390234,
        "quantile_99": 0.06071777103854884,
        "hill_tail_index": 3.629203821101503
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01700834479986279,
        "excess_kurtosis": 6.704319135948822,
        "return_acf_1": -0.18058550975339646,
        "abs_return_acf_1": 0.32756617012924677,
        "abs_return_acf_5": 0.33223340946694074,
        "abs_return_acf_20": 0.22822496413614432,
        "quantile_01": -0.047520655995508185,
        "quantile_99": 0.048406006478829866,
        "hill_tail_index": 2.991487678143907
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02270495061592771,
        "excess_kurtosis": 9.618693702732699,
        "return_acf_1": -0.08076696686706479,
        "abs_return_acf_1": 0.4054636623636523,
        "abs_return_acf_5": 0.41618389541094264,
        "abs_return_acf_20": 0.36119996375630475,
        "quantile_01": -0.09056355832951307,
        "quantile_99": 0.07496645389700211,
        "hill_tail_index": 3.7052718805917344
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019912500939192293,
        "excess_kurtosis": 9.025080527469054,
        "return_acf_1": -0.11679536211321433,
        "abs_return_acf_1": 0.38261663465488316,
        "abs_return_acf_5": 0.31129569641348087,
        "abs_return_acf_20": 0.27299424431630326,
        "quantile_01": -0.060834096162129606,
        "quantile_99": 0.051351713800975474,
        "hill_tail_index": 3.3134120139757317
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02283962208599186,
        "excess_kurtosis": 9.683490717383375,
        "return_acf_1": -0.07041208597790788,
        "abs_return_acf_1": 0.34972793415729114,
        "abs_return_acf_5": 0.35994439382632426,
        "abs_return_acf_20": 0.34845725517615656,
        "quantile_01": -0.07210529347001156,
        "quantile_99": 0.06613107651834786,
        "hill_tail_index": 2.719152206995201
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022542692133577943,
        "excess_kurtosis": 9.981769128154285,
        "return_acf_1": -0.08027869960224024,
        "abs_return_acf_1": 0.38495558259799795,
        "abs_return_acf_5": 0.4279339531983347,
        "abs_return_acf_20": 0.34565816956329365,
        "quantile_01": -0.08375636131816117,
        "quantile_99": 0.06667685836198073,
        "hill_tail_index": 3.548776985853027
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0197486416086289,
        "excess_kurtosis": 6.564181684637564,
        "return_acf_1": -0.15318952904227087,
        "abs_return_acf_1": 0.3843228804495707,
        "abs_return_acf_5": 0.35353504735247937,
        "abs_return_acf_20": 0.3533393253646209,
        "quantile_01": -0.06545893597789595,
        "quantile_99": 0.0550387140923377,
        "hill_tail_index": 3.0157636259946874
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01846463432054213,
        "excess_kurtosis": 6.403766471205136,
        "return_acf_1": -0.13343815869268605,
        "abs_return_acf_1": 0.2660433451547552,
        "abs_return_acf_5": 0.2956269928667542,
        "abs_return_acf_20": 0.23349971889528273,
        "quantile_01": -0.05481077264294554,
        "quantile_99": 0.045868191548504224,
        "hill_tail_index": 3.1694347715953097
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022099585681914048,
        "excess_kurtosis": 13.115732386465165,
        "return_acf_1": -0.10975268898127323,
        "abs_return_acf_1": 0.36410273278499006,
        "abs_return_acf_5": 0.44114335734612004,
        "abs_return_acf_20": 0.2989028710829319,
        "quantile_01": -0.07933065178216148,
        "quantile_99": 0.06123808155889536,
        "hill_tail_index": 3.473032612033744
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020530026778518715,
        "excess_kurtosis": 6.353934245360584,
        "return_acf_1": -0.08283442668069366,
        "abs_return_acf_1": 0.3218907301810708,
        "abs_return_acf_5": 0.35156876042235335,
        "abs_return_acf_20": 0.26060946821720726,
        "quantile_01": -0.058197077333049324,
        "quantile_99": 0.058327530862013324,
        "hill_tail_index": 3.3322181135912174
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016732829955891176,
        "excess_kurtosis": 4.217276778366504,
        "return_acf_1": -0.10763429335034382,
        "abs_return_acf_1": 0.24599391520536815,
        "abs_return_acf_5": 0.18715984630104404,
        "abs_return_acf_20": 0.23949895489223158,
        "quantile_01": -0.05181915801951482,
        "quantile_99": 0.04289905060157158,
        "hill_tail_index": 2.9809466338932427
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020335488402812282,
        "excess_kurtosis": 4.691969248246951,
        "return_acf_1": -0.06847672682702749,
        "abs_return_acf_1": 0.32896439571045283,
        "abs_return_acf_5": 0.340673410710807,
        "abs_return_acf_20": 0.35373773568819555,
        "quantile_01": -0.066446762558571,
        "quantile_99": 0.05466663005286152,
        "hill_tail_index": 3.818450764753518
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020211948169713,
        "excess_kurtosis": 10.229121540177609,
        "return_acf_1": -0.13736057465449006,
        "abs_return_acf_1": 0.3600396535079241,
        "abs_return_acf_5": 0.3142476206632449,
        "abs_return_acf_20": 0.3070275414516667,
        "quantile_01": -0.06677352150235018,
        "quantile_99": 0.053781216155770674,
        "hill_tail_index": 2.8269957300814204
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019466797284724387,
        "excess_kurtosis": 7.226983409041171,
        "return_acf_1": -0.05911029216759231,
        "abs_return_acf_1": 0.30582409183159476,
        "abs_return_acf_5": 0.3216814462897528,
        "abs_return_acf_20": 0.2962526770432497,
        "quantile_01": -0.062249618731580886,
        "quantile_99": 0.0590923870164315,
        "hill_tail_index": 3.4273154829835395
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017653116207759778,
        "excess_kurtosis": 4.385094301443746,
        "return_acf_1": -0.05882436021479148,
        "abs_return_acf_1": 0.3127264514897799,
        "abs_return_acf_5": 0.23030742802460155,
        "abs_return_acf_20": 0.23929129925298262,
        "quantile_01": -0.04744561840537507,
        "quantile_99": 0.05061370953240466,
        "hill_tail_index": 3.370279440742514
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020525071025779114,
        "excess_kurtosis": 11.125411831771428,
        "return_acf_1": -0.08596604550338534,
        "abs_return_acf_1": 0.38881276329345993,
        "abs_return_acf_5": 0.38874770375887446,
        "abs_return_acf_20": 0.30393581744543446,
        "quantile_01": -0.06484001147608741,
        "quantile_99": 0.05614505227619849,
        "hill_tail_index": 2.544306788687067
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019692426575349198,
        "excess_kurtosis": 6.3126484244113765,
        "return_acf_1": -0.07551201965146705,
        "abs_return_acf_1": 0.2795461913507841,
        "abs_return_acf_5": 0.29056983108507106,
        "abs_return_acf_20": 0.24027928911369736,
        "quantile_01": -0.05825848265235644,
        "quantile_99": 0.056135215503772276,
        "hill_tail_index": 3.834815472062129
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017613942710798476,
        "excess_kurtosis": 7.674496789383715,
        "return_acf_1": -0.18347561638141194,
        "abs_return_acf_1": 0.2717112989977461,
        "abs_return_acf_5": 0.3146309708094208,
        "abs_return_acf_20": 0.20375184146581474,
        "quantile_01": -0.04810452308844204,
        "quantile_99": 0.04742437409718273,
        "hill_tail_index": 2.9016401346705347
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.015217355313219568,
        "excess_kurtosis": 4.446441236579664,
        "return_acf_1": -0.10197555691229902,
        "abs_return_acf_1": 0.23173866806938048,
        "abs_return_acf_5": 0.2039367909685988,
        "abs_return_acf_20": 0.18578526605995319,
        "quantile_01": -0.03978704213287608,
        "quantile_99": 0.03623995106545286,
        "hill_tail_index": 3.1353293896080876
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022689799617927144,
        "excess_kurtosis": 8.492509855667691,
        "return_acf_1": -0.14823928778175588,
        "abs_return_acf_1": 0.40060068562108136,
        "abs_return_acf_5": 0.4302019395274195,
        "abs_return_acf_20": 0.3379710489099046,
        "quantile_01": -0.08301220861217604,
        "quantile_99": 0.06349313063751318,
        "hill_tail_index": 3.574348885374372
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01991273123021029,
        "excess_kurtosis": 3.6223832379351766,
        "return_acf_1": -0.06425444258851168,
        "abs_return_acf_1": 0.3565255943024719,
        "abs_return_acf_5": 0.33974648163056137,
        "abs_return_acf_20": 0.29163093422730585,
        "quantile_01": -0.05514864164674921,
        "quantile_99": 0.059636357409479535,
        "hill_tail_index": 4.360120662286391
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
