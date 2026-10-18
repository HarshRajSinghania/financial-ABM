"""Feedback in stronger markets: write the exploratory spec (research contract 20.18).

Three cells of stage F phase map 1 (taste_median x initial II probability), each with the stage F policies
B, I (transparency 0.6) and F (fixed fine 4x) switched in on day 1201. Stage F ran only B in these cells.
Every scenario comes from the stage F builder, so the derivation is identical; the checks below compare the
frozen scenarios with stage F's frozen ones item by item.

  python build_spec.py    # writes configs/disclosure_feedback_strong_v1.json and checks the derivation
"""

from __future__ import annotations

import importlib.util
import json
import platform
import sys
from pathlib import Path


def _no_wmi(*args, **kwargs):
    raise OSError("WMI not queried")


# The machine's WMI service hangs since 2026-10-16; Python 3.12's platform module would wait on it forever
# when numpy is imported (see counterfactual.py of contract 20.17). No identity depends on it.
platform._wmi_query = _no_wmi

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STAGE_F = ROOT / "reports" / "disclosure_stage_f_20261014"

_spec = importlib.util.spec_from_file_location("stage_f_build_specs", STAGE_F / "build_specs.py")
stage_f = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(stage_f)

CELLS = ((2 * stage_f.TASTE, 0.8), (2 * stage_f.TASTE, 0.2), (stage_f.TASTE, 0.8))  # (taste_median, initial II share)
POLICIES = ("B", "I", "F")
SEEDS = list(range(41001, 41031))  # stage F confirmatory seeds, kept for pairing (contract 20.7)
SPEC_PATH = ROOT / "configs" / "disclosure_feedback_strong_v1.json"


def cell_name(taste: float, share: float) -> str:
    """The stage F phase map 1 label without its pm1_ prefix, e.g. t0p1448_s0p8."""
    return f"t{stage_f.label(round(taste, 4))}_s{stage_f.label(share)}"


def scenarios() -> list[dict]:
    return [stage_f.scenario(f"{cell_name(taste, share)}_{name}", stage_f.POLICIES[name],
                             market={"taste_median": taste, "initial_impact_share": share})
            for taste, share in CELLS for name in POLICIES]


def comparisons() -> list[dict]:
    rows = []
    for taste, share in CELLS:
        cell = cell_name(taste, share)
        for plus, minus in (("I", "B"), ("F", "B"), ("I", "F")):
            rows.append({"name": f"{cell}_{plus}_minus_{minus}", "weights": {f"{cell}_{plus}": 1, f"{cell}_{minus}": -1}})
    return rows


def spec() -> dict:
    stage_f_spec = stage_f.spec("confirmatory", SEEDS)
    return {
        "name": "disclosure_feedback_strong_v1", "purpose": "development", "archive": "compact",
        "_note": "Exploratory supplement written after the stage F results and the feedback counterfactual "
                 "(research contract 20.18); not confirmatory. The runner only accepts development or "
                 "confirmatory, so purpose is development. Stage F phase map 1 cells taste 0.1448 x II 0.8, "
                 "0.1448 x 0.2 and 0.0724 x 0.8, each under B, I (transparency 0.6) and F (fixed fine 4x), on "
                 "the stage F confirmatory seeds; no primary comparisons, so no Holm adjustment.",
        "domain": stage_f_spec["domain"], "market": stage_f_spec["market"], "seeds": SEEDS,
        "scenarios": scenarios(), "comparisons": comparisons(), "analysis": stage_f_spec["analysis"],
    }


def check_derivation() -> None:
    """Item-by-item comparison of the frozen scenarios with stage F's frozen ones.

    Each cell's B equals stage F's pm1_<cell>; each cell's I and F differ from that B only in the policy, and
    equal stage F's I and F once taste_median and initial_impact_share are set back to the main setting.
    """
    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure.experiments import freeze_spec

    new = {row["name"]: row for row in freeze_spec(SPEC_PATH)["scenarios"]}
    frozen = json.loads((STAGE_F / "confirmatory_v1" / "experiment.json").read_text(encoding="utf-8"))
    old = {row["name"]: row for row in frozen["scenarios"]}
    main_market = {"taste_median": stage_f.MARKET["taste_median"], "initial_impact_share": stage_f.MARKET["initial_impact_share"]}
    for taste, share in CELLS:
        cell = cell_name(taste, share)
        base = new[f"{cell}_B"]
        assert base["config"]["taste_median"] == taste and base["config"]["initial_impact_share"] == share
        assert {**base, "name": f"pm1_{cell}"} == old[f"pm1_{cell}"], f"{cell}_B differs from stage F pm1_{cell}"
        for name in POLICIES:
            row = new[f"{cell}_{name}"]
            assert {**row, "name": base["name"], "policy": base["policy"]} == base, f"{row['name']} differs from {cell}_B beyond the policy"
            reset = {**row, "name": name, "config": {**row["config"], **main_market}}
            assert reset == old[name], f"{row['name']} differs from stage F {name} beyond taste_median and initial_impact_share"
    print("derivation check: each <cell>_B equals stage F pm1_<cell>; each <cell>_I/F differs from it only in the "
          "policy and equals stage F I/F once taste_median and initial_impact_share are reset")


def main() -> None:
    SPEC_PATH.write_text(json.dumps(spec(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(SPEC_PATH, len(scenarios()), "scenarios", len(comparisons()), "comparisons", len(SEEDS), "seeds")
    check_derivation()


if __name__ == "__main__":
    main()
