# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27038
Run ID: `d6ddf1d160a10f3524c8199ab04a49fa15a015a2c6c08a1a1a0c176b66df5cb3`
Result fingerprint: `50f70d86c7cf1bf62eeb23b558069150185fc46b5074252d528bd35805aa8340`

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
    "equal_weight_sd": -0.6238332815129156,
    "equal_weight_raw": -9.357499222693734,
    "fixed_start_cap_weight_sd": -0.5719940885028559,
    "fixed_start_cap_weight_raw": -8.579911327542838,
    "end_cap_weight_sd": -0.5881804879107929,
    "end_cap_weight_raw": -8.822707318661896
  },
  "full_period_change": {
    "equal_weight_sd": -0.9862737577033902,
    "equal_weight_raw": -14.794106365550853
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.916491009089003,
    "inflation_mean_sd": 0.5621613756613757
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.31575000000000303,
    "equal_weight_raw": 4.736250000000045,
    "fixed_start_cap_weight_sd": 0.3772716531042768,
    "fixed_start_cap_weight_raw": 5.659074796564153,
    "end_cap_weight_sd": 0.36061520814869147,
    "end_cap_weight_raw": 5.409228122230373
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6040476190476158,
      "change_raw": -9.060714285714237,
      "decay_adjusted_gain_sd": 0.3483333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.520436507936505,
      "change_raw": -7.806547619047574,
      "decay_adjusted_gain_sd": 0.4319444444444474
    },
    "small": {
      "count": 18,
      "change_sd": -0.678829278712004,
      "change_raw": -10.18243918068006,
      "decay_adjusted_gain_sd": 0.25222222222222523
    },
    "large_minus_small_sd": 0.07478165966438821,
    "large_minus_small_raw": 1.1217248949658232
  },
  "inflation": {
    "initial_mean_sd": 0.21933333333333335,
    "final_mean_sd": 0.5913333333333333,
    "mean_sd": 0.43264474049403273,
    "mean_absolute_raw_gap": 6.489671107410492,
    "final_absolute_raw_gap": 8.87,
    "mean_range_fraction": 0.06489671107410491
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.18002891173580948,
    "final_wealth_share": 0.2763947760876373
  },
  "pricing_slope": {
    "mean": -0.00261434041942714,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.1648315313483361,
    "real_improvement_cost": 0.11384372504596971,
    "washing_cost": 0.05098780630236643,
    "fine_transfer": 0.040727763157074603,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.20555929450541072,
    "resource_cost_fraction_initial_cap": 0.005494384378277871,
    "private_net_outflow_fraction_initial_cap": 0.006851976483513691,
    "fine_transfer_fraction_initial_cap": 0.0013575921052358202,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0019206136053255083,
    "unapplied_final_day_resource_cost": 0.0017778384531320372
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 57.46776677080062,
    "beneficial_raw_gain_per_resource_cost": 862.0165015620094,
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
    "accrued_cost": 2.821745744846318,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.15444473134415834,
    "accrued_cost_fraction_initial_cap": 0.09405819149487728,
    "mean_contract_rate": 0.03903005767716077,
    "maximum_ledger_error": 1.2197274440461925e-19
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
    "maximum_relative_cash_error": 1.2368709911847647e-15,
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
      "minimum": -0.16900410702084265,
      "maximum": -0.01711165621217761,
      "mean": -0.09874098584422521,
      "median": -0.10748917496057622,
      "quantile_05": -0.16173928819619485,
      "quantile_95": -0.030118977179131774
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
      "minimum": 0.21201435194786133,
      "maximum": 0.7648258395476158,
      "mean": 0.4364690315772835,
      "median": 0.42310261646275743,
      "quantile_05": 0.2664607757007003,
      "quantile_95": 0.6872747116993094
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
        "daily_volatility": 0.018665224642596293,
        "excess_kurtosis": 6.827020306004158,
        "return_acf_1": -0.1564818929843625,
        "abs_return_acf_1": 0.3179066389024556,
        "abs_return_acf_5": 0.2688242320460008,
        "abs_return_acf_20": 0.21946888045851365,
        "quantile_01": -0.0600336588084189,
        "quantile_99": 0.051960857769552796,
        "hill_tail_index": 3.2021189326833266
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02091252938066418,
        "excess_kurtosis": 8.16418516998515,
        "return_acf_1": -0.1315522235200153,
        "abs_return_acf_1": 0.44107288039325,
        "abs_return_acf_5": 0.39507708502587485,
        "abs_return_acf_20": 0.3309273997095543,
        "quantile_01": -0.07468537288293214,
        "quantile_99": 0.060777854413934795,
        "hill_tail_index": 3.46286977042779
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01691006326297027,
        "excess_kurtosis": 2.6265375170703145,
        "return_acf_1": -0.1063544529880285,
        "abs_return_acf_1": 0.2648894534323093,
        "abs_return_acf_5": 0.2975376492930526,
        "abs_return_acf_20": 0.23904872112317055,
        "quantile_01": -0.05034462925402144,
        "quantile_99": 0.04341009221275829,
        "hill_tail_index": 4.250856099869572
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017719533047832726,
        "excess_kurtosis": 3.2517907682519755,
        "return_acf_1": -0.116609133989463,
        "abs_return_acf_1": 0.2818583412962712,
        "abs_return_acf_5": 0.32326797336834884,
        "abs_return_acf_20": 0.30425704118397584,
        "quantile_01": -0.057858209349750285,
        "quantile_99": 0.04626001268473998,
        "hill_tail_index": 3.7080942721802344
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02041774040919195,
        "excess_kurtosis": 8.338113112419784,
        "return_acf_1": -0.10862389693312395,
        "abs_return_acf_1": 0.3957397037790189,
        "abs_return_acf_5": 0.35892968292780153,
        "abs_return_acf_20": 0.32556232724027123,
        "quantile_01": -0.06683362729160859,
        "quantile_99": 0.06044698793122627,
        "hill_tail_index": 3.278407517189225
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01986964161209423,
        "excess_kurtosis": 10.010804565737642,
        "return_acf_1": -0.09359019785374051,
        "abs_return_acf_1": 0.342053637072185,
        "abs_return_acf_5": 0.3758215980915478,
        "abs_return_acf_20": 0.28804995953569656,
        "quantile_01": -0.06441631681221258,
        "quantile_99": 0.05591199613269308,
        "hill_tail_index": 2.7833494662157876
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017664797211998002,
        "excess_kurtosis": 5.434040002410365,
        "return_acf_1": -0.12972531122649988,
        "abs_return_acf_1": 0.28592047487203187,
        "abs_return_acf_5": 0.2844740326434047,
        "abs_return_acf_20": 0.31267296917036885,
        "quantile_01": -0.058624728945932895,
        "quantile_99": 0.04541565630679763,
        "hill_tail_index": 3.2718241265479087
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01850786312363543,
        "excess_kurtosis": 6.33219987550255,
        "return_acf_1": -0.13752385758019778,
        "abs_return_acf_1": 0.26281447610278524,
        "abs_return_acf_5": 0.3251454003209434,
        "abs_return_acf_20": 0.23460318279634124,
        "quantile_01": -0.05855233361275411,
        "quantile_99": 0.05875194980147728,
        "hill_tail_index": 3.2827057471334196
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01650849165766153,
        "excess_kurtosis": 12.606777406397377,
        "return_acf_1": -0.11664979515880196,
        "abs_return_acf_1": 0.25114306035683315,
        "abs_return_acf_5": 0.27261584782049614,
        "abs_return_acf_20": 0.1847372985134651,
        "quantile_01": -0.045212149766849175,
        "quantile_99": 0.04311331667869805,
        "hill_tail_index": 2.817140713638863
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017781235878559364,
        "excess_kurtosis": 3.7946162587788335,
        "return_acf_1": -0.10331824101401378,
        "abs_return_acf_1": 0.27081566569411447,
        "abs_return_acf_5": 0.23481219755279895,
        "abs_return_acf_20": 0.2608963164414806,
        "quantile_01": -0.05166629868174188,
        "quantile_99": 0.044241761753462686,
        "hill_tail_index": 4.27365953967274
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019162710416552126,
        "excess_kurtosis": 7.936352018144895,
        "return_acf_1": -0.03246693562357549,
        "abs_return_acf_1": 0.3009423684393888,
        "abs_return_acf_5": 0.29794111024064257,
        "abs_return_acf_20": 0.3203487146157056,
        "quantile_01": -0.06035652062165334,
        "quantile_99": 0.04667196607519705,
        "hill_tail_index": 2.753666221488418
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021393490885864404,
        "excess_kurtosis": 12.748258973761555,
        "return_acf_1": -0.032449695041602486,
        "abs_return_acf_1": 0.3070271397759119,
        "abs_return_acf_5": 0.33116158557037373,
        "abs_return_acf_20": 0.3541248364234354,
        "quantile_01": -0.06384547740050402,
        "quantile_99": 0.05845038307810763,
        "hill_tail_index": 2.563021048421236
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017303502794135884,
        "excess_kurtosis": 3.6211689234138857,
        "return_acf_1": -0.06673679725907898,
        "abs_return_acf_1": 0.1932916676727426,
        "abs_return_acf_5": 0.19356270571691506,
        "abs_return_acf_20": 0.31274983430430575,
        "quantile_01": -0.05191580662520823,
        "quantile_99": 0.049149865708179155,
        "hill_tail_index": 4.773587644362832
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021300252198445325,
        "excess_kurtosis": 10.595270094636493,
        "return_acf_1": -0.07045301446453164,
        "abs_return_acf_1": 0.3536944902051654,
        "abs_return_acf_5": 0.3647846547743294,
        "abs_return_acf_20": 0.376009296453382,
        "quantile_01": -0.07492279416630065,
        "quantile_99": 0.06175561355154971,
        "hill_tail_index": 2.748186817835394
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01787209377660313,
        "excess_kurtosis": 5.79082501508352,
        "return_acf_1": -0.036638592426359806,
        "abs_return_acf_1": 0.24895950134619577,
        "abs_return_acf_5": 0.2707595833834776,
        "abs_return_acf_20": 0.32130463239591994,
        "quantile_01": -0.05624184168917173,
        "quantile_99": 0.0492927034979085,
        "hill_tail_index": 3.7426894386842466
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022859345338574245,
        "excess_kurtosis": 15.477567723564523,
        "return_acf_1": -0.16900410702084265,
        "abs_return_acf_1": 0.5029723991894983,
        "abs_return_acf_5": 0.34989499405894187,
        "abs_return_acf_20": 0.3656826421955021,
        "quantile_01": -0.076729386433227,
        "quantile_99": 0.06698346713429962,
        "hill_tail_index": 3.1675129627471144
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020189951895047506,
        "excess_kurtosis": 8.957403586485162,
        "return_acf_1": -0.028212026200746625,
        "abs_return_acf_1": 0.36191727642566796,
        "abs_return_acf_5": 0.33531407147563763,
        "abs_return_acf_20": 0.3818051270589143,
        "quantile_01": -0.06082057042107267,
        "quantile_99": 0.05542615930970024,
        "hill_tail_index": 3.014531516264244
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020929541530266854,
        "excess_kurtosis": 9.38352924832573,
        "return_acf_1": -0.1480912879748303,
        "abs_return_acf_1": 0.3633890869017292,
        "abs_return_acf_5": 0.375962223984688,
        "abs_return_acf_20": 0.3525494711662995,
        "quantile_01": -0.0753643278459814,
        "quantile_99": 0.0578513833109812,
        "hill_tail_index": 3.2511182275476918
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01655977226073344,
        "excess_kurtosis": 2.12647401431272,
        "return_acf_1": -0.09906340612649225,
        "abs_return_acf_1": 0.2643619632610697,
        "abs_return_acf_5": 0.18396876565910408,
        "abs_return_acf_20": 0.23534960804970836,
        "quantile_01": -0.04474254086244895,
        "quantile_99": 0.04232330969301462,
        "hill_tail_index": 4.484212519352142
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019673863044930375,
        "excess_kurtosis": 8.800020119260065,
        "return_acf_1": -0.11728542101097551,
        "abs_return_acf_1": 0.39442505934332217,
        "abs_return_acf_5": 0.38059114486579565,
        "abs_return_acf_20": 0.34705413087248843,
        "quantile_01": -0.06381763210117218,
        "quantile_99": 0.06638038918689391,
        "hill_tail_index": 3.3204421012888923
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01914376937096395,
        "excess_kurtosis": 9.026432097630243,
        "return_acf_1": -0.01711165621217761,
        "abs_return_acf_1": 0.3568379427027981,
        "abs_return_acf_5": 0.29793278334765894,
        "abs_return_acf_20": 0.28072010155811267,
        "quantile_01": -0.061566815034978364,
        "quantile_99": 0.05122158881604048,
        "hill_tail_index": 2.836781755813399
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018829545307213386,
        "excess_kurtosis": 8.333868608157585,
        "return_acf_1": -0.06176787776311838,
        "abs_return_acf_1": 0.2856536909244702,
        "abs_return_acf_5": 0.3206396728345293,
        "abs_return_acf_20": 0.33072916913449313,
        "quantile_01": -0.06552795589184159,
        "quantile_99": 0.05057801462529172,
        "hill_tail_index": 2.90608911761257
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019135984358327404,
        "excess_kurtosis": 5.089795383081668,
        "return_acf_1": -0.12098839728837282,
        "abs_return_acf_1": 0.3557990464300341,
        "abs_return_acf_5": 0.27702403211472637,
        "abs_return_acf_20": 0.22419876131488983,
        "quantile_01": -0.06243447039764224,
        "quantile_99": 0.055469730189190304,
        "hill_tail_index": 3.862646993961192
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0164937386023051,
        "excess_kurtosis": 5.420701905730896,
        "return_acf_1": -0.10038726861445413,
        "abs_return_acf_1": 0.35686101629131467,
        "abs_return_acf_5": 0.32443349927586856,
        "abs_return_acf_20": 0.23303745823450314,
        "quantile_01": -0.04758921693823736,
        "quantile_99": 0.045957914909254896,
        "hill_tail_index": 2.277650210903276
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020254902604419183,
        "excess_kurtosis": 6.777288612862522,
        "return_acf_1": -0.046018938078893235,
        "abs_return_acf_1": 0.3464417927047556,
        "abs_return_acf_5": 0.405742520879201,
        "abs_return_acf_20": 0.34396087451345936,
        "quantile_01": -0.0641136699804501,
        "quantile_99": 0.05748208642084852,
        "hill_tail_index": 3.9310791835265606
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020668759922348165,
        "excess_kurtosis": 8.983810124497117,
        "return_acf_1": -0.11527876526647268,
        "abs_return_acf_1": 0.3294060594517273,
        "abs_return_acf_5": 0.35719055187902804,
        "abs_return_acf_20": 0.3121282966866941,
        "quantile_01": -0.06780736372449803,
        "quantile_99": 0.05909328748990288,
        "hill_tail_index": 3.0239223375650983
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015908242027466934,
        "excess_kurtosis": 3.0194817979044766,
        "return_acf_1": -0.16604079336951222,
        "abs_return_acf_1": 0.29396153534833563,
        "abs_return_acf_5": 0.24286296612470862,
        "abs_return_acf_20": 0.19652635167739932,
        "quantile_01": -0.04337537146796961,
        "quantile_99": 0.0438777025109203,
        "hill_tail_index": 3.2991877599966006
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02197600500164102,
        "excess_kurtosis": 8.781398217783403,
        "return_acf_1": -0.11893678880157281,
        "abs_return_acf_1": 0.4707481318027466,
        "abs_return_acf_5": 0.3430317591713982,
        "abs_return_acf_20": 0.34389359219205057,
        "quantile_01": -0.07918011509584572,
        "quantile_99": 0.06720405187045642,
        "hill_tail_index": 3.414989155283204
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019313762554557044,
        "excess_kurtosis": 5.763773336159959,
        "return_acf_1": -0.06729841226765557,
        "abs_return_acf_1": 0.3512014974390373,
        "abs_return_acf_5": 0.3087013206133364,
        "abs_return_acf_20": 0.33768273869250365,
        "quantile_01": -0.06175519950862796,
        "quantile_99": 0.05761346328816426,
        "hill_tail_index": 3.750580461503171
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0171578017664864,
        "excess_kurtosis": 2.9564622122482973,
        "return_acf_1": -0.1475703912672439,
        "abs_return_acf_1": 0.27679394894286335,
        "abs_return_acf_5": 0.17722313357015282,
        "abs_return_acf_20": 0.23199626628294273,
        "quantile_01": -0.04962076465634489,
        "quantile_99": 0.047137158138885964,
        "hill_tail_index": 4.178978377513638
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
Unseen state share: 0.0011111111111111111
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
