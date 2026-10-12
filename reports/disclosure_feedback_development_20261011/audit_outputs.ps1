$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$reportRoot = $PSScriptRoot
$repoRoot = Split-Path (Split-Path $reportRoot -Parent) -Parent

function FileHash([string]$path) {
    (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLower()
}

function BytesHash([byte[]]$bytes) {
    $digest = [Security.Cryptography.SHA256]::Create()
    try { -join ($digest.ComputeHash($bytes) | ForEach-Object { $_.ToString('x2') }) }
    finally { $digest.Dispose() }
}

function ReadNpy($archive, [string]$name) {
    $entry = $archive.GetEntry($name + '.npy')
    if ($null -eq $entry) { throw "Missing array: $name" }
    $reader = [IO.BinaryReader]::new($entry.Open())
    try {
        $magic = $reader.ReadBytes(6)
        if ([Text.Encoding]::ASCII.GetString($magic, 1, 5) -ne 'NUMPY') { throw "Invalid NPY: $name" }
        $major = $reader.ReadByte()
        $minor = $reader.ReadByte()
        $headerLength = if ($major -eq 1) { $reader.ReadUInt16() } else { $reader.ReadUInt32() }
        $header = [Text.Encoding]::ASCII.GetString($reader.ReadBytes($headerLength))
        if ($header -notmatch "'fortran_order': False") { throw "Unexpected NPY order: $name" }
        $dtype = [regex]::Match($header, "'descr': '([^']+)'").Groups[1].Value
        $shape = @([regex]::Match($header, "'shape': \(([^)]*)\)").Groups[1].Value.Split(',') |
            Where-Object { $_.Trim() } | ForEach-Object { [int]$_.Trim() })
        $count = 1
        foreach ($dimension in $shape) { $count *= $dimension }
        if ($dtype -eq '<f8') { $values = [double[]]::new($count); $itemSize = 8 }
        elseif ($dtype -eq '<i8') { $values = [long[]]::new($count); $itemSize = 8 }
        elseif ($dtype -eq '|b1') { $values = [byte[]]::new($count); $itemSize = 1 }
        else { throw "Unexpected dtype $dtype for $name" }
        $bytes = $reader.ReadBytes($count * $itemSize)
        if ($bytes.Length -ne $count * $itemSize) { throw "Truncated NPY: $name" }
        [Buffer]::BlockCopy($bytes, 0, $values, 0, $bytes.Length)
        [PSCustomObject]@{ values = $values; shape = $shape; dtype = $dtype; raw_sha256 = (BytesHash $bytes) }
    }
    finally { $reader.Dispose() }
}

function Stats([double[]]$values) {
    $sorted = [double[]]$values.Clone()
    [Array]::Sort($sorted)
    $sum = 0.0
    foreach ($value in $sorted) { $sum += $value }
    $output = [ordered]@{ count = $sorted.Length; mean = $sum / $sorted.Length; minimum = $sorted[0]; maximum = $sorted[-1] }
    foreach ($item in @(@('quantile_05', 0.05), @('median', 0.5), @('quantile_95', 0.95))) {
        $position = ($sorted.Length - 1) * $item[1]
        $lower = [int][Math]::Floor($position)
        $upper = [int][Math]::Ceiling($position)
        $output[$item[0]] = $sorted[$lower] + ($position - $lower) * ($sorted[$upper] - $sorted[$lower])
    }
    $output
}

$specPath = Join-Path $reportRoot 'freeze.json'
$spec = Get-Content -LiteralPath $specPath -Raw | ConvertFrom-Json
$launch = Get-Content -LiteralPath (Join-Path $reportRoot 'launch_manifest.json') -Raw | ConvertFrom-Json
$manifest = Get-Content -LiteralPath (Join-Path $reportRoot 'summary_manifest.json') -Raw | ConvertFrom-Json
$summary = Get-Content -LiteralPath (Join-Path $reportRoot 'summary.json') -Raw | ConvertFrom-Json
$checks = [ordered]@{
    freeze_hash = (FileHash $specPath) -eq $launch.contract.spec_sha256
    launcher_hash = (FileHash (Join-Path $reportRoot 'run_frozen.py')) -eq $launch.contract.launcher_sha256
    copied_source_zip_hash = (FileHash (Join-Path $reportRoot 'source.zip')) -eq $launch.contract.source_zip_sha256
    summary_hash = (FileHash (Join-Path $reportRoot 'summary.json')) -eq $manifest.summary_sha256
    report_hash = (FileHash (Join-Path $reportRoot 'report.md')) -eq $manifest.report_sha256
    original_source_zip_hash = (FileHash (Join-Path $repoRoot $spec.baseline_source.archive)) -eq $spec.baseline_source.archive_sha256
    original_manifest_hash = (FileHash (Join-Path $repoRoot $spec.baseline_source.manifest)) -eq $spec.baseline_source.manifest_sha256
}
$sourceFailures = @()
$sourceEntries = @($launch.source_hashes.PSObject.Properties)
foreach ($entry in $sourceEntries) {
    if ((FileHash (Join-Path (Join-Path $reportRoot 'isolated_src') $entry.Name)) -ne $entry.Value) { $sourceFailures += $entry.Name }
}
$checks.isolated_source_files = $sourceFailures.Count -eq 0
if (@($checks.Values | Where-Object { -not $_ }).Count) { throw 'Frozen artifact identity failed' }

$worlds = @()
$pairingInputs = @{}
foreach ($case in $spec.cases) {
    $casePath = Join-Path $reportRoot ($case.id + '.json')
    $record = Get-Content -LiteralPath $casePath -Raw | ConvertFrom-Json
    if ((FileHash $casePath) -ne $manifest.case_json_sha256.($case.id)) { throw "Case hash failed: $($case.id)" }
    if ((FileHash (Join-Path $reportRoot $record.artifact)) -ne $record.artifact_sha256) { throw "NPZ hash failed: $($case.id)" }
    if ($record.status -ne 'completed' -or $record.completed_days -ne 1800) { throw "Incomplete case: $($case.id)" }
    if (($record.config | ConvertTo-Json -Depth 20 -Compress) -ne ($case.config | ConvertTo-Json -Depth 20 -Compress)) { throw "Config changed: $($case.id)" }
    $archive = [IO.Compression.ZipFile]::OpenRead((Join-Path $reportRoot $record.artifact))
    try {
        $arrays = @{}
        foreach ($name in @('prices', 'intrinsic_values', 'price_moments', 'holder_total_moments',
                'total_cash', 'price_cap_hits_completed_prefix', 'telemetry_raw', 'telemetry_moves',
                'telemetry_news_quote', 'telemetry_permanent_flow', 'telemetry_transient_change',
                'telemetry_inventory_quote', 'telemetry_depth_fraction', 'telemetry_noise_amplification',
                'telemetry_variance_before', 'telemetry_reference_variance_before',
                'telemetry_share_error_by_asset', 'telemetry_investor_submitted', 'telemetry_noise_submitted',
                'telemetry_investor_executed', 'telemetry_noise_executed', 'telemetry_noise_common_innovation',
                'telemetry_noise_idiosyncratic_innovation', 'telemetry_deciding_count',
                'telemetry_quote_logged', 'telemetry_settlement_logged', 'telemetry_step_completed')) {
            $arrays[$name] = ReadNpy $archive $name
        }
        if (($arrays.prices.shape -join ',') -ne '1801,30' -or ($arrays.price_moments.shape -join ',') -ne '30,9') { throw 'Unexpected full path dimensions' }
        $caps = 0; $burnCaps = 0; $priceCapDayMismatch = 0
        $cashError = 0.0; $shareError = 0.0; $quoteError = 0.0; $moveError = 0.0; $flowDifference = 0.0
        $finitePositive = $true; $allFlags = $true; $priceMomentMismatch = 0; $holderMomentMismatch = 0
        $depthNearFloor = 0; $amplificationAboveOne = 0; $amplificationBelowOne = 0
        $expectedCash = [double]$arrays.total_cash.values[0]
        for ($index = 0; $index -lt $arrays.prices.values.Length; $index++) {
            $p = $arrays.prices.values[$index]
            $v = $arrays.intrinsic_values.values[$index]
            if ([double]::IsNaN($p) -or [double]::IsInfinity($p) -or $p -le 0 -or [double]::IsNaN($v) -or [double]::IsInfinity($v) -or $v -le 0) { $finitePositive = $false }
            $shareError = [Math]::Max($shareError, [Math]::Abs($arrays.telemetry_share_error_by_asset.values[$index]))
        }
        for ($day = 1; $day -le 1800; $day++) {
            $dayCaps = 0; $dividends = 0.0
            foreach ($flag in @('telemetry_quote_logged', 'telemetry_settlement_logged', 'telemetry_step_completed')) {
                if ($arrays[$flag].values[$day] -ne 1) { $allFlags = $false }
            }
            for ($asset = 0; $asset -lt 30; $asset++) {
                $index = $day * 30 + $asset
                $raw = $arrays.telemetry_raw.values[$index]
                $expectedMove = [Math]::Min(0.3, [Math]::Max(-0.3, $raw))
                if ($raw -ne $expectedMove) { $dayCaps++ }
                $reconstructed = $arrays.telemetry_news_quote.values[$index] + $arrays.telemetry_permanent_flow.values[$index] + $arrays.telemetry_transient_change.values[$index] + $arrays.telemetry_inventory_quote.values[$index]
                $quoteError = [Math]::Max($quoteError, [Math]::Abs($raw - $reconstructed))
                $moveError = [Math]::Max($moveError, [Math]::Abs($expectedMove - [Math]::Log($arrays.prices.values[$index] / $arrays.prices.values[$index - 30])))
                $submitted = $arrays.telemetry_investor_submitted.values[$index] + $arrays.telemetry_noise_submitted.values[$index]
                $executed = $arrays.telemetry_investor_executed.values[$index] + $arrays.telemetry_noise_executed.values[$index]
                $flowDifference = [Math]::Max($flowDifference, [Math]::Abs($submitted - $executed))
                $dividends += $arrays.intrinsic_values.values[$index]
                if ($arrays.telemetry_depth_fraction.values[$index] -le 0.31) { $depthNearFloor++ }
                if ($arrays.telemetry_noise_amplification.values[$index] -gt 1) { $amplificationAboveOne++ }
                if ($arrays.telemetry_noise_amplification.values[$index] -lt 1) { $amplificationBelowOne++ }
            }
            $caps += $dayCaps
            if ($day -le 600) { $burnCaps += $dayCaps }
            if ($dayCaps -ne $arrays.price_cap_hits_completed_prefix.values[$day]) { $priceCapDayMismatch++ }
            $expectedCash += $record.config.cash_flow_yield * $dividends / 252
            $cashError = [Math]::Max($cashError, [Math]::Abs($arrays.total_cash.values[$day] - $expectedCash) / [Math]::Abs($expectedCash))
        }
        for ($asset = 0; $asset -lt 30; $asset++) {
            for ($moment = 0; $moment -lt 9; $moment++) {
                if ($arrays.price_moments.values[$asset * 9 + $moment] -ne $record.price_moments_by_company[$asset][$moment]) { $priceMomentMismatch++ }
                if ($arrays.holder_total_moments.values[$asset * 9 + $moment] -ne $record.holder_total_moments_by_company[$asset][$moment]) { $holderMomentMismatch++ }
            }
        }
        if (-not $finitePositive -or -not $allFlags -or $priceCapDayMismatch -or $caps -ne $record.cap_hits_full -or $burnCaps -ne $record.cap_hits_burn_in -or $quoteError -gt 1e-12 -or $moveError -gt 1e-12 -or $cashError -gt 1e-8 -or $shareError -gt 1e-8 -or $priceMomentMismatch -or $holderMomentMismatch) { throw "Path audit failed: $($case.id)" }
        $holderKFail = @($record.holder_total_moments_by_company | Where-Object { $_[1] -le 0 }).Count
        $holderAbsFail = @($record.holder_total_moments_by_company | Where-Object { $_[3] -le 0 }).Count
        $worlds += [ordered]@{
            case = $case.id; seed = $record.seed; arm = $record.arm; status = 'PASS'
            cap_hits = $caps; burn_in_cap_hits = $burnCaps; measured_cap_hits = $caps - $burnCaps
            finite_positive_price_value_all_days = $finitePositive; all_days_quoted_settled_completed = $allFlags
            daily_cap_count_mismatches = $priceCapDayMismatch; maximum_raw_reconstruction_error = $quoteError
            maximum_log_price_move_error = $moveError; maximum_relative_cash_error = $cashError
            maximum_absolute_share_error_every_asset = $shareError; maximum_submitted_executed_net_difference = $flowDifference
            company_moment_archive_mismatches = $priceMomentMismatch + $holderMomentMismatch
            price_nonpositive_kurtosis_companies = $record.validation.stylized.failed_assets.nonpositive_excess_kurtosis.Count
            price_nonpositive_absacf1_companies = $record.validation.stylized.failed_assets.nonpositive_abs_return_acf_1.Count
            holder_nonpositive_kurtosis_companies = $holderKFail; holder_nonpositive_absacf1_companies = $holderAbsFail
            depth_at_most_031_assetday_fraction = $depthNearFloor / 54000
            noise_amplification_above_one_assetday_fraction = $amplificationAboveOne / 54000
            noise_amplification_below_one_assetday_fraction = $amplificationBelowOne / 54000
            noise_amplification_all_assetdays = (Stats $arrays.telemetry_noise_amplification.values[30..54029])
            prequote_fast_variance_all_assetdays = (Stats $arrays.telemetry_variance_before.values[30..54029])
            prequote_reference_variance_all_assetdays = (Stats $arrays.telemetry_reference_variance_before.values[30..54029])
            depth_all_assetdays = $record.depth_distribution_all_asset_days
            cross_asset_correlation_descriptive = $record.validation.cross_asset_correlation.statistics
        }
        $initialPriceBytes = [byte[]]::new(240)
        [Buffer]::BlockCopy($arrays.prices.values, 0, $initialPriceBytes, 0, 240)
        $pairingInputs[$case.id] = @{
            initial_prices = (BytesHash $initialPriceBytes)
            initialization = $record.initialization_sha256; decision_schedule = $record.decision_schedule_sha256
            intrinsic_values = $arrays.intrinsic_values.raw_sha256
            noise_common_innovation = $arrays.telemetry_noise_common_innovation.raw_sha256
            noise_idiosyncratic_innovation = $arrays.telemetry_noise_idiosyncratic_innovation.raw_sha256
            daily_deciding_count = $arrays.telemetry_deciding_count.raw_sha256
        }
    }
    finally { $archive.Dispose() }
}

$pairing = [ordered]@{}
foreach ($seed in $spec.budget.seeds) {
    $ids = @($spec.cases | Where-Object { $_.seed -eq $seed } | ForEach-Object { $_.id })
    $matches = [ordered]@{}
    foreach ($field in $pairingInputs[$ids[0]].Keys) {
        $matches[$field] = @($ids | ForEach-Object { $pairingInputs[$_][$field] } | Select-Object -Unique).Count -eq 1
    }
    if (@($matches.Values | Where-Object { -not $_ }).Count) { throw "Pairing failed: $seed" }
    $pairing["$seed"] = $matches
}
$output = [ordered]@{
    purpose = 'Archive-only independent full-path audit; zero market initializations or runs.'
    audited_utc = [DateTime]::UtcNow.ToString('o'); script_sha256 = (FileHash $PSCommandPath)
    status = 'PASS'; contract = $launch.contract; source_files_checked = $sourceEntries.Count
    identity_checks = $checks; pairing = $pairing; worlds = $worlds
    limitations = @('Saved company moments were checked against NPZ matrices, not independently re-estimated.',
        'Initialization and schedule include recorded launcher digests; full value and innovation paths were independently compared from NPZ bytes.',
        'The active workspace source is not the experiment source and is not a drift criterion.',
        'An archive audit PASS does not turn failed mechanical/stylized gates into PASS or establish empirical calibration.')
}
$output | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $reportRoot 'audit_outputs.json') -Encoding UTF8
[PSCustomObject]@{ status = 'PASS'; worlds = $worlds.Count; cap_hits = ($worlds.cap_hits | Measure-Object -Sum).Sum; source_files_checked = $sourceEntries.Count } | ConvertTo-Json
