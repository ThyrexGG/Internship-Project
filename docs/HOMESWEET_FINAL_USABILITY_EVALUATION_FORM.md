# HomeSweet: Final Prototype Usability Evaluation & Observation Instrument
> **Document Type:** Master Usability Test Protocol, Observer Observation Sheet & Evaluation Framework  
> **Project:** HomeSweet — Student Housing & Roommate Living Platform  
> **Study:** Final Prototype Usability & Trust Evaluation  
> **Status:** Approved Evaluation Instrument  
> **Target Audience:** Usability Evaluators, UX Researchers, Test Moderators, Observers, and Product Engineers  

---

## Methodological Foundation & Research Philosophy

### The Central Evaluation Framework
For HomeSweet, the central evaluation question goes far beyond basic UI mechanics:
> **"Can students successfully find appropriate housing and compatible roommates, understand why the system recommends them, recognize trustworthy versus risky interactions, protect their privacy, recover from problems, and make housing decisions with greater confidence?"**

### Evaluation Sequencing & Integrity
Do **NOT** combine heuristic evaluation and participant user testing into a single mixed activity. Maintain strict empirical separation:
```
1. Expert Heuristic Evaluation (Pre-Test)
   └── Consolidate predictive violation hypotheses
2. Participant Usability Testing (Empirical Observation)
   └── Zero evaluator hints; test actual user mental models
3. Synthesis & Triangulation
   └── Compare empirical observations against expert predictions
4. Prioritized Redesign (P0 - P3)
   └── Targeted retest on critical friction points
```
*Academic Rigor Note:* If an expert predicts "Users may not understand the verification badge," do not inform the participant. If 7/10 users fail to understand it independently, you have empirical confirmation. If 10/10 understand it immediately, the expert prediction is refuted.

---

# Part A: Evaluation Information

| Field | Record |
| :--- | :--- |
| **Project** | HomeSweet |
| **Study** | Final Prototype Usability Evaluation |
| **Prototype Version** | `________________________` |
| **Test Date** | `YYYY-MM-DD` |
| **Participant ID** | `HS-P___` *(Do not record participant legal names)* |
| **Moderator** | `________________________` |
| **Observer** | `________________________` |
| **Test Device** | `[ ] iPhone 14/15/SE  [ ] Android Flagship/Mid  [ ] Desktop (Chrome/Edge/Firefox)` |
| **Operating System** | `________________________` |
| **Browser / Version** | `________________________` |
| **Session Start Time** | `HH:MM` |
| **Session End Time** | `HH:MM` |

### Participant Persona & Rental Profile
*Check all that apply:*
- [ ] Student currently renting accommodation
- [ ] Student previously rented accommodation
- [ ] Student planning to rent in the next 1–6 months
- [ ] Student with prior roommate experience
- [ ] Student without prior roommate experience

> [!IMPORTANT]
> **Data Privacy & Ethical Protocol:** Never record participant legal names or student identification numbers on this observation instrument. Participant IDs (`HS-P01`, `HS-P02`, etc.) preserve participant anonymity and meet academic research ethics standards.

---

# Part B: Evaluation Objectives & Measurement Dimensions

### Primary Objective
Evaluate whether representative target students can **independently and confidently** navigate, comprehend, and complete HomeSweet's end-to-end student-housing journey.

### The Six Evaluation Dimensions
```
┌─────────────────┬─────────────────────────────────────────────────────────────┐
│ Dimension       │ Core Measurement Criteria                                   │
├─────────────────┼─────────────────────────────────────────────────────────────┤
│ 1. Effectiveness│ Can participants accomplish their accommodation goals?      │
│ 2. Efficiency   │ How much time, cognitive effort, and pathing is required?    │
│ 3. Learnability │ Can first-time users understand interface affordances?      │
│ 4. Comprehension│ Do users correctly interpret listing data and system states?│
│ 5. Trust & Safety│ Do verification, fraud badges, & rules inspire confidence?   │
│ 6. Satisfaction │ How do participants perceive and rate the holistic UX?      │
└─────────────────┴─────────────────────────────────────────────────────────────┘
```

---

# Part C: Pre-Test Participant Profile

*Administer verbally or via brief pre-test screener before exposing the participant to the HomeSweet interface.*

**P1. Have you searched for rental accommodation before?**
- [ ] Never
- [ ] Once
- [ ] Several times

**P2. What platforms or methods have you previously used to find housing?**
- [ ] Facebook Groups / Marketplace
- [ ] Telegram Channels
- [ ] TikTok / Social Media
- [ ] Dedicated Real-Estate Websites
- [ ] Property Agents / Brokers
- [ ] Friends / Family Recommendations
- [ ] Other: `________________________________________`

**P3. Have you ever lived with a roommate / flatmate?**
- [ ] Yes
- [ ] No

**P4. How confident are you using rental mobile apps and websites?**
```
1 — Very inexperienced   [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5   5 — Very experienced
```

**P5. Before seeing HomeSweet, what are the THREE most critical factors you consider when choosing accommodation?**
1. `____________________________________________________________________`
2. `____________________________________________________________________`
3. `____________________________________________________________________`
*(Note: Compare these 3 factors against the participant's later listing evaluation behavior in Task T3 to verify if HomeSweet's information architecture supports what students care about most).*

---

# Part D: Master Task Observation Sheet Architecture

*Every task in Parts E through M utilizes this exact rigorous observation structure. This enforces strict separation between raw observable behavior, direct quotations, and researcher interpretation.*

> [!NOTE]
> **Observation ≠ Interpretation:** Record what the user literally said and did before drawing evaluative conclusions.

### Standardized Task Block Template
```
TASK [ID] — [TASK TITLE]
Scenario Presented:
"___________________________________________________________________________________"

Timing:
• Start Time: _________  • End Time: _________  • Total Duration: _________ seconds

Task Outcome:
[ ] Success          — Independently completed goal without errors or external help
[ ] Partial Success  — Reached goal, but missed minor requirement or required neutral prompt
[ ] Failure          — Unable to reach goal / made unrecoverable error / required direct instruction
[ ] Abandoned        — Participant gave up or moderator intervened to terminate task

Assistance Level:
[ ] 0 — None (Completely autonomous)
[ ] 1 — Think-aloud reminder only ("Remember to tell me what you're thinking")
[ ] 2 — Neutral clarification ("What do you expect that button to do?")
[ ] 3 — Direct operational assistance (Moderator showed step or navigated)

Behavioral Friction Measures:
• Wrong Turns / Misclicks: _____  • System Errors: _____  • Repeated Clicks: _____
• Backtracks / Page Returns: _____ • Visible Hesitation / Pauses (>5s): _____

First Click / Initial Navigation Action:
Participant first clicked/tapped on: _________________________________________________

Think-Aloud Empirical Evidence:
┌────────────────────────┬──────────────────────────────────────────────────────────┐
│ Participant Said       │ "                                                      " │
│ (Verbatim quotation)   │                                                          │
├────────────────────────┼──────────────────────────────────────────────────────────┤
│ Participant Did        │                                                          │
│ (Observable action)    │                                                          │
├────────────────────────┼──────────────────────────────────────────────────────────┤
│ System Responded       │                                                          │
│ (UI reaction / state)  │                                                          │
├────────────────────────┼──────────────────────────────────────────────────────────┤
│ Observer Interpretation│                                                          │
│ (Mental model / issue) │                                                          │
└────────────────────────┴──────────────────────────────────────────────────────────┘
```

---

# Part E: Core Accommodation Tasks to Evaluate

### Task T1 — Homepage Discovery & Orientation
* **Goal:** Determine whether first-time users intuitively understand HomeSweet's value proposition and immediately know where to begin their search.
* **Scenario:** *"You are a university student looking for housing in Phnom Penh for the upcoming semester. You have just opened HomeSweet for the very first time. Explore the screen and tell me what you can do here."*
* **Observable Checkpoints:**
  - [ ] Correct starting point identified immediately (< 10 seconds)
  - [ ] Search / Discovery bar discovered without hesitation
  - [ ] Core purpose (student housing + verified roommates) understood
  - [ ] Global navigation / bottom dock understood
* **First Action Observed:** `________________________________________`
* **Single Ease Question (SEQ):** `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

### Task T2 — Find Suitable Accommodation (Search & Filtering)
* **Goal:** Test the utility and precision of property discovery, multi-criteria filtering, and listing comparison.
* **Scenario:** *"Find a furnished accommodation near your university with a monthly budget under $350 that has verified landlord status."*
* **Observable Checkpoints:**
  - [ ] Search input activated
  - [ ] Budget / Price range filter adjusted correctly
  - [ ] University / Location filter applied (e.g., Toul Kork, BKK1, Sen Sok)
  - [ ] Verification filter badge noticed and toggled
  - [ ] Multiple property cards compared (photo swipe / map toggle)
  - [ ] At least one suitable property identified matching all criteria
* **Friction Points Observed:** `________________________________________`
* **Single Ease Question (SEQ):** `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

### Task T3 — Property Decision & Information Comprehension
* **Goal:** Determine if the property detail page provides all necessary decision-making information and whether key safety/rule elements are noticed.
* **Scenario:** *"You are considering renting this specific unit. Review this property and explain whether it fits your lifestyle, what rules apply, and how safe you feel about it."*
* **Observable Checkpoints (Information Discovered Naturally):**
  - [ ] Monthly rent and deposit terms
  - [ ] Exact location and neighbourhood
  - [ ] Campus proximity / estimated commute time
  - [ ] Facilities & amenities (Wi-Fi, AC, kitchen, generator)
  - [ ] Availability date
  - [ ] Property rules (curfew, pets, smoking, guests)
  - [ ] Landlord verification badge and credentials
  - [ ] Safety and building security features
* **Information Expected But Could NOT Find:**
  `________________________________________________________________________________`
* **Single Ease Question (SEQ):** `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part F: Dedicated Trust & Fraud Evaluation

*HomeSweet implements anti-scam indicators, verified landlord credentials, and warning mechanisms. This dimension evaluates whether users detect and act upon trust cues.*

### Controlled Comparative Scenario
*Present the participant with two contrasting property listings: Listing A (Fully Verified, complete lease terms, verified landlord badge) and Listing B (Suspiciously low price, missing verification badge, unverified host).*

**Participant Decision Checkpoints:**
- [ ] Correctly identifies the safer listing without moderator prompts
- [ ] Actively notices the "Verified Landlord / Verified Property" badge
- [ ] Notices warning / risk disclaimers on unverified listings
- [ ] Accurately explains what the verification status means
- [ ] Can locate the "Report Listing / Flag Fraud" action
- [ ] Understands what occurs after submitting a report

### Quantitative Trust Rating
> **"How confident would you feel contacting this property owner or paying a deposit?"**
```
1 — Not confident at all   [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5   5 — Extremely confident
```

### Qualitative Trust Reasoning
*Record verbatim response:*
> **"What specific elements on the screen made you trust or distrust this listing?"**  
> `________________________________________________________________________________`  
> `________________________________________________________________________________`  

*SEQ (Trust & Safety Journey):* `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part G: Roommate Matching Evaluation

*Roommate matching is HomeSweet's core differentiator. This section evaluates feature discoverability, algorithm explainability, and perceived compatibility.*

### Task G1 — Discover & Review Roommate Profiles
* **Scenario:** *"You want to split rent by sharing an apartment. Use HomeSweet to find a compatible roommate who shares your study habits and sleep schedule."*
* **Observable Checkpoints:**
  - [ ] Roommate Matching feature discovered independently from navigation
  - [ ] Preference questionnaire / lifestyle filters understood
  - [ ] Recommended match cards inspected
  - [ ] Compatibility percentage score noticed
  - [ ] Key match factors (cleanliness, sleep schedule, study noise) understood
  - [ ] Suitable roommate candidate identified

### Matching Algorithm Comprehension & Explainability
*Ask the participant immediately after they review a profile:*

1. **"What do you think this compatibility percentage (e.g. 88% Match) actually means?"**  
   *Verbatim:* `____________________________________________________________________`

2. **"Why do you think HomeSweet recommended this specific person to you?"**  
   *Verbatim:* `____________________________________________________________________`

3. **Matching Confidence Rating:**
   > "How confident are you in this recommendation?"  
   ```
   1 — Not confident at all   [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5   5 — Extremely confident
   ```

4. **Explainability Assessment:**
   > "Is there enough clear information on the screen for you to understand WHY this person was recommended?"  
   - [ ] Yes, completely clear
   - [ ] Partially clear
   - [ ] No, unclear / black box
   *Missing Information Noted:* `____________________________________________________`

*SEQ (Find Roommate):* `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part H: Match Request & Chat Unlock (Consent Model)

*HomeSweet requires mutual consent before opening direct private messaging to prevent unsolicited harassment.*

### Funnel Progression Under Evaluation
$$\text{Discover Roommate} \longrightarrow \text{Review Profile} \longrightarrow \text{Send Request} \longrightarrow \text{Mutual Acceptance} \longrightarrow \text{Chat Unlocked}$$

### Observable Checkpoints:
- [ ] "Request Roommate / Connect" action discovered
- [ ] Purpose and implications of sending a request understood
- [ ] Mutual consent requirement recognized (both parties must agree)
- [ ] Restriction on direct messaging before mutual acceptance understood
- [ ] Next system state (pending acceptance notification) understood

### Mental Model Diagnostic Probe:
> **"Why do you think HomeSweet does not allow immediate direct messaging before a request is accepted?"**  
*Verbatim:* `____________________________________________________________________`  
*(Evaluator Note: If the participant cites safety, privacy, boundary protection, or anti-harassment, the system mental model is successfully communicated).*

*SEQ (Match & Chat Funnel):* `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part I: Identity Verification Evaluation (KYC Subsystem)

> [!CAUTION]
> **Ethical Testing Safeguard:** Usability testing must NEVER require participants to submit genuine sensitive government identification cards or personal biometric descriptors. Always provide test participants with standardized synthetic demo ID cards and pre-configured test profiles.

### Stage I1 — National ID Card Upload
* **Observable Checkpoints:**
  - [ ] Accepted identification types (National ID, Passport) understood
  - [ ] Photo quality requirements (glare-free, 4 corners visible) understood
  - [ ] Card crop / alignment tool operated successfully
  - [ ] Simulated validation error understood (e.g., blurry image prompt)
  - [ ] Error successfully recovered from
  - [ ] Purpose of government ID collection understood
* **Diagnostic Verbal Probes:**
  - *"Why do you think HomeSweet is asking for your ID?"*  
    `____________________________________________________________________________`
  - *"What do you believe happens to your ID document and data after verification is complete?"*  
    `____________________________________________________________________________`

---

### Stage I2 — Face Match (Biometric Selfie Comparison)
* **Observable Checkpoints:**
  - [ ] Camera hardware permission prompt understood and accepted
  - [ ] Oval positioning and face alignment guidelines followed
  - [ ] Live neural processing state visible and recognized
  - [ ] Match confirmation / confidence feedback understood
  - [ ] Recovery options clear if face does not align
* **Diagnostic Verbal Probe:**
  - *"What do you think the system is comparing your live face against right now?"*  
    `____________________________________________________________________________`

---

### Stage I3 — Active Liveness Verification Scan
* **Observable Checkpoints:**
  - [ ] Purpose of active liveness test understood
  - [ ] Guided motion prompts (e.g., blink, turn head, smile) executed
  - [ ] Progress indicators and scanning feedback noticed
  - [ ] Success state / verification badge unlocked clear
  - [ ] Retry mechanism intuitive if liveness check expires
* **Diagnostic Verbal Probe:**
  - *"Why do you think HomeSweet requires this live movement check in addition to a photo?"*  
    `____________________________________________________________________________`  
    *(Observer Note: If the user cannot explain it, flag for UX enhancement: "This confirms you are physically present and not an uploaded photograph").*

*SEQ (Identity Verification Flow):* `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part J: Identity Verification Privacy & Trust Dynamics

*Measure whether the KYC verification process builds student confidence or triggers privacy anxiety.*

### Before vs. After Trust & Comfort Measurement
1. **Before Starting Verification:**  
   > "How comfortable do you feel providing your identity documents to HomeSweet?"  
   ```
   1 — Extremely uncomfortable   [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5   5 — Completely comfortable
   ```

2. **After Completing Verification:**  
   > "Now that you have completed the process, how comfortable do you feel?"  
   ```
   1 — Extremely uncomfortable   [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5   5 — Completely comfortable
   ```

3. **Privacy Assurance Probe:**  
   > **"What specific guarantees, security badges, or explanations would you need to see before trusting an app like HomeSweet with your real government ID?"**  
   *Verbatim:* `________________________________________________________________`  
   `____________________________________________________________________________`  

---

# Part K: Rental Application & System Feedback

* **Goal:** Evaluate the formal rental booking request flow and verify visibility of system status.
* **Scenario:** *"You have chosen your apartment. Complete and submit the rental application to the landlord."*
* **Observable Checkpoints:**
  - [ ] "Apply Now / Rent House" call-to-action located
  - [ ] Application prerequisites (dates, lease duration, occupants) recognized
  - [ ] Form input validation and error states understood
  - [ ] Submission trigger executed
  - [ ] Confirmation screen / modal clearly noticed
  - [ ] Next expected steps (landlord review window) understood
* **System Status Confirmation Probe:**
  > *"Do you believe your rental application has been successfully submitted?"*  
  - [ ] Yes, definitely
  - [ ] No
  - [ ] Unsure / Confused
* **Grounding Evidence:**  
  > *"What specific elements on the screen made you think that?"*  
  `________________________________________________________________________________`

*SEQ (Rental Application):* `[ 1 | 2 | 3 | 4 | 5 | 6 | 7 ]`

---

# Part L: Controlled Error Recovery Test

*To measure real usability resilience, deliberately introduce ONE controlled operational disturbance during the session.*

### Error Condition Injected:
- [ ] Required form field omitted
- [ ] Invalid phone / date formatting
- [ ] Simulated upload failure (file too large)
- [ ] Network interruption simulation
- [ ] Listing temporarily unavailable

### Observable Error Recovery Metrics:
- [ ] Error message noticed immediately (< 5s)
- [ ] Plain-language error text understood without technical confusion
- [ ] Root cause identified correctly by participant
- [ ] Appropriate corrective action attempted autonomously
- [ ] Successfully recovered from error without page refresh
- [ ] Moderator assistance required: `[ ] 0 (None)  [ ] 1 (Prompt)  [ ] 2 (Hint)  [ ] 3 (Direct)`

### Quantitative Recovery Duration:
$$\text{Error Displayed} \longrightarrow \text{Successful Resolution}: \mathbf{\_\_\_\_\_\_\_\_} \text{ seconds}$$

### Qualitative Diagnostic Probe:
> **"In your own words, what just happened and why did the screen show that message?"**  
*Verbatim:* `____________________________________________________________________`  

---

# Part M: Application Status Tracking

* **Goal:** Evaluate whether users can independently locate, interpret, and track pending applications.
* **Scenario:** *"Two days have passed since you applied. Check the current status of your rental application."*
* **Observable Checkpoints:**
  - [ ] Status dashboard / notifications area located
  - [ ] Current application state (`Under Review`, `Approved`, `Deposit Required`) identified
  - [ ] Next required action understood
  - [ ] Notification timestamps and landlord notes clear
* **Diagnostic Verbal Probe:**
  > **"Explain what this application status means in your own words. What are you waiting for, and what happens next?"**  
  *Verbatim:* `____________________________________________________________________`  

---

# Part N: Master Single Ease Question (SEQ) Scorecard

*Administered immediately after each corresponding task: "Overall, how difficult or easy was this task to complete?" (1 = Very Difficult, 7 = Very Easy).*

| Task Code | Major Task Description | SEQ Score (1–7) | Observable Friction / Hesitation Notes |
| :---: | :--- | :---: | :--- |
| **T1** | Homepage Discovery & Navigation | `___ / 7` | |
| **T2** | Search, Filters & Listing Comparison | `___ / 7` | |
| **T3** | Property Decision & Rule Comprehension | `___ / 7` | |
| **TF** | Fraud Detection & Safety Evaluation | `___ / 7` | |
| **G1** | Find Compatible Roommate | `___ / 7` | |
| **H1** | Roommate Match Request & Chat Unlock | `___ / 7` | |
| **I1-3**| Biometric Identity Verification | `___ / 7` | |
| **K1** | Rental Application & Status Confirmation | `___ / 7` | |
| **L1** | Error Encounter & Recovery | `___ / 7` | |

$$\text{Participant Average Task Ease (Mean SEQ)} = \mathbf{\_\_\_.\_} \text{ / 7}$$

---

# Part O: Independent Heuristic Evaluation Worksheet

> [!IMPORTANT]
> **Heuristic Integrity Rule:** Conduct this expert heuristic review **PRIOR** to and **SEPARATELY** from participant testing. Do not force evaluators to artificially find one problem per heuristic. Document only genuine violations with observable consequences.

### Evaluator Defect Tracking Log
*Reference Heuristics: Nielsen's 10 Usability Heuristics + Domain-Specific Trust, Privacy & Student Safety.*

| Defect ID | Screen / Component | Heuristic Violated | Concrete Evidence & UI State | User Consequence | Severity (0–4) | Recommended Fix |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **H01** | `PropertyDetailView` | Visibility of System Status | No clear confirmation after bookmarking property | User clicks button multiple times | **2** | Add animated toast alert & active state icon |
| **H02** | `RoommateMatchView` | Match Between System & Real World | "Compatibility: 91%" has no explanation tooltip | User distrusts algorithmic score | **3** | Add breakdown modal (Study, Sleep, Noise) |
| **H03** | `IdUploadStep` | Error Prevention & Privacy | Missing encryption explanation near file dropzone | User fears identity theft & hesitates | **4** | Add bank-grade security badge & auto-delete notice |
| **H04** | `ChatView` | Flexibility & Efficiency | Contact list does not display read receipts | User cannot tell if landlord read message | **1** | Add double-check delivery indicator |
| **H05** | | | | | | |
| **H06** | | | | | | |
| **H07** | | | | | | |

---

# Part P: Five-Tier Usability & Safety Severity Rating Scale

*HomeSweet implements a calibrated 0–4 severity scale. In student housing, privacy and safety defects can reach Critical severity even if the user technically completes the task.*

```
┌───────┬─────────────────┬────────────────────────────────────────────────────────────────────────┐
│ Grade │ Severity Label  │ Operational Definition & Impact Threshold                              │
├───────┼─────────────────┼────────────────────────────────────────────────────────────────────────┤
│   0   │ Not an Issue    │ An observation or aesthetic opinion; does not hinder task performance.  │
│   1   │ Cosmetic        │ Minor aesthetic or phrasing issue; easily resolved; no delay.          │
│   2   │ Minor           │ Causes slight hesitation, misclick, or temporary confusion; completes. │
│   3   │ Major           │ Substantial error, severe cognitive load, requires hint or near abandon.│
│   4   │ Critical        │ Prevents task completion OR exposes user privacy, trust, or safety.    │
└───────┴─────────────────┴────────────────────────────────────────────────────────────────────────┘
```

> [!CAUTION]
> **Safety & Privacy Escalation Rule:** Any defect that could cause a student to pay an unverified landlord, share government identity data over unencrypted channels, or unintentionally reveal personal contact info to an unverified user MUST be classified as **Severity 4 (Critical)** regardless of path success.

---

# Part Q: Post-Test Standardized Usability & Perception Battery

### 1. Perceived Experience & Trust Dimensions (1–5 Likert)
```
Overall Ease of Use:               [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
System Confidence:                 [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
Trust in Landlords / Listings:     [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
Personal Safety Feeling:           [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
Roommate Matching Usefulness:      [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
Property Information Completeness: [ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5
```

### 2. Net Adoption Likelihood (0–10 Scale)
> **"How likely are you to recommend or use HomeSweet for your next student accommodation search?"**
```
0   1   2   3   4   5   6   7   8   9   10
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
(0–6: Detractor | 7–8: Passive | 9–10: Promoter)
```

---

### 3. System Usability Scale (SUS) Standard 10-Item Battery
*Scores: 1 = Strongly Disagree, 5 = Strongly Agree.*

| # | Standardized Question Item | 1 (SD) | 2 | 3 | 4 | 5 (SA) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | I think that I would like to use HomeSweet frequently. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **2** | I found HomeSweet unnecessarily complex. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **3** | I thought HomeSweet was easy to use. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **4** | I think that I would need technical support to use HomeSweet. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **5** | I found the various functions in HomeSweet were well integrated. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **6** | I thought there was too much inconsistency in HomeSweet. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **7** | I would imagine most students would learn HomeSweet very quickly. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **8** | I found HomeSweet very cumbersome / awkward to use. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **9** | I felt very confident using HomeSweet. | [ ] | [ ] | [ ] | [ ] | [ ] |
| **10**| I needed to learn a lot of things before I could get going. | [ ] | [ ] | [ ] | [ ] | [ ] |

$$\text{Calculated Composite SUS Score} = \mathbf{\_\_\_\_.\_} \text{ / 100}$$

---

# Part R: In-Depth Semi-Structured Debrief Interview

*Conduct verbally immediately following SUS administration. Record answers verbatim.*

1. **What was the easiest or most intuitive part of using HomeSweet?**  
   `____________________________________________________________________________`
2. **What was the most difficult, frustrating, or confusing part?**  
   `____________________________________________________________________________`
3. **At what specific point during the test did you feel most uncertain or hesitant?**  
   `____________________________________________________________________________`
4. **Was there any information you actively searched for but could not find?**  
   `____________________________________________________________________________`
5. **What specific elements made you feel you could trust HomeSweet?**  
   `____________________________________________________________________________`
6. **Was there anything that caused you to distrust the app or any listings?**  
   `____________________________________________________________________________`
7. **How did you feel about the three-step identity verification requirement?**  
   `____________________________________________________________________________`
8. **Did the roommate recommendation score make sense to you? What did it convey?**  
   `____________________________________________________________________________`
9. **What additional information would make you feel confident actually moving in with someone recommended by the app?**  
   `____________________________________________________________________________`
10. **If both HomeSweet and traditional Facebook/Telegram groups were available today, which would you use first to find housing, and why?**  
    `____________________________________________________________________________`
11. **What would HomeSweet need to improve or add for you to switch completely away from social media housing groups?**  
    `____________________________________________________________________________`
12. **If you had the power to change ONE single thing about HomeSweet before it launches to students, what would it be?**  
    `____________________________________________________________________________`

---

# Part S: Observer's Critical Incident Log

*Record all unexpected anomalies, breakthrough moments, severe errors, or significant expressions of delight or distress in real time.*

| Time Code | Screen / Feature | What Happened (Observable Event) | User Quotation (Verbatim) | Impact on Journey | Severity (0–4) |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `14:12` | `IdUploadStep` | Crop box jumped when dragging on mobile | "Wait, it cut off my expiration date!" | Had to cancel and re-upload twice | **2** |
| `14:26` | `RoommateMatchView`| Tapped "Request Roommate" button | "Does this send them my phone number?" | User hesitated 15s before tapping | **3** |
| | | | | | |
| | | | | | |
| | | | | | |

---

# Part T: Participant-Level Usability Summary

*To be completed by the moderator and observer immediately after the participant departs.*

### Quantitative Performance Scorecard
* **Tasks Completed Independently (Success):** `___ / 9`
* **Tasks with Minor Assistance (Partial):** `___ / 9`
* **Tasks Failed or Abandoned:** `___ / 9`
* **Overall Completion Rate:** `____%`
* **Average Task Ease (Mean SEQ):** `____ / 7`
* **Total Behavioral Errors Logged:** `____`
* **Tasks Requiring Direct Assistance:** `________________________________________`

### Qualitative Synthesis
* **Critical Usability Blockers Observed:**  
  `____________________________________________________________________________`
* **Strongest Positive User Finding / Delight Point:**  
  `____________________________________________________________________________`
* **Biggest Usability Barrier Encountered:**  
  `____________________________________________________________________________`
* **Biggest Trust or Privacy Concern Expressed:**  
  `____________________________________________________________________________`
* **Most Impactful Verbatim Quotation of the Session:**  
  > *"________________________________________________________________________"*

---

# Part U: Cross-Participant Findings & Engineering Backlog Prioritization

*Consolidate across the complete cohort of participants (e.g. $N = 10$).*

### Usability Defect & Opportunity Matrix
*Priorities:*
* **P0 — Critical Release Blocker:** Security, privacy vulnerability, or complete block on core journey. Must be resolved before launch.
* **P1 — High Priority:** Major usability defect causing high friction, severe confusion, or repeated errors.
* **P2 — Medium Improvement:** Minor friction, awkward layout, or secondary path difficulty.
* **P3 — Low Enhancement:** Cosmetic polish, text refinement, or nice-to-have suggestion.

| Issue ID | Feature Area | Empirical Usability Finding | Affected Users | Frequency (%) | Direct Behavioral Evidence | Severity (0–4) | Concrete Design Recommendation | Release Priority |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: | :--- | :---: |
| **U01** | Verification | Users confused about data retention policy | `7 / 10` | 70% | 7 participants asked if landlord sees full national ID | **4** | Add prominent "Encrypted & Never Shared with Landlords" pill badge | **P0** |
| **U02** | Roommate Match | Compatibility percentage perceived as arbitrary | `6 / 10` | 60% | Participants wondered how 85% is calculated | **3** | Introduce matching dimension tags (e.g., "Both night owls", "Non-smoker") | **P1** |
| **U03** | Search Filters | Price slider difficult to set exact value on mobile | `4 / 10` | 40% | Multiple repeated thumb taps to set $300 | **2** | Add quick-select preset chips ($150, $250, $350, $500+) | **P2** |
| **U04** | Property Details | Curfew / building rules buried at bottom | `5 / 10` | 50% | Students missed 11 PM gate lock rule | **3** | Move House Rules into dedicated card above landlord bio | **P1** |
| **U05** | Chat View | Unclear why messaging is locked before request | `5 / 10` | 50% | Tapped message icon, thought app was broken | **3** | Replace disabled icon with "Mutual Consent Required" explanation tooltip | **P1** |
| **U06** | | | ` / 10` | % | | | | |
| **U07** | | | ` / 10` | % | | | | |

---

# Part V: Final Prototype Usability Evaluation Summary & Release Gate

*The executive sign-off artifact synthesizing all empirical usability, trust, and safety evidence.*

### 1. Executive Performance Metrics Dashboard
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. Overall Task Effectiveness (Success Rate):                  _______ %    │
│ 2. Task Efficiency (Median Completion Time across tasks):      _______ sec  │
│ 3. Mean Single Ease Question (SEQ) Score:                      _______ / 7  │
│ 4. Standardized System Usability Scale (SUS) Score:            _______ / 100│
│ 5. Post-Test Trust Rating:                                     _______ / 5  │
│ 6. Personal Safety & Privacy Confidence:                       _______ / 5  │
│ 7. Net Adoption Likelihood:                                    _______ / 10 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. Categorized Defect Inventory
* **Critical Issues (Severity 4 / P0):** `____` *(Must be 0 for launch approval)*
* **Major Issues (Severity 3 / P1):** `____`
* **Minor Issues (Severity 2 / P2):** `____`
* **Cosmetic Issues (Severity 1 / P3):** `____`

### 3. Empirical Release Decision
*Select the authoritative evaluation outcome based on empirical thresholds:*

- [ ] **READY FOR PRODUCTION RELEASE**  
  *Criteria:* Overall Task Success $\ge 85\%$, SUS Score $\ge 75$, 0 P0 defects, all core journeys autonomously completed.
- [ ] **READY WITH MINOR NON-BLOCKING REVISIONS**  
  *Criteria:* 0 P0 defects; remaining defects are P2/P3; workaround available for minor friction.
- [ ] **RETEST REQUIRED AFTER P1 RESOLUTION**  
  *Criteria:* One or more P1 defects impair critical user journeys (e.g. roommate matching, search filtering, or booking submission).
- [ ] **NOT READY FOR RELEASE — CRITICAL SAFETY / PRIVACY BLOCKER**  
  *Criteria:* One or more P0 defects exist (e.g. identity privacy vulnerability, fraud exposure, or unrecoverable verification crash).

### Formal Justification & Sign-Off Statement
`____________________________________________________________________________________`  
`____________________________________________________________________________________`  
`____________________________________________________________________________________`  

**Lead UX Researcher / Evaluator:** `_________________________` **Date:** `__________`  
**Product Lead / Project Sponsor:** `_________________________` **Date:** `__________`  
