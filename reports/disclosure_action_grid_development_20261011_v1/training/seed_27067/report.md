# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27067
Run ID: `105d58a447f9608bd12776e5645b9be46392b79a41a460700a9d1b0cb14ee1e5`
Result fingerprint: `66db73600753b9f2f85473219a6300f4ee18fbca24948fff07ba1a9a224eddee`

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
    "equal_weight_sd": -0.5534642857142825,
    "equal_weight_raw": -8.301964285714238,
    "fixed_start_cap_weight_sd": -0.5274191041185535,
    "fixed_start_cap_weight_raw": -7.9112865617783035,
    "end_cap_weight_sd": -0.545219872388302,
    "end_cap_weight_raw": -8.17829808582453
  },
  "full_period_change": {
    "equal_weight_sd": -0.8693214285714238,
    "equal_weight_raw": -13.039821428571358
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.834262235449731,
    "inflation_mean_sd": 0.7271018518518517
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.39288765868605574,
    "equal_weight_raw": 5.893314880290836,
    "fixed_start_cap_weight_sd": 0.4205666522757779,
    "fixed_start_cap_weight_raw": 6.308499784136668,
    "end_cap_weight_sd": 0.40220841983560307,
    "end_cap_weight_raw": 6.0331262975340465
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.3173809523809492,
      "change_raw": -4.760714285714238,
      "decay_adjusted_gain_sd": 0.6350000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5887698412698381,
      "change_raw": -8.831547619047571,
      "decay_adjusted_gain_sd": 0.36361111111111416
    },
    "small": {
      "count": 18,
      "change_sd": -0.5751587301587269,
      "change_raw": -8.627380952380904,
      "decay_adjusted_gain_sd": 0.3671738755878687
    },
    "large_minus_small_sd": 0.25777777777777766,
    "large_minus_small_raw": 3.866666666666665
  },
  "inflation": {
    "initial_mean_sd": 0.2593333333333334,
    "final_mean_sd": 0.7794166666666666,
    "mean_sd": 0.5335368442964197,
    "mean_absolute_raw_gap": 8.003052664446294,
    "final_absolute_raw_gap": 11.691250000000002,
    "mean_range_fraction": 0.08003052664446293
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.18,
    "initial_wealth_share": 0.20144426390135461,
    "final_wealth_share": 0.15633839728183035
  },
  "pricing_slope": {
    "mean": -0.0030442598762770966,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.11849062464738931,
    "real_improvement_cost": 0.09832276399679624,
    "washing_cost": 0.020167860650593075,
    "fine_transfer": 0.0024270462406435407,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12091767088803285,
    "resource_cost_fraction_initial_cap": 0.003949687488246309,
    "private_net_outflow_fraction_initial_cap": 0.0040305890296010935,
    "fine_transfer_fraction_initial_cap": 8.090154135478467e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008054425123034427,
    "unapplied_final_day_resource_cost": 0.00021301106232798504
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 99.47310005037909,
    "beneficial_raw_gain_per_resource_cost": 1492.0965007556865,
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
    "accrued_cost": 3.2504225599362124,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.2742320837457356,
    "accrued_cost_fraction_initial_cap": 0.10834741866454038,
    "mean_contract_rate": 0.04476324508637831,
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
    "maximum_relative_cash_error": 2.610833385616125e-15,
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
      "minimum": -0.256766807837985,
      "maximum": -0.02461579149386215,
      "mean": -0.13700783019981497,
      "median": -0.13146862033629803,
      "quantile_05": -0.24351996475339935,
      "quantile_95": -0.051825072581351224
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
      "minimum": 0.23881005437631267,
      "maximum": 0.8287948322517533,
      "mean": 0.5571663339931879,
      "median": 0.5770581152131818,
      "quantile_05": 0.2977064657243726,
      "quantile_95": 0.7798792989706572
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
        "daily_volatility": 0.02241346292476083,
        "excess_kurtosis": 13.524391993873792,
        "return_acf_1": -0.15043445248915102,
        "abs_return_acf_1": 0.4244997300350466,
        "abs_return_acf_5": 0.33464593286040106,
        "abs_return_acf_20": 0.23394868645000647,
        "quantile_01": -0.07619235229579642,
        "quantile_99": 0.05860937223604936,
        "hill_tail_index": 3.1248983850891072
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02321058871698136,
        "excess_kurtosis": 11.715484763574857,
        "return_acf_1": -0.12286084929431565,
        "abs_return_acf_1": 0.44113468762986097,
        "abs_return_acf_5": 0.4237036741894633,
        "abs_return_acf_20": 0.3532157767411241,
        "quantile_01": -0.08309182811440122,
        "quantile_99": 0.07500954753277941,
        "hill_tail_index": 3.432590974267836
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022635090125006373,
        "excess_kurtosis": 7.821241143428525,
        "return_acf_1": -0.16346289521234053,
        "abs_return_acf_1": 0.44147360770091154,
        "abs_return_acf_5": 0.4419642959657819,
        "abs_return_acf_20": 0.3470143335572318,
        "quantile_01": -0.07800211687197602,
        "quantile_99": 0.07101957005241047,
        "hill_tail_index": 4.330863852037502
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022750137181813068,
        "excess_kurtosis": 8.139544710619361,
        "return_acf_1": -0.17919797614847988,
        "abs_return_acf_1": 0.49448712075691015,
        "abs_return_acf_5": 0.38912193352542496,
        "abs_return_acf_20": 0.35916350919431134,
        "quantile_01": -0.08588276892067648,
        "quantile_99": 0.06628039496344763,
        "hill_tail_index": 3.4060657226480244
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01650529544793869,
        "excess_kurtosis": 6.7236128291794195,
        "return_acf_1": -0.11000890654479976,
        "abs_return_acf_1": 0.24008687459861722,
        "abs_return_acf_5": 0.17775408891555428,
        "abs_return_acf_20": 0.22760883149040712,
        "quantile_01": -0.053457582311188516,
        "quantile_99": 0.040648542935628654,
        "hill_tail_index": 2.624611256029051
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022652978100962555,
        "excess_kurtosis": 8.711427078933262,
        "return_acf_1": -0.09634393814552004,
        "abs_return_acf_1": 0.4272108830674386,
        "abs_return_acf_5": 0.384221725628566,
        "abs_return_acf_20": 0.32960281499501637,
        "quantile_01": -0.08229614840326462,
        "quantile_99": 0.07195364811599747,
        "hill_tail_index": 3.277956912299536
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021042979485109026,
        "excess_kurtosis": 9.991500113102166,
        "return_acf_1": -0.08804427592516845,
        "abs_return_acf_1": 0.3258582914419616,
        "abs_return_acf_5": 0.3494698966350294,
        "abs_return_acf_20": 0.27796418136144396,
        "quantile_01": -0.06707923519175554,
        "quantile_99": 0.06086289203917794,
        "hill_tail_index": 2.8053664072549074
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02124957355734602,
        "excess_kurtosis": 4.949575562088579,
        "return_acf_1": -0.1398317034274331,
        "abs_return_acf_1": 0.3747689647875523,
        "abs_return_acf_5": 0.35043691948134614,
        "abs_return_acf_20": 0.3349455304659188,
        "quantile_01": -0.06182465908009225,
        "quantile_99": 0.0598439771620727,
        "hill_tail_index": 4.144304618147155
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.020092825680128313,
        "excess_kurtosis": 6.928941768353036,
        "return_acf_1": -0.11877379014785812,
        "abs_return_acf_1": 0.2547722095990886,
        "abs_return_acf_5": 0.16795979232734137,
        "abs_return_acf_20": 0.2001252487288051,
        "quantile_01": -0.05692550463590414,
        "quantile_99": 0.06083688454973256,
        "hill_tail_index": 2.8560000513011876
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02209125638593928,
        "excess_kurtosis": 9.097537649845709,
        "return_acf_1": -0.20274907355090255,
        "abs_return_acf_1": 0.44939318839834885,
        "abs_return_acf_5": 0.33194223050131133,
        "abs_return_acf_20": 0.30711365220999703,
        "quantile_01": -0.07821786615936605,
        "quantile_99": 0.06324102443342856,
        "hill_tail_index": 3.3486029306923903
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01910924546673031,
        "excess_kurtosis": 3.8177919521614934,
        "return_acf_1": -0.12825347344142096,
        "abs_return_acf_1": 0.36524707435888765,
        "abs_return_acf_5": 0.2896225804049055,
        "abs_return_acf_20": 0.30256271362091997,
        "quantile_01": -0.055723426276566575,
        "quantile_99": 0.05358096074518813,
        "hill_tail_index": 3.6684393663141828
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02291399111898677,
        "excess_kurtosis": 14.488638057597107,
        "return_acf_1": -0.1427971590320549,
        "abs_return_acf_1": 0.43060519111920215,
        "abs_return_acf_5": 0.32112553693608764,
        "abs_return_acf_20": 0.31580369220370114,
        "quantile_01": -0.08476826036748766,
        "quantile_99": 0.06486539177458772,
        "hill_tail_index": 2.881271557721531
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02306437996133884,
        "excess_kurtosis": 7.822564716701587,
        "return_acf_1": -0.10053828565646727,
        "abs_return_acf_1": 0.42743721048167377,
        "abs_return_acf_5": 0.35624332274247106,
        "abs_return_acf_20": 0.27337520222986517,
        "quantile_01": -0.07908590446208744,
        "quantile_99": 0.07442529068371992,
        "hill_tail_index": 3.173655033294435
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.023093058033341975,
        "excess_kurtosis": 14.10669639932,
        "return_acf_1": -0.256766807837985,
        "abs_return_acf_1": 0.42379925613669445,
        "abs_return_acf_5": 0.32844762540841627,
        "abs_return_acf_20": 0.27694492616534455,
        "quantile_01": -0.08244135137992033,
        "quantile_99": 0.07048013028233127,
        "hill_tail_index": 3.2401925198064916
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021700908789315198,
        "excess_kurtosis": 13.413708404058351,
        "return_acf_1": -0.02461579149386215,
        "abs_return_acf_1": 0.4003036487621828,
        "abs_return_acf_5": 0.40116349601068396,
        "abs_return_acf_20": 0.3004676304726875,
        "quantile_01": -0.06436532438397483,
        "quantile_99": 0.05567050001505597,
        "hill_tail_index": 2.42744938108664
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02368232206080231,
        "excess_kurtosis": 13.837995610156657,
        "return_acf_1": -0.04181245147398939,
        "abs_return_acf_1": 0.4862922787932873,
        "abs_return_acf_5": 0.4127272945327628,
        "abs_return_acf_20": 0.32332852635400816,
        "quantile_01": -0.0744206929584002,
        "quantile_99": 0.07057490203349134,
        "hill_tail_index": 2.5991642040954863
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02139549388580731,
        "excess_kurtosis": 8.518846121490474,
        "return_acf_1": -0.16808255308838094,
        "abs_return_acf_1": 0.4045056955765255,
        "abs_return_acf_5": 0.2651750959998931,
        "abs_return_acf_20": 0.24856792441785233,
        "quantile_01": -0.07843313974512962,
        "quantile_99": 0.06045940828618672,
        "hill_tail_index": 3.6652728089469107
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02563056780378503,
        "excess_kurtosis": 24.076378072059974,
        "return_acf_1": -0.08218881324828645,
        "abs_return_acf_1": 0.4863026367561323,
        "abs_return_acf_5": 0.3909982314075109,
        "abs_return_acf_20": 0.2828439326532241,
        "quantile_01": -0.07930265984331879,
        "quantile_99": 0.07239631002944748,
        "hill_tail_index": 2.099575562364925
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016406575721086256,
        "excess_kurtosis": 3.1217300006667177,
        "return_acf_1": -0.08766084395229344,
        "abs_return_acf_1": 0.2630418692898878,
        "abs_return_acf_5": 0.21647807774879757,
        "abs_return_acf_20": 0.19973543258072207,
        "quantile_01": -0.04309905585310848,
        "quantile_99": 0.04202421109797469,
        "hill_tail_index": 3.5365876181468034
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022629862929172916,
        "excess_kurtosis": 9.982913240754979,
        "return_acf_1": -0.11953389428716159,
        "abs_return_acf_1": 0.3559313426016989,
        "abs_return_acf_5": 0.29854681781314696,
        "abs_return_acf_20": 0.31992097982596784,
        "quantile_01": -0.07115819411684826,
        "quantile_99": 0.06766836622236498,
        "hill_tail_index": 3.05387520973699
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022115721067097242,
        "excess_kurtosis": 11.597552109697968,
        "return_acf_1": -0.19816173501566337,
        "abs_return_acf_1": 0.4705320532228667,
        "abs_return_acf_5": 0.34502865975750635,
        "abs_return_acf_20": 0.2574104498310731,
        "quantile_01": -0.07822740046280066,
        "quantile_99": 0.0645404249615835,
        "hill_tail_index": 3.187022941641249
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02420271205723513,
        "excess_kurtosis": 14.922156667582172,
        "return_acf_1": -0.2345669176373064,
        "abs_return_acf_1": 0.48078064515490454,
        "abs_return_acf_5": 0.341256390239286,
        "abs_return_acf_20": 0.2327232112512955,
        "quantile_01": -0.08107521266904576,
        "quantile_99": 0.08347842603951376,
        "hill_tail_index": 2.2526166185350887
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018356696356967444,
        "excess_kurtosis": 4.175700672130287,
        "return_acf_1": -0.06406272060146,
        "abs_return_acf_1": 0.35636468895236284,
        "abs_return_acf_5": 0.32301135739148323,
        "abs_return_acf_20": 0.2872520458092905,
        "quantile_01": -0.057360965224703506,
        "quantile_99": 0.05293083696471041,
        "hill_tail_index": 4.0156041046268065
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02103752687865787,
        "excess_kurtosis": 14.522901774388949,
        "return_acf_1": -0.158917759910238,
        "abs_return_acf_1": 0.3851636073704293,
        "abs_return_acf_5": 0.3707273843071457,
        "abs_return_acf_20": 0.3134350549703716,
        "quantile_01": -0.06086744095952435,
        "quantile_99": 0.06262557465677734,
        "hill_tail_index": 2.4388079186531177
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023110443835084017,
        "excess_kurtosis": 13.35745431172932,
        "return_acf_1": -0.1872019104207577,
        "abs_return_acf_1": 0.49407844272241264,
        "abs_return_acf_5": 0.36162515129352907,
        "abs_return_acf_20": 0.26311115246420946,
        "quantile_01": -0.0799910529097231,
        "quantile_99": 0.06606785865798592,
        "hill_tail_index": 2.686674167562891
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.025664011089549306,
        "excess_kurtosis": 12.454336811101292,
        "return_acf_1": -0.25084518512111176,
        "abs_return_acf_1": 0.5310166412610831,
        "abs_return_acf_5": 0.4631167629155077,
        "abs_return_acf_20": 0.36942100735228034,
        "quantile_01": -0.08601376976194974,
        "quantile_99": 0.08607667565914437,
        "hill_tail_index": 3.8131776995901903
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.023134732567725903,
        "excess_kurtosis": 15.130031459205394,
        "return_acf_1": -0.15769427035099692,
        "abs_return_acf_1": 0.45968905949000355,
        "abs_return_acf_5": 0.4040398982428632,
        "abs_return_acf_20": 0.28438763768498093,
        "quantile_01": -0.07194641412693152,
        "quantile_99": 0.06382091204449034,
        "hill_tail_index": 2.4747631754803625
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.025451076196527707,
        "excess_kurtosis": 17.513863312247754,
        "return_acf_1": -0.11235160261560012,
        "abs_return_acf_1": 0.5185591985070201,
        "abs_return_acf_5": 0.43188539747009463,
        "abs_return_acf_20": 0.36012267388606695,
        "quantile_01": -0.09767177228289736,
        "quantile_99": 0.06963759683910167,
        "hill_tail_index": 3.2966480050980325
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01690761372936085,
        "excess_kurtosis": 2.3694153976961942,
        "return_acf_1": -0.08779110269226874,
        "abs_return_acf_1": 0.22819839201725187,
        "abs_return_acf_5": 0.213749001497669,
        "abs_return_acf_20": 0.26574303225538115,
        "quantile_01": -0.048374584768886945,
        "quantile_99": 0.044944074746612696,
        "hill_tail_index": 4.514184481136445
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019968011139550507,
        "excess_kurtosis": 7.9044357027964445,
        "return_acf_1": -0.13468376723117506,
        "abs_return_acf_1": 0.3734175832037854,
        "abs_return_acf_5": 0.32859455513120256,
        "abs_return_acf_20": 0.2867814999189605,
        "quantile_01": -0.06737240545601633,
        "quantile_99": 0.05981681299361372,
        "hill_tail_index": 4.367257100911726
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
