// Vercel Serverless Function: /api/models
// Provides available models and example prompts for the UI

export default function handler(req, res) {
  if (req.method !== "GET") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const models = {
    models: {
      hailuo: {
        name: "Hailuo Video-01 (MiniMax) - 6s",
        description: "High quality text-to-video, 6 seconds",
        type: "text-to-video",
        duration: "6s"
      },
      cogvideox: {
        name: "CogVideoX-5B - 6s",
        description: "High quality text-to-video, 6 seconds",
        type: "text-to-video",
        duration: "6s"
      },
      hunyuan: {
        name: "HunyuanVideo (Tencent) - 5s+",
        description: "State-of-the-art by Tencent, 5+ seconds",
        type: "text-to-video",
        duration: "5s+"
      },
      luma: {
        name: "Luma Dream Machine - 5s",
        description: "Cinematic quality, 5 seconds",
        type: "text-to-video",
        duration: "5s"
      },
      runway: {
        name: "Runway Gen-3 - 10s ⭐",
        description: "Professional quality, up to 10 seconds (longer!)",
        type: "text-to-video",
        duration: "10s"
      },
      demo: {
        name: "Demo Mode",
        description: "Instant sample video (no AI)",
        type: "text-to-video",
        duration: "varies"
      }
    },
    camera_movements: [
      { name: "Static", tag: "", description: "No camera movement" },
      { name: "Zoom In", tag: "[Zoom in]", description: "Camera moves closer" },
      { name: "Zoom Out", tag: "[Zoom out]", description: "Camera moves away" },
      { name: "Pan Left", tag: "[Pan left]", description: "Camera pans left" },
      { name: "Pan Right", tag: "[Pan right]", description: "Camera pans right" },
      { name: "Tilt Up", tag: "[Tilt up]", description: "Camera tilts up" },
      { name: "Tilt Down", tag: "[Tilt down]", description: "Camera tilts down" },
      { name: "Tracking Shot", tag: "[Tracking shot]", description: "Camera follows subject" }
    ],
    visual_effects: [
      { name: "None", tag: "", description: "No effect" },
      { name: "Cinematic", tag: "cinematic lighting, film grain", description: "Movie look" },
      { name: "Dramatic", tag: "dramatic lighting, high contrast", description: "Strong contrasts" },
      { name: "Soft", tag: "soft lighting, gentle glow", description: "Soft look" },
      { name: "Golden Hour", tag: "golden hour, warm sunset lighting", description: "Warm tones" },
      { name: "Slow Motion", tag: "slow motion, high fps", description: "Slow motion feel" }
    ],
    video_styles: [
      { name: "Realistic", tag: "photorealistic, 4k, high detail", description: "Photorealistic" },
      { name: "Cinematic", tag: "cinematic, movie scene, professional", description: "Film style" },
      { name: "Anime", tag: "anime style, animated", description: "Anime" },
      { name: "3D Render", tag: "3D render, CGI, Pixar style", description: "3D" }
    ],
    example_prompts: {
      Nature: [
        "A majestic waterfall cascading down mossy rocks in a lush rainforest",
        "Ocean waves crashing on a rocky shore at sunset with seagulls flying",
        "A field of sunflowers swaying in the breeze under a blue sky"
      ],
      Animals: [
        "A golden retriever running through a field of flowers at sunset",
        "A majestic eagle soaring through clouds above mountain peaks",
        "A playful dolphin jumping out of crystal clear ocean water"
      ],
      Urban: [
        "City street with cars and pedestrians at night, neon lights reflecting on wet pavement",
        "Time-lapse of clouds moving over modern skyscrapers in downtown",
        "A busy coffee shop with people working on laptops, warm lighting"
      ],
      Fantasy: [
        "A magical portal opening in an ancient forest with glowing particles",
        "A dragon flying over a medieval castle at dawn",
        "Floating islands in the sky connected by glowing bridges"
      ]
    }
  };

  return res.status(200).json(models);
}
