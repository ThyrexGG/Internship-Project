# HomeSweet — One-page project charter (FECO301)
**Course:** FECO301 Project Management · **Date:** 3 November 2026 (Week 3) · **Status:** draft for Session 3  
**Decision to meet:** Session 2 — *approved with conditions* (Thomas, 27–28 Oct 2026)

Yellow items in the Gantt (`HomeSweet_FECO301_Gantt.xlsx`) and the blanks below still need the team’s names, signatures, and interview evidence.

---

### Client
| Role | Who | Status |
|---|---|---|
| **Client (must sit outside the team)** | **To confirm in writing this week.** Preferred: CamTech Student Affairs (students arriving from the provinces). Alternative: a named small group of landlords who will review progress. | Open — Session 3 condition |
| **Sponsor** | i-Hub (Virtubis) | Named; not the client |
| **Users** | CamTech / Phnom Penh students seeking a room; independent landlords listing rooms | Students evidenced (32 directional survey answers). Landlords **not** evidenced yet |

The client is **not** “the HomeSweet venture.” The team cannot be its own client.

---

### Problem
Students moving to Phnom Penh (especially from the provinces) cannot tell which rooms and which landlords are trustworthy. Existing portals are either general classifieds (volume, little identity) or operator-owned student housing (Bamnang). Independent landlords have not been asked whether they would list, accept verification, or pay. Until those answers exist, the marketplace is only half-proven.

---

### Purpose
Run a **bounded 15-week project** that designs, realises, and tests **a verified process for listings and students on the existing HomeSweet web app**, validated with landlords and piloted with CamTech students — not a new product roadmap.

---

### Scope (in)
- Competitor and landlord analysis (Analyse) feeding options (Advise)
- Listing / landlord verification on the **current web MVP**
- Identity checks **moved off the browser** (design + limited prototype; **no live ID photos** until consent and retention exist)
- One simple **Trust Score** (listings/students), not two scores
- Fixes from the existing usability backlog
- Two Realise cycles with the same usability protocol: **cycle 1 = Weeks 6–8**, **cycle 2 = Weeks 9–10**
- Data-protection rules: purpose, consent, retention, who can see ID data

### Scope (out of this course)
- Flutter app (Advise decision: **stay on web**)
- Real payments / ABA KHQR live money
- Push notifications, fraud-rule engines, Cloud Functions at $70–120/month unless budget is confirmed in writing
- Roommate score (defer)
- 50-student operational pilot unless the client confirms access
- Competing as a full classifieds portal against Khmerhome / realestate.com.kh

---

### Success criteria (course, not “more features”)
1. Week 3 charter accepted; named client signs a one-line review agreement.
2. ≥3 landlord interviews recorded (list / verify / pay).
3. A1 integrated plan (WBS, Gantt, budget, risks) submitted **by end of Week 5**.
4. Live site collects **no real ID photos or face scans** (test data only, or KYC off).
5. Two documented usability cycles on the trust process.
6. Honest close-out: what was validated, what remains unknown, what is internship leftover vs new course work.

---

### New work vs internship (baseline = presentation Slide 8)
| Already built (internship) | Incomplete | Missing / course work |
|---|---|---|
| Live Vue web MVP, auth, browse, landlord panel, feeds/chat, KYC **UI**, usability protocol, 32 student answers | Applications/roommates not persisted; mixed mock + Firestore listings; browser-side face match; admin PIN in the client | Landlord evidence; competitor differentiation; client outside team; consent/retention; server-side ID checks; Trust Score; two test cycles; who pays cloud |

---

### Advise (genuine choices — do not build both)
1. **Platform:** Flutter **or** web → **recommend web** (MVP exists; Flutter is out of hours).
2. **Identity:** browser face-api **or** server-side check with consent → **recommend server-side + stop live PII** until rules exist.
3. **Who pays:** students / landlords / university — **open**; landlord + client interviews must answer this.
4. **Compete or partner:** Bamnang owns operator housing; HomeSweet should **not** copy their campuses. Option to partner on inventory vs compete on **independent, verified listings**.

---

### Constraints, risks, ethics
- Effort cap: **~5 hours / student / week × 6 students × 15 weeks ≈ 450 hours**.
- Cloud cost during the course: **unconfirmed** (who pays?).
- Ethics red: ID photos, readable ID numbers, admin PIN and face matching in the browser, no retention policy.
- Immediate control: treat production KYC as **test-only** until Session 3 data-protection action is closed.
- **Data-protection rule (policy line):** HomeSweet does not collect real government ID photos, ID numbers or face images from anyone during FECO301. Identity verification runs only in `test` mode (synthetic demo ID, no third-party OCR, no selfie upload) or is `off`; `live` stays disabled until the blockers in `docs/legal/01_DATA_PROTECTION_POLICY.md` §9 are closed and the client agrees in writing. Users accept a Privacy Policy and Terms of Use (18+) at signup. Draft legal pack: `docs/legal/` (not yet reviewed by a lawyer).

---

### Team
Six members (names and work-share go in the team contract). One class project-council representative: **\_\_\_\_\_**.  
This charter is the Week 3 artefact. It is not yet a substitute for the signed client note, team contract, or landlord interview pack.
