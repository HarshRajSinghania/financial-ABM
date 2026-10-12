# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27153
Run ID: `e913d405516180f7c647723f56964429c3d6677078b5ef40336ddf80a1d2595f`
Result fingerprint: `70423f6ac3a1ebab0df617040f0e379faccacc47a2d1ec0a5d19e256331a7060`

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
    "equal_weight_sd": -0.7238809523809491,
    "equal_weight_raw": -10.858214285714238,
    "fixed_start_cap_weight_sd": -0.7110750214860067,
    "fixed_start_cap_weight_raw": -10.6661253222901,
    "end_cap_weight_sd": -0.7127822013286866,
    "end_cap_weight_raw": -10.691733019930297
  },
  "full_period_change": {
    "equal_weight_sd": -1.1009047619047572,
    "equal_weight_raw": -16.513571428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0406134259259214,
    "inflation_mean_sd": 0.6961071428571429
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.22850000000000315,
    "equal_weight_raw": 3.4275000000000477,
    "fixed_start_cap_weight_sd": 0.24130593089494579,
    "fixed_start_cap_weight_raw": 3.6195889634241873,
    "end_cap_weight_sd": 0.23959875105226594,
    "end_cap_weight_raw": 3.59398126578399
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7323809523809492,
      "change_raw": -10.985714285714238,
      "decay_adjusted_gain_sd": 0.22000000000000317
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6732142857142825,
      "change_raw": -10.098214285714239,
      "decay_adjusted_gain_sd": 0.2791666666666698
    },
    "small": {
      "count": 18,
      "change_sd": -0.7477976190476158,
      "change_raw": -11.216964285714237,
      "decay_adjusted_gain_sd": 0.2045833333333365
    },
    "large_minus_small_sd": 0.015416666666666523,
    "large_minus_small_raw": 0.23124999999999785
  },
  "inflation": {
    "initial_mean_sd": 0.2881666666666666,
    "final_mean_sd": 0.7235833333333335,
    "mean_sd": 0.512295517624202,
    "mean_absolute_raw_gap": 7.684432764363032,
    "final_absolute_raw_gap": 10.85375,
    "mean_range_fraction": 0.07684432764363032
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.29333333333333333,
    "initial_wealth_share": 0.34047524538557034,
    "final_wealth_share": 0.3444888637507754
  },
  "pricing_slope": {
    "mean": -0.0010122528816438878,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.14993233735747452,
    "real_improvement_cost": 0.11205393608891716,
    "washing_cost": 0.03787840126855735,
    "fine_transfer": 0.007213057886240166,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.15714539524371468,
    "resource_cost_fraction_initial_cap": 0.004997744578582484,
    "private_net_outflow_fraction_initial_cap": 0.005238179841457156,
    "fine_transfer_fraction_initial_cap": 0.0002404352628746722,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0005719063575235753,
    "unapplied_final_day_resource_cost": 0.0006994214192803703
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 45.720623854853514,
    "beneficial_raw_gain_per_resource_cost": 685.8093578228028,
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
    "accrued_cost": 3.020719482849821,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.0445290066593437,
    "accrued_cost_fraction_initial_cap": 0.10069064942832737,
    "mean_contract_rate": 0.04228949059628044,
    "maximum_ledger_error": 4.0657581468206416e-20
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
    "maximum_relative_cash_error": 2.035949392922042e-15,
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
      "minimum": -0.25475524384571446,
      "maximum": -0.08411641284449208,
      "mean": -0.1826405953914603,
      "median": -0.18630732801422073,
      "quantile_05": -0.2249581209028069,
      "quantile_95": -0.13146956946618507
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
      "minimum": 0.30303777413817456,
      "maximum": 0.7267500930279648,
      "mean": 0.5173264851279352,
      "median": 0.5096489164665038,
      "quantile_05": 0.3429536906530974,
      "quantile_95": 0.69842223606901
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
        "daily_volatility": 0.018714453467783224,
        "excess_kurtosis": 5.735647892997537,
        "return_acf_1": -0.15066028573921905,
        "abs_return_acf_1": 0.34682869474788264,
        "abs_return_acf_5": 0.3672188841800713,
        "abs_return_acf_20": 0.30467434650195563,
        "quantile_01": -0.05522519648459469,
        "quantile_99": 0.05103918172928056,
        "hill_tail_index": 3.545357118878545
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017237063632704625,
        "excess_kurtosis": 4.26691968532468,
        "return_acf_1": -0.19318303898395262,
        "abs_return_acf_1": 0.2683983092357691,
        "abs_return_acf_5": 0.2452285572705709,
        "abs_return_acf_20": 0.23893738927501434,
        "quantile_01": -0.04744833781816936,
        "quantile_99": 0.046133700640187736,
        "hill_tail_index": 3.4989148007496835
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017234665624497703,
        "excess_kurtosis": 5.17408058217381,
        "return_acf_1": -0.17304101575463887,
        "abs_return_acf_1": 0.3297168783586465,
        "abs_return_acf_5": 0.1573960728215189,
        "abs_return_acf_20": 0.24436221048254145,
        "quantile_01": -0.04932919781159256,
        "quantile_99": 0.046193582118654784,
        "hill_tail_index": 2.8641695194052725
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017253414658548245,
        "excess_kurtosis": 3.674939708664339,
        "return_acf_1": -0.1827896873871683,
        "abs_return_acf_1": 0.40934929035992335,
        "abs_return_acf_5": 0.3008467729263142,
        "abs_return_acf_20": 0.3355002946045014,
        "quantile_01": -0.04561311001255409,
        "quantile_99": 0.047123139499113016,
        "hill_tail_index": 3.291430613269789
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01795058274782379,
        "excess_kurtosis": 5.31786138971272,
        "return_acf_1": -0.20358722361338646,
        "abs_return_acf_1": 0.2863848042567419,
        "abs_return_acf_5": 0.27248348802679123,
        "abs_return_acf_20": 0.22595640975905035,
        "quantile_01": -0.05253936961602698,
        "quantile_99": 0.048331460637055165,
        "hill_tail_index": 2.5960109643301763
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01601984576824308,
        "excess_kurtosis": 3.1990197670418485,
        "return_acf_1": -0.21186338167866747,
        "abs_return_acf_1": 0.24744008582162894,
        "abs_return_acf_5": 0.2849687248879128,
        "abs_return_acf_20": 0.24212081224392876,
        "quantile_01": -0.043116117561503846,
        "quantile_99": 0.04098651279886824,
        "hill_tail_index": 3.3782307941059817
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017811130523989863,
        "excess_kurtosis": 5.401075400659526,
        "return_acf_1": -0.15394913804865668,
        "abs_return_acf_1": 0.26302780066765014,
        "abs_return_acf_5": 0.3144617902745829,
        "abs_return_acf_20": 0.26343544196197394,
        "quantile_01": -0.05838923734035496,
        "quantile_99": 0.04487157529280215,
        "hill_tail_index": 3.0710805857919206
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017705922845960686,
        "excess_kurtosis": 3.13136045670338,
        "return_acf_1": -0.1297356262135189,
        "abs_return_acf_1": 0.297770575283451,
        "abs_return_acf_5": 0.21769546728857134,
        "abs_return_acf_20": 0.2481131460509688,
        "quantile_01": -0.053157562190386434,
        "quantile_99": 0.05101888955905056,
        "hill_tail_index": 4.698301494530075
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01947834690480938,
        "excess_kurtosis": 9.23502161658814,
        "return_acf_1": -0.2275978099452244,
        "abs_return_acf_1": 0.3352871668719264,
        "abs_return_acf_5": 0.36026287077284486,
        "abs_return_acf_20": 0.29457441594664346,
        "quantile_01": -0.059914578481267744,
        "quantile_99": 0.05882603571356802,
        "hill_tail_index": 3.2804464655939345
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017100535809643175,
        "excess_kurtosis": 4.94738881727371,
        "return_acf_1": -0.19370563611794916,
        "abs_return_acf_1": 0.2618973849276884,
        "abs_return_acf_5": 0.28585640417706637,
        "abs_return_acf_20": 0.15950997807209477,
        "quantile_01": -0.05105025894064175,
        "quantile_99": 0.048312057534235224,
        "hill_tail_index": 3.158546904182623
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01594336900746583,
        "excess_kurtosis": 3.7980185385759127,
        "return_acf_1": -0.15891956885581862,
        "abs_return_acf_1": 0.2018389114321211,
        "abs_return_acf_5": 0.2122995234206848,
        "abs_return_acf_20": 0.21123096912724687,
        "quantile_01": -0.045384873056881034,
        "quantile_99": 0.04099692024516026,
        "hill_tail_index": 3.8893871550877894
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015905469486932552,
        "excess_kurtosis": 1.5663359212687995,
        "return_acf_1": -0.16219929639651054,
        "abs_return_acf_1": 0.19805094556839162,
        "abs_return_acf_5": 0.21630062864941169,
        "abs_return_acf_20": 0.19825266675542533,
        "quantile_01": -0.041197174765963775,
        "quantile_99": 0.04193004959434231,
        "hill_tail_index": 5.181831556509826
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017234635559174948,
        "excess_kurtosis": 3.7302773485128062,
        "return_acf_1": -0.18038939067545623,
        "abs_return_acf_1": 0.23135608876343444,
        "abs_return_acf_5": 0.23010738939775904,
        "abs_return_acf_20": 0.14672089547190278,
        "quantile_01": -0.046282978699835525,
        "quantile_99": 0.045759828288437436,
        "hill_tail_index": 3.4654663920211886
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01731261620110396,
        "excess_kurtosis": 1.9855168783041153,
        "return_acf_1": -0.210306090504081,
        "abs_return_acf_1": 0.24936206368251687,
        "abs_return_acf_5": 0.2616846840502093,
        "abs_return_acf_20": 0.27856066945826646,
        "quantile_01": -0.04999916632807741,
        "quantile_99": 0.04662178645953291,
        "hill_tail_index": 5.422240144726719
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01710026284014812,
        "excess_kurtosis": 2.593654811964255,
        "return_acf_1": -0.16734713866770803,
        "abs_return_acf_1": 0.24530814154187702,
        "abs_return_acf_5": 0.23091159098331726,
        "abs_return_acf_20": 0.2466055649227514,
        "quantile_01": -0.04367395174740463,
        "quantile_99": 0.04758127194392716,
        "hill_tail_index": 4.737615665609866
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017406736304528065,
        "excess_kurtosis": 2.9545605345445694,
        "return_acf_1": -0.21599950483239427,
        "abs_return_acf_1": 0.2578952776753833,
        "abs_return_acf_5": 0.2460154318089439,
        "abs_return_acf_20": 0.21974106980073382,
        "quantile_01": -0.051596049233719646,
        "quantile_99": 0.05012484371598784,
        "hill_tail_index": 4.16867762692862
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01871658246931736,
        "excess_kurtosis": 10.666816141826788,
        "return_acf_1": -0.08411641284449208,
        "abs_return_acf_1": 0.476269675515279,
        "abs_return_acf_5": 0.3881622474259045,
        "abs_return_acf_20": 0.3418956537529224,
        "quantile_01": -0.057166904423609444,
        "quantile_99": 0.054731797649251,
        "hill_tail_index": 2.7984259837009136
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017883454411892995,
        "excess_kurtosis": 5.069353677514364,
        "return_acf_1": -0.22173183429540771,
        "abs_return_acf_1": 0.3455731436807894,
        "abs_return_acf_5": 0.33802782624276767,
        "abs_return_acf_20": 0.2429980750266449,
        "quantile_01": -0.052915329288743713,
        "quantile_99": 0.04902807871524256,
        "hill_tail_index": 3.342933395653872
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017012858958420318,
        "excess_kurtosis": 6.09605704529525,
        "return_acf_1": -0.25475524384571446,
        "abs_return_acf_1": 0.3290130592290297,
        "abs_return_acf_5": 0.25508765113709564,
        "abs_return_acf_20": 0.24437468872956952,
        "quantile_01": -0.04775588587393811,
        "quantile_99": 0.051055855253961654,
        "hill_tail_index": 3.6970940126548797
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017896655312448384,
        "excess_kurtosis": 4.460208159773223,
        "return_acf_1": -0.2127128849499412,
        "abs_return_acf_1": 0.33204321379649077,
        "abs_return_acf_5": 0.22767365547086366,
        "abs_return_acf_20": 0.3340062664177591,
        "quantile_01": -0.05484143262290025,
        "quantile_99": 0.050050893153202075,
        "hill_tail_index": 4.037773693852287
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01759936556094589,
        "excess_kurtosis": 13.827417161599282,
        "return_acf_1": -0.17141381799181876,
        "abs_return_acf_1": 0.3810310252790942,
        "abs_return_acf_5": 0.32796756281881057,
        "abs_return_acf_20": 0.32549564892212207,
        "quantile_01": -0.05159227949243373,
        "quantile_99": 0.045648493174316636,
        "hill_tail_index": 2.5860472802204226
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0192178960815247,
        "excess_kurtosis": 6.207763202906445,
        "return_acf_1": -0.20055289777151594,
        "abs_return_acf_1": 0.3754642786441225,
        "abs_return_acf_5": 0.30854490982758037,
        "abs_return_acf_20": 0.27715321347347577,
        "quantile_01": -0.05446587407261082,
        "quantile_99": 0.0501497342649894,
        "hill_tail_index": 3.4132431199832407
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018270172694524755,
        "excess_kurtosis": 3.8244978020574107,
        "return_acf_1": -0.16617608252052252,
        "abs_return_acf_1": 0.29897074441805177,
        "abs_return_acf_5": 0.3824855678792921,
        "abs_return_acf_20": 0.27225430036707565,
        "quantile_01": -0.05567301943188307,
        "quantile_99": 0.05333965135862414,
        "hill_tail_index": 4.134756317278776
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018413490216270714,
        "excess_kurtosis": 6.257024025743357,
        "return_acf_1": -0.20465727985697998,
        "abs_return_acf_1": 0.2955089649073134,
        "abs_return_acf_5": 0.3430786474814522,
        "abs_return_acf_20": 0.3055235081674338,
        "quantile_01": -0.05359827607358944,
        "quantile_99": 0.0500057810024549,
        "hill_tail_index": 3.366134280201294
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01761641894534605,
        "excess_kurtosis": 3.2245093905197573,
        "return_acf_1": -0.18982496864127313,
        "abs_return_acf_1": 0.27028139805791734,
        "abs_return_acf_5": 0.2869709158304235,
        "abs_return_acf_20": 0.21659021242165163,
        "quantile_01": -0.052215451911550276,
        "quantile_99": 0.04720729694416847,
        "hill_tail_index": 3.8610683826062795
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018135853984924514,
        "excess_kurtosis": 5.640789792165963,
        "return_acf_1": -0.19066122963962548,
        "abs_return_acf_1": 0.3513684055879895,
        "abs_return_acf_5": 0.25715533327536555,
        "abs_return_acf_20": 0.28371652333361114,
        "quantile_01": -0.05307000047231864,
        "quantile_99": 0.05326208260231417,
        "hill_tail_index": 3.4213492719490795
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01774686646945289,
        "excess_kurtosis": 2.738952159013728,
        "return_acf_1": -0.16713182197539894,
        "abs_return_acf_1": 0.3637139743307297,
        "abs_return_acf_5": 0.31332028984066285,
        "abs_return_acf_20": 0.31247052383412155,
        "quantile_01": -0.053782646549981036,
        "quantile_99": 0.049323379799521,
        "hill_tail_index": 4.739001532906593
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.015247027808046593,
        "excess_kurtosis": 3.2332995611079394,
        "return_acf_1": -0.16703498543305148,
        "abs_return_acf_1": 0.22675511040780755,
        "abs_return_acf_5": 0.1665060736181069,
        "abs_return_acf_20": 0.15020444670841102,
        "quantile_01": -0.03814706150719126,
        "quantile_99": 0.03688426895561051,
        "hill_tail_index": 3.6171987944997306
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016895296129335526,
        "excess_kurtosis": 2.9058930064176733,
        "return_acf_1": -0.1995857351220514,
        "abs_return_acf_1": 0.23718451049839978,
        "abs_return_acf_5": 0.2118112733439191,
        "abs_return_acf_20": 0.21222117804943277,
        "quantile_01": -0.04870818065911849,
        "quantile_99": 0.04467703762045443,
        "hill_tail_index": 4.735153831993868
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01721110315198372,
        "excess_kurtosis": 4.760468874365166,
        "return_acf_1": -0.13358883344166592,
        "abs_return_acf_1": 0.30990956885804577,
        "abs_return_acf_5": 0.30399554496526837,
        "abs_return_acf_20": 0.24752934209198027,
        "quantile_01": -0.04747112557196658,
        "quantile_99": 0.045112882163444806,
        "hill_tail_index": 3.321375986901996
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
