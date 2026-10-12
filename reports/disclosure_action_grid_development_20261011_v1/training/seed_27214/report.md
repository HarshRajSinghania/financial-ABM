# Disclosure-market run

Purpose: development
Domain: esg
Seed: 27214
Run ID: `44d25630d119169dc32cb49a85c217333398fbed6173b36ca03dafa3c6feda6f`
Result fingerprint: `98eac89494662fb453308bef4763e12507b346010cb665c0850a1acd27a44862`

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
    "equal_weight_sd": -0.7879642857142825,
    "equal_weight_raw": -11.819464285714234,
    "fixed_start_cap_weight_sd": -0.7788051976673258,
    "fixed_start_cap_weight_raw": -11.682077965009885,
    "end_cap_weight_sd": -0.770183814722295,
    "end_cap_weight_raw": -11.552757220834426
  },
  "full_period_change": {
    "equal_weight_sd": -1.213904761904757,
    "equal_weight_raw": -18.208571428571354
  },
  "terminal_year": {
    "start_day": 1549,
    "observations": 252,
    "complete_year": true,
    "change_from_initial_sd": -1.1382933201058154,
    "inflation_mean_sd": 0.7148637566137565
  },
  "decay_adjusted_gain": {
    "equal_weight_sd": 0.1644166666666699,
    "equal_weight_raw": 2.466250000000048,
    "fixed_start_cap_weight_sd": 0.17357575471362646,
    "fixed_start_cap_weight_raw": 2.6036363207043967,
    "end_cap_weight_sd": 0.18219713765865733,
    "end_cap_weight_raw": 2.73295706487986
  },
  "size": {
    "large": {
      "count": 3,
      "change_sd": -0.6898809523809492,
      "change_raw": -10.348214285714237,
      "decay_adjusted_gain_sd": 0.2625000000000033
    },
    "mid": {
      "count": 9,
      "change_sd": -0.6865476190476156,
      "change_raw": -10.298214285714234,
      "decay_adjusted_gain_sd": 0.2658333333333366
    },
    "small": {
      "count": 18,
      "change_sd": -0.8550198412698379,
      "change_raw": -12.825297619047568,
      "decay_adjusted_gain_sd": 0.09736111111111434
    },
    "large_minus_small_sd": 0.16513888888888872,
    "large_minus_small_raw": 2.477083333333331
  },
  "inflation": {
    "initial_mean_sd": 0.40850000000000003,
    "final_mean_sd": 0.7267499999999999,
    "mean_sd": 0.5818998751040798,
    "mean_absolute_raw_gap": 8.728498126561199,
    "final_absolute_raw_gap": 10.90125,
    "mean_range_fraction": 0.08728498126561199
  },
  "impact": {
    "initial_share": 0.17333333333333334,
    "final_share": 0.21333333333333335,
    "initial_wealth_share": 0.09965130981166553,
    "final_wealth_share": 0.1284500727174572
  },
  "pricing_slope": {
    "mean": -0.0005694679619193293,
    "observations": 20
  },
  "costs": {
    "initial_market_cap": 29.999999999999996,
    "resource_cost": 0.016997315963162705,
    "real_improvement_cost": 0.01019254470946271,
    "washing_cost": 0.006804771253699996,
    "fine_transfer": 0.04792227283880983,
    "subsidy_transfer": 0.0,
    "private_net_outflow": 0.06491958880197253,
    "resource_cost_fraction_initial_cap": 0.0005665771987720902,
    "private_net_outflow_fraction_initial_cap": 0.0021639862933990847,
    "fine_transfer_fraction_initial_cap": 0.0015974090946269945,
    "subsidy_transfer_fraction_initial_cap": 0.0,
    "carry_in_resource_cost": 0.0034297008196684598,
    "unapplied_final_day_resource_cost": 0.0006562330074156938
  },
  "efficiency": {
    "decay_adjusted_sd_per_resource_cost": 290.1928757863899,
    "beneficial_raw_gain_per_resource_cost": 4352.8931367958485,
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
    "fixed_exposure": 14.999999999999998,
    "accrued_cost": 2.769243328215206,
    "baseline_accrued_cost": 2.9761904761904754,
    "value_adjustment": 0.20694714797527053,
    "accrued_cost_fraction_initial_cap": 0.09230811094050688,
    "mean_contract_rate": 0.0378373654851687,
    "maximum_ledger_error": 1.0333801956502464e-19
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
    "maximum_relative_cash_error": 1.704150810068462e-15,
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
      "minimum": -0.1926265803257257,
      "maximum": -0.018408356050120218,
      "mean": -0.09438905919682566,
      "median": -0.08712774779146856,
      "quantile_05": -0.16090628690555703,
      "quantile_95": -0.02447224156440616
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
      "minimum": 0.2577092827632883,
      "maximum": 0.7595245018539262,
      "mean": 0.5559679949855851,
      "median": 0.5738585016589582,
      "quantile_05": 0.33844841300184797,
      "quantile_95": 0.7231522953453596
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
        "daily_volatility": 0.01912699530953673,
        "excess_kurtosis": 4.204517749516235,
        "return_acf_1": -0.14085017842367603,
        "abs_return_acf_1": 0.29920047001011824,
        "abs_return_acf_5": 0.23424270689627275,
        "abs_return_acf_20": 0.3017629314965639,
        "quantile_01": -0.0651701789915504,
        "quantile_99": 0.053146807223661434,
        "hill_tail_index": 3.75650989277262
      }
    },
    {
      "asset": 1,
      "moments": {
        "daily_volatility": 0.019430156153817862,
        "excess_kurtosis": 4.797373886011063,
        "return_acf_1": -0.061058704291890475,
        "abs_return_acf_1": 0.34703305123822414,
        "abs_return_acf_5": 0.31754040742067813,
        "abs_return_acf_20": 0.27482167107111505,
        "quantile_01": -0.06279479088590366,
        "quantile_99": 0.05030236554369551,
        "hill_tail_index": 3.729806070352053
      }
    },
    {
      "asset": 2,
      "moments": {
        "daily_volatility": 0.020854297064782378,
        "excess_kurtosis": 12.588410336787513,
        "return_acf_1": -0.024242842776124676,
        "abs_return_acf_1": 0.3184887020375704,
        "abs_return_acf_5": 0.4090876931609018,
        "abs_return_acf_20": 0.29900572033710215,
        "quantile_01": -0.07582544408859487,
        "quantile_99": 0.05551872756923366,
        "hill_tail_index": 2.2021383747680456
      }
    },
    {
      "asset": 3,
      "moments": {
        "daily_volatility": 0.019858602637306103,
        "excess_kurtosis": 6.726592450963468,
        "return_acf_1": -0.030468833023889013,
        "abs_return_acf_1": 0.3360446695296202,
        "abs_return_acf_5": 0.39279590332041475,
        "abs_return_acf_20": 0.32385976452861587,
        "quantile_01": -0.06271825877582093,
        "quantile_99": 0.0604707163420729,
        "hill_tail_index": 3.6061976342400337
      }
    },
    {
      "asset": 4,
      "moments": {
        "daily_volatility": 0.018252420282192035,
        "excess_kurtosis": 8.815384529269627,
        "return_acf_1": -0.06284469405378744,
        "abs_return_acf_1": 0.43928708852584386,
        "abs_return_acf_5": 0.4338490836432648,
        "abs_return_acf_20": 0.37855057276687243,
        "quantile_01": -0.06788256982470815,
        "quantile_99": 0.048120927945503586,
        "hill_tail_index": 2.4061329702300096
      }
    },
    {
      "asset": 5,
      "moments": {
        "daily_volatility": 0.017258916191768933,
        "excess_kurtosis": 3.8761942692330456,
        "return_acf_1": -0.1496543168972732,
        "abs_return_acf_1": 0.21299156649651194,
        "abs_return_acf_5": 0.19903429827907482,
        "abs_return_acf_20": 0.16611638844692622,
        "quantile_01": -0.04525161529281906,
        "quantile_99": 0.04554005565122788,
        "hill_tail_index": 3.824703956321486
      }
    },
    {
      "asset": 6,
      "moments": {
        "daily_volatility": 0.0192341465705644,
        "excess_kurtosis": 5.999527946158148,
        "return_acf_1": -0.08418233261158739,
        "abs_return_acf_1": 0.4020257412501428,
        "abs_return_acf_5": 0.37899819278218677,
        "abs_return_acf_20": 0.3909193765983518,
        "quantile_01": -0.06625607648631227,
        "quantile_99": 0.051320752509742586,
        "hill_tail_index": 3.015354825357771
      }
    },
    {
      "asset": 7,
      "moments": {
        "daily_volatility": 0.019288775875653946,
        "excess_kurtosis": 6.261653716459595,
        "return_acf_1": -0.08627608444806142,
        "abs_return_acf_1": 0.3819914640827177,
        "abs_return_acf_5": 0.3489765637582131,
        "abs_return_acf_20": 0.3142181130060827,
        "quantile_01": -0.06274855377406884,
        "quantile_99": 0.05238873032381521,
        "hill_tail_index": 3.2289369920278066
      }
    },
    {
      "asset": 8,
      "moments": {
        "daily_volatility": 0.018596114430750283,
        "excess_kurtosis": 5.82783583113871,
        "return_acf_1": -0.062363259564596964,
        "abs_return_acf_1": 0.3353026796857739,
        "abs_return_acf_5": 0.2883211978482756,
        "abs_return_acf_20": 0.2701858682215439,
        "quantile_01": -0.057191719527990924,
        "quantile_99": 0.048472844997150634,
        "hill_tail_index": 3.282882076515265
      }
    },
    {
      "asset": 9,
      "moments": {
        "daily_volatility": 0.018706009326881625,
        "excess_kurtosis": 5.309833630586876,
        "return_acf_1": -0.11603755995488073,
        "abs_return_acf_1": 0.4022357766956478,
        "abs_return_acf_5": 0.41415667578408266,
        "abs_return_acf_20": 0.28596309400960057,
        "quantile_01": -0.06536561582312338,
        "quantile_99": 0.056430991361194144,
        "hill_tail_index": 3.9227424538572317
      }
    },
    {
      "asset": 10,
      "moments": {
        "daily_volatility": 0.018171964309792968,
        "excess_kurtosis": 4.684594152397872,
        "return_acf_1": -0.10128186578880145,
        "abs_return_acf_1": 0.33524730785687196,
        "abs_return_acf_5": 0.30473255951751554,
        "abs_return_acf_20": 0.3044639292426285,
        "quantile_01": -0.06096619056653009,
        "quantile_99": 0.05260988300732152,
        "hill_tail_index": 4.0720077503775585
      }
    },
    {
      "asset": 11,
      "moments": {
        "daily_volatility": 0.019259376358127436,
        "excess_kurtosis": 12.231032045358482,
        "return_acf_1": -0.018408356050120218,
        "abs_return_acf_1": 0.4518208572752118,
        "abs_return_acf_5": 0.3901441426654774,
        "abs_return_acf_20": 0.3445681933626887,
        "quantile_01": -0.05836453829199249,
        "quantile_99": 0.05345399094689631,
        "hill_tail_index": 2.5158886110220404
      }
    },
    {
      "asset": 12,
      "moments": {
        "daily_volatility": 0.020184798049691446,
        "excess_kurtosis": 7.216456301304184,
        "return_acf_1": -0.08500523443722306,
        "abs_return_acf_1": 0.3397659591710744,
        "abs_return_acf_5": 0.36420129874129914,
        "abs_return_acf_20": 0.33995530979374416,
        "quantile_01": -0.06359511730365312,
        "quantile_99": 0.05886355327165241,
        "hill_tail_index": 3.3304639174212936
      }
    },
    {
      "asset": 13,
      "moments": {
        "daily_volatility": 0.018996389213458222,
        "excess_kurtosis": 5.534427856384312,
        "return_acf_1": -0.16311212861886812,
        "abs_return_acf_1": 0.41093251049463875,
        "abs_return_acf_5": 0.3133368903361057,
        "abs_return_acf_20": 0.2591203515566516,
        "quantile_01": -0.05799750320223199,
        "quantile_99": 0.059051768621426776,
        "hill_tail_index": 3.9038731667441704
      }
    },
    {
      "asset": 14,
      "moments": {
        "daily_volatility": 0.018952808615569007,
        "excess_kurtosis": 5.89166289379715,
        "return_acf_1": -0.061959353838687975,
        "abs_return_acf_1": 0.33836060651278316,
        "abs_return_acf_5": 0.32599309979941227,
        "abs_return_acf_20": 0.24699275915776045,
        "quantile_01": -0.06249215798529887,
        "quantile_99": 0.05160195913062371,
        "hill_tail_index": 4.441892323910007
      }
    },
    {
      "asset": 15,
      "moments": {
        "daily_volatility": 0.01997918025587653,
        "excess_kurtosis": 4.957872517453055,
        "return_acf_1": -0.1926265803257257,
        "abs_return_acf_1": 0.3765923248451986,
        "abs_return_acf_5": 0.32247911231600146,
        "abs_return_acf_20": 0.29206395656989,
        "quantile_01": -0.06480668588467985,
        "quantile_99": 0.055298501929559846,
        "hill_tail_index": 3.8396123593211473
      }
    },
    {
      "asset": 16,
      "moments": {
        "daily_volatility": 0.019912325106654073,
        "excess_kurtosis": 8.628758748185232,
        "return_acf_1": -0.024752617861194637,
        "abs_return_acf_1": 0.4013853486283698,
        "abs_return_acf_5": 0.38417557118323115,
        "abs_return_acf_20": 0.37022533877403363,
        "quantile_01": -0.06131709732055983,
        "quantile_99": 0.05898334657343619,
        "hill_tail_index": 3.093609477526483
      }
    },
    {
      "asset": 17,
      "moments": {
        "daily_volatility": 0.019186730874448568,
        "excess_kurtosis": 6.158619820763645,
        "return_acf_1": -0.08389982661850565,
        "abs_return_acf_1": 0.3163452039015869,
        "abs_return_acf_5": 0.32781492959455244,
        "abs_return_acf_20": 0.34679100287838177,
        "quantile_01": -0.05955811769708259,
        "quantile_99": 0.05103313851698143,
        "hill_tail_index": 2.9853020583078718
      }
    },
    {
      "asset": 18,
      "moments": {
        "daily_volatility": 0.017324069939410876,
        "excess_kurtosis": 3.436649791686852,
        "return_acf_1": -0.09826083210201554,
        "abs_return_acf_1": 0.2744768263062451,
        "abs_return_acf_5": 0.2725683056239887,
        "abs_return_acf_20": 0.23054303031470316,
        "quantile_01": -0.0516495853577138,
        "quantile_99": 0.04999622038457121,
        "hill_tail_index": 5.32411621131306
      }
    },
    {
      "asset": 19,
      "moments": {
        "daily_volatility": 0.01863821943790119,
        "excess_kurtosis": 5.18376914116414,
        "return_acf_1": -0.1423109090803089,
        "abs_return_acf_1": 0.29454877949569763,
        "abs_return_acf_5": 0.2826012909628728,
        "abs_return_acf_20": 0.2562775630902593,
        "quantile_01": -0.05538413738578929,
        "quantile_99": 0.04841066476044449,
        "hill_tail_index": 3.852551732608383
      }
    },
    {
      "asset": 20,
      "moments": {
        "daily_volatility": 0.019408754059937555,
        "excess_kurtosis": 7.794648173386712,
        "return_acf_1": -0.0721024756332169,
        "abs_return_acf_1": 0.40562434066873,
        "abs_return_acf_5": 0.338505946315341,
        "abs_return_acf_20": 0.37302525575852225,
        "quantile_01": -0.06547125779351722,
        "quantile_99": 0.05607787968447576,
        "hill_tail_index": 3.409195155852518
      }
    },
    {
      "asset": 21,
      "moments": {
        "daily_volatility": 0.016066246671408605,
        "excess_kurtosis": 3.0773613955947337,
        "return_acf_1": -0.09426016197663233,
        "abs_return_acf_1": 0.2358799261283805,
        "abs_return_acf_5": 0.26120044182107577,
        "abs_return_acf_20": 0.19758445056131385,
        "quantile_01": -0.04564437619692047,
        "quantile_99": 0.043278145580663854,
        "hill_tail_index": 4.213755148485438
      }
    },
    {
      "asset": 22,
      "moments": {
        "daily_volatility": 0.017445226852886464,
        "excess_kurtosis": 2.9392330029942366,
        "return_acf_1": -0.12368866821828627,
        "abs_return_acf_1": 0.25707781253757195,
        "abs_return_acf_5": 0.2689578184446058,
        "abs_return_acf_20": 0.2672994338774176,
        "quantile_01": -0.053474967321398066,
        "quantile_99": 0.04462008594035912,
        "hill_tail_index": 4.749155985873166
      }
    },
    {
      "asset": 23,
      "moments": {
        "daily_volatility": 0.020413548611494983,
        "excess_kurtosis": 9.760299907638021,
        "return_acf_1": -0.09259653397890923,
        "abs_return_acf_1": 0.3809574164859935,
        "abs_return_acf_5": 0.4265750155957263,
        "abs_return_acf_20": 0.37106210979014315,
        "quantile_01": -0.06765235786133847,
        "quantile_99": 0.05351712376873495,
        "hill_tail_index": 2.588677379757663
      }
    },
    {
      "asset": 24,
      "moments": {
        "daily_volatility": 0.021093126921312915,
        "excess_kurtosis": 15.100344574116797,
        "return_acf_1": -0.08061872926504639,
        "abs_return_acf_1": 0.4823106920714308,
        "abs_return_acf_5": 0.4454374095710537,
        "abs_return_acf_20": 0.32735033121207413,
        "quantile_01": -0.07002151458267075,
        "quantile_99": 0.05243445990043879,
        "hill_tail_index": 2.865714026012201
      }
    },
    {
      "asset": 25,
      "moments": {
        "daily_volatility": 0.020696606198978028,
        "excess_kurtosis": 10.899638425039857,
        "return_acf_1": -0.07514212349811884,
        "abs_return_acf_1": 0.4843670000351147,
        "abs_return_acf_5": 0.4193017684285213,
        "abs_return_acf_20": 0.26856744061271787,
        "quantile_01": -0.07028660676095004,
        "quantile_99": 0.05721945850264648,
        "hill_tail_index": 2.6299503457127975
      }
    },
    {
      "asset": 26,
      "moments": {
        "daily_volatility": 0.01698126370763202,
        "excess_kurtosis": 5.532745670302926,
        "return_acf_1": -0.1558451387184389,
        "abs_return_acf_1": 0.38000367387327266,
        "abs_return_acf_5": 0.3853569783691736,
        "abs_return_acf_20": 0.30319232780926797,
        "quantile_01": -0.055845646064964304,
        "quantile_99": 0.043766993333868416,
        "hill_tail_index": 3.006694524585103
      }
    },
    {
      "asset": 27,
      "moments": {
        "daily_volatility": 0.020892992774412346,
        "excess_kurtosis": 5.865319785919599,
        "return_acf_1": -0.0879794111348757,
        "abs_return_acf_1": 0.4435796190119197,
        "abs_return_acf_5": 0.4565660187941335,
        "abs_return_acf_20": 0.40339235765529263,
        "quantile_01": -0.07240013889569893,
        "quantile_99": 0.0601851366383511,
        "hill_tail_index": 4.217777730701647
      }
    },
    {
      "asset": 28,
      "moments": {
        "daily_volatility": 0.020190672467030952,
        "excess_kurtosis": 7.865432748867791,
        "return_acf_1": -0.1016317645691835,
        "abs_return_acf_1": 0.364577198165181,
        "abs_return_acf_5": 0.3350757977694475,
        "abs_return_acf_20": 0.29473094638742975,
        "quantile_01": -0.06692558987898531,
        "quantile_99": 0.05271381234325781,
        "hill_tail_index": 2.9730182070172315
      }
    },
    {
      "asset": 29,
      "moments": {
        "daily_volatility": 0.017426111035481084,
        "excess_kurtosis": 6.185574983139414,
        "return_acf_1": -0.15821025814484346,
        "abs_return_acf_1": 0.37603752629539755,
        "abs_return_acf_5": 0.3221541169530868,
        "abs_return_acf_20": 0.21689864749365517,
        "quantile_01": -0.05433677159838114,
        "quantile_99": 0.04023637333420552,
        "hill_tail_index": 3.4297079676021793
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
