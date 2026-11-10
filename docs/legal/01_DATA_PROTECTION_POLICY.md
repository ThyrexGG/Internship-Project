# HomeSweet — Data protection policy & KYC control (internal)

**Status:** draft v1 · **Date:** 6 November 2026 · **Closes:** Session 3 item *"Data protection: no real ID photos on the live site, or confirm test data only"*
**Not legal advice.** Written by the project team; **needs review by a Cambodian lawyer or CamTech counsel before anything here is relied on** (see §10).

---

## 1. The rule (paste this line into the charter / A1)

> **HomeSweet does not collect real government ID photos, ID numbers or face images from anyone during FECO301.** Identity verification runs only in `test` mode (synthetic demo ID, no third-party OCR, no selfie upload) or is switched `off`. `live` mode stays disabled until every blocker in §9 is closed *and* the client has agreed in writing.

---

## 2. What changed in the code (this commit)

| Control | Where | Effect |
|---|---|---|
| `VUE_APP_KYC_MODE` = `off` \| `test` \| `live` | `src/config/legal.js` | Default `test`. Unrecognised values fail safe to `off`. |
| Consent / attestation gate | `VerifyAccountView.vue` | Nothing in the wizard is reachable until the user ticks a mode-specific box. `off` shows "verification paused". |
| Third-party OCR only in `live` | `IdUploadStep.vue` | In `test`/`off`, the ID image is **not** sent to Google Cloud Vision (previously sent whenever a key was configured). |
| Stop copying ID number to `users/{uid}` | `VerifyAccountView.vue` | The `users` collection is readable by every signed-in user. The ID number now lives only in `verification_requests` (owner + admin). |
| Remove fake fallback ID number | `VerifyAccountView.vue` | Was `'0102938475'`; now `null`. |
| Consent record | `users/{uid}.consent`, `verification_requests.consent` | `{version, acceptedAt, source/purpose, kycMode}` — proof of what text was accepted. |
| Signup consent + 18+ | `LoginView.vue` | Required checkbox (email) and notice (social). |
| Privacy Policy and Terms of Use | `/privacy`, `/terms`, footer | In-app source of truth for user-facing text. |
| Misleading claims removed | `SuccessStep.vue`, `RentalDashboard.vue`, footer | Removed "256-bit", fake "98.6%", "Est. 15 mins", "Protected by Escrow", "Legally Binding", "© HomeSweet, Inc." |

**Production setting:** set `VUE_APP_KYC_MODE=off` on the live build unless a scheduled test session is running, then set it back. `test` is the default only so the existing usability protocol keeps working.

---

## 3. Legal framework (to verify)

As far as the team could establish (desk knowledge, **no lawyer consulted, not re-checked against current sources**):

- Cambodia has **no single comprehensive personal-data-protection statute in force**; a draft law has been discussed. Relevant provisions are scattered: the Constitution (privacy of residence and correspondence), the **Law on Electronic Commerce (2019)** (includes personal-data and e-signature provisions), the Civil Code, and sector rules.
- Some users may be foreign nationals (seed data includes French users). **GDPR** could apply to EU residents in theory. Low probability for this project, but we use GDPR-style principles (consent, purpose limitation, minimisation, retention, access/erasure) as the design benchmark because they are the strictest realistic standard and the easiest to explain.

**Action:** ask counsel two questions — (a) what the Law on E-Commerce requires of an operator that stores IDs, (b) whether a student project needs any registration or notification.

---

## 4. Data inventory (what is actually stored today)

| Data | Where | Who can read (current rules) | Sensitivity | Note |
|---|---|---|---|---|
| Email, password hash | Firebase Auth | Google/Firebase; project admins | Medium | |
| Name, email, role, avatar, `consent` | Firestore `users/{uid}` | **Any signed-in user** (`allow read: if isAuthenticated()`) | Medium | Needed for chat search/profiles |
| Phone, date of birth, gender, university, job, hobbies | `users/{uid}.profile` | **Any signed-in user** | **High** | Phone and DOB should not be world-readable to members. Blocker B1. |
| Profile photo | Storage `users/{uid}/*` | **Public** | Medium | |
| Verification request: name, email, ID type/number, face-match score, liveness flag, nationality, sex, consent, kycMode | `verification_requests` | Owner + admin | **High** | ID number is `null`/demo in `test` mode |
| ID image | Held in browser memory as a `blob:` URL; **not uploaded**. In `live` mode only, base64 is sent to Google Cloud Vision. | — | **Very high** | The stored `idPreviewUrl` is a session-local blob URL, so reviewers cannot actually see it. This build cannot do real review. |
| Selfie | Not stored. `selfieUrl` is a fixed demo image path. Face comparison runs in the browser. | — | Very high (if stored) | |
| Rental application: name, email, income, occupants, message, declarations | `rental_applications` | Applicant, landlord, admin | High | ID / income files are chosen in the form but **never uploaded** |
| Chat messages + attachments | `messages`, `chats/*/messages`, Storage | Participants + admin | High | |
| Payment *records* (no real money) | `payments` | Payer, landlord, admin | Medium | |
| Agreements | `agreements`, Storage `agreement_docs/*` | Parties + admin; **Storage: any signed-in user** | High | Blocker B3 |
| Notifications | `notifications` | Recipient / admin | Low | |

---

## 5. Purpose, basis, minimisation

| Purpose | Basis | Minimisation |
|---|---|---|
| Run accounts, listings, chat, applications | Consent at signup (Terms + Privacy ticked, 18+) | Collect only what the feature needs |
| Roommate matching | Consent; fields are optional | Hobbies/lifestyle optional |
| Identity verification | **Separate, explicit consent** at the KYC gate | `test`: synthetic data only. `live`: ID + face check, nothing else |
| Abuse / safety review | Legitimate interest of the platform, stated in Privacy Policy | Admins only |

No advertising, no selling, no profiling beyond roommate compatibility.

---

## 6. Retention schedule (proposed — the team must approve)

| Data | Keep | Delete when |
|---|---|---|
| Test-mode verification requests | Until the test round's analysis is done | End of each usability round; no later than end of FECO301 |
| Live-mode verification data (if ever enabled) | 30 days after decision | Automatic job (not built — blocker B5) |
| Account/profile | While account exists | Account deletion, or wipe of the course database |
| Chat, applications | While account exists | Account deletion |
| Usability session notes | Anonymised IDs only (`HS-P01…`); no names, no student numbers | End of course |
| Consent records | Same lifetime as account | With the account |

---

## 7. Who is responsible

**Reality check:** HomeSweet has no legal entity. Until one exists (or CamTech / the client formally takes responsibility), **the six team members are the people answerable** for the data. Counsel must confirm what that means in Cambodia (§10).

Fill every name below in Week 4 and record it in the team contract. Each role has one owner and one backup, and neither may be the same person for all roles.

| Role | Responsibility | Owner | Backup |
|---|---|---|---|
| **Data owner** | Final say on what is collected, kept and deleted; approves any change to `VUE_APP_KYC_MODE`, rules or this policy | [ ] | [ ] |
| **Admin-access owner** | Keeps the admin list to named members; removes access when someone leaves; guards Firebase console + API keys | [ ] | [ ] |
| **Deletion / access-request handler** | Runs §8 "Access / correction / deletion request" within 30 days | [ ] | [ ] |
| **Breach lead** | Runs §8 "Suspected breach"; informs client and users | [ ] | [ ] |
| **Test-session lead** | Makes sure only synthetic IDs are used and test data is deleted after each round | [ ] | [ ] |
| **Legal contact** | Talks to counsel; keeps §10 questions and answers | [ ] | [ ] |
| **Client / sponsor** | Informed of this policy and of any incident; does **not** own the data | [client name] | — |

**Principle:** the safest way to be responsible for ID data is to not hold it. Only `test`/`off` are allowed until §9 is closed.

## 7a. Access and processors

- **Admins:** `admin@homesweet.com`, `thyrexgg@gmail.com` (both only count if the email is **verified**), or `users/{uid}.role == 'admin'` (see `firestore.rules`). Keep this list to the named admin-access owner's approved members.
- **Admin console gate (changed):** the visible PIN is removed. The console now opens only for a signed-in account that is an admin by email (verified) or role. This check in the browser is a convenience; `firestore.rules` and `storage.rules` re-check on every request. **After deploying the rules, `admin@homesweet.com` will lose admin access unless its email is verified or its `users` document has `role: 'admin'`.** `thyrexgg@gmail.com` (Google sign-in) is unaffected.
- **Processors:** Google Firebase (Auth, Firestore, Storage), Google Maps / Vision (Vision only in `live`), OpenStreetMap Nominatim (coordinates only), Google Fonts (IP address), Cloudinary (legacy, confirm still used). **No data-processing agreements signed.** Firebase project region: **confirm** in the console (not recorded in the repo).

---

## 8. Procedures

**Access / correction / deletion request:** user contacts team via Settings → Help → team member verifies identity by replying from the account email → delete `users/{uid}`, `verification_requests` where `userId == uid`, chats the user owns, Storage `users/{uid}/*` and `verification_docs/{uid}/*`, and the Auth account → reply within 30 days. *Tooling for this does not exist; it is a manual console task today.*

**Suspected breach:** (1) revoke the affected credentials / switch `VUE_APP_KYC_MODE=off` and redeploy; (2) note time, what data, how many users; (3) tell the client and affected users without undue delay; (4) fix, then record the cause in `docs/legal/incidents.md` (create when first needed).

**Usability test sessions** (links to `HOMESWEET_FINAL_USABILITY_EVALUATION_FORM.md`, Part I caution): participants use only the synthetic `id_good.png` / `selfie_good.png`; moderator confirms the "test mode" box is understood; no real names on sheets; recordings, if any, need separate written consent.

---

## 9. Blockers before `live` mode may be switched on

| # | Blocker | Why |
|---|---|---|
| B1 | Restrict `users` read: split public profile (name, avatar, role) from private fields (phone, DOB, consent) | Any member can currently read any other member's phone/DOB |
| B2 | ~~Replace client PIN; add `email_verified`~~ **Done in code (rules not yet deployed).** Remaining: custom admin claims, and confirm `admin@homesweet.com` is verified or has role `admin` | Anyone could register an admin email before the real owner does |
| B3 | Lock `agreement_docs` and `property_images` Storage rules to the right parties | Any signed-in user can read/write |
| B4 | Real server-side ID check + private upload to `verification_docs/{uid}` and a reviewer view that shows it | The current build neither stores nor displays the ID image |
| B5 | Automated deletion (scheduled job) per §6 | Retention promise otherwise unenforceable |
| B6 | Remove `livenessPassed ?? true` default and hard-coded `selfieUrl` | A missing liveness result is currently recorded as a pass |
| B7 | Restrict the Vision / Maps API keys by referrer + API in Google Cloud (keys ship in the JS bundle) | Key abuse |
| B8 | Lawyer review of this document, Privacy Policy and Terms | See §10 |
| B9 | Written client agreement that live KYC is wanted and who is responsible | Charter condition |
| B10 | Confirm Firebase region and who pays for the Blaze plan | Cost + data location |

Cloud Functions needed for B4/B5 need the Blaze plan — the charter lists that cost as unconfirmed, so **`live` is realistically out of scope for this course.** Recommended decision: keep `test`/`off` and document the design instead.

---

## 10. Questions for counsel

1. Is HomeSweet, run by students under a university course, a "data controller" under Cambodian law? Any registration?
2. Is "consent by checkbox" enough for storing ID numbers, or is a signed paper form required?
3. May we keep a copy of a Cambodian National ID at all, or only inspect and discard?
4. Is a click-through e-signature on a lease valid? What formalities (language, registration, notarisation) apply to leases of different lengths?
5. Do we need a Khmer-language version of the Privacy Policy and Terms for them to bind Khmer-speaking users?
6. Any liability for hosting listings if a landlord defrauds a tenant? Are our disclaimers adequate?

---

## 11. Review log
*(§7 and §7a were added in the same session; sections after §7 were not renumbered.)*

| Date | Who | Change |
|---|---|---|
| 2026-11-06 | team (drafted with Claude) | v1 |
