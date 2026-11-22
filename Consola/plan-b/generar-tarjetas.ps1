# Corazón de Pulpa · Genera las tarjetas (1920x1080 PNG) del video de respaldo.
# Uso: clic derecho > Ejecutar con PowerShell, o:
#   powershell -ExecutionPolicy Bypass -File generar-tarjetas.ps1
# Solo hace falta volver a correrlo si cambian algún texto de las tarjetas.

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$out  = Join-Path $here 'tarjetas'
New-Item -ItemType Directory -Force $out | Out-Null

$W = 1920; $H = 1080
$col = @{
  bg='#1A1410'; bg2='#2C2018'; gold='#C9A24D'; gold2='#E8C877'; cream='#F5EFE3'; muted='#B8AC98'; track='#3A2E24'
  verde1='#86B133'; verde2='#4A6315'; roja1='#F2545F'; roja2='#A51E29'; verde='#6B8E23'; roja='#E63946'
  clima='#3D9BE9'; cultura='#FF9F1C'; vrio='#9B6BFF'; criterio='#E8B04A'; up='#9BE08A'; down='#FF8A92'
}
function C([string]$hex){ [System.Drawing.ColorTranslator]::FromHtml($hex) }
function F([string]$fam, [double]$size, [string]$style = 'Regular'){
  New-Object System.Drawing.Font($fam, [single]$size, [System.Drawing.FontStyle]$style, [System.Drawing.GraphicsUnit]::Pixel)
}
$SERIF = 'Georgia'; $SANS = 'Segoe UI'
$NOTA_RESPALDO = 'Versión de respaldo · sigue el camino ADAPTAR con todas las respuestas correctas'

function New-Card {
  $bmp = New-Object System.Drawing.Bitmap($W, $H)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAlias
  $g.Clear((C $col.bg))
  $path = New-Object System.Drawing.Drawing2D.GraphicsPath
  $path.AddEllipse(-500, -1000, $W + 1000, 2000)
  $pgb = New-Object System.Drawing.Drawing2D.PathGradientBrush($path)
  $pgb.CenterPoint = New-Object System.Drawing.PointF(($W / 2), 0)
  $pgb.CenterColor = C $col.bg2
  $pgb.SurroundColors = [System.Drawing.Color[]]@((C $col.bg))
  $g.FillPath($pgb, $path)
  $pgb.Dispose(); $path.Dispose()
  return @{ bmp = $bmp; g = $g }
}
function Save-Card($card, [string]$name){
  $file = Join-Path $out ($name + '.png')
  $card.bmp.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)
  $card.g.Dispose(); $card.bmp.Dispose()
  Write-Host "  $name.png"
}
function T($g, [string]$s, $font, [string]$hex, [double]$x, [double]$y, [double]$w, [double]$h, [string]$align = 'Center', [string]$valign = 'Near'){
  $sf = New-Object System.Drawing.StringFormat
  $sf.Alignment = [System.Drawing.StringAlignment]$align
  $sf.LineAlignment = [System.Drawing.StringAlignment]$valign
  $br = New-Object System.Drawing.SolidBrush((C $hex))
  $g.DrawString($s, $font, $br, (New-Object System.Drawing.RectangleF([single]$x, [single]$y, [single]$w, [single]$h)), $sf)
  $br.Dispose(); $sf.Dispose(); $font.Dispose()
}
function RR([double]$x, [double]$y, [double]$w, [double]$h, [double]$r){
  $r = [Math]::Min($r, [Math]::Min($w / 2, $h / 2)); $d = 2 * $r
  $p = New-Object System.Drawing.Drawing2D.GraphicsPath
  $p.AddArc([single]$x, [single]$y, [single]$d, [single]$d, 180, 90)
  $p.AddArc([single]($x + $w - $d), [single]$y, [single]$d, [single]$d, 270, 90)
  $p.AddArc([single]($x + $w - $d), [single]($y + $h - $d), [single]$d, [single]$d, 0, 90)
  $p.AddArc([single]$x, [single]($y + $h - $d), [single]$d, [single]$d, 90, 90)
  $p.CloseFigure()
  return $p
}
function Fill($g, $path, [string]$hex){ $b = New-Object System.Drawing.SolidBrush((C $hex)); $g.FillPath($b, $path); $b.Dispose(); $path.Dispose() }
function FillGrad($g, $path, [double]$x, [double]$y, [double]$w, [double]$h, [string]$c1, [string]$c2){
  $rect = New-Object System.Drawing.RectangleF([single]$x, [single]$y, [single]$w, [single]$h)
  $b = New-Object System.Drawing.Drawing2D.LinearGradientBrush($rect, (C $c1), (C $c2), [single]60)
  $g.FillPath($b, $path); $b.Dispose(); $path.Dispose()
}
function Sign([int]$n){ if($n -gt 0){ "+$n" } elseif($n -lt 0){ [string][char]0x2212 + [Math]::Abs($n) } else { [string][char]0x00B1 + '0' } }

# ---------- Tipos de tarjeta ----------

function Card-Vote([string]$name, [string]$kicker, [string]$question, [string]$note, $left, $right, [int]$secs){
  $c = New-Card; $g = $c.g
  T $g $kicker.ToUpper() (F $SANS 30 'Bold') $col.gold 96 64 1728 50 'Near'
  $qs = 70
  while($qs -gt 40){
    $qf = F $SERIF $qs 'Bold, Italic'
    $hgt = $g.MeasureString($question, $qf, 1728).Height; $qf.Dispose()
    if($hgt -le 205){ break }
    $qs -= 4
  }
  T $g $question (F $SERIF $qs 'Bold, Italic') $col.cream 96 112 1728 210 'Near'
  T $g $note (F $SANS 28) $col.muted 96 330 1728 44 'Near'
  $py = 400; $ph = 540; $pw = 800
  foreach($side in @(@{o = $left; x = 96; c1 = $col.verde1; c2 = $col.verde2; tag = 'TARJETA VERDE'},
                     @{o = $right; x = (1920 - 96 - $pw); c1 = $col.roja1; c2 = $col.roja2; tag = 'TARJETA ROJA'})){
    FillGrad $g (RR $side.x $py $pw $ph 36) $side.x $py $pw $ph $side.c1 $side.c2
    T $g $side.tag (F $SANS 24 'Bold') '#FFFFFF' ($side.x + 40) ($py + 32) ($pw - 80) 40 'Near'
    T $g $side.o.label (F $SANS 104 'Bold') '#FFFFFF' $side.x ($py + 120) $pw 150
    T $g $side.o.desc (F $SANS 38) '#FFFFFF' ($side.x + 60) ($py + 290) ($pw - 120) 220
  }
  $cx = 960; $cy = $py + $ph / 2; $r = 104
  $b = New-Object System.Drawing.SolidBrush((C $col.bg)); $g.FillEllipse($b, [single]($cx - $r - 14), [single]($cy - $r - 14), [single](2 * $r + 28), [single](2 * $r + 28)); $b.Dispose()
  $pen = New-Object System.Drawing.Pen((C $col.gold2), [single]10); $g.DrawEllipse($pen, [single]($cx - $r), [single]($cy - $r), [single](2 * $r), [single](2 * $r)); $pen.Dispose()
  T $g "$secs" (F $SANS 78 'Bold') $col.cream ($cx - $r) ($cy - 70) (2 * $r) 100
  T $g 'segundos' (F $SANS 24 'Bold') $col.muted ($cx - $r) ($cy + 30) (2 * $r) 40
  T $g 'Tarjetas arriba · Si necesitan más tiempo, pausen el video' (F $SANS 28) $col.muted 0 972 1920 44
  Save-Card $c $name
}

function Card-Answer([string]$name, [string]$kicker, $opt, [string]$cls, [string]$explain, [string]$effect){
  $c = New-Card; $g = $c.g
  T $g $kicker.ToUpper() (F $SANS 30 'Bold') $col.gold 0 170 1920 50
  T $g 'La respuesta correcta es' (F $SERIF 62 'Bold, Italic') $col.cream 0 250 1920 90
  $pw = 760; $px = (1920 - $pw) / 2
  Fill $g (RR $px 380 $pw 170 30) $(if($cls -eq 'verde'){ $col.verde } else { $col.roja })
  T $g $opt (F $SANS 96 'Bold') '#FFFFFF' $px 380 $pw 170 'Center' 'Center'
  T $g $explain (F $SANS 46) $col.cream 260 610 1400 200
  T $g "Si el salón acertó: $effect" (F $SANS 38 'Bold') $col.gold2 0 840 1920 60
  T $g $NOTA_RESPALDO (F $SANS 22) '#8C806E' 0 1010 1920 36
  Save-Card $c $name
}

function Draw-Bars($g, $vals, $deltas, [double]$y0, [int]$mark = 0){
  $rows = @(@{k = 'clima'; l = 'Clima laboral'}, @{k = 'cultura'; l = 'Cultura / Alma'}, @{k = 'vrio'; l = 'Ventaja VRIO'})
  $tx = 600; $tw = 860; $th = 44; $i = 0
  foreach($r in $rows){
    $y = $y0 + $i * 120; $v = [int]$vals[$r.k]
    T $g $r.l (F $SANS 42 'Bold') $col.cream 200 ($y - 6) 380 60 'Near'
    Fill $g (RR $tx $y $tw $th 22) $col.track
    if($v -gt 0){ Fill $g (RR $tx $y ($tw * $v / 100) $th 22) $col[$r.k] }
    if($mark){ $b = New-Object System.Drawing.SolidBrush((C $col.cream)); $g.FillRectangle($b, [single]($tx + $tw * $mark / 100 - 2), [single]($y - 8), [single]4, [single]($th + 16)); $b.Dispose() }
    T $g "$v" (F $SANS 66 'Bold') $col.cream ($tx + $tw + 20) ($y - 22) 150 90 'Far'
    if($deltas){
      $d = [int]$deltas[$r.k]
      T $g (Sign $d) (F $SANS 40 'Bold') $(if($d -gt 0){ $col.up } elseif($d -lt 0){ $col.down } else { $col.muted }) ($tx + $tw + 190) ($y - 4) 160 60 'Near'
    }
    $i++
  }
}

function Card-Indicators([string]$name, [string]$title, $vals, $deltas, [int]$crit){
  $c = New-Card; $g = $c.g
  T $g 'INDICADORES DE FRUTITECH' (F $SANS 30 'Bold') $col.gold 0 110 1920 50
  T $g $title (F $SERIF 92 'Bold, Italic') $col.cream 0 160 1920 130
  T $g 'Continuará…' (F $SERIF 50 'Italic') $col.gold2 0 290 1920 70
  Draw-Bars $g $vals $deltas 440
  T $g "Criterio del salón: $crit de 20 posibles" (F $SANS 38 'Bold') $col.criterio 0 820 1920 60
  T $g $NOTA_RESPALDO (F $SANS 22) '#8C806E' 0 1010 1920 36
  Save-Card $c $name
}

function Card-Bonus([string]$name, $vals, [int]$crit, [int]$bonus){
  $c = New-Card; $g = $c.g
  T $g 'ACTO 2 · EL SALÓN TOMA EL MANDO' (F $SANS 30 'Bold') $col.gold 0 100 1920 50
  T $g 'Capital de confianza' (F $SERIF 92 'Bold, Italic') $col.cream 0 150 1920 130
  T $g "Don Harold no los escuchó, pero cada acierto contó: $crit puntos de criterio se convierten en +$bonus para cada indicador." (F $SANS 40) $col.cream 260 300 1400 130
  Draw-Bars $g $vals @{ clima = $bonus; cultura = $bonus; vrio = $bonus } 500
  T $g $NOTA_RESPALDO (F $SANS 22) '#8C806E' 0 1010 1920 36
  Save-Card $c $name
}

function Card-Reveal([string]$name, $vals){
  $c = New-Card; $g = $c.g
  $avg = [Math]::Round(($vals.clima + $vals.cultura + $vals.vrio) / 3)
  T $g '21 DE DICIEMBRE · INDICADORES FINALES' (F $SANS 30 'Bold') $col.gold 0 90 1920 50
  T $g 'Las decisiones de este salón tienen resultados' (F $SERIF 78 'Bold, Italic') $col.cream 160 140 1600 220
  Draw-Bars $g $vals $null 420 55
  T $g "Promedio $avg  ·  se necesita 55 o más" (F $SANS 44 'Bold') $col.muted 0 780 1920 70
  T $g 'Final: Con pulpa' (F $SERIF 110 'Bold, Italic') $col.gold2 0 860 1920 150
  T $g $NOTA_RESPALDO (F $SANS 22) '#8C806E' 0 1020 1920 36
  Save-Card $c $name
}

function Card-Grito([string]$name, [string]$kicker, [string]$who, [string]$call, [string]$resp){
  $c = New-Card; $g = $c.g
  T $g $kicker.ToUpper() (F $SANS 30 'Bold') $col.gold 0 150 1920 50
  T $g $who (F $SANS 40) $col.muted 0 260 1920 60
  T $g $call (F $SERIF 96 'Bold, Italic') $col.cream 0 330 1920 140
  T $g 'El salón responde:' (F $SANS 40) $col.muted 0 560 1920 60
  T $g $resp (F $SERIF 104 'Bold, Italic') $col.gold2 40 640 1840 260
  Save-Card $c $name
}

# ---------- Contenido (el mismo de la consola) ----------

function DA([string]$dup, [string]$adapt){ @(@{ label = 'DUPLICAR'; desc = $dup }, @{ label = 'ADAPTAR'; desc = $adapt }) }
$SN = @(@{ label = 'SÍ'; desc = 'Tarjeta verde' }, @{ label = 'NO'; desc = 'Tarjeta roja' })
$A1 = 'Acto 1 · El salón opina. Don Harold decide.'
$A2 = 'Acto 2 · El salón tiene el mando: lo que decida, se ejecuta.'

Write-Host 'Generando tarjetas en' $out

Card-Grito 'grito-frugle' 'Ensayo del grito' 'Cuando Don Harold diga:' '¡Así lo hace Frugle!' '¡Pero nosotros no somos Frugle!'

$o = DA 'Enviarla hoy, tal cual llegó.' 'Frenar y hacer primero un diagnóstico.'
Card-Vote 'd1' 'Decisión 1' '¿Qué debe hacer Don Harold con la política 3x2?' $A1 $o[0] $o[1] 45
Card-Indicators 'ind-cap1' 'Fin del capítulo 1' @{clima = 76; cultura = 78; vrio = 60} @{clima = -6; cultura = -7; vrio = -10} 10
Card-Indicators 'ind-acto1' 'Fin del Acto 1' @{clima = 45; cultura = 50; vrio = 42} @{clima = -31; cultura = -28; vrio = -18} 10

$vrio = @(
  @{ l = 'r'; q = 'El 3x2 de Frugle, ¿es RARO?'; ok = 1; ex = 'Lo tiene medio mundo. Valioso pero común: eso es empate, no ventaja.' },
  @{ l = 'i'; q = 'La novena con los buñuelos de Don Lulo, ¿es DIFÍCIL DE IMITAR?'; ok = 0; ex = 'Veinte años de historia no se descargan de internet. Eso es pulpa.' }
)
$i = 0
foreach($k in $vrio){
  $i++; $L = $k.l.ToUpper()
  Card-Vote "d2-$($k.l)" "Decisión 2 · Prueba VRIO · $i de 2" $k.q 'En esta prueba: tarjeta verde = SÍ · tarjeta roja = NO' $SN[0] $SN[1] 15
  Card-Answer "d2-$($k.l)-resp" "Decisión 2 · Prueba VRIO · $L" $SN[$k.ok].label $(if($k.ok -eq 0){ 'verde' } else { 'roja' }) $k.ex 'VRIO +3 · criterio +5'
}

Card-Bonus 'bonus' @{clima = 49; cultura = 54; vrio = 52} 20 4
Card-Grito 'grito-pulpa' 'Grito nuevo' 'Cuando alguien pregunte:' '¿Y cómo lo hacemos aquí?' '¡Con pulpa!'

$o = DA 'Copiar el viernes flexible de la torre.' 'Diseñar los turnos con Don Lulo y su equipo.'
Card-Vote 'd3a' 'Decisión 3 · Para la planta · 1 de 2' '¿Qué recibe la planta?' $A2 $o[0] $o[1] 30
$o = DA 'La gala FrutiVerso, importada de Frugle.' 'La novena con buñuelos, renovada con la gente.'
Card-Vote 'd3b' 'Decisión 3 · Para diciembre · 2 de 2' '¿Qué fiesta se hace en diciembre?' $A2 $o[0] $o[1] 30

Card-Reveal 'revelacion' @{clima = 65; cultura = 68; vrio = 64}

Write-Host 'Listo.'
