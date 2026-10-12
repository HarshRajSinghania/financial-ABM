# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27130
Run ID: `9608908409120757115d7e32a3c1d5b93e37cb7700a8e9c45bbf7e6865467769`
Result fingerprint: `a16461eb8695c8549a1b3874f97388ba7411e38b6037500be2a94eee300d0690`

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
    "equal_weight_sd": -0.6131903893929349,
    "equal_weight_raw": -9.197855840894025,
    "fixed_start_cap_weight_sd": -0.5001319480257271,
    "fixed_start_cap_weight_raw": -7.501979220385907,
    "end_cap_weight_sd": -0.5337346982912524,
    "end_cap_weight_raw": -8.006020474368787
  },
  "full_period_change": {
    "equal_weight_sd": -1.0048808655834096,
    "equal_weight_raw": -15.073212983751144
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9466007729908174,
    "inflation_mean_sd": 0.5806180555555556
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.32191666666666985,
    "equal_weight_raw": 4.828750000000047,
    "fixed_start_cap_weight_sd": 0.4504210502529163,
    "fixed_start_cap_weight_raw": 6.7563157537937455,
    "end_cap_weight_sd": 0.41635406576082223,
    "end_cap_weight_raw": 6.245310986412335
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.03488095238094909,
      "change_raw": -0.5232142857142363,
      "decay_adjusted_gain_sd": 0.9175000000000034
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6809920634920602,
      "change_raw": -10.214880952380904,
      "decay_adjusted_gain_sd": 0.27138888888889207
    },
    "small": {
      "count": 18,
      "change_sd": -0.6756744585120367,
      "change_raw": -10.13511687768055,
      "decay_adjusted_gain_sd": 0.24791666666666964
    },
    "large_minus_small_sd": 0.6407935061310875,
    "large_minus_small_raw": 9.611902591966313
  },
  "inflation": {
    "initial_mean_sd": 0.2846666666666667,
    "final_mean_sd": 0.5973333333333334,
    "mean_sd": 0.4655764640577297,
    "mean_absolute_raw_gap": 6.983646960865945,
    "final_absolute_raw_gap": 8.96,
    "mean_range_fraction": 0.06983646960865945
  },
  "impact": {
    "initial_share": 0.18666666666666668,
    "final_share": 0.22,
    "initial_wealth_share": 0.18872870396239425,
    "final_wealth_share": 0.2186662247464087
  },
  "pricing_slope": {
    "mean": -0.001257858630943024,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.28830612159169383,
    "real_improvement_cost": 0.2488693385088679,
    "washing_cost": 0.039436783082825944,
    "fine_transfer": 0.010282409298009238,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.29858853088970305,
    "resource_cost_fraction_initial_cap": 0.009610204053056463,
    "private_net_outflow_fraction_initial_cap": 0.00995295102965677,
    "fine_transfer_fraction_initial_cap": 0.000342746976600308,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.013660564874157698,
    "unapplied_final_day_resource_cost": 0.001292598134148625
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 33.49738100142488,
    "beneficial_raw_gain_per_resource_cost": 502.4607150213732,
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
    "accrued_cost": 2.686980096991874,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.2892103791986027,
    "accrued_cost_fraction_initial_cap": 0.08956600323306246,
    "mean_contract_rate": 0.03811926747821949,
    "maximum_ledger_error": 5.421010862427522e-20
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
    "maximum_relative_cash_error": 1.7681722047688082e-15,
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
      "minimum": -0.2566143513450934,
      "maximum": -0.10262404095647336,
      "mean": -0.16671108601640725,
      "median": -0.157059577856748,
      "quantile_05": -0.23692850013846098,
      "quantile_95": -0.10843954889883399
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
      "minimum": 0.33225455496633577,
      "maximum": 0.7447356972553957,
      "mean": 0.5121107632294813,
      "median": 0.4961672183739319,
      "quantile_05": 0.3686567955699551,
      "quantile_95": 0.6799709175648722
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
        "daily_volatility": 0.017628341636092466,
        "excess_kurtosis": 3.901551257375968,
        "return_acf_1": -0.16949068581309978,
        "abs_return_acf_1": 0.28639599994592985,
        "abs_return_acf_5": 0.25764775374124754,
        "abs_return_acf_20": 0.18365270593674027,
        "quantile_01": -0.05245940704505963,
        "quantile_99": 0.04715469905087087,
        "hill_tail_index": 3.9103486272502597
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02244867238080841,
        "excess_kurtosis": 12.329747579984241,
        "return_acf_1": -0.16408119974747934,
        "abs_return_acf_1": 0.4889344203647965,
        "abs_return_acf_5": 0.41532634101057836,
        "abs_return_acf_20": 0.31487591168807433,
        "quantile_01": -0.08185515710722399,
        "quantile_99": 0.06887680704221737,
        "hill_tail_index": 3.021915802646459
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018514671793279057,
        "excess_kurtosis": 8.922218888094113,
        "return_acf_1": -0.1140162147234135,
        "abs_return_acf_1": 0.3967311301126109,
        "abs_return_acf_5": 0.3372376438969986,
        "abs_return_acf_20": 0.37108154525405007,
        "quantile_01": -0.059128493062737666,
        "quantile_99": 0.04786964456623515,
        "hill_tail_index": 2.5242217952850283
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017395109112474636,
        "excess_kurtosis": 13.29935666837136,
        "return_acf_1": -0.10262404095647336,
        "abs_return_acf_1": 0.1955476142893671,
        "abs_return_acf_5": 0.2111292655926755,
        "abs_return_acf_20": 0.18252602953410033,
        "quantile_01": -0.04335603769342997,
        "quantile_99": 0.045582531346441225,
        "hill_tail_index": 2.0877736180518367
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.016487374634669427,
        "excess_kurtosis": 1.696108213437797,
        "return_acf_1": -0.2054673545419809,
        "abs_return_acf_1": 0.2266700722552037,
        "abs_return_acf_5": 0.14817280324595017,
        "abs_return_acf_20": 0.179477929792367,
        "quantile_01": -0.04320847578710173,
        "quantile_99": 0.044623318820854546,
        "hill_tail_index": 4.254793264367742
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017722581576304505,
        "excess_kurtosis": 5.249207770310406,
        "return_acf_1": -0.15721066522504315,
        "abs_return_acf_1": 0.31268014964702234,
        "abs_return_acf_5": 0.22650999418246104,
        "abs_return_acf_20": 0.23869103149156756,
        "quantile_01": -0.047328541915339264,
        "quantile_99": 0.04593411558965395,
        "hill_tail_index": 3.2832926784498295
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01798366850855632,
        "excess_kurtosis": 3.789231316553529,
        "return_acf_1": -0.1400000880936056,
        "abs_return_acf_1": 0.2638978682728537,
        "abs_return_acf_5": 0.3048894297657981,
        "abs_return_acf_20": 0.24438766059525552,
        "quantile_01": -0.05257040246123909,
        "quantile_99": 0.04723857150980365,
        "hill_tail_index": 3.6874035496255617
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.0167382810708973,
        "excess_kurtosis": 4.211036670121289,
        "return_acf_1": -0.1400433521673663,
        "abs_return_acf_1": 0.21728463672401568,
        "abs_return_acf_5": 0.23924347514529623,
        "abs_return_acf_20": 0.18187284201526277,
        "quantile_01": -0.0459074609833175,
        "quantile_99": 0.04181724537267172,
        "hill_tail_index": 2.9999926030919197
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01838757500899045,
        "excess_kurtosis": 5.542539543564395,
        "return_acf_1": -0.15206401414313492,
        "abs_return_acf_1": 0.3314253651266512,
        "abs_return_acf_5": 0.2782584652956818,
        "abs_return_acf_20": 0.3147473000018895,
        "quantile_01": -0.05608774517828744,
        "quantile_99": 0.05395630881237821,
        "hill_tail_index": 3.69232760793854
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01663991735704599,
        "excess_kurtosis": 1.7374130684972178,
        "return_acf_1": -0.17356242731862087,
        "abs_return_acf_1": 0.2087341288847171,
        "abs_return_acf_5": 0.08039123013315244,
        "abs_return_acf_20": 0.12230737243105033,
        "quantile_01": -0.0423217096051214,
        "quantile_99": 0.04010133546359784,
        "hill_tail_index": 4.126728671325498
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018187381077300908,
        "excess_kurtosis": 10.197017086021223,
        "return_acf_1": -0.1551870487279637,
        "abs_return_acf_1": 0.2997836217383488,
        "abs_return_acf_5": 0.22270997295352746,
        "abs_return_acf_20": 0.22504350550894298,
        "quantile_01": -0.05184240659388382,
        "quantile_99": 0.04727088622281988,
        "hill_tail_index": 2.52940790658653
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.016316359223042212,
        "excess_kurtosis": 3.424966559942887,
        "return_acf_1": -0.2544829514007811,
        "abs_return_acf_1": 0.20821459136444878,
        "abs_return_acf_5": 0.15541655250571898,
        "abs_return_acf_20": 0.07043385388744015,
        "quantile_01": -0.04025108553268189,
        "quantile_99": 0.04008521302996523,
        "hill_tail_index": 3.888164063725859
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01688137032062591,
        "excess_kurtosis": 1.918008273334018,
        "return_acf_1": -0.2566143513450934,
        "abs_return_acf_1": 0.22296335628710817,
        "abs_return_acf_5": 0.19082083771361516,
        "abs_return_acf_20": 0.19157910331706973,
        "quantile_01": -0.04905843671780822,
        "quantile_99": 0.04472784769671443,
        "hill_tail_index": 4.20550939328702
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.0174226186714828,
        "excess_kurtosis": 5.484295265896671,
        "return_acf_1": -0.20821006956005994,
        "abs_return_acf_1": 0.27283685086664483,
        "abs_return_acf_5": 0.18736848667165454,
        "abs_return_acf_20": 0.18466753438554814,
        "quantile_01": -0.047663571967683414,
        "quantile_99": 0.04158899449547519,
        "hill_tail_index": 2.710359303957515
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017165820509084124,
        "excess_kurtosis": 4.830184439951373,
        "return_acf_1": -0.10387682231508706,
        "abs_return_acf_1": 0.3415412863268046,
        "abs_return_acf_5": 0.16742659088214346,
        "abs_return_acf_20": 0.1394565983095784,
        "quantile_01": -0.05158489405863094,
        "quantile_99": 0.04842542597541207,
        "hill_tail_index": 3.506106748777449
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021680218322587205,
        "excess_kurtosis": 8.480019262169504,
        "return_acf_1": -0.21547305970673641,
        "abs_return_acf_1": 0.3635378307427976,
        "abs_return_acf_5": 0.3269366628031938,
        "abs_return_acf_20": 0.2965326027155157,
        "quantile_01": -0.062439735127495934,
        "quantile_99": 0.06233370189523583,
        "hill_tail_index": 2.9945211371729528
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017472573866106372,
        "excess_kurtosis": 3.0551937962629756,
        "return_acf_1": -0.13862468677386636,
        "abs_return_acf_1": 0.26113130182678124,
        "abs_return_acf_5": 0.2221824885211381,
        "abs_return_acf_20": 0.13768792514277356,
        "quantile_01": -0.047913494425082866,
        "quantile_99": 0.047256675114049185,
        "hill_tail_index": 4.275440390264886
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018016050359391893,
        "excess_kurtosis": 3.174791236028871,
        "return_acf_1": -0.19641758151450212,
        "abs_return_acf_1": 0.31046440741357323,
        "abs_return_acf_5": 0.23489101706570562,
        "abs_return_acf_20": 0.11667425606710169,
        "quantile_01": -0.052190060864785406,
        "quantile_99": 0.05876086587945438,
        "hill_tail_index": 3.6334875850712307
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016562133849067413,
        "excess_kurtosis": 4.421505559190431,
        "return_acf_1": -0.19238666055465678,
        "abs_return_acf_1": 0.27846599384689774,
        "abs_return_acf_5": 0.20070881634065488,
        "abs_return_acf_20": 0.21000451783106006,
        "quantile_01": -0.05352089998038047,
        "quantile_99": 0.041425418515161384,
        "hill_tail_index": 2.649952462500082
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.0204036513368429,
        "excess_kurtosis": 13.309343533720323,
        "return_acf_1": -0.2074263805636211,
        "abs_return_acf_1": 0.34176008344081654,
        "abs_return_acf_5": 0.3277040656659909,
        "abs_return_acf_20": 0.32721582638911195,
        "quantile_01": -0.07519583668970535,
        "quantile_99": 0.058678916459526075,
        "hill_tail_index": 2.798706159975717
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018666262815787208,
        "excess_kurtosis": 5.976643777897637,
        "return_acf_1": -0.14346165643421283,
        "abs_return_acf_1": 0.3538256531945205,
        "abs_return_acf_5": 0.33413421991371406,
        "abs_return_acf_20": 0.2952438821456891,
        "quantile_01": -0.06170523168726419,
        "quantile_99": 0.05774794093465726,
        "hill_tail_index": 4.034204004192159
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017366837330241403,
        "excess_kurtosis": 4.147668445549915,
        "return_acf_1": -0.16678142638043425,
        "abs_return_acf_1": 0.30609829956260265,
        "abs_return_acf_5": 0.27355138768553366,
        "abs_return_acf_20": 0.27860751599698624,
        "quantile_01": -0.05405558258051875,
        "quantile_99": 0.044339387015022866,
        "hill_tail_index": 4.060442884351801
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019406287150647336,
        "excess_kurtosis": 6.794467967474098,
        "return_acf_1": -0.1569084904884529,
        "abs_return_acf_1": 0.38125264913328183,
        "abs_return_acf_5": 0.32409142561698323,
        "abs_return_acf_20": 0.28857790648053083,
        "quantile_01": -0.06719971653758426,
        "quantile_99": 0.05326951406849781,
        "hill_tail_index": 3.138161608766204
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018647224631976593,
        "excess_kurtosis": 5.007974642351865,
        "return_acf_1": -0.1566124576248083,
        "abs_return_acf_1": 0.3709663280059936,
        "abs_return_acf_5": 0.29345451122805694,
        "abs_return_acf_20": 0.32548716656757304,
        "quantile_01": -0.056956074701723425,
        "quantile_99": 0.04767732440925502,
        "hill_tail_index": 4.446059647908912
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02169855447667533,
        "excess_kurtosis": 6.346806248624192,
        "return_acf_1": -0.1816852016882051,
        "abs_return_acf_1": 0.4498434667534466,
        "abs_return_acf_5": 0.38740446326129846,
        "abs_return_acf_20": 0.3289806027058776,
        "quantile_01": -0.06352738043293266,
        "quantile_99": 0.07096870007180732,
        "hill_tail_index": 3.6316224484261372
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016920331284879145,
        "excess_kurtosis": 5.229868253610702,
        "return_acf_1": -0.14920825043925612,
        "abs_return_acf_1": 0.240048879784142,
        "abs_return_acf_5": 0.24097200086993914,
        "abs_return_acf_20": 0.18992850679724768,
        "quantile_01": -0.05050713370027464,
        "quantile_99": 0.04522288105906632,
        "hill_tail_index": 3.1602682015674453
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020510135342813065,
        "excess_kurtosis": 6.878861528718808,
        "return_acf_1": -0.14206747826272575,
        "abs_return_acf_1": 0.4142776155162172,
        "abs_return_acf_5": 0.41863720734660564,
        "abs_return_acf_20": 0.338857695213199,
        "quantile_01": -0.06658003957599343,
        "quantile_99": 0.06294106771190802,
        "hill_tail_index": 3.7677992013006825
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018479380686407403,
        "excess_kurtosis": 5.308101130511565,
        "return_acf_1": -0.18388220757406448,
        "abs_return_acf_1": 0.2584407473213513,
        "abs_return_acf_5": 0.23273288256675864,
        "abs_return_acf_20": 0.1820774477526581,
        "quantile_01": -0.05463286274070115,
        "quantile_99": 0.04937608958751105,
        "hill_tail_index": 3.3570448326842586
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019213229948364868,
        "excess_kurtosis": 5.509490169551118,
        "return_acf_1": -0.15399235938007805,
        "abs_return_acf_1": 0.47199595625362384,
        "abs_return_acf_5": 0.39364413747925964,
        "abs_return_acf_20": 0.2923366353602068,
        "quantile_01": -0.07124299103303999,
        "quantile_99": 0.053932134208183255,
        "hill_tail_index": 3.627716028653797
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017523927234217945,
        "excess_kurtosis": 3.157674000367159,
        "return_acf_1": -0.11947339702739496,
        "abs_return_acf_1": 0.2728738212391776,
        "abs_return_acf_5": 0.24949379330336377,
        "abs_return_acf_20": 0.22205869772982714,
        "quantile_01": -0.04812507051189824,
        "quantile_99": 0.04679410379803481,
        "hill_tail_index": 4.063496708324211
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
