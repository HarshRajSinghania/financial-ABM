# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27302
Run ID: `ba72c33daae0e9e7d2a11be0258575b29859bb1743f49b2a671d2f9cd5a89537`
Result fingerprint: `5e525e92b2033da355c92266faf75fcdf03e40fb22574784660e827380c06eb1`

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
    "equal_weight_sd": -0.833464285714283,
    "equal_weight_raw": -12.501964285714244,
    "fixed_start_cap_weight_sd": -0.7907748835898304,
    "fixed_start_cap_weight_raw": -11.86162325384746,
    "end_cap_weight_sd": -0.7909341953036958,
    "end_cap_weight_raw": -11.86401292955544
  },
  "full_period_change": {
    "equal_weight_sd": -1.2873214285714245,
    "equal_weight_raw": -19.309821428571368
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.205163359788356,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11891666666666938,
    "equal_weight_raw": 1.7837500000000406,
    "fixed_start_cap_weight_sd": 0.16160606879112205,
    "fixed_start_cap_weight_raw": 2.4240910318668303,
    "end_cap_weight_sd": 0.1614467570772567,
    "end_cap_weight_raw": 2.42170135615885
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7023809523809493,
      "change_raw": -10.53571428571424,
      "decay_adjusted_gain_sd": 0.2500000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.813214285714283,
      "change_raw": -12.198214285714245,
      "decay_adjusted_gain_sd": 0.13916666666666944
    },
    "small": {
      "count": 18,
      "change_sd": -0.8654365079365053,
      "change_raw": -12.981547619047578,
      "decay_adjusted_gain_sd": 0.08694444444444707
    },
    "large_minus_small_sd": 0.16305555555555595,
    "large_minus_small_raw": 2.445833333333339
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.18096214974104394,
    "final_wealth_share": 0.163021882847075
  },
  "pricing_slope": {
    "mean": 0.0011493365237296867,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.0002466618810215475,
    "real_improvement_cost": 0.0002466618810215475,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0002466618810215475,
    "resource_cost_fraction_initial_cap": 8.22206270071825e-06,
    "private_net_outflow_fraction_initial_cap": 8.22206270071825e-06,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 4.364593623654555e-06,
    "unapplied_final_day_resource_cost": 1.8393447204820326e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 14463.118440617247,
    "beneficial_raw_gain_per_resource_cost": 216946.7766092587,
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
    "accrued_cost": 3.0446800603249033,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.06848958413442637,
    "accrued_cost_fraction_initial_cap": 0.10148933534416343,
    "mean_contract_rate": 0.04205528038641147,
    "maximum_ledger_error": 6.437450399132683e-20
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
    "maximum_relative_cash_error": 2.409108235766631e-15,
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
      "minimum": -0.2881186133622397,
      "maximum": -0.06905942050853875,
      "mean": -0.1543964192266977,
      "median": -0.1534272632822622,
      "quantile_05": -0.21769070110177377,
      "quantile_95": -0.09740985459518524
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
      "minimum": 0.26787639941995695,
      "maximum": 0.8039161845439387,
      "mean": 0.6085089075911414,
      "median": 0.6311287830239559,
      "quantile_05": 0.412942686783858,
      "quantile_95": 0.7340119363239911
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
        "daily_volatility": 0.018333278210500438,
        "excess_kurtosis": 5.8855650588688775,
        "return_acf_1": -0.16956809952880406,
        "abs_return_acf_1": 0.2895341458459637,
        "abs_return_acf_5": 0.25765207133026197,
        "abs_return_acf_20": 0.2987043193529311,
        "quantile_01": -0.05278528557754144,
        "quantile_99": 0.049020722928380424,
        "hill_tail_index": 3.025108304437002
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01911439136571691,
        "excess_kurtosis": 7.9704832555064264,
        "return_acf_1": -0.18999273850706086,
        "abs_return_acf_1": 0.41658166399895613,
        "abs_return_acf_5": 0.4291980677546705,
        "abs_return_acf_20": 0.32515652157420144,
        "quantile_01": -0.062177040623727045,
        "quantile_99": 0.05035219390617243,
        "hill_tail_index": 2.835966827561885
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01584333445098833,
        "excess_kurtosis": 2.6983374372933557,
        "return_acf_1": -0.1647724763321602,
        "abs_return_acf_1": 0.1929788875422792,
        "abs_return_acf_5": 0.1937052769083787,
        "abs_return_acf_20": 0.18873919874891693,
        "quantile_01": -0.041624810596759924,
        "quantile_99": 0.0385927650160744,
        "hill_tail_index": 3.7314556703713286
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01637156692576722,
        "excess_kurtosis": 3.6841874107240047,
        "return_acf_1": -0.10512066703085786,
        "abs_return_acf_1": 0.1864715953902821,
        "abs_return_acf_5": 0.22972280740831474,
        "abs_return_acf_20": 0.2016606443780667,
        "quantile_01": -0.04385680776154739,
        "quantile_99": 0.04054094709497285,
        "hill_tail_index": 3.3320514339219884
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017327437601320293,
        "excess_kurtosis": 5.331117074186865,
        "return_acf_1": -0.09527206718742456,
        "abs_return_acf_1": 0.3407636292497242,
        "abs_return_acf_5": 0.3199229274833454,
        "abs_return_acf_20": 0.275851227595251,
        "quantile_01": -0.055889797452944534,
        "quantile_99": 0.05160092740764079,
        "hill_tail_index": 3.48479839791412
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017865307732854364,
        "excess_kurtosis": 7.572307500124412,
        "return_acf_1": -0.18674143099389254,
        "abs_return_acf_1": 0.3410276789558752,
        "abs_return_acf_5": 0.3437405150102435,
        "abs_return_acf_20": 0.260136952743233,
        "quantile_01": -0.057619881306336176,
        "quantile_99": 0.051652339583564605,
        "hill_tail_index": 3.8840450029971
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019175146646946344,
        "excess_kurtosis": 11.23255815439117,
        "return_acf_1": -0.11973418430089149,
        "abs_return_acf_1": 0.41439093639365543,
        "abs_return_acf_5": 0.4745132869417358,
        "abs_return_acf_20": 0.36180557685228665,
        "quantile_01": -0.06722397574286525,
        "quantile_99": 0.054543706909606034,
        "hill_tail_index": 2.5255634751817606
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018892157316490268,
        "excess_kurtosis": 5.253617632974374,
        "return_acf_1": -0.16122758779257593,
        "abs_return_acf_1": 0.29635491269003283,
        "abs_return_acf_5": 0.33568200874835885,
        "abs_return_acf_20": 0.2817696768566615,
        "quantile_01": -0.060580837723565914,
        "quantile_99": 0.059879708872605956,
        "hill_tail_index": 4.058517069534095
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01856686028704423,
        "excess_kurtosis": 6.199925038180696,
        "return_acf_1": -0.18075333703236388,
        "abs_return_acf_1": 0.29460212693589927,
        "abs_return_acf_5": 0.3196112183890171,
        "abs_return_acf_20": 0.25355388860368044,
        "quantile_01": -0.06090735704897315,
        "quantile_99": 0.05320394838390061,
        "hill_tail_index": 3.258562345092569
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018360333826193884,
        "excess_kurtosis": 7.7284262348940445,
        "return_acf_1": -0.2035537110454737,
        "abs_return_acf_1": 0.41959008715140245,
        "abs_return_acf_5": 0.3597484629929225,
        "abs_return_acf_20": 0.2600099297995441,
        "quantile_01": -0.05675775178736817,
        "quantile_99": 0.052529239884218246,
        "hill_tail_index": 2.8118591776391026
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017610093526171506,
        "excess_kurtosis": 6.167926143818908,
        "return_acf_1": -0.10002270587133713,
        "abs_return_acf_1": 0.23843824677665912,
        "abs_return_acf_5": 0.2635783977933453,
        "abs_return_acf_20": 0.16752057095650524,
        "quantile_01": -0.052761178503214365,
        "quantile_99": 0.04766861010215398,
        "hill_tail_index": 3.3122489776416257
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018007442090503544,
        "excess_kurtosis": 11.428689660565063,
        "return_acf_1": -0.12037638815507073,
        "abs_return_acf_1": 0.37430883130318937,
        "abs_return_acf_5": 0.36012411950930534,
        "abs_return_acf_20": 0.23790299656493313,
        "quantile_01": -0.05963973561328174,
        "quantile_99": 0.04651535299602633,
        "hill_tail_index": 2.3429408825598026
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020114471417426397,
        "excess_kurtosis": 14.7185464966954,
        "return_acf_1": -0.21206269977474448,
        "abs_return_acf_1": 0.43029929022270386,
        "abs_return_acf_5": 0.4039866186156405,
        "abs_return_acf_20": 0.27868347484538597,
        "quantile_01": -0.0688359276115633,
        "quantile_99": 0.05626319553015304,
        "hill_tail_index": 2.169024699429962
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017217545714791508,
        "excess_kurtosis": 3.073729002094195,
        "return_acf_1": -0.1814080716866532,
        "abs_return_acf_1": 0.2866631674624492,
        "abs_return_acf_5": 0.24750613246971173,
        "abs_return_acf_20": 0.2131850977719864,
        "quantile_01": -0.049722889209889515,
        "quantile_99": 0.044133172324112784,
        "hill_tail_index": 3.392998711730608
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015909853412149098,
        "excess_kurtosis": 3.5631331476415564,
        "return_acf_1": -0.11864771873307388,
        "abs_return_acf_1": 0.27525212307948255,
        "abs_return_acf_5": 0.26452111182064775,
        "abs_return_acf_20": 0.2791235962197228,
        "quantile_01": -0.04854318168034978,
        "quantile_99": 0.039583817602843824,
        "hill_tail_index": 3.006151436395054
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01847638198260261,
        "excess_kurtosis": 11.009336500225357,
        "return_acf_1": -0.06905942050853875,
        "abs_return_acf_1": 0.3872278881295987,
        "abs_return_acf_5": 0.35462721499436234,
        "abs_return_acf_20": 0.2356032661968828,
        "quantile_01": -0.056413115140697696,
        "quantile_99": 0.04583262915641383,
        "hill_tail_index": 2.377950743067877
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018614236867400526,
        "excess_kurtosis": 12.671691264732042,
        "return_acf_1": -0.12147965270745577,
        "abs_return_acf_1": 0.3452212569825829,
        "abs_return_acf_5": 0.4185252581314177,
        "abs_return_acf_20": 0.2920260692017854,
        "quantile_01": -0.05866887140905178,
        "quantile_99": 0.04658448187783516,
        "hill_tail_index": 1.998132245611161
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018519912016590347,
        "excess_kurtosis": 4.979638145772991,
        "return_acf_1": -0.15900361127789903,
        "abs_return_acf_1": 0.26438603393425214,
        "abs_return_acf_5": 0.2834891642077868,
        "abs_return_acf_20": 0.2463954118639116,
        "quantile_01": -0.05725452805280838,
        "quantile_99": 0.05394145339278934,
        "hill_tail_index": 4.353263247487716
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017686354575800423,
        "excess_kurtosis": 3.54991610516561,
        "return_acf_1": -0.1826909462054179,
        "abs_return_acf_1": 0.31079869465993554,
        "abs_return_acf_5": 0.22870188635964347,
        "abs_return_acf_20": 0.1888925215180639,
        "quantile_01": -0.052713224187955286,
        "quantile_99": 0.04502000740360794,
        "hill_tail_index": 3.3834996734052325
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018194550583606764,
        "excess_kurtosis": 6.5686104617739645,
        "return_acf_1": -0.14569207826355438,
        "abs_return_acf_1": 0.3708308834094515,
        "abs_return_acf_5": 0.3560802634016873,
        "abs_return_acf_20": 0.22347427909331197,
        "quantile_01": -0.05711386361665993,
        "quantile_99": 0.04333489521090895,
        "hill_tail_index": 3.1147398465067155
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01816013787775819,
        "excess_kurtosis": 4.923283431608091,
        "return_acf_1": -0.1443467734432511,
        "abs_return_acf_1": 0.38281840950807394,
        "abs_return_acf_5": 0.319587820123873,
        "abs_return_acf_20": 0.2564450226511837,
        "quantile_01": -0.05767968462671252,
        "quantile_99": 0.047167473865155,
        "hill_tail_index": 3.5171717743942437
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017703237646476504,
        "excess_kurtosis": 4.003222902439193,
        "return_acf_1": -0.14014295844115918,
        "abs_return_acf_1": 0.2651535818772824,
        "abs_return_acf_5": 0.26637678461838193,
        "abs_return_acf_20": 0.20636095520022416,
        "quantile_01": -0.050636749845733985,
        "quantile_99": 0.04744512648453027,
        "hill_tail_index": 4.444982431405276
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018393675463678122,
        "excess_kurtosis": 13.176215291033387,
        "return_acf_1": -0.168422987561181,
        "abs_return_acf_1": 0.3418056788631637,
        "abs_return_acf_5": 0.34253151614375854,
        "abs_return_acf_20": 0.23762533272264644,
        "quantile_01": -0.06352389250938836,
        "quantile_99": 0.04672732012503061,
        "hill_tail_index": 2.4958454062986806
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01685867869702128,
        "excess_kurtosis": 3.4431787381979397,
        "return_acf_1": -0.14785091528662536,
        "abs_return_acf_1": 0.2397538089161291,
        "abs_return_acf_5": 0.2201522245344773,
        "abs_return_acf_20": 0.15121454680411464,
        "quantile_01": -0.051385501902997885,
        "quantile_99": 0.041615844645647534,
        "hill_tail_index": 4.549989646632179
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017974583585511322,
        "excess_kurtosis": 5.245178277574734,
        "return_acf_1": -0.10919092406456017,
        "abs_return_acf_1": 0.34102589738661093,
        "abs_return_acf_5": 0.36189004223266824,
        "abs_return_acf_20": 0.24360594184591106,
        "quantile_01": -0.059635415810435896,
        "quantile_99": 0.04924594929873292,
        "hill_tail_index": 4.161088510721142
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017442090261550455,
        "excess_kurtosis": 6.0018181928313545,
        "return_acf_1": -0.10728830828044562,
        "abs_return_acf_1": 0.31609495509405,
        "abs_return_acf_5": 0.3174012564977868,
        "abs_return_acf_20": 0.27030299217037773,
        "quantile_01": -0.04955797851232968,
        "quantile_99": 0.05081280792609502,
        "hill_tail_index": 4.13686125281457
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019633785505200455,
        "excess_kurtosis": 10.398156987640014,
        "return_acf_1": -0.2222954294602523,
        "abs_return_acf_1": 0.4551224439828858,
        "abs_return_acf_5": 0.42719921111751236,
        "abs_return_acf_20": 0.32156068207821703,
        "quantile_01": -0.06127553841408901,
        "quantile_99": 0.05927698829068655,
        "hill_tail_index": 2.5588522406486627
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01789693438067531,
        "excess_kurtosis": 5.439741846606145,
        "return_acf_1": -0.1860728132964062,
        "abs_return_acf_1": 0.2855913341792721,
        "abs_return_acf_5": 0.27376259861466556,
        "abs_return_acf_20": 0.19878663830806476,
        "quantile_01": -0.05390059700974831,
        "quantile_99": 0.05017667400707736,
        "hill_tail_index": 3.133303095304235
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019509276030678844,
        "excess_kurtosis": 13.163641092277562,
        "return_acf_1": -0.2881186133622397,
        "abs_return_acf_1": 0.43983377962181425,
        "abs_return_acf_5": 0.3718865423615151,
        "abs_return_acf_20": 0.296071348913315,
        "quantile_01": -0.06738781198290142,
        "quantile_99": 0.05813021238037862,
        "hill_tail_index": 2.2445618746600746
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017033771744438476,
        "excess_kurtosis": 5.63866793924954,
        "return_acf_1": -0.13098326066955893,
        "abs_return_acf_1": 0.28630835481720796,
        "abs_return_acf_5": 0.301229816463654,
        "abs_return_acf_20": 0.17062195454091025,
        "quantile_01": -0.05544155451697211,
        "quantile_99": 0.03951480148910829,
        "hill_tail_index": 2.7696908573754793
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

Firm policy: npv_discrete
Training: False
Coverage status: not_applicable
Unseen state share: None
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
