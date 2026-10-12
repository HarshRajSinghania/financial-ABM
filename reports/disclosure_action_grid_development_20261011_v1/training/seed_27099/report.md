# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27099
Run ID: `99a153eaa39bbb3d766bff68723e56e83b19a193bb59bb6371b85146275041ec`
Result fingerprint: `79b012c4118675b760916ca8c63dd63058f446dc7c89eec41b0bdcaf52376432`

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
    "equal_weight_sd": -0.6018809523809492,
    "equal_weight_raw": -9.028214285714236,
    "fixed_start_cap_weight_sd": -0.606412044383899,
    "fixed_start_cap_weight_raw": -9.096180665758485,
    "end_cap_weight_sd": -0.6045420489708023,
    "end_cap_weight_raw": -9.068130734562036
  },
  "full_period_change": {
    "equal_weight_sd": -0.9598214285714238,
    "equal_weight_raw": -14.397321428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.910310846560842,
    "inflation_mean_sd": 0.6328624338624339
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3505000000000031,
    "equal_weight_raw": 5.257500000000047,
    "fixed_start_cap_weight_sd": 0.3459689079970532,
    "fixed_start_cap_weight_raw": 5.1895336199558,
    "end_cap_weight_sd": 0.34783890341014984,
    "end_cap_weight_raw": 5.217583551152246
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.534880952380949,
      "change_raw": -8.023214285714236,
      "decay_adjusted_gain_sd": 0.4175000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6979365079365047,
      "change_raw": -10.469047619047572,
      "decay_adjusted_gain_sd": 0.2544444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.5650198412698381,
      "change_raw": -8.475297619047572,
      "decay_adjusted_gain_sd": 0.3873611111111142
    },
    "large_minus_small_sd": 0.03013888888888905,
    "large_minus_small_raw": 0.4520833333333357
  },
  "inflation": {
    "initial_mean_sd": 0.24975,
    "final_mean_sd": 0.6354166666666667,
    "mean_sd": 0.484636761032473,
    "mean_absolute_raw_gap": 7.269551415487094,
    "final_absolute_raw_gap": 9.531249999999998,
    "mean_range_fraction": 0.07269551415487094
  },
  "impact": {
    "initial_share": 0.19333333333333333,
    "final_share": 0.16,
    "initial_wealth_share": 0.26718181547702874,
    "final_wealth_share": 0.19233205858957766
  },
  "pricing_slope": {
    "mean": 1.2208056970225032e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.06482637350970227,
    "real_improvement_cost": 0.04989661746393419,
    "washing_cost": 0.014929756045768097,
    "fine_transfer": 0.0065258044653379085,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07135217797504018,
    "resource_cost_fraction_initial_cap": 0.0021608791169900757,
    "private_net_outflow_fraction_initial_cap": 0.0023784059325013393,
    "fine_transfer_fraction_initial_cap": 0.0002175268155112636,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0062622330019373555,
    "unapplied_final_day_resource_cost": 0.001525190534472049
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 162.20250232609973,
    "beneficial_raw_gain_per_resource_cost": 2433.037534891496,
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
    "accrued_cost": 3.2864428178043212,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.3102523416138446,
    "accrued_cost_fraction_initial_cap": 0.10954809392681071,
    "mean_contract_rate": 0.0444922332368355,
    "maximum_ledger_error": 1.2197274440461925e-19
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
    "maximum_relative_cash_error": 1.6878653896540224e-15,
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
      "minimum": -0.2081427948735053,
      "maximum": 0.02667868842508279,
      "mean": -0.11444163522531799,
      "median": -0.12814366615507805,
      "quantile_05": -0.19902793614952818,
      "quantile_95": 0.013052336512970036
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
      "minimum": 0.2963247549273626,
      "maximum": 0.7625363691142263,
      "mean": 0.5341048542414917,
      "median": 0.5340011195330004,
      "quantile_05": 0.3566066255399953,
      "quantile_95": 0.7102892448197268
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
        "daily_volatility": 0.017769771769935487,
        "excess_kurtosis": 4.373608422953845,
        "return_acf_1": -0.11338315688278928,
        "abs_return_acf_1": 0.2926935658841338,
        "abs_return_acf_5": 0.29792487356082015,
        "abs_return_acf_20": 0.19896281259210594,
        "quantile_01": -0.05662260522606146,
        "quantile_99": 0.04920809551463897,
        "hill_tail_index": 3.7850946333005475
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01829611380910452,
        "excess_kurtosis": 6.316935204587988,
        "return_acf_1": -0.18456571003245648,
        "abs_return_acf_1": 0.2992610114263365,
        "abs_return_acf_5": 0.34819846362436546,
        "abs_return_acf_20": 0.24843532604727042,
        "quantile_01": -0.05770775901516661,
        "quantile_99": 0.04961684133792141,
        "hill_tail_index": 3.1993933842046314
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.015540470312442553,
        "excess_kurtosis": 2.7162542313298834,
        "return_acf_1": -0.11571783961196293,
        "abs_return_acf_1": 0.1843253188533824,
        "abs_return_acf_5": 0.2025648542502277,
        "abs_return_acf_20": 0.1323609192347226,
        "quantile_01": -0.039029568627001694,
        "quantile_99": 0.04454194168752325,
        "hill_tail_index": 3.5787117425860955
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019470189553478345,
        "excess_kurtosis": 11.989940394727874,
        "return_acf_1": -0.20287155754804356,
        "abs_return_acf_1": 0.48878814080531224,
        "abs_return_acf_5": 0.4239752904306228,
        "abs_return_acf_20": 0.34293781850994737,
        "quantile_01": -0.06469681245389518,
        "quantile_99": 0.0607535109977209,
        "hill_tail_index": 2.580482380871682
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017103200157556953,
        "excess_kurtosis": 2.357689092085014,
        "return_acf_1": -0.14515973235433843,
        "abs_return_acf_1": 0.1831867921254506,
        "abs_return_acf_5": 0.18742889227822698,
        "abs_return_acf_20": 0.12885845771291662,
        "quantile_01": -0.04371391268092808,
        "quantile_99": 0.047165648655868274,
        "hill_tail_index": 3.779679107976102
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.014797495693094753,
        "excess_kurtosis": 2.200132587093667,
        "return_acf_1": -0.031682287906607966,
        "abs_return_acf_1": 0.19714433330454711,
        "abs_return_acf_5": 0.18646771364823522,
        "abs_return_acf_20": 0.14508819750659407,
        "quantile_01": -0.04182811812857466,
        "quantile_99": 0.03778482121190172,
        "hill_tail_index": 3.7357134761587614
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018432852272495564,
        "excess_kurtosis": 3.4455661458094227,
        "return_acf_1": -0.1430905691627227,
        "abs_return_acf_1": 0.24189611932570387,
        "abs_return_acf_5": 0.23460623695348728,
        "abs_return_acf_20": 0.18368586464101763,
        "quantile_01": -0.049846556107680566,
        "quantile_99": 0.054608184915199295,
        "hill_tail_index": 4.25350634494313
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01743233984732552,
        "excess_kurtosis": 4.851365812756718,
        "return_acf_1": -0.12511740398928048,
        "abs_return_acf_1": 0.20207510192796418,
        "abs_return_acf_5": 0.24902502018819878,
        "abs_return_acf_20": 0.2072075996528308,
        "quantile_01": -0.05119688274154882,
        "quantile_99": 0.04693366774491339,
        "hill_tail_index": 3.3420465222332583
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01892790190497371,
        "excess_kurtosis": 9.481574266201417,
        "return_acf_1": -0.18632731455775148,
        "abs_return_acf_1": 0.4416404772196862,
        "abs_return_acf_5": 0.34801895412184636,
        "abs_return_acf_20": 0.2302804151886321,
        "quantile_01": -0.060454083698559015,
        "quantile_99": 0.054673778196896713,
        "hill_tail_index": 3.732512297976337
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017888677743512237,
        "excess_kurtosis": 5.238927518821512,
        "return_acf_1": -0.2081427948735053,
        "abs_return_acf_1": 0.24736684250206253,
        "abs_return_acf_5": 0.1649098351976583,
        "abs_return_acf_20": 0.15956997968824843,
        "quantile_01": -0.051201369520124614,
        "quantile_99": 0.06109371172215061,
        "hill_tail_index": 3.988074825214091
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02052759509903105,
        "excess_kurtosis": 8.488779241680188,
        "return_acf_1": 0.02667868842508279,
        "abs_return_acf_1": 0.4549111311350297,
        "abs_return_acf_5": 0.38708665257201585,
        "abs_return_acf_20": 0.285181483778223,
        "quantile_01": -0.0674631161067685,
        "quantile_99": 0.05957383752210446,
        "hill_tail_index": 3.121329108669603
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017076279757080755,
        "excess_kurtosis": 5.33723676766234,
        "return_acf_1": -0.13641965729518765,
        "abs_return_acf_1": 0.2734783885976681,
        "abs_return_acf_5": 0.23668355111055644,
        "abs_return_acf_20": 0.1959635661869119,
        "quantile_01": -0.05004517575246018,
        "quantile_99": 0.043231616864377834,
        "hill_tail_index": 3.1782451631025292
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018083677623856462,
        "excess_kurtosis": 5.517318891756695,
        "return_acf_1": -0.1294489525978252,
        "abs_return_acf_1": 0.27003535170980436,
        "abs_return_acf_5": 0.22561339360417054,
        "abs_return_acf_20": 0.19875537114082192,
        "quantile_01": -0.04830055288827402,
        "quantile_99": 0.05868711937795681,
        "hill_tail_index": 2.680212025012494
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017149266426844736,
        "excess_kurtosis": 6.586376656777501,
        "return_acf_1": -0.07405500323209012,
        "abs_return_acf_1": 0.2828340403121465,
        "abs_return_acf_5": 0.3744315063190699,
        "abs_return_acf_20": 0.2055284194027175,
        "quantile_01": -0.05158769942601583,
        "quantile_99": 0.04997817199755105,
        "hill_tail_index": 2.669448654339119
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01740072133000857,
        "excess_kurtosis": 7.517327959735523,
        "return_acf_1": -0.09559996079571989,
        "abs_return_acf_1": 0.2664017641822567,
        "abs_return_acf_5": 0.30271403005569764,
        "abs_return_acf_20": 0.2215127821681901,
        "quantile_01": -0.053676330232456576,
        "quantile_99": 0.04860384242971616,
        "hill_tail_index": 2.785286272135201
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018156224044695923,
        "excess_kurtosis": 2.804793664332605,
        "return_acf_1": -0.1354545651017925,
        "abs_return_acf_1": 0.25853410456531634,
        "abs_return_acf_5": 0.2697663308912613,
        "abs_return_acf_20": 0.24249694948559355,
        "quantile_01": -0.0547328304955636,
        "quantile_99": 0.052997123732745524,
        "hill_tail_index": 5.390053593060314
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01769858251608252,
        "excess_kurtosis": 5.219258912815768,
        "return_acf_1": 0.021338786295031758,
        "abs_return_acf_1": 0.31851589665114693,
        "abs_return_acf_5": 0.3667690692128652,
        "abs_return_acf_20": 0.2912240265629219,
        "quantile_01": -0.061620372376036896,
        "quantile_99": 0.051478789563018774,
        "hill_tail_index": 3.3027096508394513
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01761539421950734,
        "excess_kurtosis": 11.507698438351126,
        "return_acf_1": -0.1268383797123309,
        "abs_return_acf_1": 0.26584422143860464,
        "abs_return_acf_5": 0.22097646273127966,
        "abs_return_acf_20": 0.277775322563539,
        "quantile_01": -0.050039252149471136,
        "quantile_99": 0.045288345173416004,
        "hill_tail_index": 2.365371416295003
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016523064418085355,
        "excess_kurtosis": 4.481699254138293,
        "return_acf_1": -0.18536259296328303,
        "abs_return_acf_1": 0.2444049351505178,
        "abs_return_acf_5": 0.2630853813289916,
        "abs_return_acf_20": 0.23828541045700277,
        "quantile_01": -0.044302856789098136,
        "quantile_99": 0.04785708473374527,
        "hill_tail_index": 3.3781588628895634
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0175689022261005,
        "excess_kurtosis": 4.504482994057871,
        "return_acf_1": -0.07039179628860702,
        "abs_return_acf_1": 0.27298702097555,
        "abs_return_acf_5": 0.263706091695283,
        "abs_return_acf_20": 0.19322066967674878,
        "quantile_01": -0.05485142196791507,
        "quantile_99": 0.04674385059117111,
        "hill_tail_index": 3.1225433570797168
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017911031104418454,
        "excess_kurtosis": 9.089783986136418,
        "return_acf_1": 0.0029244534460058265,
        "abs_return_acf_1": 0.3806748397701188,
        "abs_return_acf_5": 0.3939420115921695,
        "abs_return_acf_20": 0.33756424847404376,
        "quantile_01": -0.058399509878951095,
        "quantile_99": 0.05439300183111273,
        "hill_tail_index": 2.782774639864955
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01747621755499265,
        "excess_kurtosis": 3.15682578434088,
        "return_acf_1": -0.09644423850434708,
        "abs_return_acf_1": 0.23853120149930926,
        "abs_return_acf_5": 0.23379340613231878,
        "abs_return_acf_20": 0.20180488764295348,
        "quantile_01": -0.05381265006486646,
        "quantile_99": 0.04984441534310516,
        "hill_tail_index": 4.3687622324677635
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01781263498374449,
        "excess_kurtosis": 13.292047141500348,
        "return_acf_1": -0.10707614348208926,
        "abs_return_acf_1": 0.33856885269026543,
        "abs_return_acf_5": 0.2789741843690258,
        "abs_return_acf_20": 0.1962364901471772,
        "quantile_01": -0.05154651135170565,
        "quantile_99": 0.03748363965656213,
        "hill_tail_index": 2.205127614035954
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018647960829597316,
        "excess_kurtosis": 4.128830193466765,
        "return_acf_1": -0.13258647575086607,
        "abs_return_acf_1": 0.31805429023018833,
        "abs_return_acf_5": 0.3162364026550891,
        "abs_return_acf_20": 0.20996602045089954,
        "quantile_01": -0.05920687419577161,
        "quantile_99": 0.05513441072872049,
        "hill_tail_index": 4.906427790108619
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01765517644406138,
        "excess_kurtosis": 10.645247552748872,
        "return_acf_1": -0.13190477241752968,
        "abs_return_acf_1": 0.2653440768112917,
        "abs_return_acf_5": 0.3289750728482087,
        "abs_return_acf_20": 0.2801587692364711,
        "quantile_01": -0.04826640274559112,
        "quantile_99": 0.04771126976984914,
        "hill_tail_index": 2.6905171311428457
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01744647526635334,
        "excess_kurtosis": 12.099727000650386,
        "return_acf_1": -0.005918279718255908,
        "abs_return_acf_1": 0.3076602069294506,
        "abs_return_acf_5": 0.34699547329332026,
        "abs_return_acf_20": 0.21814585530871078,
        "quantile_01": -0.05242541656484381,
        "quantile_99": 0.04646497571602438,
        "hill_tail_index": 2.571641925186965
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018028239336337338,
        "excess_kurtosis": 3.7994713671846316,
        "return_acf_1": -0.0688766660860606,
        "abs_return_acf_1": 0.2904637967270486,
        "abs_return_acf_5": 0.24571556469844136,
        "abs_return_acf_20": 0.2317123111662579,
        "quantile_01": -0.05548157701686138,
        "quantile_99": 0.05052759351009731,
        "hill_tail_index": 4.715232557940446
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01553789060217586,
        "excess_kurtosis": 5.265980932970626,
        "return_acf_1": -0.19433017666245386,
        "abs_return_acf_1": 0.25407783010089313,
        "abs_return_acf_5": 0.25848699197019204,
        "abs_return_acf_20": 0.2614461953896372,
        "quantile_01": -0.03579484622720599,
        "quantile_99": 0.038445337464017584,
        "hill_tail_index": 2.6269242220736264
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01831133503393883,
        "excess_kurtosis": 2.9304158026307903,
        "return_acf_1": -0.1661477151088962,
        "abs_return_acf_1": 0.18128806124890182,
        "abs_return_acf_5": 0.2350582063312035,
        "abs_return_acf_20": 0.19021076714499707,
        "quantile_01": -0.04991683724197167,
        "quantile_99": 0.04878010458015145,
        "hill_tail_index": 4.337228314868351
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017537144752818846,
        "excess_kurtosis": 9.40269043455189,
        "return_acf_1": -0.1712772422888672,
        "abs_return_acf_1": 0.348709396684231,
        "abs_return_acf_5": 0.32333104141277336,
        "abs_return_acf_20": 0.3268682568825906,
        "quantile_01": -0.053609885445406194,
        "quantile_99": 0.04614058882141211,
        "hill_tail_index": 2.8491200164619253
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
