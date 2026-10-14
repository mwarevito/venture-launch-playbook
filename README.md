# Venture Launch Playbook

I launched Givi (heygivi.com), an AI assistant for owners of small teams, over 26 calendar days, as a side experiment alongside my other work. Almost all of the work was done by Claude Code and Codex: about 190 agent sessions and about 360 pull requests. We built two products and threw one away, and spent about £110 on ads. At the end of those 26 days we had zero paying customers.

Only about 2.5 of those 26 days were real waits on someone else: registering the company, Meta's business verification, ad reviews. The rest went to three mistakes:
- the agents built a different product from the one I asked for on day 0 (about 7.5 days);
- selling started late (no warm messages, no cold emails);
- ads went to a sign-in screen that did not work for about 5 days.

My own part was an estimated 75 hours across those 26 days, nowhere near full-time, and most of it went on passing information between agent sessions.

Afterwards I had agents read every session transcript and write down what we did, which tool we used for each step, what broke and how we fixed it. Separate reviewer agents then took it apart: what should have been done better, and faster.

This repo is the result, packaged as a skill your own agents can run. With the same tools and new accounts, I think a launch like this takes 6-8 days to a working paid funnel, or 2-3 days if you already have a verified company. After that it takes about 30 minutes a day of your time. The mistakes are in here too, because they are the useful part.

Vito

## What is inside

One agent skill, `launch-venture`: a short entry file plus 16 guides that the agent opens when a step needs them.

| Guide | What it covers |
|---|---|
| [The story](skills/launch-venture/references/00-the-story.md) | What happened, where the 26 days went, the 10 changes for next time |
| [Framework](skills/launch-venture/references/01-framework.md) | Who does what (one operator session, builders, reviewers), phases with "done when" gates, three founder sittings, cadence, metrics, paste-ready prompts |
| [Day 0 accounts](skills/launch-venture/references/02-day0-accounts.md) | Every account from zero, in dependency order: domain, DNS, Google Workspace and email authentication, GitHub, hosting, database, Stripe, socials, Meta, Google and TikTok ad accounts |
| [Positioning and pricing](skills/launch-venture/references/03-positioning-pricing.md) | One market, one buyer, one paid job; name screening; pricing from a one-hour cost test; freezing the offer |
| [Landing pages](skills/launch-venture/references/04-landing-pages.md) | Getting design taste in 10 minutes, design rules that avoid the AI look, in-app browser tests, honest tracking |
| [Product and infrastructure](skills/launch-venture/references/05-product-and-infra.md) | A live spike by day 2, Railway, Supabase, sign-in on your own domain, CI, reviews and releases |
| [Payments](skills/launch-venture/references/06-payments-stripe.md) | Stripe from account to live: checkout as sign-up, trials, webhooks, refunds, the real-card test |
| [Channels and integrations](skills/launch-venture/references/07-channels-integrations.md) | Telegram and Slack bots, the WhatsApp AI policy, connected apps |
| [Outreach](skills/launch-venture/references/08-outreach.md) | Warm outreach first, LinkedIn by hand, cold email with Instantly step by step, compliance, pipeline |
| [Content, video, anti-slop](skills/launch-venture/references/09-content-video-anti-slop.md) | Why a 20-minute static beat 30-40 hours of films, the anti-slop checklist, motion video with code, platform specs |
| [Paid ads](skills/launch-venture/references/10-paid-ads.md) | Meta, Google and TikTok setup, the funnel gate before any spend, a capped first test, delivery alarms |
| [Platform approvals](skills/launch-venture/references/11-platform-approvals.md) | Business verification, Meta App Review, the Claude and ChatGPT directories, the long-lead table |
| [Running the agents](skills/launch-venture/references/12-running-agents.md) | Organizing Claude Code and Codex sessions, permissions, secrets, browser automation, memory |
| [Daily operations](skills/launch-venture/references/13-daily-ops.md) | The morning digest, watchdogs, the weekly review, metrics and decision rules |
| [Company and legal](skills/launch-venture/references/14-company-legal.md) | Company, bank, VAT basics, policy pages, subscription rules (orientation, not legal advice) |
| [Toolbox](skills/launch-venture/references/toolbox.md) | The MCP servers, skills, command-line tools and services we used, with verdicts |

Every step carries one of three tags:
- **(done on Givi)**: we did it and it worked.
- **(learned the hard way)**: we got it wrong first.
- **(recommended, not tested by us)**: reasoned from the launch and from current docs.

Facts that change often (prices, console paths, review times) carry the date they were checked.

## Install

**Claude Code (plugin):**

```
/plugin marketplace add mwarevito/venture-launch-playbook
/plugin install launch-venture@venture-launch-playbook
```

**Any agent that reads the Agent Skills format** (Claude Code, Codex, Cursor and others), using the `skills` installer:

```
npx skills add mwarevito/venture-launch-playbook
```

**By hand:** copy `skills/launch-venture/` into `~/.claude/skills/` for Claude Code, or into `~/.agents/skills/` for Codex.

## Use it

Start a new session and describe your idea:

```
Start a new venture using the launch-venture skill. You are the operator and my only contact.
Send me the intake questions as one message, start the market research while I answer,
and do not start building until the brief holds my asks, the product bar and a kill rule.
My idea: <your idea in your own words>
```

The agent works from the framework. It sends you a short set of questions, then batches everything only you can do (passwords, ID checks, cards, approvals) into three prepared sittings. From the first public page onward it sends you one daily digest.

## What this is not

- **Not a promise.** Givi had no paying customer when this was written, so the conversion steps are our best reasoning, not proof.
- **Not legal or tax advice.**
- **A snapshot of October 2026.** Tools, prices and platform rules move. The skill tells the agent to re-check before relying on a number.

## License

MIT. Use it, fork it, adapt it. If it helps you launch something, I would like to hear what you changed.
