# Toolbox: the tools we used, the ones that failed, and the ones we wished we had

This is the catalogue of the tools and accounts the Givi launch actually used: MCP servers, agent skills, command-line tools and SaaS accounts. Each row says what the tool did for us, how it held up, how it signs in and what to use instead. After the catalogue come a task-to-tool table, the tools that failed for us with their replacements, and the tools we wished we had from day 0.

**Done when:** every tool you plan to use has its owning login in your access map (`operations/ACCESS.md`); each MCP server answers one read call from a fresh session; the CLIs are installed and signed in; and nothing on the "failed for us" list sits on your critical path without its replacement.

> **What happened on Givi.** Givi launched in 26 days (17 Sep to 12 Oct 2026), built almost entirely by Claude Code and Codex: about 190 agent sessions and about 360 pull requests. Accounts and tools were added piecemeal. The build stack worked by day 9, the ads stack by day 19, and the last pieces (a Meta system-user token, a branded sign-in domain) arrived in week four. Two services ran dry in the middle of a crisis because nobody had read their quota or billing settings first. Everything below is what we would set up again, or deliberately avoid.

## How to read the tables

- **Verdict** is what happened on Givi: *worked well*, *worked with caveats*, *flaky*, *failed*, *replaced* or *not used*. **(recommended, not tested by us)** marks rows we never ran. **(learned the hard way)** marks rows where we got it wrong first.
- **One rule behind every row:** each venture gets its own login, card and metered workspace (hosting, database, mail, CI budget, model credits, outreach, posting). On Givi a shared model-credit balance fell to about $10 of $230 on launch night.
- Call counts are rounded from the session logs; they show what carried real load. Prices are what we saw in Sep-Oct 2026, so check them again.
- Only publicly available tools are named. Where we used private tooling, the row describes the pattern.

## 1. MCP servers

Prefer an MCP server or API over a browser whenever one exists. Add servers with `claude mcp add` (or as claude.ai connectors), authorise with `/mcp`, then start a new session: new tools only appear there. Test each with one read call.

| Server | What we used it for | Verdict | Auth notes | Alternative |
|---|---|---|---|---|
| **Claude in Chrome** (Anthropic's browser extension) | The founder's signed-in consoles: DNS dialogs, Google Cloud OAuth setup, Google Ads, TikTok Ads, Meta Events Manager and billing, the Claude connector directory. About 2,000 calls, the most used server | **Worked well** for consoles. Clicks on radios and checkboxes sometimes did not register, so read state back with `javascript_tool`. Tab IDs change when the founder touches a tab; long in-page scripts time out at about 45 s; it refuses myaccount.google.com and never types passwords | Connect with `claude --chrome` or `/chrome`. Load all its tools in one ToolSearch call. Work in a dedicated venture Chrome profile (Givi used the founder's daily one and should not have) | Codex's in-app browser |
| **Meta Ads MCP** (Meta's official connector, `https://mcp.facebook.com/ads`) | Uploads, campaigns, ad sets, creatives, insights, error reads. About 370 calls | **Worked with caveats.** A full campaign took about 6 minutes. Status changes through `ads_update_entity` saved as drafts until published in Ads Manager; it could not see card holds or create a pixel. **(learned the hard way)** It writes to whatever ad account ID you pass, and the founder's login already managed other ad accounts | Meta Business OAuth via `/mcp`. Pre-allow reads and paused-entity creation only, with the venture's ad account ID pinned. Never pre-allow `ads_activate_entity` or budget tools | Marketing API (Graph, versioned URLs) with a system-user token for pause, switch-on and billing state |
| **Welder** (social scheduling) | Uploads, `validate_post`, `create_post`, `list_comments`, `get_analytics` for Instagram, TikTok, YouTube and X. About 230 calls | **Worked well.** One flaky Instagram carousel; rate limits needed a retry. No Facebook or LinkedIn, no TikTok comments or play counts | `claude mcp add --transport http --scope user welder <url> --header "Authorization: Bearer <key>"`, run by a script that reads the key from the clipboard. About $19 a month after the trial. One Welder profile per venture; `get_context` before every post | Graph API for Facebook Pages |
| **Context7** | Current docs for Composio, Remotion flags, Railway's client-IP header, Stripe trial behaviour, Resend inbound mail. About 40 calls | **Worked well.** It found at least one real root cause | None | WebFetch on vendor docs |
| **Gmail** (claude.ai connector) and **Google Workspace MCP** (open-source `workspace-mcp`, run with `uvx`) | Reading sign-in codes during test sign-ups, proving whether an email went out, drafting notes, reading and writing a queue spreadsheet | **Worked well.** It took the founder out of test sign-ups. The Workspace server only works when the right account email is passed, and one stored token was dead | Bind each to the account whose mail it must read; the brand account for codes, never the founder's personal one | mail.tm for disposable inboxes |
| **Supabase MCP** | Project setup and inventory | **Worked with caveats (learned the hard way).** The claude.ai connector stayed bound to an older organisation. A separately named MCP per organisation worked. An expired sign-in blocked one release | OAuth binds to one organisation; restart after authorising | Supabase CLI and Management API |
| **Stripe MCP** (official connector) | Nothing: never authorised. Codex's Stripe plugin failed with `USER_NOT_LOGGED_IN` | **Failed / not used** | Authorise on day 0 if you use Stripe **(recommended, not tested by us)** | Stripe CLI and API |
| **Adspirer** (ads agent plugin) | Google Ads search campaign, keywords, conversion action; TikTok video listing. 37 calls | **Failed for daily use (learned the hard way).** Fast and exact until its 15-calls-a-month quota, reads included, ran out two days in, mid-crisis, for about three weeks | `/mcp` with the Google login that owns the ad account. Read the quota first | Google Ads Scripts and automated rules (no quota); the Google Ads API with a developer token |
| **Instantly MCP** | One read-only check of an unpaid workspace (API returned 402) | **Not used.** No cold email went out for Givi | Call `workspace_get` and check the name before any write | Gmail drafts for warm outreach, where selling should start |
| **Clay**, **Canva** (claude.ai connectors) | One lead lookup; logo concepts with `generate-image` | **Not used / replaced.** Canva's image credits ran out after 4 jobs | Check credits and workspace first | Manual lists; hand-built HTML mockups |
| **Your product's own MCP connector** | Once Givi had one, agents used it to drop reminders and run notes into the founder's own account, and to dogfood | **Worked well,** including from headless `claude -p` runs | Allow only its job-creation tool | |
| Barely used: **Google Drive** (created one sheet), a free no-login **Microsoft Learn MCP** (test fixture for the product's own "connect any MCP" feature). Authorised but unused: **Figma**, **Zapier**, **Motion Creative Analytics** | | **Not needed.** Zapier is a candidate route for LinkedIn company-page and Facebook Page posts **(recommended, not tested by us)** | | |

## 2. Agent skills and plugins

Install once per machine and pin versions for the length of a launch.

| Skill or pack | What we used it for | Verdict | Notes | Alternative |
|---|---|---|---|---|
| **gstack `browse`** (Garry Tan's open-source skill pack; headless browser run as `$B`) | Screenshots at set widths, DOM reads, QA of local and live pages, brand-page edits with remembered logins, Telegram Web tests. About 1,400 calls | **Worked well** for QA. Daemon restarts lose sign-ins; X, TikTok, the Cloudflare dashboard and Stripe Checkout block it; it cannot see popups like "Continue with Google"; ad pixels never fire in it (team cookie, bot user agent) | `./setup` after cloning; first run needs `bunx playwright install chromium`. One state file per agent. Wrap commands in scripts so permission rules can match the script path | Playwright for clean-visitor checks |
| **gstack `qa`, `design-review`, `review`** | Click-through QA, visual QA, pre-merge review | **Worked well.** Every run found real bugs | Founder's rule: build UI with `impeccable`, check it with gstack | |
| **gstack `codex`** | Second-model review of branches and plans from Claude (review and challenge modes) | **Worked well.** Real defects about half the time; challenge mode caught five serious problems in a pricing plan | Needs the Codex CLI signed in; once the CLI was too old for its default model (pass `-c model=<model>`) | Plain `codex exec --sandbox read-only` |
| **gstack Claude reviewer, run from Codex** | Claude reviewing Codex's code | **Worked well,** high value | Codex asks consent before sending code to another vendor; give it once, up front | A fresh no-tools Claude session with the diff as data |
| **gstack `office-hours`, `plan-ceo-review`, `plan-design-review`** | Scope and information-architecture reviews of plans | **Worked well** | | `autoplan` runs several at once |
| **gstack `setup-browser-cookies`, `skillify`, `context-save`/`context-restore`, `careful`/`guard`, `ship`, `land-and-deploy`, `canary`, `investigate`, `design-shotgun`** | Cookie import, turning a repeated flow into a skill, session handoff, guardrails before destructive commands, release and post-deploy checks, debugging, design variants | **(recommended, not tested by us).** We built private equivalents. `design-shotgun` needs a paid image-generation key we never set up | | |
| **`gstack-upgrade`** | One mid-launch upgrade, 36 versions behind | **Worked with caveats (learned the hard way).** Local patches had to be re-applied; a later upstream change made the shared browser window lose its tabs | Pin gstack to one tag per launch; upgrade between launches | |
| **`impeccable`** (Paul Bakaus's open-source design skill) | Building UI; scored usability critiques | **Worked well;** mandatory for UI on Givi | Its loader changed repo files on our machine (a renamed context file, a `.gitignore` line); run `git status` after loading. Its live overlay is blocked by a strict content security policy | Anthropic's `frontend-design` |
| **`frontend-design`** (Anthropic) | Early visual direction | **Replaced by `impeccable`.** Codex's output with it read as generic and the first landing was rejected | | `impeccable` plus a study of 8-10 reference sites |
| **Superpowers** (Jesse Vincent's process skills) | `systematic-debugging`; brainstorming and test-first as the default workflow | **Worked well** | Claude Code plugin | gstack `investigate` |
| **Matt Pocock's skills** | `resolving-merge-conflicts` in cherry-picks; `grilling` to stress-test plans | **Worked with caveats.** Its `code-review` was too heavy as-is | Plugin | gstack `review` |
| **Anthropic document skills** (`docx`, `pdf`, `pptx`, `xlsx`) and **`skill-creator`** | Nothing on Givi | **(recommended, not tested by us):** documents for an accountant or partner; `skill-creator` to package the day-0 kit as one skill (Givi assembled it by hand over 25 days) | Built in | gstack `skillify` |
| **A handoff skill** (pattern; ours was private) | At session end: re-verify each claimed outcome live, sweep docs for stale claims, list scheduled jobs, rewrite the RESUME block | **Worked well.** Once caught search keys that were never set | Write your own; keep it to one screen | gstack `context-save` |
| **A sign-in sharing helper** (pattern; ours was private, built on gstack) | The founder signs in once in a visible window; hidden browsers reuse those cookies for an allowlist of domains | **Worked after four bug fixes (learned the hard way).** The first version checked public pages and said "signed in" when it was not; a profile switch dropped every login for every session | Test the checker on a site you know is signed out | gstack `setup-browser-cookies` |
| **Claude Code bundled skills:** `/update-config`, `/fewer-permission-prompts`, `/loop`, `/schedule` | Permission syntax (`/update-config`) | **Worked well.** `/fewer-permission-prompts` (mines transcripts for a starter allow list) **(recommended, not tested by us)** | Built in (checked 13 Oct 2026) | |
| **Artifact pages** (private claude.ai pages published from Claude Code) | One review page per asset class: landing gallery, ads, films, a materials library | **Worked well:** one link per topic on the founder's phone | Embed fonts as data URIs; read before republishing when sessions share a page. Unattended runs could not write to an artifact's database (approval prompt every time) | A static page on Vercel for anything a scheduled job writes |

## 3. Command-line tools

| CLI | What we used it for | Verdict | Notes | Alternative |
|---|---|---|---|---|
| **`gh`** | Repo creation, PRs, checks, merges, run logs, reruns. About 500 calls | **Worked well;** occasional 504s | Allow `gh pr *`, `gh run *` and the exact deploy-workflow call; never bare `gh *` (it includes `gh repo delete`). Wrap read-only `gh api` calls in a GET-only script | |
| **`git` worktrees** | One checkout per task and agent. About 3,000 calls | **Worked well** | Never copy files between trees; never trust a stale main checkout (ours was once about 580 commits behind) | Claude Code's `--worktree` |
| **`railway`** and its GraphQL API | Deploys, variables, logs, domains, per-customer provisioning. About 850 calls | **Worked with caveats.** `railway ssh` drops everything after a newline and had random host-key failures; an older stdin flag silently stored nothing; variable changes redeploy unless `--skip-deploys`; the live environment was named `staging` and misled agents; `deploymentStop` was unreliable in the API | Prefix with `timeout 60`. `printf %s "$K" \| railway variable set NAME --stdin --service <svc> --skip-deploys`. Name the live environment `production`. Never allow bare `railway *` (it includes volume deletes) | Deploys from CI |
| **`codex`** | `codex exec --sandbox read-only` and `codex review` as second-model reviewer | **Worked well;** it cannot run tests in the read-only sandbox | Wrap in `timeout 1500` (Homebrew `coreutils` on macOS) | gstack `codex` |
| **`claude`** | `claude mcp add`; headless `claude -p '<task>' --allowedTools '<only what is needed>'` | **Worked with caveats (learned the hard way).** A headless run hung 8 hours on a macOS privacy prompt for the Desktop folder | Run headless jobs from a folder outside Desktop, Documents and Downloads | Cloud routines |
| **`uv`, `pytest`, `pip-audit`** | About 860 tests by the end, dependency audit | **Worked with caveats (learned the hard way).** Each run leaked about 1,000 temp folders until a fixture fix; parallel sessions filled the disk to zero | A private `--basetemp` per run | |
| **`docker` with Colima** | Linux image builds; a 7-model eval bench that cost about $5 | **Worked with caveats.** Default socket unavailable; archive API failed on a read-only temp folder (use tar streams) | | Build in CI |
| **`curl`, `dig`, `python3`** | Outside-in checks of pages and DNS; one-off scripts for availability checks, Graph API, a Cloudflare DNS helper | **Worked well** | Real browser user agent in `curl`; no tokens in URLs | |
| **Cloudflare API** (a small Python helper) | DNS records with a zone-scoped "Edit zone DNS" token. We did not use `wrangler` | **Worked well** | Founder creates the token once | Claude in Chrome on the DNS dialogs |
| **`vercel`** | A static health page written by a scheduled job | **Worked well** | `vercel deploy --prod` | Cloudflare Pages |
| **`ffmpeg`** | 30 fps re-encodes for Meta, Opus voice notes for Telegram, posters | **Worked well;** our Homebrew build lacked `drawtext` | | |
| **Remotion CLI** | Films and video ads from React, copy and price passed as props | **Worked technically; wrong investment.** About 30-40 agent-hours of films brought no attributable sign-up, while a static made in about 20 minutes took about 96% of UK and US Meta spend. Colours shifted until rendered with `--color-space=bt709` | Free only for small companies; check the licence | HTML-to-PNG statics first |
| **Playwright** | Clean-visitor pixel and consent checks; measuring layout for creatives | **Worked well** | `npx playwright install chromium` | `$B useragent` with a real user agent |
| **macOS `security`, `pbpaste`, `pbcopy`** | Keychain storage; moving secrets without chat | **Worked with caveats (learned the hard way).** An echo once printed a generated password into chat; a clipboard hand-off failed because something else had been copied first | `security add-generic-password -U -a <acct> -s <name> -w "$(pbpaste)"` | 1Password `op` |
| **`launchctl`** | Hourly and daily jobs on the laptop | **Flaky:** froze on a privacy prompt; stops when the laptop sleeps | Allow only exact `launchctl bootstrap` lines for your jobs | Jobs in your product or a cloud routine |
| **OBS Studio** and other recorders | Screen recording for a platform review | **Failed:** about 1.5 days, zero usable clips; OBS could not capture the Codex window | | Codex frame capture plus ffmpeg (worked); time-box any recorder to 30 minutes |
| **`stripe`, `supabase`, 1Password `op`** | Nothing; not installed | **Wished for (recommended, not tested by us)** | `stripe login` gives a scoped, expiring key | |

## 4. Browser routes

`12-running-agents.md` has the full table. In order: an API, MCP or CLI first; gstack headless `browse` for your own pages and QA; Playwright with a fresh context for "real visitor" checks; Claude in Chrome in a venture profile for consoles that need the founder's identity; a shared visible window for sites that block automation; Codex's in-app browser for long forms with uploads. Never use gstack's `chrome-cdp` helper: it quit and relaunched the founder's Chrome and was banned on day 10.

## 5. SaaS accounts

Create every account under the brand identity and the company, with its own card, and write the owning login into the access map before anyone signs up.

### Company, identity and agents

| Service | Used for | Verdict | Auth notes | Alternative |
|---|---|---|---|---|
| **Companies House** (UK) | A UK limited company, needed by every platform verification | **Worked well:** about 24 hours, about £100 | Founder, with a GOV.UK One Login check | A new brand under an existing company |
| **Business bank account** | Ad-platform card, Stripe payouts | **Learned the hard way.** Ad-platform card holds failed twice and stopped delivery silently. Apply the day the company number arrives | Founder | A venture-labelled virtual card meanwhile |
| **Stripe** | Checkout subscriptions, a card trial, top-ups, refunds, the customer portal | **Worked with caveats.** Live payments came on day 17, mostly waiting on a key paste. A restricted key that could not create prices broke checkout for a day; Stripe's Managed Payments returned 503 at Checkout until each product had a tax code; Checkout ignores scripted clicks (Codex paid in test mode through Stripe's agent checkout channel); revealing a webhook secret in the dashboard needs a human click; the live key arrived pasted twice into one string | Founder creates the account under the company. Create prices by lookup key from code, and create webhooks through the API, whose response returns the secret once | A merchant of record (Paddle, or Stripe Managed Payments) if your accountant prefers it for VAT |
| **D-U-N-S** | Google Ads advertiser verification | **Learned the hard way:** started 18 days after incorporation | Founder | Skip unless you plan Google ads |
| **Claude** (founder's plan) and **OpenAI** | Running Claude Code; a Claude connector listing; a planned ChatGPT listing | **Learned the hard way.** A Claude directory listing cannot move to another account later. OpenAI business verification was never started, which blocked the ChatGPT listing | Create company-owned organisations before any listing | |
| **Codex** (ChatGPT login) | Second agent: research, platform reviews, consoles, review | **Worked well** in its lanes | | |

### Domain, email, hosting and data

| Service | Used for | Verdict | Auth notes | Alternative |
|---|---|---|---|---|
| **Cloudflare Registrar, DNS, Email Routing** | Domain at cost, all records, `hello@` forwarding | **Worked well.** The dashboard blocks headless browsers; hosting certificates needed DNS-only records; keep the forwarding MX and SPF records when adding a sender. Forwarding is fine for a short test; once you answer customers by email, move the mailbox to Google Workspace (`02-day0-accounts.md`) | Founder's login with passkey; a zone-scoped token for agents | Any registrar with a DNS API |
| **Resend** | Transactional mail and the auth provider's SMTP; inbound on a subdomain | **Worked well:** about 35 minutes to set up; free tier 3,000 a month and 100 a day. The auth provider's own 30-an-hour SMTP cap was the tighter limit | Founder signed up with GitHub; a sending-only key restricted to the domain | Postmark |
| **Brand Google account** (a new Gmail that receives `hello@yourdomain.com` through forwarding) | Sender identity and Gmail avatar, test sign-ups, reading codes | **Learned the hard way.** None existed until day 19. A Google Workspace "domain in use" recovery can convert a personal Gmail into a Workspace account, so use a fresh brand account | Create it right after the domain, before any account named after the brand, in a browser profile signed out of every personal Google account | Google Workspace on your domain once you answer customers by email: Gmail's "Send as" through another provider's SMTP is being retired **(recommended, not tested by us)** |
| **GitHub** | Private repo, PRs, rollback tags, CI | **Repo worked; Actions failed (learned the hard way).** CI was blocked for about 7 days, then failed again and was disabled. Cause: an Actions budget of $0 with "stop usage" on; adding a card changed nothing | Day 0: card plus a non-zero Actions budget (USD 10-30 a month) scoped to this venture at Settings > Billing and licensing > Budgets and alerts (github.com/settings/billing/budgets); alerts at 75%, 90% and 100% | |
| **Railway** | Web app, landing, MCP server, one service and volume per customer's agent | **Worked well:** the rebuilt app deployed in about 15 minutes. Caps: 20 volumes per project (we hit it), 100 services per project. A VPS provider was set up first and dropped as "cost optimisation for a problem we don't have yet" | Its own workspace, card and hard limit per venture; project tokens for CI. Pro was $20 a month including $20 of usage | Fly.io at around 100 tenants (our plan, not tested) |
| **Supabase** | Auth (email code first, Google second), Postgres, a custom auth domain | **Worked well.** The custom domain ($10 a month) replaced a Google consent screen showing the supabase.co address; before it, 44 of the 45 visitors who clicked Start were lost at sign-in | Founder creates the organisation; name its MCP per organisation | Railway Postgres |
| **Cloudflare Pages** | Nothing. Our landing lived in the app, so copy fixes waited 10-40 minutes for an idle deploy window | **(recommended, not tested by us)** | Same account as DNS | |
| **Free utilities:** Verisign RDAP, mail.tm, Vercel | Bulk `.com` availability; disposable test inboxes; a static health page | **Worked well** | No accounts for the first two | |

### AI providers, connections, voice and channels

| Service | Used for | Verdict | Auth notes | Alternative |
|---|---|---|---|---|
| **OpenRouter** | Every model call; per-customer capped keys minted from a management key; speech; "connect your own AI" | **Worked well technically; learned the hard way on money:** a shared model-credit balance nearly ran dry on launch night | A separate account per venture, account-level limit, auto top-up; management key off the public app | Direct provider keys |
| **Exa** | Web search and page reading for every customer's agent | **Worked well:** $10 free a month, then about 4 cents per research task | Key stored by a validating script | Brave plus Firecrawl (dropped after a broken key hand-off; the vendors were fine) |
| **Composio** | Customers' app connections, white-labelled connect page | **Worked with caveats.** Free tier covered us. Meta connections expired within days; no TikTok Ads; connect links expire in about 10 minutes and look broken | Key only on the app | Your own OAuth for the top one or two vendors |
| **Vapi** (ElevenLabs voices) | Web calls and a phone line | **Worked with caveats.** Web call built in about 18 minutes; the US phone number failed on the first test call. Balance visible only in the dashboard | Public key restricted to your origin | A web call before any phone number |
| **Telegram (BotFather)** | Main owner channel, team groups | **Worked well,** live on day 10. Privacy mode off for groups; check `getWebhookInfo` after restarts | Founder runs `/newbot` (2 minutes) | Web chat |
| **Slack app** | DM channel with approvals and files | **Worked well:** about 15 minutes of coding | Create it in a brand Slack workspace for this venture | Build only when buyers ask |
| **WhatsApp Business Platform** | Nothing | **Rejected** after a policy check: Meta's terms, as we read them in Oct 2026, bar general-purpose AI assistants in our markets | | |

### Social, ads and monitoring

| Service | Used for | Verdict | Auth notes | Alternative |
|---|---|---|---|---|
| **Meta Business portfolio, app, ad account, system user** | Ads, Page, Instagram, pixel, a token for scripts | **Worked with caveats.** Business verification took about 19 hours. Card holds stopped delivery twice while campaigns showed "Active". The system-user token arrived 13 days after verification, leaving no reliable way to pause or switch on ads | Create system users and tokens in sitting S2, together with verification. Clear any old billing problem on another ad account under the same login first: Meta links payment risk across them | |
| **Google Ads** | A small UK search test | **Learned the hard way:** created under the wrong Google login | Brand Google account; Expert mode "without a campaign" | Skip unless search demand exists |
| **TikTok for Business** | A £50 prepaid video test | **Worked with caveats:** review took over 6 hours; it adds AI text and audio edits unless you switch them off | Prepaid only | |
| **Social profiles** (Instagram, TikTok, X, YouTube, Threads, LinkedIn page, Facebook Page) | Brand presence, organic posts | **Mostly wasted before customers.** 47 organic posts in 5 days brought zero site visits; LinkedIn comments on buyers' posts produced all five buyer conversations. TikTok and X block automated sign-up | Brand logins; never automate the founder's personal LinkedIn or WhatsApp | Organic posting after the first payers |
| **Outreach tools** (Instantly, Clay, Gmail drafts) | Barely used: Gmail drafts about 6 calls, Instantly 3, Clay 1, against about 2,000 browser-extension calls. No cold email was sent and no warm notes went out in the 26 days | **Not used; our biggest gap.** Givi had no paying customer by 12 Oct 2026, and outreach was the step nobody owned | A new Instantly workspace per venture if you send cold email; pre-warmed mailboxes take time | Warm notes from the founder's own accounts, drafted by agents, sent by the founder |
| **Uptime and dead-man service** (UptimeRobot or Healthchecks.io), **error tracker** (Sentry free tier), **analytics** (Cloudflare Web Analytics, PostHog) | Nothing; monitoring lived inside the product, which cannot report its own outage. We built a humans-only server-side funnel, which worked | **Wished for (recommended, not tested by us)** | Brand login; consent-gate every tag | |

## 6. Task-to-tool decision table

| Task | Use | Avoid |
|---|---|---|
| Name and `.com` availability in bulk | Verisign RDAP from a script | Registrar search pages |
| Domain, DNS, `hello@` forwarding | Cloudflare Registrar, DNS API token, Email Routing for a short test; Google Workspace once you answer customers by email | The dashboard from a headless browser; replying through Gmail "Send as" with outside SMTP (being retired) |
| Transactional email and sign-in codes | Resend, wired as the auth provider's SMTP | The auth provider's built-in sender |
| Hosting, per-customer containers | Railway CLI and GraphQL API | Infrastructure picked for cost before the product shape is known |
| Database and auth | Supabase with a custom auth domain, email code first | Google as the only sign-in for ad traffic (in-app browsers block it) |
| Production database reads | A wrapper with a read-only database role | Raw `railway ssh` |
| Production deploys | A GitHub Actions job on merge with a concurrency lock | Laptop deploys |
| Secrets into hosting | One store plus a validating script; hosting reference variables for copies | Keys in chat; `!` lines in an editor panel |
| Model access with caps | Own OpenRouter account; capped keys per customer | A shared or uncapped balance |
| Web search for agents | Exa | Two vendors for one job |
| Customers' app connections | Composio | Your own OAuth apps for every vendor on day 1 |
| Library and API docs | Context7 | Memory |
| Meta ad builds | Meta Ads MCP, paused, ad account pinned | Pre-allowed activation or budget tools |
| Meta pause, switch-on, billing state | Marketing API with system-user tokens | MCP status changes (they save as drafts) |
| Google Ads | Scripts and automated rules; the API with a developer token | A low-quota MCP as the main route |
| TikTok Ads | Claude in Chrome | Headless browsers |
| Brand social scheduling | Welder, one profile per venture | Expecting Facebook or LinkedIn from it |
| Facebook Page posts | Graph API with the system-user token | Browser uploads (stalled at 0%) |
| Founder's LinkedIn comments | Agent drafts and copies to the founder's clipboard; the founder posts | Any automated post, comment or message in the founder's name |
| Consoles that need the founder | Claude in Chrome in a venture profile | Typing the founder's passwords |
| Screenshots and visual QA | gstack `browse`, numbers read from the DOM | Numbers read from screenshots |
| Pixel and consent checks | Playwright, fresh context | Any browser with a team cookie |
| Test sign-ups | Gmail MCP or mail.tm | Asking the founder for a code |
| Founder review pages | Private Artifact pages, one URL per asset class | Local files the founder cannot open on a phone |
| Reminders and watchdogs | Jobs in your product; cloud routines with read-only tokens; an uptime service | Laptop jobs; session-bound schedules |
| Second-model review | `codex exec --sandbox read-only` with a fixed prompt | Self-review only |
| Stripe products, prices, webhooks | Stripe CLI and API (creating a webhook returns its secret once) | Revealing the secret in the dashboard and pasting it in chat |
| Ad creatives | HTML-to-PNG statics (3-5 an hour); the first paid test is one ad set with 2-3 statics, and the one Meta spends on is the winner; one short video only after a static wins | Films first; offer terms rendered into video |
| Competitor teardown | A signed-out browser | Any browser where the founder is signed in to that competitor |

## 7. Tools that failed for us, and what to use instead

| Tool or gap | What happened | Use instead |
|---|---|---|
| GitHub Actions on a $0 budget | CI blocked about 7 days, then disabled; three founder round trips before an agent opened the billing page | Non-zero budget on day 0; "CI did not start" at the top of the daily digest |
| `!` lines handed to the founder | The VS Code panel sends them as plain chat text; at least 6 failures | A double-clickable, validating `.command` file |
| Adspirer as main Google Ads route | Quota gone in two days, for three weeks | Google Ads Scripts and rules; the API |
| Meta Ads MCP for switching ads on and off | Drafts instead of live changes; card holds invisible | Marketing API with a system-user token |
| Composio for Meta and TikTok | Meta connections expired; TikTok Ads unsupported | A system-user token; direct integration |
| Codex Stripe plugin, Supabase connector | Not signed in; bound to the wrong organisation | Stripe CLI and API; a named MCP per organisation |
| Canva and image-variant skills | Credits ran out; a paid image key was needed | HTML mockups; decide on an image key on day 0 |
| WebFetch on some vendor sites | openai.com, its help centre and the Meta Ad Library returned 403 | Claude in Chrome |
| gstack `browse` on anti-bot sites | Blocked by Cloudflare's dashboard, X, TikTok, Stripe Checkout, Google sign-in | Claude in Chrome; the visible window; APIs |
| gstack `chrome-cdp` | Restarted the founder's Chrome | Banned |
| Screen recorders | Hung or could not capture the window | Frame capture plus ffmpeg; prove a 15-second file first |
| `Monitor` for long waits | Watches end at 5 minutes by default, 30 at most | A background until-loop with a timeout |
| Laptop LaunchAgents | Hung 8 hours on a privacy prompt; stop when the laptop sleeps | Product jobs or cloud routines |
| A Codex heartbeat automation | Fired about 33 times over 17 hours with nothing it could do after losing a sign-in | Checks that alert once and pause after repeated blocked runs |
| No secrets store | A key pasted twice into one string, another stored three times, a wrong text saved as a key | 1Password `op` or Keychain only, with a validating script per key |
| No "founder is blocking" signal | A key request sat 66 minutes unseen | A push notification only when the founder blocks the critical path now |
| A VPS provider, a sandbox runtime, two search vendors | Set up, then dropped | Stay on the platform that already runs your services |
| Claude's weekly usage limit | Hit mid-merge in a heavy week | `/model sonnet`; queued work to the Codex CLI |

## 8. Tools we wished we had from day 0

- **One secrets store** (1Password with the `op` CLI and a service account, or the Keychain alone), so the founder saves each key once and agents pull it by reference: `op read op://<vault>/<item>/<field> | railway variable set NAME --stdin --skip-deploys`.
- **The Stripe CLI and Stripe MCP,** signed in on day 0, so products, prices, webhooks and test events never need the dashboard.
- **The Supabase CLI,** so auth settings do not depend on a connector bound to one organisation.
- **An uptime and dead-man service** watching the product and every scheduled job from outside, plus an **error tracker**.
- **A Google Ads developer token,** applied for when the company exists, if agents will run Google ads.
- **Company-owned Claude and OpenAI organisations** before any directory listing.
- **Static hosting for the landing,** so copy fixes ship in minutes.
- **A password manager extension in every agent-driven browser,** so a founder sign-in is one autofill click and no agent sees a password.
- **The day-0 kit as one skill:** rules files, permission pack, a validating script per expected secret, the CI deploy workflow and the review prompt, generated at once.

## Checklist

- [ ] Access map lists every service with purpose, owning login, workspace, who acts, cost, alarm and blast radius; no secrets in it
- [ ] Brand Google account created right after the domain; nothing sits on a personal login or a login shared with another venture
- [ ] hello@ forwarding only for a short test; Google Workspace in place before anyone answers customers by email
- [ ] Every metered service in its own workspace with its own card and limit
- [ ] Quota and pricing page read for every MCP or API you will rely on, and noted in the access map
- [ ] GitHub card and a non-zero Actions budget set; the first CI run on main actually started
- [ ] MCP servers authorised with `/mcp`; each answered one read call in a fresh session
- [ ] Ad tools limited to reads and paused creation, ad account ID pinned
- [ ] CLIs installed and signed in: `gh`, your host's CLI, `stripe`, `supabase`, `codex`, your test runner, `ffmpeg`
- [ ] gstack pinned to one tag; `bunx playwright install chromium` run; `chrome-cdp` disabled
- [ ] Claude in Chrome connected to a dedicated venture Chrome profile
- [ ] One secrets store chosen; a validating script exists for every expected key
- [ ] Model provider account separate for this venture, with a limit, auto top-up and capped customer keys
- [ ] Outside monitoring signed up under the brand login
- [ ] Nothing on the "failed for us" list is on the critical path without its replacement
