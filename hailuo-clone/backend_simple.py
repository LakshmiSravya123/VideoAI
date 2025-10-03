"""
Simple backend with multiple fallback options
Uses less congested models and provides demo mode
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Sample videos for demo mode
DEMO_VIDEOS = [
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
]

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'mode': 'demo',
        'message': 'Demo mode - returns sample videos for testing'
    })

@app.route('/models', methods=['GET'])
def list_models():
    return jsonify({
        'models': {
            'demo': {
                'name': 'Demo Mode (Instant)',
                'description': 'Returns sample videos instantly for testing UI',
                'type': 'text-to-video'
            },
            'local': {
                'name': 'Local Generation (Recommended)',
                'description': 'Run CogVideoX locally on your computer',
                'type': 'text-to-video'
            }
        }
    })

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        data = request.json
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        logger.info(f"Demo mode: Returning sample video for prompt: {prompt[:100]}")
        
        # Return a sample video
        import random
        video_url = random.choice(DEMO_VIDEOS)
        
        return jsonify({
            'video_url': video_url,
            'prompt': prompt,
            'model': 'demo',
            'model_name': 'Demo Mode (Sample Video)',
            'timestamp': datetime.now().isoformat(),
            'note': '⚠️ This is a demo video. All online AI services are currently overloaded. Recommendation: Use local generation (backend_local.py) for real AI videos.'
        })
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 70)
    print("🎬 DEMO MODE - Simple Backend")
    print("=" * 70)
    print("")
    print("⚠️  IMPORTANT: All online AI video services are currently overloaded!")
    print("")
    print("This demo backend returns sample videos to test the UI.")
    print("")
    print("For REAL AI video generation, you have 2 options:")
    print("")
    print("1. 🖥️  LOCAL GENERATION (Recommended):")
    print("   - Run: python backend_local.py")
    print("   - Open: index_local.html")
    print("   - Free, private, works offline")
    print("   - Takes 30-120s (GPU) or 5-10min (CPU)")
    print("")
    print("2. 💰 PAID API (Replicate Pro):")
    print("   - Upgrade to Replicate Pro account")
    print("   - Run: python backend_replicate.py")
    print("   - Fast but costs ~$0.05-0.10 per video")
    print("")
    print("=" * 70)
    print("Starting demo server on http://localhost:5000")
    print("=" * 70)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
