# Corazón de Pulpa · Arma el video de respaldo (plan B).
#
# Une los videos de ..\videos con las tarjetas de votación en un solo MP4 con capítulos,
# siguiendo el camino ADAPTAR (final "Con pulpa").
#
# Uso: doble clic en armar-respaldo.bat
#   o: powershell -ExecutionPolicy Bypass -File armar-respaldo.ps1 [-SoloLista] [-PermitirFaltantes] [-Ffmpeg ruta\ffmpeg.exe]
#
#   -SoloLista          No arma el MP4: solo deja la lista de montaje y las tarjetas numeradas para un editor.
#   -PermitirFaltantes  Arma el MP4 aunque falten videos (se los salta). Sirve para probar.
#   -Ffmpeg             Ruta de ffmpeg.exe si no está instalado en el sistema.

param([switch]$SoloLista, [switch]$PermitirFaltantes, [string]$Ffmpeg = '')

$ErrorActionPreference = 'Stop'
$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$videos  = Join-Path (Split-Path -Parent $here) 'videos'
$cards   = Join-Path $here 'tarjetas'
$montaje = Join-Path $here 'montaje'
$temp    = Join-Path $here 'temp'
$destino = Join-Path $here 'respaldo.mp4'
$utf8    = New-Object System.Text.UTF8Encoding($false)
$utf8bom = New-Object System.Text.UTF8Encoding($true)

# ---------- Orden de la función (camino ADAPTAR) ----------
# v = video de la carpeta videos · t = tarjeta (segundos en pantalla) · cap = capítulo que empieza ahí
$ORDEN = @(
  @{v='intro.mp4'; cap='Intro'}
  @{v='prologo.mp4'; cap='Prólogo'}
  @{t='grito-frugle'; s=12}
  @{v='cap01.mp4'; cap='Capítulo 1 · El atajo'}
  @{t='d1'; s=50}
  @{v='cap01-adaptar.mp4'}
  @{t='ind-cap1'; s=10}
  @{v='cap02.mp4'; cap='Capítulo 2 · Pura cáscara'}
  @{t='ind-acto1'; s=10}
  @{v='comercial.mp4'; cap='Comercial'}
  @{v='cap03.mp4'; cap='Capítulo 3 · La Piña ha hablado'}
  @{t='d2-r'; s=20}; @{v='cap03-r.mp4'}; @{t='d2-r-resp'; s=8}
  @{t='d2-i'; s=20}; @{v='cap03-i.mp4'}; @{t='d2-i-resp'; s=8}
  @{v='cap03-fin.mp4'}
  @{t='bonus'; s=12}
  @{t='grito-pulpa'; s=12}
  @{v='cap04.mp4'; cap='Capítulo 4 · Diagnóstico con alma'}
  @{t='d3a'; s=35}; @{v='cap04-planta-adaptar.mp4'}
  @{t='d3b'; s=35}; @{v='cap04-diciembre-adaptar.mp4'}
  @{v='cap04-fin.mp4'}
  @{t='revelacion'; s=15}
  @{v='final-con-pulpa.mp4'; cap='Final · Con pulpa'}
  @{v='creditos.mp4'; cap='Créditos'}
)

function Say([string]$s, [string]$color = 'Gray'){ Write-Host $s -ForegroundColor $color }
function Find-Tool([string]$name, [string]$hint){
  if($hint -and (Test-Path $hint)){ return (Resolve-Path $hint).Path }
  $cands = @((Join-Path $here "ffmpeg\bin\$name.exe"), (Join-Path $here "$name.exe"), (Join-Path $env:LOCALAPPDATA "Microsoft\WinGet\Links\$name.exe"))
  foreach($c in $cands){ if(Test-Path $c){ return $c } }
  $wg = Get-ChildItem (Join-Path $env:LOCALAPPDATA "Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\$name.exe") -ErrorAction SilentlyContinue | Select-Object -First 1
  if($wg){ return $wg.FullName }
  $g = Get-Command $name -ErrorAction SilentlyContinue
  if($g){ return $g.Source }
  return $null
}
function Run([string]$exe, [string[]]$argv){
  & $exe @argv
  if($LASTEXITCODE -ne 0){ throw "ffmpeg falló (código $LASTEXITCODE) con: $($argv -join ' ')" }
}

Say ''
Say 'Corazón de Pulpa · Video de respaldo' 'Yellow'
Say '------------------------------------' 'Yellow'

# ---------- 1. Tarjetas ----------
$faltanTarjetas = @($ORDEN | Where-Object { $_.t -and -not (Test-Path (Join-Path $cards "$($_.t).png")) })
if($faltanTarjetas.Count -gt 0){
  Say 'Generando las tarjetas…'
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $here 'generar-tarjetas.ps1') | Out-Null
}

# ---------- 2. Videos ----------
$faltan = @($ORDEN | Where-Object { $_.v -and -not (Test-Path (Join-Path $videos $_.v)) } | ForEach-Object { $_.v })
$total = @($ORDEN | Where-Object { $_.v }).Count
Say ("Videos encontrados: {0} de {1}" -f ($total - $faltan.Count), $total) $(if($faltan.Count){ 'Yellow' } else { 'Green' })
if($faltan.Count){ $faltan | ForEach-Object { Say "  falta: videos\$_" 'DarkYellow' } }

$ff = Find-Tool 'ffmpeg' $Ffmpeg
$fp = if($ff){ Find-Tool 'ffprobe' (Join-Path (Split-Path -Parent $ff) ('ffprobe' + [IO.Path]::GetExtension($ff))) } else { $null }
function Dur([string]$file){
  if(-not $fp -or -not (Test-Path $file)){ return $null }
  $d = & $fp -v error -show_entries format=duration -of csv=p=0 $file
  if($LASTEXITCODE -ne 0 -or -not $d){ return $null }
  return [double]::Parse(($d | Select-Object -First 1).Trim(), [Globalization.CultureInfo]::InvariantCulture)
}
function MMSS($sec){ if($null -eq $sec){ return '' }; $t = [TimeSpan]::FromSeconds([Math]::Round($sec)); '{0}:{1:00}' -f [int][Math]::Floor($t.TotalMinutes), $t.Seconds }

# ---------- 3. Lista de montaje y tarjetas numeradas ----------
if(Test-Path $montaje){ Remove-Item -Recurse -Force $montaje }
New-Item -ItemType Directory -Force $montaje | Out-Null
$rows = New-Object System.Collections.Generic.List[string]
$rows.Add('Orden;Tipo;Archivo;Duración;Capítulo')
$n = 0; $capActual = ''
foreach($e in $ORDEN){
  $n++; if($e.cap){ $capActual = $e.cap }
  $num = '{0:000}' -f $n
  if($e.v){
    $file = Join-Path $videos $e.v
    $dur = if(Test-Path $file){ MMSS (Dur $file) } else { 'FALTA' }
    if(-not $dur){ $dur = '(la del video)' }
    $rows.Add("$num;Video;videos\$($e.v);$dur;$capActual")
  } else {
    $dst = "$num - tarjeta $($e.t) ($($e.s) s).png"
    Copy-Item (Join-Path $cards "$($e.t).png") (Join-Path $montaje $dst)
    $rows.Add("$num;Tarjeta;plan-b\montaje\$dst;$(MMSS $e.s);$capActual")
  }
}
$lista = Join-Path $here 'LISTA-DE-MONTAJE.csv'
[IO.File]::WriteAllLines($lista, $rows, $utf8bom)
Say "Lista de montaje: $lista" 'Green'
Say "Tarjetas numeradas: $montaje" 'Green'

if($SoloLista){ Say 'Listo (solo lista, sin armar el MP4).' 'Green'; return }

if(-not $ff){
  Say ''
  Say 'No se encontró ffmpeg en este computador, así que no se armó el MP4.' 'Yellow'
  Say 'Opción 1: instalar ffmpeg (en una terminal: winget install Gyan.FFmpeg) y volver a correr este archivo.'
  Say 'Opción 2: armar el respaldo a mano en su editor siguiendo LISTA-DE-MONTAJE.csv.'
  return
}
if($faltan.Count -and -not $PermitirFaltantes){
  Say ''
  Say 'Faltan videos, así que no se armó el MP4. Cuando estén todos, vuelvan a correrlo.' 'Yellow'
  Say '(Para una prueba con los que hay: armar-respaldo.bat -PermitirFaltantes)'
  return
}

# ---------- 4. Armar el MP4 ----------
Say ''
Say "Usando ffmpeg: $ff"
if(Test-Path $temp){ Remove-Item -Recurse -Force $temp }
New-Item -ItemType Directory -Force $temp | Out-Null
$VF  = 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=24,format=yuv420p'
$ENC = @('-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-ar','48000','-ac','2','-b:a','192k')
$concat = New-Object System.Collections.Generic.List[string]
$chapters = New-Object System.Collections.Generic.List[object]
$t0 = 0.0; $n = 0; $i = 0; $capActual = $null; $capStart = 0.0
foreach($e in $ORDEN){
  $i++
  if($e.v -and -not (Test-Path (Join-Path $videos $e.v))){ continue }
  $n++
  $seg = 'seg{0:000}.mp4' -f $n
  $out = Join-Path $temp $seg
  if($e.v){
    $in = Join-Path $videos $e.v
    Say ("[{0,2}/{1}] {2}" -f $i, $ORDEN.Count, $e.v)
    $hasAudio = $false
    if($fp){ $a = & $fp -v error -select_streams a -show_entries stream=index -of csv=p=0 $in; $hasAudio = [bool]$a }
    if($hasAudio){
      Run $ff (@('-hide_banner','-loglevel','error','-y','-i',$in,'-map','0:v:0','-map','0:a:0','-vf',$VF) + $ENC + @($out))
    } else {
      Run $ff (@('-hide_banner','-loglevel','error','-y','-i',$in,'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-map','0:v:0','-map','1:a','-vf',$VF) + $ENC + @('-shortest',$out))
    }
  } else {
    Say ("[{0,2}/{1}] tarjeta {2} ({3} s)" -f $i, $ORDEN.Count, $e.t, $e.s)
    $png = Join-Path $cards "$($e.t).png"
    Run $ff (@('-hide_banner','-loglevel','error','-y','-loop','1','-framerate','24','-t',"$($e.s)",'-i',$png,'-f','lavfi','-t',"$($e.s)",'-i','anullsrc=r=48000:cl=stereo','-vf',$VF,'-tune','stillimage') + $ENC + @('-shortest',$out))
  }
  $d = Dur $out
  if($e.cap){
    if($null -ne $capActual){ $chapters.Add(@{ title = $capActual; start = $capStart; end = $t0 }) }
    $capActual = $e.cap; $capStart = $t0
  }
  $t0 += $d
  $concat.Add("file '$seg'")
}
if($null -ne $capActual){ $chapters.Add(@{ title = $capActual; start = $capStart; end = $t0 }) }

$listFile = Join-Path $temp 'lista.txt'
[IO.File]::WriteAllLines($listFile, $concat, $utf8)
$meta = New-Object System.Collections.Generic.List[string]
$meta.Add(';FFMETADATA1')
$meta.Add('title=Corazón de Pulpa · Respaldo')
foreach($c in $chapters){
  $meta.Add('[CHAPTER]'); $meta.Add('TIMEBASE=1/1000')
  $meta.Add('START=' + [int64]($c.start * 1000)); $meta.Add('END=' + [int64]($c.end * 1000))
  $meta.Add('title=' + ($c.title -replace '([=;#\\])', '\$1'))
}
$metaFile = Join-Path $temp 'capitulos.txt'
[IO.File]::WriteAllLines($metaFile, $meta, $utf8)

Say 'Uniendo todo…'
Run $ff @('-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',$listFile,'-i',$metaFile,'-map','0','-map_metadata','1','-map_chapters','1','-c','copy','-movflags','+faststart',$destino)
Remove-Item -Recurse -Force $temp

Say ''
Say ("Listo: {0}  (duración {1}, {2} capítulos)" -f $destino, (MMSS $t0), $chapters.Count) 'Green'
Say 'Ábranlo en VLC y revisen el sonido y los capítulos (Reproducción > Capítulo).'
