# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27121
Run ID: `f382288c6c746d5f3f0d918faba5f17778f4a6c9ea8ecb7f27404ca9dd63b309`
Result fingerprint: `61024ea789c10f12f077107d6781af031317ee256666e8e5b392a6518c5ad02b`

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
    "equal_weight_sd": -0.6459227996603402,
    "equal_weight_raw": -9.6888419949051,
    "fixed_start_cap_weight_sd": -0.606836758455942,
    "fixed_start_cap_weight_raw": -9.102551376839129,
    "end_cap_weight_sd": -0.606256482162347,
    "end_cap_weight_raw": -9.093847232435204
  },
  "full_period_change": {
    "equal_weight_sd": -0.9533632758508145,
    "equal_weight_raw": -14.300449137762218
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8841170236462295,
    "inflation_mean_sd": 0.6774216269841271
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.29423809523809824,
    "equal_weight_raw": 4.413571428571474,
    "fixed_start_cap_weight_sd": 0.33656132796644206,
    "fixed_start_cap_weight_raw": 5.04841991949663,
    "end_cap_weight_sd": 0.34189969125083564,
    "end_cap_weight_raw": 5.128495368762534
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6232142857142824,
      "change_raw": -9.348214285714235,
      "decay_adjusted_gain_sd": 0.3291666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5302982210900301,
      "change_raw": -7.954473316350452,
      "decay_adjusted_gain_sd": 0.3813492063492092
    },
    "small": {
      "count": 18,
      "change_sd": -0.707519841269838,
      "change_raw": -10.612797619047571,
      "decay_adjusted_gain_sd": 0.24486111111111425
    },
    "large_minus_small_sd": 0.08430555555555563,
    "large_minus_small_raw": 1.2645833333333345
  },
  "inflation": {
    "initial_mean_sd": 0.28099999999999997,
    "final_mean_sd": 0.7119166666666669,
    "mean_sd": 0.5248336802664446,
    "mean_absolute_raw_gap": 7.8725052039966705,
    "final_absolute_raw_gap": 10.67875,
    "mean_range_fraction": 0.0787250520399667
  },
  "impact": {
    "initial_share": 0.3,
    "final_share": 0.35333333333333333,
    "initial_wealth_share": 0.24793514963421986,
    "final_wealth_share": 0.32609940368606943
  },
  "pricing_slope": {
    "mean": -0.0034413832885654754,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.06637214710921613,
    "real_improvement_cost": 0.0439057289569964,
    "washing_cost": 0.022466418152219718,
    "fine_transfer": 0.0057364904900916005,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07210863759930773,
    "resource_cost_fraction_initial_cap": 0.0022124049036405377,
    "private_net_outflow_fraction_initial_cap": 0.002403621253310258,
    "fine_transfer_fraction_initial_cap": 0.00019121634966972004,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.006919841638505088,
    "unapplied_final_day_resource_cost": 0.0026470468121014886
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 132.99468589765195,
    "beneficial_raw_gain_per_resource_cost": 1994.9202884647793,
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
    "accrued_cost": 3.0254050669802717,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": -0.04921459078979553,
    "accrued_cost_fraction_initial_cap": 0.10084683556600907,
    "mean_contract_rate": 0.042168586242871176,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 1.7758151392833124e-15,
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
      "minimum": -0.18846591729615364,
      "maximum": -0.023957384477473885,
      "mean": -0.10971213998685302,
      "median": -0.11243313898854401,
      "quantile_05": -0.1672720402898106,
      "quantile_95": -0.03820311096682967
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
      "minimum": 0.2473672801842809,
      "maximum": 0.7921484447516683,
      "mean": 0.5650552693877944,
      "median": 0.5808696317171284,
      "quantile_05": 0.31709086006269244,
      "quantile_95": 0.7643510022658585
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
        "daily_volatility": 0.01981026996366488,
        "excess_kurtosis": 8.066901436817178,
        "return_acf_1": -0.05954209216674799,
        "abs_return_acf_1": 0.44810555402820584,
        "abs_return_acf_5": 0.33431194348154997,
        "abs_return_acf_20": 0.3583522054499401,
        "quantile_01": -0.06661171844709103,
        "quantile_99": 0.05842340257646913,
        "hill_tail_index": 3.3190785005862735
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019399206207765706,
        "excess_kurtosis": 4.212427478218857,
        "return_acf_1": -0.1309422924404921,
        "abs_return_acf_1": 0.32097931925203343,
        "abs_return_acf_5": 0.2934096004763972,
        "abs_return_acf_20": 0.3176661834075105,
        "quantile_01": -0.06408526125965587,
        "quantile_99": 0.05620440118653473,
        "hill_tail_index": 4.585615354119378
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018478868458621532,
        "excess_kurtosis": 6.807564243462766,
        "return_acf_1": -0.16506663249980907,
        "abs_return_acf_1": 0.35242314017999804,
        "abs_return_acf_5": 0.32579421559571103,
        "abs_return_acf_20": 0.28607969367626357,
        "quantile_01": -0.05631131222897897,
        "quantile_99": 0.04687345312501925,
        "hill_tail_index": 2.996858570710893
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021260500746955048,
        "excess_kurtosis": 10.02520440573923,
        "return_acf_1": -0.06262133462877419,
        "abs_return_acf_1": 0.40941240551501706,
        "abs_return_acf_5": 0.36976866539805364,
        "abs_return_acf_20": 0.3141240739721034,
        "quantile_01": -0.07594769824943406,
        "quantile_99": 0.07092710057697174,
        "hill_tail_index": 3.3966932514149986
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.023006264811772887,
        "excess_kurtosis": 12.633944472686574,
        "return_acf_1": -0.10167001352935971,
        "abs_return_acf_1": 0.436116560912075,
        "abs_return_acf_5": 0.4744615010736169,
        "abs_return_acf_20": 0.3674986627706205,
        "quantile_01": -0.08121253827627743,
        "quantile_99": 0.06597022036573554,
        "hill_tail_index": 3.4703911558441494
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0222909369433181,
        "excess_kurtosis": 12.561161974525822,
        "return_acf_1": -0.07714027800488596,
        "abs_return_acf_1": 0.48716428908188586,
        "abs_return_acf_5": 0.4603805556515268,
        "abs_return_acf_20": 0.35100048729696737,
        "quantile_01": -0.07966114288657901,
        "quantile_99": 0.06139854295331014,
        "hill_tail_index": 2.873033294452014
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020663274934294706,
        "excess_kurtosis": 8.263671916635042,
        "return_acf_1": -0.03116027418665905,
        "abs_return_acf_1": 0.4324561620870815,
        "abs_return_acf_5": 0.3354229362091528,
        "abs_return_acf_20": 0.3595780088177073,
        "quantile_01": -0.07225664889036358,
        "quantile_99": 0.06383322162581638,
        "hill_tail_index": 3.129889790433768
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.0202991212348064,
        "excess_kurtosis": 17.12082412234088,
        "return_acf_1": -0.08163221668953045,
        "abs_return_acf_1": 0.45345485102627603,
        "abs_return_acf_5": 0.42732272361754897,
        "abs_return_acf_20": 0.41832405915625387,
        "quantile_01": -0.07330348200815825,
        "quantile_99": 0.05817331235792121,
        "hill_tail_index": 2.3410884984035394
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021958623495096877,
        "excess_kurtosis": 11.101234248976931,
        "return_acf_1": -0.0468110225870381,
        "abs_return_acf_1": 0.4343302012012661,
        "abs_return_acf_5": 0.40423380674016235,
        "abs_return_acf_20": 0.37512021859091604,
        "quantile_01": -0.07911594803175656,
        "quantile_99": 0.061277444823094294,
        "hill_tail_index": 2.65309495826157
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022506842724251335,
        "excess_kurtosis": 11.800379776971903,
        "return_acf_1": -0.1154281677905692,
        "abs_return_acf_1": 0.5075848682745635,
        "abs_return_acf_5": 0.4727122826876114,
        "abs_return_acf_20": 0.37617070898799637,
        "quantile_01": -0.08409916345454162,
        "quantile_99": 0.06384961696047821,
        "hill_tail_index": 2.4971133580224105
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021485823592948972,
        "excess_kurtosis": 10.090452334054335,
        "return_acf_1": -0.12185167260411815,
        "abs_return_acf_1": 0.428189835976502,
        "abs_return_acf_5": 0.45014032520382063,
        "abs_return_acf_20": 0.3991803657992907,
        "quantile_01": -0.08006541416453367,
        "quantile_99": 0.061649938217043745,
        "hill_tail_index": 2.5955533231691756
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017767865814335614,
        "excess_kurtosis": 3.5080098286844565,
        "return_acf_1": -0.15983946656681688,
        "abs_return_acf_1": 0.20530183154280857,
        "abs_return_acf_5": 0.25652742411907387,
        "abs_return_acf_20": 0.2567121718650657,
        "quantile_01": -0.04969532919259835,
        "quantile_99": 0.04795802867791939,
        "hill_tail_index": 3.859600813019175
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018312021068784008,
        "excess_kurtosis": 6.627310904091482,
        "return_acf_1": -0.08592332695798173,
        "abs_return_acf_1": 0.38898716471580597,
        "abs_return_acf_5": 0.34905140324143674,
        "abs_return_acf_20": 0.3249136250041442,
        "quantile_01": -0.06831918862748086,
        "quantile_99": 0.04704937807071034,
        "hill_tail_index": 2.584672112398139
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018792980422331174,
        "excess_kurtosis": 7.581396191644746,
        "return_acf_1": -0.11385330557929876,
        "abs_return_acf_1": 0.31587132576760096,
        "abs_return_acf_5": 0.3161689449350773,
        "abs_return_acf_20": 0.26248189779738496,
        "quantile_01": -0.05727882248650161,
        "quantile_99": 0.05931173766398647,
        "hill_tail_index": 4.791400615945971
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017240763371299563,
        "excess_kurtosis": 2.958664233824222,
        "return_acf_1": -0.1435255907022135,
        "abs_return_acf_1": 0.28189957194765203,
        "abs_return_acf_5": 0.27240315785699803,
        "abs_return_acf_20": 0.25191422221971616,
        "quantile_01": -0.04680232416279447,
        "quantile_99": 0.05615700784096332,
        "hill_tail_index": 4.802584448755682
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020477404203122603,
        "excess_kurtosis": 5.846017285429614,
        "return_acf_1": -0.16907646484526642,
        "abs_return_acf_1": 0.4193050563506371,
        "abs_return_acf_5": 0.45317272549542986,
        "abs_return_acf_20": 0.3943169318312342,
        "quantile_01": -0.0673325965025576,
        "quantile_99": 0.06699637617868213,
        "hill_tail_index": 4.3939701192321
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020127590082056557,
        "excess_kurtosis": 7.984946739160618,
        "return_acf_1": -0.13135831381466312,
        "abs_return_acf_1": 0.4479273301332697,
        "abs_return_acf_5": 0.4145395949775518,
        "abs_return_acf_20": 0.36768188868114393,
        "quantile_01": -0.07964373502531472,
        "quantile_99": 0.04918597952275403,
        "hill_tail_index": 2.7824388190233282
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01853109851030804,
        "excess_kurtosis": 7.297442908613759,
        "return_acf_1": -0.1634079742490322,
        "abs_return_acf_1": 0.35571521051215566,
        "abs_return_acf_5": 0.29493085573257904,
        "abs_return_acf_20": 0.29196585567978195,
        "quantile_01": -0.054269290130580856,
        "quantile_99": 0.051942912778566,
        "hill_tail_index": 2.7935673869434963
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021534329089460326,
        "excess_kurtosis": 10.747671513526875,
        "return_acf_1": -0.11101297239778928,
        "abs_return_acf_1": 0.43205590339271577,
        "abs_return_acf_5": 0.4175902897897834,
        "abs_return_acf_20": 0.3555804316867959,
        "quantile_01": -0.07540593222192692,
        "quantile_99": 0.06324466818602585,
        "hill_tail_index": 3.0170132688253153
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021389256758323753,
        "excess_kurtosis": 9.173345137587635,
        "return_acf_1": -0.16241939976213832,
        "abs_return_acf_1": 0.40414037952005205,
        "abs_return_acf_5": 0.3823220724968457,
        "abs_return_acf_20": 0.3751824349590527,
        "quantile_01": -0.07517430452501843,
        "quantile_99": 0.06844251267557337,
        "hill_tail_index": 2.7274668712210173
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02366442606326553,
        "excess_kurtosis": 18.400144148851613,
        "return_acf_1": -0.09176590605607841,
        "abs_return_acf_1": 0.4322267229342667,
        "abs_return_acf_5": 0.43068994266995697,
        "abs_return_acf_20": 0.32342705677551137,
        "quantile_01": -0.07913553538904831,
        "quantile_99": 0.0777766828070554,
        "hill_tail_index": 3.3178601207469365
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018887195759095383,
        "excess_kurtosis": 9.389049394079366,
        "return_acf_1": -0.06389912122618752,
        "abs_return_acf_1": 0.32927179875136964,
        "abs_return_acf_5": 0.3243759696177549,
        "abs_return_acf_20": 0.27239807927421567,
        "quantile_01": -0.06076477877320123,
        "quantile_99": 0.0444537618228612,
        "hill_tail_index": 2.405160914199662
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021585873268062987,
        "excess_kurtosis": 8.968404680367788,
        "return_acf_1": -0.15223826420300732,
        "abs_return_acf_1": 0.4780962156521208,
        "abs_return_acf_5": 0.42646102883554865,
        "abs_return_acf_20": 0.39773169450291246,
        "quantile_01": -0.07925449989691291,
        "quantile_99": 0.061365572112308656,
        "hill_tail_index": 3.1116756867980104
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01980861898229118,
        "excess_kurtosis": 8.901096070581417,
        "return_acf_1": -0.12738127577123895,
        "abs_return_acf_1": 0.3952219526841899,
        "abs_return_acf_5": 0.36752980330255197,
        "abs_return_acf_20": 0.3173896762632223,
        "quantile_01": -0.06687818905240679,
        "quantile_99": 0.059068009020038705,
        "hill_tail_index": 3.1442648417955903
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023528375120304854,
        "excess_kurtosis": 18.040166496603028,
        "return_acf_1": -0.023957384477473885,
        "abs_return_acf_1": 0.48214660050023517,
        "abs_return_acf_5": 0.42023880169697514,
        "abs_return_acf_20": 0.37001093805515817,
        "quantile_01": -0.07438248419330633,
        "quantile_99": 0.06942536900348259,
        "hill_tail_index": 2.2286022048537
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019780634060430447,
        "excess_kurtosis": 7.379235285860119,
        "return_acf_1": -0.10971156655214007,
        "abs_return_acf_1": 0.32899915744086217,
        "abs_return_acf_5": 0.3796651936179385,
        "abs_return_acf_20": 0.32276318171981505,
        "quantile_01": -0.05981341762196943,
        "quantile_99": 0.052351109823907796,
        "hill_tail_index": 2.7845735879481373
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020478823790412347,
        "excess_kurtosis": 9.051405655288287,
        "return_acf_1": -0.08333374567297092,
        "abs_return_acf_1": 0.4040107043294549,
        "abs_return_acf_5": 0.35404586436413327,
        "abs_return_acf_20": 0.39100783201018985,
        "quantile_01": -0.06891429946497465,
        "quantile_99": 0.05985240239523876,
        "hill_tail_index": 3.1885453442297407
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021966370746123738,
        "excess_kurtosis": 16.398027481996923,
        "return_acf_1": -0.11449745154714554,
        "abs_return_acf_1": 0.56641510965582,
        "abs_return_acf_5": 0.5584111877330253,
        "abs_return_acf_20": 0.38177880083864624,
        "quantile_01": -0.07190486707146795,
        "quantile_99": 0.05856129254335068,
        "hill_tail_index": 2.649885676597545
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019921233052405615,
        "excess_kurtosis": 7.516488437709528,
        "return_acf_1": -0.10183075480000979,
        "abs_return_acf_1": 0.3436311395849987,
        "abs_return_acf_5": 0.3288062494615175,
        "abs_return_acf_20": 0.29078443443941493,
        "quantile_01": -0.07140178377846222,
        "quantile_99": 0.05265994117011315,
        "hill_tail_index": 2.9037944908641853
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017259969095406693,
        "excess_kurtosis": 2.243058242677873,
        "return_acf_1": -0.18846591729615364,
        "abs_return_acf_1": 0.24077151944652478,
        "abs_return_acf_5": 0.21625497012455894,
        "abs_return_acf_20": 0.204779893164829,
        "quantile_01": -0.050695186157814966,
        "quantile_99": 0.04564083382497387,
        "hill_tail_index": 4.957766847486221
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
