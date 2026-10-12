"""Conditional wash frontier: share of recorded decisions whose NPV choice would be washing at other fines.

Holds every recorded state, annuity and capacity fixed and recomputes only the choice (no feedback, no new
market path). The wash annuity and fine factor do not depend on transparency or the fine level when audit
results are unpublished and reporting is daily, which holds for these runs and is checked below.
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from diagnose import FIELDS, POLICY_START, SEEDS, replicate  # noqa: E402

PENALTIES = (0.0, 5e-5, 1e-4, 2e-4, 3.5e-4, 5e-4, 1e-3, 2e-3, 5e-3, 2e-2)
TRANSPARENCIES = (0.1, 0.6)


def main():
    diagnosis = json.loads((HERE / "diagnosis.json").read_text(encoding="utf-8"))
    runs = [row for row in diagnosis["runs"] if row["scenario"] == "market_B"]
    data = []
    for row in runs:
        path = HERE / "runs" / row["artifact"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["artifact_sha256"]
        with np.load(path) as bundle:
            data.append({field: bundle[field] for field in FIELDS})
    merged = {field: np.concatenate([item[field] for item in data]) for field in FIELDS}
    merged["wash_cost_ratio"] = 0.2
    window = merged["decision_day"] >= POLICY_START
    assert np.all(merged["subsidy"] == 0) and np.all(merged["audit_probability"] == merged["audit_probability"].flat[0])
    _, actions, _, _, _ = replicate(merged)
    assert np.array_equal(actions, merged["action"])
    frontier = []
    for transparency in TRANSPARENCIES:
        for penalty in PENALTIES:
            varied = dict(merged, transparency=np.full_like(merged["transparency"], transparency),
                          penalty=np.full_like(merged["penalty"], penalty))
            _, choice, _, _, _ = replicate(varied)
            selected = choice[window]
            frontier.append({"transparency": transparency, "penalty": penalty,
                             "share_wash": float(np.mean(selected == 1)), "share_improve": float(np.mean(selected == 0)),
                             "share_maintain": float(np.mean(selected == 2))})
    payload = {"source_runs": [row["artifact"] for row in runs], "seeds": SEEDS, "decisions": int(window.sum()),
               "scenario_states": "market_B (baseline audit probability, unpublished audits, daily reporting)",
               "frontier": frontier,
               "scope": "Conditional recomputation on fixed realized states; not a market counterfactual, equilibrium "
                        "or calibration target."}
    with (HERE / "conditional_frontier.json").open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    for row in frontier:
        print(row)


if __name__ == "__main__":
    main()
