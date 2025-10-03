"""
Configuration for multiple video generation models
Based on trending Hugging Face spaces and Hailuo-inspired features
"""

VIDEO_MODELS = {
    "cogvideox-5b": {
        "name": "CogVideoX-5B (THUDM)",
        "space_url": "THUDM/CogVideoX-5B-Space",
        "description": "High-quality text-to-video generation (6 seconds, 720p)",
        "type": "text-to-video",
        "features": ["high_quality", "longer_videos"],
        "max_frames": 49,
        "resolution": (720, 480),
        "api_name": "/infer",
        "params": {
            "num_inference_steps": 50,
            "guidance_scale": 6.0,
        }
    },
    "cogvideox-2b": {
        "name": "CogVideoX-2B (Faster)",
        "space_url": "THUDM/CogVideoX-2B-Space",
        "description": "Faster version of CogVideoX with good quality",
        "type": "text-to-video",
        "features": ["fast", "good_quality"],
        "max_frames": 49,
        "resolution": (720, 480),
        "api_name": "/infer",
        "params": {
            "num_inference_steps": 30,
            "guidance_scale": 6.0,
        }
    },
    "hunyuan-video": {
        "name": "HunyuanVideo (Tencent)",
        "space_url": "tencent/HunyuanVideo",
        "description": "State-of-the-art video generation by Tencent (may be slow/unavailable)",
        "type": "text-to-video",
        "features": ["sota", "high_quality"],
        "max_frames": 129,
        "resolution": (1280, 720),
        "api_name": "/generate",
        "params": {
            "num_inference_steps": 50,
        }
    },
    "stable-video-diffusion": {
        "name": "Stable Video Diffusion",
        "space_url": "multimodalart/stable-video-diffusion",
        "description": "Image-to-video animation (14-25 frames)",
        "type": "image-to-video",
        "features": ["image_animation", "stable"],
        "max_frames": 25,
        "resolution": (576, 576),
        "api_name": "/generate_video",
        "params": {
            "num_frames": 14,
            "fps": 7,
            "motion_bucket_id": 127,
        }
    },
    "demo": {
        "name": "Demo Mode (Test Video)",
        "space_url": "demo",
        "description": "Demo mode - returns sample video for testing UI",
        "type": "text-to-video",
        "features": ["demo", "instant"],
        "max_frames": 0,
        "resolution": (1920, 1080),
        "api_name": "/test",
        "params": {}
    }
}

# Camera movements inspired by Hailuo Director model
CAMERA_MOVEMENTS = [
    {"name": "Static", "tag": "", "description": "No camera movement"},
    {"name": "Zoom In", "tag": "[Zoom in]", "description": "Camera moves closer to subject"},
    {"name": "Zoom Out", "tag": "[Zoom out]", "description": "Camera moves away from subject"},
    {"name": "Pan Left", "tag": "[Pan left]", "description": "Camera pans to the left"},
    {"name": "Pan Right", "tag": "[Pan right]", "description": "Camera pans to the right"},
    {"name": "Tilt Up", "tag": "[Tilt up]", "description": "Camera tilts upward"},
    {"name": "Tilt Down", "tag": "[Tilt down]", "description": "Camera tilts downward"},
    {"name": "Tracking Shot", "tag": "[Tracking shot]", "description": "Camera follows subject"},
    {"name": "Dolly In", "tag": "[Dolly in]", "description": "Smooth forward movement"},
    {"name": "Dolly Out", "tag": "[Dolly out]", "description": "Smooth backward movement"},
    {"name": "Crane Shot", "tag": "[Crane shot]", "description": "Vertical camera movement"},
    {"name": "Shake", "tag": "[Shake]", "description": "Handheld camera effect"},
]

# Visual effects inspired by Hailuo
VISUAL_EFFECTS = [
    {"name": "None", "tag": "", "description": "No special effects"},
    {"name": "Cinematic", "tag": "cinematic lighting, film grain", "description": "Movie-like quality"},
    {"name": "Dramatic", "tag": "dramatic lighting, high contrast", "description": "Strong shadows and highlights"},
    {"name": "Soft", "tag": "soft lighting, gentle glow", "description": "Soft, diffused light"},
    {"name": "Golden Hour", "tag": "golden hour, warm sunset lighting", "description": "Warm, natural light"},
    {"name": "Foggy", "tag": "fog, misty atmosphere", "description": "Atmospheric fog effect"},
    {"name": "Rainy", "tag": "rain, wet surfaces, water droplets", "description": "Rain and wet environment"},
    {"name": "Slow Motion", "tag": "slow motion, high fps", "description": "Slow-motion effect"},
]

# Video styles
VIDEO_STYLES = [
    {"name": "Realistic", "tag": "photorealistic, 4k, high detail", "description": "Photorealistic style"},
    {"name": "Cinematic", "tag": "cinematic, movie scene, professional", "description": "Hollywood movie style"},
    {"name": "Anime", "tag": "anime style, animated", "description": "Japanese animation style"},
    {"name": "Cartoon", "tag": "cartoon style, animated", "description": "Western cartoon style"},
    {"name": "3D Render", "tag": "3D render, CGI, Pixar style", "description": "3D animated style"},
    {"name": "Vintage", "tag": "vintage film, retro, old footage", "description": "Old film aesthetic"},
    {"name": "Sci-Fi", "tag": "sci-fi, futuristic, cyberpunk", "description": "Science fiction style"},
    {"name": "Fantasy", "tag": "fantasy, magical, ethereal", "description": "Fantasy world style"},
]

# Example prompts categorized by use case
EXAMPLE_PROMPTS = {
    "Nature": [
        "A majestic waterfall cascading down mossy rocks in a lush rainforest",
        "Ocean waves crashing on a rocky shore at sunset with seagulls flying",
        "A field of sunflowers swaying in the breeze under a blue sky",
        "Northern lights dancing across the Arctic sky over snowy mountains",
    ],
    "Animals": [
        "A golden retriever running through a field of flowers at sunset",
        "A majestic eagle soaring through clouds above mountain peaks",
        "A playful dolphin jumping out of crystal clear ocean water",
        "A red fox walking through a snowy forest in winter",
    ],
    "Urban": [
        "City street with cars and pedestrians at night, neon lights reflecting on wet pavement",
        "Time-lapse of clouds moving over modern skyscrapers in downtown",
        "A busy coffee shop with people working on laptops, warm lighting",
        "Subway train arriving at platform with commuters waiting",
    ],
    "Fantasy": [
        "A magical portal opening in an ancient forest with glowing particles",
        "A dragon flying over a medieval castle at dawn",
        "Floating islands in the sky connected by glowing bridges",
        "A wizard casting a spell with colorful magical energy swirling",
    ],
    "Action": [
        "A sports car drifting around a corner on a race track",
        "A skateboarder performing tricks in an urban skate park",
        "A surfer riding a massive wave in slow motion",
        "A basketball player making a slam dunk in an arena",
    ]
}

def get_model_info(model_id):
    """Get information about a specific model"""
    return VIDEO_MODELS.get(model_id, VIDEO_MODELS["cogvideox-5b"])

def get_available_models():
    """Get list of available models"""
    return {k: {"name": v["name"], "description": v["description"], "type": v["type"]} 
            for k, v in VIDEO_MODELS.items()}

def build_enhanced_prompt(base_prompt, camera_movement="", visual_effect="", style=""):
    """Build an enhanced prompt with camera movements and effects (Hailuo-style)"""
    prompt_parts = []
    
    # Add style prefix if specified
    if style:
        prompt_parts.append(style)
    
    # Add base prompt
    prompt_parts.append(base_prompt)
    
    # Add camera movement
    if camera_movement:
        prompt_parts.append(camera_movement)
    
    # Add visual effects
    if visual_effect:
        prompt_parts.append(visual_effect)
    
    return ", ".join(filter(None, prompt_parts))
