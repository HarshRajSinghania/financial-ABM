# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27199
Run ID: `4c6a0b2207eade13b54cebef0b6b4911ff54d283885f0a78ae55446895fd66e7`
Result fingerprint: `4247c62c40b6f69b809c7090e895fba3bf5f931520b44a52c26ca91b23555ce0`

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
    "equal_weight_sd": -0.7235469452302523,
    "equal_weight_raw": -10.853204178453783,
    "fixed_start_cap_weight_sd": -0.7051262319898931,
    "fixed_start_cap_weight_raw": -10.576893479848401,
    "end_cap_weight_sd": -0.6977854432426791,
    "end_cap_weight_raw": -10.466781648640186
  },
  "full_period_change": {
    "equal_weight_sd": -1.1389978091771018,
    "equal_weight_raw": -17.084967137656527
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0751942377485304,
    "inflation_mean_sd": 0.4709341931216931
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.17350000000000293,
    "equal_weight_raw": 2.602500000000044,
    "fixed_start_cap_weight_sd": 0.23437667257894002,
    "fixed_start_cap_weight_raw": 3.515650088684102,
    "end_cap_weight_sd": 0.24442483550235386,
    "end_cap_weight_raw": 3.6663725325353083
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.716547619047616,
      "change_raw": -10.74821428571424,
      "decay_adjusted_gain_sd": 0.23583333333333634
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7771031746031714,
      "change_raw": -11.65654761904757,
      "decay_adjusted_gain_sd": 0.17527777777778086
    },
    "small": {
      "count": 18,
      "change_sd": -0.6979353849075657,
      "change_raw": -10.469030773613484,
      "decay_adjusted_gain_sd": 0.16222222222222504
    },
    "large_minus_small_sd": -0.01861223414005031,
    "large_minus_small_raw": -0.27918351210075465
  },
  "inflation": {
    "initial_mean_sd": 0.29833333333333345,
    "final_mean_sd": 0.48624999999999996,
    "mean_sd": 0.41425444074382456,
    "mean_absolute_raw_gap": 6.213816611157369,
    "final_absolute_raw_gap": 7.29375,
    "mean_range_fraction": 0.06213816611157369
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.23333333333333334,
    "initial_wealth_share": 0.20738891432856627,
    "final_wealth_share": 0.23861912722146622
  },
  "pricing_slope": {
    "mean": 0.0002839683222908912,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.01919518522062867,
    "real_improvement_cost": 0.015357402470978963,
    "washing_cost": 0.0038377827496497096,
    "fine_transfer": 0.011793700026261332,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.030988885246890002,
    "resource_cost_fraction_initial_cap": 0.000639839507354289,
    "private_net_outflow_fraction_initial_cap": 0.0010329628415630002,
    "fine_transfer_fraction_initial_cap": 0.0003931233342087111,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00013321920658896093,
    "unapplied_final_day_resource_cost": 0.0002595247603191248
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 271.1617491664723,
    "beneficial_raw_gain_per_resource_cost": 4067.4262374970845,
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
    "accrued_cost": 2.749551221539691,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.22663925465078605,
    "accrued_cost_fraction_initial_cap": 0.09165170738465636,
    "mean_contract_rate": 0.03874793967305735,
    "maximum_ledger_error": 4.2351647362715017e-20
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
    "maximum_relative_cash_error": 1.8838690824112766e-15,
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
      "minimum": -0.251757203625724,
      "maximum": -0.07282513898571641,
      "mean": -0.1512346334842255,
      "median": -0.14963035856309437,
      "quantile_05": -0.2345167876781742,
      "quantile_95": -0.07731476815393007
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
      "minimum": 0.24571481338887682,
      "maximum": 0.8322515623677933,
      "mean": 0.5091222428449367,
      "median": 0.5021248904018831,
      "quantile_05": 0.2959469761333441,
      "quantile_95": 0.7823242874251275
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
        "daily_volatility": 0.02040954152660874,
        "excess_kurtosis": 17.990041045812436,
        "return_acf_1": -0.1145292311186985,
        "abs_return_acf_1": 0.33185399076442795,
        "abs_return_acf_5": 0.3471522891587718,
        "abs_return_acf_20": 0.25304495306519736,
        "quantile_01": -0.060650702085627735,
        "quantile_99": 0.04829086144385614,
        "hill_tail_index": 2.067713768330301
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02324357043995131,
        "excess_kurtosis": 17.224867095046058,
        "return_acf_1": -0.13673325417971227,
        "abs_return_acf_1": 0.49247571716505323,
        "abs_return_acf_5": 0.4365780076359848,
        "abs_return_acf_20": 0.3052939851104256,
        "quantile_01": -0.08288907985169898,
        "quantile_99": 0.0642708592062421,
        "hill_tail_index": 2.463470771974413
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020385602071517045,
        "excess_kurtosis": 11.637361584457924,
        "return_acf_1": -0.07945158280913378,
        "abs_return_acf_1": 0.3018777985892868,
        "abs_return_acf_5": 0.3092359330693548,
        "abs_return_acf_20": 0.29080346244671357,
        "quantile_01": -0.05977509379456117,
        "quantile_99": 0.05235726153527439,
        "hill_tail_index": 2.4824408077537115
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022173911879714747,
        "excess_kurtosis": 22.141302756842535,
        "return_acf_1": -0.15106208378689978,
        "abs_return_acf_1": 0.4031879903347785,
        "abs_return_acf_5": 0.4105080170076091,
        "abs_return_acf_20": 0.2938083606031772,
        "quantile_01": -0.07379111968509608,
        "quantile_99": 0.06117278696953508,
        "hill_tail_index": 2.3629341603826166
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021430928080740243,
        "excess_kurtosis": 14.888414120842608,
        "return_acf_1": -0.14589955036712945,
        "abs_return_acf_1": 0.3457625259127724,
        "abs_return_acf_5": 0.31283881267473024,
        "abs_return_acf_20": 0.3310402301831118,
        "quantile_01": -0.06335541550707127,
        "quantile_99": 0.0561881360565327,
        "hill_tail_index": 2.430620912697196
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01881816711121013,
        "excess_kurtosis": 6.44357935197387,
        "return_acf_1": -0.1911108038777648,
        "abs_return_acf_1": 0.3386343292625221,
        "abs_return_acf_5": 0.2890674814377771,
        "abs_return_acf_20": 0.22527456371628166,
        "quantile_01": -0.05407981532091124,
        "quantile_99": 0.050433859960482275,
        "hill_tail_index": 3.1624866069875193
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0242004872710381,
        "excess_kurtosis": 19.122005487560514,
        "return_acf_1": -0.1790664956830362,
        "abs_return_acf_1": 0.49329519993047255,
        "abs_return_acf_5": 0.5134789385499385,
        "abs_return_acf_20": 0.3622378924851144,
        "quantile_01": -0.08807112042688847,
        "quantile_99": 0.0699824481387554,
        "hill_tail_index": 2.5570364979642592
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01968247882746096,
        "excess_kurtosis": 7.160086384080936,
        "return_acf_1": -0.13409025445125283,
        "abs_return_acf_1": 0.38992650845100574,
        "abs_return_acf_5": 0.3120642480273942,
        "abs_return_acf_20": 0.2565078108399178,
        "quantile_01": -0.05719104578234425,
        "quantile_99": 0.05400251989353318,
        "hill_tail_index": 3.488794323622532
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02122698853197696,
        "excess_kurtosis": 7.103673279955082,
        "return_acf_1": -0.16838870237974693,
        "abs_return_acf_1": 0.3712338898565855,
        "abs_return_acf_5": 0.2871732418388129,
        "abs_return_acf_20": 0.3207549225765271,
        "quantile_01": -0.059808025774199344,
        "quantile_99": 0.059231351562573926,
        "hill_tail_index": 3.4175708076454554
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021165046028415922,
        "excess_kurtosis": 10.607349711137758,
        "return_acf_1": -0.07282513898571641,
        "abs_return_acf_1": 0.3681074651033022,
        "abs_return_acf_5": 0.4580041113862542,
        "abs_return_acf_20": 0.3776649762220848,
        "quantile_01": -0.07746182278657934,
        "quantile_99": 0.055049212664126636,
        "hill_tail_index": 2.1745243900373064
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01948874567248922,
        "excess_kurtosis": 8.46700959724318,
        "return_acf_1": -0.15167034529668824,
        "abs_return_acf_1": 0.364012532699981,
        "abs_return_acf_5": 0.33297806903534893,
        "abs_return_acf_20": 0.324150369551765,
        "quantile_01": -0.06718746629008047,
        "quantile_99": 0.05700326146083163,
        "hill_tail_index": 2.699079055694214
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.0203054840047242,
        "excess_kurtosis": 17.468600854256866,
        "return_acf_1": -0.07556646525421792,
        "abs_return_acf_1": 0.42524768736578344,
        "abs_return_acf_5": 0.3864532280284535,
        "abs_return_acf_20": 0.2009911555761864,
        "quantile_01": -0.06382303089646674,
        "quantile_99": 0.058051671466055894,
        "hill_tail_index": 2.343797787236159
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024289954268505255,
        "excess_kurtosis": 16.654010159312758,
        "return_acf_1": -0.14712223138158823,
        "abs_return_acf_1": 0.5334558277028334,
        "abs_return_acf_5": 0.5271608714270535,
        "abs_return_acf_20": 0.3015283565834694,
        "quantile_01": -0.09437704399252704,
        "quantile_99": 0.07240541132577027,
        "hill_tail_index": 2.3989139821425476
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019668685798672543,
        "excess_kurtosis": 5.340297491334031,
        "return_acf_1": -0.16079594469603226,
        "abs_return_acf_1": 0.3137882521451696,
        "abs_return_acf_5": 0.24260128119899563,
        "abs_return_acf_20": 0.24373823572574102,
        "quantile_01": -0.061412371399973326,
        "quantile_99": 0.05776832000256801,
        "hill_tail_index": 4.379149466502107
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02189360310764246,
        "excess_kurtosis": 12.175742005297355,
        "return_acf_1": -0.23749352530003046,
        "abs_return_acf_1": 0.45932187984629697,
        "abs_return_acf_5": 0.3851431345892095,
        "abs_return_acf_20": 0.3827502203517724,
        "quantile_01": -0.07537482708982231,
        "quantile_99": 0.059400257688438436,
        "hill_tail_index": 3.2005585902186056
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02040831076740613,
        "excess_kurtosis": 11.551466597490386,
        "return_acf_1": -0.18589072141452073,
        "abs_return_acf_1": 0.3835877732313093,
        "abs_return_acf_5": 0.36966954740379254,
        "abs_return_acf_20": 0.3080952070270277,
        "quantile_01": -0.06501405636806397,
        "quantile_99": 0.056070453638197085,
        "hill_tail_index": 2.743977873932447
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01843931495420759,
        "excess_kurtosis": 7.71309176072773,
        "return_acf_1": -0.1332876242084559,
        "abs_return_acf_1": 0.3531061591222614,
        "abs_return_acf_5": 0.3208968619396238,
        "abs_return_acf_20": 0.15737860855714425,
        "quantile_01": -0.053999238691140566,
        "quantile_99": 0.05135796489621761,
        "hill_tail_index": 2.3938522469745402
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018555487134713368,
        "excess_kurtosis": 4.544805579727302,
        "return_acf_1": -0.10708867247400182,
        "abs_return_acf_1": 0.26112180542573366,
        "abs_return_acf_5": 0.35815114868353104,
        "abs_return_acf_20": 0.27378244460450074,
        "quantile_01": -0.05058647336305338,
        "quantile_99": 0.053860049897407364,
        "hill_tail_index": 3.345484219740595
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.0203825436086266,
        "excess_kurtosis": 9.164896729321667,
        "return_acf_1": -0.142145565917304,
        "abs_return_acf_1": 0.4170316552567378,
        "abs_return_acf_5": 0.3887660119529534,
        "abs_return_acf_20": 0.2981516720822858,
        "quantile_01": -0.06970617676949323,
        "quantile_99": 0.05925129759177041,
        "hill_tail_index": 3.2213343792561213
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022961933875316396,
        "excess_kurtosis": 13.40048920568059,
        "return_acf_1": -0.23087855280701655,
        "abs_return_acf_1": 0.4911683831025238,
        "abs_return_acf_5": 0.46532651368513284,
        "abs_return_acf_20": 0.39915464033753817,
        "quantile_01": -0.07787816231076453,
        "quantile_99": 0.06423395368038003,
        "hill_tail_index": 2.547283368664361
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.024227943232284384,
        "excess_kurtosis": 13.783640930628348,
        "return_acf_1": -0.251757203625724,
        "abs_return_acf_1": 0.47404306663316775,
        "abs_return_acf_5": 0.450708609535737,
        "abs_return_acf_20": 0.3683598718334847,
        "quantile_01": -0.09020818592819262,
        "quantile_99": 0.08115189488420471,
        "hill_tail_index": 3.381279295321461
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021807765792644224,
        "excess_kurtosis": 10.110144724256394,
        "return_acf_1": -0.15722975323491956,
        "abs_return_acf_1": 0.44482143106949035,
        "abs_return_acf_5": 0.46645050408924155,
        "abs_return_acf_20": 0.33403400783012144,
        "quantile_01": -0.07247736325500617,
        "quantile_99": 0.06305274576712391,
        "hill_tail_index": 3.674851228845783
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018834955915786447,
        "excess_kurtosis": 7.537497718375613,
        "return_acf_1": -0.09514653842970003,
        "abs_return_acf_1": 0.3384331333492328,
        "abs_return_acf_5": 0.3527747802364284,
        "abs_return_acf_20": 0.23351402036558863,
        "quantile_01": -0.05265080800851992,
        "quantile_99": 0.052249486326411264,
        "hill_tail_index": 3.0645755147452083
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021868176617802892,
        "excess_kurtosis": 12.724866345971195,
        "return_acf_1": -0.15649929552708824,
        "abs_return_acf_1": 0.49234159098643565,
        "abs_return_acf_5": 0.5195488262173789,
        "abs_return_acf_20": 0.42537658286274094,
        "quantile_01": -0.07635652552830756,
        "quantile_99": 0.0575181441958332,
        "hill_tail_index": 2.7020565535978505
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021170223368775373,
        "excess_kurtosis": 16.02355390261973,
        "return_acf_1": -0.14819863333928893,
        "abs_return_acf_1": 0.42936550587260003,
        "abs_return_acf_5": 0.42539287264173664,
        "abs_return_acf_20": 0.232534450158569,
        "quantile_01": -0.07164395973816892,
        "quantile_99": 0.05841318281511911,
        "hill_tail_index": 2.25908812263304
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01914220446254392,
        "excess_kurtosis": 6.256077788495533,
        "return_acf_1": -0.19014338358625962,
        "abs_return_acf_1": 0.3446678498720002,
        "abs_return_acf_5": 0.35003507048835003,
        "abs_return_acf_20": 0.32848288018779653,
        "quantile_01": -0.048367847038606894,
        "quantile_99": 0.05961076463048212,
        "hill_tail_index": 2.596172186774223
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020991372797911183,
        "excess_kurtosis": 5.162095155441785,
        "return_acf_1": -0.14118660667820487,
        "abs_return_acf_1": 0.4130721816998907,
        "abs_return_acf_5": 0.3796773374538354,
        "abs_return_acf_20": 0.27373375415253426,
        "quantile_01": -0.06890263866677321,
        "quantile_99": 0.06144270508100128,
        "hill_tail_index": 4.240835797258361
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019528094292067016,
        "excess_kurtosis": 3.690792347622412,
        "return_acf_1": -0.12114377069340225,
        "abs_return_acf_1": 0.35889652618372997,
        "abs_return_acf_5": 0.2547622687805789,
        "abs_return_acf_20": 0.2261891155855148,
        "quantile_01": -0.057519876032954734,
        "quantile_99": 0.05486370013526145,
        "hill_tail_index": 3.933951426110581
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021638195863670277,
        "excess_kurtosis": 8.639320230554812,
        "return_acf_1": -0.17500532082691714,
        "abs_return_acf_1": 0.438182504457303,
        "abs_return_acf_5": 0.42243542044737126,
        "abs_return_acf_20": 0.3820583371542522,
        "quantile_01": -0.0754430579496431,
        "quantile_99": 0.06524841887125837,
        "hill_tail_index": 3.233155506415718
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022937200847027522,
        "excess_kurtosis": 14.649388517103375,
        "return_acf_1": -0.15563175219631298,
        "abs_return_acf_1": 0.4387563720983186,
        "abs_return_acf_5": 0.4405005680648479,
        "abs_return_acf_20": 0.33148319624059164,
        "quantile_01": -0.076453646726064,
        "quantile_99": 0.07250308221856062,
        "hill_tail_index": 2.9371427579294003
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
