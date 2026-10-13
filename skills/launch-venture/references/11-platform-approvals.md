# Platform approvals and listings

Some outside gatekeepers run on their own clock: Meta's Business Verification and App Review, the Claude and ChatGPT app directories, and software review sites. This file says which clocks to start on day 1, because they cost a few founder minutes and then run by themselves, and which to leave until paying customers exist, because they cost days of agent work and hours of founder attention. It ends with the long-lead table for the whole launch.

**Done when:** every verification the venture needs was started in the first hour its prerequisite existed and is tracked with an owner and a re-check date; App Review, directory submissions and review sites are either deferred on purpose (with a dated item) or submitted with the narrowest scope that makes money; and every status is written at its real evidence level ("submitted" is never reported as "approved").

> **Facts checked on 13 Oct 2026** against Meta for Developers (App Review, the submission guide and its screen-recording page, Business Verification, Access Verification, Data Use Checkup), the Claude connector submission docs, the OpenAI Apps SDK submission page and its organisation-verification help article, and G2's free-profile page. Console paths and review times change often. Re-read the vendor page before you rely on any number here.

---

## The rule: start cheap clocks now, defer expensive reviews

| Kind | Examples | Cost to you | When |
|---|---|---|---|
| **Verification clocks** | Meta Business Verification, Tech Provider access verification, OpenAI organisation verification (only if you plan a ChatGPT listing), Google advertiser verification and a D-U-N-S number (only if you plan Google ads) | 10-30 founder minutes with documents and ID, then a wait you cannot shorten | In the first hour the prerequisite exists, usually the day your company number arrives |
| **Build-heavy reviews** | Meta App Review, Claude and ChatGPT directory submissions, review sites, TikTok, LinkedIn and Slack app reviews | Days of agent work, a reviewer account, films, several founder sittings | After your first 3 paying customers, **unless revenue depends on the approval sooner** |

The test for "revenue depends on it": a buyer who is ready to pay cannot use the product without this approval, and no workaround exists. "It would be nice to be in the Claude directory" does not pass. "Paying customers must connect their own Meta ad accounts, and Meta refuses anyone without a role on our app" does.

Workarounds that often remove the need for a review before you have payers:
- **Your own ad account** works through Meta's Marketing API with standard access and a system-user token. No App Review is needed to report on or manage ads your own business owns. (done on Givi)
- **Posting to your own Instagram, Page or TikTok** works through publishing tools that already hold approved apps, such as Composio or Welder. Givi's Instagram posting worked through Composio before its own App Review started. (done on Givi)
- **Customers' assets are the hard case.** Meta's limited access covers only ad accounts owned by your business or by people with a role on your app. A customer sharing their ad account with your portfolio as a partner does not get around this, and neither does Meta's hosted Ads MCP. (recommended, not tested by us: researched on Givi before building)

> **What happened on Givi.** The verification clocks went well: Meta Business Verification passed about 19 hours after submission. The build-heavy reviews went badly. Meta App Review took 16 calendar days from the first click to "Review in progress", about 20-25 agent-hours, about 1,900 browser actions and about 70 founder messages, for about 25 permission items that no paying customer was waiting for, in the same week the sign-up page was losing almost every visitor. The decision was still pending when this was written. The Claude directory submission took about 3 hours 15 minutes from start to submit, for a form that takes 3 minutes to fill. The ChatGPT listing never started, because nobody started OpenAI's organisation verification. Review sites got a listing kit on day 5 and nothing else. Givi had no paying customers by 12 Oct 2026, so none of this produced revenue.

---

## Prepare the inputs every gatekeeper asks for

Every form asks for the same facts and pages. Prepare them once: about 2 hours of agent time spread over the first days, about 15 minutes of founder time.

1. **A company-facts file** (for example `legal/identity.md`): legal name exactly as registered, company number, registered office, trading name, the founder's legal name exactly as on their ID, website, support email, business phone, VAT status. The agent fills it from the public register without asking; for a UK company, fetch `find-and-update.company-information.service.gov.uk/company/<number>` and its `/officers` page, or use the free Companies House API. Meta checks that business details exactly match the legal entity. (learned the hard way: an OpenAI form waited 3 hours for the founder's legal surname, which was on the public officers page)
2. **A shared mailbox on your domain** such as `hello@yourdomain.com`, delivering to an inbox an agent can read. It becomes the Meta app contact, the directory support contact and the review-site contact. (done on Givi)
3. **Policy pages returning HTTP 200** before you create the Meta app: privacy, terms, refunds, support, data-deletion instructions, `/.well-known/security.txt`. Privacy needs retention timelines, a "Retention and deletion" section for the data-deletion URL and, if you have an MCP connector, what an assistant connection can see and how to disconnect it. Terms must not call the product a "pilot", "beta" or "demo"; OpenAI does not accept demo apps. (learned the hard way: Meta would not save the privacy URL while the page returned an error)
4. **One icon set** once the logo is final, with no platform trademarks: 1024 px square for Meta, a 512 px full-bleed square for Claude (it rounds corners itself), 120 px under 1 MB for Google. Use `sips -z 1024 1024 master.png --out meta.png`. Update the site favicon too; the Claude directory uses it by default. (done on Givi)
5. **One browser profile per identity**: owner, tester, reviewer. Logging the owner out to test as someone else put a password prompt in front of the final Submit click. (learned the hard way)

---

## 1. Meta Business Verification

**What it is.** Meta's check that your business is a real legal entity. Meta requires it for any app that requests advanced access to permissions and for any app that lets other businesses access their own data. You also need it to run your ad account at full limits and before App Review. (Meta docs, checked 13 Oct 2026)

**Prerequisites.**
- **A company document** showing the legal name: certificate of incorporation, business registration, tax registration or a business bank statement. Meta accepts PDF, PNG or JPG up to 10 MB, legible and not expired. A utility bill proves only address and phone.
- **A website with matching details:** the same legal name and address as the documents, for example in the footer and on the policy pages. Givi's policy pages rendered the seller name, company number and registered office from the company-facts file, which made the match easy.
- **A domain email:** an address on the website's domain, or the ability to verify the domain. Meta confirms the connection by email, phone, SMS, WhatsApp or domain verification.
- **A business phone number.** Never show it on public profiles.
- **The founder's ID,** if asked: at least 1500 x 1000 pixels, JPG or PNG, all four corners visible, unedited.

**When.** In sitting S2, the day the company number arrives (see `01-framework.md`). About 30 founder minutes, then a wait. Meta says reviews can take up to 14 working days. (done on Givi: verified about 19 hours after submission)

**Steps (about 45 minutes with the founder present).**

1. **Check the founder's standing first.** If the founder owes money on any ad account they manage, in any business, Meta treats the person as a payment risk everywhere, and new Pages and cards fail with a vague "something went wrong". A separate portfolio does not isolate this. Pay old balances before the sitting. (learned the hard way: an unpaid balance under $50 on an unrelated ad account blocked a new Page and card for about 2.5 days)
2. **Business portfolio.** `business.facebook.com` > Create business. If the button is greyed out, the person has hit Meta's portfolio limit: rename an unused old portfolio (reversible) or have a co-founder create it and add you as admin. Never delete one to make room. Fill Settings > Business info with the exact register values.
3. **Create the Facebook Page and connect Instagram while the founder and their phone are there** (S1b, right after the name pick; the portfolio, Page and Instagram need no company). The founder clicks Create from Business Manager on their phone: Meta may send an SMS check, and Claude Code's safety classifier blocks agents from creating Pages and ad accounts on a personal profile. Do not leave without the Page. (learned the hard way: Givi chose "Not now" and the Page sat about 12 more days, blocking ads and Instagram linking)
4. **Create the app.** `developers.facebook.com/apps/` > Create app > Business > the use case you need first (for an ads product, "Create & manage ads with Marketing API") > link the portfolio > contact email = the shared mailbox. The founder retypes their Facebook password.
5. **Decide Tech Provider on purpose** (below).
6. **Start verification from the app.** The portfolio's Business info page may say "Your organization does not need to be verified" with no start button until an app asks for advanced access. Start from App Dashboard > Settings > Basic > Verification, or the app's Verification page > Business verification > Start. (done on Givi)
7. **Wizard:** country > entity type > company number and trading name > address > contact > reCAPTCHA (founder) > documents and ID.
8. **ID rules for the agent.** Measure the file first (`sips -g pixelWidth -g pixelHeight id.jpg`); if it is too small, ask for an original sent by AirDrop or cable, because messengers compress photos. **The agent never alters an identity document**, even when asked. Givi's compressed passport photo was upscaled, accepted by the form, then failed with "technical issues", and an altered ID can get the business flagged for tampering. An original photo of a national ID card worked. (learned the hard way)
9. **Verify:** "In review", then "Verified". Record the date on the tracked item.

**Agent tips for Meta's forms.** (learned the hard way)
- Meta's dialogs are React forms; typing by position puts values in the wrong fields. Set each input by label or `aria-label` with a JavaScript setter (focus, set value, dispatch `input` and `change`), read every value back, then Save. Reload and re-read; some "Add" buttons fail silently.
- Never press Escape in a Meta dialog. It discards the form.
- The GDPR country picker is a virtualized list. Scroll `[role=listbox]` with JavaScript in steps until the option renders, then click it.
- Where the Graph API covers a setting (app domains, privacy and terms URLs, contact email, roles, webhooks), set it by API and read it back with GET. (recommended, not tested by us)

### Tech Provider and Access Verification

**What Tech Provider means.** "Become a Tech Provider" tells Meta your app will access other businesses' data to serve them. Meta's docs require it for permissions such as `ads_management`, `business_management`, `pages_manage_posts` or `instagram_business_content_publish` on assets your customers own. The choice cannot be reversed, so get the founder's separate, explicit yes. If the product will only act on your own assets, look for the plain Business Verification route first. (Givi chose Tech Provider because it manages customers' ad accounts; the plain route was not tested by us.)

**Access Verification** comes with it: App Dashboard > Verification > Access verification > Start verification. One honest paragraph: what the product is; that owners connect their own accounts; that changes happen only after the owner approves each one; that data is not sold or shared; whether you manage other businesses' portfolios.

Meta's docs say new apps get a decision in about 5 days. Givi's was still "In review" more than 14 days later, with a deadline after which the app is restricted. Until it passes, calls on other businesses' assets fail with error code 100 unless the user has a role on your app. Submit it the minute Business Verification passes, put the deadline on an automated check, and open a developer support case if nothing moves in a week. (submission done on Givi; the deadline check and support case were not)

---

## 2. Meta App Review

### Decide whether you need it at all

Meta requires App Review when your app will be used by anyone with no role on the app and no role in the business that owns it; unapproved permissions can only be requested from people with a role. Meta tests your app during review, and if its reviewers cannot get in, the whole submission is rejected. (Meta docs, checked 13 Oct 2026)

Do it only when revenue depends on it, normally after 3 paying customers, and plan for Givi's real cost (above). **Size every estimate from the whole chain** (testers, real API calls, films, descriptions, data handling, legal ticks), never from "the remaining clicks". Givi's agent first called the rest "about an hour together"; that 20x underestimate made parking it for 8-10 days look free. (learned the hard way)

### Scope gate: round 1 holds only what makes money

Before building anything, write one row per permission: does it make money this month; is it already covered by something approved (Composio, Welder, a system-user token on your own assets); what does it cost to build (film, tester account, real outcome, special in-form rule).

Round 1 holds only the revenue-critical permissions and the dependencies Meta lists for them. For an ads product that is typically `ads_read`, `ads_management`, `business_management`, `pages_show_list`, `pages_read_engagement` and Marketing API access, shown on your own ad account with campaigns created PAUSED. Publishing, comments, Messenger and Direct auto-replies, Threads and lead ads go in round 2, once round 1 is in Meta's queue. Each permission gets its own decision, so a second round costs only its own work. Any later widening goes through the same table, with one line on what it delays, and a second model is asked to attack exactly that. (learned the hard way: Givi merged two planned rounds and added messaging auto-replies, which forced a real Facebook tester, the 30-second comment rule and extra films, and pushed the ads permissions past their target)

### Steps

1. **Audit the live app before planning** (15 minutes): requests, use cases, login settings, API test counters, alerts. Givi's first plan, written from the repo, missed a permission, kept unneeded ones and missed an empty redirect-URI list. (learned the hard way)
2. **Harvest Meta's in-form checklists on day 1.** In the draft, open each permission's "How will this app use" card > Get started, and save the text. They held rules the public docs did not: an Instagram comment reply within 30 seconds; the test post link and trigger in the reviewer instructions; a real Facebook Tester for Messenger (Meta test users not accepted). Givi read them after filming and re-shot. (learned the hard way)
3. **Add permissions properly:** Use cases > Add use cases, then per permission Customize > "Add to App Review". A use case alone does not put its permissions in the draft.
4. **Facebook Login for Business > Settings:** redirect URIs, Strict Mode on, Enforce HTTPS on.
5. **Store the App Secret and test it at once.** The founder copies it from Settings > Basic > App Secret > Show (never Reset) into a small local script that stores it and prints only its name (pattern in `12-running-agents.md`). Validate with one Graph call that never prints it, an app-token request with `grant_type=client_credentials`; a wrong secret returns error code 1. (learned the hard way: time went into debugging OAuth code when the secret was simply wrong)
6. **An isolated review host:** a small separate service (Givi: Railway, 0.25 CPU, 0.5 GB) running the current design with its own database and keys, production untouched. Replace `window.confirm` dialogs with in-page ones; system dialogs freeze agent browser control. (done on Givi)
7. **Testers before the first OAuth** (see "Reviewer test account").
8. **One real successful call per permission** within the 30 days before submitting, as Meta requires. Counters update within about 2 days; Threads lagged up to 24 hours, so run it first. Per permission: one approved write, one API read-back, one native-app screenshot, on your own labelled assets only. Ads are created PAUSED and re-read; messages are received in a real inbox; lead ads use Meta's Lead Ads Testing Tool. (done on Givi)
9. **Film** (below).
10. **Descriptions,** drafted offline: why the user needs it, the reviewer's steps, the film and timecode. Reopen each card after saving, because Meta saves slowly and reorders cards. Tick each usage-purpose box; Givi caught an unticked one at the last minute.
11. **Upload screencasts** with the visible upload button (the hidden input fails) and reopen each. A permission with no upload field gets its film under Reviewer instructions > Supporting documentation.
12. **Reviewer instructions:** public steps, the test post URL and keyword, which film shows what; the logins go into the private field only after the founder's explicit yes.
13. **Data handling** (below): a submit blocker if incomplete.
14. **Allowed usage** (Givi: 25 agreements) are legal attestations: the founder ticks them; the agent prepares and re-reads them.
15. **Submit as the owner.** Re-verify the logins, connections and one live call per platform first. The founder presses Submit; verify "Review in progress" with every item listed. (done on Givi)

### Screencast requirements

Meta's list (submission guide and screen-recording page, checked 13 Oct 2026):
- A recording for every permission and feature requested. If reviewers cannot see from it why you need a permission, they will not approve it.
- Start logged out (log out of test accounts first) and show the login, the user granting each permission, and the app using each one.
- English UI where possible; otherwise captions and tooltips.
- 1080p or better, monitor at 1440 pixels wide or less, full screen or full window, no audio.
- A larger cursor, mouse rather than keyboard, zoom into small areas, annotate where a permission is used. Show "how", not "why".

What we learned on top:
- **Prove the recording route in 15 minutes before promising films:** one 15-second file checked with `ffprobe`, including the real frame size (a requested 1080p viewport once gave 1237 x 1104). Givi lost about a day on recorders that hung. (learned the hard way)
- **The route that worked:** the agent drives the product at 1920 x 1080, captures frames per scenario, adds captions and privacy masks with a short Pillow script, and encodes silent MP4s with `ffmpeg`. Alternatives: Playwright `recordVideo`, OBS over its WebSocket API, `screencapture -v`. (done on Givi; Meta's acceptance not yet known)
- **Film the first-ever permission grant.** Refresh flows do not show the first-time screen. Givi connected the real accounts "outside recording" and had to redo 4 films with stills its own audit judged short of the guide. If a grant already happened, revoke the integration in the platform's app settings and film it again. (learned the hard way)
- **OCR every frame** and mask emails, IDs and long strings before upload. (done on Givi, about 2,500 frames)

### Reviewer test account

- **A login on the review host** such as `meta-reviewer@yourdomain.com` (no mailbox needed), no MFA, free access for 3+ months, made by a server-side script with `--seed` (sample data created through the app's own API) and `--reset` (a new password written to an owner-only file or the clipboard, never printed). Run it with `python -u` and a timeout; buffered output hid a failure on Givi.
- **Rotate any credential ever shown in chat** before it goes into a vendor field. Givi's reviewer password was printed in chat and given to Meta unrotated. (learned the hard way)
- **Testers.** An unpublished app accepts OAuth only from Tester accounts ("Insufficient developer role" otherwise). Instagram and Threads: `developers.facebook.com/apps/<app_id>/roles/roles` > Add people; close the account picker before Add, then reload and confirm "Pending". The owner accepts at `instagram.com/accounts/manage_access`, which also accepts Meta's Platform Terms. For a business-owned app, add Facebook testers in Business Suite: Settings > People > Assign assets > Apps > "Test app".
- **Messenger needs a real, separate Facebook account** with a Tester role, registered as a developer by SMS or card: a consenting teammate's own account made for the purpose, with the consent recorded and the password changed after Meta decides. Never put anyone's everyday social-media password in a vendor form. Givi's tester waited about 21 hours for SMS codes that never came; card verification is the fallback. (learned the hard way)
- **Keep it all alive until Meta decides,** with a daily health check of each connection that alerts only on failure. (recommended, not tested by us: Givi's host asked to reconnect Facebook on submission day, and nothing watched it)

### Privacy policy URL validator

Meta will not save a privacy URL that does not load, and its validator can reject a page that loads fine in your browser. Givi's main privacy page was rejected in the App Review form for a reason nobody diagnosed; the app was pointed at a privacy page on the review host, which passed. That ties the production app to a review stand. (learned the hard way)

Diagnose first (recommended, not tested by us):
1. Meta's Sharing Debugger: `developers.facebook.com/tools/debug/`.
2. `curl -A 'facebookexternalhit/1.1' -sI https://yourdomain.com/privacy`: status code, redirects, any challenge page.
3. `robots.txt`, redirect chains (www to apex, HTTP to HTTPS), and any bot-protection or firewall rule (for example on Cloudflare) that challenges Meta's crawler.
4. Fix the main page. If a temporary page is the only way forward, open an item to point the app back to the main URL before it goes Live.

### Data handling and Data Use Checkup

**Data handling** comes with the submission: the controller (your company and country), every processor with the countries where it processes or can remotely access data, national-security request disclosures, and request-handling procedures. List every processor from a vendor register: hosting, database, each model provider, any model router, and any connector platform holding the platform's tokens. Givi missed a model router and the connector platform holding its production Meta connections, and submitted country lists its own notes called an "incomplete draft". The founder confirms the facts; the agent never invents countries. **Incomplete answers are a submit blocker.** (learned the hard way)

**Data Use Checkup** is an annual certification for apps with advanced access or live use cases: an admin re-examines approved permissions, certifies allowed usage and answers data-handling questions again to keep API access. Set a yearly reminder the day the app is approved. (Meta docs, checked 13 Oct 2026; not reached on Givi)

### While in review, rejection, approval

- **Timing.** Meta's guide says submissions "should receive a decision within a week". Givi's was pending when this was written.
- **Feedback** arrives under App Review > Requests, in developer alerts and by email to the app contact. Search the shared mailbox for "App Review" and "Meta for Developers" in the weekly sweep.
- **Rejection.** Each permission is decided separately. Resubmit only the rejected items, fixing exactly what the reviewer named. (recommended, not tested by us)
- **After approval:** publish the app Live; switch your Meta sign-in on for customers only after the founder's yes; re-test with a fresh owner who has no role on the app; point any temporary privacy URL back; downgrade logins that became full portfolio admins during setup; rotate reviewer and tester passwords; set the Data Use Checkup reminder. (recommended, not tested by us)

---

## 3. Directory listings

### Claude connectors directory

For products with a remote MCP server. Submit after 3 paying customers, from a company-owned Claude organisation. About 1 agent-hour once the server is ready; about 10 founder minutes.

**Who and where (checked 13 Oct 2026):** anyone on a paid Claude plan, at `claude.ai/directory/manage` > Submit new > MCP connector. Use an organisation the company owns, created before you submit, because a listing's owner cannot be moved later. Never the founder's personal account. (learned the hard way: Givi submitted from the founder's personal account)

**Requirements:** a remote HTTPS server; OAuth 2.0 for anything that acts on a user's account; every tool with a `title` and a `readOnlyHint` or `destructiveHint`; no promotional wording in tool descriptions or results; documentation URL, privacy policy URL, support contact and icon; a fully populated reviewer account. The server's host should never redirect, and its origin is permanent once published.

**Steps:**
1. **Self-test as a custom connector** (Claude > Customize > Connectors > Add custom connector) and call every tool in one chat, **signed in as the reviewer or a test account, never the founder's real account.** Givi's self-test ran write tools on Vito's live account and paused and resumed one of his real scheduled jobs. Note and verify the undo for every write tool. (learned the hard way)
2. **Seed the reviewer account** (script above) with data that matches your example prompts.
3. **Fill the portal:** Connection > Tools > Listing (name up to 100 characters, one-liner up to 200, description up to 2,000, 1-5 categories, a permanent URL slug) > Use cases > Company > Authentication > Data handling > Test & launch > Compliance (seven acknowledgments) > Review and submit. Pick your connector explicitly on step 1 (Givi's portal preselected another). Progress saves only in that browser, so finish in one go.
4. **The founder's step.** Extensions cannot type into password fields, which is correct. Send a short card, wait for "here", put a freshly reset reviewer password on the clipboard, and give 3 clicks with a screenshot. The founder pastes, ticks the seven acknowledgments (the terms include an indemnity) and submits. Clear the clipboard afterwards (`printf '' | pbcopy`).
5. **After submitting:** an automatic scan lists the connector as Community by default; some get a human review, with queue-dependent times. Status and feedback show in the portal. Never reset the reviewer password during a review.

> **What happened on Givi.** Filling the form took about 3 minutes. The submission took about 3 hours 15 minutes: about 1.5 hours of real work (a privacy section on assistant connections, a full-bleed icon, the seeding script, removing promotional words from tool descriptions) and about 1 hour 45 minutes of waiting, because the founder step was posted inside a long terminal message while Vito was away. Status at the time of writing: "In review".

### ChatGPT apps directory

Only if you plan a ChatGPT listing, and after 3 paying customers. It needs OpenAI organisation verification first. Givi never started that, so the channel stayed blocked although the submission kit was ready. (learned the hard way)

**Organisation verification (the clock to start early).** `platform.openai.com` > Settings > Organization > General > Verifications, in the organisation that will own the app, with the Owner role. Rename the organisation after the company and verify as a business: the directory shows the verified name, so verifying as an individual would publish the founder's personal name. OpenAI's help article (checked 13 Oct 2026) says the ID check takes minutes and needs an original government ID not used for another organisation in the past 90 days; business verification wants the legal name exactly as registered and may be checked against registers, with no published review time. Start it the day the company number arrives.

**Submission (OpenAI Apps SDK docs, checked 13 Oct 2026):**
- Submit as an organisation owner or a member with Apps Management Write.
- A ZIP package including the MCP server (one per package).
- Exactly 5 positive and 3 negative test cases, plus a video walkthrough.
- Domain verification: serve the challenge token as plain text at `https://<mcp-host>/.well-known/openai-apps-challenge`. Serve it from an environment variable on the MCP host itself; Givi's apex domain redirected unknown paths.
- After approval, you choose when to publish.

From Givi's preparation: no price, trial, plans, upsell or ChatGPT comparisons in the listing; lead with what your product adds that ChatGPT cannot do natively; run all 8 test cases in ChatGPT developer mode first. Givi's kit noted that projects with EU data residency could not submit; the current page does not mention it, so check on the day. Budget about 3-4 agent-hours plus one founder video session. (estimate; not submitted on Givi)

### Review sites

G2, Capterra and AlternativeTo help with search and with buyers who compare tools. They wait for 3 paying customers and a stable offer, because they cost agent hours and your offer will change first. (learned the hard way: Givi's kit from day 5 still said "Private pilot. Contact us" after two public price changes, and nothing was submitted)

| Site | How | Notes |
|---|---|---|
| G2 | Free profile request at `sell.g2.com`; vetting about 3-5 business days, then claim approval in 1-3 (checked 13 Oct 2026) | Collect reviews here first |
| Capterra, GetApp, Software Advice | Free vendor listing. G2 announced on 29 Jan 2026 it would acquire all three from Gartner, so the vendor flow may route through G2: check on the day | At Givi's check (Sep 2026) Capterra reviews flowed to GetApp and Software Advice, and Software Advice warned of 6+ weeks |
| AlternativeTo | Free, "Suggest new application" | Link only to alternatives that match the job |
| Product Hunt | A personal maker account (company accounts were banned at Givi's check) | Only once 3 strangers have paid and a demo path exists. Ask for discussion, never upvotes |
| Trustpilot, TrustRadius, paid AI directories | Later; paid ones only with an approved amount | |

Recipe (recommended, not tested by us): one listing kit in the repo (descriptions in three lengths, honest category and feature ticks, pricing wording from your offer file, three screenshots, a short real-result video), with no unverified integrations and no invented founding year or headcount, listed among your offer surfaces so price changes reach it. One agent pass of 1-2 hours with Claude in Chrome covers the three free sites. Review invitations go out on an objective usage event, with neutral wording and no reward tied to the rating.

---

## 4. The long-lead table

"Start when" is the earliest moment the prerequisite exists. Each row becomes a tracked item with an owner and a re-check date the moment it starts; an outside item idle for 24 hours is raised in the daily digest (see `13-daily-ops.md`). Waits are Givi's where measured; vendor figures were read in Oct 2026.

| Item | Typical wait | Start when | Blocks if late |
|---|---|---|---|
| Company (UK limited company) | About 24 hours online, about £100 (Givi filed on day 6, late) | Day 0 | Every company verification, Stripe live mode, policy pages |
| Business bank account | Days; not measured | Company number day | Stripe activation and payouts, ad billing on a company card |
| Trademark screen | Minutes | Before buying the domain | A forced rename later |
| Domain and shared mailbox | Minutes (Givi waited hours on founder answers) | Right after the name | Every contact field, policy pages |
| Facebook Page | Minutes, but an SMS check can stall it (Givi: 14 days, about 12 idle) | Right after the name, on the founder's phone (S1b) | Ad account, Instagram ads |
| Meta portfolio, app, Tech Provider choice | About 2 hours of sitting time | Portfolio after the name (S1b); app on company number day (S2) | Business Verification |
| Meta Business Verification | 19 hours on Givi; Meta allows up to 14 working days | Company number day | Full ad limits, App Review, Tech Provider access |
| Tech Provider access verification | Meta: about 5 days; Givi: 14+ days and counting | The minute Business Verification passes | Customers' Meta assets; restriction after a deadline |
| Meta ad account and card hold | Minutes with a clean login (Givi: an old unpaid balance elsewhere blocked new cards for about 2.5 days), and a failed card hold is silent (Givi: about two days of "Active" ads delivering nothing) | S2; force one small charge before launch | Paid delivery (`10-paid-ads.md`) |
| Meta system-user tokens | Minutes (Givi: 13 days late) | Same sitting as the ad account | Reliable reporting and emergency pause |
| Meta App Review | 20-25 agent-hours; Meta says a decision in about a week | After 3 payers, unless revenue depends on it | Features on customers' Meta assets |
| Stripe activation and live key | Hours to days after company and bank (Givi: 11 days, mostly waiting) | Identity checks on company number day | Live payments, the real card test (`06-payments-stripe.md`) |
| D-U-N-S and Google advertiser verification | Days; not measured (Givi started on day 24) | Company number day, only if Google ads are planned | Google ads with your brand |
| Google OAuth brand verification | Minutes to days | When the sign-in domain and policy pages are live | A branded sign-in screen (Givi's showed a third-party address while almost every visitor left at sign-in) |
| Google sensitive scopes | 3-10 business days; restricted scopes (Gmail, Drive) add a paid security assessment of about 3-8 weeks | Once the smallest demo works | Features that read users' Google data |
| OpenAI organisation verification | Minutes for ID; no published business review time; never started on Givi | Company number day, only if a ChatGPT listing is planned | ChatGPT directory |
| Claude and ChatGPT directories | 1 and 3-4 agent-hours; review times vary | After 3 payers, from company-owned organisations | Listings; owners cannot be moved later |
| G2 and Capterra | G2: 3-5 plus 1-3 business days | After 3 payers and a stable offer | Review collection |
| LinkedIn, TikTok posting and Microsoft app reviews | No published time (LinkedIn); weeks with a demo video (TikTok); 3-5 business days after partner verification (Microsoft) | After 3 payers, once the smallest demo works; an empty submission leaves a rejection on record | Posting or integrations through your own app |
| Slack Marketplace | Needs 10 active workspaces and 10 weekly users, then weeks; until then label Slack a free beta (done on Givi) | Only if buyers ask for Slack | Selling a Slack app tied to a paid product |
| TikTok profile and ads | Givi: profile 11 days; ad review 6+ hours per edit | Only if the product fits TikTok | The TikTok channel |
| Cold-email mailboxes | Fresh: 2-4 weeks of warm-up (Instantly's guidance); pre-warmed: usable that week | Day 1, if cold email is planned | Cold outreach in week 2 (`08-outreach.md`) |
| Apple and Google developer accounts | Apple organisations need a D-U-N-S number, then store review per release | Day 0, only for a mobile app | Any mobile release |
| CI budget (GitHub Actions) | 2 minutes; a $0 budget stops CI silently (Givi: about 7 days down) | Day 0 | Every reviewed merge and deploy |

---

## 5. Track every clock

Givi's real outside waits were short; the idle time around them was long. The Page sat about 12 days with nobody retrying, App Review sat 8-10 days after "save this for later", OpenAI verification never started, and the D-U-N-S request began 18 days after the company existed. None had a dated item with an owner. (learned the hard way)

The pattern (recommended, not tested by us end to end):
1. **One work-item file per long-lead item** on day 0 (for example `operations/long-lead/<item>.md`, or an issue in your tracker): owner, prerequisite, realistic estimate sized from the whole chain, status with evidence and date, next check date.
2. **One founder-blockers list** whose open entries head the daily digest until cleared.
3. **Park the work if you must; the clock keeps a date and a scheduled check.** Tell the founder the real size before they decide to park.
4. **Automate the checks.** Consoles that need the founder's signed-in browser are read by the operator agent at fixed times; anything an API or health endpoint exposes is read by a scheduled cloud job with read-only tokens. Cover App Review status, the Tech Provider deadline, directory status, review-host health and token expiries (renew a 60-day token at day 50). Alerts go to the venture's alert channel, never a personal chat used for other things.
5. **Items for work with an owner but no outside clock,** dated for when they open: review sites, and Slack workspace recruiting if Slack is a channel. On Givi neither had an item, and neither moved.
6. **Write status at its evidence level,** and check the repo, the items and the live console before asking the founder "did we submit X?".

---

## Founder steps

Only the founder can do these. Batch them into the setup sittings S1a-S3b (`01-framework.md`) and, once reviews open after 3 payers, one weekly founder slot.

| Step | When |
|---|---|
| Facebook and Instagram logins with 2FA; password retype at app creation; Create on the Page and ad account | S1b (Page, Instagram) and S2 (app, ad account) |
| Tech Provider choice, as its own numbered yes | S2 |
| reCAPTCHA, ID upload, SMS codes, OpenAI and Google verifications if planned | S2 |
| Accept the policy texts | Before S2 |
| One dated, batched consent for App Review (OAuth on your own test assets, tester invites, credentials into Meta's private field, labelled test posts with the first of each shown) | When App Review prep starts |
| Tester invite acceptance, Allowed usage ticks, Submit, Publish, directory acknowledgments, reviewer password paste | Weekly founder slot |

Tell the founder out of band the moment a step is ready (a question inside a long terminal message waited 1 hour 45 minutes on Givi), give 2-3 numbered clicks with a screenshot, and never promise a fixed number of founder actions: Meta may add a password, 2FA, a CAPTCHA or a document request at any time.

---

## Gotchas not covered above

| Symptom | Cause | Fix |
|---|---|---|
| Instagram webhooks get 403 | Signature checked with the Instagram product secret | Meta signs with the parent App Secret |
| Comment auto-replies cannot be demonstrated | Comment notifications need the Advanced Access you are applying for | Poll one labelled test post for an exact keyword |
| Hiding a Threads reply fails | Threads hides only other accounts' replies | Reply from a second account |
| Ad creation rejected with a new error code | Newer API versions need extra fields | Read the versioned docs; use versioned Graph URLs |
| "Nothing pastes" for the reviewer password | Clipboard overwritten; a reset invalidates the old one | Reset onto the clipboard again |

---

## Checklist

**Start now**
- [ ] Company-facts file filled from the public register
- [ ] Shared mailbox receives mail
- [ ] Policy pages return 200, with retention timelines, a deletion section, assistant connections if relevant, and no pilot, beta or demo wording
- [ ] Icon set (1024, 512 full-bleed, 120 px) and current favicon
- [ ] No unpaid balance on any ad account the founder manages
- [ ] Meta portfolio, Page and Instagram created in S1b; nobody leaves without the Page
- [ ] Meta app created; Tech Provider decided by the founder's separate yes
- [ ] Business Verification submitted the day the company number arrived; ID measured and unaltered
- [ ] Access verification submitted the minute Business Verification passed; deadline on an automated check
- [ ] OpenAI verification (as the business) only if a ChatGPT listing is planned; D-U-N-S and Google advertiser verification only if Google ads are planned
- [ ] One tracked item per clock with owner, estimate, evidence and next check; deferred items dated for after 3 payers

**Meta App Review (only when revenue depends on it)**
- [ ] Live app audited; scope gate written and challenged; round 1 holds only what makes money
- [ ] In-form checklists saved on day 1; every permission added with "Add to App Review"
- [ ] App Secret stored by script and validated; isolated review host; reviewer login made by script, never printed; exposed credentials rotated
- [ ] Testers accepted, including a consenting teammate's real Facebook account for Messenger
- [ ] One real call per permission within 30 days
- [ ] Recording route proved; films show logout to login, the first-ever grant and each permission; privacy pass clean
- [ ] Data handling complete, or not submitted; main privacy URL accepted or the rejection diagnosed
- [ ] Founder ticked Allowed usage and pressed Submit; "Review in progress" verified; daily review-host check until Meta decides
- [ ] After approval: Live, fresh-owner test, admins downgraded, passwords rotated, yearly Data Use Checkup reminder

**Listings (after 3 payers)**
- [ ] Claude: company-owned organisation; self-test as the reviewer account with every write undone; founder pasted the password and ticked the acknowledgments; "In review" verified; clipboard cleared
- [ ] ChatGPT: organisation verified as the business; 5 positive and 3 negative cases; domain challenge on the MCP host; video; founder submitted
- [ ] Review sites: kit matches the current offer; G2, Capterra, AlternativeTo listed and verified; Product Hunt only after 3 strangers have paid
- [ ] Every status written at its evidence level
