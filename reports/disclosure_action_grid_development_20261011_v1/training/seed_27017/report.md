# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27017
Run ID: `d17042d0c3b2f2729e8a377d29d470d9ed1fb869fed6fb4d747070928f4de21a`
Result fingerprint: `fc5e6df53892060cbe05bc4f042566a440db38e7fa25623e478c69994ded7b70`

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
    "equal_weight_sd": -0.41488095238094913,
    "equal_weight_raw": -6.223214285714238,
    "fixed_start_cap_weight_sd": -0.384253104264894,
    "fixed_start_cap_weight_raw": -5.76379656397341,
    "end_cap_weight_sd": -0.3985640735021582,
    "end_cap_weight_raw": -5.978461102532372
  },
  "full_period_change": {
    "equal_weight_sd": -0.7680714285714237,
    "equal_weight_raw": -11.521071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7330952380952336,
    "inflation_mean_sd": 0.6118141534391535
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5175396876296241,
    "equal_weight_raw": 7.763095314444361,
    "fixed_start_cap_weight_sd": 0.5647798206725255,
    "fixed_start_cap_weight_raw": 8.471697310087885,
    "end_cap_weight_sd": 0.5520592596046806,
    "end_cap_weight_raw": 8.28088889407021
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.25738095238094916,
      "change_raw": -3.8607142857142374,
      "decay_adjusted_gain_sd": 0.6950000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.3968253968253936,
      "change_raw": -5.952380952380904,
      "decay_adjusted_gain_sd": 0.5555555555555587
    },
    "small": {
      "count": 18,
      "change_sd": -0.4501587301587269,
      "change_raw": -6.7523809523809035,
      "decay_adjusted_gain_sd": 0.4689550349382603
    },
    "large_minus_small_sd": 0.19277777777777777,
    "large_minus_small_raw": 2.8916666666666666
  },
  "inflation": {
    "initial_mean_sd": 0.22391666666666665,
    "final_mean_sd": 0.6631666666666668,
    "mean_sd": 0.44043560921454344,
    "mean_absolute_raw_gap": 6.6065341382181515,
    "final_absolute_raw_gap": 9.9475,
    "mean_range_fraction": 0.06606534138218151
  },
  "impact": {
    "initial_share": 0.34,
    "final_share": 0.46,
    "initial_wealth_share": 0.25807103811252347,
    "final_wealth_share": 0.4131544021099217
  },
  "pricing_slope": {
    "mean": -0.0021587668163024027,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.10600465500396011,
    "real_improvement_cost": 0.09012265612014046,
    "washing_cost": 0.015881998883819665,
    "fine_transfer": 0.020692548943327647,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12669720394728776,
    "resource_cost_fraction_initial_cap": 0.003533488500132003,
    "private_net_outflow_fraction_initial_cap": 0.004223240131576257,
    "fine_transfer_fraction_initial_cap": 0.0006897516314442547,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00913851596043993,
    "unapplied_final_day_resource_cost": 0.0043710625441150085
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 146.46706437852845,
    "beneficial_raw_gain_per_resource_cost": 2197.0059656779267,
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
    "accrued_cost": 3.0227261258554075,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.04653564966493019,
    "accrued_cost_fraction_initial_cap": 0.10075753752851356,
    "mean_contract_rate": 0.042758039658618484,
    "maximum_ledger_error": 7.030373462210693e-20
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
    "maximum_relative_cash_error": 1.625612060980843e-15,
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
      "minimum": -0.24915166969725822,
      "maximum": -0.02179833449633241,
      "mean": -0.1755253509676356,
      "median": -0.1899924280162401,
      "quantile_05": -0.23760833987706775,
      "quantile_95": -0.04371337231782675
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
      "minimum": 0.1936721506928513,
      "maximum": 0.8446397808580037,
      "mean": 0.6046910777296497,
      "median": 0.71106724017828,
      "quantile_05": 0.22981561161300096,
      "quantile_95": 0.8197766108314555
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
        "daily_volatility": 0.024734607675063025,
        "excess_kurtosis": 18.33052377606436,
        "return_acf_1": -0.1728837326638163,
        "abs_return_acf_1": 0.38367461152627835,
        "abs_return_acf_5": 0.43551533782056434,
        "abs_return_acf_20": 0.3458762834119277,
        "quantile_01": -0.07771901732834266,
        "quantile_99": 0.0637757804740896,
        "hill_tail_index": 2.521196119898097
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02463901990365037,
        "excess_kurtosis": 11.319533394052499,
        "return_acf_1": -0.22866607709661163,
        "abs_return_acf_1": 0.46796120641751204,
        "abs_return_acf_5": 0.4556863772609954,
        "abs_return_acf_20": 0.3589782251316986,
        "quantile_01": -0.07882424333346194,
        "quantile_99": 0.06958383929056638,
        "hill_tail_index": 2.7505721025554437
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023981432596528428,
        "excess_kurtosis": 15.735089806103659,
        "return_acf_1": -0.24492473669744094,
        "abs_return_acf_1": 0.4936578105138802,
        "abs_return_acf_5": 0.4525268311244594,
        "abs_return_acf_20": 0.34156465565951,
        "quantile_01": -0.07710941061048354,
        "quantile_99": 0.0626002455914984,
        "hill_tail_index": 2.23310351849366
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019616550994602397,
        "excess_kurtosis": 5.455933775671706,
        "return_acf_1": -0.024553202933287947,
        "abs_return_acf_1": 0.3851336709454083,
        "abs_return_acf_5": 0.2822958508162604,
        "abs_return_acf_20": 0.27620075947743356,
        "quantile_01": -0.058284137576118125,
        "quantile_99": 0.05741907391571589,
        "hill_tail_index": 3.6405557245544715
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024927461791881454,
        "excess_kurtosis": 11.274717903084236,
        "return_acf_1": -0.21678203164397328,
        "abs_return_acf_1": 0.5050956932504617,
        "abs_return_acf_5": 0.42375502618891,
        "abs_return_acf_20": 0.3679193105935695,
        "quantile_01": -0.08125324290170442,
        "quantile_99": 0.07326295006233904,
        "hill_tail_index": 2.781001349544448
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.025370196630069536,
        "excess_kurtosis": 14.52125567134808,
        "return_acf_1": -0.17417142563934168,
        "abs_return_acf_1": 0.4878708824483379,
        "abs_return_acf_5": 0.44397648512153276,
        "abs_return_acf_20": 0.3628374221861256,
        "quantile_01": -0.09525633513642556,
        "quantile_99": 0.07340484244574481,
        "hill_tail_index": 3.0177123954962473
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.026296036683576832,
        "excess_kurtosis": 15.213648642774338,
        "return_acf_1": -0.2210691889558116,
        "abs_return_acf_1": 0.5205244431410354,
        "abs_return_acf_5": 0.507154907208761,
        "abs_return_acf_20": 0.31251878636092695,
        "quantile_01": -0.088053237353856,
        "quantile_99": 0.0746153719101973,
        "hill_tail_index": 2.459317821045899
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.025800218795738142,
        "excess_kurtosis": 21.584151402213035,
        "return_acf_1": -0.1506077333985913,
        "abs_return_acf_1": 0.54572558908565,
        "abs_return_acf_5": 0.45361159746744767,
        "abs_return_acf_20": 0.3009661565874851,
        "quantile_01": -0.08172596491571131,
        "quantile_99": 0.07694289691700507,
        "hill_tail_index": 2.2120872493348838
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020679889722405892,
        "excess_kurtosis": 8.904208815595009,
        "return_acf_1": -0.18558015328029756,
        "abs_return_acf_1": 0.39163208784689507,
        "abs_return_acf_5": 0.3199098480685196,
        "abs_return_acf_20": 0.26453755110462296,
        "quantile_01": -0.0641314292376763,
        "quantile_99": 0.055213598975728,
        "hill_tail_index": 2.7674623757734205
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023113469246282443,
        "excess_kurtosis": 16.51460115895945,
        "return_acf_1": -0.16736927331727536,
        "abs_return_acf_1": 0.4033440687091355,
        "abs_return_acf_5": 0.397617024051606,
        "abs_return_acf_20": 0.3038222168168129,
        "quantile_01": -0.07951167339118613,
        "quantile_99": 0.061348196089126825,
        "hill_tail_index": 2.7982973814535224
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.026307197636673506,
        "excess_kurtosis": 14.309969844072562,
        "return_acf_1": -0.216266599063181,
        "abs_return_acf_1": 0.5514359789941438,
        "abs_return_acf_5": 0.48810708745313724,
        "abs_return_acf_20": 0.3736293463610627,
        "quantile_01": -0.08259944881609074,
        "quantile_99": 0.08226708843823549,
        "hill_tail_index": 2.6561541937158557
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02166662184730318,
        "excess_kurtosis": 5.097663949667089,
        "return_acf_1": -0.21701296633612968,
        "abs_return_acf_1": 0.38759524198227824,
        "abs_return_acf_5": 0.29119483445303085,
        "abs_return_acf_20": 0.24170377980496568,
        "quantile_01": -0.07942227166044485,
        "quantile_99": 0.053665709018192474,
        "hill_tail_index": 3.1712505998249303
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024092477685853698,
        "excess_kurtosis": 26.951889170605966,
        "return_acf_1": -0.24915166969725822,
        "abs_return_acf_1": 0.4537327884784866,
        "abs_return_acf_5": 0.455320569628569,
        "abs_return_acf_20": 0.2836940867814306,
        "quantile_01": -0.07450812222188696,
        "quantile_99": 0.061003714933579006,
        "hill_tail_index": 2.2184698100073694
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022523517312854454,
        "excess_kurtosis": 11.78319680971929,
        "return_acf_1": -0.20490838026163616,
        "abs_return_acf_1": 0.4168262983942398,
        "abs_return_acf_5": 0.33204053053490773,
        "abs_return_acf_20": 0.2826752463660023,
        "quantile_01": -0.0870165192196638,
        "quantile_99": 0.05615709524281647,
        "hill_tail_index": 2.4278820775547914
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02292304625368161,
        "excess_kurtosis": 23.100419422080606,
        "return_acf_1": -0.2170969380644722,
        "abs_return_acf_1": 0.3259112905799878,
        "abs_return_acf_5": 0.3191330037502905,
        "abs_return_acf_20": 0.21809809292448806,
        "quantile_01": -0.0711360287408041,
        "quantile_99": 0.04988592546346681,
        "hill_tail_index": 2.3924877572199863
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018112692546368134,
        "excess_kurtosis": 6.454393745514453,
        "return_acf_1": -0.09577273707607194,
        "abs_return_acf_1": 0.36979423616957147,
        "abs_return_acf_5": 0.4543952692414104,
        "abs_return_acf_20": 0.31240744861889397,
        "quantile_01": -0.053694833477798035,
        "quantile_99": 0.0536668264372845,
        "hill_tail_index": 3.41497561322067
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02764572679611191,
        "excess_kurtosis": 16.056996246206175,
        "return_acf_1": -0.1644169729731953,
        "abs_return_acf_1": 0.5392996618651259,
        "abs_return_acf_5": 0.45414310783031053,
        "abs_return_acf_20": 0.3651009426302301,
        "quantile_01": -0.09311834182462224,
        "quantile_99": 0.08373703856331675,
        "hill_tail_index": 2.7989048053287986
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.0241888114868287,
        "excess_kurtosis": 10.208724238208086,
        "return_acf_1": -0.18759771766555888,
        "abs_return_acf_1": 0.49718846198943306,
        "abs_return_acf_5": 0.45770427219781323,
        "abs_return_acf_20": 0.33599777224780586,
        "quantile_01": -0.0824840797068777,
        "quantile_99": 0.06620682429897798,
        "hill_tail_index": 3.3685860454832453
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022979864608788737,
        "excess_kurtosis": 5.614034479183157,
        "return_acf_1": -0.2169909881456533,
        "abs_return_acf_1": 0.38713137691895266,
        "abs_return_acf_5": 0.3267675332593633,
        "abs_return_acf_20": 0.25668233949017927,
        "quantile_01": -0.08030507402938587,
        "quantile_99": 0.06013312054619645,
        "hill_tail_index": 3.631387364567473
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017926536604970157,
        "excess_kurtosis": 7.261230864802853,
        "return_acf_1": -0.02179833449633241,
        "abs_return_acf_1": 0.2910476855651884,
        "abs_return_acf_5": 0.30307705997589496,
        "abs_return_acf_20": 0.28036858734617,
        "quantile_01": -0.054557220178033584,
        "quantile_99": 0.056885846189424466,
        "hill_tail_index": 2.91781838998839
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01796289973498446,
        "excess_kurtosis": 5.293564314147607,
        "return_acf_1": -0.06713135712115167,
        "abs_return_acf_1": 0.27913530818183935,
        "abs_return_acf_5": 0.2801593025429218,
        "abs_return_acf_20": 0.2516509047005994,
        "quantile_01": -0.05136122276365141,
        "quantile_99": 0.05128458499276215,
        "hill_tail_index": 3.504640052030016
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.025911953616292033,
        "excess_kurtosis": 16.3414885760001,
        "return_acf_1": -0.18333531498485964,
        "abs_return_acf_1": 0.5869417349718694,
        "abs_return_acf_5": 0.5211866062070222,
        "abs_return_acf_20": 0.3405427994928692,
        "quantile_01": -0.08870808923107629,
        "quantile_99": 0.07626047535091787,
        "hill_tail_index": 2.726618939880637
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02507940228359731,
        "excess_kurtosis": 16.064074423271222,
        "return_acf_1": -0.19238713836692137,
        "abs_return_acf_1": 0.4953937172979205,
        "abs_return_acf_5": 0.4549700385924613,
        "abs_return_acf_20": 0.3187320225841031,
        "quantile_01": -0.09182565084708456,
        "quantile_99": 0.06943940835898799,
        "hill_tail_index": 2.3938307548273796
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.024592510894581514,
        "excess_kurtosis": 13.270129769279873,
        "return_acf_1": -0.21910099176005837,
        "abs_return_acf_1": 0.5006851805629496,
        "abs_return_acf_5": 0.40890403083023824,
        "abs_return_acf_20": 0.33844107344936786,
        "quantile_01": -0.09107879693983237,
        "quantile_99": 0.07187346794549851,
        "hill_tail_index": 3.179987643678515
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02407755346432258,
        "excess_kurtosis": 15.372384098354054,
        "return_acf_1": -0.2046341581326375,
        "abs_return_acf_1": 0.5076243286534483,
        "abs_return_acf_5": 0.4806761458024058,
        "abs_return_acf_20": 0.34302871419020053,
        "quantile_01": -0.08411157879222546,
        "quantile_99": 0.07375374404236962,
        "hill_tail_index": 3.0646939941202898
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018498281947260237,
        "excess_kurtosis": 6.099960026458833,
        "return_acf_1": -0.08972067307337778,
        "abs_return_acf_1": 0.3365289031977706,
        "abs_return_acf_5": 0.35281000967293535,
        "abs_return_acf_20": 0.27933487007198443,
        "quantile_01": -0.05616365059515564,
        "quantile_99": 0.051989828251574305,
        "hill_tail_index": 2.9099446659142405
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02499415844321543,
        "excess_kurtosis": 14.491249636558393,
        "return_acf_1": -0.1966715089449834,
        "abs_return_acf_1": 0.4924974190078348,
        "abs_return_acf_5": 0.42156827402277397,
        "abs_return_acf_20": 0.32596530062041046,
        "quantile_01": -0.08730513914209241,
        "quantile_99": 0.06525936958485473,
        "hill_tail_index": 2.5496043263588164
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0245263649526438,
        "excess_kurtosis": 11.21796900550159,
        "return_acf_1": -0.14560968121456175,
        "abs_return_acf_1": 0.48431646364435177,
        "abs_return_acf_5": 0.40039364336427574,
        "abs_return_acf_20": 0.37798444614593985,
        "quantile_01": -0.07158550677599451,
        "quantile_99": 0.07457165035604531,
        "hill_tail_index": 2.9235904163222446
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02277026518508917,
        "excess_kurtosis": 14.941339404057857,
        "return_acf_1": -0.17275027681646893,
        "abs_return_acf_1": 0.4623360499215202,
        "abs_return_acf_5": 0.41764132042420593,
        "abs_return_acf_20": 0.3369181003582754,
        "quantile_01": -0.07331533557794484,
        "quantile_99": 0.05817504207655332,
        "hill_tail_index": 2.3124231682210596
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02412003660616775,
        "excess_kurtosis": 11.661541547326594,
        "return_acf_1": -0.21679856920811114,
        "abs_return_acf_1": 0.5163392532066085,
        "abs_return_acf_5": 0.45519205951130737,
        "abs_return_acf_20": 0.2949405770852451,
        "quantile_01": -0.0924339923145326,
        "quantile_99": 0.07092681909780497,
        "hill_tail_index": 3.706077910544543
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
