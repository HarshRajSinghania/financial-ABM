# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27146
Run ID: `514732d26e4410673ee258ad19c99ae3c207e8efb7d15df3c63a40d919a8b011`
Result fingerprint: `a6e4226d125d57ed8783ffcff64eeee2f274565da688ecbb2783b418f1b65b59`

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
    "equal_weight_sd": -0.6835476190476157,
    "equal_weight_raw": -10.25321428571424,
    "fixed_start_cap_weight_sd": -0.7054136064108519,
    "fixed_start_cap_weight_raw": -10.58120409616278,
    "end_cap_weight_sd": -0.7165844073865302,
    "end_cap_weight_raw": -10.748766110797956
  },
  "full_period_change": {
    "equal_weight_sd": -1.0380714285714236,
    "equal_weight_raw": -15.571071428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9714593253968208,
    "inflation_mean_sd": 0.5490469576719577
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2688333333333366,
    "equal_weight_raw": 4.032500000000049,
    "fixed_start_cap_weight_sd": 0.24696734597010042,
    "fixed_start_cap_weight_raw": 3.704510189551507,
    "end_cap_weight_sd": 0.23579654499442199,
    "end_cap_weight_raw": 3.5369481749163305
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7765476190476158,
      "change_raw": -11.648214285714237,
      "decay_adjusted_gain_sd": 0.1758333333333365
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7204365079365046,
      "change_raw": -10.806547619047569,
      "decay_adjusted_gain_sd": 0.2319444444444477
    },
    "small": {
      "count": 18,
      "change_sd": -0.6496031746031713,
      "change_raw": -9.744047619047569,
      "decay_adjusted_gain_sd": 0.302777777777781
    },
    "large_minus_small_sd": -0.12694444444444453,
    "large_minus_small_raw": -1.904166666666668
  },
  "inflation": {
    "initial_mean_sd": 0.2866666666666667,
    "final_mean_sd": 0.6009999999999999,
    "mean_sd": 0.4605392728281988,
    "mean_absolute_raw_gap": 6.908089092422981,
    "final_absolute_raw_gap": 9.015000000000002,
    "mean_range_fraction": 0.06908089092422981
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.18,
    "initial_wealth_share": 0.22976068930697635,
    "final_wealth_share": 0.2042474627854539
  },
  "pricing_slope": {
    "mean": -0.0023221047222556617,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.09312864887997266,
    "real_improvement_cost": 0.07346834620139829,
    "washing_cost": 0.019660302678574375,
    "fine_transfer": 0.03334358674337241,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12647223562334506,
    "resource_cost_fraction_initial_cap": 0.0031042882959990883,
    "private_net_outflow_fraction_initial_cap": 0.004215741187444835,
    "fine_transfer_fraction_initial_cap": 0.0011114528914457468,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.006700311335796344,
    "unapplied_final_day_resource_cost": 0.0034544226791251
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 86.60063360732894,
    "beneficial_raw_gain_per_resource_cost": 1299.0095041099341,
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
    "accrued_cost": 3.032848040220066,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.05665756402958955,
    "accrued_cost_fraction_initial_cap": 0.10109493467400218,
    "mean_contract_rate": 0.04161604621154656,
    "maximum_ledger_error": 4.573977915173222e-20
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
    "maximum_relative_cash_error": 2.4227402765347478e-15,
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
      "minimum": -0.2367469580818389,
      "maximum": -0.10969659497197273,
      "mean": -0.168020335160439,
      "median": -0.16412113726113925,
      "quantile_05": -0.22611378997969941,
      "quantile_95": -0.12227808214915621
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
      "minimum": 0.41532307481521025,
      "maximum": 0.7917466712782643,
      "mean": 0.6765540954551429,
      "median": 0.6957870327032318,
      "quantile_05": 0.5197964011921339,
      "quantile_95": 0.7601111130886841
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
        "daily_volatility": 0.019371671433544953,
        "excess_kurtosis": 8.558255825742789,
        "return_acf_1": -0.10969659497197273,
        "abs_return_acf_1": 0.3428036494009729,
        "abs_return_acf_5": 0.34772932261970635,
        "abs_return_acf_20": 0.27422490851718956,
        "quantile_01": -0.05826817862991413,
        "quantile_99": 0.05727692933236543,
        "hill_tail_index": 3.28995087264464
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01837956583308492,
        "excess_kurtosis": 6.603316839105824,
        "return_acf_1": -0.16431985734261054,
        "abs_return_acf_1": 0.3850821547669167,
        "abs_return_acf_5": 0.3005412714479319,
        "abs_return_acf_20": 0.29274193670612514,
        "quantile_01": -0.05605666432106107,
        "quantile_99": 0.05493497514356303,
        "hill_tail_index": 3.6718019565302136
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019581318161902058,
        "excess_kurtosis": 7.880882249586588,
        "return_acf_1": -0.2367469580818389,
        "abs_return_acf_1": 0.40617908954627174,
        "abs_return_acf_5": 0.3323724309441006,
        "abs_return_acf_20": 0.3287041299739542,
        "quantile_01": -0.06972275985626246,
        "quantile_99": 0.051407116841059294,
        "hill_tail_index": 2.7566179978153573
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019080657096006537,
        "excess_kurtosis": 3.5167763199988817,
        "return_acf_1": -0.15004066231657812,
        "abs_return_acf_1": 0.27578840281773886,
        "abs_return_acf_5": 0.3320819033838399,
        "abs_return_acf_20": 0.3157568697202624,
        "quantile_01": -0.05084642672028658,
        "quantile_99": 0.05538794870406971,
        "hill_tail_index": 4.206449176357719
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01863807148618385,
        "excess_kurtosis": 7.6436584641449254,
        "return_acf_1": -0.1610855232579017,
        "abs_return_acf_1": 0.35361391373283274,
        "abs_return_acf_5": 0.3330889738437334,
        "abs_return_acf_20": 0.3030739707419739,
        "quantile_01": -0.058979986984976605,
        "quantile_99": 0.04697698482866513,
        "hill_tail_index": 2.897491690669571
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.019142596793610328,
        "excess_kurtosis": 10.78357873400131,
        "return_acf_1": -0.22040479032038907,
        "abs_return_acf_1": 0.36371039230198726,
        "abs_return_acf_5": 0.4061611343366988,
        "abs_return_acf_20": 0.2848163994907543,
        "quantile_01": -0.06217362510854553,
        "quantile_99": 0.048457558789170574,
        "hill_tail_index": 2.5399049903660424
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020463586078886507,
        "excess_kurtosis": 8.222435157082659,
        "return_acf_1": -0.17710818059130334,
        "abs_return_acf_1": 0.43499624060272785,
        "abs_return_acf_5": 0.3424071334954229,
        "abs_return_acf_20": 0.3672239972703529,
        "quantile_01": -0.07152696811863686,
        "quantile_99": 0.056326445116820625,
        "hill_tail_index": 3.970387252962714
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018466830290361606,
        "excess_kurtosis": 7.855696648773385,
        "return_acf_1": -0.14235805625065312,
        "abs_return_acf_1": 0.3693791898753073,
        "abs_return_acf_5": 0.3128128230535,
        "abs_return_acf_20": 0.26923936666747733,
        "quantile_01": -0.06063035820364363,
        "quantile_99": 0.05233027292280375,
        "hill_tail_index": 2.6260290195916403
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01816220555240494,
        "excess_kurtosis": 4.82334344562137,
        "return_acf_1": -0.13331558268786475,
        "abs_return_acf_1": 0.21235768323034176,
        "abs_return_acf_5": 0.22732728945855546,
        "abs_return_acf_20": 0.25704042003347527,
        "quantile_01": -0.058373137592258435,
        "quantile_99": 0.0462991919932022,
        "hill_tail_index": 3.297372319081826
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01927287336774462,
        "excess_kurtosis": 5.036744940634948,
        "return_acf_1": -0.15394607165192753,
        "abs_return_acf_1": 0.28906178776116787,
        "abs_return_acf_5": 0.2807819834121995,
        "abs_return_acf_20": 0.28376778090866145,
        "quantile_01": -0.05931637833559242,
        "quantile_99": 0.05423360055491491,
        "hill_tail_index": 3.6910614962659785
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018784343060585608,
        "excess_kurtosis": 5.416213112591734,
        "return_acf_1": -0.1857498240897631,
        "abs_return_acf_1": 0.3199370670815568,
        "abs_return_acf_5": 0.3095223679686898,
        "abs_return_acf_20": 0.30168021352715474,
        "quantile_01": -0.05975771464542572,
        "quantile_99": 0.05109544600481324,
        "hill_tail_index": 3.7479610192693276
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019480567060771503,
        "excess_kurtosis": 5.117797325309441,
        "return_acf_1": -0.15211659555951665,
        "abs_return_acf_1": 0.3510856752687924,
        "abs_return_acf_5": 0.36950663683299084,
        "abs_return_acf_20": 0.3770098841387637,
        "quantile_01": -0.05480876893692283,
        "quantile_99": 0.05801967108215165,
        "hill_tail_index": 4.302444302873903
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019902932707850485,
        "excess_kurtosis": 7.918715763291253,
        "return_acf_1": -0.1488093870049364,
        "abs_return_acf_1": 0.33699366683067655,
        "abs_return_acf_5": 0.3892659324719612,
        "abs_return_acf_20": 0.3527175857432002,
        "quantile_01": -0.07001927047597312,
        "quantile_99": 0.0582331249965393,
        "hill_tail_index": 4.11166930862632
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01832947493177718,
        "excess_kurtosis": 6.111845078877218,
        "return_acf_1": -0.1203144276068395,
        "abs_return_acf_1": 0.2390185471290231,
        "abs_return_acf_5": 0.24252925300882436,
        "abs_return_acf_20": 0.2516011552297569,
        "quantile_01": -0.058417862444011884,
        "quantile_99": 0.0525475619582082,
        "hill_tail_index": 3.682899666654417
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019849550093756642,
        "excess_kurtosis": 7.956991269473692,
        "return_acf_1": -0.22084256168188438,
        "abs_return_acf_1": 0.44686460904218706,
        "abs_return_acf_5": 0.3725939436992415,
        "abs_return_acf_20": 0.3627964319882269,
        "quantile_01": -0.06863175703813888,
        "quantile_99": 0.05878051335315852,
        "hill_tail_index": 3.5007585975970588
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019188161098364482,
        "excess_kurtosis": 10.497736488997761,
        "return_acf_1": -0.16636121120313258,
        "abs_return_acf_1": 0.35172337700040157,
        "abs_return_acf_5": 0.28480260904975413,
        "abs_return_acf_20": 0.31021071060527733,
        "quantile_01": -0.05974789845770453,
        "quantile_99": 0.05527680674637492,
        "hill_tail_index": 3.5696695463057506
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01969585535277471,
        "excess_kurtosis": 9.211830282089696,
        "return_acf_1": -0.2147996980520924,
        "abs_return_acf_1": 0.3602728163543245,
        "abs_return_acf_5": 0.35585109504911233,
        "abs_return_acf_20": 0.2918311341346938,
        "quantile_01": -0.05556151308461485,
        "quantile_99": 0.0530475716411338,
        "hill_tail_index": 3.079883866321217
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020314855117159535,
        "excess_kurtosis": 9.436367081357227,
        "return_acf_1": -0.18127969366806754,
        "abs_return_acf_1": 0.39906846047637246,
        "abs_return_acf_5": 0.3796251117047807,
        "abs_return_acf_20": 0.3363234410398829,
        "quantile_01": -0.06652640767871512,
        "quantile_99": 0.051797842270691466,
        "hill_tail_index": 3.086669087807148
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01922344626868842,
        "excess_kurtosis": 8.366264092954335,
        "return_acf_1": -0.15736300873263281,
        "abs_return_acf_1": 0.3630400402757384,
        "abs_return_acf_5": 0.373493621306917,
        "abs_return_acf_20": 0.2901777048678509,
        "quantile_01": -0.059465125385947615,
        "quantile_99": 0.05219645911932985,
        "hill_tail_index": 3.840994302492912
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018260303443492745,
        "excess_kurtosis": 5.400409496644718,
        "return_acf_1": -0.12759655673490083,
        "abs_return_acf_1": 0.22821083463521757,
        "abs_return_acf_5": 0.2853046201027429,
        "abs_return_acf_20": 0.22664324366137106,
        "quantile_01": -0.0604625583830798,
        "quantile_99": 0.04892582556656406,
        "hill_tail_index": 3.495578696614433
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019717672272788457,
        "excess_kurtosis": 10.119411815313748,
        "return_acf_1": -0.16459735528908798,
        "abs_return_acf_1": 0.3724315536275547,
        "abs_return_acf_5": 0.36429514100158467,
        "abs_return_acf_20": 0.2958293789838424,
        "quantile_01": -0.060967094437613244,
        "quantile_99": 0.049758322775084185,
        "hill_tail_index": 3.234887896888022
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019833049909035123,
        "excess_kurtosis": 10.255562118370001,
        "return_acf_1": -0.1859087620556422,
        "abs_return_acf_1": 0.3748942531243581,
        "abs_return_acf_5": 0.3739699845514367,
        "abs_return_acf_20": 0.3539848691517237,
        "quantile_01": -0.06864967160183008,
        "quantile_99": 0.055703702551141765,
        "hill_tail_index": 2.978713732069789
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01932403590868942,
        "excess_kurtosis": 9.569598163094547,
        "return_acf_1": -0.163922417179668,
        "abs_return_acf_1": 0.3574104617273269,
        "abs_return_acf_5": 0.368589334874632,
        "abs_return_acf_20": 0.3039743090032027,
        "quantile_01": -0.05973912802816007,
        "quantile_99": 0.04704945446815813,
        "hill_tail_index": 3.627497335625278
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.02100567478265702,
        "excess_kurtosis": 10.012259829571715,
        "return_acf_1": -0.2304266131324572,
        "abs_return_acf_1": 0.4282061066309731,
        "abs_return_acf_5": 0.40526140939117306,
        "abs_return_acf_20": 0.3125848479251262,
        "quantile_01": -0.07773515038234592,
        "quantile_99": 0.0588004773680247,
        "hill_tail_index": 3.2325008966698916
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017736452832163588,
        "excess_kurtosis": 5.474826606421171,
        "return_acf_1": -0.16269741061619242,
        "abs_return_acf_1": 0.2884071397063833,
        "abs_return_acf_5": 0.2739867698282471,
        "abs_return_acf_20": 0.2665029958210908,
        "quantile_01": -0.05298722878752048,
        "quantile_99": 0.047062941314811715,
        "hill_tail_index": 3.632086496724507
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01928292279316681,
        "excess_kurtosis": 8.067399627673788,
        "return_acf_1": -0.144778305650768,
        "abs_return_acf_1": 0.3585278590574867,
        "abs_return_acf_5": 0.3203950068454302,
        "abs_return_acf_20": 0.33593204416198064,
        "quantile_01": -0.056037520126885086,
        "quantile_99": 0.06080446892416286,
        "hill_tail_index": 3.3865122578694087
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01855696006291367,
        "excess_kurtosis": 7.299959940144275,
        "return_acf_1": -0.1876562715787966,
        "abs_return_acf_1": 0.3797512061713035,
        "abs_return_acf_5": 0.339633298950162,
        "abs_return_acf_20": 0.32380052590366115,
        "quantile_01": -0.0676537340723642,
        "quantile_99": 0.04461679000050691,
        "hill_tail_index": 3.2717321547896225
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01885250074846599,
        "excess_kurtosis": 8.58847714490302,
        "return_acf_1": -0.16806999694697916,
        "abs_return_acf_1": 0.3541493485026735,
        "abs_return_acf_5": 0.3090001886082886,
        "abs_return_acf_20": 0.3112873195488723,
        "quantile_01": -0.06218034201420103,
        "quantile_99": 0.04725623625251698,
        "hill_tail_index": 2.652398546625734
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.021353006920965718,
        "excess_kurtosis": 10.903710580715074,
        "return_acf_1": -0.12467810436754327,
        "abs_return_acf_1": 0.3942846115110403,
        "abs_return_acf_5": 0.3633666830286841,
        "abs_return_acf_20": 0.3107146556924586,
        "quantile_01": -0.08170120550773631,
        "quantile_99": 0.06049153920155432,
        "hill_tail_index": 2.8367864877734514
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.020968630098883466,
        "excess_kurtosis": 9.181500891411455,
        "return_acf_1": -0.18361957618922925,
        "abs_return_acf_1": 0.4186091190267558,
        "abs_return_acf_5": 0.37446876679474445,
        "abs_return_acf_20": 0.4009056549176724,
        "quantile_01": -0.06881264241057174,
        "quantile_99": 0.06302425404852793,
        "hill_tail_index": 3.892694068996552
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
