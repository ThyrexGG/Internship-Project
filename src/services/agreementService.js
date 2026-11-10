/**
 * HomeSweet Normalized Landlord-Tenant Agreement Architecture
 * Lifecycle: draft -> pending_landlord -> pending_tenant -> active -> completed (or cancelled)
 */

export const AGREEMENT_STATUS = Object.freeze({
  DRAFT: 'draft',
  PENDING_LANDLORD: 'pending_landlord',
  PENDING_TENANT: 'pending_tenant',
  ACTIVE: 'active',
  COMPLETED: 'completed',
  CANCELLED: 'cancelled'
})

export const VALID_AGREEMENT_TRANSITIONS = {
  [AGREEMENT_STATUS.DRAFT]: [AGREEMENT_STATUS.PENDING_LANDLORD, AGREEMENT_STATUS.CANCELLED],
  [AGREEMENT_STATUS.PENDING_LANDLORD]: [AGREEMENT_STATUS.PENDING_TENANT, AGREEMENT_STATUS.CANCELLED],
  [AGREEMENT_STATUS.PENDING_TENANT]: [AGREEMENT_STATUS.ACTIVE, AGREEMENT_STATUS.CANCELLED],
  [AGREEMENT_STATUS.ACTIVE]: [AGREEMENT_STATUS.COMPLETED, AGREEMENT_STATUS.CANCELLED],
  [AGREEMENT_STATUS.COMPLETED]: [],
  [AGREEMENT_STATUS.CANCELLED]: []
}

/**
 * Validates whether state transition is allowed by the lifecycle state machine
 */
export function canTransitionAgreement(currentStatus, nextStatus) {
  if (!currentStatus || !nextStatus) return false
  if (currentStatus === nextStatus) return true
  const allowedNext = VALID_AGREEMENT_TRANSITIONS[currentStatus] || []
  return allowedNext.includes(nextStatus)
}

/**
 * Factory for creating normalized agreement model
 */
export function createNormalizedAgreement(data = {}) {
  const now = new Date().toISOString()
  const status = data.status || AGREEMENT_STATUS.DRAFT
  // A signature is only recorded once the lifecycle has actually reached that stage.
  const landlordSigned = [AGREEMENT_STATUS.PENDING_TENANT, AGREEMENT_STATUS.ACTIVE, AGREEMENT_STATUS.COMPLETED].includes(status)
  const tenantSigned = [AGREEMENT_STATUS.ACTIVE, AGREEMENT_STATUS.COMPLETED].includes(status)
  return {
    id: data.id || `AGR-${Date.now().toString(36).toUpperCase()}`,
    code: data.code || `Agreement-${String(Math.floor(Math.random() * 900) + 100)}`,
    landlordId: data.landlordId || null,
    landlordName: data.landlordName || '',
    landlordEmail: data.landlordEmail || '',
    tenantId: data.tenantId || null,
    tenantName: data.tenantName || '',
    tenantEmail: data.tenantEmail || '',
    propertyId: data.propertyId || null,
    propertyName: data.propertyName || '',
    propertyAddress: data.propertyAddress || '',
    monthlyRent: Number(data.monthlyRent) || 200,
    depositAmount: Number(data.depositAmount) || 400,
    startDate: data.startDate || '2026-09-15',
    endDate: data.endDate || '2027-09-15',
    leaseDuration: data.leaseDuration || '12 months',
    paymentTerms: data.paymentTerms || 'Due on the 1st of every month via Bank Transfer/Bakong KHQR.',
    status,
    signatures: {
      landlordSignedAt: data.landlordSignedAt || (landlordSigned ? now : null),
      tenantSignedAt: data.tenantSignedAt || (tenantSigned ? now : null)
    },
    metadata: {
      occupants: data.occupants || 1,
      petsAllowed: data.petsAllowed || false,
      utilitiesIncluded: data.utilitiesIncluded || ['WiFi', 'Trash Collection']
    },
    createdAt: data.createdAt || now,
    updatedAt: now
  }
}

/**
 * Initial seed agreements for 15-user test cohort
 */
export const INITIAL_AGREEMENTS = [
  createNormalizedAgreement({
    id: 'AGR-001',
    code: 'Agreement-001',
    landlordName: 'Skystar Property Co.',
    tenantName: 'Alice Freeman',
    propertyName: 'Skystar Condo #105',
    monthlyRent: 200,
    status: AGREEMENT_STATUS.ACTIVE,
    startDate: '2026-08-01',
    endDate: '2027-08-01'
  }),
  createNormalizedAgreement({
    id: 'AGR-002',
    code: 'Agreement-002',
    landlordName: 'Skystar Property Co.',
    tenantName: 'Dara Sok',
    propertyName: 'Aurafa Condo #201',
    monthlyRent: 120,
    status: AGREEMENT_STATUS.ACTIVE,
    startDate: '2026-08-15',
    endDate: '2027-02-15'
  }),
  createNormalizedAgreement({
    id: 'AGR-003',
    code: 'Agreement-003',
    landlordName: 'Mekong Real Estate',
    tenantName: 'Alexandre Meyer',
    propertyName: 'High Dafa Residence #3B',
    monthlyRent: 230,
    status: AGREEMENT_STATUS.PENDING_TENANT,
    startDate: '2026-09-15',
    endDate: '2027-09-15'
  }),
  createNormalizedAgreement({
    id: 'AGR-004',
    code: 'Agreement-004',
    landlordName: 'Lotus Holdings',
    tenantName: 'Sophia Chea',
    propertyName: 'Lotus Residence #12A',
    monthlyRent: 145,
    status: AGREEMENT_STATUS.DRAFT,
    startDate: '2026-10-01',
    endDate: '2027-04-01'
  })
]
