"""Collect one fixed current CSI300 ESG snapshot; no calibration or retries."""

import base64
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "csi300_huazheng_latest"
POOL = ROOT / "data/processed/disclosure_public_20261011/csi300_constituents_20261009.csv"
POOL_SHA = "329fa084917efb01442cf4a6a0be09bcd91f4b4f0003b571b607e03cc6aaefec"
ENDPOINT = "https://www.chindices.com/esg-carbon/api/esg/total_score?stockCode={}&flag=ESG_A"
MAX_BYTES = 1024 * 1024


def utc():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def main():
    pool_bytes = POOL.read_bytes()
    assert hashlib.sha256(pool_bytes).hexdigest() == POOL_SHA
    rows = list(csv.DictReader(io.StringIO(pool_bytes.decode("utf-8-sig"))))
    exchanges = {"深圳证券交易所": "SZ", "上海证券交易所": "SH"}
    pool = []
    for row in rows:
        assert row["日期Date"] == "20261009" and row["指数代码 Index Code"] == "000300"
        code = row["成份券代码Constituent Code"]
        assert len(code) == 6 and code.isdecimal()
        pool.append({"ticker": code + "." + exchanges[row["交易所Exchange"]],
                     "name": row["成份券名称Constituent Name"]})
    assert len(pool) == len({row["ticker"] for row in pool}) == 300
    evidence_path = HERE / "china_source_availability_20261011.json"
    evidence_bytes = evidence_path.read_bytes()
    records = json.loads(evidence_bytes)["records"]
    cached = {}
    for record in records:
        if "/esg/total_score?" in record["url"]:
            body = record["body"].encode("utf-8")
            assert hashlib.sha256(body).hexdigest() == record["body_sha256"]
            ticker = json.loads(body)["data"]["stockCode"]
            cached[ticker] = record
    assert set(cached) == {"000063.SZ", "600887.SH"}
    assert set(cached).issubset({row["ticker"] for row in pool})
    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.mkdir(exist_ok=False)
    freeze = {
        "frozen_utc": utc(), "pool_file": POOL.relative_to(ROOT).as_posix(),
        "pool_sha256": POOL_SHA, "pool_asof": "2026-10-09", "pool": pool,
        "script_sha256": script_sha,
        "cached_source_file": evidence_path.relative_to(ROOT).as_posix(),
        "cached_source_sha256": hashlib.sha256(evidence_bytes).hexdigest(),
        "cached_observed_records": cached,
        "endpoint": ENDPOINT, "max_new_requests": 298, "max_attempts_per_ticker": 1,
        "delay_between_new_requests_seconds": 1, "request_timeout_seconds": 10,
        "wall_budget_seconds": 900, "max_response_bytes": MAX_BYTES,
        "stop_conditions": ["HTTP 403 or 429", "three consecutive transport/server errors",
                            "response size limit", "unexpected response contract", "wall budget"],
        "no_registration_credentials_retries_or_paid_access": True,
        "purpose": "Current securities-pool observed score snapshot; no model fit or parameter promotion.",
        "limitations": ["Two pilot scores were observed before this pool freeze and are reused explicitly.",
                        "Current constituents are not a historical or survivorship-free population.",
                        "Keep native dates, scales and missing rows; no same-date financial match established.",
                        "A reported ESG score does not identify latent true quality or washing.",
                        "No open redistribution licence established."],
    }
    save(OUT / "freeze.json", freeze)
    started = time.monotonic()
    attempts = 0
    consecutive_errors = 0
    stop_reason = None
    observations = []
    with (OUT / "responses.jsonl").open("x", encoding="utf-8") as archive:
        for number, security in enumerate(pool, 1):
            ticker = security["ticker"]
            observation = {**security, "status": "not_attempted", "score_native": None,
                           "grade": None, "score_date": None, "industry": None}
            if stop_reason:
                observations.append(observation)
                continue
            if time.monotonic() - started > 900:
                stop_reason = "wall_budget"
                observations.append(observation)
                continue
            url = ENDPOINT.format(ticker)
            entry = {"ticker": ticker, "url": url, "requested_utc": utc(), "reused": ticker in cached}
            body = b""
            status = None
            if ticker in cached:
                record = cached[ticker]
                body = record["body"].encode("utf-8")
                status = record["http_status"]
                entry.update({key: record[key] for key in ("requested_utc", "retrieved_utc", "content_type")})
            else:
                if attempts:
                    time.sleep(1)
                attempts += 1
                entry["requested_utc"] = utc()
                request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.chindices.com/esg-data.html"})
                try:
                    with urlopen(request, timeout=10) as response:
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
                entry["retrieved_utc"] = utc()
            entry.update(http_status=status, body_sha256=hashlib.sha256(body).hexdigest(),
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
                            score = float(data["score"])
                            assert math.isfinite(score)
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
    assert len(observations) == 300 and attempts <= 298
    assert hashlib.sha256(POOL.read_bytes()).hexdigest() == POOL_SHA
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == script_sha
    summary = {
        "status": "complete" if stop_reason is None else "stopped",
        "finished_utc": utc(), "wall_seconds": time.monotonic() - started,
        "new_requests": attempts, "securities": len(observations), "stop_reason": stop_reason,
        "status_counts": dict(Counter(row["status"] for row in observations)),
        "score_date_counts": dict(Counter(row["score_date"] for row in observations if row["status"] == "observed")),
        "same_date_joint_calibration_qualified": False,
        "artifact_sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                            for path in (OUT / "freeze.json", OUT / "responses.jsonl", OUT / "observations.csv")},
    }
    save(OUT / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
