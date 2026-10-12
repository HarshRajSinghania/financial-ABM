# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27255
Run ID: `47efa158d72e6f4ede30bdf053df0f1e8d4849ac50109673a687bad2fea283b0`
Result fingerprint: `6b97c66992816595028fb2990be005abba203ed19d273a817c508b08e86d2f8f`

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
    "equal_weight_sd": -0.7982142857142824,
    "equal_weight_raw": -11.973214285714239,
    "fixed_start_cap_weight_sd": -0.7770885230392063,
    "fixed_start_cap_weight_raw": -11.656327845588095,
    "end_cap_weight_sd": -0.7873289285754638,
    "end_cap_weight_raw": -11.809933928631956
  },
  "full_period_change": {
    "equal_weight_sd": -1.23048809523809,
    "equal_weight_raw": -18.45732142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.143592923280419,
    "inflation_mean_sd": 0.7599262566137567
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.15416666666666975,
    "equal_weight_raw": 2.312500000000047,
    "fixed_start_cap_weight_sd": 0.17529242934174602,
    "fixed_start_cap_weight_raw": 2.6293864401261904,
    "end_cap_weight_sd": 0.16505202380548836,
    "end_cap_weight_raw": 2.475780357082325
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8415476190476161,
      "change_raw": -12.62321428571424,
      "decay_adjusted_gain_sd": 0.11083333333333623
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8387698412698382,
      "change_raw": -12.581547619047573,
      "decay_adjusted_gain_sd": 0.11361111111111412
    },
    "small": {
      "count": 18,
      "change_sd": -0.7707142857142825,
      "change_raw": -11.560714285714237,
      "decay_adjusted_gain_sd": 0.1816666666666699
    },
    "large_minus_small_sd": -0.07083333333333364,
    "large_minus_small_raw": -1.0625000000000044
  },
  "inflation": {
    "initial_mean_sd": 0.23183333333333334,
    "final_mean_sd": 0.8006666666666665,
    "mean_sd": 0.5009275603663613,
    "mean_absolute_raw_gap": 7.513913405495422,
    "final_absolute_raw_gap": 12.01,
    "mean_range_fraction": 0.07513913405495422
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.44,
    "initial_wealth_share": 0.32827239172851935,
    "final_wealth_share": 0.5031127361515424
  },
  "pricing_slope": {
    "mean": -0.0026554086351286248,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.3571355303143949,
    "real_improvement_cost": 0.3465122957578378,
    "washing_cost": 0.010623234556557011,
    "fine_transfer": 0.004203750020748284,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.3613392803351432,
    "resource_cost_fraction_initial_cap": 0.011904517677146497,
    "private_net_outflow_fraction_initial_cap": 0.012044642677838108,
    "fine_transfer_fraction_initial_cap": 0.00014012500069160948,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010967720748864894,
    "unapplied_final_day_resource_cost": 0.03397456215193659
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 12.95026567625068,
    "beneficial_raw_gain_per_resource_cost": 194.25398514376022,
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
    "accrued_cost": 3.109244073180192,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.1330535969897157,
    "accrued_cost_fraction_initial_cap": 0.10364146910600641,
    "mean_contract_rate": 0.04426971359070102,
    "maximum_ledger_error": 9.486769009248164e-20
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
    "maximum_relative_cash_error": 2.322082935638093e-15,
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
      "minimum": -0.230558108202302,
      "maximum": -0.006161598707208627,
      "mean": -0.14614542376096243,
      "median": -0.14867595486123547,
      "quantile_05": -0.21458310103642425,
      "quantile_95": -0.058753470700401614
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
      "minimum": 0.28566093071429294,
      "maximum": 0.7747006275468473,
      "mean": 0.5392166772420312,
      "median": 0.5476180449381167,
      "quantile_05": 0.34238841624429417,
      "quantile_95": 0.7292403325317557
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
        "daily_volatility": 0.017599722410758543,
        "excess_kurtosis": 9.869457617536169,
        "return_acf_1": -0.18729129967467098,
        "abs_return_acf_1": 0.2805115226817845,
        "abs_return_acf_5": 0.23213502286624935,
        "abs_return_acf_20": 0.18744904192548997,
        "quantile_01": -0.050720031114232865,
        "quantile_99": 0.04079127457871655,
        "hill_tail_index": 2.502013423330151
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017298355574083577,
        "excess_kurtosis": 5.8391418245508415,
        "return_acf_1": -0.21546379581482086,
        "abs_return_acf_1": 0.41894755353667706,
        "abs_return_acf_5": 0.3394082651644309,
        "abs_return_acf_20": 0.2689022087389935,
        "quantile_01": -0.05512843976357616,
        "quantile_99": 0.05084773131419377,
        "hill_tail_index": 3.709274357711361
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019881071081992097,
        "excess_kurtosis": 10.61122523012623,
        "return_acf_1": -0.1886164309863893,
        "abs_return_acf_1": 0.4101842574347311,
        "abs_return_acf_5": 0.39854400671368156,
        "abs_return_acf_20": 0.2668212261072779,
        "quantile_01": -0.06517896539614339,
        "quantile_99": 0.04918982110666204,
        "hill_tail_index": 2.01132758799979
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021004517961193254,
        "excess_kurtosis": 6.792851690282205,
        "return_acf_1": -0.16103642532400125,
        "abs_return_acf_1": 0.4362332897799629,
        "abs_return_acf_5": 0.41930377742288705,
        "abs_return_acf_20": 0.32562528688254655,
        "quantile_01": -0.06665133180957421,
        "quantile_99": 0.06454065458041175,
        "hill_tail_index": 3.3332734134882496
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019804567524766586,
        "excess_kurtosis": 10.742859108668512,
        "return_acf_1": -0.19912235424180788,
        "abs_return_acf_1": 0.47506404991258927,
        "abs_return_acf_5": 0.39859592659788384,
        "abs_return_acf_20": 0.3139901349958558,
        "quantile_01": -0.06829295362037846,
        "quantile_99": 0.05725045182915327,
        "hill_tail_index": 2.8196167612863747
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017709850770871664,
        "excess_kurtosis": 6.856134081245694,
        "return_acf_1": -0.14447856562390407,
        "abs_return_acf_1": 0.40901073788704845,
        "abs_return_acf_5": 0.39491587984237725,
        "abs_return_acf_20": 0.2763048775287295,
        "quantile_01": -0.05145370471520867,
        "quantile_99": 0.054354796549816606,
        "hill_tail_index": 2.994457894390375
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022581555403080527,
        "excess_kurtosis": 9.01723875089004,
        "return_acf_1": -0.11482589256826108,
        "abs_return_acf_1": 0.5058145821698539,
        "abs_return_acf_5": 0.4628497672698524,
        "abs_return_acf_20": 0.34135273641729597,
        "quantile_01": -0.07866530772014235,
        "quantile_99": 0.0781538707484266,
        "hill_tail_index": 2.9383492687095374
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01754884904405459,
        "excess_kurtosis": 7.2618994500181255,
        "return_acf_1": -0.21350669630727284,
        "abs_return_acf_1": 0.4332685110359967,
        "abs_return_acf_5": 0.34874425303633183,
        "abs_return_acf_20": 0.28522925737949395,
        "quantile_01": -0.05538570396504271,
        "quantile_99": 0.04754402675777036,
        "hill_tail_index": 3.1322984893940817
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021895868332763656,
        "excess_kurtosis": 7.353765618657329,
        "return_acf_1": -0.05654078795765988,
        "abs_return_acf_1": 0.39665052874509216,
        "abs_return_acf_5": 0.4250956035127885,
        "abs_return_acf_20": 0.305100080233597,
        "quantile_01": -0.06229808965848247,
        "quantile_99": 0.060812082885705145,
        "hill_tail_index": 2.862259228082571
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020089079457297265,
        "excess_kurtosis": 9.58160429137088,
        "return_acf_1": -0.18679505247789271,
        "abs_return_acf_1": 0.38710771417365275,
        "abs_return_acf_5": 0.3582563958365505,
        "abs_return_acf_20": 0.27148516017923474,
        "quantile_01": -0.06036784756985108,
        "quantile_99": 0.057163311520405075,
        "hill_tail_index": 3.2327436172952595
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02073573693817107,
        "excess_kurtosis": 6.002734298298931,
        "return_acf_1": -0.17337793970610288,
        "abs_return_acf_1": 0.326672101162279,
        "abs_return_acf_5": 0.40363128144042476,
        "abs_return_acf_20": 0.35276059467346604,
        "quantile_01": -0.06867159508169803,
        "quantile_99": 0.06385822331527038,
        "hill_tail_index": 4.179958515305122
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017575351613469674,
        "excess_kurtosis": 6.708924746059893,
        "return_acf_1": -0.1077800160397321,
        "abs_return_acf_1": 0.39910020415520536,
        "abs_return_acf_5": 0.3332685073803627,
        "abs_return_acf_20": 0.29173540213281013,
        "quantile_01": -0.05578346310917234,
        "quantile_99": 0.04653377569545042,
        "hill_tail_index": 3.1961280987463088
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01942459097946028,
        "excess_kurtosis": 7.287953834177992,
        "return_acf_1": -0.1216251673242845,
        "abs_return_acf_1": 0.3134209428510988,
        "abs_return_acf_5": 0.37782871858311323,
        "abs_return_acf_20": 0.33565462511198335,
        "quantile_01": -0.07156680062168572,
        "quantile_99": 0.04627860716056261,
        "hill_tail_index": 2.39383184122719
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.017045925651891208,
        "excess_kurtosis": 3.5408737198239217,
        "return_acf_1": -0.14348285361845967,
        "abs_return_acf_1": 0.3518890647712456,
        "abs_return_acf_5": 0.2852007997400213,
        "abs_return_acf_20": 0.23975337817267733,
        "quantile_01": -0.04684617816684633,
        "quantile_99": 0.04478444801256811,
        "hill_tail_index": 4.037121533870335
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018615220704643765,
        "excess_kurtosis": 5.2065836344542795,
        "return_acf_1": -0.1817113921232177,
        "abs_return_acf_1": 0.3107654546920654,
        "abs_return_acf_5": 0.289896646835762,
        "abs_return_acf_20": 0.21458745771051205,
        "quantile_01": -0.0586326957865568,
        "quantile_99": 0.04429687320955523,
        "hill_tail_index": 3.123899773737849
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019328954191008982,
        "excess_kurtosis": 6.130740192382531,
        "return_acf_1": -0.11191704952416207,
        "abs_return_acf_1": 0.3836763106080394,
        "abs_return_acf_5": 0.3881301348559126,
        "abs_return_acf_20": 0.3969938126427335,
        "quantile_01": -0.06487638838643736,
        "quantile_99": 0.04920896716002441,
        "hill_tail_index": 2.826329168361516
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01700550063067151,
        "excess_kurtosis": 1.7153236772849718,
        "return_acf_1": -0.1528657234112273,
        "abs_return_acf_1": 0.2324132782404236,
        "abs_return_acf_5": 0.21984753488324468,
        "abs_return_acf_20": 0.21327747080530368,
        "quantile_01": -0.04754382791450293,
        "quantile_99": 0.046927152791378934,
        "hill_tail_index": 6.877464384820553
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018629064176868725,
        "excess_kurtosis": 9.379471883646438,
        "return_acf_1": -0.10780323437354425,
        "abs_return_acf_1": 0.4596833225834965,
        "abs_return_acf_5": 0.41795546184914195,
        "abs_return_acf_20": 0.19025004895197511,
        "quantile_01": -0.06038932794353439,
        "quantile_99": 0.044671520197735654,
        "hill_tail_index": 2.231794363395062
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01999976730194437,
        "excess_kurtosis": 4.946990348069459,
        "return_acf_1": -0.230558108202302,
        "abs_return_acf_1": 0.38438852558264086,
        "abs_return_acf_5": 0.3549803970116119,
        "abs_return_acf_20": 0.2788122457620896,
        "quantile_01": -0.06829178641598713,
        "quantile_99": 0.04981742035997765,
        "hill_tail_index": 2.889709236343769
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020077211278148797,
        "excess_kurtosis": 8.753740401758344,
        "return_acf_1": -0.15380789998267108,
        "abs_return_acf_1": 0.40982457737480604,
        "abs_return_acf_5": 0.4579319733319834,
        "abs_return_acf_20": 0.3285235925182926,
        "quantile_01": -0.06683834686986918,
        "quantile_99": 0.05401469263776902,
        "hill_tail_index": 2.856672818929695
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017940147569605394,
        "excess_kurtosis": 11.367727942181004,
        "return_acf_1": -0.19005926914006083,
        "abs_return_acf_1": 0.34191293280076346,
        "abs_return_acf_5": 0.3510897157203745,
        "abs_return_acf_20": 0.2426897599116886,
        "quantile_01": -0.055934732557896744,
        "quantile_99": 0.047951413537928485,
        "hill_tail_index": 2.742860732647298
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020415063321696767,
        "excess_kurtosis": 9.235770507338461,
        "return_acf_1": -0.061457860719308144,
        "abs_return_acf_1": 0.3382554594194698,
        "abs_return_acf_5": 0.3333149462401097,
        "abs_return_acf_20": 0.3389707133314948,
        "quantile_01": -0.06638652949067506,
        "quantile_99": 0.050590764974568395,
        "hill_tail_index": 3.0930883415208053
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018901016181689524,
        "excess_kurtosis": 5.969325542611017,
        "return_acf_1": -0.09896824811467908,
        "abs_return_acf_1": 0.2881276374520515,
        "abs_return_acf_5": 0.36496988866369034,
        "abs_return_acf_20": 0.2790119056074074,
        "quantile_01": -0.055775264119704245,
        "quantile_99": 0.05226434075685675,
        "hill_tail_index": 3.3030562342102674
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01774731537989682,
        "excess_kurtosis": 3.772653205452431,
        "return_acf_1": -0.13293862410888313,
        "abs_return_acf_1": 0.2641556455662054,
        "abs_return_acf_5": 0.185060082487237,
        "abs_return_acf_20": 0.22897211455897423,
        "quantile_01": -0.04841198323900654,
        "quantile_99": 0.046343035335568744,
        "hill_tail_index": 4.145689792865221
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019722354061615932,
        "excess_kurtosis": 7.317101974494392,
        "return_acf_1": -0.1712112347642581,
        "abs_return_acf_1": 0.4078136055188656,
        "abs_return_acf_5": 0.45222184489595457,
        "abs_return_acf_20": 0.39202496040653784,
        "quantile_01": -0.058930243525143006,
        "quantile_99": 0.05486627579858206,
        "hill_tail_index": 3.678158003868603
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.016180377041623496,
        "excess_kurtosis": 4.07197060681261,
        "return_acf_1": -0.14448618631124363,
        "abs_return_acf_1": 0.24909960613563026,
        "abs_return_acf_5": 0.22739987820204918,
        "abs_return_acf_20": 0.19603521870034163,
        "quantile_01": -0.04911137348477169,
        "quantile_99": 0.040523562010325816,
        "hill_tail_index": 3.30155179423692
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02347673939830411,
        "excess_kurtosis": 32.21222551928028,
        "return_acf_1": -0.006161598707208627,
        "abs_return_acf_1": 0.41341265817812206,
        "abs_return_acf_5": 0.47316022485850406,
        "abs_return_acf_20": 0.3120864685500038,
        "quantile_01": -0.06876631246328382,
        "quantile_99": 0.041355275039303564,
        "hill_tail_index": 1.7130170912001466
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018041342480884213,
        "excess_kurtosis": 5.423415307646236,
        "return_acf_1": -0.10952048812220994,
        "abs_return_acf_1": 0.273146678530876,
        "abs_return_acf_5": 0.24551968121241347,
        "abs_return_acf_20": 0.27710967156349126,
        "quantile_01": -0.05220827454338962,
        "quantile_99": 0.05226637531400395,
        "hill_tail_index": 4.1786667689900385
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01932699818853376,
        "excess_kurtosis": 10.46058347706258,
        "return_acf_1": -0.1277198728874542,
        "abs_return_acf_1": 0.3871283733343207,
        "abs_return_acf_5": 0.41962663691914504,
        "abs_return_acf_20": 0.24259698576879093,
        "quantile_01": -0.057676721099003646,
        "quantile_99": 0.0530010117651171,
        "hill_tail_index": 3.1224670068863034
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016529904111124656,
        "excess_kurtosis": 4.372091998200661,
        "return_acf_1": -0.18923264467118314,
        "abs_return_acf_1": 0.2866666811937912,
        "abs_return_acf_5": 0.3303906387402544,
        "abs_return_acf_20": 0.2170174577413307,
        "quantile_01": -0.04923517295470175,
        "quantile_99": 0.03947771714557389,
        "hill_tail_index": 3.3580862638652014
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
