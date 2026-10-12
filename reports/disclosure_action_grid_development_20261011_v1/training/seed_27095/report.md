# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27095
Run ID: `fa691801d016160b5e551012e3e9c0bd300f741393edb15f6471a19426894659`
Result fingerprint: `0d4b8f9fe0e3a415a4d16482d1f2aa10203aba66288fb48f1a3cea245eac0a7c`

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
    "equal_weight_sd": -0.6132142857142827,
    "equal_weight_raw": -9.19821428571424,
    "fixed_start_cap_weight_sd": -0.5095895759277626,
    "fixed_start_cap_weight_raw": -7.6438436389164375,
    "end_cap_weight_sd": -0.5319554007354054,
    "end_cap_weight_raw": -7.979331011031079
  },
  "full_period_change": {
    "equal_weight_sd": -0.9884880952380907,
    "equal_weight_raw": -14.82732142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9251025132275088,
    "inflation_mean_sd": 0.5484242724867724
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3391666666666697,
    "equal_weight_raw": 5.0875000000000465,
    "fixed_start_cap_weight_sd": 0.44279137645319,
    "fixed_start_cap_weight_raw": 6.641870646797851,
    "end_cap_weight_sd": 0.42042555164554696,
    "end_cap_weight_raw": 6.306383274683204
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.461547619047616,
      "change_raw": -6.92321428571424,
      "decay_adjusted_gain_sd": 0.49083333333333634
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5218253968253936,
      "change_raw": -7.827380952380905,
      "decay_adjusted_gain_sd": 0.4305555555555586
    },
    "small": {
      "count": 18,
      "change_sd": -0.6841865079365048,
      "change_raw": -10.262797619047571,
      "decay_adjusted_gain_sd": 0.2681944444444475
    },
    "large_minus_small_sd": 0.22263888888888883,
    "large_minus_small_raw": 3.3395833333333327
  },
  "inflation": {
    "initial_mean_sd": 0.24975000000000003,
    "final_mean_sd": 0.6028333333333333,
    "mean_sd": 0.43356466833194557,
    "mean_absolute_raw_gap": 6.503470024979185,
    "final_absolute_raw_gap": 9.0425,
    "mean_range_fraction": 0.06503470024979185
  },
  "impact": {
    "initial_share": 0.30666666666666664,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.33148393394830583,
    "final_wealth_share": 0.3845455131843341
  },
  "pricing_slope": {
    "mean": -0.0022735433537139057,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.10089316766062068,
    "real_improvement_cost": 0.08947941171912632,
    "washing_cost": 0.011413755941494349,
    "fine_transfer": 0.00477868375436321,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.10567185141498389,
    "resource_cost_fraction_initial_cap": 0.0033631055886873557,
    "private_net_outflow_fraction_initial_cap": 0.0035223950471661297,
    "fine_transfer_fraction_initial_cap": 0.00015928945847877365,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004338435955604084,
    "unapplied_final_day_resource_cost": 0.00012589443492349984
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 100.8492471385797,
    "beneficial_raw_gain_per_resource_cost": 1512.7387070786954,
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
    "accrued_cost": 3.1224366979976494,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.14624622180717262,
    "accrued_cost_fraction_initial_cap": 0.10408122326658832,
    "mean_contract_rate": 0.04359737763700256,
    "maximum_ledger_error": 7.284483346386983e-20
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
    "maximum_relative_cash_error": 2.713219929207423e-15,
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
      "minimum": -0.14931994276420002,
      "maximum": -0.00185135110110131,
      "mean": -0.09964344173486823,
      "median": -0.10185886640726097,
      "quantile_05": -0.14415619627669538,
      "quantile_95": -0.06065327804866391
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
      "minimum": 0.2804980686563267,
      "maximum": 0.773159263673209,
      "mean": 0.5392856642745439,
      "median": 0.5461849871432,
      "quantile_05": 0.35196421902468417,
      "quantile_95": 0.7125003034657426
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
        "daily_volatility": 0.019102303199793114,
        "excess_kurtosis": 4.382688212711574,
        "return_acf_1": -0.07893127409445322,
        "abs_return_acf_1": 0.37648162680525865,
        "abs_return_acf_5": 0.3528508837951156,
        "abs_return_acf_20": 0.3216226815361228,
        "quantile_01": -0.05863025170072801,
        "quantile_99": 0.05034879535844501,
        "hill_tail_index": 3.561556585049497
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01876013884819661,
        "excess_kurtosis": 3.850649760563421,
        "return_acf_1": -0.14931994276420002,
        "abs_return_acf_1": 0.3760250576820337,
        "abs_return_acf_5": 0.35127234091133896,
        "abs_return_acf_20": 0.3627021958321677,
        "quantile_01": -0.05639366180913404,
        "quantile_99": 0.0535679141941194,
        "hill_tail_index": 4.976400003703664
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019618545950521683,
        "excess_kurtosis": 9.462060641981237,
        "return_acf_1": -0.00185135110110131,
        "abs_return_acf_1": 0.35716091214462464,
        "abs_return_acf_5": 0.3217667501934682,
        "abs_return_acf_20": 0.3258047049319754,
        "quantile_01": -0.06257443731130709,
        "quantile_99": 0.06120718490954416,
        "hill_tail_index": 2.991607820545276
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018543732708857764,
        "excess_kurtosis": 7.300219450207482,
        "return_acf_1": -0.08266427241377555,
        "abs_return_acf_1": 0.349688483240303,
        "abs_return_acf_5": 0.31749125059661726,
        "abs_return_acf_20": 0.27510960257848316,
        "quantile_01": -0.05519506619787062,
        "quantile_99": 0.0496099288387374,
        "hill_tail_index": 2.862721771457758
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017499953566877054,
        "excess_kurtosis": 3.64155031096662,
        "return_acf_1": -0.09651310478840304,
        "abs_return_acf_1": 0.31248934642292364,
        "abs_return_acf_5": 0.2948478600941753,
        "abs_return_acf_20": 0.31968216434259933,
        "quantile_01": -0.05431544022181576,
        "quantile_99": 0.04606596239557253,
        "hill_tail_index": 3.592136924610024
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01814880801878142,
        "excess_kurtosis": 5.121193855956186,
        "return_acf_1": -0.11537067909164114,
        "abs_return_acf_1": 0.3580156359808831,
        "abs_return_acf_5": 0.2874495169391255,
        "abs_return_acf_20": 0.26551410047092283,
        "quantile_01": -0.05750120302956084,
        "quantile_99": 0.04878758454773038,
        "hill_tail_index": 3.2243521924441545
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017498935797460327,
        "excess_kurtosis": 11.420978195139577,
        "return_acf_1": -0.13000587538523525,
        "abs_return_acf_1": 0.31967812746162755,
        "abs_return_acf_5": 0.3545288432120311,
        "abs_return_acf_20": 0.2624638967464504,
        "quantile_01": -0.05157729832869331,
        "quantile_99": 0.038997056552989226,
        "hill_tail_index": 2.1617888635576645
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01815632211644824,
        "excess_kurtosis": 4.782239901407001,
        "return_acf_1": -0.1203820079266868,
        "abs_return_acf_1": 0.28638991404137887,
        "abs_return_acf_5": 0.27206770510385936,
        "abs_return_acf_20": 0.20380906414604752,
        "quantile_01": -0.05425092264195585,
        "quantile_99": 0.05083946102286385,
        "hill_tail_index": 3.3723335624822868
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018664314166194206,
        "excess_kurtosis": 8.502696735271062,
        "return_acf_1": -0.07327113794129139,
        "abs_return_acf_1": 0.30294058877443736,
        "abs_return_acf_5": 0.3669920787165075,
        "abs_return_acf_20": 0.2192909345223198,
        "quantile_01": -0.05962925882981953,
        "quantile_99": 0.05419913821440005,
        "hill_tail_index": 3.0624096656914244
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019541241523362476,
        "excess_kurtosis": 8.858374333673071,
        "return_acf_1": -0.057312013177813245,
        "abs_return_acf_1": 0.32559252376405834,
        "abs_return_acf_5": 0.37515621766492835,
        "abs_return_acf_20": 0.2839006845611293,
        "quantile_01": -0.05607211327234333,
        "quantile_99": 0.05270896602153152,
        "hill_tail_index": 2.6798123390487945
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017057508328006885,
        "excess_kurtosis": 4.429601067727218,
        "return_acf_1": -0.1116918828121056,
        "abs_return_acf_1": 0.28289199526209846,
        "abs_return_acf_5": 0.3090723818868546,
        "abs_return_acf_20": 0.24667634822233167,
        "quantile_01": -0.051157536438633376,
        "quantile_99": 0.04790531383042485,
        "hill_tail_index": 3.692629901159967
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021411870382593953,
        "excess_kurtosis": 10.503942287061824,
        "return_acf_1": -0.0907016183077005,
        "abs_return_acf_1": 0.36725838759065965,
        "abs_return_acf_5": 0.42569481692359373,
        "abs_return_acf_20": 0.3303977822889375,
        "quantile_01": -0.06821860063949169,
        "quantile_99": 0.07132121903488041,
        "hill_tail_index": 2.8782421447875075
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02136638895228819,
        "excess_kurtosis": 13.980521326182188,
        "return_acf_1": -0.0720057841397718,
        "abs_return_acf_1": 0.38661400922136796,
        "abs_return_acf_5": 0.37085681482324534,
        "abs_return_acf_20": 0.3270309137836972,
        "quantile_01": -0.06303115232353422,
        "quantile_99": 0.05769268865043751,
        "hill_tail_index": 2.6073816457274748
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021412118291684774,
        "excess_kurtosis": 16.50977716538644,
        "return_acf_1": -0.13820530071921958,
        "abs_return_acf_1": 0.4431958811406177,
        "abs_return_acf_5": 0.3232126865667976,
        "abs_return_acf_20": 0.3203422493297229,
        "quantile_01": -0.062245871296754705,
        "quantile_99": 0.057302711541966145,
        "hill_tail_index": 2.6736760767836794
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01881466281018372,
        "excess_kurtosis": 3.5063779841229783,
        "return_acf_1": -0.14065546242950702,
        "abs_return_acf_1": 0.3253439754350411,
        "abs_return_acf_5": 0.3892784934889644,
        "abs_return_acf_20": 0.3441601428948202,
        "quantile_01": -0.05701945872954575,
        "quantile_99": 0.052150848038531955,
        "hill_tail_index": 4.547353066900177
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018288591209060755,
        "excess_kurtosis": 3.8033855861723165,
        "return_acf_1": -0.11293891514235296,
        "abs_return_acf_1": 0.2952147182695868,
        "abs_return_acf_5": 0.2993084801482296,
        "abs_return_acf_20": 0.2918532812908693,
        "quantile_01": -0.05691131034062508,
        "quantile_99": 0.05593890791619527,
        "hill_tail_index": 4.149534156700659
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018856724387663937,
        "excess_kurtosis": 7.750833447597056,
        "return_acf_1": -0.12771178923199275,
        "abs_return_acf_1": 0.42377862867604915,
        "abs_return_acf_5": 0.3315940332806192,
        "abs_return_acf_20": 0.2876632487793324,
        "quantile_01": -0.054463499987256046,
        "quantile_99": 0.048839342816177765,
        "hill_tail_index": 3.0524256572969835
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019086111625444574,
        "excess_kurtosis": 4.5156542047947354,
        "return_acf_1": -0.08839514467341461,
        "abs_return_acf_1": 0.3073164740210302,
        "abs_return_acf_5": 0.33336706185665776,
        "abs_return_acf_20": 0.3019646471928443,
        "quantile_01": -0.056966390628711075,
        "quantile_99": 0.0560816268260207,
        "hill_tail_index": 3.700252663945878
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.015576558836731074,
        "excess_kurtosis": 3.6472133767352037,
        "return_acf_1": -0.06550432303755523,
        "abs_return_acf_1": 0.1657030629328109,
        "abs_return_acf_5": 0.2254731443318159,
        "abs_return_acf_20": 0.2135182433099557,
        "quantile_01": -0.04487978466608877,
        "quantile_99": 0.041807738017758424,
        "hill_tail_index": 3.28914857791494
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018442103764262717,
        "excess_kurtosis": 5.541566547094485,
        "return_acf_1": -0.14702043306075857,
        "abs_return_acf_1": 0.29748683597452097,
        "abs_return_acf_5": 0.3087884967757427,
        "abs_return_acf_20": 0.2950310786861183,
        "quantile_01": -0.058714477444286386,
        "quantile_99": 0.04741545578453281,
        "hill_tail_index": 3.23172377040691
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019771083248387875,
        "excess_kurtosis": 22.256287706610042,
        "return_acf_1": -0.0723775061740476,
        "abs_return_acf_1": 0.35396945949581515,
        "abs_return_acf_5": 0.29357341442586266,
        "abs_return_acf_20": 0.2956438768903787,
        "quantile_01": -0.05430699731730145,
        "quantile_99": 0.041401064029177384,
        "hill_tail_index": 1.894626183007813
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019931683049567127,
        "excess_kurtosis": 14.013126187351265,
        "return_acf_1": -0.07577696108769769,
        "abs_return_acf_1": 0.4270178829661896,
        "abs_return_acf_5": 0.39836897364395507,
        "abs_return_acf_20": 0.318240117888702,
        "quantile_01": -0.06755342172611907,
        "quantile_99": 0.05010440631530239,
        "hill_tail_index": 2.4634436164324525
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01790981428255444,
        "excess_kurtosis": 3.6728433218534455,
        "return_acf_1": -0.12143108834488868,
        "abs_return_acf_1": 0.3032013305113807,
        "abs_return_acf_5": 0.27522508146058366,
        "abs_return_acf_20": 0.2816896193051793,
        "quantile_01": -0.0539644600168591,
        "quantile_99": 0.050913119891383536,
        "hill_tail_index": 4.012945992889691
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022194307148814176,
        "excess_kurtosis": 15.259576353811735,
        "return_acf_1": -0.07173089155468117,
        "abs_return_acf_1": 0.3851808867103497,
        "abs_return_acf_5": 0.3825539469520645,
        "abs_return_acf_20": 0.32178080537493314,
        "quantile_01": -0.07182285368403676,
        "quantile_99": 0.057390454085409895,
        "hill_tail_index": 2.219710459727959
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01923523900953314,
        "excess_kurtosis": 12.287001348754766,
        "return_acf_1": -0.10720462802611888,
        "abs_return_acf_1": 0.4008859397238605,
        "abs_return_acf_5": 0.3326164258166128,
        "abs_return_acf_20": 0.3409839952215652,
        "quantile_01": -0.05741329763899039,
        "quantile_99": 0.05021480002326382,
        "hill_tail_index": 2.8479757117962596
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01808242003442591,
        "excess_kurtosis": 5.461135488108788,
        "return_acf_1": -0.06473704622414801,
        "abs_return_acf_1": 0.2503330555735772,
        "abs_return_acf_5": 0.29658036657318926,
        "abs_return_acf_20": 0.25574082153986843,
        "quantile_01": -0.054707661992483544,
        "quantile_99": 0.04809961648064626,
        "hill_tail_index": 3.016616124998162
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019791137937105574,
        "excess_kurtosis": 15.265785774516825,
        "return_acf_1": -0.13864116274536506,
        "abs_return_acf_1": 0.3603621510457765,
        "abs_return_acf_5": 0.3762455138335998,
        "abs_return_acf_20": 0.2938261925025747,
        "quantile_01": -0.0554391116334133,
        "quantile_99": 0.05817492353509596,
        "hill_tail_index": 2.652512310913508
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019423549440340956,
        "excess_kurtosis": 7.536598541842606,
        "return_acf_1": -0.12302361488670535,
        "abs_return_acf_1": 0.3860282837735106,
        "abs_return_acf_5": 0.3692440176773981,
        "abs_return_acf_20": 0.34256525032347773,
        "quantile_01": -0.05926949045716379,
        "quantile_99": 0.06281006910004805,
        "hill_tail_index": 3.5034954179473754
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019720880395872838,
        "excess_kurtosis": 17.864072554650843,
        "return_acf_1": -0.09474094200247177,
        "abs_return_acf_1": 0.4182280536800756,
        "abs_return_acf_5": 0.38840190063178676,
        "abs_return_acf_20": 0.2912585441263295,
        "quantile_01": -0.05549469148002141,
        "quantile_99": 0.05301635965095175,
        "hill_tail_index": 2.7500428253291185
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01957690922356907,
        "excess_kurtosis": 11.19403077878738,
        "return_acf_1": -0.11918709876094331,
        "abs_return_acf_1": 0.3351822159308693,
        "abs_return_acf_5": 0.4045700198512253,
        "abs_return_acf_20": 0.29797789445299844,
        "quantile_01": -0.058613266334063746,
        "quantile_99": 0.059652830510310735,
        "hill_tail_index": 2.490244779192761
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
