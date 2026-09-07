<template>
  <div class="roommate-match-page">
    
    <!-- Left Column: Details -->
    <div class="details-panel">
      
      <!-- Top Action -->
      <div class="top-nav">
        <button class="back-btn" @click="$router.go(-1)">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
      </div>

      <div class="scroll-content">
        <!-- Header -->
        <h1 class="page-title">Find Roommate</h1>
        <h2 class="profile-name">{{ currentProfile.name }}</h2>

        <!-- Personal Details -->
        <section class="info-section">
          <h3 class="section-title">Personal Details</h3>
          
          <div class="form-grid">
            <div class="form-group">
              <label>First Name</label>
              <input type="text" :value="currentProfile.firstName" readonly />
            </div>
            <div class="form-group">
              <label>Last Name</label>
              <input type="text" :value="currentProfile.lastName" readonly />
            </div>
          </div>

          <div class="pill-grid">
            <div class="info-pill">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
              {{ currentProfile.gender }}
            </div>
            <div class="info-pill">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
              {{ currentProfile.relationship }}
            </div>
          </div>
        </section>

        <!-- Hobbies -->
        <section class="info-section">
          <h3 class="section-title">Hobbies</h3>
          <div class="hobbies-grid">
            <div class="hobby-pill" v-for="hobby in currentProfile.hobbies" :key="hobby.name">
              <span class="h-icon" v-html="hobby.icon"></span>
              {{ hobby.name }}
            </div>
          </div>
        </section>
      </div>

      <!-- Bottom Action Bar -->
      <div class="bottom-actions">
        <button class="btn-outline" @click="nextProfile">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>
          Find Someone Else
        </button>
        <button class="btn-black" @click="requestRoommate">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
          Request as Roommate
        </button>
        <button class="btn-icon" @click="$router.push('/user-profile/' + (currentIndex + 1))" title="View Detailed Profile">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </button>
      </div>
    </div>

    <!-- Right Column: Photo -->
    <div class="photo-panel">
      <!-- Story Progress Indicators -->
      <div class="story-progress">
        <div class="progress-bar" v-for="(_, index) in profiles" :key="index" :class="{ active: index === currentIndex }"></div>
      </div>
      
      <!-- Image -->
      <img :src="currentProfile.image" alt="Profile Photo" class="profile-image" />
    </div>

    <!-- Non-blocking feedback toast -->
    <div v-if="showToast" class="roommate-toast">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
        <path d="M20 6L9 17l-5-5"/>
      </svg>
      <span>{{ toastMsg }}</span>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { db, auth } from '../../firebase.js'
import { collection, addDoc } from 'firebase/firestore'

const toastMsg = ref('')
const showToast = ref(false)

const triggerToast = (msg) => {
  toastMsg.value = msg
  showToast.value = true
  setTimeout(() => { showToast.value = false }, 3500)
}

const profiles = ref([
  {
    id: 1,
    name: 'Emily Davis',
    firstName: 'Emily',
    lastName: 'Davis',
    location: 'Phnom Penh Toul Kork',
    contact: '+855 12 345 678',
    gender: 'Female',
    relationship: 'Single',
    hobbies: [
      { name: 'Reading', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>' },
      { name: 'Cooking', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>' },
      { name: 'Travel', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>' }
    ],
    image: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=800&q=80'
  },
  {
    id: 2,
    name: 'Michael Chen',
    firstName: 'Michael',
    lastName: 'Chen',
    location: 'BKK1, Phnom Penh',
    contact: '+855 98 765 432',
    gender: 'Male',
    relationship: 'Single',
    hobbies: [
      { name: 'Gaming', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><rect x="2" y="6" width="20" height="12" rx="2"></rect></svg>' },
      { name: 'Music', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>' },
      { name: 'Fitness', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 16.326A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"></path><path d="M8 12h8"></path></svg>' }
    ],
    image: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=800&q=80'
  },
  {
    id: 3,
    name: 'Sarah Jenkins',
    firstName: 'Sarah',
    lastName: 'Jenkins',
    location: 'Tonle Bassac, Phnom Penh',
    contact: '+855 87 654 321',
    gender: 'Female',
    relationship: 'Single',
    hobbies: [
      { name: 'Art', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="13.5" cy="6.5" r=".5"></circle><circle cx="17.5" cy="10.5" r=".5"></circle><circle cx="8.5" cy="7.5" r=".5"></circle><circle cx="6.5" cy="12.5" r=".5"></circle><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"></path></svg>' },
      { name: 'Yoga', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20a6 6 0 0 0-12 0"/><circle cx="12" cy="10" r="4"/><circle cx="12" cy="12" r="10"/></svg>' },
      { name: 'Hiking', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m8 3 4 8 5-5 5 15H2L8 3z"/></svg>' }
    ],
    image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800&q=80'
  }
])

const currentIndex = ref(0)
const currentProfile = computed(() => profiles.value[currentIndex.value])

const nextProfile = () => {
  currentIndex.value = (currentIndex.value + 1) % profiles.value.length
}

const requestRoommate = async () => {
  const target = currentProfile.value
  triggerToast(`Roommate request sent to ${target.name}!`)
  
  try {
    await addDoc(collection(db, 'roommate_requests'), {
      senderId: auth.currentUser?.uid || 'guest_user',
      senderName: auth.currentUser?.displayName || 'Resident',
      senderEmail: auth.currentUser?.email || '',
      targetId: target.id,
      targetName: target.name,
      targetLocation: target.location,
      status: 'pending',
      createdAt: new Date().toISOString()
    })
  } catch (err) {
    console.warn('Roommate request Firestore notice:', err)
  }

  nextProfile()
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.roommate-match-page {
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  display: flex;
  background: #fff;
  color: #2A2421;
}

/* ── LEFT COLUMN ── */
.details-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  background: #fff;
  border-right: 1px solid #EDE8E3;
  z-index: 10;
}

.top-nav {
  padding: 32px 40px;
}
.back-btn {
  width: 48px; height: 48px; border-radius: 50%;
  background: #5C4E4E; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.15s ease;
}
.back-btn:hover {
  background: #473B3B;
}

.scroll-content {
  flex: 1;
  overflow-y: auto;
  padding: 0 40px 40px;
}
.scroll-content::-webkit-scrollbar { display: none; }

.page-title { font-size: 2.2rem; font-weight: 700; color: #2A2421; margin-bottom: 12px; }
.profile-name { font-size: 1.6rem; font-weight: 700; color: #5C4E4E; margin-bottom: 20px; }

.info-section { margin-bottom: 24px; }
.section-title { font-size: 1.2rem; font-weight: 700; color: #2A2421; margin-bottom: 12px; }

.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group label { font-size: 0.85rem; font-weight: 600; color: #5C4E4E; }
.form-group input {
  padding: 12px 16px; border: 1.5px solid #EDE8E3; border-radius: 10px;
  font-size: 0.95rem; color: #2A2421; font-family: inherit; font-weight: 500;
  outline: none; background: #FAF8F5;
  transition: all 0.15s ease;
}
.form-group input:read-only { color: #2A2421; }

.pill-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
.info-pill {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid #EDE8E3; border-radius: 10px;
  background: #FAF8F5;
  font-size: 0.95rem; font-weight: 500; color: #2A2421;
}

.hobbies-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.hobby-pill {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid #EDE8E3; border-radius: 10px;
  background: #FAF8F5;
  font-size: 0.95rem; font-weight: 500; color: #2A2421;
}
.h-icon { display: flex; align-items: center; color: #5C4E4E; }

.bottom-actions {
  padding: 24px 40px 40px;
  background: #fff;
  border-top: 1px solid #EDE8E3;
  display: flex; gap: 12px;
  align-items: center;
}
.btn-outline {
  flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 16px; border: 1.5px solid #5C4E4E; border-radius: 10px;
  background: #fff; color: #5C4E4E; font-size: 0.95rem; font-weight: 600; cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}
.btn-outline:hover { background: #FAF8F5; border-color: #473B3B; }

.btn-black {
  flex: 1.5; display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 16px; border: none; border-radius: 10px;
  background: #5C4E4E; color: #fff; font-size: 0.95rem; font-weight: 600; cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.15);
}
.btn-black:hover { background: #473B3B; box-shadow: 0 6px 16px rgba(92, 78, 78, 0.25); }

.btn-icon {
  width: 52px; height: 52px; border-radius: 50%;
  background: #5C4E4E; border: none; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; cursor: pointer;
  transition: background 0.15s;
}
.btn-icon:hover {
  background: #473B3B;
}

/* ── RIGHT COLUMN ── */
.photo-panel {
  flex: 1;
  position: relative;
  background: #2A2421;
  overflow: hidden;
}

.profile-image {
  width: 100%; height: 100%; object-fit: cover;
  display: block;
}

.story-progress {
  position: absolute; top: 16px; left: 16px; right: 16px;
  display: flex; gap: 6px; z-index: 10;
}
.progress-bar {
  flex: 1; height: 4px; background: rgba(255,255,255,0.4);
  border-radius: 2px;
}
.progress-bar.active { background: #fff; }

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .roommate-match-page { flex-direction: column; overflow-y: auto; }
  
  .photo-panel {
    flex: none; width: 100%; height: 50vh; min-height: 400px;
    order: -1; /* Move photo to top */
  }
  
  .details-panel {
    max-width: 100%; border-right: none;
    border-radius: 24px 24px 0 0;
    margin-top: -24px;
  }
  
  .top-nav { padding: 24px; }
  .scroll-content { padding: 0 24px 24px; }
  .bottom-actions { padding: 20px 24px 32px; flex-wrap: wrap; }
  
  .btn-outline, .btn-black { flex: 1; min-width: 200px; }
}

.roommate-toast {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  background: #2A2421;
  color: #fff;
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
