<template>
  <div class="login-page">
    <!-- Left Panel: Hero Image -->
    <div class="hero-panel">
      <div class="hero-overlay" />
      <img
        src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80"
        alt="Luxury Home"
        class="hero-image"
      />
      <div class="logo">
        <div class="logo-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 18 L16 18" />
            <path d="M4 18 L4 12 L9 7 L16 14" />
            <path d="M12 18 L12 4 L16 4 L16 18 Z" />
            <path d="M12 14 L16 14" />
          </svg>
        </div>
        <span class="logo-text">HomeSweet</span>
      </div>

      <div class="hero-content">
        <h1 class="hero-title">Find your<br />sweet home</h1>
        <p class="hero-subtitle">
          Welcome to your comfort zone.<br />
          Schedule a visit in just a few clicks.
        </p>
        <div class="hero-dots">
          <span class="dot active" />
          <span class="dot" />
          <span class="dot" />
        </div>
      </div>

      <!-- Stats bar -->
      <div class="hero-stats">
        <div class="stat">
          <span class="stat-value">2.4k+</span>
          <span class="stat-label">Listings</span>
        </div>
        <div class="stat-divider" />
        <div class="stat">
          <span class="stat-value">98%</span>
          <span class="stat-label">Satisfaction</span>
        </div>
        <div class="stat-divider" />
        <div class="stat">
          <span class="stat-value">12yr</span>
          <span class="stat-label">Experience</span>
        </div>
      </div>
    </div>

    <!-- Right Panel -->
    <div class="form-panel">
      <div class="form-inner">
        <!-- Mobile Logo -->
        <div class="mobile-logo">
          <div class="logo-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 18 L16 18" />
              <path d="M4 18 L4 12 L9 7 L16 14" />
              <path d="M12 18 L12 4 L16 4 L16 18 Z" />
              <path d="M12 14 L16 14" />
            </svg>
          </div>
          <span class="logo-text">HomeSweet</span>
        </div>

        <!-- Tabs -->
        <div class="auth-tabs">
          <button class="tab-btn" :class="{ active: activeTab === 'login' }" @click="activeTab = 'login'">
            Login
          </button>
          <button class="tab-btn" :class="{ active: activeTab === 'signup' }" @click="activeTab = 'signup'">
            Sign up
          </button>
        </div>

        <!-- Header -->
        <div class="form-header">
          <h2 class="form-title">
            {{ activeTab === 'login' ? 'Welcome back!' : 'Create account' }}
          </h2>
          <p class="form-subtitle">
            {{ activeTab === 'login'
              ? 'Enter your credentials to access your account.'
              : 'Fill in the details below to get started.' }}
          </p>
        </div>

        <!-- Form -->
        <form class="auth-form" @submit.prevent="handleSubmit">
          <div class="field-group">
            <label class="field-label">Email address</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>
              </svg>
              <input
                v-model="email"
                type="email"
                placeholder="your@email.com"
                class="field-input"
                :class="{ error: errors.email }"
                autocomplete="email"
              />
            </div>
            <span v-if="errors.email" class="field-error">{{ errors.email }}</span>
          </div>

          <div v-if="activeTab === 'signup'" class="field-group">
            <label class="field-label">Full name</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
              </svg>
              <input v-model="name" type="text" placeholder="John Doe" class="field-input" autocomplete="name" />
            </div>
          </div>

          <div class="field-group">
            <div class="field-label-row">
              <label class="field-label">Password</label>
              <button v-if="activeTab === 'login'" type="button" class="forgot-link" @click="handleForgotPassword">
                Forgot password?
              </button>
            </div>
            <div class="input-wrapper password-wrapper">
              <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>
              </svg>
              <input
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="••••••••"
                class="field-input"
                :class="{ error: errors.password }"
                autocomplete="current-password"
              />
              <button type="button" class="toggle-pw" @click="showPassword = !showPassword">
                <svg v-if="!showPassword" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
                </svg>
                <svg v-else width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                </svg>
              </button>
            </div>
            <span v-if="errors.password" class="field-error">{{ errors.password }}</span>
          </div>

          <!-- Remember me (login only) -->
          <div v-if="activeTab === 'login'" class="remember-row">
            <label class="check-label">
              <input type="checkbox" v-model="rememberMe" class="check-input" />
              <span class="check-box" />
              <span class="check-text">Remember me</span>
            </label>
          </div>

          <button type="submit" class="btn-primary" :disabled="isLoading">
            <span v-if="isLoading" class="spinner" />
            <span v-else>{{ activeTab === 'login' ? 'Log In' : 'Create Account' }}</span>
          </button>
        </form>

        <!-- Divider -->
        <div class="divider">
          <span class="divider-line" /><span class="divider-text">or continue with</span><span class="divider-line" />
        </div>

        <!-- Social Buttons -->
        <div class="social-buttons">
          <button class="btn-social" @click="handleSocial('google')">
            <svg width="17" height="17" viewBox="0 0 24 24">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
            Google
          </button>
          <button class="btn-social" @click="handleSocial('apple')">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51c1.54-.06 2.84.88 3.99.88 1.11 0 2.79-.87 4.3-.87 2.22 0 4.29 1.37 5.29 3.44-.23.14-2.29 1.31-2.27 4.04.02 2.18 1.97 2.98 2.26 3.08-.11.4-.74 2.59-2.6 4.09"/>
            </svg>
            Apple
          </button>
          <button class="btn-social" @click="handleSocial('facebook')">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="#1877F2">
              <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
            </svg>
            Facebook
          </button>
        </div>

        <div class="guest-link">
          <button type="button" class="btn-guest" @click="handleGuest">
            View as guest →
          </button>
        </div>
      </div>
    </div>

    <!-- Toast -->
    <transition name="toast">
      <div v-if="toast.visible" class="toast" :class="toast.type">
        {{ toast.message }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeTab = ref('login')
const email = ref('')
const password = ref('')
const name = ref('')
const rememberMe = ref(false)
const showPassword = ref(false)
const isLoading = ref(false)
const errors = reactive({ email: '', password: '' })
const toast = reactive({ visible: false, message: '', type: 'success' })

function showToast(message, type = 'success') {
  toast.message = message; toast.type = type; toast.visible = true
  setTimeout(() => { toast.visible = false }, 3000)
}

function validate() {
  errors.email = ''; errors.password = ''; let valid = true
  if (!email.value || !/\S+@\S+\.\S+/.test(email.value)) { errors.email = 'Please enter a valid email.'; valid = false }
  if (!password.value || password.value.length < 6) { errors.password = 'Password must be at least 6 characters.'; valid = false }
  return valid
}

async function handleSubmit() {
  if (!validate()) return
  isLoading.value = true
  await new Promise(r => setTimeout(r, 1200))
  isLoading.value = false
  router.push('/home')
}

function handleSocial(provider) {
  showToast(`Continuing with ${provider.charAt(0).toUpperCase() + provider.slice(1)}...`, 'info')
  setTimeout(() => router.push('/home'), 800)
}

function handleForgotPassword() { showToast('Password reset link sent to your email.', 'info') }
function handleGuest() { router.push('/home') }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.login-page {
  display: flex;
  height: 100vh;
  width: 100%;
  font-family: 'DM Sans', sans-serif;
  background: #fff;
  overflow: hidden;
}

/* ── LEFT HERO ── */
.hero-panel {
  position: relative;
  width: 46%;
  flex-shrink: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.hero-image {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover; object-position: center;
}

.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(160deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.0) 35%, rgba(0,0,0,0.6) 75%, rgba(0,0,0,0.82) 100%);
  z-index: 1;
}

.logo {
  position: absolute; top: 24px; left: 24px; z-index: 2;
  display: flex; align-items: center; gap: 10px; color: #fff;
}

.logo-icon {
  width: 36px; height: 36px;
  background: rgba(255,255,255,0.95);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  color: #c0784a;
  box-shadow: 0 2px 12px rgba(0,0,0,0.15);
}

.logo-text { font-weight: 600; font-size: 0.95rem; letter-spacing: 0.01em; }

.hero-content {
  position: absolute; bottom: 100px; left: 32px; right: 32px; z-index: 2; color: #fff;
}

.hero-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 400; line-height: 1.1;
  margin-bottom: 14px;
}

.hero-subtitle {
  font-size: 0.9rem; font-weight: 400; line-height: 1.7;
  color: rgba(255,255,255,0.8); margin-bottom: 24px;
}

.hero-dots { display: flex; gap: 5px; }
.dot { width: 24px; height: 3px; border-radius: 3px; background: rgba(255,255,255,0.35); transition: all 0.3s; }
.dot.active { background: #fff; width: 40px; }

/* Stats bar */
.hero-stats {
  position: absolute; bottom: 0; left: 0; right: 0; z-index: 2;
  display: flex; align-items: center; justify-content: space-around;
  padding: 18px 32px;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(12px);
  border-top: 1px solid rgba(255,255,255,0.15);
}

.stat { display: flex; flex-direction: column; align-items: center; gap: 2px; color: #fff; }
.stat-value { font-size: 1.1rem; font-weight: 600; letter-spacing: 0.01em; }
.stat-label { font-size: 0.7rem; color: rgba(255,255,255,0.7); font-weight: 400; }
.stat-divider { width: 1px; height: 28px; background: rgba(255,255,255,0.2); }

/* ── RIGHT FORM ── */
.mobile-logo {
  display: none;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
  justify-content: center;
  color: #111;
}

.form-panel {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  overflow-y: auto;
  background: #fafafa;
}

.form-inner {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Tabs */
.auth-tabs {
  display: flex;
  background: #f0f0f0;
  border-radius: 12px;
  padding: 3px;
  margin-bottom: 28px;
}

.tab-btn {
  flex: 1;
  padding: 9px 0;
  border: none;
  border-radius: 10px;
  background: transparent;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem;
  font-weight: 500;
  color: #888;
  cursor: pointer;
  transition: all 0.22s;
}

.tab-btn.active {
  background: #fff;
  color: #111;
  box-shadow: 0 1px 6px rgba(0,0,0,0.1);
}

/* Header */
.form-header { margin-bottom: 22px; }

.form-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(1.6rem, 2.5vw, 2.1rem);
  font-weight: 400;
  color: #111;
  margin-bottom: 5px;
  line-height: 1.15;
}

.form-subtitle { font-size: 0.8rem; color: #999; line-height: 1.5; }

/* Form */
.auth-form { display: flex; flex-direction: column; gap: 14px; margin-bottom: 16px; }

.field-group { display: flex; flex-direction: column; gap: 5px; }

.field-label-row { display: flex; justify-content: space-between; align-items: center; }

.field-label { font-size: 0.78rem; font-weight: 600; color: #444; letter-spacing: 0.01em; }

.forgot-link {
  font-size: 0.73rem; color: #c0784a; background: none; border: none;
  cursor: pointer; font-family: 'DM Sans', sans-serif; transition: color 0.2s;
  font-weight: 500;
}
.forgot-link:hover { color: #a0622a; }

.input-wrapper {
  position: relative; display: flex; align-items: center;
}

.input-icon {
  position: absolute; left: 13px; color: #bbb; flex-shrink: 0; pointer-events: none;
}

.field-input {
  width: 100%;
  padding: 11px 13px 11px 38px;
  border: 1.5px solid #e8e8e8;
  border-radius: 11px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem;
  color: #111;
  background: #fff;
  transition: border-color 0.2s, box-shadow 0.2s;
  outline: none;
}
.field-input::placeholder { color: #ccc; }
.field-input:focus { border-color: #c0784a; box-shadow: 0 0 0 3px rgba(192,120,74,0.1); }
.field-input.error { border-color: #e55; }

.password-wrapper .field-input { padding-right: 42px; }

.toggle-pw {
  position: absolute; right: 12px;
  background: none; border: none; cursor: pointer;
  color: #bbb; display: flex; align-items: center; transition: color 0.2s;
}
.toggle-pw:hover { color: #555; }

.field-error { font-size: 0.69rem; color: #e55; }

/* Remember me */
.remember-row { display: flex; align-items: center; }
.check-label { display: flex; align-items: center; gap: 8px; cursor: pointer; user-select: none; }
.check-input { display: none; }
.check-box {
  width: 16px; height: 16px; border-radius: 4px;
  border: 1.5px solid #ddd; background: #fff;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s; flex-shrink: 0;
}
.check-input:checked + .check-box {
  background: #111; border-color: #111;
}
.check-input:checked + .check-box::after {
  content: '✓'; font-size: 10px; color: #fff; line-height: 1;
}
.check-text { font-size: 0.78rem; color: #666; }

/* Primary button */
.btn-primary {
  width: 100%;
  padding: 13px;
  background: #111;
  color: #fff;
  border: none;
  border-radius: 11px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  letter-spacing: 0.02em;
}
.btn-primary:hover:not(:disabled) { background: #2a2a2a; }
.btn-primary:active:not(:disabled) { transform: scale(0.99); }
.btn-primary:disabled { opacity: 0.6; cursor: not-allowed; }

.spinner {
  width: 16px; height: 16px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: #fff; border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* Divider */
.divider {
  display: flex; align-items: center; gap: 10px; margin: 16px 0;
}
.divider-line { flex: 1; height: 1px; background: #ececec; }
.divider-text { font-size: 0.72rem; color: #bbb; font-weight: 500; white-space: nowrap; }

/* Social — horizontal row */
.social-buttons { display: flex; gap: 8px; margin-bottom: 16px; }

.btn-social {
  flex: 1;
  padding: 10px 6px;
  background: #fff;
  border: 1.5px solid #e8e8e8;
  border-radius: 11px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  color: #333;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 6px;
  transition: border-color 0.2s, background 0.2s;
}
.btn-social:hover { border-color: #bbb; background: #f6f6f6; }

/* Guest */
.guest-link { text-align: center; }
.btn-guest {
  background: none; border: none;
  font-family: 'DM Sans', sans-serif; font-size: 0.78rem;
  color: #bbb; cursor: pointer; transition: color 0.2s;
}
.btn-guest:hover { color: #555; }

/* Toast */
.toast {
  position: fixed; bottom: 24px; right: 24px;
  padding: 11px 20px; border-radius: 10px;
  font-size: 0.83rem; font-weight: 500; z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.12);
}
.toast.success { background: #111; color: #fff; }
.toast.info { background: #fff; color: #333; border: 1px solid #e0e0e0; }
.toast-enter-active, .toast-leave-active { transition: all 0.3s ease; }
.toast-enter-from, .toast-leave-to { opacity: 0; transform: translateY(10px); }

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .hero-panel { width: 42%; }
}

@media (max-width: 640px) {
  .login-page { display: flex; flex-direction: column; background: #fafafa; }
  .hero-panel { display: none; }
  .form-panel { padding: 24px 16px; align-items: flex-start; justify-content: center; background: transparent; }
  .form-inner { 
    max-width: 100%; 
    background: #fff; 
    padding: 32px 24px; 
    border-radius: 24px; 
    box-shadow: 0 10px 40px rgba(0,0,0,0.06); 
  }
  .mobile-logo { display: flex; }
  .form-title { font-size: 1.8rem; }
}
</style>