# UltraCaptureV3 Start Script.
# This script starts both the backend and frontend servers.

Write-Host "  UltraCaptureV3 Start Script" -ForegroundColor Cyan
Write-Host ""

# Check if backend virtual environment exists.
if (-not (Test-Path "backend\ultracapturev3")) {
    Write-Host "[ERROR] Backend virtual environment not found." -ForegroundColor Red
    Write-Host "  Please run '.\setup.ps1' first to set up the application." -ForegroundColor Yellow
    exit 1
}

# Check if frontend node_modules exists.
if (-not (Test-Path "frontend\node_modules")) {
    Write-Host "[ERROR] Frontend dependencies not found." -ForegroundColor Red
    Write-Host "  Please run '.\setup.ps1' first to set up the application." -ForegroundColor Yellow
    exit 1
}

Write-Host "Starting UltraCaptureV3..." -ForegroundColor Green
Write-Host ""

# Start backend server in a new window.
Write-Host "Starting backend server (CPU-based ONNX inference)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\ultracapturev3\Scripts\Activate.ps1; python app.py"
Write-Host "[OK] Backend server starting at http://localhost:5000" -ForegroundColor Green

# Wait a moment for backend to initialize.
Start-Sleep -Seconds 2

# Start frontend server in a new window.
Write-Host "Starting frontend server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"
Write-Host "[OK] Frontend server starting at http://localhost:5173" -ForegroundColor Green

Write-Host ""
Write-Host "  Application Started!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Access the application at:" -ForegroundColor Green
Write-Host "  Frontend: http://localhost:5173" -ForegroundColor White
Write-Host "  Backend API: http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "To stop the servers:" -ForegroundColor Yellow
Write-Host "  1. Close the backend PowerShell window (or press Ctrl+C)" -ForegroundColor White
Write-Host "  2. Close the frontend PowerShell window (or press Ctrl+C)" -ForegroundColor White
Write-Host ""
Write-Host "For usage instructions, see Usage.md" -ForegroundColor Green
Write-Host ""

