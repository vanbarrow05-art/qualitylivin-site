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

# Page metadata. On the live site these go in GHL's page SEO settings (see snippets/SEO.md);
# the body Code element can't set them. The local preview carries the same values so they can
# be checked, plus an explicit noindex because it is a draft copy.
SEO = {
    "title": "Quality Living | Local Cleaning & Property Services",
    "description": "Explore residential cleaning, commercial janitorial and rental turnover services. "
                   "Tell Quality Living about your project and request an estimate.",
    "url": "https://qualitylivin.com/",
    "image": "https://storage.googleapis.com/funnel-ai-production/image-generation/wVyBbToZpkqhRQ0pkRSu/f02fa9cd-e2e5-48f9-b358-73bb9ef592bf.png",
    "icon": "https://storage.googleapis.com/funnel-ai-production/image-generation/wVyBbToZpkqhRQ0pkRSu/328fec49-8a6a-4bed-8d05-8d0703a44445.png",
}
schema = (root / "snippets" / "seo-schema.html").read_text(encoding="utf-8")
schema = schema[schema.index("<script"):]  # drop the instruction comment

preview = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SEO["title"]}</title>
<meta name="description" content="{SEO["description"]}">
<meta name="robots" content="noindex, nofollow"><!-- draft preview only: never copy to the live page -->
<link rel="canonical" href="{SEO["url"]}">
<link rel="icon" href="{SEO["icon"]}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Quality Living">
<meta property="og:title" content="{SEO["title"]}">
<meta property="og:description" content="{SEO["description"]}">
<meta property="og:url" content="{SEO["url"]}">
<meta property="og:image" content="{SEO["image"]}">
<meta name="twitter:card" content="summary_large_image">
{schema}
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
