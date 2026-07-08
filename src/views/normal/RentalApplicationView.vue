<template>
  <div class="app-page">

    <!-- ── HERO (always visible) ── -->
    <header class="app-hero">
      <div class="app-top-bar">
        <button class="back-btn" @click="handleBack" aria-label="Go back">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
        </button>
      </div>
      <div class="hero-img-wrap">
        <img :src="property.images[0]" alt="Property" class="hero-img" />
        <div class="hero-badge">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
          </svg>
          Rent House
        </div>
      </div>
    </header>

    <!-- ── BODY ── -->
    <main class="app-body" v-if="currentStep < 4">

      <!-- Title Row -->
      <div class="title-row">
        <div class="title-left">
          <h1 class="form-title">Rental Application Form</h1>
          <p class="form-subtitle">{{ property.name }}</p>
        </div>
        <div class="title-right">
          <span class="price-val">${{ property.price }}</span>
          <span class="price-period">/ monthly</span>
        </div>
      </div>

      <!-- Step Progress Bar -->
      <div class="stepper">
        <div
          v-for="(label, i) in stepLabels"
          :key="i"
          class="step-item"
          :class="{ active: currentStep === i + 1, done: currentStep > i + 1 }"
        >
          <div class="step-circle">
            <svg v-if="currentStep > i + 1" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M20 6L9 17l-5-5"/>
            </svg>
            <span v-else>{{ i + 1 }}</span>
          </div>
          <span class="step-label">{{ label }}</span>
          <div v-if="i < stepLabels.length - 1" class="step-connector"></div>
        </div>
      </div>

      <!-- ══════════════════════════════════════
           STEP 1 — Application Form
      ══════════════════════════════════════ -->
      <template v-if="currentStep === 1">
        <!-- House Information -->
        <section class="section">
          <h2 class="section-heading">House Information</h2>
          <p class="sub-heading">House detail</p>
          <div class="icons-row">
            <div class="d-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>
                <path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>
              </svg>
              <span>{{ property.pax || '2/4 pax' }}</span>
            </div>
            <div class="d-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
              </svg>
              <span>{{ property.beds }} bed</span>
            </div>
            <div class="d-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>
              </svg>
              <span>{{ property.baths }} bath</span>
            </div>
            <div class="d-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18M15 3v18"/>
              </svg>
              <span>1 int</span>
            </div>
            <div class="d-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2"/>
              </svg>
              <span>{{ property.sqft }}m²</span>
            </div>
          </div>
        </section>

        <!-- Form Card -->
        <div class="card form-card">
          <!-- Lease Duration -->
          <div class="field-group">
            <label class="field-label">Preferred Lease Duration</label>
            <div class="pill-row">
              <button
                v-for="d in leaseDurations" :key="d"
                class="pill-btn"
                :class="{ active: form.leaseDuration === d }"
                @click="form.leaseDuration = d"
              >{{ d }} month</button>
            </div>
          </div>

          <div class="field-row">
            <div class="field-group">
              <label class="field-label">Total Occupants</label>
              <input class="field-input" v-model="form.occupants" placeholder="e.g. 2 people" />
            </div>
            <div class="field-group">
              <label class="field-label">Pets</label>
              <input class="field-input" v-model="form.pets" placeholder="e.g. 1 cats" />
            </div>
            <div class="field-group">
              <label class="field-label">Previous Rental Experience</label>
              <input class="field-input" v-model="form.rentalExp" placeholder="First time renting" />
            </div>
          </div>

          <div class="field-row">
            <div class="field-group">
              <label class="field-label">Preferred move-in date</label>
              <input class="field-input" type="date" v-model="form.moveInDate" />
              <p class="field-hint">This is your preferred lease length. The landlord may counter-propose a different term.</p>
            </div>
            <div class="field-group">
              <label class="field-label">Message to LandLord</label>
              <textarea class="field-textarea" v-model="form.message"
                placeholder="Introduce yourself – tell the landlord a bit about you, your lifestyle and why this property is a good fit."
              ></textarea>
            </div>
            <div class="field-group">
              <label class="field-label">Monthly Income (USD)</label>
              <input class="field-input" v-model="form.income" placeholder="e.g. 2500" />
              <p class="field-hint">Income information is used only for landlord review and admin verification. No credit check is performed at this stage.</p>
            </div>
          </div>
        </div>

        <div class="nav-row">
          <span></span>
          <button class="btn-next" @click="goToStep(2)">Next — Upload Documents</button>
        </div>
      </template>

      <!-- ══════════════════════════════════════
           STEP 2 — Upload Documents
      ══════════════════════════════════════ -->
      <template v-if="currentStep === 2">
        <div class="card doc-card">
          <p class="doc-title">Supporting Document <span class="doc-note">(optional but speeds up approval)</span></p>
          <div class="doc-upload-row">
            <label class="upload-zone">
              <input type="file" accept=".jpg,.png,.pdf" @change="handleFile($event, 'id')" hidden />
              <div class="upload-inner">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="1.5">
                  <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/>
                </svg>
                <span v-if="!form.idFile" class="upload-label">ID / Passport<br/><span class="upload-hint">JPG, PNG or PDF</span></span>
                <span v-else class="upload-label uploaded">✓ {{ form.idFile.name }}</span>
              </div>
            </label>
            <label class="upload-zone">
              <input type="file" accept=".jpg,.png,.pdf" @change="handleFile($event, 'income')" hidden />
              <div class="upload-inner">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="1.5">
                  <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>
                </svg>
                <span v-if="!form.incomeFile" class="upload-label">Proof of Income<br/><span class="upload-hint">Payslip or bank statement</span></span>
                <span v-else class="upload-label uploaded">✓ {{ form.incomeFile.name }}</span>
              </div>
            </label>
          </div>
        </div>

        <div class="card decl-card">
          <p class="decl-title">Declarations</p>
          <label class="decl-item">
            <input type="checkbox" v-model="form.decl1" />
            <span>I confirm all information provided is accurate and complete to the best of my knowledge.</span>
          </label>
          <label class="decl-item">
            <input type="checkbox" v-model="form.decl2" />
            <span>I understand this is an <strong>application only</strong> – no payment will be charged until my application is approved by both the landlord and admin.</span>
          </label>
          <label class="decl-item">
            <input type="checkbox" v-model="form.decl3" />
            <span>I agree to the <u>Terms of Service</u> and <u>Privacy Policy</u>.</span>
          </label>
        </div>

        <div class="nav-row">
          <button class="btn-back" @click="goToStep(1)">← Back</button>
          <button class="btn-next" :disabled="!canProceedStep2" @click="goToStep(3)">Next — Review Application</button>
        </div>
      </template>

      <!-- ══════════════════════════════════════
           STEP 3 — Review Application
      ══════════════════════════════════════ -->
      <template v-if="currentStep === 3">
        <div class="review-header-card">
          <p class="review-section-title">Review your application before submitting</p>
          <p class="review-note">Please check all details carefully. You can go back to make changes.</p>
        </div>

        <!-- Property Summary -->
        <div class="card review-card">
          <div class="review-group-title">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
            Property
          </div>
          <div class="review-row">
            <span class="review-label">Property</span>
            <span class="review-val">{{ property.name }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Location</span>
            <span class="review-val">{{ property.location }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Monthly Rent</span>
            <span class="review-val">${{ property.price }} / month</span>
          </div>
        </div>

        <!-- Application Details -->
        <div class="card review-card">
          <div class="review-group-title">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>
            </svg>
            Application Details
          </div>
          <div class="review-row">
            <span class="review-label">Lease Duration</span>
            <span class="review-val">{{ form.leaseDuration }} months</span>
          </div>
          <div class="review-row">
            <span class="review-label">Total Occupants</span>
            <span class="review-val">{{ form.occupants || '—' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Pets</span>
            <span class="review-val">{{ form.pets || '—' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Rental Experience</span>
            <span class="review-val">{{ form.rentalExp || '—' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Move-in Date</span>
            <span class="review-val">{{ form.moveInDate || '—' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Monthly Income</span>
            <span class="review-val">{{ form.income ? '$' + form.income : '—' }}</span>
          </div>
          <div class="review-row tall">
            <span class="review-label">Message</span>
            <span class="review-val message-val">{{ form.message || '—' }}</span>
          </div>
        </div>

        <!-- Documents -->
        <div class="card review-card">
          <div class="review-group-title">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
            </svg>
            Uploaded Documents
          </div>
          <div class="review-row">
            <span class="review-label">ID / Passport</span>
            <span class="review-val" :class="{ 'uploaded-tag': form.idFile }">
              {{ form.idFile ? '✓ ' + form.idFile.name : 'Not uploaded' }}
            </span>
          </div>
          <div class="review-row">
            <span class="review-label">Proof of Income</span>
            <span class="review-val" :class="{ 'uploaded-tag': form.incomeFile }">
              {{ form.incomeFile ? '✓ ' + form.incomeFile.name : 'Not uploaded' }}
            </span>
          </div>
        </div>

        <!-- Declarations -->
        <div class="card review-card">
          <div class="review-group-title">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 6L9 17l-5-5"/>
            </svg>
            Declarations
          </div>
          <div class="review-row">
            <span class="review-label">Information accurate</span>
            <span class="review-val" :class="{ 'decl-yes': form.decl1, 'decl-no': !form.decl1 }">{{ form.decl1 ? '✓ Agreed' : '✗ Not agreed' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Application only (no payment)</span>
            <span class="review-val" :class="{ 'decl-yes': form.decl2, 'decl-no': !form.decl2 }">{{ form.decl2 ? '✓ Agreed' : '✗ Not agreed' }}</span>
          </div>
          <div class="review-row">
            <span class="review-label">Terms & Privacy Policy</span>
            <span class="review-val" :class="{ 'decl-yes': form.decl3, 'decl-no': !form.decl3 }">{{ form.decl3 ? '✓ Agreed' : '✗ Not agreed' }}</span>
          </div>
        </div>

        <!-- Estimated Costs -->
        <div class="card cost-card">
          <p class="cost-title">Estimated Costs</p>
          <div class="cost-row">
            <span class="cost-label"><strong>Total</strong></span>
            <span class="cost-val"><strong>${{ property.price }}.00</strong></span>
          </div>
          <div class="cost-row sub">
            <span class="cost-label">Tax (10%)</span>
            <span class="cost-val">${{ tax }}</span>
          </div>
          <div class="divider"></div>
          <div class="cost-row grand">
            <span class="cost-label">Grand Total</span>
            <span class="cost-val">${{ grandTotal }}.00</span>
          </div>
        </div>

        <div class="nav-row">
          <button class="btn-back" @click="goToStep(2)">← Back</button>
          <button class="btn-submit" @click="submitApplication">Submit Application</button>
        </div>
      </template>

    </main>

    <!-- ══════════════════════════════════════
         STEP 4 — Confirmation (Full Page)
    ══════════════════════════════════════ -->
    <div class="confirm-page" v-if="currentStep === 4">
      <div class="confirm-box">
        <div class="success-icon">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
            <path d="M20 6L9 17l-5-5"/>
          </svg>
        </div>
        <h2 class="confirm-title">Application Submitted!</h2>
        <p class="confirm-desc">
          Your rental application for <strong>{{ property.name }}</strong> has been received.
          No payment has been taken — you'll be contacted once the landlord and admin have reviewed it.
        </p>

        <!-- Summary Pill -->
        <div class="confirm-summary">
          <div class="confirm-summary-row">
            <span class="cs-label">Property</span>
            <span class="cs-val">{{ property.name }}</span>
          </div>
          <div class="confirm-summary-row">
            <span class="cs-label">Lease</span>
            <span class="cs-val">{{ form.leaseDuration }} months</span>
          </div>
          <div class="confirm-summary-row">
            <span class="cs-label">Grand Total</span>
            <span class="cs-val">${{ grandTotal }}.00</span>
          </div>
        </div>

        <!-- Timeline -->
        <div class="timeline">
          <div class="timeline-item">
            <div class="tl-dot done"></div>
            <div class="tl-content">
              <span class="tl-label">Application received</span>
              <span class="tl-time">Just now</span>
            </div>
          </div>
          <div class="tl-line"></div>
          <div class="timeline-item">
            <div class="tl-dot pending"></div>
            <div class="tl-content">
              <span class="tl-label">Landlord review</span>
              <span class="tl-time">24–48 hrs</span>
            </div>
          </div>
          <div class="tl-line"></div>
          <div class="timeline-item">
            <div class="tl-dot pending"></div>
            <div class="tl-content">
              <span class="tl-label">Admin approval</span>
              <span class="tl-time">24–72 hrs</span>
            </div>
          </div>
        </div>

        <button class="got-it-btn" @click="$router.push('/home')">Back to Home</button>
        <button class="view-prop-btn" @click="$router.push(`/property/${propertyId}`)">View Property</button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { properties } from '../../store.js'

const route = useRoute()
const router = useRouter()

const propertyId = parseInt(route.params.id)
const property = computed(() => {
  return properties.value.find(p => p.id === propertyId) || properties.value[0]
})

const currentStep = ref(1)
const stepLabels = ['Application Form', 'Upload Documents', 'Review', 'Confirmation']
const leaseDurations = [6, 12, 18, 24]

const form = ref({
  leaseDuration: 12,
  occupants: '',
  pets: '',
  rentalExp: '',
  moveInDate: '',
  message: '',
  income: '',
  idFile: null,
  incomeFile: null,
  decl1: false,
  decl2: false,
  decl3: false,
})

const tax = computed(() => Math.round(property.value.price * 0.1))
const grandTotal = computed(() => property.value.price + tax.value)

const canProceedStep2 = computed(() => form.value.decl1 && form.value.decl2 && form.value.decl3)

const handleFile = (event, type) => {
  const file = event.target.files[0]
  if (!file) return
  if (type === 'id') form.value.idFile = file
  else form.value.incomeFile = file
}

const goToStep = (step) => {
  currentStep.value = step
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const submitApplication = () => {
  currentStep.value = 4
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleBack = () => {
  if (currentStep.value === 1) {
    router.push(`/property/${propertyId}`)
  } else if (currentStep.value === 4) {
    router.push('/home')
  } else {
    goToStep(currentStep.value - 1)
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.app-page {
  font-family: 'DM Sans', sans-serif;
  background: #f7f7f7;
  min-height: 100vh;
  color: #111;
}

/* ── HERO ── */
.app-hero { background: #fff; position: relative; }
.app-top-bar {
  position: absolute;
  top: 16px; left: 20px;
  z-index: 20;
}
.back-btn {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.85);
  border: none;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  transition: background 0.2s;
}
.back-btn:hover { background: #fff; }
.hero-img-wrap {
  position: relative;
  width: 100%; height: 200px;
  overflow: hidden;
}
.hero-img { width: 100%; height: 100%; object-fit: cover; }
.hero-badge {
  position: absolute;
  bottom: 12px; left: 16px;
  display: flex; align-items: center; gap: 6px;
  background: rgba(30,30,30,0.78);
  color: #fff;
  font-size: 0.78rem; font-weight: 600;
  padding: 5px 12px; border-radius: 20px;
  backdrop-filter: blur(4px);
}

/* ── BODY ── */
.app-body {
  max-width: 780px;
  margin: 0 auto;
  padding: 28px 20px 80px;
}

/* ── TITLE ROW ── */
.title-row {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 24px; flex-wrap: wrap; gap: 8px;
}
.form-title { font-size: 1.5rem; font-weight: 700; margin: 0 0 4px; }
.form-subtitle { font-size: 0.95rem; font-weight: 500; color: #555; margin: 0; }
.title-right { display: flex; align-items: baseline; gap: 3px; padding-top: 2px; }
.price-val { font-size: 1.5rem; font-weight: 700; }
.price-period { font-size: 0.82rem; color: #666; font-weight: 500; }

/* ── STEPPER ── */
.stepper {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  margin-bottom: 28px;
  gap: 0;
  overflow-x: auto;
  padding: 4px 0 8px;
}
.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex: 1;
  min-width: 60px;
}
.step-circle {
  width: 30px; height: 30px;
  border-radius: 50%;
  border: 2px solid #ddd;
  background: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.78rem; font-weight: 700; color: #aaa;
  transition: all 0.25s;
  position: relative;
  z-index: 2;
}
.step-item.active .step-circle {
  border-color: #111; background: #111; color: #fff;
}
.step-item.done .step-circle {
  border-color: #22c55e; background: #22c55e; color: #fff;
}
.step-label {
  font-size: 0.68rem; font-weight: 600;
  color: #aaa; margin-top: 6px;
  text-align: center; line-height: 1.3;
  white-space: nowrap;
}
.step-item.active .step-label { color: #111; }
.step-item.done .step-label { color: #22c55e; }
.step-connector {
  position: absolute;
  top: 15px;
  left: calc(50% + 15px);
  width: calc(100% - 30px);
  height: 2px;
  background: #e0e0e0;
  z-index: 1;
}
.step-item.done .step-connector { background: #22c55e; }

/* ── HOUSE INFO ── */
.section { margin-bottom: 20px; }
.section-heading { font-size: 1.15rem; font-weight: 700; margin: 0 0 6px; }
.sub-heading { font-size: 0.85rem; font-weight: 600; color: #444; margin: 0 0 12px; }
.icons-row { display: flex; gap: 10px; flex-wrap: wrap; }
.d-icon {
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;
  width: 56px; height: 56px;
  border: 1px solid #e0e0e0; border-radius: 8px;
  font-size: 0.6rem; font-weight: 600; color: #444; background: #fff;
}

/* ── CARDS ── */
.card {
  background: #fff;
  border-radius: 12px;
  border: 1px solid #e8e8e8;
  padding: 20px;
  margin-bottom: 16px;
}

/* ── FORM FIELDS ── */
.field-group { display: flex; flex-direction: column; gap: 6px; flex: 1; min-width: 180px; }
.field-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px; }
.field-label { font-size: 0.82rem; font-weight: 600; color: #222; }
.field-input {
  border: 1px solid #ddd; border-radius: 8px;
  padding: 9px 12px; font-size: 0.85rem;
  font-family: inherit; color: #111; outline: none;
  transition: border-color 0.2s; background: #fff;
}
.field-input:focus { border-color: #111; }
.field-textarea {
  border: 1px solid #ddd; border-radius: 8px;
  padding: 9px 12px; font-size: 0.85rem;
  font-family: inherit; color: #111; outline: none;
  resize: none; height: 90px;
  transition: border-color 0.2s; background: #fff;
}
.field-textarea:focus { border-color: #111; }
.field-hint { font-size: 0.72rem; color: #888; line-height: 1.4; margin: 0; }

/* Pills */
.pill-row { display: flex; gap: 8px; flex-wrap: wrap; }
.pill-btn {
  padding: 6px 16px; border-radius: 20px;
  border: 1px solid #ddd; background: #fff;
  font-size: 0.82rem; font-weight: 600; color: #444;
  cursor: pointer; font-family: inherit; transition: all 0.18s;
}
.pill-btn:hover { border-color: #111; color: #111; }
.pill-btn.active { background: #111; color: #fff; border-color: #111; }

/* ── DOCUMENTS ── */
.doc-title { font-size: 0.9rem; font-weight: 600; margin: 0 0 14px; }
.doc-note { font-weight: 400; color: #888; font-size: 0.8rem; }
.doc-upload-row { display: flex; gap: 16px; flex-wrap: wrap; }
.upload-zone {
  flex: 1; min-width: 140px; max-width: 220px;
  border: 1.5px dashed #d0d0d0;
  border-radius: 10px; cursor: pointer;
  transition: border-color 0.2s; display: block;
}
.upload-zone:hover { border-color: #999; }
.upload-inner {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 8px; padding: 24px 12px; text-align: center;
}
.upload-label { font-size: 0.75rem; font-weight: 600; color: #555; line-height: 1.4; }
.upload-label.uploaded { color: #22c55e; }
.upload-hint { font-size: 0.68rem; font-weight: 400; color: #aaa; }

/* ── DECLARATIONS ── */
.decl-title { font-size: 0.9rem; font-weight: 700; margin: 0 0 14px; }
.decl-item {
  display: flex; align-items: flex-start; gap: 10px;
  font-size: 0.82rem; color: #333; line-height: 1.45;
  margin-bottom: 10px; cursor: pointer;
}
.decl-item:last-child { margin-bottom: 0; }
.decl-item input[type="checkbox"] {
  margin-top: 2px; width: 14px; height: 14px;
  flex-shrink: 0; accent-color: #111; cursor: pointer;
}

/* ── REVIEW PAGE ── */
.review-header-card {
  background: #f0f9ff;
  border: 1px solid #bae6fd;
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 16px;
}
.review-section-title {
  font-size: 0.95rem; font-weight: 700;
  color: #0369a1; margin: 0 0 4px;
}
.review-note { font-size: 0.8rem; color: #0284c7; margin: 0; }

.review-card { padding: 18px 20px; }
.review-group-title {
  display: flex; align-items: center; gap: 8px;
  font-size: 0.82rem; font-weight: 700;
  color: #555; text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 14px; padding-bottom: 10px;
  border-bottom: 1px solid #f0f0f0;
}
.review-row {
  display: flex; justify-content: space-between;
  align-items: flex-start;
  padding: 7px 0;
  border-bottom: 1px solid #f7f7f7;
  gap: 16px;
}
.review-row:last-child { border-bottom: none; }
.review-row.tall { align-items: flex-start; }
.review-label { font-size: 0.82rem; color: #888; font-weight: 500; flex-shrink: 0; min-width: 130px; }
.review-val { font-size: 0.85rem; font-weight: 600; color: #111; text-align: right; }
.message-val { text-align: left; line-height: 1.5; color: #333; font-weight: 400; }
.uploaded-tag { color: #22c55e; }
.decl-yes { color: #22c55e; }
.decl-no { color: #ef4444; }

/* ── COSTS ── */
.cost-title { font-size: 0.95rem; font-weight: 700; margin: 0 0 12px; }
.cost-row { display: flex; justify-content: space-between; align-items: center; padding: 4px 0; }
.cost-row.sub { color: #666; font-size: 0.85rem; }
.cost-row.grand { font-size: 1rem; font-weight: 700; }
.cost-val { font-weight: 600; }
.divider { border: none; border-top: 1px solid #ebebeb; margin: 10px 0; }

/* ── NAV BUTTONS ── */
.nav-row {
  display: flex; justify-content: space-between;
  align-items: center; margin-top: 8px; gap: 12px;
}
.btn-back {
  padding: 12px 20px;
  background: #fff; color: #444;
  border: 1px solid #ddd; border-radius: 10px;
  font-size: 0.9rem; font-weight: 600;
  font-family: inherit; cursor: pointer;
  transition: all 0.2s;
}
.btn-back:hover { border-color: #111; color: #111; }
.btn-next {
  flex: 1; max-width: 320px;
  padding: 13px 20px;
  background: #111; color: #fff;
  border: none; border-radius: 10px;
  font-size: 0.92rem; font-weight: 700;
  font-family: inherit; cursor: pointer;
  transition: background 0.2s, opacity 0.2s;
}
.btn-next:hover:not(:disabled) { background: #000; }
.btn-next:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-submit {
  flex: 1; max-width: 320px;
  padding: 13px 20px;
  background: #111; color: #fff;
  border: none; border-radius: 10px;
  font-size: 0.95rem; font-weight: 700;
  font-family: inherit; cursor: pointer;
  transition: background 0.2s;
}
.btn-submit:hover { background: #000; }

/* ── CONFIRMATION PAGE ── */
.confirm-page {
  display: flex; align-items: flex-start;
  justify-content: center;
  padding: 40px 20px 80px;
  min-height: calc(100vh - 200px);
}
.confirm-box {
  background: #fff;
  border-radius: 20px;
  border: 1px solid #e8e8e8;
  padding: 40px 32px 32px;
  max-width: 460px;
  width: 100%;
  text-align: center;
}
.success-icon {
  width: 76px; height: 76px;
  border-radius: 50%;
  background: #f0fdf4;
  border: 2px solid #bbf7d0;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 20px;
}
.confirm-title { font-size: 1.5rem; font-weight: 700; margin: 0 0 12px; }
.confirm-desc {
  font-size: 0.88rem; color: #555;
  line-height: 1.6; margin: 0 0 20px;
}

/* Summary pill in confirmation */
.confirm-summary {
  background: #f7f7f7;
  border-radius: 12px;
  padding: 14px 18px;
  margin-bottom: 24px;
  text-align: left;
}
.confirm-summary-row {
  display: flex; justify-content: space-between;
  padding: 5px 0;
  font-size: 0.84rem;
}
.cs-label { color: #888; font-weight: 500; }
.cs-val { font-weight: 700; color: #111; }

/* Timeline */
.timeline {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 28px;
  text-align: left;
}
.timeline-item {
  display: flex; align-items: center; gap: 12px;
}
.tl-dot {
  width: 12px; height: 12px;
  border-radius: 50%; flex-shrink: 0;
}
.tl-dot.done { background: #22c55e; }
.tl-dot.pending { background: #e0e0e0; border: 2px solid #ccc; }
.tl-line {
  width: 2px; height: 22px;
  background: #e0e0e0;
  margin-left: 5px;
}
.tl-content {
  display: flex; justify-content: space-between;
  width: 100%; align-items: center; gap: 12px;
}
.tl-label { font-size: 0.85rem; font-weight: 600; color: #222; }
.tl-time { font-size: 0.8rem; color: #888; }

.got-it-btn {
  width: 100%; padding: 14px;
  background: #111; color: #fff;
  border: none; border-radius: 10px;
  font-size: 0.95rem; font-weight: 700;
  font-family: inherit; cursor: pointer;
  transition: background 0.2s; margin-bottom: 10px;
}
.got-it-btn:hover { background: #000; }
.view-prop-btn {
  width: 100%; padding: 13px;
  background: #fff; color: #111;
  border: 1px solid #ddd; border-radius: 10px;
  font-size: 0.9rem; font-weight: 600;
  font-family: inherit; cursor: pointer;
  transition: all 0.2s;
}
.view-prop-btn:hover { border-color: #111; }

/* ── RESPONSIVE ── */

/* Tablet (≤ 768px) */
@media (max-width: 768px) {
  .app-body { padding: 22px 16px 80px; }
  .hero-img-wrap { height: 180px; }
  .title-row { flex-direction: column; gap: 4px; margin-bottom: 18px; }
  .form-title { font-size: 1.3rem; }
  .price-val { font-size: 1.3rem; }
  .card { padding: 16px; }

  .stepper { gap: 0; }
  .step-label { font-size: 0.62rem; }

  .field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .field-row .field-group:nth-child(2) { grid-column: 1 / -1; }

  .review-label { min-width: 110px; }

  .confirm-box { padding: 30px 22px 24px; }
}

/* Mobile (≤ 480px) */
@media (max-width: 480px) {
  .app-body { padding: 16px 12px 90px; }
  .hero-img-wrap { height: 155px; }

  .stepper { gap: 0; padding: 2px 0 6px; }
  .step-circle { width: 26px; height: 26px; font-size: 0.72rem; }
  .step-label { font-size: 0.58rem; }
  .step-connector { top: 13px; }

  .form-title { font-size: 1.1rem; }
  .form-subtitle { font-size: 0.8rem; }
  .price-val { font-size: 1.15rem; }

  .icons-row { gap: 6px; }
  .d-icon { width: 50px; height: 50px; font-size: 0.55rem; }

  .card { padding: 14px; border-radius: 10px; margin-bottom: 12px; }

  .field-row { display: flex; flex-direction: column; gap: 12px; }
  .field-row .field-group:nth-child(2) { grid-column: unset; }
  .field-group { min-width: 100%; }

  .pill-btn { padding: 5px 11px; font-size: 0.77rem; }

  .doc-upload-row { flex-direction: column; gap: 10px; }
  .upload-zone { max-width: 100%; width: 100%; }
  .upload-inner { flex-direction: row; justify-content: flex-start; padding: 14px 16px; gap: 14px; text-align: left; }

  .review-row { flex-direction: column; gap: 4px; }
  .review-label { min-width: unset; }
  .review-val { text-align: left; }

  .nav-row { flex-direction: column-reverse; gap: 10px; }
  .btn-next, .btn-submit { max-width: 100%; width: 100%; }
  .btn-back { width: 100%; text-align: center; }

  .confirm-page { padding: 20px 14px 80px; align-items: flex-start; }
  .confirm-box { padding: 28px 18px 22px; }
  .confirm-title { font-size: 1.2rem; }
  .confirm-desc { font-size: 0.82rem; }
}

/* Very small phones (≤ 360px) */
@media (max-width: 360px) {
  .app-body { padding: 14px 10px 90px; }
  .step-label { display: none; }
  .step-circle { width: 24px; height: 24px; font-size: 0.68rem; }
  .pill-btn { padding: 4px 9px; font-size: 0.74rem; }
  .d-icon { width: 44px; height: 44px; font-size: 0.5rem; }
}
</style>
