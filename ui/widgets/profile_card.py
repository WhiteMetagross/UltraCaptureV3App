"""
Profile card widget for displaying creator profiles
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path


class ProfileCard(QFrame):
    """Creator profile card with image"""
    
    def __init__(self, image_path: Path, name: str):
        super().__init__()
        self.setObjectName("profile-card")
        self.setStyleSheet("""
            QFrame[class="profile-card"] {
                background-color: #2a3142;
                border: 2px solid #9D4EDD;
                padding: 15px;
                border-radius: 0px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        
        # Image label
        image_label = QLabel()
        if image_path and Path(image_path).exists():
            pixmap = QPixmap(str(image_path))
            pixmap = pixmap.scaledToWidth(150, Qt.TransformationMode.SmoothTransformation)
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("[Image Not Found]")
            image_label.setStyleSheet("color: #FF3366;")
        
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Name label
        name_label = QLabel(name)
        name_font = QFont("Courier New", 14, QFont.Bold)
        name_label.setFont(name_font)
        name_label.setStyleSheet("color: #00FF41;")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(image_label)
        layout.addWidget(name_label)
        
        self.setLayout(layout)

