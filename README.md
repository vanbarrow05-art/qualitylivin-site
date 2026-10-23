# Quality Living — qualitylivin.com

The qualitylivin.com homepage as clean HTML/CSS, kept in git and pasted into GoHighLevel.

## Files

- `src/page.html`: page content (edit this)
- `src/styles.css`: styles (edit this; brand colors + hero image are at the top)
- `src/script.js`: page behavior: mobile menu, fade-in on scroll, hero search and category cards → directory, and the magazine card gallery
- `src/magazine-feature.html`: the magazine / eBook section (3D cover, contents, look-inside pages, partner feature, subscription). The build includes it in the page and also outputs it alone as `dist/magazine-feature-paste.html`
- `assets/`: magazine cover image, the April 2025 magazine PDF, and page previews (`assets/pages/`)
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
- `code-elements/`: the HTML of each Custom JS/HTML element, numbered top to bottom. GHL moves each element's `<style>` and `<script>` into the page head when publishing, so those parts are only in `builder-raw.html`. For the complete code of each element (styles and scripts included), use `code-source/`, saved from the builder by the laptop session.
- `code-source/`: the exact code inside each Code element, with its `<style>` and `<script>` included. Edit this version and paste it back into GHL.
- `page-outline.txt`: every section's text, buttons and images in page order. `NOTES.md` lists what to fix before the draft is published.

## `snippets/` (code for the GHL builder page)

- `hero-search-card.html`: hero search card. "Request an In-Person Estimate" scrolls to the inline form, or opens the GHL form in a popup if the inline form isn't on the page.
- `estimate-form-card.html`: replaces the old 4-step estimate form (which sent nothing) with your GHL form, so submissions become GHL contacts.
- `seo-schema.html` + `SEO.md`: SEO setup: page titles/descriptions, structured data, and the steps in GHL.

## Notes

- All CSS is scoped under `.ql`, so it won't affect GHL's own elements on the page.
- Page order: hero search → three service cards → directory (map + list) → how it works (3 steps) → in-person estimate form → magazine (gallery + issue feature) → standards → customer FAQ → for providers → closing call to action → footer. The top menu is Services · How It Works · Magazine · For Providers; Standards, FAQ and Contact are in the footer.
- Magazine gallery: on screens wider than 760px with motion allowed, script.js adds .ql-anim for the pinned scroll animation (280vh). Phones, reduced motion and no-JavaScript get a swipeable row with the issue link visible.
- `dist/preview.html` carries the page metadata plus `noindex` (draft only). On the live site, set the title, description, canonical and share image in GHL (snippets/SEO.md).
- The estimate section embeds the live GHL form "House Cleaning Lead Generation" (`2CZsk7kdEPJcdbYk33Tf`), so submissions become GHL contacts. Its look (header image, field colors) is set in GHL's form builder, not here.
- Commercial walkthrough intake: the local estimate copy asks for the service location, in-house cleaning setup, legal business name, manager details and preferred visit windows through the existing comments field. The owner confirmed that this form routes to the existing Quality Living janitorial pipeline in GHL. Callers submit the form; the janitorial team follows up to confirm the visit. No separate caller booking calendar or new pipeline is needed. See `partners/07-cleaning-walkthrough-intake.md` for the form handoff and optional dedicated fields.
- The directory (`src/directory.html`) has two layers:
  - **Partners** from `data/providers.csv`: only `joined` rows show, with ratings (source and date), call, booking and estimate buttons. Add a business only after it agrees in writing.
  - **Public listings** from `data/map/`: 46,424 real cleaning businesses (Overture Maps + OpenStreetMap). They show after a search by ZIP, "City, ST", state or place name. They're marked "Public listing · not reviewed" and show only name, type, city, website and "Own this business? Claim it", with no estimate button and no rating. Pins sit at ZIP centres, and phone numbers and street addresses are stripped. Licences are in `data/map/LICENSE.md`. Add `data-public="off"` to the `.qld` element to hide the layer.
- Provider plans use the Oct 21 package names and prices. Delivery limits and the $800 guarantee aren't shown until their terms are final. The provider buttons point to Contact until a provider application form exists. Search `data-ql-provider-apply` in `src/page.html` to repoint them.
- No email, phone or social links are shown until real ones exist. The footer has a commented-out social block ready to fill in.
- On Windows, the build works with plain `python scripts/build.py` (it reads and writes UTF-8 explicitly).

## Business docs

- `partners/`: partner program (offer, call scripts, prospecting, CRM pipeline, training, agreement outline, launch promo, researched prospect list). Start with `partners/README.md`.
- `data/providers.csv`: the providers shown on the website map (only `joined` rows show as partners).
- `magazine/PRINT-LAUNCH-PLAN.md`: plan for the first print issue by Jan 1, 2027.
- `prompts/CLAUDE-WEBSITE-PROMPTS.md`: copy-paste prompts for updating the site with Claude.
