# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27024
Run ID: `80e031d0f913cb5658e095b68fd6c0b1bc59dcbb002445dbda161546c8664f6c`
Result fingerprint: `0c22d96747b7f2489977ca010b613360bfcc55c3bfeb92c2a99909938045cc02`

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
    "equal_weight_sd": -0.5242976190476158,
    "equal_weight_raw": -7.864464285714235,
    "fixed_start_cap_weight_sd": -0.4083460349371429,
    "fixed_start_cap_weight_raw": -6.125190524057144,
    "end_cap_weight_sd": -0.41150413919553375,
    "end_cap_weight_raw": -6.172562087933007
  },
  "full_period_change": {
    "equal_weight_sd": -0.895404761904757,
    "equal_weight_raw": -13.431071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8551415343915298,
    "inflation_mean_sd": 0.6608912037037037
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.42808333333333665,
    "equal_weight_raw": 6.4212500000000485,
    "fixed_start_cap_weight_sd": 0.5440349174438095,
    "fixed_start_cap_weight_raw": 8.16052376165714,
    "end_cap_weight_sd": 0.5408768131854185,
    "end_cap_weight_raw": 8.113152197781279
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.23654761904761576,
      "change_raw": -3.5482142857142365,
      "decay_adjusted_gain_sd": 0.7158333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.440158730158727,
      "change_raw": -6.602380952380905,
      "decay_adjusted_gain_sd": 0.5122222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.6143253968253934,
      "change_raw": -9.214880952380902,
      "decay_adjusted_gain_sd": 0.33805555555555883
    },
    "large_minus_small_sd": 0.37777777777777766,
    "large_minus_small_raw": 5.666666666666665
  },
  "inflation": {
    "initial_mean_sd": 0.24116666666666667,
    "final_mean_sd": 0.7188333333333333,
    "mean_sd": 0.48233041909519847,
    "mean_absolute_raw_gap": 7.234956286427977,
    "final_absolute_raw_gap": 10.7825,
    "mean_range_fraction": 0.07234956286427977
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.19383303097291407,
    "final_wealth_share": 0.2726181460282899
  },
  "pricing_slope": {
    "mean": -0.0036461571574984163,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.2551443971248848,
    "real_improvement_cost": 0.2104811707992555,
    "washing_cost": 0.0446632263256293,
    "fine_transfer": 0.00437363886358491,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2595180359884697,
    "resource_cost_fraction_initial_cap": 0.00850481323749616,
    "private_net_outflow_fraction_initial_cap": 0.008650601199615656,
    "fine_transfer_fraction_initial_cap": 0.000145787962119497,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.08175318415692998,
    "unapplied_final_day_resource_cost": 0.047124785009468664
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 50.33424266696367,
    "beneficial_raw_gain_per_resource_cost": 755.013640004455,
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
    "accrued_cost": 2.8934043040304296,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.0827861721600472,
    "accrued_cost_fraction_initial_cap": 0.09644681013434765,
    "mean_contract_rate": 0.03987269914182439,
    "maximum_ledger_error": 9.910285482875314e-20
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
    "maximum_relative_cash_error": 2.1848166803788146e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.20605730743039985,
      "maximum": 0.00298750911661556,
      "mean": -0.14826217067051983,
      "median": -0.15542785838893647,
      "quantile_05": -0.20168639904075855,
      "quantile_95": -0.09136905424514852
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
      "minimum": 0.21307842763889626,
      "maximum": 0.8460724133280182,
      "mean": 0.5772380898437558,
      "median": 0.6229059547398879,
      "quantile_05": 0.27713817289741066,
      "quantile_95": 0.7894367147227884
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
        "daily_volatility": 0.026524699521756172,
        "excess_kurtosis": 17.37594257366073,
        "return_acf_1": -0.19999623522178497,
        "abs_return_acf_1": 0.4473923236644188,
        "abs_return_acf_5": 0.45628166809105536,
        "abs_return_acf_20": 0.33915541298019974,
        "quantile_01": -0.09886263075906726,
        "quantile_99": 0.0687788868506989,
        "hill_tail_index": 2.7017327001477467
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022613747432233707,
        "excess_kurtosis": 11.72310582839395,
        "return_acf_1": -0.15696275916302013,
        "abs_return_acf_1": 0.32040850017053035,
        "abs_return_acf_5": 0.3686771740787359,
        "abs_return_acf_20": 0.22607467388056568,
        "quantile_01": -0.07050356540785663,
        "quantile_99": 0.05982567120566242,
        "hill_tail_index": 3.5073418010697353
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020728607011126894,
        "excess_kurtosis": 7.28612451379222,
        "return_acf_1": -0.09998362553331157,
        "abs_return_acf_1": 0.3341209490550616,
        "abs_return_acf_5": 0.4066455009132934,
        "abs_return_acf_20": 0.3148526611550367,
        "quantile_01": -0.06810391986452854,
        "quantile_99": 0.06524876820858404,
        "hill_tail_index": 3.0444419758310004
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.024422666426002805,
        "excess_kurtosis": 12.933844133865744,
        "return_acf_1": -0.16489484195113127,
        "abs_return_acf_1": 0.4380227330147364,
        "abs_return_acf_5": 0.45242424992669644,
        "abs_return_acf_20": 0.3765444544399292,
        "quantile_01": -0.08526179052598594,
        "quantile_99": 0.07222753234775899,
        "hill_tail_index": 2.5064624230090655
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.025268756373402118,
        "excess_kurtosis": 14.334805127779184,
        "return_acf_1": -0.1679234225603745,
        "abs_return_acf_1": 0.34266601295029914,
        "abs_return_acf_5": 0.38671403958901474,
        "abs_return_acf_20": 0.24680482256483366,
        "quantile_01": -0.09833620786098676,
        "quantile_99": 0.06036501556399138,
        "hill_tail_index": 2.204250484944082
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021009496191980562,
        "excess_kurtosis": 20.305680975119156,
        "return_acf_1": -0.09289033239735513,
        "abs_return_acf_1": 0.24147700920064413,
        "abs_return_acf_5": 0.3277542293792861,
        "abs_return_acf_20": 0.16659232424314818,
        "quantile_01": -0.05876837240748375,
        "quantile_99": 0.0497305898738121,
        "hill_tail_index": 2.5791841110888587
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02045846741956065,
        "excess_kurtosis": 7.624639889114848,
        "return_acf_1": -0.12807205287862938,
        "abs_return_acf_1": 0.3086160972694029,
        "abs_return_acf_5": 0.29179380499170365,
        "abs_return_acf_20": 0.21217309424153283,
        "quantile_01": -0.05831686133192735,
        "quantile_99": 0.052432771745815704,
        "hill_tail_index": 3.0940189317124576
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017382576723170128,
        "excess_kurtosis": 2.6853055199352474,
        "return_acf_1": -0.09012437212061583,
        "abs_return_acf_1": 0.16230235143568192,
        "abs_return_acf_5": 0.22784470657176262,
        "abs_return_acf_20": 0.2333776058941268,
        "quantile_01": -0.04597130549779701,
        "quantile_99": 0.04649275040737883,
        "hill_tail_index": 3.5986431704570325
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022810925366708246,
        "excess_kurtosis": 8.916104348162616,
        "return_acf_1": -0.17129905273526155,
        "abs_return_acf_1": 0.30280733556453765,
        "abs_return_acf_5": 0.32977672829505306,
        "abs_return_acf_20": 0.1774141668205373,
        "quantile_01": -0.0733615411626716,
        "quantile_99": 0.0584889455054399,
        "hill_tail_index": 3.820936386953049
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018480788311600275,
        "excess_kurtosis": 7.237591270089439,
        "return_acf_1": -0.19478955422623168,
        "abs_return_acf_1": 0.41593333029839086,
        "abs_return_acf_5": 0.43335131960386186,
        "abs_return_acf_20": 0.27580239474016083,
        "quantile_01": -0.06347493353534532,
        "quantile_99": 0.05125369317131875,
        "hill_tail_index": 3.1926246671511924
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.024753458332395437,
        "excess_kurtosis": 14.310396452196766,
        "return_acf_1": -0.18545358495241326,
        "abs_return_acf_1": 0.4229721328267387,
        "abs_return_acf_5": 0.459235722020318,
        "abs_return_acf_20": 0.29703638220173784,
        "quantile_01": -0.09079999999397637,
        "quantile_99": 0.07064603412071431,
        "hill_tail_index": 2.670997544768265
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024463050556367827,
        "excess_kurtosis": 10.695481949016994,
        "return_acf_1": -0.16923264281913494,
        "abs_return_acf_1": 0.40063996092623205,
        "abs_return_acf_5": 0.45316155228607147,
        "abs_return_acf_20": 0.34677871959196677,
        "quantile_01": -0.09613862834834727,
        "quantile_99": 0.06306794733125755,
        "hill_tail_index": 3.3621915410940604
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019273877486150708,
        "excess_kurtosis": 4.562053439160096,
        "return_acf_1": -0.16196331498707026,
        "abs_return_acf_1": 0.34654815248813486,
        "abs_return_acf_5": 0.3162439463850277,
        "abs_return_acf_20": 0.2615472011044001,
        "quantile_01": -0.05199001926571775,
        "quantile_99": 0.061500903689833464,
        "hill_tail_index": 3.546957571779903
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.026685605632673953,
        "excess_kurtosis": 19.9266863887259,
        "return_acf_1": -0.20605730743039985,
        "abs_return_acf_1": 0.45358310885575137,
        "abs_return_acf_5": 0.44283510722662145,
        "abs_return_acf_20": 0.32266538245268844,
        "quantile_01": -0.09787243880228079,
        "quantile_99": 0.07743550748335278,
        "hill_tail_index": 2.7713924969724344
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02489614422706728,
        "excess_kurtosis": 13.611456875904206,
        "return_acf_1": -0.14457563898413409,
        "abs_return_acf_1": 0.36681389220728344,
        "abs_return_acf_5": 0.33029354676029327,
        "abs_return_acf_20": 0.24762290404063952,
        "quantile_01": -0.08466098223181037,
        "quantile_99": 0.06600675196065044,
        "hill_tail_index": 2.1861500926545174
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020504502896024904,
        "excess_kurtosis": 8.766249531835296,
        "return_acf_1": -0.1538929576148528,
        "abs_return_acf_1": 0.36722248677720515,
        "abs_return_acf_5": 0.40398658582681646,
        "abs_return_acf_20": 0.3071682367663341,
        "quantile_01": -0.06901170383632221,
        "quantile_99": 0.0496493588043789,
        "hill_tail_index": 3.09716890312709
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021482196023837132,
        "excess_kurtosis": 9.991003692452734,
        "return_acf_1": -0.1707964353418453,
        "abs_return_acf_1": 0.30976671769282976,
        "abs_return_acf_5": 0.33384477719802963,
        "abs_return_acf_20": 0.28933437905175974,
        "quantile_01": -0.08445524430481273,
        "quantile_99": 0.04976001049522897,
        "hill_tail_index": 2.8336334529698726
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016652135524387122,
        "excess_kurtosis": 3.8623217777526495,
        "return_acf_1": -0.11324001883792614,
        "abs_return_acf_1": 0.22325672913208008,
        "abs_return_acf_5": 0.30591131664054305,
        "abs_return_acf_20": 0.24424890050589948,
        "quantile_01": -0.04688367059161565,
        "quantile_99": 0.04813626685633896,
        "hill_tail_index": 4.83046133078666
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.024543525204922218,
        "excess_kurtosis": 11.339220350626796,
        "return_acf_1": -0.1862751517509668,
        "abs_return_acf_1": 0.35025417289281174,
        "abs_return_acf_5": 0.37167128088252605,
        "abs_return_acf_20": 0.2822442694225999,
        "quantile_01": -0.09399914198869973,
        "quantile_99": 0.06544284014665595,
        "hill_tail_index": 3.1072212276279974
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02205564766041979,
        "excess_kurtosis": 13.148823139558978,
        "return_acf_1": -0.14113222885172938,
        "abs_return_acf_1": 0.425630017330562,
        "abs_return_acf_5": 0.4170208276969161,
        "abs_return_acf_20": 0.3621305045359899,
        "quantile_01": -0.07464235080466988,
        "quantile_99": 0.06093930522673085,
        "hill_tail_index": 2.999778561012355
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021770767940293315,
        "excess_kurtosis": 13.831672666546964,
        "return_acf_1": -0.15249435533337038,
        "abs_return_acf_1": 0.3111138025941784,
        "abs_return_acf_5": 0.38005550311349723,
        "abs_return_acf_20": 0.25798821465004024,
        "quantile_01": -0.06271610576121203,
        "quantile_99": 0.05809429073886772,
        "hill_tail_index": 2.553310851755007
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022048225970185048,
        "excess_kurtosis": 13.51524264137483,
        "return_acf_1": 0.00298750911661556,
        "abs_return_acf_1": 0.4374275783401786,
        "abs_return_acf_5": 0.46946354955690894,
        "abs_return_acf_20": 0.42275084794190443,
        "quantile_01": -0.07893544516452751,
        "quantile_99": 0.07995155656773592,
        "hill_tail_index": 2.6218324880511905
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024109031035598874,
        "excess_kurtosis": 13.960260322158806,
        "return_acf_1": -0.1431481539705114,
        "abs_return_acf_1": 0.33308050261625677,
        "abs_return_acf_5": 0.40911837693157965,
        "abs_return_acf_20": 0.2717042892869054,
        "quantile_01": -0.08966498350080292,
        "quantile_99": 0.06446900579905325,
        "hill_tail_index": 2.832452892411524
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023019875667851943,
        "excess_kurtosis": 11.262827669009548,
        "return_acf_1": -0.2030692603471915,
        "abs_return_acf_1": 0.38873988612973703,
        "abs_return_acf_5": 0.4119435152707219,
        "abs_return_acf_20": 0.25591638623864355,
        "quantile_01": -0.08496465027772032,
        "quantile_99": 0.06522823764671845,
        "hill_tail_index": 2.563494633827134
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0224551751976426,
        "excess_kurtosis": 17.710978632158387,
        "return_acf_1": -0.14167848634235,
        "abs_return_acf_1": 0.39000084495830134,
        "abs_return_acf_5": 0.3958695348542446,
        "abs_return_acf_20": 0.2775511949254663,
        "quantile_01": -0.08243846683014404,
        "quantile_99": 0.05611006632244249,
        "hill_tail_index": 2.37809867421818
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022475545643120296,
        "excess_kurtosis": 8.259381342343804,
        "return_acf_1": -0.19630898037554836,
        "abs_return_acf_1": 0.4045410683332832,
        "abs_return_acf_5": 0.3581340311231095,
        "abs_return_acf_20": 0.32122690502736045,
        "quantile_01": -0.08034524324726507,
        "quantile_99": 0.06557771831524047,
        "hill_tail_index": 3.237909051895095
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.024586892366032936,
        "excess_kurtosis": 16.54745561501167,
        "return_acf_1": -0.13961585898746431,
        "abs_return_acf_1": 0.3765628970520476,
        "abs_return_acf_5": 0.46263808313086435,
        "abs_return_acf_20": 0.296598068722938,
        "quantile_01": -0.0916270315748351,
        "quantile_99": 0.06693242467052485,
        "hill_tail_index": 3.1993852980684903
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02561534926698065,
        "excess_kurtosis": 20.369081019817532,
        "return_acf_1": -0.1063436912718576,
        "abs_return_acf_1": 0.42481700125129446,
        "abs_return_acf_5": 0.46040909614119213,
        "abs_return_acf_20": 0.32444319578768144,
        "quantile_01": -0.09320053245441257,
        "quantile_99": 0.07274530844963796,
        "hill_tail_index": 2.541852593269789
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022490590320759365,
        "excess_kurtosis": 12.293520264843938,
        "return_acf_1": -0.1570489285691684,
        "abs_return_acf_1": 0.2856692888836689,
        "abs_return_acf_5": 0.3976455637513321,
        "abs_return_acf_20": 0.31052416817638434,
        "quantile_01": -0.07675277839046174,
        "quantile_99": 0.05463931652697974,
        "hill_tail_index": 3.413586359519851
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017137721163325785,
        "excess_kurtosis": 3.3539815453770094,
        "return_acf_1": -0.11158938367655884,
        "abs_return_acf_1": 0.2881518858952028,
        "abs_return_acf_5": 0.22971932230378503,
        "abs_return_acf_20": 0.18681659037304044,
        "quantile_01": -0.04640009818311278,
        "quantile_99": 0.04719068285082277,
        "hill_tail_index": 3.5749227071484517
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
