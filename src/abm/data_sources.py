"""Immutable public-data snapshots and point-in-time Stage 3 adapters."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import UTC, date, datetime, tzinfo
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Mapping, Sequence

from .schemas import FactorEvent

SEC_API_DOCS = "https://www.sec.gov/search-filings/edgar-application-programming-interfaces"
FRED_API_DOCS = "https://fred.stlouisfed.org/docs/api/fred/series_observations.html"
ALPHA_VANTAGE_DOCS = "https://www.alphavantage.co/documentation/"


class DataSourceError(ValueError):
    """A source failed or cannot support the requested provenance contract."""


def _fetch(url: str, *, user_agent: str = "auditable-market-abm/0.1") -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        raise DataSourceError(f"public-data request failed with HTTP {exc.code}") from None
    except (urllib.error.URLError, TimeoutError):
        raise DataSourceError("public-data request failed; no snapshot was written") from None


def _json_payload(raw: bytes) -> dict[str, Any]:
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise DataSourceError("source did not return valid JSON") from None
    if not isinstance(payload, dict):
        raise DataSourceError("source must return a JSON object")
    errors = ("Error Message", "Note", "Information", "error_code", "error")
    if any(key in payload for key in errors):
        raise DataSourceError("provider returned an API error or quota/entitlement notice")
    return payload


def write_snapshot(
    snapshot_dir: str | Path,
    *,
    source: str,
    source_url: str,
    payloads: Mapping[str, bytes],
    date_start: str,
    date_end: str,
    version: str,
    metadata: Mapping[str, Any] | None = None,
) -> Path:
    """Commit payloads and their provenance together without replacing a snapshot."""
    destination = Path(snapshot_dir)
    if destination.exists():
        raise FileExistsError(destination)
    if not payloads or any(not name or name in (".", "..") or Path(name).name != name
                           or name.lower() == "manifest.json" for name in payloads):
        raise ValueError("snapshot payloads must use nonempty simple filenames")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="public-data-", dir=destination.parent) as temporary:
        temporary_dir = Path(temporary)
        files = {}
        for name, raw in payloads.items():
            (temporary_dir / name).write_bytes(raw)
            files[name] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
        manifest = {
            "schema_version": "0.1.0", "source": source, "source_url": source_url,
            "retrieved_at": datetime.now(UTC).isoformat(), "date_start": date_start,
            "date_end": date_end, "version": version, "files": files,
            "metadata": dict(metadata or {}),
        }
        (temporary_dir / "manifest.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        temporary_dir.replace(destination)
    return destination


def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def _aware_timestamp(value: str) -> datetime:
    timestamp = datetime.fromisoformat(value)
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise DataSourceError("availability timestamp must include its UTC offset")
    return timestamp


def parse_sec_submissions(
    payload: Mapping[str, Any],
    *,
    cik: str | int | None = None,
    forms: Sequence[str] = ("8-K", "10-Q", "10-K"),
) -> tuple[dict[str, Any], ...]:
    company_cik = int(cik if cik is not None else payload["cik"])
    recent = payload.get("filings", {}).get("recent", payload)
    required = ("accessionNumber", "form", "filingDate", "reportDate", "acceptanceDateTime", "primaryDocument")
    if any(key not in recent for key in required):
        raise DataSourceError("SEC submissions lack exact acceptance metadata")
    if len({len(recent[key]) for key in required}) != 1:
        raise DataSourceError("SEC submissions columns have unequal lengths")
    filings = []
    for index, form in enumerate(recent["form"]):
        if form not in forms:
            continue
        accession = recent["accessionNumber"][index]
        accepted = _aware_timestamp(recent["acceptanceDateTime"][index])
        source_url = (
            f"https://www.sec.gov/Archives/edgar/data/{company_cik}/"
            f"{accession.replace('-', '')}/{recent['primaryDocument'][index]}"
        )
        filings.append({
            "cik": str(company_cik), "accession": accession, "form": form,
            "filing_date": recent["filingDate"][index], "report_date": recent["reportDate"][index],
            "event_time": accepted.isoformat(), "available_at": accepted.isoformat(),
            "source_url": source_url, "acceptance_raw": recent["acceptanceDateTime"][index],
            "time_basis": "submissions_acceptanceDateTime_as_supplied",
        })
    return tuple(filings)


def parse_sec_companyfacts(
    payload: Mapping[str, Any],
    *,
    filings: Sequence[Mapping[str, Any]] = (),
    as_of: datetime | None = None,
) -> tuple[dict[str, Any], ...]:
    """Retain accession-specific facts; period end and filed date are not availability."""
    if as_of is not None:
        as_of = _aware_timestamp(as_of.isoformat())
    availability = {str(filing["accession"]): filing for filing in filings}
    rows = []
    for taxonomy, concepts in payload["facts"].items():
        for concept, fact in concepts.items():
            for unit, observations in fact["units"].items():
                for observation in observations:
                    filing = availability.get(str(observation["accn"]))
                    accepted = _aware_timestamp(str(filing["available_at"])) if filing else None
                    if as_of is not None and (accepted is None or accepted > as_of):
                        continue
                    rows.append({
                        "taxonomy": taxonomy, "concept": concept, "unit": unit,
                        "value": observation["val"], "period_start": observation.get("start"),
                        "period_end": observation["end"], "accession": observation["accn"],
                        "form": observation.get("form"), "filed_date": observation.get("filed"),
                        "available_at": accepted.isoformat() if accepted else None,
                        "source_url": filing["source_url"] if filing else None,
                        "time_basis": filing["time_basis"] if filing else "unmatched_accession",
                    })
    return tuple(rows)


def download_sec_snapshot(
    snapshot_dir: str | Path,
    *,
    cik: str | int,
    user_agent: str,
    kind: str = "submissions",
) -> Path:
    if Path(snapshot_dir).exists():
        raise FileExistsError(snapshot_dir)
    identifier = f"CIK{int(cik):010d}"
    if kind == "submissions":
        url = f"https://data.sec.gov/submissions/{identifier}.json"
    elif kind == "companyfacts":
        url = f"https://data.sec.gov/api/xbrl/companyfacts/{identifier}.json"
    else:
        raise ValueError("SEC kind must be submissions or companyfacts")
    raw = _fetch(url, user_agent=user_agent)
    payload = _json_payload(raw)
    if kind == "submissions":
        rows = parse_sec_submissions(payload, cik=cik)
        dates = [row["available_at"] for row in rows]
    else:
        rows = parse_sec_companyfacts(payload)
        dates = [row["period_end"] for row in rows]
    return write_snapshot(
        snapshot_dir, source=f"SEC {kind}", source_url=url,
        payloads={f"{kind}.json": raw, f"parsed_{kind}.json": _json_bytes(rows)},
        date_start=min(dates, default=""), date_end=max(dates, default=""), version="SEC REST JSON v1",
        metadata={"docs_url": SEC_API_DOCS,
                  "time_range_basis": "acceptance_as_supplied" if kind == "submissions" else "reporting_period",
                  "historical_api_vintage": False,
                  "additional_submission_files": payload.get("filings", {}).get("files", [])},
    )


class _HTMLText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def parse_sec_filing_index(
    raw: bytes | str, *, source_url: str, acceptance_timezone: tzinfo,
) -> dict[str, Any]:
    """Read SEC's accepted clock using an explicitly verified timezone offset."""
    text = raw.decode("utf-8") if isinstance(raw, bytes) else raw
    parser = _HTMLText()
    parser.feed(text)
    text = " ".join(" ".join(parser.parts).split())
    accepted_match = re.search(r"Accepted\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", text)
    accession_match = re.search(r"SEC Accession No\.?\s*([0-9]{10}-[0-9]{2}-[0-9]{6})", text)
    form_match = re.search(r"Form\s+(\S+)\s+-", text)
    report_match = re.search(r"Period of Report\s+(\d{4}-\d{2}-\d{2})", text)
    filed_match = re.search(r"Filing Date\s+(\d{4}-\d{2}-\d{2})", text)
    cik_match = re.search(r"/edgar/data/(\d+)/", source_url)
    if not all((accepted_match, accession_match, form_match, report_match, filed_match, cik_match)):
        raise DataSourceError("SEC index lacks filing identity or exact accepted time")
    accepted = datetime.fromisoformat(accepted_match[1]).replace(tzinfo=acceptance_timezone)
    accepted = _aware_timestamp(accepted.isoformat())
    return {
        "cik": cik_match[1], "accession": accession_match[1], "form": form_match[1],
        "report_date": report_match[1], "filing_date": filed_match[1],
        "event_time": accepted.isoformat(), "available_at": accepted.isoformat(),
        "source_url": source_url, "acceptance_raw": accepted_match[1],
        "time_basis": "SEC_index_accepted_clock_with_explicit_offset",
    }


def download_sec_filing_snapshot(
    snapshot_dir: str | Path,
    *,
    index_url: str,
    document_url: str,
    acceptance_timezone: tzinfo,
    user_agent: str,
    value_unit: str | None = None,
) -> Path:
    if Path(snapshot_dir).exists():
        raise FileExistsError(snapshot_dir)
    for url in (index_url, document_url):
        if urllib.parse.urlsplit(url).hostname != "www.sec.gov":
            raise ValueError("filing source must be an official www.sec.gov URL")
    if Path(urllib.parse.urlsplit(index_url).path).parent != Path(urllib.parse.urlsplit(document_url).path).parent:
        raise ValueError("SEC document and index must belong to the same filing directory")
    index_raw = _fetch(index_url, user_agent=user_agent)
    filing = parse_sec_filing_index(index_raw, source_url=index_url, acceptance_timezone=acceptance_timezone)
    document_raw = _fetch(document_url, user_agent=user_agent)
    filing["source_url"] = document_url
    payloads = {"filing_index.html": index_raw, "filing_document" + Path(urllib.parse.urlsplit(document_url).path).suffix: document_raw,
                "filings.json": _json_bytes([filing])}
    if filing["form"] in ("13F-HR", "13F-HR/A"):
        holdings = parse_13f_holdings(
            document_raw, institution_id=filing["cik"], period_end=date.fromisoformat(filing["report_date"]),
            accepted_at=_aware_timestamp(filing["available_at"]), source_url=document_url, value_unit=value_unit,
        )
        payloads["holdings.json"] = _json_bytes(holdings)
    elif filing["form"] not in ("8-K", "10-Q", "10-K"):
        raise DataSourceError("unsupported SEC filing form")
    return write_snapshot(
        snapshot_dir, source=f"SEC {filing['form']}", source_url=document_url, payloads=payloads,
        date_start=filing["available_at"], date_end=filing["available_at"], version=filing["accession"],
        metadata={"index_url": index_url, "time_basis": filing["time_basis"],
                  "report_date": filing["report_date"], "acceptance_timezone_offset": filing["available_at"][-6:],
                  "availability_policy": "EDGAR acceptance proxy; not independently measured web dissemination",
                  "payload_representation": "original_HTTP_response_bytes", "value_unit": value_unit},
    )


def sec_factor_events(
    filings: Sequence[Mapping[str, Any]],
    *,
    log_change: float,
    targets: tuple[str, ...] = ("company-0",),
    uncertainty: float = 0.0,
    persistence: int = 1,
) -> tuple[FactorEvent, ...]:
    """Use disclosed scenario magnitudes, never infer a return from a filing form."""
    if not math.isfinite(log_change):
        raise ValueError("scenario log_change must be finite")
    return tuple(FactorEvent(
        factor_id=f"sec-{filing['accession']}", event_time=_aware_timestamp(str(filing["event_time"])),
        available_at=_aware_timestamp(str(filing["available_at"])), source=str(filing["source_url"]),
        targets=targets, channel="information", true_value={"log_change": log_change},
        observed_message=(f"SEC {filing['form']} accession {filing['accession']}; "
                          f"report date {filing['report_date']}; "
                          f"scenario log_change={log_change} configured independently of filing content."),
        uncertainty=uncertainty, persistence=persistence,
    ) for filing in filings)


def write_sec_factor_events(
    output_path: str | Path, filings: Sequence[Mapping[str, Any]], **scenario: Any,
) -> Path:
    events = sec_factor_events(filings, **scenario)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as destination:
        destination.write(_json_bytes({"events": [event.to_dict() for event in events]}).decode("utf-8"))
    return output


def parse_fred_observations(
    payload: Mapping[str, Any], *, vintage_date: date,
) -> tuple[dict[str, Any], ...]:
    vintage = vintage_date.isoformat()
    if payload.get("realtime_start") != vintage or payload.get("realtime_end") != vintage:
        raise DataSourceError("FRED response does not match the requested historical vintage")
    observations = payload["observations"]
    if int(payload.get("offset", 0)) != 0 or int(payload.get("count", len(observations))) != len(observations):
        raise DataSourceError("FRED response is incomplete; pagination is required")
    rows = []
    for observation in observations:
        start, end = str(observation["realtime_start"]), str(observation["realtime_end"])
        if not start <= vintage <= end:
            raise DataSourceError("FRED observation is unavailable in the requested vintage")
        value = None if observation["value"] == "." else float(observation["value"])
        if value is not None and not math.isfinite(value):
            raise DataSourceError("FRED observation is nonfinite")
        rows.append({"observation_date": date.fromisoformat(observation["date"]).isoformat(),
                     "value": value, "vintage_date": vintage, "realtime_start": start,
                     "realtime_end": end, "availability_precision": "date_only"})
    return tuple(rows)


def download_fred_snapshot(
    snapshot_dir: str | Path, *, series_id: str, observation_start: date,
    observation_end: date, vintage_date: date, api_key: str,
) -> Path:
    if Path(snapshot_dir).exists():
        raise FileExistsError(snapshot_dir)
    if not api_key:
        raise DataSourceError("FRED_API_KEY must be supplied externally")
    if observation_start > observation_end:
        raise ValueError("observation start must not follow end")
    parameters = {"series_id": series_id, "file_type": "json", "output_type": 1,
                  "observation_start": observation_start.isoformat(), "observation_end": observation_end.isoformat(),
                  "realtime_start": vintage_date.isoformat(), "realtime_end": vintage_date.isoformat()}
    source_url = "https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(parameters)
    raw = _fetch(source_url + "&api_key=" + urllib.parse.quote(api_key))
    if api_key.encode() in raw:
        raise DataSourceError("provider echoed credentials; response was not stored")
    rows = parse_fred_observations(_json_payload(raw), vintage_date=vintage_date)
    dates = [row["observation_date"] for row in rows]
    return write_snapshot(
        snapshot_dir, source="FRED/ALFRED", source_url=source_url,
        payloads={"observations.json": raw, "parsed_observations.json": _json_bytes(rows)},
        date_start=min(dates, default=""), date_end=max(dates, default=""), version=f"vintage-{vintage_date}",
        metadata={"docs_url": FRED_API_DOCS, "vintage_date": vintage_date.isoformat(),
                  "availability_precision": "date_only", "intraday_release_time_verified": False},
    )


def parse_alpha_vantage_daily(payload: Mapping[str, Any]) -> tuple[dict[str, Any], ...]:
    if "Time Series (Daily)" not in payload:
        raise DataSourceError("Alpha Vantage did not return daily prices")
    rows = []
    for observed_date, values in sorted(payload["Time Series (Daily)"].items()):
        row = {"date": date.fromisoformat(observed_date).isoformat()}
        for source_key, key in (("1. open", "open"), ("2. high", "high"), ("3. low", "low"),
                                ("4. close", "close"), ("5. volume", "volume")):
            value = float(values[source_key])
            if not math.isfinite(value):
                raise DataSourceError("Alpha Vantage price/volume is nonfinite")
            row[key] = value
        rows.append(row)
    return tuple(rows)


def download_alpha_vantage_snapshot(
    snapshot_dir: str | Path, *, symbol: str, api_key: str, outputsize: str = "compact",
) -> Path:
    if Path(snapshot_dir).exists():
        raise FileExistsError(snapshot_dir)
    if not api_key:
        raise DataSourceError("ALPHA_VANTAGE_API_KEY must be supplied externally")
    if outputsize not in ("compact", "full"):
        raise ValueError("outputsize must be compact or full")
    parameters = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": outputsize, "datatype": "json"}
    source_url = "https://www.alphavantage.co/query?" + urllib.parse.urlencode(parameters)
    raw = _fetch(source_url + "&apikey=" + urllib.parse.quote(api_key))
    if api_key.encode() in raw:
        raise DataSourceError("provider echoed credentials; response was not stored")
    rows = parse_alpha_vantage_daily(_json_payload(raw))
    if not rows:
        raise DataSourceError("Alpha Vantage returned no prices")
    return write_snapshot(
        snapshot_dir, source="Alpha Vantage", source_url=source_url,
        payloads={"daily.json": raw, "parsed_daily.json": _json_bytes(rows)},
        date_start=rows[0]["date"], date_end=rows[-1]["date"], version="TIME_SERIES_DAILY",
        metadata={"docs_url": ALPHA_VANTAGE_DOCS, "prices": "raw_as_traded",
                  "historical_revision_vintage": False, "outputsize": outputsize,
                  "credential_mode": "official_demo" if api_key == "demo" else "externally_supplied"},
    )


def parse_13f_holdings(
    raw: bytes | str, *, institution_id: str, period_end: date, accepted_at: datetime,
    source_url: str, value_unit: str | None,
) -> tuple[dict[str, Any], ...]:
    """Read institution-security holdings, independently of the information graph."""
    if value_unit not in ("USD", "USD_thousands"):
        raise DataSourceError("13F value unit must be verified as USD or USD_thousands")
    accepted = _aware_timestamp(accepted_at.isoformat())
    root = ET.fromstring(raw)
    rows = []
    for table in root.iter():
        if table.tag.split("}")[-1] != "infoTable":
            continue
        values = {element.tag.split("}")[-1]: (element.text or "").strip() for element in table.iter()}
        if not values.get("cusip") or not values.get("sshPrnamt") or not values.get("value"):
            raise DataSourceError("13F information table has incomplete holding fields")
        rows.append({
            "edge_type": "holding", "institution_id": institution_id,
            "security_id": "CUSIP:" + values["cusip"], "cusip": values["cusip"],
            "issuer": values.get("nameOfIssuer", ""), "title_of_class": values.get("titleOfClass", ""),
            "shares_or_principal": float(values["sshPrnamt"]), "share_type": values.get("sshPrnamtType", ""),
            "put_call": values.get("putCall"), "value_as_reported": float(values["value"]),
            "value_unit": value_unit, "period_end": period_end.isoformat(),
            "available_at": accepted.isoformat(), "source_url": source_url,
        })
    if not rows:
        raise DataSourceError("13F XML contains no information-table holdings")
    return tuple(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    sec = commands.add_parser("sec", help="SEC submissions or companyfacts raw snapshot")
    sec.add_argument("--cik", required=True)
    sec.add_argument("--kind", choices=("submissions", "companyfacts"), default="submissions")
    filing = commands.add_parser("sec-filing", help="SEC filing/index, including 13F information-table XML")
    filing.add_argument("--index-url", required=True)
    filing.add_argument("--document-url", required=True)
    filing.add_argument("--acceptance-offset", required=True, help="verified EDGAR Eastern offset, e.g. --acceptance-offset=-04:00")
    filing.add_argument("--value-unit", choices=("USD", "USD_thousands"))
    for command in (sec, filing):
        command.add_argument("--user-agent", default=os.environ.get("SEC_USER_AGENT"), required=not os.environ.get("SEC_USER_AGENT"))
    fred = commands.add_parser("fred", help="historical vintage; uses external FRED_API_KEY")
    fred.add_argument("--series-id", required=True)
    fred.add_argument("--start", type=date.fromisoformat, required=True)
    fred.add_argument("--end", type=date.fromisoformat, required=True)
    fred.add_argument("--vintage", type=date.fromisoformat, required=True)
    alpha = commands.add_parser("alpha-vantage", help="raw daily prices; uses external ALPHA_VANTAGE_API_KEY")
    alpha.add_argument("--symbol", required=True)
    alpha.add_argument("--outputsize", choices=("compact", "full"), default="compact")
    for command in (sec, filing, fred, alpha):
        command.add_argument("--snapshot-dir", type=Path, required=True)
    events = commands.add_parser("sec-events", help="export explicit scenario FactorEvents from frozen SEC metadata")
    events.add_argument("--filings", type=Path, required=True)
    events.add_argument("--output", type=Path, required=True)
    events.add_argument("--log-change", type=float, required=True)
    events.add_argument("--targets", nargs="+", default=["company-0"])
    events.add_argument("--uncertainty", type=float, default=0.0)
    events.add_argument("--persistence", type=int, default=1)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "sec":
            result = download_sec_snapshot(args.snapshot_dir, cik=args.cik, kind=args.kind, user_agent=args.user_agent)
        elif args.command == "sec-filing":
            offset = _aware_timestamp("2000-01-01T00:00:00" + args.acceptance_offset).tzinfo
            result = download_sec_filing_snapshot(args.snapshot_dir, index_url=args.index_url,
                document_url=args.document_url, acceptance_timezone=offset, user_agent=args.user_agent, value_unit=args.value_unit)
        elif args.command == "fred":
            result = download_fred_snapshot(args.snapshot_dir, series_id=args.series_id, observation_start=args.start,
                observation_end=args.end, vintage_date=args.vintage, api_key=os.environ.get("FRED_API_KEY", ""))
        elif args.command == "alpha-vantage":
            result = download_alpha_vantage_snapshot(args.snapshot_dir, symbol=args.symbol,
                outputsize=args.outputsize, api_key=os.environ.get("ALPHA_VANTAGE_API_KEY", ""))
        else:
            filings = json.loads(args.filings.read_text(encoding="utf-8"))
            result = write_sec_factor_events(args.output, filings, log_change=args.log_change,
                targets=tuple(args.targets), uncertainty=args.uncertainty, persistence=args.persistence)
    except (OSError, ValueError, KeyError, ET.ParseError) as exc:
        parser.exit(2, f"{type(exc).__name__}: {exc}\n")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
