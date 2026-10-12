# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27016
Run ID: `65d85283b8f87fe8b39103a43f8bc83784848721ba6243f9d73bcd6b88a330de`
Result fingerprint: `8b913c302efa2872b810360890b7da92e562abe89945d4dc48cd2bd2b481bae1`

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
    "equal_weight_sd": -0.573638968575698,
    "equal_weight_raw": -8.604584528635463,
    "fixed_start_cap_weight_sd": -0.4951128034726507,
    "fixed_start_cap_weight_raw": -7.426692052089761,
    "end_cap_weight_sd": -0.5081128858837348,
    "end_cap_weight_raw": -7.6216932882560195
  },
  "full_period_change": {
    "equal_weight_sd": -0.8101627780995055,
    "equal_weight_raw": -12.152441671492584
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7336720839664616,
    "inflation_mean_sd": 0.6512073412698414
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3695000000000031,
    "equal_weight_raw": 5.542500000000047,
    "fixed_start_cap_weight_sd": 0.45469459827249,
    "fixed_start_cap_weight_raw": 6.820418974087351,
    "end_cap_weight_sd": 0.44198888908436385,
    "end_cap_weight_raw": 6.62983333626546
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.39988095238094923,
      "change_raw": -5.998214285714239,
      "decay_adjusted_gain_sd": 0.5525000000000031
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5979365079365047,
      "change_raw": -8.96904761904757,
      "decay_adjusted_gain_sd": 0.35444444444444767
    },
    "small": {
      "count": 18,
      "change_sd": -0.5904498682610857,
      "change_raw": -8.856748023916285,
      "decay_adjusted_gain_sd": 0.3465277777777809
    },
    "large_minus_small_sd": 0.19056891588013647,
    "large_minus_small_raw": 2.858533738202047
  },
  "inflation": {
    "initial_mean_sd": 0.20283333333333334,
    "final_mean_sd": 0.7190833333333336,
    "mean_sd": 0.437313974465723,
    "mean_absolute_raw_gap": 6.559709616985845,
    "final_absolute_raw_gap": 10.786250000000003,
    "mean_range_fraction": 0.06559709616985845
  },
  "impact": {
    "initial_share": 0.30666666666666664,
    "final_share": 0.37333333333333335,
    "initial_wealth_share": 0.2762509152730321,
    "final_wealth_share": 0.35918590527845423
  },
  "pricing_slope": {
    "mean": -0.0029943858083069054,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.19151724348800458,
    "real_improvement_cost": 0.15392945294492885,
    "washing_cost": 0.03758779054307572,
    "fine_transfer": 0.01646968899145341,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.207986932479458,
    "resource_cost_fraction_initial_cap": 0.006383908116266818,
    "private_net_outflow_fraction_initial_cap": 0.006932897749315265,
    "fine_transfer_fraction_initial_cap": 0.0005489896330484468,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.04496647492414392,
    "unapplied_final_day_resource_cost": 0.001364008834731177
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 57.87990573650036,
    "beneficial_raw_gain_per_resource_cost": 868.1985860475054,
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
    "accrued_cost": 3.088343206476357,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.11215273028588013,
    "accrued_cost_fraction_initial_cap": 0.10294477354921187,
    "mean_contract_rate": 0.04360851428731067,
    "maximum_ledger_error": 7.115076756936123e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 1.2218208061836034e-15,
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
      "minimum": -0.2195180744658128,
      "maximum": -0.0777950717996468,
      "mean": -0.13833758106162197,
      "median": -0.14298749306728648,
      "quantile_05": -0.2006986276322551,
      "quantile_95": -0.08329439638154959
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
      "minimum": 0.27616050339803105,
      "maximum": 0.8036822697898802,
      "mean": 0.5907273347309867,
      "median": 0.6411668764578454,
      "quantile_05": 0.33196866876091063,
      "quantile_95": 0.7718840036484979
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
        "daily_volatility": 0.02040678976144028,
        "excess_kurtosis": 7.305846746332296,
        "return_acf_1": -0.15233166809446816,
        "abs_return_acf_1": 0.3471144739751819,
        "abs_return_acf_5": 0.37636059660107896,
        "abs_return_acf_20": 0.2902813992788305,
        "quantile_01": -0.0698832377791008,
        "quantile_99": 0.054065991721029716,
        "hill_tail_index": 3.2426862765438207
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01641564692712002,
        "excess_kurtosis": 2.9254663584416427,
        "return_acf_1": -0.1919391224828178,
        "abs_return_acf_1": 0.17632519905810837,
        "abs_return_acf_5": 0.1801941900419581,
        "abs_return_acf_20": 0.15338241505082612,
        "quantile_01": -0.048420142861635554,
        "quantile_99": 0.04571740766463648,
        "hill_tail_index": 4.300222071757084
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022993042623581244,
        "excess_kurtosis": 8.527898110190387,
        "return_acf_1": -0.1732993763504438,
        "abs_return_acf_1": 0.47019935364521404,
        "abs_return_acf_5": 0.45802674339547733,
        "abs_return_acf_20": 0.41227463237567763,
        "quantile_01": -0.07017286863361813,
        "quantile_99": 0.07890026243602996,
        "hill_tail_index": 3.419167802692232
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022173497997441723,
        "excess_kurtosis": 6.883770947407259,
        "return_acf_1": -0.1430556263822784,
        "abs_return_acf_1": 0.4341398959344595,
        "abs_return_acf_5": 0.4386355507811437,
        "abs_return_acf_20": 0.3031576854629806,
        "quantile_01": -0.06539141027055226,
        "quantile_99": 0.06605033248674383,
        "hill_tail_index": 3.0545237567520274
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021967651201824905,
        "excess_kurtosis": 7.1532463958737065,
        "return_acf_1": -0.10826455829741784,
        "abs_return_acf_1": 0.4225657045720777,
        "abs_return_acf_5": 0.39028748680989106,
        "abs_return_acf_20": 0.34945795451955214,
        "quantile_01": -0.08686142709974916,
        "quantile_99": 0.05992838253787137,
        "hill_tail_index": 3.0698315963690392
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0203747937942127,
        "excess_kurtosis": 5.981674298823469,
        "return_acf_1": -0.16718735657694275,
        "abs_return_acf_1": 0.38703729841531787,
        "abs_return_acf_5": 0.40642528145217316,
        "abs_return_acf_20": 0.29479435371011,
        "quantile_01": -0.058607541642706665,
        "quantile_99": 0.05939295136090363,
        "hill_tail_index": 3.63851860359138
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022766191996797455,
        "excess_kurtosis": 8.380184348763635,
        "return_acf_1": -0.0864536535154045,
        "abs_return_acf_1": 0.4347704970178582,
        "abs_return_acf_5": 0.407148548867709,
        "abs_return_acf_20": 0.3205912796846584,
        "quantile_01": -0.07896599566494253,
        "quantile_99": 0.06748880071085517,
        "hill_tail_index": 3.2934929524318273
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021205640362934642,
        "excess_kurtosis": 9.407398158079447,
        "return_acf_1": -0.10433296568394933,
        "abs_return_acf_1": 0.4132827309527024,
        "abs_return_acf_5": 0.4403541750872976,
        "abs_return_acf_20": 0.24533571940469043,
        "quantile_01": -0.06973509887054312,
        "quantile_99": 0.054863138203316994,
        "hill_tail_index": 2.608934839221359
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02197520068475484,
        "excess_kurtosis": 7.276535813047378,
        "return_acf_1": -0.11796766099158382,
        "abs_return_acf_1": 0.4365751794426837,
        "abs_return_acf_5": 0.44655167738217916,
        "abs_return_acf_20": 0.32348334960797653,
        "quantile_01": -0.07792531692754943,
        "quantile_99": 0.06415181367835757,
        "hill_tail_index": 3.3105789078539716
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023627913700519254,
        "excess_kurtosis": 10.392896665264429,
        "return_acf_1": -0.18282037190254083,
        "abs_return_acf_1": 0.4388272694093244,
        "abs_return_acf_5": 0.4250368829951225,
        "abs_return_acf_20": 0.35320682990179636,
        "quantile_01": -0.08293601593756562,
        "quantile_99": 0.07900137683160073,
        "hill_tail_index": 4.0209844321600805
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01725443584697721,
        "excess_kurtosis": 4.511261442581455,
        "return_acf_1": -0.2195180744658128,
        "abs_return_acf_1": 0.3370481305596049,
        "abs_return_acf_5": 0.26415860786506534,
        "abs_return_acf_20": 0.17843598188966503,
        "quantile_01": -0.04945791705220867,
        "quantile_99": 0.04164328322913593,
        "hill_tail_index": 3.0154934198413694
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022071502214263006,
        "excess_kurtosis": 7.919340451486066,
        "return_acf_1": -0.14438069261911754,
        "abs_return_acf_1": 0.42249794382017175,
        "abs_return_acf_5": 0.4734854740002128,
        "abs_return_acf_20": 0.3656983843091087,
        "quantile_01": -0.0760018571284094,
        "quantile_99": 0.0681063385710089,
        "hill_tail_index": 3.5476819242360365
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021401273860289928,
        "excess_kurtosis": 6.49393597660627,
        "return_acf_1": -0.10964514135409922,
        "abs_return_acf_1": 0.43679322149534794,
        "abs_return_acf_5": 0.4450112937012093,
        "abs_return_acf_20": 0.35578282488945007,
        "quantile_01": -0.07387292926776426,
        "quantile_99": 0.06229620560145736,
        "hill_tail_index": 3.6237040584643956
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02060588230236017,
        "excess_kurtosis": 5.780681298062591,
        "return_acf_1": -0.0777950717996468,
        "abs_return_acf_1": 0.3935369505978112,
        "abs_return_acf_5": 0.3121630444095046,
        "abs_return_acf_20": 0.281028852518995,
        "quantile_01": -0.07494396228619545,
        "quantile_99": 0.05829624962309103,
        "hill_tail_index": 3.7074791022642932
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02190777531700775,
        "excess_kurtosis": 8.731374959411136,
        "return_acf_1": -0.149970570377407,
        "abs_return_acf_1": 0.4142963480750716,
        "abs_return_acf_5": 0.4343639388340526,
        "abs_return_acf_20": 0.24814346257459194,
        "quantile_01": -0.06856904664304157,
        "quantile_99": 0.08292269258097745,
        "hill_tail_index": 2.5066683330264494
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01906683200040484,
        "excess_kurtosis": 3.568637210774307,
        "return_acf_1": -0.11274362982281715,
        "abs_return_acf_1": 0.3258328941312802,
        "abs_return_acf_5": 0.21890877032496406,
        "abs_return_acf_20": 0.21455223440115512,
        "quantile_01": -0.060265640388225995,
        "quantile_99": 0.04706575234207987,
        "hill_tail_index": 3.2081204727244517
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.016779090322766567,
        "excess_kurtosis": 11.971646359212537,
        "return_acf_1": -0.16818728480465253,
        "abs_return_acf_1": 0.2607680339748021,
        "abs_return_acf_5": 0.19718392536900078,
        "abs_return_acf_20": 0.21088703348860643,
        "quantile_01": -0.04507615884988696,
        "quantile_99": 0.040388023905671894,
        "hill_tail_index": 2.8390227655323987
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02190524471160631,
        "excess_kurtosis": 7.959149408251681,
        "return_acf_1": -0.1115424946105086,
        "abs_return_acf_1": 0.4697552968471605,
        "abs_return_acf_5": 0.4482382873462984,
        "abs_return_acf_20": 0.32017034214377676,
        "quantile_01": -0.07991392575710571,
        "quantile_99": 0.06533145793996085,
        "hill_tail_index": 4.280070584812014
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01980407934136316,
        "excess_kurtosis": 4.880333166780539,
        "return_acf_1": -0.14034913465602983,
        "abs_return_acf_1": 0.40428157011264776,
        "abs_return_acf_5": 0.39738837943393,
        "abs_return_acf_20": 0.2964642319798346,
        "quantile_01": -0.06392971773044868,
        "quantile_99": 0.05665262621764416,
        "hill_tail_index": 4.4855896432037685
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022433613824458375,
        "excess_kurtosis": 6.280062748260468,
        "return_acf_1": -0.15500627678044024,
        "abs_return_acf_1": 0.4623316947881118,
        "abs_return_acf_5": 0.41256342326971296,
        "abs_return_acf_20": 0.35648166763898026,
        "quantile_01": -0.07997916423879295,
        "quantile_99": 0.06136227258650504,
        "hill_tail_index": 3.898401564670982
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018277989366268812,
        "excess_kurtosis": 23.309994094799933,
        "return_acf_1": -0.08698039576456965,
        "abs_return_acf_1": 0.2753071266256648,
        "abs_return_acf_5": 0.23473490912439907,
        "abs_return_acf_20": 0.24128457781144155,
        "quantile_01": -0.04594268453341778,
        "quantile_99": 0.0444503181889414,
        "hill_tail_index": 2.677599257017555
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01815501042965096,
        "excess_kurtosis": 5.776703424996997,
        "return_acf_1": -0.20786549548179473,
        "abs_return_acf_1": 0.38268379630544513,
        "abs_return_acf_5": 0.3660879303672668,
        "abs_return_acf_20": 0.23758666914856358,
        "quantile_01": -0.055716275885390694,
        "quantile_99": 0.053528711532408194,
        "hill_tail_index": 3.4499895044529616
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02130463158158479,
        "excess_kurtosis": 7.04143340644265,
        "return_acf_1": -0.0839693475237305,
        "abs_return_acf_1": 0.4124494194265893,
        "abs_return_acf_5": 0.39348349743607636,
        "abs_return_acf_20": 0.37322968109314547,
        "quantile_01": -0.0711996757471432,
        "quantile_99": 0.06338090790957282,
        "hill_tail_index": 2.982520799977421
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020279271390482335,
        "excess_kurtosis": 7.933335291504472,
        "return_acf_1": -0.15346434567376704,
        "abs_return_acf_1": 0.5352402887734128,
        "abs_return_acf_5": 0.4145129880675438,
        "abs_return_acf_20": 0.39568308540200897,
        "quantile_01": -0.06336647273283408,
        "quantile_99": 0.05771586199891613,
        "hill_tail_index": 3.7730031439925193
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02003297134633761,
        "excess_kurtosis": 10.606988589282311,
        "return_acf_1": -0.17498348154198828,
        "abs_return_acf_1": 0.5394809206768698,
        "abs_return_acf_5": 0.49511518464420795,
        "abs_return_acf_20": 0.3988302059855302,
        "quantile_01": -0.07939803943943409,
        "quantile_99": 0.05721401567178589,
        "hill_tail_index": 2.5295106000066188
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020146094263724643,
        "excess_kurtosis": 3.750920215863392,
        "return_acf_1": -0.14641400748520653,
        "abs_return_acf_1": 0.4029373227169734,
        "abs_return_acf_5": 0.37262433167472264,
        "abs_return_acf_20": 0.2934400968067201,
        "quantile_01": -0.059821210449621055,
        "quantile_99": 0.05206323084324699,
        "hill_tail_index": 4.483749853641554
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021785295716003336,
        "excess_kurtosis": 7.374616505340958,
        "return_acf_1": -0.08274216362885611,
        "abs_return_acf_1": 0.3927359096990292,
        "abs_return_acf_5": 0.4093477479421005,
        "abs_return_acf_20": 0.3178624293556038,
        "quantile_01": -0.07016639065651668,
        "quantile_99": 0.07428576745216942,
        "hill_tail_index": 4.821817327115198
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019681815862563012,
        "excess_kurtosis": 6.708370174673073,
        "return_acf_1": -0.12433849312205686,
        "abs_return_acf_1": 0.35691202046462733,
        "abs_return_acf_5": 0.33677242049237976,
        "abs_return_acf_20": 0.2551363108519435,
        "quantile_01": -0.06040587940016884,
        "quantile_99": 0.054550553177918785,
        "hill_tail_index": 3.85425700064319
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01938069926300438,
        "excess_kurtosis": 3.0878952025576014,
        "return_acf_1": -0.14291935975229458,
        "abs_return_acf_1": 0.2623300987042959,
        "abs_return_acf_5": 0.29845046624897253,
        "abs_return_acf_20": 0.2440362417357915,
        "quantile_01": -0.05647986145129498,
        "quantile_99": 0.04923553421524609,
        "hill_tail_index": 4.123875194272597
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02174577976656774,
        "excess_kurtosis": 6.472230967075587,
        "return_acf_1": -0.12965961030601547,
        "abs_return_acf_1": 0.42600148389846976,
        "abs_return_acf_5": 0.4543847324833289,
        "abs_return_acf_20": 0.3541036156148055,
        "quantile_01": -0.07202356720256001,
        "quantile_99": 0.0706255878253612,
        "hill_tail_index": 4.518599879773906
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
