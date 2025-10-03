# 🎬 AI Video Generator Pro - Hailuo-Inspired Edition

A powerful, feature-rich AI video generation application inspired by Hailuo AI, supporting multiple state-of-the-art models from Hugging Face.

## ✨ Key Features

### 🎯 Multiple Generation Modes
- **Text-to-Video**: Create videos from text descriptions
- **Image-to-Video**: Animate static images with AI

### 🤖 Multiple AI Models
- **CogVideoX-5B**: High-quality 6-second videos at 720p
- **LTX Video**: Fast and efficient generation
- **Stable Video Diffusion**: Professional image animation
- **AnimateDiff**: Advanced motion control
- **Zeroscope V2 XL**: Fast and reliable baseline

### 🎥 Hailuo-Inspired Features
- **Camera Movements**: Zoom, pan, tilt, tracking shots, dolly, crane, shake
- **Visual Effects**: Cinematic lighting, fog, rain, slow motion
- **Video Styles**: Realistic, anime, cartoon, 3D render, vintage, sci-fi, fantasy
- **Enhanced Prompts**: Automatic prompt enhancement with cinematic tags

## 🚀 Quick Start

### Installation

```bash
cd /Users/sravyalu/VideoAI/hailuo-clone
pip install -r requirements.txt
```

### Running

**Enhanced version (recommended)**:
```bash
python backend_enhanced.py
```
Then open `index_enhanced.html` in your browser.

**Basic version**:
```bash
python backend.py
```
Then open `index.html` in your browser.

## 📖 Usage Guide

### Text-to-Video
1. Select "Text to Video" mode
2. Choose an AI model
3. Enter your prompt (3-1000 characters)
4. Add camera movements, effects, or styles (optional)
5. Click "Generate Video"
6. Wait 30-120 seconds
7. Download or share

### Image-to-Video
1. Select "Image to Video" mode
2. Upload an image
3. Add animation prompt (optional)
4. Select image-to-video model
5. Generate

## 🎯 Example Prompts

**Nature**: "A majestic waterfall cascading down mossy rocks in a lush rainforest"

**Action**: "A sports car drifting around a corner" + Camera: [Tracking shot]

**Fantasy**: "A dragon flying over a medieval castle at dawn" + Style: fantasy, magical

## 🛠️ Available Models

| Model | Type | Resolution | Best For |
|-------|------|------------|----------|
| CogVideoX-5B | T2V | 720x480 | High quality |
| LTX Video | T2V | 704x480 | Fast generation |
| Stable Video Diffusion | I2V | 576x576 | Image animation |
| AnimateDiff | I2V | 512x512 | Motion control |
| Zeroscope | T2V | 512x320 | Quick tests |

## 📁 Project Files

- `backend_enhanced.py` - Enhanced backend with multiple models
- `index_enhanced.html` - Full-featured frontend
- `models_config.py` - Model configurations
- `requirements.txt` - Dependencies

## 🔧 API Endpoints

**GET /health** - Server health check
**GET /models** - List available models and options
**POST /generate-video** - Text-to-video generation
**POST /generate-video-from-image** - Image-to-video generation

## 💡 Tips

- Start with Zeroscope for quick tests
- Use CogVideoX-5B for final high-quality output
- Combine camera movements with visual effects
- Keep prompts descriptive and specific
- Image-to-video works best with clear, well-lit images

## 🐛 Troubleshooting

**Connection errors**: Check internet and Hugging Face availability
**Timeouts**: Service may be busy, try again or use faster model
**Slow generation**: Normal for high-quality models (30-120s)

## 📊 What's New vs Basic Version

✅ Multiple AI models (5 models vs 1)
✅ Image-to-video capability
✅ Camera movement controls (Hailuo-style)
✅ Visual effects and styles
✅ Enhanced prompt building
✅ Better UI with dual panels
✅ Categorized example prompts
✅ Model information display

---

**Made with ❤️ inspired by Hailuo AI**
