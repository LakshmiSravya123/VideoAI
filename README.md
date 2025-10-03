# 🎬 VideoAI - AI-Powered Video Generation Platform

A comprehensive AI video generation platform inspired by Hailuo AI, featuring multiple state-of-the-art models from Hugging Face.

## 🌟 Overview

This repository contains a full-stack AI video generation application that allows users to create videos from text prompts or animate images using cutting-edge AI models. The application features a professional UI with Hailuo-inspired controls for camera movements, visual effects, and video styles.

## 📁 Project Structure

```
VideoAI/
├── hailuo-clone/              # Main application directory
│   ├── backend.py             # Basic Flask backend
│   ├── backend_enhanced.py    # Advanced multi-model backend
│   ├── models_config.py       # AI models configuration
│   ├── index.html             # Basic frontend UI
│   ├── index_enhanced.html    # Full-featured professional UI
│   ├── index_demo.html        # Demo mode UI
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example          # Environment configuration template
│   ├── .gitignore            # Git ignore rules
│   ├── README.md             # Basic documentation
│   └── README_ENHANCED.md    # Comprehensive documentation
└── README.md                  # This file
```

## ✨ Key Features

### 🎯 Multiple Generation Modes
- **Text-to-Video**: Create videos from text descriptions
- **Image-to-Video**: Animate static images with AI

### 🤖 AI Models (5 Models)
1. **CogVideoX-5B** - High-quality 6-second videos at 720p
2. **LTX Video** - Fast and efficient by Lightricks
3. **Stable Video Diffusion** - Professional image animation
4. **AnimateDiff** - Advanced motion control
5. **Zeroscope V2 XL** - Fast and reliable baseline

### 🎥 Hailuo-Inspired Features
- **12 Camera Movements**: Zoom, Pan, Tilt, Tracking, Dolly, Crane, Shake, etc.
- **8 Visual Effects**: Cinematic, Dramatic, Foggy, Rainy, Slow Motion, etc.
- **8 Video Styles**: Realistic, Anime, Cartoon, 3D Render, Vintage, Sci-Fi, Fantasy
- **Enhanced Prompt Building**: Automatic combination of all options

### 🎨 Professional UI
- Modern gradient design with purple theme
- Dual-panel layout for efficient workflow
- Real-time character counter and validation
- Categorized example prompts
- Video preview with download and share options
- Responsive design for all screen sizes

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser
- Internet connection (for Hugging Face API calls)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LakshmiSravya123/VideoAI.git
   cd VideoAI/hailuo-clone
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment** (optional):
   ```bash
   cp .env.example .env
   # Edit .env if needed
   ```

### Running the Application

#### Enhanced Version (Recommended)

1. **Start the backend**:
   ```bash
   python3 backend_enhanced.py
   ```

2. **Open the frontend**:
   - Open `index_enhanced.html` in your browser
   - Or serve it locally:
     ```bash
     python3 -m http.server 8000
     ```
     Then visit: `http://localhost:8000/index_enhanced.html`

3. **Try Demo Mode**:
   - Select "⭐ Demo Mode" from the model dropdown
   - Enter a prompt or use examples
   - Add camera movements, effects, styles
   - Click "Generate Video"
   - See the UI in action instantly!

#### Basic Version

1. **Start the backend**:
   ```bash
   python3 backend.py
   ```

2. **Open the frontend**:
   - Open `index.html` in your browser

## 📖 Usage

### Text-to-Video Generation

1. Select "Text to Video" mode
2. Choose an AI model (start with Demo Mode)
3. Enter your prompt (3-1000 characters)
4. **Optional**: Add advanced options:
   - Camera Movement (e.g., "Tracking Shot")
   - Visual Effects (e.g., "Cinematic")
   - Video Style (e.g., "Realistic")
5. Click "Generate Video"
6. Wait for generation (instant for Demo Mode, 30-120s for real models)
7. Download or share your video

### Image-to-Video Generation

1. Select "Image to Video" mode
2. Upload an image (JPG or PNG)
3. Add animation prompt (optional)
4. Select an image-to-video model
5. Generate

## 🎯 Example Prompts

**Nature**:
```
A majestic waterfall cascading down mossy rocks in a lush rainforest
```

**Action** (with camera):
```
A sports car drifting around a corner [Tracking shot]
```

**Fantasy** (with style):
```
A dragon flying over a medieval castle at dawn, fantasy, magical, ethereal
```

## 🛠️ Technology Stack

- **Backend**: Flask, Python
- **AI Integration**: Gradio Client, Hugging Face Spaces
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Image Processing**: Pillow
- **Environment Management**: python-dotenv

## 📊 Comparison: Basic vs Enhanced

| Feature | Basic Version | Enhanced Version |
|---------|--------------|------------------|
| Models | 1 (Zeroscope) | 6 (5 AI + Demo) |
| Generation Types | Text-to-Video | Text-to-Video + Image-to-Video |
| Camera Controls | None | 12 movements |
| Visual Effects | None | 8 effects |
| Styles | None | 8 styles |
| Example Prompts | 4 basic | 20+ categorized |
| UI | Simple | Professional dual-panel |
| Demo Mode | No | Yes |

## 🐛 Troubleshooting

### "Failed to connect to video generation service"
- **Solution**: Use "Demo Mode" to test the UI
- Real models require Hugging Face Spaces to be available
- Some spaces may be sleeping or require authentication

### Slow generation
- Normal for high-quality models (30-120 seconds)
- Use Demo Mode for instant results
- Use Zeroscope for faster real generation

## 📝 Documentation

- **Basic Guide**: See `hailuo-clone/README.md`
- **Comprehensive Guide**: See `hailuo-clone/README_ENHANCED.md`
- **API Documentation**: Included in README_ENHANCED.md

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Inspired by [Hailuo AI](https://hailuoai.video) by MiniMax
- Built with [Flask](https://flask.palletsprojects.com/)
- Uses [Gradio Client](https://www.gradio.app/) for Hugging Face integration
- AI models from [Hugging Face](https://huggingface.co/)

## 📞 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Check the documentation in the `hailuo-clone/` directory

---

**Made with ❤️ for the AI community**

🌟 **Star this repo if you find it useful!**
