from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path
import html
import re

portrait = Path(r"C:\Users\azizb\AppData\Roaming\Code\agentSessionData\8e40f257-fade-4922-af29-159a5acaf3c7\attachments\127bd8b5-d5f9-4894-823b-04bb7ee2ebd8\aziz belghaieb.png")
output = Path(__file__).resolve().parents[1] / "assets" / "hero.svg"

image = Image.open(portrait).convert("RGB")
image = image.crop((192, 0, 960, 768))
image = ImageOps.fit(image, (72, 48), method=Image.Resampling.LANCZOS)
image = ImageEnhance.Contrast(image).enhance(1.18)

characters = " .:-=+*#%@"
pixels = list(ImageOps.grayscale(image).getdata())
rows = []
for y in range(48):
    row_pixels = pixels[y * 72:(y + 1) * 72]
    row = "".join(characters[value * (len(characters) - 1) // 255] for value in row_pixels)
    rows.append(row)

ascii_lines = "\n".join(
    f'<text x="239" y="{112 + y * 5.55:.2f}" text-anchor="middle" font-family="monospace" font-size="6.1" fill="#cdd6f4">{html.escape(row)}</text>'
    for y, row in enumerate(rows)
)

svg = output.read_text(encoding="utf-8")
svg = re.sub(
    r'  <text x="239" y="236" text-anchor="middle"[^>]*>.*?</text>',
    ascii_lines,
    svg,
    flags=re.S,
)
output.write_text(svg, encoding="utf-8")
print(f"Generated {len(rows)} ASCII rows")
