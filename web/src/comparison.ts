import type { RunRecord, TelemetryEvent } from './api'

export interface ComparisonRun {
  run: RunRecord
  config: Record<string, unknown>
  events: TelemetryEvent[]
}

export interface ComparisonFilter {
  metric: string
  startDay: number
  endDay: number
  throughDay: number
}

export function comparisonDays(runs: ComparisonRun[], startDay: number, endDay: number): number[] {
  return [...new Set(runs.flatMap(({ events }) => events
    .filter((event) => event.sim_time >= startDay && event.sim_time <= endDay)
    .map((event) => event.sim_time)))].sort((left, right) => left - right)
}

export function comparisonRows(run: ComparisonRun, days: number[], metric: string, throughDay: number): Record<string, number>[] {
  const values = new Map(run.events.map((event) => [event.sim_time, event.payload[metric]]))
  return days.map((day) => {
    const value = values.get(day)
    return typeof value === 'number' && Number.isFinite(value) && day <= throughDay ? { day, [metric]: value } : { day }
  })
}

export function comparisonExport(runs: ComparisonRun[], filter: ComparisonFilter) {
  return {
    filter,
    runs: runs.map(({ run, config, events }) => ({
      id: run.id,
      seed: run.seed,
      fingerprint: run.fingerprint,
      config,
      observations: events.filter((event) => event.sim_time >= filter.startDay
        && event.sim_time <= filter.endDay && event.sim_time <= filter.throughDay).map((event) => {
        const value = event.payload[filter.metric]
        return { day: event.sim_time, sequence_no: event.sequence_no, value: typeof value === 'number' && Number.isFinite(value) ? value : null }
      }),
    })),
  }
}

export function comparisonCsv(runs: ComparisonRun[], filter: ComparisonFilter): string {
  const document = comparisonExport(runs, filter)
  const cells: unknown[][] = [['run_id', 'seed', 'fingerprint', 'config', 'metric', 'day', 'sequence_no', 'value']]
  for (const run of document.runs) {
    for (const observation of run.observations) {
      cells.push([run.id, run.seed, run.fingerprint, JSON.stringify(run.config), filter.metric, observation.day, observation.sequence_no, observation.value])
    }
  }
  return cells.map((row) => row.map((value) => `"${String(value ?? '').replaceAll('"', '""')}"`).join(',')).join('\r\n')
}
