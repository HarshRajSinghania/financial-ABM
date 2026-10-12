# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27120
Run ID: `675b8fad8edb7fbff96d03124ff607d435f4521ec68003921e80712d74d18144`
Result fingerprint: `d1dc8bd199bff9534b7420cd3a553348fef22542eb119a90dd988ba1790f05ff`

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
    "equal_weight_sd": -0.643880952380949,
    "equal_weight_raw": -9.658214285714239,
    "fixed_start_cap_weight_sd": -0.6519380084574595,
    "fixed_start_cap_weight_raw": -9.77907012686189,
    "end_cap_weight_sd": -0.6598648189525643,
    "end_cap_weight_raw": -9.897972284288468
  },
  "full_period_change": {
    "equal_weight_sd": -1.0297380952380903,
    "equal_weight_raw": -15.446071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9699990079365034,
    "inflation_mean_sd": 0.7332632275132277
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.30850000000000316,
    "equal_weight_raw": 4.627500000000047,
    "fixed_start_cap_weight_sd": 0.30044294392349274,
    "fixed_start_cap_weight_raw": 4.506644158852391,
    "end_cap_weight_sd": 0.2925161334283878,
    "end_cap_weight_raw": 4.387742001425817
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7490476190476157,
      "change_raw": -11.235714285714236,
      "decay_adjusted_gain_sd": 0.20333333333333659
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6018253968253936,
      "change_raw": -9.027380952380904,
      "decay_adjusted_gain_sd": 0.3505555555555587
    },
    "small": {
      "count": 18,
      "change_sd": -0.6473809523809491,
      "change_raw": -9.710714285714236,
      "decay_adjusted_gain_sd": 0.3050000000000032
    },
    "large_minus_small_sd": -0.10166666666666668,
    "large_minus_small_raw": -1.5250000000000004
  },
  "inflation": {
    "initial_mean_sd": 0.3644166666666668,
    "final_mean_sd": 0.7914166666666668,
    "mean_sd": 0.5710544684984735,
    "mean_absolute_raw_gap": 8.565817027477102,
    "final_absolute_raw_gap": 11.871250000000002,
    "mean_range_fraction": 0.08565817027477102
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.30520543816152806,
    "final_wealth_share": 0.3664260670236685
  },
  "pricing_slope": {
    "mean": -0.002057305842663886,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.10406043473471946,
    "real_improvement_cost": 0.08269587413493634,
    "washing_cost": 0.021364560599783127,
    "fine_transfer": 0.01988026916308521,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12394070389780468,
    "resource_cost_fraction_initial_cap": 0.0034686811578239825,
    "private_net_outflow_fraction_initial_cap": 0.00413135679659349,
    "fine_transfer_fraction_initial_cap": 0.0006626756387695071,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0022449676679804948,
    "unapplied_final_day_resource_cost": 0.0019558026217925484
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 88.9387020493793,
    "beneficial_raw_gain_per_resource_cost": 1334.0805307406895,
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
    "accrued_cost": 3.074139782267608,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.0979493060771316,
    "accrued_cost_fraction_initial_cap": 0.10247132607558695,
    "mean_contract_rate": 0.04268023829536672,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "maximum_relative_cash_error": 2.440296036262504e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.2199502493919116,
      "maximum": -0.03199669332234996,
      "mean": -0.14804579249944097,
      "median": -0.1545999059242484,
      "quantile_05": -0.2118952974919737,
      "quantile_95": -0.09642991287905357
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
      "minimum": 0.3572075893851799,
      "maximum": 0.8361071325352156,
      "mean": 0.56291291032601,
      "median": 0.5219359498587485,
      "quantile_05": 0.39247787277374047,
      "quantile_95": 0.78116338242179
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
        "daily_volatility": 0.016699266909308376,
        "excess_kurtosis": 2.39625280559932,
        "return_acf_1": -0.15419840293210432,
        "abs_return_acf_1": 0.2730924164294164,
        "abs_return_acf_5": 0.26284380564520204,
        "abs_return_acf_20": 0.15992145610292047,
        "quantile_01": -0.04565686646855266,
        "quantile_99": 0.043608398914097686,
        "hill_tail_index": 4.779197385381952
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02296356272364158,
        "excess_kurtosis": 16.967056504449758,
        "return_acf_1": -0.09669936154019061,
        "abs_return_acf_1": 0.4102383295926964,
        "abs_return_acf_5": 0.3222456542315759,
        "abs_return_acf_20": 0.33313491404067636,
        "quantile_01": -0.08510535561722851,
        "quantile_99": 0.07050288939854073,
        "hill_tail_index": 2.585918691378462
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020025997069836533,
        "excess_kurtosis": 18.814140656077875,
        "return_acf_1": -0.18770310401402296,
        "abs_return_acf_1": 0.36504701309146054,
        "abs_return_acf_5": 0.30067805075798376,
        "abs_return_acf_20": 0.26994505459847873,
        "quantile_01": -0.06004565620139257,
        "quantile_99": 0.04562309038911029,
        "hill_tail_index": 2.493442675503245
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021850926447734367,
        "excess_kurtosis": 14.4403657105909,
        "return_acf_1": -0.16953041022880336,
        "abs_return_acf_1": 0.438511192721346,
        "abs_return_acf_5": 0.31567933386989167,
        "abs_return_acf_20": 0.25422065887972745,
        "quantile_01": -0.06284475263001259,
        "quantile_99": 0.06225147667730534,
        "hill_tail_index": 2.1358353798132828
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02170736024489182,
        "excess_kurtosis": 13.73345346351902,
        "return_acf_1": -0.09884798097374763,
        "abs_return_acf_1": 0.45231704790131294,
        "abs_return_acf_5": 0.3548361581554672,
        "abs_return_acf_20": 0.24946657358424779,
        "quantile_01": -0.08572703426262032,
        "quantile_99": 0.0669325033781773,
        "hill_tail_index": 3.1661918534596487
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018466877889590293,
        "excess_kurtosis": 6.0372344298387635,
        "return_acf_1": -0.17423092370953872,
        "abs_return_acf_1": 0.38738158900710684,
        "abs_return_acf_5": 0.3629824530548031,
        "abs_return_acf_20": 0.2994980604402534,
        "quantile_01": -0.05465259533619927,
        "quantile_99": 0.04995485633593608,
        "hill_tail_index": 3.0595944876041474
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018064083446976114,
        "excess_kurtosis": 3.7734050872981504,
        "return_acf_1": -0.09620945488357782,
        "abs_return_acf_1": 0.2855741690474447,
        "abs_return_acf_5": 0.27819607657073037,
        "abs_return_acf_20": 0.23428217084585817,
        "quantile_01": -0.05611611211236838,
        "quantile_99": 0.05104490273197664,
        "hill_tail_index": 4.561318572467221
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022310050452857475,
        "excess_kurtosis": 14.455311009306318,
        "return_acf_1": -0.14128573929428787,
        "abs_return_acf_1": 0.44639128124784405,
        "abs_return_acf_5": 0.34289845627708093,
        "abs_return_acf_20": 0.30009752544475626,
        "quantile_01": -0.07497913058309555,
        "quantile_99": 0.05963762402129261,
        "hill_tail_index": 2.3600253678433982
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017459262286451685,
        "excess_kurtosis": 10.12415834192463,
        "return_acf_1": -0.20998133821446993,
        "abs_return_acf_1": 0.3800590467659307,
        "abs_return_acf_5": 0.32965367859378636,
        "abs_return_acf_20": 0.26810081170845307,
        "quantile_01": -0.05548191915088509,
        "quantile_99": 0.05066920118410604,
        "hill_tail_index": 3.99180496490133
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0177053455701802,
        "excess_kurtosis": 2.8511965559240995,
        "return_acf_1": -0.1550014089163925,
        "abs_return_acf_1": 0.35639974989374285,
        "abs_return_acf_5": 0.3266793835587602,
        "abs_return_acf_20": 0.261788416592584,
        "quantile_01": -0.052473664597518475,
        "quantile_99": 0.05052306166444699,
        "hill_tail_index": 3.8372820969676646
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02213624219044383,
        "excess_kurtosis": 12.81048213827651,
        "return_acf_1": -0.1702467374379483,
        "abs_return_acf_1": 0.4284944903247209,
        "abs_return_acf_5": 0.347171590197183,
        "abs_return_acf_20": 0.30150122774809357,
        "quantile_01": -0.08192116463749537,
        "quantile_99": 0.06747559674309621,
        "hill_tail_index": 3.509374805149844
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01799554327516477,
        "excess_kurtosis": 4.417750003198501,
        "return_acf_1": -0.1910028581459552,
        "abs_return_acf_1": 0.3022742437948034,
        "abs_return_acf_5": 0.35955687961435207,
        "abs_return_acf_20": 0.17968142587430505,
        "quantile_01": -0.056123352072345506,
        "quantile_99": 0.05131436870266122,
        "hill_tail_index": 3.831621625522074
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.015706311098448708,
        "excess_kurtosis": 3.629630263661981,
        "return_acf_1": -0.18009981093173166,
        "abs_return_acf_1": 0.2514674180764478,
        "abs_return_acf_5": 0.2720434411264303,
        "abs_return_acf_20": 0.20497829495259298,
        "quantile_01": -0.04577585653442216,
        "quantile_99": 0.041924287967500355,
        "hill_tail_index": 4.086878814208593
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.027528883977476236,
        "excess_kurtosis": 19.407186460100142,
        "return_acf_1": -0.11661939926067551,
        "abs_return_acf_1": 0.5127212824903742,
        "abs_return_acf_5": 0.4099643192376127,
        "abs_return_acf_20": 0.30262009109738675,
        "quantile_01": -0.11061477377375147,
        "quantile_99": 0.095000791752884,
        "hill_tail_index": 2.7147838620376588
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020089519543117662,
        "excess_kurtosis": 8.096361488725146,
        "return_acf_1": -0.1252578598667584,
        "abs_return_acf_1": 0.2723297669279175,
        "abs_return_acf_5": 0.32155453066417594,
        "abs_return_acf_20": 0.2088371031347381,
        "quantile_01": -0.0576302990030927,
        "quantile_99": 0.0598962136147622,
        "hill_tail_index": 2.7428670168780385
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.025172281320733902,
        "excess_kurtosis": 10.79296104686481,
        "return_acf_1": -0.10697641572445019,
        "abs_return_acf_1": 0.4957495341208712,
        "abs_return_acf_5": 0.4040933371061177,
        "abs_return_acf_20": 0.3514770090492024,
        "quantile_01": -0.09510462505616953,
        "quantile_99": 0.08527009511108526,
        "hill_tail_index": 3.5656720468486607
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02399148351038464,
        "excess_kurtosis": 16.93654308292926,
        "return_acf_1": -0.03199669332234996,
        "abs_return_acf_1": 0.49655541467203085,
        "abs_return_acf_5": 0.41332775542537226,
        "abs_return_acf_20": 0.29395150349008436,
        "quantile_01": -0.1103431215938706,
        "quantile_99": 0.06989704347870215,
        "hill_tail_index": 2.199847900011412
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018234179324479745,
        "excess_kurtosis": 5.005270099975382,
        "return_acf_1": -0.2199502493919116,
        "abs_return_acf_1": 0.397237189737298,
        "abs_return_acf_5": 0.32745418979133994,
        "abs_return_acf_20": 0.2327739036567212,
        "quantile_01": -0.05804492621652313,
        "quantile_99": 0.05038033043109404,
        "hill_tail_index": 4.228928519497561
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018511099519948913,
        "excess_kurtosis": 7.971847799614729,
        "return_acf_1": -0.2018293446155419,
        "abs_return_acf_1": 0.4234560586333354,
        "abs_return_acf_5": 0.28741426572565304,
        "abs_return_acf_20": 0.297379698815108,
        "quantile_01": -0.046171525594535856,
        "quantile_99": 0.05224169732977885,
        "hill_tail_index": 2.973378437628839
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017505251623704466,
        "excess_kurtosis": 2.935062408347979,
        "return_acf_1": -0.1884685050319853,
        "abs_return_acf_1": 0.33490803175352624,
        "abs_return_acf_5": 0.3181870030393588,
        "abs_return_acf_20": 0.23146804206173302,
        "quantile_01": -0.051430382265510007,
        "quantile_99": 0.043409104095116606,
        "hill_tail_index": 3.9729786757709014
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02125640238091682,
        "excess_kurtosis": 11.777719281968706,
        "return_acf_1": -0.10733734116850228,
        "abs_return_acf_1": 0.36789570936117194,
        "abs_return_acf_5": 0.35299264554349796,
        "abs_return_acf_20": 0.22076879274685718,
        "quantile_01": -0.07827572807901964,
        "quantile_99": 0.0590784531518972,
        "hill_tail_index": 2.7965717331942175
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0228666822353026,
        "excess_kurtosis": 14.84874314432108,
        "return_acf_1": -0.16028778626435564,
        "abs_return_acf_1": 0.45923064658101387,
        "abs_return_acf_5": 0.3617369486348634,
        "abs_return_acf_20": 0.2803224479011603,
        "quantile_01": -0.07744084379261411,
        "quantile_99": 0.062347811968275865,
        "hill_tail_index": 2.279738290341047
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.016791461760376592,
        "excess_kurtosis": 3.828057599801027,
        "return_acf_1": -0.1750804482778836,
        "abs_return_acf_1": 0.3297190563336618,
        "abs_return_acf_5": 0.24257949205807836,
        "abs_return_acf_20": 0.22114700170779705,
        "quantile_01": -0.046983013581361095,
        "quantile_99": 0.0423116659147491,
        "hill_tail_index": 3.7256633886822548
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01796750528873135,
        "excess_kurtosis": 2.873901688129907,
        "return_acf_1": -0.11424549852332841,
        "abs_return_acf_1": 0.2839392774136649,
        "abs_return_acf_5": 0.2760451445217736,
        "abs_return_acf_20": 0.2216217041031477,
        "quantile_01": -0.05046738086476684,
        "quantile_99": 0.05242938959556684,
        "hill_tail_index": 5.3041615695187385
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02251482878896915,
        "excess_kurtosis": 18.48176397922997,
        "return_acf_1": -0.2134612641735677,
        "abs_return_acf_1": 0.46685507215778993,
        "abs_return_acf_5": 0.38858700562313736,
        "abs_return_acf_20": 0.2723263632073748,
        "quantile_01": -0.0762309023349763,
        "quantile_99": 0.05773392810288567,
        "hill_tail_index": 2.9365932879559065
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01709994660285783,
        "excess_kurtosis": 4.017572138477021,
        "return_acf_1": -0.100247426595503,
        "abs_return_acf_1": 0.20807748386724223,
        "abs_return_acf_5": 0.22065937802017943,
        "abs_return_acf_20": 0.14767671506373783,
        "quantile_01": -0.04844535305039693,
        "quantile_99": 0.044338468969951306,
        "hill_tail_index": 3.1441451691614275
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02139963878633192,
        "excess_kurtosis": 10.006374474073455,
        "return_acf_1": -0.1274669216440334,
        "abs_return_acf_1": 0.4204985946681231,
        "abs_return_acf_5": 0.4005689416706375,
        "abs_return_acf_20": 0.29400862993484395,
        "quantile_01": -0.0833184096633464,
        "quantile_99": 0.06046466756509557,
        "hill_tail_index": 2.9404217331091007
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.021207225831076534,
        "excess_kurtosis": 11.09134202938191,
        "return_acf_1": -0.17102687658303387,
        "abs_return_acf_1": 0.41019239847368755,
        "abs_return_acf_5": 0.3068985057642036,
        "abs_return_acf_20": 0.32006980169390303,
        "quantile_01": -0.07113388948531525,
        "quantile_99": 0.05819172237502494,
        "hill_tail_index": 2.633891628577929
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01723249680075781,
        "excess_kurtosis": 4.473199669901633,
        "return_acf_1": -0.14841625150852733,
        "abs_return_acf_1": 0.27916809939257303,
        "abs_return_acf_5": 0.22543623491213943,
        "abs_return_acf_20": 0.22390805107531475,
        "quantile_01": -0.05068954389331381,
        "quantile_99": 0.043289484942457476,
        "hill_tail_index": 3.8428097958408376
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020393001856160005,
        "excess_kurtosis": 9.157062116053641,
        "return_acf_1": -0.10766796180805024,
        "abs_return_acf_1": 0.3192449869666325,
        "abs_return_acf_5": 0.27341657437600086,
        "abs_return_acf_20": 0.25451197061455394,
        "quantile_01": -0.05919236726076412,
        "quantile_99": 0.05657176101584192,
        "hill_tail_index": 2.8104224493669
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
