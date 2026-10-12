# Disclosure-market run

Purpose: generality_smoke
Domain: wba_social_2023
Seed: 24001
Run ID: `b19c8fbc735758f05481669c552aa6e966da08e1513950382b0b75967bbd3235`
Result fingerprint: `448e59fc214ded731e8c46e489fd628324d09eefbfa215a7b1e15a0fe0e7035f`

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
    "equal_weight_sd": -0.6295407939841806,
    "equal_weight_raw": -2.429562297274871,
    "fixed_start_cap_weight_sd": -0.613903593407041,
    "fixed_start_cap_weight_raw": -2.369214257369934,
    "end_cap_weight_sd": -0.6437279182002762,
    "end_cap_weight_raw": -2.4843141138871667
  },
  "full_period_change": {
    "equal_weight_sd": -1.0218300595941383,
    "equal_weight_raw": -3.9435090001084765
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9735128592536192,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.03178099597116486,
    "equal_weight_raw": 0.12265116148029474,
    "fixed_start_cap_weight_sd": 0.020499214637805345,
    "fixed_start_cap_weight_raw": 0.07911182163837423,
    "end_cap_weight_sd": 0.021324791246959414,
    "end_cap_weight_raw": 0.08229793733139978
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.4263239677549449,
      "change_raw": -1.6452955048820386,
      "decay_adjusted_gain_sd": 0.011936907359448598
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6749387898828194,
      "change_raw": -2.604765016878048,
      "decay_adjusted_gain_sd": 0.04424129442707371
    },
    "small": {
      "count": 18,
      "change_sd": -0.6407112670730675,
      "change_raw": -2.472672069538755,
      "decay_adjusted_gain_sd": 0.02885819484516315
    },
    "large_minus_small_sd": 0.21438729931812256,
    "large_minus_small_raw": 0.8273765646567166
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
    "initial_share": 0.25333333333333335,
    "final_share": 0.41333333333333333,
    "initial_wealth_share": 0.20584635255309666,
    "final_wealth_share": 0.38853472318464577
  },
  "pricing_slope": {
    "mean": -0.0015831070458745054,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.00033400857053971704,
    "real_improvement_cost": 0.00033400857053971704,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.00033400857053971704,
    "resource_cost_fraction_initial_cap": 1.113361901799057e-05,
    "private_net_outflow_fraction_initial_cap": 1.113361901799057e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 5.989416431934647e-06,
    "unapplied_final_day_resource_cost": 2.940661588606071e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 2854.5072289442146,
    "beneficial_raw_gain_per_resource_cost": 11016.288709188402,
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
    "accrued_cost": 2.942278150835551,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": 0.0339123253549253,
    "accrued_cost_fraction_initial_cap": 0.09807593836118506,
    "mean_contract_rate": 0.04090417660284325,
    "maximum_ledger_error": 5.759824041329242e-20
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
    "maximum_relative_cash_error": 1.9366454255715105e-15,
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
      "minimum": -0.16291097525134174,
      "maximum": -0.02304967229099351,
      "mean": -0.10203275755611034,
      "median": -0.1060179907327285,
      "quantile_05": -0.16120847875253994,
      "quantile_95": -0.028887796054669616
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
      "minimum": 0.24456233185647688,
      "maximum": 0.7804567398275815,
      "mean": 0.4811097521988646,
      "median": 0.44723534926161274,
      "quantile_05": 0.28785156527391603,
      "quantile_95": 0.7403220172091697
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
        "daily_volatility": 0.02233553783809638,
        "excess_kurtosis": 9.083548182494297,
        "return_acf_1": -0.13382095686447457,
        "abs_return_acf_1": 0.4139287022587736,
        "abs_return_acf_5": 0.30214104186273266,
        "abs_return_acf_20": 0.3513914829307534,
        "quantile_01": -0.06679679317187391,
        "quantile_99": 0.06044937755042811,
        "hill_tail_index": 3.309892583711291
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02001215534046477,
        "excess_kurtosis": 10.3494955405008,
        "return_acf_1": -0.16010143378929823,
        "abs_return_acf_1": 0.3729405581549735,
        "abs_return_acf_5": 0.38572729219085566,
        "abs_return_acf_20": 0.29579206612011943,
        "quantile_01": -0.06619845869752837,
        "quantile_99": 0.060624335683670434,
        "hill_tail_index": 2.9182504185495093
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02030587649879359,
        "excess_kurtosis": 11.634094765589355,
        "return_acf_1": -0.03462301789899601,
        "abs_return_acf_1": 0.33952970778606617,
        "abs_return_acf_5": 0.32483081563774563,
        "abs_return_acf_20": 0.33204674978155496,
        "quantile_01": -0.06835076582024215,
        "quantile_99": 0.05735159950205933,
        "hill_tail_index": 2.6835582066577977
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018874943608046795,
        "excess_kurtosis": 7.53929640143712,
        "return_acf_1": -0.1343105116142887,
        "abs_return_acf_1": 0.4095648114697894,
        "abs_return_acf_5": 0.37741196583036635,
        "abs_return_acf_20": 0.23728360376848953,
        "quantile_01": -0.06583450464065596,
        "quantile_99": 0.04921366010290999,
        "hill_tail_index": 3.1536263784399248
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02212131116130919,
        "excess_kurtosis": 7.458134270333435,
        "return_acf_1": -0.117128574064331,
        "abs_return_acf_1": 0.3889391797744006,
        "abs_return_acf_5": 0.3912057790685585,
        "abs_return_acf_20": 0.323315613597981,
        "quantile_01": -0.08265412229984342,
        "quantile_99": 0.06374290826506972,
        "hill_tail_index": 3.700368318489002
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.0221161958050173,
        "excess_kurtosis": 12.149224058081767,
        "return_acf_1": -0.12910021392078477,
        "abs_return_acf_1": 0.44941241380922137,
        "abs_return_acf_5": 0.41692247687588335,
        "abs_return_acf_20": 0.3535018885866592,
        "quantile_01": -0.06936050038446775,
        "quantile_99": 0.06456388524566405,
        "hill_tail_index": 2.570530427736626
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020268256925645094,
        "excess_kurtosis": 6.0744927263598765,
        "return_acf_1": -0.10945627869018532,
        "abs_return_acf_1": 0.3476554750246799,
        "abs_return_acf_5": 0.3665279066183552,
        "abs_return_acf_20": 0.3197037908056307,
        "quantile_01": -0.06113036005658531,
        "quantile_99": 0.06110912625522896,
        "hill_tail_index": 4.0357878916398535
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021505025289351175,
        "excess_kurtosis": 11.159990052745895,
        "return_acf_1": -0.09220623391227223,
        "abs_return_acf_1": 0.39130989017978957,
        "abs_return_acf_5": 0.3567928334605765,
        "abs_return_acf_20": 0.307196257520121,
        "quantile_01": -0.08014087196050892,
        "quantile_99": 0.06563352483114705,
        "hill_tail_index": 3.2502429368474886
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.02084140746454949,
        "excess_kurtosis": 13.184470876696931,
        "return_acf_1": -0.14043637195673558,
        "abs_return_acf_1": 0.49759986567913495,
        "abs_return_acf_5": 0.34623183497126575,
        "abs_return_acf_20": 0.21457434169592401,
        "quantile_01": -0.0772868691954294,
        "quantile_99": 0.06157915392141148,
        "hill_tail_index": 2.6420186020567127
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021367390607243627,
        "excess_kurtosis": 7.966916314599606,
        "return_acf_1": -0.06353853920623305,
        "abs_return_acf_1": 0.396812770581904,
        "abs_return_acf_5": 0.3295897175616498,
        "abs_return_acf_20": 0.3560337521622495,
        "quantile_01": -0.07239755937263682,
        "quantile_99": 0.05146611869643355,
        "hill_tail_index": 2.5184144262300374
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017694853358973455,
        "excess_kurtosis": 5.914829339441882,
        "return_acf_1": -0.07478614024300202,
        "abs_return_acf_1": 0.30825825548188607,
        "abs_return_acf_5": 0.29117036645679073,
        "abs_return_acf_20": 0.22256345764130106,
        "quantile_01": -0.05913764389067049,
        "quantile_99": 0.04982208767510601,
        "hill_tail_index": 3.4157236597092173
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020066489466278526,
        "excess_kurtosis": 9.209617810359155,
        "return_acf_1": -0.15030926482597612,
        "abs_return_acf_1": 0.47941746148376246,
        "abs_return_acf_5": 0.3792205881761056,
        "abs_return_acf_20": 0.28467903523567323,
        "quantile_01": -0.06925291450513532,
        "quantile_99": 0.05384828700282161,
        "hill_tail_index": 2.789755285864392
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01809641634990269,
        "excess_kurtosis": 11.592255160827463,
        "return_acf_1": -0.1016749128071648,
        "abs_return_acf_1": 0.37056005635169004,
        "abs_return_acf_5": 0.2989648243042819,
        "abs_return_acf_20": 0.17984179980702555,
        "quantile_01": -0.0540656251034679,
        "quantile_99": 0.04741836389390309,
        "hill_tail_index": 2.6596560039460333
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016683331877082087,
        "excess_kurtosis": 9.311338599409103,
        "return_acf_1": -0.13507101495399948,
        "abs_return_acf_1": 0.35814427223133816,
        "abs_return_acf_5": 0.30748549530463476,
        "abs_return_acf_20": 0.2295155212749411,
        "quantile_01": -0.05490537695009985,
        "quantile_99": 0.04120830755401332,
        "hill_tail_index": 2.2955677873521623
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.023089091553285927,
        "excess_kurtosis": 17.58091937568809,
        "return_acf_1": -0.10099969367733153,
        "abs_return_acf_1": 0.5041835504329097,
        "abs_return_acf_5": 0.394580288370157,
        "abs_return_acf_20": 0.27271628771909107,
        "quantile_01": -0.0805117578232462,
        "quantile_99": 0.051980728648002766,
        "hill_tail_index": 1.8809893097071844
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020828076159068617,
        "excess_kurtosis": 8.546966035785344,
        "return_acf_1": -0.0546527720218355,
        "abs_return_acf_1": 0.32859956685856845,
        "abs_return_acf_5": 0.27493855956243973,
        "abs_return_acf_20": 0.31354465960249267,
        "quantile_01": -0.06952648138386772,
        "quantile_99": 0.05495888907183857,
        "hill_tail_index": 2.96653767839933
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018703332233803882,
        "excess_kurtosis": 7.229822596102132,
        "return_acf_1": -0.16291097525134174,
        "abs_return_acf_1": 0.31372394718707125,
        "abs_return_acf_5": 0.25089646166106433,
        "abs_return_acf_20": 0.17514312510894725,
        "quantile_01": -0.05518780607034935,
        "quantile_99": 0.04863854676911385,
        "hill_tail_index": 3.29694066956637
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.024070454212501584,
        "excess_kurtosis": 11.796665111407012,
        "return_acf_1": -0.02304967229099351,
        "abs_return_acf_1": 0.3845324867757256,
        "abs_return_acf_5": 0.3779833390682746,
        "abs_return_acf_20": 0.33612709396961266,
        "quantile_01": -0.08890592917483824,
        "quantile_99": 0.06388046153267658,
        "hill_tail_index": 2.6883952922276118
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018076381551472807,
        "excess_kurtosis": 9.230116366420424,
        "return_acf_1": -0.10291172584351171,
        "abs_return_acf_1": 0.39072778022816174,
        "abs_return_acf_5": 0.40282756530691116,
        "abs_return_acf_20": 0.36020802805917124,
        "quantile_01": -0.059607512181612705,
        "quantile_99": 0.04655889747809783,
        "hill_tail_index": 2.3370761022764617
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019824389162722965,
        "excess_kurtosis": 3.212247127585411,
        "return_acf_1": -0.10679917011695654,
        "abs_return_acf_1": 0.2730242625544997,
        "abs_return_acf_5": 0.272748054219728,
        "abs_return_acf_20": 0.2611141350380243,
        "quantile_01": -0.056208447262971604,
        "quantile_99": 0.058921428795519884,
        "hill_tail_index": 4.419670040064302
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019941935887868096,
        "excess_kurtosis": 6.5870336311438376,
        "return_acf_1": -0.12898925464965727,
        "abs_return_acf_1": 0.3494526276721374,
        "abs_return_acf_5": 0.30247894216324406,
        "abs_return_acf_20": 0.30197911468496225,
        "quantile_01": -0.0675023995720875,
        "quantile_99": 0.05719320064785146,
        "hill_tail_index": 3.334181496844676
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021576860227471278,
        "excess_kurtosis": 17.33709460274251,
        "return_acf_1": -0.02419534181840251,
        "abs_return_acf_1": 0.38512698646028476,
        "abs_return_acf_5": 0.32526014061959346,
        "abs_return_acf_20": 0.31730867973228893,
        "quantile_01": -0.0742388451222176,
        "quantile_99": 0.05134326588235392,
        "hill_tail_index": 2.6073067499741946
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017749905039822895,
        "excess_kurtosis": 4.1466297747430625,
        "return_acf_1": -0.06287701317406964,
        "abs_return_acf_1": 0.2809274176579094,
        "abs_return_acf_5": 0.19790676139389182,
        "abs_return_acf_20": 0.19055938290209778,
        "quantile_01": -0.05359952925608878,
        "quantile_99": 0.0525797138671913,
        "hill_tail_index": 3.9660524692696235
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01804093507228301,
        "excess_kurtosis": 16.117396561380865,
        "return_acf_1": -0.10991171870101296,
        "abs_return_acf_1": 0.339050199525716,
        "abs_return_acf_5": 0.27687306564178693,
        "abs_return_acf_20": 0.2216959288991479,
        "quantile_01": -0.04856927161361684,
        "quantile_99": 0.04680079987813589,
        "hill_tail_index": 2.553146555648429
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021808760710712412,
        "excess_kurtosis": 9.56930290614966,
        "return_acf_1": -0.09049210219060706,
        "abs_return_acf_1": 0.4091641971524764,
        "abs_return_acf_5": 0.3642324471267118,
        "abs_return_acf_20": 0.294241505326828,
        "quantile_01": -0.08561991906084866,
        "quantile_99": 0.0667631360499731,
        "hill_tail_index": 3.365919026327559
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01842272654385458,
        "excess_kurtosis": 6.94449520209956,
        "return_acf_1": -0.10658563181801324,
        "abs_return_acf_1": 0.3539217785491604,
        "abs_return_acf_5": 0.26588939183685467,
        "abs_return_acf_20": 0.2644103075330429,
        "quantile_01": -0.06517313173599613,
        "quantile_99": 0.04746513725269439,
        "hill_tail_index": 2.7243089898050865
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020356332866960255,
        "excess_kurtosis": 10.354272141840083,
        "return_acf_1": -0.16211424281337405,
        "abs_return_acf_1": 0.4724753273787428,
        "abs_return_acf_5": 0.3638420052615636,
        "abs_return_acf_20": 0.24769190194234333,
        "quantile_01": -0.06328341471879456,
        "quantile_99": 0.05686262696330991,
        "hill_tail_index": 2.7389043251640497
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017826886100566014,
        "excess_kurtosis": 4.478689686683806,
        "return_acf_1": -0.10545034964744376,
        "abs_return_acf_1": 0.2807009566301743,
        "abs_return_acf_5": 0.23874696601642198,
        "abs_return_acf_20": 0.19241243333336905,
        "quantile_01": -0.05429005195387129,
        "quantile_99": 0.047029665736900345,
        "hill_tail_index": 3.5359695162524307
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01662252269362793,
        "excess_kurtosis": 3.237776831213597,
        "return_acf_1": -0.03894744916959494,
        "abs_return_acf_1": 0.2686414318906721,
        "abs_return_acf_5": 0.19459049891911004,
        "abs_return_acf_20": 0.16968364908997946,
        "quantile_01": -0.045232893617791724,
        "quantile_99": 0.046630277241841156,
        "hill_tail_index": 4.2197397592988795
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020638367875155054,
        "excess_kurtosis": 5.042913555250012,
        "return_acf_1": -0.10353214875142196,
        "abs_return_acf_1": 0.4207575186221813,
        "abs_return_acf_5": 0.36546873970137495,
        "abs_return_acf_20": 0.3116301802985122,
        "quantile_01": -0.06439768523476787,
        "quantile_99": 0.0637029239667971,
        "hill_tail_index": 3.9488340435238656
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
