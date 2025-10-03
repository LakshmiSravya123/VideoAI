# 🎬 AI Video Generator - Hailuo Clone

A powerful AI video generation platform with multiple backend options. Generate stunning videos from text prompts using state-of-the-art AI models!

![AI Video Generator](https://img.shields.io/badge/AI-Video%20Generation-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🎥 **Multiple AI Models** - CogVideoX, Hailuo Video-01, HunyuanVideo
- 🚀 **3 Backend Options** - Replicate API, Local Generation, or HF Spaces
- 🎨 **Advanced Controls** - Camera movements, visual effects, styles (Hailuo-inspired)
- 💻 **Beautiful UI** - Modern, responsive web interface
- 🔒 **Privacy Options** - Run completely locally or use cloud APIs
- ⚡ **Fast Generation** - 30-60 seconds with Replicate, or run locally

## 🎯 Quick Start (3 Options)

### Option 1: Replicate API (Recommended - Most Reliable)

**Best for:** Fast, reliable video generation with minimal setup

1. **Get Replicate API Token**
   ```bash
   # Sign up at https://replicate.com
   # Get token from https://replicate.com/account/api-tokens
   ```

2. **Setup**
   ```bash
   # Clone the repo
   git clone <your-repo-url>
   cd hailuo-clone
   
   # Create .env file
   echo "REPLICATE_API_TOKEN=your_token_here" > .env
   
   # Install dependencies
   pip install -r requirements.txt
   pip install replicate
   
   # Run backend
   python backend_replicate.py
   ```

3. **Open UI**
   - Open `index.html` in your browser
   - Enter a prompt and generate!

**Cost:** ~$0.05-0.10 per video

---

### Option 2: Local Generation (Free & Private)

**Best for:** Complete privacy, offline use, no API costs

1. **Install PyTorch**
   ```bash
   # For GPU (NVIDIA)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   
   # For CPU only
   pip install torch torchvision torchaudio
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements_local.txt
   ```

3. **Run**
   ```bash
   # Start backend
   python backend_local.py
   
   # Open index_local.html in browser
   ```

**Requirements:**
- GPU: RTX 3060+ (30-120s per video)
- CPU: 16GB RAM (5-10 min per video)
- Storage: 10GB for model

---

### Option 3: Hugging Face Spaces (Free but Unreliable)

**Best for:** Testing, no setup required

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run**
   ```bash
   python backend_enhanced.py
   # Open index_enhanced.html
   ```

**Note:** HF Spaces may be sleeping/overloaded. Use Demo Mode for testing.

---

## 📁 Project Structure

```
hailuo-clone/
├── Backend Options
│   ├── backend_replicate.py      # Replicate API (recommended)
│   ├── backend_local.py           # Local generation
│   ├── backend_enhanced.py        # HF Spaces (multiple models)
│   └── backend_simple.py          # Demo mode
│
├── Frontend
│   ├── index.html                 # Simple UI (works with all backends)
│   ├── index_enhanced.html        # Advanced UI with camera controls
│   └── index_local.html           # Local generation UI
│
├── Configuration
│   ├── models_config.py           # Model configurations
│   ├── requirements.txt           # Basic dependencies
│   ├── requirements_local.txt     # Local generation dependencies
│   └── .env.example               # Environment variables template
│
└── Documentation
    ├── README.md                  # This file
    ├── SOLUTION_GUIDE.md          # Troubleshooting guide
    └── README_LOCAL.md            # Local setup guide
```

## 🎨 Available Models

### Replicate API
- **Hailuo Video-01** (MiniMax) - The real Hailuo model! 🔥
- **CogVideoX-5B** - High quality text-to-video

### Local Generation
- **CogVideoX-2B** - Runs on your computer

### Hugging Face Spaces
- **CogVideoX-5B** - High quality (when available)
- **CogVideoX-2B** - Faster version
- **HunyuanVideo** - Tencent's SOTA model
- **Stable Video Diffusion** - Image-to-video

## 🎬 Usage Examples

### Basic Text-to-Video
```python
# Using any backend on localhost:5000
import requests

response = requests.post('http://localhost:5000/generate-video', json={
    'prompt': 'A golden retriever running through a field of flowers at sunset'
})

video_url = response.json()['video_url']
```

### With Replicate (Specific Model)
```python
response = requests.post('http://localhost:5000/generate-video', json={
    'prompt': 'A cat playing with yarn',
    'model': 'hailuo'  # or 'cogvideox'
})
```

### Advanced (Camera Controls)
```python
response = requests.post('http://localhost:5000/generate-video', json={
    'prompt': 'Ocean waves at sunset',
    'camera_movement': '[Zoom in]',
    'visual_effect': 'cinematic lighting, film grain',
    'style': 'photorealistic, 4k, high detail'
})
```

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Replicate API
REPLICATE_API_TOKEN=your_token_here

# Flask Configuration
FLASK_PORT=5000
FLASK_DEBUG=False

# Model Selection
DEFAULT_MODEL=cogvideox-5b
```

### Model Configuration (models_config.py)
- Camera movements (zoom, pan, tilt, etc.)
- Visual effects (cinematic, dramatic, slow-motion)
- Video styles (realistic, anime, 3D render)
- Example prompts by category

## 📊 Performance Comparison

| Backend | Setup Time | Speed | Quality | Cost | Reliability |
|---------|-----------|-------|---------|------|-------------|
| **Replicate** | 5 min | 30-60s | ⭐⭐⭐⭐⭐ | $0.05-0.10 | ⭐⭐⭐⭐⭐ |
| **Local (GPU)** | 30 min | 30-120s | ⭐⭐⭐⭐ | Free | ⭐⭐⭐⭐⭐ |
| **Local (CPU)** | 30 min | 5-10 min | ⭐⭐⭐⭐ | Free | ⭐⭐⭐⭐⭐ |
| **HF Spaces** | Instant | 30-60s | ⭐⭐⭐⭐ | Free | ⭐⭐ |

## 🚀 Deployment

### Local Development
```bash
python backend_replicate.py
# Open http://localhost:5000
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend_replicate:app
```

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "backend_replicate.py"]
```

## 🐛 Troubleshooting

### "Model provider unreachable"
- **Solution:** Use Replicate API (`backend_replicate.py`) instead of HF Spaces
- HF Spaces are often sleeping/overloaded

### "Out of memory" (Local)
- **Solution:** Use CPU mode or reduce batch size
- Close other GPU applications

### "Too slow" (Local CPU)
- **Expected:** CPU generation takes 5-10 minutes
- **Solution:** Use Replicate API or get a GPU

### Port 5000 already in use
- **Solution:** Kill the process or change port in backend file

See [SOLUTION_GUIDE.md](SOLUTION_GUIDE.md) for detailed troubleshooting.

## 📚 Documentation

- [SOLUTION_GUIDE.md](SOLUTION_GUIDE.md) - Complete troubleshooting guide
- [README_LOCAL.md](README_LOCAL.md) - Local generation setup
- [REPLICATE_SETUP.md](REPLICATE_SETUP.md) - Replicate API setup
- [QUICKSTART_LOCAL.md](QUICKSTART_LOCAL.md) - Quick local setup

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [CogVideoX](https://github.com/THUDM/CogVideo) by Tsinghua University
- [Hailuo Video-01](https://replicate.com/minimax/video-01) by MiniMax
- [Replicate](https://replicate.com) for API infrastructure
- [Hugging Face](https://huggingface.co) for model hosting

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

## 📞 Support

- **Issues:** [GitHub Issues](your-repo-url/issues)
- **Discussions:** [GitHub Discussions](your-repo-url/discussions)
- **Email:** your-email@example.com

---

**Made with ❤️ for the AI video generation community**
