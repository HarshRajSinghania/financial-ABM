# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27061
Run ID: `e4002efcd9f7aa2b52d26714f546e149021ce349b6d0fb2a7adc823a9a2804ee`
Result fingerprint: `beb8fee5c6527635ec06cf884894e0caabc6e7bc02c2ae1d3aacc91afd98b873`

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
    "equal_weight_sd": -0.5603809523809491,
    "equal_weight_raw": -8.405714285714238,
    "fixed_start_cap_weight_sd": -0.5724223205406055,
    "fixed_start_cap_weight_raw": -8.586334808109081,
    "end_cap_weight_sd": -0.5779346415826887,
    "end_cap_weight_raw": -8.669019623740333
  },
  "full_period_change": {
    "equal_weight_sd": -0.8894880952380901,
    "equal_weight_raw": -13.342321428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8327139550264505,
    "inflation_mean_sd": 0.6096835317460318
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3920000000000032,
    "equal_weight_raw": 5.880000000000047,
    "fixed_start_cap_weight_sd": 0.37995863184034684,
    "fixed_start_cap_weight_raw": 5.699379477605201,
    "end_cap_weight_sd": 0.37444631079826374,
    "end_cap_weight_raw": 5.616694661973955
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.3857142857142824,
      "change_raw": -5.785714285714236,
      "decay_adjusted_gain_sd": 0.5666666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6357142857142825,
      "change_raw": -9.535714285714237,
      "decay_adjusted_gain_sd": 0.31666666666666987
    },
    "small": {
      "count": 18,
      "change_sd": -0.5518253968253936,
      "change_raw": -8.277380952380904,
      "decay_adjusted_gain_sd": 0.4005555555555588
    },
    "large_minus_small_sd": 0.16611111111111115,
    "large_minus_small_raw": 2.491666666666667
  },
  "inflation": {
    "initial_mean_sd": 0.2703333333333333,
    "final_mean_sd": 0.6789166666666667,
    "mean_sd": 0.44368769081321124,
    "mean_absolute_raw_gap": 6.655315362198168,
    "final_absolute_raw_gap": 10.18375,
    "mean_range_fraction": 0.06655315362198168
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.35736155541090275,
    "final_wealth_share": 0.3515329294260163
  },
  "pricing_slope": {
    "mean": -0.0015974797741598653,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.12285057674066785,
    "real_improvement_cost": 0.11243860159241816,
    "washing_cost": 0.010411975148249685,
    "fine_transfer": 0.023512119104508414,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.14636269584517625,
    "resource_cost_fraction_initial_cap": 0.004095019224688929,
    "private_net_outflow_fraction_initial_cap": 0.004878756528172542,
    "fine_transfer_fraction_initial_cap": 0.0007837373034836138,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004529279508566742,
    "unapplied_final_day_resource_cost": 0.00033465876272544
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 95.72604632394146,
    "beneficial_raw_gain_per_resource_cost": 1435.8906948591218,
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
    "accrued_cost": 2.933527172235263,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.042663303955213255,
    "accrued_cost_fraction_initial_cap": 0.09778423907450878,
    "mean_contract_rate": 0.04129922682366206,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.4842554002108308e-15,
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
      "minimum": -0.20739165529604267,
      "maximum": -0.06399867278194163,
      "mean": -0.14086610839401623,
      "median": -0.14188086473838307,
      "quantile_05": -0.2013506633273423,
      "quantile_95": -0.0694989077758743
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
      "minimum": 0.30829313443093703,
      "maximum": 0.7148738195860291,
      "mean": 0.4695357192291214,
      "median": 0.4473052474808052,
      "quantile_05": 0.33272564882059213,
      "quantile_95": 0.6591155296551805
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
        "daily_volatility": 0.01816830402620774,
        "excess_kurtosis": 4.703957882185726,
        "return_acf_1": -0.17155696366133402,
        "abs_return_acf_1": 0.33092054063746157,
        "abs_return_acf_5": 0.28575221201098844,
        "abs_return_acf_20": 0.30973039154604176,
        "quantile_01": -0.05641902109507451,
        "quantile_99": 0.052448643577388265,
        "hill_tail_index": 3.8064078403126533
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016264698820667053,
        "excess_kurtosis": 7.7306606770866,
        "return_acf_1": -0.19456787203419598,
        "abs_return_acf_1": 0.46423706884439564,
        "abs_return_acf_5": 0.34222184839415754,
        "abs_return_acf_20": 0.2527714144029537,
        "quantile_01": -0.05969454179673354,
        "quantile_99": 0.03746853406620938,
        "hill_tail_index": 2.4542034521414884
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017863107679789707,
        "excess_kurtosis": 6.476562690989516,
        "return_acf_1": -0.14843447191426185,
        "abs_return_acf_1": 0.365438702290741,
        "abs_return_acf_5": 0.36283362425745624,
        "abs_return_acf_20": 0.29055365024538043,
        "quantile_01": -0.06414093319837652,
        "quantile_99": 0.05310868985801352,
        "hill_tail_index": 3.319365147613569
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01602718863865925,
        "excess_kurtosis": 7.027292710817214,
        "return_acf_1": -0.14540232907006645,
        "abs_return_acf_1": 0.3605586258940821,
        "abs_return_acf_5": 0.317356222286623,
        "abs_return_acf_20": 0.18001360559473314,
        "quantile_01": -0.04971948914097843,
        "quantile_99": 0.04690630777328827,
        "hill_tail_index": 3.69492229324316
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016189535662158493,
        "excess_kurtosis": 8.779623045409892,
        "return_acf_1": -0.10621431613873764,
        "abs_return_acf_1": 0.23153659341590274,
        "abs_return_acf_5": 0.30591479161505697,
        "abs_return_acf_20": 0.28400304842030566,
        "quantile_01": -0.0410564140174607,
        "quantile_99": 0.051913063996348076,
        "hill_tail_index": 2.9907333785058405
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01690584591772604,
        "excess_kurtosis": 10.858293139785332,
        "return_acf_1": -0.16781541000176667,
        "abs_return_acf_1": 0.3191334633587694,
        "abs_return_acf_5": 0.40907283153128704,
        "abs_return_acf_20": 0.3024299109353331,
        "quantile_01": -0.04308115380505455,
        "quantile_99": 0.05087694492943147,
        "hill_tail_index": 2.6323753682765894
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.014509760807706395,
        "excess_kurtosis": 6.20799266159381,
        "return_acf_1": -0.18702261904451434,
        "abs_return_acf_1": 0.2306619026821922,
        "abs_return_acf_5": 0.1814407207201574,
        "abs_return_acf_20": 0.15373856422844487,
        "quantile_01": -0.03827101109746444,
        "quantile_99": 0.03353811354473638,
        "hill_tail_index": 2.6870066250210916
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01679597389492895,
        "excess_kurtosis": 4.382618036062167,
        "return_acf_1": -0.17307238421936885,
        "abs_return_acf_1": 0.34334988365931507,
        "abs_return_acf_5": 0.32456061409518694,
        "abs_return_acf_20": 0.3293958002585619,
        "quantile_01": -0.048586628409707094,
        "quantile_99": 0.04495293471789663,
        "hill_tail_index": 3.811311723964543
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017880544839381587,
        "excess_kurtosis": 4.3234747832081455,
        "return_acf_1": -0.09315633333116877,
        "abs_return_acf_1": 0.3687698764472107,
        "abs_return_acf_5": 0.3427712818317094,
        "abs_return_acf_20": 0.36257966839943145,
        "quantile_01": -0.05798509083019369,
        "quantile_99": 0.04645301240145257,
        "hill_tail_index": 4.764409658792043
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019212694737142176,
        "excess_kurtosis": 9.545031520583821,
        "return_acf_1": -0.06399867278194163,
        "abs_return_acf_1": 0.37043355316982157,
        "abs_return_acf_5": 0.36038509336959695,
        "abs_return_acf_20": 0.2852938706796012,
        "quantile_01": -0.055917085784311385,
        "quantile_99": 0.05349495966192776,
        "hill_tail_index": 3.219830404631068
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016291325362435688,
        "excess_kurtosis": 5.035359036198361,
        "return_acf_1": -0.10278780148619208,
        "abs_return_acf_1": 0.2196846369056325,
        "abs_return_acf_5": 0.21928507832427477,
        "abs_return_acf_20": 0.18957549723004846,
        "quantile_01": -0.044998195283339405,
        "quantile_99": 0.04061122719432654,
        "hill_tail_index": 3.37400160670264
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018148601457869628,
        "excess_kurtosis": 6.1910955793945845,
        "return_acf_1": -0.12707840500464956,
        "abs_return_acf_1": 0.2772005621223805,
        "abs_return_acf_5": 0.2729024733639194,
        "abs_return_acf_20": 0.27693690881882255,
        "quantile_01": -0.054417219759478476,
        "quantile_99": 0.054034482111605525,
        "hill_tail_index": 3.2657482545799774
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016902777051901848,
        "excess_kurtosis": 6.980571355245614,
        "return_acf_1": -0.08095563983128863,
        "abs_return_acf_1": 0.3940282159396375,
        "abs_return_acf_5": 0.34140469772418647,
        "abs_return_acf_20": 0.2681303721802753,
        "quantile_01": -0.05239744362364752,
        "quantile_99": 0.04375521945306103,
        "hill_tail_index": 3.334461816604694
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018636972379656874,
        "excess_kurtosis": 6.450404227267825,
        "return_acf_1": -0.20690021983991655,
        "abs_return_acf_1": 0.44259688836877403,
        "abs_return_acf_5": 0.42897948845280015,
        "abs_return_acf_20": 0.3346271108575665,
        "quantile_01": -0.05849976211059319,
        "quantile_99": 0.05058997497075201,
        "hill_tail_index": 3.718528859732308
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017816620108787824,
        "excess_kurtosis": 14.74324365574444,
        "return_acf_1": -0.0688248311363113,
        "abs_return_acf_1": 0.4476485335160889,
        "abs_return_acf_5": 0.46762812310130647,
        "abs_return_acf_20": 0.35685021460160793,
        "quantile_01": -0.044457142889169285,
        "quantile_99": 0.05361772557994179,
        "hill_tail_index": 1.9936611763398744
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017007656881065182,
        "excess_kurtosis": 4.3303126665712,
        "return_acf_1": -0.13380911015804914,
        "abs_return_acf_1": 0.32734705623916366,
        "abs_return_acf_5": 0.23340708175190017,
        "abs_return_acf_20": 0.3205968736452488,
        "quantile_01": -0.05325772487252043,
        "quantile_99": 0.047779601936623964,
        "hill_tail_index": 4.259425827669804
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017411646248240483,
        "excess_kurtosis": 6.804487438768275,
        "return_acf_1": -0.11379305744593882,
        "abs_return_acf_1": 0.31427406523708384,
        "abs_return_acf_5": 0.33136610467029826,
        "abs_return_acf_20": 0.3193929185840709,
        "quantile_01": -0.051680614427597485,
        "quantile_99": 0.04736917237237646,
        "hill_tail_index": 3.035625058142121
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01877088703076702,
        "excess_kurtosis": 7.337381663657146,
        "return_acf_1": -0.20739165529604267,
        "abs_return_acf_1": 0.3697667257895729,
        "abs_return_acf_5": 0.37869356138448595,
        "abs_return_acf_20": 0.3862051480531984,
        "quantile_01": -0.06894551276775866,
        "quantile_99": 0.05037925743402564,
        "hill_tail_index": 2.8225272084162265
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017671481590209356,
        "excess_kurtosis": 4.810868590035597,
        "return_acf_1": -0.07032277922422905,
        "abs_return_acf_1": 0.3550947371652064,
        "abs_return_acf_5": 0.29994573297461485,
        "abs_return_acf_20": 0.3484057716825323,
        "quantile_01": -0.05014917156244371,
        "quantile_99": 0.05380200430405922,
        "hill_tail_index": 4.075131941219977
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01548034920554629,
        "excess_kurtosis": 5.8282292524378825,
        "return_acf_1": -0.1514444076827415,
        "abs_return_acf_1": 0.2670605941448779,
        "abs_return_acf_5": 0.2546676340065147,
        "abs_return_acf_20": 0.24729379925852554,
        "quantile_01": -0.04161892491087532,
        "quantile_99": 0.04171665692527754,
        "hill_tail_index": 3.0176566405325196
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.015407790451376184,
        "excess_kurtosis": 7.480288375858089,
        "return_acf_1": -0.13835940040669967,
        "abs_return_acf_1": 0.30603341390305605,
        "abs_return_acf_5": 0.34598015237557866,
        "abs_return_acf_20": 0.23012187041814386,
        "quantile_01": -0.04364714351392288,
        "quantile_99": 0.03973830258759581,
        "hill_tail_index": 2.670837953956334
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01789547544906367,
        "excess_kurtosis": 4.0941808303112275,
        "return_acf_1": -0.1673800575991572,
        "abs_return_acf_1": 0.2807278565697451,
        "abs_return_acf_5": 0.3132412373420907,
        "abs_return_acf_20": 0.26269017667570255,
        "quantile_01": -0.06086831538434953,
        "quantile_99": 0.0474585671632714,
        "hill_tail_index": 3.5549212344666485
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017769199978863923,
        "excess_kurtosis": 4.122624167106759,
        "return_acf_1": -0.18526609101727637,
        "abs_return_acf_1": 0.3721706275392247,
        "abs_return_acf_5": 0.35308883865081897,
        "abs_return_acf_20": 0.2578618270183836,
        "quantile_01": -0.053551332021876716,
        "quantile_99": 0.05242250638624723,
        "hill_tail_index": 4.539979065895934
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.015763683991364602,
        "excess_kurtosis": 6.0328211456380085,
        "return_acf_1": -0.12505743321232574,
        "abs_return_acf_1": 0.33647946667213624,
        "abs_return_acf_5": 0.3790367050152492,
        "abs_return_acf_20": 0.29754703761100065,
        "quantile_01": -0.04567062463547579,
        "quantile_99": 0.03993036479925542,
        "hill_tail_index": 3.218136469799401
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.016876265757987872,
        "excess_kurtosis": 6.032720706634704,
        "return_acf_1": -0.15331357222283265,
        "abs_return_acf_1": 0.3253688747411279,
        "abs_return_acf_5": 0.24116614606629933,
        "abs_return_acf_20": 0.2695460405622893,
        "quantile_01": -0.05264986233424214,
        "quantile_99": 0.0437626526616487,
        "hill_tail_index": 3.549432982172152
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01674560713618194,
        "excess_kurtosis": 18.43286951825928,
        "return_acf_1": -0.11861224969909023,
        "abs_return_acf_1": 0.3647440596025492,
        "abs_return_acf_5": 0.30168921700987855,
        "abs_return_acf_20": 0.19856180899481904,
        "quantile_01": -0.04382798051686393,
        "quantile_99": 0.04289930496299168,
        "hill_tail_index": 2.4020576396916775
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017456335581234352,
        "excess_kurtosis": 4.183476241527836,
        "return_acf_1": -0.19058700062434533,
        "abs_return_acf_1": 0.36429757446194044,
        "abs_return_acf_5": 0.39259879042249257,
        "abs_return_acf_20": 0.3268518694421771,
        "quantile_01": -0.05403474840316636,
        "quantile_99": 0.05128438945748788,
        "hill_tail_index": 5.413973370338087
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01699405481545398,
        "excess_kurtosis": 5.200348948300741,
        "return_acf_1": -0.12223248675814444,
        "abs_return_acf_1": 0.40234766202324107,
        "abs_return_acf_5": 0.3773751454228243,
        "abs_return_acf_20": 0.23627139579453543,
        "quantile_01": -0.05836795276253169,
        "quantile_99": 0.050952164443119834,
        "hill_tail_index": 3.1447807311339533
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016079148732443913,
        "excess_kurtosis": 4.3356260710673045,
        "return_acf_1": -0.12660388326425837,
        "abs_return_acf_1": 0.23578934414933542,
        "abs_return_acf_5": 0.24831678674446478,
        "abs_return_acf_20": 0.2445104750308808,
        "quantile_01": -0.048952798840931455,
        "quantile_99": 0.03787302824062413,
        "hill_tail_index": 2.7812459789620343
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016257921763367284,
        "excess_kurtosis": 12.866522849409606,
        "return_acf_1": -0.1840217977136413,
        "abs_return_acf_1": 0.46353292602723395,
        "abs_return_acf_5": 0.33231533863930296,
        "abs_return_acf_20": 0.2646417963646426,
        "quantile_01": -0.04931401780143063,
        "quantile_99": 0.047206121029253326,
        "hill_tail_index": 2.034382606323869
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
