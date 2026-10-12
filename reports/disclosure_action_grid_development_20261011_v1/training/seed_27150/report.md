# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27150
Run ID: `72693f025e2e60bf6df2c549efdd7716a1ed70b8427f484752a7e5d1d5b1148e`
Result fingerprint: `7b108484c00c63500a9a83b80133cea62068f1cd0d2fc7c2c0014db908c419d2`

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
    "equal_weight_sd": -0.7271309523809494,
    "equal_weight_raw": -10.906964285714233,
    "fixed_start_cap_weight_sd": -0.7113269666644866,
    "fixed_start_cap_weight_raw": -10.669904499967299,
    "end_cap_weight_sd": -0.7178066694344055,
    "end_cap_weight_raw": -10.767100041516088
  },
  "full_period_change": {
    "equal_weight_sd": -1.0544880952380902,
    "equal_weight_raw": -15.817321428571352
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9786263227513183,
    "inflation_mean_sd": 0.7082308201058201
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2252500000000032,
    "equal_weight_raw": 3.378750000000048,
    "fixed_start_cap_weight_sd": 0.2410539857164656,
    "fixed_start_cap_weight_raw": 3.6158097857469835,
    "end_cap_weight_sd": 0.23457428294654661,
    "end_cap_weight_raw": 3.518614244198199
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5840476190476158,
      "change_raw": -8.760714285714236,
      "decay_adjusted_gain_sd": 0.36833333333333657
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7218253968253936,
      "change_raw": -10.827380952380905,
      "decay_adjusted_gain_sd": 0.2305555555555588
    },
    "small": {
      "count": 18,
      "change_sd": -0.7536309523809491,
      "change_raw": -11.304464285714237,
      "decay_adjusted_gain_sd": 0.1987500000000032
    },
    "large_minus_small_sd": 0.1695833333333333,
    "large_minus_small_raw": 2.5437499999999997
  },
  "inflation": {
    "initial_mean_sd": 0.34349999999999997,
    "final_mean_sd": 0.7450833333333335,
    "mean_sd": 0.5411740910352485,
    "mean_absolute_raw_gap": 8.117611365528726,
    "final_absolute_raw_gap": 11.176250000000001,
    "mean_range_fraction": 0.08117611365528726
  },
  "impact": {
    "initial_share": 0.44666666666666666,
    "final_share": 0.5466666666666666,
    "initial_wealth_share": 0.4522928819718226,
    "final_wealth_share": 0.531603959548846
  },
  "pricing_slope": {
    "mean": -0.0032512169963524106,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999993,
    "resource_cost": 0.035578699394767904,
    "real_improvement_cost": 0.02406861630789033,
    "washing_cost": 0.011510083086877574,
    "fine_transfer": 0.029588728138706957,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06516742753347486,
    "resource_cost_fraction_initial_cap": 0.0011859566464922637,
    "private_net_outflow_fraction_initial_cap": 0.0021722475844491627,
    "fine_transfer_fraction_initial_cap": 0.000986290937956899,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0043960205913290695,
    "unapplied_final_day_resource_cost": 0.0008741748203179889
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 189.93105748530633,
    "beneficial_raw_gain_per_resource_cost": 2848.965862279595,
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
    "accrued_cost": 3.051881768224287,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.07569129203381113,
    "accrued_cost_fraction_initial_cap": 0.10172939227414293,
    "mean_contract_rate": 0.04171208514163772,
    "maximum_ledger_error": 4.0657581468206416e-20
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 22,
    "maximum_relative_cash_error": 1.5217618802167912e-15,
    "maximum_absolute_share_error": 2.886579864025407e-15,
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
      "minimum": -0.319752144672557,
      "maximum": -0.1256464942605941,
      "mean": -0.22695133122403932,
      "median": -0.22253821966405507,
      "quantile_05": -0.2912914372488227,
      "quantile_95": -0.15778652460040724
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
      "minimum": -0.18938495668715977,
      "maximum": 0.884287028909487,
      "mean": 0.7517118230471994,
      "median": 0.8289278472116546,
      "quantile_05": -0.08057639540793052,
      "quantile_95": 0.8741735544547343
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
        "daily_volatility": 0.02786145436929704,
        "excess_kurtosis": 25.739856566900848,
        "return_acf_1": -0.20980758270678743,
        "abs_return_acf_1": 0.5237068754492618,
        "abs_return_acf_5": 0.4799001240759906,
        "abs_return_acf_20": 0.45220784277744314,
        "quantile_01": -0.09849986589521835,
        "quantile_99": 0.07306382067756048,
        "hill_tail_index": 2.0264383707329925
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.026294364788044935,
        "excess_kurtosis": 26.48269140482097,
        "return_acf_1": -0.24023042873197015,
        "abs_return_acf_1": 0.5778447518473403,
        "abs_return_acf_5": 0.35690783245951785,
        "abs_return_acf_20": 0.34611659439658027,
        "quantile_01": -0.08831478686275847,
        "quantile_99": 0.06098089152855943,
        "hill_tail_index": 2.3900987511344947
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02751920143465738,
        "excess_kurtosis": 20.14410325952362,
        "return_acf_1": -0.16431852227253507,
        "abs_return_acf_1": 0.5956727533677427,
        "abs_return_acf_5": 0.4708325510637064,
        "abs_return_acf_20": 0.4014554222808588,
        "quantile_01": -0.10265057294039977,
        "quantile_99": 0.07690554476628395,
        "hill_tail_index": 1.9939789762929911
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.026707176900052233,
        "excess_kurtosis": 19.61744417006068,
        "return_acf_1": -0.2202177562053371,
        "abs_return_acf_1": 0.5555046780725834,
        "abs_return_acf_5": 0.44928597666766035,
        "abs_return_acf_20": 0.3878316748385518,
        "quantile_01": -0.09925454831005634,
        "quantile_99": 0.06247759441965971,
        "hill_tail_index": 2.5166024726091587
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.028441496664378323,
        "excess_kurtosis": 27.25229270396935,
        "return_acf_1": -0.26728837940049627,
        "abs_return_acf_1": 0.5817791565202037,
        "abs_return_acf_5": 0.37585874761354165,
        "abs_return_acf_20": 0.34726307773134013,
        "quantile_01": -0.09608810732156262,
        "quantile_99": 0.07601178940334435,
        "hill_tail_index": 2.238560482156295
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.027187713742464613,
        "excess_kurtosis": 33.308322564560456,
        "return_acf_1": -0.18127109607721947,
        "abs_return_acf_1": 0.5809143663122817,
        "abs_return_acf_5": 0.424643830943868,
        "abs_return_acf_20": 0.32399212513365716,
        "quantile_01": -0.098322864433455,
        "quantile_99": 0.07246620461929693,
        "hill_tail_index": 2.1072174689102305
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.026288276545224067,
        "excess_kurtosis": 28.984784721364466,
        "return_acf_1": -0.2797813369262244,
        "abs_return_acf_1": 0.5741760692059603,
        "abs_return_acf_5": 0.4169997233012076,
        "abs_return_acf_20": 0.397712078160132,
        "quantile_01": -0.08497857798357998,
        "quantile_99": 0.0730519556447139,
        "hill_tail_index": 2.3654535834147157
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.025669094148285984,
        "excess_kurtosis": 20.066329426898488,
        "return_acf_1": -0.15629271706821532,
        "abs_return_acf_1": 0.5450296593172551,
        "abs_return_acf_5": 0.42489468707825245,
        "abs_return_acf_20": 0.3899516119742295,
        "quantile_01": -0.0942091772988496,
        "quantile_99": 0.07050614690343349,
        "hill_tail_index": 2.5508002701350017
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.027109674202061052,
        "excess_kurtosis": 19.693625628638014,
        "return_acf_1": -0.26753159846185826,
        "abs_return_acf_1": 0.5229236229216316,
        "abs_return_acf_5": 0.44356496005490514,
        "abs_return_acf_20": 0.43495527915109083,
        "quantile_01": -0.09972753630648816,
        "quantile_99": 0.07017591140823648,
        "hill_tail_index": 2.349524455923654
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02825813911174151,
        "excess_kurtosis": 24.42698099762658,
        "return_acf_1": -0.2740531267981175,
        "abs_return_acf_1": 0.5976162790723143,
        "abs_return_acf_5": 0.47020767726053575,
        "abs_return_acf_20": 0.38136265121611745,
        "quantile_01": -0.09980678745031084,
        "quantile_99": 0.06602283496879849,
        "hill_tail_index": 2.042398642182132
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.029359961194372917,
        "excess_kurtosis": 21.64546826679847,
        "return_acf_1": -0.1256464942605941,
        "abs_return_acf_1": 0.574846250686522,
        "abs_return_acf_5": 0.4144212561864252,
        "abs_return_acf_20": 0.3746951008336025,
        "quantile_01": -0.12169409695715708,
        "quantile_99": 0.09210862894574198,
        "hill_tail_index": 2.3942055856486495
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02687384240957957,
        "excess_kurtosis": 25.549667264490992,
        "return_acf_1": -0.21956915655114015,
        "abs_return_acf_1": 0.5699694432388682,
        "abs_return_acf_5": 0.43392434641891864,
        "abs_return_acf_20": 0.3855924537479543,
        "quantile_01": -0.09656641642005574,
        "quantile_99": 0.06515580386095463,
        "hill_tail_index": 1.9168595240084696
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.026640108711080985,
        "excess_kurtosis": 17.68151999817563,
        "return_acf_1": -0.21692876534653777,
        "abs_return_acf_1": 0.5087331877305352,
        "abs_return_acf_5": 0.39329175425128066,
        "abs_return_acf_20": 0.3689316372042279,
        "quantile_01": -0.08673757716335193,
        "quantile_99": 0.06893399835521853,
        "hill_tail_index": 2.449237737357661
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.027558142458664912,
        "excess_kurtosis": 22.253313245651633,
        "return_acf_1": -0.20180790512350003,
        "abs_return_acf_1": 0.5658850243310942,
        "abs_return_acf_5": 0.48256995081546605,
        "abs_return_acf_20": 0.4174822047407034,
        "quantile_01": -0.09756670078828919,
        "quantile_99": 0.07933079629184617,
        "hill_tail_index": 2.4441018308223983
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.027210961501387017,
        "excess_kurtosis": 22.88015174007932,
        "return_acf_1": -0.24138737194819354,
        "abs_return_acf_1": 0.5947592389447424,
        "abs_return_acf_5": 0.48823214127559045,
        "abs_return_acf_20": 0.44446782869276735,
        "quantile_01": -0.10915447920487853,
        "quantile_99": 0.07046712527829924,
        "hill_tail_index": 2.3442409609837007
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.028458782478106782,
        "excess_kurtosis": 21.584576482553615,
        "return_acf_1": -0.2789390615866586,
        "abs_return_acf_1": 0.6218500728821529,
        "abs_return_acf_5": 0.4787246814731753,
        "abs_return_acf_20": 0.4079591855743168,
        "quantile_01": -0.10679058462082909,
        "quantile_99": 0.07492130375992778,
        "hill_tail_index": 2.438259197501981
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.025542081005871454,
        "excess_kurtosis": 27.893466573759948,
        "return_acf_1": -0.319752144672557,
        "abs_return_acf_1": 0.5149333825748122,
        "abs_return_acf_5": 0.33625832820239615,
        "abs_return_acf_20": 0.3402106041032129,
        "quantile_01": -0.09260217454239277,
        "quantile_99": 0.06317088657424613,
        "hill_tail_index": 1.8218817099022346
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.026803453077046797,
        "excess_kurtosis": 18.309890174056466,
        "return_acf_1": -0.2173305752325383,
        "abs_return_acf_1": 0.5751227953203024,
        "abs_return_acf_5": 0.4697619701207254,
        "abs_return_acf_20": 0.4200298175962467,
        "quantile_01": -0.09676881945362503,
        "quantile_99": 0.07263778379651437,
        "hill_tail_index": 3.1060200681021284
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02590551322556309,
        "excess_kurtosis": 20.181324095973924,
        "return_acf_1": -0.23332804306489605,
        "abs_return_acf_1": 0.5484098263125957,
        "abs_return_acf_5": 0.40480325546229745,
        "abs_return_acf_20": 0.4497652348019865,
        "quantile_01": -0.09404525991520404,
        "quantile_99": 0.0717569281915801,
        "hill_tail_index": 2.4654596393412405
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0241863248984644,
        "excess_kurtosis": 17.37640876727145,
        "return_acf_1": -0.22485868312277305,
        "abs_return_acf_1": 0.5221628292093259,
        "abs_return_acf_5": 0.40314224584268255,
        "abs_return_acf_20": 0.4020604386067961,
        "quantile_01": -0.07690071313800942,
        "quantile_99": 0.07549861304872785,
        "hill_tail_index": 2.5777943108215697
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.028463696960947978,
        "excess_kurtosis": 25.22975436715426,
        "return_acf_1": -0.23976494764642473,
        "abs_return_acf_1": 0.5437098264463096,
        "abs_return_acf_5": 0.4410525386106726,
        "abs_return_acf_20": 0.3915754416432963,
        "quantile_01": -0.09626895521317592,
        "quantile_99": 0.07853929823342154,
        "hill_tail_index": 2.5405341522817078
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.025231599241440052,
        "excess_kurtosis": 17.454912919938817,
        "return_acf_1": -0.21906166753751172,
        "abs_return_acf_1": 0.5913213574929259,
        "abs_return_acf_5": 0.44929945489367434,
        "abs_return_acf_20": 0.3502228213319164,
        "quantile_01": -0.09229838620654437,
        "quantile_99": 0.07085768192869889,
        "hill_tail_index": 2.7968781318501708
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02568817124502826,
        "excess_kurtosis": 24.79312564729673,
        "return_acf_1": -0.16003349724448948,
        "abs_return_acf_1": 0.5473354683670378,
        "abs_return_acf_5": 0.4304300165425708,
        "abs_return_acf_20": 0.35095599414247586,
        "quantile_01": -0.08231264893422237,
        "quantile_99": 0.07331871490967069,
        "hill_tail_index": 2.2758890178289883
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.030396266006089894,
        "excess_kurtosis": 22.197505497985336,
        "return_acf_1": -0.21807880250142725,
        "abs_return_acf_1": 0.5726202403814892,
        "abs_return_acf_5": 0.45430349906198964,
        "abs_return_acf_20": 0.41254948963520416,
        "quantile_01": -0.11117913911050908,
        "quantile_99": 0.105070877670073,
        "hill_tail_index": 1.907946965026463
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.025417295646169503,
        "excess_kurtosis": 24.415374539452976,
        "return_acf_1": -0.255438832705565,
        "abs_return_acf_1": 0.5801299802192598,
        "abs_return_acf_5": 0.40341708169724744,
        "abs_return_acf_20": 0.38394174215397553,
        "quantile_01": -0.08975682848929639,
        "quantile_99": 0.06587994214376242,
        "hill_tail_index": 1.9732669360937138
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.030724197412362673,
        "excess_kurtosis": 58.07701111885703,
        "return_acf_1": -0.18461840485047357,
        "abs_return_acf_1": 0.5261239251967446,
        "abs_return_acf_5": 0.5432602830032945,
        "abs_return_acf_20": 0.2775672742444076,
        "quantile_01": -0.05508416185018124,
        "quantile_99": 0.11070495968616544,
        "hill_tail_index": 1.2237397440120632
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.025956056418856878,
        "excess_kurtosis": 21.50011248371827,
        "return_acf_1": -0.15961228936197513,
        "abs_return_acf_1": 0.5775166205540827,
        "abs_return_acf_5": 0.477084171998155,
        "abs_return_acf_20": 0.4142562235534473,
        "quantile_01": -0.08935331683853885,
        "quantile_99": 0.06188953291435537,
        "hill_tail_index": 2.2363591508541196
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02591259913960212,
        "excess_kurtosis": 24.45907046920263,
        "return_acf_1": -0.24962569287309594,
        "abs_return_acf_1": 0.5266320087580775,
        "abs_return_acf_5": 0.3736033746987495,
        "abs_return_acf_20": 0.38722733988398744,
        "quantile_01": -0.0986424619526379,
        "quantile_99": 0.05920984559009343,
        "hill_tail_index": 1.9078329635909965
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02782100066251566,
        "excess_kurtosis": 29.94828018449082,
        "return_acf_1": -0.2940716184989237,
        "abs_return_acf_1": 0.5300782726467104,
        "abs_return_acf_5": 0.40783772336164686,
        "abs_return_acf_20": 0.3733184431443067,
        "quantile_01": -0.09747402585282097,
        "quantile_99": 0.06803268540102925,
        "hill_tail_index": 1.967705274044214
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.030433078337166474,
        "excess_kurtosis": 21.935647097013348,
        "return_acf_1": -0.28789343794314376,
        "abs_return_acf_1": 0.570991296161072,
        "abs_return_acf_5": 0.45969260686847696,
        "abs_return_acf_20": 0.3917644810598062,
        "quantile_01": -0.11665440384428033,
        "quantile_99": 0.08862090570521591,
        "hill_tail_index": 2.2079680255012066
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
