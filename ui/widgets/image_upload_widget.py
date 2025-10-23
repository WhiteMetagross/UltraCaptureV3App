"""
Image upload widget with drag-and-drop support
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QFileDialog
from pathlib import Path


class ImageUploadWidget(QFrame):
    """Custom widget for drag-drop image upload"""
    
    image_loaded = Signal(str)  # Emits image path
    
    def __init__(self):
        super().__init__()
        self.setObjectName("upload-zone")
        self.setStyleSheet("""
            QFrame[class="upload-zone"] {
                background-color: #1a1f2e;
                border: 3px dashed #00FF41;
                padding: 30px;
                border-radius: 0px;
            }
        """)
        
        self.setAcceptDrops(True)
        self.setMinimumHeight(200)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Instructions label
        instructions = QLabel("Drag and drop a CAPTCHA image here to begin the prediction process.")
        instructions_font = QFont("Courier New", 16, QFont.Bold)
        instructions.setFont(instructions_font)
        instructions.setStyleSheet("color: #00FF41;")
        instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instructions.setWordWrap(True)

        # Or label
        or_label = QLabel("or")
        or_font = QFont("Courier New", 14)
        or_label.setFont(or_font)
        or_label.setStyleSheet("color: #9D4EDD;")
        or_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Browse button
        browse_btn = QPushButton("Browse and Select Image")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #2a3142;
                color: #00FF41;
                border: 2px solid #00FF41;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: #00FF41;
                color: #0a0e14;
            }
            QPushButton:pressed {
                background-color: #00CC33;
                border: 2px solid #00CC33;
            }
        """)
        browse_btn.clicked.connect(self.browse_file)

        # Supported formats label
        formats_label = QLabel("Supported image formats: PNG, JPG, and JPEG files.")
        formats_font = QFont("Courier New", 10)
        formats_label.setFont(formats_font)
        formats_label.setStyleSheet("color: #6b7280;")
        formats_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        formats_label.setWordWrap(True)
        
        layout.addStretch()
        layout.addWidget(instructions)
        layout.addWidget(or_label)
        layout.addWidget(browse_btn)
        layout.addWidget(formats_label)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Accept drag enter event for image files"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if self._is_valid_image(file_path):
                    event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop event"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if self._is_valid_image(file_path):
                    self.image_loaded.emit(file_path)
    
    def browse_file(self):
        """Open file dialog to select image"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Image Files (*.png *.jpg *.jpeg);;All Files (*)"
        )
        
        if file_path:
            self.image_loaded.emit(file_path)
    
    @staticmethod
    def _is_valid_image(file_path: str) -> bool:
        """Check if file is a valid image"""
        valid_extensions = {'.png', '.jpg', '.jpeg'}
        path = Path(file_path)
        return path.suffix.lower() in valid_extensions

