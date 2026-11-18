from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
import html
import json

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "cards"
CARDS.mkdir(exist_ok=True)

PAPER = "#f3f3ef"
PAPER_2 = "#e2e2de"
INK = "#111111"
SOFT = "#3a3a3c"
MUTED = "#6e6e73"
RULE = "#dcdcd7"
BLUE = "#2f55ff"

portrait = ROOT / "source-photo.png"

def ascii_rows():
    image = Image.open(portrait).convert("RGB")
    image = image.crop((192, 0, 960, 768))
    image = ImageOps.fit(image, (78, 48), method=Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.3)
    chars = " .:-=+*#%@"
    pixels = list(ImageOps.grayscale(image).getdata())
    rows = []
    for y in range(48):
        row = pixels[y * 78:(y + 1) * 78]
        rows.append("".join(chars[v * (len(chars) - 1) // 255] for v in row))
    return rows

def write(name, content):
    (CARDS / name).write_text(content, encoding="utf-8")

rows = ascii_rows()
portrait_lines = "\n".join(
    f'<text xml:space="preserve" x="552" y="{75 + i * 6.7:.1f}" fill="{INK}" '
    f'font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="6.4">'
    f'{html.escape(row)}</text>'
    for i, row in enumerate(rows)
)

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="420" viewBox="0 0 880 420" role="img" aria-label="Mouhamed Aziz Belghaieb. Software engineering student and full-stack developer.">
<rect width="880" height="420" rx="14" fill="{PAPER}"/>
<rect x="1" y="1" width="878" height="418" rx="13" fill="none" stroke="{RULE}"/>
<text x="44" y="82" font-family="monospace" font-size="12" letter-spacing="1" fill="{MUTED}">SOFTWARE ENGINEERING STUDENT</text>
<text x="44" y="180" font-family="Georgia,serif" font-size="72" letter-spacing="-2" fill="{INK}">Mouhamed Aziz</text>
<text x="44" y="248" font-family="Georgia,serif" font-size="72" letter-spacing="-2" font-style="italic" fill="{BLUE}">Belghaieb</text>
<text x="48" y="302" font-family="system-ui,sans-serif" font-size="18" fill="{SOFT}">I build full-stack systems, applied AI,</text>
<text x="48" y="329" font-family="system-ui,sans-serif" font-size="18" fill="{SOFT}">secure backends and connected devices.</text>
<text x="48" y="382" font-family="monospace" font-size="12" fill="{INK}">portfolio / linkedin / email</text>
{portrait_lines}
</svg>'''
write("hero.svg", hero)

data_file = ROOT / "data" / "contributions.json"
if data_file.exists():
    data = json.loads(data_file.read_text(encoding="utf-8"))
else:
    data = {"total_contributions": 51, "days": []}

days = data.get("days", [])
by_date = {day["date"]: day for day in days}
if not days:
    days = [{"date": f"2026-{month:02d}-{day:02d}", "count": 0, "level": 0} for month in range(11, 13) for day in range(1, 30)]

heat_cells = []
for i, day in enumerate(days[-217:]):
    level = day.get("level", 0)
    if level == 0:
        level = min(4, 1 if day.get("count", 0) > 0 else 0)
    colors = ["#e8e8e3", "#cfd5e6", "#a6b1d2", "#6f83ba", "#2f55ff"]
    col = i // 7
    row = i % 7
    x = 18 + col * 27
    y = 48 + row * 20
    heat_cells.append(f'<rect x="{x}" y="{y}" width="20" height="14" rx="3" fill="{colors[level]}"/>')

total = data.get("total_contributions", sum(day.get("count", 0) for day in days))
heatmap = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="210" viewBox="0 0 880 210" role="img" aria-label="{total} GitHub contributions">
<rect width="880" height="210" rx="14" fill="{PAPER}"/>
<rect x="1" y="1" width="878" height="208" rx="13" fill="none" stroke="{RULE}"/>
<text x="24" y="30" font-family="monospace" font-size="12" fill="{MUTED}">~/contributions --last-year</text>
{''.join(heat_cells)}
<text x="856" y="188" text-anchor="end" font-family="monospace" font-size="12" fill="{MUTED}">{total} contributions</text>
</svg>'''
write("heatmap.svg", heatmap)

activity = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="300" viewBox="0 0 880 300" role="img" aria-label="Engineering activity summary">
<rect width="880" height="300" rx="14" fill="{PAPER}"/>
<rect x="1" y="1" width="878" height="298" rx="13" fill="none" stroke="{RULE}"/>
<text x="24" y="34" font-family="monospace" font-size="12" fill="{MUTED}">~/activity --summary</text>
<g font-family="monospace">
<rect x="24" y="58" width="264" height="214" rx="10" fill="{PAPER_2}" stroke="{RULE}"/>
<text x="44" y="92" font-size="12" fill="{MUTED}">FEATURED PROJECTS</text><text x="44" y="138" font-size="28" font-weight="700" fill="{INK}">03</text><text x="44" y="166" font-size="12" fill="{SOFT}">TBIBI · ShopFlow · Prefacture</text><text x="44" y="214" font-size="12" fill="{BLUE}">full-stack delivery</text>
<rect x="308" y="58" width="264" height="214" rx="10" fill="{PAPER_2}" stroke="{RULE}"/>
<text x="328" y="92" font-size="12" fill="{MUTED}">PRIMARY STACK</text><text x="328" y="138" font-size="28" font-weight="700" fill="{INK}">JAVA</text><text x="328" y="166" font-size="12" fill="{SOFT}">Spring · REST · JWT · JPA</text><text x="328" y="214" font-size="12" fill="{BLUE}">backend engineering</text>
<rect x="592" y="58" width="264" height="214" rx="10" fill="{PAPER_2}" stroke="{RULE}"/>
<text x="612" y="92" font-size="12" fill="{MUTED}">CURRENT DIRECTION</text><text x="612" y="138" font-size="28" font-weight="700" fill="{INK}">AI + IOT</text><text x="612" y="166" font-size="12" fill="{SOFT}">OCR · ESP32 · connected systems</text><text x="612" y="214" font-size="12" fill="{BLUE}">applied engineering</text>
</g></svg>'''
write("activity.svg", activity)

worlds = [
    ("BUILD", "3", "systems", "TBIBI · ShopFlow · Prefacture"),
    ("STACK", "Java", "full-stack", "Spring · Next.js · PostgreSQL"),
    ("LEARN", "3", "systems", "AI · embedded · networking"),
]
for i, (label, number, word, detail) in enumerate(worlds, 1):
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="293" height="222" viewBox="0 0 293 222" role="img" aria-label="{label}: {number} {word}">
<rect width="293" height="222" rx="14" fill="{PAPER}"/><rect x="1" y="1" width="291" height="220" rx="13" fill="none" stroke="{RULE}"/>
<text x="24" y="34" font-family="monospace" font-size="12" fill="{MUTED}">{label}</text>
<text x="24" y="82" font-family="Georgia,serif" font-size="38" fill="{INK}">{number} <tspan font-style="italic">{word}</tspan></text>
<text x="24" y="112" font-family="monospace" font-size="11" fill="{SOFT}">{detail}</text>
<text x="24" y="190" font-family="monospace" font-size="12" fill="{BLUE}" class="arrow">EXPLORE  →</text>
</svg>'''
    write(f"world-{i}.svg", card)

title = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="76" viewBox="0 0 880 76" role="img" aria-label="What I'm coding">
<rect width="880" height="76" rx="14" fill="{PAPER}"/>
<text x="440" y="50" text-anchor="middle" font-family="Georgia,serif" font-size="34" fill="{INK}">What I'm coding</text>
</svg>'''
write("title-coding.svg", title)

repos = [
    ("TBIBI", "Medical web platform", "Java · Spring Boot · JWT"),
    ("ShopFlow", "Multi-role commerce", "Next.js · Spring Boot"),
    ("Cement Prefacture", "AI invoice workflow", "Java · Gemini OCR"),
]
for i, (name, subtitle, stack) in enumerate(repos, 1):
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="293" height="222" viewBox="0 0 293 222" role="img" aria-label="{name}: {subtitle}">
<rect width="293" height="222" rx="14" fill="{PAPER}"/><rect x="1" y="1" width="291" height="220" rx="13" fill="none" stroke="{RULE}"/>
<rect x="24" y="24" width="245" height="6" rx="3" fill="{BLUE}"/>
<text x="24" y="78" font-family="monospace" font-size="20" font-weight="700" fill="{INK}">{name}</text>
<text x="24" y="108" font-family="monospace" font-size="11" fill="{SOFT}">{subtitle}</text>
<text x="24" y="140" font-family="monospace" font-size="10" fill="{MUTED}">{stack}</text>
<text x="24" y="190" font-family="monospace" font-size="12" fill="{BLUE}">VIEW REPOSITORY  →</text>
</svg>'''
    write(f"repo-{i}.svg", card)

print("Generated profile cards")
