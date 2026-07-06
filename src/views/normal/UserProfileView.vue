<template>
  <div class="user-profile-page">
    <!-- Top Nav -->
    <header class="top-nav">
      <div class="logo" @click="$router.push('/home')">
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
        <div class="avatar" style="cursor: pointer;" @click="goToProfile">
          <img :src="currentUserAvatar || defaultAvatar" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="User profile" />
        </div>
      </div>
    </header>

    <!-- Profile Hero Section -->
    <section class="profile-hero">
      <button class="back-btn" @click="goBack" aria-label="Go back">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">
          <path d="M15 18l-6-6 6-6"/>
        </svg>
      </button>

      <div class="banner-wrapper">
        <div class="banner-overlay"></div>
        <img src="https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=1600&q=80" alt="User Banner" class="banner-img" />
      </div>

      <div class="profile-meta-container">
        <div class="profile-meta-content">
          <div class="user-avatar-wrapper">
            <img :src="userInfo.avatar" alt="User Avatar" class="user-avatar" />
          </div>
          
          <div class="user-summary">
            <div class="user-name-row">
              <h1 class="user-name">{{ userInfo.firstName }} {{ userInfo.lastName }}</h1>
            </div>
            <p class="user-tagline">{{ userInfo.tagline }}</p>
          </div>
        </div>

        <div class="profile-actions">
          <button class="message-btn" @click="messageUser">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            Message
          </button>
          
          <button class="action-btn" @click="toggleFriend" :class="{ 'friend-added': isFriend }">
            <svg v-if="!isFriend" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="8.5" cy="7" r="4"></circle>
              <line x1="20" y1="8" x2="20" y2="14"></line>
              <line x1="23" y1="11" x2="17" y2="11"></line>
            </svg>
            <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="8.5" cy="7" r="4"></circle>
              <polyline points="17 11 19 13 23 9"></polyline>
            </svg>
            {{ isFriend ? 'Friends' : 'Add Friend' }}
          </button>
        </div>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <section class="profile-tabs-section">
      <div class="tabs-wrapper">
        <div class="tab-buttons">
          <button class="tab-btn" :class="{ active: activeTab === 'info' }" @click="activeTab = 'info'">
            Info
          </button>
          <button class="tab-btn" :class="{ active: activeTab === 'posts' }" @click="activeTab = 'posts'">
            Posts
          </button>
          <button class="tab-btn" :class="{ active: activeTab === 'friends' }" @click="activeTab = 'friends'">
            Mutual Friends
          </button>
        </div>
      </div>
    </section>

    <!-- Main Content Area -->
    <main class="profile-content">
      <div v-if="activeTab === 'info'" class="tab-pane info-pane">
        <div class="info-list-container">
          <div class="info-row" v-for="item in userDetails" :key="item.label">
            <span class="info-label">{{ item.label }} :</span>
            <span class="info-value">{{ item.value }}</span>
          </div>
        </div>
      </div>

      <div v-else-if="activeTab === 'posts'" class="tab-pane posts-pane">
        <div class="empty-state">
          <p>This user hasn't posted anything recently.</p>
        </div>
      </div>

      <div v-else-if="activeTab === 'friends'" class="tab-pane friends-pane">
        <div class="empty-state">
          <p>No mutual friends to show.</p>
        </div>
      </div>
    </main>

    <GlobalFooter />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import GlobalFooter from '../../components/GlobalFooter.vue'
import { auth } from '../../firebase'

const route = useRoute()
const router = useRouter()

const goToProfile = () => {
  sessionStorage.setItem('homeActiveTab', 'settings')
  router.push('/home')
}

const defaultAvatar = 'https://ui-avatars.com/api/?name=User&background=random'
const currentUserAvatar = ref('')
const activeTab = ref('info')
const isFriend = ref(false)

const userInfo = ref({
  firstName: 'Loading',
  lastName: '...',
  tagline: 'Student | Tech Enthusiast',
  avatar: defaultAvatar
})

const userDetails = ref([
  { label: 'Location', value: 'Phnom Penh, Cambodia' },
  { label: 'Joined', value: 'January 2024' },
  { label: 'Bio', value: 'Looking for a quiet place to stay near the university.' }
])

onMounted(() => {
  if (auth.currentUser) {
    currentUserAvatar.value = auth.currentUser.photoURL || defaultAvatar
  }

  // Mocking the data based on ID (for now)
  const id = route.params.id
  if (id === '1') {
    userInfo.value.firstName = 'Yim'
    userInfo.value.lastName = 'Vatey'
    userInfo.value.avatar = 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80'
  } else if (id === '2') {
    userInfo.value.firstName = 'James'
    userInfo.value.lastName = 'Son'
    userInfo.value.avatar = 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&q=80'
  } else if (id === '3') {
    userInfo.value.firstName = 'Muy'
    userInfo.value.lastName = 'Leng'
    userInfo.value.avatar = 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&q=80'
  } else if (id === '4') {
    userInfo.value.firstName = 'Neav'
    userInfo.value.lastName = 'Sveita'
    userInfo.value.avatar = 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80'
  } else if (id === '5') {
    userInfo.value.firstName = 'Dave'
    userInfo.value.lastName = 'Rim'
    userInfo.value.avatar = 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&q=80'
  } else {
    userInfo.value.firstName = 'User'
    userInfo.value.lastName = id || 'Profile'
  }
})

const setDefaultAvatar = (e) => {
  e.target.src = defaultAvatar
}

const goBack = () => {
  router.push('/home')
}

const messageUser = () => {
  alert('Messaging feature coming soon!')
}

const toggleFriend = () => {
  isFriend.value = !isFriend.value
}
</script>

<style scoped>
.user-profile-page {
  font-family: 'DM Sans', sans-serif;
  background-color: #ffffff;
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

/* Top Nav */
.top-nav {
  display: flex; justify-content: space-between; align-items: center;
  padding: 16px 40px; background: #fff;
  border-bottom: 1px solid rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100;
}
.logo { display: flex; align-items: center; gap: 8px; cursor: pointer; color: #5C4E4A; }
.logo-icon {
  width: 32px; height: 32px; color: #5C4E4A;
  display: flex; align-items: center; justify-content: center;
}
.logo-text { font-size: 1.3rem; font-weight: 600; color: #5C4E4A; letter-spacing: -0.5px; }
.nav-right { display: flex; align-items: center; gap: 20px; }
.avatar img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }

/* Profile Hero */
.profile-hero { position: relative; width: 100%; border-bottom: 1px solid #eaeaea; background: #ffffff; }
.back-btn {
  position: absolute; top: 32px; left: 32px; z-index: 10;
  width: 40px; height: 40px; border-radius: 50%;
  background: #5C4E4E; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: transform 0.2s ease;
}
.back-btn:hover { transform: scale(1.05); }
.banner-wrapper { width: 100%; height: 220px; position: relative; overflow: hidden; }
.banner-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.3)); z-index: 1; }
.banner-img { width: 100%; height: 100%; object-fit: cover; }

/* Profile Meta */
.profile-meta-container {
  display: flex; justify-content: space-between; align-items: flex-end;
  max-width: 1200px; margin: 0 auto; padding: 0 40px 24px; margin-top: -60px; position: relative; z-index: 10;
}
.profile-meta-content { display: flex; align-items: flex-end; gap: 24px; }
.user-avatar-wrapper {
  width: 150px; height: 150px; border-radius: 50%;
  border: 5px solid #ffffff; overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  background: #ffffff; flex-shrink: 0;
}
.user-avatar { width: 100%; height: 100%; object-fit: cover; }
.user-summary { padding-bottom: 12px; }
.user-name-row { display: flex; align-items: center; gap: 10px; margin-bottom: 6px; }
.user-name { font-size: 2.2rem; font-weight: 800; color: #5C4E4E; margin: 0; letter-spacing: -0.5px; }
.user-tagline { font-size: 1.05rem; color: #555; margin: 0; font-weight: 500; }

.profile-actions { display: flex; gap: 12px; margin-bottom: 12px; }
.message-btn {
  display: flex; align-items: center; gap: 8px; padding: 12px 28px;
  background: #5C4E4E; color: #fff; border: none; border-radius: 24px;
  font-size: 1.05rem; font-weight: 600; cursor: pointer; transition: background 0.2s;
}
.message-btn:hover { background: #4a3d3d; }
.action-btn {
  display: flex; align-items: center; gap: 8px; padding: 12px 28px;
  background: #fff; color: #5C4E4E; border: 1px solid #5C4E4E; border-radius: 24px;
  font-size: 1.05rem; font-weight: 600; cursor: pointer; transition: all 0.2s;
}
.action-btn:hover { background: #f7f7f7; }
.action-btn.friend-added { background: #5C4E4E; color: #fff; }

/* Tabs */
.profile-tabs-section {
  max-width: 1000px; margin: 40px auto 0; padding: 0 32px;
  border-bottom: 1px solid #eaeaea;
}
.tabs-wrapper { display: flex; justify-content: space-between; align-items: center; }
.tab-buttons { display: flex; gap: 32px; }
.tab-btn {
  padding: 0 0 16px; background: none; border: none; border-bottom: 3px solid transparent;
  font-size: 1.05rem; font-weight: 600; color: #666; cursor: pointer;
  transition: all 0.2s; font-family: 'DM Sans', sans-serif;
}
.tab-btn:hover { color: #5C4E4E; }
.tab-btn.active { color: #5C4E4E; border-bottom-color: #5C4E4E; }

/* Main Content */
.profile-content { max-width: 1000px; margin: 40px auto; padding: 0 32px; width: 100%; flex: 1; }
.tab-pane { animation: fadeIn 0.4s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

/* Info Pane */
.info-list-container {
  background: #fff; border-radius: 20px; padding: 32px; border: 1px solid #eaeaea; box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  display: grid; grid-template-columns: 1fr; gap: 20px; max-width: 600px;
}
.info-row { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed #eaeaea; padding-bottom: 16px; }
.info-row:last-child { border-bottom: none; padding-bottom: 0; }
.info-label { font-size: 1rem; color: #666; font-weight: 500; }
.info-value { font-size: 1.05rem; color: #5C4E4A; font-weight: 600; text-align: right; }

.empty-state {
  background: #fff; border-radius: 20px; padding: 60px 32px; border: 1px solid #eaeaea; box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  text-align: center; color: #666; font-size: 1.1rem;
}

@media (max-width: 900px) {
  .profile-meta-container { flex-direction: column; align-items: center; margin-top: -80px; gap: 20px; }
  .profile-meta-content { flex-direction: column; align-items: center; text-align: center; }
  .user-name-row { justify-content: center; }
  .tabs-wrapper { flex-direction: column; gap: 20px; }
}

@media (max-width: 640px) {
  .top-nav { padding: 12px 20px; }
  .logo-text { display: none; }
  .banner-wrapper { width: 100%; border-radius: 0; height: 200px; }
  .back-btn { top: 16px; left: 16px; padding: 8px 12px; }
  .user-avatar-wrapper { width: 120px; height: 120px; }
  .user-name { font-size: 1.8rem; }
  .profile-actions { flex-direction: column; width: 100%; max-width: 300px; margin: 0 auto 20px; }
  .profile-tabs-section, .profile-content { padding: 0 20px; }
  .tab-buttons { gap: 20px; width: 100%; justify-content: space-between; }
}
</style>
