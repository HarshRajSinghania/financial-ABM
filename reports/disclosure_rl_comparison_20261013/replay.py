"""Stage D.2 research question (contract section 19.4): does the learning firm wash where NPV would not?

Replays each archived frozen Q-learning validation run with a read-only wrapper on the shared candidate
builder, recording the shared-grid NPV value of every candidate at every decision. The replay's result
fingerprint must equal the archived one. Writes replay.json.

Two measures: (1) the contract's (section 19.4): the chosen wash is worth less than maintain under the
shared-grid NPV; (2) added after the first replay, not in the contract: on the same candidates and legal
mask, the shared-grid NPV rule would not have washed (it prefers maintain or a real improvement).

Usage: python replay.py [--workers 12]
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abm.disclosure import game  # noqa: E402
from abm.disclosure.config import MarketConfig  # noqa: E402
from abm.disclosure.domain import DomainSpec  # noqa: E402
from abm.disclosure.game import MINIMUM_NPV, DisclosureMarket  # noqa: E402
from abm.disclosure.learning import INFLATE, MAINTAIN, CandidateSet, action_kinds, load_frozen, npv_discrete  # noqa: E402
from abm.disclosure.policy import PolicyRegime, PolicySchedule  # noqa: E402
from abm.platform_tuning import disable_power_throttling  # noqa: E402

RUNS = HERE / "runs" / "v2"
SCENARIOS = ("B", "I", "F", "IF")
WINDOW_START = 1200


def replay(folder: Path) -> dict:
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    learning = manifest["learning"]
    config = MarketConfig.from_dict(manifest["config"])
    domain = DomainSpec.from_dict(manifest["domain"])
    payload = manifest["policy"]
    policy = PolicySchedule(PolicyRegime(**payload["baseline"]),
                            None if payload["intervention"] is None else PolicyRegime(**payload["intervention"]),
                            payload["start_day"])
    learner, _ = load_frozen(folder / "input_model.npz", expected_sha256=manifest["artifacts"]["input_model.npz"])
    market = DisclosureMarket(config, domain, policy, learner=learner, training=False,
                              coverage_target=learning.get("coverage_target", 0),
                              common_prepolicy_sha256=learning.get("common_prepolicy_sha256"))
    values = []
    original = game.discrete_candidates

    def wrapped(**kwargs):
        result = original(**kwargs)
        values.append(result.values.copy())
        return result

    game.discrete_candidates = wrapped
    try:
        result = market.run()
    finally:
        game.discrete_candidates = original
    if result.fingerprint() != manifest["result_fingerprint"]:
        raise RuntimeError(f"replay of {folder} does not reproduce the archived result")
    values = np.stack(values)  # decision periods 1.. x firms x choices
    choices = result.learning_choices[1:]
    kinds = np.array(result.actions[1:])
    decision_days = np.arange(1, values.shape[0] + 1) * config.firm_decision_interval
    window = decision_days > WINDOW_START
    rows = np.arange(values.shape[1])
    chosen = np.stack([values[p, rows, choices[p]] for p in range(values.shape[0])])
    loss = values[:, :, MAINTAIN] - chosen  # NPV given up relative to maintain; > 0 means NPV would not choose it
    wash = (kinds == INFLATE) & window[:, None]
    # The archived legal mask already includes the value-anchor and budget rules applied after the builder.
    legal = result.valid_actions[1:]
    grid = action_kinds(values.shape[2])
    empty = np.zeros(values.shape[1:])
    npv_choice = np.stack([npv_discrete(CandidateSet(empty, empty, empty, values[p], legal[p], grid), MINIMUM_NPV)
                           for p in range(values.shape[0])])
    npv_value = np.take_along_axis(values, npv_choice[:, :, None], axis=2)[:, :, 0]
    npv_other = wash & (grid[npv_choice] != INFLATE)
    size = market.firms.size_class
    out = {"path": folder.relative_to(RUNS).as_posix(), "decisions": int(window.sum() * rows.size),
           "wash_decisions": int(wash.sum()),
           "wash_below_maintain": int((wash & (loss > 0)).sum()),
           "wash_loss_bp": (loss[wash & (loss > 0)] * 1e4).tolist(),
           "wash_where_npv_would_not": int(npv_other.sum()),
           "npv_choice_of_those": np.bincount(grid[npv_choice][npv_other], minlength=3).tolist(),
           "loss_vs_npv_choice_bp": ((npv_value - chosen)[npv_other] * 1e4).tolist(),
           "by_size": {}}
    for cls, label in enumerate(("large", "mid", "small")):
        member = wash & (size == cls)[None, :]
        out["by_size"][label] = {"wash_decisions": int(member.sum()), "wash_below_maintain": int((member & (loss > 0)).sum()),
                                 "wash_where_npv_would_not": int((npv_other & member).sum())}
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--scenarios", nargs="*", help="default: B I F IF; 'baseline' replays the check runs")
    args = parser.parse_args()
    names = args.scenarios or SCENARIOS
    folders = [folder for name in names for folder in sorted((RUNS / name / "validation").glob("seed_*/q_learning"))]
    with ProcessPoolExecutor(args.workers, initializer=disable_power_throttling) as pool:
        records = list(pool.map(replay, folders))
    summary = {}
    for name in names:
        rows = [row for row in records if row["path"].startswith(name + "/")]
        wash = sum(row["wash_decisions"] for row in rows)
        below = sum(row["wash_below_maintain"] for row in rows)
        losses = [value for row in rows for value in row["wash_loss_bp"]]
        other = sum(row["wash_where_npv_would_not"] for row in rows)
        other_losses = [value for row in rows for value in row["loss_vs_npv_choice_bp"]]
        summary[name] = {"worlds": len(rows), "decisions": sum(row["decisions"] for row in rows),
                         "wash_decisions": wash, "share_of_wash_below_maintain": below / wash if wash else None,
                         "median_npv_loss_bp": float(np.median(losses)) if losses else None,
                         "share_of_wash_where_npv_would_not": other / wash if wash else None,
                         "npv_choice_of_those_improve_wash_maintain": np.sum([row["npv_choice_of_those"] for row in rows], axis=0).tolist(),
                         "median_loss_vs_npv_choice_bp": float(np.median(other_losses)) if other_losses else None,
                         "by_size": {size: {key: sum(row["by_size"][size][key] for row in rows)
                                            for key in ("wash_decisions", "wash_below_maintain", "wash_where_npv_would_not")}
                                     for size in ("large", "mid", "small")}}
    for row in records:
        row.pop("wash_loss_bp")
        row.pop("loss_vs_npv_choice_bp")
    (HERE / ("replay.json" if names == SCENARIOS else "replay_check.json")).write_text(json.dumps({"summary": summary, "worlds": records}, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
