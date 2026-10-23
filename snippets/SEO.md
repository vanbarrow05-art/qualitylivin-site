# SEO setup for qualitylivin.com (GoHighLevel)

The page code (`dist/ghl-paste.html`) sits in a body Code element. It **can't** set the page title, description, canonical or share image. Those come from GHL's page settings, so the steps below are needed even after the new design is pasted in.

Checked 2026-10-23: the live site has no title, description, share image or canonical. Its structured data lists a phone number and an email (`concierge@qualityliving.com`, a different domain) that aren't yours. `/sitemap.xml` and `/robots.txt` both return empty files.

## 1. Page SEO settings (homepage)

GHL: open the page in the builder → **Settings** (gear) → **SEO Meta Data**.

| Field | Paste this |
|---|---|
| Title (≤ 60 chars) | `Quality Living \| Local Cleaning & Property Services` |
| Description (≤ 155 chars) | `Explore residential cleaning, commercial janitorial and rental turnover services. Tell Quality Living about your project and request an estimate.` |
| Social / share image | `https://storage.googleapis.com/funnel-ai-production/image-generation/wVyBbToZpkqhRQ0pkRSu/f02fa9cd-e2e5-48f9-b358-73bb9ef592bf.png` (the hero photo, 1376×768) |
| Canonical URL (if the field exists) | `https://qualitylivin.com/` |
| Keywords | Leave blank. Google ignores the meta keywords tag, so it doesn't help ranking. |

Make sure the page is **not** set to noindex. The local `dist/preview.html` carries `noindex` on purpose because it's a draft. Never copy that tag into GHL.

When the service area is confirmed, add it to the title and description (for example `… in Austin, TX`). Don't add cities that aren't actually served, and don't create mass-produced city pages.

## 2. Structured data (whole site)

GHL: **Sites → your website → Settings → Tracking Code → Header**.

1. Delete the existing `<script type="application/ld+json">` block (the one with `concierge@qualityliving.com` and `+1 (800) 482-9110`).
2. Paste in `snippets/seo-schema.html`. It has Organization, WebSite and WebPage, plus the provider plans whose prices appear on the page. It deliberately has no address, phone, ratings or reviews. Add contact details only once they're real.
3. Check it at https://search.google.com/test/rich-results with `https://qualitylivin.com/`.

## 3. Page URLs and duplicates

`/`, `/home` and `/untitled-page` are **the same GHL page** (page ID `9T0xbhh5dOkUdztv2lB8`). GHL's real slug is `untitled-page`, and any unknown path redirects there. **Do not delete it: that deletes the homepage.** Instead:

- Set the canonical to `https://qualitylivin.com/` (step 1).
- Optionally rename the slug from `untitled-page` to something readable. First check that nothing (ads, emails, buttons) links to `/untitled-page`.

## 4. Site settings

- **Favicon:** upload the Quality Living leaf logo under the website's Settings → Favicon: `https://storage.googleapis.com/funnel-ai-production/image-generation/wVyBbToZpkqhRQ0pkRSu/328fec49-8a6a-4bed-8d05-8d0703a44445.png`
- **Sitemap:** `https://qualitylivin.com/sitemap.xml` is currently empty, so don't submit it yet. Check whether GHL's website settings can generate a sitemap. If it stays empty, use Search Console's URL Inspection → *Request indexing* for the homepage instead.
- **Google Search Console:** add `qualitylivin.com` at https://search.google.com/search-console. Verify it with the HTML meta-tag method, pasting the tag into Tracking Code → Header. Then check the homepage with URL Inspection. Indexing isn't instant, and Search Console shows when it has happened.
- **Google Business Profile:** check eligibility before creating one. Google requires in-person contact with customers at a location or within a service area. Lead-generation or referral-only businesses and online-only businesses aren't eligible. Quality Living coordinates and providers do the work, so confirm the operating model first. Each provider can hold its own profile.

## 5. On-page content

- One `<h1>` (the hero headline). Sections use `<h2>`, and cards and FAQ items sit below them.
- The service descriptions and customer FAQ are plain HTML text, so they're readable by search engines. Don't move them into images or the form iframe.
- Mention the actual cities and areas served once confirmed.
- No made-up provider listings, ratings, bonds or guarantees. Public map listings are labeled "not reviewed". Fake reviews break the FTC's rule on fake reviews and testimonials.
