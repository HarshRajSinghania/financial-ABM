# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27011
Run ID: `d2a3a27652287546cdf2b0ca4a4129c29735f8b77b725d3118a5cf7b6c5aaaae`
Result fingerprint: `c0f8536556518fdb35f244b70a4c6448fce062710d223d0522f452962480d717`

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
    "equal_weight_sd": -0.5212976190476158,
    "equal_weight_raw": -7.819464285714237,
    "fixed_start_cap_weight_sd": -0.5838805546949976,
    "fixed_start_cap_weight_raw": -8.758208320424966,
    "end_cap_weight_sd": -0.6191341536261542,
    "end_cap_weight_raw": -9.287012304392311
  },
  "full_period_change": {
    "equal_weight_sd": -0.8455714285714238,
    "equal_weight_raw": -12.683571428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8122814153439109,
    "inflation_mean_sd": 0.5726630291005291
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4310833333333365,
    "equal_weight_raw": 6.4662500000000485,
    "fixed_start_cap_weight_sd": 0.3685003976859548,
    "fixed_start_cap_weight_raw": 5.527505965289322,
    "end_cap_weight_sd": 0.3332467987547984,
    "end_cap_weight_raw": 4.998701981321977
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7740476190476158,
      "change_raw": -11.610714285714236,
      "decay_adjusted_gain_sd": 0.17833333333333648
    },
    "mid": {
      "count": 9,
      "change_sd": -0.3684920634920602,
      "change_raw": -5.527380952380903,
      "decay_adjusted_gain_sd": 0.5838888888888921
    },
    "small": {
      "count": 18,
      "change_sd": -0.5555753968253936,
      "change_raw": -8.333630952380904,
      "decay_adjusted_gain_sd": 0.39680555555555874
    },
    "large_minus_small_sd": -0.21847222222222218,
    "large_minus_small_raw": -3.2770833333333327
  },
  "inflation": {
    "initial_mean_sd": 0.1755833333333333,
    "final_mean_sd": 0.5899166666666668,
    "mean_sd": 0.396069872328615,
    "mean_absolute_raw_gap": 5.941048084929227,
    "final_absolute_raw_gap": 8.84875,
    "mean_range_fraction": 0.05941048084929226
  },
  "impact": {
    "initial_share": 0.38,
    "final_share": 0.4866666666666667,
    "initial_wealth_share": 0.40931639820235405,
    "final_wealth_share": 0.48092581085142805
  },
  "pricing_slope": {
    "mean": -0.0035673663379879018,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.11515745632678287,
    "real_improvement_cost": 0.09574185839660518,
    "washing_cost": 0.019415597930177678,
    "fine_transfer": 0.0078102481299365395,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12296770445671941,
    "resource_cost_fraction_initial_cap": 0.003838581877559429,
    "private_net_outflow_fraction_initial_cap": 0.004098923481890647,
    "fine_transfer_fraction_initial_cap": 0.00026034160433121797,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004956035713869732,
    "unapplied_final_day_resource_cost": 0.014685260302951725
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 112.30275843625338,
    "beneficial_raw_gain_per_resource_cost": 1684.5413765438007,
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
    "accrued_cost": 2.8678910584042825,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.1082994177861944,
    "accrued_cost_fraction_initial_cap": 0.09559636861347608,
    "mean_contract_rate": 0.04052011615165923,
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
    "maximum_relative_cash_error": 1.531135836297367e-15,
    "maximum_absolute_share_error": 2.1094237467877974e-15,
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
      "minimum": -0.30707668126525695,
      "maximum": -0.16386559427235697,
      "mean": -0.2427827798346792,
      "median": -0.2476824485972895,
      "quantile_05": -0.2890851478773407,
      "quantile_95": -0.17953789006227336
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
      "minimum": 0.6148865827514653,
      "maximum": 0.8084519185154964,
      "mean": 0.7228211358155056,
      "median": 0.725930025770358,
      "quantile_05": 0.64515808202244,
      "quantile_95": 0.7913222420877003
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
        "daily_volatility": 0.018490829023034908,
        "excess_kurtosis": 15.746352112823434,
        "return_acf_1": -0.28847023995975435,
        "abs_return_acf_1": 0.42158867790558213,
        "abs_return_acf_5": 0.31518867290457636,
        "abs_return_acf_20": 0.2275714935076359,
        "quantile_01": -0.04511656820732836,
        "quantile_99": 0.0399165836368316,
        "hill_tail_index": 1.6624034368428238
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020330090243756465,
        "excess_kurtosis": 6.897704261831805,
        "return_acf_1": -0.18359801615282897,
        "abs_return_acf_1": 0.3768615560774772,
        "abs_return_acf_5": 0.3363852839843559,
        "abs_return_acf_20": 0.23042717430859502,
        "quantile_01": -0.06800491617954513,
        "quantile_99": 0.06140106679343162,
        "hill_tail_index": 3.690220473065081
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01840768726615781,
        "excess_kurtosis": 8.790548086633846,
        "return_acf_1": -0.27106242147124915,
        "abs_return_acf_1": 0.44177981988212717,
        "abs_return_acf_5": 0.40324696102211766,
        "abs_return_acf_20": 0.3203671054381448,
        "quantile_01": -0.06279985968126298,
        "quantile_99": 0.05725948283489566,
        "hill_tail_index": 2.6505589054849654
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02151440062574238,
        "excess_kurtosis": 11.173841205922109,
        "return_acf_1": -0.23585629873656463,
        "abs_return_acf_1": 0.4835285531120381,
        "abs_return_acf_5": 0.349059788726925,
        "abs_return_acf_20": 0.3097631990261164,
        "quantile_01": -0.07113250265465774,
        "quantile_99": 0.05573634800657723,
        "hill_tail_index": 2.442556698359497
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020673137883208074,
        "excess_kurtosis": 17.038411350503374,
        "return_acf_1": -0.2483702579697919,
        "abs_return_acf_1": 0.3691654198639264,
        "abs_return_acf_5": 0.3232816411748216,
        "abs_return_acf_20": 0.2381715064272715,
        "quantile_01": -0.06079919699216985,
        "quantile_99": 0.049399514924884445,
        "hill_tail_index": 1.9331708066272602
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021091209840649352,
        "excess_kurtosis": 10.679576186142206,
        "return_acf_1": -0.26852291831196656,
        "abs_return_acf_1": 0.5591930005013133,
        "abs_return_acf_5": 0.476164325539271,
        "abs_return_acf_20": 0.3385936222234762,
        "quantile_01": -0.07635997254298817,
        "quantile_99": 0.06798040563611808,
        "hill_tail_index": 2.604961584080071
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019680022276841323,
        "excess_kurtosis": 17.98165397167796,
        "return_acf_1": -0.24378625632112624,
        "abs_return_acf_1": 0.3890651338804727,
        "abs_return_acf_5": 0.34496781819210737,
        "abs_return_acf_20": 0.26426988833661047,
        "quantile_01": -0.060188857320589366,
        "quantile_99": 0.04290162221897733,
        "hill_tail_index": 1.7691788875064525
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019487515910576222,
        "excess_kurtosis": 18.651652360539646,
        "return_acf_1": -0.28958825435536584,
        "abs_return_acf_1": 0.44169017966923135,
        "abs_return_acf_5": 0.4405834941022529,
        "abs_return_acf_20": 0.3057796806493308,
        "quantile_01": -0.05794534022085005,
        "quantile_99": 0.04471835895864441,
        "hill_tail_index": 2.291006740228804
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019684611472020604,
        "excess_kurtosis": 10.073058160923402,
        "return_acf_1": -0.2424665004965391,
        "abs_return_acf_1": 0.455425284981168,
        "abs_return_acf_5": 0.31840449944927907,
        "abs_return_acf_20": 0.2939956478712214,
        "quantile_01": -0.057963637248679464,
        "quantile_99": 0.056689480033514636,
        "hill_tail_index": 2.9866265068866924
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02126750016899099,
        "excess_kurtosis": 11.265815848907101,
        "return_acf_1": -0.2593642100223147,
        "abs_return_acf_1": 0.43329861011065535,
        "abs_return_acf_5": 0.33412131373498744,
        "abs_return_acf_20": 0.33466917105530786,
        "quantile_01": -0.06526078831649064,
        "quantile_99": 0.056835446527684456,
        "hill_tail_index": 2.854356300295162
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018921380218607793,
        "excess_kurtosis": 13.569574956534929,
        "return_acf_1": -0.23589513380146435,
        "abs_return_acf_1": 0.47841234566656166,
        "abs_return_acf_5": 0.33579909169194255,
        "abs_return_acf_20": 0.296603752901428,
        "quantile_01": -0.06168085872371648,
        "quantile_99": 0.05024587836238621,
        "hill_tail_index": 2.607124511468986
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01994221125579739,
        "excess_kurtosis": 18.92051954541757,
        "return_acf_1": -0.2568432307141191,
        "abs_return_acf_1": 0.47662336926826654,
        "abs_return_acf_5": 0.4150371964235101,
        "abs_return_acf_20": 0.2742414564105747,
        "quantile_01": -0.0779408416302268,
        "quantile_99": 0.045565188484591505,
        "hill_tail_index": 1.5745311663965533
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020306667678940314,
        "excess_kurtosis": 20.14481347296413,
        "return_acf_1": -0.2523581871036536,
        "abs_return_acf_1": 0.4201594832724654,
        "abs_return_acf_5": 0.32873619022697875,
        "abs_return_acf_20": 0.2577958470320283,
        "quantile_01": -0.06326483967888959,
        "quantile_99": 0.051228537812219116,
        "hill_tail_index": 2.2142209232892727
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020971304199891957,
        "excess_kurtosis": 11.432100952518125,
        "return_acf_1": -0.20454970878335865,
        "abs_return_acf_1": 0.3937865655118532,
        "abs_return_acf_5": 0.3076178589043215,
        "abs_return_acf_20": 0.2853737181990882,
        "quantile_01": -0.07347984835033346,
        "quantile_99": 0.056171055003560656,
        "hill_tail_index": 2.603795290604743
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021469207735307225,
        "excess_kurtosis": 15.120285607170413,
        "return_acf_1": -0.22019356203961848,
        "abs_return_acf_1": 0.4590512819871797,
        "abs_return_acf_5": 0.3330702621172569,
        "abs_return_acf_20": 0.29102688879821603,
        "quantile_01": -0.05924146870676733,
        "quantile_99": 0.060557422441508926,
        "hill_tail_index": 2.351757138054391
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020686858305676296,
        "excess_kurtosis": 7.348698242552743,
        "return_acf_1": -0.2529039183365088,
        "abs_return_acf_1": 0.4768203879206324,
        "abs_return_acf_5": 0.39573807272900624,
        "abs_return_acf_20": 0.31524630544340526,
        "quantile_01": -0.06468022404812926,
        "quantile_99": 0.06642318360542888,
        "hill_tail_index": 3.8996062897148875
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021465438603922655,
        "excess_kurtosis": 12.093941833453473,
        "return_acf_1": -0.19517521325233567,
        "abs_return_acf_1": 0.3800549666792015,
        "abs_return_acf_5": 0.30534601309543535,
        "abs_return_acf_20": 0.2571055971229162,
        "quantile_01": -0.07052015319851372,
        "quantile_99": 0.06321132200458703,
        "hill_tail_index": 3.1387551476156834
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02098401444939093,
        "excess_kurtosis": 16.827992942170347,
        "return_acf_1": -0.2155513683253946,
        "abs_return_acf_1": 0.39672134881823373,
        "abs_return_acf_5": 0.31083231160871166,
        "abs_return_acf_20": 0.3270428635687272,
        "quantile_01": -0.0747379332210732,
        "quantile_99": 0.04884027412605123,
        "hill_tail_index": 1.743049744639542
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021667081505134463,
        "excess_kurtosis": 13.233061659113805,
        "return_acf_1": -0.30707668126525695,
        "abs_return_acf_1": 0.5031206917059797,
        "abs_return_acf_5": 0.40629615073511777,
        "abs_return_acf_20": 0.34720088724252385,
        "quantile_01": -0.07641372854707137,
        "quantile_99": 0.05704643772398318,
        "hill_tail_index": 2.4571021803049136
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021255775410605773,
        "excess_kurtosis": 9.681094116157293,
        "return_acf_1": -0.20152323104558476,
        "abs_return_acf_1": 0.37053853908925855,
        "abs_return_acf_5": 0.33646609808431194,
        "abs_return_acf_20": 0.27862686005889903,
        "quantile_01": -0.07461779397755328,
        "quantile_99": 0.06188042759508934,
        "hill_tail_index": 2.8471406514659163
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02127271887787982,
        "excess_kurtosis": 12.11729138685313,
        "return_acf_1": -0.26838613518849463,
        "abs_return_acf_1": 0.3925896667434198,
        "abs_return_acf_5": 0.3114411226422463,
        "abs_return_acf_20": 0.3092456758214448,
        "quantile_01": -0.07388789144827256,
        "quantile_99": 0.05984857437222692,
        "hill_tail_index": 2.320261301584757
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021052621283461567,
        "excess_kurtosis": 11.238298926270515,
        "return_acf_1": -0.23332202583240097,
        "abs_return_acf_1": 0.381773903749062,
        "abs_return_acf_5": 0.3605537647967735,
        "abs_return_acf_20": 0.2898157686469376,
        "quantile_01": -0.0694180072428109,
        "quantile_99": 0.05273618193864601,
        "hill_tail_index": 2.5957368803264282
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01960418124913589,
        "excess_kurtosis": 12.790198333530983,
        "return_acf_1": -0.16386559427235697,
        "abs_return_acf_1": 0.3564060489641824,
        "abs_return_acf_5": 0.3407526991607467,
        "abs_return_acf_20": 0.3633767898837209,
        "quantile_01": -0.0757948066460801,
        "quantile_99": 0.053378673338928186,
        "hill_tail_index": 2.1701406796456797
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0199024454954896,
        "excess_kurtosis": 7.50588825555829,
        "return_acf_1": -0.2520095657661996,
        "abs_return_acf_1": 0.3859222351091935,
        "abs_return_acf_5": 0.30017924137685414,
        "abs_return_acf_20": 0.2540903199000478,
        "quantile_01": -0.06730115499913385,
        "quantile_99": 0.06268612041572057,
        "hill_tail_index": 2.974913933327386
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01993927332949922,
        "excess_kurtosis": 16.7359099880287,
        "return_acf_1": -0.2626016716481472,
        "abs_return_acf_1": 0.4275225681419407,
        "abs_return_acf_5": 0.2720205209559976,
        "abs_return_acf_20": 0.262665367105169,
        "quantile_01": -0.05618556451252078,
        "quantile_99": 0.049099007296032844,
        "hill_tail_index": 1.986920536247185
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02084813262818857,
        "excess_kurtosis": 12.21297348733774,
        "return_acf_1": -0.1762159687154551,
        "abs_return_acf_1": 0.39081006032541027,
        "abs_return_acf_5": 0.34016153917593606,
        "abs_return_acf_20": 0.30319935653967073,
        "quantile_01": -0.0676090671682923,
        "quantile_99": 0.058837555294411197,
        "hill_tail_index": 2.522318803827977
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01913463911080242,
        "excess_kurtosis": 7.224418625173314,
        "return_acf_1": -0.27961696156150717,
        "abs_return_acf_1": 0.4052980603414265,
        "abs_return_acf_5": 0.2850653594957534,
        "abs_return_acf_20": 0.30173850548343006,
        "quantile_01": -0.06736901170272282,
        "quantile_99": 0.052336204510958016,
        "hill_tail_index": 2.9229698407050906
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02247424561545966,
        "excess_kurtosis": 13.15325913047803,
        "return_acf_1": -0.24699463922478707,
        "abs_return_acf_1": 0.46985024892558896,
        "abs_return_acf_5": 0.393768406737016,
        "abs_return_acf_20": 0.2842407534881714,
        "quantile_01": -0.07437184057732744,
        "quantile_99": 0.06355906049195881,
        "hill_tail_index": 2.562952851572758
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019358281809184818,
        "excess_kurtosis": 13.512276160641218,
        "return_acf_1": -0.28261754765605085,
        "abs_return_acf_1": 0.4582157589851575,
        "abs_return_acf_5": 0.37204362492315945,
        "abs_return_acf_20": 0.3281955352125342,
        "quantile_01": -0.06096220151219153,
        "quantile_99": 0.0394001195654048,
        "hill_tail_index": 2.0351273891800306
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02001210602684158,
        "excess_kurtosis": 15.412021210027849,
        "return_acf_1": -0.24469767671017964,
        "abs_return_acf_1": 0.47558362402113863,
        "abs_return_acf_5": 0.3581365662446209,
        "abs_return_acf_20": 0.32476254606316873,
        "quantile_01": -0.06592366938267347,
        "quantile_99": 0.044235777535714435,
        "hill_tail_index": 1.8515491457524968
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
Unseen state share: 0.0077777777777777776
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
