"""Build the static site from checked-in files. No simulation runs here.

  _site/index.html         greenwashing policy sandbox (plan stage G): exported synthetic firms, the
                           browser decision core and stage F results, each traced to a committed file
  _site/stage1/index.html  the archived stage 1 exhibit (historical v13/v14 mechanism reports)
  _site/social-card.png    link preview image (og:image) of both pages, copied from showcase/social/
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = {
    "formal": "stage1_mechanism_acceptance_v13_20260814",
    "holdout": "stage1_structural_holdout_v13_20260814",
    "development": "stage1_structural_dev_v14_20260814",
}
METRICS = (
    "daily_volatility", "absolute_return_acf_1", "excess_kurtosis",
    "mean_absolute_log_price_gap",
)
CONFIG_FIELDS = (
    "population_size", "trading_days", "burn_in_days", "strategy_shares",
    "learning_enabled",
)
# Declared by og:image:width / og:image:height in both page templates; render with showcase/social/render.py.
SOCIAL_CARD_SIZE = (1200, 630)


def read_json(path: Path) -> dict:
    def invalid(value: str) -> None:
        raise ValueError(f"Non-finite JSON number in {path}: {value}")
    result = json.loads(path.read_text(encoding="utf-8"), parse_constant=invalid)
    if not isinstance(result, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return result


def export_report(root: Path, report_id: str, directory: str) -> dict:
    path = root / "reports" / directory / "mechanism_report.json"
    report = read_json(path)
    gate = report["gate"]
    checks = gate["checks"]
    if not checks or any(type(value) is not bool for value in checks.values()):
        raise ValueError(f"Invalid gate checks: {path}")
    passed = sum(checks.values())
    if gate["passed_checks"] != passed or gate["total_checks"] != len(checks):
        raise ValueError(f"Inconsistent gate counts: {path}")
    if type(gate["passed"]) is not bool or gate["passed"] != all(checks.values()):
        raise ValueError(f"Inconsistent gate decision: {path}")
    protocol = report["protocol"]
    seeds = protocol["seeds"]
    if not seeds or len(set(seeds)) != len(seeds) or any(type(s) is not int for s in seeds):
        raise ValueError(f"Invalid seed inventory: {path}")
    config = {key: report["config"][key] for key in CONFIG_FIELDS}
    if not 0 <= config["burn_in_days"] < config["trading_days"]:
        raise ValueError(f"Invalid evaluation window: {path}")
    summary = {}
    for scenario, source_metrics in report["summary"].items():
        summary[scenario] = {}
        for metric in METRICS:
            values = {key: source_metrics[metric][key] for key in ("median", "q10", "q90")}
            if any(type(v) not in (int, float) or not math.isfinite(v) for v in values.values()):
                raise ValueError(f"Invalid {scenario}/{metric} in {path}")
            if not values["q10"] <= values["median"] <= values["q90"]:
                raise ValueError(f"Unordered quantiles in {path}")
            summary[scenario][metric] = values
    if "full" not in summary:
        raise ValueError(f"Missing baseline: {path}")
    evidence = {
        key: {field: value[field] for field in ("observed", "threshold", "pass_rate", "failed_seeds") if field in value}
        for key, value in gate.get("evidence", {}).items()
    }
    # Validate the historical formal verdict; this is NOT a new model gate run.
    if report_id == "formal":
        decision = read_json(path.with_name("final_decision.json"))
        if decision["passed_checks"] != passed or decision["total_checks"] != len(checks):
            raise ValueError("Formal final_decision disagrees with archived report")
        if decision["stage1_complete"] is not False or decision["may_enter_stage2"] is not False:
            raise ValueError("Historical exhibit expects incomplete Stage 1; revise its narrative before publication")
        if passed != 18 or len(checks) != 22:
            raise ValueError("Historical 18/22 snapshot changed; revise the dated exhibition copy")
    return {
        "id": report_id, "path": f"reports/{directory}",
        "protocol": protocol["version"], "stage": protocol.get("stage", "development"),
        "seeds": len(seeds), "config": config,
        "code_revision": report.get("code_revision", "not recorded"),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "checks": checks, "evidence": evidence, "summary": summary,
    }


SANDBOX_FIRM_FIELDS = {"size_class", "market_cap", "cost_scale", "benefit", "initial_goodness", "goodness",
                       "inflation", "pending", "full_model_decision"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_size(path: Path) -> tuple[int, int]:
    """Width and height from the PNG header."""
    with path.open("rb") as handle:
        head = handle.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError(f"Not a PNG file: {path}")
    return struct.unpack(">II", head[16:24])


def sandbox_payload(root: Path, revision: str) -> dict:
    """Sandbox data, checked against the committed files it was exported from."""
    data = root / "showcase" / "data"
    firms = read_json(data / "sandbox_firms.json")
    stage_f = read_json(data / "stage_f.json")
    simplification = read_json(data / "simplification.json")
    source = stage_f["source"]
    analysis_path = root / source["path"]
    if sha256_file(analysis_path) != source["sha256"]:
        raise ValueError(f"stage F numbers no longer match {source['path']}; rerun the export")
    if read_json(analysis_path)["experiment_id"] != source["experiment_id"]:
        raise ValueError("stage F experiment_id disagrees with its analysis file")
    if sha256_file(root / firms["experiment_spec"]) != firms["experiment_spec_sha256"]:
        raise ValueError("sandbox firms were exported from a different stage F specification")
    ai = firms["domains"]["ai_washing"]
    if sha256_file(root / ai["domain_file"]) != ai["domain_file_sha256"]:
        raise ValueError("the AI-washing domain file changed after the export")
    for key, domain in firms["domains"].items():
        columns = domain["firms"]
        # Synthetic firms only: no names or identifiers beyond the model's own firm order.
        if set(columns) != SANDBOX_FIRM_FIELDS:
            raise ValueError(f"unexpected sandbox firm fields in {key}: {sorted(set(columns) ^ SANDBOX_FIRM_FIELDS)}")
        lengths = {len(columns[name]) for name in SANDBOX_FIRM_FIELDS - {"pending", "full_model_decision"}}
        if lengths != {200}:
            raise ValueError(f"{key}: every firm column needs 200 rows")
    return {"schema_version": 1, "source_commit": revision, "firms": firms, "stage_f": stage_f, "simplification": simplification}


def inline(template: str, replacements: dict[str, str]) -> str:
    for marker, value in replacements.items():
        if template.count(marker) != 1:
            raise ValueError(f"Template marker missing or duplicated: {marker}")
        if marker.startswith("/* ") and not marker.endswith("_CSS */") and "</script" in value.lower():
            raise ValueError(f"inline script for {marker} contains a closing script tag")
        template = template.replace(marker, value)
    if re.search(r'<(?:script|link)[^>]+(?:src|href)=["\']https?://', template):
        raise ValueError("Exhibit must not require third-party scripts/styles/fonts")
    return template


def serialize(payload: dict) -> str:
    # Escape raw-text HTML delimiters even if a report string contains markup.
    return json.dumps(payload, ensure_ascii=False, allow_nan=False, separators=(",", ":")).replace("<", "\\u003c")


def build(output: Path, root: Path = ROOT) -> dict:
    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = "master"
    snapshot = {
        "schema_version": "1.0.0", "source_commit": revision,
        "report_date": "2026-08-14", "mode": "archived_read_only",
        "notice": "Historical v13 failed 18/22; frozen v15 passed 22/22 on 2026-09-26. Neither is a rerun of merged source.",
        "reports": [export_report(root, key, directory) for key, directory in REPORTS.items()],
    }
    stage1 = root / "showcase" / "stage1"
    stage1_html = inline((stage1 / "index.html").read_text(encoding="utf-8"), {
        "/* SHOWCASE_CSS */": (stage1 / "styles.css").read_text(encoding="utf-8"),
        "/* SHOWCASE_TEXT */": (stage1 / "i18n.js").read_text(encoding="utf-8"),
        "/* SHOWCASE_JS */": (stage1 / "app.js").read_text(encoding="utf-8"),
        '{"reports":[]}': json.dumps(snapshot, ensure_ascii=False, allow_nan=False).replace("<", "\\u003c"),
    })
    sandbox = root / "showcase" / "sandbox"
    payload = sandbox_payload(root, revision)
    sandbox_html = inline((sandbox / "index.html").read_text(encoding="utf-8"), {
        "/* SANDBOX_CSS */": (sandbox / "styles.css").read_text(encoding="utf-8"),
        "/* SANDBOX_CORE */": (sandbox / "core.js").read_text(encoding="utf-8"),
        "/* SANDBOX_DESK */": (sandbox / "desk.js").read_text(encoding="utf-8"),
        "/* SANDBOX_TEXT */": (sandbox / "i18n.js").read_text(encoding="utf-8"),
        "/* SANDBOX_APP */": (sandbox / "app.js").read_text(encoding="utf-8"),
        '{"sandbox":null}': serialize(payload),
    })
    card = root / "showcase" / "social" / "social-card.png"
    if png_size(card) != SOCIAL_CARD_SIZE:
        raise ValueError(f"{card.name} is {png_size(card)}, but the pages declare {SOCIAL_CARD_SIZE}")
    (output / "stage1").mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(sandbox_html, encoding="utf-8")
    (output / "sandbox-data.json").write_text(json.dumps(payload, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    (output / "stage1" / "index.html").write_text(stage1_html, encoding="utf-8")
    (output / "stage1" / "data.json").write_text(json.dumps(snapshot, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    shutil.copyfile(card, output / card.name)
    (output / ".nojekyll").touch()
    print(f"Built {output / 'index.html'}: {len(sandbox_html.encode()):,} bytes (sandbox); "
          f"{output / 'stage1' / 'index.html'}: {len(stage1_html.encode()):,} bytes; no simulation executed")
    return {"stage1": snapshot, "sandbox": payload}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    build(args.output.resolve())
