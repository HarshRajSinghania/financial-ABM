"""Resume the stopped CSI300 Huazheng snapshot for unobserved securities only; one attempt each."""

import base64
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
PRIOR = HERE / "csi300_huazheng_latest"
OUT = HERE / "csi300_huazheng_resume_20261012"
PRIOR_FILES = ("freeze.json", "summary.json", "responses.jsonl", "observations.csv",
               "audited_observations.csv", "audit.json")
ENDPOINT = "https://www.chindices.com/esg-carbon/api/esg/total_score?stockCode={}&flag=ESG_A"
MAX_BYTES = 1024 * 1024
DELAY_SECONDS = 3
TIMEOUT_SECONDS = 10
WALL_BUDGET_SECONDS = 1200


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def main():
    prior_hashes = {name: sha(PRIOR / name) for name in PRIOR_FILES}
    prior_freeze = json.loads((PRIOR / "freeze.json").read_text(encoding="utf-8"))
    audited = list(csv.DictReader((PRIOR / "audited_observations.csv").open(encoding="utf-8-sig")))
    assert [row["ticker"] for row in audited] == [row["ticker"] for row in prior_freeze["pool"]]
    assert len(audited) == 300
    targets = [{"ticker": row["ticker"], "name": row["name"], "prior_status": row["status"]}
               for row in audited if row["status"] != "observed"]
    assert Counter(row["prior_status"] for row in targets) == Counter({"not_attempted": 175, "request_error": 5})
    script_sha = sha(Path(__file__))
    OUT.mkdir(exist_ok=False)
    freeze = {
        "frozen_utc": utc(), "script_sha256": script_sha,
        "prior_snapshot": PRIOR.name, "prior_file_sha256": prior_hashes,
        "pool_source": "prior freeze pool (official CSI300 file dated 2026-10-09), unchanged order",
        "targets": targets, "scope": "Only the 180 securities without an observed score in audited_observations.csv: "
        "175 never attempted plus 5 prior transport errors. The 5 receive one new attempt in this separately "
        "declared round; prior failures stay recorded unchanged. Observed 120 scores are not re-queried.",
        "endpoint": ENDPOINT, "max_new_requests": len(targets), "max_attempts_per_ticker": 1,
        "delay_between_new_requests_seconds": DELAY_SECONDS, "request_timeout_seconds": TIMEOUT_SECONDS,
        "wall_budget_seconds": WALL_BUDGET_SECONDS, "max_response_bytes": MAX_BYTES,
        "stop_conditions": ["HTTP 403 or 429", "three consecutive transport/server errors",
                            "response size limit", "unexpected response contract", "wall budget"],
        "no_registration_credentials_retries_or_paid_access": True,
        "date_policy": "Keep native date labels. Scores whose label differs from the prior 2026/09/24 snapshot are "
                       "reported separately and must not be silently pooled with it.",
        "limitations": prior_freeze["limitations"],
    }
    save(OUT / "freeze.json", freeze)
    started = time.monotonic()
    attempts = consecutive_errors = 0
    stop_reason = None
    observations = []
    with (OUT / "responses.jsonl").open("x", encoding="utf-8") as archive:
        for number, security in enumerate(targets, 1):
            ticker = security["ticker"]
            observation = {**security, "status": "not_attempted", "score_native": None,
                           "grade": None, "score_date": None, "industry": None}
            if stop_reason or time.monotonic() - started > WALL_BUDGET_SECONDS:
                stop_reason = stop_reason or "wall_budget"
                observations.append(observation)
                continue
            if attempts:
                time.sleep(DELAY_SECONDS)
            attempts += 1
            url = ENDPOINT.format(ticker)
            entry = {"ticker": ticker, "url": url, "requested_utc": utc()}
            body, status = b"", None
            request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.chindices.com/esg-data.html"})
            try:
                with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                    status = response.status
                    entry["final_url"] = response.url
                    entry["content_type"] = response.headers.get("Content-Type")
                    body = response.read(MAX_BYTES + 1)
            except HTTPError as error:
                status = error.code
                body = error.read(MAX_BYTES + 1)
                entry["error"] = str(error)
            except (URLError, OSError, TimeoutError) as error:
                entry["error"] = type(error).__name__ + ": " + str(error)
            entry.update(retrieved_utc=utc(), http_status=status, body_sha256=hashlib.sha256(body).hexdigest(),
                         body_base64=base64.b64encode(body).decode("ascii"), body_bytes=len(body))
            archive.write(json.dumps(entry, ensure_ascii=False) + "\n")
            archive.flush()
            observation["status"] = "request_error"
            if len(body) > MAX_BYTES:
                stop_reason = "response_size_limit"
            elif status in (403, 429):
                stop_reason = "HTTP_" + str(status)
            elif status is None or status >= 500:
                consecutive_errors += 1
                if consecutive_errors >= 3:
                    stop_reason = "three_consecutive_transport_or_server_errors"
            elif status != 200:
                consecutive_errors = 0
                observation["status"] = "http_error"
            else:
                consecutive_errors = 0
                try:
                    payload = json.loads(body)
                    assert payload["code"] == 200
                    data = payload["data"]
                    if data is None or data == {}:
                        observation["status"] = "missing"
                    else:
                        assert data["stockCode"] == ticker
                        if data["score"] is None or data["score"] == "":
                            observation["status"] = "missing"
                        else:
                            assert math.isfinite(float(data["score"]))
                            datetime.strptime(data["date"], "%Y/%m/%d")
                            observation.update(status="observed", score_native=data["score"],
                                               grade=data["totalScore"], score_date=data["date"],
                                               industry=data["industryClass"])
                except (AssertionError, KeyError, TypeError, ValueError, UnicodeDecodeError) as error:
                    observation["status"] = "contract_error"
                    stop_reason = "unexpected_response_contract: " + type(error).__name__
            observations.append(observation)
            if number % 30 == 0 or stop_reason:
                print(json.dumps({"processed": number, "requests": attempts,
                                  "statuses": dict(Counter(row["status"] for row in observations)),
                                  "stop_reason": stop_reason}), flush=True)
    with (OUT / "observations.csv").open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(observations[0]))
        writer.writeheader()
        writer.writerows(observations)
    assert len(observations) == len(targets) and attempts <= len(targets)
    assert {name: sha(PRIOR / name) for name in PRIOR_FILES} == prior_hashes
    assert sha(Path(__file__)) == script_sha
    summary = {
        "status": "complete" if stop_reason is None else "stopped",
        "finished_utc": utc(), "wall_seconds": time.monotonic() - started,
        "new_requests": attempts, "targets": len(targets), "stop_reason": stop_reason,
        "status_counts": dict(Counter(row["status"] for row in observations)),
        "score_date_counts": dict(Counter(row["score_date"] for row in observations if row["status"] == "observed")),
        "same_date_joint_calibration_qualified": False,
        "artifact_sha256": {path.name: sha(path) for path in
                            (OUT / "freeze.json", OUT / "responses.jsonl", OUT / "observations.csv")},
    }
    save(OUT / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
