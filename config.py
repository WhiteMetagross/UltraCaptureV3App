"""
Application configuration and constants
"""
import os
from pathlib import Path

# Application paths
BASE_DIR = Path(__file__).parent
RESOURCES_DIR = BASE_DIR / "resources"
MODELS_DIR = RESOURCES_DIR / "models"
IMAGES_DIR = RESOURCES_DIR / "images"
CONFIG_DIR = RESOURCES_DIR / "config"
STYLES_DIR = BASE_DIR / "ui" / "styles"

# Model configuration
MODEL_PATH = MODELS_DIR / "best_model.onnx"
CONFIG_PATH = CONFIG_DIR / "model_config.json"

# Image paths
PROFILE_REDZAPDOS = IMAGES_DIR / "redZapdos.jpg"
PROFILE_WHITEMETAGROSS = IMAGES_DIR / "WhiteMetagross.jpg"
TRAINING_METRICS = IMAGES_DIR / "TrainingMetrics.png"

# Application settings
APP_NAME = "UltraCaptureV3"
APP_VERSION = "1.0.0"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MIN_WINDOW_WIDTH = 800
MIN_WINDOW_HEIGHT = 600

# Theme settings
DEFAULT_THEME = "dark"
THEME_STYLESHEET = STYLES_DIR / "fallout_theme.qss"

# Model settings
IMAGE_HEIGHT = 64
IMAGE_WIDTH = 256
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ALLOWED_IMAGE_FORMATS = [".png", ".jpg", ".jpeg"]

# ImageNet normalization stats
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

# Inference settings
INFERENCE_TIMEOUT = 10  # seconds
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

