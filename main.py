"""
UltraCaptureV3 Desktop Application
Main entry point
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt

from ui.main_window import MainWindow
from core import ModelManager
from utils import logger
import config


def main():
    """Main application entry point"""
    try:
        # Create application
        app = QApplication(sys.argv)
        
        # Set application style
        app.setStyle('Fusion')
        
        logger.info(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
        
        # Check if model exists
        if not config.MODEL_PATH.exists():
            logger.error(f"Model not found: {config.MODEL_PATH}")
            QMessageBox.critical(
                None,
                "Error",
                f"Model file not found:\n{config.MODEL_PATH}\n\n"
                "Please ensure the ONNX model is in the resources/models directory."
            )
            return 1
        
        logger.info(f"Loading model from: {config.MODEL_PATH}")
        
        # Initialize model manager
        model_manager = ModelManager(config.MODEL_PATH, config.CONFIG_PATH)
        
        if not model_manager.is_ready():
            logger.error("Model failed to load")
            QMessageBox.critical(
                None,
                "Error",
                "Failed to load the ONNX model.\n\n"
                "Please check that the model file is valid and all dependencies are installed."
            )
            return 1
        
        logger.info("Model loaded successfully")
        
        # Create main window
        window = MainWindow(model_manager)
        window.show()
        
        logger.info("Application started successfully")
        
        # Run application
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        QMessageBox.critical(
            None,
            "Fatal Error",
            f"An unexpected error occurred:\n{e}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())

