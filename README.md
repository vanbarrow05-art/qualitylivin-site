# Quality Living — qualitylivin.com

The qualitylivin.com homepage as clean HTML/CSS, kept in git and pasted into GoHighLevel.

## Files

- `src/page.html`: page content (edit this)
- `src/styles.css`: styles (edit this; brand colors + hero image are at the top)
- `dist/ghl-paste.html`: **the file you paste into GHL** (generated)
- `dist/preview.html`: open in a browser to preview (generated)

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

The live site's hero photo is set inside GHL, so it isn't in this repo yet. Copy its URL from GHL Media Library and set it in `src/styles.css`:

```css
--ql-hero-img: url("https://...your-image.jpg");
```

## Notes

- All CSS is scoped under `.ql`, so it won't affect GHL's own elements on the page.
- "Request a Virtual Estimate" links to your existing GHL form. For the estimate section you can also place your native GHL form element below the Code block, so contacts and workflows keep working.
- The hero search box and the "Map + results" panel are visual only, the same as on the current live site.
- Social icons still point to the generic instagram.com / linkedin.com / etc. Swap in your real profile URLs in `src/page.html`.
