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
        <span class="host-text" @click="activeTab = 'settings'; activeSettingsTab = 'upgrade'">Become a host</span>
        <div class="profile-menu" @click="activeTab = 'settings'; activeSettingsTab = 'profile'" aria-label="Go to Profile">
          <div class="avatar">
            <img :src="userProfile.avatar || defaultAvatar" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="User" />
          </div>
        </div>
      </div>
    </header>

    <!-- Scrollable Content -->
    <main class="content">
      <template v-if="activeTab === 'home'">
        <!-- URGENT VERIFICATION BANNER -->
        <div v-if="userProfile.verificationStatus !== 'verified'" class="urgent-verification-banner" @click="$router.push('/verify-account')">
          <div class="banner-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
              <line x1="12" y1="9" x2="12" y2="13"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg>
          </div>
          <div class="banner-text">
            <strong>Action Required: Verify Identity</strong>
            <p>You must complete your identity verification to ensure community safety.</p>
          </div>
          <button class="banner-btn">Verify Now</button>
        </div>

        <!-- Hero + Search -->
        <section class="hero-section">
        <h1 class="hero-title">Safety is what we priority,<br />Affordable is what we offer.</h1>
        <div class="search-filter">
          <div class="search-box">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#aaa" stroke-width="2">
              <circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" />
            </svg>
            <input v-model="searchQuery" type="text" placeholder="Search" @keydown.enter="navigateToSearch" />
          </div>
          <button class="filter-btn" @click="filterOpen = !filterOpen">
            Filter By
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path :d="filterOpen ? 'M18 15l-6-6-6 6' : 'M6 9l6 6 6-6'" />
            </svg>
          </button>
        </div>
      </section>

      <div class="home-content-wrapper">
        <!-- Property Grid -->
        <section class="listings">
        <div v-for="property in filteredProperties" :key="property.id" class="property-card" @click="handleCardClick($event, property.id, $router)">
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
                loading="lazy"
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
                <span class="tag" tabindex="0" data-tooltip="Bed">
                  <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
                  {{ property.beds }}
                </span>
                <span class="tag" tabindex="0" data-tooltip="Bath">
                  <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                  {{ property.baths }}
                </span>
                <span class="tag" tabindex="0" data-tooltip="Size of the room">
                  <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
                  {{ property.sqft }}
                </span>
              </div>
              <span class="match">{{ property.match }}%</span>
            </div>
          </div>
        </div>
        </section>

        <div v-if="hasMoreProperties || loadingMoreProperties" style="display: flex; justify-content: center; padding: 20px 0 40px;">
          <button 
            @click="loadMoreProperties" 
            :disabled="loadingMoreProperties"
            style="padding: 12px 24px; background: #111; color: #fff; border: none; border-radius: 20px; font-weight: 600; cursor: pointer; transition: background 0.2s; min-width: 160px;"
          >
            {{ loadingMoreProperties ? 'Loading...' : 'Load More Properties' }}
          </button>
        </div>
      </div>
        <GlobalFooter />
      </template>

      <template v-else-if="activeTab === 'favorite'">
        <div style="display: flex; flex-direction: column; min-height: calc(100vh - 70px);">
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
        <section class="listings" style="flex-grow: 1;">
          <div v-if="favoriteProperties.length === 0" class="empty-favorites">
            <p>No favorites yet. Start saving properties you love!</p>
          </div>
          <div v-for="property in favoriteProperties" :key="property.id" class="property-card" @click="handleCardClick($event, property.id, $router)">
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
                  <span class="tag" tabindex="0" data-tooltip="Bed">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
                    {{ property.beds }}
                  </span>
                  <span class="tag" tabindex="0" data-tooltip="Bath">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                    {{ property.baths }}
                  </span>
                  <span class="tag" tabindex="0" data-tooltip="Size of the room">
                    <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>
                    {{ property.sqft }}
                  </span>
                </div>
                <span class="match">{{ property.match }}%</span>
              </div>
            </div>
          </div>
        </section>
        <GlobalFooter style="margin-top: auto;" />
        </div>
      </template>

      <template v-else-if="activeTab === 'feeds'">
        <section class="feeds-section">
          <div class="feeds-main">
            <div class="feeds-header-wrapper">
              <h1 class="feeds-title">Feeds</h1>
              <div class="mobile-discover-search" @click="showMobileDiscover = true">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <span>Discover People...</span>
              </div>
            </div>

            <article class="post-composer">
              <h2>Post something</h2>
              <div class="composer-body">
                <div class="composer-row">
                  <img class="feed-avatar" :src="currentUser.avatar" :alt="currentUser.name" />
                  <textarea v-model="newPostText" placeholder="What's on your mind?" rows="2" class="composer-textarea"></textarea>
                </div>
                
                <!-- Image Preview Area -->
                <div v-if="newPostImage" class="composer-image-preview">
                  <img :src="newPostImage" alt="Preview" />
                  <button class="remove-preview-btn" @click="removeAttachedImage" type="button" aria-label="Remove image">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M18 6L6 18M6 6l12 12"/>
                    </svg>
                  </button>
                  <input v-model="newPostCaption" type="text" placeholder="Add a caption for your photo..." class="composer-caption-input" />
                </div>

                <div class="composer-actions">
                  <div class="composer-actions-left">
                    <button class="action-btn attachment-btn" @click="triggerPostImage" type="button">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                        <circle cx="8.5" cy="8.5" r="1.5"/>
                        <polyline points="21 15 16 10 5 21"/>
                      </svg>
                      <span>Photo</span>
                    </button>
                    <div class="location-input-wrapper">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
                      </svg>
                      <input v-model="newPostLocation" type="text" placeholder="Check in..." class="composer-location-input" />
                    </div>
                  </div>
                  <input type="file" ref="postImageInput" @change="handlePostImage" accept="image/*" style="display: none" />
                  
                  <button class="composer-submit-btn btn-dark" @click="createPost" :disabled="(!newPostText.trim() && !newPostImage) || isPosting" type="button">
                    {{ isPosting ? 'Posting...' : 'Post' }}
                  </button>
                </div>
              </div>
            </article>

            <article v-for="post in feedPosts" :key="post.id" class="feed-card">
              <header class="feed-card-header">
                <div class="feed-author">
                  <img class="feed-avatar" :src="post.avatar" :alt="post.author" />
                  <div class="feed-author-details">
                    <span class="feed-author-name">{{ post.author }}</span>
                    <span v-if="post.location" class="feed-author-location">📍 {{ post.location }}</span>
                  </div>
                </div>
                <button v-if="post.author === currentUser.name" class="feed-delete-btn" @click="deletePost(post.id)" aria-label="Delete post" type="button">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#e02424" stroke-width="2">
                    <polyline points="3 6 5 6 21 6"/>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                    <line x1="10" y1="11" x2="10" y2="17"/>
                    <line x1="14" y1="11" x2="14" y2="17"/>
                  </svg>
                </button>
                <button v-else class="feed-more" aria-label="More options" type="button">
                  <span></span><span></span><span></span>
                </button>
              </header>

              <img v-if="post.image" class="feed-image" :src="post.image" :alt="post.imageAlt" />
              <p v-if="post.text" class="feed-text">{{ post.text }}</p>

              <footer class="feed-actions">
                <span @click="toggleLike(post)" style="cursor: pointer;" class="action-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" :fill="post.likedByMe ? '#f40f0f' : 'none'" :stroke="post.likedByMe ? '#f40f0f' : 'currentColor'" stroke-width="2">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                  </svg>
                  {{ post.likes }}
                </span>
                <span @click="toggleComments(post)" style="cursor: pointer;" class="action-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15a4 4 0 0 1-4 4H7l-4 4V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z" />
                  </svg>
                  {{ post.commentsList ? post.commentsList.length : post.comments }}
                </span>
              </footer>
              <p v-if="post.caption" class="feed-caption">{{ post.caption }}</p>

              <!-- Comments Area -->
              <div v-if="post.showComments" class="feed-comments-section">
                <!-- Comments list -->
                <div class="comments-list" v-if="post.commentsList && post.commentsList.length">
                  <div v-for="(comment, index) in post.commentsList" :key="index" class="comment-item">
                    <img class="comment-avatar" :src="comment.avatar" :alt="comment.author" />
                    <div class="comment-bubble">
                      <div class="comment-author">{{ comment.author }}</div>
                      <div class="comment-text">{{ comment.text }}</div>
                    </div>
                  </div>
                </div>

                <!-- Add Comment input -->
                <div class="add-comment-row">
                  <img class="comment-avatar" :src="currentUser.avatar" :alt="currentUser.name" />
                  <div class="comment-input-wrapper">
                    <input 
                      v-model="post.newCommentText" 
                      type="text" 
                      placeholder="Write a comment..." 
                      @keydown.enter="submitComment(post)"
                    />
                    <button class="comment-send-btn" @click="submitComment(post)" :disabled="!post.newCommentText || !post.newCommentText.trim()" type="button">
                      Send
                    </button>
                  </div>
                </div>
              </div>
            </article>
          </div>

          <!-- Discover People Sidebar -->
          <aside class="discover-sidebar" :class="{ 'show-on-mobile': showMobileDiscover }">
            <div class="discover-title-wrapper">
              <h2 class="discover-title" @click="resetDiscoverSearch" style="cursor: pointer;" title="Reset Search">Discover People</h2>
              <button class="mobile-discover-close" @click="showMobileDiscover = false" type="button" aria-label="Close">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
              </button>
            </div>
            
            <div class="discover-search-wrapper">
              <button class="search-icon-btn" @click="discoverSearchActive = discoverSearchInput" type="button" aria-label="Search">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </button>
              <input 
                type="text" 
                v-model="discoverSearchInput" 
                @keydown.enter="discoverSearchActive = discoverSearchInput" 
                placeholder="Search" 
                class="discover-search-input" 
              />
            </div>

            <div class="discover-tabs">
              <button 
                v-for="tab in discoverTabs" 
                :key="tab"
                class="discover-tab-btn"
                :class="{ active: discoverTab === tab }"
                @click="discoverTab = tab"
              >
                {{ tab }}
              </button>
            </div>

            <!-- People Block -->
            <div class="discover-block" v-if="discoverTab === 'All' || discoverTab === 'People'">
              <div class="discover-block-header">
                <h3>People</h3>
                <button class="view-all-btn" @click="discoverTab = 'People'" type="button">View all</button>
              </div>
              <div class="discover-list">
                <div v-for="person in filteredDiscoverPeople" :key="'p-'+person.id" class="discover-item" @click="$router.push('/user-profile/' + person.id)">
                  <img :src="person.avatar" :alt="person.name" class="discover-avatar" />
                  <div class="discover-info">
                    <h4>{{ person.name }}</h4>
                    <p v-if="person.subtitle">{{ person.subtitle }}</p>
                  </div>
                  <button class="discover-action-btn" @click.stop="toggleFriend(person)">
                    <svg v-if="!person.isFriend" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="2">
                      <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                      <circle cx="8.5" cy="7" r="4"></circle>
                      <line x1="20" y1="8" x2="20" y2="14"></line>
                      <line x1="23" y1="11" x2="17" y2="11"></line>
                    </svg>
                    <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2">
                      <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                      <circle cx="8.5" cy="7" r="4"></circle>
                      <polyline points="17 11 19 13 23 9"></polyline>
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- Posts Block -->
            <div class="discover-block" v-if="discoverTab === 'All' || discoverTab === 'Posts'">
              <div class="discover-block-header">
                <h3>Posts</h3>
                <button class="view-all-btn" @click="discoverTab = 'Posts'" type="button">View all</button>
              </div>
              <div class="discover-list">
                <div v-for="post in filteredDiscoverPosts" :key="'post-'+post.id" class="discover-item post-item">
                  <img :src="post.image" :alt="post.title" class="discover-post-img" />
                  <div class="discover-info">
                    <h4>{{ post.title }}</h4>
                    <p>{{ post.author }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Roommates Block -->
            <div class="discover-block" v-if="discoverTab === 'All' || discoverTab === 'Roommates'">
              <div class="discover-block-header">
                <h3>Roommates</h3>
                <button class="view-all-btn" @click="discoverTab = 'Roommates'" type="button">View all</button>
              </div>
              <div class="discover-list">
                <div v-for="roommate in filteredDiscoverRoommates" :key="'r-'+roommate.id" class="discover-item" @click="$router.push('/user-profile/' + roommate.id)">
                  <img :src="roommate.avatar" :alt="roommate.name" class="discover-avatar" />
                  <div class="discover-info">
                    <h4>{{ roommate.name }}</h4>
                    <p>{{ roommate.subtitle }}</p>
                  </div>
                </div>
              </div>
            </div>

          </aside>

        </section>
      </template>

      <template v-else-if="activeTab === 'messages'">
        <section class="messages-tab-section full-screen-messenger">

          
          <div class="messenger-boxes-container" :class="{ 'has-chat': !!selectedChatRecipient }">
            <!-- Left Column: Chats List -->
            <div class="messenger-sidebar">
              <div class="messenger-header">
                <h2 class="messenger-title">Messages</h2>
              <button class="new-msg-btn" aria-label="New Message" @click="startNewMessage">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </button>
            </div>

            <div class="messenger-search">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#8e8e8e" stroke-width="2">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="M21 21l-4.35-4.35"></path>
              </svg>
              <input type="text" v-model="messengerSearchQuery" placeholder="Search Messenger" />
            </div>

            <div class="active-now-section">
              <div 
                class="active-users-scroller"
                ref="activeUsersScrollerRef"
                @mousedown="startDragActiveUsers"
                @mousemove="onDragActiveUsers"
                @mouseup="stopDragActiveUsers"
                @mouseleave="stopDragActiveUsers"
              >
                <div v-for="mate in roommates" :key="'active-'+mate.name" class="active-user-bubble" @click="openChat(mate.name)">
                  <div class="active-avatar-wrapper">
                    <img :src="mate.avatar" :alt="mate.name" class="active-avatar" />
                    <span class="online-dot"></span>
                  </div>
                  <span class="active-name">{{ mate.name.split(' ')[0] }}</span>
                </div>
                <div v-for="friend in friends" :key="'active-'+friend.name" class="active-user-bubble" @click="openChat(friend.name)">
                  <div class="active-avatar-wrapper">
                    <img :src="friend.avatar" :alt="friend.name" class="active-avatar" />
                    <span class="online-dot"></span>
                  </div>
                  <span class="active-name">{{ friend.name.split(' ')[0] }}</span>
                </div>
              </div>
            </div>

            <div class="recent-messages-section">
              <div class="chat-list">
                <div v-for="message in filteredMessages" :key="message.name" class="chat-row" :class="{ 'active-chat': selectedChatRecipient === message.name }" @click="openChat(message.name)">
                  <img class="chat-avatar" :src="message.avatar" :alt="message.name" />
                  <div class="chat-info">
                    <span class="chat-name">{{ message.name }}</span>
                    <p class="chat-preview">
                      <span class="preview-text" :class="{ 'unread-text': message.sender === 'them' }">{{ message.preview }}</span>
                      <span class="chat-time">· {{ message.time }}</span>
                    </p>
                  </div>
                  <div v-if="message.preview && !message.preview.startsWith('You:')" class="unread-indicator"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Center Column: Conversation -->
          <div class="messenger-main">
            <template v-if="selectedChatRecipient">
              <header class="chat-main-header">
                <div class="chat-header-user">
                  <button class="mobile-chat-back" @click="selectedChatRecipient = null" type="button" aria-label="Back">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="19" y1="12" x2="5" y2="12"></line>
                      <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                  </button>
                  <img :src="findAvatarByName(selectedChatRecipient)" :alt="selectedChatRecipient" class="chat-header-avatar" />
                  <div class="chat-header-info">
                    <h3>{{ selectedChatRecipient }}</h3>
                    <span class="chat-status">Active now</span>
                  </div>
                </div>
                <div class="chat-header-actions">
                  <svg @click="startAudioCall" style="cursor: pointer;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2c9efc" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  <svg @click="startVideoCall" style="cursor: pointer;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2c9efc" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>
                  <svg @click="toggleChatInfo" style="cursor: pointer;" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2c9efc" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                </div>
              </header>

              <div class="chat-main-messages" ref="chatMessagesContainer">
                <div v-for="(msg, i) in activeChatHistory" :key="i" class="chat-bubble-wrapper" :class="msg.sender">
                  <div class="chat-bubble">
                    <p>{{ msg.text }}</p>
                    <time>{{ msg.time }}</time>
                  </div>
                </div>
                <div v-if="activeChatHistory.length === 0" class="empty-chat-state">
                  <p>Say hi to {{ selectedChatRecipient }}!</p>
                </div>
              </div>

              <footer class="chat-main-footer">
                <div class="chat-input-wrapper">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8e8e8e" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
                  <input 
                    v-model="chatInputText" 
                    type="text" 
                    placeholder="Aa" 
                    @keydown.enter="sendChatMessage"
                  />
                  <button class="chat-send-btn" @click="sendChatMessage" :disabled="!chatInputText || !chatInputText.trim()" type="button">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" :stroke="(!chatInputText || !chatInputText.trim()) ? '#8e8e8e' : '#0084ff'" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                  </button>
                </div>
              </footer>
            </template>
            <template v-else>
              <div class="no-chat-selected">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#c0c0c0" stroke-width="1.5"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                <h2>Your Messages</h2>
                <p>Send private photos and messages to a friend.</p>
                <button class="btn-dark" @click="selectedChatRecipient = 'James Son'">Send Message</button>
              </div>
            </template>
          </div>

          <!-- Right Column: Details -->
          <div v-if="selectedChatRecipient" class="messenger-details">
            <div class="details-profile-header">
              <img :src="findAvatarByName(selectedChatRecipient)" :alt="selectedChatRecipient" class="details-avatar" />
              <h2>{{ selectedChatRecipient }}</h2>
              <span>Active now</span>
            </div>
            <div class="details-actions">
              <div class="chat-action-btn" @click="actionProfile" style="cursor: pointer;">
                <div class="icon-circle"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>
                <span>Profile</span>
              </div>
              <div class="chat-action-btn" @click="actionMute" style="cursor: pointer;">
                <div class="icon-circle"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"></path><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg></div>
                <span>Mute</span>
              </div>
              <div class="chat-action-btn" @click="actionSearch" style="cursor: pointer;">
                <div class="icon-circle"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
                <span>Search</span>
              </div>
            </div>
            
            <div class="details-accordion">
              <div class="accordion-item" @click="toggleAccordion('chatInfo')" style="cursor: pointer;">
                <span>Chat info</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" :style="{ transform: showAccordion.chatInfo ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
              <div v-if="showAccordion.chatInfo" style="padding: 0 16px 16px; font-size: 0.9rem; color: #666;">
                No additional chat info available.
              </div>
              <div class="accordion-item" @click="toggleAccordion('customize')" style="cursor: pointer;">
                <span>Customize chat</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" :style="{ transform: showAccordion.customize ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
              <div v-if="showAccordion.customize" style="padding: 0 16px 16px; font-size: 0.9rem; color: #666;">
                Chat customization options coming soon.
              </div>
              <div class="accordion-item" @click="toggleAccordion('media')" style="cursor: pointer;">
                <span>Media, files and links</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" :style="{ transform: showAccordion.media ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
              <div v-if="showAccordion.media" style="padding: 0 16px 16px; font-size: 0.9rem; color: #666;">
                No media files shared yet.
              </div>
              <div class="accordion-item" @click="toggleAccordion('privacy')" style="cursor: pointer;">
                <span>Privacy & support</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" :style="{ transform: showAccordion.privacy ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
              <div v-if="showAccordion.privacy" style="padding: 0 16px 16px; font-size: 0.9rem; color: #666;">
                Privacy settings are managed in your account.
              </div>
            </div>
          </div>
          </div>
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
                <div style="position: relative; display: inline-block;">
                  <img :src="userProfile.avatar || defaultAvatar" referrerpolicy="no-referrer" @error="setDefaultAvatar" alt="Profile" class="profile-lg-avatar" />
                  <button v-if="isEditingProfile" class="edit-photo-btn" @click="fileInput.click()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                  </button>
                </div>
                <input type="file" ref="fileInput" @change="handleFileChange" accept="image/*" style="display: none;" />
                
                <div class="profile-actions">
                  <template v-if="!isEditingProfile">
                    <button class="btn-dark" @click="isEditingProfile = true">Edit Profile</button>
                  </template>
                  <template v-else>
                    <button class="btn-dark" @click="saveProfileChanges" :disabled="isSavingProfile">
                      {{ isSavingProfile ? 'Saving...' : 'Save Changes' }}
                    </button>
                    <button class="btn-outline" @click="cancelProfileChanges">Cancel</button>
                  </template>
                </div>
                <p class="profile-note">Please noted that you can only change your profile only once a week</p>
              </div>

              <h2 class="sub-title">Personal Details</h2>
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">First Name</label>
                  <div class="input-wrapper" :class="{'editing-mode': isEditingProfile}">
                    <input type="text" v-model="userProfile.firstName" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <label class="form-label">Last Name</label>
                  <div class="input-wrapper" :class="{'editing-mode': isEditingProfile}">
                    <input type="text" v-model="userProfile.lastName" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    <input type="text" v-model="userProfile.dob" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    <input type="text" v-model="userProfile.gender" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                    <input type="text" v-model="userProfile.phone" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" /></svg>
                    <input type="text" v-model="userProfile.status" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                    <input type="text" v-model="userProfile.university" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
                    <input type="text" v-model="userProfile.job" :readonly="!isEditingProfile" />
                  </div>
                </div>
              </div>

              <h2 class="sub-title" style="margin-top: 24px;">Hobbies</h2>
              <div class="form-grid">
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
                    <input type="text" v-model="userProfile.hobbies.music" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"/><circle cx="16" cy="12" r="1"/><circle cx="18" cy="12" r="1"/><path d="M6 12h4M8 10v4"/></svg>
                    <input type="text" v-model="userProfile.hobbies.games" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20M2 12a14.5 14.5 0 0 0 20 0M12 2a14.5 14.5 0 0 1 0 20M2 12a14.5 14.5 0 0 1 20 0"/></svg>
                    <input type="text" v-model="userProfile.hobbies.sports" :readonly="!isEditingProfile" />
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>
                    <input type="text" v-model="userProfile.hobbies.movies" :readonly="!isEditingProfile" />
                  </div>
                </div>
              </div>

              <h2 class="sub-title" style="margin-top: 24px;">Address Details</h2>
              <div class="sub-section">
                <h3 class="minor-title">Room Detail</h3>
                <div class="form-grid">
                  <div class="form-group">
                    <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="8" y1="6" x2="8.01" y2="6"/><line x1="16" y1="6" x2="16.01" y2="6"/><line x1="8" y1="10" x2="8.01" y2="10"/><line x1="16" y1="10" x2="16.01" y2="10"/><line x1="8" y1="14" x2="8.01" y2="14"/><line x1="16" y1="14" x2="16.01" y2="14"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
                      <input type="text" v-model="userProfile.roomDetail" :readonly="!isEditingProfile" />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-wrapper with-icon" :class="{'editing-mode': isEditingProfile}">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l9 4v6c0 5.5-3.5 10.5-9 12-5.5-1.5-9-6.5-9-12V6l9-4z"/><circle cx="12" cy="11" r="3"/></svg>
                      <input type="text" v-model="userProfile.roommate" :readonly="!isEditingProfile" />
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="sub-section">
                <h3 class="minor-title">Mates</h3>
                <div class="form-grid">
                  <div class="form-group">
                    <div class="input-wrapper" :class="{'editing-mode': isEditingProfile}">
                      <input type="text" v-model="userProfile.mates[0]" :readonly="!isEditingProfile" />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-wrapper" :class="{'editing-mode': isEditingProfile}">
                      <input type="text" v-model="userProfile.mates[1]" :readonly="!isEditingProfile" />
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

                <button @click="$router.push('/login?role=landlord')" style="background: #fff; color: #111; border: none; width: 100%; padding: 14px; font-size: 1.05rem; font-weight: 700; border-radius: 12px; cursor: pointer;">Start Earning Today</button>
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
    <div class="bottom-nav-interaction-group" :class="{ 'mobile-visible': mobileHotbarVisible }">
      <div class="thin-bar-trigger" @click="mobileHotbarVisible = !mobileHotbarVisible"></div>
      <nav class="bottom-nav auto-hide" :class="{ 'mobile-visible': mobileHotbarVisible }">
        <button v-for="tab in tabs" :key="tab.id" class="nav-tab" :class="{ active: activeTab === tab.id }" @click="activeTab = tab.id">
          <component :is="tab.icon" />
          <span>{{ tab.label }}</span>
        </button>
      </nav>
    </div>

    <!-- Filter Modal -->
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
                  @click="toggleAmenity(amenity.id)">
                  <component :is="amenity.icon" class="amenity-icon" />
                  <span>{{ amenity.label }}</span>
                </button>
              </div>
            </section>
          </div>

          <footer class="filter-footer">
            <button class="clear-btn" @click="clearFilters">Clear all</button>
            <button class="show-btn" @click="applyFiltersAndNavigate">Show properties</button>
          </footer>
        </div>
      </div>


    <!-- Crop Modal -->
    <div v-if="showCropModal" class="crop-overlay" @click.self="cancelCrop">
      <div class="crop-modal">
        <header class="crop-header">
          <button type="button" class="crop-close-btn" @click="cancelCrop">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 6L6 18M6 6l12 12" />
            </svg>
          </button>
          <h2 class="crop-title">Adjust Photo</h2>
          <button type="button" class="crop-done-btn" @click="applyCrop">Done</button>
        </header>

        <div class="crop-body">
          <div class="crop-canvas-wrapper" ref="cropWrapperRef">
            <canvas
              ref="cropCanvasRef"
              @mousedown="onCropMouseDown"
              @mousemove="onCropMouseMove"
              @mouseup="onCropMouseUp"
              @mouseleave="onCropMouseUp"
              @touchstart.prevent="onCropTouchStart"
              @touchmove.prevent="onCropTouchMove"
              @touchend="onCropTouchEnd"
              @wheel.prevent="onCropWheel"
            ></canvas>
          </div>
        </div>

        <div class="crop-controls">
          <div class="control-group">
            <label class="control-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8" />
                <path d="M21 21l-4.35-4.35" />
                <path d="M11 8v6M8 11h6" />
              </svg>
              Zoom
            </label>
            <input
              type="range"
              min="0.5"
              max="3"
              step="0.01"
              v-model.number="cropZoom"
              class="range-slider"
              @input="drawCropCanvas"
            />
          </div>
          <div class="control-group">
            <label class="control-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21.5 2v6h-6M2.5 22v-6h6" />
                <path d="M2 11.5a10 10 0 0118.8-4.3M22 12.5a10 10 0 01-18.8 4.2" />
              </svg>
              Rotate
            </label>
            <input
              type="range"
              min="-180"
              max="180"
              step="1"
              v-model.number="cropRotation"
              class="range-slider"
              @input="drawCropCanvas"
            />
          </div>
          <div class="control-quick-actions">
            <button type="button" class="quick-action-btn" @click="rotateLeft">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2.5 2v6h6" />
                <path d="M2 11.5a10 10 0 0118.8-4.3" />
              </svg>
            </button>
            <button type="button" class="quick-action-btn" @click="rotateRight">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21.5 2v6h-6" />
                <path d="M22 11.5A10 10 0 003.2 7.2" />
              </svg>
            </button>
            <button type="button" class="quick-action-btn" @click="resetCrop">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 12a9 9 0 1018-0 9 9 0 00-18 0z" />
                <path d="M12 8v4l2 2" />
              </svg>
              Reset
            </button>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script setup>
import { ref, computed, h, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import GlobalFooter from '../../components/GlobalFooter.vue'
import { properties, globalSearchQuery, globalFilterState } from '../../store.js'
import { auth, db, storage } from '../../firebase'
import { doc, getDoc, setDoc, collection, getDocs, addDoc, onSnapshot, query, orderBy, where, deleteDoc, updateDoc, serverTimestamp, limit, startAfter } from 'firebase/firestore'
import { onAuthStateChanged } from 'firebase/auth'
import { ref as storageRef, uploadBytes, getDownloadURL, uploadString } from 'firebase/storage'

const router = useRouter()
const currentAuthUser = ref(null)

let postsUnsubscribe = null;
let authUnsubscribe = null;
let chatsUnsubscribe = null;
const searchQuery = globalSearchQuery

const lastPropertyDoc = ref(null);
const loadingMoreProperties = ref(false);
const hasMoreProperties = ref(true);

const loadMoreProperties = async () => {
  if (loadingMoreProperties.value || !hasMoreProperties.value) return;
  loadingMoreProperties.value = true;
  try {
    let q;
    if (lastPropertyDoc.value) {
      q = query(collection(db, 'properties'), limit(10), startAfter(lastPropertyDoc.value));
    } else {
      q = query(collection(db, 'properties'), limit(10));
    }
    const querySnapshot = await getDocs(q);
    
    if (querySnapshot.empty) {
      hasMoreProperties.value = false;
      return;
    }
    
    lastPropertyDoc.value = querySnapshot.docs[querySnapshot.docs.length - 1];
    
    const fetchedProperties = [];
    querySnapshot.forEach((doc) => {
      const data = doc.data();
      if (!data.images || data.images.length === 0) {
        data.images = ['https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80'];
        data.image = data.images[0];
      }
      data.activeSlide = 0;
      fetchedProperties.push({ id: doc.id, ...data });
    });
    
    fetchedProperties.sort((a, b) => {
      if (a.createdAt && b.createdAt) {
        return b.createdAt.toMillis() - a.createdAt.toMillis();
      }
      return 0;
    });

    const demoProperties = properties.value.filter(p => typeof p.id === 'number');
    const existingFetchedProperties = properties.value.filter(p => typeof p.id === 'string');
    
    properties.value = [...existingFetchedProperties, ...fetchedProperties, ...demoProperties];
    
    if (querySnapshot.docs.length < 10) {
       hasMoreProperties.value = false;
    }
  } catch (e) {
    console.error("Error fetching properties: ", e);
  } finally {
    loadingMoreProperties.value = false;
  }
}

const defaultAvatar = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23dfa37b'/><stop offset='100%' stop-color='%23c0784a'/></linearGradient></defs><circle cx='50' cy='50' r='50' fill='url(%23g)'/><circle cx='50' cy='37' r='17' fill='%23fff'/><path d='M50 58c-18 0-32 9-32 20v4h64v-4c0-11-14-20-32-20z' fill='%23fff'/></svg>"

function setDefaultAvatar(event) {
  event.target.src = defaultAvatar
}

const newPostText = ref('')
const newPostImage = ref(null)
const postImageInput = ref(null)
const newPostCaption = ref('')
const newPostLocation = ref('')
const isPosting = ref(false)

const isEditingProfile = ref(false)
const isSavingProfile = ref(false)
const fileInput = ref(null)

// --- Mobile Carousel Swipe & Click Prevention state ---
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
      if (property.activeSlide > 0) {
        property.activeSlide--
      }
    } else {
      if (property.activeSlide < property.images.length - 1) {
        property.activeSlide++
      }
    }
  }
}

function handleCardClick(event, propertyId, router) {
  if (isSwiping) {
    isSwiping = false
    return
  }
  router.push(`/property/${propertyId}`)
}

// --- Active Users Drag to Scroll ---
const activeUsersScrollerRef = ref(null)
let isDraggingActiveUsers = false
let startXActiveUsers = 0
let scrollLeftActiveUsers = 0

function startDragActiveUsers(e) {
  if (!activeUsersScrollerRef.value) return
  isDraggingActiveUsers = true
  startXActiveUsers = e.pageX - activeUsersScrollerRef.value.offsetLeft
  scrollLeftActiveUsers = activeUsersScrollerRef.value.scrollLeft
}

function onDragActiveUsers(e) {
  if (!isDraggingActiveUsers || !activeUsersScrollerRef.value) return
  e.preventDefault()
  const x = e.pageX - activeUsersScrollerRef.value.offsetLeft
  const walk = (x - startXActiveUsers) * 2
  activeUsersScrollerRef.value.scrollLeft = scrollLeftActiveUsers - walk
}

function stopDragActiveUsers() {
  isDraggingActiveUsers = false
}

const userProfile = ref({
  verificationStatus: 'unverified',
  avatar: '',
  firstName: 'Soth',
  lastName: 'Sokhomal',
  dob: '09 Oct, 2006',
  gender: 'Female',
  phone: '01156787697',
  status: 'In relationship',
  university: 'Camtech University',
  job: 'Software Developer',
  hobbies: { music: 'Music', games: 'Games', sports: 'Sports', movies: 'Movies' },
  roomDetail: 'Skystar Condo Premium',
  roommate: 'Skystar - Somnang',
  mates: ['Yim Vatey', 'Muy Leng']
})

// --- Photo upload & crop state ---
const showCropModal = ref(false)
const cropCanvasRef = ref(null)
const cropWrapperRef = ref(null)

const cropZoom = ref(1)
const cropRotation = ref(0)
const cropOffsetX = ref(0)
const cropOffsetY = ref(0)
const isDragging = ref(false)
const dragStartX = ref(0)
const dragStartY = ref(0)
const dragStartOffsetX = ref(0)
const dragStartOffsetY = ref(0)

// Touch pinch state
const lastTouchDist = ref(0)

let originalImage = null
let croppedBlob = null

function handleFileChange(event) {
  const file = event.target.files[0]
  if (!file) return

  // Validate file size (10MB max)
  if (file.size > 10 * 1024 * 1024) {
    alert('File size must be less than 10MB.')
    return
  }

  const reader = new FileReader()
  reader.onload = (e) => {
    const img = new Image()
    img.onload = () => {
      originalImage = img
      cropZoom.value = 1
      cropRotation.value = 0
      cropOffsetX.value = 0
      cropOffsetY.value = 0
      showCropModal.value = true
      nextTick(() => {
        setTimeout(() => {
          initCropCanvas()
        }, 100)
      })
    }
    img.src = e.target.result
  }
  reader.readAsDataURL(file)

  // Reset input so same file can be re-selected
  if (fileInput.value) fileInput.value.value = null
}

function initCropCanvas() {
  const canvas = cropCanvasRef.value
  const wrapper = cropWrapperRef.value
  if (!canvas || !wrapper) {
    setTimeout(() => initCropCanvas(), 50)
    return
  }

  const wrapperWidth = wrapper.clientWidth || 360
  const size = Math.min(wrapperWidth, 400)
  canvas.width = size * 2 // HiDPI
  canvas.height = size * 2
  canvas.style.width = size + 'px'
  canvas.style.height = size + 'px'

  drawCropCanvas()
}

function drawCropCanvas() {
  const canvas = cropCanvasRef.value
  if (!canvas || !originalImage) return

  const ctx = canvas.getContext('2d')
  const w = canvas.width
  const h = canvas.height
  const cx = w / 2
  const cy = h / 2
  const circleRadius = Math.min(w, h) * 0.4

  ctx.clearRect(0, 0, w, h)

  ctx.save()
  ctx.translate(cx + cropOffsetX.value * 2, cy + cropOffsetY.value * 2)
  ctx.rotate((cropRotation.value * Math.PI) / 180)
  ctx.scale(cropZoom.value, cropZoom.value)

  const imgAspect = originalImage.width / originalImage.height
  let drawW, drawH
  if (imgAspect > 1) {
    drawH = h * 0.8
    drawW = drawH * imgAspect
  } else {
    drawW = w * 0.8
    drawH = drawW / imgAspect
  }

  ctx.drawImage(originalImage, -drawW / 2, -drawH / 2, drawW, drawH)
  ctx.restore()

  ctx.save()
  ctx.fillStyle = 'rgba(0, 0, 0, 0.55)'
  ctx.fillRect(0, 0, w, h)

  ctx.globalCompositeOperation = 'destination-out'
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.fill()
  ctx.restore()

  ctx.save()
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.7)'
  ctx.lineWidth = 3
  ctx.beginPath()
  ctx.arc(cx, cy, circleRadius, 0, Math.PI * 2)
  ctx.stroke()
  ctx.restore()
}

function onCropMouseDown(e) {
  isDragging.value = true
  dragStartX.value = e.clientX
  dragStartY.value = e.clientY
  dragStartOffsetX.value = cropOffsetX.value
  dragStartOffsetY.value = cropOffsetY.value
}

function onCropMouseMove(e) {
  if (!isDragging.value) return
  cropOffsetX.value = dragStartOffsetX.value + (e.clientX - dragStartX.value)
  cropOffsetY.value = dragStartOffsetY.value + (e.clientY - dragStartY.value)
  drawCropCanvas()
}

function onCropMouseUp() {
  isDragging.value = false
}

function onCropTouchStart(e) {
  if (e.touches.length === 1) {
    isDragging.value = true
    dragStartX.value = e.touches[0].clientX
    dragStartY.value = e.touches[0].clientY
    dragStartOffsetX.value = cropOffsetX.value
    dragStartOffsetY.value = cropOffsetY.value
  } else if (e.touches.length === 2) {
    isDragging.value = false
    const dx = e.touches[0].clientX - e.touches[1].clientX
    const dy = e.touches[0].clientY - e.touches[1].clientY
    lastTouchDist.value = Math.sqrt(dx * dx + dy * dy)
  }
}

function onCropTouchMove(e) {
  if (e.touches.length === 1 && isDragging.value) {
    cropOffsetX.value = dragStartOffsetX.value + (e.touches[0].clientX - dragStartX.value)
    cropOffsetY.value = dragStartOffsetY.value + (e.touches[0].clientY - dragStartY.value)
    drawCropCanvas()
  } else if (e.touches.length === 2) {
    const dx = e.touches[0].clientX - e.touches[1].clientX
    const dy = e.touches[0].clientY - e.touches[1].clientY
    const dist = Math.sqrt(dx * dx + dy * dy)
    if (lastTouchDist.value > 0) {
      const scale = dist / lastTouchDist.value
      cropZoom.value = Math.max(0.5, Math.min(3, cropZoom.value * scale))
      drawCropCanvas()
    }
    lastTouchDist.value = dist
  }
}

function onCropTouchEnd() {
  isDragging.value = false
  lastTouchDist.value = 0
}

function onCropWheel(e) {
  const delta = e.deltaY > 0 ? -0.05 : 0.05
  cropZoom.value = Math.max(0.5, Math.min(3, cropZoom.value + delta))
  drawCropCanvas()
}

function rotateLeft() {
  cropRotation.value = ((cropRotation.value - 90 + 180) % 360) - 180
  drawCropCanvas()
}

function rotateRight() {
  cropRotation.value = ((cropRotation.value + 90 + 180) % 360) - 180
  drawCropCanvas()
}

function resetCrop() {
  cropZoom.value = 1
  cropRotation.value = 0
  cropOffsetX.value = 0
  cropOffsetY.value = 0
  drawCropCanvas()
}

function cancelCrop() {
  showCropModal.value = false
  originalImage = null
}

function applyCrop() {
  if (!originalImage || !cropCanvasRef.value) return

  const sourceCanvas = cropCanvasRef.value
  const w = sourceCanvas.width
  const h = sourceCanvas.height
  const cx = w / 2
  const cy = h / 2
  const circleRadius = Math.min(w, h) * 0.4

  const outputSize = Math.round(circleRadius * 2)
  const outputCanvas = document.createElement('canvas')
  outputCanvas.width = outputSize
  outputCanvas.height = outputSize
  const outCtx = outputCanvas.getContext('2d')

  const tempCanvas = document.createElement('canvas')
  tempCanvas.width = w
  tempCanvas.height = h
  const tempCtx = tempCanvas.getContext('2d')

  tempCtx.translate(cx + cropOffsetX.value * 2, cy + cropOffsetY.value * 2)
  tempCtx.rotate((cropRotation.value * Math.PI) / 180)
  tempCtx.scale(cropZoom.value, cropZoom.value)

  const imgAspect = originalImage.width / originalImage.height
  let drawW, drawH
  if (imgAspect > 1) {
    drawH = h * 0.8
    drawW = drawH * imgAspect
  } else {
    drawW = w * 0.8
    drawH = drawW / imgAspect
  }
  tempCtx.drawImage(originalImage, -drawW / 2, -drawH / 2, drawW, drawH)

  outCtx.beginPath()
  outCtx.arc(outputSize / 2, outputSize / 2, outputSize / 2, 0, Math.PI * 2)
  outCtx.closePath()
  outCtx.clip()

  outCtx.drawImage(
    tempCanvas,
    cx - circleRadius,
    cy - circleRadius,
    circleRadius * 2,
    circleRadius * 2,
    0,
    0,
    outputSize,
    outputSize
  )

  outputCanvas.toBlob(
    (blob) => {
      if (!blob) {
        alert('Failed to crop image. Please try again.')
        return
      }
      croppedBlob = blob
      userProfile.value.avatar = URL.createObjectURL(blob)
      showCropModal.value = false
      originalImage = null
    },
    'image/jpeg',
    0.9
  )
}

async function saveProfileChanges() {
  const user = auth.currentUser;
  if (!user) return;
  
  isSavingProfile.value = true;
  try {
    let avatarUrl = userProfile.value.avatar;

    // Upload cropped photo to Firebase Storage
    if (croppedBlob) {
      const fileRef = storageRef(storage, `users/${user.uid}/profilePic`);
      await uploadBytes(fileRef, croppedBlob);
      avatarUrl = await getDownloadURL(fileRef);
      userProfile.value.avatar = avatarUrl;
      croppedBlob = null; // Reset
    }

    await setDoc(doc(db, 'users', user.uid), {
      firstName: userProfile.value.firstName,
      lastName: userProfile.value.lastName,
      avatar: avatarUrl,
      profile: {
        dob: userProfile.value.dob,
        gender: userProfile.value.gender,
        phone: userProfile.value.phone,
        status: userProfile.value.status,
        university: userProfile.value.university,
        job: userProfile.value.job,
        hobbies: userProfile.value.hobbies
      }
    }, { merge: true });
    
    isEditingProfile.value = false;
  } catch (err) {
    console.error("Error saving profile:", err);
    alert("Failed to save profile.");
  } finally {
    isSavingProfile.value = false;
  }
}

async function cancelProfileChanges() {
  isEditingProfile.value = false;
  croppedBlob = null;
  const user = auth.currentUser;
  if (user) {
    await fetchUserProfile(user);
  }
}

async function fetchUserProfile(user) {
  try {
    const docRef = doc(db, 'users', user.uid);
    const docSnap = await getDoc(docRef);
    if (docSnap.exists()) {
      const data = docSnap.data();
      if (data.firstName) userProfile.value.firstName = data.firstName;
      if (data.lastName) userProfile.value.lastName = data.lastName;
      if (data.avatar) userProfile.value.avatar = data.avatar;
      if (data.verificationStatus) userProfile.value.verificationStatus = data.verificationStatus;
      
      if (data.profile) {
        if (data.profile.dob) userProfile.value.dob = data.profile.dob;
        if (data.profile.gender) userProfile.value.gender = data.profile.gender;
        if (data.profile.phone) userProfile.value.phone = data.profile.phone;
        if (data.profile.status) userProfile.value.status = data.profile.status;
        if (data.profile.university) userProfile.value.university = data.profile.university;
        if (data.profile.job) userProfile.value.job = data.profile.job;
        
        if (data.profile.hobbies) {
          if (data.profile.hobbies.music) userProfile.value.hobbies.music = data.profile.hobbies.music;
          if (data.profile.hobbies.games) userProfile.value.hobbies.games = data.profile.hobbies.games;
          if (data.profile.hobbies.sports) userProfile.value.hobbies.sports = data.profile.hobbies.sports;
          if (data.profile.hobbies.movies) userProfile.value.hobbies.movies = data.profile.hobbies.movies;
        }
      }
    }
  } catch (err) {
    console.error("Error fetching user profile:", err);
  }
}

onMounted(async () => {
  const postsQuery = query(collection(db, 'feed_posts'), orderBy('timestamp', 'desc'));
  postsUnsubscribe = onSnapshot(postsQuery, (snapshot) => {
    const newPosts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    const mappedNewPosts = newPosts.map(p => {
      const existing = feedPosts.value.find(e => e.id === p.id)
      if (existing) {
        return { ...p, showComments: existing.showComments, newCommentText: existing.newCommentText }
      }
      return { ...p, showComments: false, newCommentText: '' }
    });
    
    const currentDemoPosts = feedPosts.value.filter(p => typeof p.id === 'string' && p.id.startsWith('demo-'));
    const demoPostsToKeep = currentDemoPosts.length > 0 ? currentDemoPosts : demoFeedPosts;
    
    feedPosts.value = [...mappedNewPosts, ...demoPostsToKeep];
  });

  try {
    // Reset pagination state on mount
    lastPropertyDoc.value = null;
    hasMoreProperties.value = true;
    
    // Clear previously fetched properties (strings) but keep demo (numbers)
    const demoProperties = properties.value.filter(p => typeof p.id === 'number');
    properties.value = [...demoProperties];
    
    await loadMoreProperties();
  } catch (e) {
    console.error("Error init properties: ", e)
  }

  // Fetch real profile from Firebase
  authUnsubscribe = onAuthStateChanged(auth, async (user) => {
    if (user) {
      currentAuthUser.value = user;
      await fetchUserProfile(user);
      
      if (chatsUnsubscribe) chatsUnsubscribe();
      chatsUnsubscribe = onSnapshot(
        query(collection(db, 'chats'), where('participants', 'array-contains', user.uid)),
        (snapshot) => {
          snapshot.forEach(doc => {
            const data = doc.data();
            const otherParticipant = data.participants.find(p => p !== user.uid);
            if (otherParticipant && !chats.value[otherParticipant]) {
              chats.value[otherParticipant] = [];
            }
          });
        }
      );
    }
  });
})

onUnmounted(() => {
  if (postsUnsubscribe) postsUnsubscribe();
  if (authUnsubscribe) authUnsubscribe();
  if (chatsUnsubscribe) chatsUnsubscribe();
  if (messagesUnsubscribe) messagesUnsubscribe();
})
const filterOpen  = ref(false)
const activeTab   = ref(sessionStorage.getItem('homeActiveTab') || 'home')
const activeSettingsTab = ref('profile')

const filterState = globalFilterState

const navigateToSearch = () => {
  router.push('/search')
}

const applyFiltersAndNavigate = () => {
  filterOpen.value = false
  navigateToSearch()
}


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

const currentUser = computed(() => {
  const firstName = userProfile.value.firstName || '';
  const lastName = userProfile.value.lastName || '';
  return {
    name: `${firstName} ${lastName}`.trim() || 'Anonymous User',
    avatar: userProfile.value.avatar || defaultAvatar
  }
})

const demoFeedPosts = [
  {
    id: 'demo-1',
    author: 'Dave Rim',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80',
    image: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1000&q=85',
    imageAlt: 'Ocean waves under a cloudy sky',
    likes: 18,
    likedByMe: false,
    showComments: false,
    newCommentText: '',
    commentsList: [
      { author: 'James Son', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80', text: 'Take care Dave! Stunning photo.' }
    ],
    caption: 'Take some time to give yourself a rest',
  },
  {
    id: 'demo-2',
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: 'Wanna go grab a coffee with me?',
    likes: 10,
    likedByMe: false,
    showComments: false,
    newCommentText: '',
    commentsList: [
      { author: 'Dave Rim', avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80', text: 'Sure, where to?' }
    ],
  },
  {
    id: 'demo-3',
    author: 'Dave Rim',
    avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80',
    image: 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1000&q=85',
    imageAlt: 'Bright hotel bedroom with ocean view',
    likes: 32,
    likedByMe: false,
    showComments: false,
    newCommentText: '',
    commentsList: [],
    caption: 'Just move in, Roommate please take care of me. ^^',
  },
  {
    id: 'demo-4',
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: "Need another roommate to split the bill. I'm broke :((",
    likes: 10,
    likedByMe: false,
    showComments: false,
    newCommentText: '',
    commentsList: [],
  },
  {
    id: 'demo-5',
    author: 'James Son',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80',
    text: 'Our room still have a room left, looking for a roommate',
    likes: 10,
    likedByMe: false,
    showComments: false,
    newCommentText: '',
    commentsList: [],
  },
]

const feedPosts = ref([...demoFeedPosts])

// --- Discover People State ---
const mobileHotbarVisible = ref(false)
const showMobileDiscover = ref(false)
const discoverSearchInput = ref('')
const discoverSearchActive = ref('')
const discoverTab = ref('All')
const discoverTabs = ['All', 'People', 'Posts', 'Roommates', 'Friends']

const discoverPeople = ref([
  { id: 1, name: 'Yim Vatey', subtitle: '', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80', isFriend: false },
  { id: 2, name: 'James Son', subtitle: '', avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&q=80', isFriend: false },
  { id: 3, name: 'Muy Leng', subtitle: '', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&q=80', isFriend: false },
  { id: 4, name: 'Neav Sveita', subtitle: '', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80', isFriend: false },
  { id: 5, name: 'Dave Rim', subtitle: '', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&q=80', isFriend: false }
])

const discoverPosts = ref([
  { id: 1, title: 'Take some time to give yourself a rest', author: 'Erich Summer', image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=150&q=80' },
  { id: 2, title: 'Sunset after a long day', author: 'Dave Rim', image: 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=150&q=80' },
  { id: 3, title: 'Coffee and good talk', author: 'Erich Summer', image: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=150&q=80' }
])

const discoverRoommates = ref([
  { id: 1, name: 'Yim Vatey', subtitle: 'Roommate', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80', isFriend: false }
])

const resetDiscoverSearch = () => {
  discoverSearchInput.value = ''
  discoverSearchActive.value = ''
  discoverTab.value = 'All'
}

const fuzzyMatch = (target, query) => {
  if (!target || !query) return false
  const t = target.toLowerCase()
  const q = query.toLowerCase().trim()
  if (t.includes(q) || q.includes(t)) return true
  
  const tWords = t.split(/[\s\W]+/)
  const qWords = q.split(/[\s\W]+/)
  
  for (const qw of qWords) {
    if (qw.length < 3) continue
    for (const tw of tWords) {
      if (tw.length < 3) continue
      if (tw.includes(qw) || qw.includes(tw)) return true
    }
  }
  return false
}

const filteredDiscoverPeople = computed(() => {
  const q = discoverSearchActive.value
  if (!q.trim()) return discoverPeople.value
  return discoverPeople.value.filter(p => fuzzyMatch(p.name, q) || fuzzyMatch(p.subtitle, q))
})

const toggleFriend = (person) => {
  person.isFriend = !person.isFriend
}

const filteredDiscoverPosts = computed(() => {
  const q = discoverSearchActive.value
  if (!q.trim()) return discoverPosts.value
  return discoverPosts.value.filter(p => fuzzyMatch(p.title, q) || fuzzyMatch(p.author, q))
})

const filteredDiscoverRoommates = computed(() => {
  const q = discoverSearchActive.value
  if (!q.trim()) return discoverRoommates.value
  return discoverRoommates.value.filter(r => fuzzyMatch(r.name, q) || fuzzyMatch(r.subtitle, q))
})

const triggerPostImage = () => {
  if (postImageInput.value) {
    postImageInput.value.click()
  }
}

const handlePostImage = (event) => {
  const file = event.target.files[0]
  if (!file) return
  const reader = new FileReader()
  reader.onload = (e) => {
    newPostImage.value = e.target.result
  }
  reader.readAsDataURL(file)
}

const removeAttachedImage = () => {
  newPostImage.value = null
  if (postImageInput.value) {
    postImageInput.value.value = null
  }
}

const createPost = async () => {
  if (!newPostText.value.trim() && !newPostImage.value) return
  if (isPosting.value) return
  
  isPosting.value = true
  try {
    let finalImageUrl = null
    if (newPostImage.value) {
      const imgRef = storageRef(storage, `feed_images/${Date.now()}_${Math.random().toString(36).substring(7)}`)
      await uploadString(imgRef, newPostImage.value, 'data_url')
      finalImageUrl = await getDownloadURL(imgRef)
    }

    const newPost = {
      author: currentUser.value.name,
      avatar: currentUser.value.avatar,
      text: newPostText.value.trim(),
      image: finalImageUrl,
      imageAlt: finalImageUrl ? 'Attached Photo' : undefined,
      caption: newPostCaption.value.trim(),
      location: newPostLocation.value.trim(),
      likes: 0,
      likedByMe: false,
      commentsList: [],
      timestamp: serverTimestamp()
    }
    
    await addDoc(collection(db, 'feed_posts'), newPost)

    newPostText.value = ''
    newPostCaption.value = ''
    newPostLocation.value = ''
    newPostImage.value = null
    if (postImageInput.value) {
      postImageInput.value.value = null
    }
  } catch (err) {
    console.error("Error creating post:", err)
    alert("Failed to create post. Please try again.")
  } finally {
    isPosting.value = false
  }
}

const deletePost = async (postId) => {
  if (confirm("Are you sure you want to delete this post?")) {
    if (typeof postId === 'string' && postId.startsWith('demo-')) {
      feedPosts.value = feedPosts.value.filter(p => p.id !== postId)
      return
    }
    try {
      await deleteDoc(doc(db, 'feed_posts', postId))
    } catch (err) {
      console.error("Error deleting post:", err)
    }
  }
}

const toggleLike = async (post) => {
  let newLikes = post.likes
  let newLikedByMe = post.likedByMe
  
  if (post.likedByMe) {
    newLikes = Math.max(0, post.likes - 1)
    newLikedByMe = false
  } else {
    newLikes++
    newLikedByMe = true
  }
  
  post.likes = newLikes
  post.likedByMe = newLikedByMe
  
  if (typeof post.id === 'string' && post.id.startsWith('demo-')) return;
  
  try {
    await updateDoc(doc(db, 'feed_posts', post.id), {
      likes: newLikes,
      likedByMe: newLikedByMe
    })
  } catch (err) {
    console.error("Error toggling like:", err)
  }
}

const toggleComments = (post) => {
  post.showComments = !post.showComments
}

const submitComment = async (post) => {
  if (!post.newCommentText || !post.newCommentText.trim()) return
  const newComment = {
    author: currentUser.value.name,
    avatar: currentUser.value.avatar,
    text: post.newCommentText.trim()
  }
  
  const updatedComments = [...(post.commentsList || []), newComment]
  post.newCommentText = ''
  
  if (typeof post.id === 'string' && post.id.startsWith('demo-')) {
    post.commentsList = updatedComments
    return
  }
  
  try {
    await updateDoc(doc(db, 'feed_posts', post.id), {
      commentsList: updatedComments
    })
  } catch (err) {
    console.error("Error submitting comment:", err)
  }
}

const selectedChatRecipient = ref(null)
const chatInputText = ref('')
const chatMessagesContainer = ref(null)

const messengerSearchQuery = ref('')
const showAccordion = ref({
  chatInfo: false,
  customize: false,
  media: false,
  privacy: false
})
const startNewMessage = () => {
  alert("Feature coming soon: Start a new message")
}
const startAudioCall = () => {
  alert(`Starting audio call with ${selectedChatRecipient.value}...`)
}
const startVideoCall = () => {
  alert(`Starting video call with ${selectedChatRecipient.value}...`)
}
const toggleChatInfo = () => {
  alert("Toggle chat info panel")
}
const toggleAccordion = (section) => {
  showAccordion.value[section] = !showAccordion.value[section]
}
const actionProfile = () => alert(`Viewing profile for ${selectedChatRecipient.value}`)
const actionMute = () => alert(`Muted ${selectedChatRecipient.value}`)
const actionSearch = () => alert(`Searching in chat with ${selectedChatRecipient.value}`)

const chats = ref({
  'Yim Vatey': [
    { sender: 'them', text: 'Hey, are you home yet?', time: '10m ago' },
    { sender: 'me', text: 'Where r you', time: '1m ago' }
  ],
  'James Son': [
    { sender: 'them', text: 'Did you finish the assignment?', time: '15m ago' },
    { sender: 'me', text: 'Haha have fun', time: '2m ago' }
  ],
  'Muy Leng': [
    { sender: 'them', text: 'I almost there', time: '5m ago' }
  ],
  'Neav Sveita': [
    { sender: 'them', text: 'On my way there', time: '7m ago' }
  ],
  'Dave Rim': [
    { sender: 'them', text: 'Gogo !!!', time: '10m ago' }
  ],
  'Erich Summer': [],
  'David Pluash': [],
  'John N': []
})

function findAvatarByName(name) {
  if (!name) return defaultAvatar
  const allMates = [
    ...roommates,
    ...friends,
    { name: 'Yim Vatey', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&q=80' },
    { name: 'James Son', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80' },
    { name: 'Muy Leng', avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&q=80' },
    { name: 'Neav Sveita', avatar: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=100&q=80' },
    { name: 'Dave Rim', avatar: 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=100&q=80' }
  ]
  const match = allMates.find(m => m.name === name)
  return match ? match.avatar : defaultAvatar
}

const activeChatHistory = computed(() => {
  if (!selectedChatRecipient.value) return []
  return chats.value[selectedChatRecipient.value] || []
})

const messages = computed(() => {
  const list = []
  for (const name in chats.value) {
    const thread = chats.value[name]
    if (thread.length > 0) {
      const lastMsg = thread[thread.length - 1]
      const avatar = findAvatarByName(name)
      list.push({
        name,
        preview: lastMsg.sender === 'me' ? `You: ${lastMsg.text}` : lastMsg.text,
        time: lastMsg.time,
        avatar
      })
    }
  }
  return list
})

const filteredMessages = computed(() => {
  let list = messages.value
  if (messengerSearchQuery.value) {
    const q = messengerSearchQuery.value.toLowerCase()
    list = list.filter(m => m.name.toLowerCase().includes(q) || m.preview.toLowerCase().includes(q))
  }
  return list
})

function getChatId(uid, recipientName) {
  return [uid, recipientName].sort().join('_');
}

let messagesUnsubscribe = null;

const openChat = (name) => {
  selectedChatRecipient.value = name
  activeTab.value = 'messages'
  if (!chats.value[name]) {
    chats.value[name] = []
  }
  
  if (currentAuthUser.value) {
    if (messagesUnsubscribe) messagesUnsubscribe();
    
    const chatId = getChatId(currentAuthUser.value.uid, name);
    messagesUnsubscribe = onSnapshot(
      query(collection(db, 'chats', chatId, 'messages'), orderBy('timestamp', 'asc')),
      (snapshot) => {
        const msgs = [];
        snapshot.forEach(doc => {
          const data = doc.data();
          msgs.push({
            sender: data.senderId === currentAuthUser.value.uid ? 'me' : 'them',
            text: data.text,
            time: data.time || 'Just now',
            timestamp: data.timestamp
          });
        });
        chats.value[name] = msgs;
        nextTick(() => scrollToBottom());
      }
    );
  } else {
    nextTick(() => scrollToBottom());
  }
}



const sendChatMessage = async () => {
  if (!chatInputText.value || !chatInputText.value.trim() || !selectedChatRecipient.value) return
  
  const text = chatInputText.value.trim()
  const recipient = selectedChatRecipient.value
  chatInputText.value = ''
  
  if (currentAuthUser.value) {
    const chatId = getChatId(currentAuthUser.value.uid, recipient);
    const msg = {
      senderId: currentAuthUser.value.uid,
      text,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      timestamp: serverTimestamp()
    };
    
    try {
      await addDoc(collection(db, 'chats', chatId, 'messages'), msg);
      await setDoc(doc(db, 'chats', chatId), {
        participants: [currentAuthUser.value.uid, recipient],
        lastMessage: text,
        lastMessageTime: serverTimestamp()
      }, { merge: true });
    } catch(e) {
      console.error("Error sending message:", e);
    }
  } else {
    chats.value[recipient].push({
      sender: 'me',
      text,
      time: 'Just now'
    })
    triggerMockReply(recipient)
  }
  
  nextTick(() => {
    scrollToBottom()
  })
}

const triggerMockReply = (recipient) => {
  setTimeout(() => {
    if (chats.value[recipient]) {
      const replies = [
        "Hey! Yes, that sounds good. Let's catch up later!",
        "Awesome! Let me know when you are free.",
        "Got it! Thanks for letting me know.",
        "Perfect, let's talk about it tomorrow.",
        "Haha that is cool! Let's do it.",
        "I am a bit busy right now, talk to you later!"
      ]
      const randomReply = replies[Math.floor(Math.random() * replies.length)]
      chats.value[recipient].push({
        sender: 'them',
        text: randomReply,
        time: 'Just now'
      })
      nextTick(() => {
        scrollToBottom()
      })
    }
  }, 1500)
}

const scrollToBottom = () => {
  if (chatMessagesContainer.value) {
    chatMessagesContainer.value.scrollTop = chatMessagesContainer.value.scrollHeight
  }
}

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
const IconMessages = { render: () => h('svg', { class: 'messages-icon', width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { d: 'M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z' })]) }
const IconBell     = { render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { d: 'M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9' }), h('path', { d: 'M13.73 21a2 2 0 01-3.46 0' })]) }
const IconSettings = { render: () => h('svg', { class: 'settings-icon', width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [h('path', { class: 'settings-gear', d: 'M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z' }), h('circle', { class: 'settings-center', cx: 12, cy: 12, r: 3 })]) }

const tabs = [
  { id: 'home',     label: 'Home',     icon: IconHome },
  { id: 'favorite', label: 'Favorite', icon: IconHeart },
  { id: 'feeds',    label: 'Feeds',    icon: IconFeeds },
  { id: 'messages', label: 'Messages', icon: IconMessages },
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
  let list = properties.value

  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    list = list.filter(p => p.name.toLowerCase().includes(q) || p.location.toLowerCase().includes(q))
  }

  const state = filterState.value
  
  if (state.type !== 'Any type') {
    list = list.filter(p => {
      const pType = (p.type || '').toLowerCase()
      const sType = state.type.toLowerCase().replace('entire ', '')
      return pType === state.type.toLowerCase() || pType.includes(sType)
    })
  }
  
  list = list.filter(p => p.price >= state.priceMin && p.price <= state.priceMax)
  
  if (state.bedrooms > 0) list = list.filter(p => (p.bedrooms || p.beds) >= state.bedrooms)
  if (state.beds > 0) list = list.filter(p => p.beds >= state.beds)
  if (state.bathrooms > 0) list = list.filter(p => p.baths >= state.bathrooms)
  
  if (state.amenities && state.amenities.length > 0) {
    list = list.filter(p => state.amenities.every(a => p.amenities && p.amenities.includes(a)))
  }
  
  if (state.period !== 'Any') {
    list = list.filter(p => p.period === state.period)
  }

  if (state.rate !== 'Any') {
    const minRate = parseFloat(state.rate)
    if (!isNaN(minRate)) {
      list = list.filter(p => p.rating >= minRate)
    }
  }
  
  return list
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
/* ── CONTENT ── */
.content {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 20px 52px 12px;
}

/* ── VERIFICATION BANNER ── */
.urgent-verification-banner {
  display: flex; align-items: center; gap: 16px;
  background: #fff3cd !important; border: 1px solid #ffe69c !important; border-radius: 12px;
  padding: 16px 20px; margin-bottom: 24px; cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.urgent-verification-banner:hover {
  transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.banner-icon { color: #856404 !important; flex-shrink: 0; }
.banner-text { flex: 1; color: #856404 !important; }
.banner-text strong { display: block; font-size: 1.05rem; margin-bottom: 4px; }
.banner-text p { font-size: 0.85rem; opacity: 0.9; margin: 0; }
.banner-btn {
  background: #856404 !important; color: #fff !important; border: none; border-radius: 8px;
  padding: 8px 16px; font-weight: 600; cursor: pointer; font-family: inherit; white-space: nowrap;
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

/* ── GRID — Responsive grid ── */
.listings {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px 14px;
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
  width: min(1200px, 100%);
  margin: 22px auto 96px;
  display: grid;
  grid-template-columns: minmax(0, 1.8fr) minmax(0, 1fr);
  align-items: start;
  gap: 40px;
}

/* ── DISCOVER PEOPLE SIDEBAR ── */
.discover-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.discover-title-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mobile-discover-close {
  display: none;
  background: transparent;
  border: none;
  color: #111;
  cursor: pointer;
  padding: 4px;
}

.discover-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.75rem;
  line-height: 1.15;
  font-weight: 800;
  color: #050505;
  margin: 0;
}

.discover-search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.discover-search-input {
  width: 100%;
  padding: 12px 42px 12px 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 0.95rem;
  outline: none;
}
.discover-search-input:focus {
  border-color: #5C4E4E;
}

.search-icon-btn {
  position: absolute;
  right: 14px;
  background: none;
  border: none;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 2;
}
.search-icon-btn svg {
  transition: stroke 0.2s;
}
.search-icon-btn:hover svg {
  stroke: #5C4E4E;
}

.discover-tabs {
  display: flex;
  gap: 16px;
  border-bottom: 1px solid #eee;
  padding-bottom: 2px;
}

.discover-tab-btn {
  background: none;
  border: none;
  font-size: 0.85rem;
  font-weight: 600;
  color: #6b7280;
  padding: 6px 4px;
  cursor: pointer;
  position: relative;
}

.discover-tab-btn.active {
  color: #050505;
}

.discover-tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  right: 0;
  height: 2px;
  background: #050505;
}

.discover-block {
  background: #fff;
  border: 1px solid #dedede;
  border-radius: 12px;
  padding: 16px;
}

.discover-block-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.discover-block-header h3 {
  font-size: 1.15rem;
  font-weight: 800;
  color: #050505;
  margin: 0;
}

.view-all-btn {
  background: none;
  border: none;
  font-size: 0.85rem;
  font-weight: 700;
  color: #5C4E4E;
  cursor: pointer;
  text-decoration: underline;
}

.discover-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.discover-item {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.discover-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
}

.discover-post-img {
  width: 48px;
  height: 48px;
  border-radius: 6px;
  object-fit: cover;
}

.discover-info {
  flex: 1;
  min-width: 0;
}

.discover-info h4 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #050505;
  margin: 0 0 2px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.discover-info p {
  font-size: 0.8rem;
  color: #6b7280;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.discover-action-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  border-radius: 50%;
}
.discover-action-btn:hover {
  background: #f3f4f6;
}

.feeds-main {
  min-width: 0;
}

.feeds-header-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0 0 14px;
}

.mobile-discover-search {
  display: none;
}

.feeds-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.75rem;
  line-height: 1.15;
  font-weight: 800;
  color: #050505;
  margin: 0;
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
  font-size: 1.15rem;
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

.composer-caption-input {
  width: 100%;
  padding: 8px;
  margin-top: 8px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 0.8rem;
  outline: none;
}
.composer-caption-input:focus {
  border-color: #2c9efc;
}

.composer-actions-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.location-input-wrapper {
  display: flex;
  align-items: center;
  background: #f0f2f5;
  padding: 6px 10px;
  border-radius: 16px;
  gap: 6px;
}
.location-input-wrapper svg {
  stroke: #8e8e8e;
}

.composer-location-input {
  border: none;
  background: transparent;
  font-size: 0.75rem;
  outline: none;
  color: #050505;
}

.feed-author-details {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.feed-author-name {
  font-size: 0.75rem;
  color: #050505;
  font-weight: 700;
}

.feed-author-location {
  font-size: 0.65rem;
  color: #65676b;
  font-weight: 500;
  margin-top: 2px;
}

/* MESSENGER FULL SCREEN LAYOUT */
.full-screen-messenger {
  position: absolute;
  top: 71px; /* Height of the top nav */
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  background: #fcfcfc;
  z-index: 50;
  padding: 24px;
  box-sizing: border-box;
}



.messenger-boxes-container {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 24px;
  flex: 1;
  min-height: 0;
  transition: all 0.3s ease;
}

.messenger-boxes-container.has-chat {
  grid-template-columns: 320px 1fr 300px;
}

/* LEFT SIDEBAR */
.messenger-sidebar {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e5e5e5;
  display: flex;
  flex-direction: column;
  padding: 16px 12px 0;
  height: 100%;
  overflow: hidden;
}

.messenger-header,
.messenger-search,
.active-now-section {
  flex-shrink: 0;
}

.recent-messages-section {
  flex: 1;
  overflow-y: auto;
  padding-bottom: 20px;
}

.recent-messages-section::-webkit-scrollbar { width: 4px; }
.recent-messages-section::-webkit-scrollbar-thumb { background: #e4e6e9; border-radius: 4px; }

/* MAIN CHAT AREA */
.messenger-main {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e5e5e5;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.mobile-chat-back {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  color: #111;
  padding: 4px;
  margin-right: 8px;
}

.chat-main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid #f0f0f0;
}

.chat-header-user {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-header-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-header-info h3 {
  font-size: 1.05rem;
  margin: 0 0 2px;
}

.chat-header-info .chat-status {
  font-size: 0.8rem;
  color: #65676b;
}

.chat-header-actions {
  display: flex;
  gap: 16px;
  cursor: pointer;
}

.chat-main-messages {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.chat-main-messages::-webkit-scrollbar { width: 6px; }
.chat-main-messages::-webkit-scrollbar-thumb { background: #d0d0d0; border-radius: 6px; }

.chat-main-footer {
  padding: 16px 24px;
  background: #ffffff;
}

.chat-input-wrapper {
  display: flex;
  align-items: center;
  background: #f0f2f5;
  border-radius: 24px;
  padding: 8px 12px 8px 20px;
  gap: 12px;
}

.chat-input-wrapper input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.95rem;
  color: #050505;
}

.chat-send-btn {
  background: #111;
  color: #fff;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  transition: all 0.2s;
}

.chat-send-btn svg {
  stroke: #fff !important;
  width: 16px;
  height: 16px;
}

.chat-send-btn:disabled {
  background: #e4e6e9;
  cursor: not-allowed;
}

.chat-send-btn:disabled svg {
  stroke: #a0a0a0 !important;
}

/* DETAILS SIDEBAR */
.messenger-details {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e5e5e5;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  overflow-y: auto;
}

.messenger-details::-webkit-scrollbar { width: 4px; }
.messenger-details::-webkit-scrollbar-thumb { background: #e4e6e9; border-radius: 4px; }

.details-profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 24px;
}

.details-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 12px;
}

.details-profile-header h2 {
  font-size: 1.15rem;
  margin: 0 0 4px;
}

.details-profile-header span {
  font-size: 0.85rem;
  color: #65676b;
}

.details-actions {
  display: flex;
  justify-content: space-around;
  margin-bottom: 32px;
}

.chat-action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #050505;
}

.icon-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #f0f2f5;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #111;
  transition: background 0.2s;
}

.chat-action-btn:hover .icon-circle {
  background: #e4e6e9;
}

.chat-action-btn span {
  font-size: 0.8rem;
  font-weight: 500;
}

.details-accordion {
  display: flex;
  flex-direction: column;
}

.accordion-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.2s;
  font-weight: 600;
  font-size: 0.95rem;
  color: #111;
}

.accordion-item:hover {
  background: #f0f2f5;
}

/* NO CHAT SELECTED STATE */
.no-chat-selected {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.no-chat-selected h2 {
  font-size: 1.4rem;
  margin: 16px 0 8px;
}

.no-chat-selected p {
  color: #65676b;
  margin-bottom: 24px;
}

.active-chat {
  background: #e6f2ff !important;
}

.messenger-panel::-webkit-scrollbar {
  width: 4px;
}
.messenger-panel::-webkit-scrollbar-thumb {
  background: #e4e6e9;
  border-radius: 4px;
}

.messenger-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.messenger-title {
  font-family: 'DM Sans', sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: #050505;
  margin: 0;
}

.new-msg-btn {
  background: #f0f2f5;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #050505;
  cursor: pointer;
  transition: background 0.2s;
}

.new-msg-btn:hover {
  background: #e4e6e9;
}

.messenger-search {
  display: flex;
  align-items: center;
  background: #f0f2f5;
  border-radius: 20px;
  padding: 10px 14px;
  margin-bottom: 16px;
}

.messenger-search svg {
  margin-right: 8px;
}

.messenger-search input {
  background: transparent;
  border: none;
  outline: none;
  font-size: 0.9rem;
  width: 100%;
  color: #050505;
}

.messenger-search input::placeholder {
  color: #8e8e8e;
}

.active-now-section {
  margin-bottom: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f2f5;
}

.active-users-scroller {
  display: flex;
  gap: 14px;
  overflow-x: auto;
  padding-bottom: 4px;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  cursor: grab;
}

.active-users-scroller:active {
  cursor: grabbing;
}

.active-users-scroller::-webkit-scrollbar {
  height: 6px;
  background: transparent;
}

.active-users-scroller::-webkit-scrollbar-thumb {
  background: #d0d0d0;
  border-radius: 4px;
}

.active-user-bubble {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  min-width: 52px;
  flex-shrink: 0;
}

.active-avatar-wrapper {
  position: relative;
  width: 52px;
  height: 52px;
}

.active-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 2px #e4e6e9;
}

.online-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 12px;
  height: 12px;
  background: #31a24c;
  border: 2px solid #ffffff;
  border-radius: 50%;
}

.active-name {
  font-size: 0.75rem;
  color: #65676b;
  font-weight: 500;
}

.chat-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.chat-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
  margin: 0 -10px;
}

.chat-row:hover {
  background: #f2f2f2;
}

.chat-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.chat-name {
  display: block;
  font-weight: 600;
  color: #050505;
  font-size: 0.95rem;
  margin-bottom: 2px;
}

.chat-preview {
  display: flex;
  align-items: center;
  color: #65676b;
  font-size: 0.85rem;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
}

.preview-text {
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 130px;
}

.unread-text {
  font-weight: 700;
  color: #050505;
}

.chat-time {
  margin-left: 4px;
  flex-shrink: 0;
  font-size: 0.75rem;
}

.unread-indicator {
  width: 10px;
  height: 10px;
  background: #0084ff;
  border-radius: 50%;
  flex-shrink: 0;
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

.edit-photo-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  background: #111;
  color: #fff;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  transition: transform 0.2s;
}
.edit-photo-btn:hover {
  transform: scale(1.05);
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
  transition: all 0.2s ease;
}

.input-wrapper.editing-mode {
  border-color: #111;
  background: #fafafa;
  box-shadow: 0 0 0 1px #111;
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

/* ── RESPONSIVE GRID MEDIA QUERIES ── */
@media (min-width: 600px) {
  .listings {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 900px) {
  .listings {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1200px) {
  .listings {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* ── INTERACTIVE FEEDS DESIGN ── */
.composer-body {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.composer-textarea {
  width: 100%;
  border: none;
  resize: none;
  outline: none;
  font-family: inherit;
  font-size: 0.95rem;
  color: #111;
  background: transparent;
  padding: 4px;
}

.composer-textarea::placeholder {
  color: #999;
}

.composer-image-preview {
  position: relative;
  width: 100%;
  max-height: 200px;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #eee;
  background: #fdfdfd;
}

.composer-image-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.remove-preview-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(0,0,0,0.6);
  color: #fff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
}

.remove-preview-btn:hover {
  background: rgba(0,0,0,0.8);
}

.composer-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #f0f0f0;
  padding-top: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  color: #555;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 20px;
  transition: background 0.2s, color 0.2s;
}

.action-btn:hover {
  background: #f5f5f5;
  color: #111;
}

.composer-submit-btn {
  padding: 6px 18px;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s;
}

.composer-submit-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.feed-delete-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
}

.feed-delete-btn:hover {
  background: #fef2f2;
}

.feed-actions .action-item {
  transition: transform 0.15s, color 0.15s;
}

.feed-actions .action-item:hover {
  transform: scale(1.05);
  color: #111;
}

/* Comments section styling */
.feed-comments-section {
  border-top: 1px solid #eee;
  margin-top: 14px;
  padding-top: 12px;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
  max-height: 240px;
  overflow-y: auto;
  padding-right: 4px;
}

.comment-item {
  display: flex;
  gap: 8px;
  align-items: flex-start;
}

.comment-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.comment-bubble {
  background: #f0f2f5;
  padding: 8px 12px;
  border-radius: 14px;
  max-width: 85%;
}

.comment-author {
  font-weight: 700;
  font-size: 0.72rem;
  color: #050505;
  margin-bottom: 2px;
}

.comment-text {
  font-size: 0.78rem;
  color: #1c1e21;
  line-height: 1.25;
}

.add-comment-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
}

.comment-input-wrapper {
  display: flex;
  align-items: center;
  flex: 1;
  background: #f0f2f5;
  border-radius: 20px;
  padding: 4px 6px 4px 12px;
}

.comment-input-wrapper input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-family: inherit;
  font-size: 0.78rem;
  color: #111;
  padding: 4px 0;
}

.comment-input-wrapper input::placeholder {
  color: #888;
}

.comment-send-btn {
  background: #111;
  color: #fff;
  border: none;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.72rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s;
}

.comment-send-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

/* ── BOTTOM NAV ── */
.bottom-nav {
  position: fixed;
  bottom: 12px;
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
  .full-screen-messenger {
    padding: 0;
  }
  .messenger-boxes-container,
  .messenger-boxes-container.has-chat {
    grid-template-columns: 1fr;
    gap: 0;
  }
  .messenger-sidebar, .messenger-main, .messenger-details {
    border-radius: 0;
    border: none;
  }
  .messenger-boxes-container.has-chat .messenger-sidebar {
    display: none;
  }
  .messenger-boxes-container:not(.has-chat) .messenger-main {
    display: none;
  }
  .messenger-boxes-container.has-chat .messenger-details {
    display: none;
  }
  .mobile-chat-back {
    display: flex;
    align-items: center;
  }
  
  .listings { gap: 10px 8px; }
  .content { padding: 16px 32px; }
  .top-nav { padding: 10px 32px; }
  .feeds-section {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .discover-sidebar {
    display: none;
  }
  .discover-sidebar.show-on-mobile {
    display: flex;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #fff;
    z-index: 99999;
    padding: 24px 20px;
    overflow-y: auto;
  }
  .mobile-discover-close { display: block; }
  .mobile-discover-search {
    display: flex;
    align-items: center;
    gap: 6px;
    background: #f0f0f0;
    padding: 8px 14px;
    border-radius: 20px;
    color: #666;
    font-size: 0.9rem;
    cursor: pointer;
    margin-right: 16px;
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
  .full-screen-messenger { top: 58px; }
  .listings { gap: 18px; }
  .content { padding: 14px 16px 112px; }
  .top-nav { padding: 10px 16px; gap: 12px; }
  .logo { gap: 6px; min-width: 0; }
  .logo-icon { width: 28px; height: 28px; }
  .logo-icon svg { width: 24px; height: 24px; }
  .logo-text { font-size: 1.05rem; white-space: nowrap; }
  .nav-right { gap: 4px; flex-shrink: 0; }
  .host-text { display: none; }
  .profile-menu {
    margin-left: 2px;
    padding: 2px;
  }
  .avatar img { width: 32px; height: 32px; }
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
  .feeds-section { margin: 16px auto 0; gap: 24px; }
  .feeds-header-wrapper { padding: 0; }
  .feeds-title { font-size: 1.45rem; padding: 0; }
  .discover-sidebar { padding: 24px 20px; }
  .post-composer, .feed-card {
    border-radius: 8px;
    border: 1px solid #dedede;
  }
  .post-composer h2,
  .mates-card { padding-left: 16px; padding-right: 16px; }
  .composer-row { padding-left: 16px; padding-right: 16px; }
  .feed-card { margin-bottom: 16px; padding: 12px 12px 14px; }
  .feed-image { height: 190px; margin: 0; width: 100%; border-radius: 4px; }
  .feed-text { font-size: 1rem; min-height: 58px; margin-top: 4px; }
  .mates-panel { grid-template-columns: 1fr; }
  .notification-section { margin: 16px auto 0; }
  .notification-title { font-size: 1.45rem; margin-bottom: 16px; }
  .notification-item {
    grid-template-columns: 32px minmax(0, 1fr) 24px;
    gap: 10px;
    padding: 10px 12px;
  }
  .settings-layout { flex-direction: column; }
  .settings-sidebar { 
    width: 100%; 
    border-right: none; 
    padding-right: 0; 
    position: static; 
    margin-bottom: 24px;
    display: flex;
    overflow-x: auto;
    padding-bottom: 12px;
    -webkit-overflow-scrolling: touch;
    white-space: nowrap;
    border-bottom: 1px solid #eee;
  }
  .settings-sidebar::-webkit-scrollbar { display: none; }
  .settings-sidebar h2.settings-title,
  .settings-sidebar .search-filter,
  .sidebar-section h3 {
    display: none;
  }
  .sidebar-section {
    display: flex;
    margin-bottom: 0;
  }
  .sidebar-menu {
    display: flex;
    flex-direction: row;
    gap: 8px;
    padding-left: 8px;
  }
  .sidebar-item {
    margin-bottom: 0;
    padding: 8px 16px;
    border-radius: 20px;
    background: #f5f5f5;
  }
  .sidebar-item.active {
    background: #111;
    color: #fff;
  }
  .sidebar-item.active svg {
    stroke: #fff;
  }
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
  .profile-menu { padding-left: 8px; }
  .bottom-nav { width: calc(100% - 16px); }
}

/* ===== Crop Modal ===== */

.crop-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.crop-modal {
  background: #1a1a1a;
  border-radius: 20px;
  width: 95%;
  max-width: 460px;
  overflow: hidden;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.5);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.crop-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.crop-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
  margin: 0;
  font-family: 'DM Sans', sans-serif;
}

.crop-close-btn {
  background: rgba(255, 255, 255, 0.08);
  border: none;
  color: #aaa;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}

.crop-close-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

.crop-done-btn {
  background: #fff;
  border: none;
  color: #111;
  padding: 8px 20px;
  border-radius: 10px;
  font-weight: 700;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.crop-done-btn:hover {
  background: #e5e5e5;
}

.crop-body {
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.crop-canvas-wrapper {
  width: 100%;
  max-width: 400px;
  aspect-ratio: 1;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
}

.crop-canvas-wrapper canvas {
  display: block;
  cursor: grab;
  border-radius: 16px;
}

.crop-canvas-wrapper canvas:active {
  cursor: grabbing;
}

.crop-controls {
  padding: 16px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.control-group {
  display: flex;
  align-items: center;
  gap: 14px;
}

.control-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #888;
  min-width: 80px;
  white-space: nowrap;
}

.range-slider {
  -webkit-appearance: none;
  appearance: none;
  flex: 1;
  height: 4px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.12);
  outline: none;
  transition: background 0.2s;
}

.range-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.15s ease;
}

.range-slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.range-slider::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  border: none;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

.control-quick-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding-top: 4px;
}

.quick-action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  border: none;
  color: #aaa;
  padding: 8px 14px;
  border-radius: 10px;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.quick-action-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}
/* ===== Chat Drawer Overlay ===== */
.chat-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 9999;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  backdrop-filter: blur(2px);
}

.chat-drawer-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.chat-drawer {
  position: absolute;
  top: 0;
  right: -400px;
  width: min(400px, 100%);
  height: 100%;
  background: #fff;
  box-shadow: -10px 0 30px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.chat-drawer-overlay.open .chat-drawer {
  right: 0;
}

.chat-header {
  padding: 16px 20px;
  border-bottom: 1px solid #ebebeb;
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-close-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #666;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background 0.2s;
}

.chat-close-btn:hover {
  background: #f5f5f5;
  color: #111;
}

.chat-header-user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.chat-header-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-header-info h3 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #111;
  margin: 0;
  line-height: 1.2;
}

.chat-status {
  font-size: 0.72rem;
  color: #10b981;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
}

.chat-status::before {
  content: '';
  width: 6px;
  height: 6px;
  background: currentColor;
  border-radius: 50%;
}

.chat-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: #f9f9f9;
}

.chat-bubble-wrapper {
  display: flex;
  width: 100%;
}

.chat-bubble-wrapper.me {
  justify-content: flex-end;
}

.chat-bubble-wrapper.them {
  justify-content: flex-start;
}

.chat-bubble {
  max-width: 75%;
  padding: 12px 16px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.chat-bubble-wrapper.me .chat-bubble {
  background: #111;
  color: #fff;
  border-bottom-right-radius: 4px;
}

.chat-bubble-wrapper.them .chat-bubble {
  background: #f0f2f5;
  color: #050505;
  border-bottom-left-radius: 4px;
  border: none;
}

.chat-bubble p {
  font-size: 0.88rem;
  line-height: 1.35;
  margin: 0;
  word-break: break-word;
}

.chat-bubble time {
  font-size: 0.62rem;
  align-self: flex-end;
  opacity: 0.6;
}

.chat-bubble-wrapper.me time {
  color: rgba(255, 255, 255, 0.75);
}

.chat-bubble-wrapper.them time {
  color: #888;
}

.empty-chat-state {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #888;
  font-size: 0.85rem;
}

.chat-footer {
  padding: 14px 20px;
  border-top: 1px solid #ebebeb;
  display: flex;
  gap: 10px;
  background: #fff;
}

.chat-footer input {
  flex: 1;
  border: 1px solid #e0e0e0;
  border-radius: 24px;
  padding: 10px 16px;
  font-family: inherit;
  font-size: 0.88rem;
  outline: none;
  transition: border-color 0.2s;
  background: #fff;
}

.chat-footer input:focus {
  border-color: #111;
}

.chat-send-btn {
  background: #111;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 24px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, opacity 0.2s;
}

.chat-send-btn:hover {
  background: #000;
}

.chat-send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ── FINAL THEME OVERRIDE ── */
.home-page, .content { background: #ffffff !important; }
.top-nav { background: #5C4E4E !important; border-bottom: none !important; }
.logo-text, .logo-icon { color: #ffffff !important; }
.hero-title, .feeds-title, .notification-title, .section-title { color: #000000 !important; }

/* Inputs and Buttons */
.search-box, .filter-btn { background: #ffffff !important; border: 1px solid #c0c0c0 !important; color: #000000 !important; border-radius: 30px !important; }
.search-box input { color: #000000 !important; }
.search-box input::placeholder { color: #888888 !important; }

/* Cards (Feeds, Mates, Notifications) */
.post-composer, .feed-card, .mates-card, .notification-item.seen, .chat-modal, .chat-header { 
  background: #ffffff !important; 
  border: 1px solid #e0e0e0 !important; 
  border-radius: 16px !important;
}
.property-card { background: #fafafa !important; border: none !important; box-shadow: none !important; border-radius: 16px !important; }
.notification-item { background: #f0f0f0 !important; color: #000000 !important; border: 1px solid #e0e0e0 !important; }

/* Text within cards */
.feed-text, .card-name, .card-price, .notification-copy h2, .chat-message.me .msg-bubble { color: #000000 !important; }
.feed-author span, .mate-copy span { color: #000000 !important; }
.card-location, .match, .mate-copy p, .mate-row time, .feed-caption, .chat-message.them .msg-bubble, .composer-row input { color: #888888 !important; }
.host-text { color: #ffffff !important; font-weight: 600 !important; font-size: 0.95rem !important; cursor: pointer; }

/* Tags & Badges */
.tag { background: #ffffff !important; color: #888888 !important; border: 1px solid #e0e0e0 !important; border-radius: 8px !important; position: relative; }
.tag::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-2px);
  background: #333 !important;
  color: #fff !important;
  padding: 4px 8px !important;
  border-radius: 6px !important;
  font-size: 0.75rem !important;
  white-space: nowrap !important;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.15s ease, transform 0.15s ease;
  pointer-events: none;
  z-index: 20;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
  border: none !important;
}
.tag:hover::after, .tag:focus::after {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(-6px);
}
.tag::before {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(2px);
  border-width: 5px;
  border-style: solid;
  border-color: #333 transparent transparent transparent;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.15s ease, transform 0.15s ease;
  pointer-events: none;
  z-index: 20;
}
.tag:hover::before, .tag:focus::before {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(6px);
}
.notification-badge { background: #000000 !important; color: #ffffff !important; }
.heart-btn { background: #ffffff !important; border-radius: 50% !important; border: none !important; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }

/* Bottom Nav - Floating Pill */
.bottom-nav { 
  background: rgba(92, 78, 78, 0.95) !important; /* #5C4E4E with some transparency */
  backdrop-filter: blur(10px);
  border-top: none !important; 
  border-radius: 40px !important; 
  margin: 0 auto 24px auto !important; 
  width: max-content !important; 
  padding: 8px 32px !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
  position: fixed !important;
  bottom: 12px !important; left: 50% !important; right: auto !important; transform: translateX(-50%) !important; margin: 0 !important;
  display: flex !important;
  gap: 24px !important;
  align-items: center !important;
  justify-content: center !important;
}
.nav-tab { 
  display: flex !important; 
  flex-direction: column !important; 
  align-items: center !important; 
  justify-content: center !important; 
  color: #c0c0c0 !important; 
  background: transparent !important; 
  border: none !important; 
  min-width: 60px !important;
  padding: 8px 12px !important;
}
.nav-tab.active { color: #ffffff !important; }

/* SVG Icon Coloring */
.nav-tab svg { stroke: #c0c0c0 !important; fill: none !important; }
.nav-tab.active svg { stroke: #ffffff !important; fill: #ffffff !important; }

/* Specifically fill complex icons */
:deep(.nav-tab.active .home-icon .home-body),
:deep(.nav-tab.active .feeds-icon .feeds-frame),
:deep(.nav-tab.active .settings-icon .settings-gear) {
  fill: #ffffff !important;
  stroke: #ffffff !important;
}

/* Cutout paths for complex icons (make them match pill background) */
:deep(.nav-tab.active .home-icon .home-door),
:deep(.nav-tab.active .feeds-icon .feeds-line),
:deep(.nav-tab.active .settings-icon .settings-center) {
  stroke: #5C4E4E !important;
  fill: none !important;
}

/* Chat bubbles */
.msg-bubble { background: #f0f0f0 !important; color: #000000 !important; border: 1px solid #e0e0e0 !important; }
.chat-message.me .msg-bubble { background: #5C4E4E !important; color: #ffffff !important; border: none !important; }
.chat-input-area { background: #ffffff !important; border-top: 1px solid #e0e0e0 !important; }
.chat-input-area input { background: #f0f0f0 !important; color: #000000 !important; border: 1px solid #e0e0e0 !important; }
.chat-input-area input::placeholder { color: #888888 !important; }

/* Buttons */
.btn-primary, .btn-dark, .composer-submit-btn, .banner-btn, .action-btn { background: #5C4E4E !important; color: #ffffff !important; border: none !important; border-radius: 20px !important; }
.composer-row input::placeholder { color: #888888 !important; }
.card-carousel { background: #e0e0e0 !important; }

@media (max-width: 900px) {
  .bottom-nav {
    width: calc(100% - 24px) !important;
    max-width: 420px !important;
    gap: 0 !important;
    padding: 8px 10px !important;
  }
  .nav-tab {
    flex: 1 !important;
    min-width: 0 !important;
    padding: 6px 2px !important;
  }
}

@media (max-width: 360px) {
  .bottom-nav { width: calc(100% - 16px) !important; }
}

/* --- Bottom Nav Thin Bar Hover Interaction --- */
.bottom-nav-interaction-group {
  display: contents;
}

.thin-bar-trigger {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 40px;
  z-index: 110;
  cursor: default;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 6px;
}

.thin-bar-trigger::after {
  content: '';
  width: 100px;
  height: 5px;
  background: rgba(92, 78, 78, 0.6);
  border-radius: 5px;
  transition: opacity 0.3s;
}

.bottom-nav.auto-hide {
  transform: translate(-50%, calc(100% + 20px)) !important;
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
  z-index: 105 !important;
}

.bottom-nav-interaction-group:hover .bottom-nav.auto-hide {
  transform: translate(-50%, 0) !important;
}

.bottom-nav-interaction-group:hover .thin-bar-trigger::after {
  opacity: 0;
}

@media (hover: none) and (pointer: coarse) {
  /* Disable desktop hover on touch devices */
  .tag:hover::after, .tag:hover::before {
    opacity: 0 !important;
    visibility: hidden !important;
  }
  /* Rely entirely on click (focus) for tooltips on touch */
  .tag:focus::after {
    opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(-6px) !important;
  }
  .tag:focus::before {
    opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(6px) !important;
  }

  /* Hotbar touch interaction */
  .bottom-nav-interaction-group:hover .bottom-nav.auto-hide {
    transform: translate(-50%, calc(100% + 20px)) !important;
  }
  .bottom-nav-interaction-group:hover .thin-bar-trigger::after {
    opacity: 1;
  }
  
  .bottom-nav.auto-hide.mobile-visible {
    transform: translate(-50%, 0) !important;
  }
  .bottom-nav-interaction-group.mobile-visible .thin-bar-trigger::after {
    opacity: 0;
  }
}
</style>
