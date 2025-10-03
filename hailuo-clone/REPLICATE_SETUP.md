# 🚀 Using Replicate API for Real Hailuo (MiniMax) Video Generation

If Hugging Face Spaces are not working, you can use **Replicate API** which has the actual **Hailuo video-01 model** by MiniMax!

## 🌟 Why Replicate?

- ✅ **Real Hailuo Model**: The actual MiniMax video-01 model
- ✅ **Reliable**: Always available, no sleeping spaces
- ✅ **Fast**: Optimized infrastructure
- ✅ **Free Tier**: $5 free credits to start

## 📝 Setup Instructions

### 1. Get Replicate API Token

1. Go to https://replicate.com
2. Sign up for a free account
3. Go to https://replicate.com/account/api-tokens
4. Copy your API token

### 2. Install Replicate Python Client

```bash
pip install replicate
```

### 3. Create Replicate Backend

Create a new file `backend_replicate.py`:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import replicate
import os
from dotenv import load_dotenv
from datetime import datetime
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Set your Replicate API token
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
if REPLICATE_API_TOKEN:
    os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'Replicate API'})

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        logger.info(f"Generating video with Hailuo: {prompt[:100]}")
        
        # Use the real Hailuo (MiniMax) model on Replicate
        output = replicate.run(
            "minimax/video-01",
            input={
                "prompt": prompt,
                "prompt_optimizer": True
            }
        )
        
        # Output is a video URL
        video_url = output if isinstance(output, str) else output[0]
        
        logger.info(f"Video generated: {video_url}")
        
        return jsonify({
            'video_url': video_url,
            'prompt': prompt,
            'model': 'hailuo-minimax',
            'model_name': 'Hailuo Video-01 (MiniMax)',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not REPLICATE_API_TOKEN:
        print("⚠️  Warning: REPLICATE_API_TOKEN not set in .env file")
        print("Get your token from: https://replicate.com/account/api-tokens")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### 4. Update .env File

Add your Replicate API token to `.env`:

```env
REPLICATE_API_TOKEN=r8_your_token_here
```

### 5. Run the Replicate Backend

```bash
python3 backend_replicate.py
```

### 6. Use with Your Frontend

The frontend (`index_enhanced.html`) will work with this backend without any changes!

## 🎬 Available Models on Replicate

### Text-to-Video Models:

1. **Hailuo Video-01 (MiniMax)** - The real Hailuo model!
   ```python
   replicate.run("minimax/video-01", input={"prompt": "..."})
   ```

2. **CogVideoX**
   ```python
   replicate.run("lucataco/cogvideox-5b", input={"prompt": "..."})
   ```

3. **Kling v1.6**
   ```python
   replicate.run("fofr/kling-v1.6-standard", input={"prompt": "..."})
   ```

### Image-to-Video Models:

1. **Stable Video Diffusion**
   ```python
   replicate.run("stability-ai/stable-video-diffusion", input={"image": "..."})
   ```

2. **Hailuo Image-to-Video**
   ```python
   replicate.run("minimax/video-01", input={"image": "...", "prompt": "..."})
   ```

## 💰 Pricing

- **Free Tier**: $5 free credits (enough for ~50 videos)
- **Pay-as-you-go**: ~$0.10 per video generation
- Much cheaper than running your own GPU!

## 🔧 Advanced: Multi-Model Support

Create `backend_replicate_multi.py` with multiple models:

```python
MODELS = {
    "hailuo": "minimax/video-01",
    "cogvideox": "lucataco/cogvideox-5b",
    "kling": "fofr/kling-v1.6-standard",
    "svd": "stability-ai/stable-video-diffusion"
}

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    model_id = data.get('model', 'hailuo')
    prompt = data.get('prompt', '')
    
    model_name = MODELS.get(model_id, MODELS['hailuo'])
    
    output = replicate.run(model_name, input={"prompt": prompt})
    # ... rest of the code
```

## ✅ Advantages of Replicate

1. **Real Hailuo Model**: The actual MiniMax video-01
2. **No Space Sleeping**: Always available
3. **Better Performance**: Optimized infrastructure
4. **Predictable Costs**: Pay per generation
5. **Multiple Models**: Access to many models
6. **Better Support**: Professional API support

## 📚 Resources

- **Replicate Docs**: https://replicate.com/docs
- **Hailuo Model**: https://replicate.com/minimax/video-01
- **Python Client**: https://github.com/replicate/replicate-python
- **Pricing**: https://replicate.com/pricing

## 🎯 Recommendation

For **production use** or if Hugging Face Spaces keep failing:
- ✅ Use Replicate API
- ✅ Get the real Hailuo model
- ✅ Reliable and fast
- ✅ Only pay for what you use

For **testing/development**:
- Use Demo Mode in the current app
- Or use Hugging Face Spaces (free but may be slow/unavailable)

---

**Ready to use the real Hailuo model? Set up Replicate now!** 🚀
