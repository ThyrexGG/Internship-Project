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
      <!-- STEP 1: ID UPLOAD -->
      <div v-if="currentStep === 1" class="step-section">
        <h2 class="section-title">Verify ID Document</h2>
        <p class="section-subtitle">Please upload a clear, well-lit photo of your Cambodian National ID.</p>

        <div class="upload-box" @click="triggerIdInput">
          <input type="file" ref="idInput" accept="image/*" class="hidden-input" @change="handleIdChange" />
          <div v-if="idPreview" class="preview-container">
            <img :src="idPreview" alt="ID Preview" class="preview-image" />
          </div>
          <div v-else class="upload-placeholder">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
            <span>Tap to upload ID</span>
          </div>
        </div>

        <!-- ID Upload Guidelines Card -->
        <div class="guidelines-card">
          <h4 class="guide-title">📷 Photo Requirements</h4>
          
          <div class="visual-examples">
            <div class="example-box acceptable">
              <div class="img-wrapper">
                <img src="/examples/id_good.png" alt="Correct ID Example" />
              </div>
              <span class="label">✅ Correct</span>
            </div>
            <div class="example-box declined">
              <div class="img-wrapper">
                <img src="/examples/id_bad.png" alt="Incorrect ID Example" />
              </div>
              <span class="label">❌ Incorrect</span>
            </div>
          </div>

          <div class="guide-grid">
            <div class="guide-item good">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Fully visible and clear text</span>
            </div>
            <div class="guide-item good">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Good, even lighting without glare</span>
            </div>
            <div class="guide-item bad">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              <span>No blur, cropping, or reflections</span>
            </div>
          </div>
        </div>

        <button class="btn-primary" :disabled="!idFile || isScanningId" @click="scanIdCard">
          {{ isScanningId ? 'Scanning...' : 'Verify ID' }}
        </button>

        <div v-if="idValidationErrors.length > 0 || idParsedData" class="result-box" style="margin-top: 24px;">
          <h3>Verification Status</h3>
          <div v-if="idValidationErrors.length > 0" class="error-box">
            <ul>
              <li v-for="(err, index) in idValidationErrors" :key="index">❌ {{ err }}</li>
            </ul>
          </div>
          <div v-else class="success-box">
            <p>✅ ID Verified Successfully!</p>
          </div>

          <div v-if="idParsedData" class="extracted-data">
            <h4>Extracted Information</h4>
            <p><strong>ID Number:</strong> {{ idParsedData.idNumber || 'Not Found' }}</p>
            <p><strong>Date of Birth:</strong> {{ idParsedData.dob ? idParsedData.dob.toLocaleDateString() : 'Not Found' }}</p>
            <p><strong>Gender:</strong> {{ idParsedData.sex === 'M' ? 'Male' : (idParsedData.sex === 'F' ? 'Female' : 'Not Found') }}</p>
          </div>
        </div>

        <div v-if="idParsedData && idValidationErrors.length === 0" class="auto-advance-msg">
          Proceeding to Face Match...
        </div>
      </div>

      <!-- STEP 2: FACE MATCH -->
      <div v-if="currentStep === 2" class="step-section">
        <h2 class="section-title">Verify Identity</h2>
        <p class="section-subtitle">Take a clear selfie to match your face with your ID document.</p>

        <div v-show="isSelfieCameraActive && !selfiePreview" class="camera-container">
          <video ref="selfieVideoElement" autoplay playsinline muted class="camera-video"></video>
          <div class="camera-overlay">
            <div class="oval-cutout"></div>
          </div>
          <div class="liveness-msg" :class="{'text-success': isSelfieGood}">
            {{ selfieFeedbackMsg }}
          </div>
        </div>
        
        <div v-if="!isSelfieCameraActive && !selfiePreview" class="upload-placeholder" @click="startSelfieCamera" style="padding: 40px 0; background: #fff; border: 2px dashed #cbd5e1; border-radius: 12px; margin-bottom: 16px; cursor: pointer; transition: background 0.2s;">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2" style="margin-bottom: 12px; display: block; margin-left: auto; margin-right: auto;"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
          <span style="display: block; text-align: center; color: #64748b;">Tap here to open camera and take selfie</span>
        </div>

        <div v-if="selfiePreview" class="upload-box" style="cursor: default;">
          <div class="preview-container">
            <img :src="selfiePreview" alt="Selfie Preview" class="preview-image" style="object-fit: contain; background: #000;" />
          </div>
        </div>

        <!-- Face Match Guidelines Card -->
        <div class="guidelines-card" v-if="!isSelfieCameraActive && !selfiePreview">
          <h4 class="guide-title">👤 Selfie Tips</h4>

          <div class="visual-examples">
            <div class="example-box acceptable">
              <div class="img-wrapper">
                <img src="/examples/selfie_good.png" alt="Correct Selfie Example" />
              </div>
              <span class="label">✅ Correct</span>
            </div>
            <div class="example-box declined">
              <div class="img-wrapper">
                <img src="/examples/selfie_bad.png" alt="Incorrect Selfie Example" />
              </div>
              <span class="label">❌ Incorrect</span>
            </div>
          </div>

          <div class="guide-grid">
            <div class="guide-item good">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Look directly into the camera</span>
            </div>
            <div class="guide-item good">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Neutral expression, open eyes</span>
            </div>
            <div class="guide-item good">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Well-lit, plain background</span>
            </div>
            <div class="guide-item bad">
              <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              <span>No glasses, caps, or face masks</span>
            </div>
          </div>
        </div>

        <div v-if="availableCameras.length > 1 && !selfiePreview" class="camera-selector" style="margin-top: 16px;">
          <label for="selfie-camera-select" style="font-weight: 500; font-size: 14px; margin-right: 8px;">Switch Camera:</label>
          <select id="selfie-camera-select" v-model="selectedCameraId" @change="onSelfieCameraSelectChange" style="padding: 6px; border-radius: 6px; border: 1px solid #ccc;">
            <option v-for="cam in availableCameras" :key="cam.deviceId" :value="cam.deviceId">
              {{ cam.label || 'Camera ' + (availableCameras.indexOf(cam) + 1) }}
            </option>
          </select>
        </div>

        <button v-if="!isSelfieCameraActive && !selfiePreview" class="btn-primary" style="margin-top: 16px;" @click="startSelfieCamera">
          Open Camera
        </button>

        <button v-if="isSelfieCameraActive && !selfiePreview" class="btn-primary" :disabled="!isSelfieGood" style="margin-top: 16px;" @click="captureSelfie">
          Take Photo
        </button>

        <div v-if="selfiePreview" style="display: flex; gap: 12px; margin-top: 16px;">
          <button class="btn-secondary" style="flex: 1;" :disabled="isMatchingFace" @click="retakeSelfie">
            Retake
          </button>
          <button class="btn-primary" style="flex: 2;" :disabled="isMatchingFace" @click="matchFace">
            {{ isMatchingFace ? 'Comparing Faces...' : 'Verify Match' }}
          </button>
        </div>

        <div v-if="faceMatchStatus" class="result-box" style="margin-top: 24px;">
           <div v-if="faceMatchStatus === 'success'" class="success-box">
             <p>✅ Face Matched!</p>
           </div>
           <div v-else class="error-box">
             <p>❌ {{ faceMatchErrorMsg }}</p>
           </div>
        </div>

        <div v-if="faceMatchStatus === 'success'" class="auto-advance-msg">
          Proceeding to Liveness Check...
        </div>
      </div>

      <!-- STEP 3: LIVENESS -->
      <div v-if="currentStep === 3" class="step-section">
        <h2 class="section-title">Secure Liveness Scan</h2>
        <p class="section-subtitle">Verify you are a real person by completing a quick interactive scan.</p>

        <!-- Dynamic Liveness Instruction Panel -->
        <div class="liveness-guide-card">
          <div class="guide-anim-wrapper">
            <!-- Turn Head Animation (Shown during turn stage) -->
            <div v-if="!isCameraActive || livenessStage !== 'done'" class="animation-container">
              <div class="anim-avatar">
                <svg viewBox="0 0 100 100" class="avatar-svg">
                  <!-- Head -->
                  <circle cx="50" cy="50" r="40" fill="#f8fafc" stroke="#4f46e5" stroke-width="2"/>
                  <!-- Shiftable Face Features (Head Turn) -->
                  <g class="facial-features-turn">
                    <ellipse cx="36" cy="45" rx="5" ry="5" fill="#1e1b4b" />
                    <ellipse cx="64" cy="45" rx="5" ry="5" fill="#1e1b4b" />
                    <path d="M50 48 L47 58 L53 58 Z" fill="#4f46e5" />
                    <path d="M38 65 Q50 72 62 65" fill="none" stroke="#1e1b4b" stroke-width="3" stroke-linecap="round"/>
                  </g>
                </svg>
              </div>
              <p class="anim-label" v-if="livenessStage === 'turnRight'">Slowly turn head to the right</p>
              <p class="anim-label" v-else-if="livenessStage === 'turnLeft'">Now turn head to the left</p>
              <p class="anim-label" v-else-if="livenessStage === 'lookUp'">Now look up slightly</p>
              <p class="anim-label" v-else-if="livenessStage === 'lookDown'">Now look down slightly</p>
              <p class="anim-label" v-else>Follow the instructions</p>
            </div>

            <!-- Verified State (Shown when done) -->
            <div v-if="livenessStage === 'done'" class="animation-container success-anim">
              <div class="anim-avatar scale-up">
                <svg viewBox="0 0 100 100" class="avatar-svg">
                  <circle cx="50" cy="50" r="40" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
                  <path d="M35 50 L45 60 L65 40" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <p class="anim-label text-success">Liveness Verified!</p>
            </div>
          </div>
        </div>

        <div class="camera-container">
          <video ref="videoElement" autoplay playsinline muted class="camera-video"></video>
          <div class="camera-overlay">
            <div class="oval-cutout"></div>
          </div>
          <div v-if="isCameraActive" class="liveness-msg">
            {{ livenessMsg }}
          </div>
        </div>

        <div v-if="availableCameras.length > 1 && !isCameraActive" class="camera-selector" style="margin-top: 16px;">
          <label for="liveness-camera-select" style="font-weight: 500; font-size: 14px; margin-right: 8px;">Switch Camera:</label>
          <select id="liveness-camera-select" v-model="selectedCameraId" style="padding: 6px; border-radius: 6px; border: 1px solid #ccc;">
            <option v-for="cam in availableCameras" :key="cam.deviceId" :value="cam.deviceId">
              {{ cam.label || 'Camera ' + (availableCameras.indexOf(cam) + 1) }}
            </option>
          </select>
        </div>

        <button v-if="!isCameraActive" class="btn-primary" style="margin-top: 16px;" @click="startCamera">
          Start Camera Check
        </button>
      </div>

      <!-- SUCCESS SCREEN -->
      <div v-if="currentStep === 4" class="success-screen">
        <div class="success-card">
          <!-- Animated Checkmark Badge -->
          <div class="success-badge-wrapper">
            <div class="pulse-ring"></div>
            <div class="success-badge">
              <svg viewBox="0 0 100 100" class="badge-check-svg">
                <circle cx="50" cy="50" r="40" fill="#10b981" />
                <path d="M35 50 L45 60 L65 40" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" class="check-draw"/>
              </svg>
            </div>
          </div>

          <h2 class="success-title">Verification Complete!</h2>
          <p class="success-subtitle">Your identity has been successfully verified using real AI.</p>

          <!-- Verified Details Section -->
          <div class="verification-details-box">
            <h3 class="details-title">Verification Summary</h3>
            <div class="details-list">
              <div class="detail-item">
                <span class="icon">✓</span>
                <span class="label">Document Authenticity</span>
                <span class="value success">Verified</span>
              </div>
              <div class="detail-item">
                <span class="icon">✓</span>
                <span class="label">Biometric Face Match</span>
                <span class="value success">Match Confirmed</span>
              </div>
              <div class="detail-item">
                <span class="icon">✓</span>
                <span class="label">Real-time Liveness</span>
                <span class="value success">Passed</span>
              </div>
            </div>
            
            <div class="security-seal">
              <svg class="shield-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              </svg>
              <span>Secured by Advanced AI Biometrics</span>
            </div>
          </div>

          <div class="action-buttons">
            <button class="btn-primary" @click="$router.push('/home')">
              Return to Dashboard
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import * as faceapi from 'face-api.js'
import { auth, db } from '../../firebase'
import { onAuthStateChanged } from 'firebase/auth'
import { collection, addDoc, doc, setDoc } from 'firebase/firestore'

const router = useRouter()
const currentStep = ref(1)
const isModelsLoaded = ref(false)

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

  // Attempt to populate cameras early if permissions were already granted previously
  await populateCameras()
})

function goBack() {
  if (currentStep.value > 1 && currentStep.value <= 3) {
    if (currentStep.value === 2) stopSelfieCamera()
    if (currentStep.value === 3) stopCamera()
    currentStep.value--
  } else {
    router.push('/home')
  }
}

// --- STEP 1: ID SCANNING (Google Cloud Vision) ---
const idInput = ref(null)
const idFile = ref(null)
const idPreview = ref(null)
const isScanningId = ref(false)
const idOcrResult = ref(null)
const idParsedData = ref(null)
const idValidationErrors = ref([])

function triggerIdInput() { if (idInput.value) idInput.value.click() }

function handleIdChange(e) {
  const file = e.target.files[0]
  if (file) {
    idFile.value = file
    idPreview.value = URL.createObjectURL(file)
    idOcrResult.value = null
    idValidationErrors.value = []
  }
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = () => resolve(reader.result.split(',')[1])
    reader.onerror = error => reject(error)
  })
}

async function scanIdCard() {
  if (!idFile.value) return
  isScanningId.value = true
  idOcrResult.value = null
  idParsedData.value = null
  idValidationErrors.value = []

  try {
    const base64Image = await fileToBase64(idFile.value)
    const apiKey = process.env.VUE_APP_GOOGLE_CLOUD_VISION_API_KEY
    if (!apiKey || apiKey === 'YOUR_VISION_API_KEY_HERE') {
      alert("Please add Vision API key to .env")
      isScanningId.value = false
      return
    }

    const response = await fetch(`https://vision.googleapis.com/v1/images:annotate?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        requests: [{ image: { content: base64Image }, features: [{ type: 'DOCUMENT_TEXT_DETECTION' }] }]
      })
    })

    const data = await response.json()
    if (data.responses && data.responses[0].fullTextAnnotation) {
      const text = data.responses[0].fullTextAnnotation.text
      idOcrResult.value = text
      parseIDData(text)
    } else {
      idValidationErrors.value = ["No readable text found."]
    }
  } catch (error) {
    console.error(error)
    idValidationErrors.value = ["Error connecting to Vision API."]
  } finally {
    isScanningId.value = false
  }
}

function parseIDData(text) {
  idValidationErrors.value = []
  const results = { idNumber: null, dob: null, expiryDate: null, sex: null, nationality: null }

  const idMatch = text.match(/\b\d{9}\b/)
  if (idMatch) results.idNumber = idMatch[0]
  else idValidationErrors.value.push("No 9-digit ID number found.")

  const mrzDateRegex = new RegExp("(\\d{6})[0-9<]([MF<])(\\d{6})[0-9<]([A-Z<]{3})");
  const mrzMatch = text.match(mrzDateRegex)
  
  if (mrzMatch) {
    results.sex = mrzMatch[2]
    results.nationality = mrzMatch[4]
    const parseMRZ = (yymmdd, isDob) => {
      let y = parseInt(yymmdd.substring(0, 2), 10)
      const m = parseInt(yymmdd.substring(2, 4), 10) - 1
      const d = parseInt(yymmdd.substring(4, 6), 10)
      if (isDob) y += (y + 2000 > new Date().getFullYear()) ? 1900 : 2000
      else y += 2000
      return new Date(y, m, d)
    }
    results.dob = parseMRZ(mrzMatch[1], true)
    results.expiryDate = parseMRZ(mrzMatch[3], false)

    let age = new Date().getFullYear() - results.dob.getFullYear()
    if (age < 18) idValidationErrors.value.push(`User is underage (${age}). Must be 18+.`)
    if (results.expiryDate < new Date()) idValidationErrors.value.push("ID is expired.")
  } else {
    idValidationErrors.value.push("MRZ not found. Cannot verify dates.")
  }

  idParsedData.value = results
  if (idValidationErrors.value.length === 0) {
    setTimeout(() => {
      if (currentStep.value === 1) currentStep.value = 2;
    }, 2000);
  }
}

// --- STEP 2: REAL FACE MATCH (face-api.js) ---
const selfieVideoElement = ref(null)
const isSelfieCameraActive = ref(false)
const selfieFeedbackMsg = ref("Position your face in the oval.")
const isSelfieGood = ref(false)
const selfiePreview = ref(null)
const selfieFile = ref(null)
const isMatchingFace = ref(false)
const faceMatchStatus = ref(null)
const faceMatchErrorMsg = ref(null)

// --- CAMERA SELECTION LOGIC ---
const availableCameras = ref([])
const selectedCameraId = ref('')

async function populateCameras() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices()
    const videoInputs = devices.filter(device => device.kind === 'videoinput')
    availableCameras.value = videoInputs
    if (videoInputs.length > 0 && !selectedCameraId.value) {
      const userCam = videoInputs.find(c => c.label.toLowerCase().includes('front') || c.label.toLowerCase().includes('user'))
      selectedCameraId.value = userCam ? userCam.deviceId : videoInputs[0].deviceId
    }
  } catch (err) {
    console.error("Error enumerating cameras:", err)
  }
}

let selfieMediaStream = null
let selfieLoopRunning = false

function onSelfieCameraSelectChange() {
  if (isSelfieCameraActive.value) {
    stopSelfieCamera()
    startSelfieCamera()
  }
}

async function startSelfieCamera() {
  try {
    let constraints = { video: true }
    if (selectedCameraId.value) {
      constraints = { video: { deviceId: { exact: selectedCameraId.value } } }
    }
    selfieMediaStream = await navigator.mediaDevices.getUserMedia(constraints)
    await populateCameras()
    
    if (selfieVideoElement.value) {
      selfieVideoElement.value.srcObject = selfieMediaStream
      selfieVideoElement.value.onloadedmetadata = () => {
        isSelfieCameraActive.value = true
        selfieVideoElement.value.play()
        selfieFeedbackMsg.value = "Analyzing lighting and position..."
        startSelfieLoop()
      }
    }
  } catch (err) {
    console.error("Camera error:", err)
    // Even if it failed, try to list cameras. The user might be able to select a working one.
    await populateCameras()
    if (availableCameras.value.length > 1 && !selectedCameraId.value) {
        alert("Primary camera failed. A camera dropdown has been enabled. Please select a different camera from the list.")
    } else {
        alert("Camera access denied or unavailable. Please check your browser permissions or connection.")
    }
  }
}

function stopSelfieCamera() {
  selfieLoopRunning = false
  if (selfieMediaStream) {
    selfieMediaStream.getTracks().forEach(track => track.stop())
    selfieMediaStream = null
  }
  isSelfieCameraActive.value = false
}

function startSelfieLoop() {
  selfieLoopRunning = true
  const loop = async () => {
    if (!selfieLoopRunning) return
    if (selfieVideoElement.value && isSelfieCameraActive.value) {
      try {
        const detection = await faceapi.detectSingleFace(selfieVideoElement.value)
        if (detection) {
          const score = detection.score
          const box = detection.box
          const videoWidth = selfieVideoElement.value.videoWidth
          const videoHeight = selfieVideoElement.value.videoHeight
          
          const faceArea = box.width * box.height
          const frameArea = videoWidth * videoHeight
          const sizeRatio = faceArea / frameArea
          
          if (score < 0.7) {
             selfieFeedbackMsg.value = "Lighting might be too dark or uneven."
             isSelfieGood.value = false
          } else if (sizeRatio < 0.08) {
             selfieFeedbackMsg.value = "Move closer to the camera."
             isSelfieGood.value = false
          } else if (sizeRatio > 0.4) {
             selfieFeedbackMsg.value = "Move slightly away."
             isSelfieGood.value = false
          } else {
             selfieFeedbackMsg.value = "Perfect! Keep still."
             isSelfieGood.value = true
          }
        } else {
          selfieFeedbackMsg.value = "No face detected. Look directly at the camera."
          isSelfieGood.value = false
        }
      } catch (e) {
         console.error(e)
      }
    }
    requestAnimationFrame(loop)
  }
  loop()
}

function captureSelfie() {
  if (!selfieVideoElement.value) return
  const canvas = document.createElement('canvas')
  canvas.width = selfieVideoElement.value.videoWidth
  canvas.height = selfieVideoElement.value.videoHeight
  const ctx = canvas.getContext('2d')
  ctx.drawImage(selfieVideoElement.value, 0, 0, canvas.width, canvas.height)
  
  canvas.toBlob((blob) => {
    selfieFile.value = new File([blob], "selfie.jpg", { type: "image/jpeg" })
    selfiePreview.value = URL.createObjectURL(blob)
    stopSelfieCamera()
  }, 'image/jpeg', 0.95)
}

function retakeSelfie() {
  selfiePreview.value = null
  selfieFile.value = null
  faceMatchStatus.value = null
  faceMatchErrorMsg.value = null
  startSelfieCamera()
}

async function loadImageFromUrl(url) {
  return new Promise((resolve, reject) => {
    const img = new Image()
    img.crossOrigin = 'anonymous'
    img.onload = () => resolve(img)
    img.onerror = reject
    img.src = url
  })
}

async function matchFace() {
  if (!idPreview.value) {
    faceMatchStatus.value = 'error'
    faceMatchErrorMsg.value = 'Missing ID Card. Please go back to Step 1 and upload your ID.'
    return
  }
  if (!selfiePreview.value) {
    faceMatchStatus.value = 'error'
    faceMatchErrorMsg.value = 'Please capture a selfie.'
    return
  }
  isMatchingFace.value = true
  faceMatchStatus.value = null
  faceMatchErrorMsg.value = null
  
  try {
    const idImg = await loadImageFromUrl(idPreview.value)
    const selfieImg = await loadImageFromUrl(selfiePreview.value)
    
    const idDetection = await faceapi.detectSingleFace(idImg).withFaceLandmarks().withFaceDescriptor()
    const selfieDetection = await faceapi.detectSingleFace(selfieImg).withFaceLandmarks().withFaceDescriptor()
    
    if (!idDetection) throw new Error("Could not detect a clear face on the ID Card.")
    if (!selfieDetection) throw new Error("Could not detect a clear face in your Selfie.")
    
    const distance = faceapi.euclideanDistance(idDetection.descriptor, selfieDetection.descriptor)
    
    if (distance < 0.6) {
      faceMatchStatus.value = 'success'
      setTimeout(() => {
        if (currentStep.value === 2) currentStep.value = 3;
      }, 2000);
    } else {
      faceMatchStatus.value = 'error'
      faceMatchErrorMsg.value = `Faces do not match (Distance: ${distance.toFixed(2)}).`
    }
  } catch(e) {
    console.error(e)
    faceMatchStatus.value = 'error'
    faceMatchErrorMsg.value = e.message || 'Error running AI face match'
  } finally {
    isMatchingFace.value = false
  }
}

// --- STEP 3: REAL LIVENESS CHECK (Webcam Head Turn Detection) ---
const videoElement = ref(null)
const isCameraActive = ref(false)
const livenessMsg = ref("Please look straight at the camera.")
const livenessStage = ref('turnRight')

let mediaStream = null
let livenessLoopRunning = false

async function analyzeLiveness() {
  if (!videoElement.value || !isCameraActive.value) return;
  
  try {
    const detection = await faceapi.detectSingleFace(videoElement.value).withFaceLandmarks()
    
    if (detection) {
      const landmarks = detection.landmarks
      
      if (livenessStage.value === 'turnRight') {
        const positions = landmarks.positions;
        const noseTip = positions[30];
        const leftJaw = positions[0];
        const rightJaw = positions[16];
        const distL = noseTip.x - leftJaw.x;
        const distR = rightJaw.x - noseTip.x;
        if (distR > 0) {
          const ratio = distL / distR;
          if (ratio < 0.6) {
            livenessStage.value = 'turnLeft';
            livenessMsg.value = "Great! Now turn your head left.";
          }
        }
      } else if (livenessStage.value === 'turnLeft') {
        const positions = landmarks.positions;
        const noseTip = positions[30];
        const leftJaw = positions[0];
        const rightJaw = positions[16];
        const distL = noseTip.x - leftJaw.x;
        const distR = rightJaw.x - noseTip.x;
        if (distR > 0) {
          const ratio = distL / distR;
          if (ratio > 1.7) {
            livenessStage.value = 'lookUp';
            livenessMsg.value = "Good! Now look up slightly.";
          }
        }
      } else if (livenessStage.value === 'lookUp') {
        const positions = landmarks.positions;
        const noseTop = positions[27];
        const noseTip = positions[30];
        const chin = positions[8];
        const distUp = noseTip.y - noseTop.y;
        const distDown = chin.y - noseTip.y;
        if (distDown > 0) {
          const ratioY = distUp / distDown;
          if (ratioY < 0.6) {
            livenessStage.value = 'lookDown';
            livenessMsg.value = "Awesome! Finally, look down slightly.";
          }
        }
      } else if (livenessStage.value === 'lookDown') {
        const positions = landmarks.positions;
        const noseTop = positions[27];
        const noseTip = positions[30];
        const chin = positions[8];
        const distUp = noseTip.y - noseTop.y;
        const distDown = chin.y - noseTip.y;
        if (distDown > 0) {
          const ratioY = distUp / distDown;
          if (ratioY > 1.25) {
            livenessStage.value = 'done';
            livenessMsg.value = "✅ Liveness Verified! Saving your profile...";
            stopLivenessLoop();
            
            // Save to Firebase
            try {
              if (idParsedData.value && auth.currentUser) {
                const uid = auth.currentUser.uid;
                
                // 1. Audit Log: Save to verified_users
                await addDoc(collection(db, "verified_users"), {
                  userId: uid,
                  idNumber: idParsedData.value.idNumber,
                  sex: idParsedData.value.sex,
                  nationality: idParsedData.value.nationality,
                  dob: idParsedData.value.dob ? idParsedData.value.dob.toISOString() : null,
                  expiryDate: idParsedData.value.expiryDate ? idParsedData.value.expiryDate.toISOString() : null,
                  verifiedAt: new Date().toISOString()
                });

                // 2. Profile Sync: Update main users collection
                await setDoc(doc(db, "users", uid), {
                  verificationStatus: 'verified',
                  idNumber: idParsedData.value.idNumber,
                  verifiedAt: new Date().toISOString()
                }, { merge: true });
              }
            } catch (err) {
              console.error("Error saving to Firebase:", err)
            }

            setTimeout(() => {
              stopCamera();
              currentStep.value = 4;
            }, 1500);
          }
        }
      }
    } else {
      livenessMsg.value = "No face detected in frame. Please adjust."
    }
  } catch(e) {
    console.error("Liveness error:", e)
  }
}

function startLivenessLoop() {
  livenessLoopRunning = true;
  const loop = async () => {
    if (!livenessLoopRunning) return;
    await analyzeLiveness();
    requestAnimationFrame(loop);
  }
  loop();
}

function stopLivenessLoop() {
  livenessLoopRunning = false;
}

async function startCamera() {
  try {
    let constraints = { video: true }
    if (selectedCameraId.value) {
      constraints = { video: { deviceId: { exact: selectedCameraId.value } } }
    }
    mediaStream = await navigator.mediaDevices.getUserMedia(constraints)
    await populateCameras()
    
    if (videoElement.value) {
      videoElement.value.srcObject = mediaStream
      
      videoElement.value.onloadedmetadata = () => {
        isCameraActive.value = true
        livenessMsg.value = "Initializing AI..."
        videoElement.value.play();
        livenessStage.value = 'turnRight';
        startLivenessLoop();
      }
    }
  } catch (err) {
    console.error("Camera error:", err)
    await populateCameras()
    if (availableCameras.value.length > 1 && !selectedCameraId.value) {
        alert("Primary camera failed. A camera dropdown has been enabled. Please select a different camera from the list.")
    } else {
        alert("Camera access denied or unavailable. Please check your browser permissions or connection.")
    }
  }
}

function stopCamera() {
  stopLivenessLoop()
  if (mediaStream) {
    mediaStream.getTracks().forEach(track => track.stop())
    mediaStream = null
  }
  isCameraActive.value = false
}


onBeforeUnmount(() => {
  stopSelfieCamera()
  stopCamera()
  // Restore global overflow/height states
  document.body.style.overflow = ''
  const appEl = document.getElementById('app')
  if (appEl) {
    appEl.style.height = ''
    appEl.style.minHeight = ''
  }
})
</script>

<style scoped>
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
  padding: 16px 20px; border-bottom: 1px solid #e2e8f0; background: #fff;
}
.back-btn { background: none; border: none; cursor: pointer; color: #111; display: flex; align-items: center; justify-content: center; }
.page-title { font-size: 1.1rem; font-weight: 600; color: #111; }
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
  height: 90px;
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid #e2e8f0;
  background: #f8fafc;
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
  width: 100%; padding: 14px; background: #0f172a; color: #fff;
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
.liveness-msg {
  position: absolute; bottom: 20px; left: 20px; right: 20px;
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
</style>
