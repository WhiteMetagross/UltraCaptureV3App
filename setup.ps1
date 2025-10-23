# UltraCaptureV3 Desktop Application Setup Script
# This script sets up the Python virtual environment and installs dependencies

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "UltraCaptureV3 Desktop Application Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "[*] Script directory: $scriptDir" -ForegroundColor Yellow

# Check if Python is installed
Write-Host "[*] Checking Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher from https://www.python.org/" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Found: $pythonVersion" -ForegroundColor Green

# Create virtual environment
$venvPath = Join-Path $scriptDir "venv"
if (Test-Path $venvPath) {
    Write-Host "[*] Virtual environment already exists at: $venvPath" -ForegroundColor Yellow
    Write-Host "[*] Skipping venv creation" -ForegroundColor Yellow
} else {
    Write-Host "[*] Creating virtual environment..." -ForegroundColor Yellow
    python -m venv $venvPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
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

# Upgrade pip
Write-Host "[*] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARNING] Failed to upgrade pip, continuing anyway..." -ForegroundColor Yellow
}

# Install requirements
$requirementsFile = Join-Path $scriptDir "requirements.txt"
if (Test-Path $requirementsFile) {
    Write-Host "[*] Installing dependencies from requirements.txt..." -ForegroundColor Yellow
    pip install -r $requirementsFile
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "[ERROR] requirements.txt not found at: $requirementsFile" -ForegroundColor Red
    exit 1
}

# Verify resources exist
Write-Host "[*] Verifying resources..." -ForegroundColor Yellow
$resourcesDir = Join-Path $scriptDir "resources"
$modelsDir = Join-Path $resourcesDir "models"
$imagesDir = Join-Path $resourcesDir "images"
$configDir = Join-Path $resourcesDir "config"

# Create resources directories if they don't exist
New-Item -ItemType Directory -Force -Path $modelsDir | Out-Null
New-Item -ItemType Directory -Force -Path $imagesDir | Out-Null
New-Item -ItemType Directory -Force -Path $configDir | Out-Null

# Verify ONNX model exists
$modelPath = Join-Path $modelsDir "best_model.onnx"
if (Test-Path $modelPath) {
    $modelSize = (Get-Item $modelPath).Length / 1MB
    Write-Host "[OK] ONNX model found ($('{0:F2}' -f $modelSize) MB)" -ForegroundColor Green
} else {
    Write-Host "[ERROR] ONNX model not found at: $modelPath" -ForegroundColor Red
    Write-Host "Please ensure the model file is in the resources/models directory" -ForegroundColor Red
    exit 1
}

# Verify config exists
$configPath = Join-Path $configDir "model_config.json"
if (Test-Path $configPath) {
    Write-Host "[OK] Model configuration found" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Model configuration not found at: $configPath" -ForegroundColor Yellow
}

# Verify images exist
$requiredImages = @("redZapdos.jpg", "WhiteMetagross.jpg", "TrainingMetrics.png")
$missingImages = @()
foreach ($image in $requiredImages) {
    $imagePath = Join-Path $imagesDir $image
    if (Test-Path $imagePath) {
        Write-Host "[OK] Image found: $image" -ForegroundColor Green
    } else {
        $missingImages += $image
    }
}

if ($missingImages.Count -gt 0) {
    Write-Host "[WARNING] Missing images: $($missingImages -join ', ')" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application, run:" -ForegroundColor Yellow
Write-Host "  .\start.ps1" -ForegroundColor Cyan
Write-Host ""

