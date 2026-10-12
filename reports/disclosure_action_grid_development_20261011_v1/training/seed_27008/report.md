# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27008
Run ID: `964404959d99fb7b6f775c1ad4e887f72bd9a8638bedd9d11001b50413606361`
Result fingerprint: `14ae7d8ca64f0f2d2b43e8e1469ead39e53aabd3d4c36d02adb93cbcdcd3e06b`

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
    "equal_weight_sd": -0.4450476190476157,
    "equal_weight_raw": -6.675714285714236,
    "fixed_start_cap_weight_sd": -0.4410058219695433,
    "fixed_start_cap_weight_raw": -6.61508732954315,
    "end_cap_weight_sd": -0.43388557414759293,
    "end_cap_weight_raw": -6.508283612213894
  },
  "full_period_change": {
    "equal_weight_sd": -0.750154761904757,
    "equal_weight_raw": -11.252321428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.703242063492059,
    "inflation_mean_sd": 0.49960052910052916
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5073333333333366,
    "equal_weight_raw": 7.610000000000048,
    "fixed_start_cap_weight_sd": 0.5113751304114093,
    "fixed_start_cap_weight_raw": 7.670626956171138,
    "end_cap_weight_sd": 0.5184953782333594,
    "end_cap_weight_raw": 7.777430673500391
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.4298809523809495,
      "change_raw": -6.448214285714242,
      "decay_adjusted_gain_sd": 0.522500000000003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4623809523809492,
      "change_raw": -6.935714285714238,
      "decay_adjusted_gain_sd": 0.49000000000000316
    },
    "small": {
      "count": 18,
      "change_sd": -0.4389087301587268,
      "change_raw": -6.583630952380902,
      "decay_adjusted_gain_sd": 0.5134722222222254
    },
    "large_minus_small_sd": 0.009027777777777302,
    "large_minus_small_raw": 0.13541666666665952
  },
  "inflation": {
    "initial_mean_sd": 0.19499999999999998,
    "final_mean_sd": 0.53225,
    "mean_sd": 0.3835350402442409,
    "mean_absolute_raw_gap": 5.753025603663614,
    "final_absolute_raw_gap": 7.983749999999998,
    "mean_range_fraction": 0.05753025603663614
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.31333333333333335,
    "initial_wealth_share": 0.3762207723559516,
    "final_wealth_share": 0.35343650621869266
  },
  "pricing_slope": {
    "mean": -0.0012868549446940678,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.25003603790651213,
    "real_improvement_cost": 0.2138368669278051,
    "washing_cost": 0.03619917097870699,
    "fine_transfer": 0.006360894199434365,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2563969321059465,
    "resource_cost_fraction_initial_cap": 0.008334534596883738,
    "private_net_outflow_fraction_initial_cap": 0.008546564403531551,
    "fine_transfer_fraction_initial_cap": 0.00021202980664781218,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.009262109995097556,
    "unapplied_final_day_resource_cost": 0.0030990173763378996
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 60.87122531389183,
    "beneficial_raw_gain_per_resource_cost": 913.0683797083775,
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
    "fixed_exposure": 14.999999999999998,
    "accrued_cost": 2.826524992592913,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.14966548359756332,
    "accrued_cost_fraction_initial_cap": 0.09421749975309711,
    "mean_contract_rate": 0.03947103146639357,
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
    "maximum_relative_cash_error": 2.016952741923753e-15,
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
      "minimum": -0.28248602910241877,
      "maximum": -0.0023800383115735488,
      "mean": -0.12817806103363713,
      "median": -0.12185427393379762,
      "quantile_05": -0.2283673750300743,
      "quantile_95": -0.028030754212219854
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
      "minimum": 0.2368900140715788,
      "maximum": 0.7828468700983238,
      "mean": 0.5218383541999604,
      "median": 0.5009164264514231,
      "quantile_05": 0.30841430129403286,
      "quantile_95": 0.7448026339114088
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
        "daily_volatility": 0.018910320868967264,
        "excess_kurtosis": 2.5807994695735097,
        "return_acf_1": -0.21464215852167992,
        "abs_return_acf_1": 0.3289330844163794,
        "abs_return_acf_5": 0.25339109246508323,
        "abs_return_acf_20": 0.22616325110516353,
        "quantile_01": -0.060675745022531036,
        "quantile_99": 0.0507755015799258,
        "hill_tail_index": 3.934162391263925
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01962907120290819,
        "excess_kurtosis": 9.380632673054862,
        "return_acf_1": -0.05797140274803017,
        "abs_return_acf_1": 0.3271267355178018,
        "abs_return_acf_5": 0.3680851683815468,
        "abs_return_acf_20": 0.33407895686621475,
        "quantile_01": -0.0682252705248212,
        "quantile_99": 0.05736309541515614,
        "hill_tail_index": 2.9315488467711917
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018206279921136853,
        "excess_kurtosis": 7.738496453939323,
        "return_acf_1": -0.10689970181461854,
        "abs_return_acf_1": 0.2591734966574027,
        "abs_return_acf_5": 0.2875924874527278,
        "abs_return_acf_20": 0.2226094047283597,
        "quantile_01": -0.05061867945263794,
        "quantile_99": 0.04842014141519414,
        "hill_tail_index": 3.565416252700005
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019527217304373554,
        "excess_kurtosis": 9.270859126689466,
        "return_acf_1": -0.059060173079574646,
        "abs_return_acf_1": 0.35386251596710144,
        "abs_return_acf_5": 0.3044447545035159,
        "abs_return_acf_20": 0.2679197973855273,
        "quantile_01": -0.06378433266676427,
        "quantile_99": 0.048348875386469495,
        "hill_tail_index": 2.4412015882590614
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017917296029429274,
        "excess_kurtosis": 5.36646496091717,
        "return_acf_1": -0.0910333737149478,
        "abs_return_acf_1": 0.3978419379629255,
        "abs_return_acf_5": 0.30154731119167194,
        "abs_return_acf_20": 0.2348726930492463,
        "quantile_01": -0.05507529831790239,
        "quantile_99": 0.04848672640960796,
        "hill_tail_index": 3.2180721822853244
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017505595627225777,
        "excess_kurtosis": 6.904410722139691,
        "return_acf_1": -0.12252890033850697,
        "abs_return_acf_1": 0.24510511236473922,
        "abs_return_acf_5": 0.25668850739100413,
        "abs_return_acf_20": 0.22489464115035468,
        "quantile_01": -0.04680619579053569,
        "quantile_99": 0.04894755224613311,
        "hill_tail_index": 3.4088007269343437
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0228227617911408,
        "excess_kurtosis": 11.54899276668386,
        "return_acf_1": -0.21914689621627878,
        "abs_return_acf_1": 0.4051713877497523,
        "abs_return_acf_5": 0.3551939561081044,
        "abs_return_acf_20": 0.2950286992928027,
        "quantile_01": -0.089818682654316,
        "quantile_99": 0.07082055817784833,
        "hill_tail_index": 2.714328176446692
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02077976463554916,
        "excess_kurtosis": 11.224406867078676,
        "return_acf_1": -0.04249034536264817,
        "abs_return_acf_1": 0.4125853471386846,
        "abs_return_acf_5": 0.38868564682584383,
        "abs_return_acf_20": 0.32127211531622646,
        "quantile_01": -0.0709028434695205,
        "quantile_99": 0.056368530072548356,
        "hill_tail_index": 3.0271150223295353
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01865959266116754,
        "excess_kurtosis": 6.654582522407395,
        "return_acf_1": -0.16876297713623145,
        "abs_return_acf_1": 0.3130700516022361,
        "abs_return_acf_5": 0.23992386471584873,
        "abs_return_acf_20": 0.21170042247521156,
        "quantile_01": -0.0613899019138579,
        "quantile_99": 0.051944904089710225,
        "hill_tail_index": 3.626889186139084
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021071810628952102,
        "excess_kurtosis": 13.768573039385473,
        "return_acf_1": -0.0965368891959242,
        "abs_return_acf_1": 0.3977821175178668,
        "abs_return_acf_5": 0.2793700222579854,
        "abs_return_acf_20": 0.2973920421218978,
        "quantile_01": -0.06585274386796189,
        "quantile_99": 0.05731200193841933,
        "hill_tail_index": 3.358671353081668
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020642134454741296,
        "excess_kurtosis": 7.426021123655488,
        "return_acf_1": -0.23591140315045245,
        "abs_return_acf_1": 0.37358045163215775,
        "abs_return_acf_5": 0.29536770577837346,
        "abs_return_acf_20": 0.24561622886378548,
        "quantile_01": -0.06499827130364375,
        "quantile_99": 0.06413901104360109,
        "hill_tail_index": 5.014637874716338
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018966320554898813,
        "excess_kurtosis": 9.595321127012886,
        "return_acf_1": -0.025701954648346608,
        "abs_return_acf_1": 0.31301993164209896,
        "abs_return_acf_5": 0.31062779551721287,
        "abs_return_acf_20": 0.27528110917199616,
        "quantile_01": -0.06293119748081698,
        "quantile_99": 0.049526284908496775,
        "hill_tail_index": 2.818199882778997
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019573663037023594,
        "excess_kurtosis": 6.585224681737177,
        "return_acf_1": -0.12117964752908827,
        "abs_return_acf_1": 0.388096214929717,
        "abs_return_acf_5": 0.33650665582292927,
        "abs_return_acf_20": 0.27632765888853666,
        "quantile_01": -0.06119332894590543,
        "quantile_99": 0.05352151359979834,
        "hill_tail_index": 3.2513024555643915
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01868800257762562,
        "excess_kurtosis": 10.486122249983845,
        "return_acf_1": -0.03087706479028712,
        "abs_return_acf_1": 0.4030933297193999,
        "abs_return_acf_5": 0.34718614706589346,
        "abs_return_acf_20": 0.24412203871115404,
        "quantile_01": -0.05515181087912682,
        "quantile_99": 0.047773468279826085,
        "hill_tail_index": 2.962773492845457
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017909901051672592,
        "excess_kurtosis": 3.4186064218551477,
        "return_acf_1": -0.20307699442248325,
        "abs_return_acf_1": 0.2943591282752678,
        "abs_return_acf_5": 0.212492179991768,
        "abs_return_acf_20": 0.1067055099976199,
        "quantile_01": -0.05436076899933025,
        "quantile_99": 0.04733418668669192,
        "hill_tail_index": 4.013948553672009
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02052934867699734,
        "excess_kurtosis": 9.511211196564048,
        "return_acf_1": -0.131890137218295,
        "abs_return_acf_1": 0.4361890720874759,
        "abs_return_acf_5": 0.3433564271933073,
        "abs_return_acf_20": 0.3456835315031513,
        "quantile_01": -0.06578737828115494,
        "quantile_99": 0.05789047478435419,
        "hill_tail_index": 3.0499581790337684
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019106640069367735,
        "excess_kurtosis": 9.256137971862087,
        "return_acf_1": -0.19574616505419404,
        "abs_return_acf_1": 0.2781858208993423,
        "abs_return_acf_5": 0.24263425524571572,
        "abs_return_acf_20": 0.23075532836955026,
        "quantile_01": -0.05429564224894839,
        "quantile_99": 0.05105960192819452,
        "hill_tail_index": 3.005700892592093
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019454323516514667,
        "excess_kurtosis": 15.385683815466876,
        "return_acf_1": -0.052511913804348574,
        "abs_return_acf_1": 0.39961346051744484,
        "abs_return_acf_5": 0.4273500778451237,
        "abs_return_acf_20": 0.28983143285620194,
        "quantile_01": -0.05787046938954845,
        "quantile_99": 0.047752762055965695,
        "hill_tail_index": 2.751731248095056
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018452533763227152,
        "excess_kurtosis": 2.331055767321497,
        "return_acf_1": -0.1573946570523155,
        "abs_return_acf_1": 0.2681634045766376,
        "abs_return_acf_5": 0.19597289962962142,
        "abs_return_acf_20": 0.24175360327224532,
        "quantile_01": -0.052491351048940066,
        "quantile_99": 0.04647587575824202,
        "hill_tail_index": 5.489030752012519
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016317856982869507,
        "excess_kurtosis": 2.968069805288991,
        "return_acf_1": -0.11247843497127649,
        "abs_return_acf_1": 0.23790735472757318,
        "abs_return_acf_5": 0.16478642937874455,
        "abs_return_acf_20": 0.12492456053401735,
        "quantile_01": -0.04238784859105067,
        "quantile_99": 0.041049863042032265,
        "hill_tail_index": 3.776195653739364
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016989686138104223,
        "excess_kurtosis": 2.6232972633028977,
        "return_acf_1": -0.13548066029827852,
        "abs_return_acf_1": 0.3060930117680446,
        "abs_return_acf_5": 0.1993659308620818,
        "abs_return_acf_20": 0.20026951655216935,
        "quantile_01": -0.048328063182271654,
        "quantile_99": 0.043508800756379744,
        "hill_tail_index": 3.951438072954761
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017641991883840635,
        "excess_kurtosis": 5.90316759408549,
        "return_acf_1": -0.0687778721907439,
        "abs_return_acf_1": 0.3068701170816852,
        "abs_return_acf_5": 0.26812399618879884,
        "abs_return_acf_20": 0.2274089241466009,
        "quantile_01": -0.0553970840408573,
        "quantile_99": 0.039157390639988084,
        "hill_tail_index": 3.1007027273714947
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01953364100201546,
        "excess_kurtosis": 8.21562780255663,
        "return_acf_1": -0.0989675860045179,
        "abs_return_acf_1": 0.39366560327624217,
        "abs_return_acf_5": 0.30916151720770585,
        "abs_return_acf_20": 0.23907701607632217,
        "quantile_01": -0.06573353336197596,
        "quantile_99": 0.05282973155463689,
        "hill_tail_index": 2.761870490802849
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019044606725476906,
        "excess_kurtosis": 4.4629609805271535,
        "return_acf_1": -0.18142723223446525,
        "abs_return_acf_1": 0.30366441118615906,
        "abs_return_acf_5": 0.25497476396997476,
        "abs_return_acf_20": 0.2190567377534798,
        "quantile_01": -0.05451727326536242,
        "quantile_99": 0.05176676328530557,
        "hill_tail_index": 3.862933358347385
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01758684390966042,
        "excess_kurtosis": 2.5126444490264355,
        "return_acf_1": -0.17438954081901867,
        "abs_return_acf_1": 0.3014604066650877,
        "abs_return_acf_5": 0.13928174581323507,
        "abs_return_acf_20": 0.17497886686417352,
        "quantile_01": -0.05005041374418167,
        "quantile_99": 0.045116630260347075,
        "hill_tail_index": 3.906473461352296
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01817914659969709,
        "excess_kurtosis": 10.297406663185473,
        "return_acf_1": -0.2007926735646617,
        "abs_return_acf_1": 0.26522084391485207,
        "abs_return_acf_5": 0.28050821962611716,
        "abs_return_acf_20": 0.2392648793779903,
        "quantile_01": -0.053175940646067295,
        "quantile_99": 0.042440729713644466,
        "hill_tail_index": 2.1740852959006904
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020733026985660135,
        "excess_kurtosis": 11.607817410793222,
        "return_acf_1": -0.28248602910241877,
        "abs_return_acf_1": 0.40506799570618063,
        "abs_return_acf_5": 0.35634263986402065,
        "abs_return_acf_20": 0.2069188366339193,
        "quantile_01": -0.07830000869788573,
        "quantile_99": 0.05367688015395869,
        "hill_tail_index": 2.69844766923032
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019347005951820564,
        "excess_kurtosis": 7.438132768315793,
        "return_acf_1": -0.09336950858839702,
        "abs_return_acf_1": 0.39329619200877375,
        "abs_return_acf_5": 0.3556007971235645,
        "abs_return_acf_20": 0.3504507353026798,
        "quantile_01": -0.06402393345365692,
        "quantile_99": 0.05168607196395344,
        "hill_tail_index": 2.8697163324084447
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017457291846352776,
        "excess_kurtosis": 2.2257580349812542,
        "return_acf_1": -0.16142949912551116,
        "abs_return_acf_1": 0.3130202034935719,
        "abs_return_acf_5": 0.2560659439001082,
        "abs_return_acf_20": 0.17402483313272477,
        "quantile_01": -0.0497840133219788,
        "quantile_99": 0.04975824855068304,
        "hill_tail_index": 5.305456142713783
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.018693117016621526,
        "excess_kurtosis": 6.605634497300731,
        "return_acf_1": -0.0023800383115735488,
        "abs_return_acf_1": 0.4041183911915394,
        "abs_return_acf_5": 0.32985134789163567,
        "abs_return_acf_20": 0.26335019865156123,
        "quantile_01": -0.06382150115588385,
        "quantile_99": 0.05052263867498949,
        "hill_tail_index": 3.3068435525004896
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
Unseen state share: 0.0022222222222222222
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
