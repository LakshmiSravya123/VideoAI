@echo off
REM Local AI Video Generator Startup Script for Windows

echo 🎬 Starting Local AI Video Generator...
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.9 or higher.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if requirements are installed
if not exist "venv\.requirements_installed" (
    echo 📥 Installing dependencies (this may take a few minutes)...
    echo.
    echo ⚠️  Note: If you have an NVIDIA GPU, install PyTorch with CUDA first:
    echo    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    echo.
    pause
    
    pip install -r requirements_local.txt
    type nul > venv\.requirements_installed
    echo ✅ Dependencies installed!
)

REM Start the backend server
echo.
echo 🚀 Starting backend server on http://localhost:5000
echo 📝 Open index_local.html in your browser to use the app
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python backend_local.py
