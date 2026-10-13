---
name: launch-venture
description: Launch and run a new online business from zero with AI coding agents (Claude Code, Codex), using a framework and field-tested playbook from a real 26-day SaaS launch. Use when starting a new venture, product or brand; setting up accounts from scratch (domain, Google Workspace email, Stripe, hosting, database, socials, Meta and Google ad accounts, platform approvals); planning or sequencing a launch; running cold or warm outreach (including Instantly); making ad creative, motion video and social content that does not look like AI slop; or setting up the daily operating cadence for the first weeks.
---

# Launch a venture with agents

This skill turns one founder plus AI coding agents into a launch team. It comes from a real launch, Givi (heygivi.com), an AI business-assistant SaaS built and launched in 26 days with Claude Code and Codex. It includes what worked, what went wrong, and how to do it faster.

All the detail lives in `references/`. Read only the file the current step needs.

| File | Use it for |
|---|---|
| `references/00-the-story.md` | What happened on the real launch, where the time went, the top 10 changes. Read once before planning. |
| `references/01-framework.md` | **The plan.** Operating model, phases with "done when" gates, founder sittings, cadence, metrics, paste-ready prompts. |
| `references/02-day0-accounts.md` | Every account from zero, in dependency order: domain, DNS, Google Workspace, email auth, hosting, database, Stripe, socials, ad accounts. |
| `references/03-positioning-pricing.md` | One market, one buyer, one paid job; name screen; pricing from a cost test; freezing the offer. |
| `references/04-landing-pages.md` | Taste intake, design rules that avoid the AI look, in-app browser tests, tracking. |
| `references/05-product-and-infra.md` | Spike by day 2, architecture, Railway, Supabase, auth on your own domain, CI and releases. |
| `references/06-payments-stripe.md` | Stripe from account to live: Checkout as sign-up, trials, webhooks, refunds, the real-card test. |
| `references/07-channels-integrations.md` | Telegram and Slack bots, WhatsApp policy, connected-app integrations. |
| `references/08-outreach.md` | Warm outreach first, LinkedIn by hand, cold email with Instantly, compliance, pipeline. |
| `references/09-content-video-anti-slop.md` | Statics, real-work recordings, motion video with code, platform specs, the anti-slop checklist. |
| `references/10-paid-ads.md` | Meta, Google and TikTok setup, the funnel gate before spend, a capped first test, delivery alarms. |
| `references/11-platform-approvals.md` | Business verification, App Review, directory listings, the long-lead table. |
| `references/12-running-agents.md` | How to organize Claude Code and Codex sessions, permissions, secrets, browser automation, memory. |
| `references/13-daily-ops.md` | The daily digest, morning check, watchdogs, weekly review, metrics and decision rules. |
| `references/14-company-legal.md` | Company, bank, VAT basics, policy pages, subscription rules (orientation, not legal advice). |
| `references/toolbox.md` | MCP servers, skills, CLIs and services, with verdicts and alternatives. |

## How to run a launch

1. Read `references/01-framework.md` fully, then `references/00-the-story.md`.
2. Act as the **operator**: the founder's only contact for this venture. Send the founder intake from the framework as one message. While the founder answers, start the market research and check which accounts already exist.
3. Write the brief (`decisions/brief.md` in the venture repo) before any build starts. It must hold the founder's day-0 asks, word for word, as acceptance criteria, plus the product bar and a kill rule.
4. Open one tracked item per long-lead step (verifications, reviews, company registration) with a re-check date. Start every waiting clock in the first hour its prerequisite exists.
5. Batch everything only the founder can do (passwords, 2FA, ID, cards, approvals) into the three prepared sittings described in the framework. Never trickle requests through the day.
6. Work through the phases. Before each one, open the reference file it names and follow that file's steps and checklist.
7. From the first public URL, run the daily cadence in `references/13-daily-ops.md`.

## Ground rules

- **Selling starts on day 1, alongside building.** Warm outreach goes out on the day friends can first use the product. No ad spend until the sign-up works on a phone inside the Instagram, Facebook and TikTok in-app browsers, and one real card payment and refund have gone through.
- **The founder decides identity, money, taste and offer, first contact with people they know, and anything said in their name.** Agents decide and log everything else, and every question to the founder carries a recommendation and a default.
- **Secrets never pass through chat.** Hand the founder a small local script that reads the key, checks it with the provider, stores it, and prints only its name.
- **Re-check before relying on a number.** Console paths, prices and review times change. Each reference file says when its facts were checked.
- **Evidence tags.** Steps are tagged (done on Givi), (learned the hard way) or (recommended, not tested by us). Treat the last kind as a starting point to verify.
