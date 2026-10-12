# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27253
Run ID: `47b075859c9ffec2f72995f6ff3fc8a18c79398442b678c29e9f18d818a8d602`
Result fingerprint: `93e72099381aa0cfc20d71752a84fd4ad673344865a616760835221dfc91ce17`

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
    "equal_weight_sd": -0.7864642857142824,
    "equal_weight_raw": -11.796964285714237,
    "fixed_start_cap_weight_sd": -0.7263549311191693,
    "fixed_start_cap_weight_raw": -10.89532396678754,
    "end_cap_weight_sd": -0.6873740117717708,
    "end_cap_weight_raw": -10.310610176576562
  },
  "full_period_change": {
    "equal_weight_sd": -1.2119880952380906,
    "equal_weight_raw": -18.17982142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1488015873015829,
    "inflation_mean_sd": 0.8722890211640213
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.16591666666666993,
    "equal_weight_raw": 2.488750000000048,
    "fixed_start_cap_weight_sd": 0.22602602126178295,
    "fixed_start_cap_weight_raw": 3.390390318926744,
    "end_cap_weight_sd": 0.26500694060918156,
    "end_cap_weight_raw": 3.9751041091377246
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6373809523809492,
      "change_raw": -9.560714285714237,
      "decay_adjusted_gain_sd": 0.315000000000003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7004365079365047,
      "change_raw": -10.50654761904757,
      "decay_adjusted_gain_sd": 0.25194444444444763
    },
    "small": {
      "count": 18,
      "change_sd": -0.8543253968253937,
      "change_raw": -12.814880952380905,
      "decay_adjusted_gain_sd": 0.09805555555555881
    },
    "large_minus_small_sd": 0.2169444444444445,
    "large_minus_small_raw": 3.2541666666666673
  },
  "inflation": {
    "initial_mean_sd": 0.24333333333333332,
    "final_mean_sd": 0.8480000000000002,
    "mean_sd": 0.6539797391063003,
    "mean_absolute_raw_gap": 9.809696086594506,
    "final_absolute_raw_gap": 12.72,
    "mean_range_fraction": 0.09809696086594506
  },
  "impact": {
    "initial_share": 0.36666666666666664,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.3358280425740856,
    "final_wealth_share": 0.3759148504824977
  },
  "pricing_slope": {
    "mean": -0.0014948373057232715,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.021189564802813254,
    "real_improvement_cost": 0.006810845019406795,
    "washing_cost": 0.01437871978340646,
    "fine_transfer": 0.011156762290033546,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0323463270928468,
    "resource_cost_fraction_initial_cap": 0.0007063188267604418,
    "private_net_outflow_fraction_initial_cap": 0.0010782109030948934,
    "fine_transfer_fraction_initial_cap": 0.00037189207633445153,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0008784523309606984,
    "unapplied_final_day_resource_cost": 6.614626773591887e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 234.90336145739317,
    "beneficial_raw_gain_per_resource_cost": 3523.5504218608976,
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
    "accrued_cost": 3.0920129778947905,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.11582250170431393,
    "accrued_cost_fraction_initial_cap": 0.10306709926315968,
    "mean_contract_rate": 0.04319205987690542,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "price_cap_hits": 17,
    "maximum_relative_cash_error": 1.0797704783083007e-15,
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
      "minimum": -0.2219133091593478,
      "maximum": -0.053197622536446255,
      "mean": -0.1349587458351954,
      "median": -0.14227038086783483,
      "quantile_05": -0.203282130779528,
      "quantile_95": -0.05911595699943327
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
      "minimum": 0.12807389148818094,
      "maximum": 0.8221281224459657,
      "mean": 0.5245482375084934,
      "median": 0.5603979400640338,
      "quantile_05": 0.2046690043338337,
      "quantile_95": 0.7823589694748595
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
        "daily_volatility": 0.01660462986195737,
        "excess_kurtosis": 3.4485900642378757,
        "return_acf_1": -0.10054892035092258,
        "abs_return_acf_1": 0.2735132007654602,
        "abs_return_acf_5": 0.32057180349014625,
        "abs_return_acf_20": 0.21370554300956857,
        "quantile_01": -0.052890047398000725,
        "quantile_99": 0.04210413100484236,
        "hill_tail_index": 3.89281043059313
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017090268065527988,
        "excess_kurtosis": 7.6751841299623536,
        "return_acf_1": -0.15652170095008155,
        "abs_return_acf_1": 0.2923555047451747,
        "abs_return_acf_5": 0.2778939307495504,
        "abs_return_acf_20": 0.21185465757023064,
        "quantile_01": -0.05055465498398666,
        "quantile_99": 0.045587269745849465,
        "hill_tail_index": 3.2105805698038683
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017190137410628324,
        "excess_kurtosis": 10.03629258310845,
        "return_acf_1": -0.15927505044526002,
        "abs_return_acf_1": 0.31236192659086015,
        "abs_return_acf_5": 0.3126137187051246,
        "abs_return_acf_20": 0.2337204422437846,
        "quantile_01": -0.05165322793936109,
        "quantile_99": 0.03908821299364216,
        "hill_tail_index": 2.1688391695771134
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020019071243511707,
        "excess_kurtosis": 12.689216224926971,
        "return_acf_1": -0.09427888490458441,
        "abs_return_acf_1": 0.4150870921590525,
        "abs_return_acf_5": 0.43749850770278703,
        "abs_return_acf_20": 0.35822256172929007,
        "quantile_01": -0.06607796201592589,
        "quantile_99": 0.05956346192436139,
        "hill_tail_index": 2.69638926004242
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016619556018932537,
        "excess_kurtosis": 6.487145912023832,
        "return_acf_1": -0.1383870441772144,
        "abs_return_acf_1": 0.3651645755009538,
        "abs_return_acf_5": 0.3401962544408886,
        "abs_return_acf_20": 0.2708303838945855,
        "quantile_01": -0.05725912325298331,
        "quantile_99": 0.04309900888864288,
        "hill_tail_index": 3.43192635729288
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017151817964952614,
        "excess_kurtosis": 10.957605806516922,
        "return_acf_1": -0.053197622536446255,
        "abs_return_acf_1": 0.35295013610271975,
        "abs_return_acf_5": 0.33918877884032095,
        "abs_return_acf_20": 0.22908507637201586,
        "quantile_01": -0.056278739141309285,
        "quantile_99": 0.04829228667331627,
        "hill_tail_index": 2.283784694939271
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01887711269872155,
        "excess_kurtosis": 13.507421882592439,
        "return_acf_1": -0.12855303385024142,
        "abs_return_acf_1": 0.5177542559636769,
        "abs_return_acf_5": 0.3442980315633368,
        "abs_return_acf_20": 0.34279399172834135,
        "quantile_01": -0.06527564150026412,
        "quantile_99": 0.046330892611757955,
        "hill_tail_index": 2.638630200174672
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019657828720415264,
        "excess_kurtosis": 8.589769408134089,
        "return_acf_1": -0.15457249635753523,
        "abs_return_acf_1": 0.47383013800432294,
        "abs_return_acf_5": 0.3891031650529145,
        "abs_return_acf_20": 0.316953029917375,
        "quantile_01": -0.0667252742388888,
        "quantile_99": 0.06007919224099974,
        "hill_tail_index": 3.2506234808421217
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0191731347614305,
        "excess_kurtosis": 13.141984757752024,
        "return_acf_1": -0.14195177445778853,
        "abs_return_acf_1": 0.35481580695978576,
        "abs_return_acf_5": 0.35404163155205376,
        "abs_return_acf_20": 0.34072889919789856,
        "quantile_01": -0.06693592074697492,
        "quantile_99": 0.04963392278855273,
        "hill_tail_index": 2.0552200150566535
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.015981237634016616,
        "excess_kurtosis": 4.945461307026142,
        "return_acf_1": -0.11892394452807735,
        "abs_return_acf_1": 0.3460977156343221,
        "abs_return_acf_5": 0.3211282448096822,
        "abs_return_acf_20": 0.27539669251277,
        "quantile_01": -0.047062293012885635,
        "quantile_99": 0.041254253395937864,
        "hill_tail_index": 3.153685607056425
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018517192440926842,
        "excess_kurtosis": 5.968376435414989,
        "return_acf_1": -0.2048963490995961,
        "abs_return_acf_1": 0.3631055596776443,
        "abs_return_acf_5": 0.35002489018454763,
        "abs_return_acf_20": 0.3172789309934155,
        "quantile_01": -0.05415158828519247,
        "quantile_99": 0.05499949539673065,
        "hill_tail_index": 4.180002613441716
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021731372043402825,
        "excess_kurtosis": 18.78393069381441,
        "return_acf_1": -0.09160919805531394,
        "abs_return_acf_1": 0.5604730091187522,
        "abs_return_acf_5": 0.457371942907178,
        "abs_return_acf_20": 0.35538991021282385,
        "quantile_01": -0.07959226601287607,
        "quantile_99": 0.05771667408169924,
        "hill_tail_index": 2.001325025489345
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01771974889637164,
        "excess_kurtosis": 23.10414509479476,
        "return_acf_1": -0.2219133091593478,
        "abs_return_acf_1": 0.2884015027216565,
        "abs_return_acf_5": 0.1797763474211267,
        "abs_return_acf_20": 0.20102565999934421,
        "quantile_01": -0.04521913115939051,
        "quantile_99": 0.057168461872075776,
        "hill_tail_index": 3.244086026226244
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.0177719819689661,
        "excess_kurtosis": 5.883485418172956,
        "return_acf_1": -0.07781821324408887,
        "abs_return_acf_1": 0.31827035874917,
        "abs_return_acf_5": 0.3196440893184184,
        "abs_return_acf_20": 0.30120813907395927,
        "quantile_01": -0.054463367131693544,
        "quantile_99": 0.04669270640111693,
        "hill_tail_index": 2.875349526700074
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016801510616042476,
        "excess_kurtosis": 6.694494169953316,
        "return_acf_1": -0.05813364689461507,
        "abs_return_acf_1": 0.3248279090756622,
        "abs_return_acf_5": 0.31556385200113946,
        "abs_return_acf_20": 0.28607370499979023,
        "quantile_01": -0.054575177283499324,
        "quantile_99": 0.046049428821296715,
        "hill_tail_index": 2.8268810731185785
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018885708326232084,
        "excess_kurtosis": 6.80728979008078,
        "return_acf_1": -0.14307597892699556,
        "abs_return_acf_1": 0.28907263274072675,
        "abs_return_acf_5": 0.3316958569330897,
        "abs_return_acf_20": 0.3003727347672304,
        "quantile_01": -0.05210825298894321,
        "quantile_99": 0.05492552870616813,
        "hill_tail_index": 2.984893371374249
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018869310662331846,
        "excess_kurtosis": 10.173662469411738,
        "return_acf_1": -0.14944176264411235,
        "abs_return_acf_1": 0.4557017765847517,
        "abs_return_acf_5": 0.4090381797647141,
        "abs_return_acf_20": 0.3822136528065961,
        "quantile_01": -0.06400527520391817,
        "quantile_99": 0.0495608015820659,
        "hill_tail_index": 2.5606136954462047
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01754733615738079,
        "excess_kurtosis": 7.5709399925405965,
        "return_acf_1": -0.20130919727722255,
        "abs_return_acf_1": 0.306556416128098,
        "abs_return_acf_5": 0.22579695950064446,
        "abs_return_acf_20": 0.2440225128997405,
        "quantile_01": -0.047637561823277455,
        "quantile_99": 0.06235511225237923,
        "hill_tail_index": 3.1809946765344526
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01720472937084383,
        "excess_kurtosis": 2.8822718260122357,
        "return_acf_1": -0.1425889872778811,
        "abs_return_acf_1": 0.2599581719616594,
        "abs_return_acf_5": 0.25448090204185664,
        "abs_return_acf_20": 0.2117551148372918,
        "quantile_01": -0.04624282988287286,
        "quantile_99": 0.04736327534641877,
        "hill_tail_index": 5.5804584330608415
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01777678948415013,
        "excess_kurtosis": 11.289662218020986,
        "return_acf_1": -0.10684752119096341,
        "abs_return_acf_1": 0.4173060567090548,
        "abs_return_acf_5": 0.4208532428174783,
        "abs_return_acf_20": 0.32024281394479853,
        "quantile_01": -0.056284253135841775,
        "quantile_99": 0.04634966883119195,
        "hill_tail_index": 2.3670554101408356
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.015084437987316707,
        "excess_kurtosis": 2.3649031298056737,
        "return_acf_1": -0.1250623996769882,
        "abs_return_acf_1": 0.2876763150069001,
        "abs_return_acf_5": 0.27309533535385466,
        "abs_return_acf_20": 0.21990564804420606,
        "quantile_01": -0.037969814580992835,
        "quantile_99": 0.042241312752615556,
        "hill_tail_index": 3.9145246531726
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01803833727044753,
        "excess_kurtosis": 11.281512612528513,
        "return_acf_1": -0.06031655823865551,
        "abs_return_acf_1": 0.3927098642162445,
        "abs_return_acf_5": 0.4332609550138328,
        "abs_return_acf_20": 0.3116465033651194,
        "quantile_01": -0.06310170175887167,
        "quantile_99": 0.04558520744353778,
        "hill_tail_index": 2.486010851892591
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01591950410507142,
        "excess_kurtosis": 4.9832951012599676,
        "return_acf_1": -0.11807550400308049,
        "abs_return_acf_1": 0.27190949233044703,
        "abs_return_acf_5": 0.24909815277263453,
        "abs_return_acf_20": 0.1999114483310388,
        "quantile_01": -0.044848775901724765,
        "quantile_99": 0.0417220163994012,
        "hill_tail_index": 2.9507973410842996
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020540095801329476,
        "excess_kurtosis": 16.20992156621762,
        "return_acf_1": -0.16160201484307263,
        "abs_return_acf_1": 0.44709720202717895,
        "abs_return_acf_5": 0.4191977032463505,
        "abs_return_acf_20": 0.34885736858722594,
        "quantile_01": -0.0733361136257221,
        "quantile_99": 0.05606545108186266,
        "hill_tail_index": 2.391832850848484
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01914524900075488,
        "excess_kurtosis": 16.616094530238097,
        "return_acf_1": -0.16989407697373232,
        "abs_return_acf_1": 0.4376692295086754,
        "abs_return_acf_5": 0.41545153809064367,
        "abs_return_acf_20": 0.36391122423753275,
        "quantile_01": -0.06718700269790813,
        "quantile_99": 0.055432187111854506,
        "hill_tail_index": 2.4988590953113925
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018719702673680064,
        "excess_kurtosis": 5.553530241813318,
        "return_acf_1": -0.1696155272532954,
        "abs_return_acf_1": 0.3400079543716263,
        "abs_return_acf_5": 0.2855475243462786,
        "abs_return_acf_20": 0.23382173616004454,
        "quantile_01": -0.05397036091168543,
        "quantile_99": 0.05059127039556729,
        "hill_tail_index": 3.3677464956465673
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017079979725853647,
        "excess_kurtosis": 9.14051213641732,
        "return_acf_1": -0.11540895673664642,
        "abs_return_acf_1": 0.38561297913110293,
        "abs_return_acf_5": 0.32008349855688983,
        "abs_return_acf_20": 0.27414915900553033,
        "quantile_01": -0.0550185050528715,
        "quantile_99": 0.04404665269952301,
        "hill_tail_index": 2.318793447621298
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019345720852780374,
        "excess_kurtosis": 4.833609406375114,
        "return_acf_1": -0.16315934803894636,
        "abs_return_acf_1": 0.3088360646297357,
        "abs_return_acf_5": 0.37024606531280396,
        "abs_return_acf_20": 0.2914445221759456,
        "quantile_01": -0.06386169163853614,
        "quantile_99": 0.058256586440054596,
        "hill_tail_index": 4.030527152316368
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017617504976281565,
        "excess_kurtosis": 7.61096787387455,
        "return_acf_1": -0.1584517999339369,
        "abs_return_acf_1": 0.37082699254313123,
        "abs_return_acf_5": 0.3428670380552394,
        "abs_return_acf_20": 0.27215009354466857,
        "quantile_01": -0.05603012937211967,
        "quantile_99": 0.05148651263799038,
        "hill_tail_index": 3.6459124577898443
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019483997182717146,
        "excess_kurtosis": 15.65848445531077,
        "return_acf_1": -0.1633315530292188,
        "abs_return_acf_1": 0.35082096515958155,
        "abs_return_acf_5": 0.26448924947649727,
        "abs_return_acf_20": 0.2942365621577756,
        "quantile_01": -0.056875011865609226,
        "quantile_99": 0.063789116361008,
        "hill_tail_index": 4.297462124368188
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
