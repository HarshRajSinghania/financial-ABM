$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$reportRoot = $PSScriptRoot
$summary = Get-Content -LiteralPath (Join-Path $reportRoot 'summary.json') -Raw | ConvertFrom-Json
$audit = Get-Content -LiteralPath (Join-Path $reportRoot 'audit_outputs.json') -Raw | ConvertFrom-Json
if ($audit.status -ne 'PASS' -or $summary.completed_worlds -ne 12) { throw 'Expected the audited fixed twelve-world archive' }

function ReadDoubleArray($archive, [string]$name) {
    $reader = [IO.BinaryReader]::new($archive.GetEntry($name + '.npy').Open())
    try {
        $prefix = $reader.ReadBytes(8)
        $headerLength = if ($prefix[6] -eq 1) { $reader.ReadUInt16() } else { $reader.ReadUInt32() }
        $header = [Text.Encoding]::ASCII.GetString($reader.ReadBytes($headerLength))
        if ($header -notmatch "'descr': '<f8'" -or $header -notmatch "'shape': \(1801, 30\)" -or $header -notmatch "'fortran_order': False") { throw "Unexpected array: $name" }
        $bytes = $reader.ReadBytes(1801 * 30 * 8)
        if ($bytes.Length -ne 1801 * 30 * 8) { throw "Truncated array: $name" }
        $values = [double[]]::new(1801 * 30)
        [Buffer]::BlockCopy($bytes, 0, $values, 0, $bytes.Length)
        ,$values
    }
    finally { $reader.Dispose() }
}

function ContrastStats([double[]]$values) {
    $stats = $values | Measure-Object -Average -Minimum -Maximum
    [ordered]@{ count = $values.Length; mean = $stats.Average; minimum = $stats.Minimum; maximum = $stats.Maximum
        negative_count = @($values | Where-Object { $_ -lt 0 }).Count
        zero_count = @($values | Where-Object { $_ -eq 0 }).Count
        positive_count = @($values | Where-Object { $_ -gt 0 }).Count }
}

$contrasts = [ordered]@{}
$armDiagnostics = [ordered]@{}
foreach ($arm in $summary.arms.PSObject.Properties.Name) {
    $rows = @($summary.records | Where-Object { $_.arm -eq $arm })
    $audits = @($audit.worlds | Where-Object { $_.arm -eq $arm })
    $armDiagnostics[$arm] = [ordered]@{
        worlds = $rows.Count; completed = @($rows | Where-Object { $_.status -eq 'completed' }).Count
        mechanical_pass_worlds = @($rows | Where-Object { $_.validation.mechanical.status -eq 'PASS' }).Count
        price_stylized_pass_worlds = @($rows | Where-Object { $_.validation.stylized.status -eq 'PASS' }).Count
        holder_stylized_pass_worlds = @($rows | Where-Object { $_.holder_total_stylized.status -eq 'PASS' }).Count
        caps = ($rows.cap_hits_full | Measure-Object -Sum).Sum
        burn_caps = ($rows.cap_hits_burn_in | Measure-Object -Sum).Sum
        measured_caps = ($rows.cap_hits_measurement | Measure-Object -Sum).Sum
        nonpositive_kurtosis_company_worlds = ($audits.price_nonpositive_kurtosis_companies | Measure-Object -Sum).Sum
        nonpositive_absacf1_company_worlds = ($audits.price_nonpositive_absacf1_companies | Measure-Object -Sum).Sum
        maximum_absolute_raw_quote = ($rows.maximum_absolute_raw_quote | Measure-Object -Maximum).Maximum
        mean_depth = ($audits.depth_all_assetdays.mean | Measure-Object -Average).Average
        depth_at_most_031_assetday_fraction = ($audits.depth_at_most_031_assetday_fraction | Measure-Object -Average).Average
        noise_amplification_below_one_assetday_fraction = ($audits.noise_amplification_below_one_assetday_fraction | Measure-Object -Average).Average
        noise_amplification_above_one_assetday_fraction = ($audits.noise_amplification_above_one_assetday_fraction | Measure-Object -Average).Average
        maximum_noise_amplification = ($audits.noise_amplification_all_assetdays.maximum | Measure-Object -Maximum).Maximum
        mean_fast_variance = ($audits.prequote_fast_variance_all_assetdays.mean | Measure-Object -Average).Average
        mean_reference_variance = ($audits.prequote_reference_variance_all_assetdays.mean | Measure-Object -Average).Average
        mean_cross_asset_correlation = ($audits.cross_asset_correlation_descriptive.mean | Measure-Object -Average).Average
        holder_volatility_change_percent = 100 * ($summary.arms.$arm.holder_total_mean_moments[0] / $summary.arms.current.holder_total_mean_moments[0] - 1)
        holder_kurtosis_change_percent = 100 * ($summary.arms.$arm.holder_total_mean_moments[1] / $summary.arms.current.holder_total_mean_moments[1] - 1)
        holder_absacf1_change_percent = 100 * ($summary.arms.$arm.holder_total_mean_moments[3] / $summary.arms.current.holder_total_mean_moments[3] - 1)
    }
    if ($arm -eq 'current') { continue }
    $contrasts[$arm] = [ordered]@{}
    foreach ($definition in @('price', 'holder_total')) {
        $key = $definition + '_moments_by_company'
        $moments = [ordered]@{}
        for ($moment = 0; $moment -lt 9; $moment++) {
            $differences = @(foreach ($row in $rows) {
                $baseline = $summary.records | Where-Object { $_.seed -eq $row.seed -and $_.arm -eq 'current' }
                for ($company = 0; $company -lt 30; $company++) { $row.$key[$company][$moment] - $baseline.$key[$company][$moment] }
            })
            $moments[$summary.moment_names[$moment]] = ContrastStats $differences
        }
        $contrasts[$arm][$definition] = $moments
    }
}

$interaction = [ordered]@{}
foreach ($definition in @('price', 'holder_total')) {
    $key = $definition + '_moments_by_company'
    $interaction[$definition] = [ordered]@{}
    for ($moment = 0; $moment -lt 9; $moment++) {
        $differences = @(foreach ($seed in @('27001', '27304', '27305')) {
            $rows = @{}
            foreach ($row in @($summary.records | Where-Object { $_.seed -eq $seed })) { $rows[$row.arm] = $row }
            for ($company = 0; $company -lt 30; $company++) {
                $rows.neither_volatility_feedback.$key[$company][$moment] - $rows.no_noise_volatility_feedback.$key[$company][$moment] - $rows.no_depth_volatility_feedback.$key[$company][$moment] + $rows.current.$key[$company][$moment]
            }
        })
        $interaction[$definition][$summary.moment_names[$moment]] = ContrastStats $differences
    }
}

$capEvents = @()
foreach ($row in @($summary.records | Where-Object { $_.cap_hits_full -gt 0 })) {
    $archive = [IO.Compression.ZipFile]::OpenRead((Join-Path $reportRoot $row.artifact))
    try {
        $arrays = @{}
        foreach ($name in @('raw', 'news_quote', 'permanent_flow', 'transient_change', 'inventory_quote',
                'depth_fraction', 'noise_amplification', 'investor_submitted', 'noise_submitted', 'investor_executed', 'noise_executed')) {
            $arrays[$name] = ReadDoubleArray $archive ('telemetry_' + $name)
        }
        for ($index = 30; $index -lt 54030; $index++) {
            if ([Math]::Abs($arrays.raw[$index]) -le 0.3) { continue }
            $submitted = $arrays.investor_submitted[$index] + $arrays.noise_submitted[$index]
            $executed = $arrays.investor_executed[$index] + $arrays.noise_executed[$index]
            $capEvents += [ordered]@{
                case = $row.case; day = [int][Math]::Floor($index / 30); asset = $index % 30
                raw = $arrays.raw[$index]; news = $arrays.news_quote[$index]; permanent = $arrays.permanent_flow[$index]
                transient_change = $arrays.transient_change[$index]; inventory = $arrays.inventory_quote[$index]
                depth = $arrays.depth_fraction[$index]; noise_amplification = $arrays.noise_amplification[$index]
                investor_submitted = $arrays.investor_submitted[$index]; noise_submitted = $arrays.noise_submitted[$index]
                investor_executed = $arrays.investor_executed[$index]; noise_executed = $arrays.noise_executed[$index]
                submitted_executed_net_difference = $submitted - $executed
            }
        }
    }
    finally { $archive.Dispose() }
}
if ($capEvents.Count -ne 10) { throw 'Cap event count differs from the full-path audit' }
$output = [ordered]@{
    purpose = 'Archive-only interpretation; zero new market runs, no selection or threshold changes.'
    script_sha256 = (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLower()
    contract = $summary.contract; summary_sha256 = (Get-FileHash -LiteralPath (Join-Path $reportRoot 'summary.json') -Algorithm SHA256).Hash.ToLower()
    audit_sha256 = (Get-FileHash -LiteralPath (Join-Path $reportRoot 'audit_outputs.json') -Algorithm SHA256).Hash.ToLower()
    arm_diagnostics = $armDiagnostics; paired_company_moment_changes = $contrasts
    factorial_interaction_neither_minus_nonoise_minus_nodepth_plus_current = $interaction
    cap_events = $capEvents; automatic_winner = $null
    limits = @('The 90 company-world contrasts within an arm are correlated observations nested in only three already-seen seeds; no inferential confidence interval or holdout claim.',
        'Factorial contrasts include all endogenous path responses; individual quote terms are accounting decompositions, not separately identified path effects.',
        'Exponent zero removes both high-volatility amplification and low-volatility suppression; sensitivity zero fixes depth at its initial value of one.',
        'Bare results do not address disclosure cash-flow costs or the separate nine large corporate-cost/news cap cases.',
        'All original gates and failed worlds remain unchanged; empirical, return-ACF and cross-correlation acceptance remain pending.')
}
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $reportRoot 'interpretation.json') -Encoding UTF8
[PSCustomObject]@{ worlds = 12; cap_events = $capEvents.Count; market_runs = 0; output = 'interpretation.json' } | ConvertTo-Json
