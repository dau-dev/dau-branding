"""Generate dau logo SVGs (wordmark as outlines) and high-resolution PNGs.

Run from the repo root after `pnpm install`:

    python3 scripts/logos.py

Writes src/lib/assets/logo/{mark,disk,lockup,avatar}-on-{shadow,lit}.{svg,png}.
The avatar is a square tile with the chip drawn in ink only (no inner fills),
for places like a GitHub organization picture that cannot switch themes.
Requires fontTools, brotli, and rsvg-convert.
"""

import subprocess
from io import BytesIO
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "node_modules/@fontsource-variable/hanken-grotesk/files/hanken-grotesk-latin-wght-normal.woff2"
OUT = ROOT / "src/lib/assets/logo"

SURFACES = {"shadow": ("#eeede9", "#202021"), "lit": ("#202021", "#eeede9")}  # name: (ink, paper)

# Matches BrandMark.svelte: 64-unit mark, wordmark at 0.72 of the mark height,
# light 300 "dau" with a heavy 800 period, tracking -0.04em, gap 0.5em of the mark.
MARK = 64
WORD_SIZE = MARK * 0.72
TRACKING = -0.04
GAP = MARK * 0.5 * 0.5

# The chip's pins stop 4 units inside the viewBox; pad the wordmark's right edge to match.
INSET = 4

# Avatar: the chip at 70% of a solid tile, leaving room for rounded-corner crops.
AVATAR_PAD = 14

PNG_HEIGHT = {"mark": 2048, "disk": 2048, "lockup": 1024, "avatar": 1024}


def chip(ink: str, paper: str = "none") -> str:
    return (
        f'<path d="M10 22H4M10 32H4M10 42H4M54 22h6M54 32h6M54 42h6M22 10V4M32 10V4M42 10V4M22 54v6M32 54v6M42 54v6" '
        f'stroke="{ink}" stroke-width="2" stroke-linecap="square"/>'
        f'<rect x="10" y="10" width="44" height="44" rx="2" fill="{paper}" stroke="{ink}" stroke-width="2"/>'
        f'<circle cx="32" cy="32" r="12" fill="{paper}" stroke="{ink}" stroke-width="2"/>'
        f'<path d="M32 20a12 12 0 0 0 0 24z" fill="{ink}"/>'
    )


def disk(ink: str, paper: str) -> str:
    return (
        f'<circle cx="32" cy="32" r="29" fill="{paper}" stroke="{ink}" stroke-width="4"/>'
        f'<path d="M32 3a29 29 0 0 0 0 58z" fill="{ink}"/>'
    )


def instance(weight: int) -> TTFont:
    font = TTFont(BytesIO(FONT.read_bytes()))
    return instantiateVariableFont(font, {"wght": weight})


def wordmark(x0: float) -> tuple[str, float]:
    """Return outline path data for "dau." starting at x0, and the end x."""
    runs = [("dau", instance(300)), (".", instance(800))]
    upm = runs[0][1]["head"].unitsPerEm
    scale = WORD_SIZE / upm
    hhea = runs[0][1]["hhea"]
    # Line box of height WORD_SIZE centred on the mark, as in a flex row with line-height 1.
    content = (hhea.ascent - hhea.descent) * scale
    baseline = MARK / 2 - WORD_SIZE / 2 + (WORD_SIZE - content) / 2 + hhea.ascent * scale

    x = x0
    paths = []
    for text, font in runs:
        cmap, glyphs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
        for ch in text:
            name = cmap[ord(ch)]
            pen = SVGPathPen(glyphs)
            glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
            paths.append(pen.getCommands())
            x += hmtx[name][0] * scale + TRACKING * WORD_SIZE
    return " ".join(paths), x - TRACKING * WORD_SIZE


def avatar(ink: str, paper: str) -> str:
    size = MARK + 2 * AVATAR_PAD
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-AVATAR_PAD} {-AVATAR_PAD} {size} {size}" '
        f'width="{size}" height="{size}"><title>dau</title>'
        f'<rect x="{-AVATAR_PAD}" y="{-AVATAR_PAD}" width="{size}" height="{size}" fill="{paper}"/>{chip(ink)}</svg>\n'
    )


def svg(width: float, body: str) -> str:
    w = round(width, 2)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {MARK}" width="{w}" height="{MARK}">'
        f"<title>dau</title>{body}</svg>\n"
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    word_path, word_end = wordmark(MARK + GAP)
    for surface, (ink, paper) in SURFACES.items():
        files = {
            "mark": svg(MARK, chip(ink, paper)),
            "disk": svg(MARK, disk(ink, paper)),
            "lockup": svg(word_end + INSET, chip(ink, paper) + f'<path d="{word_path}" fill="{ink}"/>'),
            "avatar": avatar(ink, paper),
        }
        for kind, text in files.items():
            path = OUT / f"{kind}-on-{surface}.svg"
            path.write_text(text)
            subprocess.run(
                ["rsvg-convert", "-h", str(PNG_HEIGHT[kind]), str(path), "-o", str(path.with_suffix(".png"))],
                check=True,
            )
            print(path.relative_to(ROOT), path.with_suffix(".png").name)


if __name__ == "__main__":
    main()
