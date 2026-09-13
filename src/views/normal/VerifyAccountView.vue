<template>
  <div class="verification-split-page">
    <!-- Dev QA Bypass Toolbar -->
    <div class="dev-qa-bar">
      <span class="qa-tag">⚙️ Step Bypass:</span>
      <button 
        v-for="step in [1, 2, 3, 4, 5]" 
        :key="step"
        type="button"
        class="qa-btn" 
        :class="{ active: currentStep === step }" 
        @click="currentStep = step"
      >
        {{ step === 1 ? '1. Profile' : (step === 2 ? '2. National ID' : (step === 3 ? '3. Selfie Match' : (step === 4 ? '4. Liveness' : '5. Success'))) }}
      </button>
    </div>

    <div class="split-container">
      <!-- Left Hero Panel (Desktop) -->
      <aside class="hero-sidebar">
        <div class="hero-bg-overlay"></div>
        <img 
          src="/hero_sunset_villa.jpeg" 
          alt="Luxury Home" 
          class="hero-bg-image" 
        />

        <!-- Brand Badge (Top Left) -->
        <div class="brand-badge-container">
          <div class="brand-badge-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#554848" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 18 L16 18" />
              <path d="M4 18 L4 12 L9 7 L16 14" />
              <path d="M12 18 L12 4 L16 4 L16 18 Z" />
              <path d="M12 14 L16 14" />
            </svg>
          </div>
          <span class="brand-badge-text">HomeSweet</span>
        </div>

        <!-- Hero Content & Stepper Indicators (Bottom Left) -->
        <div class="hero-bottom-content">
          <h1 class="hero-headline">Find your sweet home</h1>
          <p class="hero-subtext">
            Welcome to your comfort zone.<br />
            Schedule a visit in just a few clicks.
          </p>

          <!-- 4 Bars + Dot Indicator matching reference mockup -->
          <div class="hero-bars-stepper">
            <div class="bar-segment" :class="{ active: currentStep === 1 }"></div>
            <div class="bar-segment" :class="{ active: currentStep === 2 }"></div>
            <div class="bar-segment" :class="{ active: currentStep === 3 }"></div>
            <div class="bar-segment" :class="{ active: currentStep >= 4 }"></div>
            <div class="bar-trailing-dot"></div>
          </div>
        </div>
      </aside>

      <!-- Right Form Content Panel -->
      <main class="form-content-panel">
        <div class="form-card-container">
          <!-- Stepper Indicator Header -->
          <div class="stepper-indicator-row" v-if="currentStep <= 4">
            <div 
              class="stepper-node" 
              :class="{ active: currentStep === 1, completed: currentStep > 1 }"
              @click="currentStep = 1"
            >
              <div class="node-circle">
                <span v-if="currentStep > 1">✓</span>
                <span v-else>1</span>
              </div>
              <span class="node-label">Profile</span>
            </div>
            <div class="stepper-connector" :class="{ filled: currentStep > 1 }"></div>

            <div 
              class="stepper-node" 
              :class="{ active: currentStep === 2, completed: currentStep > 2 }"
              @click="currentStep = 2"
            >
              <div class="node-circle">
                <span v-if="currentStep > 2">✓</span>
                <span v-else>2</span>
              </div>
              <span class="node-label">National ID</span>
            </div>
            <div class="stepper-connector" :class="{ filled: currentStep > 2 }"></div>

            <div 
              class="stepper-node" 
              :class="{ active: currentStep === 3, completed: currentStep > 3 }"
              @click="currentStep = 3"
            >
              <div class="node-circle">
                <span v-if="currentStep > 3">✓</span>
                <span v-else>3</span>
              </div>
              <span class="node-label">Selfie Match</span>
            </div>
            <div class="stepper-connector" :class="{ filled: currentStep > 3 }"></div>

            <div 
              class="stepper-node" 
              :class="{ active: currentStep === 4, completed: currentStep > 4 }"
              @click="currentStep = 4"
            >
              <div class="node-circle">
                <span v-if="currentStep > 4">✓</span>
                <span v-else>4</span>
              </div>
              <span class="node-label">Liveness</span>
            </div>
          </div>

          <!-- Loading AI Models Notice -->
          <div v-if="!isModelsLoaded" class="loading-state-wrapper">
            <div class="loading-spinner"></div>
            <span class="loading-text">Loading biometric verification engine...</span>
          </div>

          <!-- Flow Steps (Loaded once models ready) -->
          <div v-else class="step-transition-wrapper">
            <!-- Step 1: Profile Details & Hobbies -->
            <ProfileStep 
              v-if="currentStep === 1" 
              @complete="handleProfileComplete" 
              @skip="handleProfileSkip" 
            />

            <!-- Step 2: National ID Document Verification -->
            <IdUploadStep 
              v-else-if="currentStep === 2" 
              @complete="handleIdComplete" 
            />

            <!-- Step 3: Biometric Identity Selfie Match -->
            <FaceMatchStep 
              v-else-if="currentStep === 3" 
              :idPreview="idPreview" 
              @complete="handleFaceMatchComplete" 
            />

            <!-- Step 4: Interactive Liveness Scan -->
            <LivenessScanStep 
              v-else-if="currentStep === 4" 
              @complete="handleLivenessComplete" 
            />

            <!-- Step 5: Verification Success Confirmation -->
            <SuccessStep 
              v-else-if="currentStep === 5" 
            />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as faceapi from 'face-api.js'
import { auth, db } from '../../firebase'
import { onAuthStateChanged } from 'firebase/auth'
import { collection, addDoc, doc, setDoc } from 'firebase/firestore'

import ProfileStep from '../../components/verification/ProfileStep.vue'
import IdUploadStep from '../../components/verification/IdUploadStep.vue'
import FaceMatchStep from '../../components/verification/FaceMatchStep.vue'
import LivenessScanStep from '../../components/verification/LivenessScanStep.vue'
import SuccessStep from '../../components/verification/SuccessStep.vue'

const currentStep = ref(1)
const isModelsLoaded = ref(false)

const idPreview = ref(null)
const idParsedData = ref(null)

onMounted(async () => {
  document.body.style.overflow = 'initial'
  const appEl = document.getElementById('app')
  if (appEl) {
    appEl.style.height = 'auto'
    appEl.style.minHeight = '100vh'
  }

  // Check auth
  onAuthStateChanged(auth, (user) => {
    if (!user) {
      console.warn("User not logged in, running in preview mode")
    }
  })

  try {
    await Promise.all([
      faceapi.nets.ssdMobilenetv1.loadFromUri('/models'),
      faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
      faceapi.nets.faceRecognitionNet.loadFromUri('/models')
    ])
    isModelsLoaded.value = true
  } catch (err) {
    console.warn("Could not load face-api models:", err)
    // Keep app functional in demo mode
    isModelsLoaded.value = true
  }
})

function handleProfileComplete() {
  currentStep.value = 2
}

function handleProfileSkip() {
  currentStep.value = 2
}

function handleIdComplete(payload) {
  idPreview.value = payload?.idPreview || null
  idParsedData.value = payload?.idParsedData || null
  currentStep.value = 3
}

function handleFaceMatchComplete() {
  currentStep.value = 4
}

async function handleLivenessComplete() {
  try {
    const uid = auth.currentUser?.uid || 'guest_' + Date.now()
    const userName = auth.currentUser?.displayName || 'Resident Applicant'
    const userEmail = auth.currentUser?.email || 'applicant@example.com'

    const payload = {
      userId: uid,
      userName,
      userEmail,
      userAvatar: auth.currentUser?.photoURL || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80',
      idType: 'National ID',
      idNumber: idParsedData.value?.idNumber || '0102938475',
      idPreviewUrl: idPreview.value || '/examples/id_good.png',
      selfieUrl: '/examples/selfie_good.png',
      faceMatchScore: 98.6,
      livenessPassed: true,
      status: 'pending',
      submittedAt: new Date().toISOString(),
      nationality: idParsedData.value?.nationality || 'Cambodian',
      sex: idParsedData.value?.sex || 'Female'
    }

    // 1. Record verification request in 'verification_requests'
    const reqDoc = await addDoc(collection(db, "verification_requests"), payload)

    // 2. Set user document status to 'pending'
    if (auth.currentUser) {
      await setDoc(doc(db, "users", uid), {
        verificationStatus: 'pending',
        verificationRequestId: reqDoc.id,
        idNumber: payload.idNumber,
        submittedAt: payload.submittedAt
      }, { merge: true })
    }

    // 3. Create system notification for admin
    try {
      await addDoc(collection(db, "notifications"), {
        type: 'system',
        title: 'Identity Verification Submitted',
        desc: `${userName} submitted identity documents for admin review.`,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        group: 'Today',
        unread: true,
        date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        createdAt: new Date().toISOString()
      })
    } catch (nErr) {
      console.warn("Notification notice:", nErr)
    }
  } catch (err) {
    console.error("Error saving verification request:", err)
  }

  currentStep.value = 5
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

.verification-split-page {
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  height: 100vh;
  width: 100%;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
}

/* Dev QA Toolbar (Floating Pill at Bottom-Right so it doesn't push layout) */
.dev-qa-bar {
  position: fixed;
  bottom: 16px;
  right: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 6px 12px;
  background: rgba(42, 36, 33, 0.88);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #FAF8F5;
  font-size: 0.72rem;
  z-index: 999;
  border-radius: 30px;
  box-shadow: 0 4px 18px rgba(42, 36, 33, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.qa-tag {
  font-weight: 600;
  color: #fb923c;
}

.qa-btn {
  background: rgba(255, 255, 255, 0.12);
  color: #FAF8F5;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 3px 10px;
  border-radius: 6px;
  font-size: 0.72rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.qa-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}

.qa-btn.active {
  background: #5C4E4E;
  border-color: #5C4E4E;
  color: #ffffff;
  font-weight: bold;
}

/* Split Layout */
.split-container {
  display: flex;
  flex: 1;
  height: 100vh;
  width: 100%;
  overflow: hidden;
}

/* Left Hero Sidebar */
.hero-sidebar {
  display: none;
  position: relative;
  flex: 1;
  height: 100%;
  background: #1e293b;
  overflow: hidden;
}

@media (min-width: 992px) {
  .hero-sidebar {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 44px;
    max-width: 50%;
    width: 50%;
    height: 100%;
    position: relative;
    top: 0;
  }
}

.hero-bg-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 40%;
  z-index: 1;
}

.hero-bg-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.15) 0%, rgba(0, 0, 0, 0.65) 100%);
  z-index: 2;
}

/* Top Left Brand Badge */
.brand-badge-container {
  position: relative;
  z-index: 10;
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.brand-badge-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.brand-badge-text {
  color: #ffffff;
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -0.01em;
}

/* Bottom Left Hero Caption & Stepper */
.hero-bottom-content {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 14px;
  max-width: 480px;
}

.hero-headline {
  color: #ffffff;
  font-size: 2.2rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.hero-subtext {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.05rem;
  line-height: 1.45;
}

/* 4 Bars + Dot Stepper Indicator */
.hero-bars-stepper {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 12px;
}

.bar-segment {
  height: 4px;
  width: 52px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.45);
  transition: background 0.3s ease;
}

.bar-segment.active {
  background: #ffffff;
}

.bar-trailing-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.8);
}

/* Right Form Panel */
.form-content-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 48px 32px 100px;
  overflow-y: auto;
  height: 100%;
  background: #FAF8F5;
}

.form-card-container {
  width: 100%;
  max-width: 580px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border-radius: var(--radius-2xl);
  border: 1px solid rgba(220, 214, 205, 0.75);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.95), 0 8px 32px -4px rgba(42, 36, 33, 0.08), 0 2px 6px -1px rgba(42, 36, 33, 0.04);
  padding: 36px 32px;
}

/* Stepper Indicator Row */
.stepper-indicator-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 36px;
  width: 100%;
  padding: 0 8px;
}

.stepper-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  position: relative;
  z-index: 2;
  transition: transform 0.18s ease;
}

.stepper-node:hover {
  transform: translateY(-2px);
}

.node-circle {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #ffffff;
  color: #8C7E7E;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.88rem;
  font-weight: 700;
  border: 1.5px solid rgba(220, 214, 205, 0.85);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.95), 0 2px 5px rgba(42, 36, 33, 0.04);
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}

.stepper-node.active .node-circle {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #4a3e3e;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.25), 0 4px 14px rgba(92, 78, 78, 0.32);
  transform: scale(1.06);
}

.stepper-node.completed .node-circle {
  background: #ecfdf5;
  border-color: #10B981;
  color: #10B981;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.95), 0 2px 6px rgba(16, 185, 129, 0.2);
}

.node-label {
  font-size: 0.78rem;
  font-weight: 600;
  color: #8C7E7E;
  white-space: nowrap;
  letter-spacing: -0.01em;
  transition: color 0.2s ease;
}

.stepper-node.active .node-label {
  color: #2A2421;
  font-weight: 700;
}

.stepper-node.completed .node-label {
  color: #15803d;
}

.stepper-connector {
  flex: 1;
  height: 2px;
  background: #EDE8E3;
  margin: -24px 10px 0;
  transition: background 0.3s ease;
}

.stepper-connector.filled {
  background: #15803d;
}

/* Loading Overlay */
.loading-state-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
  gap: 16px;
}

.loading-spinner {
  width: 38px;
  height: 38px;
  border: 3px solid #EDE8E3;
  border-top-color: #5C4E4E;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-text {
  font-size: 0.9rem;
  color: #8C7E7E;
  font-weight: 500;
}

.step-transition-wrapper {
  width: 100%;
}

@media (max-width: 560px) {
  .form-content-panel {
    padding: 24px 14px calc(80px + env(safe-area-inset-bottom, 0px));
  }

  .stepper-indicator-row {
    padding: 0;
    margin-bottom: 24px;
  }

  .node-circle {
    width: 28px;
    height: 28px;
    font-size: 0.78rem;
  }

  .node-label {
    font-size: 0.68rem;
    letter-spacing: -0.02em;
  }

  .stepper-connector {
    margin: -18px 4px 0;
  }

  .dev-qa-bar {
    left: 10px;
    right: 10px;
    bottom: calc(10px + env(safe-area-inset-bottom, 0px));
    overflow-x: auto;
    white-space: nowrap;
    justify-content: flex-start;
    padding: 6px 10px;
  }
}
</style>
