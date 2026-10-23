# Prompts for updating the website with Claude

Copy a prompt, fill in the [brackets], and paste it into Claude Code (web, desktop or laptop). Every prompt starts with the same context block so Claude knows how this repo works.

## Context block (always paste this first)

```
Repo: github.com/vanbarrow05-art/qualitylivin-site (GoHighLevel site built from code).
Rules:
- Run `git pull` before editing. Another Claude session may have pushed changes.
- Edit files in src/ (page.html, styles.css, script.js, directory.html, magazine-feature.html) and data/providers.csv. Never hand-edit dist/.
- After editing, run `python3 scripts/build.py`, check dist/preview.html in a browser at desktop and phone width, then commit and push to main.
- All CSS stays scoped under .ql / .qld / .qlm so it can't break GoHighLevel's own styles.
- Never invent providers, ratings, reviews, guarantees, phone numbers or emails. Only list providers who agreed to be listed (status "joined").
- Tell me what to paste into GHL afterwards (usually dist/ghl-paste.html into the homepage's Custom JS/HTML element).
```

## Provider map

**Add a partner who agreed**
```
Add this provider to data/providers.csv with status "joined": [company name], categories [residential-cleaning / commercial-janitorial / str-turnovers / move-in-out / deep-cleaning], city [city], state [ST], service areas [cities; ZIPs], phone [number], website [url], booking link [url or none], Google rating [x.x] from [n] reviews (link: [url], checked [month year]), featured in magazine [yes/no], founding partner [yes/no]. Look up the latitude/longitude for their address [address]. Remove any "example" rows within 50 miles once there are 2+ real partners in that area.
```

**Mark TLG (or anyone) as joined**
```
In data/providers.csv, change [company] from "invited" to "joined" and confirm the city, coordinates and service areas are right.
```

**Remove a partner**
```
Remove [company] from the map: set their status to "declined" in data/providers.csv (don't delete the row, so we keep the history).
```

**Open a new trade (e.g. construction)**
```
Start showing the [construction] category: in src/directory.html make it selectable in the search dropdown (it's currently "coming"), add a matching photo card to the "Find a Service" categories in src/page.html, and update the "More trades on the way" note.
```

## Prices, packages and promos

**Change a package**
```
Change the [AI Autopilot & Growth] plan to [$___/month] and these features: [list]. Update src/page.html, snippets/seo-schema.html, and partners/01-offer-and-packages.md so they all match.
```

**Change the referral %**
```
Change the Referral Partner fee to [10–20% depending on trade]. Update the site copy and the example ("On $1,000 collected, the fee is…"), partners/01-offer-and-packages.md and partners/05-partner-agreement-outline.md.
```

**End or change the Founding Partner promo**
```
[Remove / Update] the Founding Partner launch banner (class ql-founding in src/page.html): [new deadline / new perks / remove entirely]. Update partners/06-launch-promo.md to match.
```

**Add a customer promo banner**
```
Add a slim promo bar under the hero: "[text]" linking to [#section or url], dismissible, styled in the site's gold/green. Remove it automatically after [date].
```

## Magazine

**New issue**
```
New magazine issue: the PDF is [path/to/file.pdf], issue name [Winter 2027]. Add it to assets/, render the cover and 7 page previews like the current ones, and update src/magazine-feature.html (cover, contents list with page links, look-inside pages, partner feature) and the gallery's cover card in src/page.html. Keep the old issue's files.
```

**Turn on subscriptions**
```
Subscriptions are live at [payment link]. In src/magazine-feature.html replace the "Subscriptions opening soon" pill with a gold "Subscribe now" button to that link, and update the price/perks text to: [price, number of print issues, perks].
```

**Gate the eBook behind email**
```
Make the eBook a lead magnet: "Read the eBook" should open a popup with GHL form [form ID or embed code] and only reveal the PDF link after the form is submitted. Keep "Download PDF" behind the same form.
```

## SEO

**City landing content**
```
We now serve [city, state]. Add it to the SEO title/description in snippets/SEO.md, the structured data in snippets/seo-schema.html (areaServed), and a sentence in the directory intro in src/page.html. Don't claim partners there unless data/providers.csv has a joined provider in that city.
```

## Fixes

**Something looks broken in GHL**
```
On the live site [url], [describe what's wrong, attach a screenshot]. Compare with dist/preview.html, find the cause (GHL wrapper styles, sticky/overflow, script order) and fix it in src/. Tell me exactly what to re-paste in GHL.
```
