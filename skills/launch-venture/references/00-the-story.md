# The Givi launch: what happened and what to change

Givi (heygivi.com), an AI business-assistant SaaS, went from a first brief on 17 Sep 2026 to a sign-up and payment path that worked for a stranger arriving from an ad on 12 Oct 2026. Claude Code and Codex sessions did almost all of the work. It ended with no paying customer, and only about 2-2.5 of the 26 days were real waits on outside parties. This file tells the story, does the arithmetic on where the time went, and turns it into ten changes and a compressed plan.

**Done when:** you have read this once, marked which of the ten changes apply to your venture, and started your plan from `01-framework.md`.

Reading notes:
- Day 0 is 17 Sep 2026; day 25 is 12 Oct 2026.
- Numbers are rounded. Founder hours and savings are estimates from message timestamps and step times.
- Evidence tags: **(done on Givi)** we did it and it worked; **(learned the hard way)** we did it wrong first; **(recommended, not tested by us)** reasoned from the launch and from docs. Every "Do instead" below is in the third group, because Givi did not get to run it.

---

## At a glance

| Measure | Value |
|---|---|
| Calendar time | 26 days, 17 Sep to 12 Oct 2026 |
| Agent sessions | about 190 Claude Code and Codex sessions; about 100 with real founder involvement; up to 6 Claude sessions plus Codex at once |
| Pull requests | about 360 in 19 days |
| Products built | 2, one thrown away |
| End state on 12 Oct | product live for all accounts, live Stripe, a 3-day card trial with checkout as sign-up, Meta and Google ads delivering, two platform reviews pending |
| Ad spend | about £110 across Meta, Google and TikTok, for 1 ad-attributed sign-up and 0 card trials |
| Paying customers | 0 |
| Founder attention | roughly 75 hours (estimate), much of it relaying information between sessions |
| Selling | 0 warm messages, 0 cold emails, 0 interviews with target buyers |

## What Givi is, and what the founder asked for on day 0

Givi gives the owner of a small team (an agency, a service firm, an online business) a persistent AI assistant that works inside Telegram, Slack and a web app, connected to the owner's own apps. The day-0 goal was ten subscriptions at $99 in the first month, with AI usage included up to a clear limit.

On day 0 the founder, Vito, gave a direction that later proved to be the right shape: reuse the personal AI assistant he already ran (built on an open-source agent engine) inside Telegram, Slack or any chat, package it as four role cases (front office, warehouse, ads, chat manager), and "start creating the social pages, registrations, ad accounts and the product flow right away". None of the account work started that day, and the product built over the next week went somewhere else.

## The launch in nine phases

| Phase | Dates (days) | What happened | Outcome |
|---|---|---|---|
| 1. Frame and research | 17-19 Sep (0-2) | Codex framed the brief in three rounds of multiple-choice questions (about 40 minutes); research streams; naming; legal route; local prototypes. On day 2 a hosting document proposed one persistent agent server per business | Goal and buyer set; two of three prototypes rejected |
| 2. First real loop | 20-21 Sep (3-4) | A 7-model eval inside the pinned agent container (about $5); a working local pilot in about 48 minutes; then "nobody will buy this" and a reset to "Givi, an AI hire" | Name chosen, domain bought |
| 3. Identity | 21-23 Sep (4-6) | Domain, hello@ forwarding, social handles, a UK limited company | Company exists on day 6. The filing takes about a day; the rest was a late start |
| 4. The detour | 22-26 Sep (5-9) | After a cost challenge, and without asking the founder, Codex built a platform that started a fresh virtual machine per task: 4 hosting services, 45 secured tables, credits, a 156-finding review, overnight outages. On day 8 the founder called production garbage | Mostly replaced within 48 hours |
| 5. Pivot | 26-27 Sep (9-10) | Claude rebuilt Givi as one persistent, white-labelled agent per customer in about 31 hours; Meta Business Verification passed | Friends go-live on day 10 |
| 6. Quality and testers | 27 Sep-2 Oct (10-15) | Quality round, redesign, domain move, ops monitoring, a $69 early-bird price, tester reviews, first films | Good enough for strangers; positioning shaken by a large AI lab's competing launch |
| 7. Big push and go-to-market setup | 3-6 Oct (16-19) | Go-to-market session started on day 16.8; 13 build agents in one night; live Stripe; Slack; a landing split test; socials; pixels; ad accounts | Ads usable on day 19, after a 2.5-day payment block |
| 8. Paid launch | 7-8 Oct (20-21) | Meta and Google live just before midnight on 7 Oct, TikTok next day; price cut to $49 | Ads barely delivering; zero conversions at launch |
| 9. Funnel repair | 9-12 Oct (22-25) | Failed card holds on Meta; the sign-in leak fixed; one landing; a card trial; checkout as sign-up | First real sign-up from an ad on 12 Oct; no card yet |

---

## Where the 26 days went

| Bucket | Days | What it was |
|---|---|---|
| Real outside waits | about 2-2.5 | Incorporation (about 1 day), Meta Business Verification (about 19 hours), ad reviews (hours; TikTok more than 6) |
| Product detour | about 7.5 | From the right shape on paper (day 2) to building it (day 9.5) |
| Go-to-market started late | about 6.4 | Paid-ready was possible around day 14.6; the paid launch came on day 21 |
| Funnel repaired after the paid launch | about 4.9 | Day 21 to day 25.9, fixing sign-in while ads ran |
| What remains | about 7 | 25.9 days minus the three agent-made losses |

The last row is the honest size of the launch with the same tools and new accounts: about a week of real work. Run in three parallel lanes (product, accounts, revenue), the step times give about 5-6 days to a paid-ready funnel. With an existing verified company and a fork of a working product, about 2-3 days. **(learned the hard way)**

### The critical path, in order

1. **Product shape, day 9.5.** Everything shipped before the pivot was a platform the founder would not sell.
2. **Company, day 6.** Every verification needs the legal identity. A UK company registers online in about 24 hours for £100, after each director verifies their identity through GOV.UK One Login (GOV.UK, checked 13 Oct 2026). It could have existed on day 1.
3. **Meta usable for ads, day 19.7.** Verification took 19 hours. The Facebook Page then sat about 12 days with no owner after a failed SMS check, and an unpaid balance on another business's ad account under the same login blocked every card for 2.5 days.
4. **Live payments, day 17.** Mostly a key swap waiting on the founder's paste. The real-card test was never done.
5. **Paid launch, day 21, then about 4 days of lost delivery:** a Meta A/B test object that held delivery until the next midnight, failed card holds hidden behind "Active" for about 2 days, and an hour of ads showing an old price.
6. **Sign-in that works for ad traffic, day 25.9.**

Warm outreach, the cheapest route to a first payer for a $49 product, never got onto the path at all.

---

## Output and effort

| Measure | Value |
|---|---|
| Effort split by work item | about 52% product engineering, 24% go-to-market, 10% accounts, payments and approvals, 15% agent tooling and coordination |
| Hardening the discarded platform | the test suite grew from about 300 to about 700; about 25 operations documents in five days; one 88-agent review that burned about 240M input tokens, most of its agents dying on the usage limit |
| Product work in the leakiest week | about 35 PRs live on 8-11 Oct while almost every Start click was lost at sign-in |
| Meta App Review | about 20-25 agent-hours and nearly 2,000 browser actions, for permissions the product did not need to sell |
| Films | about 30-40 agent-hours, no attributable sign-up. A static made in about 20 minutes took about 96% of UK and US Meta spend (5.6% click-through against 2.6%) |
| Organic social | 47 posts in 5 days, 0 site visits. LinkedIn comments the founder posted on buyers' posts produced all 5 buyer conversations |
| Outreach tools used | a handful of calls to the Gmail, Instantly and Clay tools, against several hundred to the ad and posting tools |

## Where the founder's time went

Only the founder can do four kinds of work: identity checks, money, taste, and first contact with people they know. Each took minutes once the options were laid out. The roughly 75 hours went mostly elsewhere: **(learned the hard way)**

- **Switchboard.** Carrying state between more than 90 sessions he talked to directly, often after midnight. At least 30 messages were pure relaying ("i'm really lost").
- **Acceptance testing for agents that had drifted.** About 15 hours over 25-27 Sep, finding out the agents had built the wrong product and forked two versions.
- **Broken hand-offs.** About 10 hours of wall clock on secret steps a dry run would have caught: a model key took about 2.5 hours, the live Stripe key about 3 hours (the first paste held two keys glued together), a directory reviewer password about 2 hours for a 30-second paste.
- **Permission blocks.** Every safety-classifier block on a deploy became a script for him to run. One rollout took about 16 hours.
- **Status questions.** After a "few pings" rule, problems went quiet too ("what should I do??? how are ads?"). Two sessions reported different Meta numbers on the same day.

Meanwhile the one growth step only he could take, approving and sending warm notes, never reached him as a ready batch.

## Money, the funnel, and shared accounts

- **The warning before launch:** about 370 "visitors" (mostly cloud scanners), 30 Start clicks, 0 sign-ups.
- **The sign-in leak:** 44 of 45 Start clickers left at sign-in, because Google's consent screen showed the database provider's domain instead of the brand. Later, Google sign-in turned out to be blocked inside Instagram's in-app browser.
- **The click-to-visit gap:** about two thirds of paid clicks never became a landing visit. It was never investigated.
- **The split test:** two landings, about 280 visitors each, 16 against 14 sign-in clicks. No verdict was possible.
- **The offer:** five configurations in twelve days.

One root cause sat behind six separate incidents: no account was reused on purpose, so agents used whatever login was open. **(learned the hard way)**

1. An unpaid balance on another business's ad account under the same login blocked the new Facebook Page and every card for 2.5 days.
2. The Google Ads account was created under a login that manages another business's ads.
3. The model-provider credit was shared with another business's paying customers and fell to a few dollars on launch night.
4. A Google Workspace "domain in use" recovery for hello@ turned the founder's personal Gmail into a Workspace account.
5. The YouTube channel stayed on another business's Workspace account, where it cannot be moved.
6. A competitor teardown run while signed in switched on six live cold-email campaigns in the founder's account of that tool, on a balance shared with another business.

---

## Top 10 changes for the next launch

Ranked by how much each would have moved the first payment and how much founder time it frees.

### 1. Build what the founder asked for on day 0, and prove it on production by day 2

- **What happened.** The founder asked to reuse the assistant he already ran. On day 2 a hosting document proposed exactly that. From day 5 Codex built a per-task virtual-machine platform instead. Claude spotted the fork on day 5 while reviewing and never raised it; Codex noticed on day 10, after the founder pushed. The pivot came on day 9 and friends could use the product about 27 hours later. **(learned the hard way)**
- **Why.** The day-0 asks were never written as acceptance criteria. The architecture changed without his one-line OK. Hardening started before anyone used the product for a real task. There was no kill rule.
- **Do instead.** Write the day-0 asks into the brief word for word, with a one-sentence product bar (Givi's: "must not feel weaker than the assistant I already use") and a kill rule ("slower than 60 seconds per typical task, or weaker than my own tool, means we switch within 24 hours"). Run a spike that packages what the founder already uses, live on a public URL by the end of day 2. The founder does one real task on production before any hardening. Cap hardening and review at one day until a buyer has used the product. A second agent family reviews and never builds the same surface; a fork found in review becomes one multiple-choice question within 24 hours. **(recommended, not tested by us)**
- **Estimated saving.** About 7 days on the critical path.

### 2. Give the first payer a named owner from day 0, and send warm outreach the day friends go live

- **What happened.** From day 11 the go-to-market plan ranked friends and the founder's network as channels 1 and 2, with "twenty warm messages" in week 2. None went out. Two questions about the warm list sat at the bottom of an ads status message and were never asked again. The go-to-market session started on day 16.8 and also ran the ads, which absorbed it. Testers wrote one to three messages each, and nobody followed up personally. **(learned the hard way)**
- **Why.** Go-to-market was treated as a phase that starts after product quality. Nobody owned the first payment. Ads were the one channel agents could run alone. Agents asked permission to draft lists, which contacts nobody.
- **Do instead.** Three lanes from day 0, each with an owner session: product, accounts and long-lead items, and revenue (the first payer). The day before friends go live, the revenue owner drafts 20-30 personal notes to owners the founder knows, without asking: email notes as Gmail drafts, Telegram notes ready to send, WhatsApp notes as `wa.me` links the founder taps, and LinkedIn messages never automated. The founder approves the list and texts once, one test send goes out, then the batches. The founder sends a drafted two-line note within an hour of each of the first 20 sign-ups. Every tester is asked for one introduction. The session that owns warm outreach never owns ads. See `08-outreach.md`. **(recommended, not tested by us)**
- **Estimated saving.** First warm conversations about 2 weeks earlier; the first payer likely 1-2 weeks earlier, for about 30 minutes of founder time (an estimate that depends on conversion).

### 3. Decide reuse or new for every account on day 0, and never share money between ventures

- **What happened.** The six incidents above. **(learned the hard way)**
- **Why.** Nobody decided, so whatever login was open got used.
- **Do instead.** On day 0, fill one table with a row per account. If you already have a verified company with verified accounts, reusing the entity skips incorporation and most verifications. Always new per venture: domain, handles, Facebook Page, a brand Google account, a model-provider account with capped keys, a card (a virtual card labelled for the venture works until a company card exists), and every metered workspace (hosting, database, mail, CI budget, outreach, posting), because a shared limit or quota lets one venture take another offline. Before any Meta step, an agent reads every ad account the founder's login can see for unpaid balances. Run competitor studies only in fresh, signed-out accounts. Sharing a Meta portfolio is a founder decision with no default: one policy strike can stop both ventures' ads. See `02-day0-accounts.md`. **(recommended, not tested by us)**
- **Estimated saving.** With reuse, 6-10 calendar days on the Meta, Stripe and Google path; in every case, the 2.5-day block and the risk to another business's customers.

### 4. Put a numeric funnel gate before any ad spend, run by a session that does not own the ads

- **What happened.** On day 19 the ads session reported 30 Start clicks and 0 sign-ups, called it "mostly our own team checking links", and said the founder's test checkout would confirm the rest. That checkout never ran. Ads launched the next night. Three days later the 44-of-45 leak surfaced, then the Instagram in-app block. The fix took about a day: a sign-in subdomain on the brand domain (about an hour, about $10 a month), email-first sign-in, and checkout as sign-up. Tracking tags placed after a `#` never reached the server, and only about 5% of visitors accepted cookies. **(learned the hard way)**
- **Why.** The pre-launch check confirmed that pages rendered; nobody tested what a visitor from an ad sees. There was no numeric bar. The session building the ads explained away its own warning. Measurement came after the channels it was meant to judge.
- **Do instead.** From the first deploy: sign-in on `auth.<yourdomain>`, email-first sign-in or checkout as sign-up, humans-only server-side counting of every step, tracking parameters before any `#`. Before any spend, a session that neither built the sign-up nor runs the ads passes a gate: sign-up finished from a DM link inside the Instagram, Facebook and TikTok in-app browsers on a real phone, with screenshots; at least 20 organic Start clicks with 25% or more reaching an account; the founder's real card checkout and refund seen in Stripe and in the database. If the bar is missed, fix the path. The first paid test is one ad set with 2-3 static ads, capped at about 100 in the checkout currency. At launch: no Meta A/B test object, prepaid funds plus a backup card, and a fixed-rule alarm outside any agent session that fires on 0 impressions for 2 hours while ads show Active. See `10-paid-ads.md`. **(recommended, not tested by us)**
- **Estimated saving.** 4-5 days to a working paid funnel, and most of the £110 turned into readable data.

### 5. Make one operator session the founder's only contact, and never let a question stop the work

- **What happened.** The founder talked to more than 90 sessions, most opened by himself, one per topic. Questions stopped work: Codex ended a turn on a decision card one evening and nothing moved until noon the next day. A usage limit hit at 03:15 and lifted within about an hour, but nothing restarted the work for about 9 more hours. A key request sat unseen inside a status message for over an hour. **(learned the hard way)**
- **Why.** Nobody owned the founder-facing view, so his head was the only place where every session's state came together. Questions had no defaults, nothing resumed work after a limit, and Codex never received his standing rules.
- **Do instead.** One long-lived operator session per venture is the only contact. It opens at most three role sessions (product and release; revenue, from day 0; acquisition, near the funnel gate) plus a second agent family as reviewer. It runs every action that needs the founder's yes inside its own conversation, checks claims live before reporting, and writes state into the repo. Questions go out in two fixed windows a day, never between 22:00 and 08:00, each with a recommendation and, if reversible, a default that applies at a stated time. A one-shot resume is armed at every usage-limit reset. The 09:00 digest leads with one revenue action only the founder can take. See `01-framework.md` and `12-running-agents.md`. **(recommended, not tested by us)**
- **Estimated saving.** About half the founder's daily attention and 1.5-2.5 calendar days.

### 6. Track every long-lead item with an owner and a re-check date, and batch founder steps into sittings ordered by dependency

- **What happened.** The Facebook Page failed an SMS check on day 5 and nobody retried for about 12 days. The Meta sitting on day 9 (the S2 equivalent) got Business Verification but not the Page, the ad account or the system-user token, which came 13 days later. OpenAI business verification never started. A CI billing problem was reported at least 4 times as one bullet in a long status. **(learned the hard way)**
- **Why.** Long-lead items lived in chat with no owner and no automatic re-check.
- **Do instead.** One tracked work item per long-lead item, and a founder-blockers list at the top of every digest. Any outside item idle for 24 hours is a defect. Then sittings split by what each step waits for: S1a on day 0 (needs no name), S1b within 2 hours of the name pick, S2 the day the company number arrives (bank first, then the whole Meta path, then Stripe identity checks), S3a at friends go-live (warm list, one test send, tester access), S3b once Stripe is active (live key, real card payment, phone test). One sitting for everything on day 0 cannot work: Meta and Stripe need the company number, and Google branding needs live policy pages. **(recommended, not tested by us)**
- **Estimated saving.** About 8 days on the Meta path, overlapping with change 2.

### 7. Get buyer evidence before setting positioning and price

- **What happened.** An interview script and an observation protocol existed from day 0; neither was run. The positioning was rewritten about six times ("AI hire", "Hand it the job", three directions after a competitor launch, "Your $1,000+ hire", "AI agents that know the job. With a human touch."), each time after founder frustration, a developer friend's opinion or a competitor's launch. None of the four testers (the founder, a co-founder, a developer friend, a family member) was a target buyer. Effort spread over the UK, the US, a four-country test, a second language and 8 business types. **(learned the hard way)**
- **Why.** Nothing forced buyer evidence, and agents can ship any idea the same day, so building replaced asking.
- **Do instead.** On day 0, write one market, one buyer, one first paid job, the "why us" sentence and a stop rule (no payer after 20 warm conversations and 5 calls, or after the written ad budget, means the offer or the audience changes while the feature list stays as it is). Book 5 buyer calls in week 1 from introductions. Freeze positioning for two weeks; any change cites something a buyer said or did. At least 3 of the first 5 testers are target buyers. See `03-positioning-pricing.md`. **(recommended, not tested by us)**
- **Estimated saving.** Positioning settled by about day 3 instead of still moving on day 25.

### 8. Freeze the offer before the first render, and keep it as configuration

- **What happened.** Paid launched at a $69 early bird. A cost study then produced $49 the next afternoon, plus a $99 tier and a $29 bring-your-own-AI plan that evening. Every ad still said $69, so all channels paused for about an hour. Three days later the trial became 3 days with the card upfront, against the agent's advice, and 16 films, 24 scheduled posts and over 12 Meta ads were re-rendered or rescheduled. The cut came while people left before seeing any price, so price was not the bottleneck. **(learned the hard way)**
- **Why.** Price came from category ranges and feel before cost data or a buyer at checkout. Offer terms were burned into rendered assets.
- **Do instead.** Decide the price once, on day 1-2, from a 1-hour cost test on the real engine that checks a typical user fits the included allowance (from zero, day 2-3, with only a price band before; no page shows a price until the founder accepts it). The offer lives in configuration and one canon offer file that pages, ads and films read; no offer terms inside video. Any price change pauses the ads first, then one batch re-render and a stale-text sweep. Freeze the offer until 10 buyers have reached checkout. Price and trial stay the founder's calls; the agent's duty is to state its numbers in a dated record. **(recommended, not tested by us)**
- **Estimated saving.** 2-3 agent-days of re-renders and a first paid week that can be read.

### 9. Set up the agents' operating system on day 0

- **What happened.** Deploys ran from laptop checkouts through Claude Code's auto-mode safety classifier; one batch went live about 15 hours after merging. CI was down about 7 days on GitHub billing, then failed again on a $0 Actions budget and was disabled. Two deploys from stale checkouts overwrote other work. Commands starting with `!` arrived as chat text at least 6 times, because the founder runs Claude Code in the VS Code panel, where `!` lines do not execute. The global settings grew to 180 allow rules and no deny rules, and five incidents happened under the founder's identity, including a LinkedIn post as him and his Gmail turned into a Workspace account. Codex's rules file was a fraction of Claude's, so the two kept undoing each other's copy fixes. **(learned the hard way)**
- **Why.** Nobody designed deploys, permissions, hand-offs or the rules home on day 0; each was patched under pressure.
- **Do instead.** A bootstrap before any build: byte-identical `AGENTS.md` and `CLAUDE.md` with the founder's rules mirrored into Codex; CI with a funded Actions budget and a deploy job on merge (concurrency lock, stale-checkout guard, content-hash check, `/api/version`); a narrow permission pack with deny rules for deletes and nothing that switches ads on, loaded once and every session restarted; a brand-only browser profile for automated public actions; secret hand-offs through a small validating script, after checking where the founder runs Claude Code (`echo $CLAUDE_CODE_ENTRYPOINT`); the app database off the server volume. See `12-running-agents.md`. **(recommended, not tested by us)**
- **Estimated saving.** About 1 day on the critical path and 8-10 hours of hand-off waits.

### 10. Freeze scope until 3 payers, and budget agent capacity like money

- **What happened.** On day 16 a 13-agent push started on approvals, job chains, zero-downtime releases, connect-any-app, a phone line and more, while the plan's own fact table showed 2 outside users and 0 payments. The agents used up the 5-hour usage window in about 4 hours, and work stalled for about 10. Off the critical path: Meta App Review, a directory listing, 30-40 hours of films, a second language, about 15 landing rounds, seven onboarding versions with no drop-off data. A full app redesign went live for everyone on launch day, untested in in-app browsers. **(learned the hard way)**
- **Why.** Progress was counted in PRs instead of moves along the critical path. There was no written scope, no limit on work in progress and no capacity plan.
- **Do instead.** Write the first-launch scope on day 0: web sign-up plus one messenger channel, one landing, one market, one language, statics plus one video, one ad platform, warm outreach, checkout as sign-up. Every agent track names the milestone it moves; at most 2 run off the critical path until 3 payers. At most 2 landing rounds; no split test under about 1,000 visitors per arm; no redesign in the 48 hours before a paid launch; statics before video (see `09-content-video-anti-slop.md`). Cheaper builder models under one stronger coordinator; state the count and roughly 10M input tokens per agent before any run over 20 agents. App Review, directories, organic social, films and extra languages wait for 3 payers. **(recommended, not tested by us)**
- **Estimated saving.** About 8-10 agent-days, and funnel fixes 2-3 days earlier.

---

## What went well and should be kept

| Keep | Evidence on Givi |
|---|---|
| Framing the brief by multiple-choice questions | A full brief in about 40 minutes, every founder message a decision **(done on Givi)** |
| A sub-agent researching the legal route | UK company plus Stripe recommended in about 30 minutes **(done on Givi)** |
| Choosing models with small real evals | A 7-model eval for about $5, a blind 6-model comparison for about $4, an effort judge that matched the expected answer in 37 of 39 cases **(done on Givi)** |
| Speed once the shape was right | Decision to friends go-live in about 27 hours; the hosting deploy in 15 minutes; self-serve sign-up from a warm pool of ready servers **(done on Givi)** |
| A fast iteration loop | Four reviewed tester sessions turned into about 15 PRs, most live within a day **(done on Givi)** |
| The founder and a family member as testers | Each session found bugs the tests missed **(done on Givi)** |
| Release safety | Rollouts that wait for idle users, rollback tags, a stale-checkout guard, feature flags, canary on the founder's account first **(done on Givi)** |
| The validating secret script | The Meta system-user token in 8 minutes; it caught two Stripe keys pasted together **(done on Givi)** |
| Policy checks before building a channel | Meta's ban on general-purpose AI assistants over WhatsApp found in about 1.5 hours, before any build **(done on Givi)** |
| Fast repair once data existed | Sign-in subdomain in about an hour; email-first sign-in and checkout as sign-up in one day **(done on Givi)** |
| The 20-minute HTML-to-PNG static loop | It produced the winning ad **(done on Givi)** |
| Canon files and one gallery link | Market and go-to-market facts in two files every session read; every live landing on one private link **(done on Givi)** |
| Meta Business Verification in one sitting (S2) | Verified about 19 hours after submission. The Tech Provider choice that opened it is irreversible, so make it on purpose **(done on Givi)** |
| Numbered decision lists | Five decisions answered in about 25 minutes **(done on Givi)** |

---

## If we did it again: the compressed plan

One rule runs the plan: **the launch is done when a stranger has paid without help (M2), and the first paying customer from any source (M1) comes first.** Until 3 people have paid, nothing ships that does not move someone from conversation to payment. The full plan, with gates and run sheets, is in `01-framework.md`. **(recommended, not tested by us)**

### Version A: new accounts (plan 6-8 days to a paid-ready funnel, budget 10)

- **Day 0.** Intake by multiple choice: one market, one buyer, one paid job, a price band, the day-0 asks with a product bar and kill rule, a stop rule. Name screened (domains, company register, same-category products, trademarks, handles). A one-page go-or-no-go check before any money step. Taste intake in 10 minutes. Sitting S1a (no name needed: permissions, CI budget, new hosting, database, mail and model accounts, Stripe test mode, the company filing). Sitting S1b within 2 hours of the name pick (domain, DNS token, brand Google account, mail routing, bots, Facebook Page, handles). The founder lists about 30 owners they know. Agents start the bootstrap, the product spike, a smoke page with a waitlist and no price, and a buyer list.
- **Day 1.** The company registers. Sitting S2 (30-45 minutes): bank application first, then the whole Meta path in one go, Stripe identity checks, other verifications only if planned. Agents: the multi-tenant product, `auth.<yourdomain>`, email-first sign-in, checkout as sign-up in test mode, backups with one restore drill, humans-only counting, landing round 2, warm notes drafted, buyer calls 1-2.
- **Day 2.** Friends go-live. The journey gate runs on production. The founder does one real task. Sitting S3a: approve the warm list, one test send, then the batches. 3-5 testers start, at least 3 of them target buyers.
- **Days 3-4.** Same-day tester fixes; buyer calls 3-5; 3-5 statics; about 5 LinkedIn comments a day drafted for the founder to post; a founder note within an hour of every sign-up. Sitting S3b once Stripe is active: live key, one real card payment and refund, Google branding, the phone test. The funnel gate, run by a session that does not own ads.
- **Days 5-6.** Only if the gate passed, warm notes are out and the founder has recorded a dated override: one capped Meta test (one market, one ad set with 2-3 static ads, 10-15 a day, about 100 in total in the checkout currency), stopped at the cap or at 150 landing visits with 0 sign-ups. Meta will concentrate spend on one static; that ad is the winner signal, and one short video comes only after it. A delivery alarm checks at +2 hours, +24 hours, then daily.
- **Days 7-14.** Ask for the card at the end of each pilot week. Pre-warmed cold mailboxes come online, using only results the product really produced. Target: the first 1-3 paying customers from the warm network (an estimate). If the stop rule triggers, change the offer or the audience and add no features.
- **Weeks 2-4, after 3 payers.** Scale paid on a measured winner; App Review with only the permissions revenue depends on; directory listings; organic social built on finished jobs; video beyond the winning static.

### Version B: reuse an existing verified company and fork a working product (2-3 days)

- **Day 0:** the same brief, offer, taste pick and stop rule; name and domain; a new Page and ad account; a new Stripe product, capped model key, card and metered workspaces; fork and rebrand the product (under a day). S2 merges into S1a and S1b.
- **Day 1:** friends go-live, warm notes sent, statics made, the phone gate run. S3a and S3b merge because Stripe is already active.
- **Days 2-3:** a capped paid test only if the gate passes and the override is recorded.

Givi's 27 hours from decision to friends go-live reused accounts made during the detour. A product built from zero without a fork takes about 3-4.5 days.

### Founder time and risks

About 2-2.75 hours of sittings plus the daily 30 minutes and up to five buyer calls: about 7-8 hours in week 1, then under 30 minutes a day. Givi took roughly 75 hours over 26 days.

- **Agent usage limits** can stall a night. Use cheaper builder models, overflow to Codex, and arm an automatic resume.
- **Meta verification time varies.** If it slips, paid slips; warm outreach does not.
- **After about day 6, infrastructure stops being the bottleneck.** If the first payer does not come, apply the stop rule and change the offer or the audience. Do not start a new build push.

---

## Checklist

- [ ] Read "Where the 26 days went" and noted which buckets your plan removes
- [ ] Marked which of the ten changes apply to your venture
- [ ] Founder's day-0 asks written word for word as acceptance criteria, with a product bar and a kill rule
- [ ] Three lanes named with an owner each: product, accounts and long-lead, revenue
- [ ] Reuse-or-new table filled; money, cards and metered workspaces new for this venture
- [ ] Every long-lead item tracked with an owner and a re-check date
- [ ] Founder sittings scheduled by dependency (S1a, S1b, S2, S3a, S3b)
- [ ] One market, one buyer, one first paid job and a stop rule written down
- [ ] Offer kept as configuration and one canon file
- [ ] CI deploy on merge, narrow permissions and a tested secret hand-off in place before any build
- [ ] Funnel gate defined before any ad money
- [ ] Warm notes drafted the day before friends go live
- [ ] First-launch scope written; at most 2 tracks off the critical path until 3 payers
- [ ] Practices from "What went well" carried into the plan
