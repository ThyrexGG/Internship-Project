<template>
  <div class="property-detail-page">
    
    <!-- ══════════════════════════════════════════════════════════════
         1. TOP NAVIGATION / BREADCRUMB BAR
    ══════════════════════════════════════════════════════════════ -->
    <nav class="detail-nav-bar" aria-label="Breadcrumb navigation">
      <div class="nav-bar-container">
        <div class="nav-left">
          <button class="nav-back-btn" type="button" aria-label="Back to listings" @click="goBack">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M15 18l-6-6 6-6"/>
            </svg>
            <span>Back to listings</span>
          </button>
          
          <div class="breadcrumb-trail">
            <span class="crumb-link" @click="goBack">Home</span>
            <span class="crumb-sep">/</span>
            <span class="crumb-link" @click="goBack">Phnom Penh</span>
            <span class="crumb-sep">/</span>
            <span class="crumb-current">{{ property.name }}</span>
          </div>
        </div>

        <div class="nav-right">
          <button class="nav-action-pill" type="button" aria-label="Share this property" @click="handleShare">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8M16 6l-4-4-4 4M12 2v13"/>
            </svg>
            <span>Share</span>
          </button>
          
          <button 
            class="nav-action-pill favorite-pill" 
            :class="{ active: property.liked }"
            type="button" 
            :aria-label="property.liked ? 'Remove from saved' : 'Save property'"
            @click="toggleFavorite"
          >
            <svg 
              width="16" 
              height="16" 
              viewBox="0 0 24 24" 
              :fill="property.liked ? '#E11D48' : 'none'" 
              :stroke="property.liked ? '#E11D48' : 'currentColor'" 
              stroke-width="2"
              class="heart-icon"
              :class="{ 'heart-pop': justFavorited }"
            >
              <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
            </svg>
            <span>{{ property.liked ? 'Saved' : 'Save' }}</span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Main Container -->
    <div class="detail-container">

      <!-- ══════════════════════════════════════════════════════════════
           2. PROPERTY HEADER (TITLE, BADGES & LOCATION)
      ══════════════════════════════════════════════════════════════ -->
      <header class="property-header-section">
        <div class="header-main-content">
          <div class="title-badge-row">
            <h1 class="property-main-title">{{ property.name }}</h1>
            <div class="header-badges">
              <span class="verified-partner-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="#10B981" stroke="none">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
                HomeSweet Verified
              </span>
              <span class="period-badge">{{ property.period || 'Long-term' }}</span>
            </div>
          </div>

          <div class="property-sub-meta">
            <div class="meta-rating">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="#F59E0B" stroke="#F59E0B" stroke-width="1">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
              </svg>
              <span class="rating-num">{{ property.rating || 4.9 }}</span>
              <span class="rating-count">(128 reviews)</span>
            </div>
            <span class="meta-dot">·</span>
            <div class="meta-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/>
              </svg>
              <span>{{ property.location }}</span>
            </div>
            <span class="meta-dot">·</span>
            <span class="meta-specs-brief">{{ property.beds }} Beds · {{ property.baths }} Baths · {{ property.sqft }} m²</span>
          </div>
        </div>
      </header>

      <!-- ══════════════════════════════════════════════════════════════
           3. PROPERTY IMAGE GALLERY (MOSAIC DESKTOP + CAROUSEL MOBILE)
      ══════════════════════════════════════════════════════════════ -->
      <section class="gallery-section" aria-label="Property photo gallery">
        
        <!-- Desktop Mosaic Gallery (5-photo layout) -->
        <div class="mosaic-gallery desktop-only">
          <div class="mosaic-primary" @click="openLightbox(0)">
            <img 
              :src="propertyImages[0]" 
              :alt="`${property.name} primary photo`" 
              class="mosaic-img"
              loading="eager"
            />
            <div class="mosaic-hover-overlay">
              <span class="view-prompt">Click to view full photo</span>
            </div>
          </div>

          <div class="mosaic-grid">
            <div 
              v-for="(img, idx) in secondaryImages" 
              :key="idx" 
              class="mosaic-thumb"
              @click="openLightbox(idx + 1)"
            >
              <img 
                :src="img" 
                :alt="`${property.name} photo ${idx + 2}`" 
                class="mosaic-img"
                loading="lazy"
              />
              <div class="mosaic-hover-overlay"></div>
            </div>
          </div>

          <!-- All Photos Trigger Button -->
          <button class="btn-all-photos" type="button" @click="openLightbox(0)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="3" width="7" height="7"></rect>
              <rect x="14" y="3" width="7" height="7"></rect>
              <rect x="14" y="14" width="7" height="7"></rect>
              <rect x="3" y="14" width="7" height="7"></rect>
            </svg>
            <span>Show all {{ propertyImages.length }} photos</span>
          </button>
        </div>

        <!-- Mobile Swipeable Hero -->
        <div class="mobile-gallery mobile-only">
          <div class="mobile-slider-track">
            <img 
              :src="propertyImages[activeMobileImage]" 
              :alt="property.name" 
              class="mobile-hero-img"
              @click="openLightbox(activeMobileImage)"
            />
            
            <button 
              v-if="activeMobileImage > 0" 
              class="mobile-nav-arrow left" 
              type="button" 
              aria-label="Previous photo"
              @click="activeMobileImage--"
            >
              ‹
            </button>
            <button 
              v-if="activeMobileImage < propertyImages.length - 1" 
              class="mobile-nav-arrow right" 
              type="button" 
              aria-label="Next photo"
              @click="activeMobileImage++"
            >
              ›
            </button>

            <div class="mobile-photo-counter">
              {{ activeMobileImage + 1 }} / {{ propertyImages.length }}
            </div>
          </div>
        </div>
      </section>

      <!-- ══════════════════════════════════════════════════════════════
           4. TWO-COLUMN MARKETPLACE WORKSPACE
      ══════════════════════════════════════════════════════════════ -->
      <div class="marketplace-grid">
        
        <!-- ── LEFT COLUMN: MAIN CONTENT ── -->
        <div class="marketplace-content">

          <!-- Host Quick Intro -->
          <section class="host-intro-card">
            <div class="host-avatar-wrap">
              <img 
                :src="hostData.avatar" 
                :alt="hostData.name" 
                class="host-avatar"
              />
              <div class="host-verified-check">✓</div>
            </div>
            <div class="host-text-details">
              <h2 class="host-title">Hosted by {{ hostData.name }}</h2>
              <p class="host-subtext">Verified Landlord · 100% response rate · Speaks Khmer & English</p>
            </div>
            <button class="btn-chat-host" type="button" @click="handleChatHost">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
              </svg>
              <span>Chat Host</span>
            </button>
          </section>

          <!-- ── BENTO PROPERTY HIGHLIGHTS ── -->
          <section class="bento-section">
            <h2 class="section-title">Property Highlights</h2>
            
            <div class="bento-grid">
              <!-- Large Bento Card 1: Bedrooms -->
              <div class="bento-card bento-large">
                <div class="bento-icon-badge">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
                  </svg>
                </div>
                <div class="bento-content">
                  <div class="bento-value">{{ property.beds }} Private Bedrooms</div>
                  <div class="bento-label">Accommodates {{ property.pax || '2–4' }} guests with premium mattress setups and natural daylight.</div>
                </div>
              </div>

              <!-- Large Bento Card 2: Bathrooms -->
              <div class="bento-card bento-large">
                <div class="bento-icon-badge">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>
                  </svg>
                </div>
                <div class="bento-content">
                  <div class="bento-value">{{ property.baths }} Clean Bathrooms</div>
                  <div class="bento-label">Modern en-suite sanitary with instant hot shower systems and premium tile finishing.</div>
                </div>
              </div>

              <!-- Medium Bento Card 1: Floor Area -->
              <div class="bento-card bento-medium">
                <div class="bento-icon-badge">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2"/>
                  </svg>
                </div>
                <div class="bento-content">
                  <div class="bento-value">{{ property.sqft }} m² Living Space</div>
                  <div class="bento-label">Thoughtfully planned open layout with spacious living & study zone.</div>
                </div>
              </div>

              <!-- Medium Bento Card 2: Furnishing & Type -->
              <div class="bento-card bento-medium">
                <div class="bento-icon-badge">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/><path d="M9 21V12h6v9"/>
                  </svg>
                </div>
                <div class="bento-content">
                  <div class="bento-value">Fully Furnished {{ property.type ? property.type.toUpperCase() : 'CONDO' }}</div>
                  <div class="bento-label">Turnkey move-in ready with work desk, wardrobe, and dining area.</div>
                </div>
              </div>

              <!-- Small Bento Amenities (Rendered only if in property.amenities) -->
              <div v-if="hasAmenity('wifi')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>
                </svg>
                <span>High-Speed Wi-Fi</span>
              </div>

              <div v-if="hasAmenity('ac')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>
                </svg>
                <span>Inverter A/C</span>
              </div>

              <div v-if="hasAmenity('kitchen')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 3v18M6 3v7a4 4 0 0 0 4 4v7M3 3h6M15 3h6"/>
                </svg>
                <span>Equipped Kitchen</span>
              </div>

              <div v-if="hasAmenity('parking')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/>
                </svg>
                <span>Secured Parking</span>
              </div>

              <div v-if="hasAmenity('pool')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M2 12h20M2 17h20M2 7c4 0 4 3 8 3s4-3 8-3 4 3 8 3"/>
                </svg>
                <span>Swimming Pool</span>
              </div>

              <div v-if="hasAmenity('washer')" class="bento-card bento-small">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="2" width="18" height="20" rx="2"/><circle cx="12" cy="13" r="5"/><path d="M12 18a5 5 0 0 0 5-5"/>
                </svg>
                <span>In-Unit Laundry</span>
              </div>
            </div>
          </section>

          <!-- ── DESCRIPTION SECTION ── -->
          <section class="description-section">
            <h2 class="section-title">About this home</h2>
            <div class="desc-text-wrapper">
              <p class="desc-paragraph">
                <strong>{{ property.name }}</strong> is a thoughtfully designed residence offering a seamless blend of modern comfort and urban convenience. Positioned in the heart of {{ property.location }}, this home provides immediate access to major academic campuses, vibrant coffee shops, and daily essentials.
              </p>
              <p class="desc-paragraph">
                The interior features a clean architectural layout with generous natural light, dedicated study zones for students and remote professionals, and full climate control. Resident amenities include high-speed fiber internet, 24/7 building security, elevator access, and dedicated parking.
              </p>
            </div>
          </section>

          <!-- ── EXPLORE LIKE A LOCAL / NEIGHBORHOOD ── -->
          <section class="neighborhood-section">
            <div class="neighborhood-header">
              <h2 class="section-title">Explore Like a Local</h2>
              <span class="location-tag">{{ property.location }}</span>
            </div>
            
            <p class="neighborhood-intro">
              Situated in an active, friendly neighborhood with top convenience scores. Here is what is right around your future doorstep:
            </p>

            <div class="landmarks-grid">
              <div class="landmark-card" v-for="(place, pIdx) in neighborhoodPlaces" :key="pIdx">
                <div class="place-icon-wrap" :class="place.type">
                  <svg v-if="place.type === 'edu'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>
                  </svg>
                  <svg v-else-if="place.type === 'cafe'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8zM6 1v3M10 1v3M14 1v3"/>
                  </svg>
                  <svg v-else-if="place.type === 'market'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
                  </svg>
                  <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                  </svg>
                </div>
                <div class="place-info">
                  <span class="place-name">{{ place.name }}</span>
                  <span class="place-category">{{ place.category }}</span>
                </div>
                <div class="place-distance">{{ place.distance }}</div>
              </div>
            </div>

            <!-- Visual Map Card with Coordinates -->
            <div class="map-preview-card">
              <div class="map-interactive-substrate">
                <div class="map-pin-pulse">
                  <div class="pin-dot"></div>
                  <div class="pin-ring"></div>
                </div>
                <div class="map-label-chip">
                  <strong>{{ property.name }}</strong>
                  <span>{{ property.location }}</span>
                </div>
              </div>
              <div class="map-action-footer">
                <span>Coordinates: {{ property.lat }}, {{ property.lng }}</span>
                <a 
                  :href="`https://www.google.com/maps?q=${property.lat},${property.lng}`" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="btn-open-maps"
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
                  </svg>
                  Open in Google Maps
                </a>
              </div>
            </div>
          </section>

          <!-- ── RECENT TENANTS ── -->
          <section class="renters-section">
            <h2 class="section-title">Recent Tenants</h2>
            <p class="renters-subtext">Students & young professionals who called this place home:</p>
            <div class="renter-list">
              <div class="renter-card" v-for="(renter, r) in renters" :key="r">
                <img :src="renter.avatar" :alt="renter.name" class="renter-avatar" />
                <div class="renter-details">
                  <span class="renter-name">{{ renter.name }}</span>
                  <span class="renter-tag">Verified Tenant</span>
                </div>
              </div>
            </div>
          </section>

          <!-- ── RATINGS & REVIEWS ── -->
          <section class="rate-section">
            <div class="rate-summary-bar">
              <div class="score-box">
                <span class="big-score">{{ property.rating || 4.9 }}</span>
                <div class="score-stars">
                  <svg v-for="s in 5" :key="s" width="16" height="16" viewBox="0 0 24 24" fill="#F59E0B" stroke="#F59E0B" stroke-width="1">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                </div>
              </div>
              <div class="score-meta">
                <span class="overall-label">Outstanding Living Experience</span>
                <span class="review-total-label">Based on 128 verified tenant evaluations</span>
              </div>
            </div>
            
            <div class="reviews-list">
              <div class="review-card" v-for="(review, rv) in reviews" :key="rv">
                <div class="review-header">
                  <div class="reviewer-avatar-circle">
                    {{ review.name.charAt(0) }}
                  </div>
                  <div class="reviewer-info">
                    <span class="reviewer-name">{{ review.name }}</span>
                    <span class="review-date">{{ review.date }} · Verified Student</span>
                  </div>
                </div>
                <div class="review-stars">
                  <svg v-for="s in 5" :key="s" width="13" height="13" viewBox="0 0 24 24" fill="#F59E0B" stroke="#F59E0B" stroke-width="1">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                </div>
                <p class="review-text">{{ review.text }}</p>
              </div>
            </div>
          </section>

          <!-- ── CONTACT HOST SECTION ── -->
          <section class="contact-section">
            <h2 class="section-title">Direct Host Contact</h2>
            <div class="contact-channels-grid">
              <div class="channel-pill fb">
                <div class="c-icon-badge">FB</div>
                <div class="c-info">
                  <span class="c-label">Facebook Page</span>
                  <span class="c-val">{{ property.name }} Cambodia</span>
                </div>
              </div>
              <div class="channel-pill tg">
                <div class="c-icon-badge">TG</div>
                <div class="c-info">
                  <span class="c-label">Telegram Host</span>
                  <span class="c-val">@homesweet_host</span>
                </div>
              </div>
              <div class="channel-pill ph">
                <div class="c-icon-badge">TEL</div>
                <div class="c-info">
                  <span class="c-label">Direct Hotline</span>
                  <span class="c-val">081 743 949</span>
                </div>
              </div>
            </div>
          </section>

        </div>

        <!-- ── RIGHT COLUMN: STICKY BOOKING / INQUIRY CARD ── -->
        <aside class="marketplace-sidebar">
          <div class="sticky-booking-card">
            
            <!-- Price Display Header -->
            <div class="booking-price-header">
              <div class="price-stack">
                <span class="price-currency">$</span>
                <span class="price-number">{{ property.price }}</span>
                <span class="price-freq">/ month</span>
              </div>
              <div class="booking-guarantee-tag">Instant Booking</div>
            </div>

            <div class="booking-card-divider"></div>

            <!-- Interactive Parameters -->
            <div class="booking-inputs-block">
              <!-- Check-in Date -->
              <div class="booking-input-row">
                <label class="input-label" for="bookingCheckin">Move-in Date</label>
                <div class="date-input-wrap">
                  <input 
                    id="bookingCheckin" 
                    v-model="bookingForm.checkInDate" 
                    type="date" 
                    class="booking-date-field" 
                  />
                </div>
              </div>

              <!-- Lease Duration Selection -->
              <div class="booking-input-row">
                <label class="input-label">Lease Duration</label>
                <div class="duration-pill-group">
                  <button 
                    v-for="dur in durationOptions" 
                    :key="dur.value"
                    type="button" 
                    class="dur-pill" 
                    :class="{ active: bookingForm.duration === dur.value }"
                    @click="bookingForm.duration = dur.value"
                  >
                    {{ dur.label }}
                  </button>
                </div>
              </div>

              <!-- Guests Selection -->
              <div class="booking-input-row">
                <label class="input-label">Occupants / Guests</label>
                <select v-model="bookingForm.guests" class="booking-select-field">
                  <option :value="1">1 Resident</option>
                  <option :value="2">2 Residents</option>
                  <option :value="3">3 Residents</option>
                  <option :value="4">4 Residents</option>
                </select>
              </div>
            </div>

            <!-- Price Breakdown Calculation -->
            <div class="booking-calculation">
              <div class="calc-line">
                <span>Monthly Rent</span>
                <span>${{ property.price }}</span>
              </div>
              <div class="calc-line">
                <span>Security Deposit (Refundable)</span>
                <span>${{ property.price }}</span>
              </div>
              <div class="calc-line">
                <span>Estimated Utilities</span>
                <span>~$25</span>
              </div>
              <div class="calc-divider"></div>
              <div class="calc-line total-line">
                <span>Total Due at Signing</span>
                <span class="total-amount">${{ property.price * 2 }}</span>
              </div>
            </div>

            <!-- Action Buttons Stack (Preserving All Existing Functional Routes!) -->
            <div class="booking-actions-stack">
              <!-- Primary: Rent / Apply -->
              <button 
                class="btn-booking-primary" 
                type="button" 
                @click="handleRentApply"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" />
                </svg>
                <span>Rent House / Apply</span>
              </button>

              <!-- Secondary: Instant Pay -->
              <button 
                class="btn-booking-pay" 
                type="button" 
                @click="handlePayNow"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect>
                  <line x1="1" y1="10" x2="23" y2="10"></line>
                </svg>
                <span>Pay Deposit Now</span>
              </button>

              <!-- Roommate Match Link -->
              <button 
                class="btn-booking-roommate" 
                type="button" 
                @click="handleFindRoommate"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" />
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 010 7.75" />
                </svg>
                <span>Find Roommate to Split</span>
              </button>

              <!-- Landlord Profile Link -->
              <button 
                class="btn-booking-landlord" 
                type="button" 
                @click="handleViewLandlordProfile"
              >
                <span>View Landlord Profile & Reviews →</span>
              </button>
            </div>

            <!-- Trust & Guarantee Footer -->
            <div class="booking-trust-footer">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              </svg>
              <span>100% Protected by HomeSweet Tenant Guarantee</span>
            </div>

          </div>
        </aside>

      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════════
         5. FULL-SCREEN LIGHTBOX MODAL
    ══════════════════════════════════════════════════════════════ -->
    <div 
      v-if="lightboxOpen" 
      class="lightbox-backdrop" 
      role="dialog" 
      aria-modal="true" 
      aria-label="Property photo lightbox"
      @click.self="closeLightbox"
    >
      <!-- Lightbox Header Bar -->
      <div class="lightbox-header">
        <span class="lightbox-counter">Photo {{ lightboxIndex + 1 }} of {{ propertyImages.length }}</span>
        <button 
          class="lightbox-close-btn" 
          type="button" 
          aria-label="Close photo lightbox"
          @click="closeLightbox"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Main Lightbox Stage -->
      <div class="lightbox-stage">
        <button 
          class="lightbox-arrow prev" 
          type="button" 
          aria-label="Previous photo"
          @click="prevPhoto"
        >
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
        </button>

        <div class="lightbox-image-container">
          <img 
            :src="propertyImages[lightboxIndex]" 
            :alt="`${property.name} photo ${lightboxIndex + 1}`"
            class="lightbox-current-image" 
          />
        </div>

        <button 
          class="lightbox-arrow next" 
          type="button" 
          aria-label="Next photo"
          @click="nextPhoto"
        >
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2">
            <path d="M9 18l6-6-6-6"/>
          </svg>
        </button>
      </div>

      <!-- Bottom Thumbnail Carousel Strip -->
      <div class="lightbox-thumbs-strip">
        <div 
          v-for="(tImg, tIdx) in propertyImages" 
          :key="tIdx"
          class="lightbox-thumb-item" 
          :class="{ active: lightboxIndex === tIdx }"
          @click="lightboxIndex = tIdx"
        >
          <img :src="tImg" :alt="`Thumbnail ${tIdx + 1}`" />
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════
         6. MOBILE FIXED BOTTOM ACTION BAR
    ══════════════════════════════════════════════════════════════ -->
    <div class="mobile-sticky-bottom-bar mobile-only">
      <div class="mobile-bar-price">
        <span class="m-price">${{ property.price }}</span>
        <span class="m-period">/ month</span>
      </div>
      <button class="m-btn-apply" type="button" @click="handleRentApply">
        Rent House
      </button>
    </div>

    <!-- Global Footer -->
    <GlobalFooter />

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { properties } from '../../store.js'
import GlobalFooter from '../../components/GlobalFooter.vue'

const route = useRoute()
const router = useRouter()
const propertyId = parseInt(route.params.id)

// Find property by id or fallback to first one
const property = computed(() => {
  return properties.value.find(p => p.id === propertyId) || properties.value[0]
})

// Images Array
const propertyImages = computed(() => {
  return property.value?.images && property.value.images.length > 0 
    ? property.value.images 
    : ['/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg']
})

const secondaryImages = computed(() => {
  return propertyImages.value.slice(1, 5)
})

// Active Mobile Hero Index
const activeMobileImage = ref(0)

// ── Lightbox State & Controls ──
const lightboxOpen = ref(false)
const lightboxIndex = ref(0)

const openLightbox = (index = 0) => {
  lightboxIndex.value = index
  lightboxOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeLightbox = () => {
  lightboxOpen.value = false
  document.body.style.overflow = ''
}

const nextPhoto = () => {
  if (lightboxIndex.value < propertyImages.value.length - 1) {
    lightboxIndex.value++
  } else {
    lightboxIndex.value = 0
  }
}

const prevPhoto = () => {
  if (lightboxIndex.value > 0) {
    lightboxIndex.value--
  } else {
    lightboxIndex.value = propertyImages.value.length - 1
  }
}

const handleKeydown = (e) => {
  if (!lightboxOpen.value) return
  if (e.key === 'Escape') closeLightbox()
  if (e.key === 'ArrowRight') nextPhoto()
  if (e.key === 'ArrowLeft') prevPhoto()
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  document.body.style.overflow = ''
})

// ── Favorite & Share Interactions ──
const justFavorited = ref(false)
const toggleFavorite = () => {
  property.value.liked = !property.value.liked
  if (property.value.liked) {
    justFavorited.value = true
    setTimeout(() => { justFavorited.value = false }, 400)
  }
}

const goBack = () => {
  if (route.query.from === 'search') {
    router.push('/search')
  } else {
    router.push('/home')
  }
}

const handleShare = () => {
  if (navigator.share) {
    navigator.share({
      title: property.value?.name || 'HomeSweet Property',
      text: `Check out ${property.value?.name} on HomeSweet!`,
      url: window.location.href
    }).catch(() => {})
  } else {
    navigator.clipboard?.writeText(window.location.href)
    alert('Property link copied to clipboard!')
  }
}

// ── Amenities Check Helper ──
const hasAmenity = (key) => {
  if (!property.value?.amenities) return false
  return property.value.amenities.includes(key)
}

// ── Booking Parameters ──
const defaultCheckIn = new Date(Date.now() + 86400000).toISOString().split('T')[0]
const bookingForm = ref({
  checkInDate: defaultCheckIn,
  duration: '6m',
  guests: 1
})

const durationOptions = [
  { label: '1 Mo', value: '1m' },
  { label: '3 Mo', value: '3m' },
  { label: '6 Mo', value: '6m' },
  { label: '1 Yr', value: '1y' }
]

// ── Navigation Action Handlers ──
const handleRentApply = () => {
  router.push(`/property/${property.value.id}/apply`)
}

const handlePayNow = () => {
  router.push(`/property/${property.value.id}/payment`)
}

const handleFindRoommate = () => {
  router.push(`/property/${property.value.id}/roommate`)
}

const handleViewLandlordProfile = () => {
  router.push(`/landlord-profile/${property.value.id}?from=${route.query.from || ''}`)
}

const handleChatHost = () => {
  router.push({
    path: '/chat',
    query: {
      landlordId: `landlord_${property.value.id}`,
      contact: `${property.value.name} Host`
    }
  })
}

// ── Host Data ──
const hostData = computed(() => {
  return {
    name: property.value.contactName || `${property.value.name} Host`,
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&q=80',
    role: 'Verified Landlord'
  }
})

// ── Neighborhood Points of Interest (Phnom Penh) ──
const neighborhoodPlaces = computed(() => {
  const loc = property.value.location || ''
  if (loc.includes('Chroy Chongva')) {
    return [
      { name: 'Norton University Campus', category: 'Education', distance: '5 min drive', type: 'edu' },
      { name: 'Brown Coffee Riverside', category: 'Cafe & Bakery', distance: '3 min walk', type: 'cafe' },
      { name: 'Bayon Supermarket Chroy Changvar', category: 'Grocery', distance: '4 min walk', type: 'market' },
      { name: 'Sunrise Japan Hospital', category: 'Medical', distance: '6 min drive', type: 'hospital' }
    ]
  } else if (loc.includes('BKK1') || loc.includes('Chamkarmon')) {
    return [
      { name: 'Paragon International University', category: 'Education', distance: '8 min drive', type: 'edu' },
      { name: 'Starbucks BKK1 Flagship', category: 'Cafe', distance: '2 min walk', type: 'cafe' },
      { name: 'Lucky Supermarket Sihanouk Blvd', category: 'Grocery', distance: '5 min walk', type: 'market' },
      { name: 'Khema International Polyclinic', category: 'Medical', distance: '4 min drive', type: 'hospital' }
    ]
  } else if (loc.includes('Toul Kork')) {
    return [
      { name: 'Royal University of Phnom Penh (RUPP)', category: 'Education', distance: '6 min drive', type: 'edu' },
      { name: 'Tube Coffee TK Avenue', category: 'Cafe & Study', distance: '3 min walk', type: 'cafe' },
      { name: 'TK Avenue Shopping Centre', category: 'Retail & Dining', distance: '4 min walk', type: 'market' },
      { name: 'Royal Phnom Penh Hospital', category: 'Medical', distance: '7 min drive', type: 'hospital' }
    ]
  }
  return [
    { name: 'Norton University Campus', category: 'Education', distance: '6 min drive', type: 'edu' },
    { name: 'Brown Coffee Flagship', category: 'Cafe & Workspace', distance: '3 min walk', type: 'cafe' },
    { name: 'Lucky Supermarket Express', category: 'Grocery', distance: '5 min walk', type: 'market' },
    { name: 'Community Medical Clinic', category: 'Healthcare', distance: '6 min drive', type: 'hospital' }
  ]
})

// Mock Tenants
const renters = [
  { name: 'Yim Vatey', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&q=80' },
  { name: 'Muy Leng', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&q=80' },
  { name: 'Neav Sveita', avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80' }
]

// Mock Reviews
const reviews = [
  { 
    name: 'Sokha Meng', 
    date: '3 days ago', 
    text: 'Living here during my university semester has been exceptional. The building is quiet at night, fast Wi-Fi makes remote coursework effortless, and the landlord is very responsive.' 
  },
  { 
    name: 'Dara Pich', 
    date: '2 weeks ago', 
    text: 'Extremely clean and secure apartment with modern fittings. The location is peaceful yet close to cafes and markets. Highly recommend for students and young professionals.' 
  }
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.property-detail-page {
  font-family: 'Plus Jakarta Sans', 'DM Sans', sans-serif;
  background-color: var(--color-bg-canvas, #FAF8F5);
  color: var(--color-text-primary, #2A2421);
  min-height: 100vh;
  overflow-x: hidden;
}

/* ══════════════════════════════════════════════════════════════
   1. NAVIGATION BAR
══════════════════════════════════════════════════════════════ */
.detail-nav-bar {
  position: sticky;
  top: 0;
  z-index: 40;
  background: rgba(255, 255, 255, 0.92);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  backdrop-filter: blur(16px) saturate(180%);
  border-bottom: 1px solid var(--color-border, #EDE8E3);
  box-shadow: 0 1px 3px rgba(42, 36, 33, 0.03);
}

.nav-bar-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-back-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-pill, 50px);
  color: var(--color-text-primary, #2A2421);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--shadow-elevation-1-specular, 0 1px 3px rgba(42, 36, 33, 0.04));
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-back-btn:hover {
  background: #F4EDEA;
  border-color: var(--color-primary, #5C4E4E);
  transform: translateY(-1px);
}

.breadcrumb-trail {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--color-text-muted, #8C7E7E);
}

.crumb-link {
  cursor: pointer;
  transition: color 0.15s;
}

.crumb-link:hover {
  color: var(--color-primary, #5C4E4E);
  text-decoration: underline;
}

.crumb-sep {
  opacity: 0.5;
}

.crumb-current {
  font-weight: 600;
  color: var(--color-text-primary, #2A2421);
  max-width: 220px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-action-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-pill, 50px);
  color: var(--color-text-primary, #2A2421);
  font-size: 0.86rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--shadow-elevation-1-specular, 0 1px 3px rgba(42, 36, 33, 0.04));
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-action-pill:hover {
  background: #F4EDEA;
  border-color: var(--color-primary, #5C4E4E);
  transform: translateY(-1px);
}

.favorite-pill.active {
  border-color: #F43F5E;
  color: #E11D48;
  background: #FFF1F2;
}

/* ══════════════════════════════════════════════════════════════
   2. MAIN DETAIL CONTAINER & HEADER
══════════════════════════════════════════════════════════════ */
.detail-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 28px 24px 80px;
}

.property-header-section {
  margin-bottom: 24px;
}

.title-badge-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 8px;
}

.property-main-title {
  font-size: 2.1rem;
  font-weight: 800;
  color: var(--color-text-primary, #2A2421);
  letter-spacing: -0.5px;
  margin: 0;
  line-height: 1.2;
}

.header-badges {
  display: flex;
  align-items: center;
  gap: 8px;
}

.verified-partner-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: #ECFDF5;
  color: #065F46;
  border: 1px solid #A7F3D0;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-pill, 50px);
}

.period-badge {
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  color: var(--color-text-secondary, #5C4E4E);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-pill, 50px);
}

.property-sub-meta {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  font-size: 0.95rem;
  color: var(--color-text-secondary, #5C4E4E);
}

.meta-rating {
  display: flex;
  align-items: center;
  gap: 4px;
}

.rating-num {
  font-weight: 700;
  color: #1E1B18;
}

.rating-count {
  color: var(--color-text-muted, #8C7E7E);
  font-size: 0.88rem;
}

.meta-location {
  display: flex;
  align-items: center;
  gap: 4px;
  color: var(--color-text-primary, #2A2421);
  font-weight: 600;
}

.meta-dot {
  color: var(--color-text-muted, #8C7E7E);
}

/* ══════════════════════════════════════════════════════════════
   3. IMAGE GALLERY (MOSAIC DESKTOP)
══════════════════════════════════════════════════════════════ */
.gallery-section {
  position: relative;
  margin-bottom: 36px;
}

.mosaic-gallery {
  position: relative;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 12px;
  height: 480px;
  border-radius: var(--radius-xl, 18px);
  overflow: hidden;
  box-shadow: var(--shadow-elevation-1-specular, 0 4px 16px rgba(42, 36, 33, 0.06));
}

.mosaic-primary {
  position: relative;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  background-color: #EDE8E3;
}

.mosaic-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 12px;
  height: 100%;
}

.mosaic-thumb {
  position: relative;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  background-color: #EDE8E3;
}

.mosaic-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), filter 0.35s ease;
}

.mosaic-primary:hover .mosaic-img,
.mosaic-thumb:hover .mosaic-img {
  transform: scale(1.03);
}

.mosaic-hover-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.25s ease;
}

.mosaic-primary:hover .mosaic-hover-overlay {
  background: rgba(0, 0, 0, 0.15);
}

.view-prompt {
  background: rgba(0, 0, 0, 0.65);
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 50px;
  backdrop-filter: blur(6px);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.mosaic-primary:hover .view-prompt {
  opacity: 1;
}

.btn-all-photos {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: rgba(255, 255, 255, 0.94);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: var(--radius-pill, 50px);
  padding: 9px 18px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 700;
  color: #1E1B18;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-all-photos:hover {
  background: #ffffff;
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
}

/* Mobile Hero Carousel */
.mobile-gallery {
  position: relative;
  width: 100%;
  height: 280px;
  border-radius: var(--radius-lg, 14px);
  overflow: hidden;
  background: #EDE8E3;
}

.mobile-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.mobile-nav-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid var(--color-border);
  color: #1E1B18;
  font-size: 1.4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.mobile-nav-arrow.left { left: 12px; }
.mobile-nav-arrow.right { right: 12px; }

.mobile-photo-counter {
  position: absolute;
  bottom: 12px;
  right: 12px;
  background: rgba(0, 0, 0, 0.65);
  color: #ffffff;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 50px;
  backdrop-filter: blur(4px);
}

/* ══════════════════════════════════════════════════════════════
   4. TWO-COLUMN MARKETPLACE WORKSPACE
══════════════════════════════════════════════════════════════ */
.marketplace-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 48px;
  align-items: start;
}

.marketplace-content {
  min-width: 0;
}

/* Section Title Standard */
.section-title {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--color-text-primary, #2A2421);
  letter-spacing: -0.3px;
  margin-top: 0;
  margin-bottom: 20px;
}

/* Host Quick Card */
.host-intro-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-lg, 14px);
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.04));
  margin-bottom: 36px;
}

.host-avatar-wrap {
  position: relative;
  width: 54px;
  height: 54px;
  flex-shrink: 0;
}

.host-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.host-verified-check {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 18px;
  height: 18px;
  background: #10B981;
  color: #ffffff;
  border-radius: 50%;
  font-size: 0.68rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #ffffff;
}

.host-text-details {
  flex: 1;
  min-width: 0;
}

.host-title {
  font-size: 1.12rem;
  font-weight: 700;
  margin: 0 0 2px;
  color: var(--color-text-primary, #2A2421);
}

.host-subtext {
  font-size: 0.85rem;
  color: var(--color-text-muted, #8C7E7E);
  margin: 0;
}

.btn-chat-host {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-pill, 50px);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-primary, #5C4E4E);
  cursor: pointer;
  transition: all 0.15s ease;
  flex-shrink: 0;
}

.btn-chat-host:hover {
  background: #F4EDEA;
  border-color: var(--color-primary, #5C4E4E);
}

/* ── BENTO HIGHLIGHTS ── */
.bento-section {
  margin-bottom: 40px;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.bento-card {
  background: #ffffff;
  border: 1px solid rgba(237, 232, 227, 0.95);
  border-radius: var(--radius-lg, 14px);
  padding: 20px;
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.04));
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
}

.bento-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-elevation-2-specular, 0 6px 18px rgba(42, 36, 33, 0.08));
}

.bento-large {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.bento-medium {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.bento-icon-badge {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  color: var(--color-primary, #5C4E4E);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.bento-content {
  flex: 1;
}

.bento-value {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
  margin-bottom: 4px;
}

.bento-label {
  font-size: 0.85rem;
  color: var(--color-text-muted, #8C7E7E);
  line-height: 1.4;
}

.bento-small {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--color-text-primary, #2A2421);
}

.bento-small svg {
  color: var(--color-primary, #5C4E4E);
  flex-shrink: 0;
}

/* ── DESCRIPTION SECTION ── */
.description-section {
  margin-bottom: 44px;
}

.desc-paragraph {
  font-size: 1.02rem;
  line-height: 1.7;
  color: #473B3B;
  margin-bottom: 16px;
}

/* ── NEIGHBORHOOD SECTION ── */
.neighborhood-section {
  margin-bottom: 44px;
}

.neighborhood-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.location-tag {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-primary, #5C4E4E);
  background: #FAF8F5;
  padding: 4px 12px;
  border-radius: var(--radius-pill, 50px);
  border: 1px solid var(--color-border, #EDE8E3);
}

.neighborhood-intro {
  font-size: 0.95rem;
  color: var(--color-text-muted, #8C7E7E);
  margin-bottom: 20px;
}

.landmarks-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.landmark-card {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-md, 10px);
  padding: 14px 16px;
  box-shadow: 0 1px 3px rgba(42, 36, 33, 0.03);
}

.place-icon-wrap {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.place-icon-wrap.edu { background: #EEF2FF; color: #4F46E5; }
.place-icon-wrap.cafe { background: #FEF3C7; color: #D97706; }
.place-icon-wrap.market { background: #ECFDF5; color: #059669; }
.place-icon-wrap.hospital { background: #FEE2E2; color: #DC2626; }

.place-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.place-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.place-category {
  font-size: 0.76rem;
  color: var(--color-text-muted, #8C7E7E);
}

.place-distance {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--color-primary, #5C4E4E);
  background: #FAF8F5;
  padding: 4px 8px;
  border-radius: 6px;
  flex-shrink: 0;
}

/* Map Interactive Card */
.map-preview-card {
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-lg, 14px);
  overflow: hidden;
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.04));
}

.map-interactive-substrate {
  position: relative;
  height: 200px;
  background-color: #E6E2DC;
  background-image: 
    linear-gradient(rgba(255,255,255,0.4) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.4) 1px, transparent 1px);
  background-size: 32px 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-pin-pulse {
  position: relative;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pin-dot {
  width: 14px;
  height: 14px;
  background: #E11D48;
  border-radius: 50%;
  border: 2px solid #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
  z-index: 2;
}

.pin-ring {
  position: absolute;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(225, 29, 72, 0.25);
  animation: pulse 2s infinite ease-out;
}

@keyframes pulse {
  0% { transform: scale(0.6); opacity: 0.9; }
  100% { transform: scale(1.6); opacity: 0; }
}

.map-label-chip {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(8px);
  padding: 8px 14px;
  border-radius: 8px;
  border: 1px solid rgba(237, 232, 227, 0.9);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  font-size: 0.8rem;
}

.map-label-chip strong {
  color: #1E1B18;
}

.map-label-chip span {
  color: #8C7E7E;
  font-size: 0.75rem;
}

.map-action-footer {
  padding: 12px 18px;
  background: #FAF8F5;
  border-top: 1px solid var(--color-border, #EDE8E3);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--color-text-muted, #8C7E7E);
}

.btn-open-maps {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--color-primary, #5C4E4E);
  font-weight: 700;
  text-decoration: none;
  transition: color 0.15s;
}

.btn-open-maps:hover {
  color: #1E1B18;
  text-decoration: underline;
}

/* ── RENTERS LIST ── */
.renters-section {
  margin-bottom: 44px;
}

.renters-subtext {
  font-size: 0.92rem;
  color: var(--color-text-muted, #8C7E7E);
  margin-top: -12px;
  margin-bottom: 18px;
}

.renter-list {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.renter-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-pill, 50px);
  box-shadow: 0 1px 3px rgba(42, 36, 33, 0.03);
}

.renter-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
}

.renter-details {
  display: flex;
  flex-direction: column;
}

.renter-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
}

.renter-tag {
  font-size: 0.72rem;
  font-weight: 600;
  color: #059669;
}

/* ── RATINGS & REVIEWS ── */
.rate-section {
  margin-bottom: 44px;
}

.rate-summary-bar {
  display: flex;
  align-items: center;
  gap: 20px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-lg, 14px);
  padding: 20px 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.04));
}

.score-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-right: 20px;
  border-right: 1px solid var(--color-border, #EDE8E3);
}

.big-score {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--color-text-primary, #2A2421);
  line-height: 1;
  margin-bottom: 4px;
}

.score-stars {
  display: flex;
  gap: 2px;
}

.score-meta {
  display: flex;
  flex-direction: column;
}

.overall-label {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
  margin-bottom: 2px;
}

.review-total-label {
  font-size: 0.85rem;
  color: var(--color-text-muted, #8C7E7E);
}

.reviews-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.review-card {
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-lg, 14px);
  padding: 20px;
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.04));
}

.review-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.reviewer-avatar-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #FAF8F5;
  border: 1px solid var(--color-border);
  color: var(--color-primary, #5C4E4E);
  font-weight: 800;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.reviewer-info {
  display: flex;
  flex-direction: column;
}

.reviewer-name {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
}

.review-date {
  font-size: 0.78rem;
  color: var(--color-text-muted, #8C7E7E);
}

.review-stars {
  display: flex;
  gap: 2px;
  margin-bottom: 10px;
}

.review-text {
  font-size: 0.9rem;
  line-height: 1.6;
  color: #473B3B;
  margin: 0;
}

/* ── CONTACT SECTION ── */
.contact-section {
  margin-bottom: 44px;
}

.contact-channels-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.channel-pill {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #ffffff;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-lg, 14px);
  padding: 16px;
  box-shadow: var(--shadow-elevation-1-specular, 0 2px 8px rgba(42, 36, 33, 0.03));
}

.c-icon-badge {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.78rem;
  flex-shrink: 0;
}

.channel-pill.fb .c-icon-badge { background: #1877F2; color: #ffffff; }
.channel-pill.tg .c-icon-badge { background: #2AABEE; color: #ffffff; }
.channel-pill.ph .c-icon-badge { background: #10B981; color: #ffffff; }

.c-info {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.c-label {
  font-size: 0.75rem;
  color: var(--color-text-muted, #8C7E7E);
}

.c-val {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-text-primary, #2A2421);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ══════════════════════════════════════════════════════════════
   5. STICKY BOOKING / INQUIRY CARD (RIGHT COLUMN)
══════════════════════════════════════════════════════════════ */
.marketplace-sidebar {
  position: relative;
}

.sticky-booking-card {
  position: sticky;
  top: 90px;
  background: #ffffff;
  border: 1px solid rgba(220, 214, 205, 0.95);
  border-radius: var(--radius-xl, 18px);
  padding: 26px;
  box-shadow: var(--shadow-elevation-2-specular, 0 8px 30px rgba(42, 36, 33, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.95));
}

.booking-price-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.price-stack {
  display: flex;
  align-items: baseline;
  gap: 2px;
}

.price-currency {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--color-primary, #5C4E4E);
}

.price-number {
  font-size: 2.1rem;
  font-weight: 800;
  color: #1E1B18;
  letter-spacing: -0.5px;
}

.price-freq {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-text-muted, #8C7E7E);
  margin-left: 4px;
}

.booking-guarantee-tag {
  font-size: 0.75rem;
  font-weight: 700;
  background: #ECFDF5;
  color: #059669;
  border: 1px solid #A7F3D0;
  padding: 4px 10px;
  border-radius: var(--radius-pill, 50px);
}

.booking-card-divider {
  height: 1px;
  background: var(--color-border, #EDE8E3);
  margin-bottom: 20px;
}

/* Booking Parameters Inputs */
.booking-inputs-block {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 20px;
}

.booking-input-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.input-label {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--color-text-secondary, #5C4E4E);
}

.booking-date-field,
.booking-select-field {
  width: 100%;
  height: 42px;
  padding: 0 12px;
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-md, 10px);
  font-family: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  color: #2A2421;
  outline: none;
  transition: all 0.15s ease;
}

.booking-date-field:focus,
.booking-select-field:focus {
  background: #ffffff;
  border-color: var(--color-primary, #5C4E4E);
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.duration-pill-group {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
}

.dur-pill {
  padding: 8px 4px;
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-text-secondary, #5C4E4E);
  cursor: pointer;
  transition: all 0.15s ease;
}

.dur-pill:hover {
  border-color: var(--color-primary, #5C4E4E);
}

.dur-pill.active {
  background: var(--color-primary, #5C4E4E);
  border-color: var(--color-primary, #5C4E4E);
  color: #ffffff;
  box-shadow: 0 2px 6px rgba(92, 78, 78, 0.25);
}

/* Booking Price Calculation */
.booking-calculation {
  background: #FAF8F5;
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-md, 10px);
  padding: 14px 16px;
  margin-bottom: 22px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.88rem;
  color: var(--color-text-secondary, #5C4E4E);
}

.calc-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.calc-divider {
  height: 1px;
  background: var(--color-border, #EDE8E3);
  margin: 4px 0;
}

.total-line {
  font-weight: 800;
  font-size: 0.95rem;
  color: #1E1B18;
}

.total-amount {
  font-size: 1.15rem;
  color: var(--color-primary, #5C4E4E);
}

/* Actions Stack */
.booking-actions-stack {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 18px;
}

.btn-booking-primary {
  width: 100%;
  height: 48px;
  background: #2A2421;
  color: #ffffff;
  border: none;
  border-radius: var(--radius-md, 10px);
  font-size: 0.98rem;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: 0 4px 14px rgba(42, 36, 33, 0.22), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-booking-primary:hover {
  background: #14100E;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(42, 36, 33, 0.3);
}

.btn-booking-primary:active {
  transform: translateY(0);
}

.btn-booking-pay {
  width: 100%;
  height: 44px;
  background: #FAF8F5;
  color: var(--color-primary, #5C4E4E);
  border: 1px solid var(--color-border, #EDE8E3);
  border-radius: var(--radius-md, 10px);
  font-size: 0.92rem;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.15s ease;
}

.btn-booking-pay:hover {
  background: #F4EDEA;
  border-color: var(--color-primary, #5C4E4E);
}

.btn-booking-roommate {
  width: 100%;
  height: 42px;
  background: transparent;
  color: var(--color-text-secondary, #5C4E4E);
  border: 1px dashed var(--color-border, #EDE8E3);
  border-radius: var(--radius-md, 10px);
  font-size: 0.88rem;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.15s ease;
}

.btn-booking-roommate:hover {
  background: #FAF8F5;
  border-style: solid;
  border-color: var(--color-primary, #5C4E4E);
}

.btn-booking-landlord {
  background: none;
  border: none;
  font-size: 0.84rem;
  font-weight: 700;
  color: var(--color-primary, #5C4E4E);
  cursor: pointer;
  padding: 6px;
  text-align: center;
  transition: color 0.15s;
}

.btn-booking-landlord:hover {
  color: #1E1B18;
  text-decoration: underline;
}

.booking-trust-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-text-muted, #8C7E7E);
  text-align: center;
}

/* ══════════════════════════════════════════════════════════════
   6. LIGHTBOX MODAL
══════════════════════════════════════════════════════════════ */
.lightbox-backdrop {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: rgba(12, 10, 9, 0.94);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.lightbox-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 32px;
  color: #ffffff;
}

.lightbox-counter {
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: rgba(255, 255, 255, 0.8);
}

.lightbox-close-btn {
  background: rgba(255, 255, 255, 0.15);
  border: none;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s ease;
}

.lightbox-close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.lightbox-stage {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  position: relative;
  min-height: 0;
}

.lightbox-image-container {
  max-width: 85vw;
  max-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
}

.lightbox-current-image {
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
  border-radius: 12px;
  animation: scaleUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes scaleUp {
  from { transform: scale(0.96); opacity: 0.8; }
  to { transform: scale(1); opacity: 1; }
}

.lightbox-arrow {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
  flex-shrink: 0;
}

.lightbox-arrow:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.08);
}

.lightbox-thumbs-strip {
  height: 90px;
  padding: 12px 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  overflow-x: auto;
}

.lightbox-thumb-item {
  width: 72px;
  height: 54px;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  opacity: 0.5;
  border: 2px solid transparent;
  transition: all 0.2s ease;
}

.lightbox-thumb-item.active {
  opacity: 1;
  border-color: #ffffff;
  transform: scale(1.05);
}

.lightbox-thumb-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ══════════════════════════════════════════════════════════════
   6. MOBILE FIXED BOTTOM ACTION BAR
══════════════════════════════════════════════════════════════ */
.mobile-sticky-bottom-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background: rgba(255, 255, 255, 0.96);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  border-top: 1px solid var(--color-border, #EDE8E3);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 -4px 16px rgba(42, 36, 33, 0.08);
}

.mobile-bar-price {
  display: flex;
  align-items: baseline;
  gap: 2px;
}

.m-price {
  font-size: 1.4rem;
  font-weight: 800;
  color: #1E1B18;
}

.m-period {
  font-size: 0.85rem;
  font-weight: 600;
  color: #8C7E7E;
}

.m-btn-apply {
  padding: 12px 28px;
  background: #2A2421;
  color: #ffffff;
  border: none;
  border-radius: var(--radius-pill, 50px);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(42, 36, 33, 0.2);
}

/* ══════════════════════════════════════════════════════════════
   7. RESPONSIVE BREAKPOINTS
══════════════════════════════════════════════════════════════ */
.desktop-only { display: grid; }
.mobile-only { display: none; }

@media (max-width: 992px) {
  .marketplace-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }

  .sticky-booking-card {
    position: static;
    max-width: 520px;
    margin: 0 auto;
  }
}

@media (max-width: 768px) {
  .desktop-only { display: none !important; }
  .mobile-only { display: flex !important; }

  .nav-bar-container {
    padding: 10px 16px;
  }

  .breadcrumb-trail {
    display: none;
  }

  .detail-container {
    padding: 16px 16px 90px;
  }

  .property-main-title {
    font-size: 1.6rem;
  }

  .bento-grid {
    grid-template-columns: 1fr;
  }

  .landmarks-grid {
    grid-template-columns: 1fr;
  }

  .reviews-list {
    grid-template-columns: 1fr;
  }

  .contact-channels-grid {
    grid-template-columns: 1fr;
  }

  .rate-summary-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .score-box {
    padding-right: 0;
    border-right: none;
    border-bottom: 1px solid var(--color-border);
    padding-bottom: 12px;
    width: 100%;
    align-items: flex-start;
  }
}
</style>
