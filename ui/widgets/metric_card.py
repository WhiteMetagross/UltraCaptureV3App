"""
Metric card widget for displaying metrics
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MetricCard(QFrame):
    """Reusable metric display card"""
    
    def __init__(self, value: str, label: str, color: str = "#0096FF"):
        super().__init__()
        self.setObjectName("metric-card")
        self.setStyleSheet(f"""
            QFrame[class="metric-card"] {{
                background-color: #1a1f2e;
                border: 3px solid {color};
                padding: 20px;
                border-radius: 0px;
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        
        # Value label
        value_label = QLabel(value)
        value_font = QFont("Courier New", 32, QFont.Bold)
        value_label.setFont(value_font)
        value_label.setStyleSheet(f"color: {color};")
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Description label
        desc_label = QLabel(label)
        desc_font = QFont("Courier New", 14)
        desc_label.setFont(desc_font)
        desc_label.setStyleSheet("color: #9D4EDD;")
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(value_label)
        layout.addWidget(desc_label)
        
        self.setLayout(layout)

