#!/usr/bin/env python3
"""Combine src/styles.css + src/page.html + src/script.js into files ready for GoHighLevel.

dist/ghl-paste.html  -> paste this into a GHL "Custom JS/HTML" (Code) element
dist/preview.html    -> open in a browser to preview locally
dist/magazine-feature-paste.html -> just the magazine section, to paste into another GHL page
dist/directory-paste.html -> just the provider map/directory, to paste into another GHL page
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent


def read(name):
    # Explicit UTF-8: Windows would otherwise default to cp1252 and fail on characters like é and →
    return (root / "src" / name).read_text(encoding="utf-8")


css = read("styles.css")
html = read("page.html")

# <!-- @include file.html --> pulls in another file from src/
html = re.sub(r"<!-- @include ([\w.-]+) -->", lambda m: read(m.group(1)), html)
js = read("script.js")

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
(dist / "ghl-paste.html").write_text(snippet, encoding="utf-8")
(dist / "preview.html").write_text(preview, encoding="utf-8")
# The magazine feature on its own, for pasting into any GHL page (e.g. the builder page)
(dist / "magazine-feature-paste.html").write_text(read("magazine-feature.html"), encoding="utf-8")
# The provider directory/map on its own (e.g. to replace the builder page's directory element)
(dist / "directory-paste.html").write_text(read("directory.html"), encoding="utf-8")
print("Built dist/ghl-paste.html, dist/preview.html, dist/magazine-feature-paste.html and dist/directory-paste.html")
