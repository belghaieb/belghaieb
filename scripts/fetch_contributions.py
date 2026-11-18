import json
import re
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = "belghaieb"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT = Path(__file__).resolve().parents[1] / "data" / "contributions.json"

response = requests.get(URL, headers={"User-Agent": "profile-readme-bot/1.0"}, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
cells = soup.select("td.ContributionCalendar-day")
if not cells:
    print("No GitHub contribution cells found", file=sys.stderr)
    sys.exit(1)

days = []
for td in cells:
    date = td.get("data-date")
    if not date:
        continue
    tooltip = soup.find("tool-tip", attrs={"for": td.get("id")}) if td.get("id") else None
    text = tooltip.get_text(strip=True) if tooltip else ""
    match = re.match(r"(\d+)", text)
    count = int(match.group(1)) if match and "no contributions" not in text.lower() else 0
    days.append({"date": date, "count": count, "level": int(td.get("data-level") or 0)})

days.sort(key=lambda day: day["date"])
total = sum(day["count"] for day in days)
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps({
    "username": USERNAME,
    "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "total_contributions": total,
    "days": days,
}, indent=2), encoding="utf-8")
print(f"Fetched {total} contributions")
