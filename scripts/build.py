#!/usr/bin/env python3
"""Combine src/styles.css + src/page.html into files ready for GoHighLevel.

dist/ghl-paste.html  -> paste this into a GHL "Custom JS/HTML" (Code) element
dist/preview.html    -> open in a browser to preview locally
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
css = (root / "src" / "styles.css").read_text()
html = (root / "src" / "page.html").read_text()

snippet = f"<style>\n{css}</style>\n\n{html}"

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
print("Built dist/ghl-paste.html and dist/preview.html")
