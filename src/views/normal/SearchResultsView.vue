<template>
  <div class="search-results-page">
    <!-- Top Nav Header -->
    <header class="top-nav">
      <button class="logo" type="button" @click="$router.push('/home')" aria-label="Go to Home">
        <div class="logo-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 18 L16 18" />
            <path d="M4 18 L4 12 L9 7 L16 14" />
            <path d="M12 18 L12 4 L16 4 L16 18 Z" />
            <path d="M12 14 L16 14" />
          </svg>
        </div>
        <span class="logo-text">HomeSweet</span>
      </button>

      <div class="nav-right">
        <span class="host-text" @click="$router.push('/home')">Become a host</span>
        <div class="profile-menu" @click="$router.push('/home')" aria-label="Go to Profile">
          <div class="avatar">
            <img :src="userProfile.avatar || defaultAvatar" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="User" />
          </div>
        </div>
      </div>
    </header>

    <!-- Content Workspace -->
    <div class="search-workspace">
      <!-- Left: Listings Column -->
      <div class="results-column" v-show="!showMapView || isDesktop">
        
        <!-- Filter Bar -->
        <div class="filter-bar">
          <!-- Price Filter Pill -->
          <div class="filter-dropdown-wrapper">
            <button class="filter-pill-btn" :class="{ active: isPriceFilterActive || activeDropdown === 'price' }" @click.stop="toggleDropdown('price')">
              <span>Price</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <div class="filter-popover" v-if="activeDropdown === 'price'" @click.stop>
              <div class="popover-title">Price range</div>
              <div class="popover-price-inputs">
                <div class="price-input-box">
                  <span class="popover-currency">$</span>
                  <input type="number" v-model.number="filterState.priceMin" min="0" placeholder="Min" />
                </div>
                <span class="input-dash">-</span>
                <div class="price-input-box">
                  <span class="popover-currency">$</span>
                  <input type="number" v-model.number="filterState.priceMax" placeholder="Max" />
                </div>
              </div>
              <div class="popover-footer">
                <button class="popover-clear" @click="resetPriceFilter">Clear</button>
                <button class="popover-apply" @click="activeDropdown = null">Apply</button>
              </div>
            </div>
          </div>

          <!-- Rate Filter Pill -->
          <div class="filter-dropdown-wrapper">
            <button class="filter-pill-btn" :class="{ active: filterState.rate !== 'Any' || activeDropdown === 'rate' }" @click.stop="toggleDropdown('rate')">
              <span>Rate</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <div class="filter-popover" v-if="activeDropdown === 'rate'" @click.stop>
              <div class="popover-title">Minimum rating</div>
              <div class="popover-options">
                <label class="option-label" v-for="r in ['Any', '4.5+', '4.0+', '3.5+']" :key="r">
                  <input type="radio" :value="r" v-model="filterState.rate" />
                  <span>{{ r }}</span>
                </label>
              </div>
              <div class="popover-footer">
                <button class="popover-clear" @click="filterState.rate = 'Any'">Reset</button>
                <button class="popover-apply" @click="activeDropdown = null">Apply</button>
              </div>
            </div>
          </div>

          <!-- Period Filter Pill -->
          <div class="filter-dropdown-wrapper">
            <button class="filter-pill-btn" :class="{ active: filterState.period !== 'Any' || activeDropdown === 'period' }" @click.stop="toggleDropdown('period')">
              <span>Period</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <div class="filter-popover" v-if="activeDropdown === 'period'" @click.stop>
              <div class="popover-title">Lease duration</div>
              <div class="popover-options">
                <label class="option-label" v-for="p in ['Any', 'Short-term', 'Long-term']" :key="p">
                  <input type="radio" :value="p" v-model="filterState.period" />
                  <span>{{ p }}</span>
                </label>
              </div>
              <div class="popover-footer">
                <button class="popover-clear" @click="filterState.period = 'Any'">Reset</button>
                <button class="popover-apply" @click="activeDropdown = null">Apply</button>
              </div>
            </div>
          </div>

          <!-- Conveniences Filter Pill -->
          <div class="filter-dropdown-wrapper">
            <button class="filter-pill-btn" :class="{ active: filterState.amenities.length > 0 || activeDropdown === 'conveniences' }" @click.stop="toggleDropdown('conveniences')">
              <span>Conveniences</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <div class="filter-popover wide" v-if="activeDropdown === 'conveniences'" @click.stop>
              <div class="popover-title">Conveniences</div>
              <div class="popover-checkbox-grid">
                <label class="popover-checkbox" v-for="amenity in availableAmenities" :key="amenity.id">
                  <input type="checkbox" :value="amenity.id" v-model="filterState.amenities" />
                  <span>{{ amenity.label }}</span>
                </label>
              </div>
              <div class="popover-footer">
                <button class="popover-clear" @click="filterState.amenities = []">Clear</button>
                <button class="popover-apply" @click="activeDropdown = null">Apply</button>
              </div>
            </div>
          </div>

          <!-- More Filter Pill -->
          <div class="filter-dropdown-wrapper">
            <button class="filter-pill-btn" :class="{ active: isMoreFilterActive || activeDropdown === 'more' }" @click.stop="toggleDropdown('more')">
              <span>More</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <div class="filter-popover counter-popover" v-if="activeDropdown === 'more'" @click.stop>
              <div class="popover-title">More filters</div>
              <div class="popover-counters">
                <!-- Bedrooms -->
                <div class="popover-counter-row">
                  <span>Bedrooms</span>
                  <div class="popover-counter-controls">
                    <button class="counter-btn" :disabled="filterState.bedrooms === 0" @click="filterState.bedrooms > 0 ? filterState.bedrooms-- : null">-</button>
                    <span class="counter-val">{{ filterState.bedrooms === 0 ? 'Any' : filterState.bedrooms }}</span>
                    <button class="counter-btn" @click="filterState.bedrooms++">+</button>
                  </div>
                </div>
                <!-- Beds -->
                <div class="popover-counter-row">
                  <span>Beds</span>
                  <div class="popover-counter-controls">
                    <button class="counter-btn" :disabled="filterState.beds === 0" @click="filterState.beds > 0 ? filterState.beds-- : null">-</button>
                    <span class="counter-val">{{ filterState.beds === 0 ? 'Any' : filterState.beds }}</span>
                    <button class="counter-btn" @click="filterState.beds++">+</button>
                  </div>
                </div>
                <!-- Bathrooms -->
                <div class="popover-counter-row">
                  <span>Bathrooms</span>
                  <div class="popover-counter-controls">
                    <button class="counter-btn" :disabled="filterState.bathrooms === 0" @click="filterState.bathrooms > 0 ? filterState.bathrooms-- : null">-</button>
                    <span class="counter-val">{{ filterState.bathrooms === 0 ? 'Any' : filterState.bathrooms }}</span>
                    <button class="counter-btn" @click="filterState.bathrooms++">+</button>
                  </div>
                </div>
              </div>
              <div class="popover-footer">
                <button class="popover-clear" @click="resetMoreFilters">Clear</button>
                <button class="popover-apply" @click="activeDropdown = null">Apply</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Headline Results -->
        <div class="stats-header">
          <h2 class="stats-title">{{ filteredProperties.length }} Result founds in {{ searchQuery || 'Phnom Penh' }}</h2>
          <p class="stats-subtitle">Find and book a comfortable home for your living.</p>
        </div>

        <!-- Listings Grid (2 columns) -->
        <div class="listings-grid">
          <div v-for="property in filteredProperties" :key="property.id" class="search-property-card" @click="handleCardClick($event, property.id)">
            <!-- Carousel -->
            <div 
              class="card-carousel"
              @touchstart="handleTouchStart"
              @touchmove="handleTouchMove"
              @touchend="handleTouchEnd($event, property)"
            >
              <div class="carousel-track" :style="{ transform: `translateX(-${property.activeSlide * 100}%)` }">
                <img
                  v-for="(img, i) in property.images" :key="i"
                  :src="img" :alt="property.name"
                  class="carousel-img" draggable="false"
                />
              </div>
              <button class="heart-btn" :class="{ liked: property.liked }" @click.stop="property.liked = !property.liked">
                <svg width="13" height="13" viewBox="0 0 24 24" :fill="property.liked ? '#111' : 'none'" :stroke="property.liked ? '#111' : '#555'" stroke-width="2">
                  <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z" />
                </svg>
              </button>
              <div class="carousel-dots">
                <span v-for="(_, i) in property.images" :key="i" class="cdot" :class="{ active: property.activeSlide === i }" @click.stop="property.activeSlide = i" />
              </div>
              <button v-if="property.activeSlide > 0" class="carousel-arrow left" @click.stop="property.activeSlide--">‹</button>
              <button v-if="property.activeSlide < property.images.length - 1" class="carousel-arrow right" @click.stop="property.activeSlide++">›</button>
            </div>

            <!-- Card Info -->
            <div class="card-info">
              <div class="card-title-row">
                <span class="card-name">{{ property.name }}</span>
                <span class="card-price">${{ property.price }}</span>
              </div>
              <div class="card-location">
                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
                </svg>
                <span>{{ property.location }}</span>
              </div>
              <div class="card-meta">
                <div class="meta-tags">
                  <span class="tag">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
                    {{ property.beds }}
                  </span>
                  <span class="tag">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                    {{ property.baths }}
                  </span>
                  <span class="tag">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
                    {{ property.sqft }}
                  </span>
                </div>
                <span class="match">{{ property.match }}%</span>
              </div>
            </div>
          </div>
          
          <div v-if="filteredProperties.length === 0" class="empty-results">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5">
              <circle cx="12" cy="12" r="10"/><path d="M8 15h8M9 9h.01M15 9h.01"/>
            </svg>
            <p>No properties match your filter preferences.</p>
            <button class="btn-clear-all" @click="clearAllFilters">Clear all filters</button>
          </div>
        </div>
        <GlobalFooter />
      </div>

      <!-- Right: Map Column -->
      <div class="map-column" v-show="showMapView || isDesktop">
        <!-- Google Map Container -->
        <div class="map-outer-wrapper">
          <!-- Search input box aligned over the map on top right -->
          <div class="map-search-container">
            <div class="map-search-box">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
              </svg>
              <input ref="mapSearchInput" v-model="searchQuery" type="text" placeholder="Search neighborhood or city..." />
            </div>
            
            <div class="map-amenities-toolbar" v-if="isMapLoaded">
              <button class="amenity-btn" @click="toggleTraffic" :class="{ 'active-btn': isTrafficEnabled }">🚦 Traffic</button>
              <button class="amenity-btn" @click="searchNearby('transit_station', 'Transit')" :class="{ 'active-btn': activeAmenities['transit_station'] }">🚇 Transit</button>
              <button class="amenity-btn" @click="searchNearby('supermarket', 'Groceries')" :class="{ 'active-btn': activeAmenities['supermarket'] }">🛒 Groceries</button>
              <button class="amenity-btn" @click="searchNearby('school', 'Schools')" :class="{ 'active-btn': activeAmenities['school'] }">🎓 Schools</button>
              <button class="amenity-btn clear-btn" @click="clearAmenities()" v-show="activeAmenities['transit_station'] || activeAmenities['supermarket'] || activeAmenities['school']">Clear</button>
            </div>
          </div>

          <button class="locate-me-btn" @click="panToUserLocation" title="Locate Me" v-if="isMapLoaded">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/>
            </svg>
          </button>

          <div ref="mapContainer" class="map-element"></div>
          <div v-if="!isMapLoaded" class="map-loading-overlay">
            <span>{{ mapMessage }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Mobile toggle Map/List float button -->
    <button class="mobile-toggle-btn" @click="showMapView = !showMapView" v-if="!isDesktop">
      <span v-if="showMapView">
        List
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: 4px;">
          <line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>
        </svg>
      </span>
      <span v-else>
        Map
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: 4px;">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
        </svg>
      </span>
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRouter } from 'vue-router'
import GlobalFooter from '../../components/GlobalFooter.vue'
import { properties, globalSearchQuery, globalFilterState } from '../../store.js'
import { auth, db } from '../../firebase'
import { doc, getDoc } from 'firebase/firestore'
import { onAuthStateChanged } from 'firebase/auth'

const router = useRouter()

const defaultAvatar = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23dfa37b'/><stop offset='100%' stop-color='%23c0784a'/></linearGradient></defs><circle cx='50' cy='50' r='50' fill='url(%23g)'/><circle cx='50' cy='37' r='17' fill='%23fff'/><path d='M50 58c-18 0-32 9-32 20v4h64v-4c0-11-14-20-32-20z' fill='%23fff'/></svg>"

function setDefaultAvatar(event) {
  event.target.src = defaultAvatar
}

// Reactive references tied to global store
const searchQuery = globalSearchQuery
const filterState = globalFilterState

// UI states
const activeDropdown = ref(null)
const showMapView = ref(false)
const isDesktop = ref(window.innerWidth > 992)

const mapContainer = ref(null)
const isMapLoaded = ref(false)
const mapMessage = ref('Loading Map...')
const isTrafficEnabled = ref(false)

const mapSearchInput = ref(null)

let map = null
let trafficLayer = null
let markers = []
let infoWindow = null
let directionsService = null
let directionsRenderer = null
let trafficPolylines = []
let userLocation = null
let userLocationMarker = null
let currentRouteState = null
let placesService = null
let amenityMarkers = {
  transit_station: [],
  supermarket: [],
  school: []
}
const activeAmenities = ref({
  transit_station: false,
  supermarket: false,
  school: false
})

const mapStyles = [
  { featureType: "water", stylers: [{ color: "#b9e2f5" }] },
  { featureType: "landscape", stylers: [{ color: "#f3fbf1" }] },
  { featureType: "poi", stylers: [{ visibility: "off" }] },
  { featureType: "transit", stylers: [{ visibility: "off" }] },
  { featureType: "road", elementType: "geometry", stylers: [{ color: "#ffffff" }] },
  { featureType: "road", elementType: "geometry.stroke", stylers: [{ color: "#e5ede5" }, { weight: 1 }] },
  { featureType: "road", elementType: "labels.text.fill", stylers: [{ color: "#a5b5a5" }] },
  { featureType: "road", elementType: "labels.icon", stylers: [{ visibility: "off" }] },
  { featureType: "administrative", elementType: "labels.text.fill", stylers: [{ color: "#8a9a8a" }] },
  { featureType: "landscape.natural", stylers: [{ color: "#dcf0d9" }] }
];

// User Profile Data
const userProfile = ref({
  avatar: '',
  firstName: 'Soth',
  lastName: 'Sokhomal'
})

// Hobbies/conveniences list
const availableAmenities = [
  { id: 'wifi', label: 'Wifi' },
  { id: 'kitchen', label: 'Kitchen' },
  { id: 'washer', label: 'Washer' },
  { id: 'ac', label: 'Air conditioning' },
  { id: 'parking', label: 'Free parking' },
  { id: 'pool', label: 'Pool' }
]

// Drag & Prevention setup
let touchStartX = 0
let touchStartY = 0
let isSwiping = false

function handleTouchStart(event) {
  touchStartX = event.touches[0].clientX
  touchStartY = event.touches[0].clientY
  isSwiping = false
}

function handleTouchMove(event) {
  const diffX = event.touches[0].clientX - touchStartX
  if (Math.abs(diffX) > 10) {
    isSwiping = true
  }
}

function handleTouchEnd(event, property) {
  const touchEndX = event.changedTouches[0].clientX
  const touchEndY = event.changedTouches[0].clientY
  
  const diffX = touchEndX - touchStartX
  const diffY = touchEndY - touchStartY
  
  if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 50) {
    if (diffX > 0) {
      if (property.activeSlide > 0) property.activeSlide--
    } else {
      if (property.activeSlide < property.images.length - 1) property.activeSlide++
    }
  }
}

function handleCardClick(event, propertyId) {
  if (isSwiping) {
    isSwiping = false
    return
  }
  router.push(`/property/${propertyId}`)
}

// Dropdown Toggling
function toggleDropdown(name) {
  activeDropdown.value = activeDropdown.value === name ? null : name
}

// Reset operations
function resetPriceFilter() {
  filterState.value.priceMin = 50
  filterState.value.priceMax = 610
}

function resetMoreFilters() {
  filterState.value.bedrooms = 0
  filterState.value.beds = 0
  filterState.value.bathrooms = 0
}

function clearAllFilters() {
  searchQuery.value = ''
  filterState.value.type = 'Any type'
  resetPriceFilter()
  resetMoreFilters()
  filterState.value.amenities = []
  filterState.value.rate = 'Any'
  filterState.value.period = 'Any'
}

// Filter Status Check computed variables (to highlight filter pills)
const isPriceFilterActive = computed(() => {
  return filterState.value.priceMin !== 50 || filterState.value.priceMax !== 610
})

const isMoreFilterActive = computed(() => {
  return filterState.value.bedrooms > 0 || filterState.value.beds > 0 || filterState.value.bathrooms > 0
})

// Main Property Filtering computed property
const filteredProperties = computed(() => {
  return properties.value.filter(p => {
    // 1. Text Search matching name or location
    if (searchQuery.value) {
      const q = searchQuery.value.toLowerCase()
      const matchName = p.name.toLowerCase().includes(q)
      const matchLocation = p.location.toLowerCase().includes(q)
      if (!matchName && !matchLocation) return false
    }

    // 2. Type of Place matching
    if (filterState.value.type !== 'Any type') {
      if (filterState.value.type === 'Room' && p.type !== 'condo' && p.type !== 'apartment') return false
      if (filterState.value.type === 'Entire home' && p.type !== 'house') return false
    }

    // 3. Price Range matching
    if (p.price < filterState.value.priceMin || p.price > filterState.value.priceMax) return false

    // 4. Counters matching (More filter)
    if (filterState.value.bedrooms > 0 && p.beds < filterState.value.bedrooms) return false
    if (filterState.value.beds > 0 && p.beds < filterState.value.beds) return false
    if (filterState.value.bathrooms > 0 && p.baths < filterState.value.bathrooms) return false

    // 5. Conveniences (Amenities) matching
    if (filterState.value.amenities && filterState.value.amenities.length > 0) {
      const pAmenities = p.amenities || []
      const hasAll = filterState.value.amenities.every(amenityId => pAmenities.includes(amenityId))
      if (!hasAll) return false
    }

    // 6. Review Rating matching
    if (filterState.value.rate !== 'Any') {
      const reqRating = parseFloat(filterState.value.rate.replace('+', ''))
      if (!p.rating || p.rating < reqRating) return false
    }

    // 7. Lease Period matching
    if (filterState.value.period !== 'Any') {
      if (p.period !== filterState.value.period) return false
    }

    return true
  })
})

// Google Maps Setup
function initMap() {
  isMapLoaded.value = true;
  if (!mapContainer.value) return;
  
  map = new window.google.maps.Map(mapContainer.value, {
    center: { lat: 11.588, lng: 104.925 }, // Center on Phnom Penh / Chroy Chongva
    zoom: 13,
    disableDefaultUI: false, // Turn off fully disabling UI
    mapTypeControl: false,
    streetViewControl: true, // Let users see the street
    fullscreenControl: true,
    zoomControl: true,
    padding: { top: 70, right: 16, bottom: 24, left: 0 }, // Push controls away from edges so they don't get clipped
    styles: mapStyles
  });

  if (mapSearchInput.value && window.google.maps.places) {
    const autocomplete = new window.google.maps.places.Autocomplete(mapSearchInput.value);
    autocomplete.bindTo('bounds', map);
    autocomplete.addListener('place_changed', () => {
      const place = autocomplete.getPlace();
      if (!place.geometry || !place.geometry.location) {
        return;
      }
      if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
      } else {
        map.setCenter(place.geometry.location);
        map.setZoom(15);
      }
      searchQuery.value = place.name; // This will trigger our local list filter too!
    });
  }

  directionsService = new window.google.maps.DirectionsService();
  directionsRenderer = new window.google.maps.DirectionsRenderer({
    map,
    suppressMarkers: true,
    suppressPolylines: false, // We'll toggle this based on mode
    polylineOptions: { strokeColor: '#4285F4', strokeWeight: 6, strokeOpacity: 0.8 } // Beautiful Google Blue
  });

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        userLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        renderUserLocationMarker();
      },
      (err) => {
        console.warn("Geolocation error:", err);
      }
    );
  }

  infoWindow = new window.google.maps.InfoWindow();

  updateMapMarkers();
}

function updateMapMarkers() {
  if (!map) return;

  // Clear existing markers
  markers.forEach(m => m.setMap(null));
  markers = [];

  const getMarkerIcon = (property) => {
    const score = property.match || 90;
    const text = `✨ ${score}%`;
    const svgWidth = 84;
    const svgHeight = 44;

    const svg = `
      <svg width="${svgWidth}" height="${svgHeight}" viewBox="0 0 ${svgWidth} ${svgHeight}" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.18"/>
          </filter>
        </defs>
        <rect x="6" y="6" width="${svgWidth - 12}" height="28" rx="14" fill="#ffffff" filter="url(#shadow)"/>
        <text x="${svgWidth / 2}" y="25" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#222" text-anchor="middle">${text}</text>
      </svg>
    `;
    return `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`;
  };

  filteredProperties.value.forEach(property => {
    if (!property.lat) return;

    const marker = new window.google.maps.Marker({
      position: { lat: property.lat, lng: property.lng },
      map,
      title: property.name,
      icon: {
        url: getMarkerIcon(property),
        scaledSize: new window.google.maps.Size(84, 44),
        anchor: new window.google.maps.Point(42, 22)
      },
      animation: window.google.maps.Animation.DROP,
    });

    marker.addListener('click', () => {
      if (directionsRenderer) {
        directionsRenderer.setDirections({ routes: [] });
      }

      const btnId = `btn-dir-${property.id}`;
      const infoId = `routing-info-${property.id}`;
      const content = `
        <div style="padding: 4px; font-family: 'DM Sans', sans-serif; max-width: 160px;">
          <div id="header-${property.id}">
            <img src="${property.images[0]}" style="width: 100%; height: 90px; object-fit: cover; border-radius: 8px; margin-bottom: 8px;" />
            <h3 style="margin: 0 0 4px 0; font-size: 14px; font-weight: 600; color: #111;">${property.name}</h3>
            <p style="margin: 0; font-size: 13px; color: #555; font-weight: 500;">$${property.price} / mo</p>
          </div>
          <div id="${infoId}" style="margin-top: 8px;"></div>
          <button id="${btnId}" style="margin-top: 8px; width: 100%; padding: 8px; background: #222; color: #fff; border: none; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; transition: background 0.2s;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0112 2a8 8 0 018 8.2c0 7.3-8 11.8-8 11.8z"/><circle cx="12" cy="10" r="3"/></svg>
            Route Estimate
          </button>
        </div>
      `;
      infoWindow.setContent(content);
      infoWindow.open({ anchor: marker, map });

      window.google.maps.event.addListenerOnce(infoWindow, 'closeclick', () => {
        if (window.clearActiveRoute) {
          window.clearActiveRoute(infoId, btnId, true);
        }
      });

      window.google.maps.event.addListenerOnce(infoWindow, 'domready', () => {
        const btn = document.getElementById(btnId);
        if (btn) {
          btn.addEventListener('click', () => {
            if (!userLocation) {
              alert("Location access is required. Please enable it or drag the blue location marker.");
              return;
            }
            btn.innerHTML = 'Calculating...';
            btn.style.opacity = '0.7';
            btn.style.pointerEvents = 'none';

            window.calculateRouteForMode(property.lat, property.lng, 'DRIVING', infoId, btnId);
          });
        }
      });
    });

    markers.push(marker);
  });
}

window.clearActiveRoute = function(infoId, btnId, isCloseClick = false) {
  if (directionsRenderer) directionsRenderer.setDirections({ routes: [] });
  for (let i = 0; i < trafficPolylines.length; i++) {
    trafficPolylines[i].setMap(null);
  }
  trafficPolylines = [];
  currentRouteState = null;
  
  if (!isCloseClick) {
    try {
      const rawId = infoId.replace('routing-info-', '');
      const headerDiv = document.getElementById(`header-${rawId}`);
      if (headerDiv) headerDiv.style.display = 'block';
    } catch(e) {
      // Ignore error
    }

    const infoDiv = document.getElementById(infoId);
    if (infoDiv) infoDiv.innerHTML = '';
    
    const btn = document.getElementById(btnId);
    if (btn) {
      btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0112 2a8 8 0 018 8.2c0 7.3-8 11.8-8 11.8z"/><circle cx="12" cy="10" r="3"/></svg> Route Estimate`;
      btn.style.opacity = '1';
      btn.style.pointerEvents = 'auto';
      btn.style.display = 'flex';
    }
  }
};

window.calculateRouteForMode = async function(lat, lng, mode, infoId, btnId, useMockOrigin = false) {
  if (!userLocation) return;
  
  currentRouteState = { lat, lng, mode, infoId, btnId };

  const originToUse = useMockOrigin ? { lat: 11.5564, lng: 104.9282 } : userLocation;

  // Hide the property image/title to save space while routing
  try {
    const rawId = infoId.replace('routing-info-', '');
    const headerDiv = document.getElementById(`header-${rawId}`);
    if (headerDiv) headerDiv.style.display = 'none';
  } catch (e) {
    // Ignore error
  }

  const infoDiv = document.getElementById(infoId);
  if (infoDiv) {
    infoDiv.innerHTML = `<span style="font-size: 12px; color: #666; margin-top: 8px; display: block;">Calculating ${mode.toLowerCase()} route...</span>`;
  }
  
  const btn = document.getElementById(btnId);
  if (btn) btn.style.display = 'none';

  if (directionsRenderer) directionsRenderer.setDirections({ routes: [] });
  trafficPolylines.forEach(p => p.setMap(null));
  trafficPolylines = [];

  if (mode === 'DRIVING' || mode === 'TWO_WHEELER') {
    directionsRenderer.setOptions({ suppressPolylines: true });
    try {
      const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY;
      if (!apiKey) {
        throw new Error("Missing Google Maps API Key in .env");
      }

      const response = await fetch('https://routes.googleapis.com/directions/v2:computeRoutes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Goog-Api-Key': apiKey,
          'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline,routes.travelAdvisory.speedReadingIntervals'
        },
        body: JSON.stringify({
          origin: { location: { latLng: { latitude: originToUse.lat, longitude: originToUse.lng } } },
          destination: { location: { latLng: { latitude: lat, longitude: lng } } },
          travelMode: mode === 'DRIVING' ? 'DRIVE' : 'TWO_WHEELER',
          routingPreference: 'TRAFFIC_AWARE',
          extraComputations: ['TRAFFIC_ON_POLYLINE']
        })
      });

      const data = await response.json();

      if (!response.ok || !data.routes || data.routes.length === 0) {
        if (!useMockOrigin) {
          window.calculateRouteForMode(lat, lng, mode, infoId, btnId, true);
          return;
        }
        renderRouteDashboardError("No valid route found or API error.", lat, lng, mode, infoId, btnId);
        return;
      }

      const route = data.routes[0];
      const path = window.google.maps.geometry.encoding.decodePath(route.polyline.encodedPolyline);
      
      if (route.travelAdvisory && route.travelAdvisory.speedReadingIntervals) {
        route.travelAdvisory.speedReadingIntervals.forEach(interval => {
          const start = interval.startPolylinePointIndex || 0;
          const end = interval.endPolylinePointIndex || 0;
          if (start === end) return;
          
          const segmentPath = path.slice(start, end + 1);
          let color = '#4285F4'; // NORMAL
          if (interval.speed === 'SLOW') color = '#fbbf24'; 
          if (interval.speed === 'TRAFFIC_JAM') color = '#ef4444'; 
          
          const poly = new window.google.maps.Polyline({
            path: segmentPath,
            strokeColor: color,
            strokeWeight: 6,
            strokeOpacity: 1.0,
            map: map
          });
          trafficPolylines.push(poly);
        });
      } else {
        const poly = new window.google.maps.Polyline({
          path: path,
          strokeColor: '#4285F4',
          strokeWeight: 6,
          strokeOpacity: 0.8,
          map: map
        });
        trafficPolylines.push(poly);
      }
      
      const bounds = new window.google.maps.LatLngBounds();
      path.forEach(p => bounds.extend(p));
      map.fitBounds(bounds);

      // Create Mock Result for existing Dashboard UI
      const distanceText = (route.distanceMeters / 1000).toFixed(1) + ' km';
      const durationMins = Math.ceil(parseInt(route.duration) / 60);
      const durationText = durationMins > 60 ? Math.floor(durationMins / 60) + ' hours ' + (durationMins % 60) + ' mins' : durationMins + ' mins';
      
      const mockResult = {
        routes: [{
          summary: 'Fastest route',
          legs: [{
            duration: { text: durationText },
            duration_in_traffic: { text: durationText },
            distance: { text: distanceText }
          }]
        }]
      };
      
      renderRouteDashboard(mockResult, lat, lng, mode, infoId, btnId, useMockOrigin);

    } catch (err) {
      console.error(err);
      renderRouteDashboardError("Error fetching traffic route.", lat, lng, mode, infoId, btnId);
    }
  } else {
    // TRANSIT mode uses classic DirectionsService
    directionsRenderer.setOptions({ suppressPolylines: false });
    const request = {
      origin: originToUse,
      destination: { lat, lng },
      travelMode: mode
    };

    directionsService.route(request, (result, status) => {
      if (status === 'OK') {
        directionsRenderer.setDirections(result);
        renderRouteDashboard(result, lat, lng, mode, infoId, btnId, useMockOrigin);
      } else if (status === 'ZERO_RESULTS') {
        if (!useMockOrigin) {
          window.calculateRouteForMode(lat, lng, mode, infoId, btnId, true);
          return;
        }
        renderRouteDashboardError("Transit not available for this route.", lat, lng, mode, infoId, btnId);
      } else if (status === 'REQUEST_DENIED') {
        alert("Directions API failed: REQUEST_DENIED. Please enable it in Google Cloud Console.");
      } else {
        renderRouteDashboardError("API Error: " + status, lat, lng, mode, infoId, btnId);
      }
    });
  }
};

function renderRouteDashboard(result, lat, lng, activeMode, infoId, btnId, isFallback = false) {
  const infoDiv = document.getElementById(infoId);
  if (!infoDiv) return;
  const leg = result.routes[0].legs[0];
  
  const isDrive = activeMode === 'DRIVING';
  const isTransit = activeMode === 'TRANSIT';
  const isMoto = activeMode === 'TWO_WHEELER';

  let fallbackWarning = isFallback ? `<span style="color:#664d03; font-size: 11px; font-weight: 600; margin-bottom: 2px; line-height: 1.2;">No route from your location. Estimating from city center:</span>` : '';
  let bgStyle = isFallback ? 'background: #fff3cd; border: 1px solid #ffe69c;' : 'border: 1px solid #eee;';

  infoDiv.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
      <div style="display: flex; justify-content: space-between; gap: 4px; background: #f5f5f5; padding: 4px; border-radius: 6px;">
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'DRIVING', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isDrive ? '#fff' : 'transparent'}; box-shadow: ${isDrive ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isDrive ? '600' : '400'}; font-size: 11px;">🚗 Drive</button>
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'TRANSIT', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isTransit ? '#fff' : 'transparent'}; box-shadow: ${isTransit ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isTransit ? '600' : '400'}; font-size: 11px;">🚌 Transit</button>
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'TWO_WHEELER', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isMoto ? '#fff' : 'transparent'}; box-shadow: ${isMoto ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isMoto ? '600' : '400'}; font-size: 11px;">🏍️ Moto</button>
      </div>
      <div style="padding: 6px 8px; border-radius: 6px; display: flex; flex-direction: column; gap: 2px; ${bgStyle}">
        ${fallbackWarning}
        <span style="color:#111; font-weight:700; font-size: 14px;">
          ${leg.duration_in_traffic ? `${leg.duration_in_traffic.text} <span style="font-size:12px; font-weight:500; color:#b91c1c;">(with traffic)</span>` : leg.duration.text}
        </span>
        <span style="color:#666; font-size: 12px;">${leg.distance.text} ${activeMode.toLowerCase()} via ${result.routes[0].summary || 'route'}</span>
      </div>
      <button onclick="window.clearActiveRoute('${infoId}', '${btnId}')" style="width:100%; padding: 6px; background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; transition: background 0.2s;">Cancel Route</button>
    </div>
  `;
  
  const btn = document.getElementById(btnId);
  if (btn) btn.style.display = 'none';
}

function renderRouteDashboardError(errorMsg, lat, lng, activeMode, infoId, btnId) {
  const infoDiv = document.getElementById(infoId);
  if (!infoDiv) return;
  const isDrive = activeMode === 'DRIVING';
  const isTransit = activeMode === 'TRANSIT';
  const isMoto = activeMode === 'TWO_WHEELER';

  infoDiv.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
      <div style="display: flex; justify-content: space-between; gap: 4px; background: #f5f5f5; padding: 4px; border-radius: 6px;">
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'DRIVING', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isDrive ? '#fff' : 'transparent'}; box-shadow: ${isDrive ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isDrive ? '600' : '400'}; font-size: 11px;">🚗 Drive</button>
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'TRANSIT', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isTransit ? '#fff' : 'transparent'}; box-shadow: ${isTransit ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isTransit ? '600' : '400'}; font-size: 11px;">🚌 Transit</button>
        <button onclick="window.calculateRouteForMode(${lat}, ${lng}, 'TWO_WHEELER', '${infoId}', '${btnId}')" style="flex:1; border:none; padding: 4px 8px; border-radius: 4px; cursor: pointer; background: ${isMoto ? '#fff' : 'transparent'}; box-shadow: ${isMoto ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'}; font-weight: ${isMoto ? '600' : '400'}; font-size: 11px;">🏍️ Moto</button>
      </div>
      <div style="padding: 6px 8px; border: 1px solid #fee2e2; background: #fef2f2; border-radius: 6px; display: flex; flex-direction: column; gap: 2px;">
        <span style="color:#991b1b; font-weight:600; font-size: 11px;">${errorMsg}</span>
      </div>
      <button onclick="window.clearActiveRoute('${infoId}', '${btnId}')" style="width:100%; padding: 6px; background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; transition: background 0.2s;">Cancel Route</button>
    </div>
  `;

  const btn = document.getElementById(btnId);
  if (btn) btn.style.display = 'none';
}

function getAmenityMarkerIcon(type) {
  let emoji = '📍';
  if (type === 'transit_station') emoji = '🚇';
  else if (type === 'supermarket') emoji = '🛒';
  else if (type === 'school') emoji = '🎓';

  const svg = `<svg width="44" height="44" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg">
  <circle cx="22" cy="22" r="18" fill="white" stroke="%234285F4" stroke-width="2"/>
  <text x="22" y="29" font-family="sans-serif" font-size="20" text-anchor="middle">${emoji}</text>
</svg>`;
  
  return 'data:image/svg+xml;charset=UTF-8,' + svg;
}

function searchNearby(type, keyword) {
  if (!map || !window.google.maps.places) {
    alert("Places API not loaded yet.");
    return;
  }
  
  if (activeAmenities.value[type]) {
    clearAmenities(type);
    return;
  }

  if (!placesService) {
    placesService = new window.google.maps.places.PlacesService(map);
  }
  
  activeAmenities.value[type] = true;
  
  const request = {
    location: map.getCenter(),
    radius: 1500, // 1.5km
    type: type
  };

  placesService.nearbySearch(request, (results, status) => {
    // If the user quickly toggled it off while searching, abort marker creation
    if (!activeAmenities.value[type]) return;

    if (status === window.google.maps.places.PlacesServiceStatus.OK && results) {
      for (let i = 0; i < results.length; i++) {
        createAmenityMarker(results[i], type);
      }
    } else {
      console.warn('Places API nearby search failed or found 0 results.', status);
      alert(`No ${keyword} found nearby or Places API not enabled. Status: ` + status);
      activeAmenities.value[type] = false;
    }
  });
}

function createAmenityMarker(place, type) {
  if (!place.geometry || !place.geometry.location) return;
  
  const marker = new window.google.maps.Marker({
    map,
    position: place.geometry.location,
    title: place.name,
    icon: {
      url: getAmenityMarkerIcon(type),
      scaledSize: new window.google.maps.Size(44, 44),
      anchor: new window.google.maps.Point(22, 22)
    }
  });
  amenityMarkers[type].push(marker);
}

function toggleTraffic() {
  if (!map) return;
  if (!trafficLayer) {
    trafficLayer = new window.google.maps.TrafficLayer();
  }
  isTrafficEnabled.value = !isTrafficEnabled.value;
  if (isTrafficEnabled.value) {
    trafficLayer.setMap(map);
    map.setOptions({ styles: [] });
  } else {
    trafficLayer.setMap(null);
    map.setOptions({ styles: mapStyles });
  }
}

function clearAmenities(type = null) {
  if (type) {
    activeAmenities.value[type] = false;
    for (let i = 0; i < amenityMarkers[type].length; i++) {
      if (amenityMarkers[type][i]) {
        amenityMarkers[type][i].setMap(null);
      }
    }
    amenityMarkers[type] = [];
  } else {
    for (const key of Object.keys(activeAmenities.value)) {
      activeAmenities.value[key] = false;
      for (let i = 0; i < amenityMarkers[key].length; i++) {
        if (amenityMarkers[key][i]) {
          amenityMarkers[key][i].setMap(null);
        }
      }
      amenityMarkers[key] = [];
    }
  }
}

function renderUserLocationMarker() {
  if (!map || !userLocation) return;
  if (userLocationMarker) {
    userLocationMarker.setPosition(userLocation);
  } else {
    userLocationMarker = new window.google.maps.Marker({
      map,
      position: userLocation,
      draggable: true,
      title: "Your Location (Drag to adjust)",
      icon: {
        path: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
        fillColor: '#4285F4',
        fillOpacity: 1,
        strokeColor: '#ffffff',
        strokeWeight: 2,
        scale: 1.5,
        anchor: new window.google.maps.Point(12, 24)
      },
      zIndex: 999
    });
    userLocationMarker.addListener('dragend', () => {
      const pos = userLocationMarker.getPosition();
      userLocation = { lat: pos.lat(), lng: pos.lng() };
      
      if (currentRouteState) {
        window.calculateRouteForMode(
          currentRouteState.lat, 
          currentRouteState.lng, 
          currentRouteState.mode, 
          currentRouteState.infoId, 
          currentRouteState.btnId
        );
      }
    });
  }
}

function panToUserLocation() {
  if (userLocation && map) {
    map.panTo(userLocation);
    map.setZoom(15);
  } else if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      userLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
      renderUserLocationMarker();
      map.panTo(userLocation);
      map.setZoom(15);
    });
  } else {
    alert("Location not available. Please allow browser location access.");
  }
}

// Lifecycle Events & Handlers
const handleGlobalClick = (event) => {
  if (activeDropdown.value) {
    const closestWrapper = event.target.closest('.filter-dropdown-wrapper')
    if (!closestWrapper) {
      activeDropdown.value = null
    }
  }
}

const handleResize = () => {
  isDesktop.value = window.innerWidth > 992
}

async function fetchUserProfile(user) {
  try {
    const docSnap = await getDoc(doc(db, 'users', user.uid));
    if (docSnap.exists()) {
      const data = docSnap.data();
      if (data.firstName) userProfile.value.firstName = data.firstName;
      if (data.lastName) userProfile.value.lastName = data.lastName;
      if (data.avatar) userProfile.value.avatar = data.avatar;
    }
  } catch (err) {
    console.error("Error fetching profile on search page:", err);
  }
}

onMounted(() => {
  window.addEventListener('click', handleGlobalClick)
  window.addEventListener('resize', handleResize)

  // Auth fetch
  onAuthStateChanged(auth, async (user) => {
    if (user) {
      await fetchUserProfile(user);
    }
  });

  // Load Map Script
  const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY;
  if (!apiKey || apiKey === 'your_api_key_here') {
    mapMessage.value = 'Please add your Google Maps API key to .env file'
    console.warn('Google Maps API key is missing.');
    return;
  }

  if (window.google && window.google.maps) {
    initMap();
    return;
  }

  window.initGoogleMap = initMap;
  const script = document.createElement('script');
  script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&libraries=places&callback=initGoogleMap`;
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);
})

onBeforeUnmount(() => {
  window.removeEventListener('click', handleGlobalClick)
  window.removeEventListener('resize', handleResize)
})

// Watch filters to redraw markers on map
watch(filteredProperties, () => {
  if (isMapLoaded.value && map) {
    updateMapMarkers();
  }
}, { deep: true })
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.search-results-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  background: #fff;
  font-family: 'DM Sans', sans-serif;
  overflow: hidden;
}

/* Header Nav */
.top-nav {
  display: flex; justify-content: space-between; align-items: center;
  padding: 16px 40px;
  background: #fff;
  border-bottom: 1px solid #ebebeb;
  height: 70px;
  flex-shrink: 0;
}
.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #5C4E4A;
  cursor: pointer;
  border: 0;
  background: transparent;
  font-family: inherit;
}
.logo-icon {
  width: 32px; height: 32px; color: #5C4E4A;
  display: flex; align-items: center; justify-content: center;
}
.logo-text { font-size: 1.3rem; font-weight: 600; color: #5C4E4A; letter-spacing: -0.5px; }

.nav-right { display: flex; align-items: center; gap: 12px; }
.host-text { font-size: 0.9rem; font-weight: 600; color: #222; cursor: pointer; padding: 12px; border-radius: 20px; transition: background 0.2s; }
.host-text:hover { background: #f7f7f7; }
.profile-menu {
  display: flex; align-items: center; justify-content: center; margin-left: 8px;
  border-radius: 50%; padding: 4px; cursor: pointer; transition: background 0.2s;
}
.profile-menu:hover { background: #f0f0f0; }
.avatar img {
  width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 1px solid #ebebeb;
}

/* Workspace Panels */
.search-workspace {
  display: flex;
  flex: 1;
  height: calc(100vh - 70px);
  overflow: hidden;
}

/* Left Listings Column */
.results-column {
  width: 55%;
  height: 100%;
  overflow-y: auto;
  padding: 24px 32px 100px 40px;
  background: #fff;
  display: flex;
  flex-direction: column;
  border-right: 1px solid #ebebeb;
}

/* Horizontal Filters Bar */
.filter-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  z-index: 10;
  flex-wrap: wrap;
}

.filter-dropdown-wrapper {
  position: relative;
}

.filter-pill-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 50px;
  background: #fff;
  color: #333;
  font-size: 0.85rem;
  font-weight: 500;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-pill-btn:hover {
  border-color: #999;
}

.filter-pill-btn.active {
  border-color: #111;
  background: #f7f7f7;
  color: #111;
  font-weight: 600;
}

.filter-pill-btn svg {
  transition: transform 0.2s ease;
}

.filter-pill-btn.active svg {
  transform: rotate(180deg);
}

/* Dropdown popover styling */
.filter-popover {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  background: #fff;
  border: 1px solid #eaeaea;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  padding: 16px 20px;
  min-width: 260px;
  z-index: 99;
  animation: popoverFadeIn 0.2s ease;
}

.filter-popover.wide {
  min-width: 320px;
}

@keyframes popoverFadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.popover-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 12px;
}

/* Price range popover elements */
.popover-price-inputs {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.price-input-box {
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 8px 12px;
  background: #fafafa;
  flex: 1;
}

.popover-currency {
  color: #888;
  font-weight: 600;
  margin-right: 4px;
  font-size: 0.9rem;
}

.price-input-box input {
  border: none;
  background: transparent;
  outline: none;
  font-family: inherit;
  font-size: 0.9rem;
  width: 100%;
}

.input-dash {
  color: #aaa;
  font-weight: 500;
}

/* Radio options and checkboxes */
.popover-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}

.option-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  color: #444;
  cursor: pointer;
}

.option-label input {
  cursor: pointer;
  accent-color: #111;
}

.popover-checkbox-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

.popover-checkbox {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: #444;
  cursor: pointer;
}

.popover-checkbox input {
  cursor: pointer;
  accent-color: #111;
}

/* Counters for bedrooms/beds (More filter) */
.popover-counters {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 16px;
}

.popover-counter-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.88rem;
  color: #444;
}

.popover-counter-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.counter-btn {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid #ccc;
  background: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  transition: all 0.2s;
}

.counter-btn:hover:not(:disabled) {
  border-color: #111;
  background: #f7f7f7;
}

.counter-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.counter-val {
  font-weight: 600;
  min-width: 24px;
  text-align: center;
  font-size: 0.85rem;
}

/* Popover action footers */
.popover-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #f2f2f2;
  padding-top: 12px;
  margin-top: 8px;
}

.popover-clear {
  border: none;
  background: transparent;
  color: #666;
  text-decoration: underline;
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
}

.popover-clear:hover {
  color: #111;
}

.popover-apply {
  background: #111;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 6px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.popover-apply:hover {
  background: #333;
}

/* Stats Header block */
.stats-header {
  margin-bottom: 20px;
}

.stats-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 4px;
}

.stats-subtitle {
  font-size: 0.9rem;
  color: #666;
}

/* Listings Grid */
.listings-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px 14px;
}

/* 2-column property card */
.search-property-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
  min-width: 0;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  border-radius: 12px;
  padding: 8px;
}

.search-property-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
  background: #fafafa;
}

.card-carousel {
  position: relative; border-radius: 12px;
  overflow: hidden; aspect-ratio: 1.48; background: #f0f0f0;
}

.carousel-track {
  display: flex; height: 100%;
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.carousel-img {
  min-width: 100%; height: 100%; object-fit: cover;
  flex-shrink: 0; pointer-events: none; user-select: none;
}

.heart-btn {
  position: absolute; top: 8px; right: 8px;
  width: 26px; height: 26px; background: #fff; border: none;
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  transition: transform 0.15s; z-index: 2;
}

.heart-btn.liked {
  transform: scale(1.05);
}

.carousel-dots {
  position: absolute; bottom: 6px; left: 50%; transform: translateX(-50%);
  display: flex; gap: 3px; z-index: 2;
}

.cdot {
  width: 4px; height: 4px; border-radius: 50%;
  background: rgba(255,255,255,0.5); cursor: pointer;
  transition: background 0.2s, width 0.2s;
}

.cdot.active { background: #fff; width: 12px; border-radius: 4px; }

.carousel-arrow {
  position: absolute; top: 50%; transform: translateY(-50%);
  background: rgba(255,255,255,0.88); border: none; border-radius: 50%;
  width: 20px; height: 20px; font-size: 0.85rem;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; z-index: 2; transition: background 0.15s; line-height: 1;
}

.carousel-arrow:hover { background: #fff; }
.carousel-arrow.left { left: 6px; }
.carousel-arrow.right { right: 6px; }

/* Card Info */
.card-info { display: flex; flex-direction: column; gap: 4px; padding: 0 1px; }

.card-title-row {
  display: flex; justify-content: space-between; align-items: center; gap: 4px;
}

.card-name {
  font-weight: 700; font-size: 0.85rem; color: #111;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

.card-price { font-weight: 700; font-size: 0.85rem; color: #111; flex-shrink: 0; }

.card-location { display: flex; align-items: center; gap: 3px; font-size: 0.72rem; color: #aaa; }

.card-meta { display: flex; align-items: center; justify-content: space-between; }

.meta-tags { display: flex; gap: 4px; flex-wrap: wrap; }

.tag {
  display: flex; align-items: center; gap: 2px;
  padding: 2px 6px; background: #f5f5f5; border-radius: 50px;
  font-size: 0.65rem; color: #555; font-weight: 500;
}

.match { font-size: 0.72rem; color: #aaa; font-weight: 500; flex-shrink: 0; }

/* Empty state */
.empty-results {
  grid-column: 1 / -1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
  color: #666;
}

.empty-results p {
  margin-top: 12px;
  font-size: 0.95rem;
  font-weight: 500;
}

.btn-clear-all {
  margin-top: 16px;
  background: #111;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 8px 20px;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-clear-all:hover {
  background: #333;
}

/* Right: Map Column */
/* ====================================================
   CHOOSE YOUR MAP LAYOUT:
   To switch back to full-screen map (Option 1), uncomment
   Option 1 below and comment out Option 2.
   ==================================================== */

/* --- OPTION 1: Full-column Map (No spacing) ---
/*
.map-column {
  width: 45%;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
}
*/

/* --- OPTION 2: Floating Card Map (With spacing & rounded corners) - ACTIVE --- */
.map-column {
  width: 45%;
  max-width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #f7f9fb;
  padding: 24px 24px 24px 20px;
  position: relative;
  box-sizing: border-box;
}

/* Search Box Overlay on Map */
.map-search-container {
  position: absolute;
  top: 16px;
  left: 16px;
  z-index: 10;
  max-width: 320px;
  width: calc(100% - 32px);
}

.map-search-box {
  display: flex;
  align-items: center;
  gap: 7px;
  border: 1.5px solid #e8e8e8;
  border-radius: 50px;
  padding: 8px 16px;
  background: #fff;
  width: 100%;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.map-search-box input {
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 0.82rem;
  color: #333;
  flex: 1;
  background: transparent;
}

.map-search-box input::placeholder {
  color: #bbb;
}

/* --- OPTION 1: Full-column Map (No spacing) ---
/*
.map-outer-wrapper {
  flex: 1;
  height: 100%;
  width: 100%;
  background: #eee;
  position: relative;
}
*/

/* --- OPTION 2: Floating Card Map (With spacing & rounded corners) - ACTIVE --- */
.map-outer-wrapper {
  flex: 1;
  height: 100%;
  width: 100%;
  max-width: 100%;
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  border: 1px solid #e2e5e8;
  box-sizing: border-box;
}

.map-element {
  width: 100%;
  height: 100%;
}

.map-loading-overlay {
  position: absolute;
  inset: 0;
  background: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
  font-size: 0.9rem;
  font-weight: 500;
  z-index: 2;
}

/* Floating toggles and mobile styles */
.mobile-toggle-btn {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 99;
  display: flex;
  align-items: center;
  padding: 12px 24px;
  background: #111;
  color: #fff;
  border: none;
  border-radius: 50px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
  font-family: inherit;
}

.mobile-toggle-btn:active {
  transform: translateX(-50%) scale(0.98);
}

/* Responsive queries */
@media (max-width: 992px) {
  .top-nav {
    padding: 12px 20px;
  }
  .results-column {
    width: 100%;
    padding: 16px 20px 100px;
  }
  .map-column {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 5;
  }
  .listings-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .listings-grid {
    grid-template-columns: 1fr;
  }
  .filter-bar {
    gap: 6px;
  }
  .filter-pill-btn {
    padding: 6px 12px;
    font-size: 0.8rem;
  }
}

/* Amenities Toolbar */
.map-amenities-toolbar {
  display: flex;
  gap: 6px;
  margin-top: 8px;
  overflow-x: auto;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.map-amenities-toolbar::-webkit-scrollbar {
  display: none;
}

.amenity-btn {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 50px;
  padding: 6px 12px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  transition: all 0.2s;
  white-space: nowrap;
}

.amenity-btn:hover {
  background: #f7f7f7;
  border-color: #bbb;
}

.amenity-btn.active-btn {
  background: #e6f2ff;
  border-color: #4285F4;
  color: #4285F4;
}

.clear-btn {
  color: #d9534f;
  border-color: #d9534f;
}
.clear-btn:hover {
  background: #fdf2f2;
}

/* Locate Me Button */
.locate-me-btn {
  position: absolute;
  bottom: 24px;
  right: 24px;
  width: 44px;
  height: 44px;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  color: #333;
  z-index: 10;
  transition: all 0.2s;
}

.locate-me-btn:hover {
  background: #f0f0f0;
}
</style>
