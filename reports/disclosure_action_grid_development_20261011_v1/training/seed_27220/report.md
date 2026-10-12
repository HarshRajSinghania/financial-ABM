# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27220
Run ID: `68037328175aab415baab0bfb2717371ee0e588b529af4f01b8a3f5730127225`
Result fingerprint: `2df8bf2366145e5de78c0de2d1809df28a6cca36eb994a5d97ee098ec6256bac`

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
    "equal_weight_sd": -0.8331143777827437,
    "equal_weight_raw": -12.496715666741158,
    "fixed_start_cap_weight_sd": -0.7832694018628104,
    "fixed_start_cap_weight_raw": -11.74904102794216,
    "end_cap_weight_sd": -0.8006825243940897,
    "end_cap_weight_raw": -12.010237865911348
  },
  "full_period_change": {
    "equal_weight_sd": -1.2670548539732183,
    "equal_weight_raw": -19.005822809598275
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1880078175660629,
    "inflation_mean_sd": 0.547049933862434
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11016666666666976,
    "equal_weight_raw": 1.6525000000000463,
    "fixed_start_cap_weight_sd": 0.15648239312052792,
    "fixed_start_cap_weight_raw": 2.347235896807919,
    "end_cap_weight_sd": 0.1349217767678114,
    "end_cap_weight_raw": 2.0238266515171706
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7557142857142823,
      "change_raw": -11.335714285714236,
      "decay_adjusted_gain_sd": 0.19666666666666996
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8217701481647087,
      "change_raw": -12.326552222470632,
      "decay_adjusted_gain_sd": 0.10027777777778052
    },
    "small": {
      "count": 18,
      "change_sd": -0.8516865079365047,
      "change_raw": -12.77529761904757,
      "decay_adjusted_gain_sd": 0.10069444444444768
    },
    "large_minus_small_sd": 0.09597222222222235,
    "large_minus_small_raw": 1.4395833333333352
  },
  "inflation": {
    "initial_mean_sd": 0.31216666666666665,
    "final_mean_sd": 0.5680833333333335,
    "mean_sd": 0.43322904524007777,
    "mean_absolute_raw_gap": 6.498435678601167,
    "final_absolute_raw_gap": 8.521250000000002,
    "mean_range_fraction": 0.06498435678601167
  },
  "impact": {
    "initial_share": 0.5266666666666666,
    "final_share": 0.56,
    "initial_wealth_share": 0.528405547244994,
    "final_wealth_share": 0.5608000914316031
  },
  "pricing_slope": {
    "mean": -0.0029890494869489357,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.04426004323499577,
    "real_improvement_cost": 0.03733903489523572,
    "washing_cost": 0.006921008339760049,
    "fine_transfer": 0.027649780025491396,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07190982326048717,
    "resource_cost_fraction_initial_cap": 0.0014753347744998594,
    "private_net_outflow_fraction_initial_cap": 0.0023969941086829064,
    "fine_transfer_fraction_initial_cap": 0.0009216593341830467,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.05656174164776009,
    "unapplied_final_day_resource_cost": 0.000601763274853218
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 74.6723174772427,
    "beneficial_raw_gain_per_resource_cost": 1120.0847621586406,
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
    "accrued_cost": 3.1329494666176623,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.15675899042718644,
    "accrued_cost_fraction_initial_cap": 0.10443164888725544,
    "mean_contract_rate": 0.04457244531749216,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.4272439757095092e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.208231649967428,
      "maximum": -0.015867195662589012,
      "mean": -0.101444442492639,
      "median": -0.0959300325293184,
      "quantile_05": -0.1887435420326045,
      "quantile_95": -0.02661988506987425
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
      "minimum": 0.4722998468244781,
      "maximum": 0.784053705738692,
      "mean": 0.67886110063746,
      "median": 0.6877806502985474,
      "quantile_05": 0.5713470534560784,
      "quantile_95": 0.7551354118600938
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
        "daily_volatility": 0.019370709168126637,
        "excess_kurtosis": 16.45475811083139,
        "return_acf_1": -0.1349478695637278,
        "abs_return_acf_1": 0.39588397397691893,
        "abs_return_acf_5": 0.37518452130274627,
        "abs_return_acf_20": 0.3181273644421864,
        "quantile_01": -0.057256744325368154,
        "quantile_99": 0.04833191360564415,
        "hill_tail_index": 2.672184487612214
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01818643969261074,
        "excess_kurtosis": 9.674593198986123,
        "return_acf_1": -0.032121567696876886,
        "abs_return_acf_1": 0.3748775308649649,
        "abs_return_acf_5": 0.3239615687531648,
        "abs_return_acf_20": 0.2495529657580126,
        "quantile_01": -0.05894050475977,
        "quantile_99": 0.04795099205986919,
        "hill_tail_index": 2.5367022818441978
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019280794681580653,
        "excess_kurtosis": 23.343510926414016,
        "return_acf_1": -0.208231649967428,
        "abs_return_acf_1": 0.4426454435366741,
        "abs_return_acf_5": 0.40679239606635026,
        "abs_return_acf_20": 0.3357071417614554,
        "quantile_01": -0.06031470194312866,
        "quantile_99": 0.04804719372188186,
        "hill_tail_index": 2.3379072957210894
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018347902882788553,
        "excess_kurtosis": 11.701795998211916,
        "return_acf_1": -0.08423617762200658,
        "abs_return_acf_1": 0.33305523302702644,
        "abs_return_acf_5": 0.39632002834443286,
        "abs_return_acf_20": 0.250214867197254,
        "quantile_01": -0.056551190450341585,
        "quantile_99": 0.04662599721397494,
        "hill_tail_index": 2.8501382103809707
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020485880349153825,
        "excess_kurtosis": 24.252795741489006,
        "return_acf_1": -0.19123563380130765,
        "abs_return_acf_1": 0.3438776829882765,
        "abs_return_acf_5": 0.4000673899334988,
        "abs_return_acf_20": 0.3443098534153316,
        "quantile_01": -0.0780049122275427,
        "quantile_99": 0.05643161569347821,
        "hill_tail_index": 2.434888506651197
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01995610247666529,
        "excess_kurtosis": 18.553963312038565,
        "return_acf_1": -0.09737953294223756,
        "abs_return_acf_1": 0.31884436163259805,
        "abs_return_acf_5": 0.24527612029663118,
        "abs_return_acf_20": 0.3045075525206266,
        "quantile_01": -0.06718561233976528,
        "quantile_99": 0.05239374586146498,
        "hill_tail_index": 2.812975260851743
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01810559898836169,
        "excess_kurtosis": 9.740890824882179,
        "return_acf_1": -0.04330690895022761,
        "abs_return_acf_1": 0.4379394226064738,
        "abs_return_acf_5": 0.3275829531935649,
        "abs_return_acf_20": 0.2957927130659822,
        "quantile_01": -0.06378152261381893,
        "quantile_99": 0.04811676788560036,
        "hill_tail_index": 2.5837071834379604
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017271688087275774,
        "excess_kurtosis": 13.662612941630982,
        "return_acf_1": -0.0491010369682443,
        "abs_return_acf_1": 0.2957544497495886,
        "abs_return_acf_5": 0.2333995857798089,
        "abs_return_acf_20": 0.17037245911740154,
        "quantile_01": -0.055892294915974805,
        "quantile_99": 0.04868501547711488,
        "hill_tail_index": 2.296958253257997
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017561872636011392,
        "excess_kurtosis": 14.022401340932955,
        "return_acf_1": -0.0741829073398858,
        "abs_return_acf_1": 0.2752330078475675,
        "abs_return_acf_5": 0.23940104020630004,
        "abs_return_acf_20": 0.23972463980791117,
        "quantile_01": -0.05606330652722125,
        "quantile_99": 0.03913391845306763,
        "hill_tail_index": 2.6469699154177517
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018770619911244558,
        "excess_kurtosis": 18.37094347983096,
        "return_acf_1": -0.10764369786690736,
        "abs_return_acf_1": 0.33325528712012753,
        "abs_return_acf_5": 0.36127207546702217,
        "abs_return_acf_20": 0.2793837802293263,
        "quantile_01": -0.05657943079234069,
        "quantile_99": 0.04834745091941841,
        "hill_tail_index": 2.3784340494733303
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018938927504579477,
        "excess_kurtosis": 28.579473973907334,
        "return_acf_1": -0.1672468262880519,
        "abs_return_acf_1": 0.4279384544668974,
        "abs_return_acf_5": 0.3774792183148392,
        "abs_return_acf_20": 0.29937240390550285,
        "quantile_01": -0.05955639224043844,
        "quantile_99": 0.04165833093053622,
        "hill_tail_index": 2.1299759156572384
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01874175680627781,
        "excess_kurtosis": 11.264519296266684,
        "return_acf_1": -0.09448053211639923,
        "abs_return_acf_1": 0.3952765128190551,
        "abs_return_acf_5": 0.3881245426937864,
        "abs_return_acf_20": 0.23710931203791688,
        "quantile_01": -0.06333345102055156,
        "quantile_99": 0.04785644438639129,
        "hill_tail_index": 2.2661353294672684
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021333483575739984,
        "excess_kurtosis": 27.07383272522547,
        "return_acf_1": -0.18569765209307842,
        "abs_return_acf_1": 0.4404600826598071,
        "abs_return_acf_5": 0.40386525966414777,
        "abs_return_acf_20": 0.3801371186793694,
        "quantile_01": -0.07034397565630139,
        "quantile_99": 0.059514307183177795,
        "hill_tail_index": 2.8105310862553177
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018882248856203467,
        "excess_kurtosis": 10.364725137198635,
        "return_acf_1": -0.09246785349824092,
        "abs_return_acf_1": 0.3812637169732988,
        "abs_return_acf_5": 0.33807566553800766,
        "abs_return_acf_20": 0.21917209124541626,
        "quantile_01": -0.05795220481479433,
        "quantile_99": 0.04784070566318446,
        "hill_tail_index": 2.4670763739978803
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018904651505102142,
        "excess_kurtosis": 25.695987107933338,
        "return_acf_1": -0.11079465850063361,
        "abs_return_acf_1": 0.37767236127250353,
        "abs_return_acf_5": 0.2813379095190673,
        "abs_return_acf_20": 0.2855706280151595,
        "quantile_01": -0.05248689796774608,
        "quantile_99": 0.03843504938147952,
        "hill_tail_index": 1.918829368032248
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017772720471886928,
        "excess_kurtosis": 17.313412754082677,
        "return_acf_1": -0.13259084605892202,
        "abs_return_acf_1": 0.254656271228647,
        "abs_return_acf_5": 0.27455066837715353,
        "abs_return_acf_20": 0.25347696224380595,
        "quantile_01": -0.05653349599088575,
        "quantile_99": 0.04015567895510942,
        "hill_tail_index": 2.6897952870325823
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019648826200135867,
        "excess_kurtosis": 17.836146692491056,
        "return_acf_1": -0.1140119833961539,
        "abs_return_acf_1": 0.32515623730331206,
        "abs_return_acf_5": 0.2895388307268459,
        "abs_return_acf_20": 0.24267921007223495,
        "quantile_01": -0.0542568408176727,
        "quantile_99": 0.04176049276770904,
        "hill_tail_index": 2.2618581986094974
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018438612979747186,
        "excess_kurtosis": 15.265215356095236,
        "return_acf_1": -0.10159168491664224,
        "abs_return_acf_1": 0.37214861553746376,
        "abs_return_acf_5": 0.30866991273089633,
        "abs_return_acf_20": 0.24429256100995506,
        "quantile_01": -0.05856045396785353,
        "quantile_99": 0.04917284860726275,
        "hill_tail_index": 2.896204143096764
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01818232027629685,
        "excess_kurtosis": 17.380894596660987,
        "return_acf_1": -0.0685856369223983,
        "abs_return_acf_1": 0.27282168071544205,
        "abs_return_acf_5": 0.3352192088189078,
        "abs_return_acf_20": 0.20598267928532818,
        "quantile_01": -0.06268654069802178,
        "quantile_99": 0.04147925724740856,
        "hill_tail_index": 2.4478835300135655
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01728309283927879,
        "excess_kurtosis": 8.365799296105337,
        "return_acf_1": -0.10445304428378105,
        "abs_return_acf_1": 0.31937825069713116,
        "abs_return_acf_5": 0.3308760542626022,
        "abs_return_acf_20": 0.19621912697868793,
        "quantile_01": -0.05351006327983369,
        "quantile_99": 0.05395708181289228,
        "hill_tail_index": 2.80474266867451
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01724146975861367,
        "excess_kurtosis": 17.470001313718132,
        "return_acf_1": -0.07415874392833637,
        "abs_return_acf_1": 0.19610151986444738,
        "abs_return_acf_5": 0.27330784218737886,
        "abs_return_acf_20": 0.19974652460530073,
        "quantile_01": -0.0502736537493202,
        "quantile_99": 0.0424463540279184,
        "hill_tail_index": 2.6586197885450407
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019120363838559747,
        "excess_kurtosis": 16.473674662669893,
        "return_acf_1": -0.02211850837505386,
        "abs_return_acf_1": 0.3232021412931116,
        "abs_return_acf_5": 0.3273785474081877,
        "abs_return_acf_20": 0.23448560034775395,
        "quantile_01": -0.0580916468232945,
        "quantile_99": 0.04710551374541293,
        "hill_tail_index": 1.9749500866425609
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01770180050009939,
        "excess_kurtosis": 11.456074366018505,
        "return_acf_1": -0.038648650792046824,
        "abs_return_acf_1": 0.3327655102380192,
        "abs_return_acf_5": 0.34254494977134053,
        "abs_return_acf_20": 0.2588488218392559,
        "quantile_01": -0.05260162363866672,
        "quantile_99": 0.045866967082476486,
        "hill_tail_index": 2.530724145283539
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01866913414027202,
        "excess_kurtosis": 8.259925705846094,
        "return_acf_1": -0.05436859087320569,
        "abs_return_acf_1": 0.3895397120330545,
        "abs_return_acf_5": 0.416804066766331,
        "abs_return_acf_20": 0.3353820515750727,
        "quantile_01": -0.05639148211391466,
        "quantile_99": 0.05271464234226398,
        "hill_tail_index": 2.9823468889648646
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018360758809564403,
        "excess_kurtosis": 10.827830439290437,
        "return_acf_1": -0.015867195662589012,
        "abs_return_acf_1": 0.3117099015408852,
        "abs_return_acf_5": 0.28947016836652967,
        "abs_return_acf_20": 0.2674358974911179,
        "quantile_01": -0.053477652052989245,
        "quantile_99": 0.041555165081207324,
        "hill_tail_index": 2.1227391809546488
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019167545750379593,
        "excess_kurtosis": 21.842245604269387,
        "return_acf_1": -0.09217942762833753,
        "abs_return_acf_1": 0.3247822851455968,
        "abs_return_acf_5": 0.2942087217767847,
        "abs_return_acf_20": 0.27936494664739264,
        "quantile_01": -0.06307737827651379,
        "quantile_99": 0.04465210136413374,
        "hill_tail_index": 2.506841764313946
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018817133174365536,
        "excess_kurtosis": 31.373558002849776,
        "return_acf_1": -0.17852280071541704,
        "abs_return_acf_1": 0.39163529752060605,
        "abs_return_acf_5": 0.3674614672242706,
        "abs_return_acf_20": 0.3554781857109141,
        "quantile_01": -0.05704975636958965,
        "quantile_99": 0.04498273698780899,
        "hill_tail_index": 2.5089448474036375
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01914867637083571,
        "excess_kurtosis": 25.799971846952527,
        "return_acf_1": -0.16077777076415695,
        "abs_return_acf_1": 0.37403786967480923,
        "abs_return_acf_5": 0.3115089368704644,
        "abs_return_acf_20": 0.2926473869558654,
        "quantile_01": -0.059570740555517566,
        "quantile_99": 0.04073398937581685,
        "hill_tail_index": 2.0233213859243016
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019580063477908156,
        "excess_kurtosis": 20.31410417672776,
        "return_acf_1": -0.1268772103798757,
        "abs_return_acf_1": 0.33221407583526297,
        "abs_return_acf_5": 0.33678665443723743,
        "abs_return_acf_20": 0.32083104373510807,
        "quantile_01": -0.05777116082181583,
        "quantile_99": 0.04647245300986245,
        "hill_tail_index": 2.518677244873563
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017299994094881286,
        "excess_kurtosis": 9.28614527145889,
        "return_acf_1": -0.08550667486699978,
        "abs_return_acf_1": 0.3305964221622159,
        "abs_return_acf_5": 0.3546419469924635,
        "abs_return_acf_20": 0.23221958757711392,
        "quantile_01": -0.05501694859814732,
        "quantile_99": 0.051718064626201064,
        "hill_tail_index": 3.026397573224989
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
