# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27302
Run ID: `4b8e098d76db4f917316153950c466e0051053193b6b3262650289ad20b2448c`
Result fingerprint: `0895a8eb239be918894ba9efb9724fdef63f263b39ac03b507fd8133b026022e`

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
    "equal_weight_sd": -0.8520476190476157,
    "equal_weight_raw": -12.780714285714232,
    "fixed_start_cap_weight_sd": -0.7648756658365405,
    "fixed_start_cap_weight_raw": -11.47313498754811,
    "end_cap_weight_sd": -0.7722534039051988,
    "end_cap_weight_raw": -11.583801058577984
  },
  "full_period_change": {
    "equal_weight_sd": -1.30823809523809,
    "equal_weight_raw": -19.623571428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2245443121693074,
    "inflation_mean_sd": 0.2529093915343915
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.10033333333333666,
    "equal_weight_raw": 1.5050000000000499,
    "fixed_start_cap_weight_sd": 0.18750528654441181,
    "fixed_start_cap_weight_raw": 2.8125792981661775,
    "end_cap_weight_sd": 0.18012754847575366,
    "end_cap_weight_raw": 2.701913227136305
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5773809523809487,
      "change_raw": -8.66071428571423,
      "decay_adjusted_gain_sd": 0.3750000000000036
    },
    "mid": {
      "count": 9,
      "change_sd": -0.7918253968253933,
      "change_raw": -11.8773809523809,
      "decay_adjusted_gain_sd": 0.160555555555559
    },
    "small": {
      "count": 18,
      "change_sd": -0.9279365079365047,
      "change_raw": -13.919047619047571,
      "decay_adjusted_gain_sd": 0.02444444444444768
    },
    "large_minus_small_sd": 0.35055555555555606,
    "large_minus_small_raw": 5.258333333333341
  },
  "inflation": {
    "initial_mean_sd": 0.22341666666666665,
    "final_mean_sd": 0.25558333333333333,
    "mean_sd": 0.24682535387177354,
    "mean_absolute_raw_gap": 3.702380308076603,
    "final_absolute_raw_gap": 3.8337499999999998,
    "mean_range_fraction": 0.037023803080766034
  },
  "impact": {
    "initial_share": 0.2733333333333333,
    "final_share": 0.2733333333333333,
    "initial_wealth_share": 0.18096308528822616,
    "final_wealth_share": 0.1629983811333721
  },
  "pricing_slope": {
    "mean": 0.0012871542007669916,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.0023621942737354065,
    "real_improvement_cost": 0.0010720328692579342,
    "washing_cost": 0.001290161404477472,
    "fine_transfer": 0.01116845056191057,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.013530644835645977,
    "resource_cost_fraction_initial_cap": 7.873980912451354e-05,
    "private_net_outflow_fraction_initial_cap": 0.0004510214945215325,
    "fine_transfer_fraction_initial_cap": 0.00037228168539701895,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 9.564656931225954e-05,
    "unapplied_final_day_resource_cost": 0.00012680996052797877
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 1274.238970717806,
    "beneficial_raw_gain_per_resource_cost": 19113.584560767093,
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
    "accrued_cost": 3.044977260737955,
    "baseline_accrued_cost": 2.976190476190477,
    "value_adjustment": -0.06878678454747758,
    "accrued_cost_fraction_initial_cap": 0.1014992420245985,
    "mean_contract_rate": 0.04206311640235165,
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
    "maximum_relative_cash_error": 1.068999138876603e-15,
    "maximum_absolute_share_error": 1.5543122344752192e-15,
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
      "minimum": -0.287687477606292,
      "maximum": -0.06911467578578886,
      "mean": -0.1547570651044933,
      "median": -0.1540069908101434,
      "quantile_05": -0.21996532573376718,
      "quantile_95": -0.09739120379891714
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
      "minimum": 0.2672208805518885,
      "maximum": 0.8048756799799284,
      "mean": 0.6082475399487146,
      "median": 0.6304865693017337,
      "quantile_05": 0.4134710579204081,
      "quantile_95": 0.734767512607839
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
        "daily_volatility": 0.018345315676495253,
        "excess_kurtosis": 5.971530275843934,
        "return_acf_1": -0.16998444980818606,
        "abs_return_acf_1": 0.29078569048910835,
        "abs_return_acf_5": 0.2586395430383739,
        "abs_return_acf_20": 0.2994612095811817,
        "quantile_01": -0.05292686977237028,
        "quantile_99": 0.048904010840546804,
        "hill_tail_index": 3.0312968169615515
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01909481984305529,
        "excess_kurtosis": 7.874771483841329,
        "return_acf_1": -0.18870121189112965,
        "abs_return_acf_1": 0.4153179088244726,
        "abs_return_acf_5": 0.42804813762440286,
        "abs_return_acf_20": 0.3246690922396275,
        "quantile_01": -0.0619923689454027,
        "quantile_99": 0.050302251220726436,
        "hill_tail_index": 2.8275926735781294
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.015835791824226803,
        "excess_kurtosis": 2.633897597594755,
        "return_acf_1": -0.16572625846535924,
        "abs_return_acf_1": 0.1909796604852488,
        "abs_return_acf_5": 0.19118009770720065,
        "abs_return_acf_20": 0.18751244818053872,
        "quantile_01": -0.04154296141292744,
        "quantile_99": 0.038615246316001446,
        "hill_tail_index": 3.7454925151254597
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.016396058122397764,
        "excess_kurtosis": 3.6519104065298276,
        "return_acf_1": -0.10617300368988336,
        "abs_return_acf_1": 0.18712264070544432,
        "abs_return_acf_5": 0.22936354101109271,
        "abs_return_acf_20": 0.20190299245473253,
        "quantile_01": -0.04385393148027551,
        "quantile_99": 0.04063371201030557,
        "hill_tail_index": 3.5247932385567298
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01732665945652882,
        "excess_kurtosis": 5.32259625596479,
        "return_acf_1": -0.09513863735044135,
        "abs_return_acf_1": 0.3408201895170683,
        "abs_return_acf_5": 0.3196331583186622,
        "abs_return_acf_20": 0.27587938439535153,
        "quantile_01": -0.05593227211776525,
        "quantile_99": 0.05158752353667295,
        "hill_tail_index": 3.4773726204414683
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017861094211759822,
        "excess_kurtosis": 7.56108361687078,
        "return_acf_1": -0.18677750250745492,
        "abs_return_acf_1": 0.3408574897793604,
        "abs_return_acf_5": 0.34369584374230105,
        "abs_return_acf_20": 0.26012434660144684,
        "quantile_01": -0.05764330399305296,
        "quantile_99": 0.051671136916349114,
        "hill_tail_index": 3.898820439846271
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01917724001486691,
        "excess_kurtosis": 11.247016693168684,
        "return_acf_1": -0.11978458124990084,
        "abs_return_acf_1": 0.4145805032169188,
        "abs_return_acf_5": 0.47468430944604056,
        "abs_return_acf_20": 0.36193760338400743,
        "quantile_01": -0.06717895779906102,
        "quantile_99": 0.05449289195345858,
        "hill_tail_index": 2.5280527367033625
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01888908965199346,
        "excess_kurtosis": 5.237866933559902,
        "return_acf_1": -0.16109587097764852,
        "abs_return_acf_1": 0.29669873749572756,
        "abs_return_acf_5": 0.33590302126735233,
        "abs_return_acf_20": 0.28238055337075024,
        "quantile_01": -0.06057406399997382,
        "quantile_99": 0.059529100611371975,
        "hill_tail_index": 4.093091458435854
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01857708287622144,
        "excess_kurtosis": 6.193109020834935,
        "return_acf_1": -0.1812640216168405,
        "abs_return_acf_1": 0.2948340663612503,
        "abs_return_acf_5": 0.31963644177666994,
        "abs_return_acf_20": 0.2537145011677443,
        "quantile_01": -0.06152822172399399,
        "quantile_99": 0.05328338723241179,
        "hill_tail_index": 3.2670344884190383
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018375981758691772,
        "excess_kurtosis": 7.766823942967298,
        "return_acf_1": -0.2041022023512325,
        "abs_return_acf_1": 0.4205077945089649,
        "abs_return_acf_5": 0.36101768280543844,
        "abs_return_acf_20": 0.2610283753748386,
        "quantile_01": -0.05664027581749808,
        "quantile_99": 0.052673737283202814,
        "hill_tail_index": 2.7937613270964383
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01760776952521186,
        "excess_kurtosis": 6.133404907459527,
        "return_acf_1": -0.1001443405692764,
        "abs_return_acf_1": 0.23793331733688328,
        "abs_return_acf_5": 0.26339532005666993,
        "abs_return_acf_20": 0.16741926665064663,
        "quantile_01": -0.052669967467165714,
        "quantile_99": 0.0478078800335569,
        "hill_tail_index": 3.3167258437622995
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.018005567871780467,
        "excess_kurtosis": 11.402864673029047,
        "return_acf_1": -0.12028567264357343,
        "abs_return_acf_1": 0.3741574252262896,
        "abs_return_acf_5": 0.3600196825563152,
        "abs_return_acf_20": 0.23793639060422514,
        "quantile_01": -0.05955099101302548,
        "quantile_99": 0.046538510576301435,
        "hill_tail_index": 2.345141118464692
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02011635235692831,
        "excess_kurtosis": 14.73211454704862,
        "return_acf_1": -0.21221599474399278,
        "abs_return_acf_1": 0.42975630688329264,
        "abs_return_acf_5": 0.40370418512668516,
        "abs_return_acf_20": 0.27811049706429763,
        "quantile_01": -0.06866288072000941,
        "quantile_99": 0.05619356146554293,
        "hill_tail_index": 2.167637455602631
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01721820833421483,
        "excess_kurtosis": 3.0746416354679953,
        "return_acf_1": -0.18132678061465937,
        "abs_return_acf_1": 0.2862985842712028,
        "abs_return_acf_5": 0.24714252259406003,
        "abs_return_acf_20": 0.2135960557778481,
        "quantile_01": -0.04985327769185965,
        "quantile_99": 0.044271541645906104,
        "hill_tail_index": 3.411125650520645
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.015892699169683774,
        "excess_kurtosis": 3.5088485326384387,
        "return_acf_1": -0.11970909656081961,
        "abs_return_acf_1": 0.27372080880284727,
        "abs_return_acf_5": 0.2613146357697952,
        "abs_return_acf_20": 0.2764515641979592,
        "quantile_01": -0.04816788915441478,
        "quantile_99": 0.03969932490747398,
        "hill_tail_index": 3.036287427816407
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01848254244703892,
        "excess_kurtosis": 11.018727911874496,
        "return_acf_1": -0.06911467578578886,
        "abs_return_acf_1": 0.38724238240258796,
        "abs_return_acf_5": 0.3550432011604002,
        "abs_return_acf_20": 0.23568605640180096,
        "quantile_01": -0.05641648346108526,
        "quantile_99": 0.04577256892388375,
        "hill_tail_index": 2.4018715209925676
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.018616425739080393,
        "excess_kurtosis": 12.716855732478962,
        "return_acf_1": -0.1218832737053316,
        "abs_return_acf_1": 0.3456479822426174,
        "abs_return_acf_5": 0.41929957900951614,
        "abs_return_acf_20": 0.2916718681346647,
        "quantile_01": -0.05865984895691571,
        "quantile_99": 0.04656243272340217,
        "hill_tail_index": 2.0189077651538874
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.018523394917820606,
        "excess_kurtosis": 4.9502101123233935,
        "return_acf_1": -0.16005983781523678,
        "abs_return_acf_1": 0.26342067822308807,
        "abs_return_acf_5": 0.2829694945937188,
        "abs_return_acf_20": 0.2460124462672787,
        "quantile_01": -0.05724903785144861,
        "quantile_99": 0.05429488443252599,
        "hill_tail_index": 4.425199174116124
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01769100696553293,
        "excess_kurtosis": 3.5506160220999403,
        "return_acf_1": -0.1827688691891387,
        "abs_return_acf_1": 0.3109275062252626,
        "abs_return_acf_5": 0.2289168269606191,
        "abs_return_acf_20": 0.18863585193749494,
        "quantile_01": -0.05268938670862558,
        "quantile_99": 0.045056592733817506,
        "hill_tail_index": 3.3568339976321577
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018199403232953392,
        "excess_kurtosis": 6.644121473546408,
        "return_acf_1": -0.1457083305285742,
        "abs_return_acf_1": 0.37110192338423426,
        "abs_return_acf_5": 0.3567161185053627,
        "abs_return_acf_20": 0.22323774133693475,
        "quantile_01": -0.0571926511980353,
        "quantile_99": 0.043395468930438025,
        "hill_tail_index": 3.088497447553518
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.018209337897860826,
        "excess_kurtosis": 5.019192088066198,
        "return_acf_1": -0.14620405572953057,
        "abs_return_acf_1": 0.38223917161128607,
        "abs_return_acf_5": 0.3229464777062313,
        "abs_return_acf_20": 0.25587772942047443,
        "quantile_01": -0.057547588198456394,
        "quantile_99": 0.046731203725075623,
        "hill_tail_index": 3.4303765819796355
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017694138766821108,
        "excess_kurtosis": 3.974291019824456,
        "return_acf_1": -0.14021673003817828,
        "abs_return_acf_1": 0.26447499354751314,
        "abs_return_acf_5": 0.2657879401845707,
        "abs_return_acf_20": 0.20672010829121087,
        "quantile_01": -0.05048458517717467,
        "quantile_99": 0.047387911293343195,
        "hill_tail_index": 4.540059937470004
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01839348317639491,
        "excess_kurtosis": 13.182902964337536,
        "return_acf_1": -0.16818636031357684,
        "abs_return_acf_1": 0.34130089589477053,
        "abs_return_acf_5": 0.3428061135158475,
        "abs_return_acf_20": 0.23759681714265377,
        "quantile_01": -0.06351530448189643,
        "quantile_99": 0.04674806941724051,
        "hill_tail_index": 2.5088166218931236
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.016858474268097633,
        "excess_kurtosis": 3.44082187271057,
        "return_acf_1": -0.14795414380505004,
        "abs_return_acf_1": 0.23997567755070662,
        "abs_return_acf_5": 0.22001490577824231,
        "abs_return_acf_20": 0.15081424356262332,
        "quantile_01": -0.05150494841022749,
        "quantile_99": 0.04164626997079967,
        "hill_tail_index": 4.5309416361539965
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.017978520861671,
        "excess_kurtosis": 5.267529291872135,
        "return_acf_1": -0.10902839133852604,
        "abs_return_acf_1": 0.3416447115754683,
        "abs_return_acf_5": 0.36246647882445027,
        "abs_return_acf_20": 0.2441193014986398,
        "quantile_01": -0.05949437263072299,
        "quantile_99": 0.049281651556013654,
        "hill_tail_index": 4.110010611625401
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017506910313409157,
        "excess_kurtosis": 6.207648824203185,
        "return_acf_1": -0.10772678193588715,
        "abs_return_acf_1": 0.3195736293410805,
        "abs_return_acf_5": 0.32154293545925067,
        "abs_return_acf_20": 0.27325768596774114,
        "quantile_01": -0.050692150467644415,
        "quantile_99": 0.05137315358400885,
        "hill_tail_index": 4.135477559875975
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019630705917339494,
        "excess_kurtosis": 10.591030184602692,
        "return_acf_1": -0.22630568745267352,
        "abs_return_acf_1": 0.4549763133649991,
        "abs_return_acf_5": 0.4279513726313097,
        "abs_return_acf_20": 0.32081002020853033,
        "quantile_01": -0.061862411963714586,
        "quantile_99": 0.058104855016253974,
        "hill_tail_index": 2.4732948065227345
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017901758596324382,
        "excess_kurtosis": 5.45363473953128,
        "return_acf_1": -0.1864059235373539,
        "abs_return_acf_1": 0.2853452266656128,
        "abs_return_acf_5": 0.27387728087568464,
        "abs_return_acf_20": 0.1986378354667183,
        "quantile_01": -0.05387743106331243,
        "quantile_99": 0.05021511175325962,
        "hill_tail_index": 3.114669328283184
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019507472916856783,
        "excess_kurtosis": 13.200991066139142,
        "return_acf_1": -0.287687477606292,
        "abs_return_acf_1": 0.4395387266341059,
        "abs_return_acf_5": 0.3721926197289224,
        "abs_return_acf_20": 0.29570421455405366,
        "quantile_01": -0.06752512813598086,
        "quantile_99": 0.057798579013439724,
        "hill_tail_index": 2.2037310513339965
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017038886584029734,
        "excess_kurtosis": 5.623409874018613,
        "return_acf_1": -0.13103178931326223,
        "abs_return_acf_1": 0.2860980887692387,
        "abs_return_acf_5": 0.30115363194285716,
        "abs_return_acf_20": 0.17046609270691676,
        "quantile_01": -0.05538273552115467,
        "quantile_99": 0.03947194049090111,
        "hill_tail_index": 2.7486806123347147
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
