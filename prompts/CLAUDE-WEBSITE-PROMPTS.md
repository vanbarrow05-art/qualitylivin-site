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

CLEANING CUSTOMER FORM AND IN-PERSON ESTIMATE UPDATE — OCTOBER 23

The owner clarified the existing workflow: callers submit the House Cleaning Lead Generation form (2CZsk7kdEPJcdbYk33Tf); it routes to the existing Quality Living janitorial pipeline in GoHighLevel. The janitorial team confirms the representative and appointment. Preserve that form and routing. Do not create a second pipeline or require a separate caller booking calendar.

Before calling, check the prospect's official website and confirm uncertain information. Ask in this order: exact service location; in-house cleaners and any outside company; legal business name and DBA; manager/approver names and work contact details; who can meet on-site; cleaning scope; two dates/time slots and timezone when that manager is available for an IN-PERSON ESTIMATE. These are customer availability windows, not promises that our representative is booked.

Use partners/07-cleaning-walkthrough-intake.md and Script I in partners/02-call-scripts.md. Until native fields exist, put the complete structured summary in the existing Additional Details or Comments field. Use the customer's actual contact details, submit once and check acknowledgement. Do not describe form submission as appointment confirmation or make up test leads to trigger the live pipeline.

If adding dedicated native fields in the correct GHL account, inspect and preserve current field IDs, contact mappings, assignments, workflow triggers and the existing janitorial pipeline. Show business fields conditionally and keep preferred cleaning date separate from estimate visit slots. Keep different site requests separate. No new calendar configuration is required for this change.

Commission rebuttal: the customer may be told Quality Living can be paid by providers through agreed marketing or referral arrangements; confirm the actual provider terms and any charge to the customer before agreement. For provider recruitment, the first three eligible introductions are fee-free; later referral-only rates are fixed by written agreement, normally 10–20% of eligible collected revenue, with scope/duration defined. Declining a package is not consent to commission. Do not promise a free visit or that commission cannot affect price without supporting terms.

Verify the form still submits to the existing janitorial pipeline and retains the full notes/time slots. Check residential/business branching, unknown legal name, unavailable manager, timezone and duplicate handling when native fields change. Rebuild the local site; report separately what is local, changed in GHL and published. Remove the temporary comments instruction only when dedicated fields are live.
