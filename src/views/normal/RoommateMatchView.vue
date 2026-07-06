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
        <button class="btn-icon">
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

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const profiles = ref([
  {
    name: 'Ko Euntake',
    firstName: 'Soth',
    lastName: 'Sokhomal',
    gender: 'Male',
    relationship: 'In relationship',
    hobbies: [
      { name: 'Music', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>' },
      { name: 'Games', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect><path d="M12 12h.01M16 12h.01M8 12h.01"></path></svg>' },
      { name: 'Sports', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>' },
      { name: 'Movies', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>' }
    ],
    image: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=800&q=80'
  },
  {
    name: 'Chen Wei',
    firstName: 'Chen',
    lastName: 'Wei',
    gender: 'Male',
    relationship: 'Single',
    hobbies: [
      { name: 'Reading', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>' },
      { name: 'Cooking', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>' },
      { name: 'Photography', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>' },
      { name: 'Travel', icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>' }
    ],
    image: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=800&q=80'
  }
])

const currentIndex = ref(0)
const currentProfile = computed(() => profiles.value[currentIndex.value])

const nextProfile = () => {
  currentIndex.value = (currentIndex.value + 1) % profiles.value.length
}

const requestRoommate = () => {
  alert(`Roommate request sent to ${currentProfile.value.name}!`)
  nextProfile()
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.roommate-match-page {
  font-family: 'Inter', sans-serif;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  display: flex;
  background: #fff;
}

/* ── LEFT COLUMN ── */
.details-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  background: #fff;
  border-right: 1px solid #ebebeb;
  z-index: 10;
}

.top-nav {
  padding: 32px 40px;
}
.back-btn {
  width: 48px; height: 48px; border-radius: 50%;
  background: #111; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
}

.scroll-content {
  flex: 1;
  overflow-y: auto;
  padding: 0 40px 40px;
}
.scroll-content::-webkit-scrollbar { display: none; }

.page-title { font-size: 2.2rem; font-weight: 700; color: #111; margin-bottom: 12px; }
.profile-name { font-size: 1.6rem; font-weight: 600; color: #111; margin-bottom: 20px; }

.info-section { margin-bottom: 24px; }
.section-title { font-size: 1.2rem; font-weight: 600; color: #111; margin-bottom: 12px; }

.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group label { font-size: 0.85rem; font-weight: 500; color: #555; }
.form-group input {
  padding: 12px 16px; border: 1px solid #ccc; border-radius: 8px;
  font-size: 0.95rem; color: #111; font-family: inherit; font-weight: 500;
  outline: none; background: #fff;
}
.form-group input:read-only { color: #333; }

.pill-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
.info-pill {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid #ccc; border-radius: 8px;
  font-size: 0.95rem; font-weight: 500; color: #111;
}

.hobbies-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.hobby-pill {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid #ccc; border-radius: 8px;
  font-size: 0.95rem; font-weight: 500; color: #111;
}
.h-icon { display: flex; align-items: center; color: #111; }

.bottom-actions {
  padding: 24px 40px 40px;
  background: #fff;
  display: flex; gap: 12px;
  align-items: center;
}
.btn-outline {
  flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 16px; border: 1px solid #111; border-radius: 8px;
  background: #fff; color: #111; font-size: 0.95rem; font-weight: 600; cursor: pointer;
  transition: background 0.2s;
  white-space: nowrap;
}
.btn-outline:hover { background: #f5f5f5; }

.btn-black {
  flex: 1.5; display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 16px; border: none; border-radius: 8px;
  background: #111; color: #fff; font-size: 0.95rem; font-weight: 600; cursor: pointer;
  transition: background 0.2s;
}
.btn-black:hover { background: #222; }

.btn-icon {
  width: 52px; height: 52px; border-radius: 50%;
  background: #111; border: none; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; cursor: pointer;
}

/* ── RIGHT COLUMN ── */
.photo-panel {
  flex: 1;
  position: relative;
  background: #111;
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

@media (max-width: 480px) {
  .form-grid, .pill-grid, .hobbies-grid { grid-template-columns: 1fr; }
  .btn-outline, .btn-black { min-width: 100%; }
}
</style>
