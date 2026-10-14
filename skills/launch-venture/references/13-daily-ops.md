# Daily operations: the first 30 days

How to run the business once it is live, with agents doing the work and the founder spending under 30 minutes a day. It covers what may interrupt the founder, the 09:00 digest, founder cards, the morning check, watchdogs that keep running when the laptop sleeps, support and tester loops, the weekly and monthly routines, the metrics and stop rules that drive decisions, the ops page inside the product, and cost capture.

**Done when:** before the first outside user, the founder gets one digest a day at a fixed local hour and instant messages only for money moving, a real sign-up or something broken; uptime, model balance, ad delivery and "did the digest go out" are watched by fixed rules on runners outside the product and outside any agent session; an operator page shows every user, task, cost and piece of feedback; and by day 30 there is a written verdict against the stop rules, with numbers and sample sizes.

> **Facts checked on 13 Oct 2026:** Claude Code routines (cloud scheduled runs) on code.claude.com; Healthchecks.io docs, pricing and Telegram integration; UptimeRobot's free-plan terms (third-party report, see below). Everything else comes from running Givi, an AI business-assistant SaaS, from 17 Sep to 12 Oct 2026. Givi had no paying customers by 12 Oct 2026, so the revenue rules below are what we would run next time; none of them has produced revenue for us yet.

---

## The operating idea

The founder's minutes are the scarcest resource in the business. Agents run in parallel; the founder stays serial. Four rules follow:

1. **Three channels to the founder, no others:** the 09:00 digest, a decisions page with numbered questions and defaults, and instant messages for a short fixed list of events. Plus one line at 18:00.
2. **Silence needs a machine behind it.** Money, uptime, ad delivery and the digest itself are watched by fixed rules on runners that keep going when no agent session is open and the laptop is asleep.
3. **A question never stops the work.** Every reversible question carries a recommendation and a default that applies at a stated time.
4. **Every number states its source and the time it was read**, and one agent session owns each number. On Givi two sessions reported different ad spend for the same day. (learned the hard way)

> **What happened on Givi.** Monitoring was built piecemeal over about 25 days, at a rough 20-25 agent-hours, much of it rework. Vito found the first outage himself. A model-provider balance shared with other projects nearly ran dry unnoticed, and the product was blocked for about 19 hours before the top-up landed. Meta showed ads as "Active" for about two days in total while delivering nothing, and the morning check called £0 spend "probably normal". A scheduled job hung 8 hours on a macOS permission prompt and nobody noticed. Visitor counting was redesigned four or five times on live data, each time after a founder complaint. Next time the same end state should take about one working day of agent time, done before the first tester, and less if you start from a reusable ops kit.

---

## A day at a glance

All times are the founder's local time. "Operator", "revenue owner" and "acquisition owner" are agent sessions with fixed jobs (see `01-framework.md` and `12-running-agents.md`).

| Time | What | Who |
|---|---|---|
| Hourly, all day | Uptime, prepaid balances, ad delivery and billing, every scheduled run's heartbeat, build-machine disk. Silent unless something is wrong | Outside watchers |
| Continuous | Instant messages: money moved, a real sign-up (with source and ad), something broken the founder must fix | The product's ops loop |
| 08:45 | Morning check, 5-10 minutes | Acquisition owner (the operator before paid ads) |
| 09:00 | Digest; dead-man alert if missing by 09:30 | Written by the operator, sent by the ops loop |
| 09:00-09:30 | **The founder's 30 minutes:** read the digest (5), do the one revenue action (10), use the product as a customer (10), answer decisions (5) | Founder |
| 10:00 and 18:00 | Question windows (defaults due, cards answered); support sweep | Operator; revenue owner |
| Within 1 hour of a real sign-up | A two-line personal note drafted for the founder; day-2 check-in if no first result | Revenue owner drafts, founder taps Send |
| Midday | Pipeline sweep: approved notes unsent, replies unanswered, testers silent over 24 hours, sign-ups with no first result | Ops loop |
| 18:00 | "Today so far": visitors by page and source, Start clicks, checkouts, open founder items; reversible defaults applied | Ops loop and operator |
| 20:00 | Anything tomorrow's critical path needs from the founder, as cards. Nothing is asked between 22:00 and 08:00 | Operator |

---

## 1. What may interrupt the founder

Agree this once, on day 0, as a default the founder answers with "yes". (done on Givi, after two corrections)

- **Instant:** money moved (a payment or refund), a real new sign-up, something broken that needs the founder, or a founder step that blocks the critical path right now.
- **Everything else:** the 09:00 digest and the 18:00 line. Never hourly. Givi's funnel pings first went out hourly; Vito said "it distracts me a lot", and visits moved into the digest and the 18:00 line. (learned the hard way)
- **Failed scheduled runs** go to a heartbeat service. The founder hears only if they must act.
- **The alert home:** the venture's own product if it can message the founder, otherwise a dedicated Telegram bot for this venture; never a personal chat or a bot shared with anything else. Write it into the brief and into the instruction file every agent reads. **When the rule changes, grep every run brief, script and scheduled job for the old channel the same day.** Givi's rule changed and scheduled runs kept using the old channel for four more days. (learned the hard way)
- **Recurring job status belongs on a board** (a jobs page in the product); the messenger is for "needs you now". (done on Givi)

---

## 2. The 09:00 digest

**The order is fixed.** It leads with the one revenue action only the founder can take, because selling is the founder's job and the one most likely to slip. On Givi, approving and sending warm notes never reached Vito as a ready batch, and in 26 days nobody sent a warm message. (learned the hard way)

```
<Venture>, <date>

Your one thing today (about 10 min): <the revenue action only you can take, ready to send>

Needs you:
F-12 <card title> (2 min, blocks the paid test)
D4 <decision> I recommend A. Default A at 18:00.

Numbers (source, time read):
Yesterday: <n> visitors, <n> Start clicks, <n> sign-ups, <n> first results, <n> checkouts, <n> paid (warm / ads / cold).
M1, first payer: <yes/no>. M2, first stranger self-serve payer: <yes/no>.
Pipeline: contacted <n>, replied <n>, calls <n>, trials <n>, paid <n>.
Spend: today / week / cap, per channel. Balances: model <n days left>, ads <state>.
Stop rules: <each rule with its count against its limit>.
Support: <n> messages, all answered within the promise: <yes/no>.

Live and checked: <what shipped and was verified live>
Fixed without you: <...>
Not proven yet: <...>
Long-lead: <item> in review since <date>, next check <date>.
Your time yesterday: <minutes>, <questions>.
```

"Your one thing" is a ready-to-send batch of warm notes, replies to yesterday's sign-ups, a drafted comment the founder posts from the clipboard, or a buyer call to book. Never "review this document".

**How to build it** (done on Givi, except where marked):
- A loop inside the product (never a laptop cron) sends it once a day after the digest hour in the operator's timezone (for example `<APP>_DIGEST_HOUR=9`, `<APP>_OPS_TIMEZONE`) and records the send, so a restart never repeats it. A manual trigger such as `POST /api/ops/digest?again=1` lets an agent test it.
- **A dead-man check:** the loop pings an outside heartbeat URL after each send; no ping by 09:30 raises "today's digest did not go out". Otherwise a dead digest loop is silent forever. (recommended, not tested by us)
- **Lead with a plain verdict** such as "too early to tell: day one, about £6 spent", then the numbers. A first-day ads report without one left Vito lost. (learned the hard way)
- **Counts and categories only,** never customers' message text.

---

## 3. Founder cards and the decisions page

Every request to the founder uses one shape. (recommended, not tested by us; built from what failed on Givi)

```
F-07  Meta ad account card hold. About 2 minutes. Blocks: paid test (critical path).
Why: Meta could not place its small test charge on the card, so ads show "Active" but deliver nothing.
The Chrome window "Venture - Meta Billing" is open in front.
1. Click "Try again" on the red notice (outlined in the picture).
2. If it fails, click "Make primary" on the backup card.
Success: the red notice disappears. Reply "done"; I will watch impressions until they move.
Default: none (money). I will ask again at 18:00.
```

- At most 3 clicks, the window already open and named, a picture, what success looks like, one reply word.
- **Reversible questions get a default** that applies at the next 18:00 window or after 24 hours, announced in one line. Money, deleting data, access and secrets, first contact with a person, and anything said in the founder's name never default; they are asked again at the top of every digest until answered.
- **The decisions page** numbers each question (D1, D2...) in customer words, with 2-3 options, a recommendation and a default, so the founder can reply "1. B, 2. as you recommend".
- **Never end a turn on a setting for the founder.** One Givi build ended with "set this environment variable, then deploy"; the deploy waited 3 hours until Vito replied "consider every registration to be a tester and finalize everything". Derive the value and ship. (learned the hard way)
- **Anything the founder must run** is a small local script that reads a secret from the clipboard, validates it, never prints it, and deletes itself (see `12-running-agents.md`).
- **Push notifications** only for the instant list. A key request on Givi sat 66 minutes inside a status message before Vito saw it. (learned the hard way)

**Founder-time ledger.** The operator writes one line a day:

```
14 Oct  minutes requested: 22  questions: 3 (D4, D5, F-07)  pings: 1 (sign-up)  answered late: 0  defaults applied: 1
```

Targets: under 30 minutes and at most 5 questions a day, zero asks between 22:00 and 08:00. Anything above is explained in the next digest, and each week every question a standing rule could have answered becomes a rule. Givi never counted: the estimate afterwards was about 75 hours of founder attention in 26 days. (learned the hard way)

---

## 4. The morning check (08:45, 5-10 minutes)

The acquisition owner runs it once paid ads run, the operator before that. It fixes what it may inside the approved budget, puts everything else into the 09:00 digest, and never messages the founder separately. (done on Givi from 8 Oct, except where marked)

1. **Billing on every ad account and prepaid provider first.** Read each billing page itself (for example with Claude in Chrome's `get_page_text`): a failed card hold shows there and nowhere else. "Active" only means the switches are on, and Meta Ads MCP tools such as `ads_get_errors` do not see card holds.
2. **Delivery per channel since midnight.** Meta Ads MCP: `ads_get_ad_entities`, `ads_get_errors`, `ads_insights_anomaly_signal`, and `ads_account_get_activity_logs` for who changed what. Google: Ads Scripts and automated rules inside the account (no quota), then the Google Ads API once you have a developer token. TikTok: the Marketing API once approved, otherwise Ads Manager in the browser.
   - **No wait-and-see on zero.** An active campaign with nothing spent by mid-morning is a billing problem to check now. On Givi "probably normal for a test's first morning" cost most of a day; the failed card hold took 3 minutes to find once someone looked. (learned the hard way)
3. **Waste:** Google search terms, with negatives added the same morning; the sum of campaign budgets against the monthly cap; any automatically applied recommendation.
4. **The humans-only funnel** by source, page and ad (see "Metrics").
5. **Every stop rule** against its limit.
6. **Fix inside the budget:** pause losing ads, add negatives, shift budget between ad sets inside the approved weekly ceiling. Switching ads on and raising the total are the founder's money decisions (see `10-paid-ads.md`).

Paste-ready prompt:

```
Morning check for the venture in this repository. In order: billing on every ad account
and provider (read each billing page; error tools cannot see card holds); delivery per
channel since midnight (an active campaign at zero by now is a billing problem to check
now); waste (search terms and negatives; Google budget sum against the monthly cap and any
auto-applied change); the humans-only funnel by source, page and ad; progress against every
stop rule. Fix anything inside the approved budget yourself. Put everything else into
today's digest as founder cards or decisions. Do not message the founder separately.
```

---

## 5. Watchdogs that survive a sleeping laptop

A morning check is someone looking. It misses things between looks and stops when the session closes or the laptop sleeps. Watchdogs are fixed rules on durable runners. (learned the hard way: none of Givi's worst incidents was caught by a monitor)

### Fixed rules for alarms, never AI judgement

An alarm is a number against a threshold: "0 impressions for 2 hours while Active", "balance below 3 days of spend", "no digest ping by 09:30". A rule fires the same way every time and costs nothing. Use a model only to explain an alarm after it fires, never to decide whether to raise it. Givi's own assistant judged day-one ads "not well" from a window that left out today, counted review robots as visitors and had no spend data. (learned the hard way)

### Four runners, plus an outside uptime check

| Runner | Runs | Why there |
|---|---|---|
| **(a) The product's own ops loop** | The digest, the 18:00 line, instant messages, the pipeline sweep, watch jobs on the founder's jobs board | Always on, visible where the founder already looks |
| **(b) A scheduled cloud job with read-only tokens** | Model-provider balance, ad delivery and billing, token expiry, review-host health | Independent of the product, the laptop and any session; a job inside the product stops when the balance it runs on is empty |
| **(c) A LaunchAgent on an always-on Mac** | Wakes the operator agent at the question windows (`claude -p` with a fixed prompt), with a timeout, a lock, a heartbeat and a pause file | Work that needs the founder's signed-in browser or local files |
| **(d) Local checks in that same job** | Disk space, test temp folders | A cloud job cannot see the Mac's disk |
| **Outside uptime service and error tracker** (for example Sentry) | `/health` every few minutes; error rate | The product cannot report its own outage |

Also: a daily job reconciles Stripe charges and refunds against the app's records and watches webhook failures, because payment messages depend on your own webhook handler; a digest line confirms CI ran on `main` (a $0 CI budget stopped Givi's CI silently for days); and every runner has a heartbeat and a row in a `runners.md` file with its stop command.

### Tools for runners (checked 13 Oct 2026)

- **Claude Code routines** (research preview): cloud runs that keep going while the laptop is closed, on Pro, Max, Team and Enterprise plans. Create them at `claude.ai/code/routines` or with `/schedule` in the CLI; manage with `/schedule list`, `/schedule update`, `/schedule run`.
  - The minimum interval is one hour.
  - Every connector on your account is included by default, and the routine can use all its tools, writes included, without asking. Remove every connector a watcher does not need.
  - Environment variables are visible to anyone using the environment; on Pro and Max store API keys as network secrets.
  - A green run status means only that the session started and ended; open the run to see whether the check worked.
  - Give watchers read-only tokens only (a Meta `ads_read` system-user token, a balance-read key). Nothing that can spend or write goes into a cloud job.
- **`/loop` and in-session scheduled prompts** die with the session and expire after 7 days; Claude Code Desktop's local scheduled tasks run only while the app is open and the computer is awake. Use them for one-off follow-ups, never for the daily cadence.
- **Healthchecks.io** for heartbeats: each runner pings at start and end; a late or missing ping alerts after a grace time. The free plan monitors 20 jobs, and Telegram is a free integration.
- **An outside uptime pinger** for `/health`. UptimeRobot's free plan checks every 5 minutes and was reported in 2026 to be limited to non-commercial use (third-party report, not verified with UptimeRobot), so budget a paid plan or pick another provider.

### Alert behaviour

Givi spent three review rounds rediscovering standard alerting rules after one warning repeated in the founder's chat. Use these from day 1, or let a heartbeat or uptime service do it. (learned the hard way)
- A new condition alerts at once; a repeat stays silent; a reminder goes out every 6 hours while it is open; absent for 30 minutes counts as new again; recovery sends a message.
- Store alert state in the database after the messenger confirms delivery. If the state cannot be read, alert anyway, rate-limited.
- Alerts carry fixed condition names, never amounts, IDs or customer content.
- A watch blocked by the same cause N runs in a row pauses itself and reports once.

### Jobs that must run on a Mac

- A timeout on every headless run, an hourly catch-up keyed on its output file, and a lock file.
- Never touch the Desktop, Documents or Downloads folders from a scheduled run: macOS shows a permission prompt and the run waits for a click. That is how Givi's run hung for 8 hours. (learned the hard way)
- Set `PATH` explicitly in every launchd job; `node` and `vercel` were not found otherwise. Diagnose with `launchctl list`, `plutil -p <plist>` and `pmset -g log | grep -E 'Sleep|Wake'`. (learned the hard way)
- **No unattended, late or catch-up run acts in public as the founder.** On Givi an agent replayed a missed run by hand on the strength of a general "Go!" given the day before; founder posts were then banned outright. Never let an agent post or comment as the founder: LinkedIn's User Agreement forbids bots and automated posting. Agents draft; the founder posts. A late run re-reads the current rules and skips every public action. (learned the hard way)

### Day-0 money watchers

- **Separate money and keys per venture:** its own model-provider account or organisation, a capped key for agents' own tests, auto top-up. Givi's cost filter counted only the venture's keys, which also removed the only view of the shared balance. Keep two numbers: "what this venture costs" (filtered) and "will we run out" (the whole balance). When the founder says yes to a top-up, open the billing page in their browser at once: on Givi it reached Vito 4.5 hours later. (learned the hard way)
- **Ad billing watcher,** hourly with the read-only token: `account_status`, any campaign Active with 0 impressions for 2 hours, billing notices. Before launch, confirm Meta's small test hold succeeded on the card. On Givi prepaid funds alone did not clear a failed hold; "Try again" on the billing notice did, within minutes. (learned the hard way; the automated watcher is recommended, not tested by us)

---

## 6. Support and tester feedback loops

### Support

- **Sweep at 10:00 and 18:00:** the shared mailbox and in-app messages, every reply the same day against a reply-time promise in a support file. (recommended, not tested by us)
- Refunds inside your published window happen at once; refunds outside it, discounts and free access go to the founder as cards with amounts.
- Failed payments beyond Stripe's retries get a short note with the billing-portal link; cancellation reasons are logged; invoice requests get a Stripe invoice. Themes go into the weekly review.

### A personal note to each of the first 20 sign-ups

Within an hour of each of the first 20 real sign-ups, the revenue owner drafts a two-line note from the founder: thanks, one question ("what is the one job you want off your plate this week?"), and a 15-minute call link. It goes into the founder's email drafts (for example with the Gmail connector's `create_draft`) or as a ready Telegram text; the founder taps Send, about a minute each. On day 2, a short check-in if there is no first result yet. (recommended, not tested by us)

Why: on Givi the two outside testers wrote 1-3 messages each and stopped, the first stranger typed "hello" and left, and a tester's account went to sleep when its trial ended. Automated lifecycle emails alone brought none of them back. (learned the hard way)

### Tester sessions, reviewed the same day

- **Order:** the tester's own words, point by point; the read-only database timeline (counts and metadata); one plan with numbered decisions; one release; then re-read the tester's messages right before releasing. Close every comment in a per-comment status table. On Givi a release went out before the tester's one-to-one comments were worked through. (learned the hard way)
- Cheap fixes ship the same day. Strategy doubts from people who are not buyers get tested with real buyers before anything changes.
- Ask every tester for one introduction, and for a quote (first name and role, with permission) when they praise a result.

### Feedback capture inside the product

- A quiet thumbs control under each finished answer, a note box only after a tap, one follow-up after a thumbs-down, and a `/feedback` command. (done on Givi)
- A nightly cheap-model scan of the last 48 hours flags complaint, praise, confusion, stuck or wish; on Givi it cost under one cent a day for ten testers. (done on Givi)
- **Privacy rule for agents:** counts and metadata by default; message text only for a session the customer reported, never copied into memory, work items or the digest. The privacy page says support may read a reported session. (recommended; Givi's testers had agreed to full reading, which is too broad for strangers)

### Hand-check each early lead

For each early sign-up, read the event timeline read-only (source, campaign, ad, device, sign-in steps, billing) and open the landing page in the same in-app browser user agent. Report "real or not, card or not, where they stopped". Most Meta traffic opens inside the Instagram or Facebook in-app browser, where Google sign-in is blocked; Givi's first paid-traffic sign-up failed exactly there. (done on Givi)

---

## 7. The ops page inside the product

One page behind sign-in, inside the product, reading live data. (done on Givi)

**`/ops`, the operator page:**
- The operator is derived automatically (the owner of the first account), plus an optional list of operator emails. Signed-out visitors are redirected to sign-in and back; everyone else gets the normal not-found page.
- Users (plan, last seen, channels, connected apps, tasks, thumbs, spend, share of allowance, approvals waiting); money (today, 7 days, month to date by source, a projection); the latest 100 tasks with metadata; feedback; events; warnings sent; a free-access panel.
- JSON twins and manual triggers for agents, such as `GET /api/ops/summary` and `POST /api/ops/collect`.

**`/ops/analytics`, funnel and ads:**
- Tabs for Overview, Ads, Landings and App; a Refresh button (the founder asked for exactly this); Today, Yesterday, 7 days, 30 days, Since launch and custom dates.
- Spend per channel from long-lived tokens. Read each Meta ad's real destination link from its creative and fetch deleted ads by ID (they still carry spend). Never join ads to tracking tags by ad name: on Givi that matched nothing, and every Meta ad showed no spend. (learned the hard way)
- Labels such as "too early to judge" and "no recent traffic", a "who's counted" box, and a "what to look at" line (the best ad by sign-in clicks per visitor, with at least 20 visitors).
- Never estimate spend and never add up currencies. Use `is None`, never a truthiness check, so a real zero shows as zero.

**Report tools in your own assistant** (if your product is one): name in the tool description every phrasing it should catch, test three phrasings, and confirm from the agent log that the tool was called. On Givi the tool existed but was not chosen until its description was rewritten. (learned the hard way)

---

## 8. Cost capture

Know the real cost per customer from the providers, from the first deploy. (done on Givi, except where marked)

1. **Record usage:** one row per user message (channel, model, timings, outcome, tools, tokens, cost) and one event row per gated action (sign-up, login, connection, approval, scheduled run, run failed, checkout, sign-in screen shown). Events never hold the user's words; deleting an account deletes its rows.
2. **Book every cost source:** user messages, scheduled jobs, sub-tasks and first turns. Givi booked only user-started work at first, and its estimate ran about 19% below the provider's bill. (learned the hard way)
3. **An hourly collector** reads per-key usage from the provider's management API on the venture's own account, adds per-call costs (search, connectors) and a flat hosting estimate per customer until real usage can be queried.
4. **Show three numbers apart:** what the app reserved, what the provider says, the settled invoice. Reconcile daily and alert once when the gap passes 10%. (reconciliation recommended, not tested by us)
5. **Once-only warnings with tunable thresholds:** a task over $0.50, a day over $10, a customer at 50% of their allowance, a feature key at 80% of its cap, 80% of customer slots used, a balance below a few days of spend. Give each spending feature its own capped key.
6. **A cost register** of every recurring charge (provider, plan, card, renewal date), checked monthly against card statements. (recommended, not tested by us)

---

## 9. Metrics and decision rules

### Definitions

- **Visitors are people.** A page download does not count; an inline script sends one beacon after a scroll, tap, keypress, mouse move or 15 seconds open, once per browser. Exclude the team (a cookie set when an operator opens the app, the operator's IP for 7 days after last use, links tagged `utm_source=qa`), automated browsers and ad-platform review robots. On Givi, "visitors" in a week with no marketing were cloud scanners, and review robots showed up as dozens of "Meta visitors" before any ad delivered. (learned the hard way)
- **Read the client IP from the host's real header** through one shared function. On Railway that is `X-Real-IP`; the last `X-Forwarded-For` hop is Railway's own proxy, which made every Givi visitor share one IP. (learned the hard way)
- **Write the measurement spec before the first visitor.** Counts stored before a fix stay wrong forever, and stop rules then run on polluted numbers.
- **Paid** means a first charge above zero not refunded within the money-back window; free access, test payments and refunds are excluded; warm, ad and cold payers are counted separately.
- **Milestones:** M0, a stranger can go from a link to an account, a first result and card checkout, proven on a phone in the in-app browsers with one real card payment and refund; M1, the first paying customer from any source; M2, the first stranger who pays without help.
- **Activation,** reported next to "paid" per cohort: a first result within 24 hours, an app connected, back on day 2, a second result without help.
- **Funnel steps** per page, language, source and ad: real visit, Start click, sign-in screen shown, sign-in redirect started, sign-up, first result, checkout, card, charged, refunded. **Log the sign-in steps from day 1.** On Givi 44 of 45 people who clicked Start left at sign-in, and the step tracking that would have shown where came only afterwards. (learned the hard way)

### Decision rules

Money figures are in the venture's checkout currency. Givi ran several of these after the fact or not at all.

| Trigger | Threshold | Action |
|---|---|---|
| Funnel gate before any ad spend | Fewer than 20 organic Start clicks, under 25% reaching an account, any in-app sign-up failure, or no real card payment and refund | No spend; fix the path. The bar is never lowered |
| Capped paid test, before 3 payers | The cap reached, or 150 landing visits with 0 sign-ups | Stop; judge on sign-ups per landing visit, with the sample size |
| Whole paid programme, after 3 payers | 400 paid visitors and no trial | Pause every channel |
| One channel, after 3 payers | 500 spent and no trial | Stop that channel |
| Ad delivery | 0 impressions for 2 hours while Active, or nothing spent by mid-morning | Billing check at once; "Try again" or switch the default card |
| Ad creative, day 1 | Link click-through under 0.5% | Pause that ad, keep at least one running, and swap in a replacement static |
| Day-7 paid verdict | Cost per trial per channel and market | Move money to the cheapest |
| Paid clicks against counted visitors | An unexplained gap (Givi once saw about 3 paid clicks per counted visitor) | Check in-app load time, bots, the consent banner |
| Activation | Under half of trials get a first result within 24 hours | Ads to minimum; fix onboarding |
| Split test | Fewer than about 1,000 visitors per arm reachable in 14 days | No split test; change one version at a time |
| Offer change | Fewer than 10 buyers have reached checkout | Frozen; a change needs buyer evidence and the number it will be judged by |
| Stop rule (offer and audience) | No payer after 20 warm conversations plus 5 buyer calls, or after the written ad-spend limit | Change the offer or the audience. Do not add features |
| Scope and scale | Fewer than 3 payers | No new channels, languages, films or platform reviews; no paid scale-up |
| Public launch (Product Hunt and similar) | Fewer than 3 strangers have paid | Not yet |
| Claims | A capability with 0 real uses in production | Not shown in any page, ad or video |
| Tester silent, or an approved note unsent | More than 24 hours | Personal nudge; send the note |
| Uptime and errors | 2 failed minutes; errors above threshold for 10 minutes | Alert; roll back if a release caused it |
| Long-lead item or founder blocker | No movement for 24 hours | Top of every digest until cleared |

Two more lessons from Givi:
- **Expect low cookie consent:** about 5% of UK visitors allowed ad cookies. Optimise on your own server-side counts and the platforms' landing-page views, never on pixel conversions. (learned the hard way)
- **Verify tracking with each platform's test-event mode** (Meta's test event code, TikTok's test events, Google's conversion diagnostics). Givi's check put a fake sign-up into three production ad dashboards before any ad ran. (learned the hard way)

---

## 10. The weekly review (Monday, 20-30 founder minutes)

The operator prepares one private page; it replaces that day's 30-minute slot. (recommended, not tested by us)

1. **Numbers against every rule above, with sample sizes.** "2 sign-ups from 31 visitors" is a fact; "6% conversion" from 31 visitors is not a finding.
2. **M1 and M2:** reached or not, and on which day.
3. **Pipeline per line** (warm, ads, cold, social): contacted, replied, call, trial, paid. Cost per trial per channel and market. What each stop rule says.
4. **The experiment log:** what changed and the number it was judged by.
5. **The founder-time ledger,** with the questions a rule could have answered and the proposed rules.
6. **Rules review:** superseded rules removed; run briefs grepped for outdated channels and offer wording.
7. **Hygiene:** token expiries and scopes, balances and auto top-ups, CI billing, platform quotas, disk and test temp folders (zero left after a run), the runners list.
8. **Support and cancellation themes,** and reply times against the promise.
9. **1-2 changes decided,** each with the number it will be judged by; the offer untouched unless a written trigger fired. End with numbered decisions, each with a recommendation and a default.

Also weekly: a read-only review of code, security and a live walkthrough as a brand-new user ("would a stranger pay?"); a competitor launch watch; agent capacity for next week. Fortnightly: 3-5 booked buyer conversations.

A prompt the founder can paste any time:

```
Is this venture working? Answer from the numbers only: M1 and M2, pipeline counts,
cost per trial, what the stop rule says, and the one change you recommend for next
week with the number it will be judged by. Three short paragraphs, no technical terms.
```

---

## 11. Monthly tasks (and at day 30)

| What | Who |
|---|---|
| **Day-30 verdict:** continue, change the offer, change the audience, or stop, with numbers and sample sizes | Operator drafts; founder decides |
| **Secrets sitting** (about 10 minutes): rotate keys logged as exposed; renew expiring tokens (a 60-day Meta management token at day 50) | Operator prepares one-step routes; founder rotates |
| **Cost review:** the cost register against card statements; provider cost per customer against what the app booked; unit economics per plan | Operator and product owner |
| **Compliance check:** policy pages match the product; vendors and data regions current; every claim has real production use behind it | Operator with a reviewer agent |
| **Statutory dates** for a new company (see `14-company-legal.md`) | Operator; accountant files |
| **Restore drill:** restore one backup into an isolated database and compare counts and hashes. "Backups on" does not prove restore; Givi never restore-tested its live app | Product owner |
| **Teardown:** finished worktrees, stale scheduled jobs, broad permission rules, retired services, OAuth clients and keys | Operator; founder approves deletes |
| **Platform reviews and directories,** once 3 payers exist (see `11-platform-approvals.md`) | Agent |

If the verdict is stop, wind down row by row from the cost register, runners list and access list: refund or cancel subscriptions, tell users in one plain note, delete customer data as the privacy page promises, close ad accounts and recover prepaid balances, remove scheduled jobs, revoke keys, decide the domain. Nothing irreversible happens before the founder's yes for each refund and delete. (recommended, not tested by us)

---

## 12. The first 30 days, by week

| Week | Focus | Founder time |
|---|---|---|
| 1 | Setup sittings (S1a, S1b, S2, S3a, S3b); friends using the product; warm network; same-day fixes; 5 buyer calls; the funnel gate; a capped paid test (one ad set, 2-3 statics, about 100 in the checkout currency) only after the gate passes, the warm notes are out and the founder has given a dated yes | Sittings, 5 calls, 30 minutes a day |
| 2 | First payers from the warm network (estimate: day 7-14); cold email with proof of real results; one introduction asked of every tester | 30 minutes a day |
| 3 | Scale paid only on a measured winner and only after 3 payers; public launch steps | One listing slot |
| 4 | Day-30 verdict; tear down anything not earning; write down what to reuse next time | Weekly review |

---

## Gotchas

| Symptom | Cause | Fix |
|---|---|---|
| A chronic warning mutes later alerts | The incident closes only on a full all-clear | 30 minutes absent counts as new again |
| The ops page "doesn't open" | Signed-out visitors got a 404 by design | Redirect to sign-in and back; list every team email from the start |
| Pixel "not firing" in the agent's browser | The team cookie and bot detection exclude it on purpose | Check in a clean Playwright context |
| "Records wiped" but storage remains | The deletion path skipped per-customer volumes | The post-deletion check covers volumes too |
| A cloud watcher could have written to accounts | Every connector is included in a routine by default | Remove connectors it does not need; read-only tokens only |

---

## Checklist

**Day 0 and the setup sittings (S1a, S1b, S2, S3a, S3b)**
- [ ] Alert policy agreed and written into the brief and the agents' instruction file; alert home chosen
- [ ] The venture's own model-provider account, a capped key for agents' tests, auto top-up on
- [ ] Ad accounts with two payment methods; Meta's small test hold confirmed before launch
- [ ] CI funded above $0; read-only Meta system-user token created, any management token kept off the server

**Before the first outside user**
- [ ] `/health` with an outside uptime check, outage and recovery tested; an error tracker
- [ ] Digest dead-man heartbeat: alert if no ping by 09:30
- [ ] Daily backups on every volume and one restore drill
- [ ] Usage and event tables; hourly cost collector; every cost source booked; daily reconciliation
- [ ] `/ops` with the operator derived automatically and a signed-out redirect
- [ ] 09:00 digest loop, restart-proof, leading with the founder's one revenue action
- [ ] Once-only money, capacity and balance warnings; alert behaviour tested
- [ ] Thumbs feedback and a nightly scan; privacy page says support may read a reported session
- [ ] Stripe webhook failures watched; daily charges and refunds reconciled

**Before the first paid visitor**
- [ ] Measurement spec written; beacon counting; team, test, bot and review-robot exclusions; one client-IP function
- [ ] Funnel rows per page, language, source and ad; sign-in steps logged
- [ ] Pixels only after consent, verified with test-event modes
- [ ] Instant sign-up and payment messages name the page and the ad; 18:00 line live
- [ ] `/ops/analytics` with real spend per channel and creative-link matching
- [ ] Ad delivery and billing watcher on a cloud job with a read-only token and a heartbeat

**Every day**
- [ ] Morning check at 08:45; zero spend by mid-morning checked at once
- [ ] Digest at 09:00 with source and time on every number
- [ ] Support answered the same day
- [ ] A personal note within an hour for each of the first 20 sign-ups; day-2 check-in
- [ ] Tester sessions reviewed the same day, comment by comment
- [ ] Founder-time ledger line written

**Every week**
- [ ] Weekly review with sample sizes, M1 and M2, pipeline, cost per trial, stop rules, the ledger and rule updates
- [ ] Every runner ran on time; blocked jobs paused and reported once
- [ ] Briefs and scripts grepped for outdated channels and offer wording

**Every month and at day 30**
- [ ] Secrets sitting done; expiring tokens renewed
- [ ] Cost register reconciled; unit economics re-measured
- [ ] Compliance check done; restore drill repeated; stale automations removed
- [ ] Day-30 verdict written: continue, change the offer, change the audience, or stop
