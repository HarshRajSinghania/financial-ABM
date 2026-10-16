"""Decay grid: write the exploratory spec for uniform natural decay 0.05, 0.1, 0.15 SD/year (contract 20.16).

Each grid point repeats stage F block E (decay0_B/I/F/IF) with a different `natural_decay`; every other setting,
the seeds and the analysis metrics come from the stage F builder, so the derivation is identical. The two
endpoints (0 and 0.2) are not rerun: they are stage F's decay0_* and B/I/F/IF.

  python build_spec.py    # writes configs/disclosure_decay_grid_v1.json and checks the derivation against stage F
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STAGE_F = ROOT / "reports" / "disclosure_stage_f_20261014"

_spec = importlib.util.spec_from_file_location("stage_f_build_specs", STAGE_F / "build_specs.py")
stage_f = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(stage_f)

DECAYS = (0.05, 0.1, 0.15)
SEEDS = list(range(41001, 41031))  # stage F confirmatory seeds, kept for pairing (contract 20.7)
SPEC_PATH = ROOT / "configs" / "disclosure_decay_grid_v1.json"


def prefix(decay: float) -> str:
    return f"decay{stage_f.label(decay)}_"


def scenarios() -> list[dict]:
    return [stage_f.scenario(f"{prefix(decay)}{name}", changes, domain={"natural_decay": decay})
            for decay in DECAYS for name, changes in stage_f.POLICIES.items()]


def comparisons() -> list[dict]:
    rows = []
    for decay in DECAYS:
        p = prefix(decay)
        for plus, minus in (("I", "B"), ("F", "B"), ("I", "F"), ("IF", "B")):
            rows.append({"name": f"{p}{plus}_minus_{minus}", "weights": {f"{p}{plus}": 1, f"{p}{minus}": -1}})
    return rows


def spec() -> dict:
    stage_f_spec = stage_f.spec("confirmatory", SEEDS)
    return {
        "name": "disclosure_decay_grid_v1", "purpose": "development", "archive": "compact",
        "_note": "Exploratory supplement written after the stage F results (research contract 20.16); not "
                 "confirmatory. The runner only accepts development or confirmatory, so purpose is development. "
                 "Stage F block E with natural_decay 0.05, 0.1, 0.15 on the stage F confirmatory seeds; no "
                 "primary comparisons, so no Holm adjustment.",
        "domain": stage_f_spec["domain"], "market": stage_f_spec["market"], "seeds": SEEDS,
        "scenarios": scenarios(), "comparisons": comparisons(), "analysis": stage_f_spec["analysis"],
    }


def check_derivation() -> None:
    """Each new scenario, with natural_decay set back to 0, must equal stage F's frozen decay0_<policy>."""
    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure.experiments import freeze_spec

    new = {row["name"]: row for row in freeze_spec(SPEC_PATH)["scenarios"]}
    frozen = json.loads((STAGE_F / "confirmatory_v1" / "experiment.json").read_text(encoding="utf-8"))
    old = {row["name"]: row for row in frozen["scenarios"]}
    for decay in DECAYS:
        for name in stage_f.POLICIES:
            row = new[f"{prefix(decay)}{name}"]
            assert row["domain"]["natural_decay"] == decay
            reset = {**row, "name": f"decay0_{name}", "domain": {**row["domain"], "natural_decay": 0.0}}
            assert reset == old[f"decay0_{name}"], f"{row['name']} differs from stage F decay0_{name}"
            main = {**row, "name": name, "domain": {**row["domain"], "natural_decay": 0.2}}
            assert main == old[name], f"{row['name']} differs from stage F {name} beyond natural_decay"
    print("derivation check: every scenario equals stage F decay0_<policy> and <policy> except natural_decay")


def main() -> None:
    SPEC_PATH.write_text(json.dumps(spec(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(SPEC_PATH, len(scenarios()), "scenarios", len(comparisons()), "comparisons", len(SEEDS), "seeds")
    check_derivation()


if __name__ == "__main__":
    main()
