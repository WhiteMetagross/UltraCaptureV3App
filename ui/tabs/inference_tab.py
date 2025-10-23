"""
Inference tab - Live CAPTCHA prediction interface
"""
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                               QScrollArea, QProgressBar)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QPixmap

from ui.widgets import ImageUploadWidget, PredictionDisplay
from core import ModelManager
import config


class InferenceWorker(QThread):
    """Worker thread for model inference"""
    
    prediction_ready = Signal(str, float)  # prediction, time
    error_occurred = Signal(str)  # error message
    
    def __init__(self, model_manager: ModelManager, image_path: str):
        super().__init__()
        self.model_manager = model_manager
        self.image_path = image_path
    
    def run(self):
        """Run inference in background thread"""
        try:
            prediction, inference_time = self.model_manager.predict(self.image_path)
            self.prediction_ready.emit(prediction, inference_time)
        except Exception as e:
            self.error_occurred.emit(str(e))


class InferenceTab(QWidget):
    """Inference tab with live prediction"""
    
    def __init__(self, model_manager: ModelManager):
        super().__init__()
        self.model_manager = model_manager
        self.current_image_path = None
        self.inference_worker = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; background-color: #0a0e14; }")
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(10, 10, 10, 10)
        scroll_layout.setSpacing(20)
        
        # Title
        title = QLabel("LIVE INFERENCE DEMONSTRATION")
        title_font = QFont("Courier New", 32, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #00FF41;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(title)
        
        # Image upload widget
        self.upload_widget = ImageUploadWidget()
        self.upload_widget.image_loaded.connect(self.on_image_loaded)
        scroll_layout.addWidget(self.upload_widget)
        
        # Image preview
        self.image_preview = QLabel()
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setStyleSheet("color: #6b7280;")
        self.image_preview.setMinimumHeight(200)
        scroll_layout.addWidget(self.image_preview)
        
        # Predict button
        predict_btn = QPushButton("Predict CAPTCHA")
        predict_btn.setMinimumHeight(50)
        predict_btn.setFont(QFont("Courier New", 14, QFont.Bold))
        predict_btn.clicked.connect(self.on_predict_clicked)
        scroll_layout.addWidget(predict_btn)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #00FF41;
                background-color: #1a1f2e;
                text-align: center;
                color: #00FF41;
                font-family: 'Courier New', monospace;
                border-radius: 0px;
            }
            QProgressBar::chunk {
                background-color: #00FF41;
            }
        """)
        self.progress_bar.setVisible(False)
        scroll_layout.addWidget(self.progress_bar)
        
        # Prediction display
        self.prediction_display = PredictionDisplay()
        scroll_layout.addWidget(self.prediction_display)
        
        # Error message label
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: #FF3366;")
        self.error_label.setFont(QFont("Courier New", 12))
        self.error_label.setWordWrap(True)
        self.error_label.setVisible(False)
        scroll_layout.addWidget(self.error_label)
        
        # Clear button
        clear_btn = QPushButton("Clear")
        clear_btn.setMinimumHeight(40)
        clear_btn.setFont(QFont("Courier New", 12, QFont.Bold))
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF3333;
                color: #FFFFFF;
                border: 2px solid #FF0000;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF5555;
                border: 2px solid #FF3333;
            }
            QPushButton:pressed {
                background-color: #CC0000;
                border: 2px solid #990000;
            }
        """)
        clear_btn.clicked.connect(self.on_clear_clicked)
        scroll_layout.addWidget(clear_btn)
        
        scroll_layout.addStretch()
        
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
    
    def on_image_loaded(self, image_path: str):
        """Handle image loaded signal"""
        self.current_image_path = image_path
        
        # Display image preview
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(300, Qt.TransformationMode.SmoothTransformation)
        self.image_preview.setPixmap(pixmap)
        
        # Clear previous results
        self.error_label.setVisible(False)
        self.prediction_display.clear()
    
    def on_predict_clicked(self):
        """Handle predict button click"""
        if not self.current_image_path:
            self.show_error("Please select an image first")
            return
        
        if not self.model_manager.is_ready():
            self.show_error("Model is not ready")
            return
        
        # Show progress
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.error_label.setVisible(False)
        
        # Start inference in background thread
        self.inference_worker = InferenceWorker(self.model_manager, self.current_image_path)
        self.inference_worker.prediction_ready.connect(self.on_prediction_ready)
        self.inference_worker.error_occurred.connect(self.on_inference_error)
        self.inference_worker.start()
    
    def on_prediction_ready(self, prediction: str, inference_time: float):
        """Handle prediction ready signal"""
        self.progress_bar.setVisible(False)
        self.prediction_display.update_prediction(prediction, inference_time)
        self.error_label.setVisible(False)
    
    def on_inference_error(self, error_msg: str):
        """Handle inference error"""
        self.progress_bar.setVisible(False)
        self.show_error(f"Inference error: {error_msg}")
    
    def on_clear_clicked(self):
        """Handle clear button click"""
        self.current_image_path = None
        self.image_preview.clear()
        self.image_preview.setText("")
        self.prediction_display.clear()
        self.error_label.setVisible(False)
        self.progress_bar.setVisible(False)
    
    def show_error(self, message: str):
        """Show error message"""
        self.error_label.setText(message)
        self.error_label.setVisible(True)

