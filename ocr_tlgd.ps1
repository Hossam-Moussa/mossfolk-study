$sp="C:\Users\LENOVO~1\AppData\Local\Temp\claude\D--Auto-Supernova\9ba10441-b608-4edd-8686-60bb9ec5e6ff\scratchpad"
$dl="$sp\dl_tlgd"
$out="$sp\books\tlgd.txt"
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Media.Ocr.OcrEngine,Windows.Foundation.UniversalApiContract,ContentType=WindowsRuntime]
$null = [Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder,Windows.Graphics,ContentType=WindowsRuntime]
Function Await($WinRtTask, $ResultType) {
  $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation``1' })[0]
  $t = $asTask.MakeGenericMethod($ResultType).Invoke($null, @($WinRtTask)); $t.Wait() | Out-Null; $t.Result
}
$eng = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$hashes = Get-Content "$dl\pages.txt"
$sb = New-Object System.Text.StringBuilder
for ($i=0; $i -lt $hashes.Count; $i++) {
  $n = $i + 1
  $webp = "$dl\pg$n.webp"; $png = "$dl\pg$n.png"
  try {
    if (-not (Test-Path $webp)) {
      Invoke-WebRequest -Uri ("https://online.fliphtml5.com/roldangorgonio/ogzu/files/large/" + $hashes[$i] + ".webp") -OutFile $webp -UseBasicParsing
      Start-Sleep -Milliseconds 150
    }
    python -I -c "from PIL import Image; im=Image.open(r'$webp').convert('RGB'); im.thumbnail((2500,2500)); im.save(r'$png')"
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($png)) ([Windows.Storage.StorageFile])
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $dec = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bmp = Await ($dec.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $res = Await ($eng.RecognizeAsync($bmp)) ([Windows.Media.Ocr.OcrResult])
    $stream.Dispose()
    $txt = ($res.Lines | ForEach-Object { $_.Text }) -join "`n"
    $null = $sb.AppendLine("===== PAGE $n ====="); $null = $sb.AppendLine($txt)
    Remove-Item $png -ErrorAction SilentlyContinue
    Write-Output "page $n ok ($($txt.Length) chars)"
  } catch {
    $null = $sb.AppendLine("===== PAGE $n ====="); $null = $sb.AppendLine("[OCR ERROR: $_]")
    Write-Output "page $n FAILED: $_"
  }
}
[System.IO.File]::WriteAllText($out, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Output ("WROTE " + $out)
