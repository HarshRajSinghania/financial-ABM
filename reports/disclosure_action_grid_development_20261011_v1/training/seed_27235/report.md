# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27235
Run ID: `e5d8ad30915379ed0ac319b2e0ccc5264b68a5f62446cacbf170b77844d4bbed`
Result fingerprint: `9e4c0a44c4e630200f87071215bf62e9bba9139a92c8bb7ac40a2fbfd6c44202`

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
    "equal_weight_sd": -0.8874642857142826,
    "equal_weight_raw": -13.311964285714236,
    "fixed_start_cap_weight_sd": -0.9013753918211562,
    "fixed_start_cap_weight_raw": -13.520630877317343,
    "end_cap_weight_sd": -0.9017959033890817,
    "end_cap_weight_raw": -13.52693855083622
  },
  "full_period_change": {
    "equal_weight_sd": -1.3002380952380903,
    "equal_weight_raw": -19.503571428571355
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.2108664021163977,
    "inflation_mean_sd": 1.1140056216931216
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.06491666666666976,
    "equal_weight_raw": 0.973750000000046,
    "fixed_start_cap_weight_sd": 0.05100556055979581,
    "fixed_start_cap_weight_raw": 0.7650834083969372,
    "end_cap_weight_sd": 0.050585048991870864,
    "end_cap_weight_raw": 0.7587757348780629
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.9165476190476163,
      "change_raw": -13.748214285714244,
      "decay_adjusted_gain_sd": 0.035833333333336014
    },
    "mid": {
      "count": 9,
      "change_sd": -0.898769841269838,
      "change_raw": -13.481547619047571,
      "decay_adjusted_gain_sd": 0.05361111111111427
    },
    "small": {
      "count": 18,
      "change_sd": -0.8769642857142825,
      "change_raw": -13.154464285714237,
      "decay_adjusted_gain_sd": 0.07541666666666977
    },
    "large_minus_small_sd": -0.03958333333333375,
    "large_minus_small_raw": -0.5937500000000062
  },
  "inflation": {
    "initial_mean_sd": 0.28150000000000003,
    "final_mean_sd": 1.2189166666666664,
    "mean_sd": 0.642309672495143,
    "mean_absolute_raw_gap": 9.634645087427144,
    "final_absolute_raw_gap": 18.28375,
    "mean_range_fraction": 0.09634645087427143
  },
  "impact": {
    "initial_share": 0.26,
    "final_share": 0.32,
    "initial_wealth_share": 0.250706727103903,
    "final_wealth_share": 0.29065938299205313
  },
  "pricing_slope": {
    "mean": -0.0014605166010109975,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.07749068229904035,
    "real_improvement_cost": 0.0639561385119577,
    "washing_cost": 0.013534543787082683,
    "fine_transfer": 0.006209839392890205,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.08370052169193055,
    "resource_cost_fraction_initial_cap": 0.002583022743301345,
    "private_net_outflow_fraction_initial_cap": 0.002790017389731018,
    "fine_transfer_fraction_initial_cap": 0.00020699464642967347,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.00015551156611649228,
    "unapplied_final_day_resource_cost": 0.001430656344019535
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 25.132053844675085,
    "beneficial_raw_gain_per_resource_cost": 376.98080767012624,
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
    "accrued_cost": 2.7308041192086483,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.24538635698182856,
    "accrued_cost_fraction_initial_cap": 0.0910268039736216,
    "mean_contract_rate": 0.03786753305132255,
    "maximum_ledger_error": 6.268043809681823e-20
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
    "maximum_relative_cash_error": 9.561805723829845e-16,
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
      "minimum": -0.20514469288339482,
      "maximum": -0.069365562424538,
      "mean": -0.1377809185928446,
      "median": -0.1365479396371148,
      "quantile_05": -0.20142567003241732,
      "quantile_95": -0.07569566682852946
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
      "minimum": 0.2885358907053855,
      "maximum": 0.7558361504264276,
      "mean": 0.5230744469563938,
      "median": 0.5084128804137519,
      "quantile_05": 0.3409044274732203,
      "quantile_95": 0.70055544916805
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
        "daily_volatility": 0.017132372778954595,
        "excess_kurtosis": 2.58707989451542,
        "return_acf_1": -0.16390127132086518,
        "abs_return_acf_1": 0.26320498797243735,
        "abs_return_acf_5": 0.18688093862618668,
        "abs_return_acf_20": 0.1981011607385043,
        "quantile_01": -0.04487309119069276,
        "quantile_99": 0.04611213382624615,
        "hill_tail_index": 4.4403222431858715
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020720479656335087,
        "excess_kurtosis": 13.056291378240154,
        "return_acf_1": -0.1624822563133493,
        "abs_return_acf_1": 0.3145258901293744,
        "abs_return_acf_5": 0.28543630482770915,
        "abs_return_acf_20": 0.2847274468482215,
        "quantile_01": -0.0628909721867138,
        "quantile_99": 0.05700878242061658,
        "hill_tail_index": 2.4615785397535284
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020209556317778456,
        "excess_kurtosis": 6.263523686101189,
        "return_acf_1": -0.14898730353855857,
        "abs_return_acf_1": 0.42962883778430944,
        "abs_return_acf_5": 0.3123463488201307,
        "abs_return_acf_20": 0.3175039810979954,
        "quantile_01": -0.06711863377266486,
        "quantile_99": 0.0572938004754287,
        "hill_tail_index": 3.7148788887077857
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.021124716536586752,
        "excess_kurtosis": 10.951692081876217,
        "return_acf_1": -0.20514469288339482,
        "abs_return_acf_1": 0.3209896812911599,
        "abs_return_acf_5": 0.34578467233123966,
        "abs_return_acf_20": 0.3017989634528199,
        "quantile_01": -0.0685410467464032,
        "quantile_99": 0.05460968191783817,
        "hill_tail_index": 2.670889663155769
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.021221988848975415,
        "excess_kurtosis": 10.069845539607556,
        "return_acf_1": -0.16222963259519657,
        "abs_return_acf_1": 0.4300129032196451,
        "abs_return_acf_5": 0.36041067308022035,
        "abs_return_acf_20": 0.3029417256890503,
        "quantile_01": -0.07361557068028812,
        "quantile_99": 0.059750474301213455,
        "hill_tail_index": 2.6685898098149434
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.020274817195530946,
        "excess_kurtosis": 10.824018479490336,
        "return_acf_1": -0.17819380067046856,
        "abs_return_acf_1": 0.3433314592022889,
        "abs_return_acf_5": 0.3298212495115131,
        "abs_return_acf_20": 0.3007742100238937,
        "quantile_01": -0.07300466810164363,
        "quantile_99": 0.05186667067126029,
        "hill_tail_index": 2.6834879154462747
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.018190111805692546,
        "excess_kurtosis": 16.908949872814137,
        "return_acf_1": -0.07729087968610537,
        "abs_return_acf_1": 0.5304078426912817,
        "abs_return_acf_5": 0.49072407635750914,
        "abs_return_acf_20": 0.21330393612609588,
        "quantile_01": -0.05055907381447449,
        "quantile_99": 0.051678950557975945,
        "hill_tail_index": 1.7073835021152097
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01705714160562821,
        "excess_kurtosis": 7.905664968483597,
        "return_acf_1": -0.1114735251667107,
        "abs_return_acf_1": 0.3847888666076334,
        "abs_return_acf_5": 0.34761694959783296,
        "abs_return_acf_20": 0.23702239789289695,
        "quantile_01": -0.049867017637287146,
        "quantile_99": 0.04701423542902821,
        "hill_tail_index": 3.3096559103545258
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019502320920570453,
        "excess_kurtosis": 5.107640384375365,
        "return_acf_1": -0.09676425798539445,
        "abs_return_acf_1": 0.29318187260327766,
        "abs_return_acf_5": 0.3172483235676123,
        "abs_return_acf_20": 0.27619697270550764,
        "quantile_01": -0.05590889515703628,
        "quantile_99": 0.04672338076127801,
        "hill_tail_index": 3.830911923590817
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01592452782090409,
        "excess_kurtosis": 3.7312241500886074,
        "return_acf_1": -0.12380079051257416,
        "abs_return_acf_1": 0.2961367317247117,
        "abs_return_acf_5": 0.21578714267192917,
        "abs_return_acf_20": 0.21459120421546737,
        "quantile_01": -0.04611603089150463,
        "quantile_99": 0.04372201329958484,
        "hill_tail_index": 3.619066738697724
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.01892159649632506,
        "excess_kurtosis": 7.651404336744175,
        "return_acf_1": -0.069365562424538,
        "abs_return_acf_1": 0.3245672682398019,
        "abs_return_acf_5": 0.2761187047905818,
        "abs_return_acf_20": 0.26714547189428345,
        "quantile_01": -0.056914362197578,
        "quantile_99": 0.0474744247711674,
        "hill_tail_index": 3.0456624892181647
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015872047599131023,
        "excess_kurtosis": 2.3246078618963377,
        "return_acf_1": -0.07439049267233099,
        "abs_return_acf_1": 0.16079867910448534,
        "abs_return_acf_5": 0.13616993020076798,
        "abs_return_acf_20": 0.12382007099887515,
        "quantile_01": -0.04179879278360704,
        "quantile_99": 0.04397193622460335,
        "hill_tail_index": 4.483430702019201
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017394975862029857,
        "excess_kurtosis": 5.9150214855003735,
        "return_acf_1": -0.10431288620748974,
        "abs_return_acf_1": 0.289614020545688,
        "abs_return_acf_5": 0.28562920880651876,
        "abs_return_acf_20": 0.2341862032088767,
        "quantile_01": -0.05548314743638296,
        "quantile_99": 0.03952217783046495,
        "hill_tail_index": 3.003615037412594
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.02049927708531569,
        "excess_kurtosis": 7.708652275325779,
        "return_acf_1": -0.13510788793214465,
        "abs_return_acf_1": 0.32060863731697126,
        "abs_return_acf_5": 0.37910435599730696,
        "abs_return_acf_20": 0.2676335380800855,
        "quantile_01": -0.06271220290781299,
        "quantile_99": 0.05888076888072678,
        "hill_tail_index": 3.567589318587271
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.020668474278944547,
        "excess_kurtosis": 8.190314959727061,
        "return_acf_1": -0.13149501072941094,
        "abs_return_acf_1": 0.3387703249719186,
        "abs_return_acf_5": 0.321684275762348,
        "abs_return_acf_20": 0.2520981784443339,
        "quantile_01": -0.068590496965672,
        "quantile_99": 0.049275986233336545,
        "hill_tail_index": 3.1001689713161724
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.020493341948235464,
        "excess_kurtosis": 10.879611037902789,
        "return_acf_1": -0.2025982434559829,
        "abs_return_acf_1": 0.43024588425316085,
        "abs_return_acf_5": 0.362764696263216,
        "abs_return_acf_20": 0.31097014224119535,
        "quantile_01": -0.06420578956225592,
        "quantile_99": 0.05573664002762644,
        "hill_tail_index": 2.915003560955017
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019446849710996406,
        "excess_kurtosis": 7.639281090532972,
        "return_acf_1": -0.1273590633553329,
        "abs_return_acf_1": 0.3331741394719789,
        "abs_return_acf_5": 0.3026815886020902,
        "abs_return_acf_20": 0.2661072143569025,
        "quantile_01": -0.06161575536271968,
        "quantile_99": 0.052370447078764065,
        "hill_tail_index": 2.9530932179488696
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.017090483412793726,
        "excess_kurtosis": 4.244990547986084,
        "return_acf_1": -0.17208441370957456,
        "abs_return_acf_1": 0.32044521088065847,
        "abs_return_acf_5": 0.2368307939481021,
        "abs_return_acf_20": 0.1740630495504938,
        "quantile_01": -0.04996133045482859,
        "quantile_99": 0.04523932365160683,
        "hill_tail_index": 3.760018380580082
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01716103667455301,
        "excess_kurtosis": 2.4286103957580165,
        "return_acf_1": -0.11353413453508403,
        "abs_return_acf_1": 0.22019337714804813,
        "abs_return_acf_5": 0.22987322551782585,
        "abs_return_acf_20": 0.16943087389129402,
        "quantile_01": -0.05170696615002212,
        "quantile_99": 0.04908907847413619,
        "hill_tail_index": 4.629747725048182
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.019427814021158365,
        "excess_kurtosis": 6.062989635643957,
        "return_acf_1": -0.16092060527212082,
        "abs_return_acf_1": 0.36916288755770066,
        "abs_return_acf_5": 0.28626835471587203,
        "abs_return_acf_20": 0.26597337877814464,
        "quantile_01": -0.07443372892461188,
        "quantile_99": 0.05192757807274243,
        "hill_tail_index": 3.187901074140981
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.015647794072794947,
        "excess_kurtosis": 1.8160614057506113,
        "return_acf_1": -0.15105932012710993,
        "abs_return_acf_1": 0.18849586296952972,
        "abs_return_acf_5": 0.16598889476732204,
        "abs_return_acf_20": 0.10419871597030343,
        "quantile_01": -0.040941688469192064,
        "quantile_99": 0.03549093472568301,
        "hill_tail_index": 3.9175944205464988
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016558364586861354,
        "excess_kurtosis": 2.8590880926297713,
        "return_acf_1": -0.13798799134208495,
        "abs_return_acf_1": 0.2169322108855821,
        "abs_return_acf_5": 0.18888288182870097,
        "abs_return_acf_20": 0.15196657583573686,
        "quantile_01": -0.0452578759921343,
        "quantile_99": 0.04191945327996151,
        "hill_tail_index": 4.550110646272289
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.019417090410224862,
        "excess_kurtosis": 5.786524650359835,
        "return_acf_1": -0.19999252473694829,
        "abs_return_acf_1": 0.3504751138605606,
        "abs_return_acf_5": 0.28290866519287794,
        "abs_return_acf_20": 0.2948399043436064,
        "quantile_01": -0.05995792608021576,
        "quantile_99": 0.04620681729045674,
        "hill_tail_index": 2.650262277739868
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020435942494999908,
        "excess_kurtosis": 6.245622706355968,
        "return_acf_1": -0.13232028947663485,
        "abs_return_acf_1": 0.345406602063661,
        "abs_return_acf_5": 0.33106479249030446,
        "abs_return_acf_20": 0.27277598601260244,
        "quantile_01": -0.06604522914957346,
        "quantile_99": 0.06128521048783113,
        "hill_tail_index": 3.8623908545074923
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.019078479057334004,
        "excess_kurtosis": 7.724384598371058,
        "return_acf_1": -0.15505236906386424,
        "abs_return_acf_1": 0.297312611141178,
        "abs_return_acf_5": 0.22753984153549636,
        "abs_return_acf_20": 0.26195086297010556,
        "quantile_01": -0.055309044938690884,
        "quantile_99": 0.048846799729625,
        "hill_tail_index": 2.8324989181712317
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.02048294539317083,
        "excess_kurtosis": 8.68711730153754,
        "return_acf_1": -0.14459295634669386,
        "abs_return_acf_1": 0.2980108145060513,
        "abs_return_acf_5": 0.2946532367195459,
        "abs_return_acf_20": 0.2975593998070133,
        "quantile_01": -0.06341066431129391,
        "quantile_99": 0.05510303273047502,
        "hill_tail_index": 3.086213013934072
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.019500531420170737,
        "excess_kurtosis": 5.0206529987189885,
        "return_acf_1": -0.10430130134870028,
        "abs_return_acf_1": 0.3647412342001776,
        "abs_return_acf_5": 0.34845174890618696,
        "abs_return_acf_20": 0.2502154423733138,
        "quantile_01": -0.059463071209345575,
        "quantile_99": 0.05704291119464672,
        "hill_tail_index": 3.6991996769305153
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.019742504798532432,
        "excess_kurtosis": 7.5049370112488205,
        "return_acf_1": -0.12024113430227777,
        "abs_return_acf_1": 0.3710303955895263,
        "abs_return_acf_5": 0.3970861768666511,
        "abs_return_acf_20": 0.32046804854520045,
        "quantile_01": -0.07031983026133641,
        "quantile_99": 0.05638538164515584,
        "hill_tail_index": 3.366954796061014
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.019167344579742042,
        "excess_kurtosis": 9.088994984746494,
        "return_acf_1": -0.17675958139029097,
        "abs_return_acf_1": 0.361429997243675,
        "abs_return_acf_5": 0.31342999357541207,
        "abs_return_acf_20": 0.25703750289208865,
        "quantile_01": -0.071151804758734,
        "quantile_99": 0.04962029372418122,
        "hill_tail_index": 2.700322969237997
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02007815477714822,
        "excess_kurtosis": 10.47315082219301,
        "return_acf_1": -0.08968337868410589,
        "abs_return_acf_1": 0.3804914657848043,
        "abs_return_acf_5": 0.341761299842615,
        "abs_return_acf_20": 0.2192654491068827,
        "quantile_01": -0.06910795082400496,
        "quantile_99": 0.05457808931710784,
        "hill_tail_index": 2.8996582717731814
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
