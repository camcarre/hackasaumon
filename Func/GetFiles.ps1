
$Files = Get-ChildItem -Path "C:\Users\$($env:USERNAME)\AppData\Roaming\Microsoft\Windows\Recent" -Exclude ms*| Sort LastWriteTime

$Date = Get-Date 
$Day = $Date.Day
$Month = $Date.Month

foreach ($element in $Files)
{
  $LastUsed = $element.LastWriteTime
  $LastDay = $LastUsed.Day
  $LastMonth = $LastUsed.Month
  If (($LastDay -eq $Day) -and ($LastMonth -eq $Month))
  {
    ($element.Name) | Out-File -FilePath "..\data\LastUsed.txt" -Append
  }
}
