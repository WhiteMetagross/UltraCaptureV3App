import { useState, useEffect, memo } from 'react';
import { Moon, Sun, Github, Database, Upload, X } from 'lucide-react';
import axios from 'axios';
import './App.css';

// Performance optimizations:
// - Lazy loading for images (loading="lazy" attribute)
// - Code splitting in Vite config for vendor libraries
// - React.memo for component memoization
// - Optimized Vite build with minification and terser
// - Efficient state management with React hooks

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<string>('');
  const [inferenceTime, setInferenceTime] = useState<number>(0);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleImageSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedImage(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result as string);
      };
      reader.readAsDataURL(file);
      setPrediction('');
      setError('');
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const file = e.dataTransfer.files?.[0];
    if (file && (file.type === 'image/png' || file.type === 'image/jpeg' || file.type === 'image/jpg')) {
      setSelectedImage(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result as string);
      };
      reader.readAsDataURL(file);
      setPrediction('');
      setError('');
    }
  };

  const handlePredict = async () => {
    if (!selectedImage) return;

    setIsLoading(true);
    setError('');
    setPrediction('');

    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
      const response = await axios.post('http://localhost:5000/api/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setPrediction(response.data.prediction);
      setInferenceTime(response.data.inference_time);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to get prediction. Make sure the backend server is running.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setSelectedImage(null);
    setImagePreview(null);
    setPrediction('');
    setInferenceTime(0);
    setError('');
  };

  return (
    <div className={`min-h-screen ${darkMode ? 'dark' : ''}`}>
      <div className="bg-amber-50 dark:bg-amber-950 min-h-screen" style={{backgroundImage: 'repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(0,0,0,.03) 10px, rgba(0,0,0,.03) 20px)'}}>
        {/* Navigation */}
        <nav className="fixed top-0 w-full bg-amber-100/95 dark:bg-amber-900/95 backdrop-blur-sm z-50 border-b-4 border-amber-800 dark:border-amber-700 shadow-lg">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              <div className="flex items-center space-x-8">
                <h1 className="text-3xl font-black text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif', letterSpacing: '0.05em', textShadow: '2px 2px 0px rgba(0,0,0,0.1)'}}>
                  UltraCaptureV3
                </h1>
                <div className="hidden md:flex space-x-6">
                  <a href="#home" className="text-amber-900 dark:text-amber-100 hover:text-amber-700 dark:hover:text-amber-200 transition font-semibold" style={{fontFamily: 'Georgia, serif'}}>Home</a>
                  <a href="#about" className="text-amber-900 dark:text-amber-100 hover:text-amber-700 dark:hover:text-amber-200 transition font-semibold" style={{fontFamily: 'Georgia, serif'}}>About</a>
                  <a href="#architecture" className="text-amber-900 dark:text-amber-100 hover:text-amber-700 dark:hover:text-amber-200 transition font-semibold" style={{fontFamily: 'Georgia, serif'}}>Architecture</a>
                  <a href="#inference" className="text-amber-900 dark:text-amber-100 hover:text-amber-700 dark:hover:text-amber-200 transition font-semibold" style={{fontFamily: 'Georgia, serif'}}>Inference</a>
                </div>
              </div>
              <button
                onClick={() => setDarkMode(!darkMode)}
                className="p-2 rounded-lg bg-amber-200 dark:bg-amber-800 hover:bg-amber-300 dark:hover:bg-amber-700 transition border-2 border-amber-800 dark:border-amber-600"
              >
                {darkMode ? <Sun className="w-5 h-5 text-amber-900" /> : <Moon className="w-5 h-5 text-amber-900" />}
              </button>
            </div>
          </div>
        </nav>

        {/* Section 1: Hero/Home */}
        <section id="home" className="pt-32 pb-20 px-4">
          <div className="max-w-7xl mx-auto text-center">
            <h1 className="text-6xl md:text-8xl font-black mb-6 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif', letterSpacing: '0.02em', textShadow: '3px 3px 0px rgba(0,0,0,0.2)'}}>
              UltraCaptureV3.
            </h1>
            <p className="text-xl md:text-2xl text-amber-800 dark:text-amber-200 mb-8 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
              Advanced CRNN-Based CAPTCHA Recognition System.
            </p>
            <div className="flex flex-col md:flex-row justify-center items-center gap-8 mb-12">
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-6 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <p className="text-4xl font-black text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>95.08%</p>
                <p className="text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>Character Accuracy</p>
              </div>
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-6 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <p className="text-4xl font-black text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>86.37%</p>
                <p className="text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>Sequence Accuracy</p>
              </div>
            </div>
            <p className="text-lg text-amber-800 dark:text-amber-200 mb-12 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
              Created by Mridankan Mandal as part of Project AA
            </p>

            {/* Profile Cards */}
            <div className="flex flex-col md:flex-row justify-center items-center gap-8 mt-12">
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-6 shadow-lg border-4 border-amber-800 dark:border-amber-700 transform hover:scale-105 transition" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <img
                  src="/redZapdos.jpg"
                  alt="RedZapdos123"
                  loading="lazy"
                  className="w-32 h-32 rounded-none mx-auto mb-4 object-cover border-4 border-amber-800 dark:border-amber-700"
                />
                <p className="text-xl font-black text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>RedZapdos123</p>
              </div>
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-6 shadow-lg border-4 border-amber-800 dark:border-amber-700 transform hover:scale-105 transition" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <img
                  src="/WhiteMetagross.jpg"
                  alt="WhiteMetagross"
                  loading="lazy"
                  className="w-32 h-32 rounded-none mx-auto mb-4 object-cover border-4 border-amber-800 dark:border-amber-700"
                />
                <p className="text-xl font-black text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>WhiteMetagross</p>
              </div>
            </div>
          </div>
        </section>

        {/* Section 2: About */}
        <section id="about" className="py-20 px-4 bg-amber-100/50 dark:bg-amber-900/50 border-t-4 border-b-4 border-amber-800 dark:border-amber-700">
          <div className="max-w-7xl mx-auto">
            <h2 className="text-5xl font-black mb-12 text-center text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif', letterSpacing: '0.02em'}}>
              About the Project:
            </h2>
            <div className="grid md:grid-cols-2 gap-8 mb-12">
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <h3 className="text-2xl font-black mb-4 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>Overview:</h3>
                <p className="text-amber-800 dark:text-amber-200 leading-relaxed font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                  This project provides a complete, end-to-end pipeline for training and deploying a Deep Learning model
                  to solve complex CAPTCHA images. The solution uses a hybrid CRNN architecture with attention mechanisms,
                  achieves high accuracy, and demonstrates a full lifecycle from data preparation to deployment.
                </p>
              </div>
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <h3 className="text-2xl font-black mb-4 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>Key Features:</h3>
                <ul className="space-y-2 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 mr-2 font-black">▪</span>
                    <span>Hybrid architecture combining ResNet-style CNN, CBAM, Bi-LSTM, and Transformer.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 mr-2 font-black">▪</span>
                    <span>High accuracy: 95.08% character, 86.37% sequence.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 mr-2 font-black">▪</span>
                    <span>End-to-end workflow from data prep to deployment.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 mr-2 font-black">▪</span>
                    <span>Advanced augmentation with albumentations library.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 mr-2 font-black">▪</span>
                    <span>Deployment-ready with ONNX export.</span>
                  </li>
                </ul>
              </div>
            </div>

            {/* Links */}
            <div className="flex flex-col md:flex-row justify-center gap-6 mb-12">
              <a
                href="https://github.com/WhiteMetagross/CRNN_Captcha_Recognition"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 bg-amber-800 dark:bg-amber-700 text-amber-50 px-8 py-4 rounded-none hover:bg-amber-700 dark:hover:bg-amber-600 transition shadow-lg border-4 border-amber-900 dark:border-amber-800 font-black" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.3)', fontFamily: 'Georgia, serif'}}
              >
                <Github className="w-6 h-6" />
                <span>View on GitHub</span>
              </a>
              <a
                href="https://www.kaggle.com/datasets/redzapdos123/huge-captcha-dataset"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 bg-amber-700 dark:bg-amber-600 text-amber-50 px-8 py-4 rounded-none hover:bg-amber-600 dark:hover:bg-amber-500 transition shadow-lg border-4 border-amber-900 dark:border-amber-800 font-black" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.3)', fontFamily: 'Georgia, serif'}}
              >
                <Database className="w-6 h-6" />
                <span>Dataset on Kaggle</span>
              </a>
            </div>

            {/* Performance Table */}
            <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
              <h3 className="text-2xl font-black mb-6 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>Performance Metrics:</h3>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b-4 border-amber-800 dark:border-amber-700 bg-amber-200 dark:bg-amber-800">
                      <th className="text-left py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>Metric</th>
                      <th className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>Validation Set</th>
                      <th className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>Test Set</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b-2 border-amber-800 dark:border-amber-700">
                      <td className="py-3 px-4 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>Sequence Accuracy</td>
                      <td className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>86.4%</td>
                      <td className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>86.37%</td>
                    </tr>
                    <tr>
                      <td className="py-3 px-4 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>Character Accuracy</td>
                      <td className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>95.1%</td>
                      <td className="text-center py-3 px-4 text-amber-900 dark:text-amber-100 font-black" style={{fontFamily: 'Georgia, serif'}}>95.08%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <p className="mt-6 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                <strong>Training Performance:</strong> ~11 minutes per epoch on RTX 4060 GPU (8GB VRAM) with mixed-precision training.
              </p>
            </div>

            {/* Training Metrics Graph */}
            <div className="mt-12 bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
              <h3 className="text-2xl font-black mb-6 text-amber-900 dark:text-amber-100 text-center" style={{fontFamily: 'Georgia, serif'}}>Training and Validation Metrics Graphs:</h3>
              <div className="flex justify-center">
                <img
                  src="/TrainingMetrics.png"
                  alt="Training and Validation Metrics Graphs"
                  loading="lazy"
                  className="max-w-full h-auto rounded-none border-4 border-amber-800 dark:border-amber-700"
                  style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}
                />
              </div>
              <p className="mt-6 text-center text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                Visualization of model performance across training epochs showing convergence and validation accuracy trends.
              </p>
            </div>
          </div>
        </section>

        {/* Section 3: Model Architecture */}
        <section id="architecture" className="py-20 px-4 bg-amber-100/50 dark:bg-amber-900/50 border-t-4 border-b-4 border-amber-800 dark:border-amber-700">
          <div className="max-w-7xl mx-auto">
            <h2 className="text-5xl font-black mb-12 text-center text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif', letterSpacing: '0.02em'}}>
              Model Architecture:
            </h2>

            <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700 mb-8" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
              <h3 className="text-2xl font-black mb-4 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>CRNN with Attention:</h3>
              <p className="text-amber-800 dark:text-amber-200 leading-relaxed mb-6 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                The model is a custom-built Convolutional Recurrent Neural Network (CRNN) that integrates multiple
                advanced concepts to maximize accuracy. It's structured in two primary stages:
              </p>

              {/* Architecture Flow */}
              <div className="grid md:grid-cols-3 gap-6 mb-8">
                <div className="bg-amber-200 dark:bg-amber-800 rounded-none p-6 border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.2)'}}>
                  <h4 className="text-xl font-black text-amber-900 dark:text-amber-100 mb-3" style={{fontFamily: 'Georgia, serif'}}>Stage 1: Feature Extraction.</h4>
                  <p className="text-amber-800 dark:text-amber-200 text-sm font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                    Deep CNN with ResNet-style residual blocks enhanced with CBAM attention mechanism.
                  </p>
                </div>
                <div className="bg-amber-200 dark:bg-amber-800 rounded-none p-6 border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.2)'}}>
                  <h4 className="text-xl font-black text-amber-900 dark:text-amber-100 mb-3" style={{fontFamily: 'Georgia, serif'}}>Stage 2: Sequence Modeling.</h4>
                  <p className="text-amber-800 dark:text-amber-200 text-sm font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                    Bidirectional LSTM processes feature sequences, refined by Transformer Encoder.
                  </p>
                </div>
                <div className="bg-amber-200 dark:bg-amber-800 rounded-none p-6 border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.2)'}}>
                  <h4 className="text-xl font-black text-amber-900 dark:text-amber-100 mb-3" style={{fontFamily: 'Georgia, serif'}}>Loss Function.</h4>
                  <p className="text-amber-800 dark:text-amber-200 text-sm font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                    CTC (Connectionist Temporal Classification) for unsegmented sequence learning.
                  </p>
                </div>
              </div>
            </div>

            {/* Technical Specifications */}
            <div className="grid md:grid-cols-2 gap-8">
              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <h3 className="text-2xl font-black mb-4 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>Components:</h3>
                <ul className="space-y-3 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 font-black mr-2">1.</span>
                    <span><strong>Convolutional Backbone:</strong> ResNet-style CNN with residual connections.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 font-black mr-2">2.</span>
                    <span><strong>CBAM Attention:</strong> Channel and spatial attention mechanisms.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 font-black mr-2">3.</span>
                    <span><strong>Bi-LSTM:</strong> Bidirectional LSTM for temporal dependencies.</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-amber-900 dark:text-amber-100 font-black mr-2">4.</span>
                    <span><strong>Transformer Encoder:</strong> Self-attention for long-range dependencies.</span>
                  </li>
                </ul>
              </div>

              <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
                <h3 className="text-2xl font-black mb-4 text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif'}}>Hyperparameters:</h3>
                <ul className="space-y-2 text-amber-800 dark:text-amber-200 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                  <li><strong>Hidden Size:</strong> 512</li>
                  <li><strong>Attention Heads:</strong> 8</li>
                  <li><strong>Transformer Layers:</strong> 4</li>
                  <li><strong>Dropout:</strong> 0.1</li>
                  <li><strong>Input Size:</strong> 64×256 pixels</li>
                  <li><strong>Charset:</strong> 62 characters (0-9, A-Z, a-z)</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* Section 4: Live Inference Demonstration */}
        <section id="inference" className="py-20 px-4 bg-amber-100/50 dark:bg-amber-900/50">
          <div className="max-w-4xl mx-auto">
            <h2 className="text-5xl font-black mb-12 text-center text-amber-900 dark:text-amber-100" style={{fontFamily: 'Georgia, serif', letterSpacing: '0.02em'}}>
              Live Inference Demonstration:
            </h2>

            <div className="bg-amber-100 dark:bg-amber-900 rounded-none p-8 shadow-lg border-4 border-amber-800 dark:border-amber-700" style={{boxShadow: '6px 6px 0px rgba(0,0,0,0.2)'}}>
              {/* Upload Area */}
              <div
                onDrop={handleDrop}
                onDragOver={(e) => e.preventDefault()}
                className="border-4 border-dashed border-amber-800 dark:border-amber-700 rounded-none p-12 text-center hover:border-amber-600 dark:hover:border-amber-500 transition cursor-pointer bg-amber-50 dark:bg-amber-950"
              >
                {!imagePreview ? (
                  <div>
                    <Upload className="w-16 h-16 mx-auto mb-4 text-amber-800 dark:text-amber-200" />
                    <p className="text-xl text-amber-800 dark:text-amber-200 mb-2 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                      Drag and drop your CAPTCHA image here.
                    </p>
                    <p className="text-sm text-amber-700 dark:text-amber-300 mb-4 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
                      Or click to browse (PNG, JPG, JPEG).
                    </p>
                    <label className="inline-block">
                      <input
                        type="file"
                        accept="image/png,image/jpeg,image/jpg"
                        onChange={handleImageSelect}
                        className="hidden"
                      />
                      <span className="bg-amber-800 dark:bg-amber-700 text-amber-50 px-6 py-3 rounded-none hover:bg-amber-700 dark:hover:bg-amber-600 transition cursor-pointer inline-block border-2 border-amber-900 dark:border-amber-800 font-black" style={{boxShadow: '3px 3px 0px rgba(0,0,0,0.2)', fontFamily: 'Georgia, serif'}}>
                        Choose File
                      </span>
                    </label>
                  </div>
                ) : (
                  <div className="relative">
                    <img
                      src={imagePreview}
                      alt="Preview"
                      className="max-w-full max-h-64 mx-auto rounded-none shadow-lg border-4 border-amber-800 dark:border-amber-700"
                    />
                    <button
                      onClick={handleClear}
                      className="absolute top-2 right-2 bg-amber-800 dark:bg-amber-700 text-amber-50 p-2 rounded-none hover:bg-amber-700 dark:hover:bg-amber-600 transition border-2 border-amber-900 dark:border-amber-800"
                    >
                      <X className="w-5 h-5" />
                    </button>
                  </div>
                )}
              </div>

              {/* Predict Button */}
              {selectedImage && !prediction && (
                <div className="mt-6 text-center">
                  <button
                    onClick={handlePredict}
                    disabled={isLoading}
                    className="bg-amber-800 dark:bg-amber-700 text-amber-50 px-8 py-4 rounded-none hover:bg-amber-700 dark:hover:bg-amber-600 transition disabled:bg-amber-400 disabled:cursor-not-allowed text-lg font-black shadow-lg border-2 border-amber-900 dark:border-amber-800" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.3)', fontFamily: 'Georgia, serif'}}
                  >
                    {isLoading ? 'Processing...' : 'Predict CAPTCHA'}
                  </button>
                </div>
              )}

              {/* Error Message */}
              {error && (
                <div className="mt-6 bg-amber-200 dark:bg-amber-800 border-4 border-amber-800 dark:border-amber-700 rounded-none p-4" style={{boxShadow: '3px 3px 0px rgba(0,0,0,0.2)'}}>
                  <p className="text-amber-900 dark:text-amber-100 text-center font-semibold" style={{fontFamily: 'Georgia, serif'}}>{error}</p>
                </div>
              )}

              {/* Prediction Result */}
              {prediction && (
                <div className="mt-6 space-y-4">
                  <div className="bg-amber-200 dark:bg-amber-800 border-4 border-amber-800 dark:border-amber-700 rounded-none p-6" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.2)'}}>
                    <p className="text-sm text-amber-800 dark:text-amber-200 mb-2 font-semibold" style={{fontFamily: 'Georgia, serif'}}>Prediction:</p>
                    <p className="text-4xl font-black text-amber-900 dark:text-amber-100 text-center tracking-wider" style={{fontFamily: 'Georgia, serif'}}>
                      {prediction}
                    </p>
                  </div>
                  <div className="bg-amber-200 dark:bg-amber-800 border-4 border-amber-800 dark:border-amber-700 rounded-none p-4" style={{boxShadow: '4px 4px 0px rgba(0,0,0,0.2)'}}>
                    <p className="text-amber-900 dark:text-amber-100 text-center font-black" style={{fontFamily: 'Georgia, serif'}}>
                      <strong>Inference Time:</strong> {inferenceTime} ms.
                    </p>
                  </div>
                  <div className="text-center">
                    <button
                      onClick={handleClear}
                      className="bg-amber-800 dark:bg-amber-700 text-amber-50 px-6 py-3 rounded-none hover:bg-amber-700 dark:hover:bg-amber-600 transition border-2 border-amber-900 dark:border-amber-800 font-black" style={{boxShadow: '3px 3px 0px rgba(0,0,0,0.2)', fontFamily: 'Georgia, serif'}}
                    >
                      Try Another Image
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="py-8 px-4 bg-amber-900 dark:bg-amber-950 text-amber-50 border-t-4 border-amber-800 dark:border-amber-700">
          <div className="max-w-7xl mx-auto text-center">
            <p className="text-amber-100 font-semibold" style={{fontFamily: 'Georgia, serif'}}>
              © 2025 UltraCaptureV3 | Created by Mridankan Mandal | Project AA.
            </p>
          </div>
        </footer>
      </div>
    </div>
  );
}

export default App;
