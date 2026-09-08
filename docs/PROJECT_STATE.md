# HomeSweet — Project State & Architectural Blueprint
> **Document Version:** 1.0.0  
> **Status:** Production-Ready MVP  
> **Last Verified Date:** September 8, 2026  
> **Target Repository:** `ThyrexGG/Internship-Project` (Branch: `main`)  
> **Primary Authors & Maintainers:** HomeSweet Core Engineering Team

---

## Table of Contents
1. [Executive Overview & Platform Identity](#1-executive-overview--platform-identity)
2. [Technology Stack & Dependency Inventory](#2-technology-stack--dependency-inventory)
3. [Repository Directory & File Breakdown](#3-repository-directory--file-breakdown)
4. [Routing Architecture & Route Catalog](#4-routing-architecture--route-catalog)
5. [Core Application Modules & Component Deep-Dive](#5-core-application-modules--component-deep-dive)
   - 5.1 [Resident / Renter Subsystem](#51-resident--renter-subsystem)
   - 5.2 [Biometric Identity & KYC Verification Subsystem](#52-biometric-identity--kyc-verification-subsystem)
   - 5.3 [Landlord & Host Operations Portal](#53-landlord--host-operations-portal)
   - 5.4 [Administrative Management Console](#54-administrative-management-console)
   - 5.5 [Shared Components & Cross-Cutting Services](#55-shared-components--cross-cutting-services)
6. [Data Architecture & Firestore Schema Dictionary](#6-data-architecture--firestore-schema-dictionary)
7. [Security Architecture & Access Control Policies](#7-security-architecture--access-control-policies)
8. [Design System, Typography & CSS Architecture](#8-design-system-typography--css-architecture)
9. [Local Development, Build & Environment Configuration](#9-local-development-build--environment-configuration)
10. [Known Technical Limitations, Edge Cases & Roadmap](#10-known-technical-limitations-edge-cases--roadmap)
11. [Workflow Guidelines & Engineering SOPs](#11-workflow-guidelines--engineering-sops)

---

## 1. Executive Overview & Platform Identity

### 1.1 Purpose
**HomeSweet** is a full-stack, high-fidelity real estate and rental living platform tailored specifically for the Southeast Asian urban market, with initial primary focus on **Phnom Penh, Cambodia**. It unites property discovery, tenant rental applications, roommate matchmaking, digital lease agreements, ABA KHQR payments, and identity verification into a unified experience.

### 1.2 Core Personas & Roles
The platform is designed around three distinct user personas:
1. **Resident / Tenant (`role: 'resident'`):**
   - Discovers residential properties (condos, apartments, houses, studios) across Phnom Penh districts (Chroy Chongva, BKK1, Tonle Bassac, Sen Sok, Toul Kork, Chamkarmon, Daun Penh).
   - Submits formal rental applications with document uploads.
   - Finds and matches with compatible roommates via card-swiping interfaces.
   - Communicates in real-time with property managers and landlords.
   - Completes multi-step biometric identity verification (National ID + Face Matching + Liveness Scan).
   - Makes digital rent and deposit payments with automated PDF receipts.
2. **Landlord / Host (`role: 'landlord'`):**
   - Creates, edits, and manages property listings with geolocation auto-detection and Firebase Storage photo galleries.
   - Reviews and acts upon rental booking applications (Accept / Decline).
   - Inspects tenant identity verification records and chat histories.
   - Tracks rental revenue, invoices, and lease agreement states.
3. **Platform Administrator (`role: 'admin'`):**
   - Accesses a confidential administrative portal via hotkey (`Ctrl + Shift + A`) or secret PIN gate.
   - Audits KYC biometric verification submissions, inspecting user ID cards against live selfies with AI confidence scores, and approves or rejects applications.
   - Manages platform property inventories, moderates users, and audits digital lease contracts and payments.

### 1.3 Strict Terminology Standard
- **No "rentalus":** The platform strictly enforces standard real estate nomenclature. The term "rentalus" is completely prohibited and has been eliminated across all UI labels, code variables, and data structures in favor of **"Tenants"**, **"Residents"**, and **"Renters"**.

---

## 2. Technology Stack & Dependency Inventory

### 2.1 Core Framework & Tooling
| Component | Technology | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | Vue.js | `^3.2.13` | Reactive component architecture using Composition API (`<script setup>`) and Options API |
| **Routing** | Vue Router | `^4.6.4` | Single Page Application (SPA) HTML5 history routing and deep linking |
| **Build Tooling** | Vue CLI Service | `~5.0.0` | Webpack 5 bundling, Babel compilation, and local HTTPS dev server |
| **Linter & Quality** | ESLint + `plugin:vue` | `^7.32.0` / `^8.0.3` | Linting with `vue3-essential` and `eslint:recommended` rulesets |
| **Compiler** | Babel Core | `^7.12.16` | Modern ECMAScript transpilation |

### 2.2 Backend & Cloud Infrastructure
| Service | Provider / Library | Version | Role in Architecture |
| :--- | :--- | :--- | :--- |
| **Database** | Firebase Cloud Firestore | `^12.13.0` | Real-time NoSQL document store with live listeners (`onSnapshot`) |
| **Authentication** | Firebase Auth | `^12.13.0` | Email/Password auth, Google OAuth popup, auth token listener |
| **Cloud Storage** | Firebase Storage | `^12.13.0` | High-res property media, user avatars, and private KYC documents |
| **Media Service** | Cloudinary (`@cloudinary/vue`) | `^1.13.4` | Legacy cloud media delivery and URL generation |

### 2.3 Specialized Client-Side Libraries
| Library | Version | Exact Purpose |
| :--- | :--- | :--- |
| **`face-api.js`** | `^0.22.2` | Client-side TensorFlow.js neural networks for face detection (SSD MobileNet V1), 68 facial landmarks, and 128D facial descriptors for biometric verification. Models are hosted locally in `/public/models/`. |
| **`cropperjs`** | `^2.1.1` | Client-side interactive canvas image cropper for national ID card and passport alignment before OCR/biometric comparison. |
| **`html2pdf.js`** | `^0.14.0` | High-fidelity client-side PDF document compiler for rental lease agreements, official invoices, and receipt downloads. |
| **`core-js`** | `^3.8.3` | Modular standard library polyfills for cross-browser ECMAScript runtime support. |

---

## 3. Repository Directory & File Breakdown

```
Internship-Project-main/
├── .env                              # Local environment variables (Firebase config & keys)
├── .env.example                      # Template environment variable definitions
├── .gitignore                        # Git ignore specifications (node_modules, dist, .env)
├── babel.config.js                   # Babel transpilation preset config
├── cors.json                         # Firebase Storage CORS configuration for web uploads
├── firebase.json                     # Firebase deployment manifest linking rules
├── firestore.indexes.json            # Firestore composite index declarations
├── firestore.rules                   # Production Cloud Firestore security & authorization rules
├── storage.rules                     # Production Firebase Storage access control policies
├── jsconfig.json                     # IDE JavaScript project path configuration
├── package.json                      # Project manifest, script commands, and dependencies
├── package-lock.json                 # Pinned dependency tree lockfile
├── vue.config.js                     # Vue CLI & Webpack config (HTTPS dev server, polyfills)
├── README.md                         # Project overview and pointer to documentation
│
├── public/                           # Static assets served directly at root
│   ├── favicon.svg                   # Brand vector favicon
│   ├── favicon.ico                   # Fallback ICO favicon
│   ├── index.html                    # Root HTML document mounting #app with Google Fonts
│   ├── logo.png                      # Primary HomeSweet brand mark
│   ├── hero_sunset_villa.jpeg        # High-resolution hero imagery
│   ├── skystar_bedroom.jpeg          # Architectural property visual
│   ├── examples/                     # KYC validation test examples (id_good, selfie_good, etc.)
│   ├── homesweet/                    # Standardized high-res property catalog photography
│   └── models/                       # face-api.js pre-trained neural network weights & manifests
│       ├── ssd_mobilenetv1_model-*   # Face detection weights
│       ├── face_landmark_68_model-*  # 68-point landmark detector weights
│       └── face_recognition_model-*  # 128D facial recognition descriptor weights
│
├── src/                              # Source application code
│   ├── App.vue                       # Root component, global CSS design tokens, admin hotkey listener
│   ├── main.js                       # Vue 3 application bootstrapper & router mounting
│   ├── router.js                     # Route table definitions, history mode, path mappings
│   ├── store.js                      # Centralized reactive state: property listings & search filter state
│   ├── firebase.js                   # Firebase app initialization and service exports (db, auth, storage)
│   │
│   ├── assets/                       # Bundled static assets (hero banners, deck illustrations)
│   │
│   ├── components/                   # Reusable UI components
│   │   ├── GlobalFooter.vue          # Universal application footer with legal & site navigation
│   │   ├── NotificationDropdown.vue  # Real-time bell dropdown with category filters & unread badges
│   │   ├── PropertyImage.vue         # Unified image component with shimmer skeleton & fallback
│   │   └── verification/             # Identity verification multi-step wizard components
│   │       ├── ProfileStep.vue       # Step 1: Personal profile, occupation & lifestyle habits
│   │       ├── IdUploadStep.vue      # Step 2: National ID / Passport capture & interactive crop
│   │       ├── FaceMatchStep.vue     # Step 3: Biometric face matching with face-api.js
│   │       ├── LivenessScanStep.vue  # Step 4: Real-time webcam liveness challenge (turn/blink)
│   │       └── SuccessStep.vue       # Step 5: Submission confirmation & pending review state
│   │
│   ├── services/                     # Cross-cutting business logic & service engines
│   │   ├── agreementService.js       # Agreement lifecycle state machine & seed contracts
│   │   └── locationService.js        # Geolocation, OpenStreetMap reverse geocoding & district resolver
│   │
│   └── views/                        # Route page views
│       ├── normal/                   # Resident & Renter Views
│       │   ├── HomeView.vue          # Core resident shell: Home, Favorites, Feeds, Messages, Settings
│       │   ├── LoginView.vue         # Email/Google Auth, role selection, multi-step password recovery
│       │   ├── SetupAccountView.vue  # Post-signup redirect wrapper mounting VerifyAccountView
│       │   ├── SearchResultsView.vue # Split-screen search & interactive vector map engine
│       │   ├── PropertyDetailView.vue# Property presentation, gallery, amenities & action CTAs
│       │   ├── RentalApplicationView.vue # 4-step rental application wizard with Firestore persistence
│       │   ├── PaymentView.vue       # Payment checkout, ABA Bakong KHQR, invoice & PDF receipts
│       │   ├── ChatView.vue          # Two-column real-time Firestore messaging & attachments
│       │   ├── VerifyAccountView.vue # KYC stepper container with split hero & dev bypass bar
│       │   ├── UserProfileView.vue   # Resident profile, friend connection & messaging entry
│       │   ├── FindRoommateView.vue  # Property-specific roommate application & split calculator
│       │   └── RoommateMatchView.vue # Swipeable roommate deck with compatibility metrics
│       │
│       ├── landlord/                 # Landlord & Property Host Views
│       │   ├── LandlordNotification.vue # Landlord Operations Hub: listing creation, booking manager
│       │   └── LandlordProfileView.vue  # Public landlord credentials, ratings, listings & direct chat
│       │
│       └── admin/                    # Administrative Views
│           └── AdminPortalView.vue   # Master Admin Console: audits, KYC review, listings & agreements
```

---

## 4. Routing Architecture & Route Catalog

The routing system is configured via `src/router.js` using `createWebHistory()`. Below is the complete catalog of application routes:

| Route Path | View / Component | Name | Access Level | Description & Query / Params |
| :--- | :--- | :--- | :--- | :--- |
| `/` | Redirects to `/login` | — | Public | Root redirection |
| `/login` | `LoginView.vue` | — | Public | Dual-tab login & registration, password recovery |
| `/home` | `HomeView.vue` | — | Authenticated / Guest | Primary discovery feed, favorites, social feeds, settings |
| `/search` | `SearchResultsView.vue` | `SearchResults` | Public | Split-screen listing search with interactive vector map |
| `/property/:id` | `PropertyDetailView.vue` | `PropertyDetail` | Public | Comprehensive property detail view with photo gallery |
| `/property/:id/apply` | `RentalApplicationView.vue`| `RentalApplication` | Resident | 4-stage rental application form & lease agreement init |
| `/property/:id/payment`| `PaymentView.vue` | `PropertyPayment` | Resident | Property-linked checkout & rent/deposit settlement |
| `/payment` | `PaymentView.vue` | `Payment` | Resident | General checkout portal (supports `?id=<propId>`) |
| `/checkout` | Redirects to `/payment` | — | Resident | Convenience alias for payment checkout |
| `/property/:id/roommate`| `FindRoommateView.vue` | `FindRoommate` | Resident | Roommate application form for a specific property |
| `/roommate-match` | `RoommateMatchView.vue` | `RoommateMatch` | Resident | Tinder-style swipeable roommate compatibility discovery |
| `/chat` | `ChatView.vue` | `Chat` | Authenticated | Live 2-column messaging interface with real-time sync |
| `/messages` | Redirects to `/chat` | — | Authenticated | Convenience alias for messaging |
| `/verify-account` | `VerifyAccountView.vue` | — | Authenticated | 5-step biometric KYC account verification wizard |
| `/setup-account` | `SetupAccountView.vue` | — | Authenticated | Post-registration verification onboarding wrapper |
| `/user-profile/:id` | `UserProfileView.vue` | `UserProfile` | Public / Resident | Resident public profile view with friend connect action |
| `/landlord-profile/:id`| `LandlordProfileView.vue` | `LandlordProfile` | Public | Public landlord verification badges, reviews & listings |
| `/landlord` | `LandlordNotification.vue` | — | Landlord / Host | Landlord operations dashboard & listing creation console |
| `/admin` | `AdminPortalView.vue` | `AdminPortal` | Secret / Admin | Administrative management console (Protected by PIN gate) |
| `/admin/login` | Redirects to `/admin` | — | Public | Convenience alias for admin entry |
| `/admin/verifications` | `AdminPortalView.vue` | `AdminVerifications`| Admin | Direct deep link to verification requests auditing tab |

### 4.1 Global Hotkey & Admin Access
To access the administrative console discreetly from any screen in the application, a global keyboard listener is mounted in `src/App.vue`:
- **Shortcut:** `Ctrl + Shift + A` (Windows / Linux) or `Cmd + Shift + A` (macOS).
- **Behavior:** Immediately redirects the browser to `/admin`, opening the PIN-authenticated admin security gate.

---

## 5. Core Application Modules & Component Deep-Dive

### 5.1 Resident / Renter Subsystem

#### 1. `HomeView.vue` (Core Shell)
- **Navigation Tabs:** Managed via `activeTab` ref (`home`, `favorite`, `feeds`, `messages`, `settings`), persisted across browser navigation via `sessionStorage.getItem('homeActiveTab')`.
- **Top Navigation Bar:**
  - Dynamic brand mark with logo.
  - Search trigger input that routes directly to `/search`.
  - **"Become a Host"** CTA button that switches directly to the Host Upgrade onboarding view.
  - Compact **`NotificationDropdown.vue`** bell icon with live unread counter.
  - Profile menu button that navigates directly to user settings.
- **Home Tab:** Filter pills (All, Condo, Apartment, House, Studio), property search input, featured listings carousel, responsive property grid, and bookmark toggling.
- **Favorite Tab:** Displays saved properties saved by the user with one-click navigation to property details.
- **Feeds Tab:** Community social wall where residents and landlords post updates, queries, and lifestyle stories with photo upload integration, like counts, and real-time comment threads.
- **Messages Tab:** Integrated chat launcher routing seamlessly to `/chat`.
- **Settings Tab:** Deep settings panel structured with sub-tabs:
  - `profile`: Edit first/last name, phone, bio, avatar upload to Firebase Storage.
  - `security`: Change password, toggle 2FA, session review.
  - `verification`: Account KYC status banner displaying real-time verification state (`unverified`, `pending`, `verified`, or `rejected`) with direct link to `/verify-account`.
  - `upgrade`: Resident-to-Host upgrade request form writing to `landlord_applications`.
- **Floating Bottom Nav Bar:** Capsule navigation bar supporting mobile swipe/tap interactions with active pill indicators and automatic scrolling visibility behaviors.

#### 2. `SearchResultsView.vue` (Map & Discovery Engine)
- **Layout Architecture:** Split-screen layout inspired by Airbnb and Plum Guide. Left column renders property card stream; right column renders an interactive visual map.
- **Dual-Mode Map Engine:**
  - **Google Maps Canvas:** Automatically binds to `window.google.maps` if an API key is supplied.
  - **Interactive Vector Fallback:** When offline or when no Google Maps API key is configured, the view renders a proprietary SVG vector map of Phnom Penh. It accurately projects real-world latitude/longitude coordinates (`11.5400`–`11.5950` N, `104.8850`–`104.9350` E) onto a 2D canvas with interactive price pins, river geometries (Mekong / Tonle Sap), district boundary labels, and marker click synchronizations.
- **Filter & Sort Popover:** Real-time filtering by property type, price range slider ($50–$610+), bedroom and bathroom counts, amenities checklist, and rental term period (Short-term / Long-term).
- **Fullscreen Mode:** Toggle button expands the map to 100% viewport width with floating listings overlay.

#### 3. `PropertyDetailView.vue` (Listing Showcase)
- **Gallery:** Hero display with horizontal thumbnail scroller and interactive index switching.
- **Specifications:** Displays price/month, location badge, bedroom/bathroom count, square footage, and compatibility match score.
- **Amenities Grid:** Wifi, kitchen, pool, air conditioning, parking, laundry with standardized SVG icons.
- **Tenants Section:** Shows active verified residents living in the building with privacy-compliant avatars.
- **Reviews & Ratings:** Aggregated rating score with breakdown bar indicators and resident review testimonials.
- **Conversion Actions:** Direct action buttons to "Apply to Rent" (`/property/:id/apply`), "Find Roommate" (`/property/:id/roommate`), or "Pay Rent" (`/property/:id/payment`).

#### 4. `RentalApplicationView.vue` (Lease Application Wizard)
- **Step 1: Application Form:** Applicant identification, employment info, proposed lease duration (6, 12, 18, 24 months), desired move-in date, and legal declarations.
- **Step 2: Upload Documents:** File upload inputs for Government ID / Passport, Proof of Employment / Income, and Bank Statements.
- **Step 3: Review & Terms:** Real-time calculation of monthly rent, security deposit (typically 2x monthly rent), estimated utilities, and VAT.
- **Step 4: Confirmation & Submission:** Persists the complete application record to Firestore `rental_applications` collection with status `'pending'`, generates an automated system notification for the landlord, and returns an application tracking reference ID.

#### 5. `PaymentView.vue` (Checkout & KHQR Settlement)
- **Checkout Stages:** Step 1: Payment Method Selection -> Step 2: Billing Information -> Step 3: Transaction Processing & Confirmation -> Step 4: Digital Receipt Modal.
- **Supported Payment Gateways:**
  - **ABA PAY / Bakong KHQR:** Generates a standard Cambodian National Bank KHQR code for instant mobile banking checkout.
  - **Credit / Debit Cards:** Mastercard and Visa card entry with client-side Luhn validation formatting.
  - **Bank Transfer / Wing:** Manual account reference instructions.
- **Invoice Breakdown:** Base rental charge, security deposit line-item, promotional discount code calculation, 10% VAT calculation, and grand total.
- **Receipt Generation:** Integrated `html2pdf.js` engine renders and exports a pixel-perfect, branded PDF invoice document for the resident's tax and lease records.
- **Firestore Recording:** Commits the transaction to the `payments` collection with timestamps, user ID, landlord ID, and settlement status.

#### 6. `ChatView.vue` (Real-Time Communication Hub)
- **Interface:** Split two-column layout matching modern messaging platforms (Telegram / WhatsApp).
- **Conversation List:** Real-time list of active chat threads with unread message badges, avatar status rings, and timestamp formatting.
- **Live Synchronization:** Listens to Firestore `messages` and `chats/{chatId}/messages` using `onSnapshot()` for instant bidirectional communication.
- **Media & Document Sharing:** Integrated file inputs supporting image attachments (JPEG, PNG) and PDF document transfers.
- **In-Chat Search:** Instant client-side text filtering to search through conversation message history.

---

### 5.2 Biometric Identity & KYC Verification Subsystem

The identity verification pipeline (`src/views/normal/VerifyAccountView.vue` and `src/components/verification/`) establishes a fraud-resistant user base through automated client-side neural networks.

```
[Step 1: Profile Details] ──> [Step 2: National ID Upload] ──> [Step 3: Biometric Face Match]
                                                                        │
[Step 5: Pending Review] <── [Step 4: Interactive Liveness Scan] <──────┘
```

#### Step 1: Profile & Lifestyle Information (`ProfileStep.vue`)
- Gathers applicant legal identity details: First Name, Last Name, Phone Number, Date of Birth, Gender, Nationality, and Emergency Contact.
- Captures lifestyle habits (e.g., Early Bird, Night Owl, Pet Friendly, Non-Smoker) that populate the user's roommate matching profile.

#### Step 2: Document Capture & Cropping (`IdUploadStep.vue`)
- Supports upload or webcam capture of Cambodian National ID Cards or Passports.
- Integrates `cropperjs` to allow users to align, rotate, and crop document borders cleanly.
- Simulates automated MRZ/document data extraction (National ID number, issue date, nationality).

#### Step 3: Neural Face Matching (`FaceMatchStep.vue`)
- Initializes three neural models from `face-api.js`:
  1. `ssdMobilenetv1`: Detects facial bounding boxes with high confidence.
  2. `faceLandmark68Net`: Extracts 68 facial landmark coordinates (eyes, nose, mouth contour).
  3. `faceRecognitionNet`: Computes a 128-dimensional biometric descriptor vector.
- Compares the facial descriptor extracted from the ID document against a captured user selfie.
- Computes Euclidean distance and converts it to a percentage match score (e.g. 98.4%).
- Enforces an automated threshold requirement (> 80%) before allowing progression.

#### Step 4: Interactive Liveness Challenge (`LivenessScanStep.vue`)
- Activates the device webcam in real-time within a guide oval.
- Issues dynamic, anti-spoofing micro-challenges to detect photo/screen replay fraud:
  - Detection of head rotation (Left / Right) by tracking nose bridge displacement relative to eye corners.
  - Eye blink detection via eye aspect ratio (EAR) analysis.
- Confirms biological presence before enabling final submission.

#### Step 5: Submission & Admin Review State (`SuccessStep.vue`)
- **Strict Security Guard:** The client-side wizard **never** self-grants `verificationStatus = 'verified'`.
- Submits the complete payload (ID photo URL, live selfie URL, face match score, liveness result) to the `verification_requests` Firestore collection with status `'pending'`.
- Updates the user's record in `users/{userId}` to `verificationStatus: 'pending'`.
- Dispatches a high-priority notification to the Admin Portal.
- Renders an informative pending review status card with estimated completion time (typically 24 hours).

---

### 5.3 Landlord & Host Operations Portal

#### 1. `LandlordNotification.vue` (Operations Dashboard)
- **Listing Management:**
  - View all managed properties with status indicators (Active, Occupied, Under Maintenance).
  - Add New Property Modal with:
    - Title, price per month, deposit amount, category (Condo, Apartment, House, Studio).
    - **One-Click Geolocation:** Integrates `locationService.js` to read GPS coordinates from the browser, perform reverse geocoding via OpenStreetMap Nominatim, and auto-populate district and street address.
    - **AI Description Assistant:** Automatically drafts appealing, professional property descriptions based on selected amenities.
    - **Photo Gallery Upload:** Direct file-to-Firebase-Storage pipeline with image preview and delete actions.
    - Spec attributes: Bedroom count, bathroom count, square meters, amenities checklist.
- **Booking & Rental Applications:**
  - Real-time stream of incoming tenant applications.
  - Review applicant profile, uploaded financial documents, and verification badges.
  - **One-Click Actions:** Accept application (transitions to agreement creation), Decline application, or Open direct chat with applicant.
  - Export invoice and booking summaries as PDF via `html2pdf.js`.

#### 2. `LandlordProfileView.vue` (Public Landlord Portfolio)
- Public profile page accessible by prospective tenants.
- Displays landlord credentials: Email Verified, Phone Verified, Government ID Verified, Property Ownership Title Verified.
- Overall rating summary, responsiveness metrics (e.g., "Responds within 1 hour"), and tenant reviews.
- Portfolio catalog displaying all listings operated by this landlord.
- Embedded direct chat tab for immediate tenant inquiries.

---

### 5.4 Administrative Management Console

#### `AdminPortalView.vue`
- **Security Access Control:**
  - Protected by a client-side PIN gate (`123456` or `admin@homesweet.com`) and session authorization stored in `sessionStorage.getItem('adminAuth')`.
  - Backend Firestore access is strictly validated via `firestore.rules` checking Firebase Auth token claims or admin email lists.
- **Console Navigation Tabs:**
  1. **Dashboard Tab:** High-level platform KPIs: Total Properties, Active Tenants, Monthly Revenue, Pending Verifications, and Recent System Activity Feed.
  2. **Verifications Tab:** Dedicated audit queue for identity submissions. Admins inspect ID card uploads side-by-side with webcam selfies, review AI face match scores and liveness flags, and execute single-click **Approve** or **Reject** decisions (with customizable rejection feedback sent to the resident).
  3. **Houses / Properties Tab:** Catalog of all active listings across Phnom Penh with ability to edit, feature, or remove non-compliant listings.
  4. **Agreements Tab:** Digital lease agreement manager powered by `agreementService.js` displaying contract status (`draft`, `pending_landlord`, `pending_tenant`, `active`, `completed`, `cancelled`).
  5. **Users Tab:** Complete resident and landlord directory with role management, status toggling, and verification badges.

---

### 5.5 Shared Components & Cross-Cutting Services

#### 1. `NotificationDropdown.vue`
- Compact, unobtrusive bell dropdown positioned in the top navigation bar.
- Replaces bulky fullscreen notification views with an interactive popdown.
- Features:
  - Category filter pills (`All`, `Bookings`, `Payments`).
  - Real-time unread count pill badge (`99+` formatting).
  - Single-click **"Mark all read"** action updating both local state and Firestore documents.
  - Keyboard accessible (`Escape` to close) and click-outside dismissal.

#### 2. `PropertyImage.vue`
- Standardized image display component applied across all property cards and detail views.
- **Skeleton Shimmer Wave:** Displays a smooth CSS gradient wave animation while the remote image loads.
- **Graceful Error Handling:** Automatically intercepts broken URLs or network errors and seamlessly substitutes a high-resolution local fallback asset (`/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg`).
- **Interactive Depth:** Applies subtle gradient vignetting and smooth scale transitions on hover.

#### 3. `agreementService.js`
- Enforces a formal **Finite State Machine (FSM)** for digital lease agreements:
  ```
  DRAFT ──> PENDING_LANDLORD ──> PENDING_TENANT ──> ACTIVE ──> COMPLETED
    │             │                    │              │
    └─────────────┴────────────────────┴──────────────┴───────> CANCELLED
  ```
- Exposes validation helper `canTransitionAgreement(currentStatus, nextStatus)` preventing illegal lifecycle leaps.
- Generates normalized agreement data structures with signatures, terms, and payment schedules.

#### 4. `locationService.js`
- High-resilience geolocation service:
  1. Requests device GPS coordinates via `navigator.geolocation`.
  2. Attempts reverse geocoding via Google Maps Geocoder if initialized.
  3. Falls back to **OpenStreetMap Nominatim** API with strict 4-second timeout.
  4. Falls back to **Offline Centroid Distance Matching** against known Phnom Penh district coordinates (Chroy Chongva, BKK1, Tonle Bassac, Sen Sok, Toul Kork, Chamkarmon, Daun Penh).

---

## 6. Data Architecture & Firestore Schema Dictionary

### 6.1 Collection: `users`
Represents registered resident and landlord accounts.
```typescript
interface UserDocument {
  uid: string;                       // Firebase Auth UID (Document ID)
  email: string;                     // User email address
  firstName: string;                 // Given name
  lastName: string;                  // Family name
  role: 'resident' | 'landlord' | 'admin'; // Authorization role
  verificationStatus: 'unverified' | 'pending' | 'verified' | 'rejected';
  verificationRequestId?: string;    // Reference to verification_requests doc
  idNumber?: string;                 // National ID or Passport number
  phoneNumber?: string;              // Contact number
  profilePicUrl?: string;            // Cloud Storage URL
  bio?: string;                      // Personal introduction
  nationality?: string;              // e.g. "Cambodian", "French"
  hobbies?: string[];                // Lifestyle tags: ['Early bird', 'No smoking']
  friends?: string[];                // Array of connected user UIDs
  createdAt: string | Timestamp;     // ISO timestamp or Firestore Timestamp
  updatedAt?: string | Timestamp;
}
```

### 6.2 Collection: `properties`
Represents residential properties listed on the platform.
```typescript
interface PropertyDocument {
  id: string | number;               // Unique property identifier
  ownerId: string;                   // Landlord Firebase Auth UID
  userId?: string;                   // Alias for ownerId compatibility
  name: string;                      // Listing title (e.g. "Skystar Condo Unit 105")
  type: 'condo' | 'apartment' | 'house' | 'studio';
  location: string;                  // District & city string (e.g. "Chroy Chongva, Phnom Penh")
  lat: number;                       // Geolocation latitude (e.g. 11.5900)
  lng: number;                       // Geolocation longitude (e.g. 104.9300)
  price: number;                     // Monthly rent in USD ($)
  deposit?: number;                  // Security deposit in USD ($)
  period: 'Short-term' | 'Long-term';// Minimum lease requirement
  beds: number;                      // Number of bedrooms
  baths: number;                     // Number of bathrooms
  sqft: number;                      // Living space in square meters / sqft
  match?: number;                    // Algorithmic compatibility rating (%)
  rating: number;                    // Average review score (e.g. 4.9)
  amenities: string[];               // ['wifi', 'kitchen', 'ac', 'pool', 'parking', 'washer']
  images: string[];                  // Array of image URLs (Cloud Storage or local)
  description?: string;              // Extended promotional listing text
  status?: 'active' | 'rented' | 'maintenance';
  createdAt: string | Timestamp;
}
```

### 6.3 Collection: `verification_requests`
Audit records for biometric KYC submissions.
```typescript
interface VerificationRequestDocument {
  id?: string;                       // Auto-generated Firestore Document ID
  userId: string;                    // Applicant UID
  userName: string;                  // Applicant full name
  userEmail: string;                 // Applicant email
  userAvatar?: string;               // Existing avatar URL
  idType: 'National ID' | 'Passport' | 'Driver License';
  idNumber: string;                  // Document identification number
  idPreviewUrl: string;              // Cropped document image URL
  selfieUrl: string;                 // Live webcam selfie image URL
  faceMatchScore: number;            // AI similarity percentage (e.g. 98.4)
  livenessPassed: boolean;           // Anti-spoofing challenge flag
  status: 'pending' | 'approved' | 'rejected';
  rejectionReason?: string;          // Admin feedback if rejected
  reviewedAt?: string | null;        // Timestamp when audited by admin
  reviewedBy?: string | null;        // Admin UID or identifier
  nationality: string;               // e.g. "Cambodian"
  sex: 'Male' | 'Female' | 'Other';
  submittedAt: string;               // ISO submission timestamp
}
```

### 6.4 Collection: `agreements`
Formal digital lease agreements binding landlords and tenants.
```typescript
interface AgreementDocument {
  id: string;                        // Agreement ID (e.g. "AGR-001")
  code: string;                      // Display code (e.g. "Agreement-001")
  landlordId: string;                // Landlord UID
  landlordName: string;              // Landlord full name or company
  landlordEmail: string;             // Landlord contact email
  tenantId: string;                  // Tenant UID
  tenantName: string;                // Tenant full name
  tenantEmail: string;               // Tenant contact email
  propertyId: number | string;       // Associated property ID
  propertyName: string;              // Property title
  propertyAddress: string;           // Physical location
  monthlyRent: number;               // Rent amount in USD ($)
  depositAmount: number;             // Deposit amount in USD ($)
  startDate: string;                 // Lease start date (YYYY-MM-DD)
  endDate: string;                   // Lease end date (YYYY-MM-DD)
  leaseDuration: string;             // e.g. "12 months"
  paymentTerms: string;              // Payment stipulations
  status: 'draft' | 'pending_landlord' | 'pending_tenant' | 'active' | 'completed' | 'cancelled';
  signatures: {
    landlordSignedAt?: string | null;
    tenantSignedAt?: string | null;
  };
  metadata?: {
    occupants: number;
    petsAllowed: boolean;
    utilitiesIncluded: string[];
  };
  createdAt: string;
  updatedAt: string;
}
```

### 6.5 Collection: `payments`
Digital transaction records and settled invoices.
```typescript
interface PaymentDocument {
  id?: string;                       // Document ID
  userId: string;                    // Payer UID
  landlordId?: string;               // Payee Landlord UID
  propertyId: number | string;       // Associated property ID
  amount: number;                    // Paid amount in USD ($)
  planName?: string;                 // e.g. "Standard Pro" or "Monthly Rent"
  method: 'khqr' | 'mastercard' | 'visa' | 'bank_transfer' | 'wing';
  status: 'completed' | 'pending' | 'failed';
  invoiceNumber?: string;            // e.g. "INV-2026-8942"
  createdAt: string | Timestamp;     // Transaction creation timestamp
}
```

### 6.6 Collection: `rental_applications`
Prospective tenant booking submissions.
```typescript
interface RentalApplicationDocument {
  applicantId: string;               // Tenant UID
  landlordId?: string;               // Landlord UID
  propertyId: number | string;       // Property ID
  fullName: string;                  // Applicant name
  email: string;                     // Applicant email
  phone: string;                     // Applicant phone
  leaseDuration: number;             // Months (6, 12, 18, 24)
  moveInDate: string;                // Target move-in date
  monthlyRent: number;               // Agreed monthly rent
  depositAmount: number;             // Required deposit
  documents: {
    idCardUrl?: string;
    employmentProofUrl?: string;
    bankStatementUrl?: string;
  };
  status: 'pending' | 'accepted' | 'declined';
  createdAt: string;
}
```

### 6.7 Collection: `notifications`
Real-time system and transactional alerts.
```typescript
interface NotificationDocument {
  userId?: string;                   // Target user UID (null if broadcast/admin)
  targetRole?: 'admin' | 'landlord' | 'resident';
  type: 'booking' | 'payment' | 'system';
  title: string;                     // Alert headline
  desc: string;                      // Detailed message content
  roomName?: string;                 // Associated property name
  amount?: string;                   // Financial reference
  unread: boolean;                   // Read status indicator
  time?: string;                     // Display timestamp (e.g. "12m ago")
  createdAt: string | Timestamp;     // ISO timestamp
}
```

### 6.8 Collection: `messages` & `chats/{chatId}/messages`
Bidirectional communication channels.
```typescript
interface MessageDocument {
  senderId: string;                  // Sender UID
  receiverId?: string;               // Direct receiver UID
  recipientId?: string;              // Receiver UID alias
  content: string;                   // Text content
  mediaUrl?: string;                 // Attached image URL
  documentUrl?: string;              // Attached PDF document URL
  timestamp: string | Timestamp;     // Server timestamp
}
```

---

## 7. Security Architecture & Access Control Policies

The application adheres to a zero-trust model implemented directly inside `firestore.rules` and `storage.rules`.

### 7.1 Cloud Firestore Security Rules (`firestore.rules`)
- **Authentication Check (`isAuthenticated()`):** Rejects all unauthenticated attempts to read or mutate non-public collections.
- **Admin Privileges (`isAdmin()`):** Evaluates whether the request token contains `admin == true`, matches official admin emails (`admin@homesweet.com`, `thyrexgg@gmail.com`), or possesses a verified `role == 'admin'` in `users/{uid}`.
- **Privilege Escalation Prevention:**
  - Standard users are strictly blocked from writing `role: 'admin'` or setting `verificationStatus: 'verified'`. Only administrative roles can approve KYC transitions.
- **Ownership Verification:**
  - Property listings can only be updated or deleted by their registered `ownerId` / `userId` or a platform admin.
  - Users can only read and mutate their own profile documents (`isOwner(userId)`).
- **Communication Privacy:**
  - Direct and threaded messages are strictly restricted to the conversation participants. Unrelated users cannot read or inject messages.
- **Application & Payment Immutability:**
  - Rental applications can only be created by the applicant.
  - Payment records can be created by authenticated users for their own transactions, but can only be modified or deleted by administrators for reconciliation.

### 7.2 Cloud Storage Security Rules (`storage.rules`)
- **Profile Avatars (`/users/{userId}/*`):** Publicly readable; writable only by the account owner; max file size 5MB; image MIME type enforced.
- **Property Media (`/property_images/*`):** Publicly readable; writable by authenticated landlords; max file size 10MB; image MIME type enforced.
- **Social Feed Images (`/feed_images/*`):** Publicly readable; writable by authenticated authors; max file size 10MB; image MIME type enforced.
- **Confidential KYC Documents (`/verification_docs/{userId}/*`):**
  - **Strict Privacy:** Under no circumstances are national ID cards or verification selfies publicly accessible.
  - Accessible strictly and exclusively by the applicant (`request.auth.uid == userId`) and authorized platform administrators (`isAdmin()`).
  - Max file size 10MB; restricted to image and PDF formats.
- **Agreements & Contracts (`/agreement_docs/{agreementId}/*`):** Authenticated access; max file size 15MB.

---

## 8. Design System, Typography & CSS Architecture

The application design reflects an editorial, luxury residential visual aesthetic using vanilla CSS custom properties declared in `src/App.vue`.

### 8.1 CSS Token Dictionary
```css
:root {
  /* Color Palette */
  --color-primary: #5C4E4E;          /* Signature warm charcoal taupe */
  --color-primary-hover: #473B3B;    /* Darkened hover state */
  --color-primary-dark: #2A2421;     /* Deep espresso accent */
  --color-primary-light: #F2EDE9;    /* Warm pearl background fill */
  --color-text-primary: #2A2421;     /* Primary header & body text */
  --color-text-secondary: #5C4E4E;   /* Secondary descriptive text */
  --color-text-muted: #8C7E7E;       /* Subtle meta labels & captions */
  --color-bg-canvas: #faf8f5;        /* Platform background canvas */
  --color-bg-surface: #ffffff;       /* Pure white card surface */
  --color-border: #ede8e3;           /* Standard container border */
  --color-border-subtle: #f2eee9;    /* Hairline divider */
  
  /* Status Indicators */
  --color-success: #10B981;          /* Verified green */
  --color-success-bg: #ECFDF5;
  --color-warning: #F59E0B;          /* Pending review amber */
  --color-warning-bg: #FEF3C7;
  --color-error: #EF4444;            /* Rejection red */
  --color-error-bg: #FEE2E2;
  --color-info: #3B82F6;             /* Information blue */
  --color-info-bg: #EFF6FF;

  /* Spacing Scale */
  --spacing-2xs: 2px;
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  --spacing-3xl: 64px;
  --container-max: 1280px;
  --container-gutter: 24px;

  /* Corner Radii */
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;
  --radius-2xl: 24px;
  --radius-pill: 50px;

  /* Elevation Shadows */
  --shadow-sm: 0 1px 3px rgba(92, 78, 78, 0.05);
  --shadow-md: 0 4px 16px rgba(92, 78, 78, 0.06);
  --shadow-lg: 0 10px 30px rgba(92, 78, 78, 0.08);
  --shadow-dropdown: 0 12px 36px rgba(42, 36, 33, 0.12), 0 4px 12px rgba(42, 36, 33, 0.06);

  /* Typography */
  --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-serif: 'DM Serif Display', Georgia, serif;

  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-normal: 0.25s ease;
}
```

### 8.2 Typography Hierarchy
- **Editorial Headlines (`--font-serif`):** Used on hero sections, marketing callouts, and landing titles to create a warm, inviting residential atmosphere.
- **Functional Interface (`--font-body`):** High-legibility geometric sans-serif applied to navigation items, listing specs, form fields, and data tables.

---

## 9. Local Development, Build & Environment Configuration

### 9.1 Prerequisites
- **Node.js:** v16.x to v20.x recommended.
- **npm:** v8.x or higher.
- **Operating System:** Windows, macOS, or Linux.

### 9.2 Environment Configuration (`.env`)
Create a `.env` file at the root of the project with the following keys:
```ini
VUE_APP_FIREBASE_API_KEY=your_firebase_api_key
VUE_APP_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VUE_APP_FIREBASE_PROJECT_ID=your_project_id
VUE_APP_FIREBASE_STORAGE_BUCKET=your_project.firebasestorage.app
VUE_APP_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
VUE_APP_FIREBASE_APP_ID=your_app_id
```

### 9.3 Windows PowerShell Commands
On Windows environments, use `npm.cmd` rather than `npm` to respect execution policies:
```powershell
# 1. Install dependencies
npm.cmd install

# 2. Start local HTTPS development server
npm.cmd run serve
# Local URL: https://localhost:8080/
# Note: HTTPS is enabled by default in vue.config.js to allow WebRTC camera access!

# 3. Execute linter checks (0 warnings / 0 errors required)
npm.cmd run lint

# 4. Compile optimized production bundle
npm.cmd run build
```

---

## 10. Known Technical Limitations, Edge Cases & Roadmap

### 10.1 Current Status & Fallbacks
1. **Google Maps Integration:**
   - *Status:* Works out-of-the-box without requiring an API key via the built-in **Interactive Vector Map Canvas**.
   - *Enhancement:* When a production Google Maps API key with Geocoding and Places API is injected into `index.html`, the system automatically activates Google Maps rendering.
2. **Webcam Permissions:**
   - *Status:* WebRTC `getUserMedia()` requires a secure context (`https://` or `localhost`). `vue.config.js` is pre-configured with `https: true`.
   - *Fallback:* If a user denies camera access during ID upload or selfie capture, the UI automatically provides a manual photo file upload fallback.
3. **face-api.js Model Serving:**
   - Neural network weights are committed directly to `/public/models/`. This eliminates external CDN dependencies and guarantees that facial verification operates even on offline or low-bandwidth networks.
4. **Admin Portal Authentication:**
   - *Current State:* PIN gate (`123456` or `admin@homesweet.com`) validated in frontend UI, coupled with email checks in `firestore.rules`.
   - *Recommended Future Enhancement:* Implement Firebase Custom Claims via Cloud Functions (`admin: true`) for enterprise-tier token claims.

---

## 11. Workflow Guidelines & Engineering SOPs

### 11.1 Code Contributions & Standards
1. **Component Scoping:** All Vue components must utilize `<style scoped>` to prevent CSS selector leakage, referencing centralized tokens from `:root`.
2. **ESLint Cleanliness:** Run `npm.cmd run lint` prior to every commit. Zero lint errors are tolerated on `main`.
3. **State Management:**
   - Use `store.js` for universal cross-view state (`properties`, `globalSearchQuery`, `globalFilterState`).
   - Use scoped Composition API state for view-specific lifecycles.
4. **Git Commit Conventions:**
   - Format: `<type>(<scope>): <short summary>`
   - Types: `feat`, `fix`, `refactor`, `style`, `docs`, `chore`, `perf`.
   - Example: `feat(verification): add liveness head turn challenge to kyc flow`

---
*HomeSweet Platform Architecture & State Documentation — Maintained by the Core Team.*
