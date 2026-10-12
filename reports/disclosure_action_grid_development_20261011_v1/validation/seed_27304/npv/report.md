# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27304
Run ID: `4c0577961bd57c4a674b376316a7bbf9746f8c84abffe04bcd3ffaa9ba835dc2`
Result fingerprint: `4070140f71e5e569b48dab4b2050d0c6ece017a37b55694c4c8f586641e3b15d`

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
    "equal_weight_sd": -0.7537618415216826,
    "equal_weight_raw": -11.306427622825236,
    "fixed_start_cap_weight_sd": -0.7325526614723183,
    "fixed_start_cap_weight_raw": -10.988289922084775,
    "end_cap_weight_sd": -0.7605370944977339,
    "end_cap_weight_raw": -11.40805641746601
  },
  "full_period_change": {
    "equal_weight_sd": -1.2026184439902126,
    "equal_weight_raw": -18.03927665985319
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1323411704512334,
    "inflation_mean_sd": 0.0
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19861911085926992,
    "equal_weight_raw": 2.979286662889048,
    "fixed_start_cap_weight_sd": 0.2198282909086339,
    "fixed_start_cap_weight_raw": 3.297424363629509,
    "end_cap_weight_sd": 0.1918438578832183,
    "end_cap_weight_raw": 2.8776578682482747
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8208858139952205,
      "change_raw": -12.313287209928308,
      "decay_adjusted_gain_sd": 0.13149513838573182
    },
    "mid": {
      "count": 9,
      "change_sd": -0.632037211040309,
      "change_raw": -9.480558165604634,
      "decay_adjusted_gain_sd": 0.32034374134064336
    },
    "small": {
      "count": 18,
      "change_sd": -0.8034368280167796,
      "change_raw": -12.051552420251694,
      "decay_adjusted_gain_sd": 0.14894412436417284
    },
    "large_minus_small_sd": -0.017448985978440912,
    "large_minus_small_raw": -0.2617347896766137
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
    "initial_share": 0.37333333333333335,
    "final_share": 0.38666666666666666,
    "initial_wealth_share": 0.32631240549545737,
    "final_wealth_share": 0.3162383574577016
  },
  "pricing_slope": {
    "mean": -0.0010334846319875655,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.0007929815475616216,
    "real_improvement_cost": 0.0007929815475616216,
    "washing_cost": 0.0,
    "fine_transfer": 0.0,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.0007929815475616216,
    "resource_cost_fraction_initial_cap": 2.643271825205405e-05,
    "private_net_outflow_fraction_initial_cap": 2.643271825205405e-05,
    "fine_transfer_fraction_initial_cap": 0.0,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 4.284836201627077e-05,
    "unapplied_final_day_resource_cost": 4.639565969694042e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 7514.138688473156,
    "beneficial_raw_gain_per_resource_cost": 112712.08032709734,
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
    "accrued_cost": 3.308806487692916,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": -0.3326160115024392,
    "accrued_cost_fraction_initial_cap": 0.11029354958976387,
    "mean_contract_rate": 0.04615601085955615,
    "maximum_ledger_error": 1.0842021724855044e-19
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
    "price_cap_hits": 7,
    "maximum_relative_cash_error": 1.1682841138646767e-15,
    "maximum_absolute_share_error": 2.220446049250313e-15,
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
      "minimum": -0.23837052319858165,
      "maximum": -0.07942422572608207,
      "mean": -0.14218854906315206,
      "median": -0.1391099315104284,
      "quantile_05": -0.20234937865054634,
      "quantile_95": -0.09368328952367833
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
      "minimum": 0.549371307804725,
      "maximum": 0.8365886912431914,
      "mean": 0.7278161386097415,
      "median": 0.7408931344622708,
      "quantile_05": 0.5995208092616976,
      "quantile_95": 0.8164759480205419
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
        "daily_volatility": 0.02005444628212438,
        "excess_kurtosis": 30.271560896929238,
        "return_acf_1": -0.14076982706536428,
        "abs_return_acf_1": 0.30193379126994097,
        "abs_return_acf_5": 0.2959683930605808,
        "abs_return_acf_20": 0.2841283822924417,
        "quantile_01": -0.0700799093161002,
        "quantile_99": 0.048102392089882096,
        "hill_tail_index": 1.906836389374672
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019582917447177817,
        "excess_kurtosis": 21.521645126915608,
        "return_acf_1": -0.11992795419242681,
        "abs_return_acf_1": 0.36119622009061053,
        "abs_return_acf_5": 0.2992943172331007,
        "abs_return_acf_20": 0.285508086855079,
        "quantile_01": -0.06903674635467932,
        "quantile_99": 0.0527845153641188,
        "hill_tail_index": 2.6384899350138804
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.017552859217340195,
        "excess_kurtosis": 17.525294401298705,
        "return_acf_1": -0.23837052319858165,
        "abs_return_acf_1": 0.2943590641421877,
        "abs_return_acf_5": 0.25468628996406484,
        "abs_return_acf_20": 0.29507284469893413,
        "quantile_01": -0.051343839191679154,
        "quantile_99": 0.046279106430163586,
        "hill_tail_index": 1.8000755230307182
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021825388305202576,
        "excess_kurtosis": 27.48154083968966,
        "return_acf_1": -0.1287309043436281,
        "abs_return_acf_1": 0.3911931400351121,
        "abs_return_acf_5": 0.319965459049574,
        "abs_return_acf_20": 0.28726379487398923,
        "quantile_01": -0.07040058036469875,
        "quantile_99": 0.05872254093524032,
        "hill_tail_index": 2.0318195729334745
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02170597930697367,
        "excess_kurtosis": 32.757046975731896,
        "return_acf_1": -0.1519264152984739,
        "abs_return_acf_1": 0.4942800333255197,
        "abs_return_acf_5": 0.3899002584234218,
        "abs_return_acf_20": 0.3139552960875716,
        "quantile_01": -0.07894474492900658,
        "quantile_99": 0.048124148464100576,
        "hill_tail_index": 1.636917493635167
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02071980415277579,
        "excess_kurtosis": 26.74796852555314,
        "return_acf_1": -0.14858858050310184,
        "abs_return_acf_1": 0.3609557512298065,
        "abs_return_acf_5": 0.26609260156520104,
        "abs_return_acf_20": 0.3127746074382307,
        "quantile_01": -0.07003609659459074,
        "quantile_99": 0.05358544748062042,
        "hill_tail_index": 2.1584783263833187
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018431416139298867,
        "excess_kurtosis": 17.61442712002415,
        "return_acf_1": -0.17762117827920923,
        "abs_return_acf_1": 0.4312596417354514,
        "abs_return_acf_5": 0.3383207546685554,
        "abs_return_acf_20": 0.3370278588093535,
        "quantile_01": -0.04664901125707355,
        "quantile_99": 0.05281442044789185,
        "hill_tail_index": 1.8620192880130377
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021365610246128597,
        "excess_kurtosis": 13.092791036110611,
        "return_acf_1": -0.15353210416225238,
        "abs_return_acf_1": 0.35781807578375274,
        "abs_return_acf_5": 0.19970064431709644,
        "abs_return_acf_20": 0.27832762184248855,
        "quantile_01": -0.06744279130665246,
        "quantile_99": 0.060205351859827526,
        "hill_tail_index": 2.92480797374871
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019951683414067212,
        "excess_kurtosis": 25.58970476507508,
        "return_acf_1": -0.11846485655087607,
        "abs_return_acf_1": 0.3446742729894176,
        "abs_return_acf_5": 0.29907177842527305,
        "abs_return_acf_20": 0.277334496270659,
        "quantile_01": -0.07591318609634227,
        "quantile_99": 0.05065498623378115,
        "hill_tail_index": 2.2345813488618393
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02089656353560984,
        "excess_kurtosis": 29.930200806745376,
        "return_acf_1": -0.13385948333580872,
        "abs_return_acf_1": 0.4362474754632786,
        "abs_return_acf_5": 0.36556171954229194,
        "abs_return_acf_20": 0.31938919778611635,
        "quantile_01": -0.07482678180215233,
        "quantile_99": 0.04598053205017783,
        "hill_tail_index": 2.0252947431097903
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02023106231393395,
        "excess_kurtosis": 23.500031113620928,
        "return_acf_1": -0.13164935637135447,
        "abs_return_acf_1": 0.38541227471415873,
        "abs_return_acf_5": 0.3905305772428027,
        "abs_return_acf_20": 0.31016659160851034,
        "quantile_01": -0.06731767923028377,
        "quantile_99": 0.04871953478450092,
        "hill_tail_index": 2.062357321046507
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.02031395809124071,
        "excess_kurtosis": 18.313108510877658,
        "return_acf_1": -0.15467952808728114,
        "abs_return_acf_1": 0.3770920013301999,
        "abs_return_acf_5": 0.3140361860775936,
        "abs_return_acf_20": 0.25966087257519754,
        "quantile_01": -0.06648383190822965,
        "quantile_99": 0.048207369318076974,
        "hill_tail_index": 2.3559420214813156
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.021643798072561695,
        "excess_kurtosis": 22.65586872870896,
        "return_acf_1": -0.1406022814208922,
        "abs_return_acf_1": 0.4095865683912109,
        "abs_return_acf_5": 0.4019896958529774,
        "abs_return_acf_20": 0.3909638504866232,
        "quantile_01": -0.08369601765662858,
        "quantile_99": 0.06631645864418198,
        "hill_tail_index": 2.3404159061425287
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021492455424735126,
        "excess_kurtosis": 19.604956764262173,
        "return_acf_1": -0.10749079590784957,
        "abs_return_acf_1": 0.438736338189517,
        "abs_return_acf_5": 0.4445202995281443,
        "abs_return_acf_20": 0.3500790334954901,
        "quantile_01": -0.06787161390307797,
        "quantile_99": 0.060912108790052336,
        "hill_tail_index": 2.2063275534196256
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.0202050983667266,
        "excess_kurtosis": 31.054570322554667,
        "return_acf_1": -0.12072922436450767,
        "abs_return_acf_1": 0.3360565131845888,
        "abs_return_acf_5": 0.3215921866891957,
        "abs_return_acf_20": 0.27720163981811585,
        "quantile_01": -0.06677063172278873,
        "quantile_99": 0.0510342401582945,
        "hill_tail_index": 2.3452436847236737
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02118553284474657,
        "excess_kurtosis": 23.007033642046803,
        "return_acf_1": -0.07942422572608207,
        "abs_return_acf_1": 0.2877702358741488,
        "abs_return_acf_5": 0.2251603783252123,
        "abs_return_acf_20": 0.28133246247293675,
        "quantile_01": -0.05890188595467869,
        "quantile_99": 0.05858407838291418,
        "hill_tail_index": 2.7605592066433515
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.02026055721146356,
        "excess_kurtosis": 27.49264027937316,
        "return_acf_1": -0.17716986335838775,
        "abs_return_acf_1": 0.3710912015979178,
        "abs_return_acf_5": 0.252963792464415,
        "abs_return_acf_20": 0.3314492520065775,
        "quantile_01": -0.06737942309307064,
        "quantile_99": 0.04788366038030562,
        "hill_tail_index": 2.0458418769708646
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019765908189006677,
        "excess_kurtosis": 27.27178153668341,
        "return_acf_1": -0.12568775952068986,
        "abs_return_acf_1": 0.3562427541997235,
        "abs_return_acf_5": 0.26377594416978045,
        "abs_return_acf_20": 0.32209181929656466,
        "quantile_01": -0.06636567310154806,
        "quantile_99": 0.05492314519503957,
        "hill_tail_index": 2.540648040053804
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020123854118319136,
        "excess_kurtosis": 9.413814253066239,
        "return_acf_1": -0.1437035957537566,
        "abs_return_acf_1": 0.3717072800896267,
        "abs_return_acf_5": 0.2831131679782628,
        "abs_return_acf_20": 0.2826364430191318,
        "quantile_01": -0.06354646350767551,
        "quantile_99": 0.0621782380104014,
        "hill_tail_index": 3.64858014990663
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021528775168683227,
        "excess_kurtosis": 29.00993908415129,
        "return_acf_1": -0.18495149253431276,
        "abs_return_acf_1": 0.3578291592409816,
        "abs_return_acf_5": 0.31263841747304855,
        "abs_return_acf_20": 0.320847429182832,
        "quantile_01": -0.08147542959468153,
        "quantile_99": 0.05356239158283424,
        "hill_tail_index": 2.057230148520888
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02103389398841171,
        "excess_kurtosis": 23.281899218810647,
        "return_acf_1": -0.12731980104900587,
        "abs_return_acf_1": 0.4409784425444424,
        "abs_return_acf_5": 0.2614047388619638,
        "abs_return_acf_20": 0.29295892230355675,
        "quantile_01": -0.06660764706739612,
        "quantile_99": 0.0537563907333932,
        "hill_tail_index": 2.2574193065468267
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022516998070241788,
        "excess_kurtosis": 28.560498715925945,
        "return_acf_1": -0.1376175815999646,
        "abs_return_acf_1": 0.4200982303424872,
        "abs_return_acf_5": 0.32064547552910394,
        "abs_return_acf_20": 0.38996362923766154,
        "quantile_01": -0.08150743679152636,
        "quantile_99": 0.056827346139878936,
        "hill_tail_index": 2.1970786073833457
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019813319588279955,
        "excess_kurtosis": 13.906260879848023,
        "return_acf_1": -0.14246591577827966,
        "abs_return_acf_1": 0.3537702817570065,
        "abs_return_acf_5": 0.25333290432282146,
        "abs_return_acf_20": 0.24363230339605393,
        "quantile_01": -0.05840697651022121,
        "quantile_99": 0.05959096224961921,
        "hill_tail_index": 3.4986649185396885
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018325109807846608,
        "excess_kurtosis": 22.786406548776664,
        "return_acf_1": -0.10865172407343376,
        "abs_return_acf_1": 0.2675150258726489,
        "abs_return_acf_5": 0.22255421281093388,
        "abs_return_acf_20": 0.21350581905930027,
        "quantile_01": -0.05183785569641946,
        "quantile_99": 0.05070016332837323,
        "hill_tail_index": 2.37382633780505
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019741128375949057,
        "excess_kurtosis": 10.99719362845803,
        "return_acf_1": -0.1473352821577525,
        "abs_return_acf_1": 0.27683750073435787,
        "abs_return_acf_5": 0.2464831192297916,
        "abs_return_acf_20": 0.2733017383901339,
        "quantile_01": -0.06268330662752733,
        "quantile_99": 0.058169446174298235,
        "hill_tail_index": 2.5390425107644212
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02021953960031273,
        "excess_kurtosis": 22.809801892073775,
        "return_acf_1": -0.12223076306718575,
        "abs_return_acf_1": 0.3602819160410458,
        "abs_return_acf_5": 0.3255439659642736,
        "abs_return_acf_20": 0.2896610930779035,
        "quantile_01": -0.06784537474790908,
        "quantile_99": 0.048326039982653696,
        "hill_tail_index": 1.8866001434145496
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.020197748584468756,
        "excess_kurtosis": 11.168016937642912,
        "return_acf_1": -0.21658401274564654,
        "abs_return_acf_1": 0.4152880600451003,
        "abs_return_acf_5": 0.28030265050770964,
        "abs_return_acf_20": 0.23621853756729133,
        "quantile_01": -0.06228078536404248,
        "quantile_99": 0.058748501422585496,
        "hill_tail_index": 2.9764434869936043
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02026854693487827,
        "excess_kurtosis": 23.98482128006569,
        "return_acf_1": -0.08238623884571991,
        "abs_return_acf_1": 0.3113590024367079,
        "abs_return_acf_5": 0.32273230972583467,
        "abs_return_acf_20": 0.319412807337136,
        "quantile_01": -0.06625483377268246,
        "quantile_99": 0.04725904931874021,
        "hill_tail_index": 1.9830085285627508
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023025964708297757,
        "excess_kurtosis": 28.222196533273383,
        "return_acf_1": -0.1781461420070019,
        "abs_return_acf_1": 0.44229508468614426,
        "abs_return_acf_5": 0.33120476028008666,
        "abs_return_acf_20": 0.38470076293589256,
        "quantile_01": -0.07635711069870163,
        "quantile_99": 0.05664172161832518,
        "hill_tail_index": 1.8258504404125968
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02082243896033285,
        "excess_kurtosis": 21.1844071116584,
        "return_acf_1": -0.12503906059573372,
        "abs_return_acf_1": 0.4397758560276177,
        "abs_return_acf_5": 0.29056810275964257,
        "abs_return_acf_20": 0.32120789587605497,
        "quantile_01": -0.06693352937008243,
        "quantile_99": 0.05477820729676222,
        "hill_tail_index": 2.1158271328606024
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
