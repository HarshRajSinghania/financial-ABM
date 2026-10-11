"""Public-source provenance, acceptance clocks, and credential-safe adapter tests."""

import hashlib
import json
import urllib.error
from datetime import UTC, date, datetime, timedelta, timezone

import pytest

from abm import data_sources
from abm.data_sources import (
    DataSourceError,
    download_alpha_vantage_snapshot,
    download_fred_snapshot,
    download_sec_filing_snapshot,
    download_sec_snapshot,
    parse_13f_holdings,
    parse_fred_observations,
    parse_sec_companyfacts,
    parse_sec_filing_index,
    parse_sec_submissions,
    sec_factor_events,
    write_sec_factor_events,
    write_snapshot,
)
from abm.schemas import FactorEvent

SEC_DIRECTORY = "https://www.sec.gov/Archives/edgar/data/1384905/000138490524000043/"
INDEX_URL = SEC_DIRECTORY + "0001384905-24-000043-index.html"
DOCUMENT_URL = SEC_DIRECTORY + "rng-20240801.htm"
INDEX_HTML = b"""<html><h1>Form 8-K - Current report:</h1>
<p>SEC <b>Accession</b> No. <span>0001384905-24-000043</span></p>
<div>Filing Date</div><div>2024-08-01</div>
<div>Accepted</div><div>2024-08-01 16:33:57</div>
<div>Period of Report</div><div>2024-06-30</div></html>"""


def _submissions():
    return {"cik": 1384905, "filings": {"recent": {
        "accessionNumber": ["0001384905-24-000043", "0001384905-24-000044"],
        "form": ["8-K", "10-Q"], "filingDate": ["2024-08-01", "2024-08-02"],
        "reportDate": ["2024-06-30", "2024-06-30"],
        "acceptanceDateTime": ["2024-08-01T20:33:57.000Z", "2024-08-02T20:00:00.000Z"],
        "primaryDocument": ["rng-20240801.htm", "rng-20240630.htm"],
    }, "files": [{"name": "CIK0001384905-submissions-001.json"}]}}


def _fred(vintage="2024-07-15"):
    return {"realtime_start": vintage, "realtime_end": vintage, "count": 2, "offset": 0,
            "observations": [
                {"date": "2024-06-01", "value": "100.5", "realtime_start": vintage, "realtime_end": vintage},
                {"date": "2024-07-01", "value": ".", "realtime_start": vintage, "realtime_end": vintage},
            ]}


def _alpha():
    return {"Time Series (Daily)": {"2024-07-15": {
        "1. open": "100", "2. high": "102", "3. low": "99", "4. close": "101", "5. volume": "10"}}}


def test_snapshot_records_hashes_time_range_and_rejects_overwrite(tmp_path):
    destination = tmp_path / "snapshot"
    raw = b"actual public response"
    write_snapshot(destination, source="fixture", source_url=INDEX_URL,
                   payloads={"raw.html": raw}, date_start="2024-08-01", date_end="2024-08-02", version="v1")
    manifest = json.loads((destination / "manifest.json").read_text())
    assert manifest["source_url"] == INDEX_URL
    assert manifest["files"]["raw.html"] == {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    assert datetime.fromisoformat(manifest["retrieved_at"]).utcoffset() == timedelta(0)
    assert (manifest["date_start"], manifest["date_end"], manifest["version"]) == ("2024-08-01", "2024-08-02", "v1")
    with pytest.raises(FileExistsError):
        write_snapshot(destination, source="changed", source_url=INDEX_URL,
                       payloads={"raw.html": b"replacement"}, date_start="", date_end="", version="v2")
    assert (destination / "raw.html").read_bytes() == raw
    for name in ("../outside", "", ".", "..", "manifest.json", "Manifest.JSON"):
        with pytest.raises(ValueError):
            write_snapshot(tmp_path / "invalid", source="fixture", source_url=INDEX_URL,
                           payloads={name: raw}, date_start="", date_end="", version="v1")


def test_sec_acceptance_is_separate_from_reporting_period_and_preserves_raw_clock():
    filings = parse_sec_submissions(_submissions())
    first = filings[0]
    assert first["report_date"] == "2024-06-30"
    assert first["available_at"] == "2024-08-01T20:33:57+00:00"
    assert first["acceptance_raw"] == "2024-08-01T20:33:57.000Z"
    assert first["time_basis"] == "submissions_acceptanceDateTime_as_supplied"
    assert first["source_url"] == DOCUMENT_URL
    payload = _submissions()
    payload["filings"]["recent"]["acceptanceDateTime"][0] = "2024-08-01T16:33:57"
    with pytest.raises(DataSourceError, match="UTC offset"):
        parse_sec_submissions(payload)


def test_sec_companyfacts_joins_accession_availability_without_collapsing_revisions():
    payload = {"facts": {"us-gaap": {"Revenue": {"units": {"USD": [
        {"accn": "0001384905-24-000043", "end": "2024-06-30", "val": 100, "filed": "2024-08-01"},
        {"accn": "0001384905-24-000044", "end": "2024-06-30", "val": 101, "filed": "2024-08-02"},
        {"accn": "unmatched", "end": "2024-06-30", "val": 999, "filed": "2024-08-01"},
    ]}}}}}
    filings = parse_sec_submissions(_submissions())
    all_rows = parse_sec_companyfacts(payload, filings=filings)
    assert [row["value"] for row in all_rows] == [100, 101, 999]
    assert all_rows[-1]["available_at"] is None
    before = datetime(2024, 8, 1, 20, 0, tzinfo=UTC)
    assert parse_sec_companyfacts(payload, filings=filings, as_of=before) == ()
    after = datetime(2024, 8, 1, 21, 0, tzinfo=UTC)
    assert [row["value"] for row in parse_sec_companyfacts(payload, filings=filings, as_of=after)] == [100]


def test_sec_index_uses_verified_offset_and_event_magnitude_is_explicit(tmp_path):
    filing = parse_sec_filing_index(INDEX_HTML, source_url=INDEX_URL,
                                   acceptance_timezone=timezone(timedelta(hours=-4)))
    accepted = datetime(2024, 8, 1, 20, 33, 57, tzinfo=UTC)
    assert datetime.fromisoformat(filing["available_at"]) == accepted
    event = sec_factor_events([filing], log_change=-0.017)[0]
    assert event.true_value == {"log_change": -0.017}
    assert event.event_time == event.available_at == accepted
    assert event.channel == "information" and event.targets == ("company-0",)
    assert "configured independently" in event.observed_message
    assert event.source == INDEX_URL
    output = write_sec_factor_events(tmp_path / "events.json", [filing], log_change=-0.017)
    exported = json.loads(output.read_text())["events"][0]
    assert FactorEvent.from_dict(exported) == event
    with pytest.raises(FileExistsError):
        write_sec_factor_events(output, [filing], log_change=0.1)
    with pytest.raises(ValueError, match="finite"):
        sec_factor_events([filing], log_change=float("nan"))


def test_sec_filing_snapshot_preserves_index_and_original_document_bytes(tmp_path, monkeypatch):
    body = b"<html>SEC original filing fixture</html>"
    monkeypatch.setattr(data_sources, "_fetch", lambda url, **kwargs: INDEX_HTML if url == INDEX_URL else body)
    destination = download_sec_filing_snapshot(tmp_path / "snapshot", index_url=INDEX_URL,
        document_url=DOCUMENT_URL, acceptance_timezone=timezone(timedelta(hours=-4)), user_agent="fixture researcher")
    assert (destination / "filing_index.html").read_bytes() == INDEX_HTML
    assert (destination / "filing_document.htm").read_bytes() == body
    metadata = json.loads((destination / "manifest.json").read_text())["metadata"]
    assert metadata["payload_representation"] == "original_HTTP_response_bytes"
    assert metadata["report_date"] == "2024-06-30"
    assert metadata["acceptance_timezone_offset"] == "-04:00"
    with pytest.raises(ValueError, match="same filing"):
        download_sec_filing_snapshot(tmp_path / "bad", index_url=INDEX_URL,
            document_url=DOCUMENT_URL.replace("000138490524000043", "000138490524000044"),
            acceptance_timezone=UTC, user_agent="fixture researcher")


def test_sec_snapshot_keeps_original_response_and_historical_page_inventory(tmp_path, monkeypatch):
    raw = json.dumps(_submissions()).encode()
    monkeypatch.setattr(data_sources, "_fetch", lambda *args, **kwargs: raw)
    destination = download_sec_snapshot(tmp_path / "snapshot", cik=1384905, user_agent="fixture researcher")
    assert (destination / "submissions.json").read_bytes() == raw
    manifest = json.loads((destination / "manifest.json").read_text())
    assert manifest["metadata"]["additional_submission_files"] == _submissions()["filings"]["files"]
    assert manifest["metadata"]["historical_api_vintage"] is False


def test_fred_historical_vintage_is_verified_and_missing_values_remain_missing():
    rows = parse_fred_observations(_fred(), vintage_date=date(2024, 7, 15))
    assert rows[0]["observation_date"] == "2024-06-01"
    assert rows[0]["vintage_date"] == "2024-07-15"
    assert rows[0]["availability_precision"] == "date_only"
    assert rows[1]["value"] is None
    with pytest.raises(DataSourceError, match="historical vintage"):
        parse_fred_observations(_fred("2026-10-03"), vintage_date=date(2024, 7, 15))
    payload = _fred()
    payload["count"] = 100001
    with pytest.raises(DataSourceError, match="incomplete"):
        parse_fred_observations(payload, vintage_date=date(2024, 7, 15))


def test_fred_request_specifies_vintage_and_excludes_key_from_manifest(tmp_path, monkeypatch):
    secret = "externally-supplied-test-key"
    requested = []
    def fetch(url, **kwargs):
        requested.append(url)
        return json.dumps(_fred()).encode()
    monkeypatch.setattr(data_sources, "_fetch", fetch)
    destination = download_fred_snapshot(tmp_path / "snapshot", series_id="TEST", observation_start=date(2024, 6, 1),
        observation_end=date(2024, 7, 1), vintage_date=date(2024, 7, 15), api_key=secret)
    assert "realtime_start=2024-07-15" in requested[0] and "realtime_end=2024-07-15" in requested[0]
    assert all(secret.encode() not in path.read_bytes() for path in destination.iterdir())


def test_alpha_keys_are_external_and_error_or_echoed_responses_are_not_saved(tmp_path, monkeypatch):
    with pytest.raises(DataSourceError, match="externally"):
        download_alpha_vantage_snapshot(tmp_path / "missing", symbol="IBM", api_key="")
    secret = "external-test-key"
    monkeypatch.setattr(data_sources, "_fetch", lambda *args, **kwargs: json.dumps({"Information": "API quota exceeded"}).encode())
    with pytest.raises(DataSourceError, match="quota"):
        download_alpha_vantage_snapshot(tmp_path / "quota", symbol="IBM", api_key=secret)
    assert not (tmp_path / "quota").exists()
    payload = _alpha()
    payload["echoed"] = secret
    monkeypatch.setattr(data_sources, "_fetch", lambda *args, **kwargs: json.dumps(payload).encode())
    with pytest.raises(DataSourceError, match="echoed"):
        download_alpha_vantage_snapshot(tmp_path / "echo", symbol="IBM", api_key=secret)
    assert not (tmp_path / "echo").exists()
    monkeypatch.setattr(data_sources, "_fetch", lambda *args, **kwargs: json.dumps(_alpha()).encode())
    destination = download_alpha_vantage_snapshot(tmp_path / "success", symbol="IBM", api_key=secret)
    assert all(secret.encode() not in path.read_bytes() for path in destination.iterdir())
    assert json.loads((destination / "manifest.json").read_text())["metadata"]["prices"] == "raw_as_traded"
    demo = download_alpha_vantage_snapshot(tmp_path / "demo", symbol="IBM", api_key="demo")
    assert json.loads((demo / "manifest.json").read_text())["metadata"]["credential_mode"] == "official_demo"


def test_http_error_does_not_reveal_request_credentials_or_leave_partial_snapshot(tmp_path, monkeypatch):
    secret = "must-not-appear-in-errors"
    def fail(request, **kwargs):
        raise urllib.error.HTTPError(request.full_url, 429, "quota " + secret, {}, None)
    monkeypatch.setattr(data_sources.urllib.request, "urlopen", fail)
    with pytest.raises(DataSourceError, match="HTTP 429") as error:
        download_alpha_vantage_snapshot(tmp_path / "blocked", symbol="IBM", api_key=secret)
    assert secret not in str(error.value)
    assert not (tmp_path / "blocked").exists()


def test_13f_is_a_holding_edge_with_verified_value_unit_and_lagged_public_availability():
    raw = """<informationTable xmlns="http://www.sec.gov/edgar/document/thirteenf/informationtable">
<infoTable><nameOfIssuer>Example Corp</nameOfIssuer><titleOfClass>COMMON</titleOfClass>
<cusip>123456789</cusip><value>25000</value><shrsOrPrnAmt><sshPrnamt>100</sshPrnamt>
<sshPrnamtType>SH</sshPrnamtType></shrsOrPrnAmt><putCall>CALL</putCall></infoTable></informationTable>"""
    accepted = datetime(2024, 8, 14, 20, 0, tzinfo=UTC)
    rows = parse_13f_holdings(raw, institution_id="manager-1", period_end=date(2024, 6, 30),
                            accepted_at=accepted, source_url=DOCUMENT_URL, value_unit="USD")
    assert rows[0]["edge_type"] == "holding"
    assert rows[0]["security_id"] == "CUSIP:123456789"
    assert rows[0]["period_end"] == "2024-06-30"
    assert rows[0]["available_at"] == "2024-08-14T20:00:00+00:00"
    assert rows[0]["value_unit"] == "USD" and rows[0]["value_as_reported"] == 25000
    assert rows[0]["put_call"] == "CALL"
    assert not {"trust", "delay_days", "source_id", "target_id"}.intersection(rows[0])
    with pytest.raises(DataSourceError, match="unit"):
        parse_13f_holdings(raw, institution_id="manager-1", period_end=date(2024, 6, 30),
                          accepted_at=accepted, source_url=DOCUMENT_URL, value_unit=None)
