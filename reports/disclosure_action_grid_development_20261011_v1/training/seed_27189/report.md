# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27189
Run ID: `a0a4cb477df6871c021086821294e338fb0dba3f708844f4e806c4629e13d76d`
Result fingerprint: `caf1a40ed6759bdd1013f1357cb785ce3f128ef810a389372a05c9396252784d`

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
    "equal_weight_sd": -0.7522880460228819,
    "equal_weight_raw": -11.28432069034323,
    "fixed_start_cap_weight_sd": -0.7378129643316271,
    "fixed_start_cap_weight_raw": -11.067194464974406,
    "end_cap_weight_sd": -0.7597017699547025,
    "end_cap_weight_raw": -11.39552654932054
  },
  "full_period_change": {
    "equal_weight_sd": -1.13931185554669,
    "equal_weight_raw": -17.089677833200348
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0707108547176376,
    "inflation_mean_sd": 0.6496808862433862
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19108333333333632,
    "equal_weight_raw": 2.8662500000000453,
    "fixed_start_cap_weight_sd": 0.20766390217057284,
    "fixed_start_cap_weight_raw": 3.114958532558592,
    "end_cap_weight_sd": 0.185322590517529,
    "end_cap_weight_raw": 2.7798388577629343
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6282142857142827,
      "change_raw": -9.423214285714241,
      "decay_adjusted_gain_sd": 0.32416666666666955
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8048809523809493,
      "change_raw": -12.073214285714238,
      "decay_adjusted_gain_sd": 0.14750000000000313
    },
    "small": {
      "count": 18,
      "change_sd": -0.7466705528952816,
      "change_raw": -11.200058293429224,
      "decay_adjusted_gain_sd": 0.19069444444444744
    },
    "large_minus_small_sd": 0.11845626718099889,
    "large_minus_small_raw": 1.7768440077149834
  },
  "inflation": {
    "initial_mean_sd": 0.26525000000000004,
    "final_mean_sd": 0.6681666666666668,
    "mean_sd": 0.4859227033028032,
    "mean_absolute_raw_gap": 7.288840549542048,
    "final_absolute_raw_gap": 10.0225,
    "mean_range_fraction": 0.07288840549542047
  },
  "impact": {
    "initial_share": 0.36,
    "final_share": 0.41333333333333333,
    "initial_wealth_share": 0.33128092752939087,
    "final_wealth_share": 0.3995014059331324
  },
  "pricing_slope": {
    "mean": -0.0038675034561918716,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.15203275655780268,
    "real_improvement_cost": 0.1077921970938117,
    "washing_cost": 0.044240559463990976,
    "fine_transfer": 0.014632571592579679,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.16666532815038237,
    "resource_cost_fraction_initial_cap": 0.005067758551926756,
    "private_net_outflow_fraction_initial_cap": 0.005555510938346079,
    "fine_transfer_fraction_initial_cap": 0.00048775238641932263,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00925340337278497,
    "unapplied_final_day_resource_cost": 0.0011441406385215302
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 37.70569007489251,
    "beneficial_raw_gain_per_resource_cost": 565.5853511233877,
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
    "accrued_cost": 3.2171634285920203,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.24097295240154376,
    "accrued_cost_fraction_initial_cap": 0.10723878095306734,
    "mean_contract_rate": 0.04451366810891468,
    "maximum_ledger_error": 9.486769009248164e-20
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
    "price_cap_hits": 6,
    "maximum_relative_cash_error": 1.0029141631394132e-15,
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
      "minimum": -0.20009430274295595,
      "maximum": -0.05693433019452011,
      "mean": -0.1383322698907963,
      "median": -0.13656209064945668,
      "quantile_05": -0.19234920301903938,
      "quantile_95": -0.07643716336384763
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
      "minimum": 0.21078978123312447,
      "maximum": 0.8583059398310351,
      "mean": 0.7168629651279914,
      "median": 0.7624838353824297,
      "quantile_05": 0.34591987997691886,
      "quantile_95": 0.8357354831926306
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
        "daily_volatility": 0.02805011821300705,
        "excess_kurtosis": 18.21435077785835,
        "return_acf_1": -0.09033826438013522,
        "abs_return_acf_1": 0.4637918787127392,
        "abs_return_acf_5": 0.4550101354903997,
        "abs_return_acf_20": 0.3610764794583437,
        "quantile_01": -0.10089677516798128,
        "quantile_99": 0.09002543866914267,
        "hill_tail_index": 2.5634822776932005
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02184002293890745,
        "excess_kurtosis": 9.980653126650065,
        "return_acf_1": -0.15121625889130166,
        "abs_return_acf_1": 0.3108343936766337,
        "abs_return_acf_5": 0.34695774816286257,
        "abs_return_acf_20": 0.29516560322568464,
        "quantile_01": -0.06769719094743298,
        "quantile_99": 0.06623701160138405,
        "hill_tail_index": 3.489881806956582
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02329555645960833,
        "excess_kurtosis": 13.374593910256667,
        "return_acf_1": -0.11960568491739644,
        "abs_return_acf_1": 0.35978047002393687,
        "abs_return_acf_5": 0.39843425799499,
        "abs_return_acf_20": 0.2501098145761065,
        "quantile_01": -0.07281696262082228,
        "quantile_99": 0.06706571475346992,
        "hill_tail_index": 2.7313712083510335
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.026753391638532076,
        "excess_kurtosis": 18.897768219172576,
        "return_acf_1": -0.05693433019452011,
        "abs_return_acf_1": 0.49569199851440154,
        "abs_return_acf_5": 0.4289500148172588,
        "abs_return_acf_20": 0.32100923001099124,
        "quantile_01": -0.07017376863562284,
        "quantile_99": 0.08357311115323938,
        "hill_tail_index": 2.5479860046658347
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02587434444553755,
        "excess_kurtosis": 24.02401587952479,
        "return_acf_1": -0.07392499020434701,
        "abs_return_acf_1": 0.35561465599365266,
        "abs_return_acf_5": 0.3459173676669454,
        "abs_return_acf_20": 0.27369579546091766,
        "quantile_01": -0.09232349685499798,
        "quantile_99": 0.06816318818509035,
        "hill_tail_index": 2.1584989305251825
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.025857030977746942,
        "excess_kurtosis": 18.106229021632224,
        "return_acf_1": -0.11712603232161085,
        "abs_return_acf_1": 0.3710758939790794,
        "abs_return_acf_5": 0.39674371507187445,
        "abs_return_acf_20": 0.2721820782592768,
        "quantile_01": -0.08844022321054415,
        "quantile_99": 0.07639950000576345,
        "hill_tail_index": 2.443726403883924
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.024056584383297212,
        "excess_kurtosis": 15.664108125721203,
        "return_acf_1": -0.13602405297041387,
        "abs_return_acf_1": 0.33221508299455943,
        "abs_return_acf_5": 0.42701154460472757,
        "abs_return_acf_20": 0.24826567142926553,
        "quantile_01": -0.07690587276908058,
        "quantile_99": 0.07054115368402947,
        "hill_tail_index": 2.764958093756712
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.026462078304830893,
        "excess_kurtosis": 16.46294739667003,
        "return_acf_1": -0.16138080309827174,
        "abs_return_acf_1": 0.4555743045328212,
        "abs_return_acf_5": 0.45069141119645567,
        "abs_return_acf_20": 0.3456271817167173,
        "quantile_01": -0.09961046981517563,
        "quantile_99": 0.08101156458918422,
        "hill_tail_index": 2.9750576052860285
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02603574286591999,
        "excess_kurtosis": 24.146032067118764,
        "return_acf_1": -0.14229240490563508,
        "abs_return_acf_1": 0.39065874841489795,
        "abs_return_acf_5": 0.43933892296238397,
        "abs_return_acf_20": 0.27717055864321993,
        "quantile_01": -0.09087912257292706,
        "quantile_99": 0.06665897837136509,
        "hill_tail_index": 2.2893672329082473
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.027025210596432744,
        "excess_kurtosis": 16.813272510863193,
        "return_acf_1": -0.13436703186607035,
        "abs_return_acf_1": 0.46066608906857814,
        "abs_return_acf_5": 0.4839600055106021,
        "abs_return_acf_20": 0.33846078740309454,
        "quantile_01": -0.095819481868789,
        "quantile_99": 0.09126476918492715,
        "hill_tail_index": 3.324984845363174
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.023187229694556444,
        "excess_kurtosis": 12.087912236750217,
        "return_acf_1": -0.18143332694349243,
        "abs_return_acf_1": 0.385363800648344,
        "abs_return_acf_5": 0.4445791016494037,
        "abs_return_acf_20": 0.32682331117763014,
        "quantile_01": -0.07733122284008205,
        "quantile_99": 0.06675854800327193,
        "hill_tail_index": 2.884931224742016
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.026349261856591574,
        "excess_kurtosis": 13.955947383587052,
        "return_acf_1": -0.10624175625850801,
        "abs_return_acf_1": 0.3937086894907299,
        "abs_return_acf_5": 0.5251106726195546,
        "abs_return_acf_20": 0.3417978051573643,
        "quantile_01": -0.09721258118527273,
        "quantile_99": 0.08271311974720257,
        "hill_tail_index": 3.586962379733927
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.024699644182786425,
        "excess_kurtosis": 14.506487702657285,
        "return_acf_1": -0.16598105879786895,
        "abs_return_acf_1": 0.3683829072901561,
        "abs_return_acf_5": 0.42447692800036857,
        "abs_return_acf_20": 0.356266034022644,
        "quantile_01": -0.08543168322389585,
        "quantile_99": 0.08011234906165905,
        "hill_tail_index": 3.180386642307833
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.025227453531005115,
        "excess_kurtosis": 14.929581234844616,
        "return_acf_1": -0.13304443159269203,
        "abs_return_acf_1": 0.42836964767037117,
        "abs_return_acf_5": 0.43232499702684163,
        "abs_return_acf_20": 0.30475628134573324,
        "quantile_01": -0.0899093747049249,
        "quantile_99": 0.0689988191809441,
        "hill_tail_index": 2.8451237738451987
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024771045079392696,
        "excess_kurtosis": 13.490450079786203,
        "return_acf_1": -0.13156608720697652,
        "abs_return_acf_1": 0.37293543147652575,
        "abs_return_acf_5": 0.4100407185751588,
        "abs_return_acf_20": 0.2416324078107262,
        "quantile_01": -0.08747896667247165,
        "quantile_99": 0.06985933925481647,
        "hill_tail_index": 2.7345802817722817
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02624780819103941,
        "excess_kurtosis": 16.14499547852524,
        "return_acf_1": -0.14799369347694663,
        "abs_return_acf_1": 0.4066404263265351,
        "abs_return_acf_5": 0.4041989179109218,
        "abs_return_acf_20": 0.333985591212011,
        "quantile_01": -0.08557201480524,
        "quantile_99": 0.09037080613474703,
        "hill_tail_index": 3.0911603704971515
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.024113199017392135,
        "excess_kurtosis": 14.518397556726853,
        "return_acf_1": -0.17674758654407813,
        "abs_return_acf_1": 0.3571062937866754,
        "abs_return_acf_5": 0.3841078774497878,
        "abs_return_acf_20": 0.2773116108634101,
        "quantile_01": -0.08240870402637367,
        "quantile_99": 0.07267948789090978,
        "hill_tail_index": 2.6352369102676323
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.026317995466903298,
        "excess_kurtosis": 15.236966706492073,
        "return_acf_1": -0.20009430274295595,
        "abs_return_acf_1": 0.4538667967030443,
        "abs_return_acf_5": 0.43342269306709263,
        "abs_return_acf_20": 0.34119124895996933,
        "quantile_01": -0.09481750807639623,
        "quantile_99": 0.07276084499800216,
        "hill_tail_index": 2.5320222778576693
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.025823708156609816,
        "excess_kurtosis": 18.170780431933693,
        "return_acf_1": -0.13710012832849947,
        "abs_return_acf_1": 0.41765481137021604,
        "abs_return_acf_5": 0.4130960977157318,
        "abs_return_acf_20": 0.3432984904323657,
        "quantile_01": -0.08721000438684098,
        "quantile_99": 0.0791543103709878,
        "hill_tail_index": 2.5339702505206874
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022800703509093287,
        "excess_kurtosis": 10.619262799279346,
        "return_acf_1": -0.1503331917714405,
        "abs_return_acf_1": 0.37216527484490924,
        "abs_return_acf_5": 0.39457512157593105,
        "abs_return_acf_20": 0.3370562602510732,
        "quantile_01": -0.07544053594123394,
        "quantile_99": 0.0632115667203261,
        "hill_tail_index": 2.759379021019904
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.027061019819986185,
        "excess_kurtosis": 16.570813357844653,
        "return_acf_1": -0.18813847175427115,
        "abs_return_acf_1": 0.4485735313406846,
        "abs_return_acf_5": 0.4849810935153014,
        "abs_return_acf_20": 0.3540624459608559,
        "quantile_01": -0.09407333242683147,
        "quantile_99": 0.07951824154312989,
        "hill_tail_index": 2.5100508891631814
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02511960877058597,
        "excess_kurtosis": 15.169576950770338,
        "return_acf_1": -0.14334751774592058,
        "abs_return_acf_1": 0.4437283876101994,
        "abs_return_acf_5": 0.4406497990905824,
        "abs_return_acf_20": 0.31000660730146146,
        "quantile_01": -0.08727390621015031,
        "quantile_99": 0.06833939008117744,
        "hill_tail_index": 2.793844076879188
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02487677771509239,
        "excess_kurtosis": 15.295373408093308,
        "return_acf_1": -0.1292372778035464,
        "abs_return_acf_1": 0.3873564069864172,
        "abs_return_acf_5": 0.43849335552900176,
        "abs_return_acf_20": 0.33372886952396763,
        "quantile_01": -0.10272627340030162,
        "quantile_99": 0.06604126057379557,
        "hill_tail_index": 2.168152727828996
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02598429566695451,
        "excess_kurtosis": 18.633452030429577,
        "return_acf_1": -0.07950759722545947,
        "abs_return_acf_1": 0.39989420599943476,
        "abs_return_acf_5": 0.4083753385952949,
        "abs_return_acf_20": 0.24331358615509904,
        "quantile_01": -0.08305491368282432,
        "quantile_99": 0.06820910869604446,
        "hill_tail_index": 2.4192226874059775
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.027524737942221714,
        "excess_kurtosis": 23.195630930561883,
        "return_acf_1": -0.13333857623635587,
        "abs_return_acf_1": 0.3812528562951476,
        "abs_return_acf_5": 0.4318353653812562,
        "abs_return_acf_20": 0.23211427144799102,
        "quantile_01": -0.08994973877155218,
        "quantile_99": 0.07207217734922713,
        "hill_tail_index": 2.118194468087665
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02518862804552578,
        "excess_kurtosis": 9.484570250907085,
        "return_acf_1": -0.19579434678112248,
        "abs_return_acf_1": 0.4275949661054246,
        "abs_return_acf_5": 0.39305262059374857,
        "abs_return_acf_20": 0.3134348909688362,
        "quantile_01": -0.07751610231257931,
        "quantile_99": 0.07871894488097399,
        "hill_tail_index": 2.9414492384214648
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.027943253494590994,
        "excess_kurtosis": 20.153613977069995,
        "return_acf_1": -0.11488188931592876,
        "abs_return_acf_1": 0.4642601729943048,
        "abs_return_acf_5": 0.4251928780980602,
        "abs_return_acf_20": 0.313819750758401,
        "quantile_01": -0.09914422479931484,
        "quantile_99": 0.08185350210687592,
        "hill_tail_index": 2.9564863960480863
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02716569635094136,
        "excess_kurtosis": 16.949489813294985,
        "return_acf_1": -0.1327862562118297,
        "abs_return_acf_1": 0.38316073009864726,
        "abs_return_acf_5": 0.4740445585383185,
        "abs_return_acf_20": 0.33449735603549047,
        "quantile_01": -0.1014659103719736,
        "quantile_99": 0.07425448662815612,
        "hill_tail_index": 2.7986299866023727
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020892308738889323,
        "excess_kurtosis": 6.793239719840448,
        "return_acf_1": -0.16909786491898998,
        "abs_return_acf_1": 0.3380150035722295,
        "abs_return_acf_5": 0.39918128310589585,
        "abs_return_acf_20": 0.26605613967015185,
        "quantile_01": -0.07249215371038392,
        "quantile_99": 0.052527558771727115,
        "hill_tail_index": 3.328330465134457
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02658162559122334,
        "excess_kurtosis": 17.840603006236766,
        "return_acf_1": -0.15009288131730375,
        "abs_return_acf_1": 0.45371980133351425,
        "abs_return_acf_5": 0.42378844669764526,
        "abs_return_acf_20": 0.3078817147756149,
        "quantile_01": -0.09148942004559077,
        "quantile_99": 0.06779016960664518,
        "hill_tail_index": 2.284397344075751
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
