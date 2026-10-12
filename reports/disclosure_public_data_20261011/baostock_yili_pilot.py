"""Bounded anonymous-provider probe for one security; no model fitting."""

import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import socket
import subprocess
import sys


HERE = Path(__file__).resolve().parent
OUT = HERE / "baostock_yili_pilot"
FIELDS = "date,code,close,preclose,volume,amount,adjustflag,tradestatus,pctChg,pbMRQ"


def worker():
    runtime = json.loads((HERE / "baostock_reader_runtime.json").read_text(encoding="utf-8"))
    wheel = Path(runtime["runtime_path"])
    assert hashlib.sha256(wheel.read_bytes()).hexdigest() == runtime["sha256"]
    socket.setdefaulttimeout(15)
    sys.path.insert(0, str(wheel))
    import baostock as bs
    import baostock.common.context as context

    receipt = {"started_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
               "provider_version": bs.__version__, "login": None, "queries": [], "status": "started"}
    try:
        login = bs.login()
        receipt["login"] = {"error_code": login.error_code, "error_msg": login.error_msg}
        if login.error_code != "0":
            receipt["status"] = "login_failed"
            return
        for flag in ("3", "2"):
            response = bs.query_history_k_data_plus("sh.600887", FIELDS, start_date="2020-01-01",
                                                    end_date="2026-10-09", frequency="d", adjustflag=flag)
            entry = {"adjustflag": flag, "error_code": response.error_code, "error_msg": response.error_msg,
                     "fields": response.fields, "rows": 0, "final_error_code": response.error_code}
            receipt["queries"].append(entry)
            if response.error_code != "0":
                receipt["status"] = "query_failed"
                return
            rows = []
            while response.error_code == "0" and response.next():
                rows.append(response.get_row_data())
                if len(rows) > 2000:
                    raise RuntimeError("Unexpected row count exceeds fixed pilot budget")
            entry.update(rows=len(rows), final_error_code=response.error_code)
            assert response.error_code == "0"
            assert response.fields == FIELDS.split(",")
            target = OUT / ("yili_adjustflag_" + flag + ".csv")
            with target.open("x", encoding="utf-8-sig", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(response.fields)
                writer.writerows(rows)
            entry.update(file=target.name, sha256=hashlib.sha256(target.read_bytes()).hexdigest())
            if rows:
                entry.update(first_date=rows[0][0], last_date=rows[-1][0], last_row=rows[-1])
        receipt["status"] = "complete"
    except Exception as error:
        receipt.update(status="failed", error=type(error).__name__ + ": " + str(error))
    finally:
        if getattr(context, "default_socket", None) is not None:
            context.default_socket.close()
        receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (OUT / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(receipt, ensure_ascii=False), flush=True)


def main():
    OUT.mkdir(exist_ok=False)
    freeze = {"security": "sh.600887", "start_date": "2020-01-01", "end_date": "2026-10-09",
              "fields": FIELDS, "adjustflags": ["3", "2"], "max_logical_history_queries": 2,
              "max_rows_per_query": 2000, "wall_timeout_seconds": 75, "socket_timeout_seconds": 15,
              "anonymous_library_login_only": True, "registration_or_personal_credentials": False,
              "provider_endpoint": "public-api.baostock.com:10030", "manual_retries": 0,
              "method_documentation": "https://www.baostock.com/mainContent?file=stockKData.md",
              "score_or_ABM_queries": 0, "purpose": "Single-security public data and return-definition verification, not a fitted model.",
              "reader_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "runtime_metadata_sha256": hashlib.sha256((HERE / "baostock_reader_runtime.json").read_bytes()).hexdigest()}
    (OUT / "freeze.json").write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (OUT / "worker.log").open("x", encoding="utf-8") as log:
        try:
            result = subprocess.run([sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()), "--worker"],
                                    stdout=log, stderr=subprocess.STDOUT, timeout=75, check=False)
            status = {"process_status": "exited", "exit_code": result.returncode}
        except subprocess.TimeoutExpired:
            status = {"process_status": "timeout", "timeout_seconds": 75, "retry": False}
    (OUT / "process.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status), flush=True)
    if (OUT / "receipt.json").exists():
        print((OUT / "receipt.json").read_text(encoding="utf-8"), flush=True)


if __name__ == "__main__":
    worker() if sys.argv[1:] == ["--worker"] else main()
