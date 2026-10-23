# 4. CRM pipeline, daily routine, training and compliance

## GHL pipeline: "Provider Partnerships"

Create it in GHL → Opportunities → Pipelines. One opportunity per provider company.

| Stage | Means | Automation to set up in GHL |
|---|---|---|
| 1. Prospect | Researched, meets the 5-star bar, not contacted | none |
| 2. Contacted | Called / voicemail / email sent | Task: follow up in 3 business days |
| 3. Conversation | Spoke with the decision-maker | Task: send partner email within 1 hour |
| 4. Agreed (free leads) | Replied "agreed" / signed | Tag `partner-joined`; internal alert "add to map"; welcome email |
| 5. Leads sent (1–3) | Free leads delivered | After each lead: SMS check-in 24h later (Script F) |
| 6. Upgrade offered | Upgrade call done | Task: follow up in 7 days |
| 7a. Referral Partner | Ongoing leads, 10% fee | Monthly "report your jobs" email on the 1st |
| 7b. Paid plan | $400 / $800 / $1,600 | Hand off to onboarding (website, AI receptionist, posts) |
| Lost / Not now | Said no or unqualified | Re-engage in 90 days |

**Custom fields:** segment, cities/ZIPs served, rating + source + date, insured (Y/N + COI file), booking system, monthly capacity, free leads used (0–3), plan, referral %, consent-to-list date.

## Lead delivery (how a lead reaches a provider)

1. A customer submits the estimate form on the website (GHL form "House Cleaning Lead Generation").
2. GHL workflow: match by service + ZIP → pick the provider (rotate fairly between matched partners; send each lead to **one** provider only).
3. Send the provider an SMS + email with the lead details; mark "free lead #n" until 3.
4. Text the customer: "Thanks! [Company], a top-rated Quality Living partner, will contact you within [1 business hour]."
5. 24h later, check in with the provider (Script F); record booked / quoted / no answer / not a fit.
6. Invalid leads (fake, duplicate, out of area) don't count toward the free 3. Replace them.

## Daily routine for a caller

| Time | Activity | Target |
|---|---|---|
| 30 min | Research: add qualified prospects to the pipeline | 10 new |
| 2 × 90 min | Call blocks (Script A/B), log every call | 40–60 dials · 8–12 conversations |
| 30 min | Send partner emails + follow-ups | Same-day for every conversation |
| 15 min | Lead check-ins with active partners | Every lead sent yesterday |

**Weekly KPIs:** dials · conversations · agreed (goal: 25–35% of conversations) · free leads delivered · providers who got all 3 · upgrades (goal: 1 in 5 within 60 days) · referral revenue collected · cost per lead.

## 5-day training plan for a new caller

| Day | Learn | Practice |
|---|---|---|
| 1 | The offer and packages (`01-offer-and-packages.md`), the 5-star bar, what we never say | Explain the ladder out loud in 60 seconds |
| 2 | Script A + gatekeeper + voicemail (`02-call-scripts.md`) | 10 role-plays with a manager playing the owner |
| 3 | Objection handling table; CRM stages and fields | Role-play the 8 objections; log 5 practice calls in GHL |
| 4 | Prospecting a new city (`03-prospecting-and-listing.md`) | Build a list of 20 qualified prospects |
| 5 | Live calls with a manager listening | 30 live dials; review recordings together |

**Certification before solo calling:** explains the offer in 60s, handles 5 objections, logs calls correctly, and never claims a provider is "in the network" before they agree.

## Compliance: read before the first call

*This is practical guidance, not legal advice. Have an attorney review the partner agreement and your texting setup.*

- **Network listings need consent.** Only list a business as a partner after it agrees in writing. Showing a business as "in our network" without its OK can be false endorsement / false advertising.
- **Reviews:** only show ratings you saw, with source, link and date. Never write, buy, or filter reviews. The FTC's rule on fake reviews (2024) carries civil penalties.
- **Calls:** calling businesses is generally allowed, but check the National Do Not Call Registry and state lists for numbers that are personal cell phones (common for small owner-operators), honor "don't call me" immediately, and call within 8am–9pm their local time.
- **Texts:** only text providers who agreed to texts; include "Reply STOP to opt out". No auto-dialed texts or robocalls to cell phones without prior consent (TCPA). Register your GHL texting number for A2P 10DLC.
- **Email:** real sender name, real postal address, and an unsubscribe line in commercial emails (CAN-SPAM).
- **Customer data:** only share a customer's details with the one provider matched to them, and say so on the estimate form.
- **Referral fees:** fine for cleaning. For licensed trades (construction, plumbing, electrical), check your state's contractor rules before charging a % of job revenue.
