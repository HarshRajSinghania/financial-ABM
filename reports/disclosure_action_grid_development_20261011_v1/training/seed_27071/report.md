# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27071
Run ID: `e1f519af5c99d95b21e296bc8508bc023f0c2cb4ef583637d265074f47828a3c`
Result fingerprint: `af18aef8f4ad68c7868d8cdea6a196b6e5b3344e1c7870333ea71b63dc87363b`

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
    "equal_weight_sd": -0.5630476190476158,
    "equal_weight_raw": -8.445714285714237,
    "fixed_start_cap_weight_sd": -0.54539234796621,
    "fixed_start_cap_weight_raw": -8.18088521949315,
    "end_cap_weight_sd": -0.581433600921336,
    "end_cap_weight_raw": -8.721504013820041
  },
  "full_period_change": {
    "equal_weight_sd": -0.8527380952380903,
    "equal_weight_raw": -12.791071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8030241402116357,
    "inflation_mean_sd": 0.5828763227513227
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3893333333333364,
    "equal_weight_raw": 5.840000000000047,
    "fixed_start_cap_weight_sd": 0.4069886044147422,
    "fixed_start_cap_weight_raw": 6.104829066221133,
    "end_cap_weight_sd": 0.3709473514596161,
    "end_cap_weight_raw": 5.564210271894241
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5298809523809491,
      "change_raw": -7.948214285714236,
      "decay_adjusted_gain_sd": 0.42250000000000315
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6168253968253936,
      "change_raw": -9.252380952380904,
      "decay_adjusted_gain_sd": 0.33555555555555866
    },
    "small": {
      "count": 18,
      "change_sd": -0.5416865079365046,
      "change_raw": -8.12529761904757,
      "decay_adjusted_gain_sd": 0.41069444444444764
    },
    "large_minus_small_sd": 0.011805555555555514,
    "large_minus_small_raw": 0.1770833333333327
  },
  "inflation": {
    "initial_mean_sd": 0.2530833333333334,
    "final_mean_sd": 0.6227499999999999,
    "mean_sd": 0.45989265889536507,
    "mean_absolute_raw_gap": 6.898389883430474,
    "final_absolute_raw_gap": 9.34125,
    "mean_range_fraction": 0.06898389883430474
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.36,
    "initial_wealth_share": 0.3534025782869674,
    "final_wealth_share": 0.46421092911745676
  },
  "pricing_slope": {
    "mean": -0.005269673038714418,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.26050538383482136,
    "real_improvement_cost": 0.2141590056151225,
    "washing_cost": 0.04634637821969882,
    "fine_transfer": 0.015014877218709607,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.27552026105353095,
    "resource_cost_fraction_initial_cap": 0.008683512794494046,
    "private_net_outflow_fraction_initial_cap": 0.009184008701784365,
    "fine_transfer_fraction_initial_cap": 0.0005004959072903203,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.011629610015797187,
    "unapplied_final_day_resource_cost": 0.028310946858756757
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 44.83592556922366,
    "beneficial_raw_gain_per_resource_cost": 672.538883538355,
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
    "accrued_cost": 2.8492580329559525,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": 0.12693244323452318,
    "accrued_cost_fraction_initial_cap": 0.09497526776519842,
    "mean_contract_rate": 0.0401006598063153,
    "maximum_ledger_error": 8.470329472543003e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 2.1196312731774744e-15,
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
      "minimum": -0.15978783083524428,
      "maximum": 0.02897521873831445,
      "mean": -0.06700558239546607,
      "median": -0.06854307390691658,
      "quantile_05": -0.13171375774430194,
      "quantile_95": 0.00208705267775227
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
      "minimum": 0.2305075979774713,
      "maximum": 0.7725136726712447,
      "mean": 0.5399906640047997,
      "median": 0.5764277627795211,
      "quantile_05": 0.281799513415771,
      "quantile_95": 0.7359536846603425
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
        "daily_volatility": 0.018297461579306284,
        "excess_kurtosis": 12.251799388177469,
        "return_acf_1": -0.07166621714527657,
        "abs_return_acf_1": 0.31882464124380505,
        "abs_return_acf_5": 0.30458831203789993,
        "abs_return_acf_20": 0.27727764732829524,
        "quantile_01": -0.06032677480492295,
        "quantile_99": 0.045138961559869226,
        "hill_tail_index": 2.777489724446942
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01969035190497795,
        "excess_kurtosis": 10.387133621624969,
        "return_acf_1": -0.08576561741493834,
        "abs_return_acf_1": 0.36040899955497535,
        "abs_return_acf_5": 0.32964844864466414,
        "abs_return_acf_20": 0.28767293558706986,
        "quantile_01": -0.0718294976392308,
        "quantile_99": 0.04860349614288224,
        "hill_tail_index": 2.4882215993030212
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019474154932071996,
        "excess_kurtosis": 3.60983414713189,
        "return_acf_1": -0.07504379752988555,
        "abs_return_acf_1": 0.3365671896852162,
        "abs_return_acf_5": 0.2802795467469003,
        "abs_return_acf_20": 0.33029985093686065,
        "quantile_01": -0.06416115760649087,
        "quantile_99": 0.05611686356662424,
        "hill_tail_index": 4.546621117822631
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020983834262816185,
        "excess_kurtosis": 9.013114478361407,
        "return_acf_1": -0.06224178667312819,
        "abs_return_acf_1": 0.30853733465715505,
        "abs_return_acf_5": 0.3222133948388515,
        "abs_return_acf_20": 0.3092028376170328,
        "quantile_01": -0.07350316572220139,
        "quantile_99": 0.05300721090210334,
        "hill_tail_index": 3.1454802666368304
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01853615546887512,
        "excess_kurtosis": 3.201897194159895,
        "return_acf_1": -0.07298349505808945,
        "abs_return_acf_1": 0.25036426385036387,
        "abs_return_acf_5": 0.2323873287496436,
        "abs_return_acf_20": 0.20829762905185778,
        "quantile_01": -0.05721582779576836,
        "quantile_99": 0.048565935273690505,
        "hill_tail_index": 4.033564563699202
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020728811225006374,
        "excess_kurtosis": 6.987681649886101,
        "return_acf_1": -0.10969876538767312,
        "abs_return_acf_1": 0.4410933836142933,
        "abs_return_acf_5": 0.3662299781419253,
        "abs_return_acf_20": 0.40591033128119125,
        "quantile_01": -0.06635700924018943,
        "quantile_99": 0.06758306823489325,
        "hill_tail_index": 3.9761453496814343
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020570277329028,
        "excess_kurtosis": 9.450334332918182,
        "return_acf_1": -0.0931311175101081,
        "abs_return_acf_1": 0.4171671826001994,
        "abs_return_acf_5": 0.37727305911901166,
        "abs_return_acf_20": 0.35272244451296886,
        "quantile_01": -0.07337217854765264,
        "quantile_99": 0.05664973399627113,
        "hill_tail_index": 3.4679804171080124
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017457039237652686,
        "excess_kurtosis": 10.722507109901702,
        "return_acf_1": -0.037512280371094,
        "abs_return_acf_1": 0.3276580648087894,
        "abs_return_acf_5": 0.2549303419299078,
        "abs_return_acf_20": 0.25125321241662935,
        "quantile_01": -0.055303232927088074,
        "quantile_99": 0.040321977800822646,
        "hill_tail_index": 2.1565978872639424
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016921177157511843,
        "excess_kurtosis": 7.757303714473162,
        "return_acf_1": -0.06541993066855657,
        "abs_return_acf_1": 0.30137117455192924,
        "abs_return_acf_5": 0.24307414847523123,
        "abs_return_acf_20": 0.2163128064291592,
        "quantile_01": -0.048595941733119055,
        "quantile_99": 0.04815455354931859,
        "hill_tail_index": 2.599579198999051
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01654499048939201,
        "excess_kurtosis": 2.818992687818067,
        "return_acf_1": -0.12474997756145315,
        "abs_return_acf_1": 0.23873534327886167,
        "abs_return_acf_5": 0.20902457303451905,
        "abs_return_acf_20": 0.23745322261657406,
        "quantile_01": -0.0510069860252375,
        "quantile_99": 0.05005966706323755,
        "hill_tail_index": 4.242874584146331
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018140452893608175,
        "excess_kurtosis": 12.00923148063686,
        "return_acf_1": 0.02897521873831445,
        "abs_return_acf_1": 0.3668446554099371,
        "abs_return_acf_5": 0.3598724947288029,
        "abs_return_acf_20": 0.3172375600037158,
        "quantile_01": -0.05709938404326515,
        "quantile_99": 0.046913808802448935,
        "hill_tail_index": 2.309892523913593
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015211406242487692,
        "excess_kurtosis": 1.9932146449344268,
        "return_acf_1": -0.08269612398871502,
        "abs_return_acf_1": 0.20588676465949232,
        "abs_return_acf_5": 0.18328063161759467,
        "abs_return_acf_20": 0.22189769494553124,
        "quantile_01": -0.04130460209237821,
        "quantile_99": 0.03949559287934357,
        "hill_tail_index": 4.097466706926338
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01702685222274391,
        "excess_kurtosis": 11.005859891225507,
        "return_acf_1": 0.010455541259484407,
        "abs_return_acf_1": 0.3595770322789553,
        "abs_return_acf_5": 0.3036364571288292,
        "abs_return_acf_20": 0.2945847381895381,
        "quantile_01": -0.05375689783620109,
        "quantile_99": 0.04252483456573003,
        "hill_tail_index": 2.291225518483507
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016981431862738653,
        "excess_kurtosis": 3.289327976486108,
        "return_acf_1": -0.027266022351657232,
        "abs_return_acf_1": 0.2835401121333904,
        "abs_return_acf_5": 0.2650703906592736,
        "abs_return_acf_20": 0.27238727451684563,
        "quantile_01": -0.05090364147731773,
        "quantile_99": 0.04550137349695069,
        "hill_tail_index": 3.642589044909596
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01723408387402908,
        "excess_kurtosis": 7.045188579339243,
        "return_acf_1": -0.13103430949223008,
        "abs_return_acf_1": 0.23649685315528998,
        "abs_return_acf_5": 0.22578040235716634,
        "abs_return_acf_20": 0.19713797201577216,
        "quantile_01": -0.05294431239124399,
        "quantile_99": 0.04874261385901448,
        "hill_tail_index": 3.0268881931812732
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01899359422048482,
        "excess_kurtosis": 8.674945935036646,
        "return_acf_1": -0.07459145637296326,
        "abs_return_acf_1": 0.33082824374112985,
        "abs_return_acf_5": 0.29171210959607546,
        "abs_return_acf_20": 0.27289616464319266,
        "quantile_01": -0.07071774809066003,
        "quantile_99": 0.05193822751567321,
        "hill_tail_index": 2.7266394215185135
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018776621836140456,
        "excess_kurtosis": 11.126006134745639,
        "return_acf_1": -0.05717066985813185,
        "abs_return_acf_1": 0.36524678918758996,
        "abs_return_acf_5": 0.3085296109031313,
        "abs_return_acf_20": 0.29186830561859134,
        "quantile_01": -0.0672959399311316,
        "quantile_99": 0.04395750310510559,
        "hill_tail_index": 2.708022899215773
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017792738375768943,
        "excess_kurtosis": 9.307074181353585,
        "return_acf_1": -0.03661915396568138,
        "abs_return_acf_1": 0.3228144949592282,
        "abs_return_acf_5": 0.22745207248177582,
        "abs_return_acf_20": 0.2185399442777886,
        "quantile_01": -0.06300155908375855,
        "quantile_99": 0.04885245390791533,
        "hill_tail_index": 2.6180852597060125
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.0177775080491374,
        "excess_kurtosis": 8.240390770930288,
        "return_acf_1": -0.027063453544904203,
        "abs_return_acf_1": 0.3446960265779566,
        "abs_return_acf_5": 0.27592852404013724,
        "abs_return_acf_20": 0.25746413296624576,
        "quantile_01": -0.05371820605157377,
        "quantile_99": 0.04944447436744943,
        "hill_tail_index": 3.375546227893049
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016478157495866355,
        "excess_kurtosis": 7.439117115176554,
        "return_acf_1": -0.13226966995054257,
        "abs_return_acf_1": 0.414911566198916,
        "abs_return_acf_5": 0.29513489730974124,
        "abs_return_acf_20": 0.2628531775487785,
        "quantile_01": -0.04774142138657134,
        "quantile_99": 0.04895913904772928,
        "hill_tail_index": 2.5631178760259563
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016949002928166087,
        "excess_kurtosis": 5.674054291062969,
        "return_acf_1": -0.11316372008458879,
        "abs_return_acf_1": 0.34793506104947114,
        "abs_return_acf_5": 0.23458668678693614,
        "abs_return_acf_20": 0.2895447072539346,
        "quantile_01": -0.0460567382751915,
        "quantile_99": 0.049611910810155195,
        "hill_tail_index": 2.453821093568067
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016607316521169185,
        "excess_kurtosis": 3.834014382008612,
        "return_acf_1": -0.050945119221987814,
        "abs_return_acf_1": 0.25448565782798477,
        "abs_return_acf_5": 0.23639429348220567,
        "abs_return_acf_20": 0.21085165868183803,
        "quantile_01": -0.047941720624865534,
        "quantile_99": 0.045705499052699584,
        "hill_tail_index": 3.934368789527359
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020877132312124944,
        "excess_kurtosis": 8.092715158513602,
        "return_acf_1": -0.027005487930182783,
        "abs_return_acf_1": 0.35242991287373765,
        "abs_return_acf_5": 0.36096513780077993,
        "abs_return_acf_20": 0.31483332437793293,
        "quantile_01": -0.07478521297064779,
        "quantile_99": 0.06273613909219902,
        "hill_tail_index": 3.5200633088503275
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017017041072856492,
        "excess_kurtosis": 11.47350710495711,
        "return_acf_1": -0.008141100033253556,
        "abs_return_acf_1": 0.4352321164679588,
        "abs_return_acf_5": 0.3244494055783473,
        "abs_return_acf_20": 0.2592415541384283,
        "quantile_01": -0.05636143003148969,
        "quantile_99": 0.04033402225665728,
        "hill_tail_index": 1.8052446199855685
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017058416535770154,
        "excess_kurtosis": 5.812299596689261,
        "return_acf_1": -0.09630487163266385,
        "abs_return_acf_1": 0.36565285661852315,
        "abs_return_acf_5": 0.2507000388996457,
        "abs_return_acf_20": 0.2975890640965177,
        "quantile_01": -0.051654170491081224,
        "quantile_99": 0.049285867622202766,
        "hill_tail_index": 2.4125479530388083
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017883165288584635,
        "excess_kurtosis": 6.654988858455333,
        "return_acf_1": -0.03941716274624881,
        "abs_return_acf_1": 0.27553134737121476,
        "abs_return_acf_5": 0.29981002005870566,
        "abs_return_acf_20": 0.2939769212444039,
        "quantile_01": -0.0535388709450964,
        "quantile_99": 0.04952619042083885,
        "hill_tail_index": 2.865895164264035
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019277093740628214,
        "excess_kurtosis": 7.32480370121961,
        "return_acf_1": -0.05160290781095639,
        "abs_return_acf_1": 0.33739016756930856,
        "abs_return_acf_5": 0.34337748967170434,
        "abs_return_acf_20": 0.25694350491872464,
        "quantile_01": -0.06174458018142117,
        "quantile_99": 0.04596357939597008,
        "hill_tail_index": 3.2314895098433896
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02045648776708806,
        "excess_kurtosis": 7.487657377666215,
        "return_acf_1": -0.15978783083524428,
        "abs_return_acf_1": 0.4250192151028561,
        "abs_return_acf_5": 0.41939255127967584,
        "abs_return_acf_20": 0.3278933967511326,
        "quantile_01": -0.06732626784133042,
        "quantile_99": 0.05436131042351254,
        "hill_tail_index": 2.792867031730033
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01652819678068289,
        "excess_kurtosis": 3.7520565173765217,
        "return_acf_1": -0.10727031190715824,
        "abs_return_acf_1": 0.21285604449102122,
        "abs_return_acf_5": 0.24648699308888886,
        "abs_return_acf_20": 0.19692757482513437,
        "quantile_01": -0.04586129501448647,
        "quantile_99": 0.04343379479064698,
        "hill_tail_index": 2.9438681170075247
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01781624530282294,
        "excess_kurtosis": 11.148382675242598,
        "return_acf_1": -0.029035874814468295,
        "abs_return_acf_1": 0.29200484000243687,
        "abs_return_acf_5": 0.2792889667973238,
        "abs_return_acf_20": 0.26962410064813425,
        "quantile_01": -0.057145965087625296,
        "quantile_99": 0.038760177677845425,
        "hill_tail_index": 2.256348479860259
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
