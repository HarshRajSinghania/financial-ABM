# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27198
Run ID: `769b93270db7fb310b55a5cfbe3c8155dc3fb3cea1086051ef0007a28e270516`
Result fingerprint: `4267a5bcb8fc765f5e714ec14ed323b885f76d13b7ab41b8ac90ff34187a49f3`

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
    "equal_weight_sd": -0.7981309523809491,
    "equal_weight_raw": -11.97196428571424,
    "fixed_start_cap_weight_sd": -0.7583146842185307,
    "fixed_start_cap_weight_raw": -11.374720263277961,
    "end_cap_weight_sd": -0.774405761894297,
    "end_cap_weight_raw": -11.616086428414453
  },
  "full_period_change": {
    "equal_weight_sd": -1.2059047619047574,
    "equal_weight_raw": -18.08857142857136
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1337050264550221,
    "inflation_mean_sd": 0.579984126984127
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.15425000000000313,
    "equal_weight_raw": 2.313750000000047,
    "fixed_start_cap_weight_sd": 0.19406626816242156,
    "fixed_start_cap_weight_raw": 2.9109940224363235,
    "end_cap_weight_sd": 0.1779751904866552,
    "end_cap_weight_raw": 2.6696278572998278
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5207142857142829,
      "change_raw": -7.810714285714243,
      "decay_adjusted_gain_sd": 0.4316666666666695
    },
    "mid": {
      "count": 9,
      "change_sd": -0.8759920634920602,
      "change_raw": -13.139880952380903,
      "decay_adjusted_gain_sd": 0.0763888888888921
    },
    "small": {
      "count": 18,
      "change_sd": -0.8054365079365047,
      "change_raw": -12.08154761904757,
      "decay_adjusted_gain_sd": 0.14694444444444765
    },
    "large_minus_small_sd": 0.28472222222222177,
    "large_minus_small_raw": 4.270833333333327
  },
  "inflation": {
    "initial_mean_sd": 0.2531666666666667,
    "final_mean_sd": 0.6153333333333333,
    "mean_sd": 0.4460854843186234,
    "mean_absolute_raw_gap": 6.6912822647793515,
    "final_absolute_raw_gap": 9.23,
    "mean_range_fraction": 0.06691282264779351
  },
  "impact": {
    "initial_share": 0.28,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.2822912117345859,
    "final_wealth_share": 0.28198485750561375
  },
  "pricing_slope": {
    "mean": -0.0013753258108132307,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000007,
    "resource_cost": 0.019540025795249293,
    "real_improvement_cost": 0.0131623047707534,
    "washing_cost": 0.00637772102449589,
    "fine_transfer": 0.002412579757201746,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.02195260555245104,
    "resource_cost_fraction_initial_cap": 0.0006513341931749763,
    "private_net_outflow_fraction_initial_cap": 0.0007317535184150345,
    "fine_transfer_fraction_initial_cap": 8.041932524005818e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0016204659333620027,
    "unapplied_final_day_resource_cost": 8.32080088016618e-05
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 236.82159115292282,
    "beneficial_raw_gain_per_resource_cost": 3552.3238672938423,
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
    "accrued_cost": 2.9925618495316666,
    "baseline_accrued_cost": 2.976190476190476,
    "value_adjustment": -0.016371373341190088,
    "accrued_cost_fraction_initial_cap": 0.09975206165105553,
    "mean_contract_rate": 0.04122815423283645,
    "maximum_ledger_error": 6.776263578034403e-20
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
    "maximum_relative_cash_error": 2.0642815788945028e-15,
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
      "minimum": -0.1891802552351353,
      "maximum": 0.010848799914102812,
      "mean": -0.08191386755713871,
      "median": -0.07042586618165653,
      "quantile_05": -0.1774612611744933,
      "quantile_95": -0.000657003772325809
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
      "minimum": 0.30873599731516177,
      "maximum": 0.7664383967180101,
      "mean": 0.48192468379310105,
      "median": 0.4612073181401348,
      "quantile_05": 0.3323534738724033,
      "quantile_95": 0.6957314008472755
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
        "daily_volatility": 0.019162548087196567,
        "excess_kurtosis": 6.2341752979791885,
        "return_acf_1": 0.010848799914102812,
        "abs_return_acf_1": 0.3437197801017615,
        "abs_return_acf_5": 0.37559413190852153,
        "abs_return_acf_20": 0.31359058651984084,
        "quantile_01": -0.06546548617144107,
        "quantile_99": 0.055805193664976785,
        "hill_tail_index": 3.285341491039763
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019239593181292064,
        "excess_kurtosis": 10.4331940061578,
        "return_acf_1": -0.12813688252354283,
        "abs_return_acf_1": 0.35025802002495465,
        "abs_return_acf_5": 0.32439448298447787,
        "abs_return_acf_20": 0.28865024988699745,
        "quantile_01": -0.05986070282706533,
        "quantile_99": 0.05290567592860161,
        "hill_tail_index": 2.77052646692325
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01625975112689376,
        "excess_kurtosis": 9.240931659024222,
        "return_acf_1": -0.13949691157624025,
        "abs_return_acf_1": 0.4515128710981043,
        "abs_return_acf_5": 0.42222163915395544,
        "abs_return_acf_20": 0.22433482185099585,
        "quantile_01": -0.0403939640751589,
        "quantile_99": 0.04241259954413601,
        "hill_tail_index": 2.218701113453515
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.01699469187299317,
        "excess_kurtosis": 11.322965565862532,
        "return_acf_1": -0.14637610440267496,
        "abs_return_acf_1": 0.2806173143223683,
        "abs_return_acf_5": 0.25585443916875394,
        "abs_return_acf_20": 0.30224396116066876,
        "quantile_01": -0.05140146942746702,
        "quantile_99": 0.04474057562273467,
        "hill_tail_index": 2.584778758237781
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.01679977620590963,
        "excess_kurtosis": 6.03540576403554,
        "return_acf_1": -0.07080996499245566,
        "abs_return_acf_1": 0.27648360461743593,
        "abs_return_acf_5": 0.2707832986526579,
        "abs_return_acf_20": 0.28133009096810435,
        "quantile_01": -0.050467060337377426,
        "quantile_99": 0.046707063435612234,
        "hill_tail_index": 3.0123418117911647
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018306383496261344,
        "excess_kurtosis": 5.705475171945022,
        "return_acf_1": -0.12691270018080494,
        "abs_return_acf_1": 0.2987639778781033,
        "abs_return_acf_5": 0.35466245881025266,
        "abs_return_acf_20": 0.21274350261099562,
        "quantile_01": -0.059278978383217835,
        "quantile_99": 0.048667770202753056,
        "hill_tail_index": 3.037419256410956
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.016698668295833923,
        "excess_kurtosis": 7.442071469452706,
        "return_acf_1": -0.04370620608762817,
        "abs_return_acf_1": 0.285020236805569,
        "abs_return_acf_5": 0.27927538101830696,
        "abs_return_acf_20": 0.2384666012902203,
        "quantile_01": -0.0491616431478954,
        "quantile_99": 0.041703977774952335,
        "hill_tail_index": 2.143709601380054
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.018120198994293478,
        "excess_kurtosis": 3.292287241783203,
        "return_acf_1": -0.17969592384235816,
        "abs_return_acf_1": 0.3492647663752378,
        "abs_return_acf_5": 0.2957572499433138,
        "abs_return_acf_20": 0.3486996539179337,
        "quantile_01": -0.05975285418340873,
        "quantile_99": 0.049597048049526304,
        "hill_tail_index": 4.504902068039721
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017528047523701223,
        "excess_kurtosis": 3.1126945623241546,
        "return_acf_1": -0.05551258055256911,
        "abs_return_acf_1": 0.26371488550639977,
        "abs_return_acf_5": 0.24786553703212483,
        "abs_return_acf_20": 0.21382138743712265,
        "quantile_01": -0.05079729686878581,
        "quantile_99": 0.048436130067258276,
        "hill_tail_index": 4.073486499446712
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01564236618344748,
        "excess_kurtosis": 5.824442977328751,
        "return_acf_1": -0.10576980134878324,
        "abs_return_acf_1": 0.21511648642201653,
        "abs_return_acf_5": 0.19885425354377514,
        "abs_return_acf_20": 0.2135256087611066,
        "quantile_01": -0.0412931143827886,
        "quantile_99": 0.03904839462836005,
        "hill_tail_index": 2.6686015291908705
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018156970319973702,
        "excess_kurtosis": 5.583781991623052,
        "return_acf_1": 0.0030289620731074212,
        "abs_return_acf_1": 0.39420014392533914,
        "abs_return_acf_5": 0.4286850021994364,
        "abs_return_acf_20": 0.31220955427150465,
        "quantile_01": -0.05628775304845682,
        "quantile_99": 0.05273992769151723,
        "hill_tail_index": 3.6663105088973924
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.016409782417610534,
        "excess_kurtosis": 13.253976120286499,
        "return_acf_1": -0.034408601904148475,
        "abs_return_acf_1": 0.3040954931824023,
        "abs_return_acf_5": 0.2624441812560221,
        "abs_return_acf_20": 0.21319171459792052,
        "quantile_01": -0.044832415878490586,
        "quantile_99": 0.046346780879716235,
        "hill_tail_index": 2.4842039593308844
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.019139624691662714,
        "excess_kurtosis": 7.087359463789358,
        "return_acf_1": -0.08804748283504767,
        "abs_return_acf_1": 0.32924609230136737,
        "abs_return_acf_5": 0.4097310428268777,
        "abs_return_acf_20": 0.30623808059942115,
        "quantile_01": -0.06646555221998472,
        "quantile_99": 0.05294986323608616,
        "hill_tail_index": 3.375279308713585
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.016017774669365104,
        "excess_kurtosis": 10.61214573434516,
        "return_acf_1": -0.07004176737085738,
        "abs_return_acf_1": 0.23661621775910868,
        "abs_return_acf_5": 0.26698190601818106,
        "abs_return_acf_20": 0.17831637862483055,
        "quantile_01": -0.04024289481451772,
        "quantile_99": 0.05044453755372342,
        "hill_tail_index": 3.0304105442709472
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018877369654771367,
        "excess_kurtosis": 7.197393891410764,
        "return_acf_1": -0.05938059645935744,
        "abs_return_acf_1": 0.3006438684079771,
        "abs_return_acf_5": 0.33684785809809525,
        "abs_return_acf_20": 0.23473495974143566,
        "quantile_01": -0.06737112258890807,
        "quantile_99": 0.0548103796600199,
        "hill_tail_index": 3.5436618096419363
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01586274319300255,
        "excess_kurtosis": 5.270453487887121,
        "return_acf_1": -0.028648070097150022,
        "abs_return_acf_1": 0.23516516297081927,
        "abs_return_acf_5": 0.29691835098363595,
        "abs_return_acf_20": 0.3094915648921715,
        "quantile_01": -0.047304048252405875,
        "quantile_99": 0.041751161029569876,
        "hill_tail_index": 3.113623172135919
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.016665693099179094,
        "excess_kurtosis": 4.706442899380121,
        "return_acf_1": -0.05613705934874632,
        "abs_return_acf_1": 0.1692718687961496,
        "abs_return_acf_5": 0.1685746281129073,
        "abs_return_acf_20": 0.2017857914851515,
        "quantile_01": -0.04654136601925209,
        "quantile_99": 0.0412801853598082,
        "hill_tail_index": 3.622540520442919
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016945278460906908,
        "excess_kurtosis": 6.530543879034072,
        "return_acf_1": -0.11108070307183725,
        "abs_return_acf_1": 0.4081044652232297,
        "abs_return_acf_5": 0.34483428358125773,
        "abs_return_acf_20": 0.3052606648635631,
        "quantile_01": -0.04985255460849893,
        "quantile_99": 0.04321996172846794,
        "hill_tail_index": 2.5630904469918008
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017904932139787277,
        "excess_kurtosis": 2.6881101311502498,
        "return_acf_1": -0.16957950517447629,
        "abs_return_acf_1": 0.34968670632338067,
        "abs_return_acf_5": 0.3026883270764289,
        "abs_return_acf_20": 0.2759203401098549,
        "quantile_01": -0.05094784652131563,
        "quantile_99": 0.051278838561806504,
        "hill_tail_index": 5.814335444709467
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.017362175730101886,
        "excess_kurtosis": 3.5924398098238406,
        "return_acf_1": -0.06652376396838153,
        "abs_return_acf_1": 0.29264599993205964,
        "abs_return_acf_5": 0.24480499156338914,
        "abs_return_acf_20": 0.2993648884210888,
        "quantile_01": -0.047369200267077714,
        "quantile_99": 0.05115083890013889,
        "hill_tail_index": 3.899574164946912
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.017316539277333814,
        "excess_kurtosis": 16.152524300804515,
        "return_acf_1": -0.1891802552351353,
        "abs_return_acf_1": 0.3928248494489815,
        "abs_return_acf_5": 0.30877777260839057,
        "abs_return_acf_20": 0.1923443255202383,
        "quantile_01": -0.04618583762907299,
        "quantile_99": 0.046824330369093364,
        "hill_tail_index": 2.0090717087710384
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.017589209130802082,
        "excess_kurtosis": 5.999024129767212,
        "return_acf_1": -0.005162073138966373,
        "abs_return_acf_1": 0.36574677252432874,
        "abs_return_acf_5": 0.3865088921538262,
        "abs_return_acf_20": 0.2941343111831847,
        "quantile_01": -0.05345616152773306,
        "quantile_99": 0.05083685893648856,
        "hill_tail_index": 3.405364114296712
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017352884345171952,
        "excess_kurtosis": 12.810943329703626,
        "return_acf_1": -0.03119044691878633,
        "abs_return_acf_1": 0.4480439648163336,
        "abs_return_acf_5": 0.43881201986796164,
        "abs_return_acf_20": 0.32498508088342926,
        "quantile_01": -0.05542506914060321,
        "quantile_99": 0.046094209625457454,
        "hill_tail_index": 2.380241381549789
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01661230246116696,
        "excess_kurtosis": 3.1866074494986316,
        "return_acf_1": -0.04002008828434853,
        "abs_return_acf_1": 0.3102215904006539,
        "abs_return_acf_5": 0.27241501459255674,
        "abs_return_acf_20": 0.23060831777097132,
        "quantile_01": -0.052917590151370895,
        "quantile_99": 0.04206680218893434,
        "hill_tail_index": 4.833311059116125
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.01733966748044813,
        "excess_kurtosis": 5.424767271221015,
        "return_acf_1": -0.047556663510382534,
        "abs_return_acf_1": 0.30370056754511704,
        "abs_return_acf_5": 0.3345622503954358,
        "abs_return_acf_20": 0.27957829052319016,
        "quantile_01": -0.053588834681198086,
        "quantile_99": 0.04452988174099629,
        "hill_tail_index": 2.9351714347145026
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01541799431808145,
        "excess_kurtosis": 3.9954214312938774,
        "return_acf_1": -0.09862126031708304,
        "abs_return_acf_1": 0.2805467695200907,
        "abs_return_acf_5": 0.2950842183640797,
        "abs_return_acf_20": 0.21287920662479645,
        "quantile_01": -0.037023653232042084,
        "quantile_99": 0.04254778706274879,
        "hill_tail_index": 2.951333637276976
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.017895982461415345,
        "excess_kurtosis": 4.091126956393543,
        "return_acf_1": -0.07387685703332805,
        "abs_return_acf_1": 0.30132427575231246,
        "abs_return_acf_5": 0.27309735185405715,
        "abs_return_acf_20": 0.2683562644307002,
        "quantile_01": -0.05797843776205487,
        "quantile_99": 0.047274899145018076,
        "hill_tail_index": 3.5747119019742097
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019485599652597923,
        "excess_kurtosis": 4.893707869731753,
        "return_acf_1": -0.0867402900848805,
        "abs_return_acf_1": 0.36511063839186,
        "abs_return_acf_5": 0.3450837944932046,
        "abs_return_acf_20": 0.2746672477677807,
        "quantile_01": -0.060909981669595645,
        "quantile_99": 0.06130820745530677,
        "hill_tail_index": 3.3631071167712943
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019617635347397258,
        "excess_kurtosis": 5.924673009707181,
        "return_acf_1": -0.17473000680265846,
        "abs_return_acf_1": 0.3519648220606843,
        "abs_return_acf_5": 0.4533679673326193,
        "abs_return_acf_20": 0.30515016389380456,
        "quantile_01": -0.05942068121480546,
        "quantile_99": 0.05351018922982019,
        "hill_tail_index": 3.3501505336815685
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01837818262132069,
        "excess_kurtosis": 12.629577255382127,
        "return_acf_1": -0.04395122163874312,
        "abs_return_acf_1": 0.45727765739271703,
        "abs_return_acf_5": 0.4240444524606599,
        "abs_return_acf_20": 0.32899791871366235,
        "quantile_01": -0.05851911568468511,
        "quantile_99": 0.04471913448933863,
        "hill_tail_index": 2.3049775474913674
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
