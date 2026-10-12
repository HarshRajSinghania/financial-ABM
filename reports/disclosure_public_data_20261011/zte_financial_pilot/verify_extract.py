"""Extract one issuer crosswalk from the archived public sources; no fitting."""

import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RAW = ROOT / "data/raw/disclosure_public_20261011"
PROCESSED = ROOT / "data/processed/disclosure_public_20261011"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def main():
    destination = HERE / "matched_observations.json"
    if destination.exists():
        raise FileExistsError(destination)
    pdf = RAW / "zte_annual_report_2023_cninfo.pdf"
    hkex = RAW / "hkex_securities_list_20261011.xlsx"
    huazheng = RAW / "huazheng_zte_latest_20261011.json"
    expected = {
        pdf: "b11c96ff8cca3cd9ce63a309ced8f4a79ca10658d5c46998d527e4ab8ae59978",
        hkex: "dfeeab4726febaf20d322ba1d9b5b931bddd8d5d777b7b9d7b5fd988e376fc49",
        huazheng: "6fa1f71a8255de81ccf0a827e2193eafeb197f1aabfba9e8212af79bb100d1f0",
    }
    for path, digest in expected.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest

    command = ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"]
    extracted = subprocess.run(command, check=True, capture_output=True).stdout
    pages = extracted.decode("utf-8").split("\f")
    assert "ZTE Corporation" in pages[9] and "9144030027939873X7" in pages[9]
    assert "股票代码：000063" in pages[9] and "股票代码：763" in pages[9]
    amounts = {}
    locations = {}
    for field, page_number, label in (
        ("total_assets_cny", 107, "资产总计"),
        ("total_liabilities_cny", 108, "负债合计"),
        ("ordinary_parent_equity_cny", 109, "归属于母公司普通股股东权益合计"),
        ("noncontrolling_interests_cny", 109, "少数股东权益"),
        ("total_equity_cny", 109, "股东权益合计"),
    ):
        page = pages[page_number - 1]
        assert "人民币千元" in page and "2023年12月31日" in page
        match = re.search(r"^\s*" + label + r"\s+([\d,]+)\s+([\d,]+)\s*$", page, re.M)
        assert match is not None, field
        amounts[field] = int(match.group(1).replace(",", "")) * 1000
        locations[field] = {"pdf_page": page_number, "printed_page": page_number - 1, "label": label}
    assert amounts["total_assets_cny"] == amounts["total_liabilities_cny"] + amounts["total_equity_cny"]
    assert amounts["total_equity_cny"] == amounts["ordinary_parent_equity_cny"] + amounts["noncontrolling_interests_cny"]
    share_page = " ".join(pages[34].split())
    share_match = re.search(r"股本总数为 ([\d,]+) 股（其中 A 股 ([\d,]+) 股，H 股 ([\d,]+) 股", share_page)
    assert share_match is not None
    total_shares, a_shares, h_shares = [int(value.replace(",", "")) for value in share_match.groups()]
    assert total_shares == a_shares + h_shares

    with (PROCESSED / "latest_indicator_scores.csv").open(encoding="utf-8-sig", newline="") as handle:
        selected = [row for row in csv.DictReader(handle) if row["WBA ID"] == "PT_01998"]
    assert len(selected) == 1
    score = selected[0]
    assert score["COMPANY NAME "] == "ZTE" and score["YEAR "] == "2023"
    with (PROCESSED / "latest_full_assessment.csv").open(encoding="utf-8-sig", newline="") as handle:
        evidence = [row for row in csv.DictReader(handle) if row["WBA ID"] == "PT_01998"]
    assert len(evidence) == 46 and all(row["Year"] == "2023" for row in evidence)
    references = sorted({row["Reference"] for row in evidence if row["Reference"]})

    with zipfile.ZipFile(hkex) as archive:
        shared = ET.fromstring(archive.read("xl/sharedStrings.xml"))
        strings = ["".join(node.itertext()) for node in shared.findall("s:si", NS)]
        rows = []
        for row in ET.fromstring(archive.read("xl/worksheets/sheet1.xml")).findall("s:sheetData/s:row", NS):
            values = {}
            for cell in row.findall("s:c", NS):
                node = cell.find("s:v", NS)
                value = node.text if node is not None else None
                if cell.attrib.get("t") == "s":
                    value = strings[int(value)]
                values[re.sub(r"\d", "", cell.attrib["r"])] = value
            rows.append((row.attrib["r"], values))
    matched = [(row, values) for row, values in rows if values.get("F") == score["ISIN "]]
    assert len(matched) == 1
    excel_row, security = matched[0]
    assert (security["A"], security["B"], security["Q"]) == ("00763", "ZTE", "HKD")
    latest = json.loads(huazheng.read_text(encoding="utf-8"))
    assert latest["code"] == 200 and latest["data"]["stockCode"] == "000063.SZ"

    inputs = [*expected, PROCESSED / "latest_indicator_scores.csv", PROCESSED / "latest_full_assessment.csv"]
    result = {
        "status": "PASS", "scope": "One issuer identity and extraction pilot; no calibration or market run.",
        "issuer": {"name": "ZTE Corporation", "legal_name": "中兴通讯股份有限公司", "unified_social_credit_code": "9144030027939873X7",
                   "a_share_ticker": "000063.SZ", "h_share_ticker": "00763.HK", "identity_pdf_page": 10,
                   "a_share_isin": None, "match_basis": "Annual-report issuer and both listings; source ISIN resolves to the HKD security, not the A-share."},
        "financial": {"fiscal_date": "2023-12-31", "filing_url_date": "2024-03-09", "scope": "consolidated group",
                      "source_currency": "CNY", "source_unit": "CNY thousand", "reported_precision_cny": 1000,
                      **amounts, "locations": locations, "total_issued_shares": total_shares,
                      "a_issued_shares": a_shares, "h_issued_shares": h_shares, "share_count_pdf_page": 35},
        "wba": {"source_row": {key: score[key] for key in list(score)[:8]}, "measure": "CSI social proxy, not comprehensive ESG",
                "evidence_rows": len(evidence), "reference_labels": references,
                "reference_years_in_labels": sorted({year for label in references for year in re.findall(r"20\d{2}", label)}),
                "blank_reference_rows": sum(not row["Reference"] for row in evidence)},
        "hkex_identifier_reference": {"sheet": "Sheet1", "excel_row": int(excel_row), "row": security,
                                     "source_asof_label": rows[1][1]["A"], "historical_2023_identifier_snapshot": False},
        "huazheng_latest": {"source_response": latest, "website_scheme_label": "华证ESG评级2.0", "historical_2023_observation": False},
        "market_cap_cny": None, "market_price_date": None, "book_to_market": None,
        "same_date_joint_calibration_qualified": False,
        "limitations": [
            "Assessment year is not the year of every underlying reference; WBA references include 2020 and 2021.",
            "The latest Huazheng score and 2023 financial statements are separate dated observations, not a contemporaneous fitted sample.",
            "The downloaded HKEX list is labelled 12/10/2026, after its 11/10 retrieval date; retain that label and do not infer historical membership.",
            "Book equity is not intrinsic value; consolidated equity is not A-share market capitalisation.",
            "No market prices, exchange rates, broad-sample representativeness, open redistribution permission, or latent true/disclosed decomposition established.",
        ],
        "input_sha256": {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs},
        "extractor_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "pdftotext_output_sha256": hashlib.sha256(extracted).hexdigest(),
    }
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "issuer": result["issuer"]["a_share_ticker"],
                      "financial": amounts, "same_date_joint_calibration_qualified": False}, ensure_ascii=False))


if __name__ == "__main__":
    main()
