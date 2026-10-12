# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27165
Run ID: `40482150b14f7a4734225026e5a2a54cf3eeaba17f45f3d0812f812ad4f902b5`
Result fingerprint: `ad9058b34a39fd33b1ee3a16a16511b82ca233433f11c8a90e43ef57b44fcc23`

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
    "equal_weight_sd": -0.6325476190476158,
    "equal_weight_raw": -9.488214285714237,
    "fixed_start_cap_weight_sd": -0.6156359668843101,
    "fixed_start_cap_weight_raw": -9.234539503264651,
    "end_cap_weight_sd": -0.6128237686291677,
    "end_cap_weight_raw": -9.192356529437516
  },
  "full_period_change": {
    "equal_weight_sd": -1.018154761904757,
    "equal_weight_raw": -15.272321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9537655423280379,
    "inflation_mean_sd": 0.4729953703703704
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.31983333333333647,
    "equal_weight_raw": 4.797500000000047,
    "fixed_start_cap_weight_sd": 0.3367449854966425,
    "fixed_start_cap_weight_raw": 5.051174782449636,
    "end_cap_weight_sd": 0.33955718375178456,
    "end_cap_weight_raw": 5.093357756276768
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5240476190476157,
      "change_raw": -7.860714285714235,
      "decay_adjusted_gain_sd": 0.4283333333333366
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6762698412698379,
      "change_raw": -10.14404761904757,
      "decay_adjusted_gain_sd": 0.2761111111111142
    },
    "small": {
      "count": 18,
      "change_sd": -0.6287698412698381,
      "change_raw": -9.431547619047572,
      "decay_adjusted_gain_sd": 0.32361111111111435
    },
    "large_minus_small_sd": 0.1047222222222225,
    "large_minus_small_raw": 1.5708333333333373
  },
  "inflation": {
    "initial_mean_sd": 0.2706666666666667,
    "final_mean_sd": 0.49425,
    "mean_sd": 0.38711705523175133,
    "mean_absolute_raw_gap": 5.806755828476271,
    "final_absolute_raw_gap": 7.413749999999999,
    "mean_range_fraction": 0.058067558284762705
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.27218647744834806,
    "final_wealth_share": 0.41520104795768215
  },
  "pricing_slope": {
    "mean": -0.0007849110981062703,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.1065368562809847,
    "real_improvement_cost": 0.09157304083283828,
    "washing_cost": 0.01496381544814642,
    "fine_transfer": 0.011559069774930451,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11809592605591515,
    "resource_cost_fraction_initial_cap": 0.0035512285426994904,
    "private_net_outflow_fraction_initial_cap": 0.003936530868530506,
    "fine_transfer_fraction_initial_cap": 0.0003853023258310151,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005286967458025827,
    "unapplied_final_day_resource_cost": 0.0018361338404528735
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 90.06272885219971,
    "beneficial_raw_gain_per_resource_cost": 1350.9409327829958,
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
    "accrued_cost": 2.983716824122884,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.0075263479324082505,
    "accrued_cost_fraction_initial_cap": 0.09945722747076281,
    "mean_contract_rate": 0.04159698759833345,
    "maximum_ledger_error": 7.326834993749698e-20
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
    "maximum_relative_cash_error": 2.1348330018089124e-15,
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
      "minimum": -0.23163815451503278,
      "maximum": -0.07511746219400131,
      "mean": -0.1683828853219972,
      "median": -0.17059435561022257,
      "quantile_05": -0.22277513128184084,
      "quantile_95": -0.09087772634928143
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
      "minimum": 0.09246053081653338,
      "maximum": 0.8491028844676668,
      "mean": 0.637691324227801,
      "median": 0.7594383952972714,
      "quantile_05": 0.17066851337311031,
      "quantile_95": 0.8223042746791187
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
        "daily_volatility": 0.02299643025709793,
        "excess_kurtosis": 13.573677161007357,
        "return_acf_1": -0.22363070689894357,
        "abs_return_acf_1": 0.5208961610702244,
        "abs_return_acf_5": 0.32997401760919254,
        "abs_return_acf_20": 0.3398710420448877,
        "quantile_01": -0.09064977771455995,
        "quantile_99": 0.060896488759690136,
        "hill_tail_index": 2.31872078215858
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021881006824605715,
        "excess_kurtosis": 18.449466216804,
        "return_acf_1": -0.1964834405952081,
        "abs_return_acf_1": 0.4463925671819363,
        "abs_return_acf_5": 0.3277948796391497,
        "abs_return_acf_20": 0.3667564926003422,
        "quantile_01": -0.0771892912411146,
        "quantile_99": 0.06590547794810495,
        "hill_tail_index": 2.597585835232081
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020670074900056033,
        "excess_kurtosis": 16.567855563135666,
        "return_acf_1": -0.14487739531707233,
        "abs_return_acf_1": 0.48236823565674675,
        "abs_return_acf_5": 0.2620615774141148,
        "abs_return_acf_20": 0.3769983172379953,
        "quantile_01": -0.06576849930949215,
        "quantile_99": 0.057220540008907306,
        "hill_tail_index": 2.3094447148014754
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019609404905714816,
        "excess_kurtosis": 5.99888025945161,
        "return_acf_1": -0.08821155057103365,
        "abs_return_acf_1": 0.37017951358670986,
        "abs_return_acf_5": 0.3077806519265322,
        "abs_return_acf_20": 0.23564497692146683,
        "quantile_01": -0.05800866838472373,
        "quantile_99": 0.058747302923948856,
        "hill_tail_index": 3.5351596758729826
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021098996758567516,
        "excess_kurtosis": 16.4900893047425,
        "return_acf_1": -0.18919523593573184,
        "abs_return_acf_1": 0.5226292556937916,
        "abs_return_acf_5": 0.3113661857508684,
        "abs_return_acf_20": 0.46938816422884017,
        "quantile_01": -0.0731509627848432,
        "quantile_99": 0.045891779718863254,
        "hill_tail_index": 1.9941777050415952
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021652760181386246,
        "excess_kurtosis": 8.721422644639066,
        "return_acf_1": -0.22172942774982637,
        "abs_return_acf_1": 0.38191919147985426,
        "abs_return_acf_5": 0.40073637691090847,
        "abs_return_acf_20": 0.30737738255820174,
        "quantile_01": -0.06296073920445375,
        "quantile_99": 0.06589640655164082,
        "hill_tail_index": 3.285192587365278
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02068737207699668,
        "excess_kurtosis": 24.855721417711102,
        "return_acf_1": -0.18574802737853716,
        "abs_return_acf_1": 0.48204226006492634,
        "abs_return_acf_5": 0.391388640609573,
        "abs_return_acf_20": 0.3279233120627661,
        "quantile_01": -0.07726540671201743,
        "quantile_99": 0.04499742441822124,
        "hill_tail_index": 1.6205035415619649
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022625385086478364,
        "excess_kurtosis": 26.768452670890024,
        "return_acf_1": -0.1598843300016308,
        "abs_return_acf_1": 0.5587038299226973,
        "abs_return_acf_5": 0.42204114138384696,
        "abs_return_acf_20": 0.4156074503035649,
        "quantile_01": -0.07858557525107521,
        "quantile_99": 0.05346489912386892,
        "hill_tail_index": 1.8046025177697496
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02104181090102798,
        "excess_kurtosis": 5.777676829505383,
        "return_acf_1": -0.17014650057463335,
        "abs_return_acf_1": 0.3459967859675198,
        "abs_return_acf_5": 0.28390780107418967,
        "abs_return_acf_20": 0.3297493061740476,
        "quantile_01": -0.06815576100014674,
        "quantile_99": 0.056701110800170415,
        "hill_tail_index": 3.9713394475913275
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021206147616197768,
        "excess_kurtosis": 20.50545813023128,
        "return_acf_1": -0.13866974149588307,
        "abs_return_acf_1": 0.5234106651565772,
        "abs_return_acf_5": 0.34893645820159663,
        "abs_return_acf_20": 0.4014382713359387,
        "quantile_01": -0.07279592603114998,
        "quantile_99": 0.054913354069948704,
        "hill_tail_index": 2.552273587170068
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.023513566301888476,
        "excess_kurtosis": 19.972481924376584,
        "return_acf_1": -0.17104221064581182,
        "abs_return_acf_1": 0.5320094835002923,
        "abs_return_acf_5": 0.3054631321484344,
        "abs_return_acf_20": 0.4116120821375993,
        "quantile_01": -0.08102487309923068,
        "quantile_99": 0.0699475004556067,
        "hill_tail_index": 2.2640729710399445
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021881819697567504,
        "excess_kurtosis": 21.869203575822727,
        "return_acf_1": -0.23163815451503278,
        "abs_return_acf_1": 0.5238519937913269,
        "abs_return_acf_5": 0.3233826973576348,
        "abs_return_acf_20": 0.4072831958596955,
        "quantile_01": -0.07338595102665975,
        "quantile_99": 0.05663881531305537,
        "hill_tail_index": 2.442023468289605
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018262968022060764,
        "excess_kurtosis": 2.5659722596682997,
        "return_acf_1": -0.12335231668509639,
        "abs_return_acf_1": 0.2963105406864965,
        "abs_return_acf_5": 0.24231226667736544,
        "abs_return_acf_20": 0.20689618217350647,
        "quantile_01": -0.05393289715635772,
        "quantile_99": 0.0533002087069137,
        "hill_tail_index": 4.402425016648401
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023031988486043056,
        "excess_kurtosis": 19.070192811716126,
        "return_acf_1": -0.18309547300674706,
        "abs_return_acf_1": 0.47831187217204246,
        "abs_return_acf_5": 0.35627295035727485,
        "abs_return_acf_20": 0.39782461746443726,
        "quantile_01": -0.08212770165550685,
        "quantile_99": 0.06116212405955115,
        "hill_tail_index": 2.277954890088067
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022753874154959306,
        "excess_kurtosis": 23.59957014935957,
        "return_acf_1": -0.19720773764860633,
        "abs_return_acf_1": 0.5550695941303635,
        "abs_return_acf_5": 0.41579884829664887,
        "abs_return_acf_20": 0.4324535230695372,
        "quantile_01": -0.08376822484226118,
        "quantile_99": 0.059105907031092586,
        "hill_tail_index": 2.2289039894643023
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022637500896313025,
        "excess_kurtosis": 22.651824945321312,
        "return_acf_1": -0.09413638563380647,
        "abs_return_acf_1": 0.5114372523473277,
        "abs_return_acf_5": 0.3943648787093698,
        "abs_return_acf_20": 0.39621491907027556,
        "quantile_01": -0.07663842030400854,
        "quantile_99": 0.05960335496265349,
        "hill_tail_index": 2.2620690243708697
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021250160350549743,
        "excess_kurtosis": 16.468653993619647,
        "return_acf_1": -0.14986391057614631,
        "abs_return_acf_1": 0.44414551541208075,
        "abs_return_acf_5": 0.3552308328860191,
        "abs_return_acf_20": 0.3251502874006071,
        "quantile_01": -0.06000035488013792,
        "quantile_99": 0.04868612251927566,
        "hill_tail_index": 1.925222659065823
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02516535515170429,
        "excess_kurtosis": 34.686358622808804,
        "return_acf_1": -0.14011676621158228,
        "abs_return_acf_1": 0.5568990852408695,
        "abs_return_acf_5": 0.47138126349334897,
        "abs_return_acf_20": 0.3514280147979505,
        "quantile_01": -0.07812486788730734,
        "quantile_99": 0.06360495864016602,
        "hill_tail_index": 1.690391571418068
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021859052985230266,
        "excess_kurtosis": 15.122296829215692,
        "return_acf_1": -0.18472086273946114,
        "abs_return_acf_1": 0.4856870122790094,
        "abs_return_acf_5": 0.32776859833252303,
        "abs_return_acf_20": 0.43202856208296414,
        "quantile_01": -0.06883038872747378,
        "quantile_99": 0.05885793307835691,
        "hill_tail_index": 2.582673758300585
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020127451342507145,
        "excess_kurtosis": 15.699136444840079,
        "return_acf_1": -0.1577591449346816,
        "abs_return_acf_1": 0.43344449043454397,
        "abs_return_acf_5": 0.3619528643419176,
        "abs_return_acf_20": 0.38465858464464964,
        "quantile_01": -0.06179373565272615,
        "quantile_99": 0.0597106765741606,
        "hill_tail_index": 2.22589837879227
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017680751627398558,
        "excess_kurtosis": 5.008533347197483,
        "return_acf_1": -0.07511746219400131,
        "abs_return_acf_1": 0.23867221332412442,
        "abs_return_acf_5": 0.25395068230920215,
        "abs_return_acf_20": 0.23034212506920915,
        "quantile_01": -0.05677363783780051,
        "quantile_99": 0.054427050727873474,
        "hill_tail_index": 3.8883584456530684
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022255045623271668,
        "excess_kurtosis": 26.028719162380586,
        "return_acf_1": -0.1774181050090503,
        "abs_return_acf_1": 0.5507160761821902,
        "abs_return_acf_5": 0.4251737255253908,
        "abs_return_acf_20": 0.4365041767661568,
        "quantile_01": -0.08591753617826214,
        "quantile_99": 0.05592677292499342,
        "hill_tail_index": 1.8340281521701658
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02132406137181648,
        "excess_kurtosis": 24.373802660229877,
        "return_acf_1": -0.15460359044046437,
        "abs_return_acf_1": 0.469497196168816,
        "abs_return_acf_5": 0.48940569715659965,
        "abs_return_acf_20": 0.3303040114296051,
        "quantile_01": -0.07546617395416971,
        "quantile_99": 0.05840016370223986,
        "hill_tail_index": 2.2293261875000985
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023761341653963704,
        "excess_kurtosis": 35.518405549018745,
        "return_acf_1": -0.22009474798494116,
        "abs_return_acf_1": 0.5842218709930035,
        "abs_return_acf_5": 0.4222072786417702,
        "abs_return_acf_20": 0.30418298368675994,
        "quantile_01": -0.07946339870549177,
        "quantile_99": 0.061854940721927446,
        "hill_tail_index": 1.6174084165928633
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02282812520861475,
        "excess_kurtosis": 25.207174054923005,
        "return_acf_1": -0.13776563825482743,
        "abs_return_acf_1": 0.4796758775209891,
        "abs_return_acf_5": 0.3257361091230928,
        "abs_return_acf_20": 0.41798439500508655,
        "quantile_01": -0.07472155451769222,
        "quantile_99": 0.04735582908484423,
        "hill_tail_index": 2.16864738188734
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.023753913774302787,
        "excess_kurtosis": 29.389283936104185,
        "return_acf_1": -0.18253077692713265,
        "abs_return_acf_1": 0.51328406390738,
        "abs_return_acf_5": 0.366157549765926,
        "abs_return_acf_20": 0.41534951536102127,
        "quantile_01": -0.09134808557078915,
        "quantile_99": 0.059521198365189605,
        "hill_tail_index": 1.8098824260010666
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021158619174671028,
        "excess_kurtosis": 23.06238584086841,
        "return_acf_1": -0.20684233333509264,
        "abs_return_acf_1": 0.47744086088018445,
        "abs_return_acf_5": 0.41891887028515307,
        "abs_return_acf_20": 0.34671009340844605,
        "quantile_01": -0.05969892551383991,
        "quantile_99": 0.04785424985861629,
        "hill_tail_index": 1.685782502881913
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022528225740216404,
        "excess_kurtosis": 28.16692541068018,
        "return_acf_1": -0.16162067856741388,
        "abs_return_acf_1": 0.5108500501112552,
        "abs_return_acf_5": 0.3807250748892991,
        "abs_return_acf_20": 0.4012559090525964,
        "quantile_01": -0.0714796018809336,
        "quantile_99": 0.061283624316160634,
        "hill_tail_index": 1.8948883637077287
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02249889454378959,
        "excess_kurtosis": 19.48522739098672,
        "return_acf_1": -0.16311989983428749,
        "abs_return_acf_1": 0.5537609021634625,
        "abs_return_acf_5": 0.3966088556812608,
        "abs_return_acf_20": 0.4504865326875409,
        "quantile_01": -0.08241363506055512,
        "quantile_99": 0.06588390205743078,
        "hill_tail_index": 1.9751595223216798
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02220280341181109,
        "excess_kurtosis": 15.999359337331668,
        "return_acf_1": -0.22086400799723205,
        "abs_return_acf_1": 0.4906438721020428,
        "abs_return_acf_5": 0.37758197204773875,
        "abs_return_acf_20": 0.36220439113538416,
        "quantile_01": -0.07943892551651971,
        "quantile_99": 0.06605673016892834,
        "hill_tail_index": 2.237928901975456
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
