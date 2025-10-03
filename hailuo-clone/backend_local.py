"""
Local Video Generation Backend
Uses diffusers library to run models locally on your computer
Based on the VideoAI_Free_Colab.ipynb notebook
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import torch
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video
import os
import logging
from datetime import datetime
import tempfile
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app_local.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
OUTPUT_DIR = "generated_videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Global pipeline variable
pipeline = None
device = "cuda" if torch.cuda.is_available() else "cpu"

def initialize_model():
    """Initialize the CogVideoX model"""
    global pipeline
    
    if pipeline is not None:
        logger.info("Model already loaded")
        return True
    
    try:
        logger.info("🤖 Loading CogVideoX-2B model...")
        logger.info("⏳ This may take 2-5 minutes on first run...")
        
        # Use CogVideoX-2B (smaller, faster)
        pipeline = CogVideoXPipeline.from_pretrained(
            "THUDM/CogVideoX-2b",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            use_safetensors=True
        )
        
        if device == "cuda":
            pipeline.to("cuda")
            logger.info("✅ Model loaded on GPU!")
        else:
            logger.info("⚠️ Running on CPU (will be slower)")
            logger.info("💡 For faster generation, use a computer with NVIDIA GPU")
        
        logger.info("🎬 Model ready to generate videos!")
        return True
        
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    model_loaded = pipeline is not None
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_loaded,
        'device': device,
        'gpu_available': torch.cuda.is_available(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/models', methods=['GET'])
def list_models():
    """List available models"""
    return jsonify({
        'models': {
            'cogvideox-2b-local': {
                'name': 'CogVideoX-2B (Local)',
                'description': 'Running locally on your computer',
                'type': 'text-to-video'
            }
        },
        'device': device,
        'gpu_available': torch.cuda.is_available()
    })

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video from text prompt"""
    try:
        # Initialize model if not already loaded
        if pipeline is None:
            logger.info("Model not loaded, initializing...")
            if not initialize_model():
                return jsonify({
                    'error': 'Failed to load model. Check logs for details.'
                }), 500
        
        # Get request data
        data = request.json
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        if len(prompt) < 3:
            return jsonify({'error': 'Prompt must be at least 3 characters'}), 400
        
        logger.info(f"🎨 Generating video for: {prompt[:100]}")
        logger.info(f"⏳ This will take 30-120 seconds depending on your hardware...")
        
        # Generate video
        num_frames = 49  # ~6 seconds at 8 fps
        
        video_frames = pipeline(
            prompt=prompt,
            num_frames=num_frames,
            guidance_scale=6.0,
            num_inference_steps=50
        ).frames[0]
        
        # Save video
        video_id = str(uuid.uuid4())
        output_path = os.path.join(OUTPUT_DIR, f"{video_id}.mp4")
        export_to_video(video_frames, output_path, fps=8)
        
        logger.info(f"✅ Video generated successfully: {output_path}")
        
        # Return video URL
        video_url = f"/download/{video_id}.mp4"
        
        return jsonify({
            'video_url': video_url,
            'prompt': prompt,
            'model': 'cogvideox-2b-local',
            'model_name': 'CogVideoX-2B (Local)',
            'device': device,
            'num_frames': num_frames,
            'timestamp': datetime.now().isoformat()
        })
        
    except torch.cuda.OutOfMemoryError:
        logger.error("GPU out of memory!")
        return jsonify({
            'error': 'GPU out of memory. Try closing other applications or use a shorter prompt.'
        }), 500
        
    except Exception as e:
        logger.error(f"Error generating video: {str(e)}", exc_info=True)
        return jsonify({
            'error': f'Video generation failed: {str(e)}'
        }), 500

@app.route('/download/<filename>', methods=['GET'])
def download_video(filename):
    """Download generated video"""
    try:
        file_path = os.path.join(OUTPUT_DIR, filename)
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'Video not found'}), 404
        
        return send_file(
            file_path,
            mimetype='video/mp4',
            as_attachment=False,
            download_name=filename
        )
        
    except Exception as e:
        logger.error(f"Error serving video: {str(e)}")
        return jsonify({'error': 'Failed to serve video'}), 500

@app.route('/initialize', methods=['POST'])
def initialize():
    """Manually initialize the model"""
    if initialize_model():
        return jsonify({
            'status': 'success',
            'message': 'Model loaded successfully',
            'device': device
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Failed to load model'
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info("🚀 Starting Local Video Generation Backend")
    logger.info("=" * 60)
    logger.info(f"Device: {device}")
    logger.info(f"GPU Available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        logger.info(f"GPU: {torch.cuda.get_device_name(0)}")
        logger.info(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    else:
        logger.info("⚠️ No GPU detected - will run on CPU (slower)")
        logger.info("💡 For faster generation, use a computer with NVIDIA GPU")
    
    logger.info("=" * 60)
    logger.info("📝 Model will be downloaded on first request (~5GB)")
    logger.info("📝 First generation will take longer (model loading)")
    logger.info("📝 Subsequent generations will be faster")
    logger.info("=" * 60)
    
    # Optionally pre-load model (uncomment to load on startup)
    # logger.info("Pre-loading model...")
    # initialize_model()
    
    logger.info(f"🌐 Starting server on http://localhost:{FLASK_PORT}")
    logger.info("=" * 60)
    
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=False)
