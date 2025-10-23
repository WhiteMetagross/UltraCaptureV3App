# Installation and Setup Guide:

This guide provides step-by-step instructions for setting up and running the UltraCaptureV3 desktop application. The application is a standalone PySide6-based CAPTCHA recognition system with a Fallout-themed interface.

## Quick Links:

- **For End Users (Standalone Executable):** See [Distribution.md](Distribution.md) for instructions on downloading and running the pre-built executable.
- **For Developers (Building from Source):** Continue with this guide for development setup.
- **For Distribution Information:** See [Distribution.md](Distribution.md) for build scripts and distribution details.

## Prerequisites:

Before you begin, ensure you have the following installed on your system.

### Required Software:

1. **Python** (version 3.11 recommended, 3.8+ supported).
   - Download from: https://www.python.org/downloads/.
   - Verify installation: `python --version`.
   - **Note:** Python 3.11 is recommended for optimal ONNX Runtime performance.

2. **pip** (Python package installer).
   - Usually comes with Python.
   - Verify installation: `pip --version`.

3. **Git** (optional, for cloning the repository).
   - Download from: https://git-scm.com/.

### System Requirements:

- **CPU:** Any modern processor (Intel, AMD, ARM).
- **RAM:** Minimum 4GB (8GB recommended).
- **Storage:** At least 500MB free space for dependencies and models.
- **GPU:** Not required (CPU inference is fully supported).

## Installation Steps:

### Automated Setup (Recommended):

The easiest way to set up the application is using the provided PowerShell script:

```powershell
.\setup.ps1
```

#### What the setup.ps1 Script Does:

The `setup.ps1` PowerShell script automates the entire setup process for the desktop application:

**Script Functionality:**
- Checks for Python 3.8+ installation on your system.
- Creates a Python virtual environment in the project root.
- Installs all dependencies (PySide6, ONNX Runtime, Pillow, NumPy).
- Verifies the ONNX model exists at `resources/models/best_model.onnx`.
- Verifies all required resources are in place.
- Displays status messages for each step ([OK] for success, [ERROR] for failures).

**Expected Output:**
```
UltraCaptureV3 Desktop Application Setup

Checking prerequisites...
[OK] Python 3.11 found

Setting up virtual environment...
[OK] Virtual environment created
[OK] Dependencies installed

Verifying resources...
[OK] ONNX model found (272.82 MB)
[OK] Config files verified
[OK] Images verified

Setup complete! You can now run .\start.ps1 to launch the application.
```

**When to Use:**
- First-time setup of the project.
- After cloning the repository.
- When you need to reinstall dependencies.

**Troubleshooting:**
- If the script fails, check that Python 3.8+ is installed and accessible from the command line.
- Ensure you have administrator privileges to create virtual environments.
- If dependencies fail to install, try running the script again or use manual setup.

### Manual Setup:

If you prefer to set up manually or encounter issues with the automated script, follow these steps.

#### Step 1: Create Virtual Environment:

1. Navigate to the project root directory.

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

#### Step 2: Install Dependencies:

Install Python dependencies (PySide6 and ONNX Runtime for CPU inference):
```bash
pip install -r requirements.txt
```

This will install:
- PySide6 6.6.1 - Qt for Python GUI framework.
- ONNX Runtime 1.17.1 - CPU-based inference engine.
- Pillow 10.1.0 - Image processing.
- NumPy 1.24.3 - Numerical computing.

#### Step 3: Verify Resources:

Verify the ONNX model exists:
```bash
ls resources/models/best_model.onnx
```

The ONNX model should already be present in the `resources/models/` directory. If not, contact the project maintainers.

## Running the Application:

### Automated Start (Recommended):

Use the provided PowerShell script to launch the desktop application:

```powershell
.\start.ps1
```

#### What the start.ps1 Script Does:

The `start.ps1` PowerShell script launches the desktop application:

**Script Functionality:**
- Activates the Python virtual environment.
- Launches the PySide6 desktop application with the Fallout-themed interface.
- Displays startup messages and status information.
- Keeps the application running until you close it.

**Expected Output:**
```
UltraCaptureV3 Desktop Application

Activating virtual environment...
[OK] Virtual environment activated

Launching application...
[OK] Application starting

UltraCaptureV3 is now running!
```

**When to Use:**
- Every time you want to run the application.
- After setup is complete.
- For daily use.

**Stopping the Application:**
- Close the application window directly.
- Or press `Ctrl+C` in the terminal window.

**Troubleshooting:**
- If the application fails to start, ensure the ONNX model exists at `resources/models/best_model.onnx`.
- If you see import errors, ensure all dependencies are installed with `pip install -r requirements.txt`.
- If the application crashes, check the console output for error messages.

### Manual Start:

If you prefer to start the application manually:

1. Activate the virtual environment (if not already activated):
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

2. Launch the desktop application:
   ```bash
   python main.py
   ```

   The application will open with the Fallout-themed interface.

## Accessing the Application:

Once the application is running:

1. The desktop window will open automatically.
2. You will see the Fallout-themed interface with four tabs: Home, About, Architecture, and Inference.
3. Use the drag-and-drop area or browse button to select a CAPTCHA image.
4. The model will process the image and display the predicted text.

## Troubleshooting:

### Application Launch Issues:

**Problem:** `ModuleNotFoundError` when starting the application.
- **Solution:** Ensure you've activated the virtual environment and installed all dependencies with `pip install -r requirements.txt`.

**Problem:** `FileNotFoundError: ONNX model not found at resources/models/best_model.onnx`.
- **Solution:** Ensure the ONNX model file exists in the `resources/models/` directory. The model should be pre-exported and included with the project.

**Problem:** `ImportError: No module named 'PySide6'`.
- **Solution:** Install PySide6 with `pip install PySide6==6.6.1`.

**Problem:** `ImportError: No module named 'onnxruntime'`.
- **Solution:** Install ONNX Runtime with `pip install onnxruntime==1.17.1`.

**Problem:** Application window doesn't appear or crashes immediately.
- **Solution:** Check the console output for error messages. Ensure all dependencies are installed and the ONNX model exists.

### Performance Issues:

**Problem:** Slow inference times on CPU.
- **Solution:** This is normal for CPU inference. ONNX Runtime is optimized for CPU performance, and typical inference times are 30-100ms per image.

**Problem:** Application is slow or unresponsive.
- **Solution:** Ensure your system has at least 4GB of RAM available. Close other applications to free up resources.

### Setup Issues:

**Problem:** `setup.ps1` script fails to run.
- **Solution:** Ensure you have administrator privileges. Try running PowerShell as Administrator and then run the script again.

**Problem:** Python is not found or not in PATH.
- **Solution:** Ensure Python is installed and added to your system PATH. Restart your terminal after installing Python.

### General Issues:

**Problem:** Images not displaying in the application.
- **Solution:** Ensure the profile images are present in the `resources/images/` directory.

**Problem:** Application crashes when loading an image.
- **Solution:** Ensure the image is in a supported format (PNG, JPG, JPEG) and is not corrupted. Check the console output for error messages.

## Environment Configuration:

### Application Configuration:

The application configuration is stored in `config.py`. Key settings include:

- `BASE_DIR`: Base directory for the application.
- `RESOURCES_DIR`: Path to resources directory.
- `MODEL_PATH`: Path to the ONNX model file.
- `CONFIG_PATH`: Path to model configuration file.

### Model Configuration:

The model configuration is stored in `resources/config/model_config.json`. Key settings include:

- `data.image_height`: Input image height (default: 64).
- `data.image_width`: Input image width (default: 256).
- `data.charset`: Character set for predictions.
- `model.*`: Model architecture hyperparameters.

---

## Building the Executable:

For developers who want to create a standalone executable for distribution, see [Distribution.md - Building from Source](Distribution.md#building-from-source) for detailed instructions on using the build scripts:

- **`build_exe.ps1`** - PowerShell script for building the executable.
- **`build.py`** - Python script for building the executable.
- **`create_distribution.ps1`** - Script for creating the distribution package.

The build process creates a standalone Windows executable that requires no Python installation.

---

## Next Steps:

After successful installation and setup:

1. **Launch the Application**: Run `.\start.ps1` to launch the desktop application.
2. **Explore the Interface**: Navigate through the four tabs (Home, About, Architecture, Inference).
3. **Test CAPTCHA Recognition**: Upload a CAPTCHA image and see the model's prediction.
4. **Check Performance**: View inference time and accuracy metrics.
5. **Build Executable (Optional)**: See [Distribution.md](Distribution.md#building-from-source) for instructions on creating a standalone executable.

For detailed usage instructions, see the [Usage Guide](Usage.md).

---

## Support:

If you encounter issues not covered in this guide:

1. Check the [Distribution.md](Distribution.md#troubleshooting) troubleshooting guide for common issues.
2. Check the GitHub repository for known issues: https://github.com/WhiteMetagross/CRNN_Captcha_Recognition.
3. Review the README.md for additional context.
4. Ensure all prerequisites are correctly installed and up to date.
5. Check the [Codebase Index](CodeBaseIndex.md) for technical details.

For end-user support and troubleshooting, see [Distribution.md - Troubleshooting](Distribution.md#troubleshooting).

