"""Stage D.2: train and validate the learning firm (research contract section 19).

  python run_stage_d.py baseline          # common pre-policy table: 96 training worlds, 3 check seeds
  python run_stage_d.py scenario B|I|F|IF # post-policy table on the frozen baseline: 64 worlds, 10 paired seeds

Archives go to runs/v2/ next to this script (local only). Each call refuses to overwrite an existing output.
Version 1 (no cost budget, seeds 30201-30296 ...) failed in training world 30214 and is kept in runs/v1/;
see failure_probe.py and research contract section 19.7.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.disclosure.training import train_and_evaluate  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

DOMAIN_PATH = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json"
CONFIG = MarketConfig(
    n_investors=1000, n_firms=200, trading_days=3500, burn_in_days=1200,
    initial_impact_share=0.2, taste_median=0.0724, imitation_rule="pairwise",
    financing_exposure_fraction=0.5, financing_spread=0.05, financing_repricing_interval=60,
    financing_horizon_days=1260, firm_discount_rate=0.05, intrinsic_value_log_sd=0.9151544344205937,
    firm_policy="q_learning", firm_action_fractions=(0.04, 0.2, 1.0),
    firm_learning_context="signal_tercile", firm_learning_rate_power=0.85,
    firm_cost_budget_fraction=0.01,
)
SWITCH_DAY = 1201
FOUR_TIMES_FINE = 0.00018245963214655838  # 4 x 1000 万元 in model units (contract 16.2, 16.5)
SCENARIOS = {
    "B": {},
    "I": {"transparency": 0.6},
    "F": {"fixed_fine": FOUR_TIMES_FINE},
    "IF": {"transparency": 0.6, "fixed_fine": FOUR_TIMES_FINE},
}
BASELINE_TRAINING = list(range(31201, 31297))
BASELINE_CHECK = [31301, 31302, 31303]
SCENARIO_TRAINING = list(range(31501, 31565))
VALIDATION = list(range(31401, 31411))
RESERVED = list(range(20261101, 20261131))
COVERAGE_TARGET = 20
RUNS = HERE / "runs" / "v2"


def baseline() -> dict:
    domain = load_domain(DOMAIN_PATH)
    return train_and_evaluate(CONFIG, domain, PolicySchedule.constant(domain), RUNS / "baseline",
                              training_seeds=BASELINE_TRAINING, validation_seeds=BASELINE_CHECK,
                              reserved_seeds=RESERVED, coverage_target=COVERAGE_TARGET)


def scenario(name: str) -> dict:
    domain = load_domain(DOMAIN_PATH)
    source = json.loads((RUNS / "baseline" / "summary.json").read_text(encoding="utf-8"))
    if source["status"] != "complete":
        raise RuntimeError("the common pre-policy training is not complete")
    policy = PolicySchedule.constant(domain).with_intervention(SWITCH_DAY, **SCENARIOS[name])
    return train_and_evaluate(CONFIG, domain, policy, RUNS / name,
                              training_seeds=SCENARIO_TRAINING, validation_seeds=VALIDATION,
                              reserved_seeds=RESERVED, coverage_target=COVERAGE_TARGET,
                              common_prepolicy_model=RUNS / "baseline" / "frozen_model.npz",
                              common_prepolicy_sha256=source["frozen_model_sha256"])


def main() -> int:
    disable_power_throttling()
    if sys.argv[1:] == ["baseline"]:
        summary = baseline()
    elif len(sys.argv) == 3 and sys.argv[1] == "scenario" and sys.argv[2] in SCENARIOS:
        summary = scenario(sys.argv[2])
    else:
        raise SystemExit(__doc__)
    print(json.dumps({"status": summary["status"], "coverage": summary["validation"]["coverage"]["status"]}))
    return 0 if summary["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
