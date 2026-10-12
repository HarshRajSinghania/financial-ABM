# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27305
Run ID: `c8e96bd9229712d2c0673dc40c6d37ad0719e07c6768a1662d4997c42f574ebc`
Result fingerprint: `46dc4df42a5ccbac3b0ba09d4345db0ada0f3ae5c664994885dcf0deaf9916dc`

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
    "equal_weight_sd": -0.8582976190476158,
    "equal_weight_raw": -12.874464285714234,
    "fixed_start_cap_weight_sd": -0.785755620825023,
    "fixed_start_cap_weight_raw": -11.786334312375345,
    "end_cap_weight_sd": -0.7889287768085375,
    "end_cap_weight_raw": -11.833931652128062
  },
  "full_period_change": {
    "equal_weight_sd": -1.3151547619047568,
    "equal_weight_raw": -19.72732142857135
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2269877645502598,
    "inflation_mean_sd": 0.2896451719576719
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.0940833333333366,
    "equal_weight_raw": 1.411250000000049,
    "fixed_start_cap_weight_sd": 0.16662533155592946,
    "fixed_start_cap_weight_raw": 2.499379973338942,
    "end_cap_weight_sd": 0.16345217557241498,
    "end_cap_weight_raw": 2.4517826335862245
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6582142857142822,
      "change_raw": -9.873214285714234,
      "decay_adjusted_gain_sd": 0.2941666666666701
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8146031746031714,
      "change_raw": -12.219047619047572,
      "decay_adjusted_gain_sd": 0.13777777777778102
    },
    "small": {
      "count": 18,
      "change_sd": -0.9134920634920601,
      "change_raw": -13.702380952380903,
      "decay_adjusted_gain_sd": 0.038888888888892116
    },
    "large_minus_small_sd": 0.25527777777777794,
    "large_minus_small_raw": 3.8291666666666693
  },
  "inflation": {
    "initial_mean_sd": 0.19291666666666663,
    "final_mean_sd": 0.2991666666666667,
    "mean_sd": 0.2473279211767971,
    "mean_absolute_raw_gap": 3.709918817651957,
    "final_absolute_raw_gap": 4.487499999999999,
    "mean_range_fraction": 0.03709918817651957
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.14,
    "initial_wealth_share": 0.15805261391423606,
    "final_wealth_share": 0.12277824249364612
  },
  "pricing_slope": {
    "mean": -0.001986538779338668,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.002245276850943287,
    "real_improvement_cost": 0.0005957160168284701,
    "washing_cost": 0.0016495608341148167,
    "fine_transfer": 0.00315444433289278,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.005399721183836067,
    "resource_cost_fraction_initial_cap": 7.484256169810955e-05,
    "private_net_outflow_fraction_initial_cap": 0.00017999070612786884,
    "fine_transfer_fraction_initial_cap": 0.00010514814442975931,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00012214452871734928,
    "unapplied_final_day_resource_cost": 3.832388611149015e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 1257.0832852146086,
    "beneficial_raw_gain_per_resource_cost": 18856.24927821913,
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
    "fixed_exposure": 15.000000000000004,
    "accrued_cost": 2.9401530069173836,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": 0.03603746927309399,
    "accrued_cost_fraction_initial_cap": 0.09800510023057943,
    "mean_contract_rate": 0.04091549838452388,
    "maximum_ledger_error": 7.792703114739563e-20
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
    "price_cap_hits": 2,
    "maximum_relative_cash_error": 1.3865313487460798e-15,
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
      "minimum": -0.25426037152753744,
      "maximum": -0.010265817490789033,
      "mean": -0.12683185069751407,
      "median": -0.12325771325433085,
      "quantile_05": -0.22159506351353703,
      "quantile_95": -0.02831302815457217
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
      "minimum": 0.2827475411249222,
      "maximum": 0.8033961599045998,
      "mean": 0.500184041478772,
      "median": 0.46622754467003,
      "quantile_05": 0.32212795334551453,
      "quantile_95": 0.7476278355706645
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
        "daily_volatility": 0.01907355172502539,
        "excess_kurtosis": 5.944414379745998,
        "return_acf_1": -0.19702027945535744,
        "abs_return_acf_1": 0.3187045075016871,
        "abs_return_acf_5": 0.27828661428107077,
        "abs_return_acf_20": 0.2453937380976233,
        "quantile_01": -0.06191951563316306,
        "quantile_99": 0.04543095994319451,
        "hill_tail_index": 3.4145127526358294
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017122756689969917,
        "excess_kurtosis": 2.5021152109065703,
        "return_acf_1": -0.20161969061280188,
        "abs_return_acf_1": 0.31152360923889855,
        "abs_return_acf_5": 0.264247875190184,
        "abs_return_acf_20": 0.24174971153403355,
        "quantile_01": -0.048732378207222725,
        "quantile_99": 0.05126982142765214,
        "hill_tail_index": 4.946136988104245
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016981278294538438,
        "excess_kurtosis": 4.714024693613104,
        "return_acf_1": -0.25426037152753744,
        "abs_return_acf_1": 0.30587198626169976,
        "abs_return_acf_5": 0.24215607591557659,
        "abs_return_acf_20": 0.2458356480945814,
        "quantile_01": -0.045429247993123395,
        "quantile_99": 0.04651510428656714,
        "hill_tail_index": 3.6161029569674925
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019857209390131438,
        "excess_kurtosis": 11.425075596205758,
        "return_acf_1": -0.0778396047586854,
        "abs_return_acf_1": 0.34875054953030243,
        "abs_return_acf_5": 0.345875945266678,
        "abs_return_acf_20": 0.2577908181716796,
        "quantile_01": -0.05911482198193367,
        "quantile_99": 0.049232061906305,
        "hill_tail_index": 2.8186047164685064
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.022301744482692273,
        "excess_kurtosis": 24.408997969349045,
        "return_acf_1": -0.06534028537272056,
        "abs_return_acf_1": 0.4148795397391912,
        "abs_return_acf_5": 0.42763478996562604,
        "abs_return_acf_20": 0.23864136394347835,
        "quantile_01": -0.0645440730771809,
        "quantile_99": 0.06194236544149828,
        "hill_tail_index": 2.4987536868993128
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.02166562122957815,
        "excess_kurtosis": 13.63609255232803,
        "return_acf_1": -0.13280472145458724,
        "abs_return_acf_1": 0.45582299223745376,
        "abs_return_acf_5": 0.4164725959707192,
        "abs_return_acf_20": 0.32660288440126267,
        "quantile_01": -0.06377944620662669,
        "quantile_99": 0.06675136488240772,
        "hill_tail_index": 2.9594616628665134
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018993761428644527,
        "excess_kurtosis": 5.1099488800781145,
        "return_acf_1": -0.1931400455241745,
        "abs_return_acf_1": 0.3035171041102755,
        "abs_return_acf_5": 0.27527275757361874,
        "abs_return_acf_20": 0.24495215626047898,
        "quantile_01": -0.06153519792570947,
        "quantile_99": 0.04734827467772553,
        "hill_tail_index": 3.1148015366723434
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018721039691757785,
        "excess_kurtosis": 4.336624051422919,
        "return_acf_1": -0.16301982265522666,
        "abs_return_acf_1": 0.403329615495781,
        "abs_return_acf_5": 0.29778431526293153,
        "abs_return_acf_20": 0.26799278285359307,
        "quantile_01": -0.05071858298151548,
        "quantile_99": 0.055153033674441944,
        "hill_tail_index": 3.42353232238363
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01924054113294366,
        "excess_kurtosis": 8.313237201615467,
        "return_acf_1": -0.10233117156032058,
        "abs_return_acf_1": 0.3035232610083878,
        "abs_return_acf_5": 0.2854807137694249,
        "abs_return_acf_20": 0.2645907198610861,
        "quantile_01": -0.04736346796057817,
        "quantile_99": 0.05278537548035032,
        "hill_tail_index": 3.314872309667197
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022828383474780216,
        "excess_kurtosis": 10.444889473015756,
        "return_acf_1": -0.1039673675032912,
        "abs_return_acf_1": 0.4657519981292475,
        "abs_return_acf_5": 0.44693599103916193,
        "abs_return_acf_20": 0.3336440847233948,
        "quantile_01": -0.07960171432099755,
        "quantile_99": 0.06716400101785998,
        "hill_tail_index": 3.339518206791399
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.023819134992261588,
        "excess_kurtosis": 25.69426816959247,
        "return_acf_1": -0.07959750295211741,
        "abs_return_acf_1": 0.4018411178946165,
        "abs_return_acf_5": 0.3719379986369844,
        "abs_return_acf_20": 0.27188980861401885,
        "quantile_01": -0.08113572495431232,
        "quantile_99": 0.05779938654205766,
        "hill_tail_index": 2.0400703221443477
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018120822643733495,
        "excess_kurtosis": 2.6770498592812686,
        "return_acf_1": -0.1266126952185575,
        "abs_return_acf_1": 0.30613297596592376,
        "abs_return_acf_5": 0.25908058051621236,
        "abs_return_acf_20": 0.18285783728039048,
        "quantile_01": -0.05614701607602688,
        "quantile_99": 0.04772348684816992,
        "hill_tail_index": 4.258405919415474
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017323216223871743,
        "excess_kurtosis": 3.441533077911356,
        "return_acf_1": -0.11990273129010419,
        "abs_return_acf_1": 0.31181054710235806,
        "abs_return_acf_5": 0.2694886436003745,
        "abs_return_acf_20": 0.22419289900932254,
        "quantile_01": -0.04899505918302896,
        "quantile_99": 0.04981257783697896,
        "hill_tail_index": 3.31260820499294
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01675470888772915,
        "excess_kurtosis": 4.247052438288426,
        "return_acf_1": -0.16225053934878428,
        "abs_return_acf_1": 0.3013390370450252,
        "abs_return_acf_5": 0.2976610608380902,
        "abs_return_acf_20": 0.31875124364309726,
        "quantile_01": -0.04432693523447649,
        "quantile_99": 0.046448097417324356,
        "hill_tail_index": 3.5738096032958158
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01809893047011492,
        "excess_kurtosis": 2.1280092445254333,
        "return_acf_1": -0.18250170062671253,
        "abs_return_acf_1": 0.32516058195815484,
        "abs_return_acf_5": 0.288699095570684,
        "abs_return_acf_20": 0.23486441779730055,
        "quantile_01": -0.05097825600761415,
        "quantile_99": 0.04937021544787795,
        "hill_tail_index": 5.0193443122098635
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.022218493633344147,
        "excess_kurtosis": 23.146766284983773,
        "return_acf_1": -0.04254059743540389,
        "abs_return_acf_1": 0.4153179345011583,
        "abs_return_acf_5": 0.38298432933443827,
        "abs_return_acf_20": 0.31995971397001266,
        "quantile_01": -0.060866959281046316,
        "quantile_99": 0.05961333591096071,
        "hill_tail_index": 2.1156425438033915
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017670616072474558,
        "excess_kurtosis": 6.303683804640878,
        "return_acf_1": -0.21146700067050478,
        "abs_return_acf_1": 0.33620892579732353,
        "abs_return_acf_5": 0.30176751450994865,
        "abs_return_acf_20": 0.30030479661731446,
        "quantile_01": -0.05096798089256923,
        "quantile_99": 0.041793504076286535,
        "hill_tail_index": 2.8391490708486846
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02065731708340599,
        "excess_kurtosis": 19.65692930011347,
        "return_acf_1": -0.09444585864019596,
        "abs_return_acf_1": 0.4946593181493056,
        "abs_return_acf_5": 0.4157463271811781,
        "abs_return_acf_20": 0.3192855237750519,
        "quantile_01": -0.05899489394257273,
        "quantile_99": 0.06513690243115397,
        "hill_tail_index": 2.417244246101806
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017945236771950646,
        "excess_kurtosis": 8.572723871832784,
        "return_acf_1": -0.08190666558197802,
        "abs_return_acf_1": 0.3111045236904155,
        "abs_return_acf_5": 0.3396697258025231,
        "abs_return_acf_20": 0.22840494964388014,
        "quantile_01": -0.047213573367321474,
        "quantile_99": 0.06118749695601068,
        "hill_tail_index": 2.6031341233190175
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022729020368345447,
        "excess_kurtosis": 19.442953754450237,
        "return_acf_1": -0.1007800552238541,
        "abs_return_acf_1": 0.4719870815221326,
        "abs_return_acf_5": 0.3944813601586137,
        "abs_return_acf_20": 0.33230458260885987,
        "quantile_01": -0.07940974097248903,
        "quantile_99": 0.05677892925602581,
        "hill_tail_index": 2.1255277107511477
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01955139587537041,
        "excess_kurtosis": 3.563501915621961,
        "return_acf_1": -0.1317247616395741,
        "abs_return_acf_1": 0.2864518711420321,
        "abs_return_acf_5": 0.3232192441360692,
        "abs_return_acf_20": 0.2916844378311037,
        "quantile_01": -0.055759337463496664,
        "quantile_99": 0.05528926552153162,
        "hill_tail_index": 3.9105052800002142
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02024944131642755,
        "excess_kurtosis": 7.4319536521498275,
        "return_acf_1": -0.15931449892616711,
        "abs_return_acf_1": 0.3923700339778766,
        "abs_return_acf_5": 0.32242861074935847,
        "abs_return_acf_20": 0.2880761550186308,
        "quantile_01": -0.06272006654128857,
        "quantile_99": 0.058219561497476716,
        "hill_tail_index": 3.9568820948740884
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.024086264380892206,
        "excess_kurtosis": 20.950647756613037,
        "return_acf_1": -0.01667228965207336,
        "abs_return_acf_1": 0.4218503872788265,
        "abs_return_acf_5": 0.388534834722873,
        "abs_return_acf_20": 0.31231756053860227,
        "quantile_01": -0.08980467257194673,
        "quantile_99": 0.06051818870741413,
        "hill_tail_index": 2.10439351878423
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01769881017884406,
        "excess_kurtosis": 3.3078240315733822,
        "return_acf_1": -0.10196087564035067,
        "abs_return_acf_1": 0.21902802850355776,
        "abs_return_acf_5": 0.2461456485405178,
        "abs_return_acf_20": 0.19060435025752745,
        "quantile_01": -0.047382901301223926,
        "quantile_99": 0.04890099055626338,
        "hill_tail_index": 3.9743325865613928
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018385972264919052,
        "excess_kurtosis": 6.415539424866331,
        "return_acf_1": -0.15409066910823188,
        "abs_return_acf_1": 0.3624250152636397,
        "abs_return_acf_5": 0.34966969939392284,
        "abs_return_acf_20": 0.264255469178314,
        "quantile_01": -0.06112625569095755,
        "quantile_99": 0.0494856858453954,
        "hill_tail_index": 2.9653033610807387
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.023237886310017025,
        "excess_kurtosis": 19.283012630074225,
        "return_acf_1": -0.010265817490789033,
        "abs_return_acf_1": 0.4973246972498077,
        "abs_return_acf_5": 0.401729594108625,
        "abs_return_acf_20": 0.3336595906971855,
        "quantile_01": -0.07567770242471765,
        "quantile_99": 0.05973951352770569,
        "hill_tail_index": 1.9318641165529062
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.02209658129287644,
        "excess_kurtosis": 12.19219727584358,
        "return_acf_1": -0.10608903710620467,
        "abs_return_acf_1": 0.39808555688074204,
        "abs_return_acf_5": 0.3889252312046175,
        "abs_return_acf_20": 0.35036465710512343,
        "quantile_01": -0.0787657869119719,
        "quantile_99": 0.06547650059967045,
        "hill_tail_index": 3.6804356291025195
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02119939249958847,
        "excess_kurtosis": 18.39217131075422,
        "return_acf_1": -0.06706267259150726,
        "abs_return_acf_1": 0.4680234599455021,
        "abs_return_acf_5": 0.38701131171303643,
        "abs_return_acf_20": 0.29990318876499555,
        "quantile_01": -0.06643730153860607,
        "quantile_99": 0.05803039741567988,
        "hill_tail_index": 2.7135460887770813
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01836686475412436,
        "excess_kurtosis": 4.987682078786705,
        "return_acf_1": -0.22988166038510888,
        "abs_return_acf_1": 0.39437295762971003,
        "abs_return_acf_5": 0.41200092337985517,
        "abs_return_acf_20": 0.3180712228408528,
        "quantile_01": -0.05519361893269352,
        "quantile_99": 0.05514841522996616,
        "hill_tail_index": 3.893632255920421
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01916859762153098,
        "excess_kurtosis": 4.026609292356752,
        "return_acf_1": -0.13454453097249885,
        "abs_return_acf_1": 0.29333766205251743,
        "abs_return_acf_5": 0.29953137306587674,
        "abs_return_acf_20": 0.22963805666491152,
        "quantile_01": -0.062241803540714694,
        "quantile_99": 0.05001663555178016,
        "hill_tail_index": 3.609831168370069
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
Training: False
Coverage status: FAIL
Unseen state share: 0.0
Unclosed decisions: 30
Ledger, coverage counts and pending liabilities: [learning.json](learning.json).
