# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27148
Run ID: `ee3e4ca8bc71f04a10b640365522379d96b17a861201dfd8060135ab0f0aae35`
Result fingerprint: `0e410b87350754829f24aac3330e2a8c4f3abbb0300fa2f198d16b8505264e98`

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
    "equal_weight_sd": -0.6992245924794754,
    "equal_weight_raw": -10.48836888719213,
    "fixed_start_cap_weight_sd": -0.6549908961063924,
    "fixed_start_cap_weight_raw": -9.824863441595888,
    "end_cap_weight_sd": -0.6722835069293149,
    "end_cap_weight_raw": -10.084252603939728
  },
  "full_period_change": {
    "equal_weight_sd": -1.1049150686699498,
    "equal_weight_raw": -16.573726030049247
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.030828630798021,
    "inflation_mean_sd": 0.6367027116402116
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.24416666666666964,
    "equal_weight_raw": 3.662500000000045,
    "fixed_start_cap_weight_sd": 0.28831257620992423,
    "fixed_start_cap_weight_raw": 4.324688643148864,
    "end_cap_weight_sd": 0.2659069411677011,
    "end_cap_weight_raw": 3.988604117515517
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5448809523809492,
      "change_raw": -8.173214285714238,
      "decay_adjusted_gain_sd": 0.4075000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6701930860427024,
      "change_raw": -10.052896290640536,
      "decay_adjusted_gain_sd": 0.25222222222222507
    },
    "small": {
      "count": 18,
      "change_sd": -0.7394642857142826,
      "change_raw": -11.091964285714239,
      "decay_adjusted_gain_sd": 0.2129166666666697
    },
    "large_minus_small_sd": 0.19458333333333333,
    "large_minus_small_raw": 2.91875
  },
  "inflation": {
    "initial_mean_sd": 0.30033333333333334,
    "final_mean_sd": 0.6683333333333333,
    "mean_sd": 0.5251443241742992,
    "mean_absolute_raw_gap": 7.877164862614488,
    "final_absolute_raw_gap": 10.024999999999999,
    "mean_range_fraction": 0.07877164862614489
  },
  "impact": {
    "initial_share": 0.18,
    "final_share": 0.17333333333333334,
    "initial_wealth_share": 0.23865429063952165,
    "final_wealth_share": 0.1978532391486845
  },
  "pricing_slope": {
    "mean": -0.00022802498986072302,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.06820700931440027,
    "real_improvement_cost": 0.05893820948187954,
    "washing_cost": 0.00926879983252074,
    "fine_transfer": 0.003344252584200515,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07155126189860078,
    "resource_cost_fraction_initial_cap": 0.0022735669771466755,
    "private_net_outflow_fraction_initial_cap": 0.0023850420632866923,
    "fine_transfer_fraction_initial_cap": 0.00011147508614001716,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.006930231181161277,
    "unapplied_final_day_resource_cost": 0.004217474857637426
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 107.39365460572381,
    "beneficial_raw_gain_per_resource_cost": 1610.904819085857,
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
    "accrued_cost": 3.157626356123136,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.18143587993265972,
    "accrued_cost_fraction_initial_cap": 0.10525421187077119,
    "mean_contract_rate": 0.043178929617298495,
    "maximum_ledger_error": 1.4907779871675686e-19
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.2605026603221741e-15,
    "maximum_absolute_share_error": 1.6653345369377348e-15,
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
      "minimum": -0.26638282581319517,
      "maximum": -0.13621120799484013,
      "mean": -0.20037143982375386,
      "median": -0.19983380150219554,
      "quantile_05": -0.25231815310496647,
      "quantile_95": -0.14313104116663056
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
      "minimum": 0.12493475466555809,
      "maximum": 0.8029167234189947,
      "mean": 0.5788433223923405,
      "median": 0.6118883862616382,
      "quantile_05": 0.23390977043275038,
      "quantile_95": 0.7558379168555349
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
        "daily_volatility": 0.016988316753236643,
        "excess_kurtosis": 3.0032156242247003,
        "return_acf_1": -0.1596046310365482,
        "abs_return_acf_1": 0.31884837095032903,
        "abs_return_acf_5": 0.3001652731491212,
        "abs_return_acf_20": 0.25232467740727915,
        "quantile_01": -0.04825302067912179,
        "quantile_99": 0.051376069046786633,
        "hill_tail_index": 4.580807932852908
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01771873092150845,
        "excess_kurtosis": 7.514262321800997,
        "return_acf_1": -0.22527002398857823,
        "abs_return_acf_1": 0.3708497854257958,
        "abs_return_acf_5": 0.2681762290785975,
        "abs_return_acf_20": 0.25711475023829067,
        "quantile_01": -0.05557707693687205,
        "quantile_99": 0.046842125895622234,
        "hill_tail_index": 2.941060636068552
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01845943941707103,
        "excess_kurtosis": 7.348624875327266,
        "return_acf_1": -0.18006532491834137,
        "abs_return_acf_1": 0.43789646448731273,
        "abs_return_acf_5": 0.285798931535815,
        "abs_return_acf_20": 0.24686567952148544,
        "quantile_01": -0.06698331241220536,
        "quantile_99": 0.042989937223745854,
        "hill_tail_index": 2.556520020270895
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022398575946304077,
        "excess_kurtosis": 12.720235923666136,
        "return_acf_1": -0.1841585324283289,
        "abs_return_acf_1": 0.4741667745615002,
        "abs_return_acf_5": 0.34237772268650557,
        "abs_return_acf_20": 0.2908885779855304,
        "quantile_01": -0.07621839925301159,
        "quantile_99": 0.05693506003702359,
        "hill_tail_index": 3.006538349627537
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020807472488216353,
        "excess_kurtosis": 7.036166079897569,
        "return_acf_1": -0.13621120799484013,
        "abs_return_acf_1": 0.4020299325378248,
        "abs_return_acf_5": 0.32463369284362187,
        "abs_return_acf_20": 0.30817511248438406,
        "quantile_01": -0.0687438661821656,
        "quantile_99": 0.056667151772942015,
        "hill_tail_index": 3.55138356262882
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019882297658991036,
        "excess_kurtosis": 8.70684249146039,
        "return_acf_1": -0.22601896567825694,
        "abs_return_acf_1": 0.41236214313504965,
        "abs_return_acf_5": 0.36678983293676953,
        "abs_return_acf_20": 0.3460673491050665,
        "quantile_01": -0.06491742300219798,
        "quantile_99": 0.0567310740569657,
        "hill_tail_index": 2.900252250130029
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017565152043930835,
        "excess_kurtosis": 5.642735733647964,
        "return_acf_1": -0.1626523639288542,
        "abs_return_acf_1": 0.3284848646535921,
        "abs_return_acf_5": 0.2388578327242152,
        "abs_return_acf_20": 0.1760403157372622,
        "quantile_01": -0.053131088088564975,
        "quantile_99": 0.04266656087930959,
        "hill_tail_index": 2.746575266656574
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018760503570252007,
        "excess_kurtosis": 11.47680410068583,
        "return_acf_1": -0.24089413802552606,
        "abs_return_acf_1": 0.46279779308853114,
        "abs_return_acf_5": 0.2692840159499731,
        "abs_return_acf_20": 0.3127721491407468,
        "quantile_01": -0.05987165118624204,
        "quantile_99": 0.04872891235703917,
        "hill_tail_index": 2.7175551869326453
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021167190286823984,
        "excess_kurtosis": 17.83266553436462,
        "return_acf_1": -0.17172984197647728,
        "abs_return_acf_1": 0.47601533560089593,
        "abs_return_acf_5": 0.3737935181401165,
        "abs_return_acf_20": 0.3685347274141056,
        "quantile_01": -0.07210966520511336,
        "quantile_99": 0.05525256939412746,
        "hill_tail_index": 2.5541951475057063
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021443709328696336,
        "excess_kurtosis": 33.99346446535197,
        "return_acf_1": -0.2147473404785296,
        "abs_return_acf_1": 0.37767095463927075,
        "abs_return_acf_5": 0.27085628365350467,
        "abs_return_acf_20": 0.2665621982877797,
        "quantile_01": -0.05617219250809204,
        "quantile_99": 0.0657003000315564,
        "hill_tail_index": 2.62062531901435
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01762145392501398,
        "excess_kurtosis": 4.8579254797745275,
        "return_acf_1": -0.14486539591790365,
        "abs_return_acf_1": 0.2855083193113475,
        "abs_return_acf_5": 0.3008583486077699,
        "abs_return_acf_20": 0.20863910074934736,
        "quantile_01": -0.053849675912769984,
        "quantile_99": 0.050740496262698886,
        "hill_tail_index": 3.1879245878305777
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021082200208675992,
        "excess_kurtosis": 14.79646221700369,
        "return_acf_1": -0.1976941657701622,
        "abs_return_acf_1": 0.41191661757159037,
        "abs_return_acf_5": 0.36620718584379525,
        "abs_return_acf_20": 0.28442770574502196,
        "quantile_01": -0.07365889444677425,
        "quantile_99": 0.05898990879428593,
        "hill_tail_index": 2.7204539187590724
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022163390481868887,
        "excess_kurtosis": 14.980470720992685,
        "return_acf_1": -0.22182933965450213,
        "abs_return_acf_1": 0.49633317775066843,
        "abs_return_acf_5": 0.3325111498970413,
        "abs_return_acf_20": 0.35040460845231464,
        "quantile_01": -0.08639112320642797,
        "quantile_99": 0.056129988047757894,
        "hill_tail_index": 3.9307952576959804
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01921872752437127,
        "excess_kurtosis": 7.042871629848797,
        "return_acf_1": -0.1772389513273463,
        "abs_return_acf_1": 0.4540875535676308,
        "abs_return_acf_5": 0.3358423015946683,
        "abs_return_acf_20": 0.29038892933756894,
        "quantile_01": -0.06908930650175858,
        "quantile_99": 0.052948751218357896,
        "hill_tail_index": 3.1430435885665005
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01948861933112199,
        "excess_kurtosis": 5.454297358768068,
        "return_acf_1": -0.19344932538621193,
        "abs_return_acf_1": 0.39620158899496444,
        "abs_return_acf_5": 0.3368119338893217,
        "abs_return_acf_20": 0.29366140587738154,
        "quantile_01": -0.06357848477728459,
        "quantile_99": 0.05636259764838865,
        "hill_tail_index": 3.812910193764014
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0221631152871107,
        "excess_kurtosis": 9.71801765334354,
        "return_acf_1": -0.23711128499749118,
        "abs_return_acf_1": 0.49734334350008325,
        "abs_return_acf_5": 0.3770411601605093,
        "abs_return_acf_20": 0.3157315026571963,
        "quantile_01": -0.0825629934812693,
        "quantile_99": 0.05994740693973851,
        "hill_tail_index": 4.389447979304997
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02035649705512249,
        "excess_kurtosis": 9.47733219621128,
        "return_acf_1": -0.17638123661494576,
        "abs_return_acf_1": 0.4781796353418421,
        "abs_return_acf_5": 0.3758922043992719,
        "abs_return_acf_20": 0.2713842657635755,
        "quantile_01": -0.06969280688636632,
        "quantile_99": 0.06651259282570879,
        "hill_tail_index": 3.215707989088945
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01771384062554643,
        "excess_kurtosis": 5.253433237966316,
        "return_acf_1": -0.15878678921572875,
        "abs_return_acf_1": 0.32691319090364246,
        "abs_return_acf_5": 0.2862215667737967,
        "abs_return_acf_20": 0.2651711684413116,
        "quantile_01": -0.054484080630036215,
        "quantile_99": 0.04430593363655411,
        "hill_tail_index": 3.4020670374009674
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019148850604164804,
        "excess_kurtosis": 14.420556281539358,
        "return_acf_1": -0.23094549611281215,
        "abs_return_acf_1": 0.3735619274921647,
        "abs_return_acf_5": 0.27295383677145835,
        "abs_return_acf_20": 0.3089282762179985,
        "quantile_01": -0.061770708303485876,
        "quantile_99": 0.04661118402055142,
        "hill_tail_index": 2.351186623957309
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02176530117532093,
        "excess_kurtosis": 12.486792314354549,
        "return_acf_1": -0.26638282581319517,
        "abs_return_acf_1": 0.49899636050415147,
        "abs_return_acf_5": 0.38249672798323214,
        "abs_return_acf_20": 0.36865332969492187,
        "quantile_01": -0.07818354823231533,
        "quantile_99": 0.05322986129257368,
        "hill_tail_index": 3.0633456509473294
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01839450971839588,
        "excess_kurtosis": 6.644361363837334,
        "return_acf_1": -0.2396925760384756,
        "abs_return_acf_1": 0.40814478779537744,
        "abs_return_acf_5": 0.29992592568346516,
        "abs_return_acf_20": 0.24436123510800073,
        "quantile_01": -0.06469527193787314,
        "quantile_99": 0.04962649463065018,
        "hill_tail_index": 2.9816420753177897
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020471368531603407,
        "excess_kurtosis": 13.187149798187008,
        "return_acf_1": -0.23136385854770403,
        "abs_return_acf_1": 0.49674043997605144,
        "abs_return_acf_5": 0.27883342202089006,
        "abs_return_acf_20": 0.28884894716689585,
        "quantile_01": -0.06951052274371645,
        "quantile_99": 0.048968793415160784,
        "hill_tail_index": 2.7772971188747757
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02408445031451066,
        "excess_kurtosis": 43.06680240598069,
        "return_acf_1": -0.26166507453359955,
        "abs_return_acf_1": 0.4283367334198521,
        "abs_return_acf_5": 0.27736849216678217,
        "abs_return_acf_20": 0.2476806229424459,
        "quantile_01": -0.06362965008688246,
        "quantile_99": 0.0653578957944056,
        "hill_tail_index": 2.5235749675281833
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022508460849543117,
        "excess_kurtosis": 13.076168935186654,
        "return_acf_1": -0.18675698575603508,
        "abs_return_acf_1": 0.5005165913405608,
        "abs_return_acf_5": 0.3613256471622941,
        "abs_return_acf_20": 0.2790540210000438,
        "quantile_01": -0.08986895636375516,
        "quantile_99": 0.05557869057548291,
        "hill_tail_index": 2.2360375032063184
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020283748051906,
        "excess_kurtosis": 17.68571281822674,
        "return_acf_1": -0.24050408978982252,
        "abs_return_acf_1": 0.45901066838265947,
        "abs_return_acf_5": 0.3799401882552956,
        "abs_return_acf_20": 0.35784917353302015,
        "quantile_01": -0.06613713398529403,
        "quantile_99": 0.053092117437016834,
        "hill_tail_index": 2.6768408748260613
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018505589124640474,
        "excess_kurtosis": 19.868963416240945,
        "return_acf_1": -0.20197343723422886,
        "abs_return_acf_1": 0.32509217149681124,
        "abs_return_acf_5": 0.32858110363597665,
        "abs_return_acf_20": 0.16489672592159757,
        "quantile_01": -0.04481149936221463,
        "quantile_99": 0.04438736671783095,
        "hill_tail_index": 1.7004566723145738
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018673537607417124,
        "excess_kurtosis": 5.423439556775213,
        "return_acf_1": -0.21426248205594636,
        "abs_return_acf_1": 0.3784413071133793,
        "abs_return_acf_5": 0.30141094430979865,
        "abs_return_acf_20": 0.2980671805174127,
        "quantile_01": -0.05769862322312804,
        "quantile_99": 0.05344143248442574,
        "hill_tail_index": 3.7368912331064363
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019889523362192622,
        "excess_kurtosis": 8.46059904228711,
        "return_acf_1": -0.23442327335519164,
        "abs_return_acf_1": 0.457892891605784,
        "abs_return_acf_5": 0.32386098296951865,
        "abs_return_acf_20": 0.2682412025802887,
        "quantile_01": -0.07393953525271428,
        "quantile_99": 0.05348880665398812,
        "hill_tail_index": 3.3656802874136167
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019292416174478497,
        "excess_kurtosis": 2.889757079684946,
        "return_acf_1": -0.14171202364286165,
        "abs_return_acf_1": 0.35680650385094526,
        "abs_return_acf_5": 0.2864584336092435,
        "abs_return_acf_20": 0.29928696998942056,
        "quantile_01": -0.05848455626877079,
        "quantile_99": 0.05382873229107086,
        "hill_tail_index": 4.704666542726476
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016769440406562947,
        "excess_kurtosis": 2.1621550795540863,
        "return_acf_1": -0.15275221249417065,
        "abs_return_acf_1": 0.24788852483670368,
        "abs_return_acf_5": 0.21619881839824664,
        "abs_return_acf_20": 0.1932054569573121,
        "quantile_01": -0.04731881829116575,
        "quantile_99": 0.04618755439398938,
        "hill_tail_index": 5.798408338830991
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
