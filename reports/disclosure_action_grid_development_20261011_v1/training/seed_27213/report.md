# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27213
Run ID: `11609dc8425ca903d5c6fd66276d1aa2ef48fbec081561fc5dc5304e807bd8f9`
Result fingerprint: `0aa5c45e3f5918d5b65a32284b095f26f0e1b99edd10466a8bb8993b996147b3`

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
    "equal_weight_sd": -0.7855476190476158,
    "equal_weight_raw": -11.783214285714239,
    "fixed_start_cap_weight_sd": -0.7246778045950698,
    "fixed_start_cap_weight_raw": -10.870167068926044,
    "end_cap_weight_sd": -0.7223946031466725,
    "end_cap_weight_raw": -10.835919047200084
  },
  "full_period_change": {
    "equal_weight_sd": -1.2089047619047575,
    "equal_weight_raw": -18.13357142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1194976851851808,
    "inflation_mean_sd": 1.0260608465608463
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.16683333333333653,
    "equal_weight_raw": 2.502500000000048,
    "fixed_start_cap_weight_sd": 0.22770314778588252,
    "fixed_start_cap_weight_raw": 3.415547216788238,
    "end_cap_weight_sd": 0.22998634923427988,
    "end_cap_weight_raw": 3.449795238514198
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6915476190476157,
      "change_raw": -10.373214285714237,
      "decay_adjusted_gain_sd": 0.2608333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8165476190476157,
      "change_raw": -12.248214285714237,
      "decay_adjusted_gain_sd": 0.13583333333333653
    },
    "small": {
      "count": 18,
      "change_sd": -0.7857142857142825,
      "change_raw": -11.785714285714237,
      "decay_adjusted_gain_sd": 0.16666666666666985
    },
    "large_minus_small_sd": 0.09416666666666673,
    "large_minus_small_raw": 1.412500000000001
  },
  "inflation": {
    "initial_mean_sd": 0.4434166666666667,
    "final_mean_sd": 1.0856666666666668,
    "mean_sd": 0.8611593116847073,
    "mean_absolute_raw_gap": 12.91738967527061,
    "final_absolute_raw_gap": 16.285,
    "mean_range_fraction": 0.1291738967527061
  },
  "impact": {
    "initial_share": 0.2866666666666667,
    "final_share": 0.3466666666666667,
    "initial_wealth_share": 0.33580820856886145,
    "final_wealth_share": 0.33021199750096075
  },
  "pricing_slope": {
    "mean": -0.0022938392567481937,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.027199638670031417,
    "real_improvement_cost": 0.015210408527936717,
    "washing_cost": 0.011989230142094699,
    "fine_transfer": 0.02750564401492437,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05470528268495579,
    "resource_cost_fraction_initial_cap": 0.0009066546223343804,
    "private_net_outflow_fraction_initial_cap": 0.0018235094228318594,
    "fine_transfer_fraction_initial_cap": 0.0009168548004974789,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.003331557491830357,
    "unapplied_final_day_resource_cost": 0.00032712455213527476
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 184.00979736229397,
    "beneficial_raw_gain_per_resource_cost": 2760.1469604344093,
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
    "accrued_cost": 3.053160661169491,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.07697018497901406,
    "accrued_cost_fraction_initial_cap": 0.10177202203898301,
    "mean_contract_rate": 0.041148278306468944,
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
    "maximum_relative_cash_error": 1.2316178696104566e-15,
    "maximum_absolute_share_error": 1.4432899320127035e-15,
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
      "minimum": -0.21147399757968108,
      "maximum": -0.07374086653211846,
      "mean": -0.14179007388737394,
      "median": -0.14836600345585976,
      "quantile_05": -0.19235939762067675,
      "quantile_95": -0.07913855184590832
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
      "minimum": 0.26771356545751923,
      "maximum": 0.7713798809745857,
      "mean": 0.4640558208486385,
      "median": 0.4240534423383868,
      "quantile_05": 0.30634661175067834,
      "quantile_95": 0.6870944691031186
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
        "daily_volatility": 0.0193966652424836,
        "excess_kurtosis": 12.084998973069766,
        "return_acf_1": -0.21147399757968108,
        "abs_return_acf_1": 0.39201485983408607,
        "abs_return_acf_5": 0.3872078558571142,
        "abs_return_acf_20": 0.3223136000689287,
        "quantile_01": -0.07063989300872714,
        "quantile_99": 0.054622156090769355,
        "hill_tail_index": 2.329633140700434
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01832928015518932,
        "excess_kurtosis": 4.858621107790108,
        "return_acf_1": -0.14873204925329253,
        "abs_return_acf_1": 0.35979304273465884,
        "abs_return_acf_5": 0.3271302461837367,
        "abs_return_acf_20": 0.24537747959111766,
        "quantile_01": -0.05753190662631914,
        "quantile_99": 0.04808444021127809,
        "hill_tail_index": 3.3242182535807476
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01899413996876863,
        "excess_kurtosis": 8.454564089543792,
        "return_acf_1": -0.14799995765842697,
        "abs_return_acf_1": 0.3374446106546753,
        "abs_return_acf_5": 0.3813028170166672,
        "abs_return_acf_20": 0.2632382975541337,
        "quantile_01": -0.055825780493998896,
        "quantile_99": 0.057010330202042374,
        "hill_tail_index": 3.127073340175025
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016832281100271396,
        "excess_kurtosis": 1.8679682459497071,
        "return_acf_1": -0.1342188784869864,
        "abs_return_acf_1": 0.23071313567841983,
        "abs_return_acf_5": 0.20766987333610762,
        "abs_return_acf_20": 0.11229407363596904,
        "quantile_01": -0.04571365423730822,
        "quantile_99": 0.04245429289011003,
        "hill_tail_index": 4.835228296724655
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01952221199131293,
        "excess_kurtosis": 17.668055404817718,
        "return_acf_1": -0.18905445579333005,
        "abs_return_acf_1": 0.48526066624197167,
        "abs_return_acf_5": 0.4363000439900814,
        "abs_return_acf_20": 0.26638799845366723,
        "quantile_01": -0.05899065705773942,
        "quantile_99": 0.05820263047469985,
        "hill_tail_index": 2.451381279559864
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017843738522001433,
        "excess_kurtosis": 7.3412320511021,
        "return_acf_1": -0.1308046047470418,
        "abs_return_acf_1": 0.21584370529149888,
        "abs_return_acf_5": 0.2966020855557999,
        "abs_return_acf_20": 0.21471837992542525,
        "quantile_01": -0.04904834011904503,
        "quantile_99": 0.04083932594882329,
        "hill_tail_index": 3.0606911121777207
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01781314994864448,
        "excess_kurtosis": 11.468313671824001,
        "return_acf_1": -0.10638991725373773,
        "abs_return_acf_1": 0.2709175950330524,
        "abs_return_acf_5": 0.3204573982377982,
        "abs_return_acf_20": 0.2896048712095715,
        "quantile_01": -0.052144654466360595,
        "quantile_99": 0.044811669481255666,
        "hill_tail_index": 2.1043830409101894
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.020705988268028136,
        "excess_kurtosis": 8.343523173124767,
        "return_acf_1": -0.1770482268602876,
        "abs_return_acf_1": 0.4850514915734386,
        "abs_return_acf_5": 0.4833763920209501,
        "abs_return_acf_20": 0.3336461529785108,
        "quantile_01": -0.07016234005875399,
        "quantile_99": 0.06207117297145029,
        "hill_tail_index": 3.8211440497101843
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017099053844510798,
        "excess_kurtosis": 7.718558830229684,
        "return_acf_1": -0.10546581003461529,
        "abs_return_acf_1": 0.3602864531787045,
        "abs_return_acf_5": 0.3639180517832204,
        "abs_return_acf_20": 0.23001845906641033,
        "quantile_01": -0.05054765813013288,
        "quantile_99": 0.04829955225922436,
        "hill_tail_index": 3.194129630731571
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.016308901474117767,
        "excess_kurtosis": 1.3552851594846897,
        "return_acf_1": -0.08045041613177675,
        "abs_return_acf_1": 0.23956398596249756,
        "abs_return_acf_5": 0.19248466094386688,
        "abs_return_acf_20": 0.1659602965813073,
        "quantile_01": -0.0426821253354246,
        "quantile_99": 0.04239062596254595,
        "hill_tail_index": 4.963826339670438
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017466730967334854,
        "excess_kurtosis": 8.12668845936769,
        "return_acf_1": -0.10902727392886621,
        "abs_return_acf_1": 0.35871490754185176,
        "abs_return_acf_5": 0.39177845522501453,
        "abs_return_acf_20": 0.2972857191662642,
        "quantile_01": -0.05742977760375255,
        "quantile_99": 0.049794336867503015,
        "hill_tail_index": 2.9056313171236003
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01790126148703987,
        "excess_kurtosis": 5.1580897489449455,
        "return_acf_1": -0.12702700219861363,
        "abs_return_acf_1": 0.3705168072088205,
        "abs_return_acf_5": 0.3574340513558899,
        "abs_return_acf_20": 0.2822122604642396,
        "quantile_01": -0.056929020066745585,
        "quantile_99": 0.05177147002670871,
        "hill_tail_index": 3.457140994063865
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.016752850052490092,
        "excess_kurtosis": 4.189155178174962,
        "return_acf_1": -0.176355318486292,
        "abs_return_acf_1": 0.3388548634016496,
        "abs_return_acf_5": 0.3191844444965435,
        "abs_return_acf_20": 0.3162467370259008,
        "quantile_01": -0.05305437274272397,
        "quantile_99": 0.04487216828856407,
        "hill_tail_index": 3.295704124939104
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016686478337271837,
        "excess_kurtosis": 7.359317542245497,
        "return_acf_1": -0.07374086653211846,
        "abs_return_acf_1": 0.2239579577946102,
        "abs_return_acf_5": 0.34162767620445744,
        "abs_return_acf_20": 0.15352949123161796,
        "quantile_01": -0.044194924365097345,
        "quantile_99": 0.04439637928012353,
        "hill_tail_index": 3.35594036212525
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01716009638852214,
        "excess_kurtosis": 3.463743775026124,
        "return_acf_1": -0.11554800214953863,
        "abs_return_acf_1": 0.3219257572473923,
        "abs_return_acf_5": 0.333288498685633,
        "abs_return_acf_20": 0.2012391846273751,
        "quantile_01": -0.05495905163585526,
        "quantile_99": 0.04614955833083066,
        "hill_tail_index": 4.5988287810684705
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019818575871945052,
        "excess_kurtosis": 10.902761579273978,
        "return_acf_1": -0.1950634409339604,
        "abs_return_acf_1": 0.5221394488565994,
        "abs_return_acf_5": 0.47557123540366547,
        "abs_return_acf_20": 0.3271236189098178,
        "quantile_01": -0.06812304862331475,
        "quantile_99": 0.05707554397295308,
        "hill_tail_index": 2.3753344040135063
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01873339777961375,
        "excess_kurtosis": 4.4524863537466155,
        "return_acf_1": -0.17797178687173895,
        "abs_return_acf_1": 0.3758740729836477,
        "abs_return_acf_5": 0.3691134556004701,
        "abs_return_acf_20": 0.30096393760762374,
        "quantile_01": -0.0561609967141042,
        "quantile_99": 0.0557215265515151,
        "hill_tail_index": 3.8009085681679595
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020303074557881554,
        "excess_kurtosis": 8.520486057033525,
        "return_acf_1": -0.18002185279273153,
        "abs_return_acf_1": 0.39704202060755256,
        "abs_return_acf_5": 0.4052957308721796,
        "abs_return_acf_20": 0.3050830393950904,
        "quantile_01": -0.06660543780821573,
        "quantile_99": 0.05671900197708843,
        "hill_tail_index": 2.748094693195114
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018043333401965716,
        "excess_kurtosis": 5.175845792645228,
        "return_acf_1": -0.1491878379879218,
        "abs_return_acf_1": 0.35457516750626444,
        "abs_return_acf_5": 0.3319072083621971,
        "abs_return_acf_20": 0.27478078825326485,
        "quantile_01": -0.05854226722207102,
        "quantile_99": 0.05187526322038837,
        "hill_tail_index": 3.788866709287061
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.016301799536158398,
        "excess_kurtosis": 4.118920845523823,
        "return_acf_1": -0.15067150664774323,
        "abs_return_acf_1": 0.3017495043848294,
        "abs_return_acf_5": 0.18757529672237777,
        "abs_return_acf_20": 0.18895961088308527,
        "quantile_01": -0.05301953924668415,
        "quantile_99": 0.045400648611921064,
        "hill_tail_index": 4.1409845948658255
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018350451145616443,
        "excess_kurtosis": 6.1302555211786345,
        "return_acf_1": -0.07806520833928866,
        "abs_return_acf_1": 0.2722228219350814,
        "abs_return_acf_5": 0.3356442059747927,
        "abs_return_acf_20": 0.22158888261100568,
        "quantile_01": -0.05798325099040551,
        "quantile_99": 0.05346126308854525,
        "hill_tail_index": 3.2478542378283732
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01811829743468176,
        "excess_kurtosis": 6.080003252738512,
        "return_acf_1": -0.11378109138631423,
        "abs_return_acf_1": 0.36612243477310025,
        "abs_return_acf_5": 0.30629314799495533,
        "abs_return_acf_20": 0.26382181210722666,
        "quantile_01": -0.05941482835942425,
        "quantile_99": 0.0551420725584019,
        "hill_tail_index": 3.4503541734393712
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017328550761365923,
        "excess_kurtosis": 12.859106767525113,
        "return_acf_1": -0.11935430917652537,
        "abs_return_acf_1": 0.24867711508486406,
        "abs_return_acf_5": 0.3499101809067828,
        "abs_return_acf_20": 0.17585835135313888,
        "quantile_01": -0.049216806451430214,
        "quantile_99": 0.03959831442852868,
        "hill_tail_index": 2.3923522317013353
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017233030253396658,
        "excess_kurtosis": 8.982833608983626,
        "return_acf_1": -0.11163834880174169,
        "abs_return_acf_1": 0.38606052868197505,
        "abs_return_acf_5": 0.4282405896104424,
        "abs_return_acf_20": 0.30989156460843786,
        "quantile_01": -0.0473267657301977,
        "quantile_99": 0.048355444293109485,
        "hill_tail_index": 2.473699539390101
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01959230038574441,
        "excess_kurtosis": 7.754912530627285,
        "return_acf_1": -0.18195084054743793,
        "abs_return_acf_1": 0.4209578732106654,
        "abs_return_acf_5": 0.43788722493794263,
        "abs_return_acf_20": 0.3766932541913385,
        "quantile_01": -0.05836109019759562,
        "quantile_99": 0.05785561488758181,
        "hill_tail_index": 2.7880615502932464
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018107075835253426,
        "excess_kurtosis": 36.75030393161041,
        "return_acf_1": -0.08846360663490131,
        "abs_return_acf_1": 0.3306522559689593,
        "abs_return_acf_5": 0.27594945955029015,
        "abs_return_acf_20": 0.21744797870431945,
        "quantile_01": -0.047041077082335514,
        "quantile_99": 0.04167469640675162,
        "hill_tail_index": 2.1267286569256805
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.018224975242251102,
        "excess_kurtosis": 16.27004324900638,
        "return_acf_1": -0.15180779286558432,
        "abs_return_acf_1": 0.3290906833230195,
        "abs_return_acf_5": 0.3583112470667477,
        "abs_return_acf_20": 0.22788672236347757,
        "quantile_01": -0.05464891679341445,
        "quantile_99": 0.0477121026801087,
        "hill_tail_index": 2.3620145162888666
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017400161494023254,
        "excess_kurtosis": 3.857945115439243,
        "return_acf_1": -0.18540529800082725,
        "abs_return_acf_1": 0.35047264278849033,
        "abs_return_acf_5": 0.3392780996010269,
        "abs_return_acf_20": 0.2256149755997116,
        "quantile_01": -0.04794263207276617,
        "quantile_99": 0.050027158583123996,
        "hill_tail_index": 4.149287160236217
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.018140466094112913,
        "excess_kurtosis": 4.065965186345256,
        "return_acf_1": -0.16090218277597612,
        "abs_return_acf_1": 0.37494542061742936,
        "abs_return_acf_5": 0.3173366898941185,
        "abs_return_acf_20": 0.25630212682966996,
        "quantile_01": -0.056836612627869924,
        "quantile_99": 0.053128892743981804,
        "hill_tail_index": 4.124225585378629
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01765713134752602,
        "excess_kurtosis": 5.202999275061988,
        "return_acf_1": -0.17608033576392038,
        "abs_return_acf_1": 0.34038348209573305,
        "abs_return_acf_5": 0.3614664487034444,
        "abs_return_acf_20": 0.3072106187567798,
        "quantile_01": -0.05716208015301913,
        "quantile_99": 0.05814239759825416,
        "hill_tail_index": 3.461332079206122
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
