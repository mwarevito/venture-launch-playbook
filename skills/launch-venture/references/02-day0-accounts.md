# Day 0 accounts: every account a new online business needs, in dependency order

Every outside account a new online business needs, created from nothing, in the order that avoids waiting: domain and DNS, a brand mailbox and email authentication, code, hosting, database, payments, model keys, social handles, ad accounts and the company verifications behind them. Each recipe gives the reason, the console steps, what only the founder can do, the usual wait, what went wrong for us, and how to check it worked.

**Done when:** every account your venture needs exists under the venture's own identity and its own card; every long-lead verification shows "In review" or "Verified"; a test email to hello@ arrives, and a test email from your product passes SPF, DKIM and DMARC; and one access register lists each account's owner, second admin and spending limit.

Console paths, prices and review times were checked against official documentation on 13 Oct 2026. They change, so re-check a number before you rely on it. More detail: payments in `06-payments-stripe.md`, ads in `10-paid-ads.md`, verifications and app reviews in `11-platform-approvals.md`, the company in `14-company-legal.md`.

## How to read this file

Evidence tags: **(done on Givi)** we did it and it worked; **(learned the hard way)** we did it wrong first; **(recommended, not tested by us)** from documentation or best practice.

Two rules sit under every recipe:

1. **Reuse nothing that holds money.** Each venture gets its own card, hosting workspace, model-provider account and ad accounts. On Givi, a small unpaid balance on an ad account from another of the founder's businesses made Meta refuse every new card and the Facebook Page for about 2.5 days, and the AI model credit was a pool shared with another live product that nearly ran dry on launch night. **(learned the hard way)**
2. **One access register, read before anything is created.** Two agents working in parallel on Givi created two Google Cloud projects under two different Google accounts 90 minutes apart, and one recommended an email service the other had wired the day before. **(learned the hard way)**

## The dependency chain

Some accounts need something that does not exist yet. That is why the founder's time is split into three sittings (end of this file).

| You need first | Then you can create |
|---|---|
| Nothing | Password manager, venture card, GitHub, hosting, database, email-sending account, model keys, Stripe in test mode, the company filing |
| A screened name | The domain, then the DNS token, then the brand Google account and hello@, then every account that signs up with hello@ (social handles, tool vendors, Search Console) |
| The company number (UK: usually within about 24 hours of filing) | Business bank account, Meta Business Verification and the ad account, Stripe activation, D-U-N-S and Google advertiser verification |
| The business bank account | Stripe payouts, so Stripe activation and the live key |
| Live privacy and terms pages and your own auth domain | Google OAuth branding ("Continue with Google" showing your name), Meta app settings, directory listings |
| A clean payment history on the founder's Meta profile | The Facebook Page, the ad account and cards on it |

## Before any account: agent prep (about 1 hour, no founder time)

- **Access register.** A file in the venture repo (we use `operations/ACCESS.md`), one row per account: service, purpose, owning login, workspace ID, browser profile, monthly cost, spending limit, alert, recovery route, second admin and blast radius (what else stops if this account is restricted or runs dry). Names and IDs only, never secret values. Every agent reads it before creating anything and adds a row in the same turn. **(recommended, not tested by us; its absence cost us twice)**
- **Company facts file.** `legal/identity.md`: legal name exactly as registered, number, registered office, trading name, support email, business phone, VAT status, D-U-N-S, base currency. Every form copies from it. On Givi an agent told the founder the venture had no company 18 days after it was incorporated, because nothing written said so. **(learned the hard way)**
- **Field sheet.** Every value the founder will type in the sittings: page names and categories, bio (brand line plus domain, no price), website, ad-account name, currency (permanent on Meta and Google, so use your checkout currency), time zone, legal name and address, VAT status.
- **Account-standing check.** Read-only: billing on every Meta ad account the founder administers, which Google login holds which Google Ads account, GitHub billing, restrictions on Stripe or hosting. Debts go first in sitting S1a.
- **Secret hand-off scripts.** Per key, a small Desktop script (`.command` on macOS) that reads the clipboard, checks the key's shape, tests it with the provider, stores it, clears the clipboard, prints only "accepted" and deletes itself, dry-run first with a dummy value. Keys never go through chat. **(done on Givi; the dry run was learned the hard way after two scripts failed silently)**

## Sitting S1a, day 0: accounts that need no name

### 1. Password manager, 2FA and a second admin

- **Steps:** one store. 1Password with its `op` CLI and a service account lets agents read a key by reference (`op read op://<vault>/<item>/<field>`); the macOS Keychain works too (`security add-generic-password -U -a <venture> -s <item> -w` to save, `security find-generic-password -a <venture> -s <item> -w` to read inside the command that uses it). Authenticator-app 2FA wherever offered; backup codes saved as each account is created.
- **Founder only:** passwords, 2FA, naming a second admin (a co-founder or someone trusted, with their own 2FA).
- **Gotcha:** on Givi nothing recorded where recovery codes lived. **(learned the hard way)**
- **Verify:** the register's recovery and second-admin columns are filled for every row.

### 2. A separate card for this venture

- **Steps:** a new virtual card from a business bank, labelled with the venture's name. Until the venture's own company and bank exist, use a virtual card from an existing business account, dedicated to this venture. When the company card arrives, one tracked task lists every account to switch.
- **Founder only:** issuing the card and entering it.
- **Verify:** every register row that charges money names this card.

### 3. GitHub: organisation, private repo and an Actions budget above zero

- **Steps:** a GitHub organisation for the company (so the code belongs to the company), then `gh repo create <org>/<venture> --private`. In the organisation's billing settings > Budgets and alerts, set an Actions budget above $0 (about $10-30 a month is plenty) and scope it to this repository, so a "stop usage" limit on one venture never stops another's CI.
- **Founder only:** the card and the amount (2 minutes, page already open).
- **Gotcha:** Givi's hosted CI was blocked by a billing failure for about 7 days, then stopped again by a $0 Actions budget with "stop usage" on. A new card did not lift it, and CI was switched off for the rest of the launch. Open the exact budgets page before advising anyone. **(learned the hard way)**
- **Verify:** a trivial pull request runs the real tests and goes green.

### 4. Hosting: Railway workspace with a hard limit

- **Steps:** a new workspace named after the venture (never shared with another product: the hard limit applies to the whole workspace), a paid plan, the venture card. At railway.com/workspace/usage set an email alert and a hard limit; at the hard limit Railway takes every workload in the workspace offline, after warnings at 75%, 90% and 100%. Create the project, name the live environment `production`, create a project-scoped deploy token, and write the IDs into the register.
- **Founder only:** the card and the two amounts.
- **Gotchas:** Givi's live environment was called `staging` for its whole life and confused every new session. Our first token was account-wide and could open projects in another workspace; a separate workspace separates billing, not credentials, so test each token against a project it should not reach. **(learned the hard way)**
- **Verify:** `railway whoami`; `railway status --json` shows the right workspace, project and environment.

### 5. Database and auth: Supabase organisation with the spend cap on

- **Steps:** a new organisation for this venture, created directly at supabase.com; check the Spend Cap is on (organisation > Billing > Cost Control) so overage is blocked rather than billed. Create the project in a region chosen on purpose and record it in `legal/vendors.md`: privacy pages and Meta's data-handling form ask for it. Run `supabase login` once so agents use the CLI and Management API, not the dashboard. A custom auth domain (`auth.yourdomain.com`, so Google's sign-in screen never shows a supabase.co address) needs a paid plan plus an add-on.
- **Founder only:** the plan and the card.
- **Verify:** `supabase projects list` shows the project; a Supabase MCP connection scoped to it can read it.

### 6. Email-sending account: Resend

- **Why:** sign-in codes and product email. Supabase's built-in mailer sends only to your own team, a handful an hour. Outside testers on Givi could not get sign-in codes for two days until this was fixed. **(learned the hard way)**
- **Steps:** a new Resend account per venture (sign in with GitHub or Google); the free plan's limits are per account. Create one full-access API key, store it through its script; the agent makes every narrower key from it by API. The domain comes after S1b (section 12).
- **Founder only:** signing up and accepting the terms.
- **Verify:** `GET https://api.resend.com/domains` with the key answers 200.

### 7. AI model keys with spend caps

- **Steps:** one provider account or organisation per venture, never shared with another live product.
  - **OpenRouter:** credit, auto top-up, and keys with a credit limit and a reset period. A management key creates capped keys by API (`POST /api/v1/keys` with `limit` and `limit_reset`), so each customer or feature gets its own cap.
  - **Anthropic (Claude Console):** Organization settings > Billing > Spend limits; a lower limit per workspace.
  - **OpenAI Platform:** Settings > Organization limits > Spend, and per project Settings > Project settings > Limits > Spend. Alerts only email you; a hard limit makes requests fail with a 429.
  - A separate small-capped key for the agents' own tests.
- **Founder only:** the card, top-up amount and limits.
- **Gotcha:** Givi's credit came from a pool shared with another live product. On launch night it fell below $10, paid calls were frozen for about 19 hours, and the other product's paying customers were at risk. There was no balance alert. **(learned the hard way)**
- **Verify:** a test call per key; the balance shows in the daily digest; a key over a tiny cap is refused.

### 8. Stripe in test mode

- **Steps:** create the account at dashboard.stripe.com (it starts in test mode). Install the Stripe CLI and run `stripe login` once: one browser confirmation, and the agent gets test keys without the founder copying anything. Check any Stripe connector with one read call. Activation is in S2 (section 17); full recipe in `06-payments-stripe.md`.
- **Founder only:** creating the account.
- **Gotcha:** a Stripe plugin installed but never authorised answered "user not logged in". **(learned the hard way)**
- **Verify:** `stripe get /v1/account` answers in test mode.

### 9. The company filing (only if you need a new company)

Every later verification needs a registered company; UK online registration usually completes within about 24 hours. The founder files it on day 0, as the last item of S1a (steps in `14-company-legal.md`). On Givi the company existed 6 days after we decided to form one, and every company-gated step waited behind it. **(learned the hard way)**

## Sitting S1b, within 2 hours of the name pick

### 10. Domain and DNS on Cloudflare

- **Steps:**
  1. Agent, before the sitting: bulk-check 8-10 .com variants against the registry (`GET https://rdap.verisign.com/com/v1/domain/<name>.com`; 404 means unregistered) and the handle on every network in one pass; drop variants with a same-name live product; run the trade mark screen in `14-company-legal.md`. Check every option you recommend; on Givi a .ai alternative was suggested and never checked. **(learned the hard way)**
  2. Founder: dash.cloudflare.com > Domain Registration > Register Domains, on the venture card. Cloudflare sells at list price with no markup and keeps DNS and Email Routing in one account; auto-renew is on by default. Confirm 2FA on the login.
  3. Founder, same visit: My Profile > API Tokens > Create Token > template "Edit zone DNS", zone = this domain only; copy it and double-click its hand-off script.
  4. Agent: all DNS through the API (`GET /zones?name=<domain>`, then `POST /zones/<id>/dns_records` with `"proxied": false`), or a BIND zone file uploaded at DNS > Records > Import and Export.
- **Founder only:** payment and the token. **Wait:** minutes.
- **Gotchas (all learned the hard way):**
  - Every CNAME pointing at Railway, Supabase or Resend must be **DNS only** (grey cloud). Proxied records broke certificate issuance and showed a Cloudflare 404. If `dig` returns 104.21.x.x or 172.67.x.x, the record is proxied.
  - Cloudflare's dashboard blocks automated browsers and its sign-ins expired within days; the stored token is the reliable route. Givi got it a week late, re-pasted it for each change, and needed the founder in Cloudflare eight separate times where two batches (S1b and one later) would have done.
  - Validate the token by listing the zone. User tokens verify at `/user/tokens/verify`, account-owned tokens at `/accounts/<id>/tokens/verify`; calling the wrong one returned an error for us.
- **Verify:** `dig NS <domain> +short` shows Cloudflare; a test TXT record the agent creates resolves at `@1.1.1.1` and `@8.8.8.8`.

### 11. The brand mailbox: a brand Google account or Google Workspace

You need an inbox for hello@ (plus support@, privacy@ and a named address such as yourname@, since some partner programmes refuse role addresses) and a Google identity that owns the brand's YouTube, Google Ads, Google Cloud and Search Console. Two routes:

| | A. Free brand Google account plus Cloudflare Email Routing | B. Google Workspace |
|---|---|---|
| Cost | $0 | Per user per month (below) |
| Receiving | Cloudflare forwards each address to the brand account's inbox | Real mailboxes; aliases and groups free |
| Sending as hello@ | Only through Gmail "Send mail as" with an outside SMTP server, which Google is retiring (below) | Native |
| More than one person | Forward to each; no central control | A licence each; remove access in one place |
| Best for | A solo founder testing an idea who rarely replies by email | Anyone who will answer customers by email, two or more people, or buyers who expect a proper business mailbox |

**The rule:** a free brand Google account plus forwarding (route A) is fine for a short test. Move to Google Workspace (route B) once you answer customers by email, because Gmail's "Send as" through another provider's SMTP is being retired: Google says Gmail stops supporting "Send as" for third-party addresses from January 2027 and has started restricting new setups (checked 13 Oct 2026). Route A keeps receiving hello@ but will not be able to reply as it, so until you move, replies come from the brand Gmail address or from your product. Move earlier if two people share the inbox or you need to remove access cleanly. The root MX records point at Email Routing or at Google, never both; switching means turning Email Routing off and replacing MX and SPF.

#### Route A: free brand Google account plus Email Routing (done on Givi in part)

1. Founder: in a browser profile signed out of every Google account, create a new Google account at accounts.google.com/signup named after the venture; phone verification, password manager, 2FA.
2. Agent: Cloudflare > your domain > Email Routing (the docs now file it under Email Service) > Get started; accept the MX, SPF and DKIM records it proposes. Add the brand account as the destination; no rule saves until the verification link Cloudflare sends is clicked (by the founder, or by the agent once it can read that inbox through a Gmail MCP).
3. Agent: Routing rules > Create address for `hello`, `support`, `privacy` and the named address, each "Send to an email" to the brand account. Test after Routing status shows Enabled.
4. Replies as hello@: until Google retires it (January 2027), Gmail's Settings > See all settings > Accounts and Import > Send mail as > Add another email address can send through `smtp.resend.com`, port 465, username `resend`, password = a sending key restricted to your domain. Google may already refuse a new setup, so treat this as a stopgap and plan the move to route B. **(recommended, not tested by us)**
5. Founder, once the logo is locked: set it as the account's profile photo at myaccount.google.com; Gmail shows it as the sender avatar (the alternative, BIMI, needs a registered trade mark).

- **Gotchas:** the first test right after saving a rule bounced with "550 5.1.1 Address does not exist"; wait for Enabled. Never forward hello@ to a personal inbox or another company's: on Givi it forwarded into another business's mailbox for weeks, where privacy and deletion requests would have landed and no agent could read them. **(learned the hard way)**

#### Route B: Google Workspace (recommended, not tested by us; from Google's documentation, checked 13 Oct 2026)

1. **Sign up in a clean browser.** Open workspace.google.com in a browser profile signed out of every Google account. Of the three signup paths (a Gmail address, an unverified business email, a domain you own), choose **the domain you own** and create the first admin as a new address on it (`you@yourdomain.com`), with a recovery address outside the domain. The 14-day free trial covers up to 10 users; add billing before it ends or the account is suspended. Business Starter was $7 per user per month on the annual plan or $8.40 flexible (USD), and £5.90 or £7 (GBP, excluding VAT), when we checked; see workspace.google.com/pricing.
2. **Verify the domain.** Admin console > Account > Domains > Manage domains > Verify domain gives a TXT record (`google-site-verification=...`) for the root (a CNAME method also exists). The agent adds it through the token and presses Verify; usually minutes, up to 72 hours.
3. **MX.** One record at the root: priority `1`, value `smtp.google.com` (older accounts may still use `aspmx` records, which keep working). Delete every other root MX first, which means switching Email Routing off.
4. **SPF.** One TXT at the root: `v=spf1 include:_spf.google.com ~all`. Only one SPF record per name; another service sending from the root adds its `include:` to the same record. Resend does not need this.
5. **DKIM.** Admin console > Apps > Google Workspace > Gmail > Authenticate email. Google says the key can only be generated 24-72 hours after Gmail is turned on for the domain. Then pick the domain, Generate new record (2048-bit, prefix `google`), add the TXT at `google._domainkey`, and only after publishing press **Start authentication**; allow up to 48 hours for it to take effect.
6. **DMARC.** One TXT at `_dmarc`: start with `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com` so reports arrive, and move to `p=quarantine` after a few weeks of clean reports. Gmail requires SPF, DKIM and DMARC from anyone sending 5,000 or more messages a day to Gmail users, and has rejected non-compliant traffic more strictly since November 2025.
7. **Aliases and shared addresses.** An alias (Admin console > Directory > Users > the user > Alternate email addresses) is free, up to 30 per user, and lands in one person's inbox: fine for hello@ and privacy@ (allow up to 24 hours). A Google Group (Directory > Groups > Create group) is free and reaches several people: use it for support@ once a second person helps, and allow external senders or outside mail bounces. Only a real extra mailbox needs a licence.
8. **Profile photo.** Set the logo on the account that sends customer mail.

#### The trap: never turn a personal Gmail into the business account (learned the hard way)

On Givi, an agent in a browser signed in to the founder's personal Gmail clicked Google Admin's "Get set up" and "connect a domain you already own" and entered the venture's domain, on a general "do it all yourself". The next day the personal Gmail was a managed Workspace account with the venture address as primary, and the cancellation screen warned that mail and files would be permanently deleted. A support case and five days later, the founder separated the accounts himself.

Why, per Google's documentation: Workspace can be started "with a Gmail address". If a domain is then verified on that account, the personal Gmail becomes a domain-verified admin account under the custom address; Google Family, Fit and Nest stop working on it, and a super admin can later delete all of it. Any personal account already using an address on the domain becomes a conflicting account to be transferred in or renamed (to a temporary `@gtempaccount.com` name). "This domain is already in use" means some account already holds the domain; use the recovery form, not "free up domain".

Rules:
- Start Workspace signup only in a browser profile signed out of every personal Google account.
- On a personal account, treat "Get set up", "connect a domain you already own", Gmail's prompts to verify your domain for extra features and "Request to free up domain" as irreversible. An agent clicks none of them without the founder's explicit yes to that exact screen; "do everything yourself" is not that yes.
- Create every Google asset (YouTube, Google Ads, Google Cloud, Search Console) under the brand account from the start, and check which account the browser is signed in as before any Google console work.

### 12. Email authentication and the transactional sender (Resend)

Each sender needs its own DKIM record, a name may carry only one SPF record, and the domain has one DMARC record. Keep the root for people's mail; product mail gets its own records.

| Record | Name | Route A (Email Routing) | Route B (Workspace) | Resend |
|---|---|---|---|---|
| MX | root | Cloudflare's three routing MX records, added by Email Routing (often `route1`-`route3.mx.cloudflare.net`; copy what the dashboard shows) | `smtp.google.com`, priority 1 | none at the root |
| SPF (TXT) | root | `v=spf1 include:_spf.mx.cloudflare.net ~all` | `v=spf1 include:_spf.google.com ~all` | none at the root; its own record on its subdomain |
| DKIM | selector | `cf2024-1._domainkey` (added by Email Routing) | `google._domainkey` | `resend._domainkey` |
| DMARC | `_dmarc` | one record for the domain, `p=none` with a `rua` address to start | same | same |

Resend's classic set is a DKIM TXT at `resend._domainkey`, an MX at `send` pointing to `feedback-smtp.<region>.amazonses.com` (priority 10) and an SPF TXT at `send` (`v=spf1 include:amazonses.com ~all`). Domains created since August 2026 may get two CNAMEs instead (at `send` and `rsend`), which is what Givi received. Copy whatever the dashboard or `GET /domains/<id>` shows; the return-path name is fixed when the domain is created. Resend recommends a sending subdomain such as `mail.yourdomain.com`. The free plan allowed 3,000 emails a month, 100 a day (received mail counts too) and 3 domains when we checked.

**Steps (done on Givi in about 35 minutes; DNS verified in about 4):**
1. Agent: Domains > Add Domain (or `POST /domains`), a region near your users (us-east-1, eu-west-1, sa-east-1 or ap-northeast-1; Givi used eu-west-1). Put the records into Cloudflare, all DNS only (a proxied CNAME never verifies), or use Resend's "Sign in to Cloudflare" button. Leave the root MX and SPF alone.
2. Agent: add `_dmarc` if missing, then switch on Cloudflare's free DMARC Management (your domain > Email > DMARC Management) so reports have somewhere to go. Givi published `p=none` with no report address, so it never got a report and can never safely tighten the policy. **(learned the hard way)**
3. Agent: Verify (or `POST /domains/<id>/verify`), retrying while pending; TLS Enforced; tracking off.
4. Agent: create keys by API with sending access restricted to the domain, one for Supabase SMTP and one for the app, piped into place without printing. Receiving mail into the product needs a full-access key; Givi waited 2.5 hours for one later. **(learned the hard way)**
5. Agent: Supabase > Authentication > Emails > SMTP Settings: `smtp.resend.com`, port 465, username `resend`, password = the SMTP key, sender `Brand <hello@yourdomain.com>`. Save, reload, read back.

- **Gotchas:** templates must show the code (`{{ .Token }}`) as well as the link, because links fail when opened on another device; and read the hosted code length before building the sign-in screen (Givi's project sent 8-digit codes to an app that accepted 6). **(learned the hard way)**
- **Verify:** sign out and request a code; Gmail's "Show original" shows `signed-by: yourdomain.com`, the return path on your sending subdomain, and SPF, DKIM and DMARC PASS. Before ads, check an Outlook.com and an iCloud inbox and score one message at mail-tester.com. **(recommended, not tested by us)**

### 13. Tool vendors signed up with the brand account

Anything the product calls (web search, a connected-apps platform, error tracking) belongs to the brand. Sign up with the brand Google account, store each key through its script, record each vendor, the data it receives and its region in `legal/vendors.md`, and make one live test call per key.

### 14. Social handles, in the order that avoids SMS and verification failures

Claim every handle on the founder's phone in S1b. Avatars and bios wait for the logo; bios carry only the brand line and domain, never a price or trial length.

| Order | Network | How | Why this order |
|---|---|---|---|
| 0 | All | Agent checks the handle everywhere the hour the name is picked | Domain and handles match |
| 1 | Facebook Page | Founder creates it in Meta Business Suite inside the portfolio (section 15), on their phone, after the debt check | Automated attempts triggered an SMS check that blocked it for us; do it while the phone is in hand |
| 2 | Instagram | Professional (Business) account, added to the portfolio at once (Business settings > Instagram accounts > Add) | Switching later cost a second round |
| 3 | LinkedIn page | linkedin.com/company/setup/new from the founder's personal profile; agent fills the form, founder clicks Create | LinkedIn may want a profile older than seven days with connections and a work email on your domain, so mail must already arrive **(recommended, not tested by us)** |
| 4 | YouTube | Channel created from the brand Google account with the final name and handle | A channel under another organisation's account could not be moved **(learned the hard way)** |
| 5 | X | Only if your buyers are there | Givi paid for X posting tools and got almost no reach |
| 6 | TikTok | Only if the product fits short video; created in the phone app with the final username and display name | Display name locks for 7 days after a change, username for 30; automated sign-up hit "Maximum number of attempts reached" **(learned the hard way)** |

Agents never automate a social sign-up or type invented identity data into a real form (one typed a placeholder birth date into TikTok; learned the hard way). Set 2FA, recovery codes and the second admin on each network in the same sitting (S1b).

- **Verify:** each profile loads signed out and has a register row with owner and second admin.

> **What happened on Givi.** The Facebook Page failed silently when an agent filled the form, then stalled on an SMS check the founder could not find in his app. Nobody owned the retry, and the Page took about two weeks, blocking ads and Instagram linking; the founder then created it from Business Manager in minutes. TikTok took 11 days and ended up as an old personal account renamed.

### 15. Meta business portfolio (S1b) and the rest of Meta (S2)

- **S1b:** create or choose the business portfolio at business.facebook.com, details exactly as on the company register, then add the Page and Instagram. First the founder pays any unpaid balance on any ad account they administer: Meta treats the person as a payment risk everywhere, and new Pages and cards fail with a vague error. Meta limits how many portfolios one person can create (2, per its help centre when we checked); Givi's founder was at his limit and renamed an empty old portfolio rather than delete one.
- **S2:** Business Verification (Meta Business Suite > Security Center > Start verification), the developer app (make the irreversible Tech Provider choice on purpose), the ad account in your checkout currency (permanent), two payment methods and one small charge before launch day, a spending limit read back through the API, a second admin, domain verification, and two system-user tokens (read-only and never expiring for the server and alarms; a 60-day management token kept only in the secrets store). Steps in `10-paid-ads.md` and `11-platform-approvals.md`.
- **Founder only:** Facebook login and 2FA, creating the Page and ad account (agents' safety checks block that), the ID upload, the irreversible choice, cards.
- **Wait:** about 19 hours on Givi; Meta says up to 14 business days, and changing business details later means verifying again.
- **Gotcha:** upload an original camera photo of the ID, at least 1500 x 1000 pixels. Never upscale or edit an identity image: Givi's upscaled passport photo was followed by "technical issues", and another ID worked. **(learned the hard way)**
- **Verify:** the Meta Ads MCP (`ads_get_ad_accounts`, `ads_get_ad_account_pages`) sees the Page, Instagram and ad account.

### 16. Analytics and watchers (agent, no founder time)

- **Your own server-side funnel:** real visitors, Start clicks, sign-ins, sign-ups and payments per page and per ad in your own database, bots and team excluded. Pixels only see people who accept cookies; with Givi's first small banner that was about 5%. **(learned the hard way)**
- **Cloudflare Web Analytics** as a free, cookieless baseline; **Google Search Console** as a Domain property under the brand account, verified by a DNS TXT the agent adds; **PostHog** for funnels and replays, loaded after consent. **(recommended, not tested by us)**
- **Sentry** for errors and **UptimeRobot** or **Healthchecks.io** for uptime and "the daily job did not run", signed up with the brand account.
- **Verify:** a test visit appears in each; one forced alert arrives.

## Sitting S2, the day the company number arrives

### 17. Business bank account, then Stripe activation

- **Bank first:** Stripe needs a payout account in the company's name to activate, and ad platforms bill the company card. Apply the day the number arrives; plan for days (`14-company-legal.md`).
- **Stripe activation:** the dashboard's activation flow asks for business type and company number, directors and anyone owning more than 25%, a representative's identity, the payout account, industry, website, product description, a support contact, and a statement descriptor (the name on card statements: 5-22 characters, at least one letter, none of `< > \ ' " *`; use your domain or brand so people recognise the charge). Activation is usually near-instant; a document review can take 3-5 business days. Full recipe: `06-payments-stripe.md`.
- **Founder only:** identity, bank details, the descriptor.
- **Verify:** `stripe get /v1/account` shows `charges_enabled` and `payouts_enabled` true.

> **What happened on Givi.** Stripe itself was never the blocker. Live payments came 17 days after the start, mostly waiting for a key to be pasted, and the one real card payment and refund that should gate ad spend was never run before ads went live. **(learned the hard way)**

### 18. Google Ads and advertiser verification (only if Google ads are planned)

- **Steps:** signed in as the brand Google account (never a login that holds another business's ads), create an account at ads.google.com and, at the business-information step, choose to create it without a campaign (Expert mode), so Google does not walk you into a Smart campaign that starts spending. Set country, time zone and currency (permanent; your checkout currency), stop at payment, and turn off auto-applied recommendations that change bids, budgets, keywords or targeting. Advertiser verification asks for organisation details, payment history (a small refunded test charge) and identity by D-U-N-S number or company documents; once Google asks, you have 30 days to start and 30 to finish, or ads are paused. Review takes up to 5 business days.
- **D-U-N-S:** optional for Google, needed for Apple's organisation developer account. Dun & Bradstreet says every UK-registered business gets one automatically, free; look it up at dnb.co.uk when the company number arrives (D&B says it answers requests within five working days; the free US route can take 30 business days). **(recommended, not tested by us)**
- **Founder only:** the card and the verification forms (agents' safety checks blocked typing into them on Givi).
- **Gotcha:** Givi's Google Ads account sat under a login that also manages another business's ads, because the brand had no Google account yet, and verification started 18 days after incorporation. **(learned the hard way)**
- **Verify:** billing shows a payment method and no warnings; verification reads in progress or verified.

### 19. TikTok Ads (only if planned)

In TikTok Business Center and Ads Manager: the ad account (currency, time zone), a small prepaid balance that works as a hard cap, phone verification, and the brand TikTok account linked as the ad identity. TikTok blocks most automated browsers, so check settings through an extension in the founder's own browser. Ad review took more than 6 hours per edit on Givi.

### 20. Other S2 items, where they apply

- The ICO data protection fee and a registered-office provider for a UK company (`14-company-legal.md`).
- Company-owned OpenAI and Claude organisations, with OpenAI Business verification, if you will list in the ChatGPT or Claude directories. Listing ownership cannot be moved later; Givi's Claude listing sits on a personal account. **(learned the hard way)**
- Apple Developer enrolment as an organisation for a mobile app (needs a D-U-N-S number).

## Sitting S3, once there is a public URL

- **S3a, friends go-live:** the founder approves the warm list and the note texts and watches one test send go out (the batches follow; `08-outreach.md`), signs in once in the agents' visible browser window to each network and console so agents can work without asking again, and approves free access for the first testers.
- **S3b, once Stripe is active:** Google OAuth consent screen and branding in the brand Google account (needs live privacy and terms pages and your `auth.` domain; verification was instant on Givi because only name and email are requested), the live Stripe key through its script, one real card checkout and refund by the founder, and a real-phone sign-up test inside the Instagram, Facebook and TikTok in-app browsers. Steps in `05-product-and-infra.md` and `06-payments-stripe.md`.

## The three founder sittings

Identity, cards and approvals go into three sittings, two in halves, because each half needs something the earlier one cannot have. The agent prepares every page and value beforehand. Long-lead items go first, since their clocks start when the founder finishes. Anything that fails (an SMS that never arrives, a captcha limit) becomes a tracked task with a re-check date before the sitting ends.

| Sitting | When | Founder time | What goes in (sections above) | What forces the split |
|---|---|---|---|---|
| S1a | Day 0, after agent prep | 30-40 min | Hand-off test (a harmless script that prints "ok"), old debts, 1-8, then the company filing (9) last | Nothing here needs the name |
| S1b | Within 2 hours of the name pick | 30-40 min | Domain and token (10), brand account or Workspace and the routing click (11), tool vendors (13), Meta portfolio, Page and Instagram (15), other handles (14) | Everything carries the name; the brand account must exist before anything signs up with hello@ |
| S2 | The day the company number arrives (merges into S1a and S1b if you reuse a company) | 30-45 min | Bank first, then Stripe activation (17), the Meta path with verification and tokens (15), Google Ads and D-U-N-S (18) and TikTok (19) if planned, the company items (20) | Every verification needs a registered company; Stripe needs the bank |
| S3a | Friends go-live, usually day 2 | 15-20 min | Warm list and texts approved, one test send, sign-ins in the agents' visible browser, tester access | Needs a working product |
| S3b | Stripe active, usually day 3-4 | 15-20 min | Google branding, live Stripe key, real card run and refund, real-phone in-app sign-up test | Needs live policy pages, the auth domain and active Stripe |

On Givi the same accounts arrived piecemeal over about three and a half weeks, through dozens of separate interruptions; several single waits for one key or one click cost 2-3 hours each.

## Checklist

**Before S1a (agent)**
- [ ] Access register, company facts file and vendor register exist; agents read the register before creating anything
- [ ] Field sheet written; account-standing check run; debts listed first in S1a
- [ ] One hand-off script per expected key, dry-run with a dummy value

**S1a, day 0**
- [ ] Hand-off test passed; password manager, 2FA, backup codes, second admin
- [ ] Venture card issued and labelled
- [ ] GitHub organisation and private repo; Actions budget above $0, scoped to the repo; a test PR runs CI
- [ ] Railway workspace for this venture with hard limit and alert; environment `production`; project-scoped token
- [ ] Supabase organisation for this venture, spend cap on, region recorded, `supabase login` done
- [ ] Resend account and full-access key; model-provider account with auto top-up and limits; capped agent test key
- [ ] Stripe in test mode with `stripe login`; company filed if needed

**S1b and the agent work that follows**
- [ ] Name, domain, handles and trade marks screened together
- [ ] Domain on Cloudflare with the venture card; `dig NS` shows Cloudflare; zone token stored; test TXT resolves
- [ ] Brand Google account (A) or Workspace (B) created in a clean browser profile, never from a personal Gmail; Workspace in place before anyone answers customers by email
- [ ] hello@, support@, privacy@ and a named address receive mail, not in spam; root MX and a single SPF record match the route
- [ ] Workspace only: domain verified, DKIM started, aliases or groups set
- [ ] Resend domain verified; `_dmarc` with a report address; sending keys restricted to the domain; a real sign-in code passes SPF, DKIM and DMARC
- [ ] Facebook Page, Instagram (professional), LinkedIn page, YouTube on the brand account; X and TikTok only if planned; 2FA and second admin on each
- [ ] Meta portfolio matches the register; no unpaid balances on the founder's other ad accounts
- [ ] Own funnel, Search Console, error and uptime monitoring under the brand account

**S2, company number arrives**
- [ ] Bank applied for first; card-switch task opened
- [ ] Stripe activated; `charges_enabled` and `payouts_enabled` true
- [ ] Meta: verification submitted, ad account in the checkout currency, two payment methods, small charge passed, spending limit read back, second admin, domain verified, both tokens stored, renewal reminder
- [ ] If planned: Google Ads without a campaign, auto-apply off, advertiser verification started; TikTok prepaid with identity linked
- [ ] ICO fee, registered office, company-owned AI provider organisations where they apply

**S3a and S3b**
- [ ] S3a: warm list and texts approved; one test send went out; testers have access
- [ ] S3a: founder signed in once in the agents' visible browser to every console and network
- [ ] S3b: Google OAuth branding published; live Stripe key stored; real card payment and refund seen in Stripe and the database
- [ ] S3b: real-phone sign-up passed in the Instagram, Facebook and TikTok in-app browsers

**After every sitting**
- [ ] Every account has a register row with owner, card, limit, alert and second admin; no personal login owns anything unless marked as a deliberate exception
- [ ] Every waiting verification is a tracked task with a re-check date
