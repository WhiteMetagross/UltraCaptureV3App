# UltraCaptureV3 - Create Distribution Package Script
# This script creates a distribution package with the standalone executable

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "UltraCaptureV3 - Creating Distribution" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "[*] Project directory: $scriptDir" -ForegroundColor Yellow

# Check if executable exists
$exePath = Join-Path $scriptDir "dist\UltraCaptureV3.exe"
if (-not (Test-Path $exePath)) {
    Write-Host "[ERROR] Executable not found at: $exePath" -ForegroundColor Red
    Write-Host "[*] Please run build_exe.ps1 first to create the executable" -ForegroundColor Yellow
    exit 1
}
Write-Host "[OK] Executable found: $exePath" -ForegroundColor Green

# Create distribution directory
$distDir = Join-Path $scriptDir "dist"
$distPackageDir = Join-Path $distDir "UltraCaptureV3-Distribution"

Write-Host "[*] Creating distribution directory..." -ForegroundColor Yellow
if (Test-Path $distPackageDir) {
    Remove-Item -Recurse -Force $distPackageDir
}
New-Item -ItemType Directory -Force -Path $distPackageDir | Out-Null
Write-Host "[OK] Distribution directory created" -ForegroundColor Green

# Copy executable
Write-Host "[*] Copying executable..." -ForegroundColor Yellow
Copy-Item -Path $exePath -Destination $distPackageDir
Write-Host "[OK] Executable copied" -ForegroundColor Green

# Copy README
Write-Host "[*] Copying documentation..." -ForegroundColor Yellow
$readmePath = Join-Path $scriptDir "DISTRIBUTION_README.md"
if (Test-Path $readmePath) {
    Copy-Item -Path $readmePath -Destination (Join-Path $distPackageDir "README.md")
    Write-Host "[OK] README copied" -ForegroundColor Green
} else {
    Write-Host "[WARNING] DISTRIBUTION_README.md not found" -ForegroundColor Yellow
}

# Copy LICENSE
$licensePath = Join-Path $scriptDir "LICENSE"
if (Test-Path $licensePath) {
    Copy-Item -Path $licensePath -Destination $distPackageDir
    Write-Host "[OK] LICENSE copied" -ForegroundColor Green
} else {
    Write-Host "[WARNING] LICENSE not found" -ForegroundColor Yellow
}

# Create ZIP file
Write-Host "[*] Creating ZIP distribution package..." -ForegroundColor Yellow
$zipPath = Join-Path $distDir "UltraCaptureV3-Distribution.zip"

# Remove existing ZIP if it exists
if (Test-Path $zipPath) {
    Remove-Item -Force $zipPath
}

# Create ZIP using PowerShell
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory($distPackageDir, $zipPath)

if (Test-Path $zipPath) {
    $zipSize = (Get-Item $zipPath).Length / 1MB
    Write-Host "[OK] ZIP package created: $zipPath" -ForegroundColor Green
    Write-Host "[OK] ZIP size: $('{0:F2}' -f $zipSize) MB" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Failed to create ZIP package" -ForegroundColor Red
    exit 1
}

# Create a folder-based distribution as well
Write-Host "[*] Distribution folder ready at: $distPackageDir" -ForegroundColor Yellow

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Distribution Package Created!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Distribution Packages:" -ForegroundColor Yellow
Write-Host "  ZIP File: $zipPath" -ForegroundColor Cyan
Write-Host "  Folder:   $distPackageDir" -ForegroundColor Cyan
Write-Host ""
Write-Host "To distribute:" -ForegroundColor Yellow
Write-Host "  1. Share the ZIP file: UltraCaptureV3-Distribution.zip" -ForegroundColor Cyan
Write-Host "  2. Users can extract and run UltraCaptureV3.exe directly" -ForegroundColor Cyan
Write-Host "  3. No Python installation required!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Package Contents:" -ForegroundColor Yellow
Write-Host "  - UltraCaptureV3.exe (470+ MB)" -ForegroundColor Cyan
Write-Host "  - README.md (Usage instructions)" -ForegroundColor Cyan
Write-Host "  - LICENSE (MIT License)" -ForegroundColor Cyan
Write-Host ""

