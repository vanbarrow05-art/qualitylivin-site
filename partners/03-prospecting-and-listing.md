# 3. Finding 5-star providers and getting them on the map

## The prospect list

`partners/prospects-research.csv` is the starting list (researched Oct 23, 2026). It has 41 rows:

| Tier | Rows | What it is | How to use it |
|---|---|---|---|
| `national` | 17 | Corporate & franchise cleaning brands (Two Maids, Molly Maid, Merry Maids, The Maids, MaidPro, Jan-Pro, Coverall, Anago, Jani-King, City Wide, ServiceMaster Clean, ABM…) | Script B: ask corporate for the partnerships / local-marketing route, then call **local franchise owners** in your markets with Script A. |
| `marketplace` | 6 | Angi/HomeAdvisor, Thumbtack, Yelp, Google Local Services Ads, Networx, Porch | **Not partners.** They're what providers compare us to. Their pricing models are in the notes column, for the objection "we tried Angi". |
| `featured-partner` | 1 | TLG Janitorial Services, Preston ID (5.0★, 7 Google reviews) | Already in the magazine. Call them first: get written consent, then set them to `joined` on the map. |
| `regional-cleaning` | 11 | Top-rated independents in the Logan UT–ID (Cache Valley) metro around TLG | 6 meet the full bar (4.8+, 40+ reviews); 5 have 30–37 reviews and are flagged. Call the top 6 first. |
| `regional-construction` | 6 | Top-rated remodelers/contractors in the same metro | For the construction campaign later. Note Madsen Remodeling is in Brigham City and OLO Builders is multi-state. |

**Before calling, re-check:** several national main phone numbers couldn't be verified (Two Maids, MaidPro, Maid Right, Vanguard, Stratus, Office Pride), and two regional companies list different numbers on their website and Google (see the notes column). Ratings change, so re-check on the day you call.

## Building more regional lists (repeat for each new city)

1. **Google Maps:** search `house cleaning [city]`, `commercial cleaning [city]`, `janitorial [city]`, `move out cleaning [city]`, `Airbnb cleaning [city]`. Open each result with **4.7★+ and 40+ reviews**.
2. **Cross-check** the same company on **Yelp**, **BBB** and **Trustpilot** (if listed). Skip it if any shows a pattern of unresolved complaints.
3. **Website check:** do they have a site, real photos, insurance mentioned, online booking?
4. **Record it** in the CRM (or a copy of `prospects-research.csv`): company, segment, city, phone (from their own website first), website, rating, review count, rating source + link, date checked, notes.
5. **Aim for 20–30 qualified prospects per city** before you start calling, so one caller has a full week.

Speed tips: Google Maps "Sort by: Highly rated" helps; franchises show the brand name in the listing (a franchise location is fine to call as a local owner).

## Putting a provider on the website map

The map reads `data/providers.csv` in the GitHub repo. **Only add a provider as `joined` after they've replied "agreed"** to the partner email or signed the agreement.

1. Open `data/providers.csv` on GitHub → pencil icon (Edit).
2. Add a row (or change `invited` to `joined`). Columns:
   - `status`: `joined` (shown) · `invited` / `pending` / `declined` (hidden) · `example` (labeled sample, delete when real partners exist)
   - `categories`: one or more of `residential-cleaning; commercial-janitorial; str-turnovers; move-in-out; deep-cleaning` (later: `construction; plumbing; electrical; hvac; landscaping; handyman; interior-design; massage`)
   - `lat`, `lng`: in Google Maps, right-click the business → click the numbers at the top to copy them
   - `service_areas`: cities, ZIPs, or 3-digit ZIP prefixes separated by `;` (e.g. `Logan;North Logan;843`)
   - `rating`, `review_count`, `rating_source`, `rating_url`, `rating_checked`: only what you saw yourself, with the link and the month
   - `booking_url`: their online booking or calendar link, if any (shows a "Book online" button)
   - `featured`: `yes` if they're in the magazine
   - `founding`: `yes` for Founding Partners (shows a badge; see `06-launch-promo.md`)
3. Commit. The live map picks it up within a few minutes.
4. When a city has 2+ real partners, delete the `example` rows near it.

**Ratings:** show the number, the source, a link, and the date checked. Don't copy review text from Google or Yelp onto the site (their terms don't allow it); link to it instead. Re-check ratings monthly.

## Booking / calendar integration (part of onboarding)

| Provider uses… | What we do |
|---|---|
| Nothing | Set up a GHL calendar for them (included from AI Autopilot & Growth); put the booking link on the map. |
| Calendly / Google Calendar / Square | Put their booking link in `booking_url`; send leads with that link. |
| Jobber, Housecall Pro, ServiceTitan | Use their online booking link; for revenue tracking, ask for a monthly job export (or a Zapier connection to GHL). |
| GHL already | Share leads into their sub-account via a webhook or GHL snapshot. |
