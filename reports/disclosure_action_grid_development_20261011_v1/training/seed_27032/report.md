# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27032
Run ID: `9d80fe8456be2fcc0f3126f0f731ed59dc505b504293e4db43ddb7b4cfc08243`
Result fingerprint: `374e062a5bb7cf4ca2f5e487a7ccc8b00c01039d51d01c76d2e5bf62eac62f5c`

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
    "equal_weight_sd": -0.5282976190476159,
    "equal_weight_raw": -7.9244642857142376,
    "fixed_start_cap_weight_sd": -0.5841332664883683,
    "fixed_start_cap_weight_raw": -8.761998997325524,
    "end_cap_weight_sd": -0.5698305000606686,
    "end_cap_weight_raw": -8.547457500910028
  },
  "full_period_change": {
    "equal_weight_sd": -0.8205714285714237,
    "equal_weight_raw": -12.308571428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.771225198412694,
    "inflation_mean_sd": 0.6122948231518149
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4240833333333365,
    "equal_weight_raw": 6.361250000000046,
    "fixed_start_cap_weight_sd": 0.36824768589258394,
    "fixed_start_cap_weight_raw": 5.52371528838876,
    "end_cap_weight_sd": 0.38255045232028384,
    "end_cap_weight_raw": 5.738256784804257
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6198809523809494,
      "change_raw": -9.298214285714241,
      "decay_adjusted_gain_sd": 0.33250000000000296
    },
    "mid": {
      "count": 9,
      "change_sd": -0.47960317460317153,
      "change_raw": -7.194047619047573,
      "decay_adjusted_gain_sd": 0.47277777777778085
    },
    "small": {
      "count": 18,
      "change_sd": -0.5373809523809492,
      "change_raw": -8.060714285714237,
      "decay_adjusted_gain_sd": 0.4150000000000031
    },
    "large_minus_small_sd": -0.08250000000000024,
    "large_minus_small_raw": -1.2375000000000036
  },
  "inflation": {
    "initial_mean_sd": 0.25693569616768797,
    "final_mean_sd": 0.6479356961676879,
    "mean_sd": 0.45397372003668607,
    "mean_absolute_raw_gap": 6.8096058005502895,
    "final_absolute_raw_gap": 9.71903544251532,
    "mean_range_fraction": 0.06809605800550289
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.35333333333333333,
    "initial_wealth_share": 0.3692662492670652,
    "final_wealth_share": 0.40328350134388324
  },
  "pricing_slope": {
    "mean": -0.0024998960618067825,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.36494299190446144,
    "real_improvement_cost": 0.30106502735753515,
    "washing_cost": 0.06387796454692635,
    "fine_transfer": 0.007671716459706348,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.37261470836416777,
    "resource_cost_fraction_initial_cap": 0.01216476639681538,
    "private_net_outflow_fraction_initial_cap": 0.01242049027880559,
    "fine_transfer_fraction_initial_cap": 0.00025572388199021157,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002854113515888092,
    "unapplied_final_day_resource_cost": 0.005245474996402477
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 34.86160929850305,
    "beneficial_raw_gain_per_resource_cost": 522.9241394775457,
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
    "accrued_cost": 2.8355881577614097,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.1406023184290675,
    "accrued_cost_fraction_initial_cap": 0.09451960525871364,
    "mean_contract_rate": 0.03938346329801343,
    "maximum_ledger_error": 8.978549240895584e-20
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
    "maximum_relative_cash_error": 2.162328545633927e-15,
    "maximum_absolute_share_error": 2.1094237467877974e-15,
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
      "minimum": -0.22619733671733563,
      "maximum": -0.045027794825315944,
      "mean": -0.14247437360595977,
      "median": -0.1427520821849656,
      "quantile_05": -0.2174942156996814,
      "quantile_95": -0.0653520296814369
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
      "minimum": 0.23470748465139113,
      "maximum": 0.8098925538036259,
      "mean": 0.5107223885068408,
      "median": 0.5494013047490679,
      "quantile_05": 0.2690389362274571,
      "quantile_95": 0.7795575917831767
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
        "daily_volatility": 0.021375223294308594,
        "excess_kurtosis": 26.996363040980494,
        "return_acf_1": -0.15490565437304407,
        "abs_return_acf_1": 0.35659621846102935,
        "abs_return_acf_5": 0.41798853845101147,
        "abs_return_acf_20": 0.4083759260213155,
        "quantile_01": -0.07500354493666822,
        "quantile_99": 0.0447328065884538,
        "hill_tail_index": 1.7999703183745848
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02112696292747449,
        "excess_kurtosis": 21.44896489863161,
        "return_acf_1": -0.16605765856033464,
        "abs_return_acf_1": 0.34742649835156797,
        "abs_return_acf_5": 0.3673092715744998,
        "abs_return_acf_20": 0.27365755017436066,
        "quantile_01": -0.07309381618928323,
        "quantile_99": 0.04877468908429233,
        "hill_tail_index": 1.898092002340442
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02069469687815968,
        "excess_kurtosis": 7.924554944305029,
        "return_acf_1": -0.12139034629491707,
        "abs_return_acf_1": 0.3695309980274063,
        "abs_return_acf_5": 0.3449522026543327,
        "abs_return_acf_20": 0.32009944008861024,
        "quantile_01": -0.06930148938535763,
        "quantile_99": 0.06556582693101887,
        "hill_tail_index": 3.6554111016063224
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02049931172329377,
        "excess_kurtosis": 6.414919139678025,
        "return_acf_1": -0.10112982662025996,
        "abs_return_acf_1": 0.38156125076104086,
        "abs_return_acf_5": 0.3864276493915768,
        "abs_return_acf_20": 0.2929600143906206,
        "quantile_01": -0.06991972656767483,
        "quantile_99": 0.05516166444752221,
        "hill_tail_index": 3.7077733525357717
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018697937508168685,
        "excess_kurtosis": 5.262390384405908,
        "return_acf_1": -0.134257903248453,
        "abs_return_acf_1": 0.39019001092820144,
        "abs_return_acf_5": 0.3079659803737572,
        "abs_return_acf_20": 0.29897643690070963,
        "quantile_01": -0.05688693511560536,
        "quantile_99": 0.0537273707011385,
        "hill_tail_index": 3.03650020034548
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023187786309689786,
        "excess_kurtosis": 12.012243507148405,
        "return_acf_1": -0.1493114746666363,
        "abs_return_acf_1": 0.3918859361505705,
        "abs_return_acf_5": 0.34380870357111887,
        "abs_return_acf_20": 0.3599829282257341,
        "quantile_01": -0.07594875455527182,
        "quantile_99": 0.0803693716423988,
        "hill_tail_index": 3.433133700051661
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01943584186604166,
        "excess_kurtosis": 15.745963964970041,
        "return_acf_1": -0.1790338091840366,
        "abs_return_acf_1": 0.3559293643258966,
        "abs_return_acf_5": 0.3671379140600203,
        "abs_return_acf_20": 0.3505979002511774,
        "quantile_01": -0.06396639003024125,
        "quantile_99": 0.04644875543690774,
        "hill_tail_index": 2.114628046259462
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021311427463635773,
        "excess_kurtosis": 11.581388288853798,
        "return_acf_1": -0.21144507288848577,
        "abs_return_acf_1": 0.3708348203833363,
        "abs_return_acf_5": 0.3240585134484414,
        "abs_return_acf_20": 0.3196374671307127,
        "quantile_01": -0.075567715420727,
        "quantile_99": 0.060061284777722206,
        "hill_tail_index": 3.1815120908912498
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018775705874607754,
        "excess_kurtosis": 12.037048373140617,
        "return_acf_1": -0.15331807892149465,
        "abs_return_acf_1": 0.3006640874450297,
        "abs_return_acf_5": 0.3401726186010737,
        "abs_return_acf_20": 0.24062693615254185,
        "quantile_01": -0.06493974800541258,
        "quantile_99": 0.04772559311582724,
        "hill_tail_index": 2.286238697739757
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019631093014069505,
        "excess_kurtosis": 12.787006419929948,
        "return_acf_1": -0.15477321856913373,
        "abs_return_acf_1": 0.4228677364245297,
        "abs_return_acf_5": 0.35502936652964734,
        "abs_return_acf_20": 0.41105012149156533,
        "quantile_01": -0.06420128386469072,
        "quantile_99": 0.047968189012253824,
        "hill_tail_index": 2.6084106103977085
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02068594351638137,
        "excess_kurtosis": 5.48234767620683,
        "return_acf_1": -0.14338963344868022,
        "abs_return_acf_1": 0.3611722033579432,
        "abs_return_acf_5": 0.29370078548163003,
        "abs_return_acf_20": 0.2785710068004226,
        "quantile_01": -0.07062587939668194,
        "quantile_99": 0.06003946595253184,
        "hill_tail_index": 3.6430917651508876
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01967940625650058,
        "excess_kurtosis": 13.46784739606553,
        "return_acf_1": -0.2224435143633869,
        "abs_return_acf_1": 0.3341100363968329,
        "abs_return_acf_5": 0.2985568300048583,
        "abs_return_acf_20": 0.23087023275146135,
        "quantile_01": -0.05799755389625302,
        "quantile_99": 0.047704353073836345,
        "hill_tail_index": 2.020924432554478
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021400490285638566,
        "excess_kurtosis": 9.102670478496666,
        "return_acf_1": -0.045027794825315944,
        "abs_return_acf_1": 0.34406619057514626,
        "abs_return_acf_5": 0.3241827959925415,
        "abs_return_acf_20": 0.22835263195003438,
        "quantile_01": -0.07494127993364706,
        "quantile_99": 0.05751847007349822,
        "hill_tail_index": 3.3136706412973447
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018069437764359694,
        "excess_kurtosis": 12.423421042864627,
        "return_acf_1": -0.1807565154471466,
        "abs_return_acf_1": 0.299550213437015,
        "abs_return_acf_5": 0.36055952999019597,
        "abs_return_acf_20": 0.30435509548839845,
        "quantile_01": -0.051352262432009,
        "quantile_99": 0.03982933669791365,
        "hill_tail_index": 2.205110416661984
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020554247167397573,
        "excess_kurtosis": 6.9605109055362515,
        "return_acf_1": -0.06619286090204392,
        "abs_return_acf_1": 0.42906851632431936,
        "abs_return_acf_5": 0.4359219898539964,
        "abs_return_acf_20": 0.36102574029652423,
        "quantile_01": -0.06995401300155234,
        "quantile_99": 0.06867727426491856,
        "hill_tail_index": 3.787843616880323
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0216062755425643,
        "excess_kurtosis": 20.8558197044938,
        "return_acf_1": -0.14898051423790412,
        "abs_return_acf_1": 0.42446644527391364,
        "abs_return_acf_5": 0.4094580049893872,
        "abs_return_acf_20": 0.4080788050600282,
        "quantile_01": -0.07254375778734955,
        "quantile_99": 0.05090066139692257,
        "hill_tail_index": 2.232763896098632
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02037584447585652,
        "excess_kurtosis": 14.780086944114629,
        "return_acf_1": -0.09864602481830645,
        "abs_return_acf_1": 0.4091996631452268,
        "abs_return_acf_5": 0.3634622321007282,
        "abs_return_acf_20": 0.3528006472248529,
        "quantile_01": -0.05858082104800616,
        "quantile_99": 0.05519995804394843,
        "hill_tail_index": 2.6149965937360307
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.0196016145347626,
        "excess_kurtosis": 7.836665750560268,
        "return_acf_1": -0.11361729954129908,
        "abs_return_acf_1": 0.3984361269711644,
        "abs_return_acf_5": 0.41071445261169365,
        "abs_return_acf_20": 0.3337140975270821,
        "quantile_01": -0.0614271706537681,
        "quantile_99": 0.058536437224774356,
        "hill_tail_index": 2.8705765704295225
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02178057629931577,
        "excess_kurtosis": 26.331302802900414,
        "return_acf_1": -0.18267751021732187,
        "abs_return_acf_1": 0.4049382349468368,
        "abs_return_acf_5": 0.3711788328518693,
        "abs_return_acf_20": 0.2849116758787232,
        "quantile_01": -0.07264176748569941,
        "quantile_99": 0.04887944284509808,
        "hill_tail_index": 1.7690083557428629
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021114395617334906,
        "excess_kurtosis": 10.822597927435202,
        "return_acf_1": -0.17474023260585816,
        "abs_return_acf_1": 0.4123512747331491,
        "abs_return_acf_5": 0.3213965193538903,
        "abs_return_acf_20": 0.27404273101463156,
        "quantile_01": -0.06948184448540234,
        "quantile_99": 0.06252990306408532,
        "hill_tail_index": 3.069579496726243
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01880753709982746,
        "excess_kurtosis": 6.286250815896667,
        "return_acf_1": -0.1183057793922262,
        "abs_return_acf_1": 0.4136121616372511,
        "abs_return_acf_5": 0.3093775373424776,
        "abs_return_acf_20": 0.2222753220129676,
        "quantile_01": -0.061990551186390845,
        "quantile_99": 0.05044752936756156,
        "hill_tail_index": 3.7547531257801348
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019480819508866397,
        "excess_kurtosis": 5.9304628710209,
        "return_acf_1": -0.06466407686457659,
        "abs_return_acf_1": 0.315585912075845,
        "abs_return_acf_5": 0.4059700014425885,
        "abs_return_acf_20": 0.33198510913500884,
        "quantile_01": -0.06306687912335701,
        "quantile_99": 0.06535729355526775,
        "hill_tail_index": 3.8169147386225717
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019085733817512194,
        "excess_kurtosis": 6.57750227676094,
        "return_acf_1": -0.1388150544093571,
        "abs_return_acf_1": 0.42271946395299526,
        "abs_return_acf_5": 0.3873530721355462,
        "abs_return_acf_20": 0.3168279329920574,
        "quantile_01": -0.05536141298101213,
        "quantile_99": 0.06095481764625475,
        "hill_tail_index": 2.839378266416833
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020399850153188636,
        "excess_kurtosis": 17.462557039598565,
        "return_acf_1": -0.14211453092125098,
        "abs_return_acf_1": 0.29844619793902394,
        "abs_return_acf_5": 0.32072137907855414,
        "abs_return_acf_20": 0.3289870405574404,
        "quantile_01": -0.07171004651243607,
        "quantile_99": 0.05221602840107215,
        "hill_tail_index": 2.7356402518148277
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02014044099412837,
        "excess_kurtosis": 16.98975746404703,
        "return_acf_1": -0.20348822631979838,
        "abs_return_acf_1": 0.3693136770558738,
        "abs_return_acf_5": 0.33763845140629084,
        "abs_return_acf_20": 0.3081167357308817,
        "quantile_01": -0.05805309861110173,
        "quantile_99": 0.04262292531074252,
        "hill_tail_index": 1.8447740244944169
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020642468405178627,
        "excess_kurtosis": 16.070770572865502,
        "return_acf_1": -0.11047637205645612,
        "abs_return_acf_1": 0.40894518246713485,
        "abs_return_acf_5": 0.3665446998780446,
        "abs_return_acf_20": 0.38907339568444305,
        "quantile_01": -0.08055590772834192,
        "quantile_99": 0.04300712576772644,
        "hill_tail_index": 1.9027571268016539
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021286095820067182,
        "excess_kurtosis": 10.348827766203783,
        "return_acf_1": -0.11534019731169323,
        "abs_return_acf_1": 0.30567212340255634,
        "abs_return_acf_5": 0.3207294575803051,
        "abs_return_acf_20": 0.2905645062598941,
        "quantile_01": -0.07008808953567444,
        "quantile_99": 0.06732113106523302,
        "hill_tail_index": 2.328138415822545
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020082540361527946,
        "excess_kurtosis": 11.19997953326243,
        "return_acf_1": -0.11577401017068405,
        "abs_return_acf_1": 0.3289331416036374,
        "abs_return_acf_5": 0.26212558302929084,
        "abs_return_acf_20": 0.34483598020882844,
        "quantile_01": -0.05840403912342236,
        "quantile_99": 0.058331855038275114,
        "hill_tail_index": 3.647733064041407
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021725109422219398,
        "excess_kurtosis": 12.213208053128715,
        "return_acf_1": -0.13696068028135555,
        "abs_return_acf_1": 0.37404489411411473,
        "abs_return_acf_5": 0.4242674636676071,
        "abs_return_acf_20": 0.3955168157691413,
        "quantile_01": -0.0680928428439478,
        "quantile_99": 0.06038119389608982,
        "hill_tail_index": 2.63495829506609
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020763699408619836,
        "excess_kurtosis": 20.298561781124,
        "return_acf_1": -0.22619733671733563,
        "abs_return_acf_1": 0.45797981222968964,
        "abs_return_acf_5": 0.3716175457776249,
        "abs_return_acf_20": 0.3842651230108062,
        "quantile_01": -0.07086120477120929,
        "quantile_99": 0.044364147456431004,
        "hill_tail_index": 1.966098480038622
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
