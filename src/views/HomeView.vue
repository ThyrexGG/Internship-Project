<template>
  <div class="home-page">
    <!-- Top Nav -->
    <header class="top-nav">
      <button class="logo" type="button" @click="activeTab = 'home'" aria-label="Go to Home">
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

      <!-- Right Actions -->
      <div class="nav-right">
        <span class="host-text">Become a host</span>
        <button class="globe-btn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>
          </svg>
        </button>
        <div class="profile-menu">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
          <div class="avatar">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80" alt="User" />
          </div>
        </div>
      </div>
    </header>

    <!-- Scrollable Content -->
    <main class="content">
      <template v-if="activeTab === 'home'">
        <!-- Hero + Search -->
        <section class="hero-section">
        <h1 class="hero-title">Safety is what we priority,<br />Affordable is what we offer.</h1>
        <div class="search-filter">
          <div class="search-box">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
              <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
            </svg>
            <input v-model="searchQuery" type="text" placeholder="Search" />
          </div>
          <button class="filter-btn" @click="filterOpen = !filterOpen">
            Filter By
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path :d="filterOpen ? 'M18 15l-6-6-6 6' : 'M6 9l6 6 6-6'" />
            </svg>
          </button>
        </div>
      </section>

      <!-- Map Section -->
      <section class="map-section">
        <div class="map-wrapper">
          <div ref="mapContainer" class="map-container"></div>
          <div v-if="!isMapLoaded" class="map-placeholder">
            <span>{{ mapMessage }}</span>
          </div>
        </div>
      </section>

      <!-- Property Grid -->
      <section class="listings">
        <div v-for="property in filteredProperties" :key="property.id" class="property-card" @click="$router.push(`/property/${property.id}`)">
          <!-- Carousel -->
          <div class="card-carousel">
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
              <span v-for="(_, i) in property.images" :key="i" class="cdot" :class="{ active: property.activeSlide === i }" @click="property.activeSlide = i" />
            </div>
            <button v-if="property.activeSlide > 0" class="carousel-arrow left" @click="property.activeSlide--">‹</button>
            <button v-if="property.activeSlide < property.images.length - 1" class="carousel-arrow right" @click="property.activeSlide++">›</button>
          </div>

          <!-- Info -->
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
      </section>
      </template>

      <template v-else-if="activeTab === 'favorite'">
        <section class="hero-section">
          <h1 class="hero-title">Save to favorite and still<br />considering?</h1>
          <div class="search-filter">
            <div class="search-box">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
              </svg>
              <input v-model="searchQuery" type="text" placeholder="Search" />
            </div>
            <button class="filter-btn" @click="filterOpen = !filterOpen">
              Filter By
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path :d="filterOpen ? 'M18 15l-6-6-6 6' : 'M6 9l6 6 6-6'" />
              </svg>
            </button>
          </div>
        </section>

        <!-- Favorite Properties Grid -->
        <section class="listings">
          <div v-if="favoriteProperties.length === 0" class="empty-favorites">
            <p>No favorites yet. Start saving properties you love!</p>
          </div>
          <div v-for="property in favoriteProperties" :key="property.id" class="property-card" @click="$router.push(`/property/${property.id}`)">
            <!-- Carousel -->
            <div class="card-carousel">
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
                <span v-for="(_, i) in property.images" :key="i" class="cdot" :class="{ active: property.activeSlide === i }" @click="property.activeSlide = i" />
              </div>
              <button v-if="property.activeSlide > 0" class="carousel-arrow left" @click="property.activeSlide--">‹</button>
              <button v-if="property.activeSlide < property.images.length - 1" class="carousel-arrow right" @click="property.activeSlide++">›</button>
            </div>

            <!-- Info -->
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
        </section>
      </template>

      <template v-else-if="activeTab === 'feeds'">
        <section class="feeds-section">
          <div class="feeds-main">
            <h1 class="feeds-title">Feeds</h1>

            <article class="post-composer">
              <h2>Post something</h2>
              <div class="composer-row">
                <img class="feed-avatar" :src="currentUser.avatar" :alt="currentUser.name" />
                <input type="text" placeholder="What's on your mind?" />
                <button class="composer-add" aria-label="Add post">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 5v14M5 12h14" />
                  </svg>
                </button>
              </div>
            </article>

            <article v-for="post in feedPosts" :key="post.id" class="feed-card">
              <header class="feed-card-header">
                <div class="feed-author">
                  <img class="feed-avatar" :src="post.avatar" :alt="post.author" />
                  <span>{{ post.author }}</span>
                </div>
                <button class="feed-more" aria-label="More options">
                  <span></span><span></span><span></span>
                </button>
              </header>

              <img v-if="post.image" class="feed-image" :src="post.image" :alt="post.imageAlt" />
              <p v-if="post.text" class="feed-text">{{ post.text }}</p>

              <footer class="feed-actions">
                <span>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                  </svg>
                  {{ post.likes }}
                </span>
                <span>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15a4 4 0 0 1-4 4H7l-4 4V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z" />
                  </svg>
                  {{ post.comments }}
                </span>
              </footer>
              <p v-if="post.caption" class="feed-caption">{{ post.caption }}</p>
            </article>
          </div>

          <aside class="mates-panel">
            <h1 class="feeds-title">Messages &amp; Mates</h1>
            <section class="mates-card">
              <h2>Messages</h2>
              <div v-for="message in messages" :key="message.name" class="mate-row">
                <img class="feed-avatar" :src="message.avatar" :alt="message.name" />
                <div class="mate-copy">
                  <span>{{ message.name }}</span>
                  <p>{{ message.preview }}</p>
                </div>
                <time>{{ message.time }}</time>
              </div>
            </section>

            <section class="mates-card">
              <h2>Roommates</h2>
              <div v-for="mate in roommates" :key="mate.name" class="mate-row">
                <img class="feed-avatar" :src="mate.avatar" :alt="mate.name" />
                <div class="mate-copy">
                  <span>{{ mate.name }}</span>
                </div>
                <small>Roommate</small>
              </div>
            </section>

            <section class="mates-card">
              <h2>Friends</h2>
              <div v-for="friend in friends" :key="friend.name" class="mate-row">
                <img class="feed-avatar" :src="friend.avatar" :alt="friend.name" />
                <div class="mate-copy">
                  <span>{{ friend.name }}</span>
                </div>
                <small>Friends</small>
              </div>
            </section>
          </aside>
        </section>
      </template>

      <template v-else-if="activeTab === 'noti'">
        <section class="notification-section">
          <h1 class="notification-title">Notification</h1>

          <div class="notification-list">
            <article
              v-for="notification in notifications"
              :key="notification.id"
              class="notification-item"
              :class="{ seen: notification.seen }"
            >
              <img class="notification-avatar" :src="notification.avatar" :alt="notification.name" />
              <div class="notification-copy">
                <h2>{{ notification.name }}</h2>
                <p>{{ notification.message }}</p>
              </div>

              <div class="notification-status" :class="notification.type">
                <svg v-if="notification.type === 'roommate'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                  <circle cx="9" cy="7" r="4" />
                  <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
                  <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                </svg>
                <span v-else-if="notification.type === 'unread'" class="unread-dot"></span>
                <svg v-else-if="notification.type === 'heart'" width="16" height="16" viewBox="0 0 24 24" fill="#f40f0f" stroke="#f40f0f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z" />
                </svg>
                <svg v-else-if="notification.type === 'comment'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15a4 4 0 0 1-4 4H7l-4 4V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z" />
                </svg>
              </div>
            </article>
          </div>
        </section>
      </template>

      <template v-else-if="activeTab === 'settings'">
        <div class="settings-layout">
          <!-- Sidebar -->
          <aside class="settings-sidebar">
            <h2 class="settings-title">Setting</h2>
            <div class="search-filter" style="max-width: 100%; margin-bottom: 24px;">
              <div class="search-box">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
                  <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
                </svg>
                <input type="text" placeholder="Search" />
              </div>
            </div>
            
            <div class="sidebar-section">
              <h3>How you use Homesweet</h3>
              <ul class="sidebar-menu">
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'profile'}" @click="activeSettingsTab = 'profile'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                  My Profile
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'notification'}" @click="activeSettingsTab = 'notification'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>
                  Notification
                </li>
              </ul>
            </div>

            <div class="sidebar-section">
              <h3>Who can your content</h3>
              <ul class="sidebar-menu">
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'security'}" @click="activeSettingsTab = 'security'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                  Password & Security
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'block'}" @click="activeSettingsTab = 'block'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>
                  Block
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'location'}" @click="activeSettingsTab = 'location'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  Location
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'visibility'}" @click="activeSettingsTab = 'visibility'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
                  How public see you
                </li>
              </ul>
            </div>

            <div class="sidebar-section">
              <h3>Account & Help</h3>
              <ul class="sidebar-menu">
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'help'}" @click="activeSettingsTab = 'help'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                  Help
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'upgrade'}" @click="activeSettingsTab = 'upgrade'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                  Upgrade to Landlord
                </li>
                <li class="sidebar-item" :class="{active: activeSettingsTab === 'status'}" @click="activeSettingsTab = 'status'">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/></svg>
                  Account status
                </li>
              </ul>
            </div>
          </aside>

          <!-- Main Content -->
          <div class="settings-main">
            <template v-if="activeSettingsTab === 'profile'">
              <h1 class="main-title">Edit Profile</h1>
              <div class="profile-header">
                <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=160&q=80" alt="Profile" class="profile-lg-avatar" />
                <div class="profile-actions">
                  <button class="btn-dark">Change Image</button>
                  <button class="btn-outline">Delete Profile</button>
                </div>
                <p class="profile-note">Please noted that you can only change your profile only once a week</p>
              </div>

              <h2 class="sub-title">Personal Details</h2>
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">First Name</label>
                  <div class="input-wrapper">
                    <input type="text" value="Soth" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <label class="form-label">Last Name</label>
                  <div class="input-wrapper">
                    <input type="text" value="Sokhomal" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    <input type="text" value="09 Oct, 2006" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    <input type="text" value="Female" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                    <input type="text" value="01156787697" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" /></svg>
                    <input type="text" value="In relationship" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                    <input type="text" value="Camtech University" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
                    <input type="text" value="Software Developer" readonly />
                  </div>
                </div>
              </div>

              <h2 class="sub-title" style="margin-top: 24px;">Hobbies</h2>
              <div class="form-grid">
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
                    <input type="text" value="Music" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"/><circle cx="16" cy="12" r="1"/><circle cx="18" cy="12" r="1"/><path d="M6 12h4M8 10v4"/></svg>
                    <input type="text" value="Games" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20M2 12a14.5 14.5 0 0 0 20 0M12 2a14.5 14.5 0 0 1 0 20M2 12a14.5 14.5 0 0 1 20 0"/></svg>
                    <input type="text" value="Sports" readonly />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>
                    <input type="text" value="Movies" readonly />
                  </div>
                </div>
              </div>

              <h2 class="sub-title" style="margin-top: 24px;">Address Details</h2>
              <div class="sub-section">
                <h3 class="minor-title">Room Detail</h3>
                <div class="form-grid">
                  <div class="form-group">
                    <div class="input-wrapper with-icon">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="8" y1="6" x2="8.01" y2="6"/><line x1="16" y1="6" x2="16.01" y2="6"/><line x1="8" y1="10" x2="8.01" y2="10"/><line x1="16" y1="10" x2="16.01" y2="10"/><line x1="8" y1="14" x2="8.01" y2="14"/><line x1="16" y1="14" x2="16.01" y2="14"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
                      <input type="text" value="Skystar Condo Premium" readonly />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-wrapper with-icon">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l9 4v6c0 5.5-3.5 10.5-9 12-5.5-1.5-9-6.5-9-12V6l9-4z"/><circle cx="12" cy="11" r="3"/></svg>
                      <input type="text" value="Skystar - Somnang" readonly />
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="sub-section">
                <h3 class="minor-title">Mates</h3>
                <div class="form-grid">
                  <div class="form-group">
                    <div class="input-wrapper">
                      <input type="text" value="Yim Vatey" readonly />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-wrapper">
                      <input type="text" value="Muy Leng" readonly />
                    </div>
                  </div>
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'notification'">
              <h1 class="main-title">Push Notifications</h1>
              
              <div class="notification-setting-group">
                <h3 class="minor-title">Pause all</h3>
                <div class="setting-row">
                  <span>Pause all</span>
                  <label class="toggle-switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                  </label>
                </div>
              </div>

              <div class="notification-setting-group">
                <h3 class="minor-title">Like</h3>
                <div class="radio-group">
                  <label class="radio-label"><input type="radio" name="like" value="off"> Off</label>
                  <label class="radio-label"><input type="radio" name="like" value="friends" checked> Friends</label>
                  <label class="radio-label"><input type="radio" name="like" value="everyone"> Everyone</label>
                </div>
              </div>

              <div class="notification-setting-group">
                <h3 class="minor-title">Comments</h3>
                <div class="radio-group">
                  <label class="radio-label"><input type="radio" name="comment" value="off"> Off</label>
                  <label class="radio-label"><input type="radio" name="comment" value="friends" checked> Friends</label>
                  <label class="radio-label"><input type="radio" name="comment" value="everyone"> Everyone</label>
                </div>
              </div>

              <div class="notification-setting-group">
                <h3 class="minor-title">Follow</h3>
                <div class="radio-group">
                  <label class="radio-label"><input type="radio" name="follow" value="off"> Off</label>
                  <label class="radio-label"><input type="radio" name="follow" value="everyone" checked> Everyone</label>
                </div>
              </div>

              <div class="notification-setting-group">
                <h3 class="minor-title">Message Request</h3>
                <div class="radio-group">
                  <label class="radio-label"><input type="radio" name="msg" value="off"> Off</label>
                  <label class="radio-label"><input type="radio" name="msg" value="everyone" checked> Everyone</label>
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'security'">
              <h1 class="main-title">Password & Security</h1>
              
              <h2 class="minor-title" style="margin-top: 24px;">Login & Recovery</h2>
              <div class="settings-list-group">
                <div class="settings-list-item">
                  <div class="list-item-text">Change password</div>
                  <div class="list-item-arrow">›</div>
                </div>
                <div class="settings-list-item">
                  <div class="list-item-text">Two-factor authentication</div>
                  <div class="list-item-arrow">›</div>
                </div>
              </div>

              <h2 class="minor-title" style="margin-top: 32px;">Security Check</h2>
              <div class="settings-list-group">
                <div class="settings-list-item">
                  <div class="list-item-text">Where you login</div>
                  <div class="list-item-arrow">›</div>
                </div>
                <div class="settings-list-item">
                  <div class="list-item-text">Recent email</div>
                  <div class="list-item-arrow">›</div>
                </div>
              </div>

              <h2 class="minor-title" style="margin-top: 32px;">Account Verification</h2>
              <div class="settings-list-group">
                <div class="settings-list-item" @click="$router.push('/verify-account')">
                  <div class="list-item-text">Verify Identity</div>
                  <div class="list-item-arrow">›</div>
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'block'">
              <h1 class="main-title">Blocked Users</h1>
              <p style="color: #666; font-size: 0.95rem; margin-bottom: 24px;">Manage the people you have blocked. They cannot see your profile or message you.</p>
              
              <div class="settings-list-group">
                <!-- Mock Data Item -->
                <div class="settings-list-item" style="cursor: default;">
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=50&q=80" alt="Blocked User" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />
                    <div class="list-item-text">Dave Rim</div>
                  </div>
                  <button class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">Unblock</button>
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'location'">
              <h1 class="main-title">Location Settings</h1>
              <p style="color: #666; font-size: 0.95rem; margin-bottom: 24px;">Manage your location preferences and visibility.</p>
              
              <div class="notification-setting-group">
                <div class="setting-row">
                  <span>Share precise location</span>
                  <label class="toggle-switch">
                    <input type="checkbox" checked>
                    <span class="slider round"></span>
                  </label>
                </div>
                <p style="font-size: 0.85rem; color: #888; margin-top: -8px; margin-bottom: 24px;">Allows roommates to see your exact location on the map.</p>
              </div>

              <h2 class="minor-title">Current Region</h2>
              <div class="form-group" style="max-width: 500px;">
                <div class="input-wrapper with-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" /></svg>
                  <input type="text" value="Phnom Penh, Cambodia" readonly style="background: #f9f9f9; cursor: not-allowed;" />
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'public'">
              <h1 class="main-title">How public see you</h1>
              <p style="color: #666; font-size: 0.95rem; margin-bottom: 24px;">Control your privacy and online visibility.</p>
              
              <div class="notification-setting-group">
                <h3 class="minor-title">Profile Visibility</h3>
                <div class="radio-group">
                  <label class="radio-label"><input type="radio" name="visibility" value="public" checked> Public (Everyone)</label>
                  <label class="radio-label"><input type="radio" name="visibility" value="registered"> Registered Users Only</label>
                  <label class="radio-label"><input type="radio" name="visibility" value="private"> Private (Only connected roommates)</label>
                </div>
              </div>

              <div class="notification-setting-group" style="margin-top: 32px;">
                <h3 class="minor-title">Activity</h3>
                <div class="setting-row">
                  <span>Show online status</span>
                  <label class="toggle-switch">
                    <input type="checkbox" checked>
                    <span class="slider round"></span>
                  </label>
                </div>
                <div class="setting-row">
                  <span>Show read receipts</span>
                  <label class="toggle-switch">
                    <input type="checkbox" checked>
                    <span class="slider round"></span>
                  </label>
                </div>
                <div class="setting-row">
                  <span>Allow search engine indexing</span>
                  <label class="toggle-switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                  </label>
                </div>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'help'">
              <h1 class="main-title">Help & Support</h1>
              
              <div class="search-box" style="margin-bottom: 24px; max-width: 500px; border-radius: 12px; background: #fff; border: 1px solid #ccc; padding: 12px 16px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
                <input type="text" placeholder="How can we help?" style="border: none; outline: none; background: transparent; width: 100%; font-size: 1rem; margin-left: 8px; font-family: inherit;" />
              </div>

              <h2 class="minor-title">Quick Links</h2>
              <div class="settings-list-group" style="margin-bottom: 24px;">
                <div class="settings-list-item">
                  <div class="list-item-text">Reporting a listing or user</div>
                  <div class="list-item-arrow">›</div>
                </div>
                <div class="settings-list-item">
                  <div class="list-item-text">Understanding fees and payments</div>
                  <div class="list-item-arrow">›</div>
                </div>
                <div class="settings-list-item">
                  <div class="list-item-text">Safety and guidelines</div>
                  <div class="list-item-arrow">›</div>
                </div>
              </div>
              
              <button class="btn-dark" style="width: 100%; max-width: 500px; justify-content: center;">Contact Support</button>
            </template>

            <template v-else-if="activeSettingsTab === 'upgrade'">
              <div style="background: linear-gradient(145deg, #111, #333); color: white; border-radius: 20px; padding: 40px 32px; text-align: center; max-width: 500px; margin: 20px 0;">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="margin-bottom: 16px;"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                <h1 style="font-size: 1.8rem; margin-bottom: 12px; font-weight: 700;">Become a Landlord</h1>
                <p style="font-size: 1rem; color: #ddd; margin-bottom: 32px; line-height: 1.5;">List your properties, find reliable roommates, and earn money with zero upfront listing fees.</p>
                
                <div style="text-align: left; margin-bottom: 32px; font-size: 0.95rem; color: #ddd; display: flex; flex-direction: column; gap: 12px;">
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                    <span>Verified Landlord Badge</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                    <span>Priority Listing Placement</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                    <span>Premium Dashboard Analytics</span>
                  </div>
                </div>

                <button style="background: #fff; color: #111; border: none; width: 100%; padding: 14px; font-size: 1.05rem; font-weight: 700; border-radius: 12px; cursor: pointer;">Start Earning Today</button>
              </div>
            </template>

            <template v-else-if="activeSettingsTab === 'status'">
              <h1 class="main-title">Account Status</h1>
              <p style="color: #666; font-size: 0.95rem; margin-bottom: 24px;">View your current standing and account health.</p>

              <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; padding: 16px; display: flex; align-items: center; gap: 16px; margin-bottom: 32px; max-width: 500px;">
                <div style="background: #10b981; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
                </div>
                <div>
                  <h3 style="font-size: 1rem; color: #065f46; margin: 0 0 4px 0;">Active & Good Standing</h3>
                  <p style="font-size: 0.85rem; color: #047857; margin: 0;">Your account meets all community guidelines.</p>
                </div>
              </div>

              <h2 class="minor-title">Milestones</h2>
              <div class="settings-list-group">
                <div class="settings-list-item" style="cursor: default; background: #fafafa;">
                  <div class="list-item-text" style="color: #666;">Account Created</div>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                </div>
                <div class="settings-list-item" style="cursor: default; background: #fafafa;">
                  <div class="list-item-text" style="color: #666;">Identity Verified</div>
                  <div class="list-item-arrow" style="font-size: 0.85rem; color: #111; background: #eee; padding: 4px 8px; border-radius: 4px;">Pending</div>
                </div>
                <div class="settings-list-item" style="cursor: default; background: #fafafa;">
                  <div class="list-item-text" style="color: #666;">First Listing Uploaded</div>
                  <div class="list-item-arrow" style="font-size: 0.85rem; color: #111; background: #eee; padding: 4px 8px; border-radius: 4px;">Pending</div>
                </div>
              </div>
            </template>
          </div>
        </div>
      </template>

      <template v-else>
        <div class="empty-tab-content">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <p>This feature is coming soon!</p>
          <button class="btn-primary" @click="activeTab = 'home'">Go back Home</button>
        </div>
      </template>
    </main>

    <!-- Bottom Nav -->
    <nav class="bottom-nav">
      <button v-for="tab in tabs" :key="tab.id" class="nav-tab" :class="{ active: activeTab === tab.id }" @click="activeTab = tab.id">
        <component :is="tab.icon" />
        <span>{{ tab.label }}</span>
      </button>
    </nav>

    <!-- Filter Modal -->
    <Teleport to="body">
      <div v-if="filterOpen" class="filter-overlay" @click.self="filterOpen = false">
        <div class="filter-modal">
          <header class="filter-header">
            <button class="close-btn" @click="filterOpen = false">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
            <h2>Filters</h2>
            <div style="width: 32px"></div> <!-- spacer for centering -->
          </header>

          <div class="filter-body">
            <!-- Type of place -->
            <section class="filter-section">
              <h3>Type of place</h3>
              <div class="segmented-control">
                <button :class="{active: filterState.type === 'Any type'}" @click="filterState.type = 'Any type'">Any type</button>
                <button :class="{active: filterState.type === 'Room'}" @click="filterState.type = 'Room'">Room</button>
                <button :class="{active: filterState.type === 'Entire home'}" @click="filterState.type = 'Entire home'">Entire home</button>
              </div>
            </section>

            <!-- Price range -->
            <section class="filter-section">
              <h3>Price range</h3>
              <p class="filter-desc">Nightly prices before fees and taxes</p>
              <div class="price-inputs">
                <div class="price-field">
                  <label>Minimum</label>
                  <div class="price-input-wrapper">
                    <span class="currency">$</span>
                    <input type="number" v-model="filterState.priceMin" min="0" />
                  </div>
                </div>
                <div class="price-dash"></div>
                <div class="price-field">
                  <label>Maximum</label>
                  <div class="price-input-wrapper">
                    <span class="currency">$</span>
                    <input type="number" v-model="filterState.priceMax" :min="filterState.priceMin" />
                  </div>
                </div>
              </div>
            </section>

            <!-- Rooms and beds -->
            <section class="filter-section">
              <h3>Rooms and beds</h3>
              <div class="counter-row">
                <span>Bedrooms</span>
                <div class="counter">
                  <button @click="filterState.bedrooms > 0 ? filterState.bedrooms-- : null" :disabled="filterState.bedrooms === 0">-</button>
                  <span class="count-value">{{ filterState.bedrooms === 0 ? 'Any' : filterState.bedrooms }}</span>
                  <button @click="filterState.bedrooms++">+</button>
                </div>
              </div>
              <div class="counter-row">
                <span>Beds</span>
                <div class="counter">
                  <button @click="filterState.beds > 0 ? filterState.beds-- : null" :disabled="filterState.beds === 0">-</button>
                  <span class="count-value">{{ filterState.beds === 0 ? 'Any' : filterState.beds }}</span>
                  <button @click="filterState.beds++">+</button>
                </div>
              </div>
              <div class="counter-row">
                <span>Bathrooms</span>
                <div class="counter">
                  <button @click="filterState.bathrooms > 0 ? filterState.bathrooms-- : null" :disabled="filterState.bathrooms === 0">-</button>
                  <span class="count-value">{{ filterState.bathrooms === 0 ? 'Any' : filterState.bathrooms }}</span>
                  <button @click="filterState.bathrooms++">+</button>
                </div>
              </div>
            </section>

            <!-- Amenities -->
            <section class="filter-section border-none">
              <h3>Amenities</h3>
              <div class="amenities-grid">
                <button 
                  v-for="amenity in availableAmenities" :key="amenity.id"
                  class="amenity-chip"
                  :class="{active: filterState.amenities.includes(amenity.id)}"
                  @click="toggleAmenity(amenity.id)"
                >
                  <component :is="amenity.icon" class="amenity-icon" />
                  <span>{{ amenity.label }}</span>
                </button>
              </div>
            </section>
          </div>

          <footer class="filter-footer">
            <button class="clear-btn" @click="clearFilters">Clear all</button>
            <button class="show-btn" @click="filterOpen = false">Show properties</button>
          </footer>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, h, onMounted, watch } from 'vue'
import { properties } from '../store.js'

const searchQuery = ref('')
const mapContainer = ref(null)
const isMapLoaded = ref(false)
const mapMessage = ref('Loading Map...')

onMounted(() => {
  const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY;
  if (!apiKey || apiKey === 'your_api_key_here') {
    mapMessage.value = 'Please add your Google Maps API key to .env file'
    console.warn('Google Maps API key is missing. Please add VUE_APP_GOOGLE_MAPS_API_KEY to your .env file.');
    return;
  }

  if (window.google && window.google.maps) {
    initMap();
    return;
  }

  window.initGoogleMap = initMap;
  const script = document.createElement('script');
  script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initGoogleMap`;
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);
})

const importantPlaces = [
  { name: 'Royal Palace, Phnom Penh', lat: 11.5638, lng: 104.9315 },
  { name: 'Independence Monument, Phnom Penh', lat: 11.5564, lng: 104.9282 },
  { name: 'Angkor Wat, Siem Reap', lat: 13.4125, lng: 103.8667 },
  { name: 'Bayon Temple, Siem Reap', lat: 13.4413, lng: 103.8590 },
  { name: 'Koh Rong, Sihanoukville', lat: 10.7280, lng: 103.2427 },
  { name: 'Bokor Hill Station, Kampot', lat: 10.6214, lng: 104.0208 },
  { name: 'Preah Vihear Temple', lat: 14.3948, lng: 104.6800 },
];

function initMap() {
  isMapLoaded.value = true;
  if (!mapContainer.value) return;
  
  const map = new window.google.maps.Map(mapContainer.value, {
    center: { lat: 12.5657, lng: 104.9910 }, // Center of Cambodia
    zoom: 7, // Zoomed out to see the whole country
    disableDefaultUI: true,
    zoomControl: true,
  });

  importantPlaces.forEach(place => {
    new window.google.maps.Marker({
      position: { lat: place.lat, lng: place.lng },
      map,
      title: place.name,
      animation: window.google.maps.Animation.DROP,
    });
  });
}
const filterOpen  = ref(false)
const activeTab   = ref(sessionStorage.getItem('homeActiveTab') || 'home')
const activeSettingsTab = ref('profile')

const filterState = ref({
  type: 'Any type',
  priceMin: 50,
  priceMax: 610,
  bedrooms: 0,
  beds: 0,
  bathrooms: 0,
  amenities: []
})

const clearFilters = () => {
  filterState.value = {
    type: 'Any type',
    priceMin: 50,
    priceMax: 610,
    bedrooms: 0,
    beds: 0,
    bathrooms: 0,
    amenities: []
  }
}

const toggleAmenity = (id) => {
  const idx = filterState.value.amenities.indexOf(id)
  if (idx > -1) {
    filterState.value.amenities.splice(idx, 1)
  } else {
    filterState.value.amenities.push(id)
  }
}

const availableAmenities = [
  { id: 'wifi', label: 'Wifi', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('path', {d: 'M5 12.55a11 11 0 0114.08 0'}), h('path', {d: 'M1.42 9a16 16 0 0121.16 0'}), h('path', {d: 'M8.53 16.11a6 6 0 016.95 0'}), h('circle', {cx: 12, cy: 20, r: 1})]) } },
  { id: 'kitchen', label: 'Kitchen', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('path', {d: 'M18 6v6h-4V6h4zM6 6v6h4V6H6zM18 18v-4h-4v4h4zM6 18v-4h4v4H6z'}), h('path', {d: 'M2 12h20M12 2v20'})]) } },
  { id: 'washer', label: 'Washer', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('rect', {x: 4, y: 3, width: 16, height: 18, rx: 2}), h('circle', {cx: 12, cy: 13, r: 4}), h('path', {d: 'M8 7h8'})]) } },
  { id: 'ac', label: 'Air conditioning', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('path', {d: 'M12 2v20M8 6h8M6 10h12M4 14h16M8 18h8'})]) } },
  { id: 'parking', label: 'Free parking', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('rect', {x: 3, y: 4, width: 18, height: 16, rx: 2}), h('path', {d: 'M9 8h4a2 2 0 010 4H9v4M9 12h4'})]) } },
  { id: 'pool', label: 'Pool', icon: { render: () => h('svg', {width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 1.5}, [h('path', {d: 'M2 12h20M4 16c2 0 2 2 4 2s2-2 4-2 2 2 4 2 2-2 4-2M4 20c2 0 2 2 4 2s2-2 4-2 2 2 4 2 2-2 4-2'})]) } }
]

const currentUser = {
  name: 'Yim Vatey',
  avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&q=80',
}

const feedPosts = [
  {
    id: 1,
    author: 'Dave Rim',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80',
    image: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1000&q=85',
    imageAlt: 'Ocean waves under a cloudy sky',
    likes: 18,
    comments: 26,
    caption: 'Take some time to give yourself a rest',
  },
  {
    id: 2,
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: 'Wanna go grab a coffee with me?',
    likes: 10,
    comments: 12,
  },
  {
    id: 3,
    author: 'Dave Rim',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80',
    image: 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1000&q=85',
    imageAlt: 'Bright hotel bedroom with ocean view',
    likes: 32,
    comments: 12,
    caption: 'Just move in, Roommate please take care of me. ^^',
  },
  {
    id: 4,
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: "Need another roommate to split the bill. I'm broke :((",
    likes: 10,
    comments: 12,
  },
  {
    id: 5,
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: 'Our room still have a room left, looking for a roommate',
    likes: 10,
    comments: 12,
  },
]

const messages = [
  {
    name: 'Yim Vatey',
    preview: 'You: Where r you',
    time: '1m',
    avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&q=80',
  },
  {
    name: 'James Son',
    preview: 'You: Haha have fun',
    time: '2m',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
  },
  {
    name: 'Muy Leng',
    preview: 'I almost there',
    time: '5m',
    avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&q=80',
  },
  {
    name: 'Neav Sveita',
    preview: 'On my way there',
    time: '7m',
    avatar: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=100&q=80',
  },
  {
    name: 'Dave Rim',
    preview: 'Gogo !!!',
    time: '10m',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80',
  },
]

const roommates = [
  {
    name: 'Yim Vatey',
    avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&q=80',
  },
  {
    name: 'Muy Leng',
    avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&q=80',
  },
  {
    name: 'Neav Sveita',
    avatar: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=100&q=80',
  },
]

const friends = [
  {
    name: 'Erich Summer',
    avatar: 'https://images.unsplash.com/photo-1491349174775-aaafddd81942?w=100&q=80',
  },
  {
    name: 'David Pluash',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&q=80',
  },
  {
    name: 'John N',
    avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&q=80',
  },
]

const notifications = [
  {
    id: 1,
    name: 'Muy Leng',
    message: 'New Roommate',
    type: 'roommate',
    avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=80&q=80',
  },
  {
    id: 2,
    name: 'Dave Rim',
    message: 'Just post a new picture',
    type: 'unread',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=80&q=80',
  },
  {
    id: 3,
    name: 'James Son',
    message: 'Just post a text',
    type: 'unread',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&q=80',
  },
  {
    id: 4,
    name: 'James Son',
    message: 'Just post a text',
    type: 'unread',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&q=80',
  },
  {
    id: 5,
    name: 'Dave Rim',
    message: 'Just post a new video',
    type: 'none',
    seen: true,
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=80&q=80',
  },
  {
    id: 6,
    name: 'James Son',
    message: 'Just post a text',
    type: 'none',
    seen: true,
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&q=80',
  },
  {
    id: 7,
    name: 'Yim Vatey',
    message: 'React to your post',
    type: 'heart',
    seen: true,
    avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=80&q=80',
  },
  {
    id: 8,
    name: 'Neav Sveita',
    message: 'Comment on your post',
    type: 'comment',
    seen: true,
    avatar: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=80&q=80',
  },
  {
    id: 9,
    name: 'Neav Sveita',
    message: 'React to your post',
    type: 'heart',
    seen: true,
    avatar: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=80&q=80',
  },
  {
    id: 10,
    name: 'James Son',
    message: 'React to your post',
    type: 'heart',
    seen: false,
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&q=80',
  },
]

watch(activeTab, (val) => {
  sessionStorage.setItem('homeActiveTab', val)
})

const IconHome     = { render: () => h('svg', { class: 'home-icon', width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { class: 'home-body', d: 'M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z' }), h('path', { class: 'home-door', d: 'M9 21V12h6v9' })]) }
const IconHeart    = { render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { d: 'M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z' })]) }
const IconFeeds    = { render: () => h('svg', { class: 'feeds-icon', width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('rect', { class: 'feeds-frame', x: 3, y: 3, width: 18, height: 18, rx: 2 }), h('line', { class: 'feeds-line', x1: 5, y1: 9, x2: 19, y2: 9 }), h('line', { class: 'feeds-line', x1: 5, y1: 15, x2: 19, y2: 15 })]) }
const IconBell     = { render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { d: 'M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9' }), h('path', { d: 'M13.73 21a2 2 0 01-3.46 0' })]) }
const IconSettings = { render: () => h('svg', { class: 'settings-icon', width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { class: 'settings-gear', d: 'M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z' }), h('circle', { class: 'settings-center', cx: 12, cy: 12, r: 3 })]) }

const tabs = [
  { id: 'home',     label: 'Home',     icon: IconHome },
  { id: 'favorite', label: 'Favorite', icon: IconHeart },
  { id: 'feeds',    label: 'Feeds',    icon: IconFeeds },
  { id: 'noti',     label: 'Noti',     icon: IconBell },
  { id: 'settings', label: 'Settings', icon: IconSettings },
]

const favoriteProperties = computed(() => {
  const favs = properties.value.filter(p => p.liked)
  if (!searchQuery.value) return favs
  return favs.filter(p =>
    p.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    p.location.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

const filteredProperties = computed(() => {
  if (!searchQuery.value) return properties.value
  return properties.value.filter(p =>
    p.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    p.location.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.home-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  background: #fff;
  font-family: 'DM Sans', sans-serif;
  overflow: hidden;
}

/* ── TOP NAV ── */
.top-nav {
  display: flex; justify-content: space-between; align-items: center;
  padding: 16px 40px;
  background: #fff;
  border-bottom: 1px solid #ebebeb;
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

/* NAV RIGHT */
.nav-right { display: flex; align-items: center; gap: 8px; }
.host-text { font-size: 0.9rem; font-weight: 600; color: #222; cursor: pointer; padding: 12px; border-radius: 20px; transition: background 0.2s; }
.host-text:hover { background: #f7f7f7; }
.globe-btn {
  background: none; border: none; cursor: pointer; width: 44px; height: 44px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; color: #222; transition: background 0.2s;
}
.globe-btn:hover { background: #f7f7f7; }
.profile-menu {
  display: flex; align-items: center; gap: 12px; margin-left: 8px;
  border: 1px solid #dddddd; border-radius: 30px;
  padding: 4px 4px 4px 12px; cursor: pointer; transition: box-shadow 0.2s;
}
.profile-menu:hover { box-shadow: 0 2px 4px rgba(0,0,0,0.18); }
.avatar img {
  width: 32px; height: 32px; border-radius: 50%; object-fit: cover;
}
/* ── CONTENT ── */
.content {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 20px 52px 12px;
}

/* ── HERO ── */
.hero-section {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.hero-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(1.6rem, 2.4vw, 2.6rem);
  font-weight: 400;
  color: #111;
  line-height: 1.2;
  flex: 1;
  min-width: 200px;
}

.search-filter {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
  flex: 1;
  max-width: 320px;
  min-width: 160px;
}

.search-box {
  display: flex; align-items: center; gap: 7px;
  border: 1.5px solid #e8e8e8; border-radius: 50px;
  padding: 7px 12px; background: #fff; width: 100%;
}

.search-box input {
  border: none; outline: none;
  font-family: 'DM Sans', sans-serif; font-size: 0.8rem;
  color: #333; flex: 1; background: transparent; min-width: 0;
}
.search-box input::placeholder { color: #bbb; }

.filter-btn {
  display: flex; align-items: center; gap: 5px;
  padding: 6px 14px;
  border: 1.5px solid #e8e8e8; border-radius: 50px;
  background: #fff;
  font-family: 'DM Sans', sans-serif; font-size: 0.78rem; font-weight: 500; color: #333;
  cursor: pointer; white-space: nowrap; transition: border-color 0.2s;
}
.filter-btn:hover { border-color: #bbb; }

/* ── MAP ── */
.map-section {
  width: 100%;
  margin-bottom: 24px;
}

.map-wrapper {
  position: relative;
  width: 100%;
  height: 500px;
  border-radius: 16px;
  background: #f5f5f5;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

.map-container {
  width: 100%;
  height: 100%;
}

.map-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 0.9rem;
  font-weight: 500;
  text-align: center;
  padding: 20px;
  background: #f5f5f5;
  z-index: 10;
}

/* ── GRID — 3 columns, compact ── */
.listings {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px 12px;
}

/* ── CARD ── */
.property-card {
  display: flex; flex-direction: column; gap: 7px;
  cursor: pointer; min-width: 0;
}

/* KEY CHANGE: smaller aspect ratio = shorter image */
.card-carousel {
  position: relative; border-radius: 12px;
  overflow: hidden; aspect-ratio: 16/9; background: #f0f0f0;
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
.heart-btn:hover { transform: scale(1.1); }

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

/* ── CARD INFO ── */
.card-info { display: flex; flex-direction: column; gap: 4px; padding: 0 1px; }

.card-title-row {
  display: flex; justify-content: space-between; align-items: center; gap: 4px;
}

.card-name {
  font-weight: 600; font-size: 0.82rem; color: #111;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

.card-price { font-weight: 700; font-size: 0.82rem; color: #111; flex-shrink: 0; }

.card-location { display: flex; align-items: center; gap: 3px; font-size: 0.68rem; color: #aaa; }

.card-meta { display: flex; align-items: center; justify-content: space-between; }

.meta-tags { display: flex; gap: 3px; flex-wrap: wrap; }

.tag {
  display: flex; align-items: center; gap: 2px;
  padding: 2px 6px; background: #f5f5f5; border-radius: 50px;
  font-size: 0.62rem; color: #555; font-weight: 500;
}

.match { font-size: 0.68rem; color: #aaa; font-weight: 500; flex-shrink: 0; }

/* ── EMPTY TAB ── */
.empty-tab-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  gap: 16px;
  color: #666;
}
.empty-tab-content .btn-primary {
  padding: 10px 20px;
  background: #111;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-family: 'DM Sans', sans-serif;
  margin-top: 10px;
}

.empty-favorites {
  grid-column: 1 / -1;
  text-align: center;
  padding: 40px 20px;
  color: #666;
  font-size: 0.95rem;
}

/* ── FEEDS ── */
.feeds-section {
  width: min(922px, 100%);
  margin: 22px auto 96px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 305px;
  gap: 24px;
  align-items: start;
}

.feeds-main,
.mates-panel {
  min-width: 0;
}

.feeds-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.75rem;
  line-height: 1.15;
  font-weight: 800;
  color: #050505;
  margin: 0 0 14px;
}

.post-composer,
.feed-card,
.mates-card {
  background: #fff;
  border: 1px solid #dedede;
  border-radius: 8px;
}

.post-composer {
  overflow: hidden;
  margin-bottom: 18px;
}

.post-composer h2,
.mates-card h2 {
  font-size: 1rem;
  line-height: 1.2;
  font-weight: 800;
  color: #050505;
}

.post-composer h2 {
  padding: 22px 24px 6px;
}

.composer-row {
  min-height: 64px;
  display: grid;
  grid-template-columns: 28px minmax(0, 1fr) 30px;
  align-items: center;
  gap: 8px;
  border-top: 1px solid #eeeeee;
  padding: 12px 24px;
}

.composer-row input {
  min-width: 0;
  border: 0;
  outline: none;
  color: #111;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.72rem;
  background: transparent;
}

.composer-row input::placeholder {
  color: #969696;
}

.composer-add {
  width: 30px;
  height: 30px;
  border: 0;
  background: transparent;
  color: #9a9a9a;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.feed-card {
  padding: 12px 12px 14px;
  margin-bottom: 18px;
}

.feed-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}

.feed-author {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.feed-author span,
.mate-copy span {
  font-size: 0.75rem;
  line-height: 1.1;
  color: #050505;
  font-weight: 700;
}

.feed-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  flex-shrink: 0;
}

.feed-more {
  width: 28px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3px;
  border: 0;
  background: transparent;
  color: #999;
  cursor: pointer;
}

.feed-more span {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: currentColor;
}

.feed-image {
  width: 100%;
  height: 252px;
  display: block;
  object-fit: cover;
}

.feed-text {
  min-height: 44px;
  display: flex;
  align-items: center;
  color: #050505;
  font-size: 1.08rem;
  line-height: 1.25;
  font-weight: 500;
  margin: 4px 0 2px;
}

.feed-actions {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 9px 10px 0;
  color: #050505;
}

.feed-actions span {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.74rem;
  line-height: 1;
  font-weight: 500;
}

.feed-caption {
  padding: 4px 10px 0;
  color: #050505;
  font-size: 0.7rem;
  line-height: 1.25;
  font-weight: 500;
}

.mates-panel {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.mates-panel > .feeds-title {
  margin-bottom: 0;
}

.mates-card {
  padding: 24px;
}

.mates-card h2 {
  margin-bottom: 14px;
}

.mate-row {
  display: grid;
  grid-template-columns: 28px minmax(0, 1fr) auto;
  align-items: center;
  gap: 8px;
  min-height: 36px;
}

.mate-row + .mate-row {
  margin-top: 3px;
}

.mate-copy {
  min-width: 0;
}

.mate-copy p {
  margin-top: 1px;
  color: #8d8d8d;
  font-size: 0.58rem;
  line-height: 1.1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mate-row time,
.mate-row small {
  color: #969696;
  font-size: 0.62rem;
  line-height: 1;
  font-weight: 500;
}

/* ── NOTIFICATION ── */
.notification-section {
  width: min(548px, 100%);
  margin: 26px auto 86px;
}

.notification-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.75rem;
  line-height: 1.2;
  font-weight: 700;
  color: #050505;
  margin-bottom: 24px;
}

.notification-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.notification-item {
  min-height: 52px;
  display: grid;
  grid-template-columns: 36px 1fr 32px;
  align-items: center;
  gap: 12px;
  padding: 10px 20px 10px 24px;
  background: #f5f8fb;
  border-radius: 10px;
}

.notification-item.seen {
  background: #e1e6ea;
}

.notification-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
}

.notification-copy {
  min-width: 0;
}

.notification-copy h2 {
  font-size: 0.78rem;
  line-height: 1.15;
  font-weight: 700;
  color: #050505;
  margin: 0;
}

.notification-copy p {
  font-size: 0.63rem;
  line-height: 1.2;
  font-weight: 500;
  color: #050505;
  margin: 1px 0 0;
}

.notification-status {
  display: flex;
  align-items: center;
  justify-content: center;
  justify-self: end;
  color: #050505;
  width: 24px;
  height: 24px;
}

.notification-status.none {
  display: none;
}

.unread-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #4c7cff;
  display: block;
}

/* ── SETTINGS REDESIGN ── */
.settings-layout {
  display: flex;
  align-items: flex-start;
  min-height: 100%;
}

.settings-sidebar {
  width: 260px;
  flex-shrink: 0;
  border-right: 1px solid #ebebeb;
  padding-right: 24px;
  position: sticky;
  top: 0;
}

.settings-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 24px;
}

.sidebar-section {
  margin-bottom: 28px;
}

.sidebar-section h3 {
  font-size: 0.8rem;
  color: #888;
  font-weight: 600;
  margin-bottom: 12px;
}

.sidebar-menu {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sidebar-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 500;
  color: #333;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid transparent;
}

.sidebar-item:hover {
  background: #f7f7f7;
}

.sidebar-item.active {
  border-color: #e0e0e0;
  background: #fff;
  font-weight: 600;
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}

.settings-main {
  flex: 1;
  padding-left: 40px;
  max-width: 800px;
}

.main-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 32px;
}

.profile-header {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 40px;
}

.profile-lg-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-actions {
  display: flex;
  gap: 12px;
}

.btn-dark {
  background: #111;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
}

.btn-outline {
  background: transparent;
  color: #111;
  border: 1px solid #ccc;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
}

.profile-note {
  font-size: 0.85rem;
  color: #666;
  margin-top: 4px;
}

.sub-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #111;
  margin-bottom: 20px;
}

.minor-title {
  font-size: 1.05rem;
  font-weight: 600;
  color: #111;
  margin-bottom: 12px;
}

.sub-section {
  margin-bottom: 24px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 24px;
  margin-bottom: 32px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 0.9rem;
  color: #555;
  font-weight: 500;
}

.input-wrapper {
  display: flex;
  align-items: center;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 12px 16px;
  background: #fff;
}

.input-wrapper.with-icon {
  gap: 12px;
}

.input-wrapper svg {
  color: #555;
}

.input-wrapper input {
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 0.95rem;
  color: #111;
  font-weight: 500;
  width: 100%;
  background: transparent;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 0;
  color: #999;
  font-weight: 500;
  gap: 16px;
}

.settings-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.settings-tile {
  display: flex;
  align-items: center;
  padding: 16px;
  background: #fdfdfd;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s;
  max-width: 400px;
}
.settings-tile:hover {
  background: #f5f5f5;
  border-color: #e0e0e0;
}
.tile-icon {
  margin-right: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #111;
}
.tile-text {
  flex: 1;
  font-size: 0.95rem;
  font-weight: 500;
  color: #222;
}
.tile-arrow {
  font-size: 1.2rem;
  color: #999;
}

/* Toggle Switch */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
}
.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}
.slider {
  position: absolute;
  cursor: pointer;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 24px;
}
.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}
.toggle-switch input:checked + .slider {
  background-color: #111;
}
.toggle-switch input:checked + .slider:before {
  transform: translateX(20px);
}

/* Radio buttons */
.notification-setting-group {
  margin-bottom: 28px;
}
.setting-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.95rem;
  font-weight: 500;
  color: #111;
  margin-bottom: 12px;
}
.radio-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.radio-label {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.95rem;
  font-weight: 500;
  color: #111;
  cursor: pointer;
}
.radio-label input[type="radio"] {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-radius: 50%;
  position: relative;
  cursor: pointer;
}
.radio-label input[type="radio"]:checked {
  border-color: #111;
}
.radio-label input[type="radio"]:checked::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 10px;
  height: 10px;
  background: #111;
  border-radius: 50%;
}

/* List Groups (for Password & Security) */
.settings-list-group {
  display: flex;
  flex-direction: column;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  max-width: 500px;
}
.settings-list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: #fff;
  cursor: pointer;
  transition: background 0.2s;
  border-bottom: 1px solid #e0e0e0;
}
.settings-list-item:last-child {
  border-bottom: none;
}
.settings-list-item:hover {
  background: #f7f7f7;
}
.list-item-text {
  font-size: 0.95rem;
  font-weight: 500;
  color: #111;
}
.list-item-arrow {
  font-size: 1.2rem;
  color: #888;
}

/* ── FILTER MODAL ── */
.filter-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}
.filter-modal {
  background: #fff;
  border-radius: 16px;
  width: 100%;
  max-width: 560px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 12px 32px rgba(0,0,0,0.15);
  animation: modal-fade-up 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}
@keyframes modal-fade-up {
  from { opacity: 0; transform: translateY(20px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
.filter-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid #ebebeb;
}
.filter-header h2 {
  font-size: 1.1rem;
  font-weight: 700;
  color: #111;
  margin: 0;
}
.close-btn {
  background: none; border: none; cursor: pointer;
  width: 32px; height: 32px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #111; transition: background 0.2s;
}
.close-btn:hover { background: #f0f0f0; }

.filter-body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
}
.filter-section {
  padding-bottom: 24px;
  margin-bottom: 24px;
  border-bottom: 1px solid #ebebeb;
}
.filter-section.border-none {
  border-bottom: none; margin-bottom: 0; padding-bottom: 0;
}
.filter-section h3 {
  font-size: 1.25rem; font-weight: 600; color: #111; margin-bottom: 16px;
}

/* Segmented Control */
.segmented-control {
  display: flex;
  background: #f4f4f4;
  border-radius: 10px;
  padding: 4px;
}
.segmented-control button {
  flex: 1;
  padding: 10px 0;
  border: none;
  background: transparent;
  font-family: inherit; font-size: 0.95rem; font-weight: 500;
  color: #444; border-radius: 8px; cursor: pointer;
  transition: all 0.2s;
}
.segmented-control button.active {
  background: #fff; color: #111; font-weight: 600;
  box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}

/* Price Range Custom */
.filter-desc { font-size: 0.9rem; color: #666; margin-bottom: 16px; }
.price-inputs {
  display: flex; align-items: center; gap: 16px;
}
.price-field { flex: 1; }
.price-field label { display: block; font-size: 0.75rem; font-weight: 600; color: #777; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
.price-input-wrapper {
  display: flex; align-items: center;
  border: 1px solid #ccc; border-radius: 12px; padding: 12px 16px;
  background: #fff; transition: border-color 0.2s;
}
.price-input-wrapper:focus-within { border-color: #111; box-shadow: 0 0 0 1px #111; }
.currency { color: #111; font-size: 1.1rem; font-weight: 500; margin-right: 4px; }
.price-input-wrapper input {
  border: none; outline: none; font-family: inherit; font-size: 1.1rem; font-weight: 500; color: #111; width: 100%;
}
.price-dash { width: 16px; height: 1px; background: #ccc; margin-top: 24px; }

/* Counters */
.counter-row {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 16px;
}
.counter-row > span { font-size: 1.05rem; color: #111; font-weight: 400; }
.counter { display: flex; align-items: center; gap: 16px; }
.counter button {
  width: 32px; height: 32px; border-radius: 50%;
  border: 1px solid #ccc; background: #fff; color: #555;
  font-size: 1.2rem; display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: all 0.2s;
}
.counter button:hover:not(:disabled) { border-color: #111; color: #111; }
.counter button:disabled { opacity: 0.3; cursor: not-allowed; }
.count-value { font-size: 1.05rem; font-weight: 500; min-width: 24px; text-align: center; }

/* Amenities Grid */
.amenities-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
}
.amenity-chip {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1px solid #ccc; border-radius: 12px;
  background: #fff; color: #333; font-family: inherit; font-size: 0.95rem; font-weight: 500;
  cursor: pointer; transition: all 0.2s; text-align: left;
}
.amenity-chip:hover { border-color: #111; }
.amenity-chip.active {
  border-color: #111; background: #111; color: #fff;
}
.amenity-icon { opacity: 0.8; }
.amenity-chip.active .amenity-icon { opacity: 1; }

.filter-footer {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 24px; border-top: 1px solid #ebebeb; background: #fff;
}
.clear-btn {
  background: none; border: none; font-family: inherit; font-size: 0.95rem; font-weight: 600; text-decoration: underline; cursor: pointer; color: #111;
}
.show-btn {
  background: #111; color: #fff; border: none; font-family: inherit; font-size: 0.95rem; font-weight: 600;
  padding: 12px 24px; border-radius: 8px; cursor: pointer; transition: transform 0.1s;
}
.show-btn:active { transform: scale(0.97); }

/* ── BOTTOM NAV ── */
.bottom-nav {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 16px;
  background: #f2f2f2;
  border-radius: 40px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  z-index: 100;
  width: max-content;
  gap: 12px;
}

.nav-tab {
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  background: none; border: none; cursor: pointer;
  font-family: 'DM Sans', sans-serif; font-size: 0.55rem; color: #111; font-weight: 500;
  padding: 8px 14px; border-radius: 20px; transition: color 0.2s, background 0.2s;
  min-width: 60px;
}
.nav-tab.active { background: transparent; }
.nav-tab.active svg { fill: #111; stroke: #111; }
:deep(.nav-tab .home-icon .home-body),
:deep(.nav-tab .home-icon .home-door) {
  fill: none;
}
:deep(.nav-tab.active .home-icon .home-body) {
  fill: #111;
  stroke: #111;
}
:deep(.nav-tab.active .home-icon .home-door) {
  fill: none;
  stroke: #fff;
  stroke-width: 2.2;
}
:deep(.nav-tab .feeds-icon .feeds-frame),
:deep(.nav-tab .feeds-icon .feeds-line) {
  fill: none;
}
:deep(.nav-tab.active .feeds-icon .feeds-frame) {
  fill: #111;
  stroke: #111;
  stroke-width: 2;
}
:deep(.nav-tab.active .feeds-icon .feeds-line) {
  fill: none;
  stroke: #fff;
  stroke-width: 2.2;
}
:deep(.nav-tab .settings-icon .settings-gear),
:deep(.nav-tab .settings-icon .settings-center) {
  fill: none;
}
:deep(.nav-tab.active .settings-icon .settings-gear) {
  fill: #111;
  stroke: #111;
}
:deep(.nav-tab.active .settings-icon .settings-center) {
  fill: #fff;
  stroke: #111;
}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .listings { grid-template-columns: repeat(3, 1fr); gap: 10px 8px; }
  .content { padding: 16px 32px; }
  .top-nav { padding: 10px 32px; }
  .feeds-section {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .mates-panel {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .mates-panel > .feeds-title {
    grid-column: 1 / -1;
  }
}

@media (max-width: 640px) {
  .home-page { height: 100dvh; }
  .map-wrapper { height: 260px; border-radius: 12px; }
  .listings { grid-template-columns: 1fr; gap: 18px; }
  .content { padding: 14px 16px 112px; }
  .top-nav { padding: 10px 16px; gap: 12px; }
  .logo { gap: 6px; min-width: 0; }
  .logo-icon { width: 28px; height: 28px; }
  .logo-icon svg { width: 24px; height: 24px; }
  .logo-text { font-size: 1.05rem; white-space: nowrap; }
  .nav-right { gap: 4px; flex-shrink: 0; }
  .host-text { display: none; }
  .globe-btn { width: 36px; height: 36px; }
  .profile-menu {
    gap: 8px;
    margin-left: 2px;
    padding: 3px 3px 3px 10px;
  }
  .avatar img { width: 30px; height: 30px; }
  .hero-section { flex-direction: column; gap: 12px; margin-bottom: 18px; }
  .search-filter { max-width: 100%; min-width: unset; width: 100%; align-items: stretch; }
  .filter-btn { align-self: flex-end; }
  .hero-title { font-size: 1.45rem; min-width: 0; }
  .card-carousel { border-radius: 14px; }
  .card-name,
  .card-price { font-size: 0.9rem; }
  .card-location { font-size: 0.74rem; }
  .tag,
  .match { font-size: 0.7rem; }
  .feeds-section { margin: 16px auto 0; }
  .feeds-title { font-size: 1.45rem; }
  .post-composer h2,
  .mates-card { padding-left: 16px; padding-right: 16px; }
  .composer-row { padding-left: 16px; padding-right: 16px; }
  .feed-card { margin-bottom: 16px; }
  .feed-image { height: 190px; }
  .feed-text { font-size: 1rem; min-height: 58px; }
  .mates-panel { grid-template-columns: 1fr; }
  .notification-section { margin: 16px auto 0; }
  .notification-title { font-size: 1.45rem; margin-bottom: 16px; }
  .notification-item {
    grid-template-columns: 32px minmax(0, 1fr) 24px;
    gap: 10px;
    padding: 10px 12px;
  }
  .settings-layout { flex-direction: column; }
  .settings-sidebar { width: 100%; border-right: none; padding-right: 0; position: static; margin-bottom: 24px; }
  .settings-main { padding-left: 0; max-width: 100%; }
  .form-grid { grid-template-columns: 1fr; gap: 12px; margin-bottom: 24px; }
  .bottom-nav {
    bottom: max(12px, env(safe-area-inset-bottom));
    width: calc(100% - 24px);
    max-width: 420px;
    gap: 0;
    padding: 8px 10px;
  }
  .nav-tab {
    flex: 1;
    min-width: 0;
    padding: 6px 2px;
    font-size: 0.52rem;
  }
}

@media (max-width: 360px) {
  .content { padding-left: 12px; padding-right: 12px; }
  .top-nav { padding-left: 12px; padding-right: 12px; }
  .logo-text { font-size: 0.96rem; }
  .globe-btn { display: none; }
  .profile-menu { padding-left: 8px; }
  .bottom-nav { width: calc(100% - 16px); }
}
</style>
