# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27034
Run ID: `eb0c3b50c60ca01bb076138eafd8227b9dead12c23662a62e7be5eb03bb5b3c4`
Result fingerprint: `15aaa155442e9fe65bd880e37b00daa8b8663dfdde1964c3edcc08d6c46dd7a7`

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
    "equal_weight_sd": -0.5739642857142826,
    "equal_weight_raw": -8.609464285714237,
    "fixed_start_cap_weight_sd": -0.591652692332897,
    "fixed_start_cap_weight_raw": -8.874790384993453,
    "end_cap_weight_sd": -0.6100548524067493,
    "end_cap_weight_raw": -9.150822786101237
  },
  "full_period_change": {
    "equal_weight_sd": -0.8374047619047571,
    "equal_weight_raw": -12.561071428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7824123677248632,
    "inflation_mean_sd": 0.6674963624338625
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3784166666666698,
    "equal_weight_raw": 5.676250000000047,
    "fixed_start_cap_weight_sd": 0.36072826004805536,
    "fixed_start_cap_weight_raw": 5.41092390072083,
    "end_cap_weight_sd": 0.34232609997420316,
    "end_cap_weight_raw": 5.1348914996130475
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6357142857142825,
      "change_raw": -9.535714285714237,
      "decay_adjusted_gain_sd": 0.3166666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6071031746031714,
      "change_raw": -9.106547619047571,
      "decay_adjusted_gain_sd": 0.3452777777777809
    },
    "small": {
      "count": 18,
      "change_sd": -0.5471031746031714,
      "change_raw": -8.206547619047571,
      "decay_adjusted_gain_sd": 0.40527777777778096
    },
    "large_minus_small_sd": -0.08861111111111108,
    "large_minus_small_raw": -1.3291666666666662
  },
  "inflation": {
    "initial_mean_sd": 0.27125000000000005,
    "final_mean_sd": 0.7065,
    "mean_sd": 0.509515542603386,
    "mean_absolute_raw_gap": 7.642733139050792,
    "final_absolute_raw_gap": 10.597500000000002,
    "mean_range_fraction": 0.07642733139050792
  },
  "impact": {
    "initial_share": 0.3,
    "final_share": 0.36666666666666664,
    "initial_wealth_share": 0.23437655483446032,
    "final_wealth_share": 0.30727273087249596
  },
  "pricing_slope": {
    "mean": -0.0017532160906106136,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.14191622471509557,
    "real_improvement_cost": 0.09576838269011004,
    "washing_cost": 0.046147842024985564,
    "fine_transfer": 0.018470289847419448,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.16038651456251501,
    "resource_cost_fraction_initial_cap": 0.004730540823836518,
    "private_net_outflow_fraction_initial_cap": 0.005346217152083833,
    "fine_transfer_fraction_initial_cap": 0.0006156763282473149,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.007355164816717599,
    "unapplied_final_day_resource_cost": 0.0013316416432789
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 79.99437712489073,
    "beneficial_raw_gain_per_resource_cost": 1199.9156568733608,
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
    "accrued_cost": 2.757973406097567,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.21821707009290997,
    "accrued_cost_fraction_initial_cap": 0.09193244686991889,
    "mean_contract_rate": 0.03818616673448568,
    "maximum_ledger_error": 8.131516293641283e-20
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
    "maximum_relative_cash_error": 2.7577969442586326e-15,
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
      "minimum": -0.19066659321728957,
      "maximum": 0.009697890389072235,
      "mean": -0.09871883459613918,
      "median": -0.10749934094202176,
      "quantile_05": -0.1780225768050907,
      "quantile_95": -0.007108938375441681
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
      "minimum": 0.2615833012798398,
      "maximum": 0.7390270377739466,
      "mean": 0.47767969239881986,
      "median": 0.44395353454810316,
      "quantile_05": 0.34461027138885847,
      "quantile_95": 0.6792908114124117
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
        "daily_volatility": 0.016247476068537593,
        "excess_kurtosis": 3.0657870608733697,
        "return_acf_1": -0.15429196393662017,
        "abs_return_acf_1": 0.2238439137940183,
        "abs_return_acf_5": 0.24808525678201987,
        "abs_return_acf_20": 0.16947999193210297,
        "quantile_01": -0.04188386102662489,
        "quantile_99": 0.04520531369253558,
        "hill_tail_index": 3.7677360986579504
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01732727211207708,
        "excess_kurtosis": 6.45890452767096,
        "return_acf_1": -0.1150771059092204,
        "abs_return_acf_1": 0.29594312663719247,
        "abs_return_acf_5": 0.21482058712678778,
        "abs_return_acf_20": 0.2230647204145318,
        "quantile_01": -0.0499963518144693,
        "quantile_99": 0.04744902972184225,
        "hill_tail_index": 3.2501510353339693
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017961118655234847,
        "excess_kurtosis": 11.35878435513661,
        "return_acf_1": -0.14627760667588724,
        "abs_return_acf_1": 0.33786284637633285,
        "abs_return_acf_5": 0.20287216262389318,
        "abs_return_acf_20": 0.23944159881342883,
        "quantile_01": -0.04995822018005694,
        "quantile_99": 0.04972365033550705,
        "hill_tail_index": 3.3853507238294105
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018677465942160427,
        "excess_kurtosis": 6.530808985125061,
        "return_acf_1": -0.120401427637225,
        "abs_return_acf_1": 0.3115123275128841,
        "abs_return_acf_5": 0.22982144666984336,
        "abs_return_acf_20": 0.222955443167345,
        "quantile_01": -0.05630734652555804,
        "quantile_99": 0.055779279313893586,
        "hill_tail_index": 4.00354169339579
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01664649329733884,
        "excess_kurtosis": 17.563970343565366,
        "return_acf_1": -0.10147452738092727,
        "abs_return_acf_1": 0.32412362580316284,
        "abs_return_acf_5": 0.19748972445368665,
        "abs_return_acf_20": 0.23218239526889795,
        "quantile_01": -0.042620567073116955,
        "quantile_99": 0.038900162660638594,
        "hill_tail_index": 2.0389569525024984
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015694710111544986,
        "excess_kurtosis": 5.24967122361047,
        "return_acf_1": -0.09986920671080989,
        "abs_return_acf_1": 0.29628098300575123,
        "abs_return_acf_5": 0.24604211293263692,
        "abs_return_acf_20": 0.20041280547546286,
        "quantile_01": -0.04161889431884234,
        "quantile_99": 0.0423647463618669,
        "hill_tail_index": 2.866143269737461
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018468439004390196,
        "excess_kurtosis": 10.482375019980298,
        "return_acf_1": -0.04587182964728908,
        "abs_return_acf_1": 0.45436295523557246,
        "abs_return_acf_5": 0.36272452136152444,
        "abs_return_acf_20": 0.33836325855154237,
        "quantile_01": -0.05792125199352657,
        "quantile_99": 0.052295542226559334,
        "hill_tail_index": 2.7942849255489746
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01719473943057105,
        "excess_kurtosis": 7.0501334492668555,
        "return_acf_1": 0.009697890389072235,
        "abs_return_acf_1": 0.25083903225155757,
        "abs_return_acf_5": 0.22429836253053456,
        "abs_return_acf_20": 0.23713801172285376,
        "quantile_01": -0.054312191510545685,
        "quantile_99": 0.04658673497835769,
        "hill_tail_index": 3.083205785694728
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017876701887494833,
        "excess_kurtosis": 5.60326495575149,
        "return_acf_1": -0.07008693844263886,
        "abs_return_acf_1": 0.27389542263408084,
        "abs_return_acf_5": 0.1999582861279133,
        "abs_return_acf_20": 0.2127034820817556,
        "quantile_01": -0.05647933675665277,
        "quantile_99": 0.049111238841651715,
        "hill_tail_index": 3.480933095981421
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016915465681123072,
        "excess_kurtosis": 6.431477826646283,
        "return_acf_1": -0.06967919293540027,
        "abs_return_acf_1": 0.24524402575911092,
        "abs_return_acf_5": 0.2655446682708221,
        "abs_return_acf_20": 0.2590657645246174,
        "quantile_01": -0.04704408839503893,
        "quantile_99": 0.04443008464493168,
        "hill_tail_index": 2.873772070522503
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.014547789929339524,
        "excess_kurtosis": 2.5647118174946506,
        "return_acf_1": -0.11109343171376732,
        "abs_return_acf_1": 0.171845153898503,
        "abs_return_acf_5": 0.09706513389579728,
        "abs_return_acf_20": 0.12145313502028758,
        "quantile_01": -0.03671328093190689,
        "quantile_99": 0.03667726530636119,
        "hill_tail_index": 3.3625552120826727
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01565088182936829,
        "excess_kurtosis": 12.750736932176466,
        "return_acf_1": -0.1544454719666961,
        "abs_return_acf_1": 0.2594181964806591,
        "abs_return_acf_5": 0.10565964872642856,
        "abs_return_acf_20": 0.09565427709867738,
        "quantile_01": -0.03612974711188372,
        "quantile_99": 0.041991485046962235,
        "hill_tail_index": 2.6977226706541915
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019212364339799122,
        "excess_kurtosis": 14.981707024741691,
        "return_acf_1": -0.1838058861136955,
        "abs_return_acf_1": 0.407525919967516,
        "abs_return_acf_5": 0.18197877292462533,
        "abs_return_acf_20": 0.18296477967927685,
        "quantile_01": -0.04804585795584989,
        "quantile_99": 0.04764493176797512,
        "hill_tail_index": 2.7464699180023957
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016336777835408454,
        "excess_kurtosis": 8.191614589261775,
        "return_acf_1": -0.10228330531586206,
        "abs_return_acf_1": 0.2203465006073291,
        "abs_return_acf_5": 0.23737994945463983,
        "abs_return_acf_20": 0.24964433061979827,
        "quantile_01": -0.04409733215296267,
        "quantile_99": 0.048458843083736304,
        "hill_tail_index": 2.8509737217782805
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017460393271097014,
        "excess_kurtosis": 5.490655357363506,
        "return_acf_1": -0.032369976772042196,
        "abs_return_acf_1": 0.24642087894586615,
        "abs_return_acf_5": 0.15506218838207694,
        "abs_return_acf_20": 0.15966950765328528,
        "quantile_01": -0.05267105740341982,
        "quantile_99": 0.04953429246940574,
        "hill_tail_index": 3.433185940888319
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.015210251771986542,
        "excess_kurtosis": 2.5506431179378453,
        "return_acf_1": -0.1437520905789778,
        "abs_return_acf_1": 0.2741438117863615,
        "abs_return_acf_5": 0.22743069319378478,
        "abs_return_acf_20": 0.15498934290216343,
        "quantile_01": -0.040033876344931885,
        "quantile_99": 0.04435675999063122,
        "hill_tail_index": 4.11605497568359
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.015468984202267659,
        "excess_kurtosis": 10.933335201126425,
        "return_acf_1": -0.12129929918755923,
        "abs_return_acf_1": 0.26101815755138963,
        "abs_return_acf_5": 0.13307700721968838,
        "abs_return_acf_20": 0.1070548777442345,
        "quantile_01": -0.03866248580889278,
        "quantile_99": 0.036333748255347846,
        "hill_tail_index": 2.245877148196653
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018245081153472415,
        "excess_kurtosis": 9.08949454847274,
        "return_acf_1": -0.005591148484470916,
        "abs_return_acf_1": 0.32772965431461093,
        "abs_return_acf_5": 0.30982656052340785,
        "abs_return_acf_20": 0.2775348196368233,
        "quantile_01": -0.06175712995678748,
        "quantile_99": 0.04865469031108104,
        "hill_tail_index": 2.5289594601308014
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018211765495721146,
        "excess_kurtosis": 7.485010347221351,
        "return_acf_1": -0.12533265059909743,
        "abs_return_acf_1": 0.26539240743522813,
        "abs_return_acf_5": 0.21553338850305914,
        "abs_return_acf_20": 0.19719052148491736,
        "quantile_01": -0.06387679596332392,
        "quantile_99": 0.05485204261704075,
        "hill_tail_index": 3.040964095640278
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016542237509373253,
        "excess_kurtosis": 6.473701242872206,
        "return_acf_1": -0.02631184634915934,
        "abs_return_acf_1": 0.2182816209359507,
        "abs_return_acf_5": 0.16078603093008706,
        "abs_return_acf_20": 0.20206199783867224,
        "quantile_01": -0.04634186650853647,
        "quantile_99": 0.0398438825497414,
        "hill_tail_index": 2.62700658695683
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01857324481759787,
        "excess_kurtosis": 7.2099970510748825,
        "return_acf_1": -0.10886371234608219,
        "abs_return_acf_1": 0.33598637796087466,
        "abs_return_acf_5": 0.2664600816769076,
        "abs_return_acf_20": 0.2580634608091621,
        "quantile_01": -0.05790906851933485,
        "quantile_99": 0.049185721074587824,
        "hill_tail_index": 3.4593908979935337
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.015135339120695666,
        "excess_kurtosis": 4.903799613999857,
        "return_acf_1": -0.12665660900269465,
        "abs_return_acf_1": 0.2012714719823768,
        "abs_return_acf_5": 0.2138685279349782,
        "abs_return_acf_20": 0.17001699419399333,
        "quantile_01": -0.03731345795505556,
        "quantile_99": 0.03903209188832468,
        "hill_tail_index": 2.9494574488492713
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.015472482078725893,
        "excess_kurtosis": 8.260497032677021,
        "return_acf_1": -0.03388735982620426,
        "abs_return_acf_1": 0.27673706731983366,
        "abs_return_acf_5": 0.2199619896373276,
        "abs_return_acf_20": 0.17374371423853016,
        "quantile_01": -0.042620822270281834,
        "quantile_99": 0.03780365413060771,
        "hill_tail_index": 2.6805870573333577
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01527479922316369,
        "excess_kurtosis": 3.587151542149095,
        "return_acf_1": -0.19066659321728957,
        "abs_return_acf_1": 0.24338922253246692,
        "abs_return_acf_5": 0.17113683617884767,
        "abs_return_acf_20": 0.15382136174221028,
        "quantile_01": -0.03996498296083088,
        "quantile_99": 0.036470984039336955,
        "hill_tail_index": 2.9659320340568827
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.015810223696638454,
        "excess_kurtosis": 11.746547784878588,
        "return_acf_1": -0.1709540876501293,
        "abs_return_acf_1": 0.24504220731724566,
        "abs_return_acf_5": 0.21177934042357555,
        "abs_return_acf_20": 0.19607439156963213,
        "quantile_01": -0.03994401288519473,
        "quantile_99": 0.04022946591828923,
        "hill_tail_index": 2.783489499049918
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.015289328340558692,
        "excess_kurtosis": 3.801582601460198,
        "return_acf_1": -0.10613496953796135,
        "abs_return_acf_1": 0.2651712110165079,
        "abs_return_acf_5": 0.18473190452025992,
        "abs_return_acf_20": 0.1781756955457243,
        "quantile_01": -0.044497049288789045,
        "quantile_99": 0.03986628597504841,
        "hill_tail_index": 4.543960269510882
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021887067402397018,
        "excess_kurtosis": 16.185436941730845,
        "return_acf_1": -0.06891379841957435,
        "abs_return_acf_1": 0.39131254276295585,
        "abs_return_acf_5": 0.341121392491867,
        "abs_return_acf_20": 0.2753482697644772,
        "quantile_01": -0.07036711577337317,
        "quantile_99": 0.06910453335899756,
        "hill_tail_index": 2.285168901971175
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01835993571489176,
        "excess_kurtosis": 8.778347880611202,
        "return_acf_1": -0.008964014908850371,
        "abs_return_acf_1": 0.36264946783271995,
        "abs_return_acf_5": 0.2709815693361202,
        "abs_return_acf_20": 0.28677408854651004,
        "quantile_01": -0.056710859391687476,
        "quantile_99": 0.05042034446719189,
        "hill_tail_index": 2.6861423393209596
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01919082571702064,
        "excess_kurtosis": 12.618160560505615,
        "return_acf_1": -0.0887086070683438,
        "abs_return_acf_1": 0.4128159086306988,
        "abs_return_acf_5": 0.3621773354944835,
        "abs_return_acf_20": 0.28749967258129033,
        "quantile_01": -0.05822653849622466,
        "quantile_99": 0.05354675286683917,
        "hill_tail_index": 2.52332039221613
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016071596293917315,
        "excess_kurtosis": 3.018041853728932,
        "return_acf_1": -0.1381982699387717,
        "abs_return_acf_1": 0.21389409859354971,
        "abs_return_acf_5": 0.22513503566017853,
        "abs_return_acf_20": 0.22907278325583177,
        "quantile_01": -0.04557823635901901,
        "quantile_99": 0.04299899167834202,
        "hill_tail_index": 3.8037366412193947
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
