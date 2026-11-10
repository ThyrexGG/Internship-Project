/**
 * Central legal / data-protection configuration.
 * Keep the version string in sync with docs/legal/ when the policy text changes.
 */

export const LEGAL_VERSION = '2026-11-06-draft'
export const LEGAL_UPDATED = '6 November 2026'

/**
 * Identity-verification (KYC) mode, set with VUE_APP_KYC_MODE at build time.
 *
 *   off  - the verification flow is paused; nobody can submit anything.
 *   test - (default) the flow runs for usability testing only. The user must
 *          confirm they are using the synthetic demo ID, and the ID is never
 *          sent to a third-party OCR service.
 *   live - real identity checks with a real consent step. Do NOT use until the
 *          open items in docs/legal/01_DATA_PROTECTION_POLICY.md are closed.
 *
 * Any unrecognised value fails safe to 'off'.
 */
const RAW_KYC_MODE = String(process.env.VUE_APP_KYC_MODE || 'test').trim().toLowerCase()
export const KYC_MODE = ['off', 'test', 'live'].includes(RAW_KYC_MODE) ? RAW_KYC_MODE : 'off'

/** Build the consent record stored alongside an account or a KYC submission. */
export function buildConsentRecord(extra = {}) {
  return {
    version: LEGAL_VERSION,
    acceptedAt: new Date().toISOString(),
    ...extra
  }
}
