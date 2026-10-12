# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27247
Run ID: `75a46d5c76a013ad74deb7ac07b28466a3499c5c934b1b1561f0e2a554ddfd80`
Result fingerprint: `899fd59fbd6e8320ef346da9d8b9750676e0fdb43095bae54a587b4d926df6e8`

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
    "equal_weight_sd": -0.8120155928074,
    "equal_weight_raw": -12.180233892111001,
    "fixed_start_cap_weight_sd": -0.7502425182367262,
    "fixed_start_cap_weight_raw": -11.25363777355089,
    "end_cap_weight_sd": -0.7629803405318438,
    "end_cap_weight_raw": -11.44470510797765
  },
  "full_period_change": {
    "equal_weight_sd": -1.2380394023312078,
    "equal_weight_raw": -18.570591034968118
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1659521958693144,
    "inflation_mean_sd": 0.428558201058201
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.10175000000000288,
    "equal_weight_raw": 1.5262500000000432,
    "fixed_start_cap_weight_sd": 0.17377553908728585,
    "fixed_start_cap_weight_raw": 2.606633086309288,
    "end_cap_weight_sd": 0.16135677521140568,
    "end_cap_weight_raw": 2.4203516281710855
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.472380952380949,
      "change_raw": -7.085714285714236,
      "decay_adjusted_gain_sd": 0.48000000000000326
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7888358708147992,
      "change_raw": -11.832538062221989,
      "decay_adjusted_gain_sd": 0.04111111111111362
    },
    "small": {
      "count": 18,
      "change_sd": -0.8802112272081091,
      "change_raw": -13.203168408121636,
      "decay_adjusted_gain_sd": 0.06902777777778077
    },
    "large_minus_small_sd": 0.40783027482716006,
    "large_minus_small_raw": 6.117454122407401
  },
  "inflation": {
    "initial_mean_sd": 0.27525000000000005,
    "final_mean_sd": 0.4494166666666667,
    "mean_sd": 0.3556434221482098,
    "mean_absolute_raw_gap": 5.334651332223147,
    "final_absolute_raw_gap": 6.741249999999998,
    "mean_range_fraction": 0.05334651332223147
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.3,
    "initial_wealth_share": 0.2703601691564684,
    "final_wealth_share": 0.3135588773349602
  },
  "pricing_slope": {
    "mean": -0.0009508905161426863,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.031467183833257945,
    "real_improvement_cost": 0.023152657967973223,
    "washing_cost": 0.008314525865284729,
    "fine_transfer": 0.027920645202548923,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05938782903580687,
    "resource_cost_fraction_initial_cap": 0.0010489061277752646,
    "private_net_outflow_fraction_initial_cap": 0.0019795943011935617,
    "fine_transfer_fraction_initial_cap": 0.0009306881734182972,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0019502718497276157,
    "unapplied_final_day_resource_cost": 0.0009812022987655679
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 97.00582092681177,
    "beneficial_raw_gain_per_resource_cost": 1455.0873139021764,
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
    "accrued_cost": 2.8190477518460493,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.15714272434442794,
    "accrued_cost_fraction_initial_cap": 0.09396825839486829,
    "mean_contract_rate": 0.03947768320190758,
    "maximum_ledger_error": 4.5951537388545793e-20
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
    "maximum_relative_cash_error": 2.203886752366819e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.1754573584518076,
      "maximum": -0.02015547617366312,
      "mean": -0.10576064082327478,
      "median": -0.10807621351180897,
      "quantile_05": -0.1671309070661201,
      "quantile_95": -0.04077098558129431
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
      "minimum": 0.2472515813238176,
      "maximum": 0.7369439471562053,
      "mean": 0.43605802883298206,
      "median": 0.40138237065914356,
      "quantile_05": 0.30743187178990405,
      "quantile_95": 0.6486162974022682
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
        "daily_volatility": 0.018816693333602832,
        "excess_kurtosis": 3.636615592196752,
        "return_acf_1": -0.1590787472335645,
        "abs_return_acf_1": 0.334440159759171,
        "abs_return_acf_5": 0.34976537632817445,
        "abs_return_acf_20": 0.37111067134065734,
        "quantile_01": -0.05906246714669629,
        "quantile_99": 0.05753793073500619,
        "hill_tail_index": 5.401885653555662
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018679687972969983,
        "excess_kurtosis": 6.0993309234130475,
        "return_acf_1": -0.07227070233497078,
        "abs_return_acf_1": 0.379037823622646,
        "abs_return_acf_5": 0.30043276602047303,
        "abs_return_acf_20": 0.30673202350193146,
        "quantile_01": -0.058694347910508794,
        "quantile_99": 0.058323999596866516,
        "hill_tail_index": 3.6415094442203024
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019898200428375017,
        "excess_kurtosis": 7.266170320498416,
        "return_acf_1": -0.04925196900758141,
        "abs_return_acf_1": 0.363213030680038,
        "abs_return_acf_5": 0.3734295331267531,
        "abs_return_acf_20": 0.3161206440738065,
        "quantile_01": -0.06660191987296733,
        "quantile_99": 0.05893733231932011,
        "hill_tail_index": 3.795904925721655
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019960672565190147,
        "excess_kurtosis": 11.233256646563387,
        "return_acf_1": -0.1396941860785872,
        "abs_return_acf_1": 0.3751785659848434,
        "abs_return_acf_5": 0.4065121830670928,
        "abs_return_acf_20": 0.2562045300319067,
        "quantile_01": -0.0704141228052375,
        "quantile_99": 0.05492778272388605,
        "hill_tail_index": 2.9927895141301195
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018700864033717783,
        "excess_kurtosis": 4.59868603123388,
        "return_acf_1": -0.1159194874549635,
        "abs_return_acf_1": 0.23385759151625812,
        "abs_return_acf_5": 0.3039641035057459,
        "abs_return_acf_20": 0.28743762860408273,
        "quantile_01": -0.053690852075331176,
        "quantile_99": 0.05694144916803745,
        "hill_tail_index": 4.056620408236405
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016269913492654282,
        "excess_kurtosis": 6.127218656899373,
        "return_acf_1": -0.03383199914160478,
        "abs_return_acf_1": 0.2839130936203217,
        "abs_return_acf_5": 0.26788443590159555,
        "abs_return_acf_20": 0.27606053339906156,
        "quantile_01": -0.05335541191672931,
        "quantile_99": 0.03805472918010638,
        "hill_tail_index": 2.3538791014821143
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01798493419649151,
        "excess_kurtosis": 3.4310967675284587,
        "return_acf_1": -0.11063994671404377,
        "abs_return_acf_1": 0.20116102483697415,
        "abs_return_acf_5": 0.233866201499835,
        "abs_return_acf_20": 0.2299052883968032,
        "quantile_01": -0.049676293461875104,
        "quantile_99": 0.04950422092564496,
        "hill_tail_index": 3.846145668338431
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015510645482711406,
        "excess_kurtosis": 3.392440420920014,
        "return_acf_1": -0.10755517062971261,
        "abs_return_acf_1": 0.24282121101902812,
        "abs_return_acf_5": 0.27157527323340075,
        "abs_return_acf_20": 0.16495927657151313,
        "quantile_01": -0.04075734991626212,
        "quantile_99": 0.044263032457527676,
        "hill_tail_index": 4.2018267665086455
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01896979712091146,
        "excess_kurtosis": 8.595868493647904,
        "return_acf_1": -0.09515825395291629,
        "abs_return_acf_1": 0.2999039565282596,
        "abs_return_acf_5": 0.3251054503030859,
        "abs_return_acf_20": 0.20038082497250023,
        "quantile_01": -0.05165124643880654,
        "quantile_99": 0.060629978420328336,
        "hill_tail_index": 2.698330053035191
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01619390923982296,
        "excess_kurtosis": 0.943118959503598,
        "return_acf_1": -0.09771472954201911,
        "abs_return_acf_1": 0.1268926125742697,
        "abs_return_acf_5": 0.1227602835919373,
        "abs_return_acf_20": 0.16895154036798218,
        "quantile_01": -0.039328220738898544,
        "quantile_99": 0.042476899309132204,
        "hill_tail_index": 5.4316511861832995
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018358357200738928,
        "excess_kurtosis": 3.304332152523524,
        "return_acf_1": -0.09786047276504584,
        "abs_return_acf_1": 0.33447298579123297,
        "abs_return_acf_5": 0.31821945016294784,
        "abs_return_acf_20": 0.24738075914734625,
        "quantile_01": -0.0500492010940251,
        "quantile_99": 0.057191086975077424,
        "hill_tail_index": 4.038596436156957
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018409398975929175,
        "excess_kurtosis": 5.44306227559969,
        "return_acf_1": -0.15743570041401575,
        "abs_return_acf_1": 0.30567486117157544,
        "abs_return_acf_5": 0.32117408074725523,
        "abs_return_acf_20": 0.26904698001094607,
        "quantile_01": -0.049824949158606496,
        "quantile_99": 0.0581228221500352,
        "hill_tail_index": 3.4899150379883985
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016585656341698306,
        "excess_kurtosis": 2.983616629544616,
        "return_acf_1": -0.13137407782357952,
        "abs_return_acf_1": 0.2722532144656668,
        "abs_return_acf_5": 0.16445684305691147,
        "abs_return_acf_20": 0.15232519877251532,
        "quantile_01": -0.0437207497511749,
        "quantile_99": 0.04470946917216199,
        "hill_tail_index": 3.6581780519293994
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019206495522177826,
        "excess_kurtosis": 7.945684728004705,
        "return_acf_1": -0.07907971141304675,
        "abs_return_acf_1": 0.30946762374676834,
        "abs_return_acf_5": 0.29433521572020455,
        "abs_return_acf_20": 0.24187894968821788,
        "quantile_01": -0.05585803314387339,
        "quantile_99": 0.06178984249021424,
        "hill_tail_index": 2.763400253146188
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0166066157760875,
        "excess_kurtosis": 8.34573524005772,
        "return_acf_1": -0.17371903783821105,
        "abs_return_acf_1": 0.3414045590758448,
        "abs_return_acf_5": 0.2273722664707992,
        "abs_return_acf_20": 0.24939913499462144,
        "quantile_01": -0.04002229292387452,
        "quantile_99": 0.05320100735618407,
        "hill_tail_index": 2.0814506180903574
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017701023020519496,
        "excess_kurtosis": 7.853024671770502,
        "return_acf_1": -0.08443664477019966,
        "abs_return_acf_1": 0.2618381929805061,
        "abs_return_acf_5": 0.25729838180758313,
        "abs_return_acf_20": 0.21752382622116015,
        "quantile_01": -0.04216587902261952,
        "quantile_99": 0.04786117089529166,
        "hill_tail_index": 3.2178164882895737
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017783542976242288,
        "excess_kurtosis": 3.935999452674399,
        "return_acf_1": -0.08741993536748185,
        "abs_return_acf_1": 0.3000510092757201,
        "abs_return_acf_5": 0.28692204855297454,
        "abs_return_acf_20": 0.2600103831334957,
        "quantile_01": -0.04966973661625967,
        "quantile_99": 0.04823975583893101,
        "hill_tail_index": 3.6797662226614696
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.014728741700745914,
        "excess_kurtosis": 3.8946566637438336,
        "return_acf_1": -0.1302266621513812,
        "abs_return_acf_1": 0.23145550355637726,
        "abs_return_acf_5": 0.2684841242619053,
        "abs_return_acf_20": 0.16672476319007715,
        "quantile_01": -0.03453153164988781,
        "quantile_99": 0.03638614632183376,
        "hill_tail_index": 2.9998405439345244
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017801718937915992,
        "excess_kurtosis": 3.5661574584413707,
        "return_acf_1": -0.14598977132741023,
        "abs_return_acf_1": 0.2850646830975507,
        "abs_return_acf_5": 0.28908349157429997,
        "abs_return_acf_20": 0.2704497305483375,
        "quantile_01": -0.05598443132584754,
        "quantile_99": 0.046915673106120465,
        "hill_tail_index": 3.6341102474737252
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020836786660391838,
        "excess_kurtosis": 7.280898262697004,
        "return_acf_1": -0.10859725639390534,
        "abs_return_acf_1": 0.367480952927936,
        "abs_return_acf_5": 0.4119924207769715,
        "abs_return_acf_20": 0.3244498888534119,
        "quantile_01": -0.06565330604125788,
        "quantile_99": 0.06194346005137073,
        "hill_tail_index": 3.347330645039814
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01646245698775577,
        "excess_kurtosis": 6.226110096307719,
        "return_acf_1": -0.12218009353444022,
        "abs_return_acf_1": 0.32621915801080276,
        "abs_return_acf_5": 0.2631709205069441,
        "abs_return_acf_20": 0.2828428975409993,
        "quantile_01": -0.04534922734140223,
        "quantile_99": 0.05206923688123762,
        "hill_tail_index": 2.7915971584527037
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01971761715422131,
        "excess_kurtosis": 5.994148647497013,
        "return_acf_1": -0.07663449152185552,
        "abs_return_acf_1": 0.34380300735819674,
        "abs_return_acf_5": 0.36647602723600886,
        "abs_return_acf_20": 0.2995121229001329,
        "quantile_01": -0.06859465087497262,
        "quantile_99": 0.05424861964126674,
        "hill_tail_index": 3.0741610045668954
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019523740328764968,
        "excess_kurtosis": 8.363501277451805,
        "return_acf_1": -0.05753956585031834,
        "abs_return_acf_1": 0.3960916090617542,
        "abs_return_acf_5": 0.43015256192450935,
        "abs_return_acf_20": 0.33583016951019884,
        "quantile_01": -0.06510011393337645,
        "quantile_99": 0.06048326405406889,
        "hill_tail_index": 3.626655039684461
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01788518867760146,
        "excess_kurtosis": 6.209352100399702,
        "return_acf_1": -0.05168225455097248,
        "abs_return_acf_1": 0.20947435410962334,
        "abs_return_acf_5": 0.3274202863247683,
        "abs_return_acf_20": 0.31853980387931463,
        "quantile_01": -0.052438842254133214,
        "quantile_99": 0.052009090217734165,
        "hill_tail_index": 3.5790629761852175
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01757525935495027,
        "excess_kurtosis": 2.000312800076143,
        "return_acf_1": -0.14141080108949938,
        "abs_return_acf_1": 0.22872657854945974,
        "abs_return_acf_5": 0.24548747925113176,
        "abs_return_acf_20": 0.20266250461498836,
        "quantile_01": -0.047609143690503807,
        "quantile_99": 0.04468293487910605,
        "hill_tail_index": 4.390250210202072
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017731588605144063,
        "excess_kurtosis": 4.945164261411975,
        "return_acf_1": -0.1754573584518076,
        "abs_return_acf_1": 0.3295122634070016,
        "abs_return_acf_5": 0.30775283680047744,
        "abs_return_acf_20": 0.24429491399810654,
        "quantile_01": -0.04924762786487622,
        "quantile_99": 0.05361402028827179,
        "hill_tail_index": 3.814248645391292
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021752059448115577,
        "excess_kurtosis": 8.038728142555298,
        "return_acf_1": -0.14553867727824757,
        "abs_return_acf_1": 0.402457650471887,
        "abs_return_acf_5": 0.43016935326117306,
        "abs_return_acf_20": 0.27243186018514964,
        "quantile_01": -0.07745096159863293,
        "quantile_99": 0.0652459081391579,
        "hill_tail_index": 3.183446936840048
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02152236981696447,
        "excess_kurtosis": 16.351592034232517,
        "return_acf_1": -0.02015547617366312,
        "abs_return_acf_1": 0.3363450680180755,
        "abs_return_acf_5": 0.4422478906871453,
        "abs_return_acf_20": 0.3306219965676597,
        "quantile_01": -0.06523930348795881,
        "quantile_99": 0.059959469652765385,
        "hill_tail_index": 2.7172564894915756
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0173494074185492,
        "excess_kurtosis": 5.366575907223927,
        "return_acf_1": -0.06529238316020008,
        "abs_return_acf_1": 0.24801041135853039,
        "abs_return_acf_5": 0.2264546754408122,
        "abs_return_acf_20": 0.21785885445761735,
        "quantile_01": -0.05127945700334429,
        "quantile_99": 0.05221584345690877,
        "hill_tail_index": 2.8184421585136366
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01816206432985848,
        "excess_kurtosis": 3.451532852326264,
        "return_acf_1": -0.1396736607329986,
        "abs_return_acf_1": 0.3529839032302547,
        "abs_return_acf_5": 0.36352650846692847,
        "abs_return_acf_20": 0.2912744116408231,
        "quantile_01": -0.04602206130298389,
        "quantile_99": 0.049985190753286855,
        "hill_tail_index": 3.874146956672708
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
