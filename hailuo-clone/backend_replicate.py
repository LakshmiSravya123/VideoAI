from flask import Flask, request, jsonify
from flask_cors import CORS
import replicate
import os
from dotenv import load_dotenv
from datetime import datetime
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Set your Replicate API token
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
if REPLICATE_API_TOKEN:
    os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN

@app.route('/health', methods=['GET'])
def health():
    has_token = bool(REPLICATE_API_TOKEN)
    return jsonify({
        'status': 'healthy',
        'service': 'Replicate API',
        'token_configured': has_token
    })

@app.route('/models', methods=['GET'])
def list_models():
    """Return available models"""
    return jsonify({
        'models': {
            'hailuo': {
                'name': 'Hailuo Video-01 (MiniMax)',
                'description': 'Real Hailuo model - High quality video generation',
                'type': 'text-to-video'
            },
            'cogvideox': {
                'name': 'CogVideoX-5B',
                'description': 'High quality text-to-video',
                'type': 'text-to-video'
            }
        }
    })

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        if not REPLICATE_API_TOKEN:
            return jsonify({
                'error': 'Replicate API token not configured. Add REPLICATE_API_TOKEN to .env file'
            }), 500
        
        data = request.json
        prompt = data.get('prompt', '')
        model_id = data.get('model', 'hailuo')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        logger.info(f"Generating video with {model_id}: {prompt[:100]}")
        
        # Select model
        if model_id == 'cogvideox':
            model_name = "lucataco/cogvideox-5b"
        else:
            model_name = "minimax/video-01"  # Real Hailuo model!
        
        # Generate video
        output = replicate.run(
            model_name,
            input={"prompt": prompt}
        )
        
        # Output is a video URL
        video_url = output if isinstance(output, str) else (output[0] if isinstance(output, list) else str(output))
        
        logger.info(f"Video generated successfully: {video_url}")
        
        return jsonify({
            'video_url': video_url,
            'prompt': prompt,
            'model': model_id,
            'model_name': 'Hailuo Video-01 (MiniMax)' if model_id == 'hailuo' else 'CogVideoX-5B',
            'timestamp': datetime.now().isoformat(),
            'service': 'Replicate API'
        })
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': f'Video generation failed: {str(e)}'}), 500

if __name__ == '__main__':
    if not REPLICATE_API_TOKEN:
        print("=" * 60)
        print("⚠️  WARNING: REPLICATE_API_TOKEN not set!")
        print("=" * 60)
        print("1. Sign up at: https://replicate.com")
        print("2. Get token from: https://replicate.com/account/api-tokens")
        print("3. Add to .env file: REPLICATE_API_TOKEN=your_token_here")
        print("=" * 60)
    else:
        print("✅ Replicate API token configured!")
    
    logger.info("Starting Replicate backend on port 5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
