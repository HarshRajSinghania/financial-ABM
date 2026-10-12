# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27176
Run ID: `c76458d345c5de2e7a9ff52d486b99afcc00dd37eee63e8c06812ded35254c74`
Result fingerprint: `5ffcf82c2c54699a4fe924d2102f00b1fb028407775eae4883bea48a0913a91b`

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
    "equal_weight_sd": -0.7164642857142826,
    "equal_weight_raw": -10.746964285714238,
    "fixed_start_cap_weight_sd": -0.6426641435862516,
    "fixed_start_cap_weight_raw": -9.639962153793773,
    "end_cap_weight_sd": -0.6579985888772721,
    "end_cap_weight_raw": -9.869978833159081
  },
  "full_period_change": {
    "equal_weight_sd": -1.1121547619047571,
    "equal_weight_raw": -16.682321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0472037037036992,
    "inflation_mean_sd": 0.45123611111111117
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.23591666666666988,
    "equal_weight_raw": 3.5387500000000487,
    "fixed_start_cap_weight_sd": 0.3097168087947007,
    "fixed_start_cap_weight_raw": 4.64575213192051,
    "end_cap_weight_sd": 0.29438236350368036,
    "end_cap_weight_raw": 4.4157354525552055
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.4840476190476159,
      "change_raw": -7.260714285714238,
      "decay_adjusted_gain_sd": 0.46833333333333643
    },
    "mid": {
      "count": 9,
      "change_sd": -0.766269841269838,
      "change_raw": -11.49404761904757,
      "decay_adjusted_gain_sd": 0.18611111111111436
    },
    "small": {
      "count": 18,
      "change_sd": -0.7302976190476157,
      "change_raw": -10.954464285714236,
      "decay_adjusted_gain_sd": 0.22208333333333657
    },
    "large_minus_small_sd": 0.2462499999999998,
    "large_minus_small_raw": 3.693749999999997
  },
  "inflation": {
    "initial_mean_sd": 0.32783333333333337,
    "final_mean_sd": 0.47358333333333336,
    "mean_sd": 0.4085555786844297,
    "mean_absolute_raw_gap": 6.128333680266445,
    "final_absolute_raw_gap": 7.103749999999999,
    "mean_range_fraction": 0.061283336802664456
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.19231331279258868,
    "final_wealth_share": 0.2739592069331133
  },
  "pricing_slope": {
    "mean": -0.0007086377733170966,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.22273615887412704,
    "real_improvement_cost": 0.20504347181519672,
    "washing_cost": 0.017692687058930352,
    "fine_transfer": 0.034798503208716296,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2575346620828433,
    "resource_cost_fraction_initial_cap": 0.007424538629137566,
    "private_net_outflow_fraction_initial_cap": 0.008584488736094775,
    "fine_transfer_fraction_initial_cap": 0.0011599501069572097,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001589010892488316,
    "unapplied_final_day_resource_cost": 0.0010201833257362158
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 31.775262875031185,
    "beneficial_raw_gain_per_resource_cost": 476.62894312546774,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 3.0028346000705017,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.02664412388002483,
    "accrued_cost_fraction_initial_cap": 0.1000944866690167,
    "mean_contract_rate": 0.040914342200994,
    "maximum_ledger_error": 8.300922883092143e-20
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
    "maximum_relative_cash_error": 2.3849865597046248e-15,
    "maximum_absolute_share_error": 1.3322676295501878e-15,
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
      "minimum": -0.22152745736547944,
      "maximum": -0.059456836553130527,
      "mean": -0.14551319811287727,
      "median": -0.1413377974090418,
      "quantile_05": -0.20573288001947604,
      "quantile_95": -0.07380901166392766
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
      "minimum": 0.2440162768603427,
      "maximum": 0.769322303514602,
      "mean": 0.4040970120429192,
      "median": 0.3595710022889857,
      "quantile_05": 0.2631757437524922,
      "quantile_95": 0.6784188133949934
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
        "daily_volatility": 0.022047937294796427,
        "excess_kurtosis": 6.435467309524197,
        "return_acf_1": -0.20537580431623675,
        "abs_return_acf_1": 0.4093565627569352,
        "abs_return_acf_5": 0.3229368465000911,
        "abs_return_acf_20": 0.32041346054332764,
        "quantile_01": -0.0722301266712718,
        "quantile_99": 0.06840264494109596,
        "hill_tail_index": 4.134114391053509
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02197402565058441,
        "excess_kurtosis": 14.04420417666919,
        "return_acf_1": -0.17678482742375506,
        "abs_return_acf_1": 0.4626467884168465,
        "abs_return_acf_5": 0.4574773510589155,
        "abs_return_acf_20": 0.2809822016711526,
        "quantile_01": -0.06521534028554563,
        "quantile_99": 0.0673607416756506,
        "hill_tail_index": 2.953990956593469
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02069274046036101,
        "excess_kurtosis": 6.237470714401427,
        "return_acf_1": -0.1395873532848886,
        "abs_return_acf_1": 0.4024443259909921,
        "abs_return_acf_5": 0.3762832309313915,
        "abs_return_acf_20": 0.34520032279053214,
        "quantile_01": -0.0704851643562983,
        "quantile_99": 0.05943363216728412,
        "hill_tail_index": 3.3660409366270376
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020833840040086343,
        "excess_kurtosis": 15.114784930324731,
        "return_acf_1": -0.17231201291028111,
        "abs_return_acf_1": 0.5129160363131063,
        "abs_return_acf_5": 0.44499536082242275,
        "abs_return_acf_20": 0.36992642845449764,
        "quantile_01": -0.06958679804894302,
        "quantile_99": 0.05704385212486321,
        "hill_tail_index": 2.3028223685329796
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020600035276862855,
        "excess_kurtosis": 8.598671610078197,
        "return_acf_1": -0.13849590028531014,
        "abs_return_acf_1": 0.41445018071442413,
        "abs_return_acf_5": 0.4666400764919578,
        "abs_return_acf_20": 0.2955235395472664,
        "quantile_01": -0.06739484195689949,
        "quantile_99": 0.06375161659838378,
        "hill_tail_index": 4.058454505734972
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020490245492165354,
        "excess_kurtosis": 4.354760275688561,
        "return_acf_1": -0.08420484582584505,
        "abs_return_acf_1": 0.35759658771845654,
        "abs_return_acf_5": 0.3753603325060347,
        "abs_return_acf_20": 0.3466705121005913,
        "quantile_01": -0.06093893443107544,
        "quantile_99": 0.060688445754642974,
        "hill_tail_index": 4.6035661272916695
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019103725638828006,
        "excess_kurtosis": 6.613346139059795,
        "return_acf_1": -0.14536249881973196,
        "abs_return_acf_1": 0.3729493487271376,
        "abs_return_acf_5": 0.36320602098566107,
        "abs_return_acf_20": 0.29213735035659977,
        "quantile_01": -0.05663504349135469,
        "quantile_99": 0.060220793161513304,
        "hill_tail_index": 3.615449638011194
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01987298978491546,
        "excess_kurtosis": 8.971177990879312,
        "return_acf_1": -0.16316562421640338,
        "abs_return_acf_1": 0.4210268156181326,
        "abs_return_acf_5": 0.38646273380260504,
        "abs_return_acf_20": 0.24973575680950996,
        "quantile_01": -0.06362579478971449,
        "quantile_99": 0.05364378459672396,
        "hill_tail_index": 3.214193710843847
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019768065573547627,
        "excess_kurtosis": 3.5496003853730933,
        "return_acf_1": -0.22152745736547944,
        "abs_return_acf_1": 0.3327956867896725,
        "abs_return_acf_5": 0.29899144746180956,
        "abs_return_acf_20": 0.25251330997441224,
        "quantile_01": -0.056987439847366365,
        "quantile_99": 0.05357602472658472,
        "hill_tail_index": 4.5743125971366565
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017074145568108892,
        "excess_kurtosis": 3.5925855346585402,
        "return_acf_1": -0.13714105857589004,
        "abs_return_acf_1": 0.2965376469635002,
        "abs_return_acf_5": 0.29520144993648656,
        "abs_return_acf_20": 0.22459428353674105,
        "quantile_01": -0.049851333197458284,
        "quantile_99": 0.05126533474074249,
        "hill_tail_index": 5.074680724490626
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019028175642135024,
        "excess_kurtosis": 5.810004010112259,
        "return_acf_1": -0.20282652308977175,
        "abs_return_acf_1": 0.4455017315082694,
        "abs_return_acf_5": 0.3625864586801166,
        "abs_return_acf_20": 0.31759320172271727,
        "quantile_01": -0.06193245356399749,
        "quantile_99": 0.05303201588380939,
        "hill_tail_index": 3.028380375105719
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019350122948618226,
        "excess_kurtosis": 6.533927563657878,
        "return_acf_1": -0.12421389619696085,
        "abs_return_acf_1": 0.34331894686696474,
        "abs_return_acf_5": 0.3408596151864254,
        "abs_return_acf_20": 0.20640732065525713,
        "quantile_01": -0.058905311268447114,
        "quantile_99": 0.05926016597490454,
        "hill_tail_index": 3.521222802754611
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018127397622948092,
        "excess_kurtosis": 4.04545586857597,
        "return_acf_1": -0.14308824153319494,
        "abs_return_acf_1": 0.2691232514510509,
        "abs_return_acf_5": 0.2833767525507143,
        "abs_return_acf_20": 0.22839494373781535,
        "quantile_01": -0.048913533678689995,
        "quantile_99": 0.050393293701468944,
        "hill_tail_index": 4.086984441324616
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02066110238409355,
        "excess_kurtosis": 7.727066109031195,
        "return_acf_1": -0.12755171920653993,
        "abs_return_acf_1": 0.35652103021752757,
        "abs_return_acf_5": 0.3579708999121334,
        "abs_return_acf_20": 0.37017825486585526,
        "quantile_01": -0.06692165118595718,
        "quantile_99": 0.062379398440770235,
        "hill_tail_index": 3.5900532171076676
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021259506863441864,
        "excess_kurtosis": 9.293752464951607,
        "return_acf_1": -0.11342335682706726,
        "abs_return_acf_1": 0.47890325502028475,
        "abs_return_acf_5": 0.49951260180447277,
        "abs_return_acf_20": 0.3221167260605542,
        "quantile_01": -0.07338650435432344,
        "quantile_99": 0.06768178627812393,
        "hill_tail_index": 3.275283312511766
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017329588784761273,
        "excess_kurtosis": 7.510398678281753,
        "return_acf_1": -0.16497943240336999,
        "abs_return_acf_1": 0.38243625199704845,
        "abs_return_acf_5": 0.3211387396814989,
        "abs_return_acf_20": 0.2537052438282043,
        "quantile_01": -0.05841822859649846,
        "quantile_99": 0.04461425007787039,
        "hill_tail_index": 2.75618691181594
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020523454246315263,
        "excess_kurtosis": 7.970851336244966,
        "return_acf_1": -0.06530332916781333,
        "abs_return_acf_1": 0.3258010005419503,
        "abs_return_acf_5": 0.34470192798300864,
        "abs_return_acf_20": 0.29505705984609365,
        "quantile_01": -0.06777645565752043,
        "quantile_99": 0.061318672240514877,
        "hill_tail_index": 2.9244395572380903
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02180301812865775,
        "excess_kurtosis": 9.98742646717579,
        "return_acf_1": -0.13866787859812074,
        "abs_return_acf_1": 0.4317382426098748,
        "abs_return_acf_5": 0.36449891023890063,
        "abs_return_acf_20": 0.266402182669362,
        "quantile_01": -0.07209888068007315,
        "quantile_99": 0.06067931469218438,
        "hill_tail_index": 2.8770626958469854
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018707272938137617,
        "excess_kurtosis": 5.194819998791372,
        "return_acf_1": -0.1500094536031796,
        "abs_return_acf_1": 0.3504638616598185,
        "abs_return_acf_5": 0.31880702264492455,
        "abs_return_acf_20": 0.2394740301731122,
        "quantile_01": -0.05394832478652516,
        "quantile_99": 0.05357095277243066,
        "hill_tail_index": 3.909789289392242
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02050033577144633,
        "excess_kurtosis": 7.320764364783612,
        "return_acf_1": -0.135359808052425,
        "abs_return_acf_1": 0.3540772639150707,
        "abs_return_acf_5": 0.3613740163810883,
        "abs_return_acf_20": 0.3034115741634114,
        "quantile_01": -0.06146798295048323,
        "quantile_99": 0.06862003296392792,
        "hill_tail_index": 3.4210864423052127
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.0194059569915433,
        "excess_kurtosis": 7.588056648116211,
        "return_acf_1": -0.18124216442538843,
        "abs_return_acf_1": 0.3527942470705463,
        "abs_return_acf_5": 0.33696083269666754,
        "abs_return_acf_20": 0.3291921111528145,
        "quantile_01": -0.05322022555401026,
        "quantile_99": 0.05875605691670564,
        "hill_tail_index": 3.423271723935573
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022633453768135196,
        "excess_kurtosis": 9.432324231170893,
        "return_acf_1": -0.0981252977208195,
        "abs_return_acf_1": 0.47574500495591193,
        "abs_return_acf_5": 0.39308801362258805,
        "abs_return_acf_20": 0.3530104881000611,
        "quantile_01": -0.07503000358348928,
        "quantile_99": 0.067447741138626,
        "hill_tail_index": 3.6038951423886245
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020653256499047274,
        "excess_kurtosis": 14.775341074376026,
        "return_acf_1": -0.17842943600153338,
        "abs_return_acf_1": 0.4015976106373148,
        "abs_return_acf_5": 0.3724381387865527,
        "abs_return_acf_20": 0.28068930575079765,
        "quantile_01": -0.0593024283102356,
        "quantile_99": 0.053653880323013874,
        "hill_tail_index": 2.3564349244263583
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018639074202802905,
        "excess_kurtosis": 5.5002900826777115,
        "return_acf_1": -0.10703190708841354,
        "abs_return_acf_1": 0.2746778528362539,
        "abs_return_acf_5": 0.3373101126598906,
        "abs_return_acf_20": 0.24687919437140224,
        "quantile_01": -0.054281899722490666,
        "quantile_99": 0.04979729109953271,
        "hill_tail_index": 3.2502396783419965
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019584484056366893,
        "excess_kurtosis": 12.633175557437772,
        "return_acf_1": -0.14596717401388842,
        "abs_return_acf_1": 0.3915676825287389,
        "abs_return_acf_5": 0.4089066441886055,
        "abs_return_acf_20": 0.370983889072402,
        "quantile_01": -0.0627622199298193,
        "quantile_99": 0.04639495957056229,
        "hill_tail_index": 2.738238805793675
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021697998032576722,
        "excess_kurtosis": 9.598313566786898,
        "return_acf_1": -0.12411584871934489,
        "abs_return_acf_1": 0.3612388329646356,
        "abs_return_acf_5": 0.3354322795522417,
        "abs_return_acf_20": 0.33570877658807724,
        "quantile_01": -0.06675247136582116,
        "quantile_99": 0.06603749311655673,
        "hill_tail_index": 3.539260968144538
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020974089033292422,
        "excess_kurtosis": 13.482218169265035,
        "return_acf_1": -0.059456836553130527,
        "abs_return_acf_1": 0.4369644130629419,
        "abs_return_acf_5": 0.4680879023606514,
        "abs_return_acf_20": 0.32437414853813606,
        "quantile_01": -0.06447944178881417,
        "quantile_99": 0.05562240703409487,
        "hill_tail_index": 2.4149387556533877
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01910853607046805,
        "excess_kurtosis": 4.560256312589342,
        "return_acf_1": -0.12461495126078238,
        "abs_return_acf_1": 0.31111994889407507,
        "abs_return_acf_5": 0.2589158975663457,
        "abs_return_acf_20": 0.25642596164207987,
        "quantile_01": -0.056446621037013416,
        "quantile_99": 0.05464687438189958,
        "hill_tail_index": 3.7850126528594807
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018848466446450867,
        "excess_kurtosis": 5.751992404780104,
        "return_acf_1": -0.2060250328675809,
        "abs_return_acf_1": 0.3639873806189275,
        "abs_return_acf_5": 0.2343127696123283,
        "abs_return_acf_20": 0.2183275557325115,
        "quantile_01": -0.055972340736719174,
        "quantile_99": 0.056871101976307126,
        "hill_tail_index": 3.3263090983494
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019104933173575506,
        "excess_kurtosis": 11.79527489881701,
        "return_acf_1": -0.19100627303317053,
        "abs_return_acf_1": 0.3876281613568117,
        "abs_return_acf_5": 0.39173587977399793,
        "abs_return_acf_20": 0.30719852489276717,
        "quantile_01": -0.05670420334330292,
        "quantile_99": 0.05315769077534149,
        "hill_tail_index": 2.8814203021335696
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
