"""Join the CSI300 score, half-year book and 2026-10-09 size snapshots; describe and run the proxy calibrations."""

import csv
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
POOL_SOURCE = HERE / "csi300_huazheng_latest" / "freeze.json"
SCORES_PRIOR = HERE / "csi300_huazheng_latest" / "audited_observations.csv"
SCORES_RESUME = HERE / "csi300_huazheng_resume_20261012" / "observations.csv"
BOOK = HERE / "csi300_book_20260630_v2_resume" / "merged_observations.csv"
SIZE = HERE / "csi300_size_20261009_v2_resume" / "merged_observations.csv"
PROCESSED = ROOT / "data" / "processed" / "disclosure_public_20261012"
OUT = HERE / "csi300_joint_20261009"
COHORT = "CSI300_20261009"
AS_OF = "2026-06-30"
CUTOFF = "2026-10-09"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def save(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def ranks(values):
    order = np.argsort(values, kind="stable")
    result = np.empty(len(values))
    result[order] = np.arange(len(values))
    for value in np.unique(values):
        tied = values == value
        result[tied] = result[tied].mean()
    return result


def spearman(a, b):
    return float(np.corrcoef(ranks(np.asarray(a)), ranks(np.asarray(b)))[0, 1])


def describe(values):
    values = [float(value) for value in values]
    return {"n": len(values), "mean": statistics.fmean(values), "population_sd": statistics.pstdev(values),
            "min": min(values), "median": statistics.median(values), "max": max(values)}


def main():
    inputs = {path.relative_to(ROOT).as_posix(): sha(path)
              for path in (POOL_SOURCE, SCORES_PRIOR, SCORES_RESUME, BOOK, SIZE, Path(__file__))}
    pool = json.loads(POOL_SOURCE.read_text(encoding="utf-8"))["pool"]
    scores = {}
    for path, origin in ((SCORES_PRIOR, "snapshot_20261011"), (SCORES_RESUME, "resume_20261012")):
        for row in read(path):
            if row["status"] == "observed":
                assert row["ticker"] not in scores, "score observed twice: " + row["ticker"]
                scores[row["ticker"]] = {**row, "score_round": origin}
    book = {row["ticker"]: row for row in read(BOOK) if row["status"] == "observed"}
    size = {row["ticker"]: row for row in read(SIZE) if row["status"] == "observed" and row.get("market_cap_cny")}
    rows, exclusions = [], Counter()
    for security in pool:
        ticker = security["ticker"]
        missing = [name for name, table in (("score", scores), ("book", book), ("size", size)) if ticker not in table]
        if missing:
            exclusions["missing_" + "_".join(missing)] += 1
            continue
        s, b, z = scores[ticker], book[ticker], size[ticker]
        parent = float(b["total_parent_equity"])
        common = float(b["common_book_equity"])
        cap = float(z["market_cap_cny"])
        pb = float(z["pb_mrq"]) if z.get("pb_mrq") else None
        rows.append({
            "ticker": ticker, "name": security["name"], "exchange": ticker[-2:], "cohort": COHORT,
            "score": s["score_native"], "grade": s["grade"], "score_date": s["score_date"], "industry": s["industry"],
            "score_round": s["score_round"], "company_type": b["company_type"], "as_of": b["report_date"],
            "notice_date": b["notice_date"], "update_date": b["update_date"], "currency": b["currency"],
            "total_parent_equity": b["total_parent_equity"], "other_equity_tool": b["other_equity_tool"],
            "common_book_equity": b["common_book_equity"], "minority_equity": b["minority_equity"],
            "close_20261009": z["close"], "tradestatus_20261009": z["tradestatus"],
            "total_share_20260630": z["total_share"], "market_cap_cny": z["market_cap_cny"], "price_date": CUTOFF,
            "vendor_pb_mrq": z.get("pb_mrq"),
            "implied_pb_parent": cap / parent,
            "implied_pb_common": cap / common if common > 0 else None,
            "pb_parent_ratio_to_vendor": (cap / parent) / pb if pb else None,
            "pb_common_ratio_to_vendor": (cap / common) / pb if pb and common > 0 else None,
        })
    PROCESSED.mkdir(parents=True, exist_ok=False)
    joint = PROCESSED / "csi300_joint_20261009.csv"
    with joint.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    OUT.mkdir(exist_ok=False)

    sys.path.insert(0, str(ROOT / "src"))
    from abm.disclosure.calibration import main as calibrate
    from abm.disclosure.config import MarketConfig

    template = OUT / "market_template_defaults.json"
    template.write_text(json.dumps(MarketConfig().to_dict(), indent=2) + "\n", encoding="utf-8")
    common = ["--csv", str(joint), "--unit", "CNY yuan", "--issuer-column", "ticker", "--cohort-column", "cohort",
              "--cohort", COHORT, "--currency-column", "currency", "--currency", "CNY", "--template", str(template)]
    # Primary V dispersion: market cap (P0=V0); book equity is the sensitivity case.
    for proxy, column, as_of_column, as_of, publication in (
            ("market_cap", "market_cap_cny", "price_date", CUTOFF, "price_date"),
            ("book", "common_book_equity", "as_of", AS_OF, "notice_date")):
        assert calibrate(["--kind", "book", "--proxy", proxy, "--value-column", column, *common,
                          "--as-of-column", as_of_column, "--as-of", as_of, "--publication-column", publication,
                          "--publication-cutoff", CUTOFF, "--output-config", str(OUT / f"market_{proxy}_sigma.json"),
                          "--report", str(OUT / f"market_{proxy}_sigma_report.json")]) == 0
    score_options = ["--csv", str(joint), "--value-column", "score", "--all-rows", "--raw-lower", "0", "--raw-upper", "100",
                     "--direction", "1", "--unit", "Huazheng ESG composite score points (0-100, higher is better)",
                     "--attribute-label", "Huazheng ESG composite observed proxy",
                     "--template", str(ROOT / "configs/domains/esg.json")]
    # Primary: latent link with the market-cap rank copula; controls isolate the copula and the link.
    for suffix, extra in (("quantile_copula", ["--observation-link", "empirical_quantile", "--size-column", "market_cap_cny"]),
                          ("quantile_independent", ["--observation-link", "empirical_quantile"]),
                          ("linear", [])):
        assert calibrate([*score_options, *extra, "--name", "huazheng_esg_csi300_20260924_" + suffix,
                          "--output-domain", str(OUT / f"domain_huazheng_esg_{suffix}.json"),
                          "--report", str(OUT / f"domain_huazheng_esg_{suffix}_report.json")]) == 0

    score = np.array([float(row["score"]) for row in rows])
    log_book = np.log([float(row["common_book_equity"]) for row in rows])
    log_cap = np.log([float(row["market_cap_cny"]) for row in rows])
    banks = np.array([row["company_type"] != "4" for row in rows])
    stats = {
        "cohort": COHORT, "n_joint": len(rows), "exclusions": dict(exclusions),
        "score_date_counts": dict(Counter(row["score_date"] for row in rows)),
        "score_round_counts": dict(Counter(row["score_round"] for row in rows)),
        "company_type_counts": dict(Counter(row["company_type"] for row in rows)),
        "notice_after_cutoff": [row["ticker"] for row in rows if row["notice_date"] > CUTOFF],
        "updated_after_cutoff": [row["ticker"] for row in rows if row["update_date"] and row["update_date"] > CUTOFF],
        "not_trading_20261009": [row["ticker"] for row in rows if row["tradestatus_20261009"] != "1"],
        "score": describe(score), "log_common_book": describe(log_book), "log_market_cap": describe(log_cap),
        "log_market_to_common_book": describe(log_cap - log_book),
        "spearman": {"score_vs_log_market_cap": spearman(score, log_cap), "score_vs_log_common_book": spearman(score, log_book),
                     "log_market_cap_vs_log_common_book": spearman(log_cap, log_book)},
        "spearman_excluding_financial_templates": {
            "n": int((~banks).sum()), "score_vs_log_market_cap": spearman(score[~banks], log_cap[~banks]),
            "score_vs_log_common_book": spearman(score[~banks], log_book[~banks])},
        "vendor_pb_consistency": {
            kind: {"definition": f"(close*totalShare/{label}) / BaoStock pbMRQ",
                   "n": int(sum(row[key] is not None for row in rows)),
                   "median": float(np.median([row[key] for row in rows if row[key] is not None])),
                   "share_within_2pct": float(np.mean([abs(row[key] - 1) <= .02 for row in rows if row[key] is not None])),
                   "outside_5pct": [row["ticker"] for row in rows if row[key] is not None and abs(row[key] - 1) > .05]}
            for kind, key, label in (("parent", "pb_parent_ratio_to_vendor", "TOTAL_PARENT_EQUITY"),
                                     ("common", "pb_common_ratio_to_vendor", "common_book_equity"))},
        "vendor_pb_note": "The vendor PB denominator matches common equity (parent minus preferred/perpetual instruments) "
                          "far better than parent equity. Remaining common-basis gaps are consistent with share-count "
                          "changes after 2026-06-30 (the carried-share assumption) and are flagged, not adjusted.",
        "interpretation_limits": [
            "Score date labels are native vendor labels, not proven first-publication dates.",
            "Book equity is an accounting proxy for latent value; market cap is a size measure; neither is identified true value.",
            "The current model draws attribute and value independently; a nonzero score-size rank correlation means that "
            "independence is an approximation to be disclosed, not that a joint initialization has been fitted.",
            "Current constituents are not a historical or survivorship-free population."],
    }
    save(OUT / "joint_statistics.json", stats)
    outputs = {path.relative_to(ROOT).as_posix(): sha(path) for path in sorted(OUT.iterdir()) if path.is_file()}
    outputs[joint.relative_to(ROOT).as_posix()] = sha(joint)
    save(OUT / "manifest.json", {"inputs": inputs, "outputs": outputs})
    print(json.dumps({key: stats[key] for key in ("n_joint", "exclusions", "spearman", "vendor_pb_consistency")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
