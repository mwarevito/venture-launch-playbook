# Positioning, naming and pricing

Decide what you sell, to whom, under which name and for how much, once, from evidence, in the first two to three days. Agents run the market research, the name screen and the cost bench in parallel. The founder gives one intake reply, holds five buyer calls in week 1, picks a name and says yes to one offer page. Then the decisions freeze, and every page, ad and checkout reads the offer from one config file.

**Done when:** one market, one buyer, one first paid job, a "why us" sentence and a stop rule are written down and accepted; the name has passed a full screen (domains, company register, same-category products, handles, trademarks in every launch market); price, trial and allowance come from a cost bench showing that a typical user fits inside the allowance; the offer exists only in one config module and one canon file; and five buyer calls are booked for week 1.

> **What happened on Givi.** The positioning was rewritten about six times in 25 days, and the offer went through five setups in twelve days: $99 with a no-card trial, a $69 early bird, $49 with a $99 tier, a 3-day trial with the card collected at sign-up, and finally checkout as the sign-up step. Each rewrite came from founder frustration, one power-user tester or a frontier lab's launch. None came from a buyer, because nobody interviewed a target buyer in 25 days. The launch market was never chosen, so effort spread over the UK, the US, four cheap-ad markets and a second language. The name the founder finally picked was never trademark-screened, although ads ran in two countries. The price was cut from $69 to $49 while almost everyone was leaving at the sign-in screen, before they ever saw a price. Every price change meant re-rendering films and images, because the price was burned into them. Givi had no paying customer by 12 Oct 2026. The order in this file is the fix: research, buyer calls, one decision batch, a cost bench, then a freeze.

---

## The order, and how long each part takes

Steps 1-5 start on day 0 and run in parallel. The offer (step 7) waits for the cost bench (step 6), which needs a working engine.

| # | Step | When | Agent time | Founder time |
|---|---|---|---|---|
| 1 | Canon files | day 0, first hour | 20 min | none |
| 2 | Research fan-out | day 0 | 1-2 h wall clock, parallel | none |
| 3 | Buyer calls | booked day 0, held week 1 | 30 min to prepare | introductions, plus 5 calls of about 20 min |
| 4 | One market, one buyer, one paid job, "why us" | accepted by end of day 1 | 1-2 h | one reply, about 5 min |
| 5 | Name screen | end of day 0 or day 1 | about 1 h | one pick |
| 6 | Cost bench | day 1 on an existing engine; day 2-3 if built from zero | about 1 h | none |
| 7 | The offer in one batch | day 1-2 (day 2-3 from zero) | 30 min | one numbered reply |
| 8 | Offer as configuration | with the first checkout build | 1-2 h | none |
| 9 | Freeze and change protocol | from acceptance | about 1 h per change | one yes per change |
| 10 | Stop rules | day 0, inside the intake | 5 min | inside the intake |

No page shows a price until step 7 is accepted. A smoke page with the job and a waitlist can go up on day 0-1 (see `04-landing-pages.md`).

---

## Step 1. Create the canon files (20 minutes, day 0)

**(learned the hard way)** Givi created its market and go-to-market files on day 12. Until then, research from different agents piled up as competing truths, and later two documents showed different prices at the same time.

| File | What it holds |
|---|---|
| `bd/MARKET.md` | facts about the market: buyer, competitor table, category pricing conventions, the "not a differentiator" list |
| `bd/GTM.md` | decisions: market, buyer, first paid job, "why us" sentence, channels, paid gate, experiment log |
| `bd/offer.md` | the only home of the offer: headline, price, currency, trial, refund window, allowance, each public claim and its basis |
| `bd/offer-surfaces.md` | every place the offer appears and who updates it (step 8) |
| `bd/metrics.md` | definitions (visitor, paid, activation), acceptance metrics, stop rules |
| `decisions/DECISIONS.md` | one dated row per decision: proposed, accepted or frozen, with the founder's words and what it supersedes |

Every fact carries a tag and a date: `verified`, `vendor` (the vendor's own page says so), `secondary`, `assumption` or `proposal`. Edit the living file first, then add a change-log line saying what it replaces. Agents read canon from the remote, never from an old local checkout: `git fetch -q && git show origin/main:bd/offer.md`. **(learned the hard way)** One Givi checkout was hundreds of commits behind, and agents built from stale briefs.

---

## Step 2. Market research with agents (1-2 hours wall clock, day 0)

**(done on Givi, late)** Givi's research was sound, but it was redone six times between 17 Sep and 8 Oct, each time for a new question. Run it once, broadly, on day 0, then keep a weekly watch.

Launch 5-6 research sub-agents in one message, on a cheaper model, each with a self-contained brief. More agents do not help: one Givi review with 88 top-model agents hit usage limits twice and cost about 4.5 hours of work.

| Stream | What it returns |
|---|---|
| Direct competitors' pricing (8-10 vendors) | entry price, higher tiers, the metering unit (credits, seats, tasks), behaviour at the limit, trial length, card required, evidence tag, date read |
| Frontier-lab products in your lane | what they ship, at what price, in which countries |
| The cheapest substitute in each channel | for Givi, a $19-a-month chat-app assistant |
| Onboarding of the 3-5 nearest competitors | step by step, with screenshots taken signed out |
| Channel and platform policy per market | which messenger leads; platform terms that could bar you |
| What competitors advertise | hooks, offers and trials from the Meta Ad Library |

Paste-ready brief (the operator fills the angle brackets):

```
Today is <date>. You are researching one question for a new product. Product in one line: <line>. Buyer: <buyer>. Launch market: <market>.
Your stream: <stream and what to return>.
Read first-party pages only: the vendor's own pricing, help or docs pages, and investor or company posts for funding. Cite the URL and the date read for every row. If a page blocks you or shows no numbers, say so and leave the cell empty; never fill it from a third-party article. If a vendor contradicts itself, record both values. Tag each row verified, vendor, secondary or assumption.
Return a markdown table ready to paste into MARKET.md, then at most five lines on what it means for us. Do not create accounts, sign in or pay for anything.
```

Tools: `WebFetch` on each `/pricing` page, `WebSearch` for gaps; live model prices from the provider's API (`curl -s https://openrouter.ai/api/v1/models`); gstack `browse` for onboarding screenshots (`$B goto <url>`, `$B screenshot`); the public Meta Ad Library (facebook.com/ads/library), or `ads_library_search` if Meta's Ads MCP server is connected. **(recommended, not tested by us)** Givi never read competitors' ads first, and found its winning hook only in the sixth round of statics.

Gotchas **(done on Givi)**: some big vendors' pricing pages block `WebFetch` and headless browsers, so use their help centre and tag the figure `secondary`; sites that block reading are left out. Never study competitors inside your own signed-in accounts.

**Verify every decision-driving claim yourself (30 minutes).** The operator re-reads each claim that changes a decision (a price, a policy, a ban, what an API can reach) on the vendor's own page and tags it `verified` with the date. **(learned the hard way)** A Givi research agent said a CRM's MCP server could read only documentation; it could read account data, and the decision built on the wrong claim was redone.

**Derive the category conventions.** Five lines in `MARKET.md`: entry price band, metering unit, what happens at the limit, what higher tiers sell, common trial types. These set the price band before anyone picks a number.

> **What happened on Givi.** A 10-page pricing sweep on 28 Sep (about 5 minutes of agent time) found that nobody in the category entered at $99: entry tiers were $20-50, about $100 was the second step, and everyone metered usage. Givi had one $99 tier and an invisible limit. Run on day 0, the sweep would have prevented the first price.

**Keep watching weekly.** A scheduled job outside any agent session (a cloud routine or a server cron) searches for launches by frontier labs and direct competitors, adds dated rows to `MARKET.md`, and reports only when something lands in your lane. **(learned the hard way)** Givi learned of a frontier lab's always-on agents two days late, through a tester, then had to retire a brand device that suddenly looked borrowed.

---

## Step 3. Talk to five buyers before you position (book on day 0, hold in week 1)

**(learned the hard way)** Givi wrote an interview script on day 0 and never ran it. Its four testers were the founder, a co-founder, a developer friend and a family member; none was a target buyer. One question from the developer friend ("why do I need this when my coding agent can do it?") set off a full repositioning, although he was never the buyer. The protocol below is **(recommended, not tested by us)**.

A buyer matches the one-line buyer definition in step 4 and would pay from their own budget. Friends who build their own tools, family and the founding team do not count, however useful their bug reports are.

| Source of week-1 calls | Notes |
|---|---|
| Introductions from the founders' networks | the agent drafts one forwardable message with the booking link; the founder sends it personally |
| Replies to comments the founder leaves on buyers' LinkedIn posts | the agent drafts about 5 a day; the founder posts each one personally from the clipboard (LinkedIn's terms forbid automating a personal account). All five buyer conversations Givi had (replies, never full interviews) came from here **(done on Givi)** |
| A cold list (for example Clay MCP `search-companies`, `search-contacts`) | build it on day 0, contact it from week 2, after the founder approves the list and the text, through warmed mailboxes |

Book calls on a booking page on the brand's own calendar, never from the founder's personal inbox.

**The 20-minute call.** Show the "why us" sentence and two or three landing directions as private links. Ask:
1. How do you handle <the first paid job> today? Who does it, and how long does it take?
2. What have you tried for it? What did it cost, and why did you stop?
3. Would you set up <the frontier agent or cheapest substitute> to do this yourself? What stops you?
4. Which of these pages would you start from, and what would you click first?
5. What would it need to do in its first week for you to keep paying?
6. What would you expect to pay each month?

Write each call up the same day in `bd/buyer-calls.md`: role and business type (no names in shared docs), their words, and which positioning line it supports or breaks. Put the pass line in `bd/metrics.md` before the first call, for example "at least 3 of 5 recognise the first job as their own and name a price inside our band". Keep 3-5 conversations every two weeks after launch.

---

## Step 4. Choose one market, one buyer, one first paid job (end of day 1)

**(learned the hard way)** Givi left the first paid job "proposed but not chosen" for five days. An agent built a clickable prototype 20 minutes after the day-0 brief, and five days of re-skins followed until the founder said nobody would buy it.

| Decision | What it drives | What went wrong on Givi without it |
|---|---|---|
| **One launch market and its currency** | checkout currency, ad-account currency (permanent once created), which trademark registers to search, consumer law and VAT, which messenger leads, ad costs | an ad paired a pound figure with a dollar price and had to be paused; the chat app the product led with was not the main one in any target market; WhatsApp came off every page because Meta's WhatsApp Business terms bar general-purpose AI assistants outside the EU, EEA and Brazil (as Givi's agents read them on 3 Oct 2026) |
| **One buyer**, in one line: kind of business, size, place, language | landing copy, outreach lists, ad targeting, recruiting for calls | eight business types and seven industry films for a product with no buyer evidence |
| **One first paid job**, a whole job end to end | the landing hero, the demo, the first ad, the cost bench | "anything in, a file out" read as a free chatbot in disguise |

Size the first paid job like work people already pay staff or agencies for, shown from start to finish: "find leads, write the offer, send it, take the payment", never a small chore.

**The "why us" sentence.**
1. List what every competitor already has; it goes on the "not a differentiator" list and never leads the copy. Givi's list: always-on, memory, scheduling, approval before acting, connector counts, "lives in your chat app", and the price.
2. Write one sentence: what you do that the frontier agents and the cheapest substitute structurally do not. Givi's eventual answer was ease of use (one message, no setup, no workflows to build) plus real people behind the product, contrasted with "other AI agents". By the founder's rule, public copy never named ChatGPT.
3. Name the first paid job the sentence is proven on, and tag each line proven, customer-backed or assumption.

**Force it, then attack it.**
- Run gstack `/office-hours` (startup mode) by default, without asking. It forces the demand, status-quo and narrowest-wedge questions. **(learned the hard way)** On Givi a review skill asked whether to run it first, the founder said "do as you see fit", and it was skipped.
- Attack the result with gstack `/plan-ceo-review` (scope-reduction mode) or `/codex challenge`, which has a second model look for where the plan silently does less or overclaims.
- Present one private page of numbered yes/no lines with a recommendation on each; the founder answers in about 5 minutes. Work continues on a placeholder meanwhile.
- Record it in `DECISIONS.md` (accepted, the founder's words, the date) and in `GTM.md`.

**Freeze it for two weeks.** A change inside that window must cite something a buyer said or did. Founder frustration, a single power-user tester and a competitor's headline are reasons to look, never reasons to rewrite.

---

## Step 5. The name screen (about 1 hour of agent time, end of day 0 or day 1)

**(learned the hard way)** Givi's first naming round screened about fifteen candidates and dropped them all. Four days later Vito picked the name of an assistant bot the team already used. Nobody had asked whether he already had a name, so the screen was wasted, and the chosen name was never trademark-screened or checked against other software of the same name. Ads then ran in the UK and the US.

**Ask first.** One intake line: "Do you already have a name in mind?" If yes, screen only that name. If not, collect their anchors (family or place names, words that mean something to them, domains they own) and generate 10-15 candidates.

**Screen each candidate in parallel:**

| Check | How | Fails when |
|---|---|---|
| `.com` | RDAP: `curl -s -o /dev/null -w '%{http_code}' https://rdap.verisign.com/com/v1/domain/<name>.com`; 404 means no registry record (it says nothing about price). Try `get`, `use`, `hey`, `try` prefixes and `hq`, `app` suffixes | taken on the name and its useful variants |
| Other TLDs (`.ai`, `.io`, `.co`) | `https://rdap.org/domain/<name>.<tld>` redirects to the right registry; price and renewal from the registrar's search page | registered, or premium-priced. Web search is not a registry check |
| Same-category products | `WebSearch` for "<name> AI", "<name> app", "<name> <category>", then open the hits | any live product in your category or a neighbouring one, even if the domain is free |
| Company register | UK: Companies House search (`find-and-update.company-information.service.gov.uk/search/companies?q=<name>`); US: the registry of your state | a live company of that name in your field |
| Handles | Instagram, X, TikTok, LinkedIn page, YouTube; a Telegram bot username if needed (5-32 characters, ending in "bot") | the plain handle is held by an active account in your field |
| Trademarks in every launch market, with similar spellings | UK: UKIPO, from gov.uk/search-for-trademark (it blocks scripted fetches, so use a browser). US: USPTO Trademark Search, tmsearch.uspto.gov. EU: EUIPO eSearch, or TMview (tmdn.org/tmview), which covers many national offices. Sweep: WIPO Global Brand Database, branddb.wipo.int | a live mark for the same or a similar name in your classes (software is usually Nice classes 9 and 42); note famous marks in any class |
| The founder's own products and bots | ask, and search their sites and repos | any of them uses the name or a close variant |

All URLs above answered on 13 Oct 2026.

The agent scripts the domain rows: a small Python loop over the candidate list with `concurrent.futures`, calling the two RDAP URLs above and printing taken, no registry record, or check by hand for any other status code. It runs in seconds.

Gotchas **(done on Givi)**: Companies House pages carry a hidden "No results found" template, so strip `<script>` and `<style>` before reading. A free domain is never trademark clearance; for a brand you will spend real money on, ask a trademark attorney for a clearance search **(recommended, not tested by us)**.

**Choose and lock.**
- Show 3 finalists on one private page with their screen results. The final pick gets the full screen, even from outside the shortlist.
- Keep the company name separate and neutral ("<Something> Labs Ltd"), so the filing never waits for the brand.
- Buy the domain within 2 hours of the pick, in sitting S1b, on the venture's own card (Cloudflare Registrar sells at cost and gives DNS and email routing in one account). Claim the handles in the same sitting, on the founder's phone where platforms block automated sign-up. See `02-day0-accounts.md` for the run sheet.
- Lock the logo before any avatar, favicon or sign-in or payment-page branding is uploaded: about half a day, rendered marks shown at 512, 96, 40 and 20 px on light and dark, two rounds, two picks. **(learned the hard way)** Givi's logo came 14 days after the name, and an agent uploaded the old logo to a profile ten minutes before the founder asked for a new one.

---

## Step 6. Pricing from a one-hour cost bench

**(learned the hard way)** Givi's first prices came from category ranges and founder feel. A calibration on five tasks ran after the price was decided and built. The early bench underestimated real heavy tasks by 3-5 times, so the capacity line on the pricing card had to be corrected twice. The included AI allowance ended up about a third below what a regular user was estimated to spend: regular users would hit the limit before month end, which is the top complaint buyers have about the category. The internal cost estimate also ran about a fifth below the provider's bill until background sessions were booked. The bench below is **(recommended, not tested by us)** as one step; each part of it was done on Givi at some point.

**What you need first:** a working engine, meaning the founder's existing tool, a starter-kit fork or the product itself. Building from zero, the engine exists only around the end of day 2, so record a provisional price band on day 1 and freeze the exact offer on day 2-3.

**Instrument cost from the first deploy (1-2 hours).** Store the model, effort level, tokens and cost for every job, including background work and sub-tasks. Keep cost rows when test accounts are deleted (Givi lost its calibration data that way). Reconcile each API key daily against the provider's bill and alert above a 10% gap. Give agents a read-only database role, so a cost question never needs a founder click.

**Run the bench (about 1 hour):**
1. Pick 5-10 representative jobs per effort level (quick, standard, heavy), including the first paid job.
2. Run each on the real engine; record cost and time. Treat the result as a floor.
3. Build light, regular and heavy profiles as jobs per month, labelled as assumptions until live usage exists.
4. For each profile add model cost, hosting per customer, payment fees (your processor's current rate) and a share of fixed costs; compute the margin at each candidate price inside the category band.
5. **Check that a regular user fits inside the included allowance.** If not, raise the allowance, cut the cost per job, or say plainly who the plan is for.
6. Label every figure with its sample size and evidence level, and write a re-measure trigger, for example "after two weeks of live heavy jobs, if the median heavy-job cost is 25% above the bench, re-open the allowance".

Illustrative arithmetic (made-up numbers):

| Profile | Jobs a month | Model cost | Hosting | Fees | Cost if fully served | Margin at $49 | Fits a $20 allowance |
|---|---|---|---|---|---|---|---|
| Light | 100 quick, 10 heavy | $5 | $4 | $2 | $11 | 78% | yes |
| Regular | 300 quick, 40 heavy | $28 | $6 | $2 | $36 | 27% | **no: hits the limit around day 21** |
| Heavy | 600 quick, 120 heavy | $80 | $8 | $2 | $90 | capped by the allowance | no, by design |

Here the $20 allowance protects the margin but fails the regular user. Decide before anything is published: raise it to about $30 and accept a lower margin, cut the heavy-job cost, or sell this plan as "for light use" next to a higher tier.

Show the allowance in units buyers understand ("about 25 heavy jobs or 2,000 quick ones a month"), never credits or dollars of model spend. **(learned the hard way)** An abstract "$0.35 AI allowance" leaked into Givi's interface and confused testers.

---

## Step 7. Decide the whole offer in one batch (founder: one numbered reply)

**(learned the hard way)** On 8 Oct Givi shipped $49 at lunchtime, recorded a per-role price ladder an hour later, and replaced it with another plan shape that evening: three production releases in one day, because the first decision shipped before the plan shape was settled.

Put all of these on one page, each with a recommendation. Money items have no default: the offer freezes only on the founder's yes.

| Item | Notes |
|---|---|
| Price per plan, and the one price the landing shows | plan details live inside the account |
| Currency | one, matching checkout and ad accounts |
| Trial mode and length | card trial, no-card trial or no trial, held as one config value; card-first usually means fewer trials, so choose on purpose |
| Refund window | for example 14 days, automatic inside the window |
| Allowance and how it is shown | from step 6, in tasks |
| Top-up price | and whether auto top-up is on (default off) |
| Plan shape | every plan, tier, seat or role count, settled together; no plan shown that cannot be bought today |
| VAT and tax | UK prices shown to consumers must include VAT once you are VAT-registered; EU consumers bring their own VAT rules; decide on a merchant of record. Ask an accountant **(recommended, not tested by us)** |
| Subscription and trial rules | an auto-renewing card-first trial needs a check of subscription and auto-renewal rules in each launch market; trial ads must state the significant conditions (card taken, when and how much it charges, how to cancel) **(recommended, not tested by us)** |

How:
- A one-page decision memo scores the options on cash impact, reversibility and risk, and names the number the decision will be judged by and when (for example "trial-to-paid rate after 30 trials").
- Attack the plan with `/codex challenge` against the real code. **(done on Givi)** On 29 Sep this found five serious problems in about two minutes, including a founding price the code could not enforce and a capacity claim off by a large factor.
- Check each option against the brief. **(learned the hard way)** The founder chose "no bring-your-own-key plan in the first offer" on day 0; one was built on day 21 from a passing idea, with zero payers.
- Record the offer in `bd/offer.md` and the decision in `DECISIONS.md` with the founder's words, the judging number and what it supersedes.

Avoid, for a brand with no payers: early-bird deadlines, seat counters, struck-through prices nobody paid, "places are limited", and any urgency that is not literally true. UK consumer law bans false urgency, and dates get baked into every creative. **(learned the hard way)** Givi's $69 early bird came with a real end date, a hidden cap and a 12-month price lock; all of it was replaced nine days later.

**The founder's call wins on price and trial.** State the numbers and the judging metric once, in a dated record, then build exactly what the founder decides behind a switch so it can be reverted. **(learned the hard way)** On 11 Oct an agent spent 25 minutes arguing from data against a card-first trial the founder was already deciding elsewhere. Two lines with a measured trigger would have done the job.

**Define "paid" in code before counting anything:** a first charge above zero, not refunded within the refund window, scored on a fixed date after the window closes. A `trialing` subscription is not paid. Count warm, ad and cold-email payers separately; exclude free access and test payments. **(learned the hard way)** Givi's first metric counted trials as paid.

---

## Step 8. Keep the offer as configuration

**(learned the hard way)** Givi kept the landing price in a server-side config value from early on, so pages changed without HTML edits; that worked. Films and images did not: price and trial were burned into them, so offer changes meant re-rendering 16 films, rescheduling 24 posts and rebuilding 12 or more ads. A static image made in about 20 minutes ended up taking almost all the paid spend.

- **One plans module** (`plans.py`, `plans.ts`) holds price, currency, allowance, top-up, trial length and the capacity line. Every figure in copy is computed from it.
- **Stripe prices are created by a script with stable lookup keys** (`pro_monthly`, `plus_monthly`) in test and live mode. A change creates a new price; never edit a live one.
- **Feature flags separate deciding from going live**, for example `CARD_TRIAL=off|<founder email>|all` and `TRIAL_DAYS=3`. The founder's account gets it first, everyone after a check.
- **The landing reads the price** from `offer.md` at build time, or from a server-side token if the app serves the landing. No price is typed into HTML.
- **Rendered video and images carry the hook and the URL only.** Price, trial and allowance go in the ad's text fields or in an overlay rendered from the same config.
- **Profile bios carry no price and no dates.**

**The offer-surface register** (`bd/offer-surfaces.md`), one row per surface:

| Surface | Reads the offer from | Owner | How to update |
|---|---|---|---|
| Landing pages, terms, refund page | `offer.md` at build | landing owner | rebuild and deploy |
| In-app plan page and checkout | plans module, Stripe lookup keys | product owner | flag or new price |
| Ad text on each platform | `offer.md`, copied | ads owner | new ads; delete the old ones |
| Statics and films | hook and URL only | ads owner | nothing to change |
| Scheduled social posts | `offer.md`, copied | social owner | cancel and recreate |
| The assistant's own instructions, if it quotes the price | plans module | product owner | redeploy |

**Verify after every offer change:** the app's public offer endpoint signed out returns the new terms (`curl -s https://app.<domain>/api/offer`); landing, terms and refund pages match; a phone user agent finds no old strings on any public route, fallback and preview pages included (`curl -s -A "<iPhone Safari UA>" https://<domain>/ | grep -E "<old price>|<old trial words>"` returns nothing); Stripe prices read by lookup key are live; each film's end card shows no offer (`ffmpeg -sseof -0.5 -i film.mp4 -frames:v 1 endcard.png`, then look).

---

## Step 9. Freeze, and the change protocol

Each decision freezes just before the first thing that depends on it is built.

| Decision | Freeze by | First dependent | Frozen until |
|---|---|---|---|
| Market, buyer, first paid job, "why us", stop rule | end of day 1 | landing, outreach lists, ads, legal checks | 2 weeks; a change cites buyer evidence |
| Name | end of day 0 or 1, before the domain | domain, company, handles, logo | never changed after handles and the company exist |
| Logo | end of day 1 | avatars, favicon, sign-in and payment branding | a change means re-uploading everywhere the same day |
| Offer (price, currency, trial, refund, allowance, plan shape, VAT stance) | day 1-2 after the bench (day 2-3 from zero) | landing price, checkout, terms, ads | 10 buyers have reached checkout |
| Ad-account currency and time zone | before any ad account exists | every budget and cap | permanent: Meta and Google do not allow a change |
| Taste and bans | day 0 | every page, film, ad and logo | two landing rounds at most (see `04-landing-pages.md`) |

**Changing a frozen decision.** **(learned the hard way)** On 8 Oct the price changed at 13:37. The pricing session noted that the ads still said $69 but neither paused them nor told the ads session; Google served the old price all afternoon until the founder caught it at 18:02. A Meta pause made through an MCP tool landed as an unpublished draft, so the campaign stayed live. Three days later the trial change repeated the re-render cycle. The protocol:

1. **Evidence:** a one-page memo with the new value, evidence and sample size, the judging number, and every affected surface.
2. **Decision:** the founder's numbered yes in the operator's own chat; a yes relayed through another session does not count for a money or sign-in switch.
3. **Pause paid first.** For Meta, pause through the Graph API and read the status back (use a versioned URL):
   ```bash
   curl -s -X POST "https://graph.facebook.com/v<NN>.0/<CAMPAIGN_ID>" -d status=PAUSED -d access_token="$META_TOKEN"
   curl -s -G "https://graph.facebook.com/v<NN>.0/<CAMPAIGN_ID>" -d fields=effective_status -d access_token="$META_TOKEN"
   ```
   For Google, use an automated rule, a Google Ads Script or the API, with the Ads UI as fallback. **(learned the hard way)** A quota-limited ads tool ran out of monthly calls in the middle of Givi's pause.
4. **Switch in order:** site and terms, checkout, a live check, new ads (Givi's agents could not edit a published Meta ad's text, so create new ads and delete the old ones), bios, scheduled posts.
5. **Sweep:** `git grep` on `origin/main` for old price and trial words; the scheduled-post queue; every live and paused ad; film end cards; a phone user-agent `curl` of every public page.
6. **Broadcast** to every session that owns a surface, in the same turn.
7. **Close:** a new `DECISIONS.md` row supersedes the old one; the freeze clock restarts.
8. **Existing subscribers** keep their price until a stated date and get notice well before (at least 30 days by default; check each market's rules). Move them on that date to the new lookup key.

---

## Step 10. Stop rules

Write these on day 0, in the intake, so they hold when the launch gets emotional. Givi had no such set (one paid-traffic pause rule existed, and no daily check ever read it), so the set is **(recommended, not tested by us)**; the right-hand column shows what its absence cost.

| Rule | Default | What it prevents |
|---|---|---|
| Offer and audience | no payer after 20 warm conversations and 5 buyer calls, or after the written ad-spend limit, means the offer or the audience changes; features do not | Givi opened about 360 pull requests for two outside users |
| Scope freeze | until 3 payers: no new channels, languages, films, platform reviews or plans | a second language and seven industry films while sign-up leaked |
| Paid before the first payer | one capped test (one market, one ad set with 2-3 static ads, 10-15 a day, about 100 in total in the checkout currency), only after the funnel gate (G5 in `01-framework.md`) passes, the warm notes are out and the founder has recorded a dated override; stop at the cap or at 150 landing visits with 0 sign-ups | about £110 of ads for one sign-up and no card trials |
| Re-opening price or trial | only on a trigger written in advance, through the change protocol | a price cut nobody had reached yet |
| Reading by market | segment every number by market before an offer decision | about three quarters of one day's Meta clicks came from a cheap-market test outside the buyer |
| Split tests | none below about 1,000 visitors per arm reachable in 14 days (see `04-landing-pages.md`) | an 8-day test that ended 16 sign-in clicks against 14 |

---

## What needs the founder

| Decision or action | How to make it take minutes |
|---|---|
| Target, market, buyer, first paid job, price band, existing name, taste rules, stop rule | one numbered intake message with a default on each reversible line; the founder replies "defaults" or changes lines by number (about 10 minutes) |
| "Why us", name, logo | one private page each, numbered, with a recommendation (5-10 minutes each) |
| Domain and handles | inside sitting S1b, within 2 hours of the name pick |
| Buyer calls | a ready message the founder forwards with the booking link; five 20-minute calls in week 1 |
| The offer, any change to it, any spend | one page of numbered items plus a decision memo; no default on money; the founder's yes in the operator's chat |

Never a question: ".com or .ai" (default .com and say why), where hello@ lands (a free brand Google account is fine for a short test; move to Google Workspace once you answer customers by email, see `02-day0-accounts.md`), and whether to run `/office-hours` (yes). When the founder asks for testimonials with invented names, decline (fake reviews are banned under the UK DMCC Act 2024 and by Meta's ad rules) and offer case cards at once: business type and city, what was built, no invented people or quotes. **(done on Givi)**

---

## Checklist

- [ ] Canon files committed on day 0; every fact tagged and dated
- [ ] Research fan-out run in one message (5-6 agents, cheaper model, URL and date per row); decision-driving claims re-verified at the source
- [ ] Category conventions written; competitor ads read in the Meta Ad Library; weekly watch scheduled outside any agent session
- [ ] Five buyer calls booked on day 0 from introductions and LinkedIn comment replies; pass line written; cold list held until week 2; each call written up the same day
- [ ] One launch market and currency, one buyer, one first paid job decided
- [ ] "Not a differentiator" list and "why us" sentence written, evidence-tagged, accepted and frozen for two weeks
- [ ] `/office-hours` run by default; result attacked with `/plan-ceo-review` or `/codex challenge`
- [ ] Founder asked whether they already have a name
- [ ] Name screen done: RDAP, same-category search, company register, handles, trademarks in every launch market, the founder's own products; final pick fully screened
- [ ] Company name kept separate; domain bought within 2 hours of the pick and handles claimed in the same sitting (S1b)
- [ ] Logo locked before any avatar, favicon or branding upload
- [ ] Cost instrumented per job from the first deploy and reconciled daily with the provider bill
- [ ] Cost bench run on the real engine; a regular user fits inside the allowance, or the plan says who it is for
- [ ] Every figure labelled with sample size and evidence level; re-measure trigger written
- [ ] Whole offer decided in one batch, including plan shape, VAT stance and trial rules per market; attacked with `/codex challenge`
- [ ] No early-bird deadlines, seat counters, struck-through prices or false urgency
- [ ] "Paid" defined in code; trials excluded; warm, ads and cold counted separately
- [ ] Offer held in one plans module, Stripe lookup keys and feature flags; landing price read from `offer.md`
- [ ] No offer terms in any rendered video or image, or in bios
- [ ] Offer-surface register filled, one owner per surface
- [ ] Freeze dates recorded; ad-account currency chosen before any ad account exists
- [ ] Change protocol written down: memo, yes, pause paid first, switch order, sweep, broadcast, close, existing subscribers
- [ ] Stop rule, scope freeze, paid-before-first-payer rule (one ad set, 2-3 statics, about 100 in the checkout currency, only after the funnel gate) and market segmentation in `bd/metrics.md`
