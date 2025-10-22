# UltraCaptureV3 Setup Script.
# This script automates the setup process for both frontend and backend.

Write-Host "  UltraCaptureV3 Setup Script" -ForegroundColor Cyan
Write-Host ""

# Check for Python 3.11 installation.
Write-Host "Checking for Python 3.11 installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found. Please install Python 3.11" -ForegroundColor Red
    exit 1
}

# Check for Node.js installation.
Write-Host "Checking for Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "[OK] Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Node.js not found. Please install Node.js" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "  Setting up Backend" -ForegroundColor Cyan
Write-Host ""

Set-Location -Path "backend"

Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
if (Test-Path "ultracapturev3") {
    Write-Host "[OK] Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv ultracapturev3
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Virtual environment created" -ForegroundColor Green
    } else {
        Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
        Set-Location -Path ".."
        exit 1
    }
}

Write-Host "Installing backend dependencies (ONNX Runtime CPU)..." -ForegroundColor Yellow
& "ultracapturev3\Scripts\Activate.ps1"
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Backend dependencies installed" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Failed to install backend dependencies" -ForegroundColor Red
    deactivate
    Set-Location -Path ".."
    exit 1
}

Write-Host "Checking for ONNX model..." -ForegroundColor Yellow
if (Test-Path "models\best_model.onnx") {
    Write-Host "[OK] ONNX model found" -ForegroundColor Green
} else {
    Write-Host "[ERROR] ONNX model not found" -ForegroundColor Red
    deactivate
    Set-Location -Path ".."
    exit 1
}

deactivate
Set-Location -Path ".."

Write-Host ""
Write-Host "  Setting up Frontend" -ForegroundColor Cyan
Write-Host ""

Set-Location -Path "frontend"

Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
npm install
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Frontend dependencies installed" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Failed to install frontend dependencies" -ForegroundColor Red
    Set-Location -Path ".."
    exit 1
}

Set-Location -Path ".."

Write-Host ""
Write-Host "  Setup Complete!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Green
Write-Host "1. Run '.\start.ps1' to start the application" -ForegroundColor White
Write-Host "2. Open your browser to http://localhost:5173" -ForegroundColor White
Write-Host ""

