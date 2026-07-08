<template>
  <div class="verify-account-page">
    <!-- Dev / QA Testing Tools -->
    <div class="dev-nav-panel">
      <span class="dev-label">🛠️ Step Bypass:</span>
      <button class="dev-btn" @click="currentStep = 1" :class="{ active: currentStep === 1 }">1. ID Upload</button>
      <button class="dev-btn" @click="currentStep = 2" :class="{ active: currentStep === 2 }">2. Face Match</button>
      <button class="dev-btn" @click="currentStep = 3" :class="{ active: currentStep === 3 }">3. Liveness Scan</button>
      <button class="dev-btn" @click="currentStep = 4" :class="{ active: currentStep === 4 }">4. Success</button>
    </div>

    <header class="top-nav">
      <button class="back-btn" type="button" @click="goBack">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
      </button>
      <h1 class="page-title">Identity Verification</h1>
      <div class="placeholder-spacer"></div>
    </header>

    <!-- Progress Indicator -->
    <div class="progress-bar-container" v-if="currentStep <= 3">
      <div class="progress-steps">
        <div class="step" :class="{ active: currentStep >= 1, completed: currentStep > 1 }">
          <div class="step-icon">1</div>
          <span>ID Upload</span>
        </div>
        <div class="step-line" :class="{ active: currentStep >= 2 }"></div>
        <div class="step" :class="{ active: currentStep >= 2, completed: currentStep > 2 }">
          <div class="step-icon">2</div>
          <span>Face Match</span>
        </div>
        <div class="step-line" :class="{ active: currentStep >= 3 }"></div>
        <div class="step" :class="{ active: currentStep >= 3, completed: currentStep > 3 }">
          <div class="step-icon">3</div>
          <span>Liveness Scan</span>
        </div>
      </div>
    </div>

    <!-- Loading Models State -->
    <div v-if="!isModelsLoaded" class="loading-overlay">
      <div class="spinner"></div>
      <p style="margin-top: 16px; font-weight: 500; color: #555;">Loading AI Models...</p>
    </div>

    <main class="content" v-else>
      <!-- Step 1: ID Card Upload and Google Cloud Vision OCR -->
      <IdUploadStep 
        v-if="currentStep === 1" 
        @complete="handleIdComplete" 
      />
      <!-- Step 2: Biometric Selfie Face Match against the ID Card face -->
      <FaceMatchStep 
        v-else-if="currentStep === 2" 
        :idPreview="idPreview" 
        @complete="handleFaceMatchComplete" 
      />
      <!-- Step 3: Interactive Liveness detection (head turn/pose logic) -->
      <LivenessScanStep 
        v-else-if="currentStep === 3" 
        @complete="handleLivenessComplete" 
      />
      <!-- Step 4: Verification Success Screen -->
      <SuccessStep 
        v-else-if="currentStep === 4" 
      />
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import * as faceapi from 'face-api.js'
import { auth, db } from '../../firebase'
import { onAuthStateChanged } from 'firebase/auth'
import { collection, addDoc, doc, setDoc } from 'firebase/firestore'

// Import Subcomponents for the modular verification steps
import IdUploadStep from '../../components/verification/IdUploadStep.vue'
import FaceMatchStep from '../../components/verification/FaceMatchStep.vue'
import LivenessScanStep from '../../components/verification/LivenessScanStep.vue'
import SuccessStep from '../../components/verification/SuccessStep.vue'

const router = useRouter()
const currentStep = ref(1)
const isModelsLoaded = ref(false)

// Shared flow states
const idPreview = ref(null)
const idParsedData = ref(null)

onMounted(async () => {
  // Override global body lock & #app height limits for natural mobile scroll
  document.body.style.overflow = 'initial'
  const appEl = document.getElementById('app')
  if (appEl) {
    appEl.style.height = 'auto'
    appEl.style.minHeight = '100vh'
  }

  // Enforce Login
  onAuthStateChanged(auth, (user) => {
    if (!user) {
      alert("You must be logged in to verify your account!");
      router.push('/login');
    }
  });

  try {
    // Load models from public/models (which we downloaded)
    await Promise.all([
      faceapi.nets.ssdMobilenetv1.loadFromUri('/models'),
      faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
      faceapi.nets.faceRecognitionNet.loadFromUri('/models')
    ])
    isModelsLoaded.value = true
  } catch(e) {
    console.error("Error loading face-api models", e)
    alert("Failed to load AI models. Please ensure they are in public/models/")
  }
})

function goBack() {
  if (currentStep.value > 1 && currentStep.value <= 3) {
    currentStep.value--
  } else {
    router.push('/home')
  }
}

// Flow step transitions and state synchronization
function handleIdComplete(payload) {
  idPreview.value = payload.idPreview
  idParsedData.value = payload.idParsedData
  currentStep.value = 2
}

function handleFaceMatchComplete() {
  currentStep.value = 3
}

async function handleLivenessComplete() {
  // Save verified details to Firebase
  try {
    if (auth.currentUser) {
      const uid = auth.currentUser.uid;
      
      const payload = {
        userId: uid,
        verifiedAt: new Date().toISOString()
      };

      if (idParsedData.value) {
        payload.idNumber = idParsedData.value.idNumber || null;
        payload.sex = idParsedData.value.sex || null;
        payload.nationality = idParsedData.value.nationality || null;
        
        // Parse dates safely to ISO strings
        if (idParsedData.value.dob) {
          payload.dob = typeof idParsedData.value.dob.toISOString === 'function' 
            ? idParsedData.value.dob.toISOString() 
            : new Date(idParsedData.value.dob).toISOString();
        }
        if (idParsedData.value.expiryDate) {
          payload.expiryDate = typeof idParsedData.value.expiryDate.toISOString === 'function'
            ? idParsedData.value.expiryDate.toISOString()
            : new Date(idParsedData.value.expiryDate).toISOString();
        }
      }

      // 1. Audit Log: Save to verified_users
      await addDoc(collection(db, "verified_users"), payload);

      // 2. Profile Sync: Update main users collection to remove home warning banner
      await setDoc(doc(db, "users", uid), {
        verificationStatus: 'verified',
        idNumber: payload.idNumber || 'Verified',
        verifiedAt: new Date().toISOString()
      }, { merge: true });
    }
  } catch (err) {
    console.error("Error saving verification state to Firebase:", err)
  }

  currentStep.value = 4
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.verify-account-page {
  display: flex; flex-direction: column; min-height: 100vh; width: 100%;
  background: #f8fafc; font-family: 'Inter', sans-serif;
}

/* QA Dev Controls */
.dev-nav-panel {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
  padding: 8px 16px;
  background: #0f172a;
  color: #e2e8f0;
  border-bottom: 2px solid #334155;
  font-family: monospace;
  font-size: 0.8rem;
}
.dev-label {
  font-weight: 600;
  color: #fb923c;
}
.dev-btn {
  background: #1e293b;
  color: #e2e8f0;
  border: 1px solid #475569;
  padding: 4px 10px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.75rem;
  transition: all 0.2s ease;
}
.dev-btn:hover {
  background: #334155;
  color: #f472b6;
}
.dev-btn.active {
  background: #10b981;
  color: #ffffff;
  border-color: #10b981;
  font-weight: bold;
}

.top-nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 20px; border-bottom: none; background: #5C4E4E;
}
.back-btn { background: none; border: none; cursor: pointer; color: #fff; display: flex; align-items: center; justify-content: center; }
.page-title { font-size: 1.1rem; font-weight: 600; color: #fff; }
.placeholder-spacer { width: 24px; }

/* Progress Bar */
.progress-bar-container { padding: 20px; background: #fff; border-bottom: 1px solid #e2e8f0; }
.progress-steps { display: flex; align-items: center; justify-content: space-between; max-width: 400px; margin: 0 auto; }
.step { display: flex; flex-direction: column; align-items: center; gap: 8px; color: #94a3b8; transition: 0.3s; }
.step.active { color: #0f172a; }
.step.completed .step-icon { background: #0f172a; color: #fff; border-color: #0f172a; }
.step-icon { 
  width: 32px; height: 32px; border-radius: 50%; border: 2px solid #cbd5e1;
  display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.9rem; transition: 0.3s;
}
.step.active .step-icon { border-color: #0f172a; color: #0f172a; }
.step span { font-size: 0.8rem; font-weight: 500; }
.step-line { flex: 1; height: 2px; background: #e2e8f0; margin: 0 10px; position: relative; top: -10px; transition: 0.3s; }
.step-line.active { background: #0f172a; }

.content { flex: 1; padding: 24px 20px; -webkit-overflow-scrolling: touch; }
.step-section { max-width: 500px; margin: 0 auto; animation: fadeIn 0.3s ease; display: flex; flex-direction: column; gap: 16px; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

.section-title { font-size: 1.3rem; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-align: center; }
.section-subtitle { font-size: 0.95rem; color: #475569; margin-bottom: 12px; line-height: 1.5; text-align: center; }

.upload-box {
  width: 100%; height: 200px; border: 2px dashed #cbd5e1; border-radius: 16px;
  display: flex; align-items: center; justify-content: center; cursor: pointer;
  background: #ffffff; transition: 0.2s; overflow: hidden;
}
.upload-box:hover { border-color: #94a3b8; background: #f8fafc; }
.hidden-input { display: none; }
.upload-placeholder { display: flex; flex-direction: column; align-items: center; gap: 12px; color: #64748b; font-size: 0.95rem; font-weight: 500; }
.preview-container { width: 100%; height: 100%; }
.preview-image { width: 100%; height: 100%; object-fit: contain; background: #0f172a; }

/* Guidelines Cards */
.guidelines-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}
.guide-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #334155;
  margin-bottom: 12px;
}
.guide-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.guide-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  font-weight: 500;
}
.guide-item.good {
  color: #047857;
}
.guide-item.bad {
  color: #b91c1c;
}
.guide-item .icon {
  flex-shrink: 0;
}

/* Guidelines Cards Visual Examples */
.visual-examples {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}
.example-box {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.example-box .img-wrapper {
  width: 100%;
  height: 120px;
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid #e2e8f0;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
}
.example-box.acceptable .img-wrapper {
  border-color: #a7f3d0;
}
.example-box.declined .img-wrapper {
  border-color: #fecaca;
}
.example-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transform: scale(1.15);
  mix-blend-mode: multiply;
}
.example-box .label {
  font-size: 0.75rem;
  font-weight: 600;
}
.example-box.acceptable .label {
  color: #059669;
}
.example-box.declined .label {
  color: #dc2626;
}

/* Liveness Guide Panel & Animations */
.liveness-guide-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}
.guide-anim-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}
.animation-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
}
.anim-avatar {
  width: 70px;
  height: 70px;
}
.avatar-svg {
  width: 100%;
  height: 100%;
}
.anim-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #4f46e5;
}
.text-success {
  color: #10b981 !important;
}

/* Eye Blink Keyframes */
@keyframes blink {
  0%, 90%, 100% {
    ry: 5px;
    fill: #1e1b4b;
  }
  95% {
    ry: 1px;
    fill: #475569;
  }
}
.eye-blink {
  animation: blink 2s infinite;
  transform-origin: center;
}

/* Head Turn Keyframes */
@keyframes turnFace {
  0%, 100% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-10px);
  }
  75% {
    transform: translateX(10px);
  }
}
.facial-features-turn {
  animation: turnFace 3.5s infinite ease-in-out;
  transform-origin: center;
}

/* Scale Up for Success */
.scale-up {
  animation: scaleUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
@keyframes scaleUp {
  from { transform: scale(0.8); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.btn-primary {
  width: 100%; padding: 14px; background: #5C4E4E; color: #fff;
  border: none; border-radius: 12px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: 0.2s;
}
.btn-primary:disabled { background: #cbd5e1; color: #94a3b8; cursor: not-allowed; }
.btn-primary:active:not(:disabled) { transform: scale(0.98); }

.btn-secondary {
  width: 100%; padding: 14px; background: #f1f5f9; color: #0f172a;
  border: none; border-radius: 12px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: 0.2s;
}
.btn-secondary:active { transform: scale(0.98); background: #e2e8f0; }

/* Result boxes */
.result-box { padding: 16px; background: #f8fafc; border-radius: 12px; border: 1px solid #e2e8f0; }
.result-box h3 { margin-bottom: 12px; font-size: 1rem; color: #0f172a; }
.error-box { background: #fef2f2; padding: 12px; border-radius: 8px; border: 1px solid #fecaca; }
.error-box ul { margin-left: 20px; color: #dc2626; font-size: 0.9rem; }
.error-box p { color: #dc2626; font-weight: 500; font-size: 0.9rem; }
.success-box { background: #ecfdf5; padding: 12px; border-radius: 8px; border: 1px solid #a7f3d0; color: #059669; font-weight: 600; text-align: center; }
.auto-advance-msg { text-align: center; color: #64748b; font-size: 0.95rem; margin-top: 16px; font-weight: 500; animation: pulse 1.5s infinite; }
@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }

.extracted-data { background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 12px; }
.extracted-data h4 { margin-bottom: 12px; font-size: 0.95rem; color: #334155; }
.extracted-data p { font-size: 0.9rem; margin-bottom: 6px; color: #475569; }

/* Camera Liveness */
.camera-container {
  position: relative; width: 100%; height: 320px; background: #000; border-radius: 16px; overflow: hidden;
}
.camera-video { width: 100%; height: 100%; object-fit: cover; transform: scaleX(-1); }
.camera-overlay {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center;
  pointer-events: none;
}
.oval-cutout {
  width: 180px; height: 250px; border-radius: 50%;
  box-shadow: 0 0 0 9999px rgba(0,0,0,0.5);
  border: 2px dashed rgba(255,255,255,0.6);
}
.id-cutout {
  width: 85%; aspect-ratio: 1.58; border-radius: 8px;
  box-shadow: 0 0 0 9999px rgba(0,0,0,0.5);
  border: 2px dashed rgba(255,255,255,0.8);
}
.liveness-msg {
  position: absolute; top: 16px; left: 20px; right: 20px; bottom: auto;
  background: rgba(255,255,255,0.95); color: #0f172a; padding: 12px; border-radius: 8px;
  text-align: center; font-weight: 600; font-size: 0.95rem; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* Success Screen & Card */
.success-screen {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  padding: 24px 20px;
  animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.success-card {
  width: 100%;
  max-width: 440px;
  background: #ffffff;
  border-radius: 24px;
  padding: 36px 28px;
  box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.08);
  border: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  animation: slideUpIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes slideUpIn {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.success-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 8px;
}

.success-subtitle {
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.5;
  margin-bottom: 12px;
}

/* Success Badge & Pulse Animation */
.success-badge-wrapper {
  position: relative;
  width: 90px;
  height: 90px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.success-badge {
  width: 80px;
  height: 80px;
  z-index: 2;
  border-radius: 50%;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.badge-check-svg {
  width: 100%;
  height: 100%;
}

.pulse-ring {
  position: absolute;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(16, 185, 129, 0.15);
  animation: pulseRing 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
  z-index: 1;
}

@keyframes pulseRing {
  0% {
    transform: scale(0.95);
    opacity: 1;
  }
  100% {
    transform: scale(1.6);
    opacity: 0;
  }
}

/* Drawing checkmark animation */
.check-draw {
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  animation: drawCheck 0.6s 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes drawCheck {
  to {
    stroke-dashoffset: 0;
  }
}

/* Verification Details */
.verification-details-box {
  width: 100%;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 18px 16px;
  margin: 16px 0 24px 0;
  text-align: left;
}

.details-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 14px;
}

.details-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.detail-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
}

.detail-item .icon {
  color: #10b981;
  font-weight: 700;
  margin-right: 6px;
}

.detail-item .label {
  color: #475569;
  font-weight: 500;
  flex: 1;
}

.detail-item .value.success {
  color: #059669;
  font-weight: 600;
  background: #ecfdf5;
  padding: 2px 8px;
  border-radius: 9999px;
  font-size: 0.75rem;
}

.security-seal {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid #e2e8f0;
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 500;
}

.shield-icon {
  width: 14px;
  height: 14px;
  color: #4f46e5;
}

.action-buttons {
  width: 100%;
}

/* Loading Spinner */
.loading-overlay { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; }
.spinner { width: 40px; height: 40px; border: 4px solid #f1f5f9; border-top: 4px solid #0f172a; border-radius: 50%; animation: spin 1s linear infinite; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

/* Liveness Flash */
.camera-container::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: 16px;
  pointer-events: none;
  z-index: 10;
  box-shadow: inset 0 0 0 0 rgba(16, 185, 129, 0);
}

.camera-container.flash-green::after {
  animation: flashSuccess 0.6s ease-out;
}

@keyframes flashSuccess {
  0% { box-shadow: inset 0 0 0 0 rgba(16, 185, 129, 0); }
  15% { box-shadow: inset 0 0 0 8px #10b981, inset 0 0 50px 15px rgba(16, 185, 129, 0.7); }
  100% { box-shadow: inset 0 0 0 0 rgba(16, 185, 129, 0); }
}
</style>
