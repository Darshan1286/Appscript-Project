import os
import httpx

# If you have a GEMINI_API_KEY, you can set it here
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze_market(sector: str, info: list) -> str:
    """Use LLM (Gemini or placeholder) to analyze trends."""
    if not info:
        return "Not enough data to analyze this sector."

    prompt = f"Analyze the current trade opportunities in India's {sector} sector:\n\n" + "\n".join(info[:5])

    # Placeholder logic if Gemini not available
    if not GEMINI_API_KEY:
        return f"The {sector} sector in India is showing moderate opportunities based on recent trends. Focus on R&D, digital innovation, and export potential."

    # Real API call (pseudo)
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "[generativelanguage.googleapis.com](https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText)",
                params={"key": GEMINI_API_KEY},
                json={"prompt": {"text": prompt}}
            )
            data = resp.json()
            return data.get("candidates", [{}])[0].get("output", "No insight available.")
    except Exception:
        return "Failed to fetch AI analysis due to API limits or config issues."
