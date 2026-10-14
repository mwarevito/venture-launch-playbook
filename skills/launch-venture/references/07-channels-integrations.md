# Chat channels and integrations

An AI-assistant product lives where customers already talk, and it is only as useful as the apps it can act in. This file covers choosing channels (and checking each platform's policy first), a Telegram bot, a Slack app, why WhatsApp was closed to Givi, voice, and the connected-apps layer with its approval gate and acceptance tests.

**Done when:** a thin web surface (sign-up, checkout, connecting apps) and one messenger pass a scripted acceptance on every release; every channel you show has a written policy verdict per market; customers connect their apps through branded one-tap links; money, publishing, deletions and access changes always wait for the owner's approval; every advertised connector has passed one live test on a real account.

Telegram Bot API, Slack, Composio and Vapi details and Meta's WhatsApp policy were checked on 13 Oct 2026. Platform terms change; re-check before you build or advertise a channel.

> **What happened on Givi.** Telegram was live on day 10 and was where testers spent their time. Slack went live as a free beta after about 15 minutes of coding and 3 hours waiting on a sign-in. WhatsApp was estimated twice, put on two landing pages and half-configured in the Meta console before anyone read Meta's policy, which bars general-purpose AI assistants in Givi's markets. A phone line failed on the founder's first call. Connected apps went through Composio after a hand-built OAuth layer and a second rival connector stack were thrown away. In the week when 44 of 45 visitors who clicked Start were lost at sign-in, about 35 pull requests shipped. **(learned the hard way)**

---

## 1. Which channels, and when

**Rule: one messenger plus a thin web surface until 3 customers pay.** Extra channels, phone numbers, marketplace listings and extra "doors" wait unless revenue depends on them. Each new channel adds code, a review surface, test identities and a founder sign-in. The brand's own marketing profiles (Facebook Page, Instagram and the other handles) are a separate job: brand-owned, with two-factor and a second admin, set up in sitting S1b (`02-day0-accounts.md`, section 14).

| Channel | Verdict for a first launch | Givi evidence |
|---|---|---|
| Web app | Always: sign-up, checkout, connecting apps, settings | **(done on Givi)** |
| Telegram | The default messenger for an assistant product: open policy, free, bots are first-class | Live on day 10; testers used it most **(done on Givi)** |
| Slack | Only when buyers ask; a free beta at most before a Marketplace listing | About 15 minutes of coding **(done on Givi)** |
| WhatsApp | Check policy per market first; barred for general-purpose AI assistants in the UK and US as of Oct 2026 | Found after the channel was already on landing pages **(learned the hard way)** |
| Phone number | After a web call has proven demand, and only when owners ask | Failed on the founder's first call **(learned the hard way)** |
| Web call (WebRTC) | The first voice option, inside the app or a Telegram Mini App | About 18 minutes to build **(done on Givi)** |
| Instagram DM, Messenger, email-in | After 3 payers; Meta messaging scopes need App Review | Built and proven for a review, not sold **(done on Givi)** |

---

## 2. Check the platform's policy before any estimate, copy or console change

About 30 minutes per channel and market, on day 0. **(recommended, not tested by us; Givi found its WhatsApp answer in about 1.5 hours, too late)**

1. Fetch the platform's primary terms pages (business API terms, AI or automation clauses, commercial-use rules), then search for current enforcement news.
2. Record, per channel and market: allowed or not; approvals needed; per-message costs; group limits; marketplace or review thresholds; and the ban risk to the business account that also holds your ads and app reviews.
3. Write one line in your go-to-market doc: "Channels live: ... / Channels barred: ...", with the clause quoted and the date checked.
4. Add a test that fails if a barred channel's name or logo appears on a public page or in app copy. **(done on Givi, after the fact)**
5. Add one line to the repo's agent instructions: "Before estimating or building any third-party channel, fetch its AI-assistant and commercial-use terms and record the verdict."

The founder only gives a go or no-go per channel, based on the agent's one-line verdict.

### WhatsApp, as of 13 Oct 2026

Meta's WhatsApp Business Solution terms gained an "AI Providers" section in October 2025, effective 15 Jan 2026. It bars providers of AI technologies, including general-purpose AI assistants, from using the WhatsApp Business Platform when that technology is their primary functionality. Businesses that use AI to serve their own customers (a travel company's support bot, for example) are still allowed ([TechCrunch, 18 Oct 2025](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform)). Regulators then forced exceptions: Italy and Brazil in January 2026 ([TechCrunch, 15 Jan 2026](https://techcrunch.com/2026/01/15/after-italy-whatsapp-excludes-brazil-from-rival-chatbot-ban)), and the EU, where Meta announced paid access for rival AI assistants for 12 months on 6 Mar 2026 while the European Commission's investigation continued ([trade press report](https://storyboard18.com/brand-makers/meta-to-allow-rival-ai-chatbots-on-whatsapp-in-europe-for-12-months-amid-eu-probe-2-91405.htm)). Givi's own check on 3 Oct 2026 found its launch markets, the UK and the US included, still barred. The answer differs by region and keeps moving, so check the current terms for each market you sell in.

> **What happened on Givi.** WhatsApp was estimated at 1-2 weeks of work, then re-estimated at 1-2 days, and listed on two landing pages. An agent had started adding the WhatsApp use case to a Meta app whose ads-related review was still pending when a parallel session flagged the ban. Removal took six correction PRs and a clean-up of the Meta review draft; the use case was still on the Meta app a week later. The real cost was risk to the app under review and wrong public copy. **(learned the hard way)**

Even where WhatsApp is allowed, budget for business verification, a WhatsApp Business Account, display-name and template approvals, and paid templates for any message sent more than 24 hours after the customer's last one. Never use an unofficial WhatsApp Web bridge for a paid product: it can get the number banned, and the founder ruled it out because it could put the ad accounts at risk. **(done on Givi: research only)**

---

## 3. Telegram bot

Agent time for the core (pairing, approvals, commands, restart handling): about 70 minutes plus three review rounds. Founder time: about 5 minutes. **(done on Givi)**

### 3.1 Create the bots

1. **The founder** opens @BotFather: `/newbot`, a display name, then a username of 5-32 characters ending in `bot`. About 2 minutes, in sitting S1b, right after the name is chosen. **(done on Givi)**
2. Create a **second bot for staging and tests**. A bot has exactly one webhook, so tests against the real bot steal production traffic. **(recommended, not tested by us)**
3. `/setprivacy` > Disable, only if the bot must read every group message. After changing privacy mode, the bot must be re-added to existing groups (Telegram docs). **(done on Givi)**
4. Set commands and description from code at boot (`setMyCommands`, `setMyDescription`) and check `getMe` returns `can_read_all_group_messages` as expected. **(done on Givi)**

**Move the token with a script, never through chat.** The founder copies the token and double-clicks a prepared script that validates it with `getMe`, checks the linked hosting project is the venture's own, stores it with `railway variable set TELEGRAM_BOT_TOKEN --stdin --skip-deploys`, clears the clipboard and prints only the bot's username. Dry-run it with a dummy value first. On Givi three secrets were pasted into chat, and one then appeared as a literal in at least five shell commands. If a key lands in chat, move it to the macOS Keychain at once (`security add-generic-password -U -a "$USER" -s <name> -w "$(pbpaste)"`) and log its name as exposed. **(learned the hard way)**

**Never run the real token locally.** Givi's app re-points the webhook at startup, so a local run with the real token steals production's webhook. Use a fake token and a fake Telegram server for local work. **(learned the hard way)**

### 3.2 Webhook and delivery

- `setWebhook` to `https://app.yourdomain.com/telegram/webhook` with a `secret_token` (1-256 characters, `A-Z a-z 0-9 _ -`). Telegram sends it in the `X-Telegram-Bot-Api-Secret-Token` header on every request; reject anything else with 401. Webhooks accept ports 443, 80, 88 and 8443; `getUpdates` stops working while a webhook is set. (Bot API 10.3 docs, checked 13 Oct 2026.) **(done on Givi)**
- Include `callback_query` in `allowed_updates`: inline-button taps arrive that way.
- **Store, then handle.** Insert each update by `update_id` (insert-or-ignore) before handling it; mark malformed but authentic updates done. A malformed update on Givi crashed before the dedupe step, so Telegram retried it forever. **(learned the hard way)**
- **Durable outbox** with idempotency keys. A row stuck in "sending" for 2 minutes becomes "unknown" and is never re-sent automatically. **(done on Givi)**
- **After a restart**, requests younger than an hour get "I restarted before I could answer" and are never re-run, because they may have partly run. **(done on Givi)**
- **Rate limits:** one outbound queue that honours `retry_after` on HTTP 429, and broadcasts (such as an 08:00 brief to every owner) spread over a few minutes. Check the current limits in Telegram's Bot FAQ. **(recommended, not tested by us)**
- **Merged is not shipped.** A fix for inbound messages was merged and never deployed. Check the running deployment contains the commit (`/api/version`, see `05-product-and-infra.md`). **(learned the hard way)**

### 3.3 Pairing a user

1. The web app makes a one-time deep link `https://t.me/<bot>?start=<code>`, valid 10 minutes and stored hashed. The start parameter allows up to 64 characters of `A-Z a-z 0-9 _ -`, so send an opaque code only.
2. After the user taps Start, the bot replies "Almost done: confirm in <app> that this is you" with a button that opens the exact app screen. Confirming there stops a forwarded link from binding someone else.
3. One active link per chat (a unique index on bot and chat ID).

**(done on Givi)** Every bot step ends with a button to the exact place: a new owner told "confirm in the app" with no pointer got lost. The pairing screen needs one request in flight at a time, inline errors, "copy command" as a fallback, and a Telegram entry in the main menu; one tester could not find where to connect Telegram at all. **(learned the hard way)**

### 3.4 The chat contract

Ship these in version 1. Each came from a real session that went wrong. **(learned the hard way, then done on Givi)**
- **Never refuse a message sent mid-turn.** Queue it, save the text at once, and after 10 seconds send one "one moment" line. Givi first answered "I'm still working on your previous message" and stored nothing.
- **Progress line:** one temporary message naming the current step ("Searching the web..."), edited every few seconds and deleted after the answer. Users had stared at "typing" for 30-90 seconds.
- **Approval cards as inline buttons:** "Needs your OK: <one sentence>" with Approve and Decline; recipients, amounts and targets always visible, the rest behind Details. Only the paired owner's taps count, matched by Telegram user ID. Send the card after its explanation (hold it up to 45 seconds). Private cards expire visibly after 6 hours.
- **No footers or diagnostic lines.** A tester called the effort footer "rubbish".
- **Formatting:** split at about 3,800 characters (Telegram's limit is 4,096); turn tables into one line per row; files up to 20 MB (the Bot API download limit); gather photo albums into one task.
- **No loose ends:** a "not connected" answer carries the connect link; a repeatable check ends with one "Want this every morning?" offer.

### 3.5 Voice notes in and out

- **In:** voice notes, audio files and round videos go to a speech-to-text model on their own capped key. Givi used OpenRouter's `POST /api/v1/audio/transcriptions`; a test came back word for word in 4 seconds for a fraction of a cent. Built in 44 minutes. Cap notes at 5 minutes and 20 MB, show "Heard: ..." for longer notes, and keep message order so a typed message cannot overtake a voice note. Treat forwarded voice as someone else's words, never the owner's instruction. **(done on Givi)**
- **Out:** `sendVoice` displays a playable voice message for OGG encoded with Opus, MP3 or M4A, up to 50 MB (Bot API docs). Givi's text-to-speech model returned raw PCM only, so replies are converted with `ffmpeg` to OGG/Opus; ffmpeg must be in the app image. **(done on Givi)**
- **Verify that a voice message arrives**, not that a flag is on. Givi switched voice replies on for everyone after checking the flag; every reply silently fell back to text for about a day. Alert operators on any silent fallback. **(learned the hard way)**
- Name the transcription and voice providers on the privacy page. **(recommended, not tested by us)**

### 3.6 Groups

- The owner adds the bot to a group by hand, following three written steps, then taps Allow in their private chat. Avoid the `startgroup` invite link: it posts a start command the bot could answer before the owner allows it. **(done on Givi)**
- Answer only when mentioned or replied to; keep the last 24 hours as context (Givi capped it at 40 messages). **(done on Givi)**
- Each connected app has a Private or Team switch; group tasks use only Team apps, and every change in a group waits for the owner's private approval. Store whether a request came from a private chat or a group with the job, and have the tool proxy deny private apps in group context. Code review found two leaks where a scheduled job created in a group could later read the owner's private apps. **(learned the hard way)**
- Test with a real second account in a real test group. Givi's team groups went two weeks without a live test because no second account existed. **(learned the hard way)**

> **What happened on Givi.** Two testers had bad sessions on 29-30 Sep 2026: messages refused and lost mid-turn, approval cards arriving before their explanation, three cards for one fix, a $0.76 turn because a bare "yes" was judged a hard task, and two deploys from other sessions restarting the app mid-conversation. Rebuilding the timeline from the chat export, the database, the agent transcript and the logs, then fixing it, took about 1.5 days. Acceptance had tested the mechanics (pairing, webhook, "got an answer") and never a conversation. **(learned the hard way)**

---

## 4. Slack app

About 15-20 minutes of coding and 20 minutes of review on Givi; 3 hours 44 minutes of wall clock, 3 hours of it waiting for the founder to sign in to api.slack.com. Put that sign-in in a planned founder sitting (S1b, if Slack is part of the first launch). **(done on Givi)**

**The manifest** (Givi's, DM only, generalised):

```yaml
display_information:
  name: YourBrand
features:
  app_home:
    home_tab_enabled: false
    messages_tab_enabled: true          # the DM lives in App Home > Messages
    messages_tab_read_only_enabled: false
  bot_user:
    display_name: YourBrand
    always_online: true
oauth_config:
  redirect_urls:
    - https://app.yourdomain.com/slack/oauth
  scopes:
    bot: [chat:write, files:read, im:history, im:write, reactions:write]
settings:
  event_subscriptions:
    request_url: https://app.yourdomain.com/slack/events
    bot_events: [message.im, app_uninstalled, tokens_revoked]
  interactivity:
    is_enabled: true
    request_url: https://app.yourdomain.com/slack/interactions
  org_deploy_enabled: false
  socket_mode_enabled: false             # HTTP Events API
  token_rotation_enabled: false
```

Steps:
1. Deploy the three routes first. Slack sends a signed challenge to the events URL before it saves the manifest.
2. api.slack.com/apps > Create New App > From a manifest > choose a workspace the venture owns > paste the YAML. **Ask for every scope in the first install**: adding `files:read` later forced every workspace to re-approve. **(learned the hard way)**
3. Basic Information: icon; copy the client ID, client secret and signing secret through the validating script. Record the public App ID for links.
4. Manage Distribution > confirm no hard-coded tokens > Activate Public Distribution.
5. "Add to Slack" sends users to `https://slack.com/oauth/v2/authorize` with a one-time `state` (10 minutes, stored hashed) naming the owner. The Slack account that approves becomes the owner's identity.
6. Events: verify the signature with the signing secret, refuse requests older than 5 minutes, acknowledge within 3 seconds and process asynchronously, handle each event once. Keep section blocks under 3,000 characters.
7. Send the bot token only to `files.slack.com` when downloading files. Link users to their DM with `https://slack.com/app_redirect?app=<APP_ID>&team=<TEAM_ID>`; a `slack://` link failed an https-only validator. **(learned the hard way)**
8. Live test after every release: Add to Slack, a task, a gated delete with Approve, Undo on a send, a voice clip and a document; an unsigned request returns 401 or 403, never 404. **(done on Givi)**

Givi's agent edited the manifest through the page's code editor, because the coding agent's safety classifier refused to handle a Slack configuration token. Next time, have the founder run a small script that passes that token to `apps.manifest.create` or `apps.manifest.update` with the manifest from the repo. **(recommended, not tested by us)**

**The Marketplace comes later.** Slack's changelog of 1 Sep 2026 says apps submitted to the Slack Marketplace need at least 10 installations on active workspaces and must stay at 10 or more for the whole review. Givi's research also found Slack treats an app connected to a paid product as commercial distribution, review taking up to 10 weeks, and tight rate limits on history calls for unlisted commercial apps. Givi shipped Slack as a labelled free beta, counted tasks against the customer's plan, and added a digest line with active workspaces. **(done on Givi)**

---

## 5. Voice: a web call first

> **What happened on Givi.** The first voice feature was a phone number on Vapi with a custom-LLM endpoint and a spoken PIN, about 1 hour to build plus 35 minutes of setup. The founder's first test call never reached Vapi, and the free number only takes calls. Vapi's free numbers are US-only and call only US and Canada numbers (Vapi docs, checked 13 Oct 2026). The question of who pays for call minutes came up only afterwards. **(learned the hard way)**

What worked: a **web call inside a Telegram Mini App**, about 18 minutes to build and 38 minutes from complaint to live. A `/call` command opens a page that starts a Vapi web call over WebRTC: no number, no carrier. The owner is proven by Telegram's signed `initData` (at most an hour old), then a 10-minute signed call token; the public key is restricted to the app's origin and one assistant. A 48-second test call cost about $0.05. **(done on Givi)**

Rules from the calls that followed:
- When an API-created voice assistant has no voice and no transcriber block, calls are silent. Copy both from a known-good assistant. **(learned the hard way)**
- The platform resends the whole turn when the caller talks over the agent, so Givi's agent restarted up to 13 times in one call. Keep each word once and steer new words into the running work. A fast "talker" model in front cut time to first words from about 2.8 seconds to about 1 second. **(learned the hard way)**
- Check every language against the speech provider's supported list before promising it; one provider silently accepted a language code it does not support. **(learned the hard way)**
- Answer in 1-3 sentences; links and longer work go to the chat. Never confirm sends, payments or deletions by voice. Save each call as a session with its transcript. **(done on Givi)**
- Phone numbers only when owners ask, each a separate purchase yes, with a PIN confirmed by a code sent to the messenger. **(recommended, not tested by us)**

---

## 6. One adapter, one acceptance script, real test identities

**One channel adapter interface** implemented by every channel: `link`, `send_text`, `send_card`, `progress_start/update/stop`, `download_file` (streamed, size-capped), `deliver_scheduled`, `undo`, `feedback`, `restart_note`. **One contract test suite** parametrised over channels, run against fake servers: card order and owner-only taps, a message during a turn, a 1 MB file arriving whole, a scheduled result delivered, Undo inside the window, a restart mid-task. **(recommended, not tested by us)** Givi copied its Telegram module into a Slack module by hand instead; the suite would have caught three shipped bugs: scheduled results never reaching Slack-only owners, downloads cut off at about 64 KB, and Undo wired wrongly. **(learned the hard way)**

**Headless test identities.** A dedicated Telegram test account (its own SIM or virtual number, ordered in week 1) driven by an MTProto client such as Telethon or Pyrogram can send text, a generated `.ogg` voice note and files, read replies, press inline buttons and post in a test group with a second account. Keep session strings in the Keychain or a hosting variable. **(recommended, not tested by us)** Across Givi's sessions, agents touched the Bot API or Telegram Web in only a handful; the founder and testers found most channel bugs. **(learned the hard way)**

**Scripted acceptance on every release**, about 10 minutes, from the test identity first, then the founder's account:
- link a fresh account;
- memory across two messages;
- an approval-heavy task (connect an app, change a record, delete something), checking card order, count and the Approve tap;
- a message sent during a running turn;
- a voice note in, and a voice reply that actually arrives;
- a file;
- a restart mid-task;
- a group message from the second account;
- a reminder set 2 minutes ahead arriving in the same channel.

Check every claim against the database or the artifact, never the bot's own words.

**Channel health, hourly, silent when healthy:** `getWebhookInfo` (alert when `pending_update_count` grows or `last_error_date` is new), a signed test request to the Slack events URL, and an outside heartbeat such as Healthchecks.io. Telegram keeps unprocessed updates for only 24 hours, and Slack can turn off events to an endpoint that keeps failing; both fail quietly. **(recommended, not tested by us)**

**Retire old doors the same week:** `/deletebot` in BotFather (or at least `deleteWebhook`), old variables, redirect URLs and unused Meta use cases. Givi's old pilot bot was still live weeks later. **(learned the hard way)**

---

## 7. Connected apps through an aggregator

### 7.1 Why an aggregator

> **What happened on Givi.** On day 9 the founder said "nothing can be connected". Five connectors on the screen were dead ends: connections required a paid plan while payments were switched off, and the Google, Slack and ad-platform OAuth apps had never been registered. Two agents then built two rival connector stacks for two products on the same day. The working layer (Composio, white-labelled, behind an approval gate) took about 1.5 days, followed by two weeks of fixes found live. **(learned the hard way)**

Hand-built OAuth means registering an app with every provider, and Google's sensitive scopes take days to weeks of review. A hosted aggregator gives you managed OAuth apps for hundreds of services on day 1. Budget about 2 working days of agent time and about 45 minutes of founder time, inside the existing sittings: the aggregator sign-up in S1b, any Meta company steps in S2. **(recommended, from Givi's results)**

| Option | Notes (Givi's research, Sep-Oct 2026) |
|---|---|
| Composio | Chosen. Free tier at the time: 100,000 tool calls a month, unlimited connected accounts, branded connect page; Givi used a few hundred calls in 10 days at $0. Per-tool read and destructive tags. **(done on Givi)** |
| Pipedream Connect | The strongest alternative; short-lived tokens. Not tested |
| Nango | Full white-label, but you register your own app with every provider |
| Own OAuth apps | For the top 1-2 vendors after 3 payers, when a branded consent screen or push triggers matter |

Read the aggregator's commercial-use terms and get a data-processing agreement before charging customers. If the terms read as unclear on commercial use, ask for written confirmation. **(recommended, not tested by us)**

### 7.2 Wiring it

- **Account:** sign up with the brand Google account (or the Google Workspace address once you have moved to Workspace; see `02-day0-accounts.md`), two-factor on, a second admin, the workspace and project recorded in the access register. On Givi the sign-up login was not recorded, and a day later nobody knew which login held the account. **(learned the hard way)** The key arrives through the validating script and lives only on the app server.
- **One identity per customer:** each owner's connections live under their own `user_id`. Connections start with `connectedAccounts.initiate(<user_id>, <auth_config_id>)`, which returns a redirect URL ([Composio docs](https://docs.composio.dev/docs/auth-configuration/white-labeling), checked 13 Oct 2026). **(done on Givi)**
- **Agents never hold the platform key.** Givi's agents talk MCP to a proxy on the app's private port (the public URL returns 404); the proxy pins each agent to its owner's `user_id`. An adversarial review found the first version on a public URL guarded only by a token in the path, which a leak could have used to read a customer's mail or CRM. **(learned the hard way)**
- **Block the aggregator's general-purpose sandbox tools** (remote code and shell) and gate each item inside batch-execute tools on its own. They could bypass approvals. **(learned the hard way)**
- **White-label from the first wiring.** The founder's complaint: "it shows that I'm using Composio... that lowers my app's value." Fix (about 50 minutes): connect links on your own domain (`/connect/link/<token>`, valid 24 hours, remade on click because the vendor's link expires after about 10 minutes), your own interstitial and "Connected" pages, and Composio's Settings > White Labeling for name and logo. The provider's consent screen shows your brand only with your own OAuth app: create a custom auth config with your client ID and secret (`use_custom_auth`) per provider. That takes minutes for some providers and weeks for Google. **(done on Givi)**
- **Return to the same conversation.** After connecting, post "The owner connected X" into the conversation that asked, bound by link token, so the agent carries on without the owner typing "done". Matching by user and app resumed the wrong chat. **(learned the hard way)**
- **Curate the catalogue.** Show three honest tiers: one-click; a key on a secure form (never in chat), validated with the provider before the connection is created; not supported, with a "request this" button. Hide developer toolkits: asking to "send it on Telegram" once produced BotFather instructions. **(learned the hard way)**
- **Public claims use the in-app count.** Givi's landing and ads said "1,000+ apps" while owners could pick about 500. **(learned the hard way)**
- **Connected-apps page** with dates and a Disconnect that checks ownership; subscribe to the aggregator's "connection expired" webhook plus a 6-hourly sweep, and tell the owner "<App> disconnected, tap to reconnect". Abandoned connect links also show as expired after about 10 minutes, which caused two false alarms. **(learned the hard way)**

### 7.3 The approval gate: money, access, deletes

The founder's rule on Givi: "if something is connected by the person, we don't need any approvals; only in case of money and deletions." The final policy **(done on Givi)**:
- Reads never ask.
- Money, publishing or launches, deletions and access changes (sharing, invites, permissions, keys) always ask, whatever mode the owner picks.
- Everything else runs with a log line and a 60-second Undo for sends.
- Team groups ask for everything.

How to build it:
- **Classify by the tool's metadata** (`readOnlyHint`, `destructiveHint`, `openWorldHint` from the aggregator's catalogue), never by words in the tool name. Unknown or unparseable tools ask, or are refused. Word lists misfired live four times on Givi: "export" (how Sheets are read) and "report" asked for approval, a spreadsheet ending in "SHEET1" asked, and on the day "only deletions ask" went live, deletion words were missing from the list. **(learned the hard way)**
- **Publishing arguments count as publishing**: `publish`, `published`, `auto_publish`, `publish_now`, `direct_post`. A video upload with `publish=true` skipped Approve. Hold only the public step of two-step publish APIs. **(learned the hard way)**
- **Approved actions run exactly as shown, at most once.** An uncertain outcome (a timeout) is reported as "unknown" and never retried automatically. **(done on Givi)**
- **Pass the full approved result back to the agent.** Results cut to 300 characters made the agent ask to approve the same read again. **(learned the hard way)**
- **Measure the gate before every policy change:** a labelled set generated from the full catalogue (read, change, delete, publish argument, two-step publish, access, money), scored on every PR that touches the gate, blocking the merge if any delete, publish, access or money case would run without asking. A second-family review (`05-product-and-infra.md`, section 9) runs before the change ships. **(recommended, not tested by us)**

### 7.4 Connector acceptance tests

**Fixture accounts the agents control** (created in week 1): a test Google account in a non-UTC timezone, a second Gmail for multi-account tests, a CRM developer or demo account, a test Instagram account with a Facebook Page, and a controlled outside address to receive invites. Credentials in the Keychain, never in chat. Without them Givi never verified five paths live, including a calendar fix after a tester's invite reached a real outside partner at the wrong time. **(learned the hard way)**

**The suite, gating every connections release** (paste results into the PR):
1. The labelled gate set from 7.3.
2. A scripted live write pass: a CRM row with a phone number starting "+", a non-UTC calendar booking read back from the guest's side, a Gmail draft then send, a two-step social publish, two accounts on one app.
3. A probe of every advertised one-click provider, including one real OAuth pass. Hide any provider that refuses. A metadata-only probe let a "sign in with Meta Ads" button fail for every owner for 4 days. **(learned the hard way)**
4. "Connect my Gmail" from a fresh account: the button arrives in the first reply.
5. Before any public claim: every advertised connect button tested from a non-founder account, one write per top app, and a permalink for any "posts to Instagram" claim.

**Conventions the agent follows**, in a connected-apps skill and enforced in code where possible **(done on Givi)**: restate the effect before any write and read back after; write spreadsheet values starting with "+", "=" or "0" as text (phone numbers became formulas); calendar times as local time plus an IANA zone; follow pagination and report coverage (one inbox read silently covered 10 messages); search a CRM before creating.

### 7.5 Credentials and offboarding

- The aggregator key reaches every customer's connected mail, CRM and ad accounts. Keep it on a brand-owned account with two-factor and a second admin, stored only in server variables, with a written rotation runbook and one rotation drill before launch. **(recommended, not tested by us)**
- Deleting an account ends the plan, deletes every connected account for that owner at the aggregator, and unlinks chat channels. Run it once on a fixture account and check the aggregator's dashboard. Decide what happens to connections of lapsed trials and write it into the terms. **(done on Givi, unit-tested only)**
- Name the aggregator and every sub-processor on the privacy page. **(done on Givi)**

### 7.6 After 3 payers

- Your own OAuth apps, fastest first (CRM and Slack in minutes to days; Google sensitive scopes days to weeks plus a demo video; Gmail restricted scopes need a paid security assessment). Register at least one the same night you build the switch, or it stays untested; Givi's stayed dark. **(learned the hard way)**
- Your product as a connector for Claude and ChatGPT (an MCP server with OAuth). Givi built it in about an hour including two reviews, and first tested it from a real client 4 days later; test it the same day. **(learned the hard way)**
- Acting in customers' Meta ad accounts, WhatsApp or Instagram messaging needs your own Meta app and App Review; see `11-platform-approvals.md`. Givi spent about 20-25 agent-hours on App Review for permissions it did not need to sell. **(learned the hard way)**

---

## Checklist

- [ ] One codebase owns all channels; one thin web surface plus one messenger for the first launch
- [ ] Policy verdict per channel and market written, with clause and date; copy-guard test in place; agent-instructions line added
- [ ] No barred or unchecked channel on any landing page, ad or "coming soon" badge
- [ ] Product bot and staging bot created; privacy mode set; token stored by a validating script
- [ ] Webhook with `secret_token` checked on every request; updates stored by `update_id` before handling
- [ ] Durable outbox; restart note; outbound queue honouring `retry_after`; real token never run locally
- [ ] Pairing by 10-minute hashed deep link plus in-app confirm; Telegram entry in the main menu
- [ ] Chat contract shipped: queue mid-turn messages, progress line, owner-only approval buttons, no footers, tables flattened
- [ ] Voice notes capped and on their own key; voice replies verified by arrival, with a fallback alert
- [ ] Groups: manual add plus Allow, mention-only, private apps denied in group context, tested with a second account
- [ ] Slack (only if buyers ask): routes live before the manifest, all scopes in the first install, signatures checked, labelled free beta
- [ ] Voice: web call before any phone number; languages checked; numbers only on a purchase yes
- [ ] Channel adapter interface and contract suite; headless test identity; scripted acceptance on every release
- [ ] Hourly channel health job with an outside heartbeat; old bots and variables retired
- [ ] Aggregator account on the brand login, key via script, key only on the app server
- [ ] Connections per customer `user_id`; agents reach them through a private proxy; sandbox tools blocked
- [ ] White-label: own-domain links, own pages, vendor name never shown; return to the same conversation
- [ ] Approval gate by tool metadata: money, publishing, deletions and access always ask; at-most-once execution; labelled set scored on every gate PR
- [ ] Fixture accounts created; connector acceptance suite run and pasted into each connections PR
- [ ] Public claims match the in-app connector count and live tests
- [ ] Aggregator key rotation runbook; deletion path tested; sub-processors on the privacy page
