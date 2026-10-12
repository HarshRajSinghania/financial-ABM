"""Fixed 15-world engineering smoke; coverage and market failures remain visible."""

from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np

from abm.disclosure import runner
from abm.disclosure.config import MarketConfig
from abm.disclosure.domain import load_domain
from abm.disclosure.learning import load_frozen, table_fingerprint
from abm.disclosure.policy import PolicySchedule
from abm.disclosure.training import train_and_evaluate
from abm.manifest import canonical_json_bytes, sha256_file


SPEC = {
    "name": "common_prepolicy_real_entry_smoke_v1",
    "purpose": "engineering_smoke",
    "regression": {
        "path": "reports/disclosure_learning_protocol_checks_20261011/regression.json",
        "sha256": "a85f4b1c343ef26f439bfc2db7e3cb83596d5d4599201c564345a5b3dc6b005a",
    },
    "market_source": {
        "path": "configs/disclosure_action_grid_development_v1.json",
        "sha256": "a87ec3e4633b7d6c743e3eea3bf6c1079e57efd7fc4f328874c1c7492d72160c",
    },
    "domain": {
        "path": "configs/domains/esg.json",
        "sha256": "1010e0aea9a50d2c62dc43076b996fd6befd35dc75a7fee44f28b66252ac52b5",
    },
    "source_training_seeds": [720101, 720102],
    "source_validation_seeds": [720111],
    "post_training_seeds": [720201, 720202],
    "post_validation_seeds": [720211],
    "coverage_target": 20,
    "policy_start_day": 601,
    "transparency_T": .6,
    "budget": {
        "source_worlds": 5, "post_worlds_per_scenario": 5, "total_worlds": 15,
        "source_completed_td_samples": 1740, "post_new_td_samples_per_scenario": 1140,
        "training_worlds": 6, "validation_worlds": 9, "simulated_trading_days": 27000,
        "company_day_states": 810450,
    },
    "seed_collision_check": {
        "status": "PASS", "matches": 0,
        "scope": "Static exact-integer search of configs/reports JSON, Python and Markdown plus seed archive paths before creating this launcher.",
    },
    "scope": "Real entry and provenance only; not coverage qualification, empirical validity, from-zero online learning or a policy ranking.",
    "automatic_additional_worlds": False,
}
OUTPUT = Path(__file__).resolve().parent / "common_prepolicy_smoke"


def main() -> None:
    for item in (SPEC["regression"], SPEC["market_source"], SPEC["domain"]):
        if sha256_file(ROOT / item["path"]) != item["sha256"]:
            raise ValueError(f"frozen smoke input hash mismatch: {item['path']}")
    regression = json.loads((ROOT / SPEC["regression"]["path"]).read_text(encoding="utf-8"))
    expected_sources = {name.removeprefix("src/"): digest for name, digest in regression["input_sha256"].items()
                        if name.startswith("src/abm/")}
    assert regression["status"] == "PASS" and regression["source_and_tests_unchanged"]
    assert runner.source_hashes() == expected_sources
    base = json.loads((ROOT / SPEC["market_source"]["path"]).read_text(encoding="utf-8"))
    config = MarketConfig.from_dict(base["market"])
    domain = load_domain(ROOT / SPEC["domain"]["path"])
    baseline = PolicySchedule.constant(domain)
    assert (config.n_investors, config.n_firms, config.trading_days, config.burn_in_days) == (150, 30, 1800, 600)
    assert config.firm_action_fractions == (.01, .02, .04, .08, .16, .32, .64, 1.)
    assert config.firm_decision_interval == 60
    source_used = set(SPEC["source_training_seeds"] + SPEC["source_validation_seeds"])
    post_used = set(SPEC["post_training_seeds"] + SPEC["post_validation_seeds"])
    assert not source_used & post_used
    assert not (source_used | post_used) & set(base["reserved_seeds"])
    policies = {"B": baseline.with_intervention(SPEC["policy_start_day"]),
                "T": baseline.with_information_intervention(SPEC["policy_start_day"], transparency=SPEC["transparency_T"])}
    OUTPUT.mkdir(parents=True, exist_ok=False)
    frozen_spec = {**SPEC, "source_hashes": expected_sources, "config": config.to_dict(),
                   "domain_spec": domain.to_dict(), "launcher_sha256": sha256_file(__file__)}
    frozen_spec["experiment_id"] = hashlib.sha256(canonical_json_bytes(frozen_spec)).hexdigest()
    runner.write_json(OUTPUT / "experiment.json", frozen_spec)
    report = {"engineering_status": "running", "purpose": SPEC["purpose"],
              "experiment_id": frozen_spec["experiment_id"], "budget": SPEC["budget"], "stages": {},
              "scientific_deployment_qualified": False, "empirical_status": "pending", "scope": SPEC["scope"]}
    report_path = OUTPUT / "verification.json"
    runner.write_json(report_path, report)
    try:
        source_folder = OUTPUT / "source_baseline"
        source_summary = train_and_evaluate(config, domain, baseline, source_folder,
                                            training_seeds=SPEC["source_training_seeds"],
                                            validation_seeds=SPEC["source_validation_seeds"],
                                            reserved_seeds=base["reserved_seeds"], coverage_target=SPEC["coverage_target"])
        source_path = source_folder / "frozen_model.npz"
        source_hash = source_summary["frozen_model_sha256"]
        source, _ = load_frozen(source_path, expected_sha256=source_hash)
        assert source.counts.sum() == SPEC["budget"]["source_completed_td_samples"]
        assert not source.values[3:].any() and not source.counts[3:].any()
        prefix = table_fingerprint(source, prefix_groups=3)
        report["source_model_sha256"] = source_hash
        summaries = {"source_baseline": source_summary}
        report["stages"]["source_baseline"] = {"status": source_summary["status"], "validation": source_summary["validation"]}
        runner.write_json(report_path, report)
        print(json.dumps({"stage": "source_baseline", "completed_worlds": len(source_summary["records"])}), flush=True)
        for name, policy in policies.items():
            stage = train_and_evaluate(config, domain, policy, OUTPUT / name,
                                       training_seeds=SPEC["post_training_seeds"],
                                       validation_seeds=SPEC["post_validation_seeds"], reserved_seeds=base["reserved_seeds"],
                                       coverage_target=SPEC["coverage_target"], common_prepolicy_model=source_path,
                                       common_prepolicy_sha256=source_hash)
            summaries[name] = stage
            trained, _ = load_frozen(OUTPUT / name / "frozen_model.npz", expected_sha256=stage["frozen_model_sha256"])
            assert table_fingerprint(trained, prefix_groups=3) == prefix
            assert trained.counts[3:].sum() == SPEC["budget"]["post_new_td_samples_per_scenario"]
            initial, _ = load_frozen(OUTPUT / name / "initial_model.npz")
            assert table_fingerprint(initial, prefix_groups=3) == prefix
            assert not initial.values[3:].any() and not initial.counts[3:].any()
            report["stages"][name] = {"status": stage["status"], "validation": stage["validation"],
                                      "new_td_samples": int(trained.counts[3:].sum())}
            runner.write_json(report_path, report)
            print(json.dumps({"stage": name, "completed_worlds": len(stage["records"])}), flush=True)

        checked_runs = []
        for name, stage in summaries.items():
            assert stage["status"] == "complete" and len(stage["records"]) == 5
            for record in stage["records"]:
                folder = OUTPUT / name / record["path"]
                manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
                assert record["status"] == manifest["status"] == "complete"
                assert manifest["source_hashes"] == expected_sources
                for artifact, digest in manifest["artifacts"].items():
                    assert sha256_file(folder / artifact) == digest
                with zipfile.ZipFile(folder / "source.zip") as archive:
                    assert set(archive.namelist()) == set(expected_sources)
                    assert all(hashlib.sha256(archive.read(path)).hexdigest() == digest
                               for path, digest in expected_sources.items())
                result = runner.load_result(folder / "result.npz")
                assert result.fingerprint() == manifest["result_fingerprint"]
                item = {"stage": name, "seed": record["seed"], "rule": record["firm_policy"],
                        "phase": record["phase"], "manifest_sha256": sha256_file(folder / "manifest.json"),
                        "validation": record["validation"]}
                if record["firm_policy"] == "q_learning":
                    before, _ = load_frozen(folder / "input_model.npz")
                    after, _ = load_frozen(folder / "output_model.npz")
                    if record["phase"] == "validation":
                        assert table_fingerprint(before) == table_fingerprint(after)
                        assert result.learning_update is None or not result.learning_update.any()
                    else:
                        expected = 870 if name == "source_baseline" else 570
                        assert int(after.counts.sum() - before.counts.sum()) == expected
                        if name != "source_baseline":
                            update = np.zeros_like(result.learning_transition)
                            update[1:] = result.learning_transition[1:] & (result.learning_groups[:-1] >= 3)
                            np.testing.assert_array_equal(result.learning_update, update)
                            assert int(update.sum()) == expected
                            assert not result.coverage_forced[-1].any()
                            assert not result.coverage_forced[result.learning_groups < 3].any()
                            assert not (result.coverage_forced[:-1] & ~update[1:]).any()
                    if name != "source_baseline":
                        assert table_fingerprint(before, prefix_groups=3) == prefix
                        assert table_fingerprint(after, prefix_groups=3) == prefix
                    item.update({"initial_table_fingerprint": table_fingerprint(before),
                                 "final_table_fingerprint": table_fingerprint(after),
                                 "count_increment": int(after.counts.sum() - before.counts.sum())})
                checked_runs.append(item)

        pairs = []
        left = summaries["B"]["records"]
        right = {(item["phase"], item["seed"], item["firm_policy"]): item for item in summaries["T"]["records"]}
        for item in left:
            key = (item["phase"], item["seed"], item["firm_policy"])
            match = right[key]
            with np.load(OUTPUT / "B" / item["path"] / "result.npz", allow_pickle=False) as first, \
                    np.load(OUTPUT / "T" / match["path"] / "result.npz", allow_pickle=False) as second:
                assert set(first.files) == set(second.files)
                for field in first.files:
                    a, b = first[field], second[field]
                    assert a.dtype == b.dtype and a.shape == b.shape
                    if a.ndim and a.shape[0] == config.trading_days + 1:
                        a, b = a[:SPEC["policy_start_day"]], b[:SPEC["policy_start_day"]]
                    elif a.ndim and a.shape[0] == config.trading_days // config.firm_decision_interval + 1:
                        end = (SPEC["policy_start_day"] - 1) // config.firm_decision_interval + 1
                        a, b = a[:end], b[:end]
                    assert a.tobytes() == b.tobytes(), (key, field)
                pairs.append({"phase": key[0], "seed": key[1], "rule": key[2], "fields": len(first.files),
                              "through_day": 600, "status": "PASS"})
        assert len(checked_runs) == SPEC["budget"]["total_worlds"] and len(pairs) == 5
        assert sha256_file(source_path) == source_hash
        assert runner.source_hashes() == expected_sources
        report.update({"engineering_status": "PASS", "checked_worlds": len(checked_runs),
                       "runs": checked_runs, "prepolicy_pairs": pairs, "source_model_unchanged": True,
                       "source_and_post_coverage_gates": {name: stage["validation"]["coverage"]["status"]
                                                         for name, stage in summaries.items()}})
        runner.write_json(report_path, report)
    except BaseException as error:
        report.update({"engineering_status": "FAIL", "error_type": type(error).__name__, "error": str(error),
                       "automatic_additional_worlds": False, "resumable": False})
        runner.write_json(report_path, report)
        raise
    print(json.dumps({"engineering_status": report["engineering_status"], "worlds": report["checked_worlds"],
                      "coverage": report["source_and_post_coverage_gates"], "verification": str(report_path)}), flush=True)


if __name__ == "__main__":
    main()
