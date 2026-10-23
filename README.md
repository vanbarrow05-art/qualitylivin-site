# Quality Living — qualitylivin.com

The qualitylivin.com homepage as clean HTML/CSS, kept in git and pasted into GoHighLevel.

## Files

- `src/page.html`: page content (edit this)
- `src/styles.css`: styles (edit this; brand colors + hero image are at the top)
- `src/script.js`: the scroll animation for the magazine card gallery
- `assets/`: magazine cover image + the April 2025 magazine PDF
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

## Magazine card gallery (scroll animation)

The magazine section (`#section-floureshe-editorial`) is a scroll-driven card gallery. As visitors scroll, the cards scatter, line up, form a circle, then spread into an arc with the magazine cover in the center. In the arc, hovering (or tapping on a phone) flips a card. It uses normal page scrolling, so it never traps the mouse wheel.

- **Photos:** free Unsplash images (free for commercial use, no attribution required). Swap any `images.unsplash.com` URL in `src/page.html` for your own job photos from GHL Media Library.
- **Card backs:** each card's back text is in `src/page.html` (the `ql-card-back` blocks).
- **Cover + PDF:** both load from this repo via `cdn.jsdelivr.net/gh/vanbarrow05-art/qualitylivin-site@main/assets/...`. That only works while the repo is public, and changes can take up to a day to show. For production, upload both to GHL Media Library and replace those URLs.
- **Pinned scrolling:** the section stays pinned on screen while it animates. If a GHL wrapper blocks that, the script automatically switches to an un-pinned version.
- **Reduced motion:** visitors with "reduce motion" turned on see the finished arc with no animation.

## `original/` folder

A snapshot of the live qualitylivin.com as GHL built it (October 2026), kept for reference:

- `qualitylivin-screenshot.png`: full-page screenshot
- `qualitylivin-clean.html`: page markup with scripts stripped (easier to read)
- `qualitylivin-raw.html`: exactly what GHL serves, including its CSS

These are reference only. GHL can't re-import them, and they're not used by the build.

`original/builder-page/` is the GHL builder version ("Discover Verified Professionals", 4-step estimate form, FLOURESHÉ stories), saved from its preview link:

- `builder-screenshot.png`: full-page screenshot
- `builder-clean.html` / `builder-raw.html`: readable markup / exactly what GHL serves (includes all CSS and JS)
- `code-elements/`: the HTML of each Custom JS/HTML element, numbered top to bottom. GHL moves each element's `<style>` and `<script>` into the page head when publishing, so those parts are only in `builder-raw.html`.
- `code-source/`: the exact code inside each Code element, with its `<style>` and `<script>` included. Edit this version and paste it back into GHL.
- `page-outline.txt`: every section's text, buttons and images in page order. `NOTES.md` lists what to fix before the draft is published.

## `snippets/` (code for the GHL builder page)

- `hero-search-card.html`: hero search card. "Request a Virtual Estimate" scrolls to the inline form, or opens the GHL form in a popup if the inline form isn't on the page.
- `estimate-form-card.html`: replaces the old 4-step estimate form (which sent nothing) with your GHL form, so submissions become GHL contacts.
- `seo-schema.html` + `SEO.md`: SEO setup: page titles/descriptions, structured data, and the steps in GHL.

## Notes

- All CSS is scoped under `.ql`, so it won't affect GHL's own elements on the page.
- "Request a Virtual Estimate" links to your existing GHL form. For the estimate section you can also place your native GHL form element below the Code block, so contacts and workflows keep working.
- The hero search box and the "Map + results" panel are visual only, the same as on the current live site.
- Social icons still point to the generic instagram.com / linkedin.com / etc. Swap in your real profile URLs in `src/page.html`.
