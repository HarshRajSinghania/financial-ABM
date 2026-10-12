# Disclosure-market run

Purpose: serial_reproducibility_check
Domain: esg
Seed: 21001
Run ID: `f116696c419414abf7fdd6d895b2a427a3440d68201c4430b680cbce806fb928`
Result fingerprint: `33a4a98863bed03fc97dda10d47ddeeda6f98ec1d90e5f4de23bbb92ce76cedc`

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
    "equal_weight_sd": 0.31944373947926336,
    "equal_weight_raw": 4.79165609218895,
    "fixed_start_cap_weight_sd": 0.43457441627120885,
    "fixed_start_cap_weight_raw": 6.518616244068132,
    "end_cap_weight_sd": 0.4429253569332602,
    "end_cap_weight_raw": 6.643880353998902
  },
  "full_period_change": {
    "equal_weight_sd": 0.7314654480770937,
    "equal_weight_raw": 10.971981721156405
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": 0.7064280094944225,
    "inflation_mean_sd": 0.09922392687026578
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 1.2718246918602154,
    "equal_weight_raw": 19.077370377903232,
    "fixed_start_cap_weight_sd": 1.3869553686521607,
    "fixed_start_cap_weight_raw": 20.804330529782412,
    "end_cap_weight_sd": 1.3953063093142126,
    "end_cap_weight_raw": 20.929594639713184
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": 0.5405289884996776,
      "change_raw": 8.107934827495164,
      "decay_adjusted_gain_sd": 1.4929099408806301
    },
    "mid": {
      "count": 9,
      "change_sd": 0.4137844913767449,
      "change_raw": 6.206767370651173,
      "decay_adjusted_gain_sd": 1.366165443757697
    },
    "small": {
      "count": 18,
      "change_sd": 0.23542582202712017,
      "change_raw": 3.5313873304068024,
      "decay_adjusted_gain_sd": 1.1878067744080725
    },
    "large_minus_small_sd": 0.3051031664725574,
    "large_minus_small_raw": 4.576547497088361
  },
  "inflation": {
    "initial_mean_sd": 0.06589013465600421,
    "final_mean_sd": 0.09922392687026577,
    "mean_sd": 0.09690064831947254,
    "mean_absolute_raw_gap": 1.453509724792088,
    "final_absolute_raw_gap": 1.4883589030539865,
    "mean_range_fraction": 0.01453509724792088
  },
  "impact": {
    "initial_share": 0.36,
    "final_share": 0.36,
    "initial_wealth_share": 0.296710058262813,
    "final_wealth_share": 0.29829311803407266
  },
  "pricing_slope": {
    "mean": 0.0025757370666194416,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.00000000000001,
    "resource_cost": 0.20965774126396292,
    "real_improvement_cost": 0.20814362668476927,
    "washing_cost": 0.001514114579193635,
    "fine_transfer": 0.020914840314267633,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.23057258157823055,
    "resource_cost_fraction_initial_cap": 0.0069885913754654284,
    "private_net_outflow_fraction_initial_cap": 0.007685752719274349,
    "fine_transfer_fraction_initial_cap": 0.0006971613438089209,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.018093784862226566,
    "unapplied_final_day_resource_cost": 0.008643645821714516
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 181.98584285885704,
    "beneficial_raw_gain_per_resource_cost": 2729.787642882856,
    "undefined_reason": null
  },
  "diagnostics": {
    "status": "ok",
    "missing_size_classes": [],
    "pricing_slope_missing_observations": 0,
    "finite_metrics": true
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
    "maximum_relative_cash_error": 2.2551344614836348e-15,
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
      "minimum": -0.21234744916270012,
      "maximum": 0.06636385725429389,
      "mean": -0.1119195720093334,
      "median": -0.11983273909088471,
      "quantile_05": -0.18528567236158172,
      "quantile_95": -0.04219345737077479
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
      "minimum": 0.2460396963535776,
      "maximum": 0.7665053387679893,
      "mean": 0.4809453397219605,
      "median": 0.45935088757707965,
      "quantile_05": 0.3012790600162528,
      "quantile_95": 0.7083757640654818
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
        "daily_volatility": 0.015698069243887405,
        "excess_kurtosis": 4.765178433099447,
        "return_acf_1": -0.08911685680274417,
        "abs_return_acf_1": 0.2655823008335071,
        "abs_return_acf_5": 0.22469152852129676,
        "abs_return_acf_20": 0.16126768764160815,
        "quantile_01": -0.042300302044801404,
        "quantile_99": 0.03832710941013939,
        "hill_tail_index": 2.986798781068168
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.016643384245921142,
        "excess_kurtosis": 2.773299003908389,
        "return_acf_1": -0.1569768129936233,
        "abs_return_acf_1": 0.21515041025426693,
        "abs_return_acf_5": 0.1869444382821378,
        "abs_return_acf_20": 0.22290313687609126,
        "quantile_01": -0.043442160618455156,
        "quantile_99": 0.04444011162973883,
        "hill_tail_index": 4.3524647231554585
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01624374489395179,
        "excess_kurtosis": 4.75656770704268,
        "return_acf_1": -0.12357760808376748,
        "abs_return_acf_1": 0.2660083071371329,
        "abs_return_acf_5": 0.26614643304330915,
        "abs_return_acf_20": 0.2394589087644886,
        "quantile_01": -0.05381154836776034,
        "quantile_99": 0.044363932063793195,
        "hill_tail_index": 3.827900187842534
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.015825568332811676,
        "excess_kurtosis": 3.0094748332318124,
        "return_acf_1": -0.11825076995276965,
        "abs_return_acf_1": 0.2373737875199747,
        "abs_return_acf_5": 0.21843308860998753,
        "abs_return_acf_20": 0.1664470556052242,
        "quantile_01": -0.049092406046385734,
        "quantile_99": 0.0397849204142963,
        "hill_tail_index": 3.3945904538221683
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01858374129445361,
        "excess_kurtosis": 7.1242809779918606,
        "return_acf_1": -0.14711847474779022,
        "abs_return_acf_1": 0.2704020008788906,
        "abs_return_acf_5": 0.2535477854458764,
        "abs_return_acf_20": 0.2883932023411247,
        "quantile_01": -0.0561009676210068,
        "quantile_99": 0.048885461904373394,
        "hill_tail_index": 3.059445376180644
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.01730445818245638,
        "excess_kurtosis": 6.541679745398614,
        "return_acf_1": -0.08037436679762837,
        "abs_return_acf_1": 0.4009260098578061,
        "abs_return_acf_5": 0.2927895412679853,
        "abs_return_acf_20": 0.3730585471723455,
        "quantile_01": -0.05227543503299128,
        "quantile_99": 0.04321767883344416,
        "hill_tail_index": 2.6943654691919923
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019094401492637608,
        "excess_kurtosis": 11.23603307801072,
        "return_acf_1": -0.12053712850352007,
        "abs_return_acf_1": 0.4812397749216492,
        "abs_return_acf_5": 0.39631158871673594,
        "abs_return_acf_20": 0.39156638524178067,
        "quantile_01": -0.05877866358063672,
        "quantile_99": 0.049474079076408446,
        "hill_tail_index": 2.1933889682379073
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019625788396059857,
        "excess_kurtosis": 13.54391198084695,
        "return_acf_1": 0.06636385725429389,
        "abs_return_acf_1": 0.518710561866644,
        "abs_return_acf_5": 0.4414769512983149,
        "abs_return_acf_20": 0.4622422751703352,
        "quantile_01": -0.06587299082805267,
        "quantile_99": 0.061352651100896494,
        "hill_tail_index": 2.1160632994106794
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.01780648047343216,
        "excess_kurtosis": 6.158242082714308,
        "return_acf_1": -0.12094775811153144,
        "abs_return_acf_1": 0.33635838716118216,
        "abs_return_acf_5": 0.3723391471455501,
        "abs_return_acf_20": 0.26643737075616686,
        "quantile_01": -0.0498675533848352,
        "quantile_99": 0.048295546219523824,
        "hill_tail_index": 2.7866961395689733
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018932862184357132,
        "excess_kurtosis": 4.555609480414235,
        "return_acf_1": -0.16224309771860235,
        "abs_return_acf_1": 0.3066636217696606,
        "abs_return_acf_5": 0.2890520283675161,
        "abs_return_acf_20": 0.2750347793041129,
        "quantile_01": -0.06086795971025232,
        "quantile_99": 0.0538175913647612,
        "hill_tail_index": 4.39981703307208
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017055087969230203,
        "excess_kurtosis": 6.155537522074967,
        "return_acf_1": -0.054577243452883964,
        "abs_return_acf_1": 0.3457840248946908,
        "abs_return_acf_5": 0.3016099748248054,
        "abs_return_acf_20": 0.2878252847235321,
        "quantile_01": -0.050957075365183443,
        "quantile_99": 0.0468650211651465,
        "hill_tail_index": 3.3980041267201124
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.0159562245416843,
        "excess_kurtosis": 2.7556306779984103,
        "return_acf_1": -0.14577160980321366,
        "abs_return_acf_1": 0.2529503304403062,
        "abs_return_acf_5": 0.1828884837024954,
        "abs_return_acf_20": 0.1749187913276458,
        "quantile_01": -0.04433426655375492,
        "quantile_99": 0.044111110121420806,
        "hill_tail_index": 4.5657381558021575
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.01722356940162758,
        "excess_kurtosis": 3.606910152989026,
        "return_acf_1": -0.12099926196296931,
        "abs_return_acf_1": 0.3907806306516175,
        "abs_return_acf_5": 0.29111911966707027,
        "abs_return_acf_20": 0.2714080610011984,
        "quantile_01": -0.05072296154811904,
        "quantile_99": 0.04265937717205679,
        "hill_tail_index": 3.969955027278639
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01779361330548799,
        "excess_kurtosis": 2.5434236291003174,
        "return_acf_1": -0.11912834967824934,
        "abs_return_acf_1": 0.25911910205680966,
        "abs_return_acf_5": 0.21614221209877885,
        "abs_return_acf_20": 0.2043859615917536,
        "quantile_01": -0.05085476130770415,
        "quantile_99": 0.04908223328517533,
        "hill_tail_index": 4.829570237183596
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01734058900373519,
        "excess_kurtosis": 2.9008777030851087,
        "return_acf_1": -0.14042194960472243,
        "abs_return_acf_1": 0.27933333785679193,
        "abs_return_acf_5": 0.2394913585591879,
        "abs_return_acf_20": 0.15541588871526804,
        "quantile_01": -0.053630123153875706,
        "quantile_99": 0.04355745359574692,
        "hill_tail_index": 4.392620217008856
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.016442819719998697,
        "excess_kurtosis": 1.9242276062907893,
        "return_acf_1": -0.16360692206316577,
        "abs_return_acf_1": 0.20458954704725765,
        "abs_return_acf_5": 0.1909057416372036,
        "abs_return_acf_20": 0.17366669712313265,
        "quantile_01": -0.042241799559569436,
        "quantile_99": 0.045764474162719386,
        "hill_tail_index": 4.85499673903596
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.01832547093481345,
        "excess_kurtosis": 10.93806603021501,
        "return_acf_1": -0.08604984020485308,
        "abs_return_acf_1": 0.46929277492215515,
        "abs_return_acf_5": 0.4454490191078999,
        "abs_return_acf_20": 0.3880673233378846,
        "quantile_01": -0.059063186826059134,
        "quantile_99": 0.043811854471675404,
        "hill_tail_index": 2.2984426108534106
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.02021337508850406,
        "excess_kurtosis": 22.804103881806945,
        "return_acf_1": -0.20302283169664934,
        "abs_return_acf_1": 0.36615788348842254,
        "abs_return_acf_5": 0.2786909540789514,
        "abs_return_acf_20": 0.2505763020650347,
        "quantile_01": -0.054405956565459664,
        "quantile_99": 0.055246255978301205,
        "hill_tail_index": 3.1129000975429855
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.018690455903936448,
        "excess_kurtosis": 9.585050705276123,
        "return_acf_1": -0.11803581230499352,
        "abs_return_acf_1": 0.3667881545278033,
        "abs_return_acf_5": 0.293567829741426,
        "abs_return_acf_20": 0.21314942582117577,
        "quantile_01": -0.0499069181214709,
        "quantile_99": 0.04740481896660098,
        "hill_tail_index": 3.0241076009232954
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019528040868614444,
        "excess_kurtosis": 12.211866671045874,
        "return_acf_1": -0.12144667568045808,
        "abs_return_acf_1": 0.5109311772463578,
        "abs_return_acf_5": 0.44999501179064355,
        "abs_return_acf_20": 0.44657819965062934,
        "quantile_01": -0.07128172705165524,
        "quantile_99": 0.055337753483800795,
        "hill_tail_index": 2.8166056175777787
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01920478517463773,
        "excess_kurtosis": 11.4317693512129,
        "return_acf_1": -0.08667217011291288,
        "abs_return_acf_1": 0.4912300340939331,
        "abs_return_acf_5": 0.454359872190124,
        "abs_return_acf_20": 0.4448769470900729,
        "quantile_01": -0.07479683929675254,
        "quantile_99": 0.06083683707573933,
        "hill_tail_index": 3.2591982574568363
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017210952587109276,
        "excess_kurtosis": 4.777628866623906,
        "return_acf_1": -0.048866188171960166,
        "abs_return_acf_1": 0.3094129806330547,
        "abs_return_acf_5": 0.2907657803551123,
        "abs_return_acf_20": 0.2845181933809272,
        "quantile_01": -0.051359470751322224,
        "quantile_99": 0.04708779941626245,
        "hill_tail_index": 3.171699213241613
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.01651737598739666,
        "excess_kurtosis": 7.058905325643952,
        "return_acf_1": -0.08491027904621237,
        "abs_return_acf_1": 0.33587113074438524,
        "abs_return_acf_5": 0.3077738334290222,
        "abs_return_acf_20": 0.2436780669264543,
        "quantile_01": -0.04706081755203048,
        "quantile_99": 0.044004182082608596,
        "hill_tail_index": 3.0138818590628746
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.017348454840683515,
        "excess_kurtosis": 3.982378106773118,
        "return_acf_1": -0.21234744916270012,
        "abs_return_acf_1": 0.3379175436226747,
        "abs_return_acf_5": 0.2786492033538159,
        "abs_return_acf_20": 0.26785374617243485,
        "quantile_01": -0.05271614589116243,
        "quantile_99": 0.057657087033903,
        "hill_tail_index": 4.075970718377414
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01926554279152741,
        "excess_kurtosis": 9.088097750698843,
        "return_acf_1": -0.04718035944013904,
        "abs_return_acf_1": 0.5178372952647472,
        "abs_return_acf_5": 0.4211101462026476,
        "abs_return_acf_20": 0.3131170523145908,
        "quantile_01": -0.07020268105258926,
        "quantile_99": 0.05768669042012498,
        "hill_tail_index": 3.1680963793383654
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.017394710282258037,
        "excess_kurtosis": 3.6154127870626587,
        "return_acf_1": -0.15428806822252553,
        "abs_return_acf_1": 0.2741349159130254,
        "abs_return_acf_5": 0.27515335485238673,
        "abs_return_acf_20": 0.2121221791733829,
        "quantile_01": -0.05195362594136899,
        "quantile_99": 0.04666886326294419,
        "hill_tail_index": 3.879825074237809
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019956592740665177,
        "excess_kurtosis": 9.771355403888572,
        "return_acf_1": -0.13930637575949267,
        "abs_return_acf_1": 0.38587631597079497,
        "abs_return_acf_5": 0.3285983298332465,
        "abs_return_acf_20": 0.36941343243576097,
        "quantile_01": -0.060795637907817654,
        "quantile_99": 0.054550244722750676,
        "hill_tail_index": 2.9579245261559457
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01867232255023382,
        "excess_kurtosis": 3.801169675887956,
        "return_acf_1": -0.10455441715596528,
        "abs_return_acf_1": 0.3681253648593265,
        "abs_return_acf_5": 0.359829130703804,
        "abs_return_acf_20": 0.3433026027541619,
        "quantile_01": -0.0567699602758664,
        "quantile_99": 0.05081326597073532,
        "hill_tail_index": 5.0860727227470806
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019042601766516568,
        "excess_kurtosis": 3.8035760044334754,
        "return_acf_1": -0.11550907552968522,
        "abs_return_acf_1": 0.3438939582944085,
        "abs_return_acf_5": 0.3273516600371267,
        "abs_return_acf_20": 0.30903452411873455,
        "quantile_01": -0.05815344678793435,
        "quantile_99": 0.05642447797127404,
        "hill_tail_index": 5.197303094359143
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.016604399834693584,
        "excess_kurtosis": 6.988127089470071,
        "return_acf_1": -0.03811326476856763,
        "abs_return_acf_1": 0.33825851156168735,
        "abs_return_acf_5": 0.33934299823810254,
        "abs_return_acf_20": 0.2620570059946576,
        "quantile_01": -0.04455481769899677,
        "quantile_99": 0.04194120454976447,
        "hill_tail_index": 2.753688377134805
      }
    }
  ],
  "empirical_calibration": {
    "status": "pending",
    "reason": "This validator does not evaluate held-out empirical targets."
  }
}
```
