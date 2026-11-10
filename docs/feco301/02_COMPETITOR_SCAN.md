# HomeSweet — Competitor scan (Analyse)
**For:** FECO301 Session 3 · **Date:** 3 November 2026  
**Sources:** public websites and news, desk research only. **Not** a substitute for talking to users of those products.  
**Thomas’s ask:** cover Khmerhome, Bamnang, **and** at least one other Cambodian initiative; what they offer, who uses them, how they verify, then what HomeSweet does differently *or* whether partnering is smarter than competing.

---

## 1. How to read this
Cambodia already has listing portals, agent marketplaces, and at least one student-housing operator with a “verified rooms” claim. HomeSweet’s only defensible difference is **trust for independent student–landlord matching** — if landlords will join. If they will not, the idea fails regardless of UI.

---

## 2. Named competitors

### A. Khmerhome — general property classifieds
| | |
|---|---|
| **What it is** | Cambodia sale / rent portal and app (houses, apartments, commercial, land). Agent directory, map search, land-area tools, automated land-price valuation. |
| **Who uses it** | Buyers, renters, and agents looking for **volume listings**, not student KYC. Office: St. 306, BKK1. App since ~2018. |
| **How it verifies** | **No public identity or listing-verification product** found. Listings appear agent/owner-submitted. Title/agent checks are left to the user (RPR licence, cadastral due diligence). |
| **Implication** | HomeSweet should **not** compete on catalogue size. Khmerhome already owns “search a lot of properties.” |

Sources: [khmerhome.com/about](https://www.khmerhome.com/about), [App Store listing](https://apps.apple.com/kh/app/khmerhome/id1329326284).

### B. Bamnang — student housing operator + super-app
| | |
|---|---|
| **What it is** | Student (and now young-professional) **housing operator** plus an app: rooms, events, scholarships, mentoring, payments/invoices for *their* residents. Campuses in Chamkarmon, Russey Keo, Toul Kork; rooms roughly **$16–$63/week** dorm/private, higher at Tha Da Tra. Founded as a pivot (Mar 2024); first MVP campus Dec 2024. MoU with Thadatra Residence (2026) for professional housing. |
| **Who uses it** | Students near RULE / urban campuses; residents of Bamnang-managed buildings. Not a marketplace for random independent landlords. |
| **How it verifies** | Marketing: **“verified student rooms near campus.”** Verification is **operator-side** (they run or partner on the buildings), not a third-party ID pipeline for any landlord. CEO interview: they work with landlords/institutions on standards; they explicitly did **not** want “another listing site.” |
| **Implication** | Closest **student** overlap. Competing with Bamnang on *owned campuses* is a losing Advise option. Sensible options: (1) **partner** (they have rooms, HomeSweet has CamTech students / KYC process), or (2) **differentiate** on *independent* rooms Bamnang does not operate. |

Sources: [bamnang.com](https://bamnang.com/), [app.bamnang.com/room](https://app.bamnang.com/room), [Cambodia Investment Review, Jan 2026](https://cambodiainvestmentreview.com/2026/01/06/leader-talks-rothsethamony-seng-on-building-bamnang-and-the-investment-case-for-cambodias-next-gen-education-infrastructure/).

---

## 3. The other Cambodian initiatives (the gap Thomas flagged)

The team named Khmerhome and Bamnang. Two further initiatives matter; the first is the large incumbent, the second is the closest *product* analogue.

### C. realestate.com.kh — incumbent portal with “certified listings”
| | |
|---|---|
| **What it is** | Leading Cambodia property portal since 2009; ~50k listings, site + app, concierge, expos. Phnom Penh rent search on the order of **30,000+** homes; studio median around **$450/month**. |
| **Who uses it** | Agents, developers, expats, mid/high renters — not CamTech-from-the-provinces as a designed persona. |
| **How it verifies** | **Certified listing:** staff **physically visit**, record a walkthrough, and rank certified above unverified. Aimed at stale/fake agent listings — **property existence**, not tenant/landlord biometric ID. |
| **Implication** | Proof that the Cambodian market already pays for *some* verification (staff visit). HomeSweet’s ID/face pipeline is a different (and more sensitive) bet. Do not claim “first to verify listings in Cambodia.” |

Sources: [About](https://www.realestate.com.kh/about/), [certified listings announcement](https://www.realestate.com.kh/news/Revolutionizing-real-estate-technology-Launch-of-new-website-mobile-app/).

### D. CamboRent — map-first rental marketplace (closest “similar initiative”)
| | |
|---|---|
| **What it is** | Cambodia rental marketplace for locals and expats: map-first browse, owners **and** agencies, flag-and-takedown of bad photos/prices/addresses. Public site still shows a **demo** (“1,600+ mock listings”). |
| **Who uses it** | Intended: renters tired of messaging to learn the address. Stage: early / demo — treat claims as **unproven at scale**. |
| **How it verifies** | User **flags** → review team → pull misrepresenting listings. Honesty via **moderation**, not KYC. |
| **Implication** | Same *problem family* (trust in listings) without student KYC. If CamboRent is live among CamTech students, HomeSweet must explain the extra identity step. If it is still demo, HomeSweet’s live MVP is ahead on existence, behind on listing honesty process. |

Source: [camborent.com](https://camborent.com/).

### Informal alternatives (not products, but they win today)
Facebook groups, Telegram, and WhatsApp are how many students actually find rooms. **Zero verification.** Landlord interviews should ask: “Do you already fill rooms this way? Would a portal be worth it?”

---

## 4. Comparison (for Advise)

| | Khmerhome | realestate.com.kh | Bamnang | CamboRent | **HomeSweet (today)** |
|---|---|---|---|---|---|
| Model | Classifieds | Portal + certified visits | **Operator** housing + student app | Map marketplace | Student web MVP + KYC UI |
| Student-specific | No | No | **Yes** | No | **Yes** |
| Independent landlords | Yes (agents) | Yes (agents) | Mostly own/partner buildings | Owners + agencies | Intended; **unproven** |
| Listing verification | Unclear / none | Staff visit + video | Operator control | User flags | Weak (demo + Firestore mix) |
| Person verification | No | No | Resident of their campus | No | Face-api **in browser** (ethics red) |
| Who pays | Agents / ads (assumed) | Agents / certified product | Residents of Bamnang | Unclear | **Open** |

---

## 5. What HomeSweet does differently — or should not
**Different (if we can prove it):** a CamTech-oriented **process** that verifies *both* the listing and the student, on a web app students already tested — not another 30,000-listing portal, and not another Bamnang campus.

**Not different (do not claim):** “first housing app in Cambodia,” “first verification,” “full Flutter product,” “real payments.”

**Partner vs compete (Advise, not build):**
1. **Compete with Khmerhome / realestate.com.kh on volume** — reject (out of scope and hours).
2. **Compete with Bamnang on owned student housing** — reject unless landlords prove a parallel independent supply.
3. **Partner with Bamnang or Student Affairs for inventory/access; HomeSweet owns the verification process** — keep as an Advise option after landlord interviews.
4. **Narrow to CamTech + a handful of landlords + Trust Score on the web MVP** — **recommended course project.**

---

## 6. Still to do (not desk research)
- [ ] Confirm with 3+ landlords: list / verify / pay  
- [ ] Ask 5 CamTech students which of the four they have actually used  
- [ ] One call or email to Bamnang / Student Affairs on partnership (optional, after client is named)  
- [ ] Record who Thomas meant if he names a different “existing initiative” in Session 3  

---

## 7. Source log
| Source | Date accessed |
|---|---|
| https://www.khmerhome.com/about | 3 Nov 2026 |
| https://apps.apple.com/kh/app/khmerhome/id1329326284 | 3 Nov 2026 |
| https://bamnang.com/ | 3 Nov 2026 |
| https://app.bamnang.com/room | 3 Nov 2026 |
| Cambodia Investment Review, Bamnang Leader Talks | 3 Nov 2026 |
| https://www.realestate.com.kh/about/ | 3 Nov 2026 |
| realestate.com.kh certified-listings news article | 3 Nov 2026 |
| https://camborent.com/ | 3 Nov 2026 |
