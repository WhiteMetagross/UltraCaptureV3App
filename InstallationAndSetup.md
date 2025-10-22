# Installation and Setup Guide:

This guide provides step-by-step instructions for setting up and running the UltraCaptureV3 web application.

## Prerequisites:

Before you begin, ensure you have the following installed on your system.

### Required Software:

1. **Node.js** (version 18.0 or higher).
   - Download from: https://nodejs.org/.
   - Verify installation: `node --version`.

2. **Python** (version 3.11 recommended, 3.8+ supported).
   - Download from: https://www.python.org/downloads/.
   - Verify installation: `python --version`.
   - **Note:** Python 3.11 is recommended for optimal ONNX Runtime performance.

3. **pip** (Python package installer).
   - Usually comes with Python.
   - Verify installation: `pip --version`.

4. **Git** (optional, for cloning the repository).
   - Download from: https://git-scm.com/.

### System Requirements:

- **CPU:** Any modern processor (Intel, AMD, ARM).
- **RAM:** Minimum 4GB (8GB recommended).
- **Storage:** At least 500MB free space for dependencies and models.
- **GPU:** Not required (CPU inference is fully supported).

## Installation Steps:

### Option 1: Automated Setup (Recommended):

The easiest way to set up the application is using the provided PowerShell script:

```powershell
.\setup.ps1
```

#### What the setup.ps1 Script Does.

The `setup.ps1` PowerShell script automates the entire setup process for both backend and frontend:

**Script Functionality:**
- Checks for Python 3.11 and Node.js installation on your system.
- Creates a Python virtual environment in the `backend` directory.
- Installs all backend dependencies (Flask, ONNX Runtime, Pillow, NumPy, Flask-CORS).
- Installs all frontend dependencies (React, Vite, Tailwind CSS, Axios).
- Verifies the ONNX model exists at `backend/models/best_model.onnx`.
- Displays status messages for each step ([OK] for success, [ERROR] for failures).

**Expected Output:**
```
UltraCaptureV3 Setup Script

Checking prerequisites...
[OK] Python 3.11 found
[OK] Node.js found

Setting up backend...
[OK] Virtual environment created
[OK] Backend dependencies installed

Setting up frontend...
[OK] Frontend dependencies installed

Verifying ONNX model...
[OK] ONNX model found at backend/models/best_model.onnx

Setup complete! You can now run .\start.ps1 to start the application.
```

**When to Use:**
- First-time setup of the project.
- After cloning the repository.
- When you need to reinstall dependencies.

**Troubleshooting:**
- If the script fails, check that Python 3.11 and Node.js are installed and accessible from the command line.
- Ensure you have administrator privileges to create virtual environments.
- If dependencies fail to install, try running the script again or use manual setup (Option 2).

### Option 2: Manual Setup:

If you prefer to set up manually or encounter issues with the automated script, follow these steps.

#### Backend Setup.

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

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

4. Install Python dependencies (ONNX Runtime for CPU inference):
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask 3.0.0 - Web framework.
   - Flask-CORS 4.0.0 - Cross-origin resource sharing.
   - ONNX Runtime 1.17.1 - CPU-based inference engine.
   - Pillow 10.1.0 - Image processing.
   - NumPy 1.24.3 - Numerical computing.

5. Verify the ONNX model exists:
   ```bash
   ls models/best_model.onnx
   ```

   The ONNX model should already be present in the `models/` directory. If not, contact the project maintainers.

#### Frontend Setup.

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Running the Application:

### Option 1: Automated Start (Recommended):

Use the provided PowerShell script to start both servers:

```powershell
.\start.ps1
```

#### What the start.ps1 Script Does.

The `start.ps1` PowerShell script launches both the backend and frontend servers simultaneously:

**Script Functionality:**
- Activates the Python virtual environment in the `backend` directory.
- Starts the Flask backend server on http://localhost:5000 with CPU-based ONNX inference.
- Starts the Vite frontend development server on http://localhost:5173.
- Displays the URLs for accessing the application.
- Keeps both servers running until you close the terminal windows.

**Expected Output:**
```
UltraCaptureV3 Start Script

Starting UltraCaptureV3...

Starting backend server (CPU-based ONNX inference)...
[OK] Backend server starting at http://localhost:5000
Starting frontend server...
[OK] Frontend server starting at http://localhost:5173

Application Started!

Access the application at:
  Frontend: http://localhost:5173
  Backend API: http://localhost:5000

To stop the servers:
  1. Close the backend PowerShell window (or press Ctrl+C)
  2. Close the frontend PowerShell window (or press Ctrl+C)
```

**When to Use:**
- Every time you want to run the application.
- After setup is complete.
- For development and testing.

**Stopping the Application:**
- Press `Ctrl+C` in each terminal window to stop the servers.
- Or close the terminal windows directly.

**Troubleshooting:**
- If the backend fails to start, ensure the ONNX model exists at `backend/models/best_model.onnx`.
- If the frontend fails to start, ensure all dependencies are installed with `npm install` in the frontend directory.
- If ports 5000 or 5173 are already in use, close other applications using those ports or modify the port numbers in the respective configuration files.

### Option 2: Manual Start:

If you prefer to start the servers manually:

#### Start the Backend Server.

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Activate the virtual environment (if not already activated):
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

   The backend API will be available at http://localhost:5000.

#### Start the Frontend Server.

1. Open a new terminal window.

2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at http://localhost:5173.

## Accessing the Application:

Once both servers are running:

1. Open your web browser.
2. Navigate to http://localhost:5173.
3. You should see the UltraCaptureV3 homepage.

## Stopping the Application:

### If using the automated start script:
- Press `Ctrl+C` in each terminal window to stop the servers.

### If running manually:
- Press `Ctrl+C` in the terminal running the backend server, and press `Ctrl+C` in the terminal running the frontend server.

## Troubleshooting:

### Backend Issues:

**Problem:** `ModuleNotFoundError` when starting the backend.
- **Solution:** Ensure you've activated the virtual environment and installed all dependencies with `pip install -r requirements.txt`.

**Problem:** `FileNotFoundError: ONNX model not found at models/best_model.onnx`.
- **Solution:** Ensure the ONNX model file exists in the `models/` directory, and the model should be pre-exported and included with the project.

**Problem:** `ImportError: No module named 'onnxruntime'`.
- **Solution:** Install ONNX Runtime with `pip install onnxruntime==1.17.1`.

**Problem:** Port 5000 is already in use.
- **Solution:** Either stop the process using port 5000, or modify the port in `backend/app.py` (change the last line to use a different port).

**Problem:** Slow inference times on CPU.
- **Solution:** This is normal for CPU inference. ONNX Runtime is optimized for CPU performance, and typical inference times are 30-100ms per image.

### Frontend Issues:

**Problem:** `npm install` fails with dependency conflicts.
- **Solution:** Try running `npm install --legacy-peer-deps`.

**Problem:** Port 5173 is already in use.
- **Solution:** Vite will automatically try the next available port, and check the terminal output for the actual URL.

**Problem:** "Failed to get prediction" error when uploading images.
- **Solution:** Ensure the backend server is running on http://localhost:5000, and check the browser console for detailed error messages.

### General Issues:

**Problem:** Images not displaying on the homepage.
- **Solution:** Ensure the profile images (`redZapdos.jpg` and `WhiteMetagross.jpg`) are present in the `frontend/public` directory.

**Problem:** CORS errors in the browser console.
- **Solution:** Ensure Flask-CORS is installed in the backend (`pip install Flask-CORS`), and the backend is running.

## Environment Configuration:

### Backend Configuration:

The backend configuration is stored in `backend/config.json`. Key settings include:

- `data.image_height`: Input image height (default: 64).
- `data.image_width`: Input image width (default: 256).
- `data.charset`: Character set for predictions.
- `model.*`: Model architecture hyperparameters.

### Frontend Configuration:

The frontend connects to the backend API at `http://localhost:5000`. If you need to change this:

1. Open `frontend/src/App.tsx`.
2. Find the `axios.post` call in the `handlePredict` function.
3. Update the URL to match your backend server address.

## Next Steps:

After successful installation and setup:

1. Read the [Usage Guide](Usage.md) to learn how to use the application.
2. Check the [API Documentation](API.md) for details on the backend API.
3. Explore the [Codebase Index](CodeBaseIndex.md) to understand the project structure.

## Support:

If you encounter issues not covered in this guide:

1. Check the GitHub repository for known issues: https://github.com/WhiteMetagross/CRNN_Captcha_Recognition.
2. Review the original README.md for additional context.
3. Ensure all prerequisites are correctly installed and up to date.

