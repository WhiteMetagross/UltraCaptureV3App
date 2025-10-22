from flask import Flask, request, jsonify
from flask_cors import CORS
import onnxruntime as ort
import numpy as np
from PIL import Image
import io
import json
import time
import os
import sys

app = Flask(__name__)
CORS(app)

# Load configuration.
with open('config.json', 'r') as f:
    config = json.load(f)

# Load ONNX model.
model_path = 'models/best_model.onnx'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")

# Create ONNX Runtime session with CPU provider.
session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
print(f"Using device: CPU")
print(f"ONNX Runtime version: {ort.__version__}")

charset = config['data']['charset']
image_height = config['data']['image_height']
image_width = config['data']['image_width']
blank_idx = len(charset)

# ImageNet normalization parameters.
MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

def preprocess_image(image_bytes):
    """
    Preprocesses the uploaded image for model inference.
    Resizes to 64x256, converts to RGB, normalizes with ImageNet stats.
    Returns a numpy array for ONNX Runtime inference.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))

        # Convert to RGB if necessary.
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize to model input size.
        image = image.resize((image_width, image_height), Image.LANCZOS)

        # Convert to numpy array and normalize to [0, 1].
        image_array = np.array(image, dtype=np.float32) / 255.0

        # Apply ImageNet normalization.
        image_array = (image_array - MEAN) / STD

        # Transpose to CHW format and add batch dimension.
        image_array = np.transpose(image_array, (2, 0, 1))
        image_array = np.expand_dims(image_array, axis=0)

        return image_array
    except Exception as e:
        raise ValueError(f"Error preprocessing image: {str(e)}")

def ctc_decode(predictions):
    """
    Decodes CTC predictions to text using greedy decoding.
    Predictions should be raw model output (logits) as numpy array.
    Removes consecutive duplicates and blank labels.
    """
    # Apply log softmax and get argmax.
    # predictions shape: (1, sequence_length, vocab_size)
    log_probs = predictions - np.max(predictions, axis=2, keepdims=True)
    log_probs = log_probs - np.log(np.sum(np.exp(log_probs), axis=2, keepdims=True))
    pred_indices = np.argmax(log_probs, axis=2)

    # Decode the first (and only) sample in the batch.
    decoded = []
    prev_idx = None
    for idx in pred_indices[0]:
        if idx != prev_idx and idx != blank_idx:
            decoded.append(int(idx))
        prev_idx = idx

    # Convert indices to characters.
    text = ''.join([charset[idx] for idx in decoded if 0 <= idx < len(charset)])

    return text

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Endpoint for captcha prediction.
    Accepts an image file and returns the predicted text.
    """
    try:
        # Check if image file is present in request.
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        file = request.files['image']

        # Check if file has a valid filename.
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Check file extension.
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
        if file_ext not in allowed_extensions:
            return jsonify({'error': f'Invalid file type. Allowed types: {", ".join(allowed_extensions)}'}), 400

        # Read image bytes.
        image_bytes = file.read()

        # Preprocess image and run inference.
        start_time = time.time()
        input_array = preprocess_image(image_bytes)

        # Run ONNX Runtime model inference.
        input_name = session.get_inputs()[0].name
        output = session.run(None, {input_name: input_array})

        # Decode predictions.
        predicted_text = ctc_decode(output[0])

        inference_time = time.time() - start_time

        return jsonify({
            'prediction': predicted_text,
            'inference_time': round(inference_time * 1000, 2)
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    """
    return jsonify({'status': 'healthy', 'model_loaded': True}), 200

if __name__ == '__main__':
    print("Starting UltraCaptureV3 Flask Backend (ONNX Runtime CPU)...")
    print(f"Model loaded from: {model_path}")
    print(f"Device: CPU")
    print(f"Charset: {charset}")
    print(f"Image size: {image_height}x{image_width}")
    print(f"Blank index: {blank_idx}")
    app.run(host='0.0.0.0', port=5000, debug=True)

