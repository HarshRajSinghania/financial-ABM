# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27243
Run ID: `6ce1406bb93277d668e0dd412432d1805ed99f76e19b2adeb3cf898b4f2ad20c`
Result fingerprint: `24f49de8cf8ce0b9fbfa40d7827c6578f676eb088f0a8e9f0065800ad9e9a27c`

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
    "equal_weight_sd": -0.7988809523809492,
    "equal_weight_raw": -11.983214285714237,
    "fixed_start_cap_weight_sd": -0.7792102479733245,
    "fixed_start_cap_weight_raw": -11.688153719599866,
    "end_cap_weight_sd": -0.7874508976913778,
    "end_cap_weight_raw": -11.811763465370664
  },
  "full_period_change": {
    "equal_weight_sd": -1.2093214285714238,
    "equal_weight_raw": -18.139821428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1193693783068739,
    "inflation_mean_sd": 0.5502999338624338
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.15350000000000313,
    "equal_weight_raw": 2.3025000000000473,
    "fixed_start_cap_weight_sd": 0.17317070440762777,
    "fixed_start_cap_weight_raw": 2.5975605661144163,
    "end_cap_weight_sd": 0.16493005468957428,
    "end_cap_weight_raw": 2.473950820343614
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7548809523809493,
      "change_raw": -11.32321428571424,
      "decay_adjusted_gain_sd": 0.19750000000000298
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7154365079365047,
      "change_raw": -10.731547619047571,
      "decay_adjusted_gain_sd": 0.23694444444444762
    },
    "small": {
      "count": 18,
      "change_sd": -0.8479365079365048,
      "change_raw": -12.719047619047572,
      "decay_adjusted_gain_sd": 0.1044444444444476
    },
    "large_minus_small_sd": 0.09305555555555545,
    "large_minus_small_raw": 1.3958333333333317
  },
  "inflation": {
    "initial_mean_sd": 0.2855833333333333,
    "final_mean_sd": 0.56575,
    "mean_sd": 0.4350658479045241,
    "mean_absolute_raw_gap": 6.52598771856786,
    "final_absolute_raw_gap": 8.48625,
    "mean_range_fraction": 0.0652598771856786
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.4,
    "initial_wealth_share": 0.23795764881372308,
    "final_wealth_share": 0.3870562590361119
  },
  "pricing_slope": {
    "mean": -0.003798715217538374,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.03078468792042141,
    "real_improvement_cost": 0.012152181152085138,
    "washing_cost": 0.01863250676833627,
    "fine_transfer": 0.0019137098295873918,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0326983977500088,
    "resource_cost_fraction_initial_cap": 0.0010261562640140468,
    "private_net_outflow_fraction_initial_cap": 0.0010899465916669598,
    "fine_transfer_fraction_initial_cap": 6.379032765291306e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.010231202642594233,
    "unapplied_final_day_resource_cost": 0.0007769644676094387
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 149.5873536838848,
    "beneficial_raw_gain_per_resource_cost": 2243.8103052582724,
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
    "accrued_cost": 2.982924781414345,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.0067343052238683365,
    "accrued_cost_fraction_initial_cap": 0.09943082604714482,
    "mean_contract_rate": 0.041310044971745064,
    "maximum_ledger_error": 6.098637220230962e-20
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
    "price_cap_hits": 7,
    "maximum_relative_cash_error": 1.1105823815253041e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.29613651900532934,
      "maximum": -0.15732116927317494,
      "mean": -0.22604198827836888,
      "median": -0.22919520799225962,
      "quantile_05": -0.27671979516885226,
      "quantile_95": -0.17466165044702353
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
      "minimum": 0.033994363671265466,
      "maximum": 0.8446461962374866,
      "mean": 0.6025664666027586,
      "median": 0.6862472281828567,
      "quantile_05": 0.10809988197944533,
      "quantile_95": 0.8185937074669961
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
        "daily_volatility": 0.023199426750378914,
        "excess_kurtosis": 16.58011874460252,
        "return_acf_1": -0.1800238008363439,
        "abs_return_acf_1": 0.477974507238766,
        "abs_return_acf_5": 0.4683011626675881,
        "abs_return_acf_20": 0.3174579303311849,
        "quantile_01": -0.08222562639582842,
        "quantile_99": 0.06755484434495679,
        "hill_tail_index": 2.7286116979307966
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.022320107245238075,
        "excess_kurtosis": 20.553656573981264,
        "return_acf_1": -0.17095274633812693,
        "abs_return_acf_1": 0.34264309309348395,
        "abs_return_acf_5": 0.36194987387891575,
        "abs_return_acf_20": 0.3208062075047253,
        "quantile_01": -0.07797042547738316,
        "quantile_99": 0.06602180553211065,
        "hill_tail_index": 3.0641678884245507
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020951153280929734,
        "excess_kurtosis": 12.21576072281561,
        "return_acf_1": -0.22796743446904424,
        "abs_return_acf_1": 0.3691142675250265,
        "abs_return_acf_5": 0.3755693585024079,
        "abs_return_acf_20": 0.3058933880968512,
        "quantile_01": -0.06454395512177527,
        "quantile_99": 0.056452334561474145,
        "hill_tail_index": 2.8355979784861924
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.025591414881896108,
        "excess_kurtosis": 25.005465999951667,
        "return_acf_1": -0.15732116927317494,
        "abs_return_acf_1": 0.500404942952687,
        "abs_return_acf_5": 0.44517442996853507,
        "abs_return_acf_20": 0.33837974120402137,
        "quantile_01": -0.08965471154441608,
        "quantile_99": 0.06220745199219152,
        "hill_tail_index": 1.8459731253633385
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.026163764356612385,
        "excess_kurtosis": 28.125495535348673,
        "return_acf_1": -0.29613651900532934,
        "abs_return_acf_1": 0.47452230101011084,
        "abs_return_acf_5": 0.4867139787541362,
        "abs_return_acf_20": 0.30897475595627927,
        "quantile_01": -0.07801863773221987,
        "quantile_99": 0.058564032885923614,
        "hill_tail_index": 2.0692345951926137
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.023750162214602872,
        "excess_kurtosis": 27.52221417801246,
        "return_acf_1": -0.2653755327116279,
        "abs_return_acf_1": 0.551134959458253,
        "abs_return_acf_5": 0.46000542194924937,
        "abs_return_acf_20": 0.3561512795522997,
        "quantile_01": -0.06981381059620076,
        "quantile_99": 0.04674701160399507,
        "hill_tail_index": 1.4727474912485077
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022209168771242512,
        "excess_kurtosis": 10.476211242942803,
        "return_acf_1": -0.23661630670875072,
        "abs_return_acf_1": 0.4382899064343365,
        "abs_return_acf_5": 0.3337426795577157,
        "abs_return_acf_20": 0.3308758142681298,
        "quantile_01": -0.077121762303882,
        "quantile_99": 0.0627689027952068,
        "hill_tail_index": 2.479248276404874
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.0249782904146387,
        "excess_kurtosis": 18.602842969338745,
        "return_acf_1": -0.2016690758126209,
        "abs_return_acf_1": 0.41941707873200335,
        "abs_return_acf_5": 0.4197968969637123,
        "abs_return_acf_20": 0.399996798091687,
        "quantile_01": -0.07913999687908589,
        "quantile_99": 0.06791839933520573,
        "hill_tail_index": 2.348278284180173
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02162586337239769,
        "excess_kurtosis": 15.870583087092438,
        "return_acf_1": -0.2520231466885964,
        "abs_return_acf_1": 0.3798574899435414,
        "abs_return_acf_5": 0.3824002528795539,
        "abs_return_acf_20": 0.3635593426429145,
        "quantile_01": -0.06968756912100507,
        "quantile_99": 0.04860498338009681,
        "hill_tail_index": 2.2865943237629116
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.023872129034092002,
        "excess_kurtosis": 26.51372870831942,
        "return_acf_1": -0.1910346155443538,
        "abs_return_acf_1": 0.49680114964113015,
        "abs_return_acf_5": 0.45551253236207867,
        "abs_return_acf_20": 0.3578019593473205,
        "quantile_01": -0.07119449436973195,
        "quantile_99": 0.05452747390237166,
        "hill_tail_index": 1.5652759687956064
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.021487436493102703,
        "excess_kurtosis": 7.2870597569901285,
        "return_acf_1": -0.20330765777337934,
        "abs_return_acf_1": 0.39568838853984767,
        "abs_return_acf_5": 0.3930751585436097,
        "abs_return_acf_20": 0.31343350929838143,
        "quantile_01": -0.06564453914368425,
        "quantile_99": 0.06169541938486022,
        "hill_tail_index": 3.513051960374226
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022787012613369732,
        "excess_kurtosis": 16.116828670623264,
        "return_acf_1": -0.21569183567449104,
        "abs_return_acf_1": 0.3855716878332895,
        "abs_return_acf_5": 0.39033865326842876,
        "abs_return_acf_20": 0.3298127851634167,
        "quantile_01": -0.07502392920481575,
        "quantile_99": 0.06317932343999041,
        "hill_tail_index": 2.427714805459465
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.025063652517112806,
        "excess_kurtosis": 23.486007298441365,
        "return_acf_1": -0.20083820928341847,
        "abs_return_acf_1": 0.4114225297745263,
        "abs_return_acf_5": 0.41751896374290365,
        "abs_return_acf_20": 0.33726465916344,
        "quantile_01": -0.08117663098783326,
        "quantile_99": 0.06868637491955162,
        "hill_tail_index": 2.595706305663856
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.028146088123706014,
        "excess_kurtosis": 18.836435184153096,
        "return_acf_1": -0.22114383753342415,
        "abs_return_acf_1": 0.41527624505427585,
        "abs_return_acf_5": 0.37265640552222457,
        "abs_return_acf_20": 0.33717012493275705,
        "quantile_01": -0.08101655127593214,
        "quantile_99": 0.09576457209204799,
        "hill_tail_index": 2.873836292802078
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02793557017731949,
        "excess_kurtosis": 24.34643585944635,
        "return_acf_1": -0.23487267596573758,
        "abs_return_acf_1": 0.4018915594321247,
        "abs_return_acf_5": 0.38746953981876064,
        "abs_return_acf_20": 0.29717166213153895,
        "quantile_01": -0.07344046277039132,
        "quantile_99": 0.08552239655616853,
        "hill_tail_index": 2.2690182522178026
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.025345022342637875,
        "excess_kurtosis": 13.338779200943762,
        "return_acf_1": -0.22363614710358545,
        "abs_return_acf_1": 0.41365359746704905,
        "abs_return_acf_5": 0.4381481580687229,
        "abs_return_acf_20": 0.4297574462111006,
        "quantile_01": -0.07657304252535957,
        "quantile_99": 0.07164201964289327,
        "hill_tail_index": 2.6213089271328713
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.024117285041413472,
        "excess_kurtosis": 27.825526884756435,
        "return_acf_1": -0.23626721078546553,
        "abs_return_acf_1": 0.46692615199273735,
        "abs_return_acf_5": 0.447386852398559,
        "abs_return_acf_20": 0.31783009678467505,
        "quantile_01": -0.07148764972512293,
        "quantile_99": 0.050992674815868055,
        "hill_tail_index": 1.6168777175121112
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.022772974258422857,
        "excess_kurtosis": 25.144018761347105,
        "return_acf_1": -0.2702485829677872,
        "abs_return_acf_1": 0.5663517928531732,
        "abs_return_acf_5": 0.5447622350340614,
        "abs_return_acf_20": 0.3774298333570812,
        "quantile_01": -0.07564392947630987,
        "quantile_99": 0.04676640356159214,
        "hill_tail_index": 1.5879359301291494
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023099405013191774,
        "excess_kurtosis": 13.635508251279884,
        "return_acf_1": -0.1791947554690082,
        "abs_return_acf_1": 0.4143914348864513,
        "abs_return_acf_5": 0.34698071846799233,
        "abs_return_acf_20": 0.24715208652943582,
        "quantile_01": -0.06591402858694467,
        "quantile_99": 0.06462011843486597,
        "hill_tail_index": 2.5249351587637574
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024279643723085137,
        "excess_kurtosis": 23.919151277721827,
        "return_acf_1": -0.2616551873605415,
        "abs_return_acf_1": 0.4510244907198059,
        "abs_return_acf_5": 0.4432519807956291,
        "abs_return_acf_20": 0.35667217961712383,
        "quantile_01": -0.07201550453301434,
        "quantile_99": 0.05550801668649312,
        "hill_tail_index": 2.1386913071518117
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02314387211846654,
        "excess_kurtosis": 13.429230944577426,
        "return_acf_1": -0.20862748407149145,
        "abs_return_acf_1": 0.4953358217252246,
        "abs_return_acf_5": 0.4064010946527688,
        "abs_return_acf_20": 0.335920682636847,
        "quantile_01": -0.08305773077750143,
        "quantile_99": 0.05832734558687163,
        "hill_tail_index": 2.8506768444147417
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.026697281764358063,
        "excess_kurtosis": 16.82935143594347,
        "return_acf_1": -0.2573445921001448,
        "abs_return_acf_1": 0.43169637734583605,
        "abs_return_acf_5": 0.3474431864033258,
        "abs_return_acf_20": 0.29448861536558235,
        "quantile_01": -0.07672687741607943,
        "quantile_99": 0.09304872645351916,
        "hill_tail_index": 2.3120915480743376
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02150445808127406,
        "excess_kurtosis": 11.688501405831206,
        "return_acf_1": -0.2510752531828337,
        "abs_return_acf_1": 0.4099322590000938,
        "abs_return_acf_5": 0.402076838717345,
        "abs_return_acf_20": 0.27325114762895425,
        "quantile_01": -0.06767975498683097,
        "quantile_99": 0.05942798453897531,
        "hill_tail_index": 2.9103791136418193
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0262751173653288,
        "excess_kurtosis": 29.888912637466078,
        "return_acf_1": -0.23406535181514396,
        "abs_return_acf_1": 0.5116604780553082,
        "abs_return_acf_5": 0.5057724055796045,
        "abs_return_acf_20": 0.37310874464666915,
        "quantile_01": -0.08050810434468392,
        "quantile_99": 0.060163618587739595,
        "hill_tail_index": 2.1988510679585342
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.022969170336717845,
        "excess_kurtosis": 14.80622288335147,
        "return_acf_1": -0.2090115552492254,
        "abs_return_acf_1": 0.41444485769864114,
        "abs_return_acf_5": 0.3628786899335064,
        "abs_return_acf_20": 0.3486356082210928,
        "quantile_01": -0.0697314365388205,
        "quantile_99": 0.06262618325248233,
        "hill_tail_index": 2.493957237461898
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.025434815797166305,
        "excess_kurtosis": 30.281913955096726,
        "return_acf_1": -0.24395027574852662,
        "abs_return_acf_1": 0.48417758824263407,
        "abs_return_acf_5": 0.49134978449221983,
        "abs_return_acf_20": 0.33430854371377056,
        "quantile_01": -0.073240925689238,
        "quantile_99": 0.05452952649325805,
        "hill_tail_index": 1.8266818352295289
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02480369777900368,
        "excess_kurtosis": 22.962912990956802,
        "return_acf_1": -0.23042298151547502,
        "abs_return_acf_1": 0.473915426483239,
        "abs_return_acf_5": 0.4786584438854351,
        "abs_return_acf_20": 0.34412489850475825,
        "quantile_01": -0.07741073951083205,
        "quantile_99": 0.06975195737388604,
        "hill_tail_index": 2.1501433776587606
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.025177456383753502,
        "excess_kurtosis": 35.968037113900685,
        "return_acf_1": -0.1869418932965026,
        "abs_return_acf_1": 0.504859562425908,
        "abs_return_acf_5": 0.5278321888620005,
        "abs_return_acf_20": 0.3527685856937093,
        "quantile_01": -0.07395299816586676,
        "quantile_99": 0.05253340073375864,
        "hill_tail_index": 1.5692785883358185
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02498921289858202,
        "excess_kurtosis": 22.56316507545087,
        "return_acf_1": -0.2518293907335547,
        "abs_return_acf_1": 0.5328080038376924,
        "abs_return_acf_5": 0.48554968461455833,
        "abs_return_acf_20": 0.3576210130934744,
        "quantile_01": -0.07649522524989306,
        "quantile_99": 0.0663422935572417,
        "hill_tail_index": 1.7823991485276822
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02617922350227916,
        "excess_kurtosis": 18.94754226566823,
        "return_acf_1": -0.28201442333336,
        "abs_return_acf_1": 0.5641091097514055,
        "abs_return_acf_5": 0.5369100439271226,
        "abs_return_acf_20": 0.44102841302639345,
        "quantile_01": -0.08726040607068897,
        "quantile_99": 0.07050877813650552,
        "hill_tail_index": 2.2906942338286687
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
