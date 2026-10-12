# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27035
Run ID: `a601c86d67ae269c10953393190d479bce93759184a3231bcdc8dc0a1505c803`
Result fingerprint: `49bdaee8f6987ac2bd387708028ec439503b119e31b95a4776f1005bc2a425b6`

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
    "equal_weight_sd": -0.6011205457263061,
    "equal_weight_raw": -9.016808185894588,
    "fixed_start_cap_weight_sd": -0.621677646463551,
    "fixed_start_cap_weight_raw": -9.325164696953268,
    "end_cap_weight_sd": -0.6448729553568406,
    "end_cap_weight_raw": -9.673094330352608
  },
  "full_period_change": {
    "equal_weight_sd": -0.9038943552501137,
    "equal_weight_raw": -13.558415328751707
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8431798694036882,
    "inflation_mean_sd": 0.5782962962962963
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3404166666666697,
    "equal_weight_raw": 5.1062500000000455,
    "fixed_start_cap_weight_sd": 0.31829287008116336,
    "fixed_start_cap_weight_raw": 4.774393051217449,
    "end_cap_weight_sd": 0.2958998809150515,
    "end_cap_weight_raw": 4.438498213725772
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
      "change_sd": -0.5648462635321386,
      "change_raw": -8.472693952982079,
      "decay_adjusted_gain_sd": 0.35138888888889164
    },
    "small": {
      "count": 18,
      "change_sd": -0.5973809523809491,
      "change_raw": -8.960714285714237,
      "decay_adjusted_gain_sd": 0.3550000000000032
    },
    "large_minus_small_sd": -0.13500000000000012,
    "large_minus_small_raw": -2.0250000000000017
  },
  "inflation": {
    "initial_mean_sd": 0.2534166666666667,
    "final_mean_sd": 0.58475,
    "mean_sd": 0.45920739661393284,
    "mean_absolute_raw_gap": 6.8881109492089925,
    "final_absolute_raw_gap": 8.771249999999998,
    "mean_range_fraction": 0.06888110949208992
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.2904316510133344,
    "final_wealth_share": 0.27519478098498457
  },
  "pricing_slope": {
    "mean": -0.0013787530223304386,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.0390583280103822,
    "real_improvement_cost": 0.02627138589788728,
    "washing_cost": 0.012786942112494912,
    "fine_transfer": 0.0135527640246579,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0526110920350401,
    "resource_cost_fraction_initial_cap": 0.00130194426701274,
    "private_net_outflow_fraction_initial_cap": 0.00175370306783467,
    "fine_transfer_fraction_initial_cap": 0.00045175880082193,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.000795762049500684,
    "unapplied_final_day_resource_cost": 0.003668393793384165
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 261.46792554165347,
    "beneficial_raw_gain_per_resource_cost": 3922.018883124802,
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
    "accrued_cost": 2.9490540906332567,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.027136385557219624,
    "accrued_cost_fraction_initial_cap": 0.09830180302110855,
    "mean_contract_rate": 0.04064875586739082,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 2.2649721812174244e-15,
    "maximum_absolute_share_error": 1.3322676295501878e-15,
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
      "minimum": -0.19332336830158736,
      "maximum": -0.022811673821123497,
      "mean": -0.0877152601115325,
      "median": -0.08926224511561792,
      "quantile_05": -0.14323401811702438,
      "quantile_95": -0.032809473621989015
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
      "minimum": 0.2826024571528506,
      "maximum": 0.7381277120427867,
      "mean": 0.44225026444341486,
      "median": 0.3830735163498222,
      "quantile_05": 0.30835795151784295,
      "quantile_95": 0.683203665510288
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
        "daily_volatility": 0.021527995401517917,
        "excess_kurtosis": 7.75527961525443,
        "return_acf_1": -0.09135454441005697,
        "abs_return_acf_1": 0.4097538668630239,
        "abs_return_acf_5": 0.38665366607087315,
        "abs_return_acf_20": 0.31110781931229653,
        "quantile_01": -0.08053392637231709,
        "quantile_99": 0.06891375567347263,
        "hill_tail_index": 4.0796316508035515
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019417224979882006,
        "excess_kurtosis": 7.058664952964083,
        "return_acf_1": -0.0707357043459196,
        "abs_return_acf_1": 0.3642445433738728,
        "abs_return_acf_5": 0.3362899031882747,
        "abs_return_acf_20": 0.3542182248487045,
        "quantile_01": -0.05477065532655115,
        "quantile_99": 0.05861083522803396,
        "hill_tail_index": 3.536248014371537
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020273128923305503,
        "excess_kurtosis": 8.637267629803956,
        "return_acf_1": -0.14243634436208974,
        "abs_return_acf_1": 0.4041976424801062,
        "abs_return_acf_5": 0.34274072139365414,
        "abs_return_acf_20": 0.3281673472645288,
        "quantile_01": -0.06038907375234769,
        "quantile_99": 0.06010378133875428,
        "hill_tail_index": 4.0733215419110875
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01838698007748984,
        "excess_kurtosis": 6.937833094036762,
        "return_acf_1": -0.04658712711144808,
        "abs_return_acf_1": 0.3280625768023597,
        "abs_return_acf_5": 0.2505340758700284,
        "abs_return_acf_20": 0.2515547768079841,
        "quantile_01": -0.05903372494307516,
        "quantile_99": 0.05658606435277156,
        "hill_tail_index": 4.063904457165169
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01873767216118007,
        "excess_kurtosis": 9.722304399659764,
        "return_acf_1": -0.14388666028015273,
        "abs_return_acf_1": 0.48881505559688226,
        "abs_return_acf_5": 0.4233561825376488,
        "abs_return_acf_20": 0.3586892612226476,
        "quantile_01": -0.0567276742677033,
        "quantile_99": 0.06037399756024519,
        "hill_tail_index": 2.5011415918680644
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020204068345396637,
        "excess_kurtosis": 8.628358270868363,
        "return_acf_1": -0.11781479491871923,
        "abs_return_acf_1": 0.34101253351126987,
        "abs_return_acf_5": 0.36028277247623075,
        "abs_return_acf_20": 0.30780546993735186,
        "quantile_01": -0.06535931950888187,
        "quantile_99": 0.06228914778536556,
        "hill_tail_index": 4.1628626369488435
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0174419471040231,
        "excess_kurtosis": 3.293649211217927,
        "return_acf_1": -0.08716994582117889,
        "abs_return_acf_1": 0.28446717006852495,
        "abs_return_acf_5": 0.2689033999488707,
        "abs_return_acf_20": 0.24293225962414694,
        "quantile_01": -0.04840073921344135,
        "quantile_99": 0.04283088637940955,
        "hill_tail_index": 4.455937839103802
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021407384730923167,
        "excess_kurtosis": 6.076411986053047,
        "return_acf_1": -0.056344159164541406,
        "abs_return_acf_1": 0.46032602286539276,
        "abs_return_acf_5": 0.45932647555030437,
        "abs_return_acf_20": 0.34683388878741117,
        "quantile_01": -0.06986626238401904,
        "quantile_99": 0.06434438704193118,
        "hill_tail_index": 3.6686791363480977
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019736076608298136,
        "excess_kurtosis": 7.117783011903535,
        "return_acf_1": -0.04595321672435656,
        "abs_return_acf_1": 0.39332302176333556,
        "abs_return_acf_5": 0.35641226092931194,
        "abs_return_acf_20": 0.344526541588063,
        "quantile_01": -0.057044241317661636,
        "quantile_99": 0.050749257160169314,
        "hill_tail_index": 2.8001051002938313
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01716195401293673,
        "excess_kurtosis": 2.709334392996383,
        "return_acf_1": -0.09626226658749697,
        "abs_return_acf_1": 0.19882302679360336,
        "abs_return_acf_5": 0.23490751311697872,
        "abs_return_acf_20": 0.21830966922531342,
        "quantile_01": -0.04907850165068354,
        "quantile_99": 0.04480771969254306,
        "hill_tail_index": 3.8207817822663785
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01756724037612925,
        "excess_kurtosis": 12.04103759873512,
        "return_acf_1": -0.02914015713989565,
        "abs_return_acf_1": 0.3783772117315156,
        "abs_return_acf_5": 0.32693039227538045,
        "abs_return_acf_20": 0.27428053095719734,
        "quantile_01": -0.04814958806862378,
        "quantile_99": 0.057658948975484084,
        "hill_tail_index": 2.6868752759313757
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019673504934147944,
        "excess_kurtosis": 7.276456933526196,
        "return_acf_1": -0.05003538491063452,
        "abs_return_acf_1": 0.243754511464384,
        "abs_return_acf_5": 0.2986693403360611,
        "abs_return_acf_20": 0.21309640967893095,
        "quantile_01": -0.06568043044197093,
        "quantile_99": 0.05563608266220095,
        "hill_tail_index": 3.789028096728279
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01876019670593108,
        "excess_kurtosis": 5.2460846976280475,
        "return_acf_1": -0.11121735046037722,
        "abs_return_acf_1": 0.24730874398666644,
        "abs_return_acf_5": 0.2622557176402233,
        "abs_return_acf_20": 0.23304420891050306,
        "quantile_01": -0.05614608378991482,
        "quantile_99": 0.05926452932526987,
        "hill_tail_index": 3.8081647836873547
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020401818887688602,
        "excess_kurtosis": 7.101658724261442,
        "return_acf_1": -0.10179248983824012,
        "abs_return_acf_1": 0.32609074460145765,
        "abs_return_acf_5": 0.3323037564902961,
        "abs_return_acf_20": 0.3350537975580606,
        "quantile_01": -0.06462114907862,
        "quantile_99": 0.054102679812799696,
        "hill_tail_index": 3.1925446872924947
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019165265524197846,
        "excess_kurtosis": 12.820473145712585,
        "return_acf_1": -0.061279237382611935,
        "abs_return_acf_1": 0.31216547951478985,
        "abs_return_acf_5": 0.3352639491658492,
        "abs_return_acf_20": 0.27753418343597025,
        "quantile_01": -0.0590064312155692,
        "quantile_99": 0.05117310686633839,
        "hill_tail_index": 3.168021649145766
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017870491930195836,
        "excess_kurtosis": 10.683653015782134,
        "return_acf_1": -0.12465059713144382,
        "abs_return_acf_1": 0.3266806649294158,
        "abs_return_acf_5": 0.32206581787132477,
        "abs_return_acf_20": 0.3428150818313412,
        "quantile_01": -0.05394733473931097,
        "quantile_99": 0.05250062817710581,
        "hill_tail_index": 4.381139963211263
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018972168544641916,
        "excess_kurtosis": 8.817945191725508,
        "return_acf_1": -0.11709772886298427,
        "abs_return_acf_1": 0.21663185202483887,
        "abs_return_acf_5": 0.24743184742636362,
        "abs_return_acf_20": 0.35216117509929756,
        "quantile_01": -0.059491503133126504,
        "quantile_99": 0.057176968582730026,
        "hill_tail_index": 3.095945069011563
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016216037851600515,
        "excess_kurtosis": 4.509933830278997,
        "return_acf_1": -0.07401531857830226,
        "abs_return_acf_1": 0.26661689329790234,
        "abs_return_acf_5": 0.3284953606158048,
        "abs_return_acf_20": 0.21477450726109545,
        "quantile_01": -0.044603981975295824,
        "quantile_99": 0.041582351526414124,
        "hill_tail_index": 3.517894633081011
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.0173315474439264,
        "excess_kurtosis": 9.233422064751469,
        "return_acf_1": -0.11706533205000898,
        "abs_return_acf_1": 0.26735767437209734,
        "abs_return_acf_5": 0.14433578165030614,
        "abs_return_acf_20": 0.22586616746531749,
        "quantile_01": -0.052995833676968175,
        "quantile_99": 0.0459299399273945,
        "hill_tail_index": 3.144004114311917
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020556333211303564,
        "excess_kurtosis": 7.428063108411116,
        "return_acf_1": -0.052377759022545656,
        "abs_return_acf_1": 0.3358120555004545,
        "abs_return_acf_5": 0.2616649318625837,
        "abs_return_acf_20": 0.26795445294979875,
        "quantile_01": -0.07134623494634006,
        "quantile_99": 0.07106461303986288,
        "hill_tail_index": 4.032245653437638
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020275706185818462,
        "excess_kurtosis": 11.88986103992175,
        "return_acf_1": -0.12589926215552744,
        "abs_return_acf_1": 0.4436937973363441,
        "abs_return_acf_5": 0.3788007737010026,
        "abs_return_acf_20": 0.23754067613820284,
        "quantile_01": -0.06214270744857941,
        "quantile_99": 0.0524841468971482,
        "hill_tail_index": 2.5213904317330185
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01761986819542,
        "excess_kurtosis": 13.628768068776662,
        "return_acf_1": -0.022811673821123497,
        "abs_return_acf_1": 0.23978666258935438,
        "abs_return_acf_5": 0.21908358581529289,
        "abs_return_acf_20": 0.21071905285882286,
        "quantile_01": -0.04989231267989187,
        "quantile_99": 0.04259839972176107,
        "hill_tail_index": 3.1417734218161772
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018257769118806985,
        "excess_kurtosis": 5.227877864223975,
        "return_acf_1": -0.10039974446203229,
        "abs_return_acf_1": 0.27471188318080086,
        "abs_return_acf_5": 0.2202823806705702,
        "abs_return_acf_20": 0.2700628318524602,
        "quantile_01": -0.04947452378040905,
        "quantile_99": 0.04597391863140341,
        "hill_tail_index": 3.313517595893413
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01737155570556365,
        "excess_kurtosis": 8.478922683541521,
        "return_acf_1": -0.040108788503013054,
        "abs_return_acf_1": 0.323274526391627,
        "abs_return_acf_5": 0.40517487035036887,
        "abs_return_acf_20": 0.30080085308285137,
        "quantile_01": -0.048962484919849274,
        "quantile_99": 0.04739257735347827,
        "hill_tail_index": 2.7450855893976627
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0201384187910317,
        "excess_kurtosis": 5.442318121564515,
        "return_acf_1": -0.19332336830158736,
        "abs_return_acf_1": 0.265444194204065,
        "abs_return_acf_5": 0.2953309088732452,
        "abs_return_acf_20": 0.26508273616360883,
        "quantile_01": -0.06285586748954633,
        "quantile_99": 0.055390869879432356,
        "hill_tail_index": 3.813799186559831
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019022744391300365,
        "excess_kurtosis": 12.45053478258186,
        "return_acf_1": -0.03729419376676975,
        "abs_return_acf_1": 0.32141440670592314,
        "abs_return_acf_5": 0.3016793276313676,
        "abs_return_acf_20": 0.25417083696170356,
        "quantile_01": -0.056231544906050666,
        "quantile_99": 0.05235540076034147,
        "hill_tail_index": 2.7645875092502403
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019814621843331395,
        "excess_kurtosis": 5.807762653507895,
        "return_acf_1": -0.12928544276021325,
        "abs_return_acf_1": 0.3276028773289731,
        "abs_return_acf_5": 0.37611281192761586,
        "abs_return_acf_20": 0.3627726144453303,
        "quantile_01": -0.057116047491199425,
        "quantile_99": 0.06808259187804354,
        "hill_tail_index": 3.4870362594555973
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018681257773063058,
        "excess_kurtosis": 10.776939223141644,
        "return_acf_1": -0.13093571980400384,
        "abs_return_acf_1": 0.29571716430220785,
        "abs_return_acf_5": 0.21081256401266313,
        "abs_return_acf_20": 0.25519985247136995,
        "quantile_01": -0.049087251175957976,
        "quantile_99": 0.052442759187954324,
        "hill_tail_index": 3.2045498643224573
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02028056345524142,
        "excess_kurtosis": 13.708564414543098,
        "return_acf_1": -0.060335895620179644,
        "abs_return_acf_1": 0.36308582193172356,
        "abs_return_acf_5": 0.2940079012490466,
        "abs_return_acf_20": 0.29086930936208827,
        "quantile_01": -0.059560075971988875,
        "quantile_99": 0.056469995198938354,
        "hill_tail_index": 2.6327220609806523
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01807635972404497,
        "excess_kurtosis": 2.5192606455537527,
        "return_acf_1": -0.05384759504851957,
        "abs_return_acf_1": 0.26046247610552925,
        "abs_return_acf_5": 0.25754467592971464,
        "abs_return_acf_20": 0.2531236612083423,
        "quantile_01": -0.0532511709117402,
        "quantile_99": 0.048815373059001806,
        "hill_tail_index": 5.02493924483163
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
