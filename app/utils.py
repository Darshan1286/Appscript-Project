from datetime import datetime

def format_markdown_report(sector: str, info: list, analysis: str) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    md = f"""# Market Analysis Report: {sector.capitalize()}

**Generated at:** {now}

---

## 📰 Recent Market Highlights
"""
    for i, item in enumerate(info, 1):
        md += f"{i}. {item}\n"

    md += f"""

---

## 💡 AI Market Insights

{analysis}

---

*End of Report*
"""
    return md
