# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27144
Run ID: `b25502119fef96ba7616e274e9d51b7d0bde12135d78a130ab9f81d63f9f3edb`
Result fingerprint: `24279d6347fe04bd0373444cd2032bce58579776c67ff17e8fae5606d0536368`

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
    "equal_weight_sd": -0.6967142857142824,
    "equal_weight_raw": -10.450714285714236,
    "fixed_start_cap_weight_sd": -0.7045514892681486,
    "fixed_start_cap_weight_raw": -10.568272339022228,
    "end_cap_weight_sd": -0.7170362572989365,
    "end_cap_weight_raw": -10.755543859484044
  },
  "full_period_change": {
    "equal_weight_sd": -1.0773214285714237,
    "equal_weight_raw": -16.159821428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0261610449735403,
    "inflation_mean_sd": 0.7587013888888888
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.25566666666666993,
    "equal_weight_raw": 3.8350000000000484,
    "fixed_start_cap_weight_sd": 0.24782946311280385,
    "fixed_start_cap_weight_raw": 3.717441946692057,
    "end_cap_weight_sd": 0.23534469508201605,
    "end_cap_weight_raw": 3.5301704262302414
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7165476190476157,
      "change_raw": -10.748214285714235,
      "decay_adjusted_gain_sd": 0.2358333333333367
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6790476190476158,
      "change_raw": -10.185714285714237,
      "decay_adjusted_gain_sd": 0.2733333333333366
    },
    "small": {
      "count": 18,
      "change_sd": -0.7022420634920603,
      "change_raw": -10.533630952380905,
      "decay_adjusted_gain_sd": 0.25013888888889213
    },
    "large_minus_small_sd": -0.01430555555555535,
    "large_minus_small_raw": -0.21458333333333024
  },
  "inflation": {
    "initial_mean_sd": 0.3688333333333333,
    "final_mean_sd": 0.7710833333333333,
    "mean_sd": 0.6012790036081044,
    "mean_absolute_raw_gap": 9.019185054121564,
    "final_absolute_raw_gap": 11.56625,
    "mean_range_fraction": 0.09019185054121565
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.30058699717488,
    "final_wealth_share": 0.36715263613536614
  },
  "pricing_slope": {
    "mean": -0.0021517939638746398,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.042513801978215825,
    "real_improvement_cost": 0.030870749255535335,
    "washing_cost": 0.011643052722680482,
    "fine_transfer": 0.02031855012044177,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06283235209865759,
    "resource_cost_fraction_initial_cap": 0.0014171267326071935,
    "private_net_outflow_fraction_initial_cap": 0.002094411736621919,
    "fine_transfer_fraction_initial_cap": 0.0006772850040147254,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00024944973022433706,
    "unapplied_final_day_resource_cost": 0.0010240213632234428
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 180.41199900047104,
    "beneficial_raw_gain_per_resource_cost": 2706.1799850070656,
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
    "accrued_cost": 3.0092058336608645,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.0330153574703876,
    "accrued_cost_fraction_initial_cap": 0.10030686112202877,
    "mean_contract_rate": 0.04216518607478465,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 13,
    "maximum_relative_cash_error": 2.4936623257501684e-15,
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
      "minimum": -0.2229252786347549,
      "maximum": -0.07573617659077234,
      "mean": -0.16020528273361612,
      "median": -0.15694771345924835,
      "quantile_05": -0.22219000530224797,
      "quantile_95": -0.10554835790439746
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
      "minimum": 0.6114149611609533,
      "maximum": 0.8374498118484377,
      "mean": 0.7620934942233717,
      "median": 0.7645039410105203,
      "quantile_05": 0.6926274007209967,
      "quantile_95": 0.8108127638016467
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
        "daily_volatility": 0.019975248621251784,
        "excess_kurtosis": 27.127181443664625,
        "return_acf_1": -0.13420929884241747,
        "abs_return_acf_1": 0.3359147441896426,
        "abs_return_acf_5": 0.2588922846073796,
        "abs_return_acf_20": 0.29598231379384543,
        "quantile_01": -0.053553911286759445,
        "quantile_99": 0.05977785039477646,
        "hill_tail_index": 2.420575637388185
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021693239959463415,
        "excess_kurtosis": 30.229832903050628,
        "return_acf_1": -0.12399767117877636,
        "abs_return_acf_1": 0.393149480732681,
        "abs_return_acf_5": 0.30195528735155575,
        "abs_return_acf_20": 0.3016914417127982,
        "quantile_01": -0.06505230636093977,
        "quantile_99": 0.05954799606857588,
        "hill_tail_index": 2.5014815402430717
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022640932089455293,
        "excess_kurtosis": 30.376288656594376,
        "return_acf_1": -0.22154863611371203,
        "abs_return_acf_1": 0.44685624762792536,
        "abs_return_acf_5": 0.3514812827216799,
        "abs_return_acf_20": 0.33127103101096966,
        "quantile_01": -0.07469367302156418,
        "quantile_99": 0.058134948257006616,
        "hill_tail_index": 2.0845158736605516
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01904441467418762,
        "excess_kurtosis": 26.51104513147017,
        "return_acf_1": -0.13511743062656706,
        "abs_return_acf_1": 0.32879176142011707,
        "abs_return_acf_5": 0.16913887395920307,
        "abs_return_acf_20": 0.23686165683379862,
        "quantile_01": -0.04722083452105438,
        "quantile_99": 0.05392273076105651,
        "hill_tail_index": 2.254962396094216
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017934430214339717,
        "excess_kurtosis": 23.091373546271857,
        "return_acf_1": -0.2229252786347549,
        "abs_return_acf_1": 0.3471839445508653,
        "abs_return_acf_5": 0.20372082009573747,
        "abs_return_acf_20": 0.2960777842981874,
        "quantile_01": -0.054104078965277316,
        "quantile_99": 0.0504225779168902,
        "hill_tail_index": 2.678053729865282
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020893025360726274,
        "excess_kurtosis": 24.12729477873905,
        "return_acf_1": -0.1569640707114365,
        "abs_return_acf_1": 0.404582510319971,
        "abs_return_acf_5": 0.3032950133329244,
        "abs_return_acf_20": 0.33684593078591496,
        "quantile_01": -0.05814912348711794,
        "quantile_99": 0.056013635372249855,
        "hill_tail_index": 2.2687391087926354
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019260804739072802,
        "excess_kurtosis": 23.986676862377024,
        "return_acf_1": -0.15693135620706022,
        "abs_return_acf_1": 0.3676122026284424,
        "abs_return_acf_5": 0.2476831007724921,
        "abs_return_acf_20": 0.34198015641534996,
        "quantile_01": -0.05943368897947314,
        "quantile_99": 0.05298482065250552,
        "hill_tail_index": 2.0023009912548737
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020785895234462476,
        "excess_kurtosis": 23.30576483846383,
        "return_acf_1": -0.16756454775138077,
        "abs_return_acf_1": 0.3655455124950703,
        "abs_return_acf_5": 0.32855098434501584,
        "abs_return_acf_20": 0.321469861358166,
        "quantile_01": -0.06375427271693386,
        "quantile_99": 0.05214841426894197,
        "hill_tail_index": 1.8728725399182418
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021171795772996726,
        "excess_kurtosis": 20.746411996631963,
        "return_acf_1": -0.18116318861884093,
        "abs_return_acf_1": 0.41023306142302784,
        "abs_return_acf_5": 0.34678467420064507,
        "abs_return_acf_20": 0.3120754507340867,
        "quantile_01": -0.06563315667109854,
        "quantile_99": 0.057505416417003366,
        "hill_tail_index": 2.4350561276833256
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019205184983619436,
        "excess_kurtosis": 17.206865675205346,
        "return_acf_1": -0.10104579695292949,
        "abs_return_acf_1": 0.34022115924196494,
        "abs_return_acf_5": 0.29593081148503236,
        "abs_return_acf_20": 0.28650170608474784,
        "quantile_01": -0.05881468752506495,
        "quantile_99": 0.05864417812421436,
        "hill_tail_index": 2.5225869916256647
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021808920886422924,
        "excess_kurtosis": 31.993677697892807,
        "return_acf_1": -0.21985926792950208,
        "abs_return_acf_1": 0.47846676491426243,
        "abs_return_acf_5": 0.3294957955343903,
        "abs_return_acf_20": 0.29712622435196007,
        "quantile_01": -0.07637872402142404,
        "quantile_99": 0.05551148210207699,
        "hill_tail_index": 2.050576732674098
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02027762081064611,
        "excess_kurtosis": 26.423756133629436,
        "return_acf_1": -0.12439636196131158,
        "abs_return_acf_1": 0.3520592499500666,
        "abs_return_acf_5": 0.3029469999925389,
        "abs_return_acf_20": 0.3107165649246745,
        "quantile_01": -0.0549089132815231,
        "quantile_99": 0.05858717141258803,
        "hill_tail_index": 2.448167889884082
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02210820829063611,
        "excess_kurtosis": 25.935537429586113,
        "return_acf_1": -0.19694244460485671,
        "abs_return_acf_1": 0.4310168592552991,
        "abs_return_acf_5": 0.3155944877972875,
        "abs_return_acf_20": 0.3363639938201788,
        "quantile_01": -0.07328385215890458,
        "quantile_99": 0.06744506996394971,
        "hill_tail_index": 2.875727874148842
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02103614773905935,
        "excess_kurtosis": 16.340229103249655,
        "return_acf_1": -0.16090328556100542,
        "abs_return_acf_1": 0.3882583953707603,
        "abs_return_acf_5": 0.3080267946174571,
        "abs_return_acf_20": 0.29380168985272315,
        "quantile_01": -0.06643646471278496,
        "quantile_99": 0.06183890496471924,
        "hill_tail_index": 3.457392090154041
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018385856402057876,
        "excess_kurtosis": 27.72074232764937,
        "return_acf_1": -0.16249926720768998,
        "abs_return_acf_1": 0.22429031877188976,
        "abs_return_acf_5": 0.15953142492066208,
        "abs_return_acf_20": 0.24051392992234177,
        "quantile_01": -0.04997262936335255,
        "quantile_99": 0.04632483166972475,
        "hill_tail_index": 2.1835136364947187
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019890125405491538,
        "excess_kurtosis": 28.603844801550142,
        "return_acf_1": -0.1611652906721755,
        "abs_return_acf_1": 0.3255101142102627,
        "abs_return_acf_5": 0.2666979968579432,
        "abs_return_acf_20": 0.33596548939688964,
        "quantile_01": -0.06153565128912225,
        "quantile_99": 0.047847054837728116,
        "hill_tail_index": 2.0398099746804395
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019831520833974763,
        "excess_kurtosis": 26.35435691076225,
        "return_acf_1": -0.15538268231213442,
        "abs_return_acf_1": 0.3008723349485236,
        "abs_return_acf_5": 0.27057792004743275,
        "abs_return_acf_20": 0.30517366534537316,
        "quantile_01": -0.05644673862772831,
        "quantile_99": 0.049093747303589605,
        "hill_tail_index": 2.481027374675512
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019838314007507702,
        "excess_kurtosis": 23.212551627861185,
        "return_acf_1": -0.14204297570964677,
        "abs_return_acf_1": 0.3224170623728484,
        "abs_return_acf_5": 0.28592869689312583,
        "abs_return_acf_20": 0.30623095597543715,
        "quantile_01": -0.056634008070120964,
        "quantile_99": 0.04993095833681498,
        "hill_tail_index": 2.5205923050609442
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018754526683402217,
        "excess_kurtosis": 17.31521651095216,
        "return_acf_1": -0.18180232432702284,
        "abs_return_acf_1": 0.3845613472589413,
        "abs_return_acf_5": 0.40325832782210413,
        "abs_return_acf_20": 0.24320397016973078,
        "quantile_01": -0.05215610230978096,
        "quantile_99": 0.05688082934753712,
        "hill_tail_index": 2.3295673544371964
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020557465679222356,
        "excess_kurtosis": 23.89389717636669,
        "return_acf_1": -0.11105148795619156,
        "abs_return_acf_1": 0.38140503911694734,
        "abs_return_acf_5": 0.3138291836762331,
        "abs_return_acf_20": 0.31044554782649847,
        "quantile_01": -0.050724042623718046,
        "quantile_99": 0.05814938053788834,
        "hill_tail_index": 2.149794500195435
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01793988546120781,
        "excess_kurtosis": 22.094184196153915,
        "return_acf_1": -0.14888379826110465,
        "abs_return_acf_1": 0.35259868865277716,
        "abs_return_acf_5": 0.24228779633285585,
        "abs_return_acf_20": 0.2778862937529714,
        "quantile_01": -0.04843927939745162,
        "quantile_99": 0.04489920501197495,
        "hill_tail_index": 2.2836130538112553
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019242465661813157,
        "excess_kurtosis": 29.00658463030839,
        "return_acf_1": -0.13620871762174266,
        "abs_return_acf_1": 0.30659884824606576,
        "abs_return_acf_5": 0.28862831834955205,
        "abs_return_acf_20": 0.2723167643932252,
        "quantile_01": -0.050192352904628965,
        "quantile_99": 0.05591699130541331,
        "hill_tail_index": 2.625991535574133
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01994899483617333,
        "excess_kurtosis": 31.226765798094405,
        "return_acf_1": -0.2227147619110501,
        "abs_return_acf_1": 0.352934364988519,
        "abs_return_acf_5": 0.23179683768298306,
        "abs_return_acf_20": 0.2760213608738081,
        "quantile_01": -0.05608897214463239,
        "quantile_99": 0.05413577832404219,
        "hill_tail_index": 2.2967802134945874
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018327469218453143,
        "excess_kurtosis": 28.854906757827898,
        "return_acf_1": -0.17969192976262857,
        "abs_return_acf_1": 0.3602869255754796,
        "abs_return_acf_5": 0.3051433723801322,
        "abs_return_acf_20": 0.19661067137472263,
        "quantile_01": -0.04821128601773524,
        "quantile_99": 0.048545628279602474,
        "hill_tail_index": 1.989621073811526
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021209457412395733,
        "excess_kurtosis": 24.583946853809877,
        "return_acf_1": -0.1906097811039185,
        "abs_return_acf_1": 0.42247612681657626,
        "abs_return_acf_5": 0.3437501280159422,
        "abs_return_acf_20": 0.31611910603073073,
        "quantile_01": -0.06931242411796598,
        "quantile_99": 0.06364479562857302,
        "hill_tail_index": 2.1980862343333953
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02113946027530359,
        "excess_kurtosis": 23.254666738586458,
        "return_acf_1": -0.07573617659077234,
        "abs_return_acf_1": 0.3014775742422778,
        "abs_return_acf_5": 0.35874352691936173,
        "abs_return_acf_20": 0.3548795383411114,
        "quantile_01": -0.06622285910380282,
        "quantile_99": 0.057169458583367534,
        "hill_tail_index": 2.281145785417922
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019148920004841696,
        "excess_kurtosis": 22.069359898155497,
        "return_acf_1": -0.1529486745102003,
        "abs_return_acf_1": 0.3227538468008212,
        "abs_return_acf_5": 0.2824294950408618,
        "abs_return_acf_20": 0.29203597706181494,
        "quantile_01": -0.05260697716302881,
        "quantile_99": 0.050997153923716766,
        "hill_tail_index": 2.332212571173079
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02132015254086543,
        "excess_kurtosis": 22.388038298606023,
        "return_acf_1": -0.15123584808215343,
        "abs_return_acf_1": 0.37435721637516894,
        "abs_return_acf_5": 0.29653930168094805,
        "abs_return_acf_20": 0.2690486101024863,
        "quantile_01": -0.058739566672351334,
        "quantile_99": 0.06615522984788268,
        "hill_tail_index": 2.108010520537052
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018177026263915763,
        "excess_kurtosis": 18.801075663638482,
        "return_acf_1": -0.18625224900057524,
        "abs_return_acf_1": 0.32678716223421594,
        "abs_return_acf_5": 0.25238773687355953,
        "abs_return_acf_20": 0.22697982336235087,
        "quantile_01": -0.05370889518632236,
        "quantile_99": 0.050625421498117586,
        "hill_tail_index": 2.598137287533782
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02058078652013403,
        "excess_kurtosis": 29.94325482801873,
        "return_acf_1": -0.14436388128492522,
        "abs_return_acf_1": 0.3606792779536861,
        "abs_return_acf_5": 0.2875208128391674,
        "abs_return_acf_20": 0.27600203940956536,
        "quantile_01": -0.06057284615315505,
        "quantile_99": 0.04948784907758076,
        "hill_tail_index": 2.1698423285735853
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
