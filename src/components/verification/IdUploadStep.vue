<template>
  <div class="step-section">
    <h2 class="section-title">Verify ID Document</h2>
    <p class="section-subtitle">Please upload a clear, well-lit photo of your Cambodian National ID.</p>

    <!-- ID Input Method Toggle -->
    <div v-if="!idPreview" class="mode-toggle-group" style="display: flex; gap: 8px; margin-bottom: 16px;">
      <button class="btn-secondary" style="flex: 1; padding: 8px;" :style="idScanMode === 'upload' ? 'background: #e2e8f0;' : ''" @click="switchIdMode('upload')">📁 Upload File</button>
      <button class="btn-secondary" style="flex: 1; padding: 8px;" :style="idScanMode === 'scan' ? 'background: #e2e8f0;' : ''" @click="switchIdMode('scan')">📷 Scan ID</button>
    </div>

    <div v-if="idScanMode === 'upload' || idPreview" class="upload-box" @click="!idPreview ? triggerIdInput() : null" :style="idPreview ? 'cursor: default;' : ''">
      <input type="file" ref="idInput" accept="image/*" class="hidden-input" @change="handleIdChange" />
      <div v-if="idPreview" class="preview-container">
        <img :src="idPreview" alt="ID Preview" class="preview-image" style="object-fit: contain; background: #000;" />
      </div>
      <div v-else class="upload-placeholder">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
        <span>Tap to upload ID</span>
      </div>
    </div>

    <!-- SCAN MODE -->
    <div v-if="idScanMode === 'scan' && !idPreview" class="camera-container" style="margin-bottom: 16px;">
      <video ref="idVideoElement" autoplay playsinline muted class="camera-video" style="transform: none;"></video>
      <div class="camera-overlay">
        <div class="id-cutout"></div>
      </div>
      <div class="liveness-msg">
        {{ idScanMsg }}
      </div>
    </div>
    
    <div v-if="idScanMode === 'scan' && !idPreview && availableCameras.length > 1" class="camera-selector" style="margin-bottom: 16px;">
      <label for="id-camera-select" style="font-weight: 500; font-size: 14px; margin-right: 8px;">Switch Camera:</label>
      <select id="id-camera-select" v-model="selectedCameraId" @change="onIdCameraSelectChange" style="padding: 6px; border-radius: 6px; border: 1px solid #ccc;">
        <option v-for="cam in availableCameras" :key="cam.deviceId" :value="cam.deviceId">
          {{ cam.label || 'Camera ' + (availableCameras.indexOf(cam) + 1) }}
        </option>
      </select>
    </div>

    <button v-if="idScanMode === 'scan' && !idPreview" class="btn-primary" style="margin-bottom: 16px;" :disabled="!isIdLightingGood" @click="captureIdPhoto">
      Capture Photo
    </button>

    <div v-if="idPreview" style="display: flex; gap: 12px; margin-bottom: 16px; margin-top: 12px;">
       <button class="btn-secondary" style="flex: 1;" :disabled="isScanningId" @click="retakeId">
         Retake
       </button>
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

      <div v-if="idOcrResult" class="raw-scan-section" style="margin-top: 16px;">
        <button 
          type="button" 
          class="btn-secondary" 
          style="padding: 8px 12px; font-size: 0.85rem; border-radius: 8px; width: auto; display: inline-flex; align-items: center; gap: 6px; margin-bottom: 8px;"
          @click="showRawScan = !showRawScan"
        >
          <span>{{ showRawScan ? 'Hide Raw Scan' : 'Show Raw Scan' }}</span>
          <svg 
            width="14" 
            height="14" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2"
            :style="showRawScan ? 'transform: rotate(180deg); transition: transform 0.2s;' : 'transition: transform 0.2s;'"
          >
            <path d="M6 9l6 6 6-6"/>
          </svg>
        </button>
        <div v-if="showRawScan" class="raw-scan-box" style="background: #0f172a; color: #38bdf8; padding: 12px; border-radius: 8px; font-family: monospace; font-size: 0.8rem; white-space: pre-wrap; max-height: 150px; overflow-y: auto; text-align: left; border: 1px solid #334155;">
          {{ idOcrResult }}
        </div>
      </div>
    </div>

    <div v-if="idParsedData && idValidationErrors.length === 0" class="auto-advance-msg">
      Proceeding to Face Match...
    </div>
  </div>
</template>

<script setup>
/* global defineEmits */
import { ref, onMounted, onBeforeUnmount } from 'vue'

const emit = defineEmits(['complete'])

// --- STEP 1: ID SCANNING (Google Cloud Vision) ---
const idInput = ref(null)
const idFile = ref(null)
const idPreview = ref(null)
const isScanningId = ref(false)
const idOcrResult = ref(null)
const showRawScan = ref(false)
const idParsedData = ref(null)
const idValidationErrors = ref([])

// --- ID CAMERA SCAN MODE ---
const idScanMode = ref('upload')
const idVideoElement = ref(null)
const isIdCameraActive = ref(false)
const idScanMsg = ref("Position your ID inside the rectangle.")
const isIdLightingGood = ref(false)
let idMediaStream = null
let idScanLoopRunning = false

// --- CAMERA SELECTION LOGIC ---
const availableCameras = ref([])
const selectedCameraId = ref('')

onMounted(async () => {
  await populateCameras()
})

onBeforeUnmount(() => {
  stopIdCamera()
})

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

function switchIdMode(mode) {
  idScanMode.value = mode
  if (mode === 'scan') {
    startIdCamera()
  } else {
    stopIdCamera()
  }
}

async function startIdCamera() {
  try {
    let constraints = { video: { facingMode: 'environment' } }
    if (selectedCameraId.value) {
      constraints = { video: { deviceId: { exact: selectedCameraId.value } } }
    }
    idMediaStream = await navigator.mediaDevices.getUserMedia(constraints)
    await populateCameras()
    
    if (idVideoElement.value) {
      idVideoElement.value.srcObject = idMediaStream
      idVideoElement.value.onloadedmetadata = () => {
        isIdCameraActive.value = true
        idVideoElement.value.play()
        startIdScanLoop()
      }
    }
  } catch (err) {
    console.error("ID Camera error:", err)
    alert("Camera access denied or unavailable.")
    idScanMode.value = 'upload'
  }
}

function stopIdCamera() {
  idScanLoopRunning = false
  if (idMediaStream) {
    idMediaStream.getTracks().forEach(track => track.stop())
    idMediaStream = null
  }
  isIdCameraActive.value = false
}

function startIdScanLoop() {
  idScanLoopRunning = true
  const loop = () => {
    if (!idScanLoopRunning) return
    if (idVideoElement.value && isIdCameraActive.value) {
       const canvas = document.createElement('canvas')
       canvas.width = 64
       canvas.height = 64
       const ctx = canvas.getContext('2d')
       ctx.drawImage(idVideoElement.value, 0, 0, 64, 64)
       const imgData = ctx.getImageData(0,0,64,64).data
       let brightnessSum = 0
       for (let i = 0; i < imgData.length; i += 4) {
         brightnessSum += 0.299 * imgData[i] + 0.587 * imgData[i+1] + 0.114 * imgData[i+2]
       }
       const avg = brightnessSum / (imgData.length / 4)
       
       if (avg < 50) {
         idScanMsg.value = "Too dark! Find better lighting."
         isIdLightingGood.value = false
       } else {
         idScanMsg.value = "Align your ID and click Capture."
         isIdLightingGood.value = true
       }
    }
    setTimeout(() => requestAnimationFrame(loop), 100)
  }
  loop()
}

function captureIdPhoto() {
  if (!idVideoElement.value) return
  const canvas = document.createElement('canvas')
  canvas.width = idVideoElement.value.videoWidth
  canvas.height = idVideoElement.value.videoHeight
  if (canvas.width === 0 || canvas.height === 0) return
  const ctx = canvas.getContext('2d')
  ctx.drawImage(idVideoElement.value, 0, 0, canvas.width, canvas.height)
  
  canvas.toBlob((blob) => {
    if (!blob) return
    const file = new File([blob], "scanned_id.jpg", { type: "image/jpeg" })
    idFile.value = file
    idPreview.value = URL.createObjectURL(blob)
    idOcrResult.value = null
    idValidationErrors.value = []
    stopIdCamera()
  }, 'image/jpeg', 0.95)
}

function onIdCameraSelectChange() {
  if (isIdCameraActive.value) {
    stopIdCamera()
    startIdCamera()
  }
}

function retakeId() {
  idPreview.value = null
  idFile.value = null
  idParsedData.value = null
  idOcrResult.value = null
  showRawScan.value = false
  idValidationErrors.value = []
  if (idScanMode.value === 'scan') {
    startIdCamera()
  }
}

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
  showRawScan.value = false
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

  const mrzDateRegex = new RegExp("(\\d{6})[0-9<]([MF<])(\\d{6})[0-9<]([A-Z<]{3})")
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
      emit('complete', {
        idPreview: idPreview.value,
        idParsedData: idParsedData.value
      })
    }, 2000)
  }
}
</script>
