"""
Theme toggle button widget
"""
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QFont


class ThemeToggle(QPushButton):
    """Theme toggle button"""
    
    theme_changed = Signal(str)  # Emits 'dark' or 'light'
    
    def __init__(self):
        super().__init__()
        self.current_theme = "dark"
        self.setText("☀ Light Mode")
        self.setObjectName("theme-toggle")
        self.setStyleSheet("""
            QPushButton[class="theme-toggle"] {
                background-color: #9D4EDD;
                border: 2px solid #9D4EDD;
                color: #ffffff;
                padding: 8px 16px;
                border-radius: 0px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QPushButton[class="theme-toggle"]:hover {
                background-color: #C77DFF;
                border: 2px solid #C77DFF;
            }
            QPushButton[class="theme-toggle"]:pressed {
                background-color: #7B2CBF;
                border: 2px solid #7B2CBF;
            }
        """)
        
        font = QFont("Courier New", 11, QFont.Bold)
        self.setFont(font)
        
        self.clicked.connect(self.toggle_theme)
    
    def toggle_theme(self):
        """Toggle between dark and light theme"""
        if self.current_theme == "dark":
            self.current_theme = "light"
            self.setText("🌙 Dark Mode")
        else:
            self.current_theme = "dark"
            self.setText("☀ Light Mode")
        
        self.theme_changed.emit(self.current_theme)
    
    def set_theme(self, theme: str):
        """Set theme without emitting signal"""
        self.current_theme = theme
        if theme == "dark":
            self.setText("☀ Light Mode")
        else:
            self.setText("🌙 Dark Mode")

