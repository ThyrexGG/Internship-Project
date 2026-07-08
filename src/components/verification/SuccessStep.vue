<template>
  <div class="success-screen">
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
        <button class="btn-primary" @click="router.push('/home')">
          Return to Dashboard
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>
