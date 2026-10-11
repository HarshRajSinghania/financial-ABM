"""Snapshot-backed information factors on an explicit daily session calendar."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from dataclasses import dataclass, fields, replace
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Protocol

import numpy as np

from .information import InformationGraph
from .manifest import canonical_json_bytes
from .schemas import Edge, FactorEvent, Message
from .stage2 import Stage2Config, Stage2Harness, Stage2Policy, Stage2Result
from .telemetry import TelemetrySink


class FactorPlugin(Protocol):
    def events(self, date: datetime, state: Mapping[str, Any]) -> list[FactorEvent]: ...


class SnapshotInformationPlugin:
    plugin_id = "snapshot_information_v1"

    def __init__(self, path: str | Path):
        self.snapshot_bytes = Path(path).read_bytes()
        payload = json.loads(self.snapshot_bytes)
        self.records = tuple(sorted(
            (FactorEvent.from_dict(value) for value in payload["events"]),
            key=lambda event: (event.available_at, event.factor_id),
        ))
        if len({event.factor_id for event in self.records}) != len(self.records):
            raise ValueError("factor event IDs must be unique")
        for event in self.records:
            if any(at.utcoffset() is None for at in (event.event_time, event.available_at)):
                raise ValueError("factor event timestamps must be timezone-aware")
            if event.channel != "information":
                raise ValueError("the snapshot plugin currently supports only the information channel")
            if not isinstance(event.true_value, dict) or "log_change" not in event.true_value:
                raise ValueError("information factors require a disclosed scenario log_change")
            value = event.true_value["log_change"]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not np.isfinite(value):
                raise ValueError("disclosed scenario log_change must be finite")
        self.next_record = 0

    def events(self, date: datetime, state: Mapping[str, Any]) -> list[FactorEvent]:
        start = self.next_record
        while self.next_record < len(self.records) and self.records[self.next_record].available_at <= date:
            self.next_record += 1
        return deepcopy(list(self.records[start:self.next_record]))


@dataclass(frozen=True, slots=True)
class Stage3Config(Stage2Config):
    stage3_enabled: bool = True
    rules_enabled: bool = True
    factors_enabled: bool = True
    factor_events_path: str = ""
    start_date: str = "2026-01-05"
    session_cutoff: str = "21:00:00+00:00"
    session_dates: tuple[str, ...] = ()
    factor_data_files: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.stage3_enabled and not self.stage2_enabled:
            for name in ("bandit_enabled", "company_learning_enabled", "graph_enabled", "dynamic_graph_enabled"):
                object.__setattr__(self, name, False)
        Stage2Config.__post_init__(self)
        date.fromisoformat(self.start_date)
        cutoff = time.fromisoformat(self.session_cutoff)
        if cutoff.utcoffset() is None:
            raise ValueError("session_cutoff must include a UTC offset")
        if self.session_dates:
            sessions = tuple(datetime.fromisoformat(value) for value in self.session_dates)
            if len(sessions) != self.trading_days or any(at.utcoffset() is None for at in sessions):
                raise ValueError("session_dates must contain one timezone-aware cutoff per trading day")
            if any(right <= left or right.date() <= left.date()
                   for left, right in zip(sessions, sessions[1:])):
                raise ValueError("session_dates must be strictly ordered daily cutoffs")
        if self.stage3_enabled and self.factors_enabled and not self.factor_events_path:
            raise ValueError("enabled factors require factor_events_path")
        if self.stage3_enabled and self.learning_enabled:
            raise ValueError("Stage 3 requires the Stage 1 Logit switch to be off")

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "Stage3Config":
        values = dict(payload)
        for name in ("session_dates", "factor_data_files"):
            if name in values:
                if not isinstance(values[name], (list, tuple)) or any(not isinstance(value, str) for value in values[name]):
                    raise TypeError(f"{name} must be an array of strings")
                values[name] = tuple(values[name])
        return super(Stage3Config, cls).from_dict(values)

    def stage2_config(self) -> Stage2Config:
        return Stage2Config(**{field.name: getattr(self, field.name) for field in fields(Stage2Config)})


class Stage3Policy(Stage2Policy):
    def act(self, observation, population, rng):
        orders = super().act(observation, population, rng)
        if not self.harness.config.rules_enabled:
            orders = np.zeros_like(orders)
            self.submitted_orders = orders.copy()
        return orders


@dataclass(frozen=True, slots=True)
class Stage3Result(Stage2Result):
    stage3_audit: dict[str, Any]
    source_snapshots: dict[str, bytes]
    data_snapshots: dict[str, bytes]
    original_paths: dict[str, str]

    def fingerprint(self) -> str:
        digest = hashlib.sha256(Stage2Result.fingerprint(self).encode("ascii"))
        digest.update(canonical_json_bytes(self.stage3_audit))
        return digest.hexdigest()

    def summary(self) -> dict[str, Any]:
        summary = Stage2Result.summary(self)
        summary.update(stage=3, factor_events=self.stage3_audit["emitted_events"],
                       pending_factor_events=self.stage3_audit["pending_events"],
                       calendar=self.stage3_audit["calendar"])
        return summary

    def write(self, output_dir, config, *, code_revision="working-tree") -> Path:
        destination = Stage2Result.write(self, output_dir, config, code_revision=code_revision)
        (destination / "stage3_audit.json").write_text(
            json.dumps(self.stage3_audit, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8",
        )
        archive = {"data_files": {}, "source_files": {}, "original_paths": self.original_paths}
        for category, snapshots, directory in (("source_files", self.source_snapshots, "source"),
                                                ("data_files", self.data_snapshots, "inputs")):
            (destination / directory).mkdir()
            for index, (logical, content) in enumerate(sorted(snapshots.items())):
                basename = logical.removeprefix("source:") if category == "source_files" else Path(self.original_paths[logical]).name
                relative = f"{directory}/{index:03d}_{basename}"
                (destination / relative).write_bytes(content)
                archive[category][logical] = relative
        (destination / "reproducibility.json").write_text(
            json.dumps(archive, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8",
        )
        return destination


class Stage3Harness(Stage2Harness):
    def __init__(self, config: Stage3Config, telemetry_sink: TelemetrySink | None = None,
                 *, event_log: str | Path | None = None, code_revision: str = "working-tree",
                 data_file_overrides: Mapping[str, str | Path] | None = None):
        self.data_file_overrides = dict(data_file_overrides or {})
        if config.session_dates:
            self.sessions = tuple(datetime.fromisoformat(value) for value in config.session_dates)
        else:
            current, cutoff = date.fromisoformat(config.start_date), time.fromisoformat(config.session_cutoff)
            sessions = []
            while len(sessions) < config.trading_days:
                if current.weekday() < 5:
                    sessions.append(datetime.combine(current, cutoff))
                current += timedelta(days=1)
            self.sessions = tuple(sessions)
        self.plugin = SnapshotInformationPlugin(self._input_path(config.factor_events_path)) if config.factors_enabled else None
        self.factor_records: list[dict[str, Any]] = []
        self.current_factors: list[dict[str, Any]] = []
        super().__init__(config, telemetry_sink, code_revision=code_revision)
        self.policy = Stage3Policy(self)
        self.manifest = replace(self.manifest, started_at=datetime.now(timezone.utc))
        self.original_paths = {}
        if config.graph_fixture:
            self.original_paths["graph_fixture"] = config.graph_fixture
        if config.factors_enabled:
            self.original_paths["factor_events"] = config.factor_events_path
            self.original_paths.update({f"factor_data:{i}": path for i, path in enumerate(config.factor_data_files)})
        self.source_snapshots, self.data_snapshots = {}, {}
        for logical, path in self._manifest_data_files().items():
            if logical == "factor_events":
                content = self.plugin.snapshot_bytes
            elif logical == "graph_fixture":
                content = self.graph_fixture_bytes
            else:
                content = path.read_bytes()
            if hashlib.sha256(content).hexdigest() != self.manifest.data_sha256[logical]:
                raise ValueError(f"input changed while preparing the run: {logical}")
            target = self.source_snapshots if logical.startswith("source:") else self.data_snapshots
            target[logical] = content
        if self.plugin is not None and any(target not in self.company_ids for event in self.plugin.records for target in event.targets):
            raise ValueError("information factor targets must be configured company IDs")
        if event_log is not None:
            self.event_log = Path(event_log)
            self.event_log.parent.mkdir(parents=True, exist_ok=True)
            with self.event_log.open("x", encoding="utf-8"):
                pass

    def _input_path(self, path: str | Path) -> Path:
        return Path(self.data_file_overrides.get(str(path), path))

    def _manifest_data_files(self) -> dict[str, Path]:
        sources = super()._manifest_data_files()
        if self.config.factors_enabled:
            sources["factor_events"] = self._input_path(self.config.factor_events_path)
            sources.update({f"factor_data:{i}": self._input_path(path)
                            for i, path in enumerate(self.config.factor_data_files)})
        return sources

    def _enabled_plugins(self) -> tuple[str, ...]:
        return (self.plugin.plugin_id,) if self.plugin is not None else ()

    def _simulation_time(self, day_index: int) -> datetime:
        return self.sessions[day_index]

    def _build_graph(self) -> InformationGraph:
        if self.config.graph_fixture:
            self.graph_fixture_bytes = self._input_path(self.config.graph_fixture).read_bytes()
            fixture = json.loads(self.graph_fixture_bytes)
            nodes = self.company_ids + self.trader_ids
            if set(fixture["nodes"]) != set(nodes):
                raise ValueError("graph fixture nodes must match the company and trader population")
            return InformationGraph(tuple(fixture["nodes"]), tuple(Edge.from_dict(edge) for edge in fixture["edges"]))
        graph = super()._build_graph()
        return InformationGraph(graph.nodes, tuple(replace(edge, valid_from=self.sessions[0].date()) for edge in graph.edges))

    def _additional_messages(self, day: int, now: datetime) -> list[Message]:
        state = MappingProxyType({"day": day, "company_ids": self.company_ids, "trader_ids": self.trader_ids})
        events = self.plugin.events(now, state) if self.plugin is not None else []
        self.current_factors = [{**event.to_dict(), "session_available_at": now.isoformat()} for event in events]
        self.factor_records.extend(self.current_factors)
        messages = []
        for event in events:
            for target in event.targets:
                messages.append(Message(
                    f"factor:{event.factor_id}:{target}", target, ("public",), event.event_time, now,
                    "factor_information", {"log_change": float(event.true_value["log_change"]),
                                           "factor_id": event.factor_id, "source": event.source,
                                           "source_available_at": event.available_at.isoformat(),
                                           "observed_message": event.observed_message}, 1 - event.uncertainty,
                ))
        return messages

    def _frame_extra(self, day: int, now: datetime) -> dict[str, Any]:
        return {"session_cutoff": now.isoformat(), "factor_events": self.current_factors}

    def run(self) -> Stage3Result:
        result = super().run()
        self.manifest = replace(self.manifest, ended_at=datetime.now(timezone.utc))
        audit = {"calendar": "explicit_sessions" if self.config.session_dates else "synthetic_weekdays_fixed_offset",
                 "session_cutoffs": [at.isoformat() for at in self.sessions],
                 "emitted_events": len(self.factor_records),
                 "pending_events": len(self.plugin.records) - self.plugin.next_record if self.plugin is not None else 0,
                 "events": self.factor_records, "information_magnitude": "disclosed_scenario_log_change",
                 "rules_enabled": self.config.rules_enabled}
        return Stage3Result(**{field.name: getattr(result, field.name) for field in fields(Stage2Result)
                              if field.name != "stage2_manifest"}, stage2_manifest=self.manifest,
                            stage3_audit=audit, source_snapshots=self.source_snapshots,
                            data_snapshots=self.data_snapshots, original_paths=self.original_paths)
