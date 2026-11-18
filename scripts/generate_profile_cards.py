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
image = ImageOps.fit(image, (58, 40), method=Image.Resampling.LANCZOS)
image = ImageEnhance.Contrast(image).enhance(1.2)
characters = " .:-=+*#%@"
pixels = list(ImageOps.grayscale(image).getdata())
rows = []
for y in range(40):
    row_pixels = pixels[y * 58:(y + 1) * 58]
    row = "".join(characters[value * (len(characters) - 1) // 255] for value in row_pixels)
    rows.append(html.escape(row))

ascii_lines = "\n".join(
    f'<text x="30" y="{112 + y * 7:.1f}" font-family="monospace" font-size="7" letter-spacing="0" fill="#eadcc8">{row}</text>'
    for y, row in enumerate(rows)
)

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="430" viewBox="0 0 1000 430">
<rect width="1000" height="430" rx="18" fill="#f1eadc"/>
<rect x="1" y="1" width="998" height="428" rx="17" fill="none" stroke="#d5cbb8" stroke-width="2"/>
<rect width="1000" height="46" rx="18" fill="#102a43"/>
<circle cx="24" cy="23" r="7" fill="#f38ba8"/><circle cx="48" cy="23" r="7" fill="#f9e2af"/><circle cx="72" cy="23" r="7" fill="#a6e3a1"/>
<text x="500" y="28" text-anchor="middle" font-family="monospace" font-size="14" fill="#eadcc8">aziz@github:~</text>
<rect x="24" y="68" width="430" height="338" rx="10" fill="#102a43" stroke="#c6bdaa"/>
{ascii_lines}
<rect x="478" y="68" width="498" height="338" rx="10" fill="#102a43" stroke="#c6bdaa"/>
<text x="504" y="112" font-family="monospace" font-size="24" font-weight="700" fill="#f7efe1">Mouhamed Aziz Belghaieb</text>
<g font-family="monospace" font-size="15">
<text x="504" y="176"><tspan fill="#75b7d3">role</tspan><tspan fill="#baa98e">       </tspan><tspan fill="#f7efe1">software engineering student</tspan></text>
<text x="504" y="206"><tspan fill="#75b7d3">build</tspan><tspan fill="#baa98e">      </tspan><tspan fill="#f7efe1">full-stack systems</tspan></text>
<text x="504" y="236"><tspan fill="#75b7d3">focus</tspan><tspan fill="#baa98e">     </tspan><tspan fill="#f7efe1">security · AI · embedded</tspan></text>
<text x="504" y="266"><tspan fill="#75b7d3">stack</tspan><tspan fill="#baa98e">     </tspan><tspan fill="#f7efe1">Java · Spring · Next.js</tspan></text>
<text x="504" y="296"><tspan fill="#75b7d3">base</tspan><tspan fill="#baa98e">      </tspan><tspan fill="#f7efe1">Monastir, Tunisia</tspan></text>
</g>
<g font-family="monospace" font-size="13">
<rect x="504" y="332" width="118" height="34" rx="17" fill="#172554"/><text x="563" y="354" text-anchor="middle" fill="#60a5fa">PORTFOLIO</text>
<rect x="632" y="332" width="112" height="34" rx="17" fill="#172554"/><text x="688" y="354" text-anchor="middle" fill="#60a5fa">LINKEDIN</text>
<rect x="754" y="332" width="92" height="34" rx="17" fill="#172554"/><text x="800" y="354" text-anchor="middle" fill="#60a5fa">EMAIL</text>
</g></svg>'''
(cards / "hero.svg").write_text(hero, encoding="utf-8")

random.seed(18)
cells = []
for row in range(7):
    for col in range(31):
        level = random.choice([0, 0, 1, 1, 2, 2, 3, 4])
        colors = ["#d8cfbd", "#b5c8ce", "#75b7d3", "#377ea1", "#102a43"]
        x = 18 + col * 30
        y = 42 + row * 30
        cells.append(f'<rect x="{x}" y="{y}" width="21" height="21" rx="4" fill="{colors[level]}"/>')

heatmap = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="180" viewBox="0 0 1000 180">
<rect width="1000" height="180" rx="14" fill="#f1eadc"/>
<rect x="1" y="1" width="998" height="178" rx="13" fill="none" stroke="#d5cbb8"/>
<text x="24" y="28" font-family="monospace" font-size="12" fill="#6b6457">~/contributions --last-31-weeks</text>
{''.join(cells)}
<text x="958" y="160" text-anchor="end" font-family="monospace" font-size="12" fill="#6b6457">2,184 contributions</text>
</svg>'''
(cards / "heatmap.svg").write_text(heatmap, encoding="utf-8")

activity = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" viewBox="0 0 1000 280">
<rect width="1000" height="280" rx="14" fill="#f1eadc"/>
<rect x="1" y="1" width="998" height="278" rx="13" fill="none" stroke="#d5cbb8"/>
<text x="28" y="38" font-family="monospace" font-size="13" fill="#6b6457">~/activity --summary</text>
<g font-family="monospace">
<rect x="28" y="62" width="300" height="190" rx="10" fill="#102a43" stroke="#c6bdaa"/>
<text x="48" y="94" font-size="12" fill="#baa98e">FEATURED PROJECTS</text>
<text x="48" y="132" font-size="21" font-weight="700" fill="#f7efe1">03</text>
<text x="48" y="158" font-size="12" fill="#d9cdb7">TBIBI / ShopFlow / Prefacture</text>
<text x="48" y="198" font-size="12" fill="#75b7d3">● full-stack delivery</text>
<rect x="350" y="62" width="300" height="190" rx="10" fill="#102a43" stroke="#c6bdaa"/>
<text x="370" y="94" font-size="12" fill="#baa98e">PRIMARY STACK</text>
<text x="370" y="132" font-size="21" font-weight="700" fill="#f7efe1">JAVA</text>
<text x="370" y="158" font-size="12" fill="#d9cdb7">Spring · REST · JWT · JPA</text>
<text x="370" y="198" font-size="12" fill="#75b7d3">● backend engineering</text>
<rect x="672" y="62" width="300" height="190" rx="10" fill="#102a43" stroke="#c6bdaa"/>
<text x="692" y="94" font-size="12" fill="#baa98e">CURRENT DIRECTION</text>
<text x="692" y="132" font-size="21" font-weight="700" fill="#f7efe1">AI + IOT</text>
<text x="692" y="158" font-size="12" fill="#d9cdb7">OCR · ESP32 · connected systems</text>
<text x="692" y="198" font-size="12" fill="#75b7d3">● applied engineering</text>
</g></svg>'''
(cards / "activity.svg").write_text(activity, encoding="utf-8")

projects = [
    ("TBIBI", "Medical web platform", "Patients · doctors · appointments", "#75b7d3", "tbibi"),
    ("ShopFlow", "Multi-role commerce", "Products · carts · orders · roles", "#75b7d3", "ShopFlow"),
    ("Prefacture", "AI document workflow", "OCR · verification · dashboard", "#75b7d3", "cement-project"),
]

for index, (title, subtitle, detail, accent, repo) in enumerate(projects):
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="330" height="230" viewBox="0 0 330 230">
<rect width="330" height="230" rx="14" fill="#102a43"/>
<rect x="1" y="1" width="328" height="228" rx="13" fill="none" stroke="#c6bdaa"/>
<rect x="20" y="20" width="290" height="6" rx="3" fill="{accent}"/>
<text x="20" y="68" font-family="monospace" font-size="25" font-weight="700" fill="#f7efe1">{title}</text>
<text x="20" y="96" font-family="monospace" font-size="13" fill="{accent}">{subtitle}</text>
<text x="20" y="128" font-family="monospace" font-size="12" fill="#d9cdb7">{detail}</text>
<rect x="20" y="160" width="290" height="44" rx="8" fill="#f1eadc" stroke="#c6bdaa"/>
<text x="165" y="187" text-anchor="middle" font-family="monospace" font-size="12" fill="#102a43">VIEW REPOSITORY  →</text>
</svg>'''
    (cards / f"project-{index + 1}.svg").write_text(card, encoding="utf-8")

print("Generated profile card assets")
