"""
Main application window
"""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QFont

from ui.tabs.home_tab import HomeTab
from ui.tabs.about_tab import AboutTab
from ui.tabs.architecture_tab import ArchitectureTab
from ui.tabs.inference_tab import InferenceTab
from core import ModelManager
import config


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, model_manager: ModelManager):
        super().__init__()
        self.model_manager = model_manager
        self.settings = QSettings("UltraCaptureV3", "UltraCaptureV3")
        
        self.setWindowTitle(f"{config.APP_NAME} v{config.APP_VERSION}")
        self.setGeometry(100, 100, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.setMinimumSize(config.MIN_WINDOW_WIDTH, config.MIN_WINDOW_HEIGHT)

        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #00FF41;
                background-color: #1a1f2e;
                border-radius: 0px;
            }
            QTabBar::tab {
                background-color: #2a3142;
                color: #00FF41;
                border: 2px solid #00FF41;
                border-bottom: none;
                padding: 10px 20px;
                margin-right: 2px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QTabBar::tab:selected {
                background-color: #00FF41;
                color: #0a0e14;
            }
            QTabBar::tab:hover {
                background-color: #00CC33;
                color: #0a0e14;
            }
        """)
        
        # Create tabs
        self.home_tab = HomeTab()
        self.about_tab = AboutTab()
        self.architecture_tab = ArchitectureTab()
        self.inference_tab = InferenceTab(self.model_manager)
        
        self.tab_widget.addTab(self.home_tab, "Home")
        self.tab_widget.addTab(self.about_tab, "About")
        self.tab_widget.addTab(self.architecture_tab, "Architecture")
        self.tab_widget.addTab(self.inference_tab, "Inference")
        
        main_layout.addWidget(self.tab_widget)
        
        central_widget.setLayout(main_layout)
        
        # Apply stylesheet
        self.apply_stylesheet()
    
    def apply_stylesheet(self):
        """Apply QSS stylesheet"""
        try:
            with open(config.THEME_STYLESHEET, 'r') as f:
                stylesheet = f.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet: {e}")
    
    def closeEvent(self, event):
        """Handle window close event"""
        # Save window geometry
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        event.accept()

