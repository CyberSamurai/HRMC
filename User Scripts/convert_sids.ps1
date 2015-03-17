$Sids = Get-Content -Path "C:\\TEMP\users_admins.txt"

ForEach ($Sid In $Sids)
{
    $SAM = (New-Object System.Security.Principal.SecurityIdentifier($SID)).Translate([System.Security.Principal.NTAccount])
    $SAM | Out-File .\users_admins_conv.txt -Append
}

$Sids = Get-Content -Path "C:\\TEMP\users_providers.txt"

ForEach ($Sid In $Sids)
{
    $SAM = (New-Object System.Security.Principal.SecurityIdentifier($SID)).Translate([System.Security.Principal.NTAccount])
    $SAM | Out-File .\users_providers_conv.txt -Append
}

$Sids = Get-Content -Path "C:\\TEMP\users_radiologists.txt"

ForEach ($Sid In $Sids)
{
    $SAM = (New-Object System.Security.Principal.SecurityIdentifier($SID)).Translate([System.Security.Principal.NTAccount])
    $SAM | Out-File .\users_radiologists_conv.txt -Append
}

$Sids = Get-Content -Path "C:\\TEMP\users_technicians.txt"

ForEach ($Sid In $Sids)
{
    $SAM = (New-Object System.Security.Principal.SecurityIdentifier($SID)).Translate([System.Security.Principal.NTAccount])
    $SAM | Out-File .\users_technicians_conv.txt -Append
}