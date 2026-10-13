# Landing pages

Get one landing page live on your own domain in 1-2 working days, approved on taste in two short founder picks, saying only what the product does today, and measured from its first real visitor. Agents build three variants in parallel, check them mechanically against a written bans list, and show the founder one private link. Before any ad money, the sign-up path is proven on a real phone inside the Instagram, Facebook and TikTok in-app browsers.

**Done when:** one page is live on the apex of your domain, built from a committed taste file and bans list and frozen after at most two rounds; every claim on it traces to the capability ledger or the offer file; a sign-up started from a DM link works inside the Instagram, Facebook and TikTok in-app browsers on a real phone, with your own domain on the sign-in screen; visitors are counted on the server (humans only) with UTMs intact; link previews, favicon, robots and sitemap are in place; and no split test is running below about 1,000 visitors per arm.

> **What happened on Givi.** The landing took about 25 days and roughly 15 rejected or reworked visual rounds; the productive core, from three directions to two live finalists, took 4 days. Most of the rework came from the agents themselves; very little came from hidden founder taste. No taste or bans file existed that every agent read, so agents kept bringing back things already rejected: "Example" labels, pause and replay buttons, phones dressed up as a messenger app. Nobody owned the landing, so two agents built two landings on the same day. Claims ran ahead of the product four times. A split test between two finalists ran 8 days and ended 16 sign-in clicks against 14. Worst, paid traffic arrived at a sign-in screen showing the database provider's address instead of the brand, and Google sign-in did not work at all inside Instagram's browser: 44 of 45 people who clicked Start left at sign-in.

---

## The plan, day by day

| When | What the agents do | Founder |
|---|---|---|
| Day 0 | one landing owner; taste intake; `TASTE.md`, `BANS.md` and the capability ledger committed; smoke page with the job and a waitlist | about 10 min: pick from 8-10 references, answer the taste lines |
| Day 1 | reference scout, shared brief, round 1 (three variants in parallel), mechanical checks, one gallery link | about 10 min: pick one or two |
| Day 2 | round 2 on the pick, freeze, port to production | about 10 min: final pick |
| Day 2-3 | head tags and link previews, tracking and consent, in-app QA, claims audit | none |
| Before any ad | the funnel gate (G5): real-phone in-app sign-up, numeric pass bar, real card payment and refund | about 5 min on their phone, in sitting S3b |

At most two rounds of three variants, then freeze.

---

## Step 0. One owner, one release lane, everything committed (day 0)

**(learned the hard way)** Codex and Claude built two Givi landings and a separate product prototype in the same two days; most of it was thrown away. A reference study with a take/avoid table, the one rebuild the founder did not reject, was never committed, so no later agent saw it.

- One session owns the landing from first draft to live page. Every other session sends it change requests.
- Commit every design artifact (reference studies, briefs, concept HTML, round notes, screenshots) to `main` the same day through a docs-only pull request. Check with `git status` (no untracked design folders) and `git cat-file -e origin/main:<path>`.
- Put "read `bd/TASTE.md`, `bd/BANS.md` and `product/capabilities.md` first" at the top of `CLAUDE.md` and `AGENTS.md`, so Claude Code and Codex follow the same rules.
- Host the landing statically (Cloudflare Pages or any static host), separate from app releases. **(learned the hard way)** Givi's landing shipped inside the app, whose release waited for 10 idle minutes, so two-line copy fixes took 15-40 minutes.

---

## Step 1. The taste intake (day 0, about 10 founder minutes)

**(learned the hard way)** Givi's founder had clear taste rules (first name only, no photo, no cursive or bookish serif fonts, no "Example" labels, no agency wording, one currency). Each surfaced in a different round and cost a re-render. The single-step format below is **(recommended, not tested by us)**.

**The reference gallery.** One private page with 8-10 references: pages the founder approved before, plus scouted sites that look nothing alike, each with one screenshot and one line on what to take from it, and a draft bans list at the bottom. The founder picks two or three and strikes out anything they hate.

**The taste lines,** inside the operator's one intake message:

```
Taste for <venture>. Reply "defaults" or change a line by number.
1. Public founder name: <first name only>. Photo: <none>.
2. Fonts or styles you never want: <for example cursive script, bookish serif headlines>.
3. Tone: <the product speaking plainly; never agency wording such as "done for you">.
4. One market and one display currency: <market>, <currency>.
5. Your acceptance tests: <"easy to read" / "these people have taste, I want to try it" / "finally something for me">.
6. Examples to avoid: <small chores; any industry you find weak>.
7. Name competitors publicly: <no; contrast with "other tools">.
8. References: pick 2-3 on <private link>; strike any you dislike.
```

Commit two files before any design agent runs:
- `bd/TASTE.md`: the picked references (archived screenshots or private copies, never live URLs that can change), what to take from each, fonts, colour approach, the signature device, the acceptance tests.
- `bd/BANS.md`: one grep-able line per ban, seeded with the founder's answers and the generic tropes in "Design rules" below.

> **What happened on Givi.** On 4 Oct Vito approved two finished pages as his reference for future work, and the agent wrote a taste file with exact fonts, colours, signature devices and dated screenshots. Within a week it was stale: its "live" link for one page had been repointed to the other, and a newer decision (a calmer look for the app after sign-up) was missing. Update the taste file in the same pull request as any taste decision.

---

## Step 2. Write the truth before the copy (day 0)

**(learned the hard way)** Givi's pages claimed "1,000+ tools" (checked against the connector vendor's catalogue while the app showed 500+), "helper" assistants (checked against what the engine could do while no owner had used one), WhatsApp (before Meta's terms ruled it out), and a promise that nothing goes out without approval (false on the live product then).

- **`product/capabilities.md`**: every capability with its status as **an owner sees it today** (live, gated, not built), checked on a fresh account or from usage numbers, plus a "do not promise yet" list. "The code exists" and "the vendor supports it" do not count. Each gated item gets an expected live date and an owner.
- **`bd/job-chains.md`**: every example the page, ads and films show, as steps with a live status per step.
- **`bd/offer.md`**: headline, price line, and each value claim with a one-line basis. UK advertising rules expect evidence for objective claims before an ad runs. See `03-positioning-pricing.md`.

A read-only sub-agent can draft the ledger from code, feature flags and in-app guides in under an hour.

---

## Step 3. A smoke page on day 0-1 (1-2 hours)

**(recommended, not tested by us)** Givi had no public page for its first five days. Put one page on the apex with the accepted (or provisional) "why us" sentence, the first paid job and a waitlist form, and no price until the offer is accepted. It collects first-party visit data while the product is built, and buyers from your calls can be sent to it. Verify that a test sign-up lands in the list and the server counts visits by source.

---

## Step 4. Reference scout and one shared brief (about 45 minutes)

**(done on Givi)** A take/avoid study turned a rejected build into a page the founder did not reject, in 24 minutes.

**Scout.** Screenshot the first screen and scroll of 5-6 direct competitors and 3 aesthetic references that look nothing alike (gstack `browse`, signed out), with one line each: "take this, ignore the rest". Search galleries by moment (onboarding, pricing, chat) rather than industry: Mobbin, Page Flows, Refero, Godly, SaaS Landing Page, One Page Love. For any page owned by a friend or a direct competitor, write a "do not take" list. **(learned the hard way)** Givi's first prototype was rejected as a copy of the one competitor the founder had mentioned.

**The shared brief** (`bd/directions-<month>/README.md`):

```
Read bd/TASTE.md, bd/BANS.md and product/capabilities.md first. BANS.md is pasted below; every line is a hard rule.
Audience: <buyer>, at a 12-year-old reading level. Banned jargon: <internal terms>.
The one job to show end to end: <chain from bd/job-chains.md>. Show only steps marked live.
Headline and price line: from bd/offer.md; never invent a number.
References: take <X> from <A>, <Y> from <B>, <Z> from <C>. Do not take: <list>.
Length budget: 7 sections, about 600 words, each thing said once.
No empty box: any input shows suggested jobs by business type.
Design laws: OKLCH colours, neutrals tinted toward the brand hue, no pure black or white; type scale ratio at least 1.25; body at least 19 px on phones; no gradient text, glassmorphism, side-stripe borders, identical icon-card grids or nested cards; ease-out motion; prefers-reduced-motion shows the finished state.
Technical: one self-contained HTML file, inline CSS and vanilla JS, Google Fonts only, inline SVG, works at 390 and 1440 px with no horizontal scroll and a 16 px gutter, explicit body background.
Deliver: brief.md (three voice words, what you took from each reference, fonts with a reason each, sections, motion plan, a real-today versus concept table) and index.html.
```

Grep the brief against `BANS.md` before sending: `grep -n -i -E "example|pause|replay" README.md` must return only the ban lines. **(learned the hard way)** Givi's own round-1 brief told agents to label results "Example" and add a pause control, both banned.

Give all design agents one shared chat-screen component in your product's own look, so nobody redraws a third-party messenger.

---

## Step 5. Round 1: three variants in parallel (about 40 minutes)

**(done on Givi)** Three directions plus the gallery took about 1 hour 45 minutes, from sub-agents launched in one message.

**Setup.** One sub-agent per direction, each with its own folder, its own local server (`python3 -m http.server <port> --bind 127.0.0.1`, because gstack `browse` refuses `file://`) and its own `BROWSE_STATE_FILE`. Designers run on a mid-tier model; the top model only for a genuinely new direction. **(learned the hard way)** About 37 top-model sub-agents over three days hit Givi's weekly usage cap and stopped two agents halfway through editing live files; the coordinator then did the fixes itself in about 40 minutes.

**Coordinator checks before the founder sees anything:**
1. Re-shoot each agent's "final" screens after animations finish; agents report optimistically.
2. A rule-check script built from `BANS.md` greps every page for banned words, labels, fonts and competitor names.
3. `$B js "document.documentElement.scrollWidth > innerWidth"` prints `false` at 390 and 1440 px; section positions do not move after animations.
4. Every number is read from the DOM. A screenshot of an animated counter can catch it mid-count.
5. Your own fixes pass `BANS.md` too. **(learned the hard way)** Givi's coordinator fixed a looping animation by adding a banned Replay button.
6. No personal files unless the founder supplied them for this. **(learned the hard way)** An agent built a direction around a portrait of Vito found on his computer and published it to the review link before he saw it.

**One private gallery link, one question.** Desktop and phone thumbnails of each direction with its headline and honesty notes, published to one private URL and republished to the same URL every round (a claude.ai artifact on Givi; any private static page works). Embed non-Google fonts as base64 `@font-face`, and check `document.fonts` on the published link in a fresh browser. **(learned the hard way)** Fonts that rendered locally failed twice on Givi's gallery link after "done" was reported. Ask "pick one or two; anything you hate?" with a recommendation, and keep working.

gstack `/design-shotgun` builds variants, a comparison board and structured feedback in one run **(recommended, not tested by us)**.

---

## Step 6. Round 2, then freeze (about 2 hours)

- Turn the founder's reply (often a voice note) into a numbered change list and address every point.
- **Ambiguous notes get 2-3 small options.** **(learned the hard way)** Givi read "the phone screens are not natural" as "draw real iPhones running a messenger app"; five hours later the founder said those screens ruined the design.
- Offer colour preferences as live swatches on the real page.
- **Fresh-eyes scoring (done on Givi):** reviewer sub-agents that never saw earlier versions score each page on the founder's acceptance tests while you measure sections, words and height. It cut pages from 1,200-1,900 words to about 600.
- **Model reviewers are not buyers.** Before paid traffic, show the phone view to 3-5 target buyers: "what does this do, who is it for, what would you tap?" **(recommended, not tested by us)** Givi's pages scored well with model reviewers, then only about 1 in 60 Meta visitors tapped Start, against 5-6% of direct visitors.
- **Freeze after round 2** and update `TASTE.md` with tokens, fonts, devices and dated screenshots the same day.
- **One language** until 3 payers, then only for a market with traffic and a booked native reader. **(learned the hard way)** Givi built a second language with custom fonts the evening it was asked: about 4-5 agent-hours for a page with no visitors.
- Decide on day 1 whether the app after sign-up shares the landing's look, from one canvas with the landing next to two app looks. Givi's app look flipped three times in five days.

---

## Design rules that stop a page looking AI-made

These generalise the two Givi pages Vito approved and every ban he set **(done on Givi)**. The middle column seeds `BANS.md`.

| Do | Never | Why (Givi) |
|---|---|---|
| Show the real product UI drawn in code (chat threads, approval cards, dashboards) as the proof | stock photos, illustrations of people, generic SaaS mockups, screens dressed as a third-party messenger | five concepts rejected as "AI slop" in one review |
| Show whole jobs step by step (find leads, make the offer, send it, get paid) | feature lists, small chores | small examples made the product look small |
| One signature device, used three or four times (a pen underline drawing in under each heading's key phrase; one word in a speech bubble) | a new trick in every section; coloured pills and chips | "don't shortcut on style" |
| Calm space: max width about 1220 px, varied section padding, cards only where a card is the right object, OKLCH colours with tinted neutrals | pure black or white, nested cards, identical icon-card grids | shared by both approved pages |
| Big type: body about 19-22 px on phones | small grey text | an early prototype was rejected as unreadable |
| Motion that just runs, with reserved height so nothing jumps | pause, stop, replay or "Play again" controls | "it's sloppy, we stay with motion" |
| Honest trust: a short text founder note, case cards (business type, city, what was built), a monochrome wall of real app logos (Simple Icons, CC0) | invented names, quotes, ratings or customer counts; the founder's photo unless they ask | fake reviews are banned under the UK DMCC Act 2024 |
| Plain words; who it is for; conditions said once in one quiet line | "Example", "sample" or "demo" labels; uppercase eyebrows over headings; decorative dots or badges with no fact; empty slogans; em dashes in copy | labels were removed as slop, then reintroduced by a later brief |
| One display currency | two currencies in one sentence | an ad mixed pounds and dollars |
| Real dates and limits only | "places are limited", seat counters, struck-through prices nobody paid | an agent added "places are limited"; it came off within two hours |

Run impeccable's critique or gstack `/design-review` before calling a page done. **(done on Givi)** A critique found a "Continue with Google" button that showed "You're in" without creating an account, an hour after the page was declared ready for paid traffic.

---

## Tools

| Job | Tool | Notes |
|---|---|---|
| Building pages | Anthropic's `frontend-design` skill; the `impeccable` design skill (github.com/pbakaus/impeccable) | `frontend-design` with no references produced generic pages on Givi. After impeccable loads, run `git status`: the version we used renamed a design-context file and edited `.gitignore` |
| Day-0 design system | gstack `/design-consultation` | font and colour preview **(recommended, not tested by us)** |
| Review and fix | gstack `/design-review`, impeccable critique, gstack `/qa` | taste and function are separate checks: five fully QA'd concepts were rejected in seconds |
| Screenshots, DOM reads | gstack `browse` | recipe below |
| Real clicks with consent and ad scripts | the Claude in Chrome extension, in a venture browser profile, plus a private window | headless browsing misses consent-dependent behaviour |
| Scripted QA, pixel checks | Playwright with a clean context | proves pixels fire only after Allow |
| Page weight and load time | gstack `/benchmark` at phone width | **(recommended, not tested by us)** |
| Brand logos | Simple Icons (`cdn.jsdelivr.net/npm/simple-icons`), inlined as SVG | swap wordmarks unreadable at tile size |

Screenshot recipe:

```bash
B=~/.claude/skills/gstack/browse/dist/browse
$B viewport 390x844
$B goto "https://<domain>/?utm_source=qa"
$B js "document.querySelectorAll('.reveal').forEach(e => e.classList.add('in'))"   # end state of entrance animations
$B js "document.documentElement.scrollWidth > innerWidth"                        # must print false
$B js "[...document.querySelectorAll('[data-count]')].map(e => e.innerText).join(' | ')"
$B js "document.getElementById('pricing').scrollIntoView()"
$B screenshot --selector '#pricing'
```

The selector must match exactly one element, scrolled into view first, or the capture is blank. The headless browser cannot emulate dark mode, so inject the dark CSS to check it. Use `utm_source=qa` on test visits so counters exclude them.

---

## Step 7. Port to production (1-2 hours)

**(done on Givi)** Most of this shipped on 4 Oct as one readiness release.

- **Price:** none until the offer is accepted; then filled at build time from `bd/offer.md` (or a server-side token if the app serves the page) and pinned by a test.
- **Head:** a 2-4 word `<title>`; `og:title`; `og:description` with no price; `og:image` per page at 1200 x 630 with an absolute URL; `twitter:card` set to `summary_large_image`; canonical on the apex; an inline SVG favicon in brand colours; Google Fonts with `display=swap`.
- **Link previews:** render the OG image from an HTML artboard using the page's CSS (`$B screenshot --selector '#og'`). After each change, re-scrape in the Facebook Sharing Debugger (developers.facebook.com/tools/debug) and LinkedIn Post Inspector (linkedin.com/post-inspector), which cache aggressively, then send the link to yourself in a chat app and look. Replace the OG image and favicon in the same pull request as any redesign.
- **Site files:** `robots.txt` keeping the app out; a sitemap; `www` 301 to the apex keeping path and query; privacy, terms, refund and support pages.
- **Fallback and preview routes are public pages:** retire them or audit their claims. **(learned the hard way)** Givi's old home page, still reachable at a preview route, kept "1,000+ tools" six times after the live page was fixed.
- **Budgets and hygiene:** a page-weight and Largest Contentful Paint limit for phone in-app browsers (Givi's next screen after Start autoplayed a 5.5 MB film); the licence recorded next to every font and icon set; text contrast on brand colours, alt text, tap targets of at least 44 px.
- **Verify from outside:** `curl -s -A "<iPhone Safari UA>" https://<domain>/ | grep -E "<headline>|og:image|<price>"`; `curl -sI "https://www.<domain>/x?y=1"` shows a 301 keeping the query; screenshots at 1440 x 900 and 390 x 844.

**A real input in the hero** **(done on Givi, on day 25)**: a box ("What job would you hand a new hire?", later a website-or-Instagram box that starts a study of the business) saved through sign-up, so the first session starts from it. Every Start button scrolls to it. Watch it work on production in a real browser with cookies allowed: an ad-click script held Givi's Start clicks and followed the link anyway, and the scroll was never seen working live.

---

## Step 8. The in-app browser test and sign-in on your own domain

**(learned the hard way)** Paid traffic from Instagram, Facebook and TikTok opens inside each app's built-in browser. On Givi, 44 of 45 people who clicked Start left at a sign-in screen that said "continue to <project>.supabase.co", which looks like a scam to a stranger. Two days later the team found Google refuses sign-in inside Instagram's browser. Both were found after the ads launched.

### Google sign-in fails inside in-app browsers

Google blocks OAuth in embedded webviews (error `403: disallowed_useragent`), and the Instagram, Facebook, TikTok and LinkedIn in-app browsers are webviews (checked 13 Oct 2026).
- Detect in-app browsers by user-agent family: Instagram's contains `Instagram`, Facebook's `FBAN` or `FBAV`, TikTok's `musical_ly` or `Bytedance`, LinkedIn's `LinkedInApp`. Confirm against your own logs; Givi's first detection missed TikTok.
- There, make email sign-in with a typed code the main button and never auto-start Google. A magic link opened in another browser fails the PKCE check.
- For paid traffic, make checkout the sign-up (the framework's default; see `06-payments-stripe.md`): Stripe Checkout collects the email and the account is created from the Checkout session **(done on Givi, on day 25)**.
- Keep the in-app check in one helper used by every sign-in and sign-up screen. **(learned the hard way)** A new card-trial step brought "Continue with Google" back as Givi's main button, and the first paid lead hit it.
- Anything typed before sign-in must survive a switch to Safari or Chrome. Show the cookie banner on phones only after the first scroll (Givi used 240 px), so it never covers the main button.

### Your domain on the sign-in screen

With Supabase Auth **(done on Givi through the dashboard: about an hour plus a 6-minute verification; the CLI commands below are recommended, not tested by us)**. Set this up on first-deploy day; the founder's Google branding clicks fall in sitting S3b.
1. Enable the custom domain add-on ($10 a month on a paid plan, Supabase pricing checked 13 Oct 2026), then run `supabase domains create --project-ref <ref> --custom-hostname auth.<domain>`.
2. In Cloudflare DNS add a CNAME `auth` to `<ref>.supabase.co` (DNS only) and the `_acme-challenge.auth` TXT record it printed.
3. Run `supabase domains reverify --project-ref <ref>` until verified, then `supabase domains activate --project-ref <ref>`. A 401 from `https://auth.<domain>/auth/v1/health` without a key means it is serving. Point the app's auth URL at it and redeploy.
4. Google Cloud console > Google Auth Platform: under Clients, a Web client with redirect URI `https://auth.<domain>/auth/v1/callback`; under Branding, the app name, a 120 x 120 logo, only your domain as authorised domain, and a support email from the venture's own Google account; scopes `openid`, `email`, `profile` only; under Audience, Publish app (In production); then Verification Center > Verify branding > Publish branding. Instant on Givi with basic scopes; a manual review can take 2-3 business days. Full steps in `05-product-and-infra.md`, section 6.
5. Screenshot the consent screen: your logo and "continue to <Brand>".

Other auth providers offer the same under "custom domain" or "auth domain" **(recommended, not tested by us)**.

### The real-phone test (about 5 minutes in sitting S3b, before any ad)

Givi never ran this before its ads **(recommended, not tested by us)**. First the app-side check: gstack `browse` at `390x844` with each in-app user agent (`$B useragent '<UA>'`) through to the sign-in screen. It checks only your own detection and layout. Then the real test: the founder sends the landing URL with UTMs to themselves in an Instagram DM, a Messenger chat and a TikTok DM, opens it inside each app and finishes a sign-up with the typed code; the agent saves a screenshot of every step, consent screen included. Meta Ads Manager's "send preview to device" does the same for a real ad. Re-run it when a release touches a sign-in surface.

---

## Step 9. Tracking done right

**(learned the hard way)** Givi redesigned its counting four or five times on live data. The day before launch it reported about 370 "visitors", mostly cloud scanners posing as iPhones. Google's campaign and keyword tags sat after a `#` and never reached the server. About 5% of visitors accepted cookies. One day about 260 paid clicks produced about 85 visits, and nobody found out why. Write the measurement spec before the first visitor.

**UTMs before any `#`.** Every link carries `utm_source`, `utm_medium`, `utm_campaign` and `utm_content`, and the query comes first:

```
https://<domain>/?utm_source=meta&utm_medium=paid_social&utm_campaign=test-us&utm_content=static-a#pricing
```

Everything after `#` stays in the browser. Google Ads appends its tracking template to the final URL, so a final URL ending in `#anchor` swallows it. Lint every final URL for a `#` before a `?`, and test one through Google's tracking template before launch.

**First-touch attribution.** A first-party cookie stores UTMs, `gclid`, `fbclid`, `ttclid`, referrer and page variant; copy it onto the account at sign-up and into Stripe Checkout metadata. Keep the query string through sign-in redirects and email links. **(learned the hard way)** Givi lost two weeks of channel learning there.

**Count humans, on the server** **(done on Givi)**. A visit counts only after a scroll, tap, keypress, mouse move or 15 seconds open, once per browser:

```html
<script>
(function () {
  var sent = false;
  function seen() {
    if (sent) return; sent = true;
    navigator.sendBeacon('/seen', JSON.stringify({ path: location.pathname, q: location.search, ref: document.referrer, wd: !!navigator.webdriver }));
  }
  ['scroll', 'pointerdown', 'keydown', 'mousemove', 'touchstart'].forEach(function (e) { addEventListener(e, seen, { once: true, passive: true }); });
  setTimeout(seen, 15000);
})();
</script>
```

Exclude the team (a cookie set when they open the app or admin pages, their IP for 7 days, test UTMs such as `utm_source=qa`), automated browsers, link-preview fetchers and ad-review robots. Read the client IP from your host's real header in one shared function. **(learned the hard way)** On Railway that is `X-Real-IP`; the last `X-Forwarded-For` hop is Railway's own proxy, so Givi's team filter failed until probed live. Verify: a plain fetch adds 0, a beacon adds 1, a repeat adds 0, a team probe adds 0.

**Funnel steps on the server,** per page, source and ad: engaged visit, Start click, sign-in shown, Google tapped, came back, error, code sent, sign-up, first job, checkout, charged, refunded, each with the in-app flag. Compare the ad platform's link clicks and landing-page views with your engaged visits per ad; an unexplained gap is a defect (in-app load time, bots, the consent wall).

**A consent loader that does not blind you.**
- One plain sentence with two equal buttons, "No thanks" and "Allow"; no platform names in the banner; the privacy page names each platform and event. **(learned the hard way)** About 95% of visitors never pressed Allow on Givi's first, unequal banner.
- One loader injects every planned platform's tag only after Allow; all pixels and the banner ship in one pull request.
- Google Consent Mode v2, basic mode, for UK and EEA traffic: `gtag('consent', 'default', {...})` with `ad_storage`, `ad_user_data`, `ad_personalization` and `analytics_storage` set to `denied`, then `gtag('consent', 'update', {...})` to `granted` on Allow (Google's docs, checked 13 Oct 2026) **(recommended, not tested by us)**.
- Server-side conversion events only for consenting visitors, with hashed email and click IDs.
- Test with Meta's test events, TikTok's test event code and Google Tag Assistant. **(learned the hard way)** Givi's check fired a fake sign-up into three live dashboards.
- Expect low consent, and decide on your server counts.

**See what visitors do.** Session replay after Allow: Microsoft Clarity (free; since 31 Oct 2025 it needs a consent signal for EEA, UK and Swiss visitors) or PostHog. Alert when a paid source's Start rate falls below about a third of direct traffic's after 100 visits **(recommended, not tested by us)**. Givi found its 1-in-60 Meta Start rate a week into ads.

---

## Step 10. No split test below about 1,000 visitors per arm

**(learned the hard way)** Givi split traffic between two finalists for 8 days on about 280 visitors each; it ended 16 sign-in clicks against 14. The agent had written on day one that the test could not give an answer in time. Ads were later mapped to pages by promise, so the pages also got different audiences, and every copy change meanwhile touched up to 8 files.

Visitors needed per arm (80% power, 5% significance, two-sided):

| Start rate now | To detect | Visitors per arm |
|---|---|---|
| 5% | 10% | about 440 |
| 6% | 9% | about 1,200 |
| 5% | 7.5% | about 1,500 |
| 2% | 3% | about 3,800 |
| 5.2% | 5.7% (Givi's gap) | about 32,000 |

No split unless about 1,000 visitors per arm are reachable within 14 days, roughly 70 engaged visitors per arm per day. Below that, run one page and change it in sequence, judging each change on server-counted Start rate with the sample size stated. Before 3 payers, the capped paid test is one ad set with 2-3 static ads in one market, all sending traffic to one page.

If you do split: assign server-side with a sticky cookie; count `?v=` forced views separately; freeze copy or log change times; and write a stop date, a stop rule the traffic can reach, and who ends the test, on launch day. Mapping ads to pages ends the randomisation.

---

## Step 11. The gate before ads, and keeping the page true

**Before any ad money: the funnel gate** (G5 in `01-framework.md`), run by the revenue owner, a session that neither runs the ads nor built the sign-up path **(recommended, not tested by us)**. The bar is never lowered:
- Sign-up finished from a DM link inside the Instagram, Facebook and TikTok in-app browsers on a real phone (sitting S3b), with the branded consent screen on `auth.<domain>` captured.
- At least 20 organic Start clicks, 25% or more reaching an account, humans only, on the server. If fewer arrive, the gate stays closed.
- The founder's real card payment and refund seen by the agent in Stripe and in the database (sitting S3b; see `06-payments-stripe.md`).

Checks the same session runs alongside the gate:
- Every CTA on every variant clicked in a real browser, signed out, cookies allowed; the whole funnel walked as a new visitor to the payment screen.
- Claims grep clean on every served page; each ad's promise and final URL match its page with no `#` before the UTMs; session replay and per-source Start rate live.

**After every copy release:** live-grep the served HTML for retired claims (expect zero) and the expected price, ideally as a test that fails the build when a retired claim reappears on any served file; tell the ads and social owners about corrected claims within the hour; refresh the private gallery of live pages by script (Givi did about ten refreshes by hand at 15-20 minutes each); keep an outside watcher (an uptime keyword check or a scheduled cloud job, never a check inside an agent session) that fetches every landing URL with a phone user agent and alerts on a missing headline, an unfilled price token, a returned claim or a non-200; verify the domain in Google Search Console and submit the sitemap.

---

## What needs the founder

| Action | How to make it take minutes |
|---|---|
| Taste lines and a pick from 8-10 references (day 0) | numbered lines with defaults, one private reference page (10 min) |
| Pick between directions (two rounds) | one link, phone and desktop thumbnails, one question with a recommendation; a voice note is fine |
| Approve any personal asset (photo, name, story) | ask with the exact asset and where it goes, before any link, even a private one |
| Confirm proof is real | list case cards as the founder described them; never invent people |
| Introduce 3-5 buyers for a 5-second test | one forwardable message with the phone link and three questions |
| Real-phone in-app sign-up test (S3b) | the URL and a 4-line script, about 5 minutes |
| Google branding clicks (S3b) | the console open on the right page, the logo file ready, about 5 minutes |

Removing a false claim needs no approval: agents fix every surface the same day and show before-and-after screenshots in the daily digest.

---

## Checklist

- [ ] One landing owner; static hosting separate from app releases
- [ ] `bd/TASTE.md` and `bd/BANS.md` committed on day 0 and referenced from `CLAUDE.md` and `AGENTS.md`; bans seeded with the generic tropes and the founder's own
- [ ] Capability ledger with owner-visible status and live dates; job chains and offer file written; every value claim has a basis
- [ ] Smoke page with the job and a waitlist live on day 0-1, no price before the offer is accepted
- [ ] Reference scout and take/avoid table committed; shared brief grep-checked against `BANS.md`
- [ ] Round 1: three variants in parallel, each with its own folder, port and browse state
- [ ] Coordinator checks: re-shot after animations, ban grep, overflow and layout shift, numbers from the DOM, own fixes checked, no personal files
- [ ] One private gallery link, same URL each round, fonts checked on the published link
- [ ] Ambiguous notes answered with options; frozen after round 2; `TASTE.md` updated the same day
- [ ] 3-5 target buyers shown the phone view before paid traffic; one language until 3 payers
- [ ] Production head, 1200 x 630 OG images, favicon, robots, sitemap, `www` redirect and policy pages; previews re-scraped
- [ ] Fallback routes retired or audited; licences recorded; accessibility and page weight checked
- [ ] Hero input carried through sign-up and seen working on production
- [ ] In-app detection in one helper; email code first in in-app browsers; Google never auto-started
- [ ] Sign-in on `auth.<domain>`; branding verified and published; consent screen captured
- [ ] Real-phone sign-up finished inside Instagram, Facebook and TikTok in-app browsers (S3b)
- [ ] UTMs before any `#`; final URLs linted; Google tracking template tested
- [ ] First-touch cookie on the account and in checkout metadata
- [ ] Humans-only server counting probed; real client IP header used; funnel steps logged with the in-app flag; clicks compared with visits per ad
- [ ] Equal-weight consent banner; one loader after Allow; Consent Mode v2 defaults; test-event modes used
- [ ] Session replay after consent; per-source Start-rate alert
- [ ] No split below about 1,000 visitors per arm in 14 days; otherwise stop date, reachable rule and owner written
- [ ] Funnel gate (G5) passed and recorded by the revenue owner, a session that neither runs ads nor built sign-up: real-phone in-app sign-up, 20 organic Start clicks with 25% reaching an account, real card payment and refund seen
- [ ] Claims grep after every release; gallery refreshed; outside watcher running; Search Console verified
