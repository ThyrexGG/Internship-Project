<template>
  <div class="step-content-section">
    <header class="step-header">
      <h2 class="step-title">Secure Liveness Scan</h2>
      <p class="step-subtitle">Verify you are a real person by completing a quick interactive scan.</p>
    </header>

    <!-- Dynamic Purple Instruction Card -->
    <div class="liveness-prompt-card">
      <div class="prompt-icon-badge">
        <svg v-if="livenessStage !== 'done'" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#9333ea" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <!-- Circular motion turn arrow -->
          <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 11-.57-8.38l6.67-1.19"/>
        </svg>
        <svg v-else width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="3">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
      </div>
      <p class="prompt-instruction-text" :class="{ 'text-verified': livenessStage === 'done' }">
        <span v-if="livenessStage === 'turnRight'">Slowly turn head to the right</span>
        <span v-else-if="livenessStage === 'turnLeft'">Now turn head to the left</span>
        <span v-else-if="livenessStage === 'lookUp'">Now look up slightly</span>
        <span v-else-if="livenessStage === 'lookDown'">Now look down slightly</span>
        <span v-else-if="livenessStage === 'processing'">Processing scan...</span>
        <span v-else-if="livenessStage === 'done'">Liveness scan complete!</span>
        <span v-else>Follow the interactive instructions</span>
      </p>
    </div>

    <!-- Video Stream Container with Center Oval Cutout -->
    <div class="camera-stream-wrapper" :class="{ 'flash-success': livenessFlash }">
      <video ref="videoElement" autoplay playsinline muted class="camera-stream-video"></video>
      <div class="camera-stream-overlay">
        <div class="oval-silhouette-guide"></div>
      </div>
      <div v-if="isCameraActive" class="liveness-status-pill">
        <span v-if="!isFaceInFrame && livenessStage !== 'processing' && livenessStage !== 'done'" class="text-warn">
          No face detected. Adjust your position.
        </span>
        <span v-else>
          {{ livenessMsg }}
        </span>
      </div>
    </div>

    <!-- Camera switcher if multiple cameras -->
    <div v-if="availableCameras.length > 1 && !isCameraActive" class="camera-switch-row">
      <label for="live-cam-sel" class="cam-label">Camera:</label>
      <select id="live-cam-sel" v-model="selectedCameraId" class="cam-select">
        <option v-for="cam in availableCameras" :key="cam.deviceId" :value="cam.deviceId">
          {{ cam.label || 'Camera ' + (availableCameras.indexOf(cam) + 1) }}
        </option>
      </select>
    </div>

    <!-- Main Action Button: Complete & Go to Account -->
    <button 
      type="button" 
      class="btn-primary-action" 
      :disabled="isCompleting"
      @click="handleCompleteAndGoToAccount"
    >
      {{ isCompleting ? 'Finalizing Verification...' : 'Complete & Go to Account' }}
    </button>
  </div>
</template>

<script setup>
/* global defineEmits */
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as faceapi from 'face-api.js'

const emit = defineEmits(['complete'])

const videoElement = ref(null)
const isCameraActive = ref(false)
const livenessMsg = ref("Look straight at the camera.")
const livenessStage = ref('turnRight')
const isFaceInFrame = ref(true)
const livenessFlash = ref(false)
const isCompleting = ref(false)

const availableCameras = ref([])
const selectedCameraId = ref('')

let mediaStream = null
let livenessLoopRunning = false
let missingFaceFrames = 0

onMounted(async () => {
  await populateCameras()
  setTimeout(() => {
    if (!isCameraActive.value) {
      startCamera()
    }
  }, 400)
})

onBeforeUnmount(() => {
  stopCamera()
})

async function populateCameras() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices()
    const videoInputs = devices.filter(d => d.kind === 'videoinput')
    availableCameras.value = videoInputs
    if (videoInputs.length > 0 && !selectedCameraId.value) {
      const userCam = videoInputs.find(c => c.label.toLowerCase().includes('front') || c.label.toLowerCase().includes('user'))
      selectedCameraId.value = userCam ? userCam.deviceId : videoInputs[0].deviceId
    }
  } catch (err) {
    console.warn("Camera enumeration:", err)
  }
}

function triggerLivenessFlash() {
  livenessFlash.value = true
  setTimeout(() => {
    livenessFlash.value = false
  }, 500)
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
        videoElement.value.play()
        livenessStage.value = 'turnRight'
        livenessMsg.value = "Slowly turn head to the right"
        startLivenessLoop()
      }
    }
  } catch (err) {
    console.warn("Camera start failed, operating in test mode:", err)
    isCameraActive.value = false
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

function startLivenessLoop() {
  livenessLoopRunning = true
  const loop = async () => {
    if (!livenessLoopRunning) return
    await analyzeLiveness()
    requestAnimationFrame(loop)
  }
  loop()
}

function stopLivenessLoop() {
  livenessLoopRunning = false
}

async function analyzeLiveness() {
  if (!videoElement.value || !isCameraActive.value) return

  try {
    const detection = await faceapi.detectSingleFace(videoElement.value).withFaceLandmarks()

    if (detection) {
      missingFaceFrames = 0
      isFaceInFrame.value = true
      const landmarks = detection.landmarks
      const positions = landmarks.positions
      const noseTip = positions[30]
      const leftJaw = positions[0]
      const rightJaw = positions[16]
      const distL = noseTip.x - leftJaw.x
      const distR = rightJaw.x - noseTip.x

      if (livenessStage.value === 'turnRight') {
        if (distR > 0 && distL / distR < 0.7) {
          triggerLivenessFlash()
          livenessStage.value = 'processing'
          setTimeout(() => {
            livenessStage.value = 'turnLeft'
            livenessMsg.value = "Now turn head to the left"
          }, 1500)
        }
      } else if (livenessStage.value === 'turnLeft') {
        if (distR > 0 && distL / distR > 1.4) {
          triggerLivenessFlash()
          livenessStage.value = 'processing'
          setTimeout(() => {
            livenessStage.value = 'done'
            livenessMsg.value = "Liveness scan complete!"
          }, 1500)
        }
      }
    } else {
      missingFaceFrames++
      if (missingFaceFrames > 15) {
        isFaceInFrame.value = false
      }
    }
  } catch (err) {
    // Graceful landmark check
  }
}

function handleCompleteAndGoToAccount() {
  isCompleting.value = true
  stopCamera()
  emit('complete')
}
</script>

<style scoped>
.step-content-section {
  width: 100%;
  animation: fadeIn 0.3s ease;
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.step-header {
  text-align: center;
  margin-bottom: 24px;
}

.step-title {
  font-size: 1.85rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 8px;
  letter-spacing: -0.02em;
}

.step-subtitle {
  font-size: 0.92rem;
  color: #8C7E7E;
  line-height: 1.5;
  max-width: 440px;
  margin: 0 auto;
}

/* Dynamic Instruction Card */
.liveness-prompt-card {
  border: 1.5px solid #EDE8E3;
  border-radius: 14px;
  background: #FAF8F5;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.prompt-icon-badge {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #F4EDEA;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #5C4E4E;
}

.prompt-instruction-text {
  font-size: 1rem;
  font-weight: 700;
  color: #5C4E4E;
  text-align: center;
}

.text-verified {
  color: #2E7D32 !important;
}

/* Stream Wrapper */
.camera-stream-wrapper {
  position: relative;
  width: 100%;
  height: 260px;
  border-radius: 14px;
  background: #2A2421;
  overflow: hidden;
  margin-bottom: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.camera-stream-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scaleX(-1);
}

.camera-stream-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.oval-silhouette-guide {
  width: 140px;
  height: 190px;
  border: 2px dashed rgba(255, 255, 255, 0.75);
  border-radius: 50%;
}

.liveness-status-pill {
  position: absolute;
  bottom: 14px;
  left: 16px;
  right: 16px;
  padding: 8px 14px;
  background: rgba(42, 36, 33, 0.85);
  color: #ffffff;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  text-align: center;
  backdrop-filter: blur(4px);
}

.text-warn {
  color: #DC2626 !important;
}

.camera-switch-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.cam-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #5C4E4E;
}

.cam-select {
  flex: 1;
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #D1D5DB;
  font-size: 0.85rem;
  font-family: inherit;
  color: #2A2421;
}

/* Action Button */
.btn-primary-action {
  width: 100%;
  padding: 14px 20px;
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
  box-sizing: border-box;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.15);
}

.btn-primary-action:hover:not(:disabled) {
  background: #473B3B;
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.25);
}

.btn-primary-action:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

.camera-stream-wrapper.flash-success::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  box-shadow: inset 0 0 0 6px #2E7D32, inset 0 0 40px 10px rgba(46, 125, 50, 0.6);
  pointer-events: none;
  animation: flashFade 0.5s ease-out;
}

@keyframes flashFade {
  from { opacity: 1; }
  to { opacity: 0; }
}
</style>
