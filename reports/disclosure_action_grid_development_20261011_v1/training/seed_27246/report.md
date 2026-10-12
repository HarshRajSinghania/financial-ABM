# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27246
Run ID: `675ac79f5449cacce8b54a2f60b89a0ae8d0b7968ba160d70d4ad0cc6aeb4fbd`
Result fingerprint: `fc8c9b5713ef859d1d6465fd9c0ba89eafea4b26cf08f3f2d35afe6ac90d3513`

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
    "equal_weight_sd": -0.8069756358550998,
    "equal_weight_raw": -12.1046345378265,
    "fixed_start_cap_weight_sd": -0.7315844561038629,
    "fixed_start_cap_weight_raw": -10.973766841557943,
    "end_cap_weight_sd": -0.7073111564246821,
    "end_cap_weight_raw": -10.60966734637023
  },
  "full_period_change": {
    "equal_weight_sd": -1.2235827787122415,
    "equal_weight_raw": -18.353741680683623
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1469877041852217,
    "inflation_mean_sd": 0.4527602513227514
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11375000000000283,
    "equal_weight_raw": 1.7062500000000427,
    "fixed_start_cap_weight_sd": 0.19606773122271906,
    "fixed_start_cap_weight_raw": 2.9410159683407873,
    "end_cap_weight_sd": 0.22932153110511416,
    "end_cap_weight_raw": 3.439822966576711
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5707142857142826,
      "change_raw": -8.560714285714239,
      "decay_adjusted_gain_sd": 0.38166666666666976
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8151440377968329,
      "change_raw": -12.227160566952493,
      "decay_adjusted_gain_sd": 0.0855555555555579
    },
    "small": {
      "count": 18,
      "change_sd": -0.8422683265743697,
      "change_raw": -12.634024898615545,
      "decay_adjusted_gain_sd": 0.08319444444444746
    },
    "large_minus_small_sd": 0.27155404086008705,
    "large_minus_small_raw": 4.073310612901306
  },
  "inflation": {
    "initial_mean_sd": 0.2258333333333333,
    "final_mean_sd": 0.49266666666666675,
    "mean_sd": 0.32976075492645013,
    "mean_absolute_raw_gap": 4.946411323896753,
    "final_absolute_raw_gap": 7.39,
    "mean_range_fraction": 0.04946411323896753
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.41333333333333333,
    "initial_wealth_share": 0.24042578361072908,
    "final_wealth_share": 0.3661135775643305
  },
  "pricing_slope": {
    "mean": -0.002090692999358066,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.023122263385016925,
    "real_improvement_cost": 0.018865640532893285,
    "washing_cost": 0.004256622852123645,
    "fine_transfer": 0.007396163373714823,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.03051842675873175,
    "resource_cost_fraction_initial_cap": 0.0007707421128338974,
    "private_net_outflow_fraction_initial_cap": 0.0010172808919577249,
    "fine_transfer_fraction_initial_cap": 0.0002465387791238274,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001168076543314599,
    "unapplied_final_day_resource_cost": 0.0005117053325582346
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 147.58503279619947,
    "beneficial_raw_gain_per_resource_cost": 2213.7754919429917,
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
    "fixed_exposure": 15.000000000000002,
    "accrued_cost": 3.2028319503531066,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": -0.22664147416263009,
    "accrued_cost_fraction_initial_cap": 0.10676106501177021,
    "mean_contract_rate": 0.04342989870984797,
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
    "maximum_relative_cash_error": 1.7056678626871612e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.25002128327406986,
      "maximum": -0.01187401326880199,
      "mean": -0.17286370945820762,
      "median": -0.17673056236040682,
      "quantile_05": -0.2266406611039108,
      "quantile_95": -0.0914133234705403
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
      "minimum": 0.15066745741697873,
      "maximum": 0.8284364888937975,
      "mean": 0.5067034225352128,
      "median": 0.49174346940258906,
      "quantile_05": 0.21596469658776546,
      "quantile_95": 0.7990672560821089
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
        "daily_volatility": 0.016595870694496372,
        "excess_kurtosis": 5.125935081630727,
        "return_acf_1": -0.1453188908661777,
        "abs_return_acf_1": 0.2706803225152693,
        "abs_return_acf_5": 0.2464246360802698,
        "abs_return_acf_20": 0.22367835133368033,
        "quantile_01": -0.04556627135288059,
        "quantile_99": 0.04291796122650821,
        "hill_tail_index": 3.6141428655824543
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01903592543249793,
        "excess_kurtosis": 4.83752505301339,
        "return_acf_1": -0.13057469241734843,
        "abs_return_acf_1": 0.36134340911243273,
        "abs_return_acf_5": 0.33694448387302994,
        "abs_return_acf_20": 0.3008787166092031,
        "quantile_01": -0.06774271774076207,
        "quantile_99": 0.04669745538004244,
        "hill_tail_index": 3.2711750481798445
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.024156999385658094,
        "excess_kurtosis": 12.816535988560808,
        "return_acf_1": -0.25002128327406986,
        "abs_return_acf_1": 0.4546039834044789,
        "abs_return_acf_5": 0.4647654723853769,
        "abs_return_acf_20": 0.4068674725159774,
        "quantile_01": -0.08918836678346717,
        "quantile_99": 0.07210268181531625,
        "hill_tail_index": 3.4498465774711544
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02173974737946718,
        "excess_kurtosis": 9.40141845680911,
        "return_acf_1": -0.17742822013336518,
        "abs_return_acf_1": 0.3969338922021855,
        "abs_return_acf_5": 0.39746207473029377,
        "abs_return_acf_20": 0.3913744553101317,
        "quantile_01": -0.08169314283811333,
        "quantile_99": 0.06561308555451517,
        "hill_tail_index": 3.197116342699606
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024765406699909457,
        "excess_kurtosis": 11.677040818280032,
        "return_acf_1": -0.17222536244255643,
        "abs_return_acf_1": 0.40427337488203163,
        "abs_return_acf_5": 0.4508351053266785,
        "abs_return_acf_20": 0.3738906635233093,
        "quantile_01": -0.09628302961871792,
        "quantile_99": 0.06734356708759937,
        "hill_tail_index": 2.6084542373686506
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023179389036192013,
        "excess_kurtosis": 10.484293320448614,
        "return_acf_1": -0.22222980741976195,
        "abs_return_acf_1": 0.4166908502498747,
        "abs_return_acf_5": 0.4046768508314889,
        "abs_return_acf_20": 0.34385160224831707,
        "quantile_01": -0.07717337766243325,
        "quantile_99": 0.0695751123562827,
        "hill_tail_index": 3.32913891584946
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0188029359139966,
        "excess_kurtosis": 5.524690096557748,
        "return_acf_1": -0.06538074286832699,
        "abs_return_acf_1": 0.2547351875482919,
        "abs_return_acf_5": 0.2997434798331308,
        "abs_return_acf_20": 0.24611882474650706,
        "quantile_01": -0.05437694483644602,
        "quantile_99": 0.05098606687846681,
        "hill_tail_index": 3.6509357238700177
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01800039856763968,
        "excess_kurtosis": 9.580675798918895,
        "return_acf_1": -0.15762243612463273,
        "abs_return_acf_1": 0.31802701201374894,
        "abs_return_acf_5": 0.21428237204291511,
        "abs_return_acf_20": 0.25735879005340856,
        "quantile_01": -0.05736439531196745,
        "quantile_99": 0.04926125852620684,
        "hill_tail_index": 2.645492596494879
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02484756452868524,
        "excess_kurtosis": 17.66302027306259,
        "return_acf_1": -0.22814711945976524,
        "abs_return_acf_1": 0.4227397857442886,
        "abs_return_acf_5": 0.38392530405406117,
        "abs_return_acf_20": 0.36479687850204856,
        "quantile_01": -0.09453477206498134,
        "quantile_99": 0.061638799871789954,
        "hill_tail_index": 2.4602118127221333
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02310709325394034,
        "excess_kurtosis": 8.926669788362936,
        "return_acf_1": -0.1448288636904593,
        "abs_return_acf_1": 0.3985600964349962,
        "abs_return_acf_5": 0.4036692348516316,
        "abs_return_acf_20": 0.3226928422501482,
        "quantile_01": -0.08163410306591531,
        "quantile_99": 0.07462047392579786,
        "hill_tail_index": 3.3487869987959855
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019172043608653752,
        "excess_kurtosis": 6.170789879606737,
        "return_acf_1": -0.18168966246325768,
        "abs_return_acf_1": 0.4275405995047126,
        "abs_return_acf_5": 0.3970665086755845,
        "abs_return_acf_20": 0.35983383112332795,
        "quantile_01": -0.0627498273147796,
        "quantile_99": 0.056333158111958714,
        "hill_tail_index": 3.3865248812039
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.024098467059500746,
        "excess_kurtosis": 12.85732332553883,
        "return_acf_1": -0.15903485064148526,
        "abs_return_acf_1": 0.3461976137735413,
        "abs_return_acf_5": 0.397168704451379,
        "abs_return_acf_20": 0.34112130916070715,
        "quantile_01": -0.08641873364152663,
        "quantile_99": 0.06471112669853082,
        "hill_tail_index": 2.783761899216741
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022892056188979777,
        "excess_kurtosis": 10.7489195028694,
        "return_acf_1": -0.1645055662012505,
        "abs_return_acf_1": 0.36156946419218844,
        "abs_return_acf_5": 0.4195615015024493,
        "abs_return_acf_20": 0.3237031073338464,
        "quantile_01": -0.08908510003456516,
        "quantile_99": 0.06926673981254758,
        "hill_tail_index": 3.173409932775915
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022111358980452803,
        "excess_kurtosis": 9.856367955468174,
        "return_acf_1": -0.19688398627346596,
        "abs_return_acf_1": 0.3718990392978095,
        "abs_return_acf_5": 0.46792927968091647,
        "abs_return_acf_20": 0.3098535627678993,
        "quantile_01": -0.07576030228314963,
        "quantile_99": 0.0570192617800292,
        "hill_tail_index": 3.1307861728392634
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016797397089023277,
        "excess_kurtosis": 4.154135262195631,
        "return_acf_1": -0.12323092198435621,
        "abs_return_acf_1": 0.20129892144039538,
        "abs_return_acf_5": 0.2279025916925367,
        "abs_return_acf_20": 0.21153137368803396,
        "quantile_01": -0.044423475892826615,
        "quantile_99": 0.04826109861027957,
        "hill_tail_index": 3.488757989308654
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020019615663408753,
        "excess_kurtosis": 5.008519701495636,
        "return_acf_1": -0.2160895067597909,
        "abs_return_acf_1": 0.3721279212600701,
        "abs_return_acf_5": 0.3116442470975203,
        "abs_return_acf_20": 0.2861874753374699,
        "quantile_01": -0.05789579238207393,
        "quantile_99": 0.052714613035108236,
        "hill_tail_index": 3.6832475358227477
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022331034622945858,
        "excess_kurtosis": 13.038236775733246,
        "return_acf_1": -0.15107530765898602,
        "abs_return_acf_1": 0.41246014162975364,
        "abs_return_acf_5": 0.45789679119833415,
        "abs_return_acf_20": 0.35581118282670493,
        "quantile_01": -0.07669893182769402,
        "quantile_99": 0.0678715508870067,
        "hill_tail_index": 2.5752921899223327
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019193235142065345,
        "excess_kurtosis": 7.255723255353441,
        "return_acf_1": -0.17659686390330373,
        "abs_return_acf_1": 0.34686137720780874,
        "abs_return_acf_5": 0.4015259578938804,
        "abs_return_acf_20": 0.3255228650190883,
        "quantile_01": -0.060615082850332416,
        "quantile_99": 0.05177362467853529,
        "hill_tail_index": 3.157939052308465
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02527533666601647,
        "excess_kurtosis": 10.829123774990592,
        "return_acf_1": -0.2223644663744038,
        "abs_return_acf_1": 0.4377486242717993,
        "abs_return_acf_5": 0.43260043497614825,
        "abs_return_acf_20": 0.382482470094882,
        "quantile_01": -0.09235280840493326,
        "quantile_99": 0.0747061920596269,
        "hill_tail_index": 3.52046361700084
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019607827459581225,
        "excess_kurtosis": 5.826736792776991,
        "return_acf_1": -0.20628937421354507,
        "abs_return_acf_1": 0.33065002470339266,
        "abs_return_acf_5": 0.385539695235962,
        "abs_return_acf_20": 0.30814322077968204,
        "quantile_01": -0.05998790775354408,
        "quantile_99": 0.06464706663736458,
        "hill_tail_index": 3.5363115773039664
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01954514220199053,
        "excess_kurtosis": 6.862884617637926,
        "return_acf_1": -0.20508249673897816,
        "abs_return_acf_1": 0.30670876854703605,
        "abs_return_acf_5": 0.29381571309495214,
        "abs_return_acf_20": 0.2637397561299869,
        "quantile_01": -0.06455378039813754,
        "quantile_99": 0.054262159070538385,
        "hill_tail_index": 3.4521098886312314
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01849477702069691,
        "excess_kurtosis": 7.133452452927596,
        "return_acf_1": -0.01187401326880199,
        "abs_return_acf_1": 0.29111980159961015,
        "abs_return_acf_5": 0.35315317309854466,
        "abs_return_acf_20": 0.2741346674965475,
        "quantile_01": -0.05162280447139736,
        "quantile_99": 0.05384919712666554,
        "hill_tail_index": 3.544326931357351
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022788028969926804,
        "excess_kurtosis": 12.767416815394727,
        "return_acf_1": -0.18870124570741942,
        "abs_return_acf_1": 0.4066045361892804,
        "abs_return_acf_5": 0.4079000101163737,
        "abs_return_acf_20": 0.330194750155779,
        "quantile_01": -0.08286729075547983,
        "quantile_99": 0.06375405716826166,
        "hill_tail_index": 3.4550918885922495
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021933682168150757,
        "excess_kurtosis": 10.248154025578188,
        "return_acf_1": -0.18926961137335707,
        "abs_return_acf_1": 0.44198927093927887,
        "abs_return_acf_5": 0.4415747496015862,
        "abs_return_acf_20": 0.34628358292999295,
        "quantile_01": -0.07831182413471749,
        "quantile_99": 0.05836313093464739,
        "hill_tail_index": 2.936893763602112
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02210610698344405,
        "excess_kurtosis": 13.55762632773769,
        "return_acf_1": -0.21535918427126657,
        "abs_return_acf_1": 0.4531591077596644,
        "abs_return_acf_5": 0.43827710923468816,
        "abs_return_acf_20": 0.3439690217765183,
        "quantile_01": -0.08105085432474433,
        "quantile_99": 0.061669924678714794,
        "hill_tail_index": 3.0396459207478514
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.023050565702428114,
        "excess_kurtosis": 13.284025694992792,
        "return_acf_1": -0.17504842513620122,
        "abs_return_acf_1": 0.3583098400435792,
        "abs_return_acf_5": 0.42540223720570564,
        "abs_return_acf_20": 0.2597591605276068,
        "quantile_01": -0.08504560055419896,
        "quantile_99": 0.05344143802528575,
        "hill_tail_index": 2.346123273846189
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02296369682853535,
        "excess_kurtosis": 12.602120976154202,
        "return_acf_1": -0.22479943422453316,
        "abs_return_acf_1": 0.3932730075988257,
        "abs_return_acf_5": 0.3911897550350836,
        "abs_return_acf_20": 0.38412290061639404,
        "quantile_01": -0.08192223649252695,
        "quantile_99": 0.05754016482371121,
        "hill_tail_index": 2.7087744724589062
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02186850022102614,
        "excess_kurtosis": 8.740822027922347,
        "return_acf_1": -0.16882877818882008,
        "abs_return_acf_1": 0.3846144706163827,
        "abs_return_acf_5": 0.43325623546165076,
        "abs_return_acf_20": 0.37359916023410494,
        "quantile_01": -0.07885582823630852,
        "quantile_99": 0.06876623469986776,
        "hill_tail_index": 3.824967679667456
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01718256820926243,
        "excess_kurtosis": 6.021066398107077,
        "return_acf_1": -0.17686426081750992,
        "abs_return_acf_1": 0.2609115776564696,
        "abs_return_acf_5": 0.3053130932420401,
        "abs_return_acf_20": 0.2539748404568586,
        "quantile_01": -0.04662163483102152,
        "quantile_99": 0.05136134018463289,
        "hill_tail_index": 3.6461651532718435
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018994073467481616,
        "excess_kurtosis": 16.373619404407833,
        "return_acf_1": -0.1385459088490309,
        "abs_return_acf_1": 0.30186022027446247,
        "abs_return_acf_5": 0.2689245038490559,
        "abs_return_acf_20": 0.3090529959562131,
        "quantile_01": -0.05875826858949564,
        "quantile_99": 0.04144653564785816,
        "hill_tail_index": 2.334602243232047
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
