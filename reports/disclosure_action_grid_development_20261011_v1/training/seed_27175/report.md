# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27175
Run ID: `c5a88aa449664fef68f0746eed7f2760d88c2cc70f47228d7acae268ed3a35ac`
Result fingerprint: `c94cce03dadb565cc78d8fce56e32aca4c881626f7aab3649017263c916cdaf6`

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
    "equal_weight_sd": -0.7132142857142825,
    "equal_weight_raw": -10.698214285714238,
    "fixed_start_cap_weight_sd": -0.7154944944718172,
    "fixed_start_cap_weight_raw": -10.732417417077258,
    "end_cap_weight_sd": -0.7076340183499663,
    "end_cap_weight_raw": -10.614510275249495
  },
  "full_period_change": {
    "equal_weight_sd": -1.1139880952380905,
    "equal_weight_raw": -16.709821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.03011276455026,
    "inflation_mean_sd": 0.8403928571428573
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.23916666666666983,
    "equal_weight_raw": 3.5875000000000483,
    "fixed_start_cap_weight_sd": 0.23688645790913518,
    "fixed_start_cap_weight_raw": 3.553296868637029,
    "end_cap_weight_sd": 0.2447469340309859,
    "end_cap_weight_raw": 3.671204010464789
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7457142857142826,
      "change_raw": -11.185714285714239,
      "decay_adjusted_gain_sd": 0.20666666666666988
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6290476190476157,
      "change_raw": -9.435714285714237,
      "decay_adjusted_gain_sd": 0.3233333333333365
    },
    "small": {
      "count": 18,
      "change_sd": -0.7498809523809492,
      "change_raw": -11.248214285714239,
      "decay_adjusted_gain_sd": 0.20250000000000315
    },
    "large_minus_small_sd": 0.004166666666666652,
    "large_minus_small_raw": 0.06249999999999978
  },
  "inflation": {
    "initial_mean_sd": 0.46675000000000005,
    "final_mean_sd": 0.8638333333333332,
    "mean_sd": 0.6888777407715793,
    "mean_absolute_raw_gap": 10.33316611157369,
    "final_absolute_raw_gap": 12.957500000000001,
    "mean_range_fraction": 0.1033316611157369
  },
  "impact": {
    "initial_share": 0.31333333333333335,
    "final_share": 0.3466666666666667,
    "initial_wealth_share": 0.36922496618995637,
    "final_wealth_share": 0.4019634530418515
  },
  "pricing_slope": {
    "mean": -0.0006126891042863068,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.08005148609543343,
    "real_improvement_cost": 0.0475519410566277,
    "washing_cost": 0.03249954503880571,
    "fine_transfer": 0.03917105689399453,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.11922254298942796,
    "resource_cost_fraction_initial_cap": 0.0026683828698477806,
    "private_net_outflow_fraction_initial_cap": 0.003974084766314265,
    "fine_transfer_fraction_initial_cap": 0.001305701896466484,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005720534589975917,
    "unapplied_final_day_resource_cost": 0.0014100785557068021
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 89.62981638400085,
    "beneficial_raw_gain_per_resource_cost": 1344.4472457600127,
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
    "accrued_cost": 2.860639559998156,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.11555091619232064,
    "accrued_cost_fraction_initial_cap": 0.09535465199993852,
    "mean_contract_rate": 0.039727154503394764,
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
    "maximum_relative_cash_error": 2.1540299902867095e-15,
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
      "minimum": -0.22097042937602807,
      "maximum": -0.04450848497447033,
      "mean": -0.13514517060302678,
      "median": -0.12433047926425124,
      "quantile_05": -0.21856625140828195,
      "quantile_95": -0.06610763862060451
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
      "minimum": 0.30544443480557276,
      "maximum": 0.7782702783132726,
      "mean": 0.5311820810688483,
      "median": 0.5321604967044594,
      "quantile_05": 0.3485523087362067,
      "quantile_95": 0.7262145715954799
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
        "daily_volatility": 0.019860479366005608,
        "excess_kurtosis": 19.287475310212773,
        "return_acf_1": -0.1324984790439811,
        "abs_return_acf_1": 0.3680448551064851,
        "abs_return_acf_5": 0.2773825664790407,
        "abs_return_acf_20": 0.2123058606060308,
        "quantile_01": -0.053788767171817686,
        "quantile_99": 0.046191579060344656,
        "hill_tail_index": 2.264286368771652
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01787022920386195,
        "excess_kurtosis": 11.209304570218265,
        "return_acf_1": -0.1246649833322286,
        "abs_return_acf_1": 0.40686061003055163,
        "abs_return_acf_5": 0.3129116945044735,
        "abs_return_acf_20": 0.27178922351214907,
        "quantile_01": -0.05360840568252517,
        "quantile_99": 0.04529881792837208,
        "hill_tail_index": 2.6077794056658283
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016927179698571,
        "excess_kurtosis": 10.617874027945586,
        "return_acf_1": -0.11182526224885979,
        "abs_return_acf_1": 0.3858266424022046,
        "abs_return_acf_5": 0.3181956415396872,
        "abs_return_acf_20": 0.18249730672562475,
        "quantile_01": -0.054136957666996846,
        "quantile_99": 0.03902906047930194,
        "hill_tail_index": 2.0805463140378526
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01945466680595737,
        "excess_kurtosis": 13.56859139925265,
        "return_acf_1": -0.1849709955972664,
        "abs_return_acf_1": 0.3541698220318996,
        "abs_return_acf_5": 0.31084510206790195,
        "abs_return_acf_20": 0.2454615434938786,
        "quantile_01": -0.06335927797430846,
        "quantile_99": 0.051938655037773285,
        "hill_tail_index": 2.285886443059445
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022061026375237713,
        "excess_kurtosis": 15.243417713750915,
        "return_acf_1": -0.22097042937602807,
        "abs_return_acf_1": 0.48013633763196195,
        "abs_return_acf_5": 0.4090758637800591,
        "abs_return_acf_20": 0.3190269401696687,
        "quantile_01": -0.07101487420159293,
        "quantile_99": 0.06018424955874003,
        "hill_tail_index": 2.273751832325588
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019425164480156062,
        "excess_kurtosis": 7.687586866479144,
        "return_acf_1": -0.061439063420320454,
        "abs_return_acf_1": 0.41216347631631955,
        "abs_return_acf_5": 0.29973152311694473,
        "abs_return_acf_20": 0.23185430967186668,
        "quantile_01": -0.06462567614259294,
        "quantile_99": 0.0516452418195351,
        "hill_tail_index": 2.8316499919627214
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019025582264430435,
        "excess_kurtosis": 11.980418621743526,
        "return_acf_1": -0.11457494796779905,
        "abs_return_acf_1": 0.4145070358814269,
        "abs_return_acf_5": 0.32457836134604096,
        "abs_return_acf_20": 0.22149399893810628,
        "quantile_01": -0.05338126562010602,
        "quantile_99": 0.06215214377309652,
        "hill_tail_index": 2.597596806171836
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.017169504096427698,
        "excess_kurtosis": 8.51897462088318,
        "return_acf_1": -0.1698579716982394,
        "abs_return_acf_1": 0.3069532934288551,
        "abs_return_acf_5": 0.26271018893878645,
        "abs_return_acf_20": 0.1706820095646015,
        "quantile_01": -0.049608434908801596,
        "quantile_99": 0.04683482623520118,
        "hill_tail_index": 2.414635976565472
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01683067500622282,
        "excess_kurtosis": 4.651393076878004,
        "return_acf_1": -0.11545846897652426,
        "abs_return_acf_1": 0.27713674318777953,
        "abs_return_acf_5": 0.22959511107628686,
        "abs_return_acf_20": 0.20101345079430336,
        "quantile_01": -0.049653912775915916,
        "quantile_99": 0.04748818512702732,
        "hill_tail_index": 3.4262030115633024
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016779110140531413,
        "excess_kurtosis": 13.024768257603899,
        "return_acf_1": -0.1084078462732644,
        "abs_return_acf_1": 0.46867963172596705,
        "abs_return_acf_5": 0.3683502929521616,
        "abs_return_acf_20": 0.22575543004623028,
        "quantile_01": -0.048477236111652916,
        "quantile_99": 0.04193211714088005,
        "hill_tail_index": 2.4509276838771505
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018313742309307886,
        "excess_kurtosis": 5.401013225129489,
        "return_acf_1": -0.13617266463360603,
        "abs_return_acf_1": 0.3801045359260061,
        "abs_return_acf_5": 0.3219973989389666,
        "abs_return_acf_20": 0.1894077288238591,
        "quantile_01": -0.05543466160259225,
        "quantile_99": 0.047038155361444,
        "hill_tail_index": 3.3030910933754396
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01949252999777368,
        "excess_kurtosis": 6.767705853172442,
        "return_acf_1": -0.11263710190493538,
        "abs_return_acf_1": 0.28978766804875356,
        "abs_return_acf_5": 0.3201921412667355,
        "abs_return_acf_20": 0.23467459766825954,
        "quantile_01": -0.06146488166801021,
        "quantile_99": 0.05168964756903276,
        "hill_tail_index": 3.808735521679713
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017179337864139492,
        "excess_kurtosis": 1.5538768821225997,
        "return_acf_1": -0.12984974499986013,
        "abs_return_acf_1": 0.17952549257539147,
        "abs_return_acf_5": 0.18340066090860457,
        "abs_return_acf_20": 0.20069641186736095,
        "quantile_01": -0.04462942714555603,
        "quantile_99": 0.04700266813604286,
        "hill_tail_index": 5.8815103880700255
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017960596569769633,
        "excess_kurtosis": 5.5422546652688585,
        "return_acf_1": -0.11913717537208718,
        "abs_return_acf_1": 0.34223721813962465,
        "abs_return_acf_5": 0.24119394013943238,
        "abs_return_acf_20": 0.14519334677027204,
        "quantile_01": -0.061459763601097415,
        "quantile_99": 0.05141181553129508,
        "hill_tail_index": 3.446308917442086
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018433756852077963,
        "excess_kurtosis": 11.018161669992775,
        "return_acf_1": -0.17131437150519113,
        "abs_return_acf_1": 0.360675732110166,
        "abs_return_acf_5": 0.34251165887976126,
        "abs_return_acf_20": 0.27597302444611044,
        "quantile_01": -0.05835608436561677,
        "quantile_99": 0.05351790684740752,
        "hill_tail_index": 2.219398301189397
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.018793411496931936,
        "excess_kurtosis": 5.472253276816623,
        "return_acf_1": -0.19581227940405657,
        "abs_return_acf_1": 0.28951460972718274,
        "abs_return_acf_5": 0.2852108756409546,
        "abs_return_acf_20": 0.15666383743145024,
        "quantile_01": -0.058088547076060024,
        "quantile_99": 0.04859040897292276,
        "hill_tail_index": 3.3394015796877694
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020353556897104455,
        "excess_kurtosis": 14.242284994608873,
        "return_acf_1": -0.08050074784615567,
        "abs_return_acf_1": 0.46946241000603156,
        "abs_return_acf_5": 0.35584418720780553,
        "abs_return_acf_20": 0.26810051058534906,
        "quantile_01": -0.08114478011754099,
        "quantile_99": 0.06268510741152226,
        "hill_tail_index": 2.417779708959344
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018850683430243046,
        "excess_kurtosis": 6.3365037679926015,
        "return_acf_1": -0.12399597519627388,
        "abs_return_acf_1": 0.3286088290729108,
        "abs_return_acf_5": 0.27980427936227226,
        "abs_return_acf_20": 0.1922216990874025,
        "quantile_01": -0.06123953013173268,
        "quantile_99": 0.05527098854031903,
        "hill_tail_index": 2.897626444815828
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018190047375276262,
        "excess_kurtosis": 14.412449798618752,
        "return_acf_1": -0.13634080539507742,
        "abs_return_acf_1": 0.36558135511045564,
        "abs_return_acf_5": 0.3219027672333322,
        "abs_return_acf_20": 0.19642646167216385,
        "quantile_01": -0.056163585884943266,
        "quantile_99": 0.04220246888024276,
        "hill_tail_index": 1.9748052955686815
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020705703309128742,
        "excess_kurtosis": 15.09145682804754,
        "return_acf_1": -0.1835097447460863,
        "abs_return_acf_1": 0.47924552835688894,
        "abs_return_acf_5": 0.47111593325998163,
        "abs_return_acf_20": 0.2785128079701131,
        "quantile_01": -0.07463573884744075,
        "quantile_99": 0.052566046636524484,
        "hill_tail_index": 2.2317901686537356
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021603283252254322,
        "excess_kurtosis": 14.844826144330295,
        "return_acf_1": -0.2194450711196017,
        "abs_return_acf_1": 0.38645279924842235,
        "abs_return_acf_5": 0.4308194181987295,
        "abs_return_acf_20": 0.3020087137461039,
        "quantile_01": -0.07025876091231413,
        "quantile_99": 0.05611154103626595,
        "hill_tail_index": 2.043480708470556
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019962366107736083,
        "excess_kurtosis": 6.8670510857648,
        "return_acf_1": -0.07181367497650719,
        "abs_return_acf_1": 0.4158055909839021,
        "abs_return_acf_5": 0.2890692915396045,
        "abs_return_acf_20": 0.2969577690136672,
        "quantile_01": -0.06459546413838127,
        "quantile_99": 0.06276482641289274,
        "hill_tail_index": 3.8672518527662163
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019961243246164335,
        "excess_kurtosis": 7.636130123937171,
        "return_acf_1": -0.12299058892192738,
        "abs_return_acf_1": 0.3023461873056469,
        "abs_return_acf_5": 0.31857914581716884,
        "abs_return_acf_20": 0.26339713164353157,
        "quantile_01": -0.06024444912188216,
        "quantile_99": 0.05755050960723296,
        "hill_tail_index": 3.251605892293101
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01748425531230518,
        "excess_kurtosis": 3.851802278213781,
        "return_acf_1": -0.08315983692740468,
        "abs_return_acf_1": 0.26877367694275506,
        "abs_return_acf_5": 0.27814674308672244,
        "abs_return_acf_20": 0.2062200256443366,
        "quantile_01": -0.054561578902129114,
        "quantile_99": 0.050622260534148145,
        "hill_tail_index": 3.9170327927125266
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020942108066049098,
        "excess_kurtosis": 18.33760877357529,
        "return_acf_1": -0.21749213842778004,
        "abs_return_acf_1": 0.4060796111374533,
        "abs_return_acf_5": 0.42794619571484915,
        "abs_return_acf_20": 0.27877233187486544,
        "quantile_01": -0.06383545333722325,
        "quantile_99": 0.06057790190529735,
        "hill_tail_index": 2.4309128400643596
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018510696077280755,
        "excess_kurtosis": 2.730003163594268,
        "return_acf_1": -0.15471618187158742,
        "abs_return_acf_1": 0.28511070204498573,
        "abs_return_acf_5": 0.23186341227865798,
        "abs_return_acf_20": 0.22392349173609385,
        "quantile_01": -0.0502670705288921,
        "quantile_99": 0.051474661929083475,
        "hill_tail_index": 5.009476599450123
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01942819659075699,
        "excess_kurtosis": 15.093299770838641,
        "return_acf_1": -0.19716019541343213,
        "abs_return_acf_1": 0.3489087290559037,
        "abs_return_acf_5": 0.35301691549890574,
        "abs_return_acf_20": 0.2772763411559878,
        "quantile_01": -0.06261254261279935,
        "quantile_99": 0.05276280409545459,
        "hill_tail_index": 2.619328959579251
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01807164511947105,
        "excess_kurtosis": 9.826542279334069,
        "return_acf_1": -0.04450848497447033,
        "abs_return_acf_1": 0.4566359793294957,
        "abs_return_acf_5": 0.35417963359719346,
        "abs_return_acf_20": 0.19227944876417366,
        "quantile_01": -0.05925836991383424,
        "quantile_99": 0.04382902322622013,
        "hill_tail_index": 2.414289566546954
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01958327652153919,
        "excess_kurtosis": 7.687836583128059,
        "return_acf_1": -0.12108021818555373,
        "abs_return_acf_1": 0.45850290718302567,
        "abs_return_acf_5": 0.3876315717124461,
        "abs_return_acf_20": 0.351591360826773,
        "quantile_01": -0.05588008342015032,
        "quantile_99": 0.04866395266414636,
        "hill_tail_index": 2.644611420920443
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01891441083806339,
        "excess_kurtosis": 16.56440005685583,
        "return_acf_1": -0.08804966833469638,
        "abs_return_acf_1": 0.46703040917965377,
        "abs_return_acf_5": 0.3904899597547684,
        "abs_return_acf_20": 0.20408512403581502,
        "quantile_01": -0.06622412007297929,
        "quantile_99": 0.04874871593043476,
        "hill_tail_index": 1.7811717052649327
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
