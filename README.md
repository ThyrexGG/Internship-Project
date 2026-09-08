# HomeSweet

> Modern Real Estate & Rental Living Platform for Phnom Penh, Cambodia.

HomeSweet combines residential property discovery, tenant rental applications, roommate matchmaking, digital lease agreements, ABA KHQR payments, and AI-powered biometric identity verification into a unified experience.

---

## 📖 Master Documentation
For the complete, down-to-the-bare-bones technical architecture, data model schemas, route maps, security policies, and engineering workflow SOPs, please refer to the primary specification:

👉 **[Master Project State & Architecture Documentation](docs/PROJECT_STATE.md)**

---

## 🚀 Quick Start

### 1. Prerequisites
- **Node.js**: v16.x – v20.x
- **npm**: v8.x+
- **Environment**: Configure `.env` with your Firebase project credentials (see `.env.example`).

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
# Run Linter (0 errors enforced)
npm.cmd run lint

# Compile production build
npm.cmd run build
```

---

## 🗺️ Key Routes & Access
- **Resident Discovery Portal:** `/home`
- **Map & Listing Search:** `/search`
- **Rental Application Wizard:** `/property/:id/apply`
- **Payment & Invoices:** `/payment`
- **Real-Time Messaging:** `/chat`
- **Biometric Identity KYC:** `/verify-account`
- **Landlord Operations:** `/landlord`
- **Admin Management Console:** `/admin` (Shortcut: `Ctrl + Shift + A`)

---

## 🔒 Security & Rules
- **Firestore Security Rules:** Defined in `firestore.rules`
- **Storage Security Rules:** Defined in `storage.rules`
- **Deployment Manifest:** Defined in `firebase.json`

For detailed technical specifications, inspect **[docs/PROJECT_STATE.md](docs/PROJECT_STATE.md)**.
