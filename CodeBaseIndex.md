# Codebase Index

This document provides a comprehensive overview of the UltraCaptureV3 desktop application project structure, describing each major file and folder.

## Documentation Files

- **[README.md](README.md)** - Project overview and quick start guide
- **[Distribution.md](Distribution.md)** - Standalone executable distribution guide, build instructions, and troubleshooting
- **[InstallationAndSetup.md](InstallationAndSetup.md)** - Detailed setup and installation instructions for development
- **[Usage.md](Usage.md)** - Comprehensive usage guide for the desktop application
- **[CodeBaseIndex.md](CodeBaseIndex.md)** - This file: complete codebase structure and descriptions

## Directory Structure

```
UltraCaptureV3/
├── main.py                     # Application entry point
├── config.py                   # Configuration management
├── requirements.txt            # Application dependencies
├── setup.ps1                   # Setup automation script
├── start.ps1                   # Launch script
│
├── core/                       # Core inference logic
│   ├── __init__.py
│   ├── model_manager.py        # ONNX model management
│   ├── image_processor.py      # Image preprocessing
│   ├── ctc_decoder.py          # CTC decoding
│   └── config_loader.py        # Configuration loader
│
├── ui/                         # User interface
│   ├── __init__.py
│   ├── main_window.py          # Main window
│   ├── tabs/                   # Tab implementations
│   │   ├── home_tab.py
│   │   ├── about_tab.py
│   │   ├── architecture_tab.py
│   │   └── inference_tab.py
│   ├── widgets/                # Custom widgets
│   │   ├── metric_card.py
│   │   ├── profile_card.py
│   │   ├── image_upload_widget.py
│   │   └── prediction_display.py
│   └── styles/                 # QSS stylesheets
│       ├── fallout_theme.qss
│       ├── colors.py
│       └── fonts.py
│
├── utils/                      # Utility functions
│   ├── __init__.py
│   ├── logger.py               # Logging configuration
│   ├── file_utils.py           # File operations
│   └── image_utils.py          # Image utilities
│
├── resources/                  # Application resources
│   ├── models/
│   │   └── best_model.onnx     # ONNX model for CPU inference (273MB)
│   ├── config/
│   │   └── model_config.json   # Model configuration
│   └── images/                 # Profile images
│
├── build_exe.ps1               # PowerShell script for building executable
├── build.py                    # Python script for building executable
├── create_distribution.ps1     # Script for creating distribution package
│
├── README.md                   # Project overview
├── Distribution.md             # Distribution guide and build instructions
├── Usage.md                    # Usage guide for desktop application
├── InstallationAndSetup.md     # Installation instructions for development
├── CodeBaseIndex.md            # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore rules
```

**Note:** The following directories are created during the build process and are excluded from version control:
- `build/` - PyInstaller build artifacts
- `dist/` - Compiled executable and distribution package
- `__pycache__/` - Python bytecode cache
- `venv/` - Python virtual environment

These directories are listed in `.gitignore` to keep the repository clean.

## Desktop Application Components:

### Main Application Files:

#### `main.py`:
The main entry point for the desktop application:
- Initializes the PySide6 application
- Creates the main window
- Loads the Fallout-themed interface
- Handles application lifecycle

#### `config.py`:
Configuration management for the application:
- Base directory paths
- Resources directory configuration
- Model path configuration
- Configuration file paths
- Logging configuration

### Build and Distribution Scripts:

#### `build_exe.ps1`:
PowerShell script for building the standalone executable:
- Activates the Python virtual environment
- Cleans previous build artifacts
- Runs PyInstaller with optimized settings
- Creates `dist/UltraCaptureV3.exe` (470+ MB)
- Includes all dependencies and the ONNX model

#### `build.py`:
Python script for building the standalone executable:
- Alternative to `build_exe.ps1`
- Same functionality as the PowerShell script
- Cross-platform compatible
- Useful for non-Windows environments

#### `create_distribution.ps1`:
PowerShell script for creating the distribution package:
- Copies the executable to a distribution folder
- Includes README.md and LICENSE files
- Creates a ZIP file for easy distribution
- Generates `dist/UltraCaptureV3-Distribution.zip`

### Core Inference Logic:

#### `core/model_manager.py`:
ONNX model management:
- Loads the ONNX model from `resources/models/best_model.onnx`
- Manages model inference sessions
- Handles model initialization and cleanup
- Provides prediction interface

#### `core/image_processor.py`:
Image preprocessing pipeline:
- Loads images from file paths
- Resizes images to 64×256 pixels
- Normalizes pixel values
- Converts to appropriate tensor format for the model

#### `core/ctc_decoder.py`:
CTC (Connectionist Temporal Classification) decoding:
- Decodes model output to text
- Handles greedy decoding strategy
- Maps character indices to actual characters
- Supports 62-character charset (0-9, A-Z, a-z)

#### `core/config_loader.py`:
Configuration file loader:
- Loads model configuration from JSON
- Provides access to model hyperparameters
- Manages character set and encoding

### User Interface:

#### `ui/main_window.py`:
Main application window:
- Creates the main PySide6 window
- Sets up the tab widget with four tabs
- Manages window properties and styling
- Handles theme switching

#### `ui/tabs/home_tab.py`:
Home tab implementation:
- Displays project title and tagline
- Shows accuracy metrics (95.08% character, 86.37% sequence)
- Displays creator information
- Shows profile cards with images

#### `ui/tabs/about_tab.py`:
About tab implementation:
- Project overview and description
- Key features list with complete sentences
- External links (GitHub, Kaggle)
- Performance metrics table
- Training metrics visualization

#### `ui/tabs/architecture_tab.py`:
Architecture tab implementation:
- CRNN model architecture explanation
- Model components breakdown with descriptions
- Hyperparameters display
- Technical specifications
- Three-stage architecture flow visualization

#### `ui/tabs/inference_tab.py`:
Inference tab implementation:
- Drag-and-drop image upload interface
- File browser for image selection
- Image preview display
- Predict button for running inference
- Results display with prediction text and inference time
- Clear button to reset for new image

### Custom Widgets:

#### `ui/widgets/metric_card.py`:
Metric card widget:
- Displays accuracy metrics in card format
- Shows metric name and value
- Styled with Fallout theme colors

#### `ui/widgets/profile_card.py`:
Profile card widget:
- Displays profile image and name
- Used for creator information
- Styled with Fallout theme

#### `ui/widgets/image_upload_widget.py`:
Image upload widget:
- Drag-and-drop area for image upload
- Browse button for file selection
- Supported format information
- Upload instructions with complete sentences

#### `ui/widgets/prediction_display.py`:
Prediction display widget:
- Shows predicted CAPTCHA text in large, bold font
- Displays model inference time
- Color-coded for success/error states
- Uses complete sentence labels



### Styling:

#### `ui/styles/fallout_theme.qss`:
QSS stylesheet with Fallout-themed design:
- Green (#00FF41), purple (#9D4EDD), blue (#0096FF) color scheme
- Courier New monospace font for retro aesthetic
- Enhanced button styling with padding and hover effects
- Improved tab styling with better spacing
- Enhanced frame and card styling with hover effects
- Improved scrollbar styling
- Enhanced text input styling with hover states
- Improved table styling with better padding and hover effects

#### `ui/styles/colors.py`:
Color definitions:
- Fallout theme color constants
- Primary, secondary, and accent colors
- Text and background colors

#### `ui/styles/fonts.py`:
Font definitions:
- Courier New monospace font configuration
- Font sizes for different UI elements

### Utility Functions:

#### `utils/logger.py`:
Logging configuration:
- Sets up application logging
- Logs to console and file
- Configurable log levels

#### `utils/file_utils.py`:
File operation utilities:
- File path handling
- Directory creation
- File existence checking

#### `utils/image_utils.py`:
Image utility functions:
- Image loading and validation
- Image format checking
- Image dimension utilities

### Configuration Files:

#### `requirements.txt`:
Python dependencies:
- PySide6 6.6.1 - Qt for Python GUI framework
- ONNX Runtime 1.17.1 - CPU-based inference engine
- Pillow 10.1.0 - Image processing
- NumPy 1.24.3 - Numerical computing

#### `setup.ps1`:
Setup automation script:
- Checks for Python installation
- Creates virtual environment
- Installs dependencies
- Verifies ONNX model
- Verifies resources

#### `start.ps1`:
Launch script:
- Activates virtual environment
- Launches the desktop application
- Displays status messages

### Resources:

#### `resources/models/best_model.onnx`:
ONNX model file (273MB):
- Pre-trained CRNN model for CAPTCHA recognition
- CPU-optimized inference
- 95.08% character accuracy, 86.37% sequence accuracy

#### `resources/config/model_config.json`:
Model configuration:
- Image dimensions (64×256)
- Character set (62 characters)
- Model hyperparameters

#### `resources/images/`:
Profile images:
- redZapdos.jpg - Profile image
- WhiteMetagross.jpg - Profile image
- TrainingMetrics.png - Training metrics visualization

## Key Features and Architecture

### Model Architecture:

The CRNN (Convolutional Recurrent Neural Network) model consists of:

1. **Convolutional Backbone:** ResNet-style CNN with residual connections for robust feature extraction
2. **CBAM Attention:** Channel and spatial attention mechanisms for feature refinement
3. **Bidirectional LSTM:** Captures temporal dependencies in CAPTCHA text sequences
4. **Transformer Encoder:** Processes long-range dependencies for enhanced text recognition
5. **CTC Loss:** Connectionist Temporal Classification for sequence-to-sequence learning

### Model Performance:

- **Character Accuracy:** 95.08% (individual character prediction accuracy)
- **Sequence Accuracy:** 86.37% (entire CAPTCHA sequence prediction accuracy)
- **Inference Time:** 30-100ms per image on modern CPUs
- **Model Size:** 273MB (ONNX format, CPU-optimized)
- **Input:** 64×256 pixel images (RGB)
- **Output:** 62-character charset (0-9, A-Z, a-z)

### Deployment:

- **Framework:** ONNX Runtime 1.17.1 (CPU-based inference)
- **No GPU Required:** Fully optimized for CPU performance
- **Cross-Platform:** Runs on Windows, macOS, and Linux
- **Offline Capable:** Works completely offline after initial setup
- **Lightweight:** No PyTorch or TensorFlow required for inference

## Development and Customization

### Adding New Features:

To add new features to the desktop application:

1. **New Tab:** Create a new file in `ui/tabs/` and implement the tab class
2. **New Widget:** Create a new file in `ui/widgets/` for custom widgets
3. **New Utility:** Add functions to `utils/` modules
4. **Styling:** Update `ui/styles/fallout_theme.qss` for visual changes

### Modifying the Model:

To use a different ONNX model:

1. Replace `resources/models/best_model.onnx` with your model
2. Update `resources/config/model_config.json` with new model parameters
3. Ensure input/output shapes match the model expectations
4. Update charset if different from 62 characters

### Building Executables:

To create a standalone executable (Windows):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be created in the `dist/` directory.

## Documentation Files

### `InstallationAndSetup.md`:
Comprehensive installation guide:
- Prerequisites for desktop application
- Automated and manual setup instructions
- Running the desktop application
- Troubleshooting common issues
- Environment configuration

### `Usage.md`:
User guide for desktop application:
- Desktop application usage
- Tab navigation and features
- Tips and best practices
- Troubleshooting

### `API.md`:
Historical REST API documentation (for reference)

### `CodeBaseIndex.md`:
This file - complete codebase structure and descriptions

### `README.md`:
Project README with:
- Project overview and features
- Model architecture details
- Performance metrics
- Quick start guide
- Links to detailed documentation

## PowerShell Scripts:

### `setup.ps1`:
Automated setup script:
- Checks for Python installation
- Creates Python virtual environment
- Installs dependencies
- Verifies ONNX model
- Verifies resources

### `start.ps1`:
Application startup script:
- Activates virtual environment
- Launches desktop application
- Displays status messages

## Technology Stack

### Desktop Application
- **Framework:** PySide6 6.6.1 (Qt for Python)
- **Inference:** ONNX Runtime 1.17.1 (CPU-optimized)
- **Image Processing:** Pillow 10.1.0, NumPy 1.24.3
- **Styling:** QSS (Qt Style Sheets) with Fallout theme
- **Python:** 3.11 (recommended) or 3.8+

## Key Design Decisions

1. **ONNX Runtime for CPU Inference:**
   - No GPU requirement (works on any CPU)
   - Faster inference than PyTorch (30-100ms per image)
   - Smaller deployment footprint (273MB model)
   - Cross-platform compatibility

2. **Desktop Application Focus:**
   - Native GUI for performance and offline capability
   - Standalone executable for easy distribution
   - Direct ONNX model access (no API required)

3. **Fallout-Themed Design:**
   - Green (#00FF41), purple (#9D4EDD), blue (#0096FF) color scheme
   - Courier New monospace font for retro aesthetic
   - Enhanced interactive elements with hover effects

4. **Modular Architecture:**
   - Clear separation between core inference, UI, and utilities
   - Easy to extend with new tabs and widgets
   - Reusable components for consistent design

5. **Threading for Desktop:**
   - Non-blocking inference using QThread to prevent UI freezing
   - Responsive interface during model processing

## Development Workflow

### Desktop Application Development
```bash
.\setup.ps1  # First time only
.\start.ps1  # Launch application
```
- PySide6 for native GUI
- Direct ONNX model access (no API required)
- QSS stylesheets for theming

### Building for Production

**Desktop:**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
# Creates standalone executable in dist/
```

## Future Enhancements:

Potential areas for expansion:
- Batch image processing
- Model performance analytics dashboard
- Real-time webcam capture for CAPTCHA solving
- Additional export formats for predictions
- Model fine-tuning interface

