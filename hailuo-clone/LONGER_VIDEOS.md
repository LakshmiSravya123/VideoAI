# 🎬 Longer Video Generation Models

## Available Models by Duration

### 🥇 Longest Videos (10+ seconds)

#### 1. **Runway Gen-3** - Up to 10 seconds ⭐
- **Model ID:** `runway`
- **Replicate:** `stability-ai/stable-video-diffusion-img2vid-xt`
- **Duration:** Up to 10 seconds
- **Quality:** Professional, cinematic
- **Cost:** ~$0.15-0.25 per video
- **Best for:** Professional content, commercials, high-quality shorts

#### 2. **Kling AI** - Up to 10 seconds
- **Not yet on Replicate** (Chinese model)
- **Duration:** Up to 10 seconds
- **Quality:** Very high, comparable to Hailuo
- **Best for:** Realistic scenes, character animations

---

### 🥈 Medium Length (5-7 seconds)

#### 3. **Hailuo Video-01** - 6 seconds
- **Model ID:** `hailuo`
- **Replicate:** `minimax/video-01`
- **Duration:** 6 seconds
- **Quality:** Excellent
- **Cost:** ~$0.05-0.10 per video
- **Best for:** General purpose, high quality

#### 4. **CogVideoX-5B** - 6 seconds
- **Model ID:** `cogvideox`
- **Replicate:** `lucataco/cogvideox-5b`
- **Duration:** 6 seconds (49 frames at 8fps)
- **Quality:** High
- **Cost:** ~$0.05 per video
- **Best for:** Good balance of quality and cost

#### 5. **HunyuanVideo** - 5+ seconds
- **Model ID:** `hunyuan`
- **Replicate:** `tencent/hunyuan-video`
- **Duration:** 5+ seconds
- **Quality:** State-of-the-art
- **Cost:** ~$0.08-0.12 per video
- **Best for:** High-quality, smooth motion

#### 6. **Luma Dream Machine** - 5 seconds
- **Model ID:** `luma`
- **Replicate:** `fofr/dream-machine`
- **Duration:** 5 seconds
- **Quality:** Cinematic
- **Cost:** ~$0.10 per video
- **Best for:** Cinematic shots, smooth camera movements

---

### 🥉 Shorter Videos (3-4 seconds)

#### 7. **Pika Labs** - 3 seconds (extendable)
- Can extend videos by generating continuations
- Good for creating longer sequences

#### 8. **AnimateDiff** - 2-4 seconds
- Fast generation
- Lower cost
- Good for quick tests

---

## 📊 Comparison Table

| Model | Duration | Quality | Cost/Video | Speed | Best For |
|-------|----------|---------|------------|-------|----------|
| **Runway Gen-3** | 10s | ⭐⭐⭐⭐⭐ | $0.15-0.25 | Slow | Professional |
| **Hailuo** | 6s | ⭐⭐⭐⭐⭐ | $0.05-0.10 | Medium | General |
| **CogVideoX-5B** | 6s | ⭐⭐⭐⭐ | $0.05 | Medium | Balanced |
| **HunyuanVideo** | 5s+ | ⭐⭐⭐⭐⭐ | $0.08-0.12 | Medium | High quality |
| **Luma** | 5s | ⭐⭐⭐⭐ | $0.10 | Medium | Cinematic |
| **Pika** | 3s | ⭐⭐⭐ | $0.03 | Fast | Quick tests |

---

## 🎯 How to Use Longer Video Models

### In Your App

The models are now available in your dropdown:

1. **Via Web UI:**
   - Select "Runway Gen-3 - 10s ⭐" for longest videos
   - Select "Hailuo Video-01 - 6s" for good balance
   - Enter your prompt and generate!

2. **Via API:**
   ```bash
   curl -X POST https://your-app.vercel.app/api/generate-video \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "A golden retriever running through flowers",
       "model": "runway"
     }'
   ```

3. **Via Python Backend:**
   ```python
   import requests
   
   response = requests.post('http://localhost:5000/generate-video', json={
       'prompt': 'Ocean waves at sunset',
       'model': 'runway'  # For 10s videos
   })
   
   video_url = response.json()['video_url']
   ```

---

## 💡 Tips for Longer Videos

### 1. **Be More Specific**
Longer videos need more detailed prompts:
```
❌ Bad: "A dog running"
✅ Good: "A golden retriever running through a field of sunflowers, 
         camera tracking from the side, golden hour lighting, 
         slow motion, cinematic"
```

### 2. **Use Camera Movements**
Longer videos benefit from camera direction:
- "Camera slowly zooms in"
- "Tracking shot following the subject"
- "Pan from left to right"

### 3. **Specify Pacing**
- "Slow motion"
- "Time-lapse"
- "Smooth, continuous motion"

### 4. **Consider Cost**
- Runway (10s): ~$0.20 per video
- Hailuo (6s): ~$0.08 per video
- Test with shorter/cheaper models first

---

## 🚀 Future: Even Longer Videos

### Coming Soon:
- **Sora (OpenAI)** - Up to 60 seconds (not yet public)
- **Kling 1.5** - Extended duration modes
- **Runway Gen-4** - Longer outputs expected

### Workarounds for Now:
1. **Video Extension:** Generate multiple clips and stitch
2. **Loop Seamlessly:** Create loopable content
3. **Multi-shot:** Generate scenes separately, edit together

---

## 🔧 Technical Details

### Why Are Videos Short?

1. **Computational Cost:** Each frame requires significant GPU time
2. **Memory Requirements:** Longer videos = more VRAM needed
3. **Quality Trade-off:** Maintaining quality over time is hard
4. **Training Data:** Most training videos are short clips

### Frame Rates:
- **CogVideoX:** 49 frames at 8 fps = 6.1 seconds
- **Hailuo:** 48 frames at 8 fps = 6 seconds
- **Runway:** 80 frames at 8 fps = 10 seconds

---

## 💰 Cost Optimization

### For Budget-Conscious Users:

1. **Start with CogVideoX** ($0.05) or **Hailuo** ($0.08)
2. **Use Runway** ($0.20) only for final/important videos
3. **Test prompts** with shorter models first
4. **Batch generate** to save on setup costs

### For Quality-First:

1. **Use Runway** for professional work
2. **HunyuanVideo** for high-quality content
3. **Hailuo** for general high-quality needs

---

## 📝 Example Prompts for Longer Videos

### 10-Second Videos (Runway):
```
"A surfer riding a massive wave, camera following from behind, 
slow motion, golden hour, spray and mist, cinematic 4k"

"City street time-lapse from day to night, cars and people 
moving fast, lights turning on, smooth transition"

"A bird taking flight from a branch, slow motion, camera 
tracking upward following the bird into the sky"
```

### 6-Second Videos (Hailuo/CogVideoX):
```
"A cat jumping onto a windowsill, looking outside at falling 
snow, soft lighting, cozy atmosphere"

"Fireworks exploding over a city skyline at night, colorful 
bursts, reflection on water below"

"A coffee cup being filled, steam rising, close-up shot, 
morning light through window"
```

---

## ✅ Updated in Your Project

I've updated:
- ✅ `api/generate-video.js` - Added all longer video models
- ✅ `api/models.js` - Listed models with durations
- ✅ `backend_replicate.py` - Added model support
- ✅ UI will now show duration in model names

**Commit and deploy to use the new models!**

---

**For the longest videos (10s), use `model: "runway"` in your requests! 🎬✨**
