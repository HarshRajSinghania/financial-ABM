"""Check daily-report compatibility on six existing archived paths."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CASES = (
    ("disclosure_action_grid_development_20261011_v1/training/seed_27001", 41),
    ("disclosure_action_grid_development_20261011_v1/validation/seed_27304/q_learning", 41),
    ("disclosure_action_grid_development_20261011_v1/validation/seed_27304/npv_discrete", 40),
    ("disclosure_action_grid_development_20261011_v1/validation/seed_27304/npv", 31),
    ("disclosure_information_development_20261011_v1/zero_fine_public/seed_26001/attempt_001", 31),
    ("disclosure_information_development_20261011_v1/zero_fine_delay/seed_26001/attempt_001", 31),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay(folder, expected_fields, temporary):
    from abm.disclosure.config import MarketConfig
    from abm.disclosure.domain import DomainSpec
    from abm.disclosure.game import DisclosureMarket
    from abm.disclosure.learning import load_frozen, table_fingerprint
    from abm.disclosure.policy import PolicyRegime, PolicySchedule
    from abm.disclosure.runner import load_result, save_result

    manifest_path = folder / "manifest.json"
    manifest_hash = sha(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["status"] == "complete"
    assert manifest["python_version"] == platform.python_version()
    assert manifest["numpy_version"] == np.__version__
    original_hashes = {name: sha(folder / name) for name in manifest["artifacts"]}
    assert original_hashes == manifest["artifacts"]
    config = MarketConfig.from_dict(manifest["config"])
    assert config.trading_days == 1800
    stored_policy = manifest["policy"]
    policy = PolicySchedule(
        PolicyRegime(**stored_policy["baseline"]),
        PolicyRegime(**stored_policy["intervention"]) if stored_policy["intervention"] else None,
        stored_policy["start_day"],
    )
    assert policy.baseline.reporting_interval_days == 1
    assert policy.intervention is None or policy.intervention.reporting_interval_days == 1
    old_result = load_result(folder / "result.npz")
    assert old_result.fingerprint() == manifest["result_fingerprint"]
    learning = manifest.get("learning") or {}
    learner = None
    initial_table = None
    if learning:
        learner, _ = load_frozen(folder / "input_model.npz")
        initial_table = table_fingerprint(learner)
        assert initial_table == learning["initial_table_fingerprint"]
        assert learner.learning_rate == learning["learning_rate"]
        assert learner.discount == learning["discount"]
        if learning["training"]:
            learner.values, learner.counts = learner.values.copy(), learner.counts.copy()
        learner.epsilon = learning["epsilon"]
    started = time.perf_counter()
    market = DisclosureMarket(config, DomainSpec.from_dict(manifest["domain"]), policy,
                              learner=learner, training=learning.get("training", False))
    result = market.run()
    fresh = temporary / "result.npz"
    save_result(fresh, result)
    fields = []
    with np.load(fresh, allow_pickle=False) as new, np.load(folder / "result.npz", allow_pickle=False) as old:
        assert set(new.files) == set(old.files)
        assert len(old.files) == expected_fields
        for name in sorted(old.files):
            before, after = old[name], new[name]
            assert before.dtype == after.dtype and before.shape == after.shape, name
            assert before.tobytes() == after.tobytes(), name
            fields.append({"name": name, "dtype": str(before.dtype), "shape": list(before.shape),
                           "bytes_sha256": hashlib.sha256(before.tobytes()).hexdigest(), "equal": True})
    assert result.fingerprint() == manifest["result_fingerprint"]
    table = {"status": "not_applicable"}
    if learner is not None:
        final, _ = load_frozen(folder / "output_model.npz")
        for name in ("values", "counts"):
            before, after = getattr(final, name), getattr(learner, name)
            assert before.dtype == after.dtype and before.shape == after.shape, name
            assert before.tobytes() == after.tobytes(), name
        final_table = table_fingerprint(learner)
        stored_learning = json.loads((folder / "learning.json").read_text(encoding="utf-8"))
        assert final_table == stored_learning["final_table_fingerprint"] == table_fingerprint(final)
        assert int(learner.counts.sum()) == stored_learning["final_transition_count"]
        if not learning["training"]:
            assert final_table == initial_table
        table = {"status": "PASS", "initial_table_fingerprint": initial_table,
                 "final_table_fingerprint": final_table, "count_sum": int(learner.counts.sum()),
                 "values_and_counts_bitwise_equal": True}
    assert original_hashes == {name: sha(folder / name) for name in original_hashes}
    assert manifest_hash == sha(manifest_path)
    return {"archive": folder.relative_to(ROOT).as_posix(), "status": "PASS",
            "seed": config.seed, "rule": config.firm_policy, "training": learning.get("training", False),
            "elapsed_seconds": time.perf_counter() - started, "bitwise_equal_fields": len(fields),
            "fields": fields, "result_fingerprint": result.fingerprint(), "final_table": table,
            "original_run_id": manifest["run_id"], "current_market_run_id": market.run_id,
            "original_source_hashes": manifest["source_hashes"], "manifest_sha256": manifest_hash,
            "original_artifact_hashes": original_hashes, "original_archives_unchanged": True,
            "original_validation": json.loads((folder / "validation.json").read_text(encoding="utf-8"))}


def main():
    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure import game
    from abm.disclosure.runner import source_hashes, write_json

    assert Path(game.__file__).resolve() == ROOT / "src/abm/disclosure/game.py"
    manifest_path, output = HERE / "compatibility_manifest.json", HERE / "compatibility.json"
    if manifest_path.exists() or output.exists():
        raise FileExistsError("Compatibility outputs already exist; preserve this attempt.")
    frozen_source = source_hashes()
    stamp = {"created_utc": datetime.now(timezone.utc).isoformat(), "script_sha256": sha(Path(__file__)),
             "current_source_hashes": frozen_source, "python_version": platform.python_version(),
             "numpy_version": np.__version__, "cases": [{"archive": "reports/" + path,
                                                        "expected_fields": count} for path, count in CASES],
             "purpose": "daily_reporting_backward_compatibility",
             "budget": {"replays": len(CASES), "days_each": 1800, "new_seeds": 0, "reporting_interval_days": 1},
             "limitations": ["Archived Q tables are loaded directly for compatibility only; their old research contracts are not accepted for new studies.",
                             "Current source and policy identities differ from the archived identities; only specified result arrays, fingerprints and final tables must agree.",
                             "Reproduction does not override archived market failures, coverage failures or empirical pending status."]}
    with manifest_path.open("x", encoding="utf-8") as handle:
        json.dump(stamp, handle, ensure_ascii=False, allow_nan=False, indent=2)
        handle.write("\n")
    report = {"status": "running", "planned_cases": len(CASES), "completed_cases": 0, "manifest": stamp, "cases": []}
    write_json(output, report)
    active_case = None
    try:
        with tempfile.TemporaryDirectory(prefix="abm-reporting-compatibility-") as temporary:
            for path, expected_fields in CASES:
                active_case = "reports/" + path
                assert source_hashes() == frozen_source
                case = replay(ROOT / active_case, expected_fields, Path(temporary))
                assert source_hashes() == frozen_source
                report["cases"].append(case)
                report["completed_cases"] = len(report["cases"])
                write_json(output, report)
                print(json.dumps({"completed": len(report["cases"]), "planned": len(CASES),
                                  "case": active_case, "status": case["status"]}), flush=True)
        assert stamp["script_sha256"] == sha(Path(__file__))
        assert source_hashes() == frozen_source
        report["status"] = "PASS"
        report["source_unchanged"] = True
        write_json(output, report)
    except BaseException as error:
        report["status"] = "FAIL"
        report["error"] = {"type": type(error).__name__, "message": str(error), "archive": active_case}
        try:
            write_json(output, report)
        except Exception as secondary:
            print(f"Could not save compatibility failure: {secondary}", file=sys.stderr, flush=True)
        raise


if __name__ == "__main__":
    main()
