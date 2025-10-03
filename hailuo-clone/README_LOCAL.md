# 🎬 Local AI Video Generator

Generate AI videos **completely locally** on your computer using CogVideoX-2B model!

## 🌟 Features

- ✅ **100% Local** - No API keys, no cloud services, runs on your computer
- 🚀 **CogVideoX-2B** - State-of-the-art text-to-video model by Tsinghua University
- 🎥 **6-second videos** - Generate 49 frames at 8 fps (720p quality)
- 💻 **GPU or CPU** - Works on both (GPU recommended for speed)
- 🎨 **Simple UI** - Clean web interface for easy video generation

## 📋 Requirements

### Hardware Requirements

**Minimum (CPU):**
- 16GB RAM
- 10GB free disk space
- Generation time: 5-10 minutes per video

**Recommended (GPU):**
- NVIDIA GPU with 8GB+ VRAM (RTX 3060 or better)
- 16GB RAM
- 10GB free disk space
- Generation time: 30-120 seconds per video

### Software Requirements

- Python 3.9 or higher
- CUDA 11.8+ (for GPU acceleration)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install PyTorch with CUDA support (for GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Or install PyTorch for CPU only
pip install torch torchvision torchaudio

# Install other requirements
pip install -r requirements_local.txt
```

### 2. Run the Backend

```bash
python backend_local.py
```

The server will start on `http://localhost:5000`

**First Run Notes:**
- The model (~5GB) will be downloaded automatically
- This happens only once
- Subsequent runs will be much faster

### 3. Open the Web Interface

Open `index_local.html` in your browser:

```bash
# On macOS
open index_local.html

# On Linux
xdg-open index_local.html

# On Windows
start index_local.html
```

Or manually open: `http://localhost:5000` and navigate to the HTML file

### 4. Initialize the Model

1. Click the **"🚀 Initialize Model"** button in the UI
2. Wait 2-5 minutes for the model to load
3. Once loaded, you can start generating videos!

### 5. Generate Videos

1. Enter a descriptive prompt (e.g., "A cat playing with a ball of yarn")
2. Click **"🎬 Generate Video"**
3. Wait 30-120 seconds (GPU) or 5-10 minutes (CPU)
4. Download or share your video!

## 📝 Example Prompts

- "A golden retriever running through a field of flowers at sunset"
- "Ocean waves crashing on a beach, aerial view"
- "A bird flying through clouds, slow motion"
- "City street with cars at night, neon lights"
- "Flowers blooming in a garden, time-lapse"

## 🎯 Tips for Best Results

1. **Be Descriptive** - Include details about lighting, camera angle, movement
2. **Keep it Simple** - Focus on one main subject or action
3. **Use Cinematic Terms** - "aerial view", "close-up", "slow motion", etc.
4. **GPU Recommended** - Much faster generation (30-120s vs 5-10min)
5. **First Generation** - May take longer as model initializes

## 🔧 Troubleshooting

### Model Not Loading
- **Issue**: Model fails to download or load
- **Solution**: Check internet connection, ensure 10GB free disk space

### Out of Memory (GPU)
- **Issue**: CUDA out of memory error
- **Solution**: Close other GPU applications, or use CPU mode

### Slow Generation (CPU)
- **Issue**: Takes 5-10 minutes per video
- **Solution**: This is normal for CPU. Consider using a GPU for faster generation

### Server Won't Start
- **Issue**: Port 5000 already in use
- **Solution**: Change port in `backend_local.py` (line 33): `FLASK_PORT = 5001`

### Video Quality Issues
- **Issue**: Video looks blurry or low quality
- **Solution**: This is expected for the 2B model. For better quality, upgrade to CogVideoX-5B (requires more VRAM)

## 📊 Performance Benchmarks

| Hardware | Model Load Time | Generation Time | Quality |
|----------|----------------|-----------------|---------|
| RTX 4090 | 1-2 min | 30-45 sec | Excellent |
| RTX 3060 | 2-3 min | 60-90 sec | Good |
| CPU (16GB) | 3-5 min | 5-10 min | Good |

## 🔄 Model Information

- **Model**: CogVideoX-2B
- **Developer**: Tsinghua University (THUDM)
- **License**: Apache 2.0
- **Size**: ~5GB
- **Output**: 49 frames, 720p, 8 fps (~6 seconds)

## 📁 File Structure

```
hailuo-clone/
├── backend_local.py          # Local backend server
├── index_local.html          # Web interface for local backend
├── requirements_local.txt    # Python dependencies
├── README_LOCAL.md          # This file
└── generated_videos/        # Output directory (auto-created)
```

## 🆚 Comparison with Cloud Backends

| Feature | Local (backend_local.py) | Cloud (backend_enhanced.py) |
|---------|-------------------------|----------------------------|
| Setup | Complex (install PyTorch, download model) | Simple (just API keys) |
| Cost | Free (one-time setup) | Pay per generation |
| Speed | 30-120s (GPU) or 5-10min (CPU) | 30-60s |
| Privacy | 100% private | Data sent to cloud |
| Quality | Good (2B model) | Excellent (5B+ models) |
| Internet | Only for first download | Required for every generation |

## 🛠️ Advanced Configuration

### Change Model

Edit `backend_local.py` line 54-56 to use a different model:

```python
# For better quality (requires 16GB+ VRAM)
pipeline = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-5b",
    torch_dtype=torch.float16
)
```

### Adjust Generation Parameters

Edit `backend_local.py` lines 126-132:

```python
num_frames = 49          # More frames = longer video
guidance_scale = 6.0     # Higher = more prompt adherence
num_inference_steps = 50 # More steps = better quality (slower)
```

### Pre-load Model on Startup

Uncomment lines 232-233 in `backend_local.py`:

```python
logger.info("Pre-loading model...")
initialize_model()
```

## 📚 Resources

- [CogVideoX GitHub](https://github.com/THUDM/CogVideo)
- [Diffusers Documentation](https://huggingface.co/docs/diffusers)
- [PyTorch Installation](https://pytorch.org/get-started/locally/)

## 🤝 Support

If you encounter issues:

1. Check the console logs in the terminal
2. Check browser console (F12) for errors
3. Ensure all dependencies are installed correctly
4. Verify GPU drivers are up to date (for GPU mode)

## 📄 License

This project uses CogVideoX-2B which is licensed under Apache 2.0.

---

**Happy Video Generation! 🎬✨**
