# Company and legal basics for a small online venture

**Practical orientation, not legal or tax advice.** What a founder of a small software business sets up on the company side, in what order, and which questions go to an accountant or lawyer: the seller, a UK limited company, checks for a founder living outside the UK, the bank account Stripe payouts depend on, VAT and sales tax for UK, EU and US buyers, four policy pages rendered from one facts file, card-first trials, data protection when an AI agent touches customer data, and trade mark screening. Rules were checked against official sources on 13 Oct 2026; they change, and your own facts (where you live, who you sell to, your visa) change the answer.

**Done when:** the seller exists on its public register; one facts file holds its identity and every console form and policy page copies from it; the bank account exists; an accountant has answered the VAT question in writing; the privacy, terms, refund and cookie pages are live and match what the code really does; a written check of the subscription rules exists before any card-first trial ships; and the public brand has been searched in the trade mark registers of every market you will advertise in.

Evidence tags: **(done on Givi)**, **(learned the hard way)**, **(recommended, not tested by us)**.

## 1. Decide who the seller is, on day 0

Three options, in order of speed:

| Option | Time to a seller that can be verified | When it fits |
|---|---|---|
| A new brand under a company you already own and have verified | Today | A pilot; the cheapest path, because Meta Business Verification and Stripe KYC are already done |
| A new UK private limited company | Usually within about 24 hours of filing online | You live and run the business in the UK, or the venture will be sold, funded or carry a different risk |
| An entity elsewhere | Days to weeks | Your tax home is elsewhere; get local advice |

Reusing a company is fine; reusing its money is not. Give the new venture its own card, ad accounts and billing even under the same company (`02-day0-accounts.md`). One risk of sharing: a policy strike on a shared Meta business portfolio can stop both ventures' ads, so decide the portfolio on its own, with that risk written next to the question.

> **What happened on Givi.** An agent researched entity options from primary sources in about 30 minutes on day 0 and recommended a UK limited company. The company existed 6 days later. Every company-gated step (Meta verification, Stripe under the company, the seller details on the policy pages, other verifications) waited behind it. The research took half an hour; the six days before filing were the cost. **(learned the hard way)**

## 2. Forming a UK limited company online

**What it takes** (Companies House online registration, £100 since 1 Feb 2026, usually registered within 24 hours):
- a company name (screen it first, section 9); keep the company name neutral (for example "<Something> Labs Ltd") and separate from the product brand, so the brand can change without touching the company;
- a registered office address in the same UK nation as the registration (England and Wales, Scotland, or Northern Ireland). It is public. It cannot be a PO box. A registered-office service from an accountant or formation agent keeps your home address off the public register and off every policy page;
- at least one director and the people with significant control (anyone holding more than 25% of shares or votes);
- shareholders and share capital (one founder with a small number of £1 shares is common), and model articles;
- a SIC code describing the activity (for SaaS, 58290 "other software publishing" or 62012 "business and domestic software development" are common choices);
- a registered email address for Companies House;
- identity verification for every director and person with significant control, a legal requirement since 18 Nov 2025. New directors must verify before the company is incorporated. It is free through GOV.UK One Login (by app, security questions or at a Post Office), which gives each person a Companies House personal code; the alternative is an Authorised Corporate Service Provider (an accountant or formation agent registered with Companies House), which may charge.

**Steps:** the agent prepares every answer on one page before sitting S1a; in S1a the founder verifies identity through GOV.UK One Login and files at gov.uk/limited-company-formation (about 10-15 minutes of the founder's time). Then the agent reads the public record and writes the facts file:
- `https://find-and-update.company-information.service.gov.uk/company/<number>` (or the free Companies House API: `GET https://api.company-information.service.gov.uk/company/{number}`, `/officers`, `/persons-with-significant-control`);
- if you scrape the search page instead of using the API, strip `<script>` and `<style>` first: the page carries a hidden "No results found" template even when results exist, which gives false "available" answers. **(learned the hard way)**

**The facts file** (`legal/identity.md`): legal name exactly as registered, company number, jurisdiction, registered office, trading name, incorporation date, SIC code, support email (a monitored mailbox owned by the venture, with a named person; forwarding into a free brand Google account is fine for a short test, but once someone answers customers or privacy requests from it, move it to Google Workspace, see `02-day0-accounts.md`), business phone, website, VAT status and number, D-U-N-S number, base currency, accountant (name only), bank (name only). No documents, ID scans or account numbers in the repo. Every console form, policy page and verification copies from this file, and every agent reads it before claiming anything about the company.

> **What happened on Givi.** An agent verified the company on the register the day it was formed, but wrote the facts into an unrelated deployment note. Two later agents re-verified it, and 18 days after incorporation another agent told the founder the venture "has no registered company yet" while preparing an advertiser verification. The registered office used was a home address, printed on every policy page, the Meta portfolio and Stripe. **(learned the hard way)**

**Fixed dates to put in a calendar the day the company exists**:
- register for Corporation Tax with HMRC within 3 months of starting to do business;
- a confirmation statement at least once every 12 months;
- first annual accounts due 21 months after incorporation, then 9 months after each year end;
- VAT registration once taxable turnover passes the threshold (section 5);
- the ICO data protection fee, yearly (section 8).

Ask an accountant to confirm them and to set up bookkeeping connected to the bank feed. Corporation Tax was 19% on profits up to £50,000 and 25% above £250,000, with marginal relief in between, when we checked. The confirmation statement costs £50 online.

## 3. What a non-UK founder should check

Forming a UK company does not by itself make you UK-resident, and living elsewhere does not stop you forming one. Before filing, write these questions down and send them to an adviser (the agent can draft them straight into your email drafts so you only press Send):

- **Visa or immigration status.** If you hold a visa in the country where you live, check whether owning, directing or being paid by a company is allowed under it. Agents should flag this once and never conclude it.
- **Where the company is managed.** A company run day to day from another country can become tax-resident or create a taxable presence there, wherever it is registered.
- **Personal tax** on salary, dividends or a director's loan, in your country of residence.
- **Identity verification from abroad.** Directors do not need to be UK-resident, but must still verify. The One Login app accepts a biometric passport from any country (not expired); if you hold no document it accepts, an Authorised Corporate Service Provider can verify you from any country, usually for a fee.
- **A bank that will open an account** for a UK company with a non-resident director (some UK app banks require UK residence; check before filing).
- **Stripe availability.** Check Stripe's list of supported countries for the country where your company is registered. If Stripe is not available there, look at the local bank's online card acquiring or a merchant of record that accepts sellers from your country.

Other structures we read about and did not use **(recommended, not tested by us)**: a US single-member LLC owned by a foreigner is not a tax exemption and brings yearly federal reporting (Form 5472 with a pro forma 1120, with a $25,000 base penalty for not filing); Estonia's e-Residency route takes weeks and an in-person card pickup. For a ten-customer test, neither beats a company in the country you live in.

## 4. Business bank account: the dependency nobody times

A UK limited company is a separate legal person: its money must be kept apart from yours. GOV.UK says "there must be a clear division between the company's finances and those of the owners and directors" and that a business bank account is "the simplest way" to keep them apart. In practice the bank account is a hard dependency:

- **Stripe** needs a payout account in the company's name before it activates, so live payments wait for the bank.
- **Ad platforms** bill a company card or direct debit; failed card holds silently stopped Givi's Meta ads twice, the second time with prepaid funds on the account. **(learned the hard way)**
- **Prepaid balances** (TikTok, model credit) need a card in the company's name.

Apply the day the company number arrives, as the first item of sitting S2; plan for days, not hours. Until it exists, put venture costs on a virtual card used only for this venture. If a personal card paid a company cost, keep the invoice and record it as paid on the company's behalf, reimbursed or booked to the director's loan account (general UK practice; your accountant confirms). Pick one currency for the business (the currency you charge in) and create every ad account in it, since Meta and Google ad-account currencies cannot be changed later; Givi ended up with ad spend in pounds and dollars and prices in dollars. **(learned the hard way)**

## 5. VAT and sales tax when selling software

Software sold online is an "electronically supplied service" in the UK and EU, and taxable in many US states. Who owes tax depends on where the buyer is and whether the buyer is a business or a consumer.

| Buyer | What usually applies to a UK seller (orientation only) |
|---|---|
| UK business or consumer | UK VAT at 20% once you are VAT-registered. Registration is required when taxable turnover over any rolling 12 months passes £90,000 (the threshold since 1 Apr 2024, unchanged when we checked); you may register voluntarily earlier, which lets you reclaim VAT on costs and add your VAT number to ad accounts |
| EU business | Usually no UK VAT; the customer accounts for VAT under the reverse charge. Collect and check their VAT number |
| EU consumer | EU VAT at the customer's country's rate from the first sale: the €10,000 EU threshold applies only to sellers established in the EU, not to a UK company. Register once through the EU's non-Union One Stop Shop (OSS) in a single member state and file one quarterly return for all EU countries, or use a merchant of record |
| US business or consumer | No federal sales tax. Each state sets its own rules: many tax SaaS, many do not, and a state can require you to register once your sales into it pass its "economic nexus" threshold. Most states use $100,000 of sales or 200 transactions in 12 months as the threshold (California and Texas use $500,000), following the 2018 Wayfair decision. Taxability differs too: when we checked, Connecticut taxed SaaS, California did not, and Texas taxed 80% of the price. |
| Other countries | Many tax foreign digital services sold to consumers, with their own thresholds. Check each market before you advertise there |

**Three ways to handle it:**

1. **You are the seller, and Stripe Tax calculates.** Stripe Tax works out the right tax at checkout, shows you where you are approaching a threshold, and produces reports; you still register in each place and file the returns (or use a filing partner). When we checked, the pay-as-you-go plan cost 0.5% per transaction (no-code) and covered calculation and collection only; a subscription plan from £70 a month added registration and filing.
2. **A merchant of record sells for you.** The merchant of record is the legal seller to your customer and handles VAT and sales tax registration, collection and filing everywhere, for a higher fee. Options: Stripe Managed Payments (Stripe's own merchant of record, generally available since 22 Apr 2026 and open to UK businesses; 3.5% per successful transaction on top of standard Stripe fees, for fully automated digital products only, not services involving people; buyers see "Sold through Onelink" at checkout and `LINK.COM*` on their card statements), Paddle and Lemon Squeezy (each listed 5% plus 50 cents per transaction when we checked). Your policy pages then need to say who the seller is, and it must match what checkout shows.
3. **UK only, consumers excluded.** If you sell only to UK businesses at first and stay under the UK threshold, there is little to collect. Narrow, but simple for a first test.

**Ad platforms:** Meta asked Givi's ad account for a VAT number and, without one, added 20% UK VAT to every ad charge, so plan ad budgets with VAT included. **(done on Givi)**

Decide VAT and the merchant-of-record question together, with an accountant, before the first ad account exists, and write the answer down. If the founder says they do not understand an option, it is not a decision yet: explain it again with the fee in money at your real price.

> **What happened on Givi.** The Stripe account turned out to be using Stripe's merchant-of-record option (checkout read "Sold through" a Stripe entity), while the policy pages named the company as the seller. The founder said he still did not understand the option, but "keep it" was recorded as a decision; nobody priced the extra fee, and VAT was never settled with an accountant before ads ran. **(learned the hard way)**

## 6. The four policy pages, rendered from one facts file

Each page must state only what the product really does, so write it from the code (grep the deletion, retention and cookie paths first), not from the plan.

| Page | What it must cover |
|---|---|
| **Privacy** | Who you are (legal name, number, registered office, contact); what data you collect and why, with the lawful basis for each use; every processor (hosting, database and auth, AI model providers, email sender, payments, analytics, connected-app platform) with its purpose and region; international transfers and the safeguard used; how long each kind of data is kept, including backups; how to delete an account, get a copy or correct data, and who answers within what time; the right to complain to the ICO; cookies (or a link to the cookie notice); anything special to your product (what the AI agent can see and do, whether staff can read conversations, what happens to keys a customer pastes, assistant connections) |
| **Terms** | Who the seller is and who may buy (businesses only, or individuals too, which brings consumer rights); what is sold, the price, trial, renewal and how to cancel; acceptable use (no spam or unlawful marketing through the product, respect each platform's rules, right to suspend); limits of liability that respect consumers' statutory rights; governing law and courts. For business customers, link a data processing agreement (section 8) |
| **Refunds** | The window, what is refunded, how to ask (a button or an email), how long it takes. Givi: the first payment refunded in full within 14 days, no reason needed, later monthly payments not refunded on cancellation; later a self-serve "Refund and cancel" button **(done on Givi; never exercised, because nobody had paid by 12 Oct 2026)** |
| **Cookies** | Every cookie and pixel, its purpose and lifetime; which ones wait for consent; how to change your choice |

**Render all four from files, never by hand:**
- `legal/identity.md` (the seller), `legal/vendors.md` (one row per processor: what it does, what data it receives, region, link to its data processing terms), and the plan values in code (price, trial length, refund window, cookie list). A pricing or trial change then updates the pages in the same pull request. Givi hand-edited its pages about eight times in two weeks and still shipped stale text: a cookie count that was wrong, "private pilot" wording that blocked a directory listing, and terms promising automation that had not been built. **(learned the hard way)**
- Gate publication. Until the seller fields and an "accepted" flag are set, every policy page returns 503 "Draft, not approved for publication" with `noindex`, and checkout stays off. Set the flag only when the vendor list has regions, retention is written and the refund rules are final, then get the founder's "I accept the policy texts" in their own message. **(done on Givi; we opened the gate with the vendor list and retention still empty, which later stalled two platform forms, learned the hard way)**
- Put a "Policy version: <date>" line at the top and keep old versions in git.
- Test: the draft state, the accepted state, and escaping of the seller fields.
- Use the same four URLs everywhere: site footer, Stripe's public details, Google's OAuth branding, Meta's app settings, directory listings. Paste the privacy URL into Meta's app settings early; Meta's validator rejected Givi's main privacy page without saying why, and a plain page on a separate path passed. **(learned the hard way)**
- Never call the product a "pilot", "beta" or "demo" in the terms if you plan to list it in app directories; OpenAI does not accept trial or demo apps.

**Cookie consent.** Under UK rules (PECR), storing cookies or similar on a visitor's device needs consent unless it is strictly necessary. Since 5 Feb 2026 (Data (Use and Access) Act 2025) there are new exceptions, including cookies used only to produce statistics about how your own service is used, so you can improve it, provided people are told clearly and can object; anything used for advertising still needs consent. PECR fines now go up to the UK GDPR level (£17.5m or 4% of turnover). Load every advertising pixel (Meta, Google, TikTok) only after the visitor presses "Allow". Make "No thanks" and "Allow" equally visible. On phones, do not cover the main button. Givi's first small grey banner got about 5% opt-in; an equal-weight banner took 15 minutes to build. **(learned the hard way)** Check in a clean browser that nothing loads from an ad network before consent.

**Account deletion.** Ship a self-serve "Delete account" with the first sign-up: one menu item, a typed confirmation, then cancel the subscription, revoke connected apps, delete per-customer infrastructure and keys, delete the rows, delete the auth record, end the session, and abort everything if any outside call fails. Keep only a one-way hash of the email if you need to stop repeat free trials, and say so in the privacy page. **(done on Givi, except the auth record, which stayed until a missing key was added)**

## 7. Free trials that take a card: subscription and auto-renewal rules

A trial that takes a card and then charges automatically is the most regulated thing a small SaaS does. Get a written answer before shipping one, and keep a no-card trial ready as the fallback.

**UK (orientation):**
- Consumers who buy online usually have 14 days to cancel (Consumer Contracts Regulations 2013). For a **service** started early at the consumer's express request, they can still cancel and pay a proportionate amount for what they used. For **digital content**, they lose the right only if they expressly agreed to immediate supply and acknowledged losing it. Whether your SaaS counts as a service or digital content depends on the facts, so ask; either way, collect the request and acknowledgement at checkout. Business buyers do not get this right.
- A dedicated subscription regime under the Digital Markets, Competition and Consumers Act 2024 is not yet in force. When it is, it requires key information before the contract, a reminder before the first payment after a free or discounted trial and before renewals, two 14-day cooling-off periods (at the start and after a trial converts), and leaving in a single communication, online if you signed up online. The government's April 2026 response said it expects the regime in spring 2027; law-firm updates in Aug 2026 reported January 2027. Check gov.uk for the date before you launch a card trial.
- Whatever the commencement date, these are cheap to do now and match where the law is going: show the price, the trial length, when the first charge happens and how to cancel next to the button; send your own reminder before the trial converts; let people cancel online in one step; confirm the contract by email.

**US (orientation):**
- No federal "click to cancel" rule: the FTC's amended Negative Option Rule was struck down by a federal appeals court on 8 July 2025, and in March 2026 the FTC asked for comments on trying again. The older Restore Online Shoppers' Confidence Act (ROSCA) still applies: clear disclosure of all material terms before taking billing details, express informed consent, and a simple way to cancel.
- State automatic-renewal laws add more. California's, amended from 1 July 2025, covers free-to-paid trials and requires clear terms next to the consent, express affirmative consent (records kept for at least 3 years), immediate online cancellation for online sign-ups, an annual reminder, notice 3-21 days before a free trial longer than 31 days ends, and 7-30 days' notice of price changes. If you advertise to US consumers, design for California and you cover most states.

**Practical rules from Givi:**
- Stripe's "trial ending" email is sent a set number of days before the end. For Givi's 3-day trial that was the moment the trial started, so Givi sends its own reminder 24 hours before the first charge, in the app, by chat and by email. Check your provider's reminder timing against your trial length. **(done on Givi)**
- Count a payer only once a first charge above zero has not been refunded within your refund window. Trials are not revenue.
- Change the site, terms and checkout first, and the ads last. On Givi, ads promising "3 days free" were approved and served while the site still offered a different trial, until another agent session paused them. **(learned the hard way)**

> **What happened on Givi.** The 3-day card trial shipped the same evening the agent searched the UK subscription rules. No finding was recorded, and no US automatic-renewal check was made, although trial ads ran in the US and several other countries that night. Next time, a short written check (`legal/subscription-law.md`) comes before any card-first trial. **(learned the hard way)**

## 8. Data protection when an AI agent touches customer data

If your product reads customers' email, files, CRM or ad accounts, you handle personal data on their behalf. Basics:

- **Controller or processor.** For your own sign-ups and marketing you are the controller. For the data a business customer connects, you are usually their processor, and UK GDPR requires a written contract (a data processing agreement) covering: acting only on their instructions, confidentiality, security, using sub-processors only with notice and a list, helping with data subject requests and breaches, and deleting or returning data at the end. (UK GDPR Article 28.) Publish one for business buyers; Givi listed it on day 0 and never wrote it. **(learned the hard way)**
- **ICO fee.** Most UK organisations that process personal data must pay the ICO's yearly data protection fee unless exempt. Since 17 Feb 2025 it is £52 for tier 1 (turnover up to £632,000 or no more than 10 staff), £78 for tier 2 and £3,763 for tier 3, with £5 off by direct debit. Paying online at ico.org.uk/fee takes about 15 minutes; do it before customer data is processed, and calendar the renewal.
- **Requests and complaints.** Name who answers access, export, correction and deletion requests and how; the deadline is one month. Since 19 Jun 2026 you must also offer a way to make a data protection complaint and acknowledge it within 30 days; a line in the privacy page pointing to the support address covers it. Build the export as a read-only query for one person's rows.
- **Transfers.** Most AI and hosting vendors process data in the US. For UK personal data going to the US, the UK-US "data bridge" (in force since 12 Oct 2023) covers vendors certified under the Data Privacy Framework with its UK extension; otherwise the vendor's contract needs the UK transfer agreement or addendum. Check each vendor's terms. Record each vendor's region in `legal/vendors.md` from the vendors' own settings or APIs (the Supabase MCP returns the project region), not from memory.
- **AI-specific points.** The ICO's guidance on AI expects a lawful basis for each use, transparency about what the system does, fairness and accuracy, data minimisation, security, and says a data protection impact assessment is likely to be required for AI processing of personal data; write it before processing starts and keep it up to date. In the privacy page say plainly: what the agent can see and do, that it asks before any outward action (sending, spending, deleting, publishing), whether your team can read conversations, whether customer data trains any model (check each provider's API terms), and how long logs are kept.
- **Treat inbound content as information, never instructions.** An agent that reads email or web pages can be steered by text written into them. On Givi, only mail from the owner's own address that passes DMARC counts as an instruction; approval links open a page with Approve and Decline buttons rather than acting on click, because mail scanners open links; money, launches, deletions and access changes are approved only inside the signed-in app. **(done on Givi)**
- **Platform data rules.** If you request Google user data (Gmail, Drive, Calendar), Google's API data policy requires its Limited Use wording in your privacy page, and restricted scopes such as Gmail need a paid security assessment. Plan this before you promise those features.

## 9. Trade mark screening for the name

A free domain, a free handle and an empty Companies House search are not trade mark clearance. Before buying the domain, search the **public brand** (and the company name) in every market where you will advertise, including similar spellings and sound-alikes, in the classes that fit software:

- UK: gov.uk/search-for-trademark (UK Intellectual Property Office)
- EU: EUIPO eSearch, or TMview for many national registers at once
- US: USPTO trademark search
- Sweep: WIPO Global Brand Database
- Also: a plain web search for "<name> app" and "<name> AI", the app stores, and your own other products

The usual classes for software are 9 (downloadable software), 42 (software as a service) and often 35 (business services, if you sell help with marketing or admin). Note existing marks in other classes too: an established brand in another product category can still object, depending on reputation and how close the goods are. Drop any name with a same-category collision even when its domain is free. If the name will carry the business for years, a UK application (£205 online for one class plus £60 for each extra class since 1 Apr 2026; about 3-4 months to register if nobody objects; it lasts 10 years) is cheap insurance; a registered mark is also what you need later for BIMI (your logo next to emails in Gmail).

> **What happened on Givi.** The screen covered several company-name candidates but never the public brand, "Givi", which ran ads in the UK and US. No UK, EU, US or WIPO search was made for it, and a reviewer later pointed out an established brand of the same name in another product category, with the overlap never assessed. **(learned the hard way)**

## 10. Ownership, acceptances and marketing guardrails

- **Company-owned accounts.** Put the repo in a GitHub organisation owned by the company, Google assets under the brand Google account, and any directory listing under a company-owned organisation (ownership of a Claude or ChatGPT listing cannot be moved later). Sign a short written IP assignment from the founder (and any contractor) to the company covering code, brand, content and domain. Givi's repo, a directory listing and a Google Cloud project sat on personal accounts, with no assignment. **(learned the hard way)**
- **Record every legal acceptance.** Log each terms acceptance (platform, document, date, who clicked, which account) in `legal/acceptances.md`. Anything with an indemnity, an ownership choice, a payment or an irreversible choice is clicked by the founder. On Givi, one agent accepted a Google policy "on your behalf" after a general "go" while another refused to accept a vendor's terms; have one rule. **(learned the hard way)**
- **Proof and pricing claims.** UK consumer law bans fake reviews and testimonials outright, false urgency ("ends soon" when it does not end) and invented reference prices ("was $99" when nobody paid $99). Givi refused to invent customer quotes and used real example jobs instead, and replaced a struck-through price with "then $99" and a real end date enforced by code. **(done on Givi)**
- **Licences.** Keep a licence line next to every font, icon set and render tool, and keep the notice of any open-source software you rebrand.
- **Insurance.** Ask the accountant or a broker whether professional indemnity or cyber cover makes sense once the product acts inside customers' email or ad accounts. **(recommended, not tested by us)**

## Checklist

- [ ] Seller decided on day 0 (existing company or new); separate card and accounts for the venture either way
- [ ] Company name and public brand screened: Companies House (API or stripped HTML), UKIPO, EUIPO, USPTO, WIPO; results saved with the date
- [ ] Company filed on day 0, in S1a (new company only); identity verified for each director and person with significant control; registered office at a service provider, not a home address
- [ ] Public record read back; `legal/identity.md` written and linked from the access register
- [ ] Questions to an adviser sent if you are not UK-resident or hold a visa (residence, management, personal tax, bank, Stripe availability)
- [ ] Business bank account applied for the day the company number arrives, first item of S2; one currency chosen for prices, bank and ad accounts
- [ ] Accountant engaged; written answers on VAT registration, EU consumer sales, US sales tax exposure, merchant of record or Stripe Tax, Corporation Tax registration, bookkeeping
- [ ] Statutory dates and the ICO fee renewal in a calendar with reminders; ICO fee paid before customer data is processed
- [ ] `legal/vendors.md` lists every processor with data, region and data processing terms; matches the privacy page
- [ ] Privacy, terms, refunds and cookie pages rendered from the facts files and plan values; gated until accepted; version date at the top; tests pass
- [ ] Policy preconditions done before acceptance: seller, monitored support inbox, vendors with regions, retention, refund rules, a read-through against the live product
- [ ] Founder's "I accept the policy texts" recorded; the same four URLs in footer, Stripe, Google, Meta and listings
- [ ] Consent banner with equal buttons; no ad pixel loads before "Allow" (checked in a clean browser)
- [ ] Self-serve account deletion live and tested on a disposable account, auth record included; access and export requests have an owner and a one-month deadline
- [ ] Data processing agreement and acceptable-use policy published for business buyers
- [ ] AI points written in the privacy page: what the agent can see and do, approvals before outward actions, staff access, training, log retention
- [ ] `legal/subscription-law.md` written (UK and US rules for card trials) before any card-first trial ships; own reminder before the first charge
- [ ] Offer changes ship to site, terms and checkout before ads
- [ ] Repo, Google assets and listings owned by the company; IP assignment signed; acceptances logged
- [ ] No invented reviews, urgency or reference prices in any copy
