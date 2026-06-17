<template>
  <div class="property-detail-page">
    <!-- Hero Header Area -->
    <header class="hero-header">
      
      <!-- Listing Top Bar -->
      <div class="listing-top-bar">
        <div class="listing-title-wrap">
          <button class="back-text-btn" type="button" aria-label="Go back" @click="goBack">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <h1 class="listing-title">{{ property.name }}</h1>
        </div>
        <div class="listing-actions">
          <button class="action-link">
             <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 002 2h12a2 2 0 002-2v-8M16 6l-4-4-4 4M12 2v13"/></svg>
             <u>Share</u>
          </button>
          <button class="action-link" @click="property.liked = !property.liked">
             <svg width="16" height="16" viewBox="0 0 24 24" :fill="property.liked ? '#e74c3c' : 'none'" :stroke="property.liked ? '#e74c3c' : 'currentColor'" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
             <u>{{ property.liked ? 'Saved' : 'Save' }}</u>
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

        <!-- Floating Buttons Panel -->
        <div class="floating-actions">
          <button class="action-btn black">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" /><circle cx="12" cy="7" r="4" />
            </svg>
            Rent House
          </button>
          <button class="action-btn outline" @click="$router.push(`/property/${property.id}/roommate`)">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" /><circle cx="9" cy="7" r="4" />
              <path d="M23 21v-2a4 4 0 00-3-3.87" /><path d="M16 3.13a4 4 0 010 7.75" />
            </svg>
            Find Roommate
          </button>
        </div>
      </div>
    </header>

    <main class="content-body">
      <!-- Title & Price Section -->
      <section class="title-section">
        <div class="title-left">
          <h1 class="prop-title">{{ property.name }}</h1>
          <div class="prop-location">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
            </svg>
            <span>{{ property.location }}</span>
          </div>
        </div>
        <div class="title-right">
          <div class="prop-price">
            <span class="price-val">${{ property.price }}</span>
            <span class="price-period">/monthly</span>
          </div>
          <button class="landlord-btn" @click="$router.push(`/landlord-profile/${property.id}?from=${route.query.from || ''}`)">Find out more Landlord Profile</button>
        </div>
      </section>

      <!-- Properties Detail (Icons) -->
      <section class="detail-icons">
        <h2 class="section-title">Properties Detail</h2>
        <div class="icons-row">
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg><span>{{ property.pax || '2/4 pax' }}</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg><span>{{ property.beds }} bed</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg><span>{{ property.baths }} bath</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18M15 3v18"/></svg><span>1 int</span></div>
          <div class="d-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg><span>{{ property.sqft }}m</span></div>
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
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { properties } from '../../store.js'

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
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/')
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
  margin-bottom: 24px;
}
.listing-title-wrap {
  display: flex; align-items: center; gap: 16px;
}
.back-text-btn {
  background: none; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  width: 40px; height: 40px; border-radius: 50%; transition: background 0.2s;
  margin-left: -10px; /* Aligns visually with left edge */
}
.back-text-btn:hover { background: #f5f5f5; }
.listing-title {
  font-size: 1.6rem; font-weight: 600; color: #222; margin: 0;
}
.listing-actions {
  display: flex; gap: 8px;
}
.action-link {
  display: flex; align-items: center; gap: 8px;
  background: none; border: none; font-size: 0.9rem; font-weight: 500; color: #222;
  cursor: pointer; padding: 8px 12px; border-radius: 8px; transition: background 0.2s;
}
.action-link:hover { background: #f5f5f5; }

.hero-image-wrapper {
  position: relative;
  width: 100%;
  height: 50vh;
  max-height: 480px;
  background: #f5f5f5;
  border-radius: 12px;
  overflow: hidden;
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
  background: rgba(255,255,255,0.7);
  border: none;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; z-index: 10;
  color: #111;
  transition: background 0.2s;
}
.hero-arrow:hover { background: rgba(255,255,255,0.95); }
.hero-arrow.left { left: 24px; }
.hero-arrow.right { right: 24px; }
.hero-dots {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex; gap: 6px;
  z-index: 10;
}
.cdot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  cursor: pointer;
}
.cdot.active { background: #fff; width: 14px; border-radius: 4px; }

.floating-actions {
  position: absolute;
  bottom: 0;
  right: 0;
  display: flex; gap: 12px;
  background: #fff;
  padding: 16px 0 0 16px; /* Added padding to the top and left */
  border-top-left-radius: 24px;
  z-index: 20;
}
.action-btn {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 20px;
  font-size: 0.9rem; font-weight: 500;
  border-radius: 8px; cursor: pointer;
  font-family: inherit;
}
.action-btn.black {
  background: #111; color: #fff; border: 1px solid #111;
}
.action-btn.outline {
  background: #fff; color: #111; border: 1px solid #e0e0e0;
}

/* ── MAIN CONTENT ── */
.content-body {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 40px 60px;
  width: 100%;
}
.section-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 24px;
  color: #222;
}

/* ── TITLE & PRICE ── */
.title-section {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
  gap: 20px;
  flex-wrap: wrap;
}
.prop-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 8px;
  line-height: 1.2;
}
.prop-location {
  display: flex; align-items: center; gap: 6px;
  font-size: 0.95rem; font-weight: 500; color: #222;
}
.title-right {
  display: flex; flex-direction: column; align-items: flex-end; gap: 12px;
}
.prop-price { display: flex; align-items: baseline; gap: 4px; }
.price-val { font-size: 1.8rem; font-weight: 700; }
.price-period { font-size: 0.85rem; font-weight: 600; color: #555; }

.landlord-btn {
  background: #222; color: #fff;
  border: none; border-radius: 8px;
  padding: 10px 18px; font-size: 0.9rem; font-weight: 600;
  cursor: pointer;
}

/* ── ICONS DETAIL ── */
.detail-icons {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #ebebeb;
}
.icons-row { display: flex; gap: 12px; flex-wrap: wrap; }
.d-icon {
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;
  width: 56px; height: 56px;
  border: 1px solid #ebebeb; border-radius: 8px;
  font-size: 0.65rem; font-weight: 600; color: #444;
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
.c-icon.fb { background: #111; }
.c-icon.tg { background: #111; }
.c-icon.ph { background: #111; }

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
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 8px;
  }

  .d-icon {
    width: 100%;
    height: 58px;
    min-width: 0;
    font-size: 0.58rem;
    padding: 6px 2px;
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
