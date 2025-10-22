import torch
import os
import json
from model import CRNN

def export_model_to_onnx():
    device = torch.device('cpu')
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    print("Initializing model...")
    model = CRNN(
        vocab_size=len(config['data']['charset']),
        hidden_size=config['model']['hidden_size'],
        attention_heads=config['model']['attention_heads'],
        num_layers=config['model']['num_layers'],
        dropout=config['model']['dropout']
    )
    
    model_path = config['paths']['model_save']
    print(f"Loading model from {model_path}...")
    
    try:
        checkpoint = torch.load(model_path, map_location=device, weights_only=True)
        if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'])
        else:
            model.load_state_dict(checkpoint)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return False
    
    model.eval()
    
    dummy_input = torch.randn(
        1,
        3,
        config['data']['image_height'],
        config['data']['image_width'],
        device=device
    )
    
    onnx_path = 'models/captcha_solver.onnx'
    os.makedirs(os.path.dirname(onnx_path), exist_ok=True)
    
    try:
        print(f"Exporting model to ONNX format at {onnx_path}...")
        torch.onnx.export(
            model,
            dummy_input,
            onnx_path,
            export_params=True,
            opset_version=14,
            do_constant_folding=True,
            input_names=['input'],
            output_names=['output'],
            dynamic_axes={
                'input': {0: 'batch_size'},
                'output': {0: 'batch_size'}
            }
        )
        print(f"Model successfully exported to {onnx_path}.")
        return True
    except Exception as e:
        print(f"Error during ONNX export: {e}")
        return False

if __name__ == "__main__":
    success = export_model_to_onnx()
    exit(0 if success else 1)

