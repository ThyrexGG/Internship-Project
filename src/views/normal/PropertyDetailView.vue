<template>
  <div class="property-detail-page">
    <!-- Hero Header Area -->
    <header class="hero-header">
      
      <!-- Listing Top Bar -->
      <div class="listing-top-bar">
        <button class="back-text-btn" type="button" aria-label="Go back" @click="goBack">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg>
          <span class="back-nav-text">Back to listings</span>
        </button>
        <div class="listing-actions">
          <button class="action-link" type="button" @click="handleShare">
             <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8M16 6l-4-4-4 4M12 2v13"/></svg>
             <span>Share</span>
          </button>
          <button class="action-link" type="button" @click="property.liked = !property.liked">
             <svg width="16" height="16" viewBox="0 0 24 24" :fill="property.liked ? '#e74c3c' : 'none'" :stroke="property.liked ? '#e74c3c' : 'currentColor'" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
             <span>{{ property.liked ? 'Saved' : 'Save' }}</span>
          </button>
        </div>
      </div>

      <div class="hero-image-wrapper">
        <!-- Main hero image -->
        <img :src="property.images[activeImage]" alt="Property" class="hero-image" />

        <!-- Carousel Arrows -->
        <button v-if="activeImage > 0" class="hero-arrow left" @click="activeImage--">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <button v-if="activeImage < property.images.length - 1" class="hero-arrow right" @click="activeImage++">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
        </button>

        <!-- Carousel dots -->
        <div class="hero-dots">
          <span v-for="(img, i) in property.images" :key="i" class="cdot" :class="{ active: activeImage === i }" @click="activeImage = i"></span>
        </div>
      </div>
    </header>

    <main class="content-body">
      <!-- Title & Price Section -->
      <section class="title-section">
        <div class="title-left">
          <div class="title-heading-row">
            <h1 class="prop-title">{{ property.name }}</h1>
            <span class="prop-rating-badge">★ {{ property.rating || 4.9 }}</span>
          </div>
          <div class="prop-location">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
            </svg>
            <span>{{ property.location }}</span>
          </div>
        </div>
        <div class="title-right">
          <div class="prop-price">
            <span class="price-val">${{ property.price }}</span>
            <span class="price-period">/ month</span>
          </div>
          <div class="landlord-actions-row">
            <button class="landlord-btn" @click="$router.push(`/landlord-profile/${property.id}?from=${route.query.from || ''}`)">Landlord Profile</button>
            <button class="landlord-chat-btn" @click="router.push({ path: '/chat', query: { landlordId: `landlord_${property.id}`, contact: property.name + ' Host' } })">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
              </svg>
              Chat Host
            </button>
          </div>
        </div>

        <!-- Integrated Booking Action Buttons -->
        <div class="detail-booking-actions">
          <button class="action-btn black" @click="router.push(`/property/${propertyId}/apply`)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" /><circle cx="12" cy="7" r="4" />
            </svg>
            Rent House
          </button>
          <button class="action-btn pay" @click="router.push(`/property/${property.id}/payment`)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect>
              <line x1="1" y1="10" x2="23" y2="10"></line>
            </svg>
            Pay Now
          </button>
          <button class="action-btn outline" @click="$router.push(`/property/${property.id}/roommate`)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" /><circle cx="9" cy="7" r="4" />
              <path d="M23 21v-2a4 4 0 00-3-3.87" /><path d="M16 3.13a4 4 0 010 7.75" />
            </svg>
            Find Roommate
          </button>
        </div>
      </section>

      <!-- Property Details (Feature Cards) -->
      <section class="detail-icons">
        <h2 class="section-title">Property Details</h2>
        <div class="icons-row">
          <div class="d-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            <span class="d-val">{{ property.pax || '2/4 pax' }}</span>
            <span class="d-lbl">Occupancy</span>
          </div>
          <div class="d-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            <span class="d-val">{{ property.beds }} Beds</span>
            <span class="d-lbl">Bedrooms</span>
          </div>
          <div class="d-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
            <span class="d-val">{{ property.baths }} Baths</span>
            <span class="d-lbl">Bathrooms</span>
          </div>
          <div class="d-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18M15 3v18"/></svg>
            <span class="d-val">1 Interior</span>
            <span class="d-lbl">Furnished</span>
          </div>
          <div class="d-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
            <span class="d-val">{{ property.sqft }} m²</span>
            <span class="d-lbl">Floor Area</span>
          </div>
        </div>
      </section>

      <!-- Photos Section -->
      <section class="photos-section">
        <h2 class="section-title">Photos</h2>
        <div class="photos-carousel-wrapper">
          <button class="gallery-arrow left" @click="scrollGallery(-1)">
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <div class="photos-grid" ref="galleryGrid">
            <div v-for="(img, idx) in property.images" :key="idx" class="photo-item">
              <img :src="img" alt="Gallery Photo" />
            </div>
          </div>
          <button class="gallery-arrow right" @click="scrollGallery(1)">
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </div>
      </section>

      <!-- Description Section -->
      <section class="description-section">
        <h2 class="section-title">Description</h2>
        <p class="desc-text">
          {{ property.name }} is a modern and comfortable apartment designed to provide a premium living experience. The condo features high-quality furnishings and premium appliances to ensure convenience and comfort for residents. With its stylish interior, spacious layout, and well-equipped facilities, {{ property.name }} offers the perfect environment for students and professionals who are looking for a safe and relaxing place to stay.
        </p>
      </section>

      <!-- Recently Rent By -->
      <section class="renters-section">
        <h2 class="section-title">Recently Rent By</h2>
        <div class="renter-list">
          <div class="renter-card" v-for="(renter, r) in renters" :key="r">
            <img :src="renter.avatar" :alt="renter.name" class="renter-avatar" />
            <span class="renter-name">{{ renter.name }}</span>
            <button class="view-profile-btn">View profile <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></button>
          </div>
        </div>
      </section>

      <!-- Rate & Reviews -->
      <section class="rate-section">
        <div class="rate-header">
          <div class="rate-left">
            <h2 class="section-title">Rate</h2>
            <div class="stars">
              <svg v-for="s in 5" :key="s" width="16" height="16" viewBox="0 0 24 24" fill="#111" stroke="#111" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
          </div>
          <div class="rate-right">
            <span class="reviews-label">Reviews</span>
            <span class="reviews-count">1000+</span>
          </div>
        </div>
        
        <div class="reviews-list">
          <div class="review-card" v-for="(review, rv) in reviews" :key="rv">
            <div class="review-header">
              <div class="reviewer-avatar">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#ccc"><circle cx="12" cy="8" r="4"/><path d="M12 14c-4.42 0-8 3.58-8 8h16c0-4.42-3.58-8-8-8z"/></svg>
              </div>
              <div class="reviewer-info">
                <span class="reviewer-name">{{ review.name }}</span>
                <span class="review-date">{{ review.date }}</span>
              </div>
            </div>
            <div class="review-stars">
              <svg v-for="s in 5" :key="s" width="12" height="12" viewBox="0 0 24 24" fill="#111" stroke="#111" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <p class="review-text">{{ review.text }}</p>
          </div>
        </div>
        <button class="show-more-btn">Show more <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></button>
      </section>

      <!-- Contact Landlord -->
      <section class="contact-section">
        <h2 class="section-title">Contact Landlord</h2>
        <div class="contact-list">
          <div class="contact-item">
            <div class="c-icon fb"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff" stroke="none"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></div>
            <span>{{ property.contactName || (property.name + ' Cambodia') }}</span>
          </div>
          <div class="contact-item">
            <div class="c-icon tg"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff" stroke="none"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></div>
            <span>{{ property.contactSocial || ('@' + property.name.toLowerCase().replace(/\s+/g, '_') + '_cambodia') }}</span>
          </div>
          <div class="contact-item">
            <div class="c-icon ph"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff" stroke="none"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg></div>
            <span>{{ property.contactPhone || '081 743 949 / 077 843 984' }}</span>
          </div>
        </div>
      </section>
      
      <div class="spacer"></div>
      <GlobalFooter />
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
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

const activeImage = ref(0)
const galleryGrid = ref(null)

const scrollGallery = (dir) => {
  if (galleryGrid.value) {
    galleryGrid.value.scrollBy({ left: dir * 280, behavior: 'smooth' })
  }
}

const goBack = () => {
  router.push('/home')
}

const handleShare = () => {
  if (navigator.share) {
    navigator.share({
      title: property.value?.name || 'HomeSweet Property',
      url: window.location.href
    }).catch(() => {})
  } else {
    navigator.clipboard?.writeText(window.location.href)
    alert('Property link copied to clipboard!')
  }
}



// Mock data based on design
const renters = [
  { name: 'Yim Vatey', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&q=80' },
  { name: 'Muy Leng', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&q=80' },
  { name: 'Neav Sveita', avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80' },
]

const reviews = [
  { name: 'LaDawn Hunter', date: '1 day ago', text: 'Great experience staying here. The environment is quiet, the rooms are comfortable, and the management is friendly and helpful. A perfect place for students and young professionals.' },
  { name: 'Eric Summers', date: '1 day ago', text: 'Great experience staying here. The environment is quiet, the rooms are comfortable, and the management is friendly and helpful. A perfect place for students and young professionals.' }
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.property-detail-page {
  font-family: 'DM Sans', sans-serif;
  background: #fff;
  height: 100vh;
  overflow-y: auto;
  color: #111;
}

/* ── HERO ── */
.hero-header {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 40px 0;
}

/* ── LISTING TOP BAR ── */
.listing-top-bar {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 20px;
}
.back-text-btn {
  background: #ffffff;
  border: 1px solid #ede8e3;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 30px;
  color: #2b2723;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: all 0.2s ease;
}
.back-text-btn:hover { 
  background: #fdfbf9;
  border-color: #5C4E4E;
}
.back-nav-text {
  font-size: 0.88rem;
  font-weight: 600;
}
.listing-actions {
  display: flex; gap: 8px;
}
.action-link {
  display: flex; align-items: center; gap: 8px;
  background: #ffffff;
  border: 1px solid #ede8e3;
  font-size: 0.88rem;
  font-weight: 600;
  color: #2b2723;
  cursor: pointer;
  padding: 8px 16px;
  border-radius: 30px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: all 0.2s ease;
}
.action-link:hover {
  background: #fdfbf9;
  border-color: #5C4E4E;
}

.hero-image-wrapper {
  position: relative;
  width: 100%;
  height: 52vh;
  max-height: 480px;
  background: #f5f5f5;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}
.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px; height: 40px;
  border-radius: 50%;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(4px);
  border: none;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; z-index: 10;
  color: #111;
  transition: all 0.2s;
}
.hero-arrow:hover { background: rgba(255,255,255,1); transform: translateY(-50%) scale(1.05); }
.hero-arrow.left { left: 20px; }
.hero-arrow.right { right: 20px; }
.hero-dots {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex; gap: 6px;
  z-index: 10;
}
.cdot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,0.6);
  cursor: pointer;
  transition: all 0.2s;
}
.cdot.active { background: #fff; width: 16px; border-radius: 4px; }

/* ── MAIN CONTENT ── */
.content-body {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 40px 80px;
  width: 100%;
}
.section-title {
  font-size: 1.45rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: #1e1b18;
  letter-spacing: -0.3px;
}

/* ── TITLE & PRICE ── */
.title-section {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
  align-items: start;
  margin-bottom: 36px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ede8e3;
}
.title-heading-row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}
.prop-title {
  font-size: 2.2rem;
  font-weight: 800;
  color: #1e1b18;
  margin: 0;
  letter-spacing: -0.5px;
  line-height: 1.15;
}
.prop-rating-badge {
  background: #fffbeb;
  color: #b45309;
  border: 1px solid #fde68a;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.86rem;
  font-weight: 700;
}
.prop-location {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.96rem;
  font-weight: 500;
  color: #64748b;
}
.title-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
}
.prop-price { display: flex; align-items: baseline; gap: 4px; }
.price-val { font-size: 2rem; font-weight: 800; color: #1e1b18; }
.price-period { font-size: 0.9rem; font-weight: 600; color: #78716c; }

.landlord-actions-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.landlord-btn {
  background: #5C4E4E; color: #fff;
  border: none; border-radius: 8px;
  padding: 10px 18px; font-size: 0.9rem; font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;
}

.landlord-btn:hover {
  background: #473B3B;
}

.landlord-chat-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  color: #5C4E4E;
  border: 1.5px solid #5C4E4E;
  border-radius: 8px;
  padding: 9px 16px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.landlord-chat-btn:hover {
  background: #F2EDE9;
}

/* Integrated Booking Actions Row */
.detail-booking-actions {
  grid-column: 1 / -1;
  display: flex;
  gap: 12px;
  margin-top: 10px;
  flex-wrap: wrap;
}
.detail-booking-actions .action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s ease;
}
.detail-booking-actions .action-btn.black {
  background: #5C4E4E;
  color: #ffffff;
  border: 1.5px solid #5C4E4E;
  box-shadow: 0 4px 12px rgba(92, 78, 78, 0.22);
}
.detail-booking-actions .action-btn.black:hover {
  background: #473B3B;
  transform: translateY(-1px);
}
.detail-booking-actions .action-btn.pay {
  background: #2563eb;
  color: #ffffff;
  border: 1.5px solid #2563eb;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.22);
}
.detail-booking-actions .action-btn.pay:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
}
.detail-booking-actions .action-btn.outline {
  background: #ffffff;
  color: #5C4E4E;
  border: 1.5px solid #5C4E4E;
}
.detail-booking-actions .action-btn.outline:hover {
  background: #F2EDE9;
  transform: translateY(-1px);
}

/* ── ICONS DETAIL (FEATURE CARDS) ── */
.detail-icons {
  margin-bottom: 36px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ede8e3;
}
.icons-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 14px;
}
.d-icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 18px 12px;
  background: #faf8f5;
  border: 1px solid #ede8e3;
  border-radius: 12px;
  transition: all 0.2s ease;
  color: #5C4E4E;
}
.d-icon:hover {
  transform: translateY(-2px);
  border-color: #5C4E4E;
  background: #ffffff;
  box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}
.d-val {
  font-size: 0.95rem;
  font-weight: 700;
  color: #1e1b18;
}
.d-lbl {
  font-size: 0.76rem;
  font-weight: 500;
  color: #78716c;
}

/* ── PHOTOS ── */
.photos-section {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
}
.photos-carousel-wrapper {
  position: relative;
  display: flex; align-items: center;
}
.photos-grid {
  display: flex; gap: 16px; overflow-x: auto;
  padding-bottom: 8px; scrollbar-width: none;
  scroll-behavior: smooth;
  width: 100%;
}
.photos-grid::-webkit-scrollbar { display: none; }
.photo-item {
  width: 260px; height: 320px;
  border-radius: 16px; overflow: hidden; flex-shrink: 0;
}
.photo-item img { width: 100%; height: 100%; object-fit: cover; }
.gallery-arrow {
  position: absolute;
  top: 50%; transform: translateY(-50%);
  width: 40px; height: 40px; border-radius: 50%;
  background: #fff; border: 1px solid #eee;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; z-index: 10; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.gallery-arrow.left { left: -20px; }
.gallery-arrow.right { right: -20px; }

/* ── DESCRIPTION ── */
.description-section {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
}
.desc-text {
  font-size: 1rem; line-height: 1.6; color: #222;
  font-weight: 400;
}

/* ── RECENTLY RENT BY ── */
.renters-section {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
}
.renter-list { display: flex; flex-direction: column; gap: 16px; }
.renter-card {
  display: flex; align-items: center; padding: 12px 0;
  border: none; border-radius: 0;
}
.renter-avatar { width: 48px; height: 48px; border-radius: 50%; object-fit: cover; margin-right: 16px; }
.renter-name { font-size: 1rem; font-weight: 600; flex: 1; }
.view-profile-btn {
  background: none; border: none;
  font-size: 0.9rem; font-weight: 500; color: #222; text-decoration: underline;
  display: flex; align-items: center; gap: 4px; cursor: pointer;
}

/* ── RATE & REVIEWS ── */
.rate-section {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
}
.rate-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.rate-left .section-title { margin-bottom: 4px; }
.stars { display: flex; gap: 2px; }
.rate-right { display: flex; flex-direction: column; align-items: flex-end; }
.reviews-label { font-size: 0.8rem; color: #888; font-weight: 500; }
.reviews-count { font-size: 0.9rem; font-weight: 500; }

.reviews-list { display: flex; flex-direction: column; gap: 16px; margin-bottom: 16px; }
.review-card {
  padding: 16px; border: 1px solid #eaeaea; border-radius: 16px;
}
.review-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.reviewer-info { display: flex; flex-direction: column; }
.reviewer-name { font-size: 0.9rem; font-weight: 600; }
.review-date { font-size: 0.7rem; color: #999; font-weight: 500; }
.review-stars { margin-bottom: 8px; display: flex; gap: 2px; }
.review-text { font-size: 0.85rem; line-height: 1.5; color: #333; font-weight: 500; }

.show-more-btn {
  background: none; border: none; font-size: 0.9rem; color: #888; font-weight: 500;
  display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 0;
}

/* ── CONTACT ── */
.contact-section {
  margin-bottom: 32px;
  padding-bottom: 32px;
}
.contact-list { display: flex; flex-direction: column; gap: 16px; }
.contact-item { display: flex; align-items: center; gap: 16px; font-size: 1rem; font-weight: 500; color: #222; }
.c-icon {
  width: 32px; height: 32px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}
.c-icon.fb { background: #5C4E4E; }
.c-icon.tg { background: #5C4E4E; }
.c-icon.ph { background: #5C4E4E; }

.spacer { height: 60px; }

/* ── RESPONSIVE ── */
@media (max-width: 768px) {
  .property-detail-page {
    height: 100dvh;
  }

  .hero-header {
    padding: 16px 20px 0;
  }

  .listing-top-bar {
    gap: 12px;
    margin-bottom: 16px;
  }

  .listing-title-wrap {
    gap: 8px;
    min-width: 0;
  }

  .back-text-btn {
    width: 36px;
    height: 36px;
    margin-left: -8px;
    flex-shrink: 0;
  }

  .listing-title {
    font-size: 1.2rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .listing-actions {
    gap: 2px;
    flex-shrink: 0;
  }

  .action-link {
    padding: 8px;
    font-size: 0;
    gap: 0;
  }

  .action-link svg {
    width: 18px;
    height: 18px;
  }

  .action-link u {
    display: none;
  }

  .hero-image-wrapper {
    height: min(54vh, 430px);
    min-height: 300px;
    border-radius: 14px;
    margin-bottom: 28px;
  }

  .hero-arrow {
    width: 34px;
    height: 34px;
  }

  .hero-arrow.left { left: 12px; }
  .hero-arrow.right { right: 12px; }
  .hero-dots { bottom: 68px; }

  .floating-actions {
    left: 12px;
    right: 12px;
    bottom: 12px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 0;
    background: transparent;
    border-radius: 0;
  }

  .action-btn {
    justify-content: center;
    padding: 11px 10px;
    min-width: 0;
    font-size: 0.78rem;
    border-radius: 10px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  }

  .content-body {
    padding: 22px 20px 72px;
  }

  .section-title {
    font-size: 1.18rem;
    margin-bottom: 16px;
  }

  .title-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 24px;
    padding-bottom: 24px;
  }

  .title-right {
    width: 100%;
    align-items: flex-start;
  }

  .prop-title {
    font-size: 1.7rem;
  }

  .prop-location {
    align-items: flex-start;
    font-size: 0.86rem;
    line-height: 1.35;
  }

  .price-val {
    font-size: 1.55rem;
  }

  .landlord-btn {
    width: 100%;
    padding: 12px 14px;
  }

  .detail-icons,
  .photos-section,
  .description-section,
  .renters-section,
  .rate-section,
  .contact-section {
    margin-bottom: 24px;
    padding-bottom: 24px;
  }

  .icons-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 10px !important;
  }

  .d-icon {
    width: 100%;
    height: auto;
    min-height: 72px;
    min-width: 0;
    font-size: 0.72rem;
    padding: 12px 8px;
  }

  .d-icon .d-val {
    font-size: 0.88rem;
  }

  .d-icon .d-lbl {
    font-size: 0.72rem;
  }

  .detail-booking-actions {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
  }

  .detail-booking-actions .action-btn {
    width: 100%;
    height: 48px;
    font-size: 0.95rem;
    justify-content: center;
  }

  .landlord-actions-row {
    width: 100%;
    display: flex;
    gap: 10px;
    margin-top: 6px;
  }

  .landlord-actions-row .landlord-btn,
  .landlord-actions-row .landlord-chat-btn {
    flex: 1;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.88rem;
    padding: 0 10px;
  }

  .photos-carousel-wrapper {
    margin: 0 -20px;
    padding-left: 20px;
  }

  .photos-grid {
    gap: 12px;
    padding-right: 20px;
  }

  .photo-item {
    width: min(72vw, 260px);
    height: 230px;
    border-radius: 12px;
  }

  .gallery-arrow {
    display: none;
  }

  .desc-text {
    font-size: 0.92rem;
    line-height: 1.55;
  }

  .renter-card {
    gap: 12px;
    padding: 10px 0;
  }

  .renter-avatar {
    width: 42px;
    height: 42px;
    margin-right: 0;
  }

  .renter-name {
    min-width: 0;
    font-size: 0.92rem;
  }

  .view-profile-btn {
    flex-shrink: 0;
    font-size: 0.78rem;
  }

  .rate-header {
    align-items: flex-start;
    gap: 12px;
  }

  .review-card {
    padding: 14px;
    border-radius: 12px;
  }

  .contact-item {
    align-items: flex-start;
    gap: 12px;
    font-size: 0.9rem;
    line-height: 1.35;
  }

  .contact-item span {
    min-width: 0;
    overflow-wrap: anywhere;
  }

  .spacer {
    height: 20px;
  }
}

@media (max-width: 390px) {
  .hero-header {
    padding-left: 14px;
    padding-right: 14px;
  }

  .content-body {
    padding-left: 14px;
    padding-right: 14px;
  }

  .hero-image-wrapper {
    min-height: 280px;
  }

  .floating-actions {
    left: 10px;
    right: 10px;
  }

  .action-btn {
    font-size: 0.72rem;
  }

  .action-btn svg {
    display: none;
  }

  .icons-row {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .photos-carousel-wrapper {
    margin-left: -14px;
    margin-right: -14px;
    padding-left: 14px;
  }

  .photos-grid {
    padding-right: 14px;
  }

  .photo-item {
    width: 78vw;
  }

  .renter-card {
    display: grid;
    grid-template-columns: 42px minmax(0, 1fr);
  }

  .view-profile-btn {
    grid-column: 2;
    justify-self: start;
  }
}
</style>
