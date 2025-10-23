# UltraCaptureV3 Desktop Application Start Script
# This script activates the virtual environment and launches the application

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "UltraCaptureV3 Desktop Application" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "[*] Application directory: $scriptDir" -ForegroundColor Yellow

# Check if virtual environment exists
$venvPath = Join-Path $scriptDir "venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "[ERROR] Virtual environment not found at: $venvPath" -ForegroundColor Red
    Write-Host "[*] Please run setup.ps1 first to create the virtual environment" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Activate virtual environment
Write-Host "[*] Activating virtual environment..." -ForegroundColor Yellow
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
& $activateScript
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to activate virtual environment" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Virtual environment activated" -ForegroundColor Green

# Check if main.py exists
$mainScript = Join-Path $scriptDir "main.py"
if (-not (Test-Path $mainScript)) {
    Write-Host "[ERROR] main.py not found at: $mainScript" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Application..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Launch the application
python $mainScript

# If we get here, the application has closed
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Application Closed" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

