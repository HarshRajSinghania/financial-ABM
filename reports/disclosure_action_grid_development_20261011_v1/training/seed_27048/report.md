# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27048
Run ID: `5c9201e2082d71178b39735b0b04236bda8fe6a2c280bf91185ee9b04e9e4f8f`
Result fingerprint: `f8bd8c8d1f8c814ca30f0d80663bd5e350b8c37fc677402dab58241ce3d95b92`

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
    "equal_weight_sd": -0.5345518998502559,
    "equal_weight_raw": -8.018278497753839,
    "fixed_start_cap_weight_sd": -0.48496674426990294,
    "fixed_start_cap_weight_raw": -7.2745011640485435,
    "end_cap_weight_sd": -0.4735639701550301,
    "end_cap_weight_raw": -7.103459552325451
  },
  "full_period_change": {
    "equal_weight_sd": -0.7870757093740637,
    "equal_weight_raw": -11.806135640610956
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7578656302899326,
    "inflation_mean_sd": 0.6500800264550264
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4092500000000031,
    "equal_weight_raw": 6.138750000000045,
    "fixed_start_cap_weight_sd": 0.4635632056421405,
    "fixed_start_cap_weight_raw": 6.9534480846321065,
    "end_cap_weight_sd": 0.47721782188120937,
    "end_cap_weight_raw": 7.15826732821814
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5365476190476159,
      "change_raw": -8.04821428571424,
      "decay_adjusted_gain_sd": 0.41583333333333633
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4351587301587268,
      "change_raw": -6.527380952380902,
      "decay_adjusted_gain_sd": 0.5172222222222255
    },
    "small": {
      "count": 18,
      "change_sd": -0.5839158648297939,
      "change_raw": -8.758737972446907,
      "decay_adjusted_gain_sd": 0.3541666666666696
    },
    "large_minus_small_sd": 0.04736824578217791,
    "large_minus_small_raw": 0.7105236867326686
  },
  "inflation": {
    "initial_mean_sd": 0.2680833333333333,
    "final_mean_sd": 0.6954166666666666,
    "mean_sd": 0.5139803635859006,
    "mean_absolute_raw_gap": 7.7097054537885095,
    "final_absolute_raw_gap": 10.431249999999999,
    "mean_range_fraction": 0.0770970545378851
  },
  "impact": {
    "initial_share": 0.25333333333333335,
    "final_share": 0.24666666666666667,
    "initial_wealth_share": 0.3627233294435128,
    "final_wealth_share": 0.3685467327437501
  },
  "pricing_slope": {
    "mean": -0.0007034235619303271,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.06909817699726045,
    "real_improvement_cost": 0.05653323792338563,
    "washing_cost": 0.012564939073874829,
    "fine_transfer": 0.0008273585419780077,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06992553553923846,
    "resource_cost_fraction_initial_cap": 0.0023032725665753486,
    "private_net_outflow_fraction_initial_cap": 0.002330851184641282,
    "fine_transfer_fraction_initial_cap": 2.7578618065933593e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00989438996582199,
    "unapplied_final_day_resource_cost": 0.0030465763599718822
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 177.68196692782303,
    "beneficial_raw_gain_per_resource_cost": 2665.2295039173455,
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
    "accrued_cost": 3.565852255939542,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.589661779749066,
    "accrued_cost_fraction_initial_cap": 0.11886174186465141,
    "mean_contract_rate": 0.0492388951576073,
    "maximum_ledger_error": 1.6263032587282567e-19
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
    "maximum_relative_cash_error": 1.796933701139383e-15,
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
      "minimum": -0.22516372827009085,
      "maximum": -0.03320470060129038,
      "mean": -0.12767965961267275,
      "median": -0.13005033760860646,
      "quantile_05": -0.18778282190381984,
      "quantile_95": -0.04896893457253673
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
      "minimum": 0.29205805152078396,
      "maximum": 0.7969540424217743,
      "mean": 0.5273953096569639,
      "median": 0.5129484893923885,
      "quantile_05": 0.354463069565881,
      "quantile_95": 0.7340498346068378
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
        "daily_volatility": 0.017899681777423775,
        "excess_kurtosis": 19.40551734491822,
        "return_acf_1": -0.12723544136367912,
        "abs_return_acf_1": 0.288208264814162,
        "abs_return_acf_5": 0.4045661188835253,
        "abs_return_acf_20": 0.28722253780743656,
        "quantile_01": -0.0505842132155068,
        "quantile_99": 0.04222579728318669,
        "hill_tail_index": 2.543552072809468
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018384481320103768,
        "excess_kurtosis": 5.6947290747954575,
        "return_acf_1": -0.10198556302749748,
        "abs_return_acf_1": 0.2546527619044777,
        "abs_return_acf_5": 0.33914728423703655,
        "abs_return_acf_20": 0.3043871246879638,
        "quantile_01": -0.05133027348557807,
        "quantile_99": 0.05517463708078578,
        "hill_tail_index": 3.586608674059936
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.0189463096506585,
        "excess_kurtosis": 4.302809104486444,
        "return_acf_1": -0.11984623745309242,
        "abs_return_acf_1": 0.3211233052642066,
        "abs_return_acf_5": 0.33675584863123287,
        "abs_return_acf_20": 0.2536135557237505,
        "quantile_01": -0.05726535284793723,
        "quantile_99": 0.05843712695526404,
        "hill_tail_index": 3.405192473510813
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021155477514579937,
        "excess_kurtosis": 11.975558459387866,
        "return_acf_1": -0.16743348446771258,
        "abs_return_acf_1": 0.4160738471751878,
        "abs_return_acf_5": 0.45033220861507733,
        "abs_return_acf_20": 0.2778683872647467,
        "quantile_01": -0.06635431716448227,
        "quantile_99": 0.05588689141711733,
        "hill_tail_index": 2.927716750348947
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01813996693679311,
        "excess_kurtosis": 4.3020516091877985,
        "return_acf_1": -0.16516462470759555,
        "abs_return_acf_1": 0.37235695037586053,
        "abs_return_acf_5": 0.3716915581903057,
        "abs_return_acf_20": 0.22605843781526064,
        "quantile_01": -0.055911955456675155,
        "quantile_99": 0.05048339904312962,
        "hill_tail_index": 3.735599161164294
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02144996739220841,
        "excess_kurtosis": 16.574808531700533,
        "return_acf_1": -0.16008779280946156,
        "abs_return_acf_1": 0.4642935236042662,
        "abs_return_acf_5": 0.4006651505050214,
        "abs_return_acf_20": 0.2506786263135396,
        "quantile_01": -0.0663736192091679,
        "quantile_99": 0.06260933582427332,
        "hill_tail_index": 2.7717398487787417
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01600811826913606,
        "excess_kurtosis": 1.190671852533674,
        "return_acf_1": -0.054180993145101414,
        "abs_return_acf_1": 0.2412013741010788,
        "abs_return_acf_5": 0.22191328054991005,
        "abs_return_acf_20": 0.20162782733317203,
        "quantile_01": -0.04391933724601888,
        "quantile_99": 0.03865027557745942,
        "hill_tail_index": 4.169014089491184
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018431042440727262,
        "excess_kurtosis": 4.387202325455079,
        "return_acf_1": -0.1411555582435651,
        "abs_return_acf_1": 0.37917857866457444,
        "abs_return_acf_5": 0.3409371332906769,
        "abs_return_acf_20": 0.24365865629383118,
        "quantile_01": -0.05789582853314936,
        "quantile_99": 0.050013187276049746,
        "hill_tail_index": 3.930919343228188
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.023643293875564624,
        "excess_kurtosis": 11.719288854066498,
        "return_acf_1": -0.18906559416457172,
        "abs_return_acf_1": 0.5075529516420028,
        "abs_return_acf_5": 0.4858717903899659,
        "abs_return_acf_20": 0.40161398858138525,
        "quantile_01": -0.08184785190655768,
        "quantile_99": 0.07446973566086997,
        "hill_tail_index": 2.831719843502441
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018308939578955057,
        "excess_kurtosis": 5.018112414693036,
        "return_acf_1": -0.11543581630764925,
        "abs_return_acf_1": 0.22098342907351587,
        "abs_return_acf_5": 0.2863346793405514,
        "abs_return_acf_20": 0.1993438761057972,
        "quantile_01": -0.05726471407425598,
        "quantile_99": 0.05227842523562151,
        "hill_tail_index": 3.461069827954271
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020677948658930544,
        "excess_kurtosis": 14.94866884462866,
        "return_acf_1": -0.18621498914067863,
        "abs_return_acf_1": 0.4667355644902612,
        "abs_return_acf_5": 0.47206831577787356,
        "abs_return_acf_20": 0.30708960206631125,
        "quantile_01": -0.061517911688086194,
        "quantile_99": 0.053021309700301646,
        "hill_tail_index": 2.12253289949983
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019195818620521526,
        "excess_kurtosis": 9.097299583091093,
        "return_acf_1": -0.22516372827009085,
        "abs_return_acf_1": 0.38062250647463325,
        "abs_return_acf_5": 0.39269652098669283,
        "abs_return_acf_20": 0.22517149391168986,
        "quantile_01": -0.06108048213936281,
        "quantile_99": 0.05097081338973688,
        "hill_tail_index": 2.8821397263201236
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01768762455099289,
        "excess_kurtosis": 20.100106605672714,
        "return_acf_1": -0.07160153257397231,
        "abs_return_acf_1": 0.36466980926280335,
        "abs_return_acf_5": 0.3273858100477958,
        "abs_return_acf_20": 0.2775751961471119,
        "quantile_01": -0.05380534386262958,
        "quantile_99": 0.04714912505901553,
        "hill_tail_index": 2.7973278641318275
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01826386996314369,
        "excess_kurtosis": 1.964595478071038,
        "return_acf_1": -0.12986750577266679,
        "abs_return_acf_1": 0.3030852313151031,
        "abs_return_acf_5": 0.2686705635220715,
        "abs_return_acf_20": 0.26389295048757466,
        "quantile_01": -0.05594575957268602,
        "quantile_99": 0.04807674813670122,
        "hill_tail_index": 5.591705212213928
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01737035585947752,
        "excess_kurtosis": 22.58629942628506,
        "return_acf_1": -0.10815508153718581,
        "abs_return_acf_1": 0.20741304787262144,
        "abs_return_acf_5": 0.26513301076927803,
        "abs_return_acf_20": 0.18414791332884814,
        "quantile_01": -0.04941878704996124,
        "quantile_99": 0.04315514209458111,
        "hill_tail_index": 2.606821526026589
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021406235320127864,
        "excess_kurtosis": 13.304843610240997,
        "return_acf_1": -0.14035233711598996,
        "abs_return_acf_1": 0.48174010299067593,
        "abs_return_acf_5": 0.455080824107229,
        "abs_return_acf_20": 0.3336706184912176,
        "quantile_01": -0.06345916588391223,
        "quantile_99": 0.05399741515471605,
        "hill_tail_index": 2.4254503880347285
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02271772906042953,
        "excess_kurtosis": 13.222336628055434,
        "return_acf_1": -0.1490154415655186,
        "abs_return_acf_1": 0.49332547193472537,
        "abs_return_acf_5": 0.5012751698006942,
        "abs_return_acf_20": 0.3569317952945243,
        "quantile_01": -0.0733267880430471,
        "quantile_99": 0.0617543415679006,
        "hill_tail_index": 2.0045252307151658
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018113974436563356,
        "excess_kurtosis": 4.909740931295646,
        "return_acf_1": -0.14651512290925348,
        "abs_return_acf_1": 0.29574536769817295,
        "abs_return_acf_5": 0.3470974764390023,
        "abs_return_acf_20": 0.23189391682559765,
        "quantile_01": -0.05536282510092113,
        "quantile_99": 0.04841638906240092,
        "hill_tail_index": 3.8766367342190637
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016874567478271794,
        "excess_kurtosis": 3.3738037708245523,
        "return_acf_1": -0.1437128497731453,
        "abs_return_acf_1": 0.19600918740005233,
        "abs_return_acf_5": 0.2043739816957812,
        "abs_return_acf_20": 0.20651744463344962,
        "quantile_01": -0.04156459625689482,
        "quantile_99": 0.04561397615121374,
        "hill_tail_index": 4.049013612161984
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01563634102905344,
        "excess_kurtosis": 6.942200618578012,
        "return_acf_1": -0.09260239465220436,
        "abs_return_acf_1": 0.21522430978416157,
        "abs_return_acf_5": 0.25897971874672376,
        "abs_return_acf_20": 0.16111940763495622,
        "quantile_01": -0.04079914334441413,
        "quantile_99": 0.03891377486659128,
        "hill_tail_index": 3.39606391185608
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01909959586720776,
        "excess_kurtosis": 5.449199295867679,
        "return_acf_1": -0.1302331694445461,
        "abs_return_acf_1": 0.3567826622019578,
        "abs_return_acf_5": 0.36358970255398426,
        "abs_return_acf_20": 0.21659942795487683,
        "quantile_01": -0.059163684228938015,
        "quantile_99": 0.047127590826718975,
        "hill_tail_index": 3.4163224415057356
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016377700902863754,
        "excess_kurtosis": 2.7392420214385353,
        "return_acf_1": -0.044704523013165576,
        "abs_return_acf_1": 0.22215642988271528,
        "abs_return_acf_5": 0.24097569447083111,
        "abs_return_acf_20": 0.23480490969315532,
        "quantile_01": -0.047874182218985505,
        "quantile_99": 0.04225561944052365,
        "hill_tail_index": 3.9496687712417065
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01808778099770939,
        "excess_kurtosis": 4.58869477438409,
        "return_acf_1": -0.13441639663518795,
        "abs_return_acf_1": 0.3505737851300149,
        "abs_return_acf_5": 0.3049471178934997,
        "abs_return_acf_20": 0.2440548554899912,
        "quantile_01": -0.050885515979289156,
        "quantile_99": 0.04992453634524734,
        "hill_tail_index": 4.123271824981146
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01709724161210109,
        "excess_kurtosis": 14.509690096960536,
        "return_acf_1": -0.11386848289402288,
        "abs_return_acf_1": 0.18238773654374832,
        "abs_return_acf_5": 0.31559569000821763,
        "abs_return_acf_20": 0.2942177967515383,
        "quantile_01": -0.05133467291741073,
        "quantile_99": 0.04039067106908775,
        "hill_tail_index": 2.5626388148524692
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018322507178397212,
        "excess_kurtosis": 21.08328629144445,
        "return_acf_1": -0.03320470060129038,
        "abs_return_acf_1": 0.3790955192407694,
        "abs_return_acf_5": 0.34732788955271093,
        "abs_return_acf_20": 0.19195938822954517,
        "quantile_01": -0.05321252818276142,
        "quantile_99": 0.04565386055820615,
        "hill_tail_index": 2.528840665796665
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016483372639302173,
        "excess_kurtosis": 5.773257613812294,
        "return_acf_1": -0.10472593242127816,
        "abs_return_acf_1": 0.3135179921080582,
        "abs_return_acf_5": 0.28137509084681683,
        "abs_return_acf_20": 0.27431770732690963,
        "quantile_01": -0.04870840671434233,
        "quantile_99": 0.04548073983883605,
        "hill_tail_index": 3.7696172115072595
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017328836147907905,
        "excess_kurtosis": 13.357805754407565,
        "return_acf_1": -0.1256921090077943,
        "abs_return_acf_1": 0.270372169058027,
        "abs_return_acf_5": 0.27031033378932395,
        "abs_return_acf_20": 0.26453483364957525,
        "quantile_01": -0.04556369636326616,
        "quantile_99": 0.042932272654822204,
        "hill_tail_index": 2.9279496414842825
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017960334182277445,
        "excess_kurtosis": 6.654534453782601,
        "return_acf_1": -0.14662352671407558,
        "abs_return_acf_1": 0.32130267988746697,
        "abs_return_acf_5": 0.3587517161159819,
        "abs_return_acf_20": 0.3401324915586035,
        "quantile_01": -0.055098392421950824,
        "quantile_99": 0.051725745924260456,
        "hill_tail_index": 4.748567984586395
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020999624826375563,
        "excess_kurtosis": 12.169548134645513,
        "return_acf_1": -0.1360352618977159,
        "abs_return_acf_1": 0.4219270434796968,
        "abs_return_acf_5": 0.3843015433709098,
        "abs_return_acf_20": 0.2643080525345102,
        "quantile_01": -0.06245209608240621,
        "quantile_99": 0.060107878845192135,
        "hill_tail_index": 2.6232932832019666
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01942140142916552,
        "excess_kurtosis": 6.307448472062397,
        "return_acf_1": -0.1260935967504733,
        "abs_return_acf_1": 0.48357317412266476,
        "abs_return_acf_5": 0.41767021638462326,
        "abs_return_acf_20": 0.32850514147062665,
        "quantile_01": -0.06478313270007276,
        "quantile_99": 0.06535277950911357,
        "hill_tail_index": 3.152029062054499
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
