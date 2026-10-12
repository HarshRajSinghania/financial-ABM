# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27044
Run ID: `21d4d458be4e8a51b5bc0be7260bc12926e7803085658ff263fa245b393bd956`
Result fingerprint: `6b7b6d0c4151b4fc50f9474ad5680017354880521822df4f93a0257203df45b6`

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
    "equal_weight_sd": -0.5212142857142825,
    "equal_weight_raw": -7.8182142857142365,
    "fixed_start_cap_weight_sd": -0.5714008928295831,
    "fixed_start_cap_weight_raw": -8.571013392443746,
    "end_cap_weight_sd": -0.5751890704373679,
    "end_cap_weight_raw": -8.627836056560518
  },
  "full_period_change": {
    "equal_weight_sd": -0.8659880952380904,
    "equal_weight_raw": -12.989821428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8143293650793607,
    "inflation_mean_sd": 0.7083991402116402
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.43116666666666975,
    "equal_weight_raw": 6.467500000000046,
    "fixed_start_cap_weight_sd": 0.3809800595513694,
    "fixed_start_cap_weight_raw": 5.714700893270539,
    "end_cap_weight_sd": 0.3771918819435843,
    "end_cap_weight_raw": 5.6578782291537655
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5348809523809491,
      "change_raw": -8.023214285714237,
      "decay_adjusted_gain_sd": 0.41750000000000315
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4846031746031713,
      "change_raw": -7.26904761904757,
      "decay_adjusted_gain_sd": 0.467777777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.5372420634920604,
      "change_raw": -8.058630952380906,
      "decay_adjusted_gain_sd": 0.41513888888889205
    },
    "large_minus_small_sd": 0.002361111111111258,
    "large_minus_small_raw": 0.03541666666666887
  },
  "inflation": {
    "initial_mean_sd": 0.25541666666666674,
    "final_mean_sd": 0.7509999999999999,
    "mean_sd": 0.5185117957257841,
    "mean_absolute_raw_gap": 7.7776769358867615,
    "final_absolute_raw_gap": 11.265000000000004,
    "mean_range_fraction": 0.07777676935886761
  },
  "impact": {
    "initial_share": 0.15333333333333332,
    "final_share": 0.24,
    "initial_wealth_share": 0.13594130760225695,
    "final_wealth_share": 0.22530464706805356
  },
  "pricing_slope": {
    "mean": -0.00030755135301069287,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.04530224562617614,
    "real_improvement_cost": 0.024557558867393196,
    "washing_cost": 0.020744686758782944,
    "fine_transfer": 0.007631796339377895,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.052934041965554034,
    "resource_cost_fraction_initial_cap": 0.0015100748542058713,
    "private_net_outflow_fraction_initial_cap": 0.0017644680655184678,
    "fine_transfer_fraction_initial_cap": 0.0002543932113125965,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.017350048178687596,
    "unapplied_final_day_resource_cost": 0.0013511019486753969
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 285.526684631415,
    "beneficial_raw_gain_per_resource_cost": 4282.900269471225,
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
    "accrued_cost": 3.2423926505669725,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.2662021743764966,
    "accrued_cost_fraction_initial_cap": 0.10807975501889908,
    "mean_contract_rate": 0.04267885501978073,
    "maximum_ledger_error": 3.2526065174565133e-19
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
    "price_cap_hits": 2,
    "maximum_relative_cash_error": 1.2333700563026483e-15,
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
      "minimum": -0.24976398390763696,
      "maximum": -0.08518524874034757,
      "mean": -0.18577442631781557,
      "median": -0.19236949964489164,
      "quantile_05": -0.23962638085022944,
      "quantile_95": -0.11987453379143591
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
      "minimum": 0.2912023409924477,
      "maximum": 0.7683086216993064,
      "mean": 0.5253478152779576,
      "median": 0.5071236866691605,
      "quantile_05": 0.3471077982596928,
      "quantile_95": 0.728521468772167
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
        "daily_volatility": 0.018661217176220588,
        "excess_kurtosis": 7.72249873314067,
        "return_acf_1": -0.23166655409260625,
        "abs_return_acf_1": 0.32097786701122616,
        "abs_return_acf_5": 0.2902420663095638,
        "abs_return_acf_20": 0.21037972609333686,
        "quantile_01": -0.054034074504518456,
        "quantile_99": 0.04365840298080175,
        "hill_tail_index": 2.797270297751417
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020407312360226373,
        "excess_kurtosis": 11.531439799536399,
        "return_acf_1": -0.21107467969817958,
        "abs_return_acf_1": 0.3880199654888699,
        "abs_return_acf_5": 0.31838667093680345,
        "abs_return_acf_20": 0.23339688015388957,
        "quantile_01": -0.0606593059895781,
        "quantile_99": 0.062451112895197475,
        "hill_tail_index": 2.8781283903728028
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01841426066533588,
        "excess_kurtosis": 5.424841900750749,
        "return_acf_1": -0.23903755206377697,
        "abs_return_acf_1": 0.28208884365089937,
        "abs_return_acf_5": 0.3402902144253896,
        "abs_return_acf_20": 0.19639110733918608,
        "quantile_01": -0.05749247656237833,
        "quantile_99": 0.0480104202676712,
        "hill_tail_index": 4.30692148033392
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0194063010132109,
        "excess_kurtosis": 6.116294464659921,
        "return_acf_1": -0.16139759520980285,
        "abs_return_acf_1": 0.38554568354604485,
        "abs_return_acf_5": 0.35055259247322784,
        "abs_return_acf_20": 0.3223481606169183,
        "quantile_01": -0.06623584015467777,
        "quantile_99": 0.05448364840868453,
        "hill_tail_index": 3.6800833320854025
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018627930433522625,
        "excess_kurtosis": 6.825770292772399,
        "return_acf_1": -0.18131742582871205,
        "abs_return_acf_1": 0.3433636913484288,
        "abs_return_acf_5": 0.3048595299358961,
        "abs_return_acf_20": 0.21764091728406418,
        "quantile_01": -0.05834485725925271,
        "quantile_99": 0.04712752540108032,
        "hill_tail_index": 3.509769023251954
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01861165780299661,
        "excess_kurtosis": 3.7789299218762924,
        "return_acf_1": -0.15866722066338906,
        "abs_return_acf_1": 0.27079415084863756,
        "abs_return_acf_5": 0.3035047347686709,
        "abs_return_acf_20": 0.20019196021921074,
        "quantile_01": -0.05950977757844169,
        "quantile_99": 0.05566155043221948,
        "hill_tail_index": 5.46411611071436
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01741836549866876,
        "excess_kurtosis": 3.566927252270972,
        "return_acf_1": -0.1939281428798119,
        "abs_return_acf_1": 0.2524362488980543,
        "abs_return_acf_5": 0.23687728135879835,
        "abs_return_acf_20": 0.23335331512369023,
        "quantile_01": -0.05261151732915725,
        "quantile_99": 0.04112509185201757,
        "hill_tail_index": 3.4405323916490698
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01874704299071266,
        "excess_kurtosis": 5.925229846813041,
        "return_acf_1": -0.20940282693525922,
        "abs_return_acf_1": 0.36795084994541305,
        "abs_return_acf_5": 0.3234745530252877,
        "abs_return_acf_20": 0.29292723779344954,
        "quantile_01": -0.058167001556455794,
        "quantile_99": 0.056161378184500316,
        "hill_tail_index": 3.776995204952784
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017674830067096355,
        "excess_kurtosis": 5.453534799330791,
        "return_acf_1": -0.17568627713817972,
        "abs_return_acf_1": 0.31523401838093623,
        "abs_return_acf_5": 0.2973996771633471,
        "abs_return_acf_20": 0.17276345273007568,
        "quantile_01": -0.054072758508241274,
        "quantile_99": 0.04292507470920024,
        "hill_tail_index": 3.0083155266572277
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0188826036645244,
        "excess_kurtosis": 5.018386021498179,
        "return_acf_1": -0.19081085640997136,
        "abs_return_acf_1": 0.29442679353402984,
        "abs_return_acf_5": 0.2555727543142583,
        "abs_return_acf_20": 0.27041796936344137,
        "quantile_01": -0.05885363454260999,
        "quantile_99": 0.049437832767224014,
        "hill_tail_index": 3.332216851639372
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017069001834997374,
        "excess_kurtosis": 4.622274975619335,
        "return_acf_1": -0.17813624054332253,
        "abs_return_acf_1": 0.3058862345627619,
        "abs_return_acf_5": 0.23598899677702434,
        "abs_return_acf_20": 0.2465229008727347,
        "quantile_01": -0.05401812527285034,
        "quantile_99": 0.04014012847765037,
        "hill_tail_index": 2.8243008029383474
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018645664993485567,
        "excess_kurtosis": 9.279292521738938,
        "return_acf_1": -0.24976398390763696,
        "abs_return_acf_1": 0.30092170105201754,
        "abs_return_acf_5": 0.22986904121859475,
        "abs_return_acf_20": 0.2135829181403094,
        "quantile_01": -0.0555552489881558,
        "quantile_99": 0.05106422951201023,
        "hill_tail_index": 3.2830813340697538
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02025707552023312,
        "excess_kurtosis": 15.720901876530466,
        "return_acf_1": -0.20191344978621253,
        "abs_return_acf_1": 0.3865939707859085,
        "abs_return_acf_5": 0.3808991585268594,
        "abs_return_acf_20": 0.21619105798475954,
        "quantile_01": -0.05870162536329399,
        "quantile_99": 0.052599090771554585,
        "hill_tail_index": 2.130665782431705
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017224485906193618,
        "excess_kurtosis": 4.459994343304874,
        "return_acf_1": -0.1592766259679064,
        "abs_return_acf_1": 0.2710891490767051,
        "abs_return_acf_5": 0.22407547840968473,
        "abs_return_acf_20": 0.21938822561689741,
        "quantile_01": -0.04720768649140594,
        "quantile_99": 0.04937767328007376,
        "hill_tail_index": 3.3995320321065665
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018789719743735913,
        "excess_kurtosis": 3.324179107270141,
        "return_acf_1": -0.20058197832760713,
        "abs_return_acf_1": 0.30244387706860115,
        "abs_return_acf_5": 0.2798936643784294,
        "abs_return_acf_20": 0.25958876356622584,
        "quantile_01": -0.06225931559814745,
        "quantile_99": 0.049901644145348,
        "hill_tail_index": 4.273396414238383
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019798303833798665,
        "excess_kurtosis": 15.970114981361334,
        "return_acf_1": -0.12145778373773103,
        "abs_return_acf_1": 0.3040666700677056,
        "abs_return_acf_5": 0.2777484688312408,
        "abs_return_acf_20": 0.2841656962711743,
        "quantile_01": -0.05543786649852117,
        "quantile_99": 0.05379491577616481,
        "hill_tail_index": 3.04316327953386
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018891979188018757,
        "excess_kurtosis": 4.892979002806811,
        "return_acf_1": -0.2167646003628185,
        "abs_return_acf_1": 0.3015965808995298,
        "abs_return_acf_5": 0.2696186617882521,
        "abs_return_acf_20": 0.27354436311868924,
        "quantile_01": -0.054345701820501094,
        "quantile_99": 0.04743774609859461,
        "hill_tail_index": 3.5115695352894805
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017770752313785915,
        "excess_kurtosis": 7.6072116663015645,
        "return_acf_1": -0.20232221563591804,
        "abs_return_acf_1": 0.28057727582817305,
        "abs_return_acf_5": 0.30701571338026595,
        "abs_return_acf_20": 0.19715381932548343,
        "quantile_01": -0.05423246904736767,
        "quantile_99": 0.05017178590092579,
        "hill_tail_index": 3.443557395094686
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018312927572406806,
        "excess_kurtosis": 4.390714395795333,
        "return_acf_1": -0.16269818759342602,
        "abs_return_acf_1": 0.312568304613145,
        "abs_return_acf_5": 0.3197985699961289,
        "abs_return_acf_20": 0.25021987943303486,
        "quantile_01": -0.05472774814127961,
        "quantile_99": 0.05153401952114147,
        "hill_tail_index": 4.226969825219555
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019278543036100312,
        "excess_kurtosis": 6.4097002686286455,
        "return_acf_1": -0.11857914747173988,
        "abs_return_acf_1": 0.39200514565117633,
        "abs_return_acf_5": 0.32256380599360707,
        "abs_return_acf_20": 0.3164277813657931,
        "quantile_01": -0.05854950111316332,
        "quantile_99": 0.05365804207528169,
        "hill_tail_index": 3.510621288162129
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018350608908650576,
        "excess_kurtosis": 5.579319342697346,
        "return_acf_1": -0.2014635841435716,
        "abs_return_acf_1": 0.2648497435039361,
        "abs_return_acf_5": 0.21830813797039644,
        "abs_return_acf_20": 0.22613522342988363,
        "quantile_01": -0.054765348842681465,
        "quantile_99": 0.0583280838607584,
        "hill_tail_index": 3.5616461817985203
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01826472240198207,
        "excess_kurtosis": 5.5703498462826,
        "return_acf_1": -0.18313579513404316,
        "abs_return_acf_1": 0.28968842267007905,
        "abs_return_acf_5": 0.23015592037755891,
        "abs_return_acf_20": 0.2369086878593881,
        "quantile_01": -0.060359576635304786,
        "quantile_99": 0.049740217890513125,
        "hill_tail_index": 3.497859810537995
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017833082564871133,
        "excess_kurtosis": 5.6712910796854015,
        "return_acf_1": -0.1833301470348746,
        "abs_return_acf_1": 0.3155977778919955,
        "abs_return_acf_5": 0.27905860572599006,
        "abs_return_acf_20": 0.21603221778073012,
        "quantile_01": -0.05634267634725101,
        "quantile_99": 0.04845440349244841,
        "hill_tail_index": 3.900636844125468
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01865551216765664,
        "excess_kurtosis": 9.838063922997168,
        "return_acf_1": -0.1995334919700078,
        "abs_return_acf_1": 0.3131195620443251,
        "abs_return_acf_5": 0.3509349835331611,
        "abs_return_acf_20": 0.19220658197280086,
        "quantile_01": -0.06093789337717718,
        "quantile_99": 0.0469917725673091,
        "hill_tail_index": 3.2159274547867196
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01869627661868223,
        "excess_kurtosis": 6.182648152065708,
        "return_acf_1": -0.2297710776267817,
        "abs_return_acf_1": 0.3124585249848773,
        "abs_return_acf_5": 0.25953116268110243,
        "abs_return_acf_20": 0.2597699140752633,
        "quantile_01": -0.06160419283078978,
        "quantile_99": 0.05214848263616531,
        "hill_tail_index": 3.4487742412149305
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017869414958798305,
        "excess_kurtosis": 3.279539251409287,
        "return_acf_1": -0.1469773713864037,
        "abs_return_acf_1": 0.27252170392210767,
        "abs_return_acf_5": 0.23331681048132605,
        "abs_return_acf_20": 0.17779498374016053,
        "quantile_01": -0.05512771800344351,
        "quantile_99": 0.05065206773147238,
        "hill_tail_index": 3.448821244164886
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018310601477730663,
        "excess_kurtosis": 6.43940192826876,
        "return_acf_1": -0.13399937677001,
        "abs_return_acf_1": 0.24723180371326814,
        "abs_return_acf_5": 0.25035607989912656,
        "abs_return_acf_20": 0.19346629209837007,
        "quantile_01": -0.050508974111932496,
        "quantile_99": 0.04577932673299382,
        "hill_tail_index": 3.605287101907236
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0183285511441942,
        "excess_kurtosis": 6.598998045037639,
        "return_acf_1": -0.08518524874034757,
        "abs_return_acf_1": 0.3656441302756275,
        "abs_return_acf_5": 0.3029334516372487,
        "abs_return_acf_20": 0.2835536967468244,
        "quantile_01": -0.05265599830431746,
        "quantile_99": 0.049840373192615216,
        "hill_tail_index": 2.7789089910981377
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018773257193948713,
        "excess_kurtosis": 5.7173508504676125,
        "return_acf_1": -0.20524520261709198,
        "abs_return_acf_1": 0.3644304233195973,
        "abs_return_acf_5": 0.31457061979805906,
        "abs_return_acf_20": 0.25326811524484494,
        "quantile_01": -0.05603223954872387,
        "quantile_99": 0.05597941981124751,
        "hill_tail_index": 3.6140325793607766
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019061918715338792,
        "excess_kurtosis": 5.991748959838709,
        "return_acf_1": -0.24010814985732692,
        "abs_return_acf_1": 0.29004664907345196,
        "abs_return_acf_5": 0.22656283214589834,
        "abs_return_acf_20": 0.21188788268198852,
        "quantile_01": -0.061274167570685906,
        "quantile_99": 0.04943109208285911,
        "hill_tail_index": 3.66950811983399
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
