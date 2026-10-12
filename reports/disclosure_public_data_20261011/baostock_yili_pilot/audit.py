"""Audit the two archived price series and describe returns; no data requests or fit."""

import csv
import hashlib
import json
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

import numpy as np

from abm.msm import MOMENT_NAMES, compute_moments


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    destination = HERE / "audit.json"
    output = HERE / "derived_returns.csv"
    if destination.exists() or output.exists():
        raise FileExistsError("audit outputs already exist")
    receipt_path = HERE / "receipt.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt["status"] == "complete" and len(receipt["queries"]) == 2
    series, inputs = {}, {}
    for query in receipt["queries"]:
        path = HERE / query["file"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == query["sha256"]
        inputs[path.relative_to(ROOT).as_posix()] = digest
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            assert reader.fieldnames == query["fields"]
            rows = list(reader)
        assert len(rows) == query["rows"] == 1638
        assert all(None not in row and all(value is not None and value.strip() for value in row.values()) for row in rows)
        days = [date.fromisoformat(row["date"]) for row in rows]
        assert len(set(days)) == len(days) and days == sorted(days)
        assert days[0].isoformat() == "2020-01-02" and days[-1].isoformat() == "2026-10-09"
        assert all(row["code"] == "sh.600887" and row["adjustflag"] == query["adjustflag"] and row["tradestatus"] == "1" for row in rows)
        numeric = np.array([[float(row[key]) for key in ("close", "preclose", "volume", "amount", "pctChg", "pbMRQ")] for row in rows])
        assert np.isfinite(numeric).all() and (numeric[:, :4] > 0).all()
        assert all(Decimal(row["volume"]) == int(row["volume"]) for row in rows)
        series[query["adjustflag"]] = rows
    raw, adjusted = series["3"], series["2"]
    invariant_fields = ("date", "code", "volume", "amount", "tradestatus", "pctChg", "pbMRQ")
    assert all(all(a[key] == b[key] for key in invariant_fields) for a, b in zip(raw, adjusted, strict=True))
    close = np.array([float(row["close"]) for row in raw])
    reference = np.array([float(row["preclose"]) for row in raw])
    adjusted_close = np.array([float(row["close"]) for row in adjusted])
    adjusted_reference = np.array([float(row["preclose"]) for row in adjusted])
    reported_pct = np.array([float(row["pctChg"]) / 100 for row in raw])
    raw_returns = close[1:] / close[:-1] - 1
    adjusted_returns = adjusted_close[1:] / adjusted_close[:-1] - 1
    reference_returns = close / reference - 1
    events = np.flatnonzero(reference[1:] != close[:-1]) + 1
    availability_path = HERE.parent / "china_source_availability_20261011.json"
    availability = json.loads(availability_path.read_text(encoding="utf-8"))["sse_snapshot_evidence"]
    assert hashlib.sha256(availability["body"].encode()).hexdigest() == availability["body_sha256"]
    quote = json.loads(availability["body"].split("(", 1)[1][:-1])
    assert quote["code"] == "600887" and quote["date"] == 20261009
    assert Decimal(raw[-1]["close"]) == Decimal(str(quote["snap"][1]))
    assert int(raw[-1]["volume"]) == quote["snap"][5]
    amount_difference = Decimal(raw[-1]["amount"]) - Decimal(str(quote["snap"][4]))
    with output.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "code", "unadjusted_simple_return", "provider_adjusted_simple_return",
                         "provider_adjusted_log_return", "exchange_reference_simple_return", "reference_differs_from_previous_close"])
        for i in range(1, len(raw)):
            writer.writerow([raw[i]["date"], raw[i]["code"], raw_returns[i - 1], adjusted_returns[i - 1],
                             np.log1p(adjusted_returns[i - 1]), reference_returns[i], reference[i] != close[i - 1]])
    for path in (receipt_path, availability_path, Path(__file__), output, ROOT / "src/abm/msm.py", ROOT / "src/abm/french49.py"):
        inputs[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    report = {
        "status": "PASS", "scope": "Archived identity, schema and last-quote checks; descriptive return calculations, not market acceptance.",
        "generated_utc": datetime.now(timezone.utc).isoformat(), "new_network_queries": 0,
        "rows_each": len(raw), "paired_returns": len(raw_returns), "missing_cells": 0, "duplicate_dates": 0,
        "all_rows_normal_trading": True, "dates_matched_between_adjustments": True,
        "complete_exchange_calendar_verified": False,
        "first_date": raw[0]["date"], "last_date": raw[-1]["date"],
        "last_quote_crosscheck": {"price_equal": True, "volume_equal": True,
                                  "baostock_minus_sse_amount_cny": str(amount_difference),
                                  "sse_amount_is_integer_cny": True},
        "return_definitions": {
            "unadjusted": "close_t / actual_close_(t-1) - 1; includes corporate-action price changes",
            "provider_adjusted": "forward_adjusted_close_t / forward_adjusted_close_(t-1) - 1",
            "exchange_reference": "unadjusted_close_t / provider_preclose_t - 1; preclose may be an ex-action reference",
            "provider_method": "BaoStock price-change adjustment; its reinvestment convention need not equal a cash-dividend holder return.",
            "documentation_url": "https://www.baostock.com/mainContent?file=stockKData.md",
            "formal_ABM_return_mapping_qualified": False,
        },
        "descriptive_discrepancies": {
            "max_abs_reference_vs_reported_pct_fraction": float(np.max(np.abs(reference_returns - reported_pct))),
            "max_abs_adjusted_vs_reported_pct_fraction": float(np.max(np.abs(adjusted_returns - reported_pct[1:]))),
            "max_abs_adjusted_vs_reference_fraction": float(np.max(np.abs(adjusted_returns - reference_returns[1:]))),
            "max_abs_adjusted_preclose_vs_previous_close_cny": float(np.max(np.abs(adjusted_reference[1:] - adjusted_close[:-1]))),
            "max_abs_raw_vs_adjusted_return_fraction": float(np.max(np.abs(raw_returns - adjusted_returns))),
            "interpretation": "Measured discrepancies are retained; no post-hoc numeric acceptance tolerance or corporate-action type inference is imposed.",
        },
        "reference_change_days": [{"date": raw[i]["date"], "previous_close": raw[i - 1]["close"],
                                   "reference_preclose": raw[i]["preclose"], "independent_action_announcement_verified": False}
                                  for i in events],
        "descriptive_moments": {name: dict(zip(MOMENT_NAMES, compute_moments(values).tolist(), strict=True))
                                for name, values in (("unadjusted_simple", raw_returns), ("provider_adjusted_simple", adjusted_returns))},
        "empirical_target_fitted": False,
        "limitations": [
            "One current constituent is not a representative stock pool; no population uncertainty, cross-asset correlation or model fit is established.",
            "No official exchange calendar or full independent history was acquired; absence of duplicate/blank rows does not prove no missing trading days.",
            "Latest adjusted history may incorporate later corporate-action revisions and is not a frozen historical point-in-time vintage.",
            "Eight reference-price changes are flagged from prices; their dividend, split or rights event types were not independently verified.",
            "Adjusted returns must not receive another cash-dividend term by default. Raw price, provider adjustment and ABM holder-total returns remain distinct.",
        ],
        "input_and_output_sha256": inputs,
    }
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "rows_each": len(raw), "returns": len(raw_returns),
                      "reference_change_days": len(events), "empirical_target_fitted": False}))


if __name__ == "__main__":
    main()
