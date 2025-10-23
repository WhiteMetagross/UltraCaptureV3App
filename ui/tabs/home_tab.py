"""
Home tab - Hero/landing content
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from pathlib import Path

from ui.widgets import MetricCard, ProfileCard
import config


class HomeTab(QWidget):
    """Home tab with hero content and metrics"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Scroll area for content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #0a0e14;
            }
        """)
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(10, 10, 10, 10)
        scroll_layout.setSpacing(30)
        
        # Title
        title = QLabel("ULTRACAPTUREV3")
        title_font = QFont("Courier New", 48, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #00FF41; text-shadow: 0px 0px 10px #00FF41;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(title)
        
        # Tagline
        tagline = QLabel("Advanced CRNN-Based CAPTCHA Recognition System")
        tagline_font = QFont("Courier New", 18)
        tagline.setFont(tagline_font)
        tagline.setStyleSheet("color: #9D4EDD;")
        tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(tagline)
        
        # Metrics container
        metrics_layout = QHBoxLayout()
        metrics_layout.setSpacing(20)
        
        char_metric = MetricCard("95.08%", "Character Accuracy", "#0096FF")
        seq_metric = MetricCard("86.37%", "Sequence Accuracy", "#00FF41")
        
        metrics_layout.addWidget(char_metric)
        metrics_layout.addWidget(seq_metric)
        scroll_layout.addLayout(metrics_layout)
        
        # Creator info
        creator_label = QLabel("Created by Mridankan Mandal")
        creator_font = QFont("Courier New", 14)
        creator_label.setFont(creator_font)
        creator_label.setStyleSheet("color: #00FF41;")
        creator_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(creator_label)
        
        project_label = QLabel("Project AA")
        project_font = QFont("Courier New", 12)
        project_label.setFont(project_font)
        project_label.setStyleSheet("color: #6b7280;")
        project_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(project_label)
        
        # Profile cards
        profiles_layout = QHBoxLayout()
        profiles_layout.setSpacing(20)
        
        profile1 = ProfileCard(config.PROFILE_REDZAPDOS, "RedZapdos123")
        profile2 = ProfileCard(config.PROFILE_WHITEMETAGROSS, "WhiteMetagross")
        
        profiles_layout.addWidget(profile1)
        profiles_layout.addWidget(profile2)
        scroll_layout.addLayout(profiles_layout)
        
        scroll_layout.addStretch()
        
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

