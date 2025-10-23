# UltraCaptureV3 Desktop Application - PyInstaller Build Script
# This script builds a standalone Windows executable (.exe) from the Python application

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "UltraCaptureV3 - Building Executable" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "[*] Build directory: $scriptDir" -ForegroundColor Yellow

# Check if virtual environment exists
$venvPath = Join-Path $scriptDir "venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "[ERROR] Virtual environment not found at: $venvPath" -ForegroundColor Red
    Write-Host "[*] Please run setup.ps1 first to create the virtual environment" -ForegroundColor Yellow
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

# Check if PyInstaller is installed
Write-Host "[*] Checking PyInstaller installation..." -ForegroundColor Yellow
python -m pip show pyinstaller > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[*] Installing PyInstaller..." -ForegroundColor Yellow
    pip install PyInstaller==6.3.0
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to install PyInstaller" -ForegroundColor Red
        exit 1
    }
}
Write-Host "[OK] PyInstaller is available" -ForegroundColor Green

# Clean previous builds
Write-Host "[*] Cleaning previous builds..." -ForegroundColor Yellow
$buildDir = Join-Path $scriptDir "build"
$distDir = Join-Path $scriptDir "dist"
$specFile = Join-Path $scriptDir "main.spec"

if (Test-Path $buildDir) {
    Remove-Item -Recurse -Force $buildDir
    Write-Host "[OK] Removed build directory" -ForegroundColor Green
}
if (Test-Path $distDir) {
    Remove-Item -Recurse -Force $distDir
    Write-Host "[OK] Removed dist directory" -ForegroundColor Green
}
if (Test-Path $specFile) {
    Remove-Item -Force $specFile
    Write-Host "[OK] Removed spec file" -ForegroundColor Green
}

# Prepare paths
$mainScript = Join-Path $scriptDir "main.py"
$resourcesDir = Join-Path $scriptDir "resources"
$uiDir = Join-Path $scriptDir "ui"
$coreDir = Join-Path $scriptDir "core"
$utilsDir = Join-Path $scriptDir "utils"

# Verify required files exist
Write-Host "[*] Verifying required files..." -ForegroundColor Yellow
$requiredFiles = @($mainScript, $resourcesDir, $uiDir, $coreDir, $utilsDir)
foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        Write-Host "[ERROR] Required file/directory not found: $file" -ForegroundColor Red
        exit 1
    }
}
Write-Host "[OK] All required files found" -ForegroundColor Green

# Build the executable
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Building Executable with PyInstaller..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Build PyInstaller command
Write-Host "[*] Running PyInstaller..." -ForegroundColor Yellow

$pyinstallerArgs = @(
    "--onefile",
    "--windowed",
    "--name=UltraCaptureV3",
    "--add-data=resources:resources",
    "--add-data=ui:ui",
    "--add-data=core:core",
    "--add-data=utils:utils",
    "--hidden-import=PySide6",
    "--hidden-import=onnxruntime",
    "--hidden-import=PIL",
    "--hidden-import=numpy",
    "--collect-all=PySide6",
    "--distpath=$distDir",
    "--workpath=$buildDir",
    "--specpath=$scriptDir",
    $mainScript
)

# Run PyInstaller
& python -m PyInstaller $pyinstallerArgs

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] PyInstaller build failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[OK] PyInstaller build completed successfully" -ForegroundColor Green

# Verify the executable was created
$exePath = Join-Path $distDir "UltraCaptureV3.exe"
if (Test-Path $exePath) {
    $exeSize = (Get-Item $exePath).Length / 1MB
    Write-Host "[OK] Executable created: $exePath" -ForegroundColor Green
    Write-Host "[OK] Executable size: $('{0:F2}' -f $exeSize) MB" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Executable not found at: $exePath" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Build Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Executable location: $exePath" -ForegroundColor Yellow
Write-Host ""
Write-Host "To test the executable:" -ForegroundColor Yellow
Write-Host "  $exePath" -ForegroundColor Cyan
Write-Host ""
Write-Host "To create a distribution package:" -ForegroundColor Yellow
Write-Host "  1. Copy the dist/UltraCaptureV3 folder" -ForegroundColor Cyan
Write-Host "  2. Create a zip file or installer" -ForegroundColor Cyan
Write-Host ""

