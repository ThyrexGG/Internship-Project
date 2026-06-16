<template>
  <div class="landlord-profile-page">
    <!-- Top Nav -->
    <header class="top-nav">
      <div class="logo" @click="goBack">
        <div class="logo-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 18 L16 18" />
            <path d="M4 18 L4 12 L9 7 L16 14" />
            <path d="M12 18 L12 4 L16 4 L16 18 Z" />
            <path d="M12 14 L16 14" />
          </svg>
        </div>
        <span class="logo-text">HomeSweet</span>
      </div>
      <div class="nav-right">
        <div class="profile-menu">
          <div class="avatar">
            <img :src="currentUserAvatar || defaultAvatar" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="User profile" />
          </div>
        </div>
      </div>
    </header>

    <!-- Profile Hero Section -->
    <section class="profile-hero">
      <!-- Glassmorphic Back Button -->
      <button class="back-btn" @click="goBack" aria-label="Go back">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        <span>Back</span>
      </button>

      <div class="banner-wrapper">
        <div class="banner-overlay"></div>
        <img src="https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1600&q=80" alt="Landlord Banner" class="banner-img" />
      </div>

      <div class="profile-meta-container">
        <div class="profile-meta-content">
          <div class="landlord-avatar-wrapper">
            <img :src="landlordInfo.avatar" alt="Landlord Avatar" class="landlord-avatar" />
          </div>
          
          <div class="landlord-summary">
            <div class="landlord-name-row">
              <h1 class="landlord-name">{{ landlordInfo.firstName }} {{ landlordInfo.lastName }}</h1>
              <span class="verified-badge" title="Verified Landlord">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="#4ade80" stroke="#fff" stroke-width="2">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                  <polyline points="22 4 12 14.01 9 11.01" />
                </svg>
              </span>
            </div>
            <p class="landlord-tagline">{{ landlordInfo.tagline }}</p>
          </div>
        </div>

        <button class="message-btn" @click="messageLandlord">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
          Message
        </button>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <section class="profile-tabs-section">
      <div class="tabs-wrapper">
        <div class="tab-buttons">
          <button 
            class="tab-btn" 
            :class="{ active: activeTab === 'info' }" 
            @click="activeTab = 'info'"
          >
            Landlord Info
          </button>
          <button 
            class="tab-btn" 
            :class="{ active: activeTab === 'verification' }" 
            @click="activeTab = 'verification'"
          >
            Verification
          </button>
          <button 
            class="tab-btn" 
            :class="{ active: activeTab === 'reviews' }" 
            @click="activeTab = 'reviews'"
          >
            Review
          </button>
        </div>

        <div class="tab-actions">
          <button class="tab-action-icon-btn" @click="shareProfile" aria-label="Share profile">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="18" cy="5" r="3" />
              <circle cx="6" cy="12" r="3" />
              <circle cx="18" cy="19" r="3" />
              <line x1="8.59" y1="13.51" x2="15.42" y2="17.49" />
              <line x1="15.41" y1="6.51" x2="8.59" y2="10.49" />
            </svg>
          </button>
          <button class="tab-action-icon-btn" aria-label="More actions">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="5" r="1" />
              <circle cx="12" cy="12" r="1" />
              <circle cx="12" cy="19" r="1" />
            </svg>
          </button>
        </div>
      </div>
    </section>

    <!-- Main Content Area -->
    <main class="profile-content">
      <!-- TAB 1: LANDLORD INFO -->
      <div v-if="activeTab === 'info'" class="tab-pane info-pane">
        <!-- Details List -->
        <div class="info-list-container">
          <div class="info-row" v-for="item in landlordDetails" :key="item.label">
            <span class="info-label">{{ item.label }} :</span>
            <span class="info-value">{{ item.value }}</span>
          </div>
        </div>

        <!-- Properties Grid -->
        <div class="properties-container">
          <h2 class="section-title">Properties</h2>
          <div class="properties-grid">
            <div 
              v-for="prop in landlordProperties" 
              :key="prop.id" 
              class="landlord-prop-card"
              @click="$router.push(`/property/${prop.id}`)"
            >
              <div class="prop-img-wrapper">
                <img :src="prop.images[0]" :alt="prop.name" class="prop-img" />
                <div class="prop-gradient-overlay"></div>
                <span class="prop-overlay-name">{{ prop.name }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: VERIFICATION -->
      <div v-else-if="activeTab === 'verification'" class="tab-pane verification-pane">
        <div class="verification-card" v-for="ver in verificationList" :key="ver.title">
          <div class="ver-icon-wrapper" :class="{ verified: ver.status === 'Verified' }">
            <svg v-if="ver.status === 'Verified'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" />
            </svg>
          </div>
          <div class="ver-copy">
            <h3>{{ ver.title }}</h3>
            <p>{{ ver.description }}</p>
          </div>
          <span class="ver-status-label" :class="{ verified: ver.status === 'Verified' }">{{ ver.status }}</span>
        </div>
      </div>

      <!-- TAB 3: REVIEWS -->
      <div v-else-if="activeTab === 'reviews'" class="tab-pane reviews-pane">
        <div class="reviews-summary-card">
          <div class="overall-rating">
            <span class="rating-num">4.9</span>
            <div class="rating-stars">
              <svg v-for="s in 5" :key="s" width="16" height="16" viewBox="0 0 24 24" fill="#f59e0b" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <span class="rating-count">Based on 142 reviews</span>
          </div>

          <div class="rating-breakdown">
            <div class="rating-bar-row" v-for="stars in [5, 4, 3, 2, 1]" :key="stars">
              <span class="star-label">{{ stars }} ★</span>
              <div class="rating-bar-bg">
                <div class="rating-bar-fill" :style="{ width: getRatingPercent(stars) + '%' }"></div>
              </div>
              <span class="star-percent">{{ getRatingPercent(stars) }}%</span>
            </div>
          </div>
        </div>

        <div class="reviews-list">
          <div class="tenant-review-card" v-for="(rev, idx) in tenantReviews" :key="idx">
            <div class="review-header">
              <img :src="rev.avatar" :alt="rev.name" class="reviewer-img" />
              <div class="reviewer-meta">
                <h4>{{ rev.name }}</h4>
                <span class="review-date">{{ rev.date }}</span>
              </div>
              <div class="reviewer-stars">
                <svg v-for="s in rev.rating" :key="s" width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              </div>
            </div>
            <p class="review-text">{{ rev.text }}</p>
          </div>
        </div>
      </div>
    </main>

    <!-- Direct Messaging Popup Modal -->
    <transition name="modal-fade">
      <div v-if="showChatModal" class="chat-modal-overlay" @click.self="showChatModal = false">
        <div class="chat-modal-box">
          <header class="chat-modal-header">
            <div class="chat-modal-title-row">
              <div class="chat-avatar-wrapper">
                <img :src="landlordInfo.avatar" alt="Landlord Avatar" class="chat-avatar-img" />
              </div>
              <div class="chat-landlord-info">
                <h3>{{ landlordInfo.firstName }} {{ landlordInfo.lastName }}</h3>
                <span class="chat-verified-badge">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="#4ade80" stroke="#fff" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                  <span>Verified Landlord</span>
                </span>
              </div>
            </div>
            <button class="chat-close-btn" @click="showChatModal = false" aria-label="Close message window">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </header>

          <div class="chat-modal-body">
            <label class="chat-label">Type your message to landlord:</label>
            <textarea 
              v-model="chatMessage" 
              class="chat-textarea" 
              placeholder="Write your message here..."
              rows="5"
              :disabled="isSendingMessage"
            ></textarea>
            <p class="chat-hint">This landlord usually replies within an hour.</p>
          </div>

          <footer class="chat-modal-footer">
            <button class="chat-cancel-btn" @click="showChatModal = false" :disabled="isSendingMessage">Cancel</button>
            <button class="chat-send-btn" @click="sendDirectMessage" :disabled="isSendingMessage || !chatMessage.trim()">
              <span v-if="isSendingMessage" class="chat-spinner"></span>
              <span v-else>Send Message</span>
            </button>
          </footer>
        </div>
      </div>
    </transition>

    <!-- Success Toast -->
    <transition name="toast-fade">
      <div v-if="showSuccessToast" class="chat-success-toast">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="toast-check-icon">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <span>Message sent successfully to {{ landlordInfo.firstName }}!</span>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { auth, db } from '../../firebase'
import { doc, getDoc } from 'firebase/firestore'
import { onAuthStateChanged } from 'firebase/auth'
import { properties } from '../../store'

const route = useRoute()
const router = useRouter()
const activeTab = ref('info')

const defaultAvatar = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23dfa37b'/><stop offset='100%' stop-color='%23c0784a'/></linearGradient></defs><circle cx='50' cy='50' r='50' fill='url(%23g)'/><circle cx='50' cy='37' r='17' fill='%23fff'/><path d='M50 58c-18 0-32 9-32 20v4h64v-4c0-11-14-20-32-20z' fill='%23fff'/></svg>"

function setDefaultAvatar(event) {
  event.target.src = defaultAvatar
}

const currentUserAvatar = ref('https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80')

// Load current user avatar if logged in
onMounted(() => {
  onAuthStateChanged(auth, async (user) => {
    if (user) {
      try {
        const userDoc = await getDoc(doc(db, 'users', user.uid))
        if (userDoc.exists() && userDoc.data().avatar) {
          currentUserAvatar.value = userDoc.data().avatar
        }
      } catch (err) {
        console.error('Error fetching user avatar:', err)
      }
    }
  })
})

// Landlord general info mocked as per the screen mockup design
const landlordInfo = ref({
  firstName: 'Sangonomiya',
  lastName: 'Kokomi',
  avatar: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=200&q=80', // Cat image matching mockup profile
  tagline: 'Safe, Secure and Affordable',
  phone: '+855 123 456 78',
  email: 'skmi23@gmail.com',
  address: 'Phnom Penh/Cambodia',
  dob: '22 SEP 2029',
  contactHour: '7:00 - 9:00',
  propertyOwned: 4,
  totalTenants: 350,
  joinedDate: '10 OCT 2027',
  experience: '10'
})

// Map landlord general info to list display
const landlordDetails = computed(() => [
  { label: 'First Name', value: landlordInfo.value.firstName },
  { label: 'Last Name', value: landlordInfo.value.lastName },
  { label: 'Phone Number', value: landlordInfo.value.phone },
  { label: 'Email', value: landlordInfo.value.email },
  { label: 'Address', value: landlordInfo.value.address },
  { label: 'Birthday', value: landlordInfo.value.dob },
  { label: 'Contact Hour', value: landlordInfo.value.contactHour },
  { label: 'Property Owned', value: landlordInfo.value.propertyOwned },
  { label: 'Total Tenants', value: landlordInfo.value.totalTenants },
  { label: 'Joined Date', value: landlordInfo.value.joinedDate },
  { label: 'Years of Experience', value: landlordInfo.value.experience }
])

// Get properties owned by the landlord from store
// Filtered to represent 5 mock properties in Phnom Penh
const landlordProperties = computed(() => {
  return properties.value.slice(0, 5).map((p, idx) => ({
    ...p,
    name: idx === 0 ? 'Green Village' : p.name // Match the first few cards to mockup's style
  }))
})

// Verification items list
const verificationList = [
  { title: 'Identity Verified', description: 'National ID card and identity checks successfully validated.', status: 'Verified' },
  { title: 'Property Ownership Verified', description: 'Land registry documentation matches developer registration listings.', status: 'Verified' },
  { title: 'Phone Number Verified', description: 'Validated via active mobile OTP handshake.', status: 'Verified' },
  { title: 'Email Address Verified', description: 'Validated via secure confirmation link.', status: 'Verified' },
  { title: 'Business License', description: 'Corporate leasing certificate and housing permits.', status: 'Under Review' }
]

// Mock reviews matching landlord rating dashboard
const tenantReviews = [
  {
    name: 'Soth Sokhomal',
    avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&q=80',
    date: '3 weeks ago',
    rating: 5,
    text: 'Sangonomiya Kokomi is a wonderful landlord! She is extremely responsive, helpful, and keeps the property in top-tier condition. Highly recommend renting any property owned by her.'
  },
  {
    name: 'Yim Vatey',
    avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80',
    date: '1 month ago',
    rating: 5,
    text: 'Safe environment, excellent service, and responsive. Very happy staying at Green Village Condo!'
  },
  {
    name: 'Muy Leng',
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&q=80',
    date: '2 months ago',
    rating: 4,
    text: 'Management is really polite. Maintenance issues are solved within 24 hours. A peaceful condo experience.'
  }
]

function getRatingPercent(stars) {
  if (stars === 5) return 85
  if (stars === 4) return 10
  if (stars === 3) return 3
  if (stars === 2) return 2
  return 0
}

function goBack() {
  // Try to go back to the previous property detail or fallback to home
  const propId = route.params.id
  const fromQuery = route.query.from ? `?from=${route.query.from}` : ''
  if (propId) {
    router.push(`/property/${propId}${fromQuery}`)
  } else {
    router.push('/home')
  }
}

const showChatModal = ref(false)
const chatMessage = ref('')
const isSendingMessage = ref(false)
const showSuccessToast = ref(false)

function messageLandlord() {
  chatMessage.value = `Hi ${landlordInfo.value.firstName} ${landlordInfo.value.lastName}, I am interested in your property Green Village Condo. Is it still available for rent?`
  showChatModal.value = true
}

function sendDirectMessage() {
  if (!chatMessage.value.trim()) return
  isSendingMessage.value = true
  setTimeout(() => {
    isSendingMessage.value = false
    showChatModal.value = false
    showSuccessToast.value = true
    setTimeout(() => {
      showSuccessToast.value = false
    }, 3000)
  }, 1200)
}

function shareProfile() {
  navigator.clipboard.writeText(window.location.href)
  alert('Profile link copied to clipboard!')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

.landlord-profile-page {
  font-family: 'DM Sans', sans-serif;
  background: #ffffff;
  color: #111111;
  height: 100vh;
  overflow-y: auto;
  padding-bottom: 60px;
}

/* --- Top Nav --- */
.top-nav {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  border-bottom: 1px solid #ebebeb;
  background: #fff;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.logo-icon {
  width: 32px;
  height: 32px;
  background: #111;
  border-radius: 8px;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-text {
  font-size: 1.15rem;
  font-weight: 700;
  color: #111;
}

.profile-menu .avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #ddd;
}

.profile-menu .avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* --- Profile Hero Section --- */
.profile-hero {
  position: relative;
  width: 100%;
  background: #ffffff;
  border-bottom: 1px solid #eaeaea;
}

.back-btn {
  position: absolute;
  top: 24px;
  left: 40px;
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(0, 0, 0, 0.08);
  color: #111;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  z-index: 20;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.back-btn:hover {
  background: #ffffff;
  transform: translateX(-3px);
}

.banner-wrapper {
  width: 100%;
  height: 220px;
  position: relative;
  overflow: hidden;
}

.banner-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.3));
  z-index: 1;
}

.banner-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-meta-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  position: relative;
  margin-top: -60px;
  z-index: 10;
}

.profile-meta-content {
  display: flex;
  align-items: flex-end;
  gap: 24px;
}

.landlord-avatar-wrapper {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 5px solid #ffffff;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  background: #fff;
  flex-shrink: 0;
}

.landlord-avatar-img, .landlord-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.landlord-summary {
  padding-bottom: 8px;
}

.landlord-name-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.landlord-name {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111;
  margin: 0;
}

.verified-badge {
  display: flex;
  align-items: center;
  justify-content: center;
}

.landlord-tagline {
  font-size: 0.95rem;
  color: #666;
  margin: 0;
  font-weight: 500;
}

.message-btn {
  background: #111111;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 24px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background 0.2s ease;
  margin-bottom: 8px;
}

.message-btn:hover {
  background: #2a2a2a;
}

/* --- Navigation Tabs --- */
.profile-tabs-section {
  background: #ffffff;
  border-bottom: 1px solid #eaeaea;
}

.tabs-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tab-buttons {
  display: flex;
  gap: 32px;
}

.tab-btn {
  background: none;
  border: none;
  padding: 16px 0;
  font-size: 0.92rem;
  font-weight: 600;
  color: #666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s ease;
}

.tab-btn:hover {
  color: #111;
}

.tab-btn.active {
  color: #111;
}

.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2.5px;
  background: #111;
  border-radius: 2px;
}

.tab-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.tab-action-icon-btn {
  background: none;
  border: none;
  color: #222;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s ease;
}

.tab-action-icon-btn:hover {
  background: #f5f5f5;
}

/* --- Main Content Area --- */
.profile-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  width: 100%;
}

.tab-pane {
  animation: tabFadeIn 0.3s ease;
}

@keyframes tabFadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* --- TAB 1: INFO PANE --- */
.info-pane {
  display: grid;
  grid-template-columns: 1.1fr 1.9fr;
  gap: 80px;
  align-items: start;
}

.info-list-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: #fafafa;
  padding: 32px;
  border-radius: 16px;
  border: 1px solid #f0f0f0;
}

.info-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.95rem;
  line-height: 1.4;
}

.info-label {
  font-weight: 500;
  color: #111;
  min-width: 140px;
}

.info-value {
  color: #333;
  font-weight: 600;
  text-align: right;
  word-break: break-word;
}

/* Properties Grid */
.properties-container {
  display: flex;
  flex-direction: column;
}

.section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #111;
  margin-top: 0;
  margin-bottom: 24px;
}

.properties-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 16px;
}

.landlord-prop-card {
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 1.15;
  cursor: pointer;
  position: relative;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.landlord-prop-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.prop-img-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

.prop-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.prop-gradient-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.2) 50%, transparent 100%);
}

.prop-overlay-name {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* --- TAB 2: VERIFICATION PANE --- */
.verification-pane {
  max-width: 700px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.verification-card {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid #eaeaea;
  background: #ffffff;
  transition: border-color 0.2s ease;
}

.verification-card:hover {
  border-color: #ddd;
}

.ver-icon-wrapper {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #f3f4f6;
  color: #9ca3af;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.ver-icon-wrapper.verified {
  background: #dcfce7;
  color: #16a34a;
}

.ver-copy {
  flex: 1;
}

.ver-copy h3 {
  font-size: 0.95rem;
  font-weight: 600;
  margin: 0 0 4px 0;
  color: #111;
}

.ver-copy p {
  font-size: 0.8rem;
  color: #666;
  margin: 0;
}

.ver-status-label {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 20px;
  background: #f3f4f6;
  color: #4b5563;
}

.ver-status-label.verified {
  background: #dcfce7;
  color: #15803d;
}

/* --- TAB 3: REVIEWS PANE --- */
.reviews-pane {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.reviews-summary-card {
  display: flex;
  gap: 60px;
  align-items: center;
  background: #fafafa;
  padding: 32px;
  border-radius: 16px;
  border: 1px solid #f0f0f0;
}

.overall-rating {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.rating-num {
  font-size: 3.2rem;
  font-weight: 800;
  color: #111;
  line-height: 1;
  margin-bottom: 8px;
}

.rating-stars {
  display: flex;
  gap: 2px;
  margin-bottom: 8px;
}

.rating-count {
  font-size: 0.8rem;
  color: #666;
  font-weight: 500;
}

.rating-breakdown {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rating-bar-row {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.82rem;
  font-weight: 500;
  color: #333;
}

.star-label {
  min-width: 32px;
}

.rating-bar-bg {
  flex: 1;
  height: 6px;
  background: #eaeaea;
  border-radius: 3px;
  overflow: hidden;
}

.rating-bar-fill {
  height: 100%;
  background: #f59e0b;
  border-radius: 3px;
}

.star-percent {
  min-width: 36px;
  text-align: right;
  color: #666;
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tenant-review-card {
  padding: 24px;
  border: 1px solid #eaeaea;
  border-radius: 16px;
  background: #fff;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.tenant-review-card:hover {
  border-color: #ddd;
}

.review-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.reviewer-img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid #eaeaea;
}

.reviewer-meta {
  flex: 1;
}

.reviewer-meta h4 {
  font-size: 0.92rem;
  font-weight: 600;
  margin: 0 0 2px 0;
  color: #111;
}

.reviewer-meta .review-date {
  font-size: 0.72rem;
  color: #999;
  font-weight: 500;
}

.reviewer-stars {
  display: flex;
  gap: 2px;
}

.review-text {
  font-size: 0.88rem;
  line-height: 1.55;
  color: #333;
  margin: 0;
  font-weight: 400;
}

/* --- RESPONSIVE --- */
@media (max-width: 900px) {
  .info-pane {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .reviews-summary-card {
    flex-direction: column;
    gap: 32px;
    align-items: stretch;
  }
  .overall-rating {
    align-items: center;
  }
}

@media (max-width: 768px) {
  .landlord-profile-page {
    height: 100dvh;
  }
  .top-nav {
    padding: 0 20px;
  }
  .back-btn {
    left: 20px;
    top: 16px;
    padding: 6px 12px;
    font-size: 0.8rem;
  }
  .banner-wrapper {
    height: 160px;
  }
  .profile-meta-container {
    padding: 0 20px 16px;
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  .profile-meta-content {
    gap: 16px;
  }
  .landlord-avatar-wrapper {
    width: 100px;
    height: 100px;
  }
  .landlord-name {
    font-size: 1.4rem;
  }
  .message-btn {
    width: 100%;
    justify-content: center;
    margin-bottom: 0;
  }
  .tabs-wrapper {
    padding: 0 20px;
  }
  .tab-buttons {
    gap: 20px;
  }
  .tab-btn {
    font-size: 0.85rem;
    padding: 12px 0;
  }
  .profile-content {
    padding: 24px 20px;
  }
  .info-list-container {
    padding: 20px;
    border-radius: 12px;
  }
  .info-label {
    min-width: 120px;
    font-size: 0.85rem;
  }
  .info-value {
    font-size: 0.85rem;
  }
}

/* --- Direct Message Modal --- */
.chat-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.chat-modal-box {
  width: 90%;
  max-width: 500px;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  animation: modalScaleIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

@keyframes modalScaleIn {
  from { opacity: 0; transform: scale(0.96) translateY(10px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.chat-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid #f0f0f0;
}

.chat-modal-title-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-avatar-wrapper {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #ebebeb;
}

.chat-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.chat-landlord-info h3 {
  font-size: 1rem;
  font-weight: 700;
  color: #111;
  margin: 0 0 3px 0;
}

.chat-verified-badge {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.72rem;
  color: #16a34a;
  font-weight: 600;
}

.chat-close-btn {
  background: none;
  border: none;
  color: #999;
  cursor: pointer;
  padding: 4px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.chat-close-btn:hover {
  background: #f5f5f5;
  color: #333;
}

.chat-modal-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.chat-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #444;
}

.chat-textarea {
  width: 100%;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  padding: 14px;
  font-family: inherit;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #1a202c;
  outline: none;
  resize: none;
  transition: border-color 0.2s ease;
}

.chat-textarea:focus {
  border-color: #111;
}

.chat-textarea:disabled {
  background: #f8fafc;
  color: #a0aec0;
  cursor: not-allowed;
}

.chat-hint {
  font-size: 0.75rem;
  color: #718096;
  margin: 0;
}

.chat-modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 16px 24px;
  background: #f8fafc;
  border-top: 1px solid #f0f0f0;
}

.chat-cancel-btn {
  padding: 10px 18px;
  border: 1px solid #e2e8f0;
  background: #fff;
  color: #4a5568;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.chat-cancel-btn:hover:not(:disabled) {
  background: #f7fafc;
  color: #1a202c;
}

.chat-cancel-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.chat-send-btn {
  padding: 10px 20px;
  border: none;
  background: #111111;
  color: #fff;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-width: 120px;
  transition: all 0.2s ease;
}

.chat-send-btn:hover:not(:disabled) {
  background: #2a2a2a;
}

.chat-send-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.chat-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #ffffff;
  border-radius: 50%;
  animation: chatSpin 0.6s linear infinite;
}

@keyframes chatSpin {
  to { transform: rotate(360deg); }
}

/* Success Toast */
.chat-success-toast {
  position: fixed;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  background: #111111;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 30px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 600;
  z-index: 1100;
  pointer-events: none;
}

.toast-check-icon {
  color: #4ade80;
}

/* Transitions */
.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity 0.25s ease;
}
.modal-fade-enter-from, .modal-fade-leave-to {
  opacity: 0;
}

.toast-fade-enter-active, .toast-fade-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.toast-fade-enter-from {
  opacity: 0;
  transform: translate(-50%, 20px);
}
.toast-fade-leave-to {
  opacity: 0;
  transform: translate(-50%, -10px);
}
</style>
