# SEO setup for qualitylivin.com (GoHighLevel)

The live site currently has **no page title, no meta description, no social-share image and no canonical URL**, and its structured data lists a phone number and email that aren't real. Fix it in this order.

## 1. Page SEO settings (each page)

GHL: open the page in the builder → **Settings** (gear) → **SEO Meta Data**.

| Field | Paste this |
|---|---|
| Title (≤ 60 chars) | `Quality Living \| Vetted Local Cleaning & Property Services` |
| Description (≤ 155 chars) | `Find reviewed local cleaning and property care providers. Share your project and request a virtual estimate for your home, rental, or business.` |
| Keywords | `house cleaning, janitorial services, Airbnb turnover cleaning, move out cleaning, deep cleaning, property care, cleaning estimate` |
| Social image | `https://storage.googleapis.com/funnel-ai-production/image-generation/wVyBbToZpkqhRQ0pkRSu/f02fa9cd-e2e5-48f9-b358-73bb9ef592bf.png` (the hero photo, 1376×768) |
| Author | `Quality Living` |

Once you know your service area, add it to the title and description (e.g. `... in Austin, TX`). City names are what local search ranks on.

## 2. Structured data (whole site)

GHL: **Sites → your website → Settings → Tracking Code → Header**.

1. Delete the existing `<script type="application/ld+json">` block (the one with `concierge@qualityliving.com` / `+1 (800) 482-9110`).
2. Paste in `snippets/seo-schema.html`.
3. Check it at https://search.google.com/test/rich-results with `https://qualitylivin.com`.

## 3. Page URLs and duplicates

- Rename `/untitled-page` to a real slug (e.g. `/marketplace`), or delete it. Right now it shows the same content as the homepage, and duplicate pages compete with each other in search.
- Make the page you want found the **home page** (path `/`).

## 4. Site settings

- **Favicon:** the site uses GHL's default icon. Upload the Quality Living leaf logo under the website's Settings → Favicon.
- **Google Search Console:** add `qualitylivin.com` at https://search.google.com/search-console, verify it (GHL accepts the verification meta tag in Tracking Code → Header), then submit `https://qualitylivin.com/sitemap.xml` if your GHL site generates one.
- **Google Business Profile:** if you serve a local area, create one. It drives "near me" searches more than anything on the page.

## 5. On-page content

- Keep one `<h1>` per page (the hero headline already is one).
- Mention the actual cities/areas you serve somewhere in the page text.
- Replace the made-up provider listings, ratings and guarantees. Fake reviews can get a site penalised and break FTC rules on fake reviews.
