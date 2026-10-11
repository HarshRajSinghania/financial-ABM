import { useQueries } from '@tanstack/react-query'
import * as echarts from 'echarts'
import { useEffect, useState } from 'react'
import { api, loadRunEvents, type RunRecord } from './api'
import { Chart } from './Chart'
import { comparisonCsv, comparisonDays, comparisonExport, comparisonRows, type ComparisonRun } from './comparison'
import { useLanguage } from './i18n'

const colors = ['#377dff', '#b477ff', '#00b880', '#f77fb3', '#08b8c8', '#ffb020']

export function ComparisonPanel({ runs }: { runs: RunRecord[] }) {
  const { t, format } = useLanguage()
  const [selectedIds, setSelectedIds] = useState<string[] | null>(null)
  const [metric, setMetric] = useState('mid_price')
  const [start, setStart] = useState('')
  const [end, setEnd] = useState('')
  const [replayIndex, setReplayIndex] = useState<number | null>(null)
  const [playing, setPlaying] = useState(false)
  const [exporting, setExporting] = useState(false)
  const [exportError, setExportError] = useState(false)
  const completed = runs.filter((run) => run.state === 'completed')
  const ids = selectedIds ?? completed.slice(0, 2).map((run) => run.id)
  const queries = useQueries({ queries: ids.map((id) => ({
    queryKey: ['comparison', id],
    staleTime: Infinity,
    queryFn: async ({ signal }: { signal: AbortSignal }): Promise<ComparisonRun> => {
      const [events, config] = await Promise.all([
        loadRunEvents(id, signal),
        api<Record<string, unknown>>(`/api/runs/${encodeURIComponent(id)}/artifacts/config`, { signal }),
      ])
      return { run: runs.find((run) => run.id === id)!, config, events }
    },
  })) })
  const data = queries.flatMap((query) => query.data ? [query.data] : [])
  const allDays = comparisonDays(data, -Infinity, Infinity)
  const startDay = start === '' ? (allDays[0] ?? 0) : Number(start)
  const endDay = end === '' ? (allDays.at(-1) ?? 0) : Number(end)
  const days = comparisonDays(data, startDay, endDay)
  const currentIndex = Math.min(replayIndex ?? days.length - 1, days.length - 1)
  const throughDay = days[currentIndex] ?? startDay
  const ready = data.length === ids.length && data.length >= 2 && days.length > 0
  const metricLabels: Record<string, string> = {
    mid_price: t('Market price', '市场价格'), fundamental_value: t('Fundamental value', '基本价值'),
    return: t('Daily return', '日收益率'), volatility_20d: t('20-day volatility', '20日波动率'),
    volume: t('Executed volume', '实际成交量'), spread: t('Bid-ask spread', '买卖价差'),
    depth: t('Quoted depth', '报价深度'), value_share: t('Value strategy share', '价值型占比'),
    trend_share: t('Trend strategy share', '趋势型占比'), noise_share: t('Noise strategy share', '噪声型占比'),
    wealth_gini: t('Wealth Gini', '财富基尼系数'),
  }
  const metrics = [...new Set(data.flatMap(({ events }) => events.flatMap((event) => Object.entries(event.payload)
    .filter(([, value]) => typeof value === 'number' && Number.isFinite(value)).map(([key]) => key))))].sort()
  if (!metrics.includes(metric)) metrics.unshift(metric)
  const fullRows = data.map((run) => comparisonRows(run, days, metric, endDay))
  const values = fullRows.flatMap((rows) => rows.flatMap((row) => Number.isFinite(row[metric]) ? [row[metric]] : []))
  let minimum = Infinity
  let maximum = -Infinity
  for (const value of values) { minimum = Math.min(minimum, value); maximum = Math.max(maximum, value) }
  const padding = values.length ? (maximum - minimum || Math.abs(maximum) || 1) * .05 : 1
  const yRange: [number, number] = values.length ? [minimum - padding, maximum + padding] : [0, 1]
  const filter = { metric, startDay, endDay, throughDay }
  const metricLabel = metricLabels[metric] ?? metric

  useEffect(() => {
    if (!playing || currentIndex >= days.length - 1) return
    const timer = setInterval(() => setReplayIndex((index) => Math.min((index ?? 0) + 1, days.length - 1)), 100)
    return () => clearInterval(timer)
  }, [playing, currentIndex, days.length])

  const resetReplay = () => { setReplayIndex(null); setPlaying(false) }
  const download = (blob: Blob, extension: string) => {
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `abm-comparison-${metric}-${startDay}-${throughDay}.${extension}`
    link.click()
    setTimeout(() => URL.revokeObjectURL(url), 1000)
  }
  const exportVisual = async (animation: boolean) => {
    setExporting(true)
    setExportError(false)
    setPlaying(false)
    const canvas = document.createElement(animation ? 'div' : 'canvas')
    const width = 1400
    const height = 100 + Math.ceil(data.length / 2) * 390
    const chart = echarts.init(canvas, undefined, { width, height, devicePixelRatio: 1, renderer: animation ? 'svg' : 'canvas' })
    try {
      const draw = (day: number) => chart.setOption({
        animation: false,
        backgroundColor: '#ffffff',
        title: [{ text: `${animation ? t('Comparison reveal animation', '对比揭示动画') : t('Experiment comparison', '实验对比')} · ${metricLabel}`, left: 30, top: 12,
          subtext: `${t('Days', '天数')} ${startDay}–${endDay} · ${t('Replay through day', '回放至')} ${day}` },
        ...data.map(({ run }, index) => ({ text: run.id, left: 35 + index % 2 * 700, top: 85 + Math.floor(index / 2) * 390,
          textStyle: { fontSize: 15 }, subtext: `${t('Seed', '种子')} ${run.seed} · ${format(run.population_size, 0)} ${t('agents', '智能体')}` }))],
        grid: data.map((_, index) => ({ left: 80 + index % 2 * 700, top: 160 + Math.floor(index / 2) * 390, width: 570, height: 240 })),
        xAxis: data.map((_, index) => ({ gridIndex: index, type: 'category' as const, data: days, boundaryGap: false,
          name: t('Simulation day', '仿真天数'), nameLocation: 'middle' as const, nameGap: 30 })),
        yAxis: data.map((_, index) => ({ gridIndex: index, type: 'value' as const, name: metricLabel, min: yRange[0], max: yRange[1],
          axisLabel: { formatter: (value: number) => format(value, 4) } })),
        series: data.map((run, index) => ({ name: run.run.id, type: 'line' as const, xAxisIndex: index, yAxisIndex: index,
          data: comparisonRows(run, days, metric, day).map((row) => row[metric] ?? null), showSymbol: false, connectNulls: false,
          lineStyle: { width: 2, color: colors[index % colors.length] } })),
      }, { notMerge: true })
      draw(throughDay)
      if (!animation) {
        const blob = await new Promise<Blob | null>((resolve) => (canvas as HTMLCanvasElement).toBlob(resolve, 'image/png'))
        if (!blob) throw new Error('Image export failed')
        download(blob, 'png')
      } else {
        const document = new DOMParser().parseFromString(chart.renderToSVGString(), 'image/svg+xml')
        const svg = document.documentElement
        const groups = [...svg.querySelectorAll('g[clip-path]')]
        if (groups.length !== data.length) throw new Error('Unexpected SVG chart structure')
        const namespace = 'http://www.w3.org/2000/svg'
        const defs = document.createElementNS(namespace, 'defs')
        svg.prepend(defs)
        groups.forEach((group, index) => {
          const clip = document.createElementNS(namespace, 'clipPath')
          clip.id = `comparison-reveal-${index}`
          const rect = document.createElementNS(namespace, 'rect')
          rect.setAttribute('x', String(80 + index % 2 * 700))
          rect.setAttribute('y', String(150 + Math.floor(index / 2) * 390))
          rect.setAttribute('width', '570')
          rect.setAttribute('height', '260')
          const reveal = document.createElementNS(namespace, 'animate')
          reveal.setAttribute('attributeName', 'width')
          reveal.setAttribute('from', '0')
          reveal.setAttribute('to', String(Math.min(570, currentIndex / Math.max(days.length - 1, 1) * 570 + 2)))
          reveal.setAttribute('dur', `${Math.min(Math.max((currentIndex + 1) / 10, 1), 30)}s`)
          reveal.setAttribute('repeatCount', 'indefinite')
          rect.append(reveal)
          clip.append(rect)
          defs.append(clip)
          const wrapper = document.createElementNS(namespace, 'g')
          wrapper.setAttribute('clip-path', `url(#${clip.id})`)
          group.parentNode!.insertBefore(wrapper, group)
          wrapper.append(group)
        })
        download(new Blob([new XMLSerializer().serializeToString(document)], { type: 'image/svg+xml' }), 'svg')
      }
    } catch {
      setExportError(true)
    } finally {
      chart.dispose()
      setExporting(false)
    }
  }

  return <section className="comparison-panel">
    <section className="panel comparison-settings">
      <header><div><h3>{t('Experiment comparison', '实验对比')}</h3><p>{t('Compare completed runs on the same day and value scales. Missing observations remain gaps.', '在统一日期与数值坐标下比较已完成实验，缺失观测保留为空白。')}</p></div></header>
      <div className="comparison-selector" role="group" aria-label={t('Experiments to compare', '选择对比实验')}>{completed.map((run) => <label key={run.id}><input type="checkbox" checked={ids.includes(run.id)} disabled={exporting} onChange={(event) => { setSelectedIds(event.target.checked ? [...ids, run.id] : ids.filter((id) => id !== run.id)); resetReplay() }} /><span>{run.id}<small>{t('Seed', '种子')} {run.seed}</small></span></label>)}</div>
      {completed.length < 2 && <p className="empty">{t('Complete at least two experiments with different seeds or configurations to compare them.', '请先完成至少两个不同种子或配置的实验。')}</p>}
      <fieldset disabled={exporting} className="comparison-filters"><div className="controls">
        <label>{t('Metric', '对比指标')}<select aria-label={t('Comparison metric', '对比指标')} value={metric} onChange={(event) => setMetric(event.target.value)}>{metrics.map((field) => <option key={field} value={field}>{metricLabels[field] ?? field}</option>)}</select></label>
        <label>{t('From day', '起始天数')}<input type="number" min="0" placeholder={String(allDays[0] ?? 0)} value={start} onChange={(event) => { setStart(event.target.value); resetReplay() }} /></label>
        <label>{t('To day', '结束天数')}<input type="number" min="0" placeholder={String(allDays.at(-1) ?? 0)} value={end} onChange={(event) => { setEnd(event.target.value); resetReplay() }} /></label>
        <button disabled={!ready || days.length < 2} onClick={() => { if (currentIndex >= days.length - 1) setReplayIndex(0); setPlaying(!playing || currentIndex >= days.length - 1) }}>{playing && currentIndex < days.length - 1 ? t('Pause replay', '暂停回放') : t('Replay comparison', '回放对比')}</button>
        <button disabled={!ready} onClick={() => void exportVisual(false)}>{t('Export PNG', '导出 PNG')}</button>
        <button disabled={!ready || days.length < 2} onClick={() => void exportVisual(true)}>{t('Export SVG animation', '导出 SVG 动画')}</button>
        <button disabled={!ready} onClick={() => download(new Blob([comparisonCsv(data, filter)], { type: 'text/csv;charset=utf-8' }), 'csv')}>{t('Filtered CSV', '筛选 CSV')}</button>
        <button disabled={!ready} onClick={() => download(new Blob([JSON.stringify(comparisonExport(data, filter), null, 2)], { type: 'application/json' }), 'json')}>{t('Filtered JSON', '筛选 JSON')}</button>
      </div>
      <label className="replay-slider">{t('Replay through day', '回放至')} {format(throughDay, 0)}<input aria-label={t('Comparison replay day', '对比回放天数')} type="range" min="0" max={Math.max(days.length - 1, 0)} value={Math.max(currentIndex, 0)} disabled={!ready} onChange={(event) => { setReplayIndex(Number(event.target.value)); setPlaying(false) }} /></label></fieldset>
      <p className="comparison-note">{t('Exports use the selected metric, day range and replay cutoff. Data includes run seeds and full configurations. SVG animation reveals the filtered curves from left to right in a repeating loop.', '导出遵循所选指标、日期范围与回放截止天数，数据包含种子与完整配置。SVG 动画循环从左往右呈现筛选后的曲线。')}</p>
      {queries.some((query) => query.isPending) && <p className="empty">{t('Loading saved experiments…', '正在加载实验记录…')}</p>}
      {queries.some((query) => query.isError) && <p className="error" role="alert">{t('Unable to load a selected experiment.', '无法加载所选实验。')}</p>}
      {ids.length < 2 && completed.length >= 2 && <p className="empty">{t('Select at least two experiments.', '请选择至少两个实验。')}</p>}
      {startDay > endDay && <p className="error" role="alert">{t('From day must not exceed to day.', '起始天数不能晚于结束天数。')}</p>}
      {data.length >= 2 && !days.length && startDay <= endDay && <p className="empty">{t('No observations in this day range.', '该日期范围没有观测。')}</p>}
      {exporting && <p role="status" className="empty">{t('Preparing export…', '正在生成导出文件…')}</p>}
      {exportError && <p className="error" role="alert">{t('Export failed. Please retry.', '导出失败，请重试。')}</p>}
    </section>
    <div className="chart-grid comparison-grid">{data.map((run, index) => <article key={run.run.id}>
      <Chart title={run.run.id} rows={comparisonRows(run, days, metric, throughDay)} yRange={yRange} yLabel={metricLabel} series={[{ name: metricLabel, field: metric, color: colors[index % colors.length] }]} />
      <div className="comparison-context"><p>{t('Seed', '种子')} {run.run.seed} · {format(run.run.population_size, 0)} {t('agents', '智能体')} · {t('Observed days', '已记录天数')} {format(run.events.filter((event) => event.sim_time >= startDay && event.sim_time <= endDay && event.sim_time <= throughDay).length, 0)}</p><details><summary>{t('Saved configuration & fingerprint', '完整配置与结果指纹')}</summary><p>{run.run.fingerprint ?? '—'}</p><pre>{JSON.stringify(run.config, null, 2)}</pre></details></div>
    </article>)}</div>
  </section>
}
