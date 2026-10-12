# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27162
Run ID: `25372d4acbd05ce9ef14cf019c915e394a0808a9738450004e2d436fa5fba4a3`
Result fingerprint: `4e986256d71f33cd6b823c12bd0d052ebe8462d156ede2a86a2bb211645bca45`

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
    "equal_weight_sd": -0.7575476190476159,
    "equal_weight_raw": -11.36321428571424,
    "fixed_start_cap_weight_sd": -0.7796459245865595,
    "fixed_start_cap_weight_raw": -11.694688868798393,
    "end_cap_weight_sd": -0.7859540580512633,
    "end_cap_weight_raw": -11.789310870768949
  },
  "full_period_change": {
    "equal_weight_sd": -1.1277380952380904,
    "equal_weight_raw": -16.916071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0603055555555512,
    "inflation_mean_sd": 0.7007853835978836
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19436652521774686,
    "equal_weight_raw": 2.9154978782662027,
    "fixed_start_cap_weight_sd": 0.17135697519189824,
    "fixed_start_cap_weight_raw": 2.5703546278784732,
    "end_cap_weight_sd": 0.16568900072175471,
    "end_cap_weight_raw": 2.4853350108263212
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8573809523809492,
      "change_raw": -12.860714285714238,
      "decay_adjusted_gain_sd": 0.09500000000000323
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7518253968253937,
      "change_raw": -11.277380952380906,
      "decay_adjusted_gain_sd": 0.19899952850359318
    },
    "small": {
      "count": 18,
      "change_sd": -0.743769841269838,
      "change_raw": -11.15654761904757,
      "decay_adjusted_gain_sd": 0.2086111111111143
    },
    "large_minus_small_sd": -0.11361111111111122,
    "large_minus_small_raw": -1.7041666666666684
  },
  "inflation": {
    "initial_mean_sd": 0.3693333333333333,
    "final_mean_sd": 0.7187499999999998,
    "mean_sd": 0.5698338190396891,
    "mean_absolute_raw_gap": 8.547507285595337,
    "final_absolute_raw_gap": 10.781249999999998,
    "mean_range_fraction": 0.08547507285595338
  },
  "impact": {
    "initial_share": 0.13333333333333333,
    "final_share": 0.16666666666666666,
    "initial_wealth_share": 0.15991142940811928,
    "final_wealth_share": 0.1974333118722899
  },
  "pricing_slope": {
    "mean": -0.0014951051306889354,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.04372066785059597,
    "real_improvement_cost": 0.03446637596948418,
    "washing_cost": 0.009254291881111786,
    "fine_transfer": 0.025316154081538964,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06903682193213494,
    "resource_cost_fraction_initial_cap": 0.0014573555950198659,
    "private_net_outflow_fraction_initial_cap": 0.0023012273977378313,
    "fine_transfer_fraction_initial_cap": 0.0008438718027179655,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00048383215240675785,
    "unapplied_final_day_resource_cost": 0.007522969471506964
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 133.3693203511511,
    "beneficial_raw_gain_per_resource_cost": 2000.5398052672663,
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
    "accrued_cost": 2.968544419809213,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.007646056381263477,
    "accrued_cost_fraction_initial_cap": 0.0989514806603071,
    "mean_contract_rate": 0.04178971374167074,
    "maximum_ledger_error": 8.809142651444724e-20
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
    "maximum_relative_cash_error": 1.7458574637854124e-15,
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
      "minimum": -0.25809543598410767,
      "maximum": -0.09525316591968797,
      "mean": -0.1705271936658875,
      "median": -0.16888162762588566,
      "quantile_05": -0.24223459409490056,
      "quantile_95": -0.12148163446763181
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
      "minimum": 0.2366436151742249,
      "maximum": 0.827574248573689,
      "mean": 0.5830034282996892,
      "median": 0.6497922819371118,
      "quantile_05": 0.31323885683857794,
      "quantile_95": 0.780325704579897
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
        "daily_volatility": 0.02089393300019826,
        "excess_kurtosis": 15.195933036292491,
        "return_acf_1": -0.18465743892139266,
        "abs_return_acf_1": 0.43660908781058755,
        "abs_return_acf_5": 0.4728902491553261,
        "abs_return_acf_20": 0.31441857348958097,
        "quantile_01": -0.07588038159319513,
        "quantile_99": 0.051198020550705645,
        "hill_tail_index": 2.070329075091829
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02155667857860187,
        "excess_kurtosis": 11.998054999885177,
        "return_acf_1": -0.1898409155486049,
        "abs_return_acf_1": 0.4611533207506626,
        "abs_return_acf_5": 0.42465856359511767,
        "abs_return_acf_20": 0.3087675149247202,
        "quantile_01": -0.06150815127800175,
        "quantile_99": 0.06382694840147636,
        "hill_tail_index": 2.449733742373985
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019670062819954308,
        "excess_kurtosis": 16.372028573908995,
        "return_acf_1": -0.16806034784963458,
        "abs_return_acf_1": 0.4214680761054523,
        "abs_return_acf_5": 0.46755159433649285,
        "abs_return_acf_20": 0.3426742916860859,
        "quantile_01": -0.06399897435437082,
        "quantile_99": 0.05111228414429893,
        "hill_tail_index": 2.378598171727262
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018317167080072645,
        "excess_kurtosis": 3.8152557100506694,
        "return_acf_1": -0.1939225168774183,
        "abs_return_acf_1": 0.27466415473628614,
        "abs_return_acf_5": 0.3376215600494507,
        "abs_return_acf_20": 0.2662947299542055,
        "quantile_01": -0.05990364600724667,
        "quantile_99": 0.05075734726099563,
        "hill_tail_index": 3.7688450995950844
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018356343893675634,
        "excess_kurtosis": 4.0554460510583565,
        "return_acf_1": -0.25809543598410767,
        "abs_return_acf_1": 0.3073384177677172,
        "abs_return_acf_5": 0.29810701917758875,
        "abs_return_acf_20": 0.22669289345462523,
        "quantile_01": -0.051356487848132966,
        "quantile_99": 0.04837654458423312,
        "hill_tail_index": 3.308562240988078
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020775601562497602,
        "excess_kurtosis": 13.794920481182057,
        "return_acf_1": -0.17903709059058187,
        "abs_return_acf_1": 0.4144863795810535,
        "abs_return_acf_5": 0.3144267595657459,
        "abs_return_acf_20": 0.2920057916430491,
        "quantile_01": -0.06633629367816578,
        "quantile_99": 0.0621921997387308,
        "hill_tail_index": 2.5199172093432733
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021206676695867743,
        "excess_kurtosis": 6.801634745814134,
        "return_acf_1": -0.16033190793592225,
        "abs_return_acf_1": 0.3913232151837974,
        "abs_return_acf_5": 0.4058656197716224,
        "abs_return_acf_20": 0.3113088338907265,
        "quantile_01": -0.06472491838906834,
        "quantile_99": 0.05994059386866413,
        "hill_tail_index": 3.948437971008851
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018667656657156445,
        "excess_kurtosis": 8.07518859938252,
        "return_acf_1": -0.13728009638172955,
        "abs_return_acf_1": 0.41458242164262565,
        "abs_return_acf_5": 0.4365272640834428,
        "abs_return_acf_20": 0.3138935627823825,
        "quantile_01": -0.0637857236142455,
        "quantile_99": 0.048437189282852254,
        "hill_tail_index": 2.702799258122116
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021242866570462638,
        "excess_kurtosis": 8.124102451271439,
        "return_acf_1": -0.21362123938641844,
        "abs_return_acf_1": 0.4232861627991466,
        "abs_return_acf_5": 0.3168428771811473,
        "abs_return_acf_20": 0.31784968313503525,
        "quantile_01": -0.07628586941981622,
        "quantile_99": 0.05973803032273239,
        "hill_tail_index": 2.930249486103526
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021267855582462813,
        "excess_kurtosis": 10.009840502100865,
        "return_acf_1": -0.14564612372633418,
        "abs_return_acf_1": 0.4763643918222841,
        "abs_return_acf_5": 0.42035223169280794,
        "abs_return_acf_20": 0.335664917630726,
        "quantile_01": -0.07186543655972037,
        "quantile_99": 0.058004625023056554,
        "hill_tail_index": 2.841703028221655
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020167503087247365,
        "excess_kurtosis": 15.259433406599236,
        "return_acf_1": -0.16103718519935215,
        "abs_return_acf_1": 0.4227905122220822,
        "abs_return_acf_5": 0.41925445658942595,
        "abs_return_acf_20": 0.3133763017586387,
        "quantile_01": -0.060657741600983736,
        "quantile_99": 0.046007251463218185,
        "hill_tail_index": 2.2038265370746672
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02277503160470474,
        "excess_kurtosis": 7.933953154998365,
        "return_acf_1": -0.18146810163016322,
        "abs_return_acf_1": 0.41660372641335836,
        "abs_return_acf_5": 0.435516984894446,
        "abs_return_acf_20": 0.2873874236116628,
        "quantile_01": -0.07202301088860334,
        "quantile_99": 0.06555664577369394,
        "hill_tail_index": 2.667642228947825
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02054398864665398,
        "excess_kurtosis": 13.302005300669585,
        "return_acf_1": -0.24281147155459565,
        "abs_return_acf_1": 0.3700245598787448,
        "abs_return_acf_5": 0.3900402544184245,
        "abs_return_acf_20": 0.3008979529382409,
        "quantile_01": -0.05870887733718273,
        "quantile_99": 0.05995645387986878,
        "hill_tail_index": 2.434532468278027
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02054925068463483,
        "excess_kurtosis": 5.11551520919342,
        "return_acf_1": -0.16970290740213673,
        "abs_return_acf_1": 0.33199701642624513,
        "abs_return_acf_5": 0.37172962274314164,
        "abs_return_acf_20": 0.28310882518388414,
        "quantile_01": -0.062083587587693966,
        "quantile_99": 0.05463979917664161,
        "hill_tail_index": 2.641440506140123
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020818818661316126,
        "excess_kurtosis": 9.769934344228538,
        "return_acf_1": -0.24152952164416214,
        "abs_return_acf_1": 0.47499125822800375,
        "abs_return_acf_5": 0.4308178950666761,
        "abs_return_acf_20": 0.3642745941869886,
        "quantile_01": -0.06891957117004048,
        "quantile_99": 0.059375555360438495,
        "hill_tail_index": 2.599346836734617
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020368189200393048,
        "excess_kurtosis": 7.898357510867934,
        "return_acf_1": -0.17450751963560687,
        "abs_return_acf_1": 0.31890806879869105,
        "abs_return_acf_5": 0.3357878573301918,
        "abs_return_acf_20": 0.22486416169865753,
        "quantile_01": -0.06370359832281046,
        "quantile_99": 0.05343180185762556,
        "hill_tail_index": 3.0477465553217753
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017916207341183186,
        "excess_kurtosis": 8.555493030938628,
        "return_acf_1": -0.18039972328503623,
        "abs_return_acf_1": 0.28304585688490413,
        "abs_return_acf_5": 0.3588457047019886,
        "abs_return_acf_20": 0.20244076552641996,
        "quantile_01": -0.054233157955009985,
        "quantile_99": 0.05082144599680632,
        "hill_tail_index": 3.159597485621421
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020746318625462844,
        "excess_kurtosis": 9.753736376792025,
        "return_acf_1": -0.17846981672097523,
        "abs_return_acf_1": 0.3828171753991052,
        "abs_return_acf_5": 0.45082730905295915,
        "abs_return_acf_20": 0.3082323783934968,
        "quantile_01": -0.06362468359022651,
        "quantile_99": 0.05544963038966501,
        "hill_tail_index": 2.4502991819176523
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017140003725715926,
        "excess_kurtosis": 4.72131121164882,
        "return_acf_1": -0.13310921949845797,
        "abs_return_acf_1": 0.34372506929814145,
        "abs_return_acf_5": 0.26592892845494276,
        "abs_return_acf_20": 0.2745281668012193,
        "quantile_01": -0.05142753294687,
        "quantile_99": 0.04376166470086093,
        "hill_tail_index": 3.461965789950709
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019680247235510904,
        "excess_kurtosis": 7.67387903744212,
        "return_acf_1": -0.1660019999249251,
        "abs_return_acf_1": 0.4532426932864862,
        "abs_return_acf_5": 0.4061342447413864,
        "abs_return_acf_20": 0.3148954953817797,
        "quantile_01": -0.05802757869185828,
        "quantile_99": 0.04819474266301065,
        "hill_tail_index": 3.077987761313862
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020752549504245873,
        "excess_kurtosis": 5.105742852032417,
        "return_acf_1": -0.09525316591968797,
        "abs_return_acf_1": 0.3296808688556047,
        "abs_return_acf_5": 0.28948629304891815,
        "abs_return_acf_20": 0.36368667756026046,
        "quantile_01": -0.0634262218178299,
        "quantile_99": 0.06146404228798759,
        "hill_tail_index": 4.340984735321144
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02031839117762961,
        "excess_kurtosis": 16.61039057737669,
        "return_acf_1": -0.1395456676676384,
        "abs_return_acf_1": 0.4052568372333364,
        "abs_return_acf_5": 0.47568421624299784,
        "abs_return_acf_20": 0.26453834819952465,
        "quantile_01": -0.07214587983837462,
        "quantile_99": 0.04496436419772521,
        "hill_tail_index": 1.898772837632027
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021033237383076175,
        "excess_kurtosis": 10.482195922519297,
        "return_acf_1": -0.16138914928495204,
        "abs_return_acf_1": 0.39808160864533226,
        "abs_return_acf_5": 0.44175239720338055,
        "abs_return_acf_20": 0.3499650162025681,
        "quantile_01": -0.06728915295579785,
        "quantile_99": 0.06302096455146568,
        "hill_tail_index": 2.515193643369813
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02057611340424895,
        "excess_kurtosis": 13.61983206685262,
        "return_acf_1": -0.15297137471074396,
        "abs_return_acf_1": 0.4004439718961179,
        "abs_return_acf_5": 0.47935728394290095,
        "abs_return_acf_20": 0.3183146005878013,
        "quantile_01": -0.06096749396005415,
        "quantile_99": 0.0581683309714077,
        "hill_tail_index": 2.515672041463146
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021955891490748974,
        "excess_kurtosis": 11.978287131944713,
        "return_acf_1": -0.12640451968216157,
        "abs_return_acf_1": 0.44009526500704826,
        "abs_return_acf_5": 0.45655087523087506,
        "abs_return_acf_20": 0.37840137574015015,
        "quantile_01": -0.0708546010273146,
        "quantile_99": 0.05978828180036398,
        "hill_tail_index": 2.4273839375392363
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021696794944977907,
        "excess_kurtosis": 14.600454853008621,
        "return_acf_1": -0.11745381929210741,
        "abs_return_acf_1": 0.4196922339483309,
        "abs_return_acf_5": 0.5046723748032147,
        "abs_return_acf_20": 0.37146400499033705,
        "quantile_01": -0.06616962818426275,
        "quantile_99": 0.051348318938811276,
        "hill_tail_index": 1.9325009673305835
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02028929386824699,
        "excess_kurtosis": 10.410516801894332,
        "return_acf_1": -0.1733885054648705,
        "abs_return_acf_1": 0.444349662438363,
        "abs_return_acf_5": 0.4496043046830355,
        "abs_return_acf_20": 0.37348464515774027,
        "quantile_01": -0.0686313577710057,
        "quantile_99": 0.05934170014004793,
        "hill_tail_index": 2.5631778871008524
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022291705521521314,
        "excess_kurtosis": 14.567525822722658,
        "return_acf_1": -0.1492549045397459,
        "abs_return_acf_1": 0.4656715962318329,
        "abs_return_acf_5": 0.5354310787235671,
        "abs_return_acf_20": 0.3581066734337762,
        "quantile_01": -0.07937460001601401,
        "quantile_99": 0.06334160581980333,
        "hill_tail_index": 2.3086042074680866
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020474469251047858,
        "excess_kurtosis": 11.415352191285022,
        "return_acf_1": -0.1729097354044182,
        "abs_return_acf_1": 0.39675260606548646,
        "abs_return_acf_5": 0.48814891057441445,
        "abs_return_acf_20": 0.3490329349319601,
        "quantile_01": -0.06789616839223843,
        "quantile_99": 0.05626046830336455,
        "hill_tail_index": 2.5189504076238856
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020020245511549305,
        "excess_kurtosis": 11.196669140116098,
        "return_acf_1": -0.16771438831274316,
        "abs_return_acf_1": 0.39336558445425296,
        "abs_return_acf_5": 0.39640921081304414,
        "abs_return_acf_20": 0.3448008398078076,
        "quantile_01": -0.06915207934108894,
        "quantile_99": 0.05453071401027329,
        "hill_tail_index": 2.9522752577755456
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
