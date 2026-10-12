# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27228
Run ID: `d2a06444907420cdf91adcd2909ad8d5247b058eb8405fb87c69d20df1b50756`
Result fingerprint: `a7c60d060224fa58176b9331c7c3f1b357acb2a1f0b41eede6f80395b8e5ea0f`

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
    "equal_weight_sd": -0.8246309523809493,
    "equal_weight_raw": -12.369464285714237,
    "fixed_start_cap_weight_sd": -0.8584850594360933,
    "fixed_start_cap_weight_raw": -12.877275891541405,
    "end_cap_weight_sd": -0.8507618824130613,
    "end_cap_weight_raw": -12.761428236195917
  },
  "full_period_change": {
    "equal_weight_sd": -1.2537380952380908,
    "equal_weight_raw": -18.80607142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1583356481481435,
    "inflation_mean_sd": 0.810496693121693
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1277500000000031,
    "equal_weight_raw": 1.9162500000000473,
    "fixed_start_cap_weight_sd": 0.09389589294485931,
    "fixed_start_cap_weight_raw": 1.4084383941728897,
    "end_cap_weight_sd": 0.10161906996789101,
    "end_cap_weight_raw": 1.5242860495183652
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8832142857142826,
      "change_raw": -13.248214285714239,
      "decay_adjusted_gain_sd": 0.06916666666666975
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8423809523809495,
      "change_raw": -12.635714285714242,
      "decay_adjusted_gain_sd": 0.11000000000000294
    },
    "small": {
      "count": 18,
      "change_sd": -0.8059920634920602,
      "change_raw": -12.089880952380904,
      "decay_adjusted_gain_sd": 0.14638888888889212
    },
    "large_minus_small_sd": -0.07722222222222241,
    "large_minus_small_raw": -1.1583333333333363
  },
  "inflation": {
    "initial_mean_sd": 0.25575000000000003,
    "final_mean_sd": 0.855,
    "mean_sd": 0.5732944768248682,
    "mean_absolute_raw_gap": 8.599417152373022,
    "final_absolute_raw_gap": 12.825,
    "mean_range_fraction": 0.08599417152373022
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.2,
    "initial_wealth_share": 0.2518737299155953,
    "final_wealth_share": 0.24833562798623218
  },
  "pricing_slope": {
    "mean": 0.0007652369721219525,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.09025196925259862,
    "real_improvement_cost": 0.06994603871195007,
    "washing_cost": 0.02030593054064856,
    "fine_transfer": 0.0033240322873245463,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.09357600153992317,
    "resource_cost_fraction_initial_cap": 0.0030083989750866206,
    "private_net_outflow_fraction_initial_cap": 0.0031192000513307725,
    "fine_transfer_fraction_initial_cap": 0.00011080107624415155,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007901186592873328,
    "unapplied_final_day_resource_cost": 0.0004848919215601101
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 42.46444738810776,
    "beneficial_raw_gain_per_resource_cost": 636.9667108216163,
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
    "accrued_cost": 3.010274702522311,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.03408422633183456,
    "accrued_cost_fraction_initial_cap": 0.10034249008407703,
    "mean_contract_rate": 0.04112916179647222,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "maximum_relative_cash_error": 9.871311498670506e-16,
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
      "minimum": -0.25534310391132026,
      "maximum": -0.09559162470108018,
      "mean": -0.17748425007671437,
      "median": -0.17215002433122695,
      "quantile_05": -0.2299660370268005,
      "quantile_95": -0.12122607876301818
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
      "minimum": 0.26618180832042887,
      "maximum": 0.8155960488599067,
      "mean": 0.5783564662372603,
      "median": 0.5806546461403839,
      "quantile_05": 0.31826714323879335,
      "quantile_95": 0.7852032334896933
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
        "daily_volatility": 0.020782176530715676,
        "excess_kurtosis": 6.108284158838574,
        "return_acf_1": -0.15234201589586385,
        "abs_return_acf_1": 0.35822967352924695,
        "abs_return_acf_5": 0.3385228114870122,
        "abs_return_acf_20": 0.24603613403520366,
        "quantile_01": -0.06258265596222884,
        "quantile_99": 0.055340713653613184,
        "hill_tail_index": 3.602448551020047
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021540225894796743,
        "excess_kurtosis": 6.47669844495735,
        "return_acf_1": -0.20087892578665073,
        "abs_return_acf_1": 0.42079531164015394,
        "abs_return_acf_5": 0.39362480135197814,
        "abs_return_acf_20": 0.2637756258535524,
        "quantile_01": -0.07302371911188955,
        "quantile_99": 0.06782003134720371,
        "hill_tail_index": 4.436823388413113
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021338241965251303,
        "excess_kurtosis": 8.900614681177494,
        "return_acf_1": -0.22177653315145116,
        "abs_return_acf_1": 0.4129886782877173,
        "abs_return_acf_5": 0.4480634998388746,
        "abs_return_acf_20": 0.35870106970412746,
        "quantile_01": -0.07346347439305069,
        "quantile_99": 0.05995331545429118,
        "hill_tail_index": 3.1533919333548615
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018631438428415508,
        "excess_kurtosis": 3.9600069620457274,
        "return_acf_1": -0.205450857506925,
        "abs_return_acf_1": 0.2729946102969183,
        "abs_return_acf_5": 0.19212153924182054,
        "abs_return_acf_20": 0.13993516101764364,
        "quantile_01": -0.05027642235391435,
        "quantile_99": 0.05313613959654752,
        "hill_tail_index": 4.4704750838833744
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020705862334956124,
        "excess_kurtosis": 7.091004544273927,
        "return_acf_1": -0.16309019368038788,
        "abs_return_acf_1": 0.42078250475996953,
        "abs_return_acf_5": 0.3763281499021767,
        "abs_return_acf_20": 0.3310998885460899,
        "quantile_01": -0.06816286545876148,
        "quantile_99": 0.056519759811966414,
        "hill_tail_index": 3.446110579813098
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019239432185723403,
        "excess_kurtosis": 5.784399772448467,
        "return_acf_1": -0.13344911752366528,
        "abs_return_acf_1": 0.319031855894263,
        "abs_return_acf_5": 0.3067076358268992,
        "abs_return_acf_20": 0.27075335481758406,
        "quantile_01": -0.05831559601723254,
        "quantile_99": 0.053940429737568456,
        "hill_tail_index": 3.813236527449787
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01888667946069891,
        "excess_kurtosis": 6.258287887292578,
        "return_acf_1": -0.17580523190121006,
        "abs_return_acf_1": 0.36391960486379527,
        "abs_return_acf_5": 0.36170895358501015,
        "abs_return_acf_20": 0.22821517756855314,
        "quantile_01": -0.06646222849049285,
        "quantile_99": 0.04921432578218083,
        "hill_tail_index": 2.8892463565791933
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01935478686456738,
        "excess_kurtosis": 2.9711298602132565,
        "return_acf_1": -0.1325633338541911,
        "abs_return_acf_1": 0.311941124677876,
        "abs_return_acf_5": 0.30532191158336974,
        "abs_return_acf_20": 0.2716258655436907,
        "quantile_01": -0.0561176104928046,
        "quantile_99": 0.055123732714701626,
        "hill_tail_index": 4.36443267316869
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01922711517010012,
        "excess_kurtosis": 8.214732830354919,
        "return_acf_1": -0.14977467568327943,
        "abs_return_acf_1": 0.33925414151555877,
        "abs_return_acf_5": 0.34673294410165373,
        "abs_return_acf_20": 0.281243658957068,
        "quantile_01": -0.06024093888505542,
        "quantile_99": 0.04904565756677752,
        "hill_tail_index": 3.7032356915329263
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02398059548592317,
        "excess_kurtosis": 9.733756578414479,
        "return_acf_1": -0.22017638459002611,
        "abs_return_acf_1": 0.4597107882739627,
        "abs_return_acf_5": 0.45212835864288364,
        "abs_return_acf_20": 0.3099354611199077,
        "quantile_01": -0.0837629734192044,
        "quantile_99": 0.07085549451852252,
        "hill_tail_index": 3.455395551048259
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02157757673122935,
        "excess_kurtosis": 9.473845188259975,
        "return_acf_1": -0.16208028673584213,
        "abs_return_acf_1": 0.41355643478514637,
        "abs_return_acf_5": 0.4614063908936199,
        "abs_return_acf_20": 0.32088770477021095,
        "quantile_01": -0.07382406642052017,
        "quantile_99": 0.06158206546998026,
        "hill_tail_index": 3.0195558507387683
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019543089458242808,
        "excess_kurtosis": 9.964478084151768,
        "return_acf_1": -0.1361146365275945,
        "abs_return_acf_1": 0.3311394589681702,
        "abs_return_acf_5": 0.3572205470740927,
        "abs_return_acf_20": 0.2630446191105268,
        "quantile_01": -0.057264263624155584,
        "quantile_99": 0.05440020436671328,
        "hill_tail_index": 3.152888940106245
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021525937962753455,
        "excess_kurtosis": 9.838750662879432,
        "return_acf_1": -0.21228260559734916,
        "abs_return_acf_1": 0.40635107455883096,
        "abs_return_acf_5": 0.48177158824787425,
        "abs_return_acf_20": 0.34446410805189853,
        "quantile_01": -0.08400315778332311,
        "quantile_99": 0.06075139280784021,
        "hill_tail_index": 3.5841928311992617
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01948271352263235,
        "excess_kurtosis": 8.448696994973375,
        "return_acf_1": -0.16651138576963245,
        "abs_return_acf_1": 0.36771244707114437,
        "abs_return_acf_5": 0.3587854719428034,
        "abs_return_acf_20": 0.28538680287692025,
        "quantile_01": -0.06228668008261119,
        "quantile_99": 0.05417902706748563,
        "hill_tail_index": 3.33086261486375
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020921083942757726,
        "excess_kurtosis": 5.836984797298895,
        "return_acf_1": -0.13916589100426216,
        "abs_return_acf_1": 0.3561755169178195,
        "abs_return_acf_5": 0.3663457153996655,
        "abs_return_acf_20": 0.2961219720570346,
        "quantile_01": -0.06482104337125764,
        "quantile_99": 0.06038846272571363,
        "hill_tail_index": 2.6076693310839794
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02138348488529197,
        "excess_kurtosis": 7.268942014035783,
        "return_acf_1": -0.19320827924269057,
        "abs_return_acf_1": 0.38013238868417265,
        "abs_return_acf_5": 0.41608073501323567,
        "abs_return_acf_20": 0.34472138926346657,
        "quantile_01": -0.07149073568939067,
        "quantile_99": 0.06291999452876085,
        "hill_tail_index": 3.668367463689734
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02087095516751046,
        "excess_kurtosis": 5.287647991750813,
        "return_acf_1": -0.14207368001229626,
        "abs_return_acf_1": 0.3895160742992099,
        "abs_return_acf_5": 0.40053227168920347,
        "abs_return_acf_20": 0.30304439409930767,
        "quantile_01": -0.06879799199775158,
        "quantile_99": 0.0541355883208641,
        "hill_tail_index": 3.7081623143753597
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019468742384632278,
        "excess_kurtosis": 7.5958448639630465,
        "return_acf_1": -0.21028264766645272,
        "abs_return_acf_1": 0.34664111076452175,
        "abs_return_acf_5": 0.34719630239406,
        "abs_return_acf_20": 0.2514726642201032,
        "quantile_01": -0.06996012917559156,
        "quantile_99": 0.05540275182397716,
        "hill_tail_index": 3.524582216932271
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022461872492132145,
        "excess_kurtosis": 7.4778464980213,
        "return_acf_1": -0.22832653987673096,
        "abs_return_acf_1": 0.4815875646561938,
        "abs_return_acf_5": 0.4772334293174198,
        "abs_return_acf_20": 0.3643756406161154,
        "quantile_01": -0.070528866986845,
        "quantile_99": 0.07005268631760318,
        "hill_tail_index": 3.6414018177750567
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02195739436581675,
        "excess_kurtosis": 9.049999689114651,
        "return_acf_1": -0.25534310391132026,
        "abs_return_acf_1": 0.40565313902658995,
        "abs_return_acf_5": 0.3795077337959856,
        "abs_return_acf_20": 0.2676787875655328,
        "quantile_01": -0.07779567933988629,
        "quantile_99": 0.060933272174906024,
        "hill_tail_index": 3.466484975627532
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02175672797036722,
        "excess_kurtosis": 7.12156179198338,
        "return_acf_1": -0.21650787969250626,
        "abs_return_acf_1": 0.4580574857494149,
        "abs_return_acf_5": 0.43321007521621313,
        "abs_return_acf_20": 0.34485778706092984,
        "quantile_01": -0.06750416898261957,
        "quantile_99": 0.06156657922618868,
        "hill_tail_index": 3.4200929496839407
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018726267840643202,
        "excess_kurtosis": 5.451228193681031,
        "return_acf_1": -0.23130744378594828,
        "abs_return_acf_1": 0.387628963332333,
        "abs_return_acf_5": 0.41306321784236283,
        "abs_return_acf_20": 0.283270680562947,
        "quantile_01": -0.061736296474655145,
        "quantile_99": 0.05294067150737943,
        "hill_tail_index": 3.7144457277491196
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01887532361205363,
        "excess_kurtosis": 6.444767514555325,
        "return_acf_1": -0.11195014277933113,
        "abs_return_acf_1": 0.3404204843585511,
        "abs_return_acf_5": 0.2517787665286939,
        "abs_return_acf_20": 0.269907369733445,
        "quantile_01": -0.05197580780252993,
        "quantile_99": 0.05447744410661506,
        "hill_tail_index": 3.2591912901358873
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020319094019845087,
        "excess_kurtosis": 6.4065153906562635,
        "return_acf_1": -0.21928076102857497,
        "abs_return_acf_1": 0.42734559392075516,
        "abs_return_acf_5": 0.40687568304162297,
        "abs_return_acf_20": 0.2737607153801013,
        "quantile_01": -0.0683952240583032,
        "quantile_99": 0.05349125394068262,
        "hill_tail_index": 3.1366245530392356
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02079009118040988,
        "excess_kurtosis": 6.277762258353469,
        "return_acf_1": -0.1390239911006141,
        "abs_return_acf_1": 0.40621967909909995,
        "abs_return_acf_5": 0.4052877293314031,
        "abs_return_acf_20": 0.284014784284832,
        "quantile_01": -0.06891725102815831,
        "quantile_99": 0.054302243248757175,
        "hill_tail_index": 4.152976361913684
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020548441784644673,
        "excess_kurtosis": 7.7293208979421255,
        "return_acf_1": -0.1695978132980611,
        "abs_return_acf_1": 0.38788005180052887,
        "abs_return_acf_5": 0.45889323830389034,
        "abs_return_acf_20": 0.38454911776129536,
        "quantile_01": -0.06412600461661816,
        "quantile_99": 0.05780359813046149,
        "hill_tail_index": 2.89967884451033
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02085159008762652,
        "excess_kurtosis": 7.5872307212633014,
        "return_acf_1": -0.19627147133503958,
        "abs_return_acf_1": 0.40895430212639683,
        "abs_return_acf_5": 0.41378557538814414,
        "abs_return_acf_20": 0.2766838865425248,
        "quantile_01": -0.07537174657860381,
        "quantile_99": 0.06769506702507785,
        "hill_tail_index": 4.20182913611566
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020290961239278944,
        "excess_kurtosis": 9.100702994421281,
        "return_acf_1": -0.17106484661068294,
        "abs_return_acf_1": 0.391300993350482,
        "abs_return_acf_5": 0.422106682790697,
        "abs_return_acf_20": 0.33631060139780883,
        "quantile_01": -0.0717577948658557,
        "quantile_99": 0.05424989077580267,
        "hill_tail_index": 3.019161090416405
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023126163024430883,
        "excess_kurtosis": 8.655439742967959,
        "return_acf_1": -0.17323520205177095,
        "abs_return_acf_1": 0.4432140436453881,
        "abs_return_acf_5": 0.47285070171813565,
        "abs_return_acf_20": 0.31917165472832254,
        "quantile_01": -0.07928163033501853,
        "quantile_99": 0.07487711362453937,
        "hill_tail_index": 3.1322922788101755
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018859010606246483,
        "excess_kurtosis": 19.848078767342955,
        "return_acf_1": -0.09559162470108018,
        "abs_return_acf_1": 0.278548142630075,
        "abs_return_acf_5": 0.38937244034118706,
        "abs_return_acf_20": 0.18464903408762842,
        "quantile_01": -0.050389764350159204,
        "quantile_99": 0.049087758231274294,
        "hill_tail_index": 2.731532147650967
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
