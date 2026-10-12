$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$taskRaw = Join-Path $taskRoot 'data\raw\disclosure_public_20261011'
$taskSources = @(
    @{name='wba_csi_assessments_2021_2023_april2024_v2.xlsx'; url='https://www.worldbenchmarkingalliance.org/sites/default/files/2026-07/WBA-Latest-CSI-Assessments-2021-23-external-dataset-April-2024-version-2%20%281%29.xlsx'},
    @{name='wba_dataset_page.html'; url='https://www.worldbenchmarkingalliance.org/latest/core-social-indicator-assessments-2000-largest-and-most-influential-companies-globally'},
    @{name='wba_disclaimer.html'; url='https://www.worldbenchmarkingalliance.org/disclaimer'},
    @{name='sec_api_documentation.html'; url='https://www.sec.gov/search-filings/edgar-application-programming-interfaces'},
    @{name='sec_developer_faq.html'; url='https://www.sec.gov/about/webmaster-frequently-asked-questions'}
)
$taskRecords = @()
foreach ($taskSource in $taskSources) {
    $taskDestination = Join-Path $taskRaw $taskSource.name
    $taskStarted = [DateTime]::UtcNow.ToString('o')
    $taskExit = 0
    $taskTransfer = $null
    $taskReused = Test-Path -LiteralPath $taskDestination
    if (-not $taskReused) {
        $taskTransferText = & curl.exe --silent --show-error --location --fail --retry 1 --max-time 60 --user-agent 'ABM-public-data-research/1.0' --dump-header ($taskDestination + '.headers.txt') --output $taskDestination --write-out '{"url_effective":"%{url_effective}","http_code":%{http_code},"content_type":"%{content_type}","size_download":%{size_download},"time_total":%{time_total}}' $taskSource.url
        $taskExit = $LASTEXITCODE
        if ($taskTransferText) { $taskTransfer = $taskTransferText | ConvertFrom-Json }
    }
    $taskAvailable = (Test-Path -LiteralPath $taskDestination) -and $taskExit -eq 0
    $taskRecords += [ordered]@{
        name=$taskSource.name; requested_url=$taskSource.url;
        attempt_started_utc=$taskStarted; recorded_utc=[DateTime]::UtcNow.ToString('o');
        reused_local_file=$taskReused; curl_exit_code=$taskExit; transfer=$taskTransfer;
        available=$taskAvailable;
        file_write_completed_utc=$(if ($taskAvailable) { (Get-Item -LiteralPath $taskDestination).LastWriteTimeUtc.ToString('o') } else { $null });
        bytes=$(if ($taskAvailable) { (Get-Item -LiteralPath $taskDestination).Length } else { $null });
        sha256=$(if ($taskAvailable) { (Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLower() } else { $null })
    }
}
[ordered]@{
    recorded_utc=[DateTime]::UtcNow.ToString('o');
    acquisition_note='For reused files, file_write_completed_utc records the original local completion time; attempt_started_utc is only this manifest refresh. The workbook was obtained by curl from the same official URL after an Invoke-WebRequest TLS failure and HTTP 520. No login, registration, or contact message was used.';
    sources=$taskRecords
} | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $taskRaw 'source_manifest.json') -Encoding UTF8
$taskRecords | ForEach-Object { [pscustomobject]$_ } | Select-Object name,available,bytes,sha256
