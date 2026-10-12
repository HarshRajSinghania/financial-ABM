"""Collect one fixed CSI300 half-year book-equity snapshot from Eastmoney F10; no fitting or retries."""

import base64
import gzip
from collections import Counter
import csv
from datetime import date, datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
POOL_SOURCE = HERE / "csi300_huazheng_latest" / "freeze.json"
OUT = HERE / "csi300_book_20260630_v2"
PRIOR_STOPPED_RUN = HERE / "csi300_book_20260630"
ENDPOINT = ("https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/zcfzbAjaxNew"
            "?companyType={}&reportDateType=0&reportType=1&dates={}&code={}")
REPORT_DATE = "2026-06-30"
PUBLICATION_CUTOFF = "2026-10-09"
COMPANY_TYPES = (4, 3, 2, 1)
MAX_BYTES = 2 * 1024 * 1024
DELAY_SECONDS = 2
TIMEOUT_SECONDS = 15
WALL_BUDGET_SECONDS = 2400
AMOUNT_FIELDS = ("TOTAL_PARENT_EQUITY", "OTHER_EQUITY_TOOL", "PREFERRED_SHARES", "PERPETUAL_BOND",
                 "MINORITY_EQUITY", "TOTAL_EQUITY", "SHARE_CAPITAL", "TREASURY_SHARES")
ANCHORS = {"600887.SH": 53711364981.99}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def amount(row, name):
    value = row.get(name)
    if value is None:
        return None
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(name + " is not finite")
    return value


def main():
    pool_sha = sha(POOL_SOURCE)
    pool = json.loads(POOL_SOURCE.read_text(encoding="utf-8"))["pool"]
    assert len(pool) == len({row["ticker"] for row in pool}) == 300
    script_sha = sha(Path(__file__))
    OUT.mkdir(exist_ok=False)
    save(OUT / "freeze.json", {
        "frozen_utc": utc(), "script_sha256": script_sha,
        "pool_source": POOL_SOURCE.relative_to(HERE.parents[1]).as_posix(), "pool_source_sha256": pool_sha,
        "pool_asof": "2026-10-09", "pool": pool, "endpoint": ENDPOINT,
        "report_date": REPORT_DATE, "publication_cutoff": PUBLICATION_CUTOFF,
        "company_type_order": COMPANY_TYPES,
        "company_type_rule": "Query types in order; a response without a data list means the statement template does "
                             "not apply and the next type is queried. These are distinct queries, not retries.",
        "max_new_requests": len(pool) * len(COMPANY_TYPES), "delay_between_requests_seconds": DELAY_SECONDS,
        "request_timeout_seconds": TIMEOUT_SECONDS, "wall_budget_seconds": WALL_BUDGET_SECONDS,
        "max_response_bytes": MAX_BYTES,
        "stop_conditions": ["HTTP 403 or 429", "three consecutive transport/server errors", "response size limit",
                            "unexpected response contract", "wall budget"],
        "revision": "v2 of a run stopped by its contract rule at 000977.SZ because the server sent an unrequested "
                    "gzip body. v2 adds gzip decoding (archived bytes stay as received) and re-queries all 300; "
                    "the stopped run is kept unchanged as evidence.",
        "prior_stopped_run_summary_sha256": sha(PRIOR_STOPPED_RUN / "summary.json"),
        "derived_field": "common_book_equity = TOTAL_PARENT_EQUITY - OTHER_EQUITY_TOOL (missing tool treated as 0; "
                         "the tool line holds preferred shares and perpetual bonds).",
        "anchor_checks": {"600887.SH TOTAL_PARENT_EQUITY": "53711364981.99 CNY from the PDF-verified 2026 half-year report"},
        "no_registration_credentials_retries_or_paid_access": True,
        "limitations": ["Vendor-transcribed statements; only anchor companies are checked against original filings.",
                        "Book equity is an accounting proxy, not latent intrinsic value.",
                        "Half-year statements are mostly unaudited.",
                        "Current constituents are not a historical or survivorship-free population.",
                        "No open redistribution licence established."],
    })
    started = time.monotonic()
    attempts = consecutive_errors = 0
    stop_reason = None
    observations = []
    with (OUT / "responses.jsonl").open("x", encoding="utf-8") as archive:
        for number, security in enumerate(pool, 1):
            ticker = security["ticker"]
            code = ticker[-2:] + ticker[:6]
            observation = {**security, "status": "not_attempted", "company_type": None}
            for company_type in COMPANY_TYPES:
                if stop_reason or time.monotonic() - started > WALL_BUDGET_SECONDS:
                    stop_reason = stop_reason or "wall_budget"
                    break
                if attempts:
                    time.sleep(DELAY_SECONDS)
                attempts += 1
                url = ENDPOINT.format(company_type, REPORT_DATE, code)
                entry = {"ticker": ticker, "company_type": company_type, "url": url, "requested_utc": utc()}
                body, status = b"", None
                try:
                    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=TIMEOUT_SECONDS) as response:
                        status = response.status
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
                    break
                if status in (403, 429):
                    stop_reason = "HTTP_" + str(status)
                    break
                if status is None or status >= 500:
                    consecutive_errors += 1
                    if consecutive_errors >= 3:
                        stop_reason = "three_consecutive_transport_or_server_errors"
                    break
                consecutive_errors = 0
                if status != 200:
                    observation["status"] = "http_error"
                    break
                try:
                    if body[:2] == bytes((0x1F, 0x8B)):
                        entry_decoded = True
                        body = gzip.decompress(body)
                    else:
                        entry_decoded = False
                    payload = json.loads(body)
                    assert isinstance(payload, dict)
                    rows = payload.get("data")
                    if not rows:
                        observation["status"] = "no_template_match"
                        continue
                    assert len(rows) == 1
                    row = rows[0]
                    assert row["SECUCODE"] == ticker and row["REPORT_DATE"][:10] == REPORT_DATE
                    notice = date.fromisoformat(row["NOTICE_DATE"][:10])
                    update = date.fromisoformat(row["UPDATE_DATE"][:10]) if row.get("UPDATE_DATE") else None
                    amounts = {name.lower(): amount(row, name) for name in AMOUNT_FIELDS}
                    parent = amounts["total_parent_equity"]
                    common = None if parent is None else parent - (amounts["other_equity_tool"] or 0.0)
                    observation.update(
                        status="observed", company_type=company_type, report_date=REPORT_DATE,
                        notice_date=notice.isoformat(), update_date=update.isoformat() if update else None,
                        currency=row["CURRENCY"], **amounts, common_book_equity=common,
                        published_by_cutoff=notice <= date.fromisoformat(PUBLICATION_CUTOFF),
                        updated_after_cutoff=bool(update and update > date.fromisoformat(PUBLICATION_CUTOFF)),
                        body_sha256=entry["body_sha256"], body_gzip_decoded=entry_decoded)
                except (AssertionError, KeyError, TypeError, ValueError, UnicodeDecodeError, OSError, EOFError) as error:
                    observation["status"] = "contract_error"
                    stop_reason = "unexpected_response_contract: " + type(error).__name__ + " " + ticker
                break
            observations.append(observation)
            if number % 30 == 0 or stop_reason:
                print(json.dumps({"processed": number, "requests": attempts,
                                  "statuses": dict(Counter(row["status"] for row in observations)),
                                  "stop_reason": stop_reason}), flush=True)
            if stop_reason and number < len(pool):
                observations += [{**rest, "status": "not_attempted", "company_type": None} for rest in pool[number:]]
                break
    fields = list(dict.fromkeys(key for row in observations for key in row))
    with (OUT / "observations.csv").open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(observations)
    observed = {row["ticker"]: row for row in observations if row["status"] == "observed"}
    anchors = {ticker: {"expected": value, "observed": observed.get(ticker, {}).get("total_parent_equity"),
                        "status": "PASS" if observed.get(ticker, {}).get("total_parent_equity") == value else "FAIL"}
               for ticker, value in ANCHORS.items()}
    assert len(observations) == 300 and sha(POOL_SOURCE) == pool_sha and sha(Path(__file__)) == script_sha
    summary = {
        "status": "complete" if stop_reason is None else "stopped",
        "finished_utc": utc(), "wall_seconds": time.monotonic() - started,
        "new_requests": attempts, "securities": len(observations), "stop_reason": stop_reason,
        "status_counts": dict(Counter(row["status"] for row in observations)),
        "company_type_counts": dict(Counter(row["company_type"] for row in observed.values())),
        "currency_counts": dict(Counter(row["currency"] for row in observed.values())),
        "published_after_cutoff": sorted(t for t, row in observed.items() if not row["published_by_cutoff"]),
        "updated_after_cutoff": sorted(t for t, row in observed.items() if row["updated_after_cutoff"]),
        "nonpositive_common_book": sorted(t for t, row in observed.items()
                                          if row["common_book_equity"] is None or row["common_book_equity"] <= 0),
        "anchor_checks": anchors,
        "artifact_sha256": {path.name: sha(path) for path in
                            (OUT / "freeze.json", OUT / "responses.jsonl", OUT / "observations.csv")},
    }
    save(OUT / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in summary if key != "artifact_sha256"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
