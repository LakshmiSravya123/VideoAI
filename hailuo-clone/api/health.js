// Vercel Serverless Function: /api/health
export default function handler(req, res) {
  if (req.method !== "GET") {
    return res.status(405).json({ error: "Method not allowed" });
  }
  return res.status(200).json({
    status: "healthy",
    provider: process.env.REPLICATE_API_TOKEN ? "replicate" : "none",
    timestamp: new Date().toISOString(),
  });
}
