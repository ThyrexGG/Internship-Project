# HomeSweet

> Real Estate & Rental Living Platform for Phnom Penh, Cambodia.

HomeSweet combines residential property discovery, tenant rental applications, roommate matchmaking, digital lease agreements, ABA KHQR payments, real-time messaging, social friend connections, 360-degree virtual property tours, and AI-powered biometric identity verification into a unified experience.

---

## Documentation

For the complete technical architecture, data model schemas, route maps, security policies, and engineering workflow SOPs, refer to the primary specification:

**[Project State & Architecture Documentation](docs/PROJECT_STATE.md)**

---

## Quick Start

### 1. Prerequisites
- Node.js: v16.x - v20.x
- npm: v8.x+
- Environment: configure `.env` with your Firebase project credentials (see `.env.example`).

### 2. Installation
```powershell
npm install
# Note for Windows PowerShell users: use npm.cmd
npm.cmd install
```

### 3. Local Development (HTTPS)
```powershell
npm run serve
# Or on Windows PowerShell:
npm.cmd run serve
```
The local development server runs at `https://localhost:8080/`. HTTPS is enabled by default to allow WebRTC camera access for biometric KYC identity verification.

### 4. Quality & Build
```powershell
# Run linter (0 errors enforced)
npm.cmd run lint

# Compile production build
npm.cmd run build
```

---

## Key Features

- **Property Discovery & Search** - Filterable listings with an interactive map view.
- **360-Degree Virtual Tours** - Equirectangular panorama viewer for participating listings.
- **Rental Applications & Digital Lease Agreements** - End-to-end booking and lease lifecycle.
- **ABA KHQR & Card Payments** - Rent and deposit checkout with PDF receipts.
- **Real-Time Messaging** - Firestore-backed direct chat between residents and landlords.
- **Friend Connections** - Send/accept/decline friend requests between residents.
- **Roommate Matching** - Swipeable compatibility-based roommate discovery.
- **Biometric KYC Verification** - National ID capture, face match, and liveness detection.
- **Landlord Operations Console** - Listing management, bookings, and revenue dashboard.
- **Admin Management Console** - Platform-wide moderation, verification review, and oversight.

---

## Key Routes & Access

| Route | Description |
| :--- | :--- |
| `/home` | Resident discovery portal |
| `/search` | Map and listing search |
| `/property/:id` | Property detail, including 360-degree tour |
| `/property/:id/apply` | Rental application wizard |
| `/payment` | Payment and invoices |
| `/chat` | Real-time messaging |
| `/verify-account` | Biometric identity KYC |
| `/user-profile/:id` | Resident profile and friend connections |
| `/roommate-match` | Roommate compatibility discovery |
| `/landlord` | Landlord operations console |
| `/admin` | Admin management console (shortcut: `Ctrl + Shift + A`) |

---

## Security & Rules

- Firestore security rules: defined in `firestore.rules`
- Storage security rules: defined in `storage.rules`
- Deployment manifest: defined in `firebase.json`

For detailed technical specifications, see **[docs/PROJECT_STATE.md](docs/PROJECT_STATE.md)**.
