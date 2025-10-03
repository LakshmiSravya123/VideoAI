#!/bin/bash

# Local AI Video Generator Startup Script

echo "🎬 Starting Local AI Video Generator..."
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
if [ ! -f "venv/.requirements_installed" ]; then
    echo "📥 Installing dependencies (this may take a few minutes)..."
    echo ""
    echo "⚠️  Note: If you have an NVIDIA GPU, install PyTorch with CUDA first:"
    echo "   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118"
    echo ""
    read -p "Press Enter to continue with installation..."
    
    pip install -r requirements_local.txt
    touch venv/.requirements_installed
    echo "✅ Dependencies installed!"
fi

# Start the backend server
echo ""
echo "🚀 Starting backend server on http://localhost:5000"
echo "📝 Open index_local.html in your browser to use the app"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python backend_local.py
