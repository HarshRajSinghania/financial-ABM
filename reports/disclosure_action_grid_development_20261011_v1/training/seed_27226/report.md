# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27226
Run ID: `dfd9083fac4b4c48fc519f8db79ef62f967be137b79a706ce7bf9e0c63d67333`
Result fingerprint: `0f005e9c06e9f12ad331295e1dc34ea88904e51c604046baf3c503ce668bfa01`

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
    "equal_weight_sd": -0.7977214831311934,
    "equal_weight_raw": -11.965822246967907,
    "fixed_start_cap_weight_sd": -0.7577723799935508,
    "fixed_start_cap_weight_raw": -11.366585699903265,
    "end_cap_weight_sd": -0.7622613846205613,
    "end_cap_weight_raw": -11.433920769308417
  },
  "full_period_change": {
    "equal_weight_sd": -1.2300786259883343,
    "equal_weight_raw": -18.451179389825015
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.141304155088864,
    "inflation_mean_sd": 0.7499933862433863
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1406666666666697,
    "equal_weight_raw": 2.1100000000000447,
    "fixed_start_cap_weight_sd": 0.19228883072055705,
    "fixed_start_cap_weight_raw": 2.8843324608083556,
    "end_cap_weight_sd": 0.1874376769922929,
    "end_cap_weight_raw": 2.811565154884394
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7607142857142826,
      "change_raw": -11.410714285714239,
      "decay_adjusted_gain_sd": 0.19166666666666976
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7384920634920606,
      "change_raw": -11.07738095238091,
      "decay_adjusted_gain_sd": 0.2138888888888917
    },
    "small": {
      "count": 18,
      "change_sd": -0.833504059186912,
      "change_raw": -12.502560887803678,
      "decay_adjusted_gain_sd": 0.09555555555555863
    },
    "large_minus_small_sd": 0.07278977347262938,
    "large_minus_small_raw": 1.0918466020894408
  },
  "inflation": {
    "initial_mean_sd": 0.2638333333333333,
    "final_mean_sd": 0.7765000000000001,
    "mean_sd": 0.5640756314182626,
    "mean_absolute_raw_gap": 8.46113447127394,
    "final_absolute_raw_gap": 11.647500000000003,
    "mean_range_fraction": 0.0846113447127394
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.2866666666666667,
    "initial_wealth_share": 0.2144670972059397,
    "final_wealth_share": 0.27718154284090507
  },
  "pricing_slope": {
    "mean": -0.001275223155041929,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.03551404132148231,
    "real_improvement_cost": 0.019066493230018185,
    "washing_cost": 0.016447548091464117,
    "fine_transfer": 0.008732294818626831,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.044246336140109144,
    "resource_cost_fraction_initial_cap": 0.0011838013773827437,
    "private_net_outflow_fraction_initial_cap": 0.0014748778713369716,
    "fine_transfer_fraction_initial_cap": 0.00029107649395422776,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00043064546016770245,
    "unapplied_final_day_resource_cost": 1.7698892115600555e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 118.82624007218881,
    "beneficial_raw_gain_per_resource_cost": 1782.393601082832,
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
    "accrued_cost": 2.8924528217267396,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.0837376544637366,
    "accrued_cost_fraction_initial_cap": 0.09641509405755799,
    "mean_contract_rate": 0.040090693923610525,
    "maximum_ledger_error": 1.2027867851011065e-19
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
    "maximum_relative_cash_error": 1.5621227442601196e-15,
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
      "minimum": -0.1935757476321347,
      "maximum": 0.021034641993605684,
      "mean": -0.11675254658284294,
      "median": -0.12396921409939693,
      "quantile_05": -0.1882188348722346,
      "quantile_95": -0.02045606302631995
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
      "minimum": 0.2592505219272352,
      "maximum": 0.7804656798622991,
      "mean": 0.4764618997220001,
      "median": 0.44673615750300805,
      "quantile_05": 0.3085641261817066,
      "quantile_95": 0.7146451743725964
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
        "daily_volatility": 0.016766505911947165,
        "excess_kurtosis": 18.339656226440386,
        "return_acf_1": -0.0447873049586056,
        "abs_return_acf_1": 0.48909608221424383,
        "abs_return_acf_5": 0.4250386209979641,
        "abs_return_acf_20": 0.19888512834202463,
        "quantile_01": -0.03745263709878804,
        "quantile_99": 0.0416096198981819,
        "hill_tail_index": 1.5349575281127994
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018900982324591326,
        "excess_kurtosis": 7.1417806585650485,
        "return_acf_1": -0.07849350225008096,
        "abs_return_acf_1": 0.3269247933792066,
        "abs_return_acf_5": 0.3479990374175736,
        "abs_return_acf_20": 0.3150235146422982,
        "quantile_01": -0.054447977234026335,
        "quantile_99": 0.04917447632535755,
        "hill_tail_index": 2.6072018006820503
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016954948530058536,
        "excess_kurtosis": 3.042777972523692,
        "return_acf_1": -0.16991540747010683,
        "abs_return_acf_1": 0.25841896775382067,
        "abs_return_acf_5": 0.28713593556942013,
        "abs_return_acf_20": 0.28716356264424103,
        "quantile_01": -0.051836405314800826,
        "quantile_99": 0.048444233592115186,
        "hill_tail_index": 4.929666203226511
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.015490168245685354,
        "excess_kurtosis": 19.964373866124614,
        "return_acf_1": -0.000548683263540556,
        "abs_return_acf_1": 0.3265989553494144,
        "abs_return_acf_5": 0.3095879068859985,
        "abs_return_acf_20": 0.21093810073457672,
        "quantile_01": -0.03653142591350737,
        "quantile_99": 0.03914634746251029,
        "hill_tail_index": 2.3689403651399696
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020300878523039273,
        "excess_kurtosis": 6.602760741780459,
        "return_acf_1": -0.14026496431696142,
        "abs_return_acf_1": 0.35027194663339883,
        "abs_return_acf_5": 0.4044873676835548,
        "abs_return_acf_20": 0.32601607526506376,
        "quantile_01": -0.06314826612374853,
        "quantile_99": 0.0574624453340225,
        "hill_tail_index": 3.810361019066128
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0217636390689262,
        "excess_kurtosis": 13.006800797143637,
        "return_acf_1": -0.12111744938584978,
        "abs_return_acf_1": 0.3694141211683912,
        "abs_return_acf_5": 0.410749717081526,
        "abs_return_acf_20": 0.34869170642489977,
        "quantile_01": -0.07351997524021893,
        "quantile_99": 0.058135396160104665,
        "hill_tail_index": 2.7587744816563555
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01794282661938573,
        "excess_kurtosis": 6.625564731684223,
        "return_acf_1": -0.11501396333476671,
        "abs_return_acf_1": 0.29406512072704877,
        "abs_return_acf_5": 0.3137606428021584,
        "abs_return_acf_20": 0.22887137966692397,
        "quantile_01": -0.057290734206822215,
        "quantile_99": 0.05091122756887773,
        "hill_tail_index": 3.9624413169439268
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01638333785884451,
        "excess_kurtosis": 4.108570590418229,
        "return_acf_1": -0.0712250784928051,
        "abs_return_acf_1": 0.22123044127934305,
        "abs_return_acf_5": 0.22413251598718859,
        "abs_return_acf_20": 0.2249769539557026,
        "quantile_01": -0.05202151272604882,
        "quantile_99": 0.045278407104443336,
        "hill_tail_index": 3.7162484393534263
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018140984238972875,
        "excess_kurtosis": 5.232300064163789,
        "return_acf_1": -0.18294180515320513,
        "abs_return_acf_1": 0.2882848581360162,
        "abs_return_acf_5": 0.30542746277526095,
        "abs_return_acf_20": 0.34078666085446196,
        "quantile_01": -0.05611395675344661,
        "quantile_99": 0.04953766725189257,
        "hill_tail_index": 3.0968018029906914
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019204155971704297,
        "excess_kurtosis": 5.492946611061619,
        "return_acf_1": -0.15220268190602396,
        "abs_return_acf_1": 0.39721092015325365,
        "abs_return_acf_5": 0.364434705445384,
        "abs_return_acf_20": 0.32549338417804413,
        "quantile_01": -0.06261878795552496,
        "quantile_99": 0.0583214712525485,
        "hill_tail_index": 3.7465954139495503
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01800922304319127,
        "excess_kurtosis": 7.822136042346177,
        "return_acf_1": -0.09688387337771624,
        "abs_return_acf_1": 0.2779926614933268,
        "abs_return_acf_5": 0.3387159738710425,
        "abs_return_acf_20": 0.2667494108849998,
        "quantile_01": -0.04995168834175643,
        "quantile_99": 0.04853281800530877,
        "hill_tail_index": 2.7938888608867454
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01705944669771292,
        "excess_kurtosis": 4.933778547894423,
        "return_acf_1": -0.04532647970692018,
        "abs_return_acf_1": 0.27159614082685346,
        "abs_return_acf_5": 0.30606731995183195,
        "abs_return_acf_20": 0.21767607197875632,
        "quantile_01": -0.044960571040885446,
        "quantile_99": 0.0417180569579475,
        "hill_tail_index": 2.7641730133274613
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019599313296084483,
        "excess_kurtosis": 6.155117625705328,
        "return_acf_1": -0.14704639070123912,
        "abs_return_acf_1": 0.2545444375352707,
        "abs_return_acf_5": 0.3174983578602727,
        "abs_return_acf_20": 0.28687241258906837,
        "quantile_01": -0.057044663776159715,
        "quantile_99": 0.04926640942528919,
        "hill_tail_index": 3.81708180528905
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021721465148721725,
        "excess_kurtosis": 9.745935554980829,
        "return_acf_1": -0.16546805589495303,
        "abs_return_acf_1": 0.39507055022644033,
        "abs_return_acf_5": 0.4684905891505704,
        "abs_return_acf_20": 0.31274778962184707,
        "quantile_01": -0.07114038670792254,
        "quantile_99": 0.0628215775887285,
        "hill_tail_index": 3.2387647198505554
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02337024618170344,
        "excess_kurtosis": 16.59538811566907,
        "return_acf_1": -0.08505113736013321,
        "abs_return_acf_1": 0.39075812267191845,
        "abs_return_acf_5": 0.4586301859691012,
        "abs_return_acf_20": 0.3123325894499595,
        "quantile_01": -0.08493390846588743,
        "quantile_99": 0.0746256087435087,
        "hill_tail_index": 3.2207390599980785
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017733624247388842,
        "excess_kurtosis": 5.079550376980938,
        "return_acf_1": -0.12281543984278215,
        "abs_return_acf_1": 0.29631347479791004,
        "abs_return_acf_5": 0.3293544286700334,
        "abs_return_acf_20": 0.33016310322567227,
        "quantile_01": -0.05129860142116997,
        "quantile_99": 0.04810914013509658,
        "hill_tail_index": 3.756176023514808
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017690196465340886,
        "excess_kurtosis": 16.095478484458322,
        "return_acf_1": 0.021034641993605684,
        "abs_return_acf_1": 0.46066577937402164,
        "abs_return_acf_5": 0.5332924003289967,
        "abs_return_acf_20": 0.32922922787551456,
        "quantile_01": -0.05051356393685118,
        "quantile_99": 0.05180467725280029,
        "hill_tail_index": 2.0090067426672715
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018881892149458058,
        "excess_kurtosis": 4.191569507644842,
        "return_acf_1": -0.10528711874264356,
        "abs_return_acf_1": 0.4226249366030689,
        "abs_return_acf_5": 0.3762435763879778,
        "abs_return_acf_20": 0.29071570836247607,
        "quantile_01": -0.06373390774851441,
        "quantile_99": 0.05463752293541332,
        "hill_tail_index": 4.7773181316145825
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01971030269178541,
        "excess_kurtosis": 4.895253855951834,
        "return_acf_1": -0.13924978627568418,
        "abs_return_acf_1": 0.4003048049273497,
        "abs_return_acf_5": 0.43013268216034367,
        "abs_return_acf_20": 0.3156883384992886,
        "quantile_01": -0.06386498068030509,
        "quantile_99": 0.05828928008804605,
        "hill_tail_index": 4.386195027880411
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020003350404717065,
        "excess_kurtosis": 10.25884664119369,
        "return_acf_1": -0.16312670054456754,
        "abs_return_acf_1": 0.35455058140156537,
        "abs_return_acf_5": 0.396102213283169,
        "abs_return_acf_20": 0.26123680045255787,
        "quantile_01": -0.06595552904684819,
        "quantile_99": 0.059742178596606736,
        "hill_tail_index": 3.6042931697383835
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019731415015160046,
        "excess_kurtosis": 5.906939608518266,
        "return_acf_1": -0.1935757476321347,
        "abs_return_acf_1": 0.32569376053304433,
        "abs_return_acf_5": 0.30330450706472917,
        "abs_return_acf_20": 0.2833640679049995,
        "quantile_01": -0.06308612145049529,
        "quantile_99": 0.062400703905285425,
        "hill_tail_index": 3.3886675428222612
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01946454627078905,
        "excess_kurtosis": 6.261423222178138,
        "return_acf_1": -0.13505302792158108,
        "abs_return_acf_1": 0.4464755569522986,
        "abs_return_acf_5": 0.4332828875524117,
        "abs_return_acf_20": 0.3292675921192179,
        "quantile_01": -0.0604206684786257,
        "quantile_99": 0.06025419917194817,
        "hill_tail_index": 2.968459748045595
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01663328286947316,
        "excess_kurtosis": 2.7819489196494516,
        "return_acf_1": -0.1925364046423496,
        "abs_return_acf_1": 0.2518053234519024,
        "abs_return_acf_5": 0.3384522756149181,
        "abs_return_acf_20": 0.2560557069516602,
        "quantile_01": -0.04729917079269007,
        "quantile_99": 0.045363851453083325,
        "hill_tail_index": 4.724982321684682
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02032004238718934,
        "excess_kurtosis": 5.535198793737882,
        "return_acf_1": -0.11549805700200015,
        "abs_return_acf_1": 0.4371931154181164,
        "abs_return_acf_5": 0.48708570526582795,
        "abs_return_acf_20": 0.3391702898750182,
        "quantile_01": -0.06252518250646734,
        "quantile_99": 0.06522069107061745,
        "hill_tail_index": 4.14108439712086
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018304389017159715,
        "excess_kurtosis": 5.113361765150099,
        "return_acf_1": -0.07325848511422554,
        "abs_return_acf_1": 0.34170396244693624,
        "abs_return_acf_5": 0.38760530274231203,
        "abs_return_acf_20": 0.3242981447479323,
        "quantile_01": -0.057306397567487566,
        "quantile_99": 0.05293038388886567,
        "hill_tail_index": 4.020716211770094
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019920110347375144,
        "excess_kurtosis": 7.173429215195911,
        "return_acf_1": -0.12308826030684113,
        "abs_return_acf_1": 0.4354915457797102,
        "abs_return_acf_5": 0.41136754637538897,
        "abs_return_acf_20": 0.34799953979632625,
        "quantile_01": -0.059799241888322044,
        "quantile_99": 0.06274506573666183,
        "hill_tail_index": 3.5122456278682015
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01666313844287856,
        "excess_kurtosis": 3.1748447831078,
        "return_acf_1": -0.12485016789195272,
        "abs_return_acf_1": 0.2776532117904255,
        "abs_return_acf_5": 0.29349622715617274,
        "abs_return_acf_20": 0.26347717885382166,
        "quantile_01": -0.045078167707406004,
        "quantile_99": 0.04389325312227226,
        "hill_tail_index": 3.4648563062901188
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02020198279104225,
        "excess_kurtosis": 5.745470123035469,
        "return_acf_1": -0.13399759826712804,
        "abs_return_acf_1": 0.41743454378408085,
        "abs_return_acf_5": 0.44598813468484055,
        "abs_return_acf_20": 0.3519620609767409,
        "quantile_01": -0.06771478900773517,
        "quantile_99": 0.05081379856578186,
        "hill_tail_index": 3.604977268827274
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020161638195060463,
        "excess_kurtosis": 8.187674948108578,
        "return_acf_1": -0.1459117487430216,
        "abs_return_acf_1": 0.42094456875618014,
        "abs_return_acf_5": 0.4698584050288041,
        "abs_return_acf_20": 0.29220714118607594,
        "quantile_01": -0.060210471179612424,
        "quantile_99": 0.05841912924817042,
        "hill_tail_index": 3.2587768933202637
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02170579326714625,
        "excess_kurtosis": 8.445350680661413,
        "return_acf_1": -0.13907571897907384,
        "abs_return_acf_1": 0.3852664696199254,
        "abs_return_acf_5": 0.4382277769473424,
        "abs_return_acf_20": 0.3320824805575772,
        "quantile_01": -0.07630647804615237,
        "quantile_99": 0.0645923836619029,
        "hill_tail_index": 4.094813544291858
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
