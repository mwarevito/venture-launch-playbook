# Payments with Stripe, from zero to the first real payment

A subscription product needs very little billing to take its first dollar: Stripe Checkout as the sign-up, a small webhook, the customer portal and one table that says who has access. This file takes you from an empty Stripe account to live payments, with the agent doing almost all of it and the founder spending about 30 minutes across three short sittings (S1a, S2 and S3b), plus the money and tax decisions. Refund buttons, top-ups and plan ladders wait until someone has paid.

**Done when:** a live Stripe account can charge and pay out; the app creates its own product, prices, webhook and portal from one key in both sandbox and live; every offer has passed a live preflight (a Checkout session created, read and expired); and the founder has paid with a real card, been refunded, and the agent has seen the refund in Stripe and in the app's database.

Stripe facts here were checked against docs.stripe.com and support.stripe.com on 13 Oct 2026. Dashboard menus move: if a path below is missing, type the setting's name into the dashboard search bar.

---

## What happened on Givi

- Stripe was never the slow part. Activation finished without anyone waiting on it. The slow parts were a late go-live decision, a live-key hand-off that took about 3 hours, and a founder-only real-card test that never happened.
- Billing was built twice. The first build (refund and dispute holds, a guarantee state machine, credits, a webhook handling 23 event types) took about 2.5 agent-days and was thrown away when the product changed direction, before anyone had paid. The replacement took one agent about 16 minutes. **(learned the hard way)**
- The offer changed four times in about two weeks with zero payers. Each change meant code, terms, landing and ad edits, and all ads were paused once because images still showed the old price. **(learned the hard way)**
- The only production service was switched to the live key with no sandbox copy kept. Every later billing feature was checked only against a fake Stripe in tests and live "create, then expire" sessions; none completed a real Checkout. **(learned the hard way)**
- The real-card-and-refund test was offered as optional at least four times and never run. Paid ads ran for five days without it. By 12 Oct 2026 Givi had no paying customers.

---

## 1. The first-dollar cut

| Build before the first payment (Tier 0) | Build after the first payer (Tier 1) |
|---|---|
| Stripe account, agent access to a sandbox, one `ensure()` setup for sandbox and live | Self-serve "Refund and cancel" button |
| Checkout in subscription mode, used as the sign-up | Top-ups, credits, auto top-up |
| A webhook for about 8 events (section 9) | Plan ladders, upgrades with proration |
| The customer portal for cancel and card change | Early-bird caps, locked prices |
| One entitlement table: source is `stripe`, `trial` or `comp` | Lifecycle runners and guarantee engines |
| Dunning, Radar and dispute settings; policy pages; a tax and seller-of-record decision | Dunning emails beyond Stripe's own |

Until the refund button exists, an agent refunds inside the published refund window from the dashboard or the API, under a written standing permission from the founder. If even Tier 0 is too much for one pilot customer, send a Stripe Payment Link: a real payment with no billing code. **(recommended, not tested by us)**

---

## 2. Decide the money basics once

The agent writes each option in one plain sentence with a recommendation; the founder answers in about 15 minutes. Record the answers with dates in one offer file (for example `bd/offer.md`). Sandbox billing code can start before the answers, as long as every value lives in configuration.

| Decision | Recommendation |
|---|---|
| Seller of record | See the comparison below; decide with an accountant by sitting S2, before any ad account exists (F9 in `01-framework.md`) |
| Currency | One checkout currency for prices, ad accounts, budgets and ad copy. Never two currencies in one sentence |
| Launch price | One variable that the app, landing, terms and ad text all read. Never inside an image or video |
| Trial mode | Build card trial, no-card trial and no trial behind one config value; pick one (section 7) |
| Refund window | For example 14 days on the first payment; refund and cancel together |
| Who you sell to | Businesses only, or consumers too. Consumers bring consumer law (section 7) and VAT duties (section 11) |
| Founder's own position | A yes or no, checked with an accountant, on taking revenue through this company |

**Plain Stripe or Stripe Managed Payments** (checked 13 Oct 2026):

| | Plain Stripe (your company sells) | Managed Payments (Stripe is the merchant of record) |
|---|---|---|
| VAT and sales tax | Yours. Stripe Tax can calculate and collect; you register and file | Stripe's, in more than 80 countries |
| Extra fee | Stripe Tax: 0.5% per transaction where you are registered | 3.5% per successful transaction, on the full amount including tax, on top of processing fees |
| Fraud, disputes, buyer support | Yours (Radar available) | Included for eligible card disputes; transaction-level support by Stripe |
| Works with | Checkout, Elements, Payment Links, invoices | Checkout and Payment Links only; subscriptions need Billing; no Connect |
| Eligible products | Anything Stripe allows | Fully automated digital products (SaaS, software, AI services, digital media). Not consulting, marketing, design, development or support services, nothing with live human delivery |
| Business locations | All Stripe countries | US, Canada, the UK, most of the EU, Switzerland, Norway, Australia, Hong Kong, Japan, Singapore |
| Product setup | Tax code optional (needed for Stripe Tax) | Every product needs an eligible tax code, or Checkout fails |

Eligible codes include `txcd_10103001` (SaaS, business use) and `txcd_10105002` (AI as a service, cloud, business use). Stripe can withdraw Managed Payments later if it decides a product involves human work.

On Givi the sandbox ran under Managed Payments, so Checkout failed with a generic error until the product got a SaaS tax code (found in Stripe's request log). **(learned the hard way)** The agent quotes Stripe's docs and the current fee when it presents this choice, never only its own summary, and checks which model live mode uses.

---

## 3. Create and activate the account

**Timing:** the account takes 5 minutes and comes with a sandbox; create it in sitting S1a. Activation takes the founder about 10 minutes, but it needs the company's bank account for payouts, so on a new company it waits for the bank (often days). Do the identity checks in sitting S2, the day the company number arrives, and add the payout account the day the bank details exist. Stripe can come back with follow-up requests; on Givi it asked for nothing further.

1. **Create the account** at dashboard.stripe.com/register with a company-owned email (for example `billing@yourdomain.com`). Turn on two-factor authentication with a passkey or security key, which Stripe recommends over SMS. **(done on Givi)**
2. **Verify the business** at dashboard.stripe.com/account/onboarding: legal entity, registration number and address; the representative's identity; the payout bank account; a product description and the website. Keep one identity file open (legal name, number, addresses, support inbox) so every console form gets the same values. **(done on Givi)**
3. **Public details** (dashboard.stripe.com/settings/public): business name, website, support email, phone, address and statement descriptor. Customers see these on receipts and card statements. The descriptor is 5-22 Latin characters and must be recognisable (for example `YOURBRAND.COM`); an unrecognised statement line becomes a dispute. **(done on Givi)**
4. **The website review.** Stripe checks the site at activation and afterwards. It must show the business name, a description of what you sell that matches what you told Stripe, contact details (an email plus at least one more channel, not only a form), a refund and cancellation policy, terms, and the terms of any promotion. Publish these pages before submitting. **(recommended, not tested by us)**
5. **The country is permanent.** After activation you cannot change the account's business country.
6. **Verify from code:** `GET /v1/account` returns `charges_enabled` and `payouts_enabled` true. Show this on the app's admin page.

### Account settings for the same week

None of these were set or checked on Givi. Each takes a few minutes; the agent can click them while the founder is signed in. **(recommended, not tested by us)**

| Setting | Where | What to set |
|---|---|---|
| Failed-payment retries | Billing > Revenue recovery > Retries | Smart Retries on (Stripe suggests 8 tries in 2 weeks). After the last retry: **cancel the subscription**. "Leave past due" lets a non-payer keep access for as long as your app allows `past_due` |
| Customer emails | Settings > Customer emails, and the Billing email settings | Receipts, refunds, failed payments, trial-ending reminder (check its timing against your trial length) |
| Radar | Radar > Rules | Block or review repeated declines from one card, email or IP; 3D Secure on elevated risk. A Checkout that charges nothing today is a classic card-testing target |
| Branding | Settings > Branding | Icon, colour and logo for Checkout and the portal |
| Payouts | Settings > Payouts | Schedule and currency. USD prices paid into a GBP account pay a conversion fee |
| Disputes | Notification preferences | Who gets the dispute email, and what evidence you will send (terms, sign-up record, usage log) |

---

## 4. Sandbox, test mode and live

Stripe renamed its test environments. As of 13 Oct 2026:

| Environment | What it is | Use it for |
|---|---|---|
| Test mode sandbox | The original "test mode". Shares many settings with live, so a change there can change live. Cannot be deleted | Avoid for new integrations |
| General sandboxes (up to 5) | Isolated settings and data copied from live at creation, own keys, deletable, can be private | Development, CI and a permanent staging service |
| Live mode | Real cards, real money | Production only |

Keys show the mode: `sk_test_`, `rk_test_`, `pk_test_` versus `sk_live_`, `rk_live_`, `pk_live_`. Objects never cross modes.

- **Never hard-code price IDs.** Givi's first test price vanished when its sandbox was deleted. Look prices up by `lookup_key` (section 6). **(learned the hard way)**
- **Keep a permanent staging service on sandbox keys after going live.** Before the live switch, clone the production service with its own database, sandbox key and webhook, and complete one real sandbox Checkout there for every billing change. **(learned the hard way)**
- Sandboxes do not email customers by default; send receipts manually from the dashboard to check them.

---

## 5. Agent access without pasting secrets

On Givi, agents waited about 20 hours for permission to move one test key, and a webhook secret ended up pasted into chat. Set these routes up in sitting S1a, where the Stripe account is created.

**The Stripe CLI, for sandbox work.** Install with `npm install -g @stripe/cli`. The founder runs `stripe login` once and confirms in the browser; the agent then has sandbox access without anyone copying a secret. Stripe's docs now also suggest `stripe agent setup`, which installs Stripe's agent skills and MCP configuration for the coding agents it finds, and `stripe sandbox create` for an anonymous 7-day sandbox that can be claimed later. No Claude session used the CLI on Givi. **(recommended, not tested by us)**

**The Stripe MCP server, for reads, audits and docs** (checked 13 Oct 2026):

```bash
claude mcp add --transport http stripe https://mcp.stripe.com/   # then /mcp to sign in with OAuth
codex mcp add stripe --url https://mcp.stripe.com
```

Tools: `stripe_api_search`, `stripe_api_details`, `stripe_api_read` (any GET), `stripe_api_write`, `get_stripe_account_info`, `search_stripe_documentation`, `stripe_implementation_planner` and an analytics tool. OAuth grants live and sandbox access separately. Some writes, such as refunds, wait for a human to click a confirmation link. From 31 Oct 2026 the server refuses plain secret keys and untagged restricted keys: use OAuth, or an "agent key" (a restricted key tagged at creation as "Authorizing agent access to your account", which comes with approval rules for refunds, payouts and account changes). After connecting, start a new session and prove it with one read call. On Givi, Codex's Stripe plugin returned `USER_NOT_LOGGED_IN` because the connector had been installed but never authorised. **(learned the hard way)**

**Standing permission.** Have the founder write one dated line in the agent's rules file: "Agents may create, move and archive Stripe sandbox keys and objects for this venture without asking." Live keys and live changes stay with the founder.

**A read-only live key for audits.** On Givi, audits ran with the full live key, and one script printed the live webhook secret into the agent's output because it dumped whole objects. Use a read-only restricted key and print named fields only. **(learned the hard way)**

---

## 6. Products and prices managed by code

Write one idempotent `ensure()` that runs on every app start, and from an admin button, with whichever key is present. Givi's version ran in live mode only, so the sandbox was set up by hand: typing produced "9,999.00" instead of 99 and doubled product names, the webhook secret needed a human "reveal" click, and the missing tax code surfaced only in QA. **(learned the hard way)**

```python
import stripe  # pin the API version in one place

PLANS = {"app_monthly": {"amount": 4900, "currency": "usd", "interval": "month"}}
PRODUCT = {"name": "YourBrand", "description": "Your assistant for ...",
           "tax_code": "txcd_10103001"}
EVENTS = ["checkout.session.completed", "customer.subscription.created",
          "customer.subscription.updated", "customer.subscription.deleted",
          "customer.subscription.trial_will_end", "invoice.paid",
          "invoice.payment_failed", "charge.refunded", "charge.dispute.created"]

def ensure(base_url, settings):
    acct = stripe.Account.retrieve()
    report = {"can_charge": acct.charges_enabled, "can_pay_out": acct.payouts_enabled}
    product = find_product(app_key="main") or stripe.Product.create(
        **PRODUCT, metadata={"app_key": "main"})
    for key, p in PLANS.items():
        hit = stripe.Price.list(lookup_keys=[key], active=True).data
        same = hit and (hit[0].unit_amount, hit[0].currency,
                        hit[0].recurring.interval) == (p["amount"], p["currency"], p["interval"])
        if not same:
            stripe.Price.create(product=product.id, unit_amount=p["amount"],
                                currency=p["currency"], recurring={"interval": p["interval"]},
                                lookup_key=key, transfer_lookup_key=True)
    if not settings.get("webhook_secret"):
        ep = stripe.WebhookEndpoint.create(url=f"{base_url}/stripe/webhook",
                                           enabled_events=EVENTS)
        settings.save("webhook_secret", ep.secret)  # returned once; never log it
    ensure_portal(cancel="at_period_end", card_update=True, plan_switch=False)
    return report  # one line per step on the admin page
```

- **Reuse a price only if amount, currency and interval match**; otherwise create it and move the lookup key. Archive the old price.
- **Create the webhook endpoint through the API.** The response carries the signing secret once, so nobody clicks "reveal" and nobody pastes it.
- **Give the product a human description.** Without one, Givi's Checkout showed an internal price code. **(learned the hard way)**
- **Derive the key's permissions from the code.** Grep every Stripe call the app makes and give the restricted key exactly those. On Givi a key built for "read prices" met new code that created prices, and checkout failed for about a day in sandbox until a tester complained. Givi's documented permission list also missed refunds, invoices and payment methods. **(learned the hard way)**
- **If the runtime key cannot create prices,** send unknown prices inline with `line_items[0][price_data]`, and always log Stripe's error body instead of "Payments aren't available".

---

## 7. Checkout as the sign-up, and trials

### Checkout as the sign-up

The visitor sees value first (a demo or a result), types one email, goes to Checkout with that email locked, pays or starts a trial, and the account is created from the Checkout session. **(done on Givi from 12 Oct 2026; the full real-card path was never completed)**

Why: ad clicks open inside the Instagram, Facebook and TikTok in-app browsers, and Google refuses OAuth sign-in in embedded browsers (error `disallowed_useragent`). On Givi, all but one of about 45 people who clicked Start left at the sign-in screen. **(learned the hard way)**

```python
session = stripe.checkout.Session.create(
    mode="subscription",
    line_items=[{"price": price_for("app_monthly"), "quantity": 1}],
    customer_email=email,                         # locked on the page
    client_reference_id=signup_token,
    subscription_data={"trial_period_days": TRIAL_DAYS,   # per session, never on the Price
        "trial_settings": {"end_behavior": {"missing_payment_method": "cancel"}}},
    payment_method_collection="always" if CARD_TRIAL else "if_required",
    consent_collection={"terms_of_service": "required"},
    allow_promotion_codes=True,
    metadata={"offer": OFFER_ID, "utm_source": utm_source, "utm_content": utm_content},
    success_url=f"{BASE}/welcome?session_id={{CHECKOUT_SESSION_ID}}",
    cancel_url=f"{BASE}/?checkout=cancelled")
```

- **On return,** read the session on the server, create the account, and sign in **only the browser that started the sign-up** (match a cookie set before the redirect). The webhook also creates the account, idempotently, in case the tab is closed. Email a sign-in link so the address is confirmed and they can get back in from another browser.
- **Terms consent** (`consent_collection`) needs your terms URL in the public details first.
- **The return URL grants nothing on its own.** Only a verified webhook or a server-side read of the session changes access.
- **One open session per email;** return hosts from an allow-list; Checkout creation rate-limited per IP and per email, with an alert on a spike in declines. **(recommended, not tested by us)**
- **Keep work done before sign-up.** A visitor who starts in the in-app browser and finishes in Chrome must not lose what they made. Givi's leads landed on an empty box. **(learned the hard way)**

### The three trial modes

| Mode | Checkout settings | Watch out for |
|---|---|---|
| No trial | No `trial_period_days` | Fewer starts, highest intent |
| No-card trial | `trial_period_days`, `payment_method_collection="if_required"`, `missing_payment_method="cancel"` or `"pause"` | Most never convert; turn on Stripe's reminder email to collect a card before the end |
| Card trial | `trial_period_days`, card always collected | Card testing, consumer-law duties, cost before the first real charge |

Card-trial protections (built on Givi after an adversarial review found ten holes in the plan in about seven minutes): **(done on Givi)**

- Create nothing expensive per customer (servers, AI keys) before the card is on file.
- Gate every entry route. Givi's plan first forgot Telegram, Slack, email, phone and assistant connectors, any of which gave the product to someone with no card.
- Treat `trialing` as unpaid: a small usage cap until the first real, unrefunded charge, and check every path that could reset the cap (monthly refresh, plan switch, failed first charge).
- Mark repeat trials by email and by card fingerprint, and keep the marks after account deletion.
- Send your own reminder 24 hours before the first charge. `customer.subscription.trial_will_end` fires 3 days before the end, or at once if the trial is shorter, so on a 3-day trial it arrives at the start.
- Offer "Start my plan now" (`trial_end="now"` on the subscription).
- One switch with off, team and all, plus a kill switch. Switching a money feature on for everyone is the founder's call, in their own words.

**Legal check before a card trial.** Selling to UK consumers brings the Consumer Contracts Regulations (cancellation rights for digital services, consent to start at once), card-network rules on disclosing free trials, and the DMCC Act 2024 subscription regime, which law firms in March 2026 did not expect in force before autumn 2026 at the earliest; check GOV.UK on the day. US states have automatic-renewal laws. Write a one-page check mapping each rule to a line in your terms and a screen in your flow (see `14-company-legal.md`). **(recommended, not tested by us)**

---

## 8. The customer portal

Configure it in `ensure()` or at Settings > Billing > Customer portal: card update on; cancel at period end on; invoice history on; plan switching off until there is more than one plan; terms, privacy and support details filled. The app's "Manage subscription" button creates a portal session and redirects. **(done on Givi)**

A portal cancellation can set `cancel_at` to the period end while `cancel_at_period_end` stays false. Treat both as "cancels on date X" and show "Active until <date>". Givi showed "Next renewal" on a cancelled plan until this was fixed. **(learned the hard way)**

---

## 9. Webhooks

The endpoint is `https://<your-app>/stripe/webhook`, one per environment, created by `ensure()`.

| Event | What the app does |
|---|---|
| `checkout.session.completed` | Create or link the account; store customer and subscription IDs |
| `customer.subscription.created` / `.updated` | Re-read the subscription; update status, period end, cancel date |
| `customer.subscription.deleted` | End paid access, only if the subscription ID matches the one on file |
| `customer.subscription.trial_will_end` | Optional reminder logic |
| `invoice.paid` | Paid through the invoice's period; raise the usage cap after the first real charge |
| `invoice.payment_failed` | "Fix your card" banner; access only during Stripe's retries |
| `charge.refunded` | Record the refund; proves the real-card test |
| `charge.dispute.created` | Alert the founder at once; pause the paid allowance |

Givi's live webhook did not subscribe to dispute events, so a chargeback would have changed nothing and alerted nobody. **(learned the hard way)**

Handler rules:

- Verify the signature; reject unsigned posts.
- Re-read the object from Stripe instead of trusting the event snapshot; events arrive out of order.
- Store processed event IDs so every handler is idempotent.
- Match the subscription ID before changing an account, so a late `deleted` for an old subscription cannot downgrade someone who resubscribed. **(learned the hard way)**
- Return 2xx for objects you do not own, and a retryable status such as 409 (never 500) when two events for one subscription contend.
- Pin the API version and read moved fields from both places. On Givi a version change moved where an invoice points to its subscription, and invoice events were skipped silently. **(learned the hard way)**
- Run billing tests on the production database engine. A query that passed on SQLite returned 500 on Postgres for every refund. **(learned the hard way)**
- Alert when the endpoint starts failing (Developers > Webhooks > the endpoint shows failed deliveries). **(recommended, not tested by us)**

---

## 10. Entitlements, refunds, proration, top-ups, coupons and free access

**One entitlement table.** One row per account: `source` (`stripe`, `trial` or `comp`), status, period end, cancel date, usage cap. "Paid" means a first charge above zero not refunded inside the window; free access, test payments and refunds never count. Givi's first code counted `trialing` as paid. **(learned the hard way)** `past_due` keeps access during Stripe's retries only, which is why dunning (section 3) must cancel at the end.

**Refunds.** Before a button exists: Dashboard > Payments > the payment > Refund, then cancel the subscription, because a refund alone does not cancel it. The Tier 1 button calls `POST /v1/refunds` for the first payment, then `DELETE /v1/subscriptions/{id}`, each with an idempotency key and a state row so a double tap is safe, once per person, inside the window. **(done on Givi in code; never exercised with a real card)** Account deletion cancels the subscription first and stops if Stripe does not answer. **(done on Givi)**

**Proration (Tier 1).** Plan switches go through `stripe.Subscription.modify` with an explicit `proration_behavior` (`create_prorations`, `always_invoice` or `none`). Preview the next invoice with `stripe.Invoice.create_preview` before showing a number. **(recommended, not tested by us)**

**Top-ups and credits (Tier 1).**
- Price them above cost plus every Stripe fee. Givi's first $20 top-up bought exactly $20 of AI and lost money on each sale; it became $20 for $15 of usage. Work the margin out from a real balance transaction (`GET /v1/balance_transactions/<id>`, `fee_details`), not the headline card rate. **(learned the hard way)**
- Keep them in their own ledger valid for 12 months, with the plan's allowance used first. Givi's first version expired them at month end. **(learned the hard way)**
- Off-session auto top-ups can come back `requires_action` when a UK or EU bank asks for Strong Customer Authentication; fall back to a normal payment link.
- Show usage as jobs or tasks, never dollars of AI.

**Coupons and free access.**
- Discounts: a coupon, then a customer-facing promotion code, with `allow_promotion_codes=True` on Checkout. **(recommended, not tested by us)**
- Free access: grant a `comp` row from an admin panel (1, 3 or 12 months or no end, with a note and an End button), never a fake 100% coupon. Keep the founder's own account on comp across the live switch. Testers start on comp and are asked for a card at the end of their pilot week. **(done on Givi)**
- Free-access links: a signed, single-use, expiring invite that creates a `comp` row at sign-up. **(recommended, not tested by us)**

---

## 11. Stripe Tax at a high level

Orientation, not tax advice; confirm with an accountant and see `14-company-legal.md`.

- **What it does:** from a product tax code and the customer's location it calculates VAT or sales tax, collects it in Checkout (`automatic_tax={"enabled": True}`), tracks your sales against registration thresholds and reports what you collected. You still register with each authority and file returns; Stripe offers filing through partners in some places.
- **Price:** 0.5% per transaction where you are registered, on Checkout, Billing, Invoicing and Payment Links (pay-as-you-go, checked 13 Oct 2026).
- **A UK seller, roughly:** UK VAT registration becomes compulsory once taxable turnover passes £90,000 in 12 months. Selling digital services to EU consumers from outside the EU has no threshold: EU VAT is due from the first sale, usually through one non-Union One-Stop Shop registration. US states set their own thresholds, which Stripe Tax's monitoring flags. Business buyers with a VAT number are generally reverse-charged.
- **The choice:** selling to consumers internationally without registering anywhere points to Managed Payments (section 2). Selling only to businesses usually makes plain Stripe plus Stripe Tax cheaper.

Get VAT advice and write down your tax and seller-of-record position, including whether you sell to individuals, before ads run, so anyone can say what your live tax status is. **(recommended, not tested by us)**

---

## 12. Test before any real money

- **A fake Stripe in the test suite** that behaves like the real key, including refusing calls the restricted key cannot make. **(done on Givi)**
- **Sandbox cards:** `4242 4242 4242 4242`, any future expiry, any CVC. Declines, 3D Secure and disputes have their own numbers in Stripe's testing docs.
- **The agent pays, not the founder.** Checkout ignores synthetic clicks from headless browsers, so use the API: a customer, the test payment method `pm_card_visa`, a subscription and a test clock to move time. On Givi, Codex's built-in browser also completed a sandbox Checkout through the page's WebMCP tool (`submit_payment`, after ticking the AI-agent disclosure box). **(done on Givi, sandbox only)** No agent ever types a real card.
- **Local webhooks and events:**

```bash
stripe listen --forward-to localhost:8000/stripe/webhook     # prints a local signing secret
stripe trigger checkout.session.completed
stripe trigger invoice.payment_failed
stripe events resend evt_123 --webhook-endpoint we_123        # replay to prove idempotency
stripe test_helpers test_clocks create --frozen-time "$(date +%s)"
```

`stripe trigger` also runs in the dashboard's Workbench shell with nothing installed, and Workbench > Logs shows every request with its error body. Those two found Givi's missing tax code and the 403 on price creation in minutes. **(done on Givi)**

- **Run the lifecycle on a test clock:** trial end, first charge, renewal, failed renewal, refund, resubscribe.
- **Never re-run a failed money action.** Reconcile what exists, then fix.
- **Merge money fixes inside a deploy window,** not late at night. On Givi a late fix never deployed cleanly and the refund and dispute cases were never run. **(learned the hard way)**
- **Review:** an adversarial review of the plan before building ("where does this break live, and what silently does less?"), and one second-model review of every billing change. **(done on Givi)**

---

## 13. The live switch

The founder's part takes about 10 minutes in sitting S3b, booked once activation is complete. Send the ask alone at the top of its own message. Givi's ask sat inside a long status update, two agent sessions sent competing instructions, and the hand-off took about 3 hours. **(learned the hard way)**

1. **Before the sitting:** the tax and seller-of-record line is written down; dunning, Radar and dispute settings are on; the real-card test (section 14) is booked straight after.
2. **The agent opens** dashboard.stripe.com/apikeys in live view and fills "Create restricted key" with the permission list derived from the code. The founder clicks Create and copies the key. A restricted live key you create is shown once only.
3. **The founder double-clicks a validating script** the agent wrote and dry-ran with a dummy value. A `!` line runs only where the agent sits in a terminal; Givi's founder used the VS Code panel, where `!` lines arrive as chat text. Check `echo $CLAUDE_CODE_ENTRYPOINT` first. **(learned the hard way)**

```bash
#!/bin/bash
# set-stripe-live-key.command : copy the restricted live key, then double-click this file
set -euo pipefail
KEY="$(pbpaste)"
fail() { echo "Refused: $1"; exit 1; }
[[ "$KEY" == rk_live_* ]] || fail "clipboard does not start with rk_live_"
[[ "$KEY" =~ [[:space:]] ]] && fail "whitespace in the clipboard"
[ "$(grep -o 'rk_live_' <<<"$KEY" | wc -l | tr -d ' ')" = "1" ] || fail "more than one key"
CODE=$(curl -s -o /dev/null -w '%{http_code}' -K - https://api.stripe.com/v1/prices?limit=1 <<EOF
user = "$KEY:"
EOF
)
[ "$CODE" = "200" ] || fail "Stripe rejected the key (HTTP $CODE)"
railway status | grep -q "your-project-name" || fail "linked to the wrong project"
printf %s "$KEY" | railway variable set STRIPE_SECRET_KEY --stdin --skip-deploys --service app
pbcopy </dev/null
echo "accepted"
rm -- "$0"
```

   The key reaches Stripe through curl's config on stdin, so it never shows in the process list. On Givi the first unvalidated attempt stored two keys glued together, because the clipboard still held the old test key. **(learned the hard way)**
4. **The agent checks the stored value by prefix and length only,** never printing it, and stops other sessions deploying if the shape is wrong.
5. **Restart through the normal deploy path** in a quiet window. On Railway, a variable change with `--skip-deploys`, or a variable delete, restarts nothing. **(learned the hard way)**
6. **Verify from inside the running app,** named fields only: can charge and pay out; live prices with the right amounts; webhook enabled with `charge.refunded` and `charge.dispute.created`; portal allows cancel; old sandbox variables gone.
7. **Live preflight for every offer:** create a real Checkout session with the exact offer, open its URL to check the price, trial line and locked email, then expire it (`POST /v1/checkout/sessions/{id}/expire`). No charge. Repeat after every price or trial change. **(done on Givi)**

---

## 14. The real card and refund test, before any ad spend

Never done on Givi, and the most important five minutes in this file. It belongs to sitting S3b, straight after the live switch, and it is part of the funnel gate (G5 in `01-framework.md`). **(recommended, not tested by us)**

The founder, in a private browser window:

1. signs up as a new visitor from the public landing page;
2. pays through Checkout with a real card (Apple Pay or Link on a phone is fastest; on a card trial, $0 today);
3. presses "Start my plan now", or ends the trial from the dashboard, so a real charge happens;
4. presses "Refund and cancel", or refunds and cancels from the dashboard.

The agent then checks: `charge.refunded` delivered; refund and subscription rows in the database; the account created on return; the usage cap raised after the charge and lowered after the refund; receipt and refund emails received.

**Make it a hard gate.** No ad money moves until the agent has seen `charge.refunded` and the database rows. Give it its own message as a 5-minute item. On Givi it was offered as optional several times, then put off, and ads ran five days without it. Then the sign-up path changed shape and went live to all ad traffic with no completed payment on that path. **(learned the hard way)** Repeat the test whenever the sign-up or payment path changes. A founder purchase that is refunded tests the path; never count it as revenue.

---

## 15. After going live

- **Daily checkout probe** per live offer (create and expire) in the morning digest, and a **daily reconciliation** of Stripe against the database: subscriptions with no matching entitlement, entitlements marked paid with no live subscription. **(recommended, not tested by us)**
- **Alerts** on a failing webhook endpoint, any `charge.dispute.created` and a spike in declines.
- **Archive superseded prices** (the product > Pricing > the price > Archive).
- **A leaked live key or webhook secret** (in a chat, log or tool output) is rotated within 24 hours: API keys > the key > Rotate (old and new can overlap for up to 7 days). Record it by name only.
- **Changing a price** is a protocol. With zero payers it is a guess replacing a guess, so freeze the offer until about 10 buyers have reached checkout. When it changes: pause paid ads first; update the offer file; create the new price by lookup key through `ensure()`; ship one change touching every surface (landing, terms, app, ad text); `curl` each page for old and new strings; run the live preflight; create new ads and delete the old ones (Givi's agents could not edit published Meta ad text); archive the old price. Full protocol in `03-positioning-pricing.md`, step 9. Existing subscribers keep their price until a stated date with at least 30 days' notice.

---

## Tools

| Task | Use | Avoid |
|---|---|---|
| Create products, prices, webhook, portal | The app's `ensure()`, both modes | Clicking through the dashboard |
| Sandbox access for agents | Stripe CLI after `stripe login` | Waiting for the founder to copy a key |
| Audits and docs | Stripe MCP (`stripe_api_read`, `search_stripe_documentation`) with OAuth or an agent key | Scripts holding the full live key |
| Current parameters | Context7 (`/websites/stripe`) or docs.stripe.com before each design step | Memory |
| Events | `stripe listen`, `stripe trigger`, `stripe events resend`, Workbench shell and Logs | Forged payloads |
| Agent test payment | API with `pm_card_visa` and a test clock | Synthetic clicks on Checkout |
| Live key on the host | Validating script the founder double-clicks | Pasting in chat |
| Waiting on a deploy or a stored key | A background until-loop (Claude Code's Monitor tool) | Hand-written `sleep` loops |

## What needs the founder

| Step | When | Minutes |
|---|---|---|
| Money decisions in one message, each option with a recommendation | the offer batch, day 1-2 (`03-positioning-pricing.md`, step 7) | 15 |
| Tax position and the founder's own yes/no, with an accountant | by S2 | 10 plus the accountant |
| Account, 2FA, `stripe login`, authorise the Stripe MCP | S1a | 10 |
| KYC and bank details | S2, with the payout account the day the bank account exists | 10 |
| Live restricted key: one click on a pre-filled form, one double-click on the script | S3b | 5 |
| Real card and refund | S3b | 5 |

## Checklist

- [ ] Tier 0 scope written down; Tier 1 parked until the first payer
- [ ] Seller of record chosen from Stripe's docs and current fees, confirmed with an accountant, written down with the tax position
- [ ] Currency, price as one shared variable, trial mode, refund window and "who we sell to" recorded with dates; founder's own yes/no recorded
- [ ] Account under a company email with 2FA; KYC done; `charges_enabled` and `payouts_enabled` true
- [ ] Public details and statement descriptor set; website shows contact details, terms, refund and cancellation policy
- [ ] Dunning cancels after the last retry; Radar rules, customer emails, branding, payout currency and dispute contact set
- [ ] Development on a general sandbox; `stripe login` done; Stripe MCP authorised and proven with one read in a fresh session
- [ ] Standing permission for sandbox keys and objects; read-only live key for audits
- [ ] `ensure()` runs in sandbox and live: described product with tax code, prices by lookup key, webhook by API with its secret stored server-side, portal configured
- [ ] Restricted key permissions derived from every Stripe call in the code
- [ ] Checkout as the sign-up: locked email, trial per session, missing-payment-method behaviour, attribution metadata, one open session per email, allow-listed hosts, rate limit
- [ ] Sign-up and Checkout walked in the Instagram, Facebook and TikTok in-app browsers on a real phone (S3b, part of the funnel gate)
- [ ] Card trial (if chosen): nothing costly before the card, every entry route gated, repeat-trial marks, own 24-hour reminder, kill switch, written consumer-law check
- [ ] Webhook verified, re-reads objects, idempotent, matches subscription IDs, handles both cancel shapes, alerts on disputes and endpoint failures
- [ ] Entitlement table with `stripe`, `trial` and `comp`; founder comped; admin free-access panel
- [ ] Tests on the production database engine, fake Stripe with the key's permissions, test-clock lifecycle, event replays
- [ ] Permanent staging service on sandbox keys cloned before the live switch
- [ ] Live restricted key stored through the validating script; restart through the deploy path; checks from inside the app
- [ ] Live preflight (create, read, expire) for every offer
- [ ] Founder's real card payment and refund done in S3b; agent saw `charge.refunded` and the database rows; ads stay off until then
- [ ] Daily checkout probe and reconciliation running; old prices archived
