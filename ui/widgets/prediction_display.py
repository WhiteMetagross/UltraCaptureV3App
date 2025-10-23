"""
Prediction display widget
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class PredictionDisplay(QFrame):
    """Display prediction results"""
    
    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.setStyleSheet("""
            QFrame[class="card"] {
                background-color: #2a3142;
                border: 2px solid #00FF41;
                padding: 15px;
                border-radius: 0px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Prediction label
        pred_title = QLabel("Predicted CAPTCHA Text:")
        pred_title_font = QFont("Courier New", 12)
        pred_title.setFont(pred_title_font)
        pred_title.setStyleSheet("color: #9D4EDD;")

        self.prediction_label = QLabel("")
        pred_font = QFont("Courier New", 28, QFont.Bold)
        pred_font.setLetterSpacing(QFont.PercentageSpacing, 110)  # 10% extra spacing
        self.prediction_label.setFont(pred_font)
        self.prediction_label.setStyleSheet("""
            color: #00FF41;
            letter-spacing: 2px;
            line-height: 1.5;
        """)
        self.prediction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.prediction_label.setMinimumHeight(80)

        # Inference time label
        time_title = QLabel("Model Inference Time:")
        time_title_font = QFont("Courier New", 12)
        time_title.setFont(time_title_font)
        time_title.setStyleSheet("color: #9D4EDD;")

        self.time_label = QLabel("")
        time_font = QFont("Courier New", 14)
        self.time_label.setFont(time_font)
        self.time_label.setStyleSheet("color: #0096FF;")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(pred_title)
        layout.addWidget(self.prediction_label)
        layout.addWidget(time_title)
        layout.addWidget(self.time_label)
        
        self.setLayout(layout)
    
    def update_prediction(self, text: str, time_ms: float):
        """Update prediction display"""
        display_text = text if text else "No prediction"
        self.prediction_label.setText(display_text)
        self.time_label.setText(f"{time_ms:.2f} ms")
    
    def clear(self):
        """Clear prediction display"""
        self.prediction_label.setText("")
        self.time_label.setText("")

