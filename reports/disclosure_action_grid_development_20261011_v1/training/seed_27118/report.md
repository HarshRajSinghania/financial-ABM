# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27118
Run ID: `ad15e71bb629432c79cf974110791eecf55fa64bfb4bc5bfd47ebf78623552b8`
Result fingerprint: `8a950dfe9a507a5936de7ce7f4d168e835ddec78e1fa97a95d67570c5eaee7bb`

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
    "equal_weight_sd": -0.665368477232539,
    "equal_weight_raw": -9.980527158488085,
    "fixed_start_cap_weight_sd": -0.6259186733149827,
    "fixed_start_cap_weight_raw": -9.38878009972474,
    "end_cap_weight_sd": -0.6132459045012156,
    "end_cap_weight_raw": -9.198688567518234
  },
  "full_period_change": {
    "equal_weight_sd": -1.0405589534230135,
    "equal_weight_raw": -15.608384301345202
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.9850467022262387,
    "inflation_mean_sd": 0.6672103174603174
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2771666666666697,
    "equal_weight_raw": 4.157500000000046,
    "fixed_start_cap_weight_sd": 0.31807705617860593,
    "fixed_start_cap_weight_raw": 4.771155842679089,
    "end_cap_weight_sd": 0.33346195952008895,
    "end_cap_weight_raw": 5.001929392801335
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5507142857142824,
      "change_raw": -8.260714285714236,
      "decay_adjusted_gain_sd": 0.40166666666667
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6542838129973595,
      "change_raw": -9.814257194960392,
      "decay_adjusted_gain_sd": 0.26527777777778055
    },
    "small": {
      "count": 18,
      "change_sd": -0.6900198412698381,
      "change_raw": -10.350297619047572,
      "decay_adjusted_gain_sd": 0.26236111111111426
    },
    "large_minus_small_sd": 0.13930555555555568,
    "large_minus_small_raw": 2.0895833333333353
  },
  "inflation": {
    "initial_mean_sd": 0.2529166666666667,
    "final_mean_sd": 0.7323333333333331,
    "mean_sd": 0.4538501248959201,
    "mean_absolute_raw_gap": 6.807751873438801,
    "final_absolute_raw_gap": 10.985000000000001,
    "mean_range_fraction": 0.06807751873438801
  },
  "impact": {
    "initial_share": 0.24,
    "final_share": 0.23333333333333334,
    "initial_wealth_share": 0.16117492689255153,
    "final_wealth_share": 0.16784788207153675
  },
  "pricing_slope": {
    "mean": -0.0012958597981906855,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.07657378774623268,
    "real_improvement_cost": 0.05618203180123808,
    "washing_cost": 0.020391755944994604,
    "fine_transfer": 0.011224959972806467,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08779874771903914,
    "resource_cost_fraction_initial_cap": 0.002552459591541089,
    "private_net_outflow_fraction_initial_cap": 0.002926624923967971,
    "fine_transfer_fraction_initial_cap": 0.00037416533242688217,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0028604082767921778,
    "unapplied_final_day_resource_cost": 0.00604155201317862
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 108.5880722990509,
    "beneficial_raw_gain_per_resource_cost": 1628.8210844857635,
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
    "accrued_cost": 2.9694505408410223,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.006739935349454586,
    "accrued_cost_fraction_initial_cap": 0.09898168469470073,
    "mean_contract_rate": 0.042709144066817396,
    "maximum_ledger_error": 7.104488845095444e-20
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
    "price_cap_hits": 5,
    "maximum_relative_cash_error": 3.699508028045818e-15,
    "maximum_absolute_share_error": 2.1094237467877974e-15,
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
      "minimum": -0.15032422856275182,
      "maximum": 0.13302792559972776,
      "mean": -0.03247434789868528,
      "median": -0.041156349468878375,
      "quantile_05": -0.13215737145969245,
      "quantile_95": 0.07864168856763275
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
      "minimum": 0.1762601420770639,
      "maximum": 0.8559151154715791,
      "mean": 0.7500458590333375,
      "median": 0.7918860393760466,
      "quantile_05": 0.2653537756700992,
      "quantile_95": 0.8368512769879081
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
        "daily_volatility": 0.022528492257642266,
        "excess_kurtosis": 27.756324417668104,
        "return_acf_1": 0.07946974410953545,
        "abs_return_acf_1": 0.44785807814617934,
        "abs_return_acf_5": 0.47564133331229635,
        "abs_return_acf_20": 0.34512384451357647,
        "quantile_01": -0.07586591786444602,
        "quantile_99": 0.04929400561667763,
        "hill_tail_index": 1.746624862388119
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.021073533170298805,
        "excess_kurtosis": 15.388975929132776,
        "return_acf_1": -0.11601356069828173,
        "abs_return_acf_1": 0.3349114899145915,
        "abs_return_acf_5": 0.38766291429952937,
        "abs_return_acf_20": 0.33447329688336624,
        "quantile_01": -0.08088547597562488,
        "quantile_99": 0.05404893459663933,
        "hill_tail_index": 1.9596629292308823
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.022005697085406315,
        "excess_kurtosis": 20.919397728317485,
        "return_acf_1": -0.10130071175905477,
        "abs_return_acf_1": 0.3723478003099413,
        "abs_return_acf_5": 0.43960515546278445,
        "abs_return_acf_20": 0.3636811446561325,
        "quantile_01": -0.08856594139463686,
        "quantile_99": 0.049345099260639944,
        "hill_tail_index": 1.5063716209615199
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.0209319584319326,
        "excess_kurtosis": 21.85985927687545,
        "return_acf_1": -0.0576272299951798,
        "abs_return_acf_1": 0.40571874713835154,
        "abs_return_acf_5": 0.4643931727167229,
        "abs_return_acf_20": 0.3739572333149724,
        "quantile_01": -0.07361552887298756,
        "quantile_99": 0.053303410715752834,
        "hill_tail_index": 2.133031754806289
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.020804153784497688,
        "excess_kurtosis": 29.83139933967074,
        "return_acf_1": 0.04143282923804316,
        "abs_return_acf_1": 0.36267616562060767,
        "abs_return_acf_5": 0.4004892658228979,
        "abs_return_acf_20": 0.30932139365015787,
        "quantile_01": -0.06554364104880507,
        "quantile_99": 0.049823033872913244,
        "hill_tail_index": 1.7069116878417625
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.022495643017778295,
        "excess_kurtosis": 17.752745674905878,
        "return_acf_1": -0.1453659439008467,
        "abs_return_acf_1": 0.4559530639430257,
        "abs_return_acf_5": 0.4950914741245706,
        "abs_return_acf_20": 0.4277458316817694,
        "quantile_01": -0.11483745009424441,
        "quantile_99": 0.05465091930282854,
        "hill_tail_index": 1.6749002731763891
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.019829206726416807,
        "excess_kurtosis": 22.452090407146017,
        "return_acf_1": 0.036172230074324956,
        "abs_return_acf_1": 0.31617832724916844,
        "abs_return_acf_5": 0.3393904046804765,
        "abs_return_acf_20": 0.3658890885568323,
        "quantile_01": -0.05695199569798607,
        "quantile_99": 0.04731477059066553,
        "hill_tail_index": 2.0624497050496404
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018621378292516828,
        "excess_kurtosis": 10.582144917800536,
        "return_acf_1": -0.07267620867101662,
        "abs_return_acf_1": 0.3533969311220597,
        "abs_return_acf_5": 0.3499790829991987,
        "abs_return_acf_20": 0.34584397406364503,
        "quantile_01": -0.059485093853458126,
        "quantile_99": 0.04980996107745348,
        "hill_tail_index": 3.1735800233837543
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.0225274960404283,
        "excess_kurtosis": 30.80725135519924,
        "return_acf_1": 0.07762962068308502,
        "abs_return_acf_1": 0.36813954752351025,
        "abs_return_acf_5": 0.3959003380997564,
        "abs_return_acf_20": 0.2701961557945597,
        "quantile_01": -0.0776425212436398,
        "quantile_99": 0.047450039346695116,
        "hill_tail_index": 1.6884642084128938
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.022138608755579516,
        "excess_kurtosis": 22.899248141461022,
        "return_acf_1": -0.024251506959831193,
        "abs_return_acf_1": 0.44411155612263603,
        "abs_return_acf_5": 0.4664337665620398,
        "abs_return_acf_20": 0.4050763135850753,
        "quantile_01": -0.08964535381585483,
        "quantile_99": 0.0529111663715001,
        "hill_tail_index": 1.7680153038187343
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01995686354935165,
        "excess_kurtosis": 23.90168929762631,
        "return_acf_1": -0.02840504751132853,
        "abs_return_acf_1": 0.4023183985308432,
        "abs_return_acf_5": 0.48788554173962384,
        "abs_return_acf_20": 0.34185310058605617,
        "quantile_01": -0.063367904520756,
        "quantile_99": 0.047113780494291255,
        "hill_tail_index": 1.8734643923283758
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.022609978142908802,
        "excess_kurtosis": 37.62453572737637,
        "return_acf_1": 0.005553755551689878,
        "abs_return_acf_1": 0.35730684130889406,
        "abs_return_acf_5": 0.356196732755569,
        "abs_return_acf_20": 0.2855035868235394,
        "quantile_01": -0.07761183992942497,
        "quantile_99": 0.049049828905592355,
        "hill_tail_index": 1.410012857943587
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017712960020012495,
        "excess_kurtosis": 20.237258622162692,
        "return_acf_1": -0.11346881198703031,
        "abs_return_acf_1": 0.31395209094669285,
        "abs_return_acf_5": 0.24043937313868782,
        "abs_return_acf_20": 0.23864932225439214,
        "quantile_01": -0.04005748377487766,
        "quantile_99": 0.04650376974660725,
        "hill_tail_index": 2.5631222186477736
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.022828514313842335,
        "excess_kurtosis": 26.296745998021652,
        "return_acf_1": -0.0010960931351533412,
        "abs_return_acf_1": 0.37322874622015456,
        "abs_return_acf_5": 0.41463199507309384,
        "abs_return_acf_20": 0.34506001955071886,
        "quantile_01": -0.0826199163431668,
        "quantile_99": 0.05486340932237261,
        "hill_tail_index": 1.6795763983909242
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.021110335140809743,
        "excess_kurtosis": 23.32021053875845,
        "return_acf_1": -0.09499849818215376,
        "abs_return_acf_1": 0.4327649415318201,
        "abs_return_acf_5": 0.43335992713325117,
        "abs_return_acf_20": 0.3880920880712074,
        "quantile_01": -0.07196659563546841,
        "quantile_99": 0.0482405049337941,
        "hill_tail_index": 1.6735259716102422
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02223215984428518,
        "excess_kurtosis": 24.06576577535976,
        "return_acf_1": -0.04721907390967896,
        "abs_return_acf_1": 0.3456272084524179,
        "abs_return_acf_5": 0.4110393727616396,
        "abs_return_acf_20": 0.3784403792126911,
        "quantile_01": -0.08634586946014523,
        "quantile_99": 0.051012783239195794,
        "hill_tail_index": 1.542189636754577
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.022036582624857356,
        "excess_kurtosis": 24.119923509120284,
        "return_acf_1": -0.06060997150593957,
        "abs_return_acf_1": 0.472562867220794,
        "abs_return_acf_5": 0.42828410491707997,
        "abs_return_acf_20": 0.34927781897045374,
        "quantile_01": -0.07472801945051145,
        "quantile_99": 0.05216103247588165,
        "hill_tail_index": 1.7504155366992415
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.023345992363953322,
        "excess_kurtosis": 24.28546603551702,
        "return_acf_1": -0.05019256452108184,
        "abs_return_acf_1": 0.40575899339285126,
        "abs_return_acf_5": 0.42880200651834455,
        "abs_return_acf_20": 0.36420956844620533,
        "quantile_01": -0.09783399145307928,
        "quantile_99": 0.04874536151242207,
        "hill_tail_index": 1.4178106926980796
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.02259320058907061,
        "excess_kurtosis": 26.201984997213156,
        "return_acf_1": 0.007627970608702785,
        "abs_return_acf_1": 0.353764734274221,
        "abs_return_acf_5": 0.4364746645586172,
        "abs_return_acf_20": 0.4168432584058332,
        "quantile_01": -0.08092697567672649,
        "quantile_99": 0.050037080275615674,
        "hill_tail_index": 1.5682130940951453
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.021074842166768908,
        "excess_kurtosis": 20.83804905684915,
        "return_acf_1": 0.0004817679540897052,
        "abs_return_acf_1": 0.45242931844487166,
        "abs_return_acf_5": 0.4067043242833639,
        "abs_return_acf_20": 0.36599585558857023,
        "quantile_01": -0.07433180299927435,
        "quantile_99": 0.051992890735544826,
        "hill_tail_index": 1.8330475199807934
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.021774567865236818,
        "excess_kurtosis": 25.15720455025283,
        "return_acf_1": 0.02272500279717123,
        "abs_return_acf_1": 0.4447287476731058,
        "abs_return_acf_5": 0.46262387836810964,
        "abs_return_acf_20": 0.40004131835220463,
        "quantile_01": -0.07713884400682179,
        "quantile_99": 0.04517751594561776,
        "hill_tail_index": 1.6686944629306641
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.02334625656430173,
        "excess_kurtosis": 30.156574315009998,
        "return_acf_1": -0.02096838289826188,
        "abs_return_acf_1": 0.43181650815429273,
        "abs_return_acf_5": 0.43726547226722273,
        "abs_return_acf_20": 0.3794573990994757,
        "quantile_01": -0.09246984281603254,
        "quantile_99": 0.04939412993271833,
        "hill_tail_index": 1.6571576198333675
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.02241783219826854,
        "excess_kurtosis": 29.483502958833142,
        "return_acf_1": 0.015787611644675258,
        "abs_return_acf_1": 0.29570858086979673,
        "abs_return_acf_5": 0.4254408502642442,
        "abs_return_acf_20": 0.31166029359875574,
        "quantile_01": -0.06641175574134663,
        "quantile_99": 0.04687659231737375,
        "hill_tail_index": 1.4499607497356575
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.022445179236748308,
        "excess_kurtosis": 25.930193746269868,
        "return_acf_1": -0.04966873544165099,
        "abs_return_acf_1": 0.4031999424323525,
        "abs_return_acf_5": 0.3866567424717529,
        "abs_return_acf_20": 0.3353513897659097,
        "quantile_01": -0.0816815339474338,
        "quantile_99": 0.049385927893579346,
        "hill_tail_index": 1.425592905751148
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.020156269792987506,
        "excess_kurtosis": 15.579116249552651,
        "return_acf_1": -0.03509362502807779,
        "abs_return_acf_1": 0.35266475122404206,
        "abs_return_acf_5": 0.47243587301106893,
        "abs_return_acf_20": 0.3267634972230927,
        "quantile_01": -0.07889579520546273,
        "quantile_99": 0.04536173701020278,
        "hill_tail_index": 1.849026529708853
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02220304886071246,
        "excess_kurtosis": 15.332826881134945,
        "return_acf_1": -0.08326397544025946,
        "abs_return_acf_1": 0.4417424955445428,
        "abs_return_acf_5": 0.4271536693632992,
        "abs_return_acf_20": 0.43719210369090405,
        "quantile_01": -0.08611573928769171,
        "quantile_99": 0.0597475864116785,
        "hill_tail_index": 2.1934321932287655
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.022165605707726712,
        "excess_kurtosis": 21.543947879916477,
        "return_acf_1": -0.15032422856275182,
        "abs_return_acf_1": 0.44239997810884435,
        "abs_return_acf_5": 0.41793110366061875,
        "abs_return_acf_20": 0.33907457283198833,
        "quantile_01": -0.08414409032054902,
        "quantile_99": 0.05134311086443871,
        "hill_tail_index": 1.7511939797196865
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.02388637320438613,
        "excess_kurtosis": 30.653403747740917,
        "return_acf_1": -0.07909873324210137,
        "abs_return_acf_1": 0.3629544611816334,
        "abs_return_acf_5": 0.38632980004572604,
        "abs_return_acf_20": 0.2780023488246052,
        "quantile_01": -0.07220009715186951,
        "quantile_99": 0.050064736732135254,
        "hill_tail_index": 1.4544152230686216
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.022390313332186024,
        "excess_kurtosis": 20.51875611691965,
        "return_acf_1": -0.06249599187192295,
        "abs_return_acf_1": 0.504723078713019,
        "abs_return_acf_5": 0.45405494305723904,
        "abs_return_acf_20": 0.47674493347774966,
        "quantile_01": -0.08534437412170323,
        "quantile_99": 0.06022656031078127,
        "hill_tail_index": 1.925844694689433
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.021437903903534252,
        "excess_kurtosis": 27.04410503134574,
        "return_acf_1": 0.13302792559972776,
        "abs_return_acf_1": 0.426047277097361,
        "abs_return_acf_5": 0.4869135493265925,
        "abs_return_acf_20": 0.3589416039689062,
        "quantile_01": -0.06287517695621712,
        "quantile_99": 0.05152533634995333,
        "hill_tail_index": 2.0050459329588097
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
