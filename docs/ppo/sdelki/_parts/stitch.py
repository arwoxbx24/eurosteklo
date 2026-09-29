#!/usr/bin/env python3
"""Склейка карты «Сделки» из слоёв karta-A/B/C.svg.html → karta.svg.html (механически)."""
import re
from pathlib import Path

P = Path(__file__).parent
W, GAP = 2600, 40
defs = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
        '<path d="M0,0L10,5L0,10z" fill="#1f2937"/></marker>'
        '<marker id="arrg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
        '<path d="M0,0L10,5L0,10z" fill="#8a94a3"/></marker></defs>')
PT = re.compile(r'<g class="pt">.*?</g>', re.S)
y, body, pts, bounds = 0, [], [], []
for L in "ABC":
    f = P / f"karta-{L}.svg.html"
    s = f.read_text(encoding="utf8")
    h = int(re.search(r"<!--\s*height:\s*(\d+)\s*-->", s).group(1))
    for g in PT.findall(s):  # точки — поверх, в глобальных координатах
        g = re.sub(r'(cy|y)="([\d.]+)"', lambda m: f'{m.group(1)}="{float(m.group(2)) + y:g}"', g)
        pts.append(g)
    body.append(f'<g transform="translate(0,{y})">{PT.sub("", s)}</g>')
    y += h + GAP
    bounds.append(y - GAP // 2)
H = y - GAP
svg = (f'<!-- layers: A<{bounds[0]} B<{bounds[1]} -->\n'
       f'<svg class="map" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,sans-serif">'
       f'{defs}<rect width="{W}" height="{H}" fill="#fff"/>{"".join(body)}{"".join(pts)}</svg>\n')
(P / "karta.svg.html").write_text(svg, encoding="utf8")
print("ok", W, H, "точек", len(pts))
