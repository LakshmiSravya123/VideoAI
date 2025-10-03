from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client
import os
import logging
from dotenv import load_dotenv
from datetime import datetime

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
CORS(app)  # Enable CORS for frontend requests

# Configuration from environment variables
HF_SPACE_URL = os.getenv('HF_SPACE_URL', 'https://cerspense-zeroscope-v2-xl.hf.space/')
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Constants
MAX_PROMPT_LENGTH = 500
MIN_PROMPT_LENGTH = 3

# Initialize client with error handling
try:
    client = Client(HF_SPACE_URL)
    logger.info(f"Successfully connected to Hugging Face Space: {HF_SPACE_URL}")
except Exception as e:
    logger.error(f"Failed to initialize Gradio client: {str(e)}")
    client = None

def validate_prompt(prompt):
    """Validate the input prompt."""
    if not prompt or not isinstance(prompt, str):
        return False, "Prompt must be a non-empty string"
    
    prompt = prompt.strip()
    
    if len(prompt) < MIN_PROMPT_LENGTH:
        return False, f"Prompt must be at least {MIN_PROMPT_LENGTH} characters long"
    
    if len(prompt) > MAX_PROMPT_LENGTH:
        return False, f"Prompt must not exceed {MAX_PROMPT_LENGTH} characters"
    
    return True, prompt

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'client_initialized': client is not None
    })

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video from text prompt."""
    try:
        # Check if client is initialized
        if client is None:
            logger.error("Gradio client not initialized")
            return jsonify({'error': 'Service unavailable. Please check server configuration.'}), 503
        
        # Validate request data
        if not request.json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.json
        prompt = data.get('prompt', '').strip()
        
        # Validate prompt
        is_valid, result = validate_prompt(prompt)
        if not is_valid:
            logger.warning(f"Invalid prompt: {result}")
            return jsonify({'error': result}), 400
        
        prompt = result
        logger.info(f"Generating video for prompt: {prompt[:50]}...")
        
        # Call the HF Space API with timeout handling
        result = client.predict(
            prompt,          # Text prompt
            8,               # Number of frames (short video)
            512,             # Width
            320,             # Height
            api_name="/predict"
        )
        
        # Extract video path/URL from result
        video_path = result[0] if isinstance(result, list) else result
        
        if not video_path:
            logger.error("No video path returned from API")
            return jsonify({'error': 'Failed to generate video. No output received.'}), 500
        
        logger.info(f"Video generated successfully: {video_path}")
        return jsonify({
            'video_url': video_path,
            'prompt': prompt,
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

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors."""
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info(f"Starting Flask server on port {FLASK_PORT} (debug={FLASK_DEBUG})")
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=FLASK_DEBUG)