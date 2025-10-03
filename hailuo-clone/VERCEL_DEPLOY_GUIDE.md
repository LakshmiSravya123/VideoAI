# 🚀 Vercel Deployment Guide

## ✅ Your Project is Ready for Vercel!

All files have been created and pushed to GitHub. You now have:
- ✅ Serverless API functions in `/api`
- ✅ Frontend with relative API calls
- ✅ Support for 5 AI models (including 10s videos!)
- ✅ package.json with dependencies

---

## 📋 Quick Deploy (5 minutes)

### Method 1: Vercel Dashboard (Easiest)

1. **Go to Vercel**
   - Visit: https://vercel.com
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New" → "Project"
   - Select "Import Git Repository"
   - Choose: `LakshmiSravya123/VideoAI`

3. **Configure Project**
   - **Root Directory:** `hailuo-clone` ⚠️ IMPORTANT!
   - **Framework Preset:** None
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty)

4. **Add Environment Variable**
   - Click "Environment Variables"
   - Key: `REPLICATE_API_TOKEN`
   - Value: `r8_YOUR_TOKEN_HERE` (from https://replicate.com/account/api-tokens)
   - Apply to: Production, Preview, Development

5. **Deploy**
   - Click "Deploy"
   - Wait 1-2 minutes
   - You'll get a URL like: `https://video-ai-xyz.vercel.app`

6. **Test**
   - Visit: `https://your-url.vercel.app/index_enhanced.html`
   - Try generating a video!

---

### Method 2: Vercel CLI (Advanced)

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to project
cd /Users/sravyalu/VideoAI/hailuo-clone

# Deploy
vercel

# Follow prompts:
# - Link to existing project or create new
# - Confirm settings
# - Add REPLICATE_API_TOKEN when prompted

# Deploy to production
vercel --prod
```

---

## 🎬 Available Models After Deployment

Your deployed app will have:

1. **Runway Gen-3** - 10 seconds ⭐ (longest!)
2. **Hailuo Video-01** - 6 seconds (best quality/price)
3. **CogVideoX-5B** - 6 seconds (good balance)
4. **HunyuanVideo** - 5+ seconds (SOTA)
5. **Luma Dream Machine** - 5 seconds (cinematic)

---

## 🔧 Post-Deployment Setup

### 1. Set Custom Domain (Optional)
- Vercel Dashboard → Your Project → Settings → Domains
- Add: `video.yourdomain.com`
- Update DNS as instructed

### 2. Make index_enhanced.html the Homepage
Option A: Rename file
```bash
cd /Users/sravyalu/VideoAI/hailuo-clone
mv index_enhanced.html index.html
git add -A && git commit -m "Make enhanced UI the homepage" && git push
```

Option B: Add vercel.json
```json
{
  "rewrites": [
    { "source": "/", "destination": "/index_enhanced.html" }
  ]
}
```

### 3. Enable Analytics (Optional)
- Vercel Dashboard → Your Project → Analytics
- Enable Web Analytics
- Track usage and performance

---

## 📊 API Endpoints

Your deployed app will have:

- `GET /api/health` - Check API status
- `GET /api/models` - List available models
- `POST /api/generate-video` - Generate videos

### Example API Call:
```bash
curl -X POST https://your-url.vercel.app/api/generate-video \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A golden retriever running through flowers at sunset",
    "model": "runway"
  }'
```

---

## 💰 Cost Estimation

### Vercel Costs:
- **Hobby Plan:** FREE
  - 100GB bandwidth/month
  - Unlimited requests
  - Serverless functions included

### Replicate Costs (per video):
- **Runway Gen-3 (10s):** ~$0.20
- **Hailuo (6s):** ~$0.08
- **CogVideoX (6s):** ~$0.05
- **HunyuanVideo (5s):** ~$0.10
- **Luma (5s):** ~$0.10

**Example Monthly Cost:**
- 100 videos with Hailuo: ~$8
- 100 videos with Runway: ~$20
- Vercel hosting: FREE

---

## 🐛 Troubleshooting

### Issue: 404 on /api/generate-video
**Solution:** 
- Ensure Root Directory is set to `hailuo-clone`
- Check that `package.json` exists in that directory
- Redeploy

### Issue: 500 "Missing REPLICATE_API_TOKEN"
**Solution:**
- Add environment variable in Vercel Dashboard
- Settings → Environment Variables
- Redeploy after adding

### Issue: Functions timeout
**Solution:**
- Video generation can take 30-120 seconds
- Vercel Hobby: 10s timeout (may fail for long videos)
- Upgrade to Pro for 60s timeout
- Or use webhook/polling pattern

### Issue: CORS errors
**Solution:**
- Should not happen (same-origin)
- If using custom domain, ensure it's properly configured

### Issue: Slow first request
**Solution:**
- Cold start is normal (2-5 seconds)
- Subsequent requests are faster
- Consider keeping functions warm with cron job

---

## 🔒 Security Best Practices

### ✅ Already Implemented:
- API token in environment variables (not in code)
- .gitignore excludes .env files
- Serverless functions are isolated

### 🎯 Recommended:
1. **Rate Limiting:** Add rate limiting to prevent abuse
2. **Authentication:** Add user auth for production
3. **Input Validation:** Already implemented in API
4. **Monitoring:** Enable Vercel Analytics

---

## 📈 Scaling

### Current Setup:
- ✅ Serverless (auto-scales)
- ✅ No server management
- ✅ Pay per use

### For High Traffic:
1. **Add Caching:** Cache model metadata
2. **Add Queue:** Use queue for video generation
3. **Add Database:** Store generation history
4. **Add CDN:** Serve videos via CDN

---

## 🎯 Next Steps After Deployment

1. **Test All Models**
   - Try each model (runway, hailuo, cogvideox, etc.)
   - Test different prompts
   - Verify video quality

2. **Share Your App**
   - Share the Vercel URL
   - Add to your portfolio
   - Share on social media

3. **Monitor Usage**
   - Check Vercel Analytics
   - Monitor Replicate costs
   - Track popular models

4. **Iterate**
   - Add more features
   - Improve UI
   - Add user accounts

---

## 📝 Deployment Checklist

Before deploying:
- [x] API functions created (`/api/*.js`)
- [x] package.json with dependencies
- [x] Frontend updated to use `/api` endpoints
- [x] .gitignore excludes sensitive files
- [x] All changes pushed to GitHub
- [ ] Replicate API token ready
- [ ] Vercel account created
- [ ] Project imported to Vercel
- [ ] Environment variable added
- [ ] Deployment successful
- [ ] Test video generation works

---

## 🎉 You're Ready!

Your project is fully prepared for Vercel deployment with:
- ✅ 5 AI models (up to 10s videos)
- ✅ Beautiful animated UI
- ✅ Serverless architecture
- ✅ Complete documentation
- ✅ GitHub repository

**Just deploy and start generating videos! 🚀✨**

---

## 📞 Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review Vercel logs in Dashboard
3. Check GitHub Issues
4. Vercel Discord: https://vercel.com/discord

**Your deployment URL will be:**
`https://video-ai-[random].vercel.app`

(You can customize this in Vercel settings)
