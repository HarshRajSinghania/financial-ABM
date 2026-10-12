"""Fit observed-proxy initial distributions from explicitly selected CSV cohorts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import Counter
from dataclasses import fields, replace
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .config import MarketConfig, load_market_config
from .domain import OBSERVATION_LINKS, DomainSpec, load_domain

STATE_ASSUMPTION = (
    "The CSV measures an observed proxy. Assigning independent empirical draws to the simulated "
    "true state with zero initial inflation is a modeling assumption, not an identified "
    "decomposition of real capability and misrepresentation."
)
LATENT_STATE_ASSUMPTION = (
    "The CSV measures an observed proxy. Treating it as a saturating empirical-quantile image of a latent "
    "standard-normal true state with zero initial inflation is a modeling assumption, not an identified "
    "decomposition of real capability and misrepresentation."
)


BOOK_PROXIES = {
    "book": ("book_proxy_lognormal_dispersion_only",
             "Book equity is an observed proxy. Using its fitted dispersion for latent intrinsic value is a modeling "
             "assumption, not identification of true firm value."),
    "market_cap": ("market_cap_proxy_lognormal_dispersion_only",
                   "Market capitalization is an observed size measure. Because the model starts at P0=V0, using its "
                   "fitted dispersion for initial intrinsic value matches the initial market-cap dispersion by assumption; "
                   "it does not identify true firm value."),
}


def _average_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    start = 0
    while start < len(order):
        stop = start
        while stop + 1 < len(order) and values[order[stop + 1]] == values[order[start]]:
            stop += 1
        for position in range(start, stop + 1):
            ranks[order[position]] = (start + stop) / 2
        start = stop + 1
    return ranks


def file_identity(path: Path) -> dict[str, Any]:
    return {"path": path.as_posix(), "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def calibrate_csv(
    source_csv: str | Path,
    template: DomainSpec,
    *,
    value_column: str,
    year_column: str | None,
    year: str | None,
    raw_lower: float,
    raw_upper: float,
    direction: int,
    unit: str,
    name: str,
    attribute_label: str,
    source_url: str | None = None,
    raw_source: str | Path | None = None,
    observation_link: str = "linear",
    size_column: str | None = None,
) -> tuple[DomainSpec, dict[str, Any]]:
    if observation_link not in OBSERVATION_LINKS:
        raise ValueError(f"observation_link must be one of {OBSERVATION_LINKS}")
    if size_column is not None and observation_link != "empirical_quantile":
        raise ValueError("a size rank correlation requires the empirical quantile link")
    if (year_column is None) != (year is None):
        raise ValueError("year_column and year must be specified together, or both explicitly None")
    if not unit.strip():
        raise ValueError("unit must be explicitly specified")
    if direction not in (-1, 1):
        raise ValueError("direction must be +1 or -1")
    if not math.isfinite(raw_lower) or not math.isfinite(raw_upper) or raw_lower >= raw_upper:
        raise ValueError("theoretical raw bounds must be finite and ordered")
    source_csv = Path(source_csv)
    values, sizes = [], []
    total_rows = filtered_out = missing_values = missing_years = 0
    with source_csv.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if len(set(headers)) != len(headers) or not headers or any(not field.strip() for field in headers):
            raise ValueError("CSV headers must be present, nonblank and unique")
        required = ({value_column} | ({year_column} if year_column is not None else set())
                    | ({size_column} if size_column is not None else set()))
        if required - set(headers):
            raise ValueError(f"missing explicitly selected CSV columns: {sorted(required - set(headers))}")
        for row_number, row in enumerate(reader, start=2):
            total_rows += 1
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"malformed CSV record {row_number}")
            if year_column is not None:
                if not row[year_column].strip():
                    missing_years += 1
                if row[year_column].strip() != str(year):
                    filtered_out += 1
                    continue
            text = row[value_column].strip()
            if not text:
                missing_values += 1
                continue
            try:
                value = float(text)
            except ValueError as error:
                raise ValueError(f"nonnumeric proxy at CSV record {row_number}: {text!r}") from error
            if not math.isfinite(value) or not raw_lower <= value <= raw_upper:
                raise ValueError(f"proxy outside finite theoretical bounds at CSV record {row_number}: {text!r}")
            if size_column is not None:
                try:
                    size = float(row[size_column].strip())
                except ValueError as error:
                    raise ValueError(f"missing or nonnumeric size at CSV record {row_number}") from error
                if not math.isfinite(size) or size <= 0:
                    raise ValueError(f"size must be finite and positive at CSV record {row_number}")
                sizes.append(size)
            values.append(value)
    if len(values) < 2 or len(set(values)) < 2:
        raise ValueError("selected cohort needs at least two distinct finite proxy values")
    distribution = tuple(sorted(Counter(values).items()))
    mean, sd = statistics.fmean(values), statistics.pstdev(values)
    size_dependence = None
    latent_correlation = 0.0
    if size_column is not None:
        log_sizes = [math.log(size) for size in sizes]
        if len(set(log_sizes)) < 2:
            raise ValueError("size rank correlation needs at least two distinct sizes")
        spearman = statistics.correlation(_average_ranks(values), _average_ranks(log_sizes))
        latent_correlation = direction * 2 * math.sin(math.pi * spearman / 6)
        size_dependence = {
            "size_column": size_column, "n": len(sizes), "spearman_raw_vs_log_size": spearman,
            "conversion": "Gaussian copula: latent Pearson = 2*sin(pi*spearman/6), signed by direction so it "
                          "refers to goodness",
            "initial_size_rank_correlation": latent_correlation,
            "assumption": "The model correlates latent goodness with log intrinsic value; with P0=V0 their initial "
                          "ranks equal the market-cap ranks. Only this rank dependence is fitted; the copula form "
                          "is an assumption.",
        }
    domain = replace(
        template, name=name, attribute_label=attribute_label, unit=unit, direction=direction,
        raw_lower=raw_lower, raw_upper=raw_upper, initial_mean=mean, initial_sd=sd,
        initial_empirical_distribution=distribution, action_labels={},
        observation_link=observation_link, initial_size_rank_correlation=latent_correlation,
    )
    identified = {"name", "attribute_label", "unit", "direction", "raw_lower", "raw_upper",
                  "initial_mean", "initial_sd", "initial_empirical_distribution", "action_labels",
                  "observation_link", "initial_size_rank_correlation"}
    assumed = {item.name: getattr(domain, item.name) for item in fields(domain) if item.name not in identified}
    report = {
        "status": "observed_proxy_initial_distribution_only",
        "source_csv": file_identity(source_csv),
        "upstream_raw_file": file_identity(Path(raw_source)) if raw_source is not None else None,
        "source_url": source_url,
        "selection": {"value_column": value_column, "year_column": year_column, "year": year,
                      "year_match": "trimmed literal equality" if year_column is not None else "all rows",
                      "input_rows": total_rows, "filtered_out_rows": filtered_out,
                      "missing_year_rows": missing_years, "selected_blank_value_rows": missing_values,
                      "included_rows": len(values), "missing_policy": "exclude blank values; reject nonnumeric, nonfinite and out-of-bounds values"},
        "mapping": {"direction": direction, "unit": unit, "raw_lower": raw_lower, "raw_upper": raw_upper,
                    "fixed_initial_mean": mean, "fixed_initial_sd": sd, "sd_convention": "population, ddof=0"},
        "sample": {"n": len(values), "unique_values": len(distribution), "min": min(values), "max": max(values),
                   "mean": mean, "population_sd": sd, "median": statistics.median(values),
                   "zero_mass": values.count(0.0) / len(values),
                   "lower_bound_mass": values.count(raw_lower) / len(values),
                   "upper_bound_mass": values.count(raw_upper) / len(values)},
        "initialization": {"method": "empirical discrete sampling with replacement" if observation_link == "linear"
                           else "latent standard normal mapped to raw scores by the empirical mid-rank quantile link",
                           "observation_link": observation_link,
                           "raw_value_counts": [list(pair) for pair in distribution],
                           "state_assumption": STATE_ASSUMPTION if observation_link == "linear" else LATENT_STATE_ASSUMPTION,
                           "size_dependence": size_dependence,
                           "joint_distribution": ("No company identity, size-attribute correlation, measurement-error process or longitudinal dynamics is fitted."
                                                  if size_dependence is None else
                                                  "Only the rank correlation with size is fitted, through a Gaussian copula; no company identity, measurement-error process or longitudinal dynamics is fitted.")},
        "assumption_template": template.name,
        "unidentified_domain_parameters": list(assumed),
        "assumed_domain_parameters": assumed,
        "other_unidentified_mechanisms": ["latent capability and initial inflation", "investor preferences and learning",
                                          "price impact and financing transmission", "policy causal effects"],
    }
    return domain, report


def calibrate_book_csv(
    source_csv: str | Path,
    template: MarketConfig,
    *,
    issuer_column: str,
    value_column: str,
    cohort_column: str,
    cohort: str,
    currency_column: str,
    currency: str,
    as_of_column: str,
    as_of: str,
    publication_column: str,
    publication_cutoff: str,
    unit: str,
    source_url: str | None = None,
    raw_source: str | Path | None = None,
    proxy: str = "book",
) -> tuple[MarketConfig, dict[str, Any]]:
    if proxy not in BOOK_PROXIES:
        raise ValueError(f"proxy must be one of {sorted(BOOK_PROXIES)}")
    if not cohort.strip() or not currency.strip() or not unit.strip():
        raise ValueError("cohort, currency and amount unit must be explicitly specified")
    as_of_date, cutoff_date = date.fromisoformat(as_of), date.fromisoformat(publication_cutoff)
    if cutoff_date < as_of_date:
        raise ValueError("publication_cutoff must not be earlier than as_of")
    source_csv = Path(source_csv)
    values, issuers = [], []
    seen = set()
    total_rows = cohort_exclusions = date_exclusions = 0
    with source_csv.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if len(set(headers)) != len(headers) or not headers or any(not field.strip() for field in headers):
            raise ValueError("CSV headers must be present, nonblank and unique")
        required = {issuer_column, value_column, cohort_column, currency_column, as_of_column, publication_column}
        if required - set(headers):
            raise ValueError(f"missing explicitly selected CSV columns: {sorted(required - set(headers))}")
        for row_number, row in enumerate(reader, start=2):
            total_rows += 1
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"malformed CSV record {row_number}")
            if not row[cohort_column].strip() or not row[as_of_column].strip():
                raise ValueError(f"missing cohort or as_of at CSV record {row_number}")
            if row[cohort_column].strip() != cohort:
                cohort_exclusions += 1
                continue
            if row[as_of_column].strip() != as_of:
                date_exclusions += 1
                continue
            issuer = row[issuer_column].strip()
            if not issuer or issuer in seen:
                raise ValueError(f"missing or duplicate issuer at CSV record {row_number}: {issuer!r}")
            if row[currency_column].strip() != currency:
                raise ValueError(f"currency mismatch at CSV record {row_number}")
            try:
                publication = date.fromisoformat(row[publication_column].strip())
            except ValueError as error:
                raise ValueError(f"missing or invalid publication date at CSV record {row_number}") from error
            if publication > cutoff_date:
                raise ValueError(f"publication after cutoff at CSV record {row_number}")
            if publication < as_of_date:
                raise ValueError(f"publication before as_of at CSV record {row_number}")
            text = row[value_column].strip()
            try:
                value = float(text)
            except ValueError as error:
                raise ValueError(f"missing or nonnumeric book value at CSV record {row_number}: {text!r}") from error
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"book value must be finite and positive at CSV record {row_number}")
            values.append(value)
            issuers.append(issuer)
            seen.add(issuer)
    if len(values) < 2:
        raise ValueError("selected cohort needs at least two distinct issuers with positive book values")
    logs = [math.log(value) for value in values]
    mu, sigma = statistics.fmean(logs), statistics.pstdev(logs)
    config = replace(template, intrinsic_value_log_sd=sigma)
    report = {
        "status": BOOK_PROXIES[proxy][0],
        "proxy": proxy,
        "source_csv": file_identity(source_csv),
        "upstream_raw_file": file_identity(Path(raw_source)) if raw_source is not None else None,
        "source_url": source_url,
        "selection": {"issuer_column": issuer_column, "value_column": value_column,
                      "cohort_column": cohort_column, "cohort": cohort,
                      "currency_column": currency_column, "currency": currency,
                      "as_of_column": as_of_column, "as_of": as_of,
                      "publication_column": publication_column, "publication_cutoff": publication_cutoff,
                      "match": "trimmed literal equality for cohort and as_of; publication between as_of and cutoff inclusive",
                      "input_rows": total_rows, "filtered_out_rows": cohort_exclusions + date_exclusions,
                      "filtered_out_cohort_rows": cohort_exclusions, "filtered_out_as_of_rows": date_exclusions,
                      "included_rows": len(values), "issuer_ids": issuers,
                      "missing_policy": "reject missing selectors and selected missing issuer, currency, publication or book value; reject duplicate issuers, mixed currencies, publications outside [as_of, cutoff] and nonpositive or nonfinite book values"},
        "sample": {"n": len(values), "min": min(values), "max": max(values)},
        "fit": {"distribution": "lognormal", "mu": mu, "sigma": sigma, "unit": unit,
                "log_convention": "natural logarithm of values in the declared input amount unit",
                "sd_convention": "population, ddof=0; equal book values permit sigma=0"},
        "updated_market_parameters": {"intrinsic_value_log_sd": sigma},
        "initialization": {
            "method": "independent lognormal draws using fitted sigma, normalized to total intrinsic value n_firms",
            "currency_scale": "The fitted mu belongs to the original input amount unit. Normalization discards mu and the absolute monetary scale; no currency or unit conversion is performed.",
            "state_assumption": BOOK_PROXIES[proxy][1],
            "joint_distribution": "No issuer-specific initialization, observed market-cap size distribution or size-attribute joint dependence is fitted.",
        },
        "unidentified_market_parameters": [item.name for item in fields(template) if item.name != "intrinsic_value_log_sd"],
    }
    return config, report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=("score", "book"), default="score")
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--value-column", required=True)
    parser.add_argument("--year-column")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--year")
    selection.add_argument("--all-rows", action="store_true")
    parser.add_argument("--raw-lower", type=float)
    parser.add_argument("--raw-upper", type=float)
    parser.add_argument("--direction", type=int, choices=(-1, 1))
    parser.add_argument("--unit", required=True)
    parser.add_argument("--name")
    parser.add_argument("--attribute-label")
    parser.add_argument("--observation-link", choices=OBSERVATION_LINKS)
    parser.add_argument("--size-column")
    parser.add_argument("--proxy", choices=sorted(BOOK_PROXIES))
    parser.add_argument("--issuer-column")
    parser.add_argument("--cohort-column")
    parser.add_argument("--cohort")
    parser.add_argument("--currency-column")
    parser.add_argument("--currency")
    parser.add_argument("--as-of-column")
    parser.add_argument("--as-of")
    parser.add_argument("--publication-column")
    parser.add_argument("--publication-cutoff")
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--source-url")
    parser.add_argument("--raw-source", type=Path)
    parser.add_argument("--output-domain", type=Path)
    parser.add_argument("--output-config", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args(argv)
    score_fields = ("raw_lower", "raw_upper", "direction", "name", "attribute_label", "output_domain")
    book_fields = ("issuer_column", "cohort_column", "cohort", "currency_column", "currency", "as_of_column",
                   "as_of", "publication_column", "publication_cutoff", "output_config")
    required = score_fields if args.kind == "score" else book_fields
    missing = ["--" + field.replace("_", "-") for field in required if getattr(args, field) is None]
    if missing:
        parser.error(f"{args.kind} requires: {', '.join(missing)}")
    unused = (book_fields + ("proxy",) if args.kind == "score"
              else score_fields + ("year_column", "year", "observation_link", "size_column"))
    if any(getattr(args, field) is not None for field in unused) or (args.kind == "book" and args.all_rows):
        parser.error("do not mix score and book options")
    if args.kind == "score" and ((args.year is None and not args.all_rows)
                                or (args.year is not None and args.year_column is None)
                                or (args.all_rows and args.year_column is not None)):
        parser.error("use --year with --year-column, or --all-rows without a year column")
    output = args.output_domain if args.kind == "score" else args.output_config
    output_kind = "domain" if args.kind == "score" else "config"
    if output.resolve() == args.report.resolve():
        parser.error(f"{output_kind} and report outputs must be different files")
    if output.exists() or args.report.exists():
        parser.error("output files already exist; choose new paths")
    try:
        if args.kind == "score":
            domain, report = calibrate_csv(
                args.csv, load_domain(args.template), value_column=args.value_column,
                year_column=args.year_column, year=args.year, raw_lower=args.raw_lower, raw_upper=args.raw_upper,
                direction=args.direction, unit=args.unit, name=args.name, attribute_label=args.attribute_label,
                source_url=args.source_url, raw_source=args.raw_source,
                observation_link=args.observation_link or "linear", size_column=args.size_column,
            )
        else:
            config, report = calibrate_book_csv(
                args.csv, load_market_config(args.template), issuer_column=args.issuer_column,
                value_column=args.value_column, cohort_column=args.cohort_column, cohort=args.cohort,
                currency_column=args.currency_column, currency=args.currency,
                as_of_column=args.as_of_column, as_of=args.as_of, publication_column=args.publication_column,
                publication_cutoff=args.publication_cutoff, unit=args.unit,
                source_url=args.source_url, raw_source=args.raw_source, proxy=args.proxy or "book",
            )
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    report["template_file"] = file_identity(args.template)
    payload = {
        "_note": report["initialization"]["state_assumption"] + " Only the initial proxy distribution is fitted. Costs, decay, delays and policy parameters are inherited assumptions, not empirical estimates.",
        "_sources": [args.source_url] if args.source_url else [],
        "_calibration": {key: report[key] for key in ("status", "source_csv", "upstream_raw_file", "selection", "sample", "template_file", "unidentified_domain_parameters")},
        **domain.to_dict(),
    } if args.kind == "score" else config.to_dict()
    output.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    report["generated_utc"] = datetime.now(timezone.utc).isoformat()
    report["output_" + output_kind] = file_identity(output)
    report["calibration_code"] = file_identity(Path(__file__))
    with args.report.open("x", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({output_kind: str(output), "report": str(args.report), "included_rows": report["sample"]["n"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
