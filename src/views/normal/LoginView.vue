<template>
  <div class="login-page" :class="{ 'forgot-flow': currentFormState !== 'auth' }">
    <!-- Hero Panel (Left by default, Right in forgot-flow) -->
    <div class="hero-panel">
      <div class="hero-overlay" />
      <img
        :src="currentHeroImage"
        alt="Luxury Home"
        class="hero-image"
      />
      
      <!-- Desktop Hero Logo (Visible only in auth state) -->
      <div v-if="currentFormState === 'auth'" class="logo">
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

      <!-- Dynamic Hero Content -->
      <div class="hero-content">
        <h1 class="hero-title">
          <span v-if="currentFormState === 'auth'">Find your<br />sweet home</span>
          <span v-else>Safe and Convenience</span>
        </h1>
        <p class="hero-subtitle">
          <span v-if="currentFormState === 'auth'">
            Welcome to your comfort zone.<br />
            Schedule a visit in just a few clicks.
          </span>
          <span v-else>
            Feel safe and free to choose your most capable roommate.
          </span>
        </p>
        
        <!-- Dynamic Indicators -->
        <div v-if="currentFormState === 'auth'" class="hero-dots">
          <span class="dot active" />
          <span class="dot" />
          <span class="dot" />
        </div>
        <div v-else class="hero-indicator">
          <span class="indicator-line" />
          <span class="indicator-dot" />
        </div>
      </div>

      <!-- Stats bar (Visible only in auth state) -->
      <div v-if="currentFormState === 'auth'" class="hero-stats">
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

    <!-- Form Panel (Right by default, Left in forgot-flow) -->
    <div class="form-panel">
      <!-- Desktop Form Logo (Visible only in forgot password flows) -->
      <div v-if="currentFormState !== 'auth'" class="desktop-logo">
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

        <!-- STATE 1: AUTHENTICATION (Login / Sign Up) -->
        <div v-if="currentFormState === 'auth'">
          <!-- Role Selector -->
          <div class="role-selector">
            <button 
              type="button" 
              class="role-btn" 
              :class="{ active: selectedRole === 'resident' }" 
              @click="selectedRole = 'resident'"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="role-icon-svg">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
              Resident (Guest)
            </button>
            <button 
              type="button" 
              class="role-btn" 
              :class="{ active: selectedRole === 'landlord' }" 
              @click="selectedRole = 'landlord'"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="role-icon-svg">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="9" y1="3" x2="9" y2="21"></line>
                <line x1="15" y1="3" x2="15" y2="21"></line>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="3" y1="15" x2="21" y2="15"></line>
              </svg>
              Landlord
            </button>
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
              {{ selectedRole === 'landlord' ? (activeTab === 'login' ? 'Landlord Portal' : 'Register Landlord') : (activeTab === 'login' ? 'Welcome back!' : 'Create account') }}
            </h2>
            <p class="form-subtitle">
              {{ selectedRole === 'landlord' 
                ? 'Access your landlord dashboard to manage listings & bookings.' 
                : (activeTab === 'login' ? 'Enter your credentials to access your account.' : 'Fill in the details below to get started.') }}
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

            <div v-if="activeTab === 'signup'" class="name-fields-row">
              <div class="field-group">
                <label class="field-label">First name</label>
                <div class="input-wrapper">
                  <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
                  </svg>
                  <input v-model="firstName" type="text" placeholder="John" class="field-input" autocomplete="given-name" />
                </div>
              </div>
              <div class="field-group">
                <label class="field-label">Last name</label>
                <div class="input-wrapper">
                  <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
                  </svg>
                  <input v-model="lastName" type="text" placeholder="Doe" class="field-input" autocomplete="family-name" />
                </div>
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
        </div>

        <!-- STATE 2: RESET PASSWORD -->
        <div v-else-if="currentFormState === 'forgot_password'">
          <!-- Header -->
          <div class="form-header centered">
            <h2 class="form-title">Reset Password</h2>
            <p class="form-subtitle">
              <span v-if="resetMethod === 'email'">Enter your email to reset your password</span>
              <span v-else-if="resetMethod === 'phone'">Enter your phone number to reset your password</span>
              <span v-else>Enter your National ID details to verify your account</span>
            </p>
          </div>

          <!-- Method Selector -->
          <div class="method-selector">
            <button 
              type="button" 
              class="method-btn" 
              :class="{ active: resetMethod === 'email' }" 
              @click="resetMethod = 'email'"
            >
              Email
            </button>
            <button 
              type="button" 
              class="method-btn" 
              :class="{ active: resetMethod === 'phone' }" 
              @click="resetMethod = 'phone'"
            >
              Phone
            </button>
            <button 
              type="button" 
              class="method-btn" 
              :class="{ active: resetMethod === 'id_card' }" 
              @click="resetMethod = 'id_card'"
            >
              ID Card
            </button>
          </div>

          <!-- Form -->
          <form class="auth-form" @submit.prevent="handleGetCode">
            <!-- Email Method -->
            <div v-if="resetMethod === 'email'" class="field-group">
              <label class="field-label">Email address</label>
              <div class="input-wrapper">
                <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>
                </svg>
                <input
                  v-model="resetEmail"
                  type="email"
                  placeholder="Enter your email address"
                  class="field-input"
                  :class="{ error: errors.resetEmail }"
                />
              </div>
              <span v-if="errors.resetEmail" class="field-error">{{ errors.resetEmail }}</span>
            </div>

            <!-- Phone Method -->
            <div v-else-if="resetMethod === 'phone'" class="field-group">
              <label class="field-label">Phone number</label>
              <div class="input-wrapper">
                <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
                <input
                  v-model="resetPhone"
                  type="tel"
                  placeholder="Enter your phone number"
                  class="field-input"
                  :class="{ error: errors.resetPhone }"
                />
              </div>
              <span v-if="errors.resetPhone" class="field-error">{{ errors.resetPhone }}</span>
            </div>

            <!-- ID Card Method -->
            <div v-else class="field-group">
              <label class="field-label">National ID Number</label>
              <div class="input-wrapper">
                <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="16" rx="2" ry="2"/><line x1="7" y1="8" x2="17" y2="8"/><line x1="7" y1="12" x2="13" y2="12"/><line x1="7" y1="16" x2="9" y2="16"/>
                </svg>
                <input
                  v-model="resetIdNumber"
                  type="text"
                  placeholder="Enter your 9 or 12-digit ID"
                  class="field-input"
                  :class="{ error: errors.resetIdNumber }"
                />
              </div>
              <span v-if="errors.resetIdNumber" class="field-error">{{ errors.resetIdNumber }}</span>
              
              <!-- ID Card Upload Scanner -->
              <div class="id-scanner-upload" @click="triggerIdCardUpload">
                <input
                  type="file"
                  ref="idCardInputRef"
                  accept="image/*"
                  class="hidden-input"
                  @change="handleIdCardFileChange"
                />
                
                <div v-if="isScanningIdCard" class="scanner-scanning">
                  <div class="scanner-laser"></div>
                  <span class="scanner-text">Scanning ID card...</span>
                </div>
                <div v-else-if="idCardPreview" class="scanner-preview">
                  <img :src="idCardPreview" alt="ID Preview" class="scanner-img" />
                  <div class="scanner-overlay-success">✓ Scanned</div>
                </div>
                <div v-else class="scanner-placeholder">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2">
                    <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
                    <circle cx="12" cy="13" r="4"/>
                  </svg>
                  <span>Upload ID Card image to scan</span>
                </div>
              </div>
            </div>

            <button type="submit" class="btn-primary" :disabled="isLoading">
              <span v-if="isLoading" class="spinner" />
              <span v-else>{{ resetMethod === 'id_card' ? 'Verify ID' : 'Get Code' }}</span>
            </button>
          </form>

          <div class="back-to-login">
            <button type="button" class="btn-link" @click="currentFormState = 'auth'">
              Back to Log In
            </button>
          </div>
        </div>

        <!-- STATE 3: VERIFY ACCOUNT OTP -->
        <div v-else-if="currentFormState === 'verify_otp'">
          <!-- Header -->
          <div class="form-header centered">
            <h2 class="form-title">Verify Account</h2>
            <p class="form-subtitle">
              Please enter the code we sent to your {{ resetMethod === 'email' ? 'email' : (resetMethod === 'phone' ? 'phone' : 'registered contact') }}
            </p>
          </div>

          <!-- OTP Input Fields -->
          <div class="otp-container">
            <div class="otp-inputs">
              <input
                v-for="(digit, idx) in 6"
                :key="idx"
                v-model="otpDigits[idx]"
                type="text"
                maxlength="1"
                class="otp-input"
                @input="handleOtpInput(idx, $event)"
                @keydown.delete="handleOtpBackspace(idx, $event)"
                autocomplete="off"
                inputmode="numeric"
              />
            </div>
          </div>

          <button type="button" class="btn-primary" @click="handleVerifyOtp" :disabled="isLoading">
            <span v-if="isLoading" class="spinner" />
            <span v-else>Verify</span>
          </button>

          <div class="otp-footer">
            <p class="resend-text">
              Didn't receive your code? 
              <button type="button" class="btn-link-highlight" @click="handleGetCode">Send code again</button>
            </p>
            <button type="button" class="btn-link" @click="currentFormState = 'forgot_password'" style="margin-top: 12px;">
              Change Recovery Option
            </button>
          </div>
        </div>

        <!-- STATE 4: NEW PASSWORD -->
        <div v-else-if="currentFormState === 'new_password'">
          <!-- Header -->
          <div class="form-header centered">
            <h2 class="form-title">New Password</h2>
            <p class="form-subtitle">Please enter your new password below</p>
          </div>

          <!-- Form -->
          <form class="auth-form" @submit.prevent="handleResetPasswordSubmit">
            <!-- New Password -->
            <div class="field-group">
              <label class="field-label">New Password</label>
              <div class="input-wrapper password-wrapper">
                <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>
                </svg>
                <input
                  v-model="newPassword"
                  :type="showNewPassword ? 'text' : 'password'"
                  placeholder="••••••••"
                  class="field-input"
                  :class="{ error: errors.newPassword }"
                  autocomplete="new-password"
                />
                <button type="button" class="toggle-pw" @click="showNewPassword = !showNewPassword">
                  <svg v-if="!showNewPassword" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
                  </svg>
                  <svg v-else width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                  </svg>
                </button>
              </div>
              <span v-if="errors.newPassword" class="field-error">{{ errors.newPassword }}</span>
            </div>

            <!-- Confirm Password -->
            <div class="field-group">
              <label class="field-label">Confirm Password</label>
              <div class="input-wrapper password-wrapper">
                <svg class="input-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>
                </svg>
                <input
                  v-model="confirmPassword"
                  :type="showConfirmPassword ? 'text' : 'password'"
                  placeholder="••••••••"
                  class="field-input"
                  :class="{ error: errors.confirmPassword }"
                  autocomplete="new-password"
                />
                <button type="button" class="toggle-pw" @click="showConfirmPassword = !showConfirmPassword">
                  <svg v-if="!showConfirmPassword" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
                  </svg>
                  <svg v-else width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                  </svg>
                </button>
              </div>
              <span v-if="errors.confirmPassword" class="field-error">{{ errors.confirmPassword }}</span>
            </div>

            <button type="submit" class="btn-primary" :disabled="isLoading">
              <span v-if="isLoading" class="spinner" />
              <span v-else>Reset Password</span>
            </button>
          </form>
        </div>

        <!-- Bottom Guest Link -->
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
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { auth, db } from '../../firebase'
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'
import { doc, setDoc } from 'firebase/firestore'
import heroImage from '@/assets/hero_sunset_deck.png'

const router = useRouter()
const activeTab = ref('login')
const selectedRole = ref('resident') // 'resident' or 'landlord'
const email = ref('')
const password = ref('')
const firstName = ref('')
const lastName = ref('')
const rememberMe = ref(false)
const showPassword = ref(false)
const isLoading = ref(false)

const errors = reactive({ 
  email: '', 
  password: '',
  resetEmail: '',
  resetPhone: '',
  resetIdNumber: '',
  newPassword: '',
  confirmPassword: ''
})

const toast = reactive({ visible: false, message: '', type: 'success' })

// Reset Password Flow States
const currentFormState = ref('auth') // 'auth', 'forgot_password', 'verify_otp', 'new_password'
const resetMethod = ref('email') // 'email', 'phone', or 'id_card'
const resetEmail = ref('')
const resetPhone = ref('')
const resetIdNumber = ref('')
const otpDigits = ref(['', '', '', '', '', ''])
const generatedCode = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)

// ID Card scanning logic refs
const idCardInputRef = ref(null)
const idCardFile = ref(null)
const idCardPreview = ref(null)
const isScanningIdCard = ref(false)

// Computed hero panel image based on current form state
const currentHeroImage = computed(() => {
  return currentFormState.value === 'auth'
    ? 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80'
    : heroImage
})

function showToast(message, type = 'success') {
  toast.message = message; toast.type = type; toast.visible = true
  setTimeout(() => { toast.visible = false }, 3500)
}

function triggerIdCardUpload() {
  if (idCardInputRef.value) {
    idCardInputRef.value.click()
  }
}

function handleIdCardFileChange(e) {
  const file = e.target.files[0]
  if (file) {
    idCardFile.value = file
    idCardPreview.value = URL.createObjectURL(file)
    isScanningIdCard.value = true
    showToast('Scanning ID Card...', 'info')
    
    setTimeout(() => {
      isScanningIdCard.value = false
      resetIdNumber.value = '982104753'
      showToast('ID Card scanned successfully! ID Number: 982104753', 'success')
    }, 2000)
  }
}

function validate() {
  errors.email = ''; errors.password = ''; let valid = true
  if (!email.value || !/\S+@\S+\.\S+/.test(email.value)) { errors.email = 'Please enter a valid email.'; valid = false }
  if (!password.value || password.value.length < 6) { errors.password = 'Password must be at least 6 characters.'; valid = false }
  if (activeTab.value === 'signup' && (!firstName.value.trim() || !lastName.value.trim())) { 
    showToast('Please enter your first and last name.', 'error'); 
    valid = false;
  }
  return valid
}

async function handleSubmit() {
  if (!validate()) return
  isLoading.value = true
  
  try {
    if (activeTab.value === 'signup') {
      // 1. Create User in Firebase Auth
      const userCredential = await createUserWithEmailAndPassword(auth, email.value, password.value)
      const user = userCredential.user
      
      // 2. Save full name and role to Firestore database
      await setDoc(doc(db, "users", user.uid), {
        firstName: firstName.value.trim(),
        lastName: lastName.value.trim(),
        email: email.value,
        role: selectedRole.value,
        createdAt: new Date().toISOString()
      })
      
      showToast('Account created successfully!', 'success')
      if (selectedRole.value === 'landlord') {
        router.push('/landlord')
      } else {
        router.push('/setup-account')
      }
    } else {
      // Login User
      await signInWithEmailAndPassword(auth, email.value, password.value)
      showToast('Welcome back!', 'success')
      if (selectedRole.value === 'landlord') {
        router.push('/landlord')
      } else {
        router.push('/home')
      }
    }
  } catch (error) {
    console.error("Auth Error:", error)
    if (error.code === 'auth/email-already-in-use') {
      showToast('This email is already registered. Please log in.', 'error')
    } else if (error.code === 'auth/invalid-credential' || error.code === 'auth/wrong-password') {
      showToast('Invalid email or password.', 'error')
    } else {
      showToast(error.message, 'error')
    }
  } finally {
    isLoading.value = false
  }
}

async function handleSocial(provider) {
  if (provider === 'google') {
    const googleProvider = new GoogleAuthProvider()
    try {
      const result = await signInWithPopup(auth, googleProvider)
      const user = result.user
      
      // Split user.displayName into firstName and lastName, and fetch profile picture (photoURL)
      const displayName = user.displayName || ''
      const nameParts = displayName.trim().split(/\s+/)
      const firstNameVal = nameParts[0] || 'Google'
      const lastNameVal = nameParts.slice(1).join(' ') || 'User'
      
      // Save or update user profile in Firestore
      await setDoc(doc(db, "users", user.uid), {
        firstName: firstNameVal,
        lastName: lastNameVal,
        name: displayName || 'Google User',
        email: user.email,
        avatar: user.photoURL || '',
        role: selectedRole.value,
        lastLogin: new Date().toISOString()
      }, { merge: true }) // merge: true ensures we don't overwrite existing data
      
      showToast('Google Sign-In successful!', 'success')
      if (selectedRole.value === 'landlord') {
        router.push('/landlord')
      } else {
        router.push('/home')
      }
    } catch (error) {
      console.error("Google Auth Error:", error)
      if (error.code !== 'auth/popup-closed-by-user') {
        showToast(error.message, 'error')
      }
    }
  } else {
    showToast(`${provider.charAt(0).toUpperCase() + provider.slice(1)} login coming soon!`, 'info')
  }
}

function handleForgotPassword() {
  currentFormState.value = 'forgot_password'
  resetEmail.value = ''
  resetPhone.value = ''
  resetIdNumber.value = ''
  idCardFile.value = null
  idCardPreview.value = null
  errors.resetEmail = ''
  errors.resetPhone = ''
  errors.resetIdNumber = ''
}

async function handleGetCode() {
  errors.resetEmail = ''
  errors.resetPhone = ''
  errors.resetIdNumber = ''
  
  if (resetMethod.value === 'email') {
    if (!resetEmail.value || !/\S+@\S+\.\S+/.test(resetEmail.value)) {
      errors.resetEmail = 'Please enter a valid email address.'
      return
    }
  } else if (resetMethod.value === 'phone') {
    const phoneRegex = /^\+?[0-9\s\-()]{8,15}$/
    if (!resetPhone.value || !phoneRegex.test(resetPhone.value)) {
      errors.resetPhone = 'Please enter a valid phone number.'
      return
    }
  } else {
    const idRegex = /^[0-9]{9,12}$/
    if (!resetIdNumber.value || !idRegex.test(resetIdNumber.value)) {
      errors.resetIdNumber = 'Please enter a valid 9 or 12-digit ID.'
      return
    }
  }
  
  isLoading.value = true
  
  setTimeout(() => {
    // Generate random 6-digit verification code
    const code = Math.floor(100000 + Math.random() * 900000).toString()
    generatedCode.value = code
    
    // Clear OTP digit array
    otpDigits.value = ['', '', '', '', '', '']
    isLoading.value = false
    currentFormState.value = 'verify_otp'
    
    // Show verification code toast
    showToast(`HomeSweet Code: ${code}`, 'success')
    console.log(`[HomeSweet Password Reset] OTP Verification Code: ${code}`)
  }, 1000)
}

function handleVerifyOtp() {
  const enteredCode = otpDigits.value.join('')
  if (enteredCode.length < 6) {
    showToast('Please enter the full 6-digit code.', 'error')
    return
  }
  
  if (enteredCode !== generatedCode.value) {
    showToast('Invalid verification code.', 'error')
    return
  }
  
  showToast('Code verified successfully!', 'success')
  currentFormState.value = 'new_password'
  newPassword.value = ''
  confirmPassword.value = ''
  errors.newPassword = ''
  errors.confirmPassword = ''
}

async function handleResetPasswordSubmit() {
  errors.newPassword = ''
  errors.confirmPassword = ''
  
  if (!newPassword.value || newPassword.value.length < 6) {
    errors.newPassword = 'Password must be at least 6 characters.'
    return
  }
  
  if (newPassword.value !== confirmPassword.value) {
    errors.confirmPassword = 'Passwords do not match.'
    return
  }
  
  isLoading.value = true
  
  setTimeout(() => {
    isLoading.value = false
    showToast('Password reset successfully! Please log in.', 'success')
    currentFormState.value = 'auth'
    activeTab.value = 'login'
    
    // Pre-fill email/username if reset by email
    if (resetMethod.value === 'email') {
      email.value = resetEmail.value
    }
    password.value = ''
  }, 1500)
}

function handleOtpInput(index, event) {
  const val = event.target.value
  otpDigits.value[index] = val.replace(/[^0-9]/g, '')
  
  // Auto-focus next box if digit entered
  if (otpDigits.value[index] && index < 5) {
    const nextInput = event.target.nextElementSibling
    if (nextInput) {
      nextInput.focus()
    }
  }
}

function handleOtpBackspace(index, event) {
  // If current box is empty, move focus to previous box
  if (!otpDigits.value[index] && index > 0) {
    const prevInput = event.target.previousElementSibling
    if (prevInput) {
      prevInput.focus()
    }
  }
}

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

/* Dynamic reverse direction when resetting password */
.login-page.forgot-flow {
  flex-direction: row-reverse;
}

/* ── HERO PANEL (LEFT BY DEFAULT) ── */
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
  transition: all 0.3s ease-in-out;
}

.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(160deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.0) 35%, rgba(0,0,0,0.5) 70%, rgba(0,0,0,0.8) 100%);
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
  color: #5C4E4E;
  box-shadow: 0 2px 12px rgba(0,0,0,0.15);
}

.logo-text { font-weight: 600; font-size: 0.95rem; letter-spacing: 0.01em; }

.hero-content {
  position: absolute; bottom: 100px; left: 32px; right: 32px; z-index: 2; color: #fff;
}

.login-page.forgot-flow .hero-content {
  bottom: 80px; left: 40px; right: 40px;
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

.login-page.forgot-flow .hero-subtitle {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.85);
}

.hero-dots { display: flex; gap: 5px; }
.dot { width: 24px; height: 3px; border-radius: 3px; background: rgba(255,255,255,0.35); transition: all 0.3s; }
.dot.active { background: #fff; width: 40px; }

/* Indicator bar (only on forgot password hero) */
.hero-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;
}

.indicator-line {
  width: 80px;
  height: 4px;
  background: #fff;
  border-radius: 4px;
}

.indicator-dot {
  width: 4px;
  height: 4px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
}

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

/* ── FORM PANEL (RIGHT BY DEFAULT) ── */
.form-panel {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  overflow-y: auto;
  background: #e0e0e0;
  position: relative;
}

.desktop-logo {
  position: absolute;
  top: 24px;
  left: 32px;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 10px;
  color: #5C4E4E;
}

.desktop-logo .logo-icon {
  width: 36px;
  height: 36px;
  background: #ffffff;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #5C4E4E;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
  border: 1px solid #eee;
}

.desktop-logo .logo-text {
  font-weight: 600;
  font-size: 0.95rem;
  letter-spacing: 0.01em;
  color: #5C4E4E;
}

.form-inner {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.mobile-logo {
  display: none;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
  justify-content: center;
  color: #5C4E4E;
}

/* ── AUTHENTICATION TABS & STATE FORMS ── */
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
  color: #5C4E4E;
  box-shadow: 0 1px 6px rgba(0,0,0,0.1);
}

/* Method Selector */
.method-selector {
  display: flex;
  background: #f0f0f0;
  border-radius: 12px;
  padding: 3px;
  margin-bottom: 22px;
}

.method-btn {
  flex: 1;
  padding: 10px 0;
  border: none;
  border-radius: 10px;
  background: transparent;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 600;
  color: #777;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.22s ease;
}

.method-btn:hover {
  color: #333;
}

.method-btn.active {
  background: #ffffff;
  color: #5C4E4E;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

/* Header */
.form-header { margin-bottom: 22px; }
.form-header.centered { text-align: center; }

.form-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(1.8rem, 2.5vw, 2.3rem);
  font-weight: 400;
  color: #5C4E4E;
  margin-bottom: 5px;
  line-height: 1.15;
}

.form-subtitle { font-size: 0.82rem; color: #888; line-height: 1.5; }

/* Forms */
.auth-form { display: flex; flex-direction: column; gap: 14px; margin-bottom: 16px; }

.name-fields-row { display: flex; gap: 12px; width: 100%; }
.name-fields-row .field-group { flex: 1; }

.field-group { display: flex; flex-direction: column; gap: 5px; }

.field-label-row { display: flex; justify-content: space-between; align-items: center; }

.field-label { font-size: 0.78rem; font-weight: 600; color: #444; letter-spacing: 0.01em; }

.forgot-link {
  font-size: 0.73rem; color: #5C4E4E; background: none; border: none;
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
  border: 1.5px solid #d1d5db;
  border-radius: 11px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem;
  color: #5C4E4E;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: border-color 0.3s, box-shadow 0.3s, transform 0.2s;
  outline: none;
}
.field-input:hover {
  border-color: #bbb;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
.field-input::placeholder { color: #aaa; }
.field-input:focus { border-color: #5C4E4E; box-shadow: 0 0 0 3px rgba(92,78,78,0.15); transform: translateY(-1px); }
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
  background: #5C4E4E; border-color: #5C4E4E;
}
.check-input:checked + .check-box::after {
  content: '✓'; font-size: 10px; color: #fff; line-height: 1;
}
.check-text { font-size: 0.78rem; color: #666; }

/* Primary button */
.btn-primary {
  width: 100%;
  padding: 13px;
  background: #5C4E4E;
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
.guest-link { 
  position: absolute; 
  bottom: 24px; 
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
}

.btn-guest {
  background: none; border: none;
  font-family: 'DM Sans', sans-serif; font-size: 0.78rem;
  color: #bbb; cursor: pointer; transition: color 0.2s;
}
.btn-guest:hover { color: #555; }

/* Back to Log In & OTP Footer Links */
.back-to-login, .otp-footer {
  text-align: center;
  margin-top: 16px;
  margin-bottom: 16px;
}

.btn-link {
  background: none;
  border: none;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.78rem;
  font-weight: 500;
  color: #5C4E4E;
  cursor: pointer;
  transition: color 0.2s;
}

.btn-link:hover {
  color: #a0622a;
}

.resend-text {
  font-size: 0.8rem;
  color: #666;
}

.btn-link-highlight {
  background: none;
  border: none;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 600;
  color: #4285F4;
  cursor: pointer;
  transition: opacity 0.2s;
  padding: 0;
  margin-left: 4px;
}

.btn-link-highlight:hover {
  text-decoration: underline;
}

/* OTP Digits styling */
.otp-container {
  display: flex;
  justify-content: center;
  margin-bottom: 22px;
  margin-top: 10px;
}

.otp-inputs {
  display: flex;
  gap: 10px;
}

.otp-input {
  width: 48px;
  height: 48px;
  border: 1.5px solid #e8e8e8;
  border-radius: 10px;
  text-align: center;
  font-size: 1.25rem;
  font-weight: 600;
  color: #5C4E4E;
  background: #fff;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.otp-input:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92,78,78,0.1);
}

/* ID Card scanner styling */
.hidden-input {
  display: none;
}

.id-scanner-upload {
  width: 100%;
  height: 100px;
  border: 1.5px dashed #ccc;
  border-radius: 11px;
  margin-top: 10px;
  cursor: pointer;
  background: #fdfdfd;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
  transition: border-color 0.2s, background 0.2s;
}

.id-scanner-upload:hover {
  border-color: #5C4E4E;
  background: #fcf8f5;
}

.scanner-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  color: #888;
  font-size: 0.75rem;
  font-weight: 500;
}

.scanner-preview {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
}

.scanner-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.scanner-overlay-success {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: #2e7d32;
  color: #fff;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
}

.scanner-scanning {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.05);
}

.scanner-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: #5C4E4E;
  z-index: 2;
  animation: pulse 1.5s infinite;
}

.scanner-laser {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #e53935;
  box-shadow: 0 0 8px #e53935;
  animation: scan 2s infinite linear;
}

@keyframes scan {
  0% { top: 0%; }
  50% { top: 100%; }
  100% { top: 0%; }
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

/* Toast */
.toast {
  position: fixed; bottom: 24px; right: 24px;
  padding: 11px 20px; border-radius: 10px;
  font-size: 0.83rem; font-weight: 500; z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.12);
}
.toast.success { background: #5C4E4E; color: #fff; }
.toast.info { background: #fff; color: #333; border: 1px solid #e0e0e0; }
.toast.error { background: #e55; color: #fff; }
.toast-enter-active, .toast-leave-active { transition: all 0.3s ease; }
.toast-enter-from, .toast-leave-to { opacity: 0; transform: translateY(10px); }

/* Role Selector */
.role-selector {
  display: flex;
  background: #f0f0f0;
  border-radius: 12px;
  padding: 3px;
  margin-bottom: 14px;
}

.role-btn {
  flex: 1;
  padding: 10px 0;
  border: none;
  border-radius: 10px;
  background: transparent;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 600;
  color: #777;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.22s ease;
}

.role-btn:hover {
  color: #333;
}

.role-btn.active {
  background: #ffffff;
  color: #5C4E4E;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.role-icon-svg {
  flex-shrink: 0;
  color: inherit;
}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .hero-panel { width: 42%; }
}

@media (max-width: 640px) {
  .login-page { display: flex; flex-direction: column; background: #fafafa; }
  .login-page.forgot-flow { flex-direction: column; }
  .hero-panel { display: none; }
  .desktop-logo { display: none; }
  .form-panel { padding: 24px 16px; align-items: flex-start; justify-content: center; background: transparent; }
  .form-inner { 
    max-width: 100%; 
    background: #e0e0e0; 
    padding: 32px 24px; 
    border-radius: 24px; 
    box-shadow: 0 10px 40px rgba(0,0,0,0.06); 
  }
  .mobile-logo { display: flex; }
  .form-title { font-size: 1.8rem; }
  
  .guest-link {
    position: static;
    transform: none;
    margin-top: 24px;
  }
}
</style>