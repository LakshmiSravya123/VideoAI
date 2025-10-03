from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gradio_client import Client
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image
import tempfile

from models_config import (
    VIDEO_MODELS, 
    CAMERA_MOVEMENTS, 
    VISUAL_EFFECTS, 
    VIDEO_STYLES,
    EXAMPLE_PROMPTS,
    get_model_info, 
    get_available_models,
    build_enhanced_prompt
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'zeroscope')

# Constants
MAX_PROMPT_LENGTH = 1000
MIN_PROMPT_LENGTH = 3

# Model clients cache
model_clients = {}

def get_or_create_client(model_id):
    """Get or create a Gradio client for the specified model"""
    if model_id not in model_clients:
        try:
            model_info = get_model_info(model_id)
            space_url = model_info['space_url']
            logger.info(f"Initializing client for {model_id}: {space_url}")
            
            # Try to connect with timeout
            model_clients[model_id] = Client(space_url, verbose=False)
            logger.info(f"Successfully connected to {model_id}")
        except Exception as e:
            logger.error(f"Failed to initialize client for {model_id}: {str(e)}")
            logger.error(f"This might be because:")
            logger.error(f"  1. The Hugging Face Space is not available or sleeping")
            logger.error(f"  2. The Space URL has changed")
            logger.error(f"  3. The Space requires authentication")
            logger.error(f"  4. Network connectivity issues")
            return None
    return model_clients.get(model_id)

def validate_prompt(prompt):
    """Validate the input prompt"""
    if not prompt or not isinstance(prompt, str):
        return False, "Prompt must be a non-empty string"
    
    prompt = prompt.strip()
    
    if len(prompt) < MIN_PROMPT_LENGTH:
        return False, f"Prompt must be at least {MIN_PROMPT_LENGTH} characters long"
    
    if len(prompt) > MAX_PROMPT_LENGTH:
        return False, f"Prompt must not exceed {MAX_PROMPT_LENGTH} characters"
    
    return True, prompt

def decode_base64_image(base64_string):
    """Decode base64 image string to PIL Image"""
    try:
        # Remove data URL prefix if present
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        image_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        logger.error(f"Failed to decode image: {str(e)}")
        return None

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'available_models': list(VIDEO_MODELS.keys()),
        'default_model': DEFAULT_MODEL
    })

@app.route('/models', methods=['GET'])
def list_models():
    """List all available video generation models"""
    return jsonify({
        'models': get_available_models(),
        'camera_movements': CAMERA_MOVEMENTS,
        'visual_effects': VISUAL_EFFECTS,
        'video_styles': VIDEO_STYLES,
        'example_prompts': EXAMPLE_PROMPTS
    })

@app.route('/test-video', methods=['POST'])
def test_video():
    """Test endpoint that returns a sample video URL for UI testing"""
    data = request.json
    prompt = data.get('prompt', 'Test prompt')
    
    logger.info(f"Test mode: Simulating video generation for: {prompt[:100]}")
    
    # Return a sample video URL (Big Buck Bunny - open source test video)
    return jsonify({
        'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
        'prompt': prompt,
        'enhanced_prompt': prompt,
        'model': 'test-mode',
        'model_name': 'Test Mode (Demo Video)',
        'timestamp': datetime.now().isoformat(),
        'note': 'This is a demo video. Connect to Hugging Face Spaces for real generation.'
    })

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video from text prompt with advanced options"""
    try:
        # Validate request data
        if not request.json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.json
        base_prompt = data.get('prompt', '').strip()
        model_id = data.get('model', DEFAULT_MODEL)
        
        # Advanced options (Hailuo-inspired)
        camera_movement = data.get('camera_movement', '')
        visual_effect = data.get('visual_effect', '')
        style = data.get('style', '')
        
        # Validate prompt
        is_valid, result = validate_prompt(base_prompt)
        if not is_valid:
            logger.warning(f"Invalid prompt: {result}")
            return jsonify({'error': result}), 400
        
        base_prompt = result
        
        # Validate model
        if model_id not in VIDEO_MODELS:
            return jsonify({'error': f'Invalid model: {model_id}'}), 400
        
        model_info = get_model_info(model_id)
        
        # Check if model supports text-to-video
        if model_info['type'] != 'text-to-video':
            return jsonify({'error': f'Model {model_id} does not support text-to-video generation'}), 400
        
        # Build enhanced prompt with camera movements and effects
        enhanced_prompt = build_enhanced_prompt(base_prompt, camera_movement, visual_effect, style)
        
        logger.info(f"Generating video with {model_id}")
        logger.info(f"Base prompt: {base_prompt[:100]}...")
        logger.info(f"Enhanced prompt: {enhanced_prompt[:150]}...")
        
        # Handle demo mode specially
        if model_id == 'demo':
            logger.info("Demo mode activated - returning sample video")
            return jsonify({
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
                'prompt': base_prompt,
                'enhanced_prompt': enhanced_prompt,
                'model': model_id,
                'model_name': model_info['name'],
                'timestamp': datetime.now().isoformat(),
                'note': 'Demo mode: This is a sample video. Select a real model for AI generation.'
            })
        
        # Get or create client
        client = get_or_create_client(model_id)
        if client is None:
            return jsonify({'error': 'Failed to connect to video generation service. Try using "Demo Mode" model to test the UI.'}), 503
        
        # Generate video based on model type
        try:
            if model_id == 'zeroscope':
                result = client.predict(
                    enhanced_prompt,
                    model_info['params']['num_frames'],
                    model_info['params']['width'],
                    model_info['params']['height'],
                    api_name=model_info['api_name']
                )
            elif model_id == 'cogvideox-5b':
                result = client.predict(
                    enhanced_prompt,
                    api_name=model_info['api_name']
                )
            elif model_id == 'ltx-video':
                result = client.predict(
                    enhanced_prompt,
                    api_name=model_info['api_name']
                )
            else:
                # Generic approach
                result = client.predict(
                    enhanced_prompt,
                    api_name=model_info['api_name']
                )
        except Exception as e:
            logger.error(f"Model API call failed: {str(e)}")
            return jsonify({'error': f'Video generation failed: {str(e)}'}), 500
        
        # Extract video path/URL from result
        video_path = result[0] if isinstance(result, list) else result
        
        if not video_path:
            logger.error("No video path returned from API")
            return jsonify({'error': 'Failed to generate video. No output received.'}), 500
        
        logger.info(f"Video generated successfully: {video_path}")
        return jsonify({
            'video_url': video_path,
            'prompt': base_prompt,
            'enhanced_prompt': enhanced_prompt,
            'model': model_id,
            'model_name': model_info['name'],
            'timestamp': datetime.now().isoformat()
        })
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    
    except ConnectionError as e:
        logger.error(f"Connection error: {str(e)}")
        return jsonify({'error': 'Failed to connect to video generation service. Please try again later.'}), 503
    
    except TimeoutError as e:
        logger.error(f"Timeout error: {str(e)}")
        return jsonify({'error': 'Request timed out. The service may be busy. Please try again.'}), 504
    
    except Exception as e:
        logger.error(f"Unexpected error in generate_video: {str(e)}", exc_info=True)
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

@app.route('/generate-video-from-image', methods=['POST'])
def generate_video_from_image():
    """Generate video from image with text prompt (Image-to-Video)"""
    try:
        # Validate request data
        if not request.json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.json
        prompt = data.get('prompt', '').strip()
        image_data = data.get('image', '')
        model_id = data.get('model', 'stable-video-diffusion')
        
        # Validate model supports image-to-video
        model_info = get_model_info(model_id)
        if model_info['type'] != 'image-to-video':
            return jsonify({'error': f'Model {model_id} does not support image-to-video generation'}), 400
        
        # Decode image
        image = decode_base64_image(image_data)
        if image is None:
            return jsonify({'error': 'Invalid image data'}), 400
        
        # Save image to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
            image.save(tmp_file.name)
            temp_image_path = tmp_file.name
        
        logger.info(f"Generating video from image with {model_id}")
        logger.info(f"Prompt: {prompt[:100]}...")
        
        # Get or create client
        client = get_or_create_client(model_id)
        if client is None:
            os.unlink(temp_image_path)
            return jsonify({'error': 'Failed to connect to video generation service'}), 503
        
        # Generate video
        try:
            if model_id == 'stable-video-diffusion':
                result = client.predict(
                    temp_image_path,
                    api_name=model_info['api_name']
                )
            elif model_id == 'animatediff':
                result = client.predict(
                    temp_image_path,
                    prompt,
                    api_name=model_info['api_name']
                )
            else:
                result = client.predict(
                    temp_image_path,
                    prompt,
                    api_name=model_info['api_name']
                )
        finally:
            # Clean up temp file
            if os.path.exists(temp_image_path):
                os.unlink(temp_image_path)
        
        # Extract video path
        video_path = result[0] if isinstance(result, list) else result
        
        if not video_path:
            return jsonify({'error': 'Failed to generate video from image'}), 500
        
        logger.info(f"Video generated from image successfully")
        return jsonify({
            'video_url': video_path,
            'prompt': prompt,
            'model': model_id,
            'model_name': model_info['name'],
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error in generate_video_from_image: {str(e)}", exc_info=True)
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors"""
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info(f"Starting Enhanced Flask server on port {FLASK_PORT} (debug={FLASK_DEBUG})")
    logger.info(f"Available models: {', '.join(VIDEO_MODELS.keys())}")
    logger.info(f"Default model: {DEFAULT_MODEL}")
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=FLASK_DEBUG)
