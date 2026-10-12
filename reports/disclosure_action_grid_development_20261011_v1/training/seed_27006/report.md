# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27006
Run ID: `9824eca0b2a17a8d1171c209c38662e8d88edc602405e267844a39eea3fb2e6c`
Result fingerprint: `1ef0e79d4f3d9fb01481d24f490b8852da6802e022aa36b807ce29e702e9addf`

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
    "equal_weight_sd": -0.44421428571428234,
    "equal_weight_raw": -6.663214285714236,
    "fixed_start_cap_weight_sd": -0.44102740943701607,
    "fixed_start_cap_weight_raw": -6.61541114155524,
    "end_cap_weight_sd": -0.4563593727220619,
    "end_cap_weight_raw": -6.845390590830928
  },
  "full_period_change": {
    "equal_weight_sd": -0.7024047619047571,
    "equal_weight_raw": -10.536071428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.6600955687830642,
    "inflation_mean_sd": 0.6198779761904762
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5081666666666699,
    "equal_weight_raw": 7.6225000000000485,
    "fixed_start_cap_weight_sd": 0.5113535429439361,
    "fixed_start_cap_weight_raw": 7.670303144159042,
    "end_cap_weight_sd": 0.4960215796588904,
    "end_cap_weight_raw": 7.440323694883355
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5848809523809492,
      "change_raw": -8.773214285714237,
      "decay_adjusted_gain_sd": 0.3675000000000032
    },
    "mid": {
      "count": 9,
      "change_sd": -0.3171031746031713,
      "change_raw": -4.756547619047569,
      "decay_adjusted_gain_sd": 0.6352777777777809
    },
    "small": {
      "count": 18,
      "change_sd": -0.4843253968253935,
      "change_raw": -7.264880952380903,
      "decay_adjusted_gain_sd": 0.4680555555555588
    },
    "large_minus_small_sd": -0.10055555555555568,
    "large_minus_small_raw": -1.508333333333335
  },
  "inflation": {
    "initial_mean_sd": 0.15874999999999995,
    "final_mean_sd": 0.6814166666666666,
    "mean_sd": 0.39275166527893424,
    "mean_absolute_raw_gap": 5.891274979184014,
    "final_absolute_raw_gap": 10.221250000000003,
    "mean_range_fraction": 0.05891274979184014
  },
  "impact": {
    "initial_share": 0.22,
    "final_share": 0.32,
    "initial_wealth_share": 0.3009950716273121,
    "final_wealth_share": 0.40015069766220795
  },
  "pricing_slope": {
    "mean": -0.0018630503285671622,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.26839141414038115,
    "real_improvement_cost": 0.19169646507742902,
    "washing_cost": 0.07669494906295216,
    "fine_transfer": 0.0010347132223200229,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.26942612736270116,
    "resource_cost_fraction_initial_cap": 0.00894638047134604,
    "private_net_outflow_fraction_initial_cap": 0.00898087091209004,
    "fine_transfer_fraction_initial_cap": 3.449044074400077e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007156008938093951,
    "unapplied_final_day_resource_cost": 0.0027708501749466445
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 56.801369927676795,
    "beneficial_raw_gain_per_resource_cost": 852.020548915152,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 2.9448558881063667,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.03133458808410974,
    "accrued_cost_fraction_initial_cap": 0.09816186293687891,
    "mean_contract_rate": 0.0405283669354784,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 2.5720524253230926e-15,
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
      "minimum": -0.23970294719527505,
      "maximum": -0.024476482194783475,
      "mean": -0.1520162982443632,
      "median": -0.15365311123234932,
      "quantile_05": -0.23569895614389455,
      "quantile_95": -0.06531833857637823
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
      "minimum": 0.41643460351422895,
      "maximum": 0.8074658646771351,
      "mean": 0.6640707014420973,
      "median": 0.6843330245358805,
      "quantile_05": 0.4882102915161612,
      "quantile_95": 0.7831665280381636
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
        "daily_volatility": 0.019223507630242945,
        "excess_kurtosis": 6.867368892549605,
        "return_acf_1": -0.20522992272377483,
        "abs_return_acf_1": 0.2643975225373341,
        "abs_return_acf_5": 0.31038361836558714,
        "abs_return_acf_20": 0.22980418373875197,
        "quantile_01": -0.055873170920951544,
        "quantile_99": 0.04990988125054038,
        "hill_tail_index": 3.246178456691779
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02157597731358574,
        "excess_kurtosis": 15.349521699708262,
        "return_acf_1": -0.06151776934716703,
        "abs_return_acf_1": 0.3780101924460499,
        "abs_return_acf_5": 0.4393403090027318,
        "abs_return_acf_20": 0.23374012311518805,
        "quantile_01": -0.07694958918657356,
        "quantile_99": 0.06449954811238914,
        "hill_tail_index": 3.0054011733873525
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02011405891247895,
        "excess_kurtosis": 13.796212328535216,
        "return_acf_1": -0.1364386548474193,
        "abs_return_acf_1": 0.3846571680987298,
        "abs_return_acf_5": 0.3719659627769576,
        "abs_return_acf_20": 0.22225458860480932,
        "quantile_01": -0.06801894849745255,
        "quantile_99": 0.051914899922177904,
        "hill_tail_index": 2.339082867093412
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018090897127435047,
        "excess_kurtosis": 4.562162999865366,
        "return_acf_1": -0.21703991463380537,
        "abs_return_acf_1": 0.27852124656733185,
        "abs_return_acf_5": 0.33942664177522125,
        "abs_return_acf_20": 0.19844637861510744,
        "quantile_01": -0.05491863793608794,
        "quantile_99": 0.055662193896039214,
        "hill_tail_index": 4.080623693731031
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019985061381123586,
        "excess_kurtosis": 24.399780219474664,
        "return_acf_1": -0.15499757006595907,
        "abs_return_acf_1": 0.29530483527494317,
        "abs_return_acf_5": 0.40739373606775986,
        "abs_return_acf_20": 0.2230462002147451,
        "quantile_01": -0.05347725759425521,
        "quantile_99": 0.04781983467106033,
        "hill_tail_index": 2.091681864932565
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02055541264756836,
        "excess_kurtosis": 27.36966508596026,
        "return_acf_1": -0.1433592483363922,
        "abs_return_acf_1": 0.3338221497130577,
        "abs_return_acf_5": 0.33926716899707127,
        "abs_return_acf_20": 0.1854587779238762,
        "quantile_01": -0.059483005357810446,
        "quantile_99": 0.048274000461449286,
        "hill_tail_index": 2.2575932177012383
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020607644465081378,
        "excess_kurtosis": 17.446307238099614,
        "return_acf_1": -0.08868488495319149,
        "abs_return_acf_1": 0.33055802970414155,
        "abs_return_acf_5": 0.3407538721459444,
        "abs_return_acf_20": 0.23339210783997516,
        "quantile_01": -0.06274008739023203,
        "quantile_99": 0.052725051938905275,
        "hill_tail_index": 2.255650730144078
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020753168086677803,
        "excess_kurtosis": 24.48200436572591,
        "return_acf_1": -0.06996347874541409,
        "abs_return_acf_1": 0.2963168147195055,
        "abs_return_acf_5": 0.36658673611987863,
        "abs_return_acf_20": 0.24295251544070165,
        "quantile_01": -0.059321574635326904,
        "quantile_99": 0.046187912203086205,
        "hill_tail_index": 1.8107455289453411
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02108952079027667,
        "excess_kurtosis": 16.563474490486946,
        "return_acf_1": -0.14569534059574102,
        "abs_return_acf_1": 0.35266826482091446,
        "abs_return_acf_5": 0.33764135034334786,
        "abs_return_acf_20": 0.2153028911012537,
        "quantile_01": -0.06085475244127284,
        "quantile_99": 0.05440815768950326,
        "hill_tail_index": 2.4335000470064116
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020927522164569386,
        "excess_kurtosis": 15.74099207543577,
        "return_acf_1": -0.18174186085990787,
        "abs_return_acf_1": 0.32822564180259295,
        "abs_return_acf_5": 0.3850138124818533,
        "abs_return_acf_20": 0.275588497226747,
        "quantile_01": -0.06512778096137337,
        "quantile_99": 0.05771512607245682,
        "hill_tail_index": 3.0309143287002747
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020648912512280404,
        "excess_kurtosis": 9.347972088259713,
        "return_acf_1": -0.14153636883579673,
        "abs_return_acf_1": 0.350673715848977,
        "abs_return_acf_5": 0.2503277669374522,
        "abs_return_acf_20": 0.20213127575707987,
        "quantile_01": -0.06486242744268883,
        "quantile_99": 0.053896075678422514,
        "hill_tail_index": 3.016723917526668
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020605405924708917,
        "excess_kurtosis": 12.070380907802829,
        "return_acf_1": -0.10710021980523429,
        "abs_return_acf_1": 0.4463419069695499,
        "abs_return_acf_5": 0.38969553238537713,
        "abs_return_acf_20": 0.24807535437442826,
        "quantile_01": -0.06286908471166144,
        "quantile_99": 0.053905654667406336,
        "hill_tail_index": 2.78477718938961
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021213281188177995,
        "excess_kurtosis": 32.96637876754308,
        "return_acf_1": -0.1152198577222046,
        "abs_return_acf_1": 0.41024223298118206,
        "abs_return_acf_5": 0.4077724634807488,
        "abs_return_acf_20": 0.31761968374064703,
        "quantile_01": -0.05444946862932087,
        "quantile_99": 0.05055455202418327,
        "hill_tail_index": 1.673855191316395
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021251927071230685,
        "excess_kurtosis": 19.140924322212403,
        "return_acf_1": -0.14383577961499663,
        "abs_return_acf_1": 0.3919026125933507,
        "abs_return_acf_5": 0.28833386963661983,
        "abs_return_acf_20": 0.32411809490390403,
        "quantile_01": -0.05687117358223282,
        "quantile_99": 0.050991817397748884,
        "hill_tail_index": 2.0678959756621333
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021383170910281395,
        "excess_kurtosis": 24.69743342726443,
        "return_acf_1": -0.23970294719527505,
        "abs_return_acf_1": 0.43017786289276083,
        "abs_return_acf_5": 0.39293467310740804,
        "abs_return_acf_20": 0.22714361043361525,
        "quantile_01": -0.06320457606189442,
        "quantile_99": 0.05549036329805937,
        "hill_tail_index": 2.6374837321065225
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019458238967824927,
        "excess_kurtosis": 10.195576967822293,
        "return_acf_1": -0.21305528396896156,
        "abs_return_acf_1": 0.29085613169274255,
        "abs_return_acf_5": 0.2612206183036138,
        "abs_return_acf_20": 0.2715330312411471,
        "quantile_01": -0.06649700884475745,
        "quantile_99": 0.06714529610642955,
        "hill_tail_index": 2.693865778249946
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020801650899713114,
        "excess_kurtosis": 32.31103818806158,
        "return_acf_1": -0.12016125170267901,
        "abs_return_acf_1": 0.39246025870721163,
        "abs_return_acf_5": 0.46500655188227147,
        "abs_return_acf_20": 0.2883999540914895,
        "quantile_01": -0.06842551020922878,
        "quantile_99": 0.0468480323875185,
        "hill_tail_index": 1.9850124684660795
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019200651211564872,
        "excess_kurtosis": 17.278637647265626,
        "return_acf_1": -0.1795121571776534,
        "abs_return_acf_1": 0.23212769166954758,
        "abs_return_acf_5": 0.23909126798413133,
        "abs_return_acf_20": 0.18396381001793538,
        "quantile_01": -0.06430729097150686,
        "quantile_99": 0.054154762834513454,
        "hill_tail_index": 3.226098428477175
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018577385081971584,
        "excess_kurtosis": 5.843055031406829,
        "return_acf_1": -0.23323813996312517,
        "abs_return_acf_1": 0.2945501516015702,
        "abs_return_acf_5": 0.28903769190856454,
        "abs_return_acf_20": 0.23649698019565815,
        "quantile_01": -0.059532060995168674,
        "quantile_99": 0.05638229012251346,
        "hill_tail_index": 3.346432370292897
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021239344642294735,
        "excess_kurtosis": 22.422862211212415,
        "return_acf_1": -0.10385611572436572,
        "abs_return_acf_1": 0.3538584214299993,
        "abs_return_acf_5": 0.3468011414531514,
        "abs_return_acf_20": 0.27026819563222787,
        "quantile_01": -0.06462375762167405,
        "quantile_99": 0.04741905819625357,
        "hill_tail_index": 2.1316167980860294
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019979367919942967,
        "excess_kurtosis": 10.677176721660805,
        "return_acf_1": -0.194674809362598,
        "abs_return_acf_1": 0.32309080764623904,
        "abs_return_acf_5": 0.28396115316159876,
        "abs_return_acf_20": 0.2622852909113665,
        "quantile_01": -0.05838820580877621,
        "quantile_99": 0.059373170648885865,
        "hill_tail_index": 3.9590258672116065
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01885148219410868,
        "excess_kurtosis": 9.23402013683286,
        "return_acf_1": -0.23771235120088768,
        "abs_return_acf_1": 0.29502190381576593,
        "abs_return_acf_5": 0.3038721630419204,
        "abs_return_acf_20": 0.2747169732642449,
        "quantile_01": -0.05672352526136575,
        "quantile_99": 0.06214071825499378,
        "hill_tail_index": 2.769725705381885
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01979753556886645,
        "excess_kurtosis": 25.006672249268927,
        "return_acf_1": -0.024476482194783475,
        "abs_return_acf_1": 0.43479262499582655,
        "abs_return_acf_5": 0.3383276620629474,
        "abs_return_acf_20": 0.20887350714027086,
        "quantile_01": -0.06651742661324539,
        "quantile_99": 0.04384953112874963,
        "hill_tail_index": 1.6967955140227748
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019829955442313186,
        "excess_kurtosis": 12.02031894381806,
        "return_acf_1": -0.19415469097477106,
        "abs_return_acf_1": 0.33542006402961505,
        "abs_return_acf_5": 0.3285360563989436,
        "abs_return_acf_20": 0.20799526535171992,
        "quantile_01": -0.06275544532608116,
        "quantile_99": 0.05207983632326556,
        "hill_tail_index": 2.9006913957930207
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019689547061160013,
        "excess_kurtosis": 6.395514115787995,
        "return_acf_1": -0.1841149588613958,
        "abs_return_acf_1": 0.33051965906452474,
        "abs_return_acf_5": 0.3215936908460676,
        "abs_return_acf_20": 0.22229219288146734,
        "quantile_01": -0.062140014587092104,
        "quantile_99": 0.054072321255305075,
        "hill_tail_index": 3.3617384210604433
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01981648055737838,
        "excess_kurtosis": 6.580383911960119,
        "return_acf_1": -0.16186327189494026,
        "abs_return_acf_1": 0.33790278001234875,
        "abs_return_acf_5": 0.3790475429981916,
        "abs_return_acf_20": 0.24907233013455077,
        "quantile_01": -0.06630137575747976,
        "quantile_99": 0.06304093990910625,
        "hill_tail_index": 3.6276022638369176
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019827818862398882,
        "excess_kurtosis": 23.40226123243359,
        "return_acf_1": -0.15230865239873953,
        "abs_return_acf_1": 0.32726858620565424,
        "abs_return_acf_5": 0.3290001835263775,
        "abs_return_acf_20": 0.2672702966230942,
        "quantile_01": -0.06001002806458111,
        "quantile_99": 0.04680556187953061,
        "hill_tail_index": 1.9795952190334112
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02031076491771903,
        "excess_kurtosis": 22.74351361951557,
        "return_acf_1": -0.09344881706508161,
        "abs_return_acf_1": 0.3954719140578817,
        "abs_return_acf_5": 0.404534878978537,
        "abs_return_acf_20": 0.2419405313727058,
        "quantile_01": -0.06279816306849972,
        "quantile_99": 0.05436336108384241,
        "hill_tail_index": 2.000032660770072
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022833596200792165,
        "excess_kurtosis": 17.845545851100393,
        "return_acf_1": -0.15830090646808814,
        "abs_return_acf_1": 0.33851546579051717,
        "abs_return_acf_5": 0.40931205442573587,
        "abs_return_acf_20": 0.24803990046188243,
        "quantile_01": -0.07601026520573767,
        "quantile_99": 0.05954336936360302,
        "hill_tail_index": 2.2656488940114716
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01861468888715472,
        "excess_kurtosis": 13.095437057210642,
        "return_acf_1": -0.15754724009054702,
        "abs_return_acf_1": 0.3696722352612762,
        "abs_return_acf_5": 0.28222650871589067,
        "abs_return_acf_20": 0.12736485555574376,
        "quantile_01": -0.05125795387045786,
        "quantile_99": 0.04234329631855754,
        "hill_tail_index": 2.2832713687369943
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
Unseen state share: 0.0033333333333333335
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
