# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27080
Run ID: `a7d18f3a3265e41764b544be0b3080a7c9b1508bdfe68244d9e8f4d6f2797e22`
Result fingerprint: `5d562308bb3b37b3f7bc581c82a9eeca8241b9472437ba6a95c9f83181d09618`

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
    "equal_weight_sd": -0.5879642857142825,
    "equal_weight_raw": -8.81946428571424,
    "fixed_start_cap_weight_sd": -0.6286255279061328,
    "fixed_start_cap_weight_raw": -9.429382918591994,
    "end_cap_weight_sd": -0.6209082465758982,
    "end_cap_weight_raw": -9.31362369863847
  },
  "full_period_change": {
    "equal_weight_sd": -0.8573214285714238,
    "equal_weight_raw": -12.859821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7942784391534347,
    "inflation_mean_sd": 0.703421626984127
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3616635678856016,
    "equal_weight_raw": 5.424953518284024,
    "fixed_start_cap_weight_sd": 0.3211301029270839,
    "fixed_start_cap_weight_raw": 4.816951543906258,
    "end_cap_weight_sd": 0.3290806724981566,
    "end_cap_weight_raw": 4.9362100874723485
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7248809523809493,
      "change_raw": -10.873214285714239,
      "decay_adjusted_gain_sd": 0.22750000000000323
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5668253968253935,
      "change_raw": -8.502380952380902,
      "decay_adjusted_gain_sd": 0.38555555555555876
    },
    "small": {
      "count": 18,
      "change_sd": -0.5757142857142825,
      "change_raw": -8.635714285714238,
      "decay_adjusted_gain_sd": 0.37207816869822286
    },
    "large_minus_small_sd": -0.14916666666666678,
    "large_minus_small_raw": -2.2375000000000016
  },
  "inflation": {
    "initial_mean_sd": 0.2828333333333333,
    "final_mean_sd": 0.7603333333333333,
    "mean_sd": 0.5149725228975853,
    "mean_absolute_raw_gap": 7.724587843463781,
    "final_absolute_raw_gap": 11.405000000000001,
    "mean_range_fraction": 0.07724587843463782
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.17715436454914918,
    "final_wealth_share": 0.27491651443008064
  },
  "pricing_slope": {
    "mean": -0.0023479324201476524,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.3168543196191841,
    "real_improvement_cost": 0.28963679505923456,
    "washing_cost": 0.02721752455994951,
    "fine_transfer": 0.010834506220944787,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3276888258401289,
    "resource_cost_fraction_initial_cap": 0.010561810653972806,
    "private_net_outflow_fraction_initial_cap": 0.010922960861337632,
    "fine_transfer_fraction_initial_cap": 0.00036115020736482634,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002158718171011718,
    "unapplied_final_day_resource_cost": 0.002152664723613101
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 34.24257257912142,
    "beneficial_raw_gain_per_resource_cost": 513.6385886868213,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 3.253650672898517,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": -0.2774601967080411,
    "accrued_cost_fraction_initial_cap": 0.10845502242995059,
    "mean_contract_rate": 0.044717424269733755,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 1.3892283646366814e-15,
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
      "minimum": -0.2476783481507129,
      "maximum": -0.08600409718717057,
      "mean": -0.1629942080019984,
      "median": -0.1551701811859917,
      "quantile_05": -0.23265636547079788,
      "quantile_95": -0.09879992140880836
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
      "minimum": 0.3856312154897126,
      "maximum": 0.7928968906478262,
      "mean": 0.5841961283874176,
      "median": 0.5794243185103928,
      "quantile_05": 0.4478720810872147,
      "quantile_95": 0.7248371622826619
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
        "daily_volatility": 0.020764341268837656,
        "excess_kurtosis": 20.280949597279367,
        "return_acf_1": -0.2289536636174017,
        "abs_return_acf_1": 0.31933625497686935,
        "abs_return_acf_5": 0.27583511536752814,
        "abs_return_acf_20": 0.2547692401652402,
        "quantile_01": -0.059690566789156546,
        "quantile_99": 0.04670049022617954,
        "hill_tail_index": 1.9387790534737377
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01885905394542668,
        "excess_kurtosis": 5.2265935897821425,
        "return_acf_1": -0.11298949250490227,
        "abs_return_acf_1": 0.2776799544880233,
        "abs_return_acf_5": 0.2890364755392186,
        "abs_return_acf_20": 0.20621895404334634,
        "quantile_01": -0.06112229594358925,
        "quantile_99": 0.04995299420562938,
        "hill_tail_index": 3.4998629113947417
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.0174748478718939,
        "excess_kurtosis": 3.0549325692711946,
        "return_acf_1": -0.13344243696764582,
        "abs_return_acf_1": 0.2933113908545825,
        "abs_return_acf_5": 0.30786230048459706,
        "abs_return_acf_20": 0.30008339797225975,
        "quantile_01": -0.05526944515466118,
        "quantile_99": 0.05307299090948149,
        "hill_tail_index": 6.080032857492638
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01776701269962859,
        "excess_kurtosis": 5.788000312811457,
        "return_acf_1": -0.160413731276594,
        "abs_return_acf_1": 0.2509516713162476,
        "abs_return_acf_5": 0.2627763188888066,
        "abs_return_acf_20": 0.1833933473604018,
        "quantile_01": -0.05343685320421043,
        "quantile_99": 0.04605097330663734,
        "hill_tail_index": 3.0042922979698825
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018059237102478642,
        "excess_kurtosis": 2.885607594158582,
        "return_acf_1": -0.13006136482784927,
        "abs_return_acf_1": 0.27594036389265525,
        "abs_return_acf_5": 0.28860264831156945,
        "abs_return_acf_20": 0.24963571509681798,
        "quantile_01": -0.060990620482234484,
        "quantile_99": 0.0424681597862855,
        "hill_tail_index": 3.800190002530499
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01722949681756716,
        "excess_kurtosis": 2.470257920411526,
        "return_acf_1": -0.13321386150781148,
        "abs_return_acf_1": 0.24304923573443737,
        "abs_return_acf_5": 0.2644717068931633,
        "abs_return_acf_20": 0.1772348943166938,
        "quantile_01": -0.05149881892315791,
        "quantile_99": 0.04278980051275372,
        "hill_tail_index": 4.719488393656877
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02128238199089492,
        "excess_kurtosis": 13.273828176489204,
        "return_acf_1": -0.23051826114443513,
        "abs_return_acf_1": 0.3675612010679443,
        "abs_return_acf_5": 0.36679786711758117,
        "abs_return_acf_20": 0.2962141919639132,
        "quantile_01": -0.07437482431048638,
        "quantile_99": 0.04623288564276339,
        "hill_tail_index": 1.8618788717678303
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020312706281218642,
        "excess_kurtosis": 13.246514980377604,
        "return_acf_1": -0.19171930947594962,
        "abs_return_acf_1": 0.3950767009919282,
        "abs_return_acf_5": 0.36317880475094066,
        "abs_return_acf_20": 0.2895625815539467,
        "quantile_01": -0.07463209030223852,
        "quantile_99": 0.048079894285006405,
        "hill_tail_index": 2.189541466189621
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02248361103825968,
        "excess_kurtosis": 10.481557366006,
        "return_acf_1": -0.19366138425750232,
        "abs_return_acf_1": 0.4546020474940975,
        "abs_return_acf_5": 0.367835548358277,
        "abs_return_acf_20": 0.3292629160412655,
        "quantile_01": -0.07650686142702595,
        "quantile_99": 0.06945387639212215,
        "hill_tail_index": 3.62686447319876
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0190930209935463,
        "excess_kurtosis": 4.244722036850041,
        "return_acf_1": -0.14992663109538942,
        "abs_return_acf_1": 0.35313995263347536,
        "abs_return_acf_5": 0.2934555424863853,
        "abs_return_acf_20": 0.280803268764524,
        "quantile_01": -0.05856874382596539,
        "quantile_99": 0.05180959195863547,
        "hill_tail_index": 4.234731630134294
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018679411341804633,
        "excess_kurtosis": 2.3444592610931974,
        "return_acf_1": -0.18220470092740257,
        "abs_return_acf_1": 0.3054009561311961,
        "abs_return_acf_5": 0.333299587473731,
        "abs_return_acf_20": 0.2617545390913364,
        "quantile_01": -0.0534184315184967,
        "quantile_99": 0.052983006964916445,
        "hill_tail_index": 6.3784753132458
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01993423302007253,
        "excess_kurtosis": 10.754683144227286,
        "return_acf_1": -0.22642094006678462,
        "abs_return_acf_1": 0.29523008874565926,
        "abs_return_acf_5": 0.25039549425994434,
        "abs_return_acf_20": 0.32135041812524584,
        "quantile_01": -0.06895258155562826,
        "quantile_99": 0.050718099139210354,
        "hill_tail_index": 1.9926315259628766
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017761651191212362,
        "excess_kurtosis": 4.571877619777336,
        "return_acf_1": -0.10895164815194676,
        "abs_return_acf_1": 0.29810533239281584,
        "abs_return_acf_5": 0.24418134718274082,
        "abs_return_acf_20": 0.22770092671663167,
        "quantile_01": -0.05183700957433283,
        "quantile_99": 0.04453614886468485,
        "hill_tail_index": 3.7455352762933782
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019990042967620705,
        "excess_kurtosis": 6.8341956889273625,
        "return_acf_1": -0.20169825716203246,
        "abs_return_acf_1": 0.34599018376352025,
        "abs_return_acf_5": 0.2136055324110998,
        "abs_return_acf_20": 0.23871062083120675,
        "quantile_01": -0.060911249553943815,
        "quantile_99": 0.05841783157564837,
        "hill_tail_index": 3.18506322112464
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0178976850941625,
        "excess_kurtosis": 3.2770410741609375,
        "return_acf_1": -0.0982359015047544,
        "abs_return_acf_1": 0.26926050391839,
        "abs_return_acf_5": 0.24155542580998818,
        "abs_return_acf_20": 0.21107555366623174,
        "quantile_01": -0.05598913482018329,
        "quantile_99": 0.05075239740048266,
        "hill_tail_index": 3.822288463531799
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017997410324929977,
        "excess_kurtosis": 4.298999320800546,
        "return_acf_1": -0.18460104127121846,
        "abs_return_acf_1": 0.28082348665883616,
        "abs_return_acf_5": 0.2420164677805216,
        "abs_return_acf_20": 0.23997493934368425,
        "quantile_01": -0.05740093599454562,
        "quantile_99": 0.04831103982578172,
        "hill_tail_index": 3.9698835691641503
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020121752278622514,
        "excess_kurtosis": 15.397575557344823,
        "return_acf_1": -0.18875900646212856,
        "abs_return_acf_1": 0.44491368708114293,
        "abs_return_acf_5": 0.41412682403302237,
        "abs_return_acf_20": 0.22996266572969895,
        "quantile_01": -0.06912878960577247,
        "quantile_99": 0.04298676082060206,
        "hill_tail_index": 1.824093832948871
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017163958748254392,
        "excess_kurtosis": 3.1080532017551468,
        "return_acf_1": -0.1189005108220674,
        "abs_return_acf_1": 0.2576440113314104,
        "abs_return_acf_5": 0.27663983346305254,
        "abs_return_acf_20": 0.2524006033285068,
        "quantile_01": -0.057031162457742986,
        "quantile_99": 0.0445689765311256,
        "hill_tail_index": 4.278539100141585
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018849536695037788,
        "excess_kurtosis": 5.536258144630525,
        "return_acf_1": -0.20069976569311887,
        "abs_return_acf_1": 0.39546050409930733,
        "abs_return_acf_5": 0.3315316433309245,
        "abs_return_acf_20": 0.26558676020549754,
        "quantile_01": -0.06528878993429445,
        "quantile_99": 0.050886478235511935,
        "hill_tail_index": 3.0924666973670676
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019856379062511316,
        "excess_kurtosis": 4.279855934364695,
        "return_acf_1": -0.1325794782185848,
        "abs_return_acf_1": 0.23748175725824883,
        "abs_return_acf_5": 0.26470496832493734,
        "abs_return_acf_20": 0.27249046483315315,
        "quantile_01": -0.05985098238042464,
        "quantile_99": 0.05542687019452228,
        "hill_tail_index": 4.717672684703693
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021925522228896516,
        "excess_kurtosis": 11.90011549768931,
        "return_acf_1": -0.14719269295250448,
        "abs_return_acf_1": 0.28515160027721825,
        "abs_return_acf_5": 0.30359964585160437,
        "abs_return_acf_20": 0.34336356086075803,
        "quantile_01": -0.06752007362112623,
        "quantile_99": 0.0604153759900967,
        "hill_tail_index": 2.656105434184562
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018003948863481646,
        "excess_kurtosis": 3.730921000798194,
        "return_acf_1": -0.1322366598324703,
        "abs_return_acf_1": 0.2922261172871787,
        "abs_return_acf_5": 0.3099149158540204,
        "abs_return_acf_20": 0.313223644923318,
        "quantile_01": -0.05982770223172915,
        "quantile_99": 0.04732940122108466,
        "hill_tail_index": 3.769065659013008
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019317433924601134,
        "excess_kurtosis": 6.805923394954267,
        "return_acf_1": -0.08600409718717057,
        "abs_return_acf_1": 0.3240977232934684,
        "abs_return_acf_5": 0.3061383951031595,
        "abs_return_acf_20": 0.2595589517365175,
        "quantile_01": -0.07104925912947914,
        "quantile_99": 0.05203412908249777,
        "hill_tail_index": 3.493819097126326
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021533666737476944,
        "excess_kurtosis": 14.265938911467927,
        "return_acf_1": -0.21368581421975694,
        "abs_return_acf_1": 0.4133092033853691,
        "abs_return_acf_5": 0.43546984352236584,
        "abs_return_acf_20": 0.2841437621591932,
        "quantile_01": -0.05841646039984945,
        "quantile_99": 0.0543663570565957,
        "hill_tail_index": 2.134658784777274
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017150315190849943,
        "excess_kurtosis": 3.2318637767738503,
        "return_acf_1": -0.09948927906931873,
        "abs_return_acf_1": 0.2344923376351212,
        "abs_return_acf_5": 0.24287793973793875,
        "abs_return_acf_20": 0.19862456955489366,
        "quantile_01": -0.05139720644540193,
        "quantile_99": 0.04730578942332411,
        "hill_tail_index": 4.400373776860905
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01756605401086435,
        "excess_kurtosis": 3.034490573505379,
        "return_acf_1": -0.14227987034637116,
        "abs_return_acf_1": 0.19221941258834302,
        "abs_return_acf_5": 0.21022166568317405,
        "abs_return_acf_20": 0.22778884408324532,
        "quantile_01": -0.056284471106765974,
        "quantile_99": 0.044887410597143504,
        "hill_tail_index": 3.779092389355551
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02160787847677975,
        "excess_kurtosis": 12.213119717706237,
        "return_acf_1": -0.2476783481507129,
        "abs_return_acf_1": 0.42861266057806163,
        "abs_return_acf_5": 0.4131686521473215,
        "abs_return_acf_20": 0.28093491634705564,
        "quantile_01": -0.08439135329921252,
        "quantile_99": 0.05181301124241535,
        "hill_tail_index": 2.1614493051338006
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021547111843791003,
        "excess_kurtosis": 11.836294532522697,
        "return_acf_1": -0.16910111752728885,
        "abs_return_acf_1": 0.3533258692013981,
        "abs_return_acf_5": 0.397245928244987,
        "abs_return_acf_20": 0.3251916951997537,
        "quantile_01": -0.0652808358193855,
        "quantile_99": 0.06491422895011353,
        "hill_tail_index": 2.5595951978188465
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017942215859002145,
        "excess_kurtosis": 5.162679888895509,
        "return_acf_1": -0.23440572355600378,
        "abs_return_acf_1": 0.3328098619162562,
        "abs_return_acf_5": 0.31007401437363563,
        "abs_return_acf_20": 0.25756936613779324,
        "quantile_01": -0.058410530167796466,
        "quantile_99": 0.042713732285251806,
        "hill_tail_index": 3.193704743253244
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019223637237758884,
        "excess_kurtosis": 7.162014237043882,
        "return_acf_1": -0.10980125026283298,
        "abs_return_acf_1": 0.2915584987699408,
        "abs_return_acf_5": 0.2976847336597406,
        "abs_return_acf_20": 0.24362723712305168,
        "quantile_01": -0.06374152121718883,
        "quantile_99": 0.05232132406258208,
        "hill_tail_index": 3.3678985126668297
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
