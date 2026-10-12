# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27244
Run ID: `a9ae1a07bcad6dd5d833c42396d2d7a254044a2ccbb6bcac0b0469e0a838d0fa`
Result fingerprint: `8428817c35a93f23dc389bb848d4a5b519256759b54e7efa199cf651e07e25b1`

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
    "equal_weight_sd": -0.833725102044433,
    "equal_weight_raw": -12.505876530666493,
    "fixed_start_cap_weight_sd": -0.7952615294445027,
    "fixed_start_cap_weight_raw": -11.928922941667542,
    "end_cap_weight_sd": -0.7952362994419554,
    "end_cap_weight_raw": -11.92854449162933
  },
  "full_period_change": {
    "equal_weight_sd": -1.2642489115682412,
    "equal_weight_raw": -18.963733673523617
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.173014902459152,
    "inflation_mean_sd": 0.39567427248677245
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.11483333333333633,
    "equal_weight_raw": 1.722500000000045,
    "fixed_start_cap_weight_sd": 0.15251140168793875,
    "fixed_start_cap_weight_raw": 2.287671025319082,
    "end_cap_weight_sd": 0.1543179563133333,
    "end_cap_weight_raw": 2.3147693447
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7357142857142831,
      "change_raw": -11.035714285714246,
      "decay_adjusted_gain_sd": 0.2166666666666693
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7813058957036725,
      "change_raw": -11.719588435555087,
      "decay_adjusted_gain_sd": 0.1583333333333361
    },
    "small": {
      "count": 18,
      "change_sd": -0.8762698412698381,
      "change_raw": -13.144047619047571,
      "decay_adjusted_gain_sd": 0.07611111111111431
    },
    "large_minus_small_sd": 0.140555555555555,
    "large_minus_small_raw": 2.108333333333325
  },
  "inflation": {
    "initial_mean_sd": 0.3105833333333333,
    "final_mean_sd": 0.39041666666666675,
    "mean_sd": 0.3731338467943381,
    "mean_absolute_raw_gap": 5.597007701915071,
    "final_absolute_raw_gap": 5.85625,
    "mean_range_fraction": 0.05597007701915071
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.15333333333333332,
    "initial_wealth_share": 0.2908346270979444,
    "final_wealth_share": 0.18864686722869187
  },
  "pricing_slope": {
    "mean": -0.0020409022574512077,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.02987940923789826,
    "real_improvement_cost": 0.02358882961903978,
    "washing_cost": 0.006290579618858479,
    "fine_transfer": 0.01647261172899492,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.046352020966893184,
    "resource_cost_fraction_initial_cap": 0.0009959803079299422,
    "private_net_outflow_fraction_initial_cap": 0.0015450673655631067,
    "fine_transfer_fraction_initial_cap": 0.0005490870576331643,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0006145779522300761,
    "unapplied_final_day_resource_cost": 0.009599878540948625
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 115.29679092953894,
    "beneficial_raw_gain_per_resource_cost": 1729.451863943084,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 2.6706925335667453,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.3054979426237308,
    "accrued_cost_fraction_initial_cap": 0.08902308445222487,
    "mean_contract_rate": 0.03717587981698234,
    "maximum_ledger_error": 3.7269449679189215e-20
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
    "maximum_relative_cash_error": 3.141198712380935e-15,
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
      "minimum": -0.17276830553114922,
      "maximum": -0.023661536639440837,
      "mean": -0.10217971402609767,
      "median": -0.09607955961595666,
      "quantile_05": -0.16229977513935726,
      "quantile_95": -0.05192581012512397
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
      "minimum": 0.2701538695386504,
      "maximum": 0.8179117212464172,
      "mean": 0.5822100014397139,
      "median": 0.6398509930748191,
      "quantile_05": 0.3119098933506955,
      "quantile_95": 0.7612457875777239
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
        "daily_volatility": 0.01656684552547304,
        "excess_kurtosis": 4.083872195858741,
        "return_acf_1": -0.08994967074657265,
        "abs_return_acf_1": 0.2139897259254895,
        "abs_return_acf_5": 0.23014731445235392,
        "abs_return_acf_20": 0.169332169228838,
        "quantile_01": -0.047398217653941546,
        "quantile_99": 0.04436142550338226,
        "hill_tail_index": 4.124251497811004
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017352389661774263,
        "excess_kurtosis": 5.349088710496112,
        "return_acf_1": -0.1358448520323217,
        "abs_return_acf_1": 0.36240983298269,
        "abs_return_acf_5": 0.32760865722243415,
        "abs_return_acf_20": 0.2077262106823493,
        "quantile_01": -0.05099107110899359,
        "quantile_99": 0.050764001113247456,
        "hill_tail_index": 3.7564224642971764
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019199098294077285,
        "excess_kurtosis": 6.60591462353503,
        "return_acf_1": -0.07455184999857352,
        "abs_return_acf_1": 0.316567434633056,
        "abs_return_acf_5": 0.3864868738840713,
        "abs_return_acf_20": 0.2873278448852191,
        "quantile_01": -0.05346183820807175,
        "quantile_99": 0.06104043254716166,
        "hill_tail_index": 3.623791960853499
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02006326863412405,
        "excess_kurtosis": 8.988689614512712,
        "return_acf_1": -0.05614172292978032,
        "abs_return_acf_1": 0.4166056966194504,
        "abs_return_acf_5": 0.4026707570036725,
        "abs_return_acf_20": 0.2670690416488068,
        "quantile_01": -0.06313373552773686,
        "quantile_99": 0.050558766553119916,
        "hill_tail_index": 3.3494370212310893
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018895676215557874,
        "excess_kurtosis": 19.0184663963502,
        "return_acf_1": -0.023661536639440837,
        "abs_return_acf_1": 0.40942900887496236,
        "abs_return_acf_5": 0.3999891566071842,
        "abs_return_acf_20": 0.18641970535524727,
        "quantile_01": -0.05584296514427795,
        "quantile_99": 0.05036781574170279,
        "hill_tail_index": 1.8916675486296677
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019055283937759907,
        "excess_kurtosis": 12.409161087590562,
        "return_acf_1": -0.08402042359787612,
        "abs_return_acf_1": 0.4238381271525529,
        "abs_return_acf_5": 0.472985657694351,
        "abs_return_acf_20": 0.27286302879290075,
        "quantile_01": -0.055035942300580336,
        "quantile_99": 0.06028949752367378,
        "hill_tail_index": 2.1069413659538783
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017959848924200366,
        "excess_kurtosis": 5.164321996089036,
        "return_acf_1": -0.08618444259594905,
        "abs_return_acf_1": 0.3492131350823829,
        "abs_return_acf_5": 0.3184894008689001,
        "abs_return_acf_20": 0.2946388376844686,
        "quantile_01": -0.05867034531313619,
        "quantile_99": 0.047553096214141374,
        "hill_tail_index": 3.1511415787544608
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.023015615994481688,
        "excess_kurtosis": 15.885907467073839,
        "return_acf_1": -0.08067712523024025,
        "abs_return_acf_1": 0.49694616177779144,
        "abs_return_acf_5": 0.5276742310483624,
        "abs_return_acf_20": 0.35426455725424283,
        "quantile_01": -0.07721833517158141,
        "quantile_99": 0.056487434049048886,
        "hill_tail_index": 2.23528071378174
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021986198859150215,
        "excess_kurtosis": 11.27181015771511,
        "return_acf_1": -0.1152089340977875,
        "abs_return_acf_1": 0.4190683784179059,
        "abs_return_acf_5": 0.3930781826718181,
        "abs_return_acf_20": 0.3476272953693498,
        "quantile_01": -0.07267177028142553,
        "quantile_99": 0.05773144335597139,
        "hill_tail_index": 2.6220691485122485
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02013680873302152,
        "excess_kurtosis": 7.009557910828297,
        "return_acf_1": -0.08702256157050745,
        "abs_return_acf_1": 0.4322518846049934,
        "abs_return_acf_5": 0.37638452328692135,
        "abs_return_acf_20": 0.31067097543713573,
        "quantile_01": -0.07731091965285654,
        "quantile_99": 0.05441683641025429,
        "hill_tail_index": 3.37889394482624
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01968401660970635,
        "excess_kurtosis": 7.273966096844665,
        "return_acf_1": -0.1035269215152206,
        "abs_return_acf_1": 0.3878634422740014,
        "abs_return_acf_5": 0.369197164898441,
        "abs_return_acf_20": 0.26032408035351007,
        "quantile_01": -0.07647174619898693,
        "quantile_99": 0.05448190581801438,
        "hill_tail_index": 3.1068135519380453
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01791653924915778,
        "excess_kurtosis": 3.994430095498984,
        "return_acf_1": -0.16538298195072948,
        "abs_return_acf_1": 0.3259411074565891,
        "abs_return_acf_5": 0.32611716933775176,
        "abs_return_acf_20": 0.26401242315735574,
        "quantile_01": -0.054434300807600526,
        "quantile_99": 0.05157511849419691,
        "hill_tail_index": 3.677982913432525
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01807886550373484,
        "excess_kurtosis": 5.8593767134003905,
        "return_acf_1": -0.11945529971311072,
        "abs_return_acf_1": 0.3003612734426483,
        "abs_return_acf_5": 0.31655950257238796,
        "abs_return_acf_20": 0.17317786381954606,
        "quantile_01": -0.05576206138959424,
        "quantile_99": 0.04605503020565783,
        "hill_tail_index": 3.8190410379072457
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01790349364163052,
        "excess_kurtosis": 6.42443937498483,
        "return_acf_1": -0.08537074235844788,
        "abs_return_acf_1": 0.34752885838602676,
        "abs_return_acf_5": 0.33911682929849435,
        "abs_return_acf_20": 0.2372498237126873,
        "quantile_01": -0.060194847358540346,
        "quantile_99": 0.04407692982241115,
        "hill_tail_index": 3.0938514874005825
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021136874286380718,
        "excess_kurtosis": 10.447819715419795,
        "return_acf_1": -0.10971926549374786,
        "abs_return_acf_1": 0.460562899130901,
        "abs_return_acf_5": 0.4820387627947635,
        "abs_return_acf_20": 0.29855756636685177,
        "quantile_01": -0.06905818304450292,
        "quantile_99": 0.053688369110456394,
        "hill_tail_index": 2.9142157698023983
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01798051770569749,
        "excess_kurtosis": 8.430963738573261,
        "return_acf_1": -0.04847642692131419,
        "abs_return_acf_1": 0.3564897064680072,
        "abs_return_acf_5": 0.38833533849579044,
        "abs_return_acf_20": 0.2044544624096618,
        "quantile_01": -0.0503897873593249,
        "quantile_99": 0.05569985098146046,
        "hill_tail_index": 2.90767507766729
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02164244777684718,
        "excess_kurtosis": 12.120660623105735,
        "return_acf_1": -0.10220944848534068,
        "abs_return_acf_1": 0.4206863820987598,
        "abs_return_acf_5": 0.4831195980207073,
        "abs_return_acf_20": 0.3224066292291084,
        "quantile_01": -0.08768497071885924,
        "quantile_99": 0.06192888795063673,
        "hill_tail_index": 2.446369621538172
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02211775084734111,
        "excess_kurtosis": 13.080004088650472,
        "return_acf_1": -0.14440129313889946,
        "abs_return_acf_1": 0.423888977864242,
        "abs_return_acf_5": 0.4156130266763116,
        "abs_return_acf_20": 0.3396513312681839,
        "quantile_01": -0.07895079983713396,
        "quantile_99": 0.052533435478182164,
        "hill_tail_index": 2.5494651133471153
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018971637571780692,
        "excess_kurtosis": 6.590143312278986,
        "return_acf_1": -0.11870668144600649,
        "abs_return_acf_1": 0.42169978997837804,
        "abs_return_acf_5": 0.4080220425304783,
        "abs_return_acf_20": 0.2625370445000099,
        "quantile_01": -0.06072094307551577,
        "quantile_99": 0.05835774000698453,
        "hill_tail_index": 4.006033201370086
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02003531740450164,
        "excess_kurtosis": 9.629119437383498,
        "return_acf_1": -0.15853141125879122,
        "abs_return_acf_1": 0.3818210558935385,
        "abs_return_acf_5": 0.35091103143093605,
        "abs_return_acf_20": 0.24601284349657232,
        "quantile_01": -0.061064449928830415,
        "quantile_99": 0.052920031019148266,
        "hill_tail_index": 3.2837268066594576
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021390590377918597,
        "excess_kurtosis": 10.406016294794618,
        "return_acf_1": -0.10534721760977812,
        "abs_return_acf_1": 0.36965110136476154,
        "abs_return_acf_5": 0.36634880506534134,
        "abs_return_acf_20": 0.3374181716948405,
        "quantile_01": -0.07156452874775321,
        "quantile_99": 0.054365063309006194,
        "hill_tail_index": 3.0262990921424446
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0193809041600521,
        "excess_kurtosis": 11.618743813470555,
        "return_acf_1": -0.15220461981426645,
        "abs_return_acf_1": 0.34812301192934897,
        "abs_return_acf_5": 0.3169396109768207,
        "abs_return_acf_20": 0.24413543152243342,
        "quantile_01": -0.060244079764873296,
        "quantile_99": 0.05430612379624879,
        "hill_tail_index": 2.933735248811484
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017045944718469555,
        "excess_kurtosis": 3.0992499620309903,
        "return_acf_1": -0.11069026550179535,
        "abs_return_acf_1": 0.25205181176970654,
        "abs_return_acf_5": 0.21038209282267012,
        "abs_return_acf_20": 0.17777088798806137,
        "quantile_01": -0.04876651277077592,
        "quantile_99": 0.04217852255779357,
        "hill_tail_index": 4.063766046278196
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018497758201740953,
        "excess_kurtosis": 6.497761105255485,
        "return_acf_1": -0.08249801142609256,
        "abs_return_acf_1": 0.2630529354755783,
        "abs_return_acf_5": 0.24927300259209906,
        "abs_return_acf_20": 0.18485545120813446,
        "quantile_01": -0.05584553122460599,
        "quantile_99": 0.046094725001576936,
        "hill_tail_index": 3.228045720146786
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02002150516186233,
        "excess_kurtosis": 7.993166022868438,
        "return_acf_1": -0.07285482415655674,
        "abs_return_acf_1": 0.4283317023052515,
        "abs_return_acf_5": 0.3643294236694818,
        "abs_return_acf_20": 0.2846998984122522,
        "quantile_01": -0.06899260609194484,
        "quantile_99": 0.05013035579602516,
        "hill_tail_index": 2.4951618359146845
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018024685226389007,
        "excess_kurtosis": 4.751511489292554,
        "return_acf_1": -0.17276830553114922,
        "abs_return_acf_1": 0.3229091078530128,
        "abs_return_acf_5": 0.29072653507351304,
        "abs_return_acf_20": 0.23396200756095015,
        "quantile_01": -0.052600921306332676,
        "quantile_99": 0.05137329318741844,
        "hill_tail_index": 3.8964309311832332
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01811135739211043,
        "excess_kurtosis": 5.305430630682174,
        "return_acf_1": -0.08607295078549475,
        "abs_return_acf_1": 0.34874999205013735,
        "abs_return_acf_5": 0.36987364216861357,
        "abs_return_acf_20": 0.2351392627571713,
        "quantile_01": -0.05950201006959592,
        "quantile_99": 0.048179862872088766,
        "hill_tail_index": 3.772563871083315
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022405780899992022,
        "excess_kurtosis": 9.869729406825988,
        "return_acf_1": -0.0822350755652738,
        "abs_return_acf_1": 0.40027246982131004,
        "abs_return_acf_5": 0.4071275554603207,
        "abs_return_acf_20": 0.35296720949087623,
        "quantile_01": -0.08337989528582672,
        "quantile_99": 0.06380506198785388,
        "hill_tail_index": 3.334827448150767
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021014144455394075,
        "excess_kurtosis": 11.572688630213682,
        "return_acf_1": -0.08685206267947713,
        "abs_return_acf_1": 0.37864774930452355,
        "abs_return_acf_5": 0.3163012832851504,
        "abs_return_acf_20": 0.2627264403166604,
        "quantile_01": -0.07283088133982832,
        "quantile_99": 0.052663909918366,
        "hill_tail_index": 2.9064995756942396
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018797597645563623,
        "excess_kurtosis": 8.106638009252839,
        "return_acf_1": -0.12482449599238772,
        "abs_return_acf_1": 0.3352180095897819,
        "abs_return_acf_5": 0.3585364207435441,
        "abs_return_acf_20": 0.22361277261185283,
        "quantile_01": -0.061619272038109935,
        "quantile_99": 0.04712699829140357,
        "hill_tail_index": 2.598586971584212
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
