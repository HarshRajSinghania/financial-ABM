# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27306
Run ID: `d2fa7c696250271b4687524833df8df6553cb5f7ce76e40c89688352f63632e4`
Result fingerprint: `1fa9623adc73adc6a4318ab08b72902f00946927354ca67faf26618de6a7d65b`

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
    "equal_weight_sd": -0.6717976190476157,
    "equal_weight_raw": -10.076964285714237,
    "fixed_start_cap_weight_sd": -0.7230922259886057,
    "fixed_start_cap_weight_raw": -10.84638338982908,
    "end_cap_weight_sd": -0.7622118385782992,
    "end_cap_weight_raw": -11.433177578674487
  },
  "full_period_change": {
    "equal_weight_sd": -1.1020714285714235,
    "equal_weight_raw": -16.53107142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0491491402116357,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.28058333333333657,
    "equal_weight_raw": 4.208750000000049,
    "fixed_start_cap_weight_sd": 0.22928872639234663,
    "fixed_start_cap_weight_raw": 3.4393308958851994,
    "end_cap_weight_sd": 0.19016911380265325,
    "end_cap_weight_raw": 2.8525367070397976
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6782142857142822,
      "change_raw": -10.173214285714232,
      "decay_adjusted_gain_sd": 0.27416666666667006
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7479365079365046,
      "change_raw": -11.219047619047569,
      "decay_adjusted_gain_sd": 0.20444444444444768
    },
    "small": {
      "count": 18,
      "change_sd": -0.632658730158727,
      "change_raw": -9.489880952380904,
      "decay_adjusted_gain_sd": 0.3197222222222254
    },
    "large_minus_small_sd": -0.04555555555555524,
    "large_minus_small_raw": -0.6833333333333286
  },
  "inflation": {
    "initial_mean_sd": 0.0,
    "final_mean_sd": 0.0,
    "mean_sd": 0.0,
    "mean_absolute_raw_gap": 0.0,
    "final_absolute_raw_gap": 0.0,
    "mean_range_fraction": 0.0
  },
  "impact": {
    "initial_share": 0.4533333333333333,
    "final_share": 0.5066666666666667,
    "initial_wealth_share": 0.45756523209630184,
    "final_wealth_share": 0.578539422695421
  },
  "pricing_slope": {
    "mean": -0.002745689346113809,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.0013141365080132157,
    "real_improvement_cost": 0.0013141365080132157,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0013141365080132157,
    "resource_cost_fraction_initial_cap": 4.380455026710719e-05,
    "private_net_outflow_fraction_initial_cap": 4.380455026710719e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 2.5179771290934296e-05,
    "unapplied_final_day_resource_cost": 9.290649413455393e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 6405.346741889196,
    "beneficial_raw_gain_per_resource_cost": 96080.20112833793,
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
    "accrued_cost": 3.0504665895534986,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.07427611336302209,
    "accrued_cost_fraction_initial_cap": 0.10168221965178328,
    "mean_contract_rate": 0.042968823176806455,
    "maximum_ledger_error": 7.665648172651418e-20
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
    "maximum_relative_cash_error": 1.5959810433987464e-15,
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
      "minimum": -0.16299982266006738,
      "maximum": -0.03806897054795034,
      "mean": -0.09510720133734053,
      "median": -0.09188889701463157,
      "quantile_05": -0.15059684298819656,
      "quantile_95": -0.051064208889301924
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
      "minimum": 0.5933215466228695,
      "maximum": 0.8031331208520456,
      "mean": 0.7283009946042839,
      "median": 0.7359501466170059,
      "quantile_05": 0.655067511629808,
      "quantile_95": 0.7739644096627611
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
        "daily_volatility": 0.019896901217003354,
        "excess_kurtosis": 5.012453613339076,
        "return_acf_1": -0.105617481395459,
        "abs_return_acf_1": 0.30752561036112286,
        "abs_return_acf_5": 0.32798837277940796,
        "abs_return_acf_20": 0.30665731651087835,
        "quantile_01": -0.06613394938153913,
        "quantile_99": 0.06011298260951,
        "hill_tail_index": 5.132313321097355
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01991251612659804,
        "excess_kurtosis": 5.9267814515048585,
        "return_acf_1": -0.16299982266006738,
        "abs_return_acf_1": 0.4189083169460287,
        "abs_return_acf_5": 0.3849689540362009,
        "abs_return_acf_20": 0.205008807955022,
        "quantile_01": -0.06623043485109349,
        "quantile_99": 0.05380713352977753,
        "hill_tail_index": 4.478754441677286
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02071794203114646,
        "excess_kurtosis": 9.57497675963441,
        "return_acf_1": -0.14737774126832465,
        "abs_return_acf_1": 0.4298261818482215,
        "abs_return_acf_5": 0.36263140679119393,
        "abs_return_acf_20": 0.20878876746823105,
        "quantile_01": -0.07296919080514115,
        "quantile_99": 0.050919066723868076,
        "hill_tail_index": 2.658058275881871
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019535464750521907,
        "excess_kurtosis": 8.17701474558702,
        "return_acf_1": -0.09648800891451464,
        "abs_return_acf_1": 0.3141334527073959,
        "abs_return_acf_5": 0.32827710783064207,
        "abs_return_acf_20": 0.2326951806544934,
        "quantile_01": -0.06150045156747575,
        "quantile_99": 0.04931782200605308,
        "hill_tail_index": 3.088121987280044
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020799089941898982,
        "excess_kurtosis": 4.762501364955352,
        "return_acf_1": -0.09191400464585887,
        "abs_return_acf_1": 0.4548962813816137,
        "abs_return_acf_5": 0.41851689999329644,
        "abs_return_acf_20": 0.33031505281228973,
        "quantile_01": -0.06787645491410661,
        "quantile_99": 0.0544173607262266,
        "hill_tail_index": 4.943144373080243
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01955475282602602,
        "excess_kurtosis": 4.509651143024692,
        "return_acf_1": -0.11203123877129327,
        "abs_return_acf_1": 0.30140244452039877,
        "abs_return_acf_5": 0.3925008312202893,
        "abs_return_acf_20": 0.24842505692853545,
        "quantile_01": -0.06978039736364657,
        "quantile_99": 0.05497925481681029,
        "hill_tail_index": 4.17445428785943
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.02034281391859504,
        "excess_kurtosis": 5.485226844871686,
        "return_acf_1": -0.14164083812128145,
        "abs_return_acf_1": 0.3282002334078227,
        "abs_return_acf_5": 0.3861303206433095,
        "abs_return_acf_20": 0.2950317428437589,
        "quantile_01": -0.06809273539158903,
        "quantile_99": 0.060286300857447565,
        "hill_tail_index": 4.577432143382521
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019669263514710645,
        "excess_kurtosis": 7.461336206483757,
        "return_acf_1": -0.04754712937503597,
        "abs_return_acf_1": 0.3459384983014287,
        "abs_return_acf_5": 0.38803323990540595,
        "abs_return_acf_20": 0.21041244133829698,
        "quantile_01": -0.0665949391238926,
        "quantile_99": 0.057309893481938115,
        "hill_tail_index": 2.8858344677701004
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01796840399701991,
        "excess_kurtosis": 4.772638646604603,
        "return_acf_1": -0.06346529654144051,
        "abs_return_acf_1": 0.2844800340659939,
        "abs_return_acf_5": 0.2929576162189271,
        "abs_return_acf_20": 0.24317830263915566,
        "quantile_01": -0.056420477417933323,
        "quantile_99": 0.04535573790591777,
        "hill_tail_index": 3.8594102804211383
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020386709161140912,
        "excess_kurtosis": 6.76759073430361,
        "return_acf_1": -0.09186378938340428,
        "abs_return_acf_1": 0.421443465377697,
        "abs_return_acf_5": 0.39293958512347293,
        "abs_return_acf_20": 0.25133294333495176,
        "quantile_01": -0.07055278928892292,
        "quantile_99": 0.058780464090534064,
        "hill_tail_index": 3.8208698311774167
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019400363500640467,
        "excess_kurtosis": 4.267456431539228,
        "return_acf_1": -0.13038708506293548,
        "abs_return_acf_1": 0.28317056882427366,
        "abs_return_acf_5": 0.42501874544727086,
        "abs_return_acf_20": 0.30295629535725305,
        "quantile_01": -0.059484121080723165,
        "quantile_99": 0.05789410618950911,
        "hill_tail_index": 5.318588372435381
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020439396165858402,
        "excess_kurtosis": 5.763770252298961,
        "return_acf_1": -0.12285694141317302,
        "abs_return_acf_1": 0.4113926823955328,
        "abs_return_acf_5": 0.3839343045615261,
        "abs_return_acf_20": 0.28562384178214567,
        "quantile_01": -0.06963868551889513,
        "quantile_99": 0.052940849273682394,
        "hill_tail_index": 3.4581423245179557
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02228380392280518,
        "excess_kurtosis": 9.274634287993376,
        "return_acf_1": -0.05536286162896026,
        "abs_return_acf_1": 0.4849129715599164,
        "abs_return_acf_5": 0.5084718354532364,
        "abs_return_acf_20": 0.3214268984326222,
        "quantile_01": -0.08439417558800937,
        "quantile_99": 0.0662983448534993,
        "hill_tail_index": 3.2590743632644523
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02001502959251305,
        "excess_kurtosis": 7.307652058470554,
        "return_acf_1": -0.08247616741295968,
        "abs_return_acf_1": 0.3778884134119636,
        "abs_return_acf_5": 0.32471798212550557,
        "abs_return_acf_20": 0.22370088737723834,
        "quantile_01": -0.061030877174749296,
        "quantile_99": 0.05127962846485642,
        "hill_tail_index": 3.7277640001373036
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020201933714062967,
        "excess_kurtosis": 8.249641735064907,
        "return_acf_1": -0.1327481402841517,
        "abs_return_acf_1": 0.32918950707999306,
        "abs_return_acf_5": 0.40897362569845197,
        "abs_return_acf_20": 0.26105255092261553,
        "quantile_01": -0.07034844420354291,
        "quantile_99": 0.051760492673532325,
        "hill_tail_index": 3.7176289965417757
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019180809389995154,
        "excess_kurtosis": 5.172380562296427,
        "return_acf_1": -0.06816459392110849,
        "abs_return_acf_1": 0.32586459762285047,
        "abs_return_acf_5": 0.3639252407491612,
        "abs_return_acf_20": 0.3244853570408069,
        "quantile_01": -0.06432718208599425,
        "quantile_99": 0.0481826890786228,
        "hill_tail_index": 3.3836456219675264
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02067530053740646,
        "excess_kurtosis": 7.1808726555097255,
        "return_acf_1": -0.07417571610854655,
        "abs_return_acf_1": 0.35899929300631944,
        "abs_return_acf_5": 0.36279736801214724,
        "abs_return_acf_20": 0.25102389519477686,
        "quantile_01": -0.0733380327668415,
        "quantile_99": 0.06064222770995216,
        "hill_tail_index": 3.72612677203968
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01913507174852386,
        "excess_kurtosis": 4.50287459518248,
        "return_acf_1": -0.061408732404009056,
        "abs_return_acf_1": 0.36344662639446584,
        "abs_return_acf_5": 0.33359044816546823,
        "abs_return_acf_20": 0.17334071170531132,
        "quantile_01": -0.06363458919407165,
        "quantile_99": 0.05050940468168481,
        "hill_tail_index": 4.237334534259514
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01874049817831904,
        "excess_kurtosis": 6.863246043368482,
        "return_acf_1": -0.08931268916852088,
        "abs_return_acf_1": 0.33404227637533773,
        "abs_return_acf_5": 0.3688852419706312,
        "abs_return_acf_20": 0.20954218378246425,
        "quantile_01": -0.055879224835476804,
        "quantile_99": 0.04994324308511079,
        "hill_tail_index": 3.3282962458342196
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02024487628312758,
        "excess_kurtosis": 5.65763452532345,
        "return_acf_1": -0.07973853612198499,
        "abs_return_acf_1": 0.311779194684751,
        "abs_return_acf_5": 0.42861861366381965,
        "abs_return_acf_20": 0.3545380260388031,
        "quantile_01": -0.0603062831716109,
        "quantile_99": 0.0605812249348922,
        "hill_tail_index": 3.967638644195025
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01898168775010498,
        "excess_kurtosis": 5.750187404167782,
        "return_acf_1": -0.07493867061154372,
        "abs_return_acf_1": 0.2967490807874874,
        "abs_return_acf_5": 0.3783019040895797,
        "abs_return_acf_20": 0.21522436011617427,
        "quantile_01": -0.05891353050693585,
        "quantile_99": 0.05206948990078151,
        "hill_tail_index": 3.2566690692817604
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02197828666596068,
        "excess_kurtosis": 12.31537874538381,
        "return_acf_1": -0.11750811145567394,
        "abs_return_acf_1": 0.4284261305596451,
        "abs_return_acf_5": 0.41264358078072216,
        "abs_return_acf_20": 0.21615692319910482,
        "quantile_01": -0.07279481041717306,
        "quantile_99": 0.0662677387439802,
        "hill_tail_index": 2.152497809072354
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02163964698453251,
        "excess_kurtosis": 9.347884976761922,
        "return_acf_1": -0.1532306534862736,
        "abs_return_acf_1": 0.4265858547879529,
        "abs_return_acf_5": 0.3992415825275626,
        "abs_return_acf_20": 0.3017522982337403,
        "quantile_01": -0.077995485449019,
        "quantile_99": 0.0639160998641519,
        "hill_tail_index": 3.5423084040886765
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02031950857521244,
        "excess_kurtosis": 4.057165221412036,
        "return_acf_1": -0.10670865370674329,
        "abs_return_acf_1": 0.34489464992738256,
        "abs_return_acf_5": 0.40390211097536577,
        "abs_return_acf_20": 0.29770849179443315,
        "quantile_01": -0.06353381470321391,
        "quantile_99": 0.05881874867171241,
        "hill_tail_index": 4.870270084409455
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019432579313295072,
        "excess_kurtosis": 5.328021302597104,
        "return_acf_1": -0.058599193660660624,
        "abs_return_acf_1": 0.3053874007986426,
        "abs_return_acf_5": 0.3987077858174676,
        "abs_return_acf_20": 0.32741967730535093,
        "quantile_01": -0.06459118311311807,
        "quantile_99": 0.05927449221832109,
        "hill_tail_index": 4.344923355260739
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.019175086348854304,
        "excess_kurtosis": 5.45306956720667,
        "return_acf_1": -0.11586496958488049,
        "abs_return_acf_1": 0.3405100484378642,
        "abs_return_acf_5": 0.3114132862608882,
        "abs_return_acf_20": 0.2044696891189593,
        "quantile_01": -0.06192035809524619,
        "quantile_99": 0.05279430941492179,
        "hill_tail_index": 3.2348555745437078
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021695185656863073,
        "excess_kurtosis": 6.942310684848271,
        "return_acf_1": -0.03806897054795034,
        "abs_return_acf_1": 0.4066024893635552,
        "abs_return_acf_5": 0.40937095420236685,
        "abs_return_acf_20": 0.3364175582663453,
        "quantile_01": -0.07318824346274705,
        "quantile_99": 0.05533135391551556,
        "hill_tail_index": 3.120461804517199
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018987097984257236,
        "excess_kurtosis": 4.396522908002982,
        "return_acf_1": -0.05798350310303752,
        "abs_return_acf_1": 0.3163115023397225,
        "abs_return_acf_5": 0.3371134166610049,
        "abs_return_acf_20": 0.21326880091121603,
        "quantile_01": -0.06126573526944769,
        "quantile_99": 0.050870995522949276,
        "hill_tail_index": 4.067871014522825
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020211041005440484,
        "excess_kurtosis": 6.16037183782489,
        "return_acf_1": -0.10127793019505188,
        "abs_return_acf_1": 0.440053790967927,
        "abs_return_acf_5": 0.40451938220264483,
        "abs_return_acf_20": 0.21974597517877817,
        "quantile_01": -0.06911892969563356,
        "quantile_99": 0.05397060410715502,
        "hill_tail_index": 3.240526288855699
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.019237969285149353,
        "excess_kurtosis": 5.60488715338823,
        "return_acf_1": -0.07145856916537048,
        "abs_return_acf_1": 0.32684503167754364,
        "abs_return_acf_5": 0.32158575994071054,
        "abs_return_acf_20": 0.2232357216432552,
        "quantile_01": -0.06256303279842568,
        "quantile_99": 0.054786448545105504,
        "hill_tail_index": 3.6617380784907496
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

Firm policy: npv_discrete
Training: False
Coverage status: not_applicable
Unseen state share: None
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
