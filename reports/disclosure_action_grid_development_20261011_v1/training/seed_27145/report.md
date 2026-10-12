# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27145
Run ID: `945c0b076eb1ef04c471651d949f48d2c4082da010a2778399c4e2a444644a95`
Result fingerprint: `bba54fce58146ad4eaba624929a523c7143f2e955c37505180d6675185e46fbc`

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
    "equal_weight_sd": -0.6597357289207739,
    "equal_weight_raw": -9.896035933811607,
    "fixed_start_cap_weight_sd": -0.6665132321172249,
    "fixed_start_cap_weight_raw": -9.997698481758373,
    "end_cap_weight_sd": -0.6590526654500606,
    "end_cap_weight_raw": -9.885789981750909
  },
  "full_period_change": {
    "equal_weight_sd": -1.0565928717779152,
    "equal_weight_raw": -15.848893076668727
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0024374564893839,
    "inflation_mean_sd": 0.7074136904761905
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.27383333333333654,
    "equal_weight_raw": 4.107500000000046,
    "fixed_start_cap_weight_sd": 0.27215264129405453,
    "fixed_start_cap_weight_raw": 4.082289619410817,
    "end_cap_weight_sd": 0.28174516379929976,
    "end_cap_weight_raw": 4.226177456989496
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8232142857142826,
      "change_raw": -12.348214285714239,
      "decay_adjusted_gain_sd": 0.12916666666666984
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5613413186248098,
      "change_raw": -8.420119779372147,
      "decay_adjusted_gain_sd": 0.32833333333333614
    },
    "small": {
      "count": 18,
      "change_sd": -0.6816865079365046,
      "change_raw": -10.22529761904757,
      "decay_adjusted_gain_sd": 0.2706944444444477
    },
    "large_minus_small_sd": -0.14152777777777792,
    "large_minus_small_raw": -2.1229166666666686
  },
  "inflation": {
    "initial_mean_sd": 0.3596666666666667,
    "final_mean_sd": 0.6842500000000001,
    "mean_sd": 0.5560818068276437,
    "mean_absolute_raw_gap": 8.341227102414656,
    "final_absolute_raw_gap": 10.26375,
    "mean_range_fraction": 0.08341227102414656
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.16666666666666666,
    "initial_wealth_share": 0.17681592696946533,
    "final_wealth_share": 0.1896673876202184
  },
  "pricing_slope": {
    "mean": -0.0014263511237108937,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.04710151383741846,
    "real_improvement_cost": 0.03670939377400079,
    "washing_cost": 0.010392120063417672,
    "fine_transfer": 0.020991176884146222,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06809269072156468,
    "resource_cost_fraction_initial_cap": 0.001570050461247282,
    "private_net_outflow_fraction_initial_cap": 0.0022697563573854896,
    "fine_transfer_fraction_initial_cap": 0.0006997058961382075,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0036411695968174922,
    "unapplied_final_day_resource_cost": 0.0007577830295177377
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 174.4105301658887,
    "beneficial_raw_gain_per_resource_cost": 2616.1579524883305,
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
    "accrued_cost": 2.863689501168687,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.11250097502178931,
    "accrued_cost_fraction_initial_cap": 0.0954563167056229,
    "mean_contract_rate": 0.040454779054897284,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 2.760192752251332e-15,
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
      "minimum": -0.22196258845588865,
      "maximum": -0.04640559225740607,
      "mean": -0.11408766380326546,
      "median": -0.10775145376869992,
      "quantile_05": -0.17340084752511617,
      "quantile_95": -0.0610643328637081
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
      "minimum": 0.2719489294618907,
      "maximum": 0.7719807982186944,
      "mean": 0.5115644220547495,
      "median": 0.4988682483779132,
      "quantile_05": 0.3264740169433081,
      "quantile_95": 0.7018392885065562
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
        "daily_volatility": 0.01638095349001992,
        "excess_kurtosis": 2.454604780957352,
        "return_acf_1": -0.11459883536055072,
        "abs_return_acf_1": 0.22708750819944257,
        "abs_return_acf_5": 0.1524489438248629,
        "abs_return_acf_20": 0.22386315270209436,
        "quantile_01": -0.04710101544550374,
        "quantile_99": 0.045491365367851956,
        "hill_tail_index": 4.824041572662795
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018636381178964163,
        "excess_kurtosis": 5.686168724536561,
        "return_acf_1": -0.11224534604136163,
        "abs_return_acf_1": 0.293758883382281,
        "abs_return_acf_5": 0.258669891599696,
        "abs_return_acf_20": 0.276778839983565,
        "quantile_01": -0.06533215772509561,
        "quantile_99": 0.04917509381230166,
        "hill_tail_index": 3.330397432841823
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019348817298461246,
        "excess_kurtosis": 9.83938908718754,
        "return_acf_1": -0.17235785508221502,
        "abs_return_acf_1": 0.3237508773853441,
        "abs_return_acf_5": 0.3712228021723846,
        "abs_return_acf_20": 0.19371063208233416,
        "quantile_01": -0.061041575726906,
        "quantile_99": 0.050401291425598044,
        "hill_tail_index": 2.4585350981081606
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019320554105914992,
        "excess_kurtosis": 14.33135174639434,
        "return_acf_1": -0.0923361344770601,
        "abs_return_acf_1": 0.2691948907066176,
        "abs_return_acf_5": 0.36245812230161956,
        "abs_return_acf_20": 0.21651863970391463,
        "quantile_01": -0.0624367865117443,
        "quantile_99": 0.052221356320952525,
        "hill_tail_index": 2.4091680014628234
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02076928945542069,
        "excess_kurtosis": 11.166763148421476,
        "return_acf_1": -0.10765795609263423,
        "abs_return_acf_1": 0.35233588473192035,
        "abs_return_acf_5": 0.3554648485029502,
        "abs_return_acf_20": 0.2863470329625334,
        "quantile_01": -0.07206475296531936,
        "quantile_99": 0.05286217037422847,
        "hill_tail_index": 2.6474142040174864
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0197318563810596,
        "excess_kurtosis": 11.941005286979367,
        "return_acf_1": -0.12459374331545044,
        "abs_return_acf_1": 0.3312559450861876,
        "abs_return_acf_5": 0.3844790683970474,
        "abs_return_acf_20": 0.17676655938891925,
        "quantile_01": -0.06810918323067666,
        "quantile_99": 0.04830048762396973,
        "hill_tail_index": 1.9871317979674803
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018495842970921036,
        "excess_kurtosis": 6.00238512167865,
        "return_acf_1": -0.10784495144476561,
        "abs_return_acf_1": 0.24220060376842165,
        "abs_return_acf_5": 0.3014797369621538,
        "abs_return_acf_20": 0.20507606683386495,
        "quantile_01": -0.05672512562752248,
        "quantile_99": 0.04612879623713154,
        "hill_tail_index": 3.364781480975722
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022288251991276976,
        "excess_kurtosis": 12.380857628221838,
        "return_acf_1": -0.05280625947560506,
        "abs_return_acf_1": 0.3996053139078378,
        "abs_return_acf_5": 0.3769835116757079,
        "abs_return_acf_20": 0.32531385805518115,
        "quantile_01": -0.07856408985743746,
        "quantile_99": 0.05986135635385081,
        "hill_tail_index": 2.8395115803508872
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017404797074662564,
        "excess_kurtosis": 11.469347873853604,
        "return_acf_1": -0.12022315608579527,
        "abs_return_acf_1": 0.3279714960377569,
        "abs_return_acf_5": 0.22246758503905198,
        "abs_return_acf_20": 0.31993494472970113,
        "quantile_01": -0.045159240275277866,
        "quantile_99": 0.04491071939460599,
        "hill_tail_index": 2.089491971012121
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01744292504464419,
        "excess_kurtosis": 4.6487236133014935,
        "return_acf_1": -0.08439238165000917,
        "abs_return_acf_1": 0.3513760416453417,
        "abs_return_acf_5": 0.2693286769746691,
        "abs_return_acf_20": 0.27531884436861265,
        "quantile_01": -0.0553548050394966,
        "quantile_99": 0.04790226037129318,
        "hill_tail_index": 3.486860569893352
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021660463729720494,
        "excess_kurtosis": 11.90193560241239,
        "return_acf_1": -0.07656258319012903,
        "abs_return_acf_1": 0.31108107596202683,
        "abs_return_acf_5": 0.34196556417841634,
        "abs_return_acf_20": 0.2277999974442924,
        "quantile_01": -0.06376297144789028,
        "quantile_99": 0.05396035117809255,
        "hill_tail_index": 2.6818798455902644
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020259333735121288,
        "excess_kurtosis": 12.425191260105906,
        "return_acf_1": -0.10194734578535013,
        "abs_return_acf_1": 0.4475522930311193,
        "abs_return_acf_5": 0.4837963492334152,
        "abs_return_acf_20": 0.24587939142473633,
        "quantile_01": -0.06443777793743473,
        "quantile_99": 0.05205973716547335,
        "hill_tail_index": 2.644194651173334
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021792416098589746,
        "excess_kurtosis": 17.26650989671316,
        "return_acf_1": -0.10752134623493985,
        "abs_return_acf_1": 0.3956374424133923,
        "abs_return_acf_5": 0.3803625217456917,
        "abs_return_acf_20": 0.23750972173139662,
        "quantile_01": -0.07197774216602681,
        "quantile_99": 0.055196243864094045,
        "hill_tail_index": 2.1938278120306705
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01783253181880848,
        "excess_kurtosis": 7.052755959750655,
        "return_acf_1": -0.08172540943677008,
        "abs_return_acf_1": 0.3573614072841331,
        "abs_return_acf_5": 0.2778914188966315,
        "abs_return_acf_20": 0.21076358252249996,
        "quantile_01": -0.04938410084626133,
        "quantile_99": 0.04760312269263307,
        "hill_tail_index": 3.2748435264560984
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020618230020379234,
        "excess_kurtosis": 9.057147839918697,
        "return_acf_1": -0.07115753367138948,
        "abs_return_acf_1": 0.35916251185194986,
        "abs_return_acf_5": 0.3819648906281205,
        "abs_return_acf_20": 0.3019910728698976,
        "quantile_01": -0.07493119247780111,
        "quantile_99": 0.06511582171986752,
        "hill_tail_index": 3.253009920657123
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020774436994842885,
        "excess_kurtosis": 19.41233454171639,
        "return_acf_1": -0.04640559225740607,
        "abs_return_acf_1": 0.38634672448203966,
        "abs_return_acf_5": 0.40961121958458463,
        "abs_return_acf_20": 0.22629898680298857,
        "quantile_01": -0.06270803073430026,
        "quantile_99": 0.04541486962278191,
        "hill_tail_index": 1.7193184834717317
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017938891473243197,
        "excess_kurtosis": 4.900068103700426,
        "return_acf_1": -0.10253249112517134,
        "abs_return_acf_1": 0.33127072124574536,
        "abs_return_acf_5": 0.3217579067523805,
        "abs_return_acf_20": 0.27141040143825557,
        "quantile_01": -0.059188496579073005,
        "quantile_99": 0.04872334693560757,
        "hill_tail_index": 3.1957134077235536
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018826270227184368,
        "excess_kurtosis": 5.586516684497838,
        "return_acf_1": -0.15389010204162443,
        "abs_return_acf_1": 0.31442466178600165,
        "abs_return_acf_5": 0.32727540543212014,
        "abs_return_acf_20": 0.24734200711303794,
        "quantile_01": -0.05787186410260174,
        "quantile_99": 0.0506142822001707,
        "hill_tail_index": 3.16303486471968
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01756089706491536,
        "excess_kurtosis": 6.39198687444676,
        "return_acf_1": -0.1243219979295708,
        "abs_return_acf_1": 0.3619897300053773,
        "abs_return_acf_5": 0.41335320475167714,
        "abs_return_acf_20": 0.3059194871274246,
        "quantile_01": -0.05470321262468399,
        "quantile_99": 0.04952878549346858,
        "hill_tail_index": 3.1991563255915194
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021154878592029008,
        "excess_kurtosis": 15.358041883473131,
        "return_acf_1": -0.22196258845588865,
        "abs_return_acf_1": 0.4256551692207373,
        "abs_return_acf_5": 0.319081639406541,
        "abs_return_acf_20": 0.3163120797717946,
        "quantile_01": -0.06867826225887316,
        "quantile_99": 0.058365633009493025,
        "hill_tail_index": 2.4855602371423955
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01974877763996983,
        "excess_kurtosis": 14.010051822547915,
        "return_acf_1": -0.14699639650215782,
        "abs_return_acf_1": 0.3548899140262525,
        "abs_return_acf_5": 0.2936399463259469,
        "abs_return_acf_20": 0.2181340966886144,
        "quantile_01": -0.06958025708522556,
        "quantile_99": 0.049743367458725395,
        "hill_tail_index": 2.6889493017808648
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018813932774176298,
        "excess_kurtosis": 8.191067840490874,
        "return_acf_1": -0.16641826644665944,
        "abs_return_acf_1": 0.38731474319847914,
        "abs_return_acf_5": 0.30341783233437536,
        "abs_return_acf_20": 0.23746870445688528,
        "quantile_01": -0.06410271264691943,
        "quantile_99": 0.05693518922238569,
        "hill_tail_index": 3.0697416116549725
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.016677275165261022,
        "excess_kurtosis": 2.6228097487578355,
        "return_acf_1": -0.09837884023474525,
        "abs_return_acf_1": 0.23762328818614945,
        "abs_return_acf_5": 0.18699514944650733,
        "abs_return_acf_20": 0.16262447375645406,
        "quantile_01": -0.048284669235933386,
        "quantile_99": 0.04645266583905655,
        "hill_tail_index": 5.086275318689215
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022089382452824134,
        "excess_kurtosis": 13.138372566525618,
        "return_acf_1": -0.1742542049783989,
        "abs_return_acf_1": 0.43246455137198636,
        "abs_return_acf_5": 0.4632332753192012,
        "abs_return_acf_20": 0.26607792021862936,
        "quantile_01": -0.07035353135070861,
        "quantile_99": 0.05476293744637921,
        "hill_tail_index": 2.4806012404167084
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01540883757664722,
        "excess_kurtosis": 1.8281878124936766,
        "return_acf_1": -0.08255534569703447,
        "abs_return_acf_1": 0.20698828625235738,
        "abs_return_acf_5": 0.15263312967543388,
        "abs_return_acf_20": 0.19692830184540155,
        "quantile_01": -0.04651663278014118,
        "quantile_99": 0.03715559628390986,
        "hill_tail_index": 5.071413658641448
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017280036872692344,
        "excess_kurtosis": 1.7206464947429252,
        "return_acf_1": -0.1420672116842749,
        "abs_return_acf_1": 0.27055582145036905,
        "abs_return_acf_5": 0.2094996869940822,
        "abs_return_acf_20": 0.19813481753763582,
        "quantile_01": -0.04710304649059387,
        "quantile_99": 0.04623176286318192,
        "hill_tail_index": 5.972549784207294
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01814668586939369,
        "excess_kurtosis": 3.370523290367493,
        "return_acf_1": -0.12603012490090185,
        "abs_return_acf_1": 0.28634686331509246,
        "abs_return_acf_5": 0.2723248879121451,
        "abs_return_acf_20": 0.19742519605151937,
        "quantile_01": -0.05321002440795154,
        "quantile_99": 0.046411367011617216,
        "hill_tail_index": 3.8161857791102105
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019373601840285207,
        "excess_kurtosis": 16.69830796989242,
        "return_acf_1": -0.10531323819914229,
        "abs_return_acf_1": 0.22648338258382195,
        "abs_return_acf_5": 0.3469872300539939,
        "abs_return_acf_20": 0.16765120467673067,
        "quantile_01": -0.06460687073398798,
        "quantile_99": 0.04397748659721505,
        "hill_tail_index": 1.8980859976001894
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018484307953524248,
        "excess_kurtosis": 7.148516628507908,
        "return_acf_1": -0.1274517494248168,
        "abs_return_acf_1": 0.335155343646698,
        "abs_return_acf_5": 0.3796117678542142,
        "abs_return_acf_20": 0.23203451710653503,
        "quantile_01": -0.0657761398579405,
        "quantile_99": 0.05160928967409803,
        "hill_tail_index": 2.9699284404535993
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019969989295173997,
        "excess_kurtosis": 9.460166214515464,
        "return_acf_1": -0.07608092687614537,
        "abs_return_acf_1": 0.39853439597902157,
        "abs_return_acf_5": 0.444964493815674,
        "abs_return_acf_20": 0.27437794862601117,
        "quantile_01": -0.06385375094901752,
        "quantile_99": 0.053445824410445805,
        "hill_tail_index": 2.729400623202979
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
