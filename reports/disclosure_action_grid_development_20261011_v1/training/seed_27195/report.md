# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27195
Run ID: `5ca52e13a0fa273d92a159a2715463ad5d8b8bc9cb3068e4266cd24ba426a498`
Result fingerprint: `7a4847f081a5e506d49043a1d0f1dc536164a90dfc6dee0158b8a8122a05a0b8`

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
    "equal_weight_sd": -0.6793809523809492,
    "equal_weight_raw": -10.19071428571424,
    "fixed_start_cap_weight_sd": -0.6645963724565626,
    "fixed_start_cap_weight_raw": -9.968945586848434,
    "end_cap_weight_sd": -0.6741965699859515,
    "end_cap_weight_raw": -10.112948549789271
  },
  "full_period_change": {
    "equal_weight_sd": -1.044654761904757,
    "equal_weight_raw": -15.669821428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9809976851851807,
    "inflation_mean_sd": 0.503479828042328
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.27300000000000313,
    "equal_weight_raw": 4.095000000000047,
    "fixed_start_cap_weight_sd": 0.28778457992439005,
    "fixed_start_cap_weight_raw": 4.316768698865849,
    "end_cap_weight_sd": 0.278184382395001,
    "end_cap_weight_raw": 4.172765735925014
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6332142857142834,
      "change_raw": -9.498214285714251,
      "decay_adjusted_gain_sd": 0.3191666666666688
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6959920634920602,
      "change_raw": -10.439880952380904,
      "decay_adjusted_gain_sd": 0.25638888888889216
    },
    "small": {
      "count": 18,
      "change_sd": -0.6787698412698379,
      "change_raw": -10.181547619047567,
      "decay_adjusted_gain_sd": 0.27361111111111436
    },
    "large_minus_small_sd": 0.04555555555555446,
    "large_minus_small_raw": 0.6833333333333169
  },
  "inflation": {
    "initial_mean_sd": 0.31449999999999995,
    "final_mean_sd": 0.4946666666666666,
    "mean_sd": 0.40897696364140995,
    "mean_absolute_raw_gap": 6.134654454621149,
    "final_absolute_raw_gap": 7.419999999999999,
    "mean_range_fraction": 0.06134654454621149
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.20666666666666667,
    "initial_wealth_share": 0.16510469157195007,
    "final_wealth_share": 0.18324191623949587
  },
  "pricing_slope": {
    "mean": -0.0021019421318499336,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.02917760038642727,
    "real_improvement_cost": 0.023072801132794033,
    "washing_cost": 0.006104799253633239,
    "fine_transfer": 0.03162658693374379,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06080418732017106,
    "resource_cost_fraction_initial_cap": 0.0009725866795475758,
    "private_net_outflow_fraction_initial_cap": 0.0020268062440057023,
    "fine_transfer_fraction_initial_cap": 0.0010542195644581264,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004865306162632319,
    "unapplied_final_day_resource_cost": 0.0009042174347436767
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 280.6947758394103,
    "beneficial_raw_gain_per_resource_cost": 4210.421637591155,
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
    "accrued_cost": 2.909423866863924,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.06676660932655208,
    "accrued_cost_fraction_initial_cap": 0.09698079556213081,
    "mean_contract_rate": 0.03774345083929236,
    "maximum_ledger_error": 2.507217523872729e-19
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
    "maximum_relative_cash_error": 1.8144253766745496e-15,
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
      "minimum": -0.20474239376059475,
      "maximum": -0.017060660773141854,
      "mean": -0.13148303689630422,
      "median": -0.1432513384769496,
      "quantile_05": -0.19773482327348105,
      "quantile_95": -0.04511583615614019
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
      "minimum": 0.44004031031611085,
      "maximum": 0.7614628927114769,
      "mean": 0.6525473849226514,
      "median": 0.6676952848003344,
      "quantile_05": 0.5203044676033592,
      "quantile_95": 0.7393770885753194
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
        "daily_volatility": 0.018784021046434993,
        "excess_kurtosis": 10.05903316556498,
        "return_acf_1": -0.11353024879255574,
        "abs_return_acf_1": 0.40350985781598103,
        "abs_return_acf_5": 0.3841976716010245,
        "abs_return_acf_20": 0.2840707454175518,
        "quantile_01": -0.05858451558973165,
        "quantile_99": 0.052285219763713885,
        "hill_tail_index": 2.7743479704933205
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019266528618078545,
        "excess_kurtosis": 12.084090540179304,
        "return_acf_1": -0.11626672236031724,
        "abs_return_acf_1": 0.46106256644478993,
        "abs_return_acf_5": 0.38162310110354897,
        "abs_return_acf_20": 0.27759474954589697,
        "quantile_01": -0.06086129855235091,
        "quantile_99": 0.04999258104591156,
        "hill_tail_index": 2.5183327249362852
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017477297120791917,
        "excess_kurtosis": 8.70515494030635,
        "return_acf_1": -0.15561515681741336,
        "abs_return_acf_1": 0.31249121927029555,
        "abs_return_acf_5": 0.26897894706896425,
        "abs_return_acf_20": 0.1899866894754593,
        "quantile_01": -0.059328413347508616,
        "quantile_99": 0.04273852796021442,
        "hill_tail_index": 2.732552898508165
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017898077482252406,
        "excess_kurtosis": 7.789768944414023,
        "return_acf_1": -0.16006896221189068,
        "abs_return_acf_1": 0.2523470453922064,
        "abs_return_acf_5": 0.261141631694534,
        "abs_return_acf_20": 0.18178852923877042,
        "quantile_01": -0.06289351227151833,
        "quantile_99": 0.04199792372349149,
        "hill_tail_index": 2.7497974151053213
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01805468371148205,
        "excess_kurtosis": 6.0798962750589,
        "return_acf_1": -0.1790647013173666,
        "abs_return_acf_1": 0.37593646868479985,
        "abs_return_acf_5": 0.35467805014338044,
        "abs_return_acf_20": 0.264190901492617,
        "quantile_01": -0.060952646308141234,
        "quantile_99": 0.041200505266831174,
        "hill_tail_index": 2.9660837719884685
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018280079457770194,
        "excess_kurtosis": 14.163895649061434,
        "return_acf_1": -0.04733335521864259,
        "abs_return_acf_1": 0.35252619250952716,
        "abs_return_acf_5": 0.35409528757007236,
        "abs_return_acf_20": 0.22896153383676396,
        "quantile_01": -0.05981297784866773,
        "quantile_99": 0.04040297464179891,
        "hill_tail_index": 2.4550941772490993
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01954933022651925,
        "excess_kurtosis": 11.584290275264612,
        "return_acf_1": -0.04330150237772911,
        "abs_return_acf_1": 0.38192230877202227,
        "abs_return_acf_5": 0.40374727956985595,
        "abs_return_acf_20": 0.3094357436865911,
        "quantile_01": -0.06480207026307129,
        "quantile_99": 0.049911912015324855,
        "hill_tail_index": 2.508060032320612
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01787474704331931,
        "excess_kurtosis": 7.502089109066258,
        "return_acf_1": -0.1390442362957443,
        "abs_return_acf_1": 0.35842457683850576,
        "abs_return_acf_5": 0.23148047106455036,
        "abs_return_acf_20": 0.2052074160434382,
        "quantile_01": -0.050511500857741004,
        "quantile_99": 0.05481472196712392,
        "hill_tail_index": 3.3553346748224873
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016974281544347422,
        "excess_kurtosis": 5.656270979884823,
        "return_acf_1": -0.20474239376059475,
        "abs_return_acf_1": 0.336774090557079,
        "abs_return_acf_5": 0.32123581579083643,
        "abs_return_acf_20": 0.1899223005564558,
        "quantile_01": -0.048609629499780906,
        "quantile_99": 0.045982351298005764,
        "hill_tail_index": 3.794043339781092
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018763837535755293,
        "excess_kurtosis": 6.93725797305912,
        "return_acf_1": -0.15540105080406538,
        "abs_return_acf_1": 0.378987232487787,
        "abs_return_acf_5": 0.3809865680581301,
        "abs_return_acf_20": 0.26336675989656294,
        "quantile_01": -0.06700252534158622,
        "quantile_99": 0.04611150069032997,
        "hill_tail_index": 3.7175678825150427
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018960153160452773,
        "excess_kurtosis": 7.944769801009873,
        "return_acf_1": -0.07416438114321922,
        "abs_return_acf_1": 0.39603024324746733,
        "abs_return_acf_5": 0.40283026670422667,
        "abs_return_acf_20": 0.308988747352151,
        "quantile_01": -0.06377679728285801,
        "quantile_99": 0.051951853787006244,
        "hill_tail_index": 3.0812844024566703
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018395693426726728,
        "excess_kurtosis": 8.685323448000712,
        "return_acf_1": -0.05637724586099803,
        "abs_return_acf_1": 0.4797451766102048,
        "abs_return_acf_5": 0.4196351463154416,
        "abs_return_acf_20": 0.27590844262857983,
        "quantile_01": -0.06116159929810317,
        "quantile_99": 0.04819677140924381,
        "hill_tail_index": 2.900640476587907
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018230457135224788,
        "excess_kurtosis": 3.64360712570544,
        "return_acf_1": -0.14927221833793416,
        "abs_return_acf_1": 0.3131237957807631,
        "abs_return_acf_5": 0.2857277713710448,
        "abs_return_acf_20": 0.25351388667374364,
        "quantile_01": -0.05575077499792581,
        "quantile_99": 0.046572652468603225,
        "hill_tail_index": 4.042738367752623
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017218007886417787,
        "excess_kurtosis": 7.065508387431686,
        "return_acf_1": -0.11134347388643062,
        "abs_return_acf_1": 0.33892423844786174,
        "abs_return_acf_5": 0.3220637248697607,
        "abs_return_acf_20": 0.22587655350287703,
        "quantile_01": -0.05793142253353982,
        "quantile_99": 0.042680624081377294,
        "hill_tail_index": 2.6407210595803785
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01693782399590986,
        "excess_kurtosis": 6.501789402528832,
        "return_acf_1": -0.1407571452211476,
        "abs_return_acf_1": 0.2887866360317699,
        "abs_return_acf_5": 0.2599372660013509,
        "abs_return_acf_20": 0.20570273112207904,
        "quantile_01": -0.04816730631278522,
        "quantile_99": 0.038677134839200135,
        "hill_tail_index": 3.463361390281312
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018423561003729518,
        "excess_kurtosis": 4.841408314347726,
        "return_acf_1": -0.19387928625791195,
        "abs_return_acf_1": 0.36390872870937335,
        "abs_return_acf_5": 0.37661507683315343,
        "abs_return_acf_20": 0.2581608164411115,
        "quantile_01": -0.05042247507456093,
        "quantile_99": 0.04978653126854692,
        "hill_tail_index": 3.5492546192861725
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018217232520585356,
        "excess_kurtosis": 6.399111220884057,
        "return_acf_1": -0.2008893535589467,
        "abs_return_acf_1": 0.3754882659203897,
        "abs_return_acf_5": 0.30143080448196385,
        "abs_return_acf_20": 0.2420019536120851,
        "quantile_01": -0.052048451422124865,
        "quantile_99": 0.05048185281825242,
        "hill_tail_index": 2.971619462776707
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017845587477132323,
        "excess_kurtosis": 6.531859014240865,
        "return_acf_1": -0.11706111759821869,
        "abs_return_acf_1": 0.3486180594930186,
        "abs_return_acf_5": 0.30110717417518473,
        "abs_return_acf_20": 0.21450634829223458,
        "quantile_01": -0.062148109687869976,
        "quantile_99": 0.047420368259626484,
        "hill_tail_index": 3.036086267655167
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019242499386022068,
        "excess_kurtosis": 18.266860022855212,
        "return_acf_1": -0.09297413689503008,
        "abs_return_acf_1": 0.38031989240645353,
        "abs_return_acf_5": 0.38498776486929703,
        "abs_return_acf_20": 0.23436887325194997,
        "quantile_01": -0.0678368116510727,
        "quantile_99": 0.042323074684361195,
        "hill_tail_index": 1.9369324082931056
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01768133037148793,
        "excess_kurtosis": 6.123706911636171,
        "return_acf_1": -0.17192691806552504,
        "abs_return_acf_1": 0.3391812222695386,
        "abs_return_acf_5": 0.29463669215320987,
        "abs_return_acf_20": 0.2593628204255921,
        "quantile_01": -0.05255271225570803,
        "quantile_99": 0.047382311241143386,
        "hill_tail_index": 4.002892979726712
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017664825163179944,
        "excess_kurtosis": 8.252541070713857,
        "return_acf_1": -0.162024192042949,
        "abs_return_acf_1": 0.384062530331123,
        "abs_return_acf_5": 0.3605838333842408,
        "abs_return_acf_20": 0.19728700006795377,
        "quantile_01": -0.057677775245517156,
        "quantile_99": 0.03974517116167811,
        "hill_tail_index": 2.707743556786784
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019566831215805595,
        "excess_kurtosis": 8.604285645894233,
        "return_acf_1": -0.1848491409615268,
        "abs_return_acf_1": 0.36248141633483444,
        "abs_return_acf_5": 0.36655894066762906,
        "abs_return_acf_20": 0.23618728601093858,
        "quantile_01": -0.06854890178211716,
        "quantile_99": 0.04556168104919582,
        "hill_tail_index": 2.828622749855486
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018003702058444676,
        "excess_kurtosis": 6.81092758426853,
        "return_acf_1": -0.16434946720906002,
        "abs_return_acf_1": 0.35871729360637317,
        "abs_return_acf_5": 0.37384784533168797,
        "abs_return_acf_20": 0.27048051983835325,
        "quantile_01": -0.05776616081771283,
        "quantile_99": 0.04328217955445512,
        "hill_tail_index": 2.94110113977554
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016963050017290243,
        "excess_kurtosis": 6.77297148563405,
        "return_acf_1": -0.14574553173275162,
        "abs_return_acf_1": 0.3224658707033421,
        "abs_return_acf_5": 0.27423083054226216,
        "abs_return_acf_20": 0.1926727042904354,
        "quantile_01": -0.04544664668288746,
        "quantile_99": 0.04606699343366961,
        "hill_tail_index": 3.825869058266332
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01946123091437615,
        "excess_kurtosis": 11.409542458137048,
        "return_acf_1": -0.07475229034118354,
        "abs_return_acf_1": 0.4370183693585976,
        "abs_return_acf_5": 0.39937580682508184,
        "abs_return_acf_20": 0.23458082599995542,
        "quantile_01": -0.06744373257601222,
        "quantile_99": 0.04325315296104524,
        "hill_tail_index": 2.8132305600882836
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018073577249424412,
        "excess_kurtosis": 8.041742028055102,
        "return_acf_1": -0.151333623193086,
        "abs_return_acf_1": 0.32549885268165074,
        "abs_return_acf_5": 0.3168751114034605,
        "abs_return_acf_20": 0.22827295503175404,
        "quantile_01": -0.061092793175156486,
        "quantile_99": 0.04666948593819063,
        "hill_tail_index": 2.8379814915245203
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017566253466731695,
        "excess_kurtosis": 4.998915992678951,
        "return_acf_1": -0.14815799430406615,
        "abs_return_acf_1": 0.34920804090474244,
        "abs_return_acf_5": 0.2866669202339737,
        "abs_return_acf_20": 0.22780302989153678,
        "quantile_01": -0.05312321460664651,
        "quantile_99": 0.043160315648209525,
        "hill_tail_index": 3.2104856361486163
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01845341394219641,
        "excess_kurtosis": 12.380382982763559,
        "return_acf_1": -0.017060660773141854,
        "abs_return_acf_1": 0.47933042532863346,
        "abs_return_acf_5": 0.37295793370752284,
        "abs_return_acf_20": 0.298936419431057,
        "quantile_01": -0.06234075230495805,
        "quantile_99": 0.04305096620224437,
        "hill_tail_index": 1.9927940500929404
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01912992457952267,
        "excess_kurtosis": 7.479047524329802,
        "return_acf_1": -0.13846825438505997,
        "abs_return_acf_1": 0.428429757239453,
        "abs_return_acf_5": 0.37948106701560885,
        "abs_return_acf_20": 0.2506373300707301,
        "quantile_01": -0.06052107151687719,
        "quantile_99": 0.05610574257629953,
        "hill_tail_index": 3.7865439914571426
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01810451579117489,
        "excess_kurtosis": 4.891096397821495,
        "return_acf_1": -0.1347363451646197,
        "abs_return_acf_1": 0.4673938315153626,
        "abs_return_acf_5": 0.40738371363767467,
        "abs_return_acf_20": 0.271107193394824,
        "quantile_01": -0.062071092160329626,
        "quantile_99": 0.05303463646971707,
        "hill_tail_index": 4.290968997338837
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
