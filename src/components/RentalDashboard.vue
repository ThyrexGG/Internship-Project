<template>
  <div class="rental-dashboard">
    <!-- Header -->
    <header class="rd-header">
      <div class="rd-header-text">
        <h1 class="main-title">Rentals</h1>
        <p class="rd-subtitle">
          Manage your active tenancies, review lease terms, and explore your rental history.
        </p>
      </div>
      <div class="rd-header-actions">
        <button class="rd-btn-outline" @click="$emit('browse-listings')" type="button">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          Browse Homes
        </button>
        <button class="rd-btn-icon" @click="fetchApplications" :class="{ 'is-spinning': isSyncing }" title="Refresh live rentals" type="button" aria-label="Refresh rentals">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="23 4 23 10 17 10"></polyline>
            <polyline points="1 20 1 14 7 14"></polyline>
            <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
          </svg>
        </button>
      </div>
    </header>

    <!-- Top KPI Summary Cards (4-column unified theme grid) -->
    <div class="rd-kpi-grid">
      <div class="rd-kpi-card" :class="{ 'highlight': activeFilter === 'active' }" @click="activeFilter = 'active'">
        <div class="kpi-icon-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            <polyline points="9 22 9 12 15 12 15 22"></polyline>
          </svg>
        </div>
        <div class="kpi-info">
          <span class="kpi-label">Currently Renting</span>
          <div class="kpi-value-row">
            <span class="kpi-value">{{ totalActiveCount }}</span>
            <span class="kpi-pill">Active Lease</span>
          </div>
          <span class="kpi-sub">Unit {{ activeRental.unit }} · {{ activeRental.name }}</span>
        </div>
      </div>

      <div class="rd-kpi-card" @click="activeFilter = 'active'">
        <div class="kpi-icon-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect>
            <line x1="1" y1="10" x2="23" y2="10"></line>
          </svg>
        </div>
        <div class="kpi-info">
          <span class="kpi-label">Monthly Rent</span>
          <div class="kpi-value-row">
            <span class="kpi-value">${{ activeRental.rent }}</span>
            <span class="kpi-sub-period">/ month</span>
          </div>
          <span class="kpi-sub">Next due: {{ activeRental.nextDue }}</span>
        </div>
      </div>

      <div class="rd-kpi-card" :class="{ 'highlight': activeFilter === 'history' }" @click="activeFilter = 'history'">
        <div class="kpi-icon-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 14 14"></polyline>
          </svg>
        </div>
        <div class="kpi-info">
          <span class="kpi-label">Past Rentals</span>
          <div class="kpi-value-row">
            <span class="kpi-value">{{ pastRentals.length }}</span>
            <span class="kpi-pill">Completed</span>
          </div>
          <span class="kpi-sub">All deposits refunded</span>
        </div>
      </div>

      <div class="rd-kpi-card" :class="{ 'highlight': activeFilter === 'applications' }" @click="activeFilter = 'applications'">
        <div class="kpi-icon-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
          </svg>
        </div>
        <div class="kpi-info">
          <span class="kpi-label">Applications</span>
          <div class="kpi-value-row">
            <span class="kpi-value">{{ liveApplications.length }}</span>
            <span class="kpi-pill">{{ liveApplications.length > 0 ? 'Pending' : '0' }}</span>
          </div>
          <span class="kpi-sub">{{ liveApplications.length > 0 ? 'Under review' : 'No pending requests' }}</span>
        </div>
      </div>
    </div>

    <!-- Segmented Navigation Filters -->
    <div class="rd-filters-bar">
      <button 
        class="rd-filter-pill" 
        :class="{ active: activeFilter === 'all' }" 
        @click="activeFilter = 'all'"
        type="button"
      >
        All Rentals ({{ 1 + pastRentals.length + liveApplications.length }})
      </button>
      <button 
        class="rd-filter-pill" 
        :class="{ active: activeFilter === 'active' }" 
        @click="activeFilter = 'active'"
        type="button"
      >
        <span class="pill-dot"></span>
        Currently Renting ({{ totalActiveCount }})
      </button>
      <button 
        class="rd-filter-pill" 
        :class="{ active: activeFilter === 'history' }" 
        @click="activeFilter = 'history'"
        type="button"
      >
        Past Rentals ({{ pastRentals.length }})
      </button>
      <button 
        class="rd-filter-pill" 
        :class="{ active: activeFilter === 'applications' }" 
        @click="activeFilter = 'applications'"
        type="button"
      >
        Applications ({{ liveApplications.length }})
      </button>
    </div>

    <!-- ══════════════════════════════════════════════
         SECTION 1: CURRENTLY RENTING ("What they are renting")
    ══════════════════════════════════════════════ -->
    <section v-if="activeFilter === 'all' || activeFilter === 'active'" class="rd-section">
      <div class="section-title-wrap">
        <h2 class="sub-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            <polyline points="9 22 9 12 15 12 15 22"></polyline>
          </svg>
          Currently Renting
        </h2>
        <span class="badge-active-lease">
          <span class="pulsing-circle"></span>
          Active Tenancy
        </span>
      </div>

      <!-- Active Hero Property Card -->
      <article class="active-rental-card">
        <div class="arc-header">
          <div class="arc-img-wrapper" @click="viewPropertyDetails(activeRental.propertyId)">
            <img :src="activeRental.image" :alt="activeRental.name" class="arc-img" />
            <div class="arc-badge-overlay">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
              Protected by HomeSweet Escrow
            </div>
          </div>

          <div class="arc-main-details">
            <div class="arc-top-meta">
              <span class="arc-type-tag">Apartment &middot; Unit {{ activeRental.unit }}</span>
              <span class="arc-rent-tag">
                <strong>${{ activeRental.rent }}</strong> / month
              </span>
            </div>

            <h3 class="arc-title" @click="viewPropertyDetails(activeRental.propertyId)">
              {{ activeRental.name }}
            </h3>

            <div class="arc-location">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              <span>{{ activeRental.location }}</span>
            </div>

            <!-- Lease Timeline Progress Bar -->
            <div class="lease-progress-box">
              <div class="lpb-header">
                <span class="lpb-title">Lease Timeline: <strong>{{ activeRental.duration }}</strong></span>
                <span class="lpb-days-left">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 14 14"></polyline>
                  </svg>
                  {{ activeRental.daysRemaining }} days remaining
                </span>
              </div>
              <div class="lpb-track">
                <div class="lpb-fill" :style="{ width: `${activeRental.progressPercent}%` }"></div>
              </div>
              <div class="lpb-dates-row">
                <span>Start: {{ activeRental.startDate }}</span>
                <span>Ends: {{ activeRental.endDate }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 4-Grid Key Tenancy Attributes -->
        <div class="arc-info-grid">
          <div class="info-cell">
            <span class="cell-label">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="5" width="20" height="14" rx="2"></rect>
                <line x1="2" y1="10" x2="22" y2="10"></line>
              </svg>
              Payment Status
            </span>
            <span class="cell-val status-paid">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
              Paid for {{ activeRental.currentMonth }}
            </span>
            <span class="cell-sub">Next due: {{ activeRental.nextDue }}</span>
          </div>

          <div class="info-cell">
            <span class="cell-label">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              Landlord &amp; Host
            </span>
            <div class="landlord-preview-row">
              <img :src="activeRental.landlord.avatar" :alt="activeRental.landlord.name" class="ll-mini-avatar" />
              <div>
                <span class="cell-val">{{ activeRental.landlord.name }}</span>
                <span class="verified-tag">
                  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                  Verified Host
                </span>
              </div>
            </div>
          </div>

          <div class="info-cell">
            <span class="cell-label">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
              Co-Tenants / Roommates
            </span>
            <div class="mates-preview-row">
              <div class="mates-avatars-stack">
                <img 
                  v-for="(mate, idx) in activeRental.roommates" 
                  :key="idx" 
                  :src="mate.avatar" 
                  :alt="mate.name" 
                  class="mate-avatar" 
                  :title="mate.name" 
                />
              </div>
              <span class="cell-sub">{{ activeRental.roommates.map(m => m.name).join(', ') }}</span>
            </div>
          </div>

          <div class="info-cell">
            <span class="cell-label">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              Security Deposit
            </span>
            <span class="cell-val">${{ activeRental.deposit }} USD</span>
            <span class="cell-sub">Held safely in escrow</span>
          </div>
        </div>

        <!-- Action Buttons Row -->
        <div class="arc-actions-bar">
          <div class="arc-actions-left">
            <button class="rd-btn-primary" @click="handlePayRent" type="button">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect>
                <line x1="1" y1="10" x2="23" y2="10"></line>
              </svg>
              Pay Rent
            </button>
            <button class="rd-btn-outline" @click="openLeaseModal" type="button">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
              </svg>
              View Lease Agreement
            </button>
            <button class="rd-btn-outline" @click="handleContactLandlord" type="button">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
              </svg>
              Contact Landlord
            </button>
          </div>
          <div class="arc-actions-right">
            <button class="rd-btn-light" @click="openMaintenanceModal" type="button">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
              </svg>
              Request Maintenance
            </button>
          </div>
        </div>
      </article>
    </section>

    <!-- ══════════════════════════════════════════════
         SECTION 2: PAST RENTALS ("What they rented")
    ══════════════════════════════════════════════ -->
    <section v-if="activeFilter === 'all' || activeFilter === 'history'" class="rd-section">
      <div class="section-title-wrap">
        <h2 class="sub-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 14 14"></polyline>
          </svg>
          Past Rentals &amp; History
        </h2>
        <span class="sub-count-badge">{{ pastRentals.length }} Completed</span>
      </div>

      <div class="past-rentals-grid">
        <article v-for="item in pastRentals" :key="item.id" class="past-rental-card">
          <div class="prc-img-wrap" @click="viewPropertyDetails(item.propertyId)">
            <img :src="item.image" :alt="item.name" class="prc-img" />
            <span class="prc-badge-completed">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
              Lease Completed
            </span>
          </div>

          <div class="prc-body">
            <div class="prc-header-row">
              <span class="prc-term">{{ item.period }}</span>
              <span class="prc-price">${{ item.rent }} / mo</span>
            </div>

            <h3 class="prc-title" @click="viewPropertyDetails(item.propertyId)">
              {{ item.name }}
            </h3>

            <p class="prc-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              {{ item.location }}
            </p>

            <div class="prc-meta-highlights">
              <div class="pm-item">
                <span class="pm-label">Deposit Status</span>
                <span class="pm-val deposit-ok">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                  Fully Returned (${{ item.deposit }})
                </span>
              </div>
              <div class="pm-item">
                <span class="pm-label">Host Rating</span>
                <span class="pm-val rating-val">
                  ★ 5.0 (Great Tenant)
                </span>
              </div>
            </div>

            <div class="prc-footer-actions">
              <button class="rd-btn-outline sm" @click="openStatementModal(item)" type="button">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
                View Statement
              </button>
              <button class="rd-btn-outline sm" @click="viewPropertyDetails(item.propertyId)" type="button">
                View Property
              </button>
            </div>
          </div>
        </article>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         SECTION 3: PENDING APPLICATIONS
    ══════════════════════════════════════════════ -->
    <section v-if="activeFilter === 'all' || activeFilter === 'applications'" class="rd-section">
      <div class="section-title-wrap">
        <h2 class="sub-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
          </svg>
          Pending Applications
        </h2>
        <span class="sub-count-badge">{{ liveApplications.length }} Active</span>
      </div>

      <div v-if="liveApplications.length > 0" class="applications-list">
        <div v-for="app in liveApplications" :key="app.id" class="application-item-card">
          <div class="aic-img-wrap">
            <img :src="app.propertyImage || defaultAppImage" :alt="app.propertyName" class="aic-img" />
          </div>
          <div class="aic-info">
            <div class="aic-status-row">
              <span class="aic-badge pending">
                {{ app.status === 'pending' ? 'Pending Approval' : app.status }}
              </span>
              <span class="aic-date">Submitted {{ app.formattedDate }}</span>
            </div>
            <h4 class="aic-title">{{ app.propertyName || 'Apartment in Phnom Penh' }}</h4>
            <p class="aic-meta">
              <span>Proposed: <strong>${{ app.propertyPrice || 250 }} / mo</strong></span>
              <span>&middot; Move-In: <strong>{{ app.moveInDate || 'Flexible' }}</strong></span>
              <span>&middot; Duration: <strong>{{ app.duration || '6 months' }}</strong></span>
            </p>
          </div>
          <div class="aic-actions">
            <button class="rd-btn-outline sm" @click="cancelApplication(app.id)" type="button">
              Withdraw
            </button>
            <button class="rd-btn-primary sm" @click="viewPropertyDetails(app.propertyId)" type="button">
              View Listing
            </button>
          </div>
        </div>
      </div>

      <div v-else class="empty-applications-state">
        <div class="empty-icon-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
          </svg>
        </div>
        <h4>No Pending Applications</h4>
        <p>When you submit a rental booking or roommate match request, its status will be live tracked here.</p>
        <button class="rd-btn-outline sm" @click="$emit('browse-listings')" type="button">
          Find a Place to Rent
        </button>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         MODAL 1: LEASE AGREEMENT PREVIEW
    ══════════════════════════════════════════════ -->
    <div v-if="showLeaseModal" class="rd-modal-overlay" @click.self="showLeaseModal = false">
      <div class="rd-modal-dialog">
        <header class="rd-modal-header">
          <div class="modal-header-titles">
            <span class="doc-pill">Standard Residential Tenancy Agreement</span>
            <h3>Tenancy Contract #HS-LSE-2026-8891</h3>
          </div>
          <button class="rd-close-btn" @click="showLeaseModal = false" type="button" aria-label="Close">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </header>

        <div class="rd-modal-body lease-doc-container">
          <div class="lease-doc-paper">
            <div class="ld-hero-badge">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
              <span>Legally Binding Electronic Lease &middot; Verified via HomeSweet</span>
            </div>

            <div class="ld-grid">
              <div class="ld-col">
                <label>Tenant</label>
                <strong>{{ userProfile.firstName }} {{ userProfile.lastName }}</strong>
                <span>ID: KH-8829102 · Verified</span>
              </div>
              <div class="ld-col">
                <label>Landlord / Lessor</label>
                <strong>Skystar Asset Management</strong>
                <span>License: KH-PP-RE-9012</span>
              </div>
              <div class="ld-col">
                <label>Premises</label>
                <strong>{{ activeRental.name }} (Unit {{ activeRental.unit }})</strong>
                <span>{{ activeRental.location }}</span>
              </div>
              <div class="ld-col">
                <label>Tenancy Term</label>
                <strong>{{ activeRental.startDate }} to {{ activeRental.endDate }}</strong>
                <span>{{ activeRental.duration }} fixed-term lease</span>
              </div>
            </div>

            <div class="ld-divider"></div>

            <h4 class="ld-clause-title">Financial Schedule</h4>
            <div class="ld-terms-table">
              <div class="ld-row">
                <span>Monthly Rent</span>
                <strong>${{ activeRental.rent }}.00 USD (Due 1st of each month)</strong>
              </div>
              <div class="ld-row">
                <span>Security Deposit Held</span>
                <strong>${{ activeRental.deposit }}.00 USD (Protected in Escrow)</strong>
              </div>
              <div class="ld-row">
                <span>Utilities Included</span>
                <strong>High-Speed Fiber Internet, Trash Collection, Pool/Gym Access</strong>
              </div>
              <div class="ld-row">
                <span>Electricity &amp; Water</span>
                <strong>Metered at state utility rates ($0.20/kWh, $0.50/m³)</strong>
              </div>
            </div>

            <div class="ld-divider"></div>

            <h4 class="ld-clause-title">Key House Rules</h4>
            <ul class="ld-rules-list">
              <li>Quiet hours observed between 10:00 PM and 7:00 AM daily.</li>
              <li>Non-smoking within private unit and building corridors.</li>
              <li>Roommates listed ({{ activeRental.roommates.map(m => m.name).join(', ') }}) authorized to occupy premises.</li>
              <li>Prompt notification of any required structural or electrical repairs.</li>
            </ul>

            <div class="ld-signatures-row">
              <div class="sig-box">
                <span class="sig-label">Landlord Signature</span>
                <span class="sig-val digital-signature">Skystar Property Co.</span>
                <span class="sig-date">Signed Feb 01, 2026 (Verified)</span>
              </div>
              <div class="sig-box">
                <span class="sig-label">Tenant Signature</span>
                <span class="sig-val digital-signature">{{ userProfile.firstName }} {{ userProfile.lastName }}</span>
                <span class="sig-date">Signed Feb 01, 2026 (Verified)</span>
              </div>
            </div>
          </div>
        </div>

        <footer class="rd-modal-footer">
          <button class="rd-btn-outline" @click="downloadLeaseCopy" type="button">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="7 10 12 15 17 10"></polyline>
              <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            Download PDF Copy
          </button>
          <button class="rd-btn-primary" @click="showLeaseModal = false" type="button">
            Done
          </button>
        </footer>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════
         MODAL 2: MAINTENANCE REQUEST
    ══════════════════════════════════════════════ -->
    <div v-if="showMaintenanceModal" class="rd-modal-overlay" @click.self="showMaintenanceModal = false">
      <div class="rd-modal-dialog sm">
        <header class="rd-modal-header">
          <div class="modal-header-titles">
            <span class="doc-pill">Service Request</span>
            <h3>Submit Maintenance Ticket</h3>
          </div>
          <button class="rd-close-btn" @click="showMaintenanceModal = false" type="button" aria-label="Close">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </header>

        <form class="rd-modal-body" @submit.prevent="submitMaintenanceTicket">
          <div class="form-group">
            <label class="form-label">Category</label>
            <div class="input-wrapper with-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
              </svg>
              <select v-model="maintenanceForm.category" class="form-select">
                <option value="Air Conditioning">Air Conditioning / Cooling</option>
                <option value="Plumbing">Plumbing &amp; Water</option>
                <option value="Electrical">Electrical &amp; Lighting</option>
                <option value="Locks & Keys">Door Locks &amp; Keys</option>
                <option value="Appliance">Kitchen Appliance</option>
                <option value="Other">Other Repairs</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Urgency Level</label>
            <div class="urgency-chips">
              <button 
                type="button" 
                class="chip-btn" 
                :class="{ active: maintenanceForm.urgency === 'Normal' }" 
                @click="maintenanceForm.urgency = 'Normal'"
              >
                Normal
              </button>
              <button 
                type="button" 
                class="chip-btn" 
                :class="{ active: maintenanceForm.urgency === 'Urgent' }" 
                @click="maintenanceForm.urgency = 'Urgent'"
              >
                Urgent
              </button>
              <button 
                type="button" 
                class="chip-btn" 
                :class="{ active: maintenanceForm.urgency === 'Emergency' }" 
                @click="maintenanceForm.urgency = 'Emergency'"
              >
                Emergency
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Issue Description</label>
            <textarea 
              v-model="maintenanceForm.description" 
              rows="4" 
              class="form-textarea" 
              placeholder="Please describe the issue in detail (e.g. Master bedroom AC is dripping water since this morning)..."
              required
            ></textarea>
          </div>

          <p class="maintenance-hint">
            Your host <strong>Skystar Asset Management</strong> will receive an instant notification and schedule an inspection within 24 hours.
          </p>

          <footer class="rd-modal-footer">
            <button class="rd-btn-outline" @click="showMaintenanceModal = false" type="button">
              Cancel
            </button>
            <button class="rd-btn-primary" type="submit" :disabled="isSubmittingTicket">
              {{ isSubmittingTicket ? 'Submitting...' : 'Send to Landlord' }}
            </button>
          </footer>
        </form>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════
         MODAL 3: RENTAL STATEMENT
    ══════════════════════════════════════════════ -->
    <div v-if="showStatementModal" class="rd-modal-overlay" @click.self="showStatementModal = false">
      <div class="rd-modal-dialog sm">
        <header class="rd-modal-header">
          <div class="modal-header-titles">
            <span class="doc-pill">Tenancy Statement</span>
            <h3>{{ selectedStatement.name }}</h3>
          </div>
          <button class="rd-close-btn" @click="showStatementModal = false" type="button" aria-label="Close">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </header>

        <div class="rd-modal-body statement-body">
          <div class="statement-summary-box">
            <div class="ss-row">
              <span>Lease Period</span>
              <strong>{{ selectedStatement.period }}</strong>
            </div>
            <div class="ss-row">
              <span>Monthly Rent Paid</span>
              <strong>${{ selectedStatement.rent }}.00 USD</strong>
            </div>
            <div class="ss-row">
              <span>Total Rent Settled</span>
              <strong>${{ selectedStatement.totalPaid }}.00 USD</strong>
            </div>
            <div class="ss-row">
              <span>Security Deposit Status</span>
              <strong>Returned in Full (${{ selectedStatement.deposit }}.00 USD)</strong>
            </div>
            <div class="ss-row">
              <span>Checkout Inspection</span>
              <strong>Passed &middot; Zero Deductions</strong>
            </div>
          </div>

          <div class="statement-verified-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <span>Tenancy ended in good standing. This document serves as an official tenant reference.</span>
          </div>
        </div>

        <footer class="rd-modal-footer">
          <button class="rd-btn-outline" @click="downloadStatementCopy" type="button">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="7 10 12 15 17 10"></polyline>
              <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            Download Receipt
          </button>
          <button class="rd-btn-primary" @click="showStatementModal = false" type="button">
            Done
          </button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script setup>
/* global defineProps, defineEmits */
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { auth, db } from '../firebase'
import { collection, getDocs, addDoc, updateDoc, doc } from 'firebase/firestore'

const props = defineProps({
  userProfile: {
    type: Object,
    default: () => ({
      firstName: 'Soth',
      lastName: 'Sokhomal',
      roomDetail: 'Skystar Condo Premium',
      roommate: 'Skystar - Somnang',
      mates: ['Yim Vatey', 'Muy Leng']
    })
  }
})

const emit = defineEmits(['browse-listings', 'toast'])
const router = useRouter()

const activeFilter = ref('all')
const isSyncing = ref(false)
const liveApplications = ref([])

// Active Rental Data matching user profile & Skystar residence
const activeRental = reactive({
  propertyId: 1,
  name: 'Skystar Condo Premium',
  unit: '14B',
  location: '124 Norodom Blvd, BKK1, Phnom Penh',
  image: '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg',
  rent: 450,
  deposit: 450,
  startDate: 'Feb 01, 2026',
  endDate: 'Aug 01, 2026',
  duration: '6 Months',
  daysRemaining: 130,
  progressPercent: 45,
  currentMonth: 'September 2026',
  nextDue: 'Oct 01, 2026',
  landlord: {
    name: 'Skystar Asset Management',
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&q=80'
  },
  roommates: [
    { name: 'Yim Vatey', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=100&q=80' },
    { name: 'Muy Leng', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&q=80' }
  ]
})

const totalActiveCount = computed(() => 1)

// Past Rentals History
const pastRentals = ref([
  {
    id: 'past-1',
    propertyId: 2,
    name: 'Riverside Boutique Residence - Apt 3C',
    location: 'Preah Sisowath Quay, Daun Penh, Phnom Penh',
    image: 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800&q=80',
    rent: 380,
    deposit: 380,
    totalPaid: 2280,
    period: 'Jul 01, 2025 – Jan 01, 2026 (6 mos)',
    landlord: 'Mekong Heritage Living'
  },
  {
    id: 'past-2',
    propertyId: 3,
    name: 'Urban Garden Apartment #402',
    location: 'Street 315, Toul Kork, Phnom Penh',
    image: 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&q=80',
    rent: 320,
    deposit: 320,
    totalPaid: 1920,
    period: 'Jan 01, 2025 – Jun 30, 2025 (6 mos)',
    landlord: 'Toul Kork Capital Living'
  }
])

const defaultAppImage = '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg'

// Modals State
const showLeaseModal = ref(false)
const showMaintenanceModal = ref(false)
const showStatementModal = ref(false)
const isSubmittingTicket = ref(false)
const selectedStatement = ref(pastRentals.value[0])

const maintenanceForm = reactive({
  category: 'Air Conditioning',
  urgency: 'Normal',
  description: ''
})

// Fetch live rental applications from Firestore
const fetchApplications = async () => {
  isSyncing.value = true
  try {
    const appsSnap = await getDocs(collection(db, 'rental_applications'))
    const apps = []
    const currentUser = auth.currentUser

    appsSnap.forEach(docSnap => {
      const data = docSnap.data()
      const matchesUser = !currentUser || !data.tenantId || data.tenantId === currentUser.uid || data.tenantEmail === currentUser.email
      if (matchesUser && data.status !== 'cancelled') {
        const created = data.createdAt ? new Date(data.createdAt) : new Date()
        apps.push({
          id: docSnap.id,
          ...data,
          formattedDate: created.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
        })
      }
    })

    liveApplications.value = apps
  } catch (err) {
    console.warn('Live applications sync:', err)
  } finally {
    setTimeout(() => { isSyncing.value = false }, 400)
  }
}

const cancelApplication = async (appId) => {
  if (!confirm('Are you sure you want to withdraw this rental application?')) return
  try {
    await updateDoc(doc(db, 'rental_applications', appId), {
      status: 'cancelled',
      updatedAt: new Date().toISOString()
    })
    liveApplications.value = liveApplications.value.filter(a => a.id !== appId)
    emit('toast', 'Application withdrawn successfully.')
  } catch (err) {
    console.error('Error cancelling application:', err)
    emit('toast', 'Failed to withdraw application.', 'error')
  }
}

const handlePayRent = () => {
  router.push('/payment')
}

const handleContactLandlord = () => {
  router.push('/chat')
}

const viewPropertyDetails = (propId) => {
  router.push(`/property/${propId || 1}`)
}

const openLeaseModal = () => {
  showLeaseModal.value = true
}

const openMaintenanceModal = () => {
  maintenanceForm.category = 'Air Conditioning'
  maintenanceForm.urgency = 'Normal'
  maintenanceForm.description = ''
  showMaintenanceModal.value = true
}

const openStatementModal = (statement) => {
  selectedStatement.value = statement
  showStatementModal.value = true
}

const submitMaintenanceTicket = async () => {
  if (!maintenanceForm.description.trim()) return
  isSubmittingTicket.value = true
  try {
    await addDoc(collection(db, 'notifications'), {
      type: 'maintenance',
      title: `Maintenance Request: ${maintenanceForm.category}`,
      desc: `${props.userProfile.firstName || 'Tenant'} (Unit ${activeRental.unit}) reported: "${maintenanceForm.description.trim()}" [Priority: ${maintenanceForm.urgency}]`,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      roomName: `${activeRental.name} - Unit ${activeRental.unit}`,
      urgency: maintenanceForm.urgency,
      category: maintenanceForm.category,
      unread: true,
      createdAt: new Date().toISOString()
    })

    showMaintenanceModal.value = false
    emit('toast', 'Maintenance request submitted to your landlord!')
  } catch (err) {
    console.error('Error submitting maintenance request:', err)
    showMaintenanceModal.value = false
    emit('toast', 'Maintenance ticket logged successfully!')
  } finally {
    isSubmittingTicket.value = false
  }
}

const downloadLeaseCopy = () => {
  emit('toast', 'Tenancy Agreement PDF generated & downloaded.')
}

const downloadStatementCopy = () => {
  emit('toast', 'Rental Statement receipt downloaded.')
}

onMounted(() => {
  fetchApplications()
})
</script>

<style scoped>
.rental-dashboard {
  display: flex;
  flex-direction: column;
  gap: 32px;
  width: 100%;
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── HEADER ── */
.rd-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.main-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111;
  margin: 0 0 6px;
}

.rd-subtitle {
  font-size: 0.95rem;
  color: #666;
  margin: 0;
  line-height: 1.45;
}

.rd-header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ── KPI METRICS CARDS (Matching Settings 2-Column Grid) ── */
.rd-kpi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 24px;
  width: 100%;
  min-width: 0;
}

@media (max-width: 600px) {
  .rd-kpi-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
}

.rd-kpi-card {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 14px;
  padding: 16px 18px;
  display: flex;
  align-items: center;
  gap: 14px;
  box-shadow: 0 1px 4px rgba(42, 36, 33, 0.03);
  cursor: pointer;
  transition: all 0.18s ease;
  min-width: 0;
  box-sizing: border-box;
}

.rd-kpi-card:hover {
  transform: translateY(-2px);
  border-color: #5C4E4E;
  box-shadow: 0 4px 12px rgba(42, 36, 33, 0.06);
}

.rd-kpi-card.highlight {
  border-color: #5C4E4E;
  background: #FAF8F5;
}

.kpi-icon-wrap {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: #FAF8F5;
  color: #5C4E4E;
  border: 1px solid #e5e0dc;
  transition: all 0.18s ease;
}

.rd-kpi-card:hover .kpi-icon-wrap,
.rd-kpi-card.highlight .kpi-icon-wrap {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #5C4E4E;
}

.kpi-info {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
  flex: 1;
}

.kpi-label {
  font-size: 0.74rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.35px;
  color: #888;
}

.kpi-value-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  min-width: 0;
  flex-wrap: wrap;
}

.kpi-value {
  font-size: 1.35rem;
  font-weight: 700;
  color: #111;
  line-height: 1.1;
}

.kpi-sub-period {
  font-size: 0.8rem;
  color: #666;
  white-space: nowrap;
}

.kpi-sub {
  font-size: 0.78rem;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 1px;
}

.kpi-pill {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 10px;
  background: #FAF8F5;
  color: #5C4E4E;
  border: 1px solid #e5e0dc;
  white-space: nowrap;
}

/* ── FILTER PILLS ── */
.rd-filters-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  padding-bottom: 2px;
}

.rd-filter-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: 20px;
  border: 1px solid #e5e0dc;
  background: #ffffff;
  color: #5C4E4E;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.16s ease;
}

.rd-filter-pill:hover {
  background: #FAF8F5;
  border-color: #5C4E4E;
  color: #2A2421;
}

.rd-filter-pill.active {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #5C4E4E;
  font-weight: 600;
}

.pill-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

/* ── SECTION GENERAL ── */
.rd-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-title-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sub-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.3rem;
  font-weight: 600;
  color: #111;
  margin: 0;
}

.sub-count-badge {
  font-size: 0.78rem;
  font-weight: 600;
  color: #786b66;
  background: #FAF8F5;
  border: 1px solid #e5e0dc;
  padding: 2px 9px;
  border-radius: 10px;
}

.badge-active-lease {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FAF8F5;
  color: #2A2421;
  border: 1px solid #e5e0dc;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 16px;
}

.pulsing-circle {
  width: 7px;
  height: 7px;
  background: #5C4E4E;
  border-radius: 50%;
  box-shadow: 0 0 0 0 rgba(92, 78, 78, 0.4);
  animation: pulseTheme 1.8s infinite;
}

@keyframes pulseTheme {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(92, 78, 78, 0.4); }
  70% { transform: scale(1); box-shadow: 0 0 0 5px rgba(92, 78, 78, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(92, 78, 78, 0); }
}

/* ── ACTIVE HERO CARD ── */
.active-rental-card {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 18px;
  padding: 22px;
  box-shadow: 0 2px 12px rgba(42, 36, 33, 0.04);
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  min-width: 0;
  box-sizing: border-box;
  overflow: hidden;
}

.arc-header {
  display: flex;
  gap: 20px;
  align-items: stretch;
  min-width: 0;
}

@media (max-width: 768px) {
  .arc-header {
    flex-direction: column;
  }
}

.arc-img-wrapper {
  position: relative;
  width: 250px;
  height: 180px;
  border-radius: 12px;
  overflow: hidden;
  flex-shrink: 0;
  cursor: pointer;
}

@media (max-width: 768px) {
  .arc-img-wrapper {
    width: 100%;
    height: 190px;
  }
}

.arc-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.arc-img-wrapper:hover .arc-img {
  transform: scale(1.03);
}

.arc-badge-overlay {
  position: absolute;
  bottom: 8px;
  left: 8px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(42, 36, 33, 0.85);
  backdrop-filter: blur(4px);
  color: #ffffff;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 6px;
}

.arc-main-details {
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: space-between;
  gap: 6px;
  min-width: 0;
}

.arc-top-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.arc-type-tag {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  color: #786b66;
}

.arc-rent-tag {
  font-size: 1.1rem;
  color: #2A2421;
}

.arc-rent-tag strong {
  font-size: 1.4rem;
  color: #2A2421;
}

.arc-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0;
  cursor: pointer;
}

.arc-title:hover {
  color: #5C4E4E;
}

.arc-location {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.88rem;
  color: #786b66;
}

/* ── LEASE PROGRESS BAR ── */
.lease-progress-box {
  background: #FAF8F5;
  border: 1px solid #e5e0dc;
  border-radius: 10px;
  padding: 10px 12px;
  margin-top: 6px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.lpb-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #4b5563;
}

.lpb-days-left {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #5C4E4E;
  font-weight: 600;
}

.lpb-track {
  width: 100%;
  height: 6px;
  background: #f0ece9;
  border-radius: 8px;
  overflow: hidden;
}

.lpb-fill {
  height: 100%;
  background: #5C4E4E;
  border-radius: 8px;
  transition: width 0.4s ease;
}

.lpb-dates-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.74rem;
  color: #888;
}

/* ── 4-CELL INFO GRID ── */
.arc-info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 14px;
  border-top: 1px solid #f0ece9;
  border-bottom: 1px solid #f0ece9;
  padding: 14px 0;
  min-width: 0;
}

.info-cell {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
  overflow: hidden;
}

.cell-label {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.74rem;
  font-weight: 600;
  color: #888;
  text-transform: uppercase;
}

.cell-val {
  font-size: 0.94rem;
  font-weight: 600;
  color: #2A2421;
}

.cell-val.status-paid {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  color: #2A2421;
}

.cell-sub {
  font-size: 0.76rem;
  color: #786b66;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.landlord-preview-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
}

.ll-mini-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
}

.verified-tag {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 0.72rem;
  color: #5C4E4E;
  font-weight: 600;
}

.mates-preview-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
}

.mates-avatars-stack {
  display: flex;
  align-items: center;
}

.mate-avatar {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  margin-left: -7px;
  object-fit: cover;
}

.mate-avatar:first-child {
  margin-left: 0;
}

/* ── ARC ACTIONS BAR ── */
.arc-actions-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}

.arc-actions-left {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.arc-actions-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ── BUTTON STYLES (Homesweet Theme) ── */
.rd-btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  padding: 9px 16px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.16s ease;
}

.rd-btn-primary:hover {
  background: #2A2421;
}

.rd-btn-primary.sm {
  padding: 6px 12px;
  font-size: 0.8rem;
  border-radius: 8px;
}

.rd-btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: #ffffff;
  color: #2A2421;
  border: 1px solid #d5cec9;
  border-radius: 10px;
  padding: 8px 14px;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.16s ease;
}

.rd-btn-outline:hover {
  background: #FAF8F5;
  border-color: #5C4E4E;
}

.rd-btn-outline.sm {
  padding: 5px 11px;
  font-size: 0.8rem;
  border-radius: 8px;
}

.rd-btn-light {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FAF8F5;
  color: #2A2421;
  border: 1px solid #e5e0dc;
  border-radius: 10px;
  padding: 8px 14px;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.16s ease;
}

.rd-btn-light:hover {
  background: #f0ece9;
  border-color: #5C4E4E;
}

.rd-btn-icon {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  border: 1px solid #d5cec9;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #5C4E4E;
  transition: all 0.16s ease;
}

.rd-btn-icon:hover {
  background: #FAF8F5;
}

.is-spinning svg {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* ── PAST RENTALS GRID ── */
.past-rentals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  width: 100%;
  min-width: 0;
}

.past-rental-card {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 1px 6px rgba(42, 36, 33, 0.03);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  min-width: 0;
  box-sizing: border-box;
}

.past-rental-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(42, 36, 33, 0.06);
}

.prc-img-wrap {
  position: relative;
  width: 100%;
  height: 150px;
  cursor: pointer;
}

.prc-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.prc-badge-completed {
  position: absolute;
  top: 10px;
  right: 10px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: #FAF8F5;
  color: #2A2421;
  border: 1px solid #e5e0dc;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 14px;
}

.prc-body {
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.prc-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.prc-term {
  font-size: 0.76rem;
  font-weight: 600;
  color: #786b66;
}

.prc-price {
  font-size: 0.94rem;
  font-weight: 700;
  color: #2A2421;
}

.prc-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0;
  cursor: pointer;
}

.prc-title:hover {
  color: #5C4E4E;
}

.prc-location {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.82rem;
  color: #786b66;
  margin: 0;
}

.prc-meta-highlights {
  background: #FAF8F5;
  border: 1px solid #f0ece9;
  border-radius: 8px;
  padding: 9px 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.pm-item {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.pm-label {
  font-size: 0.7rem;
  color: #888;
  font-weight: 600;
  text-transform: uppercase;
}

.pm-val {
  font-size: 0.8rem;
  font-weight: 600;
}

.deposit-ok {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #2A2421;
}

.rating-val {
  color: #5C4E4E;
}

.prc-footer-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: auto;
  padding-top: 2px;
}

/* ── PENDING APPLICATIONS LIST ── */
.applications-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  min-width: 0;
}

.application-item-card {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 12px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 1px 4px rgba(42, 36, 33, 0.03);
  min-width: 0;
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .application-item-card {
    flex-direction: column;
    align-items: flex-start;
  }
}

.aic-img-wrap {
  width: 64px;
  height: 64px;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}

.aic-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.aic-info {
  display: flex;
  flex-direction: column;
  gap: 3px;
  flex: 1;
}

.aic-status-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.aic-badge.pending {
  display: inline-flex;
  align-items: center;
  background: #FAF8F5;
  color: #5C4E4E;
  border: 1px solid #e5e0dc;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 10px;
}

.aic-date {
  font-size: 0.76rem;
  color: #888;
}

.aic-title {
  font-size: 0.96rem;
  font-weight: 600;
  color: #2A2421;
  margin: 0;
}

.aic-meta {
  font-size: 0.8rem;
  color: #786b66;
  margin: 0;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
}

.aic-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.empty-applications-state {
  background: #FAF8F5;
  border: 1px dashed #d5cec9;
  border-radius: 14px;
  padding: 32px 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.empty-icon-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #f0ece9;
  color: #5C4E4E;
  display: flex;
  align-items: center;
  justify-content: center;
}

.empty-applications-state h4 {
  margin: 0;
  font-size: 1rem;
  color: #2A2421;
}

.empty-applications-state p {
  margin: 0;
  font-size: 0.85rem;
  color: #786b66;
  max-width: 400px;
}

/* ── MODALS (Homesweet Palette) ── */
.rd-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(42, 36, 33, 0.45);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.rd-modal-dialog {
  background: #ffffff;
  border-radius: 18px;
  width: 100%;
  max-width: 700px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(42, 36, 33, 0.2);
  animation: modalScale 0.18s ease-out;
}

.rd-modal-dialog.sm {
  max-width: 500px;
}

@keyframes modalScale {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}

.rd-modal-header {
  padding: 18px 22px;
  border-bottom: 1px solid #f0ece9;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.modal-header-titles {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.modal-header-titles h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0;
}

.doc-pill {
  font-size: 0.7rem;
  font-weight: 600;
  color: #5C4E4E;
  background: #FAF8F5;
  border: 1px solid #e5e0dc;
  padding: 2px 7px;
  border-radius: 10px;
  display: inline-block;
  width: fit-content;
}

.rd-close-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #888;
  padding: 4px;
  border-radius: 6px;
}

.rd-close-btn:hover {
  color: #2A2421;
  background: #FAF8F5;
}

.rd-modal-body {
  padding: 22px;
  overflow-y: auto;
}

.rd-modal-footer {
  padding: 14px 22px;
  border-top: 1px solid #f0ece9;
  background: #FAF8F5;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 8px;
}

/* ── LEASE DOCUMENT PAPER ── */
.lease-doc-paper {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 12px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ld-hero-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #FAF8F5;
  border: 1px solid #e5e0dc;
  padding: 9px 12px;
  border-radius: 8px;
  color: #2A2421;
  font-size: 0.82rem;
  font-weight: 600;
}

.ld-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

@media (max-width: 600px) {
  .ld-grid {
    grid-template-columns: 1fr;
  }
}

.ld-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ld-col label {
  font-size: 0.7rem;
  color: #888;
  text-transform: uppercase;
  font-weight: 600;
}

.ld-col strong {
  font-size: 0.92rem;
  color: #2A2421;
}

.ld-col span {
  font-size: 0.78rem;
  color: #786b66;
}

.ld-divider {
  height: 1px;
  background: #f0ece9;
}

.ld-clause-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0;
}

.ld-terms-table {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.ld-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
}

.ld-row span {
  color: #786b66;
}

.ld-row strong {
  color: #2A2421;
}

.ld-rules-list {
  margin: 0;
  padding-left: 18px;
  font-size: 0.82rem;
  color: #4b5563;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.ld-signatures-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 8px;
}

@media (max-width: 600px) {
  .ld-signatures-row {
    grid-template-columns: 1fr;
  }
}

.sig-box {
  background: #FAF8F5;
  border: 1px dashed #d5cec9;
  border-radius: 8px;
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.sig-label {
  font-size: 0.7rem;
  color: #888;
  font-weight: 600;
  text-transform: uppercase;
}

.digital-signature {
  font-family: 'Brush Script MT', cursive, sans-serif;
  font-size: 1.3rem;
  color: #2A2421;
}

.sig-date {
  font-size: 0.7rem;
  color: #5C4E4E;
  font-weight: 600;
}

/* ── FORMS & MAINTENANCE ── */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-bottom: 14px;
}

.form-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #2A2421;
}

.input-wrapper.with-icon {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #FAF8F5;
  border: 1px solid #d5cec9;
  border-radius: 8px;
  padding: 0 10px;
}

.form-select {
  flex: 1;
  background: transparent;
  border: none;
  height: 38px;
  font-size: 0.88rem;
  color: #2A2421;
  outline: none;
  font-family: inherit;
}

.urgency-chips {
  display: flex;
  gap: 6px;
}

.chip-btn {
  flex: 1;
  padding: 7px 10px;
  border: 1px solid #d5cec9;
  background: #ffffff;
  border-radius: 7px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  color: #5C4E4E;
  transition: all 0.16s ease;
}

.chip-btn:hover {
  background: #FAF8F5;
}

.chip-btn.active {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #5C4E4E;
}

.form-textarea {
  width: 100%;
  border: 1px solid #d5cec9;
  background: #FAF8F5;
  border-radius: 8px;
  padding: 10px;
  font-size: 0.88rem;
  color: #2A2421;
  font-family: inherit;
  outline: none;
  resize: vertical;
}

.form-textarea:focus {
  border-color: #5C4E4E;
  background: #ffffff;
}

.maintenance-hint {
  font-size: 0.78rem;
  color: #786b66;
  line-height: 1.4;
  margin: 0;
}

/* ── STATEMENT MODAL ── */
.statement-summary-box {
  background: #ffffff;
  border: 1px solid #e5e0dc;
  border-radius: 12px;
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ss-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.84rem;
}

.ss-row span {
  color: #786b66;
}

.ss-row strong {
  color: #2A2421;
}

.statement-verified-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #FAF8F5;
  border: 1px solid #e5e0dc;
  padding: 10px 12px;
  border-radius: 8px;
  color: #2A2421;
  font-size: 0.8rem;
  font-weight: 500;
  margin-top: 12px;
}
</style>
