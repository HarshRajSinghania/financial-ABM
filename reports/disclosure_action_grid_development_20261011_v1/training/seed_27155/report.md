# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27155
Run ID: `c800697ad4a4b66e33a4195e2384da979045e24c6e1c3fc6ab1252d071de5e1a`
Result fingerprint: `9aeea608405c2ea7dfc613de5c8351f0f0704851273630518f02cda6aaed74f7`

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
    "equal_weight_sd": -0.7436309523809491,
    "equal_weight_raw": -11.154464285714235,
    "fixed_start_cap_weight_sd": -0.7501930325254066,
    "fixed_start_cap_weight_raw": -11.252895487881098,
    "end_cap_weight_sd": -0.7520546464041783,
    "end_cap_weight_raw": -11.280819696062675
  },
  "full_period_change": {
    "equal_weight_sd": -1.1123214285714238,
    "equal_weight_raw": -16.684821428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.062691137566133,
    "inflation_mean_sd": 0.5240552248677248
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.2087500000000032,
    "equal_weight_raw": 3.131250000000048,
    "fixed_start_cap_weight_sd": 0.20218791985554554,
    "fixed_start_cap_weight_raw": 3.0328187978331824,
    "end_cap_weight_sd": 0.20032630597677412,
    "end_cap_weight_raw": 3.004894589651611
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8123809523809493,
      "change_raw": -12.18571428571424,
      "decay_adjusted_gain_sd": 0.140000000000003
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6934920634920603,
      "change_raw": -10.402380952380904,
      "decay_adjusted_gain_sd": 0.25888888888889205
    },
    "small": {
      "count": 18,
      "change_sd": -0.7572420634920601,
      "change_raw": -11.358630952380903,
      "decay_adjusted_gain_sd": 0.19513888888889216
    },
    "large_minus_small_sd": -0.05513888888888918,
    "large_minus_small_raw": -0.8270833333333377
  },
  "inflation": {
    "initial_mean_sd": 0.32775000000000004,
    "final_mean_sd": 0.5325000000000001,
    "mean_sd": 0.45249999999999996,
    "mean_absolute_raw_gap": 6.7875000000000005,
    "final_absolute_raw_gap": 7.987499999999999,
    "mean_range_fraction": 0.067875
  },
  "impact": {
    "initial_share": 0.26666666666666666,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.26747031555541206,
    "final_wealth_share": 0.4260295900759802
  },
  "pricing_slope": {
    "mean": -0.0010598872559736744,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.99999999999999,
    "resource_cost": 0.09729907551386115,
    "real_improvement_cost": 0.07948227839410217,
    "washing_cost": 0.017816797119758976,
    "fine_transfer": 0.05098565323170541,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.14828472874556656,
    "resource_cost_fraction_initial_cap": 0.003243302517128706,
    "private_net_outflow_fraction_initial_cap": 0.004942824291518887,
    "fine_transfer_fraction_initial_cap": 0.001699521774390181,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.001855988382466135,
    "unapplied_final_day_resource_cost": 0.0011058295873632783
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 64.36340702032616,
    "beneficial_raw_gain_per_resource_cost": 965.4511053048924,
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
    "accrued_cost": 2.6341445991269365,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": 0.3420458770635384,
    "accrued_cost_fraction_initial_cap": 0.08780481997089791,
    "mean_contract_rate": 0.03629329286874887,
    "maximum_ledger_error": 1.2197274440461925e-19
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
    "maximum_relative_cash_error": 2.6237713310726112e-15,
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
      "minimum": -0.3477196016865184,
      "maximum": -0.17673146305288118,
      "mean": -0.2430305577668306,
      "median": -0.24855037883226788,
      "quantile_05": -0.30029272359796877,
      "quantile_95": -0.18875470547845138
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
      "minimum": 0.655817056214695,
      "maximum": 0.8399903117623225,
      "mean": 0.7626707767468578,
      "median": 0.766267641938395,
      "quantile_05": 0.695686141606625,
      "quantile_95": 0.8176795786517853
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
        "daily_volatility": 0.020619265436070008,
        "excess_kurtosis": 36.873087641611455,
        "return_acf_1": -0.25879787398928433,
        "abs_return_acf_1": 0.4896632918354076,
        "abs_return_acf_5": 0.39263728736173015,
        "abs_return_acf_20": 0.3343062252539686,
        "quantile_01": -0.0582579525305437,
        "quantile_99": 0.04509134074221636,
        "hill_tail_index": 1.7087388860807018
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.020687745781633106,
        "excess_kurtosis": 26.99487889477156,
        "return_acf_1": -0.283464535477918,
        "abs_return_acf_1": 0.4555146044391323,
        "abs_return_acf_5": 0.36642438202309996,
        "abs_return_acf_20": 0.328314112203318,
        "quantile_01": -0.0868111835097383,
        "quantile_99": 0.045945758657056524,
        "hill_tail_index": 1.5488652473799913
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.01911193781135155,
        "excess_kurtosis": 31.5594424173441,
        "return_acf_1": -0.25569290310035864,
        "abs_return_acf_1": 0.3948430837907607,
        "abs_return_acf_5": 0.37378944869572306,
        "abs_return_acf_20": 0.2528579189016168,
        "quantile_01": -0.05293522066538155,
        "quantile_99": 0.04202157180666837,
        "hill_tail_index": 1.7281244370388409
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.020164777530228273,
        "excess_kurtosis": 38.45806779913362,
        "return_acf_1": -0.2452496752676581,
        "abs_return_acf_1": 0.38819380045460183,
        "abs_return_acf_5": 0.3374598850901812,
        "abs_return_acf_20": 0.2827994112295358,
        "quantile_01": -0.062428115993996926,
        "quantile_99": 0.04013345081604522,
        "hill_tail_index": 1.6810424628438612
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.019562591399208906,
        "excess_kurtosis": 29.29962306146352,
        "return_acf_1": -0.2508111026368917,
        "abs_return_acf_1": 0.44804227365070376,
        "abs_return_acf_5": 0.35034792149208605,
        "abs_return_acf_20": 0.3033280620154192,
        "quantile_01": -0.07802500498315118,
        "quantile_99": 0.04301501212425694,
        "hill_tail_index": 1.4475753391756558
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.018907726946052236,
        "excess_kurtosis": 19.875471971337138,
        "return_acf_1": -0.22411007062533927,
        "abs_return_acf_1": 0.36953243869817975,
        "abs_return_acf_5": 0.2975661101273476,
        "abs_return_acf_20": 0.21529059046772692,
        "quantile_01": -0.05800128161266098,
        "quantile_99": 0.04784418660071148,
        "hill_tail_index": 2.21238901210605
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.021408732061068938,
        "excess_kurtosis": 40.7743349947272,
        "return_acf_1": -0.26513071172430147,
        "abs_return_acf_1": 0.4228408320970971,
        "abs_return_acf_5": 0.38110457367149275,
        "abs_return_acf_20": 0.25357302044574614,
        "quantile_01": -0.068091991314561,
        "quantile_99": 0.04464241191987911,
        "hill_tail_index": 1.417795065379167
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01905533122309186,
        "excess_kurtosis": 32.91565286527777,
        "return_acf_1": -0.1915320140616244,
        "abs_return_acf_1": 0.36180232867063405,
        "abs_return_acf_5": 0.3995004937892379,
        "abs_return_acf_20": 0.26287491640988214,
        "quantile_01": -0.057485048916519677,
        "quantile_99": 0.04021244918446261,
        "hill_tail_index": 1.5784714952808654
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.019148293229279346,
        "excess_kurtosis": 39.03657001935008,
        "return_acf_1": -0.19148315810525818,
        "abs_return_acf_1": 0.2728999548971882,
        "abs_return_acf_5": 0.2695059264506873,
        "abs_return_acf_20": 0.2540632277686865,
        "quantile_01": -0.05292463104455002,
        "quantile_99": 0.0407093930632114,
        "hill_tail_index": 1.6313997552126671
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.02036565179052565,
        "excess_kurtosis": 29.56935069132586,
        "return_acf_1": -0.26879234140346375,
        "abs_return_acf_1": 0.4860119950612052,
        "abs_return_acf_5": 0.4194500502797698,
        "abs_return_acf_20": 0.30766813989604913,
        "quantile_01": -0.06632549439533142,
        "quantile_99": 0.03969105069903957,
        "hill_tail_index": 1.4665860078910236
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.016706581665703362,
        "excess_kurtosis": 17.244648813041618,
        "return_acf_1": -0.17673146305288118,
        "abs_return_acf_1": 0.2661750044350043,
        "abs_return_acf_5": 0.2539622620957533,
        "abs_return_acf_20": 0.19770643369730234,
        "quantile_01": -0.045868807326218376,
        "quantile_99": 0.03342252773650637,
        "hill_tail_index": 1.7285438499484267
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.01887836770468789,
        "excess_kurtosis": 34.98289002656116,
        "return_acf_1": -0.2295250011690388,
        "abs_return_acf_1": 0.5127003565542769,
        "abs_return_acf_5": 0.406215577823441,
        "abs_return_acf_20": 0.350210223062334,
        "quantile_01": -0.05786307734146694,
        "quantile_99": 0.044585622884827654,
        "hill_tail_index": 1.8866179779013614
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.018951045626190117,
        "excess_kurtosis": 32.749937870497995,
        "return_acf_1": -0.26567251158152744,
        "abs_return_acf_1": 0.37259571388091817,
        "abs_return_acf_5": 0.31950606268602716,
        "abs_return_acf_20": 0.321071286585073,
        "quantile_01": -0.05527424408651232,
        "quantile_99": 0.04183738670407418,
        "hill_tail_index": 1.6996249243750754
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01890675932251336,
        "excess_kurtosis": 14.049145742361699,
        "return_acf_1": -0.19570178357749732,
        "abs_return_acf_1": 0.33274211269000964,
        "abs_return_acf_5": 0.34258541139639587,
        "abs_return_acf_20": 0.22390850720136232,
        "quantile_01": -0.04976258313458844,
        "quantile_99": 0.04975038088445698,
        "hill_tail_index": 2.2028562426718823
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.019828948888053137,
        "excess_kurtosis": 29.76969365885487,
        "return_acf_1": -0.2645573004371144,
        "abs_return_acf_1": 0.4485250874889264,
        "abs_return_acf_5": 0.36365660994937016,
        "abs_return_acf_20": 0.2975488175072555,
        "quantile_01": -0.05846049982280542,
        "quantile_99": 0.04161420854592385,
        "hill_tail_index": 1.4940507116632071
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.02008373284008952,
        "excess_kurtosis": 26.240860192449546,
        "return_acf_1": -0.2478579277308225,
        "abs_return_acf_1": 0.470119972582106,
        "abs_return_acf_5": 0.34821658213043066,
        "abs_return_acf_20": 0.3053472296879856,
        "quantile_01": -0.06464828148811448,
        "quantile_99": 0.041717009001311374,
        "hill_tail_index": 1.5244652384868391
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.021595721909230134,
        "excess_kurtosis": 23.077219485318835,
        "return_acf_1": -0.20561057390718973,
        "abs_return_acf_1": 0.4245823988240497,
        "abs_return_acf_5": 0.3663170305872472,
        "abs_return_acf_20": 0.29272353066211343,
        "quantile_01": -0.06545764021944722,
        "quantile_99": 0.04826136388358159,
        "hill_tail_index": 2.0794739607988615
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.020126457592180704,
        "excess_kurtosis": 32.6723497658326,
        "return_acf_1": -0.21494710124442318,
        "abs_return_acf_1": 0.4556177117099001,
        "abs_return_acf_5": 0.33190481348021345,
        "abs_return_acf_20": 0.2264030708689217,
        "quantile_01": -0.05797740808414569,
        "quantile_99": 0.04757652372782967,
        "hill_tail_index": 1.7387834159523485
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.021036660627257897,
        "excess_kurtosis": 29.965476625138187,
        "return_acf_1": -0.3477196016865184,
        "abs_return_acf_1": 0.5140767589085039,
        "abs_return_acf_5": 0.4725565731007171,
        "abs_return_acf_20": 0.3476111979738521,
        "quantile_01": -0.07629631863144343,
        "quantile_99": 0.05183902467896754,
        "hill_tail_index": 1.8718960952000527
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018898713619512057,
        "excess_kurtosis": 24.055312727889653,
        "return_acf_1": -0.23615971530609023,
        "abs_return_acf_1": 0.36925813858223955,
        "abs_return_acf_5": 0.29688818920468124,
        "abs_return_acf_20": 0.25371931087707167,
        "quantile_01": -0.05672945925232836,
        "quantile_99": 0.043751993207929565,
        "hill_tail_index": 2.228996487406177
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01662145136473222,
        "excess_kurtosis": 13.23081521633097,
        "return_acf_1": -0.2706740755177394,
        "abs_return_acf_1": 0.3193424575536608,
        "abs_return_acf_5": 0.20066392468577324,
        "abs_return_acf_20": 0.2342257310066439,
        "quantile_01": -0.04089409594005185,
        "quantile_99": 0.04220489703459419,
        "hill_tail_index": 2.4254559959912663
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.01866211004432356,
        "excess_kurtosis": 26.749010423186032,
        "return_acf_1": -0.2665165366224705,
        "abs_return_acf_1": 0.37318573250489934,
        "abs_return_acf_5": 0.3950699951880086,
        "abs_return_acf_20": 0.22988254927922144,
        "quantile_01": -0.06244810264617217,
        "quantile_99": 0.04116783513681952,
        "hill_tail_index": 1.627404196004051
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.018378498270204654,
        "excess_kurtosis": 18.283332717241528,
        "return_acf_1": -0.18652233514742764,
        "abs_return_acf_1": 0.44951968398476744,
        "abs_return_acf_5": 0.36229145979265426,
        "abs_return_acf_20": 0.28010918852108985,
        "quantile_01": -0.052854890497002927,
        "quantile_99": 0.048763771530541594,
        "hill_tail_index": 2.2536340828992047
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.0196728289806431,
        "excess_kurtosis": 28.074042311076955,
        "return_acf_1": -0.21375047894736807,
        "abs_return_acf_1": 0.4718926154121429,
        "abs_return_acf_5": 0.4078878504196986,
        "abs_return_acf_20": 0.38702888526593093,
        "quantile_01": -0.0585475484750997,
        "quantile_99": 0.044410642090076044,
        "hill_tail_index": 1.6505564970378692
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.02064421306961875,
        "excess_kurtosis": 26.67757738194124,
        "return_acf_1": -0.26102786445020637,
        "abs_return_acf_1": 0.4690498814410698,
        "abs_return_acf_5": 0.37393500359511317,
        "abs_return_acf_20": 0.31821503434782916,
        "quantile_01": -0.06087819549749151,
        "quantile_99": 0.045850288654982786,
        "hill_tail_index": 1.6599738065821763
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.018425905721526175,
        "excess_kurtosis": 22.857304381586747,
        "return_acf_1": -0.3140612411507376,
        "abs_return_acf_1": 0.35541380312015947,
        "abs_return_acf_5": 0.32408691671273177,
        "abs_return_acf_20": 0.22965488129748116,
        "quantile_01": -0.054287567854775946,
        "quantile_99": 0.03954970982401609,
        "hill_tail_index": 1.5551488771624467
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.0201303532832207,
        "excess_kurtosis": 29.741514667744532,
        "return_acf_1": -0.20242141330818714,
        "abs_return_acf_1": 0.39282372146958416,
        "abs_return_acf_5": 0.30691044917327687,
        "abs_return_acf_20": 0.23436791283385466,
        "quantile_01": -0.06752617875534958,
        "quantile_99": 0.04380086924093292,
        "hill_tail_index": 1.5734538618194849
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.017917891200959737,
        "excess_kurtosis": 17.22790628277641,
        "return_acf_1": -0.27200630904916373,
        "abs_return_acf_1": 0.39663355842711545,
        "abs_return_acf_5": 0.4028256120474714,
        "abs_return_acf_20": 0.2585005421541091,
        "quantile_01": -0.046653815563048234,
        "quantile_99": 0.04557261420355481,
        "hill_tail_index": 2.0893078436031858
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.01701343735409878,
        "excess_kurtosis": 15.703590377026842,
        "return_acf_1": -0.23514628279270552,
        "abs_return_acf_1": 0.2695651105274851,
        "abs_return_acf_5": 0.25746520957589736,
        "abs_return_acf_20": 0.23283105348626607,
        "quantile_01": -0.0389428009985192,
        "quantile_99": 0.037110103994364284,
        "hill_tail_index": 1.895701520007852
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.02003803087083998,
        "excess_kurtosis": 35.80898937990685,
        "return_acf_1": -0.24924282993371324,
        "abs_return_acf_1": 0.5098827187476718,
        "abs_return_acf_5": 0.384346672699764,
        "abs_return_acf_20": 0.3059853658354203,
        "quantile_01": -0.06532311085280344,
        "quantile_99": 0.044798790876592914,
        "hill_tail_index": 1.5883790733303098
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
