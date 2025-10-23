# UltraCaptureV3 - Distribution Guide

**Version:** 1.0.0  
**Created by:** Mridankan Mandal  
**Project:** Project AA  
**© 2025 UltraCaptureV3**

---

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Quick Start for End Users](#quick-start-for-end-users)
4. [Building from Source](#building-from-source)
5. [Application Features](#application-features)
6. [Usage Guide](#usage-guide)
7. [Troubleshooting](#troubleshooting)
8. [Version Information](#version-information)
9. [Support Resources](#support-resources)

---

## Overview:

**UltraCaptureV3** is an advanced CAPTCHA recognition system featuring a hybrid CRNN (Convolutional Recurrent Neural Network) architecture with attention mechanisms. This distribution includes a standalone Windows executable that requires no Python installation.

### Key Highlights:

- **High Accuracy:** 95.08% Character Accuracy, 86.37% Sequence Accuracy.
- **Advanced Architecture:** Hybrid CRNN with ResNet backbone, CBAM attention, Bi-LSTM, and Transformer Encoder.
- **CPU-Based Inference:** Fast, optimized CPU inference (30-100ms per image) without GPU requirements.
- **Fallout-Themed UI:** Unique retro aesthetic with green, purple, and blue color palette.
- **Standalone Executable:** No Python installation required.
- **Cross-Platform Ready:** Can be adapted for macOS and Linux.

---

## System Requirements:

### Minimum Requirements:

- **Operating System:** Windows 7 or later (64-bit).
- **RAM:** 4GB minimum.
- **Storage:** 500MB free disk space.
- **GPU:** Not required (CPU inference is fully supported).
- **Python:** NOT required (included in the executable).

### Recommended Requirements:

- **Operating System:** Windows 10 or later (64-bit).
- **RAM:** 8GB or more.
- **Storage:** 1GB free disk space.

---

## Quick Start for End Users:

### Step 1: Download the Distribution Package:

Download `UltraCaptureV3-Distribution.zip` (approximately 469 MB).

**File Location:** `dist/UltraCaptureV3-Distribution.zip`.

### Step 2: Extract the Package:

1. Right-click the ZIP file.
2. Select "Extract All...".
3. Choose your destination folder (e.g., `C:\Program Files\UltraCaptureV3\`).

### Step 3: Run the Application:

1. Navigate to the extracted folder.
2. Double-click `UltraCaptureV3.exe`.
3. The application will launch with the Fallout-themed interface.

### Step 4: Using the Application:

- Navigate through the four tabs: **Home**, **About**, **Architecture**, and **Inference**.
- Use the **Inference tab** to upload CAPTCHA images and get predictions.
- Drag-and-drop images or use the browse button to select files.

---

## Building from Source:

### Prerequisites:

- Python 3.8+ (3.11 recommended).
- Virtual environment (venv).
- All dependencies from `requirements.txt`.

### Build Instructions:

#### Option 1: Using PowerShell Script (Recommended):

```powershell
# First time setup
.\setup.ps1

# Build the executable
.\build_exe.ps1

# Create distribution package
.\create_distribution.ps1
```

#### Option 2: Using Python Script:

```bash
# First time setup
.\setup.ps1

# Build the executable
python build.py

# Create distribution package
.\create_distribution.ps1
```

### Build Output:

- **Executable:** `dist/UltraCaptureV3.exe` (470+ MB).
- **Distribution Package:** `dist/UltraCaptureV3-Distribution.zip` (469+ MB).
- **Distribution Folder:** `dist/UltraCaptureV3-Distribution/`.

### Build Scripts Reference:

- **`build_exe.ps1`** - PowerShell script for building the executable.
  - Cleans previous builds.
  - Verifies required files.
  - Runs PyInstaller with optimized settings.
  - Creates standalone executable.

- **`build.py`** - Python script for building the executable.
  - Alternative to PowerShell script.
  - Same functionality as build_exe.ps1.
  - Cross-platform compatible.

- **`create_distribution.ps1`** - Creates distribution package.
  - Copies executable to distribution folder.
  - Includes README and LICENSE.
  - Creates ZIP file for distribution.

---

## Application Features:

### Home Tab:
- Project title and tagline.
- Accuracy metrics (95.08% character, 86.37% sequence).
- Creator information.
- Project overview.

### About Tab:
- Project overview and description.
- Key features and capabilities.
- Performance metrics table.
- External links (GitHub, Kaggle).

### Architecture Tab:
- CRNN model architecture explanation.
- Model components breakdown.
- Hyperparameters display.
- Technical specifications.

### Inference Tab (Main Feature):
- **Upload Image:** Drag-and-drop or browse to select a CAPTCHA image.
- **Supported Formats:** PNG, JPG, JPEG.
- **Predict:** Click "Predict CAPTCHA" to run inference.
- **View Results:** See the predicted text and inference time.
- **Clear:** Click "Clear" to reset and try another image.

---

## Usage Guide:

### Supported Characters:

The model recognizes 62 characters:
- **Digits:** 0-9.
- **Uppercase Letters:** A-Z.
- **Lowercase Letters:** a-z.

### Performance Metrics:

| Metric             | Validation Set | Test Set |
| ------------------ | :------------: | :------: |
| Sequence Accuracy  |     86.4%      | 86.37%   |
| Character Accuracy |     95.1%      | 95.08%   |

**Inference Time:** 30-100ms per image (CPU).
**Model Size:** 273MB (ONNX format).

### Tips for Best Results:

- Use clear, high-contrast CAPTCHA images.
- Avoid heavily distorted or low-resolution images.
- The model performs best on images similar to the Huge CAPTCHA Dataset.
- First prediction may be slower (200-300ms) due to model initialization.
- Subsequent predictions should be faster (100-200ms).

---

## Troubleshooting:

### Application Won't Start:

**Problem:** Application fails to launch.
**Solutions:**
- Ensure your system meets minimum requirements (Windows 7+, 4GB RAM).
- Try running as Administrator.
- Check that you have at least 500MB free disk space.
- Verify the executable file is not corrupted.

### Slow Performance:

**Problem:** Predictions are taking too long.
**Solutions:**
- First prediction is slower due to model initialization (normal).
- Close other applications to free up system resources.
- Ensure your system has at least 4GB of RAM available.
- Check CPU usage and close unnecessary programs.

### Prediction Errors:

**Problem:** Model predictions are incorrect.
**Solutions:**
- The model has 86.37% sequence accuracy (some errors are expected).
- Try with clearer images or images similar to the Huge CAPTCHA Dataset.
- Ensure the image is in PNG, JPG, or JPEG format.
- Check that the image can be resized to 64×256 pixels.

### Image Upload Issues:

**Problem:** Image upload doesn't work.
**Solutions:**
- Ensure the file is in PNG, JPG, or JPEG format.
- Check that the file size is reasonable (under 10MB).
- Try dragging and dropping instead of using the browse button.
- Verify the image file is not corrupted.

### Application Crashes:

**Problem:** Application crashes unexpectedly.
**Solutions:**
- Try restarting the application.
- Ensure your Windows installation is up to date.
- Check that you have sufficient disk space.
- Try with a different image file.

---

## Distribution Package Contents:

### Build Output Structure:

After running the build scripts, the following directories and files are created:

```
dist/
├── UltraCaptureV3.exe                    # Main executable (470+ MB)
├── UltraCaptureV3-Distribution.zip       # Distribution package (469+ MB)
└── UltraCaptureV3-Distribution/          # Distribution folder
    ├── UltraCaptureV3.exe
    ├── README.md
    └── LICENSE
```

### Distribution Package Contents:

When you extract `UltraCaptureV3-Distribution.zip`, you get:

```
UltraCaptureV3-Distribution/
├── UltraCaptureV3.exe          # Main executable (470+ MB)
├── README.md                    # User guide
├── LICENSE                      # MIT License
└── resources/                   # Application resources (included in .exe)
    ├── models/
    │   └── best_model.onnx      # ONNX model (273MB)
    ├── config/
    │   └── model_config.json    # Model configuration
    └── images/                  # Profile images
```

### File Sizes:

- **UltraCaptureV3.exe:** 470.43 MB.
- **UltraCaptureV3-Distribution.zip:** 469.48 MB.

**Note:** The `dist/` directory is created during the build process and is not included in the repository. It is listed in `.gitignore` to keep the repository clean.

---

## Version Information:

### Current Version: 1.0.0:

**Build Information:**
- Build Date: 2025-10-23.
- Python Version: 3.11.
- PySide6 Version: 6.6.1.
- ONNX Runtime Version: 1.17.1.
- PyInstaller Version: 6.3.0.

### Changelog:

**v1.0.0 (2025-10-23)**
- Initial standalone executable release.
- Fixed character '0' display bug in CTC decoder.
- Optimized for CPU-based inference.
- Fallout-themed UI with four tabs.
- Drag-and-drop image upload interface.
- Comprehensive documentation.

---

## Support Resources:

### For End Users:

- **Usage Guide:** See [Usage Guide](#usage-guide) section above.
- **Troubleshooting:** See [Troubleshooting](#troubleshooting) section above.
- **GitHub Repository:** https://github.com/WhiteMetagross/CRNN_Captcha_Recognition.
- **Kaggle Dataset:** https://www.kaggle.com/datasets/redzapdos123/huge-captcha-dataset.

### For Developers:

- **CodeBaseIndex.md** - Complete codebase structure and descriptions.
- **InstallationAndSetup.md** - Detailed setup and installation instructions.
- **Usage.md** - Comprehensive usage guide for all features.
- **README.md** - Project overview and quick start.

### Creator Information:

- **Creator:** Mridankan Mandal (RedZapdos123, WhiteMetagross).
- **Project:** Project AA.
- **License:** MIT License.

---

## License:

This project is licensed under the MIT License - see the LICENSE file for details.

© 2025 UltraCaptureV3. All rights reserved.

---

## Deployment Status:

**Status:** PRODUCTION READY.

All deliverables completed and verified. Ready for production deployment.

For detailed deployment information, see the project documentation files.

