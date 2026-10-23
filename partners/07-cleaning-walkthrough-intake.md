# Cleaning intake — in-person estimate requests

Updated October 23, 2026. The owner confirmed the operating route: **submit the existing cleaning form → existing Quality Living janitorial pipeline in GoHighLevel → janitorial team confirms the in-person estimate**. The caller collects the manager's available time slots. A new pipeline or separate caller booking calendar is not required.

## Existing form and current implementation

Use **House Cleaning Lead Generation**, ID `2CZsk7kdEPJcdbYk33Tf`:
https://api.leadconnectorhq.com/widget/form/2CZsk7kdEPJcdbYk33Tf

The public form was checked October 23. It already has contact/address, cleaning type, preferred cleaning date, comments, scope and upload fields. The local website tells callers/customers to put the new details in **Additional Details or Comments**, so the existing submission route can be used now. Dedicated native fields remain an optional form improvement; they are not a blocker to submitting requests. The owner's pipeline routing was not independently tested from inside GHL, and no real or test lead was submitted by this work.

## Before calling

Check the prospect's official website for the correct location and any public business/manager information. Confirm uncertain details on the call. Open the cleaning form and collect the customer's availability. Do not treat website opening hours as a manager's confirmed availability.

## Question and field order

| Order | Question / field | Notes |
|---|---|---|
| 1 | Exact service location: address, suite, city, state, ZIP | Use the property to be visited, not an unrelated headquarters. Keep ZIPs as text. |
| 1 | Home or business/property-management request? | Business fields apply to business requests; households do not need a legal company name. |
| 2 | Any in-house cleaners? Yes / No / Unsure | Ask before the business-name and manager questions. |
| 2 | Any outside cleaning company as well? | Both in-house and outside help can be true. |
| 3 | Legal business name; trading/location name if different | Confirm rather than assuming the website brand is the legal name. Mark unknown details for follow-up. |
| 4 | Site manager's full name, role, work phone/email | Keep the person submitting the request separate if different. |
| 4 | Additional manager/approver, if relevant | Optional; do not invent or require a second person. |
| 4 | Who can meet the representative at the property? | Manager or authorized delegate. Record whether their availability was confirmed by them or reported by someone else. |
| 5 | Cleaning need, approximate size and frequency | Reuse current service and scope fields. |
| 6 | Two dates and available time slots for an in-person estimate | Capture date, start/end time, timezone and attending manager. These are customer preferences for the team to confirm. |
| 6 | Preferred cleaning start date | Keep separate from the estimate visit date. |
| 7 | Best contact for appointment confirmation | Confirm the work phone/email and requested contact method. |

Use the actual customer's contact information in the form's contact fields. If a required detail is missing, ask for it; do not insert a fake phone/email or the caller's own details.

## Copy into Additional Details or Comments

```text
Request: IN-PERSON CLEANING ESTIMATE
Service location:
In-house cleaners: Yes / No / Unsure
Outside cleaning company: Yes / No / Unsure
Legal business name:
Trading/location name, if different:
Site manager — full name / role / work phone / email:
Additional manager or approver, if relevant:
Person attending the estimate:
Cleaning need / approximate size / frequency:
Available slot 1 — date / start / end / timezone:
Available slot 2 — date / start / end / timezone:
Whose availability was confirmed:
Preferred cleaning start date, if known:
Best confirmation contact/method:
Visit notes:
Website checked:
Caller / call date:
```

## Submit and hand off

1. Read back the address, legal name, manager/contact and time slots. Correct errors before submission.
2. Submit the existing form once. Check its acknowledgement before telling the customer the request was submitted. Record the submission time; avoid creating duplicates if the result is uncertain.
3. The existing Quality Living janitorial pipeline receives the request, per the owner's confirmed workflow. Preserve its form ID, routing, assignments and stage configuration. Do not create a second pipeline or a new booking dependency.
4. The janitorial team reviews scope, confirms the eligible representative and verifies the chosen slot with the customer's manager. The caller does not promise a representative or an appointment time.
5. A confirmed visit should identify the in-person-estimate purpose, address, date/time/timezone, representative and attendee. Explain any estimate-visit charge before the customer agrees; do not label the visit free without approved terms.
6. Keep each location/request separate. A reschedule or follow-up belongs with its existing request where possible. Submission is an intake event, not confirmation that a visit is booked.

Internal record suggestions: source website/check date, caller, service location, customer availability, form-submission acknowledgement/time, existing GHL request/opportunity reference if available, follow-up owner and next action. Use existing pipeline statuses; no stage renaming is required by this handoff.

## Optional dedicated GHL fields

Inspect the active form and its current field IDs/workflows first. Add the missing business, manager and time-slot fields in the order above, using conditional display for business requests. Preserve the existing janitorial pipeline route and contact mapping. Copy site/visit details into the appropriate request record so one contact's second location does not overwrite an earlier job.

Verify saved field values, correct existing pipeline routing, business versus household requests, unknown details, multiple locations, timezone and duplicate handling before publishing changes. Remove the temporary comments instruction only after dedicated fields are live. The form itself remains the submission path; no calendar link is needed for the caller.

## Commission objection

Customer: "Quality Living may be paid by the cleaning provider through a marketing agreement or an agreed referral fee. The provider supplies your cleaning quote. Our team will explain any charge to you for the estimate or the work before you agree."

Provider: "The first three eligible introductory leads carry no lead or referral fee. After that, a referral-only arrangement uses a fixed rate agreed in writing, normally 10–20% of eligible collected revenue, with the covered services and duration defined first. There is no automatic charge just because you decline a package."

Never guess an individual provider's rate, claim every provider pays commission, promise that the estimate is free, or promise commission cannot affect a quote. Use the actual written terms for the relevant arrangement.

Caller script: Script I in `02-call-scripts.md`.
