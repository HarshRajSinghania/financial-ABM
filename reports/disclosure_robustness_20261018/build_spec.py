"""Robustness checks: write the exploratory spec for contract 20.21 and check it against stage F.

Three groups, each a stage F block with one new option switched on; every other setting, the seeds and the
analysis metrics come from the stage F builder, so the derivation is identical.

  R  reverting true values: block E (decay0_B/I/F/IF, no uniform decay) with natural_reversion 0.32 and 0.5
  P  one fixed fine per inflated report from day 0: B, I, F, IF and the fixed-fine doses 0x, 2x, 8x
  W  firm-level wash cost ratios, lognormal with log SD ln 2 around 0.2: B, I_0p3, I, I_0p8 and F

  python build_spec.py [--stage-f <stage F confirmatory archive>]

Writes configs/disclosure_robustness_v1.json (confirmatory seeds) and configs/disclosure_robustness_check_v1.json
(development seeds 33001-33002, pipeline check only), then checks that every scenario, with its new option set
back to the default, equals the frozen stage F scenario it was derived from.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STAGE_F = ROOT / "reports" / "disclosure_stage_f_20261014"

_spec = importlib.util.spec_from_file_location("stage_f_build_specs", STAGE_F / "build_specs.py")
stage_f = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(stage_f)

SEEDS = list(range(41001, 41031))   # stage F confirmatory seeds, kept for pairing (contract 20.7)
CHECK_SEEDS = [33001, 33002]        # stage F development seeds; the runner needs at least two
REVERSIONS = (0.32, 0.5)            # contract 20.21 group R, upper bounds from the Huazheng panel
WASH_LOG_SD = math.log(2)           # contract 20.21 group W
F1 = stage_f.F1
POLICIES = stage_f.POLICIES
DOSES = {"F_0x": {"fixed_fine": 0.0}, "F_2x": {"fixed_fine": 2 * F1}, "F_8x": {"fixed_fine": 8 * F1}}
TAUS = {"I_0p3": {"transparency": 0.3}, "I": POLICIES["I"], "I_0p8": {"transparency": 0.8}}
SPEC_PATH = ROOT / "configs" / "disclosure_robustness_v1.json"
CHECK_PATH = ROOT / "configs" / "disclosure_robustness_check_v1.json"


def reversion_prefix(kappa: float) -> str:
    return f"rev{stage_f.label(kappa)}_"


def groups() -> dict[str, list[tuple[str, str, dict]]]:
    """Group -> (new scenario, stage F scenario it derives from, scenario keyword arguments)."""
    rows: dict[str, list] = {"R": [], "P": [], "W": []}
    for kappa in REVERSIONS:
        for name, changes in POLICIES.items():
            rows["R"].append((f"{reversion_prefix(kappa)}{name}", f"decay0_{name}",
                              {"changes": changes, "domain": {"natural_decay": 0.0, "natural_reversion": kappa}}))
    for name, changes in {**POLICIES, **DOSES}.items():
        rows["P"].append((f"rep_{name}", name, {"changes": changes, "baseline": {"fixed_fine_basis": "report"}}))
    for name, changes in {"B": {}, **TAUS, "F": POLICIES["F"]}.items():
        rows["W"].append((f"wlog_{name}", name, {"changes": changes, "domain": {"wash_cost_log_sd": WASH_LOG_SD}}))
    return rows


def scenarios() -> list[dict]:
    out = []
    for rows in groups().values():
        for name, _, options in rows:
            changes = options.get("changes") or None
            out.append(stage_f.scenario(name, changes, domain=options.get("domain"), baseline=options.get("baseline")))
    return out


def comparisons() -> list[dict]:
    rows = []

    def add(plus: str, minus: str) -> None:
        rows.append({"name": f"{plus}_minus_{minus}", "weights": {plus: 1, minus: -1}})

    for prefix in [reversion_prefix(k) for k in REVERSIONS] + ["rep_", "wlog_"]:
        for plus, minus in (("I", "B"), ("F", "B"), ("I", "F")):
            add(prefix + plus, prefix + minus)
    for prefix in [reversion_prefix(k) for k in REVERSIONS] + ["rep_"]:
        add(prefix + "IF", prefix + "B")
    for plus, minus in (("F_0x", "B"), ("F_2x", "B"), ("F_8x", "B"), ("F_2x", "F_0x"), ("F", "F_2x"), ("F_8x", "F")):
        add("rep_" + plus, "rep_" + minus)
    for tau in ("I_0p3", "I_0p8"):
        add("wlog_" + tau, "wlog_B")
    return rows


def spec(seeds: list[int], name: str) -> dict:
    stage_f_spec = stage_f.spec("confirmatory", SEEDS)
    return {
        "name": name, "purpose": "development", "archive": "compact",
        "_note": "Exploratory robustness checks written after the stage F results (research contract 20.21); not "
                 "confirmatory. The runner only accepts development or confirmatory, so purpose is development. "
                 "Group R: block E with natural_reversion 0.32 and 0.5; group P: fixed_fine_basis report from day 0; "
                 "group W: wash_cost_log_sd ln 2. No primary comparisons, so no Holm adjustment.",
        "domain": stage_f_spec["domain"], "market": stage_f_spec["market"], "seeds": seeds,
        "scenarios": scenarios(), "comparisons": comparisons(), "analysis": stage_f_spec["analysis"],
    }


def reset(row: dict, group: str, old_name: str) -> dict:
    """The new scenario with its option set back to the default (omitted, as the serializers do)."""
    row = json.loads(json.dumps(row))
    row["name"] = old_name
    if group == "R":
        assert row["domain"].pop("natural_reversion") in REVERSIONS
    elif group == "W":
        assert row["domain"].pop("wash_cost_log_sd") == WASH_LOG_SD
    else:
        for regime in ("baseline", "intervention"):
            if row["policy"][regime] is not None:
                assert row["policy"][regime].pop("fixed_fine_basis") == "report"
    return row


def check_derivation(stage_f_archive: Path) -> None:
    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure.experiments import freeze_spec

    new = {row["name"]: row for row in freeze_spec(SPEC_PATH)["scenarios"]}
    frozen = json.loads((stage_f_archive / "experiment.json").read_text(encoding="utf-8"))
    old = {row["name"]: row for row in frozen["scenarios"]}
    count = 0
    for group, rows in groups().items():
        for name, old_name, _ in rows:
            assert reset(new[name], group, old_name) == old[old_name], f"{name} differs from stage F {old_name}"
            count += 1
    # Group R also differs from the stage F main setting only in the decay form.
    for kappa in REVERSIONS:
        for name in POLICIES:
            row = json.loads(json.dumps(new[f"{reversion_prefix(kappa)}{name}"]))
            row["name"], row["domain"]["natural_decay"] = name, 0.2
            row["domain"].pop("natural_reversion")
            assert row == old[name]
    print(f"derivation check: {count} scenarios equal their stage F scenario once the new option is reset")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage-f", type=Path, default=STAGE_F / "confirmatory_v1",
                        help="stage F confirmatory archive (read-only)")
    args = parser.parse_args()
    for path, seeds, name in ((SPEC_PATH, SEEDS, "disclosure_robustness_v1"),
                              (CHECK_PATH, CHECK_SEEDS, "disclosure_robustness_check_v1")):
        path.write_text(json.dumps(spec(seeds, name), indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(path, len(scenarios()), "scenarios", len(comparisons()), "comparisons", len(seeds), "seeds")
    check_derivation(args.stage_f)


if __name__ == "__main__":
    main()
