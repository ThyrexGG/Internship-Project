<template>
  <div class="find-roommate-page">
    
    <!-- Hero Image Area -->
    <section class="hero-section">
      <img :src="property.images[0]" alt="Hero Image" class="hero-image" />
      <div class="hero-overlay">
        <button class="back-btn" type="button" aria-label="Go back" @click="goBack">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <div class="roommate-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">
            <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>
            <path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>
          </svg>
          Roommate
        </div>
      </div>
    </section>

    <main class="main-content">
      <!-- Header Info -->
      <section class="header-info">
        <div class="header-left">
          <div class="page-title-row">
            <button class="form-back-btn" type="button" aria-label="Back to property" @click="goBack">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                <path d="M15 18l-6-6 6-6" />
              </svg>
            </button>
            <h1 class="page-title">Rental Application Form</h1>
          </div>
          <h2 class="property-subtitle">{{ property.name }}</h2>
        </div>
        <div class="header-right">
          <span class="price-amount">${{ property.price }}</span>
          <span class="price-period">/monthly</span>
        </div>
      </section>

      <!-- House Information -->
      <section class="house-info">
        <h3 class="section-heading">House Information</h3>
        
        <h4 class="sub-heading">House detail</h4>
        <div class="house-detail-icons">
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg><span>2/4 pax</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg><span>{{ property.beds }} bed</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg><span>{{ property.baths }} bath</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18M15 3v18"/></svg><span>1 int</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg><span>{{ property.sqft }}m</span></div>
        </div>

        <h4 class="sub-heading">Room Available</h4>
        <div class="rooms-grid">
          <button v-for="room in ['101A','101B','101C','102A','102B','102C','103A','103B','103C','104A','104B','104C']" 
                  :key="room" 
                  class="room-pill"
                  :class="{ selected: selectedRoom === room }"
                  @click="selectedRoom = room">
            {{ room }}
          </button>
        </div>
      </section>

      <!-- Photos -->
      <section class="photos-section">
        <h3 class="section-heading">Photos</h3>
        <div class="photos-container">
          <div class="photo-item" v-for="(img, idx) in property.images" :key="idx">
            <img :src="img" alt="Room Photo" />
            <button v-if="idx === property.images.length - 1" class="more-photos-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            </button>
          </div>
        </div>
      </section>

      <!-- Roommate -->
      <section class="roommate-cta">
        <h3 class="section-heading">Roommate</h3>
        <div class="cta-row">
          <p class="cta-text">This room doesn't anyone yet, please find a roommate.</p>
          <button class="btn-black" @click="$router.push('/roommate-match')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>
            </svg>
            Go find Roommate
          </button>
        </div>
      </section>

      <!-- Your Information -->
      <section class="user-info">
        <h3 class="section-heading">Your Information</h3>
        <h4 class="sub-heading">Basic Personal Info</h4>
        
        <div class="form-grid">
          <div class="form-group">
            <label>First Name</label>
            <input type="text" v-model="form.firstName" placeholder="Soth" />
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="text" v-model="form.lastName" placeholder="Sokhomal" />
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              <input type="text" v-model="form.dob" placeholder="15 Oct, 2006" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <input type="text" v-model="form.gender" placeholder="Female" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M4 12h16M12 4v16"/></svg>
              <input type="text" v-model="form.phone" placeholder="01156787697" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
              <input type="text" v-model="form.relationship" placeholder="In relationship" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              <input type="text" v-model="form.address" placeholder="Preak Leab, Chroy Chongva" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
              <input type="text" v-model="form.altPhone" placeholder="081 503 109" />
            </div>
          </div>
        </div>
      </section>

      <!-- Landlord Information -->
      <section class="landlord-info">
        <h3 class="section-heading">Landlord Information</h3>
        <div class="landlord-card">
          <div class="l-avatar">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=80&q=80" alt="Landlord" />
            <span class="l-name">{{ property.name }} Cambodia</span>
          </div>
          <span class="l-view">View profile &rarr;</span>
        </div>
        <div class="landlord-details-grid">
          <div class="detail-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            {{ property.name }} Premium
          </div>
          <div class="detail-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
            081 743 949/ 077 843 984
          </div>
          <div class="detail-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            Chroy Chongva, Phnum Penh
          </div>
        </div>
      </section>

      <!-- Agreement -->
      <section class="agreement-info">
        <h3 class="section-heading">Agreement & Legal Information</h3>
        <div class="doc-row" @click="handleDownload" style="cursor: pointer;">
          <span>Download All the Application Form</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        </div>
        <div class="doc-row borderless" @click="triggerUploadForm" style="cursor: pointer;">
          <input type="file" ref="fileUploadRef" accept=".pdf,.doc,.docx,.png,.jpg" style="display: none;" @change="onFileAttached" />
          <span v-if="!uploadedFormFileName">Upload Application Form</span>
          <span v-else style="color: #15803d; font-weight: 600;">✓ Attached: {{ uploadedFormFileName }}</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        </div>
      </section>

      <!-- Feedback Toast -->
      <div v-if="showToast" class="submit-toast">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
        <span>{{ toastMessage }}</span>
      </div>

      <div class="spacer"></div>
      <GlobalFooter />
    </main>

    <!-- Footer Action Bar -->
    <footer class="bottom-action-bar">
      <div class="payment-info">
        <span class="payment-label">Monthly rent after sharing:</span>
        <div class="payment-val">
           <span class="p-amount">${{ Math.round(property.price / 2) }}</span><span class="p-period">/mo</span>
        </div>
      </div>
      <button class="btn-submit" @click="handleSubmit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Submitting Application...' : 'Submit Application' }}
      </button>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import GlobalFooter from '../../components/GlobalFooter.vue'
import { properties } from '../../store.js'
import { db, auth } from '../../firebase.js'
import { collection, addDoc } from 'firebase/firestore'

const route = useRoute()
const router = useRouter()
const propertyId = parseInt(route.params.id)

// Find property
const property = computed(() => {
  return properties.value.find(p => p.id === propertyId) || properties.value[0]
})

const selectedRoom = ref('101A')
const isSubmitting = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const fileUploadRef = ref(null)
const uploadedFormFileName = ref('')

const form = reactive({
  firstName: '',
  lastName: '',
  dob: '',
  gender: '',
  phone: '',
  relationship: '',
  address: '',
  altPhone: ''
})

const triggerUploadForm = () => {
  if (fileUploadRef.value) {
    fileUploadRef.value.click()
  }
}

const onFileAttached = (e) => {
  const file = e.target.files[0]
  if (file) {
    uploadedFormFileName.value = file.name
    toastMessage.value = `File attached: ${file.name}`
    showToast.value = true
    setTimeout(() => { showToast.value = false }, 3000)
  }
}

const handleSubmit = async () => {
  if (isSubmitting.value) return

  isSubmitting.value = true
  
  try {
    const monthlySharePrice = Math.round(property.value.price / 2)
    const applicantName = `${form.firstName || 'Resident'} ${form.lastName || 'Applicant'}`.trim()

    // 1. Real persistence to Firestore 'rental_applications' collection
    await addDoc(collection(db, 'rental_applications'), {
      propertyId: property.value.id,
      propertyName: property.value.name,
      propertyLocation: property.value.location,
      selectedRoom: selectedRoom.value,
      price: monthlySharePrice,
      isRoommateSharing: true,
      tenantId: auth.currentUser?.uid || 'guest_' + Date.now(),
      tenantName: applicantName,
      tenantEmail: auth.currentUser?.email || '',
      firstName: form.firstName,
      lastName: form.lastName,
      dob: form.dob,
      gender: form.gender,
      phone: form.phone,
      relationship: form.relationship,
      address: form.address,
      altPhone: form.altPhone,
      attachedFileName: uploadedFormFileName.value || null,
      status: 'pending',
      createdAt: new Date().toISOString()
    })

    // 2. Add real notification for landlord
    try {
      await addDoc(collection(db, 'notifications'), {
        type: 'booking',
        title: 'New Roommate Application',
        desc: `${applicantName} applied for room ${selectedRoom.value} in ${property.value.name}.`,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        group: 'Today',
        unread: true,
        date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        roomName: `${property.value.name}, Room ${selectedRoom.value}`,
        amount: `$${monthlySharePrice}`,
        createdAt: new Date().toISOString()
      })
    } catch (notifErr) {
      console.warn("Notification sync notice:", notifErr)
    }

    toastMessage.value = 'Application submitted successfully!'
    showToast.value = true

    setTimeout(() => {
      router.push('/home')
    }, 1200)
  } catch (error) {
    console.error("Submission error:", error)
    toastMessage.value = 'Failed to submit application. Please try again.'
    showToast.value = true
    setTimeout(() => { showToast.value = false }, 3500)
  } finally {
    isSubmitting.value = false
  }
}

const goBack = () => {
  router.push(`/property/${property.value.id}`)
}

const handleDownload = () => {
  const applicantName = `${form.firstName || 'Applicant'} ${form.lastName || ''}`.trim()
  const contractContent = `=====================================================
HOMESWEET RESIDENTIAL ROOMMATE LEASE APPLICATION
=====================================================
Date: ${new Date().toLocaleDateString()}
Property: ${property.value.name}
Location: ${property.value.location}
Selected Room: ${selectedRoom.value}
Monthly Rent (Share): $${Math.round(property.value.price / 2)}.00 / month

APPLICANT INFORMATION:
Name: ${applicantName}
Date of Birth: ${form.dob || 'N/A'}
Gender: ${form.gender || 'N/A'}
Contact Phone: ${form.phone || 'N/A'}
Current Address: ${form.address || 'N/A'}
Alternate Contact: ${form.altPhone || 'N/A'}

TERMS & CONDITIONS:
1. The applicant agrees to abide by building regulations, noise guidelines, and common area cleanliness rules.
2. Roommate disputes shall be mediated through the HomeSweet residential community portal.
3. Subletting without landlord consent is strictly prohibited.

Applicant Signature: _______________________
Date: _______________________
=====================================================`

  const element = document.createElement('a')
  const file = new Blob([contractContent], { type: 'text/plain;charset=utf-8' })
  element.href = URL.createObjectURL(file)
  element.download = `${property.value.name.replace(/\s+/g, '_')}_Roommate_Application.txt`
  document.body.appendChild(element)
  element.click()
  document.body.removeChild(element)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.find-roommate-page {
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #fff;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  color: #2A2421;
  display: flex;
  flex-direction: column;
}

/* ── HERO ── */
.hero-section {
  position: relative;
  width: 100%;
  max-width: 1200px;
  height: 280px;
  margin: 24px auto 0;
  border-radius: 16px;
  overflow: hidden;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
}
.hero-image {
  width: 100%; height: 100%; object-fit: cover;
}
.hero-overlay {
  position: absolute; inset: 0;
  padding: 24px;
  display: flex; flex-direction: column; justify-content: space-between;
  background: linear-gradient(180deg, rgba(42,36,33,0.25) 0%, rgba(42,36,33,0) 40%, rgba(42,36,33,0.3) 100%);
}
.back-btn {
  width: 40px; height: 40px; border-radius: 50%;
  background: #5C4E4E; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.15s ease;
}
.back-btn:hover {
  background: #473B3B;
}
.roommate-badge {
  background: #5C4E4E; color: #fff;
  align-self: flex-start;
  padding: 8px 16px; border-radius: 8px;
  display: flex; align-items: center; gap: 8px;
  font-size: 0.9rem; font-weight: 500;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.2);
}

/* ── MAIN CONTENT ── */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 40px 100px;
  width: 100%;
}

.section-heading {
  font-size: 1.4rem; font-weight: 700; color: #2A2421;
  margin-bottom: 20px;
}
.sub-heading {
  font-size: 1.1rem; font-weight: 600; color: #2A2421;
  margin-bottom: 12px; margin-top: 24px;
}
.sub-heading:first-of-type { margin-top: 0; }

/* Header Info */
.header-info {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 40px;
}
.page-title-row {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}
.form-back-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #EDE8E3;
  border-radius: 50%;
  background: #FAF8F5;
  color: #5C4E4E;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: all 0.15s ease;
}
.form-back-btn:hover {
  background: #F4EDEA;
  border-color: #5C4E4E;
}
.page-title {
  font-size: 2rem; font-weight: 700; color: #2A2421; margin-bottom: 8px; line-height: 1.2;
}
.property-subtitle {
  font-size: 1.4rem; font-weight: 500; color: #5C4E4E;
}
.header-right {
  display: flex; align-items: baseline; gap: 4px;
}
.price-amount { font-size: 1.8rem; font-weight: 700; color: #5C4E4E; }
.price-period { font-size: 0.9rem; font-weight: 600; color: #8C7E7E; }

/* House Info */
.house-info { margin-bottom: 48px; }
.house-detail-icons {
  display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 32px;
}
.d-icon {
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;
  width: 60px; height: 60px;
  border: 1px solid #EDE8E3; border-radius: 10px;
  background: #FAF8F5;
  font-size: 0.65rem; font-weight: 600; color: #5C4E4E;
}

.rooms-grid {
  display: flex; flex-wrap: wrap; gap: 12px; max-width: 400px;
}
.room-pill {
  background: #fff; border: 1.5px solid #EDE8E3; border-radius: 8px;
  padding: 8px 14px; font-size: 0.72rem; font-weight: 600; color: #8C7E7E;
  cursor: pointer; transition: all 0.2s;
  font-family: inherit;
}
.room-pill:hover {
  border-color: #5C4E4E; color: #5C4E4E; background: #FAF8F5;
}
.room-pill.selected {
  border-color: #5C4E4E; color: #ffffff; background: #5C4E4E;
}

/* Photos */
.photos-section { margin-bottom: 48px; }
.photos-container {
  display: flex; gap: 16px; overflow-x: auto; scrollbar-width: none;
}
.photos-container::-webkit-scrollbar { display: none; }
.photo-item {
  position: relative;
  width: 280px; height: 380px; border-radius: 16px; overflow: hidden; flex-shrink: 0;
  border: 1px solid #EDE8E3;
}
.photo-item img { width: 100%; height: 100%; object-fit: cover; }
.more-photos-btn {
  position: absolute; top: 50%; right: 16px; transform: translateY(-50%);
  width: 40px; height: 40px; border-radius: 50%;
  background: rgba(255,255,255,0.9); border: 1px solid #EDE8E3; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  color: #5C4E4E;
}

/* Roommate CTA */
.roommate-cta { margin-bottom: 48px; }
.cta-row {
  display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 16px;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  padding: 20px 24px;
  border-radius: 14px;
}
.cta-text { font-size: 1.05rem; font-weight: 600; color: #2A2421; }
.btn-black {
  background: #5C4E4E; color: #fff; border: none; border-radius: 10px;
  padding: 12px 20px; font-size: 0.9rem; font-weight: 600; cursor: pointer;
  display: flex; align-items: center; gap: 8px;
  transition: background 0.15s ease;
  box-shadow: 0 2px 6px rgba(92, 78, 78, 0.15);
}
.btn-black:hover {
  background: #473B3B;
}

/* User Info Form */
.user-info { margin-bottom: 48px; }
.form-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
}
.form-group { display: flex; flex-direction: column; gap: 8px; }
.form-group label { font-size: 0.85rem; font-weight: 600; color: #5C4E4E; }
.form-group input {
  padding: 14px 16px; border: 1.5px solid #D1D5DB; border-radius: 10px;
  font-size: 0.92rem; color: #2A2421; font-family: inherit; font-weight: 500;
  outline: none; transition: all 0.2s;
  background: #ffffff;
}
.form-group input:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.input-with-icon {
  position: relative; display: flex; align-items: center;
}
.input-with-icon svg {
  position: absolute; left: 14px; color: #5C4E4E; pointer-events: none;
}
.input-with-icon input {
  width: 100%; padding-left: 42px;
}

/* Landlord Info */
.landlord-info { margin-bottom: 48px; }
.landlord-card {
  display: flex; justify-content: space-between; align-items: center;
  border: 1px solid #EDE8E3; border-radius: 14px; padding: 16px 20px;
  margin-bottom: 16px;
  background: #FAF8F5;
}
.l-avatar { display: flex; align-items: center; gap: 12px; }
.l-avatar img { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 1px solid #EDE8E3; }
.l-name { font-size: 0.95rem; font-weight: 600; color: #2A2421; }
.l-view { font-size: 0.85rem; color: #5C4E4E; font-weight: 600; cursor: pointer; }
.l-view:hover { text-decoration: underline; }

.landlord-details-grid {
  display: flex; gap: 16px; flex-wrap: wrap;
}
.detail-box {
  flex: 1; min-width: 200px;
  display: flex; align-items: center; gap: 12px;
  border: 1px solid #EDE8E3; border-radius: 10px; padding: 16px;
  font-size: 0.85rem; font-weight: 500; color: #2A2421;
  background: #ffffff;
  overflow-wrap: anywhere;
}
.detail-box svg {
  color: #5C4E4E;
  flex-shrink: 0;
}

/* Agreement */
.agreement-info { margin-bottom: 48px; }
.doc-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 18px 20px; border: 1px solid #EDE8E3; border-radius: 10px;
  font-size: 0.9rem; font-weight: 500; margin-bottom: 24px; cursor: pointer;
  background: #FAF8F5;
  color: #2A2421;
  transition: all 0.15s ease;
}
.doc-row:hover {
  background: #F4EDEA;
  border-color: #5C4E4E;
}
.doc-row svg {
  color: #5C4E4E;
}
.doc-row.borderless {
  border: none; padding: 0 4px; color: #2A2421; font-weight: 600; margin-bottom: 0; background: transparent;
}
.doc-row.borderless:hover {
  background: transparent;
}

.spacer { height: 100px; }

/* ── FOOTER ── */
.bottom-action-bar {
  position: sticky;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  background: #ffffff;
  border-top: 1px solid #EDE8E3;
  box-shadow: 0 -8px 24px rgba(92, 78, 78, 0.06);
  padding: 16px 8%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
}
.payment-info { display: flex; flex-direction: column; align-items: flex-start; gap: 4px; }
.payment-label { font-size: 0.88rem; font-weight: 500; color: #8C7E7E; }
.payment-val { display: flex; align-items: baseline; }
.p-amount { font-size: 1.8rem; font-weight: 700; color: #5C4E4E; line-height: 1; }
.p-period { font-size: 0.95rem; font-weight: 600; color: #8C7E7E; line-height: 1; margin-left: 2px; }

.btn-submit {
  width: auto;
  min-width: 200px;
  padding: 14px 32px;
  border-radius: 10px;
  background: #5C4E4E;
  color: #fff;
  border: none;
  font-size: 1rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.15);
}
.btn-submit:hover:not(:disabled) {
  background: #473B3B;
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.25);
  transform: translateY(-1px);
}
.btn-submit:active:not(:disabled) {
  transform: translateY(0);
}
.btn-submit:disabled {
  background: #EDE8E3;
  color: #8C7E7E;
  cursor: not-allowed;
  box-shadow: none;
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .find-roommate-page {
    width: 100vw;
    height: 100dvh;
  }
  .hero-section {
    width: 100%;
    max-width: none;
    margin: 0;
    border-radius: 0;
    height: 220px;
  }
  .hero-overlay { padding: 16px; }
  .main-content {
    width: 100%;
    max-width: none;
    margin: 0;
    padding: 24px 20px 80px;
  }
  .header-info { flex-direction: column; gap: 16px; margin-bottom: 32px; }
  .page-title { font-size: 1.55rem; }
  .property-subtitle { font-size: 1.05rem; }
  .price-amount { font-size: 1.45rem; }
  .section-heading { font-size: 1.22rem; margin-bottom: 16px; }
  .sub-heading { font-size: 1rem; }
  .house-info,
  .photos-section,
  .roommate-cta,
  .user-info,
  .landlord-info,
  .agreement-info {
    margin-bottom: 36px;
  }
  .house-detail-icons {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 8px;
  }
  .d-icon {
    width: 100%;
    height: 58px;
    min-width: 0;
    padding: 6px 2px;
    font-size: 0.58rem;
  }
  .rooms-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
    max-width: none;
  }
  .room-pill {
    width: 100%;
    padding: 10px 6px;
    text-align: center;
  }
  .photos-container {
    margin: 0 -20px;
    padding: 0 20px 4px;
    gap: 12px;
  }
  .photo-item {
    width: min(76vw, 280px);
    height: 260px;
    border-radius: 12px;
  }
  .cta-row {
    align-items: stretch;
  }
  .cta-text {
    width: 100%;
    font-size: 0.98rem;
    line-height: 1.4;
  }
  .btn-black {
    width: 100%;
    justify-content: center;
  }
  .form-grid { grid-template-columns: 1fr; }
  .form-group,
  .input-with-icon,
  .form-group input {
    min-width: 0;
  }
  .landlord-card {
    padding: 12px;
    gap: 12px;
  }
  .l-avatar {
    min-width: 0;
  }
  .l-name {
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .l-view {
    flex-shrink: 0;
  }
  .landlord-details-grid { flex-direction: column; }
  .detail-box {
    width: 100%;
    min-width: 0;
  }
  .doc-row {
    gap: 12px;
    padding: 16px 14px;
  }
  .doc-row span {
    min-width: 0;
    line-height: 1.35;
  }
  .bottom-action-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px 20px;
    background: #ffffff;
    border-top: 1px solid #EDE8E3;
    box-shadow: 0 -8px 24px rgba(92, 78, 78, 0.08);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
  }
  .payment-info { flex-direction: column; align-items: flex-start; gap: 2px; }
  .payment-label { font-size: 0.85rem; }
  .btn-submit {
    width: auto;
    min-width: 140px;
    padding: 12px 20px;
    font-size: 0.95rem;
  }
}

@media (max-width: 390px) {
  .hero-section {
    height: 200px;
  }
  .main-content {
    padding-left: 14px;
    padding-right: 14px;
  }
  .house-detail-icons {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  .rooms-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .photos-container {
    margin-left: -14px;
    margin-right: -14px;
    padding-left: 14px;
    padding-right: 14px;
  }
  .photo-item {
    width: 80vw;
    height: 230px;
  }
  .landlord-card {
    align-items: flex-start;
    flex-direction: column;
  }
  .l-name {
    white-space: normal;
  }
  .bottom-action-bar {
    padding-left: 14px;
    padding-right: 14px;
  }
}

.submit-toast {
  position: fixed;
  bottom: 90px;
  left: 50%;
  transform: translateX(-50%);
  background: #2A2421;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.92rem;
  font-weight: 600;
  box-shadow: 0 10px 25px rgba(42, 36, 33, 0.3);
  z-index: 99999;
  animation: fadeInToast 0.25s ease-out;
}

@keyframes fadeInToast {
  from { opacity: 0; transform: translate(-50%, 15px); }
  to { opacity: 1; transform: translate(-50%, 0); }
}
</style>

