# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27215
Run ID: `62c8261157bdbf6a06a53c5923dcfb101d64a7e5cc7ccabef1a32e362f07181a`
Result fingerprint: `135392366cfd1e306a83f919fbd84cba8b929d49c9db1ab2b952b1dd48e497dc`

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
    "equal_weight_sd": -0.8127142857142825,
    "equal_weight_raw": -12.19071428571424,
    "fixed_start_cap_weight_sd": -0.7932598741104249,
    "fixed_start_cap_weight_raw": -11.898898111656374,
    "end_cap_weight_sd": -0.77301747000709,
    "end_cap_weight_raw": -11.595262050106351
  },
  "full_period_change": {
    "equal_weight_sd": -1.2525714285714238,
    "equal_weight_raw": -18.788571428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1869993386243338,
    "inflation_mean_sd": 0.5307615740740741
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.13966666666666988,
    "equal_weight_raw": 2.095000000000048,
    "fixed_start_cap_weight_sd": 0.15912107827052746,
    "fixed_start_cap_weight_raw": 2.386816174057912,
    "end_cap_weight_sd": 0.1793634823738623,
    "end_cap_weight_raw": 2.6904522356079337
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7432142857142825,
      "change_raw": -11.148214285714237,
      "decay_adjusted_gain_sd": 0.20916666666666991
    },
    "mid": {
      "count": 9,
      "change_sd": -0.748769841269838,
      "change_raw": -11.231547619047571,
      "decay_adjusted_gain_sd": 0.20361111111111438
    },
    "small": {
      "count": 18,
      "change_sd": -0.8562698412698381,
      "change_raw": -12.84404761904757,
      "decay_adjusted_gain_sd": 0.0961111111111143
    },
    "large_minus_small_sd": 0.11305555555555558,
    "large_minus_small_raw": 1.6958333333333337
  },
  "inflation": {
    "initial_mean_sd": 0.29566666666666663,
    "final_mean_sd": 0.5309166666666667,
    "mean_sd": 0.44056695809048013,
    "mean_absolute_raw_gap": 6.608504371357203,
    "final_absolute_raw_gap": 7.9637499999999966,
    "mean_range_fraction": 0.06608504371357203
  },
  "impact": {
    "initial_share": 0.18666666666666668,
    "final_share": 0.32,
    "initial_wealth_share": 0.18138774023048226,
    "final_wealth_share": 0.3276089245801474
  },
  "pricing_slope": {
    "mean": -0.0008196628001927188,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.02974767086244394,
    "real_improvement_cost": 0.015969142071841372,
    "washing_cost": 0.013778528790602571,
    "fine_transfer": 0.008753048006127445,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.038500718868571385,
    "resource_cost_fraction_initial_cap": 0.0009915890287481312,
    "private_net_outflow_fraction_initial_cap": 0.001283357295619046,
    "fine_transfer_fraction_initial_cap": 0.00029176826687091483,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005525228972473722,
    "unapplied_final_day_resource_cost": 0.0006302640962368241
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 140.8513634353108,
    "beneficial_raw_gain_per_resource_cost": 2112.770451529662,
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
    "accrued_cost": 3.095854293660807,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.11966381747033057,
    "accrued_cost_fraction_initial_cap": 0.10319514312202688,
    "mean_contract_rate": 0.042750103461116754,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "maximum_relative_cash_error": 2.9480217050488686e-15,
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
      "minimum": -0.22507982767677287,
      "maximum": -0.0925833321808837,
      "mean": -0.1496682337656251,
      "median": -0.1519910149245704,
      "quantile_05": -0.1908931466364831,
      "quantile_95": -0.10505882594113747
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
      "minimum": 0.32165581229019846,
      "maximum": 0.8250868972855662,
      "mean": 0.5777366967349148,
      "median": 0.5546073461612145,
      "quantile_05": 0.4088772917860235,
      "quantile_95": 0.7846542551271884
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
        "daily_volatility": 0.02016882664670872,
        "excess_kurtosis": 7.985208054435613,
        "return_acf_1": -0.1535351824851574,
        "abs_return_acf_1": 0.35135218167590265,
        "abs_return_acf_5": 0.38374734130070176,
        "abs_return_acf_20": 0.21445115897804493,
        "quantile_01": -0.06054853249783806,
        "quantile_99": 0.048147361402087384,
        "hill_tail_index": 3.6995005612970555
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02255211358686694,
        "excess_kurtosis": 14.073813464287106,
        "return_acf_1": -0.22507982767677287,
        "abs_return_acf_1": 0.5372874535440213,
        "abs_return_acf_5": 0.4941041600463936,
        "abs_return_acf_20": 0.3235018447163916,
        "quantile_01": -0.07415644266690041,
        "quantile_99": 0.06577367081301179,
        "hill_tail_index": 2.6494835767650806
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022506265844783387,
        "excess_kurtosis": 11.7410471398075,
        "return_acf_1": -0.1194811117574829,
        "abs_return_acf_1": 0.4395423981255617,
        "abs_return_acf_5": 0.48998474469843734,
        "abs_return_acf_20": 0.26751139344099945,
        "quantile_01": -0.07831163321349517,
        "quantile_99": 0.06286919051011322,
        "hill_tail_index": 3.465500074764547
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01694176017004089,
        "excess_kurtosis": 4.343666850801345,
        "return_acf_1": -0.146047085622309,
        "abs_return_acf_1": 0.26604004341460175,
        "abs_return_acf_5": 0.24581161998821138,
        "abs_return_acf_20": 0.21718660675879897,
        "quantile_01": -0.04744941572870691,
        "quantile_99": 0.044481006455360766,
        "hill_tail_index": 3.4897606728853034
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01941890995558795,
        "excess_kurtosis": 7.299134462986583,
        "return_acf_1": -0.16394067327389128,
        "abs_return_acf_1": 0.3597121007531107,
        "abs_return_acf_5": 0.26751686142093833,
        "abs_return_acf_20": 0.21653712089183139,
        "quantile_01": -0.06130289641036462,
        "quantile_99": 0.05725414841665619,
        "hill_tail_index": 2.993441344168344
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022686159022423043,
        "excess_kurtosis": 17.341188188007294,
        "return_acf_1": -0.19657799217157457,
        "abs_return_acf_1": 0.4029485330422772,
        "abs_return_acf_5": 0.43523590044794663,
        "abs_return_acf_20": 0.23742627383066445,
        "quantile_01": -0.08423123336890945,
        "quantile_99": 0.05399955236944898,
        "hill_tail_index": 1.8263721643989077
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023169792408009798,
        "excess_kurtosis": 16.024799963786148,
        "return_acf_1": -0.16790482755366665,
        "abs_return_acf_1": 0.44463770389041857,
        "abs_return_acf_5": 0.4718473603648272,
        "abs_return_acf_20": 0.2424004310245655,
        "quantile_01": -0.08202498893014626,
        "quantile_99": 0.05191398846647537,
        "hill_tail_index": 2.3608629403102492
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020500617474570527,
        "excess_kurtosis": 5.172674379615307,
        "return_acf_1": -0.13962110373726483,
        "abs_return_acf_1": 0.3603159084296476,
        "abs_return_acf_5": 0.3342061429722258,
        "abs_return_acf_20": 0.2734485280049535,
        "quantile_01": -0.07172655557383502,
        "quantile_99": 0.05028247604832913,
        "hill_tail_index": 3.8363886301606094
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016341922664879563,
        "excess_kurtosis": 1.5468110748268717,
        "return_acf_1": -0.1254752224881372,
        "abs_return_acf_1": 0.21675274304822859,
        "abs_return_acf_5": 0.2107814406253677,
        "abs_return_acf_20": 0.14335828903676426,
        "quantile_01": -0.04502067023667771,
        "quantile_99": 0.04596788265636488,
        "hill_tail_index": 6.761242324865112
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01799550422517826,
        "excess_kurtosis": 2.945562813225788,
        "return_acf_1": -0.16834044871942597,
        "abs_return_acf_1": 0.321375108094712,
        "abs_return_acf_5": 0.2808738591587731,
        "abs_return_acf_20": 0.1751829456332725,
        "quantile_01": -0.053191995891854624,
        "quantile_99": 0.04762378272304553,
        "hill_tail_index": 4.280568283954962
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020775089611729875,
        "excess_kurtosis": 10.48610315346719,
        "return_acf_1": -0.10031662255133784,
        "abs_return_acf_1": 0.3825368414489995,
        "abs_return_acf_5": 0.3532125423084389,
        "abs_return_acf_20": 0.22987387289378172,
        "quantile_01": -0.05405750357512124,
        "quantile_99": 0.04990800815861992,
        "hill_tail_index": 2.6857826314339497
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02323738286910557,
        "excess_kurtosis": 19.78625357391075,
        "return_acf_1": -0.12342256513337901,
        "abs_return_acf_1": 0.4030577710799271,
        "abs_return_acf_5": 0.530679083021208,
        "abs_return_acf_20": 0.2995662010459848,
        "quantile_01": -0.08392089941487049,
        "quantile_99": 0.061726240764315,
        "hill_tail_index": 2.5542993572339214
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02321170102604499,
        "excess_kurtosis": 16.782819820710415,
        "return_acf_1": -0.12596217766958626,
        "abs_return_acf_1": 0.3654082589069361,
        "abs_return_acf_5": 0.444685234171965,
        "abs_return_acf_20": 0.21604207193876082,
        "quantile_01": -0.0804080501812052,
        "quantile_99": 0.06855939996314026,
        "hill_tail_index": 2.229031253901996
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.020277016746362942,
        "excess_kurtosis": 5.195354505338102,
        "return_acf_1": -0.1540267373729909,
        "abs_return_acf_1": 0.40246794968776023,
        "abs_return_acf_5": 0.36838618114314087,
        "abs_return_acf_20": 0.2617087664993772,
        "quantile_01": -0.06982312075352234,
        "quantile_99": 0.06414259344078878,
        "hill_tail_index": 4.012543369567011
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0215474307828503,
        "excess_kurtosis": 12.162345625426784,
        "return_acf_1": -0.11085485230644805,
        "abs_return_acf_1": 0.33458849159327836,
        "abs_return_acf_5": 0.34305119532226286,
        "abs_return_acf_20": 0.23174119903350587,
        "quantile_01": -0.0665446866505036,
        "quantile_99": 0.05963397212431319,
        "hill_tail_index": 2.3440808504699926
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023720086129808176,
        "excess_kurtosis": 16.942947937992983,
        "return_acf_1": -0.16991473585064432,
        "abs_return_acf_1": 0.410008895814662,
        "abs_return_acf_5": 0.4297915656595259,
        "abs_return_acf_20": 0.268572896269772,
        "quantile_01": -0.08413439671752246,
        "quantile_99": 0.06694951756918323,
        "hill_tail_index": 2.6964827181359445
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023094839088224337,
        "excess_kurtosis": 8.50574599663204,
        "return_acf_1": -0.12949160546282149,
        "abs_return_acf_1": 0.38943390959212354,
        "abs_return_acf_5": 0.43912410888156844,
        "abs_return_acf_20": 0.2361047595313385,
        "quantile_01": -0.07696456479532106,
        "quantile_99": 0.07079995278866313,
        "hill_tail_index": 3.0654477039307966
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021515835906064422,
        "excess_kurtosis": 9.354026462095606,
        "return_acf_1": -0.17751459466891445,
        "abs_return_acf_1": 0.3541476641005765,
        "abs_return_acf_5": 0.38340266404599,
        "abs_return_acf_20": 0.3038364001440407,
        "quantile_01": -0.07251905038057443,
        "quantile_99": 0.05551262782399612,
        "hill_tail_index": 2.81339478147454
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017635142624850296,
        "excess_kurtosis": 6.854547662790372,
        "return_acf_1": -0.1720208779041068,
        "abs_return_acf_1": 0.32134189110395023,
        "abs_return_acf_5": 0.32293640593538037,
        "abs_return_acf_20": 0.32312809656024677,
        "quantile_01": -0.04994625564801435,
        "quantile_99": 0.045532820668564726,
        "hill_tail_index": 2.9198773820433988
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022999277788395122,
        "excess_kurtosis": 14.619959679473943,
        "return_acf_1": -0.1836266559194735,
        "abs_return_acf_1": 0.37352528041080546,
        "abs_return_acf_5": 0.47122863168765267,
        "abs_return_acf_20": 0.28210586023399403,
        "quantile_01": -0.07537730101569641,
        "quantile_99": 0.06572455620458913,
        "hill_tail_index": 2.6477817353652258
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.023449409364640125,
        "excess_kurtosis": 10.193710996938167,
        "return_acf_1": -0.12526748238412108,
        "abs_return_acf_1": 0.4038068257355266,
        "abs_return_acf_5": 0.4029015476299732,
        "abs_return_acf_20": 0.26565129698095213,
        "quantile_01": -0.07643670875143761,
        "quantile_99": 0.07167320795886903,
        "hill_tail_index": 3.1915916916049127
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01775607084676731,
        "excess_kurtosis": 4.896207938526559,
        "return_acf_1": -0.14685642361422827,
        "abs_return_acf_1": 0.301712742595773,
        "abs_return_acf_5": 0.34870820682814785,
        "abs_return_acf_20": 0.20613201801780742,
        "quantile_01": -0.05582115755954875,
        "quantile_99": 0.04932912826687297,
        "hill_tail_index": 3.4870244596618307
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02107700088605022,
        "excess_kurtosis": 11.144949581424768,
        "return_acf_1": -0.18394500209359352,
        "abs_return_acf_1": 0.3954928833347447,
        "abs_return_acf_5": 0.39760386542022624,
        "abs_return_acf_20": 0.23781485949122017,
        "quantile_01": -0.06498862232656692,
        "quantile_99": 0.056786248748213766,
        "hill_tail_index": 2.505532421036214
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02306814479034574,
        "excess_kurtosis": 7.446360469596634,
        "return_acf_1": -0.12210880889123243,
        "abs_return_acf_1": 0.3823124737611773,
        "abs_return_acf_5": 0.3688406525672135,
        "abs_return_acf_20": 0.27612230863072174,
        "quantile_01": -0.07686579220266222,
        "quantile_99": 0.06471796634303675,
        "hill_tail_index": 3.893460090144393
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018953945884407793,
        "excess_kurtosis": 8.110323258809252,
        "return_acf_1": -0.15131802486696816,
        "abs_return_acf_1": 0.4098348519051088,
        "abs_return_acf_5": 0.3995452632394336,
        "abs_return_acf_20": 0.24564361743112983,
        "quantile_01": -0.0556834769291525,
        "quantile_99": 0.0534338661552231,
        "hill_tail_index": 3.1165910701877433
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019044826170605992,
        "excess_kurtosis": 5.21301155895206,
        "return_acf_1": -0.16872566378321727,
        "abs_return_acf_1": 0.2725164935311621,
        "abs_return_acf_5": 0.26051145301813294,
        "abs_return_acf_20": 0.19918687701428317,
        "quantile_01": -0.054318798752683584,
        "quantile_99": 0.05173893910436034,
        "hill_tail_index": 3.1722910512551086
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02283764971223457,
        "excess_kurtosis": 14.833990467636905,
        "return_acf_1": -0.1555866564950378,
        "abs_return_acf_1": 0.43024224327262817,
        "abs_return_acf_5": 0.4541640990285408,
        "abs_return_acf_20": 0.2684200159525735,
        "quantile_01": -0.07749652657500301,
        "quantile_99": 0.05896704117153425,
        "hill_tail_index": 2.5455215166234657
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02021116569730997,
        "excess_kurtosis": 8.912129724207583,
        "return_acf_1": -0.1378367133519124,
        "abs_return_acf_1": 0.3777093166215139,
        "abs_return_acf_5": 0.37610563021448384,
        "abs_return_acf_20": 0.22759324101638792,
        "quantile_01": -0.06740319441101539,
        "quantile_99": 0.0578020572918184,
        "hill_tail_index": 2.9389222523028438
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018537342638355995,
        "excess_kurtosis": 6.906839385432024,
        "return_acf_1": -0.0925833321808837,
        "abs_return_acf_1": 0.32145697987595956,
        "abs_return_acf_5": 0.265075549278016,
        "abs_return_acf_20": 0.21529002985177295,
        "quantile_01": -0.05527074312617073,
        "quantile_99": 0.05723257461294743,
        "hill_tail_index": 3.7053189222137632
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019343816827653796,
        "excess_kurtosis": 2.9016734391731385,
        "return_acf_1": -0.15266400498217267,
        "abs_return_acf_1": 0.369043943323447,
        "abs_return_acf_5": 0.29672673643507413,
        "abs_return_acf_20": 0.224371171357487,
        "quantile_01": -0.055342631645524824,
        "quantile_99": 0.05584869824789456,
        "hill_tail_index": 4.88503565121232
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
