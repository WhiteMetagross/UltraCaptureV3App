"""
ONNX model management and inference
"""
import time
import numpy as np
from pathlib import Path
from typing import Tuple
import onnxruntime as ort

from .image_processor import ImageProcessor
from .ctc_decoder import CTCDecoder
from .config_loader import ConfigLoader


class ModelManager:
    """Manage ONNX model loading and inference"""
    
    def __init__(self, model_path: Path, config_path: Path):
        """
        Initialize model manager
        
        Args:
            model_path: Path to ONNX model file
            config_path: Path to model configuration JSON
        """
        self.model_path = model_path
        self.config_loader = ConfigLoader(config_path)
        self.session = None
        self.charset = self.config_loader.get('charset', 
            "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        
        self._load_model()
    
    def _load_model(self):
        """Load ONNX model"""
        try:
            if not self.model_path.exists():
                raise FileNotFoundError(f"Model not found: {self.model_path}")
            
            # Create ONNX Runtime session with CPU provider
            self.session = ort.InferenceSession(
                str(self.model_path),
                providers=['CPUExecutionProvider']
            )
            print(f"Model loaded successfully: {self.model_path}")
            
        except Exception as e:
            raise RuntimeError(f"Error loading model: {e}")
    
    def predict(self, image_path: str) -> Tuple[str, float]:
        """
        Predict CAPTCHA text from image
        
        Args:
            image_path: Path to image file
            
        Returns:
            Tuple of (predicted_text, inference_time_ms)
        """
        try:
            # Validate image
            is_valid, error_msg = ImageProcessor.validate_image(image_path)
            if not is_valid:
                raise ValueError(error_msg)
            
            # Preprocess image
            image_array = ImageProcessor.preprocess(image_path)
            
            # Run inference
            start_time = time.time()
            
            input_name = self.session.get_inputs()[0].name
            output = self.session.run(None, {input_name: image_array})
            
            inference_time = (time.time() - start_time) * 1000  # Convert to ms
            
            # Decode predictions
            predictions = output[0]  # Get first output
            predicted_text = CTCDecoder.decode(predictions[0], self.charset)
            
            return predicted_text, inference_time
            
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {e}")
    
    def is_ready(self) -> bool:
        """Check if model is ready for inference"""
        return self.session is not None
    
    def get_config(self):
        """Get model configuration"""
        return self.config_loader.get_all()

