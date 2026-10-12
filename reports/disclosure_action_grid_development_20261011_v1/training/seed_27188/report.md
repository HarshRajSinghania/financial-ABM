# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27188
Run ID: `c906dad363cd077786ec2ea89b2bf7af72a15632af73c54fa22ccdb23c275099`
Result fingerprint: `de2edb0023e0b8d71bb79cdcd02bf6590ea71882ad88fef0b05a38f8fb056ca6`

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
    "equal_weight_sd": -0.7231507936507905,
    "equal_weight_raw": -10.847261904761858,
    "fixed_start_cap_weight_sd": -0.7290492492961788,
    "fixed_start_cap_weight_raw": -10.935738739442684,
    "end_cap_weight_sd": -0.7305168172043842,
    "end_cap_weight_raw": -10.957752258065764
  },
  "full_period_change": {
    "equal_weight_sd": -1.1370760979403913,
    "equal_weight_raw": -17.05614146910587
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0425688070610772,
    "inflation_mean_sd": 0.6408095238095237
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19557891969450078,
    "equal_weight_raw": 2.9336837954175126,
    "fixed_start_cap_weight_sd": 0.21681748181232188,
    "fixed_start_cap_weight_raw": 3.2522622271848296,
    "end_cap_weight_sd": 0.21617585839429893,
    "end_cap_weight_raw": 3.2426378759144834
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.721547619047616,
      "change_raw": -10.82321428571424,
      "decay_adjusted_gain_sd": 0.23083333333333625
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7348809523809492,
      "change_raw": -11.023214285714237,
      "decay_adjusted_gain_sd": 0.21750000000000316
    },
    "small": {
      "count": 18,
      "change_sd": -0.717552910052907,
      "change_raw": -10.763293650793605,
      "decay_adjusted_gain_sd": 0.17874264393527706
    },
    "large_minus_small_sd": -0.003994708994708995,
    "large_minus_small_raw": -0.05992063492063493
  },
  "inflation": {
    "initial_mean_sd": 0.31349999999999995,
    "final_mean_sd": 0.6675,
    "mean_sd": 0.5148702470163753,
    "mean_absolute_raw_gap": 7.723053705245628,
    "final_absolute_raw_gap": 10.012499999999998,
    "mean_range_fraction": 0.07723053705245628
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.2,
    "initial_wealth_share": 0.1687781435357597,
    "final_wealth_share": 0.20398327971830313
  },
  "pricing_slope": {
    "mean": -0.0016926569527569394,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.19144681402252728,
    "real_improvement_cost": 0.16097678421149514,
    "washing_cost": 0.030470029811032143,
    "fine_transfer": 0.03094393911242454,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.22239075313495182,
    "resource_cost_fraction_initial_cap": 0.006381560467417577,
    "private_net_outflow_fraction_initial_cap": 0.007413025104498396,
    "fine_transfer_fraction_initial_cap": 0.0010314646370808182,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001145278840227592,
    "unapplied_final_day_resource_cost": 0.0010331610188862791
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 30.647507093769754,
    "beneficial_raw_gain_per_resource_cost": 459.71260640654634,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 2.88451681716509,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.09167365902538654,
    "accrued_cost_fraction_initial_cap": 0.09615056057216968,
    "mean_contract_rate": 0.03970165264915457,
    "maximum_ledger_error": 1.3552527156068805e-19
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
    "price_cap_hits": 26,
    "maximum_relative_cash_error": 1.6003400835760233e-15,
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
      "minimum": -0.24502745225842198,
      "maximum": -0.03279899518144404,
      "mean": -0.14278025975597483,
      "median": -0.1509343364091444,
      "quantile_05": -0.2194538966147486,
      "quantile_95": -0.050850893676998875
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
      "minimum": 0.3056159694278825,
      "maximum": 0.7754722743750144,
      "mean": 0.5172184117363114,
      "median": 0.5155988990128648,
      "quantile_05": 0.3647786458947902,
      "quantile_95": 0.7064167014781657
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
        "daily_volatility": 0.02022890089879704,
        "excess_kurtosis": 6.4976553375310235,
        "return_acf_1": -0.24502745225842198,
        "abs_return_acf_1": 0.4247571362448694,
        "abs_return_acf_5": 0.30958750993988293,
        "abs_return_acf_20": 0.30709102193590226,
        "quantile_01": -0.06419570936485611,
        "quantile_99": 0.06337417928007659,
        "hill_tail_index": 3.2600977938281392
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018613542433700475,
        "excess_kurtosis": 5.418796555451474,
        "return_acf_1": -0.197447362955713,
        "abs_return_acf_1": 0.2507424493745175,
        "abs_return_acf_5": 0.2753849790851394,
        "abs_return_acf_20": 0.26070436032393324,
        "quantile_01": -0.054065756226830276,
        "quantile_99": 0.04847328998713071,
        "hill_tail_index": 3.89473296028788
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018857203072898166,
        "excess_kurtosis": 4.437129174569785,
        "return_acf_1": -0.15929412608931326,
        "abs_return_acf_1": 0.3730655170654457,
        "abs_return_acf_5": 0.28851904553774393,
        "abs_return_acf_20": 0.32334296156092646,
        "quantile_01": -0.05836351760387351,
        "quantile_99": 0.058497304341792254,
        "hill_tail_index": 3.9935051015430054
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02022656208644314,
        "excess_kurtosis": 6.917547263815235,
        "return_acf_1": -0.18384563134399873,
        "abs_return_acf_1": 0.4555805493298927,
        "abs_return_acf_5": 0.4055871590804569,
        "abs_return_acf_20": 0.32131059373641446,
        "quantile_01": -0.07356076285466823,
        "quantile_99": 0.0535423244701223,
        "hill_tail_index": 2.995320630378919
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019299600136669735,
        "excess_kurtosis": 5.944290854063112,
        "return_acf_1": -0.1330575433328423,
        "abs_return_acf_1": 0.3578582766447329,
        "abs_return_acf_5": 0.3405363419887749,
        "abs_return_acf_20": 0.2913656042950276,
        "quantile_01": -0.06415655643127091,
        "quantile_99": 0.05934258224340514,
        "hill_tail_index": 3.8198440517996723
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019197983392290605,
        "excess_kurtosis": 4.636149653729668,
        "return_acf_1": -0.17887624450388312,
        "abs_return_acf_1": 0.2880542841755823,
        "abs_return_acf_5": 0.3192582077613775,
        "abs_return_acf_20": 0.2675869924964779,
        "quantile_01": -0.054184827748839745,
        "quantile_99": 0.06059632261989714,
        "hill_tail_index": 3.9647106717088847
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017578053876031133,
        "excess_kurtosis": 2.925559200510796,
        "return_acf_1": -0.15308760897448717,
        "abs_return_acf_1": 0.1636852582858047,
        "abs_return_acf_5": 0.16331484187681125,
        "abs_return_acf_20": 0.18211691868766297,
        "quantile_01": -0.04815159680507939,
        "quantile_99": 0.0501304109655953,
        "hill_tail_index": 4.220665706729619
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015719339293167663,
        "excess_kurtosis": 1.3674366181856215,
        "return_acf_1": -0.12456040904361071,
        "abs_return_acf_1": 0.20957139018050247,
        "abs_return_acf_5": 0.19401983231897516,
        "abs_return_acf_20": 0.1350398337710279,
        "quantile_01": -0.04163971772915016,
        "quantile_99": 0.04248496112986879,
        "hill_tail_index": 4.883577222504721
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018688582623883232,
        "excess_kurtosis": 3.8114965077110874,
        "return_acf_1": -0.16404995094957847,
        "abs_return_acf_1": 0.2849776329535664,
        "abs_return_acf_5": 0.248251242657035,
        "abs_return_acf_20": 0.33092070604083773,
        "quantile_01": -0.05958512355030015,
        "quantile_99": 0.05247396913424146,
        "hill_tail_index": 4.343517776874823
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020326535551757483,
        "excess_kurtosis": 10.032970044784236,
        "return_acf_1": -0.15807246364647295,
        "abs_return_acf_1": 0.3733186491473922,
        "abs_return_acf_5": 0.2943475411891522,
        "abs_return_acf_20": 0.267790818124256,
        "quantile_01": -0.06717376831189817,
        "quantile_99": 0.05618336303549787,
        "hill_tail_index": 3.1494607029111106
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01655176133026965,
        "excess_kurtosis": 3.929097371911321,
        "return_acf_1": -0.0852018400531481,
        "abs_return_acf_1": 0.16082157715061005,
        "abs_return_acf_5": 0.1976217689760595,
        "abs_return_acf_20": 0.22997580481043475,
        "quantile_01": -0.04493071768874103,
        "quantile_99": 0.04888760680490122,
        "hill_tail_index": 3.9236386659074864
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01702467786343248,
        "excess_kurtosis": 3.3389485618161103,
        "return_acf_1": -0.14878106384380158,
        "abs_return_acf_1": 0.3366192635379348,
        "abs_return_acf_5": 0.27054716550466207,
        "abs_return_acf_20": 0.3261655156030483,
        "quantile_01": -0.0487741683449072,
        "quantile_99": 0.05027815216008551,
        "hill_tail_index": 3.8805963151001026
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022234876722869324,
        "excess_kurtosis": 11.992296324467397,
        "return_acf_1": -0.21644455237790863,
        "abs_return_acf_1": 0.4508674070872304,
        "abs_return_acf_5": 0.4420985063959112,
        "abs_return_acf_20": 0.31433484964867303,
        "quantile_01": -0.07247318376500943,
        "quantile_99": 0.06937289309012488,
        "hill_tail_index": 3.1673143960664354
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018868159955516373,
        "excess_kurtosis": 2.4788653744783913,
        "return_acf_1": -0.12966341794165007,
        "abs_return_acf_1": 0.2885985200501717,
        "abs_return_acf_5": 0.2767011608261133,
        "abs_return_acf_20": 0.2931980524412819,
        "quantile_01": -0.054211072651014464,
        "quantile_99": 0.05322535067528779,
        "hill_tail_index": 4.9784941159165905
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021092385246721884,
        "excess_kurtosis": 9.758119150106046,
        "return_acf_1": -0.08241619083328358,
        "abs_return_acf_1": 0.4896153197127247,
        "abs_return_acf_5": 0.47795107560807104,
        "abs_return_acf_20": 0.34641448112088175,
        "quantile_01": -0.06780625085112493,
        "quantile_99": 0.07051579758094635,
        "hill_tail_index": 3.316220042669818
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01693341760516853,
        "excess_kurtosis": 8.822561739801818,
        "return_acf_1": -0.08573429432115594,
        "abs_return_acf_1": 0.3803196257251301,
        "abs_return_acf_5": 0.32112302787732716,
        "abs_return_acf_20": 0.2557994661374729,
        "quantile_01": -0.05398821271837832,
        "quantile_99": 0.040155449493140816,
        "hill_tail_index": 2.0922033968672955
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01660600637180031,
        "excess_kurtosis": 4.319420461598902,
        "return_acf_1": -0.10329090383013506,
        "abs_return_acf_1": 0.3540434868114509,
        "abs_return_acf_5": 0.3476584737343004,
        "abs_return_acf_20": 0.245576905644651,
        "quantile_01": -0.05106104519625518,
        "quantile_99": 0.0502030746543111,
        "hill_tail_index": 4.0259864356075905
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018680071075185406,
        "excess_kurtosis": 5.460282633781336,
        "return_acf_1": -0.03279899518144404,
        "abs_return_acf_1": 0.2956174925281132,
        "abs_return_acf_5": 0.3056589669681798,
        "abs_return_acf_20": 0.3293811648947405,
        "quantile_01": -0.05475974362713324,
        "quantile_99": 0.05176831299268941,
        "hill_tail_index": 3.8334384891378193
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019598895081196718,
        "excess_kurtosis": 5.906314640842057,
        "return_acf_1": -0.12195182452259139,
        "abs_return_acf_1": 0.344491292975381,
        "abs_return_acf_5": 0.3428900198900741,
        "abs_return_acf_20": 0.2655801151006085,
        "quantile_01": -0.05603786127912207,
        "quantile_99": 0.05779016093996336,
        "hill_tail_index": 3.569208632249432
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020670075783037235,
        "excess_kurtosis": 10.854833355205455,
        "return_acf_1": -0.06958074738123853,
        "abs_return_acf_1": 0.42245896780364095,
        "abs_return_acf_5": 0.40486487262584114,
        "abs_return_acf_20": 0.2882970965603159,
        "quantile_01": -0.059245316918182835,
        "quantile_99": 0.058681684022719845,
        "hill_tail_index": 2.7326981260412495
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019947029005619517,
        "excess_kurtosis": 7.547858599016227,
        "return_acf_1": -0.08494265857327597,
        "abs_return_acf_1": 0.3692636456333554,
        "abs_return_acf_5": 0.3598255146586979,
        "abs_return_acf_20": 0.3429004536194235,
        "quantile_01": -0.06232884764311913,
        "quantile_99": 0.055882615828701375,
        "hill_tail_index": 3.578325644412518
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.018005131777727643,
        "excess_kurtosis": 6.474871853708189,
        "return_acf_1": -0.20822365981473623,
        "abs_return_acf_1": 0.32087318884943283,
        "abs_return_acf_5": 0.2838763472850722,
        "abs_return_acf_20": 0.25295078643398333,
        "quantile_01": -0.05282658797115965,
        "quantile_99": 0.05096970615453305,
        "hill_tail_index": 3.3994143411367417
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021536891821158158,
        "excess_kurtosis": 13.249347617280005,
        "return_acf_1": -0.18533909379155042,
        "abs_return_acf_1": 0.4522197277832526,
        "abs_return_acf_5": 0.45356004372875514,
        "abs_return_acf_20": 0.3452526081778848,
        "quantile_01": -0.07006256845267018,
        "quantile_99": 0.05938765461189513,
        "hill_tail_index": 2.7330221734247524
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01941750015186514,
        "excess_kurtosis": 7.244272340523185,
        "return_acf_1": -0.15756360129448527,
        "abs_return_acf_1": 0.35011152526447437,
        "abs_return_acf_5": 0.30956068593017977,
        "abs_return_acf_20": 0.3097674431191657,
        "quantile_01": -0.06445880702880326,
        "quantile_99": 0.05579000933746667,
        "hill_tail_index": 3.3317758049182133
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019383061978447875,
        "excess_kurtosis": 6.143316316123853,
        "return_acf_1": -0.2219160873539813,
        "abs_return_acf_1": 0.3968727802354002,
        "abs_return_acf_5": 0.31102632207610315,
        "abs_return_acf_20": 0.31658155123265513,
        "quantile_01": -0.057739961446926454,
        "quantile_99": 0.055185688419620266,
        "hill_tail_index": 3.804802383750646
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018536953714581472,
        "excess_kurtosis": 7.5375746041671245,
        "return_acf_1": -0.19976951679481691,
        "abs_return_acf_1": 0.341722987223728,
        "abs_return_acf_5": 0.2753941479155919,
        "abs_return_acf_20": 0.3132598231008908,
        "quantile_01": -0.05357206893701441,
        "quantile_99": 0.050645199285391004,
        "hill_tail_index": 3.0622516927712398
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018738750068020588,
        "excess_kurtosis": 3.7891249617038545,
        "return_acf_1": -0.12857333971672677,
        "abs_return_acf_1": 0.23247126329748,
        "abs_return_acf_5": 0.20647410011676703,
        "abs_return_acf_20": 0.2149015527928119,
        "quantile_01": -0.05425860083085923,
        "quantile_99": 0.05050434851648591,
        "hill_tail_index": 3.81437252531934
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.015561027781183711,
        "excess_kurtosis": 1.5466468052668958,
        "return_acf_1": -0.20523845392220066,
        "abs_return_acf_1": 0.1533843981162497,
        "abs_return_acf_5": 0.1069840932723077,
        "abs_return_acf_20": 0.1049382890659821,
        "quantile_01": -0.03925138290730969,
        "quantile_99": 0.044099602023150476,
        "hill_tail_index": 6.1741470284997675
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02083859846622367,
        "excess_kurtosis": 8.617495963892802,
        "return_acf_1": -0.035526467918984436,
        "abs_return_acf_1": 0.40988054180502614,
        "abs_return_acf_5": 0.4153752402762843,
        "abs_return_acf_20": 0.2926568363107179,
        "quantile_01": -0.07170905991673314,
        "quantile_99": 0.06027145084824282,
        "hill_tail_index": 3.705229555634372
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017253518515957647,
        "excess_kurtosis": 5.233705240641823,
        "return_acf_1": -0.0831322901138092,
        "abs_return_acf_1": 0.2569111287089664,
        "abs_return_acf_5": 0.23817712480853173,
        "abs_return_acf_20": 0.23695811595301908,
        "quantile_01": -0.04751387610760992,
        "quantile_99": 0.05118600364991848,
        "hill_tail_index": 3.8213467532956065
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
