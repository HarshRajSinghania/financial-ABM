# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27242
Run ID: `096e03c1e76c19af075b8736604cb9a7b4a618daaf957c0b619dc6fae57395d3`
Result fingerprint: `5a312bc5e91f87a72eda3ede69dca634444c5489b992fcd72a3618b7800f000c`

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
    "equal_weight_sd": -0.8072142857142827,
    "equal_weight_raw": -12.108214285714237,
    "fixed_start_cap_weight_sd": -0.7423158958197855,
    "fixed_start_cap_weight_raw": -11.134738437296784,
    "end_cap_weight_sd": -0.7538268406285397,
    "end_cap_weight_raw": -11.307402609428093
  },
  "full_period_change": {
    "equal_weight_sd": -1.255654761904757,
    "equal_weight_raw": -18.834821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.181253637566133,
    "inflation_mean_sd": 0.5832423941798943
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.14199676268725767,
    "equal_weight_raw": 2.1299514403088655,
    "fixed_start_cap_weight_sd": 0.2040556170169719,
    "fixed_start_cap_weight_raw": 3.060834255254578,
    "end_cap_weight_sd": 0.1880746356282519,
    "end_cap_weight_raw": 2.8211195344237776
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6765476190476161,
      "change_raw": -10.148214285714241,
      "decay_adjusted_gain_sd": 0.27583333333333626
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7212698412698378,
      "change_raw": -10.819047619047568,
      "decay_adjusted_gain_sd": 0.22054476451307384
    },
    "small": {
      "count": 18,
      "change_sd": -0.8719642857142824,
      "change_raw": -13.079464285714236,
      "decay_adjusted_gain_sd": 0.08041666666666983
    },
    "large_minus_small_sd": 0.19541666666666635,
    "large_minus_small_raw": 2.931249999999995
  },
  "inflation": {
    "initial_mean_sd": 0.36675,
    "final_mean_sd": 0.6441666666666668,
    "mean_sd": 0.5274111851235082,
    "mean_absolute_raw_gap": 7.911167776852623,
    "final_absolute_raw_gap": 9.662500000000001,
    "mean_range_fraction": 0.07911167776852623
  },
  "impact": {
    "initial_share": 0.29333333333333333,
    "final_share": 0.38,
    "initial_wealth_share": 0.3891065650624238,
    "final_wealth_share": 0.4173193769265398
  },
  "pricing_slope": {
    "mean": -0.0021200763496137306,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.025280597974505763,
    "real_improvement_cost": 0.011549610046154775,
    "washing_cost": 0.013730987928350993,
    "fine_transfer": 0.12500598550457795,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.15028658347908372,
    "resource_cost_fraction_initial_cap": 0.000842686599150192,
    "private_net_outflow_fraction_initial_cap": 0.005009552782636123,
    "fine_transfer_fraction_initial_cap": 0.004166866183485931,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.002494904274281722,
    "unapplied_final_day_resource_cost": 0.0008277985660381905
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 168.5048306576305,
    "beneficial_raw_gain_per_resource_cost": 2527.5724598644574,
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
    "accrued_cost": 2.9441109859606627,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.032079490229814156,
    "accrued_cost_fraction_initial_cap": 0.09813703286535541,
    "mean_contract_rate": 0.0412159886990492,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.8976542621803315e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.1477445933685626,
      "maximum": -0.012680729228739477,
      "mean": -0.07208300019123333,
      "median": -0.0745299073303018,
      "quantile_05": -0.14055237166450174,
      "quantile_95": -0.01500353259952204
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
      "minimum": 0.2327984366476779,
      "maximum": 0.7897366361260539,
      "mean": 0.46837438345615307,
      "median": 0.42605940013556004,
      "quantile_05": 0.26779823018521737,
      "quantile_95": 0.7441327493883199
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
        "daily_volatility": 0.020240194877621773,
        "excess_kurtosis": 5.883304872310642,
        "return_acf_1": -0.10277777501471033,
        "abs_return_acf_1": 0.32996117079016285,
        "abs_return_acf_5": 0.3753135581612387,
        "abs_return_acf_20": 0.34264877579127284,
        "quantile_01": -0.06542644254095219,
        "quantile_99": 0.0585612909528844,
        "hill_tail_index": 4.0854764176008525
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01743236190945533,
        "excess_kurtosis": 19.373157572653316,
        "return_acf_1": -0.0852923960678575,
        "abs_return_acf_1": 0.32646686247712214,
        "abs_return_acf_5": 0.19712841561383568,
        "abs_return_acf_20": 0.19371284810937653,
        "quantile_01": -0.047903062596158064,
        "quantile_99": 0.03800482598308052,
        "hill_tail_index": 1.99384593041398
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017879285358991744,
        "excess_kurtosis": 12.935640868618753,
        "return_acf_1": -0.08853231923843577,
        "abs_return_acf_1": 0.34600706245506907,
        "abs_return_acf_5": 0.34007108812630527,
        "abs_return_acf_20": 0.2646718937524319,
        "quantile_01": -0.05327601604497428,
        "quantile_99": 0.042088730221447636,
        "hill_tail_index": 2.036047869192123
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0208266293471774,
        "excess_kurtosis": 15.249028662959645,
        "return_acf_1": -0.039359056469947175,
        "abs_return_acf_1": 0.4518225758343762,
        "abs_return_acf_5": 0.4573519277742019,
        "abs_return_acf_20": 0.3394409216099645,
        "quantile_01": -0.06804530354996868,
        "quantile_99": 0.06415109604011675,
        "hill_tail_index": 2.071893426023476
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02355812073389051,
        "excess_kurtosis": 10.437628642482316,
        "return_acf_1": -0.047251472744298376,
        "abs_return_acf_1": 0.41567479311062716,
        "abs_return_acf_5": 0.38141696807050396,
        "abs_return_acf_20": 0.3162154905941434,
        "quantile_01": -0.07509343636023307,
        "quantile_99": 0.07809678731039633,
        "hill_tail_index": 2.9845480202289636
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021108713082270004,
        "excess_kurtosis": 11.37788792193886,
        "return_acf_1": -0.021046510872272522,
        "abs_return_acf_1": 0.4473197320840469,
        "abs_return_acf_5": 0.3925169533849352,
        "abs_return_acf_20": 0.3207518977889123,
        "quantile_01": -0.0647073796158867,
        "quantile_99": 0.057818208355383136,
        "hill_tail_index": 3.5317556648650146
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02079086543868303,
        "excess_kurtosis": 8.651315361534838,
        "return_acf_1": -0.012680729228739477,
        "abs_return_acf_1": 0.3148182609178571,
        "abs_return_acf_5": 0.3469536467983125,
        "abs_return_acf_20": 0.31731709173264105,
        "quantile_01": -0.07512413414329593,
        "quantile_99": 0.050100616785905064,
        "hill_tail_index": 2.221617416336935
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.022146243399020576,
        "excess_kurtosis": 11.1169839644621,
        "return_acf_1": -0.014071620220359028,
        "abs_return_acf_1": 0.3508853648553634,
        "abs_return_acf_5": 0.3171838945261636,
        "abs_return_acf_20": 0.2846668091381071,
        "quantile_01": -0.07714915819869322,
        "quantile_99": 0.058098392947804105,
        "hill_tail_index": 2.6419382518814736
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.015157181810252525,
        "excess_kurtosis": 1.5661600334662804,
        "return_acf_1": -0.14114576400935736,
        "abs_return_acf_1": 0.15259875081091218,
        "abs_return_acf_5": 0.20184441811470843,
        "abs_return_acf_20": 0.1823675965308137,
        "quantile_01": -0.037110554105609574,
        "quantile_99": 0.043199036865857916,
        "hill_tail_index": 5.34179289466855
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017522279389397186,
        "excess_kurtosis": 10.958146959985354,
        "return_acf_1": -0.11168516894502495,
        "abs_return_acf_1": 0.23576562766615533,
        "abs_return_acf_5": 0.19505397423427107,
        "abs_return_acf_20": 0.207124318448908,
        "quantile_01": -0.049290264345420526,
        "quantile_99": 0.05003680549247979,
        "hill_tail_index": 2.757643966533377
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021880514864150415,
        "excess_kurtosis": 8.312394158651722,
        "return_acf_1": -0.03487636020318237,
        "abs_return_acf_1": 0.3679706411938657,
        "abs_return_acf_5": 0.3634389621422087,
        "abs_return_acf_20": 0.309399309163134,
        "quantile_01": -0.0784780896675854,
        "quantile_99": 0.06183197497072987,
        "hill_tail_index": 3.1527124230425705
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020681185401187827,
        "excess_kurtosis": 20.80673978893579,
        "return_acf_1": -0.09974478984131477,
        "abs_return_acf_1": 0.5788482604725301,
        "abs_return_acf_5": 0.5214136685403314,
        "abs_return_acf_20": 0.4153955736410625,
        "quantile_01": -0.0638348277172119,
        "quantile_99": 0.057142517212122976,
        "hill_tail_index": 2.274298759266087
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.023879811908334738,
        "excess_kurtosis": 10.408165247665334,
        "return_acf_1": -0.0642117983488197,
        "abs_return_acf_1": 0.39577687529302435,
        "abs_return_acf_5": 0.3611492613358099,
        "abs_return_acf_20": 0.30849821323882737,
        "quantile_01": -0.07814977455106793,
        "quantile_99": 0.08280456632102227,
        "hill_tail_index": 3.611635060293412
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02293474294800546,
        "excess_kurtosis": 8.171500640289421,
        "return_acf_1": -0.0681571272165474,
        "abs_return_acf_1": 0.38868759857699736,
        "abs_return_acf_5": 0.4150372902783494,
        "abs_return_acf_20": 0.2999115805371522,
        "quantile_01": -0.08004798876789894,
        "quantile_99": 0.06001334837498512,
        "hill_tail_index": 3.3734641758651036
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.022548122958812908,
        "excess_kurtosis": 8.320902666270717,
        "return_acf_1": -0.01614253661849904,
        "abs_return_acf_1": 0.35692540040077114,
        "abs_return_acf_5": 0.29383457763464876,
        "abs_return_acf_20": 0.31607376714235536,
        "quantile_01": -0.0771569248985613,
        "quantile_99": 0.0667486374445002,
        "hill_tail_index": 4.075356702957075
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020849627730963924,
        "excess_kurtosis": 20.90170240682647,
        "return_acf_1": -0.13982711435412268,
        "abs_return_acf_1": 0.4509257363023934,
        "abs_return_acf_5": 0.4733925453401343,
        "abs_return_acf_20": 0.34201440801862154,
        "quantile_01": -0.07251896310356262,
        "quantile_99": 0.056875902037614376,
        "hill_tail_index": 1.9179053763903682
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01680436911689674,
        "excess_kurtosis": 5.114389233171524,
        "return_acf_1": -0.08106562699994546,
        "abs_return_acf_1": 0.2732780693572872,
        "abs_return_acf_5": 0.24699330156412452,
        "abs_return_acf_20": 0.2934370966773177,
        "quantile_01": -0.045225814349640736,
        "quantile_99": 0.047108225457664916,
        "hill_tail_index": 3.722383476476865
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022369128579919663,
        "excess_kurtosis": 7.732933154081641,
        "return_acf_1": -0.045007412452613554,
        "abs_return_acf_1": 0.41718265418669354,
        "abs_return_acf_5": 0.4168923948986894,
        "abs_return_acf_20": 0.37876826064155195,
        "quantile_01": -0.07934238206437134,
        "quantile_99": 0.06661526365173409,
        "hill_tail_index": 3.248155563484071
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019895007711216474,
        "excess_kurtosis": 9.032442104924886,
        "return_acf_1": -0.034168410049722174,
        "abs_return_acf_1": 0.45050571394705463,
        "abs_return_acf_5": 0.4365778498679669,
        "abs_return_acf_20": 0.39223396500368346,
        "quantile_01": -0.0708924937620487,
        "quantile_99": 0.05803731102310089,
        "hill_tail_index": 2.7408827288169717
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02050520927193322,
        "excess_kurtosis": 8.669611333047273,
        "return_acf_1": -0.08090268744405621,
        "abs_return_acf_1": 0.3542143473451607,
        "abs_return_acf_5": 0.39364933841628685,
        "abs_return_acf_20": 0.2736683728312333,
        "quantile_01": -0.060901464302929656,
        "quantile_99": 0.06201509163277683,
        "hill_tail_index": 2.9598147694867816
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02349472588842435,
        "excess_kurtosis": 7.8980325784019865,
        "return_acf_1": -0.08383613910590065,
        "abs_return_acf_1": 0.5384292209253386,
        "abs_return_acf_5": 0.5066654571650762,
        "abs_return_acf_20": 0.45705744492522843,
        "quantile_01": -0.08587811759228936,
        "quantile_99": 0.07172763231345805,
        "hill_tail_index": 3.366890939064147
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02238930022041931,
        "excess_kurtosis": 14.82957609971955,
        "return_acf_1": -0.1477445933685626,
        "abs_return_acf_1": 0.5483042079233423,
        "abs_return_acf_5": 0.5502431820836665,
        "abs_return_acf_20": 0.4120664727643662,
        "quantile_01": -0.07010969578558622,
        "quantile_99": 0.06920090433186663,
        "hill_tail_index": 2.6683135100574797
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022260567872770785,
        "excess_kurtosis": 9.923963826407146,
        "return_acf_1": -0.08350356099341687,
        "abs_return_acf_1": 0.3571646298755481,
        "abs_return_acf_5": 0.3910195530985254,
        "abs_return_acf_20": 0.31779465844169896,
        "quantile_01": -0.07588430398807941,
        "quantile_99": 0.06696395198784436,
        "hill_tail_index": 3.230031242453643
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.024034560695191495,
        "excess_kurtosis": 6.573999557944205,
        "return_acf_1": -0.09484807808758595,
        "abs_return_acf_1": 0.4059585043762659,
        "abs_return_acf_5": 0.3838426417167005,
        "abs_return_acf_20": 0.36357323893932514,
        "quantile_01": -0.08080939316663482,
        "quantile_99": 0.07118359760676993,
        "hill_tail_index": 3.81638352332439
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023345755281284165,
        "excess_kurtosis": 8.490788864170797,
        "return_acf_1": -0.05099108465188769,
        "abs_return_acf_1": 0.352343983387605,
        "abs_return_acf_5": 0.4032111685470384,
        "abs_return_acf_20": 0.3761897228931526,
        "quantile_01": -0.08880344869161359,
        "quantile_99": 0.07010109707307455,
        "hill_tail_index": 4.253431871915152
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02066912255679729,
        "excess_kurtosis": 9.659868702845259,
        "return_acf_1": -0.06603992098579313,
        "abs_return_acf_1": 0.3616911565681454,
        "abs_return_acf_5": 0.3579775185235169,
        "abs_return_acf_20": 0.26971855186701066,
        "quantile_01": -0.06677556865670504,
        "quantile_99": 0.06290815295225413,
        "hill_tail_index": 3.251754554121085
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01738521072113557,
        "excess_kurtosis": 4.5181512172239975,
        "return_acf_1": -0.10069974165562137,
        "abs_return_acf_1": 0.24631297358584525,
        "abs_return_acf_5": 0.22432846239996054,
        "abs_return_acf_20": 0.19471180731578533,
        "quantile_01": -0.04965052375622138,
        "quantile_99": 0.04560125060241614,
        "hill_tail_index": 3.3355367823256947
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.0199479487215239,
        "excess_kurtosis": 5.8646361521753825,
        "return_acf_1": -0.12275357230113783,
        "abs_return_acf_1": 0.3475198554398589,
        "abs_return_acf_5": 0.3194338154293373,
        "abs_return_acf_20": 0.23560538763423852,
        "quantile_01": -0.06042221306789794,
        "quantile_99": 0.05757286948212809,
        "hill_tail_index": 3.181078367958367
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022366311334230105,
        "excess_kurtosis": 12.12582968358464,
        "return_acf_1": -0.06269582251784084,
        "abs_return_acf_1": 0.3210416989387148,
        "abs_return_acf_5": 0.36493172992017064,
        "abs_return_acf_20": 0.3801143495338264,
        "quantile_01": -0.07170824886165829,
        "quantile_99": 0.05688261764489258,
        "hill_tail_index": 2.4012943376868643
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.023344306801697093,
        "excess_kurtosis": 9.275929291276722,
        "return_acf_1": -0.021430815729427247,
        "abs_return_acf_1": 0.34675292337986297,
        "abs_return_acf_5": 0.37077480781081745,
        "abs_return_acf_20": 0.3199865897100396,
        "quantile_01": -0.08949729507102915,
        "quantile_99": 0.07490687758812976,
        "hill_tail_index": 3.807965678475235
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
