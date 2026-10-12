# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27187
Run ID: `cbc5998f73bdc86cbabda5f6ac1a7001dbe7c4800d1f94c40baf3df86ab3b904`
Result fingerprint: `1ff0c44f3f4f108f870da91ca3aec5cc1ba406e7d08730ace392c01b70979f1d`

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
    "equal_weight_sd": -0.7977142857142826,
    "equal_weight_raw": -11.965714285714238,
    "fixed_start_cap_weight_sd": -0.8272129993430245,
    "fixed_start_cap_weight_raw": -12.408194990145375,
    "end_cap_weight_sd": -0.8318492819041174,
    "end_cap_weight_raw": -12.477739228561763
  },
  "full_period_change": {
    "equal_weight_sd": -1.2113214285714236,
    "equal_weight_raw": -18.169821428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1413022486772442,
    "inflation_mean_sd": 0.5720568783068783
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1546666666666698,
    "equal_weight_raw": 2.3200000000000474,
    "fixed_start_cap_weight_sd": 0.12516795303792722,
    "fixed_start_cap_weight_raw": 1.877519295568908,
    "end_cap_weight_sd": 0.12053167047683508,
    "end_cap_weight_raw": 1.8079750571525266
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8573809523809491,
      "change_raw": -12.860714285714238,
      "decay_adjusted_gain_sd": 0.0950000000000032
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8296031746031715,
      "change_raw": -12.444047619047572,
      "decay_adjusted_gain_sd": 0.12277777777778086
    },
    "small": {
      "count": 18,
      "change_sd": -0.7718253968253936,
      "change_raw": -11.577380952380905,
      "decay_adjusted_gain_sd": 0.1805555555555587
    },
    "large_minus_small_sd": -0.0855555555555555,
    "large_minus_small_raw": -1.2833333333333323
  },
  "inflation": {
    "initial_mean_sd": 0.3816666666666666,
    "final_mean_sd": 0.6250833333333333,
    "mean_sd": 0.49245496808215367,
    "mean_absolute_raw_gap": 7.386824521232306,
    "final_absolute_raw_gap": 9.376249999999999,
    "mean_range_fraction": 0.07386824521232306
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.32,
    "initial_wealth_share": 0.19535139647309208,
    "final_wealth_share": 0.31403680981017473
  },
  "pricing_slope": {
    "mean": 2.9954095728990366e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.03393663985750884,
    "real_improvement_cost": 0.023741475006331367,
    "washing_cost": 0.010195164851177465,
    "fine_transfer": 0.05451175948923313,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08844839934674198,
    "resource_cost_fraction_initial_cap": 0.0011312213285836284,
    "private_net_outflow_fraction_initial_cap": 0.0029482799782247337,
    "fine_transfer_fraction_initial_cap": 0.001817058649641105,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005908435321012417,
    "unapplied_final_day_resource_cost": 0.0017011392294917329
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 136.72538057634029,
    "beneficial_raw_gain_per_resource_cost": 2050.8807086451043,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 2.9209451100974757,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.05524536609299993,
    "accrued_cost_fraction_initial_cap": 0.09736483700324923,
    "mean_contract_rate": 0.04048437168998603,
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
    "maximum_relative_cash_error": 1.1143193199971817e-15,
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
      "minimum": -0.2521531579666179,
      "maximum": -0.029945702109186297,
      "mean": -0.14319681829794134,
      "median": -0.1348401293988648,
      "quantile_05": -0.23032569880973905,
      "quantile_95": -0.06045868420800717
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
      "minimum": 0.24650394862555958,
      "maximum": 0.7869299242627287,
      "mean": 0.46446177786260484,
      "median": 0.4466943598301641,
      "quantile_05": 0.28207087373529427,
      "quantile_95": 0.7112586322363035
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
        "daily_volatility": 0.021670969917237343,
        "excess_kurtosis": 22.915725212101623,
        "return_acf_1": -0.21946601580516445,
        "abs_return_acf_1": 0.5191126936985433,
        "abs_return_acf_5": 0.4354946330988502,
        "abs_return_acf_20": 0.27388011947946794,
        "quantile_01": -0.06311279133164197,
        "quantile_99": 0.04867355082561568,
        "hill_tail_index": 1.8481434750410335
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.018581885823152903,
        "excess_kurtosis": 4.204453777261691,
        "return_acf_1": -0.12322833785225133,
        "abs_return_acf_1": 0.34152612848075126,
        "abs_return_acf_5": 0.28245543776196025,
        "abs_return_acf_20": 0.31032414579861517,
        "quantile_01": -0.05497192535783095,
        "quantile_99": 0.053074909460148055,
        "hill_tail_index": 3.840689661464055
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021904333531533756,
        "excess_kurtosis": 18.19199506437374,
        "return_acf_1": -0.22990445524843203,
        "abs_return_acf_1": 0.470770889174099,
        "abs_return_acf_5": 0.44047577303162033,
        "abs_return_acf_20": 0.23917808781726466,
        "quantile_01": -0.07160333856180276,
        "quantile_99": 0.06338546577377076,
        "hill_tail_index": 2.7138777479971354
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019351557968801694,
        "excess_kurtosis": 6.270181327245643,
        "return_acf_1": -0.12373027767761392,
        "abs_return_acf_1": 0.36050791321952524,
        "abs_return_acf_5": 0.28975906137275526,
        "abs_return_acf_20": 0.34071590825175607,
        "quantile_01": -0.05951156545753757,
        "quantile_99": 0.055580077113858886,
        "hill_tail_index": 3.792771105283126
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01727441655389209,
        "excess_kurtosis": 4.028697573148089,
        "return_acf_1": -0.11442316294788561,
        "abs_return_acf_1": 0.2980342033782715,
        "abs_return_acf_5": 0.21450695610471565,
        "abs_return_acf_20": 0.19505925199984334,
        "quantile_01": -0.05162722585690216,
        "quantile_99": 0.048457355566453746,
        "hill_tail_index": 3.6052457672996208
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017745179857017984,
        "excess_kurtosis": 3.5821068368004703,
        "return_acf_1": -0.13888611933772413,
        "abs_return_acf_1": 0.29483959009046395,
        "abs_return_acf_5": 0.2049245790130133,
        "abs_return_acf_20": 0.18371387541599746,
        "quantile_01": -0.052330044422225816,
        "quantile_99": 0.05178473080525524,
        "hill_tail_index": 4.264148755841679
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.023359528709296255,
        "excess_kurtosis": 17.66844914524346,
        "return_acf_1": -0.205217150935663,
        "abs_return_acf_1": 0.4398588473027511,
        "abs_return_acf_5": 0.4485873312629892,
        "abs_return_acf_20": 0.36895500131244385,
        "quantile_01": -0.07292789250832869,
        "quantile_99": 0.06602338963892061,
        "hill_tail_index": 2.585435477485945
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018294488892314918,
        "excess_kurtosis": 4.777766525796569,
        "return_acf_1": -0.11078527054590484,
        "abs_return_acf_1": 0.2841618572212926,
        "abs_return_acf_5": 0.3694487473580593,
        "abs_return_acf_20": 0.26040722709510467,
        "quantile_01": -0.04986541725657622,
        "quantile_99": 0.05546169722495666,
        "hill_tail_index": 3.1348678092233793
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01741711823383544,
        "excess_kurtosis": 5.080625029118675,
        "return_acf_1": -0.11478271902841296,
        "abs_return_acf_1": 0.31575478160116277,
        "abs_return_acf_5": 0.26019618311778314,
        "abs_return_acf_20": 0.1824287717563343,
        "quantile_01": -0.0495847677135731,
        "quantile_99": 0.0525919333739814,
        "hill_tail_index": 4.083962531267573
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01778541840000979,
        "excess_kurtosis": 5.903921667199766,
        "return_acf_1": -0.12062825609516283,
        "abs_return_acf_1": 0.30726771898534555,
        "abs_return_acf_5": 0.28848757702959565,
        "abs_return_acf_20": 0.26089714473127706,
        "quantile_01": -0.05166825008626018,
        "quantile_99": 0.04299643715995794,
        "hill_tail_index": 2.871144081896984
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022996294955030104,
        "excess_kurtosis": 12.308628713822037,
        "return_acf_1": -0.21897831281845467,
        "abs_return_acf_1": 0.4627076616090215,
        "abs_return_acf_5": 0.3826757806120147,
        "abs_return_acf_20": 0.28383552899508224,
        "quantile_01": -0.06660759160683614,
        "quantile_99": 0.06976571751739706,
        "hill_tail_index": 2.6726007403761103
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02400262985169727,
        "excess_kurtosis": 16.55042339489857,
        "return_acf_1": -0.20810642077311423,
        "abs_return_acf_1": 0.47609722784988556,
        "abs_return_acf_5": 0.4194074614043643,
        "abs_return_acf_20": 0.23846183033108276,
        "quantile_01": -0.06539480945175044,
        "quantile_99": 0.06665385815241845,
        "hill_tail_index": 2.814871895940378
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019138773059900742,
        "excess_kurtosis": 6.7901140137159235,
        "return_acf_1": -0.14541134419302346,
        "abs_return_acf_1": 0.31111019677780216,
        "abs_return_acf_5": 0.2700801346731191,
        "abs_return_acf_20": 0.17723961643655167,
        "quantile_01": -0.060392890113549605,
        "quantile_99": 0.05133924345881615,
        "hill_tail_index": 3.4871392445711953
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022991138979662096,
        "excess_kurtosis": 13.473944760290564,
        "return_acf_1": -0.19479126855853138,
        "abs_return_acf_1": 0.4749882730525802,
        "abs_return_acf_5": 0.45117299822391255,
        "abs_return_acf_20": 0.3133345696294405,
        "quantile_01": -0.0727041825970701,
        "quantile_99": 0.08700263253088097,
        "hill_tail_index": 3.0571309170753147
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018316105348983786,
        "excess_kurtosis": 3.8878365773097174,
        "return_acf_1": -0.12934672169633835,
        "abs_return_acf_1": 0.3137935705770909,
        "abs_return_acf_5": 0.2689050009540589,
        "abs_return_acf_20": 0.25334254415837293,
        "quantile_01": -0.05966413224676993,
        "quantile_99": 0.05319564441748637,
        "hill_tail_index": 4.494054878597437
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016591062849470185,
        "excess_kurtosis": 4.356586291074448,
        "return_acf_1": -0.029945702109186297,
        "abs_return_acf_1": 0.3200994658163094,
        "abs_return_acf_5": 0.27751748247295005,
        "abs_return_acf_20": 0.2589648821486256,
        "quantile_01": -0.04719608102059141,
        "quantile_99": 0.05154037678592076,
        "hill_tail_index": 4.095783735250931
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019376131448241178,
        "excess_kurtosis": 10.340173415557382,
        "return_acf_1": -0.1343103091544913,
        "abs_return_acf_1": 0.44592024246156226,
        "abs_return_acf_5": 0.41574812575782305,
        "abs_return_acf_20": 0.3087767152299687,
        "quantile_01": -0.0643547462616379,
        "quantile_99": 0.053047523495047655,
        "hill_tail_index": 3.0233588912982454
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017313005504406925,
        "excess_kurtosis": 3.301043156101387,
        "return_acf_1": -0.08732396132392165,
        "abs_return_acf_1": 0.22073053617494645,
        "abs_return_acf_5": 0.232227654325085,
        "abs_return_acf_20": 0.2009061081278892,
        "quantile_01": -0.04566385710830917,
        "quantile_99": 0.047336561663617625,
        "hill_tail_index": 4.031904677262219
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01921922271249723,
        "excess_kurtosis": 11.497815658588436,
        "return_acf_1": -0.13673317574558175,
        "abs_return_acf_1": 0.4157641194903289,
        "abs_return_acf_5": 0.3666173731702746,
        "abs_return_acf_20": 0.2181550041811604,
        "quantile_01": -0.06133765697302171,
        "quantile_99": 0.05198250198586819,
        "hill_tail_index": 2.6259011107557177
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020961650132381313,
        "excess_kurtosis": 9.55307772370845,
        "return_acf_1": -0.06017695931805721,
        "abs_return_acf_1": 0.4678349561865182,
        "abs_return_acf_5": 0.39747329772173823,
        "abs_return_acf_20": 0.3602029618398317,
        "quantile_01": -0.07018032014660867,
        "quantile_99": 0.06285572843949705,
        "hill_tail_index": 2.6174899196603225
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017360590726896618,
        "excess_kurtosis": 2.486246373077198,
        "return_acf_1": -0.08274480300725055,
        "abs_return_acf_1": 0.21824379362166213,
        "abs_return_acf_5": 0.31599112687986214,
        "abs_return_acf_20": 0.1905442204135855,
        "quantile_01": -0.048322081540733954,
        "quantile_99": 0.04470093005489264,
        "hill_tail_index": 4.057220429615259
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021712737159719567,
        "excess_kurtosis": 18.12067188810553,
        "return_acf_1": -0.23067035263262659,
        "abs_return_acf_1": 0.4663206387255046,
        "abs_return_acf_5": 0.4502552318929378,
        "abs_return_acf_20": 0.36868132675131793,
        "quantile_01": -0.06058059708466623,
        "quantile_99": 0.062490308872624606,
        "hill_tail_index": 2.3277032590832065
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01768434352957924,
        "excess_kurtosis": 8.052833347150596,
        "return_acf_1": -0.07660971514841296,
        "abs_return_acf_1": 0.29212766075741753,
        "abs_return_acf_5": 0.3365026426086694,
        "abs_return_acf_20": 0.27900634472141134,
        "quantile_01": -0.06158163786925623,
        "quantile_99": 0.043328356188832136,
        "hill_tail_index": 2.5756074486071583
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0227693807452667,
        "excess_kurtosis": 5.7597746375547345,
        "return_acf_1": -0.18611089400257447,
        "abs_return_acf_1": 0.3919270361502948,
        "abs_return_acf_5": 0.39346759288467453,
        "abs_return_acf_20": 0.2921595439747293,
        "quantile_01": -0.06761800916120059,
        "quantile_99": 0.06643576496390943,
        "hill_tail_index": 3.936732020038232
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017642999427027132,
        "excess_kurtosis": 5.601088731354142,
        "return_acf_1": -0.06080301462905712,
        "abs_return_acf_1": 0.2524153987098011,
        "abs_return_acf_5": 0.36510038134720557,
        "abs_return_acf_20": 0.23265124953988264,
        "quantile_01": -0.048831378168898404,
        "quantile_99": 0.048463893259151215,
        "hill_tail_index": 3.130547680116083
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02043354906569403,
        "excess_kurtosis": 11.2051409519457,
        "return_acf_1": -0.1556634727996834,
        "abs_return_acf_1": 0.40791771131530896,
        "abs_return_acf_5": 0.4200688759991976,
        "abs_return_acf_20": 0.33138148215797314,
        "quantile_01": -0.06933360542782774,
        "quantile_99": 0.05785458952805448,
        "hill_tail_index": 2.945232469749834
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022425857235537007,
        "excess_kurtosis": 16.3191111094964,
        "return_acf_1": -0.2041979103613029,
        "abs_return_acf_1": 0.4217342939242458,
        "abs_return_acf_5": 0.4002921758108589,
        "abs_return_acf_20": 0.2538993867164614,
        "quantile_01": -0.06693949134639536,
        "quantile_99": 0.05983208126699836,
        "hill_tail_index": 2.2762048884564847
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.022219405359534965,
        "excess_kurtosis": 23.176418026122725,
        "return_acf_1": -0.2521531579666179,
        "abs_return_acf_1": 0.3720416816206541,
        "abs_return_acf_5": 0.40257381747276444,
        "abs_return_acf_20": 0.3092635686338931,
        "quantile_01": -0.06574169538913396,
        "quantile_99": 0.06267572114685276,
        "hill_tail_index": 2.379600827864149
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018209769259233,
        "excess_kurtosis": 6.734186899298617,
        "return_acf_1": -0.06540533758256036,
        "abs_return_acf_1": 0.31788109371487644,
        "abs_return_acf_5": 0.23896545518993748,
        "abs_return_acf_20": 0.21119002634302217,
        "quantile_01": -0.05435928369675061,
        "quantile_99": 0.048366217498929526,
        "hill_tail_index": 2.879772033699818
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0183446628748281,
        "excess_kurtosis": 7.0698843801408024,
        "return_acf_1": -0.13536994964323834,
        "abs_return_acf_1": 0.2812077457869997,
        "abs_return_acf_5": 0.22881849302569995,
        "abs_return_acf_20": 0.17433936939703665,
        "quantile_01": -0.05519966712606122,
        "quantile_99": 0.04897081617338486,
        "hill_tail_index": 3.9564660321294793
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
