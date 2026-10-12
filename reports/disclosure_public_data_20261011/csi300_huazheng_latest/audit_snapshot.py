"""Check archived responses and retain a preexisting cached score without requests."""

import base64
from collections import Counter
import csv
from datetime import datetime
import hashlib
import json
from pathlib import Path
import statistics


HERE = Path(__file__).resolve().parent


def main():
    assert not (HERE / "audit.json").exists()
    summary = json.loads((HERE / "summary.json").read_text(encoding="utf-8"))
    for name, digest in summary["artifact_sha256"].items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest
    freeze = json.loads((HERE / "freeze.json").read_text(encoding="utf-8"))
    assert hashlib.sha256((HERE.parent / "collect_csi300_scores.py").read_bytes()).hexdigest() == freeze["script_sha256"]
    responses = [json.loads(line) for line in (HERE / "responses.jsonl").read_text(encoding="utf-8").splitlines()]
    with (HERE / "observations.csv").open(encoding="utf-8-sig", newline="") as handle:
        original = list(csv.DictReader(handle))
    assert len(original) == 300
    assert [(row["ticker"], row["name"]) for row in original] == [(row["ticker"], row["name"]) for row in freeze["pool"]]
    assert len({row["ticker"] for row in responses}) == len(responses)
    assert dict(Counter(row["status"] for row in original)) == summary["status_counts"]
    by_ticker = {}
    new_requests = []
    for response in responses:
        body = base64.b64decode(response["body_base64"], validate=True)
        assert len(body) == response["body_bytes"]
        assert hashlib.sha256(body).hexdigest() == response["body_sha256"]
        assert response["url"] == freeze["endpoint"].format(response["ticker"])
        if response["reused"]:
            cached = freeze["cached_observed_records"][response["ticker"]]
            assert body == cached["body"].encode("utf-8")
        else:
            new_requests.append(response)
        by_ticker[response["ticker"]] = (response, body)
    assert len(new_requests) == summary["new_requests"] <= freeze["max_new_requests"]
    delays = [(datetime.fromisoformat(current["requested_utc"]) - datetime.fromisoformat(previous["retrieved_utc"])).total_seconds()
              for previous, current in zip(new_requests, new_requests[1:])]
    assert min(delays) >= 0.99
    assert summary["stop_reason"] == "three_consecutive_transport_or_server_errors"
    assert all(row["http_status"] is None or row["http_status"] >= 500 for row in new_requests[-3:])
    assert [row["ticker"] for row in responses] == [row["ticker"] for row in original[:len(responses)]]
    audited = []
    supplements = []
    for row in original:
        ticker = row["ticker"]
        source = by_ticker.get(ticker)
        output = {**row, "original_status": row["status"], "evidence_origin": "unavailable"}
        data = None
        if source is not None and source[0]["http_status"] == 200:
            payload = json.loads(source[1])
            assert payload["code"] == 200 and payload["data"]["stockCode"] == ticker
            data = payload["data"]
            assert row["status"] == "observed"
            assert [row[key] for key in ("score_native", "grade", "score_date", "industry")] == [data[key] for key in ("score", "totalScore", "date", "industryClass")]
            output["evidence_origin"] = "prior_cache" if source[0]["reused"] else "new_response"
        elif ticker in freeze["cached_observed_records"]:
            assert row["status"] == "not_attempted" and source is None
            record = freeze["cached_observed_records"][ticker]
            body = record["body"].encode("utf-8")
            assert hashlib.sha256(body).hexdigest() == record["body_sha256"]
            data = json.loads(body)["data"]
            assert data["stockCode"] == ticker
            output.update(status="observed", score_native=data["score"], grade=data["totalScore"],
                          score_date=data["date"], industry=data["industryClass"], evidence_origin="prior_cache_after_stop")
            supplements.append(ticker)
        elif source is not None:
            assert row["status"] == "request_error" and source[0]["http_status"] is None
            output["evidence_origin"] = "failed_request"
        else:
            assert row["status"] == "not_attempted"
        audited.append(output)
    destination = HERE / "audited_observations.csv"
    with destination.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audited[0]))
        writer.writeheader()
        writer.writerows(audited)
    observed = [row for row in audited if row["status"] == "observed"]
    values = [float(row["score_native"]) for row in observed]
    result = {
        "archive_integrity": "PASS", "collection_status": "stopped_partial",
        "network_calls_by_audit": 0, "original_status_counts": summary["status_counts"],
        "audited_status_counts": dict(Counter(row["status"] for row in audited)),
        "cached_supplements_without_network": supplements,
        "new_requests": len(new_requests), "minimum_between_request_delay_seconds": min(delays),
        "error_records": [{key: row.get(key) for key in ("ticker", "error", "http_status")} for row in new_requests if row["http_status"] != 200],
        "pool_exchange_counts": dict(Counter(row["ticker"][-2:] for row in original)),
        "observed_exchange_counts": dict(Counter(row["ticker"][-2:] for row in observed)),
        "score_date_counts": dict(Counter(row["score_date"] for row in observed)),
        "descriptive_only": {"n": len(values), "mean": statistics.fmean(values), "population_sd": statistics.pstdev(values),
                             "min": min(values), "max": max(values), "unique_scores": len(set(values))},
        "complete_pool_calibration_qualified": False, "same_date_joint_calibration_qualified": False,
        "limitations": ["The ordered network stop overrepresents Shenzhen securities; missingness is not assumed random.",
                        "The initial collector stops before consuming a later cached security. This audit adds its already frozen response and preserves the original files.",
                        "Native scores and dates retained; no bounds, measurement model, issuer aggregation or financial fit inferred."],
        "input_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                         for name in ("summary.json", "freeze.json", "responses.jsonl", "observations.csv")},
        "output_csv_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "audit_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    with (HERE / "audit.json").open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
