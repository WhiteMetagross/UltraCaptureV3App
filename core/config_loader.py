"""
Configuration loader for model settings
"""
import json
from pathlib import Path
from typing import Dict, Any


class ConfigLoader:
    """Load and manage model configuration"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            if not self.config_path.exists():
                return self._get_default_config()
            
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration"""
        return {
            "image_height": 64,
            "image_width": 256,
            "charset": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "hidden_size": 512,
            "attention_heads": 8,
            "transformer_layers": 4,
            "dropout": 0.1,
            "model_accuracy": {
                "character": 95.08,
                "sequence": 86.37
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration"""
        return self.config.copy()

