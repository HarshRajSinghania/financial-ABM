# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27124
Run ID: `ba4aef7dc93d6f7c5bdd1cd04da94c12531cf6e1e599e283e48840efa50408b9`
Result fingerprint: `87c5f38ebe9b30d4b22047d839a2973c6fde53b168fe0808b7ec64c1f5f120fe`

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
    "equal_weight_sd": -0.6430476190476158,
    "equal_weight_raw": -9.645714285714238,
    "fixed_start_cap_weight_sd": -0.628043650447615,
    "fixed_start_cap_weight_raw": -9.420654756714228,
    "end_cap_weight_sd": -0.6515922174351814,
    "end_cap_weight_raw": -9.773883261527724
  },
  "full_period_change": {
    "equal_weight_sd": -0.9859047619047572,
    "equal_weight_raw": -14.788571428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.935074735449731,
    "inflation_mean_sd": 0.6461226851851852
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.3093333333333364,
    "equal_weight_raw": 4.640000000000047,
    "fixed_start_cap_weight_sd": 0.32433730193333704,
    "fixed_start_cap_weight_raw": 4.865059529000057,
    "end_cap_weight_sd": 0.30078873494577113,
    "end_cap_weight_raw": 4.511831024186567
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6707142857142826,
      "change_raw": -10.060714285714239,
      "decay_adjusted_gain_sd": 0.2816666666666697
    },
    "mid": {
      "count": 9,
      "change_sd": -0.5634920634920605,
      "change_raw": -8.452380952380908,
      "decay_adjusted_gain_sd": 0.38888888888889195
    },
    "small": {
      "count": 18,
      "change_sd": -0.6782142857142825,
      "change_raw": -10.173214285714238,
      "decay_adjusted_gain_sd": 0.27416666666666983
    },
    "large_minus_small_sd": 0.007499999999999951,
    "large_minus_small_raw": 0.11249999999999927
  },
  "inflation": {
    "initial_mean_sd": 0.26083333333333336,
    "final_mean_sd": 0.6363333333333332,
    "mean_sd": 0.47484013322231466,
    "mean_absolute_raw_gap": 7.122601998334721,
    "final_absolute_raw_gap": 9.545,
    "mean_range_fraction": 0.07122601998334721
  },
  "impact": {
    "initial_share": 0.22666666666666666,
    "final_share": 0.26666666666666666,
    "initial_wealth_share": 0.24972429463563403,
    "final_wealth_share": 0.26768001465935215
  },
  "pricing_slope": {
    "mean": -0.00013691020428866928,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.04981549611164558,
    "real_improvement_cost": 0.035005179233450395,
    "washing_cost": 0.014810316878195187,
    "fine_transfer": 0.004985454400719699,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.05480095051236528,
    "resource_cost_fraction_initial_cap": 0.001660516537054853,
    "private_net_outflow_fraction_initial_cap": 0.0018266983504121764,
    "fine_transfer_fraction_initial_cap": 0.00016618181335732333,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.012924072477117493,
    "unapplied_final_day_resource_cost": 0.002099722595501603
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 186.2874150485609,
    "beneficial_raw_gain_per_resource_cost": 2794.3112257284133,
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
    "accrued_cost": 3.2312318519452434,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.25504137575476704,
    "accrued_cost_fraction_initial_cap": 0.10770772839817479,
    "mean_contract_rate": 0.044295998501093115,
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
    "status": "PASS",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": true,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 0,
    "maximum_relative_cash_error": 1.678099164920501e-15,
    "maximum_absolute_share_error": 1.887379141862766e-15,
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
      "minimum": -0.2589979392020148,
      "maximum": -0.038627160974355285,
      "mean": -0.14923914338161984,
      "median": -0.14783789889534563,
      "quantile_05": -0.21274748517827355,
      "quantile_95": -0.05160651009846931
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
      "minimum": 0.2084700360854345,
      "maximum": 0.8151139256599105,
      "mean": 0.5182132596975643,
      "median": 0.49002745686873217,
      "quantile_05": 0.26080555227177293,
      "quantile_95": 0.7864644346071256
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
        "daily_volatility": 0.022115901943034828,
        "excess_kurtosis": 10.684023554384497,
        "return_acf_1": -0.07747922724111019,
        "abs_return_acf_1": 0.35820078083989787,
        "abs_return_acf_5": 0.36189394385568974,
        "abs_return_acf_20": 0.3070551331208317,
        "quantile_01": -0.07901379675215055,
        "quantile_99": 0.05690247992009288,
        "hill_tail_index": 2.95940977475211
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.02392094169350159,
        "excess_kurtosis": 13.204922693233772,
        "return_acf_1": -0.13261608134832567,
        "abs_return_acf_1": 0.4703936217312307,
        "abs_return_acf_5": 0.49127750904454853,
        "abs_return_acf_20": 0.2939956495897366,
        "quantile_01": -0.08635427651983037,
        "quantile_99": 0.05913291292035209,
        "hill_tail_index": 3.2792568154126887
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.019606934940877323,
        "excess_kurtosis": 4.661052741196199,
        "return_acf_1": -0.10557244855399688,
        "abs_return_acf_1": 0.36729942237110796,
        "abs_return_acf_5": 0.32290855527377244,
        "abs_return_acf_20": 0.28236196145299136,
        "quantile_01": -0.06428837403161021,
        "quantile_99": 0.05249541241338326,
        "hill_tail_index": 4.646285520621635
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019967323987796895,
        "excess_kurtosis": 4.818385848412739,
        "return_acf_1": -0.1501542754083728,
        "abs_return_acf_1": 0.33804594951381833,
        "abs_return_acf_5": 0.34646979646082404,
        "abs_return_acf_20": 0.2737713582150328,
        "quantile_01": -0.06082685628319016,
        "quantile_99": 0.0594865747663279,
        "hill_tail_index": 3.8533233866459717
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01983385779741567,
        "excess_kurtosis": 11.633357667016956,
        "return_acf_1": -0.2589979392020148,
        "abs_return_acf_1": 0.3450043164831589,
        "abs_return_acf_5": 0.3592833919274461,
        "abs_return_acf_20": 0.3009101805782606,
        "quantile_01": -0.07152672932647205,
        "quantile_99": 0.054890381651153314,
        "hill_tail_index": 2.247479805163293
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022746161947087333,
        "excess_kurtosis": 9.02162996110748,
        "return_acf_1": -0.17107819962415113,
        "abs_return_acf_1": 0.3476176098307506,
        "abs_return_acf_5": 0.4213916713062523,
        "abs_return_acf_20": 0.23872932530663807,
        "quantile_01": -0.086610606190581,
        "quantile_99": 0.057014881539706484,
        "hill_tail_index": 3.4722173888586854
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.020935072305186035,
        "excess_kurtosis": 20.010081161700917,
        "return_acf_1": -0.13286374332303497,
        "abs_return_acf_1": 0.45199246835957574,
        "abs_return_acf_5": 0.46264720036423446,
        "abs_return_acf_20": 0.3001858239031153,
        "quantile_01": -0.06234882764438261,
        "quantile_99": 0.03988161658560588,
        "hill_tail_index": 1.9219143421658678
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01862970175415222,
        "excess_kurtosis": 4.700758783869193,
        "return_acf_1": -0.041610609651394764,
        "abs_return_acf_1": 0.3158848299282516,
        "abs_return_acf_5": 0.3306837494432779,
        "abs_return_acf_20": 0.31197846871519613,
        "quantile_01": -0.055593230242846466,
        "quantile_99": 0.04870092023919345,
        "hill_tail_index": 3.7018105588792625
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.023511320050200367,
        "excess_kurtosis": 15.024460662286874,
        "return_acf_1": -0.2022159833152895,
        "abs_return_acf_1": 0.4802534458725644,
        "abs_return_acf_5": 0.4916522866342209,
        "abs_return_acf_20": 0.3260778027637543,
        "quantile_01": -0.07699979148851495,
        "quantile_99": 0.05936373489420867,
        "hill_tail_index": 2.3681996745639804
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022269332153027108,
        "excess_kurtosis": 9.434927862029447,
        "return_acf_1": -0.20739689461299876,
        "abs_return_acf_1": 0.4237278173744501,
        "abs_return_acf_5": 0.3806621823256632,
        "abs_return_acf_20": 0.28255127790678825,
        "quantile_01": -0.08255178743320894,
        "quantile_99": 0.05724553021155163,
        "hill_tail_index": 3.1375294752506884
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.024780005474043354,
        "excess_kurtosis": 7.678667255858485,
        "return_acf_1": -0.1876782274171929,
        "abs_return_acf_1": 0.4871604307241104,
        "abs_return_acf_5": 0.48903368302577344,
        "abs_return_acf_20": 0.3324683003764052,
        "quantile_01": -0.08802627593831407,
        "quantile_99": 0.07625690916774637,
        "hill_tail_index": 4.220386523491524
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019912323219901856,
        "excess_kurtosis": 5.5210101735388495,
        "return_acf_1": -0.20778998183557748,
        "abs_return_acf_1": 0.3736737733343735,
        "abs_return_acf_5": 0.3627723397170114,
        "abs_return_acf_20": 0.25832155533204176,
        "quantile_01": -0.0629818678128237,
        "quantile_99": 0.059139299491979457,
        "hill_tail_index": 3.9738166125674343
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.025266266089121085,
        "excess_kurtosis": 14.584089049751128,
        "return_acf_1": -0.11980308624255478,
        "abs_return_acf_1": 0.4437418336823083,
        "abs_return_acf_5": 0.4593854584365644,
        "abs_return_acf_20": 0.24569729580724478,
        "quantile_01": -0.09068467670847302,
        "quantile_99": 0.06649671350349956,
        "hill_tail_index": 2.595176499318172
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022084485995443142,
        "excess_kurtosis": 15.364419473021577,
        "return_acf_1": -0.14552152238231844,
        "abs_return_acf_1": 0.43804743813321956,
        "abs_return_acf_5": 0.47062828204223794,
        "abs_return_acf_20": 0.2940734311708417,
        "quantile_01": -0.07518143937249107,
        "quantile_99": 0.06615087303269941,
        "hill_tail_index": 3.535630515080859
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.017340996845863745,
        "excess_kurtosis": 7.42101950000194,
        "return_acf_1": -0.1658584463132966,
        "abs_return_acf_1": 0.24968279119119627,
        "abs_return_acf_5": 0.23303143197263346,
        "abs_return_acf_20": 0.18659284947243707,
        "quantile_01": -0.05615163344012188,
        "quantile_99": 0.04359584160260652,
        "hill_tail_index": 2.264322062381504
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02337134942737217,
        "excess_kurtosis": 11.586304038692067,
        "return_acf_1": -0.12510446546356566,
        "abs_return_acf_1": 0.3723410989695727,
        "abs_return_acf_5": 0.41585892975978805,
        "abs_return_acf_20": 0.34371689088365887,
        "quantile_01": -0.08323764183586727,
        "quantile_99": 0.06057464527136026,
        "hill_tail_index": 2.8344483892015138
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.017591741220328205,
        "excess_kurtosis": 5.494475465784207,
        "return_acf_1": -0.038627160974355285,
        "abs_return_acf_1": 0.2305488455281239,
        "abs_return_acf_5": 0.2599913148695578,
        "abs_return_acf_20": 0.26147367244487946,
        "quantile_01": -0.052699948105874715,
        "quantile_99": 0.05299724927427798,
        "hill_tail_index": 3.7586707149770406
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017902976858280083,
        "excess_kurtosis": 4.696927574326876,
        "return_acf_1": -0.1895273239940088,
        "abs_return_acf_1": 0.354359055355477,
        "abs_return_acf_5": 0.2902256098338865,
        "abs_return_acf_20": 0.21347990396346375,
        "quantile_01": -0.0539891611696019,
        "quantile_99": 0.048095532841059496,
        "hill_tail_index": 3.865596618769943
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01830756724974722,
        "excess_kurtosis": 5.313263281032356,
        "return_acf_1": -0.17483895514473802,
        "abs_return_acf_1": 0.3285543047802667,
        "abs_return_acf_5": 0.3165170101412328,
        "abs_return_acf_20": 0.2694961658104949,
        "quantile_01": -0.06253977494316487,
        "quantile_99": 0.04875531704308699,
        "hill_tail_index": 3.1200337978380404
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.02095866980352497,
        "excess_kurtosis": 7.279588183902312,
        "return_acf_1": -0.06382372175600473,
        "abs_return_acf_1": 0.392212241121913,
        "abs_return_acf_5": 0.34998705369531363,
        "abs_return_acf_20": 0.2978764716488134,
        "quantile_01": -0.06395834109013163,
        "quantile_99": 0.05654016071204817,
        "hill_tail_index": 3.0751885543758455
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.024395302646618263,
        "excess_kurtosis": 16.78023080284198,
        "return_acf_1": -0.14283178912027752,
        "abs_return_acf_1": 0.48550463907092545,
        "abs_return_acf_5": 0.5508758941291979,
        "abs_return_acf_20": 0.30325621309259476,
        "quantile_01": -0.07387723005555695,
        "quantile_99": 0.06354375340212352,
        "hill_tail_index": 2.2177557848706417
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02457692399931982,
        "excess_kurtosis": 16.881307524617412,
        "return_acf_1": -0.15576600678640654,
        "abs_return_acf_1": 0.451803895816773,
        "abs_return_acf_5": 0.4391146911227098,
        "abs_return_acf_20": 0.30860437604943725,
        "quantile_01": -0.09005363057977511,
        "quantile_99": 0.06349596674533668,
        "hill_tail_index": 2.5788283021044665
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.0239137181515819,
        "excess_kurtosis": 9.746394353044606,
        "return_acf_1": -0.2099198116449383,
        "abs_return_acf_1": 0.49359092997253157,
        "abs_return_acf_5": 0.5195663671262897,
        "abs_return_acf_20": 0.37017836150281036,
        "quantile_01": -0.08170714156326919,
        "quantile_99": 0.06762240494047157,
        "hill_tail_index": 3.5765565102013315
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01586980081262213,
        "excess_kurtosis": 5.434699520777491,
        "return_acf_1": -0.13205614408225155,
        "abs_return_acf_1": 0.23680759028112736,
        "abs_return_acf_5": 0.22031751211355416,
        "abs_return_acf_20": 0.2349332017416534,
        "quantile_01": -0.04160637105442,
        "quantile_99": 0.038924789502625526,
        "hill_tail_index": 2.736604185043395
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.023686352462762926,
        "excess_kurtosis": 15.086771181011645,
        "return_acf_1": -0.12161820282212696,
        "abs_return_acf_1": 0.3977470572187687,
        "abs_return_acf_5": 0.45251935175547187,
        "abs_return_acf_20": 0.3185541186879121,
        "quantile_01": -0.08298646222509928,
        "quantile_99": 0.05431108770207619,
        "hill_tail_index": 2.651613124822937
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02035480565259252,
        "excess_kurtosis": 25.653316205277527,
        "return_acf_1": -0.17947428017505662,
        "abs_return_acf_1": 0.3602269824904673,
        "abs_return_acf_5": 0.3201883930823654,
        "abs_return_acf_20": 0.2375778634797486,
        "quantile_01": -0.06307896520772428,
        "quantile_99": 0.047222477640571345,
        "hill_tail_index": 1.7680432339193966
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022213575865441572,
        "excess_kurtosis": 23.93334250659908,
        "return_acf_1": -0.1680951993483469,
        "abs_return_acf_1": 0.4991298952176551,
        "abs_return_acf_5": 0.5094314907580063,
        "abs_return_acf_20": 0.30215561878320973,
        "quantile_01": -0.07326794437718719,
        "quantile_99": 0.05256968262840457,
        "hill_tail_index": 2.45519391247748
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02200241531826338,
        "excess_kurtosis": 6.690279674729977,
        "return_acf_1": -0.21506103625100237,
        "abs_return_acf_1": 0.408351352118408,
        "abs_return_acf_5": 0.4447589361905977,
        "abs_return_acf_20": 0.279794477876406,
        "quantile_01": -0.07501054126505483,
        "quantile_99": 0.06073900255823732,
        "hill_tail_index": 3.3908981196506995
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.024381039166750638,
        "excess_kurtosis": 17.066074183549322,
        "return_acf_1": -0.136983932393997,
        "abs_return_acf_1": 0.36292580192980184,
        "abs_return_acf_5": 0.35633516260186665,
        "abs_return_acf_20": 0.26657440848470276,
        "quantile_01": -0.07980910186392796,
        "quantile_99": 0.0656466237844359,
        "hill_tail_index": 2.4757330460357183
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02345073464448631,
        "excess_kurtosis": 9.741758160101332,
        "return_acf_1": -0.11680960501988868,
        "abs_return_acf_1": 0.4547060369633766,
        "abs_return_acf_5": 0.4358578532259015,
        "abs_return_acf_20": 0.3063887193319514,
        "quantile_01": -0.08317916153784265,
        "quantile_99": 0.06539558066671546,
        "hill_tail_index": 3.2486763319729923
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
