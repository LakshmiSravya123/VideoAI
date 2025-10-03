// Vercel Serverless Function: /api/generate-video
// Text-to-video via Replicate (Hailuo or CogVideoX)

import Replicate from "replicate";

const replicate = new Replicate({ apiToken: process.env.REPLICATE_API_TOKEN });

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  try {
    const { prompt = "", model = "hailuo" } = req.body || {};

    if (!process.env.REPLICATE_API_TOKEN) {
      return res.status(500).json({ error: "Missing REPLICATE_API_TOKEN env var" });
    }

    if (!prompt || typeof prompt !== "string" || prompt.trim().length < 3) {
      return res.status(400).json({ error: "Prompt must be a non-empty string (min 3 chars)" });
    }

    // Map incoming model id to Replicate model name
    const modelMap = {
      hailuo: "minimax/video-01", // Real Hailuo Video-01 (6s)
      cogvideox: "lucataco/cogvideox-5b", // CogVideoX-5B (6s)
      hunyuan: "tencent/hunyuan-video", // HunyuanVideo (5s+)
      luma: "fofr/dream-machine", // Luma Dream Machine (5s)
      runway: "stability-ai/stable-video-diffusion-img2vid-xt", // Runway (10s)
    };

    const replicateModel = modelMap[model] || modelMap.hailuo;

    const output = await replicate.run(replicateModel, {
      input: { prompt: prompt.trim() },
    });

    // Replicate often returns a URL or an array of URLs
    const videoUrl = Array.isArray(output) ? output[0] : output;

    if (!videoUrl) {
      return res.status(500).json({ error: "No video URL returned from provider" });
    }

    return res.status(200).json({
      video_url: videoUrl,
      prompt: prompt.trim(),
      model,
      timestamp: new Date().toISOString(),
      service: "replicate",
    });
  } catch (err) {
    console.error("/api/generate-video error:", err);
    return res.status(500).json({ error: `Video generation failed: ${err.message || String(err)}` });
  }
}
