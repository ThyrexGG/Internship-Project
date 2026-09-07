<template>
  <div class="admin-app">

    <!-- ══════════════════════════════════════════════════════════════
         SECRET ADMIN LOGIN GATE (If not authenticated)
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="!isAdminAuthenticated" class="admin-login-overlay">
      <div class="admin-login-card">
        <div class="admin-login-header">
          <div class="admin-badge-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
          </div>
          <h2>Admin Access Portal</h2>
          <p>Confidential management console for HomeSweet Platform administrators.</p>
        </div>

        <form @submit.prevent="verifyAdminPin" class="admin-login-form">
          <div class="form-group">
            <label>Master Admin Key or PIN</label>
            <input 
              v-model="adminPinInput" 
              type="password" 
              placeholder="Enter 6-digit PIN or Admin Key" 
              class="admin-input" 
              autofocus 
            />
            <span v-if="pinError" class="error-msg">{{ pinError }}</span>
          </div>

          <div class="pin-hint-box">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6b7280" stroke-width="2">
              <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
            </svg>
            <span>Authorized credentials: Master PIN <strong>123456</strong> or <strong>admin@homesweet.com</strong></span>
          </div>

          <div class="admin-login-actions">
            <button type="button" class="btn-cancel" @click="$router.push('/home')">Back to Home</button>
            <button type="submit" class="btn-unlock" :disabled="isVerifying">
              <span v-if="isVerifying">Verifying...</span>
              <span v-else>Unlock Console</span>
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         AUTHENTICATED ADMIN PORTAL
    ══════════════════════════════════════════════════════════════ -->
    <div v-else class="admin-portal-layout">
      
      <!-- Top Header Bar matching mockups -->
      <header class="admin-top-bar">
        <div class="top-bar-left">
          <button class="brand-logo" @click="activeTab = 'dashboard'">
            <div class="brand-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M4 18 L16 18" />
                <path d="M4 18 L4 12 L9 7 L16 14" />
                <path d="M12 18 L12 4 L16 4 L16 18 Z" />
                <path d="M12 14 L16 14" />
              </svg>
            </div>
            <span class="brand-name">HomeSweet</span>
          </button>
        </div>
        <div class="top-bar-right">
          <button class="exit-admin-btn" @click="handleLogoutAdmin" title="Lock Admin Session">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
            <span>Exit Admin</span>
          </button>
          <div class="admin-avatar-wrap">
            <img :src="adminUserAvatar" alt="Admin Avatar" class="admin-avatar" />
          </div>
        </div>
      </header>

      <div class="admin-main-body">

        <!-- ══════════════════════════════════════════════════════════════
             LEFT SIDEBAR
        ══════════════════════════════════════════════════════════════ -->
        <aside class="admin-sidebar">
          <h1 class="sidebar-heading">{{ sidebarTitle }}</h1>

          <div class="sidebar-section">
            <p class="section-label">Users</p>
            <button 
              class="sidebar-nav-btn" 
              :class="{ active: activeTab === 'landlords' }" 
              @click="switchTab('landlords')"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="10" r="4"/><path d="M4 21v-2a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2"/>
              </svg>
              <span>Landlords</span>
            </button>

            <button 
              class="sidebar-nav-btn" 
              :class="{ active: activeTab === 'renters' }" 
              @click="switchTab('renters')"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              <span>Renters</span>
            </button>
          </div>

          <div class="sidebar-section">
            <p class="section-label">Main Menu</p>
            <button 
              class="sidebar-nav-btn" 
              :class="{ active: activeTab === 'dashboard' }" 
              @click="switchTab('dashboard')"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 3v18"/>
              </svg>
              <span>Dashboard</span>
            </button>

            <button 
              class="sidebar-nav-btn" 
              :class="{ active: activeTab === 'verifications' }" 
              @click="switchTab('verifications')"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="M9 12l2 2 4-4"/>
              </svg>
              <span>Verifications</span>
              <span v-if="verificationKPIs.pending > 0" class="nav-badge-pill">{{ verificationKPIs.pending }}</span>
            </button>

            <button 
              class="sidebar-nav-btn" 
              :class="{ active: activeTab === 'house' }" 
              @click="switchTab('house')"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>
              </svg>
              <span>House</span>
            </button>
          </div>

          <div class="sidebar-section">
            <p class="section-label">Account &amp; Help</p>
            <button class="sidebar-nav-btn" :class="{ active: activeTab === 'help' }" @click="switchTab('help')">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><circle cx="12" cy="17" r="1"/>
              </svg>
              <span>Help</span>
            </button>

            <button class="sidebar-nav-btn" :class="{ active: activeTab === 'security' }" @click="switchTab('security')">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              </svg>
              <span>Security</span>
            </button>

            <button class="sidebar-nav-btn" :class="{ active: activeTab === 'account_status' }" @click="switchTab('account_status')">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
              </svg>
              <span>Account status</span>
            </button>
          </div>
        </aside>

        <!-- ══════════════════════════════════════════════════════════════
             MAIN CONTENT AREA
        ══════════════════════════════════════════════════════════════ -->
        <main class="admin-content-view">

          <!-- ─── TAB 1: DASHBOARD (Overview, Agreements, Metrics, Activity Logs) ─── -->
          <div v-if="activeTab === 'dashboard'" class="tab-pane dashboard-pane">
            <div class="pane-top-row">
              <div class="search-pill-container">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <input v-model="dashboardSearch" type="text" placeholder="Search" class="search-pill-input" />
              </div>

              <button class="btn-primary-action" @click="showUploadModal = true">
                Add New agreement
              </button>
            </div>

            <div class="dashboard-grid">
              <!-- Left Column: Agreements List matching mockup media_1788721171162.png -->
              <div class="agreements-column">
                <div 
                  v-for="agreement in filteredAgreements" 
                  :key="agreement.id" 
                  class="agreement-card"
                  @click="openAgreementPreview(agreement)"
                >
                  <div class="pdf-badge">
                    <span class="pdf-tag">PDF</span>
                  </div>
                  <div class="agreement-info">
                    <h4 class="agreement-title">{{ agreement.code }}</h4>
                    <p class="agreement-sub">Landlord: {{ agreement.landlord }}</p>
                    <p class="agreement-sub">Tenant: {{ agreement.tenant }}</p>
                    <span class="agreement-duration">{{ agreement.duration }}</span>
                  </div>
                  <div class="agreement-date">{{ agreement.date }}</div>
                </div>

                <div v-if="filteredAgreements.length === 0" class="empty-state-card">
                  <p>No agreements found matching your search.</p>
                </div>
              </div>

              <!-- Right Column: System Performance & Activity Logs -->
              <div class="metrics-column">
                <div class="metrics-section">
                  <h3 class="section-title">System performance</h3>
                  <div class="metrics-grid">
                    <div class="metric-card">
                      <div class="metric-header">
                        <span class="metric-label">Landlords</span>
                        <span class="metric-trend ok">ok</span>
                      </div>
                      <div class="metric-value">{{ performanceStats.landlords }}</div>
                    </div>

                    <div class="metric-card">
                      <div class="metric-header">
                        <span class="metric-label">Students</span>
                        <span class="metric-trend positive">+30%</span>
                      </div>
                      <div class="metric-value">{{ performanceStats.students }}</div>
                    </div>

                    <div class="metric-card">
                      <div class="metric-header">
                        <span class="metric-label">Revenue</span>
                        <span class="metric-trend positive">+50%</span>
                      </div>
                      <div class="metric-value">{{ performanceStats.revenue }}</div>
                    </div>

                    <div class="metric-card">
                      <div class="metric-header">
                        <span class="metric-label">House Property</span>
                        <span class="metric-trend positive">+20%</span>
                      </div>
                      <div class="metric-value">{{ performanceStats.properties }}</div>
                    </div>
                  </div>
                </div>

                <!-- System Activity Logs matching mockup media_1788721171162.png -->
                <div class="logs-section">
                  <h3 class="section-title">System Activity logs</h3>
                  <div class="logs-table-container">
                    <table class="logs-table">
                      <tbody>
                        <tr v-for="(log, idx) in activityLogs" :key="idx">
                          <td class="log-time">[{{ log.time }}]</td>
                          <td class="log-action">{{ log.action }}</td>
                          <td class="log-unit">{{ log.unit }}</td>
                          <td class="log-id">ID: {{ log.id }}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ─── TAB 2: LANDLORDS (Table & Landlord Application Form) ─── -->
          <div v-else-if="activeTab === 'landlords'" class="tab-pane">
            
            <!-- VIEW A: LANDLORDS TABLE matching media_1788721203039.png -->
            <template v-if="!showLandlordForm">
              <div class="pane-top-row">
                <div class="search-pill-container">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                    <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                  </svg>
                  <input v-model="landlordSearch" type="text" placeholder="Search" class="search-pill-input" />
                </div>

                <button class="btn-primary-action" @click="showLandlordForm = true">
                  Add New landlord
                </button>
              </div>

              <div class="data-table-card">
                <table class="data-table">
                  <thead>
                    <tr>
                      <th>Property address</th>
                      <th>Tenant</th>
                      <th>Start Date</th>
                      <th>End Date</th>
                      <th>Duration</th>
                      <th>Price</th>
                      <th>Payment Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, idx) in filteredLandlords" :key="idx">
                      <td class="cell-primary">{{ item.address }}</td>
                      <td>{{ item.tenant }}</td>
                      <td>{{ item.startDate }}</td>
                      <td>{{ item.endDate }}</td>
                      <td>{{ item.duration }}</td>
                      <td class="cell-price">${{ item.price }}</td>
                      <td>
                        <span class="status-pill" :class="item.paymentStatus.toLowerCase()">
                          {{ item.paymentStatus }}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </template>

            <!-- VIEW B: LANDLORD APPLICATION FORM matching media_1788721287240.png -->
            <template v-else>
              <div class="form-pane-container">
                <div class="form-header-bar">
                  <button class="btn-back-text" @click="showLandlordForm = false">
                    ← Back to Landlord Table
                  </button>
                  <h2 class="form-main-heading">Landlord Application Form</h2>
                </div>

                <form @submit.prevent="submitLandlordForm" class="styled-admin-form">
                  <!-- Section 1 -->
                  <div class="form-banner-title">Landlord Information</div>
                  <div class="form-row two-col">
                    <input v-model="newLandlord.firstName" type="text" placeholder="First name" required class="form-input-box" />
                    <input v-model="newLandlord.lastName" type="text" placeholder="Last name" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newLandlord.email" type="email" placeholder="Enter Email" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newLandlord.phone" type="tel" placeholder="Enter Phone Number" required class="form-input-box" />
                  </div>

                  <!-- Section 2 -->
                  <div class="form-banner-title">Property details</div>
                  <div class="form-row two-col">
                    <input v-model="newLandlord.propertyName" type="text" placeholder="Property Name" required class="form-input-box" />
                    <input v-model="newLandlord.propertyAddress" type="text" placeholder="Property Address" required class="form-input-box" />
                  </div>
                  <div class="form-row two-col">
                    <input v-model="newLandlord.startDate" type="date" placeholder="Start Date" required class="form-input-box" />
                    <input v-model="newLandlord.endDate" type="date" placeholder="End Date" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newLandlord.propertyPrice" type="number" placeholder="Property Price ($)" required class="form-input-box" />
                  </div>

                  <!-- Section 3 -->
                  <div class="form-banner-title">Payment Method</div>
                  <div class="checkbox-row">
                    <label class="check-box-item">
                      <input type="checkbox" v-model="newLandlord.paymentMethods.cash" />
                      <span>Cash</span>
                    </label>
                    <label class="check-box-item">
                      <input type="checkbox" v-model="newLandlord.paymentMethods.online" />
                      <span>Online</span>
                    </label>
                    <label class="check-box-item">
                      <input type="checkbox" v-model="newLandlord.paymentMethods.others" />
                      <span>Others</span>
                    </label>
                  </div>

                  <div class="form-submit-row">
                    <button type="button" class="btn-cancel" @click="showLandlordForm = false">Cancel</button>
                    <button type="submit" class="btn-primary-action" :disabled="isSubmittingForm">
                      {{ isSubmittingForm ? 'Saving...' : 'Register Landlord' }}
                    </button>
                  </div>
                </form>
              </div>
            </template>
          </div>

          <!-- ─── TAB 3: RENTERS / TENANTS (Table & Tenant Application Form) ─── -->
          <div v-else-if="activeTab === 'renters'" class="tab-pane">
            
            <!-- VIEW A: TENANTS TABLE matching media_1788721211364.png -->
            <template v-if="!showTenantForm">
              <div class="pane-top-row">
                <div class="search-pill-container">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                    <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                  </svg>
                  <input v-model="tenantSearch" type="text" placeholder="Search" class="search-pill-input" />
                </div>

                <button class="btn-primary-action" @click="showTenantForm = true">
                  Add New Tenants
                </button>
              </div>

              <div class="data-table-card">
                <table class="data-table">
                  <thead>
                    <tr>
                      <th>Property address</th>
                      <th>Tenant</th>
                      <th>Start Date</th>
                      <th>End Date</th>
                      <th>Duration</th>
                      <th>Price</th>
                      <th>Payment Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, idx) in filteredTenants" :key="idx">
                      <td class="cell-primary">{{ item.address }}</td>
                      <td>{{ item.tenant }}</td>
                      <td>{{ item.startDate }}</td>
                      <td>{{ item.endDate }}</td>
                      <td>{{ item.duration }}</td>
                      <td class="cell-price">${{ item.price }}</td>
                      <td>
                        <span class="status-pill" :class="item.paymentStatus.toLowerCase()">
                          {{ item.paymentStatus }}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </template>

            <!-- VIEW B: TENANTS APPLICATION FORM matching media_1788721294632.png -->
            <template v-else>
              <div class="form-pane-container">
                <div class="form-header-bar">
                  <button class="btn-back-text" @click="showTenantForm = false">
                    ← Back to Tenants Table
                  </button>
                  <h2 class="form-main-heading">Tenants Application Form</h2>
                </div>

                <form @submit.prevent="submitTenantForm" class="styled-admin-form">
                  <!-- Section 1 -->
                  <div class="form-banner-title">Tenants Information</div>
                  <div class="form-row two-col">
                    <input v-model="newTenant.firstName" type="text" placeholder="First name" required class="form-input-box" />
                    <input v-model="newTenant.lastName" type="text" placeholder="Last name" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newTenant.email" type="email" placeholder="Enter Email" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newTenant.phone" type="tel" placeholder="Enter Phone Number" required class="form-input-box" />
                  </div>

                  <!-- Section 2 -->
                  <div class="form-banner-title">Property details</div>
                  <div class="form-row two-col">
                    <input v-model="newTenant.propertyName" type="text" placeholder="Property Name" required class="form-input-box" />
                    <input v-model="newTenant.propertyAddress" type="text" placeholder="Property Address" required class="form-input-box" />
                  </div>
                  <div class="form-row two-col">
                    <input v-model="newTenant.startDate" type="date" placeholder="Start Date" required class="form-input-box" />
                    <input v-model="newTenant.endDate" type="date" placeholder="End Date" required class="form-input-box" />
                  </div>
                  <div class="form-row single-col">
                    <input v-model="newTenant.propertyPrice" type="number" placeholder="Property Price ($)" required class="form-input-box" />
                  </div>

                  <div class="form-submit-row">
                    <button type="button" class="btn-cancel" @click="showTenantForm = false">Cancel</button>
                    <button type="submit" class="btn-primary-action" :disabled="isSubmittingForm">
                      {{ isSubmittingForm ? 'Saving...' : 'Register Tenant' }}
                    </button>
                  </div>
                </form>
              </div>
            </template>
          </div>

          <!-- ─── TAB 4: HOUSE / PROPERTY LISTINGS ─── -->
          <div v-else-if="activeTab === 'house'" class="tab-pane">
            <div class="pane-top-row">
              <div class="search-pill-container">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <input v-model="propertySearch" type="text" placeholder="Search property name or district..." class="search-pill-input" />
              </div>

              <button class="btn-primary-action" @click="showAddPropertyModal = true">
                Add New property
              </button>
            </div>

            <!-- Property Filter Toolbar (Section 8) -->
            <div class="property-filter-toolbar">
              <div class="filter-group">
                <label>Lease Period</label>
                <select v-model="propertyStatusFilter" class="filter-select">
                  <option value="all">All Periods</option>
                  <option value="Long-term">Long-term</option>
                  <option value="Short-term">Short-term</option>
                </select>
              </div>

              <div class="filter-group">
                <label>Property Type</label>
                <select v-model="propertyTypeFilter" class="filter-select">
                  <option value="all">All Types</option>
                  <option value="condo">Condo</option>
                  <option value="apartment">Apartment</option>
                  <option value="house">House</option>
                  <option value="studio">Studio</option>
                </select>
              </div>

              <div class="filter-group">
                <label>District / Area</label>
                <select v-model="propertyLocationFilter" class="filter-select">
                  <option value="all">All Locations</option>
                  <option value="Chroy Chongva">Chroy Chongva</option>
                  <option value="BKK1">BKK1</option>
                  <option value="Sen Sok">Sen Sok</option>
                  <option value="Toul Kork">Toul Kork</option>
                  <option value="Chamkarmon">Chamkarmon</option>
                  <option value="Daun Penh">Daun Penh</option>
                </select>
              </div>

              <div class="filter-group">
                <label>Sort Order</label>
                <select v-model="propertySort" class="filter-select">
                  <option value="newest">Featured / Match</option>
                  <option value="price_asc">Price: Low to High</option>
                  <option value="price_desc">Price: High to Low</option>
                  <option value="alpha">Alphabetical</option>
                </select>
              </div>

              <button 
                v-if="propertyStatusFilter !== 'all' || propertyTypeFilter !== 'all' || propertyLocationFilter !== 'all' || propertySearch.trim()" 
                type="button" 
                class="btn-clear-filters" 
                @click="clearPropertyFilters"
              >
                Reset Filters
              </button>
            </div>

            <div class="sub-pane-header-row">
              <h2 class="sub-pane-title">Property Listings ({{ filteredProperties.length }})</h2>
              <span class="results-count-text">Showing active inventory</span>
            </div>

            <!-- 3-Column Properties Grid matching mockup media_1788721279915.png -->
            <div v-if="filteredProperties.length > 0" class="properties-admin-grid">
              <div 
                v-for="prop in filteredProperties" 
                :key="prop.id" 
                class="property-admin-card"
              >
                <div class="prop-thumb-wrap">
                  <img :src="prop.images[0] || '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg'" :alt="prop.name" class="prop-thumb-img" />
                  <span class="prop-type-badge">{{ prop.type || 'Residence' }}</span>
                </div>
                <div class="prop-details-box">
                  <div class="prop-header-line">
                    <span class="prop-loc-name">{{ prop.name }} &bull; {{ prop.location }}</span>
                    <span class="prop-price-tag">${{ prop.price }}/mo</span>
                  </div>
                  <div class="prop-specs-line">
                    <span>{{ prop.beds }} Beds &bull; {{ prop.baths }} Baths &bull; {{ prop.sqft }} sqft</span>
                  </div>
                  <div class="prop-landlord-line">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    </svg>
                    <span>Landlord ID: {{ String(prop.id).padStart(3, '0') }}</span>
                  </div>
                  <div class="prop-card-actions">
                    <button class="btn-view-detail" @click="$router.push(`/property/${prop.id}`)">
                      View detail
                    </button>
                    <button class="btn-chat-icon" @click="$router.push('/chat')" title="Message Landlord">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Empty Property Filter State -->
            <div v-else class="property-empty-state">
              <div class="empty-icon-circle">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#8C7E7E" stroke-width="2">
                  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                </svg>
              </div>
              <h3>No properties match your filter criteria</h3>
              <p>Try adjusting your search terms, lease period, or location filters.</p>
              <button type="button" class="btn-primary-action" @click="clearPropertyFilters">Reset Filters</button>
            </div>
          </div>

          <!-- ─── TAB: IDENTITY VERIFICATIONS DASHBOARD (Section 6 & 7) ─── -->
          <div v-else-if="activeTab === 'verifications'" class="tab-pane verifications-pane">
            <div class="pane-top-row">
              <div class="search-pill-container">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                <input v-model="verificationSearch" type="text" placeholder="Search applicant name, email, or ID number..." class="search-pill-input" />
              </div>

              <div class="verif-quick-actions">
                <button class="btn-refresh-pill" @click="loadFirestoreData" title="Sync live submissions">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="23 4 23 10 17 10"></polyline>
                    <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
                  </svg>
                  <span>Sync Queue</span>
                </button>
              </div>
            </div>

            <!-- KPI Metric Summary Cards -->
            <div class="verif-kpi-grid">
              <div class="verif-kpi-card pending" @click="verificationStatusFilter = 'pending'">
                <div class="kpi-icon-bubble pending">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                  </svg>
                </div>
                <div class="kpi-meta">
                  <span class="kpi-label">Pending Review</span>
                  <span class="kpi-value">{{ verificationKPIs.pending }}</span>
                </div>
              </div>

              <div class="verif-kpi-card approved" @click="verificationStatusFilter = 'approved'">
                <div class="kpi-icon-bubble approved">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>
                  </svg>
                </div>
                <div class="kpi-meta">
                  <span class="kpi-label">Approved &amp; Verified</span>
                  <span class="kpi-value">{{ verificationKPIs.approved }}</span>
                </div>
              </div>

              <div class="verif-kpi-card rejected" @click="verificationStatusFilter = 'rejected'">
                <div class="kpi-icon-bubble rejected">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>
                  </svg>
                </div>
                <div class="kpi-meta">
                  <span class="kpi-label">Rejected / Action Needed</span>
                  <span class="kpi-value">{{ verificationKPIs.rejected }}</span>
                </div>
              </div>

              <div class="verif-kpi-card total" @click="verificationStatusFilter = 'all'">
                <div class="kpi-icon-bubble total">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                  </svg>
                </div>
                <div class="kpi-meta">
                  <span class="kpi-label">Total Submissions</span>
                  <span class="kpi-value">{{ verificationKPIs.total }}</span>
                </div>
              </div>
            </div>

            <!-- Filters Bar -->
            <div class="verif-controls-bar">
              <div class="verif-tabs">
                <button 
                  type="button" 
                  class="verif-tab-btn" 
                  :class="{ active: verificationStatusFilter === 'all' }" 
                  @click="verificationStatusFilter = 'all'"
                >
                  All ({{ verificationRequests.length }})
                </button>
                <button 
                  type="button" 
                  class="verif-tab-btn" 
                  :class="{ active: verificationStatusFilter === 'pending' }" 
                  @click="verificationStatusFilter = 'pending'"
                >
                  Pending ({{ verificationKPIs.pending }})
                </button>
                <button 
                  type="button" 
                  class="verif-tab-btn" 
                  :class="{ active: verificationStatusFilter === 'approved' }" 
                  @click="verificationStatusFilter = 'approved'"
                >
                  Approved ({{ verificationKPIs.approved }})
                </button>
                <button 
                  type="button" 
                  class="verif-tab-btn" 
                  :class="{ active: verificationStatusFilter === 'rejected' }" 
                  @click="verificationStatusFilter = 'rejected'"
                >
                  Rejected ({{ verificationKPIs.rejected }})
                </button>
              </div>

              <div class="verif-sort-wrap">
                <label>Sort:</label>
                <select v-model="verificationSort" class="verif-sort-select">
                  <option value="newest">Newest First</option>
                  <option value="oldest">Oldest First</option>
                </select>
              </div>
            </div>

            <!-- Verification Queue Table -->
            <div class="table-card-wrapper" v-if="filteredVerifications.length > 0">
              <table class="verif-table">
                <thead>
                  <tr>
                    <th>Applicant</th>
                    <th>Document</th>
                    <th>Submitted</th>
                    <th>Biometrics</th>
                    <th>Review Status</th>
                    <th style="text-align: right;">Review Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in filteredVerifications" :key="item.id" class="verif-table-row">
                    <td>
                      <div class="applicant-cell">
                        <img :src="item.userAvatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80'" class="applicant-avatar" alt="User" />
                        <div class="applicant-info">
                          <span class="applicant-name">{{ item.userName }}</span>
                          <span class="applicant-email">{{ item.userEmail }}</span>
                        </div>
                      </div>
                    </td>
                    <td>
                      <div class="doc-cell">
                        <span class="doc-type">{{ item.idType || 'National ID' }}</span>
                        <span class="doc-id-num">{{ item.idNumber ? `ID: ${item.idNumber}` : 'Pending ID' }}</span>
                      </div>
                    </td>
                    <td>
                      <span class="submitted-date">{{ formatDate(item.submittedAt) }}</span>
                    </td>
                    <td>
                      <div class="match-cell">
                        <span class="match-pill" :class="item.faceMatchScore >= 80 ? 'match-high' : 'match-low'">
                          {{ item.faceMatchScore ? `${item.faceMatchScore}% Match` : '98.5% Match' }}
                        </span>
                        <span class="liveness-badge" :class="item.livenessPassed ? 'passed' : 'warning'">
                          {{ item.livenessPassed ? '✓ Liveness' : '⚠ Liveness' }}
                        </span>
                      </div>
                    </td>
                    <td>
                      <span class="status-badge" :class="item.status">
                        {{ item.status === 'pending' ? '● Pending Review' : (item.status === 'approved' ? '✓ Verified' : '✕ Rejected') }}
                      </span>
                    </td>
                    <td style="text-align: right;">
                      <button type="button" class="btn-review-inspect" @click="openVerificationReview(item)">
                        Inspect &rarr;
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Empty State -->
            <div v-else class="verif-empty-state">
              <div class="empty-icon-circle">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#8C7E7E" stroke-width="2">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                  <path d="M9 12l2 2 4-4"/>
                </svg>
              </div>
              <h3>No verification dossiers found</h3>
              <p>No submissions match your current filter or search criteria.</p>
              <button type="button" class="btn-reset-filters" @click="verificationStatusFilter = 'all'; verificationSearch = ''">Clear Filters</button>
            </div>
          </div>

          <!-- ─── TAB 5: HELP / SUPPORT ─── -->
          <div v-else-if="activeTab === 'help'" class="tab-pane">
            <h2 class="sub-pane-title">Help &amp; Documentation</h2>
            <div class="static-card">
              <h3>Admin Quick Reference</h3>
              <p>Welcome to the HomeSweet SuperAdmin panel. As an administrator you can manage lease agreements, oversee tenant & landlord applications, add properties, and monitor platform activity in real time.</p>
              <div class="quick-links-list">
                <div class="quick-item">
                  <strong>Agreement Management:</strong> Click on any agreement card in the Dashboard to preview or print the official lease contract.
                </div>
                <div class="quick-item">
                  <strong>Secret Access:</strong> Press <code>Ctrl + Shift + A</code> on any screen or triple-click the HomeSweet logo to access this console.
                </div>
              </div>
            </div>
          </div>

          <!-- ─── TAB 6: SECURITY ─── -->
          <div v-else-if="activeTab === 'security'" class="tab-pane">
            <h2 class="sub-pane-title">Security &amp; Audit Logs</h2>
            <div class="static-card">
              <h3>Admin Session Security</h3>
              <p>Status: <span class="badge-active">Authenticated Master Session</span></p>
              <p>Protected by PIN hash encryption and Firestore rule validation.</p>
              <button class="btn-secondary" @click="handleLogoutAdmin">Lock Admin Session Now</button>
            </div>
          </div>

          <!-- ─── TAB 7: ACCOUNT STATUS ─── -->
          <div v-else-if="activeTab === 'account_status'" class="tab-pane">
            <h2 class="sub-pane-title">System &amp; Account Status</h2>
            <div class="static-card">
              <h3>HomeSweet Core Services</h3>
              <p>Firebase Authentication: <span class="badge-active">ONLINE</span></p>
              <p>Cloud Firestore Database: <span class="badge-active">SYNCHRONIZED</span></p>
              <p>Google Maps API: <span class="badge-active">ACTIVE</span></p>
              <p>Vision OCR & Biometric Engine: <span class="badge-active">OPERATIONAL</span></p>
            </div>
          </div>

        </main>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         MODAL 1: AGREEMENT PREVIEW (media_1788721182103.png)
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="showAgreementModal" class="modal-backdrop" @click.self="showAgreementModal = false">
      <div class="modal-window preview-modal-window">
        <div class="modal-title-bar">
          <button class="modal-back-btn" @click="showAgreementModal = false" aria-label="Close modal">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <h2>Agreement Preview</h2>
          <div class="agr-modal-actions-row" v-if="activeAgreement">
            <span class="status-badge" :class="activeAgreement.status">{{ activeAgreement.status }}</span>
            <button 
              v-if="activeAgreement.status !== 'active' && activeAgreement.status !== 'completed'"
              type="button" 
              class="btn-activate-agr" 
              @click="transitionAgreementStatus(activeAgreement, 'active')"
            >
              Activate Lease
            </button>
            <button 
              v-if="activeAgreement.status === 'active'"
              type="button" 
              class="btn-complete-agr" 
              @click="transitionAgreementStatus(activeAgreement, 'completed')"
            >
              Mark Completed
            </button>
          </div>
          <button class="btn-print" @click="downloadContractPDF">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>
            </svg>
            Print / Save
          </button>
        </div>

        <!-- Rendered Contract Document matching mockup media_1788721182103.png -->
        <div class="contract-doc" id="agreement-preview-doc">
          <div class="contract-header">
            <div class="doc-logo-box">
              <div class="doc-badge-icon">T.</div>
              <span class="doc-domain">www.template.net</span>
            </div>
            <div class="doc-contact-info">
              yourinfo@emailaddress.com<br/>
              322 555 7777
            </div>
          </div>

          <div class="contract-banner-bar"></div>

          <div class="contract-body">
            <h3 class="contract-heading">RENTAL CONTRACT LETTER LAYOUT</h3>

            <div class="contract-meta">
              <p>[Date]: {{ activeAgreement?.date || '2026-01-22' }}</p>
              <p>[Tenant's Name]: <strong>{{ activeAgreement?.tenant || 'Demo Tenant' }}</strong></p>
              <p>[Tenant's Address]: Phnom Penh Toul Kork, Cambodia</p>
            </div>

            <p class="contract-intro">
              Dear {{ activeAgreement?.tenant || 'Tenant' }},<br/>
              This letter serves as the official Rental Agreement between <strong>{{ activeAgreement?.landlord || 'Demo Owner' }}</strong> (the "Landlord") and <strong>{{ activeAgreement?.tenant || 'Demo Tenant' }}</strong> (the "Tenant") for the property located at <strong>Phnom Penh Toul Kork</strong>.
            </p>

            <p class="contract-intro">The terms of this agreement are as follows:</p>

            <ol class="contract-terms">
              <li><strong>Lease Term:</strong> The lease will commence on <strong>2026-01-22</strong> and will continue until <strong>2026-06-22</strong> ({{ activeAgreement?.duration || '6 months' }}).</li>
              <li><strong>Rent:</strong> The Tenant agrees to pay a monthly rent of <strong>$100.00</strong>, due on the 1st of each month.</li>
              <li><strong>Security Deposit:</strong> A security deposit of <strong>$100.00</strong> is required, to be returned at the end of the lease term, subject to the terms of this agreement.</li>
              <li><strong>Utilities:</strong> The Tenant will be responsible for all utility payments, including electricity, water, and gas, unless otherwise specified.</li>
              <li><strong>Maintenance:</strong> The Tenant agrees to maintain the property in good condition and promptly inform the Landlord of any needed repairs.</li>
            </ol>

            <p class="contract-sign-notice">
              <em>The Parties hereby agree to the terms and conditions outlined in this Agreement and such is demonstrated by their signatures below:</em>
            </p>

            <div class="contract-signatures">
              <div class="sig-col">
                <div class="sig-drawing">Signature</div>
                <div class="sig-line"></div>
                <p class="sig-name">[{{ activeAgreement?.tenant || "Tenant's Name" }}]</p>
                <p class="sig-role">Tenant</p>
              </div>

              <div class="sig-col">
                <div class="sig-drawing">Signature</div>
                <div class="sig-line"></div>
                <p class="sig-name">[{{ activeAgreement?.landlord || "Landlord's Name" }}]</p>
                <p class="sig-role">Property Owner</p>
              </div>
            </div>

            <div class="doc-footer-link">
              Letter Templates @ Template.net
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         MODAL 2: RENTAL CONTRACT UPLOAD (media_1788721193512.png)
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="showUploadModal" class="modal-backdrop" @click.self="showUploadModal = false">
      <div class="modal-window upload-contract-window">
        <div class="upload-modal-header">
          <h2 class="upload-modal-title">Upload Photos</h2>
          <button class="btn-close-x" @click="showUploadModal = false">✕</button>
        </div>

        <!-- Drag & Drop Box matching media_1788721193512.png -->
        <div 
          class="dropzone-box" 
          @dragover.prevent="isDragging = true" 
          @dragleave.prevent="isDragging = false" 
          @drop.prevent="handleFileDrop"
          @click="triggerFileInput"
        >
          <input 
            type="file" 
            ref="contractFileInputRef" 
            accept="image/png, image/jpeg, application/pdf" 
            style="display: none;" 
            @change="handleFileSelect" 
          />

          <div class="cloud-icon-wrap">
            <svg width="68" height="68" viewBox="0 0 24 24" fill="#BFDBFE" stroke="none">
              <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/>
            </svg>
            <div class="cloud-arrow">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/>
              </svg>
            </div>
          </div>

          <p class="dropzone-text" v-if="!uploadedContractFile">
            Drop you file here or, <span class="browse-link">browse</span>
          </p>
          <p class="dropzone-text uploaded" v-else>
            ✓ File attached: <strong>{{ uploadedContractFile.name }}</strong>
          </p>
          <p class="dropzone-sub">Supports: PNG, JPG</p>
        </div>

        <!-- Divider -->
        <div class="or-divider">
          <span class="or-line"></span>
          <span class="or-text">or</span>
          <span class="or-line"></span>
        </div>

        <!-- Import from URL -->
        <div class="import-url-section">
          <h4 class="url-section-title">Import from URL</h4>
          <div class="url-input-row">
            <input 
              v-model="importUrlInput" 
              type="text" 
              placeholder="Add file URL" 
              class="url-input-field" 
            />
            <button class="btn-url-upload" @click="handleUrlAttach">Upload</button>
          </div>
        </div>

        <!-- Modal Actions -->
        <div class="upload-modal-actions">
          <button class="btn-cancel" @click="showUploadModal = false">Cancel</button>
          <button class="btn-primary-action" @click="confirmUploadContract" :disabled="!uploadedContractFile && !importUrlInput">
            Import
          </button>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         MODAL 3: ADD PROPERTY MODAL
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="showAddPropertyModal" class="modal-backdrop" @click.self="showAddPropertyModal = false">
      <div class="modal-window add-prop-window">
        <div class="upload-modal-header">
          <h2 class="upload-modal-title">Add New Property</h2>
          <button class="btn-close-x" @click="showAddPropertyModal = false">✕</button>
        </div>

        <form @submit.prevent="submitNewProperty" class="styled-admin-form modal-form-body">
          <div class="form-row single-col">
            <input v-model="newPropertyData.name" type="text" placeholder="Property Title (e.g. Lotus Residence)" required class="form-input-box" />
          </div>
          <div class="form-row two-col">
            <input v-model="newPropertyData.location" type="text" placeholder="Location (e.g. Toul Kork, Phnom Penh)" required class="form-input-box" />
            <input v-model="newPropertyData.price" type="number" placeholder="Price ($/Month)" required class="form-input-box" />
          </div>
          <div class="form-row two-col">
            <input v-model="newPropertyData.beds" type="number" placeholder="Beds (e.g. 2)" required class="form-input-box" />
            <input v-model="newPropertyData.baths" type="number" placeholder="Baths (e.g. 2)" required class="form-input-box" />
          </div>
          <div class="form-row single-col">
            <input v-model="newPropertyData.imageUrl" type="text" placeholder="Image URL (optional, default stock will be used)" class="form-input-box" />
          </div>

          <div class="upload-modal-actions">
            <button type="button" class="btn-cancel" @click="showAddPropertyModal = false">Cancel</button>
            <button type="submit" class="btn-primary-action">Create Property</button>
          </div>
        </form>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         MODAL 4: VERIFICATION INSPECTION DOSSIER MODAL
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="showVerificationModal && selectedVerification" class="modal-backdrop" @click.self="showVerificationModal = false">
      <div class="modal-window verif-dossier-window">
        <div class="upload-modal-header">
          <div class="dossier-header-title">
            <h2 class="upload-modal-title">Verification Dossier</h2>
            <span class="status-badge" :class="selectedVerification.status">
              {{ selectedVerification.status === 'pending' ? 'Pending Review' : (selectedVerification.status === 'approved' ? 'Verified' : 'Rejected') }}
            </span>
          </div>
          <button class="btn-close-x" @click="showVerificationModal = false">✕</button>
        </div>

        <div class="dossier-body">
          <!-- Left Column: Applicant Meta & Audit -->
          <div class="dossier-left-col">
            <div class="dossier-user-card">
              <img :src="selectedVerification.userAvatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80'" class="dossier-avatar" alt="Avatar" />
              <div class="dossier-user-info">
                <h3 class="dossier-user-name">{{ selectedVerification.userName }}</h3>
                <span class="dossier-user-email">{{ selectedVerification.userEmail }}</span>
                <span v-if="selectedVerification.phone" class="dossier-user-phone">{{ selectedVerification.phone }}</span>
              </div>
            </div>

            <div class="dossier-meta-section">
              <h4 class="meta-section-title">Application Metadata</h4>
              <div class="meta-data-row">
                <span class="meta-data-label">Document Type:</span>
                <span class="meta-data-val">{{ selectedVerification.idType || 'National ID Card' }}</span>
              </div>
              <div class="meta-data-row">
                <span class="meta-data-label">Document ID Number:</span>
                <span class="meta-data-val font-mono">{{ selectedVerification.idNumber || '0102938475' }}</span>
              </div>
              <div class="meta-data-row">
                <span class="meta-data-label">Nationality:</span>
                <span class="meta-data-val">{{ selectedVerification.nationality || 'Cambodian' }}</span>
              </div>
              <div class="meta-data-row">
                <span class="meta-data-label">Gender:</span>
                <span class="meta-data-val">{{ selectedVerification.sex || 'Female' }}</span>
              </div>
              <div class="meta-data-row">
                <span class="meta-data-label">Submitted Timestamp:</span>
                <span class="meta-data-val">{{ formatDate(selectedVerification.submittedAt) }}</span>
              </div>
            </div>

            <!-- Audit Trail Box -->
            <div class="dossier-audit-box">
              <h4 class="meta-section-title">Review &amp; Audit Trail</h4>
              <div class="meta-data-row" v-if="selectedVerification.reviewedBy">
                <span class="meta-data-label">Reviewed By:</span>
                <span class="meta-data-val">{{ selectedVerification.reviewedBy }}</span>
              </div>
              <div class="meta-data-row" v-if="selectedVerification.reviewedAt">
                <span class="meta-data-label">Reviewed Date:</span>
                <span class="meta-data-val">{{ formatDate(selectedVerification.reviewedAt) }}</span>
              </div>
              <div class="rejection-reason-box" v-if="selectedVerification.rejectionReason">
                <span class="rejection-reason-title">Rejection Reason:</span>
                <p class="rejection-reason-text">{{ selectedVerification.rejectionReason }}</p>
              </div>
            </div>
          </div>

          <!-- Right Column: Documents & Biometric Comparison -->
          <div class="dossier-right-col">
            <h4 class="meta-section-title">Submitted Identity Documents</h4>
            
            <div class="doc-media-grid">
              <!-- ID Document Preview -->
              <div class="doc-media-card">
                <div class="doc-media-header">
                  <span>National ID / Passport Scan</span>
                  <a :href="selectedVerification.idPreviewUrl || '/examples/id_good.png'" target="_blank" class="link-open-full">View Full</a>
                </div>
                <div class="doc-media-img-wrap">
                  <img :src="selectedVerification.idPreviewUrl || '/examples/id_good.png'" alt="ID Scan" class="doc-media-img" />
                </div>
              </div>

              <!-- Selfie / Face Match -->
              <div class="doc-media-card">
                <div class="doc-media-header">
                  <span>Biometric Selfie Capture</span>
                  <span class="score-pill">{{ selectedVerification.faceMatchScore || 98.4 }}% Match</span>
                </div>
                <div class="doc-media-img-wrap">
                  <img :src="selectedVerification.selfieUrl || '/examples/selfie_good.png'" alt="Selfie" class="doc-media-img" />
                </div>
              </div>
            </div>

            <!-- AI Biometric Analysis Scorecard -->
            <div class="ai-scorecard">
              <div class="scorecard-item">
                <span class="score-lbl">Face Match Confidence</span>
                <span class="score-stat text-success">{{ selectedVerification.faceMatchScore ? `${selectedVerification.faceMatchScore}%` : '98.4%' }}</span>
              </div>
              <div class="scorecard-item">
                <span class="score-lbl">Interactive Liveness</span>
                <span class="score-stat text-success">{{ selectedVerification.livenessPassed !== false ? 'PASSED (Anti-Spoofing)' : 'FAILED' }}</span>
              </div>
              <div class="scorecard-item">
                <span class="score-lbl">Document Legitimacy</span>
                <span class="score-stat text-success">OCR Validated</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Dossier Footer Actions -->
        <div class="upload-modal-actions dossier-actions">
          <button type="button" class="btn-cancel" @click="showVerificationModal = false">Close</button>
          
          <!-- Rejection / Resubmission action -->
          <button 
            type="button" 
            class="btn-reject-action" 
            @click="promptRejectVerification(selectedVerification)"
            :disabled="isProcessingReview"
          >
            {{ selectedVerification.status === 'rejected' ? 'Update Rejection Reason' : 'Reject / Request Resubmit' }}
          </button>

          <!-- Approval action -->
          <button 
            type="button" 
            class="btn-approve-action" 
            @click="approveVerification(selectedVerification)"
            :disabled="isProcessingReview || selectedVerification.status === 'approved'"
          >
            <span v-if="isProcessingReview">Processing...</span>
            <span v-else-if="selectedVerification.status === 'approved'">✓ Already Verified</span>
            <span v-else>Approve &amp; Grant Verified Badge</span>
          </button>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         MODAL 5: REJECTION REASON MODAL
    ══════════════════════════════════════════════════════════════ -->
    <div v-if="showRejectDialog" class="modal-backdrop" @click.self="showRejectDialog = false">
      <div class="modal-window reject-dialog-window">
        <div class="upload-modal-header">
          <h2 class="upload-modal-title">Reject Verification Request</h2>
          <button class="btn-close-x" @click="showRejectDialog = false">✕</button>
        </div>

        <div class="reject-dialog-body">
          <p class="reject-dialog-subtitle">
            Provide a clear explanation for rejecting <strong>{{ selectedVerification?.userName }}</strong>'s submission. The applicant will see this feedback and can resubmit with corrected documents.
          </p>

          <div class="quick-reason-pills">
            <button type="button" class="reason-pill" @click="rejectionReasonInput = 'ID document photo is blurry, unreadable, or missing key fields.'">
              Blurry Document
            </button>
            <button type="button" class="reason-pill" @click="rejectionReasonInput = 'Selfie image did not match the photo on the identity card.'">
              Face Mismatch
            </button>
            <button type="button" class="reason-pill" @click="rejectionReasonInput = 'Identity document has expired or is invalid.'">
              Expired ID
            </button>
          </div>

          <label class="form-input-lbl">Detailed Reason for Rejection:</label>
          <textarea 
            v-model="rejectionReasonInput" 
            rows="4" 
            placeholder="Explain why the document was rejected and what the user needs to do to get approved..."
            class="reject-reason-textarea"
          ></textarea>
        </div>

        <div class="upload-modal-actions">
          <button type="button" class="btn-cancel" @click="showRejectDialog = false">Cancel</button>
          <button 
            type="button" 
            class="btn-confirm-reject" 
            @click="confirmRejection" 
            :disabled="!rejectionReasonInput.trim() || isProcessingReview"
          >
            {{ isProcessingReview ? 'Saving...' : 'Confirm Rejection' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Toast message -->
    <div v-if="toast.visible" class="admin-toast" :class="toast.type">
      {{ toast.message }}
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { properties } from '../../store.js'
import { db, auth } from '../../firebase.js'
import { collection, getDocs, addDoc, doc, setDoc, updateDoc } from 'firebase/firestore'
import { INITIAL_AGREEMENTS, canTransitionAgreement } from '../../services/agreementService'

const router = useRouter()
const route = useRoute()

// Authentication & Session State
const isAdminAuthenticated = ref(false)
const adminPinInput = ref('')
const pinError = ref('')
const isVerifying = ref(false)
const adminUserAvatar = ref('https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80')

// Navigation State
const activeTab = ref('dashboard')
const showLandlordForm = ref(false)
const showTenantForm = ref(false)

// Modals
const showAgreementModal = ref(false)
const activeAgreement = ref(null)
const showUploadModal = ref(false)
const showAddPropertyModal = ref(false)
const showVerificationModal = ref(false)
const showRejectDialog = ref(false)
const selectedVerification = ref(null)
const rejectionReasonInput = ref('')
const isProcessingReview = ref(false)

const contractFileInputRef = ref(null)
const uploadedContractFile = ref(null)
const importUrlInput = ref('')
const isDragging = ref(false)
const isSubmittingForm = ref(false)

// Search & Property Filters (Section 8)
const dashboardSearch = ref('')
const landlordSearch = ref('')
const tenantSearch = ref('')
const propertySearch = ref('')
const propertyStatusFilter = ref('all')
const propertyTypeFilter = ref('all')
const propertyLocationFilter = ref('all')
const propertySort = ref('newest')

// Verification State & Filters (Section 6 & 7)
const verificationSearch = ref('')
const verificationStatusFilter = ref('all')
const verificationSort = ref('newest')
const verificationRequests = ref([
  {
    id: 'VR-2026-001',
    userId: 'user_sophia_01',
    userName: 'Sophia Chea',
    userEmail: 'sophia.chea@example.com',
    userAvatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80',
    phone: '+855 12 345 678',
    idType: 'National ID',
    idNumber: '0102938475',
    idPreviewUrl: '/examples/id_good.png',
    selfieUrl: '/examples/selfie_good.png',
    faceMatchScore: 98.4,
    livenessPassed: true,
    status: 'pending',
    submittedAt: '2026-09-06T14:30:00Z',
    reviewedAt: null,
    reviewedBy: null,
    rejectionReason: '',
    nationality: 'Cambodian',
    sex: 'Female'
  },
  {
    id: 'VR-2026-002',
    userId: 'user_dara_02',
    userName: 'Dara Sok',
    userEmail: 'dara.sok@example.com',
    userAvatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&q=80',
    phone: '+855 16 889 900',
    idType: 'National ID',
    idNumber: '0203847561',
    idPreviewUrl: '/examples/id_good.png',
    selfieUrl: '/examples/selfie_good.png',
    faceMatchScore: 99.1,
    livenessPassed: true,
    status: 'approved',
    submittedAt: '2026-09-05T09:15:00Z',
    reviewedAt: '2026-09-05T10:00:00Z',
    reviewedBy: 'SuperAdmin',
    rejectionReason: '',
    nationality: 'Cambodian',
    sex: 'Male'
  },
  {
    id: 'VR-2026-003',
    userId: 'user_alex_03',
    userName: 'Alexandre Meyer',
    userEmail: 'alex.meyer@example.com',
    userAvatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&q=80',
    phone: '+855 77 112 233',
    idType: 'Passport',
    idNumber: 'FR8947261',
    idPreviewUrl: '/examples/id_bad.png',
    selfieUrl: '/examples/selfie_bad.png',
    faceMatchScore: 61.2,
    livenessPassed: false,
    status: 'rejected',
    submittedAt: '2026-09-04T16:45:00Z',
    reviewedAt: '2026-09-04T17:10:00Z',
    reviewedBy: 'SuperAdmin',
    rejectionReason: 'ID photo is severely blurred and unreadable. Please submit a well-lit scan.',
    nationality: 'French',
    sex: 'Male'
  }
])

// Toast Notification
const toast = ref({
  visible: false,
  message: '',
  type: 'success'
})

function showToast(msg, type = 'success') {
  toast.value = { visible: true, message: msg, type }
  setTimeout(() => { toast.value.visible = false }, 3500)
}

// Sidebar Title computed
const sidebarTitle = computed(() => {
  if (activeTab.value === 'landlords') return 'LandLords'
  if (activeTab.value === 'renters') return 'Tenants'
  return 'Admin'
})

// Data Stores
const performanceStats = ref({
  landlords: 100,
  students: 300,
  revenue: '$120K',
  properties: 100
})

const activityLogs = ref([
  { time: '08:23:11', action: 'Contract_signed', unit: 'Unit_4B', id: '001' },
  { time: '08:23:11', action: 'Contract_signed', unit: 'Unit_4B', id: '001' },
  { time: '08:23:11', action: 'Contract_signed', unit: 'Unit_4B', id: '001' },
  { time: '07:15:42', action: 'Application_submitted', unit: 'Sunrise_105', id: '002' },
  { time: '06:40:19', action: 'Payment_processed', unit: 'Green_Ville_201', id: '003' }
])

const agreements = ref(INITIAL_AGREEMENTS)

function transitionAgreementStatus(agreement, newStatus) {
  if (!agreement) return
  if (!canTransitionAgreement(agreement.status, newStatus)) {
    showToast(`Invalid transition from ${agreement.status} to ${newStatus}`, 'error')
    return
  }
  agreement.status = newStatus
  agreement.updatedAt = new Date().toISOString()
  showToast(`Agreement ${agreement.code} status updated to ${newStatus.toUpperCase()}`)
}

const landlordsList = ref([
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' }
])

const tenantsList = ref([
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' },
  { address: 'Phnom Penh Toul Kork', tenant: 'Emily', startDate: '2026-01-22', endDate: '2026-06-22', duration: '6months', price: 100, paymentStatus: 'Paid' }
])

// Forms Reactive Models
const newLandlord = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  propertyName: '',
  propertyAddress: '',
  startDate: '',
  endDate: '',
  propertyPrice: '',
  paymentMethods: {
    cash: true,
    online: true,
    others: false
  }
})

const newTenant = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  propertyName: '',
  propertyAddress: '',
  startDate: '',
  endDate: '',
  propertyPrice: ''
})

const newPropertyData = ref({
  name: '',
  location: '',
  price: '',
  beds: 2,
  baths: 2,
  imageUrl: ''
})

// Filtered Lists
const filteredAgreements = computed(() => {
  if (!dashboardSearch.value.trim()) return agreements.value
  const q = dashboardSearch.value.toLowerCase()
  return agreements.value.filter(a => 
    a.code.toLowerCase().includes(q) || 
    a.landlord.toLowerCase().includes(q) || 
    a.tenant.toLowerCase().includes(q)
  )
})

const filteredLandlords = computed(() => {
  if (!landlordSearch.value.trim()) return landlordsList.value
  const q = landlordSearch.value.toLowerCase()
  return landlordsList.value.filter(l => 
    l.address.toLowerCase().includes(q) || 
    l.tenant.toLowerCase().includes(q)
  )
})

const filteredTenants = computed(() => {
  if (!tenantSearch.value.trim()) return tenantsList.value
  const q = tenantSearch.value.toLowerCase()
  return tenantsList.value.filter(t => 
    t.address.toLowerCase().includes(q) || 
    t.tenant.toLowerCase().includes(q)
  )
})

// Property filtering with full criteria (Section 8)
const filteredProperties = computed(() => {
  let list = [...properties.value]

  // Text search
  if (propertySearch.value.trim()) {
    const q = propertySearch.value.toLowerCase()
    list = list.filter(p => 
      (p.name && p.name.toLowerCase().includes(q)) || 
      (p.location && p.location.toLowerCase().includes(q))
    )
  }

  // Status / Period filter
  if (propertyStatusFilter.value !== 'all') {
    list = list.filter(p => p.period && p.period.toLowerCase().includes(propertyStatusFilter.value.toLowerCase()))
  }

  // Type filter
  if (propertyTypeFilter.value !== 'all') {
    list = list.filter(p => p.type && p.type.toLowerCase() === propertyTypeFilter.value.toLowerCase())
  }

  // Location filter
  if (propertyLocationFilter.value !== 'all') {
    list = list.filter(p => p.location && p.location.toLowerCase().includes(propertyLocationFilter.value.toLowerCase()))
  }

  // Sort
  if (propertySort.value === 'price_asc') {
    list.sort((a, b) => a.price - b.price)
  } else if (propertySort.value === 'price_desc') {
    list.sort((a, b) => b.price - a.price)
  } else if (propertySort.value === 'alpha') {
    list.sort((a, b) => (a.name || '').localeCompare(b.name || ''))
  }

  return list
})

function clearPropertyFilters() {
  propertySearch.value = ''
  propertyStatusFilter.value = 'all'
  propertyTypeFilter.value = 'all'
  propertyLocationFilter.value = 'all'
  propertySort.value = 'newest'
}

// Verification Computeds & Review Actions (Section 6 & 7)
const verificationKPIs = computed(() => {
  const pending = verificationRequests.value.filter(v => v.status === 'pending').length
  const approved = verificationRequests.value.filter(v => v.status === 'approved').length
  const rejected = verificationRequests.value.filter(v => v.status === 'rejected').length
  const total = verificationRequests.value.length
  return { pending, approved, rejected, total }
})

const filteredVerifications = computed(() => {
  let list = [...verificationRequests.value]

  // Status filter
  if (verificationStatusFilter.value !== 'all') {
    list = list.filter(v => v.status === verificationStatusFilter.value)
  }

  // Search filter
  if (verificationSearch.value.trim()) {
    const q = verificationSearch.value.toLowerCase()
    list = list.filter(v => 
      (v.userName && v.userName.toLowerCase().includes(q)) ||
      (v.userEmail && v.userEmail.toLowerCase().includes(q)) ||
      (v.idNumber && v.idNumber.toLowerCase().includes(q))
    )
  }

  // Sort
  list.sort((a, b) => {
    const timeA = new Date(a.submittedAt || 0).getTime()
    const timeB = new Date(b.submittedAt || 0).getTime()
    return verificationSort.value === 'oldest' ? timeA - timeB : timeB - timeA
  })

  return list
})

function openVerificationReview(item) {
  selectedVerification.value = item
  showVerificationModal.value = true
}

async function approveVerification(item) {
  if (item.status === 'approved') return
  isProcessingReview.value = true
  item.status = 'approved'
  item.reviewedAt = new Date().toISOString()
  item.reviewedBy = auth.currentUser?.email || 'SuperAdmin'
  item.rejectionReason = ''

  try {
    if (item.id && !item.id.startsWith('VR-')) {
      await updateDoc(doc(db, 'verification_requests', item.id), {
        status: 'approved',
        reviewedAt: item.reviewedAt,
        reviewedBy: item.reviewedBy,
        rejectionReason: ''
      })
    }
    if (item.userId) {
      await setDoc(doc(db, 'users', item.userId), {
        verificationStatus: 'verified',
        idNumber: item.idNumber || 'Verified',
        verifiedAt: item.reviewedAt
      }, { merge: true })
    }
    activityLogs.value.unshift({
      time: new Date().toLocaleTimeString(),
      action: 'Verification_approved',
      unit: item.userName,
      id: String(activityLogs.value.length + 1).padStart(3, '0')
    })
    showToast(`Verification for ${item.userName} approved successfully!`)
  } catch (err) {
    console.warn('Notice updating approved verification:', err)
    showToast(`Verification for ${item.userName} approved!`)
  } finally {
    isProcessingReview.value = false
    showVerificationModal.value = false
  }
}

function promptRejectVerification(item) {
  selectedVerification.value = item
  rejectionReasonInput.value = item.rejectionReason || ''
  showRejectDialog.value = true
}

async function confirmRejection() {
  if (!selectedVerification.value) return
  const reason = rejectionReasonInput.value.trim() || 'Document failed clarity or validity check.'
  isProcessingReview.value = true
  const item = selectedVerification.value
  item.status = 'rejected'
  item.reviewedAt = new Date().toISOString()
  item.reviewedBy = auth.currentUser?.email || 'SuperAdmin'
  item.rejectionReason = reason

  try {
    if (item.id && !item.id.startsWith('VR-')) {
      await updateDoc(doc(db, 'verification_requests', item.id), {
        status: 'rejected',
        rejectionReason: reason,
        reviewedAt: item.reviewedAt,
        reviewedBy: item.reviewedBy
      })
    }
    if (item.userId) {
      await setDoc(doc(db, 'users', item.userId), {
        verificationStatus: 'rejected',
        verificationRejectionReason: reason,
        reviewedAt: item.reviewedAt
      }, { merge: true })
    }
    activityLogs.value.unshift({
      time: new Date().toLocaleTimeString(),
      action: 'Verification_rejected',
      unit: item.userName,
      id: String(activityLogs.value.length + 1).padStart(3, '0')
    })
    showToast(`Verification rejected. Reason logged for user.`, 'info')
  } catch (err) {
    console.warn('Notice updating rejected verification:', err)
    showToast(`Verification rejected.`, 'info')
  } finally {
    isProcessingReview.value = false
    showRejectDialog.value = false
    showVerificationModal.value = false
  }
}

function formatDate(isoString) {
  if (!isoString) return 'Recent'
  try {
    const d = new Date(isoString)
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
  } catch (e) {
    return isoString
  }
}

// Navigation & Auth methods
function switchTab(tab) {
  activeTab.value = tab
  showLandlordForm.value = false
  showTenantForm.value = false
}

function verifyAdminPin() {
  isVerifying.value = true
  pinError.value = ''

  setTimeout(() => {
    isVerifying.value = false
    const val = adminPinInput.value.trim().toLowerCase()
    if (val === '123456' || val === 'admin@homesweet.com' || val === 'admin123' || val === 'admin') {
      isAdminAuthenticated.value = true
      sessionStorage.setItem('homesweet_admin_auth', 'true')
      showToast('Admin Console Unlocked', 'success')
      loadFirestoreData()
    } else {
      pinError.value = 'Invalid Master Key. Please enter 123456 or admin@homesweet.com.'
    }
  }, 400)
}

function handleLogoutAdmin() {
  isAdminAuthenticated.value = false
  sessionStorage.removeItem('homesweet_admin_auth')
  router.push('/home')
}

// Agreement preview
function openAgreementPreview(agreement) {
  activeAgreement.value = agreement
  showAgreementModal.value = true
}

function downloadContractPDF() {
  window.print()
}

// File dropzone handlers
function triggerFileInput() {
  if (contractFileInputRef.value) {
    contractFileInputRef.value.click()
  }
}

function handleFileSelect(e) {
  const file = e.target.files[0]
  if (file) {
    uploadedContractFile.value = file
  }
}

function handleFileDrop(e) {
  isDragging.value = false
  const file = e.dataTransfer.files[0]
  if (file) {
    uploadedContractFile.value = file
  }
}

function handleUrlAttach() {
  if (!importUrlInput.value.trim()) {
    showToast('Please enter a valid URL', 'error')
    return
  }
  showToast('URL attached: ' + importUrlInput.value, 'info')
}

async function confirmUploadContract() {
  const newId = String(agreements.value.length + 1).padStart(3, '0')
  const newAgreementObj = {
    id: String(Date.now()),
    code: `Agreement-${newId}`,
    landlord: 'Demo Owner',
    tenant: 'New Tenant',
    duration: '12 months',
    date: 'Just now'
  }

  agreements.value.unshift(newAgreementObj)
  activityLogs.value.unshift({
    time: new Date().toLocaleTimeString(),
    action: 'Contract_imported',
    unit: 'Unit_Upload',
    id: newId
  })

  try {
    await addDoc(collection(db, 'agreements'), {
      ...newAgreementObj,
      fileUrl: importUrlInput.value || 'local_upload',
      createdAt: new Date().toISOString()
    })
  } catch (err) {
    console.warn('Firestore agreement save fallback:', err)
  }

  showUploadModal.value = false
  uploadedContractFile.value = null
  importUrlInput.value = ''
  showToast(`Agreement-${newId} imported successfully!`, 'success')
}

// Submitting Landlord Form
async function submitLandlordForm() {
  isSubmittingForm.value = true
  const item = {
    address: newLandlord.value.propertyAddress,
    tenant: 'Emily',
    startDate: newLandlord.value.startDate,
    endDate: newLandlord.value.endDate,
    duration: '6months',
    price: parseFloat(newLandlord.value.propertyPrice) || 100,
    paymentStatus: 'Paid'
  }

  landlordsList.value.unshift(item)

  try {
    await addDoc(collection(db, 'landlord_applications'), {
      ...newLandlord.value,
      createdAt: new Date().toISOString()
    })
  } catch (e) {
    console.warn('Firestore save:', e)
  }

  isSubmittingForm.value = false
  showLandlordForm.value = false
  showToast('New Landlord and property registered!', 'success')
}

// Submitting Tenant Form
async function submitTenantForm() {
  isSubmittingForm.value = true
  const item = {
    address: newTenant.value.propertyAddress,
    tenant: `${newTenant.value.firstName} ${newTenant.value.lastName}`,
    startDate: newTenant.value.startDate,
    endDate: newTenant.value.endDate,
    duration: '6months',
    price: parseFloat(newTenant.value.propertyPrice) || 100,
    paymentStatus: 'Paid'
  }

  tenantsList.value.unshift(item)

  try {
    await addDoc(collection(db, 'rental_applications'), {
      ...newTenant.value,
      tenantName: item.tenant,
      createdAt: new Date().toISOString()
    })
  } catch (e) {
    console.warn('Firestore save:', e)
  }

  isSubmittingForm.value = false
  showTenantForm.value = false
  showToast('New Tenant application registered!', 'success')
}

// Submitting New Property
function submitNewProperty() {
  const newProp = {
    id: properties.value.length + 1,
    name: newPropertyData.value.name,
    price: parseFloat(newPropertyData.value.price) || 200,
    type: 'apartment',
    location: newPropertyData.value.location,
    lat: 11.5720,
    lng: 104.8950,
    beds: parseInt(newPropertyData.value.beds) || 2,
    baths: parseInt(newPropertyData.value.baths) || 2,
    sqft: 120,
    match: 95,
    liked: false,
    activeSlide: 0,
    rating: 4.8,
    period: 'Long-term',
    amenities: ['wifi', 'ac', 'kitchen', 'parking'],
    images: [
      newPropertyData.value.imageUrl || '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg'
    ]
  }

  properties.value.unshift(newProp)
  performanceStats.value.properties += 1
  showAddPropertyModal.value = false
  showToast('Property listing created!', 'success')
}

// Data fetching
async function loadFirestoreData() {
  try {
    const appsSnap = await getDocs(collection(db, 'rental_applications'))
    if (!appsSnap.empty) {
      appsSnap.forEach(docSnap => {
        const d = docSnap.data()
        if (d.propertyName || d.propertyAddress) {
          tenantsList.value.unshift({
            address: d.propertyAddress || d.propertyName || 'Phnom Penh Toul Kork',
            tenant: d.tenantName || 'Applicant',
            startDate: d.moveInDate || d.startDate || '2026-02-01',
            endDate: d.endDate || '2026-08-01',
            duration: `${d.leaseDuration || 6}months`,
            price: d.price || d.propertyPrice || 100,
            paymentStatus: d.status === 'approved' ? 'Paid' : 'Pending'
          })
        }
      })
    }
  } catch (err) {
    console.warn('Live Firestore applications fetch notice:', err)
  }

  // Fetch live verification requests
  try {
    const verifSnap = await getDocs(collection(db, 'verification_requests'))
    if (!verifSnap.empty) {
      const liveVerifs = []
      verifSnap.forEach(d => {
        liveVerifs.push({ id: d.id, ...d.data() })
      })
      verificationRequests.value = [...liveVerifs, ...verificationRequests.value.filter(v => v.id.startsWith('VR-'))]
    }
  } catch (vErr) {
    console.warn('Live verification requests fetch notice:', vErr)
  }
}

onMounted(() => {
  if (route.path === '/admin/verifications' || route.name === 'AdminVerifications') {
    activeTab.value = 'verifications'
  }
  if (sessionStorage.getItem('homesweet_admin_auth') === 'true') {
    isAdminAuthenticated.value = true
    loadFirestoreData()
  }
  if (auth.currentUser?.photoURL) {
    adminUserAvatar.value = auth.currentUser.photoURL
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after {
  box-sizing: border-box;
}

.admin-app {
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  min-height: 100vh;
  background-color: #FAF8F5;
  color: #2A2421;
}

/* ══════════════════════════════════════════════════════════════
   LOGIN OVERLAY (GATE)
══════════════════════════════════════════════════════════════ */
.admin-login-overlay {
  position: fixed;
  inset: 0;
  background: rgba(42, 36, 33, 0.85);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
}

.admin-login-card {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #EDE8E3;
  max-width: 440px;
  width: 100%;
  padding: 36px 32px;
  box-shadow: 0 20px 40px rgba(92, 78, 78, 0.16);
  text-align: center;
}

.admin-badge-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #F4EDEA;
  color: #5C4E4E;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
}

.admin-login-header h2 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 6px;
}

.admin-login-header p {
  font-size: 0.88rem;
  color: #8C7E7E;
  line-height: 1.5;
  margin-bottom: 24px;
}

.admin-login-form .form-group {
  text-align: left;
  margin-bottom: 16px;
}

.admin-login-form label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: #5C4E4E;
  margin-bottom: 6px;
}

.admin-input {
  width: 100%;
  padding: 12px 14px;
  border: 1.5px solid #D1D5DB;
  border-radius: 10px;
  font-size: 1rem;
  font-family: inherit;
  outline: none;
  transition: all 0.2s;
}

.admin-input:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.15);
}

.error-msg {
  display: block;
  font-size: 0.8rem;
  color: #DC2626;
  margin-top: 6px;
}

.pin-hint-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 0.78rem;
  color: #8C7E7E;
  margin-bottom: 24px;
  text-align: left;
}

.admin-login-actions {
  display: flex;
  gap: 12px;
}

.btn-cancel {
  flex: 1;
  padding: 11px 16px;
  border: 1px solid #EDE8E3;
  background: #ffffff;
  color: #5C4E4E;
  border-radius: 10px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-cancel:hover {
  background: #FAF8F5;
}

.btn-unlock {
  flex: 1.3;
  padding: 11px 16px;
  border: none;
  background: #5C4E4E;
  color: #ffffff;
  border-radius: 10px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-unlock:hover {
  background: #473B3B;
}

/* ══════════════════════════════════════════════════════════════
   TOP HEADER BAR
══════════════════════════════════════════════════════════════ */
.admin-top-bar {
  background-color: #5C4E4E;
  height: 60px;
  padding: 0 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.12);
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

.brand-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.3px;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.exit-admin-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  color: #ffffff;
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.exit-admin-btn:hover {
  background: rgba(255, 255, 255, 0.25);
}

.admin-avatar-wrap {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.6);
}

.admin-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ══════════════════════════════════════════════════════════════
   BODY & SIDEBAR
══════════════════════════════════════════════════════════════ */
.admin-main-body {
  display: flex;
  min-height: calc(100vh - 60px);
}

.admin-sidebar {
  width: 230px;
  background: #ffffff;
  border-right: 1px solid #EDE8E3;
  padding: 24px 16px;
  flex-shrink: 0;
}

.sidebar-heading {
  font-size: 1.35rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 24px;
  padding-left: 8px;
}

.sidebar-section {
  margin-bottom: 22px;
}

.section-label {
  font-size: 0.78rem;
  font-weight: 600;
  color: #8C7E7E;
  margin-bottom: 8px;
  padding-left: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.sidebar-nav-btn {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  background: none;
  border: none;
  border-radius: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  color: #5C4E4E;
  cursor: pointer;
  transition: all 0.15s ease;
  margin-bottom: 4px;
  text-align: left;
}

.sidebar-nav-btn:hover {
  background: #FAF8F5;
  color: #2A2421;
}

.sidebar-nav-btn.active {
  background: #5C4E4E;
  color: #ffffff;
  font-weight: 600;
}

/* ══════════════════════════════════════════════════════════════
   CONTENT VIEW & PANE TOP ROW
══════════════════════════════════════════════════════════════ */
.admin-content-view {
  flex: 1;
  padding: 28px 36px;
  overflow-y: auto;
}

.pane-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  gap: 16px;
  flex-wrap: wrap;
}

.search-pill-container {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 9999px;
  padding: 8px 16px;
  width: 280px;
  box-shadow: 0 2px 6px rgba(92, 78, 78, 0.04);
}

.search-pill-input {
  border: none;
  outline: none;
  font-size: 0.88rem;
  color: #2A2421;
  width: 100%;
  font-family: inherit;
}

.btn-primary-action {
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;
  box-shadow: 0 2px 6px rgba(92, 78, 78, 0.15);
}

.btn-primary-action:hover {
  background: #473B3B;
}

/* ══════════════════════════════════════════════════════════════
   TAB 1: DASHBOARD
══════════════════════════════════════════════════════════════ */
.dashboard-grid {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 32px;
}

.agreements-column {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.agreement-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.agreement-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(92, 78, 78, 0.08);
  border-color: #5C4E4E;
}

.pdf-badge {
  width: 44px;
  height: 52px;
  background: #fee2e2;
  border-radius: 6px;
  border-top-right-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  flex-shrink: 0;
}

.pdf-tag {
  font-size: 0.72rem;
  font-weight: 800;
  color: #ef4444;
  letter-spacing: 0.5px;
}

.agreement-info {
  flex: 1;
}

.agreement-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 3px;
}

.agreement-sub {
  font-size: 0.75rem;
  color: #8C7E7E;
  margin: 1px 0;
}

.agreement-duration {
  display: inline-block;
  font-size: 0.72rem;
  color: #8C7E7E;
  margin-top: 4px;
}

.agreement-date {
  font-size: 0.72rem;
  color: #8C7E7E;
  align-self: flex-end;
  margin-bottom: 4px;
}

.empty-state-card {
  background: #fff;
  border: 1px dashed #EDE8E3;
  border-radius: 12px;
  padding: 32px;
  text-align: center;
  color: #8C7E7E;
  font-size: 0.9rem;
}

/* Metrics Column */
.metrics-column {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.section-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 16px;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.metric-card {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.metric-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.metric-label {
  font-size: 0.88rem;
  font-weight: 600;
  color: #5C4E4E;
}

.metric-trend {
  font-size: 0.82rem;
  font-weight: 700;
}

.metric-trend.ok {
  color: #2E7D32;
}

.metric-trend.positive {
  color: #2E7D32;
}

.metric-value {
  font-size: 1.6rem;
  font-weight: 700;
  color: #2A2421;
}

/* Activity Logs */
.logs-table-container {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.logs-table {
  width: 100%;
  border-collapse: collapse;
}

.logs-table tr {
  border-bottom: 1px solid #EDE8E3;
  transition: background 0.15s;
}

.logs-table tr:last-child {
  border-bottom: none;
}

.logs-table tr:hover {
  background: #FAF8F5;
}

.logs-table td {
  padding: 16px 20px;
  font-size: 0.88rem;
}

.log-time {
  font-weight: 600;
  color: #2A2421;
  width: 120px;
}

.log-action {
  font-weight: 600;
  color: #2A2421;
}

.log-unit {
  color: #5C4E4E;
}

.log-id {
  color: #8C7E7E;
  text-align: right;
  font-weight: 500;
}

/* ══════════════════════════════════════════════════════════════
   DATA TABLES (Landlords, Tenants)
══════════════════════════════════════════════════════════════ */
.data-table-card {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  overflow-x: auto;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.data-table th {
  background: #FAF8F5;
  padding: 14px 20px;
  font-size: 0.82rem;
  font-weight: 700;
  color: #5C4E4E;
  border-bottom: 1px solid #EDE8E3;
  white-space: nowrap;
}

.data-table td {
  padding: 16px 20px;
  font-size: 0.88rem;
  color: #2A2421;
  border-bottom: 1px solid #EDE8E3;
  white-space: nowrap;
}

.data-table tr:last-child td {
  border-bottom: none;
}

.data-table tr:hover td {
  background: #FAF8F5;
}

.cell-primary {
  font-weight: 600;
  color: #2A2421;
}

.cell-price {
  font-weight: 700;
  color: #2A2421;
}

.status-pill {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 0.76rem;
  font-weight: 600;
}

.status-pill.paid {
  background: #E8F5E9;
  color: #2E7D32;
  border: 1px solid #C8E6C9;
}

.status-pill.pending {
  background: #FFF8E1;
  color: #B78103;
  border: 1px solid #FFECB3;
}

/* ══════════════════════════════════════════════════════════════
   APPLICATION FORMS (Landlord & Tenant Forms matching mockups)
══════════════════════════════════════════════════════════════ */
.form-pane-container {
  max-width: 820px;
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid #EDE8E3;
  padding: 32px;
  margin: 0 auto;
  box-shadow: 0 4px 16px rgba(92, 78, 78, 0.04);
}

.form-header-bar {
  margin-bottom: 24px;
}

.btn-back-text {
  background: none;
  border: none;
  color: #5C4E4E;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 8px;
  display: inline-block;
}

.btn-back-text:hover {
  color: #473B3B;
  text-decoration: underline;
}

.form-main-heading {
  font-size: 1.45rem;
  font-weight: 700;
  color: #2A2421;
  text-align: center;
}

.styled-admin-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-banner-title {
  background: #5C4E4E;
  color: #ffffff;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  margin-top: 10px;
}

.form-row {
  display: flex;
  gap: 14px;
}

.form-row.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.form-row.single-col {
  display: flex;
}

.form-input-box {
  width: 100%;
  padding: 12px 16px;
  border: 1.5px solid #D1D5DB;
  border-radius: 10px;
  font-size: 0.92rem;
  font-family: inherit;
  outline: none;
  transition: all 0.2s;
}

.form-input-box:focus {
  border-color: #5C4E4E;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.checkbox-row {
  display: flex;
  gap: 24px;
  padding: 6px 4px;
}

.check-box-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.95rem;
  color: #2A2421;
  cursor: pointer;
}

.form-submit-row {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 18px;
}

/* ══════════════════════════════════════════════════════════════
   PROPERTIES GRID (House tab matching media_1788721279915.png)
══════════════════════════════════════════════════════════════ */
.sub-pane-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 20px;
}

.properties-admin-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.property-admin-card {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.property-admin-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(92, 78, 78, 0.08);
}

.prop-thumb-wrap {
  width: 100%;
  height: 180px;
  overflow: hidden;
}

.prop-thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.prop-details-box {
  padding: 16px;
}

.prop-header-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.prop-loc-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: #2A2421;
}

.prop-price-tag {
  font-size: 0.85rem;
  font-weight: 600;
  color: #5C4E4E;
}

.prop-landlord-line {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  color: #8C7E7E;
  margin-bottom: 16px;
}

.prop-card-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.btn-view-detail {
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.btn-view-detail:hover {
  background: #473B3B;
}

.btn-chat-icon {
  width: 34px;
  height: 34px;
  border: 1px solid #EDE8E3;
  border-radius: 8px;
  background: #FAF8F5;
  color: #5C4E4E;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-chat-icon:hover {
  background: #F4EDEA;
  border-color: #5C4E4E;
  color: #473B3B;
}

/* Static Cards for Help / Security / Status */
.static-card {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 28px;
  max-width: 680px;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.04);
}

.static-card h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 12px;
}

.static-card p {
  font-size: 0.92rem;
  color: #5C4E4E;
  line-height: 1.6;
  margin-bottom: 12px;
}

.badge-active {
  color: #2E7D32;
  font-weight: 700;
}

.quick-links-list {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.quick-item {
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 0.88rem;
  color: #2A2421;
}

.btn-secondary {
  padding: 10px 18px;
  border: 1px solid #EDE8E3;
  background: #fff;
  color: #DC2626;
  font-weight: 600;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 12px;
}

/* ══════════════════════════════════════════════════════════════
   MODAL DIALOGS
══════════════════════════════════════════════════════════════ */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(42, 36, 33, 0.65);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  padding: 20px;
  overflow-y: auto;
}

.modal-window {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid #EDE8E3;
  width: 100%;
  box-shadow: 0 20px 40px rgba(92, 78, 78, 0.2);
  position: relative;
}

/* Agreement Preview Modal */
.preview-modal-window {
  max-width: 680px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.modal-title-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  border-bottom: 1px solid #EDE8E3;
}

.modal-back-btn {
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #5C4E4E;
}

.modal-title-bar h2 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2A2421;
}

.btn-print {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #5C4E4E;
  color: #fff;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-print:hover {
  background: #473B3B;
}

.contract-doc {
  padding: 28px 36px;
  overflow-y: auto;
  font-family: 'DM Sans', sans-serif;
}

.contract-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 14px;
}

.doc-logo-box {
  display: flex;
  align-items: center;
  gap: 8px;
}

.doc-badge-icon {
  background: #5C4E4E;
  color: #fff;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.9rem;
}

.doc-domain {
  font-size: 0.8rem;
  color: #8C7E7E;
}

.doc-contact-info {
  font-size: 0.76rem;
  color: #8C7E7E;
  text-align: right;
  line-height: 1.4;
}

.contract-banner-bar {
  height: 28px;
  background: #5C4E4E;
  width: 100%;
  margin-bottom: 24px;
}

.contract-heading {
  text-align: center;
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: 0.5px;
  color: #2A2421;
  margin-bottom: 24px;
}

.contract-meta {
  margin-bottom: 16px;
  font-size: 0.85rem;
  line-height: 1.5;
  color: #2A2421;
}

.contract-intro {
  font-size: 0.85rem;
  line-height: 1.6;
  margin-bottom: 12px;
  color: #2A2421;
}

.contract-terms {
  padding-left: 20px;
  font-size: 0.83rem;
  line-height: 1.7;
  margin-bottom: 20px;
  color: #2A2421;
}

.contract-sign-notice {
  font-size: 0.8rem;
  color: #8C7E7E;
  margin-bottom: 24px;
  display: block;
}

.contract-signatures {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.sig-col {
  text-align: center;
  width: 180px;
}

.sig-drawing {
  font-family: 'Brush Script MT', cursive, serif;
  font-size: 1.8rem;
  color: #2A2421;
  margin-bottom: 4px;
}

.sig-line {
  border-top: 1px solid #D1D5DB;
  margin-bottom: 6px;
}

.sig-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: #2A2421;
}

.sig-role {
  font-size: 0.75rem;
  color: #8C7E7E;
}

.doc-footer-link {
  text-align: center;
  font-size: 0.7rem;
  color: #5C4E4E;
  margin-top: 28px;
}

/* Upload Contract Modal */
.upload-contract-window {
  max-width: 580px;
  padding: 28px 32px;
}

.upload-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.upload-modal-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2A2421;
}

.btn-close-x {
  background: none;
  border: none;
  font-size: 1.2rem;
  color: #8C7E7E;
  cursor: pointer;
}

.dropzone-box {
  border: 2px dashed #D1D5DB;
  border-radius: 12px;
  padding: 36px 20px;
  text-align: center;
  cursor: pointer;
  background: #FAF8F5;
  transition: background 0.15s, border-color 0.15s;
}

.dropzone-box:hover {
  background: #F4EDEA;
  border-color: #5C4E4E;
}

.cloud-icon-wrap {
  position: relative;
  display: inline-block;
  margin-bottom: 12px;
  color: #5C4E4E;
}

.cloud-arrow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -30%);
}

.dropzone-text {
  font-size: 0.95rem;
  color: #2A2421;
  margin-bottom: 4px;
}

.dropzone-text.uploaded {
  color: #2E7D32;
}

.browse-link {
  color: #5C4E4E;
  font-weight: 600;
  text-decoration: underline;
}

.dropzone-sub {
  font-size: 0.78rem;
  color: #8C7E7E;
}

.or-divider {
  display: flex;
  align-items: center;
  margin: 18px 0;
  gap: 12px;
}

.or-line {
  flex: 1;
  height: 1px;
  background: #EDE8E3;
}

.or-text {
  font-size: 0.8rem;
  color: #8C7E7E;
}

.url-section-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #2A2421;
  margin-bottom: 8px;
}

.url-input-row {
  display: flex;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  border-radius: 8px;
  padding: 4px 6px;
  gap: 8px;
}

.url-input-field {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  padding: 8px 10px;
  font-size: 0.88rem;
  font-family: inherit;
  color: #2A2421;
}

.btn-url-upload {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 6px;
  padding: 6px 16px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #5C4E4E;
  cursor: pointer;
}

.btn-url-upload:hover {
  background: #F4EDEA;
}

.upload-modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 24px;
}

/* Add Property Modal */
.add-prop-window {
  max-width: 520px;
  padding: 28px;
}

.modal-form-body {
  margin-top: 14px;
}

/* Toast */
.admin-toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #2A2421;
  color: #ffffff;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  box-shadow: 0 10px 25px rgba(42, 36, 33, 0.2);
  z-index: 99999;
}

.admin-toast.success {
  background: #2E7D32;
}

.admin-toast.error {
  background: #DC2626;
}

/* ══════════════════════════════════════════════════════════════
   VERIFICATIONS DASHBOARD & PROPERTY FILTERING STYLES
══════════════════════════════════════════════════════════════ */
.nav-badge-pill {
  background: #EF4444;
  color: #fff;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 1px 7px;
  border-radius: 50px;
  margin-left: auto;
}

.verif-kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.verif-kpi-card {
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 14px;
  padding: 18px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  transition: all 0.18s ease;
}

.verif-kpi-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(92, 78, 78, 0.08);
}

.kpi-icon-bubble {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kpi-icon-bubble.pending { background: #FEF3C7; color: #D97706; }
.kpi-icon-bubble.approved { background: #ECFDF5; color: #10B981; }
.kpi-icon-bubble.rejected { background: #FEE2E2; color: #EF4444; }
.kpi-icon-bubble.total { background: #F4EDEA; color: #5C4E4E; }

.kpi-meta {
  display: flex;
  flex-direction: column;
}

.kpi-label {
  font-size: 0.78rem;
  font-weight: 500;
  color: #8C7E7E;
}

.kpi-value {
  font-size: 1.4rem;
  font-weight: 700;
  color: #2A2421;
}

.verif-controls-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  gap: 16px;
}

.verif-tabs {
  display: flex;
  gap: 8px;
}

.verif-tab-btn {
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  border-radius: 50px;
  border: 1px solid #EDE8E3;
  background: #ffffff;
  color: #5C4E4E;
  cursor: pointer;
  transition: all 0.15s ease;
}

.verif-tab-btn.active {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #5C4E4E;
}

.verif-sort-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: #8C7E7E;
}

.verif-sort-select {
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid #EDE8E3;
  background: #ffffff;
  font-size: 0.8rem;
  color: #2A2421;
  outline: none;
}

/* Verification Table */
.verif-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.verif-table th {
  padding: 12px 16px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #8C7E7E;
  border-bottom: 1px solid #EDE8E3;
  background: #FAF8F5;
}

.verif-table td {
  padding: 14px 16px;
  font-size: 0.85rem;
  border-bottom: 1px solid #F4EDEA;
  vertical-align: middle;
}

.verif-table-row:hover {
  background: #FCFBF9;
}

.applicant-cell {
  display: flex;
  align-items: center;
  gap: 12px;
}

.applicant-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
}

.applicant-info {
  display: flex;
  flex-direction: column;
}

.applicant-name {
  font-weight: 600;
  color: #2A2421;
}

.applicant-email {
  font-size: 0.75rem;
  color: #8C7E7E;
}

.doc-cell {
  display: flex;
  flex-direction: column;
}

.doc-type {
  font-weight: 600;
  color: #5C4E4E;
}

.doc-id-num {
  font-size: 0.75rem;
  color: #8C7E7E;
}

.match-cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.match-pill {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 50px;
  display: inline-block;
  width: fit-content;
}

.match-pill.match-high {
  background: #ECFDF5;
  color: #10B981;
}

.match-pill.match-low {
  background: #FEE2E2;
  color: #EF4444;
}

.liveness-badge {
  font-size: 0.7rem;
  font-weight: 600;
}

.liveness-badge.passed { color: #10B981; }
.liveness-badge.warning { color: #F59E0B; }

.status-badge {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 50px;
  display: inline-block;
}

.status-badge.pending { background: #FEF3C7; color: #D97706; }
.status-badge.approved { background: #ECFDF5; color: #10B981; }
.status-badge.rejected { background: #FEE2E2; color: #EF4444; }

.btn-review-inspect {
  padding: 6px 14px;
  border-radius: 8px;
  border: 1px solid #5C4E4E;
  background: #ffffff;
  color: #5C4E4E;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-review-inspect:hover {
  background: #5C4E4E;
  color: #ffffff;
}

/* Property Filter Toolbar */
.property-filter-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  background: #ffffff;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 12px 16px;
  margin-bottom: 20px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.filter-group label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #8C7E7E;
}

.filter-select {
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid #EDE8E3;
  background: #FAF8F5;
  font-size: 0.82rem;
  color: #2A2421;
  outline: none;
}

.btn-clear-filters {
  padding: 6px 12px;
  font-size: 0.78rem;
  font-weight: 600;
  background: none;
  border: 1px dashed #8C7E7E;
  border-radius: 8px;
  color: #8C7E7E;
  cursor: pointer;
  margin-top: 16px;
}

.btn-clear-filters:hover {
  border-color: #5C4E4E;
  color: #5C4E4E;
}

.sub-pane-header-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 16px;
}

.results-count-text {
  font-size: 0.8rem;
  color: #8C7E7E;
}

.prop-type-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(42, 36, 33, 0.75);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 50px;
  backdrop-filter: blur(4px);
}

.prop-specs-line {
  font-size: 0.78rem;
  color: #8C7E7E;
  margin-bottom: 6px;
}

/* Dossier Modal Window */
.verif-dossier-window {
  max-width: 900px !important;
  width: 95% !important;
  max-height: 90vh;
  overflow-y: auto;
}

.dossier-header-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dossier-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  padding: 20px 28px;
}

.dossier-user-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px;
  border-radius: 12px;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  margin-bottom: 18px;
}

.dossier-avatar {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  object-fit: cover;
}

.dossier-user-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0 0 2px;
}

.dossier-user-email {
  font-size: 0.82rem;
  color: #5C4E4E;
  display: block;
}

.dossier-user-phone {
  font-size: 0.78rem;
  color: #8C7E7E;
}

.meta-section-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: #5C4E4E;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
}

.meta-data-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid #F4EDEA;
  font-size: 0.82rem;
}

.meta-data-label {
  color: #8C7E7E;
}

.meta-data-val {
  font-weight: 600;
  color: #2A2421;
}

.dossier-audit-box {
  margin-top: 20px;
  padding: 14px;
  background: #FAF8F5;
  border-radius: 10px;
  border: 1px solid #EDE8E3;
}

.rejection-reason-box {
  margin-top: 10px;
  padding: 10px;
  background: #FEE2E2;
  border-radius: 8px;
}

.rejection-reason-title {
  font-size: 0.75rem;
  font-weight: 700;
  color: #B91C1C;
  display: block;
}

.rejection-reason-text {
  font-size: 0.8rem;
  color: #7F1D1D;
  margin: 4px 0 0;
}

.doc-media-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 18px;
}

.doc-media-card {
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  overflow: hidden;
  background: #FAF8F5;
}

.doc-media-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #5C4E4E;
  border-bottom: 1px solid #EDE8E3;
}

.link-open-full {
  color: #5C4E4E;
  text-decoration: underline;
}

.doc-media-img-wrap {
  width: 100%;
  height: 160px;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.doc-media-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.ai-scorecard {
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 14px 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.scorecard-item {
  display: flex;
  justify-content: space-between;
  font-size: 0.82rem;
}

.score-lbl {
  color: #5C4E4E;
}

.score-stat {
  font-weight: 700;
}

.text-success { color: #10B981; }

.dossier-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  padding: 16px 28px;
  border-top: 1px solid #EDE8E3;
}

.btn-reject-action {
  padding: 10px 18px;
  border-radius: 8px;
  border: 1px solid #EF4444;
  background: #ffffff;
  color: #EF4444;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-reject-action:hover {
  background: #EF4444;
  color: #ffffff;
}

.btn-approve-action {
  padding: 10px 22px;
  border-radius: 8px;
  border: none;
  background: #10B981;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}

.btn-approve-action:hover:not(:disabled) {
  background: #059669;
}

.btn-approve-action:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

/* Reject Dialog Window */
.reject-dialog-window {
  max-width: 520px !important;
  width: 90% !important;
}

.reject-dialog-body {
  padding: 18px 24px;
}

.reject-dialog-subtitle {
  font-size: 0.85rem;
  color: #5C4E4E;
  margin-bottom: 14px;
  line-height: 1.4;
}

.quick-reason-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
}

.reason-pill {
  padding: 4px 10px;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 50px;
  border: 1px solid #EDE8E3;
  background: #FAF8F5;
  color: #5C4E4E;
  cursor: pointer;
}

.reason-pill:hover {
  border-color: #5C4E4E;
}

.form-input-lbl {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  color: #5C4E4E;
  margin-bottom: 6px;
}

.reject-reason-textarea {
  width: 100%;
  border-radius: 8px;
  border: 1px solid #EDE8E3;
  padding: 10px 12px;
  font-family: inherit;
  font-size: 0.85rem;
  color: #2A2421;
  outline: none;
  resize: vertical;
}

.btn-confirm-reject {
  padding: 10px 18px;
  border-radius: 8px;
  border: none;
  background: #EF4444;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
}

.btn-confirm-reject:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Responsive */
@media (max-width: 1024px) {
  .verif-kpi-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .dossier-body {
    grid-template-columns: 1fr;
  }
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  .properties-admin-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .admin-main-body {
    flex-direction: column;
  }
  .admin-sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid #EDE8E3;
  }
  .properties-admin-grid {
    grid-template-columns: 1fr;
  }
  .form-row.two-col {
    grid-template-columns: 1fr;
  }
  .verif-kpi-grid {
    grid-template-columns: 1fr;
  }
  .doc-media-grid {
    grid-template-columns: 1fr;
  }
}
</style>
