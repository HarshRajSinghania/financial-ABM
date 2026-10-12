# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27052
Run ID: `f162af7960487c15840b81f53f3c26ec10632866f0b5d438774d82d8fa793031`
Result fingerprint: `bb66e88588258b8a90b22d8cbecd9718a14ed322ac14d5591b14bac6fcabe135`

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
    "equal_weight_sd": -0.5251309523809491,
    "equal_weight_raw": -7.876964285714237,
    "fixed_start_cap_weight_sd": -0.511366280278368,
    "fixed_start_cap_weight_raw": -7.670494204175521,
    "end_cap_weight_sd": -0.5171891235212184,
    "end_cap_weight_raw": -7.7578368528182775
  },
  "full_period_change": {
    "equal_weight_sd": -0.8147380952380903,
    "equal_weight_raw": -12.221071428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.7649169973544928,
    "inflation_mean_sd": 0.5158607804232804
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4272500000000033,
    "equal_weight_raw": 6.408750000000048,
    "fixed_start_cap_weight_sd": 0.4410146721025844,
    "fixed_start_cap_weight_raw": 6.615220081538766,
    "end_cap_weight_sd": 0.43519182885973384,
    "end_cap_weight_raw": 6.527877432896006
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6215476190476158,
      "change_raw": -9.323214285714236,
      "decay_adjusted_gain_sd": 0.3308333333333366
    },
    "mid": {
      "count": 9,
      "change_sd": -0.45432539682539347,
      "change_raw": -6.814880952380902,
      "decay_adjusted_gain_sd": 0.4980555555555588
    },
    "small": {
      "count": 18,
      "change_sd": -0.5444642857142825,
      "change_raw": -8.166964285714238,
      "decay_adjusted_gain_sd": 0.4079166666666698
    },
    "large_minus_small_sd": -0.07708333333333328,
    "large_minus_small_raw": -1.1562499999999991
  },
  "inflation": {
    "initial_mean_sd": 0.22924999999999998,
    "final_mean_sd": 0.539,
    "mean_sd": 0.41417069109075777,
    "mean_absolute_raw_gap": 6.212560366361365,
    "final_absolute_raw_gap": 8.084999999999999,
    "mean_range_fraction": 0.06212560366361365
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.25333333333333335,
    "initial_wealth_share": 0.14501372932583678,
    "final_wealth_share": 0.22663504425915934
  },
  "pricing_slope": {
    "mean": 0.00041411254106447036,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.19820605187302773,
    "real_improvement_cost": 0.16613127546732556,
    "washing_cost": 0.03207477640570218,
    "fine_transfer": 0.0027134522414376363,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.20091950411446535,
    "resource_cost_fraction_initial_cap": 0.006606868395767591,
    "private_net_outflow_fraction_initial_cap": 0.006697316803815512,
    "fine_transfer_fraction_initial_cap": 9.04484080479212e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.01396912553750883,
    "unapplied_final_day_resource_cost": 0.009638855120251281
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 64.66755116140996,
    "beneficial_raw_gain_per_resource_cost": 970.0132674211494,
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
    "accrued_cost": 3.045712070832246,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": -0.06952159464176927,
    "accrued_cost_fraction_initial_cap": 0.10152373569440819,
    "mean_contract_rate": 0.042035942234112784,
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
    "price_cap_hits": 17,
    "maximum_relative_cash_error": 1.796243111250846e-15,
    "maximum_absolute_share_error": 1.6653345369377348e-15,
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
      "minimum": -0.3958548031535578,
      "maximum": -0.05261638647729737,
      "mean": -0.2943607396295306,
      "median": -0.30884341608388577,
      "quantile_05": -0.3871509098350056,
      "quantile_95": -0.08569467030425755
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
      "minimum": 0.10779539588936635,
      "maximum": 0.8496059550372012,
      "mean": 0.6623137013046172,
      "median": 0.7719945881139263,
      "quantile_05": 0.21280022943965066,
      "quantile_95": 0.8292712521855328
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
        "daily_volatility": 0.022629080330484247,
        "excess_kurtosis": 41.87360616324339,
        "return_acf_1": -0.34757310387825063,
        "abs_return_acf_1": 0.5560337165548939,
        "abs_return_acf_5": 0.40507751046594687,
        "abs_return_acf_20": 0.3085787354701143,
        "quantile_01": -0.06909059408043523,
        "quantile_99": 0.05355754889619883,
        "hill_tail_index": 1.7630588189708456
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.023703888879450418,
        "excess_kurtosis": 36.52290324454663,
        "return_acf_1": -0.3591620690562295,
        "abs_return_acf_1": 0.5094589550219214,
        "abs_return_acf_5": 0.36488912243970656,
        "abs_return_acf_20": 0.33655172517283477,
        "quantile_01": -0.06925600701568918,
        "quantile_99": 0.05521850819352068,
        "hill_tail_index": 1.875243811826033
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022746679584187388,
        "excess_kurtosis": 46.69849840326074,
        "return_acf_1": -0.3958548031535578,
        "abs_return_acf_1": 0.612902098612998,
        "abs_return_acf_5": 0.3412358510478018,
        "abs_return_acf_20": 0.26866610974793587,
        "quantile_01": -0.07485153435863723,
        "quantile_99": 0.05744744985043001,
        "hill_tail_index": 2.052935757552245
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.022102687213824156,
        "excess_kurtosis": 30.53400272875875,
        "return_acf_1": -0.30362881216736476,
        "abs_return_acf_1": 0.5138779499090393,
        "abs_return_acf_5": 0.35596599062627465,
        "abs_return_acf_20": 0.31065447483918973,
        "quantile_01": -0.07680554990924694,
        "quantile_99": 0.054318454102692544,
        "hill_tail_index": 2.189029505286342
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02399544586480029,
        "excess_kurtosis": 33.04724830248356,
        "return_acf_1": -0.33596980493326495,
        "abs_return_acf_1": 0.5329152968837979,
        "abs_return_acf_5": 0.3895206873373858,
        "abs_return_acf_20": 0.278179522438441,
        "quantile_01": -0.07431777982285406,
        "quantile_99": 0.0606983385538351,
        "hill_tail_index": 1.9874766260993804
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021219731944539206,
        "excess_kurtosis": 18.43187719820155,
        "return_acf_1": -0.26696020624776534,
        "abs_return_acf_1": 0.5243353003087846,
        "abs_return_acf_5": 0.40909827666187104,
        "abs_return_acf_20": 0.31174622999163276,
        "quantile_01": -0.07520469593757623,
        "quantile_99": 0.045557515097444976,
        "hill_tail_index": 1.6881131327764742
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01847544708231529,
        "excess_kurtosis": 14.014582698286738,
        "return_acf_1": -0.06796406969329818,
        "abs_return_acf_1": 0.46789077952466707,
        "abs_return_acf_5": 0.43447412938704255,
        "abs_return_acf_20": 0.30529704477968583,
        "quantile_01": -0.06069076513558832,
        "quantile_99": 0.05385040297846142,
        "hill_tail_index": 3.2272798674841603
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02261120695088382,
        "excess_kurtosis": 28.43781274026335,
        "return_acf_1": -0.2936054928215258,
        "abs_return_acf_1": 0.470495208586962,
        "abs_return_acf_5": 0.31218240082127247,
        "abs_return_acf_20": 0.25588541619665334,
        "quantile_01": -0.07220531043414893,
        "quantile_99": 0.05633980821653506,
        "hill_tail_index": 2.0473899420918444
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.021391180799982357,
        "excess_kurtosis": 39.34531169090524,
        "return_acf_1": -0.3898637292944973,
        "abs_return_acf_1": 0.5575293049233945,
        "abs_return_acf_5": 0.4123575336478003,
        "abs_return_acf_20": 0.2941908059838676,
        "quantile_01": -0.06380019241276223,
        "quantile_99": 0.05674079328756782,
        "hill_tail_index": 2.223207132428933
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022136235852350673,
        "excess_kurtosis": 30.878316202771174,
        "return_acf_1": -0.3066362914101679,
        "abs_return_acf_1": 0.4458442730753989,
        "abs_return_acf_5": 0.309359957378562,
        "abs_return_acf_20": 0.302256295617616,
        "quantile_01": -0.0723165123150871,
        "quantile_99": 0.04862793380256492,
        "hill_tail_index": 2.2933289099911933
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022398158714747617,
        "excess_kurtosis": 14.139570268491294,
        "return_acf_1": -0.2675662574152265,
        "abs_return_acf_1": 0.4347304317878304,
        "abs_return_acf_5": 0.3607801695044138,
        "abs_return_acf_20": 0.2958070792962578,
        "quantile_01": -0.08229512186739561,
        "quantile_99": 0.055857823280673756,
        "hill_tail_index": 2.733991955518386
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02291898291771084,
        "excess_kurtosis": 33.6977480464344,
        "return_acf_1": -0.29413424262450516,
        "abs_return_acf_1": 0.4812904452862256,
        "abs_return_acf_5": 0.3727463844453177,
        "abs_return_acf_20": 0.32008104948979715,
        "quantile_01": -0.07754215859554417,
        "quantile_99": 0.05493404599182762,
        "hill_tail_index": 2.213622122500981
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.023058120408295697,
        "excess_kurtosis": 38.25838300051088,
        "return_acf_1": -0.38383524160673793,
        "abs_return_acf_1": 0.5805205670682252,
        "abs_return_acf_5": 0.4065395465043304,
        "abs_return_acf_20": 0.3185160790276641,
        "quantile_01": -0.07483146014638525,
        "quantile_99": 0.057983396381708255,
        "hill_tail_index": 1.9818074700744694
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019585431037495108,
        "excess_kurtosis": 12.398235235870931,
        "return_acf_1": -0.2439478890549284,
        "abs_return_acf_1": 0.5040961189073881,
        "abs_return_acf_5": 0.38080449072577416,
        "abs_return_acf_20": 0.3020249113816792,
        "quantile_01": -0.06125469497263482,
        "quantile_99": 0.05999554444639378,
        "hill_tail_index": 2.7909654463878217
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021144584970214476,
        "excess_kurtosis": 30.31043115534454,
        "return_acf_1": -0.30088689373119615,
        "abs_return_acf_1": 0.43977720605565124,
        "abs_return_acf_5": 0.30836506325538865,
        "abs_return_acf_20": 0.2714004326691412,
        "quantile_01": -0.061064566353458465,
        "quantile_99": 0.04676752131919703,
        "hill_tail_index": 1.7908653542253956
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.023887924462230124,
        "excess_kurtosis": 29.09760839483996,
        "return_acf_1": -0.3103150377428889,
        "abs_return_acf_1": 0.4949549836951349,
        "abs_return_acf_5": 0.3635488318727453,
        "abs_return_acf_20": 0.31786216037279935,
        "quantile_01": -0.07122250648917586,
        "quantile_99": 0.062063123359219693,
        "hill_tail_index": 2.486764822393979
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022366157231512404,
        "excess_kurtosis": 34.98171851943394,
        "return_acf_1": -0.3237172278466252,
        "abs_return_acf_1": 0.5689934045611906,
        "abs_return_acf_5": 0.46039929719383366,
        "abs_return_acf_20": 0.3525407236880344,
        "quantile_01": -0.06831334766320447,
        "quantile_99": 0.05108353813009748,
        "hill_tail_index": 1.9698609941981187
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.021489818967278484,
        "excess_kurtosis": 42.1913419793771,
        "return_acf_1": -0.33306386414337324,
        "abs_return_acf_1": 0.5059056798522186,
        "abs_return_acf_5": 0.3230480022120531,
        "abs_return_acf_20": 0.23254169134449382,
        "quantile_01": -0.061190293745259,
        "quantile_99": 0.04727462928771819,
        "hill_tail_index": 1.7899449337160338
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02262570973542912,
        "excess_kurtosis": 42.98726528972617,
        "return_acf_1": -0.34256263002903775,
        "abs_return_acf_1": 0.4684638912363761,
        "abs_return_acf_5": 0.32096332307373004,
        "abs_return_acf_20": 0.30991595733138055,
        "quantile_01": -0.06976889588528647,
        "quantile_99": 0.05281917203519114,
        "hill_tail_index": 1.8623983306835106
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022485845542660483,
        "excess_kurtosis": 44.9862927354167,
        "return_acf_1": -0.36302602183071464,
        "abs_return_acf_1": 0.533247022102515,
        "abs_return_acf_5": 0.2743220050891221,
        "abs_return_acf_20": 0.21446414585628468,
        "quantile_01": -0.06149760758808455,
        "quantile_99": 0.047891769476487725,
        "hill_tail_index": 1.9886225699192674
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.022435152788380156,
        "excess_kurtosis": 40.77550607496003,
        "return_acf_1": -0.3836475077124939,
        "abs_return_acf_1": 0.5497125931834134,
        "abs_return_acf_5": 0.3572374015354802,
        "abs_return_acf_20": 0.2823370851147196,
        "quantile_01": -0.07383451548388237,
        "quantile_99": 0.05598116944150713,
        "hill_tail_index": 1.93871699393455
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022580665168462452,
        "excess_kurtosis": 38.34405811285538,
        "return_acf_1": -0.3817849813075472,
        "abs_return_acf_1": 0.5552427119751604,
        "abs_return_acf_5": 0.34632113524066777,
        "abs_return_acf_20": 0.300148184135978,
        "quantile_01": -0.06922172613094096,
        "quantile_99": 0.05137070390396063,
        "hill_tail_index": 2.208161841892007
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02122927968775228,
        "excess_kurtosis": 10.43448271824572,
        "return_acf_1": -0.1363247527175313,
        "abs_return_acf_1": 0.38232441471766165,
        "abs_return_acf_5": 0.33149554302116707,
        "abs_return_acf_20": 0.32219940080693743,
        "quantile_01": -0.056953197658105074,
        "quantile_99": 0.07370284157973754,
        "hill_tail_index": 2.8259281166860086
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.021360633979236838,
        "excess_kurtosis": 26.91586594039674,
        "return_acf_1": -0.30737179442488266,
        "abs_return_acf_1": 0.49814995310770954,
        "abs_return_acf_5": 0.39495360554104103,
        "abs_return_acf_20": 0.3472952259957362,
        "quantile_01": -0.0673407768078961,
        "quantile_99": 0.05681152630133591,
        "hill_tail_index": 2.4028397242624995
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.022746356822760078,
        "excess_kurtosis": 25.726524402836308,
        "return_acf_1": -0.30666193381728907,
        "abs_return_acf_1": 0.5148912654743485,
        "abs_return_acf_5": 0.33029449903554464,
        "abs_return_acf_20": 0.30218965976842516,
        "quantile_01": -0.07566099080579208,
        "quantile_99": 0.05920906750877552,
        "hill_tail_index": 2.174068957354261
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021032633576923282,
        "excess_kurtosis": 24.9975062722622,
        "return_acf_1": -0.3151131359387758,
        "abs_return_acf_1": 0.5147189396738153,
        "abs_return_acf_5": 0.3636972229520354,
        "abs_return_acf_20": 0.28982057507413966,
        "quantile_01": -0.0663460980935447,
        "quantile_99": 0.055381601730468105,
        "hill_tail_index": 2.9654485787445486
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02171466616059496,
        "excess_kurtosis": 23.439368753958295,
        "return_acf_1": -0.27118638189837035,
        "abs_return_acf_1": 0.5557611806841414,
        "abs_return_acf_5": 0.4949322617005921,
        "abs_return_acf_20": 0.3748919684243153,
        "quantile_01": -0.06987186337411157,
        "quantile_99": 0.058367270457045886,
        "hill_tail_index": 2.151172132007474
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020909980257360152,
        "excess_kurtosis": 13.140346500607311,
        "return_acf_1": -0.05261638647729737,
        "abs_return_acf_1": 0.3651552880220062,
        "abs_return_acf_5": 0.4049392416865202,
        "abs_return_acf_20": 0.2261608258387124,
        "quantile_01": -0.0600256327301654,
        "quantile_99": 0.0627002071011109,
        "hill_tail_index": 2.786644084610398
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019486392725475598,
        "excess_kurtosis": 13.050913523381489,
        "return_acf_1": -0.10736540438431874,
        "abs_return_acf_1": 0.472448429734746,
        "abs_return_acf_5": 0.3720615493380391,
        "abs_return_acf_20": 0.29877716900216383,
        "quantile_01": -0.05642674377408393,
        "quantile_99": 0.05710325060215664,
        "hill_tail_index": 2.5056983367548984
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02180758534247812,
        "excess_kurtosis": 34.76301315309677,
        "return_acf_1": -0.3384762215262558,
        "abs_return_acf_1": 0.5394346208615736,
        "abs_return_acf_5": 0.4357043551237887,
        "abs_return_acf_20": 0.315928470310766,
        "quantile_01": -0.07231556324736287,
        "quantile_99": 0.05104752106076711,
        "hill_tail_index": 1.6687372247837498
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
