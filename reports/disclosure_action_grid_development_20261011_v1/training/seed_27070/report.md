# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27070
Run ID: `9c18f4db91ea1032f9108698c79962def4dfac4669af5792a33bf37ae64e7740`
Result fingerprint: `fe45944a8d386b9ebafbfbd8573bbc9a7a43b0828b339706549e8489e13fe308`

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
    "equal_weight_sd": -0.6377976190476159,
    "equal_weight_raw": -9.566964285714237,
    "fixed_start_cap_weight_sd": -0.568944389648309,
    "fixed_start_cap_weight_raw": -8.534165844724635,
    "end_cap_weight_sd": -0.5987817090180969,
    "end_cap_weight_raw": -8.981725635271452
  },
  "full_period_change": {
    "equal_weight_sd": -0.9871547619047568,
    "equal_weight_raw": -14.807321428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9381878306878262,
    "inflation_mean_sd": 0.7348482142857143
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3138858194597498,
    "equal_weight_raw": 4.708287291896246,
    "fixed_start_cap_weight_sd": 0.3826105118685469,
    "fixed_start_cap_weight_raw": 5.739157678028204,
    "end_cap_weight_sd": 0.35309456888812246,
    "end_cap_weight_raw": 5.296418533321838
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.35821428571428254,
      "change_raw": -5.373214285714238,
      "decay_adjusted_gain_sd": 0.59416666666667
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6587698412698381,
      "change_raw": -9.881547619047572,
      "decay_adjusted_gain_sd": 0.2912860648658251
    },
    "small": {
      "count": 18,
      "change_sd": -0.6739087301587269,
      "change_raw": -10.108630952380903,
      "decay_adjusted_gain_sd": 0.27847222222222545
    },
    "large_minus_small_sd": 0.31569444444444433,
    "large_minus_small_raw": 4.735416666666665
  },
  "inflation": {
    "initial_mean_sd": 0.2783333333333333,
    "final_mean_sd": 0.8064999999999998,
    "mean_sd": 0.5374159034138218,
    "mean_absolute_raw_gap": 8.061238551207328,
    "final_absolute_raw_gap": 12.097499999999998,
    "mean_range_fraction": 0.08061238551207328
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.26,
    "initial_wealth_share": 0.26036178759047535,
    "final_wealth_share": 0.2879841793922496
  },
  "pricing_slope": {
    "mean": -0.0016136651503788353,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.09269267631641943,
    "real_improvement_cost": 0.07381379109946312,
    "washing_cost": 0.01887888521695632,
    "fine_transfer": 0.010864462225347789,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10355713854176722,
    "resource_cost_fraction_initial_cap": 0.0030897558772139807,
    "private_net_outflow_fraction_initial_cap": 0.003451904618058907,
    "fine_transfer_fraction_initial_cap": 0.0003621487408449263,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001789448888499998,
    "unapplied_final_day_resource_cost": 0.00370467746412776
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 101.58919731314799,
    "beneficial_raw_gain_per_resource_cost": 1523.8379596972202,
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
    "accrued_cost": 3.059195238502615,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.08300476231213834,
    "accrued_cost_fraction_initial_cap": 0.10197317461675381,
    "mean_contract_rate": 0.0417349903011494,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "price_cap_hits": 2,
    "maximum_relative_cash_error": 1.4735848116684155e-15,
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
      "minimum": -0.17825387174741517,
      "maximum": -0.07286208987664904,
      "mean": -0.11963899284557523,
      "median": -0.11565399753641577,
      "quantile_05": -0.17138684172153576,
      "quantile_95": -0.07977999595228318
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
      "minimum": 0.2636903550317897,
      "maximum": 0.7785264740607153,
      "mean": 0.5026068747433371,
      "median": 0.47663726318669947,
      "quantile_05": 0.32651483148137317,
      "quantile_95": 0.7324323512552067
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
        "daily_volatility": 0.01576873018133463,
        "excess_kurtosis": 11.605018215104892,
        "return_acf_1": -0.08192570586057438,
        "abs_return_acf_1": 0.26175792091690986,
        "abs_return_acf_5": 0.3579388002835093,
        "abs_return_acf_20": 0.18394933762161034,
        "quantile_01": -0.03683007940848038,
        "quantile_99": 0.04048251116070508,
        "hill_tail_index": 2.6188843590305724
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016069939924874526,
        "excess_kurtosis": 1.804078232917977,
        "return_acf_1": -0.11331355164772505,
        "abs_return_acf_1": 0.171623243042059,
        "abs_return_acf_5": 0.2602595075479425,
        "abs_return_acf_20": 0.15763112150017494,
        "quantile_01": -0.04449253675201008,
        "quantile_99": 0.04466985356074936,
        "hill_tail_index": 4.205281387485712
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019162883144263017,
        "excess_kurtosis": 9.025414865461414,
        "return_acf_1": -0.1200832920210004,
        "abs_return_acf_1": 0.418850373536385,
        "abs_return_acf_5": 0.34448974025541446,
        "abs_return_acf_20": 0.26367692945097604,
        "quantile_01": -0.05606902038901028,
        "quantile_99": 0.05948471784904169,
        "hill_tail_index": 3.452817993523409
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017106180013226526,
        "excess_kurtosis": 13.820248491537892,
        "return_acf_1": -0.09253609367025846,
        "abs_return_acf_1": 0.2289167848663233,
        "abs_return_acf_5": 0.4145624435493333,
        "abs_return_acf_20": 0.2226253914889812,
        "quantile_01": -0.04582723293853954,
        "quantile_99": 0.04613733900497703,
        "hill_tail_index": 1.9160455308286686
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01757279119952183,
        "excess_kurtosis": 5.819390480330945,
        "return_acf_1": -0.09827610461874879,
        "abs_return_acf_1": 0.29925782164093623,
        "abs_return_acf_5": 0.31631833672005516,
        "abs_return_acf_20": 0.17214300191669996,
        "quantile_01": -0.05135592092286995,
        "quantile_99": 0.04475115526738587,
        "hill_tail_index": 3.4466991179975532
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015280041937007233,
        "excess_kurtosis": 8.515859534380796,
        "return_acf_1": -0.13014743077743549,
        "abs_return_acf_1": 0.1675451463393038,
        "abs_return_acf_5": 0.294254107828104,
        "abs_return_acf_20": 0.1874504251689079,
        "quantile_01": -0.037954848807145045,
        "quantile_99": 0.03853251726315819,
        "hill_tail_index": 2.367875492539706
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0180430864535274,
        "excess_kurtosis": 3.817155889856429,
        "return_acf_1": -0.12432375261355677,
        "abs_return_acf_1": 0.329847180097578,
        "abs_return_acf_5": 0.32553862557796975,
        "abs_return_acf_20": 0.23844890944262986,
        "quantile_01": -0.052069116636590924,
        "quantile_99": 0.05112105719753881,
        "hill_tail_index": 4.683519697999635
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01596881195274267,
        "excess_kurtosis": 2.8709390177548855,
        "return_acf_1": -0.14663601507645058,
        "abs_return_acf_1": 0.20753569486275458,
        "abs_return_acf_5": 0.22127867442657906,
        "abs_return_acf_20": 0.19777382776885377,
        "quantile_01": -0.041909315105732474,
        "quantile_99": 0.043021728897492624,
        "hill_tail_index": 5.318867906089366
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016747113585960375,
        "excess_kurtosis": 5.464608073556677,
        "return_acf_1": -0.1089305156190737,
        "abs_return_acf_1": 0.2816014776716652,
        "abs_return_acf_5": 0.32228478157082346,
        "abs_return_acf_20": 0.2428837626641905,
        "quantile_01": -0.04987851315571118,
        "quantile_99": 0.046722873406826314,
        "hill_tail_index": 3.2558311321571733
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016884062690143926,
        "excess_kurtosis": 2.978187216980457,
        "return_acf_1": -0.10276314078109194,
        "abs_return_acf_1": 0.22023228665559721,
        "abs_return_acf_5": 0.24572055100632884,
        "abs_return_acf_20": 0.13330533928892804,
        "quantile_01": -0.04979855032681317,
        "quantile_99": 0.041560818488191924,
        "hill_tail_index": 3.6619088948616256
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019115175573374058,
        "excess_kurtosis": 17.501565838871613,
        "return_acf_1": -0.09536289001079308,
        "abs_return_acf_1": 0.40872676304137423,
        "abs_return_acf_5": 0.4631103001072463,
        "abs_return_acf_20": 0.2888032989275997,
        "quantile_01": -0.06391030889030552,
        "quantile_99": 0.04414092025854651,
        "hill_tail_index": 1.6431672931834769
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.016812477324710754,
        "excess_kurtosis": 12.380470895650099,
        "return_acf_1": -0.09766550736440646,
        "abs_return_acf_1": 0.2758194507668199,
        "abs_return_acf_5": 0.41993469503041553,
        "abs_return_acf_20": 0.25160566663228723,
        "quantile_01": -0.044955382651086326,
        "quantile_99": 0.043093478142720854,
        "hill_tail_index": 2.214929205353221
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01691889380664238,
        "excess_kurtosis": 2.8058650327008614,
        "return_acf_1": -0.13751334854198585,
        "abs_return_acf_1": 0.2752149050777226,
        "abs_return_acf_5": 0.25235798112607927,
        "abs_return_acf_20": 0.19999063411882192,
        "quantile_01": -0.045758726639722413,
        "quantile_99": 0.04705939237161648,
        "hill_tail_index": 4.931985479215138
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01946805628217647,
        "excess_kurtosis": 27.94774450387422,
        "return_acf_1": -0.11586206236493896,
        "abs_return_acf_1": 0.326240766618828,
        "abs_return_acf_5": 0.4654459757479635,
        "abs_return_acf_20": 0.20725656813732965,
        "quantile_01": -0.05182197745583409,
        "quantile_99": 0.05029301758227752,
        "hill_tail_index": 1.9005463153723585
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016804233615566273,
        "excess_kurtosis": 13.20073172856403,
        "return_acf_1": -0.10260248314732463,
        "abs_return_acf_1": 0.1922117912652891,
        "abs_return_acf_5": 0.3847823737883678,
        "abs_return_acf_20": 0.1983044089692061,
        "quantile_01": -0.04766987313215121,
        "quantile_99": 0.03785530833012794,
        "hill_tail_index": 1.9114543384255878
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016604372312686397,
        "excess_kurtosis": 3.0447006791825544,
        "return_acf_1": -0.175829180113507,
        "abs_return_acf_1": 0.15974362559668445,
        "abs_return_acf_5": 0.2075549841312289,
        "abs_return_acf_20": 0.1250248312275798,
        "quantile_01": -0.04317413557387881,
        "quantile_99": 0.04520319671672423,
        "hill_tail_index": 3.2973097586501554
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017248674249791787,
        "excess_kurtosis": 19.596345973930948,
        "return_acf_1": -0.16595731702023755,
        "abs_return_acf_1": 0.28711414508298805,
        "abs_return_acf_5": 0.41519922180671676,
        "abs_return_acf_20": 0.21162717489005806,
        "quantile_01": -0.03857055519252214,
        "quantile_99": 0.040442068463749134,
        "hill_tail_index": 1.861509007999291
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017959245864165498,
        "excess_kurtosis": 8.457260340777092,
        "return_acf_1": -0.15494547470373363,
        "abs_return_acf_1": 0.2992014727239795,
        "abs_return_acf_5": 0.302479603391383,
        "abs_return_acf_20": 0.19698033159801615,
        "quantile_01": -0.05816451069093109,
        "quantile_99": 0.05041354228013683,
        "hill_tail_index": 3.133886610585962
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01695742152701056,
        "excess_kurtosis": 12.551778248062474,
        "return_acf_1": -0.11752433215595616,
        "abs_return_acf_1": 0.18313508637282236,
        "abs_return_acf_5": 0.31196447707260655,
        "abs_return_acf_20": 0.1341110068131062,
        "quantile_01": -0.04453256891197185,
        "quantile_99": 0.04160259688544997,
        "hill_tail_index": 2.1917354436419445
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020215596837015775,
        "excess_kurtosis": 27.40622944785995,
        "return_acf_1": -0.07286208987664904,
        "abs_return_acf_1": 0.3012110994285604,
        "abs_return_acf_5": 0.4495808765404834,
        "abs_return_acf_20": 0.18443192960767232,
        "quantile_01": -0.05268954196826492,
        "quantile_99": 0.04864699057085314,
        "hill_tail_index": 1.8708718722368096
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01744923364978171,
        "excess_kurtosis": 4.561871412598765,
        "return_acf_1": -0.10824082147676754,
        "abs_return_acf_1": 0.39525397594300987,
        "abs_return_acf_5": 0.285667846607313,
        "abs_return_acf_20": 0.26042191597221587,
        "quantile_01": -0.05163478652843323,
        "quantile_99": 0.044889795048372795,
        "hill_tail_index": 3.3711441654035523
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01960993306393129,
        "excess_kurtosis": 14.04015135090934,
        "return_acf_1": -0.11991963633958272,
        "abs_return_acf_1": 0.3438456018542864,
        "abs_return_acf_5": 0.4453378396445105,
        "abs_return_acf_20": 0.27591304785306947,
        "quantile_01": -0.057244439287786775,
        "quantile_99": 0.04959814963248034,
        "hill_tail_index": 1.9531596844346346
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01637361665753046,
        "excess_kurtosis": 4.705114836347075,
        "return_acf_1": -0.1384078001401669,
        "abs_return_acf_1": 0.3335485767970308,
        "abs_return_acf_5": 0.3468856152923709,
        "abs_return_acf_20": 0.2185015042828833,
        "quantile_01": -0.05137536313625893,
        "quantile_99": 0.04276906209555927,
        "hill_tail_index": 3.1570255338855837
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.015571350607458146,
        "excess_kurtosis": 4.5539321044448995,
        "return_acf_1": -0.10258311764562622,
        "abs_return_acf_1": 0.2510490435715702,
        "abs_return_acf_5": 0.31121202637060824,
        "abs_return_acf_20": 0.21958621089368147,
        "quantile_01": -0.045164013742474626,
        "quantile_99": 0.044814061438188516,
        "hill_tail_index": 3.860964726816223
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015211152852743166,
        "excess_kurtosis": 4.249566985322349,
        "return_acf_1": -0.0938229128375078,
        "abs_return_acf_1": 0.2821056028727949,
        "abs_return_acf_5": 0.3442150793397501,
        "abs_return_acf_20": 0.22000808229372024,
        "quantile_01": -0.040269334844414084,
        "quantile_99": 0.0444086672406864,
        "hill_tail_index": 3.8326333861602575
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020335918211778287,
        "excess_kurtosis": 14.350162908850422,
        "return_acf_1": -0.11544593270789258,
        "abs_return_acf_1": 0.40642377054733403,
        "abs_return_acf_5": 0.29484826826938587,
        "abs_return_acf_20": 0.2963790289626112,
        "quantile_01": -0.06391385697123698,
        "quantile_99": 0.059776023772411264,
        "hill_tail_index": 2.6792675728036226
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018257529732420653,
        "excess_kurtosis": 18.19816958634129,
        "return_acf_1": -0.07802441511822672,
        "abs_return_acf_1": 0.3248604961301438,
        "abs_return_acf_5": 0.4537595586754223,
        "abs_return_acf_20": 0.20391674773060492,
        "quantile_01": -0.05642258605849975,
        "quantile_99": 0.0408517879080604,
        "hill_tail_index": 1.8158252128901233
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016225926493084127,
        "excess_kurtosis": 4.651844208109696,
        "return_acf_1": -0.16323485692779963,
        "abs_return_acf_1": 0.2208221916670761,
        "abs_return_acf_5": 0.30337382356675496,
        "abs_return_acf_20": 0.17897674777155298,
        "quantile_01": -0.04465285671092902,
        "quantile_99": 0.04699469884389147,
        "hill_tail_index": 4.05852541145465
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018218517948639046,
        "excess_kurtosis": 7.280258133014668,
        "return_acf_1": -0.17825387174741517,
        "abs_return_acf_1": 0.27467031892264115,
        "abs_return_acf_5": 0.3275856172231952,
        "abs_return_acf_20": 0.21465285060895384,
        "quantile_01": -0.054269503270005036,
        "quantile_99": 0.04304025528001737,
        "hill_tail_index": 3.227949118192077
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.015200040836161529,
        "excess_kurtosis": 3.1167660328146205,
        "return_acf_1": -0.13617613244082455,
        "abs_return_acf_1": 0.22783599880110877,
        "abs_return_acf_5": 0.24517078023642497,
        "abs_return_acf_20": 0.21107654016775682,
        "quantile_01": -0.04202239457028358,
        "quantile_99": 0.03918823789630715,
        "hill_tail_index": 3.4704876187920353
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
