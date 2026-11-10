# HomeSweet — Lease agreement & rental flow: legal review

**Date:** 6 November 2026 · **Scope:** `src/services/agreementService.js`, the lease preview in `src/components/RentalDashboard.vue`, `RentalApplicationView.vue`, `PaymentView.vue`, `firestore.rules` (agreements / rental_applications).
**This is an engineering review of what the app claims and does, not legal advice.** Cambodian-law points are marked **[verify]** and need a lawyer.

---

## 1. Summary

HomeSweet does **not** currently produce a lease that would stand up as a contract. It produces an *illustrative preview*. That is acceptable for a course prototype **only if the app never calls it binding** and users are told to get a real lease. This review fixed the claims, and lists what must be built before anyone could rely on it.

---

## 2. Claims the app made that were not true (fixed in this commit)

| Was | Problem | Now |
|---|---|---|
| "Legally Binding Electronic Lease · Verified via HomeSweet" | No signing, identity or form requirements are met; implies HomeSweet verifies the lease | "Sample agreement · illustration only, not a legal contract" |
| "Protected by HomeSweet Escrow" / "Protected in Escrow" | HomeSweet holds no money. Payments are only a Firestore record | "Sample tenancy" / "held by landlord per lease terms" |
| Tenant "ID: KH-8829102 · Verified"; landlord "License: KH-PP-RE-9012" | Invented identifiers presented as verified | "ID: sample data" / "Licence: sample data" |
| Signature "Signed Feb 01, 2026 (Verified)" | No signature happened | "Sample signature" |
| Footer "© HomeSweet, Inc." | Implies an incorporated company | "© 2026 HomeSweet · student project" |

The same seeded rental (Skystar Condo Unit 14B, $450) is still shown to **every** resident as their "Currently Renting" lease. It is now labelled as sample on the preview, but the dashboard KPIs still read as real. Recommendation: show seed data only for demo accounts, otherwise show the empty state.

---

## 3. Findings

### Critical
**L1 — Rental application is never saved, but the user is told it was.** `submitApplication()` writes a record that has `tenantId` but **no `applicantId`**, while `firestore.rules` requires `request.resource.data.applicantId == request.auth.uid`. The write is denied, the `catch` block invents a random `APP-XXXXXXX` reference and moves the user to the "confirmation" step. A student believes they applied; the landlord never sees it. (`RentalApplicationView.vue:~485` and `~539`.) Fix: set `applicantId` and `landlordId` (= `property.ownerId`), and show an error instead of a fake reference. *Not changed in this commit — it is a functional fix, say the word.*

**L2 — Agreement documents readable/writable by any signed-in user.** `storage.rules` → `agreement_docs/{agreementId}/**`: `allow read, write: if isAuthenticated()`. Any account can read or overwrite any contract file. Tie access to the agreement's `landlordId`/`tenantId` via a Firestore lookup.

### High
**L3 — Either party can rewrite the agreement.** `firestore.rules` → `agreements` `allow update` lets the landlord or tenant change *any* field: rent, deposit, dates, status, and the **other party's signature**. Restrict updates to specific fields per role and validate the status transition server-side (`canTransitionAgreement` runs only in the browser).

**L4 — A landlord can create an agreement naming any tenant.** `create` only checks `landlordId == auth.uid`; `tenantId` is arbitrary. The named tenant never consented. Require tenant acceptance before status can leave `pending_tenant`, and require the tenant to be the one who sets their own `tenantSignedAt`.

**L5 — Defaults fabricate a signed, active contract.** `createNormalizedAgreement()` defaults to status `active`, both signatures to *now*, and demo names/emails (`Skystar…`, `Alice Freeman`). Any call with missing data yields an apparently executed lease. Defaults should be `draft`, signatures `null`, no demo parties.

**L6 — A timestamp is not a signature.** There is no binding of signer to identity, no record of which text was agreed, no IP/user-agent, no audit trail, no document hash. Cambodia's Law on E-Commerce recognises electronic signatures **[verify requirements]**; at minimum record: signer UID, time, agreement version hash, and a consent statement; keep it append-only.

### Medium
**L7 — Lease content is too thin to be a lease.** The preview covers parties, premises, term, rent, deposit, utilities and four house rules. Missing, at minimum:
- precise identification of the lessor's **right to let** (title / authority) and of both parties (ID numbers kept off the public page);
- permitted use, number of occupants, subletting;
- rent payment method, currency (USD/KHR), late-payment consequences;
- **deposit**: purpose, deductions, inspection, return deadline;
- repairs and maintenance responsibility; landlord entry notice;
- renewal, termination, early termination and notice periods;
- handover condition / inventory;
- utilities billing method (the preview quotes fixed $0.20/kWh, $0.50/m³ — **[verify]** against actual tariffs, and say they are examples);
- dispute resolution, governing law (Cambodia), language;
- taxes (rental tax / withholding) **[verify]**.

**L8 — Language and formalities.** Contracts in Cambodia are commonly in Khmer; an English-only electronic lease may be hard to enforce or to register **[verify]**. Lease registration / notarisation for longer terms **[verify]**.

**L9 — Money language in the application and payment flow.** The application adds a 10% "tax"/VAT and "typically 2× rent" deposit as if standard. `PaymentView.vue` accepts card/KHQR/Wing inputs and writes a `payments` record with `status: 'succeeded'` and the billing address, with no gateway behind it (the card number is not written to the record — keep it that way). Even so, a form that looks like a real checkout will get real card numbers typed into it: add a visible "Demonstration payment — no money is taken, do not enter a real card" banner, and keep card fields out of any stored data. The receipt/invoice also reads as a real tax invoice — label it as a sample.

**L10 — Documents step is cosmetic.** The ID and income-proof inputs in `RentalApplicationView.vue` keep the `File` in memory (`handleFile`) and never upload it. Users believe they submitted documents. Either upload to a private Storage path (and add retention rules) or remove the step.

### Low
**L11 — Agreement IDs and codes are random** (`Agreement-${random}`, `AGR-${Date.now()}`) and can collide. Use Firestore auto-IDs.
**L12 — Terms of Use now say HomeSweet is not a party to leases, holds no escrow, and lease previews are illustrative.** Keep the UI consistent with that (e.g. do not add "guaranteed", "secure payment", "escrow" copy later).

---

## 4. Minimum viable "real" agreement (if the client wants it)

1. Landlord fills a template with the clauses in L7; status `draft`.
2. Landlord signs → server-validated transition to `pending_tenant`; document hash stored.
3. Tenant reads the **same hash**, signs with explicit statement → `active`. Each party can only write their own signature field.
4. PDF with both signature blocks, hash and timestamps; Storage access limited to the two parties.
5. Lawyer reviews the template once (L7/L8), then it is frozen with a version number.

Estimated effort exceeds the course hours budget alongside the other scope — recommended to **keep the preview as a clearly-labelled sample** and put this in the A1 plan as future work.

---

## 5. Status (updated 6 Nov 2026, second pass)

| Finding | Status |
|---|---|
| §2 false claims | **Fixed** |
| L1 application never saved | **Fixed in code** — now sets `applicantId`/`landlordId`, requires sign-in, shows an error instead of a fake reference |
| L2 `agreement_docs` open to all | **Fixed in `storage.rules` — NOT DEPLOYED** (admin-only; nothing in the app uses this path) |
| L3 either party can rewrite agreement | **Fixed in `firestore.rules` — NOT DEPLOYED** (parties may change only `status`, `signatures`, `updatedAt`, and only their own signature) |
| L4 landlord can create signed agreement for any tenant | **Partly fixed in `firestore.rules` — NOT DEPLOYED**: create must be `draft`. Tenant-consent step still not built |
| L5 defaults fabricate signed contract | **Fixed** — default `draft`, signatures only set once the status reaches that stage, no demo parties |
| L6 signature is only a timestamp | Open (design work, see §4) |
| L7 / L8 thin clauses, language, formalities | Open (needs lawyer) |
| L9 payment looks real | **Banner added**; card number still not stored |
| L10 documents step cosmetic | **Notice added** ("not uploaded or stored"); real upload still not built |
| L11 random IDs | Open (low) |

Deploy the rules with `npx firebase-tools deploy --only firestore:rules,storage` after testing with a real signed-in account (see `docs/PROJECT_STATE.md` §11.3). The new `agreements` update rule reads `signatures.*` fields, so it fails closed (denies) on documents that lack a `signatures` map.
