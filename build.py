#!/usr/bin/env python3
"""
UltraCaptureV3 - PyInstaller Build Script
Builds a standalone Windows executable from the Python application
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 40)
    print(text)
    print("=" * 40 + "\n")

def print_status(status, message):
    """Print a status message"""
    symbols = {
        "info": "[*]",
        "ok": "[OK]",
        "error": "[ERROR]",
        "warning": "[WARNING]"
    }
    print(f"{symbols.get(status, '[*]')} {message}")

def main():
    """Main build function"""
    print_header("UltraCaptureV3 - Building Executable")
    
    # Get project root directory
    project_root = Path(__file__).parent.absolute()
    print_status("info", f"Build directory: {project_root}")
    
    # Check if virtual environment exists
    venv_path = project_root / "venv"
    if not venv_path.exists():
        print_status("error", f"Virtual environment not found at: {venv_path}")
        print_status("info", "Please run setup.ps1 first to create the virtual environment")
        return 1
    
    # Check if PyInstaller is installed
    print_status("info", "Checking PyInstaller installation...")
    try:
        import PyInstaller
        print_status("ok", "PyInstaller is available")
    except ImportError:
        print_status("info", "Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "PyInstaller==6.3.0"], check=True)
        print_status("ok", "PyInstaller installed")
    
    # Clean previous builds
    print_status("info", "Cleaning previous builds...")
    build_dir = project_root / "build"
    dist_dir = project_root / "dist"
    spec_file = project_root / "main.spec"
    
    if build_dir.exists():
        shutil.rmtree(build_dir)
        print_status("ok", "Removed build directory")
    
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
        print_status("ok", "Removed dist directory")
    
    if spec_file.exists():
        spec_file.unlink()
        print_status("ok", "Removed spec file")
    
    # Verify required files exist
    print_status("info", "Verifying required files...")
    required_files = [
        project_root / "main.py",
        project_root / "resources",
        project_root / "ui",
        project_root / "core",
        project_root / "utils"
    ]
    
    for file_path in required_files:
        if not file_path.exists():
            print_status("error", f"Required file/directory not found: {file_path}")
            return 1
    
    print_status("ok", "All required files found")
    
    # Build the executable
    print_header("Building Executable with PyInstaller...")
    
    # PyInstaller arguments
    pyinstaller_args = [
        "pyinstaller",
        "--onefile",                                    # Single executable file
        "--windowed",                                   # No console window
        "--name=UltraCaptureV3",                       # Executable name
        "--add-data=resources:resources",              # Include resources directory
        "--add-data=ui:ui",                            # Include UI directory
        "--add-data=core:core",                        # Include core directory
        "--add-data=utils:utils",                      # Include utils directory
        "--hidden-import=PySide6",                     # Hidden imports
        "--hidden-import=onnxruntime",
        "--hidden-import=PIL",
        "--hidden-import=numpy",
        "--collect-all=PySide6",                       # Collect all PySide6 files
        f"--distpath={dist_dir}",                      # Output directory
        f"--workpath={build_dir}",                     # Work directory
        f"--specpath={project_root}",                  # Spec file directory
        str(project_root / "main.py")                  # Main script
    ]
    
    # Check for icon file
    icon_path = project_root / "resources" / "images" / "icon.ico"
    if icon_path.exists():
        pyinstaller_args.insert(3, f"--icon={icon_path}")
    
    print_status("info", f"Running PyInstaller...")
    print_status("info", f"Command: {' '.join(pyinstaller_args)}")
    
    try:
        result = subprocess.run(pyinstaller_args, check=True)
    except subprocess.CalledProcessError as e:
        print_status("error", f"PyInstaller build failed with exit code {e.returncode}")
        return 1
    
    print_status("ok", "PyInstaller build completed successfully")
    
    # Verify the executable was created
    exe_path = dist_dir / "UltraCaptureV3.exe"
    if exe_path.exists():
        exe_size = exe_path.stat().st_size / (1024 * 1024)
        print_status("ok", f"Executable created: {exe_path}")
        print_status("ok", f"Executable size: {exe_size:.2f} MB")
    else:
        print_status("error", f"Executable not found at: {exe_path}")
        return 1
    
    print_header("Build Complete!")
    print_status("info", f"Executable location: {exe_path}")
    print_status("info", f"To test the executable: {exe_path}")
    print_status("info", "To create a distribution package:")
    print_status("info", "  1. Copy the dist/UltraCaptureV3 folder")
    print_status("info", "  2. Create a zip file or installer")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

