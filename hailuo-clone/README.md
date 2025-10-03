# 🎬 AI Video Generator - Free Hailuo Clone

A free, open-source AI-powered video generation application that creates videos from text prompts using Hugging Face's Zeroscope model.

## ✨ Features

- 🎨 **Text-to-Video Generation**: Create videos from simple text descriptions
- 🎯 **Modern UI**: Beautiful, responsive interface with gradient design
- 📥 **Video Download**: Download generated videos directly to your device
- ⚡ **Real-time Status**: Live feedback with loading indicators and status messages
- 🔒 **Input Validation**: Robust validation and error handling
- 📊 **Health Monitoring**: Server health check endpoint
- 🎭 **Example Prompts**: Quick-start with pre-made prompt examples
- 📝 **Character Counter**: Track your prompt length in real-time

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, or Edge)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd /Users/sravyalu/VideoAI/hailuo-clone
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file if you need to customize settings:
   ```env
   HF_SPACE_URL=https://cerspense-zeroscope-v2-xl.hf.space/
   FLASK_PORT=5000
   FLASK_DEBUG=False
   ```

### Running the Application

1. **Start the backend server**:
   ```bash
   python backend.py
   ```
   
   You should see:
   ```
   INFO - Starting Flask server on port 5000 (debug=False)
   INFO - Successfully connected to Hugging Face Space
   ```

2. **Open the frontend**:
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     ```
     Then visit: `http://localhost:8000`

3. **Generate your first video**:
   - Enter a text prompt (e.g., "A dog running in a park")
   - Click "Generate Video"
   - Wait 10-60 seconds for the AI to create your video
   - Watch and download your generated video!

## 📁 Project Structure

```
hailuo-clone/
├── backend.py          # Flask backend server
├── index.html          # Frontend UI
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── app.log            # Application logs (created at runtime)
```

## 🛠️ Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HF_SPACE_URL` | `https://cerspense-zeroscope-v2-xl.hf.space/` | Hugging Face Space URL |
| `FLASK_PORT` | `5000` | Backend server port |
| `FLASK_DEBUG` | `False` | Enable/disable debug mode |

### Prompt Limits

- **Minimum length**: 3 characters
- **Maximum length**: 500 characters

## 🔧 API Endpoints

### Health Check
```
GET /health
```
Returns server health status and client initialization state.

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2025-10-02T17:38:51-07:00",
  "client_initialized": true
}
```

### Generate Video
```
POST /generate-video
Content-Type: application/json
```

**Request Body**:
```json
{
  "prompt": "A dog running in a park"
}
```

**Success Response** (200):
```json
{
  "video_url": "https://...",
  "prompt": "A dog running in a park",
  "timestamp": "2025-10-02T17:38:51-07:00"
}
```

**Error Response** (400/500/503/504):
```json
{
  "error": "Error message here"
}
```

## 🐛 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Install dependencies: `pip install -r requirements.txt`

**Problem**: `Failed to initialize Gradio client`
- **Solution**: Check your internet connection and verify the Hugging Face Space URL is correct

**Problem**: `Port 5000 already in use`
- **Solution**: Change the port in `.env` file or stop the process using port 5000

### Frontend Issues

**Problem**: "Cannot connect to server" error
- **Solution**: Ensure the backend is running on port 5000

**Problem**: Video doesn't play
- **Solution**: Check browser console for errors. Some browsers block autoplay.

**Problem**: CORS errors
- **Solution**: The backend has CORS enabled. Make sure you're using the correct URL.

## 📝 Logging

Application logs are saved to `app.log` in the project directory. Logs include:
- Server startup/shutdown events
- Video generation requests
- Errors and exceptions
- Client connection status

View logs in real-time:
```bash
tail -f app.log
```

## 🔒 Security Notes

- Never commit `.env` file to version control
- Don't run in debug mode in production (`FLASK_DEBUG=False`)
- Consider adding rate limiting for production use
- Validate and sanitize all user inputs (already implemented)

## 🚀 Production Deployment

For production deployment, consider:

1. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 backend:app
   ```

2. **Set up a reverse proxy** (e.g., Nginx)

3. **Enable HTTPS** with SSL certificates

4. **Add rate limiting** to prevent abuse

5. **Set up monitoring** and alerting

6. **Use environment variables** for sensitive configuration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Uses [Gradio Client](https://www.gradio.app/) for Hugging Face integration
- Video generation powered by [Zeroscope](https://huggingface.co/cerspense/zeroscope_v2_XL)

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the logs in `app.log`
3. Open an issue on the project repository

---

**Made with ❤️ for the AI community**
