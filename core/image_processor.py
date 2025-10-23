"""
Image preprocessing for ONNX model inference
"""
import numpy as np
from PIL import Image
from pathlib import Path
from typing import Tuple


class ImageProcessor:
    """Handle image preprocessing for model input"""
    
    # ImageNet normalization statistics
    MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    
    @staticmethod
    def preprocess(image_path: str, target_height: int = 64, 
                   target_width: int = 256) -> np.ndarray:
        """
        Preprocess image for model inference
        
        Args:
            image_path: Path to image file
            target_height: Target image height
            target_width: Target image width
            
        Returns:
            Preprocessed image as numpy array (1, 3, H, W)
        """
        try:
            # Load image
            image = Image.open(image_path)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize image
            image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
            
            # Convert to numpy array
            image_array = np.array(image, dtype=np.float32)
            
            # Normalize to [0, 1]
            image_array = image_array / 255.0
            
            # Apply ImageNet normalization
            image_array = (image_array - ImageProcessor.MEAN) / ImageProcessor.STD
            
            # Convert to CHW format
            image_array = np.transpose(image_array, (2, 0, 1))
            
            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
            
        except Exception as e:
            raise ValueError(f"Error preprocessing image: {e}")
    
    @staticmethod
    def validate_image(image_path: str) -> Tuple[bool, str]:
        """
        Validate image file
        
        Args:
            image_path: Path to image file
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            path = Path(image_path)
            
            # Check file exists
            if not path.exists():
                return False, "File does not exist"
            
            # Check file extension
            valid_extensions = {'.png', '.jpg', '.jpeg'}
            if path.suffix.lower() not in valid_extensions:
                return False, f"Invalid file format. Supported: {valid_extensions}"
            
            # Try to open image
            with Image.open(image_path) as img:
                if img.size[0] < 10 or img.size[1] < 10:
                    return False, "Image too small"
            
            return True, ""
            
        except Exception as e:
            return False, f"Error validating image: {e}"

