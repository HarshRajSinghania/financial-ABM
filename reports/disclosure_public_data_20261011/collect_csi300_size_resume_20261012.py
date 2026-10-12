"""Resume the stopped CSI300 size v2 run for its unobserved securities only; v2 rows are kept unchanged."""

import csv
from collections import Counter
import hashlib
import json
from pathlib import Path
import socket
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import collect_csi300_size_20261012 as base  # noqa: E402

PRIOR = HERE / "csi300_size_20261009_v2"
OUT = HERE / "csi300_size_20261009_v2_resume"
TRANSIENT_CODES = {"10001001"} | {f"1000200{i}" for i in range(1, 9)}
MAX_RENEWALS = 10


def main():
    runtime = json.loads((HERE / "baostock_reader_runtime.json").read_text(encoding="utf-8"))
    wheel = Path(runtime["runtime_path"])
    assert base.sha(wheel) == runtime["sha256"]
    prior_hashes = {name: base.sha(PRIOR / name) for name in ("freeze.json", "observations.csv", "summary.json")}
    prior_rows = list(csv.DictReader((PRIOR / "observations.csv").open(encoding="utf-8-sig", newline="")))
    assert len(prior_rows) == 300
    targets = [{"ticker": row["ticker"], "name": row["name"], "prior_status": row["status"]}
               for row in prior_rows if row["status"] != "observed"]
    script_sha = base.sha(Path(__file__))
    OUT.mkdir(exist_ok=False)
    base.save(OUT / "freeze.json", {
        "frozen_utc": base.utc(), "script_sha256": script_sha, "base_module_sha256": base.sha(Path(base.__file__)),
        "provider_wheel_sha256": runtime["sha256"], "prior_run": PRIOR.name, "prior_file_sha256": prior_hashes,
        "targets": targets,
        "scope": "Only securities not observed in v2 (stopped at 601229.SH by BaoStock 10002007 network receive "
                 "error). v2 observed rows are reused unchanged. Same price date, fields and share source as v2.",
        "transient_rule": "On session/network codes 10001001 or 10002001-10002008, renew the anonymous session and "
                          "re-issue the same query once; at most MAX_RENEWALS renewals in total. Any other error stops.",
        "max_session_renewals": MAX_RENEWALS, "max_logical_queries": 4 * len(targets),
        "wall_budget_seconds": base.WALL_BUDGET_SECONDS,
    })
    socket.setdefaulttimeout(15)
    sys.path.insert(0, str(wheel))
    import baostock as bs
    import baostock.common.context as context

    started = time.monotonic()
    queries, renewals, stop_reason, observations = 0, [], None, []

    def query(call, *args, **kwargs):
        nonlocal queries
        queries += 1
        response = call(*args, **kwargs)
        if response.error_code in TRANSIENT_CODES and len(renewals) < MAX_RENEWALS:
            login = bs.login()
            renewals.append({"utc": base.utc(), "after_queries": queries, "trigger_code": response.error_code,
                             "login_error_code": login.error_code})
            assert login.error_code == "0", "session renewal failed"
            queries += 1
            response = call(*args, **kwargs)
        return response

    try:
        login = bs.login()
        if login.error_code != "0":
            stop_reason = "login_failed: " + login.error_msg
        for security in targets:
            ticker = security["ticker"]
            code = ticker[-2:].lower() + "." + ticker[:6]
            observation = {**security, "status": "not_attempted"}
            if stop_reason or time.monotonic() - started > base.WALL_BUDGET_SECONDS:
                stop_reason = stop_reason or "wall_budget"
                observations.append(observation)
                continue
            try:
                response = query(bs.query_history_k_data_plus, code, base.PRICE_FIELDS, start_date=base.PRICE_DATE,
                                 end_date=base.PRICE_DATE, frequency="d", adjustflag="3")
                assert response.error_code == "0", "price query error " + response.error_code
                prices = base.fetch(response, 1)
                assert response.fields == base.PRICE_FIELDS.split(",")
                response = query(bs.query_profit_data, code=code, year=base.PROFIT_YEAR, quarter=base.PROFIT_QUARTER)
                assert response.error_code == "0", "profit query error " + response.error_code
                profits = base.fetch(response, 1)
                fields = response.fields
                observation["status"] = "observed"
                if prices:
                    price = dict(zip(base.PRICE_FIELDS.split(","), prices[0]))
                    assert price["code"] == code and price["date"] == base.PRICE_DATE
                    observation.update(close=base.number(price["close"]), preclose=base.number(price["preclose"]),
                                       tradestatus=price["tradestatus"], is_st=price["isST"],
                                       pb_mrq=base.number(price["pbMRQ"]))
                else:
                    observation["status"] = "missing_price"
                if profits:
                    profit = dict(zip(fields, profits[0]))
                    assert profit["code"] == code and profit["statDate"] == f"{base.PROFIT_YEAR}-06-30"
                    observation.update(total_share=base.number(profit["totalShare"]),
                                       liqa_share=base.number(profit["liqaShare"]),
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
    resumed = {row["ticker"]: row for row in observations}
    merged = [{**{key: value for key, value in resumed[row["ticker"]].items() if key != "prior_status"},
               "round": "v2_resume"} if row["ticker"] in resumed else {**row, "round": "v2"} for row in prior_rows]
    merged_fields = list(dict.fromkeys(key for row in merged for key in row))
    with (OUT / "merged_observations.csv").open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=merged_fields)
        writer.writeheader()
        writer.writerows(merged)
    assert {name: base.sha(PRIOR / name) for name in prior_hashes} == prior_hashes
    assert base.sha(Path(__file__)) == script_sha
    summary = {"status": "complete" if stop_reason is None else "stopped", "finished_utc": base.utc(),
               "wall_seconds": time.monotonic() - started, "logical_queries": queries, "session_renewals": renewals,
               "stop_reason": stop_reason, "targets": len(targets),
               "status_counts": dict(Counter(row["status"] for row in observations)),
               "merged_status_counts": dict(Counter(row["status"] for row in merged)),
               "not_trading_on_price_date": sorted(r["ticker"] for r in merged if r.get("tradestatus") == "0"),
               "artifact_sha256": {path.name: base.sha(path) for path in
                                   (OUT / "freeze.json", OUT / "observations.csv", OUT / "merged_observations.csv")}}
    base.save(OUT / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in summary if key != "artifact_sha256"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
