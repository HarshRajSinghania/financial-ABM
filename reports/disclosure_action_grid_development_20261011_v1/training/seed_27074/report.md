# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27074
Run ID: `832169087717d304d60f17e3595ff6ff36c591212fa0a9da7671a1774d73de5f`
Result fingerprint: `2b52dc74399b8444423ecca7d27e27cb1f864a7394769ed541b63e848e14687d`

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
    "equal_weight_sd": -0.5268809523809491,
    "equal_weight_raw": -7.903214285714238,
    "fixed_start_cap_weight_sd": -0.5168385332276753,
    "fixed_start_cap_weight_raw": -7.75257799841513,
    "end_cap_weight_sd": -0.5191632595746029,
    "end_cap_weight_raw": -7.787448893619044
  },
  "full_period_change": {
    "equal_weight_sd": -0.8084880952380903,
    "equal_weight_raw": -12.127321428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7561722883597838,
    "inflation_mean_sd": 0.5788898809523809
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.42550000000000326,
    "equal_weight_raw": 6.382500000000048,
    "fixed_start_cap_weight_sd": 0.4355424191532771,
    "fixed_start_cap_weight_raw": 6.533136287299157,
    "end_cap_weight_sd": 0.4332176928063495,
    "end_cap_weight_raw": 6.498265392095244
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.44404761904761575,
      "change_raw": -6.660714285714236,
      "decay_adjusted_gain_sd": 0.5083333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.461269841269838,
      "change_raw": -6.91904761904757,
      "decay_adjusted_gain_sd": 0.4911111111111143
    },
    "small": {
      "count": 18,
      "change_sd": -0.5734920634920602,
      "change_raw": -8.602380952380903,
      "decay_adjusted_gain_sd": 0.3788888888888921
    },
    "large_minus_small_sd": 0.12944444444444442,
    "large_minus_small_raw": 1.9416666666666662
  },
  "inflation": {
    "initial_mean_sd": 0.25991666666666663,
    "final_mean_sd": 0.6084166666666668,
    "mean_sd": 0.45540112406328065,
    "mean_absolute_raw_gap": 6.831016860949208,
    "final_absolute_raw_gap": 9.12625,
    "mean_range_fraction": 0.06831016860949207
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.48,
    "initial_wealth_share": 0.3516216434060351,
    "final_wealth_share": 0.4843841226695409
  },
  "pricing_slope": {
    "mean": -0.002398470728299544,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.3516513796499636,
    "real_improvement_cost": 0.3220384313232897,
    "washing_cost": 0.029612948326673976,
    "fine_transfer": 0.00636320664160759,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.35801458629157124,
    "resource_cost_fraction_initial_cap": 0.011721712654998788,
    "private_net_outflow_fraction_initial_cap": 0.011933819543052376,
    "fine_transfer_fraction_initial_cap": 0.00021210688805358636,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.02725349313649334,
    "unapplied_final_day_resource_cost": 0.004558218802292773
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 36.300156173726585,
    "beneficial_raw_gain_per_resource_cost": 544.5023426058988,
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
    "accrued_cost": 2.868283787205435,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.10790668898504105,
    "accrued_cost_fraction_initial_cap": 0.09560945957351451,
    "mean_contract_rate": 0.04029456915666742,
    "maximum_ledger_error": 1.3552527156068805e-19
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
    "maximum_relative_cash_error": 3.3081056016564833e-15,
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
      "minimum": -0.2246376438825829,
      "maximum": -0.05950343004294708,
      "mean": -0.1344207346888772,
      "median": -0.12951369073723704,
      "quantile_05": -0.20060460681219738,
      "quantile_95": -0.07501129645634809
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
      "minimum": 0.2760354675681814,
      "maximum": 0.8132085596015719,
      "mean": 0.5579606299859048,
      "median": 0.548761010763665,
      "quantile_05": 0.36669191981702687,
      "quantile_95": 0.7609640742594246
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
        "daily_volatility": 0.01929853498606336,
        "excess_kurtosis": 40.22618646089195,
        "return_acf_1": -0.20121900859812963,
        "abs_return_acf_1": 0.4750623382103519,
        "abs_return_acf_5": 0.3652330377823488,
        "abs_return_acf_20": 0.2760337513267926,
        "quantile_01": -0.06749667616422972,
        "quantile_99": 0.03427582205264234,
        "hill_tail_index": 1.7290647490335835
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01784338381914372,
        "excess_kurtosis": 4.521822030558252,
        "return_acf_1": -0.09321382667257704,
        "abs_return_acf_1": 0.3405636833472762,
        "abs_return_acf_5": 0.3229084706650187,
        "abs_return_acf_20": 0.23258930516014878,
        "quantile_01": -0.05560488084017359,
        "quantile_99": 0.05363915660974755,
        "hill_tail_index": 4.715255520856206
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021279246746341834,
        "excess_kurtosis": 39.3306784840816,
        "return_acf_1": -0.2246376438825829,
        "abs_return_acf_1": 0.5215186184299244,
        "abs_return_acf_5": 0.41919577152336707,
        "abs_return_acf_20": 0.26816010633447507,
        "quantile_01": -0.06882750804067408,
        "quantile_99": 0.04499279188281035,
        "hill_tail_index": 2.4007071643356173
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022897703185241675,
        "excess_kurtosis": 11.903898746503337,
        "return_acf_1": -0.12944845247871278,
        "abs_return_acf_1": 0.5057286982902081,
        "abs_return_acf_5": 0.4458256595979388,
        "abs_return_acf_20": 0.32270112018468355,
        "quantile_01": -0.07061845381847921,
        "quantile_99": 0.06245812252926249,
        "hill_tail_index": 2.4160327910574546
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019541677731050654,
        "excess_kurtosis": 32.24219470359422,
        "return_acf_1": -0.14639424181673566,
        "abs_return_acf_1": 0.4087021883969418,
        "abs_return_acf_5": 0.34523616177944433,
        "abs_return_acf_20": 0.2818420591841596,
        "quantile_01": -0.059668327727379136,
        "quantile_99": 0.04451473926897006,
        "hill_tail_index": 2.295159054431336
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017969398012400266,
        "excess_kurtosis": 16.412575031570952,
        "return_acf_1": -0.13300950060952701,
        "abs_return_acf_1": 0.33654391703418346,
        "abs_return_acf_5": 0.29507821228334813,
        "abs_return_acf_20": 0.25415361673911147,
        "quantile_01": -0.055321098605266704,
        "quantile_99": 0.03730333619962639,
        "hill_tail_index": 2.5099495806082137
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01897211848900087,
        "excess_kurtosis": 10.346052679186714,
        "return_acf_1": -0.1665326365402797,
        "abs_return_acf_1": 0.42788503959427254,
        "abs_return_acf_5": 0.32184792785421246,
        "abs_return_acf_20": 0.2594273833651725,
        "quantile_01": -0.05081954515718377,
        "quantile_99": 0.049081771407766005,
        "hill_tail_index": 2.475178415247628
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02037950552352435,
        "excess_kurtosis": 19.1157295338149,
        "return_acf_1": -0.19985367129605794,
        "abs_return_acf_1": 0.5104647739983317,
        "abs_return_acf_5": 0.38238791896962876,
        "abs_return_acf_20": 0.3209919992754071,
        "quantile_01": -0.06167367997305088,
        "quantile_99": 0.05599027036917811,
        "hill_tail_index": 2.857106082810442
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02233727905978096,
        "excess_kurtosis": 8.623577032511305,
        "return_acf_1": -0.08303916177705692,
        "abs_return_acf_1": 0.46401952379045064,
        "abs_return_acf_5": 0.3749037970074453,
        "abs_return_acf_20": 0.2775056351917428,
        "quantile_01": -0.0676685239976342,
        "quantile_99": 0.061086616482814146,
        "hill_tail_index": 2.831832359391494
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02385052420349339,
        "excess_kurtosis": 11.625018691807211,
        "return_acf_1": -0.08003301812998165,
        "abs_return_acf_1": 0.5055816842186757,
        "abs_return_acf_5": 0.4666041013620782,
        "abs_return_acf_20": 0.3538919142498144,
        "quantile_01": -0.07411558759159034,
        "quantile_99": 0.07778891601208834,
        "hill_tail_index": 3.2423088607593087
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020139844811896176,
        "excess_kurtosis": 18.42288067248867,
        "return_acf_1": -0.19219108295016188,
        "abs_return_acf_1": 0.39360917052097605,
        "abs_return_acf_5": 0.3706653345025861,
        "abs_return_acf_20": 0.30098058530521565,
        "quantile_01": -0.06986665366871228,
        "quantile_99": 0.04726444362723546,
        "hill_tail_index": 2.1686809778935237
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020294558539648826,
        "excess_kurtosis": 19.233017268749617,
        "return_acf_1": -0.10742444803934377,
        "abs_return_acf_1": 0.49504294035721524,
        "abs_return_acf_5": 0.37791307800265456,
        "abs_return_acf_20": 0.3919167074697303,
        "quantile_01": -0.0677985617248124,
        "quantile_99": 0.04799958663500608,
        "hill_tail_index": 1.7824301617485092
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01836174692154531,
        "excess_kurtosis": 15.26607718425598,
        "return_acf_1": -0.17980529814958374,
        "abs_return_acf_1": 0.3997319556492214,
        "abs_return_acf_5": 0.3520033137829239,
        "abs_return_acf_20": 0.3273418822059561,
        "quantile_01": -0.05469947808537847,
        "quantile_99": 0.04972695621367381,
        "hill_tail_index": 2.2650897241070473
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019840985311708907,
        "excess_kurtosis": 7.058304404395395,
        "return_acf_1": -0.12202906395542708,
        "abs_return_acf_1": 0.3823216069486047,
        "abs_return_acf_5": 0.29751437431592875,
        "abs_return_acf_20": 0.24196012122936886,
        "quantile_01": -0.05889716875196293,
        "quantile_99": 0.05398594047167153,
        "hill_tail_index": 3.646160205286236
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01987583574563677,
        "excess_kurtosis": 3.828028806422581,
        "return_acf_1": -0.11226868134095275,
        "abs_return_acf_1": 0.3880417196204617,
        "abs_return_acf_5": 0.32266233823396173,
        "abs_return_acf_20": 0.28750739869263364,
        "quantile_01": -0.06109288343505392,
        "quantile_99": 0.05988597696826404,
        "hill_tail_index": 4.061834058129323
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018924613528906856,
        "excess_kurtosis": 7.643139770691784,
        "return_acf_1": -0.1295789289957613,
        "abs_return_acf_1": 0.3688608439730719,
        "abs_return_acf_5": 0.28881218522412927,
        "abs_return_acf_20": 0.28227580086436854,
        "quantile_01": -0.05790010489041246,
        "quantile_99": 0.04724167002274786,
        "hill_tail_index": 3.639327289060209
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01929833194728355,
        "excess_kurtosis": 21.532459469450384,
        "return_acf_1": -0.16148919284988025,
        "abs_return_acf_1": 0.4192212958698153,
        "abs_return_acf_5": 0.3090186124260502,
        "abs_return_acf_20": 0.2115178196929591,
        "quantile_01": -0.05704956682714489,
        "quantile_99": 0.05434685241253364,
        "hill_tail_index": 3.0672072495452816
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01873653105633988,
        "excess_kurtosis": 18.64478674605597,
        "return_acf_1": -0.1332931502173234,
        "abs_return_acf_1": 0.4130637046095241,
        "abs_return_acf_5": 0.37321591394284265,
        "abs_return_acf_20": 0.26841273697693496,
        "quantile_01": -0.060430114712487,
        "quantile_99": 0.042763290415414226,
        "hill_tail_index": 1.9590070494403768
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019948090022284735,
        "excess_kurtosis": 35.54533433403215,
        "return_acf_1": -0.17257047164221267,
        "abs_return_acf_1": 0.5099509290257993,
        "abs_return_acf_5": 0.44433132646856804,
        "abs_return_acf_20": 0.324620746935081,
        "quantile_01": -0.07154266357014417,
        "quantile_99": 0.04421107363702135,
        "hill_tail_index": 2.0874728423966156
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01901555651743419,
        "excess_kurtosis": 4.575829137958121,
        "return_acf_1": -0.12602030447228205,
        "abs_return_acf_1": 0.35930345617418563,
        "abs_return_acf_5": 0.3110872219985064,
        "abs_return_acf_20": 0.2762746596692752,
        "quantile_01": -0.058642339480132366,
        "quantile_99": 0.051990244663450674,
        "hill_tail_index": 3.6836002465853923
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022321207639745086,
        "excess_kurtosis": 8.620304476683556,
        "return_acf_1": -0.05950343004294708,
        "abs_return_acf_1": 0.44621259720643724,
        "abs_return_acf_5": 0.3952004690616234,
        "abs_return_acf_20": 0.3356583144648944,
        "quantile_01": -0.06875420271453508,
        "quantile_99": 0.07125940241090767,
        "hill_tail_index": 3.288828810720109
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018912325207872973,
        "excess_kurtosis": 9.778464746233814,
        "return_acf_1": -0.12977853957481708,
        "abs_return_acf_1": 0.4244560763980886,
        "abs_return_acf_5": 0.39832257666466636,
        "abs_return_acf_20": 0.32820601817749107,
        "quantile_01": -0.05625938033867685,
        "quantile_99": 0.050090856140468966,
        "hill_tail_index": 3.209779909703464
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019284237736420438,
        "excess_kurtosis": 4.574464921872095,
        "return_acf_1": -0.10076201124061776,
        "abs_return_acf_1": 0.38532413020728956,
        "abs_return_acf_5": 0.3385169602491426,
        "abs_return_acf_20": 0.2893361115702541,
        "quantile_01": -0.0640256201251982,
        "quantile_99": 0.06081560680875004,
        "hill_tail_index": 4.363086647848583
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019445525603199763,
        "excess_kurtosis": 3.487841698896929,
        "return_acf_1": -0.0960744089128815,
        "abs_return_acf_1": 0.3015485343087876,
        "abs_return_acf_5": 0.29584600676510614,
        "abs_return_acf_20": 0.25939254226171515,
        "quantile_01": -0.05981307858859334,
        "quantile_99": 0.05659934168402085,
        "hill_tail_index": 5.775784478082245
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017341396793036454,
        "excess_kurtosis": 3.675154646288588,
        "return_acf_1": -0.11626766152431274,
        "abs_return_acf_1": 0.3135406112267948,
        "abs_return_acf_5": 0.21828632879805776,
        "abs_return_acf_20": 0.20437965448408604,
        "quantile_01": -0.04555218843116634,
        "quantile_99": 0.0517992035167672,
        "hill_tail_index": 3.8141305295534025
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.0179266708178807,
        "excess_kurtosis": 3.8040968978108953,
        "return_acf_1": -0.12628444166989858,
        "abs_return_acf_1": 0.28067877151381593,
        "abs_return_acf_5": 0.27971825091212676,
        "abs_return_acf_20": 0.2467497376814577,
        "quantile_01": -0.05332255224454467,
        "quantile_99": 0.055821983948138504,
        "hill_tail_index": 4.345028316082424
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02293217133112779,
        "excess_kurtosis": 9.274108365160506,
        "return_acf_1": -0.07090261508701148,
        "abs_return_acf_1": 0.3658732105093575,
        "abs_return_acf_5": 0.33905951647701393,
        "abs_return_acf_20": 0.261616130052635,
        "quantile_01": -0.07740273649560991,
        "quantile_99": 0.06840372752178892,
        "hill_tail_index": 3.477738837227517
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018671821606379223,
        "excess_kurtosis": 21.19837331372879,
        "return_acf_1": -0.18059997304821046,
        "abs_return_acf_1": 0.44187989677181333,
        "abs_return_acf_5": 0.39399444946887296,
        "abs_return_acf_20": 0.35269146688864655,
        "quantile_01": -0.0567862713192326,
        "quantile_99": 0.04343911230978478,
        "hill_tail_index": 1.888666729049026
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019726188192148858,
        "excess_kurtosis": 14.62513556314044,
        "return_acf_1": -0.10871375829077931,
        "abs_return_acf_1": 0.43589994923811093,
        "abs_return_acf_5": 0.3786031399942255,
        "abs_return_acf_20": 0.2985047397137277,
        "quantile_01": -0.05875589606062543,
        "quantile_99": 0.05537005970267533,
        "hill_tail_index": 3.161395183640206
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018085658644844096,
        "excess_kurtosis": 14.380442332535665,
        "return_acf_1": -0.14968341686026967,
        "abs_return_acf_1": 0.3779458557170332,
        "abs_return_acf_5": 0.309253795441114,
        "abs_return_acf_20": 0.21996097604684797,
        "quantile_01": -0.04969932635621604,
        "quantile_99": 0.04778755789030356,
        "hill_tail_index": 2.749525228807599
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
