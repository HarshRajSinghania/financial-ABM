# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27191
Run ID: `8692bb6ad11b246177fd6e2095af7186c1be9ca15e46ce240af7abe0ff473833`
Result fingerprint: `25e3ac216753fa976e5cb0663306654aa41295eb3a1bba17c23e6154797fc821`

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
    "equal_weight_sd": -0.7436897643541661,
    "equal_weight_raw": -11.155346465312494,
    "fixed_start_cap_weight_sd": -0.7685389124599767,
    "fixed_start_cap_weight_raw": -11.528083686899652,
    "end_cap_weight_sd": -0.765161670149144,
    "end_cap_weight_raw": -11.47742505223716
  },
  "full_period_change": {
    "equal_weight_sd": -1.134463573877974,
    "equal_weight_raw": -17.01695360816961
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0520413800004234,
    "inflation_mean_sd": 0.5745152116402118
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.17808167180040116,
    "equal_weight_raw": 2.671225077006017,
    "fixed_start_cap_weight_sd": 0.16791681092167443,
    "fixed_start_cap_weight_raw": 2.518752163825116,
    "end_cap_weight_sd": 0.16723472603538947,
    "end_cap_weight_raw": 2.5085208905308423
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7665476190476156,
      "change_raw": -11.498214285714234,
      "decay_adjusted_gain_sd": 0.18583333333333663
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8557142857142825,
      "change_raw": -12.835714285714237,
      "decay_adjusted_gain_sd": 0.09666666666666981
    },
    "small": {
      "count": 18,
      "change_sd": -0.6838678612251998,
      "change_raw": -10.258017918377998,
      "decay_adjusted_gain_sd": 0.2174972307784442
    },
    "large_minus_small_sd": -0.08267975782241577,
    "large_minus_small_raw": -1.2401963673362366
  },
  "inflation": {
    "initial_mean_sd": 0.29666666666666663,
    "final_mean_sd": 0.5672499999999999,
    "mean_sd": 0.4413798917568693,
    "mean_absolute_raw_gap": 6.6206983763530385,
    "final_absolute_raw_gap": 8.50875,
    "mean_range_fraction": 0.06620698376353039
  },
  "impact": {
    "initial_share": 0.24666666666666667,
    "final_share": 0.3333333333333333,
    "initial_wealth_share": 0.1828143072223254,
    "final_wealth_share": 0.26639997348758376
  },
  "pricing_slope": {
    "mean": -0.0017562524930723393,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.05629862561307452,
    "real_improvement_cost": 0.04683870575895266,
    "washing_cost": 0.009459919854121862,
    "fine_transfer": 0.025255349208692154,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08155397482176667,
    "resource_cost_fraction_initial_cap": 0.001876620853769151,
    "private_net_outflow_fraction_initial_cap": 0.0027184658273922226,
    "fine_transfer_fraction_initial_cap": 0.0008418449736230719,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.018043640870974615,
    "unapplied_final_day_resource_cost": 0.01986306756642905
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 94.89485925871928,
    "beneficial_raw_gain_per_resource_cost": 1423.4228888807893,
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
    "accrued_cost": 3.109510409154602,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.13331993296412542,
    "accrued_cost_fraction_initial_cap": 0.10365034697182007,
    "mean_contract_rate": 0.04330357234042389,
    "maximum_ledger_error": 4.743384504624082e-20
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
    "price_cap_hits": 3,
    "maximum_relative_cash_error": 1.2419595530678866e-15,
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
      "minimum": -0.2814479176950691,
      "maximum": 0.0028964426775026767,
      "mean": -0.09003308804141538,
      "median": -0.08098253067442848,
      "quantile_05": -0.19347076768008445,
      "quantile_95": 0.0012412456280009095
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
      "minimum": 0.4190768479756582,
      "maximum": 0.8296184932091264,
      "mean": 0.7002404653247536,
      "median": 0.7216198988965661,
      "quantile_05": 0.5459274173158929,
      "quantile_95": 0.798732164001067
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
        "daily_volatility": 0.023160258120149733,
        "excess_kurtosis": 16.47525007197882,
        "return_acf_1": -0.09324120526783863,
        "abs_return_acf_1": 0.4168578958140156,
        "abs_return_acf_5": 0.3796326246852079,
        "abs_return_acf_20": 0.2628925354206512,
        "quantile_01": -0.08553045336315501,
        "quantile_99": 0.06202283334766831,
        "hill_tail_index": 2.362792585239453
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02250008849526045,
        "excess_kurtosis": 13.6835708400193,
        "return_acf_1": -0.19344876006153172,
        "abs_return_acf_1": 0.5034260605233455,
        "abs_return_acf_5": 0.4233147522117031,
        "abs_return_acf_20": 0.2735166940029943,
        "quantile_01": -0.07573701585839572,
        "quantile_99": 0.06072198448177253,
        "hill_tail_index": 3.0958273965458707
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022787774893085647,
        "excess_kurtosis": 17.37624863688423,
        "return_acf_1": -0.09611179782718951,
        "abs_return_acf_1": 0.4954077244949641,
        "abs_return_acf_5": 0.391827850553792,
        "abs_return_acf_20": 0.31115917279700667,
        "quantile_01": -0.08262064374578462,
        "quantile_99": 0.06132862586921181,
        "hill_tail_index": 3.034956492340353
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021418065135907684,
        "excess_kurtosis": 7.500354318390922,
        "return_acf_1": -0.1804777232896214,
        "abs_return_acf_1": 0.47364425930244364,
        "abs_return_acf_5": 0.39487109570599527,
        "abs_return_acf_20": 0.3211514912763472,
        "quantile_01": -0.07285336638868165,
        "quantile_99": 0.06502373290786577,
        "hill_tail_index": 3.753749616327284
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022254385629500852,
        "excess_kurtosis": 13.184037825019573,
        "return_acf_1": -0.014041786990118715,
        "abs_return_acf_1": 0.34803850968511607,
        "abs_return_acf_5": 0.43274756453345997,
        "abs_return_acf_20": 0.2819941461329644,
        "quantile_01": -0.0771575713756398,
        "quantile_99": 0.06199938873604711,
        "hill_tail_index": 2.6946505464576203
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02438122846671286,
        "excess_kurtosis": 16.109638231239817,
        "return_acf_1": -0.15425204102376652,
        "abs_return_acf_1": 0.5254324711043885,
        "abs_return_acf_5": 0.4164547853421483,
        "abs_return_acf_20": 0.33800157442446366,
        "quantile_01": -0.08208582496316605,
        "quantile_99": 0.0726881044714337,
        "hill_tail_index": 2.708582299970075
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0204492569055567,
        "excess_kurtosis": 10.062472092623151,
        "return_acf_1": 0.00153216705785471,
        "abs_return_acf_1": 0.3914611476901324,
        "abs_return_acf_5": 0.3257597536648164,
        "abs_return_acf_20": 0.24491698698035783,
        "quantile_01": -0.08051937764142204,
        "quantile_99": 0.054910302539908716,
        "hill_tail_index": 2.9682355347133598
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.024320278031136306,
        "excess_kurtosis": 30.157026792148642,
        "return_acf_1": -0.19348877391344577,
        "abs_return_acf_1": 0.5332989143697426,
        "abs_return_acf_5": 0.33731235128186265,
        "abs_return_acf_20": 0.31325949550778376,
        "quantile_01": -0.07454187076402798,
        "quantile_99": 0.06916516787049551,
        "hill_tail_index": 2.4844695569660673
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.022921753986581885,
        "excess_kurtosis": 14.742430378463713,
        "return_acf_1": -0.06703907023693215,
        "abs_return_acf_1": 0.40066182637100456,
        "abs_return_acf_5": 0.4115913968375421,
        "abs_return_acf_20": 0.24665127827244376,
        "quantile_01": -0.07381751380154879,
        "quantile_99": 0.07027023510934524,
        "hill_tail_index": 2.6158906592785915
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021986565967382608,
        "excess_kurtosis": 16.405773042296758,
        "return_acf_1": -0.0801576423660403,
        "abs_return_acf_1": 0.4366113700093616,
        "abs_return_acf_5": 0.3971961857279158,
        "abs_return_acf_20": 0.25157461154038757,
        "quantile_01": -0.07298558763458657,
        "quantile_99": 0.06408369190454392,
        "hill_tail_index": 2.640716334003579
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.025231996505610272,
        "excess_kurtosis": 16.694228214907024,
        "return_acf_1": -0.06232081772530325,
        "abs_return_acf_1": 0.5487922101122644,
        "abs_return_acf_5": 0.46127905522495605,
        "abs_return_acf_20": 0.2996649820145655,
        "quantile_01": -0.09824111533359384,
        "quantile_99": 0.06000081932617298,
        "hill_tail_index": 2.443470153994311
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02177565558237794,
        "excess_kurtosis": 10.969483808486329,
        "return_acf_1": -0.12778165211937437,
        "abs_return_acf_1": 0.47850717807481347,
        "abs_return_acf_5": 0.402515745446075,
        "abs_return_acf_20": 0.32565832725406924,
        "quantile_01": -0.08139272870109565,
        "quantile_99": 0.06172313502371005,
        "hill_tail_index": 2.9728292539358567
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02129183829701487,
        "excess_kurtosis": 8.984018479286036,
        "return_acf_1": -0.07204235832625897,
        "abs_return_acf_1": 0.4146157507234746,
        "abs_return_acf_5": 0.35199997684307577,
        "abs_return_acf_20": 0.29941763278915473,
        "quantile_01": -0.07862558711321622,
        "quantile_99": 0.056861725010859836,
        "hill_tail_index": 3.2259459400123265
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02202555028491212,
        "excess_kurtosis": 15.647716781103458,
        "return_acf_1": -0.03262467242534075,
        "abs_return_acf_1": 0.44450994508119474,
        "abs_return_acf_5": 0.36409703320599973,
        "abs_return_acf_20": 0.2821464049620095,
        "quantile_01": -0.0694682385312662,
        "quantile_99": 0.05930680632056743,
        "hill_tail_index": 2.6598197548262634
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02706073357583359,
        "excess_kurtosis": 28.20357853037042,
        "return_acf_1": -0.2814479176950691,
        "abs_return_acf_1": 0.49031995265010236,
        "abs_return_acf_5": 0.3377694560512137,
        "abs_return_acf_20": 0.3718938099979241,
        "quantile_01": -0.07775128692696849,
        "quantile_99": 0.0807475691877396,
        "hill_tail_index": 1.9682516242012376
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022529940751123183,
        "excess_kurtosis": 13.916013892925829,
        "return_acf_1": -0.00908005956674917,
        "abs_return_acf_1": 0.43157343893005917,
        "abs_return_acf_5": 0.3385491309173858,
        "abs_return_acf_20": 0.3180459047915409,
        "quantile_01": -0.07103279035514891,
        "quantile_99": 0.0663805312531444,
        "hill_tail_index": 2.8855717788647364
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.020971651219799214,
        "excess_kurtosis": 9.21670683007864,
        "return_acf_1": 0.000885674991512935,
        "abs_return_acf_1": 0.4754028601527698,
        "abs_return_acf_5": 0.42150969993270165,
        "abs_return_acf_20": 0.3369859908215693,
        "quantile_01": -0.07832889770774992,
        "quantile_99": 0.060622325668218985,
        "hill_tail_index": 3.477724413104866
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02437096191255719,
        "excess_kurtosis": 21.30458365960917,
        "return_acf_1": 0.0028964426775026767,
        "abs_return_acf_1": 0.4605302361698127,
        "abs_return_acf_5": 0.48821978868361926,
        "abs_return_acf_20": 0.2650020100758649,
        "quantile_01": -0.0850388837152649,
        "quantile_99": 0.06578706063370067,
        "hill_tail_index": 2.3197667723106985
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02199399165860741,
        "excess_kurtosis": 14.388166549843252,
        "return_acf_1": -0.06261774215721777,
        "abs_return_acf_1": 0.4572355877949359,
        "abs_return_acf_5": 0.3925674959689655,
        "abs_return_acf_20": 0.23024016942792738,
        "quantile_01": -0.0764195666967095,
        "quantile_99": 0.05994251959887502,
        "hill_tail_index": 2.3755491116337732
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.024049435236639764,
        "excess_kurtosis": 21.435992143269978,
        "return_acf_1": -0.16472739238203687,
        "abs_return_acf_1": 0.48336328965495046,
        "abs_return_acf_5": 0.3363230953725144,
        "abs_return_acf_20": 0.2394340454898967,
        "quantile_01": -0.07586470393411927,
        "quantile_99": 0.06005897963894113,
        "hill_tail_index": 2.041128631148186
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019949821222987794,
        "excess_kurtosis": 5.189373010678647,
        "return_acf_1": -0.0936158554701771,
        "abs_return_acf_1": 0.4307368095087451,
        "abs_return_acf_5": 0.4352658136862673,
        "abs_return_acf_20": 0.30685648494080126,
        "quantile_01": -0.06478794046561673,
        "quantile_99": 0.06561084437460621,
        "hill_tail_index": 3.809877480465135
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.020831563965458433,
        "excess_kurtosis": 9.030840946228833,
        "return_acf_1": -0.07262230853751796,
        "abs_return_acf_1": 0.4298686685249141,
        "abs_return_acf_5": 0.41328494403681376,
        "abs_return_acf_20": 0.3098273240305643,
        "quantile_01": -0.0662245591010162,
        "quantile_99": 0.059704456728322905,
        "hill_tail_index": 3.184456840271315
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02426911224841096,
        "excess_kurtosis": 15.330109590644952,
        "return_acf_1": -0.05807569974351449,
        "abs_return_acf_1": 0.5730721266916173,
        "abs_return_acf_5": 0.4977992844439921,
        "abs_return_acf_20": 0.26899253731454914,
        "quantile_01": -0.0851764915254866,
        "quantile_99": 0.06620480346186194,
        "hill_tail_index": 2.777745872230196
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.023995131761149095,
        "excess_kurtosis": 12.71298733978713,
        "return_acf_1": -0.11836271712486124,
        "abs_return_acf_1": 0.4550751819700397,
        "abs_return_acf_5": 0.45032445311982783,
        "abs_return_acf_20": 0.33296048133734096,
        "quantile_01": -0.08171478042993419,
        "quantile_99": 0.07803732196024062,
        "hill_tail_index": 2.9121265764965907
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.024366514422285875,
        "excess_kurtosis": 15.125151118105531,
        "return_acf_1": -0.11673356870795738,
        "abs_return_acf_1": 0.5179843843741023,
        "abs_return_acf_5": 0.46615075392809185,
        "abs_return_acf_20": 0.273728195842216,
        "quantile_01": -0.08899928934366906,
        "quantile_99": 0.07415127247167898,
        "hill_tail_index": 3.2735504361007837
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.023965318534073788,
        "excess_kurtosis": 14.62304655449201,
        "return_acf_1": -0.12158305270215441,
        "abs_return_acf_1": 0.48334770214715284,
        "abs_return_acf_5": 0.4343742811228871,
        "abs_return_acf_20": 0.2955273537248508,
        "quantile_01": -0.08163579416219588,
        "quantile_99": 0.06853230653971601,
        "hill_tail_index": 2.8824472483664825
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02274813727227248,
        "excess_kurtosis": 9.815742975040859,
        "return_acf_1": -0.02884931541251353,
        "abs_return_acf_1": 0.43585823550286984,
        "abs_return_acf_5": 0.36966883204049783,
        "abs_return_acf_20": 0.284077262806904,
        "quantile_01": -0.08176392160270639,
        "quantile_99": 0.06234918705094171,
        "hill_tail_index": 2.8186745360388583
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02189045543645656,
        "excess_kurtosis": 10.540735179856384,
        "return_acf_1": -0.08180741898281667,
        "abs_return_acf_1": 0.35437872447729307,
        "abs_return_acf_5": 0.4142164789140996,
        "abs_return_acf_20": 0.27916940268625023,
        "quantile_01": -0.07962665932546967,
        "quantile_99": 0.05670308936859824,
        "hill_tail_index": 2.3441544247262365
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023892405108129504,
        "excess_kurtosis": 12.367439957242699,
        "return_acf_1": -0.11990091485419056,
        "abs_return_acf_1": 0.4829228908611443,
        "abs_return_acf_5": 0.48500955199538104,
        "abs_return_acf_20": 0.32015303809556295,
        "quantile_01": -0.08017195702795211,
        "quantile_99": 0.0722589756894855,
        "hill_tail_index": 2.899280787276915
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021179786699341542,
        "excess_kurtosis": 14.819918132772855,
        "return_acf_1": -0.009854661059793162,
        "abs_return_acf_1": 0.4388430574589193,
        "abs_return_acf_5": 0.3826598626134882,
        "abs_return_acf_20": 0.2454529810642144,
        "quantile_01": -0.0677101735099311,
        "quantile_99": 0.06104739344587445,
        "hill_tail_index": 2.9319413204470623
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
