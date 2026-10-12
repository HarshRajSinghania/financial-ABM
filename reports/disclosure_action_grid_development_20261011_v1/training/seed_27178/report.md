# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27178
Run ID: `908c0d5aa615e244bdad9903e82201fe7628742d0b26492377977fc127c5e0b3`
Result fingerprint: `df587496fe2e249c03beede226541bb7e08f444f016139bc8c378b4a6dd7f3ef`

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
    "equal_weight_sd": -0.7192142857142826,
    "equal_weight_raw": -10.788214285714238,
    "fixed_start_cap_weight_sd": -0.6893721985080616,
    "fixed_start_cap_weight_raw": -10.340582977620924,
    "end_cap_weight_sd": -0.6850406064593536,
    "end_cap_weight_raw": -10.275609096890303
  },
  "full_period_change": {
    "equal_weight_sd": -1.106821428571424,
    "equal_weight_raw": -16.602321428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0455158730158687,
    "inflation_mean_sd": 0.6152106481481482
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2331666666666699,
    "equal_weight_raw": 3.4975000000000476,
    "fixed_start_cap_weight_sd": 0.2630087538728907,
    "fixed_start_cap_weight_raw": 3.9451313080933597,
    "end_cap_weight_sd": 0.26734034592159894,
    "end_cap_weight_raw": 4.010105188823983
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6365476190476158,
      "change_raw": -9.548214285714238,
      "decay_adjusted_gain_sd": 0.3158333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6973809523809492,
      "change_raw": -10.460714285714237,
      "decay_adjusted_gain_sd": 0.2550000000000033
    },
    "small": {
      "count": 18,
      "change_sd": -0.743908730158727,
      "change_raw": -11.158630952380905,
      "decay_adjusted_gain_sd": 0.20847222222222536
    },
    "large_minus_small_sd": 0.10736111111111124,
    "large_minus_small_raw": 1.6104166666666686
  },
  "inflation": {
    "initial_mean_sd": 0.3395833333333333,
    "final_mean_sd": 0.5809166666666666,
    "mean_sd": 0.47110262281432136,
    "mean_absolute_raw_gap": 7.0665393422148215,
    "final_absolute_raw_gap": 8.713750000000001,
    "mean_range_fraction": 0.07066539342214821
  },
  "impact": {
    "initial_share": 0.3,
    "final_share": 0.4266666666666667,
    "initial_wealth_share": 0.3111531446339072,
    "final_wealth_share": 0.4877665503619481
  },
  "pricing_slope": {
    "mean": -0.0012411520987947182,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.051710975130945025,
    "real_improvement_cost": 0.036251861880042445,
    "washing_cost": 0.015459113250902592,
    "fine_transfer": 0.01675462080474651,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06846559593569154,
    "resource_cost_fraction_initial_cap": 0.0017236991710315006,
    "private_net_outflow_fraction_initial_cap": 0.002282186531189718,
    "fine_transfer_fraction_initial_cap": 0.0005584873601582169,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0092218151431796,
    "unapplied_final_day_resource_cost": 0.0003491735996370539
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 135.27109056224566,
    "beneficial_raw_gain_per_resource_cost": 2029.0663584336849,
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
    "fixed_exposure": 15.000000000000002,
    "accrued_cost": 2.9841639928940205,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.007973516703544023,
    "accrued_cost_fraction_initial_cap": 0.09947213309646734,
    "mean_contract_rate": 0.04146752916003632,
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
    "maximum_relative_cash_error": 1.3728150843087533e-15,
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
      "minimum": -0.2736863810096345,
      "maximum": -0.10290758987486164,
      "mean": -0.17849170420604474,
      "median": -0.17833056720406593,
      "quantile_05": -0.2591578465608808,
      "quantile_95": -0.11371034962289281
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
      "minimum": 0.2707428983928207,
      "maximum": 0.8356945738416457,
      "mean": 0.5318354709840278,
      "median": 0.49450080745722363,
      "quantile_05": 0.29537033094964693,
      "quantile_95": 0.7983189442258921
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
        "daily_volatility": 0.02112444913262087,
        "excess_kurtosis": 11.517861513850246,
        "return_acf_1": -0.17413599242636385,
        "abs_return_acf_1": 0.4689583532633264,
        "abs_return_acf_5": 0.43496805137643685,
        "abs_return_acf_20": 0.3793072659697912,
        "quantile_01": -0.0729647727395071,
        "quantile_99": 0.06262057499555725,
        "hill_tail_index": 2.6301720325325744
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020718915896540194,
        "excess_kurtosis": 11.01064225439396,
        "return_acf_1": -0.11447527597152451,
        "abs_return_acf_1": 0.3919657762866698,
        "abs_return_acf_5": 0.38695102840176415,
        "abs_return_acf_20": 0.2942909395329779,
        "quantile_01": -0.07103404203889206,
        "quantile_99": 0.061789876726016935,
        "hill_tail_index": 2.535349640555889
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020382817653315573,
        "excess_kurtosis": 8.522600893405434,
        "return_acf_1": -0.19730167504921403,
        "abs_return_acf_1": 0.4264913802685711,
        "abs_return_acf_5": 0.3687966778841142,
        "abs_return_acf_20": 0.3285764596237559,
        "quantile_01": -0.07037426282756856,
        "quantile_99": 0.05447393420443345,
        "hill_tail_index": 2.670193964408943
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021524536366363763,
        "excess_kurtosis": 14.376216542006762,
        "return_acf_1": -0.20813376208012435,
        "abs_return_acf_1": 0.535716635931622,
        "abs_return_acf_5": 0.4507203450483265,
        "abs_return_acf_20": 0.327637076414007,
        "quantile_01": -0.07232171927548182,
        "quantile_99": 0.0559660868705356,
        "hill_tail_index": 2.0325469759273855
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02046037618820217,
        "excess_kurtosis": 11.772924528423783,
        "return_acf_1": -0.17228034907377407,
        "abs_return_acf_1": 0.4818218033152685,
        "abs_return_acf_5": 0.44154914893127734,
        "abs_return_acf_20": 0.3601627326731377,
        "quantile_01": -0.0769003957428984,
        "quantile_99": 0.06783531643253911,
        "hill_tail_index": 3.504100715519871
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022847889318377827,
        "excess_kurtosis": 16.15281883184809,
        "return_acf_1": -0.22435454429187626,
        "abs_return_acf_1": 0.5072126801435711,
        "abs_return_acf_5": 0.4885476191766737,
        "abs_return_acf_20": 0.4106762089085449,
        "quantile_01": -0.0836967463972907,
        "quantile_99": 0.06404657001056631,
        "hill_tail_index": 2.463773026149254
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019371487633803697,
        "excess_kurtosis": 5.831438424147464,
        "return_acf_1": -0.11421677002438513,
        "abs_return_acf_1": 0.3549676624875352,
        "abs_return_acf_5": 0.29154007827486844,
        "abs_return_acf_20": 0.2367485165795467,
        "quantile_01": -0.06280299289748904,
        "quantile_99": 0.05974697445629591,
        "hill_tail_index": 3.4846149021541164
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017873332330236066,
        "excess_kurtosis": 4.41977720067275,
        "return_acf_1": -0.21162165896909574,
        "abs_return_acf_1": 0.338448442132235,
        "abs_return_acf_5": 0.2697674333325849,
        "abs_return_acf_20": 0.2063241155514155,
        "quantile_01": -0.05059217572673203,
        "quantile_99": 0.0490951264857975,
        "hill_tail_index": 3.460502179494237
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018793692721829392,
        "excess_kurtosis": 4.929064758108265,
        "return_acf_1": -0.11700048373087367,
        "abs_return_acf_1": 0.2824529512427251,
        "abs_return_acf_5": 0.3233449358343524,
        "abs_return_acf_20": 0.2619109263251028,
        "quantile_01": -0.057433569998021246,
        "quantile_99": 0.053102899163751105,
        "hill_tail_index": 3.51990320003909
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021040517456835293,
        "excess_kurtosis": 13.333721954857548,
        "return_acf_1": -0.2166156915537154,
        "abs_return_acf_1": 0.45475442470058713,
        "abs_return_acf_5": 0.41823823210466887,
        "abs_return_acf_20": 0.31752700766671044,
        "quantile_01": -0.07551932039965502,
        "quantile_99": 0.05693766041023425,
        "hill_tail_index": 2.255506092813396
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018971967103834413,
        "excess_kurtosis": 5.535250168615114,
        "return_acf_1": -0.17854624025032526,
        "abs_return_acf_1": 0.32247289834761705,
        "abs_return_acf_5": 0.2125009554678293,
        "abs_return_acf_20": 0.23789765675397034,
        "quantile_01": -0.06312937255597664,
        "quantile_99": 0.049341111750661505,
        "hill_tail_index": 4.363811133579885
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01859220557871087,
        "excess_kurtosis": 4.825289898808708,
        "return_acf_1": -0.13670606212015712,
        "abs_return_acf_1": 0.36538796380711763,
        "abs_return_acf_5": 0.340406431092942,
        "abs_return_acf_20": 0.2817678420795657,
        "quantile_01": -0.05702773513913948,
        "quantile_99": 0.04963911185783801,
        "hill_tail_index": 3.6899601344901902
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02163653454854606,
        "excess_kurtosis": 16.69579021241019,
        "return_acf_1": -0.263275584359045,
        "abs_return_acf_1": 0.47414674784692823,
        "abs_return_acf_5": 0.4598761541096884,
        "abs_return_acf_20": 0.3220629317103588,
        "quantile_01": -0.08811302190406996,
        "quantile_99": 0.05286115041249317,
        "hill_tail_index": 2.0550970254404684
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01842881392311837,
        "excess_kurtosis": 5.737361533678921,
        "return_acf_1": -0.14407936525606277,
        "abs_return_acf_1": 0.3366575302649565,
        "abs_return_acf_5": 0.2862754433831882,
        "abs_return_acf_20": 0.21966453978365835,
        "quantile_01": -0.058929201810151224,
        "quantile_99": 0.049808210805349834,
        "hill_tail_index": 3.2939056631150336
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020165231108242237,
        "excess_kurtosis": 12.441172684373425,
        "return_acf_1": -0.17811489415780662,
        "abs_return_acf_1": 0.39293053714451925,
        "abs_return_acf_5": 0.40880666084749545,
        "abs_return_acf_20": 0.28528761725264884,
        "quantile_01": -0.08039757211659472,
        "quantile_99": 0.05433012281373849,
        "hill_tail_index": 2.3843731668072783
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0191446826836431,
        "excess_kurtosis": 5.07120062577051,
        "return_acf_1": -0.1585502189307294,
        "abs_return_acf_1": 0.3867774172943192,
        "abs_return_acf_5": 0.3042617198249883,
        "abs_return_acf_20": 0.2564840776695585,
        "quantile_01": -0.061055366350646935,
        "quantile_99": 0.05388691436348598,
        "hill_tail_index": 3.837816088154661
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01942226318815883,
        "excess_kurtosis": 11.795201464768075,
        "return_acf_1": -0.17506147536103536,
        "abs_return_acf_1": 0.3832613841514604,
        "abs_return_acf_5": 0.37067037161681343,
        "abs_return_acf_20": 0.33851818947317086,
        "quantile_01": -0.07140944934698856,
        "quantile_99": 0.0543035869179191,
        "hill_tail_index": 2.0856659704873266
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017738393846454283,
        "excess_kurtosis": 3.700451377141248,
        "return_acf_1": -0.13464002620982846,
        "abs_return_acf_1": 0.27590169164866923,
        "abs_return_acf_5": 0.29154460521707354,
        "abs_return_acf_20": 0.19805656690688292,
        "quantile_01": -0.05360761096572306,
        "quantile_99": 0.04779687288766426,
        "hill_tail_index": 3.795806864776519
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02077218137589178,
        "excess_kurtosis": 12.724512130618184,
        "return_acf_1": -0.2033880247462303,
        "abs_return_acf_1": 0.4820052156844262,
        "abs_return_acf_5": 0.3647186176225447,
        "abs_return_acf_20": 0.3685478363430084,
        "quantile_01": -0.07732652796589216,
        "quantile_99": 0.06131764816718249,
        "hill_tail_index": 2.622927866796431
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020416534342352414,
        "excess_kurtosis": 14.608443796828361,
        "return_acf_1": -0.18395297675569322,
        "abs_return_acf_1": 0.5027199155187427,
        "abs_return_acf_5": 0.46522960018758325,
        "abs_return_acf_20": 0.3544107109573363,
        "quantile_01": -0.08108018509160873,
        "quantile_99": 0.05114158789504465,
        "hill_tail_index": 1.889625733789955
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02037482281550708,
        "excess_kurtosis": 12.695361717751057,
        "return_acf_1": -0.2541250559186801,
        "abs_return_acf_1": 0.4409504968691421,
        "abs_return_acf_5": 0.34857582823777583,
        "abs_return_acf_20": 0.3005303555340583,
        "quantile_01": -0.0708691449783993,
        "quantile_99": 0.057151136686025915,
        "hill_tail_index": 2.0251334706113124
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02010222273468229,
        "excess_kurtosis": 6.899073501431001,
        "return_acf_1": -0.1454601701207974,
        "abs_return_acf_1": 0.37557875834901583,
        "abs_return_acf_5": 0.34067657156246395,
        "abs_return_acf_20": 0.23670643073447353,
        "quantile_01": -0.055729016521306074,
        "quantile_99": 0.06126723064292023,
        "hill_tail_index": 3.4159265523802897
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022804317808507307,
        "excess_kurtosis": 13.700624928805038,
        "return_acf_1": -0.2736863810096345,
        "abs_return_acf_1": 0.5634143641087491,
        "abs_return_acf_5": 0.5151820876960506,
        "abs_return_acf_20": 0.4101068971730032,
        "quantile_01": -0.08488811199922888,
        "quantile_99": 0.081266699073443,
        "hill_tail_index": 3.0688696096371224
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020552683203286303,
        "excess_kurtosis": 11.43132837443709,
        "return_acf_1": -0.19082278598411062,
        "abs_return_acf_1": 0.34687339039583254,
        "abs_return_acf_5": 0.32054333941199453,
        "abs_return_acf_20": 0.2720463615851284,
        "quantile_01": -0.06610715559321162,
        "quantile_99": 0.05403514846885292,
        "hill_tail_index": 2.985573610439704
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018966273044722523,
        "excess_kurtosis": 4.943968628118566,
        "return_acf_1": -0.11329600565803546,
        "abs_return_acf_1": 0.32072798453267043,
        "abs_return_acf_5": 0.33172856820712154,
        "abs_return_acf_20": 0.3009756476070102,
        "quantile_01": -0.05786238001932722,
        "quantile_99": 0.058349937198232976,
        "hill_tail_index": 4.530368049908085
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020208168021600918,
        "excess_kurtosis": 7.911852429682552,
        "return_acf_1": -0.22756911750945866,
        "abs_return_acf_1": 0.46944032646232675,
        "abs_return_acf_5": 0.42856127070419897,
        "abs_return_acf_20": 0.354825076246182,
        "quantile_01": -0.0702136528859866,
        "quantile_99": 0.05946081698553629,
        "hill_tail_index": 3.295041837065905
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020423629112401896,
        "excess_kurtosis": 10.083618021358982,
        "return_acf_1": -0.22951863385203766,
        "abs_return_acf_1": 0.3777995404698898,
        "abs_return_acf_5": 0.40417307805488073,
        "abs_return_acf_20": 0.3216232387478471,
        "quantile_01": -0.07392830508213163,
        "quantile_99": 0.05705377037888184,
        "hill_tail_index": 2.690438718032736
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019210413359970355,
        "excess_kurtosis": 5.933853016405408,
        "return_acf_1": -0.10290758987486164,
        "abs_return_acf_1": 0.3873860462657423,
        "abs_return_acf_5": 0.32997347523993686,
        "abs_return_acf_20": 0.22180542911289577,
        "quantile_01": -0.05872200186945475,
        "quantile_99": 0.05588238666598126,
        "hill_tail_index": 3.2368635820636067
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021323602421324517,
        "excess_kurtosis": 12.792976253178592,
        "return_acf_1": -0.11998212105588034,
        "abs_return_acf_1": 0.4290031917679824,
        "abs_return_acf_5": 0.39372464656661627,
        "abs_return_acf_20": 0.27911657023393066,
        "quantile_01": -0.058117441601078845,
        "quantile_99": 0.06318665057876005,
        "hill_tail_index": 2.5371688225007207
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019651747040339416,
        "excess_kurtosis": 9.945011058700748,
        "return_acf_1": -0.1909321938799835,
        "abs_return_acf_1": 0.4097246082496933,
        "abs_return_acf_5": 0.3532879412835444,
        "abs_return_acf_20": 0.3272419831022433,
        "quantile_01": -0.07598288381443842,
        "quantile_99": 0.048123877174977014,
        "hill_tail_index": 2.95975690526099
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
