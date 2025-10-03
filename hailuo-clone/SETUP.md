# 🚀 Complete Setup Guide

## Prerequisites

- Python 3.9 or higher
- Git
- 10GB free disk space (for local models)

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd hailuo-clone
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Choose Your Backend

#### Option A: Replicate API (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt
pip install replicate

# Get API token from https://replicate.com/account/api-tokens
# Create .env file
echo "REPLICATE_API_TOKEN=your_token_here" > .env

# Run backend
python backend_replicate.py

# Open index.html in browser
```

#### Option B: Local Generation

```bash
# Install PyTorch (GPU version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Or CPU version
pip install torch torchvision torchaudio

# Install other dependencies
pip install -r requirements_local.txt

# Run backend
python backend_local.py

# Open index_local.html in browser
```

#### Option C: Hugging Face Spaces

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
python backend_enhanced.py

# Open index_enhanced.html in browser
```

### 4. Test the Setup

1. Open the appropriate HTML file in your browser
2. Enter a test prompt: "A cat playing with a ball of yarn"
3. Click "Generate Video"
4. Wait for the video to generate

## Quick Commands

### Start Replicate Backend
```bash
source venv/bin/activate
python backend_replicate.py
```

### Start Local Backend
```bash
source venv/bin/activate
python backend_local.py
```

### Start Enhanced Backend
```bash
source venv/bin/activate
python backend_enhanced.py
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>
```

### Missing Dependencies
```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt
```

### API Token Issues
```bash
# Verify .env file exists
cat .env

# Should show: REPLICATE_API_TOKEN=your_token_here
```

## Next Steps

- Read [README_GITHUB.md](README_GITHUB.md) for full documentation
- Check [SOLUTION_GUIDE.md](SOLUTION_GUIDE.md) for troubleshooting
- See [models_config.py](models_config.py) to customize models
