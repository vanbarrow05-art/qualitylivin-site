#!/usr/bin/env python3
"""Combine src/styles.css + src/page.html + src/script.js into files ready for GoHighLevel.

dist/ghl-paste.html  -> paste this into a GHL "Custom JS/HTML" (Code) element
dist/preview.html    -> open in a browser to preview locally
dist/magazine-feature-paste.html -> just the magazine section, to paste into another GHL page
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
css = (root / "src" / "styles.css").read_text()
html = (root / "src" / "page.html").read_text()

# <!-- @include file.html --> pulls in another file from src/
def include(match):
    return (root / "src" / match.group(1)).read_text()

html = re.sub(r"<!-- @include ([\w.-]+) -->", include, html)
js = (root / "src" / "script.js").read_text()

snippet = f"<style>\n{css}</style>\n\n{html}\n<script>\n{js}</script>\n"

preview = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview</title>
<style>body {{ margin: 0; }}</style>
</head>
<body>
{snippet}
</body>
</html>
"""

dist = root / "dist"
dist.mkdir(exist_ok=True)
(dist / "ghl-paste.html").write_text(snippet)
(dist / "preview.html").write_text(preview)
# The magazine feature on its own, for pasting into any GHL page (e.g. the builder page)
(dist / "magazine-feature-paste.html").write_text((root / "src" / "magazine-feature.html").read_text())
print("Built dist/ghl-paste.html, dist/preview.html and dist/magazine-feature-paste.html")
