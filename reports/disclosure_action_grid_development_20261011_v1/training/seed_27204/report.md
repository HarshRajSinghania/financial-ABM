# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27204
Run ID: `ea4cc198f4fcad46e5ecabf9adbb8deb309527c8cefb2102c4364341917b7abc`
Result fingerprint: `e1bab0e026043d44137f760106900badd65a85b9abc491bd92f15195b651c555`

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
    "equal_weight_sd": -0.7767976190476158,
    "equal_weight_raw": -11.651964285714238,
    "fixed_start_cap_weight_sd": -0.7680800746239963,
    "fixed_start_cap_weight_raw": -11.521201119359944,
    "end_cap_weight_sd": -0.7553367555835171,
    "end_cap_weight_raw": -11.330051333752756
  },
  "full_period_change": {
    "equal_weight_sd": -1.21098809523809,
    "equal_weight_raw": -18.16482142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.118267526455022,
    "inflation_mean_sd": 0.4931957671957672
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1755833333333365,
    "equal_weight_raw": 2.633750000000047,
    "fixed_start_cap_weight_sd": 0.18430087775695622,
    "fixed_start_cap_weight_raw": 2.764513166354343,
    "end_cap_weight_sd": 0.19704419679743554,
    "end_cap_weight_raw": 2.9556629519615334
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8057142857142825,
      "change_raw": -12.085714285714237,
      "decay_adjusted_gain_sd": 0.1466666666666698
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6659920634920602,
      "change_raw": -9.989880952380902,
      "decay_adjusted_gain_sd": 0.2863888888888921
    },
    "small": {
      "count": 18,
      "change_sd": -0.8273809523809492,
      "change_raw": -12.410714285714239,
      "decay_adjusted_gain_sd": 0.12500000000000314
    },
    "large_minus_small_sd": 0.021666666666666723,
    "large_minus_small_raw": 0.32500000000000084
  },
  "inflation": {
    "initial_mean_sd": 0.2541666666666667,
    "final_mean_sd": 0.5314166666666666,
    "mean_sd": 0.36686074104912575,
    "mean_absolute_raw_gap": 5.502911115736886,
    "final_absolute_raw_gap": 7.971249999999999,
    "mean_range_fraction": 0.05502911115736886
  },
  "impact": {
    "initial_share": 0.35333333333333333,
    "final_share": 0.37333333333333335,
    "initial_wealth_share": 0.3999456341886123,
    "final_wealth_share": 0.42965341474870866
  },
  "pricing_slope": {
    "mean": -0.0033385112913393586,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.027824625730790815,
    "real_improvement_cost": 0.020017929585249693,
    "washing_cost": 0.007806696145541121,
    "fine_transfer": 0.00861287603655917,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.036437501767349986,
    "resource_cost_fraction_initial_cap": 0.0009274875243596937,
    "private_net_outflow_fraction_initial_cap": 0.0012145833922449995,
    "fine_transfer_fraction_initial_cap": 0.0002870958678853057,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0010176413597613623,
    "unapplied_final_day_resource_cost": 0.0005565658069043782
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 189.31072248605534,
    "beneficial_raw_gain_per_resource_cost": 2839.6608372908304,
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
    "accrued_cost": 3.0148576798582942,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.03866720366781741,
    "accrued_cost_fraction_initial_cap": 0.10049525599527646,
    "mean_contract_rate": 0.042021321422930615,
    "maximum_ledger_error": 7.115076756936123e-20
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
    "maximum_relative_cash_error": 2.307679209638628e-15,
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
      "minimum": -0.22574682540856253,
      "maximum": 0.03215136904378639,
      "mean": -0.09629453495391707,
      "median": -0.08832786230449599,
      "quantile_05": -0.170871948322576,
      "quantile_95": -0.018397075465997597
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
      "minimum": 0.17889392619911185,
      "maximum": 0.807667836007474,
      "mean": 0.5035915471346484,
      "median": 0.48025831193929236,
      "quantile_05": 0.25751655515000826,
      "quantile_95": 0.7705753683897985
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
        "daily_volatility": 0.023967380569148013,
        "excess_kurtosis": 11.604647064425047,
        "return_acf_1": -0.22574682540856253,
        "abs_return_acf_1": 0.4954241965582298,
        "abs_return_acf_5": 0.38743761458147463,
        "abs_return_acf_20": 0.4082403215279003,
        "quantile_01": -0.08417827089818157,
        "quantile_99": 0.07507443213526105,
        "hill_tail_index": 3.356018990488327
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.024051577927818025,
        "excess_kurtosis": 16.73641853024003,
        "return_acf_1": -0.058334403787071415,
        "abs_return_acf_1": 0.38823366240367857,
        "abs_return_acf_5": 0.43361223811407307,
        "abs_return_acf_20": 0.2611666975619734,
        "quantile_01": -0.07965648678365006,
        "quantile_99": 0.06931669455130791,
        "hill_tail_index": 2.3734772613643305
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.02296065671456926,
        "excess_kurtosis": 13.147331099813538,
        "return_acf_1": -0.061850377514147,
        "abs_return_acf_1": 0.47125142774209733,
        "abs_return_acf_5": 0.4774961459351681,
        "abs_return_acf_20": 0.3487239938458189,
        "quantile_01": -0.08186976300373908,
        "quantile_99": 0.07534062330275726,
        "hill_tail_index": 2.887893237878239
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02585358793644211,
        "excess_kurtosis": 18.489940875465468,
        "return_acf_1": -0.10633687415743129,
        "abs_return_acf_1": 0.4186086650285618,
        "abs_return_acf_5": 0.4437748404757204,
        "abs_return_acf_20": 0.2776925457393383,
        "quantile_01": -0.09611219219907063,
        "quantile_99": 0.07185370697317252,
        "hill_tail_index": 2.1902789344509546
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019187215334470802,
        "excess_kurtosis": 4.094510106814884,
        "return_acf_1": -0.1670986611001401,
        "abs_return_acf_1": 0.2977997904734115,
        "abs_return_acf_5": 0.20843523494950986,
        "abs_return_acf_20": 0.1920257281991691,
        "quantile_01": -0.05237936877099654,
        "quantile_99": 0.05077223187464987,
        "hill_tail_index": 3.334721278558478
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021253541533205324,
        "excess_kurtosis": 6.518967111066871,
        "return_acf_1": -0.03473121115736341,
        "abs_return_acf_1": 0.36402344640771556,
        "abs_return_acf_5": 0.37177367787792204,
        "abs_return_acf_20": 0.24049717048898786,
        "quantile_01": -0.0660664973212368,
        "quantile_99": 0.0671680926654954,
        "hill_tail_index": 3.7610661086259367
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.022149425396161722,
        "excess_kurtosis": 7.08070862695098,
        "return_acf_1": -0.014702349450064881,
        "abs_return_acf_1": 0.3429039734698907,
        "abs_return_acf_5": 0.3549525456095189,
        "abs_return_acf_20": 0.22727974688469754,
        "quantile_01": -0.06875998738747778,
        "quantile_99": 0.061242689101573496,
        "hill_tail_index": 2.9010102490185012
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02381916727778695,
        "excess_kurtosis": 18.557761013789634,
        "return_acf_1": -0.15629628928105513,
        "abs_return_acf_1": 0.46722243864008306,
        "abs_return_acf_5": 0.31315868234203964,
        "abs_return_acf_20": 0.31014590180629675,
        "quantile_01": -0.0865970215971686,
        "quantile_99": 0.06454753174543869,
        "hill_tail_index": 2.592384225591437
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.023877532241555074,
        "excess_kurtosis": 10.084334412879983,
        "return_acf_1": -0.1280351923365345,
        "abs_return_acf_1": 0.4532364241720905,
        "abs_return_acf_5": 0.4493025967224009,
        "abs_return_acf_20": 0.306697795421154,
        "quantile_01": -0.08841465929867424,
        "quantile_99": 0.06549410524089039,
        "hill_tail_index": 2.448589103290492
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021219720851566804,
        "excess_kurtosis": 15.744182048543298,
        "return_acf_1": 0.03215136904378639,
        "abs_return_acf_1": 0.4020697242907373,
        "abs_return_acf_5": 0.4360555299646417,
        "abs_return_acf_20": 0.2732065081281675,
        "quantile_01": -0.07227829382063036,
        "quantile_99": 0.056696953367232024,
        "hill_tail_index": 2.338986841494195
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.022417237216897097,
        "excess_kurtosis": 8.202485250141532,
        "return_acf_1": -0.07523212951250056,
        "abs_return_acf_1": 0.3349344716301042,
        "abs_return_acf_5": 0.3321606255944438,
        "abs_return_acf_20": 0.23666968810366523,
        "quantile_01": -0.08349135865409903,
        "quantile_99": 0.06241786757425112,
        "hill_tail_index": 2.799732496169948
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02675810859394452,
        "excess_kurtosis": 22.389031961922477,
        "return_acf_1": -0.08645798433643608,
        "abs_return_acf_1": 0.4483467630520745,
        "abs_return_acf_5": 0.4319803227430841,
        "abs_return_acf_20": 0.24868687490087085,
        "quantile_01": -0.08373323416895721,
        "quantile_99": 0.08528593069911604,
        "hill_tail_index": 2.1801613982732797
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.022020351440398003,
        "excess_kurtosis": 4.865288178183247,
        "return_acf_1": -0.022912851707693086,
        "abs_return_acf_1": 0.3981472007979536,
        "abs_return_acf_5": 0.3684172045649352,
        "abs_return_acf_20": 0.3206343225478684,
        "quantile_01": -0.07123821204372287,
        "quantile_99": 0.06833525653664255,
        "hill_tail_index": 4.401940519762043
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01826717536954945,
        "excess_kurtosis": 6.5882584236664155,
        "return_acf_1": -0.045604263148903756,
        "abs_return_acf_1": 0.3296896440823257,
        "abs_return_acf_5": 0.3167006223022791,
        "abs_return_acf_20": 0.23213362780121813,
        "quantile_01": -0.060757752350731754,
        "quantile_99": 0.04616315053977637,
        "hill_tail_index": 3.051603061141864
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.02374210424687592,
        "excess_kurtosis": 11.124546757513366,
        "return_acf_1": -0.11526033219823938,
        "abs_return_acf_1": 0.48958222550577923,
        "abs_return_acf_5": 0.4474837630081741,
        "abs_return_acf_20": 0.35953237610933997,
        "quantile_01": -0.08373388907191624,
        "quantile_99": 0.06992758567402446,
        "hill_tail_index": 3.184925055012949
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020229294828492454,
        "excess_kurtosis": 7.597477308241812,
        "return_acf_1": -0.12931943666055096,
        "abs_return_acf_1": 0.44847911309747035,
        "abs_return_acf_5": 0.35131076592576566,
        "abs_return_acf_20": 0.26167815551795237,
        "quantile_01": -0.06285432998082305,
        "quantile_99": 0.05992236538953939,
        "hill_tail_index": 3.6811809552570653
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021574203945977553,
        "excess_kurtosis": 10.602062179233604,
        "return_acf_1": -0.1739591833227508,
        "abs_return_acf_1": 0.3209851616678691,
        "abs_return_acf_5": 0.28843095715586015,
        "abs_return_acf_20": 0.22797678512182754,
        "quantile_01": -0.053972191649505265,
        "quantile_99": 0.07334771278783932,
        "hill_tail_index": 2.985293607036414
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02250499495387932,
        "excess_kurtosis": 10.583490011440544,
        "return_acf_1": -0.06801160928739443,
        "abs_return_acf_1": 0.41258603499854396,
        "abs_return_acf_5": 0.36925389521282664,
        "abs_return_acf_20": 0.3007831727338026,
        "quantile_01": -0.07869822850628293,
        "quantile_99": 0.0577091323140854,
        "hill_tail_index": 2.658885969444617
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02140031116348732,
        "excess_kurtosis": 10.690017207086596,
        "return_acf_1": -0.07602981823736397,
        "abs_return_acf_1": 0.3764190562304435,
        "abs_return_acf_5": 0.3338452352944637,
        "abs_return_acf_20": 0.2333462552370836,
        "quantile_01": -0.06622620968405338,
        "quantile_99": 0.05458022985484432,
        "hill_tail_index": 2.658611944208364
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.025436375366576454,
        "excess_kurtosis": 15.034446238173675,
        "return_acf_1": -0.1112384987059762,
        "abs_return_acf_1": 0.5027250596869326,
        "abs_return_acf_5": 0.3708110847178365,
        "abs_return_acf_20": 0.3005900089743537,
        "quantile_01": -0.1035073008805518,
        "quantile_99": 0.08120625882632501,
        "hill_tail_index": 2.75716337708502
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01998561942919273,
        "excess_kurtosis": 8.894210535953357,
        "return_acf_1": -0.10710647466614513,
        "abs_return_acf_1": 0.3283830966528989,
        "abs_return_acf_5": 0.25395583753278567,
        "abs_return_acf_20": 0.18134847867222448,
        "quantile_01": -0.05291531240367951,
        "quantile_99": 0.059404212675821765,
        "hill_tail_index": 3.177007558936508
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022710774680037293,
        "excess_kurtosis": 12.839811436735726,
        "return_acf_1": -0.14866564726874315,
        "abs_return_acf_1": 0.4609225276506008,
        "abs_return_acf_5": 0.3705374497695835,
        "abs_return_acf_20": 0.29463780200628964,
        "quantile_01": -0.07763447090267303,
        "quantile_99": 0.06229770297841483,
        "hill_tail_index": 2.2947507648578616
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02094395700901705,
        "excess_kurtosis": 4.942582032013432,
        "return_acf_1": -0.07010604028407741,
        "abs_return_acf_1": 0.3992445843072052,
        "abs_return_acf_5": 0.43131673390944303,
        "abs_return_acf_20": 0.28298551132307526,
        "quantile_01": -0.07501824690002148,
        "quantile_99": 0.05835739412709893,
        "hill_tail_index": 4.287680271385189
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02483742280579071,
        "excess_kurtosis": 14.99968034498313,
        "return_acf_1": -0.14709113222330442,
        "abs_return_acf_1": 0.4860851213488159,
        "abs_return_acf_5": 0.3583904800710297,
        "abs_return_acf_20": 0.29600112077193913,
        "quantile_01": -0.07836362880743275,
        "quantile_99": 0.06258251492571484,
        "hill_tail_index": 2.1463184884714526
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021669395786299967,
        "excess_kurtosis": 8.615493913477,
        "return_acf_1": -0.15720619895375174,
        "abs_return_acf_1": 0.38607756958481604,
        "abs_return_acf_5": 0.3494169345353874,
        "abs_return_acf_20": 0.25461772856254744,
        "quantile_01": -0.06372273058507331,
        "quantile_99": 0.06826241088170175,
        "hill_tail_index": 3.729632023500996
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02322098969493549,
        "excess_kurtosis": 17.114309198911986,
        "return_acf_1": -0.05101788669180383,
        "abs_return_acf_1": 0.3643995992009112,
        "abs_return_acf_5": 0.365849625826551,
        "abs_return_acf_20": 0.21348049462722418,
        "quantile_01": -0.06283114954765734,
        "quantile_99": 0.0773758771492832,
        "hill_tail_index": 2.5496474505923272
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02434822826228834,
        "excess_kurtosis": 11.878186698754973,
        "return_acf_1": -0.0901977402725559,
        "abs_return_acf_1": 0.4340922669048322,
        "abs_return_acf_5": 0.3377553512757328,
        "abs_return_acf_20": 0.34910856591429135,
        "quantile_01": -0.09578963244586293,
        "quantile_99": 0.061454781755402234,
        "hill_tail_index": 2.189807861593363
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019373296180809633,
        "excess_kurtosis": 6.519861813973726,
        "return_acf_1": -0.05414954647595449,
        "abs_return_acf_1": 0.3120145002229084,
        "abs_return_acf_5": 0.30678047081828214,
        "abs_return_acf_20": 0.26056130437987934,
        "quantile_01": -0.06344817594050459,
        "quantile_99": 0.05731865438022144,
        "hill_tail_index": 3.4775849764834845
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0236814232171528,
        "excess_kurtosis": 10.004456985041527,
        "return_acf_1": -0.07625752144188047,
        "abs_return_acf_1": 0.3891991707547045,
        "abs_return_acf_5": 0.38302857754497965,
        "abs_return_acf_20": 0.2960884744110909,
        "quantile_01": -0.09429817728489613,
        "quantile_99": 0.06229368001279254,
        "hill_tail_index": 2.3379747340230157
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01940579273167288,
        "excess_kurtosis": 8.698854485938282,
        "return_acf_1": -0.16203093807290317,
        "abs_return_acf_1": 0.2804997349160112,
        "abs_return_acf_5": 0.2841512088703256,
        "abs_return_acf_20": 0.23353380021317421,
        "quantile_01": -0.05232807539050427,
        "quantile_99": 0.0640922805545592,
        "hill_tail_index": 3.3402578438542574
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
