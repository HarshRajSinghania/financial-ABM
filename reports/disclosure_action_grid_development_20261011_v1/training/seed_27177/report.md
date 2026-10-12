# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27177
Run ID: `6057595590715a119cf55c9c0c25c60e1f6ea1816d4b2449ab66fed30d7ec202`
Result fingerprint: `7d3abdf6fe8d2ef31e3fa3b1954bde5481324db6ecfe212762700af8c47db97d`

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
    "equal_weight_sd": -0.7548809523809492,
    "equal_weight_raw": -11.323214285714238,
    "fixed_start_cap_weight_sd": -0.7159284219373787,
    "fixed_start_cap_weight_raw": -10.738926329060678,
    "end_cap_weight_sd": -0.7067868919785688,
    "end_cap_weight_raw": -10.601803379678532
  },
  "full_period_change": {
    "equal_weight_sd": -1.1393214285714237,
    "equal_weight_raw": -17.089821428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.070177579365075,
    "inflation_mean_sd": 0.5674735449735451
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19750000000000323,
    "equal_weight_raw": 2.962500000000048,
    "fixed_start_cap_weight_sd": 0.23645253044357353,
    "fixed_start_cap_weight_raw": 3.5467879566536036,
    "end_cap_weight_sd": 0.24559406040238357,
    "end_cap_weight_raw": 3.6839109060357544
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6298809523809491,
      "change_raw": -9.448214285714236,
      "decay_adjusted_gain_sd": 0.3225000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7946031746031714,
      "change_raw": -11.919047619047571,
      "decay_adjusted_gain_sd": 0.157777777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.7558531746031714,
      "change_raw": -11.33779761904757,
      "decay_adjusted_gain_sd": 0.19652777777778105
    },
    "large_minus_small_sd": 0.12597222222222226,
    "large_minus_small_raw": 1.8895833333333338
  },
  "inflation": {
    "initial_mean_sd": 0.3137499999999999,
    "final_mean_sd": 0.5691666666666667,
    "mean_sd": 0.4733839855675826,
    "mean_absolute_raw_gap": 7.100759783513738,
    "final_absolute_raw_gap": 8.5375,
    "mean_range_fraction": 0.07100759783513738
  },
  "impact": {
    "initial_share": 0.16666666666666666,
    "final_share": 0.3,
    "initial_wealth_share": 0.13567639057419908,
    "final_wealth_share": 0.48767968760002073
  },
  "pricing_slope": {
    "mean": -0.0033256655649447292,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.04593409165632946,
    "real_improvement_cost": 0.03713158603752977,
    "washing_cost": 0.008802505618799689,
    "fine_transfer": 0.009812214008250435,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.055746305664579894,
    "resource_cost_fraction_initial_cap": 0.0015311363885443152,
    "private_net_outflow_fraction_initial_cap": 0.0018582101888193299,
    "fine_transfer_fraction_initial_cap": 0.0003270738002750145,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0005580585709834218,
    "unapplied_final_day_resource_cost": 0.0038791756328507058
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 128.98916221811615,
    "beneficial_raw_gain_per_resource_cost": 1934.8374332717424,
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
    "accrued_cost": 3.2157592706743277,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.23956879448385116,
    "accrued_cost_fraction_initial_cap": 0.10719197568914425,
    "mean_contract_rate": 0.045202876944089344,
    "maximum_ledger_error": 6.098637220230962e-20
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
    "price_cap_hits": 244,
    "maximum_relative_cash_error": 2.464560233140241e-15,
    "maximum_absolute_share_error": 2.4424906541753444e-15,
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
      "minimum": -0.33231518314594477,
      "maximum": -0.19564750478160015,
      "mean": -0.2569246273689863,
      "median": -0.2569760898891368,
      "quantile_05": -0.3074817329395404,
      "quantile_95": -0.20403403970805803
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
      "minimum": 0.8333714489838427,
      "maximum": 0.9250055371317245,
      "mean": 0.885271848147532,
      "median": 0.8882937020176072,
      "quantile_05": 0.8528734124091708,
      "quantile_95": 0.9078914260931522
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
        "daily_volatility": 0.03480530006814398,
        "excess_kurtosis": 31.65445855644822,
        "return_acf_1": -0.30952561077325164,
        "abs_return_acf_1": 0.5581020827405521,
        "abs_return_acf_5": 0.3734962269328675,
        "abs_return_acf_20": 0.2358072778650199,
        "quantile_01": -0.1121805676898202,
        "quantile_99": 0.09477499874100948,
        "hill_tail_index": 2.4460275409896637
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.033757818253164776,
        "excess_kurtosis": 33.91586004879145,
        "return_acf_1": -0.2865305910448002,
        "abs_return_acf_1": 0.5284150251078544,
        "abs_return_acf_5": 0.30412332870456443,
        "abs_return_acf_20": 0.2241486152239089,
        "quantile_01": -0.12484348690730854,
        "quantile_99": 0.08088625520315901,
        "hill_tail_index": 1.557309130047931
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.03559093025257631,
        "excess_kurtosis": 28.270570451455466,
        "return_acf_1": -0.3000501627194749,
        "abs_return_acf_1": 0.5138255764495194,
        "abs_return_acf_5": 0.29207076615525124,
        "abs_return_acf_20": 0.20231222075680733,
        "quantile_01": -0.12397867790155435,
        "quantile_99": 0.11123966637881832,
        "hill_tail_index": 1.9033659839535233
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.03479860963910587,
        "excess_kurtosis": 31.86268543395434,
        "return_acf_1": -0.2752734885281008,
        "abs_return_acf_1": 0.5485240236260996,
        "abs_return_acf_5": 0.254404798937757,
        "abs_return_acf_20": 0.28685971837363633,
        "quantile_01": -0.12395036693739188,
        "quantile_99": 0.0911798395647809,
        "hill_tail_index": 1.9790144418769358
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.036605297691649184,
        "excess_kurtosis": 28.043130686790587,
        "return_acf_1": -0.2872275429740723,
        "abs_return_acf_1": 0.5119078473039383,
        "abs_return_acf_5": 0.3321777629078881,
        "abs_return_acf_20": 0.2955363493789817,
        "quantile_01": -0.14093460775893268,
        "quantile_99": 0.09712148053729854,
        "hill_tail_index": 1.9029046456958272
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.03461451408679634,
        "excess_kurtosis": 30.58176804225497,
        "return_acf_1": -0.3004686023987124,
        "abs_return_acf_1": 0.5322952447277107,
        "abs_return_acf_5": 0.31731057386740225,
        "abs_return_acf_20": 0.25126796028516757,
        "quantile_01": -0.13309839040349453,
        "quantile_99": 0.09726272486968174,
        "hill_tail_index": 2.029199353536095
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.036533815278131355,
        "excess_kurtosis": 27.412575681908134,
        "return_acf_1": -0.2239427695963449,
        "abs_return_acf_1": 0.5295213014234371,
        "abs_return_acf_5": 0.2814070690004019,
        "abs_return_acf_20": 0.2476752777763581,
        "quantile_01": -0.13991231139683247,
        "quantile_99": 0.13054636123801702,
        "hill_tail_index": 2.1405830704092064
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.034409211966970436,
        "excess_kurtosis": 30.67260031560592,
        "return_acf_1": -0.30498366003167116,
        "abs_return_acf_1": 0.5393508502119013,
        "abs_return_acf_5": 0.3382978781351814,
        "abs_return_acf_20": 0.29442318156002023,
        "quantile_01": -0.11594797478746524,
        "quantile_99": 0.08764857259036138,
        "hill_tail_index": 1.9859626875416545
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.03606882565645401,
        "excess_kurtosis": 27.489455041827284,
        "return_acf_1": -0.22195408839246414,
        "abs_return_acf_1": 0.5106477677247813,
        "abs_return_acf_5": 0.3015083949135851,
        "abs_return_acf_20": 0.2824160446262427,
        "quantile_01": -0.13360309010064017,
        "quantile_99": 0.11034346233993066,
        "hill_tail_index": 2.2338655495250164
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.03388025173688865,
        "excess_kurtosis": 32.10263049077804,
        "return_acf_1": -0.33231518314594477,
        "abs_return_acf_1": 0.5669269604022402,
        "abs_return_acf_5": 0.34790791582640346,
        "abs_return_acf_20": 0.2889025363023019,
        "quantile_01": -0.12302250480599146,
        "quantile_99": 0.0905378598519379,
        "hill_tail_index": 2.0407501732847075
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.03409497567857612,
        "excess_kurtosis": 32.42179173811427,
        "return_acf_1": -0.23961945064012394,
        "abs_return_acf_1": 0.5196022622202822,
        "abs_return_acf_5": 0.27317662772554746,
        "abs_return_acf_20": 0.25411438551141324,
        "quantile_01": -0.11930995972055024,
        "quantile_99": 0.08607020813953502,
        "hill_tail_index": 1.9979349690888724
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.03539082049849934,
        "excess_kurtosis": 28.71019801600245,
        "return_acf_1": -0.2516926086368193,
        "abs_return_acf_1": 0.5048184551992206,
        "abs_return_acf_5": 0.30439293942088097,
        "abs_return_acf_20": 0.29310187469824556,
        "quantile_01": -0.12763826912926943,
        "quantile_99": 0.09522562210749515,
        "hill_tail_index": 1.8600927839278214
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.03481747495931053,
        "excess_kurtosis": 29.67646429402707,
        "return_acf_1": -0.2742461322801986,
        "abs_return_acf_1": 0.5637222705774179,
        "abs_return_acf_5": 0.3284325266202809,
        "abs_return_acf_20": 0.27305316025269505,
        "quantile_01": -0.12460440247111199,
        "quantile_99": 0.08824581918691556,
        "hill_tail_index": 1.6433877299849127
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.03526670921770635,
        "excess_kurtosis": 30.307079375360942,
        "return_acf_1": -0.28946759355165275,
        "abs_return_acf_1": 0.5506299070322725,
        "abs_return_acf_5": 0.3438783629542695,
        "abs_return_acf_20": 0.26034138897128833,
        "quantile_01": -0.11592430543373536,
        "quantile_99": 0.08122815735191856,
        "hill_tail_index": 1.8257245596520135
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.03404290204854959,
        "excess_kurtosis": 35.6413253985,
        "return_acf_1": -0.2482847527282679,
        "abs_return_acf_1": 0.5158156833821507,
        "abs_return_acf_5": 0.2687921323211356,
        "abs_return_acf_20": 0.2456310830400636,
        "quantile_01": -0.11854312840007424,
        "quantile_99": 0.07616553288906562,
        "hill_tail_index": 1.669423651268808
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.03739994639325233,
        "excess_kurtosis": 24.268927539781053,
        "return_acf_1": -0.24155314847309764,
        "abs_return_acf_1": 0.5622458173496356,
        "abs_return_acf_5": 0.3805818846981399,
        "abs_return_acf_20": 0.3232453440998979,
        "quantile_01": -0.14489235832005554,
        "quantile_99": 0.12362669936140239,
        "hill_tail_index": 2.4524621749609614
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.037227712952326394,
        "excess_kurtosis": 27.43947866113064,
        "return_acf_1": -0.2707037505769609,
        "abs_return_acf_1": 0.5486992961092025,
        "abs_return_acf_5": 0.3653024033022867,
        "abs_return_acf_20": 0.29089054896591904,
        "quantile_01": -0.14959744648080806,
        "quantile_99": 0.12024158383461366,
        "hill_tail_index": 2.391888254897095
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.036799603414511564,
        "excess_kurtosis": 26.6723734942057,
        "return_acf_1": -0.22288565606617283,
        "abs_return_acf_1": 0.552891873109425,
        "abs_return_acf_5": 0.35985920809613625,
        "abs_return_acf_20": 0.2958160693419291,
        "quantile_01": -0.14297059637848372,
        "quantile_99": 0.11156935457870668,
        "hill_tail_index": 2.2891471290860403
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.03431154264907783,
        "excess_kurtosis": 34.922675592672896,
        "return_acf_1": -0.2886130735164938,
        "abs_return_acf_1": 0.5485643295548474,
        "abs_return_acf_5": 0.25691096073648967,
        "abs_return_acf_20": 0.26651077826745995,
        "quantile_01": -0.11458357914909438,
        "quantile_99": 0.08265485281926628,
        "hill_tail_index": 1.6982857728354275
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.037449648413745235,
        "excess_kurtosis": 25.76075458816691,
        "return_acf_1": -0.2005629439134665,
        "abs_return_acf_1": 0.5578918794954779,
        "abs_return_acf_5": 0.36050991721417264,
        "abs_return_acf_20": 0.3025932957522543,
        "quantile_01": -0.13970462222451685,
        "quantile_99": 0.1149265375868252,
        "hill_tail_index": 2.120580497483359
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.035735490149614205,
        "excess_kurtosis": 27.637394468765322,
        "return_acf_1": -0.21055555168434212,
        "abs_return_acf_1": 0.5110384518524598,
        "abs_return_acf_5": 0.33856391948818665,
        "abs_return_acf_20": 0.3084817014976358,
        "quantile_01": -0.12844159252358583,
        "quantile_99": 0.09646150215249899,
        "hill_tail_index": 1.8569155565062794
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.034786510536952475,
        "excess_kurtosis": 34.61487246035976,
        "return_acf_1": -0.2629321090509226,
        "abs_return_acf_1": 0.550850796490787,
        "abs_return_acf_5": 0.2681258349478591,
        "abs_return_acf_20": 0.25281962688685333,
        "quantile_01": -0.1052491871629413,
        "quantile_99": 0.08273774332923318,
        "hill_tail_index": 1.7995952227225878
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.03668571006010931,
        "excess_kurtosis": 28.458567803727625,
        "return_acf_1": -0.2155071483766041,
        "abs_return_acf_1": 0.5226673345111741,
        "abs_return_acf_5": 0.32535494084869626,
        "abs_return_acf_20": 0.27240175173496906,
        "quantile_01": -0.1456864262322397,
        "quantile_99": 0.1048514625624708,
        "hill_tail_index": 2.1538063346589977
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0345612663008886,
        "excess_kurtosis": 30.817512539732043,
        "return_acf_1": -0.2424448094767656,
        "abs_return_acf_1": 0.5118736784249244,
        "abs_return_acf_5": 0.26177957233884364,
        "abs_return_acf_20": 0.27200557769994593,
        "quantile_01": -0.12412518019383938,
        "quantile_99": 0.08635494774485084,
        "hill_tail_index": 1.9525863004511197
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.03679045703391892,
        "excess_kurtosis": 24.57271251700088,
        "return_acf_1": -0.25198465927217867,
        "abs_return_acf_1": 0.6046304054748445,
        "abs_return_acf_5": 0.40524198873060585,
        "abs_return_acf_20": 0.3450461885261,
        "quantile_01": -0.14540156499112167,
        "quantile_99": 0.12320532200307557,
        "hill_tail_index": 2.6365082477344273
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.036407713067543646,
        "excess_kurtosis": 27.36197834732855,
        "return_acf_1": -0.21305623437345036,
        "abs_return_acf_1": 0.5324749792888852,
        "abs_return_acf_5": 0.3110657897317338,
        "abs_return_acf_20": 0.29249249389867876,
        "quantile_01": -0.13362348833404405,
        "quantile_99": 0.10681780017460292,
        "hill_tail_index": 2.1576189623754822
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.03647770545690431,
        "excess_kurtosis": 28.979633809953253,
        "return_acf_1": -0.19564750478160015,
        "abs_return_acf_1": 0.5472544336402217,
        "abs_return_acf_5": 0.3585190305809951,
        "abs_return_acf_20": 0.3129883133330775,
        "quantile_01": -0.121457573784347,
        "quantile_99": 0.10958656325463727,
        "hill_tail_index": 2.124373634903635
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.03570024551128629,
        "excess_kurtosis": 28.280549980944762,
        "return_acf_1": -0.2619675205060949,
        "abs_return_acf_1": 0.5267253855326215,
        "abs_return_acf_5": 0.3120706268791404,
        "abs_return_acf_20": 0.2760458620132516,
        "quantile_01": -0.12294337042960153,
        "quantile_99": 0.10871000668764381,
        "hill_tail_index": 2.30044044760582
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.03650646381267994,
        "excess_kurtosis": 25.7480265920611,
        "return_acf_1": -0.20827649012366986,
        "abs_return_acf_1": 0.5475115297452114,
        "abs_return_acf_5": 0.3362791735481431,
        "abs_return_acf_20": 0.3072785522736761,
        "quantile_01": -0.13935979729949516,
        "quantile_99": 0.10874519492863514,
        "hill_tail_index": 2.1416168913063607
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.03579630280081632,
        "excess_kurtosis": 28.59110117198252,
        "return_acf_1": -0.27546598343586903,
        "abs_return_acf_1": 0.5255759036480548,
        "abs_return_acf_5": 0.2721936135228561,
        "abs_return_acf_20": 0.29918524432087296,
        "quantile_01": -0.1251482464259278,
        "quantile_99": 0.1055542697866303,
        "hill_tail_index": 2.0260688211482316
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
