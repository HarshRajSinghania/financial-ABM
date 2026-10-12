$ErrorActionPreference = 'Stop'
$capPath = Join-Path $PSScriptRoot 'cap_diagnostic.json'
$replayPath = Join-Path $PSScriptRoot 'feedback_replay.json'
$cap = Get-Content -LiteralPath $capPath -Raw | ConvertFrom-Json
$replay = Get-Content -LiteralPath $replayPath -Raw | ConvertFrom-Json
$rootPath = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$manifestPath = Join-Path $rootPath 'reports/disclosure_action_grid_development_20261011_v1/training/seed_27001/manifest.json'
$cfg = (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).config
$p = $cfg.permanent_impact_fraction
$rows = @(foreach ($world in $replay.cases) {
    if ($world.status -ne 'PASS' -or -not $world.original_archives_unchanged) { throw 'Replay failed' }
    $actualHash = (Get-FileHash -LiteralPath (Join-Path $PSScriptRoot $world.telemetry.name)).Hash.ToLower()
    if ($actualHash -ne $world.telemetry.sha256) { throw 'Telemetry hash mismatch' }
    foreach ($e in $world.caps) {
        $coef = $cfg.price_impact / $cfg.liquidity_fraction * ($p + (1 - $p) / $e.depth_fraction)
        $i = $coef * $e.investor_submitted
        $n = $coef * $e.noise_submitted
        $m = ($cfg.transient_impact_decay - 1) * $e.transient_before - (1 - $p) * $e.expected_flow_before
        $unit = $e.raw - (1 - $p) * $cfg.price_impact / $cfg.liquidity_fraction * $e.submitted_net * (1 / $e.depth_fraction - 1)
        [ordered]@{
            seed=$world.seed; rule=$world.rule; day=$e.day; asset_zero_based=$e.asset_zero_based
            raw=$e.raw; news=$e.news; investor_current=$i; noise_current=$n; prior_memory=$m
            inventory=$e.inventory_skew; depth=$e.depth_fraction; noise_amplification=$e.noise_amplification
            raw_reconstruction_error=[Math]::Abs($e.raw - ($e.news + $i + $n + $m + $e.inventory_skew))
            submitted_executed_net_difference=[Math]::Abs($e.submitted_net - $e.executed_net)
            raw_unit_depth_static=$unit; raw_zero_noise_static=$e.raw - $n
            raw_zero_investor_static=$e.raw - $i
        }
    }
})
$maxError = ($rows | Measure-Object -Property raw_reconstruction_error -Maximum).Maximum
if ($rows.Count -ne 28 -or $maxError -gt 1e-12) { throw 'Unexpected decomposition result' }
$costRows = @($cap.hits | Where-Object { $_.quote.signed_news_toward_cap -ge $_.quote.cap_limit } | ForEach-Object {
    [ordered]@{seed=$_.seed; day=$_.day; asset_zero_based=$_.firm_index_zero_based
        semantic_action=$_.prior_decision.semantic_action; amount_sd=$_.prior_decision.amount_sd
        news_toward_down_cap=$_.quote.signed_news_toward_cap
        commitment_news_toward_down_cap=$_.quote.signed_commitment_news_toward_cap
        cost_over_precommitment_value=$_.accounting.resource_cost / ($_.accounting.intrinsic_value - $_.accounting.financing_adjustment + $_.accounting.resource_cost + $_.accounting.fine - $_.accounting.subsidy)
    }
})
$output = [ordered]@{
    scope='Read-only arithmetic on archived cap JSON and root replay JSON; no market initialization or run'
    script_sha256=(Get-FileHash -LiteralPath $PSCommandPath).Hash.ToLower()
    cap_diagnostic_sha256=(Get-FileHash -LiteralPath $capPath).Hash.ToLower()
    replay_sha256=(Get-FileHash -LiteralPath $replayPath).Hash.ToLower()
    original_manifest_sha256=(Get-FileHash -LiteralPath $manifestPath).Hash.ToLower()
    verified_telemetry_hashes=7
    formula='raw = news + (p+(1-p)/depth)*(price_impact/liquidity_fraction)*netshares + (decay-1)*Tprev - (1-p)*Eprev + inventory'
    events=$rows.Count; maximum_reconstruction_error=$maxError
    unit_depth_static_caps=@($rows | Where-Object { [Math]::Abs($_.raw_unit_depth_static) -gt $cfg.max_log_return }).Count
    zero_noise_static_caps=@($rows | Where-Object { [Math]::Abs($_.raw_zero_noise_static) -gt $cfg.max_log_return }).Count
    zero_investor_static_caps=@($rows | Where-Object { [Math]::Abs($_.raw_zero_investor_static) -gt $cfg.max_log_return }).Count
    maximum_absolute_unit_depth_static_raw=($rows | ForEach-Object { [Math]::Abs($_.raw_unit_depth_static) } | Measure-Object -Maximum).Maximum
    static_rows=$rows; cost_news_cap_examples=$costRows
    limits=@('The 28 cap records contain ten distinct seed-day-asset keys selected after failures.',
        'Static substitutions freeze original state and orders; they are not path counterfactuals or modified-market acceptance.',
        'Removing observed noise flow is not the same operation as setting the volatility exponent to zero.',
        'Root recorded bitwise replay assertions; this review verifies saved telemetry hashes and algebra only.',
        'The replay subset does not include the nine large-expenditure news cases.')
}
$json = $output | ConvertTo-Json -Depth 8
[IO.File]::WriteAllText((Join-Path $PSScriptRoot 'cap_followup_checks.json'), $json + [Environment]::NewLine, [Text.UTF8Encoding]::new($false))
Write-Output "PASS: 28 algebra checks; static unit-depth caps=$($output.unit_depth_static_caps); static zero-noise caps=$($output.zero_noise_static_caps)"
