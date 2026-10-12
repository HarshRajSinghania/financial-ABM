# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27058
Run ID: `0384f53362c41eddc89b3b3fb54dab2f6bd218c478df94a1d68845dee83e09ef`
Result fingerprint: `7c17bfc69df28dc5adbb8d0b1b66d8f417d872fadcb36286878cea4c54b71f13`

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
    "equal_weight_sd": -0.5591309523809492,
    "equal_weight_raw": -8.386964285714237,
    "fixed_start_cap_weight_sd": -0.5118823658526485,
    "fixed_start_cap_weight_raw": -7.678235487789728,
    "end_cap_weight_sd": -0.5198207732144506,
    "end_cap_weight_raw": -7.797311598216759
  },
  "full_period_change": {
    "equal_weight_sd": -0.9242380952380905,
    "equal_weight_raw": -13.863571428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8947526455026409,
    "inflation_mean_sd": 0.6294460978835977
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.38889760212828806,
    "equal_weight_raw": 5.833464031924321,
    "fixed_start_cap_weight_sd": 0.4373653159348282,
    "fixed_start_cap_weight_raw": 6.560479739022425,
    "end_cap_weight_sd": 0.4277065975600054,
    "end_cap_weight_raw": 6.415598963400082
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5082142857142825,
      "change_raw": -7.623214285714238,
      "decay_adjusted_gain_sd": 0.4441666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.453769841269838,
      "change_raw": -6.80654761904757,
      "decay_adjusted_gain_sd": 0.4986111111111142
    },
    "small": {
      "count": 18,
      "change_sd": -0.6202976190476158,
      "change_raw": -9.304464285714237,
      "decay_adjusted_gain_sd": 0.32482933688047805
    },
    "large_minus_small_sd": 0.11208333333333331,
    "large_minus_small_raw": 1.6812499999999997
  },
  "inflation": {
    "initial_mean_sd": 0.316,
    "final_mean_sd": 0.5971666666666666,
    "mean_sd": 0.5225108243130724,
    "mean_absolute_raw_gap": 7.8376623646960875,
    "final_absolute_raw_gap": 8.9575,
    "mean_range_fraction": 0.07837662364696088
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.28,
    "initial_wealth_share": 0.3563031842346731,
    "final_wealth_share": 0.3485334850160653
  },
  "pricing_slope": {
    "mean": -3.975953625721427e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.11074195057444144,
    "real_improvement_cost": 0.08450072287928401,
    "washing_cost": 0.026241227695157448,
    "fine_transfer": 0.026834063582619666,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1375760141570611,
    "resource_cost_fraction_initial_cap": 0.003691398352481383,
    "private_net_outflow_fraction_initial_cap": 0.0045858671385687055,
    "fine_transfer_fraction_initial_cap": 0.0008944687860873226,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010476280874357987,
    "unapplied_final_day_resource_cost": 0.003482278589888198
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 105.3523800450495,
    "beneficial_raw_gain_per_resource_cost": 1580.2857006757424,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 2.8906988277624723,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.085491648428004,
    "accrued_cost_fraction_initial_cap": 0.09635662759208244,
    "mean_contract_rate": 0.040274089944825404,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 1.1831018549677722e-15,
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
      "minimum": -0.170187256476557,
      "maximum": -0.029180771141299258,
      "mean": -0.10001310007517862,
      "median": -0.0987069124640563,
      "quantile_05": -0.16446633828711843,
      "quantile_95": -0.037251205799858564
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
      "minimum": 0.26050869988171066,
      "maximum": 0.76528495892547,
      "mean": 0.46467207092610313,
      "median": 0.4185903513534614,
      "quantile_05": 0.3055196605768793,
      "quantile_95": 0.714030123305683
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
        "daily_volatility": 0.017510145263838046,
        "excess_kurtosis": 4.819906841208852,
        "return_acf_1": -0.16764384148952785,
        "abs_return_acf_1": 0.21772501072415196,
        "abs_return_acf_5": 0.23202169917953433,
        "abs_return_acf_20": 0.23042033937196876,
        "quantile_01": -0.04844997391524961,
        "quantile_99": 0.04836405260962105,
        "hill_tail_index": 3.3630654974608216
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01793024323507487,
        "excess_kurtosis": 12.077694117891017,
        "return_acf_1": -0.11746046446960115,
        "abs_return_acf_1": 0.37570330856728934,
        "abs_return_acf_5": 0.3630902065012509,
        "abs_return_acf_20": 0.3195205335700933,
        "quantile_01": -0.05642913349386035,
        "quantile_99": 0.04510146074031369,
        "hill_tail_index": 1.7920541342715701
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.0172098490402104,
        "excess_kurtosis": 5.20547588338523,
        "return_acf_1": -0.054824174449062596,
        "abs_return_acf_1": 0.30306870595648355,
        "abs_return_acf_5": 0.30227635115430423,
        "abs_return_acf_20": 0.20435356320477832,
        "quantile_01": -0.05157920689392265,
        "quantile_99": 0.04254876470127159,
        "hill_tail_index": 2.903264730887883
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0188192530711965,
        "excess_kurtosis": 5.498603798238474,
        "return_acf_1": -0.14926415340326477,
        "abs_return_acf_1": 0.36780192898023306,
        "abs_return_acf_5": 0.2743557608344649,
        "abs_return_acf_20": 0.3246629465438584,
        "quantile_01": -0.06088952494427724,
        "quantile_99": 0.05786400191596043,
        "hill_tail_index": 3.1960460601815948
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017529585260867654,
        "excess_kurtosis": 6.0279224353699945,
        "return_acf_1": -0.11769401018672036,
        "abs_return_acf_1": 0.3506378492191094,
        "abs_return_acf_5": 0.2455876235355377,
        "abs_return_acf_20": 0.30828200893352686,
        "quantile_01": -0.050457271643441305,
        "quantile_99": 0.045388809474557396,
        "hill_tail_index": 3.071408446713093
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017986399572229708,
        "excess_kurtosis": 5.395434270162257,
        "return_acf_1": -0.12853956548562304,
        "abs_return_acf_1": 0.3393891660810465,
        "abs_return_acf_5": 0.19971210423105484,
        "abs_return_acf_20": 0.2857730942828325,
        "quantile_01": -0.057476931047913835,
        "quantile_99": 0.047447642305991404,
        "hill_tail_index": 4.074627656631693
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01863408593536613,
        "excess_kurtosis": 9.348660664512133,
        "return_acf_1": -0.1484486940827246,
        "abs_return_acf_1": 0.33119019178722786,
        "abs_return_acf_5": 0.32220590468825644,
        "abs_return_acf_20": 0.3253644054722373,
        "quantile_01": -0.05946346792683719,
        "quantile_99": 0.04948968388100251,
        "hill_tail_index": 2.51898686029876
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018799732999723415,
        "excess_kurtosis": 5.556439402533362,
        "return_acf_1": -0.0744823766391757,
        "abs_return_acf_1": 0.3952367023288867,
        "abs_return_acf_5": 0.3937852729147976,
        "abs_return_acf_20": 0.297855694254103,
        "quantile_01": -0.05882737419545878,
        "quantile_99": 0.059540199943769544,
        "hill_tail_index": 3.550265201650199
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01776133293973666,
        "excess_kurtosis": 3.911965813733458,
        "return_acf_1": -0.1605827232619514,
        "abs_return_acf_1": 0.29619002510997644,
        "abs_return_acf_5": 0.20068568504360057,
        "abs_return_acf_20": 0.2573112981674179,
        "quantile_01": -0.05594598768518921,
        "quantile_99": 0.04442936363354749,
        "hill_tail_index": 3.649106242503902
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018682010606611642,
        "excess_kurtosis": 5.0588768924114405,
        "return_acf_1": -0.11730646484099912,
        "abs_return_acf_1": 0.37447124560824363,
        "abs_return_acf_5": 0.3384925524390648,
        "abs_return_acf_20": 0.3394830819261711,
        "quantile_01": -0.05495475801205306,
        "quantile_99": 0.0473792301410779,
        "hill_tail_index": 3.367952288149242
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017600366993421927,
        "excess_kurtosis": 6.580549829383072,
        "return_acf_1": -0.170187256476557,
        "abs_return_acf_1": 0.29036226005066834,
        "abs_return_acf_5": 0.24894747425466685,
        "abs_return_acf_20": 0.2731568039630622,
        "quantile_01": -0.05869822520378116,
        "quantile_99": 0.05563827670467391,
        "hill_tail_index": 2.810600916490772
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01713490178715899,
        "excess_kurtosis": 2.3605073822657454,
        "return_acf_1": -0.1292496262512274,
        "abs_return_acf_1": 0.336523930553398,
        "abs_return_acf_5": 0.21854218905139652,
        "abs_return_acf_20": 0.2661411002554731,
        "quantile_01": -0.04925915848437809,
        "quantile_99": 0.044272880903066095,
        "hill_tail_index": 4.410090956345443
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.015459899088571274,
        "excess_kurtosis": 3.5159980760222025,
        "return_acf_1": -0.057344829679030124,
        "abs_return_acf_1": 0.21697012514742112,
        "abs_return_acf_5": 0.24115520881702743,
        "abs_return_acf_20": 0.17777410876522529,
        "quantile_01": -0.046982687640666376,
        "quantile_99": 0.0420866348707766,
        "hill_tail_index": 3.6391225343877838
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017248397741750816,
        "excess_kurtosis": 3.7362267773657356,
        "return_acf_1": -0.13659005622469672,
        "abs_return_acf_1": 0.3097747681476231,
        "abs_return_acf_5": 0.2928372581926869,
        "abs_return_acf_20": 0.2505430781374741,
        "quantile_01": -0.049610947869757484,
        "quantile_99": 0.04684424573500561,
        "hill_tail_index": 3.7662196946016655
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01877587455648064,
        "excess_kurtosis": 2.117782621203272,
        "return_acf_1": -0.07192123985250773,
        "abs_return_acf_1": 0.2591342299238519,
        "abs_return_acf_5": 0.2092849606423168,
        "abs_return_acf_20": 0.2950159500410705,
        "quantile_01": -0.05448270354494085,
        "quantile_99": 0.0526283420273516,
        "hill_tail_index": 6.229885470439035
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016942921575468225,
        "excess_kurtosis": 5.548368156363663,
        "return_acf_1": -0.08049536693528683,
        "abs_return_acf_1": 0.22563843096746483,
        "abs_return_acf_5": 0.27913149136969034,
        "abs_return_acf_20": 0.2202803408181446,
        "quantile_01": -0.04309870384076796,
        "quantile_99": 0.04804560366777003,
        "hill_tail_index": 2.9138862030048855
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019452964985486206,
        "excess_kurtosis": 7.394706562232825,
        "return_acf_1": -0.11994781742466165,
        "abs_return_acf_1": 0.35891552384701714,
        "abs_return_acf_5": 0.27741556104607595,
        "abs_return_acf_20": 0.3484915367206731,
        "quantile_01": -0.06621538326124539,
        "quantile_99": 0.056015786804106245,
        "hill_tail_index": 3.607664664162771
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01719374998374792,
        "excess_kurtosis": 12.47903078308999,
        "return_acf_1": -0.04231608604107456,
        "abs_return_acf_1": 0.3551811198585252,
        "abs_return_acf_5": 0.2655605631673516,
        "abs_return_acf_20": 0.270143909454366,
        "quantile_01": -0.04685077262467361,
        "quantile_99": 0.0390745722052597,
        "hill_tail_index": 2.018820468085993
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01754306220226165,
        "excess_kurtosis": 8.849396954838918,
        "return_acf_1": -0.08904554911806459,
        "abs_return_acf_1": 0.4010246078350472,
        "abs_return_acf_5": 0.31494576905385296,
        "abs_return_acf_20": 0.3053873606063258,
        "quantile_01": -0.05427151610889675,
        "quantile_99": 0.047830330429096124,
        "hill_tail_index": 2.1263567393970266
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.015564653357081655,
        "excess_kurtosis": 4.97006230233851,
        "return_acf_1": -0.10757030973639109,
        "abs_return_acf_1": 0.20187941526930075,
        "abs_return_acf_5": 0.20378748895835094,
        "abs_return_acf_20": 0.19009737719271594,
        "quantile_01": -0.043489716789523035,
        "quantile_99": 0.03804877617652944,
        "hill_tail_index": 3.165116471849697
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019101817497942698,
        "excess_kurtosis": 7.468891996364416,
        "return_acf_1": -0.06886064705227359,
        "abs_return_acf_1": 0.2457431999777679,
        "abs_return_acf_5": 0.2694088331253662,
        "abs_return_acf_20": 0.30865340848497685,
        "quantile_01": -0.06450923436989987,
        "quantile_99": 0.05621837348712076,
        "hill_tail_index": 2.820905662060043
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017066061852595293,
        "excess_kurtosis": 3.960477420877611,
        "return_acf_1": -0.05262742153978715,
        "abs_return_acf_1": 0.2139144825328727,
        "abs_return_acf_5": 0.2484879141143976,
        "abs_return_acf_20": 0.23772049878501533,
        "quantile_01": -0.05175340571241238,
        "quantile_99": 0.04639366347218577,
        "hill_tail_index": 4.204217249298407
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019506357491082236,
        "excess_kurtosis": 19.418422568634565,
        "return_acf_1": -0.15303565082742546,
        "abs_return_acf_1": 0.4196714271936376,
        "abs_return_acf_5": 0.4559333392742145,
        "abs_return_acf_20": 0.38063911677958956,
        "quantile_01": -0.04763710415510335,
        "quantile_99": 0.058001229913472986,
        "hill_tail_index": 1.6909818235331593
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019573950764329842,
        "excess_kurtosis": 14.589873044017555,
        "return_acf_1": -0.06422261723693785,
        "abs_return_acf_1": 0.3285183585369417,
        "abs_return_acf_5": 0.28022759424620386,
        "abs_return_acf_20": 0.37129622539972523,
        "quantile_01": -0.06066455858081715,
        "quantile_99": 0.04802136081558556,
        "hill_tail_index": 2.228957291582486
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017061301697916777,
        "excess_kurtosis": 15.098493585300346,
        "return_acf_1": -0.03310721287522725,
        "abs_return_acf_1": 0.2561698295450537,
        "abs_return_acf_5": 0.3475688054874921,
        "abs_return_acf_20": 0.19276018218596008,
        "quantile_01": -0.04909053731763925,
        "quantile_99": 0.03378478236506393,
        "hill_tail_index": 1.671272253752922
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01585834966848245,
        "excess_kurtosis": 1.845086504885594,
        "return_acf_1": -0.07545027329874751,
        "abs_return_acf_1": 0.21972428761953358,
        "abs_return_acf_5": 0.2447720683587815,
        "abs_return_acf_20": 0.23622651500273756,
        "quantile_01": -0.041004368332904606,
        "quantile_99": 0.04624387973975066,
        "hill_tail_index": 4.664563100530724
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018994323603828918,
        "excess_kurtosis": 6.292491201865452,
        "return_acf_1": -0.08984351519172151,
        "abs_return_acf_1": 0.3107579802115012,
        "abs_return_acf_5": 0.30333784703916616,
        "abs_return_acf_20": 0.3713909313464305,
        "quantile_01": -0.05842589254828466,
        "quantile_99": 0.053042207609383794,
        "hill_tail_index": 3.1311385611361917
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017805275239376098,
        "excess_kurtosis": 7.618690852732941,
        "return_acf_1": -0.029180771141299258,
        "abs_return_acf_1": 0.27550695158752153,
        "abs_return_acf_5": 0.3256179972542807,
        "abs_return_acf_20": 0.25125182193466267,
        "quantile_01": -0.058818616451179154,
        "quantile_99": 0.04929155590190069,
        "hill_tail_index": 3.3245249743815144
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.016869218842730595,
        "excess_kurtosis": 3.598980114116644,
        "return_acf_1": -0.13175048918494872,
        "abs_return_acf_1": 0.21697171956349706,
        "abs_return_acf_5": 0.28237889764174634,
        "abs_return_acf_20": 0.3039009221354611,
        "quantile_01": -0.043527305420012416,
        "quantile_99": 0.04566846292389181,
        "hill_tail_index": 3.28155507819956
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01868802329260386,
        "excess_kurtosis": 13.205674386258764,
        "return_acf_1": -0.061399797858841004,
        "abs_return_acf_1": 0.3543896140728518,
        "abs_return_acf_5": 0.4008763988923993,
        "abs_return_acf_20": 0.3846381985180774,
        "quantile_01": -0.06640673016694751,
        "quantile_99": 0.04876053728514788,
        "hill_tail_index": 2.513248384252493
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
