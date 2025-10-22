# Codebase Index:

This document provides a comprehensive overview of the UltraCaptureV3 project structure, describing each major file and folder.

## Directory Structure:

```
ProjectAAWebsite/
├── frontend/                   # React + Vite frontend application.
│   ├── public/                 # Static assets.
│   │   ├── redZapdos.jpg       # Profile image for RedZapdos123.
│   │   ├── WhiteMetagross.jpg  # Profile image for WhiteMetagross.
│   │   └── vite.svg            # Vite logo.
│   ├── src/                    # Source code.
│   │   ├── lib/                # Utility libraries.
│   │   │   └── utils.ts        # Utility functions (cn for className merging).
│   │   ├── App.css             # Application styles.
│   │   ├── App.tsx             # Main application component.
│   │   ├── index.css           # Global styles with Tailwind directives.
│   │   └── main.tsx            # Application entry point.
│   ├── eslint.config.js        # ESLint configuration.
│   ├── index.html              # HTML entry point.
│   ├── package.json            # Frontend dependencies and scripts.
│   ├── postcss.config.js       # PostCSS configuration for Tailwind.
│   ├── tailwind.config.js      # Tailwind CSS configuration.
│   ├── tsconfig.json           # TypeScript configuration.
│   ├── tsconfig.app.json       # TypeScript app-specific configuration.
│   ├── tsconfig.node.json      # TypeScript Node-specific configuration.
│   └── vite.config.ts          # Vite build configuration.
│
├── backend/                    # Flask backend API with ONNX Runtime.
│   ├── models/                 # Model files.
│   │   └── best_model.onnx     # ONNX exported model for CPU inference (273MB).
│   ├── app.py                  # Flask application with ONNX Runtime inference.
│   ├── config.json             # Model configuration.
│   ├── requirements.txt        # Backend Python dependencies (ONNX Runtime).
│   └── export_to_onnx.py       # Script to export PyTorch model to ONNX format (reference).
│
├── InstallationAndSetup.md     # Installation and setup guide.
├── CodeBaseIndex.md            # This file - codebase structure documentation.
├── Usage.md                    # User guide for the web application.
├── API.md                      # Backend API documentation.
├── setup.ps1                   # PowerShell script for automated setup.
├── start.ps1                   # PowerShell script to start the application.
├── README.md                   # Original project README (reference).
└── config.json                 # Root configuration file (reference).
```

## Frontend Components:

### Main Application Files:

#### `frontend/src/App.tsx`
The main React component containing the entire single-page application with four sections and retro/vintage aesthetic design:

1. **Hero/Home Section:**
   - Project title and tagline with retro typography.
   - Accuracy metrics display (95.08% character, 86.37% sequence).
   - Creator credit and profile cards with vintage styling.

2. **About Section:**
   - Project overview and description.
   - Key features list with retro borders and amber color scheme.
   - Links to GitHub repository and Kaggle dataset.
   - Performance metrics table with vintage styling.
   - Model performance and inference speed information.

3. **Architecture Section:**
   - Detailed explanation of the CRNN architecture.
   - Visual representation of model components with retro cards.
   - Technical specifications and hyperparameters.
   - Amber color palette with no rounded corners.

4. **Inference Section:**
   - Live inference demonstration interface with retro styling.
   - Drag-and-drop image upload with vintage borders.
   - Prediction display with inference time.
   - Error handling with retro alert boxes.

**Key Features:**
- Dark/light theme toggle with retro color scheme.
- Smooth scroll navigation.
- Responsive design for mobile, tablet, and desktop.
- Axios integration for API calls to ONNX Runtime backend.
- State management with React hooks.
- Retro/vintage aesthetic: Amber color palette, Georgia serif font, 4px borders, box shadows, no rounded corners.

#### `frontend/src/index.css`
Global styles with Tailwind CSS directives:
- Base Tailwind imports (`@tailwind base`, `@tailwind components`, `@tailwind utilities`).
- CSS custom properties for theming.
- Global resets and base styles.
- Smooth scrolling behavior.

#### `frontend/src/App.css`
Application-specific styles:
- Root container styling.

#### `frontend/src/lib/utils.ts`
Utility functions:
- `cn()`: Merges className strings using clsx and tailwind-merge for conditional styling.

### Configuration Files:

#### `frontend/package.json`
Frontend dependencies and scripts:
- **Dependencies:** React, React DOM, Axios, Lucide React, Tailwind utilities.
- **Dev Dependencies:** Vite, TypeScript, ESLint, Tailwind CSS, PostCSS.
- **Scripts:**
  - `dev`: Start development server.
  - `build`: Build for production.
  - `preview`: Preview production build.

#### `frontend/tailwind.config.js`
Tailwind CSS configuration:
- Content paths for purging unused styles.
- Dark mode configuration (class-based).
- Custom color palette (purple, blue, red shades).

#### `frontend/vite.config.ts`
Vite build tool configuration:
- React plugin integration.
- Build optimizations.

#### `frontend/tsconfig.json`
TypeScript compiler configuration:
- Strict type checking.
- JSX support for React.
- Module resolution settings.

## Backend Components:

### API Server:

#### `backend/app.py`
Flask application with ONNX Runtime CPU inference (no GPU required):

**Endpoints:**
- `POST /api/predict`: Accepts image upload, returns prediction and inference time (30-100ms).
- `GET /api/health`: Health check endpoint returns model status.

**Key Functions:**
- `preprocess_image()`: Resizes image to 64×256, normalizes with ImageNet stats, returns NumPy array.
- `ctc_decode()`: Decodes CTC predictions using greedy decoding with NumPy operations.

**Features:**
- CORS enabled for frontend communication.
- Comprehensive error handling.
- Image validation (PNG, JPG, JPEG).
- ONNX Runtime session with CPU provider for fast inference.
- No GPU required - optimized for CPU performance.
- Inference time: 30-100ms per image on modern CPUs.

### Model Files:

#### `backend/models/best_model.onnx`
ONNX exported model for CPU-based inference:
- Model size: ~273MB.
- Optimized for ONNX Runtime CPU inference.
- Input shape: (1, 3, 64, 256) - batch_size=1, channels=3, height=64, width=256.
- Output: CTC predictions for CAPTCHA text recognition.
- Inference time: 30-100ms per image on modern CPUs.

#### `backend/export_to_onnx.py`
Reference script to convert PyTorch model to ONNX format (for reference only):
- Loads checkpoint from PyTorch model.
- Exports to ONNX format for CPU inference.
- Uses opset version 14 for compatibility.
- Note: The ONNX model is pre-exported and included with the project.

### Configuration:

#### `backend/config.json`
Model configuration:
- **Data:** Image dimensions (64×256), charset (62 characters).
- **Model:** Hidden size (512), attention heads (8), layers (4), dropout (0.1).
- **Inference:** ONNX model path and inference settings.

#### `backend/requirements.txt`
Python dependencies for ONNX Runtime CPU inference:
- Flask 3.0.0: Web framework.
- Flask-CORS 4.0.0: Cross-origin resource sharing support.
- onnxruntime 1.17.1: ONNX model inference engine (CPU-optimized).
- Pillow 10.1.0: Image processing and manipulation.
- numpy 1.24.3: Numerical operations and array handling.
- Note: PyTorch is NOT required for inference (only for model export).

## Documentation Files:

### `InstallationAndSetup.md`:
Comprehensive installation and setup guide:
- Prerequisites and required software.
- Automated and manual setup instructions.
- Running the application.
- Troubleshooting common issues.

### `Usage.md`:
User guide for the web application:
- How to navigate the interface.
- How to upload images and get predictions.
- Understanding the results.
- Tips for best results.

### `API.md`:
Backend API documentation:
- Endpoint specifications.
- Request/response formats.
- Example requests using curl and JavaScript.
- Error codes and messages.

### `CodeBaseIndex.md`:
This file - complete codebase structure and file descriptions.

## PowerShell Scripts:

### `setup.ps1`:
Automated setup script:
- Checks for Python and Node.js installation.
- Creates Python virtual environment.
- Installs backend dependencies.
- Installs frontend dependencies.
- Exports ONNX model if needed.

### `start.ps1`:
Application startup script:
- Starts Flask backend server in background.
- Starts Vite development server in background.
- Displays access URLs.
- Provides instructions for stopping servers.

## Reference Files:

### `README.md`:
Project README with:
- Project overview and features.
- Model architecture details.
- Performance metrics.
- Quick start guide.
- Links to detailed documentation and resources.

## Technology Stack:

### Frontend:
- **Framework:** React 19 with TypeScript.
- **Build Tool:** Vite 7.
- **Styling:** Tailwind CSS 3.
- **Icons:** Lucide React.
- **HTTP Client:** Axios.
- **Utilities:** clsx, tailwind-merge, class-variance-authority.

### Backend:
- **Framework:** Flask 3.0.0.
- **Inference:** ONNX Runtime 1.17.1 (CPU-optimized, no GPU required).
- **Image Processing:** Pillow 10.1.0, NumPy 1.24.3.
- **Deep Learning:** PyTorch 2.1 (for model export only, not required for inference).
- **CORS:** Flask-CORS 4.0.0 for frontend communication.

### Development Tools:
- **TypeScript:** Type-safe JavaScript.
- **ESLint:** Code linting.
- **PostCSS:** CSS processing.
- **Autoprefixer:** CSS vendor prefixing.

## Key Design Decisions:

1. **ONNX Runtime for CPU Inference:** Chosen for:
   - No GPU requirement (works on any CPU).
   - Faster inference than PyTorch (30-100ms per image).
   - Smaller deployment footprint (273MB model).
   - Cross-platform compatibility.

2. **Single-Page Application:** All sections on one scrollable page for better user experience.

3. **Dark/Light Theme:** Implemented using Tailwind's dark mode with class-based toggling and retro color scheme.

4. **Retro/Vintage Design:** Amber color palette (amber-50 to amber-950), Georgia serif font, 4px borders, box shadows, no rounded corners for authentic vintage aesthetic.

5. **Responsive Design:** Mobile-first approach with Tailwind's responsive utilities.

6. **Modular Architecture:** Clear separation between frontend and backend with RESTful API.

## Development Workflow:

1. **Frontend Development:**
   - Run `npm run dev` in the frontend directory.
   - Vite provides hot module replacement for instant updates.
   - Access at http://localhost:5173.

2. **Backend Development:**
   - Run `python app.py` in the backend directory.
   - Flask runs in debug mode for auto-reload.
   - Access API at http://localhost:5000.

3. **Building for Production:**
   - Frontend: `npm run build` creates optimized bundle in `dist/`.
   - Backend: Deploy Flask app with production WSGI server (e.g., Gunicorn).

## Future Enhancements:

Potential areas for expansion:
- Batch image processing.
- Model performance analytics dashboard.
- User authentication and history.
- Additional export formats (TensorFlow.js, TFLite).
- Real-time webcam capture for CAPTCHA solving.

