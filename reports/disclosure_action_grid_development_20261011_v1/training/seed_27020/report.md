# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27020
Run ID: `6ab6e163b39e08e85e29a2efb93bd403e88d5223170a670466d98039132e52a9`
Result fingerprint: `2bbebc07487444298a7b4d3cc22a5232cd56381898edee0bc9a5528964f72e1c`

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
    "equal_weight_sd": -0.44113095238094907,
    "equal_weight_raw": -6.616964285714237,
    "fixed_start_cap_weight_sd": -0.4068874883687114,
    "fixed_start_cap_weight_raw": -6.103312325530671,
    "end_cap_weight_sd": -0.4213736166592958,
    "end_cap_weight_raw": -6.320604249889437
  },
  "full_period_change": {
    "equal_weight_sd": -0.7543214285714238,
    "equal_weight_raw": -11.314821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7238505291005246,
    "inflation_mean_sd": 0.4976574074074074
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5054861756014231,
    "equal_weight_raw": 7.582292634021345,
    "fixed_start_cap_weight_sd": 0.5404984590449221,
    "fixed_start_cap_weight_raw": 8.107476885673833,
    "end_cap_weight_sd": 0.5263994191781218,
    "end_cap_weight_raw": 7.895991287671828
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.37821428571428245,
      "change_raw": -5.673214285714237,
      "decay_adjusted_gain_sd": 0.5741666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4893253968253936,
      "change_raw": -7.339880952380904,
      "decay_adjusted_gain_sd": 0.4514054689669566
    },
    "small": {
      "count": 18,
      "change_sd": -0.42751984126983794,
      "change_raw": -6.412797619047569,
      "decay_adjusted_gain_sd": 0.5210797804077818
    },
    "large_minus_small_sd": 0.04930555555555549,
    "large_minus_small_raw": 0.7395833333333324
  },
  "inflation": {
    "initial_mean_sd": 0.22774999999999998,
    "final_mean_sd": 0.5220833333333332,
    "mean_sd": 0.39008222314737717,
    "mean_absolute_raw_gap": 5.851233347210658,
    "final_absolute_raw_gap": 7.831249999999999,
    "mean_range_fraction": 0.05851233347210658
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.20781161872008147,
    "final_wealth_share": 0.2587690499675698
  },
  "pricing_slope": {
    "mean": -0.0009295330450789627,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.3507141693686344,
    "real_improvement_cost": 0.3091441875555355,
    "washing_cost": 0.0415699818130989,
    "fine_transfer": 0.014226411378091441,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.36494058074672586,
    "resource_cost_fraction_initial_cap": 0.011690472312287814,
    "private_net_outflow_fraction_initial_cap": 0.012164686024890863,
    "fine_transfer_fraction_initial_cap": 0.00047421371260304804,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.019188227378033582,
    "unapplied_final_day_resource_cost": 0.015571248340931751
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 43.23915767458842,
    "beneficial_raw_gain_per_resource_cost": 648.5873651188263,
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
    "accrued_cost": 2.856137306098885,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.12005317009159165,
    "accrued_cost_fraction_initial_cap": 0.09520457686996282,
    "mean_contract_rate": 0.04018768478084647,
    "maximum_ledger_error": 5.082197683525802e-20
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
    "maximum_relative_cash_error": 2.131247506918235e-15,
    "maximum_absolute_share_error": 1.4432899320127035e-15,
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
      "minimum": -0.2202466602942629,
      "maximum": -0.04869990371785114,
      "mean": -0.1469050882989427,
      "median": -0.1483788444783913,
      "quantile_05": -0.20543672544736677,
      "quantile_95": -0.079283027081208
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
      "minimum": 0.25840297300382803,
      "maximum": 0.8126130272295515,
      "mean": 0.5774579222003595,
      "median": 0.6034426646745934,
      "quantile_05": 0.3363465174032899,
      "quantile_95": 0.7371760409135842
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
        "daily_volatility": 0.018902004839262677,
        "excess_kurtosis": 4.978584652919347,
        "return_acf_1": -0.04869990371785114,
        "abs_return_acf_1": 0.3083294601979191,
        "abs_return_acf_5": 0.3362891018815631,
        "abs_return_acf_20": 0.2596993302734102,
        "quantile_01": -0.05271994640150362,
        "quantile_99": 0.054971473375307736,
        "hill_tail_index": 3.961844652393317
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.0209759643731883,
        "excess_kurtosis": 6.533657317965025,
        "return_acf_1": -0.16315510299195893,
        "abs_return_acf_1": 0.5059282954816882,
        "abs_return_acf_5": 0.3976311522649961,
        "abs_return_acf_20": 0.33840639559209995,
        "quantile_01": -0.07105072937020594,
        "quantile_99": 0.05744824472607831,
        "hill_tail_index": 3.903610061686621
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02167128032960809,
        "excess_kurtosis": 6.940803981449511,
        "return_acf_1": -0.18356932330025075,
        "abs_return_acf_1": 0.4000436130449762,
        "abs_return_acf_5": 0.3829042739954775,
        "abs_return_acf_20": 0.33914685753065615,
        "quantile_01": -0.07286881677525665,
        "quantile_99": 0.0642479187224621,
        "hill_tail_index": 3.8254289139096382
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02147530356964674,
        "excess_kurtosis": 6.839858914946573,
        "return_acf_1": -0.1529864479324856,
        "abs_return_acf_1": 0.45420985865733543,
        "abs_return_acf_5": 0.4399921711044375,
        "abs_return_acf_20": 0.3020073336398002,
        "quantile_01": -0.0726508891125584,
        "quantile_99": 0.06017409533729524,
        "hill_tail_index": 4.241338517934168
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019399066554370792,
        "excess_kurtosis": 10.169700568105412,
        "return_acf_1": -0.13831278256560173,
        "abs_return_acf_1": 0.40656016465909056,
        "abs_return_acf_5": 0.3502256444717735,
        "abs_return_acf_20": 0.312664186330591,
        "quantile_01": -0.0662356336397481,
        "quantile_99": 0.049246929023400304,
        "hill_tail_index": 2.642448892358231
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01895652980753591,
        "excess_kurtosis": 7.440986046787797,
        "return_acf_1": -0.09480523969185241,
        "abs_return_acf_1": 0.3659164753779827,
        "abs_return_acf_5": 0.34450049771165614,
        "abs_return_acf_20": 0.27280238060539375,
        "quantile_01": -0.07464144115362552,
        "quantile_99": 0.05176800345245258,
        "hill_tail_index": 2.982864874260367
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021290129283144308,
        "excess_kurtosis": 9.549782037353769,
        "return_acf_1": -0.14377124102429703,
        "abs_return_acf_1": 0.5046426723366223,
        "abs_return_acf_5": 0.47655845523787144,
        "abs_return_acf_20": 0.32416518575493025,
        "quantile_01": -0.0683574571284225,
        "quantile_99": 0.060829196861458365,
        "hill_tail_index": 3.646679580116615
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018327633233116647,
        "excess_kurtosis": 5.46110013599392,
        "return_acf_1": -0.18820784055829526,
        "abs_return_acf_1": 0.340319730024618,
        "abs_return_acf_5": 0.26586363639576494,
        "abs_return_acf_20": 0.23895745221081943,
        "quantile_01": -0.056369453459720234,
        "quantile_99": 0.04877649424314608,
        "hill_tail_index": 3.203424941005647
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02090973515624989,
        "excess_kurtosis": 5.726295933383522,
        "return_acf_1": -0.10946955658849818,
        "abs_return_acf_1": 0.35385879875877246,
        "abs_return_acf_5": 0.38187804536072606,
        "abs_return_acf_20": 0.27185062058440973,
        "quantile_01": -0.07282361401803567,
        "quantile_99": 0.06251083581634533,
        "hill_tail_index": 4.397406046443876
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019858547410466026,
        "excess_kurtosis": 8.208653653871885,
        "return_acf_1": -0.16784942572581638,
        "abs_return_acf_1": 0.4529984372661783,
        "abs_return_acf_5": 0.34551046021381376,
        "abs_return_acf_20": 0.2894500431977372,
        "quantile_01": -0.07783390454988162,
        "quantile_99": 0.056821816836812505,
        "hill_tail_index": 3.2651617878888253
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02215990479234259,
        "excess_kurtosis": 8.866231319008437,
        "return_acf_1": -0.13740707240283803,
        "abs_return_acf_1": 0.3485140590062809,
        "abs_return_acf_5": 0.3570340911197006,
        "abs_return_acf_20": 0.30929276720235954,
        "quantile_01": -0.07201278477639894,
        "quantile_99": 0.06139323140543549,
        "hill_tail_index": 3.660509088131182
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019381857020763088,
        "excess_kurtosis": 9.168691353895047,
        "return_acf_1": -0.15599280647638822,
        "abs_return_acf_1": 0.39982577650387996,
        "abs_return_acf_5": 0.33333403055134603,
        "abs_return_acf_20": 0.30254111575383663,
        "quantile_01": -0.07259275874725195,
        "quantile_99": 0.06056399434000801,
        "hill_tail_index": 3.656048435413023
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019129893452913636,
        "excess_kurtosis": 7.0548197951250895,
        "return_acf_1": -0.1598809180826581,
        "abs_return_acf_1": 0.33045279325427984,
        "abs_return_acf_5": 0.38174162520542904,
        "abs_return_acf_20": 0.24755680857375914,
        "quantile_01": -0.06696689970185712,
        "quantile_99": 0.05854238954153918,
        "hill_tail_index": 4.403842687717546
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.0220127169095341,
        "excess_kurtosis": 9.40876753114497,
        "return_acf_1": -0.14232569063715783,
        "abs_return_acf_1": 0.5375947991058408,
        "abs_return_acf_5": 0.41096543896188936,
        "abs_return_acf_20": 0.3188609005820088,
        "quantile_01": -0.07341763882192728,
        "quantile_99": 0.06804187540121932,
        "hill_tail_index": 3.391512655379686
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01779644560860119,
        "excess_kurtosis": 5.241097705713232,
        "return_acf_1": -0.06658303494522608,
        "abs_return_acf_1": 0.2383966634266635,
        "abs_return_acf_5": 0.25696308827649583,
        "abs_return_acf_20": 0.22042499678638333,
        "quantile_01": -0.05138065512303811,
        "quantile_99": 0.049520385795872694,
        "hill_tail_index": 3.6992761162844556
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020250689897190338,
        "excess_kurtosis": 9.897077887556673,
        "return_acf_1": -0.13587568471975403,
        "abs_return_acf_1": 0.42325302189025915,
        "abs_return_acf_5": 0.32877401620339514,
        "abs_return_acf_20": 0.28710650951016287,
        "quantile_01": -0.0710368697904685,
        "quantile_99": 0.05501558241666012,
        "hill_tail_index": 2.8577538441964268
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.0200814119073346,
        "excess_kurtosis": 6.275390661383362,
        "return_acf_1": -0.17359322335513946,
        "abs_return_acf_1": 0.4010745990357613,
        "abs_return_acf_5": 0.453617526962731,
        "abs_return_acf_20": 0.30850390992411814,
        "quantile_01": -0.06776883475960432,
        "quantile_99": 0.05646984227669085,
        "hill_tail_index": 3.0690144736937084
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020044414560835496,
        "excess_kurtosis": 10.995825189513464,
        "return_acf_1": -0.12609609545194808,
        "abs_return_acf_1": 0.36044382613653403,
        "abs_return_acf_5": 0.30760860673367324,
        "abs_return_acf_20": 0.2717382088732715,
        "quantile_01": -0.056929194032749535,
        "quantile_99": 0.054934243508473465,
        "hill_tail_index": 2.9952310596876237
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.0215683015866155,
        "excess_kurtosis": 11.606290278895187,
        "return_acf_1": -0.18582151158008622,
        "abs_return_acf_1": 0.44213226933742406,
        "abs_return_acf_5": 0.48968288010808897,
        "abs_return_acf_20": 0.35263496012163426,
        "quantile_01": -0.07730311027628331,
        "quantile_99": 0.0593769455726754,
        "hill_tail_index": 3.211885271195829
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019752090076747587,
        "excess_kurtosis": 9.73027531222322,
        "return_acf_1": -0.1701766502017565,
        "abs_return_acf_1": 0.4843742843798948,
        "abs_return_acf_5": 0.3342130083824637,
        "abs_return_acf_20": 0.31767653738641977,
        "quantile_01": -0.07475323344367661,
        "quantile_99": 0.0510740274257161,
        "hill_tail_index": 2.518778230165358
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02047216056114923,
        "excess_kurtosis": 9.347089541227293,
        "return_acf_1": -0.13923067368807515,
        "abs_return_acf_1": 0.4123354771347824,
        "abs_return_acf_5": 0.3930810717756379,
        "abs_return_acf_20": 0.31237553689037345,
        "quantile_01": -0.07727867207349727,
        "quantile_99": 0.05665622511820366,
        "hill_tail_index": 2.7741147432955047
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0198474328854545,
        "excess_kurtosis": 7.435058644408345,
        "return_acf_1": -0.2202466602942629,
        "abs_return_acf_1": 0.5597335654401082,
        "abs_return_acf_5": 0.4320546214476373,
        "abs_return_acf_20": 0.2973014141525453,
        "quantile_01": -0.07053721654246874,
        "quantile_99": 0.05874491101241365,
        "hill_tail_index": 3.8924152219706962
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02021653680483597,
        "excess_kurtosis": 7.998523880584184,
        "return_acf_1": -0.12446046443642145,
        "abs_return_acf_1": 0.3433328459368753,
        "abs_return_acf_5": 0.3169282370105573,
        "abs_return_acf_20": 0.22143833038048355,
        "quantile_01": -0.06185220960096526,
        "quantile_99": 0.05357403680230921,
        "hill_tail_index": 3.3950913866509986
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020213193976381987,
        "excess_kurtosis": 9.255363347743756,
        "return_acf_1": -0.11550888140828135,
        "abs_return_acf_1": 0.41200621264405685,
        "abs_return_acf_5": 0.33889609292264256,
        "abs_return_acf_20": 0.3354251979331545,
        "quantile_01": -0.06846014103367642,
        "quantile_99": 0.05766637945211715,
        "hill_tail_index": 3.251956354302816
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01986265303433238,
        "excess_kurtosis": 5.089992222064437,
        "return_acf_1": -0.15349650033990264,
        "abs_return_acf_1": 0.3120704133330705,
        "abs_return_acf_5": 0.2943241099497163,
        "abs_return_acf_20": 0.24567086120895662,
        "quantile_01": -0.05660607268544354,
        "quantile_99": 0.06446254142446092,
        "hill_tail_index": 3.939633162968406
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019884671975220376,
        "excess_kurtosis": 5.9546324154577555,
        "return_acf_1": -0.21953308581115258,
        "abs_return_acf_1": 0.40074518323007646,
        "abs_return_acf_5": 0.3611728776868565,
        "abs_return_acf_20": 0.346164868938075,
        "quantile_01": -0.0684183192796216,
        "quantile_99": 0.06026741225867369,
        "hill_tail_index": 4.44573748840022
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021462189840821603,
        "excess_kurtosis": 12.89400042676627,
        "return_acf_1": -0.13617738878854524,
        "abs_return_acf_1": 0.4762174405742568,
        "abs_return_acf_5": 0.4668477421660326,
        "abs_return_acf_20": 0.29480311217643584,
        "quantile_01": -0.07655941192544306,
        "quantile_99": 0.06766553190742164,
        "hill_tail_index": 3.29015686001111
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021673540338580082,
        "excess_kurtosis": 8.580726284233473,
        "return_acf_1": -0.12224164114026756,
        "abs_return_acf_1": 0.3543760019485158,
        "abs_return_acf_5": 0.3863540410811257,
        "abs_return_acf_20": 0.34972746156463236,
        "quantile_01": -0.07124034015044348,
        "quantile_99": 0.06342345996482211,
        "hill_tail_index": 3.4420751311404127
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020414243665796434,
        "excess_kurtosis": 10.533429017561758,
        "return_acf_1": -0.17340483449670746,
        "abs_return_acf_1": 0.459422056684199,
        "abs_return_acf_5": 0.3919895673141754,
        "abs_return_acf_20": 0.3388734889907498,
        "quantile_01": -0.0783153435298705,
        "quantile_99": 0.05441689872824464,
        "hill_tail_index": 2.2896315780453884
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020668432856786653,
        "excess_kurtosis": 8.18525626360996,
        "return_acf_1": -0.1582729666148041,
        "abs_return_acf_1": 0.3906258728664905,
        "abs_return_acf_5": 0.3371174318087054,
        "abs_return_acf_20": 0.3224443141386231,
        "quantile_01": -0.07019574345798997,
        "quantile_99": 0.0537392757563837,
        "hill_tail_index": 2.4864513881316572
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
Unseen state share: 0.0022222222222222222
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
