<template>
  <div class="search-experience-wrapper" :class="{ 'fullscreen-active': isFullScreenMap }">
    
    <!-- ======================================================== -->
    <!-- 1. DEFAULT VIEW HEADER (Plum Guide Style Luxury Header)   -->
    <!-- ======================================================== -->
    <header v-if="!isFullScreenMap" class="plum-nav-header">
      <!-- Left: Logo & Brand -->
      <div class="plum-brand" @click="$router.push('/home')">
        <div class="plum-brand-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#221e1e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 18 L16 18" />
            <path d="M4 18 L4 12 L9 7 L16 14" />
            <path d="M12 18 L12 4 L16 4 L16 18 Z" />
            <path d="M12 14 L16 14" />
          </svg>
        </div>
        <span class="plum-brand-text">HomeSweet</span>
      </div>

      <!-- Center: Plum Guide Search Capsule (Destination | Dates | Guests | Search) -->
      <div class="plum-search-capsule">
        <div class="capsule-col destination-col">
          <label class="capsule-label">Where</label>
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Add destination" 
            class="capsule-input" 
          />
        </div>

        <div class="capsule-divider"></div>

        <div class="capsule-col dates-col" @click="cycleDates">
          <label class="capsule-label">When</label>
          <span class="capsule-value">{{ selectedDatesLabel }}</span>
        </div>

        <div class="capsule-divider"></div>

        <div class="capsule-col guests-col" @click="cycleGuests">
          <label class="capsule-label">Who</label>
          <span class="capsule-value">{{ guestsLabel }}</span>
        </div>

        <button type="button" class="capsule-search-btn" title="Search properties" @click="recenterMap">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.8">
            <circle cx="11" cy="11" r="8" />
            <path d="M21 21l-4.35-4.35" />
          </svg>
        </button>
      </div>

      <!-- Right: Actions & User Profile -->
      <div class="plum-header-right">
        <button 
          type="button" 
          class="btn-plum-filter" 
          :class="{ active: isFilterPopoverOpen }"
          @click="isFilterPopoverOpen = !isFilterPopoverOpen"
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="4" y1="21" x2="4" y2="14"/>
            <line x1="4" y1="10" x2="4" y2="3"/>
            <line x1="12" y1="21" x2="12" y2="12"/>
            <line x1="12" y1="8" x2="12" y2="3"/>
            <line x1="20" y1="21" x2="20" y2="16"/>
            <line x1="20" y1="12" x2="20" y2="3"/>
            <line x1="1" y1="14" x2="7" y2="14"/>
            <line x1="9" y1="8" x2="15" y2="8"/>
            <line x1="17" y1="16" x2="23" y2="16"/>
          </svg>
          <span>Filter & Sort</span>
        </button>

        <span class="plum-nav-link" @click="$router.push('/home')">Become a host</span>

        <div class="plum-lang-currency">
          <span>EN | $</span>
        </div>

        <div class="plum-user-avatar-wrap" @click="$router.push('/home')">
          <img 
            :src="userProfile.avatar || defaultAvatar" 
            referrerpolicy="no-referrer" 
            @error="setDefaultAvatar" 
            alt="User" 
            class="plum-avatar-img"
          />
        </div>
      </div>
    </header>


    <!-- End of Default Plum Guide Header -->


    <!-- ======================================================== -->
    <!-- 3. MAIN WORKSPACE: SPLIT VIEW OR FULLSCREEN MAP          -->
    <!-- ======================================================== -->
    <main class="search-main-workspace" :class="{ 'is-fullscreen-layout': isFullScreenMap }">
      
      <!-- LEFT LISTINGS COLUMN (Visible in Default Split Mode) -->
      <section v-show="!isFullScreenMap" class="plum-listings-column">
        <!-- Header Info Bar -->
        <div class="listings-summary-header">
          <h2 class="listings-count-title">{{ filteredProperties.length }}+ homes available</h2>
          <p class="listings-subtitle">
            Curated, verified homes in Phnom Penh, so you don't have to worry.
            <a href="javascript:void(0)" class="standards-link">Learn about our standards</a>
          </p>
        </div>

        <!-- Horizontal Property Cards Feed -->
        <div class="plum-cards-list">
          <article 
            v-for="prop in filteredProperties" 
            :key="prop.id" 
            class="plum-property-card"
            :class="{ 'card-active-selected': selectedProperty && selectedProperty.id === prop.id }"
            @click="selectProperty(prop)"
          >
            <!-- Left: Card Media 16:9 Carousel -->
            <div class="plum-card-media-box">
              <img 
                :src="prop.images[prop.activeSlide || 0] || prop.images[0]" 
                :alt="prop.name" 
                class="plum-card-cover-img"
              />

              <!-- Heart Button -->
              <button 
                type="button" 
                class="plum-heart-btn" 
                :class="{ liked: prop.liked }" 
                title="Save home"
                @click.stop="prop.liked = !prop.liked"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" :fill="prop.liked ? '#ef4444' : 'rgba(0,0,0,0.3)'" :stroke="prop.liked ? '#ef4444' : '#ffffff'" stroke-width="2">
                  <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z" />
                </svg>
              </button>

              <!-- Carousel Pagination Dots -->
              <div v-if="prop.images && prop.images.length > 1" class="plum-media-dots">
                <span 
                  v-for="(_, idx) in prop.images.slice(0, 4)" 
                  :key="idx" 
                  class="plum-dot"
                  :class="{ active: (prop.activeSlide || 0) === idx }"
                  @click.stop="prop.activeSlide = idx"
                ></span>
              </div>
            </div>

            <!-- Right: Card Metadata & Info -->
            <div class="plum-card-details-box">
              <div class="plum-card-top-row">
                <h3 class="plum-property-name">{{ prop.name }}</h3>
                <span class="plum-property-rating">★ {{ prop.rating || 4.9 }}</span>
              </div>

              <div class="plum-property-location">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{{ prop.location }}</span>
              </div>

              <div class="plum-property-specs">
                <span>{{ prop.baths * 2 }} guests</span>
                <span class="spec-dot">•</span>
                <span>{{ prop.beds }} bedrooms</span>
                <span class="spec-dot">•</span>
                <span>{{ prop.baths }} bathrooms</span>
                <span class="spec-dot">•</span>
                <span>{{ prop.sqft }} m²</span>
              </div>

              <div class="plum-features-row">
                <span class="plum-badge-free-cancel">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <polyline points="9 12 11 14 15 10"/>
                  </svg>
                  Free cancellation
                </span>
                <span class="plum-badge-match">{{ prop.match }}% match</span>
              </div>

              <div class="plum-card-price-action-row">
                <div class="plum-price-group">
                  <span class="plum-price-val">${{ prop.price }}</span>
                  <span class="plum-price-sub">/ month</span>
                </div>
                <button 
                  type="button" 
                  class="btn-plum-view-detail" 
                  @click.stop="navigateToDetail(prop.id)"
                >
                  View Detail
                </button>
              </div>
            </div>
          </article>
        </div>
      </section>

      <!-- RIGHT MAP COLUMN / FULLSCREEN MAP VIEWPORT -->
      <section class="map-viewport-section" :class="{ 'is-fullscreen-mode': isFullScreenMap }">
        
        <!-- Google Map Canvas -->
        <div ref="mapContainerRef" class="google-map-canvas"></div>

        <!-- Active "Pick Location on Map" Banner -->
        <transition name="toast-fade">
          <div v-if="isPickingLocationOnMap" class="map-pick-indicator-banner">
            <div class="pick-banner-content">
              <span class="pick-pulse-dot"></span>
              <span>Click anywhere on the map to place your starting point</span>
              <button type="button" class="btn-cancel-pick" @click="isPickingLocationOnMap = false">Cancel</button>
            </div>
          </div>
        </transition>

        <!-- High-Fidelity Interactive Vector Map Fallback (Active when Google Maps key is loading/offline) -->
        <div v-if="!isGoogleMapReady" class="interactive-fallback-canvas" @click="handleVectorCanvasClick">
          <div class="map-grid-overlay"></div>
          <div class="map-river-shape"></div>

          <!-- SVG Vector Route Connector connecting user location to target property -->
          <svg v-if="selectedProperty" class="vector-route-svg">
            <line 
              :x1="getVectorPercentCoords(userLocation).left" 
              :y1="getVectorPercentCoords(userLocation).top" 
              :x2="getVectorPercentCoords(selectedProperty).left" 
              :y2="getVectorPercentCoords(selectedProperty).top" 
              stroke="#2563EB" 
              stroke-width="3" 
              stroke-dasharray="6,6"
              stroke-linecap="round"
            />
          </svg>

          <!-- User Location Pin on Vector Canvas -->
          <div 
            class="vector-user-pin"
            :style="getVectorPinStyle(userLocation)"
            :title="userLocation.name + ' • Click to change or drag location'"
            @click.stop="showLocationPickerModal = true"
          >
            <div class="user-pulse-ring"></div>
            <div class="user-loc-pill">
              <span class="user-loc-dot" :class="{ 'is-locating': userLocation.isLocating }"></span>
              <span>{{ userLocation.isManual ? userLocation.name : 'Your Location' }}</span>
            </div>
            <div class="user-loc-pointer"></div>
          </div>
          
          <!-- Interactive Property Markers placed on the vector canvas -->
          <div 
            v-for="prop in filteredProperties" 
            :key="prop.id" 
            class="vector-map-pin"
            :class="{ active: selectedProperty && selectedProperty.id === prop.id }"
            :style="getVectorPinStyle(prop)"
            @click.stop="selectProperty(prop)"
          >
            <div class="pin-pill">${{ prop.price }}</div>
            <div class="pin-pointer"></div>
          </div>

          <div class="fallback-map-badge">
            <span class="live-pulse-dot"></span>
            <span>Phnom Penh Map Registry &bull; {{ filteredProperties.length }} Homes Available</span>
          </div>
        </div>

        <!-- ============================================== -->
        <!-- OVERLAYS SPECIFIC TO SPLIT-VIEW MODE           -->
        <!-- ============================================== -->
        <template v-if="!isFullScreenMap">
          <!-- Floating Expand to Fullscreen Pill Button (<) -->
          <button 
            type="button" 
            class="btn-split-toggle-expand" 
            title="Expand to Fullscreen Map"
            @click="toggleFullScreenMap"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <polyline points="15 18 9 12 15 6"/>
            </svg>
          </button>

          <!-- Floating Map Control Buttons at Top Center of Map -->
          <div class="split-map-top-bar">
            <!-- Manual Location Placer Button -->
            <button 
              type="button" 
              class="btn-set-loc-pill" 
              :class="{ 'is-manual': userLocation.isManual }"
              @click="showLocationPickerModal = true"
              title="Set or place starting point manually"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.4">
                <circle cx="12" cy="12" r="3"/>
                <path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
              </svg>
              <span>{{ userLocation.isManual ? userLocation.name : 'Set Location' }}</span>
            </button>

            <button type="button" class="btn-search-area-pill" @click="recenterMap">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/>
                <line x1="21" y1="21" x2="16.65" y2="16.65"/>
              </svg>
              <span>Search this area</span>
            </button>

            <button type="button" class="btn-fullscreen-toggle-pill" @click="toggleFullScreenMap">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
              </svg>
              <span>Fullscreen</span>
            </button>
          </div>
        </template>


        <!-- ============================================== -->
        <!-- OVERLAYS SPECIFIC TO FULLSCREEN IMMERSIVE MODE -->
        <!-- ============================================== -->
        <template v-else>
          <!-- 1. Collapsible Icon-First Navigation Bar (Top Left) -->
          <div class="fullscreen-nav-capsule" :class="{ 'is-expanded': isFullscreenNavExpanded }">
            <!-- Collapsed Single Icon Trigger -->
            <button 
              v-if="!isFullscreenNavExpanded"
              type="button" 
              class="btn-nav-icon-only" 
              title="Open Navigation Menu"
              @click.stop="isFullscreenNavExpanded = true"
            >
              <div class="nav-icon-badge">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 18 L16 18" />
                  <path d="M4 18 L4 12 L9 7 L16 14" />
                  <path d="M12 18 L12 4 L16 4 L16 18 Z" />
                  <path d="M12 14 L16 14" />
                </svg>
              </div>
            </button>

            <!-- Expanded Full Navigation Bar -->
            <div v-else class="nav-bar-expanded" @click.stop>
              <div class="expanded-brand" @click="$router.push('/home')">
                <div class="expanded-brand-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 18 L16 18" />
                    <path d="M4 18 L4 12 L9 7 L16 14" />
                    <path d="M12 18 L12 4 L16 4 L16 18 Z" />
                    <path d="M12 14 L16 14" />
                  </svg>
                </div>
                <span class="expanded-brand-text">HomeSweet</span>
              </div>

              <div class="expanded-divider"></div>

              <!-- Split View Switcher Button -->
              <button type="button" class="btn-expanded-action" @click="toggleFullScreenMap">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <line x1="12" y1="3" x2="12" y2="21"/>
                </svg>
                <span>Split View</span>
              </button>

              <div class="expanded-divider"></div>

              <!-- Quick Navigation Links -->
              <button type="button" class="btn-expanded-link" @click="$router.push('/home')">
                Home
              </button>
              <button type="button" class="btn-expanded-link" @click="$router.push('/verify-account')">
                Verify
              </button>

              <div class="expanded-divider"></div>

              <!-- User Profile Avatar -->
              <div class="expanded-user-profile" @click="$router.push('/home')">
                <img 
                  :src="userProfile.avatar || defaultAvatar" 
                  referrerpolicy="no-referrer" 
                  @error="setDefaultAvatar" 
                  alt="User" 
                  class="expanded-user-avatar"
                />
              </div>

              <!-- Close / Collapse Button -->
              <button 
                type="button" 
                class="btn-expanded-close" 
                title="Collapse Navigation"
                @click.stop="isFullscreenNavExpanded = false"
              >
                ✕
              </button>
            </div>
          </div>

          <!-- Floating Search Bar (Top Left) -->
          <div class="floating-search-bar">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="2.2" class="search-icon">
              <circle cx="11" cy="11" r="8" />
              <path d="M21 21l-4.35-4.35" />
            </svg>
            <input 
              ref="mapSearchInput" 
              v-model="searchQuery" 
              type="text" 
              placeholder="Search Phnom Penh..." 
              class="search-input" 
            />
            <button v-if="searchQuery" type="button" class="search-clear-btn" @click="searchQuery = ''">✕</button>
          </div>

          <!-- Floating Controls (Top Right): Location Placer, Filters, Share, Heart, Split View -->
          <div class="floating-top-actions">
            <button 
              type="button" 
              class="btn-floating-filter" 
              :class="{ 'loc-manual': userLocation.isManual }"
              title="Set or change starting location"
              @click="showLocationPickerModal = true"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2">
                <circle cx="12" cy="12" r="3"/>
                <path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
              </svg>
              <span>{{ userLocation.isManual ? userLocation.name : 'Location' }}</span>
            </button>

            <button 
              type="button" 
              class="btn-floating-filter" 
              :class="{ active: isFilterPopoverOpen }"
              @click="isFilterPopoverOpen = !isFilterPopoverOpen"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="4" y1="21" x2="4" y2="14"/>
                <line x1="4" y1="10" x2="4" y2="3"/>
                <line x1="12" y1="21" x2="12" y2="12"/>
                <line x1="12" y1="8" x2="12" y2="3"/>
                <line x1="20" y1="21" x2="20" y2="16"/>
                <line x1="20" y1="12" x2="20" y2="3"/>
                <line x1="1" y1="14" x2="7" y2="14"/>
                <line x1="9" y1="8" x2="15" y2="8"/>
                <line x1="17" y1="16" x2="23" y2="16"/>
              </svg>
              <span>Filters</span>
            </button>

            <button type="button" class="btn-floating-square" title="Share" @click="handleShare">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8"/>
                <polyline points="16 6 12 2 8 6"/>
                <line x1="12" y1="2" x2="12" y2="15"/>
              </svg>
            </button>

            <button 
              type="button" 
              class="btn-floating-square" 
              :class="{ 'favorited': selectedProperty && selectedProperty.liked }"
              title="Save Property" 
              @click="toggleLikeSelected"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" :fill="selectedProperty && selectedProperty.liked ? '#ef4444' : 'none'" :stroke="selectedProperty && selectedProperty.liked ? '#ef4444' : 'currentColor'" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
              </svg>
            </button>

            <button type="button" class="btn-floating-square" title="Exit to Split View" @click="toggleFullScreenMap">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <line x1="12" y1="3" x2="12" y2="21"/>
              </svg>
            </button>
          </div>

          <!-- Focus Shade Layer on Map (active when user is viewing a house) -->
          <transition name="fade-shade">
            <div 
              v-if="selectedProperty" 
              class="map-focus-shade" 
              title="Click map to exit focus mode"
              @click="dismissCards"
            ></div>
          </transition>

          <!-- Floating Commute / Travel-Time Card (Left) -->
          <transition name="panel-pop-left">
            <div v-if="selectedProperty" class="floating-commute-panel">
              <!-- Origin Box: User's Current Location -->
              <div 
                class="commute-origin-box" 
                @click="showLocationPickerModal = true" 
                title="Click to manually set, drag, or change starting point"
              >
                <div class="origin-icon-badge user-origin-badge">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5">
                    <circle cx="12" cy="12" r="3"/>
                    <path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
                  </svg>
                </div>
                <div class="origin-info-col">
                  <span class="origin-title">{{ userLocation.name }}</span>
                  <span class="origin-gps-tag" :class="{ 'active': userLocation.isDetected, 'locating': userLocation.isLocating, 'manual': userLocation.isManual }">
                    {{ userLocation.isLocating ? 'Locating...' : (userLocation.isManual ? 'Manual Pin' : (userLocation.isDetected ? 'GPS Active' : 'Default Pin')) }}
                  </span>
                </div>
                <div class="origin-edit-badge" title="Edit location">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                </div>
              </div>

              <div class="commute-down-pointer">
                <svg width="12" height="8" viewBox="0 0 12 8" fill="#554848">
                  <path d="M6 8 L0 0 L12 0 Z" />
                </svg>
              </div>

              <div class="commute-transit-modes">
                <div class="transit-mode-item" title="Walking Estimate">
                  <div class="mode-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#475569" stroke-width="2">
                      <circle cx="12" cy="4" r="2" />
                      <path d="M12 7v5l3 3M9 11l3-2 3 2M10 17l2 4 2-4" />
                    </svg>
                  </div>
                  <span class="mode-time">{{ calculatedCommute.walking }} min</span>
                </div>

                <div class="mode-separator"></div>

                <div class="transit-mode-item" title="Scooter / Moto Estimate">
                  <div class="mode-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#475569" stroke-width="2">
                      <circle cx="6" cy="17" r="3" />
                      <circle cx="18" cy="17" r="3" />
                      <path d="M6 14l5-5h4l3 5M12 9v5M9 5l3 2" />
                    </svg>
                  </div>
                  <span class="mode-time">{{ calculatedCommute.scooter }} min</span>
                </div>

                <div class="mode-separator"></div>

                <div class="transit-mode-item" title="Car / Taxi Estimate">
                  <div class="mode-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#475569" stroke-width="2">
                      <rect x="3" y="11" width="18" height="8" rx="2" />
                      <path d="M5 11l2-5h10l2 5M7 19v2M17 19v2" />
                      <circle cx="7" cy="15" r="1.5" />
                      <circle cx="17" cy="15" r="1.5" />
                    </svg>
                  </div>
                  <span class="mode-time">{{ calculatedCommute.car }} min</span>
                </div>

                <div class="mode-separator"></div>

                <div class="transit-mode-item" title="Public Transit Estimate">
                  <div class="mode-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#475569" stroke-width="2">
                      <rect x="4" y="4" width="16" height="14" rx="2" />
                      <path d="M4 11h16M8 18v3M16 18v3" />
                      <circle cx="8" cy="15" r="1" />
                      <circle cx="16" cy="15" r="1" />
                    </svg>
                  </div>
                  <span class="mode-time">{{ calculatedCommute.transit }} min</span>
                </div>
              </div>

              <div class="commute-down-pointer">
                <svg width="12" height="8" viewBox="0 0 12 8" fill="#554848">
                  <path d="M6 8 L0 0 L12 0 Z" />
                </svg>
              </div>

              <!-- Destination Box: Target Property -->
              <div class="commute-destination-card">
                <div class="destination-name">To {{ selectedProperty.name }}</div>
                <div class="destination-est-label">From your location</div>
                <div class="destination-est-time">
                  {{ calculatedCommute.distanceKm }} km &bull; {{ calculatedCommute.car }} min drive
                </div>
              </div>
            </div>
          </transition>

          <!-- Floating Property Preview Card (Right) -->
          <transition name="panel-pop-right">
            <div v-if="selectedProperty" class="floating-property-card">
              <!-- Image Carousel -->
              <div class="property-carousel-container">
                <img 
                  :src="currentPropertyImage" 
                  :alt="selectedProperty.name" 
                  class="carousel-main-image"
                />
                
                <button 
                  type="button" 
                  class="carousel-nav-btn prev" 
                  title="Previous image"
                  @click.stop="prevSlide"
                >
                  ‹
                </button>

                <button 
                  type="button" 
                  class="carousel-nav-btn next" 
                  title="Next image"
                  @click.stop="nextSlide"
                >
                  ›
                </button>

                <div class="carousel-dots-bar">
                  <span 
                    v-for="(_, idx) in selectedProperty.images" 
                    :key="idx" 
                    class="carousel-dot"
                    :class="{ active: activeSlideIndex === idx }"
                    @click.stop="activeSlideIndex = idx"
                  ></span>
                </div>
              </div>

              <!-- Property Information -->
              <div class="property-details-content">
                <div class="property-title-price-row">
                  <h3 class="property-name">{{ selectedProperty.name }}</h3>
                  <span class="property-price">${{ selectedProperty.price }}</span>
                </div>

                <div class="property-location-pin">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" />
                    <circle cx="12" cy="10" r="3" />
                  </svg>
                  <span>{{ selectedProperty.location }}</span>
                </div>

                <div class="property-specs-row">
                  <span class="spec-pill">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    </svg>
                    {{ selectedProperty.beds }}
                  </span>
                  <span class="spec-pill">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                      <circle cx="9" cy="7" r="4"/>
                    </svg>
                    {{ selectedProperty.baths * 2 }}
                  </span>
                  <span class="spec-pill">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <rect x="3" y="3" width="18" height="18" rx="2"/>
                    </svg>
                    {{ selectedProperty.sqft }}
                  </span>
                  <span class="match-score">{{ selectedProperty.match }}%</span>
                </div>

                <!-- Neighborhood Tags -->
                <div class="property-tags-row">
                  <span class="prop-tag tag-campus">Near Campus</span>
                  <span class="prop-tag tag-quiet">Quiet Area</span>
                  <span class="prop-tag tag-nightlife">Nightlife</span>
                  <span class="prop-tag tag-more">More</span>
                </div>

                <!-- "Around Your New Home" Amenities List -->
                <div class="around-home-block">
                  <h4 class="around-title">Around Your New Home</h4>
                  <ul class="around-list">
                    <li class="around-item">
                      <span class="around-emoji">🎓</span>
                      <span>Universities</span>
                    </li>
                    <li class="around-item">
                      <span class="around-emoji">☕</span>
                      <span>Cafes</span>
                    </li>
                    <li class="around-item">
                      <span class="around-emoji">🛒</span>
                      <span>Supermarkets</span>
                    </li>
                    <li class="around-item">
                      <span class="around-emoji">🏥</span>
                      <span>Hospitals</span>
                    </li>
                  </ul>
                </div>

                <!-- Action Buttons: Save & View Detail -->
                <div class="property-actions-row">
                  <button 
                    type="button" 
                    class="btn-save-action" 
                    :class="{ 'favorited': selectedProperty.liked }"
                    @click="toggleLikeSelected"
                  >
                    {{ selectedProperty.liked ? 'Saved' : 'Save' }}
                  </button>
                  <button 
                    type="button" 
                    class="btn-view-detail-action" 
                    @click="navigateToDetail(selectedProperty.id)"
                  >
                    View Detail
                  </button>
                </div>
              </div>
            </div>
          </transition>

          <!-- Floating Bottom Center Down Chevron Button -->
          <transition name="fade-shade">
            <div v-if="selectedProperty" class="floating-bottom-chevron-wrap">
              <button type="button" class="btn-bottom-chevron" title="Close Preview" @click="dismissCards">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#334155" stroke-width="2.5">
                  <polyline points="6 9 12 15 18 9"/>
                </svg>
              </button>
            </div>
          </transition>
        </template>

      </section>
    </main>
    <div v-if="isFilterPopoverOpen" class="filters-popover-card" @click.stop>
      <div class="popover-header">
        <h4 class="popover-title">Filter & Sort Properties</h4>
        <button type="button" class="popover-close" @click="isFilterPopoverOpen = false">✕</button>
      </div>

      <div class="popover-body">
        <div class="filter-group">
          <label class="filter-label">Price Range ($/month)</label>
          <div class="price-range-row">
            <input type="number" v-model.number="filterState.priceMin" placeholder="Min" class="filter-input-small" />
            <span>-</span>
            <input type="number" v-model.number="filterState.priceMax" placeholder="Max" class="filter-input-small" />
          </div>
        </div>

        <div class="filter-group">
          <label class="filter-label">Property Type</label>
          <select v-model="filterState.type" class="filter-select">
            <option value="Any type">Any type</option>
            <option value="condo">Condo</option>
            <option value="apartment">Apartment</option>
            <option value="house">House</option>
            <option value="studio">Studio</option>
          </select>
        </div>

        <div class="filter-group">
          <label class="filter-label">Lease Duration</label>
          <div class="segmented-chips">
            <button 
              type="button" 
              class="chip-btn" 
              :class="{ active: filterState.period === 'Any' }" 
              @click="filterState.period = 'Any'"
            >Any</button>
            <button 
              type="button" 
              class="chip-btn" 
              :class="{ active: filterState.period === 'Short-term' }" 
              @click="filterState.period = 'Short-term'"
            >Short-term</button>
            <button 
              type="button" 
              class="chip-btn" 
              :class="{ active: filterState.period === 'Long-term' }" 
              @click="filterState.period = 'Long-term'"
            >Long-term</button>
          </div>
        </div>
      </div>

      <div class="popover-footer">
        <button type="button" class="btn-clear-filter" @click="resetFilters">Reset</button>
        <button type="button" class="btn-apply-filter" @click="isFilterPopoverOpen = false">Apply</button>
      </div>
    </div>

    <!-- Manual Location Placer Modal -->
    <transition name="modal-fade">
      <div v-if="showLocationPickerModal" class="location-modal-overlay" @click.self="showLocationPickerModal = false">
        <div class="location-modal-card" @click.stop>
          <div class="loc-modal-header">
            <div class="loc-header-title-group">
              <div class="loc-icon-bubble">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2">
                  <circle cx="12" cy="12" r="3"/>
                  <path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
                </svg>
              </div>
              <div>
                <h3 class="loc-modal-title">Set Starting Location</h3>
                <p class="loc-modal-subtitle">Route calculations & travel times will measure from this point</p>
              </div>
            </div>
            <button type="button" class="loc-modal-close" @click="showLocationPickerModal = false">✕</button>
          </div>

          <div class="loc-modal-body">
            <!-- Current Location Status Card -->
            <div class="current-loc-status-card">
              <div class="loc-status-left">
                <span class="loc-indicator-dot" :class="{ 'manual': userLocation.isManual, 'gps': userLocation.isDetected && !userLocation.isManual }"></span>
                <div class="loc-name-col">
                  <span class="current-loc-name">{{ userLocation.name }}</span>
                  <span class="current-loc-coords">{{ userLocation.lat.toFixed(4) }}, {{ userLocation.lng.toFixed(4) }} &bull; {{ userLocation.isManual ? 'Manual Location' : (userLocation.isDetected ? 'Live GPS' : 'Default Location') }}</span>
                </div>
              </div>
            </div>

            <!-- Primary Action Buttons -->
            <div class="loc-action-buttons-grid">
              <button type="button" class="btn-loc-action primary" @click="startPickOnMap">
                <div class="action-icon">📍</div>
                <div class="action-text">
                  <span class="action-bold">Pick on Map</span>
                  <span class="action-hint">Click anywhere on the map to drop pin</span>
                </div>
              </button>

              <button type="button" class="btn-loc-action" @click="handleGpsDetect" :disabled="userLocation.isLocating">
                <div class="action-icon">🎯</div>
                <div class="action-text">
                  <span class="action-bold">{{ userLocation.isLocating ? 'Locating...' : 'Use Device GPS' }}</span>
                  <span class="action-hint">Query browser GPS coordinates</span>
                </div>
              </button>
            </div>

            <!-- Drag Tip Box -->
            <div class="loc-tip-box">
              <span class="tip-icon">💡</span>
              <span><strong>Drag & Drop:</strong> You can also grab and drag the blue location marker directly on the Google Map anytime!</span>
            </div>

            <!-- Phnom Penh Districts Presets -->
            <div class="loc-presets-section">
              <h4 class="presets-section-title">Or Choose Phnom Penh District</h4>
              <div class="presets-pills-grid">
                <button 
                  v-for="preset in PHNOM_PENH_DISTRICTS" 
                  :key="preset.name"
                  type="button" 
                  class="district-preset-pill"
                  :class="{ 'is-active': userLocation.name.includes(preset.name) }"
                  @click="selectDistrictPreset(preset)"
                >
                  <span class="preset-name">{{ preset.name }}</span>
                  <span v-if="userLocation.name.includes(preset.name)" class="preset-check">✓</span>
                </button>
              </div>
            </div>
          </div>

          <div class="loc-modal-footer">
            <button type="button" class="btn-loc-done" @click="showLocationPickerModal = false">Done</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Non-blocking toast -->
    <transition name="toast-fade">
      <div v-if="toast.visible" class="search-toast">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <span>{{ toast.message }}</span>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { properties, globalSearchQuery, globalFilterState } from '../../store.js'
import { auth, db } from '../../firebase'
import { doc, getDoc } from 'firebase/firestore'
import { onAuthStateChanged } from 'firebase/auth'
import { getCurrentCoordinates, reverseGeocodeCoordinates, getNearestDistrict, DISTRICT_CENTERS } from '../../services/locationService'

const router = useRouter()

const toast = reactive({ visible: false, message: '' })
function showToast(msg) {
  toast.message = msg
  toast.visible = true
  setTimeout(() => { toast.visible = false }, 2500)
}

// Mode Toggle: default split view (Plum Guide style) vs fullscreen map design
const isFullScreenMap = ref(false)

// Default avatar
const defaultAvatar = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23dfa37b'/><stop offset='100%' stop-color='%23c0784a'/></linearGradient></defs><circle cx='50' cy='50' r='50' fill='url(%23g)'/><circle cx='50' cy='37' r='17' fill='%23fff'/><path d='M50 58c-18 0-32 9-32 20v4h64v-4c0-11-14-20-32-20z' fill='%23fff'/></svg>"

function setDefaultAvatar(e) {
  e.target.src = defaultAvatar
}

// Global filter & search state
const searchQuery = globalSearchQuery
const filterState = globalFilterState

// Search capsule state
const selectedDatesLabel = ref('Any dates')
const guestsCount = ref(2)
const guestsLabel = computed(() => guestsCount.value ? `${guestsCount.value} guests` : 'Add guests')

function cycleDates() {
  const dates = ['Any dates', 'This weekend', 'Next month', 'Oct - Dec']
  const idx = dates.indexOf(selectedDatesLabel.value)
  selectedDatesLabel.value = dates[(idx + 1) % dates.length]
}

function cycleGuests() {
  guestsCount.value = guestsCount.value >= 6 ? 1 : guestsCount.value + 1
}

const isFilterPopoverOpen = ref(false)
const mapContainerRef = ref(null)
const mapSearchInput = ref(null)
const isGoogleMapReady = ref(false)

// Selected active property & UI state
const selectedProperty = ref(null)
const isFullscreenNavExpanded = ref(false)
const activeSlideIndex = ref(0)

// Manual Location Placer State
const isPickingLocationOnMap = ref(false)
const showLocationPickerModal = ref(false)
const PHNOM_PENH_DISTRICTS = DISTRICT_CENTERS

// User Location state (Origin for commute calculations and map routing)
const userLocation = ref({
  lat: 11.5621,
  lng: 104.9160,
  name: 'Your Location',
  address: 'Phnom Penh, Cambodia',
  isLocating: false,
  isDetected: false,
  isManual: false
})

const googleRouteData = ref({ distanceText: '', distanceKm: null, durationMin: null })

// User profile
const userProfile = ref({
  avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&q=80',
  firstName: 'Soth',
  verificationStatus: 'verified'
})

// Google Maps objects
let googleMap = null
let googleMarkers = []
let userLocationMarker = null
let routePolyline = null
let directionsService = null
let directionsRenderer = null

// Custom light grayscale map styling matching reference image
const customMapStyles = [
  { elementType: "geometry", stylers: [{ color: "#f5f5f5" }] },
  { elementType: "labels.icon", stylers: [{ visibility: "off" }] },
  { elementType: "labels.text.fill", stylers: [{ color: "#616161" }] },
  { elementType: "labels.text.stroke", stylers: [{ color: "#f5f5f5" }] },
  { featureType: "administrative.land_parcel", elementType: "labels.text.fill", stylers: [{ color: "#bdbdbd" }] },
  { featureType: "poi", elementType: "geometry", stylers: [{ color: "#eeeeee" }] },
  { featureType: "poi", elementType: "labels.text.fill", stylers: [{ color: "#757575" }] },
  { featureType: "poi.park", elementType: "geometry", stylers: [{ color: "#e5e5e5" }] },
  { featureType: "poi.park", elementType: "labels.text.fill", stylers: [{ color: "#9e9e9e" }] },
  { featureType: "road", elementType: "geometry", stylers: [{ color: "#ffffff" }] },
  { featureType: "road.arterial", elementType: "labels.text.fill", stylers: [{ color: "#757575" }] },
  { featureType: "road.highway", elementType: "geometry", stylers: [{ color: "#dadada" }] },
  { featureType: "road.highway", elementType: "labels.text.fill", stylers: [{ color: "#616161" }] },
  { featureType: "road.local", elementType: "labels.text.fill", stylers: [{ color: "#9e9e9e" }] },
  { featureType: "transit.line", elementType: "geometry", stylers: [{ color: "#e5e5e5" }] },
  { featureType: "transit.station", elementType: "geometry", stylers: [{ color: "#eeeeee" }] },
  { featureType: "water", elementType: "geometry", stylers: [{ color: "#c9c9c9" }] },
  { featureType: "water", elementType: "labels.text.fill", stylers: [{ color: "#9e9e9e" }] }
]

// Filtered properties
const filteredProperties = computed(() => {
  return properties.value.filter(p => {
    if (searchQuery.value) {
      const q = searchQuery.value.toLowerCase()
      const matchName = p.name.toLowerCase().includes(q)
      const matchLoc = p.location.toLowerCase().includes(q)
      if (!matchName && !matchLoc) return false
    }
    if (filterState.value.type !== 'Any type') {
      if (p.type !== filterState.value.type.toLowerCase()) return false
    }
    if (p.price < filterState.value.priceMin || p.price > filterState.value.priceMax) return false
    if (filterState.value.period !== 'Any' && p.period !== filterState.value.period) return false
    return true
  })
})

// Current image in carousel for active property
const currentPropertyImage = computed(() => {
  if (!selectedProperty.value) return ''
  const imgs = selectedProperty.value.images || []
  return imgs[activeSlideIndex.value] || imgs[0] || '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg'
})

// Commute travel time calculation (Origin: User Location -> Target: Selected Property)
const calculatedCommute = computed(() => {
  if (!selectedProperty.value) {
    return { walking: 18, scooter: 8, car: 6, transit: 12, distanceKm: '2.1' }
  }
  const p = selectedProperty.value
  const dLat = (Number(p.lat) || 11.5900) - userLocation.value.lat
  const dLng = (Number(p.lng) || 104.9300) - userLocation.value.lng
  const rawDist = Math.max(0.4, Math.sqrt(dLat * dLat + dLng * dLng) * 110)

  const distanceKm = googleRouteData.value.distanceKm != null 
    ? googleRouteData.value.distanceKm 
    : Math.round(rawDist * 10) / 10

  const carTime = googleRouteData.value.durationMin != null 
    ? googleRouteData.value.durationMin 
    : Math.max(3, Math.round(distanceKm * 2.8))

  return {
    distanceKm: typeof distanceKm === 'number' ? distanceKm.toFixed(1) : distanceKm,
    walking: Math.max(4, Math.round(distanceKm * 12)),
    scooter: Math.max(2, Math.round(distanceKm * 2.2)),
    car: carTime,
    transit: Math.max(5, Math.round(distanceKm * 3.5))
  }
})

onMounted(() => {
  // Check auth for avatar
  onAuthStateChanged(auth, async (user) => {
    if (user) {
      try {
        const uDoc = await getDoc(doc(db, "users", user.uid))
        if (uDoc.exists()) {
          const d = uDoc.data()
          if (d.avatar) userProfile.value.avatar = d.avatar
          if (d.firstName) userProfile.value.firstName = d.firstName
          if (d.verificationStatus) userProfile.value.verificationStatus = d.verificationStatus
        }
      } catch (e) {
        console.warn("Could not load user profile:", e)
      }
    }
  })

  // Global click outside to collapse navigation
  window.addEventListener('click', handleDocumentClick)

  // Load Google Maps API
  initGoogleMaps()

  // Detect user current location via GPS
  requestUserLocation(true)
})

onBeforeUnmount(() => {
  if (directionsRenderer) directionsRenderer.set('directions', null)
  if (routePolyline) routePolyline.setMap(null)
  window.removeEventListener('click', handleDocumentClick)
})

function dismissCards() {
  if (selectedProperty.value) {
    selectedProperty.value = null
    googleRouteData.value = { distanceText: '', distanceKm: null, durationMin: null }
    if (directionsRenderer) directionsRenderer.set('directions', null)
    if (routePolyline) {
      routePolyline.setMap(null)
      routePolyline = null
    }
    renderGoogleMarkers()
  }
  if (isFullscreenNavExpanded.value) {
    isFullscreenNavExpanded.value = false
  }
}

function handleDocumentClick(e) {
  if (isFullscreenNavExpanded.value) {
    const capsule = document.querySelector('.fullscreen-nav-capsule')
    if (capsule && !capsule.contains(e.target)) {
      isFullscreenNavExpanded.value = false
    }
  }
}

function toggleFullScreenMap() {
  isFullScreenMap.value = !isFullScreenMap.value
  isFullscreenNavExpanded.value = false
  nextTick(() => {
    if (window.google?.maps && googleMap) {
      window.google.maps.event.trigger(googleMap, 'resize')
      if (selectedProperty.value && selectedProperty.value.lat && selectedProperty.value.lng) {
        googleMap.panTo({ lat: selectedProperty.value.lat, lng: selectedProperty.value.lng })
      } else {
        googleMap.setCenter({ lat: 11.5750, lng: 104.9080 })
      }
    }
  })
}

function initGoogleMaps() {
  if (window.google && window.google.maps) {
    mountMap()
    return
  }

  const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY
  if (!apiKey) return

  window.initGoogleMapCallback = () => {
    mountMap()
  }

  // Prevent duplicate script tags
  if (document.querySelector('script[src*="maps.googleapis.com"]')) {
    return
  }

  const script = document.createElement('script')
  script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&libraries=places&callback=initGoogleMapCallback`
  script.async = true
  script.defer = true
  script.onerror = () => {
    console.warn("Notice: Google Maps API unavailable, vector map fallback remains active.")
    isGoogleMapReady.value = false
  }
  document.head.appendChild(script)
}

function mountMap() {
  if (!mapContainerRef.value || !window.google?.maps) return

  try {
    const center = { lat: 11.5750, lng: 104.9080 }
    googleMap = new window.google.maps.Map(mapContainerRef.value, {
      center,
      zoom: 13,
      disableDefaultUI: true,
      zoomControl: true,
      styles: customMapStyles
    })

    directionsService = new window.google.maps.DirectionsService()
    directionsRenderer = new window.google.maps.DirectionsRenderer({
      suppressMarkers: true,
      polylineOptions: {
        strokeColor: '#5C4E4E',
        strokeOpacity: 0.85,
        strokeWeight: 4
      },
      map: googleMap
    })

    isGoogleMapReady.value = true
    renderGoogleMarkers()

    // Dismiss cards or place manual location on map click
    googleMap.addListener('click', (e) => {
      if (isPickingLocationOnMap.value && e.latLng) {
        setManualLocation(e.latLng.lat(), e.latLng.lng())
        isPickingLocationOnMap.value = false
        showToast("✓ Starting location pin placed on map")
        return
      }
      dismissCards()
    })
    googleMap.addListener('dragstart', () => {
      dismissCards()
    })

    // Places autocomplete if input exists
    if (mapSearchInput.value && window.google.maps.places) {
      const autocomplete = new window.google.maps.places.Autocomplete(mapSearchInput.value)
      autocomplete.bindTo('bounds', googleMap)
      autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace()
        if (place.geometry && place.geometry.location) {
          googleMap.setCenter(place.geometry.location)
          googleMap.setZoom(15)
        }
      })
    }
  } catch (err) {
    console.warn("Google Maps init notice:", err)
  }
}

function renderGoogleMarkers() {
  if (!googleMap || !window.google?.maps) return

  // Clear existing
  googleMarkers.forEach(m => m.setMap(null))
  googleMarkers = []

  // Create markers for properties
  filteredProperties.value.forEach(prop => {
    if (!prop.lat || !prop.lng) return
    const isSelected = selectedProperty.value && selectedProperty.value.id === prop.id

    const marker = new window.google.maps.Marker({
      position: { lat: prop.lat, lng: prop.lng },
      map: googleMap,
      title: prop.name,
      icon: getMarkerIcon(isSelected),
      zIndex: isSelected ? 100 : 10
    })

    marker.addListener('click', (e) => {
      if (e && e.stop) e.stop()
      selectProperty(prop)
    })

    googleMarkers.push(marker)
  })

  // User Location Marker - origin on the map (draggable)
  const userPos = { lat: userLocation.value.lat, lng: userLocation.value.lng }
  if (userLocationMarker) {
    userLocationMarker.setPosition(userPos)
    userLocationMarker.setTitle(`${userLocation.value.name} (Drag to move or click to change)`)
    userLocationMarker.setMap(googleMap)
  } else {
    userLocationMarker = new window.google.maps.Marker({
      position: userPos,
      map: googleMap,
      title: `${userLocation.value.name} (Drag to move or click to change)`,
      icon: getUserLocationMarkerIcon(),
      draggable: true,
      zIndex: 95
    })
    userLocationMarker.addListener('dragend', (e) => {
      if (e.latLng) {
        setManualLocation(e.latLng.lat(), e.latLng.lng())
        showToast("✓ Location marker dragged to new position")
      }
    })
    userLocationMarker.addListener('click', () => {
      showLocationPickerModal.value = true
    })
  }

  // Draw real route if property selected
  if (selectedProperty.value) {
    drawRouteLine()
  } else {
    if (directionsRenderer) directionsRenderer.set('directions', null)
    if (routePolyline) {
      routePolyline.setMap(null)
      routePolyline = null
    }
  }
}

function drawRouteLine() {
  if (!googleMap || !window.google?.maps || !selectedProperty.value) return
  if (routePolyline) {
    routePolyline.setMap(null)
    routePolyline = null
  }

  // Origin is User Location
  const origin = { 
    lat: Number(userLocation.value.lat), 
    lng: Number(userLocation.value.lng) 
  }
  // Destination is Target Property
  const destination = { 
    lat: Number(selectedProperty.value.lat) || 11.5900, 
    lng: Number(selectedProperty.value.lng) || 104.9300 
  }

  if (directionsService && directionsRenderer) {
    directionsService.route({
      origin,
      destination,
      travelMode: window.google.maps.TravelMode.DRIVING
    }, (result, status) => {
      if (status === 'OK' && result) {
        directionsRenderer.setDirections(result)
        const leg = result.routes?.[0]?.legs?.[0]
        if (leg) {
          googleRouteData.value = {
            distanceText: leg.distance?.text || '',
            distanceKm: (leg.distance?.value || 0) / 1000,
            durationMin: Math.round((leg.duration?.value || 0) / 60)
          }
        }
      } else {
        // Fallback to direct geodesic polyline
        drawDirectRouteLine(origin, destination)
      }
    })
  } else {
    drawDirectRouteLine(origin, destination)
  }
}

function drawDirectRouteLine(origin, destination) {
  if (directionsRenderer) directionsRenderer.set('directions', null)
  if (routePolyline) routePolyline.setMap(null)
  routePolyline = new window.google.maps.Polyline({
    path: [origin, destination],
    geodesic: true,
    strokeColor: '#5C4E4E',
    strokeOpacity: 0.85,
    strokeWeight: 4,
    map: googleMap
  })
}

function getMarkerIcon(isSelected) {
  if (isSelected) {
    const svg = `
      <svg width="56" height="56" viewBox="0 0 56 56" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#d99b45" flood-opacity="0.5"/>
          </filter>
        </defs>
        <circle cx="28" cy="28" r="24" fill="#d99b45" filter="url(#glow)"/>
        <path d="M28 17 L17 26 L20 26 L20 38 L36 38 L36 26 L39 26 Z M26 38 L26 30 L30 30 L30 38 Z" fill="#ffffff"/>
      </svg>
    `;
    return {
      url: `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`,
      scaledSize: new window.google.maps.Size(56, 56),
      anchor: new window.google.maps.Point(28, 28)
    }
  } else {
    const svg = `
      <svg width="44" height="44" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="sh" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.18"/>
          </filter>
        </defs>
        <circle cx="22" cy="22" r="18" fill="#ffffff" filter="url(#sh)"/>
        <path d="M22 14 L14 21 L16 21 L16 30 L28 30 L28 21 L30 21 Z M20 30 L20 25 L24 25 L24 30 Z" fill="#4a4040"/>
      </svg>
    `;
    return {
      url: `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`,
      scaledSize: new window.google.maps.Size(44, 44),
      anchor: new window.google.maps.Point(22, 22)
    }
  }
}

function getUserLocationMarkerIcon() {
  const svg = `
    <svg width="48" height="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="uGlow" x="-30%" y="-30%" width="160%" height="160%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#2563eb" flood-opacity="0.35"/>
        </filter>
      </defs>
      <!-- Outer ripple halo -->
      <circle cx="24" cy="24" r="20" fill="rgba(37, 99, 235, 0.18)" />
      <!-- Middle ring -->
      <circle cx="24" cy="24" r="14" fill="#ffffff" filter="url(#uGlow)" stroke="#2563eb" stroke-width="2.5"/>
      <!-- Inner user blue center -->
      <circle cx="24" cy="24" r="7" fill="#2563eb"/>
      <!-- Small white core -->
      <circle cx="24" cy="24" r="2.5" fill="#ffffff"/>
    </svg>
  `;
  return {
    url: `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`,
    scaledSize: new window.google.maps.Size(48, 48),
    anchor: new window.google.maps.Point(24, 24)
  }
}

function selectProperty(prop) {
  selectedProperty.value = prop
  activeSlideIndex.value = 0
  if (isGoogleMapReady.value) {
    renderGoogleMarkers()
    if (googleMap && prop.lat && prop.lng) {
      googleMap.panTo({ lat: prop.lat, lng: prop.lng })
    }
  }
}

function getVectorPinStyle(prop) {
  if (!prop.lat || !prop.lng) return { top: '50%', left: '50%' }
  const minLat = 11.5300
  const maxLat = 11.6050
  const minLng = 104.8700
  const maxLng = 104.9450
  
  const normY = Math.min(Math.max((maxLat - prop.lat) / (maxLat - minLat), 0), 1)
  const normX = Math.min(Math.max((prop.lng - minLng) / (maxLng - minLng), 0), 1)
  
  const topPercent = 12 + normY * 74
  const leftPercent = 12 + normX * 74
  
  return {
    top: `${topPercent}%`,
    left: `${leftPercent}%`
  }
}

function getVectorPercentCoords(target) {
  if (!target || !target.lat || !target.lng) return { top: '50%', left: '50%' }
  const minLat = 11.5300
  const maxLat = 11.6050
  const minLng = 104.8700
  const maxLng = 104.9450
  
  const normY = Math.min(Math.max((maxLat - target.lat) / (maxLat - minLat), 0), 1)
  const normX = Math.min(Math.max((target.lng - minLng) / (maxLng - minLng), 0), 1)
  
  return {
    top: `${12 + normY * 74}%`,
    left: `${12 + normX * 74}%`
  }
}

function nextSlide() {
  if (!selectedProperty.value) return
  const total = selectedProperty.value.images?.length || 1
  activeSlideIndex.value = (activeSlideIndex.value + 1) % total
}

function prevSlide() {
  if (!selectedProperty.value) return
  const total = selectedProperty.value.images?.length || 1
  activeSlideIndex.value = (activeSlideIndex.value - 1 + total) % total
}

function toggleLikeSelected() {
  if (selectedProperty.value) {
    selectedProperty.value.liked = !selectedProperty.value.liked
  }
}

function navigateToDetail(propId) {
  const id = propId || selectedProperty.value?.id
  if (id) {
    router.push(`/property/${id}`)
  }
}

function recenterMap() {
  if (googleMap) {
    if (userLocation.value.isDetected && userLocation.value.lat) {
      googleMap.setCenter({ lat: userLocation.value.lat, lng: userLocation.value.lng })
    } else {
      googleMap.setCenter({ lat: 11.5750, lng: 104.9080 })
    }
    googleMap.setZoom(13)
  }
}

function handleShare() {
  if (navigator.share) {
    navigator.share({
      title: selectedProperty.value?.name || 'HomeSweet Property',
      url: window.location.href
    }).catch(() => {})
  } else {
    navigator.clipboard?.writeText(window.location.href)
    showToast("Property link copied to clipboard!")
  }
}

async function requestUserLocation(silent = false) {
  userLocation.value.isLocating = true
  if (!silent) showToast("Detecting your location via GPS...")
  try {
    const coords = await getCurrentCoordinates({ enableHighAccuracy: true, timeout: 8000 })
    userLocation.value.lat = coords.lat
    userLocation.value.lng = coords.lng
    userLocation.value.isDetected = true
    userLocation.value.name = 'Your Location'

    try {
      const geoResult = await reverseGeocodeCoordinates(coords.lat, coords.lng)
      if (geoResult?.formattedAddress) {
        userLocation.value.address = geoResult.formattedAddress
      }
    } catch {
      // Keep default
    }

    if (!silent) showToast("✓ Location updated to your GPS coordinates")

    if (isGoogleMapReady.value) {
      renderGoogleMarkers()
      if (selectedProperty.value) {
        drawRouteLine()
      }
    }
  } catch (err) {
    console.warn("GPS location notice:", err)
    if (!silent) {
      showToast(err.message || "Could not retrieve GPS location. Using Phnom Penh center.")
    }
  } finally {
    userLocation.value.isLocating = false
  }
}

function handleGpsDetect() {
  showLocationPickerModal.value = false
  userLocation.value.isManual = false
  requestUserLocation(false)
}

function setManualLocation(lat, lng, customName = null) {
  userLocation.value.lat = lat
  userLocation.value.lng = lng
  userLocation.value.isManual = true
  userLocation.value.isDetected = true
  
  if (customName) {
    userLocation.value.name = customName
  } else {
    try {
      const nearest = getNearestDistrict(lat, lng)
      userLocation.value.name = nearest ? `${nearest}` : 'Custom Location'
    } catch {
      userLocation.value.name = 'Custom Location'
    }
  }

  // Also try reverse geocoding asynchronously to enrich address
  reverseGeocodeCoordinates(lat, lng).then(res => {
    if (res?.formattedAddress) {
      userLocation.value.address = res.formattedAddress
    }
  }).catch(() => {})

  if (isGoogleMapReady.value) {
    renderGoogleMarkers()
    if (selectedProperty.value) {
      drawRouteLine()
    }
  }
}

function selectDistrictPreset(preset) {
  setManualLocation(preset.lat, preset.lng, preset.name)
  showLocationPickerModal.value = false
  showToast(`✓ Starting point set to ${preset.name}`)
}

function startPickOnMap() {
  showLocationPickerModal.value = false
  isPickingLocationOnMap.value = true
  showToast("📍 Click anywhere on the map to place your starting pin")
}

function handleVectorCanvasClick(e) {
  if (isPickingLocationOnMap.value) {
    const rect = e.currentTarget.getBoundingClientRect()
    const clickX = (e.clientX - rect.left) / rect.width
    const clickY = (e.clientY - rect.top) / rect.height
    
    const minLat = 11.5300
    const maxLat = 11.6050
    const minLng = 104.8700
    const maxLng = 104.9450
    
    const normX = Math.min(Math.max((clickX - 0.12) / 0.74, 0), 1)
    const normY = Math.min(Math.max((clickY - 0.12) / 0.74, 0), 1)
    
    const lat = maxLat - normY * (maxLat - minLat)
    const lng = minLng + normX * (maxLng - minLng)
    
    setManualLocation(lat, lng)
    isPickingLocationOnMap.value = false
    showToast("✓ Starting location pin placed")
    return
  }
  dismissCards()
}

function resetFilters() {
  filterState.value.priceMin = 50
  filterState.value.priceMax = 610
  filterState.value.type = 'Any type'
  filterState.value.period = 'Any'
}

watch(filteredProperties, () => {
  if (isGoogleMapReady.value) {
    renderGoogleMarkers()
  }
})
</script>

<style scoped>
/* ======================================================== */
/* BASE LAYOUT & WRAPPER                                    */
/* ======================================================== */
.search-experience-wrapper {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: #fafaf9;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: #1e293b;
}

/* ======================================================== */
/* 1. PLUM GUIDE LUXURY HEADER (DEFAULT SPLIT VIEW)        */
/* ======================================================== */
.plum-nav-header {
  height: 76px;
  background: #ffffff;
  border-bottom: 1px solid #edebe8;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 40;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.plum-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.plum-brand-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #f4f3f0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.plum-brand-text {
  font-size: 1.25rem;
  font-weight: 800;
  color: #1f1b1a;
  letter-spacing: -0.5px;
}

/* Search Capsule */
.plum-search-capsule {
  display: flex;
  align-items: center;
  background: #ffffff;
  border: 1px solid #dcd8d3;
  border-radius: 40px;
  padding: 6px 8px 6px 20px;
  box-shadow: 0 3px 12px rgba(0,0,0,0.06);
  transition: all 0.2s ease;
}

.plum-search-capsule:hover {
  box-shadow: 0 6px 18px rgba(0,0,0,0.1);
  border-color: #b8b2a9;
}

.capsule-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2px 14px;
  cursor: pointer;
}

.destination-col {
  min-width: 140px;
}

.capsule-label {
  font-size: 0.72rem;
  font-weight: 700;
  color: #1e1b18;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.capsule-input {
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.88rem;
  color: #2e2b27;
  font-weight: 500;
  padding: 0;
  margin: 0;
}

.capsule-input::placeholder {
  color: #8c857b;
}

.capsule-value {
  font-size: 0.88rem;
  color: #59534c;
  font-weight: 500;
}

.capsule-divider {
  width: 1px;
  height: 28px;
  background: #ede9e3;
}

.capsule-search-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #d99b45;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-left: 6px;
  transition: transform 0.15s ease, background 0.2s ease;
}

.capsule-search-btn:hover {
  background: #c58632;
  transform: scale(1.05);
}

/* Header Right */
.plum-header-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.btn-plum-filter {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1px solid #dcd8d3;
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 0.86rem;
  font-weight: 600;
  color: #2b2723;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-plum-filter:hover, .btn-plum-filter.active {
  background: #f7f5f2;
  border-color: #2b2723;
}

.plum-nav-link {
  font-size: 0.88rem;
  font-weight: 600;
  color: #3b3530;
  cursor: pointer;
  transition: color 0.15s ease;
}

.plum-nav-link:hover {
  color: #000000;
}

.plum-lang-currency {
  font-size: 0.86rem;
  font-weight: 600;
  color: #4b4540;
}

.plum-user-avatar-wrap {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid #e5e2dc;
  cursor: pointer;
}

.plum-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ======================================================== */
/* 2. FULLSCREEN COLLAPSIBLE ICON-FIRST NAVIGATION BAR      */
/* ======================================================== */
.fullscreen-nav-capsule {
  position: absolute;
  top: 24px;
  left: 24px;
  z-index: 40;
  display: flex;
  align-items: center;
  user-select: none;
}

/* Collapsed single icon trigger button */
.btn-nav-icon-only {
  width: 46px;
  height: 46px;
  background: #554848;
  border-radius: 50%;
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25), 0 2px 6px rgba(0, 0, 0, 0.15);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  padding: 0;
}

.btn-nav-icon-only:hover {
  transform: scale(1.08);
  background: #655656;
  box-shadow: 0 6px 22px rgba(0, 0, 0, 0.32);
}

.nav-icon-badge {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Expanded Navigation Bar */
.nav-bar-expanded {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #554848;
  padding: 6px 14px 6px 12px;
  border-radius: 30px;
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  animation: navExpandAnim 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes navExpandAnim {
  from {
    opacity: 0;
    transform: scale(0.85) translateX(-15px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateX(0);
  }
}

.expanded-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.expanded-brand-icon {
  width: 30px;
  height: 30px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.expanded-brand-text {
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: -0.3px;
}

.expanded-divider {
  width: 1px;
  height: 20px;
  background: rgba(255, 255, 255, 0.2);
}

.btn-expanded-action {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #ffffff;
  padding: 6px 12px;
  border-radius: 16px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-expanded-action:hover {
  background: rgba(255, 255, 255, 0.25);
}

.btn-expanded-link {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.85);
  font-size: 0.82rem;
  font-weight: 600;
  padding: 4px 8px;
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.btn-expanded-link:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.12);
}

.expanded-user-profile {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  overflow: hidden;
  border: 1.5px solid rgba(255, 255, 255, 0.4);
  cursor: pointer;
}

.expanded-user-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.btn-expanded-close {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  font-size: 0.8rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.btn-expanded-close:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* ======================================================== */
/* 3. MAIN SPLIT / FULLSCREEN WORKSPACE                     */
/* ======================================================== */
.search-main-workspace {
  position: relative;
  flex: 1;
  display: flex;
  width: 100%;
  height: calc(100vh - 76px);
  overflow: hidden;
}

.search-main-workspace.is-fullscreen-layout {
  height: 100vh;
}

/* ======================================================== */
/* 3A. LEFT LISTINGS COLUMN (PLUM GUIDE HORIZONTAL CARDS)   */
/* ======================================================== */
.plum-listings-column {
  width: 54%;
  height: 100%;
  overflow-y: auto;
  padding: 24px 32px;
  background: #ffffff;
  border-right: 1px solid #e9e6e2;
  box-sizing: border-box;
}

.listings-summary-header {
  margin-bottom: 24px;
}

.listings-count-title {
  font-size: 1.45rem;
  font-weight: 800;
  color: #1e1b18;
  margin: 0 0 6px 0;
  letter-spacing: -0.4px;
}

.listings-subtitle {
  font-size: 0.92rem;
  color: #645e57;
  margin: 0;
}

.standards-link {
  color: #c58632;
  font-weight: 600;
  text-decoration: underline;
  margin-left: 4px;
}

.plum-cards-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Horizontal Card */
.plum-property-card {
  display: flex;
  background: #ffffff;
  border: 1px solid #ede9e3;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.plum-property-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  border-color: #dcd6cd;
}

.plum-property-card.card-active-selected {
  border-color: #d99b45;
  box-shadow: 0 4px 20px rgba(217, 155, 69, 0.2);
}

/* Media Box */
.plum-card-media-box {
  position: relative;
  width: 42%;
  min-width: 220px;
  height: 190px;
  overflow: hidden;
  background: #f1efe9;
}

.plum-card-cover-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.plum-property-card:hover .plum-card-cover-img {
  transform: scale(1.03);
}

.plum-heart-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(0,0,0,0.25);
  backdrop-filter: blur(4px);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.15s ease;
}

.plum-heart-btn:hover {
  transform: scale(1.1);
}

.plum-media-dots {
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 5px;
}

.plum-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.6);
  transition: all 0.2s ease;
}

.plum-dot.active {
  background: #ffffff;
  width: 14px;
  border-radius: 4px;
}

/* Details Box */
.plum-card-details-box {
  flex: 1;
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.plum-card-top-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.plum-property-name {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1c1917;
  margin: 0;
  letter-spacing: -0.3px;
}

.plum-property-rating {
  font-size: 0.84rem;
  font-weight: 700;
  color: #d97706;
}

.plum-property-location {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.84rem;
  color: #64748b;
  margin-top: 4px;
}

.plum-property-specs {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  font-size: 0.82rem;
  color: #57534e;
  margin-top: 8px;
}

.spec-dot {
  color: #a8a29e;
}

.plum-features-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.plum-badge-free-cancel {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: #f5f5f4;
  border: 1px solid #e7e5e4;
  padding: 3px 9px;
  border-radius: 6px;
  font-size: 0.74rem;
  font-weight: 600;
  color: #44403c;
}

.plum-badge-match {
  background: #f0fdf4;
  color: #166534;
  font-size: 0.74rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
}

.plum-card-price-action-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px solid #f5f4f0;
}

.plum-price-group {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.plum-price-val {
  font-size: 1.28rem;
  font-weight: 800;
  color: #1c1917;
}

.plum-price-sub {
  font-size: 0.82rem;
  color: #78716c;
}

.btn-plum-view-detail {
  background: #554848;
  color: #ffffff;
  border: none;
  padding: 7px 16px;
  border-radius: 8px;
  font-size: 0.84rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s ease;
}

.btn-plum-view-detail:hover {
  background: #3f3636;
}


/* ======================================================== */
/* 3B. RIGHT MAP COLUMN / FULLSCREEN VIEWPORT               */
/* ======================================================== */
.map-viewport-section {
  position: relative;
  width: 46%;
  height: 100%;
  overflow: hidden;
  background: #f5f5f5;
  transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.map-viewport-section.is-fullscreen-mode {
  width: 100%;
}

.google-map-canvas {
  width: 100%;
  height: 100%;
}

/* Boundary Expand/Collapse Button (<) */
.btn-split-toggle-expand {
  position: absolute;
  top: 50%;
  left: 12px;
  transform: translateY(-50%);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #ffffff;
  border: 1px solid #dcd8d3;
  box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2b2723;
  cursor: pointer;
  z-index: 25;
  transition: all 0.2s ease;
}

.btn-split-toggle-expand:hover {
  background: #fcfbfa;
  transform: translateY(-50%) scale(1.08);
  box-shadow: 0 6px 20px rgba(0,0,0,0.18);
}

/* Split Top Floating Controls */
.split-map-top-bar {
  position: absolute;
  top: 16px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 12px;
  z-index: 20;
  pointer-events: none;
}

.btn-search-area-pill, .btn-fullscreen-toggle-pill {
  pointer-events: auto;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1px solid #dcd8d3;
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #1e1b18;
  box-shadow: 0 4px 14px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-search-area-pill:hover, .btn-fullscreen-toggle-pill:hover {
  background: #f7f5f2;
  box-shadow: 0 6px 18px rgba(0,0,0,0.16);
}


/* ======================================================== */
/* 3C. FULLSCREEN IMMERSIVE OVERLAYS                        */
/* ======================================================== */
/* Top-Left Search Bar (Positioned next to the nav icon) */
.floating-search-bar {
  position: absolute;
  top: 24px;
  left: 82px;
  z-index: 30;
  display: flex;
  align-items: center;
  background: #ffffff;
  border-radius: 40px;
  padding: 10px 20px;
  width: 300px;
  box-shadow: 0 6px 24px rgba(0,0,0,0.12);
  transition: all 0.3s ease;
}

.search-icon {
  margin-right: 12px;
  flex-shrink: 0;
}

.search-input {
  border: none;
  outline: none;
  font-size: 0.95rem;
  width: 100%;
  color: #1e293b;
  font-weight: 500;
  background: transparent;
}

.search-clear-btn {
  background: none;
  border: none;
  font-size: 0.85rem;
  color: #94a3b8;
  cursor: pointer;
  padding: 2px 6px;
}

/* Top-Right Controls */
.floating-top-actions {
  position: absolute;
  top: 24px;
  right: 24px;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: 12px;
}

/* Map Focus Shade Overlay (dimmed spotlight focusing on cards) */
.map-focus-shade {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 50%, rgba(20, 24, 33, 0.32) 0%, rgba(15, 23, 42, 0.60) 100%);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  z-index: 10;
  cursor: pointer;
  pointer-events: auto;
}

/* Card Pop-Up & Dismissal Transitions */
.panel-pop-left-enter-active,
.panel-pop-left-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
}
.panel-pop-left-enter-from,
.panel-pop-left-leave-to {
  transform: translateX(-140%);
  opacity: 0;
}

.panel-pop-right-enter-active,
.panel-pop-right-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
}
.panel-pop-right-enter-from,
.panel-pop-right-leave-to {
  transform: translateX(140%);
  opacity: 0;
}

.fade-shade-enter-active,
.fade-shade-leave-active {
  transition: opacity 0.35s ease, backdrop-filter 0.35s ease;
}
.fade-shade-enter-from,
.fade-shade-leave-to {
  opacity: 0;
  backdrop-filter: blur(0px);
}

.btn-floating-filter {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 28px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-floating-filter:hover {
  background: #f8fafc;
}

.btn-floating-square {
  width: 44px;
  height: 44px;
  background: #ffffff;
  border: none;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1e293b;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-floating-square:hover {
  background: #f8fafc;
}

.btn-floating-square.favorited {
  color: #ef4444;
}

/* Left Commute Card */
.floating-commute-panel {
  position: absolute;
  top: 90px;
  left: 24px;
  z-index: 25;
  width: 210px;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.12);
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.commute-origin-box {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  cursor: pointer;
  padding: 4px;
  border-radius: 12px;
  transition: background 0.18s ease;
}

.commute-origin-box:hover {
  background: #f8fafc;
}

.origin-icon-badge {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #554848;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.origin-icon-badge.user-origin-badge {
  background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.32);
}

.origin-info-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
  overflow: hidden;
}

.origin-title {
  font-size: 0.94rem;
  font-weight: 700;
  color: #1e293b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.origin-gps-tag {
  font-size: 0.68rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.origin-gps-tag.active {
  color: #10B981;
}

.origin-gps-tag.locating {
  color: #3B82F6;
  animation: pulse 1s infinite;
}

.commute-down-pointer {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 6px 0;
}

.commute-transit-modes {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.transit-mode-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 10px;
}

.mode-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #475569;
}

.mode-time {
  font-size: 0.88rem;
  font-weight: 600;
  color: #1e293b;
}

.mode-separator {
  width: 100%;
  height: 1px;
  background: #e2e8f0;
  margin: 2px 0;
}

.commute-destination-card {
  width: 100%;
  background: #554848;
  border-radius: 12px;
  padding: 12px 14px;
  box-sizing: border-box;
  color: #ffffff;
  cursor: pointer;
  transition: background 0.2s ease;
  margin-top: 4px;
}

.commute-destination-card:hover {
  background: #463b3b;
}

.destination-name {
  font-size: 0.84rem;
  font-weight: 700;
  margin-bottom: 6px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.destination-est-label {
  font-size: 0.68rem;
  color: #cbd5e1;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.destination-est-time {
  font-size: 0.82rem;
  font-weight: 600;
  margin-top: 2px;
}

/* Right Property Preview Card */
.floating-property-card {
  position: absolute;
  top: 90px;
  right: 24px;
  z-index: 25;
  width: 360px;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 16px 40px rgba(0,0,0,0.18);
  overflow: hidden;
}

.property-carousel-container {
  position: relative;
  width: 100%;
  height: 200px;
  background: #1e293b;
}

.carousel-main-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 5;
  transition: all 0.2s ease;
}

.carousel-nav-btn.prev { left: 10px; }
.carousel-nav-btn.next { right: 10px; }

.carousel-dots-bar {
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  z-index: 5;
}

.carousel-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
}

.carousel-dot.active {
  background: #ffffff;
  width: 16px;
  border-radius: 4px;
}

.property-details-content {
  padding: 16px 20px;
}

.property-title-price-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}

.property-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.property-price {
  font-size: 1.35rem;
  font-weight: 800;
  color: #111827;
}

.property-location-pin {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.82rem;
  color: #64748b;
  margin-bottom: 12px;
}

.property-specs-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 14px;
}

.spec-pill {
  display: flex;
  align-items: center;
  gap: 5px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 0.78rem;
  font-weight: 600;
  color: #475569;
}

.match-score {
  margin-left: auto;
  font-size: 0.82rem;
  font-weight: 700;
  color: #10b981;
}

.property-tags-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 16px;
}

.prop-tag {
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.74rem;
  font-weight: 600;
}

.tag-campus { background: #ecfdf5; color: #059669; }
.tag-quiet { background: #fffbeb; color: #d97706; }
.tag-nightlife { background: #eff6ff; color: #2563eb; }
.tag-more { background: #f1f5f9; color: #64748b; }

.around-home-block {
  border-top: 1px solid #f1f5f9;
  padding-top: 12px;
  margin-bottom: 16px;
}

.around-title {
  font-size: 0.82rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 8px 0;
}

.around-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
}

.around-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  color: #475569;
}

.around-emoji {
  font-size: 0.88rem;
}

.property-action-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-save-action {
  flex: 1;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
  background: #ffffff;
  font-size: 0.9rem;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-save-action:hover {
  background: #f8fafc;
}

.btn-save-action.saved {
  background: #fee2e2;
  border-color: #fca5a5;
  color: #b91c1c;
}

.btn-view-detail-action {
  flex: 1.6;
  padding: 10px;
  border-radius: 10px;
  border: none;
  background: #554848;
  color: #ffffff;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;
}

.btn-view-detail-action:hover {
  background: #3f3636;
}

/* Floating Bottom Chevron */
.floating-bottom-chevron-wrap {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 25;
}

.btn-bottom-chevron {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #ffffff;
  border: none;
  box-shadow: 0 6px 20px rgba(0,0,0,0.14);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.btn-bottom-chevron:hover {
  transform: scale(1.08);
}

/* ======================================================== */
/* 4. FILTERS POPOVER MODAL                                 */
/* ======================================================== */
.filters-popover-card {
  box-sizing: border-box;
  position: absolute;
  top: 86px;
  right: 32px;
  z-index: 50;
  width: 320px;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  padding: 20px;
  border: 1px solid #e2e8f0;
}

.popover-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.popover-title {
  font-size: 1rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.popover-close {
  background: none;
  border: none;
  font-size: 1rem;
  color: #64748b;
  cursor: pointer;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.filter-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: #475569;
}

.price-range-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-input-small {
  flex: 1;
  min-width: 0;
  box-sizing: border-box;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  font-size: 0.85rem;
}

.filter-select {
  box-sizing: border-box;
  width: 100%;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  font-size: 0.85rem;
}

.segmented-chips {
  display: flex;
  gap: 6px;
}

.chip-btn {
  flex: 1;
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #cbd5e1;
  background: #ffffff;
  font-size: 0.78rem;
  font-weight: 600;
  color: #475569;
  cursor: pointer;
}

.chip-btn.active {
  background: #554848;
  color: #ffffff;
  border-color: #554848;
}

.popover-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  border-top: 1px solid #f1f5f9;
  padding-top: 14px;
}

.btn-clear-filter {
  background: none;
  border: none;
  font-size: 0.85rem;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
}

.btn-apply-filter {
  background: #554848;
  border: none;
  padding: 8px 18px;
  border-radius: 8px;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}

/* ======================================================== */
/* RESPONSIVE DESIGN                                        */
/* ======================================================== */
@media (max-width: 1024px) {
  .plum-nav-header {
    padding: 0 16px;
  }
  
  .plum-search-capsule {
    display: none;
  }
  
  .plum-listings-column {
    width: 100%;
  }

  .map-viewport-section:not(.is-fullscreen-mode) {
    display: none;
  }
}
.search-toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: #1e293b;
  color: #fff;
  padding: 12px 24px;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  z-index: 9999;
}
.toast-fade-enter-active, .toast-fade-leave-active {
  transition: all 0.3s ease;
}
.toast-fade-enter-from, .toast-fade-leave-to {
  opacity: 0;
  transform: translate(-50%, 15px);
}
/* ══════════════════════════════════════════════════════════════
   INTERACTIVE MAP FALLBACK & VECTOR PIN STYLES
══════════════════════════════════════════════════════════════ */
.interactive-fallback-canvas {
  position: absolute;
  inset: 0;
  background: #E8ECE9;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-grid-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(to right, rgba(92, 78, 78, 0.06) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(92, 78, 78, 0.06) 1px, transparent 1px);
  background-size: 48px 48px;
}

.map-river-shape {
  position: absolute;
  top: 0;
  right: 18%;
  bottom: 0;
  width: 90px;
  background: #CBDCEB;
  opacity: 0.75;
  filter: blur(1px);
  transform: skewX(-12deg);
}

.vector-map-pin {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  z-index: 10;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.vector-map-pin:hover {
  transform: translate(-50%, -115%) scale(1.1);
  z-index: 50;
}

.vector-map-pin.active {
  transform: translate(-50%, -115%) scale(1.18);
  z-index: 100;
}

.pin-pill {
  background: #ffffff;
  color: #2A2421;
  font-weight: 700;
  font-size: 0.78rem;
  padding: 4px 10px;
  border-radius: 50px;
  box-shadow: 0 4px 12px rgba(42, 36, 33, 0.16);
  border: 1.5px solid #EDE8E3;
  white-space: nowrap;
  transition: all 0.18s ease;
}

.vector-map-pin.active .pin-pill {
  background: #5C4E4E;
  color: #ffffff;
  border-color: #5C4E4E;
  box-shadow: 0 6px 18px rgba(92, 78, 78, 0.35);
}

.pin-pointer {
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 6px solid #ffffff;
  margin-top: -1px;
}

.vector-map-pin.active .pin-pointer {
  border-top-color: #5C4E4E;
}

.fallback-map-badge {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(42, 36, 33, 0.85);
  color: #ffffff;
  font-size: 0.76rem;
  font-weight: 600;
  padding: 6px 16px;
  border-radius: 50px;
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
  z-index: 20;
  pointer-events: none;
}

.live-pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 8px #10B981;
  animation: pulse 1.6s infinite;
}

.vector-route-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 8;
}

.vector-user-pin {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  z-index: 18;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.vector-user-pin:hover {
  transform: translate(-50%, -112%) scale(1.08);
}

.user-pulse-ring {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%, 50%);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(37, 99, 235, 0.25);
  animation: pulse-ring 2s infinite cubic-bezier(0.215, 0.61, 0.355, 1);
  pointer-events: none;
}

@keyframes pulse-ring {
  0% {
    transform: translate(-50%, 50%) scale(0.6);
    opacity: 0.9;
  }
  100% {
    transform: translate(-50%, 50%) scale(2.2);
    opacity: 0;
  }
}

.user-loc-pill {
  background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
  color: #ffffff;
  font-weight: 700;
  font-size: 0.78rem;
  padding: 5px 12px;
  border-radius: 50px;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.38);
  border: 1.5px solid #60A5FA;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
}

.user-loc-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 6px #ffffff;
}

.user-loc-dot.is-locating {
  animation: pulse 0.8s infinite;
  background: #FEF08A;
}

.user-loc-pointer {
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 6px solid #1D4ED8;
  margin-top: -1px;
}

/* ======================================================== */
/* MANUAL LOCATION PLACER STYLES                            */
/* ======================================================== */
.btn-set-loc-pill {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  border: 1.5px solid #E2E8F0;
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #1E293B;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: all 0.18s ease;
}

.btn-set-loc-pill:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
}

.btn-set-loc-pill.is-manual {
  background: #EFF6FF;
  border-color: #93C5FD;
  color: #1D4ED8;
}

.btn-floating-filter.loc-manual {
  border-color: #93C5FD;
  background: #EFF6FF;
  color: #1D4ED8;
}

.origin-edit-badge {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #F1F5F9;
  color: #64748B;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  flex-shrink: 0;
  transition: all 0.18s ease;
}

.commute-origin-box:hover .origin-edit-badge {
  background: #E2E8F0;
  color: #1E293B;
}

.origin-gps-tag.manual {
  color: #2563EB;
}

/* Active Map Pick Banner */
.map-pick-indicator-banner {
  position: absolute;
  top: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 50;
  pointer-events: auto;
}

.pick-banner-content {
  background: rgba(15, 23, 42, 0.94);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #ffffff;
  font-size: 0.84rem;
  font-weight: 600;
  padding: 8px 20px;
  border-radius: 50px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.pick-pulse-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #3B82F6;
  box-shadow: 0 0 12px #3B82F6;
  animation: pulse 1s infinite;
}

.btn-cancel-pick {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: #ffffff;
  border-radius: 50px;
  padding: 3px 12px;
  font-size: 0.74rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s ease;
}

.btn-cancel-pick:hover {
  background: rgba(255, 255, 255, 0.35);
}

/* Location Picker Modal Overlay */
.location-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.52);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}

.location-modal-card {
  width: 100%;
  max-width: 480px;
  background: #ffffff;
  border-radius: 24px;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.22);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.loc-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 22px 24px 16px;
  border-bottom: 1px solid #F1F5F9;
}

.loc-header-title-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.loc-icon-bubble {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: #EFF6FF;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.loc-modal-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1E293B;
  margin: 0;
}

.loc-modal-subtitle {
  font-size: 0.8rem;
  color: #64748B;
  margin: 2px 0 0;
}

.loc-modal-close {
  background: none;
  border: none;
  font-size: 1.25rem;
  color: #94A3B8;
  cursor: pointer;
  padding: 4px;
  line-height: 1;
  transition: color 0.15s ease;
}

.loc-modal-close:hover {
  color: #334155;
}

.loc-modal-body {
  padding: 20px 24px;
  overflow-y: auto;
  max-height: 65vh;
}

.current-loc-status-card {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 14px;
  padding: 12px 16px;
  margin-bottom: 16px;
}

.loc-status-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.loc-indicator-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #94A3B8;
  flex-shrink: 0;
}

.loc-indicator-dot.gps {
  background: #10B981;
  box-shadow: 0 0 8px #10B981;
}

.loc-indicator-dot.manual {
  background: #2563EB;
  box-shadow: 0 0 8px #2563EB;
}

.loc-name-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.current-loc-name {
  font-size: 0.94rem;
  font-weight: 700;
  color: #1E293B;
}

.current-loc-coords {
  font-size: 0.74rem;
  color: #64748B;
}

.loc-action-buttons-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

.btn-loc-action {
  background: #ffffff;
  border: 1.5px solid #E2E8F0;
  border-radius: 14px;
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  text-align: left;
  transition: all 0.18s ease;
}

.btn-loc-action:hover {
  border-color: #3B82F6;
  background: #F8FAFC;
}

.btn-loc-action.primary {
  background: #EFF6FF;
  border-color: #93C5FD;
}

.btn-loc-action.primary:hover {
  background: #DBEAFE;
}

.btn-loc-action:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.action-icon {
  font-size: 1.4rem;
  line-height: 1;
}

.action-text {
  display: flex;
  flex-direction: column;
}

.action-bold {
  font-size: 0.88rem;
  font-weight: 700;
  color: #1E293B;
}

.action-hint {
  font-size: 0.72rem;
  color: #64748B;
  margin-top: 1px;
}

.loc-tip-box {
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  border-radius: 12px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.78rem;
  color: #92400E;
  margin-bottom: 18px;
}

.tip-icon {
  font-size: 1.1rem;
  flex-shrink: 0;
}

.presets-section-title {
  font-size: 0.84rem;
  font-weight: 700;
  color: #475569;
  margin: 0 0 10px;
}

.presets-pills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.district-preset-pill {
  background: #ffffff;
  border: 1.5px solid #E2E8F0;
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
}

.district-preset-pill:hover {
  border-color: #CBD5E1;
  background: #F8FAFC;
}

.district-preset-pill.is-active {
  background: #2563EB;
  color: #ffffff;
  border-color: #2563EB;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
}

.preset-check {
  font-weight: 800;
}

.loc-modal-footer {
  padding: 14px 24px;
  border-top: 1px solid #F1F5F9;
  display: flex;
  justify-content: flex-end;
}

.btn-loc-done {
  background: #5C4E4E;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  padding: 9px 24px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.18s ease;
}

.btn-loc-done:hover {
  background: #463B3B;
}
</style>
