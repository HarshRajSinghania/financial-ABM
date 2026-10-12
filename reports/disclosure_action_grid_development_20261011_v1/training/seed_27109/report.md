# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27109
Run ID: `c4728a41e651de3aeaa9bb233ff5ce86c40416596cbd3e88001cfcf8012199f9`
Result fingerprint: `a35b6cb788e7f6ba099e4a0a2b28f3b63d5b0780b9176adad17cb8d0da4fbed5`

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
    "equal_weight_sd": -0.6545186919246982,
    "equal_weight_raw": -9.817780378870474,
    "fixed_start_cap_weight_sd": -0.602822584311157,
    "fixed_start_cap_weight_raw": -9.042338764667354,
    "end_cap_weight_sd": -0.6022524724736318,
    "end_cap_weight_raw": -9.033787087104475
  },
  "full_period_change": {
    "equal_weight_sd": -1.0317091681151724,
    "equal_weight_raw": -15.475637521727586
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9958414432474484,
    "inflation_mean_sd": 0.542472552910053
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.28266666666666984,
    "equal_weight_raw": 4.240000000000046,
    "fixed_start_cap_weight_sd": 0.32852054046601503,
    "fixed_start_cap_weight_raw": 4.927808106990226,
    "end_cap_weight_sd": 0.332058698313811,
    "end_cap_weight_raw": 4.980880474707163
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5465476190476157,
      "change_raw": -8.198214285714236,
      "decay_adjusted_gain_sd": 0.4058333333333366
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5722845286378908,
      "change_raw": -8.584267929568362,
      "decay_adjusted_gain_sd": 0.3294444444444473
    },
    "small": {
      "count": 18,
      "change_sd": -0.7136309523809491,
      "change_raw": -10.704464285714236,
      "decay_adjusted_gain_sd": 0.23875000000000324
    },
    "large_minus_small_sd": 0.16708333333333336,
    "large_minus_small_raw": 2.5062500000000005
  },
  "inflation": {
    "initial_mean_sd": 0.3115833333333333,
    "final_mean_sd": 0.5705833333333333,
    "mean_sd": 0.4589666250346933,
    "mean_absolute_raw_gap": 6.8844993755204,
    "final_absolute_raw_gap": 8.55875,
    "mean_range_fraction": 0.06884499375520399
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.27789952467067053,
    "final_wealth_share": 0.3682051323392943
  },
  "pricing_slope": {
    "mean": -0.002715883707167871,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.8061391461570275,
    "real_improvement_cost": 0.7760020036718365,
    "washing_cost": 0.030137142485190775,
    "fine_transfer": 0.027728440663851966,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.8338675868208795,
    "resource_cost_fraction_initial_cap": 0.02687130487190091,
    "private_net_outflow_fraction_initial_cap": 0.027795586227362643,
    "fine_transfer_fraction_initial_cap": 0.000924281355461732,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.012557195879970832,
    "unapplied_final_day_resource_cost": 0.004512015229030103
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 10.51927578560771,
    "beneficial_raw_gain_per_resource_cost": 157.78913678411567,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 2.9265934691372513,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.04959700705322534,
    "accrued_cost_fraction_initial_cap": 0.09755311563790835,
    "mean_contract_rate": 0.04093032671639575,
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
    "maximum_relative_cash_error": 1.8618983274067204e-15,
    "maximum_absolute_share_error": 1.4432899320127035e-15,
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
      "minimum": -0.13756302044265276,
      "maximum": 0.07739406944925516,
      "mean": -0.06143907092993759,
      "median": -0.0731116775514617,
      "quantile_05": -0.13147009938693216,
      "quantile_95": 0.02012415520160966
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
      "minimum": 0.2565466523617166,
      "maximum": 0.762694622441354,
      "mean": 0.4559615685890324,
      "median": 0.428978909793914,
      "quantile_05": 0.2958896704071589,
      "quantile_95": 0.666634992587171
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
        "daily_volatility": 0.01800121235169641,
        "excess_kurtosis": 16.17296272748074,
        "return_acf_1": -0.13756302044265276,
        "abs_return_acf_1": 0.45269728954533983,
        "abs_return_acf_5": 0.4038740693585831,
        "abs_return_acf_20": 0.26930280899846387,
        "quantile_01": -0.05555514490830356,
        "quantile_99": 0.04742285757141034,
        "hill_tail_index": 2.018282953350599
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017094843982717507,
        "excess_kurtosis": 6.884587975524985,
        "return_acf_1": -0.009634035147966853,
        "abs_return_acf_1": 0.20698298395313974,
        "abs_return_acf_5": 0.22626350918243984,
        "abs_return_acf_20": 0.23848193418323543,
        "quantile_01": -0.04840955548277769,
        "quantile_99": 0.040811066956136975,
        "hill_tail_index": 3.085719382793781
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016858499914363646,
        "excess_kurtosis": 3.394688005114058,
        "return_acf_1": -0.09365369640850485,
        "abs_return_acf_1": 0.2843592718068228,
        "abs_return_acf_5": 0.2821902032130933,
        "abs_return_acf_20": 0.2255181707785743,
        "quantile_01": -0.05144509442649768,
        "quantile_99": 0.04123078117022074,
        "hill_tail_index": 3.408814820906516
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018865804210964787,
        "excess_kurtosis": 6.5609260661318185,
        "return_acf_1": -0.07740843735234086,
        "abs_return_acf_1": 0.3435537448550022,
        "abs_return_acf_5": 0.3775217092386027,
        "abs_return_acf_20": 0.2705394029054265,
        "quantile_01": -0.05893610183264894,
        "quantile_99": 0.057523498512751674,
        "hill_tail_index": 3.788826584830898
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018444677089528554,
        "excess_kurtosis": 5.402982531039319,
        "return_acf_1": -0.07336861171113757,
        "abs_return_acf_1": 0.23929838856501057,
        "abs_return_acf_5": 0.296276464661674,
        "abs_return_acf_20": 0.27967880266262557,
        "quantile_01": -0.060788540107830816,
        "quantile_99": 0.05527475303437907,
        "hill_tail_index": 4.711263688087259
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018366866417208486,
        "excess_kurtosis": 12.976254156841199,
        "return_acf_1": -0.00436628628050413,
        "abs_return_acf_1": 0.40550268129313305,
        "abs_return_acf_5": 0.2972896823250514,
        "abs_return_acf_20": 0.19671284306066933,
        "quantile_01": -0.05415098631482047,
        "quantile_99": 0.04484964916311518,
        "hill_tail_index": 2.2590076011940052
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018649836788499234,
        "excess_kurtosis": 5.342637578886849,
        "return_acf_1": -0.0633621357902313,
        "abs_return_acf_1": 0.3767755727586571,
        "abs_return_acf_5": 0.35627239261925103,
        "abs_return_acf_20": 0.28364916393918127,
        "quantile_01": -0.06094068259595661,
        "quantile_99": 0.05071695923660186,
        "hill_tail_index": 3.573631071339857
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01615352661836871,
        "excess_kurtosis": 4.504252249830476,
        "return_acf_1": -0.07823719476810224,
        "abs_return_acf_1": 0.20634161259818165,
        "abs_return_acf_5": 0.2606088114977737,
        "abs_return_acf_20": 0.19929488218399316,
        "quantile_01": -0.0463937972666541,
        "quantile_99": 0.04401190901141228,
        "hill_tail_index": 3.397845446121322
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01828684156722027,
        "excess_kurtosis": 3.2916226965439597,
        "return_acf_1": -0.12902892538118546,
        "abs_return_acf_1": 0.23879114550587277,
        "abs_return_acf_5": 0.30128371453390174,
        "abs_return_acf_20": 0.3064618604703047,
        "quantile_01": -0.05436488460911152,
        "quantile_99": 0.05049361193846174,
        "hill_tail_index": 4.739118703236522
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019130773888281827,
        "excess_kurtosis": 35.432118909001645,
        "return_acf_1": -0.04805576781612578,
        "abs_return_acf_1": 0.3355970203831234,
        "abs_return_acf_5": 0.32544855072888595,
        "abs_return_acf_20": 0.12611532503438355,
        "quantile_01": -0.058717291352234975,
        "quantile_99": 0.05581709455708714,
        "hill_tail_index": 2.2686480406516125
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017100707738406544,
        "excess_kurtosis": 11.565051448658773,
        "return_acf_1": -0.027865665126939804,
        "abs_return_acf_1": 0.365179651664672,
        "abs_return_acf_5": 0.30390693309511513,
        "abs_return_acf_20": 0.25004602583750046,
        "quantile_01": -0.048139015970517625,
        "quantile_99": 0.0476037334323397,
        "hill_tail_index": 2.569114727464515
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018012028562030744,
        "excess_kurtosis": 4.392000650779207,
        "return_acf_1": 0.012610788141959699,
        "abs_return_acf_1": 0.29265284542177816,
        "abs_return_acf_5": 0.22894252772046858,
        "abs_return_acf_20": 0.2356123155748317,
        "quantile_01": -0.0556806703471245,
        "quantile_99": 0.04713364748299033,
        "hill_tail_index": 4.087593705200911
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016622603109661016,
        "excess_kurtosis": 4.084521335862422,
        "return_acf_1": -0.13346742357345218,
        "abs_return_acf_1": 0.238656848667683,
        "abs_return_acf_5": 0.22585418508982327,
        "abs_return_acf_20": 0.19558654387801805,
        "quantile_01": -0.048178107492953245,
        "quantile_99": 0.04672840618151779,
        "hill_tail_index": 3.624581544488159
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018694083871667426,
        "excess_kurtosis": 23.62697275797325,
        "return_acf_1": -0.07731538653809657,
        "abs_return_acf_1": 0.3911254346512826,
        "abs_return_acf_5": 0.3450700882075165,
        "abs_return_acf_20": 0.26592207213263697,
        "quantile_01": -0.06082665169529805,
        "quantile_99": 0.04542197878730738,
        "hill_tail_index": 1.9965826620733476
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015465782013360964,
        "excess_kurtosis": 3.329830081086472,
        "return_acf_1": -0.0696386234920506,
        "abs_return_acf_1": 0.21989259292404972,
        "abs_return_acf_5": 0.14782951006283812,
        "abs_return_acf_20": 0.157559569718024,
        "quantile_01": -0.04140361311863779,
        "quantile_99": 0.038752583022443124,
        "hill_tail_index": 3.739976117250977
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016778188102665226,
        "excess_kurtosis": 5.859838540693191,
        "return_acf_1": -0.05292484005421258,
        "abs_return_acf_1": 0.3316732448521266,
        "abs_return_acf_5": 0.3372823703226756,
        "abs_return_acf_20": 0.27381066752143085,
        "quantile_01": -0.053354909701089435,
        "quantile_99": 0.04036935475335636,
        "hill_tail_index": 2.604060202917729
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018471896153592023,
        "excess_kurtosis": 26.13976315041292,
        "return_acf_1": -0.02749580088493824,
        "abs_return_acf_1": 0.48375499113882897,
        "abs_return_acf_5": 0.3792276574102577,
        "abs_return_acf_20": 0.2735567172171148,
        "quantile_01": -0.05828424089773709,
        "quantile_99": 0.04203412857107789,
        "hill_tail_index": 1.7634386730473206
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01626474443323224,
        "excess_kurtosis": 6.224490223670154,
        "return_acf_1": -0.10779584228085888,
        "abs_return_acf_1": 0.2961411536636033,
        "abs_return_acf_5": 0.33013808949182943,
        "abs_return_acf_20": 0.21253160647031596,
        "quantile_01": -0.04946090758033685,
        "quantile_99": 0.04181161937851343,
        "hill_tail_index": 2.735464190789928
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01721126102234279,
        "excess_kurtosis": 3.5364633059207424,
        "return_acf_1": -0.09715422450089718,
        "abs_return_acf_1": 0.22225183691003655,
        "abs_return_acf_5": 0.2882222451843033,
        "abs_return_acf_20": 0.23837695226586922,
        "quantile_01": -0.051989719229961866,
        "quantile_99": 0.04932575359165535,
        "hill_tail_index": 4.495921094066722
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.015564119039494954,
        "excess_kurtosis": 5.824842526729951,
        "return_acf_1": -0.11134008873351312,
        "abs_return_acf_1": 0.24984492087567975,
        "abs_return_acf_5": 0.211268946636528,
        "abs_return_acf_20": 0.1366378266023525,
        "quantile_01": -0.04083695840970219,
        "quantile_99": 0.03688500461252596,
        "hill_tail_index": 3.0246959730552034
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01785419544974,
        "excess_kurtosis": 17.583637747842804,
        "return_acf_1": -0.1131830243704944,
        "abs_return_acf_1": 0.3822302136740722,
        "abs_return_acf_5": 0.4035334799754528,
        "abs_return_acf_20": 0.256393003937175,
        "quantile_01": -0.058765072068851336,
        "quantile_99": 0.040068094805207316,
        "hill_tail_index": 1.965873360220743
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016001201723218,
        "excess_kurtosis": 3.916833077434923,
        "return_acf_1": -0.07285474339178581,
        "abs_return_acf_1": 0.2848107808188041,
        "abs_return_acf_5": 0.2164544008274696,
        "abs_return_acf_20": 0.19683896488819716,
        "quantile_01": -0.04975836352768232,
        "quantile_99": 0.037032222640374625,
        "hill_tail_index": 4.185120322864934
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.0166305229078805,
        "excess_kurtosis": 16.272688411440278,
        "return_acf_1": 0.013581177200963667,
        "abs_return_acf_1": 0.26354995971404327,
        "abs_return_acf_5": 0.32535935391073195,
        "abs_return_acf_20": 0.18315043959993196,
        "quantile_01": -0.04479919143117761,
        "quantile_99": 0.037544757510855016,
        "hill_tail_index": 2.2088550068759396
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01839323173444631,
        "excess_kurtosis": 16.037251264665667,
        "return_acf_1": -0.08645968057435327,
        "abs_return_acf_1": 0.3993955148514943,
        "abs_return_acf_5": 0.4044399332872725,
        "abs_return_acf_20": 0.30411179653641496,
        "quantile_01": -0.06488045962684758,
        "quantile_99": 0.0460553376503434,
        "hill_tail_index": 2.134916276737447
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017640161187831543,
        "excess_kurtosis": 7.098743500798783,
        "return_acf_1": 0.025477500838501897,
        "abs_return_acf_1": 0.26689290137237764,
        "abs_return_acf_5": 0.2329886449689248,
        "abs_return_acf_20": 0.22997187053698948,
        "quantile_01": -0.054903725496587064,
        "quantile_99": 0.04168977929676089,
        "hill_tail_index": 3.2590563792859712
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016403260686329652,
        "excess_kurtosis": 4.944058452217725,
        "return_acf_1": -0.05894637795292302,
        "abs_return_acf_1": 0.28278274379690493,
        "abs_return_acf_5": 0.17299025561043743,
        "abs_return_acf_20": 0.18691098895424235,
        "quantile_01": -0.04885610962571086,
        "quantile_99": 0.04548066738060477,
        "hill_tail_index": 3.2797824327282012
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017557839247442718,
        "excess_kurtosis": 8.383366363229685,
        "return_acf_1": 0.07739406944925516,
        "abs_return_acf_1": 0.3694732494214351,
        "abs_return_acf_5": 0.2617236967556301,
        "abs_return_acf_20": 0.21046237874452614,
        "quantile_01": -0.05219193343387414,
        "quantile_99": 0.04357987168477023,
        "hill_tail_index": 3.111000360663783
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.015613931861570987,
        "excess_kurtosis": 4.370395104049994,
        "return_acf_1": -0.12839111232699,
        "abs_return_acf_1": 0.32412746509163476,
        "abs_return_acf_5": 0.2510033625790546,
        "abs_return_acf_20": 0.19264206946544293,
        "quantile_01": -0.05241388654496701,
        "quantile_99": 0.040816789945271534,
        "hill_tail_index": 3.3593137223789884
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01603849033231441,
        "excess_kurtosis": 3.1362206586640626,
        "return_acf_1": -0.09820524111136342,
        "abs_return_acf_1": 0.25036347306888856,
        "abs_return_acf_5": 0.21918399207304873,
        "abs_return_acf_20": 0.1443695549986302,
        "quantile_01": -0.04571140587306297,
        "quantile_99": 0.047302402158200384,
        "hill_tail_index": 4.410647839144326
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019765737037350555,
        "excess_kurtosis": 15.8187898544717,
        "return_acf_1": 0.005480522482812951,
        "abs_return_acf_1": 0.4558183125624079,
        "abs_return_acf_5": 0.356000730786774,
        "abs_return_acf_20": 0.2435361992611913,
        "quantile_01": -0.05538535562849385,
        "quantile_99": 0.05082211839049345,
        "hill_tail_index": 2.1721858398361533
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
