# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27072
Run ID: `1433addf96975ca77453218e08f991da050db9e1e63ef17fc74e2d638ef3c40c`
Result fingerprint: `620e470516db671b4ef5e33f251daa6b0eae9209fad45f9f81a791978a604dcd`

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
    "equal_weight_sd": -0.4610476190476159,
    "equal_weight_raw": -6.915714285714238,
    "fixed_start_cap_weight_sd": -0.46219685178853787,
    "fixed_start_cap_weight_raw": -6.932952776828069,
    "end_cap_weight_sd": -0.46394458726209065,
    "end_cap_weight_raw": -6.959168808931359
  },
  "full_period_change": {
    "equal_weight_sd": -0.7965714285714237,
    "equal_weight_raw": -11.948571428571356
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.749127645502641,
    "inflation_mean_sd": 0.6425095899470898
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.4812285237847407,
    "equal_weight_raw": 7.218427856771111,
    "fixed_start_cap_weight_sd": 0.48251192482781735,
    "fixed_start_cap_weight_raw": 7.237678872417263,
    "end_cap_weight_sd": 0.4805343387503701,
    "end_cap_weight_raw": 7.2080150812555495
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.499047619047616,
      "change_raw": -7.4857142857142405,
      "decay_adjusted_gain_sd": 0.45333333333333625
    },
    "mid": {
      "count": 9,
      "change_sd": -0.4032142857142825,
      "change_raw": -6.048214285714238,
      "decay_adjusted_gain_sd": 0.5491666666666698
    },
    "small": {
      "count": 18,
      "change_sd": -0.4836309523809492,
      "change_raw": -7.2544642857142385,
      "decay_adjusted_gain_sd": 0.4519086507523435
    },
    "large_minus_small_sd": -0.0154166666666668,
    "large_minus_small_raw": -0.231250000000002
  },
  "inflation": {
    "initial_mean_sd": 0.2866666666666667,
    "final_mean_sd": 0.6769999999999999,
    "mean_sd": 0.4983974465723009,
    "mean_absolute_raw_gap": 7.475961698584514,
    "final_absolute_raw_gap": 10.155,
    "mean_range_fraction": 0.07475961698584514
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.38,
    "initial_wealth_share": 0.33168897214540843,
    "final_wealth_share": 0.4642450468998747
  },
  "pricing_slope": {
    "mean": -0.0016248776868095414,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.07182103290619027,
    "real_improvement_cost": 0.06134265361836828,
    "washing_cost": 0.010478379287821991,
    "fine_transfer": 0.010004026823326979,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08182505972951724,
    "resource_cost_fraction_initial_cap": 0.002394034430206343,
    "private_net_outflow_fraction_initial_cap": 0.0027275019909839093,
    "fine_transfer_fraction_initial_cap": 0.0003334675607775661,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0040736782562766334,
    "unapplied_final_day_resource_cost": 0.002432835819338378
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 201.01153004021896,
    "beneficial_raw_gain_per_resource_cost": 3015.1729506032843,
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
    "fixed_exposure": 14.999999999999995,
    "accrued_cost": 3.1553873334255482,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.1791968572350726,
    "accrued_cost_fraction_initial_cap": 0.10517957778085164,
    "mean_contract_rate": 0.0434889822071626,
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
    "status": "FAIL",
    "checks": {
      "finite_positive_prices": true,
      "finite_positive_intrinsic_values": true,
      "no_price_caps": false,
      "cash_conservation": true,
      "share_conservation": true
    },
    "price_cap_hits": 2,
    "maximum_relative_cash_error": 2.92963455804566e-15,
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
      "minimum": -0.22389403517553016,
      "maximum": -0.10719511126740806,
      "mean": -0.1685457551227645,
      "median": -0.16818532414124615,
      "quantile_05": -0.21320561741108648,
      "quantile_95": -0.1109324517863261
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
      "minimum": 0.27543365947269355,
      "maximum": 0.7977733820306984,
      "mean": 0.650143124990567,
      "median": 0.6703117303007791,
      "quantile_05": 0.4885547094912972,
      "quantile_95": 0.7711402493677452
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
        "daily_volatility": 0.022812039215233053,
        "excess_kurtosis": 11.123093941940745,
        "return_acf_1": -0.19733744819572022,
        "abs_return_acf_1": 0.38399430721437844,
        "abs_return_acf_5": 0.3790240772746416,
        "abs_return_acf_20": 0.3398688731716032,
        "quantile_01": -0.07168555849313853,
        "quantile_99": 0.06184671795603652,
        "hill_tail_index": 2.7093550050696567
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020962789819377936,
        "excess_kurtosis": 9.429910198578087,
        "return_acf_1": -0.17033087217647763,
        "abs_return_acf_1": 0.3902885483215081,
        "abs_return_acf_5": 0.3746720898341693,
        "abs_return_acf_20": 0.3172926315615495,
        "quantile_01": -0.07453397444938785,
        "quantile_99": 0.06107320748118462,
        "hill_tail_index": 3.1521938227256596
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020719232616526088,
        "excess_kurtosis": 6.609233495360591,
        "return_acf_1": -0.1629321962787545,
        "abs_return_acf_1": 0.3681115368771487,
        "abs_return_acf_5": 0.33322434090581277,
        "abs_return_acf_20": 0.34008980363084007,
        "quantile_01": -0.07159290579429135,
        "quantile_99": 0.06269791882794762,
        "hill_tail_index": 3.5951036048244003
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.02326975784446962,
        "excess_kurtosis": 12.587375397923394,
        "return_acf_1": -0.22389403517553016,
        "abs_return_acf_1": 0.4468019362680792,
        "abs_return_acf_5": 0.37809093209562683,
        "abs_return_acf_20": 0.33889637911431997,
        "quantile_01": -0.08520310726416948,
        "quantile_99": 0.060154867188070206,
        "hill_tail_index": 2.9963141671095994
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.02287707824878379,
        "excess_kurtosis": 9.823005748600723,
        "return_acf_1": -0.17956528415402465,
        "abs_return_acf_1": 0.4733635981848671,
        "abs_return_acf_5": 0.3998475127258311,
        "abs_return_acf_20": 0.3515864387016455,
        "quantile_01": -0.08555041601780586,
        "quantile_99": 0.061992651091895154,
        "hill_tail_index": 3.3352566720954218
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.021858745185016702,
        "excess_kurtosis": 8.722881936451323,
        "return_acf_1": -0.13339430611639455,
        "abs_return_acf_1": 0.40142115133541434,
        "abs_return_acf_5": 0.3792191393966281,
        "abs_return_acf_20": 0.3829859655518117,
        "quantile_01": -0.07653214759597489,
        "quantile_99": 0.06298261034912565,
        "hill_tail_index": 3.462109832869519
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021468463052800008,
        "excess_kurtosis": 9.10304947567756,
        "return_acf_1": -0.20048645431086579,
        "abs_return_acf_1": 0.4121812894272596,
        "abs_return_acf_5": 0.29468968001512075,
        "abs_return_acf_20": 0.34300085723644,
        "quantile_01": -0.06969266741365997,
        "quantile_99": 0.06343804200035551,
        "hill_tail_index": 2.5245358635401516
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.021177266222622417,
        "excess_kurtosis": 6.963872584031142,
        "return_acf_1": -0.11145353130747955,
        "abs_return_acf_1": 0.47693207450944675,
        "abs_return_acf_5": 0.42470734666794,
        "abs_return_acf_20": 0.33273341440924675,
        "quantile_01": -0.07364696110150186,
        "quantile_99": 0.05445603878427625,
        "hill_tail_index": 3.131303763821423
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019878265607496944,
        "excess_kurtosis": 12.955910508022571,
        "return_acf_1": -0.1412582595962709,
        "abs_return_acf_1": 0.40681774800117354,
        "abs_return_acf_5": 0.3386266803344818,
        "abs_return_acf_20": 0.371088818172861,
        "quantile_01": -0.057105635106379844,
        "quantile_99": 0.05862637206470511,
        "hill_tail_index": 2.5708505093947274
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02157994181755594,
        "excess_kurtosis": 8.857983604828545,
        "return_acf_1": -0.17160264377990106,
        "abs_return_acf_1": 0.3935045689663854,
        "abs_return_acf_5": 0.34686170045786346,
        "abs_return_acf_20": 0.3416328374718124,
        "quantile_01": -0.07094135697570451,
        "quantile_99": 0.0631729896973955,
        "hill_tail_index": 3.554113132052727
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.020046415989301937,
        "excess_kurtosis": 6.332263124621006,
        "return_acf_1": -0.19871624802559787,
        "abs_return_acf_1": 0.3875423536546582,
        "abs_return_acf_5": 0.30006388719359073,
        "abs_return_acf_20": 0.35064528711929555,
        "quantile_01": -0.06678703105893198,
        "quantile_99": 0.051723223966756646,
        "hill_tail_index": 3.1041146381956857
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.021423747968073024,
        "excess_kurtosis": 8.05739714461924,
        "return_acf_1": -0.2073867199364758,
        "abs_return_acf_1": 0.3729265070339138,
        "abs_return_acf_5": 0.29541038595537994,
        "abs_return_acf_20": 0.3435904035993902,
        "quantile_01": -0.07710131830319848,
        "quantile_99": 0.06073863319456697,
        "hill_tail_index": 3.785574951480889
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.02084594383747833,
        "excess_kurtosis": 6.932696555296646,
        "return_acf_1": -0.16585315677561013,
        "abs_return_acf_1": 0.4738684400800533,
        "abs_return_acf_5": 0.3687785764636464,
        "abs_return_acf_20": 0.32991945969403547,
        "quantile_01": -0.07711760103653682,
        "quantile_99": 0.05726670996369063,
        "hill_tail_index": 3.507788408008845
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.021618138150917187,
        "excess_kurtosis": 6.69030625411,
        "return_acf_1": -0.18992569967491282,
        "abs_return_acf_1": 0.4080715267098873,
        "abs_return_acf_5": 0.3935893151049489,
        "abs_return_acf_20": 0.3724904102907001,
        "quantile_01": -0.07035853589735133,
        "quantile_99": 0.05763405179032563,
        "hill_tail_index": 3.783913390535359
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019966741498610108,
        "excess_kurtosis": 7.262121624040798,
        "return_acf_1": -0.21796653352667705,
        "abs_return_acf_1": 0.28191809318089533,
        "abs_return_acf_5": 0.21389410726936156,
        "abs_return_acf_20": 0.29933197269653206,
        "quantile_01": -0.06303034893676036,
        "quantile_99": 0.04864630364870065,
        "hill_tail_index": 2.640895617048262
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019783744401056822,
        "excess_kurtosis": 5.75053303745597,
        "return_acf_1": -0.16591510599930992,
        "abs_return_acf_1": 0.32707290131634564,
        "abs_return_acf_5": 0.3035128807289241,
        "abs_return_acf_20": 0.29621715620588185,
        "quantile_01": -0.06783687795210233,
        "quantile_99": 0.05682127662905292,
        "hill_tail_index": 3.689001281375139
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.0190877741298932,
        "excess_kurtosis": 20.89031672503088,
        "return_acf_1": -0.13131033610005532,
        "abs_return_acf_1": 0.32058843574003165,
        "abs_return_acf_5": 0.4382180705049263,
        "abs_return_acf_20": 0.2618740862271894,
        "quantile_01": -0.06808756398013066,
        "quantile_99": 0.043066735283395656,
        "hill_tail_index": 1.597969126658495
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01993463731174708,
        "excess_kurtosis": 13.08193585508128,
        "return_acf_1": -0.15362686393204644,
        "abs_return_acf_1": 0.3620539656021156,
        "abs_return_acf_5": 0.31464052351810734,
        "abs_return_acf_20": 0.29424389811627494,
        "quantile_01": -0.058744968368333386,
        "quantile_99": 0.05102073527414936,
        "hill_tail_index": 2.4317038577667835
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.019278852536890226,
        "excess_kurtosis": 9.929958118122835,
        "return_acf_1": -0.11050611399629147,
        "abs_return_acf_1": 0.2958215502993917,
        "abs_return_acf_5": 0.3473874868976884,
        "abs_return_acf_20": 0.31431957551062967,
        "quantile_01": -0.057319048598185866,
        "quantile_99": 0.04495105567933318,
        "hill_tail_index": 2.477629326844443
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.022126270443800628,
        "excess_kurtosis": 8.587186445660748,
        "return_acf_1": -0.15925581155814178,
        "abs_return_acf_1": 0.3930168241677772,
        "abs_return_acf_5": 0.34892507406032036,
        "abs_return_acf_20": 0.3200466106863416,
        "quantile_01": -0.08358853977964541,
        "quantile_99": 0.0614743327360406,
        "hill_tail_index": 3.1721949194999066
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.020657309420625446,
        "excess_kurtosis": 5.721164879029304,
        "return_acf_1": -0.18835220853016774,
        "abs_return_acf_1": 0.3875995367456169,
        "abs_return_acf_5": 0.36538239325550403,
        "abs_return_acf_20": 0.3376449781701794,
        "quantile_01": -0.0690832555530155,
        "quantile_99": 0.05633305080603519,
        "hill_tail_index": 3.940941044324725
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.021469375512046546,
        "excess_kurtosis": 9.642637558950238,
        "return_acf_1": -0.16400381335772052,
        "abs_return_acf_1": 0.3791786034238937,
        "abs_return_acf_5": 0.31371575274546537,
        "abs_return_acf_20": 0.28098979928729517,
        "quantile_01": -0.06867095946260601,
        "quantile_99": 0.0657058362666084,
        "hill_tail_index": 2.561672189904938
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020481265064520904,
        "excess_kurtosis": 9.335256164729206,
        "return_acf_1": -0.10719511126740806,
        "abs_return_acf_1": 0.3970430585625054,
        "abs_return_acf_5": 0.363946465508213,
        "abs_return_acf_20": 0.2972474170927665,
        "quantile_01": -0.07043029861372434,
        "quantile_99": 0.0540666087415818,
        "hill_tail_index": 2.3245414297359854
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020656930009649715,
        "excess_kurtosis": 7.672846111467891,
        "return_acf_1": -0.17680909035271986,
        "abs_return_acf_1": 0.3434419071700392,
        "abs_return_acf_5": 0.2984074834650594,
        "abs_return_acf_20": 0.3465261399122749,
        "quantile_01": -0.06460746630827374,
        "quantile_99": 0.052574460042510075,
        "hill_tail_index": 2.800206465939802
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018395976724674728,
        "excess_kurtosis": 4.29112722520172,
        "return_acf_1": -0.16603977610601464,
        "abs_return_acf_1": 0.28548087231424807,
        "abs_return_acf_5": 0.31915830257056155,
        "abs_return_acf_20": 0.20344882734714892,
        "quantile_01": -0.055902681191877544,
        "quantile_99": 0.052119189258231724,
        "hill_tail_index": 4.1496431993371194
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.021392191618342354,
        "excess_kurtosis": 11.55611090596637,
        "return_acf_1": -0.17486668546927542,
        "abs_return_acf_1": 0.38970538226157075,
        "abs_return_acf_5": 0.3249798725489444,
        "abs_return_acf_20": 0.34393152630477725,
        "quantile_01": -0.065401049551711,
        "quantile_99": 0.07549427142663356,
        "hill_tail_index": 3.004243867342537
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.021261672341208373,
        "excess_kurtosis": 8.206676796783235,
        "return_acf_1": -0.1820913654122948,
        "abs_return_acf_1": 0.41605695539988047,
        "abs_return_acf_5": 0.30385806167276025,
        "abs_return_acf_20": 0.3113842370876167,
        "quantile_01": -0.06766487856199994,
        "quantile_99": 0.06200270390102051,
        "hill_tail_index": 3.2366150844305097
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02236643659474151,
        "excess_kurtosis": 7.717214966881199,
        "return_acf_1": -0.1660144669800295,
        "abs_return_acf_1": 0.46179172751437053,
        "abs_return_acf_5": 0.39957870320326305,
        "abs_return_acf_20": 0.33230605310759753,
        "quantile_01": -0.07265847840990983,
        "quantile_99": 0.07244944501097475,
        "hill_tail_index": 3.4650235291759026
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.02275131910990005,
        "excess_kurtosis": 10.716453207688385,
        "return_acf_1": -0.18225553707488096,
        "abs_return_acf_1": 0.39388585746299576,
        "abs_return_acf_5": 0.3301925810133125,
        "abs_return_acf_20": 0.3198224241606793,
        "quantile_01": -0.0792687576720512,
        "quantile_99": 0.05917079483836537,
        "hill_tail_index": 2.713082168754992
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.023477609090633036,
        "excess_kurtosis": 7.325756882779597,
        "return_acf_1": -0.1560269785158848,
        "abs_return_acf_1": 0.4425316543229775,
        "abs_return_acf_5": 0.3564274652751501,
        "abs_return_acf_20": 0.37735007196564885,
        "quantile_01": -0.08521517278549791,
        "quantile_99": 0.07630654324737236,
        "hill_tail_index": 4.644764424706916
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
