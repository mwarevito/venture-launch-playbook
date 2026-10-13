# 08 Outreach: getting the first customers

Agents find the people, draft every message, keep one pipeline and chase anything stuck. The founder approves every first contact and anything said in their name, and sends personal messages and comments themselves. The order: testers and the founder's own network first, then LinkedIn comments on buyers' posts, then cold email from separate domains. Paid ads come after all three (see `10-paid-ads.md`).

**Done when:** 20-30 personal notes went out on the day friends could first use the product, with a sent log; every tester was asked for one introduction; the founder posts about 5 agent-drafted LinkedIn comments a day; if cold email is in the plan, it runs from lookalike domains with warmed mailboxes, verified leads and a legal footer, and its first approved batch has gone; one pipeline sheet counts contacted, replied, call, trial and paid every day; the stop rule is read every week.

> **Read this first: outreach was Givi's biggest miss.** In 26 days the team sent 0 warm messages and 0 cold emails. Two notes to testers were drafted about a week after friends could use the product and never sent; the wider warm list was never drafted. The cold-email setup (roughly $130 for an Instantly plan, two domains and pre-warmed mailboxes) was never put to Vito as its own question, so it died without anyone deciding to stop it. All 5 conversations with real target buyers came from comments on buyers' posts made from Vito's personal LinkedIn by an unattended agent run (section 3.1 explains why that part must not be copied), and none had become a call or a payment by the end of the 26 days. Givi had no paying customers on 12 Oct 2026. So most of this guide is **(recommended, not tested by us)**, built from documentation checked on 13 Oct 2026, and the lessons are **(learned the hard way)**.

Evidence tags: **(done on Givi)** we did it and it worked; **(learned the hard way)** we got it wrong first; **(recommended, not tested by us)** from current docs or common practice.

---

## 1. Set up before the first message

### 1.1 One owner for outreach, never the ads session (learned the hard way)

On Givi the session that owned go-to-market also ran the ads. Its plan said "testers and warm contacts go first"; in practice it made hundreds of browser and ad-platform calls and a handful of calls to the email and lead tools. About £110 of ads bought 1 sign-up, and the warm line never started. Ads are the one channel an agent can run alone, so they swallow any session that also owns them.

- One agent session owns outreach (the **revenue owner**): tester follow-up, the warm list, LinkedIn drafts, replies, cold email and the pipeline sheet. Another session owns ads.
- Each line (warm, LinkedIn, cold, sign-up follow-up) gets a work-item file with one outcome and a due date, updated the day its status changes.
- Internal steps need no permission: drafting a list or notes contacts nobody. Givi's warm line stalled on two questions of exactly this kind, placed at the end of a long ads update and never asked again. A blocking question goes numbered at the top of the founder's next message, with a recommendation.

### 1.2 Write down what "paid" means (done on Givi)

In `bd/metrics.md`: a paying customer is a first charge above zero, not refunded inside the money-back window. Test payments, free access and refunds do not count. Count warm, LinkedIn, cold and ads separately. Then grep the billing code for the statuses it treats as paid; Givi's counted `trialing`, which would have counted $0 trials as customers.

### 1.3 One pipeline sheet (recommended, not tested by us)

Givi's leads lived in a CSV on one laptop no other session could see. Use one Google Sheet, written and read through the Google Workspace MCP (`create_spreadsheet`, `append_table_rows`, `read_sheet_values`), with one tab per line and these columns: first_seen, line, name (first name and role only), link, buyer (y/n against the written buyer), stage, last_contact, next_action, owner, approved (y/n for this exact text), sent_at (filled only after it really went).

Record only publicly listed business contact details and what the person wrote to you; note the lawful basis (legitimate interest); delete a row when someone says no (their address stays on the suppression list, 4.12) or after 90 days of silence; never paste the sheet into the repo.

### 1.4 Ask the cold-email money question on day 0 (learned the hard way)

Fresh mailboxes need 2-4 weeks of warm-up; pre-warmed ones can send in the week they are bought. That makes cold email a long-lead item. Ask once, on day 0, as its own numbered line with figures read from the pricing page that day:

> "Cold email: one-off $X plus $Y a month (Instantly plan, 2 sending domains, 4 pre-warmed mailboxes, prices read today). If yes, I order tomorrow and the first batch goes in week 2. Yes or no?"

On Givi this was never asked on its own, and no session raised cold email again after 4 Oct.

---

## 2. Warm first (recommended, not tested by us)

The cheapest first customer already trusts the founder. Givi ranked "friends" and "the founder's network of owners" as channels 1 and 2, then sent nothing to either.

### 2.1 Timing

Draft the notes the day before the friends go-live check passes and send them the day it passes. Givi's check passed on 27 Sep; two notes to testers were drafted on 3 Oct and never sent, and the list of the founder's own contacts was never drafted: about two weeks lost on the channel most likely to produce a first payment **(learned the hard way)**.

### 2.2 The list comes from the founder (about 15 minutes, day 1)

- The founder dictates 20-30 people they know who run a business that fits the buyer; a co-founder adds theirs. Agents do not browse the founder's contacts, inbox or messenger to build it.
- Leave out clients of the founder's other businesses and anyone they would not want to pitch.
- The revenue owner adds a sheet row per person with one line of context and the channel the founder uses with them, tagged buyer or non-buyer. On Givi none of the four reviewed testers was a target buyer (Vito, a co-founder, a developer friend, a family member), so the product got tuned to them **(learned the hard way)**.

### 2.3 The note: personal, short, no price (learned the hard way)

Givi's offer went through five setups and three price points in 12 days; every draft, video and email that carried it went stale each time. Warm notes carry no price and no deadline; the offer comes in a later follow-up.

```
Hi <first name>,

I've built <product> for <buyer in plain words>: <one sentence on the job it takes off their plate>.
Because <specific thing you know about them>, I think it could <concrete result> for you.

Would you try it this week? It's free while I'm testing. Tell me what breaks,
and if it's useful, who else should see it.

<link?utm_source=warm&utm_content=<initials>>
<Founder first name>
```

One real detail per person, 60-90 words, no "hope you're well", no feature list, one link, a question answerable in one line.

### 2.4 Channels: Gmail drafts; Telegram and WhatsApp sent by the founder

| Channel | Agent | Founder |
|---|---|---|
| Email | creates one draft per person in the founder's own Gmail with the Gmail connector's `create_draft` | opens Drafts, reads, taps Send |
| WhatsApp | puts a click-to-chat link in the sheet: `https://wa.me/<number, digits only, with country code>?text=<URL-encoded note>` | taps it on their phone, checks, sends |
| Telegram | puts the note and an `https://t.me/<username>` link in the sheet; on a Mac can copy the next note to the clipboard with `pbcopy` | opens the chat, pastes, sends |

These are the founder's personal accounts, so agents draft and the founder sends. Messaging apps restrict accounts that send many similar messages quickly, especially to non-contacts (general platform behaviour, not tested on Givi), and a bot sending from the founder's account is the founder speaking without having read the words.

### 2.5 The go-live sitting (S3a, about 15-20 minutes)

1. The revenue owner posts the whole list with every text in one numbered message.
2. The founder answers "ok" or edits by number ("7: drop the second sentence"). Approving takes the 15-20 minutes that sitting S3a budgets.
3. The founder sends the Gmail drafts, then works down the WhatsApp and Telegram rows.
4. The agent fills `sent_at` and checks the Gmail sent folder. If the list is long, spread messenger sends over 2-3 days at 10-15 a day.

### 2.6 Ask every tester for one introduction

Each tester gets a personal note from the founder: thanks, the one thing the product did for them (from their own session), and one ask, "Who is one owner who should try this?", with a referral link (`?utm_source=ref&utm_content=<initials>`). Introductions become warm rows, with the introducer in the context line.

### 2.7 A note to each of the first 20 sign-ups within an hour

Givi's two outside testers wrote 1-3 messages each and stopped, and the first stranger typed "hello" and left. Automated lifecycle emails brought none back, and nobody wrote to them personally **(learned the hard way)**. For each of the first 20 real sign-ups, the revenue owner drafts two lines from the founder within the hour (thanks; "what is the one job you want off your plate this week?"; a 15-minute call link on the brand calendar) as a Gmail draft or messenger text. No first finished job by day 2: one more short check-in. About 1 minute of the founder's time each.

### 2.8 The daily sweep

A job on a real scheduler (a cron in the product's ops loop, a GitHub Actions schedule, a cloud routine), never a timer inside an agent chat that dies with the session. At midday it reads the sheet and sends the founder one line, in the one alert channel they chose: replies unanswered for 4+ working hours; approved notes unsent after 24 hours; testers silent for 24+ hours; sign-ups with no first job; any line idle for 2 days. On Givi two approved notes sat unsent for more than a day, and alerts once went to a channel Vito had ruled out **(learned the hard way)**.

Every reply gets an answer the same day, ending with a question about their business or a call link.

---

## 3. LinkedIn without automation

### 3.1 Why this channel (done on Givi; the automation was learned the hard way)

All 5 of Givi's conversations with real target buyers (among them a virtual-assistant firm's founder and an e-commerce growth agency's owner) started as replies to comments posted from Vito's personal LinkedIn on those buyers' own posts. The brand's Instagram, X and TikTok activity produced replies from non-buyers and almost no site visits.

The mistake: an unattended agent run posted those comments under his name through a headless browser. On its first day it published a comment on a stranger's hiring post from his personal profile. Later an agent, catching up a missed run by hand on the strength of a general "Go!", published a LinkedIn post as him that he had not approved, and he banned founder posts for good. LinkedIn's User Agreement (section 8.2, effective 3 Nov 2025, checked 13 Oct 2026) forbids "bots or other unauthorized automated methods to ... send or redirect messages, create, comment on, like, share, or re-share posts", and bans scraping tools. The channel worked; the automation put the founder's personal account at risk.

Rule: never automate posting, comments or messages as the founder. Agents research and draft; the founder posts every comment, note and message themselves, watched or not.

### 3.2 Finding posts (agent, about 20 minutes a day) (recommended, not tested by us)

Keep agent traffic on LinkedIn itself near zero, since automated reading counts as scraping. Instead:
- a search engine restricted to public posts, for example `site:linkedin.com/posts "agency owner" (hiring OR onboarding)`, past week;
- 30-50 target buyers the founder follows; the founder pastes 5-10 post links from their feed each morning (2 minutes);
- communities where buyers discuss the job your product does.

Keep a post only if the author matches the buyer, it is under 48 hours old, and you have something useful to add. Never the same author twice in 7 days.

### 3.3 Drafting and posting (recommended, not tested by us)

About 5 comments a day, each 2-4 sentences in the founder's voice, adding one specific useful thing (a method, a number from experience, a sharp question about their case). No compliments, no restating the post, no hashtags, emojis or links, and no product mention unless the post asks for a tool. Each goes in the sheet's LinkedIn tab with the post link and why the author is a buyer.

For each row the agent opens the post in the founder's browser and copies the comment to their clipboard; the founder reads it, edits it if they want, and posts it. About 5-10 minutes a day. Givi moved to this route only after the incidents above, so it has not been run end to end.

### 3.4 Replies are leads

Every reply under the founder's comments goes on the sheet the same day; the agent drafts an answer (up to 3 exchanges, ending with a question about their business) and the founder posts it. Anyone who asks about the product, describes the problem it solves, or messages the founder is a hot lead: within hours the founder gets who, what, the link and a ready note. On Givi more than a dozen replies sat unread for up to 3 days, and a daily reply cap then held back half of them **(learned the hard way)**. Cap new comments, never replies.

Connection notes and messages: drafted by the agent, sent by the founder. On Givi Vito told the agent to send two notes to hot leads itself; it was recorded as "waiting on Vito" and they stayed unsent **(learned the hard way)**. The right answer is one line ("LinkedIn bans automated messages; both notes are on your clipboard"), and the sweep flags them if still unsent.

---

## 4. Cold email with Instantly, step by step

Givi never sent a cold email; all of this is **(recommended, not tested by us)**, checked against Instantly's documentation on 13 Oct 2026. Re-read the pricing page and the tool list on the day you start.

### 4.1 What exists today (checked 13 Oct 2026)

- **API v2:** base URL `https://api.instantly.ai/api/v2`, bearer-token auth, keys created at Settings > Integrations > API Keys with selectable scopes (such as `campaigns:create`, `leads:read`). Rate limit per workspace across all keys: 100 requests a second, 6,000 a minute; listing emails is limited to 20 a minute. Docs at developer.instantly.ai; an index for agents at developer.instantly.ai/llms.txt.
- **Official MCP server** at `https://mcp.instantly.ai/mcp`, exposing the whole API v2 as about 200 tools generated from the API spec. Header authentication is recommended; a key in the URL path works but can end up in logs.
- **CLI:** `npm install -g @instantlyai/cli`, `instantly login`; reads `INSTANTLY_API_KEY`; includes a local MCP server (`instantly mcp`).

| Item (instantly.ai/pricing, 13 Oct 2026) | Price | Notes |
|---|---|---|
| Outreach Growth | $47/month | 5,000 emails, 1,000 contacts; API yes; Unibox preview-only; no webhooks |
| Outreach Hypergrowth | $97/month | 125,000 emails, 25,000 contacts; Unibox replies, custom reply labels, webhooks |
| Free trial | 14 days, no card | 250 contacts, 1,000 emails |
| Instantly Credits | separate, from $9/month for 150 | SuperSearch and AI; work-email lookup about 1.5 credits a row |
| Domain | $15/year | pre-warmed or done-for-you |
| Pre-warmed Google mailbox | $10/month | "ready to send from day one", per Instantly |
| Done-for-you Google mailbox | $5/month | needs warm-up |

Worked example: 2 domains plus 4 pre-warmed mailboxes plus Hypergrowth is about $30 a year up front and $137 a month; on Growth about $87 a month, but replies are answered outside the Unibox. Givi's "about $130" mixed a first month of the plan, the domains and the mailboxes into one number, so give the founder the one-off and the monthly figure separately.

### 4.2 Step 1: workspace, key, MCP (agent 20 minutes, founder 5)

1. A new Instantly workspace for this venture, with its own billing. If the machine has an Instantly connection for another business, writes can land in the wrong workspace: call `workspace_get` and check the name before any write.
2. An API key with only the scopes the agent needs; leave out ordering (`dfy_email_account_orders:create`) if purchases should stay with the founder.
3. Connect. Claude Code:
   ```
   claude mcp add --transport http instantly https://mcp.instantly.ai/mcp \
     --header "Authorization: Bearer $INSTANTLY_API_KEY"
   ```
   Codex or another client: the same URL and header, or the CLI's local server (`npx @instantlyai/cli mcp`) with `INSTANTLY_API_KEY` in the environment. The key lives in a secret store, never the repo.
4. Test read-only: `get_server_info`, `workspace_get`, `workspace_billing_plan_details`, `list_accounts`. Givi's unpaid workspace answered 402.

### 4.3 Step 2: sending domains and mailboxes (agent 30 minutes; delivery time unverified)

Never send cold email from the product's main domain: its reputation carries your sign-in codes and receipts. Buy 1-2 lookalikes (`get<brand>.com`, `<brand>hq.com`, `try<brand>.com`) forwarding to the main site.

- `dfy_orders_check_domains`, `dfy_orders_similar_domains` and `dfy_orders_pre_warmed` find available and pre-warmed domains (read-only).
- `dfy_orders_create` spends real money. Run it with `simulation: true` for the exact price, show the founder the full order, then place it; the tool requires the founder's reply, verbatim, in `user_confirmation`. Order types: `dfy`, `pre_warmed_up`, `extra_accounts`. Google and AirMail allow up to 5 mailboxes per domain; Outlook requires exactly 50. Use 2 per domain, named for the person who will answer (`<first>@get<brand>.com`).
- `dfy_orders_list` and `dfy_orders_list_accounts` until they arrive; `list_accounts` to confirm.

Buying your own (Google Workspace on the lookalike domain): set DNS (section 6), connect each mailbox under Email Accounts > Add New, and warm up from scratch.

### 4.4 Step 3: warm-up (2-4 weeks for fresh mailboxes)

- `accounts_warmup_enable` on every sending account, and leave it on while campaigns run.
- Instantly's pre-filled warm-up settings for new accounts: 10 a day, plus 1 a day, 30% reply rate (Help Center). Keep them.
- Instantly's blog: warm new mailboxes at least two to four weeks; cap cold sends at 30 per mailbox per day; start at 5-10.
- Watch `get_warmup_analytics` (inbox versus spam) and `accounts_test_vitals` (MX, SPF, DKIM, DMARC per domain, passing and failing).
- Pre-warmed mailboxes still ramp: 10-15 a day each in week 1, then up to 30.

### 4.5 Step 4: lead sourcing (agent 1-2 hours for 30-50 leads)

The founder writes the buyer before any list exists; on Givi an agent picked "UK agencies" alone, so that research list (never contacted) had to be redone **(learned the hard way)**. First list: 30-50 people, one market.

- **Instantly SuperSearch** (credits spent on import only). `enrichment_generate_filters` turns "owners of 5-20 person marketing agencies in the UK" into filters; `enrichment_count` and `enrichment_preview` show matches for free. A count at the 1,000,000 cap means the filters did nothing. Locations are objects from `places_autocomplete`; a plain string is rejected, and an unresolvable place silently searches worldwide. Then `enrichment_enrich` with a `limit`, `work_email_enrichment: true` and `skip_rows_without_email: true`, which imports into a list and verifies found emails. Save the query with `saved_search_create`.
- **Clay MCP:** `get-current-workspace` first (whose credits), then `search-companies`, `search-contacts`, and `add-contact-data-points` for work emails.
- **Public pages** for small lists: the business's own site, with the source URL.

Keep per lead: first name, company, role, work email, website, source URL, one fit reason. Leave Instantly's AI Lead Finder Agent (`lead_finder_agent_create`, which spends credits on every top-up) off until you have read replies from the first 50.

### 4.6 Step 5: verification and enrichment (agent 30 minutes)

- Verify every address. One at a time: `verify_email`, then `email_verification_status` if it returns `pending` (anything over 10 seconds does). Lists: import with `verify_leads_on_import: true`, then `get_verification_stats_for_lead_list`. Drop invalid, catch-all and risky addresses from early batches.
- Fill gaps with `enrichment_create` (types include `work_email_enrichment`, `fully_enriched_profile`, `joblisting`, `news`, `funding`, `ai_enrichment`) and `enrichment_run`.
- An AI column (`enrichment_ai` with your `prompt`, `input_columns` and an `output_column` such as `observation`) can draft each lead's personal line. Treat it as a draft for the next step.

### 4.7 Step 6: personalisation that is not slop

One observation per lead, from a source you can name, that would be false for any other company: "Your careers page has had a project-coordinator role open since August." Never compliments, invented familiarity, guesses, or their tagline read back to them. No real observation in 3 minutes: the lead waits. A person checks the first 10 against their sources, then 1 in 5.

Promise only work the live product has produced. On Givi a research sub-agent drafted three sample cold emails (never sent) offering a report the product could not make: its data source returned 403 to a plain fetch, and the official API did not cover the businesses being emailed **(learned the hard way)**.

### 4.8 Step 7: the sequence

Plain text, under 100 words each, no images, attachments or tracking, and no link in email 1 (a link to the main domain ties it to the cold mailbox; send it to people who reply).

| Step | Delay | Content |
|---|---|---|
| 1 | day 0 | the observation; what you do for businesses like theirs; one concrete thing you would do for them; a yes/no question |
| 2 | day 3 | 2-3 sentences: one new useful detail, the same question |
| 3 | day 7 | a different angle, or offer the finished piece of work |
| 4 (optional) | day 14 | one polite line closing the loop |

Leave the subject empty on steps 2-4 so Instantly sends them in the same thread (Instantly Help Center, "email threading"). Givi's plan had 2 steps; 3 is a sensible first test. Use variables only where every lead has a value: `{{firstName}}`, `{{companyName}}`, `{{observation}}`.

### 4.9 Step 8: build the campaign, paused (agent 30 minutes)

1. `create_campaign` with `name`; `sequences` (one object whose `steps` each have `type: "email"`, a `delay` and `variants` with `subject` and `body`); `email_list` (sending accounts); `daily_limit` (per sending account per day, start at 10-15); `email_gap` 10-15 minutes; `text_only: true`; `open_tracking: false`; `link_tracking: false`; `stop_on_reply: true`; and `campaign_schedule`:
   ```json
   {"schedules":[{"name":"UK weekdays","timing":{"from":"08:30","to":"16:30"},
     "days":{"1":true,"2":true,"3":true,"4":true,"5":true},"timezone":"Europe/Isle_of_Man"}]}
   ```
   Two traps in the spec on 13 Oct 2026: without a schedule the MCP defaults to weekdays 9-17 US Eastern; and the accepted timezones did not include `Europe/London` or `America/New_York` (`Europe/Isle_of_Man` and `America/Detroit` keep the same clocks).
2. Settings `create_campaign` does not expose (`insert_unsubscribe_header`, `stop_for_company`, `allow_risky_contacts`) go through `update_campaign` or the campaign's Options tab. Turn the unsubscribe header on; leave bounce protection on.
3. `add_leads_to_campaign_or_list_bulk`: up to 1,000 per call, with `campaign_id`, `skip_if_in_workspace: true`, `verify_leads_on_import: true`; the workspace default blocklist applies unless you pass `blocklist_id`. Each lead carries `email`, `first_name`, `company_name`, `website` and `custom_variables`.
4. Read it back with `get_campaign` and check the preview. The API describes a step's `delay` as the wait before the next email, the MCP as the wait before this step; confirm the real dates before anything sends.

### 4.10 Step 9: test, approve, first send

1. Send yourself a test to a Gmail and an Outlook address; read it on a phone.
2. Run an inbox-placement test (6.3); fix anything landing in spam.
3. The founder approves the list and exact copy once (about 10 minutes): 5 full emails with their observations, the footer, daily volume and schedule.
4. First batch of 10-20. `activate_campaign` is a first-contact send in the founder's name: the agent runs it only after the founder's explicit yes in that conversation. More batches of the same list and copy need no new yes; a new list or new copy does.
5. Nothing going out: `campaigns_sending_status` explains why.

### 4.11 Step 10: replies within hours

- **Read:** `count_unread_emails`, then `list_emails` with `email_type: "received"`, `is_unread: true` and `campaign_id`, 3-4 times a working day. On Hypergrowth a webhook (`webhooks_create`, event `reply_received`) pushes each reply to your endpoint, with the text and an `email_id` to reply to.
- **Label:** `leads_update_interest_status` with `interest_value` 1 interested, 2 meeting booked, 3 meeting completed, 4 won, 0 out of office, -1 not interested, -2 wrong person, -3 lost, -4 no show. Custom labels with `lead_labels_create`; `lead_labels_test_ai` shows how Instantly's AI would label a sample reply.
- **Answer** within 2 working hours: the agent drafts in the founder's voice and sends with `reply_to_email` (`reply_to_uuid`, `eaccount`, and `to` set to the expected recipient so a wrong-thread reply is refused), then `mark_thread_as_read`. Interested: the call link. Not interested: one line of thanks, then the blocklist. Opt-out: blocklist at once. On Growth the Unibox is preview-only; we did not test API replies on Growth.
- Keep Instantly's AI Reply Agent off until the founder has read your first 50 replies.

### 4.12 Step 11: analytics and suppression

Tools: `get_campaign_analytics`, `analytics_campaign_overview`, `get_daily_campaign_analytics`, `analytics_campaign_steps`, `analytics_daily_account`.

| Number | Act when |
|---|---|
| Bounce rate | above 3%: `pause_campaign`, re-verify the list |
| Complaints | above 0.3%: stop that mailbox |
| Reply rate | under 1% after 150-200 delivered: change the observation or the offer |
| Interested replies, calls, trials, paid | always with the denominator: "4 interested from 180 delivered" |

Ignore open rate: tracking is off, and Apple Mail's privacy feature marks many emails opened anyway.

Before the first send, `blocklist_create` (an email or a whole domain per call) for customers, testers, warm contacts (they get personal notes, never a sequence), partners, competitors and clients of the founder's other businesses. Every opt-out and "not interested" joins it the same day and stays forever. `skip_if_in_workspace` on every import stops one person entering two campaigns.

### 4.13 What the agent may run alone

| Agent alone | Founder's yes first |
|---|---|
| reads: `workspace_get`, `list_accounts`, `dfy_orders_check_domains`, `dfy_orders_pre_warmed`, `enrichment_count`, `enrichment_preview`, analytics, `list_emails` | `dfy_orders_create`, plan changes, credit purchases |
| `accounts_warmup_enable`, `accounts_test_vitals`, `verify_email` | `enrichment_enrich`, `lead_finder_agent_create` (state the credit cost) |
| `create_campaign`, `update_campaign`, `add_leads_to_campaign_or_list_bulk`, all left paused | `activate_campaign` for a new list or new copy |
| `pause_campaign` (at once, when a stop rule trips), `blocklist_create`, `leads_update_interest_status` | `reply_to_email` outside the approved answer bank; AI Reply or Sales Agent; any `delete_*` |

> **What happened on Givi.** The Instantly MCP was connected all launch and got three read-only calls; the workspace had no paid plan, no sending domain existed, and no cold email was ever sent. The plan for pre-warmed mailboxes, plain text and stop rules never ran because the money question was never asked and the line had no owner. Separately, an agent studying a competitor's cold-email product clicked past a budget step in the founder's funded, signed-in account on that product, and the competitor's onboarding switched on six campaigns at $15 a day. The safety classifier stopped the agent from touching them, Vito pressed "Stop all campaigns", and a read-only check confirmed nothing had gone out **(learned the hard way)**. Study competitors only from a fresh test account, and stop before any launch or budget button.

---

## 5. Compliance at a practical level (recommended, not tested by us)

**Not legal advice.** What we found in primary sources on 13 Oct 2026; the ICO marked its guidance "under review" after the Data (Use and Access) Act 2025. Write findings per market into `legal/markets.md` and re-check the regulator before the first send.

**United Kingdom (PECR plus UK GDPR).**
- Corporate subscribers (limited companies, LLPs, Scottish partnerships, some public bodies): the ICO says the PECR email rule does not apply, so no consent is needed. You must not hide who you are, and must give a valid opt-out address.
- Sole traders and other partnerships count as individuals: email marketing needs their consent or the soft opt-in (your own past customers). In practice, no cold email to them. Check each UK lead on Companies House.
- UK GDPR still applies when the address names a person. Rely on legitimate interests, written as a short three-part test (the interest, why email is needed, why it does not override theirs). Say in the first email where you got their details and how to object, with a privacy-notice link. An objection means stop and suppress at once.
- The 2025 Act raises maximum PECR fines to UK GDPR levels (£17.5 million or 4% of turnover); check whether that is in force yet.
- A UK company shows its name, registered number, place of registration and registered office on business emails.

**United States (CAN-SPAM).** No consent needed; the FTC says the law "makes no exception for business-to-business email". Rules: no false headers; no deceptive subject lines; identify the message as an ad; a valid physical postal address (street address, USPS-registered PO box, or registered private mailbox); a clear opt-out that works for 30 days after sending and is honoured within 10 business days; you answer for anyone sending for you. Up to $53,088 per violating email.

**European Union.** National rules differ. France (CNIL): B2B email to a professional address is allowed without consent if it concerns the person's job, they are told where their data came from, and opting out is easy. Germany: advertising email generally needs prior consent, B2B included; skip it without local advice. Check each national regulator first. Canada and Australia also lean on consent; leave them out of a first test.

**The footer, in plain text on every email:**

```
<Founder first name> <surname>
<Company name>, registered in England and Wales, company no. <number>
<Registered office, or a registered mail-forwarding address>

I found your address on <source>. If you'd rather not hear from me,
reply "no" and I won't write again. How we handle your details: <privacy link>
```

Never the founder's home address. Subject lines say what the email is about ("Your open coordinator role"); no "Re:" on a first email, no fake urgency.

---

## 6. Deliverability basics (recommended, not tested by us)

### 6.1 SPF, DKIM and DMARC on every sending domain

Done-for-you domains arrive configured; check anyway with `accounts_test_vitals`. For your own Google Workspace domain (Cloudflare Dashboard > domain > DNS > Records > Add record):

| Record | Host | Value |
|---|---|---|
| SPF (TXT) | `@` | `v=spf1 include:_spf.google.com ~all` |
| DKIM (TXT) | `google._domainkey` | from Google Admin > Apps > Google Workspace > Gmail > Authenticate email > Generate new record, then Start authentication |
| DMARC (TXT) | `_dmarc` | `v=DMARC1; p=none; rua=mailto:dmarc@<main domain>`; move to `p=quarantine` after 2-4 clean weeks |

Check with `dig TXT <domain> +short` (and the `google._domainkey.` and `_dmarc.` hosts); Cloudflare changes show in minutes, others can take up to 48 hours. Gmail's rules (13 Oct 2026): every sender needs SPF or DKIM and a spam rate below 0.3%; senders of over 5,000 a day also need DMARC, alignment and one-click unsubscribe. Meet the bulk rules anyway.

### 6.2 Bounces and spam traps

Verified lists bounce under 2%; above 3%, pause and re-verify. Spam traps are addresses that exist to catch bad lists: never-used addresses planted on web pages (caught by scraping) and abandoned addresses that providers recycle (caught by stale lists). Hitting them can blocklist a domain. No bought lists, no scraped dumps, verify everything, drop catch-all and risky results, re-verify lists older than 90 days.

### 6.3 Inbox-placement tests

Before the first send and weekly: `inbox_placement_create`, then `inbox_placement_analytics_stats_by_test` (inbox versus spam per provider) and `inbox_placement_reports_list` (blacklist and SpamAssassin checks); these may need an add-on on your plan. A free quick score: send one campaign email to the address mail-tester.com gives you. Anything in spam: fix authentication and copy first.

---

## 7. Pipeline tracking and the stop rule

Every person moves through **contacted** (a message really went), **replied**, **call** (held, not just booked), **trial** (signed up and finished a first job), **paid** (the rule in 1.2), counted per line. The first paid row is milestone M1; the first stranger who pays without help is M2 (`01-framework.md`). The revenue owner sends one line a day (illustrative numbers):

```
Day 9: contacted 34 (warm 26, LinkedIn 8, cold 0) | replied 11 | calls 2 | trials 3 | paid 0
Stuck: 2 approved notes unsent (24h+), 1 reply unanswered (5h).
```

**The stop rule, written on day 0:** no payer after 20 warm conversations and 5 calls means change the offer or the audience, never the features. A conversation is a reply that went back and forth at least once; a call is one that happened. When it trips, the revenue owner writes one page (who was contacted, what they said in their own words, where they stopped, two concrete options such as a different first job or a different buyer) and the founder picks one. Ads have their own spend-based stop rule (`10-paid-ads.md`).

---

## 8. Prompts and approvals

### 8.1 Prompts for the revenue owner

**Warm list and notes (day before go-live)**
```
You own outreach. Read bd/metrics.md (buyer, "paid") and the live capabilities list.
The founder named: <names, one line each>. For each, add a Warm-tab row (first name and
role only), the founder's channel with them, buyer y/n. Draft one note per person in the
founder's voice: 60-90 words, one real detail about them, no price or deadline, ending
"try it, tell me what breaks, who else should see it". Email: Gmail create_draft.
WhatsApp: wa.me link with URL-encoded text. Telegram: t.me link. Send nothing. Post the
numbered list with every text in one message for the founder's approval.
```

**Daily sweep (scheduled, midday)**
```
Read the pipeline sheet. List: replies unanswered over 4 working hours; approved notes
unsent over 24h; testers silent over 24h; sign-ups with no first job; lines with no
action for 2 days. Then today's counts by stage and line. One message to the founder's
alert channel. Change nothing. Contact nobody.
```

**LinkedIn comments (each morning)**
```
Find up to 8 public LinkedIn posts under 48 hours old by people matching the buyer, via
web search restricted to linkedin.com/posts or the links the founder pasted. Do not browse
LinkedIn. Skip authors used in the last 7 days. Draft 5 comments: 2-4 sentences, one
specific useful point, the founder's voice; no compliments, links, hashtags, or product mention
unless the post asks for a tool. Add each to the LinkedIn tab with the URL and why the
author is a buyer. Never post, like, comment or message on LinkedIn.
```

**Cold list and personal lines**
```
Call workspace_get; stop unless the name is <venture workspace>. Find <30-50> people
matching <buyer line> with enrichment_generate_filters, enrichment_count and
enrichment_preview. Report count, 10 sample rows and credit cost; enrichment_enrich only
after the founder approves. UK: limited companies and LLPs only. Per lead: one checkable
fact from a public source, one plain sentence plus the URL, no compliments; NONE if
nothing in 3 minutes.
```

**Campaign build (paused)**
```
create_campaign: text_only true, open and link tracking false, stop_on_reply true,
daily_limit <10-15>, email_gap 12, weekdays 08:30-16:30 in <accepted timezone>, the
approved steps with empty subjects after step 1. Add approved leads with
add_leads_to_campaign_or_list_bulk (skip_if_in_workspace, verify_leads_on_import).
Unsubscribe header on via update_campaign. Read back with get_campaign.
Do NOT call activate_campaign. Report lead count, verification stats, 3 rendered emails.
```

**Replies (3-4 times a working day) and the weekly check**
```
list_emails with email_type "received", is_unread true. Classify each; set
leads_update_interest_status; update the sheet. Opt-out or not interested: blocklist_create
at once. Draft the answer from the approved answer bank; send with reply_to_email (with
"to") only if it stays inside the bank, else send the founder the draft and thread link.
Weekly: report contacted, conversations, calls, trials, paid per line and bounce,
complaint and reply rates per mailbox against the stop rules; pause_campaign if one trips.
```

### 8.2 What the founder approves

| Action | Who | Founder time |
|---|---|---|
| Buyer and stop rule | founder, day 0 (agent drafts) | 2 minutes |
| Money: plan, domains, mailboxes, credits | founder's yes on exact figures (`simulation` shown) | 2 minutes |
| Warm list and texts | founder approves once in sitting S3a, sends personal messages themselves | 15-20 minutes, once |
| Notes to early sign-ups | founder sends agent drafts | 1 minute each |
| LinkedIn comments, replies, notes, messages | founder posts from their clipboard, always | 5-10 minutes a day |
| Cold list and copy | founder, once per new list or copy | 10 minutes |
| First send of a new cold batch | agent, after the founder's explicit yes in that conversation | one line |
| Replies in existing threads | agent, inside the answer bank the founder approved after the first 5 replies; prices, discounts and promises go to the founder | |
| Pause, blocklist, verify, label | agent alone | none |

Write every authorisation the founder gives into the brief or script that acts on it the same turn. Anything on the founder's personal LinkedIn or WhatsApp stays manual even with their OK.

## Sources checked (13 Oct 2026)

developer.instantly.ai (API, MCP, CLI); instantly.ai/pricing; Instantly Help Center and blog; the Instantly MCP server's tool list (version 2.0.0, 199 tools); ICO B2B marketing guidance; FTC CAN-SPAM guide; CNIL; Google email sender guidelines; LinkedIn User Agreement 8.2.

## Checklist

- [ ] One revenue owner for outreach, ads owned elsewhere; a work-item file per line with outcome and due date
- [ ] "Paid" written and checked in billing code; buyer and stop rule written on day 0
- [ ] Pipeline sheet live; business contacts only; 90-day retention; never in git
- [ ] Cold-email money question asked once on day 0, one-off and monthly figures read that day
- [ ] 20-30 warm names from the founder; price-free notes drafted the day before go-live
- [ ] Gmail drafts and `wa.me` / `t.me` links ready; go-live sitting (S3a) done; sent log matches the list
- [ ] Every tester asked for one introduction; first 20 sign-ups got a note within the hour
- [ ] Daily sweep on a real scheduler, one line to the founder's chosen channel
- [ ] About 5 LinkedIn comments a day, posted by the founder; nothing automated on their profile
- [ ] New Instantly workspace, scoped key, MCP connected, `workspace_get` before writes
- [ ] Lookalike domains only; mailboxes pre-warmed or warmed 2-4 weeks; `accounts_test_vitals` and placement test clean
- [ ] 30-50 verified leads from one market with source URLs; UK leads checked on Companies House
- [ ] One checked observation per lead; promised work already produced by the live product
- [ ] 3 plain-text steps, no link in step 1, legal footer; campaign built paused with explicit schedule
- [ ] Blocklist loaded; first batch activated only after the founder's explicit yes
- [ ] Replies answered within 2 working hours; opt-outs blocklisted the same day
- [ ] Stop rules checked daily (bounce, complaints, replies) and weekly (20 conversations, 5 calls)
- [ ] Market rules in `legal/markets.md`
