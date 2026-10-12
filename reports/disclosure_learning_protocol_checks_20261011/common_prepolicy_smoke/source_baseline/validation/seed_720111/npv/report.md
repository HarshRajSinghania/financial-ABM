# Disclosure-market run

Purpose: development
Domain: esg
Seed: 720111
Run ID: `cf13cdde1da648429d81b42887de4ee74cb071e61d3cf4bfaab86dbee5369071`
Result fingerprint: `06bcfa461ea561d7a7be7a5459905d46febf418be9f6fe67db5ae02b33212ee6`

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
    "equal_weight_sd": -0.702403818798815,
    "equal_weight_raw": -10.536057281982226,
    "fixed_start_cap_weight_sd": -0.656093745254896,
    "fixed_start_cap_weight_raw": -9.84140617882344,
    "end_cap_weight_sd": -0.6363909218853155,
    "end_cap_weight_raw": -9.545863828279732
  },
  "full_period_change": {
    "equal_weight_sd": -1.1111961866974505,
    "equal_weight_raw": -16.667942800461756
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0494087794956042,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2417047332944968,
    "equal_weight_raw": 3.625570999417453,
    "fixed_start_cap_weight_sd": 0.29395150512572094,
    "fixed_start_cap_weight_raw": 4.409272576885814,
    "end_cap_weight_sd": 0.3147018577887711,
    "end_cap_weight_raw": 4.72052786683157
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5796855676686263,
      "change_raw": -8.695283515029395,
      "decay_adjusted_gain_sd": 0.37269538471232594
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7247998209582027,
      "change_raw": -10.87199731437304,
      "decay_adjusted_gain_sd": 0.22758113142274963
    },
    "small": {
      "count": 18,
      "change_sd": -0.7116588595741526,
      "change_raw": -10.67488289361229,
      "decay_adjusted_gain_sd": 0.2269347589940656
    },
    "large_minus_small_sd": 0.1319732919055263,
    "large_minus_small_raw": 1.9795993785828947
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.34,
    "initial_wealth_share": 0.4073174845159611,
    "final_wealth_share": 0.4359757858793606
  },
  "pricing_slope": {
    "mean": -0.002084607840188738,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.0011188856465251672,
    "real_improvement_cost": 0.0011188856465251672,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0011188856465251672,
    "resource_cost_fraction_initial_cap": 3.729618821750558e-05,
    "private_net_outflow_fraction_initial_cap": 3.729618821750558e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 4.17139700635646e-05,
    "unapplied_final_day_resource_cost": 5.79276232546618e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 6480.681936848677,
    "beneficial_raw_gain_per_resource_cost": 97210.22905273014,
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
    "fixed_exposure": 14.999999999999996,
    "accrued_cost": 3.049934759340744,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.07374428315026803,
    "accrued_cost_fraction_initial_cap": 0.10166449197802482,
    "mean_contract_rate": 0.04266461680780974,
    "maximum_ledger_error": 1.8295911660692887e-19
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
    "maximum_relative_cash_error": 1.8770392489950847e-15,
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
      "minimum": -0.2611837304495117,
      "maximum": -0.08562535837343302,
      "mean": -0.1618023247112028,
      "median": -0.1615453534862672,
      "quantile_05": -0.21922340788097522,
      "quantile_95": -0.09700931799618785
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
      "minimum": 0.4365563997851915,
      "maximum": 0.8011495170917459,
      "mean": 0.640644276138159,
      "median": 0.6435198999529864,
      "quantile_05": 0.5190585180990465,
      "quantile_95": 0.744040896067428
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
        "daily_volatility": 0.02170961688928184,
        "excess_kurtosis": 15.096681756015329,
        "return_acf_1": -0.2611837304495117,
        "abs_return_acf_1": 0.4038209477789332,
        "abs_return_acf_5": 0.4422422793685012,
        "abs_return_acf_20": 0.25472561786221914,
        "quantile_01": -0.06954060122737198,
        "quantile_99": 0.05439301845959822,
        "hill_tail_index": 2.394690632164121
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01879236334314871,
        "excess_kurtosis": 11.205777068750272,
        "return_acf_1": -0.16097063499195224,
        "abs_return_acf_1": 0.3132399256338807,
        "abs_return_acf_5": 0.379228029762282,
        "abs_return_acf_20": 0.24092246451643087,
        "quantile_01": -0.06308803344013668,
        "quantile_99": 0.04383318372702988,
        "hill_tail_index": 2.360241868627512
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021383095639167633,
        "excess_kurtosis": 3.0096416569655267,
        "return_acf_1": -0.15395325075170505,
        "abs_return_acf_1": 0.32831931116385515,
        "abs_return_acf_5": 0.302772125417163,
        "abs_return_acf_20": 0.31671832461538996,
        "quantile_01": -0.06538733057183999,
        "quantile_99": 0.06524255546952375,
        "hill_tail_index": 4.271970357181357
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019652809940221054,
        "excess_kurtosis": 4.257451815150665,
        "return_acf_1": -0.18308582188554717,
        "abs_return_acf_1": 0.2541706799435443,
        "abs_return_acf_5": 0.2805484409318464,
        "abs_return_acf_20": 0.15003886609818848,
        "quantile_01": -0.06617700099844721,
        "quantile_99": 0.0507728835494266,
        "hill_tail_index": 3.7502626721472323
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020784096805502764,
        "excess_kurtosis": 11.337994196023944,
        "return_acf_1": -0.09776286112592623,
        "abs_return_acf_1": 0.2858614919414762,
        "abs_return_acf_5": 0.3294780773117495,
        "abs_return_acf_20": 0.2365605172767285,
        "quantile_01": -0.07399535304296603,
        "quantile_99": 0.05405537590603282,
        "hill_tail_index": 2.3701274125671072
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020917518255777232,
        "excess_kurtosis": 8.100051484771786,
        "return_acf_1": -0.2128854347196226,
        "abs_return_acf_1": 0.27694919509542265,
        "abs_return_acf_5": 0.28875977594658575,
        "abs_return_acf_20": 0.2165672715039349,
        "quantile_01": -0.06840506471664855,
        "quantile_99": 0.053095550451824784,
        "hill_tail_index": 3.042913408184148
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018262555324552687,
        "excess_kurtosis": 5.738698392171983,
        "return_acf_1": -0.20663634471106157,
        "abs_return_acf_1": 0.22905508963118573,
        "abs_return_acf_5": 0.22506578333891264,
        "abs_return_acf_20": 0.144073240752645,
        "quantile_01": -0.057830126838825345,
        "quantile_99": 0.051718604846328335,
        "hill_tail_index": 3.7097285998933467
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018710437048162613,
        "excess_kurtosis": 4.648393022461731,
        "return_acf_1": -0.19109885319102377,
        "abs_return_acf_1": 0.30749608648970134,
        "abs_return_acf_5": 0.30181745423454864,
        "abs_return_acf_20": 0.2115743949409426,
        "quantile_01": -0.059854474237738556,
        "quantile_99": 0.051934688952911236,
        "hill_tail_index": 3.7046824720860947
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020410898353570295,
        "excess_kurtosis": 12.33239475662277,
        "return_acf_1": -0.2244090222857183,
        "abs_return_acf_1": 0.3431110167267862,
        "abs_return_acf_5": 0.357610195320578,
        "abs_return_acf_20": 0.27513305202176247,
        "quantile_01": -0.06642549846548222,
        "quantile_99": 0.05140087941590583,
        "hill_tail_index": 2.1650183772841403
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.019521482352414854,
        "excess_kurtosis": 4.10838982022695,
        "return_acf_1": -0.1946318841575184,
        "abs_return_acf_1": 0.2694432508278968,
        "abs_return_acf_5": 0.305700519629409,
        "abs_return_acf_20": 0.23387268409506212,
        "quantile_01": -0.06444865292043177,
        "quantile_99": 0.05816851477519632,
        "hill_tail_index": 4.906361474557352
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02155394615940116,
        "excess_kurtosis": 16.72371027392942,
        "return_acf_1": -0.1986203191405979,
        "abs_return_acf_1": 0.26263752377499044,
        "abs_return_acf_5": 0.3623004225071772,
        "abs_return_acf_20": 0.24431794717135835,
        "quantile_01": -0.0752225241325787,
        "quantile_99": 0.044855879432705414,
        "hill_tail_index": 2.589972670031195
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020660983877535885,
        "excess_kurtosis": 4.138723345275126,
        "return_acf_1": -0.16212007198058218,
        "abs_return_acf_1": 0.31769948014696725,
        "abs_return_acf_5": 0.3048244779083592,
        "abs_return_acf_20": 0.2514422845375378,
        "quantile_01": -0.05939723155203111,
        "quantile_99": 0.06201029790247534,
        "hill_tail_index": 4.394350062123361
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020056407255103346,
        "excess_kurtosis": 12.256413816975382,
        "return_acf_1": -0.18012081733413615,
        "abs_return_acf_1": 0.2842238563520606,
        "abs_return_acf_5": 0.32574661909629177,
        "abs_return_acf_20": 0.18051610997162407,
        "quantile_01": -0.06750450817160968,
        "quantile_99": 0.05011551913009451,
        "hill_tail_index": 3.0515909240293926
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020635182409321176,
        "excess_kurtosis": 4.0157512767533445,
        "return_acf_1": -0.15665698060574787,
        "abs_return_acf_1": 0.29727579256395903,
        "abs_return_acf_5": 0.2549091962470253,
        "abs_return_acf_20": 0.25822637195114456,
        "quantile_01": -0.06358740953934497,
        "quantile_99": 0.05668097698263169,
        "hill_tail_index": 5.345332440036964
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0219504882077385,
        "excess_kurtosis": 4.531823257577183,
        "return_acf_1": -0.1820664245782592,
        "abs_return_acf_1": 0.41728470861370803,
        "abs_return_acf_5": 0.40111389941181685,
        "abs_return_acf_20": 0.32781895990943494,
        "quantile_01": -0.07380308278361394,
        "quantile_99": 0.06399823717687274,
        "hill_tail_index": 4.255261445980312
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019464185755502857,
        "excess_kurtosis": 5.097848804433745,
        "return_acf_1": -0.08562535837343302,
        "abs_return_acf_1": 0.3408831477959867,
        "abs_return_acf_5": 0.32129842474796405,
        "abs_return_acf_20": 0.23240472362021466,
        "quantile_01": -0.07382719748131271,
        "quantile_99": 0.05628717482143021,
        "hill_tail_index": 3.7735667486367523
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01931592146399284,
        "excess_kurtosis": 6.905368169043268,
        "return_acf_1": -0.1253138169906771,
        "abs_return_acf_1": 0.31108448970096253,
        "abs_return_acf_5": 0.2995339385703738,
        "abs_return_acf_20": 0.253187830856716,
        "quantile_01": -0.0599801990376662,
        "quantile_99": 0.05493516885216188,
        "hill_tail_index": 3.207051004866633
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020231608883195588,
        "excess_kurtosis": 5.824676269652796,
        "return_acf_1": -0.11739024500716165,
        "abs_return_acf_1": 0.34134193178931427,
        "abs_return_acf_5": 0.23925228131424792,
        "abs_return_acf_20": 0.2213284940771858,
        "quantile_01": -0.07344837091381047,
        "quantile_99": 0.058773843286878735,
        "hill_tail_index": 3.7196303116632183
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019997700344478748,
        "excess_kurtosis": 3.4306018150801627,
        "return_acf_1": -0.1808914151585725,
        "abs_return_acf_1": 0.3084712800505779,
        "abs_return_acf_5": 0.3283723799563161,
        "abs_return_acf_20": 0.2629657012476198,
        "quantile_01": -0.059815120942100966,
        "quantile_99": 0.05214098140741871,
        "hill_tail_index": 4.019788836053358
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01935717741009754,
        "excess_kurtosis": 7.39220687712808,
        "return_acf_1": -0.09639278270822008,
        "abs_return_acf_1": 0.32906713704645485,
        "abs_return_acf_5": 0.3457039361666003,
        "abs_return_acf_20": 0.23290532792316104,
        "quantile_01": -0.07179686238683926,
        "quantile_99": 0.05155645471898161,
        "hill_tail_index": 2.5774160060973506
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019774588986174558,
        "excess_kurtosis": 8.202646715519025,
        "return_acf_1": -0.11521890001211164,
        "abs_return_acf_1": 0.3794016295989422,
        "abs_return_acf_5": 0.29094174237946147,
        "abs_return_acf_20": 0.2613002184885512,
        "quantile_01": -0.06641959023952522,
        "quantile_99": 0.058163971476983274,
        "hill_tail_index": 3.1539209330363343
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02118281794099709,
        "excess_kurtosis": 5.081823352974025,
        "return_acf_1": -0.15466124288403096,
        "abs_return_acf_1": 0.3529207396477018,
        "abs_return_acf_5": 0.29700937728347493,
        "abs_return_acf_20": 0.26066443916637455,
        "quantile_01": -0.07181920350099051,
        "quantile_99": 0.0554236211232981,
        "hill_tail_index": 3.9297922988538003
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021156271099145172,
        "excess_kurtosis": 3.667488221310843,
        "return_acf_1": -0.1396715956747755,
        "abs_return_acf_1": 0.29653978163801975,
        "abs_return_acf_5": 0.29154898871817375,
        "abs_return_acf_20": 0.2295293153704094,
        "quantile_01": -0.06755440347709092,
        "quantile_99": 0.06299880040077455,
        "hill_tail_index": 5.479264660147833
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021580112901209068,
        "excess_kurtosis": 4.418753996817463,
        "return_acf_1": -0.15450135625856537,
        "abs_return_acf_1": 0.3388200637245028,
        "abs_return_acf_5": 0.33852163742332625,
        "abs_return_acf_20": 0.24691825279634308,
        "quantile_01": -0.06349609543410341,
        "quantile_99": 0.06293415272467716,
        "hill_tail_index": 5.168288921540396
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021163958223532963,
        "excess_kurtosis": 6.309744263827502,
        "return_acf_1": -0.17487665130420998,
        "abs_return_acf_1": 0.34120732734047643,
        "abs_return_acf_5": 0.34014950248748493,
        "abs_return_acf_20": 0.22281325174917546,
        "quantile_01": -0.06993672564966136,
        "quantile_99": 0.06206247562650532,
        "hill_tail_index": 4.127578970720641
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020183657259263552,
        "excess_kurtosis": 6.34804444999693,
        "return_acf_1": -0.11253172531820986,
        "abs_return_acf_1": 0.3760365255817888,
        "abs_return_acf_5": 0.38809580897475826,
        "abs_return_acf_20": 0.2564537678172077,
        "quantile_01": -0.07162146972206261,
        "quantile_99": 0.0498951940946892,
        "hill_tail_index": 3.2509185869419093
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01902727609602035,
        "excess_kurtosis": 4.762040437061825,
        "return_acf_1": -0.16912864581680326,
        "abs_return_acf_1": 0.3096015010248955,
        "abs_return_acf_5": 0.29894334190265004,
        "abs_return_acf_20": 0.22615277726460417,
        "quantile_01": -0.06266385096510121,
        "quantile_99": 0.04823055778507835,
        "hill_tail_index": 3.881275789446113
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020839514544774007,
        "excess_kurtosis": 3.8451062619023304,
        "return_acf_1": -0.1310686789404029,
        "abs_return_acf_1": 0.35300786978227144,
        "abs_return_acf_5": 0.3651968545982708,
        "abs_return_acf_20": 0.2589134451424258,
        "quantile_01": -0.06351363063194274,
        "quantile_99": 0.05718961943152329,
        "hill_tail_index": 4.5108733813692385
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021813972442563393,
        "excess_kurtosis": 4.669916165759403,
        "return_acf_1": -0.14993452937594845,
        "abs_return_acf_1": 0.3445644890887976,
        "abs_return_acf_5": 0.3130515530120796,
        "abs_return_acf_20": 0.3247213293061969,
        "quantile_01": -0.07088174092331563,
        "quantile_99": 0.06502508590593986,
        "hill_tail_index": 5.0242448891979326
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02207113511656561,
        "excess_kurtosis": 4.756648974808428,
        "return_acf_1": -0.18066034560405203,
        "abs_return_acf_1": 0.3048136699899327,
        "abs_return_acf_5": 0.2968704313538713,
        "abs_return_acf_20": 0.2720983645785673,
        "quantile_01": -0.07384090408248417,
        "quantile_99": 0.06155214978991889,
        "hill_tail_index": 4.567010794499965
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
