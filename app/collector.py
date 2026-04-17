import httpx

async def get_sector_data(sector: str) -> list:
    """Collect recent articles/news for the given sector."""
    try:
        url = f"[api.duckduckgo.com](https://api.duckduckgo.com/?q={sector}+India+market+news&format=json)"
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            data = response.json()
            related = [t["Text"] for t in data.get("RelatedTopics", []) if t.get("Text")]
            return related[:5]
    except Exception:
        return []
