# Paid ads with agents: Meta, Google and TikTok

Paid ads are a measurement tool for a new venture, never the route to the first payer. This file covers the accounts and billing behind them, the gate the funnel must pass before any money moves, one capped first test (about 100 in the checkout currency), building campaigns through the Meta Ads MCP with everything created paused, a delivery and billing alarm that does not depend on a laptop or an agent session, and reading the results honestly at small budgets.

**Done when:** the funnel gate has passed (sign-up works on a real phone inside the Instagram, Facebook and TikTok in-app browsers; a real card checkout and refund are seen; at least 20 organic Start clicks with 25% or more reaching an account, checked by a session that does not own the ads); the ad account has a payment method that has passed a small charge, prepaid funds, a backup card and a spending limit read back through the API; the delivery alarm runs on a scheduler outside any agent session and has fired once on purpose; and, after the founder's dated yes, a capped test (one ad set, 2-3 statics) has run with a written stop rule and a verdict stated with its sample size.

Platform steps were checked against Meta, Google and TikTok help pages and Meta's developer docs on 13 Oct 2026. Ads consoles change often; when a path is missing, use the console's search box.

---

## What happened on Givi

From 8 to 12 Oct 2026 Givi spent about £110 (roughly £60 on Meta, $30 on Google, £25 on TikTok) and bought cheap clicks (Meta at about £0.15-0.30) and one sign-up, with no card and no paying customer. Two things caused that, and neither was the accounts or the campaign builds:

1. **Ads were bought into a sign-up path already seen failing.** Two days before launch the agent's own check showed about 30 Start clicks and zero sign-ups, and it explained the gap away as "mostly our own team". After launch, all but one of about 45 people who clicked Start left at the sign-in screen: Google's consent screen showed a backend domain instead of the brand, and Google sign-in does not work inside Instagram's in-app browser. **(learned the hard way)**
2. **Meta delivered for only about 1.8 of the first 5 days.** About one day went to a Meta A/B test object that can only start the next midnight. About two days went to failed card holds while Ads Manager showed every ad as "Active". The agent's watchdog lived inside an agent session, judged delivery in words, and died when the session ended. **(learned the hard way)**

What worked: once the Meta Ads MCP was connected, a full Meta build took about 6 minutes and a Google Search build about 2. A static image made from HTML in about 20 minutes took about 96% of UK and US Meta spend at roughly twice the click-through rate of the alternatives (about 5.6% against 2.6%). Films that took 30-40 hours of agent time barely ran. **(done on Givi)**

---

## 1. When to run paid ads at all

- **Before the first payer (M1):** only one capped measurement test, and only after the funnel gate (section 2) has passed, the warm outreach to the founder's own network has already gone out, and the founder has given a dated yes (an override recorded in the decisions log) saying they want paid traffic before a first payer.
- **Before 3 payers:** still only the capped test. No scaling, no extra markets.
- **After 3 payers:** scale on a measured winner, add markets one at a time, judged on cost per trial.

**The capped test** (in your checkout currency; Givi's figures were GBP). **(recommended, not tested by us):** Givi's own test broke most of these rules; only the spend concentration was seen on Givi.

| Item | Value |
|---|---|
| Budget | About 100 in total, 10-15 a day |
| Market | One: the launch market, where the likeliest payers are |
| Structure | One campaign, one ad set, broad targeting, 2-3 static ads running. Make 3-5 statics so you have replacements |
| Winner signal | Meta concentrates spend on one ad, usually within a day (about 96% on Givi). That ad is the winner you keep |
| Video | One short video of the winning hook, only after a static has won (`09-content-video-anti-slop.md`) |
| Stop rule | Stop at the cap, or at 150 landing visits with 0 sign-ups, whichever comes first |
| Verdict | Sign-ups per landing visit, with the sample size stated (a capped test rarely reaches enough trials for cost per trial) |
| Day-1 rule | Pause any ad under 0.5% link click-through (keep at least one running) and swap in a replacement static |

Write the metric, the founder's budget number and the stop rule down before any account is funded, and print progress against the stop rule in every daily check. Givi's launch kit had a stop rule that no daily check ever read. **(learned the hard way)**

---

## 2. The funnel gate before any spend

Run by a session that does not own the ads and did not build the sign-up path. The ads owner has every reason to explain a gap away; Givi's did. The operator checks the evidence before telling the founder. Nothing is spent until all five items pass. **(learned the hard way: none of this was done on Givi before launch)**

1. **In-app browser emulation.** With gstack's `browse` headless browser (or Playwright), at a phone viewport, using each real in-app user-agent string:

   ```bash
   B=~/.claude/skills/gstack/browse/dist/browse   # as in 04-landing-pages.md
   $B viewport 390x844
   $B useragent "<current Instagram in-app user agent for iOS>"
   $B goto https://yourdomain.com/?utm_source=meta
   $B screenshot          # every screen through to the account page
   ```

   Repeat with the Facebook and TikTok in-app user agents. Screenshot the **actual OAuth consent screen**: it must show your brand on your own auth domain. Givi's check confirmed only that "Continue with Google reaches Google", while the screen itself showed a backend project domain.

2. **The real-phone test** (about 5 minutes in sitting S3b, by the founder or a co-founder). DM the sign-up link to yourself on Instagram, open it inside the app, finish sign-up. Repeat inside Facebook and TikTok. Screenshots of every step go into the launch log.

3. **No Google sign-in inside webviews.** Google blocks OAuth in embedded browsers (error `disallowed_useragent`), and Instagram's and TikTok's in-app browsers are webviews. Offer an email code or magic link, or make Stripe Checkout the sign-up (see `06-payments-stripe.md`). Work done before sign-up must survive a switch from the in-app browser to Chrome.

4. **A real card checkout and refund** by the founder in sitting S3b, seen by the agent as `charge.refunded` in Stripe and the matching rows in the database. Givi's launch gate named this test; it never ran, and ads launched anyway.

5. **A numeric pass bar:** at least 20 organic Start clicks, at least 25% of them reaching an account, humans only, counted on the server. Organic means warm contacts, testers and paid stranger testers who are not on the team; team, bots and link previews never count. Fewer than 20 means the gate stays closed. Never lower the bar; if it fails, fix the path.

Re-run items 1 and 2 after every app release before and during the test. Givi shipped a full app redesign on launch day and never re-tested it in in-app browsers. **(learned the hard way)**

---

## 3. Meta setup

**First, the founder's standing.** Meta treats a person with an unpaid balance on any ad account they administer as a payment risk on everything they manage. On Givi, an old billing problem on another ad account under the same login was the most likely reason Meta refused every new card and the Page for about 2.5 days; the agent first blamed browser anti-fraud and cost the founder about 3 hours of retries. **(learned the hard way)** So the agent first reads Billing & payments and Account Quality for **every** ad account the founder's login can see (Claude in Chrome, read-only) and lists any balance due or failed charge for the founder to pay.

Then, in order. Steps 1-3 belong in sitting S1b, right after the name pick; steps 4-12 in sitting S2, the day the company number arrives (`01-framework.md`). Founder minutes are in brackets.

| Step | Where | Who | Notes |
|---|---|---|---|
| 1. Business portfolio | business.facebook.com > create portfolio | Founder (5 min) | Its own portfolio keeps a policy strike on one business from stopping another's ads. Reusing a verified portfolio skips Business Verification but shares that risk; decide on purpose |
| 2. Facebook Page | Business Suite > Pages > Add > Create a new Page | Founder, on their phone (5 min) | Claude Code's safety classifier blocked agents from creating it, and automated Facebook sign-ups trip anti-bot locks. Givi's first attempts failed on an SMS check and sat unowned for about 12 days **(learned the hard way)** |
| 3. Instagram professional account | Created in the Instagram app, then added to the portfolio | Founder (5 min) | |
| 4. Business Verification | Business settings > Security Centre | Founder (10 min) | Needs the company's documents. Givi's took about 19 hours **(done on Givi)** |
| 5. Ad account | Business settings > Accounts > Ad accounts > Add > Create | Founder clicks Create (5 min) | **Currency and time zone are effectively permanent** (a currency change makes Meta open a new ad account and close the old one). Use the checkout currency. Givi's was GBP against USD prices, which fed mixed currencies in ad copy **(learned the hard way)** |
| 6. Link Instagram to the ad account | Business settings > Instagram accounts > the account > Connected assets > Add | Founder (2 min) | Without it ads cannot run as the Instagram account **(done on Givi)** |
| 7. Payment | Billing & payments > Payment methods | Founder (10 min) | The venture's own card, a backup card and a small prepaid balance (Add funds). Without a VAT number Meta adds UK VAT (20%) to every charge |
| 8. Force one small charge | Billing & payments | Founder | Clear any notice with "Try again" before launch day |
| 9. Account spending limit | Billing & payments > Payment settings > Account spending limit | Founder (2 min) | Set it to the monthly cap. Read it back (below). Givi planned limits and never set them **(learned the hard way)** |
| 10. Second admin | Business settings > People | Founder (2 min) | A co-founder with their own 2FA; one admin is a lockout risk |
| 11. Domain verification | Business settings > Brand safety > Domains | Agent adds the DNS TXT record | **(recommended, not tested by us)** |
| 12. System-user tokens | Business settings > Users > System users | Founder (10 min) | Two tokens, below |

Before each sitting, the agent writes a one-screen field sheet with every value the founder will type: portfolio name, Page name, category, bio, website, ad account name, **currency**, **time zone**, legal name and address, VAT number. Keep any App Review test campaigns in a separate test ad account; Givi left a paused review fixture in the live account, one bulk action away from spending.

**Read the spending limit back** (versioned URL; Givi's unversioned calls hit a retired API version and wrongly reported "no ad account", error #2635):

```bash
curl -s -G "https://graph.facebook.com/v24.0/act_<AD_ACCOUNT_ID>" \
  --data-urlencode "fields=spend_cap,amount_spent,currency,account_status" \
  -K - <<< "header = \"Authorization: Bearer $META_READ_TOKEN\""
# spend_cap of "0" means no cap. Check Meta's changelog for the current version.
```

Read the real daily spending limit in the Billing hub too: Givi assumed "about $50 a day" for a new account, and it allowed £250. **(learned the hard way)**

**Two system-user tokens, least privilege:**

| Token | System user role and assets | Scopes | Expiry | Lives in |
|---|---|---|---|---|
| Reader | Employee, "View performance" on the ad account | `ads_read` | Never | The app server (for its ads report) and the alarm's scheduler |
| Manager | Ad account full control, Page, Instagram | `ads_management`, `ads_read`, `business_management` (Page publishing or comment scopes only if planned) | 60 days | The founder's Mac keychain only; renewal reminder at day 50 |

Keep the manager token narrow and off the app server: a server break-in would otherwise hand over the ad account and the Page. **(recommended, not tested by us)**

**Hand-off:** the agent writes one local script per token that reads the clipboard, validates the token against a versioned Graph URL, prints only names, scopes, assets and expiry, stores it (keychain via `security add-generic-password -U -s <service> -a <account> -w`, plus the host variable for the reader token only), clears the clipboard, prints "accepted" and deletes itself. The agent dry-runs it with a dummy value first; the founder copies the token and double-clicks. The token never appears in chat. **(done on Givi)**

---

## 4. Measurement: pixel, consent, server-side events and your own counts

Build all of this in one change, on day 1-2, before any creative exists.

- **Meta web pixel.** Call `ads_get_datasets` first: an app's dataset is not a web pixel. Create one in Events Manager (Connect data > Web) and confirm the ad account is listed under the dataset's Settings > Connected assets. **(done on Givi)**
- **Consent first.** In the UK and EEA, advertising pixels load only after the visitor accepts. One plain sentence, "No thanks" and "Allow" as equal-weight buttons of the same size and style, no platform names in the banner, details on the privacy page. With Givi's first banner about 95% of visitors never pressed Allow, so Meta's pixel saw a few dozen visitors while the server counted over 700. **(learned the hard way)**
- **Google Consent Mode v2** (only if Google ads run): load the Google tag with `ad_storage`, `ad_user_data`, `ad_personalization` and `analytics_storage` defaulting to `denied`, and update to `granted` on Allow. **(recommended, not tested by us)**
- **Server-side events** for consenting visitors only: Meta Conversions API and the TikTok Events API, with hashed email and click IDs. Givi sent TikTok's from the server and Meta's only from the browser. **(Meta CAPI recommended, not tested by us)**
- **No ad scripts inside the app.** Givi fired sign-up events from a small page on the landing domain that the app opened in a hidden frame. **(done on Givi)**
- **Your own funnel per ad** is the number you decide on: per `utm_content`, count real visitor, Start click (also sent to the platforms after consent), sign-in reached, sign-up, card, payment.
- **Size the consent gap on day 1.** Compare server visitors with pixel events (`ads_get_dataset_stats`, `ads_get_dataset_quality`). Meta needs about 50 conversion events a week per ad set to optimise for them. With a big gap, optimise for landing page views and decide on server counts.
- **Verify in a real browser** (headless ones get no pixel), with Meta's Test Events code and Google Tag Assistant. Givi's real test sign-up polluted all three dashboards. **(learned the hard way)**

**Humans-only counting.** A "visitor" counts only after a scroll, a tap, typing or 15 seconds on the page, reported by a small beacon (`navigator.sendBeacon` to your server). On Givi, the hourly "visitors" before marketing began were cloud servers posing as the same old iPhone, and most "visitors" in the pre-launch check were scanners and the team. Ad platforms' review robots also visit every new ad: about 30 "Meta visitors" arrived before Meta had delivered a single impression. Exclude them with one robot filter that every report and watchdog uses. **(learned the hard way)**

---

## 5. Offer, creatives and copy

- **Freeze the offer before rendering anything.** Price, currency, trial terms and claims live in one file that the app, landing, terms and ad text read. Price and trial terms go in the ad's text fields, **never inside an image or video**. On Givi the price changed mid-test: every channel was paused and 10 images and videos were re-rendered. **(learned the hard way)**
- **Statics first.** Make 3-5 static hooks in about an hour from an HTML template screenshotted to PNG at 4:5. A concrete value next to the price worked best: "$1,000+ of work. $49 a month." beat the promise images at about twice the click-through and half to a third of the cost per visit. The "AI agents" framing drew "#aiSlop" comments and people blocking the Page. **(done on Givi)** See `09-content-video-anti-slop.md`.
- **Video only after a static has won:** one 15-25 second vertical video of the winning hook, H.264 at 30 fps, under 50 MB, a cover cut from the headline frame, the call to action held for the last 3 seconds. Meta's processing silently cut Givi's 22-second videos to 4-16 seconds, losing the end screen with the offer. One file re-encoded from 60 fps to 30 fps kept its full length, but later 30 fps uploads still came back about a second short, so the cause is unproven: encode at 30 fps as a precaution and check the processed length on every upload. **(learned the hard way)**
- **Research hooks first** with `ads_library_search`. Givi's winning pattern appeared only in its sixth round of statics. **(recommended, not tested by us)**
- **Copy rules:** one currency per ad, matching checkout; no invented reviews or customers; no competitor names in ad text; a written basis for every value claim (UK CAP Code); a free-trial ad states its conditions in the ad or on the first click (card required, when and how much it charges, auto-renewal, how to cancel); nothing the product has not done live. Givi's videos showed "helper" sub-agents that had happened zero times in production. On Meta about 125 characters of primary text show before "See more", and about 27 of a headline on a phone.
- **A copy linter as a launch gate.** A short script reads every live and paused ad body, headline and sitelink (`ads_get_creatives` for Meta) and fails on a second currency symbol, a retired offer string or a claim not on the "proven live" list. Run it before every publish and on every change to the offer file. A ten-line grep would have caught Givi's "£1,000+ ... $49" ads and the stale price. **(recommended, not tested by us)**

---

## 6. Building the Meta campaign with the Meta Ads MCP

Meta released an official Ads MCP server in open beta in April 2026 (checked 13 Oct 2026):

```bash
claude mcp add --transport http --client-id <META_APP_ID> meta-ads https://mcp.facebook.com/ads
# then /mcp in Claude Code and sign in with Facebook; grant the venture's ad account only
```

It needs a Meta developer app with the "Create & manage ads with ads MCP server" use case. It is also available as a connector in Claude on the web and desktop. Givi used it from day 19. **(done on Givi)**

**Permissions.** Pre-allow the read tools and paused creates of campaigns, creatives and ads. Never pre-allow `ads_activate_entity`, `ads_create_ad_set` (it carries a budget), `ads_update_entity` (it can change budgets and status) or any Graph call that sets `status=ACTIVE`; those run only after the founder names the number and says go. The founder's Facebook login often already manages other ad accounts, so pin the venture's ad account ID in an access file and check the ID and name before every write. Givi's agents opened the wrong portfolio first. **(learned the hard way)**

**Build order (about 10 minutes):**

1. **Upload creatives.** `ads_creative_upload_local_image(ad_account_id, image_name=<exact file name>, mime_type)` returns an upload URL and a completion token; send the bytes in 1 MB chunks with curl or a small script; then `ads_finalize_local_ad_image_upload(completion_token)`. Name the file exactly as registered: two Givi uploads failed on a name mismatch. Check every video's processed length with `ads_get_ad_videos` and fail if it is shorter than the local file. Write this as one helper script, once.
2. `ads_create_campaign`: objective `OUTCOME_TRAFFIC`, end date at the end of the test.
3. `ads_create_ad_set` (after the founder's number): daily budget at that number, the one country, age 25+ for a business product, Advantage+ audience stated explicitly, no Instagram Explore placement (retired), no Audience Network, optimise for landing page views.
4. `ads_create_creative`: `page_id`, `instagram_user_id` from `ads_get_ig_accounts`, link, primary text, headline, call to action `SIGN_UP`, `image_hash` or `video_id`.
5. `ads_create_ad`, one per creative, status paused. If placement asset customisation is off on a new account, each aspect ratio becomes its own ad.
6. Pixel tracking on each ad with `ads_update_entity` (`tracking_specs`).
7. Audit with `ads_get_ad_entities(object_state='draft', level='ad')`, and save `ads_get_ad_preview_screenshot` for every ad in Feed, Stories and Reels. These would have shown Givi's mixed-currency hook and missing end screens before publishing. **(recommended, not tested by us)**

**MCP writes land as drafts.** On Givi a pause or status change through `ads_update_entity` was staged as a draft and did nothing until published. After any change, re-read `effective_status`. For an urgent pause use the Graph API directly (`POST /v24.0/<ad_id>` with `status=PAUSED`, manager token) and read the status back. **(learned the hard way)**

**Three publish errors Givi hit at launch**, each fixed with `ads_update_entity`: a pixel `promoted_object` not valid for the traffic objective (remove it; Meta still uses the pixel on the ads), the retired Instagram Explore placement (drop it), and the Advantage+ audience setting not stated (state it). After activating the campaign, its draft ads still needed "Review and publish" per ad set in Ads Manager. **(done on Givi)**

**Campaign structure for a small budget:**

- One campaign, one ad set, broad targeting, 2-3 statics in that ad set. Keep the other statics you made (3-5 in all) as replacements.
- Expect Meta to put most of the money on one ad within a day (about 96% on Givi) **(done on Givi)**. That concentration is your winner signal: keep that ad, cut the one short video from its hook, and swap a replacement in for any ad that trips the day-1 rule. The sign-up verdict still comes from your server funnel, stated with its sample size.
- **Never create a Meta A/B test object** (`ads_experiment_abtest_create_test`). It starts at the next midnight, so Givi's ads sat in "Preparing" with nothing spent for about a day, and at £10-15 a day it could never reach significance anyway. The agent proposed it in the same message in which it wrote that no page could win on sign-ups at this budget. **(learned the hard way)** A real split needs about 1,000 visitors per arm within 14 days and at least about £20 a day; below that, change one thing at a time.
- Before merging or restructuring ad sets, confirm no experiment is running with `ads_experiment_list_tests`.

---

## 7. Pre-flight and launch

**The day before:** publish one test ad set with status **paused** to surface API-versus-UI errors without spending; open every final URL and confirm its source shows on your funnel page; run the copy linter; clear every Billing hub notice and read back the spending limit; install the delivery alarm (section 8) and fire it once on purpose; re-run the in-app sign-up check on the latest release.

**Launch in daytime,** on the founder's budget number and their dated "go", given in the chat of the session that will switch the ads on. Givi launched outside working hours **(learned the hard way)**. Then immediately: `ads_activate_entity` on the campaign; `ads_get_errors` on its IDs; `ads_get_ad_entities` for `effective_status`; fix errors with `ads_update_entity`; publish remaining drafts in Ads Manager; confirm "In review" or "Active". Set a one-shot check at +2 hours and +24 hours inside the session (Claude Code's `CronCreate` is fine for that). The daily alarm must not live there.

---

## 8. The delivery and billing alarm

"Active" only means the switches are on. On Givi, Meta could not place its small temporary hold on the card, so nothing was delivered for about two days while every ad showed Active. `ads_get_errors` showed nothing; the notice appeared only in the Billing hub. **(learned the hard way)**

**The rule:** if impressions are 0 for 2 hours while any ad is Active (daytime in the ad account's time zone), or nothing has been spent by mid-morning, raise one alert. The alarm is a fixed-rule script, never an agent's judgement in words. On Givi the morning check called £0 "probably normal for a test's first morning", and another day counted 34 ad-review robot page loads as proof that ads were running. **(learned the hard way)**

**Where it runs:** on a scheduler that survives a sleeping laptop and a closed agent session: a Claude Code cloud routine (`/schedule`), a scheduled GitHub Actions workflow, or a cron service on your hosting platform. Give it a heartbeat (for example a Healthchecks.io ping at the start and end of each run) so a dead or hung alarm is noticed too. It holds only the read-only token. Givi's watchdog was a `CronCreate` job, which lives only inside the session that made it, fires only while that session is idle and expires after 7 days. It died with its session about an hour after the second billing outage began. **(learned the hard way)**

```python
# hourly; env: META_READ_TOKEN, AD_ACCOUNT (act_...), ALERT_URL, HEARTBEAT_URL
import os, json, urllib.parse, urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo
G = "https://graph.facebook.com/v24.0"   # versioned; check Meta's changelog
T, A = os.environ["META_READ_TOKEN"], os.environ["AD_ACCOUNT"]
HOUR = "hourly_stats_aggregated_by_advertiser_time_zone"

def get(path, **params):
    q = urllib.parse.urlencode({k: json.dumps(v) if isinstance(v, list) else v
                                for k, v in params.items()})
    req = urllib.request.Request(f"{G}/{path}?{q}", headers={"Authorization": f"Bearer {T}"})
    return json.load(urllib.request.urlopen(req, timeout=30))

def alert(text):
    req = urllib.request.Request(os.environ["ALERT_URL"], json.dumps({"text": text}).encode(),
                                 {"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=30)

urllib.request.urlopen(os.environ["HEARTBEAT_URL"] + "/start", timeout=10)
acct = get(A, fields="account_status,disable_reason,timezone_name,spend_cap,amount_spent")
now = datetime.now(ZoneInfo(acct["timezone_name"]))
active = get(f"{A}/ads", fields="id", limit=1, effective_status=["ACTIVE"])["data"]
rows = get(f"{A}/insights", date_preset="today", fields="impressions", breakdowns=HOUR)["data"]
recent = {f"{h:02d}:00:00" for h in (now.hour, now.hour - 1, now.hour - 2) if h >= 0}
recent_imps = sum(int(r["impressions"]) for r in rows if r[HOUR][:8] in recent)
if acct["account_status"] != 1:
    alert(f"Meta ad account status {acct['account_status']}: open Billing & payments now")
elif active and 9 <= now.hour <= 21 and recent_imps == 0:
    alert("Ads Active but 0 impressions for about 2 hours: check the Billing hub. "
          "First fix: 'Try again' on the notice, or make the backup card primary.")
urllib.request.urlopen(os.environ["HEARTBEAT_URL"], timeout=10)
```

Treat this as a starting sketch **(recommended, not tested by us)**. `account_status` 1 means active; other values (unsettled, in grace period, pending review) also mean trouble. It only applies the 2-hour rule between 09:00 and 21:00 in the ad account's time zone, because a small budget can deliver nothing at night. Send the alert to wherever the founder already reads things: the product's own notifications, a Telegram bot or a Slack channel for the venture.

**When it fires:**

1. The agent reads the notice in the Billing hub (Billing & payments > payment activity) in the founder's signed-in browser.
2. **First fix: "Try again" on the notice, or make the backup card the default.** Both are free, reversible card actions, so the founder clicks or says yes. Prepaying is only a backstop: on Givi the agent advised a £100 prepay, yet about £70 of prepaid funds later failed to lift an identical block, and "Try again" cleared it in about 5 minutes. **(learned the hard way)**
3. **Verify every founder action.** When the founder says "done", poll insights in the background until impressions rise, and only then report "fixed". On Givi the agent moved on after a "done", and delivery stayed at zero for about six more hours. **(learned the hard way)**

---

## 9. Running the test and reading it honestly

**Every morning (5-25 minutes, by the session that owns the ads):**

- Billing hub, then delivery from the API (`ads_get_ad_entities` with `date_preset=yesterday`, `ads_insights_performance_trend`, `ads_insights_anomaly_signal`, `ads_get_errors`).
- `ads_account_get_activity_logs`: only one session owns the ad account. On Givi two sessions moved it in opposite directions on one evening. **(learned the hard way)**
- Stop-rule progress (spend against the cap, landing visits against 150, sign-ups), then per-ad spend, click-through and server funnel per `utm_content`.
- Ad comments: hide hostile and spam ones through the Graph API, and pause an ad that draws them.
- Message the founder only for problems, money above the approved amount, or a change to the plan.

**Reading the numbers:**

| What you see | What it usually means |
|---|---|
| Platform "landing page views" far above your server's real visitors (Givi: about three times as many) | Accidental taps, slow in-app loads, bots. Decide on server counts |
| Visitors before any impressions | Ad-review robots. Filter them |
| Hourly visitors when nobody is marketing | Cloud scanners posing as phones. Count only after an interaction or 15 seconds |
| A cheap market with huge click counts | Accidental taps and bots. Givi's India, Philippines, South Africa and Nigeria ad set cost about £0.01 a click; add an age floor of 25 and judge on cost per sign-up |
| Pixel conversions far below server sign-ups | The consent gap. Use server counts; optimise for landing page views |
| Google campaign and keyword missing from your data | Tracking parameters placed after a `#`. Givi's final URL ended in `#uk`, so Google appended its parameters after the fragment and they never reached the server |

**UTM placement:** `https://yourdomain.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=<channel-market>&utm_content=<ad>`, any `#anchor` last; lint final URLs for `#` and test Google's tracking template with Ad Preview. Every number states its source and the time it was read: Meta's, your server's and your analytics' "visitors" are three different numbers.

**Changing the offer mid-test:** pause every paid channel first and read back `effective_status`; update the offer file; switch the site; create new ads (published Meta ad text cannot be edited) and set the superseded ones to deleted so nobody can re-enable them; hold the new ads paused until the site shows the new offer; grep live and paused ads on every platform for the old line. On Givi the site changed price at 13:37 and the ads were paused only after 18:00, when the founder noticed. **(learned the hard way)**

---

## 10. Google Ads (search first)

Only if planned; before 3 payers the capped test is Meta. Givi's Google results: about $30, about $3 a click, mostly junk searches until negatives went in, zero sign-ups.

**Account (about 30 minutes, agent driving the founder's signed-in browser):**

- Create it under the venture's own brand Google login. Givi's sat under a login that already managed other ad accounts, and the guided setup kept offering an unrelated profile. **(learned the hard way)**
- ads.google.com > New account > **Switch to Expert Mode** > **Create an account without a campaign**, so Google does not walk you into a Smart campaign. Type the site and name instead of accepting pre-fills; set country, time zone and currency (permanent) before the payment form. The founder enters the card.
- **Turn off auto-applied recommendations** that change bids, budgets, keywords or targeting (Recommendations > Auto-apply).
- **Advertiser verification** (Billing > Advertiser verification) and **identity verification**: the founder starts both the same day. Organisation accounts need a registration document and the representative's photo ID, and the business name must match the payments profile exactly. Google says verification can take up to 30 days. Until it passes, the ad shows a placeholder globe instead of your logo, and Givi's account was told identity verification would be required for any change from 24 Oct 2026. **(done on Givi)**
- Caps: there is no prepaid hard cap on card billing. Google may spend up to twice a daily budget on one day, never more than about 30.4 days' worth in a month. Write the sum of campaign budgets next to the monthly cap.

**Campaign (about 5 minutes once researched):**

- **Keyword Planner first, on day 0.** Under about 500 searches a month for the core terms means small brand and competitor-alternative groups only. Givi ran it on day 3 and found about 40 UK searches a month for its main term. **(learned the hard way)**
- Search only, with Search Partners and Display unticked; phrase and exact match set explicitly (the default is broad).
- **Negatives on day 1:** jobs, hiring, salary, career, course, training, free, download, template, meaning, "what is", homework, essay, girlfriend, and consumer chatbot names and misspellings (chatgpt, chat gpt, chat got, gemini, claude, copilot). Givi spent over half its first Google budget on consumer chatbot searches before 43 negatives went in. **(learned the hard way)**
- Max CPC at or above Keyword Planner's top-of-page estimate. Givi's $4 cap under a $6-16 market gave zero impressions for 9 hours. **(learned the hard way)**
- A sign-up conversion action, 4-6 sitelinks you write yourself with their own `utm_content`, competitor names in keywords only, an end date. Read the search terms report every morning in week 1.

**Agent routes for Google.** For routine reads, pauses and alerts, use Google Ads Scripts (Tools > Bulk actions > Scripts: free, inside the account, no quota) and automated rules for budget and CPC guards. Apply for a Google Ads API developer token (Tools > API Center, in a manager account) if the agent will manage Google often; approval takes days. Givi built through the Adspirer MCP, which was fast, but its plan then allowed 15 calls a month including reads, and the quota ran out mid-crisis, so an emergency pause was done in the UI with Claude in Chrome. **(learned the hard way)**

---

## 11. TikTok Ads

Skip it for a business-owner product until Meta converts. Givi's cold TikTok traffic gave 76 clicks for about £25, under 0.5% click-through, and zero engaged visitors. Givi never ruled out that TikTok's in-app browser blocked the visit counter, but nobody clicked sign-up either way. **(learned the hard way)**

If it fits (consumer or creator products):

- The founder creates the TikTok Business Center and ad account (currency, time zone), verifies the phone, and links the brand's TikTok account as the ad identity on the same day. Givi's launch was blocked because the identity was not linked. **(learned the hard way)**
- **Prepay a fixed amount** (manual payment): ads stop when the balance runs out, which works as a hard cap. **(done on Givi)**
- Minimums: about $20 a day per ad group (or $50 if the budget sits at campaign level), so a £50 prepay lasts about 3 days at the ad-group minimum. TikTok says most ads are reviewed within 24 hours; Givi's took more than 6 hours, and every edit goes back to review.
- Build in the UI with Claude in Chrome in the founder's own browser (TikTok blocks the gstack browser). Website traffic objective, landing page views, the pixel, budget on the ad group, TikTok placement only (untick partner apps), identity set to "Only show as ads", one call to action.
- **Before publishing,** remove TikTok's AI-suggested text and auto-added "selling points" (Givi's ad was given "5-Star Reviews", "Top Seller Ranking" and "Fast & Free Shipping", none true), and switch off automatic enhancements that replace music and dub audio. **(learned the hard way)**
- Never use a tool that creates TikTok campaigns live; Adspirer's did, so Givi built by hand.

---

## Tools

| Task | Use | Avoid |
|---|---|---|
| Account standing and billing | Claude in Chrome on the founder's browser, reading Billing & payments and Account Quality | Guessing at browser anti-fraud |
| Build and check Meta | Meta Ads MCP create tools (all paused), `ads_get_ad_entities`, `ads_get_ad_preview_screenshot`, `ads_get_creatives` | Clicking in Ads Manager, except "Review and publish" |
| Switch on | `ads_activate_entity`, only after the founder's number and go | Pre-allowing it |
| Delivery alarm | Cloud routine, scheduled CI job or host cron, with a heartbeat | `CronCreate`, a laptop, an agent session |
| Google edits, pauses, alerts | Google Ads Scripts and rules; the API once a developer token exists | A quota-limited MCP for daily reads |
| TikTok | Claude in Chrome in the founder's browser | Headless browsers; tools that create live campaigns |

## What needs the founder

| Task | Minutes |
|---|---|
| Pay balances on other ad accounts (the agent lists them with links) | 5 |
| Portfolio, Page and Instagram, on their phone, from a field sheet (sitting S1b) | 15 |
| Business Verification, ad account, cards, prepay, spending limit, second admin, tokens, MCP sign-in | 40, in sitting S2 |
| Real-phone in-app sign-up test, real card checkout and refund (sitting S3b) | 10 |
| Google Ads card, advertiser and identity verification (only if Google is planned) | 20 |
| Budget number, dated override and "go" | 2 |
| "Try again" or switching the default card, when the alarm fires | 1 |

## Checklist

- [ ] Funnel gate run by a session that does not own the ads: in-app user-agent screenshots including the OAuth consent screen; real-phone sign-up in Instagram, Facebook and TikTok; no Google sign-in in webviews; real card checkout and refund seen in Stripe and the database
- [ ] At least 20 organic Start clicks, 25% or more reaching an account, humans only, server-counted
- [ ] Warm outreach already sent; founder's dated override recorded if before the first payer
- [ ] Offer frozen in one file; no price or trial terms in any image or video; copy linter passes
- [ ] Stop rule, budget and verdict metric written down in the checkout currency
- [ ] No balance due on any ad account the founder administers
- [ ] Portfolio decided on purpose; Page and Instagram created by the founder; Instagram linked to the ad account
- [ ] Ad account in the checkout currency and right time zone; own card, backup card, prepaid balance; one small charge passed; Billing hub clean
- [ ] Account spending limit set and `spend_cap` read back; real daily limit read
- [ ] Second admin; domain verified; pixel dataset connected to the ad account
- [ ] Reader token (`ads_read`, never expires) on the server and in the alarm; manager token (60 days) in the keychain only, with a renewal reminder
- [ ] Meta Ads MCP authorised; reads and paused creates allowed; activation and budgets never pre-allowed; writes pinned to the venture's ad account ID
- [ ] Consent banner with equal-weight buttons; pixels only after Allow; Consent Mode v2 if Google runs; server-side events for consenting visitors
- [ ] Humans-only funnel per `utm_content` with one robot filter; consent gap measured on day 1
- [ ] 3-5 statics made; one campaign, one ad set, broad targeting, 2-3 statics in it, all built paused; video lengths checked; previews saved; no Meta A/B test object
- [ ] The ad Meta concentrates spend on treated as the winner; replacements swapped in for paused ads; one short video only after a static wins
- [ ] Paused test publish the day before; final URLs seen on the funnel page; no `#` before parameters
- [ ] Delivery alarm on a durable scheduler with a heartbeat, fired once on purpose
- [ ] Daytime launch on the founder's number and go; errors and drafts cleared; +2 h and +24 h checks set
- [ ] Every day: impressions from the API, Billing hub read, stop-rule progress printed, comments read, Google search terms and negatives (if Google runs)
- [ ] On a hold: "Try again" or switch the default card first, then poll until impressions rise; every founder "done" verified
- [ ] On an offer change: all paid paused first; new ads created, old ones deleted; new ads held paused until the site shows the offer; every platform grepped for the old line
