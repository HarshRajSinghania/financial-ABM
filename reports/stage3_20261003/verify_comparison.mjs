import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import path from 'node:path'
import { chromium } from 'file:///C:/Users/kanzaler/AppData/Local/npm-cache/_npx/31e32ef8478fbf80/node_modules/playwright/index.mjs'

const output = path.dirname(new URL(import.meta.url).pathname).replace(/^\/(\w:)/, '$1')
await fs.rm(path.join(output, 'comparison-browser-check.json'), { force: true })
const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const page = await browser.newPage({ viewport: { width: 1500, height: 1050 }, acceptDownloads: true })
const consoleErrors = []
page.on('pageerror', error => consoleErrors.push(error.message))
page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()) })
try {
  await page.addInitScript(() => localStorage.setItem('abm-language', 'en'))
  await page.goto('http://127.0.0.1:8783', { waitUntil: 'networkidle' })
  await page.locator('.main-nav').getByRole('button', { name: 'Analysis', exact: true }).click()
  await page.getByRole('button', { name: 'Filtered JSON', exact: true }).waitFor()
  await page.waitForFunction(() => !document.querySelector('.comparison-filters button:last-child').disabled)
  const selector = page.locator('.comparison-selector input')
  const selectable = await selector.count()
  assert.ok(selectable >= 3)
  const savedRuns = await page.evaluate(async () => {
    const headers = { Authorization: `Bearer ${sessionStorage.getItem('abm-token')}` }
    const config = await fetch('/api/configs/stage2', { headers }).then(response => response.json())
    const runs = await fetch('/api/runs', { headers }).then(response => response.json())
    return { config, runs: runs.filter(run => run.state === 'completed') }
  })
  assert.equal(savedRuns.config.stage2_enabled, true)
  const baselineRunId = savedRuns.runs.some(run => run.id === 'stage3_rules_final_20261003') ? 'stage3_rules_final_20261003' : 'stage3_rules_20261003'
  const differentSeedIndex = savedRuns.runs.findIndex(run => run.id === baselineRunId)
  assert.ok(differentSeedIndex >= 0)
  await selector.nth(differentSeedIndex).check()
  const graphOffIndex = savedRuns.runs.findIndex(run => run.id === 'stage3_graph_off_20261003')
  assert.ok(graphOffIndex >= 0)
  await selector.nth(graphOffIndex).check()
  await page.waitForFunction(() => document.querySelectorAll('.comparison-grid > article').length >= 4)
  await page.waitForFunction(() => !document.querySelector('.comparison-filters button:last-child').disabled)
  await page.getByLabel('Comparison metric', { exact: true }).selectOption('volume')
  await page.getByLabel('From day', { exact: true }).fill('10')
  await page.getByLabel('To day', { exact: true }).fill('20')
  await page.getByLabel('Comparison replay day', { exact: true }).fill('5')
  assert.equal(await page.getByLabel('Comparison replay day').inputValue(), '5')

  async function exported(label, filename) {
    const download = page.waitForEvent('download')
    await page.getByRole('button', { name: label, exact: true }).click()
    const item = await download
    const location = path.join(output, filename)
    await item.saveAs(location)
    return { filename: item.suggestedFilename(), bytes: (await fs.stat(location)).size, location }
  }
  const json = await exported('Filtered JSON', 'comparison-filtered.json')
  const document = JSON.parse(await fs.readFile(json.location, 'utf8'))
  assert.deepEqual(document.filter, { metric: 'volume', startDay: 10, endDay: 20, throughDay: 15 })
  assert.ok(document.runs.length >= 4)
  assert.equal(document.runs.find(run => run.id === 'stage3_graph_off_20261003').config.graph_enabled, false)
  assert.equal(document.runs.find(run => run.id === baselineRunId).config.graph_enabled, true)
  for (const run of document.runs) {
    assert.deepEqual(run.observations.map(observation => observation.day), [10, 11, 12, 13, 14, 15])
    assert.equal(run.config.seed, run.seed)
    assert.ok(run.fingerprint)
    const rows = await page.evaluate(async id => {
      const headers = { Authorization: `Bearer ${sessionStorage.getItem('abm-token')}` }
      return fetch(`/api/runs/${id}/events?limit=10000`, { headers }).then(response => response.json())
    }, run.id)
    for (const observation of run.observations) {
      const source = rows.find(event => event.sim_time === observation.day)
      assert.equal(observation.value, source.payload.volume)
      assert.equal(observation.sequence_no, source.sequence_no)
    }
  }
  const csv = await exported('Filtered CSV', 'comparison-filtered.csv')
  const png = await exported('Export PNG', 'comparison-export.png')
  const pngData = await fs.readFile(png.location)
  assert.equal(pngData.subarray(1, 4).toString(), 'PNG')
  assert.equal(pngData.readUInt32BE(16), 1400)
  assert.equal(pngData.readUInt32BE(20), 100 + Math.ceil(document.runs.length / 2) * 390)
  const animation = await exported('Export SVG animation', 'comparison-animation.svg')
  assert.ok(animation.bytes > 1000)
  const animatedSvg = await fs.readFile(animation.location, 'utf8')
  assert.ok(animatedSvg.includes('Comparison reveal animation'))
  assert.ok(animatedSvg.includes('Replay through day 15'))
  const preview = await browser.newPage({ viewport: { width: 1400, height: 900 } })
  await preview.setContent(animatedSvg)
  const animationFrames = await preview.evaluate(() => {
    const svg = document.querySelector('svg')
    svg.pauseAnimations()
    svg.setCurrentTime(0)
    const first = Array.from(document.querySelectorAll('[id^="comparison-reveal-"] rect')).map(rect => rect.width.animVal.value)
    svg.setCurrentTime(.999)
    const last = Array.from(document.querySelectorAll('[id^="comparison-reveal-"] rect')).map(rect => rect.width.animVal.value)
    return { first, last }
  })
  assert.equal(animationFrames.first.length, document.runs.length)
  assert.ok(animationFrames.first.every(width => width === 0))
  assert.ok(animationFrames.last.every(width => width >= 285))
  await preview.evaluate(() => document.querySelector('svg').setCurrentTime(0))
  await preview.screenshot({ path: path.join(output, 'animation-first-frame.png') })
  await preview.evaluate(() => document.querySelector('svg').setCurrentTime(.999))
  await preview.screenshot({ path: path.join(output, 'animation-last-frame.png') })
  await preview.close()
  await page.getByRole('button', { name: 'Replay comparison', exact: true }).click()
  await page.waitForFunction(() => Number(document.querySelector('.comparison-filters input[type=range]').value) > 5)
  const replayAdvanced = await page.getByLabel('Comparison replay day').inputValue()
  await page.getByLabel('Comparison replay day').fill('5')
  await page.locator('.comparison-panel').screenshot({ path: path.join(output, 'comparison-en.png') })
  await page.getByRole('button', { name: '中文', exact: true }).click()
  assert.equal(await page.getByRole('heading', { name: '实验对比', exact: true }).count(), 1)
  await page.locator('.comparison-panel').screenshot({ path: path.join(output, 'comparison-zh.png') })
  await page.setViewportSize({ width: 390, height: 844 })
  const overflow = await page.evaluate(() => ({ viewport: innerWidth, page: document.documentElement.scrollWidth }))
  assert.ok(overflow.page <= overflow.viewport, JSON.stringify(overflow))
  await page.screenshot({ path: path.join(output, 'comparison-mobile.png'), fullPage: true })
  await page.getByLabel('起始天数', { exact: true }).fill('30')
  assert.equal(await page.getByRole('alert').filter({ hasText: '起始天数不能晚于结束天数' }).count(), 1)
  assert.equal(await page.getByRole('button', { name: '筛选 JSON', exact: true }).isDisabled(), true)
  assert.deepEqual(consoleErrors, [])
  await fs.writeFile(path.join(output, 'comparison-browser-check.json'), JSON.stringify({
    passed: true, config_endpoint: 'stage2 round-trip passed', compared_runs: document.runs.map(run => ({ id: run.id, seed: run.seed, graph_enabled: run.config.graph_enabled })),
    filter: document.filter, exports: { json, csv, png, animation }, animationFrames, replayAdvanced, mobile: overflow, consoleErrors,
  }, null, 2))
  console.log(JSON.stringify({ passed: true, runs: document.runs.length, filter: document.filter, exports: { json: json.bytes, csv: csv.bytes, png: png.bytes, animation: animation.bytes }, mobile: overflow, consoleErrors }))
} finally {
  await browser.close()
}
