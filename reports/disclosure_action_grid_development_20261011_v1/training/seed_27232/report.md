# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27232
Run ID: `103745661e5a1836ec69cc3c6daea0f56e80af7847c92473217f13887bd3510f`
Result fingerprint: `f100751c2bd9ef3e6a0e58c37fb4fb371ff6b36f46faac2d47eecbf4eaffaef9`

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
    "equal_weight_sd": -0.7729642857142823,
    "equal_weight_raw": -11.594464285714231,
    "fixed_start_cap_weight_sd": -0.8302231571825371,
    "fixed_start_cap_weight_raw": -12.453347357738059,
    "end_cap_weight_sd": -0.8183375605525498,
    "end_cap_weight_raw": -12.275063408288242
  },
  "full_period_change": {
    "equal_weight_sd": -1.2209880952380903,
    "equal_weight_raw": -18.314821428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1489765211640164,
    "inflation_mean_sd": 0.7431054894179895
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.177954249806402,
    "equal_weight_raw": 2.6693137470960306,
    "fixed_start_cap_weight_sd": 0.1202101204296923,
    "fixed_start_cap_weight_raw": 1.803151806445384,
    "end_cap_weight_sd": 0.13103687593058155,
    "end_cap_weight_raw": 1.965553138958723
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.9240476190476158,
      "change_raw": -13.860714285714236,
      "decay_adjusted_gain_sd": 0.02833333333333647
    },
    "mid": {
      "count": 9,
      "change_sd": -0.76349206349206,
      "change_raw": -11.4523809523809,
      "decay_adjusted_gain_sd": 0.18401416602133264
    },
    "small": {
      "count": 18,
      "change_sd": -0.7525198412698381,
      "change_raw": -11.287797619047572,
      "decay_adjusted_gain_sd": 0.19986111111111438
    },
    "large_minus_small_sd": -0.17152777777777772,
    "large_minus_small_raw": -2.572916666666666
  },
  "inflation": {
    "initial_mean_sd": 0.33625,
    "final_mean_sd": 0.79125,
    "mean_sd": 0.6158933527615876,
    "mean_absolute_raw_gap": 9.238400291423813,
    "final_absolute_raw_gap": 11.868750000000002,
    "mean_range_fraction": 0.09238400291423814
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.25592967968264324,
    "final_wealth_share": 0.35552886057896577
  },
  "pricing_slope": {
    "mean": -0.00602910998533072,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.01565381760578114,
    "real_improvement_cost": 0.00871437869188063,
    "washing_cost": 0.006939438913900515,
    "fine_transfer": 0.05136881373923828,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06702263134501943,
    "resource_cost_fraction_initial_cap": 0.0005217939201927047,
    "private_net_outflow_fraction_initial_cap": 0.0022340877115006475,
    "fine_transfer_fraction_initial_cap": 0.0017122937913079427,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0003590333335187451,
    "unapplied_final_day_resource_cost": 0.00034020571920148786
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 341.04316459011517,
    "beneficial_raw_gain_per_resource_cost": 5115.647468851728,
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
    "accrued_cost": 2.968269633381297,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.007920842809179436,
    "accrued_cost_fraction_initial_cap": 0.0989423211127099,
    "mean_contract_rate": 0.04030737661074661,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "price_cap_hits": 3,
    "maximum_relative_cash_error": 1.1565237498713e-15,
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
      "minimum": -0.28049240089652827,
      "maximum": -0.0005824613148617882,
      "mean": -0.1516356409979374,
      "median": -0.1518688312714839,
      "quantile_05": -0.2639052003950917,
      "quantile_95": -0.013062592665680191
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
      "minimum": 0.24717540580492128,
      "maximum": 0.8147682855173407,
      "mean": 0.5326298254077212,
      "median": 0.538402410287129,
      "quantile_05": 0.3084897062190278,
      "quantile_95": 0.7722084618269156
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
        "daily_volatility": 0.022516765653758698,
        "excess_kurtosis": 8.144573616952417,
        "return_acf_1": -0.28049240089652827,
        "abs_return_acf_1": 0.4777231588952304,
        "abs_return_acf_5": 0.38871387510377736,
        "abs_return_acf_20": 0.32631209240344894,
        "quantile_01": -0.08360940829843709,
        "quantile_99": 0.06715984360847119,
        "hill_tail_index": 3.29591015396405
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.0228669923797605,
        "excess_kurtosis": 18.661450550362776,
        "return_acf_1": -0.1940950242511662,
        "abs_return_acf_1": 0.39029245575907284,
        "abs_return_acf_5": 0.3290347834798406,
        "abs_return_acf_20": 0.2537308560846116,
        "quantile_01": -0.07752397437308671,
        "quantile_99": 0.05440425008471236,
        "hill_tail_index": 2.537463151973524
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023049117876432074,
        "excess_kurtosis": 16.912686438598726,
        "return_acf_1": -0.10858064740026602,
        "abs_return_acf_1": 0.3871336441729016,
        "abs_return_acf_5": 0.40851289874674795,
        "abs_return_acf_20": 0.2757146251025604,
        "quantile_01": -0.08492268148556227,
        "quantile_99": 0.06512815330891962,
        "hill_tail_index": 2.7361301899415005
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02366494837179318,
        "excess_kurtosis": 10.972014324256257,
        "return_acf_1": -0.24768026265539356,
        "abs_return_acf_1": 0.3498554096462337,
        "abs_return_acf_5": 0.35628391342098886,
        "abs_return_acf_20": 0.30057674066779355,
        "quantile_01": -0.07775112180875135,
        "quantile_99": 0.06240086773870394,
        "hill_tail_index": 3.1791224963574436
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018563769745354185,
        "excess_kurtosis": 8.451460320583486,
        "return_acf_1": -0.0005824613148617882,
        "abs_return_acf_1": 0.35515450034533286,
        "abs_return_acf_5": 0.3883017984008835,
        "abs_return_acf_20": 0.2824536578540582,
        "quantile_01": -0.05893407994242856,
        "quantile_99": 0.05259762262552501,
        "hill_tail_index": 3.2041544405805995
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021436387696525193,
        "excess_kurtosis": 12.476115661235868,
        "return_acf_1": -0.14991577227984024,
        "abs_return_acf_1": 0.36457140736970794,
        "abs_return_acf_5": 0.3617807505224403,
        "abs_return_acf_20": 0.33059523526921897,
        "quantile_01": -0.07524146156076549,
        "quantile_99": 0.05689772765184185,
        "hill_tail_index": 2.6331455283929888
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0244438453280446,
        "excess_kurtosis": 11.813142350080234,
        "return_acf_1": -0.20355444770189857,
        "abs_return_acf_1": 0.399663538817984,
        "abs_return_acf_5": 0.35343078947181694,
        "abs_return_acf_20": 0.27679660584004956,
        "quantile_01": -0.07738431381508136,
        "quantile_99": 0.07105471627492055,
        "hill_tail_index": 3.4164244740257357
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.0251426809619235,
        "excess_kurtosis": 14.163557348375619,
        "return_acf_1": -0.20052715300218044,
        "abs_return_acf_1": 0.4515742096363353,
        "abs_return_acf_5": 0.38975002237329875,
        "abs_return_acf_20": 0.32652794594056656,
        "quantile_01": -0.08514175904648404,
        "quantile_99": 0.07436815685189717,
        "hill_tail_index": 2.747906482737868
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.015992502985200788,
        "excess_kurtosis": 3.4920993769434974,
        "return_acf_1": -0.10516001343294659,
        "abs_return_acf_1": 0.159326491586082,
        "abs_return_acf_5": 0.20119612995036942,
        "abs_return_acf_20": 0.19603108019664317,
        "quantile_01": -0.042000876232312585,
        "quantile_99": 0.04150281924428894,
        "hill_tail_index": 3.3951997882748035
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018258525675625224,
        "excess_kurtosis": 6.758310741991087,
        "return_acf_1": -0.012609920972395411,
        "abs_return_acf_1": 0.21374108951160029,
        "abs_return_acf_5": 0.34920248797522124,
        "abs_return_acf_20": 0.18135448395366185,
        "quantile_01": -0.056687993118213736,
        "quantile_99": 0.04641107147889659,
        "hill_tail_index": 2.6944451704518784
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.015507569305886563,
        "excess_kurtosis": 3.6055682953013015,
        "return_acf_1": -0.1427745359845781,
        "abs_return_acf_1": 0.26754251915760896,
        "abs_return_acf_5": 0.20073729176011978,
        "abs_return_acf_20": 0.19367301691943525,
        "quantile_01": -0.041853248374962876,
        "quantile_99": 0.04817920073419312,
        "hill_tail_index": 4.191796515117769
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024942434888536938,
        "excess_kurtosis": 22.290829750129838,
        "return_acf_1": -0.09754897927613643,
        "abs_return_acf_1": 0.42390858660645814,
        "abs_return_acf_5": 0.46118138954877885,
        "abs_return_acf_20": 0.3347282610726065,
        "quantile_01": -0.07494240789551823,
        "quantile_99": 0.0839566279790509,
        "hill_tail_index": 2.521040615800054
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02393568670152253,
        "excess_kurtosis": 14.82071677580473,
        "return_acf_1": -0.18858560988610779,
        "abs_return_acf_1": 0.37356206014374665,
        "abs_return_acf_5": 0.41140495373026525,
        "abs_return_acf_20": 0.34119266887141847,
        "quantile_01": -0.07720977765443558,
        "quantile_99": 0.06555428246862631,
        "hill_tail_index": 2.246677763164925
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02388277988341532,
        "excess_kurtosis": 17.81671779361834,
        "return_acf_1": -0.21750681885313233,
        "abs_return_acf_1": 0.42334765606908886,
        "abs_return_acf_5": 0.3631810913167645,
        "abs_return_acf_20": 0.27975988966448073,
        "quantile_01": -0.0780119844597114,
        "quantile_99": 0.06390590185190836,
        "hill_tail_index": 2.399002881305282
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022913441339213327,
        "excess_kurtosis": 11.238993183417,
        "return_acf_1": -0.2771801494548447,
        "abs_return_acf_1": 0.46211732694107993,
        "abs_return_acf_5": 0.40411134881918276,
        "abs_return_acf_20": 0.30379407307767015,
        "quantile_01": -0.08535698305817842,
        "quantile_99": 0.06369748450901835,
        "hill_tail_index": 2.930852064049083
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01710824491233668,
        "excess_kurtosis": 2.7111520118831542,
        "return_acf_1": -0.056662735030164266,
        "abs_return_acf_1": 0.27131906224970426,
        "abs_return_acf_5": 0.2632650578092574,
        "abs_return_acf_20": 0.1812555160441724,
        "quantile_01": -0.04883028789342814,
        "quantile_99": 0.04414397744885324,
        "hill_tail_index": 4.425925356588231
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02273924104799703,
        "excess_kurtosis": 17.003985469983146,
        "return_acf_1": -0.11858594996671692,
        "abs_return_acf_1": 0.3708149267480575,
        "abs_return_acf_5": 0.3651899597680402,
        "abs_return_acf_20": 0.3217834148130297,
        "quantile_01": -0.07912193058984927,
        "quantile_99": 0.06552529204736607,
        "hill_tail_index": 2.800183396253764
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021792315995112766,
        "excess_kurtosis": 11.313083480654726,
        "return_acf_1": -0.18556203116289166,
        "abs_return_acf_1": 0.2932653338638878,
        "abs_return_acf_5": 0.32207480870138055,
        "abs_return_acf_20": 0.23888229930073526,
        "quantile_01": -0.07552352674220024,
        "quantile_99": 0.05733241998454871,
        "hill_tail_index": 2.8836400133588866
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.022531505327481115,
        "excess_kurtosis": 5.934548201214778,
        "return_acf_1": -0.1942405803913531,
        "abs_return_acf_1": 0.3293455040795293,
        "abs_return_acf_5": 0.3043458231933315,
        "abs_return_acf_20": 0.3257501426347437,
        "quantile_01": -0.0703408910660878,
        "quantile_99": 0.06073690577016062,
        "hill_tail_index": 4.019938654657385
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022399035258287948,
        "excess_kurtosis": 21.673387204504877,
        "return_acf_1": -0.12718187480646512,
        "abs_return_acf_1": 0.35304092523671576,
        "abs_return_acf_5": 0.37876280442789007,
        "abs_return_acf_20": 0.31237147126544507,
        "quantile_01": -0.07573230893301997,
        "quantile_99": 0.06506149754606978,
        "hill_tail_index": 3.5231523811266166
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01746143880171105,
        "excess_kurtosis": 3.212145928180001,
        "return_acf_1": -0.06984082548468344,
        "abs_return_acf_1": 0.2427671463098375,
        "abs_return_acf_5": 0.28561380438107026,
        "abs_return_acf_20": 0.2671344806299827,
        "quantile_01": -0.05242354804184423,
        "quantile_99": 0.04766204911762358,
        "hill_tail_index": 4.128395362431965
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.023884562418368543,
        "excess_kurtosis": 21.28935893425842,
        "return_acf_1": -0.12835736159069325,
        "abs_return_acf_1": 0.41164859721994335,
        "abs_return_acf_5": 0.396879165943566,
        "abs_return_acf_20": 0.24627174438847804,
        "quantile_01": -0.08113756256720808,
        "quantile_99": 0.060179205988361725,
        "hill_tail_index": 2.242687050254002
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023866689447465037,
        "excess_kurtosis": 23.812969587066277,
        "return_acf_1": -0.15009910758208134,
        "abs_return_acf_1": 0.4390289905615965,
        "abs_return_acf_5": 0.36454467077125247,
        "abs_return_acf_20": 0.2603247418528478,
        "quantile_01": -0.07782742651169543,
        "quantile_99": 0.06445200727606712,
        "hill_tail_index": 2.611847928478067
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02519380500154578,
        "excess_kurtosis": 15.795576091155812,
        "return_acf_1": -0.2276315247926035,
        "abs_return_acf_1": 0.4480619164675129,
        "abs_return_acf_5": 0.4801836766353671,
        "abs_return_acf_20": 0.322093038434235,
        "quantile_01": -0.09301936096591643,
        "quantile_99": 0.06272743487305187,
        "hill_tail_index": 2.964079284232874
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01658661196078696,
        "excess_kurtosis": 3.45117965949522,
        "return_acf_1": -0.11566083237952603,
        "abs_return_acf_1": 0.26908313247422877,
        "abs_return_acf_5": 0.2612395703876528,
        "abs_return_acf_20": 0.24362304828279438,
        "quantile_01": -0.04637417739648597,
        "quantile_99": 0.04493827279183661,
        "hill_tail_index": 3.757517996687342
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022649257810661443,
        "excess_kurtosis": 14.955710323071173,
        "return_acf_1": -0.18559073523973843,
        "abs_return_acf_1": 0.32281814816654086,
        "abs_return_acf_5": 0.4015418573995833,
        "abs_return_acf_20": 0.25175642722203895,
        "quantile_01": -0.06952260924852725,
        "quantile_99": 0.059680012260684874,
        "hill_tail_index": 3.075647667405882
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022089174481283575,
        "excess_kurtosis": 13.184112838779424,
        "return_acf_1": -0.1802151232415592,
        "abs_return_acf_1": 0.3346009844472862,
        "abs_return_acf_5": 0.3150211621277004,
        "abs_return_acf_20": 0.22401440960530014,
        "quantile_01": -0.08281112311996668,
        "quantile_99": 0.055916079006057544,
        "hill_tail_index": 2.9214383734125966
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01676201447948726,
        "excess_kurtosis": 4.575574694484658,
        "return_acf_1": -0.013615858068583807,
        "abs_return_acf_1": 0.2444750849410646,
        "abs_return_acf_5": 0.21024281231524325,
        "abs_return_acf_20": 0.167518703162637,
        "quantile_01": -0.047456496137404984,
        "quantile_99": 0.04331908059622689,
        "hill_tail_index": 3.4322599791404733
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022874196508132646,
        "excess_kurtosis": 13.221664960756069,
        "return_acf_1": -0.15363855496088646,
        "abs_return_acf_1": 0.37146199668568175,
        "abs_return_acf_5": 0.4212293501557884,
        "abs_return_acf_20": 0.3346515101099605,
        "quantile_01": -0.0730387571628181,
        "quantile_99": 0.06369543351955037,
        "hill_tail_index": 2.6289527239983914
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.026617583952251334,
        "excess_kurtosis": 24.92787521752109,
        "return_acf_1": -0.21539193787789826,
        "abs_return_acf_1": 0.5319602783003698,
        "abs_return_acf_5": 0.397298141774158,
        "abs_return_acf_20": 0.28010433845600047,
        "quantile_01": -0.08315071095996522,
        "quantile_99": 0.06935587355527009,
        "hill_tail_index": 2.282719649295639
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
