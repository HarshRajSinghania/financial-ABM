# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27065
Run ID: `873bcba6326c21f682e06f7dd3e5a411e14502a90093d1986065957d82252f0c`
Result fingerprint: `66af6a78e087e522171c3476cbeb2859c57e9cadbcd14eee59e871c2897c875c`

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
    "equal_weight_sd": -0.5941309523809492,
    "equal_weight_raw": -8.91196428571424,
    "fixed_start_cap_weight_sd": -0.6339989750960165,
    "fixed_start_cap_weight_raw": -9.509984626440248,
    "end_cap_weight_sd": -0.6422672872002255,
    "end_cap_weight_raw": -9.634009308003385
  },
  "full_period_change": {
    "equal_weight_sd": -0.9053214285714237,
    "equal_weight_raw": -13.579821428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.8397103174603129,
    "inflation_mean_sd": 0.6179305555555556
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.35825000000000323,
    "equal_weight_raw": 5.373750000000048,
    "fixed_start_cap_weight_sd": 0.3183819772849358,
    "fixed_start_cap_weight_raw": 4.775729659274037,
    "end_cap_weight_sd": 0.3101136651807269,
    "end_cap_weight_raw": 4.651704977710903
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7007142857142825,
      "change_raw": -10.510714285714238,
      "decay_adjusted_gain_sd": 0.25166666666666987
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5526587301587269,
      "change_raw": -8.289880952380903,
      "decay_adjusted_gain_sd": 0.3997222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.5971031746031714,
      "change_raw": -8.956547619047571,
      "decay_adjusted_gain_sd": 0.355277777777781
    },
    "large_minus_small_sd": -0.1036111111111111,
    "large_minus_small_raw": -1.5541666666666665
  },
  "inflation": {
    "initial_mean_sd": 0.25583333333333336,
    "final_mean_sd": 0.6330000000000001,
    "mean_sd": 0.46108076602830966,
    "mean_absolute_raw_gap": 6.916211490424646,
    "final_absolute_raw_gap": 9.494999999999997,
    "mean_range_fraction": 0.06916211490424647
  },
  "impact": {
    "initial_share": 0.3333333333333333,
    "final_share": 0.3466666666666667,
    "initial_wealth_share": 0.31388098036904416,
    "final_wealth_share": 0.3353535530668833
  },
  "pricing_slope": {
    "mean": -0.0015884740862766842,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.0641134858936697,
    "real_improvement_cost": 0.05338453913141662,
    "washing_cost": 0.010728946762253088,
    "fine_transfer": 0.016374288511411435,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08048777440508115,
    "resource_cost_fraction_initial_cap": 0.002137116196455657,
    "private_net_outflow_fraction_initial_cap": 0.0026829258135027054,
    "fine_transfer_fraction_initial_cap": 0.0005458096170470479,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004687641534929234,
    "unapplied_final_day_resource_cost": 0.001301760723560749
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 167.63243879492848,
    "beneficial_raw_gain_per_resource_cost": 2514.486581923927,
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
    "accrued_cost": 3.1409477475024516,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.16475727131197523,
    "accrued_cost_fraction_initial_cap": 0.10469825825008174,
    "mean_contract_rate": 0.04297810923568899,
    "maximum_ledger_error": 1.1180834903756764e-19
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
    "maximum_relative_cash_error": 1.6342690012153617e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.2494868855136418,
      "maximum": -0.14079183039027945,
      "mean": -0.207324537434225,
      "median": -0.2149991440468133,
      "quantile_05": -0.24633931139774648,
      "quantile_95": -0.15973511013419836
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
      "minimum": 0.25895581101154924,
      "maximum": 0.85104991114377,
      "mean": 0.6512655848035582,
      "median": 0.6779644580563302,
      "quantile_05": 0.37199871200224255,
      "quantile_95": 0.8144407806124739
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
        "daily_volatility": 0.02277000431677397,
        "excess_kurtosis": 24.166378828663834,
        "return_acf_1": -0.22524524222440118,
        "abs_return_acf_1": 0.3333537416802592,
        "abs_return_acf_5": 0.40703114608234653,
        "abs_return_acf_20": 0.20823565428398016,
        "quantile_01": -0.0729723491805126,
        "quantile_99": 0.05987651547553094,
        "hill_tail_index": 2.4733166780451694
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01977070008562363,
        "excess_kurtosis": 5.564236190758539,
        "return_acf_1": -0.17258382937578454,
        "abs_return_acf_1": 0.30662987887299087,
        "abs_return_acf_5": 0.3766526475304065,
        "abs_return_acf_20": 0.31545503171154304,
        "quantile_01": -0.048000582991456806,
        "quantile_99": 0.0579068826902904,
        "hill_tail_index": 2.989599074557592
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.026159568946907127,
        "excess_kurtosis": 30.10869350531309,
        "return_acf_1": -0.238054426409454,
        "abs_return_acf_1": 0.4142529690368316,
        "abs_return_acf_5": 0.49198374627363,
        "abs_return_acf_20": 0.24447520400236075,
        "quantile_01": -0.08088115908391538,
        "quantile_99": 0.05825032026455117,
        "hill_tail_index": 2.1053348703157226
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02110777370422432,
        "excess_kurtosis": 7.28584960231751,
        "return_acf_1": -0.19224923663071483,
        "abs_return_acf_1": 0.3543171645890247,
        "abs_return_acf_5": 0.3636734602370091,
        "abs_return_acf_20": 0.26477709670335275,
        "quantile_01": -0.06488424284632996,
        "quantile_99": 0.06356684973762317,
        "hill_tail_index": 3.837719237965642
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02318336688959603,
        "excess_kurtosis": 25.082630980333324,
        "return_acf_1": -0.21511279476251946,
        "abs_return_acf_1": 0.3860264583964916,
        "abs_return_acf_5": 0.44885152821218854,
        "abs_return_acf_20": 0.27523519205907915,
        "quantile_01": -0.07098687018584314,
        "quantile_99": 0.05500727884876083,
        "hill_tail_index": 2.8100890557810754
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.024003226443098703,
        "excess_kurtosis": 24.85073775626507,
        "return_acf_1": -0.2494868855136418,
        "abs_return_acf_1": 0.3912044950212103,
        "abs_return_acf_5": 0.4468895133306893,
        "abs_return_acf_20": 0.2396264891491007,
        "quantile_01": -0.07157387410192614,
        "quantile_99": 0.062022583777783656,
        "hill_tail_index": 2.3754157241625875
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.024275701417044104,
        "excess_kurtosis": 22.621385280372674,
        "return_acf_1": -0.24850633033689318,
        "abs_return_acf_1": 0.3208971628116305,
        "abs_return_acf_5": 0.3879573942427148,
        "abs_return_acf_20": 0.21045050948258123,
        "quantile_01": -0.08088648434274552,
        "quantile_99": 0.05486320076410358,
        "hill_tail_index": 1.8234380839449942
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021185129133439385,
        "excess_kurtosis": 13.08301040491257,
        "return_acf_1": -0.19370742448277686,
        "abs_return_acf_1": 0.373782194321816,
        "abs_return_acf_5": 0.3869261319239566,
        "abs_return_acf_20": 0.2607096192210251,
        "quantile_01": -0.07635307190796735,
        "quantile_99": 0.06374581324830084,
        "hill_tail_index": 3.24892429781565
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.023474765752866333,
        "excess_kurtosis": 26.139229734195595,
        "return_acf_1": -0.22511386155913066,
        "abs_return_acf_1": 0.45809377959144754,
        "abs_return_acf_5": 0.4326320999671249,
        "abs_return_acf_20": 0.24496354466151296,
        "quantile_01": -0.06810889791718795,
        "quantile_99": 0.05246493822450616,
        "hill_tail_index": 1.9474787341927224
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.025108927074870252,
        "excess_kurtosis": 31.274284316952823,
        "return_acf_1": -0.2176929584055896,
        "abs_return_acf_1": 0.4125287344559857,
        "abs_return_acf_5": 0.4612076712225052,
        "abs_return_acf_20": 0.26996870322567185,
        "quantile_01": -0.08212637136236661,
        "quantile_99": 0.06415582807699222,
        "hill_tail_index": 2.285602217081779
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02122535985176026,
        "excess_kurtosis": 20.64594607817289,
        "return_acf_1": -0.1590226072697955,
        "abs_return_acf_1": 0.3900466596420346,
        "abs_return_acf_5": 0.33319850448016736,
        "abs_return_acf_20": 0.2261128539423285,
        "quantile_01": -0.06948439553809314,
        "quantile_99": 0.05676836781168358,
        "hill_tail_index": 3.1825759841160783
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02414229590536123,
        "excess_kurtosis": 20.08992887766781,
        "return_acf_1": -0.217669951689965,
        "abs_return_acf_1": 0.45547269792198797,
        "abs_return_acf_5": 0.46384195737374967,
        "abs_return_acf_20": 0.27535069282422425,
        "quantile_01": -0.0740341155917788,
        "quantile_99": 0.07323700318665748,
        "hill_tail_index": 2.6355066618372653
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022506930964346136,
        "excess_kurtosis": 7.284285063919301,
        "return_acf_1": -0.1768768928221821,
        "abs_return_acf_1": 0.4236347102458995,
        "abs_return_acf_5": 0.3414124334902299,
        "abs_return_acf_20": 0.24672053442787764,
        "quantile_01": -0.0647573514745417,
        "quantile_99": 0.06427389088541208,
        "hill_tail_index": 3.252532841178424
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.025462456707981623,
        "excess_kurtosis": 36.07351021954853,
        "return_acf_1": -0.21383312601473625,
        "abs_return_acf_1": 0.3492082683955495,
        "abs_return_acf_5": 0.4605931026370864,
        "abs_return_acf_20": 0.24117554753616716,
        "quantile_01": -0.07843723284884467,
        "quantile_99": 0.06386939278610315,
        "hill_tail_index": 2.479626580182816
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.024497617524230155,
        "excess_kurtosis": 35.89024511601312,
        "return_acf_1": -0.22599798689656259,
        "abs_return_acf_1": 0.43236259316834375,
        "abs_return_acf_5": 0.44490008831636374,
        "abs_return_acf_20": 0.21945053531702086,
        "quantile_01": -0.07303925831920323,
        "quantile_99": 0.05404722095606586,
        "hill_tail_index": 1.949140750429044
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021064431618571664,
        "excess_kurtosis": 4.927197688632328,
        "return_acf_1": -0.243690732694345,
        "abs_return_acf_1": 0.3400582054182785,
        "abs_return_acf_5": 0.35880400745940955,
        "abs_return_acf_20": 0.2689723910260821,
        "quantile_01": -0.056567945405222385,
        "quantile_99": 0.05387568012903043,
        "hill_tail_index": 3.75230027310077
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021183458770170062,
        "excess_kurtosis": 9.772313472527648,
        "return_acf_1": -0.2306609017913306,
        "abs_return_acf_1": 0.33438085900113995,
        "abs_return_acf_5": 0.3539136534732064,
        "abs_return_acf_20": 0.19187284323275533,
        "quantile_01": -0.06946058708475106,
        "quantile_99": 0.05614405347193349,
        "hill_tail_index": 3.061671646323939
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.024185817134927262,
        "excess_kurtosis": 28.047761971093145,
        "return_acf_1": -0.223857134087671,
        "abs_return_acf_1": 0.4017506355679505,
        "abs_return_acf_5": 0.4490113153461157,
        "abs_return_acf_20": 0.24921850822467367,
        "quantile_01": -0.07603358238442678,
        "quantile_99": 0.05847584328688767,
        "hill_tail_index": 2.1515790923647407
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.023079315157276497,
        "excess_kurtosis": 25.14233426268335,
        "return_acf_1": -0.14079183039027945,
        "abs_return_acf_1": 0.32785027910533765,
        "abs_return_acf_5": 0.46450233536631463,
        "abs_return_acf_20": 0.21770449284431165,
        "quantile_01": -0.06539980974201409,
        "quantile_99": 0.05707005118789105,
        "hill_tail_index": 2.3586792392800384
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01910081875173336,
        "excess_kurtosis": 6.764863913438205,
        "return_acf_1": -0.16088966760139262,
        "abs_return_acf_1": 0.21854357277986447,
        "abs_return_acf_5": 0.3154679430678736,
        "abs_return_acf_20": 0.19869414158113605,
        "quantile_01": -0.05344778004939914,
        "quantile_99": 0.04986605918974167,
        "hill_tail_index": 3.285309372670815
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022776140617544325,
        "excess_kurtosis": 14.712700629775966,
        "return_acf_1": -0.21488549333110715,
        "abs_return_acf_1": 0.4579298605992761,
        "abs_return_acf_5": 0.4106906899832218,
        "abs_return_acf_20": 0.2645191895196853,
        "quantile_01": -0.0804164646196096,
        "quantile_99": 0.06131675825666122,
        "hill_tail_index": 2.815230053022696
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02302258421862498,
        "excess_kurtosis": 20.746750735059663,
        "return_acf_1": -0.22872913343954646,
        "abs_return_acf_1": 0.30710864585216735,
        "abs_return_acf_5": 0.3983080854190378,
        "abs_return_acf_20": 0.20288593093853993,
        "quantile_01": -0.06831767224505635,
        "quantile_99": 0.058752035983582314,
        "hill_tail_index": 2.3838349791434297
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024757677196672254,
        "excess_kurtosis": 17.453037943226093,
        "return_acf_1": -0.20623154994020618,
        "abs_return_acf_1": 0.330691730893553,
        "abs_return_acf_5": 0.4229732198133766,
        "abs_return_acf_20": 0.2796748156246342,
        "quantile_01": -0.07713875199767033,
        "quantile_99": 0.06588100736176511,
        "hill_tail_index": 2.959990372755409
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022351024622300722,
        "excess_kurtosis": 12.7647136976219,
        "return_acf_1": -0.1996679452210714,
        "abs_return_acf_1": 0.3301685734681183,
        "abs_return_acf_5": 0.3634087714008455,
        "abs_return_acf_20": 0.2544610464849045,
        "quantile_01": -0.07951155938028492,
        "quantile_99": 0.06287489933806223,
        "hill_tail_index": 2.624552444632612
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02264056639257496,
        "excess_kurtosis": 30.448955546601454,
        "return_acf_1": -0.2263350796717738,
        "abs_return_acf_1": 0.34197871515734973,
        "abs_return_acf_5": 0.4072066652365719,
        "abs_return_acf_20": 0.19488810447020638,
        "quantile_01": -0.07225590037172874,
        "quantile_99": 0.052699009302511965,
        "hill_tail_index": 2.5876261185852183
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019805660377195545,
        "excess_kurtosis": 4.823758041808466,
        "return_acf_1": -0.20869851951125487,
        "abs_return_acf_1": 0.3640294936547882,
        "abs_return_acf_5": 0.3539874660931979,
        "abs_return_acf_20": 0.21869905335241327,
        "quantile_01": -0.05773935096004965,
        "quantile_99": 0.058740028633792095,
        "hill_tail_index": 3.8624521297152334
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02426088494753863,
        "excess_kurtosis": 19.33434884158116,
        "return_acf_1": -0.2156938228737166,
        "abs_return_acf_1": 0.4103745924935889,
        "abs_return_acf_5": 0.48047584379064845,
        "abs_return_acf_20": 0.26961374390219733,
        "quantile_01": -0.07674097800273434,
        "quantile_99": 0.06281665303263635,
        "hill_tail_index": 2.3094151788625488
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.023449734528288083,
        "excess_kurtosis": 24.59828008722336,
        "return_acf_1": -0.179602312471654,
        "abs_return_acf_1": 0.31037810456936177,
        "abs_return_acf_5": 0.3966223749462664,
        "abs_return_acf_20": 0.23764069889037207,
        "quantile_01": -0.07993372742692455,
        "quantile_99": 0.06331128854405606,
        "hill_tail_index": 2.679607659358416
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022731510096893653,
        "excess_kurtosis": 13.531977331174115,
        "return_acf_1": -0.20824249863878533,
        "abs_return_acf_1": 0.42324633723329735,
        "abs_return_acf_5": 0.41552480392083707,
        "abs_return_acf_20": 0.34228257813504254,
        "quantile_01": -0.06678123447071352,
        "quantile_99": 0.06317603583579835,
        "hill_tail_index": 2.6397822127869484
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.024115209529107843,
        "excess_kurtosis": 31.783645391030724,
        "return_acf_1": -0.1606059469684685,
        "abs_return_acf_1": 0.350487176381721,
        "abs_return_acf_5": 0.4079897000370263,
        "abs_return_acf_20": 0.22967600383649917,
        "quantile_01": -0.06373664396844958,
        "quantile_99": 0.05690394110848055,
        "hill_tail_index": 2.0097035949882276
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
