# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27227
Run ID: `e0e8de6318730bb2adcffed47a213d8418cd550fbc32a22702b85d0054ef95dc`
Result fingerprint: `13534f8da1b17c20333d239f1b1d943559a3218de960ae237adf2077b27269c1`

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
    "equal_weight_sd": -0.7601115727608556,
    "equal_weight_raw": -11.401673591412836,
    "fixed_start_cap_weight_sd": -0.7236245047011537,
    "fixed_start_cap_weight_raw": -10.854367570517306,
    "end_cap_weight_sd": -0.6913888849717073,
    "end_cap_weight_raw": -10.370833274575608
  },
  "full_period_change": {
    "equal_weight_sd": -1.2068853822846637,
    "equal_weight_raw": -18.103280734269955
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1391492554265132,
    "inflation_mean_sd": 0.5466375661375662
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.14866666666666967,
    "equal_weight_raw": 2.2300000000000444,
    "fixed_start_cap_weight_sd": 0.16532734888867798,
    "fixed_start_cap_weight_raw": 2.47991023333017,
    "end_cap_weight_sd": 0.17697928003561222,
    "end_cap_weight_raw": 2.6546892005341833
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5390030260185381,
      "change_raw": -8.085045390278072,
      "decay_adjusted_gain_sd": 0.16750000000000217
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6517756624347749,
      "change_raw": -9.776634936521624,
      "decay_adjusted_gain_sd": 0.23722222222222497
    },
    "small": {
      "count": 18,
      "change_sd": -0.8511309523809492,
      "change_raw": -12.766964285714238,
      "decay_adjusted_gain_sd": 0.10125000000000321
    },
    "large_minus_small_sd": 0.31212792636241105,
    "large_minus_small_raw": 4.681918895436166
  },
  "inflation": {
    "initial_mean_sd": 0.2773333333333333,
    "final_mean_sd": 0.5762500000000002,
    "mean_sd": 0.42251699972245355,
    "mean_absolute_raw_gap": 6.337754995836803,
    "final_absolute_raw_gap": 8.64375,
    "mean_range_fraction": 0.06337754995836803
  },
  "impact": {
    "initial_share": 0.32666666666666666,
    "final_share": 0.36,
    "initial_wealth_share": 0.3653602215660175,
    "final_wealth_share": 0.3845311348864284
  },
  "pricing_slope": {
    "mean": -0.0026891462099687988,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.15426594625481235,
    "real_improvement_cost": 0.14301857556175038,
    "washing_cost": 0.011247370693061986,
    "fine_transfer": 0.011244066334427255,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1655100125892396,
    "resource_cost_fraction_initial_cap": 0.0051421982084937454,
    "private_net_outflow_fraction_initial_cap": 0.005517000419641321,
    "fine_transfer_fraction_initial_cap": 0.0003748022111475752,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004004013276094039,
    "unapplied_final_day_resource_cost": 0.04782569044740834
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 28.91111167615166,
    "beneficial_raw_gain_per_resource_cost": 433.66667514227487,
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
    "accrued_cost": 2.8704426604752094,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.10574781571526651,
    "accrued_cost_fraction_initial_cap": 0.09568142201584032,
    "mean_contract_rate": 0.04043185435713868,
    "maximum_ledger_error": 6.098637220230962e-20
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
    "maximum_relative_cash_error": 1.062829724948731e-15,
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
      "minimum": -0.24229619036261674,
      "maximum": -0.09939241508070444,
      "mean": -0.16412642639913375,
      "median": -0.15969654356525764,
      "quantile_05": -0.2313373470574819,
      "quantile_95": -0.12334059981716118
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
      "minimum": 0.2609360408000178,
      "maximum": 0.85013015685055,
      "mean": 0.6864531096471692,
      "median": 0.7153197313957788,
      "quantile_05": 0.48064195575409113,
      "quantile_95": 0.808492350523307
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
        "daily_volatility": 0.026244210289691868,
        "excess_kurtosis": 26.27490387261012,
        "return_acf_1": -0.159804996538568,
        "abs_return_acf_1": 0.48858992283631647,
        "abs_return_acf_5": 0.4241377541462723,
        "abs_return_acf_20": 0.3141544302641407,
        "quantile_01": -0.09445808712304535,
        "quantile_99": 0.0723419676633417,
        "hill_tail_index": 2.1278441547003366
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024820589398996194,
        "excess_kurtosis": 15.755925017249545,
        "return_acf_1": -0.13033933528845257,
        "abs_return_acf_1": 0.5432282173400987,
        "abs_return_acf_5": 0.49256780444980197,
        "abs_return_acf_20": 0.345541402854821,
        "quantile_01": -0.0848224958924275,
        "quantile_99": 0.07047612550141119,
        "hill_tail_index": 2.26924592473233
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.024697850451994775,
        "excess_kurtosis": 18.04220599109537,
        "return_acf_1": -0.13215095501605745,
        "abs_return_acf_1": 0.5353406212291582,
        "abs_return_acf_5": 0.47938961062296814,
        "abs_return_acf_20": 0.342860312458883,
        "quantile_01": -0.08536851053723055,
        "quantile_99": 0.07587540032997715,
        "hill_tail_index": 2.9612710768458053
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.024105482580031458,
        "excess_kurtosis": 36.77927731333751,
        "return_acf_1": -0.1983972260144459,
        "abs_return_acf_1": 0.5377598610434362,
        "abs_return_acf_5": 0.5538721611504738,
        "abs_return_acf_20": 0.2718049832093405,
        "quantile_01": -0.07547757328304633,
        "quantile_99": 0.05387837007117264,
        "hill_tail_index": 1.9222472542506748
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02428737578523881,
        "excess_kurtosis": 40.75653329455788,
        "return_acf_1": -0.14897313405531357,
        "abs_return_acf_1": 0.47792442006558616,
        "abs_return_acf_5": 0.42904021461139524,
        "abs_return_acf_20": 0.298918484779799,
        "quantile_01": -0.07592130180612724,
        "quantile_99": 0.050803058099212296,
        "hill_tail_index": 1.8839919420078444
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020786725738776782,
        "excess_kurtosis": 6.581223740596343,
        "return_acf_1": -0.13259650894570593,
        "abs_return_acf_1": 0.3812682311185377,
        "abs_return_acf_5": 0.37231974453413996,
        "abs_return_acf_20": 0.3222379502381983,
        "quantile_01": -0.07430486311791666,
        "quantile_99": 0.07188566885667431,
        "hill_tail_index": 4.319315155842259
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022472600614618216,
        "excess_kurtosis": 14.385319169405058,
        "return_acf_1": -0.20765779956831687,
        "abs_return_acf_1": 0.4663822705133333,
        "abs_return_acf_5": 0.4353979927677011,
        "abs_return_acf_20": 0.26080322493026703,
        "quantile_01": -0.07398554244693871,
        "quantile_99": 0.05274986121037404,
        "hill_tail_index": 3.1453128548826172
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.024532079028395045,
        "excess_kurtosis": 14.37150982277456,
        "return_acf_1": -0.12496825426459057,
        "abs_return_acf_1": 0.46419192983380936,
        "abs_return_acf_5": 0.44901131463871574,
        "abs_return_acf_20": 0.39250950036930127,
        "quantile_01": -0.0925017297858552,
        "quantile_99": 0.0629074567822632,
        "hill_tail_index": 2.6437664457770707
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02508959522184777,
        "excess_kurtosis": 33.960875897884044,
        "return_acf_1": -0.24229619036261674,
        "abs_return_acf_1": 0.44952957870607746,
        "abs_return_acf_5": 0.3755161205692473,
        "abs_return_acf_20": 0.251354021606386,
        "quantile_01": -0.06493110554444492,
        "quantile_99": 0.06917457806827125,
        "hill_tail_index": 2.004170437780756
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022660566686755503,
        "excess_kurtosis": 12.92711844642697,
        "return_acf_1": -0.1786732236883337,
        "abs_return_acf_1": 0.5601957653324955,
        "abs_return_acf_5": 0.4710763936260288,
        "abs_return_acf_20": 0.3299759321253988,
        "quantile_01": -0.07203968354194815,
        "quantile_99": 0.06102396239743715,
        "hill_tail_index": 2.442352531833714
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021470397003667898,
        "excess_kurtosis": 11.448626962980306,
        "return_acf_1": -0.1318618028003468,
        "abs_return_acf_1": 0.45847488291259897,
        "abs_return_acf_5": 0.4472589177416362,
        "abs_return_acf_20": 0.32244066703689267,
        "quantile_01": -0.07338548279477919,
        "quantile_99": 0.07154544083200629,
        "hill_tail_index": 3.458993299793254
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024761805920931756,
        "excess_kurtosis": 31.917478872544926,
        "return_acf_1": -0.2254372074559349,
        "abs_return_acf_1": 0.5346430783450827,
        "abs_return_acf_5": 0.45127936139653735,
        "abs_return_acf_20": 0.2617383194691442,
        "quantile_01": -0.0815280775363274,
        "quantile_99": 0.056474244242236446,
        "hill_tail_index": 1.8287424813426632
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02413654399755205,
        "excess_kurtosis": 13.471323921802714,
        "return_acf_1": -0.18894148881081618,
        "abs_return_acf_1": 0.47873825168005985,
        "abs_return_acf_5": 0.46048459350426496,
        "abs_return_acf_20": 0.35510151535268175,
        "quantile_01": -0.08580599980714636,
        "quantile_99": 0.06583203910304301,
        "hill_tail_index": 2.994493251383206
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022162322145162148,
        "excess_kurtosis": 10.85702395092636,
        "return_acf_1": -0.17839218739058577,
        "abs_return_acf_1": 0.5369780858199962,
        "abs_return_acf_5": 0.46563382939689607,
        "abs_return_acf_20": 0.33601578555372946,
        "quantile_01": -0.07047409225273367,
        "quantile_99": 0.06737065906805768,
        "hill_tail_index": 3.100753219672853
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019664715286236704,
        "excess_kurtosis": 5.963299649885265,
        "return_acf_1": -0.13546963469608084,
        "abs_return_acf_1": 0.3502704922444737,
        "abs_return_acf_5": 0.36357636576136654,
        "abs_return_acf_20": 0.3033177863060023,
        "quantile_01": -0.06612304592070191,
        "quantile_99": 0.05386940728994376,
        "hill_tail_index": 3.21563437590043
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02219302955440142,
        "excess_kurtosis": 16.406930402748895,
        "return_acf_1": -0.1852094129911468,
        "abs_return_acf_1": 0.47005785826686436,
        "abs_return_acf_5": 0.3638764071297155,
        "abs_return_acf_20": 0.2560408801311048,
        "quantile_01": -0.07265325973700096,
        "quantile_99": 0.057127262987686875,
        "hill_tail_index": 2.3522802447530067
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02334452348400882,
        "excess_kurtosis": 24.914831938559352,
        "return_acf_1": -0.1657904668618191,
        "abs_return_acf_1": 0.45428010527512114,
        "abs_return_acf_5": 0.45587017882573144,
        "abs_return_acf_20": 0.29610257690122765,
        "quantile_01": -0.06616299527736262,
        "quantile_99": 0.05518391933563443,
        "hill_tail_index": 1.9723887564573988
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02054869127375171,
        "excess_kurtosis": 10.365908897318613,
        "return_acf_1": -0.13788740778814904,
        "abs_return_acf_1": 0.3955525852324123,
        "abs_return_acf_5": 0.42821659294675457,
        "abs_return_acf_20": 0.36474095392957606,
        "quantile_01": -0.06650711100365163,
        "quantile_99": 0.05961713621720604,
        "hill_tail_index": 2.8368175509238833
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021921848096467637,
        "excess_kurtosis": 10.80739130141433,
        "return_acf_1": -0.20604415475563664,
        "abs_return_acf_1": 0.4870787081441992,
        "abs_return_acf_5": 0.42520930616603214,
        "abs_return_acf_20": 0.3091713838209725,
        "quantile_01": -0.0700834714918916,
        "quantile_99": 0.0554143021354075,
        "hill_tail_index": 2.5510426973062046
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022532217709200837,
        "excess_kurtosis": 19.06552794037332,
        "return_acf_1": -0.18245384192362754,
        "abs_return_acf_1": 0.438665481136212,
        "abs_return_acf_5": 0.340444533516728,
        "abs_return_acf_20": 0.29808463872067686,
        "quantile_01": -0.07526668273143386,
        "quantile_99": 0.06478127358800354,
        "hill_tail_index": 2.7488093123033663
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021835345550363924,
        "excess_kurtosis": 14.372848509418361,
        "return_acf_1": -0.13550890045265465,
        "abs_return_acf_1": 0.5236935784214105,
        "abs_return_acf_5": 0.42015054973764304,
        "abs_return_acf_20": 0.3353725815375341,
        "quantile_01": -0.07030002443616468,
        "quantile_99": 0.0542826113243069,
        "hill_tail_index": 2.3883071268195555
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024235951136132257,
        "excess_kurtosis": 20.344592395415578,
        "return_acf_1": -0.09939241508070444,
        "abs_return_acf_1": 0.5471617564289784,
        "abs_return_acf_5": 0.44620258591223827,
        "abs_return_acf_20": 0.34192078270562126,
        "quantile_01": -0.07514844014676954,
        "quantile_99": 0.0687191171044015,
        "hill_tail_index": 2.4309594390973337
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.023176968766253067,
        "excess_kurtosis": 15.670749746446194,
        "return_acf_1": -0.20582986476751963,
        "abs_return_acf_1": 0.48159974082694185,
        "abs_return_acf_5": 0.4399197022917888,
        "abs_return_acf_20": 0.3371492588311778,
        "quantile_01": -0.06963108031543538,
        "quantile_99": 0.06510816157254821,
        "hill_tail_index": 2.101270675831703
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020468634854493913,
        "excess_kurtosis": 9.82066722575813,
        "return_acf_1": -0.12200888254199166,
        "abs_return_acf_1": 0.5036955228692526,
        "abs_return_acf_5": 0.4757380986308242,
        "abs_return_acf_20": 0.31092849688681623,
        "quantile_01": -0.0697470727216574,
        "quantile_99": 0.06882577956923164,
        "hill_tail_index": 3.5756648094420522
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019964954808429206,
        "excess_kurtosis": 8.325377073687786,
        "return_acf_1": -0.12755027597885615,
        "abs_return_acf_1": 0.4503082359966529,
        "abs_return_acf_5": 0.3976118086559311,
        "abs_return_acf_20": 0.3103591048176214,
        "quantile_01": -0.06422181493148935,
        "quantile_99": 0.05685320321170337,
        "hill_tail_index": 3.561381011041691
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02351275179170277,
        "excess_kurtosis": 23.055385459803833,
        "return_acf_1": -0.15958809059194726,
        "abs_return_acf_1": 0.44405097462173626,
        "abs_return_acf_5": 0.3989350256146856,
        "abs_return_acf_20": 0.30293496586046315,
        "quantile_01": -0.0725101992521793,
        "quantile_99": 0.06265131482066796,
        "hill_tail_index": 2.1864733634461957
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023432373025211443,
        "excess_kurtosis": 13.594254198634825,
        "return_acf_1": -0.13288873813943286,
        "abs_return_acf_1": 0.4712141384513667,
        "abs_return_acf_5": 0.3992047866153816,
        "abs_return_acf_20": 0.2930168030601393,
        "quantile_01": -0.07803029173219357,
        "quantile_99": 0.06688977896060107,
        "hill_tail_index": 2.7642110066542744
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.023581748967736404,
        "excess_kurtosis": 24.79747351963571,
        "return_acf_1": -0.18332313266657874,
        "abs_return_acf_1": 0.4693463243030206,
        "abs_return_acf_5": 0.3808857574423242,
        "abs_return_acf_20": 0.30841187308214174,
        "quantile_01": -0.08299813179580262,
        "quantile_99": 0.05387028511598946,
        "hill_tail_index": 1.966327867743633
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02277286039031632,
        "excess_kurtosis": 17.88432984562741,
        "return_acf_1": -0.23616473400420218,
        "abs_return_acf_1": 0.5002383535541406,
        "abs_return_acf_5": 0.44264684255779063,
        "abs_return_acf_20": 0.2816709930094447,
        "quantile_01": -0.08342591513186662,
        "quantile_99": 0.06638995309590282,
        "hill_tail_index": 2.28602214819247
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020123656252688416,
        "excess_kurtosis": 5.927624092994376,
        "return_acf_1": -0.12819252853357965,
        "abs_return_acf_1": 0.35065857724435046,
        "abs_return_acf_5": 0.42916380097726126,
        "abs_return_acf_20": 0.32447010153106326,
        "quantile_01": -0.0689511834298947,
        "quantile_99": 0.06265735127259657,
        "hill_tail_index": 4.9072803075701
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
