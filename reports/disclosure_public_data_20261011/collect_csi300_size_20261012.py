"""Collect CSI300 2026-10-09 close and 2026Q2 share counts from anonymous BaoStock; no fitting or retries."""

import csv
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import socket
import sys
import time


HERE = Path(__file__).resolve().parent
POOL_SOURCE = HERE / "csi300_huazheng_latest" / "freeze.json"
OUT = HERE / "csi300_size_20261009_v2"
PRIOR_STOPPED_RUN = HERE / "csi300_size_20261009"
NO_LOGIN = "10001001"
MAX_RELOGINS = 10
PRICE_DATE = "2026-10-09"
PRICE_FIELDS = "date,code,close,preclose,tradestatus,isST,pbMRQ"
PROFIT_YEAR, PROFIT_QUARTER = 2026, 2
WALL_BUDGET_SECONDS = 1800
ANCHORS = {"600887.SH": {"close": 27.66, "totalShare": 6325360667.0}}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def fetch(response, limit):
    rows = []
    while response.error_code == "0" and response.next():
        rows.append(response.get_row_data())
        if len(rows) > limit:
            raise RuntimeError("row budget exceeded")
    return rows


def number(text):
    if text in ("", None):
        return None
    value = float(text)
    if not math.isfinite(value):
        raise ValueError("nonfinite provider value")
    return value


def main():
    runtime = json.loads((HERE / "baostock_reader_runtime.json").read_text(encoding="utf-8"))
    wheel = Path(runtime["runtime_path"])
    assert sha(wheel) == runtime["sha256"]
    pool_sha = sha(POOL_SOURCE)
    pool = json.loads(POOL_SOURCE.read_text(encoding="utf-8"))["pool"]
    assert len(pool) == len({row["ticker"] for row in pool}) == 300
    script_sha = sha(Path(__file__))
    OUT.mkdir(exist_ok=False)
    save(OUT / "freeze.json", {
        "frozen_utc": utc(), "script_sha256": script_sha, "provider_wheel_sha256": runtime["sha256"],
        "pool_source": POOL_SOURCE.relative_to(HERE.parents[1]).as_posix(), "pool_source_sha256": pool_sha,
        "pool": pool, "price_date": PRICE_DATE, "price_fields": PRICE_FIELDS, "adjustflag": "3 (unadjusted)",
        "share_source": f"query_profit_data year={PROFIT_YEAR} quarter={PROFIT_QUARTER} (totalShare, liqaShare, pubDate, statDate)",
        "revision": "v2 of a run stopped by its error rule at 600011.SH when the anonymous session expired "
                    "(BaoStock BSERR_NO_LOGIN 10001001) after 229 queries. v2 re-logs in anonymously on that code only, "
                    "then re-issues the same query once; at most MAX_RELOGINS session renewals. All 300 are re-queried; "
                    "the stopped run is kept unchanged as evidence.",
        "prior_stopped_run_summary_sha256": sha(PRIOR_STOPPED_RUN / "summary.json"),
        "max_session_renewals": MAX_RELOGINS,
        "max_logical_queries": 2 * len(pool), "manual_retries": 0, "wall_budget_seconds": WALL_BUDGET_SECONDS,
        "anonymous_library_login_only": True, "registration_or_personal_credentials": False,
        "stop_conditions": ["login failure", "any query error code", "unexpected row contract", "wall budget"],
        "market_cap_definition": "A-share unadjusted close on 2026-10-09 times 2026-06-30 totalShare (all share classes, "
                                 "the Wind 'total market value 1' convention). Carrying the June share count to October "
                                 "is an assumption; A+H issuers price H shares at the A-share close under this convention.",
        "limitations": ["Vendor data; only anchor companies are checked against exchange/filing values.",
                        "Market cap is a size measure, not latent intrinsic value.",
                        "No open redistribution licence established."],
    })
    socket.setdefaulttimeout(15)
    sys.path.insert(0, str(wheel))
    import baostock as bs
    import baostock.common.context as context

    started = time.monotonic()
    queries, stop_reason, observations = 0, None, []
    renewals = []

    def query(call, *args, **kwargs):
        response = call(*args, **kwargs)
        if response.error_code == NO_LOGIN and len(renewals) < MAX_RELOGINS:
            login = bs.login()
            renewals.append({"utc": utc(), "after_queries": queries, "login_error_code": login.error_code})
            assert login.error_code == "0", "session renewal failed"
            response = call(*args, **kwargs)
        return response

    try:
        login = bs.login()
        if login.error_code != "0":
            stop_reason = "login_failed: " + login.error_msg
        for security in pool:
            ticker = security["ticker"]
            code = ticker[-2:].lower() + "." + ticker[:6]
            observation = {**security, "status": "not_attempted"}
            if stop_reason or time.monotonic() - started > WALL_BUDGET_SECONDS:
                stop_reason = stop_reason or "wall_budget"
                observations.append(observation)
                continue
            try:
                queries += 1
                response = query(bs.query_history_k_data_plus, code, PRICE_FIELDS, start_date=PRICE_DATE, end_date=PRICE_DATE,
                                                        frequency="d", adjustflag="3")
                assert response.error_code == "0", "price query error " + response.error_msg
                prices = fetch(response, 1)
                assert response.fields == PRICE_FIELDS.split(",")
                queries += 1
                response = query(bs.query_profit_data, code=code, year=PROFIT_YEAR, quarter=PROFIT_QUARTER)
                assert response.error_code == "0", "profit query error " + response.error_msg
                profits = fetch(response, 1)
                fields = response.fields
                observation["status"] = "observed"
                if prices:
                    price = dict(zip(PRICE_FIELDS.split(","), prices[0]))
                    assert price["code"] == code and price["date"] == PRICE_DATE
                    observation.update(close=number(price["close"]), preclose=number(price["preclose"]),
                                       tradestatus=price["tradestatus"], is_st=price["isST"], pb_mrq=number(price["pbMRQ"]))
                else:
                    observation["status"] = "missing_price"
                if profits:
                    profit = dict(zip(fields, profits[0]))
                    assert profit["code"] == code and profit["statDate"] == f"{PROFIT_YEAR}-06-30"
                    observation.update(total_share=number(profit["totalShare"]), liqa_share=number(profit["liqaShare"]),
                                       share_pub_date=profit["pubDate"], share_stat_date=profit["statDate"])
                else:
                    observation["status"] = "missing_shares" if prices else "missing_price_and_shares"
                if observation.get("close") and observation.get("total_share"):
                    observation["market_cap_cny"] = observation["close"] * observation["total_share"]
            except (AssertionError, KeyError, ValueError, RuntimeError, OSError) as error:
                observation["status"] = "query_or_contract_error"
                observation["error"] = type(error).__name__ + ": " + str(error)
                stop_reason = "query_or_contract_error " + ticker
            observations.append(observation)
    finally:
        try:
            bs.logout()
        except Exception:
            pass
        if getattr(context, "default_socket", None) is not None:
            context.default_socket.close()
    fields = list(dict.fromkeys(key for row in observations for key in row))
    with (OUT / "observations.csv").open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(observations)
    by_ticker = {row["ticker"]: row for row in observations}
    anchors = {ticker: {key: {"expected": value, "observed": by_ticker[ticker].get({"totalShare": "total_share"}.get(key, key)),
                              "status": "PASS" if by_ticker[ticker].get({"totalShare": "total_share"}.get(key, key)) == value else "FAIL"}
                        for key, value in expected.items()} for ticker, expected in ANCHORS.items()}
    assert len(observations) == 300 and sha(POOL_SOURCE) == pool_sha and sha(Path(__file__)) == script_sha
    summary = {"status": "complete" if stop_reason is None else "stopped", "finished_utc": utc(),
               "wall_seconds": time.monotonic() - started, "logical_queries": queries, "session_renewals": renewals, "stop_reason": stop_reason,
               "status_counts": dict(Counter(row["status"] for row in observations)),
               "not_trading_on_price_date": sorted(r["ticker"] for r in observations if r.get("tradestatus") == "0"),
               "share_published_after_price_date": sorted(r["ticker"] for r in observations
                                                          if r.get("share_pub_date") and r["share_pub_date"] > PRICE_DATE),
               "anchor_checks": anchors,
               "artifact_sha256": {path.name: sha(path) for path in (OUT / "freeze.json", OUT / "observations.csv")}}
    save(OUT / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in summary if key != "artifact_sha256"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
