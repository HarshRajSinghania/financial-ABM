"""Read-only probe of the failed training world 30214 (contract section 19.5).

Replays the archived input table for that world with a wrapper on _pre_trade that records, every day, each
firm's intrinsic value, price, financing adjustment, and cumulative resource cost and fines, up to the failure.
Also replays the same seed with the continuous-NPV and shared-grid NPV rules to see whether they survive.
"""

from __future__ import annotations

import json
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))
sys.path.insert(0, str(HERE))

from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import DomainSpec  # noqa: E402
from abm.disclosure.game import DisclosureMarket  # noqa: E402
from abm.disclosure.learning import load_frozen  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

FOLDER = HERE / "runs" / "v1" / "baseline" / "training" / "seed_30214"


def probe(market: DisclosureMarket) -> dict:
    rows = []
    original = market._pre_trade

    def wrapped(day):
        before = market.firms.intrinsic_value.copy()
        try:
            return original(day)
        finally:
            rows.append((day, before, market.firms.intrinsic_value.copy(), market.prices.copy(),
                         market.contract_rate.copy()))

    market._pre_trade = wrapped
    error = None
    try:
        market.run()
    except ValueError as exc:
        error = str(exc)
    values = np.stack([row[2] for row in rows])
    firm = int(np.argmin(values[-1]))
    initial = values[0]
    out = {"error": error, "days": len(rows), "firm": firm,
           "size_class": int(market.firms.size_class[firm]),
           "initial_value": float(initial[firm]),
           "exposure": float(market.financing_exposure[firm]),
           "value_path": [float(values[d, firm]) for d in range(0, len(rows), 250)] + [float(values[-1, firm])],
           "price_path": [float(rows[d][3][firm]) for d in range(0, len(rows), 250)] + [float(rows[-1][3][firm])],
           "rate_path": [float(rows[d][4][firm]) for d in range(0, len(rows), 250)] + [float(rows[-1][4][firm])],
           "min_value_ratio_all_firms": float((values[-1] / initial).min())}
    if market.action_history is not None:
        actions = market.action_history[:, firm]
        out["actions_by_kind"] = np.bincount(actions[actions >= 0], minlength=3).tolist()
        out["cost_fraction_sum"] = float(market.cost_history[:, firm].sum())
        out["penalty_fraction_sum"] = float(market.penalty_history[:, firm].sum())
    return out


def main() -> None:
    disable_power_throttling()
    manifest = json.loads((FOLDER / "manifest.json").read_text(encoding="utf-8"))
    config = MarketConfig.from_dict(manifest["config"])
    domain = DomainSpec.from_dict(manifest["domain"])
    policy = PolicySchedule.constant(domain)
    learner, _ = load_frozen(FOLDER / "input_model.npz")
    learner.values.flags.writeable = learner.counts.flags.writeable = True
    learner.epsilon = manifest["learning"]["epsilon"]
    result = {"q_learning": probe(DisclosureMarket(config, domain, policy, learner=learner, training=True,
                                                   coverage_target=manifest["learning"].get("coverage_target", 0)))}
    for rule in ("npv", "npv_discrete"):
        result[rule] = probe(DisclosureMarket(replace(config, firm_policy=rule), domain, policy))
    (HERE / "failure_probe.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
