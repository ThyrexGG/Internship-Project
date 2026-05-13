<template>
  <div class="app-shell">

    <!-- Top Nav -->
    <header class="top-nav">
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
      <div class="avatar">
        <img src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=80&q=80" alt="User" />
      </div>
    </header>

    <div class="body">

      <!-- Sidebar -->
      <aside class="sidebar">
        <h1 class="sidebar-title">Landlord Panel</h1>

        <div class="search-box">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
          </svg>
          <input type="text" placeholder="Search" />
        </div>

        <nav class="sidebar-nav">
          <p class="nav-group-label">Profile</p>
          <button class="nav-item" :class="{ active: activePage === 'profile' }" @click="activePage = 'profile'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
            </svg>
            My Profile
          </button>
          <button class="nav-item" :class="{ active: activePage === 'notification' }" @click="activePage = 'notification'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/>
            </svg>
            Notification
          </button>

          <p class="nav-group-label">Main Menu</p>
          <button class="nav-item" :class="{ active: activePage === 'dashboard' }" @click="activePage = 'dashboard'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 3v18"/>
            </svg>
            Dashboard
          </button>
          <button class="nav-item" :class="{ active: activePage === 'rental' }" @click="activePage = 'rental'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/><path d="M9 21V12h6v9"/>
            </svg>
            Rental
          </button>
          <button class="nav-item" :class="{ active: activePage === 'leasing' }" @click="activePage = 'leasing'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.22 4.22l2.12 2.12M17.66 17.66l2.12 2.12M2 12h3M19 12h3M4.22 19.78l2.12-2.12M17.66 6.34l2.12-2.12"/>
            </svg>
            Leasing
          </button>

          <p class="nav-group-label">Account &amp; Help</p>
          <button class="nav-item" :class="{ active: activePage === 'help' }" @click="activePage = 'help'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>
            </svg>
            Help
          </button>
          <button class="nav-item" :class="{ active: activePage === 'security' }" @click="activePage = 'security'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            </svg>
            Security
          </button>
          <button class="nav-item" :class="{ active: activePage === 'account' }" @click="activePage = 'account'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
            </svg>
            Account status
          </button>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="main-content">

        <!-- Page Header -->
        <div class="page-header">
          <button class="back-btn" @click="$emit('go-back')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M19 12H5M12 5l-7 7 7 7"/>
            </svg>
          </button>
          <h2 class="page-title">Notification</h2>
        </div>

        <!-- Notification Card -->
        <div class="notif-card">

          <!-- Notif Header -->
          <div class="notif-header">
            <div class="notif-icon-wrap">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c0784a" stroke-width="2">
                <path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/>
                <path d="M9 21V12h6v9"/>
              </svg>
            </div>
            <div class="notif-header-text">
              <p class="notif-title">New Booking Request</p>
              <p class="notif-sub">Green Villa has a new reservation.</p>
            </div>
            <div class="notif-actions-top">
              <span class="notif-time">Apr 25, 2024, 12:03 AM</span>
              <button class="icon-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/>
                </svg>
              </button>
              <button class="icon-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="5" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="12" cy="19" r="1"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Booking Details -->
          <div class="booking-details">
            <img
              src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400&q=80"
              alt="Green Villa"
              class="property-thumb"
            />
            <div class="booking-info">
              <div class="info-row">
                <span class="info-label">Property:</span>
                <span class="info-value">Green Villa</span>
              </div>
              <div class="info-row">
                <span class="info-label">Tenant name:</span>
                <span class="info-value">Chlorinde</span>
              </div>
              <div class="info-row">
                <span class="info-label">Booking Date:</span>
                <span class="info-value">25 April 2024</span>
              </div>
              <div class="info-row">
                <span class="info-label">Contact:</span>
                <span class="info-value">+855 12 345 678</span>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="booking-actions">
            <button class="btn-action outline">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
              </svg>
              View Tenant Profile
            </button>
            <button class="btn-action outline confirm">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
                <polyline points="20 6 9 17 4 12"/>
              </svg>
              Confirm Booking
            </button>
            <button class="btn-action outline reject">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5">
                <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
              </svg>
              Reject Booking
            </button>
            <button class="btn-action outline icon-only">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>
              </svg>
            </button>
          </div>

        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const activePage = ref('notification')
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.app-shell {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  font-family: 'DM Sans', sans-serif;
  background: #fff;
  overflow: hidden;
}

/* ── TOP NAV ── */
.top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 28px;
  border-bottom: 1px solid #efefef;
  flex-shrink: 0;
  background: #fff;
  z-index: 10;
}

.logo { display: flex; align-items: center; gap: 9px; }

.logo-icon {
  width: 32px; height: 32px;
  background: #f5f0eb; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  color: #c0784a;
}

.logo-text { font-weight: 600; font-size: 0.9rem; color: #111; }

.avatar {
  width: 38px; height: 38px;
  border-radius: 50%; overflow: hidden;
  border: 2px solid #eee;
}
.avatar img { width: 100%; height: 100%; object-fit: cover; }

/* ── BODY ── */
.body {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* ── SIDEBAR ── */
.sidebar {
  width: 240px;
  flex-shrink: 0;
  border-right: 1px solid #efefef;
  padding: 28px 18px 24px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  overflow-y: auto;
  background: #fff;
}

.sidebar-title {
  font-family: 'DM Serif Display', serif;
  font-size: 1.55rem;
  font-weight: 400;
  color: #111;
  line-height: 1.2;
  padding: 0 4px;
}

.search-box {
  display: flex; align-items: center; gap: 8px;
  border: 1.5px solid #e8e8e8; border-radius: 50px;
  padding: 7px 14px; background: #fff;
}

.search-box input {
  border: none; outline: none;
  font-family: 'DM Sans', sans-serif; font-size: 0.8rem;
  color: #333; flex: 1; background: transparent;
}
.search-box input::placeholder { color: #bbb; }

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-group-label {
  font-size: 0.7rem;
  font-weight: 600;
  color: #bbb;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 10px 8px 4px;
}

.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 12px;
  border: none; border-radius: 10px;
  background: transparent;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem; font-weight: 500; color: #555;
  cursor: pointer; text-align: left;
  transition: background 0.18s, color 0.18s;
  width: 100%;
}
.nav-item:hover { background: #f7f7f7; color: #111; }
.nav-item.active { background: #f3ede8; color: #111; font-weight: 600; }
.nav-item svg { flex-shrink: 0; color: inherit; }

/* ── MAIN ── */
.main-content {
  flex: 1;
  padding: 32px 44px;
  overflow-y: auto;
  background: #fff;
}

/* Page header */
.page-header {
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 32px;
}

.back-btn {
  width: 36px; height: 36px;
  border: 1.5px solid #e0e0e0; border-radius: 50%;
  background: #fff; display: flex; align-items: center; justify-content: center;
  cursor: pointer; color: #333;
  transition: border-color 0.2s;
  flex-shrink: 0;
}
.back-btn:hover { border-color: #999; }

.page-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.3rem; font-weight: 600; color: #111;
}

/* ── NOTIFICATION CARD ── */
.notif-card {
  display: flex; flex-direction: column; gap: 28px;
}

/* Notif header row */
.notif-header {
  display: flex; align-items: flex-start; gap: 14px;
}

.notif-icon-wrap {
  width: 52px; height: 52px; flex-shrink: 0;
  background: #f3ede8; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
}

.notif-header-text { flex: 1; }

.notif-title { font-weight: 600; font-size: 0.95rem; color: #111; margin-bottom: 3px; }
.notif-sub { font-size: 0.8rem; color: #888; }

.notif-actions-top {
  display: flex; align-items: center; gap: 8px; flex-shrink: 0;
}

.notif-time { font-size: 0.75rem; color: #aaa; white-space: nowrap; }

.icon-btn {
  width: 32px; height: 32px;
  background: none; border: none;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; color: #888; border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}
.icon-btn:hover { background: #f5f5f5; color: #333; }

/* Booking details */
.booking-details {
  display: flex; gap: 28px; align-items: flex-start;
}

.property-thumb {
  width: 160px; height: 125px;
  border-radius: 12px; object-fit: cover; flex-shrink: 0;
}

.booking-info {
  display: flex; flex-direction: column; gap: 12px;
  padding-top: 4px;
}

.info-row {
  display: flex; gap: 12px; align-items: baseline;
}

.info-label {
  font-size: 0.83rem; color: #888; font-weight: 400;
  min-width: 110px; flex-shrink: 0;
}

.info-value {
  font-size: 0.83rem; color: #111; font-weight: 500;
}

/* Action buttons */
.booking-actions {
  display: flex; gap: 10px; align-items: center;
  flex-wrap: wrap;
}

.btn-action {
  display: flex; align-items: center; gap: 7px;
  padding: 10px 18px;
  border-radius: 10px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.82rem; font-weight: 500;
  cursor: pointer; transition: background 0.18s, border-color 0.18s;
  white-space: nowrap;
}

.btn-action.outline {
  background: #fff;
  border: 1.5px solid #e0e0e0;
  color: #222;
}
.btn-action.outline:hover { background: #f8f8f8; border-color: #bbb; }

.btn-action.confirm { color: #16a34a; }
.btn-action.confirm:hover { background: #f0fdf4; border-color: #86efac; }

.btn-action.reject { color: #dc2626; }
.btn-action.reject:hover { background: #fef2f2; border-color: #fca5a5; }

.btn-action.icon-only {
  padding: 10px 12px;
}
</style>
