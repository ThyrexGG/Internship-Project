<template>
  <div class="notification-dropdown-wrapper" ref="dropdownRef">
    <!-- Trigger Bell Button -->
    <button 
      type="button" 
      class="notif-trigger-btn" 
      :class="{ 'is-active': isOpen }" 
      aria-label="View notifications"
      :aria-expanded="isOpen"
      @click="toggleDropdown"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
        <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
      </svg>
      <span v-if="unreadCount > 0" class="notif-badge-count">
        {{ unreadCount > 99 ? '99+' : unreadCount }}
      </span>
    </button>

    <!-- Pop-Down Panel -->
    <transition name="dropdown-fade">
      <div v-if="isOpen" class="notif-popdown-panel" role="region" aria-label="Notifications popdown">
        <!-- Header -->
        <div class="popdown-header">
          <div class="header-title-row">
            <h3 class="popdown-title">Notifications</h3>
            <span v-if="unreadCount > 0" class="unread-pill">{{ unreadCount }} new</span>
          </div>
          <button 
            v-if="unreadCount > 0" 
            type="button" 
            class="btn-mark-all-read" 
            @click="markAllAsRead"
          >
            Mark all read
          </button>
        </div>

        <!-- Filter Pills -->
        <div class="popdown-filters">
          <button 
            type="button" 
            class="filter-pill" 
            :class="{ active: currentFilter === 'all' }" 
            @click="currentFilter = 'all'"
          >
            All
          </button>
          <button 
            type="button" 
            class="filter-pill" 
            :class="{ active: currentFilter === 'booking' }" 
            @click="currentFilter = 'booking'"
          >
            Bookings
          </button>
          <button 
            type="button" 
            class="filter-pill" 
            :class="{ active: currentFilter === 'payment' }" 
            @click="currentFilter = 'payment'"
          >
            Payments
          </button>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="popdown-loading">
          <div class="skeleton-row" v-for="i in 3" :key="i">
            <div class="skeleton-avatar"></div>
            <div class="skeleton-lines">
              <div class="skeleton-line line-short"></div>
              <div class="skeleton-line line-long"></div>
            </div>
          </div>
        </div>

        <!-- Notification List -->
        <div v-else-if="filteredItems.length > 0" class="popdown-list">
          <div 
            v-for="item in filteredItems" 
            :key="item.id" 
            class="notif-card-item"
            :class="{ 'is-unread': item.unread }"
            @click="handleItemClick(item)"
          >
            <div class="item-icon-col">
              <div class="item-icon-badge" :class="item.type || 'system'">
                <!-- Booking Icon -->
                <svg v-if="item.type === 'booking'" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.5z"/>
                  <path d="M9 21V12h6v9"/>
                </svg>
                <!-- Payment Icon -->
                <svg v-else-if="item.type === 'payment'" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="2" y="5" width="20" height="14" rx="2"/>
                  <line x1="2" y1="10" x2="22" y2="10"/>
                </svg>
                <!-- Default / System Icon -->
                <svg v-else width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>
                </svg>
              </div>
            </div>

            <div class="item-body">
              <div class="item-header-row">
                <span class="item-title">{{ item.title }}</span>
                <span class="item-timestamp">{{ item.time || item.date || 'Just now' }}</span>
              </div>
              <p class="item-desc">{{ item.desc || item.message }}</p>
              <div v-if="item.roomName || item.amount" class="item-meta-tag">
                <span v-if="item.roomName" class="tag-prop">{{ item.roomName }}</span>
                <span v-if="item.amount" class="tag-price">{{ item.amount }}</span>
              </div>
            </div>

            <div class="item-action-col">
              <span v-if="item.unread" class="unread-dot" title="Unread"></span>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div v-else class="popdown-empty">
          <div class="empty-icon-bubble">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8C7E7E" stroke-width="1.8">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
            </svg>
          </div>
          <h4 class="empty-headline">All caught up!</h4>
          <p class="empty-subtext">You have no {{ currentFilter !== 'all' ? currentFilter : '' }} notifications right now.</p>
        </div>

        <!-- Footer -->
        <div class="popdown-footer">
          <button type="button" class="btn-footer-link" @click="navigateToInbox">
            View All in Landlord Portal &rarr;
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { db } from '../firebase'
import { collection, getDocs, doc, updateDoc } from 'firebase/firestore'

const router = useRouter()
const dropdownRef = ref(null)
const isOpen = ref(false)
const isLoading = ref(false)
const currentFilter = ref('all')

// Base notifications list with default seed items for immediate UX
const notifications = ref([
  {
    id: 'booking-1',
    type: 'booking',
    title: 'New Booking Request',
    desc: 'Alice has requested to book Skystar Condo (Room 105).',
    time: '12m ago',
    unread: true,
    roomName: 'Skystar Condo',
    amount: '$200/mo'
  },
  {
    id: 'payment-1',
    type: 'payment',
    title: 'Payment Received',
    desc: 'Aurafa Condo has completed monthly rent payment.',
    time: '1h ago',
    unread: true,
    roomName: 'Aurafa Condo',
    amount: '$120'
  },
  {
    id: 'system-1',
    type: 'system',
    title: 'Account Identity Status',
    desc: 'Your verification submission is being processed by safety review.',
    time: '2h ago',
    unread: false
  },
  {
    id: 'payment-2',
    type: 'payment',
    title: 'Payment Received',
    desc: 'Skystar Condo deposit invoice settled.',
    time: 'Yesterday',
    unread: false,
    amount: '$400'
  }
])

const unreadCount = computed(() => {
  return notifications.value.filter(n => n.unread).length
})

const filteredItems = computed(() => {
  if (currentFilter.value === 'all') return notifications.value
  return notifications.value.filter(n => n.type === currentFilter.value)
})

function toggleDropdown() {
  isOpen.value = !isOpen.value
}

function closeDropdown() {
  isOpen.value = false
}

function handleOutsideClick(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    closeDropdown()
  }
}

function handleKeyDown(event) {
  if (event.key === 'Escape' && isOpen.value) {
    closeDropdown()
  }
}

async function markAllAsRead() {
  notifications.value.forEach(item => {
    item.unread = false
  })

  // Try updating in Firestore if documents exist
  try {
    const unreadDocs = notifications.value.filter(n => n._isFirestore && n.unread)
    for (const d of unreadDocs) {
      await updateDoc(doc(db, 'notifications', d.id), { unread: false })
    }
  } catch (err) {
    console.warn('Silent notice marking all notifications read:', err)
  }
}

async function handleItemClick(item) {
  item.unread = false
  try {
    if (item._isFirestore) {
      await updateDoc(doc(db, 'notifications', item.id), { unread: false })
    }
  } catch (err) {
    console.warn('Notice updating notification item:', err)
  }

  closeDropdown()
  if (item.type === 'booking') {
    router.push('/landlord')
  } else if (item.type === 'payment') {
    router.push('/payment')
  }
}

function navigateToInbox() {
  closeDropdown()
  router.push('/landlord')
}

// Fetch live notifications from Firestore
async function fetchLiveNotifications() {
  isLoading.value = true
  try {
    const snap = await getDocs(collection(db, 'notifications'))
    if (!snap.empty) {
      const liveList = []
      snap.forEach(d => {
        liveList.push({ id: d.id, _isFirestore: true, ...d.data() })
      })
      // Prepend live notifications
      notifications.value = [...liveList, ...notifications.value.filter(n => !n._isFirestore)]
    }
  } catch (err) {
    console.warn('Using local notification state:', err)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleOutsideClick)
  document.addEventListener('keydown', handleKeyDown)
  fetchLiveNotifications()
})

onUnmounted(() => {
  document.removeEventListener('click', handleOutsideClick)
  document.removeEventListener('keydown', handleKeyDown)
})
</script>

<style scoped>
.notification-dropdown-wrapper {
  position: relative;
  display: inline-flex;
  align-items: center;
}

/* Trigger Button */
.notif-trigger-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill, 50px);
  border: 1px solid var(--color-border, #ede8e3);
  background: var(--color-bg-surface, #ffffff);
  color: var(--color-primary, #5C4E4E);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast, 0.15s ease);
}

.notif-trigger-btn:hover,
.notif-trigger-btn.is-active {
  background: var(--color-primary-light, #F2EDE9);
  border-color: var(--color-primary, #5C4E4E);
  color: var(--color-primary-hover, #473B3B);
}

.notif-badge-count {
  position: absolute;
  top: -4px;
  right: -4px;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  border-radius: var(--radius-pill, 50px);
  background: #EF4444;
  color: #ffffff;
  font-size: 0.68rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #ffffff;
  box-shadow: 0 2px 5px rgba(239, 68, 68, 0.35);
}

/* Popdown Panel */
.notif-popdown-panel {
  position: absolute;
  right: 0;
  top: calc(100% + 10px);
  width: 380px;
  max-width: calc(100vw - 32px);
  max-height: 520px;
  background: var(--color-bg-surface, #ffffff);
  border: 1px solid var(--color-border, #ede8e3);
  border-radius: var(--radius-xl, 18px);
  box-shadow: var(--shadow-dropdown, 0 12px 36px rgba(42, 36, 33, 0.12));
  display: flex;
  flex-direction: column;
  z-index: 1100;
  overflow: hidden;
}

/* Popdown Header */
.popdown-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px 12px;
  border-bottom: 1px solid var(--color-border-subtle, #f2eee9);
}

.header-title-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.popdown-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-primary, #5C4E4E);
  margin: 0;
}

.unread-pill {
  font-size: 0.72rem;
  font-weight: 600;
  background: var(--color-primary-light, #F2EDE9);
  color: var(--color-primary, #5C4E4E);
  padding: 2px 8px;
  border-radius: var(--radius-pill, 50px);
}

.btn-mark-all-read {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-primary, #5C4E4E);
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 6px;
  border-radius: var(--radius-xs, 4px);
  transition: opacity var(--transition-fast, 0.15s ease);
}

.btn-mark-all-read:hover {
  text-decoration: underline;
  color: var(--color-primary-dark, #2A2421);
}

/* Filters */
.popdown-filters {
  display: flex;
  gap: 8px;
  padding: 10px 20px;
  background: var(--color-bg-canvas, #faf8f5);
  border-bottom: 1px solid var(--color-border-subtle, #f2eee9);
}

.filter-pill {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: var(--radius-pill, 50px);
  border: 1px solid var(--color-border, #ede8e3);
  background: #ffffff;
  color: var(--color-text-muted, #8C7E7E);
  cursor: pointer;
  transition: all var(--transition-fast, 0.15s ease);
}

.filter-pill.active {
  background: var(--color-primary, #5C4E4E);
  color: #ffffff;
  border-color: var(--color-primary, #5C4E4E);
}

/* List */
.popdown-list {
  flex: 1;
  overflow-y: auto;
  max-height: 340px;
}

.notif-card-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--color-border-subtle, #f2eee9);
  cursor: pointer;
  transition: background var(--transition-fast, 0.15s ease);
}

.notif-card-item:hover {
  background: var(--color-bg-canvas, #faf8f5);
}

.notif-card-item.is-unread {
  background: #FAF7F4;
}

.item-icon-badge {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-md, 10px);
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-light, #F2EDE9);
  color: var(--color-primary, #5C4E4E);
}

.item-icon-badge.payment {
  background: var(--color-success-bg, #ECFDF5);
  color: var(--color-success, #10B981);
}

.item-icon-badge.system {
  background: var(--color-info-bg, #EFF6FF);
  color: var(--color-info, #3B82F6);
}

.item-body {
  flex: 1;
  min-width: 0;
}

.item-header-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 2px;
}

.item-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-timestamp {
  font-size: 0.7rem;
  color: var(--color-text-muted, #8C7E7E);
  flex-shrink: 0;
}

.item-desc {
  font-size: 0.78rem;
  color: var(--color-text-secondary, #5C4E4E);
  line-height: 1.35;
  margin: 0 0 4px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.item-meta-tag {
  display: flex;
  gap: 6px;
  font-size: 0.7rem;
  margin-top: 2px;
}

.tag-prop {
  background: #EAE6E2;
  color: var(--color-text-secondary, #5C4E4E);
  padding: 1px 6px;
  border-radius: 4px;
  font-weight: 500;
}

.tag-price {
  background: var(--color-success-bg, #ECFDF5);
  color: var(--color-success, #10B981);
  padding: 1px 6px;
  border-radius: 4px;
  font-weight: 700;
}

.unread-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary, #5C4E4E);
  margin-top: 6px;
}

/* Empty State */
.popdown-empty {
  padding: 36px 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.empty-icon-bubble {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--color-bg-canvas, #faf8f5);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

.empty-headline {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-primary, #5C4E4E);
  margin: 0 0 4px;
}

.empty-subtext {
  font-size: 0.8rem;
  color: var(--color-text-muted, #8C7E7E);
  margin: 0;
}

/* Footer */
.popdown-footer {
  padding: 10px 20px;
  background: var(--color-bg-canvas, #faf8f5);
  border-top: 1px solid var(--color-border-subtle, #f2eee9);
  text-align: center;
}

.btn-footer-link {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-primary, #5C4E4E);
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 8px;
}

.btn-footer-link:hover {
  text-decoration: underline;
}

/* Skeleton Loading */
.popdown-loading {
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.skeleton-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.skeleton-avatar {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-md, 10px);
  background: #EAE6E2;
  animation: pulse 1.5s infinite ease-in-out;
}

.skeleton-lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.skeleton-line {
  height: 10px;
  border-radius: 4px;
  background: #EAE6E2;
  animation: pulse 1.5s infinite ease-in-out;
}

.line-short { width: 40%; }
.line-long { width: 85%; }

@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

/* Transition Animations */
.dropdown-fade-enter-active,
.dropdown-fade-leave-active {
  transition: opacity 0.18s ease, transform 0.18s ease;
}

.dropdown-fade-enter-from,
.dropdown-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px) scale(0.98);
}
</style>
