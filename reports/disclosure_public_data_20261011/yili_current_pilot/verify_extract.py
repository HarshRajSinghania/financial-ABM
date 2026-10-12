"""Verify the archived Yili financial, score and price crosswalk without queries."""

import csv
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parent


def main():
    destination = HERE / "matched_observations.json"
    if destination.exists():
        raise FileExistsError(destination)
    inputs = {}
    texts = {}
    for receipt_name in ("source.json", "share_source_cninfo.json"):
        receipt_path = HERE / receipt_name
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        pdf = ROOT / receipt["file"]
        assert receipt["status"] == "downloaded"
        assert len(pdf.read_bytes()) == receipt["bytes"]
        assert hashlib.sha256(pdf.read_bytes()).hexdigest() == receipt["sha256"]
        inputs[pdf.relative_to(ROOT).as_posix()] = receipt["sha256"]
        inputs[receipt_path.relative_to(ROOT).as_posix()] = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        text = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"],
                              check=True, capture_output=True).stdout.decode("utf-8")
        texts[receipt_name] = text.split("\f")
    pages, repurchase = texts["source.json"], texts["share_source_cninfo.json"]
    assert "合并资产负债表" in pages[47] and "2026 年 6 月 30 日" in pages[47]
    assert "单位：元 币种：人民币" in pages[47]
    assert re.search(r"A股\s+上海证券交易所\s+伊利股份\s+600887", pages[5])
    assert "未经审计" in "".join(pages[:3])
    amounts = {}
    locations = {}
    for key, page, label in (
        ("total_assets_cny", 48, "资产总计"),
        ("total_liabilities_cny", 49, "负债合计"),
        ("parent_equity_cny", 49, "归属于母公司所有者权益（或股东权益）合计"),
        ("noncontrolling_interests_cny", 49, "少数股东权益"),
        ("total_equity_cny", 49, "所有者权益（或股东权益）合计"),
    ):
        match = re.search(r"^\s*" + re.escape(label) + r"\s+([\d,]+\.\d{2})\s+([\d,]+\.\d{2})\s*$",
                          pages[page - 1], re.M)
        assert match is not None, key
        amounts[key] = Decimal(match.group(1).replace(",", ""))
        locations[key] = {"pdf_page": page, "printed_page": page - 3, "label": label}
    assert amounts["total_assets_cny"] == amounts["total_liabilities_cny"] + amounts["total_equity_cny"]
    assert amounts["parent_equity_cny"] + amounts["noncontrolling_interests_cny"] == amounts["total_equity_cny"]
    shares_match = re.search(r"40,540,038 股，总股本变为\s*([\d,]+) 股", pages[65])
    assert shares_match is not None
    shares = int(shares_match.group(1).replace(",", ""))
    assert shares == 6325360667
    assert "报告期内，公司股份总数及股本结构未发生变化" in pages[41]
    assert pages[158].count("6,325,360,667.00") == 2
    assert re.search(r"56、库存股\s+□适用\s+√不适用", pages[158])
    assert re.search(r"累计已回购股数\s+0\s*万股", repurchase[0])
    assert re.search(r"截至\s*2026\s*年\s*9\s*月\s*30\s*日，公司尚未实施股份回购", repurchase[1])

    availability_path = PUBLIC / "china_source_availability_20261011.json"
    availability = json.loads(availability_path.read_text(encoding="utf-8"))
    quote_record = availability["sse_snapshot_evidence"]
    assert hashlib.sha256(quote_record["body"].encode()).hexdigest() == quote_record["body_sha256"]
    quote = json.loads(quote_record["body"].split("(", 1)[1][:-1])
    assert quote["code"] == "600887" and quote["date"] == 20261009
    score_record = next(row for row in availability["records"] if "total_score?stockCode=600887.SH" in row["url"])
    assert hashlib.sha256(score_record["body"].encode()).hexdigest() == score_record["body_sha256"]
    score = json.loads(score_record["body"])["data"]
    assert score["stockCode"] == "600887.SH"
    csv_path = PUBLIC / "baostock_yili_pilot/yili_adjustflag_3.csv"
    csv_receipt_path = PUBLIC / "baostock_yili_pilot/receipt.json"
    csv_receipt = json.loads(csv_receipt_path.read_text(encoding="utf-8"))
    assert hashlib.sha256(csv_path.read_bytes()).hexdigest() == csv_receipt["queries"][0]["sha256"]
    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        last = list(csv.DictReader(handle))[-1]
    price = Decimal(last["close"])
    assert last["date"] == "2026-10-09" and last["code"] == "sh.600887"
    assert price == Decimal(str(quote["snap"][1]))
    conditional_cap = price * shares
    conditional_pb = conditional_cap / amounts["parent_equity_cny"]
    for path in (availability_path, csv_path, csv_receipt_path, Path(__file__)):
        inputs[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(), "status": "PASS",
        "scope": "Extraction and arithmetic only; no fitted distribution or market run.", "new_data_queries": 0,
        "issuer": {"legal_name": "内蒙古伊利实业集团股份有限公司", "security": "600887.SH",
                   "share_class": "A", "currency": "CNY", "identity_pdf_page": 6},
        "financial": {"fiscal_date": "2026-06-30", "publication_date": "2026-08-27", "audited": False,
                      "scope": "consolidated group", "unit": "CNY yuan", "locations": locations,
                      **{key: str(value) for key, value in amounts.items()},
                      "other_equity_instruments_reported": False, "treasury_stock_reported_at_fiscal_date": False},
        "shares": {"registered_shares": shares, "observed_as_of": "2026-06-30",
                   "publication_date": "2026-08-27", "count_pdf_pages": [42, 66, 159],
                   "later_repurchase_observation": {"as_of": "2026-09-30", "publication_date": "2026-10-10",
                                                     "new_program_repurchase_shares": 0, "pdf_pages": [1, 2]},
                   "all_share_changes_through_price_date_verified": False,
                   "treasury_shares_at_price_date": None},
        "score": {"provider": "Huazheng", "observed_date_label": score["date"], "raw_score": score["score"],
                  "rating": score["totalScore"], "retrieved_utc": score_record["retrieved_utc"],
                  "first_publication_time_verified": False, "source_url": score_record["url"]},
        "price": {"date": last["date"], "close_cny_per_share": str(price),
                  "sse_and_baostock_last_close_equal": True, "sse_source_url": quote_record["source_page"]},
        "conditional_derived_values": {
            "assumption": "Carry forward the June registered share count through the October price date; not an independently verified current count.",
            "registered_total_cap_cny": str(conditional_cap),
            "lagged_parent_book_to_market": str(amounts["parent_equity_cny"] / conditional_cap),
            "lagged_parent_price_to_book": str(conditional_pb), "provider_pbMRQ": last["pbMRQ"],
            "absolute_pb_difference": str(abs(conditional_pb - Decimal(last["pbMRQ"]))),
            "pb_agreement_proves_share_count": False,
        },
        "strict_point_in_time_joint_match_qualified": False,
        "empirical_calibration_qualified": False,
        "limitations": [
            "Book equity is an observed accounting proxy, not intrinsic value; the June value is lagged at the October price date.",
            "The October 10 announcement is later than the price date and describes September 30; it cannot establish an October 9 point-in-time information set.",
            "Score first-publication time and all intervening share events have not been verified. No current float or treasury-share-adjusted capitalization is claimed.",
            "One issuer cannot identify a cross-sectional lognormal shape, joint correlation or population representativeness.",
            "Provider PB agreement is a consistency check and may reuse the same financial sources; it is not independent share-count evidence.",
        ],
        "input_sha256": inputs,
    }
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "registered_shares_asof_20260630": shares,
                      "conditional_market_cap_cny": str(conditional_cap), "joint_match_qualified": False}))


if __name__ == "__main__":
    main()
