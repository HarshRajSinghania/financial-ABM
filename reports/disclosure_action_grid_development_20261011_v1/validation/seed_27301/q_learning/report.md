# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27301
Run ID: `47054699bf20233c0d69bbf1254d1bc77b8a5118403eff13e41700e8a9e4e7ac`
Result fingerprint: `450a0666c47b8d8ca6c834c13ea39d06a61804af2adf80feee9c1a671f1f5c7a`

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
    "equal_weight_sd": -0.8735476190476158,
    "equal_weight_raw": -13.103214285714238,
    "fixed_start_cap_weight_sd": -0.8149885562266487,
    "fixed_start_cap_weight_raw": -12.22482834339973,
    "end_cap_weight_sd": -0.8158611946351085,
    "end_cap_weight_raw": -12.237917919526632
  },
  "full_period_change": {
    "equal_weight_sd": -1.332404761904757,
    "equal_weight_raw": -19.986071428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2459523809523763,
    "inflation_mean_sd": 0.24197817460317458
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.073617478523515,
    "equal_weight_raw": 1.1042621778527248,
    "fixed_start_cap_weight_sd": 0.13024421213241272,
    "fixed_start_cap_weight_raw": 1.953663181986191,
    "end_cap_weight_sd": 0.13091628519035584,
    "end_cap_weight_raw": 1.9637442778553378
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7507142857142823,
      "change_raw": -11.260714285714235,
      "decay_adjusted_gain_sd": 0.2016666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7857142857142824,
      "change_raw": -11.785714285714235,
      "decay_adjusted_gain_sd": 0.14928048396726465
    },
    "small": {
      "count": 18,
      "change_sd": -0.9379365079365046,
      "change_raw": -14.06904761904757,
      "decay_adjusted_gain_sd": 0.014444444444447677
    },
    "large_minus_small_sd": 0.1872222222222223,
    "large_minus_small_raw": 2.8083333333333345
  },
  "inflation": {
    "initial_mean_sd": 0.18891666666666665,
    "final_mean_sd": 0.22408333333333333,
    "mean_sd": 0.2246245489869553,
    "mean_absolute_raw_gap": 3.3693682348043295,
    "final_absolute_raw_gap": 3.3612500000000005,
    "mean_range_fraction": 0.03369368234804329
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.26666666666666666,
    "initial_wealth_share": 0.35040219806268985,
    "final_wealth_share": 0.35871987575996367
  },
  "pricing_slope": {
    "mean": -0.0017587319499443622,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.0031776838033964723,
    "real_improvement_cost": 0.0017852901827433883,
    "washing_cost": 0.0013923936206530836,
    "fine_transfer": 0.008402588742757969,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.01158027254615444,
    "resource_cost_fraction_initial_cap": 0.00010592279344654908,
    "private_net_outflow_fraction_initial_cap": 0.0003860090848718147,
    "fine_transfer_fraction_initial_cap": 0.0002800862914252656,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00027726428080409324,
    "unapplied_final_day_resource_cost": 0.00026371163544770874
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 695.0107349714484,
    "beneficial_raw_gain_per_resource_cost": 10425.161024571726,
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
    "accrued_cost": 2.9108098597268164,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.06538061646365965,
    "accrued_cost_fraction_initial_cap": 0.09702699532422722,
    "mean_contract_rate": 0.040517532012878596,
    "maximum_ledger_error": 6.606856988583543e-20
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
    "maximum_relative_cash_error": 1.7979428294576136e-15,
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
      "minimum": -0.200125964355047,
      "maximum": 0.03989750398480602,
      "mean": -0.10480563571228288,
      "median": -0.11189847289351834,
      "quantile_05": -0.15750199119916244,
      "quantile_95": -0.0072646478831748205
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
      "minimum": 0.2510509485449771,
      "maximum": 0.7439949585590864,
      "mean": 0.424790147572093,
      "median": 0.3718117300515828,
      "quantile_05": 0.284274210919073,
      "quantile_95": 0.683896582826492
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
        "daily_volatility": 0.019294618345960992,
        "excess_kurtosis": 9.302050719557803,
        "return_acf_1": -0.1335690911928359,
        "abs_return_acf_1": 0.3349939761705783,
        "abs_return_acf_5": 0.3876053691829446,
        "abs_return_acf_20": 0.26334002668500855,
        "quantile_01": -0.051961941082621525,
        "quantile_99": 0.059156181042021645,
        "hill_tail_index": 2.6349765725749195
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020395321316763197,
        "excess_kurtosis": 14.415977667737298,
        "return_acf_1": -0.1575101580710713,
        "abs_return_acf_1": 0.36396578766536075,
        "abs_return_acf_5": 0.35500921760734394,
        "abs_return_acf_20": 0.20900904731726858,
        "quantile_01": -0.06504143538298009,
        "quantile_99": 0.060824109852912076,
        "hill_tail_index": 1.9237661739753038
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018361358424680202,
        "excess_kurtosis": 5.217557304077225,
        "return_acf_1": -0.1287801717944813,
        "abs_return_acf_1": 0.32323159775031657,
        "abs_return_acf_5": 0.331083309686639,
        "abs_return_acf_20": 0.2794966387049213,
        "quantile_01": -0.059162566951315464,
        "quantile_99": 0.060112385704824606,
        "hill_tail_index": 5.4622140131408425
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016681860329448902,
        "excess_kurtosis": 9.133079692082372,
        "return_acf_1": -0.11250045283585008,
        "abs_return_acf_1": 0.36842330464395756,
        "abs_return_acf_5": 0.3506766071391711,
        "abs_return_acf_20": 0.29515013771074894,
        "quantile_01": -0.04639282124355394,
        "quantile_99": 0.04146960833853119,
        "hill_tail_index": 3.3134232353193553
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01980075436107087,
        "excess_kurtosis": 8.935470766451157,
        "return_acf_1": -0.15309863270467458,
        "abs_return_acf_1": 0.32714112636351433,
        "abs_return_acf_5": 0.31343778789596943,
        "abs_return_acf_20": 0.27699274936331936,
        "quantile_01": -0.06125573407894806,
        "quantile_99": 0.055399233499167616,
        "hill_tail_index": 2.662260274712753
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019372551728397743,
        "excess_kurtosis": 6.259335782015791,
        "return_acf_1": -0.12038527474524302,
        "abs_return_acf_1": 0.36287596228644214,
        "abs_return_acf_5": 0.3316817640608639,
        "abs_return_acf_20": 0.20734514149738478,
        "quantile_01": -0.06205308413260339,
        "quantile_99": 0.0557066516570743,
        "hill_tail_index": 3.020097659674491
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016318389937893023,
        "excess_kurtosis": 8.231488750058496,
        "return_acf_1": -0.061391476368252575,
        "abs_return_acf_1": 0.3087754000731589,
        "abs_return_acf_5": 0.21632030086619988,
        "abs_return_acf_20": 0.28669868958687,
        "quantile_01": -0.04614197917693596,
        "quantile_99": 0.04121521829534227,
        "hill_tail_index": 2.9958069617021654
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017827127875087154,
        "excess_kurtosis": 13.774358208608021,
        "return_acf_1": 0.02124119169979644,
        "abs_return_acf_1": 0.364243379191585,
        "abs_return_acf_5": 0.28023299888393155,
        "abs_return_acf_20": 0.3432815501327564,
        "quantile_01": -0.0553830576968891,
        "quantile_99": 0.049276912488759095,
        "hill_tail_index": 2.009058759811037
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01763403098143455,
        "excess_kurtosis": 8.099761467452838,
        "return_acf_1": -0.10943428506978259,
        "abs_return_acf_1": 0.28282538959484105,
        "abs_return_acf_5": 0.30130398229248934,
        "abs_return_acf_20": 0.20789638973834562,
        "quantile_01": -0.05067184064509875,
        "quantile_99": 0.05437853525645034,
        "hill_tail_index": 3.2455090200654864
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023545639276974156,
        "excess_kurtosis": 12.55847800610271,
        "return_acf_1": -0.14459083705093995,
        "abs_return_acf_1": 0.3712204726600738,
        "abs_return_acf_5": 0.45171694104039556,
        "abs_return_acf_20": 0.2600054011896682,
        "quantile_01": -0.07217713716935018,
        "quantile_99": 0.08464948814476868,
        "hill_tail_index": 2.9871310525204304
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01832842630132854,
        "excess_kurtosis": 5.023062025627057,
        "return_acf_1": -0.15749200946682942,
        "abs_return_acf_1": 0.2614486414921162,
        "abs_return_acf_5": 0.25605722566051586,
        "abs_return_acf_20": 0.22360416257069127,
        "quantile_01": -0.05687668911507825,
        "quantile_99": 0.05446914395653383,
        "hill_tail_index": 3.7329845139954383
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018941813684162256,
        "excess_kurtosis": 5.058218893443952,
        "return_acf_1": -0.09516427817474475,
        "abs_return_acf_1": 0.34111119762999503,
        "abs_return_acf_5": 0.25450777337728353,
        "abs_return_acf_20": 0.17083830148298354,
        "quantile_01": -0.05619706206462415,
        "quantile_99": 0.05507290868101885,
        "hill_tail_index": 4.458224384760829
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017504481514274174,
        "excess_kurtosis": 5.26197004640448,
        "return_acf_1": -0.131398757992682,
        "abs_return_acf_1": 0.342131121515569,
        "abs_return_acf_5": 0.24983055372648924,
        "abs_return_acf_20": 0.30574861596173925,
        "quantile_01": -0.05181628654540665,
        "quantile_99": 0.05355506069833272,
        "hill_tail_index": 4.208418025788838
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019379093668823358,
        "excess_kurtosis": 7.070666502084769,
        "return_acf_1": -0.08368920635745072,
        "abs_return_acf_1": 0.38468417098596364,
        "abs_return_acf_5": 0.3289671740865993,
        "abs_return_acf_20": 0.2727738488220758,
        "quantile_01": -0.05683872520378323,
        "quantile_99": 0.059094009942699824,
        "hill_tail_index": 2.79508513769523
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01746379007623011,
        "excess_kurtosis": 6.610604047586163,
        "return_acf_1": -0.14648197154167758,
        "abs_return_acf_1": 0.39402025251978245,
        "abs_return_acf_5": 0.3496631912342217,
        "abs_return_acf_20": 0.2514347601308574,
        "quantile_01": -0.05533464515481487,
        "quantile_99": 0.05337046391347222,
        "hill_tail_index": 3.849486535472112
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020342902967240336,
        "excess_kurtosis": 7.651945852354391,
        "return_acf_1": -0.200125964355047,
        "abs_return_acf_1": 0.3995860774864897,
        "abs_return_acf_5": 0.396231930863623,
        "abs_return_acf_20": 0.2894605376839312,
        "quantile_01": -0.06496920072118667,
        "quantile_99": 0.060297384381887496,
        "hill_tail_index": 3.341735721034741
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01945270913536404,
        "excess_kurtosis": 3.6281006655545553,
        "return_acf_1": -0.11129649295118661,
        "abs_return_acf_1": 0.35289752933880447,
        "abs_return_acf_5": 0.31098098583859063,
        "abs_return_acf_20": 0.2717861576540862,
        "quantile_01": -0.0631847549481768,
        "quantile_99": 0.05695044689027256,
        "hill_tail_index": 4.17212930552826
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018640645303595042,
        "excess_kurtosis": 5.241849995460653,
        "return_acf_1": -0.06926040065308839,
        "abs_return_acf_1": 0.2846771666937865,
        "abs_return_acf_5": 0.2530680446392604,
        "abs_return_acf_20": 0.21298424291475715,
        "quantile_01": -0.059503246216191415,
        "quantile_99": 0.054025014646568975,
        "hill_tail_index": 4.54318742649615
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017970324405889786,
        "excess_kurtosis": 10.342195078934905,
        "return_acf_1": -0.14288718962510533,
        "abs_return_acf_1": 0.3283605591633025,
        "abs_return_acf_5": 0.3630656672171362,
        "abs_return_acf_20": 0.2726988752369323,
        "quantile_01": -0.049546087910052446,
        "quantile_99": 0.05254454535513722,
        "hill_tail_index": 3.322394040371024
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017323754971516458,
        "excess_kurtosis": 6.8555367188818455,
        "return_acf_1": -0.09092769374066058,
        "abs_return_acf_1": 0.35569752772601426,
        "abs_return_acf_5": 0.31485890387894744,
        "abs_return_acf_20": 0.24323950198600044,
        "quantile_01": -0.0525852736267636,
        "quantile_99": 0.049154609707441704,
        "hill_tail_index": 3.8011643517915874
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016139286256802225,
        "excess_kurtosis": 6.092652599830863,
        "return_acf_1": -0.11966197914693016,
        "abs_return_acf_1": 0.21910443480495514,
        "abs_return_acf_5": 0.21020103764681974,
        "abs_return_acf_20": 0.1831884080941502,
        "quantile_01": -0.04455119169156555,
        "quantile_99": 0.04396782770948927,
        "hill_tail_index": 3.0059646589527405
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019336733829965272,
        "excess_kurtosis": 8.276175434537977,
        "return_acf_1": -0.09949238859153019,
        "abs_return_acf_1": 0.3833328083586864,
        "abs_return_acf_5": 0.3330531347033712,
        "abs_return_acf_20": 0.28716842749142824,
        "quantile_01": -0.06654616868178151,
        "quantile_99": 0.05875539720547609,
        "hill_tail_index": 3.8296965182337157
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01826157858021418,
        "excess_kurtosis": 18.701640426739512,
        "return_acf_1": -0.04210511848458374,
        "abs_return_acf_1": 0.408156018882723,
        "abs_return_acf_5": 0.4425967925382716,
        "abs_return_acf_20": 0.2834425004981797,
        "quantile_01": -0.046547352162077185,
        "quantile_99": 0.04689260536117318,
        "hill_tail_index": 2.6238282599035894
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018778723356766357,
        "excess_kurtosis": 5.092362258986171,
        "return_acf_1": -0.06417715947578016,
        "abs_return_acf_1": 0.34123600033032514,
        "abs_return_acf_5": 0.34524488534630315,
        "abs_return_acf_20": 0.2812321342628039,
        "quantile_01": -0.05800990333550384,
        "quantile_99": 0.052174363659781835,
        "hill_tail_index": 3.1937338865853864
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019289653690712318,
        "excess_kurtosis": 9.006532709074532,
        "return_acf_1": -0.15423132865801287,
        "abs_return_acf_1": 0.32125817792242567,
        "abs_return_acf_5": 0.34763099834443334,
        "abs_return_acf_20": 0.24522764266818142,
        "quantile_01": -0.0510746670002124,
        "quantile_99": 0.05611021234749116,
        "hill_tail_index": 2.568911280400908
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01973750836786351,
        "excess_kurtosis": 6.5149296947406015,
        "return_acf_1": -0.08806044711973114,
        "abs_return_acf_1": 0.2921104933100117,
        "abs_return_acf_5": 0.294076784384317,
        "abs_return_acf_20": 0.23728568595753857,
        "quantile_01": -0.05729601012783308,
        "quantile_99": 0.055754839440446104,
        "hill_tail_index": 3.0591753068461265
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018692864474145306,
        "excess_kurtosis": 10.141674198281002,
        "return_acf_1": -0.07155881931671038,
        "abs_return_acf_1": 0.3288542303970133,
        "abs_return_acf_5": 0.24772720416238164,
        "abs_return_acf_20": 0.2738620309386241,
        "quantile_01": -0.059807523840909926,
        "quantile_99": 0.05234089329464777,
        "hill_tail_index": 3.1899628797561896
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016712858979510595,
        "excess_kurtosis": 3.6057406666063443,
        "return_acf_1": -0.0963426619798057,
        "abs_return_acf_1": 0.26653342303583855,
        "abs_return_acf_5": 0.24480250361838868,
        "abs_return_acf_20": 0.18069989715899143,
        "quantile_01": -0.04821418877512217,
        "quantile_99": 0.04155411205865915,
        "hill_tail_index": 3.7799067762117393
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01832428635354431,
        "excess_kurtosis": 6.9315454750605685,
        "return_acf_1": -0.11969351958840167,
        "abs_return_acf_1": 0.3315305141090263,
        "abs_return_acf_5": 0.3602902005293886,
        "abs_return_acf_20": 0.3002897780111464,
        "quantile_01": -0.05003178852497749,
        "quantile_99": 0.04963166853165094,
        "hill_tail_index": 2.764832036776833
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01907879311739041,
        "excess_kurtosis": 12.191460221159298,
        "return_acf_1": 0.03989750398480602,
        "abs_return_acf_1": 0.4535921331498995,
        "abs_return_acf_5": 0.3166742297139417,
        "abs_return_acf_20": 0.4082577827767058,
        "quantile_01": -0.060984878328469806,
        "quantile_99": 0.06311465846425804,
        "hill_tail_index": 2.4069407033554238
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
Training: False
Coverage status: FAIL
Unseen state share: 0.0
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
