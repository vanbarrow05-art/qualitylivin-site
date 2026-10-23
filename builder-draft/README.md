# GHL builder draft (snapshot 2026-10-23)

What the GHL builder currently holds for the qualitylivin.com homepage. It was pulled from the page's no-login preview link:
https://sites.leadconnectorhq.com/preview/9T0xbhh5dOkUdztv2lB8?notrack=true

This is the saved **draft**. It is not what qualitylivin.com serves right now (that's `original/`). GHL page ID `9T0xbhh5dOkUdztv2lB8`. `/`, `/home` and `/untitled-page` are all this same page.

This folder is for reference only. The build doesn't use it.

## Files

- `page-outline.txt`: every section in order, with the text, buttons, images and where each code element sits
- `code/`: the contents of each GHL Custom JS/HTML element, numbered in page order

| File | Section | Notes |
| --- | --- | --- |
| `code/01-hospitality-hero.html` | hero | headline styling |
| `code/02-hospitality-hero.html` | hero | search card. **Still has the broken form embed** (the stray `});` text). The fix is `snippets/hero-search-card.html` and hasn't been pasted into GHL yet |
| (03, empty) | `section-iaUaahOIvg` | a new section with an **empty** Code element. Whatever was pasted there didn't save |
| `code/04-service-discovery-engine.html` | directory | coverage radar map |
| `code/05-virtual-estimate-flow.html` | estimate | 4-step estimate wizard |
| `code/06-floureshe-editorial.html` | magazine | article ticker |

## Content to fix before this draft is published

- **Invented claims:** provider ratings and review counts (Belgravia 4.98/164, Apex 4.95/92), the £10M indemnity bond, "fewer than 4% of applicants", "256-bit AES", "98% resolution threshold", the $10,000 escrow guarantee, and the "Alistair Vance" byline. These are presented as fact on a live business site.
- **UK details on a US site:** Belgravia, Mayfair, Cotswolds, Gas Safe/REFCOM/CIBSE, the £ bond.
- **Footer email:** `concierge@qualityliving.com` (with a "g") is someone else's live domain. Mail sent there goes to a stranger.
- **Pricing:** the $800 and $1,600 tiers are advertised as available.
