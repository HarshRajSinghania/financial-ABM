"""Replay four archived paths with the optional learning protocol disabled."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import runpy
import sys
import tempfile

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VERIFIER = ROOT / "reports/disclosure_reporting_checks_20261011/compatibility.py"
VERIFIER_SHA256 = "0e58a14be0219c70119746bc240f0aaa1eb87bb13ef63af450b2232e27bc2a3c"


def main():
    assert hashlib.sha256(VERIFIER.read_bytes()).hexdigest() == VERIFIER_SHA256
    previous = runpy.run_path(str(VERIFIER))
    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure.runner import source_hashes, write_json

    manifest_path, output = HERE / "compatibility_manifest.json", HERE / "compatibility.json"
    if manifest_path.exists() or output.exists():
        raise FileExistsError("Preserve the existing compatibility attempt.")
    sources = source_hashes()
    cases = previous["CASES"][:4]
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "replay_verifier_sha256": VERIFIER_SHA256,
        "current_source_hashes": sources,
        "python_version": platform.python_version(), "numpy_version": np.__version__,
        "cases": [{"archive": "reports/" + path, "expected_fields": count} for path, count in cases],
        "budget": {"replays": 4, "days_each": 1800, "new_seeds": 0},
        "options": {"coverage_target": 0, "common_prepolicy_sha256": None},
        "scope": "Result arrays, fingerprints, and final Q/counts; old research contracts are bypassed only for this compatibility replay.",
        "limitations": ["Reproduction preserves all original market and coverage failures and empirical pending states."],
    }
    with manifest_path.open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, allow_nan=False, indent=2)
    report = {"status": "running", "manifest": manifest, "cases": []}
    write_json(output, report)
    try:
        with tempfile.TemporaryDirectory(prefix="abm-learning-compatibility-") as temporary:
            for path, expected_fields in cases:
                assert source_hashes() == sources
                case = previous["replay"](ROOT / "reports" / path, expected_fields, Path(temporary))
                assert source_hashes() == sources
                report["cases"].append(case)
                write_json(output, report)
                print(json.dumps({"completed": len(report["cases"]), "planned": 4, "archive": path, "status": case["status"]}), flush=True)
        assert source_hashes() == sources
        assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == manifest["script_sha256"]
        assert hashlib.sha256(VERIFIER.read_bytes()).hexdigest() == VERIFIER_SHA256
        report.update(status="PASS", source_unchanged=True)
        write_json(output, report)
    except BaseException as error:
        report.update(status="FAIL", error={"type": type(error).__name__, "message": str(error)})
        write_json(output, report)
        raise


if __name__ == "__main__":
    main()
