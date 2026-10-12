# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27163
Run ID: `9fe0b62982d84fc401bcbccb304828f41e77e556788299d79b6d5d2469dc29e3`
Result fingerprint: `5b3383a874705ddea37932711d515923ac65d7950a95bdc31d93c209721ec6f2`

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
    "equal_weight_sd": -0.7239642857142824,
    "equal_weight_raw": -10.859464285714239,
    "fixed_start_cap_weight_sd": -0.7368621075562283,
    "fixed_start_cap_weight_raw": -11.052931613343423,
    "end_cap_weight_sd": -0.741333595708258,
    "end_cap_weight_raw": -11.120003935623869
  },
  "full_period_change": {
    "equal_weight_sd": -1.1057380952380902,
    "equal_weight_raw": -16.58607142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.047200727513223,
    "inflation_mean_sd": 0.530015873015873
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.22841666666666977,
    "equal_weight_raw": 3.426250000000047,
    "fixed_start_cap_weight_sd": 0.21551884482472408,
    "fixed_start_cap_weight_raw": 3.232782672370862,
    "end_cap_weight_sd": 0.21104735667269428,
    "end_cap_weight_raw": 3.1657103500904142
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7282142857142825,
      "change_raw": -10.923214285714238,
      "decay_adjusted_gain_sd": 0.22416666666666987
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6971031746031713,
      "change_raw": -10.45654761904757,
      "decay_adjusted_gain_sd": 0.255277777777781
    },
    "small": {
      "count": 18,
      "change_sd": -0.7366865079365048,
      "change_raw": -11.050297619047573,
      "decay_adjusted_gain_sd": 0.2156944444444475
    },
    "large_minus_small_sd": 0.008472222222222325,
    "large_minus_small_raw": 0.12708333333333488
  },
  "inflation": {
    "initial_mean_sd": 0.3519166666666667,
    "final_mean_sd": 0.5475833333333334,
    "mean_sd": 0.45966631973355526,
    "mean_absolute_raw_gap": 6.89499479600333,
    "final_absolute_raw_gap": 8.21375,
    "mean_range_fraction": 0.0689499479600333
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.22666666666666666,
    "initial_wealth_share": 0.2630643842556315,
    "final_wealth_share": 0.21758190840592223
  },
  "pricing_slope": {
    "mean": -0.0006092314133862693,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.11286690934681577,
    "real_improvement_cost": 0.08980144068422209,
    "washing_cost": 0.02306546866259363,
    "fine_transfer": 0.021106793856685055,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.13397370320350083,
    "resource_cost_fraction_initial_cap": 0.003762230311560526,
    "private_net_outflow_fraction_initial_cap": 0.0044657901067833615,
    "fine_transfer_fraction_initial_cap": 0.0007035597952228353,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0012563428259163992,
    "unapplied_final_day_resource_cost": 0.006645116383172934
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 60.71310040876403,
    "beneficial_raw_gain_per_resource_cost": 910.6965061314604,
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
    "accrued_cost": 2.8015218109749482,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.17466866521552799,
    "accrued_cost_fraction_initial_cap": 0.09338406036583162,
    "mean_contract_rate": 0.03902123756727251,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "maximum_relative_cash_error": 2.647184802793109e-15,
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
      "minimum": -0.17521545898058144,
      "maximum": -0.05220662283317881,
      "mean": -0.1181380358090466,
      "median": -0.11769143505809379,
      "quantile_05": -0.17292407365333054,
      "quantile_95": -0.0542552919081124
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
      "minimum": 0.3383790373268084,
      "maximum": 0.764656429486219,
      "mean": 0.5573605208341761,
      "median": 0.5979925358147461,
      "quantile_05": 0.36560983015721055,
      "quantile_95": 0.7301031240695395
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
        "daily_volatility": 0.016954435638918908,
        "excess_kurtosis": 3.0447945470556697,
        "return_acf_1": -0.10144733238452919,
        "abs_return_acf_1": 0.27542894167554804,
        "abs_return_acf_5": 0.22236727951462434,
        "abs_return_acf_20": 0.1612412195625483,
        "quantile_01": -0.042646539287068366,
        "quantile_99": 0.053605014504338896,
        "hill_tail_index": 3.572337084734111
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017604047533896168,
        "excess_kurtosis": 11.5802440114006,
        "return_acf_1": -0.1425683346743146,
        "abs_return_acf_1": 0.3987492426682106,
        "abs_return_acf_5": 0.32114184152632513,
        "abs_return_acf_20": 0.21252297097387132,
        "quantile_01": -0.05561619806496895,
        "quantile_99": 0.04063861013718536,
        "hill_tail_index": 2.6011561012029154
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01852727048683136,
        "excess_kurtosis": 5.977262692914147,
        "return_acf_1": -0.14002703353521714,
        "abs_return_acf_1": 0.31186266330878903,
        "abs_return_acf_5": 0.3406032761620233,
        "abs_return_acf_20": 0.2587648378833617,
        "quantile_01": -0.054274594970351225,
        "quantile_99": 0.047517527441563116,
        "hill_tail_index": 2.9437032385946442
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018068649546442984,
        "excess_kurtosis": 4.470392233535567,
        "return_acf_1": -0.1336408435478141,
        "abs_return_acf_1": 0.3508581937685487,
        "abs_return_acf_5": 0.2919503291252045,
        "abs_return_acf_20": 0.23986338785170358,
        "quantile_01": -0.051707068955747316,
        "quantile_99": 0.05407679880314491,
        "hill_tail_index": 3.767584360441564
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016355984771654015,
        "excess_kurtosis": 9.377174284572812,
        "return_acf_1": -0.09007860572167423,
        "abs_return_acf_1": 0.3135101511854959,
        "abs_return_acf_5": 0.21208526068485856,
        "abs_return_acf_20": 0.10113604567858368,
        "quantile_01": -0.04874656032078965,
        "quantile_99": 0.03452406027897194,
        "hill_tail_index": 2.803997974261325
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016575248767856734,
        "excess_kurtosis": 5.419790221054633,
        "return_acf_1": -0.11734758837232417,
        "abs_return_acf_1": 0.22539822033086435,
        "abs_return_acf_5": 0.24019493907204675,
        "abs_return_acf_20": 0.1977067975703735,
        "quantile_01": -0.0525439016335458,
        "quantile_99": 0.04004052620442584,
        "hill_tail_index": 2.599918461471484
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016943015400055605,
        "excess_kurtosis": 6.811545431032938,
        "return_acf_1": -0.15619753102868503,
        "abs_return_acf_1": 0.3202607340586967,
        "abs_return_acf_5": 0.2389301819766856,
        "abs_return_acf_20": 0.15514080713063427,
        "quantile_01": -0.04988958997900169,
        "quantile_99": 0.03830106369843929,
        "hill_tail_index": 2.9548557781319897
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01742880372532471,
        "excess_kurtosis": 13.055371079537707,
        "return_acf_1": -0.12009978505600605,
        "abs_return_acf_1": 0.3874525467069317,
        "abs_return_acf_5": 0.3573181200559503,
        "abs_return_acf_20": 0.1284978021509772,
        "quantile_01": -0.04713069492997171,
        "quantile_99": 0.04681477548056987,
        "hill_tail_index": 2.868151829787168
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017355953253111466,
        "excess_kurtosis": 3.87677718128802,
        "return_acf_1": -0.0895263253728904,
        "abs_return_acf_1": 0.2676261820223528,
        "abs_return_acf_5": 0.22240927180347975,
        "abs_return_acf_20": 0.1484579642216026,
        "quantile_01": -0.049508394128765364,
        "quantile_99": 0.04730794259262264,
        "hill_tail_index": 3.7980796942502795
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017471580578181777,
        "excess_kurtosis": 3.9151870546033507,
        "return_acf_1": -0.12188203851067492,
        "abs_return_acf_1": 0.33534760185274864,
        "abs_return_acf_5": 0.30430124299289535,
        "abs_return_acf_20": 0.27001324539853305,
        "quantile_01": -0.054670969884358614,
        "quantile_99": 0.05031160580967876,
        "hill_tail_index": 4.313602939741624
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.0200617536779083,
        "excess_kurtosis": 8.684652023053319,
        "return_acf_1": -0.1511808643647469,
        "abs_return_acf_1": 0.3782218997884981,
        "abs_return_acf_5": 0.32603400346278105,
        "abs_return_acf_20": 0.27475415882114224,
        "quantile_01": -0.06314762460779993,
        "quantile_99": 0.05794211660680309,
        "hill_tail_index": 2.934189545417122
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018872158321631707,
        "excess_kurtosis": 10.14737964503155,
        "return_acf_1": -0.09583118687208896,
        "abs_return_acf_1": 0.3903401524622521,
        "abs_return_acf_5": 0.39002354426708524,
        "abs_return_acf_20": 0.3157085121898003,
        "quantile_01": -0.061808908102433724,
        "quantile_99": 0.05052346594179429,
        "hill_tail_index": 2.538973309749986
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017139642863115902,
        "excess_kurtosis": 6.321081363290755,
        "return_acf_1": -0.17514220531158353,
        "abs_return_acf_1": 0.29795452109043624,
        "abs_return_acf_5": 0.3193363426392987,
        "abs_return_acf_20": 0.14149550312970868,
        "quantile_01": -0.049083869941855596,
        "quantile_99": 0.0423417680099607,
        "hill_tail_index": 2.4874146939581423
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018978297956478287,
        "excess_kurtosis": 9.217015514320838,
        "return_acf_1": -0.05325070799884376,
        "abs_return_acf_1": 0.3702466474316999,
        "abs_return_acf_5": 0.39059517120184334,
        "abs_return_acf_20": 0.26067752556968515,
        "quantile_01": -0.0725906331212799,
        "quantile_99": 0.04300210362563166,
        "hill_tail_index": 2.5245113106828847
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018881424610463375,
        "excess_kurtosis": 5.185054320114272,
        "return_acf_1": -0.1176756734155315,
        "abs_return_acf_1": 0.2967026182358949,
        "abs_return_acf_5": 0.32120385344377644,
        "abs_return_acf_20": 0.296593163818576,
        "quantile_01": -0.05363260896249666,
        "quantile_99": 0.054695560323054386,
        "hill_tail_index": 3.5793995116588038
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01960873569941926,
        "excess_kurtosis": 16.983496017534158,
        "return_acf_1": -0.11656059917935502,
        "abs_return_acf_1": 0.47289500876408025,
        "abs_return_acf_5": 0.45425593668359776,
        "abs_return_acf_20": 0.2032242981552368,
        "quantile_01": -0.0671510394577292,
        "quantile_99": 0.043459517599394024,
        "hill_tail_index": 2.5025587975460404
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017761805308831338,
        "excess_kurtosis": 10.97349873086982,
        "return_acf_1": -0.11781237121026623,
        "abs_return_acf_1": 0.3823856353053837,
        "abs_return_acf_5": 0.38732417125200896,
        "abs_return_acf_20": 0.22283268122196848,
        "quantile_01": -0.053374309063331404,
        "quantile_99": 0.044268571323834174,
        "hill_tail_index": 2.425801836974016
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01773107892723242,
        "excess_kurtosis": 6.540805143892406,
        "return_acf_1": -0.092978811931618,
        "abs_return_acf_1": 0.4157950060374021,
        "abs_return_acf_5": 0.3631920518875805,
        "abs_return_acf_20": 0.18018245199375316,
        "quantile_01": -0.05950735429624788,
        "quantile_99": 0.04617433158775657,
        "hill_tail_index": 2.8195689030815902
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018117548462314965,
        "excess_kurtosis": 19.231395845462476,
        "return_acf_1": -0.11770719670065606,
        "abs_return_acf_1": 0.3777847901533383,
        "abs_return_acf_5": 0.36857367352734444,
        "abs_return_acf_20": 0.11275303506365941,
        "quantile_01": -0.04882139454674182,
        "quantile_99": 0.03904854880685519,
        "hill_tail_index": 1.8613032554796367
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01986698136241663,
        "excess_kurtosis": 6.196541362485199,
        "return_acf_1": -0.17021302384879908,
        "abs_return_acf_1": 0.32871053936732164,
        "abs_return_acf_5": 0.348800000565831,
        "abs_return_acf_20": 0.3196378954296974,
        "quantile_01": -0.060704044159882384,
        "quantile_99": 0.05821552121156475,
        "hill_tail_index": 3.2439818175205324
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016214633244882003,
        "excess_kurtosis": 8.335028344072605,
        "return_acf_1": -0.05901717522261599,
        "abs_return_acf_1": 0.36734443343481626,
        "abs_return_acf_5": 0.31434021264123513,
        "abs_return_acf_20": 0.12332485557993073,
        "quantile_01": -0.04801019510341919,
        "quantile_99": 0.03884251678286348,
        "hill_tail_index": 2.5518344947128586
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01669089784435698,
        "excess_kurtosis": 6.251315346774669,
        "return_acf_1": -0.11170467086529201,
        "abs_return_acf_1": 0.34173358999728093,
        "abs_return_acf_5": 0.31993008212868385,
        "abs_return_acf_20": 0.1864870482610004,
        "quantile_01": -0.051725358287557054,
        "quantile_99": 0.041465863311407204,
        "hill_tail_index": 3.226267226546241
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01530764039730781,
        "excess_kurtosis": 4.1554182868725045,
        "return_acf_1": -0.08450459417930843,
        "abs_return_acf_1": 0.2427264179244308,
        "abs_return_acf_5": 0.19920370732690978,
        "abs_return_acf_20": 0.1831686614960572,
        "quantile_01": -0.04242719232462906,
        "quantile_99": 0.03587458383248407,
        "hill_tail_index": 2.8358278699214643
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01791014054102493,
        "excess_kurtosis": 5.737939621490897,
        "return_acf_1": -0.15115196989178264,
        "abs_return_acf_1": 0.33838871802628084,
        "abs_return_acf_5": 0.28270196193648234,
        "abs_return_acf_20": 0.3307432345166017,
        "quantile_01": -0.05291008171332916,
        "quantile_99": 0.050041931735334916,
        "hill_tail_index": 3.066045127782031
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018227566373111646,
        "excess_kurtosis": 9.328752406297872,
        "return_acf_1": -0.17521545898058144,
        "abs_return_acf_1": 0.3703522468973891,
        "abs_return_acf_5": 0.3222400281674627,
        "abs_return_acf_20": 0.22443589892854648,
        "quantile_01": -0.0528571944678445,
        "quantile_99": 0.04400782070530675,
        "hill_tail_index": 2.177207638862359
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018138391537844724,
        "excess_kurtosis": 6.933942975721974,
        "return_acf_1": -0.16780174130310427,
        "abs_return_acf_1": 0.3477028467533779,
        "abs_return_acf_5": 0.3376684502448042,
        "abs_return_acf_20": 0.3094192350699616,
        "quantile_01": -0.05564869632997234,
        "quantile_99": 0.058083997207728125,
        "hill_tail_index": 3.228170432165185
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.016916370703323618,
        "excess_kurtosis": 5.18443010726585,
        "return_acf_1": -0.1055236377241061,
        "abs_return_acf_1": 0.26300827261713444,
        "abs_return_acf_5": 0.28934815655358903,
        "abs_return_acf_20": 0.16326234082861854,
        "quantile_01": -0.05710721126641604,
        "quantile_99": 0.04340188944213727,
        "hill_tail_index": 3.3665861349464197
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01726140213441331,
        "excess_kurtosis": 9.763973820321807,
        "return_acf_1": -0.1603640275477012,
        "abs_return_acf_1": 0.38764850584037963,
        "abs_return_acf_5": 0.4362531097506865,
        "abs_return_acf_20": 0.18963247961512067,
        "quantile_01": -0.05091227276025983,
        "quantile_99": 0.04343514392934443,
        "hill_tail_index": 2.7523805851325873
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01589801858317042,
        "excess_kurtosis": 5.21041302811523,
        "return_acf_1": -0.05220662283317881,
        "abs_return_acf_1": 0.30198110546268325,
        "abs_return_acf_5": 0.3135820360377566,
        "abs_return_acf_20": 0.13200533537150858,
        "quantile_01": -0.0487487055431639,
        "quantile_99": 0.03739991436928651,
        "hill_tail_index": 2.76485992070666
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018505814755709882,
        "excess_kurtosis": 2.810742426234139,
        "return_acf_1": -0.0554831166861074,
        "abs_return_acf_1": 0.35558741673797656,
        "abs_return_acf_5": 0.3335446485118788,
        "abs_return_acf_20": 0.3509290679231421,
        "quantile_01": -0.055610171298835255,
        "quantile_99": 0.049037425272429915,
        "hill_tail_index": 4.55791014938855
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
