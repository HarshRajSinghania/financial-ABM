# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27141
Run ID: `057a2c2c8c1fb267fa57d7f7002efefdd4a70ca500501c27f0426d47e4f3d658`
Result fingerprint: `b850f97af8a3ce2a63e107864f369eb4f8c81012f9419e95a954a6a140d96ce2`

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
    "equal_weight_sd": -0.7082142857142824,
    "equal_weight_raw": -10.623214285714239,
    "fixed_start_cap_weight_sd": -0.6884403927689768,
    "fixed_start_cap_weight_raw": -10.326605891534651,
    "end_cap_weight_sd": -0.6996408950063686,
    "end_cap_weight_raw": -10.49461342509553
  },
  "full_period_change": {
    "equal_weight_sd": -1.0512380952380904,
    "equal_weight_raw": -15.768571428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9811921296296252,
    "inflation_mean_sd": 0.6757731481481482
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.24416666666666986,
    "equal_weight_raw": 3.662500000000048,
    "fixed_start_cap_weight_sd": 0.26394055961197554,
    "fixed_start_cap_weight_raw": 3.959108394179633,
    "end_cap_weight_sd": 0.2527400573745836,
    "end_cap_weight_raw": 3.791100860618752
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6357142857142822,
      "change_raw": -9.535714285714233,
      "decay_adjusted_gain_sd": 0.3166666666666699
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6804365079365048,
      "change_raw": -10.206547619047571,
      "decay_adjusted_gain_sd": 0.2719444444444476
    },
    "small": {
      "count": 18,
      "change_sd": -0.7341865079365048,
      "change_raw": -11.012797619047571,
      "decay_adjusted_gain_sd": 0.21819444444444766
    },
    "large_minus_small_sd": 0.09847222222222252,
    "large_minus_small_raw": 1.4770833333333377
  },
  "inflation": {
    "initial_mean_sd": 0.3429166666666667,
    "final_mean_sd": 0.6946666666666669,
    "mean_sd": 0.5449400499583681,
    "mean_absolute_raw_gap": 8.17410074937552,
    "final_absolute_raw_gap": 10.42,
    "mean_range_fraction": 0.0817410074937552
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.2459316574621136,
    "final_wealth_share": 0.2224207499882992
  },
  "pricing_slope": {
    "mean": -0.002411851747361079,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.06437723474763499,
    "real_improvement_cost": 0.05299732972538572,
    "washing_cost": 0.011379905022249262,
    "fine_transfer": 0.02762075045079556,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.09199798519843055,
    "resource_cost_fraction_initial_cap": 0.0021459078249211655,
    "private_net_outflow_fraction_initial_cap": 0.003066599506614351,
    "fine_transfer_fraction_initial_cap": 0.0009206916816931851,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010578078739133215,
    "unapplied_final_day_resource_cost": 2.1976530562132857e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 113.78245786285801,
    "beneficial_raw_gain_per_resource_cost": 1706.73686794287,
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
    "accrued_cost": 2.88179318637064,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.09439728981983682,
    "accrued_cost_fraction_initial_cap": 0.0960597728790213,
    "mean_contract_rate": 0.04008407987256197,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "maximum_relative_cash_error": 1.1185355438946614e-15,
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
      "minimum": -0.2917355623121021,
      "maximum": -0.09197000556415862,
      "mean": -0.17274746191471374,
      "median": -0.16177575298651187,
      "quantile_05": -0.2879032801768646,
      "quantile_95": -0.10153338492055458
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
      "minimum": 0.2237898312864275,
      "maximum": 0.8224773678178118,
      "mean": 0.45374834427737265,
      "median": 0.3961917911061661,
      "quantile_05": 0.2612543148785173,
      "quantile_95": 0.7496479361950485
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
        "daily_volatility": 0.01678499433748315,
        "excess_kurtosis": 3.342369981551845,
        "return_acf_1": -0.13305312034135466,
        "abs_return_acf_1": 0.22395092043714432,
        "abs_return_acf_5": 0.2505515363683789,
        "abs_return_acf_20": 0.17107154902435454,
        "quantile_01": -0.04735519910081148,
        "quantile_99": 0.05081815740064275,
        "hill_tail_index": 3.616794592079354
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017104043839588596,
        "excess_kurtosis": 9.368727785346122,
        "return_acf_1": -0.11415372333803789,
        "abs_return_acf_1": 0.2733228593334989,
        "abs_return_acf_5": 0.24045303378367533,
        "abs_return_acf_20": 0.28830929575389985,
        "quantile_01": -0.05004508854583612,
        "quantile_99": 0.048926806117106085,
        "hill_tail_index": 3.0449210042441015
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02210291568889806,
        "excess_kurtosis": 29.148739529461686,
        "return_acf_1": -0.26869600429719515,
        "abs_return_acf_1": 0.5082360449348067,
        "abs_return_acf_5": 0.3947551212547323,
        "abs_return_acf_20": 0.32995300852318044,
        "quantile_01": -0.08214180253044855,
        "quantile_99": 0.05584487284024451,
        "hill_tail_index": 1.9633413414648715
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021654993909240593,
        "excess_kurtosis": 23.041935647738573,
        "return_acf_1": -0.28657394269300157,
        "abs_return_acf_1": 0.430383717891405,
        "abs_return_acf_5": 0.40631735976256633,
        "abs_return_acf_20": 0.32658197344256795,
        "quantile_01": -0.0757922976388971,
        "quantile_99": 0.04968660738565897,
        "hill_tail_index": 2.088093917018149
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021024031899674386,
        "excess_kurtosis": 10.680307399464624,
        "return_acf_1": -0.11603710651182121,
        "abs_return_acf_1": 0.3729092208711999,
        "abs_return_acf_5": 0.4288810928449617,
        "abs_return_acf_20": 0.3276404027360369,
        "quantile_01": -0.0657118090751591,
        "quantile_99": 0.06316254026470147,
        "hill_tail_index": 3.42600995524211
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020101638127707665,
        "excess_kurtosis": 7.1823958163603425,
        "return_acf_1": -0.10945269982256296,
        "abs_return_acf_1": 0.3644998926785425,
        "abs_return_acf_5": 0.3203652593676029,
        "abs_return_acf_20": 0.25601995286451723,
        "quantile_01": -0.05657539783734287,
        "quantile_99": 0.05851627702948299,
        "hill_tail_index": 3.5765545886134342
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02055283925794387,
        "excess_kurtosis": 13.039944190091962,
        "return_acf_1": -0.19701229223286906,
        "abs_return_acf_1": 0.3959652118480994,
        "abs_return_acf_5": 0.261484068086512,
        "abs_return_acf_20": 0.21623448873410228,
        "quantile_01": -0.06364624212251875,
        "quantile_99": 0.05008011208417039,
        "hill_tail_index": 2.4967692403497708
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020234169862824794,
        "excess_kurtosis": 15.945910537774413,
        "return_acf_1": -0.17932858226681853,
        "abs_return_acf_1": 0.41734037792988676,
        "abs_return_acf_5": 0.4114583136639063,
        "abs_return_acf_20": 0.29270273797108953,
        "quantile_01": -0.06541828242763323,
        "quantile_99": 0.047628947233244706,
        "hill_tail_index": 2.147007032834119
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021186523562860275,
        "excess_kurtosis": 16.163331525032984,
        "return_acf_1": -0.11719772721336877,
        "abs_return_acf_1": 0.463060891183893,
        "abs_return_acf_5": 0.3994070162381111,
        "abs_return_acf_20": 0.32502876912488177,
        "quantile_01": -0.07240661395757289,
        "quantile_99": 0.053332247662320975,
        "hill_tail_index": 1.9740567913358515
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.0198948665776328,
        "excess_kurtosis": 26.32318387874783,
        "return_acf_1": -0.23048912723732634,
        "abs_return_acf_1": 0.5216884617106822,
        "abs_return_acf_5": 0.4812435058637331,
        "abs_return_acf_20": 0.3223216870136541,
        "quantile_01": -0.06533791180883793,
        "quantile_99": 0.0509297677548715,
        "hill_tail_index": 2.118875689677038
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01859931865046357,
        "excess_kurtosis": 6.103750662373125,
        "return_acf_1": -0.12033958904928657,
        "abs_return_acf_1": 0.3229492917741125,
        "abs_return_acf_5": 0.32828182811765994,
        "abs_return_acf_20": 0.32318658072834766,
        "quantile_01": -0.055014742341897495,
        "quantile_99": 0.05172321463000781,
        "hill_tail_index": 3.5415226212866346
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01945050636428688,
        "excess_kurtosis": 12.265269967690129,
        "return_acf_1": -0.2917355623121021,
        "abs_return_acf_1": 0.41185594004230314,
        "abs_return_acf_5": 0.47840379975140107,
        "abs_return_acf_20": 0.23735250864481314,
        "quantile_01": -0.067740007784257,
        "quantile_99": 0.056385876721296455,
        "hill_tail_index": 2.850783176271941
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019491517331016135,
        "excess_kurtosis": 6.994112576793473,
        "return_acf_1": -0.1390132626654514,
        "abs_return_acf_1": 0.4553726250876805,
        "abs_return_acf_5": 0.3592383379116398,
        "abs_return_acf_20": 0.2942469884390246,
        "quantile_01": -0.053754721431827815,
        "quantile_99": 0.0598132677649911,
        "hill_tail_index": 2.7537087022928017
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021251042191326064,
        "excess_kurtosis": 20.70435395340393,
        "return_acf_1": -0.20728039211612506,
        "abs_return_acf_1": 0.5021424825592071,
        "abs_return_acf_5": 0.4396184495487186,
        "abs_return_acf_20": 0.3239360693715212,
        "quantile_01": -0.08084734448995848,
        "quantile_99": 0.051772253619255595,
        "hill_tail_index": 1.62884260322854
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.016963036097789402,
        "excess_kurtosis": 4.567639949745647,
        "return_acf_1": -0.16719331331310808,
        "abs_return_acf_1": 0.20719092690763732,
        "abs_return_acf_5": 0.255573286515396,
        "abs_return_acf_20": 0.2263219465004742,
        "quantile_01": -0.04958600668740228,
        "quantile_99": 0.04665422522297434,
        "hill_tail_index": 3.583018881404727
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020401932235366023,
        "excess_kurtosis": 12.43899388784599,
        "return_acf_1": -0.2081768832710578,
        "abs_return_acf_1": 0.48570278803026123,
        "abs_return_acf_5": 0.3711584969099787,
        "abs_return_acf_20": 0.3670271541151544,
        "quantile_01": -0.07631660604969871,
        "quantile_99": 0.05314359914127465,
        "hill_tail_index": 2.5189229996250213
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022350904337548695,
        "excess_kurtosis": 12.622471817964202,
        "return_acf_1": -0.16824072317732688,
        "abs_return_acf_1": 0.481003133390729,
        "abs_return_acf_5": 0.4691525549652796,
        "abs_return_acf_20": 0.41119993898019397,
        "quantile_01": -0.08358865794191445,
        "quantile_99": 0.06698161566288034,
        "hill_tail_index": 2.9097999113754005
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019720254893858292,
        "excess_kurtosis": 4.617466118004809,
        "return_acf_1": -0.14672880555334267,
        "abs_return_acf_1": 0.3267510420350196,
        "abs_return_acf_5": 0.35123145573357406,
        "abs_return_acf_20": 0.31577458362176386,
        "quantile_01": -0.06441695849166246,
        "quantile_99": 0.05553755842093274,
        "hill_tail_index": 4.130904781242895
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02146682969021316,
        "excess_kurtosis": 12.401719633829007,
        "return_acf_1": -0.1163479498502482,
        "abs_return_acf_1": 0.4919075980893602,
        "abs_return_acf_5": 0.4533872043583669,
        "abs_return_acf_20": 0.31394481015698966,
        "quantile_01": -0.06814299057260768,
        "quantile_99": 0.05471040501112401,
        "hill_tail_index": 2.3193568366101243
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01638541369572369,
        "excess_kurtosis": 6.384385753754472,
        "return_acf_1": -0.09707608221435249,
        "abs_return_acf_1": 0.2113363024083942,
        "abs_return_acf_5": 0.15179618543594514,
        "abs_return_acf_20": 0.2551860736371864,
        "quantile_01": -0.044620493342293795,
        "quantile_99": 0.03608244785478973,
        "hill_tail_index": 2.8809505263498334
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021215971016326978,
        "excess_kurtosis": 7.242963721816874,
        "return_acf_1": -0.18538981273031155,
        "abs_return_acf_1": 0.4023629743514432,
        "abs_return_acf_5": 0.35947913104379453,
        "abs_return_acf_20": 0.31590980128906787,
        "quantile_01": -0.07142292420636398,
        "quantile_99": 0.062229277667290146,
        "hill_tail_index": 3.399788130995648
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01746227640238799,
        "excess_kurtosis": 5.351895737623256,
        "return_acf_1": -0.15157269654115588,
        "abs_return_acf_1": 0.3041783285979763,
        "abs_return_acf_5": 0.25678446603541627,
        "abs_return_acf_20": 0.2806565813645351,
        "quantile_01": -0.04843940889947195,
        "quantile_99": 0.046180416444931004,
        "hill_tail_index": 3.1301738221985196
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022086415863998853,
        "excess_kurtosis": 19.620238066551263,
        "return_acf_1": -0.24142982985901518,
        "abs_return_acf_1": 0.5802940914061622,
        "abs_return_acf_5": 0.5504346351211361,
        "abs_return_acf_20": 0.34429219238187037,
        "quantile_01": -0.08400582058301254,
        "quantile_99": 0.05806609864683784,
        "hill_tail_index": 1.7784305589199605
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02017724645169735,
        "excess_kurtosis": 20.40085032179097,
        "return_acf_1": -0.20039528940837917,
        "abs_return_acf_1": 0.4380490793867108,
        "abs_return_acf_5": 0.4176129933039287,
        "abs_return_acf_20": 0.2824416524186572,
        "quantile_01": -0.06098031652830578,
        "quantile_99": 0.04323101027573202,
        "hill_tail_index": 1.6638463985074978
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018776405103501464,
        "excess_kurtosis": 7.4676637394526395,
        "return_acf_1": -0.09197000556415862,
        "abs_return_acf_1": 0.30404888017555753,
        "abs_return_acf_5": 0.2656287179161243,
        "abs_return_acf_20": 0.24963321153039497,
        "quantile_01": -0.05782290424187254,
        "quantile_99": 0.051184888564317084,
        "hill_tail_index": 2.642789387162374
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019835699098279938,
        "excess_kurtosis": 17.143870180338638,
        "return_acf_1": -0.14313308622098178,
        "abs_return_acf_1": 0.36507648057660486,
        "abs_return_acf_5": 0.3839953026120614,
        "abs_return_acf_20": 0.32988693802913366,
        "quantile_01": -0.05908978375554615,
        "quantile_99": 0.047838404769756794,
        "hill_tail_index": 1.9528383165167498
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019391483959910118,
        "excess_kurtosis": 13.372936638150044,
        "return_acf_1": -0.15635819265991568,
        "abs_return_acf_1": 0.44375554632895925,
        "abs_return_acf_5": 0.3772034728169935,
        "abs_return_acf_20": 0.24755434708091553,
        "quantile_01": -0.05435209025109611,
        "quantile_99": 0.0494607707783257,
        "hill_tail_index": 2.46526216209327
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019970478093248638,
        "excess_kurtosis": 9.99890222340323,
        "return_acf_1": -0.2020759357051004,
        "abs_return_acf_1": 0.42982414379939266,
        "abs_return_acf_5": 0.36309257813093393,
        "abs_return_acf_20": 0.3284183958447214,
        "quantile_01": -0.062294461378900746,
        "quantile_99": 0.05655090431548786,
        "hill_tail_index": 3.0282937071678773
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021534425989934512,
        "excess_kurtosis": 18.78090473479629,
        "return_acf_1": -0.288990919936389,
        "abs_return_acf_1": 0.5733985647034351,
        "abs_return_acf_5": 0.4930297836660832,
        "abs_return_acf_20": 0.39968511160586084,
        "quantile_01": -0.08719159310287204,
        "quantile_99": 0.05662641049847528,
        "hill_tail_index": 1.9417047931862805
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017915980395051292,
        "excess_kurtosis": 7.047224848494164,
        "return_acf_1": -0.10698119933924595,
        "abs_return_acf_1": 0.3460251116345285,
        "abs_return_acf_5": 0.3080784612017084,
        "abs_return_acf_20": 0.2567378961919426,
        "quantile_01": -0.051528070680616274,
        "quantile_99": 0.05171357666206087,
        "hill_tail_index": 4.0659368331423735
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
