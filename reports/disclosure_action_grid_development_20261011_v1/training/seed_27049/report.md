# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27049
Run ID: `cd4b38cb634295ed68cf003e178983bafc0204217e52249a1aeccc9247df07cb`
Result fingerprint: `0426dfe34c6e605bef2c96fc1f5428be77f7ad781b9e8f76fc7eca9f2e903e5e`

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
    "equal_weight_sd": -0.5821309523809491,
    "equal_weight_raw": -8.731964285714238,
    "fixed_start_cap_weight_sd": -0.5978869232096141,
    "fixed_start_cap_weight_raw": -8.968303848144215,
    "end_cap_weight_sd": -0.5983030180022906,
    "end_cap_weight_raw": -8.974545270034357
  },
  "full_period_change": {
    "equal_weight_sd": -0.9008214285714238,
    "equal_weight_raw": -13.512321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.859777116402112,
    "inflation_mean_sd": 0.6025089285714287
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.37025000000000313,
    "equal_weight_raw": 5.553750000000048,
    "fixed_start_cap_weight_sd": 0.3544940291713381,
    "fixed_start_cap_weight_raw": 5.3174104375700715,
    "end_cap_weight_sd": 0.35407793437866175,
    "end_cap_weight_raw": 5.311169015679926
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6857142857142825,
      "change_raw": -10.285714285714237,
      "decay_adjusted_gain_sd": 0.2666666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5704365079365046,
      "change_raw": -8.556547619047569,
      "decay_adjusted_gain_sd": 0.3819444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.5707142857142825,
      "change_raw": -8.560714285714237,
      "decay_adjusted_gain_sd": 0.38166666666666976
    },
    "large_minus_small_sd": -0.11499999999999999,
    "large_minus_small_raw": -1.7249999999999999
  },
  "inflation": {
    "initial_mean_sd": 0.2873333333333334,
    "final_mean_sd": 0.6088333333333332,
    "mean_sd": 0.4874872328615043,
    "mean_absolute_raw_gap": 7.312308492922564,
    "final_absolute_raw_gap": 9.1325,
    "mean_range_fraction": 0.07312308492922565
  },
  "impact": {
    "initial_share": 0.19333333333333333,
    "final_share": 0.24666666666666667,
    "initial_wealth_share": 0.2076672886706266,
    "final_wealth_share": 0.255506658201837
  },
  "pricing_slope": {
    "mean": -0.001022931651911931,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.05747987706387322,
    "real_improvement_cost": 0.039876734289149146,
    "washing_cost": 0.017603142774724072,
    "fine_transfer": 0.02823944820807619,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0857193252719494,
    "resource_cost_fraction_initial_cap": 0.0019159959021291073,
    "private_net_outflow_fraction_initial_cap": 0.0028573108423983135,
    "fine_transfer_fraction_initial_cap": 0.0009413149402692063,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005598566006697317,
    "unapplied_final_day_resource_cost": 0.002911512128881284
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 193.24154064660115,
    "beneficial_raw_gain_per_resource_cost": 2898.6231096990173,
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
    "accrued_cost": 3.1817693697282383,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.20557889353776132,
    "accrued_cost_fraction_initial_cap": 0.10605897899094127,
    "mean_contract_rate": 0.04457994357590582,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.4214956426250038e-15,
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
      "minimum": -0.19618945277846098,
      "maximum": -0.003930471300460296,
      "mean": -0.09384149351482846,
      "median": -0.10196017688253664,
      "quantile_05": -0.16985048172133527,
      "quantile_95": -0.014922831285682708
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
      "minimum": 0.23846389890783923,
      "maximum": 0.786875868106247,
      "mean": 0.4635296672641442,
      "median": 0.4493400018869011,
      "quantile_05": 0.2998502168673021,
      "quantile_95": 0.6831493795541125
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
        "daily_volatility": 0.018330885941979402,
        "excess_kurtosis": 4.884848312829002,
        "return_acf_1": -0.11550757371560494,
        "abs_return_acf_1": 0.32216516389839445,
        "abs_return_acf_5": 0.21413684696783225,
        "abs_return_acf_20": 0.2476447955701368,
        "quantile_01": -0.05449454498074403,
        "quantile_99": 0.05002542661846361,
        "hill_tail_index": 3.2047595451046367
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020197088137031485,
        "excess_kurtosis": 7.514545354305682,
        "return_acf_1": -0.12561687379152617,
        "abs_return_acf_1": 0.3527568690692535,
        "abs_return_acf_5": 0.36511557355219193,
        "abs_return_acf_20": 0.30324356856430756,
        "quantile_01": -0.062473028009587143,
        "quantile_99": 0.0565892682447498,
        "hill_tail_index": 2.905493714991993
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021037014511750725,
        "excess_kurtosis": 10.241316656216139,
        "return_acf_1": -0.05488367614414962,
        "abs_return_acf_1": 0.3687950031305535,
        "abs_return_acf_5": 0.3323393179845898,
        "abs_return_acf_20": 0.28398226120699327,
        "quantile_01": -0.06936156954997592,
        "quantile_99": 0.05777248704564945,
        "hill_tail_index": 2.603927228293567
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01967793660347466,
        "excess_kurtosis": 10.768610171914537,
        "return_acf_1": -0.11944546798842401,
        "abs_return_acf_1": 0.34347831345823265,
        "abs_return_acf_5": 0.28176586594742936,
        "abs_return_acf_20": 0.2776536374478014,
        "quantile_01": -0.052897559709720404,
        "quantile_99": 0.05474969453741914,
        "hill_tail_index": 2.607494474618854
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017172636887124882,
        "excess_kurtosis": 5.295018922997114,
        "return_acf_1": -0.060256709498365285,
        "abs_return_acf_1": 0.3514148793695629,
        "abs_return_acf_5": 0.33474569229992723,
        "abs_return_acf_20": 0.27942479018899585,
        "quantile_01": -0.05577575769711494,
        "quantile_99": 0.04859439052791784,
        "hill_tail_index": 3.552514272895647
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02016587645896457,
        "excess_kurtosis": 5.919093586223875,
        "return_acf_1": -0.12322180994611374,
        "abs_return_acf_1": 0.369434662970788,
        "abs_return_acf_5": 0.2566902032154346,
        "abs_return_acf_20": 0.21928109982332566,
        "quantile_01": -0.0632492508091489,
        "quantile_99": 0.057680726327545784,
        "hill_tail_index": 3.843725649835562
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021144913186599577,
        "excess_kurtosis": 10.799626660002499,
        "return_acf_1": -0.13697333030179096,
        "abs_return_acf_1": 0.42837924196438554,
        "abs_return_acf_5": 0.36961174931591695,
        "abs_return_acf_20": 0.31631775890873537,
        "quantile_01": -0.07354926489158484,
        "quantile_99": 0.054930331170928784,
        "hill_tail_index": 2.537825715457203
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019562694775160917,
        "excess_kurtosis": 9.41169154604709,
        "return_acf_1": -0.08721145578035874,
        "abs_return_acf_1": 0.2761826464900707,
        "abs_return_acf_5": 0.34318665169617635,
        "abs_return_acf_20": 0.2569240949280245,
        "quantile_01": -0.06013771135504144,
        "quantile_99": 0.05476883945830514,
        "hill_tail_index": 3.3500626634111508
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018898934438197908,
        "excess_kurtosis": 4.063034629200292,
        "return_acf_1": -0.12111974272143675,
        "abs_return_acf_1": 0.3568116932818579,
        "abs_return_acf_5": 0.3539414906464239,
        "abs_return_acf_20": 0.3167133388724867,
        "quantile_01": -0.060049433550533944,
        "quantile_99": 0.05010852095650249,
        "hill_tail_index": 3.5176093127655315
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019474713609177866,
        "excess_kurtosis": 27.960128765343633,
        "return_acf_1": -0.030772837717522115,
        "abs_return_acf_1": 0.2870560377815635,
        "abs_return_acf_5": 0.26159854229935126,
        "abs_return_acf_20": 0.2279372079854981,
        "quantile_01": -0.05217908092590957,
        "quantile_99": 0.04756095408010213,
        "hill_tail_index": 2.9349223829913313
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016666976269150226,
        "excess_kurtosis": 5.38238952255249,
        "return_acf_1": -0.12128609531564896,
        "abs_return_acf_1": 0.388099618516962,
        "abs_return_acf_5": 0.30911770437440883,
        "abs_return_acf_20": 0.3780816624725822,
        "quantile_01": -0.05372744755628827,
        "quantile_99": 0.04472170934731748,
        "hill_tail_index": 3.138776503021417
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022961786570235166,
        "excess_kurtosis": 15.196519745127944,
        "return_acf_1": -0.016449325592524617,
        "abs_return_acf_1": 0.39684908967426513,
        "abs_return_acf_5": 0.3548895865420365,
        "abs_return_acf_20": 0.34667383856990946,
        "quantile_01": -0.07028961765705408,
        "quantile_99": 0.05507049675502708,
        "hill_tail_index": 2.1986020043223875
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017413765444465174,
        "excess_kurtosis": 2.745970537135195,
        "return_acf_1": -0.18051023400835106,
        "abs_return_acf_1": 0.3297799715335925,
        "abs_return_acf_5": 0.3116386738795934,
        "abs_return_acf_20": 0.24906463428184142,
        "quantile_01": -0.047365088312611915,
        "quantile_99": 0.0536170744293392,
        "hill_tail_index": 4.149935178136522
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02040782316752751,
        "excess_kurtosis": 10.400388956500422,
        "return_acf_1": -0.09567540118999926,
        "abs_return_acf_1": 0.28454561352865787,
        "abs_return_acf_5": 0.3557179253142116,
        "abs_return_acf_20": 0.2801719307794384,
        "quantile_01": -0.07011249551141406,
        "quantile_99": 0.0652441162556297,
        "hill_tail_index": 3.5426497049963146
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02147808954647965,
        "excess_kurtosis": 11.702432901282664,
        "return_acf_1": -0.05504851387420629,
        "abs_return_acf_1": 0.4103511172901571,
        "abs_return_acf_5": 0.35861961400288894,
        "abs_return_acf_20": 0.3461370046587911,
        "quantile_01": -0.06842203132919891,
        "quantile_99": 0.06639000151985636,
        "hill_tail_index": 2.565135604366535
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01701450139513346,
        "excess_kurtosis": 4.897718265819913,
        "return_acf_1": -0.04672210285196685,
        "abs_return_acf_1": 0.29092263860504375,
        "abs_return_acf_5": 0.329679456982163,
        "abs_return_acf_20": 0.2479659456470462,
        "quantile_01": -0.050624287879041746,
        "quantile_99": 0.04878365898547666,
        "hill_tail_index": 3.9122652294701927
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022094506579160164,
        "excess_kurtosis": 13.907841887288196,
        "return_acf_1": -0.038048592049165914,
        "abs_return_acf_1": 0.3749402839303204,
        "abs_return_acf_5": 0.4323016228382099,
        "abs_return_acf_20": 0.3855389936720532,
        "quantile_01": -0.07152130260154806,
        "quantile_99": 0.06328284095687532,
        "hill_tail_index": 2.2105830653653302
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019535164526823686,
        "excess_kurtosis": 12.044415819812585,
        "return_acf_1": -0.14769241653507564,
        "abs_return_acf_1": 0.43687891121292766,
        "abs_return_acf_5": 0.36363084837159965,
        "abs_return_acf_20": 0.28690549220950995,
        "quantile_01": -0.07544293326112024,
        "quantile_99": 0.04655194889403065,
        "hill_tail_index": 2.1081837260356067
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02173759961187153,
        "excess_kurtosis": 8.869354645559493,
        "return_acf_1": -0.06960536880492187,
        "abs_return_acf_1": 0.408379305565797,
        "abs_return_acf_5": 0.39946422796235714,
        "abs_return_acf_20": 0.372685510534563,
        "quantile_01": -0.07663870937306351,
        "quantile_99": 0.06636566889617392,
        "hill_tail_index": 3.3585603173711527
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017662269070059137,
        "excess_kurtosis": 8.456752370268164,
        "return_acf_1": -0.013673881398266587,
        "abs_return_acf_1": 0.3919844067517193,
        "abs_return_acf_5": 0.3694442406314139,
        "abs_return_acf_20": 0.29831165046752306,
        "quantile_01": -0.058221126469978506,
        "quantile_99": 0.043872914757428536,
        "hill_tail_index": 2.194700147422368
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02044690493968281,
        "excess_kurtosis": 6.383328470248525,
        "return_acf_1": -0.09083435246346652,
        "abs_return_acf_1": 0.291119072112843,
        "abs_return_acf_5": 0.30818731964623847,
        "abs_return_acf_20": 0.3296598242221343,
        "quantile_01": -0.06929435131938065,
        "quantile_99": 0.05858337094321758,
        "hill_tail_index": 3.3860141597389704
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01763903244830643,
        "excess_kurtosis": 4.867142494640436,
        "return_acf_1": -0.19618945277846098,
        "abs_return_acf_1": 0.2910478921034429,
        "abs_return_acf_5": 0.22178060692215096,
        "abs_return_acf_20": 0.19169468863592803,
        "quantile_01": -0.048440622801050215,
        "quantile_99": 0.052889242321553294,
        "hill_tail_index": 3.7438390786586306
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01612863693457599,
        "excess_kurtosis": 3.4266873210748843,
        "return_acf_1": -0.04400289238175294,
        "abs_return_acf_1": 0.3155679215975096,
        "abs_return_acf_5": 0.282948606726651,
        "abs_return_acf_20": 0.2592902559462344,
        "quantile_01": -0.04706824557721562,
        "quantile_99": 0.041899526947228115,
        "hill_tail_index": 4.001564725358799
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016910225864315485,
        "excess_kurtosis": 3.9341914756773457,
        "return_acf_1": -0.13891919927526164,
        "abs_return_acf_1": 0.36236505421878523,
        "abs_return_acf_5": 0.2443871475247546,
        "abs_return_acf_20": 0.3243630328116837,
        "quantile_01": -0.05189420525268279,
        "quantile_99": 0.045822762251385964,
        "hill_tail_index": 4.09274131972369
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015698074075398822,
        "excess_kurtosis": 4.520968206849278,
        "return_acf_1": -0.10824495257507404,
        "abs_return_acf_1": 0.34612625897012694,
        "abs_return_acf_5": 0.29241676074151374,
        "abs_return_acf_20": 0.27815075210637696,
        "quantile_01": -0.03905422363997452,
        "quantile_99": 0.04635839435881037,
        "hill_tail_index": 2.9476251978250394
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019799543653676328,
        "excess_kurtosis": 4.905116934835253,
        "return_acf_1": -0.1266805476320031,
        "abs_return_acf_1": 0.3520492152921001,
        "abs_return_acf_5": 0.32817704974974865,
        "abs_return_acf_20": 0.22365288961534732,
        "quantile_01": -0.07059730508623965,
        "quantile_99": 0.05565707701527747,
        "hill_tail_index": 3.4919729677071727
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.016551439867060543,
        "excess_kurtosis": 3.0775146043047785,
        "return_acf_1": -0.07718275970039125,
        "abs_return_acf_1": 0.2857029028677636,
        "abs_return_acf_5": 0.2470577586645851,
        "abs_return_acf_20": 0.2013119900401762,
        "quantile_01": -0.045009283116641145,
        "quantile_99": 0.04582078069290475,
        "hill_tail_index": 3.6795916732904534
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019792826307779572,
        "excess_kurtosis": 9.823091576028695,
        "return_acf_1": -0.11271687251980336,
        "abs_return_acf_1": 0.3130092897654051,
        "abs_return_acf_5": 0.3070092065058538,
        "abs_return_acf_20": 0.27118290578676796,
        "quantile_01": -0.0620454698941723,
        "quantile_99": 0.052001581031835394,
        "hill_tail_index": 2.4125871284916522
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017237058504559324,
        "excess_kurtosis": 10.972689582896813,
        "return_acf_1": -0.003930471300460296,
        "abs_return_acf_1": 0.4596956761403138,
        "abs_return_acf_5": 0.4353602648567851,
        "abs_return_acf_20": 0.2847593584986975,
        "quantile_01": -0.05341153332510138,
        "quantile_99": 0.0494676331881997,
        "hill_tail_index": 2.878072552182875
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01748785565722583,
        "excess_kurtosis": 5.133728381133961,
        "return_acf_1": -0.15682189559276039,
        "abs_return_acf_1": 0.33176558051760036,
        "abs_return_acf_5": 0.36067395126608714,
        "abs_return_acf_20": 0.27512333546352213,
        "quantile_01": -0.05365036229193831,
        "quantile_99": 0.043775888028942916,
        "hill_tail_index": 3.9574324054051035
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
Unseen state share: 0.0011111111111111111
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
