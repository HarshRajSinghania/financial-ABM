# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27019
Run ID: `b941c9fb63adf409c6687d5b3c1db360eb37900bd4d15b802082f6c88743de24`
Result fingerprint: `079e61d835660948823344d1145c4ec5657ea8bad260a1a19b15ba05136abe8f`

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
    "equal_weight_sd": -0.48146428571428246,
    "equal_weight_raw": -7.221964285714237,
    "fixed_start_cap_weight_sd": -0.48012871369567844,
    "fixed_start_cap_weight_raw": -7.201930705435176,
    "end_cap_weight_sd": -0.4609153256606392,
    "end_cap_weight_raw": -6.913729884909589
  },
  "full_period_change": {
    "equal_weight_sd": -0.8127380952380903,
    "equal_weight_raw": -12.191071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7664232804232759,
    "inflation_mean_sd": 0.6108505291005291
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.47091666666666987,
    "equal_weight_raw": 7.063750000000048,
    "fixed_start_cap_weight_sd": 0.4722522386852742,
    "fixed_start_cap_weight_raw": 7.083783580279112,
    "end_cap_weight_sd": 0.4914656267203133,
    "end_cap_weight_raw": 7.3719844008047
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.47821428571428254,
      "change_raw": -7.173214285714238,
      "decay_adjusted_gain_sd": 0.4741666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4882142857142824,
      "change_raw": -7.3232142857142355,
      "decay_adjusted_gain_sd": 0.46416666666666984
    },
    "small": {
      "count": 18,
      "change_sd": -0.4786309523809492,
      "change_raw": -7.179464285714238,
      "decay_adjusted_gain_sd": 0.4737500000000032
    },
    "large_minus_small_sd": 0.0004166666666666763,
    "large_minus_small_raw": 0.006250000000000144
  },
  "inflation": {
    "initial_mean_sd": 0.18299999999999997,
    "final_mean_sd": 0.6379166666666667,
    "mean_sd": 0.4366468914793228,
    "mean_absolute_raw_gap": 6.549703372189842,
    "final_absolute_raw_gap": 9.56875,
    "mean_range_fraction": 0.06549703372189841
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.3933333333333333,
    "initial_wealth_share": 0.2595132509853646,
    "final_wealth_share": 0.3251841874135554
  },
  "pricing_slope": {
    "mean": -0.002750918524558725,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.1078929118500032,
    "real_improvement_cost": 0.0933931109449184,
    "washing_cost": 0.01449980090508483,
    "fine_transfer": 0.006801463300111583,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11469437515011478,
    "resource_cost_fraction_initial_cap": 0.0035964303950001054,
    "private_net_outflow_fraction_initial_cap": 0.003823145838337158,
    "fine_transfer_fraction_initial_cap": 0.00022671544333705267,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005285717939228043,
    "unapplied_final_day_resource_cost": 0.0012116315720247376
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 130.94001967099265,
    "beneficial_raw_gain_per_resource_cost": 1964.10029506489,
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
    "fixed_exposure": 15.000000000000005,
    "accrued_cost": 3.345690831667924,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.36950035547744664,
    "accrued_cost_fraction_initial_cap": 0.11152302772226409,
    "mean_contract_rate": 0.046380639545841984,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 77,
    "maximum_relative_cash_error": 3.835258266501422e-15,
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
      "minimum": -0.48762130353402194,
      "maximum": -0.12186051008124633,
      "mean": -0.2015959845221433,
      "median": -0.18333155140254503,
      "quantile_05": -0.3901356570204506,
      "quantile_95": -0.13162405325152834
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
      "minimum": -0.37652166381377666,
      "maximum": 0.8922556971210727,
      "mean": 0.6149364824946366,
      "median": 0.8343978688347363,
      "quantile_05": -0.1944360328941318,
      "quantile_95": 0.8789705969408376
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
        "daily_volatility": 0.025428836046301705,
        "excess_kurtosis": 31.368044273887598,
        "return_acf_1": -0.15631293330763876,
        "abs_return_acf_1": 0.5293308227508561,
        "abs_return_acf_5": 0.38177957638409793,
        "abs_return_acf_20": 0.41509856332948925,
        "quantile_01": -0.08516464405691966,
        "quantile_99": 0.06328664129708438,
        "hill_tail_index": 1.7279847819872833
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02353850118137506,
        "excess_kurtosis": 19.50449429568455,
        "return_acf_1": -0.2199126791984688,
        "abs_return_acf_1": 0.4038450519501249,
        "abs_return_acf_5": 0.28936874624897857,
        "abs_return_acf_20": 0.4242639904187646,
        "quantile_01": -0.06833103651042423,
        "quantile_99": 0.08408228383282217,
        "hill_tail_index": 1.8267721534985966
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023479909740957244,
        "excess_kurtosis": 31.881505617212376,
        "return_acf_1": -0.2034556983360079,
        "abs_return_acf_1": 0.4105495717568797,
        "abs_return_acf_5": 0.3521784336668952,
        "abs_return_acf_20": 0.4261921262154931,
        "quantile_01": -0.06924315838628162,
        "quantile_99": 0.05741616114413835,
        "hill_tail_index": 1.8401196737148935
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.024932630536690804,
        "excess_kurtosis": 31.00912998333324,
        "return_acf_1": -0.17012761334410467,
        "abs_return_acf_1": 0.514718102814765,
        "abs_return_acf_5": 0.40092386080618125,
        "abs_return_acf_20": 0.40918985497477817,
        "quantile_01": -0.07104266354454644,
        "quantile_99": 0.06349160171942499,
        "hill_tail_index": 1.9064333870289467
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.025037674433796803,
        "excess_kurtosis": 31.311307177919332,
        "return_acf_1": -0.17025476518729873,
        "abs_return_acf_1": 0.4655724678192031,
        "abs_return_acf_5": 0.3252394486896323,
        "abs_return_acf_20": 0.36907178327439927,
        "quantile_01": -0.07348966830244216,
        "quantile_99": 0.058698333376436485,
        "hill_tail_index": 1.694006122206832
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.025210601361402542,
        "excess_kurtosis": 32.284699946759716,
        "return_acf_1": -0.1605407788600641,
        "abs_return_acf_1": 0.46790382730403024,
        "abs_return_acf_5": 0.36859425152900704,
        "abs_return_acf_20": 0.38676024385546914,
        "quantile_01": -0.07483013754732017,
        "quantile_99": 0.05599018711724979,
        "hill_tail_index": 1.4956561438295282
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022551112980935366,
        "excess_kurtosis": 18.387967524236668,
        "return_acf_1": -0.20259986185623513,
        "abs_return_acf_1": 0.4014639470598382,
        "abs_return_acf_5": 0.2530404928856177,
        "abs_return_acf_20": 0.44523542060022175,
        "quantile_01": -0.077889074813719,
        "quantile_99": 0.07125002446392292,
        "hill_tail_index": 2.5051886604260614
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.043910159847282436,
        "excess_kurtosis": 31.680838497402107,
        "return_acf_1": -0.48762130353402194,
        "abs_return_acf_1": 0.6873250419454155,
        "abs_return_acf_5": 0.5236004557405743,
        "abs_return_acf_20": 0.5762929021925096,
        "quantile_01": -0.17303361904887576,
        "quantile_99": 0.161780924864168,
        "hill_tail_index": 1.7768933925702928
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.024233534998323786,
        "excess_kurtosis": 28.170243823101064,
        "return_acf_1": -0.13926220149849602,
        "abs_return_acf_1": 0.4356526355629637,
        "abs_return_acf_5": 0.34936710033430035,
        "abs_return_acf_20": 0.4011061334703337,
        "quantile_01": -0.06804993942816123,
        "quantile_99": 0.057797245607774335,
        "hill_tail_index": 1.8266183867351982
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.024668622382671507,
        "excess_kurtosis": 31.553400612241084,
        "return_acf_1": -0.1856191677879939,
        "abs_return_acf_1": 0.38686627318852745,
        "abs_return_acf_5": 0.2510430881595964,
        "abs_return_acf_20": 0.361122518201695,
        "quantile_01": -0.06687791098829524,
        "quantile_99": 0.05212086778168566,
        "hill_tail_index": 1.4759906872838278
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.025189509044260424,
        "excess_kurtosis": 37.01655863143959,
        "return_acf_1": -0.15468167067702907,
        "abs_return_acf_1": 0.4639126578237407,
        "abs_return_acf_5": 0.26906502866471493,
        "abs_return_acf_20": 0.36018395321328395,
        "quantile_01": -0.06441463768549353,
        "quantile_99": 0.05636540221680313,
        "hill_tail_index": 1.5610871538140836
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.023886013607499302,
        "excess_kurtosis": 31.525352984005956,
        "return_acf_1": -0.13009898703301848,
        "abs_return_acf_1": 0.42526457403443796,
        "abs_return_acf_5": 0.3221074086950892,
        "abs_return_acf_20": 0.3985535514542544,
        "quantile_01": -0.07344981445226921,
        "quantile_99": 0.05510162092169105,
        "hill_tail_index": 1.4632700122279592
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020740454597638517,
        "excess_kurtosis": 16.60829528819354,
        "return_acf_1": -0.22103090521376076,
        "abs_return_acf_1": 0.46423132949573315,
        "abs_return_acf_5": 0.27082356430175314,
        "abs_return_acf_20": 0.35643695145682336,
        "quantile_01": -0.06575577509269433,
        "quantile_99": 0.069529442854792,
        "hill_tail_index": 2.071323277451298
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.025192734373525018,
        "excess_kurtosis": 33.20880576686289,
        "return_acf_1": -0.21827768353027985,
        "abs_return_acf_1": 0.504712246637561,
        "abs_return_acf_5": 0.3451054925523826,
        "abs_return_acf_20": 0.43634811934109663,
        "quantile_01": -0.07260720664264537,
        "quantile_99": 0.06098036362107385,
        "hill_tail_index": 1.5324938723194903
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024019615754066442,
        "excess_kurtosis": 25.348610184224476,
        "return_acf_1": -0.15839108132197305,
        "abs_return_acf_1": 0.44356367403079205,
        "abs_return_acf_5": 0.3382989710785341,
        "abs_return_acf_20": 0.43105130922836554,
        "quantile_01": -0.07782443201331347,
        "quantile_99": 0.059766068338182064,
        "hill_tail_index": 1.8261294604198266
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023917874027148737,
        "excess_kurtosis": 32.25368406605278,
        "return_acf_1": -0.19848508970949616,
        "abs_return_acf_1": 0.43244813438431,
        "abs_return_acf_5": 0.3386389893636351,
        "abs_return_acf_20": 0.3558382090679087,
        "quantile_01": -0.06390173261227963,
        "quantile_99": 0.05937564941092695,
        "hill_tail_index": 1.761930229523657
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02538177082050921,
        "excess_kurtosis": 19.900523507340335,
        "return_acf_1": -0.1977607171394981,
        "abs_return_acf_1": 0.4091890292342873,
        "abs_return_acf_5": 0.31562732718791436,
        "abs_return_acf_20": 0.41957646246659763,
        "quantile_01": -0.08322482921824458,
        "quantile_99": 0.0759504306894376,
        "hill_tail_index": 2.0034335480336525
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021104839127639472,
        "excess_kurtosis": 12.413067473265336,
        "return_acf_1": -0.13348802307415147,
        "abs_return_acf_1": 0.3860263469236385,
        "abs_return_acf_5": 0.2943727436605953,
        "abs_return_acf_20": 0.32366009520282046,
        "quantile_01": -0.05896816449242975,
        "quantile_99": 0.05850231279705914,
        "hill_tail_index": 2.255562135632711
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02629339181411726,
        "excess_kurtosis": 35.311041198753486,
        "return_acf_1": -0.17212566518082165,
        "abs_return_acf_1": 0.46032184477255467,
        "abs_return_acf_5": 0.27799432299095533,
        "abs_return_acf_20": 0.39078605798487204,
        "quantile_01": -0.07257104140544883,
        "quantile_99": 0.06254655154573054,
        "hill_tail_index": 1.6153390384945634
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024803491223320304,
        "excess_kurtosis": 32.4935056847774,
        "return_acf_1": -0.20375916834109148,
        "abs_return_acf_1": 0.4432072077236201,
        "abs_return_acf_5": 0.2535170395320938,
        "abs_return_acf_20": 0.3653731506391508,
        "quantile_01": -0.06912280383150077,
        "quantile_99": 0.05606244560341359,
        "hill_tail_index": 1.570776932588205
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.032756926608064105,
        "excess_kurtosis": 47.92486511392594,
        "return_acf_1": -0.42087895315421897,
        "abs_return_acf_1": 0.5799206425903399,
        "abs_return_acf_5": 0.4609387061322338,
        "abs_return_acf_20": 0.44483235943718485,
        "quantile_01": -0.08213510384717378,
        "quantile_99": 0.09101961490186547,
        "hill_tail_index": 1.6567101257732715
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.023298183819568035,
        "excess_kurtosis": 29.835677977051056,
        "return_acf_1": -0.2029900244078949,
        "abs_return_acf_1": 0.37100480647117146,
        "abs_return_acf_5": 0.32819994070396263,
        "abs_return_acf_20": 0.3835239054799758,
        "quantile_01": -0.06381641958698041,
        "quantile_99": 0.049600340916812743,
        "hill_tail_index": 1.5497344679692895
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024247462525139957,
        "excess_kurtosis": 27.87918309569108,
        "return_acf_1": -0.20133622251437852,
        "abs_return_acf_1": 0.3939977318531158,
        "abs_return_acf_5": 0.3782991650228802,
        "abs_return_acf_20": 0.3823475144131581,
        "quantile_01": -0.07333969771748963,
        "quantile_99": 0.06324328420493361,
        "hill_tail_index": 1.7252097002288986
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.05636605439088192,
        "excess_kurtosis": 21.660944566944853,
        "return_acf_1": -0.3525605173014004,
        "abs_return_acf_1": 0.7264637394080685,
        "abs_return_acf_5": 0.5840466635525805,
        "abs_return_acf_20": 0.5160787208944683,
        "quantile_01": -0.259181779318282,
        "quantile_99": 0.3458055298574258,
        "hill_tail_index": 4.741898706122181
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02395250987525337,
        "excess_kurtosis": 29.223128467575506,
        "return_acf_1": -0.1810439350170962,
        "abs_return_acf_1": 0.420589786819724,
        "abs_return_acf_5": 0.3418341322193534,
        "abs_return_acf_20": 0.3526833103437667,
        "quantile_01": -0.06990355812808721,
        "quantile_99": 0.07146365161912503,
        "hill_tail_index": 1.7294110979989223
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.025334769318869875,
        "excess_kurtosis": 33.63624658296791,
        "return_acf_1": -0.1956746702856379,
        "abs_return_acf_1": 0.5136903481269676,
        "abs_return_acf_5": 0.38268979662533986,
        "abs_return_acf_20": 0.41082473334038166,
        "quantile_01": -0.06541792655606539,
        "quantile_99": 0.06306424825907775,
        "hill_tail_index": 1.6744068983252005
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023707280677951803,
        "excess_kurtosis": 25.80940006052026,
        "return_acf_1": -0.1626115176270758,
        "abs_return_acf_1": 0.4071892124755625,
        "abs_return_acf_5": 0.3256380475717219,
        "abs_return_acf_20": 0.4435194366805461,
        "quantile_01": -0.0684322631864389,
        "quantile_99": 0.06521627123874613,
        "hill_tail_index": 1.7694318783562044
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02470607774699693,
        "excess_kurtosis": 34.69262812192785,
        "return_acf_1": -0.15128607612539643,
        "abs_return_acf_1": 0.4120963077101188,
        "abs_return_acf_5": 0.30687833378611895,
        "abs_return_acf_20": 0.3913597442891931,
        "quantile_01": -0.0812412155480432,
        "quantile_99": 0.05113746932456986,
        "hill_tail_index": 1.3502282412659596
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.024847650732615308,
        "excess_kurtosis": 32.67771605731452,
        "return_acf_1": -0.12186051008124633,
        "abs_return_acf_1": 0.42371984941464236,
        "abs_return_acf_5": 0.3169228940518124,
        "abs_return_acf_20": 0.3627717923252536,
        "quantile_01": -0.09240998417092085,
        "quantile_99": 0.05733212158669361,
        "hill_tail_index": 1.6043930141966232
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.023316746173924083,
        "excess_kurtosis": 33.21107164964669,
        "return_acf_1": -0.17383111501850368,
        "abs_return_acf_1": 0.39327288144317685,
        "abs_return_acf_5": 0.31047769442453,
        "abs_return_acf_20": 0.4092533591764604,
        "quantile_01": -0.06419602845954647,
        "quantile_99": 0.05426069157630352,
        "hill_tail_index": 1.7289325423962985
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
