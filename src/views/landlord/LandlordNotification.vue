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

    </header>

    <div class="body">

      <!-- Sidebar -->
      <aside class="sidebar">
        <h1 class="sidebar-title">Landlord Panel</h1>

        <div class="search-box">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
          </svg>
          <input type="text" placeholder="Search" v-model="sidebarSearchQuery" />
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
          <button class="nav-item nav-item-create" :class="{ active: activePage === 'create' }" @click="activePage = 'create'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 5v14M5 12h14"/>
            </svg>
            Create Listing
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

        <!-- CASE 1: PROFILE PAGE -->
        <div v-if="activePage === 'profile'" class="profile-tab-content">
          <!-- Page Header -->
          <div class="page-header">
            <h2 class="page-title">My Profile</h2>
          </div>
          
          <div class="profile-card-layout">
            <div class="profile-hero-mini">
              <div class="profile-avatar-wrapper-mini">
                <img :src="landlordProfile.avatar" alt="Avatar" />
              </div>
              <div class="profile-hero-info">
                <h3>{{ landlordProfile.firstName }} {{ landlordProfile.lastName }}</h3>
                <span class="badge-premium">{{ landlordProfile.tier }}</span>
              </div>
            </div>

            <h3 class="section-subtitle">Account Details</h3>
            <div class="profile-details-grid">
              <div class="profile-detail-item">
                <label>First Name</label>
                <input type="text" v-model="landlordProfile.firstName" class="profile-input" :disabled="!isEditingProfile" />
              </div>
              <div class="profile-detail-item">
                <label>Last Name</label>
                <input type="text" v-model="landlordProfile.lastName" class="profile-input" :disabled="!isEditingProfile" />
              </div>
              <div class="profile-detail-item">
                <label>Email</label>
                <input type="email" v-model="landlordProfile.email" class="profile-input" :disabled="!isEditingProfile" />
              </div>
              <div class="profile-detail-item">
                <label>Phone Number</label>
                <input type="text" v-model="landlordProfile.phone" class="profile-input" :disabled="!isEditingProfile" />
              </div>
              <div class="profile-detail-item">
                <label>Office Address</label>
                <input type="text" v-model="landlordProfile.address" class="profile-input" :disabled="!isEditingProfile" />
              </div>
              <div class="profile-detail-item">
                <label>Business License</label>
                <input type="text" v-model="landlordProfile.license" class="profile-input" :disabled="!isEditingProfile" />
              </div>
            </div>
            <div class="profile-actions-row">
              <button v-if="!isEditingProfile" class="btn-save-profile" @click="isEditingProfile = true">Edit Profile</button>
              <template v-else>
                <button class="btn-save-profile" style="background: #5C4E4E;" @click="saveProfileInfo">Save Profile</button>
                <button class="btn-save-profile outline" style="background: transparent; color: #5C4E4E; border: 1.5px solid #e0e0e0;" @click="isEditingProfile = false">Cancel</button>
              </template>
            </div>
          </div>
        </div>

        <!-- CASE 2: NOTIFICATION PAGE -->
        <div v-else-if="activePage === 'notification'">
          <!-- Page Header -->
          <div class="page-header">
            <button class="back-btn" @click="handleBack">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 12H5M12 5l-7 7 7 7"/>
              </svg>
            </button>
            <h2 class="page-title">{{ selectedNotif ? (selectedNotif === 'booking-1' ? 'New Booking Request' : 'Payment Details') : 'Notification' }}</h2>
          </div>

          <!-- Tabs (mockup style) -->
          <div class="notif-tabs" v-if="!selectedNotif">
            <button 
              v-for="tab in tabs" 
              :key="tab.id" 
              class="notif-tab-btn" 
              :class="{ active: activeNotifTab === tab.id }" 
              @click="activeNotifTab = tab.id"
            >
              {{ tab.name }}
            </button>
          </div>

          <!-- Notification List (mockup style) -->
          <div class="notif-list-container" v-if="!selectedNotif">
            <!-- Today Group -->
            <div class="notif-date-group" v-if="todayNotifications.length > 0">
              <h3 class="date-group-title">Today</h3>
              
              <div 
                v-for="notif in todayNotifications" 
                :key="notif.id" 
                class="notif-item-row" 
                @click="selectNotification(notif.id)"
              >
                <div class="notif-item-left">
                  <div v-if="notif.type === 'booking'" class="notif-badge-logo">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M4 18 L16 18" />
                      <path d="M4 18 L4 12 L9 7 L16 14" />
                      <path d="M12 18 L12 4 L16 4 L16 18 Z" />
                      <path d="M12 14 L16 14" />
                    </svg>
                  </div>
                  <div v-else-if="notif.type === 'payment'" class="notif-badge-logo" style="color: #5C4E4E; background: #D1D0D0;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="5" width="20" height="14" rx="2" ry="2"></rect>
                      <line x1="2" y1="10" x2="22" y2="10"></line>
                    </svg>
                  </div>
                  <div v-else class="notif-badge-circle"></div>
                  <div class="notif-item-copy">
                    <span class="notif-item-title">{{ notif.title }}</span>
                    <span class="notif-item-desc">{{ notif.desc }}</span>
                  </div>
                </div>
                <div class="notif-item-right">
                  <span class="notif-item-time">{{ notif.time }}</span>
                  <span v-if="notif.unread" class="unread-dot-green"></span>
                </div>
              </div>
            </div>

            <!-- Yesterday Group -->
            <div class="notif-date-group" v-if="yesterdayNotifications.length > 0">
              <h3 class="date-group-title">Yesterday</h3>

              <div 
                v-for="notif in yesterdayNotifications" 
                :key="notif.id" 
                class="notif-item-row" 
                @click="selectNotification(notif.id)"
              >
                <div class="notif-item-left">
                  <div v-if="notif.type === 'booking'" class="notif-badge-logo">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M4 18 L16 18" />
                      <path d="M4 18 L4 12 L9 7 L16 14" />
                      <path d="M12 18 L12 4 L16 4 L16 18 Z" />
                      <path d="M12 14 L16 14" />
                    </svg>
                  </div>
                  <div v-else-if="notif.type === 'payment'" class="notif-badge-logo" style="color: #5C4E4E; background: #D1D0D0;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="5" width="20" height="14" rx="2" ry="2"></rect>
                      <line x1="2" y1="10" x2="22" y2="10"></line>
                    </svg>
                  </div>
                  <div v-else class="notif-badge-circle"></div>
                  <div class="notif-item-copy">
                    <span class="notif-item-title">{{ notif.title }}</span>
                    <span class="notif-item-desc">{{ notif.desc }}</span>
                  </div>
                </div>
                <div class="notif-item-right">
                  <span class="notif-item-time">{{ notif.time }}</span>
                  <span v-if="notif.unread" class="unread-dot-green"></span>
                </div>
              </div>
            </div>

            <!-- Empty State -->
            <div v-if="filteredNotifications.length === 0" style="text-align: center; padding: 40px; color: #888; font-size: 0.9rem;">
              No notifications matching current tab or search filters.
            </div>
          </div>

          <!-- Notification Card Detail View -->
          <div class="notif-card" v-else-if="selectedNotif === 'booking-1'">
            <!-- Notif Header -->
            <div class="notif-header">
              <div class="notif-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#5C4E4E" stroke-width="2">
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
                <button class="icon-btn" @click="viewTenantProfile">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/>
                  </svg>
                </button>
                <button class="icon-btn" @click="openChatWithTenant">
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
                  <span class="info-label">Booking Status:</span>
                  <span class="info-value" style="text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;" :style="{ color: bookingStatus === 'confirmed' ? '#22c55e' : (bookingStatus === 'rejected' ? '#ef4444' : '#5C4E4E') }">
                    {{ bookingStatus }}
                  </span>
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
              <button class="btn-action outline" @click="viewTenantProfile">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
                </svg>
                View Tenant Profile
              </button>
              <button class="btn-action outline confirm" @click="confirmBooking" :disabled="bookingStatus !== 'pending'">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5C4E4E" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"/>
                </svg>
                {{ bookingStatus === 'confirmed' ? 'Confirmed' : 'Confirm Booking' }}
              </button>
              <button class="btn-action outline reject" @click="rejectBooking" :disabled="bookingStatus !== 'pending'">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5">
                  <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
                </svg>
                {{ bookingStatus === 'rejected' ? 'Rejected' : 'Reject Booking' }}
              </button>
              <button class="btn-action outline icon-only" @click="openChatWithTenant">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Generic Detail View for Payment Notification -->
          <div class="notif-card" v-else-if="selectedNotif">
            <div class="notif-header">
              <div class="notif-badge-circle" style="width: 52px; height: 52px; display: flex; align-items: center; justify-content: center; background: #fff; border: 1.5px solid #efefef; border-radius: 50%;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
                  <rect x="2" y="4" width="20" height="16" rx="2"/><path d="M12 2v20M2 12h20"/>
                </svg>
              </div>
              <div class="notif-header-text">
                <p class="notif-title">{{ currentNotification?.title || 'Notification' }}</p>
                <p class="notif-sub">{{ currentNotification?.desc }}</p>
              </div>
              <div class="notif-actions-top">
                <span class="notif-time">{{ currentNotification?.date }}, {{ currentNotification?.time }}</span>
              </div>
            </div>
            <div v-if="currentNotification?.type === 'payment'" class="receipt-card" id="receipt-pdf-target">
              <div class="receipt-header">
                <h3>Payment Receipt</h3>
                <span class="status-badge success">Paid</span>
              </div>
              <div class="receipt-body">
                <div class="receipt-row">
                  <span>Transaction ID</span>
                  <strong>#TXN-{{ Math.floor(Math.random() * 900000) + 100000 }}</strong>
                </div>
                <div class="receipt-row">
                  <span>Payment Date</span>
                  <strong>{{ currentNotification?.date }}, {{ currentNotification?.time }}</strong>
                </div>
                <div class="receipt-row">
                  <span>Room / Property</span>
                  <strong>{{ currentNotification?.roomName || 'Room 201' }}</strong>
                </div>
                <div class="receipt-row">
                  <span>Payment Method</span>
                  <strong>Bank Transfer</strong>
                </div>
                <div class="receipt-divider"></div>
                <div class="receipt-row">
                  <span>Rent Amount</span>
                  <strong>{{ currentNotification?.amount || '$350' }}</strong>
                </div>
                <div class="receipt-row">
                  <span>Service Fee</span>
                  <strong>$0.00</strong>
                </div>
                <div class="receipt-divider"></div>
                <div class="receipt-row total">
                  <span>Total Paid</span>
                  <strong style="color: #5C4E4E;">{{ currentNotification?.amount || '$350' }}</strong>
                </div>
              </div>
              <button class="btn-dark download-btn" @click="downloadReceipt" style="margin-top: 24px; width: 100%; display: flex; justify-content: center; gap: 8px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                Download PDF Receipt
              </button>
            </div>
            <div v-else class="booking-details" style="padding: 24px; border: 1.5px solid #efefef; border-radius: 12px; background: #e0e0e0; width: 100%;">
              <p style="font-size: 0.9rem; color: #333; line-height: 1.6; margin: 0;">
                {{ currentNotification?.desc }}
              </p>
            </div>
            <div class="booking-actions">
              <button class="btn-action outline" @click="selectedNotif = null">Go Back</button>
            </div>
          </div>
        </div>

        <!-- CASE 3: DASHBOARD PAGE -->
        <div v-else-if="activePage === 'dashboard'" class="dashboard-tab-content">
          <!-- Page Header -->
          <div class="dashboard-header-row">
            <h2 class="page-title">Dashboard</h2>
            <div style="position: relative;">
              <div class="date-picker-btn" @click="showMonthPicker = !showMonthPicker">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                <span>{{ selectedMonth }}</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" :style="{ transform: showMonthPicker ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }">
                  <polyline points="6 9 12 15 18 9"/>
                </svg>
              </div>

              <!-- Month Picker Dropdown -->
              <div v-if="showMonthPicker" class="month-picker-dropdown">
                <div 
                  v-for="m in Object.keys(monthlyData)" 
                  :key="m" 
                  class="month-picker-item" 
                  :class="{ active: selectedMonth === m }"
                  @click="selectedMonth = m; showMonthPicker = false"
                >
                  {{ m }}
                </div>
              </div>
            </div>
          </div>

          <!-- Donut Summary Card -->
          <div class="donut-summary-card">
            <div class="donut-left-col">
              <span class="amount-collected-red">$ {{ currentMonthStats.collectedRed.toLocaleString() }}</span>
              <span class="amount-label">COLLECTED</span>
            </div>

            <div class="donut-center-col">
              <div class="donut-chart-container">
                <svg class="donut-svg" viewBox="0 0 36 36">
                  <path class="donut-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#D1D0D0" stroke-width="3"></path>
                  <path class="donut-segment" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#5C4E4E" stroke-width="3" :stroke-dasharray="`${donutOffset} ${100 - donutOffset}`" stroke-dashoffset="25"></path>
                </svg>
                <div class="donut-inner-text">
                  <span class="donut-month">{{ selectedMonth.split(' ')[0] }}</span>
                  <span class="donut-total">$ {{ dashboardTotal.toLocaleString() }}</span>
                  <span class="donut-sublabel">Total</span>
                </div>
              </div>
            </div>

            <div class="donut-right-col">
              <span class="amount-collected-blue">$ {{ currentMonthStats.collectedBlue.toLocaleString() }}</span>
              <span class="amount-label">COLLECTED</span>
            </div>

            <!-- Footer Stats row inside card -->
            <div class="donut-card-footer">
              <div class="footer-stat-group">
                <div class="stat-col">
                  <span class="stat-label">Occupied</span>
                  <span class="stat-value">{{ currentMonthStats.occupied }}</span>
                </div>
                <div class="stat-col">
                  <span class="stat-label">Vacant</span>
                  <span class="stat-value">{{ currentMonthStats.vacant }}</span>
                </div>
              </div>
              <div class="footer-stat-group">
                <div class="stat-col">
                  <span class="stat-label">Properties</span>
                  <span class="stat-value">{{ rentalProperties.length }}</span>
                </div>
                <div class="stat-col">
                  <span class="stat-label">Tenants</span>
                  <span class="stat-value">{{ currentMonthStats.tenants }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- KPI Cards Row -->
          <div class="kpi-grid">
            <div class="kpi-card">
              <div class="kpi-icon-wrapper kpi-properties">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/><polyline points="9 22 9 12 15 12 15 22"/>
                </svg>
              </div>
              <div class="kpi-copy">
                <span class="kpi-title">Total Properties</span>
                <span class="kpi-value">{{ rentalProperties.length }}</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrapper kpi-revenue">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <div class="kpi-copy">
                <span class="kpi-title">Monthly Revenue</span>
                <span class="kpi-value">{{ currentMonthStats.revenue }}</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrapper kpi-tenants">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
              </div>
              <div class="kpi-copy">
                <span class="kpi-title">Active Tenants</span>
                <span class="kpi-value">{{ currentMonthStats.tenants }}</span>
              </div>
            </div>

            <div class="kpi-card">
              <div class="kpi-icon-wrapper kpi-maintenance">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                </svg>
              </div>
              <div class="kpi-copy">
                <span class="kpi-title">Maintenance Requests</span>
                <span class="kpi-value">{{ currentMonthStats.maintenance }}</span>
              </div>
            </div>
          </div>

          <!-- Bottom Grid Row (Tables) -->
          <div class="dashboard-tables-row">
            <!-- Properties Overview Table -->
            <div class="table-card">
              <h3 class="table-card-title">Properties Overview</h3>
              <table class="dashboard-table">
                <thead>
                  <tr>
                    <th>Properties</th>
                    <th>Tenant</th>
                    <th>Status</th>
                    <th>Income</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(p, i) in dashboardProperties" :key="i">
                    <td>{{ p.name }}</td>
                    <td>{{ p.tenants }}</td>
                    <td><span class="badge-status-occupied">{{ p.status }}</span></td>
                    <td class="income-value-cell">{{ p.income }}</td>
                  </tr>
                </tbody>
              </table>
              <button class="table-action-link-btn" @click="activePage = 'rental'">View All Properties &gt;</button>
            </div>

            <!-- Recent Payments Table -->
            <div class="table-card">
              <h3 class="table-card-title">Recent Payments</h3>
              <table class="dashboard-table">
                <thead>
                  <tr>
                    <th>Tenant</th>
                    <th>Property</th>
                    <th>Date</th>
                    <th>Amount</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(p, i) in currentMonthStats.recentPayments" :key="i">
                    <td>{{ p.tenant }}</td>
                    <td>{{ p.property }}</td>
                    <td>{{ p.date }}</td>
                    <td class="income-value-cell green">{{ p.amount }}</td>
                  </tr>
                </tbody>
              </table>
              <button class="table-action-link-btn" @click="activePage = 'leasing'">View All Payments &gt;</button>
            </div>
          </div>
        </div>

        <!-- CASE 4: RENTAL PAGE -->
        <div v-else-if="activePage === 'rental'" class="rental-tab-content">
          <!-- Page Header -->
          <div class="page-header">
            <h2 class="page-title">Rental</h2>
          </div>

          <!-- Search & Create Row -->
          <div class="rental-search-row">
            <div class="rental-search-box">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
              </svg>
              <input type="text" placeholder="Search properties..." v-model="rentalSearchQuery" />
            </div>
          </div>

          <!-- Properties section -->
          <div class="properties-section-rental">
            <h3 class="properties-title">Properties</h3>
            
            <div class="rental-properties-grid">
              <div 
                v-for="(prop, index) in filteredRentalProperties" 
                :key="index" 
                class="rental-property-card"
                @click="$router.push('/property/' + (prop.id || 1) + '?from=landlord-rental')"
              >
                <img :src="prop.image || (prop.images && prop.images[0])" alt="Property image" class="rental-card-img" loading="lazy" />
                <div class="rental-card-overlay"></div>
                <span class="rental-card-label">{{ prop.name }}</span>
                <button class="btn-delete-property" @click.stop="deleteProperty(prop.id)">&times;</button>
              </div>
            </div>
          </div>
        </div>

        <!-- CASE 5: LEASING PAGE -->
        <div v-else-if="activePage === 'leasing'" class="leasing-tab-content">
          <!-- Page Header -->
          <div class="page-header">
            <h2 class="page-title">Lease Status</h2>
          </div>

          <!-- Lease Search Box -->
          <div class="rental-search-row">
            <div class="rental-search-box">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
              </svg>
              <input type="text" placeholder="Search leases by tenant or place..." v-model="leaseSearchQuery" />
            </div>
          </div>

          <div class="lease-table-card">
            <table class="lease-table">
              <thead>
                <tr>
                  <th>No.</th>
                  <th>Tenant</th>
                  <th>Unit</th>
                  <th>Start date</th>
                  <th>End date</th>
                  <th>Place</th>
                  <th>Status</th>
                  <th>Image</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(lease, index) in filteredLeases" :key="index">
                  <td class="gray-code">{{ lease.id }}</td>
                  <td>{{ lease.tenant }}</td>
                  <td>{{ lease.unit }}</td>
                  <td>{{ lease.start }}</td>
                  <td>{{ lease.end }}</td>
                  <td>{{ lease.place }}</td>
                  <td><span class="badge-expired">{{ lease.status }}</span></td>
                  <td>
                    <div class="lease-thumb-wrapper">
                      <img :src="lease.image" alt="Thumbnail" />
                    </div>
                  </td>
                </tr>
                <tr v-if="filteredLeases.length === 0">
                  <td colspan="8" style="text-align: center; color: #888; padding: 24px;">No leases matched your search.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- CASE 6: CREATE LISTING PAGE -->
        <div v-else-if="activePage === 'create'" class="create-tab-content">
          <div class="page-header">
            <h2 class="page-title">Create New Rental Listing</h2>
          </div>
          <div class="create-layout">
            <div class="create-left">
              <!-- Image Upload Area -->
              <div class="image-upload-area" :class="{ 'has-image': newListingImages.length > 0 }">
                <div v-if="newListingImages.length > 0" class="image-grid">
                  <div v-for="(img, idx) in newListingImages" :key="idx" class="image-preview">
                    <img :src="img" alt="Preview" />
                    <button class="btn-remove-image" @click="newListingImages.splice(idx, 1); newListingFiles.splice(idx, 1)">&times;</button>
                  </div>
                  <label class="add-more-card">
                    <input type="file" accept="image/*" multiple @change="handleRealUpload" style="display: none;" />
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                    <span>Add More</span>
                  </label>
                </div>
                <div v-else class="image-placeholder">
                  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="1.5">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <circle cx="8.5" cy="8.5" r="1.5"></circle>
                    <polyline points="21 15 16 10 5 21"></polyline>
                  </svg>
                  <p>Drag and drop photos or</p>
                  <p style="font-size: 0.8rem; color: #777; margin-top: 4px;">(Min 3 images, at least 600x400. Large photos will be auto-optimized)</p>
                  <label class="btn-dark" style="margin-top: 12px; cursor: pointer; background: #5C4E4E; color: white; padding: 10px 24px; border-radius: 8px; font-weight: 600; font-size: 0.9rem; display: inline-block; text-align: center;">
                    <input type="file" accept="image/*" multiple @change="handleRealUpload" style="display: none;" />
                    Upload from Device
                  </label>
                </div>
              </div>
            </div>
            
            <div class="create-right">
              <!-- Basic Info -->
              <div class="form-section">
                <h3 class="section-title">Basic Info</h3>
                <div class="form-group full-width">
                  <label>Property Name (Title)</label>
                  <input type="text" v-model="newListingName" class="form-input" placeholder="e.g. Green Village Suite" />
                </div>
                <div class="form-row">
                  <div class="form-group">
                    <label>Property Type</label>
                    <select v-model="newListingType" class="form-input">
                      <option value="Apartment">Apartment</option>
                      <option value="House">House</option>
                      <option value="Condo">Condo</option>
                      <option value="Studio">Studio</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label>Lease Period</label>
                    <select v-model="newListingPeriod" class="form-input">
                      <option value="Long-term">Long-term (1 yr+)</option>
                      <option value="Short-term">Short-term (Month-to-month)</option>
                    </select>
                  </div>
                </div>
                <div class="form-group full-width">
                  <label>Full Address / Location</label>
                  <input type="text" v-model="newListingLocation" class="form-input" placeholder="e.g. Sen Sok, Phnom Penh" />
                </div>
              </div>

              <!-- Details -->
              <div class="form-section">
                <h3 class="section-title">Details & Pricing</h3>
                <div class="form-row">
                  <div class="form-group">
                    <label>Price ($/mo)</label>
                    <input type="number" v-model="newListingPrice" class="form-input" min="0" />
                  </div>
                  <div class="form-group">
                    <label>Square Footage (sqft)</label>
                    <input type="number" v-model="newListingSqft" class="form-input" min="0" />
                  </div>
                </div>
                <div class="form-row three-cols">
                  <div class="form-group">
                    <label>Bedrooms</label>
                    <input type="number" v-model="newListingBedrooms" class="form-input" min="0" />
                  </div>
                  <div class="form-group">
                    <label>Beds</label>
                    <input type="number" v-model="newListingBeds" class="form-input" min="0" />
                  </div>
                  <div class="form-group">
                    <label>Baths</label>
                    <input type="number" v-model="newListingBaths" class="form-input" min="0" step="0.5" />
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group">
                    <label>Max Occupancy (Pax)</label>
                    <input type="text" v-model="newListingPax" class="form-input" placeholder="e.g. 2/4" />
                  </div>
                </div>
              </div>

              <!-- Description -->
              <div class="form-section">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                  <h3 class="section-title" style="margin-bottom: 0;">Description <span style="color: red; font-size: 0.9rem;">*</span></h3>
                  <button class="btn-ai-generate" @click="generateAIDescription" :disabled="isGeneratingAI">
                    <svg v-if="!isGeneratingAI" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 6px;">
                      <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path>
                    </svg>
                    <svg v-else class="spin-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 6px;">
                      <line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line>
                    </svg>
                    {{ isGeneratingAI ? 'Thinking...' : '✨ Auto-Generate' }}
                  </button>
                </div>
                <div class="form-group full-width">
                  <textarea v-model="newListingDescription" class="form-input" rows="4" placeholder="Describe the property highlights..."></textarea>
                </div>
              </div>

              <!-- Amenities -->
              <div class="form-section">
                <h3 class="section-title">Amenities</h3>
                <div class="amenities-pills">
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('wifi') }">
                    <input type="checkbox" v-model="newListingAmenities" value="wifi" style="display: none;" />
                    WiFi
                  </label>
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('ac') }">
                    <input type="checkbox" v-model="newListingAmenities" value="ac" style="display: none;" />
                    Air Conditioning
                  </label>
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('kitchen') }">
                    <input type="checkbox" v-model="newListingAmenities" value="kitchen" style="display: none;" />
                    Kitchen
                  </label>
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('parking') }">
                    <input type="checkbox" v-model="newListingAmenities" value="parking" style="display: none;" />
                    Parking
                  </label>
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('gym') }">
                    <input type="checkbox" v-model="newListingAmenities" value="gym" style="display: none;" />
                    Gym
                  </label>
                  <label class="amenity-pill" :class="{ selected: newListingAmenities.includes('pool') }">
                    <input type="checkbox" v-model="newListingAmenities" value="pool" style="display: none;" />
                    Swimming Pool
                  </label>
                </div>
              </div>

              <!-- Contact Details -->
              <div class="form-section">
                <h3 class="section-title">Contact Details</h3>
                <div class="form-group full-width">
                  <label>Contact Name / Entity</label>
                  <input type="text" v-model="newListingContactName" class="form-input" placeholder="e.g. Skystar Condo Cambodia" />
                </div>
                <div class="form-row">
                  <div class="form-group">
                    <label>Phone Number(s)</label>
                    <input type="text" v-model="newListingContactPhone" class="form-input" placeholder="e.g. 081 743 949" />
                  </div>
                  <div class="form-group">
                    <label>Social / Telegram Handle</label>
                    <input type="text" v-model="newListingContactSocial" class="form-input" placeholder="e.g. @skystar_condo" />
                  </div>
                </div>
              </div>

              <!-- Action Area -->
              <div class="create-action-area">
                <button class="btn-publish" @click="publishListing" :disabled="!isFormValid || isPublishing" :title="!isFormValid ? 'Please fill out all required fields and upload at least 3 images' : ''">
                  {{ isPublishing ? 'Publishing...' : 'Publish Listing' }}
                </button>
              </div>

            </div>
          </div>
        </div>

        <!-- CASE 7: HELP PAGE -->
        <div v-else-if="activePage === 'help'" class="help-tab-content">
          <div class="page-header">
            <h2 class="page-title">Help &amp; FAQs</h2>
          </div>

          <!-- FAQ Search Box -->
          <div class="rental-search-row" style="margin-bottom: 16px;">
            <div class="rental-search-box" style="max-width: 100%;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                <circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>
              </svg>
              <input type="text" placeholder="Search FAQs..." v-model="faqSearchQuery" />
            </div>
          </div>

          <div class="faq-list">
            <div v-for="(faq, index) in filteredFaqs" :key="index" class="faq-item" :class="{ open: faq.open }">
              <button class="faq-question" @click="faq.open = !faq.open">
                <span>{{ faq.question }}</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="faq-arrow-svg">
                  <polyline points="6 9 12 15 18 9"/>
                </svg>
              </button>
              <div class="faq-answer" v-if="faq.open">
                <p>{{ faq.answer }}</p>
              </div>
            </div>
            <div v-if="filteredFaqs.length === 0" style="text-align: center; padding: 24px; color: #888;">
              No FAQs matched your search terms.
            </div>
          </div>
        </div>

        <!-- CASE 7: SECURITY PAGE -->
        <div v-else-if="activePage === 'security'" class="security-tab-content">
          <div class="page-header">
            <h2 class="page-title">Security &amp; Password</h2>
          </div>

          <div class="security-card">
            <div class="security-row">
              <div class="security-text-col">
                <h3>Two-Factor Authentication</h3>
                <p>Add an extra layer of security to your landlord account.</p>
              </div>
              <label class="toggle-switch">
                <input type="checkbox" v-model="enable2FA" />
                <span class="toggle-slider"></span>
              </label>
            </div>

            <div class="security-row">
              <div class="security-text-col">
                <h3>Change Portal PIN</h3>
                <p>Required when confirming bank details and payouts.</p>
              </div>
              <div class="security-pin-input-group">
                <input type="password" v-model="currentPin" disabled class="profile-input" style="width: 80px; letter-spacing: 0.2em; text-align: center;" />
                <button class="btn-change-pin" @click="changePin">Change</button>
              </div>
            </div>
          </div>
        </div>

        <!-- CASE 8: ACCOUNT STATUS PAGE -->
        <div v-else-if="activePage === 'account'" class="account-tab-content">
          <div class="page-header">
            <h2 class="page-title">Account Status</h2>
          </div>

          <div class="account-status-card">
            <div class="account-status-header">
              <div class="status-badge-wrapper">
                <span class="status-dot"></span>
                <span>Active Premium account</span>
              </div>
              <span class="status-valid-date">Renews: 12 Dec 2026</span>
            </div>

            <div class="account-usage-stats">
              <div class="usage-stat-item">
                <div class="usage-stat-header">
                  <span>Listings Usage</span>
                  <span>4 / 50 active listings</span>
                </div>
                <div class="usage-progress-bar">
                  <div class="usage-progress-fill" style="width: 8%;"></div>
                </div>
              </div>

              <div class="usage-stat-item" style="margin-top: 20px;">
                <div class="usage-stat-header">
                  <span>Tenant Applications Limit</span>
                  <span>100 / 1000 per month</span>
                </div>
                <div class="usage-progress-bar">
                  <div class="usage-progress-fill" style="width: 10%;"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </main>
    </div>
  </div>

  

  <!-- Tenant Profile Modal -->
  <transition name="modal-fade">
    <div v-if="showTenantProfileModal" class="chat-modal-overlay" @click.self="showTenantProfileModal = false">
      <div class="chat-modal-box">
        <header class="chat-modal-header">
          <h3 style="font-weight: 700; color: #5C4E4E; margin: 0;">Tenant Screening Profile</h3>
          <button class="chat-close-btn" @click="showTenantProfileModal = false">&times;</button>
        </header>
        <div class="chat-modal-body" style="text-align: center;">
          <div style="width: 80px; height: 80px; border-radius: 50%; overflow: hidden; margin: 0 auto 16px auto; border: 2px solid #efede8;">
            <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80" alt="Chlorinde Avatar" style="width: 100%; height: 100%; object-fit: cover;" />
          </div>
          <h3 style="font-weight: 700; color: #5C4E4E; margin-bottom: 4px;">Chlorinde</h3>
          <p style="font-size: 0.8rem; color: #888; margin-bottom: 20px;">Safety Security Inspector • Tenant Rating 4.9 ★</p>

          <div class="info-list-container" style="text-align: left; padding: 16px; margin-bottom: 0;">
            <div class="info-row" style="margin-bottom: 8px; display: flex; justify-content: space-between; font-size: 0.8rem;">
              <span class="info-label" style="color: #666; font-weight: 500;">Phone Number:</span>
              <span class="info-value" style="font-weight: 600;">+855 12 345 678</span>
            </div>
            <div class="info-row" style="margin-bottom: 8px; display: flex; justify-content: space-between; font-size: 0.8rem;">
              <span class="info-label" style="color: #666; font-weight: 500;">Email Address:</span>
              <span class="info-value" style="font-weight: 600;">chlorinde.insp@clor.gov</span>
            </div>
            <div class="info-row" style="margin-bottom: 8px; display: flex; justify-content: space-between; font-size: 0.8rem;">
              <span class="info-label" style="color: #666; font-weight: 500;">Identity Check:</span>
              <span class="info-value" style="color: #5C4E4E; font-weight: 600;">✓ Verified</span>
            </div>
            <div class="info-row" style="margin-bottom: 8px; display: flex; justify-content: space-between; font-size: 0.8rem;">
              <span class="info-label" style="color: #666; font-weight: 500;">Credit Background:</span>
              <span class="info-value" style="color: #5C4E4E; font-weight: 600;">✓ Excellent (98%)</span>
            </div>
            <div class="info-row" style="display: flex; justify-content: space-between; font-size: 0.8rem;">
              <span class="info-label" style="color: #666; font-weight: 500;">Reference check:</span>
              <span class="info-value" style="color: #5C4E4E; font-weight: 600;">✓ Highly Recommended</span>
            </div>
          </div>
        </div>
        <footer class="chat-modal-footer" style="display: flex; gap: 12px;">
          <button class="chat-cancel-btn" style="flex: 1;" @click="showTenantProfileModal = false">Close</button>
          <button class="chat-send-btn" style="flex: 1; background: #5C4E4E;" @click="goToFullProfile">View Full Profile</button>
        </footer>
      </div>
    </div>
  </transition>

  <!-- Reply / Message Modal -->
  <transition name="modal-fade">
    <div v-if="showReplyTenantModal" class="chat-modal-overlay" @click.self="showReplyTenantModal = false">
      <div class="chat-modal-box">
        <header class="chat-modal-header">
          <h3 style="font-weight: 700; color: #5C4E4E; margin: 0;">Direct Message to Chlorinde</h3>
          <button class="chat-close-btn" @click="showReplyTenantModal = false">&times;</button>
        </header>
        <div class="chat-modal-body">
          <label class="chat-label">Type your response:</label>
          <textarea 
            v-model="replyMessageText" 
            class="chat-textarea" 
            placeholder="Hi Chlorinde, I received your request..."
            rows="5"
          ></textarea>
        </div>
        <footer class="chat-modal-footer">
          <button class="chat-cancel-btn" @click="showReplyTenantModal = false">Cancel</button>
          <button class="chat-send-btn" @click="sendTenantMessage" :disabled="!replyMessageText.trim()">Send Message</button>
        </footer>
      </div>
    </div>
  </transition>
  <!-- Delete Confirmation Modal -->
  <transition name="modal-fade">
    <div v-if="showDeleteConfirmModal" class="chat-modal-overlay" @click.self="cancelDeleteProperty">
      <div class="delete-confirm-modal-box">
        <div class="delete-confirm-icon">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#FF4D4D" stroke-width="2"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
        </div>
        <h3 class="delete-confirm-title">Delete Listing</h3>
        <p class="delete-confirm-text">
          Are you sure you want to permanently delete this listing?
          <br><br>
          <span class="delete-confirm-subtext">This action cannot be undone. All property details, photos, and associated data will be removed from your dashboard and the public feed.</span>
        </p>
        <div class="delete-confirm-actions">
          <button class="btn-cancel-delete" @click="cancelDeleteProperty">Cancel</button>
          <button class="btn-confirm-delete" @click="confirmDeleteProperty">Delete</button>
        </div>
      </div>
    </div>
  </transition>

  <!-- Success Toast -->
  <transition name="toast-fade">
    <div v-if="showSuccessToast" class="chat-success-toast">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="toast-check-icon">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
      <span>{{ successToastMessage }}</span>
    </div>
  </transition>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { properties } from '../../store.js'
import html2pdf from 'html2pdf.js'
import { db, storage, auth } from '../../firebase.js'
import { collection, addDoc, serverTimestamp, doc, deleteDoc, getDocs } from 'firebase/firestore'
import { ref as storageRef, uploadBytes, getDownloadURL } from 'firebase/storage'

const route = useRoute()
const router = useRouter()
const activePage = ref(route.query.tab || 'dashboard')

onMounted(async () => {
  try {
    const querySnapshot = await getDocs(collection(db, 'properties'))
    const fetchedProperties = []
    querySnapshot.forEach((doc) => {
      const data = doc.data()
      if (!data.images || data.images.length === 0) {
        data.images = ['https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80']
        data.image = data.images[0]
      }
      fetchedProperties.push({ id: doc.id, ...data })
    })
    fetchedProperties.sort((a, b) => {
      if (a.createdAt && b.createdAt) {
        return b.createdAt.toMillis() - a.createdAt.toMillis()
      }
      return 0
    })
    const demoProperties = properties.value.filter(p => typeof p.id === 'number')
    if (!querySnapshot.empty) {
      properties.value = [...fetchedProperties, ...demoProperties]
    } else {
      properties.value = [...demoProperties]
    }
  } catch (e) {
    console.error("Error fetching properties in Dashboard: ", e)
  }
})
const selectedNotif = ref(null)
const activeNotifTab = ref('main')

const tabs = [
  { id: 'main', name: 'Main Notification' },
  { id: 'booking', name: 'Booking Request' },
  { id: 'property', name: 'Property Alerts' },
  { id: 'system', name: 'System Notification' }
]

function selectNotification(id) {
  selectedNotif.value = id
  const notif = notifications.value.find(n => n.id === id)
  if (notif) notif.unread = false
}

function handleBack() {
  if (selectedNotif.value) {
    selectedNotif.value = null
  } else {
    router.push('/home')
  }
}

// Search Inputs
const rentalSearchQuery = ref('')
const leaseSearchQuery = ref('')
const faqSearchQuery = ref('')
const sidebarSearchQuery = ref('')

// Notification List with unread markers
const notifications = ref([
  { id: 'booking-1', type: 'booking', title: 'New Booking Request', desc: 'New user Alice has requested to book Sunrise Apartments, room 105.', time: '13:01', group: 'Today', unread: true, date: 'Apr 25, 2024', roomName: 'Sunrise Apartments, Room 105', amount: '$400' },
  { id: 'payment-1', type: 'payment', title: 'Payment', desc: 'Green Ville, room 201 has completed their payment!', time: '13:01', group: 'Today', unread: true, date: 'Apr 25, 2024', roomName: 'Green Ville, Room 201', amount: '$350' },
  { id: 'payment-2', type: 'payment', title: 'Payment', desc: 'Blue Horizon, room 304 has completed their payment!', time: '11:45', group: 'Today', unread: false, date: 'Apr 25, 2024', roomName: 'Blue Horizon, Room 304', amount: '$420' },
  { id: 'payment-3', type: 'payment', title: 'Payment', desc: 'Maple Residency, room 112 has completed their payment!', time: '09:30', group: 'Today', unread: false, date: 'Apr 25, 2024', roomName: 'Maple Residency, Room 112', amount: '$310' },
  { id: 'payment-4', type: 'payment', title: 'Payment', desc: 'Oakwood Estate, room 405 has completed their payment!', time: '16:20', group: 'Yesterday', unread: false, date: 'Apr 24, 2024', roomName: 'Oakwood Estate, Room 405', amount: '$500' },
  { id: 'payment-5', type: 'payment', title: 'Payment', desc: 'Sunset Villa, room 210 has completed their payment!', time: '14:15', group: 'Yesterday', unread: false, date: 'Apr 24, 2024', roomName: 'Sunset Villa, Room 210', amount: '$380' },
  { id: 'payment-6', type: 'payment', title: 'Payment', desc: 'Riverfront Heights, room 501 has completed their payment!', time: '10:05', group: 'Yesterday', unread: false, date: 'Apr 24, 2024', roomName: 'Riverfront Heights, Room 501', amount: '$450' }
])

const currentNotification = computed(() => notifications.value.find(n => n.id === selectedNotif.value))

const filteredNotifications = computed(() => {
  let list = notifications.value
  
  if (activeNotifTab.value === 'booking') {
    list = list.filter(n => n.type === 'booking')
  } else if (activeNotifTab.value === 'property') {
    list = list.filter(n => n.type === 'property')
  } else if (activeNotifTab.value === 'system') {
    list = list.filter(n => n.type === 'system')
  }
  
  if (sidebarSearchQuery.value.trim()) {
    const q = sidebarSearchQuery.value.toLowerCase()
    list = list.filter(n => n.title.toLowerCase().includes(q) || n.desc.toLowerCase().includes(q))
  }
  
  return list
})

const todayNotifications = computed(() => filteredNotifications.value.filter(n => n.group === 'Today'))
const yesterdayNotifications = computed(() => filteredNotifications.value.filter(n => n.group === 'Yesterday'))

// Booking screen actions
const bookingStatus = ref('pending')
const showTenantProfileModal = ref(false)
const showReplyTenantModal = ref(false)
const replyMessageText = ref('')
const showSuccessToast = ref(false)
const successToastMessage = ref('')

function triggerToast(msg) {
  successToastMessage.value = msg
  showSuccessToast.value = true
  setTimeout(() => {
    showSuccessToast.value = false
  }, 3000)
}

function downloadReceipt() {
  const element = document.getElementById('receipt-pdf-target')
  if (!element) return
  
  const opt = {
    margin:       10,
    filename:     'Payment_Receipt.pdf',
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true },
    jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
  }
  
  html2pdf().set(opt).from(element).save().then(() => {
    triggerToast("Receipt downloaded successfully!")
  })
}

function viewTenantProfile() {
  showTenantProfileModal.value = true
}

function goToFullProfile() {
  showTenantProfileModal.value = false
  router.push('/roommate-match')
}

function openChatWithTenant() {
  replyMessageText.value = "Hi Chlorinde, thank you for booking. Your request is currently under review!"
  showReplyTenantModal.value = true
}

function sendTenantMessage() {
  showReplyTenantModal.value = false
  triggerToast("Message sent to Chlorinde!")
}

function confirmBooking() {
  bookingStatus.value = 'confirmed'
  // Increment occupied and tenants counts
  Object.keys(monthlyData.value).forEach(m => {
    monthlyData.value[m].occupied++
    monthlyData.value[m].tenants++
  })
  triggerToast("Booking confirmed successfully!")
}

function rejectBooking() {
  bookingStatus.value = 'rejected'
  triggerToast("Booking rejected.")
}

// Month selection and dashboard data
const showMonthPicker = ref(false)
const selectedMonth = ref('March 2024')
const monthlyData = ref({
  'January 2024': {
    collectedRed: 4000,
    collectedBlue: 12000,
    occupied: 25,
    vacant: 35,
    tenants: 22,
    revenue: '$1,000',
    maintenance: 3,
    recentPayments: [
      { tenant: 'Channa', property: 'Sky Star', date: 'Jan 13, 2025', amount: '$200' },
      { tenant: 'Mony', property: 'Sokha Angkor', date: 'Jan 09, 2025', amount: '$300' }
    ]
  },
  'February 2024': {
    collectedRed: 4500,
    collectedBlue: 13500,
    occupied: 28,
    vacant: 32,
    tenants: 24,
    revenue: '$1,100',
    maintenance: 4,
    recentPayments: [
      { tenant: 'Mony', property: 'Sokha Angkor', date: 'Feb 09, 2025', amount: '$300' },
      { tenant: 'Veasna', property: 'Smile Condo', date: 'Feb 22, 2025', amount: '$150' }
    ]
  },
  'March 2024': {
    collectedRed: 5000,
    collectedBlue: 15000,
    occupied: 30,
    vacant: 30,
    tenants: 25,
    revenue: '$1,200',
    maintenance: 5,
    recentPayments: [
      { tenant: 'Channa', property: 'Sky Star', date: 'Apr 13, 2025', amount: '$200' },
      { tenant: 'Mony', property: 'Sokha Angkor', date: 'Mar 09, 2025', amount: '$300' },
      { tenant: 'Veasna', property: 'Smile Condo', date: 'Feb 22, 2025', amount: '$150' }
    ]
  },
  'April 2024': {
    collectedRed: 7000,
    collectedBlue: 17000,
    occupied: 35,
    vacant: 25,
    tenants: 30,
    revenue: '$1,650',
    maintenance: 2,
    recentPayments: [
      { tenant: 'Nicole', property: 'Green Village', date: 'Apr 25, 2025', amount: '$350' },
      { tenant: 'Channa', property: 'Sky Star', date: 'Apr 13, 2025', amount: '$200' }
    ]
  },
  'May 2024': {
    collectedRed: 10000,
    collectedBlue: 20000,
    occupied: 45,
    vacant: 15,
    tenants: 40,
    revenue: '$2,300',
    maintenance: 1,
    recentPayments: [
      { tenant: 'Nicole', property: 'Green Village', date: 'May 10, 2025', amount: '$350' },
      { tenant: 'Nicole', property: 'Green Village', date: 'May 08, 2025', amount: '$350' }
    ]
  }
})

const currentMonthStats = computed(() => {
  return monthlyData.value[selectedMonth.value] || monthlyData.value['March 2024']
})

const dashboardTotal = computed(() => {
  const stats = currentMonthStats.value
  return stats.collectedRed + stats.collectedBlue
})

const donutOffset = computed(() => {
  const stats = currentMonthStats.value
  const total = dashboardTotal.value
  if (!total) return 100
  return (stats.collectedRed / total) * 100
})

// Rental listings & creation
const rentalProperties = properties

const filteredRentalProperties = computed(() => {
  if (!rentalProperties.value) return []
  if (!rentalSearchQuery.value) return rentalProperties.value
  const q = rentalSearchQuery.value.toLowerCase()
  return rentalProperties.value.filter(p => p.name.toLowerCase().includes(q))
})


const newListingName = ref('')
const newListingLocation = ref('')
const newListingPrice = ref(250)
const newListingType = ref('Apartment')
const newListingBedrooms = ref(1)
const newListingBeds = ref(1)
const newListingBaths = ref(1)
const newListingSqft = ref(500)
const newListingPax = ref('')
const newListingPeriod = ref('Long-term')
const newListingAmenities = ref([])
const newListingDescription = ref('')
const isGeneratingAI = ref(false)

async function generateAIDescription() {
  if (!newListingName.value || !newListingType.value || !newListingLocation.value) {
    triggerToast("Please fill out the Name, Type, and Location first so the AI has context!")
    return
  }

  isGeneratingAI.value = true
  
  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 1500))
  
  const name = newListingName.value
  const type = newListingType.value
  const loc = newListingLocation.value
  const beds = newListingBedrooms.value
  const baths = newListingBaths.value
  const amenities = newListingAmenities.value.join(", ") || "essential amenities"
  const price = newListingPrice.value
  const sqft = newListingSqft.value
  const period = newListingPeriod.value
  const pax = newListingPax.value || 'multiple'
  
  const generatedText = `🌟 Welcome to ${name}! 🌟\n\n` +
    `Discover this stunning ${beds}-bedroom, ${baths}-bathroom ${type.toLowerCase()} perfectly situated in the highly sought-after area of ${loc}.\n\n` +
    `✨ Property Highlights:\n` +
    `• Spacious layout with ${sqft} sqft of beautiful living space\n` +
    `• Accommodates up to ${pax} guests comfortably\n` +
    `• Premium amenities including: ${amenities}\n\n` +
    `Designed for both comfort and style, this property offers a premium living experience. Whether you're looking to relax or entertain, the modern finishes provide the perfect backdrop for your lifestyle.\n\n` +
    `💰 Available for just $${price} / ${period === 'Short-term' ? 'night' : 'month'}!\n\n` +
    `Don't miss out on making this exceptional property your next home. Contact us today to learn more!`
    
  newListingDescription.value = generatedText
  isGeneratingAI.value = false
  triggerToast("AI Description Generated!")
}
const newListingImages = ref([])
const newListingFiles = ref([])
const newListingContactName = ref('')
const newListingContactPhone = ref('')
const newListingContactSocial = ref('')
const isPublishing = ref(false)

const isFormValid = computed(() => {
  return newListingName.value.trim() !== '' &&
         newListingLocation.value.trim() !== '' &&
         newListingPrice.value !== '' && newListingPrice.value > 0 &&
         newListingSqft.value !== '' && newListingSqft.value > 0 &&
         newListingBedrooms.value !== '' && newListingBedrooms.value > 0 &&
         newListingBeds.value !== '' && newListingBeds.value > 0 &&
         newListingBaths.value !== '' && newListingBaths.value > 0 &&
         String(newListingPax.value).trim() !== '' &&
         newListingDescription.value.trim() !== '' &&
         newListingFiles.value.length >= 3 &&
         newListingContactName.value.trim() !== '' &&
         newListingContactPhone.value.trim() !== ''
})

function processImage(file) {
  return new Promise((resolve, reject) => {
    const img = new Image()
    img.src = URL.createObjectURL(file)
    img.onload = () => {
      URL.revokeObjectURL(img.src)
      
      // Dimension check: minimum 600x400
      if (img.width < 600 || img.height < 400) {
        return reject(new Error(`Image "${file.name}" is too small. Minimum size is 600x400 pixels.`))
      }

      // Max dimensions for optimization
      const MAX_WIDTH = 1920
      const MAX_HEIGHT = 1080
      let width = img.width
      let height = img.height

      if (width > MAX_WIDTH || height > MAX_HEIGHT) {
        const ratio = Math.min(MAX_WIDTH / width, MAX_HEIGHT / height)
        width = Math.round(width * ratio)
        height = Math.round(height * ratio)
      }

      const canvas = document.createElement('canvas')
      canvas.width = width
      canvas.height = height
      const ctx = canvas.getContext('2d')
      ctx.drawImage(img, 0, 0, width, height)
      
      // Convert to blob
      canvas.toBlob((blob) => {
        if (!blob) return reject(new Error('Canvas is empty'))
        const optimizedFile = new File([blob], file.name, {
          type: 'image/jpeg',
          lastModified: Date.now()
        })
        resolve(optimizedFile)
      }, 'image/jpeg', 0.85) // 85% quality JPEG
    }
    img.onerror = () => reject(new Error(`Failed to read image "${file.name}".`))
  })
}

async function handleRealUpload(event) {
  const files = event.target.files
  if (!files || files.length === 0) return
  
  triggerToast("Processing images...")
  let addedCount = 0
  
  for (let i = 0; i < files.length; i++) {
    try {
      const optimizedFile = await processImage(files[i])
      newListingFiles.value.push(optimizedFile)
      
      // Generate preview
      const reader = new FileReader()
      reader.onload = (e) => {
        newListingImages.value.push(e.target.result)
      }
      reader.readAsDataURL(optimizedFile)
      addedCount++
    } catch (err) {
      alert(err.message)
    }
  }
  
  if (addedCount > 0) {
    triggerToast(`${addedCount} image(s) processed and added!`)
  }
  
  // Clear the input so they can upload the same file again if they deleted it
  event.target.value = ''
}

async function publishListing() {
  if (!newListingName.value.trim() || isPublishing.value) return
  
  // Validation
  if (newListingFiles.value.length < 3) {
    triggerToast("Please upload at least 3 images to proceed.")
    return
  }
  if (!newListingDescription.value.trim()) {
    triggerToast("Please add a description for the listing.")
    return
  }

  isPublishing.value = true
  triggerToast("Publishing listing... please wait.")
  
  try {
    const uploadedImageUrls = []
    
    // Upload files to Firebase Storage
    if (newListingFiles.value.length > 0) {
      for (const file of newListingFiles.value) {
        const fileRef = storageRef(storage, `property_images/${Date.now()}_${file.name}`)
        const snapshot = await uploadBytes(fileRef, file)
        const downloadURL = await getDownloadURL(snapshot.ref)
        uploadedImageUrls.push(downloadURL)
      }
    }
    
    const finalImages = uploadedImageUrls.length > 0 
      ? uploadedImageUrls 
      : ['https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80']
      
    const landlordId = auth.currentUser ? auth.currentUser.uid : 'unknown_landlord'

    const newProperty = {
      name: newListingName.value,
      price: newListingPrice.value || 250,
      type: newListingType.value,
      location: newListingLocation.value || 'Phnom Penh',
      lat: 11.5750 + (Math.random() - 0.5) * 0.05,
      lng: 104.8850 + (Math.random() - 0.5) * 0.05,
      bedrooms: newListingBedrooms.value,
      beds: newListingBeds.value,
      baths: newListingBaths.value,
      sqft: newListingSqft.value,
      pax: newListingPax.value,
      period: newListingPeriod.value,
      amenities: [...newListingAmenities.value],
      rating: 0,
      reviews: 0,
      contactName: newListingContactName.value,
      contactPhone: newListingContactPhone.value,
      contactSocial: newListingContactSocial.value,
      renter: { name: newListingContactName.value || 'You (Landlord)', image: landlordProfile.value.avatar },
      images: finalImages,
      image: finalImages[0],
      description: newListingDescription.value,
      landlordId: landlordId,
      createdAt: serverTimestamp()
    }
    
    // Save to Firestore
    const docRef = await addDoc(collection(db, 'properties'), newProperty)
    
    // Add id to local object to update UI immediately
    newProperty.id = docRef.id
    // Because rentalProperties is an alias to properties, we just unshift it once
    properties.value.unshift(newProperty)
    
    triggerToast("Listing published successfully!")
    
    // Reset Form
    newListingName.value = ''
    newListingLocation.value = ''
    newListingPrice.value = 250
    newListingType.value = 'Apartment'
    newListingBedrooms.value = 1
    newListingBeds.value = 1
    newListingBaths.value = 1
    newListingSqft.value = 500
    newListingPax.value = ''
    newListingPeriod.value = 'Long-term'
    newListingAmenities.value = []
    newListingDescription.value = ''
    newListingImages.value = []
    newListingFiles.value = []
    newListingContactName.value = ''
    newListingContactPhone.value = ''
    newListingContactSocial.value = ''
    
    activePage.value = 'rental'
  } catch (error) {
    console.error("Error publishing listing:", error)
    alert("Failed to publish listing: " + error.message)
  } finally {
    isPublishing.value = false
  }
}

const showDeleteConfirmModal = ref(false)
const propertyIdToDelete = ref(null)

function deleteProperty(propertyId) {
  propertyIdToDelete.value = propertyId
  showDeleteConfirmModal.value = true
}

async function confirmDeleteProperty() {
  const propertyId = propertyIdToDelete.value
  showDeleteConfirmModal.value = false
  
  if (!propertyId || typeof propertyId === 'number') {
    // It's a mock property
    const idx = properties.value.findIndex(p => p.id === propertyId)
    if (idx !== -1) properties.value.splice(idx, 1)
    triggerToast("Mock property deleted.")
    return
  }
  
  try {
    // Delete from Firestore
    await deleteDoc(doc(db, 'properties', propertyId))
    
    // Remove from local properties array
    const globalIndex = properties.value.findIndex(p => p.id === propertyId)
    if (globalIndex !== -1) {
      properties.value.splice(globalIndex, 1)
    }
    
    triggerToast("Listing deleted successfully.")
  } catch (err) {
    console.error("Error deleting property:", err)
    triggerToast("Failed to delete property: " + err.message)
  }
}

function cancelDeleteProperty() {
  showDeleteConfirmModal.value = false
  propertyIdToDelete.value = null
}

// Leases filtering
const leases = ref([
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Sky Star', status: 'Expired', image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Green', status: 'Expired', image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Monarch', status: 'Expired', image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Morgan', status: 'Expired', image: 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Sky Star', status: 'Expired', image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Green', status: 'Expired', image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Sokha', status: 'Expired', image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=100&q=80' },
  { id: '0001', tenant: 'Nicole', unit: '101', start: 'MAR 2014', end: 'FEB 2020', place: 'Mekong', status: 'Expired', image: 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=100&q=80' }
])

const filteredLeases = computed(() => {
  if (!leaseSearchQuery.value) return leases.value
  const q = leaseSearchQuery.value.toLowerCase()
  return leases.value.filter(l => 
    l.tenant.toLowerCase().includes(q) || 
    l.place.toLowerCase().includes(q) ||
    l.unit.toLowerCase().includes(q)
  )
})

// Dashboard Properties Overview Table data
const dashboardProperties = ref([
  { name: 'Green Villa', tenants: '30 Tenants', status: 'Occupied', income: '$2,000' },
  { name: 'Green Villa', tenants: '30 Tenants', status: 'Occupied', income: '$2,000' },
  { name: 'Green Villa', tenants: '30 Tenants', status: 'Occupied', income: '$2,000' }
])

// Landlord Profile form data
const isEditingProfile = ref(false)
const landlordProfile = ref({
  firstName: 'Sangonomiya',
  lastName: 'Kokomi',
  avatar: 'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=80&q=80',
  email: 'skmi23@gmail.com',
  phone: '+855 123 456 78',
  address: 'Phnom Penh/Cambodia',
  license: 'L-2027-9948',
  tier: 'Premium Host'
})

function saveProfileInfo() {
  isEditingProfile.value = false
  triggerToast('Profile updated successfully!')
}

// Help FAQ Accordion & filtering
const faqs = ref([
  { question: 'How do I add a new property listing?', answer: 'Navigate to the "Rental" tab in the sidebar and click the "Create new +" button. Fill in the title, price, room details, and upload high-quality pictures.', open: false },
  { question: 'What is the processing time for tenant booking payouts?', answer: 'Payouts are processed within 24-48 hours after the tenant confirms their check-in details. Funds are transferred to your registered bank account.', open: false },
  { question: 'How does the background check for roommates/tenants work?', answer: 'We run secure national identity checks, credit validation, and user profile verification to ensure a safe rental community.', open: false }
])

const filteredFaqs = computed(() => {
  if (!faqSearchQuery.value) return faqs.value
  const q = faqSearchQuery.value.toLowerCase()
  return faqs.value.filter(f => 
    f.question.toLowerCase().includes(q) ||
    f.answer.toLowerCase().includes(q)
  )
})

// Security Tab details
const enable2FA = ref(true)
const currentPin = ref('****')

function changePin() {
  const newPin = prompt('Enter new 4-digit Portal PIN:')
  if (newPin && newPin.length === 4) {
    currentPin.value = newPin
    triggerToast('Portal PIN changed successfully!')
  } else if (newPin) {
    alert('PIN must be exactly 4 digits.')
  }
}
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
  border-bottom: none;
  flex-shrink: 0;
  background: #5C4E4E;
  z-index: 10;
}

.logo { display: flex; align-items: center; gap: 9px; }

.logo-icon {
  width: 32px; height: 32px;
  background: rgba(255,255,255,0.15); border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  color: #ffffff;
}

.logo-text { font-weight: 600; font-size: 1rem; color: #ffffff; }

.avatar {
  width: 38px; height: 38px;
  border-radius: 50%; overflow: hidden;
  border: 2px solid rgba(255,255,255,0.5);
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
  color: #5C4E4E;
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
.nav-item:hover { background: #f7f7f7; color: #5C4E4E; }
.nav-item.active { background: #D1D0D0; color: #5C4E4E; font-weight: 600; }
.nav-item svg { flex-shrink: 0; color: inherit; }

.nav-item.nav-item-create {
  color: #e07a5f;
}
.nav-item.nav-item-create svg {
  color: #e07a5f;
}
.nav-item.nav-item-create:hover {
  background: rgba(224, 122, 95, 0.08);
  color: #d16b50;
}
.nav-item.nav-item-create.active {
  background: #e07a5f;
  color: #ffffff;
}

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
  font-size: 1.3rem; font-weight: 600; color: #5C4E4E;
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
  background: #D1D0D0; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
}

.notif-header-text { flex: 1; }

.notif-title { font-weight: 600; font-size: 0.95rem; color: #5C4E4E; margin-bottom: 3px; }
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
  font-size: 0.83rem; color: #5C4E4E; font-weight: 500;
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

.btn-action.confirm { color: #5C4E4E; }
.btn-action.confirm:hover { background: #f0fdf4; border-color: #86efac; }

.btn-action.reject { color: #dc2626; }
.btn-action.reject:hover { background: #fef2f2; border-color: #fca5a5; }

.btn-action.icon-only {
  padding: 10px 12px;
}

/* --- Notification Tabs --- */
.notif-tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1.5px solid #eaeaea;
  margin-bottom: 24px;
}

.notif-tab-btn {
  background: none;
  border: none;
  padding: 12px 0;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  font-weight: 600;
  color: #666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s ease;
}

.notif-tab-btn:hover {
  color: #5C4E4E;
}

.notif-tab-btn.active {
  color: #5C4E4E;
}

.notif-tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: -1.5px;
  left: 0;
  right: 0;
  height: 2.5px;
  background: #5C4E4E;
  border-radius: 2px;
}

/* --- Notification List --- */
.notif-list-container {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.notif-date-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.date-group-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.85rem;
  font-weight: 500;
  color: #888;
  margin: 0;
}

.notif-item-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fafafa;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  padding: 16px 20px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.notif-item-row:hover {
  background: #f5f5f5;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}

.notif-item-left {
  display: flex;
  align-items: center;
  gap: 16px;
  flex: 1;
  min-width: 0;
}

.notif-badge-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #D1D0D0;
  color: #5C4E4E;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.notif-badge-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #ffffff;
  border: 1px solid #eaeaea;
  flex-shrink: 0;
}

.notif-item-copy {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.notif-item-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #5C4E4E;
}

.notif-item-desc {
  font-size: 0.8rem;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.notif-item-right {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-left: 16px;
}

.notif-item-time {
  font-size: 0.78rem;
  color: #999;
  font-weight: 500;
}

.unread-dot-green {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #5C4E4E;
  flex-shrink: 0;
}

/* --- My Profile Tab --- */
.profile-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.profile-card-layout {
  background: #ffffff;
  border: 1px solid #efefef;
  border-radius: 16px;
  padding: 32px;
  width: 100%;
  box-shadow: 0 10px 30px rgba(0,0,0,0.04);
}

.section-subtitle {
  font-size: 1.1rem;
  font-weight: 700;
  color: #5C4E4E;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
}

.profile-actions-row {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.profile-hero-mini {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 28px;
}

.profile-avatar-wrapper-mini {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid #efede8;
}

.profile-avatar-wrapper-mini img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-hero-info h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #5C4E4E;
  margin: 0 0 6px 0;
}

.badge-premium {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  background: #D1D0D0;
  color: #5C4E4E;
}

.profile-details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 28px;
}

.profile-detail-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.profile-detail-item.full-row {
  grid-column: 1 / -1;
}

.profile-detail-item label {
  font-size: 0.78rem;
  font-weight: 600;
  color: #555;
}

.profile-input {
  padding: 10px 14px;
  border: 1.5px solid #e0e0e0;
  border-radius: 10px;
  font-family: inherit;
  font-size: 0.85rem;
  color: #5C4E4E;
  background: #fafafa;
  outline: none;
  transition: border-color 0.2s;
}

.profile-input:focus {
  border-color: #5C4E4E;
  background: #fff;
}

.profile-input:disabled {
  background: #f0f0f0;
  color: #888;
  cursor: not-allowed;
}

.btn-save-profile {
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  padding: 12px 24px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-save-profile:hover {
  background: #2a2a2a;
}

/* --- Dashboard Tab --- */
.dashboard-tab-content {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.dashboard-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.date-picker-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1.5px solid #e0e0e0;
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #5C4E4E;
  cursor: pointer;
  background: #fff;
  transition: border-color 0.2s;
}

.date-picker-btn:hover {
  border-color: #999;
}

/* Donut Summary Card */
.donut-summary-card {
  background: #e0e0e0;
  border: 1px solid #D1D0D0;
  border-radius: 16px;
  padding: 32px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
  box-shadow: 0 8px 30px rgba(192, 120, 74, 0.08);
  flex-wrap: wrap;
  gap: 24px;
}

.donut-left-col, .donut-right-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  min-width: 120px;
}

.amount-collected-red {
  font-size: 1.5rem;
  font-weight: 700;
  color: #5C4E4E;
}

.amount-collected-blue {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
}

.amount-label {
  font-size: 0.72rem;
  font-weight: 600;
  color: #999;
  letter-spacing: 0.05em;
}

.donut-center-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.donut-chart-container {
  width: 140px;
  height: 140px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.donut-svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.donut-inner-text {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.donut-month {
  font-size: 0.8rem;
  color: #666;
  font-weight: 500;
}

.donut-total {
  font-size: 1.25rem;
  font-weight: 700;
  color: #5C4E4E;
  margin: 2px 0;
}

.donut-sublabel {
  font-size: 0.7rem;
  color: #999;
  font-weight: 500;
}

.donut-card-footer {
  width: 100%;
  border-top: 1px solid #f0f0f0;
  padding-top: 20px;
  margin-top: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 0.82rem;
  font-weight: 600;
  color: #475569;
}

.footer-stat-group {
  display: flex;
  gap: 24px;
}

.stat-col {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-label {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 500;
}

.stat-value {
  font-size: 1.1rem;
  color: #5C4E4E;
  font-weight: 600;
}

/* KPI Grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.kpi-card {
  background: #e0e0e0;
  border: 1px solid #D1D0D0;
  border-radius: 12px;
  padding: 18px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
}

.kpi-icon-wrapper {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: #f8fafc;
  color: #475569;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.kpi-properties { background: #D1D0D0; color: #5C4E4E; }
.kpi-revenue { background: #D1D0D0; color: #5C4E4E; }
.kpi-tenants { background: #D1D0D0; color: #5C4E4E; }
.kpi-maintenance { background: #D1D0D0; color: #5C4E4E; }

.kpi-copy {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.kpi-title {
  font-size: 0.72rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}

.kpi-value {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1e293b;
}

/* Tables Layout */
.dashboard-tables-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 900px) {
  .dashboard-tables-row {
    grid-template-columns: 1fr;
  }
}

.table-card {
  background: #e0e0e0;
  border: 1px solid #D1D0D0;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}

.table-card-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #5C4E4E;
  margin: 0 0 16px 0;
}

.dashboard-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  text-align: left;
}

.dashboard-table th {
  padding: 10px 12px;
  color: #64748b;
  font-weight: 600;
  border-bottom: 1px solid #f1f5f9;
}

.dashboard-table td {
  padding: 12px;
  color: #334155;
  border-bottom: 1px solid #f8fafc;
}

.badge-status-occupied {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 20px;
  background: #f1f5f9;
  color: #475569;
}

.income-value-cell {
  font-weight: 600;
  text-align: right;
}

.income-value-cell.green {
  color: #5C4E4E;
}

.table-action-link-btn {
  background: none;
  border: none;
  color: #64748b;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  align-self: center;
  margin-top: 20px;
  transition: color 0.2s;
}

.table-action-link-btn:hover {
  color: #5C4E4E;
}

/* --- Rental Tab --- */
.rental-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.rental-search-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  margin-bottom: 12px;
}

.rental-search-box {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1.5px solid #e2e8f0;
  border-radius: 50px;
  padding: 8px 16px;
  background: #fff;
  flex: 1;
  max-width: 320px;
}

.rental-search-box input {
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 0.82rem;
  color: #333;
  width: 100%;
}

.btn-create-new {
  background: #ffffff;
  border: 1.5px solid #111111;
  color: #5C4E4E;
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}

.btn-create-new:hover {
  background: #5C4E4E;
  color: #ffffff;
}

.properties-section-rental {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.properties-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #5C4E4E;
  margin: 0;
}

.rental-properties-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 16px;
}

.rental-property-card {
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 1.15;
  cursor: pointer;
  position: relative;
  transition: transform 0.2s, box-shadow 0.2s;
}

.rental-property-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.rental-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.rental-card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.1) 60%, transparent 100%);
}

.rental-card-label {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  text-align: center;
}

/* --- Leasing Tab --- */
.leasing-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.lease-table-card {
  background: #e0e0e0;
  border: 1px solid #efefef;
  border-radius: 16px;
  padding: 24px;
  overflow-x: auto;
}

.lease-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  text-align: left;
}

.lease-table th {
  padding: 12px;
  color: #64748b;
  font-weight: 600;
  border-bottom: 1px solid #e2e8f0;
}

.lease-table td {
  padding: 12px;
  color: #334155;
  border-bottom: 1px solid #f1f5f9;
}

.gray-code {
  color: #94a3b8 !important;
  font-family: monospace;
}

.badge-expired {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 20px;
  background: #fee2e2;
  color: #ef4444;
}

.lease-thumb-wrapper {
  width: 72px;
  height: 48px;
  border-radius: 6px;
  overflow: hidden;
}

.lease-thumb-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* --- Help FAQs Tab --- */
.help-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 720px;
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.faq-item {
  border: 1.5px solid #efefef;
  border-radius: 12px;
  background: #ffffff;
  overflow: hidden;
  transition: border-color 0.2s;
}

.faq-item.open {
  border-color: #5C4E4E;
}

.faq-question {
  width: 100%;
  padding: 18px 24px;
  background: none;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  color: #5C4E4E;
  text-align: left;
  cursor: pointer;
}

.faq-arrow-svg {
  transition: transform 0.2s ease;
  color: #888;
}

.faq-item.open .faq-arrow-svg {
  transform: rotate(180deg);
  color: #5C4E4E;
}

.faq-answer {
  padding: 0 24px 20px 24px;
  font-size: 0.82rem;
  line-height: 1.55;
  color: #555;
}

/* --- Security Tab --- */
.security-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 600px;
}

/* --- Create Listing Tab --- */
.create-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.create-layout {
  display: flex;
  gap: 40px;
  align-items: flex-start;
}
.create-left {
  flex: 0 0 400px;
  position: sticky;
  top: 24px;
}
.create-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 32px;
  max-width: 700px;
}
.image-upload-area {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 16px;
  border: 2px dashed #d1d5db;
  background: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
  transition: all 0.2s;
}
.image-upload-area.has-image {
  border: none;
  background: transparent;
}
.image-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  color: #6b7280;
  gap: 12px;
}
.image-preview {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}
.image-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  width: 100%;
  padding: 16px;
}
.add-more-card {
  border: 2px dashed #d1d5db;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #6b7280;
  cursor: pointer;
  background: #fafafa;
  min-height: 120px;
  transition: all 0.2s;
}
.add-more-card:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}
.add-more-card span {
  font-size: 0.85rem;
  font-weight: 600;
}
.image-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.btn-remove-image {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(0,0,0,0.5);
  color: #fff;
  border: none;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.form-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: #fff;
  border: 1px solid #efefef;
  border-radius: 12px;
  padding: 24px;
}
.section-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #111;
  margin: 0 0 8px 0;
}
.form-row {
  display: flex;
  gap: 16px;
}
.form-row.three-cols {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 16px;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}
.form-group.full-width {
  width: 100%;
}
.form-group label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #4b5563;
}
.form-input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.95rem;
  font-family: inherit;
  transition: border-color 0.2s;
  outline: none;
}
.form-input:focus {
  border-color: #5C4E4E;
}
.amenities-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.amenity-pill {
  padding: 8px 16px;
  border: 1.5px solid #d1d5db;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #4b5563;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
}
.amenity-pill.selected {
  background: #5C4E4E;
  border-color: #5C4E4E;
  color: #fff;
}
.create-action-area {
  display: flex;
  justify-content: flex-end;
  padding-top: 16px;
}
.btn-publish {
  background: #111;
  color: #fff;
  border: none;
  padding: 14px 32px;
  font-size: 1.05rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s;
}
.btn-publish:hover:not(:disabled) {
  transform: translateY(-2px);
}
.btn-publish:disabled {
  background: #ccc;
  cursor: not-allowed;
}

/* Booking Detail Info */
.booking-details {
  background: #f9f9f9;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Receipt Styles */
.receipt-card {
  background: #e0e0e0;
  border: 1px dashed #d1d5db;
  border-radius: 12px;
  padding: 24px;
  width: 100%;
  box-shadow: 0 4px 15px rgba(0,0,0,0.02);
}

.receipt-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.receipt-header h3 {
  font-size: 1.2rem;
  font-weight: 700;
  margin: 0;
  color: #5C4E4E;
}

.status-badge.success {
  background: #D1D0D0;
  color: #5C4E4E;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.receipt-body {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.receipt-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
}

.receipt-row span {
  color: #6b7280;
}

.receipt-row strong {
  color: #5C4E4E;
  font-weight: 600;
  text-align: right;
}

.receipt-row.total {
  font-size: 1.1rem;
}

.receipt-divider {
  height: 1px;
  background: #e5e7eb;
  margin: 8px 0;
}

.download-btn {
  background: #5C4E4E;
  color: #fff;
  border: none;
  padding: 14px 24px;
  border-radius: 12px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.2);
}

.download-btn:hover {
  background: #4A3E3E;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.3);
}

.download-btn:active {
  transform: translateY(0);
}

.security-card {
  background: #e0e0e0;
  border: 1px solid #efefef;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.security-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #f8fafc;
  padding-bottom: 20px;
  gap: 20px;
}

.security-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.security-text-col h3 {
  font-size: 0.92rem;
  font-weight: 600;
  color: #5C4E4E;
  margin: 0 0 4px 0;
}

.security-text-col p {
  font-size: 0.78rem;
  color: #666;
  margin: 0;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
  flex-shrink: 0;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  inset: 0;
  background-color: #cbd5e1;
  transition: .3s;
  border-radius: 34px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .3s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: #5C4E4E;
}

input:checked + .toggle-slider:before {
  transform: translateX(20px);
}

.security-pin-input-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-change-pin {
  background: none;
  border: 1.5px solid #111111;
  color: #5C4E4E;
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-change-pin:hover {
  background: #5C4E4E;
  color: #fff;
}

/* --- Account Status Tab --- */
.account-tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 600px;
}

.account-status-card {
  background: #e0e0e0;
  border: 1px solid #efefef;
  border-radius: 16px;
  padding: 28px;
}

.account-status-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #f1f5f9;
  padding-bottom: 20px;
  margin-bottom: 24px;
}

.status-badge-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9rem;
  font-weight: 700;
  color: #5C4E4E;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #5C4E4E;
}

.status-valid-date {
  font-size: 0.78rem;
  color: #64748b;
  font-weight: 500;
}

.account-usage-stats {
  display: flex;
  flex-direction: column;
}

.usage-stat-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.usage-stat-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.78rem;
  font-weight: 600;
  color: #475569;
}

.usage-progress-bar {
  width: 100%;
  height: 6px;
  background: #f1f5f9;
  border-radius: 3px;
  overflow: hidden;
}

.usage-progress-fill {
  height: 100%;
  background: #5C4E4E;
  border-radius: 3px;
}

/* --- Month Picker Dropdown --- */
.month-picker-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  background: #ffffff;
  border: 1px solid #efefef;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
  z-index: 100;
  overflow: hidden;
  min-width: 140px;
}
.month-picker-item {
  padding: 10px 16px;
  font-size: 0.8rem;
  font-weight: 500;
  color: #333;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.month-picker-item:hover {
  background: #f7f7f7;
  color: #5C4E4E;
}
.month-picker-item.active {
  background: #D1D0D0;
  color: #5C4E4E;
  font-weight: 600;
}

/* --- Custom Modals Overlay --- */
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

.chat-close-btn {
  background: none;
  border: none;
  color: #999;
  cursor: pointer;
  padding: 4px;
  font-size: 1.5rem;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.chat-close-btn:hover {
  color: #333;
}

.chat-modal-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
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
  border-color: #5C4E4E;
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

.chat-cancel-btn:hover {
  background: #f7fafc;
  color: #1a202c;
}

.chat-send-btn {
  padding: 10px 20px;
  border: none;
  background: #5C4E4E;
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

/* Success Toast */
.chat-success-toast {
  position: fixed;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  background: #5C4E4E;
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

/* --- Mobile Responsive Rules --- */
@media (max-width: 768px) {
  .body {
    flex-direction: column;
    overflow-y: auto;
  }
  
  .sidebar {
    width: 100%;
    height: auto;
    border-right: none;
    border-bottom: 1px solid #efefef;
    padding: 12px 16px;
    flex-direction: row;
    align-items: center;
    overflow-x: auto;
    overflow-y: hidden;
    gap: 8px;
    z-index: 5;
    background: #fff;
    -webkit-overflow-scrolling: touch;
  }
  
  .sidebar::-webkit-scrollbar {
    display: none;
  }
  
  .sidebar-title, .search-box, .nav-group-label {
    display: none;
  }
  
  .sidebar-nav {
    flex-direction: row;
    gap: 8px;
    flex-shrink: 0;
  }
  
  .nav-item {
    padding: 8px 16px;
    width: auto;
    white-space: nowrap;
    border-radius: 20px;
    background: #f1f1f1;
    font-size: 0.85rem;
    justify-content: center;
  }
  
  .nav-item.active {
    background: #5C4E4E;
    color: #fff;
  }

  .main-content {
    padding: 16px;
    overflow: visible;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 20px;
  }

  /* Dashboard */
  .dashboard-grid, .finance-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .quick-actions {
    flex-wrap: wrap;
  }

  .action-btn {
    flex: 1 1 calc(50% - 12px);
  }

  /* Rental */
  .properties-grid {
    grid-template-columns: 1fr;
  }

  /* Notifications */
  .notif-container {
    flex-direction: column;
    height: auto;
    max-height: none;
  }
  
  .notif-sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid #efefef;
    max-height: 350px;
  }

  .notif-main {
    min-height: 400px;
  }

  .chat-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  /* Security / Profile */
  .security-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  
  .profile-details-grid, .account-tab-content {
    grid-template-columns: 1fr;
  }

  .profile-actions-row {
    flex-direction: column;
  }

  .btn-save-profile {
    width: 100%;
  }

  /* Tables & Leasing */
  .lease-table-card, .table-card {
    padding: 16px;
    overflow-x: auto;
  }
  
  .lease-table {
    min-width: 700px;
  }
  
  .dashboard-table {
    min-width: 450px;
  }

  /* Modals */
  .chat-modal-box {
    width: 95%;
  }

  .chat-modal-body > div > div[style*="grid-template-columns"] {
    grid-template-columns: 1fr !important;
  }

  /* Create Listing */
  .create-layout {
    flex-direction: column;
    gap: 24px;
  }
  .create-left {
    flex: none;
    width: 100%;
    position: static;
  }
  .create-right {
    max-width: 100%;
  }
  .form-row, .form-row.three-cols {
    flex-direction: column;
    display: flex;
  }
  .image-grid {
    grid-template-columns: 1fr;
  }
}
  .btn-delete-property {
    position: absolute;
    top: 8px;
    right: 8px;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: background 0.2s;
  }
  .btn-delete-property:hover {
    background: rgba(255, 0, 0, 0.8);
  }

  .delete-confirm-modal-box {
    background: white;
    width: 400px;
    max-width: 90%;
    border-radius: 16px;
    padding: 32px 24px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    animation: slideUp 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  .delete-confirm-icon {
    width: 64px;
    height: 64px;
    background: #FFF0F0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 16px;
  }
  .delete-confirm-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 12px;
  }
  .delete-confirm-text {
    font-family: 'DM Sans', sans-serif;
    color: #222;
    font-size: 1.15rem;
    font-weight: 500;
    line-height: 1.5;
    margin-bottom: 40px;
    letter-spacing: 0.3px;
    padding: 0 10px;
  }
  .delete-confirm-subtext {
    font-size: 0.95rem;
    color: #666;
    font-weight: 400;
    line-height: 1.6;
    letter-spacing: 0.2px;
  }
  .delete-confirm-actions {
    display: flex;
    gap: 12px;
  }
  .btn-cancel-delete {
    flex: 1;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ddd;
    background: white;
    color: #333;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-cancel-delete:hover {
    background: #f5f5f5;
  }
  .btn-confirm-delete {
    flex: 1;
    padding: 12px;
    border-radius: 8px;
    border: none;
    background: #FF4D4D;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-confirm-delete:hover {
    background: #E63939;
  }
  
  .btn-ai-generate {
    background: linear-gradient(135deg, #a855f7, #6366f1);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .btn-ai-generate:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
  }
  .btn-ai-generate:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
  
  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  .spin-icon {
    animation: spin 1s linear infinite;
  }
</style>
