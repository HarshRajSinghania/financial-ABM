# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27108
Run ID: `4620609a456523fd9b55aa376615d2acbfe7f1dc8138936aceb939ffe31c1399`
Result fingerprint: `5382aba75a6ea1b3195aef65de1af8d664c2c838178914e5061263acebb436bb`

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
    "equal_weight_sd": -0.6190595238095207,
    "equal_weight_raw": -9.285892857142812,
    "fixed_start_cap_weight_sd": -0.5245884155943784,
    "fixed_start_cap_weight_raw": -7.8688262339156765,
    "end_cap_weight_sd": -0.5351722426684566,
    "end_cap_weight_raw": -8.027583640026851
  },
  "full_period_change": {
    "equal_weight_sd": -0.9653251133438819,
    "equal_weight_raw": -14.47987670015823
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8950439761976658,
    "inflation_mean_sd": 0.6497506613756614
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.30157539682539986,
    "equal_weight_raw": 4.523630952380998,
    "fixed_start_cap_weight_sd": 0.31498864985311265,
    "fixed_start_cap_weight_raw": 4.72482974779669,
    "end_cap_weight_sd": 0.2900566791053775,
    "end_cap_weight_raw": 4.350850186580662
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.42166666666666425,
      "change_raw": -6.324999999999964,
      "decay_adjusted_gain_sd": 0.2132539682539706
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5879365079365048,
      "change_raw": -8.819047619047572,
      "decay_adjusted_gain_sd": 0.36444444444444757
    },
    "small": {
      "count": 18,
      "change_sd": -0.6675198412698381,
      "change_raw": -10.012797619047571,
      "decay_adjusted_gain_sd": 0.28486111111111423
    },
    "large_minus_small_sd": 0.24585317460317385,
    "large_minus_small_raw": 3.6877976190476076
  },
  "inflation": {
    "initial_mean_sd": 0.26625,
    "final_mean_sd": 0.6414166666666666,
    "mean_sd": 0.5010683458229254,
    "mean_absolute_raw_gap": 7.516025187343881,
    "final_absolute_raw_gap": 9.621250000000002,
    "mean_range_fraction": 0.0751602518734388
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.3,
    "initial_wealth_share": 0.2434287026347714,
    "final_wealth_share": 0.36902364867285925
  },
  "pricing_slope": {
    "mean": -0.0022736240793144397,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.4391630288738586,
    "real_improvement_cost": 0.2918016587480742,
    "washing_cost": 0.14736137012578443,
    "fine_transfer": 0.020639477478835384,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.459802506352694,
    "resource_cost_fraction_initial_cap": 0.014638767629128616,
    "private_net_outflow_fraction_initial_cap": 0.015326750211756463,
    "fine_transfer_fraction_initial_cap": 0.000687982582627846,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.08287230757401644,
    "unapplied_final_day_resource_cost": 0.0055448076184393446
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 20.60114652174114,
    "beneficial_raw_gain_per_resource_cost": 309.01719782611707,
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
    "accrued_cost": 2.9384171930120706,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.037773283178406586,
    "accrued_cost_fraction_initial_cap": 0.097947239767069,
    "mean_contract_rate": 0.04171005166283599,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 18,
    "maximum_relative_cash_error": 1.076968592534421e-15,
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
      "minimum": -0.20317291110474683,
      "maximum": 0.00014115634426108573,
      "mean": -0.11640551905984833,
      "median": -0.123726876271054,
      "quantile_05": -0.1888825652251437,
      "quantile_95": -0.03905835101072859
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
      "minimum": 0.2722040907834639,
      "maximum": 0.7358813824081599,
      "mean": 0.49270951862401224,
      "median": 0.44939793607361617,
      "quantile_05": 0.34097401422880713,
      "quantile_95": 0.6984558258657302
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
        "daily_volatility": 0.01646603485653595,
        "excess_kurtosis": 6.934438086664244,
        "return_acf_1": -0.04806462038791052,
        "abs_return_acf_1": 0.2987281497310682,
        "abs_return_acf_5": 0.27691916692033863,
        "abs_return_acf_20": 0.34228032991664087,
        "quantile_01": -0.05112630103508244,
        "quantile_99": 0.04427912488176288,
        "hill_tail_index": 3.2160321693214264
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016371748872040185,
        "excess_kurtosis": 6.518615912323886,
        "return_acf_1": -0.1294500835859007,
        "abs_return_acf_1": 0.20303513326941278,
        "abs_return_acf_5": 0.2707316051331621,
        "abs_return_acf_20": 0.21824705412364392,
        "quantile_01": -0.04368535673402677,
        "quantile_99": 0.04405812125709614,
        "hill_tail_index": 2.6664956140396923
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016256278671827662,
        "excess_kurtosis": 6.264424495915716,
        "return_acf_1": -0.03224895916256915,
        "abs_return_acf_1": 0.1996387926276493,
        "abs_return_acf_5": 0.23002395028523678,
        "abs_return_acf_20": 0.27916370550756786,
        "quantile_01": -0.05104033530728558,
        "quantile_99": 0.0431895893309647,
        "hill_tail_index": 3.1133726662773875
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016996259071424717,
        "excess_kurtosis": 5.0543357127898005,
        "return_acf_1": -0.11811036559395723,
        "abs_return_acf_1": 0.2758937179667119,
        "abs_return_acf_5": 0.3718663469658506,
        "abs_return_acf_20": 0.27439809149207156,
        "quantile_01": -0.05251731983533234,
        "quantile_99": 0.05152735207412765,
        "hill_tail_index": 3.186788296466054
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.015849937623665333,
        "excess_kurtosis": 4.860544952780944,
        "return_acf_1": -0.13060108196696918,
        "abs_return_acf_1": 0.2319846943075304,
        "abs_return_acf_5": 0.17479519752572825,
        "abs_return_acf_20": 0.2054228430181222,
        "quantile_01": -0.03972149368046148,
        "quantile_99": 0.04791671411808247,
        "hill_tail_index": 3.3513992048601406
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016517063525592558,
        "excess_kurtosis": 6.288555544880165,
        "return_acf_1": -0.12934338694815076,
        "abs_return_acf_1": 0.21890874949456282,
        "abs_return_acf_5": 0.28618693703551507,
        "abs_return_acf_20": 0.2662290711865878,
        "quantile_01": -0.04904631112380317,
        "quantile_99": 0.04217837259795327,
        "hill_tail_index": 2.6278327281629212
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016512967228500437,
        "excess_kurtosis": 5.910054675295704,
        "return_acf_1": -0.098317698744136,
        "abs_return_acf_1": 0.23828318683495792,
        "abs_return_acf_5": 0.17911752998878672,
        "abs_return_acf_20": 0.26303720514694734,
        "quantile_01": -0.047511422578141914,
        "quantile_99": 0.044533337676347616,
        "hill_tail_index": 3.712815499686392
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01730004690641277,
        "excess_kurtosis": 3.8566893320304034,
        "return_acf_1": -0.11521861846990199,
        "abs_return_acf_1": 0.2966933934105497,
        "abs_return_acf_5": 0.30559785272844336,
        "abs_return_acf_20": 0.2613998993775886,
        "quantile_01": -0.04748524092950535,
        "quantile_99": 0.047601795587715844,
        "hill_tail_index": 3.691085941753921
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01930009343885467,
        "excess_kurtosis": 19.916489974816937,
        "return_acf_1": -0.17913589619696568,
        "abs_return_acf_1": 0.40983732826138464,
        "abs_return_acf_5": 0.3824670055292083,
        "abs_return_acf_20": 0.33471781461094396,
        "quantile_01": -0.06711723744017091,
        "quantile_99": 0.04477357807197983,
        "hill_tail_index": 2.045298221919123
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01735312172525303,
        "excess_kurtosis": 7.988830622939828,
        "return_acf_1": -0.14675908616079542,
        "abs_return_acf_1": 0.3015119040564796,
        "abs_return_acf_5": 0.2581866101294773,
        "abs_return_acf_20": 0.22157902802754414,
        "quantile_01": -0.04389998827850357,
        "quantile_99": 0.0490690510649376,
        "hill_tail_index": 2.5531816326734322
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017147378104338768,
        "excess_kurtosis": 8.233128385700446,
        "return_acf_1": -0.15214676952085637,
        "abs_return_acf_1": 0.30070243605458125,
        "abs_return_acf_5": 0.25572378902301945,
        "abs_return_acf_20": 0.2711005072387494,
        "quantile_01": -0.04180263117868574,
        "quantile_99": 0.051936795644030136,
        "hill_tail_index": 2.535894309659127
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017579016891535102,
        "excess_kurtosis": 3.7081375517168125,
        "return_acf_1": -0.1449443242339721,
        "abs_return_acf_1": 0.26725173426735344,
        "abs_return_acf_5": 0.23361345796245866,
        "abs_return_acf_20": 0.1910902683562218,
        "quantile_01": -0.052890728009728556,
        "quantile_99": 0.04993052761834826,
        "hill_tail_index": 4.2235498415993735
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018310502219869913,
        "excess_kurtosis": 4.00744728348311,
        "return_acf_1": -0.10195049224662002,
        "abs_return_acf_1": 0.31336353424298097,
        "abs_return_acf_5": 0.28298890308192315,
        "abs_return_acf_20": 0.27320193342350263,
        "quantile_01": -0.056066314834702737,
        "quantile_99": 0.05310543521679379,
        "hill_tail_index": 3.6081453498960845
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017696299855934926,
        "excess_kurtosis": 9.900342454882924,
        "return_acf_1": -0.15245182587793638,
        "abs_return_acf_1": 0.30468460252117197,
        "abs_return_acf_5": 0.2728787222703462,
        "abs_return_acf_20": 0.2529659583249962,
        "quantile_01": -0.04800986430508415,
        "quantile_99": 0.055070031674467904,
        "hill_tail_index": 2.49279016185674
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01661025514067742,
        "excess_kurtosis": 4.220916242540162,
        "return_acf_1": -0.10492087851177684,
        "abs_return_acf_1": 0.28748396479103383,
        "abs_return_acf_5": 0.23125186222695612,
        "abs_return_acf_20": 0.16201788978733547,
        "quantile_01": -0.04500637795353596,
        "quantile_99": 0.04938090077360312,
        "hill_tail_index": 3.4679235408415203
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01820822443897972,
        "excess_kurtosis": 7.070871318640956,
        "return_acf_1": -0.13643980956857388,
        "abs_return_acf_1": 0.2825320907720576,
        "abs_return_acf_5": 0.339130895292285,
        "abs_return_acf_20": 0.3248087252929321,
        "quantile_01": -0.04862451563734481,
        "quantile_99": 0.05406299703293477,
        "hill_tail_index": 3.1712785593447195
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018491594982709254,
        "excess_kurtosis": 23.164571789044032,
        "return_acf_1": -0.19685711261183483,
        "abs_return_acf_1": 0.43382039596314265,
        "abs_return_acf_5": 0.2447317292046603,
        "abs_return_acf_20": 0.38369274119599645,
        "quantile_01": -0.062486637581730314,
        "quantile_99": 0.043595262897124946,
        "hill_tail_index": 1.942620058387028
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017593635263388672,
        "excess_kurtosis": 11.696951625125548,
        "return_acf_1": -0.0473809410473678,
        "abs_return_acf_1": 0.23372565292881511,
        "abs_return_acf_5": 0.3013137118314114,
        "abs_return_acf_20": 0.3448990179541364,
        "quantile_01": -0.05546740205555892,
        "quantile_99": 0.04533392895075521,
        "hill_tail_index": 2.6184997753881527
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01665774160545685,
        "excess_kurtosis": 7.172038589412802,
        "return_acf_1": -0.15223479659946618,
        "abs_return_acf_1": 0.28435471020827996,
        "abs_return_acf_5": 0.21624056683007564,
        "abs_return_acf_20": 0.2685814538490585,
        "quantile_01": -0.046584633345347175,
        "quantile_99": 0.04428230222773951,
        "hill_tail_index": 2.6815045493324985
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01639938999111569,
        "excess_kurtosis": 6.22774124461403,
        "return_acf_1": -0.058087811284843284,
        "abs_return_acf_1": 0.24899147125478627,
        "abs_return_acf_5": 0.29151818936978324,
        "abs_return_acf_20": 0.2330375286332014,
        "quantile_01": -0.04316781748469764,
        "quantile_99": 0.04275850880434468,
        "hill_tail_index": 2.5153686230751484
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.015051062769329764,
        "excess_kurtosis": 3.444511496761896,
        "return_acf_1": -0.09161047846478455,
        "abs_return_acf_1": 0.27281332996859536,
        "abs_return_acf_5": 0.20324394200613757,
        "abs_return_acf_20": 0.20919897200511142,
        "quantile_01": -0.044053494574165526,
        "quantile_99": 0.040895204700700606,
        "hill_tail_index": 3.8690548397226965
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01779369754857639,
        "excess_kurtosis": 13.02543104741829,
        "return_acf_1": -0.08047489151852423,
        "abs_return_acf_1": 0.34870473077606706,
        "abs_return_acf_5": 0.25760049368152904,
        "abs_return_acf_20": 0.3099552554283431,
        "quantile_01": -0.05829904956415121,
        "quantile_99": 0.040438537710811275,
        "hill_tail_index": 2.0728111171316512
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.016569935118063386,
        "excess_kurtosis": 14.459217429360148,
        "return_acf_1": -0.1319285933521213,
        "abs_return_acf_1": 0.3410017037861682,
        "abs_return_acf_5": 0.2958342235112811,
        "abs_return_acf_20": 0.33096332510427096,
        "quantile_01": -0.05396728105064742,
        "quantile_99": 0.0424433572155874,
        "hill_tail_index": 2.495743465980219
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01595558930403994,
        "excess_kurtosis": 9.487141575422816,
        "return_acf_1": -0.10791103425046479,
        "abs_return_acf_1": 0.29335608471332786,
        "abs_return_acf_5": 0.2285898711375618,
        "abs_return_acf_20": 0.2694707173154648,
        "quantile_01": -0.04392864018960963,
        "quantile_99": 0.04100878119689577,
        "hill_tail_index": 2.7260109805444754
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.0184268131529763,
        "excess_kurtosis": 12.645373566183695,
        "return_acf_1": -0.16174175744993952,
        "abs_return_acf_1": 0.30660191959412164,
        "abs_return_acf_5": 0.393469305613562,
        "abs_return_acf_20": 0.32839078108703545,
        "quantile_01": -0.061998381191822036,
        "quantile_99": 0.05039967309023071,
        "hill_tail_index": 2.670084892866709
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016447724987234173,
        "excess_kurtosis": 4.605145367692146,
        "return_acf_1": -0.05514037234112686,
        "abs_return_acf_1": 0.24729250215462112,
        "abs_return_acf_5": 0.17362919895534684,
        "abs_return_acf_20": 0.13628887777329815,
        "quantile_01": -0.047244878416236195,
        "quantile_99": 0.04680274875221416,
        "hill_tail_index": 3.7075870122474774
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01676676704161893,
        "excess_kurtosis": 7.870558820499227,
        "return_acf_1": 0.00014115634426108573,
        "abs_return_acf_1": 0.3219421707673025,
        "abs_return_acf_5": 0.2510751158543922,
        "abs_return_acf_20": 0.3137932798703305,
        "quantile_01": -0.05427896262708297,
        "quantile_99": 0.04835660776858545,
        "hill_tail_index": 3.295485681570154
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.016869666439057258,
        "excess_kurtosis": 8.447390346658574,
        "return_acf_1": -0.11070662212699604,
        "abs_return_acf_1": 0.279101265903084,
        "abs_return_acf_5": 0.2432135615807397,
        "abs_return_acf_20": 0.2397525889038763,
        "quantile_01": -0.04661094775175431,
        "quantile_99": 0.047583244639172524,
        "hill_tail_index": 2.700109720168515
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017787284342734532,
        "excess_kurtosis": 9.0367108580972,
        "return_acf_1": -0.20317291110474683,
        "abs_return_acf_1": 0.33609481809215946,
        "abs_return_acf_5": 0.35698247234326047,
        "abs_return_acf_20": 0.2813717128983489,
        "quantile_01": -0.05748477195234644,
        "quantile_99": 0.05030615856788915,
        "hill_tail_index": 2.5359411286779947
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01753574979426341,
        "excess_kurtosis": 7.220480721412326,
        "return_acf_1": -0.1749555088105028,
        "abs_return_acf_1": 0.2928509604514834,
        "abs_return_acf_5": 0.29759426249252335,
        "abs_return_acf_20": 0.22796829649298891,
        "quantile_01": -0.051119890387108395,
        "quantile_99": 0.045283683681147616,
        "hill_tail_index": 2.7533747544336773
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
