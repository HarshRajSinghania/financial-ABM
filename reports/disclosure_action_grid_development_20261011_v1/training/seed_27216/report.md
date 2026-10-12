# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27216
Run ID: `5e26d8a1019146d7405d375c7178b4b71afbb965cf8642a126b236fbf6dd2554`
Result fingerprint: `31e26c01a212c746fdc094bd81ea8484ec947e021138cb31282dc22c0aab932f`

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
    "equal_weight_sd": -0.7171309523809491,
    "equal_weight_raw": -10.756964285714238,
    "fixed_start_cap_weight_sd": -0.6363602648463975,
    "fixed_start_cap_weight_raw": -9.545403972695961,
    "end_cap_weight_sd": -0.6170478892538129,
    "end_cap_weight_raw": -9.255718338807194
  },
  "full_period_change": {
    "equal_weight_sd": -1.1367380952380903,
    "equal_weight_raw": -17.051071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0468065476190431,
    "inflation_mean_sd": 0.5456226851851852
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.23287404536803016,
    "equal_weight_raw": 3.4931106805204526,
    "fixed_start_cap_weight_sd": 0.31215998126489336,
    "fixed_start_cap_weight_raw": 4.6823997189734,
    "end_cap_weight_sd": 0.3321574579599998,
    "end_cap_weight_raw": 4.982361869399995
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.3082142857142826,
      "change_raw": -4.623214285714239,
      "decay_adjusted_gain_sd": 0.6441666666666697
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7471031746031714,
      "change_raw": -11.206547619047571,
      "decay_adjusted_gain_sd": 0.19735792900453764
    },
    "small": {
      "count": 18,
      "change_sd": -0.7702976190476157,
      "change_raw": -11.554464285714236,
      "decay_adjusted_gain_sd": 0.18208333333333654
    },
    "large_minus_small_sd": 0.4620833333333331,
    "large_minus_small_raw": 6.931249999999997
  },
  "inflation": {
    "initial_mean_sd": 0.2760833333333333,
    "final_mean_sd": 0.5688333333333334,
    "mean_sd": 0.40880974188176517,
    "mean_absolute_raw_gap": 6.132146128226477,
    "final_absolute_raw_gap": 8.532499999999997,
    "mean_range_fraction": 0.06132146128226477
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.272633100745406,
    "final_wealth_share": 0.3068450779025618
  },
  "pricing_slope": {
    "mean": 0.0006112573253585922,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.07478249860958751,
    "real_improvement_cost": 0.06364595990076224,
    "washing_cost": 0.011136538708825267,
    "fine_transfer": 0.007249377564075697,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0820318761736632,
    "resource_cost_fraction_initial_cap": 0.002492749953652917,
    "private_net_outflow_fraction_initial_cap": 0.00273439587245544,
    "fine_transfer_fraction_initial_cap": 0.00024164591880252324,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002361652755979418,
    "unapplied_final_day_resource_cost": 0.00013952814016457242
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 93.42053944350604,
    "beneficial_raw_gain_per_resource_cost": 1401.3080916525905,
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
    "accrued_cost": 3.1770497692316253,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.20085929304114897,
    "accrued_cost_fraction_initial_cap": 0.10590165897438751,
    "mean_contract_rate": 0.04356929923266932,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 1.6912791457799987e-15,
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
      "minimum": -0.15779165196362957,
      "maximum": 0.02925505282332515,
      "mean": -0.10236702407957352,
      "median": -0.1044695946723305,
      "quantile_05": -0.15286434535149282,
      "quantile_95": -0.048998711251086485
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
      "minimum": 0.243143018059667,
      "maximum": 0.7908416189436608,
      "mean": 0.46698989506645705,
      "median": 0.4210798933291696,
      "quantile_05": 0.28279247992165646,
      "quantile_95": 0.7155669226159226
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
        "daily_volatility": 0.02076606192140456,
        "excess_kurtosis": 8.686408590431915,
        "return_acf_1": -0.1413578416171662,
        "abs_return_acf_1": 0.3707536855530295,
        "abs_return_acf_5": 0.4028183983504529,
        "abs_return_acf_20": 0.26784320734382766,
        "quantile_01": -0.07162440150144028,
        "quantile_99": 0.06259593216786422,
        "hill_tail_index": 3.7779165963712886
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019265096315050426,
        "excess_kurtosis": 3.3036185401029456,
        "return_acf_1": -0.11823852397884736,
        "abs_return_acf_1": 0.3516137035581044,
        "abs_return_acf_5": 0.23649108472366362,
        "abs_return_acf_20": 0.25645218053183094,
        "quantile_01": -0.05843323691276681,
        "quantile_99": 0.05241525017509995,
        "hill_tail_index": 4.3818053361717215
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01868139491977705,
        "excess_kurtosis": 8.87833636452014,
        "return_acf_1": -0.149256570590236,
        "abs_return_acf_1": 0.39389579625673127,
        "abs_return_acf_5": 0.3834779873597138,
        "abs_return_acf_20": 0.3109067210627357,
        "quantile_01": -0.0550272984239476,
        "quantile_99": 0.04181760280891877,
        "hill_tail_index": 2.2035167394361794
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022075932678958562,
        "excess_kurtosis": 16.648669612691208,
        "return_acf_1": -0.07202919130029305,
        "abs_return_acf_1": 0.4365234925097415,
        "abs_return_acf_5": 0.37989526259606027,
        "abs_return_acf_20": 0.3983523864575701,
        "quantile_01": -0.07546172371019956,
        "quantile_99": 0.06139184586587017,
        "hill_tail_index": 2.7085120745601086
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.0182552237678612,
        "excess_kurtosis": 5.710221838346275,
        "return_acf_1": -0.10361912784791281,
        "abs_return_acf_1": 0.39593844929506616,
        "abs_return_acf_5": 0.3492191668553498,
        "abs_return_acf_20": 0.3631228041249668,
        "quantile_01": -0.05581093502160422,
        "quantile_99": 0.05319624763324495,
        "hill_tail_index": 3.521836693359439
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0186756183091524,
        "excess_kurtosis": 4.0644013036738125,
        "return_acf_1": -0.0801689419229693,
        "abs_return_acf_1": 0.2627697765421666,
        "abs_return_acf_5": 0.24075787974901464,
        "abs_return_acf_20": 0.2214149046403778,
        "quantile_01": -0.05123247583411097,
        "quantile_99": 0.05571917046763929,
        "hill_tail_index": 4.030514129289862
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018214584771929873,
        "excess_kurtosis": 9.679294337704938,
        "return_acf_1": -0.15241699936669822,
        "abs_return_acf_1": 0.396007975803934,
        "abs_return_acf_5": 0.41249302406011606,
        "abs_return_acf_20": 0.281305548631605,
        "quantile_01": -0.05482231802054018,
        "quantile_99": 0.051221288790761925,
        "hill_tail_index": 3.0593043256100736
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02477403169448922,
        "excess_kurtosis": 10.333966214503938,
        "return_acf_1": -0.09167847707992856,
        "abs_return_acf_1": 0.41943459441288355,
        "abs_return_acf_5": 0.44807496212855974,
        "abs_return_acf_20": 0.3627502753338625,
        "quantile_01": -0.09357481552828047,
        "quantile_99": 0.0803833189706363,
        "hill_tail_index": 3.2210193364930526
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02321657671815485,
        "excess_kurtosis": 9.075883108517148,
        "return_acf_1": -0.1429271283387605,
        "abs_return_acf_1": 0.39532892579456685,
        "abs_return_acf_5": 0.33182543402858894,
        "abs_return_acf_20": 0.34289102991329407,
        "quantile_01": -0.07926098345465542,
        "quantile_99": 0.05963500269617015,
        "hill_tail_index": 3.0176237666385375
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01905487384627993,
        "excess_kurtosis": 5.618731078581572,
        "return_acf_1": -0.07821221669575526,
        "abs_return_acf_1": 0.37758509841988575,
        "abs_return_acf_5": 0.3427161798580259,
        "abs_return_acf_20": 0.2980035172376965,
        "quantile_01": -0.060881906328035376,
        "quantile_99": 0.05359915859981039,
        "hill_tail_index": 3.334974382210345
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02037063936017879,
        "excess_kurtosis": 9.711218558416377,
        "return_acf_1": -0.09349782807655438,
        "abs_return_acf_1": 0.40382216379428726,
        "abs_return_acf_5": 0.3707078539296288,
        "abs_return_acf_20": 0.2642989464277493,
        "quantile_01": -0.06456999006806974,
        "quantile_99": 0.0577078462852081,
        "hill_tail_index": 3.089282267234245
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01945016942878947,
        "excess_kurtosis": 19.21333224757648,
        "return_acf_1": -0.11317797542436646,
        "abs_return_acf_1": 0.43863301296041546,
        "abs_return_acf_5": 0.37959092769983377,
        "abs_return_acf_20": 0.30253113324161807,
        "quantile_01": -0.057305258795348604,
        "quantile_99": 0.05114054476620246,
        "hill_tail_index": 2.3291277607464096
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018877147114472786,
        "excess_kurtosis": 5.849573335097004,
        "return_acf_1": -0.09866947905371413,
        "abs_return_acf_1": 0.2478038872702025,
        "abs_return_acf_5": 0.26343272970984494,
        "abs_return_acf_20": 0.2775947083488786,
        "quantile_01": -0.06059288220319433,
        "quantile_99": 0.04420070505846878,
        "hill_tail_index": 2.895238622146587
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019039235910074826,
        "excess_kurtosis": 6.477412382022516,
        "return_acf_1": -0.06572753514068601,
        "abs_return_acf_1": 0.3866673091401608,
        "abs_return_acf_5": 0.26523930166472914,
        "abs_return_acf_20": 0.29269088208481014,
        "quantile_01": -0.05928808417716089,
        "quantile_99": 0.05047907353690157,
        "hill_tail_index": 3.2071700725002525
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02253575544229006,
        "excess_kurtosis": 16.194549755558818,
        "return_acf_1": 0.02925505282332515,
        "abs_return_acf_1": 0.35994339442661727,
        "abs_return_acf_5": 0.35078301645117654,
        "abs_return_acf_20": 0.3556319252264458,
        "quantile_01": -0.07957643566942603,
        "quantile_99": 0.06189901164292857,
        "hill_tail_index": 3.3222879426146767
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018511482131970434,
        "excess_kurtosis": 5.710861107710324,
        "return_acf_1": -0.15779165196362957,
        "abs_return_acf_1": 0.3230925256599563,
        "abs_return_acf_5": 0.2672259248553006,
        "abs_return_acf_20": 0.32551092150063676,
        "quantile_01": -0.05708086062439011,
        "quantile_99": 0.05208973521229422,
        "hill_tail_index": 3.1949185673024716
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020557093960519,
        "excess_kurtosis": 15.169874793957753,
        "return_acf_1": -0.12403738452921852,
        "abs_return_acf_1": 0.3106215156479726,
        "abs_return_acf_5": 0.44963631708343704,
        "abs_return_acf_20": 0.28075041511926896,
        "quantile_01": -0.059307949669912444,
        "quantile_99": 0.05404434190386546,
        "hill_tail_index": 2.156688288712026
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02484860343882581,
        "excess_kurtosis": 15.467354456726927,
        "return_acf_1": -0.055823535875585875,
        "abs_return_acf_1": 0.4126309058674572,
        "abs_return_acf_5": 0.47052542810892317,
        "abs_return_acf_20": 0.3686511579607568,
        "quantile_01": -0.08554255065126963,
        "quantile_99": 0.0631989334558698,
        "hill_tail_index": 2.4761175743971604
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019920942655189504,
        "excess_kurtosis": 4.398807396984432,
        "return_acf_1": -0.12355083261019774,
        "abs_return_acf_1": 0.35416184892058505,
        "abs_return_acf_5": 0.3204128088886434,
        "abs_return_acf_20": 0.27555066961138136,
        "quantile_01": -0.06150143871071693,
        "quantile_99": 0.05900456011026754,
        "hill_tail_index": 3.4583345897717654
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02022891420628968,
        "excess_kurtosis": 5.438454658410128,
        "return_acf_1": -0.07788188896788918,
        "abs_return_acf_1": 0.32353005579718963,
        "abs_return_acf_5": 0.3350571189539637,
        "abs_return_acf_20": 0.339076471127949,
        "quantile_01": -0.06678690233662901,
        "quantile_99": 0.05402841731646894,
        "hill_tail_index": 4.102948506723701
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020655620098458484,
        "excess_kurtosis": 13.297244057345626,
        "return_acf_1": -0.10532006149674819,
        "abs_return_acf_1": 0.3989819794325924,
        "abs_return_acf_5": 0.39704351621123724,
        "abs_return_acf_20": 0.32862034778185534,
        "quantile_01": -0.07601020468155874,
        "quantile_99": 0.059647739202043124,
        "hill_tail_index": 2.883576924988041
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02124259696392656,
        "excess_kurtosis": 9.59126402211326,
        "return_acf_1": -0.04341476383104147,
        "abs_return_acf_1": 0.35253235272804756,
        "abs_return_acf_5": 0.4226032431105364,
        "abs_return_acf_20": 0.3568358307322651,
        "quantile_01": -0.06431666382828091,
        "quantile_99": 0.05796785277672608,
        "hill_tail_index": 2.5796793846698294
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021241850201421213,
        "excess_kurtosis": 7.691597734549676,
        "return_acf_1": -0.15323035570268842,
        "abs_return_acf_1": 0.37477435095443795,
        "abs_return_acf_5": 0.33796827572720417,
        "abs_return_acf_20": 0.3144418238344662,
        "quantile_01": -0.0696633315852219,
        "quantile_99": 0.06018972138348978,
        "hill_tail_index": 3.4373044018444228
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023294836939635234,
        "excess_kurtosis": 10.65834323616497,
        "return_acf_1": -0.11970512645855486,
        "abs_return_acf_1": 0.4340656445890465,
        "abs_return_acf_5": 0.4427275481321124,
        "abs_return_acf_20": 0.33916397110252494,
        "quantile_01": -0.07760631696748836,
        "quantile_99": 0.06562423768644238,
        "hill_tail_index": 3.1895389266997696
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02081453199760159,
        "excess_kurtosis": 11.351092726433544,
        "return_acf_1": -0.1449724742441331,
        "abs_return_acf_1": 0.25371935088694353,
        "abs_return_acf_5": 0.34126812699843023,
        "abs_return_acf_20": 0.2907874356746951,
        "quantile_01": -0.057597506395228704,
        "quantile_99": 0.055437012375011974,
        "hill_tail_index": 3.278887525895684
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017457007963944508,
        "excess_kurtosis": 4.982255676595714,
        "return_acf_1": -0.09895430179696503,
        "abs_return_acf_1": 0.28247802651145726,
        "abs_return_acf_5": 0.2862182024347477,
        "abs_return_acf_20": 0.25905504509295635,
        "quantile_01": -0.05613749043475718,
        "quantile_99": 0.04504230099850952,
        "hill_tail_index": 3.579630473568132
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022263096654497355,
        "excess_kurtosis": 10.303280989702586,
        "return_acf_1": -0.06399776952883546,
        "abs_return_acf_1": 0.41985843472268736,
        "abs_return_acf_5": 0.43713754245343633,
        "abs_return_acf_20": 0.3704746255481009,
        "quantile_01": -0.08113892610314695,
        "quantile_99": 0.0660307461623363,
        "hill_tail_index": 3.257360984138535
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02134970799853903,
        "excess_kurtosis": 11.05912642126407,
        "return_acf_1": -0.12113866295125121,
        "abs_return_acf_1": 0.35228469054139794,
        "abs_return_acf_5": 0.36741059559954653,
        "abs_return_acf_20": 0.4038775571592606,
        "quantile_01": -0.06480241313429891,
        "quantile_99": 0.0516450774299807,
        "hill_tail_index": 3.0100842302537356
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017618619632613613,
        "excess_kurtosis": 7.312715513009245,
        "return_acf_1": -0.10274098909944235,
        "abs_return_acf_1": 0.40205228384470026,
        "abs_return_acf_5": 0.41679947944565304,
        "abs_return_acf_20": 0.35817486066558646,
        "quantile_01": -0.051372908254779776,
        "quantile_99": 0.0486259550035631,
        "hill_tail_index": 3.4810061381000525
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018996827995747208,
        "excess_kurtosis": 5.751771450699948,
        "return_acf_1": -0.10672813972046084,
        "abs_return_acf_1": 0.41188050278541705,
        "abs_return_acf_5": 0.3116523293986383,
        "abs_return_acf_20": 0.33281461844092564,
        "quantile_01": -0.05729182719909196,
        "quantile_99": 0.05707011596196268,
        "hill_tail_index": 3.856395432240549
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
