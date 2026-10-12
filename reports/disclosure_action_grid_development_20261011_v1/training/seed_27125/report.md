# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27125
Run ID: `553fb09d52269b50b409413f97dab7e291e2af780e773615dc45b52fbd1124e0`
Result fingerprint: `d285536a01d34ebac193e44647b27e52fd21aa485ef900150172e2fb1910fbd9`

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
    "equal_weight_sd": -0.6032182539682509,
    "equal_weight_raw": -9.048273809523765,
    "fixed_start_cap_weight_sd": -0.484608206911898,
    "fixed_start_cap_weight_raw": -7.269123103678469,
    "end_cap_weight_sd": -0.5075668712954777,
    "end_cap_weight_raw": -7.613503069432163
  },
  "full_period_change": {
    "equal_weight_sd": -0.9892728488103005,
    "equal_weight_raw": -14.839092732154509
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9243707324081843,
    "inflation_mean_sd": 0.7127734788359789
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3036049636629568,
    "equal_weight_raw": 4.554074454944352,
    "fixed_start_cap_weight_sd": 0.2583646217494555,
    "fixed_start_cap_weight_raw": 3.875469326241833,
    "end_cap_weight_sd": 0.2565572594258667,
    "end_cap_weight_raw": 3.848358891388001
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5932142857142823,
      "change_raw": -8.898214285714234,
      "decay_adjusted_gain_sd": 0.22104963662954155
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5629497354497327,
      "change_raw": -8.44424603174599,
      "decay_adjusted_gain_sd": 0.2836111111111138
    },
    "small": {
      "count": 18,
      "change_sd": -0.6250198412698381,
      "change_raw": -9.375297619047572,
      "decay_adjusted_gain_sd": 0.32736111111111427
    },
    "large_minus_small_sd": 0.031805555555555864,
    "large_minus_small_raw": 0.47708333333333797
  },
  "inflation": {
    "initial_mean_sd": 0.35775000000000007,
    "final_mean_sd": 0.7269166666666668,
    "mean_sd": 0.6074911878989732,
    "mean_absolute_raw_gap": 9.112367818484598,
    "final_absolute_raw_gap": 10.903750000000002,
    "mean_range_fraction": 0.09112367818484599
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.3466666666666667,
    "initial_wealth_share": 0.26344398747873515,
    "final_wealth_share": 0.3253220948169564
  },
  "pricing_slope": {
    "mean": -0.002183574553296975,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.04835540463037527,
    "real_improvement_cost": 0.03473793953260701,
    "washing_cost": 0.013617465097768268,
    "fine_transfer": 0.05847838371651165,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10683378834688692,
    "resource_cost_fraction_initial_cap": 0.001611846821012509,
    "private_net_outflow_fraction_initial_cap": 0.003561126278229564,
    "fine_transfer_fraction_initial_cap": 0.001949279457217055,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0014283092570690351,
    "unapplied_final_day_resource_cost": 0.0016483552397724569
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 188.35844678605514,
    "beneficial_raw_gain_per_resource_cost": 2825.376701790827,
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
    "accrued_cost": 2.8229247410298033,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.15326573516067335,
    "accrued_cost_fraction_initial_cap": 0.09409749136766012,
    "mean_contract_rate": 0.039443664720685105,
    "maximum_ledger_error": 1.6940658945086007e-19
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
    "price_cap_hits": 3,
    "maximum_relative_cash_error": 1.3744584989977823e-15,
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
      "minimum": -0.28786934447118057,
      "maximum": -0.0935440484841906,
      "mean": -0.17174068156025057,
      "median": -0.15005479665157584,
      "quantile_05": -0.26668214542251395,
      "quantile_95": -0.10402118003272318
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
      "minimum": 0.3919099747185478,
      "maximum": 0.7952507935403249,
      "mean": 0.6379818459906794,
      "median": 0.6567971285792613,
      "quantile_05": 0.45862794409808977,
      "quantile_95": 0.7507730677415657
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
        "daily_volatility": 0.018300431817704313,
        "excess_kurtosis": 8.938166558689627,
        "return_acf_1": -0.11083371360534411,
        "abs_return_acf_1": 0.2777441322349388,
        "abs_return_acf_5": 0.287760234567512,
        "abs_return_acf_20": 0.2712898944488446,
        "quantile_01": -0.06099439474356958,
        "quantile_99": 0.045691626803408665,
        "hill_tail_index": 2.8763009235404455
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019882567693485367,
        "excess_kurtosis": 22.922036279535007,
        "return_acf_1": -0.13624065532308996,
        "abs_return_acf_1": 0.34907479167043304,
        "abs_return_acf_5": 0.3612190334287518,
        "abs_return_acf_20": 0.2597264628410435,
        "quantile_01": -0.05498495034696844,
        "quantile_99": 0.052488676815818515,
        "hill_tail_index": 2.9247707215224326
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01872220092881022,
        "excess_kurtosis": 7.744262785746118,
        "return_acf_1": -0.21100195883228373,
        "abs_return_acf_1": 0.281613430879357,
        "abs_return_acf_5": 0.2264758439096413,
        "abs_return_acf_20": 0.21953403317047418,
        "quantile_01": -0.061204849737179,
        "quantile_99": 0.053112242339006493,
        "hill_tail_index": 3.531810023231707
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01800890176504439,
        "excess_kurtosis": 6.367445036793573,
        "return_acf_1": -0.11203424004524191,
        "abs_return_acf_1": 0.3055537175943417,
        "abs_return_acf_5": 0.22181127401054118,
        "abs_return_acf_20": 0.2523789490958879,
        "quantile_01": -0.05644692222029741,
        "quantile_99": 0.05037805023103026,
        "hill_tail_index": 2.7723274407054177
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020688370668982527,
        "excess_kurtosis": 15.920537308059135,
        "return_acf_1": -0.11669226083431752,
        "abs_return_acf_1": 0.36698193580965704,
        "abs_return_acf_5": 0.37838669294716365,
        "abs_return_acf_20": 0.30974856952208074,
        "quantile_01": -0.06412761137994372,
        "quantile_99": 0.061773562101947385,
        "hill_tail_index": 2.6952588357136453
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019073356856579887,
        "excess_kurtosis": 5.730077669617273,
        "return_acf_1": -0.15169602376021077,
        "abs_return_acf_1": 0.3988694908959211,
        "abs_return_acf_5": 0.2904594152183693,
        "abs_return_acf_20": 0.2794072987320493,
        "quantile_01": -0.06379610658942396,
        "quantile_99": 0.06419717942274285,
        "hill_tail_index": 4.31764360144005
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020282552243326254,
        "excess_kurtosis": 9.94701797250034,
        "return_acf_1": -0.28786934447118057,
        "abs_return_acf_1": 0.4444038156227234,
        "abs_return_acf_5": 0.3763375239590955,
        "abs_return_acf_20": 0.33329659880825413,
        "quantile_01": -0.0730533012185633,
        "quantile_99": 0.05840467254427949,
        "hill_tail_index": 2.915724275199381
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020013429674372248,
        "excess_kurtosis": 7.613091312874422,
        "return_acf_1": -0.136073687737776,
        "abs_return_acf_1": 0.39467809571831947,
        "abs_return_acf_5": 0.3417399279173278,
        "abs_return_acf_20": 0.2891973311177186,
        "quantile_01": -0.06744510659337818,
        "quantile_99": 0.05511490461599813,
        "hill_tail_index": 3.0975424620778904
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019398023302627118,
        "excess_kurtosis": 8.389173261596548,
        "return_acf_1": -0.15505543312804015,
        "abs_return_acf_1": 0.2625999655311214,
        "abs_return_acf_5": 0.29140532981222717,
        "abs_return_acf_20": 0.29437456647364435,
        "quantile_01": -0.06224092922618651,
        "quantile_99": 0.05201543039259977,
        "hill_tail_index": 2.6951196805673776
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020190439085360112,
        "excess_kurtosis": 7.893921936473829,
        "return_acf_1": -0.0935440484841906,
        "abs_return_acf_1": 0.36865055754534903,
        "abs_return_acf_5": 0.32049942151937244,
        "abs_return_acf_20": 0.27967710113993327,
        "quantile_01": -0.0702323960772079,
        "quantile_99": 0.05743707578209308,
        "hill_tail_index": 3.217787449719794
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019118594017432596,
        "excess_kurtosis": 7.401105788595386,
        "return_acf_1": -0.22541235411237617,
        "abs_return_acf_1": 0.39711398625759975,
        "abs_return_acf_5": 0.35901708022184436,
        "abs_return_acf_20": 0.27903741508478236,
        "quantile_01": -0.061028880820008465,
        "quantile_99": 0.055611552988355024,
        "hill_tail_index": 3.673043498160443
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019585365217036247,
        "excess_kurtosis": 8.464304090079695,
        "return_acf_1": -0.14841356954294088,
        "abs_return_acf_1": 0.307781569128041,
        "abs_return_acf_5": 0.29720895416246423,
        "abs_return_acf_20": 0.23166601820858596,
        "quantile_01": -0.06631494461489441,
        "quantile_99": 0.05034334244373054,
        "hill_tail_index": 4.055665897848724
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018954093998540974,
        "excess_kurtosis": 11.199999639276724,
        "return_acf_1": -0.12490054359959576,
        "abs_return_acf_1": 0.33157758847302155,
        "abs_return_acf_5": 0.34687767953415444,
        "abs_return_acf_20": 0.2547503853165434,
        "quantile_01": -0.060581231228777406,
        "quantile_99": 0.052707128567973244,
        "hill_tail_index": 2.555543490863527
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018904333091972897,
        "excess_kurtosis": 6.126141191449934,
        "return_acf_1": -0.10986483164969715,
        "abs_return_acf_1": 0.29724359615272056,
        "abs_return_acf_5": 0.3247445292520719,
        "abs_return_acf_20": 0.2910804233213235,
        "quantile_01": -0.06555660308360295,
        "quantile_99": 0.05192777258113968,
        "hill_tail_index": 3.3163346783618888
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018486197088991914,
        "excess_kurtosis": 6.304967180724326,
        "return_acf_1": -0.1423610587441983,
        "abs_return_acf_1": 0.33853954708705075,
        "abs_return_acf_5": 0.32017587086794075,
        "abs_return_acf_20": 0.29975636289226637,
        "quantile_01": -0.0586034528813457,
        "quantile_99": 0.050262270765957254,
        "hill_tail_index": 3.0779442414083054
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018468428479841266,
        "excess_kurtosis": 8.348115446953843,
        "return_acf_1": -0.14221886167798467,
        "abs_return_acf_1": 0.2838313802114696,
        "abs_return_acf_5": 0.2989207712669793,
        "abs_return_acf_20": 0.258865149813043,
        "quantile_01": -0.05441329309304009,
        "quantile_99": 0.05534647413549372,
        "hill_tail_index": 3.2498537289426093
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018947888622561034,
        "excess_kurtosis": 7.160521959171529,
        "return_acf_1": -0.14627814147175702,
        "abs_return_acf_1": 0.29927964925130185,
        "abs_return_acf_5": 0.2831365342955292,
        "abs_return_acf_20": 0.2142383030290242,
        "quantile_01": -0.0679895187779428,
        "quantile_99": 0.0494873739965988,
        "hill_tail_index": 2.882707989927894
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02096595347197959,
        "excess_kurtosis": 6.697219757878882,
        "return_acf_1": -0.24185011858255306,
        "abs_return_acf_1": 0.4548582112506196,
        "abs_return_acf_5": 0.3772239563941328,
        "abs_return_acf_20": 0.3339006276609299,
        "quantile_01": -0.07796795643953953,
        "quantile_99": 0.060979095283787525,
        "hill_tail_index": 3.980925117644697
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019573143960413823,
        "excess_kurtosis": 8.75967625408173,
        "return_acf_1": -0.11414869520819856,
        "abs_return_acf_1": 0.29769021579953026,
        "abs_return_acf_5": 0.26669370151798116,
        "abs_return_acf_20": 0.23955769924850795,
        "quantile_01": -0.06989209176978864,
        "quantile_99": 0.054115587422836516,
        "hill_tail_index": 2.7237569373752977
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01951194873768615,
        "excess_kurtosis": 5.38045433570616,
        "return_acf_1": -0.1862387562927087,
        "abs_return_acf_1": 0.41288849186719545,
        "abs_return_acf_5": 0.36498548614726173,
        "abs_return_acf_20": 0.35993598926584325,
        "quantile_01": -0.06136078023217611,
        "quantile_99": 0.05533216518642404,
        "hill_tail_index": 3.9133929401047993
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01979993091812414,
        "excess_kurtosis": 9.30714923011636,
        "return_acf_1": -0.09924001052792622,
        "abs_return_acf_1": 0.32811796619126776,
        "abs_return_acf_5": 0.3793804034358701,
        "abs_return_acf_20": 0.2939078430380245,
        "quantile_01": -0.06077311550472248,
        "quantile_99": 0.061357287276277164,
        "hill_tail_index": 2.9469354713350535
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01913998409636319,
        "excess_kurtosis": 5.107491569876034,
        "return_acf_1": -0.211028081480747,
        "abs_return_acf_1": 0.41165591789623984,
        "abs_return_acf_5": 0.33750785142881523,
        "abs_return_acf_20": 0.30455916436606517,
        "quantile_01": -0.059661017326283795,
        "quantile_99": 0.055628756430829526,
        "hill_tail_index": 4.2257948103260885
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020372665501174735,
        "excess_kurtosis": 7.117256663694098,
        "return_acf_1": -0.1424466341172412,
        "abs_return_acf_1": 0.41907131830414734,
        "abs_return_acf_5": 0.33211539724398853,
        "abs_return_acf_20": 0.27760066580691206,
        "quantile_01": -0.0747021539052747,
        "quantile_99": 0.056851571361540766,
        "hill_tail_index": 3.661279539378728
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019768491137486584,
        "excess_kurtosis": 4.457883877852925,
        "return_acf_1": -0.2313339122441566,
        "abs_return_acf_1": 0.3851459664754408,
        "abs_return_acf_5": 0.33189164364571405,
        "abs_return_acf_20": 0.3141502697101753,
        "quantile_01": -0.060067328107321696,
        "quantile_99": 0.05408131421202851,
        "hill_tail_index": 4.2811572641504245
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01974971477102809,
        "excess_kurtosis": 8.531594290391965,
        "return_acf_1": -0.22934583598607972,
        "abs_return_acf_1": 0.37304240707650366,
        "abs_return_acf_5": 0.24844522536801855,
        "abs_return_acf_20": 0.28035081773700643,
        "quantile_01": -0.0650935274756906,
        "quantile_99": 0.05277216412664661,
        "hill_tail_index": 2.7860856804058174
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019455461846697317,
        "excess_kurtosis": 5.9227252554705,
        "return_acf_1": -0.16442748841462582,
        "abs_return_acf_1": 0.3581610092838699,
        "abs_return_acf_5": 0.30125928316120176,
        "abs_return_acf_20": 0.31856977583530083,
        "quantile_01": -0.06486592854385213,
        "quantile_99": 0.05643670312358693,
        "hill_tail_index": 4.549374868926918
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017885271696346773,
        "excess_kurtosis": 8.083751925460403,
        "return_acf_1": -0.22964087120969714,
        "abs_return_acf_1": 0.3662844432638164,
        "abs_return_acf_5": 0.33932824877569784,
        "abs_return_acf_20": 0.2218771496950205,
        "quantile_01": -0.06052133509403251,
        "quantile_99": 0.049203000983238966,
        "hill_tail_index": 2.938704822951885
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02052112872813373,
        "excess_kurtosis": 9.957913703128703,
        "return_acf_1": -0.2706998499002923,
        "abs_return_acf_1": 0.3319934722819317,
        "abs_return_acf_5": 0.2543347207886052,
        "abs_return_acf_20": 0.21538986242473665,
        "quantile_01": -0.07431546685379672,
        "quantile_99": 0.057374387726437846,
        "hill_tail_index": 2.963360449165334
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018573529652815956,
        "excess_kurtosis": 5.565843959423004,
        "return_acf_1": -0.21955784809561338,
        "abs_return_acf_1": 0.2985694616744319,
        "abs_return_acf_5": 0.2673145430072018,
        "abs_return_acf_20": 0.29110535758100325,
        "quantile_01": -0.05881973395248396,
        "quantile_99": 0.04838305563851691,
        "hill_tail_index": 3.618022556196059
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01872533784192823,
        "excess_kurtosis": 6.251070256409454,
        "return_acf_1": -0.2617716177274516,
        "abs_return_acf_1": 0.44165900095798905,
        "abs_return_acf_5": 0.32560630795734646,
        "abs_return_acf_20": 0.3132447645435879,
        "quantile_01": -0.06486109912267682,
        "quantile_99": 0.05410737934992955,
        "hill_tail_index": 3.57829365660742
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
