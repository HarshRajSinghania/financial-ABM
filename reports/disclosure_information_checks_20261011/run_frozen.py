"""Run the declared information controls from an isolated source snapshot."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parents[2]
    package_parent = root / "src"
    sources = {path.relative_to(package_parent).as_posix(): path.read_bytes()
               for path in sorted((package_parent / "abm").rglob("*.py"))}
    expected = {name: hashlib.sha256(content).hexdigest() for name, content in sources.items()}
    output = root / "reports/disclosure_information_development_20261011_v1"
    if output.exists():
        raise FileExistsError(output)
    with tempfile.TemporaryDirectory(prefix="abm-information-source-") as temporary:
        snapshot = Path(temporary).resolve()
        for name, content in sources.items():
            target = snapshot / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        if any(hashlib.sha256((package_parent / name).read_bytes()).hexdigest() != digest
               for name, digest in expected.items()):
            raise RuntimeError("source changed while creating the snapshot")
        sys.path.insert(0, str(snapshot))
        from abm.disclosure.runner import source_hashes
        from abm.disclosure.experiments import run_experiment
        assert source_hashes() == expected
        report = run_experiment(root / "configs/disclosure_information_development_v1.json", output, workers=2)
        frozen = json.loads((output / "experiment.json").read_text(encoding="utf-8"))
        assert frozen["source_hashes"] == expected
        print(report)


if __name__ == "__main__":
    main()
