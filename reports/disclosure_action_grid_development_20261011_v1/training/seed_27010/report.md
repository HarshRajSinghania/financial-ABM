# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27010
Run ID: `941cd16171250e4cc9065a0c974f6b17117d7704a350fafc489c60ead3a4770b`
Result fingerprint: `75e266411315cdb6fc7b46a0931bb81be2c34fd11595fa55a23a1714e60819d9`

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
    "equal_weight_sd": -0.4431309523809491,
    "equal_weight_raw": -6.646964285714237,
    "fixed_start_cap_weight_sd": -0.4756853930099515,
    "fixed_start_cap_weight_raw": -7.135280895149273,
    "end_cap_weight_sd": -0.48251033390269593,
    "end_cap_weight_raw": -7.237655008540438
  },
  "full_period_change": {
    "equal_weight_sd": -0.7289047619047568,
    "equal_weight_raw": -10.933571428571353
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -0.6980740740740695,
    "inflation_mean_sd": 0.5408088624338625
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.5092500000000032,
    "equal_weight_raw": 7.638750000000048,
    "fixed_start_cap_weight_sd": 0.4766955593710007,
    "fixed_start_cap_weight_raw": 7.150433390565011,
    "end_cap_weight_sd": 0.46987061847825645,
    "end_cap_weight_raw": 7.048059277173842
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.5632142857142823,
      "change_raw": -8.448214285714235,
      "decay_adjusted_gain_sd": 0.38916666666667005
    },
    "mid": {
      "count": 9,
      "change_sd": -0.3951587301587268,
      "change_raw": -5.9273809523809025,
      "decay_adjusted_gain_sd": 0.5572222222222254
    },
    "small": {
      "count": 18,
      "change_sd": -0.4471031746031714,
      "change_raw": -6.706547619047571,
      "decay_adjusted_gain_sd": 0.5052777777777808
    },
    "large_minus_small_sd": -0.11611111111111094,
    "large_minus_small_raw": -1.741666666666664
  },
  "inflation": {
    "initial_mean_sd": 0.17099999999999996,
    "final_mean_sd": 0.5685833333333333,
    "mean_sd": 0.3691606300305302,
    "mean_absolute_raw_gap": 5.537409450457952,
    "final_absolute_raw_gap": 8.52875,
    "mean_range_fraction": 0.05537409450457952
  },
  "impact": {
    "initial_share": 0.32,
    "final_share": 0.32666666666666666,
    "initial_wealth_share": 0.29754535040974345,
    "final_wealth_share": 0.3259969317738056
  },
  "pricing_slope": {
    "mean": -4.523244965614309e-05,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.0,
    "resource_cost": 0.12268472101693007,
    "real_improvement_cost": 0.10204323740670608,
    "washing_cost": 0.02064148361022399,
    "fine_transfer": 0.0006240043845046094,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12330872540143467,
    "resource_cost_fraction_initial_cap": 0.004089490700564335,
    "private_net_outflow_fraction_initial_cap": 0.004110290846714489,
    "fine_transfer_fraction_initial_cap": 2.0800146150153646e-05,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.004154683278374578,
    "unapplied_final_day_resource_cost": 0.004791348787521913
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 124.52650887058589,
    "beneficial_raw_gain_per_resource_cost": 1867.8976330587882,
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
    "fixed_exposure": 15.0,
    "accrued_cost": 2.9124615412130215,
    "baseline_accrued_cost": 2.9761904761904767,
    "value_adjustment": 0.06372893497745513,
    "accrued_cost_fraction_initial_cap": 0.09708205137376738,
    "mean_contract_rate": 0.04006485015734272,
    "maximum_ledger_error": 6.437450399132683e-20
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
    "price_cap_hits": 1,
    "maximum_relative_cash_error": 2.223770244213345e-15,
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
      "minimum": -0.16039289277290011,
      "maximum": 0.027168352803350868,
      "mean": -0.08052587986183671,
      "median": -0.08263327094972886,
      "quantile_05": -0.13865812626598656,
      "quantile_95": 0.006334473717796479
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
      "minimum": 0.3029864646806868,
      "maximum": 0.7335765594330389,
      "mean": 0.4816597639314924,
      "median": 0.4561180615365138,
      "quantile_05": 0.3441979801831261,
      "quantile_95": 0.6728234912131719
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
        "daily_volatility": 0.01717996820750344,
        "excess_kurtosis": 5.893666768258983,
        "return_acf_1": -0.003271405733234857,
        "abs_return_acf_1": 0.33124352962342746,
        "abs_return_acf_5": 0.30630162884897055,
        "abs_return_acf_20": 0.2934752545381749,
        "quantile_01": -0.05138594609988813,
        "quantile_99": 0.05033285913094793,
        "hill_tail_index": 3.0863394147521923
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.01580048691458881,
        "excess_kurtosis": 5.907042494279809,
        "return_acf_1": -0.08811515520914945,
        "abs_return_acf_1": 0.38436398817353296,
        "abs_return_acf_5": 0.32203976368801746,
        "abs_return_acf_20": 0.3013599033786033,
        "quantile_01": -0.04966841294618314,
        "quantile_99": 0.04729575709910846,
        "hill_tail_index": 2.987804186221831
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.014438521467373035,
        "excess_kurtosis": 2.9306240286986993,
        "return_acf_1": -0.08108499852743074,
        "abs_return_acf_1": 0.2096617191711724,
        "abs_return_acf_5": 0.21908518238034058,
        "abs_return_acf_20": 0.24383794314586016,
        "quantile_01": -0.036846001961744645,
        "quantile_99": 0.03802468800584549,
        "hill_tail_index": 3.870678006322275
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.017398695292342475,
        "excess_kurtosis": 6.3198264206399255,
        "return_acf_1": -0.12063599037330505,
        "abs_return_acf_1": 0.3412777450574526,
        "abs_return_acf_5": 0.2385727543561602,
        "abs_return_acf_20": 0.23560785195674241,
        "quantile_01": -0.051010141450612646,
        "quantile_99": 0.04571557880905601,
        "hill_tail_index": 3.347150684562964
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.017620858223205374,
        "excess_kurtosis": 5.244413211380076,
        "return_acf_1": -0.07637131381308529,
        "abs_return_acf_1": 0.3212076736545104,
        "abs_return_acf_5": 0.26608711209437574,
        "abs_return_acf_20": 0.2199218783076945,
        "quantile_01": -0.058641316939210535,
        "quantile_99": 0.05130818170713149,
        "hill_tail_index": 3.308861668422282
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.016371093889714826,
        "excess_kurtosis": 7.406764928356516,
        "return_acf_1": -0.052921011454052584,
        "abs_return_acf_1": 0.30097135887717247,
        "abs_return_acf_5": 0.28343456734862615,
        "abs_return_acf_20": 0.2273216197141983,
        "quantile_01": -0.04060080849514157,
        "quantile_99": 0.047425027083764185,
        "hill_tail_index": 2.2759129641797515
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.015954170227900463,
        "excess_kurtosis": 9.022004851376035,
        "return_acf_1": -0.07674742583545652,
        "abs_return_acf_1": 0.22438732107238168,
        "abs_return_acf_5": 0.2888271799761689,
        "abs_return_acf_20": 0.2304495090516052,
        "quantile_01": -0.040991954809236716,
        "quantile_99": 0.045081807704084424,
        "hill_tail_index": 1.9676297330316748
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.01809391220963969,
        "excess_kurtosis": 3.5833659439743677,
        "return_acf_1": -0.11904882660313758,
        "abs_return_acf_1": 0.3209713650095551,
        "abs_return_acf_5": 0.3357647825896716,
        "abs_return_acf_20": 0.27870588388055284,
        "quantile_01": -0.053007907478827776,
        "quantile_99": 0.052822821576237154,
        "hill_tail_index": 4.283183303540663
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.017579377654997966,
        "excess_kurtosis": 11.110929495136864,
        "return_acf_1": -0.14287918268094027,
        "abs_return_acf_1": 0.3469482348012225,
        "abs_return_acf_5": 0.2618268002105993,
        "abs_return_acf_20": 0.26522446412072914,
        "quantile_01": -0.051369407368066125,
        "quantile_99": 0.043149651295396815,
        "hill_tail_index": 2.472521296526047
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.017991090499876308,
        "excess_kurtosis": 5.578815958023812,
        "return_acf_1": -0.1295330862843157,
        "abs_return_acf_1": 0.36462812214058166,
        "abs_return_acf_5": 0.3663288900238032,
        "abs_return_acf_20": 0.32758369324328135,
        "quantile_01": -0.055805971135160996,
        "quantile_99": 0.05071961748934904,
        "hill_tail_index": 4.147748748174208
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.015567892971725134,
        "excess_kurtosis": 5.669494446183641,
        "return_acf_1": -0.051629397079251044,
        "abs_return_acf_1": 0.3618037908714353,
        "abs_return_acf_5": 0.3415165188261394,
        "abs_return_acf_20": 0.22207269504246907,
        "quantile_01": -0.04135644935223891,
        "quantile_99": 0.041334882203926955,
        "hill_tail_index": 2.490690805443191
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.017255517479711067,
        "excess_kurtosis": 13.738901724205704,
        "return_acf_1": -0.014229027479027798,
        "abs_return_acf_1": 0.39554810772585114,
        "abs_return_acf_5": 0.4412935665185536,
        "abs_return_acf_20": 0.23704856614120268,
        "quantile_01": -0.03878885447198079,
        "quantile_99": 0.042337569384458415,
        "hill_tail_index": 1.561305702682905
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.017167364677774792,
        "excess_kurtosis": 9.383825298445153,
        "return_acf_1": 0.027168352803350868,
        "abs_return_acf_1": 0.3464083670731517,
        "abs_return_acf_5": 0.3503803815715385,
        "abs_return_acf_20": 0.33299611130655493,
        "quantile_01": -0.054845114728105826,
        "quantile_99": 0.0496472467454899,
        "hill_tail_index": 2.7821208336774736
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.01586322037749696,
        "excess_kurtosis": 1.88162967986597,
        "return_acf_1": -0.07263865471746739,
        "abs_return_acf_1": 0.2055459506630216,
        "abs_return_acf_5": 0.2350639174130061,
        "abs_return_acf_20": 0.16981019519784118,
        "quantile_01": -0.04437122954956575,
        "quantile_99": 0.04252769979692889,
        "hill_tail_index": 5.08580298661857
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.014969207440806804,
        "excess_kurtosis": 2.5932685376313067,
        "return_acf_1": -0.07508571882622277,
        "abs_return_acf_1": 0.2551025024065514,
        "abs_return_acf_5": 0.18326722085850033,
        "abs_return_acf_20": 0.1557706023051948,
        "quantile_01": -0.040494336462619865,
        "quantile_99": 0.0396123634010056,
        "hill_tail_index": 4.132802070787174
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.017744296131886488,
        "excess_kurtosis": 6.281391408297116,
        "return_acf_1": -0.0971491161247668,
        "abs_return_acf_1": 0.27244534033707873,
        "abs_return_acf_5": 0.2927152334481361,
        "abs_return_acf_20": 0.3119385012090283,
        "quantile_01": -0.05624911853338981,
        "quantile_99": 0.04846954285819691,
        "hill_tail_index": 3.0999731975404643
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.015193047525477454,
        "excess_kurtosis": 2.16389531355186,
        "return_acf_1": -0.12661127331817623,
        "abs_return_acf_1": 0.2562821785097086,
        "abs_return_acf_5": 0.26989865709590527,
        "abs_return_acf_20": 0.21917627571565407,
        "quantile_01": -0.036216094207563845,
        "quantile_99": 0.04063172248478989,
        "hill_tail_index": 3.8858479269517456
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.016568978992175094,
        "excess_kurtosis": 2.0066562055412636,
        "return_acf_1": -0.09478044276439491,
        "abs_return_acf_1": 0.20497669013927516,
        "abs_return_acf_5": 0.1690364977183686,
        "abs_return_acf_20": 0.23826092656903425,
        "quantile_01": -0.042301041896851924,
        "quantile_99": 0.044688628337905115,
        "hill_tail_index": 4.566306885991334
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.01660629020328778,
        "excess_kurtosis": 3.378156982366739,
        "return_acf_1": -0.028772661907603116,
        "abs_return_acf_1": 0.2136757341103209,
        "abs_return_acf_5": 0.18740580408461086,
        "abs_return_acf_20": 0.16906862725825306,
        "quantile_01": -0.049145388184951906,
        "quantile_99": 0.04394381737689393,
        "hill_tail_index": 3.6066301052364786
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.018142147897351423,
        "excess_kurtosis": 6.731581378185508,
        "return_acf_1": -0.05841617169435654,
        "abs_return_acf_1": 0.3109672289629058,
        "abs_return_acf_5": 0.2712246961491014,
        "abs_return_acf_20": 0.2294998871948095,
        "quantile_01": -0.05485470700446695,
        "quantile_99": 0.04688045550301816,
        "hill_tail_index": 3.3596984937466985
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.016252044681574714,
        "excess_kurtosis": 3.6408556017829365,
        "return_acf_1": -0.06802996757332058,
        "abs_return_acf_1": 0.2836530749844468,
        "abs_return_acf_5": 0.31929803710992644,
        "abs_return_acf_20": 0.2138861751567006,
        "quantile_01": -0.04596016396540569,
        "quantile_99": 0.04343724227435044,
        "hill_tail_index": 3.913439123082371
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.015876386545139846,
        "excess_kurtosis": 5.7683926669268875,
        "return_acf_1": -0.07259965717118563,
        "abs_return_acf_1": 0.2852807688118841,
        "abs_return_acf_5": 0.2649682117700998,
        "abs_return_acf_20": 0.2152661603835234,
        "quantile_01": -0.04215998024116368,
        "quantile_99": 0.04421100011456498,
        "hill_tail_index": 2.845243035506792
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.015688865364089165,
        "excess_kurtosis": 2.726876759939663,
        "return_acf_1": -0.16039289277290011,
        "abs_return_acf_1": 0.2890761130105476,
        "abs_return_acf_5": 0.2680620658562077,
        "abs_return_acf_20": 0.23447443521207967,
        "quantile_01": -0.04849883228552052,
        "quantile_99": 0.038488757641766624,
        "hill_tail_index": 3.7110780640413292
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.01853605569638036,
        "excess_kurtosis": 9.544580550657235,
        "return_acf_1": -0.1306263613139098,
        "abs_return_acf_1": 0.35840167907147447,
        "abs_return_acf_5": 0.3683145941778433,
        "abs_return_acf_20": 0.2751917874653928,
        "quantile_01": -0.05804866617083805,
        "quantile_99": 0.04974898682429288,
        "hill_tail_index": 2.771545521253244
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.016161997727985055,
        "excess_kurtosis": 0.9138439303004029,
        "return_acf_1": -0.13349905731437647,
        "abs_return_acf_1": 0.19358315546653518,
        "abs_return_acf_5": 0.178672534087447,
        "abs_return_acf_20": 0.1562426599155665,
        "quantile_01": -0.04072122969884233,
        "quantile_99": 0.03793106069250563,
        "hill_tail_index": 4.616601670289444
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.015483365411194282,
        "excess_kurtosis": 3.85355943219935,
        "return_acf_1": -0.10019645453066581,
        "abs_return_acf_1": 0.26125902312910776,
        "abs_return_acf_5": 0.20601729729029225,
        "abs_return_acf_20": 0.1289433708252757,
        "quantile_01": -0.03947943644063594,
        "quantile_99": 0.04726187993113355,
        "hill_tail_index": 3.8723558223163637
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.015524290401308103,
        "excess_kurtosis": 6.72837251285922,
        "return_acf_1": -0.1036077348610342,
        "abs_return_acf_1": 0.32260036027558275,
        "abs_return_acf_5": 0.22031613757757598,
        "abs_return_acf_20": 0.27531113763885456,
        "quantile_01": -0.03722728525572931,
        "quantile_99": 0.03709679268844951,
        "hill_tail_index": 2.7587170353668804
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.01907475469180815,
        "excess_kurtosis": 5.786811318903164,
        "return_acf_1": -0.09408404895593427,
        "abs_return_acf_1": 0.3769736109993098,
        "abs_return_acf_5": 0.41048969783764205,
        "abs_return_acf_20": 0.29956580696061225,
        "quantile_01": -0.06056326563239569,
        "quantile_99": 0.054846556692980226,
        "hill_tail_index": 3.671504656083585
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.0175128446014894,
        "excess_kurtosis": 3.3932970171628396,
        "return_acf_1": -0.08418154337202699,
        "abs_return_acf_1": 0.30730815760836755,
        "abs_return_acf_5": 0.28053441860771133,
        "abs_return_acf_20": 0.31489213872567867,
        "quantile_01": -0.055014933219888956,
        "quantile_99": 0.04717319608691016,
        "hill_tail_index": 4.87952556958989
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.01802122987031241,
        "excess_kurtosis": 7.258777878722421,
        "return_acf_1": 0.014193829632276753,
        "abs_return_acf_1": 0.3595077736790129,
        "abs_return_acf_5": 0.33093039783755857,
        "abs_return_acf_20": 0.24713896843556932,
        "quantile_01": -0.05657136112063711,
        "quantile_99": 0.061718826173666086,
        "hill_tail_index": 2.555265412142169
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
