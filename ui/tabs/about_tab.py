"""
About tab - Project information and metrics
"""
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, 
                               QPushButton, QTableWidget, QTableWidgetItem, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
import webbrowser
from pathlib import Path

import config


class AboutTab(QWidget):
    """About tab with project information"""
    
    def __init__(self):
        super().__init__()
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
        title = QLabel("ABOUT THE PROJECT")
        title_font = QFont("Courier New", 32, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #00FF41;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(title)
        
        # Overview section
        overview_frame = QFrame()
        overview_frame.setObjectName("card")
        overview_layout = QVBoxLayout()
        
        overview_title = QLabel("Overview:")
        overview_title_font = QFont("Courier New", 16, QFont.Bold)
        overview_title.setFont(overview_title_font)
        overview_title.setStyleSheet("color: #9D4EDD;")
        overview_layout.addWidget(overview_title)
        
        overview_text = QLabel(
            "UltraCaptureV3 is a complete CAPTCHA recognition system using a hybrid "
            "CRNN architecture with attention mechanisms. The system combines deep convolutional "
            "neural networks with recurrent layers and transformer encoders for accurate text recognition."
        )
        overview_text.setFont(QFont("Courier New", 12))
        overview_text.setStyleSheet("color: #00FF41;")
        overview_text.setWordWrap(True)
        overview_layout.addWidget(overview_text)
        
        overview_frame.setLayout(overview_layout)
        scroll_layout.addWidget(overview_frame)

        # Creator information
        creator_frame = QFrame()
        creator_frame.setObjectName("card")
        creator_layout = QHBoxLayout()
        creator_layout.setContentsMargins(10, 10, 10, 10)
        creator_layout.setSpacing(10)

        creator_label = QLabel("Created by:")
        creator_label.setFont(QFont("Courier New", 12, QFont.Bold))
        creator_label.setStyleSheet("color: #9D4EDD;")
        creator_layout.addWidget(creator_label)

        creator_name = QLabel("Mridankan Mandal")
        creator_name.setFont(QFont("Courier New", 12))
        creator_name.setStyleSheet("color: #00FF41;")
        creator_layout.addWidget(creator_name)

        creator_layout.addSpacing(20)

        year_label = QLabel("Year:")
        year_label.setFont(QFont("Courier New", 12, QFont.Bold))
        year_label.setStyleSheet("color: #9D4EDD;")
        creator_layout.addWidget(year_label)

        year_value = QLabel("2025")
        year_value.setFont(QFont("Courier New", 12))
        year_value.setStyleSheet("color: #00FF41;")
        creator_layout.addWidget(year_value)

        creator_layout.addStretch()
        creator_frame.setLayout(creator_layout)
        scroll_layout.addWidget(creator_frame)

        # Key features
        features_frame = QFrame()
        features_frame.setObjectName("card")
        features_layout = QVBoxLayout()
        
        features_title = QLabel("Key Features:")
        features_title_font = QFont("Courier New", 16, QFont.Bold)
        features_title.setFont(features_title_font)
        features_title.setStyleSheet("color: #9D4EDD;")
        features_layout.addWidget(features_title)
        
        features = [
            "The system uses a hybrid CRNN architecture with a ResNet-style CNN backbone for robust feature extraction.",
            "CBAM attention mechanisms provide channel and spatial focus to improve model accuracy.",
            "Bidirectional LSTM layers capture temporal dependencies in the CAPTCHA text sequences.",
            "A transformer encoder processes long-range dependencies for enhanced text recognition.",
            "The model is deployed in ONNX format for optimal performance and cross-platform compatibility."
        ]
        
        for feature in features:
            feature_label = QLabel(feature)
            feature_label.setFont(QFont("Courier New", 12))
            feature_label.setStyleSheet("color: #00FF41;")
            features_layout.addWidget(feature_label)
        
        features_frame.setLayout(features_layout)
        scroll_layout.addWidget(features_frame)
        
        # External links
        links_layout = QHBoxLayout()
        links_layout.setSpacing(10)
        
        github_btn = QPushButton("GitHub Repository")
        github_btn.clicked.connect(lambda: webbrowser.open("https://github.com"))
        
        kaggle_btn = QPushButton("Kaggle Dataset")
        kaggle_btn.clicked.connect(lambda: webbrowser.open("https://kaggle.com"))
        
        links_layout.addWidget(github_btn)
        links_layout.addWidget(kaggle_btn)
        scroll_layout.addLayout(links_layout)
        
        # Performance metrics table
        metrics_title = QLabel("Performance Metrics:")
        metrics_title_font = QFont("Courier New", 16, QFont.Bold)
        metrics_title.setFont(metrics_title_font)
        metrics_title.setStyleSheet("color: #9D4EDD;")
        scroll_layout.addWidget(metrics_title)

        # Create a container frame for the metrics description
        metrics_frame = QFrame()
        metrics_frame.setObjectName("card")
        metrics_layout = QVBoxLayout()
        metrics_layout.setContentsMargins(15, 15, 15, 15)
        metrics_layout.setSpacing(12)

        # First sentence - Sequence Accuracy
        seq_accuracy_text = QLabel(
            "The model achieved a sequence accuracy of <span style='color: #00CCFF; font-weight: bold;'>86.4%</span> "
            "on validation data and <span style='color: #00CCFF; font-weight: bold;'>86.37%</span> on test data."
        )
        seq_accuracy_text.setFont(QFont("Courier New", 12))
        seq_accuracy_text.setStyleSheet("color: #00FF41;")
        seq_accuracy_text.setWordWrap(True)
        seq_accuracy_text.setTextFormat(Qt.TextFormat.RichText)
        metrics_layout.addWidget(seq_accuracy_text)

        # Second sentence - Character Accuracy
        char_accuracy_text = QLabel(
            "Character-level accuracy reached <span style='color: #00CCFF; font-weight: bold;'>95.1%</span> "
            "for validation and <span style='color: #00CCFF; font-weight: bold;'>95.08%</span> for test sets."
        )
        char_accuracy_text.setFont(QFont("Courier New", 12))
        char_accuracy_text.setStyleSheet("color: #00FF41;")
        char_accuracy_text.setWordWrap(True)
        char_accuracy_text.setTextFormat(Qt.TextFormat.RichText)
        metrics_layout.addWidget(char_accuracy_text)

        # Third sentence - Summary
        summary_text = QLabel(
            "These metrics demonstrate the model's strong performance in recognizing CAPTCHA text with high accuracy "
            "across both sequence-level and character-level predictions."
        )
        summary_text.setFont(QFont("Courier New", 12))
        summary_text.setStyleSheet("color: #00FF41;")
        summary_text.setWordWrap(True)
        summary_text.setTextFormat(Qt.TextFormat.RichText)
        metrics_layout.addWidget(summary_text)

        metrics_frame.setLayout(metrics_layout)
        scroll_layout.addWidget(metrics_frame)
        
        # Training metrics image
        if config.TRAINING_METRICS.exists():
            metrics_img_frame = QFrame()
            metrics_img_frame.setObjectName("card")
            metrics_img_layout = QVBoxLayout()
            metrics_img_layout.setContentsMargins(10, 10, 10, 10)
            metrics_img_layout.setSpacing(10)

            metrics_img_label = QLabel()
            pixmap = QPixmap(str(config.TRAINING_METRICS))
            pixmap = pixmap.scaledToWidth(1100, Qt.TransformationMode.SmoothTransformation)
            metrics_img_label.setPixmap(pixmap)
            metrics_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            metrics_img_layout.addWidget(metrics_img_label)

            # Add description below the image
            description = QLabel(
                "The graph displays training and validation metrics across epochs, showing the model's "
                "convergence behavior and generalization performance on both sequence accuracy and character accuracy metrics."
            )
            description.setFont(QFont("Courier New", 14))
            description.setStyleSheet("color: #00CCFF;")
            description.setWordWrap(True)
            description.setAlignment(Qt.AlignmentFlag.AlignCenter)
            metrics_img_layout.addWidget(description)

            metrics_img_frame.setLayout(metrics_img_layout)
            scroll_layout.addWidget(metrics_img_frame)
        
        scroll_layout.addStretch()
        
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

