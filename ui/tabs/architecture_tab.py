"""
Architecture tab - Model technical details
"""
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class ArchitectureTab(QWidget):
    """Architecture tab with model details"""
    
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
        title = QLabel("MODEL ARCHITECTURE")
        title_font = QFont("Courier New", 32, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #00FF41;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(title)
        
        # Overview
        overview_frame = QFrame()
        overview_frame.setObjectName("card")
        overview_layout = QVBoxLayout()
        
        overview_title = QLabel("CRNN with Attention Mechanisms:")
        overview_title_font = QFont("Courier New", 16, QFont.Bold)
        overview_title.setFont(overview_title_font)
        overview_title.setStyleSheet("color: #9D4EDD;")
        overview_layout.addWidget(overview_title)
        
        overview_text = QLabel(
            "The model combines three main stages: feature extraction using CNN with CBAM attention, "
            "sequence modeling with Bi-LSTM, and long-range dependency capture with Transformer encoder. "
            "This hybrid approach achieves 95.08% character accuracy and 86.37% sequence accuracy."
        )
        overview_text.setFont(QFont("Courier New", 12))
        overview_text.setStyleSheet("color: #00FF41;")
        overview_text.setWordWrap(True)
        overview_layout.addWidget(overview_text)
        
        overview_frame.setLayout(overview_layout)
        scroll_layout.addWidget(overview_frame)
        
        # Three-stage flow
        stages_title = QLabel("Three-Stage Architecture Flow:")
        stages_title_font = QFont("Courier New", 16, QFont.Bold)
        stages_title.setFont(stages_title_font)
        stages_title.setStyleSheet("color: #9D4EDD;")
        scroll_layout.addWidget(stages_title)

        stages_frame = QFrame()
        stages_frame.setObjectName("card")
        stages_layout = QVBoxLayout()

        stages = [
            ("Stage 1: Feature Extraction", "Convolutional Neural Network with CBAM attention for robust image feature extraction."),
            ("Stage 2: Sequence Modeling", "Bidirectional LSTM and Transformer encoder for capturing temporal and long-range dependencies."),
            ("Stage 3: Decoding", "CTC loss function with greedy decoding for converting feature sequences into text predictions.")
        ]

        for stage_name, stage_desc in stages:
            stage_label = QLabel(f"• {stage_name}")
            stage_label_font = QFont("Courier New", 12, QFont.Bold)
            stage_label.setFont(stage_label_font)
            stage_label.setStyleSheet("color: #00FF41;")
            stages_layout.addWidget(stage_label)

            desc_label = QLabel(f"  {stage_desc}")
            desc_label.setFont(QFont("Courier New", 11))
            desc_label.setStyleSheet("color: #9D4EDD;")
            desc_label.setWordWrap(True)
            stages_layout.addWidget(desc_label)

        stages_frame.setLayout(stages_layout)
        scroll_layout.addWidget(stages_frame)
        
        # Components and hyperparameters
        details_layout = QHBoxLayout()
        details_layout.setSpacing(20)
        
        # Components
        components_frame = QFrame()
        components_frame.setObjectName("card")
        components_layout = QVBoxLayout()
        
        comp_title = QLabel("Model Components:")
        comp_title_font = QFont("Courier New", 14, QFont.Bold)
        comp_title.setFont(comp_title_font)
        comp_title.setStyleSheet("color: #9D4EDD;")
        components_layout.addWidget(comp_title)
        
        components = [
            "ResNet-style CNN backbone for robust feature extraction from images.",
            "CBAM attention module for channel and spatial feature refinement.",
            "Bidirectional LSTM for capturing temporal dependencies in sequences.",
            "Transformer encoder for modeling long-range dependencies effectively."
        ]
        
        for comp in components:
            comp_label = QLabel(comp)
            comp_label.setFont(QFont("Courier New", 12))
            comp_label.setStyleSheet("color: #00FF41;")
            components_layout.addWidget(comp_label)
        
        components_frame.setLayout(components_layout)
        details_layout.addWidget(components_frame)
        
        # Hyperparameters
        hyperparams_frame = QFrame()
        hyperparams_frame.setObjectName("card")
        hyperparams_layout = QVBoxLayout()
        
        hyper_title = QLabel("Hyperparameters:")
        hyper_title_font = QFont("Courier New", 14, QFont.Bold)
        hyper_title.setFont(hyper_title_font)
        hyper_title.setStyleSheet("color: #9D4EDD;")
        hyperparams_layout.addWidget(hyper_title)
        
        hyperparams = [
            "Hidden Size: 512",
            "Attention Heads: 8",
            "Transformer Layers: 4",
            "Dropout: 0.1",
            "Input Size: 64×256 pixels",
            "Charset: 62 characters (0-9, A-Z, a-z)"
        ]
        
        for param in hyperparams:
            param_label = QLabel(param)
            param_label.setFont(QFont("Courier New", 12))
            param_label.setStyleSheet("color: #0096FF;")
            hyperparams_layout.addWidget(param_label)
        
        hyperparams_frame.setLayout(hyperparams_layout)
        details_layout.addWidget(hyperparams_frame)
        
        scroll_layout.addLayout(details_layout)
        scroll_layout.addStretch()
        
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

