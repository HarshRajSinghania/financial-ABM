# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27212
Run ID: `541b2bcdc137c79987b213db4e8bf6b0e7a4266ab5b95b9a6c28486c25874ebc`
Result fingerprint: `12c5daed622d90d9cb9f2f501e795de150b72f521f983be0af4b4adb6b387867`

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
    "equal_weight_sd": -0.8211309523809492,
    "equal_weight_raw": -12.316964285714237,
    "fixed_start_cap_weight_sd": -0.8091519814576931,
    "fixed_start_cap_weight_raw": -12.137279721865392,
    "end_cap_weight_sd": -0.8039554309438672,
    "end_cap_weight_raw": -12.059331464158006
  },
  "full_period_change": {
    "equal_weight_sd": -1.2274880952380902,
    "equal_weight_raw": -18.412321428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1436683201058158,
    "inflation_mean_sd": 0.7183769841269841
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.12836393831053147,
    "equal_weight_raw": 1.9254590746579723,
    "fixed_start_cap_weight_sd": 0.1402929545857658,
    "fixed_start_cap_weight_raw": 2.104394318786488,
    "end_cap_weight_sd": 0.14596351072653072,
    "end_cap_weight_raw": 2.189452660897961
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6915476190476161,
      "change_raw": -10.37321428571424,
      "decay_adjusted_gain_sd": 0.26083333333333636
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8232142857142826,
      "change_raw": -12.348214285714239,
      "decay_adjusted_gain_sd": 0.11954646103509756
    },
    "small": {
      "count": 18,
      "change_sd": -0.8416865079365047,
      "change_raw": -12.62529761904757,
      "decay_adjusted_gain_sd": 0.11069444444444763
    },
    "large_minus_small_sd": 0.1501388888888886,
    "large_minus_small_raw": 2.2520833333333288
  },
  "inflation": {
    "initial_mean_sd": 0.3166666666666667,
    "final_mean_sd": 0.7907499999999997,
    "mean_sd": 0.5417824729392173,
    "mean_absolute_raw_gap": 8.12673709408826,
    "final_absolute_raw_gap": 11.86125,
    "mean_range_fraction": 0.0812673709408826
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.4066666666666667,
    "initial_wealth_share": 0.2132247217593279,
    "final_wealth_share": 0.4077688317411151
  },
  "pricing_slope": {
    "mean": -0.0015480582340341074,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.025288597421141243,
    "real_improvement_cost": 0.013664653084865619,
    "washing_cost": 0.011623944336275626,
    "fine_transfer": 0.01162537301223348,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.03691397043337472,
    "resource_cost_fraction_initial_cap": 0.0008429532473713746,
    "private_net_outflow_fraction_initial_cap": 0.0012304656811124904,
    "fine_transfer_fraction_initial_cap": 0.0003875124337411159,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008727050246738229,
    "unapplied_final_day_resource_cost": 0.0008546896185710647
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 152.2788348117947,
    "beneficial_raw_gain_per_resource_cost": 2284.1825221769204,
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
    "accrued_cost": 3.1342574062057738,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.15806693001529692,
    "accrued_cost_fraction_initial_cap": 0.10447524687352577,
    "mean_contract_rate": 0.0432161807399471,
    "maximum_ledger_error": 7.453889935837843e-20
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
    "maximum_relative_cash_error": 1.4611701953633992e-15,
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
      "minimum": -0.2110576297637448,
      "maximum": -0.0007660514792800123,
      "mean": -0.10827858701305462,
      "median": -0.11525630251563752,
      "quantile_05": -0.17381192573345614,
      "quantile_95": -0.044994873052456176
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
      "minimum": 0.2507308052549151,
      "maximum": 0.7908225720234285,
      "mean": 0.44714593439100225,
      "median": 0.405649177284327,
      "quantile_05": 0.30678640481013086,
      "quantile_95": 0.697689738831724
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
        "daily_volatility": 0.01775472594839618,
        "excess_kurtosis": 4.968157818499236,
        "return_acf_1": -0.1176562226135631,
        "abs_return_acf_1": 0.2786400544985252,
        "abs_return_acf_5": 0.34042959180963017,
        "abs_return_acf_20": 0.2817827716836487,
        "quantile_01": -0.046465778862625116,
        "quantile_99": 0.048252027428193754,
        "hill_tail_index": 3.2365349281112255
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020132265201025804,
        "excess_kurtosis": 8.397939067598058,
        "return_acf_1": -0.05786798896857,
        "abs_return_acf_1": 0.4661440133990916,
        "abs_return_acf_5": 0.42173845276795563,
        "abs_return_acf_20": 0.3645534969151431,
        "quantile_01": -0.06655620833836111,
        "quantile_99": 0.05621363098976349,
        "hill_tail_index": 3.9325993640147603
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01960238948929491,
        "excess_kurtosis": 5.430824305702657,
        "return_acf_1": -0.14271522014555366,
        "abs_return_acf_1": 0.38651456412970064,
        "abs_return_acf_5": 0.3062839301120836,
        "abs_return_acf_20": 0.33044843325396944,
        "quantile_01": -0.05881406044573298,
        "quantile_99": 0.06035445251489361,
        "hill_tail_index": 3.565495935977814
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02032465448578973,
        "excess_kurtosis": 11.327760469810512,
        "return_acf_1": -0.0007660514792800123,
        "abs_return_acf_1": 0.44381344987688337,
        "abs_return_acf_5": 0.4015639500107845,
        "abs_return_acf_20": 0.2917761841826725,
        "quantile_01": -0.06788192653714437,
        "quantile_99": 0.06204884053998183,
        "hill_tail_index": 3.337744661959562
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019626186717940815,
        "excess_kurtosis": 8.078367266954,
        "return_acf_1": -0.18044769984003856,
        "abs_return_acf_1": 0.36761546339414336,
        "abs_return_acf_5": 0.40826535272647285,
        "abs_return_acf_20": 0.35379633798966703,
        "quantile_01": -0.05702971199442443,
        "quantile_99": 0.055840084634225455,
        "hill_tail_index": 3.1647815312588867
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018122500086327032,
        "excess_kurtosis": 5.010450397972482,
        "return_acf_1": -0.045122299610522866,
        "abs_return_acf_1": 0.34103288917095087,
        "abs_return_acf_5": 0.37477489602674124,
        "abs_return_acf_20": 0.2545607089252636,
        "quantile_01": -0.05970664862748,
        "quantile_99": 0.050946112347021184,
        "hill_tail_index": 3.8088647725073455
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01901258223210325,
        "excess_kurtosis": 3.482236643521005,
        "return_acf_1": -0.0678607827335213,
        "abs_return_acf_1": 0.3431129750917919,
        "abs_return_acf_5": 0.2751903991006189,
        "abs_return_acf_20": 0.2645825232064627,
        "quantile_01": -0.059578131923045535,
        "quantile_99": 0.050464575717474924,
        "hill_tail_index": 5.120931366732841
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020933435194717416,
        "excess_kurtosis": 10.218723185214706,
        "return_acf_1": -0.0962398427317574,
        "abs_return_acf_1": 0.43582024543430814,
        "abs_return_acf_5": 0.4419758060008671,
        "abs_return_acf_20": 0.35304442701599487,
        "quantile_01": -0.06262401040878218,
        "quantile_99": 0.0517080675335772,
        "hill_tail_index": 2.59509144522606
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019706656477582164,
        "excess_kurtosis": 4.613718062533132,
        "return_acf_1": -0.050306806546032576,
        "abs_return_acf_1": 0.38649195245967,
        "abs_return_acf_5": 0.3713646977085832,
        "abs_return_acf_20": 0.31589590070088525,
        "quantile_01": -0.05834182463026025,
        "quantile_99": 0.056469790007142084,
        "hill_tail_index": 3.881874309215453
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017322853915178994,
        "excess_kurtosis": 4.685755168803886,
        "return_acf_1": -0.07831918149151847,
        "abs_return_acf_1": 0.36395918548909567,
        "abs_return_acf_5": 0.33099977876439524,
        "abs_return_acf_20": 0.32973140702624826,
        "quantile_01": -0.05847145509883155,
        "quantile_99": 0.04334295334540528,
        "hill_tail_index": 2.933132344258604
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019360156379844323,
        "excess_kurtosis": 4.4029975970534725,
        "return_acf_1": -0.11410502978252757,
        "abs_return_acf_1": 0.3967862973560298,
        "abs_return_acf_5": 0.4268451525058402,
        "abs_return_acf_20": 0.3861601779977463,
        "quantile_01": -0.06044294493578835,
        "quantile_99": 0.06266384039579263,
        "hill_tail_index": 3.5725918067333367
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021659338479526346,
        "excess_kurtosis": 11.930263450185196,
        "return_acf_1": -0.11640757524874748,
        "abs_return_acf_1": 0.46186806801871483,
        "abs_return_acf_5": 0.4304199310004382,
        "abs_return_acf_20": 0.36814416037889486,
        "quantile_01": -0.07180149037443066,
        "quantile_99": 0.0717846644501434,
        "hill_tail_index": 3.141718007638604
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020517540573202955,
        "excess_kurtosis": 19.67338970345172,
        "return_acf_1": -0.11843199199351177,
        "abs_return_acf_1": 0.4094807320662911,
        "abs_return_acf_5": 0.4804772157592155,
        "abs_return_acf_20": 0.3411753258923241,
        "quantile_01": -0.07233372542006428,
        "quantile_99": 0.05361217426261896,
        "hill_tail_index": 1.9598165366868558
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017268381350716355,
        "excess_kurtosis": 2.874652550188438,
        "return_acf_1": -0.12059906510413067,
        "abs_return_acf_1": 0.2319920036997347,
        "abs_return_acf_5": 0.28831412650221316,
        "abs_return_acf_20": 0.2166308454327982,
        "quantile_01": -0.045353204650465495,
        "quantile_99": 0.04936111243043026,
        "hill_tail_index": 3.8984736867423018
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016705546472684452,
        "excess_kurtosis": 3.501594513905177,
        "return_acf_1": -0.13338718384567222,
        "abs_return_acf_1": 0.3488367729757676,
        "abs_return_acf_5": 0.36428209912194454,
        "abs_return_acf_20": 0.2795487008987412,
        "quantile_01": -0.044871559883942994,
        "quantile_99": 0.043428768920731345,
        "hill_tail_index": 3.6493739896374544
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.0185957276599244,
        "excess_kurtosis": 3.02098895307335,
        "return_acf_1": -0.11223481154559158,
        "abs_return_acf_1": 0.2707972770876247,
        "abs_return_acf_5": 0.2828139923095121,
        "abs_return_acf_20": 0.23162155755916952,
        "quantile_01": -0.053534083825110865,
        "quantile_99": 0.05557927981365531,
        "hill_tail_index": 4.915625221944441
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01906490123605977,
        "excess_kurtosis": 4.090666540444495,
        "return_acf_1": -0.08757217223272369,
        "abs_return_acf_1": 0.3384949061010408,
        "abs_return_acf_5": 0.31074773972472564,
        "abs_return_acf_20": 0.31112534536281583,
        "quantile_01": -0.05772542715609129,
        "quantile_99": 0.05637064095278399,
        "hill_tail_index": 3.870295950091454
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018786575822827646,
        "excess_kurtosis": 3.0144679561208862,
        "return_acf_1": -0.07507901788458647,
        "abs_return_acf_1": 0.3499682655081596,
        "abs_return_acf_5": 0.30520587468180715,
        "abs_return_acf_20": 0.2405232159030575,
        "quantile_01": -0.05967972912537222,
        "quantile_99": 0.05123065548422939,
        "hill_tail_index": 4.500564915031746
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01954673399868398,
        "excess_kurtosis": 19.45486904778399,
        "return_acf_1": -0.16252581596500992,
        "abs_return_acf_1": 0.5147982685414563,
        "abs_return_acf_5": 0.5235951685762354,
        "abs_return_acf_20": 0.29257956240468225,
        "quantile_01": -0.062489674542048596,
        "quantile_99": 0.046378273727426915,
        "hill_tail_index": 1.9164286386108897
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019118080824227435,
        "excess_kurtosis": 2.5807538896717848,
        "return_acf_1": -0.08793674439785112,
        "abs_return_acf_1": 0.2816404307549251,
        "abs_return_acf_5": 0.27562482327476606,
        "abs_return_acf_20": 0.24250405415346743,
        "quantile_01": -0.05673866679181312,
        "quantile_99": 0.05150608024522958,
        "hill_tail_index": 4.3116825039070505
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018306486629345853,
        "excess_kurtosis": 15.420715083193777,
        "return_acf_1": -0.1657015351587443,
        "abs_return_acf_1": 0.4537183105584226,
        "abs_return_acf_5": 0.3396611037984122,
        "abs_return_acf_20": 0.28276876365573317,
        "quantile_01": -0.05229862707476522,
        "quantile_99": 0.04715164162904205,
        "hill_tail_index": 2.0467907893061117
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01902646584758788,
        "excess_kurtosis": 4.344768837337695,
        "return_acf_1": -0.12977620432097295,
        "abs_return_acf_1": 0.3113115257756957,
        "abs_return_acf_5": 0.2785014514034609,
        "abs_return_acf_20": 0.3255040386235493,
        "quantile_01": -0.06257172080325331,
        "quantile_99": 0.05343256392836027,
        "hill_tail_index": 3.6191429702542366
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01576488166775489,
        "excess_kurtosis": 2.2164538980138024,
        "return_acf_1": -0.14313805337528107,
        "abs_return_acf_1": 0.2528933909685898,
        "abs_return_acf_5": 0.2912086149379853,
        "abs_return_acf_20": 0.21873117360526625,
        "quantile_01": -0.041227006710954334,
        "quantile_99": 0.036500928593169536,
        "hill_tail_index": 3.9409213014664255
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01976627239929262,
        "excess_kurtosis": 9.723000287922881,
        "return_acf_1": -0.04489061495949252,
        "abs_return_acf_1": 0.396519080745137,
        "abs_return_acf_5": 0.34861918663092417,
        "abs_return_acf_20": 0.31243013904250133,
        "quantile_01": -0.06116971924320563,
        "quantile_99": 0.050631698923766955,
        "hill_tail_index": 3.4545466319460045
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019325338819282608,
        "excess_kurtosis": 5.570859877942654,
        "return_acf_1": -0.14789237676410832,
        "abs_return_acf_1": 0.34789428734255884,
        "abs_return_acf_5": 0.41309419879448794,
        "abs_return_acf_20": 0.3198258784993,
        "quantile_01": -0.05931936514263346,
        "quantile_99": 0.06048328521103759,
        "hill_tail_index": 4.024891864808116
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018591053593563212,
        "excess_kurtosis": 5.919183269149649,
        "return_acf_1": -0.1165408668891539,
        "abs_return_acf_1": 0.4113148382418365,
        "abs_return_acf_5": 0.29305215541719987,
        "abs_return_acf_20": 0.30181210035981454,
        "quantile_01": -0.050225555143502965,
        "quantile_99": 0.049880171475843615,
        "hill_tail_index": 2.9389845514944755
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020759229183209764,
        "excess_kurtosis": 7.1869152073437075,
        "return_acf_1": -0.08152266007041321,
        "abs_return_acf_1": 0.3391181195041096,
        "abs_return_acf_5": 0.3322996367287462,
        "abs_return_acf_20": 0.2997796672253357,
        "quantile_01": -0.06569923034431627,
        "quantile_99": 0.05380890960764778,
        "hill_tail_index": 3.5463293726530534
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018393925164921582,
        "excess_kurtosis": 11.221543121262272,
        "return_acf_1": -0.11079472773077707,
        "abs_return_acf_1": 0.40528409063982834,
        "abs_return_acf_5": 0.35696496036204683,
        "abs_return_acf_20": 0.2689224559130866,
        "quantile_01": -0.05873823726258175,
        "quantile_99": 0.048379029726116594,
        "hill_tail_index": 2.9166062356600126
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01935073196364515,
        "excess_kurtosis": 4.582241205585621,
        "return_acf_1": -0.13146143719823908,
        "abs_return_acf_1": 0.34232927421698156,
        "abs_return_acf_5": 0.3368582229470252,
        "abs_return_acf_20": 0.28844444495176486,
        "quantile_01": -0.05881485722225888,
        "quantile_99": 0.050924703970416006,
        "hill_tail_index": 3.6008562787908605
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019415665846463183,
        "excess_kurtosis": 23.251689240824465,
        "return_acf_1": -0.2110576297637448,
        "abs_return_acf_1": 0.4607349008617392,
        "abs_return_acf_5": 0.4293219819437108,
        "abs_return_acf_20": 0.34369252036159853,
        "quantile_01": -0.055800235809273194,
        "quantile_99": 0.04241805017887872,
        "hill_tail_index": 1.5520711135940894
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
