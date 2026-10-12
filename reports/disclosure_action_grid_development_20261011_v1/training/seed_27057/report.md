# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27057
Run ID: `6f58a8d2195f1f29e029e361a1b13a3962569de07784c5f9db790d796a6ca130`
Result fingerprint: `cbe8b9f76ca3cae31861b72c0eda13a3442e2dad856b9ec89341c18e2a5887ff`

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
    "equal_weight_sd": -0.5229348169135988,
    "equal_weight_raw": -7.844022253703982,
    "fixed_start_cap_weight_sd": -0.4673448459909376,
    "fixed_start_cap_weight_raw": -7.010172689864066,
    "end_cap_weight_sd": -0.4290082841056416,
    "end_cap_weight_raw": -6.435124261584624
  },
  "full_period_change": {
    "equal_weight_sd": -0.8572086264374067,
    "equal_weight_raw": -12.8581293965611
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.831117718778047,
    "inflation_mean_sd": 0.6392648809523809
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3875833333333363,
    "equal_weight_raw": 5.813750000000044,
    "fixed_start_cap_weight_sd": 0.4370609927338645,
    "fixed_start_cap_weight_raw": 6.555914891007967,
    "end_cap_weight_sd": 0.48508449938939413,
    "end_cap_weight_raw": 7.276267490840912
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6048809523809491,
      "change_raw": -9.073214285714236,
      "decay_adjusted_gain_sd": 0.34750000000000325
    },
    "mid": {
      "count": 9,
      "change_sd": -0.42265050455393005,
      "change_raw": -6.339757568308951,
      "decay_adjusted_gain_sd": 0.453611111111114
    },
    "small": {
      "count": 18,
      "change_sd": -0.5594192838488748,
      "change_raw": -8.391289257733122,
      "decay_adjusted_gain_sd": 0.36125000000000296
    },
    "large_minus_small_sd": -0.04546166853207423,
    "large_minus_small_raw": -0.6819250279811134
  },
  "inflation": {
    "initial_mean_sd": 0.2768333333333334,
    "final_mean_sd": 0.6715,
    "mean_sd": 0.4986384956980294,
    "mean_absolute_raw_gap": 7.479577435470443,
    "final_absolute_raw_gap": 10.072500000000002,
    "mean_range_fraction": 0.07479577435470443
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.52,
    "initial_wealth_share": 0.2877778779446078,
    "final_wealth_share": 0.4952402925676849
  },
  "pricing_slope": {
    "mean": -0.0007023109707954713,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.892849285852978,
    "real_improvement_cost": 0.7861023439444355,
    "washing_cost": 0.10674694190854243,
    "fine_transfer": 0.018008064111443657,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.9108573499644216,
    "resource_cost_fraction_initial_cap": 0.02976164286176594,
    "private_net_outflow_fraction_initial_cap": 0.03036191166548073,
    "fine_transfer_fraction_initial_cap": 0.0006002688037147888,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001708560577862345,
    "unapplied_final_day_resource_cost": 0.056864885416552484
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 13.022914599625658,
    "beneficial_raw_gain_per_resource_cost": 195.34371899438486,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 2.902022281933215,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.07416819425726162,
    "accrued_cost_fraction_initial_cap": 0.09673407606444054,
    "mean_contract_rate": 0.04102055338128093,
    "maximum_ledger_error": 4.404571325722362e-20
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
    "maximum_relative_cash_error": 1.3978931468472878e-15,
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
      "minimum": -0.24563174523831732,
      "maximum": -0.08822548412855721,
      "mean": -0.16556516932663123,
      "median": -0.17639471729169337,
      "quantile_05": -0.2264388787339453,
      "quantile_95": -0.10606093159002787
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
      "minimum": 0.21182798383964674,
      "maximum": 0.8350486638028584,
      "mean": 0.6072396557517596,
      "median": 0.6494751180156917,
      "quantile_05": 0.2634428504048666,
      "quantile_95": 0.8008399248124055
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
        "daily_volatility": 0.020597658627406097,
        "excess_kurtosis": 8.645650049141455,
        "return_acf_1": -0.17373867249474265,
        "abs_return_acf_1": 0.4032876709355737,
        "abs_return_acf_5": 0.3578552854463901,
        "abs_return_acf_20": 0.3157321251528768,
        "quantile_01": -0.07370700955485363,
        "quantile_99": 0.059085762930985664,
        "hill_tail_index": 4.08934379906009
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022328783555151503,
        "excess_kurtosis": 11.413441586783671,
        "return_acf_1": -0.20022242466174978,
        "abs_return_acf_1": 0.38154225014649135,
        "abs_return_acf_5": 0.3442073344332719,
        "abs_return_acf_20": 0.31219891497839247,
        "quantile_01": -0.07132952736134474,
        "quantile_99": 0.06259159373158249,
        "hill_tail_index": 3.269210505161734
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021916239340032655,
        "excess_kurtosis": 11.766012000687878,
        "return_acf_1": -0.1739176989499881,
        "abs_return_acf_1": 0.37427870696683546,
        "abs_return_acf_5": 0.3521380465717866,
        "abs_return_acf_20": 0.3390791766231934,
        "quantile_01": -0.07566521307113967,
        "quantile_99": 0.05774085191182462,
        "hill_tail_index": 4.049749329174403
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021556970873871192,
        "excess_kurtosis": 7.907704995198804,
        "return_acf_1": -0.12281942884459858,
        "abs_return_acf_1": 0.3551882912581296,
        "abs_return_acf_5": 0.33783995266742683,
        "abs_return_acf_20": 0.32051182999168776,
        "quantile_01": -0.05579729128401409,
        "quantile_99": 0.06616872870672047,
        "hill_tail_index": 3.101963684897741
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019180209742588775,
        "excess_kurtosis": 5.0907533102549465,
        "return_acf_1": -0.14476743153175034,
        "abs_return_acf_1": 0.3797439406522117,
        "abs_return_acf_5": 0.2815634687568516,
        "abs_return_acf_20": 0.3170244285239094,
        "quantile_01": -0.055763195520605637,
        "quantile_99": 0.05798191310570624,
        "hill_tail_index": 4.516635959498828
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02256958504904766,
        "excess_kurtosis": 11.550804678240329,
        "return_acf_1": -0.15140078794558903,
        "abs_return_acf_1": 0.4029459011441789,
        "abs_return_acf_5": 0.3787169355879106,
        "abs_return_acf_20": 0.3651857048857789,
        "quantile_01": -0.08567499971921975,
        "quantile_99": 0.06329011456033495,
        "hill_tail_index": 3.1656069325549883
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023663816624681644,
        "excess_kurtosis": 14.907367154934366,
        "return_acf_1": -0.18496593762468838,
        "abs_return_acf_1": 0.43746811525517143,
        "abs_return_acf_5": 0.32604352519580143,
        "abs_return_acf_20": 0.307585733540029,
        "quantile_01": -0.08372079765677205,
        "quantile_99": 0.0660932016395367,
        "hill_tail_index": 2.463424797097418
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021224694493784432,
        "excess_kurtosis": 17.52240364924473,
        "return_acf_1": -0.08822548412855721,
        "abs_return_acf_1": 0.37509719927592305,
        "abs_return_acf_5": 0.38437055835724687,
        "abs_return_acf_20": 0.3298017708020979,
        "quantile_01": -0.07241645683464686,
        "quantile_99": 0.05874506291616872,
        "hill_tail_index": 3.3244224131904003
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021899609070013523,
        "excess_kurtosis": 18.16954986741865,
        "return_acf_1": -0.19439640541837477,
        "abs_return_acf_1": 0.398572866660338,
        "abs_return_acf_5": 0.3670747845188298,
        "abs_return_acf_20": 0.3324294014530086,
        "quantile_01": -0.07064128031435626,
        "quantile_99": 0.06379597959062767,
        "hill_tail_index": 2.6172323110900866
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0223008602857447,
        "excess_kurtosis": 12.170008601866863,
        "return_acf_1": -0.18402178926190574,
        "abs_return_acf_1": 0.41197082580199634,
        "abs_return_acf_5": 0.36497059437699164,
        "abs_return_acf_20": 0.315436738164746,
        "quantile_01": -0.07398969492351684,
        "quantile_99": 0.05345821447445526,
        "hill_tail_index": 2.8907709612918673
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.023062030792194762,
        "excess_kurtosis": 11.029874520651202,
        "return_acf_1": -0.18734230375616387,
        "abs_return_acf_1": 0.4149711022136087,
        "abs_return_acf_5": 0.37910146238114445,
        "abs_return_acf_20": 0.40021088978329017,
        "quantile_01": -0.08160321917994173,
        "quantile_99": 0.05805599070015455,
        "hill_tail_index": 3.391057846504111
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022018477790186057,
        "excess_kurtosis": 10.441023530623166,
        "return_acf_1": -0.12108791234336155,
        "abs_return_acf_1": 0.3798371228829919,
        "abs_return_acf_5": 0.3900444259725568,
        "abs_return_acf_20": 0.31563584430473246,
        "quantile_01": -0.06773867777744316,
        "quantile_99": 0.06009043915532092,
        "hill_tail_index": 3.066246605304331
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01917169447473313,
        "excess_kurtosis": 4.193264886053107,
        "return_acf_1": -0.15937794271105937,
        "abs_return_acf_1": 0.3079494380996703,
        "abs_return_acf_5": 0.24064300343015813,
        "abs_return_acf_20": 0.29587742114962623,
        "quantile_01": -0.060456432058464606,
        "quantile_99": 0.05293607756417024,
        "hill_tail_index": 4.1285773636958325
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022378504275717068,
        "excess_kurtosis": 7.940267666310101,
        "return_acf_1": -0.10461284868917345,
        "abs_return_acf_1": 0.3789378082951493,
        "abs_return_acf_5": 0.3457714622264724,
        "abs_return_acf_20": 0.3032854824329431,
        "quantile_01": -0.05963220943107771,
        "quantile_99": 0.08257947183583224,
        "hill_tail_index": 4.118740473734368
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020483662633570803,
        "excess_kurtosis": 12.826970566872884,
        "return_acf_1": -0.10783081069107213,
        "abs_return_acf_1": 0.29694007872188505,
        "abs_return_acf_5": 0.362795605329474,
        "abs_return_acf_20": 0.31505137927384824,
        "quantile_01": -0.05807315967064896,
        "quantile_99": 0.06712237240455513,
        "hill_tail_index": 2.8330974063987737
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018689540904641047,
        "excess_kurtosis": 5.182007423312918,
        "return_acf_1": -0.12428398503178893,
        "abs_return_acf_1": 0.31706782362625646,
        "abs_return_acf_5": 0.30840490909243956,
        "abs_return_acf_20": 0.28984309200518565,
        "quantile_01": -0.06387529341202729,
        "quantile_99": 0.05738180426142993,
        "hill_tail_index": 3.7336636105260532
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02038510624547735,
        "excess_kurtosis": 7.709838863751569,
        "return_acf_1": -0.18082291304261058,
        "abs_return_acf_1": 0.39319829258923805,
        "abs_return_acf_5": 0.4072849532804682,
        "abs_return_acf_20": 0.32166659212051707,
        "quantile_01": -0.06813274209299709,
        "quantile_99": 0.07130757914051675,
        "hill_tail_index": 3.891444397635681
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022981196304297794,
        "excess_kurtosis": 13.070839100808051,
        "return_acf_1": -0.2183447057594628,
        "abs_return_acf_1": 0.4043615060545227,
        "abs_return_acf_5": 0.3922921579899567,
        "abs_return_acf_20": 0.32547274123272646,
        "quantile_01": -0.08091987333467883,
        "quantile_99": 0.06347799515026077,
        "hill_tail_index": 3.0762521583013704
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022704759260639636,
        "excess_kurtosis": 16.498029239212205,
        "return_acf_1": -0.19768964782468315,
        "abs_return_acf_1": 0.35880164443298845,
        "abs_return_acf_5": 0.38149330381486574,
        "abs_return_acf_20": 0.2857409623567018,
        "quantile_01": -0.06823130940414034,
        "quantile_99": 0.05845437132066315,
        "hill_tail_index": 2.4332458278231526
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02214445712612401,
        "excess_kurtosis": 9.433478285502563,
        "return_acf_1": -0.1899670921297753,
        "abs_return_acf_1": 0.4590933568590582,
        "abs_return_acf_5": 0.405882201171,
        "abs_return_acf_20": 0.36103193807360545,
        "quantile_01": -0.07888770011203833,
        "quantile_99": 0.057811697377852404,
        "hill_tail_index": 3.422119659865821
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023611990952448345,
        "excess_kurtosis": 12.59109046358667,
        "return_acf_1": -0.17887173563339867,
        "abs_return_acf_1": 0.4011398037336611,
        "abs_return_acf_5": 0.38039701693867256,
        "abs_return_acf_20": 0.3577491619593455,
        "quantile_01": -0.08783542796644919,
        "quantile_99": 0.06619574759440251,
        "hill_tail_index": 3.139065418504643
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0208273457632323,
        "excess_kurtosis": 9.592059290584144,
        "return_acf_1": -0.17977432136689192,
        "abs_return_acf_1": 0.39697620317460347,
        "abs_return_acf_5": 0.37092116729397084,
        "abs_return_acf_20": 0.3294317347346566,
        "quantile_01": -0.0695758400260887,
        "quantile_99": 0.058863939654409704,
        "hill_tail_index": 3.483098782717321
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018649132037329055,
        "excess_kurtosis": 3.2590505107584935,
        "return_acf_1": -0.12314783625984847,
        "abs_return_acf_1": 0.3084761885267232,
        "abs_return_acf_5": 0.24377407466549134,
        "abs_return_acf_20": 0.2089112052108267,
        "quantile_01": -0.04583514661706883,
        "quantile_99": 0.06303119209739969,
        "hill_tail_index": 4.176848290045757
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02237147729457428,
        "excess_kurtosis": 16.731270509937694,
        "return_acf_1": -0.24563174523831732,
        "abs_return_acf_1": 0.3811881986747461,
        "abs_return_acf_5": 0.37572424538188504,
        "abs_return_acf_20": 0.31216778148073454,
        "quantile_01": -0.08004908093007071,
        "quantile_99": 0.052912132665035055,
        "hill_tail_index": 2.14240403691267
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02457512196598426,
        "excess_kurtosis": 17.541193177185875,
        "return_acf_1": -0.23306138389488557,
        "abs_return_acf_1": 0.45756510953842905,
        "abs_return_acf_5": 0.3736883165873078,
        "abs_return_acf_20": 0.36489157695775437,
        "quantile_01": -0.08525521816097588,
        "quantile_99": 0.07030299807832685,
        "hill_tail_index": 3.0336728589362107
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020128590419134708,
        "excess_kurtosis": 6.613967030356177,
        "return_acf_1": -0.12780974621617888,
        "abs_return_acf_1": 0.37614671742610933,
        "abs_return_acf_5": 0.3645661160898462,
        "abs_return_acf_20": 0.28822898243075645,
        "quantile_01": -0.06067110755792747,
        "quantile_99": 0.06667008595913455,
        "hill_tail_index": 2.9854893507185487
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023644623982662247,
        "excess_kurtosis": 9.129736253253487,
        "return_acf_1": -0.1960377665188505,
        "abs_return_acf_1": 0.3878887725605262,
        "abs_return_acf_5": 0.3439877491785584,
        "abs_return_acf_20": 0.3489013903476974,
        "quantile_01": -0.08766400063348663,
        "quantile_99": 0.06685930055077807,
        "hill_tail_index": 3.3977503242904836
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020590809395132918,
        "excess_kurtosis": 7.272313242930059,
        "return_acf_1": -0.14965537253419908,
        "abs_return_acf_1": 0.3972611349858225,
        "abs_return_acf_5": 0.37244619631455933,
        "abs_return_acf_20": 0.3291276188985488,
        "quantile_01": -0.0640339697859514,
        "quantile_99": 0.06593789341951425,
        "hill_tail_index": 3.6340963552569896
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02097408873961079,
        "excess_kurtosis": 5.6997792533619265,
        "return_acf_1": -0.20845121978721062,
        "abs_return_acf_1": 0.3725247380672854,
        "abs_return_acf_5": 0.3201889852164009,
        "abs_return_acf_20": 0.3279593119809467,
        "quantile_01": -0.07396421495157847,
        "quantile_99": 0.06843858133967405,
        "hill_tail_index": 4.451469080474101
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020091709489692394,
        "excess_kurtosis": 6.4350971385631475,
        "return_acf_1": -0.11467772950805949,
        "abs_return_acf_1": 0.3363941868637677,
        "abs_return_acf_5": 0.30142827181700127,
        "abs_return_acf_20": 0.2810007484179824,
        "quantile_01": -0.06789388775178215,
        "quantile_99": 0.05850344507693957,
        "hill_tail_index": 3.8007073221371086
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
