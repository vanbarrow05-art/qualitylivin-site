# Quality Living — qualitylivin.com

The qualitylivin.com homepage as clean HTML/CSS, kept in git and pasted into GoHighLevel.

## Files

- `src/page.html`: page content (edit this)
- `src/styles.css`: styles (edit this; brand colors + hero image are at the top)
- `dist/ghl-paste.html`: **the file you paste into GHL** (generated)
- `dist/preview.html`: open in a browser to preview (generated)
- `original/`: snapshot of the original GHL site (reference only)

## Update workflow

1. Edit `src/page.html` and/or `src/styles.css`
2. Build: `python3 scripts/build.py`
3. Preview: open `dist/preview.html` in your browser
4. Commit and push: `git add -A && git commit -m "Update page" && git push`
5. Paste into GHL (below)

You can also edit `src/` directly on github.com, but then someone must run the build step before `dist/ghl-paste.html` updates.

## Pasting into GoHighLevel

1. Open the qualitylivin.com page in the GHL Sites builder
2. Add one section, set it to **full width**, and set all padding/margins to 0
3. Add a **Code** element ("Custom JS/HTML") to that section
4. Click **Open Code Editor** and paste the full contents of `dist/ghl-paste.html`
5. Save, preview, then publish

To update later: open the same Code element, select all, and paste the new `dist/ghl-paste.html`.

Tip: duplicate the page in GHL first and test there before replacing the live homepage.

## Hero background photo

Set at the top of `src/styles.css` (`--ql-hero-img`). It's the same photo the original GHL site uses. To change it, upload a new image to GHL Media Library and paste its URL there.

## `original/` folder

A snapshot of the live qualitylivin.com as GHL built it (October 2026), kept for reference:

- `qualitylivin-screenshot.png`: full-page screenshot
- `qualitylivin-clean.html`: page markup with scripts stripped (easier to read)
- `qualitylivin-raw.html`: exactly what GHL serves, including its CSS

These are reference only. GHL can't re-import them, and they're not used by the build.

## Notes

- All CSS is scoped under `.ql`, so it won't affect GHL's own elements on the page.
- "Request a Virtual Estimate" links to your existing GHL form. For the estimate section you can also place your native GHL form element below the Code block, so contacts and workflows keep working.
- The hero search box and the "Map + results" panel are visual only, the same as on the current live site.
- Social icons still point to the generic instagram.com / linkedin.com / etc. Swap in your real profile URLs in `src/page.html`.
