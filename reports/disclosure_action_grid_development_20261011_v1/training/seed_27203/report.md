# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27203
Run ID: `a23c077039a8abfccea3b8e5ae379e1e9580c2c14e273d9dec31292fa32481bc`
Result fingerprint: `48a0c6003e71d31f916317a6637536bb85efcfa0ee80eb1e307fb4dd018e1436`

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
    "equal_weight_sd": -0.7880515873015844,
    "equal_weight_raw": -11.820773809523763,
    "fixed_start_cap_weight_sd": -0.7483174540118391,
    "fixed_start_cap_weight_raw": -11.224761810177585,
    "end_cap_weight_sd": -0.7057660533756033,
    "end_cap_weight_raw": -10.58649080063405
  },
  "full_period_change": {
    "equal_weight_sd": -1.213037476154945,
    "equal_weight_raw": -18.195562142324174
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.131004738059707,
    "inflation_mean_sd": 0.5258683862433863
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.13258333333333636,
    "equal_weight_raw": 1.9887500000000449,
    "fixed_start_cap_weight_sd": 0.19249200743936642,
    "fixed_start_cap_weight_raw": 2.8873801115904953,
    "end_cap_weight_sd": 0.2379352415591383,
    "end_cap_weight_raw": 3.5690286233870734
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.729047619047616,
      "change_raw": -10.935714285714239,
      "decay_adjusted_gain_sd": 0.22333333333333635
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8418253968253935,
      "change_raw": -12.627380952380902,
      "decay_adjusted_gain_sd": 0.11055555555555878
    },
    "small": {
      "count": 18,
      "change_sd": -0.7709986772486743,
      "change_raw": -11.564980158730116,
      "decay_adjusted_gain_sd": 0.1284722222222251
    },
    "large_minus_small_sd": 0.04195105820105838,
    "large_minus_small_raw": 0.6292658730158757
  },
  "inflation": {
    "initial_mean_sd": 0.3035,
    "final_mean_sd": 0.5421666666666667,
    "mean_sd": 0.43118831529281154,
    "mean_absolute_raw_gap": 6.467824729392173,
    "final_absolute_raw_gap": 8.132499999999999,
    "mean_range_fraction": 0.06467824729392173
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.2655946446792778,
    "final_wealth_share": 0.35537395727341675
  },
  "pricing_slope": {
    "mean": -0.0022284852619445378,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.026680259988562136,
    "real_improvement_cost": 0.019994760438234355,
    "washing_cost": 0.006685499550327777,
    "fine_transfer": 0.020985268692765974,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.04766552868132811,
    "resource_cost_fraction_initial_cap": 0.0008893419996187377,
    "private_net_outflow_fraction_initial_cap": 0.00158885095604427,
    "fine_transfer_fraction_initial_cap": 0.0006995089564255324,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.000953615402671317,
    "unapplied_final_day_resource_cost": 1.1839833708107655e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 149.08025640324536,
    "beneficial_raw_gain_per_resource_cost": 2236.20384604868,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 3.0872930158479135,
    "baseline_accrued_cost": 2.976190476190478,
    "value_adjustment": -0.11110253965743595,
    "accrued_cost_fraction_initial_cap": 0.10290976719493043,
    "mean_contract_rate": 0.04375207919403024,
    "maximum_ledger_error": 4.743384504624082e-20
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
    "maximum_relative_cash_error": 2.261010021157282e-15,
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
      "minimum": -0.18732955956833428,
      "maximum": -0.07060508948590977,
      "mean": -0.11762982290989672,
      "median": -0.12478148039192347,
      "quantile_05": -0.1758117949940443,
      "quantile_95": -0.07377380523308662
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
      "minimum": 0.29207404391016706,
      "maximum": 0.7971895858148642,
      "mean": 0.5824799473050257,
      "median": 0.612615730107129,
      "quantile_05": 0.3391123040793173,
      "quantile_95": 0.7485488886639867
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
        "daily_volatility": 0.02071557604516876,
        "excess_kurtosis": 12.239382799407021,
        "return_acf_1": -0.1336845685961739,
        "abs_return_acf_1": 0.36680283422576015,
        "abs_return_acf_5": 0.3663355145768507,
        "abs_return_acf_20": 0.3238768369295502,
        "quantile_01": -0.0637213905192914,
        "quantile_99": 0.05602229510984314,
        "hill_tail_index": 2.957547235670378
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01934258919545946,
        "excess_kurtosis": 7.393998806360765,
        "return_acf_1": -0.14935458889857126,
        "abs_return_acf_1": 0.30797817447377634,
        "abs_return_acf_5": 0.3785649642658533,
        "abs_return_acf_20": 0.3037379777982328,
        "quantile_01": -0.06455465084253145,
        "quantile_99": 0.04914457331327225,
        "hill_tail_index": 2.7564796329214936
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01994265108387446,
        "excess_kurtosis": 9.11086685795767,
        "return_acf_1": -0.1577143574545451,
        "abs_return_acf_1": 0.3294728220058921,
        "abs_return_acf_5": 0.372081256786208,
        "abs_return_acf_20": 0.27026176206099045,
        "quantile_01": -0.0703918422050163,
        "quantile_99": 0.051227696302010864,
        "hill_tail_index": 3.5177054845639324
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02084038871762909,
        "excess_kurtosis": 11.884366913235663,
        "return_acf_1": -0.13664166257233554,
        "abs_return_acf_1": 0.42473513967844106,
        "abs_return_acf_5": 0.4435124944373772,
        "abs_return_acf_20": 0.3392213109084081,
        "quantile_01": -0.06050291928485636,
        "quantile_99": 0.05889034272079738,
        "hill_tail_index": 3.49491382719071
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018181774567996353,
        "excess_kurtosis": 4.439382809063257,
        "return_acf_1": -0.1253558888805577,
        "abs_return_acf_1": 0.33434378801136805,
        "abs_return_acf_5": 0.28762067791923196,
        "abs_return_acf_20": 0.27512249406494615,
        "quantile_01": -0.049307611070381736,
        "quantile_99": 0.05415624913741517,
        "hill_tail_index": 3.7397821707443324
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01921893849922561,
        "excess_kurtosis": 13.428312117088783,
        "return_acf_1": -0.09239082685844385,
        "abs_return_acf_1": 0.448077918758313,
        "abs_return_acf_5": 0.4452572270736788,
        "abs_return_acf_20": 0.30718020043708744,
        "quantile_01": -0.05827805192756382,
        "quantile_99": 0.057671090698733225,
        "hill_tail_index": 3.0010224603680467
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018798913561318582,
        "excess_kurtosis": 6.814852878947606,
        "return_acf_1": -0.16522109415514977,
        "abs_return_acf_1": 0.30241893646952356,
        "abs_return_acf_5": 0.3277682431690814,
        "abs_return_acf_20": 0.2553551333739172,
        "quantile_01": -0.0516820196187264,
        "quantile_99": 0.055250717379572864,
        "hill_tail_index": 2.8510079696985797
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017571720157706857,
        "excess_kurtosis": 7.511725752945045,
        "return_acf_1": -0.12420707190328921,
        "abs_return_acf_1": 0.3328287210907263,
        "abs_return_acf_5": 0.36727519375388656,
        "abs_return_acf_20": 0.2549812794547263,
        "quantile_01": -0.05051765499118059,
        "quantile_99": 0.04466642629940591,
        "hill_tail_index": 2.905981928915746
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018351379356857465,
        "excess_kurtosis": 6.649722962846436,
        "return_acf_1": -0.12984356578566786,
        "abs_return_acf_1": 0.36631635554940184,
        "abs_return_acf_5": 0.406268131339069,
        "abs_return_acf_20": 0.28782263175406964,
        "quantile_01": -0.05470855243405936,
        "quantile_99": 0.0557109534479711,
        "hill_tail_index": 3.656853759012165
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02060601926037292,
        "excess_kurtosis": 7.864831411804543,
        "return_acf_1": -0.0811380005448975,
        "abs_return_acf_1": 0.4861297593437803,
        "abs_return_acf_5": 0.48527239783870896,
        "abs_return_acf_20": 0.41421864682378545,
        "quantile_01": -0.06684758337913771,
        "quantile_99": 0.0716075649860878,
        "hill_tail_index": 3.6739094757050665
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018188350591296757,
        "excess_kurtosis": 10.541999689089536,
        "return_acf_1": -0.15010585985366134,
        "abs_return_acf_1": 0.23328297390510921,
        "abs_return_acf_5": 0.34337977721135887,
        "abs_return_acf_20": 0.27367957870895754,
        "quantile_01": -0.06270323152421459,
        "quantile_99": 0.04678077029641504,
        "hill_tail_index": 3.5627544546609506
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01773946117355992,
        "excess_kurtosis": 6.859107426950297,
        "return_acf_1": -0.1029416475292311,
        "abs_return_acf_1": 0.31705265229195084,
        "abs_return_acf_5": 0.3778756783734596,
        "abs_return_acf_20": 0.31698087051665275,
        "quantile_01": -0.05031953134609861,
        "quantile_99": 0.05287073661918338,
        "hill_tail_index": 2.73990565536125
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020071305551139937,
        "excess_kurtosis": 8.084528178590977,
        "return_acf_1": -0.08847218997951305,
        "abs_return_acf_1": 0.34815958573008937,
        "abs_return_acf_5": 0.33494310624177975,
        "abs_return_acf_20": 0.35501052049605036,
        "quantile_01": -0.05986545264487278,
        "quantile_99": 0.0623045402434851,
        "hill_tail_index": 3.011500559921222
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01903561016835235,
        "excess_kurtosis": 8.198076873458225,
        "return_acf_1": -0.1301298308247667,
        "abs_return_acf_1": 0.3730459728670044,
        "abs_return_acf_5": 0.42137514186927005,
        "abs_return_acf_20": 0.2845615847541691,
        "quantile_01": -0.05881934528735864,
        "quantile_99": 0.06140667420895878,
        "hill_tail_index": 2.8591137157539217
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017435251573867206,
        "excess_kurtosis": 4.330545821411508,
        "return_acf_1": -0.08514096124153925,
        "abs_return_acf_1": 0.2980335115571208,
        "abs_return_acf_5": 0.28248250935483615,
        "abs_return_acf_20": 0.23908066096894073,
        "quantile_01": -0.05231024499210747,
        "quantile_99": 0.05151647432583924,
        "hill_tail_index": 3.021712248391367
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02161741489227488,
        "excess_kurtosis": 16.854961110221513,
        "return_acf_1": -0.12636155208479516,
        "abs_return_acf_1": 0.36720626935514633,
        "abs_return_acf_5": 0.4137580306303015,
        "abs_return_acf_20": 0.2066534968770744,
        "quantile_01": -0.07196122500289663,
        "quantile_99": 0.05232427775688374,
        "hill_tail_index": 2.265361422388011
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020526786343017314,
        "excess_kurtosis": 11.983678107921806,
        "return_acf_1": -0.12873971166236228,
        "abs_return_acf_1": 0.3849982099793292,
        "abs_return_acf_5": 0.3945206687226061,
        "abs_return_acf_20": 0.2456021700415599,
        "quantile_01": -0.06513869390647789,
        "quantile_99": 0.061859559158715785,
        "hill_tail_index": 2.4131041193828495
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018350917278573013,
        "excess_kurtosis": 8.900118519446698,
        "return_acf_1": -0.07632590498099583,
        "abs_return_acf_1": 0.3103519981956022,
        "abs_return_acf_5": 0.36679696591591743,
        "abs_return_acf_20": 0.26806514349700256,
        "quantile_01": -0.060275526828068436,
        "quantile_99": 0.04237781900018315,
        "hill_tail_index": 2.9161872679486
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019024682084065762,
        "excess_kurtosis": 9.448776697183813,
        "return_acf_1": -0.09449114888594971,
        "abs_return_acf_1": 0.30446531305293745,
        "abs_return_acf_5": 0.4375880734245135,
        "abs_return_acf_20": 0.261419581933974,
        "quantile_01": -0.06139280812955806,
        "quantile_99": 0.04691827805663716,
        "hill_tail_index": 2.1720451197804165
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02090720603362679,
        "excess_kurtosis": 8.674018227767064,
        "return_acf_1": -0.11848847252104729,
        "abs_return_acf_1": 0.4144490908274475,
        "abs_return_acf_5": 0.43016997010138697,
        "abs_return_acf_20": 0.2710208007413418,
        "quantile_01": -0.060616988876653954,
        "quantile_99": 0.060639718721535334,
        "hill_tail_index": 3.1387681750647625
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019380980864307094,
        "excess_kurtosis": 7.329706766087808,
        "return_acf_1": -0.18447691386223078,
        "abs_return_acf_1": 0.3354836006233524,
        "abs_return_acf_5": 0.2866881186263062,
        "abs_return_acf_20": 0.27047012620086414,
        "quantile_01": -0.06127543712132414,
        "quantile_99": 0.06057159806352291,
        "hill_tail_index": 4.3713563433105165
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01980387883846091,
        "excess_kurtosis": 4.30684000986873,
        "return_acf_1": -0.07168572362116088,
        "abs_return_acf_1": 0.3257567343042894,
        "abs_return_acf_5": 0.38156035511031894,
        "abs_return_acf_20": 0.3547992213921745,
        "quantile_01": -0.06368925826734727,
        "quantile_99": 0.061564992133603016,
        "hill_tail_index": 3.6403906589722537
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019777020357198503,
        "excess_kurtosis": 6.008563441014093,
        "return_acf_1": -0.18732955956833428,
        "abs_return_acf_1": 0.3375091674564193,
        "abs_return_acf_5": 0.4136552199221322,
        "abs_return_acf_20": 0.35241296222209223,
        "quantile_01": -0.06177315623688864,
        "quantile_99": 0.06063403841703434,
        "hill_tail_index": 4.253256707743592
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01893141548875776,
        "excess_kurtosis": 7.632841162198195,
        "return_acf_1": -0.0801699278853747,
        "abs_return_acf_1": 0.2872499185566678,
        "abs_return_acf_5": 0.3789231718453436,
        "abs_return_acf_20": 0.29459045097208547,
        "quantile_01": -0.05668092200381242,
        "quantile_99": 0.05446296267218928,
        "hill_tail_index": 3.460149786907559
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018460922340303294,
        "excess_kurtosis": 10.102881074612554,
        "return_acf_1": -0.0962319984342144,
        "abs_return_acf_1": 0.31151190426637587,
        "abs_return_acf_5": 0.38278546973002353,
        "abs_return_acf_20": 0.22002731648560023,
        "quantile_01": -0.05628479322604765,
        "quantile_99": 0.047215826183774914,
        "hill_tail_index": 2.6605627202169186
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02093555994025682,
        "excess_kurtosis": 7.339204120446206,
        "return_acf_1": -0.1304670040491767,
        "abs_return_acf_1": 0.41238214514122257,
        "abs_return_acf_5": 0.48871757107451536,
        "abs_return_acf_20": 0.35616728551280546,
        "quantile_01": -0.06874654438736647,
        "quantile_99": 0.06291871883955272,
        "hill_tail_index": 3.4024304351108476
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01965759476372012,
        "excess_kurtosis": 6.551576909524643,
        "return_acf_1": -0.08221174738454923,
        "abs_return_acf_1": 0.3142848739427246,
        "abs_return_acf_5": 0.335183217473558,
        "abs_return_acf_20": 0.29045690044368044,
        "quantile_01": -0.0598605914232621,
        "quantile_99": 0.06302716170232599,
        "hill_tail_index": 3.521117839941361
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01842552561676682,
        "excess_kurtosis": 10.970547030712542,
        "return_acf_1": -0.07060508948590977,
        "abs_return_acf_1": 0.40449383486151885,
        "abs_return_acf_5": 0.4187002820055302,
        "abs_return_acf_20": 0.35579783495506967,
        "quantile_01": -0.060381909399529574,
        "quantile_99": 0.04591650435600744,
        "hill_tail_index": 2.632222526363712
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019982110703692203,
        "excess_kurtosis": 6.189397714141192,
        "return_acf_1": -0.08859229818254223,
        "abs_return_acf_1": 0.3795148147692392,
        "abs_return_acf_5": 0.33650811793071234,
        "abs_return_acf_20": 0.2839189320683071,
        "quantile_01": -0.05746808341642877,
        "quantile_99": 0.06672704744386404,
        "hill_tail_index": 3.7759156581526683
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0202175171754525,
        "excess_kurtosis": 11.794818265203382,
        "return_acf_1": -0.1403755196099149,
        "abs_return_acf_1": 0.37043482931134997,
        "abs_return_acf_5": 0.42644859023328135,
        "abs_return_acf_20": 0.31688102101004906,
        "quantile_01": -0.0686372503580673,
        "quantile_99": 0.05450613535136953,
        "hill_tail_index": 2.388064752534943
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
