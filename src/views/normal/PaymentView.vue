<template>
  <div class="payment-flow-page">
    <!-- SCREEN 1: SPLIT SCREEN CHECKOUT FORM -->
    <div v-if="currentStep === 1" class="split-checkout-layout">
      <!-- Left Hero Banner -->
      <div class="left-hero">
        <!-- Top Back Row -->
        <div class="hero-top-bar">
          <button class="back-circle" type="button" aria-label="Go back" @click="handleBack">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.5">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <span class="plan-label">You plan</span>
        </div>

        <div class="hero-content">
          <h1 class="plan-price">${{ planPrice.toFixed(2) }}/person</h1>
          <p class="plan-sub">
            We will bill you ${{ monthlyRate.toFixed(2) }} monthly + taxes, unless you cancel it.
          </p>

          <!-- Translucent Plan Card -->
          <div class="glass-plan-card">
            <div class="card-header-row">
              <span class="plan-name">{{ planName }}</span>
              <span class="plan-rate">${{ monthlyRate.toFixed(2) }}</span>
            </div>
            <p class="plan-terms">
              All the payment cannot be cancel after 30 days was made.
            </p>

            <!-- Promo Code Action -->
            <div class="promo-section">
              <button 
                v-if="!showPromoInput && !discountApplied" 
                class="add-promo-pill" 
                type="button" 
                @click="showPromoInput = true"
              >
                Add Promo Code
              </button>
              <div v-else-if="showPromoInput && !discountApplied" class="promo-input-row">
                <input 
                  type="text" 
                  v-model="promoInput" 
                  placeholder="Enter code (e.g. SWEET10)" 
                  class="promo-field"
                  @keyup.enter="applyPromo"
                />
                <button type="button" class="promo-apply-btn" @click="applyPromo">Apply</button>
              </div>
              <div v-else class="promo-success-pill">
                <span>Promo code applied (-${{ discount.toFixed(2) }})</span>
                <button type="button" class="promo-close" @click="removePromo">✕</button>
              </div>
            </div>

            <div class="glass-divider"></div>

            <!-- Price Breakdown -->
            <div class="breakdown-list">
              <div class="breakdown-row">
                <span class="bd-label">Subtotal:</span>
                <span class="bd-val">${{ subtotal.toFixed(2) }}</span>
              </div>
              <div class="breakdown-row">
                <span class="bd-label">Tax:</span>
                <span class="bd-val">${{ tax.toFixed(2) }}</span>
              </div>
              <div class="breakdown-row total-row">
                <span class="bd-label">Total due today</span>
                <span class="bd-val">${{ total.toFixed(2) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Form Panel -->
      <div class="right-form-panel">
        <div class="form-inner">
          <!-- Billing frequency -->
          <div class="section-block">
            <h2 class="form-title">Billing frequency</h2>
            <div class="frequency-card">
              <div class="freq-sub">Pay monthly</div>
              <div class="freq-amount">${{ total.toFixed(2) }}/monthly</div>
            </div>
          </div>

          <!-- Payment method -->
          <div class="section-block">
            <h2 class="form-title">Payment method</h2>
            <div class="payment-methods-row">
              <!-- Mastercard -->
              <button 
                type="button" 
                class="method-btn" 
                :class="{ active: selectedMethod === 'mastercard' }"
                @click="selectedMethod = 'mastercard'"
                title="Mastercard"
              >
                <div class="mc-circles">
                  <span class="mc-c mc-red"></span>
                  <span class="mc-c mc-orange"></span>
                </div>
              </button>

              <!-- VISA -->
              <button 
                type="button" 
                class="method-btn" 
                :class="{ active: selectedMethod === 'visa' }"
                @click="selectedMethod = 'visa'"
                title="VISA"
              >
                <span class="visa-badge">VISA</span>
              </button>

              <!-- KHQR -->
              <button 
                type="button" 
                class="method-btn" 
                :class="{ active: selectedMethod === 'khqr' }"
                @click="selectedMethod = 'khqr'"
                title="KHQR Bakong"
              >
                <span class="khqr-badge">KHQR</span>
              </button>
            </div>
          </div>

          <!-- Payment Information -->
          <div class="section-block">
            <h2 class="form-title">Payment Information</h2>
            
            <form @submit.prevent="proceedToConfirmation" class="payment-form">
              <!-- Card number, Expired date, CVC -->
              <div class="form-row-three">
                <div class="input-col col-card-num">
                  <label class="input-lbl">Card number</label>
                  <input 
                    type="text" 
                    v-model="cardNumber" 
                    class="txt-input" 
                    placeholder="0000 0000 0000 0000"
                    maxlength="19"
                    @input="formatCardNumber"
                  />
                </div>
                <div class="input-col col-exp">
                  <label class="input-lbl">Expired date</label>
                  <input 
                    type="text" 
                    v-model="expiryDate" 
                    class="txt-input" 
                    placeholder="MM/YY"
                    maxlength="5"
                    @input="formatExpiry"
                  />
                </div>
                <div class="input-col col-cvc">
                  <label class="input-lbl">CVC</label>
                  <input 
                    type="text" 
                    v-model="cvc" 
                    class="txt-input" 
                    placeholder="3-digits code"
                    maxlength="4"
                  />
                </div>
              </div>

              <!-- Card Name -->
              <div class="form-row">
                <label class="input-lbl">Card Name</label>
                <input 
                  type="text" 
                  v-model="cardName" 
                  class="txt-input" 
                  placeholder="e.g, Rose Berry"
                />
              </div>

              <!-- Address -->
              <div class="form-row">
                <label class="input-lbl">Address</label>
                <input 
                  type="text" 
                  v-model="address1" 
                  class="txt-input" 
                  placeholder="Street address PO number"
                />
                <input 
                  type="text" 
                  v-model="address2" 
                  class="txt-input mt-10" 
                  placeholder="Apt., suit, unit, building (opt)"
                />
              </div>

              <!-- City & State -->
              <div class="form-row-two">
                <div class="input-col">
                  <label class="input-lbl">City</label>
                  <input 
                    type="text" 
                    v-model="city" 
                    class="txt-input" 
                    placeholder="City"
                  />
                </div>
                <div class="input-col">
                  <label class="input-lbl">State</label>
                  <input 
                    type="text" 
                    v-model="state" 
                    class="txt-input" 
                    placeholder="State"
                  />
                </div>
              </div>

              <!-- Country -->
              <div class="form-row">
                <label class="input-lbl">Country</label>
                <input 
                  type="text" 
                  v-model="country" 
                  class="txt-input" 
                  placeholder="e.g, Rose Berry"
                />
              </div>

              <!-- Checkout Button -->
              <button type="submit" class="checkout-submit-btn">
                Checkout
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- SCREEN 2: PAYMENT CONFIRMATION (FULLSCREEN GRADIENT) -->
    <div v-else-if="currentStep === 2" class="fullscreen-gradient-step">
      <div class="hero-top-bar confirm-top-bar">
        <button class="back-circle" type="button" aria-label="Go back" @click="currentStep = 1">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.5">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
        </button>
        <span class="plan-label">Payment confirmation</span>
      </div>

      <div class="centered-message-box">
        <h1 class="big-gradient-title">You’re about to pay ${{ total.toFixed(2) }}</h1>
        <p class="target-entity">to {{ propertyTitle }}.</p>
        <p class="confirm-instruction">
          Are your sure that you want to proceed this payment? If so, click on <strong>Pay now</strong>.
        </p>
        
        <button 
          type="button" 
          class="frosted-pill-btn" 
          :disabled="isProcessing"
          @click="handlePayNow"
        >
          <span v-if="!isProcessing">Pay now</span>
          <span v-else class="spinner-row">
            <svg class="spin-circle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <circle cx="12" cy="12" r="10" stroke-opacity="0.25"/>
              <path d="M12 2a10 10 0 0 1 10 10" stroke-linecap="round"/>
            </svg>
            Processing...
          </span>
        </button>
      </div>
    </div>

    <!-- SCREEN 3: PAYMENT SUCCESS (FULLSCREEN GRADIENT) -->
    <div v-else-if="currentStep === 3" class="fullscreen-gradient-step">
      <div class="centered-message-box">
        <h1 class="big-gradient-title success-headline">Payment Success</h1>
        <p class="success-hint">Got to review your reciept</p>
        
        <button 
          type="button" 
          class="frosted-pill-btn" 
          @click="showReceiptModal = true"
        >
          View Receipt
        </button>
      </div>
    </div>

    <!-- SCREEN 4: PAYMENT CONFIRMED RECEIPT CARD (MODAL / OVERLAY) -->
    <div v-if="showReceiptModal" class="receipt-modal-backdrop" @click.self="showReceiptModal = false">
      <div class="receipt-card-container">
        <!-- Purple checkmark header -->
        <div class="receipt-header-banner">
          <div class="white-check-circle">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
              <polyline points="20 6 9 17 4 12"/>
            </svg>
          </div>
          <h2 class="receipt-title">Payment Confirmed!</h2>
        </div>

        <!-- Receipt Body Content -->
        <div class="receipt-card-body">
          <!-- 4-Column Metadata Row -->
          <div class="receipt-meta-grid">
            <div class="meta-item">
              <span class="meta-label">Date</span>
              <span class="meta-val">{{ receiptDate }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Order No</span>
              <span class="meta-val">{{ orderNumber }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Bill to</span>
              <span class="meta-val">Homesweet</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Payment Type</span>
              <span class="meta-val">{{ paymentTypeDisplay }}</span>
            </div>
          </div>

          <div class="receipt-divider"></div>

          <!-- Gray Room & Amount Box -->
          <div class="room-summary-box">
            <div class="room-row">
              <div class="room-title-col">
                <span class="box-small-lbl">Room</span>
                <span class="box-main-val">{{ roomFullName }}</span>
              </div>
              <div class="room-date-col">
                <span class="box-small-lbl">Payment Date</span>
                <span class="box-main-val">{{ receiptDate }}</span>
              </div>
            </div>

            <div class="box-inner-divider"></div>

            <div class="room-amount-row">
              <span class="box-amount-lbl">Amount Paid</span>
              <span class="box-amount-val">${{ total.toFixed(2) }}</span>
            </div>
          </div>

          <!-- Actions Footer -->
          <div class="receipt-actions">
            <button class="receipt-btn secondary" type="button" @click="handleDone">
              Return to Listings
            </button>
            <button class="receipt-btn primary" type="button" @click="printReceipt">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 6 2 18 2 18 9"></polyline>
                <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
                <rect x="6" y="14" width="12" height="8"></rect>
              </svg>
              Print Receipt
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { properties } from '../../store.js'
import { db, auth } from '../../firebase.js'
import { collection, addDoc } from 'firebase/firestore'

const router = useRouter()
const route = useRoute()

// Step state: 1 = Form, 2 = Confirmation, 3 = Success
const currentStep = ref(1)
const showReceiptModal = ref(false)
const isProcessing = ref(false)

// Property info
const propertyId = computed(() => Number(route.params.id) || 1)
const currentProperty = computed(() => {
  return properties.value.find(p => p.id === propertyId.value) || properties.value[0]
})

const propertyTitle = computed(() => {
  if (currentProperty.value && currentProperty.value.id !== 1) {
    return `${currentProperty.value.name} Premium`
  }
  return 'Skystar Condo Premium'
})

const roomFullName = computed(() => {
  if (currentProperty.value && currentProperty.value.id !== 1) {
    return `${currentProperty.value.name} Premium N.101A`
  }
  return 'Skystar Condo Premium N.101A'
})

// Pricing specs matching mockup ($450.00/person, $37.50 monthly + $3.75 tax = $41.25)
const planName = ref('Standard Pro')
const planPrice = ref(450.00)
const monthlyRate = ref(37.50)
const discount = ref(0.00)
const discountApplied = ref(false)
const promoInput = ref('')
const showPromoInput = ref(false)

const subtotal = computed(() => {
  return Math.max(0, monthlyRate.value - discount.value)
})

const tax = computed(() => {
  return parseFloat((subtotal.value * 0.1).toFixed(2))
})

const total = computed(() => {
  return parseFloat((subtotal.value + tax.value).toFixed(2))
})

// Form inputs
const selectedMethod = ref('mastercard')
const cardNumber = ref('')
const expiryDate = ref('')
const cvc = ref('')
const cardName = ref('')
const address1 = ref('')
const address2 = ref('')
const city = ref('')
const state = ref('')
const country = ref('')

// Receipt metadata
const receiptDate = ref('22/04/2026')
const orderNumber = ref('011-22042026')

const paymentTypeDisplay = computed(() => {
  if (selectedMethod.value === 'mastercard') return 'Debit Card'
  if (selectedMethod.value === 'visa') return 'Credit Card'
  if (selectedMethod.value === 'khqr') return 'KHQR Bakong'
  return 'Debit Card'
})

// Input formatters
function formatCardNumber(e) {
  let val = e.target.value.replace(/\D/g, '')
  val = val.substring(0, 16)
  const sections = val.match(/.{1,4}/g)
  cardNumber.value = sections ? sections.join(' ') : ''
}

function formatExpiry(e) {
  let val = e.target.value.replace(/\D/g, '')
  if (val.length >= 3) {
    expiryDate.value = val.substring(0, 2) + '/' + val.substring(2, 4)
  } else {
    expiryDate.value = val
  }
}

// Promo logic
function applyPromo() {
  if (!promoInput.value) return
  discount.value = 5.00
  discountApplied.value = true
  showPromoInput.value = false
}

function removePromo() {
  discount.value = 0.00
  discountApplied.value = false
  promoInput.value = ''
}

// Navigation & Actions
function handleBack() {
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/home')
  }
}

function proceedToConfirmation() {
  currentStep.value = 2
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function handlePayNow() {
  isProcessing.value = true

  const paymentRecord = {
    userId: auth.currentUser?.uid || 'guest_' + Date.now(),
    userName: cardName.value || auth.currentUser?.displayName || 'Resident User',
    userEmail: auth.currentUser?.email || 'resident@example.com',
    propertyId: propertyId.value,
    propertyName: propertyTitle.value,
    planName: planName.value,
    amount: total.value,
    method: selectedMethod.value,
    billingAddress: {
      address1: address1.value,
      city: city.value,
      country: country.value
    },
    status: 'succeeded',
    orderNumber: orderNumber.value,
    receiptDate: receiptDate.value,
    createdAt: new Date().toISOString()
  }

  try {
    // 1. Record payment in Firestore 'payments'
    await addDoc(collection(db, 'payments'), paymentRecord)

    // 2. Create notification in Firestore 'notifications'
    await addDoc(collection(db, 'notifications'), {
      type: 'payment',
      title: 'Payment Received',
      desc: `${paymentRecord.propertyName} payment of $${paymentRecord.amount} was completed successfully.`,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      group: 'Today',
      unread: true,
      date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      roomName: paymentRecord.propertyName,
      amount: `$${paymentRecord.amount}`,
      orderNumber: paymentRecord.orderNumber,
      createdAt: new Date().toISOString()
    })
  } catch (err) {
    console.warn('Payment recording notice:', err)
  } finally {
    isProcessing.value = false
    currentStep.value = 3
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

function handleDone() {
  showReceiptModal.value = false
  router.push('/home')
}

function printReceipt() {
  window.print()
}

onMounted(() => {
  // If query specifies step
  if (route.query.step) {
    currentStep.value = Number(route.query.step)
  }
})
</script>

<style scoped>
.payment-flow-page {
  width: 100%;
  min-height: 100vh;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: #111827;
  background: #ffffff;
  position: relative;
}

/* ==========================================================================
   SCREEN 1: SPLIT CHECKOUT LAYOUT
   ========================================================================== */
.split-checkout-layout {
  display: flex;
  min-height: 100vh;
  width: 100%;
}

/* ------------------- Left Hero Panel ------------------- */
.left-hero {
  flex: 0 0 50%;
  min-height: 100vh;
  padding: 40px 48px 60px;
  display: flex;
  flex-direction: column;
  color: #ffffff;
  position: relative;
  overflow: hidden;
  background: radial-gradient(130% 120% at 100% 100%, #ec4899 0%, #c026d3 32%, #7c3aed 68%, #380b6b 100%);
}

/* Curved lighter gradient shape sweep */
.left-hero::after {
  content: '';
  position: absolute;
  width: 120%;
  height: 120%;
  right: -25%;
  bottom: -35%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(244, 63, 148, 0.45) 0%, rgba(192, 38, 211, 0.15) 50%, transparent 70%);
  pointer-events: none;
}

.hero-top-bar {
  display: flex;
  align-items: center;
  gap: 14px;
  position: relative;
  z-index: 2;
}

.back-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #ffffff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
  transition: transform 0.15s ease, background-color 0.15s ease;
}

.back-circle:hover {
  transform: scale(1.05);
  background: #f8fafc;
}

.plan-label {
  font-size: 1.15rem;
  font-weight: 500;
  color: #ffffff;
}

.hero-content {
  margin-top: 50px;
  position: relative;
  z-index: 2;
  max-width: 480px;
}

.plan-price {
  font-size: 3.2rem;
  font-weight: 800;
  line-height: 1.15;
  color: #ffffff;
  letter-spacing: -0.5px;
}

.plan-sub {
  margin-top: 14px;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.88);
  line-height: 1.5;
}

/* Glass Plan Card */
.glass-plan-card {
  margin-top: 40px;
  background: rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 18px;
  padding: 26px 28px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}

.card-header-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
}

.plan-terms {
  margin-top: 6px;
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.78);
  line-height: 1.4;
}

.promo-section {
  margin-top: 22px;
}

.add-promo-pill {
  width: 100%;
  background: rgba(255, 255, 255, 0.28);
  border: none;
  border-radius: 9999px;
  padding: 12px 20px;
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.15s ease;
  backdrop-filter: blur(8px);
}

.add-promo-pill:hover {
  background: rgba(255, 255, 255, 0.38);
  transform: translateY(-1px);
}

.promo-input-row {
  display: flex;
  gap: 8px;
}

.promo-field {
  flex: 1;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 9999px;
  padding: 10px 18px;
  color: #ffffff;
  font-size: 0.9rem;
  outline: none;
}

.promo-field::placeholder {
  color: rgba(255, 255, 255, 0.65);
}

.promo-apply-btn {
  background: #ffffff;
  color: #7c3aed;
  border: none;
  border-radius: 9999px;
  padding: 10px 18px;
  font-weight: 700;
  cursor: pointer;
}

.promo-success-pill {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(34, 197, 94, 0.25);
  border: 1px solid rgba(34, 197, 94, 0.45);
  padding: 8px 16px;
  border-radius: 9999px;
  font-size: 0.85rem;
  color: #ffffff;
}

.promo-close {
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  font-size: 1rem;
}

.glass-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.22);
  margin: 22px 0 18px;
}

.breakdown-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.breakdown-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.88);
}

.breakdown-row.total-row {
  margin-top: 4px;
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
}

/* ------------------- Right Form Panel ------------------- */
.right-form-panel {
  flex: 0 0 50%;
  min-height: 100vh;
  padding: 40px 64px 60px;
  background: #ffffff;
  overflow-y: auto;
}

.form-inner {
  max-width: 520px;
  margin: 0 auto;
}

.section-block {
  margin-bottom: 26px;
}

.form-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 14px;
  letter-spacing: -0.2px;
}

/* Billing frequency */
.frequency-card {
  border: 1.5px solid #d1d5db;
  border-radius: 8px;
  padding: 12px 18px;
  background: #ffffff;
}

.freq-sub {
  font-size: 0.78rem;
  color: #6b7280;
  font-weight: 500;
}

.freq-amount {
  font-size: 1.12rem;
  font-weight: 700;
  color: #111827;
  margin-top: 2px;
}

/* Payment methods */
.payment-methods-row {
  display: flex;
  gap: 14px;
}

.method-btn {
  flex: 1;
  height: 52px;
  border-radius: 8px;
  border: 1.5px solid #e5e7eb;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
}

.method-btn:hover {
  border-color: #93c5fd;
  background: #fbfcfe;
}

.method-btn.active {
  border-color: #2563eb;
  background: #f8faff;
  box-shadow: 0 0 0 1px #2563eb;
}

/* Mastercard logo circles */
.mc-circles {
  display: flex;
  position: relative;
  width: 38px;
  height: 24px;
  align-items: center;
  justify-content: center;
}

.mc-c {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  position: absolute;
}

.mc-red {
  background: #eb001b;
  left: 3px;
}

.mc-orange {
  background: #f79e1b;
  right: 3px;
  opacity: 0.95;
}

/* Visa badge */
.visa-badge {
  font-family: 'Arial Black', Impact, sans-serif;
  font-weight: 900;
  font-style: italic;
  font-size: 1.2rem;
  color: #1a1f71;
  letter-spacing: 0.5px;
}

/* KHQR badge */
.khqr-badge {
  background: #e11d48;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 5px;
  letter-spacing: 0.5px;
}

/* Form fields */
.payment-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-row {
  display: flex;
  flex-direction: column;
}

.input-lbl {
  font-size: 0.88rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 7px;
}

.txt-input {
  width: 100%;
  height: 44px;
  padding: 0 14px;
  border: 1.5px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.92rem;
  color: #111827;
  outline: none;
  background: #ffffff;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.txt-input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
}

.txt-input::placeholder {
  color: #9ca3af;
  font-size: 0.9rem;
}

.mt-10 {
  margin-top: 10px;
}

.form-row-three {
  display: flex;
  gap: 12px;
}

.col-card-num {
  flex: 2.2;
}

.col-exp {
  flex: 1.2;
}

.col-cvc {
  flex: 1.3;
}

.form-row-two {
  display: flex;
  gap: 14px;
}

.input-col {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Checkout CTA Button */
.checkout-submit-btn {
  margin-top: 14px;
  width: 100%;
  height: 48px;
  background: #1d4ed8;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  font-size: 1.02rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.1s ease;
}

.checkout-submit-btn:hover {
  background: #1e40af;
  transform: translateY(-1px);
}

.checkout-submit-btn:active {
  transform: translateY(0);
}

/* ==========================================================================
   SCREEN 2 & 3: FULLSCREEN GRADIENT PAGES
   ========================================================================== */
.fullscreen-gradient-step {
  min-height: 100vh;
  width: 100%;
  padding: 40px 48px 60px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  background: radial-gradient(130% 120% at 100% 100%, #ec4899 0%, #c026d3 32%, #7c3aed 68%, #380b6b 100%);
  color: #ffffff;
}

.fullscreen-gradient-step::after {
  content: '';
  position: absolute;
  width: 120%;
  height: 120%;
  right: -25%;
  bottom: -35%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(244, 63, 148, 0.45) 0%, rgba(192, 38, 211, 0.15) 50%, transparent 70%);
  pointer-events: none;
}

.confirm-top-bar {
  position: absolute;
  top: 40px;
  left: 48px;
  z-index: 5;
}

.centered-message-box {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  max-width: 680px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  padding: 0 20px;
}

.big-gradient-title {
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: -0.8px;
  line-height: 1.15;
  color: #ffffff;
}

.big-gradient-title.success-headline {
  font-size: 3.8rem;
}

.target-entity {
  margin-top: 12px;
  font-size: 1.25rem;
  font-weight: 700;
  color: #ffffff;
}

.confirm-instruction {
  margin-top: 16px;
  font-size: 1.05rem;
  color: rgba(255, 255, 255, 0.92);
  line-height: 1.5;
}

.success-hint {
  margin-top: 14px;
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.92);
}

.frosted-pill-btn {
  margin-top: 32px;
  width: 380px;
  max-width: 90vw;
  height: 50px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.4);
  color: #ffffff;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.frosted-pill-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.48);
  transform: translateY(-2px);
}

.frosted-pill-btn:disabled {
  opacity: 0.8;
  cursor: not-allowed;
}

.spinner-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.spin-circle {
  width: 22px;
  height: 22px;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* ==========================================================================
   SCREEN 4: RECEIPT CARD MODAL
   ========================================================================== */
.receipt-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(15, 23, 42, 0.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.receipt-card-container {
  background: #ffffff;
  border-radius: 18px;
  border: 2px solid #a855f7;
  box-shadow: 0 25px 60px -10px rgba(0, 0, 0, 0.35);
  width: 100%;
  max-width: 640px;
  overflow: hidden;
  animation: popIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes popIn {
  from {
    opacity: 0;
    transform: scale(0.92) translateY(12px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

/* Purple header banner */
.receipt-header-banner {
  background: #b01b92;
  padding: 34px 24px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
}

.white-check-circle {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  border: 3px solid #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

.receipt-title {
  font-size: 1.85rem;
  font-weight: 700;
  letter-spacing: -0.3px;
  color: #ffffff;
}

/* Card body */
.receipt-card-body {
  padding: 28px 36px 32px;
  background: #ffffff;
}

.receipt-meta-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding-bottom: 20px;
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.meta-label {
  font-size: 0.78rem;
  color: #64748b;
  font-weight: 500;
}

.meta-val {
  font-size: 0.95rem;
  color: #0f172a;
  font-weight: 700;
}

.receipt-divider {
  height: 1px;
  background: #e2e8f0;
  margin-bottom: 20px;
}

/* Inner Gray Box */
.room-summary-box {
  background: #f1f5f9;
  border-radius: 10px;
  padding: 18px 22px;
  border: 1px solid #e2e8f0;
}

.room-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.room-title-col, .room-date-col {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.room-date-col {
  text-align: right;
}

.box-small-lbl {
  font-size: 0.76rem;
  color: #64748b;
  font-weight: 500;
}

.box-main-val {
  font-size: 1rem;
  font-weight: 700;
  color: #0f172a;
}

.box-inner-divider {
  height: 1px;
  background: #cbd5e1;
  margin: 16px 0 14px;
}

.room-amount-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-amount-lbl {
  font-size: 0.92rem;
  color: #334155;
  font-weight: 600;
}

.box-amount-val {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0f172a;
}

/* Receipt Actions */
.receipt-actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.receipt-btn {
  flex: 1;
  height: 44px;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.15s ease;
}

.receipt-btn.secondary {
  background: #f1f5f9;
  color: #334155;
  border: 1px solid #cbd5e1;
}

.receipt-btn.secondary:hover {
  background: #e2e8f0;
}

.receipt-btn.primary {
  background: #1d4ed8;
  color: #ffffff;
  border: none;
}

.receipt-btn.primary:hover {
  background: #1e40af;
}

/* ==========================================================================
   RESPONSIVE DESIGN
   ========================================================================== */
@media (max-width: 900px) {
  .split-checkout-layout {
    flex-direction: column;
  }
  .left-hero, .right-form-panel {
    flex: 1 0 auto;
    width: 100%;
    min-height: auto;
    padding: 30px 24px;
  }
  .plan-price {
    font-size: 2.4rem;
  }
  .big-gradient-title {
    font-size: 2.4rem;
  }
  .big-gradient-title.success-headline {
    font-size: 2.6rem;
  }
  .receipt-meta-grid {
    grid-template-columns: repeat(2, 1fr);
    row-gap: 14px;
  }
}
</style>
