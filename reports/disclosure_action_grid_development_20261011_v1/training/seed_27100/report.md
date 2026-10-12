# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27100
Run ID: `f9c3096cf62e74d058c51e2e289ee78ef82202fa73f239e107b1adb5bce9db07`
Result fingerprint: `57f23e28e52d4faf21d16a148ee2b199046b8272f2f213d0dd1e872c6b6cd750`

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
    "equal_weight_sd": -0.6315476190476157,
    "equal_weight_raw": -9.47321428571424,
    "fixed_start_cap_weight_sd": -0.6484367366873464,
    "fixed_start_cap_weight_raw": -9.726551050310194,
    "end_cap_weight_sd": -0.6481590550720462,
    "end_cap_weight_raw": -9.722385826080695
  },
  "full_period_change": {
    "equal_weight_sd": -0.9574047619047571,
    "equal_weight_raw": -14.361071428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9113938492063446,
    "inflation_mean_sd": 0.5907976190476191
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.32083333333333663,
    "equal_weight_raw": 4.812500000000047,
    "fixed_start_cap_weight_sd": 0.30394421569360597,
    "fixed_start_cap_weight_raw": 4.55916323540409,
    "end_cap_weight_sd": 0.30422189730890603,
    "end_cap_weight_raw": 4.563328459633591
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.7432142857142824,
      "change_raw": -11.148214285714236,
      "decay_adjusted_gain_sd": 0.20916666666666997
    },
    "mid": {
      "count": 9,
      "change_sd": -0.49765873015872675,
      "change_raw": -7.464880952380901,
      "decay_adjusted_gain_sd": 0.4547222222222255
    },
    "small": {
      "count": 18,
      "change_sd": -0.6798809523809491,
      "change_raw": -10.198214285714236,
      "decay_adjusted_gain_sd": 0.2725000000000032
    },
    "large_minus_small_sd": -0.06333333333333324,
    "large_minus_small_raw": -0.9499999999999986
  },
  "inflation": {
    "initial_mean_sd": 0.26983333333333337,
    "final_mean_sd": 0.6169166666666666,
    "mean_sd": 0.4534612128781571,
    "mean_absolute_raw_gap": 6.801918193172356,
    "final_absolute_raw_gap": 9.25375,
    "mean_range_fraction": 0.06801918193172356
  },
  "impact": {
    "initial_share": 0.23333333333333334,
    "final_share": 0.21333333333333335,
    "initial_wealth_share": 0.23463571847696837,
    "final_wealth_share": 0.21767941732828844
  },
  "pricing_slope": {
    "mean": -0.0008478551602825997,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.10129077530074014,
    "real_improvement_cost": 0.07712607893378558,
    "washing_cost": 0.024164696366954546,
    "fine_transfer": 0.008359754101026552,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.1096505294017667,
    "resource_cost_fraction_initial_cap": 0.003376359176691337,
    "private_net_outflow_fraction_initial_cap": 0.003655017646725556,
    "fine_transfer_fraction_initial_cap": 0.00027865847003421835,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0004019775728271491,
    "unapplied_final_day_resource_cost": 0.0014734613077190988
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 95.02346064014942,
    "beneficial_raw_gain_per_resource_cost": 1425.3519096022412,
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
    "accrued_cost": 2.84758986686168,
    "baseline_accrued_cost": 2.976190476190478,
    "value_adjustment": 0.12860060932879758,
    "accrued_cost_fraction_initial_cap": 0.09491966222872264,
    "mean_contract_rate": 0.03974999443429279,
    "maximum_ledger_error": 7.453889935837843e-20
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
    "price_cap_hits": 22,
    "maximum_relative_cash_error": 1.0255664472162922e-15,
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
      "minimum": -0.20373588258310618,
      "maximum": -0.0758291474283688,
      "mean": -0.14477352799039958,
      "median": -0.14690919300898442,
      "quantile_05": -0.19477399297533524,
      "quantile_95": -0.09331051543578552
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
      "minimum": 0.2810193530210893,
      "maximum": 0.7915976130366655,
      "mean": 0.6257927680935985,
      "median": 0.6888545395779071,
      "quantile_05": 0.33538978400222347,
      "quantile_95": 0.7538372389116816
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
        "daily_volatility": 0.019655631174997266,
        "excess_kurtosis": 7.449145408397877,
        "return_acf_1": -0.14274656634948116,
        "abs_return_acf_1": 0.32802242335421705,
        "abs_return_acf_5": 0.38013052882138687,
        "abs_return_acf_20": 0.30254447634311854,
        "quantile_01": -0.058201844191399746,
        "quantile_99": 0.05509294421784017,
        "hill_tail_index": 3.745459838186499
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.017698286936773937,
        "excess_kurtosis": 4.31938920697164,
        "return_acf_1": -0.12337767322382409,
        "abs_return_acf_1": 0.24211807619295797,
        "abs_return_acf_5": 0.28291654619419454,
        "abs_return_acf_20": 0.2360416078930692,
        "quantile_01": -0.054944156733970274,
        "quantile_99": 0.05108124573957011,
        "hill_tail_index": 4.209658758005907
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.018381757741340966,
        "excess_kurtosis": 6.636848637491369,
        "return_acf_1": -0.14873259429250618,
        "abs_return_acf_1": 0.28301562664290336,
        "abs_return_acf_5": 0.27105541208790523,
        "abs_return_acf_20": 0.26825742440984235,
        "quantile_01": -0.05473383752905618,
        "quantile_99": 0.04268827250986913,
        "hill_tail_index": 2.523301331791496
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.018259864246955183,
        "excess_kurtosis": 5.65807369718579,
        "return_acf_1": -0.09590952617582517,
        "abs_return_acf_1": 0.3943815579941457,
        "abs_return_acf_5": 0.40832633748796926,
        "abs_return_acf_20": 0.29645973507023293,
        "quantile_01": -0.05821819046777778,
        "quantile_99": 0.05245372268278523,
        "hill_tail_index": 3.334525281021504
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020330200866378566,
        "excess_kurtosis": 10.610561506863741,
        "return_acf_1": -0.14328713062182905,
        "abs_return_acf_1": 0.3769038164882761,
        "abs_return_acf_5": 0.34059093353016306,
        "abs_return_acf_20": 0.2488323931363403,
        "quantile_01": -0.06799357826208251,
        "quantile_99": 0.05759400711981062,
        "hill_tail_index": 2.9916702228263214
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01921186493565677,
        "excess_kurtosis": 8.36172061051666,
        "return_acf_1": -0.09118405210302577,
        "abs_return_acf_1": 0.3723224614607959,
        "abs_return_acf_5": 0.4270202957073098,
        "abs_return_acf_20": 0.3445572824705684,
        "quantile_01": -0.0703458450544582,
        "quantile_99": 0.05666135836963769,
        "hill_tail_index": 3.2213621429072985
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019194903418464204,
        "excess_kurtosis": 12.471314205216196,
        "return_acf_1": -0.17932717183887756,
        "abs_return_acf_1": 0.45629203883356245,
        "abs_return_acf_5": 0.46743596719260594,
        "abs_return_acf_20": 0.3894039510090665,
        "quantile_01": -0.06681202523085729,
        "quantile_99": 0.05742873349518348,
        "hill_tail_index": 2.3319173015625583
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01984479706751117,
        "excess_kurtosis": 12.358930351154838,
        "return_acf_1": -0.20373588258310618,
        "abs_return_acf_1": 0.37518901881919103,
        "abs_return_acf_5": 0.38185255629332204,
        "abs_return_acf_20": 0.3301250431953985,
        "quantile_01": -0.06868297920869863,
        "quantile_99": 0.050421040653248574,
        "hill_tail_index": 2.2012850114473337
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019787793388487702,
        "excess_kurtosis": 9.788024342886239,
        "return_acf_1": -0.10047582253613403,
        "abs_return_acf_1": 0.3154137807267951,
        "abs_return_acf_5": 0.34942087218056034,
        "abs_return_acf_20": 0.26309822282905065,
        "quantile_01": -0.06501442569405555,
        "quantile_99": 0.051079774943393906,
        "hill_tail_index": 2.815908849620228
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.020301245490823096,
        "excess_kurtosis": 13.174672431183563,
        "return_acf_1": -0.17789967549852403,
        "abs_return_acf_1": 0.315466041350573,
        "abs_return_acf_5": 0.3795824639054744,
        "abs_return_acf_20": 0.26132314007026197,
        "quantile_01": -0.06817422261571308,
        "quantile_99": 0.059817741071417,
        "hill_tail_index": 3.094231726577058
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.019350358883673556,
        "excess_kurtosis": 13.112530639679505,
        "return_acf_1": -0.17759732098231348,
        "abs_return_acf_1": 0.2954820267268635,
        "abs_return_acf_5": 0.3468137972746677,
        "abs_return_acf_20": 0.3357044172841225,
        "quantile_01": -0.061175185500480546,
        "quantile_99": 0.04917636528054844,
        "hill_tail_index": 2.3652544127398754
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01898167145247486,
        "excess_kurtosis": 10.039950222528592,
        "return_acf_1": -0.1471213104217738,
        "abs_return_acf_1": 0.3787185512981953,
        "abs_return_acf_5": 0.41418532230631494,
        "abs_return_acf_20": 0.3941660560769298,
        "quantile_01": -0.06491109715757176,
        "quantile_99": 0.04363854185402648,
        "hill_tail_index": 3.0786085291084695
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01985631478027263,
        "excess_kurtosis": 4.991490138504361,
        "return_acf_1": -0.18923620738480237,
        "abs_return_acf_1": 0.31754639915737315,
        "abs_return_acf_5": 0.38468283304525763,
        "abs_return_acf_20": 0.30524999952636306,
        "quantile_01": -0.06561214881372161,
        "quantile_99": 0.05275971400085385,
        "hill_tail_index": 3.8532870700847
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.019436776267387833,
        "excess_kurtosis": 9.684491916868291,
        "return_acf_1": -0.17155827034349297,
        "abs_return_acf_1": 0.3695607949932081,
        "abs_return_acf_5": 0.3714286530346439,
        "abs_return_acf_20": 0.3495592727387248,
        "quantile_01": -0.06586870232020903,
        "quantile_99": 0.05340669956667561,
        "hill_tail_index": 2.7038327536837587
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01990571823726898,
        "excess_kurtosis": 5.875744913361023,
        "return_acf_1": -0.1746070916169736,
        "abs_return_acf_1": 0.3608779649439037,
        "abs_return_acf_5": 0.37114307589464607,
        "abs_return_acf_20": 0.29601435885123945,
        "quantile_01": -0.07363649223979869,
        "quantile_99": 0.059731575275509,
        "hill_tail_index": 4.158696843404764
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.019125632845358138,
        "excess_kurtosis": 9.72516651352422,
        "return_acf_1": -0.14704008373581495,
        "abs_return_acf_1": 0.3017765807459307,
        "abs_return_acf_5": 0.346635160049634,
        "abs_return_acf_20": 0.2919042822814764,
        "quantile_01": -0.07145738526378423,
        "quantile_99": 0.05076278891640067,
        "hill_tail_index": 2.4937109711843943
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.016301901145011875,
        "excess_kurtosis": 4.330128416077061,
        "return_acf_1": -0.11199039726840339,
        "abs_return_acf_1": 0.25797444243580425,
        "abs_return_acf_5": 0.24979349730467557,
        "abs_return_acf_20": 0.1995817694695301,
        "quantile_01": -0.045847844936662725,
        "quantile_99": 0.04498777300006151,
        "hill_tail_index": 3.7047504775845033
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01987602619293097,
        "excess_kurtosis": 6.5985556494227815,
        "return_acf_1": -0.15937775157630216,
        "abs_return_acf_1": 0.3689839607176613,
        "abs_return_acf_5": 0.40448881702498257,
        "abs_return_acf_20": 0.2546185673634744,
        "quantile_01": -0.07259224614226692,
        "quantile_99": 0.05634912756679716,
        "hill_tail_index": 4.420631737368705
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02148680951953921,
        "excess_kurtosis": 7.6549413869902665,
        "return_acf_1": -0.14533884311030146,
        "abs_return_acf_1": 0.3874686267362202,
        "abs_return_acf_5": 0.4162636989351697,
        "abs_return_acf_20": 0.369264483286921,
        "quantile_01": -0.08038574999525414,
        "quantile_99": 0.06932545929714926,
        "hill_tail_index": 4.029632430680065
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01823907503977778,
        "excess_kurtosis": 4.087414618661619,
        "return_acf_1": -0.1212869298257575,
        "abs_return_acf_1": 0.23157506750137466,
        "abs_return_acf_5": 0.29758806870069554,
        "abs_return_acf_20": 0.25582358670495875,
        "quantile_01": -0.05317384981927283,
        "quantile_99": 0.049470190503896234,
        "hill_tail_index": 3.6475529348090143
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017411965482031982,
        "excess_kurtosis": 3.9391225441201643,
        "return_acf_1": -0.14155597245080026,
        "abs_return_acf_1": 0.3106880087436188,
        "abs_return_acf_5": 0.3158676459660232,
        "abs_return_acf_20": 0.2320855174517866,
        "quantile_01": -0.05607795975734466,
        "quantile_99": 0.05012089642446016,
        "hill_tail_index": 4.519594946408792
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.0217936421236602,
        "excess_kurtosis": 20.301217073536876,
        "return_acf_1": -0.14677830228215386,
        "abs_return_acf_1": 0.40702488678099175,
        "abs_return_acf_5": 0.42094613938971076,
        "abs_return_acf_20": 0.2542819613493195,
        "quantile_01": -0.08382923562841528,
        "quantile_99": 0.06113155356029486,
        "hill_tail_index": 2.2470587116586325
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01889292296945604,
        "excess_kurtosis": 7.444453072983125,
        "return_acf_1": -0.15606297267844269,
        "abs_return_acf_1": 0.3451423513817105,
        "abs_return_acf_5": 0.3870849139413058,
        "abs_return_acf_20": 0.3458999411966551,
        "quantile_01": -0.06220588654495063,
        "quantile_99": 0.049402089160580455,
        "hill_tail_index": 3.458351660830907
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.019390694875939057,
        "excess_kurtosis": 12.253817425088464,
        "return_acf_1": -0.15423388744908006,
        "abs_return_acf_1": 0.32873970213325426,
        "abs_return_acf_5": 0.3357279055421881,
        "abs_return_acf_20": 0.2625546769944274,
        "quantile_01": -0.07055622534209204,
        "quantile_99": 0.04509198954776505,
        "hill_tail_index": 2.9011723547186454
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.018562779132613172,
        "excess_kurtosis": 22.579066359350847,
        "return_acf_1": -0.10022851951308161,
        "abs_return_acf_1": 0.5181981755777766,
        "abs_return_acf_5": 0.47804828420853074,
        "abs_return_acf_20": 0.33429680246486504,
        "quantile_01": -0.04917068607016628,
        "quantile_99": 0.03614774802531038,
        "hill_tail_index": 1.4965039829384645
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.0186614834680099,
        "excess_kurtosis": 6.910869605533547,
        "return_acf_1": -0.14986068290239252,
        "abs_return_acf_1": 0.32116312996009255,
        "abs_return_acf_5": 0.4069679349144684,
        "abs_return_acf_20": 0.301249149294387,
        "quantile_01": -0.06049217918712743,
        "quantile_99": 0.04967876257445821,
        "hill_tail_index": 3.586933956280664
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01932579345694712,
        "excess_kurtosis": 7.179384067709732,
        "return_acf_1": -0.12452518719793071,
        "abs_return_acf_1": 0.3537162695622953,
        "abs_return_acf_5": 0.3925596904644145,
        "abs_return_acf_20": 0.3033642781035458,
        "quantile_01": -0.06897920186496853,
        "quantile_99": 0.05652183020409468,
        "hill_tail_index": 3.262592456312107
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.018790157545919495,
        "excess_kurtosis": 6.759191831253775,
        "return_acf_1": -0.1993049084584985,
        "abs_return_acf_1": 0.35696455251731696,
        "abs_return_acf_5": 0.3169522930934496,
        "abs_return_acf_20": 0.2926685080100092,
        "quantile_01": -0.06202661356106549,
        "quantile_99": 0.0470297426372539,
        "hill_tail_index": 2.818217905012398
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020021750491810233,
        "excess_kurtosis": 11.737344283568047,
        "return_acf_1": -0.0758291474283688,
        "abs_return_acf_1": 0.3951405616398356,
        "abs_return_acf_5": 0.3712819535850734,
        "abs_return_acf_20": 0.2676149145878538,
        "quantile_01": -0.07107064715415623,
        "quantile_99": 0.051972693793643145,
        "hill_tail_index": 2.6737618486044017
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.0187097629772843,
        "excess_kurtosis": 8.611525427096252,
        "return_acf_1": -0.14299595786216934,
        "abs_return_acf_1": 0.33153747582398835,
        "abs_return_acf_5": 0.3860965201751579,
        "abs_return_acf_20": 0.22528753203402585,
        "quantile_01": -0.0652779572609835,
        "quantile_99": 0.04679570598412381,
        "hill_tail_index": 2.609907727605238
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
