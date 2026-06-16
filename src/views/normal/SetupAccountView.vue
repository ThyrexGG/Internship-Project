<template>
  <div class="setup-page">
    <div class="setup-container">
      <header class="setup-header">
        <h1 class="setup-title">Complete your profile</h1>
        <p class="setup-subtitle">
          Tell us a little more about yourself. You can fill this out now to get better recommendations, or skip and do it later.
        </p>
      </header>

      <form class="setup-form" @submit.prevent="handleSave">
        <!-- Section: Profile Photo -->
        <section class="form-section photo-section">
          <h2 class="section-title">Profile Photo</h2>
          <div class="photo-upload-area">
            <div class="avatar-preview" @click="triggerFileInput">
              <img v-if="photoPreview" :src="photoPreview" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="Profile preview" class="avatar-img" />
              <div v-else class="avatar-placeholder">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="1.5">
                  <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" />
                  <circle cx="12" cy="7" r="4" />
                </svg>
              </div>
              <div class="avatar-overlay">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">
                  <path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z" />
                  <circle cx="12" cy="13" r="4" />
                </svg>
              </div>
            </div>
            <div class="photo-info">
              <button type="button" class="btn-upload" @click="triggerFileInput">
                {{ photoPreview ? 'Change Photo' : 'Upload Photo' }}
              </button>
              <p class="photo-hint">JPG, PNG or WebP. Max 10MB.</p>
            </div>
            <input
              ref="fileInputRef"
              type="file"
              accept="image/jpeg,image/png,image/webp"
              class="hidden-input"
              @change="onFileSelected"
            />
          </div>
        </section>

        <!-- Section: Personal -->
        <section class="form-section">
          <h2 class="section-title">Personal Details</h2>
          <div class="form-grid">
            <div class="field-group">
              <label>Date of Birth</label>
              <input type="date" v-model="profile.dob" class="field-input" />
            </div>
            <div class="field-group">
              <label>Gender</label>
              <select v-model="profile.gender" class="field-input">
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <div class="field-group full-width">
              <label>Phone Number</label>
              <input type="tel" v-model="profile.phone" placeholder="+1 234 567 8900" class="field-input" />
            </div>
          </div>
        </section>

        <!-- Section: Education & Work -->
        <section class="form-section">
          <h2 class="section-title">Education & Work</h2>
          <div class="form-grid">
            <div class="field-group">
              <label>Status</label>
              <select v-model="profile.status" class="field-input">
                <option value="">Select Status</option>
                <option value="Student">Student</option>
                <option value="Professional">Professional</option>
              </select>
            </div>
            <div class="field-group">
              <label>University</label>
              <input type="text" v-model="profile.university" placeholder="e.g. Harvard University" class="field-input" />
            </div>
            <div class="field-group full-width">
              <label>Job Title / Occupation</label>
              <input type="text" v-model="profile.job" placeholder="e.g. Software Engineer" class="field-input" />
            </div>
          </div>
        </section>

        <!-- Section: Hobbies -->
        <section class="form-section">
          <h2 class="section-title">Hobbies</h2>
          <p class="section-desc">What do you like to do in your free time?</p>
          <div class="form-grid">
            <div class="field-group">
              <label>Music Genre</label>
              <input type="text" v-model="profile.hobbies.music" placeholder="Pop, Rock, Jazz..." class="field-input" />
            </div>
            <div class="field-group">
              <label>Games</label>
              <input type="text" v-model="profile.hobbies.games" placeholder="Board games, Video games..." class="field-input" />
            </div>
            <div class="field-group">
              <label>Sports</label>
              <input type="text" v-model="profile.hobbies.sports" placeholder="Basketball, Tennis..." class="field-input" />
            </div>
            <div class="field-group">
              <label>Movies</label>
              <input type="text" v-model="profile.hobbies.movies" placeholder="Action, Comedy..." class="field-input" />
            </div>
          </div>
        </section>

        <!-- Action Buttons -->
        <div class="form-actions">
          <button type="button" class="btn-outline" @click="handleSkip">Skip for now</button>
          <button type="submit" class="btn-primary" :disabled="isSaving">
            {{ isSaving ? 'Saving...' : 'Save & Continue' }}
          </button>
        </div>
      </form>
    </div>

    <!-- Crop Modal -->
      <div v-if="showCropModal" class="crop-overlay" @click.self="cancelCrop">
        <div class="crop-modal">
          <header class="crop-header">
            <button type="button" class="crop-close-btn" @click="cancelCrop">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 6L6 18M6 6l12 12" />
              </svg>
            </button>
            <h2 class="crop-title">Adjust Photo</h2>
            <button type="button" class="crop-done-btn" @click="applyCrop">Done</button>
          </header>

          <div class="crop-body">
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
              <!-- Circular overlay drawn via canvas -->
            </div>
          </div>

          <div class="crop-controls">
            <div class="control-group">
              <label class="control-label">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8" />
                  <path d="M21 21l-4.35-4.35" />
                  <path d="M11 8v6M8 11h6" />
                </svg>
                Zoom
              </label>
              <input
                type="range"
                min="0.5"
                max="3"
                step="0.01"
                v-model.number="cropZoom"
                class="range-slider"
                @input="drawCropCanvas"
              />
            </div>
            <div class="control-group">
              <label class="control-label">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21.5 2v6h-6M2.5 22v-6h6" />
                  <path d="M2 11.5a10 10 0 0118.8-4.3M22 12.5a10 10 0 01-18.8 4.2" />
                </svg>
                Rotate
              </label>
              <input
                type="range"
                min="-180"
                max="180"
                step="1"
                v-model.number="cropRotation"
                class="range-slider"
                @input="drawCropCanvas"
              />
            </div>
            <div class="control-quick-actions">
              <button type="button" class="quick-action-btn" @click="rotateLeft">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M2.5 2v6h6" />
                  <path d="M2 11.5a10 10 0 0118.8-4.3" />
                </svg>
              </button>
              <button type="button" class="quick-action-btn" @click="rotateRight">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21.5 2v6h-6" />
                  <path d="M22 11.5A10 10 0 003.2 7.2" />
                </svg>
              </button>
              <button type="button" class="quick-action-btn" @click="resetCrop">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 12a9 9 0 1018-0 9 9 0 00-18 0z" />
                  <path d="M12 8v4l2 2" />
                </svg>
                Reset
              </button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick, watch } from 'vue'
import { useRouter } from 'vue-router'
import { auth, db, storage } from '../../firebase'
import { onAuthStateChanged } from 'firebase/auth'
import { doc, getDoc, setDoc } from 'firebase/firestore'
import { ref as storageRef, uploadBytes, getDownloadURL } from 'firebase/storage'

const router = useRouter()
const isSaving = ref(false)

const defaultAvatar = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23dfa37b'/><stop offset='100%' stop-color='%23c0784a'/></linearGradient></defs><circle cx='50' cy='50' r='50' fill='url(%23g)'/><circle cx='50' cy='37' r='17' fill='%23fff'/><path d='M50 58c-18 0-32 9-32 20v4h64v-4c0-11-14-20-32-20z' fill='%23fff'/></svg>"

function setDefaultAvatar(event) {
  event.target.src = defaultAvatar
}

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

// --- Photo upload & crop state ---
const fileInputRef = ref(null)
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

// Touch pinch state
const lastTouchDist = ref(0)

let originalImage = null
let croppedBlob = null

function triggerFileInput() {
  fileInputRef.value?.click()
}

function onFileSelected(event) {
  const file = event.target.files[0]
  if (!file) return

  // Validate file size (10MB max)
  if (file.size > 10 * 1024 * 1024) {
    alert('File size must be less than 10MB.')
    return
  }

  const reader = new FileReader()
  reader.onload = (e) => {
    const img = new Image()
    img.onload = () => {
      originalImage = img
      cropZoom.value = 1
      cropRotation.value = 0
      cropOffsetX.value = 0
      cropOffsetY.value = 0
      showCropModal.value = true
      // Wait for Teleport DOM to be fully laid out
      nextTick(() => {
        setTimeout(() => {
          initCropCanvas()
        }, 100)
      })
    }
    img.src = e.target.result
  }
  reader.readAsDataURL(file)

  // Reset input so same file can be re-selected
  event.target.value = null
}

function initCropCanvas() {
  const canvas = cropCanvasRef.value
  const wrapper = cropWrapperRef.value
  if (!canvas || !wrapper) {
    // Retry if DOM refs aren't ready yet
    setTimeout(() => initCropCanvas(), 50)
    return
  }

  // Fallback to 360 if wrapper hasn't laid out yet
  const wrapperWidth = wrapper.clientWidth || 360
  const size = Math.min(wrapperWidth, 400)
  canvas.width = size * 2 // HiDPI
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

  // Clear
  ctx.clearRect(0, 0, w, h)

  // Draw image
  ctx.save()
  ctx.translate(cx + cropOffsetX.value * 2, cy + cropOffsetY.value * 2)
  ctx.rotate((cropRotation.value * Math.PI) / 180)
  ctx.scale(cropZoom.value, cropZoom.value)

  // Scale image to fit within canvas while maintaining aspect ratio
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

  // Dark overlay outside the circle
  ctx.save()
  ctx.fillStyle = 'rgba(0, 0, 0, 0.55)'
  ctx.fillRect(0, 0, w, h)

  // Cut out circle
  ctx.globalCompositeOperation = 'destination-out'
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.fill()
  ctx.restore()

  // Draw circle border
  ctx.save()
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.7)'
  ctx.lineWidth = 3
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.stroke()
  ctx.restore()
}

// --- Mouse events for dragging ---
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

// --- Touch events for dragging & pinch-to-zoom ---
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

// --- Mouse wheel zoom ---
function onCropWheel(e) {
  const delta = e.deltaY > 0 ? -0.05 : 0.05
  cropZoom.value = Math.max(0.5, Math.min(3, cropZoom.value + delta))
  drawCropCanvas()
}

// --- Quick actions ---
function rotateLeft() {
  cropRotation.value = ((cropRotation.value - 90 + 180) % 360) - 180
  drawCropCanvas()
}

function rotateRight() {
  cropRotation.value = ((cropRotation.value + 90 + 180) % 360) - 180
  drawCropCanvas()
}

function resetCrop() {
  cropZoom.value = 1
  cropRotation.value = 0
  cropOffsetX.value = 0
  cropOffsetY.value = 0
  drawCropCanvas()
}

function cancelCrop() {
  showCropModal.value = false
  originalImage = null
}

function applyCrop() {
  if (!originalImage || !cropCanvasRef.value) return

  // Create an off-screen canvas to extract the circular crop region
  const sourceCanvas = cropCanvasRef.value
  const w = sourceCanvas.width
  const h = sourceCanvas.height
  const cx = w / 2
  const cy = h / 2
  const circleRadius = Math.min(w, h) * 0.4

  // Output canvas at the crop circle size
  const outputSize = Math.round(circleRadius * 2)
  const outputCanvas = document.createElement('canvas')
  outputCanvas.width = outputSize
  outputCanvas.height = outputSize
  const outCtx = outputCanvas.getContext('2d')

  // Draw the transformed image (without overlay) onto a temp canvas
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

  // Clip the circle from temp canvas to output
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

  outputCanvas.toBlob(
    (blob) => {
      if (!blob) {
        alert('Failed to crop image. Please try again.')
        return
      }
      croppedBlob = blob
      photoPreview.value = URL.createObjectURL(blob)
      showCropModal.value = false
      originalImage = null
    },
    'image/jpeg',
    0.9
  )
}

// --- Auth & Save ---
onMounted(() => {
  onAuthStateChanged(auth, async (user) => {
    if (!user) {
      router.push('/login')
    } else {
      // Prefill existing user details and avatar from Firestore
      try {
        const userDoc = await getDoc(doc(db, 'users', user.uid))
        if (userDoc.exists()) {
          const data = userDoc.data()
          if (data.avatar) {
            photoPreview.value = data.avatar
          }
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
        console.error("Error prefilling user profile:", err)
      }
    }
  })
})

function handleSkip() {
  router.push('/home')
}

async function handleSave() {
  if (!auth.currentUser) return;
  isSaving.value = true;

  try {
    const uid = auth.currentUser.uid;

    let avatarUrl = '';

    // Upload cropped photo to Firebase Storage
    if (croppedBlob) {
      const fileRef = storageRef(storage, `users/${uid}/profilePic`);
      await uploadBytes(fileRef, croppedBlob);
      avatarUrl = await getDownloadURL(fileRef);
    }

    // Build the data to save
    const saveData = {
      profile: {
        dob: profile.dob,
        gender: profile.gender,
        phone: profile.phone,
        status: profile.status,
        university: profile.university,
        job: profile.job,
        hobbies: profile.hobbies,
        profileCompletedAt: new Date().toISOString()
      }
    };

    if (avatarUrl) {
      saveData.avatar = avatarUrl;
    }

    await setDoc(doc(db, "users", uid), saveData, { merge: true });

    router.push('/home')
  } catch (err) {
    console.error("Error saving profile:", err);
    alert("Failed to save profile. Please try again.");
  } finally {
    isSaving.value = false;
  }
}

// Watch for modal open to re-init canvas on resize
watch(showCropModal, (val) => {
  if (val) {
    nextTick(() => {
      setTimeout(() => initCropCanvas(), 100)
    })
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Serif+Display&display=swap');

.setup-page {
  height: 100vh;
  overflow-y: auto;
  background: #f9f9f9;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 60px 20px;
  font-family: 'DM Sans', sans-serif;
}

.setup-container {
  background: #fff;
  width: 100%;
  max-width: 600px;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.04);
  padding: 40px;
}

.setup-header {
  text-align: center;
  margin-bottom: 40px;
}

.setup-title {
  font-family: 'DM Serif Display', serif;
  font-size: 2.2rem;
  color: #111;
  margin-bottom: 12px;
}

.setup-subtitle {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.5;
  max-width: 450px;
  margin: 0 auto;
}

.setup-form {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #222;
  border-bottom: 1px solid #eee;
  padding-bottom: 8px;
}

.section-desc {
  font-size: 0.85rem;
  color: #888;
  margin-top: -8px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.field-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.full-width {
  grid-column: 1 / -1;
}

.field-group label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #444;
}

.field-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 0.9rem;
  color: #333;
  background: #fafafa;
  transition: all 0.2s;
  font-family: inherit;
  outline: none;
}

.field-input:focus {
  border-color: #111;
  background: #fff;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 16px;
  margin-top: 20px;
  border-top: 1px solid #eee;
  padding-top: 32px;
}

.btn-outline {
  padding: 12px 24px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: transparent;
  color: #555;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-outline:hover {
  background: #f5f5f5;
  color: #111;
}

.btn-primary {
  padding: 12px 32px;
  border: none;
  border-radius: 10px;
  background: #111;
  color: #fff;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary:hover {
  background: #333;
}

.btn-primary:disabled {
  background: #888;
  cursor: not-allowed;
}

/* ===== Photo Upload Section ===== */

.photo-section {
  align-items: center;
}

.photo-upload-area {
  display: flex;
  align-items: center;
  gap: 24px;
}

.avatar-preview {
  position: relative;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  cursor: pointer;
  background: #f0f0f0;
  border: 3px solid #eee;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.avatar-preview:hover {
  border-color: #111;
  transform: scale(1.03);
}

.avatar-preview:hover .avatar-overlay {
  opacity: 1;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(145deg, #f5f5f5, #e8e8e8);
}

.avatar-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.25s ease;
  border-radius: 50%;
}

.photo-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.btn-upload {
  padding: 10px 20px;
  border: 1.5px solid #111;
  border-radius: 10px;
  background: transparent;
  color: #111;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.btn-upload:hover {
  background: #111;
  color: #fff;
}

.photo-hint {
  font-size: 0.75rem;
  color: #999;
  margin: 0;
}

.hidden-input {
  display: none;
}

/* ===== Crop Modal ===== */

.crop-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.crop-modal {
  background: #1a1a1a;
  border-radius: 20px;
  width: 95%;
  max-width: 460px;
  overflow: hidden;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.5);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.crop-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.crop-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
  margin: 0;
}

.crop-close-btn {
  background: rgba(255, 255, 255, 0.08);
  border: none;
  color: #aaa;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}

.crop-close-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

.crop-done-btn {
  background: #fff;
  border: none;
  color: #111;
  padding: 8px 20px;
  border-radius: 10px;
  font-weight: 700;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.crop-done-btn:hover {
  background: #e5e5e5;
}

.crop-body {
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.crop-canvas-wrapper {
  width: 100%;
  max-width: 400px;
  aspect-ratio: 1;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
}

.crop-canvas-wrapper canvas {
  display: block;
  cursor: grab;
  border-radius: 16px;
}

.crop-canvas-wrapper canvas:active {
  cursor: grabbing;
}

.crop-controls {
  padding: 16px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.control-group {
  display: flex;
  align-items: center;
  gap: 14px;
}

.control-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #888;
  min-width: 80px;
  white-space: nowrap;
}

.range-slider {
  -webkit-appearance: none;
  appearance: none;
  flex: 1;
  height: 4px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.12);
  outline: none;
  transition: background 0.2s;
}

.range-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.15s ease;
}

.range-slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.range-slider::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  border: none;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

.control-quick-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding-top: 4px;
}

.quick-action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  border: none;
  color: #aaa;
  padding: 8px 14px;
  border-radius: 10px;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.quick-action-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

/* ===== Responsive ===== */

@media (max-width: 600px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
  .setup-container {
    padding: 24px;
  }
  .form-actions {
    flex-direction: column;
  }
  .form-actions button {
    width: 100%;
  }
  .photo-upload-area {
    flex-direction: column;
    text-align: center;
  }
  .photo-info {
    align-items: center;
  }
  .crop-modal {
    max-width: 100%;
    border-radius: 16px 16px 0 0;
    max-height: 95vh;
    overflow-y: auto;
  }
}
</style>
