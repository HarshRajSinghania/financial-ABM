# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27083
Run ID: `24146f1661f7feebcb315383adc31283468e9fcc7c905e66e43d11d68908427e`
Result fingerprint: `0f9aad54cbff28f593588b67e7b65ca632483e4c7b7109759c7c631f0d6f855d`

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
    "equal_weight_sd": -0.6162142857142824,
    "equal_weight_raw": -9.243214285714235,
    "fixed_start_cap_weight_sd": -0.6561620308701221,
    "fixed_start_cap_weight_raw": -9.842430463051832,
    "end_cap_weight_sd": -0.6386543007164674,
    "end_cap_weight_raw": -9.579814510747012
  },
  "full_period_change": {
    "equal_weight_sd": -0.9367380952380903,
    "equal_weight_raw": -14.051071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8755353835978791,
    "inflation_mean_sd": 0.5235823412698413
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.33616666666666994,
    "equal_weight_raw": 5.042500000000048,
    "fixed_start_cap_weight_sd": 0.2962189215108305,
    "fixed_start_cap_weight_raw": 4.443283822662457,
    "end_cap_weight_sd": 0.31372665166448493,
    "end_cap_weight_raw": 4.705899774967274
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6957142857142825,
      "change_raw": -10.435714285714237,
      "decay_adjusted_gain_sd": 0.25666666666666993
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6259920634920603,
      "change_raw": -9.389880952380905,
      "decay_adjusted_gain_sd": 0.32638888888889217
    },
    "small": {
      "count": 18,
      "change_sd": -0.5980753968253936,
      "change_raw": -8.971130952380904,
      "decay_adjusted_gain_sd": 0.35430555555555876
    },
    "large_minus_small_sd": -0.09763888888888894,
    "large_minus_small_raw": -1.464583333333334
  },
  "inflation": {
    "initial_mean_sd": 0.23183333333333334,
    "final_mean_sd": 0.55175,
    "mean_sd": 0.3924771718012767,
    "mean_absolute_raw_gap": 5.887157577019151,
    "final_absolute_raw_gap": 8.27625,
    "mean_range_fraction": 0.05887157577019151
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.4,
    "initial_wealth_share": 0.24339713964740095,
    "final_wealth_share": 0.37869851120776127
  },
  "pricing_slope": {
    "mean": 0.0017814594701895982,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.2726487837898417,
    "real_improvement_cost": 0.23619346257859952,
    "washing_cost": 0.03645532121124213,
    "fine_transfer": 0.021322782953464646,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2939715667433063,
    "resource_cost_fraction_initial_cap": 0.009088292792994725,
    "private_net_outflow_fraction_initial_cap": 0.009799052224776878,
    "fine_transfer_fraction_initial_cap": 0.000710759431782155,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003021961056831787,
    "unapplied_final_day_resource_cost": 0.0009154857950491721
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 36.988978493935406,
    "beneficial_raw_gain_per_resource_cost": 554.8346774090311,
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
    "accrued_cost": 2.8960654469720692,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.08012502921840686,
    "accrued_cost_fraction_initial_cap": 0.09653551489906899,
    "mean_contract_rate": 0.04001938558794973,
    "maximum_ledger_error": 8.216219588366713e-20
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
    "maximum_relative_cash_error": 1.6487850781396144e-15,
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
      "minimum": -0.24427392851920632,
      "maximum": -0.03330985585667131,
      "mean": -0.15073609322331613,
      "median": -0.1524301475623167,
      "quantile_05": -0.2365381808016709,
      "quantile_95": -0.05807384906026368
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
      "minimum": 0.23244538189184624,
      "maximum": 0.8119195417931728,
      "mean": 0.5470161170578194,
      "median": 0.6548121484219828,
      "quantile_05": 0.2746578116439392,
      "quantile_95": 0.7766350800679351
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
        "daily_volatility": 0.021161431511628543,
        "excess_kurtosis": 14.66973404292267,
        "return_acf_1": -0.13905690940263224,
        "abs_return_acf_1": 0.4436668748756566,
        "abs_return_acf_5": 0.398935681995301,
        "abs_return_acf_20": 0.26966620881683523,
        "quantile_01": -0.07166076537337264,
        "quantile_99": 0.05565378487157077,
        "hill_tail_index": 2.8543219161505413
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020432929351000505,
        "excess_kurtosis": 16.677577398673424,
        "return_acf_1": -0.17394188789877105,
        "abs_return_acf_1": 0.446666878761833,
        "abs_return_acf_5": 0.425583970364485,
        "abs_return_acf_20": 0.3470926566841561,
        "quantile_01": -0.0656612782960498,
        "quantile_99": 0.06360496731298194,
        "hill_tail_index": 2.612711631680966
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020711988153694166,
        "excess_kurtosis": 15.03583264446327,
        "return_acf_1": -0.15821614914993895,
        "abs_return_acf_1": 0.41665119558759106,
        "abs_return_acf_5": 0.42257480592241364,
        "abs_return_acf_20": 0.3274996360367247,
        "quantile_01": -0.07158139691932086,
        "quantile_99": 0.059593965570134175,
        "hill_tail_index": 3.063890125675997
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02119907033287729,
        "excess_kurtosis": 16.60117318415183,
        "return_acf_1": -0.19359828936977147,
        "abs_return_acf_1": 0.5004003769093766,
        "abs_return_acf_5": 0.528018121702082,
        "abs_return_acf_20": 0.2910424182113604,
        "quantile_01": -0.06999660474100869,
        "quantile_99": 0.04766285228896833,
        "hill_tail_index": 1.8881170448033677
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018736232279891796,
        "excess_kurtosis": 4.9584610006050935,
        "return_acf_1": -0.14322624751449883,
        "abs_return_acf_1": 0.35040069624374187,
        "abs_return_acf_5": 0.28026045449090886,
        "abs_return_acf_20": 0.2395665645453382,
        "quantile_01": -0.048435909072324805,
        "quantile_99": 0.056964564352218326,
        "hill_tail_index": 3.2898561036558105
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02209244496737988,
        "excess_kurtosis": 16.530523716842623,
        "return_acf_1": -0.18385076698692848,
        "abs_return_acf_1": 0.5298250826841266,
        "abs_return_acf_5": 0.45895838472147227,
        "abs_return_acf_20": 0.3601610629602622,
        "quantile_01": -0.07317842173602444,
        "quantile_99": 0.06197620993057008,
        "hill_tail_index": 2.8537726009144695
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018384484118660206,
        "excess_kurtosis": 6.358617070554477,
        "return_acf_1": -0.09260953453840355,
        "abs_return_acf_1": 0.28592644633260245,
        "abs_return_acf_5": 0.35679153505461647,
        "abs_return_acf_20": 0.22319329006363903,
        "quantile_01": -0.062163725672730374,
        "quantile_99": 0.05297902848924067,
        "hill_tail_index": 3.6071264505051444
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019615812355054586,
        "excess_kurtosis": 7.57603755846886,
        "return_acf_1": -0.17559450187854186,
        "abs_return_acf_1": 0.35704679820674556,
        "abs_return_acf_5": 0.34040690032478443,
        "abs_return_acf_20": 0.3032391585026176,
        "quantile_01": -0.05349611803498232,
        "quantile_99": 0.06625056455397811,
        "hill_tail_index": 3.266426745112701
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017282412565083057,
        "excess_kurtosis": 4.763900297189595,
        "return_acf_1": -0.03330985585667131,
        "abs_return_acf_1": 0.24215092727607113,
        "abs_return_acf_5": 0.24022753611673545,
        "abs_return_acf_20": 0.16694672859270232,
        "quantile_01": -0.05278971432678276,
        "quantile_99": 0.05005649813116631,
        "hill_tail_index": 3.496658822991425
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016365127854625905,
        "excess_kurtosis": 1.4821726186666089,
        "return_acf_1": -0.11986160255495404,
        "abs_return_acf_1": 0.24284291435470182,
        "abs_return_acf_5": 0.17849713786398178,
        "abs_return_acf_20": 0.11876900995147904,
        "quantile_01": -0.04355943981257436,
        "quantile_99": 0.04115617439300823,
        "hill_tail_index": 4.63315001877251
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021323300263928615,
        "excess_kurtosis": 12.973661872253404,
        "return_acf_1": -0.24427392851920632,
        "abs_return_acf_1": 0.5042855142204709,
        "abs_return_acf_5": 0.5354991839745114,
        "abs_return_acf_20": 0.38293370053019593,
        "quantile_01": -0.07395498210166318,
        "quantile_99": 0.05699113035842631,
        "hill_tail_index": 3.0593353412952586
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021164245165071417,
        "excess_kurtosis": 11.764652617731565,
        "return_acf_1": -0.19008535517805167,
        "abs_return_acf_1": 0.5659579849500206,
        "abs_return_acf_5": 0.4774332572799712,
        "abs_return_acf_20": 0.437451666342244,
        "quantile_01": -0.07866662317256125,
        "quantile_99": 0.05774512785415132,
        "hill_tail_index": 2.877210254060052
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021327730136420326,
        "excess_kurtosis": 12.5117300358791,
        "return_acf_1": -0.23564621327761393,
        "abs_return_acf_1": 0.5202615287943362,
        "abs_return_acf_5": 0.4915591708544851,
        "abs_return_acf_20": 0.4182690976420799,
        "quantile_01": -0.07705025299752621,
        "quantile_99": 0.06243949899209754,
        "hill_tail_index": 2.731769042912228
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018050864302109317,
        "excess_kurtosis": 8.996271450794772,
        "return_acf_1": -0.1588786996187224,
        "abs_return_acf_1": 0.44536749226500977,
        "abs_return_acf_5": 0.289602802073233,
        "abs_return_acf_20": 0.262368353847369,
        "quantile_01": -0.05129261890376823,
        "quantile_99": 0.04730976696562621,
        "hill_tail_index": 2.9436330874484007
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019391217701149783,
        "excess_kurtosis": 13.319248588439017,
        "return_acf_1": -0.14431343763424243,
        "abs_return_acf_1": 0.3819045998536389,
        "abs_return_acf_5": 0.33227135647170897,
        "abs_return_acf_20": 0.26275032798586373,
        "quantile_01": -0.060419281251258734,
        "quantile_99": 0.04865571317217409,
        "hill_tail_index": 3.0848198259882476
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018932146481928824,
        "excess_kurtosis": 12.782751908022965,
        "return_acf_1": -0.1684951880483646,
        "abs_return_acf_1": 0.4503508790702276,
        "abs_return_acf_5": 0.39841448282315794,
        "abs_return_acf_20": 0.27653255699398255,
        "quantile_01": -0.06620872094266543,
        "quantile_99": 0.04450087104429987,
        "hill_tail_index": 2.4181903127376163
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020970537151639306,
        "excess_kurtosis": 13.661159117541313,
        "return_acf_1": -0.1526216008079736,
        "abs_return_acf_1": 0.4758504416965743,
        "abs_return_acf_5": 0.4637056252414549,
        "abs_return_acf_20": 0.34385109149082665,
        "quantile_01": -0.06852258408795421,
        "quantile_99": 0.051645001426612915,
        "hill_tail_index": 2.103234934426051
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020823304718878867,
        "excess_kurtosis": 19.02282732244709,
        "return_acf_1": -0.041568127084411745,
        "abs_return_acf_1": 0.421680062238959,
        "abs_return_acf_5": 0.4407903712439244,
        "abs_return_acf_20": 0.2570617476686327,
        "quantile_01": -0.07034038406117318,
        "quantile_99": 0.04691981193303878,
        "hill_tail_index": 2.2425889315767047
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018266631186630633,
        "excess_kurtosis": 8.356839862848574,
        "return_acf_1": -0.1522386943166598,
        "abs_return_acf_1": 0.3353125913464955,
        "abs_return_acf_5": 0.2795847334392569,
        "abs_return_acf_20": 0.2686017957956565,
        "quantile_01": -0.05165318441644834,
        "quantile_99": 0.04680484293583147,
        "hill_tail_index": 2.9541723224123797
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02017115820183827,
        "excess_kurtosis": 9.13240206108183,
        "return_acf_1": -0.09526079846057993,
        "abs_return_acf_1": 0.4140428839092282,
        "abs_return_acf_5": 0.4451136996621455,
        "abs_return_acf_20": 0.27346661189391763,
        "quantile_01": -0.07228652794902903,
        "quantile_99": 0.05908233132027471,
        "hill_tail_index": 3.522853886174633
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021726891864343997,
        "excess_kurtosis": 15.311266085480991,
        "return_acf_1": -0.1848555450808459,
        "abs_return_acf_1": 0.47379943650640993,
        "abs_return_acf_5": 0.44881180962305267,
        "abs_return_acf_20": 0.3119456950441769,
        "quantile_01": -0.07868726060968244,
        "quantile_99": 0.057178651391105305,
        "hill_tail_index": 3.7558661654025465
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0190281046610697,
        "excess_kurtosis": 5.866462979043426,
        "return_acf_1": -0.13122292465406485,
        "abs_return_acf_1": 0.3213012120897298,
        "abs_return_acf_5": 0.33843343519157953,
        "abs_return_acf_20": 0.3076881114065688,
        "quantile_01": -0.05878947742433047,
        "quantile_99": 0.05340804394536627,
        "hill_tail_index": 3.5416793803266806
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018191904568907933,
        "excess_kurtosis": 4.965950608183484,
        "return_acf_1": -0.10243529046370009,
        "abs_return_acf_1": 0.31081544589652527,
        "abs_return_acf_5": 0.3163871780170239,
        "abs_return_acf_20": 0.2803326525649593,
        "quantile_01": -0.057189587558181376,
        "quantile_99": 0.051190314274525875,
        "hill_tail_index": 3.3192731180566346
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01875573708169663,
        "excess_kurtosis": 6.161843489469026,
        "return_acf_1": -0.15079966356127858,
        "abs_return_acf_1": 0.33932539596112254,
        "abs_return_acf_5": 0.3908222268973576,
        "abs_return_acf_20": 0.3184036423557308,
        "quantile_01": -0.06084870628508219,
        "quantile_99": 0.04824966376630994,
        "hill_tail_index": 3.273670599995706
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019269221477095623,
        "excess_kurtosis": 8.36427966538794,
        "return_acf_1": -0.20065543038759645,
        "abs_return_acf_1": 0.30340178513107013,
        "abs_return_acf_5": 0.28387900287083656,
        "abs_return_acf_20": 0.21624516690799486,
        "quantile_01": -0.05813562017178706,
        "quantile_99": 0.0586436368548529,
        "hill_tail_index": 3.3292001620695446
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02064705635176257,
        "excess_kurtosis": 10.785456175988735,
        "return_acf_1": -0.1488606451973339,
        "abs_return_acf_1": 0.4082364209583013,
        "abs_return_acf_5": 0.43028770765389596,
        "abs_return_acf_20": 0.31270676510659295,
        "quantile_01": -0.07117312204073228,
        "quantile_99": 0.057119979323299104,
        "hill_tail_index": 2.79068958994204
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01946627987683835,
        "excess_kurtosis": 17.145397818616672,
        "return_acf_1": -0.12559213070597566,
        "abs_return_acf_1": 0.43014288287443353,
        "abs_return_acf_5": 0.42019554991982,
        "abs_return_acf_20": 0.31640463097336885,
        "quantile_01": -0.07018985316383264,
        "quantile_99": 0.04387762005697995,
        "hill_tail_index": 2.075448089924274
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02075430427367358,
        "excess_kurtosis": 11.160683030923023,
        "return_acf_1": -0.23726797241226297,
        "abs_return_acf_1": 0.5019560662080356,
        "abs_return_acf_5": 0.47947682785971796,
        "abs_return_acf_20": 0.34526150817741463,
        "quantile_01": -0.07147914389105885,
        "quantile_99": 0.060915130809987776,
        "hill_tail_index": 2.8132864521133163
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0188921782111198,
        "excess_kurtosis": 9.992786851475485,
        "return_acf_1": -0.07824750925297137,
        "abs_return_acf_1": 0.4365358949354697,
        "abs_return_acf_5": 0.3953316226428394,
        "abs_return_acf_20": 0.26804991672655093,
        "quantile_01": -0.06501046929847887,
        "quantile_99": 0.05322756340900543,
        "hill_tail_index": 3.2537782043193624
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020175257797231737,
        "excess_kurtosis": 11.992481244068522,
        "return_acf_1": -0.16549789688651606,
        "abs_return_acf_1": 0.40489617152215557,
        "abs_return_acf_5": 0.39131544109929645,
        "abs_return_acf_20": 0.25407476624862185,
        "quantile_01": -0.0670297609595407,
        "quantile_99": 0.049260366292339826,
        "hill_tail_index": 2.4335450928559776
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
