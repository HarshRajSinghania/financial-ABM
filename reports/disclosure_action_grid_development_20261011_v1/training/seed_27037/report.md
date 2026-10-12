# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27037
Run ID: `2dda98bab42bea4f4d7d58713bb00f40c09eedcf59bb2153645ebdf853dffd9d`
Result fingerprint: `ad5645518ed383aa5c9d4a476fb7adbfd741ca777bc82cab21ff4f5c7fd6f180`

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
    "equal_weight_sd": -0.5270706472114903,
    "equal_weight_raw": -7.9060597081723545,
    "fixed_start_cap_weight_sd": -0.505208083213113,
    "fixed_start_cap_weight_raw": -7.578121248196695,
    "end_cap_weight_sd": -0.4906286586461909,
    "end_cap_weight_raw": -7.3594298796928665
  },
  "full_period_change": {
    "equal_weight_sd": -0.8100325780035946,
    "equal_weight_raw": -12.15048867005392
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7934985514382552,
    "inflation_mean_sd": 0.594639880952381
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.39538888888889184,
    "equal_weight_raw": 5.930833333333377,
    "fixed_start_cap_weight_sd": 0.4029337195499175,
    "fixed_start_cap_weight_raw": 6.044005793248762,
    "end_cap_weight_sd": 0.40652626653039475,
    "end_cap_weight_raw": 6.097893997955921
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.2617063492063468,
      "change_raw": -3.9255952380952017,
      "decay_adjusted_gain_sd": 0.47388888888889164
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4985159139853981,
      "change_raw": -7.477738709780971,
      "decay_adjusted_gain_sd": 0.4263888888888916
    },
    "small": {
      "count": 18,
      "change_sd": -0.5855753968253937,
      "change_raw": -8.783630952380905,
      "decay_adjusted_gain_sd": 0.36680555555555855
    },
    "large_minus_small_sd": 0.32386904761904695,
    "large_minus_small_raw": 4.8580357142857045
  },
  "inflation": {
    "initial_mean_sd": 0.21075000000000002,
    "final_mean_sd": 0.6325833333333332,
    "mean_sd": 0.4688017624202053,
    "mean_absolute_raw_gap": 7.03202643630308,
    "final_absolute_raw_gap": 9.48875,
    "mean_range_fraction": 0.0703202643630308
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.2708889910316163,
    "final_wealth_share": 0.30688215172783373
  },
  "pricing_slope": {
    "mean": -0.0025553160111295254,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.137595534987345,
    "real_improvement_cost": 0.09353453819015405,
    "washing_cost": 0.04406099679719097,
    "fine_transfer": 0.03574294913815426,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.17333848412549926,
    "resource_cost_fraction_initial_cap": 0.004586517832911499,
    "private_net_outflow_fraction_initial_cap": 0.005777949470849974,
    "fine_transfer_fraction_initial_cap": 0.001191431637938475,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.012957240500894892,
    "unapplied_final_day_resource_cost": 0.002370532151550888
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 86.2067702106591,
    "beneficial_raw_gain_per_resource_cost": 1293.1015531598864,
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
    "accrued_cost": 2.9576572384116577,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.018533237778819375,
    "accrued_cost_fraction_initial_cap": 0.0985885746137219,
    "mean_contract_rate": 0.04119769887251247,
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
    "maximum_relative_cash_error": 1.8672430693737353e-15,
    "maximum_absolute_share_error": 1.3322676295501878e-15,
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
      "minimum": -0.17644138098654008,
      "maximum": 0.013951704532004434,
      "mean": -0.08000346815274202,
      "median": -0.0790712672282893,
      "quantile_05": -0.15349933507677277,
      "quantile_95": 0.007346392709891342
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
      "minimum": 0.28016260076854593,
      "maximum": 0.7945306091633391,
      "mean": 0.4882517853508553,
      "median": 0.4559876102459762,
      "quantile_05": 0.3056561531772151,
      "quantile_95": 0.732269573047281
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
        "daily_volatility": 0.021364331609900925,
        "excess_kurtosis": 14.520258571047247,
        "return_acf_1": -0.17644138098654008,
        "abs_return_acf_1": 0.48512454726192994,
        "abs_return_acf_5": 0.5517309959117971,
        "abs_return_acf_20": 0.43523851116448276,
        "quantile_01": -0.06428628363466596,
        "quantile_99": 0.06015129792689221,
        "hill_tail_index": 2.570805310516848
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02082256045335375,
        "excess_kurtosis": 13.626085043600188,
        "return_acf_1": -0.0791196870043008,
        "abs_return_acf_1": 0.3732475494985364,
        "abs_return_acf_5": 0.3195876713526018,
        "abs_return_acf_20": 0.2921687090929241,
        "quantile_01": -0.07507301375837983,
        "quantile_99": 0.05767338344313868,
        "hill_tail_index": 2.570326220872124
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01978511616500606,
        "excess_kurtosis": 9.109364313012687,
        "return_acf_1": -0.10108672813223896,
        "abs_return_acf_1": 0.41039818753086343,
        "abs_return_acf_5": 0.31169453916416395,
        "abs_return_acf_20": 0.30910022872634146,
        "quantile_01": -0.06665161877820058,
        "quantile_99": 0.059550659248841224,
        "hill_tail_index": 4.0229723596885805
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018835881763687213,
        "excess_kurtosis": 12.92406976998071,
        "return_acf_1": -0.15519938711177023,
        "abs_return_acf_1": 0.37074384180083586,
        "abs_return_acf_5": 0.398052988569322,
        "abs_return_acf_20": 0.3335986861312066,
        "quantile_01": -0.06146420144506866,
        "quantile_99": 0.04363528458989242,
        "hill_tail_index": 2.194592690186276
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02291826880906023,
        "excess_kurtosis": 11.254429942538751,
        "return_acf_1": -0.06936966142502327,
        "abs_return_acf_1": 0.3171370696563279,
        "abs_return_acf_5": 0.3599758911197881,
        "abs_return_acf_20": 0.38275746082332074,
        "quantile_01": -0.07481028418078133,
        "quantile_99": 0.06144754016681651,
        "hill_tail_index": 2.3151219737538895
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020742634620679518,
        "excess_kurtosis": 18.38278933034209,
        "return_acf_1": -0.08805432776300816,
        "abs_return_acf_1": 0.4831849294156603,
        "abs_return_acf_5": 0.34037091431344624,
        "abs_return_acf_20": 0.21140887104103348,
        "quantile_01": -0.06253765888532178,
        "quantile_99": 0.05593064068706849,
        "hill_tail_index": 2.7402029498969442
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021920771614505872,
        "excess_kurtosis": 19.231669895405958,
        "return_acf_1": -0.053266312360810815,
        "abs_return_acf_1": 0.40716907899601085,
        "abs_return_acf_5": 0.3494216665170205,
        "abs_return_acf_20": 0.28396437172060346,
        "quantile_01": -0.06501347420816887,
        "quantile_99": 0.05630145129238929,
        "hill_tail_index": 1.889030843999395
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01627102366150088,
        "excess_kurtosis": 3.4173345372406736,
        "return_acf_1": -0.12101243145518585,
        "abs_return_acf_1": 0.1928896324644888,
        "abs_return_acf_5": 0.12344103611446314,
        "abs_return_acf_20": 0.149882451940105,
        "quantile_01": -0.047614528456294214,
        "quantile_99": 0.037965340417862,
        "hill_tail_index": 3.365615399739562
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018787702596063712,
        "excess_kurtosis": 12.028017697026016,
        "return_acf_1": -0.022866242975288036,
        "abs_return_acf_1": 0.3272551285893871,
        "abs_return_acf_5": 0.30748886159841055,
        "abs_return_acf_20": 0.21751605859463943,
        "quantile_01": -0.05666817059121271,
        "quantile_99": 0.050553972185352326,
        "hill_tail_index": 2.3688469486394697
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02011984338062813,
        "excess_kurtosis": 21.00915305452853,
        "return_acf_1": 0.013951704532004434,
        "abs_return_acf_1": 0.34612101173978904,
        "abs_return_acf_5": 0.3354723365127533,
        "abs_return_acf_20": 0.2904687955715124,
        "quantile_01": -0.06396508763860426,
        "quantile_99": 0.04247980921775069,
        "hill_tail_index": 2.011789729445465
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.024166245830193143,
        "excess_kurtosis": 22.970667321736364,
        "return_acf_1": -0.03610167570410973,
        "abs_return_acf_1": 0.517127756004155,
        "abs_return_acf_5": 0.4419575431734449,
        "abs_return_acf_20": 0.2950930162193153,
        "quantile_01": -0.08229648316327307,
        "quantile_99": 0.06446335655342245,
        "hill_tail_index": 2.062685153117014
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01935592009970784,
        "excess_kurtosis": 7.26239203058077,
        "return_acf_1": -0.0945745036687291,
        "abs_return_acf_1": 0.31672334448802275,
        "abs_return_acf_5": 0.29312591709716507,
        "abs_return_acf_20": 0.264548248406441,
        "quantile_01": -0.07057513542566206,
        "quantile_99": 0.05530147059406409,
        "hill_tail_index": 3.2509076234471355
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021039921846461578,
        "excess_kurtosis": 11.43018230964714,
        "return_acf_1": -0.12256875561637304,
        "abs_return_acf_1": 0.24844519449707164,
        "abs_return_acf_5": 0.28603873772433386,
        "abs_return_acf_20": 0.22031698177469003,
        "quantile_01": -0.07280163086064806,
        "quantile_99": 0.055479656487196036,
        "hill_tail_index": 3.294431140937723
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017242126107231436,
        "excess_kurtosis": 8.059059019233757,
        "return_acf_1": -0.03789618781961672,
        "abs_return_acf_1": 0.31160560373999446,
        "abs_return_acf_5": 0.27232547977593974,
        "abs_return_acf_20": 0.2628036056495299,
        "quantile_01": -0.058984833700949965,
        "quantile_99": 0.04035048812463042,
        "hill_tail_index": 2.593919893957264
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017743871066212377,
        "excess_kurtosis": 5.708303555036288,
        "return_acf_1": -0.0790228474522778,
        "abs_return_acf_1": 0.39618171542556646,
        "abs_return_acf_5": 0.2913010180739688,
        "abs_return_acf_20": 0.27904899910715725,
        "quantile_01": -0.062423379524418676,
        "quantile_99": 0.047021059528046166,
        "hill_tail_index": 3.923549423503757
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.015963149860626,
        "excess_kurtosis": 7.026202971167482,
        "return_acf_1": -0.046322761736287105,
        "abs_return_acf_1": 0.2933623263691095,
        "abs_return_acf_5": 0.2442497758320873,
        "abs_return_acf_20": 0.21970544571232242,
        "quantile_01": -0.04280333295930199,
        "quantile_99": 0.03678633324393105,
        "hill_tail_index": 2.541918169894863
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01971127660785547,
        "excess_kurtosis": 16.5902220832465,
        "return_acf_1": -0.14942786383155665,
        "abs_return_acf_1": 0.31046749534512236,
        "abs_return_acf_5": 0.22454969600036867,
        "abs_return_acf_20": 0.242800424741192,
        "quantile_01": -0.059644361083186756,
        "quantile_99": 0.05038700257604115,
        "hill_tail_index": 2.515101319531186
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02196221972605072,
        "excess_kurtosis": 18.444079091312734,
        "return_acf_1": -0.06826973579600418,
        "abs_return_acf_1": 0.37338116786798425,
        "abs_return_acf_5": 0.3647408291715269,
        "abs_return_acf_20": 0.24386077860574767,
        "quantile_01": -0.06566089657741866,
        "quantile_99": 0.05358380945427034,
        "hill_tail_index": 2.0076763258236077
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018922623693425445,
        "excess_kurtosis": 5.95469350488804,
        "return_acf_1": -0.11366930605449506,
        "abs_return_acf_1": 0.3343344137065929,
        "abs_return_acf_5": 0.29903180654992123,
        "abs_return_acf_20": 0.3169481808661305,
        "quantile_01": -0.0596311288023656,
        "quantile_99": 0.04725039511355095,
        "hill_tail_index": 3.02507337038573
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01890672193861489,
        "excess_kurtosis": 12.793456311514634,
        "return_acf_1": 0.013896523413742317,
        "abs_return_acf_1": 0.41243544903716306,
        "abs_return_acf_5": 0.4021741692413201,
        "abs_return_acf_20": 0.333370474560042,
        "quantile_01": -0.06294121049748826,
        "quantile_99": 0.04512705425033691,
        "hill_tail_index": 2.417749813868023
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.026566825207562563,
        "excess_kurtosis": 24.306385697859806,
        "return_acf_1": -0.04238646239388092,
        "abs_return_acf_1": 0.4619371736002088,
        "abs_return_acf_5": 0.48268181451990466,
        "abs_return_acf_20": 0.35709035634243397,
        "quantile_01": -0.09720870577658308,
        "quantile_99": 0.07547491536817658,
        "hill_tail_index": 1.9667795650053759
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01789605728968797,
        "excess_kurtosis": 8.165351886196566,
        "return_acf_1": -0.09161435348956097,
        "abs_return_acf_1": 0.37332728088867084,
        "abs_return_acf_5": 0.36556297567042156,
        "abs_return_acf_20": 0.34300925090186013,
        "quantile_01": -0.057343808386777405,
        "quantile_99": 0.0470905067808965,
        "hill_tail_index": 3.6150251107121174
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01990367118320994,
        "excess_kurtosis": 5.023041262310693,
        "return_acf_1": -0.07054657221277691,
        "abs_return_acf_1": 0.3342741954469243,
        "abs_return_acf_5": 0.2724617187893268,
        "abs_return_acf_20": 0.2388259285139467,
        "quantile_01": -0.06860856291181637,
        "quantile_99": 0.05186339112571559,
        "hill_tail_index": 2.792704340212111
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018495063335998124,
        "excess_kurtosis": 7.93776732993059,
        "return_acf_1": -0.1514214937006648,
        "abs_return_acf_1": 0.3899530462862594,
        "abs_return_acf_5": 0.26578847441343295,
        "abs_return_acf_20": 0.2926058034732469,
        "quantile_01": -0.054769108345138325,
        "quantile_99": 0.04837733818586889,
        "hill_tail_index": 2.7766562750396893
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02498570058171262,
        "excess_kurtosis": 28.739280372128995,
        "return_acf_1": -0.04943363460999079,
        "abs_return_acf_1": 0.47816383386552147,
        "abs_return_acf_5": 0.3668658134873947,
        "abs_return_acf_20": 0.31596212862203493,
        "quantile_01": -0.07918191456722513,
        "quantile_99": 0.07349981541387984,
        "hill_tail_index": 2.305624349981854
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018369642334179138,
        "excess_kurtosis": 15.280118945819517,
        "return_acf_1": -0.1286086528354901,
        "abs_return_acf_1": 0.3289768702514141,
        "abs_return_acf_5": 0.19904309385503144,
        "abs_return_acf_20": 0.2967849673102474,
        "quantile_01": -0.05195807859031521,
        "quantile_99": 0.038954987652934286,
        "hill_tail_index": 1.9152783416388568
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019519525839212536,
        "excess_kurtosis": 5.7016113444042364,
        "return_acf_1": -0.09907104037998268,
        "abs_return_acf_1": 0.2976874999984063,
        "abs_return_acf_5": 0.3286112021350527,
        "abs_return_acf_20": 0.261480154233486,
        "quantile_01": -0.05701068049152354,
        "quantile_99": 0.05751093082441045,
        "hill_tail_index": 3.6386634206752033
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02195968226572456,
        "excess_kurtosis": 21.071919441956172,
        "return_acf_1": -0.0006593225948153128,
        "abs_return_acf_1": 0.42214699632773567,
        "abs_return_acf_5": 0.34036266028217893,
        "abs_return_acf_20": 0.26647923417493574,
        "quantile_01": -0.06615052412599161,
        "quantile_99": 0.05377539717814529,
        "hill_tail_index": 1.681983908212836
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02031801911455621,
        "excess_kurtosis": 16.72868819905478,
        "return_acf_1": -0.10108604263233002,
        "abs_return_acf_1": 0.30344401148187944,
        "abs_return_acf_5": 0.4073739510201853,
        "abs_return_acf_20": 0.38478890602462795,
        "quantile_01": -0.06787670109131451,
        "quantile_99": 0.05788327214565508,
        "hill_tail_index": 2.5478315774292017
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0207723697466882,
        "excess_kurtosis": 8.310238445129709,
        "return_acf_1": -0.0788549007848992,
        "abs_return_acf_1": 0.3504800993547171,
        "abs_return_acf_5": 0.388604811766928,
        "abs_return_acf_20": 0.32999834951513607,
        "quantile_01": -0.0674308699658692,
        "quantile_99": 0.055318140448596065,
        "hill_tail_index": 3.543426426104367
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
