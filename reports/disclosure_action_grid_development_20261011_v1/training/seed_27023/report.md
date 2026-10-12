# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27023
Run ID: `0bf0758aedf89666608c69a025573cba2573ac910db8b855fda8d666384db68e`
Result fingerprint: `9576c358392a44350cbedd01896cfc5d8baae7ee68d71f24efcfdf8f4a0c9196`

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
    "equal_weight_sd": -0.5030476190476159,
    "equal_weight_raw": -7.545714285714239,
    "fixed_start_cap_weight_sd": -0.5345709072617597,
    "fixed_start_cap_weight_raw": -8.018563608926396,
    "end_cap_weight_sd": -0.5393342698743347,
    "end_cap_weight_raw": -8.090014048115021
  },
  "full_period_change": {
    "equal_weight_sd": -0.7884880952380904,
    "equal_weight_raw": -11.827321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.745952711640207,
    "inflation_mean_sd": 0.5868693783068784
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4493333333333365,
    "equal_weight_raw": 6.740000000000048,
    "fixed_start_cap_weight_sd": 0.4178100451191923,
    "fixed_start_cap_weight_raw": 6.267150676787886,
    "end_cap_weight_sd": 0.4130466825066177,
    "end_cap_weight_raw": 6.195700237599264
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6090476190476157,
      "change_raw": -9.135714285714236,
      "decay_adjusted_gain_sd": 0.34333333333333654
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4979365079365048,
      "change_raw": -7.469047619047572,
      "decay_adjusted_gain_sd": 0.4544444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.4879365079365048,
      "change_raw": -7.319047619047572,
      "decay_adjusted_gain_sd": 0.46444444444444755
    },
    "large_minus_small_sd": -0.12111111111111095,
    "large_minus_small_raw": -1.8166666666666642
  },
  "inflation": {
    "initial_mean_sd": 0.22533333333333333,
    "final_mean_sd": 0.6202500000000001,
    "mean_sd": 0.4457301554260339,
    "mean_absolute_raw_gap": 6.685952331390508,
    "final_absolute_raw_gap": 9.30375,
    "mean_range_fraction": 0.06685952331390509
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.28,
    "initial_wealth_share": 0.3283521395587113,
    "final_wealth_share": 0.3324754499109495
  },
  "pricing_slope": {
    "mean": -0.0014146248073578132,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.04976129516183006,
    "real_improvement_cost": 0.03343552381535339,
    "washing_cost": 0.01632577134647667,
    "fine_transfer": 0.003169180548799361,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05293047571062942,
    "resource_cost_fraction_initial_cap": 0.0016587098387276682,
    "private_net_outflow_fraction_initial_cap": 0.0017643491903543136,
    "fine_transfer_fraction_initial_cap": 0.00010563935162664535,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001018457038882725,
    "unapplied_final_day_resource_cost": 0.0007586106242185416
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 270.89327068681433,
    "beneficial_raw_gain_per_resource_cost": 4063.3990603022153,
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
    "accrued_cost": 3.2400560326095924,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.26386555641911524,
    "accrued_cost_fraction_initial_cap": 0.10800186775365306,
    "mean_contract_rate": 0.04649711369659764,
    "maximum_ledger_error": 1.1180834903756764e-19
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
    "maximum_relative_cash_error": 1.3083153003121974e-15,
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
      "minimum": -0.22606757470175062,
      "maximum": -0.07198611643593797,
      "mean": -0.15077694090098506,
      "median": -0.15494203767481063,
      "quantile_05": -0.2153455876716522,
      "quantile_95": -0.08040271516525574
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
      "minimum": 0.2964496311454396,
      "maximum": 0.8264044056481351,
      "mean": 0.6425168504256065,
      "median": 0.6740153547119835,
      "quantile_05": 0.4279176005503876,
      "quantile_95": 0.7816364110277427
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
        "daily_volatility": 0.021511162222139266,
        "excess_kurtosis": 9.59603505158332,
        "return_acf_1": -0.16073514992527374,
        "abs_return_acf_1": 0.41922076155671467,
        "abs_return_acf_5": 0.40425131745324977,
        "abs_return_acf_20": 0.25682030609165657,
        "quantile_01": -0.07644410458370775,
        "quantile_99": 0.058463558761045684,
        "hill_tail_index": 3.4201925175412398
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020406658152176245,
        "excess_kurtosis": 13.291663529942912,
        "return_acf_1": -0.08829888514035292,
        "abs_return_acf_1": 0.45358721200158175,
        "abs_return_acf_5": 0.3986478578927554,
        "abs_return_acf_20": 0.24891459705274022,
        "quantile_01": -0.07089417689621728,
        "quantile_99": 0.05015586538425997,
        "hill_tail_index": 2.659584725132572
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020926338085425218,
        "excess_kurtosis": 10.450189966560947,
        "return_acf_1": -0.12708577748779734,
        "abs_return_acf_1": 0.3919662910577,
        "abs_return_acf_5": 0.46477881744569016,
        "abs_return_acf_20": 0.2241865639831525,
        "quantile_01": -0.07033961155896885,
        "quantile_99": 0.0557626289502333,
        "hill_tail_index": 2.865234204229385
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021853059475033715,
        "excess_kurtosis": 11.852023621318828,
        "return_acf_1": -0.2033029170481906,
        "abs_return_acf_1": 0.45652277383275897,
        "abs_return_acf_5": 0.47955927058212616,
        "abs_return_acf_20": 0.2958837302848002,
        "quantile_01": -0.08109071522195907,
        "quantile_99": 0.05614817746355033,
        "hill_tail_index": 2.5531938422558254
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020787210268920865,
        "excess_kurtosis": 12.654971314115095,
        "return_acf_1": -0.11945303906736136,
        "abs_return_acf_1": 0.4182041412587062,
        "abs_return_acf_5": 0.4933666379948263,
        "abs_return_acf_20": 0.30751354917088325,
        "quantile_01": -0.06953606703832088,
        "quantile_99": 0.062218978344552346,
        "hill_tail_index": 3.124466127772755
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02265619711034281,
        "excess_kurtosis": 12.055716313647906,
        "return_acf_1": -0.19562795859841123,
        "abs_return_acf_1": 0.4741370680416412,
        "abs_return_acf_5": 0.48021618311636893,
        "abs_return_acf_20": 0.2946661140818056,
        "quantile_01": -0.09006614188984469,
        "quantile_99": 0.05493776270419172,
        "hill_tail_index": 2.368692363377941
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0214039926128668,
        "excess_kurtosis": 9.938147894853476,
        "return_acf_1": -0.11999779327758613,
        "abs_return_acf_1": 0.41274608527928386,
        "abs_return_acf_5": 0.465715844020781,
        "abs_return_acf_20": 0.26707015596782435,
        "quantile_01": -0.08132483224439983,
        "quantile_99": 0.06930108931018591,
        "hill_tail_index": 2.8304828896116527
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020794291777674476,
        "excess_kurtosis": 50.85858692407123,
        "return_acf_1": -0.22606757470175062,
        "abs_return_acf_1": 0.400156200930993,
        "abs_return_acf_5": 0.3109236089518283,
        "abs_return_acf_20": 0.1870068227877711,
        "quantile_01": -0.05668069810978325,
        "quantile_99": 0.0456074550035252,
        "hill_tail_index": 1.9228509230137503
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022338456561696547,
        "excess_kurtosis": 18.507132606331457,
        "return_acf_1": -0.18201884104887753,
        "abs_return_acf_1": 0.4795101296594047,
        "abs_return_acf_5": 0.48231781968950493,
        "abs_return_acf_20": 0.30884894737087704,
        "quantile_01": -0.06945456778464133,
        "quantile_99": 0.05663379763914139,
        "hill_tail_index": 1.9106425379933802
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020300089767109675,
        "excess_kurtosis": 9.077475213681012,
        "return_acf_1": -0.1756883903765593,
        "abs_return_acf_1": 0.42024459434241984,
        "abs_return_acf_5": 0.3573852899640903,
        "abs_return_acf_20": 0.2276921519615151,
        "quantile_01": -0.07520778786469118,
        "quantile_99": 0.054535972780742244,
        "hill_tail_index": 3.1228171436527816
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02565892507029665,
        "excess_kurtosis": 16.565857502556767,
        "return_acf_1": -0.22519868181812083,
        "abs_return_acf_1": 0.4373730742450532,
        "abs_return_acf_5": 0.5233815934676258,
        "abs_return_acf_20": 0.33747269387857254,
        "quantile_01": -0.09016613019746991,
        "quantile_99": 0.07963924057727077,
        "hill_tail_index": 2.338852389367865
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02028637605619938,
        "excess_kurtosis": 5.874050654222483,
        "return_acf_1": -0.11710343021327362,
        "abs_return_acf_1": 0.39953889641352797,
        "abs_return_acf_5": 0.4062792862375612,
        "abs_return_acf_20": 0.2905324791296558,
        "quantile_01": -0.06953009151082239,
        "quantile_99": 0.0552661117637555,
        "hill_tail_index": 3.9200990492710117
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.0224215884155996,
        "excess_kurtosis": 11.5372104128076,
        "return_acf_1": -0.12220456767960045,
        "abs_return_acf_1": 0.4842787701315457,
        "abs_return_acf_5": 0.546710366073525,
        "abs_return_acf_20": 0.3669643613383599,
        "quantile_01": -0.08405895831807646,
        "quantile_99": 0.06440052256899559,
        "hill_tail_index": 2.922279233786177
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01985873835390252,
        "excess_kurtosis": 13.738126196036898,
        "return_acf_1": -0.17482590146697907,
        "abs_return_acf_1": 0.4589040382363853,
        "abs_return_acf_5": 0.3984802135608179,
        "abs_return_acf_20": 0.2519900789767321,
        "quantile_01": -0.06828898519396873,
        "quantile_99": 0.05765145934386306,
        "hill_tail_index": 2.8582566153070728
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0227124002524024,
        "excess_kurtosis": 10.116620822584476,
        "return_acf_1": -0.07786553236413779,
        "abs_return_acf_1": 0.46161955209401595,
        "abs_return_acf_5": 0.49429795223841005,
        "abs_return_acf_20": 0.3488689221784375,
        "quantile_01": -0.0868808835586166,
        "quantile_99": 0.06978718087301619,
        "hill_tail_index": 2.4052105900638536
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020927196611947932,
        "excess_kurtosis": 11.130358803789962,
        "return_acf_1": -0.16443603097854914,
        "abs_return_acf_1": 0.43695591971678516,
        "abs_return_acf_5": 0.49569377574360873,
        "abs_return_acf_20": 0.3018631096562669,
        "quantile_01": -0.0797254055306625,
        "quantile_99": 0.05172346149522031,
        "hill_tail_index": 2.3423283092101097
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021621499225602244,
        "excess_kurtosis": 13.364481879247244,
        "return_acf_1": -0.18053197467637086,
        "abs_return_acf_1": 0.4220275380799816,
        "abs_return_acf_5": 0.524609117946131,
        "abs_return_acf_20": 0.2978034566218296,
        "quantile_01": -0.0806882079179539,
        "quantile_99": 0.05364411900972168,
        "hill_tail_index": 2.383199878787477
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020356598599118193,
        "excess_kurtosis": 13.657730632320135,
        "return_acf_1": -0.0835037163666221,
        "abs_return_acf_1": 0.44244823835163977,
        "abs_return_acf_5": 0.43553907675449094,
        "abs_return_acf_20": 0.23605205783404598,
        "quantile_01": -0.0667732362858242,
        "quantile_99": 0.055695261026534854,
        "hill_tail_index": 2.8633530232900193
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020143101719792597,
        "excess_kurtosis": 8.302582479090614,
        "return_acf_1": -0.07198611643593797,
        "abs_return_acf_1": 0.3984690113254064,
        "abs_return_acf_5": 0.4185311473804783,
        "abs_return_acf_20": 0.3075940678464943,
        "quantile_01": -0.07036448974098972,
        "quantile_99": 0.06058894171503718,
        "hill_tail_index": 3.49814163309849
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020145420131068736,
        "excess_kurtosis": 10.662024330293704,
        "return_acf_1": -0.15310471370007522,
        "abs_return_acf_1": 0.45618848882858554,
        "abs_return_acf_5": 0.46012868420022196,
        "abs_return_acf_20": 0.2970999185274867,
        "quantile_01": -0.06392433674822624,
        "quantile_99": 0.056612857828817545,
        "hill_tail_index": 2.819522652863791
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01967077273740983,
        "excess_kurtosis": 15.481625322389423,
        "return_acf_1": -0.1477454713531966,
        "abs_return_acf_1": 0.37486435629023485,
        "abs_return_acf_5": 0.45613365401921707,
        "abs_return_acf_20": 0.24098343937478944,
        "quantile_01": -0.06155151442451388,
        "quantile_99": 0.044459520856719434,
        "hill_tail_index": 2.496649083337541
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02165090485999046,
        "excess_kurtosis": 13.063424036022482,
        "return_acf_1": -0.15677936164954606,
        "abs_return_acf_1": 0.4575309280581012,
        "abs_return_acf_5": 0.4678663947144543,
        "abs_return_acf_20": 0.28741305092516395,
        "quantile_01": -0.07163442921666385,
        "quantile_99": 0.05874215091654142,
        "hill_tail_index": 2.66095983078448
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020431348541506727,
        "excess_kurtosis": 9.373875226953855,
        "return_acf_1": -0.14331324465232922,
        "abs_return_acf_1": 0.49379401620058533,
        "abs_return_acf_5": 0.4879120213672674,
        "abs_return_acf_20": 0.30032932978666255,
        "quantile_01": -0.07025622942937193,
        "quantile_99": 0.059305288743881655,
        "hill_tail_index": 3.197886472156312
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02082177591985844,
        "excess_kurtosis": 16.55402488268842,
        "return_acf_1": -0.19759270231489853,
        "abs_return_acf_1": 0.4602733192940658,
        "abs_return_acf_5": 0.44361257413396704,
        "abs_return_acf_20": 0.30202190455128897,
        "quantile_01": -0.06661560305660326,
        "quantile_99": 0.058117154117439423,
        "hill_tail_index": 2.5320809832657707
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020578734487354106,
        "excess_kurtosis": 6.20344075455246,
        "return_acf_1": -0.12076104131026831,
        "abs_return_acf_1": 0.39147908552286076,
        "abs_return_acf_5": 0.4279512434543267,
        "abs_return_acf_20": 0.3056645599673753,
        "quantile_01": -0.07206799768421669,
        "quantile_99": 0.05558987468008812,
        "hill_tail_index": 2.8831588339514105
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019611352944332697,
        "excess_kurtosis": 9.564970079974968,
        "return_acf_1": -0.16872948659766107,
        "abs_return_acf_1": 0.3890085981905696,
        "abs_return_acf_5": 0.3628749864745177,
        "abs_return_acf_20": 0.28176725905814837,
        "quantile_01": -0.06051545370219616,
        "quantile_99": 0.04998616264229777,
        "hill_tail_index": 2.72436742708817
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02044754198314635,
        "excess_kurtosis": 6.248853551744196,
        "return_acf_1": -0.17586247898467836,
        "abs_return_acf_1": 0.4329800893304409,
        "abs_return_acf_5": 0.4254024756365084,
        "abs_return_acf_20": 0.31552427876835837,
        "quantile_01": -0.07550443285043366,
        "quantile_99": 0.0544318907364881,
        "hill_tail_index": 3.8350955234732043
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01733030758168608,
        "excess_kurtosis": 6.337623723498849,
        "return_acf_1": -0.12882517235363933,
        "abs_return_acf_1": 0.38603492390506183,
        "abs_return_acf_5": 0.40380752284781274,
        "abs_return_acf_20": 0.2826766948113805,
        "quantile_01": -0.05914956355733811,
        "quantile_99": 0.049826781053231496,
        "hill_tail_index": 3.4142399978047857
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02275330158571473,
        "excess_kurtosis": 14.209794658541192,
        "return_acf_1": -0.14110421695220374,
        "abs_return_acf_1": 0.5409911488392596,
        "abs_return_acf_5": 0.5703631836853937,
        "abs_return_acf_20": 0.29133844104560175,
        "quantile_01": -0.08734159232355654,
        "quantile_99": 0.05976268232467668,
        "hill_tail_index": 2.496043783492931
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020478709373463286,
        "excess_kurtosis": 9.834470581221979,
        "return_acf_1": -0.17355805848930328,
        "abs_return_acf_1": 0.4701354138142633,
        "abs_return_acf_5": 0.4864174885898472,
        "abs_return_acf_20": 0.2923293888115226,
        "quantile_01": -0.07257003726222772,
        "quantile_99": 0.05788833923569845,
        "hill_tail_index": 3.052786354768144
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
