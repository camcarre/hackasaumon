<#function Check-FileOpen {
    param (
          [parameter(Mandatory=$true)]
          [string]$Path
      )
    $oFile = New-Object System.IO.FileInfo $Path
    if ((Test-Path -Path $Path) -eq $false)
    {
      $false
      return
    }
    try
    {
        $oStream = $oFile.Open([System.IO.FileMode]::Open, [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::None)
        if ($oStream)
        {
          $oStream.Close()
        }
        $false
    }
    catch
    {
      # file is locked by a process.
      $true
    }
}
$files = get-childitem -name C:/Users/jbbod/Pictures/Screenshots

foreach ($File in $Files)
{
    "$($File) dans l'etat : $(Check-FileOpen -Path /)"
}
#>
# Chemin du dossier à parcourir
# Obtient la liste des fichiers récents
$Files = Get-ChildItem -Path "C:\Users\jbbod\AppData\Roaming\Microsoft\Windows\Recent" -Exclude ms*| Sort LastWriteTime | select -last 2

$Files.LastWriteTime