# Legal & data-protection pack

Drafted 6 November 2026. **None of this is legal advice and none of it has been reviewed by a lawyer.** Open questions for counsel are in `01_DATA_PROTECTION_POLICY.md` §10.

| File | What it is |
|---|---|
| `01_DATA_PROTECTION_POLICY.md` | Internal policy: the KYC rule, data inventory, retention, procedures, and the blockers before real ID checks can be enabled |
| `02_LEASE_AGREEMENT_REVIEW.md` | Review of the lease/rental flow: false claims fixed, 12 findings, what a real agreement would need |
| `../feco301/05_CLIENT_REVIEW_NOTE.md` | Message to send a candidate client, plus the record sheet |
| `../feco301/06_TEAM_CONTRACT.md` | Manifesto and 6-member contract (fill names, hours, signatures) |

**User-facing text lives in the app, not here:**
- Privacy Policy and Terms of Use: `src/views/normal/LegalView.vue` (routes `/privacy`, `/terms`)
- Version string and KYC mode: `src/config/legal.js` — bump `LEGAL_VERSION` / `LEGAL_UPDATED` whenever that text changes, so stored consent records show which version a user accepted.

**KYC mode** (`VUE_APP_KYC_MODE` in `.env`): `off` | `test` (default) | `live`. Keep `off` on production except during scheduled test sessions. Do not use `live` until the blockers in the data-protection policy §9 are closed.
