"""
Image utility functions
"""
from PIL import Image
from pathlib import Path
from typing import Tuple


def load_image_as_pixmap(image_path: Path):
    """Load image and convert to QPixmap"""
    from PySide6.QtGui import QPixmap
    
    if not image_path.exists():
        return None
    
    try:
        pixmap = QPixmap(str(image_path))
        return pixmap
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def scale_pixmap(pixmap, max_width: int = 300, max_height: int = 300):
    """Scale pixmap to fit within max dimensions"""
    from PySide6.QtCore import Qt
    
    if pixmap is None:
        return None
    
    return pixmap.scaledToFit(max_width, max_height, Qt.AspectRatioMode.KeepAspectRatio)


def get_image_dimensions(image_path: Path) -> Tuple[int, int]:
    """Get image dimensions"""
    try:
        with Image.open(image_path) as img:
            return img.size
    except Exception:
        return (0, 0)


def is_image_valid(image_path: Path) -> bool:
    """Check if image file is valid"""
    try:
        with Image.open(image_path) as img:
            img.verify()
        return True
    except Exception:
        return False

