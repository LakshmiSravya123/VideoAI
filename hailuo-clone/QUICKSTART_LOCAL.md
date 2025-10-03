# 🚀 Quick Start Guide - Local Video Generator

Get up and running in 3 simple steps!

## Step 1: Install PyTorch

Choose based on your hardware:

### Option A: GPU (NVIDIA) - Recommended
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Option B: CPU Only
```bash
pip install torch torchvision torchaudio
```

## Step 2: Run the Startup Script

### On macOS/Linux:
```bash
./start_local.sh
```

### On Windows:
```batch
start_local.bat
```

The script will:
- Create a virtual environment
- Install all dependencies
- Start the backend server

## Step 3: Open the Web Interface

1. Open `index_local.html` in your browser
2. Click **"🚀 Initialize Model"** (first time only, takes 2-5 minutes)
3. Enter a prompt and click **"🎬 Generate Video"**
4. Wait 30-120 seconds (GPU) or 5-10 minutes (CPU)
5. Enjoy your AI-generated video! 🎉

## ⚡ Quick Tips

- **First run**: Model download (~5GB) happens automatically
- **GPU users**: 30-120 seconds per video
- **CPU users**: 5-10 minutes per video (be patient!)
- **Example prompts**: Click the example buttons in the UI

## 🆘 Need Help?

See `README_LOCAL.md` for detailed documentation and troubleshooting.

---

**That's it! Happy video generation! 🎬✨**
