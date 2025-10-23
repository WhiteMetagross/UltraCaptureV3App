"""
File utility functions
"""
from pathlib import Path
from typing import List


def get_image_files(directory: Path) -> List[Path]:
    """Get all image files in directory"""
    valid_extensions = {'.png', '.jpg', '.jpeg'}
    return [f for f in directory.glob('*') if f.suffix.lower() in valid_extensions]


def ensure_directory(path: Path) -> Path:
    """Ensure directory exists, create if necessary"""
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_file_size_mb(file_path: Path) -> float:
    """Get file size in MB"""
    if file_path.exists():
        return file_path.stat().st_size / (1024 * 1024)
    return 0.0


def is_valid_image_file(file_path: Path) -> bool:
    """Check if file is a valid image"""
    valid_extensions = {'.png', '.jpg', '.jpeg'}
    return file_path.suffix.lower() in valid_extensions

