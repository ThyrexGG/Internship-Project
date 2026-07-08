<template>
  <div class="step-section">
    <h2 class="section-title">Secure Liveness Scan</h2>
    <p class="section-subtitle">Verify you are a real person by completing a quick interactive scan.</p>

    <!-- Dynamic Liveness Instruction Panel -->
    <div class="liveness-guide-card">
      <div class="guide-anim-wrapper">
        <!-- Turn Head Animation (Shown during turn stage) -->
        <div v-if="livenessStage !== 'done'" class="animation-container">
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
          <p class="anim-label" v-else-if="livenessStage === 'processing'">Processing scan...</p>
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

    <div class="camera-container" :class="{ 'flash-green': livenessFlash }">
      <video ref="videoElement" autoplay playsinline muted class="camera-video"></video>
      <div class="camera-overlay">
        <div class="oval-cutout"></div>
      </div>
      <div v-if="isCameraActive" class="liveness-msg">
        <span v-if="!isFaceInFrame && livenessStage !== 'processing' && livenessStage !== 'done'" style="color: #dc2626;">
          No face detected in frame. Please adjust.
        </span>
        <span v-else>
          {{ livenessMsg }}
        </span>
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
</template>

<script setup>
/* global defineEmits */
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as faceapi from 'face-api.js'

const emit = defineEmits(['complete'])

const videoElement = ref(null)
const isCameraActive = ref(false)
const livenessMsg = ref("Please look straight at the camera.")
const livenessStage = ref('turnRight')
const isFaceInFrame = ref(false)
const livenessFlash = ref(false)

// --- CAMERA SELECTION LOGIC ---
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
  }, 500)
})

onBeforeUnmount(() => {
  stopCamera()
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

function triggerLivenessFlash() {
  livenessFlash.value = true;
  setTimeout(() => {
    livenessFlash.value = false;
  }, 500);
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

async function analyzeLiveness() {
  if (!videoElement.value || !isCameraActive.value) return;
  
  try {
    const detection = await faceapi.detectSingleFace(videoElement.value).withFaceLandmarks()
    
    if (detection) {
      missingFaceFrames = 0;
      isFaceInFrame.value = true;
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
          if (ratio < 0.65) {
            triggerLivenessFlash();
            livenessStage.value = 'processing';
            livenessMsg.value = "Processing scan...";
            setTimeout(() => {
              livenessStage.value = 'turnLeft';
              livenessMsg.value = "Great! Now turn your head left.";
            }, 2000);
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
          if (ratio > 1.5) {
            triggerLivenessFlash();
            livenessStage.value = 'processing';
            livenessMsg.value = "Processing scan...";
            setTimeout(() => {
              livenessStage.value = 'lookUp';
              livenessMsg.value = "Good! Now look up slightly.";
            }, 2000);
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
          if (ratioY < 0.65) {
            triggerLivenessFlash();
            livenessStage.value = 'processing';
            livenessMsg.value = "Processing scan...";
            setTimeout(() => {
              livenessStage.value = 'lookDown';
              livenessMsg.value = "Awesome! Finally, look down slightly.";
            }, 2000);
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
          if (ratioY > 1.15) {
            triggerLivenessFlash();
            livenessStage.value = 'done';
            livenessMsg.value = "✅ Liveness Verified! Saving your profile...";
            stopLivenessLoop();
            
            setTimeout(() => {
              stopCamera();
              emit('complete');
            }, 1500);
          }
        }
      }
    } else {
      missingFaceFrames++;
      if (missingFaceFrames > 15) {
        isFaceInFrame.value = false;
      }
    }
  } catch(e) {
    console.error("Liveness error:", e)
  }
}
</script>
