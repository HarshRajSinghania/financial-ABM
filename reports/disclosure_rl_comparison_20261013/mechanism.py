"""Stage D.2, post hoc (not in contract section 19): why does the frozen learner wash so often?

Reads a frozen table and the archived frozen Q-learning validation runs of one experiment and reports:
1. by signal tercile and current-inflation feature, the share of states whose greedy choice is a wash, and
   the mean greedy value;
2. in the validation runs, the mean next-period reward by the firm's signal tercile, among firms that chose
   to maintain (no action of their own), i.e. how much of a tercile's value is selection, not the action;
3. how often a wash moves the firm up a tercile by the next decision.

Usage: python mechanism.py [experiment, default baseline]
       python mechanism.py tables   # the two section-7 tables of the README -> mechanism_tables.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs" / "v2"
KINDS = np.array([0, 1, 2, 0, 1, 0, 1])  # improve, wash, maintain by internal choice
GROUPS = 3


def main(name: str) -> dict:
    with np.load(RUNS / name / "frozen_model.npz") as model:
        values, counts = model["values"], model["counts"]
    states = np.arange(81)
    tercile, inflation = states // 27, (states // 9) % 3
    out: dict = {"experiment": name, "table": []}
    for group in range(values.shape[0]):
        if counts[group].sum() == 0:
            continue
        for t in range(3):
            for f in range(3):
                member = (tercile == t) & (inflation == f) & (counts[group].sum(axis=1) > 0)
                if not member.any():
                    continue
                greedy = np.argmax(values[group, member], axis=1)
                out["table"].append({"group": group, "tercile": t, "inflation_feature": f, "states": int(member.sum()),
                                     "greedy_wash_share": float((KINDS[greedy] == 1).mean()),
                                     "mean_greedy_value_bp": float(values[group, member].max(axis=1).mean() * 1e4)})
    rewards = {t: [] for t in range(3)}
    moves = {"wash": [0, 0], "maintain": [0, 0], "improve": [0, 0]}
    for folder in sorted((RUNS / name / "validation").glob("seed_*/q_learning")):
        with np.load(folder / "result.npz") as data:
            s, r, c, tr = data["learning_states"], data["learning_rewards"], data["learning_choices"], data["learning_transition"]
        for p in range(1, s.shape[0] - 1):
            if not tr[p + 1].all():
                continue
            t_now, t_next = s[p] // 27, s[p + 1] // 27
            kind = KINDS[c[p]]
            for t in range(3):
                rewards[t].extend((r[p + 1][(t_now == t) & (kind == 2)] * 1e4).tolist())
            for label, k in (("improve", 0), ("wash", 1), ("maintain", 2)):
                member = kind == k
                moves[label][0] += int((t_next[member] > t_now[member]).sum())
                moves[label][1] += int(member.sum())
    out["maintain_next_reward_bp_by_tercile"] = {str(t): {"mean": float(np.mean(v)), "n": len(v),
                                                         "se": float(np.std(v) / np.sqrt(len(v)))}
                                                 for t, v in rewards.items() if v}
    out["share_moving_up_a_tercile"] = {k: (v[0] / v[1] if v[1] else None) for k, v in moves.items()}
    (HERE / f"mechanism_{name}.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out


def rewards_by_state(name: str) -> dict:
    """Section 7: next-period reward by current-inflation feature x action kind (all decisions after day 60)."""
    table: dict[str, list] = {}
    for folder in sorted((RUNS / name / "validation").glob("seed_*/q_learning")):
        with np.load(folder / "result.npz") as data:
            s, r, c, tr = data["learning_states"], data["learning_rewards"], data["learning_choices"], data["learning_transition"]
        for p in range(1, s.shape[0] - 1):
            if not tr[p + 1].all():
                continue
            inflation, kind = (s[p] // 9) % 3, KINDS[c[p]]
            for f in range(3):
                for k, label in enumerate(("improve", "wash", "maintain")):
                    table.setdefault(f"inflation_{f}_{label}", []).extend((r[p + 1][(inflation == f) & (kind == k)] * 1e4).tolist())
    return {key: {"n": len(v), "mean_bp": float(np.mean(v))} for key, v in table.items() if v}


def clean_state_split(name: str, first_period: int = 21) -> dict:
    """Section 7 (b): in the policy window, clean-state decisions split by a same-day detection and by stage."""
    table: dict[str, list] = {}
    for folder in sorted((RUNS / name / "validation").glob("seed_*/q_learning")):
        with np.load(folder / "result.npz") as data:
            s, r, tr, detected = data["learning_states"], data["learning_rewards"], data["learning_transition"], data["detections"]
        for p in range(first_period, s.shape[0] - 1):
            if not tr[p + 1].all():
                continue
            inflation, stage = (s[p] // 9) % 3, s[p] % 3
            for i in range(s.shape[1]):
                key = "inflated" if inflation[i] else f"{'detected' if detected[p, i] else 'voluntary'}_stage_{stage[i]}"
                table.setdefault(key, []).append(r[p + 1, i] * 1e4)
    return {key: {"n": len(v), "mean_bp": float(np.mean(v))} for key, v in sorted(table.items())}


def tables() -> None:
    out = {"rewards_by_state_baseline_check": rewards_by_state("baseline"),
           "clean_state_split": {name: clean_state_split(name) for name in ("B", "F")}}
    (HERE / "mechanism_tables.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["tables"]:
        tables()
    else:
        result = main(sys.argv[1] if len(sys.argv) > 1 else "baseline")
        for row in result["table"]:
            if row["group"] < 3:
                print(row)
        print(json.dumps({k: v for k, v in result.items() if k not in ("table",)}, indent=2))
