"""Compare the unchanged continuous-NPV rule with pre-integration archives."""
import json
from pathlib import Path
import sys
import tempfile

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from abm.manifest import sha256_file
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import DomainSpec
from abm.disclosure.game import DisclosureMarket
from abm.disclosure.policy import PolicyRegime, PolicySchedule
from abm.disclosure.runner import save_result, source_hashes, write_json


def main():
    hashes = source_hashes()
    cases = []
    archive = ROOT / "reports/disclosure_information_development_20261011_v1"
    for scenario in ("contract_B", "zero_fine_public", "zero_fine_delay"):
        folder = archive / scenario / "seed_26001" / "attempt_001"
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        before = sha256_file(folder / "result.npz")
        assert before == manifest["artifacts"]["result.npz"]
        payload = manifest["policy"]
        policy = PolicySchedule(PolicyRegime(**payload["baseline"]),
                                PolicyRegime(**payload["intervention"]) if payload["intervention"] else None,
                                payload["start_day"])
        result = DisclosureMarket(MarketConfig.from_dict(manifest["config"]),
                                  DomainSpec.from_dict(manifest["domain"]), policy).run()
        assert result.fingerprint() == manifest["result_fingerprint"]
        with tempfile.TemporaryDirectory(prefix="abm-npv-compatibility-") as temporary:
            fresh = Path(temporary) / "result.npz"
            save_result(fresh, result)
            with np.load(fresh, allow_pickle=False) as current, np.load(folder / "result.npz", allow_pickle=False) as old:
                assert set(current.files) == set(old.files)
                for name in old.files:
                    assert current[name].dtype == old[name].dtype and current[name].shape == old[name].shape
                    assert current[name].tobytes() == old[name].tobytes(), name
                fields = len(old.files)
        assert sha256_file(folder / "result.npz") == before
        cases.append({"scenario": scenario, "seed": 26001, "status": "PASS", "fields_compared": fields,
                      "result_fingerprint": result.fingerprint(), "original_result_unchanged": True})
    assert source_hashes() == hashes
    write_json(Path(__file__).with_name("npv_compatibility.json"), {
        "status": "PASS", "scope": "Three archived 1800-day NPV paths; not a proof for every parameter setting.",
        "source_hashes": hashes, "cases": cases,
    })
    print(json.dumps({"status": "PASS", "cases": len(cases)}))


if __name__ == "__main__":
    main()
