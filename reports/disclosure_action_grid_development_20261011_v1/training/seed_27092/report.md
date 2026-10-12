# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27092
Run ID: `fc648fa65214874bfd9a3fea010cd8a9caa90917d1af3e0e7073408fdb1f0a96`
Result fingerprint: `7489a386bcd3def389447fe02728e88e93c9a53dd6fa8552d818f7c334b83cae`

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
    "equal_weight_sd": -0.5397976190476157,
    "equal_weight_raw": -8.096964285714238,
    "fixed_start_cap_weight_sd": -0.5594227937732539,
    "fixed_start_cap_weight_raw": -8.391341906598809,
    "end_cap_weight_sd": -0.554289763561184,
    "end_cap_weight_raw": -8.314346453417759
  },
  "full_period_change": {
    "equal_weight_sd": -0.8226547619047572,
    "equal_weight_raw": -12.339821428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7764302248677204,
    "inflation_mean_sd": 0.5381385582010583
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4125833333333364,
    "equal_weight_raw": 6.188750000000047,
    "fixed_start_cap_weight_sd": 0.3929581586076984,
    "fixed_start_cap_weight_raw": 5.894372379115476,
    "end_cap_weight_sd": 0.39809118881976824,
    "end_cap_weight_raw": 5.971367832296524
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5565476190476158,
      "change_raw": -8.348214285714239,
      "decay_adjusted_gain_sd": 0.39583333333333653
    },
    "mid": {
      "count": 9,
      "change_sd": -0.586269841269838,
      "change_raw": -8.794047619047571,
      "decay_adjusted_gain_sd": 0.3661111111111141
    },
    "small": {
      "count": 18,
      "change_sd": -0.513769841269838,
      "change_raw": -7.706547619047571,
      "decay_adjusted_gain_sd": 0.4386111111111143
    },
    "large_minus_small_sd": -0.0427777777777778,
    "large_minus_small_raw": -0.641666666666667
  },
  "inflation": {
    "initial_mean_sd": 0.28933333333333333,
    "final_mean_sd": 0.5191666666666667,
    "mean_sd": 0.44993824590618925,
    "mean_absolute_raw_gap": 6.74907368859284,
    "final_absolute_raw_gap": 7.787499999999999,
    "mean_range_fraction": 0.0674907368859284
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.2,
    "initial_wealth_share": 0.25627695113101695,
    "final_wealth_share": 0.22354831653602508
  },
  "pricing_slope": {
    "mean": -0.0017441148369721233,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.058952468323166515,
    "real_improvement_cost": 0.04574720957342163,
    "washing_cost": 0.013205258749744896,
    "fine_transfer": 0.016081109789337647,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.07503357811250416,
    "resource_cost_fraction_initial_cap": 0.0019650822774388834,
    "private_net_outflow_fraction_initial_cap": 0.0025011192704168053,
    "fine_transfer_fraction_initial_cap": 0.0005360369929779215,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.014284906983530288,
    "unapplied_final_day_resource_cost": 5.5993855790173946e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 209.95728172311513,
    "beneficial_raw_gain_per_resource_cost": 3149.359225846727,
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
    "accrued_cost": 2.938769858998967,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.03742061719151006,
    "accrued_cost_fraction_initial_cap": 0.09795899529996555,
    "mean_contract_rate": 0.04025301494891168,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "maximum_relative_cash_error": 1.5285166125276329e-15,
    "maximum_absolute_share_error": 1.9984014443252818e-15,
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
      "minimum": -0.2766394402505015,
      "maximum": -0.1101758793465787,
      "mean": -0.18968092825422678,
      "median": -0.18619929310597214,
      "quantile_05": -0.25745479997446746,
      "quantile_95": -0.1451877434824138
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
      "minimum": 0.5486834383858844,
      "maximum": 0.8196852031525778,
      "mean": 0.716165454511646,
      "median": 0.7324417826132684,
      "quantile_05": 0.6167561031490308,
      "quantile_95": 0.789556174595016
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
        "daily_volatility": 0.018730786997178547,
        "excess_kurtosis": 5.740464131932825,
        "return_acf_1": -0.17712471996530096,
        "abs_return_acf_1": 0.3501008158871475,
        "abs_return_acf_5": 0.27519843693595364,
        "abs_return_acf_20": 0.28614450608697856,
        "quantile_01": -0.053675871745192894,
        "quantile_99": 0.051271716439234755,
        "hill_tail_index": 3.4281923813139086
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019089708478034265,
        "excess_kurtosis": 8.084451856794207,
        "return_acf_1": -0.2158860870861325,
        "abs_return_acf_1": 0.3527703394181206,
        "abs_return_acf_5": 0.3698268563578813,
        "abs_return_acf_20": 0.3413941630553892,
        "quantile_01": -0.06496653913555667,
        "quantile_99": 0.0488887509589563,
        "hill_tail_index": 3.220806954005742
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.023176066386312658,
        "excess_kurtosis": 12.688473120611704,
        "return_acf_1": -0.20339497859944997,
        "abs_return_acf_1": 0.4668637927279036,
        "abs_return_acf_5": 0.40207512460953637,
        "abs_return_acf_20": 0.4075539907519929,
        "quantile_01": -0.07633525356582548,
        "quantile_99": 0.061893690696341035,
        "hill_tail_index": 3.4784681062718117
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021716935262305108,
        "excess_kurtosis": 18.20657917151797,
        "return_acf_1": -0.1529206831458733,
        "abs_return_acf_1": 0.4581165973921126,
        "abs_return_acf_5": 0.4338569576702486,
        "abs_return_acf_20": 0.4385088020923036,
        "quantile_01": -0.07229074106948193,
        "quantile_99": 0.05659930664729631,
        "hill_tail_index": 2.6391638175592944
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019636594636407392,
        "excess_kurtosis": 7.080676262180749,
        "return_acf_1": -0.20031931545753776,
        "abs_return_acf_1": 0.31282092697652025,
        "abs_return_acf_5": 0.28141153217507553,
        "abs_return_acf_20": 0.29811622054890324,
        "quantile_01": -0.06715526032450456,
        "quantile_99": 0.050633171635545524,
        "hill_tail_index": 2.804587673295584
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02013636580457913,
        "excess_kurtosis": 9.298191489934936,
        "return_acf_1": -0.16810119710126584,
        "abs_return_acf_1": 0.40105667928045274,
        "abs_return_acf_5": 0.347579572253534,
        "abs_return_acf_20": 0.3387995519446879,
        "quantile_01": -0.06766288095128362,
        "quantile_99": 0.050498460025790726,
        "hill_tail_index": 2.6744229357404325
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020673600144612135,
        "excess_kurtosis": 13.556744116035905,
        "return_acf_1": -0.2531569959165532,
        "abs_return_acf_1": 0.3734538376284068,
        "abs_return_acf_5": 0.3295860119954663,
        "abs_return_acf_20": 0.34478312239900083,
        "quantile_01": -0.0773475098701588,
        "quantile_99": 0.051984975953540444,
        "hill_tail_index": 2.496852267400834
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019740774639637,
        "excess_kurtosis": 19.43152600145732,
        "return_acf_1": -0.15363762441717074,
        "abs_return_acf_1": 0.48779861609634384,
        "abs_return_acf_5": 0.4554983834535189,
        "abs_return_acf_20": 0.37095370387874355,
        "quantile_01": -0.07165539848607702,
        "quantile_99": 0.04635543419952326,
        "hill_tail_index": 2.1001582464373247
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021452009187821947,
        "excess_kurtosis": 23.561814788930047,
        "return_acf_1": -0.1101758793465787,
        "abs_return_acf_1": 0.3275043740428629,
        "abs_return_acf_5": 0.27468883859985926,
        "abs_return_acf_20": 0.3135082096320515,
        "quantile_01": -0.07148744640536028,
        "quantile_99": 0.049802688609371024,
        "hill_tail_index": 2.2626873654520137
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020453386606110128,
        "excess_kurtosis": 8.948740651443758,
        "return_acf_1": -0.18872852907731164,
        "abs_return_acf_1": 0.4155111357347655,
        "abs_return_acf_5": 0.3294838910501726,
        "abs_return_acf_20": 0.34920315584532974,
        "quantile_01": -0.062164589816659406,
        "quantile_99": 0.053609778728871724,
        "hill_tail_index": 2.8188794982832652
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01761041956581825,
        "excess_kurtosis": 5.780684428430206,
        "return_acf_1": -0.17944855772501805,
        "abs_return_acf_1": 0.3615436016210597,
        "abs_return_acf_5": 0.2628237253673621,
        "abs_return_acf_20": 0.2827098259737278,
        "quantile_01": -0.05175408457282757,
        "quantile_99": 0.04553141218775161,
        "hill_tail_index": 2.9788341157271754
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019329143705501994,
        "excess_kurtosis": 18.125356680353203,
        "return_acf_1": -0.1407388430254838,
        "abs_return_acf_1": 0.5203883754380788,
        "abs_return_acf_5": 0.33697702142850067,
        "abs_return_acf_20": 0.4063168425870624,
        "quantile_01": -0.06124819827468279,
        "quantile_99": 0.047212482573625564,
        "hill_tail_index": 2.1216230277517054
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020538802560800803,
        "excess_kurtosis": 11.045559719330305,
        "return_acf_1": -0.1754411062357802,
        "abs_return_acf_1": 0.44352118305739097,
        "abs_return_acf_5": 0.4153511706581069,
        "abs_return_acf_20": 0.4034318909225095,
        "quantile_01": -0.0690959337611858,
        "quantile_99": 0.05000384063494674,
        "hill_tail_index": 2.8384408236779333
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021133425809638003,
        "excess_kurtosis": 12.27998331100098,
        "return_acf_1": -0.22199352498531946,
        "abs_return_acf_1": 0.4228883373897826,
        "abs_return_acf_5": 0.3158462394017856,
        "abs_return_acf_20": 0.2797045296650027,
        "quantile_01": -0.06793483706335632,
        "quantile_99": 0.0520353970917109,
        "hill_tail_index": 2.881961119094478
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020898747535770052,
        "excess_kurtosis": 15.77265455364375,
        "return_acf_1": -0.16907638691834928,
        "abs_return_acf_1": 0.36731251106971224,
        "abs_return_acf_5": 0.34273731966112453,
        "abs_return_acf_20": 0.3543498048298803,
        "quantile_01": -0.06545402324478293,
        "quantile_99": 0.047464045086331424,
        "hill_tail_index": 2.141647538564826
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020706811950411783,
        "excess_kurtosis": 11.16880136676428,
        "return_acf_1": -0.2100318308435813,
        "abs_return_acf_1": 0.4285651192274489,
        "abs_return_acf_5": 0.31169443401961094,
        "abs_return_acf_20": 0.38055705782395455,
        "quantile_01": -0.07691731144327667,
        "quantile_99": 0.05686466818003455,
        "hill_tail_index": 2.7042925455388946
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02084822609703408,
        "excess_kurtosis": 12.658506768868289,
        "return_acf_1": -0.15391261073171675,
        "abs_return_acf_1": 0.3954081663561625,
        "abs_return_acf_5": 0.34630793660098264,
        "abs_return_acf_20": 0.3435023871883165,
        "quantile_01": -0.06906556823514473,
        "quantile_99": 0.048645085731336205,
        "hill_tail_index": 2.46458836083475
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019492304254562227,
        "excess_kurtosis": 7.65729597326343,
        "return_acf_1": -0.18367005713463264,
        "abs_return_acf_1": 0.3328123620705657,
        "abs_return_acf_5": 0.24419846362942063,
        "abs_return_acf_20": 0.30981535668608906,
        "quantile_01": -0.053809922391812204,
        "quantile_99": 0.053604379817432594,
        "hill_tail_index": 2.6544500552358827
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021584618061868812,
        "excess_kurtosis": 11.580492364702105,
        "return_acf_1": -0.22279193504998357,
        "abs_return_acf_1": 0.47900209570902,
        "abs_return_acf_5": 0.45801237888504504,
        "abs_return_acf_20": 0.4308434628590678,
        "quantile_01": -0.07701998009097816,
        "quantile_99": 0.06314919242600517,
        "hill_tail_index": 3.3428432354805353
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022134438115692476,
        "excess_kurtosis": 15.884415698132393,
        "return_acf_1": -0.26097118511276096,
        "abs_return_acf_1": 0.44657906233347644,
        "abs_return_acf_5": 0.4278766109716335,
        "abs_return_acf_20": 0.37411248716297557,
        "quantile_01": -0.07482627680546032,
        "quantile_99": 0.055198356216713394,
        "hill_tail_index": 2.1122578968793153
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020700108540332177,
        "excess_kurtosis": 26.184760001832306,
        "return_acf_1": -0.2766394402505015,
        "abs_return_acf_1": 0.44533156807832486,
        "abs_return_acf_5": 0.3500517517411119,
        "abs_return_acf_20": 0.35443332448885706,
        "quantile_01": -0.07293285765391931,
        "quantile_99": 0.040650298850491956,
        "hill_tail_index": 1.5604575126563358
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02217426075387717,
        "excess_kurtosis": 21.62707419183428,
        "return_acf_1": -0.15062528848532822,
        "abs_return_acf_1": 0.34836203930921517,
        "abs_return_acf_5": 0.25756724551306254,
        "abs_return_acf_20": 0.32006421209086533,
        "quantile_01": -0.07158892713584095,
        "quantile_99": 0.052884313007530215,
        "hill_tail_index": 1.994311194109946
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.021955309638818945,
        "excess_kurtosis": 13.77724736889132,
        "return_acf_1": -0.2097482811022653,
        "abs_return_acf_1": 0.4755350819484981,
        "abs_return_acf_5": 0.36172337351252726,
        "abs_return_acf_20": 0.35397615929984694,
        "quantile_01": -0.0777809433057681,
        "quantile_99": 0.05486200156065336,
        "hill_tail_index": 2.3728760916878917
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01923601392227105,
        "excess_kurtosis": 12.922472144113593,
        "return_acf_1": -0.1685740221282775,
        "abs_return_acf_1": 0.351478591896278,
        "abs_return_acf_5": 0.32601101864240034,
        "abs_return_acf_20": 0.3399302547413439,
        "quantile_01": -0.06537890273715503,
        "quantile_99": 0.046899432093214975,
        "hill_tail_index": 2.8556393467999666
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020484486411877174,
        "excess_kurtosis": 7.872904559891822,
        "return_acf_1": -0.19479077497491315,
        "abs_return_acf_1": 0.329742691018089,
        "abs_return_acf_5": 0.3331807213001725,
        "abs_return_acf_20": 0.32219961765695376,
        "quantile_01": -0.06641907663399088,
        "quantile_99": 0.0530751304754051,
        "hill_tail_index": 2.7054256986702216
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018606007401147963,
        "excess_kurtosis": 8.561473162162605,
        "return_acf_1": -0.16197659075074233,
        "abs_return_acf_1": 0.378838764921638,
        "abs_return_acf_5": 0.3591196935275565,
        "abs_return_acf_20": 0.3722537557340585,
        "quantile_01": -0.06538946476198448,
        "quantile_99": 0.044190378811608845,
        "hill_tail_index": 3.2440428413150015
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.0198497835219332,
        "excess_kurtosis": 10.719290971882955,
        "return_acf_1": -0.1946846151259822,
        "abs_return_acf_1": 0.3700767432547269,
        "abs_return_acf_5": 0.3947900683383574,
        "abs_return_acf_20": 0.40553768431363246,
        "quantile_01": -0.06923731739756488,
        "quantile_99": 0.050860864298618046,
        "hill_tail_index": 2.745099739914832
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02348521366439798,
        "excess_kurtosis": 11.957411295594326,
        "return_acf_1": -0.21943389569256275,
        "abs_return_acf_1": 0.48308566884071946,
        "abs_return_acf_5": 0.45921250173878064,
        "abs_return_acf_20": 0.3952098329557105,
        "quantile_01": -0.086185895596053,
        "quantile_99": 0.07130978449678985,
        "hill_tail_index": 3.133232189732852
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018505311430812306,
        "excess_kurtosis": 13.39856974578463,
        "return_acf_1": -0.1526286491870514,
        "abs_return_acf_1": 0.3499551625461584,
        "abs_return_acf_5": 0.336140801710815,
        "abs_return_acf_20": 0.2884638826048715,
        "quantile_01": -0.06378542920541393,
        "quantile_99": 0.04344471230334768,
        "hill_tail_index": 2.4925196619309635
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019583516227806103,
        "excess_kurtosis": 9.94703072112995,
        "return_acf_1": -0.21980424205337912,
        "abs_return_acf_1": 0.40030205701350885,
        "abs_return_acf_5": 0.33944597686123723,
        "abs_return_acf_20": 0.28572319290402176,
        "quantile_01": -0.06751659996678899,
        "quantile_99": 0.04550041216946564,
        "hill_tail_index": 2.2130200091403984
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
