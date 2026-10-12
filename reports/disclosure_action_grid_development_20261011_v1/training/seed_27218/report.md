# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27218
Run ID: `3c97be9cf3cfe885da79ff201dc8cdcae6deaab060ada7c081358e74f51a3160`
Result fingerprint: `f48ab766972b6016623ec2af89c6bf87a7583a3e92a730892c377cee2fe6c9af`

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
    "equal_weight_sd": -0.8157142857142826,
    "equal_weight_raw": -12.23571428571424,
    "fixed_start_cap_weight_sd": -0.816713565118039,
    "fixed_start_cap_weight_raw": -12.250703476770587,
    "end_cap_weight_sd": -0.8150659636638142,
    "end_cap_weight_raw": -12.225989454957213
  },
  "full_period_change": {
    "equal_weight_sd": -1.2374047619047572,
    "equal_weight_raw": -18.56107142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1450181878306835,
    "inflation_mean_sd": 0.6671144179894181
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1366666666666698,
    "equal_weight_raw": 2.050000000000046,
    "fixed_start_cap_weight_sd": 0.13566738726291322,
    "fixed_start_cap_weight_raw": 2.0350108089436976,
    "end_cap_weight_sd": 0.13731498871713801,
    "end_cap_weight_raw": 2.0597248307570704
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8073809523809494,
      "change_raw": -12.110714285714241,
      "decay_adjusted_gain_sd": 0.14500000000000282
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7979365079365047,
      "change_raw": -11.96904761904757,
      "decay_adjusted_gain_sd": 0.1544444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.8259920634920603,
      "change_raw": -12.389880952380905,
      "decay_adjusted_gain_sd": 0.12638888888889194
    },
    "large_minus_small_sd": 0.018611111111110912,
    "large_minus_small_raw": 0.2791666666666637
  },
  "inflation": {
    "initial_mean_sd": 0.27258333333333334,
    "final_mean_sd": 0.6651666666666667,
    "mean_sd": 0.47708728837080205,
    "mean_absolute_raw_gap": 7.156309325562032,
    "final_absolute_raw_gap": 9.9775,
    "mean_range_fraction": 0.07156309325562032
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.19333333333333333,
    "initial_wealth_share": 0.13840572923980052,
    "final_wealth_share": 0.18699428416703084
  },
  "pricing_slope": {
    "mean": -0.0018149925998615362,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.01831200317227974,
    "real_improvement_cost": 0.01096555281819317,
    "washing_cost": 0.0073464503540865665,
    "fine_transfer": 0.01424925577889953,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.03256125895117927,
    "resource_cost_fraction_initial_cap": 0.0006104001057426579,
    "private_net_outflow_fraction_initial_cap": 0.001085375298372642,
    "fine_transfer_fraction_initial_cap": 0.0004749751926299842,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0003642623224548111,
    "unapplied_final_day_resource_cost": 0.00023606764108248496
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 223.89685942205236,
    "beneficial_raw_gain_per_resource_cost": 3358.4528913307854,
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
    "accrued_cost": 3.1131023424920183,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.13691186630154095,
    "accrued_cost_fraction_initial_cap": 0.10377007808306725,
    "mean_contract_rate": 0.044002001533758967,
    "maximum_ledger_error": 1.1519648082658485e-19
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
    "maximum_relative_cash_error": 3.855273907764261e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.14512920222294137,
      "maximum": 0.010228509959510277,
      "mean": -0.08017667753382408,
      "median": -0.08136513751441549,
      "quantile_05": -0.13743411481327106,
      "quantile_95": -0.02574264565379204
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
      "minimum": 0.3941376088984666,
      "maximum": 0.82744323935104,
      "mean": 0.6335067597703296,
      "median": 0.6360206968340623,
      "quantile_05": 0.4658778337802599,
      "quantile_95": 0.7709849684376842
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
        "daily_volatility": 0.020382654025885835,
        "excess_kurtosis": 9.265420732569384,
        "return_acf_1": 0.010228509959510277,
        "abs_return_acf_1": 0.4930069718521594,
        "abs_return_acf_5": 0.43607574291813267,
        "abs_return_acf_20": 0.28873025026620036,
        "quantile_01": -0.07762471252077051,
        "quantile_99": 0.05910254915395238,
        "hill_tail_index": 3.1206947142582817
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.023241129207140145,
        "excess_kurtosis": 7.99799745766806,
        "return_acf_1": -0.03737018875227612,
        "abs_return_acf_1": 0.4547583816171243,
        "abs_return_acf_5": 0.39859199306568177,
        "abs_return_acf_20": 0.3104432446908635,
        "quantile_01": -0.07964281612701207,
        "quantile_99": 0.06205482913591512,
        "hill_tail_index": 3.514504017779193
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02083959012029436,
        "excess_kurtosis": 7.32899856135227,
        "return_acf_1": -0.09061105523076304,
        "abs_return_acf_1": 0.34486888546207667,
        "abs_return_acf_5": 0.3550404728032647,
        "abs_return_acf_20": 0.2369883244333864,
        "quantile_01": -0.07251059264695925,
        "quantile_99": 0.053040820560877444,
        "hill_tail_index": 3.613551474517053
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021745287313616846,
        "excess_kurtosis": 8.63592677577509,
        "return_acf_1": -0.02768769078751704,
        "abs_return_acf_1": 0.4113005221604977,
        "abs_return_acf_5": 0.37697018718380493,
        "abs_return_acf_20": 0.21112072731830556,
        "quantile_01": -0.08244664057890941,
        "quantile_99": 0.055029672876197464,
        "hill_tail_index": 2.3432120391465547
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024615101867830686,
        "excess_kurtosis": 10.47692550302788,
        "return_acf_1": -0.12572537709654416,
        "abs_return_acf_1": 0.537682192788988,
        "abs_return_acf_5": 0.5450533001135606,
        "abs_return_acf_20": 0.4301861043900215,
        "quantile_01": -0.08139926398381878,
        "quantile_99": 0.07761910309873385,
        "hill_tail_index": 3.855849518661167
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02295233817933148,
        "excess_kurtosis": 6.627195190460503,
        "return_acf_1": -0.13882832227395367,
        "abs_return_acf_1": 0.5158937576284793,
        "abs_return_acf_5": 0.40361713867120314,
        "abs_return_acf_20": 0.3626128878134066,
        "quantile_01": -0.08033262766213602,
        "quantile_99": 0.06722410917660711,
        "hill_tail_index": 3.662702314351774
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023206813224792112,
        "excess_kurtosis": 10.344103749282283,
        "return_acf_1": -0.13573008347243679,
        "abs_return_acf_1": 0.4957841964185987,
        "abs_return_acf_5": 0.383148327627805,
        "abs_return_acf_20": 0.3771652422730151,
        "quantile_01": -0.08001808007421102,
        "quantile_99": 0.06073304437220499,
        "hill_tail_index": 2.7047067353688226
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02139534666929826,
        "excess_kurtosis": 7.250241676671283,
        "return_acf_1": -0.04974049740721435,
        "abs_return_acf_1": 0.3931492452145803,
        "abs_return_acf_5": 0.3447648684040114,
        "abs_return_acf_20": 0.30702487563101233,
        "quantile_01": -0.07156133910660557,
        "quantile_99": 0.059928554375229516,
        "hill_tail_index": 3.6307577834698472
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02161074774588851,
        "excess_kurtosis": 13.443968906288323,
        "return_acf_1": -0.08365782366495994,
        "abs_return_acf_1": 0.41742689963137874,
        "abs_return_acf_5": 0.38322149401837985,
        "abs_return_acf_20": 0.3111402535313214,
        "quantile_01": -0.06490460791848417,
        "quantile_99": 0.05996939316071378,
        "hill_tail_index": 2.711575786842818
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02231889926855811,
        "excess_kurtosis": 9.946750150863323,
        "return_acf_1": -0.11865570473519313,
        "abs_return_acf_1": 0.44613992347193177,
        "abs_return_acf_5": 0.38879378206062265,
        "abs_return_acf_20": 0.34821060243544116,
        "quantile_01": -0.06922500193689557,
        "quantile_99": 0.0697221097881803,
        "hill_tail_index": 3.1010133210346136
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021271846801005485,
        "excess_kurtosis": 9.536328086461511,
        "return_acf_1": -0.14512920222294137,
        "abs_return_acf_1": 0.464530351768798,
        "abs_return_acf_5": 0.3782118702025659,
        "abs_return_acf_20": 0.35292752613866774,
        "quantile_01": -0.07263156441415362,
        "quantile_99": 0.05710314799050902,
        "hill_tail_index": 3.1031330000636195
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021318870786024388,
        "excess_kurtosis": 9.661583189273355,
        "return_acf_1": -0.028238478859004806,
        "abs_return_acf_1": 0.39852928791924175,
        "abs_return_acf_5": 0.3924639033078656,
        "abs_return_acf_20": 0.2938904359694279,
        "quantile_01": -0.07243350807028799,
        "quantile_99": 0.06414057537152525,
        "hill_tail_index": 3.5038374569127444
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024731419643117286,
        "excess_kurtosis": 14.848228815611105,
        "return_acf_1": -0.07882391670953386,
        "abs_return_acf_1": 0.5456311367860011,
        "abs_return_acf_5": 0.4900423394303404,
        "abs_return_acf_20": 0.3851595219616469,
        "quantile_01": -0.07997943651631927,
        "quantile_99": 0.07285701415660964,
        "hill_tail_index": 3.5080260624993467
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021421593658585907,
        "excess_kurtosis": 12.198838360942622,
        "return_acf_1": -0.10175836696066522,
        "abs_return_acf_1": 0.36206538708630853,
        "abs_return_acf_5": 0.33066893861190977,
        "abs_return_acf_20": 0.2618724943126979,
        "quantile_01": -0.06727449776650608,
        "quantile_99": 0.056809333954969156,
        "hill_tail_index": 2.7410283172278374
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021231016002239183,
        "excess_kurtosis": 6.924090198660878,
        "return_acf_1": -0.09619225653818432,
        "abs_return_acf_1": 0.3826753732839229,
        "abs_return_acf_5": 0.32507385103563113,
        "abs_return_acf_20": 0.22014129196666082,
        "quantile_01": -0.07058996777204292,
        "quantile_99": 0.06566152019533521,
        "hill_tail_index": 3.113935864375038
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021959593015671477,
        "excess_kurtosis": 11.05692843696778,
        "return_acf_1": -0.1004325775001846,
        "abs_return_acf_1": 0.4886183975628696,
        "abs_return_acf_5": 0.4386110492455367,
        "abs_return_acf_20": 0.28308231396956085,
        "quantile_01": -0.06909089399477426,
        "quantile_99": 0.05969309096208443,
        "hill_tail_index": 2.5462214532006904
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02196426068318368,
        "excess_kurtosis": 17.503787317262947,
        "return_acf_1": -0.10758599157327753,
        "abs_return_acf_1": 0.5007844369299196,
        "abs_return_acf_5": 0.4700011304864715,
        "abs_return_acf_20": 0.2701396727486337,
        "quantile_01": -0.07428496163175352,
        "quantile_99": 0.05265970691814804,
        "hill_tail_index": 2.6815596475981347
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020990293556307424,
        "excess_kurtosis": 10.604381560481063,
        "return_acf_1": -0.054979013486105274,
        "abs_return_acf_1": 0.3906350996316143,
        "abs_return_acf_5": 0.3999974789370987,
        "abs_return_acf_20": 0.28642026113055263,
        "quantile_01": -0.06583261108963541,
        "quantile_99": 0.05601486408632182,
        "hill_tail_index": 2.9627448695724214
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021999940292812454,
        "excess_kurtosis": 9.00684621140669,
        "return_acf_1": -0.12169665869440414,
        "abs_return_acf_1": 0.49117949436066116,
        "abs_return_acf_5": 0.380690821731606,
        "abs_return_acf_20": 0.25344340434956036,
        "quantile_01": -0.07651811996045912,
        "quantile_99": 0.057939181090783554,
        "hill_tail_index": 2.4823123691053612
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021943244665708017,
        "excess_kurtosis": 8.884913244856147,
        "return_acf_1": -0.024151245089835204,
        "abs_return_acf_1": 0.49356824343632477,
        "abs_return_acf_5": 0.47293455992465694,
        "abs_return_acf_20": 0.2857394119575228,
        "quantile_01": -0.08183743536034481,
        "quantile_99": 0.05963423577807626,
        "hill_tail_index": 3.134094133383285
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02105196549937787,
        "excess_kurtosis": 5.096935623608344,
        "return_acf_1": -0.08051777119736199,
        "abs_return_acf_1": 0.3876623115586873,
        "abs_return_acf_5": 0.3690868297902626,
        "abs_return_acf_20": 0.2733734816794331,
        "quantile_01": -0.07315833385042769,
        "quantile_99": 0.058437548944262674,
        "hill_tail_index": 3.9580261229681986
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.023038503372716745,
        "excess_kurtosis": 10.051629983590937,
        "return_acf_1": -0.048015974674552375,
        "abs_return_acf_1": 0.4645201179251878,
        "abs_return_acf_5": 0.39805012202744855,
        "abs_return_acf_20": 0.30633438132689417,
        "quantile_01": -0.07357621178091689,
        "quantile_99": 0.061942077893130935,
        "hill_tail_index": 2.666761821548634
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022554356534994685,
        "excess_kurtosis": 10.477956435755083,
        "return_acf_1": -0.05709746656837447,
        "abs_return_acf_1": 0.4668184084639876,
        "abs_return_acf_5": 0.4501833625493958,
        "abs_return_acf_20": 0.366919765000328,
        "quantile_01": -0.08304334039018227,
        "quantile_99": 0.06736985428961707,
        "hill_tail_index": 3.608314419619652
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02020092398325709,
        "excess_kurtosis": 6.774304373690027,
        "return_acf_1": -0.048487803893706,
        "abs_return_acf_1": 0.3936990148235692,
        "abs_return_acf_5": 0.3901844821870426,
        "abs_return_acf_20": 0.27962021061743436,
        "quantile_01": -0.07075197522906793,
        "quantile_99": 0.05421105002025993,
        "hill_tail_index": 3.9647679183445392
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023680940834433024,
        "excess_kurtosis": 13.245864251530222,
        "return_acf_1": -0.06729224955087951,
        "abs_return_acf_1": 0.4086976956732983,
        "abs_return_acf_5": 0.4203519285891623,
        "abs_return_acf_20": 0.2603229931512494,
        "quantile_01": -0.0719478841468197,
        "quantile_99": 0.06381225643700514,
        "hill_tail_index": 2.844163271128667
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02180046792948089,
        "excess_kurtosis": 16.982575268645437,
        "return_acf_1": -0.1043256132200782,
        "abs_return_acf_1": 0.3915354160548226,
        "abs_return_acf_5": 0.3463988926064489,
        "abs_return_acf_20": 0.3223681601299282,
        "quantile_01": -0.07146439431939092,
        "quantile_99": 0.044467955267543505,
        "hill_tail_index": 1.965996578536347
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021898965322232324,
        "excess_kurtosis": 7.826962591944374,
        "return_acf_1": -0.0769429319979816,
        "abs_return_acf_1": 0.37989745977879197,
        "abs_return_acf_5": 0.39636355376604215,
        "abs_return_acf_20": 0.28044825963337333,
        "quantile_01": -0.06745479464668813,
        "quantile_99": 0.05701402707710525,
        "hill_tail_index": 3.4721531233689986
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021162349957655004,
        "excess_kurtosis": 11.5449479685178,
        "return_acf_1": -0.06441833185960014,
        "abs_return_acf_1": 0.41159606347889743,
        "abs_return_acf_5": 0.32688276770938296,
        "abs_return_acf_20": 0.2258954633118109,
        "quantile_01": -0.07133451502637196,
        "quantile_99": 0.05109922162650284,
        "hill_tail_index": 2.9580234232656335
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.025384773706410256,
        "excess_kurtosis": 10.731511132840739,
        "return_acf_1": -0.082212503831469,
        "abs_return_acf_1": 0.4668951004139256,
        "abs_return_acf_5": 0.4623046321465445,
        "abs_return_acf_20": 0.3827458328293612,
        "quantile_01": -0.09380436325059485,
        "quantile_99": 0.07973534555937564,
        "hill_tail_index": 3.035949935895824
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02433306627101153,
        "excess_kurtosis": 12.374958079074492,
        "return_acf_1": -0.11922373812523437,
        "abs_return_acf_1": 0.4849511441980122,
        "abs_return_acf_5": 0.425467550379448,
        "abs_return_acf_20": 0.3421551733947042,
        "quantile_01": -0.08171305592926584,
        "quantile_99": 0.07370398508394035,
        "hill_tail_index": 3.4330476409690256
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
