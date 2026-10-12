# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27068
Run ID: `fccef034de2574d1d33cc9748f5c4ea2f34189b517cfb97239f411f76f534323`
Result fingerprint: `1e8b0a8241828c2655cfbc27d0e55826a8f289d19e0d4c990b423f0b575a3bcf`

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
    "equal_weight_sd": -0.49330158730158413,
    "equal_weight_raw": -7.399523809523763,
    "fixed_start_cap_weight_sd": -0.43849504402456363,
    "fixed_start_cap_weight_raw": -6.577425660368457,
    "end_cap_weight_sd": -0.43669255325450657,
    "end_cap_weight_raw": -6.550388298817597
  },
  "full_period_change": {
    "equal_weight_sd": -0.7957433582566312,
    "equal_weight_raw": -11.936150373849468
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7553037639003708,
    "inflation_mean_sd": 0.6628025793650794
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4248646384831261,
    "equal_weight_raw": 6.37296957724689,
    "fixed_start_cap_weight_sd": 0.47529265269983023,
    "fixed_start_cap_weight_raw": 7.129389790497455,
    "end_cap_weight_sd": 0.4792907370024118,
    "end_cap_weight_raw": 7.189361055036178
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.36988095238094915,
      "change_raw": -5.548214285714237,
      "decay_adjusted_gain_sd": 0.5825000000000032
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5198941798941771,
      "change_raw": -7.7984126984126565,
      "decay_adjusted_gain_sd": 0.31843768383263477
    },
    "small": {
      "count": 18,
      "change_sd": -0.5005753968253936,
      "change_raw": -7.508630952380905,
      "decay_adjusted_gain_sd": 0.45180555555555885
    },
    "large_minus_small_sd": 0.1306944444444445,
    "large_minus_small_raw": 1.9604166666666676
  },
  "inflation": {
    "initial_mean_sd": 0.26233333333333336,
    "final_mean_sd": 0.70075,
    "mean_sd": 0.4857916319733555,
    "mean_absolute_raw_gap": 7.286874479600334,
    "final_absolute_raw_gap": 10.511249999999999,
    "mean_range_fraction": 0.07286874479600333
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.12736601965911404,
    "final_wealth_share": 0.3605938678681779
  },
  "pricing_slope": {
    "mean": -0.002348316184020547,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.06048268146178566,
    "real_improvement_cost": 0.054688954159481024,
    "washing_cost": 0.005793727302304638,
    "fine_transfer": 0.002075782087433396,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06255846354921905,
    "resource_cost_fraction_initial_cap": 0.002016089382059522,
    "private_net_outflow_fraction_initial_cap": 0.002085282118307302,
    "fine_transfer_fraction_initial_cap": 6.919273624777986e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010813094684098223,
    "unapplied_final_day_resource_cost": 0.0005973946581751844
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 210.73700514662133,
    "beneficial_raw_gain_per_resource_cost": 3161.05507719932,
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
    "accrued_cost": 3.3032648849417967,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.3270744087513203,
    "accrued_cost_fraction_initial_cap": 0.11010882949805989,
    "mean_contract_rate": 0.04563682463923558,
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
    "maximum_relative_cash_error": 1.714194852465488e-15,
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
      "minimum": -0.29790277272766474,
      "maximum": -0.16072120248583666,
      "mean": -0.22955378430526843,
      "median": -0.2275474588238045,
      "quantile_05": -0.29278319194950797,
      "quantile_95": -0.18774864403991495
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
      "minimum": 0.55698526734021,
      "maximum": 0.8340416447277871,
      "mean": 0.7056480645981301,
      "median": 0.7117373490072011,
      "quantile_05": 0.5941377205268575,
      "quantile_95": 0.7941659137945508
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
        "daily_volatility": 0.025470001887877645,
        "excess_kurtosis": 7.416033660731472,
        "return_acf_1": -0.2342002987286089,
        "abs_return_acf_1": 0.4366121387136072,
        "abs_return_acf_5": 0.4126854829280674,
        "abs_return_acf_20": 0.3329613049162871,
        "quantile_01": -0.08616255830942865,
        "quantile_99": 0.07357848975375769,
        "hill_tail_index": 3.578446223521415
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02478089038200998,
        "excess_kurtosis": 9.1847902473299,
        "return_acf_1": -0.19550117525035252,
        "abs_return_acf_1": 0.4359216432458564,
        "abs_return_acf_5": 0.3762886646402297,
        "abs_return_acf_20": 0.3052615634003924,
        "quantile_01": -0.08739614784936428,
        "quantile_99": 0.07121507626238885,
        "hill_tail_index": 3.3722588309123758
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022574478933800313,
        "excess_kurtosis": 13.790412018701545,
        "return_acf_1": -0.20116615565487597,
        "abs_return_acf_1": 0.47865174453432685,
        "abs_return_acf_5": 0.40554039358653804,
        "abs_return_acf_20": 0.3205281394189313,
        "quantile_01": -0.07681352577058645,
        "quantile_99": 0.05715385441699931,
        "hill_tail_index": 2.4177671070992477
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022447053778476285,
        "excess_kurtosis": 11.96582931746649,
        "return_acf_1": -0.22729750921524947,
        "abs_return_acf_1": 0.4781545341289159,
        "abs_return_acf_5": 0.4263985194220744,
        "abs_return_acf_20": 0.35002559349672274,
        "quantile_01": -0.0842353937213131,
        "quantile_99": 0.05869504490948377,
        "hill_tail_index": 2.807376802389391
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02544902901484563,
        "excess_kurtosis": 10.525076952387286,
        "return_acf_1": -0.25178856563377194,
        "abs_return_acf_1": 0.48297884239308436,
        "abs_return_acf_5": 0.39898223337428196,
        "abs_return_acf_20": 0.33368262005340776,
        "quantile_01": -0.09035253201253546,
        "quantile_99": 0.06894285502583176,
        "hill_tail_index": 2.8867207446452423
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.024052385917954264,
        "excess_kurtosis": 12.173944098179799,
        "return_acf_1": -0.2503813305049787,
        "abs_return_acf_1": 0.4761778404201755,
        "abs_return_acf_5": 0.41146744766411425,
        "abs_return_acf_20": 0.3893171051207548,
        "quantile_01": -0.08279401132908963,
        "quantile_99": 0.06308367847313281,
        "hill_tail_index": 2.7914115177896988
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023439805740521784,
        "excess_kurtosis": 12.28194768661661,
        "return_acf_1": -0.21950908353917734,
        "abs_return_acf_1": 0.4454276552864143,
        "abs_return_acf_5": 0.4426497690710751,
        "abs_return_acf_20": 0.3260711124949208,
        "quantile_01": -0.08055560078857521,
        "quantile_99": 0.06605803175247173,
        "hill_tail_index": 2.5391217134205126
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.023189544721434488,
        "excess_kurtosis": 7.3054345576302815,
        "return_acf_1": -0.29790277272766474,
        "abs_return_acf_1": 0.4239073944999528,
        "abs_return_acf_5": 0.33914650731125995,
        "abs_return_acf_20": 0.24650362955116273,
        "quantile_01": -0.07994297510354009,
        "quantile_99": 0.06864415923820072,
        "hill_tail_index": 3.655558192300245
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.024882141560241877,
        "excess_kurtosis": 10.768970832147506,
        "return_acf_1": -0.22779740843235957,
        "abs_return_acf_1": 0.46726585503495977,
        "abs_return_acf_5": 0.45160119732036846,
        "abs_return_acf_20": 0.3381629337901386,
        "quantile_01": -0.08185062077833775,
        "quantile_99": 0.07505305235338518,
        "hill_tail_index": 3.141399827604006
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022743547748823423,
        "excess_kurtosis": 11.391368727206048,
        "return_acf_1": -0.2940940527064279,
        "abs_return_acf_1": 0.5333318859898049,
        "abs_return_acf_5": 0.41290895288624485,
        "abs_return_acf_20": 0.3440790273894247,
        "quantile_01": -0.08327122840997597,
        "quantile_99": 0.0707359000408408,
        "hill_tail_index": 2.9592356014773396
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021210248988570244,
        "excess_kurtosis": 7.63596995089425,
        "return_acf_1": -0.18811621239393345,
        "abs_return_acf_1": 0.4259640158350754,
        "abs_return_acf_5": 0.41812177780731913,
        "abs_return_acf_20": 0.3066360325733159,
        "quantile_01": -0.07194662217061686,
        "quantile_99": 0.0625414512885461,
        "hill_tail_index": 3.2352026710471637
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022719110353729217,
        "excess_kurtosis": 16.709431772516123,
        "return_acf_1": -0.20341857552699133,
        "abs_return_acf_1": 0.4890801049512192,
        "abs_return_acf_5": 0.40314677930074305,
        "abs_return_acf_20": 0.2996797088479005,
        "quantile_01": -0.08677363100305255,
        "quantile_99": 0.057972139241229445,
        "hill_tail_index": 2.4265019480231613
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021864669203931684,
        "excess_kurtosis": 10.9509445459572,
        "return_acf_1": -0.2265517744287852,
        "abs_return_acf_1": 0.44715285905463853,
        "abs_return_acf_5": 0.40446940314336616,
        "abs_return_acf_20": 0.308425961391157,
        "quantile_01": -0.07225694816010104,
        "quantile_99": 0.062112694475664386,
        "hill_tail_index": 2.936060990182201
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02194089559007488,
        "excess_kurtosis": 6.674291194292831,
        "return_acf_1": -0.16072120248583666,
        "abs_return_acf_1": 0.46909332826425737,
        "abs_return_acf_5": 0.37111782463387827,
        "abs_return_acf_20": 0.3415539283576002,
        "quantile_01": -0.07986777580415484,
        "quantile_99": 0.06928374540534747,
        "hill_tail_index": 4.557043225874896
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.025323992719207863,
        "excess_kurtosis": 8.691304319954275,
        "return_acf_1": -0.2435187015881447,
        "abs_return_acf_1": 0.4443775141619367,
        "abs_return_acf_5": 0.37094409571709486,
        "abs_return_acf_20": 0.3167633369518438,
        "quantile_01": -0.08501883694743706,
        "quantile_99": 0.08539573481252465,
        "hill_tail_index": 2.672193677134038
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020612839130887472,
        "excess_kurtosis": 7.870230883319053,
        "return_acf_1": -0.20297370163148432,
        "abs_return_acf_1": 0.40528913154820784,
        "abs_return_acf_5": 0.3390305353739776,
        "abs_return_acf_20": 0.35765685299336025,
        "quantile_01": -0.06823152489840803,
        "quantile_99": 0.05508370163231022,
        "hill_tail_index": 2.92571394722312
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02419394493654369,
        "excess_kurtosis": 7.7873903567066645,
        "return_acf_1": -0.27133985698368257,
        "abs_return_acf_1": 0.4721597317973973,
        "abs_return_acf_5": 0.41529992429373086,
        "abs_return_acf_20": 0.3455189823302641,
        "quantile_01": -0.08393634895677177,
        "quantile_99": 0.06830887792897263,
        "hill_tail_index": 3.019408788176742
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02209557979071752,
        "excess_kurtosis": 8.50598912271061,
        "return_acf_1": -0.2137294187755962,
        "abs_return_acf_1": 0.4724169554928694,
        "abs_return_acf_5": 0.3928142219402652,
        "abs_return_acf_20": 0.37952219826661304,
        "quantile_01": -0.07706947339606729,
        "quantile_99": 0.060958460555090126,
        "hill_tail_index": 2.5588023624317606
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023520718020718527,
        "excess_kurtosis": 7.390899085900127,
        "return_acf_1": -0.2911810288021614,
        "abs_return_acf_1": 0.48859347528266556,
        "abs_return_acf_5": 0.37921070480017915,
        "abs_return_acf_20": 0.3160310320923267,
        "quantile_01": -0.08339256509512029,
        "quantile_99": 0.06763021758539131,
        "hill_tail_index": 4.922309510778891
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.023620777750836656,
        "excess_kurtosis": 13.39098086579859,
        "return_acf_1": -0.187447906295718,
        "abs_return_acf_1": 0.43910118310367,
        "abs_return_acf_5": 0.3854339901576932,
        "abs_return_acf_20": 0.36534898580959146,
        "quantile_01": -0.08464887041888595,
        "quantile_99": 0.06569062271681583,
        "hill_tail_index": 2.610406389917792
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02283515263967518,
        "excess_kurtosis": 11.96497240533309,
        "return_acf_1": -0.24996690249673273,
        "abs_return_acf_1": 0.47621853251471363,
        "abs_return_acf_5": 0.4095928728080043,
        "abs_return_acf_20": 0.32535579308178697,
        "quantile_01": -0.06615788315128318,
        "quantile_99": 0.06475204800408357,
        "hill_tail_index": 2.733228064782568
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.024629062159184516,
        "excess_kurtosis": 13.007051098656184,
        "return_acf_1": -0.2455253868782428,
        "abs_return_acf_1": 0.4735458877346817,
        "abs_return_acf_5": 0.4049228736549531,
        "abs_return_acf_20": 0.3539764507388836,
        "quantile_01": -0.07720213345762189,
        "quantile_99": 0.0640151941769061,
        "hill_tail_index": 2.8005318509287527
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.022511291878851585,
        "excess_kurtosis": 14.207178891492223,
        "return_acf_1": -0.2309577191341645,
        "abs_return_acf_1": 0.4181363811651221,
        "abs_return_acf_5": 0.4027394209498234,
        "abs_return_acf_20": 0.3510576638882042,
        "quantile_01": -0.08522391130680118,
        "quantile_99": 0.05593810531840918,
        "hill_tail_index": 2.533816691574061
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02103825099146169,
        "excess_kurtosis": 10.553910544106538,
        "return_acf_1": -0.22963683253468076,
        "abs_return_acf_1": 0.41613438499989985,
        "abs_return_acf_5": 0.4036304920284655,
        "abs_return_acf_20": 0.3180381469131235,
        "quantile_01": -0.07654441638093075,
        "quantile_99": 0.05745506223800567,
        "hill_tail_index": 2.8253255558141643
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.025166427416134306,
        "excess_kurtosis": 9.491198952144682,
        "return_acf_1": -0.20614810286909835,
        "abs_return_acf_1": 0.40409403684179585,
        "abs_return_acf_5": 0.38198446475782266,
        "abs_return_acf_20": 0.3131598003711672,
        "quantile_01": -0.08393921328240367,
        "quantile_99": 0.071128899165062,
        "hill_tail_index": 2.9285887785731934
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.022090567017315554,
        "excess_kurtosis": 11.426405733988085,
        "return_acf_1": -0.24037297411269629,
        "abs_return_acf_1": 0.3996539255846599,
        "abs_return_acf_5": 0.38156073839569693,
        "abs_return_acf_20": 0.35487323176461066,
        "quantile_01": -0.07329845502489227,
        "quantile_99": 0.05940431185643695,
        "hill_tail_index": 2.7468797327525976
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022271105761221557,
        "excess_kurtosis": 16.203870479036475,
        "return_acf_1": -0.21781246739844617,
        "abs_return_acf_1": 0.4129329389790197,
        "abs_return_acf_5": 0.38289106770663095,
        "abs_return_acf_20": 0.36012846887358974,
        "quantile_01": -0.07324828208279957,
        "quantile_99": 0.06570789437092994,
        "hill_tail_index": 2.0686568474246734
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02545295971324451,
        "excess_kurtosis": 10.218978320176323,
        "return_acf_1": -0.22923725297401432,
        "abs_return_acf_1": 0.4032075646120745,
        "abs_return_acf_5": 0.3880096417708136,
        "abs_return_acf_20": 0.32220794980743006,
        "quantile_01": -0.08557303762761398,
        "quantile_99": 0.06740015921646779,
        "hill_tail_index": 3.462616810336554
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0232941911589561,
        "excess_kurtosis": 7.0382390720290395,
        "return_acf_1": -0.22601736572050002,
        "abs_return_acf_1": 0.406213294911535,
        "abs_return_acf_5": 0.33714862041077986,
        "abs_return_acf_20": 0.34642665482399043,
        "quantile_01": -0.0821098022283232,
        "quantile_99": 0.06017727444797239,
        "hill_tail_index": 3.797096620587619
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02345762419606321,
        "excess_kurtosis": 13.301377573573504,
        "return_acf_1": -0.22230179373367617,
        "abs_return_acf_1": 0.4674531737603403,
        "abs_return_acf_5": 0.40717533319100624,
        "abs_return_acf_20": 0.40874167763831,
        "quantile_01": -0.0818919729954428,
        "quantile_99": 0.06124535140087743,
        "hill_tail_index": 2.7011684930076525
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
