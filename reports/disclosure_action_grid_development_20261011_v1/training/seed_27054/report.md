# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27054
Run ID: `71daf4d03894fb03b3640cfeefdb82db4b354a3013ba9041a485c1c3d4882599`
Result fingerprint: `da481113202cd6b17e60a2ceed5fdd1619cd4d208f6d354f9a9d008cb9c5b3f9`

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
    "equal_weight_sd": -0.5532976190476158,
    "equal_weight_raw": -8.299464285714237,
    "fixed_start_cap_weight_sd": -0.5631060349001464,
    "fixed_start_cap_weight_raw": -8.446590523502199,
    "end_cap_weight_sd": -0.547598365881545,
    "end_cap_weight_raw": -8.213975488223177
  },
  "full_period_change": {
    "equal_weight_sd": -0.8370714285714237,
    "equal_weight_raw": -12.556071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7913931878306832,
    "inflation_mean_sd": 0.7843022486772486
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3776126499915783,
    "equal_weight_raw": 5.664189749873676,
    "fixed_start_cap_weight_sd": 0.3824400239504984,
    "fixed_start_cap_weight_raw": 5.736600359257477,
    "end_cap_weight_sd": 0.3967371890919169,
    "end_cap_weight_raw": 5.951057836378753
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5682142857142826,
      "change_raw": -8.52321428571424,
      "decay_adjusted_gain_sd": 0.3841666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5957142857142824,
      "change_raw": -8.935714285714237,
      "decay_adjusted_gain_sd": 0.3566666666666698
    },
    "small": {
      "count": 18,
      "change_sd": -0.5296031746031713,
      "change_raw": -7.94404761904757,
      "decay_adjusted_gain_sd": 0.3869933055415175
    },
    "large_minus_small_sd": -0.03861111111111126,
    "large_minus_small_raw": -0.5791666666666689
  },
  "inflation": {
    "initial_mean_sd": 0.27516666666666667,
    "final_mean_sd": 0.8159166666666665,
    "mean_sd": 0.5543318762142658,
    "mean_absolute_raw_gap": 8.314978143213988,
    "final_absolute_raw_gap": 12.23875,
    "mean_range_fraction": 0.08314978143213989
  },
  "impact": {
    "initial_share": 0.3,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.36163013341245004,
    "final_wealth_share": 0.3493436424958405
  },
  "pricing_slope": {
    "mean": 0.0012017541594116295,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.06858186051289902,
    "real_improvement_cost": 0.059392782708637355,
    "washing_cost": 0.009189077804261675,
    "fine_transfer": 0.004823763084014337,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07340562359691336,
    "resource_cost_fraction_initial_cap": 0.002286062017096634,
    "private_net_outflow_fraction_initial_cap": 0.002446854119897112,
    "fine_transfer_fraction_initial_cap": 0.00016079210280047792,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0035338132283593447,
    "unapplied_final_day_resource_cost": 0.000274008578053866
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 165.18040506668208,
    "beneficial_raw_gain_per_resource_cost": 2477.7060760002314,
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
    "accrued_cost": 3.152980181182422,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.17678970499194566,
    "accrued_cost_fraction_initial_cap": 0.10509933937274739,
    "mean_contract_rate": 0.043691127019513096,
    "maximum_ledger_error": 1.4907779871675686e-19
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
    "price_cap_hits": 14,
    "maximum_relative_cash_error": 2.343859720903426e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.2965143128000257,
      "maximum": -0.026705688257958386,
      "mean": -0.18611113418101113,
      "median": -0.1946100791704628,
      "quantile_05": -0.2812580837660723,
      "quantile_95": -0.06736150671257977
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
      "minimum": 0.18011076588928174,
      "maximum": 0.8348262007927915,
      "mean": 0.47711632605640486,
      "median": 0.4618708791837031,
      "quantile_05": 0.2231776891262171,
      "quantile_95": 0.8014433028855155
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
        "daily_volatility": 0.02080275592936262,
        "excess_kurtosis": 21.72408701091569,
        "return_acf_1": -0.18045289270977816,
        "abs_return_acf_1": 0.298508213487899,
        "abs_return_acf_5": 0.2610627994246519,
        "abs_return_acf_20": 0.24110785363079898,
        "quantile_01": -0.06102752860206286,
        "quantile_99": 0.047265465122544384,
        "hill_tail_index": 2.1582378000605384
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017765451640844237,
        "excess_kurtosis": 4.6456465564238805,
        "return_acf_1": -0.20164916423618942,
        "abs_return_acf_1": 0.21483776871238766,
        "abs_return_acf_5": 0.25771165963177933,
        "abs_return_acf_20": 0.19697607222479194,
        "quantile_01": -0.0534830745752811,
        "quantile_99": 0.04717045197060698,
        "hill_tail_index": 2.7431841217330235
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.0204963368432591,
        "excess_kurtosis": 5.5480947536256515,
        "return_acf_1": -0.12602308836626297,
        "abs_return_acf_1": 0.3061090126918828,
        "abs_return_acf_5": 0.35640866133155763,
        "abs_return_acf_20": 0.25738249517187606,
        "quantile_01": -0.06608869886633803,
        "quantile_99": 0.057780524870741506,
        "hill_tail_index": 4.185046024850819
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.024514210782381318,
        "excess_kurtosis": 21.340697809790058,
        "return_acf_1": -0.21209586255442833,
        "abs_return_acf_1": 0.4418711331000058,
        "abs_return_acf_5": 0.4060735145919041,
        "abs_return_acf_20": 0.3436012611151349,
        "quantile_01": -0.08367356479860012,
        "quantile_99": 0.0617168084762132,
        "hill_tail_index": 2.2842363512527752
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02126874783457034,
        "excess_kurtosis": 11.461399348793156,
        "return_acf_1": -0.24142549424585905,
        "abs_return_acf_1": 0.44211825405276073,
        "abs_return_acf_5": 0.37017811175790377,
        "abs_return_acf_20": 0.31594192682638117,
        "quantile_01": -0.0785927714264758,
        "quantile_99": 0.05483461099290573,
        "hill_tail_index": 2.5155182255123516
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023606336236598947,
        "excess_kurtosis": 31.600642583327307,
        "return_acf_1": -0.2514559404038224,
        "abs_return_acf_1": 0.41697576794867836,
        "abs_return_acf_5": 0.3089739578412782,
        "abs_return_acf_20": 0.2723154493869091,
        "quantile_01": -0.06949515521901384,
        "quantile_99": 0.057185476406923105,
        "hill_tail_index": 1.8461440388089307
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022087565722508577,
        "excess_kurtosis": 10.81824579844532,
        "return_acf_1": -0.16599062737503925,
        "abs_return_acf_1": 0.33526872507955086,
        "abs_return_acf_5": 0.34885715381903804,
        "abs_return_acf_20": 0.3451660438208128,
        "quantile_01": -0.06746594128004173,
        "quantile_99": 0.06773234582467959,
        "hill_tail_index": 2.9595338560531137
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02579817617381368,
        "excess_kurtosis": 20.231717487785247,
        "return_acf_1": -0.21326220448950964,
        "abs_return_acf_1": 0.3951337134847427,
        "abs_return_acf_5": 0.4163935522421628,
        "abs_return_acf_20": 0.35337861897955986,
        "quantile_01": -0.09313674707630133,
        "quantile_99": 0.06717654897587534,
        "hill_tail_index": 2.1539776483086346
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.023384523100831965,
        "excess_kurtosis": 19.958624169445404,
        "return_acf_1": -0.21009299948858287,
        "abs_return_acf_1": 0.35209456534170597,
        "abs_return_acf_5": 0.35704021656887464,
        "abs_return_acf_20": 0.3368590801331807,
        "quantile_01": -0.08096981764424062,
        "quantile_99": 0.04920295070449388,
        "hill_tail_index": 1.8216407185059942
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023316469084605763,
        "excess_kurtosis": 31.306339567902782,
        "return_acf_1": -0.21826786307375004,
        "abs_return_acf_1": 0.3931532808427881,
        "abs_return_acf_5": 0.33574929132233183,
        "abs_return_acf_20": 0.3380523740691247,
        "quantile_01": -0.06777487854067409,
        "quantile_99": 0.05468370789344182,
        "hill_tail_index": 1.958020998491196
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.0225880143987512,
        "excess_kurtosis": 5.576852911758781,
        "return_acf_1": -0.1320054881979606,
        "abs_return_acf_1": 0.40006288224103853,
        "abs_return_acf_5": 0.4141128492422719,
        "abs_return_acf_20": 0.34877062913735996,
        "quantile_01": -0.08361739800945206,
        "quantile_99": 0.06880224817189454,
        "hill_tail_index": 5.714917560486605
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024348330408444835,
        "excess_kurtosis": 24.385325519694554,
        "return_acf_1": -0.2262017722443988,
        "abs_return_acf_1": 0.3868679490101319,
        "abs_return_acf_5": 0.3863396067586618,
        "abs_return_acf_20": 0.3517703396564755,
        "quantile_01": -0.07255623300107578,
        "quantile_99": 0.05505027032979444,
        "hill_tail_index": 2.006040561472899
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022265366535046648,
        "excess_kurtosis": 25.58615875137452,
        "return_acf_1": -0.15884310498656445,
        "abs_return_acf_1": 0.25204565792763556,
        "abs_return_acf_5": 0.24622786471155297,
        "abs_return_acf_20": 0.21690254276255747,
        "quantile_01": -0.073539461863141,
        "quantile_99": 0.056687462302025454,
        "hill_tail_index": 2.51951145520521
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022662381497467694,
        "excess_kurtosis": 8.15296613693929,
        "return_acf_1": -0.15739089889863483,
        "abs_return_acf_1": 0.4576001669134183,
        "abs_return_acf_5": 0.3936710110619536,
        "abs_return_acf_20": 0.2953058616542727,
        "quantile_01": -0.07250166588954987,
        "quantile_99": 0.06772911810662667,
        "hill_tail_index": 3.1769303042938355
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018942035570300986,
        "excess_kurtosis": 15.139631257832225,
        "return_acf_1": -0.026705688257958386,
        "abs_return_acf_1": 0.3487887302013299,
        "abs_return_acf_5": 0.43114811193965946,
        "abs_return_acf_20": 0.2592617844954255,
        "quantile_01": -0.04634515634611219,
        "quantile_99": 0.06329564048808743,
        "hill_tail_index": 2.035606689063838
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01987794001572285,
        "excess_kurtosis": 8.12600377934648,
        "return_acf_1": -0.14771465734721337,
        "abs_return_acf_1": 0.3087307355916281,
        "abs_return_acf_5": 0.35392086146631385,
        "abs_return_acf_20": 0.26644865771560833,
        "quantile_01": -0.07706736627885648,
        "quantile_99": 0.05645678834847676,
        "hill_tail_index": 2.9967612571342044
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023115969417564552,
        "excess_kurtosis": 23.21691822430457,
        "return_acf_1": -0.21548553385853986,
        "abs_return_acf_1": 0.4336010324613807,
        "abs_return_acf_5": 0.34863034886877015,
        "abs_return_acf_20": 0.3403772371666492,
        "quantile_01": -0.07595679574646605,
        "quantile_99": 0.05147404056768756,
        "hill_tail_index": 1.6518767741917937
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02206233588688526,
        "excess_kurtosis": 20.115526353373767,
        "return_acf_1": -0.18980711019092986,
        "abs_return_acf_1": 0.36088035024725695,
        "abs_return_acf_5": 0.36226440252264747,
        "abs_return_acf_20": 0.3645173038352161,
        "quantile_01": -0.06709873683996115,
        "quantile_99": 0.051864810427611846,
        "hill_tail_index": 2.113926008065103
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021199106232544555,
        "excess_kurtosis": 7.303722452772078,
        "return_acf_1": -0.09548026554976181,
        "abs_return_acf_1": 0.3399636120045134,
        "abs_return_acf_5": 0.3732515270398708,
        "abs_return_acf_20": 0.33438330402813315,
        "quantile_01": -0.07252749566421837,
        "quantile_99": 0.0634123268265607,
        "hill_tail_index": 3.693157116653038
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02166583431417854,
        "excess_kurtosis": 5.60319874416709,
        "return_acf_1": -0.044355249482157834,
        "abs_return_acf_1": 0.3905938367242336,
        "abs_return_acf_5": 0.3714015852789376,
        "abs_return_acf_20": 0.31422092308049726,
        "quantile_01": -0.07833589863943412,
        "quantile_99": 0.0642334067665185,
        "hill_tail_index": 3.923233126459384
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023637760755893963,
        "excess_kurtosis": 35.31848540933983,
        "return_acf_1": -0.281862806344605,
        "abs_return_acf_1": 0.4205295827417379,
        "abs_return_acf_5": 0.23289189073479757,
        "abs_return_acf_20": 0.22831065332831837,
        "quantile_01": -0.06956427054129032,
        "quantile_99": 0.050954909682454974,
        "hill_tail_index": 2.098185488914665
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.023261022041545534,
        "excess_kurtosis": 11.602781302174298,
        "return_acf_1": -0.16912516013687778,
        "abs_return_acf_1": 0.400584082744651,
        "abs_return_acf_5": 0.38716052474663437,
        "abs_return_acf_20": 0.3673904995059055,
        "quantile_01": -0.0786696618765836,
        "quantile_99": 0.06065840080208152,
        "hill_tail_index": 2.5115047511796957
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023101056345698617,
        "excess_kurtosis": 8.78495534676651,
        "return_acf_1": -0.13719243212629584,
        "abs_return_acf_1": 0.3365792338469601,
        "abs_return_acf_5": 0.38884979757905896,
        "abs_return_acf_20": 0.3481366996099447,
        "quantile_01": -0.0916531864644113,
        "quantile_99": 0.07138878766456813,
        "hill_tail_index": 3.1376551497174976
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02304972204385006,
        "excess_kurtosis": 36.659850927697484,
        "return_acf_1": -0.2965143128000257,
        "abs_return_acf_1": 0.4289054920158426,
        "abs_return_acf_5": 0.39934219034736357,
        "abs_return_acf_20": 0.29219662872851376,
        "quantile_01": -0.058825939586434,
        "quantile_99": 0.04552149690892062,
        "hill_tail_index": 1.762032317718697
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02405893204900826,
        "excess_kurtosis": 29.228255331687684,
        "return_acf_1": -0.2805189783923102,
        "abs_return_acf_1": 0.46837950149172414,
        "abs_return_acf_5": 0.3806454389488519,
        "abs_return_acf_20": 0.3466109235916142,
        "quantile_01": -0.06796693847050306,
        "quantile_99": 0.04649788010564103,
        "hill_tail_index": 1.5682226485539317
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.024400260772470966,
        "excess_kurtosis": 30.436097838453065,
        "return_acf_1": -0.1955224742031802,
        "abs_return_acf_1": 0.40493554704703494,
        "abs_return_acf_5": 0.4051635160096908,
        "abs_return_acf_20": 0.31760465506348673,
        "quantile_01": -0.07570030731876551,
        "quantile_99": 0.05501838980028208,
        "hill_tail_index": 1.9400715348958022
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.024733267951019395,
        "excess_kurtosis": 35.185588370544195,
        "return_acf_1": -0.22801363946610778,
        "abs_return_acf_1": 0.44579518463651013,
        "abs_return_acf_5": 0.3736474043207729,
        "abs_return_acf_20": 0.3412460421916829,
        "quantile_01": -0.07683359300894939,
        "quantile_99": 0.05886880147331704,
        "hill_tail_index": 1.9271817580298185
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022793211181903094,
        "excess_kurtosis": 27.051639277046373,
        "return_acf_1": -0.1898984782441601,
        "abs_return_acf_1": 0.33242092248848504,
        "abs_return_acf_5": 0.3424862469484057,
        "abs_return_acf_20": 0.3130900291447387,
        "quantile_01": -0.07024935515088934,
        "quantile_99": 0.056582793389171306,
        "hill_tail_index": 2.5368917476764
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020573529897859842,
        "excess_kurtosis": 3.653547381648494,
        "return_acf_1": -0.19628215362168452,
        "abs_return_acf_1": 0.2674309316464891,
        "abs_return_acf_5": 0.27334759884553106,
        "abs_return_acf_20": 0.19867454908057355,
        "quantile_01": -0.0636656676413828,
        "quantile_99": 0.05188235129521885,
        "hill_tail_index": 3.3326958857405886
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021762034638167584,
        "excess_kurtosis": 8.920786970588633,
        "return_acf_1": -0.1936976841377454,
        "abs_return_acf_1": 0.43306841426844633,
        "abs_return_acf_5": 0.44102298200004636,
        "abs_return_acf_20": 0.3259578313701309,
        "quantile_01": -0.07146634485829313,
        "quantile_99": 0.056463727441147624,
        "hill_tail_index": 2.9296512258155705
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
