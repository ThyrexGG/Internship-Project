<template>
  <div class="step-section">
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
</template>

<script setup>
/* global defineProps, defineEmits */
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as faceapi from 'face-api.js'

const props = defineProps({
  idPreview: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['complete'])

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

let selfieMediaStream = null
let selfieLoopRunning = false

onMounted(async () => {
  await populateCameras()
  setTimeout(() => {
    if (!isSelfieCameraActive.value && !selfiePreview.value) {
      startSelfieCamera()
    }
  }, 500)
})

onBeforeUnmount(() => {
  stopSelfieCamera()
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
        const tmpCanvas = document.createElement('canvas')
        tmpCanvas.width = 64
        tmpCanvas.height = 64
        const tmpCtx = tmpCanvas.getContext('2d')
        tmpCtx.drawImage(selfieVideoElement.value, 0, 0, 64, 64)
        const imgData = tmpCtx.getImageData(0,0,64,64).data
        let globalBrightnessSum = 0
        for (let i = 0; i < imgData.length; i += 4) {
          globalBrightnessSum += 0.299 * imgData[i] + 0.587 * imgData[i+1] + 0.114 * imgData[i+2]
        }
        const globalBrightness = globalBrightnessSum / (imgData.length / 4)

        if (globalBrightness < 45) {
          selfieFeedbackMsg.value = "Too dark! Please move to a well-lit area."
          isSelfieGood.value = false
        } else {
          const detection = await faceapi.detectSingleFace(selfieVideoElement.value).withFaceLandmarks()
          if (detection) {
            const score = detection.detection.score
            const box = detection.detection.box
            const videoWidth = selfieVideoElement.value.videoWidth
            const videoHeight = selfieVideoElement.value.videoHeight
            
            const faceArea = box.width * box.height
            const frameArea = videoWidth * videoHeight
            const sizeRatio = faceArea / frameArea
            
            const leftEye = detection.landmarks.getLeftEye()
            const rightEye = detection.landmarks.getRightEye()
            const allEyePoints = [...leftEye, ...rightEye]
            let minX = Math.min(...allEyePoints.map(p => p.x))
            let maxX = Math.max(...allEyePoints.map(p => p.x))
            let minY = Math.min(...allEyePoints.map(p => p.y))
            let maxY = Math.max(...allEyePoints.map(p => p.y))
            
            minX = Math.max(0, minX - 10)
            maxX = Math.min(videoWidth, maxX + 10)
            minY = Math.max(0, minY - 10)
            maxY = Math.min(videoHeight, maxY + 10)
            
            const canvas = document.createElement('canvas')
            canvas.width = videoWidth
            canvas.height = videoHeight
            const ctx = canvas.getContext('2d')
            ctx.drawImage(selfieVideoElement.value, 0, 0, videoWidth, videoHeight)
            
            let avgBrightness = 255
            const w = maxX - minX
            const h = maxY - minY
            if (w > 0 && h > 0) {
              const eyeData = ctx.getImageData(minX, minY, w, h).data
              let brightnessSum = 0
              for (let i = 0; i < eyeData.length; i += 4) {
                brightnessSum += 0.299 * eyeData[i] + 0.587 * eyeData[i+1] + 0.114 * eyeData[i+2]
              }
              avgBrightness = brightnessSum / (eyeData.length / 4)
            }

            const positions = detection.landmarks.positions;
            const leftJaw = positions[0];
            const rightJaw = positions[16];
            const noseTop = positions[27];
            const noseTip = positions[30];
            const chin = positions[8];

            const distLeftToNose = noseTip.x - leftJaw.x;
            const distRightToNose = rightJaw.x - noseTip.x;
            const yawRatio = distRightToNose > 0 ? (distLeftToNose / distRightToNose) : 1;

            const distNoseUp = noseTip.y - noseTop.y;
            const distNoseDown = chin.y - noseTip.y;
            const pitchRatio = distNoseDown > 0 ? (distNoseUp / distNoseDown) : 1;

            if (score < 0.7) {
               selfieFeedbackMsg.value = "Lighting might be too dark or uneven."
               isSelfieGood.value = false
            } else if (sizeRatio < 0.08) {
               selfieFeedbackMsg.value = "Move closer to the camera."
               isSelfieGood.value = false
            } else if (sizeRatio > 0.4) {
               selfieFeedbackMsg.value = "Move slightly away."
               isSelfieGood.value = false
            } else if (avgBrightness < 75) {
               selfieFeedbackMsg.value = "Please remove your sunglasses!"
               isSelfieGood.value = false
            } else if (yawRatio < 0.7 || yawRatio > 1.4) {
               selfieFeedbackMsg.value = "Please look straight at the camera."
               isSelfieGood.value = false
            } else if (pitchRatio < 0.6 || pitchRatio > 1.2) {
               selfieFeedbackMsg.value = "Keep your head level and look straight."
               isSelfieGood.value = false
            } else {
               selfieFeedbackMsg.value = "Perfect! Keep still."
               isSelfieGood.value = true
            }
          } else {
            selfieFeedbackMsg.value = "No face detected. Look directly at the camera."
            isSelfieGood.value = false
          }
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
  if (canvas.width === 0 || canvas.height === 0) return
  const ctx = canvas.getContext('2d')
  ctx.drawImage(selfieVideoElement.value, 0, 0, canvas.width, canvas.height)
  
  canvas.toBlob((blob) => {
    if (!blob) return
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
  if (!props.idPreview) {
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
    const idImg = await loadImageFromUrl(props.idPreview)
    const selfieImg = await loadImageFromUrl(selfiePreview.value)
    
    const idDetection = await faceapi.detectSingleFace(idImg).withFaceLandmarks().withFaceDescriptor()
    const selfieDetection = await faceapi.detectSingleFace(selfieImg).withFaceLandmarks().withFaceDescriptor()
    
    if (!idDetection) throw new Error("Could not detect a clear face on the ID Card.")
    if (!selfieDetection) throw new Error("Could not detect a clear face in your Selfie.")
    
    const leftEye = selfieDetection.landmarks.getLeftEye()
    const rightEye = selfieDetection.landmarks.getRightEye()
    
    const allEyePoints = [...leftEye, ...rightEye]
    let minX = Math.min(...allEyePoints.map(p => p.x))
    let maxX = Math.max(...allEyePoints.map(p => p.x))
    let minY = Math.min(...allEyePoints.map(p => p.y))
    let maxY = Math.max(...allEyePoints.map(p => p.y))
    
    minX = Math.max(0, minX - 10)
    maxX = Math.min(selfieImg.width, maxX + 10)
    minY = Math.max(0, minY - 10)
    maxY = Math.min(selfieImg.height, maxY + 10)
    
    const canvas = document.createElement('canvas')
    canvas.width = selfieImg.width
    canvas.height = selfieImg.height
    const ctx = canvas.getContext('2d')
    ctx.drawImage(selfieImg, 0, 0)
    
    const w = maxX - minX
    const h = maxY - minY
    if (w > 0 && h > 0) {
      const eyeData = ctx.getImageData(minX, minY, w, h).data
      let brightnessSum = 0
      for (let i = 0; i < eyeData.length; i += 4) {
        brightnessSum += 0.299 * eyeData[i] + 0.587 * eyeData[i+1] + 0.114 * eyeData[i+2]
      }
      const avgBrightness = brightnessSum / (eyeData.length / 4)
      
      if (avgBrightness < 75) {
        throw new Error("Dark glasses or sunglasses detected. Please remove them and retake your selfie.")
      }
    }

    const distance = faceapi.euclideanDistance(idDetection.descriptor, selfieDetection.descriptor)
    
    if (distance < 0.5) {
      faceMatchStatus.value = 'success'
      setTimeout(() => {
        emit('complete')
      }, 2000)
    } else {
      faceMatchStatus.value = 'error'
      faceMatchErrorMsg.value = "Identity mismatch. The face in your selfie does not match the person on the ID card."
    }
  } catch(e) {
    console.error(e)
    faceMatchStatus.value = 'error'
    faceMatchErrorMsg.value = e.message || 'Error running AI face match'
  } finally {
    isMatchingFace.value = false
  }
}
</script>
