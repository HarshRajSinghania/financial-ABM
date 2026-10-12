"""Resume book v2 for its transport-error securities only (one pass over company types); v2 rows kept unchanged."""

import base64
from collections import Counter
import csv
from datetime import date
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import collect_csi300_book_20261012 as base  # noqa: E402

PRIOR = HERE / "csi300_book_20260630_v2"
OUT = HERE / "csi300_book_20260630_v2_resume"


def main():
    prior_hashes = {name: base.sha(PRIOR / name) for name in ("freeze.json", "responses.jsonl", "observations.csv", "summary.json")}
    prior_rows = list(csv.DictReader((PRIOR / "observations.csv").open(encoding="utf-8-sig", newline="")))
    assert len(prior_rows) == 300
    targets = [row for row in prior_rows if row["status"] == "request_error"]
    script_sha = base.sha(Path(__file__))
    OUT.mkdir(exist_ok=False)
    base.save(OUT / "freeze.json", {
        "frozen_utc": base.utc(), "script_sha256": script_sha, "base_module_sha256": base.sha(Path(base.__file__)),
        "prior_run": PRIOR.name, "prior_file_sha256": prior_hashes,
        "targets": [{"ticker": row["ticker"], "name": row["name"], "prior_status": row["status"]} for row in targets],
        "scope": "Only v2 rows with a transport error (read timeout). One new pass over company types 4,3,2,1 with "
                 "the same endpoint, report date, parsing and gzip handling as v2; no further retry.",
    })
    observations, responses = [], []
    for number, row in enumerate(targets):
        ticker = row["ticker"]
        observation = {"ticker": ticker, "name": row["name"], "status": "not_attempted", "company_type": None}
        for company_type in base.COMPANY_TYPES:
            if responses:
                time.sleep(base.DELAY_SECONDS)
            url = base.ENDPOINT.format(company_type, base.REPORT_DATE, ticker[-2:] + ticker[:6])
            entry = {"ticker": ticker, "company_type": company_type, "url": url, "requested_utc": base.utc()}
            body, status = b"", None
            try:
                with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=base.TIMEOUT_SECONDS) as response:
                    status, body = response.status, response.read(base.MAX_BYTES + 1)
            except HTTPError as error:
                status, body, entry["error"] = error.code, error.read(base.MAX_BYTES + 1), str(error)
            except (URLError, OSError, TimeoutError) as error:
                entry["error"] = type(error).__name__ + ": " + str(error)
            entry.update(retrieved_utc=base.utc(), http_status=status, body_sha256=hashlib.sha256(body).hexdigest(),
                         body_base64=base64.b64encode(body).decode("ascii"), body_bytes=len(body))
            responses.append(entry)
            if status != 200 or len(body) > base.MAX_BYTES:
                observation["status"] = "request_error" if status is None else "http_error"
                break
            decoded = body[:2] == bytes((0x1F, 0x8B))
            payload = json.loads(gzip.decompress(body) if decoded else body)
            rows = payload.get("data")
            if not rows:
                observation["status"] = "no_template_match"
                continue
            assert len(rows) == 1
            data = rows[0]
            assert data["SECUCODE"] == ticker and data["REPORT_DATE"][:10] == base.REPORT_DATE
            notice = date.fromisoformat(data["NOTICE_DATE"][:10])
            update = date.fromisoformat(data["UPDATE_DATE"][:10]) if data.get("UPDATE_DATE") else None
            amounts = {name.lower(): base.amount(data, name) for name in base.AMOUNT_FIELDS}
            parent = amounts["total_parent_equity"]
            cutoff = date.fromisoformat(base.PUBLICATION_CUTOFF)
            observation.update(
                status="observed", company_type=company_type, report_date=base.REPORT_DATE,
                notice_date=notice.isoformat(), update_date=update.isoformat() if update else None,
                currency=data["CURRENCY"], **amounts,
                common_book_equity=None if parent is None else parent - (amounts["other_equity_tool"] or 0.0),
                published_by_cutoff=notice <= cutoff, updated_after_cutoff=bool(update and update > cutoff),
                body_sha256=entry["body_sha256"], body_gzip_decoded=decoded)
            break
        observations.append(observation)
    with (OUT / "responses.jsonl").open("x", encoding="utf-8") as handle:
        handle.writelines(json.dumps(entry, ensure_ascii=False) + "\n" for entry in responses)
    resumed = {row["ticker"]: row for row in observations}
    merged = [{**resumed[row["ticker"]], "round": "v2_resume"} if row["ticker"] in resumed else {**row, "round": "v2"}
              for row in prior_rows]
    fields = list(dict.fromkeys(key for row in merged for key in row))
    with (OUT / "merged_observations.csv").open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(merged)
    assert {name: base.sha(PRIOR / name) for name in prior_hashes} == prior_hashes and base.sha(Path(__file__)) == script_sha
    summary = {"finished_utc": base.utc(), "requests": len(responses), "targets": len(targets),
               "status_counts": dict(Counter(row["status"] for row in observations)),
               "merged_status_counts": dict(Counter(row["status"] for row in merged)),
               "artifact_sha256": {path.name: base.sha(path) for path in
                                   (OUT / "freeze.json", OUT / "responses.jsonl", OUT / "merged_observations.csv")}}
    base.save(OUT / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
