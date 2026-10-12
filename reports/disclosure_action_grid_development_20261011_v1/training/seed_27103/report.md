# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27103
Run ID: `1c20fcae864783b6c2678810326916c50d2f1a37074f1597b66edddc51f1a191`
Result fingerprint: `b973feff329502902edb2917708e19aaf4bd1caf411d3c22b9bf15f68221a4ff`

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
    "equal_weight_sd": -0.6318243780285137,
    "equal_weight_raw": -9.477365670427705,
    "fixed_start_cap_weight_sd": -0.7127270348165958,
    "fixed_start_cap_weight_raw": -10.690905522248936,
    "end_cap_weight_sd": -0.7154189467084325,
    "end_cap_weight_raw": -10.731284200626488
  },
  "full_period_change": {
    "equal_weight_sd": -0.9717648542189882,
    "equal_weight_raw": -14.576472813284823
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9111678625057678,
    "inflation_mean_sd": 0.6022492774876206
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.31124603174603477,
    "equal_weight_raw": 4.6686904761905215,
    "fixed_start_cap_weight_sd": 0.2190282509093734,
    "fixed_start_cap_weight_raw": 3.285423763640601,
    "end_cap_weight_sd": 0.21254554149720298,
    "end_cap_weight_raw": 3.1881831224580455
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7384818755232608,
      "change_raw": -11.077228132848912,
      "decay_adjusted_gain_sd": 0.12079365079365294
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7190476190476158,
      "change_raw": -10.785714285714237,
      "decay_adjusted_gain_sd": 0.2333333333333365
    },
    "small": {
      "count": 18,
      "change_sd": -0.5704365079365048,
      "change_raw": -8.556547619047572,
      "decay_adjusted_gain_sd": 0.38194444444444753
    },
    "large_minus_small_sd": -0.16804536758675603,
    "large_minus_small_raw": -2.5206805138013406
  },
  "inflation": {
    "initial_mean_sd": 0.24141666666666667,
    "final_mean_sd": 0.6343428621437052,
    "mean_sd": 0.4209205552526083,
    "mean_absolute_raw_gap": 6.313808328789125,
    "final_absolute_raw_gap": 9.515142932155577,
    "mean_range_fraction": 0.06313808328789125
  },
  "impact": {
    "initial_share": 0.22,
    "final_share": 0.30666666666666664,
    "initial_wealth_share": 0.21286263039967177,
    "final_wealth_share": 0.2974377974708263
  },
  "pricing_slope": {
    "mean": -0.0011389387097625152,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.1511772766653347,
    "real_improvement_cost": 0.1305397445071942,
    "washing_cost": 0.0206375321581405,
    "fine_transfer": 0.024718177932618848,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.17589545459795355,
    "resource_cost_fraction_initial_cap": 0.005039242555511156,
    "private_net_outflow_fraction_initial_cap": 0.005863181819931785,
    "fine_transfer_fraction_initial_cap": 0.0008239392644206283,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.020853985285317046,
    "unapplied_final_day_resource_cost": 0.005035543096811763
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 61.76444739807994,
    "beneficial_raw_gain_per_resource_cost": 926.4667109711991,
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
    "accrued_cost": 2.748156846828854,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.22803362936162236,
    "accrued_cost_fraction_initial_cap": 0.09160522822762847,
    "mean_contract_rate": 0.03910221368964886,
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
    "maximum_relative_cash_error": 2.350250498598878e-15,
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
      "minimum": -0.16508478165902396,
      "maximum": 0.0048334330897086995,
      "mean": -0.08840434546532641,
      "median": -0.09205814341333424,
      "quantile_05": -0.15027398833646993,
      "quantile_95": -0.0338512626585377
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
      "minimum": 0.3259804069259623,
      "maximum": 0.7458727553888856,
      "mean": 0.5430742180246815,
      "median": 0.5383529338141464,
      "quantile_05": 0.3682752961988167,
      "quantile_95": 0.7169844151246334
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
        "daily_volatility": 0.0178345324068008,
        "excess_kurtosis": 6.483010025186275,
        "return_acf_1": -0.09215301917782175,
        "abs_return_acf_1": 0.22970989726053576,
        "abs_return_acf_5": 0.2860623010875248,
        "abs_return_acf_20": 0.23261340449796208,
        "quantile_01": -0.05528635555729117,
        "quantile_99": 0.04656394125808966,
        "hill_tail_index": 3.0340829512945198
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017312313950171514,
        "excess_kurtosis": 6.33345442402004,
        "return_acf_1": -0.1153245499736164,
        "abs_return_acf_1": 0.2515993864255769,
        "abs_return_acf_5": 0.30359964899363734,
        "abs_return_acf_20": 0.24263669864094342,
        "quantile_01": -0.05377637986225996,
        "quantile_99": 0.05151578140072727,
        "hill_tail_index": 3.305467722389342
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01899756501922334,
        "excess_kurtosis": 7.008574859589652,
        "return_acf_1": -0.12197062288195297,
        "abs_return_acf_1": 0.35204160042250865,
        "abs_return_acf_5": 0.28530880981965634,
        "abs_return_acf_20": 0.2780482838254889,
        "quantile_01": -0.06373695571786217,
        "quantile_99": 0.049121540590268534,
        "hill_tail_index": 3.5777612250284294
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018087508681538723,
        "excess_kurtosis": 9.357265860469122,
        "return_acf_1": -0.06471538301221892,
        "abs_return_acf_1": 0.27880007359088804,
        "abs_return_acf_5": 0.33340150679324837,
        "abs_return_acf_20": 0.23961392973005857,
        "quantile_01": -0.0507447421051406,
        "quantile_99": 0.04401186690249017,
        "hill_tail_index": 2.5960791343698553
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01853703115528823,
        "excess_kurtosis": 7.8835543603839415,
        "return_acf_1": -0.1001859548321258,
        "abs_return_acf_1": 0.29251281677102015,
        "abs_return_acf_5": 0.332997302246113,
        "abs_return_acf_20": 0.232042326407442,
        "quantile_01": -0.055680335389714015,
        "quantile_99": 0.05460256253845776,
        "hill_tail_index": 3.47665861398061
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01938654633807606,
        "excess_kurtosis": 5.968748555904707,
        "return_acf_1": -0.09384255943275344,
        "abs_return_acf_1": 0.37862769846621697,
        "abs_return_acf_5": 0.3717851071118462,
        "abs_return_acf_20": 0.33355990559005405,
        "quantile_01": -0.061441263882044996,
        "quantile_99": 0.05736643787362278,
        "hill_tail_index": 4.222060163983201
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.017504639040652113,
        "excess_kurtosis": 7.746745961553257,
        "return_acf_1": -0.04859620135416513,
        "abs_return_acf_1": 0.21940710084321033,
        "abs_return_acf_5": 0.25198866616526716,
        "abs_return_acf_20": 0.18854388506901196,
        "quantile_01": -0.04661573031365695,
        "quantile_99": 0.05105876979434867,
        "hill_tail_index": 2.9525859210496574
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02057041065427318,
        "excess_kurtosis": 19.516736429588157,
        "return_acf_1": -0.09461087641115373,
        "abs_return_acf_1": 0.36709861622029144,
        "abs_return_acf_5": 0.28412834610513715,
        "abs_return_acf_20": 0.21598481896880192,
        "quantile_01": -0.057943415341022535,
        "quantile_99": 0.051068107658220466,
        "hill_tail_index": 2.1992494162978775
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017492733187703197,
        "excess_kurtosis": 10.589152059727947,
        "return_acf_1": -0.09196326764884673,
        "abs_return_acf_1": 0.3084602873105618,
        "abs_return_acf_5": 0.13891222313163346,
        "abs_return_acf_20": 0.1989851311789964,
        "quantile_01": -0.048067248049398534,
        "quantile_99": 0.0400635781260193,
        "hill_tail_index": 2.74961539376116
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017413060533183138,
        "excess_kurtosis": 5.6210239304832434,
        "return_acf_1": -0.05346276960973628,
        "abs_return_acf_1": 0.28052417253400835,
        "abs_return_acf_5": 0.31701973112722753,
        "abs_return_acf_20": 0.2729633151309267,
        "quantile_01": -0.055920870536795224,
        "quantile_99": 0.04781920324259376,
        "hill_tail_index": 3.4975532561435334
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017798597999121788,
        "excess_kurtosis": 3.16374788608149,
        "return_acf_1": -0.09147421967324376,
        "abs_return_acf_1": 0.21977132562785215,
        "abs_return_acf_5": 0.20284508936227433,
        "abs_return_acf_20": 0.2309486507069434,
        "quantile_01": -0.05324289350877511,
        "quantile_99": 0.045916789715905355,
        "hill_tail_index": 4.469983242992608
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.0174245343564975,
        "excess_kurtosis": 4.786905983007015,
        "return_acf_1": -0.09619814750512376,
        "abs_return_acf_1": 0.24836416660734562,
        "abs_return_acf_5": 0.19815336433809008,
        "abs_return_acf_20": 0.19329905508117762,
        "quantile_01": -0.05064926220727875,
        "quantile_99": 0.04963611680170053,
        "hill_tail_index": 3.377342259726461
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.0173074299076529,
        "excess_kurtosis": 3.7711436293646647,
        "return_acf_1": -0.09008701204168712,
        "abs_return_acf_1": 0.2745321294647501,
        "abs_return_acf_5": 0.19739566239633094,
        "abs_return_acf_20": 0.19736960298045444,
        "quantile_01": -0.053019749322604934,
        "quantile_99": 0.04623326786018775,
        "hill_tail_index": 3.439069158843922
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018463725745551243,
        "excess_kurtosis": 5.1561698951190245,
        "return_acf_1": -0.14146247838937603,
        "abs_return_acf_1": 0.29100583431766636,
        "abs_return_acf_5": 0.2556782896869935,
        "abs_return_acf_20": 0.23769695022292445,
        "quantile_01": -0.04766207743337288,
        "quantile_99": 0.05039431523107571,
        "hill_tail_index": 3.2569679880335736
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018311970247310957,
        "excess_kurtosis": 8.20949432094078,
        "return_acf_1": -0.11652192653310894,
        "abs_return_acf_1": 0.2662001950247818,
        "abs_return_acf_5": 0.28771246526132943,
        "abs_return_acf_20": 0.23798973199514434,
        "quantile_01": -0.06633840024267879,
        "quantile_99": 0.049132083986461746,
        "hill_tail_index": 2.9910350173361033
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017981111889412534,
        "excess_kurtosis": 6.214968788982585,
        "return_acf_1": -0.0347908222421489,
        "abs_return_acf_1": 0.29435641397507406,
        "abs_return_acf_5": 0.34266798414296346,
        "abs_return_acf_20": 0.30778693549522373,
        "quantile_01": -0.05432987661292773,
        "quantile_99": 0.049993987323067576,
        "hill_tail_index": 3.758209917725309
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018744034040565426,
        "excess_kurtosis": 3.544609117560193,
        "return_acf_1": -0.08795806474089148,
        "abs_return_acf_1": 0.3475862276596211,
        "abs_return_acf_5": 0.29394449966609487,
        "abs_return_acf_20": 0.24497562002387083,
        "quantile_01": -0.05578951937631633,
        "quantile_99": 0.05493202962752975,
        "hill_tail_index": 5.314425633006992
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01868261968501242,
        "excess_kurtosis": 5.49670335788065,
        "return_acf_1": -0.07361169786891968,
        "abs_return_acf_1": 0.3367319439350998,
        "abs_return_acf_5": 0.3155015271748796,
        "abs_return_acf_20": 0.2723894203368346,
        "quantile_01": -0.059275346561434225,
        "quantile_99": 0.056323121683577955,
        "hill_tail_index": 3.8406374991287042
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018633783445220316,
        "excess_kurtosis": 10.519382980758616,
        "return_acf_1": -0.0726901246359117,
        "abs_return_acf_1": 0.3792517258431537,
        "abs_return_acf_5": 0.3173626377938301,
        "abs_return_acf_20": 0.21728764858623503,
        "quantile_01": -0.06048144838959094,
        "quantile_99": 0.05063700823128867,
        "hill_tail_index": 2.195130297778003
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01807715574433683,
        "excess_kurtosis": 9.535282189654557,
        "return_acf_1": -0.03308253209012852,
        "abs_return_acf_1": 0.2541330283201046,
        "abs_return_acf_5": 0.2587279686316786,
        "abs_return_acf_20": 0.2386428270243116,
        "quantile_01": -0.05304392869422939,
        "quantile_99": 0.04300776347705891,
        "hill_tail_index": 2.413241765053265
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016838087946105352,
        "excess_kurtosis": 4.7045319107244294,
        "return_acf_1": 0.0048334330897086995,
        "abs_return_acf_1": 0.19842324568933245,
        "abs_return_acf_5": 0.21459732386564576,
        "abs_return_acf_20": 0.17432042199456713,
        "quantile_01": -0.045833077450944136,
        "quantile_99": 0.04761372551228995,
        "hill_tail_index": 3.3509978306645065
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01967696183131029,
        "excess_kurtosis": 8.295983021033372,
        "return_acf_1": -0.04361428059944911,
        "abs_return_acf_1": 0.35422643203213405,
        "abs_return_acf_5": 0.35485463425967767,
        "abs_return_acf_20": 0.3342583068151162,
        "quantile_01": -0.06680063787311727,
        "quantile_99": 0.05933412578069105,
        "hill_tail_index": 3.472656326236188
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019791634637406203,
        "excess_kurtosis": 8.183215992326593,
        "return_acf_1": -0.11602182652743831,
        "abs_return_acf_1": 0.36201923026243626,
        "abs_return_acf_5": 0.34849394504361597,
        "abs_return_acf_20": 0.2751173944859521,
        "quantile_01": -0.06065132514313777,
        "quantile_99": 0.05602017825140746,
        "hill_tail_index": 3.25358059213719
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01982646242489883,
        "excess_kurtosis": 8.525073787806765,
        "return_acf_1": -0.043888356487254934,
        "abs_return_acf_1": 0.3331689928635649,
        "abs_return_acf_5": 0.3225970173585437,
        "abs_return_acf_20": 0.25026895437417046,
        "quantile_01": -0.05758315430988257,
        "quantile_99": 0.052661370684156696,
        "hill_tail_index": 3.28835026419625
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01728380655917862,
        "excess_kurtosis": 5.7914785763405,
        "return_acf_1": -0.13047123897357835,
        "abs_return_acf_1": 0.33298699449285873,
        "abs_return_acf_5": 0.23227026796612757,
        "abs_return_acf_20": 0.21118828660457709,
        "quantile_01": -0.051389652522535835,
        "quantile_99": 0.04469812410910097,
        "hill_tail_index": 2.9057669288205963
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019195856198197934,
        "excess_kurtosis": 6.218156510025459,
        "return_acf_1": -0.15748340556591042,
        "abs_return_acf_1": 0.38688921304356044,
        "abs_return_acf_5": 0.36076419688804634,
        "abs_return_acf_20": 0.3172197993519352,
        "quantile_01": -0.05486701200859651,
        "quantile_99": 0.056272923049526614,
        "hill_tail_index": 3.06833998444096
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017416667594323462,
        "excess_kurtosis": 3.0485525314475126,
        "return_acf_1": -0.16508478165902396,
        "abs_return_acf_1": 0.21253935457693568,
        "abs_return_acf_5": 0.13710912255636917,
        "abs_return_acf_20": 0.21528135688673614,
        "quantile_01": -0.04813444793260807,
        "quantile_99": 0.04730066801002308,
        "hill_tail_index": 5.373733474061225
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01845969635328926,
        "excess_kurtosis": 23.216765703443205,
        "return_acf_1": -0.051934243396744614,
        "abs_return_acf_1": 0.35017065298056294,
        "abs_return_acf_5": 0.37845656933923616,
        "abs_return_acf_20": 0.22231722792630965,
        "quantile_01": -0.05440960416528879,
        "quantile_99": 0.05128374886589713,
        "hill_tail_index": 2.4779477923238526
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019805655807505363,
        "excess_kurtosis": 9.989202784668642,
        "return_acf_1": -0.10962648267884681,
        "abs_return_acf_1": 0.33094157457917833,
        "abs_return_acf_5": 0.31371856799379083,
        "abs_return_acf_20": 0.2837655872924792,
        "quantile_01": -0.05786700955757084,
        "quantile_99": 0.0656607469506347,
        "hill_tail_index": 2.888876597395845
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01612606811796494,
        "excess_kurtosis": 4.0465142428402565,
        "return_acf_1": -0.1241369511063234,
        "abs_return_acf_1": 0.2908382116239258,
        "abs_return_acf_5": 0.16252287694561088,
        "abs_return_acf_20": 0.2078494806670353,
        "quantile_01": -0.04589694576533972,
        "quantile_99": 0.039554882597087865,
        "hill_tail_index": 3.518519465149449
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
