"""Fetch and inspect five author-published individual daily-return teaching series."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np

DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[1]
RAW = ROOT / "data/raw/disclosure_market_public_20261011"
PROCESSED = ROOT / "data/processed/disclosure_market_public_20261011"
AUTHOR_PAGE = "https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition"
PUBLISHER_EXCERPT = "https://catalogimages.wiley.com/images/db/pdf/9780470414354.excerpt.pdf"
BASE = "https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/"
FILES = (("IBM", "d-ibm3dx7008.txt", 9845), ("Intel", "d-intc7208.txt", 9096),
         ("3M", "d-3m7008.txt", 9845), ("Microsoft", "d-msft8608.txt", 5752),
         ("Citigroup", "d-c8608.txt", 5592))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, payload):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def download(url, path):
    if path.exists():
        return {"url": url, "path": path.relative_to(ROOT).as_posix(), "sha256": sha(path),
                "bytes": path.stat().st_size, "fetched_this_invocation": False}
    with urlopen(Request(url, headers={"User-Agent": "Academic-data-availability-check/1.0"}), timeout=45) as response:
        body = response.read(10 * 1024 * 1024 + 1)
        if len(body) > 10 * 1024 * 1024:
            raise ValueError("bounded small-file download exceeded 10 MiB")
        final_url = response.geturl()
        content_type = response.headers.get("Content-Type")
    path.write_bytes(body)
    return {"url": url, "final_url": final_url, "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha(path), "bytes": len(body), "content_type": content_type,
            "fetched_this_invocation": True, "retrieved_at_utc": datetime.now(UTC).isoformat()}


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    manifest_path = RAW / "tsay_download_manifest.json"
    manifest = {"checked_at_utc": datetime.now(UTC).isoformat(), "author_page": AUTHOR_PAGE,
                "publisher_excerpt": PUBLISHER_EXCERPT, "fetch_script_sha256": sha(Path(__file__)),
                "selection": "Exactly the five individual stocks in Tsay (2010) Chapter 1 Table 1.2, in table order; no outcome-based selection. Market-index columns are excluded from the individual-stock panel.",
                "return_definition_evidence": "Publisher excerpt printed p.19, section 1.2.5 states CRSP returns used in this section include dividend payments. Table 1.2 printed p.11 and Example 1.2 explicitly identify the daily stock series and d-ibm3dx7008.txt; raw counts and numerical summaries checked below.",
                "license": {"public_author_download": True, "account_required_for_these_urls": False,
                            "explicit_open_data_license_found": False,
                            "status": "Public author-published teaching data for local research inspection; no blanket right to redistribute or republish CRSP raw data established. University site and Wiley excerpt retain copyright; no license is inferred from anonymous HTTP access."},
                "files": [], "status": "running"}
    records, panel = [], []
    write_json(manifest_path, manifest)
    for label, filename, expected_count in FILES:
        record = download(BASE + filename, RAW / filename)
        rows = (RAW / filename).read_text(encoding="utf-8-sig").splitlines()
        header = rows[0].split()
        parsed = [line.split() for line in rows[1:] if line.strip()]
        if any(len(row) != len(header) for row in parsed):
            raise ValueError(f"malformed row in {filename}; no imputation performed")
        dates = [datetime.strptime(row[0], "%Y%m%d").date().isoformat() for row in parsed]
        values = np.array([float(row[1]) for row in parsed])
        finite = bool(np.all(np.isfinite(values)))
        if not finite:
            raise ValueError(f"nonfinite return in {filename}; no imputation performed")
        centered = values - values.mean()
        kurtosis = float(np.mean(centered ** 4) / np.mean(centered ** 2) ** 2 - 3)
        checks = {"count_matches_publisher_table": len(values) == expected_count,
                  "dates_unique": len(set(dates)) == len(dates), "dates_strictly_increasing": all(a < b for a, b in zip(dates, dates[1:])),
                  "all_returns_finite": finite, "all_returns_at_least_minus_one": bool(np.all(values >= -1))}
        if not all(checks.values()):
            raise ValueError(f"inspection failed in {filename}: {checks}")
        record.update(author_label=label, raw_header=header, selected_column=header[1], observations=len(values),
                      first_date=dates[0], last_date=dates[-1], checks=checks,
                      mean_simple_return=float(values.mean()), daily_volatility=float(values.std(ddof=1)),
                      excess_kurtosis=kurtosis, minimum_return=float(values.min()), maximum_return=float(values.max()),
                      zero_return_observations=int((values == 0).sum()), missing_rows_imputed=0,
                      units="Decimal simple daily total returns, already including dividends per cited chapter; do not multiply by .01 or add dividends again.")
        records.append(record)
        panel.extend((date, label, row[1], filename) for date, row in zip(dates, parsed))
        manifest["files"] = records
        write_json(manifest_path, manifest)
    ibm = records[0]
    assert round(100 * ibm["daily_volatility"], 3) == 1.693
    assert round(ibm["excess_kurtosis"], 2) == 9.92
    assert round(100 * ibm["mean_simple_return"], 3) == .040
    manifest["publisher_evidence_file"] = download(PUBLISHER_EXCERPT, RAW / "tsay_2010_publisher_chapter1_excerpt.pdf")
    csv_path = PROCESSED / "tsay_five_company_daily_returns.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("date", "author_company_label", "simple_total_return", "source_file"))
        writer.writerows(panel)
    manifest.update(status="completed_source_inspection", company_count=5, company_day_rows=len(panel),
                    transformed_panel={"path": csv_path.relative_to(ROOT).as_posix(), "sha256": sha(csv_path),
                                       "processing": "Keep original second-column decimal return strings and observed dates; discard index columns; no interpolation, winsorization, split adjustment, duplicate removal or dividend addition."},
                    identity_limits="Author company labels are not verified permanent security identifiers; corporate histories and delisting-return coverage are not separately documented.",
                    sampling_limits=["Author-selected five teaching examples, not random or a representative firm panel. Large and long-lived listed firms are overrepresented; sector, size and survivorship selection cannot be estimated from five series.",
                                     "Different start dates, all ending 2008-12-31, unlike the 2000-2025 French training target. Calendar overlap is not a new held-out target.",
                                     "No population snapshot, firm-entry/exit coverage, underlying quotes/dividends, permanent IDs or independent audit of adjustments. Provider return convention accepted from primary-source chapter, not reconstructed.",
                                     "Series and descriptive statistics are now inspected development data. They must never later be described as unseen evaluation data."],
                    empirical_calibration="pending_not_attempted")
    write_json(manifest_path, manifest)
    write_json(DIRECTORY / "tsay_source_inspection.json", manifest)
    lines = ["# 公开个股日收益样本核查", "",
             f"来源为[芝加哥大学 Booth 的 Tsay 作者教材数据页]({AUTHOR_PAGE})；下载表1.2的全部5个个股示例，排除市场指数列，不按收益结果挑选。共{len(panel)}个公司日观察，原始文本和文件哈希已保存。", "",
             f"[Wiley官方第1章摘录]({PUBLISHER_EXCERPT})第19页§1.2.5说明该节CRSP收益已包含股息；第11页表1.2及IBM实例与作者文件对应。IBM样本数、均值、波动率、峰度与出版表的舍入值相符。原始收益是小数制简单总收益，不再加股息，也不再除以100。", "",
             "| 作者公司标签 | 首日 | 末日 | 观察数 |", "|---|---|---|---:|"]
    for record in records:
        lines.append(f"| {record['author_label']} | {record['first_date']} | {record['last_date']} | {record['observations']} |")
    lines.extend(["", "日期和缺失处理：逐行保留实际观察日，检查递增、不重复、有限且收益≥−1；未插补周末/停牌/假日，未缩尾，未额外复权。原网页中微软/Citigroup起始日期文字有误，Intel在另一章被叫作log return；本地采用实际日期，并由表1.2的样本数与IBM数值核验简单收益单位，不用有冲突的网页文字改写数据。", "",
                  "样本局限：五家公司是作者选的教材示例，偏向规模大、上市久的公司，不代表整个个股市场；不同起日且止于2008年。没有企业总体名单、退出覆盖、永久证券ID或可审计的底层分红/复权字段，幸存者及行业规模偏差无法消除。它们能支持个股口径开发核查，不能直接升级为代表性正式校准数据。", "",
                  "使用条件：这些作者文件确实无需账号即可公开下载。页面未找到明确开放数据许可；‘能下载’不等于‘可重新发布CRSP原始数据’。本次仅留本地研究快照和核查，不声称获得开放再分发许可，发布/共享原始文件前需另行核实。Wiley章节仅作为来源证据，保留版权。", "",
                  "未拟合模型、未据此改变参数、未运行额外种子；已看过这批数据及摘要，后续不得称为未触碰留出数据。现阶段先解决观察单位与收益定义，再决定是否采用更全面且许可清楚的数据。"])
    (DIRECTORY / "tsay_source_inspection.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": manifest["status"], "companies": 5, "rows": len(panel), "license": manifest["license"]["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except BaseException as error:
        print(f"Source inspection failed; preserved downloaded files and partial manifest: {error}", file=sys.stderr)
        raise
