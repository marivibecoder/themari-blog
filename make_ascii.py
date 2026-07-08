"""Convert a photo into ASCII art for the about section.

Usage: python3 make_ascii.py <photo.jpg> [cols]
Writes ascii_light.txt (dark chars on light bg) and ascii_dark.txt (inverted).
Then paste the contents into the .ascii-light / .ascii-dark <pre> blocks in index.html.
"""
import sys
from PIL import Image, ImageOps, ImageEnhance

RAMP = " .:-=+*#%@"


def to_ascii(im, cols=88, invert=False):
    im = im.convert("L")
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    w, h = im.size
    rows = max(1, int(cols * (h / w) * 0.5))
    im = im.resize((cols, rows))
    px = im.load()
    lines = []
    for y in range(rows):
        line = []
        for x in range(cols):
            v = px[x, y]
            if invert:
                v = 255 - v
            line.append(RAMP[min(len(RAMP) - 1, (255 - v) * len(RAMP) // 256)])
        lines.append("".join(line))
    return "\n".join(lines)


if __name__ == "__main__":
    path = sys.argv[1]
    cols = int(sys.argv[2]) if len(sys.argv) > 2 else 88
    im = Image.open(path)
    open("ascii_light.txt", "w").write(to_ascii(im, cols))
    open("ascii_dark.txt", "w").write(to_ascii(im, cols, invert=True))
    print(f"wrote ascii_light.txt / ascii_dark.txt ({cols} cols)")
