# Bulk caption fetcher — EN subs only, polite sleeps, archive so reruns skip done ids
$dir = Split-Path $MyInvocation.MyCommand.Path
$deno = "C:\Users\Lenovo Thinkpad\AppData\Local\Microsoft\WinGet\Packages\DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe\deno.exe"
$queue = Get-Content "$dir\download_queue.txt" | Where-Object { $_ -and -not $_.StartsWith('#') }
foreach ($url in $queue) {
  yt-dlp --js-runtimes "deno:$deno" --skip-download --write-auto-subs --write-subs `
    --sub-langs "en" --sub-format "vtt" `
    --sleep-requests 1.5 --sleep-subtitles 3 `
    --download-archive "$dir\archive.txt" `
    --ignore-errors --no-warnings `
    -o "$dir\%(id)s.%(ext)s" $url 2>&1 |
    ForEach-Object { if ($_ -match 'Writing video subtitles|ERROR|429') { Add-Content "$dir\fetch_log.txt" "$(Get-Date -Format HH:mm:ss) $_" } }
  Start-Sleep -Seconds 5
}
Add-Content "$dir\fetch_log.txt" "$(Get-Date -Format HH:mm:ss) QUEUE COMPLETE"
