# API Documentation:

This document provides comprehensive documentation for the UltraCaptureV3 backend API.

## Base URL:

When running locally:
```
http://localhost:5000
```

## API Endpoints:

### 1. Predict CAPTCHA:

Accepts an image file and returns the predicted CAPTCHA text.

**Endpoint:** `POST /api/predict`

**Request Format:**
- **Method:** POST.
- **Content-Type:** multipart/form-data.
- **Body:** Form data with an image file.

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| image | File | Yes | CAPTCHA image file (PNG, JPG, or JPEG) |

**Response Format:**

**Success Response (200 OK):**
```json
{
  "prediction": "aB3xY9",
  "inference_time": 145.23
}
```

| Field | Type | Description |
|-------|------|-------------|
| prediction | string | Predicted CAPTCHA text |
| inference_time | float | Inference time in milliseconds |

**Error Responses:**

**400 Bad Request - No image provided:**
```json
{
  "error": "No image file provided"
}
```

**400 Bad Request - No file selected:**
```json
{
  "error": "No file selected"
}
```

**400 Bad Request - Invalid file type:**
```json
{
  "error": "Invalid file type. Allowed types: png, jpg, jpeg"
}
```

**400 Bad Request - Image preprocessing error:**
```json
{
  "error": "Error preprocessing image: <error details>"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal server error: <error details>"
}
```

**Example Request (cURL):**

```bash
curl -X POST http://localhost:5000/api/predict \
  -F "image=@/path/to/captcha.png"
```

**Example Request (JavaScript/Fetch):**

```javascript
const formData = new FormData();
formData.append('image', fileInput.files[0]);

fetch('http://localhost:5000/api/predict', {
  method: 'POST',
  body: formData
})
  .then(response => response.json())
  .then(data => {
    console.log('Prediction:', data.prediction);
    console.log('Inference Time:', data.inference_time, 'ms');
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

**Example Request (Python/requests):**

```python
import requests

url = 'http://localhost:5000/api/predict'
files = {'image': open('captcha.png', 'rb')}

response = requests.post(url, files=files)
data = response.json()

print(f"Prediction: {data['prediction']}")
print(f"Inference Time: {data['inference_time']} ms")
```

**Example Request (Axios):**

```javascript
import axios from 'axios';

const formData = new FormData();
formData.append('image', imageFile);

axios.post('http://localhost:5000/api/predict', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
})
  .then(response => {
    console.log('Prediction:', response.data.prediction);
    console.log('Inference Time:', response.data.inference_time, 'ms');
  })
  .catch(error => {
    console.error('Error:', error.response?.data?.error || error.message);
  });
```

### 2. Health Check:

Checks if the API server is running and the model is loaded.

**Endpoint:** `GET /api/health`

**Request Format:**
- **Method:** GET.
- **No parameters required.**

**Response Format:**

**Success Response (200 OK):**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| status | string | Server status ("healthy") |
| model_loaded | boolean | Whether the ONNX model is loaded |

**Example Request (cURL):**

```bash
curl http://localhost:5000/api/health
```

**Example Request (JavaScript/Fetch):**

```javascript
fetch('http://localhost:5000/api/health')
  .then(response => response.json())
  .then(data => {
    console.log('Status:', data.status);
    console.log('Model Loaded:', data.model_loaded);
  });
```

## Image Processing Details:

### Input Requirements:

**Supported Formats:**
- PNG (.png).
- JPEG (.jpg, .jpeg).

**Image Preprocessing:**
1. **Conversion:** Image is converted to RGB if not already.
2. **Resizing:** Image is resized to 256×64 pixels using Lanczos resampling.
3. **Normalization:** Pixel values are normalized to [0, 1] range.
4. **Standardization:** ImageNet normalization is applied:
   - Mean: [0.485, 0.456, 0.406].
   - Std: [0.229, 0.224, 0.225].
5. **Format Conversion:** Image is transposed to CHW format (Channels, Height, Width).
6. **Batch Dimension:** A batch dimension is added (shape: 1×3×64×256).

### Output Format:

**Prediction:**
- String containing the predicted CAPTCHA text.
- Characters are from the charset: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`.
- Length varies depending on the CAPTCHA (typically 4-8 characters).

**Inference Time:**
- Measured in milliseconds.
- Includes preprocessing, model inference, and CTC decoding.
- Typical range: 30-100ms on modern CPUs with ONNX Runtime.
- ONNX Runtime provides optimized CPU inference without GPU requirements.

## CTC Decoding:

The model uses Connectionist Temporal Classification (CTC) for sequence prediction.

**Decoding Process:**
1. Model outputs a probability distribution over characters for each timestep.
2. Greedy decoding selects the most likely character at each timestep.
3. Consecutive duplicate characters are removed.
4. Blank labels (index 0) are removed.
5. Remaining indices are mapped to characters using the charset.

**Example:**
- Raw output: [0, 10, 10, 0, 11, 0, 3, 3, 0].
- After removing blanks and duplicates: [10, 11, 3].
- Mapped to charset: "A" (index 10), "B" (index 11), "3" (index 3).
- Final prediction: "AB3".

## Error Handling:

### Client Errors (4xx):

**400 Bad Request:**
- Missing image file.
- Invalid file type.
- Image preprocessing errors.

**Handling:**
- Check that the request includes a valid image file.
- Ensure the file format is PNG, JPG, or JPEG.
- Verify the image is not corrupted.

### Server Errors (5xx):

**500 Internal Server Error:**
- ONNX Runtime errors.
- Unexpected exceptions during processing.

**Handling:**
- Check backend logs for detailed error messages.
- Ensure the ONNX model file exists at `backend/models/best_model.onnx`.
- Verify ONNX Runtime is correctly installed: `pip install onnxruntime==1.17.1`.
- Ensure the model file is not corrupted (should be ~273MB).

## CORS Configuration:

The API is configured with CORS (Cross-Origin Resource Sharing) to allow requests from the frontend.

**Allowed Origins:**
- All origins (`*`) in development mode.

**Allowed Methods:**
- GET, POST.

**Allowed Headers:**
- Content-Type.

**Note:** For production deployment, restrict allowed origins to your frontend domain.

## Rate Limiting:

Currently, the API does not implement rate limiting. For production use, consider adding:
- Request rate limiting per IP address.
- Maximum file size limits.
- Request timeout limits.

## Performance Considerations:

### Inference Speed:

**Factors Affecting Speed:**
1. **CPU Performance:** Faster CPUs provide quicker inference (typical: 30-100ms).
2. **Image Size:** Larger images take longer to preprocess.
3. **Model Complexity:** The CRNN model is relatively lightweight (~273MB).
4. **ONNX Runtime Optimizations:** ONNX Runtime applies various CPU optimizations.

**Optimization Tips:**
- ONNX Runtime is already optimized for CPU inference (no GPU required).
- Typical inference time: 30-100ms per image on modern CPUs.
- Batch multiple requests if processing many images.
- ONNX Runtime automatically uses multi-threading for CPU optimization.

### Scalability:

**Current Limitations:**
- Single-threaded Flask development server.
- No request queuing or load balancing.

**Production Recommendations:**
- Use a production WSGI server (e.g., Gunicorn, uWSGI).
- Deploy behind a reverse proxy (e.g., Nginx).
- Implement request queuing for high load.
- Consider horizontal scaling with multiple backend instances.

## Security Considerations:

### Input Validation:

The API validates:
- File presence in the request.
- File extension (PNG, JPG, JPEG).

**Additional Recommendations:**
- Validate file size (implement maximum size limit).
- Validate image dimensions.
- Scan uploaded files for malware.
- Implement request authentication for production.

### Data Privacy:

**Current Implementation:**
- Uploaded images are processed in memory.
- No images are saved to disk.
- No user data is logged.

**Production Recommendations:**
- Implement HTTPS for encrypted communication.
- Add user authentication and authorization.
- Log requests for monitoring (without storing images).
- Comply with data privacy regulations (GDPR, CCPA, etc.).

## Integration Examples:

### React Application:

```typescript
import axios from 'axios';

const predictCaptcha = async (imageFile: File) => {
  const formData = new FormData();
  formData.append('image', imageFile);

  try {
    const response = await axios.post('http://localhost:5000/api/predict', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return {
      prediction: response.data.prediction,
      inferenceTime: response.data.inference_time,
    };
  } catch (error: any) {
    throw new Error(error.response?.data?.error || 'Prediction failed');
  }
};
```

### Node.js Application:

```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const predictCaptcha = async (imagePath) => {
  const formData = new FormData();
  formData.append('image', fs.createReadStream(imagePath));

  try {
    const response = await axios.post('http://localhost:5000/api/predict', formData, {
      headers: formData.getHeaders(),
    });
    return response.data;
  } catch (error) {
    console.error('Error:', error.response?.data?.error || error.message);
    throw error;
  }
};

predictCaptcha('./captcha.png')
  .then(data => {
    console.log('Prediction:', data.prediction);
    console.log('Inference Time:', data.inference_time, 'ms');
  });
```

### Python Script:

```python
import requests
import sys

def predict_captcha(image_path):
    url = 'http://localhost:5000/api/predict'
    
    with open(image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        data = response.json()
        return data['prediction'], data['inference_time']
    else:
        error = response.json().get('error', 'Unknown error')
        raise Exception(f"Prediction failed: {error}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    prediction, inference_time = predict_captcha(image_path)
    print(f"Prediction: {prediction}")
    print(f"Inference Time: {inference_time} ms")
```

## Troubleshooting:

### Common Issues:

**Issue:** CORS errors in browser console.
- **Solution:** Ensure Flask-CORS is installed and configured in `backend/app.py`.

**Issue:** "Connection refused" error.
- **Solution:** Ensure the backend server is running on port 5000.

**Issue:** Slow inference times (>1 second).
- **Solution:** Check CPU usage. Ensure ONNX Runtime is installed correctly.

**Issue:** "ONNX model not found" error.
- **Solution:** Ensure the ONNX model file exists at `backend/models/best_model.onnx`. The model should be pre-exported and included with the project.

## API Versioning:

**Current Version:** v1 (implicit).

**Future Considerations:**
- Implement explicit API versioning (e.g., `/api/v1/predict`).
- Maintain backward compatibility when adding new features.
- Document breaking changes clearly.

## Support:

For API-related issues:
1. Check the backend terminal for error logs.
2. Review this documentation for correct usage.
3. Consult the [Installation and Setup Guide](InstallationAndSetup.md).
4. Visit the GitHub repository: https://github.com/WhiteMetagross/CRNN_Captcha_Recognition.

