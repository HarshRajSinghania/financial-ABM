"""Execute the declared Q-learning integration budget from isolated source."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parents[2]
    spec_path = root / "configs/disclosure_q_learning_smoke_v1.json"
    specification = json.loads(spec_path.read_text(encoding="utf-8"))
    source_parent = root / "src"
    sources = {path.relative_to(source_parent).as_posix(): path.read_bytes()
               for path in sorted((source_parent / "abm").rglob("*.py"))}
    expected = {name: hashlib.sha256(value).hexdigest() for name, value in sources.items()}
    output = root / "reports/disclosure_q_learning_smoke_20261011_v1"
    if output.exists():
        raise FileExistsError(output)
    with tempfile.TemporaryDirectory(prefix="abm-q-learning-source-") as temporary:
        snapshot = Path(temporary).resolve()
        for name, value in sources.items():
            path = snapshot / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
        if any(hashlib.sha256((source_parent / name).read_bytes()).hexdigest() != digest
               for name, digest in expected.items()):
            raise RuntimeError("source changed while creating the snapshot")
        sys.path.insert(0, str(snapshot))
        from abm.disclosure.config import MarketConfig
        from abm.disclosure.domain import load_domain
        from abm.disclosure.runner import source_hashes, write_json
        from abm.disclosure.training import train_and_evaluate
        assert source_hashes() == expected
        result = train_and_evaluate(
            MarketConfig.from_dict(specification["market"]),
            load_domain(spec_path.parent / specification["domain"]), None, output,
            training_seeds=specification["training_seeds"], validation_seeds=specification["validation_seeds"],
            reserved_seeds=specification["reserved_seeds"],
        )
        assert result["contract"]["source_hashes"] == expected
        write_json(output / "declared_spec.json", specification)
        write_json(output / "summary_manifest.json", {
            "experiment_id": result["experiment_id"], "source_hashes": expected,
            "artifacts": {name: hashlib.sha256((output / name).read_bytes()).hexdigest()
                          for name in ("experiment.json", "summary.json", "declared_spec.json",
                                       "initial_model.npz", "frozen_model.npz")},
        })
        print(json.dumps({"experiment_id": result["experiment_id"], "status": result["status"],
                          "validation": {key: value["status"] for key, value in result["validation"].items()}}))


if __name__ == "__main__":
    main()
