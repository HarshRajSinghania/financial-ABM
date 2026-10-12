# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27166
Run ID: `995def84094ade0b513b7c231eb8a2d2085fed3e5b6bc87a280cd2143ec8a76a`
Result fingerprint: `cf34ad60f420e673ded54323fad67e0ed20a12e206dd931bd90f6e5122734d3c`

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
    "equal_weight_sd": -0.7552142857142825,
    "equal_weight_raw": -11.328214285714237,
    "fixed_start_cap_weight_sd": -0.7527762907676399,
    "fixed_start_cap_weight_raw": -11.291644361514598,
    "end_cap_weight_sd": -0.7521030701263257,
    "end_cap_weight_raw": -11.281546051894885
  },
  "full_period_change": {
    "equal_weight_sd": -1.1382380952380904,
    "equal_weight_raw": -17.073571428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0631620370370325,
    "inflation_mean_sd": 0.5282635582010583
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.19716666666666988,
    "equal_weight_raw": 2.9575000000000484,
    "fixed_start_cap_weight_sd": 0.19960466161331267,
    "fixed_start_cap_weight_raw": 2.99406992419969,
    "end_cap_weight_sd": 0.20027788225462653,
    "end_cap_weight_raw": 3.0041682338193985
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.679880952380949,
      "change_raw": -10.198214285714236,
      "decay_adjusted_gain_sd": 0.2725000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7598809523809491,
      "change_raw": -11.398214285714236,
      "decay_adjusted_gain_sd": 0.1925000000000033
    },
    "small": {
      "count": 18,
      "change_sd": -0.7654365079365046,
      "change_raw": -11.48154761904757,
      "decay_adjusted_gain_sd": 0.1869444444444476
    },
    "large_minus_small_sd": 0.0855555555555556,
    "large_minus_small_raw": 1.283333333333334
  },
  "inflation": {
    "initial_mean_sd": 0.25775,
    "final_mean_sd": 0.5306666666666667,
    "mean_sd": 0.41693921731890093,
    "mean_absolute_raw_gap": 6.254088259783514,
    "final_absolute_raw_gap": 7.960000000000003,
    "mean_range_fraction": 0.06254088259783513
  },
  "impact": {
    "initial_share": 0.20666666666666667,
    "final_share": 0.28,
    "initial_wealth_share": 0.1846248760948827,
    "final_wealth_share": 0.24545724128543775
  },
  "pricing_slope": {
    "mean": -0.003879916610630133,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.02747745747896141,
    "real_improvement_cost": 0.0199895835392616,
    "washing_cost": 0.007487873939699816,
    "fine_transfer": 0.008570498995104255,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.03604795647406567,
    "resource_cost_fraction_initial_cap": 0.0009159152492987135,
    "private_net_outflow_fraction_initial_cap": 0.0012015985491355221,
    "fine_transfer_fraction_initial_cap": 0.0002856832998368085,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.008221094231771812,
    "unapplied_final_day_resource_cost": 0.004084350694292367
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 215.26736978954543,
    "beneficial_raw_gain_per_resource_cost": 3229.0105468431816,
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
    "accrued_cost": 2.993030311105281,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.016839834914804064,
    "accrued_cost_fraction_initial_cap": 0.0997676770368427,
    "mean_contract_rate": 0.04119865136065723,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 2.1144286906830788e-15,
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
      "minimum": -0.24405606912591196,
      "maximum": -0.05157621620713242,
      "mean": -0.1421760662561839,
      "median": -0.13980400446725957,
      "quantile_05": -0.1947381567889589,
      "quantile_95": -0.09372618443400456
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
      "minimum": 0.40983082532284654,
      "maximum": 0.8451613377767754,
      "mean": 0.6615803983240802,
      "median": 0.6766168321381735,
      "quantile_05": 0.4931276146310756,
      "quantile_95": 0.7805771148461061
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
        "daily_volatility": 0.022040155929012827,
        "excess_kurtosis": 11.310358350199701,
        "return_acf_1": -0.17843813768926434,
        "abs_return_acf_1": 0.5318137613630526,
        "abs_return_acf_5": 0.4879290226854574,
        "abs_return_acf_20": 0.4002167207532018,
        "quantile_01": -0.08099547827510215,
        "quantile_99": 0.06007735563180936,
        "hill_tail_index": 2.5688750926826884
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02267951633150858,
        "excess_kurtosis": 14.676894429130527,
        "return_acf_1": -0.10322133804687149,
        "abs_return_acf_1": 0.4306022409881194,
        "abs_return_acf_5": 0.44124103418109906,
        "abs_return_acf_20": 0.3382085199014755,
        "quantile_01": -0.08031711477644655,
        "quantile_99": 0.06165092852500659,
        "hill_tail_index": 2.5602406565076934
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.021351017742437573,
        "excess_kurtosis": 5.7027583534487665,
        "return_acf_1": -0.13560277342513713,
        "abs_return_acf_1": 0.34200728245357515,
        "abs_return_acf_5": 0.3328923555867956,
        "abs_return_acf_20": 0.27308727363552404,
        "quantile_01": -0.07122562755166421,
        "quantile_99": 0.06453562745846501,
        "hill_tail_index": 3.9975409728919504
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02453105819110936,
        "excess_kurtosis": 11.081119859272476,
        "return_acf_1": -0.24405606912591196,
        "abs_return_acf_1": 0.5166786424149791,
        "abs_return_acf_5": 0.46072370590558764,
        "abs_return_acf_20": 0.4243185946627987,
        "quantile_01": -0.08823283103092491,
        "quantile_99": 0.08291084025346876,
        "hill_tail_index": 3.725927323813971
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.024276544325727487,
        "excess_kurtosis": 10.944679618135563,
        "return_acf_1": -0.18043896068623325,
        "abs_return_acf_1": 0.4824944691746403,
        "abs_return_acf_5": 0.46563946499519193,
        "abs_return_acf_20": 0.3740051854278708,
        "quantile_01": -0.0941291942575987,
        "quantile_99": 0.06301130077050736,
        "hill_tail_index": 3.4381322108673396
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021834375109125986,
        "excess_kurtosis": 12.703391891785941,
        "return_acf_1": -0.18072890221887536,
        "abs_return_acf_1": 0.5303189019513163,
        "abs_return_acf_5": 0.45733843714859845,
        "abs_return_acf_20": 0.3033825674270476,
        "quantile_01": -0.07448505957624328,
        "quantile_99": 0.057793121816239114,
        "hill_tail_index": 2.619868247310504
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020152689564530164,
        "excess_kurtosis": 5.675770594687998,
        "return_acf_1": -0.144802803906152,
        "abs_return_acf_1": 0.31833021497201774,
        "abs_return_acf_5": 0.30417474454099475,
        "abs_return_acf_20": 0.2307833672756307,
        "quantile_01": -0.061435630033750376,
        "quantile_99": 0.058576299953545054,
        "hill_tail_index": 4.74110515694362
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.02535037700910062,
        "excess_kurtosis": 15.31216259573322,
        "return_acf_1": -0.12683442691659866,
        "abs_return_acf_1": 0.5171603711840207,
        "abs_return_acf_5": 0.47908860924324265,
        "abs_return_acf_20": 0.4005523870418109,
        "quantile_01": -0.10260444896174302,
        "quantile_99": 0.06716410632698809,
        "hill_tail_index": 2.9249282880192466
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0181275658170709,
        "excess_kurtosis": 4.655656832171753,
        "return_acf_1": -0.20377353043257684,
        "abs_return_acf_1": 0.3116214158353443,
        "abs_return_acf_5": 0.22878276414235724,
        "abs_return_acf_20": 0.220142814809879,
        "quantile_01": -0.05245970736524989,
        "quantile_99": 0.05373825508618635,
        "hill_tail_index": 4.306275055905229
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.021490540591697437,
        "excess_kurtosis": 7.855012566381049,
        "return_acf_1": -0.127646409159762,
        "abs_return_acf_1": 0.34709999706893135,
        "abs_return_acf_5": 0.3944361312548307,
        "abs_return_acf_20": 0.32877488479574846,
        "quantile_01": -0.06643477258219097,
        "quantile_99": 0.05501455658100611,
        "hill_tail_index": 3.109828660537224
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.02557150415135121,
        "excess_kurtosis": 14.491082243274487,
        "return_acf_1": -0.1435916711893667,
        "abs_return_acf_1": 0.5897933764832876,
        "abs_return_acf_5": 0.5252434596856349,
        "abs_return_acf_20": 0.39623594780994914,
        "quantile_01": -0.09265548858005514,
        "quantile_99": 0.07337875589463023,
        "hill_tail_index": 2.545446646691927
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.020972150075324564,
        "excess_kurtosis": 12.241990627175928,
        "return_acf_1": -0.09896042684152008,
        "abs_return_acf_1": 0.40336401952128975,
        "abs_return_acf_5": 0.390824209287655,
        "abs_return_acf_20": 0.214355585994422,
        "quantile_01": -0.07351249401585093,
        "quantile_99": 0.05960761243377204,
        "hill_tail_index": 2.670083572653009
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.023392400381510324,
        "excess_kurtosis": 6.410795104485162,
        "return_acf_1": -0.13601633774515245,
        "abs_return_acf_1": 0.41963711425342154,
        "abs_return_acf_5": 0.4306609815299794,
        "abs_return_acf_20": 0.38190232242667976,
        "quantile_01": -0.09037821924426184,
        "quantile_99": 0.06761751176955161,
        "hill_tail_index": 3.5378444757278538
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022743280821492077,
        "excess_kurtosis": 8.533273720558332,
        "return_acf_1": -0.13029620128284167,
        "abs_return_acf_1": 0.42647984618608303,
        "abs_return_acf_5": 0.37283162617441973,
        "abs_return_acf_20": 0.3988790061274088,
        "quantile_01": -0.07551684625604381,
        "quantile_99": 0.06537155192233121,
        "hill_tail_index": 3.3635632117607916
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020505857018543464,
        "excess_kurtosis": 9.463956424922584,
        "return_acf_1": -0.12421333546560169,
        "abs_return_acf_1": 0.3476914350389851,
        "abs_return_acf_5": 0.37106036563835204,
        "abs_return_acf_20": 0.2579301589035335,
        "quantile_01": -0.07179188067351228,
        "quantile_99": 0.060118981761528204,
        "hill_tail_index": 3.0770777680181425
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.021201609787903593,
        "excess_kurtosis": 11.03048650141665,
        "return_acf_1": -0.10317035016377755,
        "abs_return_acf_1": 0.45969351279077153,
        "abs_return_acf_5": 0.3909285250519632,
        "abs_return_acf_20": 0.32966693003332626,
        "quantile_01": -0.07494812794579774,
        "quantile_99": 0.05114132464598798,
        "hill_tail_index": 2.675106107358751
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.023215841730369686,
        "excess_kurtosis": 9.392809852070783,
        "return_acf_1": -0.174267332788093,
        "abs_return_acf_1": 0.437238294959574,
        "abs_return_acf_5": 0.39197938475054767,
        "abs_return_acf_20": 0.3935272719955893,
        "quantile_01": -0.08562650726787129,
        "quantile_99": 0.06518369016129676,
        "hill_tail_index": 2.3786418312445012
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.024011283173728953,
        "excess_kurtosis": 8.283198961658996,
        "return_acf_1": -0.16056158102484783,
        "abs_return_acf_1": 0.4616919490079544,
        "abs_return_acf_5": 0.4063203675380193,
        "abs_return_acf_20": 0.4117216593585813,
        "quantile_01": -0.08436010507402412,
        "quantile_99": 0.07054528444609988,
        "hill_tail_index": 4.016623067470608
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.020595549019969555,
        "excess_kurtosis": 7.948334649617401,
        "return_acf_1": -0.1341507897822761,
        "abs_return_acf_1": 0.4667370897492003,
        "abs_return_acf_5": 0.41844714959291374,
        "abs_return_acf_20": 0.33342625331101894,
        "quantile_01": -0.06769863599614491,
        "quantile_99": 0.059515657879339226,
        "hill_tail_index": 3.3471891919860246
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.020209610909822703,
        "excess_kurtosis": 6.693013907419848,
        "return_acf_1": -0.10545577998324952,
        "abs_return_acf_1": 0.36960814273223563,
        "abs_return_acf_5": 0.335989150210856,
        "abs_return_acf_20": 0.29789303061945493,
        "quantile_01": -0.06992736876772553,
        "quantile_99": 0.05889431353379775,
        "hill_tail_index": 3.3569007415991767
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.02207336540874855,
        "excess_kurtosis": 6.83681039747162,
        "return_acf_1": -0.1493620127058831,
        "abs_return_acf_1": 0.4224825584950813,
        "abs_return_acf_5": 0.3586792114125679,
        "abs_return_acf_20": 0.4085452456965792,
        "quantile_01": -0.06906895022682623,
        "quantile_99": 0.06555887916080246,
        "hill_tail_index": 3.739468678469339
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.022500128763294946,
        "excess_kurtosis": 12.675549682149757,
        "return_acf_1": -0.10321593657081284,
        "abs_return_acf_1": 0.5173826734314384,
        "abs_return_acf_5": 0.41778895852435577,
        "abs_return_acf_20": 0.4145632673270071,
        "quantile_01": -0.08813361221628574,
        "quantile_99": 0.0555893962074783,
        "hill_tail_index": 2.4828657147499746
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019693740621613207,
        "excess_kurtosis": 7.6545136879604225,
        "return_acf_1": -0.1675118380487574,
        "abs_return_acf_1": 0.41808241891315057,
        "abs_return_acf_5": 0.32154283335933376,
        "abs_return_acf_20": 0.2879662805289,
        "quantile_01": -0.06374314898319669,
        "quantile_99": 0.05432732962899747,
        "hill_tail_index": 3.691364851464923
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022035615302291853,
        "excess_kurtosis": 10.962966260865615,
        "return_acf_1": -0.15051229102417663,
        "abs_return_acf_1": 0.4007534800756072,
        "abs_return_acf_5": 0.37399094545069916,
        "abs_return_acf_20": 0.33956063863338065,
        "quantile_01": -0.06866723628063233,
        "quantile_99": 0.061509301569067455,
        "hill_tail_index": 2.7620343353363745
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020442770814199856,
        "excess_kurtosis": 8.325487870268947,
        "return_acf_1": -0.16187051937997712,
        "abs_return_acf_1": 0.3965342093230749,
        "abs_return_acf_5": 0.3530149363228407,
        "abs_return_acf_20": 0.3236391736614735,
        "quantile_01": -0.08249808570996775,
        "quantile_99": 0.05796226903653982,
        "hill_tail_index": 2.678012819478138
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02141571065928068,
        "excess_kurtosis": 10.956734966901895,
        "return_acf_1": -0.12328241227502174,
        "abs_return_acf_1": 0.4107041475779085,
        "abs_return_acf_5": 0.36599337087344347,
        "abs_return_acf_20": 0.3284316531913379,
        "quantile_01": -0.07874931406988364,
        "quantile_99": 0.06324904838470902,
        "hill_tail_index": 2.6205817717432742
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02291097637034791,
        "excess_kurtosis": 20.2688924027306,
        "return_acf_1": -0.08944362246421908,
        "abs_return_acf_1": 0.4553733309511033,
        "abs_return_acf_5": 0.386756470810083,
        "abs_return_acf_20": 0.35338542565840997,
        "quantile_01": -0.07016711023084846,
        "quantile_99": 0.053368002296125185,
        "hill_tail_index": 1.9724612914885338
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02385728855023197,
        "excess_kurtosis": 8.811448529655284,
        "return_acf_1": -0.18369492233564808,
        "abs_return_acf_1": 0.3843550222251827,
        "abs_return_acf_5": 0.3799038229175966,
        "abs_return_acf_20": 0.36279295096189823,
        "quantile_01": -0.09742557056133944,
        "quantile_99": 0.06960242238144927,
        "hill_tail_index": 3.3138732090116267
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.023106701898104175,
        "excess_kurtosis": 13.709686028664755,
        "return_acf_1": -0.05157621620713242,
        "abs_return_acf_1": 0.4598419765679086,
        "abs_return_acf_5": 0.4945449577343633,
        "abs_return_acf_20": 0.3423184647639052,
        "quantile_01": -0.07907946176775879,
        "quantile_99": 0.06699396681514413,
        "hill_tail_index": 2.873849101076425
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.023357878131246488,
        "excess_kurtosis": 8.250344828209972,
        "return_acf_1": -0.14858505879977985,
        "abs_return_acf_1": 0.41967383761997085,
        "abs_return_acf_5": 0.43705175247054856,
        "abs_return_acf_20": 0.3949781405665645,
        "quantile_01": -0.0830975669393962,
        "quantile_99": 0.06602427795306184,
        "hill_tail_index": 2.972384720327462
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
