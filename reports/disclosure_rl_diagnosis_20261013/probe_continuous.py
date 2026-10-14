"""Stage D.1 probe: continuous-NPV choices on the same world as probe.py (baseline, main setting)."""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))
from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import load_domain  # noqa: E402
from abm.disclosure.game import DisclosureMarket  # noqa: E402
from abm.disclosure.policy import PolicySchedule  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402
from probe import DOMAIN_PATH, MAIN  # noqa: E402

def main(seed: int) -> None:
    disable_power_throttling()
    domain = load_domain(DOMAIN_PATH)
    start = time.perf_counter()
    market = DisclosureMarket(MarketConfig(seed=seed, firm_policy="npv", **MAIN), domain, PolicySchedule.constant(domain))
    result = market.run()
    actions, amounts = result.actions, result.amounts
    size = market.firms.size_class
    out = {"seed": seed, "seconds": time.perf_counter() - start,
           "actions_by_kind": np.bincount(actions.ravel(), minlength=3).tolist(),
           "by_size": {}}
    for cls, label in enumerate(("large", "mid", "small")):
        a, x = actions[:, size == cls], amounts[:, size == cls]
        out["by_size"][label] = {"share_improve": float((a == 0).mean()), "share_wash": float((a == 1).mean()),
                                 "improve_amount_quantiles_sd": np.quantile(x[a == 0], [.1, .5, .9]).tolist() if (a == 0).any() else None,
                                 "wash_amount_quantiles_sd": np.quantile(x[a == 1], [.1, .5, .9]).tolist() if (a == 1).any() else None}
    print(json.dumps(out, indent=2))
    (HERE / f"probe_continuous_{seed}.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30001)
