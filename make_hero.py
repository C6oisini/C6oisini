#!/usr/bin/env python3
"""
Generate the hero image for the README (light + dark).

Style: editorial print — paper stock, large serif name, vermilion monogram,
thin index rules. No gradients, glows, or glass cards; flat color, hairlines,
and small mono type only.

Edit the variables below, then run:
    python3 make_hero.py

Outputs:
    assets/hero-light.svg
    assets/hero-dark.svg
"""

from pathlib import Path

# ----------------------------- edit here ---------------------------------
NAME = "ChenFan"
ALIAS = "CliiFord"
MONOGRAM = "CF"
LABEL = "PALM LAB"
SCHOOL = "SOUTHEAST UNIVERSITY"
TAGLINE = "Reinforcement Learning · Agents · Ad & LLM Systems"
MOTTO = "Mens et Manus"
LOCATION = "NANJING · CN"
CLASS_OF = "2029"

# Right-hand index: number, title, one-line note
DOMAINS = [
    ("01", "RL & TEST-TIME", "reinforcement learning · test-time training"),
    ("02", "AGENT SYSTEMS", "tool loops · skill reuse · evaluation"),
    ("03", "AD ALGORITHMS & INFRA", "ranking · LTV · multi-domain transfer"),
]
# -------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

SERIF = (
    "'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, "
    "'Times New Roman', serif"
)
SANS = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, "
    "sans-serif"
)
MONO = (
    "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
    "'Liberation Mono', monospace"
)

PALETTES = {
    "light": {
        "paper": "#f3eee3",
        "ink": "#17130d",
        "muted": "#6b6252",
        "faint": "#99907d",
        "accent": "#b83c12",
        "accent_ink": "#fbf6ea",
        "rule_opacity": "0.16",
        "hair_opacity": "0.055",
        "grid_opacity": "0.030",
        "mark_opacity": "0.50",
    },
    "dark": {
        "paper": "#12100b",
        "ink": "#f3eee3",
        "muted": "#a99e89",
        "faint": "#7d7462",
        "accent": "#ff6b3d",
        "accent_ink": "#12100b",
        "rule_opacity": "0.18",
        "hair_opacity": "0.070",
        "grid_opacity": "0.050",
        "mark_opacity": "0.55",
    },
}


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def hero(p: dict) -> str:
    name = esc(NAME)
    alias = esc(ALIAS)
    alias_upper = esc(ALIAS.upper())
    monogram = esc(MONOGRAM)
    label = esc(LABEL)
    school = esc(SCHOOL)
    tagline = esc(TAGLINE)
    motto = esc(MOTTO)
    location = esc(LOCATION)
    class_of = esc(CLASS_OF)

    # Paper rules: a very faint print grid
    grid = []
    for y in range(96, 521, 32):
        grid.append(
            f'<line x1="0" y1="{y}" x2="1600" y2="{y}" '
            f'stroke="{p["ink"]}" stroke-opacity="{p["grid_opacity"]}"/>'
        )

    # Four corner crop marks
    marks = []
    for x, y in ((34, 34), (1566, 34), (34, 496), (1566, 496)):
        marks.append(
            f'<path d="M{x - 9} {y}H{x + 9}M{x} {y - 9}V{y + 9}" '
            f'stroke="{p["accent"]}" stroke-opacity="{p["mark_opacity"]}" '
            f'stroke-width="1.2"/>'
        )

    # Right-hand index rows
    rows = []
    y = 212
    for num, title, note in DOMAINS:
        rows.append(
            f'<text x="984" y="{y}" font-family="{MONO}" font-size="15" '
            f'font-weight="600" letter-spacing="1.4" '
            f'fill="{p["accent"]}">{esc(num)}</text>'
        )
        rows.append(
            f'<text x="1032" y="{y}" font-family="{SANS}" font-size="28" '
            f'font-weight="800" letter-spacing="0.8" '
            f'fill="{p["ink"]}">{esc(title)}</text>'
        )
        rows.append(
            f'<text x="1032" y="{y + 27}" font-family="{MONO}" font-size="15" '
            f'fill="{p["muted"]}">{esc(note)}</text>'
        )
        rows.append(
            f'<line x1="984" y1="{y + 45}" x2="1536" y2="{y + 45}" '
            f'stroke="{p["ink"]}" stroke-opacity="{p["rule_opacity"]}"/>'
        )
        y += 72

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="520"
     viewBox="0 0 1600 520" fill="none" role="img"
     aria-label="{name} ({alias}) — {tagline}">
  <title>{name} ({alias}) — {tagline}</title>

  <!-- paper -->
  <rect width="1600" height="520" fill="{p["paper"]}"/>
  {''.join(grid)}

  <!-- header -->
  <rect x="64" y="42" width="9" height="9" fill="{p["accent"]}"/>
  <text x="86" y="54" font-family="{MONO}" font-size="15" letter-spacing="3.4"
        fill="{p["muted"]}">PROFILE / 001</text>
  <text x="1536" y="54" text-anchor="end" font-family="{MONO}" font-size="15"
        letter-spacing="2.6" fill="{p["muted"]}">{location}</text>
  <line x1="64" y1="72" x2="1536" y2="72"
        stroke="{p["ink"]}" stroke-opacity="{p["rule_opacity"]}"/>

  <!-- left: name -->
  <text x="64" y="146" font-family="{MONO}" font-size="16" font-weight="600"
        letter-spacing="2.2" fill="{p["accent"]}">{alias_upper} · {school} / {label}</text>
  <text x="61" y="292" font-family="{SERIF}" font-size="132" font-weight="700"
        letter-spacing="-3.5" fill="{p["ink"]}">{name}<tspan fill="{p["accent"]}">.</tspan></text>
  <line x1="64" y1="332" x2="820" y2="332"
        stroke="{p["ink"]}" stroke-opacity="{p["rule_opacity"]}"/>
  <text x="64" y="380" font-family="{SANS}" font-size="30" font-weight="500"
        fill="{p["ink"]}">{tagline}</text>

  <rect x="64" y="414" width="9" height="9" fill="{p["accent"]}"/>
  <text x="86" y="426" font-family="{SERIF}" font-size="24" font-style="italic"
        fill="{p["muted"]}">{motto}</text>
  <text x="64" y="486" font-family="{MONO}" font-size="13.5" letter-spacing="1.6"
        fill="{p["faint"]}">NANJING · MSC SOFTWARE ENGINEERING · CLASS OF {class_of}</text>

  <!-- center rule -->
  <line x1="944" y1="92" x2="944" y2="452"
        stroke="{p["ink"]}" stroke-opacity="{p["rule_opacity"]}"/>
  <line x1="942.5" y1="92" x2="942.5" y2="160"
        stroke="{p["accent"]}" stroke-width="3"/>

  <!-- right: index -->
  <text x="984" y="150" font-family="{MONO}" font-size="15" letter-spacing="2.6"
        fill="{p["muted"]}">SELECTED DOMAINS / 03</text>
  {''.join(rows)}

  <text x="984" y="448" font-family="{SERIF}" font-size="19" font-style="italic"
        fill="{p["muted"]}">Taking complex systems apart,</text>
  <text x="984" y="474" font-family="{SERIF}" font-size="19" font-style="italic"
        fill="{p["muted"]}">and putting them back together.</text>

  <!-- monogram seal -->
  <g>
    <rect x="1438" y="92" width="92" height="92" fill="{p["accent"]}"/>
    <rect x="1446" y="100" width="76" height="76" fill="none"
          stroke="{p["accent_ink"]}" stroke-opacity="0.55" stroke-width="1.2"/>
    <text x="1484" y="152" text-anchor="middle" font-family="{SERIF}"
          font-size="38" font-weight="700" letter-spacing="2"
          fill="{p["accent_ink"]}">{monogram}</text>
  </g>

  <!-- crop marks -->
  {''.join(marks)}

  <!-- footer -->
  <text x="64" y="512" font-family="{MONO}" font-size="12" letter-spacing="2.4"
        fill="{p["faint"]}" opacity="0.85">FIG. 01 — PROFILE OF {alias_upper}</text>
</svg>
'''


def main() -> None:
    for mode, palette in PALETTES.items():
        path = ASSETS / f"hero-{mode}.svg"
        path.write_text(hero(palette), encoding="utf-8")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
