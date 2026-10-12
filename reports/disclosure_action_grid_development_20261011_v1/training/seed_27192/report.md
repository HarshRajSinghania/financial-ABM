# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27192
Run ID: `2b3cbe682da4740988525d22c97248350868be0b4b936c7daa86124641cdc72a`
Result fingerprint: `d2bbd3998e305b3d5013aaa4d0927da0b5200b8438b60e1c0ec4285654175e64`

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
    "equal_weight_sd": -0.7447142857142826,
    "equal_weight_raw": -11.17071428571424,
    "fixed_start_cap_weight_sd": -0.7117438065632412,
    "fixed_start_cap_weight_raw": -10.676157098448618,
    "end_cap_weight_sd": -0.7107602404864907,
    "end_cap_weight_raw": -10.66140360729736
  },
  "full_period_change": {
    "equal_weight_sd": -1.1397380952380907,
    "equal_weight_raw": -17.09607142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0741425264550222,
    "inflation_mean_sd": 0.605123015873016
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2076666666666698,
    "equal_weight_raw": 3.115000000000046,
    "fixed_start_cap_weight_sd": 0.240637145817711,
    "fixed_start_cap_weight_raw": 3.6095571872656658,
    "end_cap_weight_sd": 0.24162071189446174,
    "end_cap_weight_raw": 3.6243106784169252
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6307142857142828,
      "change_raw": -9.460714285714241,
      "decay_adjusted_gain_sd": 0.3216666666666696
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7743253968253936,
      "change_raw": -11.614880952380904,
      "decay_adjusted_gain_sd": 0.17805555555555871
    },
    "small": {
      "count": 18,
      "change_sd": -0.748908730158727,
      "change_raw": -11.233630952380906,
      "decay_adjusted_gain_sd": 0.2034722222222253
    },
    "large_minus_small_sd": 0.11819444444444427,
    "large_minus_small_raw": 1.772916666666664
  },
  "inflation": {
    "initial_mean_sd": 0.27566666666666667,
    "final_mean_sd": 0.6225833333333333,
    "mean_sd": 0.47106931723563705,
    "mean_absolute_raw_gap": 7.066039758534555,
    "final_absolute_raw_gap": 9.338750000000001,
    "mean_range_fraction": 0.07066039758534555
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.5,
    "initial_wealth_share": 0.3020134977962841,
    "final_wealth_share": 0.5855623079550045
  },
  "pricing_slope": {
    "mean": -0.0051534179322064435,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.04343275597639067,
    "real_improvement_cost": 0.030609356346254005,
    "washing_cost": 0.01282339963013666,
    "fine_transfer": 0.013827919959636953,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05726067593602763,
    "resource_cost_fraction_initial_cap": 0.0014477585325463557,
    "private_net_outflow_fraction_initial_cap": 0.0019086891978675876,
    "fine_transfer_fraction_initial_cap": 0.0004609306653212318,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0015748209828100666,
    "unapplied_final_day_resource_cost": 0.0019158857960050646
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 143.4401262352916,
    "beneficial_raw_gain_per_resource_cost": 2151.601893529374,
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
    "accrued_cost": 3.1574705399297507,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.18128006373927413,
    "accrued_cost_fraction_initial_cap": 0.10524901799765836,
    "mean_contract_rate": 0.04489497543322951,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "price_cap_hits": 36,
    "maximum_relative_cash_error": 1.1765852530268231e-15,
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
      "minimum": -0.24827203242798598,
      "maximum": -0.08883600613391045,
      "mean": -0.14961581427267648,
      "median": -0.15595614722190376,
      "quantile_05": -0.18333312265443028,
      "quantile_95": -0.09589180806904173
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
      "minimum": 0.4661457450974027,
      "maximum": 0.8996671585779012,
      "mean": 0.7877301837243244,
      "median": 0.8092250464382494,
      "quantile_05": 0.59323032420837,
      "quantile_95": 0.8848401629768048
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
        "daily_volatility": 0.031282252596042254,
        "excess_kurtosis": 18.612300951750736,
        "return_acf_1": -0.17803800938400066,
        "abs_return_acf_1": 0.5464064080509661,
        "abs_return_acf_5": 0.370682275447004,
        "abs_return_acf_20": 0.40447366001749,
        "quantile_01": -0.12359163642766995,
        "quantile_99": 0.1034734038248914,
        "hill_tail_index": 3.0122559439949903
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.03227835785199716,
        "excess_kurtosis": 20.296416488078766,
        "return_acf_1": -0.18130671230144593,
        "abs_return_acf_1": 0.49831514155979173,
        "abs_return_acf_5": 0.4111749229391603,
        "abs_return_acf_20": 0.41114949062308254,
        "quantile_01": -0.12528588527844797,
        "quantile_99": 0.09938946976056039,
        "hill_tail_index": 2.4558927804736563
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.03334093962211862,
        "excess_kurtosis": 20.42146500562288,
        "return_acf_1": -0.10419303971505403,
        "abs_return_acf_1": 0.5128019195375128,
        "abs_return_acf_5": 0.42220478978634596,
        "abs_return_acf_20": 0.42767641107766147,
        "quantile_01": -0.12003263922564306,
        "quantile_99": 0.09548384644146271,
        "hill_tail_index": 2.2774088587246903
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0317411263137948,
        "excess_kurtosis": 20.333260647048693,
        "return_acf_1": -0.15520783653875667,
        "abs_return_acf_1": 0.5506859094696244,
        "abs_return_acf_5": 0.43793420194762983,
        "abs_return_acf_20": 0.4187185349039741,
        "quantile_01": -0.1149241341879245,
        "quantile_99": 0.08771414742480994,
        "hill_tail_index": 2.315836523166408
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.03069720203043218,
        "excess_kurtosis": 21.101178009488716,
        "return_acf_1": -0.24827203242798598,
        "abs_return_acf_1": 0.5323452214707335,
        "abs_return_acf_5": 0.3562922066425346,
        "abs_return_acf_20": 0.453161418940813,
        "quantile_01": -0.10229715371930473,
        "quantile_99": 0.10770943509716831,
        "hill_tail_index": 3.0977603636212443
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.032664768807211635,
        "excess_kurtosis": 19.680650990340453,
        "return_acf_1": -0.1311287984945669,
        "abs_return_acf_1": 0.4855178927510772,
        "abs_return_acf_5": 0.41591672320685485,
        "abs_return_acf_20": 0.42277692446515674,
        "quantile_01": -0.128044462673875,
        "quantile_99": 0.09891202112565121,
        "hill_tail_index": 2.516863194417856
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.030189577455173904,
        "excess_kurtosis": 19.48598635340995,
        "return_acf_1": -0.150635284024074,
        "abs_return_acf_1": 0.5020557163858722,
        "abs_return_acf_5": 0.42526580049505863,
        "abs_return_acf_20": 0.3874124566774577,
        "quantile_01": -0.12190701588588025,
        "quantile_99": 0.09342377594451864,
        "hill_tail_index": 3.3411199429572913
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.031926859436008766,
        "excess_kurtosis": 14.67760889964114,
        "return_acf_1": -0.18499109476141745,
        "abs_return_acf_1": 0.48409463211382825,
        "abs_return_acf_5": 0.3478239571600159,
        "abs_return_acf_20": 0.45035183012771124,
        "quantile_01": -0.11997963860976506,
        "quantile_99": 0.10446732904447216,
        "hill_tail_index": 3.3479988083267935
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.030233590122570164,
        "excess_kurtosis": 15.92748263284696,
        "return_acf_1": -0.08909989126775884,
        "abs_return_acf_1": 0.44676632826226126,
        "abs_return_acf_5": 0.37630460128387294,
        "abs_return_acf_20": 0.41032304335058056,
        "quantile_01": -0.10184793765162085,
        "quantile_99": 0.08448904068620179,
        "hill_tail_index": 2.52623681222687
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.03060320668803473,
        "excess_kurtosis": 17.758829345342214,
        "return_acf_1": -0.13629181964599343,
        "abs_return_acf_1": 0.4762442959893292,
        "abs_return_acf_5": 0.3688002951916511,
        "abs_return_acf_20": 0.42322010221315387,
        "quantile_01": -0.11607293737016293,
        "quantile_99": 0.09082847839575543,
        "hill_tail_index": 2.436319604126428
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.03085410966337771,
        "excess_kurtosis": 22.157927470460486,
        "return_acf_1": -0.15785113869175887,
        "abs_return_acf_1": 0.461361748970549,
        "abs_return_acf_5": 0.35790294208649676,
        "abs_return_acf_20": 0.37065044966323324,
        "quantile_01": -0.11358254342335403,
        "quantile_99": 0.07422013091836283,
        "hill_tail_index": 2.30435239394348
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.03180567687107927,
        "excess_kurtosis": 16.764902907497408,
        "return_acf_1": -0.16496564868239186,
        "abs_return_acf_1": 0.49345410164343206,
        "abs_return_acf_5": 0.41930433328772704,
        "abs_return_acf_20": 0.4141895877800521,
        "quantile_01": -0.1250428750093722,
        "quantile_99": 0.0943942467286192,
        "hill_tail_index": 2.497945635728555
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.03457417918330359,
        "excess_kurtosis": 20.873528987756593,
        "return_acf_1": -0.08883600613391045,
        "abs_return_acf_1": 0.48622203731447733,
        "abs_return_acf_5": 0.42184076145878574,
        "abs_return_acf_20": 0.38607571542174385,
        "quantile_01": -0.13931754646250027,
        "quantile_99": 0.10119532188406402,
        "hill_tail_index": 2.5349673896943385
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.029742853069950878,
        "excess_kurtosis": 21.191692391104375,
        "return_acf_1": -0.13326123334837447,
        "abs_return_acf_1": 0.48988608818380425,
        "abs_return_acf_5": 0.3854465401163269,
        "abs_return_acf_20": 0.4260241525231002,
        "quantile_01": -0.10291516584439013,
        "quantile_99": 0.08753364136449691,
        "hill_tail_index": 2.0897853524265524
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.027522258252172457,
        "excess_kurtosis": 15.624770176907266,
        "return_acf_1": -0.1404860987749243,
        "abs_return_acf_1": 0.44394842824451347,
        "abs_return_acf_5": 0.3139499193268614,
        "abs_return_acf_20": 0.40704063535296475,
        "quantile_01": -0.09255866933049936,
        "quantile_99": 0.08497960585638605,
        "hill_tail_index": 2.619785228254579
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.027785376018937644,
        "excess_kurtosis": 19.085784201369595,
        "return_acf_1": -0.12335285493931591,
        "abs_return_acf_1": 0.5112094870438015,
        "abs_return_acf_5": 0.3842670515033875,
        "abs_return_acf_20": 0.40751771559206645,
        "quantile_01": -0.11183015202271196,
        "quantile_99": 0.08881408981107425,
        "hill_tail_index": 2.7962375441151854
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.03142320074969347,
        "excess_kurtosis": 20.027652101766886,
        "return_acf_1": -0.1710436381271682,
        "abs_return_acf_1": 0.5091334302938987,
        "abs_return_acf_5": 0.4185770220109411,
        "abs_return_acf_20": 0.3902257133497203,
        "quantile_01": -0.12320037617646709,
        "quantile_99": 0.0714446481620193,
        "hill_tail_index": 2.284427870018895
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.03352103970730959,
        "excess_kurtosis": 24.109630973078445,
        "return_acf_1": -0.16453810924055165,
        "abs_return_acf_1": 0.5168266440523438,
        "abs_return_acf_5": 0.4507051222945305,
        "abs_return_acf_20": 0.4305496537426442,
        "quantile_01": -0.11222117232367823,
        "quantile_99": 0.09966028677084121,
        "hill_tail_index": 2.4711174571075483
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.03264349887537603,
        "excess_kurtosis": 19.878178776621667,
        "return_acf_1": -0.1567044579050509,
        "abs_return_acf_1": 0.5308145694497258,
        "abs_return_acf_5": 0.43717310897577083,
        "abs_return_acf_20": 0.3984783305183694,
        "quantile_01": -0.13707985368244066,
        "quantile_99": 0.08488326447496246,
        "hill_tail_index": 2.3533551926287806
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.03353990456906206,
        "excess_kurtosis": 21.68399725673556,
        "return_acf_1": -0.1775423501328591,
        "abs_return_acf_1": 0.555485908923315,
        "abs_return_acf_5": 0.5019986879176307,
        "abs_return_acf_20": 0.4184984190922514,
        "quantile_01": -0.13215389254966273,
        "quantile_99": 0.09105394343540564,
        "hill_tail_index": 2.0286577103292616
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.03137324362165536,
        "excess_kurtosis": 14.88643405402594,
        "return_acf_1": -0.12975819183722673,
        "abs_return_acf_1": 0.5349908716700797,
        "abs_return_acf_5": 0.38575513083255136,
        "abs_return_acf_20": 0.4227678587587785,
        "quantile_01": -0.1083454093439427,
        "quantile_99": 0.0981214973598186,
        "hill_tail_index": 2.851295410621229
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02925397599242286,
        "excess_kurtosis": 21.207222248082495,
        "return_acf_1": -0.16060128285250488,
        "abs_return_acf_1": 0.4085983903256368,
        "abs_return_acf_5": 0.35876372883607915,
        "abs_return_acf_20": 0.32821583994240827,
        "quantile_01": -0.09917234135917742,
        "quantile_99": 0.08253059313433346,
        "hill_tail_index": 2.3170197683479987
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.0323957178943211,
        "excess_kurtosis": 21.18467237770264,
        "return_acf_1": -0.16475863230631785,
        "abs_return_acf_1": 0.551442534860175,
        "abs_return_acf_5": 0.48665295007054143,
        "abs_return_acf_20": 0.3833034845438145,
        "quantile_01": -0.13514412622189229,
        "quantile_99": 0.08565434423923629,
        "hill_tail_index": 2.733971871117993
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.03147387811131256,
        "excess_kurtosis": 20.131948844346937,
        "return_acf_1": -0.1388575550151672,
        "abs_return_acf_1": 0.47506114637740743,
        "abs_return_acf_5": 0.43886367164327367,
        "abs_return_acf_20": 0.41321892642652325,
        "quantile_01": -0.10411503329238785,
        "quantile_99": 0.09153459295459794,
        "hill_tail_index": 2.474062444326065
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.029470762710559612,
        "excess_kurtosis": 19.074592027537197,
        "return_acf_1": -0.11884867741359911,
        "abs_return_acf_1": 0.5629876100171313,
        "abs_return_acf_5": 0.44408869637701004,
        "abs_return_acf_20": 0.3994001872798858,
        "quantile_01": -0.11648497385662097,
        "quantile_99": 0.0944110303643625,
        "hill_tail_index": 3.217383771746099
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.032497087988319094,
        "excess_kurtosis": 28.60447117790777,
        "return_acf_1": -0.16752072805855467,
        "abs_return_acf_1": 0.46941203236249696,
        "abs_return_acf_5": 0.44091595813096696,
        "abs_return_acf_20": 0.37441738613820663,
        "quantile_01": -0.12647012671201252,
        "quantile_99": 0.08867905109941471,
        "hill_tail_index": 2.0167981758388365
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.03175644952540434,
        "excess_kurtosis": 18.487987058868814,
        "return_acf_1": -0.137140618568346,
        "abs_return_acf_1": 0.4200851687453441,
        "abs_return_acf_5": 0.3536625292221627,
        "abs_return_acf_20": 0.3979396195234095,
        "quantile_01": -0.10856873529871477,
        "quantile_99": 0.09857386282014276,
        "hill_tail_index": 2.3423330755986687
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.031951808620614155,
        "excess_kurtosis": 20.59095812552326,
        "return_acf_1": -0.11073440662139883,
        "abs_return_acf_1": 0.5396210950173154,
        "abs_return_acf_5": 0.4349651740989604,
        "abs_return_acf_20": 0.42525896721342626,
        "quantile_01": -0.13485547132148806,
        "quantile_99": 0.09639661733633464,
        "hill_tail_index": 2.5163663208088516
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.034890167917530183,
        "excess_kurtosis": 26.928802250334094,
        "return_acf_1": -0.16008368865730904,
        "abs_return_acf_1": 0.45750035734382105,
        "abs_return_acf_5": 0.39666927043839717,
        "abs_return_acf_20": 0.35608833324483763,
        "quantile_01": -0.12290142849545191,
        "quantile_99": 0.08586999774249691,
        "hill_tail_index": 1.8952499690376645
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02780152772368422,
        "excess_kurtosis": 23.657258893936543,
        "return_acf_1": -0.16242459231250855,
        "abs_return_acf_1": 0.5313566178177352,
        "abs_return_acf_5": 0.3456923341746754,
        "abs_return_acf_20": 0.4206891738329252,
        "quantile_01": -0.0952134430306107,
        "quantile_99": 0.08725574697182303,
        "hill_tail_index": 2.5995170838150305
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
