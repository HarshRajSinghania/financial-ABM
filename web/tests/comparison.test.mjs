import assert from 'node:assert/strict'
import { test } from 'node:test'
import { comparisonCsv, comparisonDays, comparisonExport, comparisonRows } from '../src/comparison.ts'

const event = (day, payload) => ({ sim_time: day, sequence_no: day + 10, payload })
const run = (id, seed, events) => ({ run: { id, seed, fingerprint: `${id}-hash` }, config: { seed, graph_enabled: false }, events })
const first = run('seed-1', 1, [event(3, { mid_price: 103, volume: 20 }), event(1, { mid_price: 101 })])
const second = run('policy-2', 2, [event(2, { mid_price: 202 }), event(3, { volume: 30 }), event(4, { mid_price: 204 })])

test('comparison aligns inclusive actual simulation days across sparse runs', () => {
  assert.deepEqual(comparisonDays([first, second], 2, 3), [2, 3])
  assert.deepEqual(comparisonDays([first, second], 4, 2), [])
  assert.deepEqual(comparisonDays([first, second], 10, 20), [])
})

test('missing observations and future replay days remain gaps', () => {
  assert.deepEqual(comparisonRows(first, [1, 2, 3], 'mid_price', 2), [
    { day: 1, mid_price: 101 }, { day: 2 }, { day: 3 },
  ])
  assert.deepEqual(comparisonRows(second, [2, 3, 4], 'mid_price', 4), [
    { day: 2, mid_price: 202 }, { day: 3 }, { day: 4, mid_price: 204 },
  ])
})

test('filtered JSON keeps exact configuration and only the metric, date range and replay cutoff', () => {
  const filter = { metric: 'mid_price', startDay: 2, endDay: 4, throughDay: 3 }
  const document = comparisonExport([first, second], filter)
  assert.deepEqual(document.filter, filter)
  assert.deepEqual(document.runs[0], {
    id: 'seed-1', seed: 1, fingerprint: 'seed-1-hash', config: { seed: 1, graph_enabled: false },
    observations: [{ day: 3, sequence_no: 13, value: 103 }],
  })
  assert.deepEqual(document.runs[1].observations, [
    { day: 2, sequence_no: 12, value: 202 }, { day: 3, sequence_no: 13, value: null },
  ])
})

test('nonfinite observations export as missing and never become zero', () => {
  const sample = run('missing', 4, [event(1, { mid_price: NaN }), event(2, { mid_price: Infinity }), event(3, { mid_price: 0 })])
  assert.deepEqual(comparisonRows(sample, [1, 2, 3], 'mid_price', 3), [{ day: 1 }, { day: 2 }, { day: 3, mid_price: 0 }])
  assert.deepEqual(comparisonExport([sample], { metric: 'mid_price', startDay: 1, endDay: 3, throughDay: 3 }).runs[0].observations.map(row => row.value), [null, null, 0])
})

test('CSV preserves configuration escaping and uses the same filters as JSON', () => {
  const sample = run('policy', 7, [event(1, { volume: 10 }), event(2, { volume: 20 })])
  sample.config.label = 'Policy, "A"\nChange'
  const csv = comparisonCsv([sample], { metric: 'volume', startDay: 1, endDay: 2, throughDay: 1 })
  assert.equal(csv.split('\r\n').length, 2)
  assert.ok(csv.includes('"policy","7","policy-hash"'))
  assert.ok(csv.includes('Policy, \\""A\\""\\nChange'))
  assert.ok(csv.endsWith('"volume","1","11","10"'))
})
