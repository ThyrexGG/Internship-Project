<template>
  <div class="success-screen">
    <div class="success-card">
      <!-- Animated Checkmark Badge -->
      <div class="success-badge-wrapper">
        <div class="pulse-ring"></div>
        <div class="success-badge">
          <svg viewBox="0 0 100 100" class="badge-check-svg">
            <circle cx="50" cy="50" r="40" fill="#5C4E4E" />
            <path d="M35 50 L45 60 L65 40" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" class="check-draw"/>
          </svg>
        </div>
      </div>

      <h2 class="success-title">Dossier Submitted for Review</h2>
      <p class="success-subtitle">Your biometric identity data has been securely encrypted and submitted to the HomeSweet Trust &amp; Safety team.</p>

      <!-- Verified Details Section -->
      <div class="verification-details-box">
        <div class="review-status-pill">
          <span class="pulse-dot"></span>
          <span>Status: Under Compliance Review (Est. 15 mins)</span>
        </div>

        <h3 class="details-title">Security &amp; Match Summary</h3>
        <div class="details-list">
          <div class="detail-item">
            <span class="icon">✓</span>
            <span class="label">Document Authenticity</span>
            <span class="value success">OCR Encrypted</span>
          </div>
          <div class="detail-item">
            <span class="icon">✓</span>
            <span class="label">Biometric Face Match</span>
            <span class="value success">Match Confirmed (98.6%)</span>
          </div>
          <div class="detail-item">
            <span class="icon">✓</span>
            <span class="label">Interactive Liveness</span>
            <span class="value success">Anti-Spoofing Passed</span>
          </div>
        </div>
        
        <div class="security-seal">
          <svg class="shield-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <span>Encrypted with 256-bit Identity Protection</span>
        </div>
      </div>

      <p class="trust-notice-text">
        <strong>Why we verify:</strong> To ensure safety, trust, and secure contracts for everyone on HomeSweet. You will receive an in-app notification once your verified badge is activated.
      </p>

      <div class="action-buttons">
        <button class="btn-primary" @click="router.push('/home')">
          Return to Home Listings
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>

<style scoped>
.success-screen {
  width: 100%;
  animation: fadeIn 0.3s ease;
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.success-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 10px 0;
}

.success-badge-wrapper {
  position: relative;
  width: 80px;
  height: 80px;
  margin-bottom: 20px;
}

.pulse-ring {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid rgba(46, 125, 50, 0.4);
  animation: pulse 1.8s infinite ease-out;
}

@keyframes pulse {
  0% { transform: scale(0.95); opacity: 1; }
  100% { transform: scale(1.25); opacity: 0; }
}

.success-badge {
  width: 100%;
  height: 100%;
}

.badge-check-svg circle {
  fill: #2E7D32;
}

.success-title {
  font-size: 1.85rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 8px;
}

.success-subtitle {
  font-size: 0.95rem;
  color: #8C7E7E;
  margin-bottom: 28px;
  max-width: 380px;
  line-height: 1.5;
}

.verification-details-box {
  width: 100%;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  border-radius: 14px;
  padding: 20px;
  margin-bottom: 20px;
}

.review-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #FEF3C7;
  color: #D97706;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 50px;
  margin-bottom: 16px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D97706;
  animation: pulse 1.5s infinite;
}

.trust-notice-text {
  font-size: 0.82rem;
  color: #8C7E7E;
  line-height: 1.5;
  margin-bottom: 24px;
  max-width: 420px;
  text-align: left;
}

.details-title {
  font-size: 1rem;
  font-weight: 700;
  color: #5C4E4E;
  margin-bottom: 16px;
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
  font-size: 0.9rem;
}

.detail-item .icon {
  color: #2E7D32;
  font-weight: 700;
  margin-right: 8px;
}

.detail-item .label {
  flex: 1;
  color: #2A2421;
  font-weight: 500;
}

.detail-item .value.success {
  color: #2E7D32;
  font-weight: 600;
}

.security-seal {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid #EDE8E3;
  font-size: 0.78rem;
  color: #8C7E7E;
}

.shield-icon {
  width: 14px;
  height: 14px;
  color: #5C4E4E;
}

.action-buttons {
  width: 100%;
}

.btn-primary {
  width: 100%;
  padding: 14px 28px;
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.15);
}

.btn-primary:hover {
  background: #473B3B;
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.25);
}
</style>
