from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.auth import verify_user
from app.rate_limit import rate_limiter
from app.collector import get_sector_data
from app.analyzer import analyze_market
from app.utils import format_markdown_report

app = FastAPI(title="Trade Opportunities API")

security = HTTPBasic()

@app.get("/analyze/{sector}")
async def analyze_sector(sector: str, credentials: HTTPBasicCredentials = Depends(security)):
    user = verify_user(credentials)

    # Apply rate limiting
    if not rate_limiter.is_allowed(user):
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

    data = await get_sector_data(sector)
    if not data:
        raise HTTPException(status_code=404, detail="No data found for this sector.")

    analysis = await analyze_market(sector, data)
    report = format_markdown_report(sector, data, analysis)
    return {"sector": sector, "report": report}
