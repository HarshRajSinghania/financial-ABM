# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27167
Run ID: `e3b06806b6b6be5d38205717be9d9c706f254b4d89a3b0cb860741fb98dd8183`
Result fingerprint: `8614f345d8bfe1a065001d5a6b6deeda31bb7f93c68007e56b5ee74122f7dbbc`

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
    "equal_weight_sd": -0.7196309523809492,
    "equal_weight_raw": -10.794464285714238,
    "fixed_start_cap_weight_sd": -0.7393269938690019,
    "fixed_start_cap_weight_raw": -11.089904908035027,
    "end_cap_weight_sd": -0.717310006572447,
    "end_cap_weight_raw": -10.759650098586704
  },
  "full_period_change": {
    "equal_weight_sd": -1.0909880952380904,
    "equal_weight_raw": -16.364821428571357
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.0074371693121649,
    "inflation_mean_sd": 0.366036044973545
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.23275000000000315,
    "equal_weight_raw": 3.4912500000000466,
    "fixed_start_cap_weight_sd": 0.21305395851195044,
    "fixed_start_cap_weight_raw": 3.195809377679256,
    "end_cap_weight_sd": 0.2350709458085051,
    "end_cap_weight_raw": 3.526064187127576
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.8682142857142825,
      "change_raw": -13.023214285714237,
      "decay_adjusted_gain_sd": 0.08416666666666985
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6254365079365045,
      "change_raw": -9.381547619047568,
      "decay_adjusted_gain_sd": 0.32694444444444776
    },
    "small": {
      "count": 18,
      "change_sd": -0.7419642857142826,
      "change_raw": -11.12946428571424,
      "decay_adjusted_gain_sd": 0.21041666666666972
    },
    "large_minus_small_sd": -0.12624999999999986,
    "large_minus_small_raw": -1.893749999999998
  },
  "inflation": {
    "initial_mean_sd": 0.2455,
    "final_mean_sd": 0.3858333333333334,
    "mean_sd": 0.3195552317513184,
    "mean_absolute_raw_gap": 4.793328476269775,
    "final_absolute_raw_gap": 5.787500000000002,
    "mean_range_fraction": 0.04793328476269775
  },
  "impact": {
    "initial_share": 0.30666666666666664,
    "final_share": 0.43333333333333335,
    "initial_wealth_share": 0.2333377857373368,
    "final_wealth_share": 0.3408858066982955
  },
  "pricing_slope": {
    "mean": -0.0015579536257898123,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 30.000000000000004,
    "resource_cost": 0.08739344348523305,
    "real_improvement_cost": 0.08017878787979126,
    "washing_cost": 0.007214655605441821,
    "fine_transfer": 0.03596366031524945,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.12335710380048251,
    "resource_cost_fraction_initial_cap": 0.0029131147828411015,
    "private_net_outflow_fraction_initial_cap": 0.0041119034600160835,
    "fine_transfer_fraction_initial_cap": 0.0011987886771749816,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.000556320847548299,
    "unapplied_final_day_resource_cost": 0.0008422740596722156
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 79.89729802991381,
    "beneficial_raw_gain_per_resource_cost": 1198.459470448707,
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
    "accrued_cost": 2.6307944296541237,
    "baseline_accrued_cost": 2.9761904761904776,
    "value_adjustment": 0.34539604653635325,
    "accrued_cost_fraction_initial_cap": 0.08769314765513744,
    "mean_contract_rate": 0.03641780188085224,
    "maximum_ledger_error": 4.2351647362715017e-20
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
    "maximum_relative_cash_error": 2.3827076411439134e-15,
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
      "minimum": -0.19301190465957116,
      "maximum": -0.03650670524890398,
      "mean": -0.1113822216432216,
      "median": -0.11127189175564234,
      "quantile_05": -0.17680492702451273,
      "quantile_95": -0.0508576467975408
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
      "minimum": 0.2719569167659246,
      "maximum": 0.7123926948508318,
      "mean": 0.44351095450126693,
      "median": 0.42261167172630876,
      "quantile_05": 0.3140264200875028,
      "quantile_95": 0.6329639225548123
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
        "daily_volatility": 0.017228027018525535,
        "excess_kurtosis": 9.640075492595345,
        "return_acf_1": -0.12699350570284476,
        "abs_return_acf_1": 0.39019577514078185,
        "abs_return_acf_5": 0.35654935765175266,
        "abs_return_acf_20": 0.4029471904873113,
        "quantile_01": -0.05659401544018298,
        "quantile_99": 0.04419778472055661,
        "hill_tail_index": 2.6169263067424304
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.012958416932158668,
        "excess_kurtosis": 2.397240003827261,
        "return_acf_1": -0.04820871430797463,
        "abs_return_acf_1": 0.1286736512368537,
        "abs_return_acf_5": 0.09028670387622566,
        "abs_return_acf_20": 0.10080900405051361,
        "quantile_01": -0.030321664047582013,
        "quantile_99": 0.033348147814326004,
        "hill_tail_index": 3.9359751119942747
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.016151731766503984,
        "excess_kurtosis": 6.245576255869366,
        "return_acf_1": -0.08719568391181066,
        "abs_return_acf_1": 0.35058714462409474,
        "abs_return_acf_5": 0.36919826051543514,
        "abs_return_acf_20": 0.2754779667487614,
        "quantile_01": -0.041546353952795274,
        "quantile_99": 0.04990083529519302,
        "hill_tail_index": 2.7056034111767167
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019370413434534144,
        "excess_kurtosis": 6.977408653032498,
        "return_acf_1": -0.1347595132270705,
        "abs_return_acf_1": 0.4199722645556073,
        "abs_return_acf_5": 0.3058619385050257,
        "abs_return_acf_20": 0.3697658245082273,
        "quantile_01": -0.058327001459123014,
        "quantile_99": 0.06418277677894378,
        "hill_tail_index": 3.3871025145858003
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.015154514688492646,
        "excess_kurtosis": 1.851491344847771,
        "return_acf_1": -0.08731090471681896,
        "abs_return_acf_1": 0.20204383464492617,
        "abs_return_acf_5": 0.167933015645312,
        "abs_return_acf_20": 0.08851359104951692,
        "quantile_01": -0.04004958207352659,
        "quantile_99": 0.0392692616729208,
        "hill_tail_index": 4.877477437679005
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017612809272275542,
        "excess_kurtosis": 5.936035402522229,
        "return_acf_1": -0.18987747089711843,
        "abs_return_acf_1": 0.38902168870236054,
        "abs_return_acf_5": 0.2879493170699117,
        "abs_return_acf_20": 0.22393177116762075,
        "quantile_01": -0.05418091415768063,
        "quantile_99": 0.05353474015223435,
        "hill_tail_index": 3.4909131757054817
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.01400646971097604,
        "excess_kurtosis": 1.9851141148679243,
        "return_acf_1": -0.16082737340243908,
        "abs_return_acf_1": 0.26242397088762404,
        "abs_return_acf_5": 0.21537353882669263,
        "abs_return_acf_20": 0.13872382134874597,
        "quantile_01": -0.037728035462812975,
        "quantile_99": 0.03243269815603404,
        "hill_tail_index": 3.8376919986399707
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.015144925154411942,
        "excess_kurtosis": 2.8200031417395017,
        "return_acf_1": -0.15157728245657198,
        "abs_return_acf_1": 0.1856821547215684,
        "abs_return_acf_5": 0.2086141445014876,
        "abs_return_acf_20": 0.12851555599413725,
        "quantile_01": -0.039877526767920654,
        "quantile_99": 0.037496996125022025,
        "hill_tail_index": 3.664953693870893
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.016536191271824235,
        "excess_kurtosis": 2.0606397951742927,
        "return_acf_1": -0.1094786928062059,
        "abs_return_acf_1": 0.22469806222093408,
        "abs_return_acf_5": 0.2216228293197343,
        "abs_return_acf_20": 0.20547953532930677,
        "quantile_01": -0.04486567189035379,
        "quantile_99": 0.045595827676190866,
        "hill_tail_index": 5.138590647794433
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.01717182000213178,
        "excess_kurtosis": 4.903967728179413,
        "return_acf_1": -0.09660694889060285,
        "abs_return_acf_1": 0.3313350461161896,
        "abs_return_acf_5": 0.27756325764650397,
        "abs_return_acf_20": 0.29331562025643015,
        "quantile_01": -0.04888410005109062,
        "quantile_99": 0.04867406654508731,
        "hill_tail_index": 3.035383908900536
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.017878284271538293,
        "excess_kurtosis": 9.184893512494254,
        "return_acf_1": -0.1440612858760241,
        "abs_return_acf_1": 0.3728592342512624,
        "abs_return_acf_5": 0.32680108406886976,
        "abs_return_acf_20": 0.2630482297926525,
        "quantile_01": -0.04875065200942287,
        "quantile_99": 0.04836097329401637,
        "hill_tail_index": 2.79325551848743
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.015835096016634215,
        "excess_kurtosis": 2.4350798180506237,
        "return_acf_1": -0.09828407726708656,
        "abs_return_acf_1": 0.20309536449346463,
        "abs_return_acf_5": 0.22291800338539985,
        "abs_return_acf_20": 0.1661619141770557,
        "quantile_01": -0.04138110300322155,
        "quantile_99": 0.044089631064563824,
        "hill_tail_index": 4.811969748093075
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.013944046085072088,
        "excess_kurtosis": 2.3748617728472494,
        "return_acf_1": -0.03650670524890398,
        "abs_return_acf_1": 0.24270232501462885,
        "abs_return_acf_5": 0.17033852811872385,
        "abs_return_acf_20": 0.13476961319654185,
        "quantile_01": -0.03600771984327871,
        "quantile_99": 0.035091808381181526,
        "hill_tail_index": 3.402141611175865
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018623754472445464,
        "excess_kurtosis": 7.787741994520642,
        "return_acf_1": -0.05409523095145496,
        "abs_return_acf_1": 0.34471205226519436,
        "abs_return_acf_5": 0.3486904561130825,
        "abs_return_acf_20": 0.37262439232969347,
        "quantile_01": -0.05807172736753516,
        "quantile_99": 0.0553767929589772,
        "hill_tail_index": 2.8133402692903746
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.01753403061983153,
        "excess_kurtosis": 7.204938472211371,
        "return_acf_1": -0.14796956745933346,
        "abs_return_acf_1": 0.37159477196534957,
        "abs_return_acf_5": 0.29826659164179636,
        "abs_return_acf_20": 0.24966157028318126,
        "quantile_01": -0.06296338126665584,
        "quantile_99": 0.04173945124727002,
        "hill_tail_index": 2.35643870198255
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01660925344480744,
        "excess_kurtosis": 4.050466551179916,
        "return_acf_1": -0.055717520553524004,
        "abs_return_acf_1": 0.241056416651717,
        "abs_return_acf_5": 0.22874665128267505,
        "abs_return_acf_20": 0.24338184889062772,
        "quantile_01": -0.04784103719110054,
        "quantile_99": 0.0464048926514797,
        "hill_tail_index": 3.456209557022263
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.0162676739076965,
        "excess_kurtosis": 3.4411401032148845,
        "return_acf_1": -0.19301190465957116,
        "abs_return_acf_1": 0.2514870685877317,
        "abs_return_acf_5": 0.22244101015702866,
        "abs_return_acf_20": 0.1828480053770372,
        "quantile_01": -0.04811818297783547,
        "quantile_99": 0.0414367489327843,
        "hill_tail_index": 3.48177819023085
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.01589592415886863,
        "excess_kurtosis": 3.035830452513185,
        "return_acf_1": -0.12181574260518807,
        "abs_return_acf_1": 0.28692596525105807,
        "abs_return_acf_5": 0.2841760405614072,
        "abs_return_acf_20": 0.21898124198069238,
        "quantile_01": -0.039861524386587334,
        "quantile_99": 0.04612919423905825,
        "hill_tail_index": 3.6132273157613137
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.016196841671928714,
        "excess_kurtosis": 3.7040233863031817,
        "return_acf_1": -0.1001251706561896,
        "abs_return_acf_1": 0.32422833288007663,
        "abs_return_acf_5": 0.24701398609600173,
        "abs_return_acf_20": 0.23496038568083538,
        "quantile_01": -0.045317203038103826,
        "quantile_99": 0.048327913173498493,
        "hill_tail_index": 3.9222740837976016
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01657706946897762,
        "excess_kurtosis": 3.8803506950644353,
        "return_acf_1": -0.11306509070507877,
        "abs_return_acf_1": 0.25845528278184315,
        "abs_return_acf_5": 0.2914882387218992,
        "abs_return_acf_20": 0.21344475131933727,
        "quantile_01": -0.0465314878986436,
        "quantile_99": 0.04463346457814826,
        "hill_tail_index": 3.1842106811169733
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.01739716254686628,
        "excess_kurtosis": 7.002361425931687,
        "return_acf_1": -0.1257643590550096,
        "abs_return_acf_1": 0.39418321884377056,
        "abs_return_acf_5": 0.3334653442977295,
        "abs_return_acf_20": 0.31402317050287537,
        "quantile_01": -0.05097897860223537,
        "quantile_99": 0.05070724171685591,
        "hill_tail_index": 2.6464322627438155
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.019797232250277023,
        "excess_kurtosis": 11.397517708914208,
        "return_acf_1": -0.0998544560457946,
        "abs_return_acf_1": 0.44662929373775445,
        "abs_return_acf_5": 0.40615904793012636,
        "abs_return_acf_20": 0.2884162693647697,
        "quantile_01": -0.06140500236237371,
        "quantile_99": 0.06171547737521613,
        "hill_tail_index": 3.388555156749695
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.020025296463466704,
        "excess_kurtosis": 8.55775510594198,
        "return_acf_1": -0.068542925314823,
        "abs_return_acf_1": 0.3665046022904611,
        "abs_return_acf_5": 0.2758127048537446,
        "abs_return_acf_20": 0.31636701220668584,
        "quantile_01": -0.06882652631796028,
        "quantile_99": 0.06104193082206467,
        "hill_tail_index": 3.3367927924643523
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.018510012295379602,
        "excess_kurtosis": 4.135673003976593,
        "return_acf_1": -0.06944212615613365,
        "abs_return_acf_1": 0.2973768123083738,
        "abs_return_acf_5": 0.2761674607847125,
        "abs_return_acf_20": 0.2100168326908663,
        "quantile_01": -0.0515416591413336,
        "quantile_99": 0.05280818817751627,
        "hill_tail_index": 3.9298984372176813
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.016725521644726942,
        "excess_kurtosis": 7.146413974420144,
        "return_acf_1": -0.12525447258642042,
        "abs_return_acf_1": 0.3239452994490526,
        "abs_return_acf_5": 0.2721280200348323,
        "abs_return_acf_20": 0.297194421162983,
        "quantile_01": -0.04565048366106499,
        "quantile_99": 0.05132836355350851,
        "hill_tail_index": 2.4866090611600047
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.01833666205345312,
        "excess_kurtosis": 8.43222672826832,
        "return_acf_1": -0.14192464347186226,
        "abs_return_acf_1": 0.45595068405942907,
        "abs_return_acf_5": 0.4096173915203736,
        "abs_return_acf_20": 0.32185761475628144,
        "quantile_01": -0.0629758285278143,
        "quantile_99": 0.05389320656772451,
        "hill_tail_index": 3.058321933266067
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.014434918351908167,
        "excess_kurtosis": 2.9188063069868333,
        "return_acf_1": -0.08025605640886949,
        "abs_return_acf_1": 0.20274226648978905,
        "abs_return_acf_5": 0.1744371715287921,
        "abs_return_acf_20": 0.15304053489633415,
        "quantile_01": -0.0383323639527786,
        "quantile_99": 0.037570268369070785,
        "hill_tail_index": 3.6594901471188437
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.014707411583957905,
        "excess_kurtosis": 1.30639634350994,
        "return_acf_1": -0.11958768120006323,
        "abs_return_acf_1": 0.20506561560775455,
        "abs_return_acf_5": 0.1856001339756555,
        "abs_return_acf_20": 0.16673198392245195,
        "quantile_01": -0.03773145290525936,
        "quantile_99": 0.03713107723465558,
        "hill_tail_index": 4.724030815533568
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.017742252517637908,
        "excess_kurtosis": 7.884369698903168,
        "return_acf_1": -0.15140806446000876,
        "abs_return_acf_1": 0.33287787403783164,
        "abs_return_acf_5": 0.30235356908268873,
        "abs_return_acf_20": 0.2669766303457479,
        "quantile_01": -0.0604402744913024,
        "quantile_99": 0.04541582416239631,
        "hill_tail_index": 2.6637507546215327
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017983476305412457,
        "excess_kurtosis": 5.5920667293255395,
        "return_acf_1": -0.10194347829584982,
        "abs_return_acf_1": 0.32587613018646994,
        "abs_return_acf_5": 0.3216198616716845,
        "abs_return_acf_20": 0.3153123750096874,
        "quantile_01": -0.056939212330424295,
        "quantile_99": 0.058245631003866614,
        "hill_tail_index": 3.9398314449697707
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
