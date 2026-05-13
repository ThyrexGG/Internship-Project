<template>
  <div class="verify-account-page">
    <header class="top-nav">
      <button class="back-btn" type="button" @click="$router.push('/home')">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
      </button>
      <h1 class="page-title">Verify Account</h1>
      <div class="placeholder-spacer"></div>
    </header>

    <main class="content">
      <div class="upload-section">
        <h2 class="section-title">Upload National ID</h2>
        <p class="section-subtitle">Please upload a clear photo of your Cambodian National ID for verification.</p>

        <div class="upload-box" @click="triggerFileInput">
          <input type="file" ref="fileInput" accept="image/*" class="hidden-input" @change="handleFileChange" />
          <div v-if="previewImage" class="preview-container">
            <img :src="previewImage" alt="ID Preview" class="preview-image" />
          </div>
          <div v-else class="upload-placeholder">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
            <span>Tap to upload or take a photo</span>
          </div>
        </div>

        <button class="btn-primary" :disabled="!selectedFile" @click="handleUpload">
          Submit for Verification
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const selectedFile = ref(null)
const previewImage = ref(null)

function triggerFileInput() {
  if (fileInput.value) {
    fileInput.value.click()
  }
}

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    previewImage.value = URL.createObjectURL(file)
  }
}

function handleUpload() {
  if (!selectedFile.value) return
  alert('Upload triggered. OCR integration will happen here later.')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.verify-account-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  background: #fdfdfd;
  font-family: 'DM Sans', sans-serif;
}

.top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid #f2f2f2;
  background: #fff;
}

.back-btn {
  background: none; border: none; cursor: pointer; color: #111;
  display: flex; align-items: center; justify-content: center;
}

.page-title {
  font-size: 1.1rem; font-weight: 600; color: #111;
}

.placeholder-spacer { width: 24px; }

.content {
  flex: 1; padding: 24px 20px; overflow-y: auto;
}

.section-title {
  font-size: 1.2rem; font-weight: 600; color: #111; margin-bottom: 8px;
}

.section-subtitle {
  font-size: 0.9rem; color: #666; margin-bottom: 24px; line-height: 1.5;
}

.upload-box {
  width: 100%;
  height: 220px;
  border: 2px dashed #ddd;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: #fafafa;
  transition: border-color 0.2s, background 0.2s;
  overflow: hidden;
  margin-bottom: 32px;
}
.upload-box:hover { border-color: #bbb; background: #f0f0f0; }

.hidden-input { display: none; }

.upload-placeholder {
  display: flex; flex-direction: column; align-items: center; gap: 12px; color: #999; font-size: 0.9rem; font-weight: 500;
}

.preview-container { width: 100%; height: 100%; }
.preview-image { width: 100%; height: 100%; object-fit: contain; background: #000; }

.btn-primary {
  width: 100%; padding: 14px; background: #111; color: #fff;
  border: none; border-radius: 12px; font-size: 0.95rem; font-weight: 600;
  cursor: pointer; transition: background 0.2s;
}
.btn-primary:disabled { background: #ccc; cursor: not-allowed; }
.btn-primary:active:not(:disabled) { transform: scale(0.98); }
</style>
