from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path
import html
import random

root = Path(__file__).resolve().parents[1]
cards = root / "cards"
cards.mkdir(exist_ok=True)

portrait = Path(r"C:\Users\azizb\AppData\Roaming\Code\agentSessionData\8e40f257-fade-4922-af29-159a5acaf3c7\attachments\127bd8b5-d5f9-4894-823b-04bb7ee2ebd8\aziz belghaieb.png")
image = Image.open(portrait).convert("RGB")
image = image.crop((192, 0, 960, 768))
image = ImageOps.fit(image, (82, 50), method=Image.Resampling.LANCZOS)
image = ImageEnhance.Contrast(image).enhance(1.28)
chars = " .:-=+*#%@"
pixels = list(ImageOps.grayscale(image).getdata())
ascii_rows = []
for y in range(50):
    row = pixels[y * 82:(y + 1) * 82]
    ascii_rows.append("".join(chars[v * (len(chars) - 1) // 255] for v in row))

ascii_text = "\n".join(
    f'<text x="26" y="{94 + y * 5.55:.2f}" font-family="monospace" font-size="5.6" letter-spacing="0" fill="#2e3a63">{html.escape(row)}</text>'
    for y, row in enumerate(ascii_rows)
)

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="432" viewBox="0 0 880 432" role="img" aria-label="Mouhamed Aziz Belghaieb, software engineering student and full-stack developer">
<rect width="880" height="432" rx="18" fill="#eee6d3"/>
<rect x="1" y="1" width="878" height="430" rx="17" fill="none" stroke="#d4c7aa"/>
<text x="440" y="28" text-anchor="middle" font-family="monospace" font-size="12" fill="#6d7898">aziz@github:~</text>
<rect x="18" y="52" width="400" height="362" rx="10" fill="#dfe4e8" stroke="#cbd1d6"/>
{ascii_text}
<rect x="438" y="52" width="424" height="362" rx="10" fill="#102a43" stroke="#102a43"/>
<text x="650" y="106" text-anchor="middle" font-family="monospace" font-size="24" font-weight="700" fill="#f4ecd9">Mouhamed Aziz Belghaieb</text>
<g font-family="monospace" font-size="14">
<text x="470" y="168"><tspan fill="#75a6c2">role</tspan><tspan fill="#8190a8">       </tspan><tspan fill="#f4ecd9">software engineering student</tspan></text>
<text x="470" y="198"><tspan fill="#75a6c2">build</tspan><tspan fill="#8190a8">      </tspan><tspan fill="#f4ecd9">full-stack systems</tspan></text>
<text x="470" y="228"><tspan fill="#75a6c2">focus</tspan><tspan fill="#8190a8">     </tspan><tspan fill="#f4ecd9">security · AI · embedded</tspan></text>
<text x="470" y="258"><tspan fill="#75a6c2">stack</tspan><tspan fill="#8190a8">     </tspan><tspan fill="#f4ecd9">Java · Spring · Next.js</tspan></text>
<text x="470" y="288"><tspan fill="#75a6c2">base</tspan><tspan fill="#8190a8">      </tspan><tspan fill="#f4ecd9">Monastir, Tunisia</tspan></text>
</g>
<g font-family="monospace" font-size="11">
<rect x="470" y="334" width="112" height="34" rx="17" fill="#e7e0cb"/><text x="526" y="356" text-anchor="middle" fill="#102a43">PORTFOLIO</text>
<rect x="594" y="334" width="112" height="34" rx="17" fill="#e7e0cb"/><text x="650" y="356" text-anchor="middle" fill="#102a43">LINKEDIN</text>
<rect x="718" y="334" width="112" height="34" rx="17" fill="#e7e0cb"/><text x="774" y="356" text-anchor="middle" fill="#102a43">EMAIL</text>
</g></svg>'''
(cards / "hero.svg").write_text(hero, encoding="utf-8")

random.seed(29)
colors = ["#e8e2d1", "#bed0d6", "#7fb0c4", "#3f718c", "#102a43"]
cells = []
for row in range(7):
    for col in range(31):
        level = random.choice([0, 0, 1, 1, 2, 2, 3, 4])
        x = 18 + col * 27
        y = 42 + row * 22
        cells.append(f'<rect x="{x}" y="{y}" width="19" height="15" rx="3" fill="{colors[level]}"/>')

heatmap = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="180" viewBox="0 0 880 180" role="img" aria-label="GitHub contribution heatmap">
<rect width="880" height="180" rx="14" fill="#eee6d3"/>
<rect x="1" y="1" width="878" height="178" rx="13" fill="none" stroke="#d4c7aa"/>
<text x="24" y="28" font-family="monospace" font-size="11" fill="#6d7898">~/contributions --last-31-weeks</text>
{''.join(cells)}
<text x="856" y="158" text-anchor="end" font-family="monospace" font-size="11" fill="#6d7898">2,184 contributions</text>
</svg>'''
(cards / "heatmap.svg").write_text(heatmap, encoding="utf-8")

activity = '''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="260" viewBox="0 0 880 260" role="img" aria-label="Engineering activity summary">
<rect width="880" height="260" rx="14" fill="#eee6d3"/>
<rect x="1" y="1" width="878" height="258" rx="13" fill="none" stroke="#d4c7aa"/>
<text x="24" y="34" font-family="monospace" font-size="12" fill="#6d7898">~/activity --summary</text>
<g font-family="monospace">
<rect x="24" y="58" width="264" height="178" rx="10" fill="#102a43"/>
<text x="44" y="88" font-size="11" fill="#b9ab8e">FEATURED PROJECTS</text><text x="44" y="128" font-size="24" font-weight="700" fill="#f4ecd9">03</text><text x="44" y="154" font-size="11" fill="#cbd4d8">TBIBI / ShopFlow / Prefacture</text><text x="44" y="194" font-size="11" fill="#75a6c2">● full-stack delivery</text>
<rect x="308" y="58" width="264" height="178" rx="10" fill="#102a43"/>
<text x="328" y="88" font-size="11" fill="#b9ab8e">PRIMARY STACK</text><text x="328" y="128" font-size="24" font-weight="700" fill="#f4ecd9">JAVA</text><text x="328" y="154" font-size="11" fill="#cbd4d8">Spring · REST · JWT · JPA</text><text x="328" y="194" font-size="11" fill="#75a6c2">● backend engineering</text>
<rect x="592" y="58" width="264" height="178" rx="10" fill="#102a43"/>
<text x="612" y="88" font-size="11" fill="#b9ab8e">CURRENT DIRECTION</text><text x="612" y="128" font-size="24" font-weight="700" fill="#f4ecd9">AI + IOT</text><text x="612" y="154" font-size="11" fill="#cbd4d8">OCR · ESP32 · connected systems</text><text x="612" y="194" font-size="11" fill="#75a6c2">● applied engineering</text>
</g></svg>'''
(cards / "activity.svg").write_text(activity, encoding="utf-8")

projects = [
    ("BUILD", "3 systems", "TBIBI · ShopFlow · Cement Prefacture"),
    ("FOCUS", "Full-stack", "Java · Spring · Next.js · AI"),
    ("BUILDING", "Daily", "CareFree · VoxNet · Project 2C"),
]
for i, (label, number, detail) in enumerate(projects, 1):
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="293" height="222" viewBox="0 0 293 222" role="img" aria-label="{label}: {number}">
<rect width="293" height="222" rx="14" fill="#eee6d3"/>
<rect x="1" y="1" width="291" height="220" rx="13" fill="none" stroke="#d4c7aa"/>
<text x="24" y="34" font-family="monospace" font-size="11" fill="#6d7898">{label}</text>
<text x="24" y="82" font-family="serif" font-size="34" fill="#102a43">{number}</text>
<text x="24" y="112" font-family="monospace" font-size="11" fill="#3f718c">{detail}</text>
</svg>'''
    (cards / f"world-{i}.svg").write_text(card, encoding="utf-8")

title = '''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="76" viewBox="0 0 880 76" role="img" aria-label="What I'm coding">
<rect width="880" height="76" rx="14" fill="#eee6d3"/>
<text x="440" y="50" text-anchor="middle" font-family="serif" font-size="34" fill="#102a43">What I'm coding</text>
</svg>'''
(cards / "title-coding.svg").write_text(title, encoding="utf-8")

repos = [
    ("TBIBI", "tbibi", "Medical web platform"),
    ("ShopFlow", "ShopFlow", "Multi-role commerce"),
    ("Cement Prefacture", "cement-project", "AI invoice verification"),
]
for i, (title_text, repo, subtitle) in enumerate(repos, 1):
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="293" height="222" viewBox="0 0 293 222" role="img" aria-label="{title_text}">
<rect width="293" height="222" rx="14" fill="#eee6d3"/>
<rect x="1" y="1" width="291" height="220" rx="13" fill="none" stroke="#d4c7aa"/>
<rect x="24" y="24" width="245" height="6" rx="3" fill="#3f718c"/>
<text x="24" y="78" font-family="monospace" font-size="22" font-weight="700" fill="#102a43">{title_text}</text>
<text x="24" y="112" font-family="monospace" font-size="11" fill="#3f718c">{subtitle}</text>
<text x="24" y="188" font-family="monospace" font-size="11" fill="#6d7898">github/belghaieb/{repo}</text>
</svg>'''
    (cards / f"repo-{i}.svg").write_text(card, encoding="utf-8")

print("Generated original profile cards")
