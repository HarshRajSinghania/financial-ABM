# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27085
Run ID: `3b93decc3149f3e1f75d174413435d90b6cd15c70da67ace7af944dcecc5db8a`
Result fingerprint: `41077e9fde73337020abb8ebc65a24f9fd69fd5a3b737b1e2782f7dc659f42c1`

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
    "equal_weight_sd": -0.625827125033537,
    "equal_weight_raw": -9.387406875503055,
    "fixed_start_cap_weight_sd": -0.6574820645154632,
    "fixed_start_cap_weight_raw": -9.86223096773195,
    "end_cap_weight_sd": -0.6619691913016228,
    "end_cap_weight_raw": -9.929537869524339
  },
  "full_period_change": {
    "equal_weight_sd": -0.967850934557345,
    "equal_weight_raw": -14.517764018360175
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.905184078926204,
    "inflation_mean_sd": 0.5310982142857144
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3141320869465591,
    "equal_weight_raw": 4.711981304198387,
    "fixed_start_cap_weight_sd": 0.28106462611643834,
    "fixed_start_cap_weight_raw": 4.215969391746575,
    "end_cap_weight_sd": 0.2786705158294663,
    "end_cap_weight_raw": 4.1800577374419925
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.704880952380949,
      "change_raw": -10.573214285714236,
      "decay_adjusted_gain_sd": 0.2475000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6591459723340204,
      "change_raw": -9.887189585010306,
      "decay_adjusted_gain_sd": 0.267222222222225
    },
    "small": {
      "count": 18,
      "change_sd": -0.5959920634920602,
      "change_raw": -8.939880952380904,
      "decay_adjusted_gain_sd": 0.3486923671331521
    },
    "large_minus_small_sd": -0.10888888888888881,
    "large_minus_small_raw": -1.6333333333333322
  },
  "inflation": {
    "initial_mean_sd": 0.23125,
    "final_mean_sd": 0.5325000000000001,
    "mean_sd": 0.423078684429642,
    "mean_absolute_raw_gap": 6.346180266444629,
    "final_absolute_raw_gap": 7.987500000000001,
    "mean_range_fraction": 0.06346180266444629
  },
  "impact": {
    "initial_share": 0.37333333333333335,
    "final_share": 0.64,
    "initial_wealth_share": 0.3816662766331607,
    "final_wealth_share": 0.6306758465023674
  },
  "pricing_slope": {
    "mean": -0.0026070388519487597,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.17145544500387566,
    "real_improvement_cost": 0.11694581685791866,
    "washing_cost": 0.05450962814595704,
    "fine_transfer": 0.028838160820029636,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.2002936058239053,
    "resource_cost_fraction_initial_cap": 0.005715181500129189,
    "private_net_outflow_fraction_initial_cap": 0.00667645352746351,
    "fine_transfer_fraction_initial_cap": 0.0009612720273343212,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.005384269695323316,
    "unapplied_final_day_resource_cost": 0.005832389918442051
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 54.96449884215546,
    "beneficial_raw_gain_per_resource_cost": 824.4674826323318,
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
    "fixed_exposure": 15.0,
    "accrued_cost": 2.873896601960248,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": 0.10229387423022816,
    "accrued_cost_fraction_initial_cap": 0.09579655339867493,
    "mean_contract_rate": 0.04035205076667881,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.7926341927023157e-15,
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
      "minimum": -0.17361021050885947,
      "maximum": -0.02844258391865439,
      "mean": -0.1106470216812525,
      "median": -0.11547937777267447,
      "quantile_05": -0.16250202482574405,
      "quantile_95": -0.0381903556209092
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
      "minimum": 0.31257800362122795,
      "maximum": 0.7283852513952345,
      "mean": 0.5239636155243738,
      "median": 0.5094271704202707,
      "quantile_05": 0.3682390506638162,
      "quantile_95": 0.6862061545731986
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
        "daily_volatility": 0.018666618133698357,
        "excess_kurtosis": 6.83261544992933,
        "return_acf_1": -0.12225129342505169,
        "abs_return_acf_1": 0.3770148758749376,
        "abs_return_acf_5": 0.3615762076577407,
        "abs_return_acf_20": 0.3185028407658231,
        "quantile_01": -0.05909352827116543,
        "quantile_99": 0.05283860786609622,
        "hill_tail_index": 3.223565594831764
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016003165121292677,
        "excess_kurtosis": 3.3825809403786513,
        "return_acf_1": -0.07289618008714534,
        "abs_return_acf_1": 0.23835025836738746,
        "abs_return_acf_5": 0.2783669243848076,
        "abs_return_acf_20": 0.2499195010171081,
        "quantile_01": -0.044371376925639076,
        "quantile_99": 0.042917191237249595,
        "hill_tail_index": 3.659705347044435
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018231431096135575,
        "excess_kurtosis": 4.947616163024367,
        "return_acf_1": -0.11555555211528677,
        "abs_return_acf_1": 0.3235758109249828,
        "abs_return_acf_5": 0.32440075702424664,
        "abs_return_acf_20": 0.2491139002685541,
        "quantile_01": -0.06150957451734147,
        "quantile_99": 0.0472349088943267,
        "hill_tail_index": 3.075971124615098
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.015890235561473405,
        "excess_kurtosis": 3.252504579453741,
        "return_acf_1": -0.11594210839014701,
        "abs_return_acf_1": 0.25544341252831265,
        "abs_return_acf_5": 0.2686317869120533,
        "abs_return_acf_20": 0.22917158321477435,
        "quantile_01": -0.04825282080621914,
        "quantile_99": 0.039922709594701816,
        "hill_tail_index": 3.746602742496128
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.014939404821129175,
        "excess_kurtosis": 2.837781171375492,
        "return_acf_1": -0.13904154048456352,
        "abs_return_acf_1": 0.20154168619860174,
        "abs_return_acf_5": 0.2198474117279624,
        "abs_return_acf_20": 0.11361895835078527,
        "quantile_01": -0.03953979732758813,
        "quantile_99": 0.04099885818283532,
        "hill_tail_index": 4.318929383969385
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.015133728162164661,
        "excess_kurtosis": 2.510183955538859,
        "return_acf_1": -0.09876026718329964,
        "abs_return_acf_1": 0.16456318035448747,
        "abs_return_acf_5": 0.2211659449130098,
        "abs_return_acf_20": 0.13652978727674903,
        "quantile_01": -0.04027831994338332,
        "quantile_99": 0.039302517420883545,
        "hill_tail_index": 3.8886116212772324
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018481233611388332,
        "excess_kurtosis": 7.569948948219357,
        "return_acf_1": -0.10380307644900746,
        "abs_return_acf_1": 0.3641385612845533,
        "abs_return_acf_5": 0.33072462229513716,
        "abs_return_acf_20": 0.26856778639461215,
        "quantile_01": -0.05507200837732013,
        "quantile_99": 0.05629257869379633,
        "hill_tail_index": 3.1999907223317567
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.014879920649111943,
        "excess_kurtosis": 6.068455741363387,
        "return_acf_1": -0.10157596618501198,
        "abs_return_acf_1": 0.25160179496380874,
        "abs_return_acf_5": 0.2483340869672871,
        "abs_return_acf_20": 0.2199906266157021,
        "quantile_01": -0.04279091866506351,
        "quantile_99": 0.03873058534746432,
        "hill_tail_index": 3.1746994593473916
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.015903240132841487,
        "excess_kurtosis": 3.9227714926621626,
        "return_acf_1": -0.1535387104169745,
        "abs_return_acf_1": 0.32562325398847164,
        "abs_return_acf_5": 0.27328636966787273,
        "abs_return_acf_20": 0.21272847084786775,
        "quantile_01": -0.044571925477472935,
        "quantile_99": 0.0397694066961788,
        "hill_tail_index": 3.396808623149351
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.015119706179178813,
        "excess_kurtosis": 6.671515570492351,
        "return_acf_1": -0.07203141078449846,
        "abs_return_acf_1": 0.2864616219635743,
        "abs_return_acf_5": 0.23236593192966773,
        "abs_return_acf_20": 0.15487480677511928,
        "quantile_01": -0.039787473439672184,
        "quantile_99": 0.03964374852857531,
        "hill_tail_index": 2.4280651374006106
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01695272130476402,
        "excess_kurtosis": 19.433708032224505,
        "return_acf_1": -0.02844258391865439,
        "abs_return_acf_1": 0.387099153042688,
        "abs_return_acf_5": 0.27188956780233037,
        "abs_return_acf_20": 0.2329044504740958,
        "quantile_01": -0.04503971613592124,
        "quantile_99": 0.04294157737386268,
        "hill_tail_index": 2.1429350602687562
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01637649405099534,
        "excess_kurtosis": 4.013372461153001,
        "return_acf_1": -0.12067138931659707,
        "abs_return_acf_1": 0.3039319775754414,
        "abs_return_acf_5": 0.2924061814720139,
        "abs_return_acf_20": 0.18183880046062154,
        "quantile_01": -0.0562582703997646,
        "quantile_99": 0.04321769156021073,
        "hill_tail_index": 3.147588565745525
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01601143500055642,
        "excess_kurtosis": 7.906338945381943,
        "return_acf_1": -0.04545683590209376,
        "abs_return_acf_1": 0.3683211000551014,
        "abs_return_acf_5": 0.2923016588989342,
        "abs_return_acf_20": 0.19847672112685535,
        "quantile_01": -0.04065790639671233,
        "quantile_99": 0.04811284009525135,
        "hill_tail_index": 2.5106139976684614
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.014874740445020334,
        "excess_kurtosis": 1.5833577783726103,
        "return_acf_1": -0.15212002831770224,
        "abs_return_acf_1": 0.23327760097217506,
        "abs_return_acf_5": 0.1514585719596802,
        "abs_return_acf_20": 0.12542535646766428,
        "quantile_01": -0.03594190833709099,
        "quantile_99": 0.03927598732375048,
        "hill_tail_index": 3.9931669832334067
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01974585429693351,
        "excess_kurtosis": 5.945780258891633,
        "return_acf_1": -0.03224505357266722,
        "abs_return_acf_1": 0.4219250733323115,
        "abs_return_acf_5": 0.34747582659929566,
        "abs_return_acf_20": 0.3461494521591899,
        "quantile_01": -0.06326166023773337,
        "quantile_99": 0.057326347405213446,
        "hill_tail_index": 3.331096827031144
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016484341778019166,
        "excess_kurtosis": 3.9108372082022926,
        "return_acf_1": -0.14379739145440087,
        "abs_return_acf_1": 0.24749976833790202,
        "abs_return_acf_5": 0.28802923015780735,
        "abs_return_acf_20": 0.21616274897366608,
        "quantile_01": -0.05051902125306496,
        "quantile_99": 0.044162794078089235,
        "hill_tail_index": 3.5676096063018368
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.014874530099582103,
        "excess_kurtosis": 5.659302800512245,
        "return_acf_1": -0.16686265564819172,
        "abs_return_acf_1": 0.23512332595023613,
        "abs_return_acf_5": 0.20536976532186865,
        "abs_return_acf_20": 0.15517657481239241,
        "quantile_01": -0.03818508826042021,
        "quantile_99": 0.03937798521381221,
        "hill_tail_index": 3.040716154351115
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019714948824270894,
        "excess_kurtosis": 5.506166236100075,
        "return_acf_1": -0.08476272364102648,
        "abs_return_acf_1": 0.3465583574953917,
        "abs_return_acf_5": 0.38587973976373746,
        "abs_return_acf_20": 0.3350043609946987,
        "quantile_01": -0.05702648596703163,
        "quantile_99": 0.06141698675187942,
        "hill_tail_index": 4.023941246427268
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.014281091746826997,
        "excess_kurtosis": 2.4051142087607618,
        "return_acf_1": -0.13085665388152273,
        "abs_return_acf_1": 0.21214786302783287,
        "abs_return_acf_5": 0.21179930980146353,
        "abs_return_acf_20": 0.16698997835082988,
        "quantile_01": -0.034223365889980865,
        "quantile_99": 0.039191679688106495,
        "hill_tail_index": 3.938838620505995
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01681100634501647,
        "excess_kurtosis": 2.518450173723572,
        "return_acf_1": -0.10525017590337284,
        "abs_return_acf_1": 0.2539695541191911,
        "abs_return_acf_5": 0.20622375660473155,
        "abs_return_acf_20": 0.16839033554985539,
        "quantile_01": -0.048306598784038104,
        "quantile_99": 0.04837623123325423,
        "hill_tail_index": 4.960608692127292
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01608817681719676,
        "excess_kurtosis": 6.796387777113273,
        "return_acf_1": -0.13091063160253527,
        "abs_return_acf_1": 0.20996155231821464,
        "abs_return_acf_5": 0.2093054818456068,
        "abs_return_acf_20": 0.18657465392335973,
        "quantile_01": -0.037363516422080585,
        "quantile_99": 0.04038900250940346,
        "hill_tail_index": 2.8263106646362712
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01589815752954618,
        "excess_kurtosis": 2.3723362287302248,
        "return_acf_1": -0.12100685321911164,
        "abs_return_acf_1": 0.2201473432644874,
        "abs_return_acf_5": 0.2561634028445394,
        "abs_return_acf_20": 0.2062316913928113,
        "quantile_01": -0.048027608898352045,
        "quantile_99": 0.041263292722165605,
        "hill_tail_index": 3.3129430989095
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.0151129161185794,
        "excess_kurtosis": 11.779243425236302,
        "return_acf_1": -0.0948486189876862,
        "abs_return_acf_1": 0.2866540191935724,
        "abs_return_acf_5": 0.25725091814297624,
        "abs_return_acf_20": 0.17192652826835686,
        "quantile_01": -0.036222632974665485,
        "quantile_99": 0.039261141404914414,
        "hill_tail_index": 2.8472999475692085
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.015351071781440555,
        "excess_kurtosis": 6.308594013965383,
        "return_acf_1": -0.15717236493164133,
        "abs_return_acf_1": 0.2160824760866551,
        "abs_return_acf_5": 0.3122314760413663,
        "abs_return_acf_20": 0.14652323800873582,
        "quantile_01": -0.034334401038307705,
        "quantile_99": 0.03823421788790885,
        "hill_tail_index": 2.417295466680782
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01831376397010194,
        "excess_kurtosis": 3.8721142587836157,
        "return_acf_1": -0.10313809500242807,
        "abs_return_acf_1": 0.306941221918881,
        "abs_return_acf_5": 0.29944078804249075,
        "abs_return_acf_20": 0.2862645026485755,
        "quantile_01": -0.05777720062272469,
        "quantile_99": 0.05427157202832813,
        "hill_tail_index": 4.459597499244053
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01710560339024961,
        "excess_kurtosis": 5.290013714475949,
        "return_acf_1": -0.0806527939231229,
        "abs_return_acf_1": 0.27951286267378883,
        "abs_return_acf_5": 0.2902072493836098,
        "abs_return_acf_20": 0.20567857334195436,
        "quantile_01": -0.04937341828962672,
        "quantile_99": 0.04709291437737576,
        "hill_tail_index": 3.200757208445224
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01649387607884879,
        "excess_kurtosis": 3.9378115266653895,
        "return_acf_1": -0.1349219625456873,
        "abs_return_acf_1": 0.2503763001704243,
        "abs_return_acf_5": 0.2717323356705458,
        "abs_return_acf_20": 0.2458948913402649,
        "quantile_01": -0.05075562021992892,
        "quantile_99": 0.04522542876116281,
        "hill_tail_index": 4.70687016001682
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01440673056285182,
        "excess_kurtosis": 4.362375263430205,
        "return_acf_1": -0.10188431920922511,
        "abs_return_acf_1": 0.1927862589476726,
        "abs_return_acf_5": 0.23043867963133052,
        "abs_return_acf_20": 0.2011958557023963,
        "quantile_01": -0.03526500459775364,
        "quantile_99": 0.037717392123380024,
        "hill_tail_index": 3.6364554250839634
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.015553482220447973,
        "excess_kurtosis": 7.330959401512638,
        "return_acf_1": -0.11540320343006219,
        "abs_return_acf_1": 0.274486900260022,
        "abs_return_acf_5": 0.24309016538369063,
        "abs_return_acf_20": 0.2448540878159359,
        "quantile_01": -0.041317142157483604,
        "quantile_99": 0.03715959173197474,
        "hill_tail_index": 3.186744405139539
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01594818990904127,
        "excess_kurtosis": 4.494924121232101,
        "return_acf_1": -0.17361021050885947,
        "abs_return_acf_1": 0.2811743240138981,
        "abs_return_acf_5": 0.2464598546157445,
        "abs_return_acf_20": 0.18702311052207354,
        "quantile_01": -0.04661853169804187,
        "quantile_99": 0.03651900335103612,
        "hill_tail_index": 3.0311231387641833
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
