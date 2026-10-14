# The launch-and-run framework

The plan for launching and running a new online business with AI coding agents: one operator session as the founder's only contact, a fixed budget of founder time, phases with "done when" gates, a decision freeze calendar, the default stack, the cadence, decision rules and paste-ready prompts. The other reference files hold the step-by-step recipes.

**Done when:** the venture has a paid-ready funnel (M0), a first paying customer (M1), a first paying stranger (M2) and a written day-30 verdict, and the founder spends under 30 minutes a day after week 1.

Evidence: written after the Givi launch (`00-the-story.md`). Parts Givi ran are tagged **(done on Givi)**, parts it got wrong first **(learned the hard way)**. The structure as a whole is **(recommended, not tested by us)**.

---

## 1. How to use this file

**Founder.** Paste the kickoff prompt (14.1) into one new Claude Code session with your idea under it. That session, the operator, is the only one you talk to. You give about 10 minutes of intake and three prepared sittings in week 1 (two of them in halves), then under 30 minutes a day plus booked buyer calls.

**Agent acting as operator.**
1. Read this file, then `00-the-story.md`. Open other reference files only when a phase points to them.
2. First turn: send the intake (14.2), start the read-only account-standing check (section 8), launch the research fan-out (P1).
3. Write `decisions/brief.md` from the answers. Start no build agent until it holds the founder's day-0 asks, the product bar and the kill rule.
4. Prepare sitting S1a, run the go-or-no-go check (P-1) before any money step, prepare S1b for the moment the name is picked, then follow section 7 and the cadence in section 11.

---

## 2. Done lines and targets

- **M0, paid-ready funnel.** A stranger goes from a link to an account, a first real result and a card checkout on the venture's own domain, sign-in and payment. Proven on a real phone inside the Instagram, Facebook and TikTok in-app browsers, and with one real card payment and refund.
- **M1, first paying customer from any source.** Proves the offer. Most likely from warm outreach, around day 7-14 (estimate).
- **M2, first paying stranger, self-serve.** Proves the funnel. The launch's done line.
- Until M1: no paid scale-up, no new channels, no new features. Until 3 payers: the scope freeze holds.

| Measure | Givi (actual) | Target |
|---|---|---|
| Paid-ready funnel (M0) | day 25.9 | day 6-8 with new accounts (budget 10); day 2-3 reusing a verified company and a working product |
| First payer (M1) | none by day 25; warm outreach never sent | day 7-14 (estimate), warm notes on friends go-live day |
| Founder attention | about 75 hours over 26 days | about 7-8 hours in week 1, then under 30 minutes a day |

---

## 3. Operating model

### 3.1 Roles

| Role | Owns | Never does |
|---|---|---|
| **Founder** (a co-founder may approve taste and warm lists, never money) | Identity, money, taste and offer, first contact, the product bar, the stop rule, anything said in their name | Engineering choices, relaying between sessions, running untested commands |
| **Operator**: one long-lived Claude Code session per venture | The founder's queue, digest and decisions; accounts and long-lead items; sittings; the critical path; briefing role sessions; checking claims live; **running every action that needs the founder's yes, in its own conversation** | Building product; ending a turn on a question; acting on a relayed yes |
| **Product and release owner** | Architecture, builder sub-agents, merges, CI deploys, flags, ops kit | Running ads; changing the offer |
| **Revenue owner**, from day 0 | Buyer calls, testers, warm notes, pipeline, cold email, landing copy, **the funnel gate** | Touching ads |
| **Acquisition owner**, from about day 3 | Statics and video, ad builds, the morning check, every ad number | Switching ads on or raising a budget |
| **Builders**: sub-agents on a cheaper model | One PR each, test first, own worktree, port and temp folder | Deploying, holding secrets, asking the founder |
| **Reviewer**: a second agent family (`codex exec --sandbox read-only`) | Review of risky PRs and plans; overflow builds | Building what it reviews |
| **Watchers**: uptime service, scheduled cloud job, product duties | Uptime, model balance, ad delivery, "did the digest go out" | Running inside an agent session or on the product they watch |

Cap: the operator plus at most three role sessions, plus the reviewer. On Givi the founder talked to more than 90 sessions. **(learned the hard way)**

### 3.2 Session rules

- **A relayed yes is information, never consent.** The session that runs a money, send, secret or switch-on action gets the founder's yes in its own conversation; role sessions hand the operator one ready command. **(learned the hard way)**
- **One builder per surface.** A second agent family only reviews; a fork found in review becomes one question to the founder within 24 hours.
- **One change, one PR, one worktree** from fresh `origin/main`, failing test first.
- **Deploys only from CI on merge,** under a concurrency lock, with a stale-checkout guard, a content-hash check and `/api/version`. The emergency route is the same job run against a tag (`gh workflow run deploy.yml -f ref=<tag>`), tested on day 0. **(learned the hard way)**
- **Never wait, never poll.** Message the peer or queue a founder card. At every usage-limit message, arm a one-shot resume at the reset time; for a weekly limit, move queued tracks to Codex.
- **Capacity is money.** Cheaper builder models under one stronger coordinator; before any run over 20 agents, state the count and roughly 10M input tokens per agent. **(learned the hard way)**: an 88-agent review burned about 240M tokens.
- **One owner per shared resource:** deploys (CI), the visible browser window, the ad account (ID pinned in `ACCESS.md`), the landing, the warm list, the offer file.

### 3.3 Sources of truth

Each fact has one home in the venture repo. Sessions and memory are evidence, never authority.

```
AGENTS.md == CLAUDE.md       scope, lanes, owners, standing rules (byte-identical)
.claude/settings.json        venture-scoped allow AND deny rules
decisions/brief.md           day-0 asks verbatim, product bar, kill rule, stop rule
decisions/DECISIONS.md       every decision with class, date, founder's words
bd/GTM.md, bd/MARKET.md      buyer, paid job, channels, paid gate; dated market facts
bd/offer.md                  THE offer: price, currency, trial, refund, allowance
bd/TASTE.md, bd/BANS.md      approved references and banned patterns
bd/metrics.md                definitions (paid, visitor) and decision rules
product/capabilities.md      what a customer sees today: live / beta / not built
legal/identity.md            legal facts every console form copies
operations/ACCESS.md         account, owning login, workspace ID, blast radius (no secrets)
operations/CRITICAL-PATH.md  dependencies and durations (the only authority for timing)
operations/cost-register.md  every recurring charge with cap and alarm
operations/runners.md        every scheduled job with its stop command
```

Outside the repo: one tracked work item per long-lead item and per revenue line, a founder-blockers list, and a secrets register (names and locations, never values). Any tracker works; the pattern is one item with an owner and a re-check date.

### 3.4 Decision classes

| Class | Examples | Rule |
|---|---|---|
| A. Irreversible or identity-bound | company filing, ad-account currency, Meta Tech Provider choice, directory-listing owner, anything published in the founder's name, first contact, deletes, money | The founder's own numbered yes, asked alone, never defaulted, given in the session that runs it |
| B. Expensive to change | product shape, market and buyer, name, offer, taste, sign-in domain | Frozen on the calendar in section 6; a change needs an evidence memo |
| C. Cheap to change | copy inside the frozen offer, engineering, internal drafts and lists, thresholds | Agents decide, log under "Choices made while building", keep going |

---

## 4. The founder-time contract

### 4.1 Slots

| Slot | When | Minutes | For |
|---|---|---|---|
| Intake | day 0 | 10-15 | Reply "defaults except ..." to one numbered message |
| S1a | day 0, after agent prep | 30-40 | No name needed: permission pack, debts, CI budget, hosting, database, mail, model account, Stripe test mode, money numbers, company filing after the go |
| S1b | within 2 hours of the name pick | 30-40 | Domain, DNS token, brand Google account, mail routing, bots, Facebook Page, handles |
| S2 | the day the company number arrives | 30-45 | Bank first, then the whole Meta path, Stripe identity checks, other verifications if planned |
| S3a | friends go-live, usually day 2 | 15-20 | Approve warm list and texts, one test send, sign-ins in the agents' visible browser window, tester access |
| S3b | once Stripe is active, usually day 3-4 | 15-20 | Live Stripe key, one real card payment and refund, Google branding, real-phone in-app sign-up test |
| Taste picks | day 0-2 | 2 x 10 | One pick per landing round |
| Daily | after S1b | under 30 | 5 digest, 10 the one revenue action, 10 using the product, 5 decisions |
| Buyer calls | week 1, then fortnightly | 20-30 each | Booked, never chat |
| Weekly review | Monday | 20-30 | Numbers against the rules, decisions, rules review |

On the reuse track S2 merges into S1a and S1b, and S3a and S3b run together. Week 1 totals about 7-8 hours including five buyer calls. The halves exist because the name arrives late on day 0, Meta and Stripe need the company number, Stripe activation needs a payout bank account, and Google branding needs live policy pages. **(learned the hard way)**

### 4.2 Channels, windows and cards

Three channels only: the **09:00 digest** (14.3) **(done on Givi)**, which should lead with one revenue action only the founder can take (Givi's did not); a **decisions page** answerable from a phone (numbered items, 2-3 options, a recommendation, a default and its time; class A shows "answer in chat"); and a **push notification** only for money moved, a real sign-up, breakage the founder must fix, or a founder step blocking the critical path. Plus one line at 18:00. Questions surface at 10:00 and 18:00; by 20:00 the operator asks for what tomorrow needs; nothing between 22:00 and 08:00. All in the founder's time zone.

Every request is a founder card:

```
F-07  Meta ad account card hold. About 2 minutes. Blocks: paid test (critical path).
Why: Meta could not place its small test charge, so ads show "Active" but deliver nothing.
The Chrome window "Venture - Meta Billing" is in front.
1. Click "Try again" on the red notice (outlined in the picture).
2. If it fails, click "Make primary" on the backup card.
Success: the red notice disappears. Reply "done"; I will watch impressions until they move.
Default: none (money). I will re-ask at 18:00.
```

### 4.3 Preflight before anything reaches the founder

- It really needs the founder, and the exact command already ran with a dummy value; any key is tested with the provider before storing.
- The surface was detected with `echo $CLAUDE_CODE_ENTRYPOINT`. A `!` command runs only in terminal Claude Code; in the VS Code panel it arrives as chat text, so hand over a double-click script. **(learned the hard way)**
- The window is in front and named, the founder's standing on the platform was checked, and the target account is this venture's per `ACCESS.md`. Afterwards the agent verifies the outcome itself.

### 4.4 What never defaults, and what agents decide alone

**Ask, no default:** any new spend, ad budgets, switching ads on; irreversible data loss; rotating credentials, adding admins, moving secrets into a new environment; switching a money or sign-in feature on for all users; first contact with a person; anything said in the founder's name; identity steps (inside a sitting); the offer and positioning (once, then frozen); a departure from the day-0 asks.

**Decide and log:** engineering, deploys, merges, rollbacks, flags, test accounts, internal drafts and lists (drafting contacts nobody), research, copy fixes inside the frozen offer, pausing losing ads inside the budget.

**Pre-clears the founder writes once, dated:** keys created for this venture may move between its own stores, and money-capable keys are always new per venture; the CI emergency job may deploy a tagged release; read-only watcher tokens may live in a scheduled cloud job; refunds inside the published window are automatic; after one approved test send, outreach batches need no new ask; inside the weekly ad ceiling, agents pause, shift budget and add negatives.

---

## 5. Standing rules

1. **The founder's day-0 words are acceptance criteria.** Any departure needs a one-line OK.
2. **Start every clock in the first hour it can start.** An outside step idle for 24 hours is a defect.
3. **Agents run in parallel; the founder stays serial.**
4. **Reuse the entity, never the money.**
5. **Selling starts on friends go-live day.**
6. **Gate with numbers before spending.**
7. **The offer is configuration, frozen on the calendar.**
8. **A question never stops the work.**
9. **One second-model review on every PR that touches money, sign-in, connections, deletion or the runtime.**
10. **Scope is frozen until 3 payers:** at most 2 tracks off the critical path, each naming the milestone it moves.
11. **Silence needs a machine heartbeat:** money, uptime, ad delivery and the digest are watched by fixed rules outside the product and any agent session.

---

## 6. Decision freeze calendar

| # | Decision | Freeze by | Givi cost of not freezing |
|---|---|---|---|
| F1 | Day-0 asks, product bar, kill rule | day 0, before any build | about 7.5 days on the wrong product |
| F2 | Runtime and data: one product line, managed Postgres, no app database on a volume | day 1 | two outages, weeks of deploys waiting for idle users |
| F3 | One market, one buyer, one first paid job, "why us", stop rule | end of day 1 | about 6 repositionings |
| F4 | Name, screened (domains, company register, same-category products, trademarks in each launch market, handles); then the logo | name end of day 0 or 1; logo end of day 1 | the logo came 14 days after the name |
| F5 | Offer: price, currency, trial, refund window, allowance, VAT stance | day 1-2 after a 1-hour cost test (day 2-3 from zero); no public price before | 5 setups in 12 days, mass re-renders |
| F6 | Taste and bans | day 0, before any design agent | about 15 landing rounds |
| F7 | Channels per market, after a 30-minute policy check each | day 0 | a WhatsApp detour |
| F8 | Address map: landing on the apex, app host, `auth.` subdomain, redirect URIs | first deploy | 44 of 45 Start clicks lost at an unbranded consent screen |
| F9 | Ad-account currency (permanent), VAT stance, merchant of record | before any ad account | mixed currencies across platforms |
| F10 | First-launch scope, paid gate, work-in-progress limit | day 0 | about 35 PRs in the leakiest week |

**Changing a frozen decision:** a one-page memo (new value, evidence with sample size, the number it will be judged by, every surface affected); the founder's numbered yes; for an offer or claim change, pause every paid channel first; switch site and terms, then checkout, live check, new ads, bios, scheduled posts; sweep for old strings; tell every owning session the same turn; existing subscribers keep their price until a stated date, with notice in advance.

---

## 7. Phases and gates

Three lanes run in parallel from day 0: **product** (product owner), **accounts and long-lead** (operator), **revenue** (revenue owner). The longest chain is the product lane: about 5 days to a gated funnel, then about a day to a paid test. Plan 6-8 days to M0 with new accounts and budget 10. If Meta verification slips, paid slips; warm outreach does not.

**P-1. Go or no-go (day 0, about 2 hours, before any money step).** Done when the founder's one-line "go" is logged after a one-page check: research so far, the cheapest substitute, a pre-mortem ("day 30, nobody paid: three likely reasons"), and the smallest version that could get one payer.

**P0. Day 0 bootstrap and long-lead sprint.** Done when `brief.md` is complete; `AGENTS.md` equals `CLAUDE.md`; G0 passed; `ACCESS.md` and the reuse-or-new table exist; S1a and S1b are ticked by the agent's own checks; the company filing is in; every long-lead item is running or tracked. See `02-day0-accounts.md`, `12-running-agents.md`.

**P1. Positioning, naming, pricing (day 0-1; offer day 1-2).** Done when F3, F4 and F5 are frozen; the offer lives only in configuration and `offer.md`; "paid" is defined in code; 3-5 buyer calls are booked. Method: 5-6 cheaper research sub-agents in one message (including competitor ads from the Meta Ad Library), the wedge challenged by a second model, one scripted name screen, a cost test on 5-10 real jobs. See `03-positioning-pricing.md`.

**P2. Landing (smoke page day 0-1; frozen after 2 rounds).** Done when one landing in one language for one market has every claim traced to `capabilities.md` or `offer.md`, policy pages, humans-only server-side counting, tracking parameters before any `#`, and pixels behind an equal-weight consent bar, with every button clicked signed out. See `04-landing-pages.md`.

**P3. Product spike and friends go-live (spike live day 2).** Done when G3 and G4 pass on production, the founder has done one real task, backups run with one restore drill, a prompt-injection set passed if the product reads outside content and can act, and anonymous model calls have daily caps. Package what the founder already uses or fork a working product; pick the default model by a small blind eval **(done on Givi)**. See `05-product-and-infra.md`.

**P4. Payments (test mode day 1; real card in S3b).** Done when Stripe Checkout works as the sign-up with the trial mode F5 chose, the webhook includes `charge.refunded`, the portal works, prices come from one idempotent setup function in both modes, and the agent has seen the founder's real card payment and refund in Stripe and the database. Ads stay off until then. See `06-payments-stripe.md`.

**P5. Channels (policy check day 0).** Done when a thin web surface plus one messenger channel pass a scripted acceptance on every release, after a 30-minute policy check per channel and market **(done on Givi)**, and marketing profiles are brand-owned with 2FA and a second admin. See `07-channels-integrations.md`.

**P6. First customers (from friends go-live).** Done when 20-30 warm notes went out on go-live day, 3-5 testers are live (at least 3 target buyers), each was asked for one introduction, 5 buyer calls were held, each of the first 20 sign-ups got a founder note within an hour, and M1 is reached or the stop rule applied. Notes are drafted the day before without asking: Gmail drafts, Telegram messages the founder sends to existing contacts (10-15 a day), WhatsApp as `wa.me` links the founder taps, LinkedIn messages never automated. Cold email from week 2. See `08-outreach.md`.

**P7. Funnel gate and capped paid test (gate earliest day 4-5).** Done when the gate passed and a capped test ran with a verdict, or the gate failed and the path is being fixed. Paid ads are never the route to the first payer. One capped test may run before M1 only when G5 has passed, the warm notes are out, and the founder has recorded a dated override: one market, one ad set with 2-3 static ads, 10-15 a day, about 100 in total in the checkout currency. Meta will concentrate spend on one of the statics, and that ad is the winner signal. One short video comes only after a static wins. The test stops at the cap or at 150 landing visits with 0 sign-ups. Scaling waits for 3 payers. No Meta A/B test object at launch: it delays delivery to the next midnight **(learned the hard way)**. See `10-paid-ads.md`, `09-content-video-anti-slop.md`.

**P8. Public launch (after 3 payers).** Done when each platform review, directory listing and review site is submitted or skipped by a written decision and M2 is reached. See `11-platform-approvals.md`.

**P9. First 30 days.** Done when the cadence ran daily, founder blockers cleared within 24 hours, founder time averaged under 30 minutes a day, and a day-30 verdict (continue, change the offer, change the audience, or stop) is written with numbers and sample sizes. See `13-daily-ops.md`.

### Gate ladder

Each gate has a pass bar and a runner who is not the author. A failed gate is fixed, never explained away.

| Gate | When | Pass bar | Runner |
|---|---|---|---|
| G0 Bootstrap | day 0 | no-op release shipped by CI and by the emergency route; every MCP read works; allow and deny rules loaded; secret scripts dry-run | Operator |
| G1-G2 Every PR and release | each merge and deploy | failing test first; full suite; second-model review where rule 9 needs it; rollback tag; canary on the founder's account, then on for all | Author, reviewer, product owner |
| G3 Value check | day 1-2 | founder uses it freely for 15 minutes; an outside model answers "can a target customer reach the value today?" | Reviewer |
| G4 Friends go-live | before any outside link | sign-up, three real tasks, a test payment, cancel, isolation between accounts, caps, run as a stranger with evidence; restore drill done | Product owner |
| G5 Funnel gate | before any ad money | sign-up from a DM link inside the Instagram, Facebook and TikTok in-app browsers on a real phone; branded consent screen; at least 20 organic Start clicks with 25% reaching an account; the real card payment and refund seen | Revenue owner |
| G6 Offer and claims | before any render or ad | offer frozen; one currency; claims only from the proven-live list | Acquisition owner plus reviewer |
| G7 Public identity | first item of each new kind under the founder's name or the brand | founder's yes on the item shown; acting identity checked before every write | Channel owner |
| G8 Paid launch | first ad money | G5 and G6 passed; warm notes out; override recorded; spending limit read back; delivery alarm fired once | Acquisition owner plus operator |

---

## 8. Day 0 accounts and the sittings

**Reuse or new.** If you already have a verified company with verified Meta, Stripe and Google Ads accounts, run the venture as a new brand under it: that skips incorporation and most verifications (about 2-3 days to M0). Sharing a Meta portfolio is a founder decision with no default, because one policy strike can stop both ventures' ads. Always new: domain, handles, Facebook Page, brand Google account, a card (a virtual card labelled for the venture until a company card exists), a model-provider account with capped keys, and every metered workspace (hosting, database, mail, CI budget, outreach, posting). **(learned the hard way)**: an old billing problem on another ad account under the same login blocked the new Page for 2.5 days.

**Agent prep before S1a (about 3-4 agent-hours from scratch):** a read-only standing check of every ad account, billing page and plan the founder's login can see; `ACCESS.md`; a field sheet of every value the founder will type; one validating script per expected secret, dry-run; every console open in run-sheet order in a dedicated venture browser profile. In S2 the whole Meta path goes in one go: Business Verification, an ad account in the checkout currency, two payment methods, one small forced charge, a spending limit, a second admin, domain verification and the system-user tokens. Anything that fails becomes a tracked item before the sitting ends. Console paths: `02-day0-accounts.md`.

**Secrets recipe (done on Givi: the Meta token in 8 minutes).** The agent writes a double-click script on the Desktop that reads the clipboard, checks prefix, length and that it holds one value, tests it against the provider's API, stores it (Keychain, or `railway variable set NAME --stdin --skip-deploys`), clears the clipboard, prints only "accepted" and deletes itself. It is dry-run with a dummy value first. The agent confirms by name and length only. A key pasted into chat anyway is used, logged as exposed, and rotated later.

---

## 9. Long-lead items

| Item | Typical wait seen | Start when |
|---|---|---|
| UK company | about 24 hours, £100 online; each director verifies identity through GOV.UK One Login first (GOV.UK, checked 13 Oct 2026) | S1a, after the go |
| Company bank account | days; Stripe activation needs it as the payout account | S2 |
| GitHub Actions budget | 2 minutes; Givi's CI was down about 7 days on a $0 budget | S1a |
| Facebook Page | minutes, but an SMS check can block it (Givi: about 12 idle days) | S1b, on the phone |
| Meta Business Verification | about 19 hours | S2 |
| Meta ad account and payment | minutes with a clean login | S2, after the standing check |
| Meta card pre-authorisation | can fail silently behind "Active" | one small charge before launch day |
| Stripe activation | hours to days after company and bank | identity in S2, live key in S3b |
| D-U-N-S and Google advertiser verification | days | S2, only if Google ads are planned |
| OpenAI business verification | no published timeline | S2, only if a ChatGPT listing is planned |
| Meta App Review, directory listings | App Review: 20-25 agent-hours to prepare, then weeks; directory listings: days to submit, then an open-ended review | after 3 payers |
| Cold mailboxes | fresh: 2-4 weeks of warm-up (Instantly's guidance); pre-warmed: usable that week | order day 1 if the intake said yes |
| Buyer-call recruiting | days | day 0 |

---

## 10. Default stack and fallbacks

| Need | Default | Fallback |
|---|---|---|
| Domain and DNS | Cloudflare Registrar, DNS with a zone-scoped token **(done on Givi)** | dashboard via browser |
| Brand mailbox | for a short test, a free brand Google account with Cloudflare Email Routing forwarding hello@ to it **(done on Givi; the brand account came late, learned the hard way)** | Google Workspace as soon as you answer customers by email, because Gmail's "Send as" through another provider's SMTP is being retired (`02-day0-accounts.md`) |
| Transactional mail | Resend, used as the auth provider's SMTP **(done on Givi)** | the auth provider's default sender |
| Code, CI, deploys | GitHub, Actions with a funded budget, deploy job on merge **(learned the hard way)** | a local test gate |
| Hosting | Railway, a new workspace per venture, live environment named `production` **(done on Givi)** | Fly at larger tenant counts |
| Database and auth | Supabase Postgres and Auth on `auth.<domain>`, email-first sign-in **(learned the hard way)** | Railway Postgres; magic link |
| Payments | Stripe Checkout as the sign-up, prices by lookup key, Stripe CLI | a merchant of record (Stripe Managed Payments or Paddle) for VAT |
| Models | the venture's own OpenRouter account, capped per-customer keys, defaults by blind eval **(done on Givi)** | direct provider keys |
| Integrations | Composio, white-labelled, behind an approval gate **(done on Givi)** | own OAuth apps for the top 1-2 vendors |
| Chat channel | Telegram plus a thin web surface; Slack when buyers ask **(done on Givi)** | web chat |
| Outside watchers | UptimeRobot or Healthchecks.io, a scheduled cloud job with read-only tokens, Sentry | a cron service on the host |
| Analytics | humans-only server-side funnel, consent-gated pixels, PostHog where drop-off needs watching | server logs |
| Paid social | Meta ads MCP for builds and reads; Graph API with a system-user token for billing and pauses | Ads Manager via the Claude in Chrome extension |
| Paid search | Google Ads Scripts and rules, then the Google Ads API | the Google Ads UI |
| Outreach | Gmail drafts; Instantly with pre-warmed mailboxes in a new workspace; Clay for lists | sends from the phone |
| Organic posting (after 3 payers) | Welder on a profile holding only this venture's networks **(done on Givi)** | platform UIs |
| Creative | HTML-to-PNG statics first, 2-3 of them in the first test's one ad set; Remotion for one short video after a static wins **(done on Givi)** | Canva for direction |
| Design QA | gstack `/design-review`, `/qa` and `browse` | Playwright |
| Secrets | 1Password CLI or the macOS Keychain, with validating scripts **(done on Givi)** | a pasted key, logged as exposed |

Browser order: API, MCP or CLI first; then headless gstack `browse`; then the Claude in Chrome extension for consoles that need the founder's login; the founder only for cards, passwords, 2FA, CAPTCHAs and ID. See `toolbox.md`.

---

## 11. Running cadence

| When (founder's time) | What | Who |
|---|---|---|
| hourly | uptime, model balance, ad delivery, billing, heartbeat of every scheduled job | watchers |
| continuous | pings for money, sign-ups, breakage; releases with canary on the founder, then on for all | product |
| 08:45 | morning check (14.4) | acquisition owner (operator before paid) |
| 09:00 | digest (14.3); the founder's 30 minutes follow | operator |
| 10:00, 18:00 | question windows (defaults apply at 18:00); support sweep, every reply the same day | operator; revenue owner |
| within 1 hour of a sign-up | drafted founder note; day-2 check-in if no first job | revenue owner |
| same day | every tester session reviewed and fixed | product owner |
| midday | pipeline sweep: unsent notes, unanswered replies, silent testers | product duty |
| 18:00 | one line: visitors, Start clicks, checkouts, open founder items | product |
| 20:00, 22:00 | cards for tomorrow; an overnight queue that needs nothing from the founder | operator |

The operator's windows run from one scheduled job on an always-on computer (a LaunchAgent or cron starting `claude -p` with that window's prompt, such as 14.4), with a timeout, a lock, a heartbeat and a pause file. Timers inside a session die with it. **(learned the hard way)**: a scheduled run hung 8 hours on a macOS permission prompt.

**Weekly:** Monday review (14.5) and the ads day-7 verdict; a midweek read-only review trio (code, security, a walkthrough as a brand-new customer); a rules review (each correction written once and mirrored to every agent family); hygiene (token expiry, balances, CI runs, disk, broad allow rules). Fortnightly, 3-5 buyer conversations.

**Monthly and day 30:** the day-30 verdict; unit economics re-measured; costs against card statements; a restore drill; a secrets sitting; teardown of stale jobs and allow rules.

---

## 12. Metrics and decision rules

Every number states its source and time; one session owns each. Visitors are people (interaction or 15 seconds; team, bots and link previews excluded). Paid is a first charge above zero not refunded within the window; warm, ads and cold payers are counted separately.

| Trigger | Threshold | Action |
|---|---|---|
| Kill rule | slower than about 60 seconds per typical task, or "weaker than my own" | switch the approach within 24 hours |
| G5 funnel gate | under 20 organic Start clicks, under 25% reaching an account, any in-app failure, no real card run | no spend; fix the path; never lower the bar |
| Ad delivery | 0 impressions for 2 hours while Active | billing check now |
| Ad creative, day 1 | link click-through under 0.5% | pause that ad |
| Capped test (before 3 payers) | cap reached, or 150 landing visits and 0 sign-ups | stop; verdict on sign-ups per visit with sample size |
| Paid after 3 payers | 400 paid visitors and no trial; 500 spent on a channel and no trial | pause all; stop that channel |
| Split test | under about 1,000 visitors per arm in 14 days | no split; change sequentially |
| Offer change | under 10 buyers reached checkout | frozen |
| Any price, trial or claim change | any | pause paid first; re-render from config; sweep |
| Cold email | replies under 1%, complaints over 0.3%, bounces over 3% | stop that mailbox |
| Stop rule | no payer after 20 warm conversations plus 5 calls, or after the written ad limit | change the offer or the audience; add no features |
| Payers | 3 | scope freeze lifts; scale paid on a measured winner |
| Claims | a capability with 0 real uses | not shown anywhere public |
| Founder load | over 30 minutes or 5 questions a day; any ask 22:00-08:00 | explain in the digest; write a rule or pre-clear |

---

## 13. Do-not list (drawn from the Givi launch)

1. Build a different shape from the one asked for, or let two agent families build the same surface.
2. Harden or review at scale before the founder has used the product.
3. Set a price before a cost test, or render offer terms into video or images.
4. Reposition on frustration, a power-user tester or a competitor headline.
5. Claim what customers cannot see today, invent reviews, add "Example" labels or mix currencies.
6. Let the ads session own warm outreach, or launch paid into a funnel already seen failing.
7. Count visitors without filtering bots, put tracking after `#`, or split-test on hundreds of visitors.
8. Make films before a static has won, or post volume on new social accounts.
9. Use whatever login is open, or share a balance, card, quota or login with another venture.
10. Run Google Workspace setup or recovery wizards on a personal account, or study competitors while signed in.
11. End a turn on a question or "waiting", or hand the founder an untested command.
12. Add broad allow rules, pre-allow tools that move money, deploy from a laptop, or leave CI unfunded.
13. Run watchdogs inside agent sessions or judge alarms with AI instead of fixed rules.
14. Let an agent post, comment or message as the founder on LinkedIn or WhatsApp, even with them watching; LinkedIn's User Agreement forbids bots and automated posting.

---

## 14. Paste-ready prompts

### 14.1 Kickoff (the founder pastes this into one new Claude Code session)

```
Start a new venture using the launch-venture skill. Read references/01-framework.md and references/00-the-story.md first and follow the framework's section 1 for agents. You are the operator and my only contact for this venture. Send me the intake as one message, run the account-standing check and the market research while I answer, and prepare my first sitting. Do not start building until the brief holds my asks, the product bar and the kill rule. My idea, in my own words, is below.
```

### 14.2 Founder intake (the agent fills the angle brackets and sends it as one message)

```
Setting up <working name>. Reply "defaults" or change any line by number. About 10 minutes. Line 2 has no default.

0. Profile: <product type>, <B2B or B2C>, seller <country>, launch market <one>, your time zone <zone>.
1. Your words, kept as acceptance criteria: "<your words>". Product bar: <draft>. Kill rule: <draft>.
2. Track (please answer yourself): A) a new brand under your existing verified company and accounts, with its own card, AI key, domain and Page; or B) everything new. Risk of A: one ad-policy strike on a shared Meta portfolio can stop both businesses' ads. I recommend <A or B, one reason>.
3. Name: do you already have one? If not, three screened finalists by tonight.
4. Market and currency: <one>, <one>. Ad accounts use the same currency, permanently.
5. Buyer: <kind of business, size, place, language>. First paid job: <recommendation>.
6. Month-one target: <N> paying customers at about <price band>. The exact offer comes from a cost test on day 1-2 and then stays frozen; no page shows a price before your yes.
7. Stop rule: no payer after 20 warm conversations and 5 calls means we change the offer or the audience.
8. Paid before the first payer: one capped test of about 100 <currency> (one ad set, 2-3 static ads), only after sign-up works on a phone and warm notes are out, and only with your dated yes.
9. Nothing posts as you. LinkedIn comments on buyers' posts are drafted and copied to your clipboard; you post them.
10. Alerts go to <where>; instant only for money, a real sign-up or breakage.
11. Money: weekly ceiling = ? Monthly ad cap per platform = ? Pre-warmed cold-email mailboxes at about <one-off> plus <monthly> (vendor pricing page, today): yes or no?
12. Pre-clears you write once, dated: <the list in section 4.4, prepared as exact lines>.
13. Warm list: about 30 owners you know who fit the buyer, by tomorrow evening. Second admin: <name>. Accountant and bank: <names>.
14. Sittings: S1a today at <time>; S1b within 2 hours of your name pick; S2 the day the company number arrives; S3a at friends go-live; S3b once Stripe is active.
15. Before anything is bought, a one-page go-or-no-go check. Reply "go" or "no-go".
```

### 14.3 Daily digest (09:00; the agent fills it)

```
<Venture>, <date>

Your one thing today (about 10 min): <the revenue action only you can take, ready to send>

Needs you:
F-12 <...> (2 min, blocks the paid test)
D4 <...> I recommend A. Default A at 18:00.

Numbers (source, time):
Yesterday: <n> visitors, <n> Start clicks, <n> sign-ups, <n> first jobs, <n> checkouts, <n> paid (warm / ads / cold).
M1 <yes/no>, M2 <yes/no>. Pipeline: contacted <n>, replied <n>, calls <n>, trials <n>, paid <n>.
Spend: <today / week / cap> per channel. Model balance: <days left>.
Stop rule: warm conversations <n>/20, calls <n>/5. Capped test: <spend>/<cap>, visits <n>/150. G5 organic Start clicks <n>/20.

Live and checked: <...>   Fixed without you: <...>   Not proven yet: <...>
Long-lead: <item> in review since <date>, next check <date>.
Your time yesterday: <minutes>, <questions>.
```

### 14.4 Morning check (08:45; paste as is)

```
Run the morning check for the venture in this repository, following references/01-framework.md section 11 and references/13-daily-ops.md. In order: billing on every ad account and model provider (read the billing pages themselves; "Active" is not proof of delivery); delivery per channel since midnight (an active campaign at zero by now is a billing problem to check now); waste (search terms, negatives, Google budgets summed against the monthly cap); the humans-only funnel by source, page and ad; progress against every stop rule. Fix anything inside the approved budget yourself. Put everything else into today's digest as founder cards or numbered decisions. Do not message the founder separately.
```

### 14.5 Weekly review (Monday; paste as is)

```
Prepare the weekly review for the venture in this repository, following references/01-framework.md sections 11 and 12. One page: numbers against every decision rule with sample sizes; M1 and M2; pipeline counts per line; cost per trial per channel; what the stop rule says. My time this week, with the questions a rule or pre-clear could have answered and the pre-clears you propose. Rules review, capacity, hygiene and the list of scheduled jobs. End with numbered decisions, each with a recommendation and a default. Keep it readable in 20 minutes.
```

---

## Checklist

- [ ] One operator session is the founder's only contact; intake answered, including the track question
- [ ] `brief.md` holds the day-0 asks verbatim, product bar, kill rule and stop rule
- [ ] Go-or-no-go "go" logged before any money step
- [ ] Reuse-or-new table committed; card, model account and metered workspaces new for this venture
- [ ] G0 passed; every long-lead item tracked with an owner and a re-check date
- [ ] Sittings S1a, S1b, S2, S3a, S3b run from prepared run sheets
- [ ] Offer frozen and kept only in configuration and `offer.md`
- [ ] Spike live by day 2; G3 and G4 passed; warm notes sent on go-live day
- [ ] Real card payment and refund seen; G5 passed before any ad money
- [ ] First paid test, if any: one ad set with 2-3 statics, capped at about 100 in the checkout currency; video only after a static wins
- [ ] Brand mail moved to Google Workspace before anyone answers customers by email
- [ ] Digest, pings and outside watchers running, each with a heartbeat
- [ ] Founder under 30 minutes and 5 questions a day after week 1
- [ ] Scope frozen until 3 payers; day-30 verdict written
