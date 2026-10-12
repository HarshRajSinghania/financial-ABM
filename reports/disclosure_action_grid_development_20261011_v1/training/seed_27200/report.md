# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27200
Run ID: `327c21cf193a129921a4eeeb17b1edc333858bcbdf850fbe0b3b6a6fb14827ae`
Result fingerprint: `9427545fe4280276bd9ccf735abea8b1a0a0022df380e6111031a6406fce0ed8`

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
    "equal_weight_sd": -0.8006309523809491,
    "equal_weight_raw": -12.009464285714236,
    "fixed_start_cap_weight_sd": -0.7507879276930737,
    "fixed_start_cap_weight_raw": -11.261818915396105,
    "end_cap_weight_sd": -0.7457631830191022,
    "end_cap_weight_raw": -11.186447745286529
  },
  "full_period_change": {
    "equal_weight_sd": -1.2362380952380905,
    "equal_weight_raw": -18.543571428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1605383597883552,
    "inflation_mean_sd": 0.5426924603174604
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.15175000000000322,
    "equal_weight_raw": 2.276250000000047,
    "fixed_start_cap_weight_sd": 0.2015930246878788,
    "fixed_start_cap_weight_raw": 3.0238953703181815,
    "end_cap_weight_sd": 0.20661776936185025,
    "end_cap_weight_raw": 3.0992665404277537
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6157142857142822,
      "change_raw": -9.235714285714232,
      "decay_adjusted_gain_sd": 0.33666666666667
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8307142857142824,
      "change_raw": -12.460714285714236,
      "decay_adjusted_gain_sd": 0.12166666666666985
    },
    "small": {
      "count": 18,
      "change_sd": -0.816408730158727,
      "change_raw": -12.246130952380904,
      "decay_adjusted_gain_sd": 0.1359722222222254
    },
    "large_minus_small_sd": 0.20069444444444473,
    "large_minus_small_raw": 3.010416666666671
  },
  "inflation": {
    "initial_mean_sd": 0.2950833333333333,
    "final_mean_sd": 0.5430833333333334,
    "mean_sd": 0.4346833888426312,
    "mean_absolute_raw_gap": 6.5202508326394675,
    "final_absolute_raw_gap": 8.14625,
    "mean_range_fraction": 0.06520250832639468
  },
  "impact": {
    "initial_share": 0.21333333333333335,
    "final_share": 0.3,
    "initial_wealth_share": 0.19339002839268152,
    "final_wealth_share": 0.26032216940144315
  },
  "pricing_slope": {
    "mean": -0.001215449584011899,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.016807086662349452,
    "real_improvement_cost": 0.009562705614847492,
    "washing_cost": 0.007244381047501959,
    "fine_transfer": 0.007452749363876595,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.02425983602622605,
    "resource_cost_fraction_initial_cap": 0.000560236222078315,
    "private_net_outflow_fraction_initial_cap": 0.0008086612008742015,
    "fine_transfer_fraction_initial_cap": 0.0002484249787958865,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.009291989433335477,
    "unapplied_final_day_resource_cost": 0.00026750903356823806
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 270.8678839741108,
    "beneficial_raw_gain_per_resource_cost": 4063.018259611662,
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
    "fixed_exposure": 15.000000000000002,
    "accrued_cost": 2.86427157670953,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.11191889948094676,
    "accrued_cost_fraction_initial_cap": 0.09547571922365099,
    "mean_contract_rate": 0.039851726081870965,
    "maximum_ledger_error": 1.198551620364835e-19
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
    "maximum_relative_cash_error": 1.7060469575598364e-15,
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
      "minimum": -0.24806511467522907,
      "maximum": -0.05191216053202869,
      "mean": -0.13407002443974417,
      "median": -0.11801448596609053,
      "quantile_05": -0.23773050172650165,
      "quantile_95": -0.07534721944434365
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
      "minimum": 0.21319802474324312,
      "maximum": 0.7773543159430621,
      "mean": 0.4414412461050546,
      "median": 0.4060584405200268,
      "quantile_05": 0.25877550176368935,
      "quantile_95": 0.7142050807705321
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
        "daily_volatility": 0.019549189145922023,
        "excess_kurtosis": 7.735405259369488,
        "return_acf_1": -0.08252679821030232,
        "abs_return_acf_1": 0.3590183542066814,
        "abs_return_acf_5": 0.2914671036649238,
        "abs_return_acf_20": 0.26288814143300504,
        "quantile_01": -0.05563680360304928,
        "quantile_99": 0.05060824114432105,
        "hill_tail_index": 2.6778942058946233
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021180787771257238,
        "excess_kurtosis": 8.178465944261218,
        "return_acf_1": -0.1175730254882113,
        "abs_return_acf_1": 0.4368697978351641,
        "abs_return_acf_5": 0.42058755559218225,
        "abs_return_acf_20": 0.3811696484631021,
        "quantile_01": -0.06756325276476614,
        "quantile_99": 0.06719831036255391,
        "hill_tail_index": 3.107669952550793
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017619857369050092,
        "excess_kurtosis": 15.072728869465085,
        "return_acf_1": -0.09970544164728377,
        "abs_return_acf_1": 0.3617240707411682,
        "abs_return_acf_5": 0.34240609467189864,
        "abs_return_acf_20": 0.2800188860810946,
        "quantile_01": -0.049877926940282924,
        "quantile_99": 0.04128369796934778,
        "hill_tail_index": 2.2574386383967195
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017343189293579937,
        "excess_kurtosis": 13.182777615004,
        "return_acf_1": -0.10448918157944502,
        "abs_return_acf_1": 0.32362937646805257,
        "abs_return_acf_5": 0.33762339102094047,
        "abs_return_acf_20": 0.2709514531958554,
        "quantile_01": -0.05274538864518584,
        "quantile_99": 0.03876756008418575,
        "hill_tail_index": 1.9507052699543959
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01906564231824737,
        "excess_kurtosis": 7.885375917781264,
        "return_acf_1": -0.07992072867070908,
        "abs_return_acf_1": 0.41721296713217876,
        "abs_return_acf_5": 0.4302952420236276,
        "abs_return_acf_20": 0.43642422262353414,
        "quantile_01": -0.06956817585029071,
        "quantile_99": 0.05797735324018031,
        "hill_tail_index": 3.5661748457083355
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021791462130266455,
        "excess_kurtosis": 8.087879920380916,
        "return_acf_1": -0.2330913807893248,
        "abs_return_acf_1": 0.43154891621948716,
        "abs_return_acf_5": 0.40012904708335534,
        "abs_return_acf_20": 0.24866648488423,
        "quantile_01": -0.07108472373661615,
        "quantile_99": 0.06953375648392987,
        "hill_tail_index": 2.6726349347382006
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019395936022353986,
        "excess_kurtosis": 4.871384682368049,
        "return_acf_1": -0.10398418655842713,
        "abs_return_acf_1": 0.3195122401749847,
        "abs_return_acf_5": 0.3232757321312015,
        "abs_return_acf_20": 0.3120864532224469,
        "quantile_01": -0.05951096091147778,
        "quantile_99": 0.054406900100459996,
        "hill_tail_index": 4.231767595063172
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019807306147008007,
        "excess_kurtosis": 4.64897379056859,
        "return_acf_1": -0.13330306069170675,
        "abs_return_acf_1": 0.36531258425188606,
        "abs_return_acf_5": 0.3029158115889332,
        "abs_return_acf_20": 0.2702117700315211,
        "quantile_01": -0.05789302610580444,
        "quantile_99": 0.05692170408632466,
        "hill_tail_index": 4.609685832213094
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01869959075662248,
        "excess_kurtosis": 10.88512645570779,
        "return_acf_1": -0.14194691530724954,
        "abs_return_acf_1": 0.4241985889774491,
        "abs_return_acf_5": 0.4129968019554995,
        "abs_return_acf_20": 0.38370825506178036,
        "quantile_01": -0.06148649609220601,
        "quantile_99": 0.05530557166539305,
        "hill_tail_index": 2.600102832511125
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018032519820409744,
        "excess_kurtosis": 3.5148589059460456,
        "return_acf_1": -0.1525432489251352,
        "abs_return_acf_1": 0.28931313203689274,
        "abs_return_acf_5": 0.2801225619777389,
        "abs_return_acf_20": 0.2150634783611609,
        "quantile_01": -0.051884796561764014,
        "quantile_99": 0.049680222647707786,
        "hill_tail_index": 4.658918916648519
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020077698774622198,
        "excess_kurtosis": 11.855419821518945,
        "return_acf_1": -0.14847070469911663,
        "abs_return_acf_1": 0.44470162154966475,
        "abs_return_acf_5": 0.46313006014504254,
        "abs_return_acf_20": 0.39103973022867355,
        "quantile_01": -0.07873290519416459,
        "quantile_99": 0.059912906147082584,
        "hill_tail_index": 2.7353251774968625
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01961726318853698,
        "excess_kurtosis": 5.157579598756769,
        "return_acf_1": -0.1667992415927904,
        "abs_return_acf_1": 0.3672710780735387,
        "abs_return_acf_5": 0.3899291293506437,
        "abs_return_acf_20": 0.2545357964263484,
        "quantile_01": -0.061891732433177055,
        "quantile_99": 0.05734359294651093,
        "hill_tail_index": 3.1720298148939414
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017968323693389205,
        "excess_kurtosis": 3.4312099485775995,
        "return_acf_1": -0.1080853634998894,
        "abs_return_acf_1": 0.35639063357420475,
        "abs_return_acf_5": 0.29919676449031885,
        "abs_return_acf_20": 0.2601113678569967,
        "quantile_01": -0.05276323010166817,
        "quantile_99": 0.05089016431009238,
        "hill_tail_index": 4.719171729664896
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019961591622597526,
        "excess_kurtosis": 7.473819892952633,
        "return_acf_1": -0.15030727405656977,
        "abs_return_acf_1": 0.3837831053578073,
        "abs_return_acf_5": 0.3186548703589069,
        "abs_return_acf_20": 0.24056081325123674,
        "quantile_01": -0.06910331511185556,
        "quantile_99": 0.05300795769041229,
        "hill_tail_index": 3.4037518533342705
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019515182440281952,
        "excess_kurtosis": 12.881597841132326,
        "return_acf_1": -0.08532985390842532,
        "abs_return_acf_1": 0.4304786830265554,
        "abs_return_acf_5": 0.41885673145942076,
        "abs_return_acf_20": 0.39543454800187017,
        "quantile_01": -0.06959697063209991,
        "quantile_99": 0.05118002546767765,
        "hill_tail_index": 2.3630599031526636
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02031200937627667,
        "excess_kurtosis": 17.26453166779016,
        "return_acf_1": -0.14307924754403298,
        "abs_return_acf_1": 0.3465283023756655,
        "abs_return_acf_5": 0.391602694149866,
        "abs_return_acf_20": 0.33763753240938366,
        "quantile_01": -0.07594820021243814,
        "quantile_99": 0.04714001511148368,
        "hill_tail_index": 1.9522424424887848
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020477055984365375,
        "excess_kurtosis": 13.364225412228556,
        "return_acf_1": -0.1710962973163232,
        "abs_return_acf_1": 0.443309987986392,
        "abs_return_acf_5": 0.38884036570107633,
        "abs_return_acf_20": 0.42558871237485174,
        "quantile_01": -0.07130191309029761,
        "quantile_99": 0.060392282292380216,
        "hill_tail_index": 2.8419441813797213
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.0182040055977641,
        "excess_kurtosis": 4.48036892309951,
        "return_acf_1": -0.10003214109297778,
        "abs_return_acf_1": 0.40000934961347967,
        "abs_return_acf_5": 0.3442105402015203,
        "abs_return_acf_20": 0.24929410580117298,
        "quantile_01": -0.054704319947640384,
        "quantile_99": 0.05409648781512476,
        "hill_tail_index": 3.8057195134969404
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02082094202211813,
        "excess_kurtosis": 16.01746113602946,
        "return_acf_1": -0.21451341497114787,
        "abs_return_acf_1": 0.48238430801573395,
        "abs_return_acf_5": 0.3812897151732079,
        "abs_return_acf_20": 0.23739496106112304,
        "quantile_01": -0.061531020143813876,
        "quantile_99": 0.053281523542408935,
        "hill_tail_index": 2.5411084979184215
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01737549878486708,
        "excess_kurtosis": 12.38661248848498,
        "return_acf_1": -0.09100678911373361,
        "abs_return_acf_1": 0.34577698939870055,
        "abs_return_acf_5": 0.3270709210339725,
        "abs_return_acf_20": 0.2807937511441504,
        "quantile_01": -0.060064316951641133,
        "quantile_99": 0.04648673511568297,
        "hill_tail_index": 2.639722171595935
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01973033349446065,
        "excess_kurtosis": 13.616128541933595,
        "return_acf_1": -0.11337890357221261,
        "abs_return_acf_1": 0.4058642184045417,
        "abs_return_acf_5": 0.39071706340823753,
        "abs_return_acf_20": 0.42141479512902114,
        "quantile_01": -0.07106109450795617,
        "quantile_99": 0.05458611020781634,
        "hill_tail_index": 2.504710849149058
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01955123256165486,
        "excess_kurtosis": 7.672140978590676,
        "return_acf_1": -0.21095719689442052,
        "abs_return_acf_1": 0.4593707105181529,
        "abs_return_acf_5": 0.38384936554260213,
        "abs_return_acf_20": 0.25764766136317835,
        "quantile_01": -0.06521246558632239,
        "quantile_99": 0.06039679248131542,
        "hill_tail_index": 3.322146258509939
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.0161576155250796,
        "excess_kurtosis": 5.409664296118613,
        "return_acf_1": -0.11845594644396976,
        "abs_return_acf_1": 0.21288721557913678,
        "abs_return_acf_5": 0.2976587685601729,
        "abs_return_acf_20": 0.243207042549176,
        "quantile_01": -0.04977973376186779,
        "quantile_99": 0.04055869702739453,
        "hill_tail_index": 3.341124274371162
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019187924499723053,
        "excess_kurtosis": 13.410652780612192,
        "return_acf_1": -0.08605198429750624,
        "abs_return_acf_1": 0.352819683792589,
        "abs_return_acf_5": 0.3870488487952305,
        "abs_return_acf_20": 0.3040145021837117,
        "quantile_01": -0.06782979405277854,
        "quantile_99": 0.0537771597479607,
        "hill_tail_index": 2.5613491760961895
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018539240343709865,
        "excess_kurtosis": 7.3456266119730635,
        "return_acf_1": -0.11682650449759323,
        "abs_return_acf_1": 0.4250197344197122,
        "abs_return_acf_5": 0.2803825981193605,
        "abs_return_acf_20": 0.25925809722110404,
        "quantile_01": -0.055949120108026676,
        "quantile_99": 0.0515669977262585,
        "hill_tail_index": 3.2912104400403757
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017742471835841357,
        "excess_kurtosis": 11.595668608558453,
        "return_acf_1": -0.13551722313687228,
        "abs_return_acf_1": 0.29679117511415704,
        "abs_return_acf_5": 0.3010466789448608,
        "abs_return_acf_20": 0.2579307175053584,
        "quantile_01": -0.06400386110269414,
        "quantile_99": 0.04198272376630998,
        "hill_tail_index": 1.8486839608151417
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01878869777663483,
        "excess_kurtosis": 6.351630603760967,
        "return_acf_1": -0.05191216053202869,
        "abs_return_acf_1": 0.3982038959687561,
        "abs_return_acf_5": 0.3186752558212756,
        "abs_return_acf_20": 0.3205203845316105,
        "quantile_01": -0.06578350482935644,
        "quantile_99": 0.05657504923103476,
        "hill_tail_index": 4.180440124829383
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02061882466695446,
        "excess_kurtosis": 9.069543276522783,
        "return_acf_1": -0.07160525735004461,
        "abs_return_acf_1": 0.43773050993760554,
        "abs_return_acf_5": 0.4044211900393362,
        "abs_return_acf_20": 0.2572174352895582,
        "quantile_01": -0.06954996330463992,
        "quantile_99": 0.05466170515433284,
        "hill_tail_index": 2.786014201259392
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021261518307271902,
        "excess_kurtosis": 8.590001856705534,
        "return_acf_1": -0.24806511467522907,
        "abs_return_acf_1": 0.49042627098074976,
        "abs_return_acf_5": 0.42972164357890263,
        "abs_return_acf_20": 0.3065228621397079,
        "quantile_01": -0.07646375847185495,
        "quantile_99": 0.0616765974097771,
        "hill_tail_index": 3.6026695855085626
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022494586961534453,
        "excess_kurtosis": 10.773654956299579,
        "return_acf_1": -0.24152614612964635,
        "abs_return_acf_1": 0.4574009098915825,
        "abs_return_acf_5": 0.47326246948979406,
        "abs_return_acf_20": 0.2568309833678027,
        "quantile_01": -0.0808934646372146,
        "quantile_99": 0.06513656203514043,
        "hill_tail_index": 2.912686914750036
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
