# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27217
Run ID: `0ab0c9cae1ac34be471f358d350948bbb670160815d3aecc87940134da73a01b`
Result fingerprint: `cab0c5089b40140faae87530bb6a193ce238854c7034ade480d34633f92a2609`

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
    "equal_weight_sd": -0.7254642857142827,
    "equal_weight_raw": -10.881964285714238,
    "fixed_start_cap_weight_sd": -0.6735039315950685,
    "fixed_start_cap_weight_raw": -10.102558973926023,
    "end_cap_weight_sd": -0.6642548919450797,
    "end_cap_weight_raw": -9.963823379176198
  },
  "full_period_change": {
    "equal_weight_sd": -1.1075714285714233,
    "equal_weight_raw": -16.61357142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0430135582010538,
    "inflation_mean_sd": 0.5605932539682539
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2269166666666698,
    "equal_weight_raw": 3.4037500000000476,
    "fixed_start_cap_weight_sd": 0.2788770207858839,
    "fixed_start_cap_weight_raw": 4.1831553117882585,
    "end_cap_weight_sd": 0.2881260604358725,
    "end_cap_weight_raw": 4.321890906538088
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5690476190476158,
      "change_raw": -8.535714285714237,
      "decay_adjusted_gain_sd": 0.38333333333333647
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7498809523809492,
      "change_raw": -11.248214285714239,
      "decay_adjusted_gain_sd": 0.20250000000000312
    },
    "small": {
      "count": 18,
      "change_sd": -0.7393253968253936,
      "change_raw": -11.089880952380904,
      "decay_adjusted_gain_sd": 0.21305555555555875
    },
    "large_minus_small_sd": 0.17027777777777775,
    "large_minus_small_raw": 2.5541666666666663
  },
  "inflation": {
    "initial_mean_sd": 0.28025,
    "final_mean_sd": 0.58925,
    "mean_sd": 0.445919442131557,
    "mean_absolute_raw_gap": 6.688791631973355,
    "final_absolute_raw_gap": 8.83875,
    "mean_range_fraction": 0.06688791631973355
  },
  "impact": {
    "initial_share": 0.34,
    "final_share": 0.36666666666666664,
    "initial_wealth_share": 0.28851420915209475,
    "final_wealth_share": 0.3176782910431687
  },
  "pricing_slope": {
    "mean": -0.002618206679358744,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.03230886146686137,
    "real_improvement_cost": 0.021383704556334315,
    "washing_cost": 0.010925156910527055,
    "fine_transfer": 0.024751027601396035,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0570598890682574,
    "resource_cost_fraction_initial_cap": 0.001076962048895379,
    "private_net_outflow_fraction_initial_cap": 0.0019019963022752467,
    "fine_transfer_fraction_initial_cap": 0.0008250342533798679,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0014066593409629014,
    "unapplied_final_day_resource_cost": 0.0002449938270262151
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 210.70070844131806,
    "beneficial_raw_gain_per_resource_cost": 3160.510626619771,
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
    "accrued_cost": 3.1840919541723096,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": -0.20790147798183325,
    "accrued_cost_fraction_initial_cap": 0.10613639847241033,
    "mean_contract_rate": 0.0442902866306063,
    "maximum_ledger_error": 8.809142651444724e-20
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
    "maximum_relative_cash_error": 1.2275828685101985e-15,
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
      "minimum": -0.1570600448212032,
      "maximum": -0.06459663374463985,
      "mean": -0.10982475601352146,
      "median": -0.10555905613139338,
      "quantile_05": -0.15109154530061972,
      "quantile_95": -0.06848829631032523
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
      "minimum": 0.20954504743383942,
      "maximum": 0.7993256933655158,
      "mean": 0.6089539820913772,
      "median": 0.6306028514187214,
      "quantile_05": 0.3530828258184349,
      "quantile_95": 0.7666316016973331
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
        "daily_volatility": 0.02044199577057722,
        "excess_kurtosis": 19.874257605610147,
        "return_acf_1": -0.13323952120188076,
        "abs_return_acf_1": 0.31379178150378767,
        "abs_return_acf_5": 0.3293402679570571,
        "abs_return_acf_20": 0.22076985904985602,
        "quantile_01": -0.061832589756050535,
        "quantile_99": 0.04708983748558621,
        "hill_tail_index": 2.4300200766214157
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022472686926081547,
        "excess_kurtosis": 11.204159648734594,
        "return_acf_1": -0.11694611285913886,
        "abs_return_acf_1": 0.40357177232232494,
        "abs_return_acf_5": 0.47160496658075046,
        "abs_return_acf_20": 0.2748249871345256,
        "quantile_01": -0.07252137258285363,
        "quantile_99": 0.059942018528376495,
        "hill_tail_index": 2.669985276568432
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018577988215239757,
        "excess_kurtosis": 3.680619970008337,
        "return_acf_1": -0.12259430534133715,
        "abs_return_acf_1": 0.289441460531781,
        "abs_return_acf_5": 0.21861203851964803,
        "abs_return_acf_20": 0.25253403521170675,
        "quantile_01": -0.05058192788625763,
        "quantile_99": 0.053226693373054516,
        "hill_tail_index": 3.830570087789794
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021164843913062118,
        "excess_kurtosis": 9.561603220847177,
        "return_acf_1": -0.09596948075366482,
        "abs_return_acf_1": 0.3633237889830732,
        "abs_return_acf_5": 0.37262496024167985,
        "abs_return_acf_20": 0.2520983629436227,
        "quantile_01": -0.06572162553504107,
        "quantile_99": 0.05249576810308281,
        "hill_tail_index": 2.416219973512252
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022086631790903345,
        "excess_kurtosis": 11.45294532779186,
        "return_acf_1": -0.10295084951493777,
        "abs_return_acf_1": 0.3839725848478572,
        "abs_return_acf_5": 0.44708741911052785,
        "abs_return_acf_20": 0.24801841769606361,
        "quantile_01": -0.08073421242954588,
        "quantile_99": 0.06362685348983067,
        "hill_tail_index": 2.8567170501978163
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02275925455206615,
        "excess_kurtosis": 10.975799350995345,
        "return_acf_1": -0.1486565393003294,
        "abs_return_acf_1": 0.41594541895166687,
        "abs_return_acf_5": 0.4278116343027399,
        "abs_return_acf_20": 0.3223499007407526,
        "quantile_01": -0.07721182291486364,
        "quantile_99": 0.06424422378675367,
        "hill_tail_index": 3.1021443833091022
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01922881646111148,
        "excess_kurtosis": 7.2350348346159254,
        "return_acf_1": -0.14115333864454208,
        "abs_return_acf_1": 0.3865648518685892,
        "abs_return_acf_5": 0.3021126072155998,
        "abs_return_acf_20": 0.2264455388398197,
        "quantile_01": -0.056912126334005386,
        "quantile_99": 0.0530185661350598,
        "hill_tail_index": 3.422404358172783
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02044622473814594,
        "excess_kurtosis": 5.853242170542277,
        "return_acf_1": -0.10280408490011068,
        "abs_return_acf_1": 0.3077050262706009,
        "abs_return_acf_5": 0.3716336939300732,
        "abs_return_acf_20": 0.22917167367377428,
        "quantile_01": -0.06825051453801442,
        "quantile_99": 0.06154664292576241,
        "hill_tail_index": 4.052789948855374
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021755841841849952,
        "excess_kurtosis": 9.940111406686889,
        "return_acf_1": -0.12681330717501804,
        "abs_return_acf_1": 0.4101129988966739,
        "abs_return_acf_5": 0.37589647412407123,
        "abs_return_acf_20": 0.3287169502355563,
        "quantile_01": -0.07380002568223058,
        "quantile_99": 0.06910169853315727,
        "hill_tail_index": 3.1431255896925374
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021023011027450075,
        "excess_kurtosis": 6.754882568393876,
        "return_acf_1": -0.0876503381545714,
        "abs_return_acf_1": 0.38090586982112157,
        "abs_return_acf_5": 0.40934044540265985,
        "abs_return_acf_20": 0.25152396863297216,
        "quantile_01": -0.060860393844075114,
        "quantile_99": 0.06442856224506562,
        "hill_tail_index": 3.440650562454308
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020758746711941903,
        "excess_kurtosis": 14.770205854419775,
        "return_acf_1": -0.07894825472995219,
        "abs_return_acf_1": 0.3466616843808718,
        "abs_return_acf_5": 0.39573807541086026,
        "abs_return_acf_20": 0.2885806073550517,
        "quantile_01": -0.07110327683178881,
        "quantile_99": 0.047826059658051326,
        "hill_tail_index": 1.8035656564314761
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020807088780759507,
        "excess_kurtosis": 10.33097044721378,
        "return_acf_1": -0.13833679317971326,
        "abs_return_acf_1": 0.2927604863190703,
        "abs_return_acf_5": 0.3071617742642368,
        "abs_return_acf_20": 0.2578406083773965,
        "quantile_01": -0.0662139085100354,
        "quantile_99": 0.05362308133452685,
        "hill_tail_index": 2.4160379972112853
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02138450904222996,
        "excess_kurtosis": 10.263486106663485,
        "return_acf_1": -0.08565498363041364,
        "abs_return_acf_1": 0.3668319999718893,
        "abs_return_acf_5": 0.340026401486567,
        "abs_return_acf_20": 0.24740904482885256,
        "quantile_01": -0.07139397574587872,
        "quantile_99": 0.05295145062114852,
        "hill_tail_index": 2.801548229460174
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021649290185498826,
        "excess_kurtosis": 11.576746299511626,
        "return_acf_1": -0.09031792147978229,
        "abs_return_acf_1": 0.3023768096837099,
        "abs_return_acf_5": 0.35877370176974815,
        "abs_return_acf_20": 0.23416199268890459,
        "quantile_01": -0.06961372882230986,
        "quantile_99": 0.053618440574507174,
        "hill_tail_index": 2.6056080947554663
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0219464866988338,
        "excess_kurtosis": 7.887716131781502,
        "return_acf_1": -0.06631728038601731,
        "abs_return_acf_1": 0.33940343874067047,
        "abs_return_acf_5": 0.43410657135949365,
        "abs_return_acf_20": 0.32322257916176195,
        "quantile_01": -0.07505841960028951,
        "quantile_99": 0.05542211978370425,
        "hill_tail_index": 3.310320503209562
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020368158669291488,
        "excess_kurtosis": 7.47747117013431,
        "return_acf_1": -0.12670828980549892,
        "abs_return_acf_1": 0.3697500558903068,
        "abs_return_acf_5": 0.2949155870170075,
        "abs_return_acf_20": 0.3517036107247199,
        "quantile_01": -0.0678160507749181,
        "quantile_99": 0.05792989631075977,
        "hill_tail_index": 3.1604553019635744
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018914003389901606,
        "excess_kurtosis": 10.342435894385643,
        "return_acf_1": -0.15308382293722086,
        "abs_return_acf_1": 0.32120003255994994,
        "abs_return_acf_5": 0.34429636363976074,
        "abs_return_acf_20": 0.25917243514996285,
        "quantile_01": -0.05242060683141322,
        "quantile_99": 0.042087301193765955,
        "hill_tail_index": 2.269319748671803
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020269789342211922,
        "excess_kurtosis": 11.603641473468002,
        "return_acf_1": -0.08121559379830172,
        "abs_return_acf_1": 0.278533325302011,
        "abs_return_acf_5": 0.31140613794279187,
        "abs_return_acf_20": 0.21644615240413184,
        "quantile_01": -0.06456992976453896,
        "quantile_99": 0.05412546475793266,
        "hill_tail_index": 2.4793603979049315
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01795813608992209,
        "excess_kurtosis": 2.984141119458717,
        "return_acf_1": -0.12364176342256282,
        "abs_return_acf_1": 0.26678657108880927,
        "abs_return_acf_5": 0.21676456324995516,
        "abs_return_acf_20": 0.16397413307878222,
        "quantile_01": -0.06055906837836926,
        "quantile_99": 0.048680192400376826,
        "hill_tail_index": 4.0016313122622496
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02345350114732109,
        "excess_kurtosis": 13.726417482107571,
        "return_acf_1": -0.07114176021781264,
        "abs_return_acf_1": 0.3333244980436753,
        "abs_return_acf_5": 0.45464143165627713,
        "abs_return_acf_20": 0.2646773299383473,
        "quantile_01": -0.10149007440856378,
        "quantile_99": 0.0685407919511776,
        "hill_tail_index": 2.5840757881991387
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022534605837952578,
        "excess_kurtosis": 13.06810074490199,
        "return_acf_1": -0.10699165109248143,
        "abs_return_acf_1": 0.342454840430461,
        "abs_return_acf_5": 0.26205949564486897,
        "abs_return_acf_20": 0.1881609431833568,
        "quantile_01": -0.061878909436711954,
        "quantile_99": 0.06652207705332355,
        "hill_tail_index": 3.0191109811679886
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02161987627719933,
        "excess_kurtosis": 14.59790729345806,
        "return_acf_1": -0.1287124755614645,
        "abs_return_acf_1": 0.32855606566416523,
        "abs_return_acf_5": 0.4184768470533605,
        "abs_return_acf_20": 0.31754623518899056,
        "quantile_01": -0.06216211886688472,
        "quantile_99": 0.06400797962772295,
        "hill_tail_index": 2.195205580579334
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018040688669403174,
        "excess_kurtosis": 6.917749789785452,
        "return_acf_1": -0.1570600448212032,
        "abs_return_acf_1": 0.27525694648204796,
        "abs_return_acf_5": 0.24392270597937418,
        "abs_return_acf_20": 0.20603440617114505,
        "quantile_01": -0.04815816385662715,
        "quantile_99": 0.051325504564013025,
        "hill_tail_index": 3.487367203545397
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018429662572686977,
        "excess_kurtosis": 9.533091325460086,
        "return_acf_1": -0.07672386868641395,
        "abs_return_acf_1": 0.32708109890583226,
        "abs_return_acf_5": 0.3242829594478493,
        "abs_return_acf_20": 0.1556763269730738,
        "quantile_01": -0.06863164286240275,
        "quantile_99": 0.045627874543586064,
        "hill_tail_index": 2.567517220788476
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020035201796739968,
        "excess_kurtosis": 10.020205698467953,
        "return_acf_1": -0.06459663374463985,
        "abs_return_acf_1": 0.34455462974802764,
        "abs_return_acf_5": 0.34737267270099403,
        "abs_return_acf_20": 0.23074256583201655,
        "quantile_01": -0.06483414812856862,
        "quantile_99": 0.05531463549830669,
        "hill_tail_index": 2.898613492212156
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02027102323851799,
        "excess_kurtosis": 8.219195128430504,
        "return_acf_1": -0.09850468419247431,
        "abs_return_acf_1": 0.36058374060567083,
        "abs_return_acf_5": 0.34687058214683253,
        "abs_return_acf_20": 0.21046582702935693,
        "quantile_01": -0.07521550584079481,
        "quantile_99": 0.05639780001076121,
        "hill_tail_index": 2.8328056931360606
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02040685708268376,
        "excess_kurtosis": 12.613535024352231,
        "return_acf_1": -0.09694022219017237,
        "abs_return_acf_1": 0.27034793363843074,
        "abs_return_acf_5": 0.31931490712779154,
        "abs_return_acf_20": 0.25750714860273344,
        "quantile_01": -0.06691416011577218,
        "quantile_99": 0.051972558510824794,
        "hill_tail_index": 2.6365698520570517
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.023144294205271285,
        "excess_kurtosis": 12.732219528519257,
        "return_acf_1": -0.13746788296037377,
        "abs_return_acf_1": 0.3973088478467691,
        "abs_return_acf_5": 0.4511613203690409,
        "abs_return_acf_20": 0.278534428574982,
        "quantile_01": -0.0864668870944697,
        "quantile_99": 0.06497601443851968,
        "hill_tail_index": 2.6012564666852698
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019544913482456766,
        "excess_kurtosis": 9.55045868462872,
        "return_acf_1": -0.12947441455330758,
        "abs_return_acf_1": 0.2933778356351636,
        "abs_return_acf_5": 0.27680572998020403,
        "abs_return_acf_20": 0.22484043204246057,
        "quantile_01": -0.05700375195784718,
        "quantile_99": 0.05124648101036868,
        "hill_tail_index": 2.6595001338080917
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.022070454646243576,
        "excess_kurtosis": 8.31910855747341,
        "return_acf_1": -0.10412646117030534,
        "abs_return_acf_1": 0.43106474415666474,
        "abs_return_acf_5": 0.3875023992988202,
        "abs_return_acf_20": 0.2976672953516441,
        "quantile_01": -0.07670482758477427,
        "quantile_99": 0.0626314565184053,
        "hill_tail_index": 3.0245105247248874
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
