<template>
  <div class="profile-step-container">
    <header class="step-header">
      <h2 class="step-title">Review & Complete Profile</h2>
      <p class="step-subtitle">
        Tell us a little more about yourself.<br />
        Please fill in all the information to get better recommendations
      </p>
    </header>

    <form class="profile-form" @submit.prevent="handleSaveAndContinue">
      <!-- Avatar Section -->
      <div class="avatar-section">
        <div class="avatar-preview-wrapper" @click="triggerFileInput">
          <img v-if="photoPreview" :src="photoPreview" @error="photoPreview = ''" alt="Profile" class="avatar-image" />
          <div v-else class="avatar-placeholder">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="2">
              <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" />
              <circle cx="12" cy="7" r="4" />
            </svg>
          </div>
        </div>
        <div class="avatar-actions">
          <button type="button" class="btn-upload-photo" @click="triggerFileInput">
            {{ photoPreview ? 'Change Photo' : 'Upload Photo' }}
          </button>
          <span v-if="!fileErrorMsg" class="avatar-hint">JPG, PNG or WebP. Max 10MB.</span>
          <span v-else class="avatar-hint" style="color: #ef4444; font-weight: 600;">{{ fileErrorMsg }}</span>
        </div>
        <input
          ref="fileInputRef"
          type="file"
          accept="image/jpeg,image/png,image/webp"
          class="hidden-file-input"
          @change="onFileSelected"
        />
      </div>

      <!-- Personal Details -->
      <div class="form-group-section">
        <h3 class="group-title">Personal Details</h3>
        
        <div class="field-item">
          <label class="field-label">Date of Birth</label>
          <input 
            type="text" 
            v-model="profile.dob" 
            placeholder="dd/mm/yyyy" 
            class="custom-input" 
          />
        </div>

        <div class="field-item">
          <label class="field-label">Gender</label>
          <div class="select-wrapper">
            <select v-model="profile.gender" class="custom-select">
              <option value="">Select Gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
            <span class="select-chevron">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M6 9l6 6 6-6"/>
              </svg>
            </span>
          </div>
        </div>

        <div class="field-item">
          <label class="field-label">Phone Number</label>
          <input 
            type="tel" 
            v-model="profile.phone" 
            placeholder="+1 234 567 8900" 
            class="custom-input" 
          />
        </div>
      </div>

      <!-- Education & Work -->
      <div class="form-group-section">
        <h3 class="group-title">Education & Work</h3>

        <div class="field-item">
          <label class="field-label">Status</label>
          <div class="select-wrapper">
            <select v-model="profile.status" class="custom-select">
              <option value="">Select Status</option>
              <option value="Student">Student</option>
              <option value="Professional">Professional</option>
              <option value="Employed">Employed</option>
              <option value="Freelancer">Freelancer</option>
            </select>
            <span class="select-chevron">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M6 9l6 6 6-6"/>
              </svg>
            </span>
          </div>
        </div>

        <div class="field-item">
          <label class="field-label">University</label>
          <input 
            type="text" 
            v-model="profile.university" 
            placeholder="e.g. Harvard University" 
            class="custom-input" 
          />
        </div>

        <div class="field-item">
          <label class="field-label">Occupation</label>
          <input 
            type="text" 
            v-model="profile.job" 
            placeholder="e.g. Software Engineering" 
            class="custom-input" 
          />
        </div>
      </div>

      <!-- Hobbies -->
      <div class="form-group-section">
        <h3 class="group-title">Hobbies</h3>

        <div class="field-item">
          <label class="field-label">Music Genre</label>
          <input 
            type="text" 
            v-model="profile.hobbies.music" 
            placeholder="e.g. Pop, Rock, Jazz..." 
            class="custom-input" 
          />
        </div>

        <div class="field-item">
          <label class="field-label">Games</label>
          <input 
            type="text" 
            v-model="profile.hobbies.games" 
            placeholder="e.g. Board games, Video games" 
            class="custom-input" 
          />
        </div>

        <div class="field-item">
          <label class="field-label">Sports</label>
          <input 
            type="text" 
            v-model="profile.hobbies.sports" 
            placeholder="e.g. Basket Ball, Tennis,..." 
            class="custom-input" 
          />
        </div>

        <div class="field-item">
          <label class="field-label">Movies</label>
          <input 
            type="text" 
            v-model="profile.hobbies.movies" 
            placeholder="e.g. Action, Romance,..." 
            class="custom-input" 
          />
        </div>
      </div>

      <!-- Buttons: Skip and Save & Continue -->
      <div class="actions-row">
        <button type="button" class="btn-skip" @click="handleSkip">
          Skip
        </button>
        <button type="submit" class="btn-save-continue" :disabled="isSaving">
          {{ isSaving ? 'Saving...' : 'Save & Continue' }}
        </button>
      </div>
    </form>

    <!-- Photo Crop Modal -->
    <div v-if="showCropModal" class="crop-overlay" @click.self="cancelCrop">
      <div class="crop-modal-card">
        <header class="crop-modal-header">
          <button type="button" class="crop-icon-btn" @click="cancelCrop">✕</button>
          <h4 class="crop-modal-title">Adjust Profile Photo</h4>
          <button type="button" class="crop-done-btn" @click="applyCrop">Done</button>
        </header>

        <div class="crop-canvas-wrapper" ref="cropWrapperRef">
          <canvas
            ref="cropCanvasRef"
            @mousedown="onCropMouseDown"
            @mousemove="onCropMouseMove"
            @mouseup="onCropMouseUp"
            @mouseleave="onCropMouseUp"
            @touchstart.prevent="onCropTouchStart"
            @touchmove.prevent="onCropTouchMove"
            @touchend="onCropTouchEnd"
            @wheel.prevent="onCropWheel"
          ></canvas>
        </div>

        <div class="crop-modal-controls">
          <div class="control-row">
            <span class="control-text">Zoom</span>
            <input
              type="range"
              min="0.5"
              max="3"
              step="0.01"
              v-model.number="cropZoom"
              class="control-slider"
              @input="drawCropCanvas"
            />
          </div>
          <div class="control-row">
            <span class="control-text">Rotate</span>
            <input
              type="range"
              min="-180"
              max="180"
              step="1"
              v-model.number="cropRotation"
              class="control-slider"
              @input="drawCropCanvas"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
/* global defineEmits */
import { ref, reactive, onMounted, nextTick } from 'vue'
import { auth, db, storage } from '../../firebase'
import { doc, getDoc, setDoc } from 'firebase/firestore'
import { ref as storageRef, uploadBytes, getDownloadURL } from 'firebase/storage'

const emit = defineEmits(['complete', 'skip'])

const isSaving = ref(false)
const fileInputRef = ref(null)
const fileErrorMsg = ref('')
const photoPreview = ref('')
const showCropModal = ref(false)
const cropCanvasRef = ref(null)
const cropWrapperRef = ref(null)

const cropZoom = ref(1)
const cropRotation = ref(0)
const cropOffsetX = ref(0)
const cropOffsetY = ref(0)
const isDragging = ref(false)
const dragStartX = ref(0)
const dragStartY = ref(0)
const dragStartOffsetX = ref(0)
const dragStartOffsetY = ref(0)
const lastTouchDist = ref(0)

let originalImage = null
let croppedBlob = null

const profile = reactive({
  dob: '',
  gender: '',
  phone: '',
  status: '',
  university: '',
  job: '',
  hobbies: {
    music: '',
    games: '',
    sports: '',
    movies: ''
  }
})

onMounted(async () => {
  // Load prefilled data from Firestore if user is logged in
  if (auth.currentUser) {
    try {
      const userDoc = await getDoc(doc(db, 'users', auth.currentUser.uid))
      if (userDoc.exists()) {
        const data = userDoc.data()
        if (data.avatar) photoPreview.value = data.avatar
        if (data.profile) {
          if (data.profile.dob) profile.dob = data.profile.dob
          if (data.profile.gender) profile.gender = data.profile.gender
          if (data.profile.phone) profile.phone = data.profile.phone
          if (data.profile.status) profile.status = data.profile.status
          if (data.profile.university) profile.university = data.profile.university
          if (data.profile.job) profile.job = data.profile.job
          if (data.profile.hobbies) {
            if (data.profile.hobbies.music) profile.hobbies.music = data.profile.hobbies.music
            if (data.profile.hobbies.games) profile.hobbies.games = data.profile.hobbies.games
            if (data.profile.hobbies.sports) profile.hobbies.sports = data.profile.hobbies.sports
            if (data.profile.hobbies.movies) profile.hobbies.movies = data.profile.hobbies.movies
          }
        }
      }
    } catch (err) {
      console.warn("Could not prefill user profile data:", err)
    }
  }
})

function triggerFileInput() {
  fileInputRef.value?.click()
}

function onFileSelected(e) {
  const file = e.target.files?.[0]
  if (!file) return

  if (file.size > 10 * 1024 * 1024) {
    fileErrorMsg.value = "File size must be under 10MB."
    setTimeout(() => { fileErrorMsg.value = '' }, 4000)
    return
  }
  fileErrorMsg.value = ''

  const reader = new FileReader()
  reader.onload = (event) => {
    const img = new Image()
    img.onload = () => {
      originalImage = img
      cropZoom.value = 1
      cropRotation.value = 0
      cropOffsetX.value = 0
      cropOffsetY.value = 0
      showCropModal.value = true
      nextTick(() => {
        setTimeout(() => initCropCanvas(), 100)
      })
    }
    img.src = event.target.result
  }
  reader.readAsDataURL(file)
  e.target.value = null
}

function initCropCanvas() {
  const canvas = cropCanvasRef.value
  const wrapper = cropWrapperRef.value
  if (!canvas || !wrapper) return

  const wrapperWidth = wrapper.clientWidth || 300
  const size = Math.min(wrapperWidth, 340)
  canvas.width = size * 2
  canvas.height = size * 2
  canvas.style.width = size + 'px'
  canvas.style.height = size + 'px'
  drawCropCanvas()
}

function drawCropCanvas() {
  const canvas = cropCanvasRef.value
  if (!canvas || !originalImage) return

  const ctx = canvas.getContext('2d')
  const w = canvas.width
  const h = canvas.height
  const cx = w / 2
  const cy = h / 2
  const circleRadius = Math.min(w, h) * 0.4

  ctx.clearRect(0, 0, w, h)

  ctx.save()
  ctx.translate(cx + cropOffsetX.value * 2, cy + cropOffsetY.value * 2)
  ctx.rotate((cropRotation.value * Math.PI) / 180)
  ctx.scale(cropZoom.value, cropZoom.value)

  const imgAspect = originalImage.width / originalImage.height
  let drawW, drawH
  if (imgAspect > 1) {
    drawH = h * 0.8
    drawW = drawH * imgAspect
  } else {
    drawW = w * 0.8
    drawH = drawW / imgAspect
  }
  ctx.drawImage(originalImage, -drawW / 2, -drawH / 2, drawW, drawH)
  ctx.restore()

  // Overlay outside circle
  ctx.save()
  ctx.fillStyle = 'rgba(0, 0, 0, 0.55)'
  ctx.fillRect(0, 0, w, h)

  // Cutout
  ctx.globalCompositeOperation = 'destination-out'
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.fill()
  ctx.restore()

  // Border ring
  ctx.save()
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)'
  ctx.lineWidth = 3
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.stroke()
  ctx.restore()
}

function onCropMouseDown(e) {
  isDragging.value = true
  dragStartX.value = e.clientX
  dragStartY.value = e.clientY
  dragStartOffsetX.value = cropOffsetX.value
  dragStartOffsetY.value = cropOffsetY.value
}

function onCropMouseMove(e) {
  if (!isDragging.value) return
  cropOffsetX.value = dragStartOffsetX.value + (e.clientX - dragStartX.value)
  cropOffsetY.value = dragStartOffsetY.value + (e.clientY - dragStartY.value)
  drawCropCanvas()
}

function onCropMouseUp() {
  isDragging.value = false
}

function onCropTouchStart(e) {
  if (e.touches.length === 1) {
    isDragging.value = true
    dragStartX.value = e.touches[0].clientX
    dragStartY.value = e.touches[0].clientY
    dragStartOffsetX.value = cropOffsetX.value
    dragStartOffsetY.value = cropOffsetY.value
  } else if (e.touches.length === 2) {
    isDragging.value = false
    const dx = e.touches[0].clientX - e.touches[1].clientX
    const dy = e.touches[0].clientY - e.touches[1].clientY
    lastTouchDist.value = Math.sqrt(dx * dx + dy * dy)
  }
}

function onCropTouchMove(e) {
  if (e.touches.length === 1 && isDragging.value) {
    cropOffsetX.value = dragStartOffsetX.value + (e.touches[0].clientX - dragStartX.value)
    cropOffsetY.value = dragStartOffsetY.value + (e.touches[0].clientY - dragStartY.value)
    drawCropCanvas()
  } else if (e.touches.length === 2) {
    const dx = e.touches[0].clientX - e.touches[1].clientX
    const dy = e.touches[0].clientY - e.touches[1].clientY
    const dist = Math.sqrt(dx * dx + dy * dy)
    if (lastTouchDist.value > 0) {
      const scale = dist / lastTouchDist.value
      cropZoom.value = Math.max(0.5, Math.min(3, cropZoom.value * scale))
      drawCropCanvas()
    }
    lastTouchDist.value = dist
  }
}

function onCropTouchEnd() {
  isDragging.value = false
  lastTouchDist.value = 0
}

function onCropWheel(e) {
  const delta = e.deltaY > 0 ? -0.05 : 0.05
  cropZoom.value = Math.max(0.5, Math.min(3, cropZoom.value + delta))
  drawCropCanvas()
}

function cancelCrop() {
  showCropModal.value = false
  originalImage = null
}

function applyCrop() {
  if (!originalImage || !cropCanvasRef.value) return

  const sourceCanvas = cropCanvasRef.value
  const w = sourceCanvas.width
  const h = sourceCanvas.height
  const cx = w / 2
  const cy = h / 2
  const circleRadius = Math.min(w, h) * 0.4
  const outputSize = Math.round(circleRadius * 2)

  const outputCanvas = document.createElement('canvas')
  outputCanvas.width = outputSize
  outputCanvas.height = outputSize
  const outCtx = outputCanvas.getContext('2d')

  const tempCanvas = document.createElement('canvas')
  tempCanvas.width = w
  tempCanvas.height = h
  const tempCtx = tempCanvas.getContext('2d')

  tempCtx.translate(cx + cropOffsetX.value * 2, cy + cropOffsetY.value * 2)
  tempCtx.rotate((cropRotation.value * Math.PI) / 180)
  tempCtx.scale(cropZoom.value, cropZoom.value)

  const imgAspect = originalImage.width / originalImage.height
  let drawW, drawH
  if (imgAspect > 1) {
    drawH = h * 0.8
    drawW = drawH * imgAspect
  } else {
    drawW = w * 0.8
    drawH = drawW / imgAspect
  }
  tempCtx.drawImage(originalImage, -drawW / 2, -drawH / 2, drawW, drawH)

  outCtx.beginPath()
  outCtx.arc(outputSize / 2, outputSize / 2, outputSize / 2, 0, Math.PI * 2)
  outCtx.closePath()
  outCtx.clip()

  outCtx.drawImage(
    tempCanvas,
    cx - circleRadius,
    cy - circleRadius,
    circleRadius * 2,
    circleRadius * 2,
    0,
    0,
    outputSize,
    outputSize
  )

  outputCanvas.toBlob((blob) => {
    if (!blob) return
    croppedBlob = blob
    photoPreview.value = URL.createObjectURL(blob)
    showCropModal.value = false
    originalImage = null
  }, 'image/jpeg', 0.9)
}

function handleSkip() {
  emit('skip')
}

async function handleSaveAndContinue() {
  isSaving.value = true
  try {
    if (auth.currentUser) {
      const uid = auth.currentUser.uid
      let avatarUrl = ''
      if (croppedBlob) {
        const fileRef = storageRef(storage, `users/${uid}/profilePic`)
        await uploadBytes(fileRef, croppedBlob)
        avatarUrl = await getDownloadURL(fileRef)
      }

      const saveData = {
        profile: {
          dob: profile.dob,
          gender: profile.gender,
          phone: profile.phone,
          status: profile.status,
          university: profile.university,
          job: profile.job,
          hobbies: profile.hobbies,
          updatedAt: new Date().toISOString()
        }
      }
      if (avatarUrl) {
        saveData.avatar = avatarUrl
      }
      await setDoc(doc(db, 'users', uid), saveData, { merge: true })
    }
    emit('complete')
  } catch (err) {
    console.error("Error saving profile details:", err)
    // Advance anyway so user is not stuck
    emit('complete')
  } finally {
    isSaving.value = false
  }
}
</script>

<style scoped>
.profile-step-container {
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
  margin-bottom: 28px;
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

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* Avatar Section */
.avatar-section {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-bottom: 8px;
}

.avatar-preview-wrapper {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #FAF8F5;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid #EDE8E3;
  flex-shrink: 0;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-actions {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
}

.btn-upload-photo {
  background: #ffffff;
  border: 1px solid #5C4E4E;
  border-radius: 9999px;
  color: #5C4E4E;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 5px 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-upload-photo:hover {
  background: #FAF8F5;
}

.avatar-hint {
  font-size: 0.72rem;
  color: #8C7E7E;
}

.hidden-file-input {
  display: none;
}

/* Form Group Sections */
.form-group-section {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.group-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 2px;
}

.field-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field-label {
  font-size: 0.88rem;
  font-weight: 600;
  color: #5C4E4E;
}

.custom-input {
  width: 100%;
  padding: 12px 14px;
  border: 1.5px solid #D1D5DB;
  border-radius: 10px;
  font-size: 0.92rem;
  font-family: inherit;
  color: #2A2421;
  background: #ffffff;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-sizing: border-box;
}

.custom-input:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.custom-input::placeholder {
  color: #8C7E7E;
}

/* Custom Select */
.select-wrapper {
  position: relative;
  width: 100%;
}

.custom-select {
  width: 100%;
  padding: 12px 36px 12px 14px;
  border: 1.5px solid #D1D5DB;
  border-radius: 10px;
  font-size: 0.92rem;
  font-family: inherit;
  color: #2A2421;
  background: #ffffff;
  outline: none;
  appearance: none;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-sizing: border-box;
}

.custom-select:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.select-chevron {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  color: #8C7E7E;
  display: flex;
  align-items: center;
}

/* Actions Row */
.actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 12px;
  padding-top: 12px;
}

.btn-skip {
  padding: 12px 28px;
  border: 1px solid #EDE8E3;
  border-radius: 10px;
  background: #ffffff;
  color: #5C4E4E;
  font-weight: 600;
  font-size: 0.95rem;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-skip:hover {
  background: #FAF8F5;
  border-color: #5C4E4E;
  color: #2A2421;
}

.btn-save-continue {
  flex: 1;
  padding: 14px 28px;
  border: none;
  border-radius: 10px;
  background: #5C4E4E;
  color: #ffffff;
  font-weight: 600;
  font-size: 0.95rem;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.15);
}

.btn-save-continue:hover:not(:disabled) {
  background: #473B3B;
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.25);
}

.btn-save-continue:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Crop Modal */
.crop-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(42, 36, 33, 0.65);
  backdrop-filter: blur(4px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.crop-modal-card {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #EDE8E3;
  width: 100%;
  max-width: 400px;
  padding: 20px;
  box-shadow: 0 20px 25px -5px rgba(42, 36, 33, 0.2);
}

.crop-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.crop-modal-title {
  font-size: 1rem;
  font-weight: 700;
  color: #2A2421;
}

.crop-icon-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #8C7E7E;
}

.crop-done-btn {
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 6px 14px;
  font-size: 0.85rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s;
}

.crop-done-btn:hover {
  background: #473B3B;
}

.crop-canvas-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 16px;
}

.crop-modal-controls {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.control-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.control-text {
  width: 50px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #5C4E4E;
}

.control-slider {
  flex: 1;
}
</style>
