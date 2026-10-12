# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27126
Run ID: `51c522a8e5b7869b5ad02f8de497cf68218f0b171d582e3de672900598f42730`
Result fingerprint: `067116e6197371bdf89f908b30fa43d1f17a7efc746ee21da1d757f5d1080101`

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
    "equal_weight_sd": -0.6899642857142824,
    "equal_weight_raw": -10.349464285714237,
    "fixed_start_cap_weight_sd": -0.6523945807946261,
    "fixed_start_cap_weight_raw": -9.785918711919393,
    "end_cap_weight_sd": -0.6408114907058141,
    "end_cap_weight_raw": -9.612172360587211
  },
  "full_period_change": {
    "equal_weight_sd": -1.0739047619047568,
    "equal_weight_raw": -16.108571428571352
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.017574735449731,
    "inflation_mean_sd": 0.5760899470899471
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2624166666666698,
    "equal_weight_raw": 3.9362500000000478,
    "fixed_start_cap_weight_sd": 0.2999863715863263,
    "fixed_start_cap_weight_raw": 4.499795573794894,
    "end_cap_weight_sd": 0.3115694616751382,
    "end_cap_weight_raw": 4.673541925127074
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6457142857142827,
      "change_raw": -9.68571428571424,
      "decay_adjusted_gain_sd": 0.3066666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5646031746031714,
      "change_raw": -8.469047619047572,
      "decay_adjusted_gain_sd": 0.3877777777777809
    },
    "small": {
      "count": 18,
      "change_sd": -0.760019841269838,
      "change_raw": -11.40029761904757,
      "decay_adjusted_gain_sd": 0.19236111111111423
    },
    "large_minus_small_sd": 0.11430555555555533,
    "large_minus_small_raw": 1.71458333333333
  },
  "inflation": {
    "initial_mean_sd": 0.27458333333333335,
    "final_mean_sd": 0.5985833333333332,
    "mean_sd": 0.45276179572578407,
    "mean_absolute_raw_gap": 6.7914269358867605,
    "final_absolute_raw_gap": 8.978750000000002,
    "mean_range_fraction": 0.0679142693588676
  },
  "impact": {
    "initial_share": 0.4266666666666667,
    "final_share": 0.48,
    "initial_wealth_share": 0.37304271596187283,
    "final_wealth_share": 0.42692706458695345
  },
  "pricing_slope": {
    "mean": -0.0013208667933231224,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.217047515545637,
    "real_improvement_cost": 0.17606897801680454,
    "washing_cost": 0.040978537528832445,
    "fine_transfer": 0.025378298225193607,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2424258137708306,
    "resource_cost_fraction_initial_cap": 0.007234917184854568,
    "private_net_outflow_fraction_initial_cap": 0.008080860459027688,
    "fine_transfer_fraction_initial_cap": 0.0008459432741731203,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0023422451931529504,
    "unapplied_final_day_resource_cost": 0.000593069413543138
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 36.27085977100162,
    "beneficial_raw_gain_per_resource_cost": 544.0628965650243,
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
    "accrued_cost": 2.9271501681681853,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.04904030802229077,
    "accrued_cost_fraction_initial_cap": 0.09757167227227286,
    "mean_contract_rate": 0.040226418369504705,
    "maximum_ledger_error": 7.115076756936123e-20
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
    "maximum_relative_cash_error": 7.716342389359899e-16,
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
      "minimum": -0.21420106586274199,
      "maximum": -0.05718835687248289,
      "mean": -0.13919218697455235,
      "median": -0.15121431983903716,
      "quantile_05": -0.19668880654324744,
      "quantile_95": -0.07944029427472757
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
      "minimum": 0.35671351113913585,
      "maximum": 0.7420630291407231,
      "mean": 0.5683097591463628,
      "median": 0.5740292369677459,
      "quantile_05": 0.41472592161259375,
      "quantile_95": 0.6972476352811636
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
        "daily_volatility": 0.015938379088049726,
        "excess_kurtosis": 5.752009765911849,
        "return_acf_1": -0.154700374318567,
        "abs_return_acf_1": 0.17891566660486644,
        "abs_return_acf_5": 0.27721540299967773,
        "abs_return_acf_20": 0.1734919186012996,
        "quantile_01": -0.04492776121198083,
        "quantile_99": 0.041848778836339154,
        "hill_tail_index": 2.675254410316081
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016221081227969173,
        "excess_kurtosis": 4.039980130187321,
        "return_acf_1": -0.16805192528376914,
        "abs_return_acf_1": 0.23620024297759,
        "abs_return_acf_5": 0.2520442129780065,
        "abs_return_acf_20": 0.21374655417602498,
        "quantile_01": -0.04602354793317822,
        "quantile_99": 0.045872152258102976,
        "hill_tail_index": 3.558736743475093
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019051304056303068,
        "excess_kurtosis": 8.27969199324695,
        "return_acf_1": -0.19886303208415296,
        "abs_return_acf_1": 0.35025438173038503,
        "abs_return_acf_5": 0.2862352132191907,
        "abs_return_acf_20": 0.2650367303627024,
        "quantile_01": -0.06698640900517254,
        "quantile_99": 0.05016556667948539,
        "hill_tail_index": 2.6171393175673985
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017711952003150157,
        "excess_kurtosis": 5.218014276478197,
        "return_acf_1": -0.1781072700357635,
        "abs_return_acf_1": 0.29677564124393174,
        "abs_return_acf_5": 0.25799981115209897,
        "abs_return_acf_20": 0.27666565479602023,
        "quantile_01": -0.056085212617364544,
        "quantile_99": 0.046888437591289994,
        "hill_tail_index": 3.3571376514717874
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.015696975661283537,
        "excess_kurtosis": 3.4372818512461807,
        "return_acf_1": -0.19403141977102958,
        "abs_return_acf_1": 0.2160398673307521,
        "abs_return_acf_5": 0.16650732704730903,
        "abs_return_acf_20": 0.18524232667245508,
        "quantile_01": -0.04055215750922835,
        "quantile_99": 0.04683044296826431,
        "hill_tail_index": 3.744155450038988
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015137783224589882,
        "excess_kurtosis": 1.3457897325708972,
        "return_acf_1": -0.12380976375814048,
        "abs_return_acf_1": 0.08376173878908011,
        "abs_return_acf_5": 0.046849389836783085,
        "abs_return_acf_20": 0.09844117157992424,
        "quantile_01": -0.041998375321258836,
        "quantile_99": 0.03918964782706338,
        "hill_tail_index": 4.711563670103632
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016852556200985393,
        "excess_kurtosis": 8.679522937695047,
        "return_acf_1": -0.08038840296583441,
        "abs_return_acf_1": 0.3487141527457248,
        "abs_return_acf_5": 0.35522551488538767,
        "abs_return_acf_20": 0.22520217902594705,
        "quantile_01": -0.051818555622730245,
        "quantile_99": 0.04454380635148702,
        "hill_tail_index": 2.59699284158794
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01769376994147568,
        "excess_kurtosis": 4.351987131721674,
        "return_acf_1": -0.1127363966217159,
        "abs_return_acf_1": 0.30328020196168376,
        "abs_return_acf_5": 0.2709299255468443,
        "abs_return_acf_20": 0.23473237084352908,
        "quantile_01": -0.05867891890958322,
        "quantile_99": 0.051607731088437275,
        "hill_tail_index": 4.363224113925101
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017894427969929134,
        "excess_kurtosis": 8.480816480823108,
        "return_acf_1": -0.1699006986400956,
        "abs_return_acf_1": 0.3621864117488281,
        "abs_return_acf_5": 0.31858724930915633,
        "abs_return_acf_20": 0.23200986158544815,
        "quantile_01": -0.05620478685376284,
        "quantile_99": 0.04843903807369749,
        "hill_tail_index": 2.8651201057841846
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017473454555903902,
        "excess_kurtosis": 5.31413163604849,
        "return_acf_1": -0.1633558399026856,
        "abs_return_acf_1": 0.29064499414961514,
        "abs_return_acf_5": 0.271993306111724,
        "abs_return_acf_20": 0.21748868576385913,
        "quantile_01": -0.054363534449900594,
        "quantile_99": 0.04110905927133147,
        "hill_tail_index": 2.8070210676925162
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01770599417866262,
        "excess_kurtosis": 6.023000201636696,
        "return_acf_1": -0.1477282653595073,
        "abs_return_acf_1": 0.28251589066436383,
        "abs_return_acf_5": 0.29415906625401705,
        "abs_return_acf_20": 0.27814853520336136,
        "quantile_01": -0.050840421610837676,
        "quantile_99": 0.0469968086630955,
        "hill_tail_index": 3.291582795003439
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017915470033549794,
        "excess_kurtosis": 9.734307926002373,
        "return_acf_1": -0.09543367953494379,
        "abs_return_acf_1": 0.26327593183743775,
        "abs_return_acf_5": 0.19145765447536764,
        "abs_return_acf_20": 0.21025216567393543,
        "quantile_01": -0.05345585272280953,
        "quantile_99": 0.04340364027317171,
        "hill_tail_index": 2.695543373037288
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016700316144734176,
        "excess_kurtosis": 4.078381588825958,
        "return_acf_1": -0.15946334023897174,
        "abs_return_acf_1": 0.2847567778155962,
        "abs_return_acf_5": 0.1461259902104053,
        "abs_return_acf_20": 0.14742309538288595,
        "quantile_01": -0.053714068668775206,
        "quantile_99": 0.039340527686404565,
        "hill_tail_index": 2.7757873769147974
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018256357556403018,
        "excess_kurtosis": 3.8807439733690305,
        "return_acf_1": -0.11811682671556278,
        "abs_return_acf_1": 0.2876835808668459,
        "abs_return_acf_5": 0.2956206264628856,
        "abs_return_acf_20": 0.18371128509656987,
        "quantile_01": -0.05025155759132484,
        "quantile_99": 0.051153215415278515,
        "hill_tail_index": 3.5144393807022913
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017624117903884087,
        "excess_kurtosis": 6.735334586784381,
        "return_acf_1": -0.14206079672162053,
        "abs_return_acf_1": 0.2938209078230853,
        "abs_return_acf_5": 0.20333881396611467,
        "abs_return_acf_20": 0.19169225502448156,
        "quantile_01": -0.053865153457743835,
        "quantile_99": 0.042710810663146484,
        "hill_tail_index": 2.875187920332357
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018476500629012956,
        "excess_kurtosis": 7.833906708742804,
        "return_acf_1": -0.10723696826921038,
        "abs_return_acf_1": 0.32186707774735746,
        "abs_return_acf_5": 0.2997399362867214,
        "abs_return_acf_20": 0.2823791526796566,
        "quantile_01": -0.05799537026900647,
        "quantile_99": 0.05399069534265012,
        "hill_tail_index": 2.6787775545905834
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017770328923375538,
        "excess_kurtosis": 7.850979055037021,
        "return_acf_1": -0.07866456898200379,
        "abs_return_acf_1": 0.2998862019085266,
        "abs_return_acf_5": 0.32392448034096916,
        "abs_return_acf_20": 0.20480069637643042,
        "quantile_01": -0.05701028174716245,
        "quantile_99": 0.04196599813897387,
        "hill_tail_index": 2.7085818071992085
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01970404282390929,
        "excess_kurtosis": 8.237307286221673,
        "return_acf_1": -0.08709523272315826,
        "abs_return_acf_1": 0.3375599773478302,
        "abs_return_acf_5": 0.2852159411225731,
        "abs_return_acf_20": 0.25443152845738043,
        "quantile_01": -0.06388468604463358,
        "quantile_99": 0.0563721692640632,
        "hill_tail_index": 3.0763893167935934
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017024019731392198,
        "excess_kurtosis": 15.341520187393193,
        "return_acf_1": -0.10494893383390645,
        "abs_return_acf_1": 0.30758440558314937,
        "abs_return_acf_5": 0.2881199380454348,
        "abs_return_acf_20": 0.22741237780578868,
        "quantile_01": -0.052753886848898396,
        "quantile_99": 0.03631869829283454,
        "hill_tail_index": 2.132453726028699
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017460713384909957,
        "excess_kurtosis": 7.335974215454758,
        "return_acf_1": -0.09025325933991692,
        "abs_return_acf_1": 0.2585463988558818,
        "abs_return_acf_5": 0.24487659692394448,
        "abs_return_acf_20": 0.19114022252849536,
        "quantile_01": -0.05413064676118544,
        "quantile_99": 0.03754078232277733,
        "hill_tail_index": 2.4743635999527362
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02006494320379839,
        "excess_kurtosis": 4.777716129854478,
        "return_acf_1": -0.05718835687248289,
        "abs_return_acf_1": 0.3124434841873054,
        "abs_return_acf_5": 0.37515068175526994,
        "abs_return_acf_20": 0.3146423612118487,
        "quantile_01": -0.06149068919134824,
        "quantile_99": 0.05238991329461316,
        "hill_tail_index": 3.691554693231392
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018626431054360272,
        "excess_kurtosis": 5.509128133633444,
        "return_acf_1": -0.10262090484610649,
        "abs_return_acf_1": 0.3465848774011723,
        "abs_return_acf_5": 0.3385326708051055,
        "abs_return_acf_20": 0.2470468674809428,
        "quantile_01": -0.05735503578074828,
        "quantile_99": 0.05407170592961643,
        "hill_tail_index": 3.9121381096656123
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019395947715957654,
        "excess_kurtosis": 4.685160886833646,
        "return_acf_1": -0.09714538318038056,
        "abs_return_acf_1": 0.35791926861633,
        "abs_return_acf_5": 0.2703411426809157,
        "abs_return_acf_20": 0.3039178118452945,
        "quantile_01": -0.05917745928259527,
        "quantile_99": 0.052999939045200506,
        "hill_tail_index": 3.739666521328976
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016369318143257486,
        "excess_kurtosis": 2.678220978243073,
        "return_acf_1": -0.1566512268579705,
        "abs_return_acf_1": 0.2280703782903166,
        "abs_return_acf_5": 0.17718667134603755,
        "abs_return_acf_20": 0.15942814678751738,
        "quantile_01": -0.046607125443590205,
        "quantile_99": 0.044194649733540516,
        "hill_tail_index": 4.509115020072753
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01618112404447779,
        "excess_kurtosis": 3.8559512527040507,
        "return_acf_1": -0.18317427200868142,
        "abs_return_acf_1": 0.22842927048525447,
        "abs_return_acf_5": 0.2603180728071414,
        "abs_return_acf_20": 0.22419950950236642,
        "quantile_01": -0.04387010120398656,
        "quantile_99": 0.036952293517048915,
        "hill_tail_index": 2.7352660315190085
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018592795756521535,
        "excess_kurtosis": 2.722776318461179,
        "return_acf_1": -0.16208575933657762,
        "abs_return_acf_1": 0.29005862102786234,
        "abs_return_acf_5": 0.3002380733489322,
        "abs_return_acf_20": 0.2455976122710399,
        "quantile_01": -0.053656920867561075,
        "quantile_99": 0.04918188949858023,
        "hill_tail_index": 4.269662768774582
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017872842095304556,
        "excess_kurtosis": 4.317795408327695,
        "return_acf_1": -0.15918978345616522,
        "abs_return_acf_1": 0.3032651590897441,
        "abs_return_acf_5": 0.2548483727708917,
        "abs_return_acf_20": 0.1998665221939084,
        "quantile_01": -0.05550425998556339,
        "quantile_99": 0.04449940359626221,
        "hill_tail_index": 3.057010495877893
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017855320070366356,
        "excess_kurtosis": 7.994100737688754,
        "return_acf_1": -0.18776028638718772,
        "abs_return_acf_1": 0.34294653385172097,
        "abs_return_acf_5": 0.25356188039735805,
        "abs_return_acf_20": 0.21291720004238446,
        "quantile_01": -0.05424100210403408,
        "quantile_99": 0.048466874538827254,
        "hill_tail_index": 3.2259206325376457
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017498944837857393,
        "excess_kurtosis": 5.2840849975869,
        "return_acf_1": -0.18080157532772045,
        "abs_return_acf_1": 0.304671800354618,
        "abs_return_acf_5": 0.25173748512334376,
        "abs_return_acf_20": 0.2233184181307137,
        "quantile_01": -0.05504214098743845,
        "quantile_99": 0.044537876012645874,
        "hill_tail_index": 3.9909228534231564
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01592911421106695,
        "excess_kurtosis": 4.941634009254652,
        "return_acf_1": -0.21420106586274199,
        "abs_return_acf_1": 0.2702714503798803,
        "abs_return_acf_5": 0.2718134449738917,
        "abs_return_acf_20": 0.304265306364134,
        "quantile_01": -0.044467511282829456,
        "quantile_99": 0.04332172348106627,
        "hill_tail_index": 3.7393691758475485
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
