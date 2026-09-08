<template>
  <div class="chat-page">
    <!-- Top Nav Bar -->
    <header class="top-nav-bar">
      <button class="logo-btn" type="button" aria-label="HomeSweet Home" @click="goHome">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 18 L16 18" />
          <path d="M4 18 L4 12 L9 7 L16 14" />
          <path d="M12 18 L12 4 L16 4 L16 18 Z" />
          <path d="M12 14 L16 14" />
        </svg>
      </button>

      <div class="nav-user-avatar" @click="goHome">
        <img :src="userAvatar" alt="User Avatar" />
      </div>
    </header>

    <!-- Main 3-Column Chat Layout -->
    <div class="chat-main-container">
      <!-- ==================== COLUMN 1: MESSAGES LIST ==================== -->
      <aside class="messages-sidebar">
        <!-- Sidebar Header -->
        <div class="sidebar-header">
          <button class="back-circle-btn" type="button" aria-label="Go Back" @click="goHome">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.5">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <h1 class="sidebar-title">Messages</h1>
        </div>

        <!-- Conversations Scroll List -->
        <div class="conversations-list">
          <div 
            v-for="(conv, index) in conversations" 
            :key="index"
            class="conversation-item"
            :class="{ active: selectedContact.id === conv.id }"
            @click="selectContact(conv)"
          >
            <div class="conv-avatar-wrap">
              <img :src="conv.avatar" :alt="conv.name" class="conv-avatar" />
            </div>
            <div class="conv-details">
              <span class="conv-name">{{ conv.name }}</span>
              <span class="conv-preview">{{ conv.preview }}</span>
            </div>
            <span class="conv-time">{{ conv.time }}</span>
          </div>
        </div>
      </aside>

      <!-- ==================== COLUMN 2: ACTIVE CONVERSATION ==================== -->
      <main class="chat-conversation-area">
        <!-- Chat Header -->
        <header class="active-chat-header">
          <div class="chat-recipient-info">
            <img :src="selectedContact.avatar" :alt="selectedContact.name" class="recipient-avatar" />
            <div class="recipient-text">
              <h2 class="recipient-name">{{ selectedContact.name }}</h2>
              <span class="recipient-email">{{ selectedContact.email }}</span>
            </div>
          </div>

          <div class="chat-header-actions" style="position: relative;">
            <button class="header-more-btn" type="button" aria-label="Chat options" @click="showMoreOptions = !showMoreOptions">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                <circle cx="5" cy="12" r="2.2" />
                <circle cx="12" cy="12" r="2.2" />
                <circle cx="19" cy="12" r="2.2" />
              </svg>
            </button>
            <div v-if="showMoreOptions" class="chat-more-dropdown">
              <button type="button" @click="viewProfile"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/></svg> View Profile</button>
              <button type="button" @click="startAudioCall"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> Audio Call</button>
              <button type="button" @click="startVideoCall"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg> Video Call</button>
              <button type="button" @click="toggleMuteContact"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg> {{ isContactMuted ? 'Unmute' : 'Mute Notifications' }}</button>
              <button type="button" class="text-danger" @click="confirmDeleteChat"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg> Clear Chat</button>
            </div>
          </div>
        </header>

        <!-- In-Chat Search Bar -->
        <div v-if="isSearchOpen" class="chat-search-bar">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
            <circle cx="11" cy="11" r="7" /><line x1="21" y1="21" x2="16" y2="16" />
          </svg>
          <input type="text" v-model="inChatSearch" placeholder="Search in conversation..." class="chat-search-input" />
          <button type="button" class="close-search-btn" @click="isSearchOpen = false; inChatSearch = ''">&times;</button>
        </div>

        <!-- Message Stream Scrollable -->
        <div class="message-stream-body" ref="messagesContainerRef">
          <!-- Sample / Active Messages -->
          <template v-for="(msg, i) in displayedMessages" :key="i">
            <!-- Received message -->
            <div v-if="msg.sender === 'them'" class="message-row received">
              <img :src="selectedContact.avatar" :alt="selectedContact.name" class="bubble-avatar" />
              <div class="bubble-content-wrap">
                <span class="sender-name-label">{{ selectedContact.name }}</span>
                <div class="message-bubble received-bubble">
                  <img v-if="msg.image" :src="msg.image" class="chat-photo-img" alt="Shared photo" />
                  <span v-if="msg.text">{{ msg.text }}</span>
                </div>
              </div>
            </div>

            <!-- Centered Timestamp -->
            <div v-if="msg.timestamp" class="centered-timestamp">
              {{ msg.timestamp }}
            </div>

            <!-- Sent message -->
            <div v-if="msg.sender === 'me'" class="message-row sent">
              <div class="bubble-content-wrap">
                <div class="message-bubble sent-bubble">
                  <img v-if="msg.image" :src="msg.image" class="chat-photo-img" alt="Sent photo" />
                  <span v-if="msg.text">{{ msg.text }}</span>
                </div>
                <span class="message-status">sent</span>
              </div>
            </div>
          </template>
        </div>

        <!-- Bottom Input Bar -->
        <footer class="chat-input-bar">
          <form class="input-form" @submit.prevent="sendMessage">
            <!-- Pill Input Container -->
            <div class="input-pill">
              <input 
                type="text" 
                v-model="messageInput" 
                placeholder="Aa" 
                class="message-input-field" 
              />
              <button type="button" class="emoji-btn" aria-label="Emoji Picker" @click="insertEmoji">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2">
                  <circle cx="12" cy="12" r="10" />
                  <path d="M8 14s1.5 2 4 2 4-2 4-2" />
                  <line x1="9" y1="9" x2="9.01" y2="9" />
                  <line x1="15" y1="9" x2="15.01" y2="9" />
                </svg>
              </button>
            </div>

            <!-- Outside Action Buttons -->
            <div class="outside-actions">
              <input type="file" ref="docInputRef" accept=".pdf,.doc,.docx,.txt" style="display: none;" @change="onDocSelected" />
              <input type="file" ref="photoInputRef" accept="image/*" style="display: none;" @change="onPhotoSelected" />

              <button type="button" class="action-icon-btn" aria-label="More actions" title="More actions" @click="insertQuickReaction">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                  <circle cx="5" cy="12" r="2.2" />
                  <circle cx="12" cy="12" r="2.2" />
                  <circle cx="19" cy="12" r="2.2" />
                </svg>
              </button>

              <button type="button" class="action-icon-btn" aria-label="Add attachment" title="Add attachment" @click="triggerDocUpload">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2">
                  <circle cx="12" cy="12" r="10" />
                  <line x1="12" y1="8" x2="12" y2="16" />
                  <line x1="8" y1="12" x2="16" y2="12" />
                </svg>
              </button>

              <button type="button" class="action-icon-btn" aria-label="Add photo" title="Add photo" @click="triggerPhotoUpload">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="3" ry="3"/>
                  <circle cx="8.5" cy="8.5" r="1.5"/>
                  <polyline points="21 15 16 10 5 21"/>
                </svg>
              </button>

              <!-- Explicit Send Button -->
              <button 
                type="submit" 
                class="send-message-btn" 
                :disabled="!messageInput.trim() || isSending" 
                aria-label="Send message"
                title="Send"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </button>
            </div>
          </form>
        </footer>
      </main>

      <!-- ==================== COLUMN 3: CONTACT INFO ==================== -->
      <aside class="contact-info-sidebar">
        <h2 class="contact-info-title">Contact Info</h2>

        <!-- Profile Photo & Summary -->
        <div class="contact-profile-card">
          <img :src="selectedContact.avatar" :alt="selectedContact.name" class="contact-big-avatar" />
          <h3 class="contact-big-name">{{ selectedContact.name }}</h3>
          <span class="contact-phone">{{ selectedContact.phone }}</span>
        </div>

        <!-- 3 Quick Action Buttons -->
        <div class="quick-actions-row">
          <button class="quick-action-btn" type="button" @click="alertAction('Profile')">
            <div class="quick-icon-wrap">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
              </svg>
            </div>
            <span class="quick-label">Profile</span>
          </button>

          <button class="quick-action-btn" type="button" @click="alertAction('Search')">
            <div class="quick-icon-wrap">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <circle cx="11" cy="11" r="7" />
                <line x1="21" y1="21" x2="16" y2="16" />
              </svg>
            </div>
            <span class="quick-label">Search</span>
          </button>

          <button class="quick-action-btn" type="button" @click="alertAction('Audio')">
            <div class="quick-icon-wrap">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.44-5.15-3.75-6.59-6.59l1.97-1.57c.27-.27.35-.65.24-1.01A11.36 11.36 0 018.96 4c0-.55-.45-1-1-1H4.5c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.62c0-.55-.45-1-1-1z"/>
              </svg>
            </div>
            <span class="quick-label">Audio</span>
          </button>
        </div>

        <!-- Action Cards List -->
        <div class="action-cards-list">
          <button class="action-card" type="button" @click="alertAction('Media, links and docs')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <circle cx="8.5" cy="8.5" r="1.5"/>
                <polyline points="21 15 16 10 5 21"/>
              </svg>
              <span>Media, links and docs</span>
            </div>
            <div class="card-right">
              <span class="count-badge">30</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 18l6-6-6-6"/>
              </svg>
            </div>
          </button>

          <button class="action-card" type="button" @click="alertAction('Chat theme')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/>
                <circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/>
                <circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/>
                <circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/>
                <path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/>
              </svg>
              <span>Chat theme</span>
            </div>
            <div class="card-right">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 18l6-6-6-6"/>
              </svg>
            </div>
          </button>

          <button class="action-card" type="button" @click="alertAction('Notifications & sounds')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span>Notifications & sounds</span>
            </div>
            <div class="card-right">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 18l6-6-6-6"/>
              </svg>
            </div>
          </button>

          <button class="action-card" type="button" @click="alertAction('Pinned messages')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="17" x2="12" y2="22"/>
                <path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.89A2 2 0 0 1 15 10.76V6a3 3 0 0 0-6 0v4.76a2 2 0 0 1-1.11 1.79l-1.78.89A2 2 0 0 0 5 15.24z"/>
              </svg>
              <span>Pinned messages</span>
            </div>
            <div class="card-right">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 18l6-6-6-6"/>
              </svg>
            </div>
          </button>

          <button class="action-card" type="button" @click="alertAction('Report')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                <line x1="12" y1="9" x2="12" y2="13"/>
                <line x1="12" y1="17" x2="12.01" y2="17"/>
              </svg>
              <span>Report</span>
            </div>
          </button>

          <button class="action-card" type="button" @click="alertAction('Block')">
            <div class="card-left">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>
              </svg>
              <span>Block</span>
            </div>
          </button>
        </div>

        <!-- Delete Chat Danger Action -->
        <div class="delete-chat-footer">
          <button class="delete-chat-btn" type="button" @click="confirmDeleteChat">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
              <line x1="10" y1="11" x2="10" y2="17"></line>
              <line x1="14" y1="11" x2="14" y2="17"></line>
            </svg>
            <span>Delete chat</span>
          </button>
        </div>
      </aside>
    </div>

    <!-- Calling Modal (Audio & Video) -->
    <div v-if="activeCall.isOpen" class="call-overlay">
      <div class="call-modal-card">
        <div class="call-avatar-container">
          <img :src="selectedContact.avatar" :alt="selectedContact.name" class="call-avatar" />
          <div class="call-pulse-ring"></div>
        </div>
        <h3 class="call-name">{{ selectedContact.name }}</h3>
        <p class="call-status">{{ activeCall.statusText }}</p>
        <div v-if="activeCall.type === 'video'" class="video-preview-box">
          <div class="simulated-camera-tag">● Camera Live HD</div>
          <img :src="selectedContact.avatar" class="video-feed-image" alt="Video stream" />
        </div>
        <div class="call-controls">
          <button type="button" class="call-action-btn" :class="{ active: activeCall.isMuted }" @click="activeCall.isMuted = !activeCall.isMuted" :title="activeCall.isMuted ? 'Unmute' : 'Mute'">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path v-if="!activeCall.isMuted" d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path v-if="!activeCall.isMuted" d="M19 10v2a7 7 0 0 1-14 0v-2"/><line v-if="!activeCall.isMuted" x1="12" y1="19" x2="12" y2="23"/><line v-if="!activeCall.isMuted" x1="8" y1="23" x2="16" y2="23"/>
              <line v-if="activeCall.isMuted" x1="1" y1="1" x2="23" y2="23"/><path v-if="activeCall.isMuted" d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"/>
            </svg>
          </button>
          <button type="button" class="call-action-btn end-call" @click="endCall" title="End Call">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 9c-1.6 0-3.15.25-4.6.72v3.1c0 .39-.23.74-.58.9-1.02.47-1.95 1.1-2.78 1.87-.27.26-.64.39-1.01.39-.41 0-.79-.16-1.09-.45L.45 14.04c-.29-.29-.45-.68-.45-1.09 0-.41.16-.8.45-1.09C4.1 8.21 7.82 6 12 6s7.9 2.21 11.55 5.86c.29.29.45.68.45 1.09s-.16.8-.45 1.09l-1.49 1.49c-.3.3-.68.45-1.09.45-.37 0-.74-.13-1.01-.39-.83-.77-1.76-1.4-2.78-1.87-.35-.16-.58-.51-.58-.9v-3.1C15.15 9.25 13.6 9 12 9z"/>
            </svg>
          </button>
          <button type="button" class="call-action-btn" :class="{ active: activeCall.isSpeaker }" @click="activeCall.isSpeaker = !activeCall.isSpeaker" :title="activeCall.isSpeaker ? 'Speaker On' : 'Speaker Off'">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Media, Links and Docs Modal -->
    <div v-if="showMediaModal" class="shared-modal-overlay" @click.self="showMediaModal = false">
      <div class="shared-modal-card">
        <div class="shared-modal-header">
          <h3>Media, Links & Documents</h3>
          <button type="button" class="modal-close-btn" @click="showMediaModal = false">&times;</button>
        </div>
        <div class="shared-media-tabs">
          <span class="active-tab">Photos (8)</span>
          <span>Docs (3)</span>
          <span>Links (12)</span>
        </div>
        <div class="shared-media-grid">
          <img src="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=300&q=80" alt="Media" />
          <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=300&q=80" alt="Media" />
          <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=300&q=80" alt="Media" />
          <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=300&q=80" alt="Media" />
        </div>
      </div>
    </div>

    <!-- Chat Theme Modal -->
    <div v-if="showThemeModal" class="shared-modal-overlay" @click.self="showThemeModal = false">
      <div class="shared-modal-card theme-card">
        <div class="shared-modal-header">
          <h3>Choose Chat Theme</h3>
          <button type="button" class="modal-close-btn" @click="showThemeModal = false">&times;</button>
        </div>
        <div class="theme-options-grid">
          <div class="theme-pill" :class="{ selected: chatTheme === 'default' }" @click="chatTheme = 'default'; showThemeModal = false; showToast('Theme set to HomeSweet Classic')">
            <span class="theme-circle default"></span>
            <span>Classic (#5C4E4E)</span>
          </div>
          <div class="theme-pill" :class="{ selected: chatTheme === 'emerald' }" @click="chatTheme = 'emerald'; showThemeModal = false; showToast('Theme set to Emerald Garden')">
            <span class="theme-circle emerald"></span>
            <span>Emerald Garden</span>
          </div>
          <div class="theme-pill" :class="{ selected: chatTheme === 'indigo' }" @click="chatTheme = 'indigo'; showThemeModal = false; showToast('Theme set to Royal Indigo')">
            <span class="theme-circle indigo"></span>
            <span>Royal Indigo</span>
          </div>
          <div class="theme-pill" :class="{ selected: chatTheme === 'rose' }" @click="chatTheme = 'rose'; showThemeModal = false; showToast('Theme set to Ruby Rose')">
            <span class="theme-circle rose"></span>
            <span>Ruby Rose</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Pinned Messages Modal -->
    <div v-if="showPinnedModal" class="shared-modal-overlay" @click.self="showPinnedModal = false">
      <div class="shared-modal-card">
        <div class="shared-modal-header">
          <h3>Pinned Information</h3>
          <button type="button" class="modal-close-btn" @click="showPinnedModal = false">&times;</button>
        </div>
        <div class="pinned-body">
          <div class="pinned-item">
            <span class="pinned-tag">📌 Property Details</span>
            <p>HomeSweet Premium Unit #402 • Check-in: 2:00 PM • Keyless Entry Code: 4819</p>
          </div>
          <div class="pinned-item">
            <span class="pinned-tag">📌 WiFi Network</span>
            <p>SSID: HomeSweet_Resident_5G • Password: Sweethome2026</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Report Modal -->
    <div v-if="showReportModal" class="shared-modal-overlay" @click.self="showReportModal = false">
      <div class="shared-modal-card">
        <div class="shared-modal-header">
          <h3>Report User</h3>
          <button type="button" class="modal-close-btn" @click="showReportModal = false">&times;</button>
        </div>
        <div class="report-body">
          <label class="report-option">
            <input type="radio" v-model="reportReason" value="spam" />
            <span>Spam or Commercial Solicitation</span>
          </label>
          <label class="report-option">
            <input type="radio" v-model="reportReason" value="harassment" />
            <span>Harassment or Offensive Behavior</span>
          </label>
          <label class="report-option">
            <input type="radio" v-model="reportReason" value="fraud" />
            <span>Fraudulent or Fake Listing</span>
          </label>
          <button type="button" class="btn-submit-report" @click="submitReport">Submit Report</button>
        </div>
      </div>
    </div>

    <!-- Toast Feedback -->
    <transition name="toast-fade">
      <div v-if="toast.visible" class="chat-toast">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <span>{{ toast.message }}</span>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { db, auth } from '../../firebase'
import { 
  collection, 
  addDoc, 
  query, 
  where, 
  onSnapshot, 
  serverTimestamp, 
  doc, 
  setDoc 
} from 'firebase/firestore'
import { onAuthStateChanged } from 'firebase/auth'

const router = useRouter()
const route = useRoute()
const isSending = ref(false)

let messagesUnsubscribe = null
let chatsUnsubscribe = null

// Current user state
const currentAuthUser = ref(auth.currentUser)
const currentUserId = computed(() => currentAuthUser.value?.uid || 'user_guest_01')
const currentUserName = computed(() => {
  return currentAuthUser.value?.displayName || 
         currentAuthUser.value?.email?.split('@')[0] || 
         'Resident User'
})
const currentUserAvatar = computed(() => {
  return currentAuthUser.value?.photoURL || 
         'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&q=80'
})

// Top nav
const userAvatar = computed(() => currentUserAvatar.value)
const showMoreOptions = ref(false)

function goHome() {
  router.push('/home')
}

// Seed starter contacts
const defaultContacts = [
  {
    id: 'landlord_skystar',
    targetId: 'landlord_skystar',
    name: 'Skystar Asset Management',
    preview: 'Hi! Your condo rental inquiry is welcome.',
    time: 'Just now',
    avatar: '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg',
    email: 'contact@skystar.com',
    phone: '+855 23 888 999'
  },
  {
    id: 'landlord_aurafa',
    targetId: 'landlord_aurafa',
    name: 'Aurafa Properties',
    preview: 'Unit 201 is ready for viewing anytime.',
    time: '20m',
    avatar: '/homesweet/86af45b4-efa9-4714-84bb-c02232f793cc.jpeg',
    email: 'info@aurafacondo.com',
    phone: '+855 12 345 678'
  },
  {
    id: 'meoww',
    targetId: 'meoww',
    name: 'Meoww Zuckerberg',
    preview: "Hi, I'm looking for a room to rent...",
    time: '1h',
    avatar: '/homesweet/meoww_cat.jpg',
    email: 'coconut123@gmail.com',
    phone: '+855 92 401 458'
  },
  {
    id: 'sophia_chea',
    targetId: 'sophia_chea',
    name: 'Sophia Chea',
    preview: 'Is the apartment still available for this month?',
    time: '3h',
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&q=80',
    email: 'sophia.chea@example.com',
    phone: '+855 12 888 123'
  },
  {
    id: 'dara_sok',
    targetId: 'dara_sok',
    name: 'Dara Sok',
    preview: 'Thanks for the quick response!',
    time: 'Yesterday',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&q=80',
    email: 'dara.sok@example.com',
    phone: '+855 16 889 900'
  }
]

// Dynamic conversations list
const conversations = ref([...defaultContacts])

// Currently selected contact
const selectedContact = ref(conversations.value[0])

// Helper: deterministic room ID between two users
function getDeterministicChatId(uidA, uidB) {
  const safeA = String(uidA || 'guest_a').trim()
  const safeB = String(uidB || 'guest_b').trim()
  return [safeA, safeB].sort().join('_')
}

// In-memory fallback message history
const messageHistory = ref({
  landlord_skystar: [
    {
      sender: 'them',
      text: "Hello! Welcome to Skystar Asset Management. Feel free to ask any questions about our listings.",
      timestamp: '10:00 AM'
    }
  ],
  meoww: [
    {
      sender: 'them',
      text: "Hi, I'm looking for a room to rent in a safe area with good wifi. Budget is around $150-200. Let me know if you have availability!",
      timestamp: '12:00 AM'
    }
  ]
})

const currentMessages = ref([])
const messageInput = ref('')
const messagesContainerRef = ref(null)

// In-chat search
const isSearchOpen = ref(false)
const inChatSearch = ref('')

const displayedMessages = computed(() => {
  if (!inChatSearch.value.trim()) return currentMessages.value
  const q = inChatSearch.value.toLowerCase()
  return currentMessages.value.filter(m => (m.text && m.text.toLowerCase().includes(q)))
})

function toggleInChatSearch() {
  isSearchOpen.value = !isSearchOpen.value
  if (!isSearchOpen.value) {
    inChatSearch.value = ''
  }
}

// Attachments
const docInputRef = ref(null)
const photoInputRef = ref(null)

function triggerDocUpload() {
  if (docInputRef.value) docInputRef.value.click()
}

function triggerPhotoUpload() {
  if (photoInputRef.value) photoInputRef.value.click()
}

async function onDocSelected(e) {
  const file = e.target.files[0]
  if (!file) return
  const docName = `📎 Document: ${file.name} (${Math.round(file.size / 1024)} KB)`
  await sendCustomMessage(docName, null)
  e.target.value = ''
}

async function onPhotoSelected(e) {
  const file = e.target.files[0]
  if (!file) return
  const reader = new FileReader()
  reader.onload = async (evt) => {
    const dataUrl = evt.target.result
    await sendCustomMessage('', dataUrl)
  }
  reader.readAsDataURL(file)
  e.target.value = ''
}

function insertQuickReaction() {
  const emojis = ['👍', '❤️', '🔥', '🎉', '👏', '🙌']
  const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)]
  messageInput.value += ` ${randomEmoji} `
}

// Calling State
const activeCall = reactive({
  isOpen: false,
  type: 'audio',
  statusText: 'Calling...',
  isMuted: false,
  isSpeaker: false,
  timerInterval: null,
  durationSeconds: 0
})

function startAudioCall() {
  showMoreOptions.value = false
  activeCall.isOpen = true
  activeCall.type = 'audio'
  activeCall.statusText = 'Ringing...'
  activeCall.durationSeconds = 0
  activeCall.isMuted = false
  activeCall.isSpeaker = false
  
  setTimeout(() => {
    if (activeCall.isOpen) {
      activeCall.statusText = 'Connected (00:00)'
      activeCall.timerInterval = setInterval(() => {
        activeCall.durationSeconds++
        const mins = String(Math.floor(activeCall.durationSeconds / 60)).padStart(2, '0')
        const secs = String(activeCall.durationSeconds % 60).padStart(2, '0')
        activeCall.statusText = `Connected (${mins}:${secs})`
      }, 1000)
    }
  }, 1800)
}

function startVideoCall() {
  showMoreOptions.value = false
  activeCall.isOpen = true
  activeCall.type = 'video'
  activeCall.statusText = 'Connecting video...'
  activeCall.durationSeconds = 0
  activeCall.isMuted = false
  activeCall.isSpeaker = true
  
  setTimeout(() => {
    if (activeCall.isOpen) {
      activeCall.statusText = 'Connected HD (00:00)'
      activeCall.timerInterval = setInterval(() => {
        activeCall.durationSeconds++
        const mins = String(Math.floor(activeCall.durationSeconds / 60)).padStart(2, '0')
        const secs = String(activeCall.durationSeconds % 60).padStart(2, '0')
        activeCall.statusText = `Connected HD (${mins}:${secs})`
      }, 1000)
    }
  }, 1800)
}

function endCall() {
  if (activeCall.timerInterval) {
    clearInterval(activeCall.timerInterval)
    activeCall.timerInterval = null
  }
  const duration = activeCall.durationSeconds
  activeCall.isOpen = false
  if (duration > 0) {
    const mins = Math.floor(duration / 60)
    const secs = duration % 60
    currentMessages.value.push({
      sender: 'them',
      text: `📞 Call ended • ${mins > 0 ? `${mins}m ` : ''}${secs}s`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    })
    scrollToBottom()
  }
}

// Contacts actions
const isContactMuted = ref(false)
const isContactBlocked = ref(false)
const showMediaModal = ref(false)
const showThemeModal = ref(false)
const showPinnedModal = ref(false)
const showReportModal = ref(false)

const toast = reactive({ visible: false, message: '' })
function showToast(msg) {
  toast.message = msg
  toast.visible = true
  setTimeout(() => { toast.visible = false }, 3000)
}

function toggleMuteContact() {
  isContactMuted.value = !isContactMuted.value
  showToast(isContactMuted.value ? `Muted notifications for ${selectedContact.value.name}` : `Unmuted notifications for ${selectedContact.value.name}`)
}

function toggleBlockContact() {
  isContactBlocked.value = !isContactBlocked.value
  showToast(isContactBlocked.value ? `${selectedContact.value.name} has been blocked` : `${selectedContact.value.name} has been unblocked`)
}

function viewProfile() {
  showMoreOptions.value = false
  const targetId = selectedContact.value.targetId || selectedContact.value.id
  router.push(`/user-profile/${targetId}`)
}

function confirmDeleteChat() {
  showMoreOptions.value = false
  currentMessages.value = []
  showToast(`Chat history with ${selectedContact.value.name} cleared.`)
}

function alertAction(actionName) {
  if (actionName === 'Profile') {
    viewProfile()
  } else if (actionName === 'Search') {
    toggleInChatSearch()
  } else if (actionName === 'Audio') {
    startAudioCall()
  } else if (actionName === 'Media, links and docs') {
    showMediaModal.value = true
  } else if (actionName === 'Chat theme') {
    showThemeModal.value = true
  } else if (actionName === 'Notifications & sounds') {
    toggleMuteContact()
  } else if (actionName === 'Pinned messages') {
    showPinnedModal.value = true
  } else if (actionName === 'Block') {
    toggleBlockContact()
  }
}

// Setup real-time listener for current user's chats in Firestore
function listenToUserChats() {
  if (chatsUnsubscribe) {
    chatsUnsubscribe()
    chatsUnsubscribe = null
  }

  const myUid = currentUserId.value
  try {
    const chatsQuery = query(
      collection(db, 'chats'),
      where('participants', 'array-contains', myUid)
    )

    chatsUnsubscribe = onSnapshot(chatsQuery, (snapshot) => {
      if (!snapshot.empty) {
        const liveChats = []
        snapshot.forEach((docSnap) => {
          const data = docSnap.data()
          const otherId = (data.participants || []).find(p => p !== myUid) || 'unknown'
          const name = data.participantNames?.[otherId] || 
                       data.recipientName || 
                       (otherId === 'admin' ? 'HomeSweet Support' : `User (${otherId.slice(0, 6)})`)
          const avatar = data.participantAvatars?.[otherId] || 
                         'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&q=80'

          let timeStr = 'Just now'
          if (data.lastMessageTime?.toDate) {
            timeStr = data.lastMessageTime.toDate().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          }

          liveChats.push({
            id: docSnap.id,
            targetId: otherId,
            name,
            preview: data.lastMessage || 'Open conversation',
            time: timeStr,
            avatar,
            email: `${name.toLowerCase().replace(/\s+/g, '')}@homesweet.com`,
            phone: '+855 12 345 678',
            rawTimestamp: data.lastMessageTime?.toMillis ? data.lastMessageTime.toMillis() : Date.now()
          })
        })

        // Sort recent chats first
        liveChats.sort((a, b) => b.rawTimestamp - a.rawTimestamp)

        // Merge live chats with default contacts avoiding duplicates
        const merged = [...liveChats]
        defaultContacts.forEach(dc => {
          if (!merged.some(c => c.targetId === dc.targetId || c.name.toLowerCase() === dc.name.toLowerCase())) {
            merged.push(dc)
          }
        })
        conversations.value = merged
      }
    }, (err) => {
      console.warn("Notice subscribing to chats:", err)
    })
  } catch (err) {
    console.warn("Chats listener initialization notice:", err)
  }
}

// Select contact and attach messages subcollection listener
function selectContact(contact) {
  selectedContact.value = contact
  setupMessagesListener(contact)
}

function setupMessagesListener(contact) {
  if (messagesUnsubscribe) {
    messagesUnsubscribe()
    messagesUnsubscribe = null
  }

  const myUid = currentUserId.value
  const targetId = contact.targetId || contact.id
  const chatId = getDeterministicChatId(myUid, targetId)

  // Initialize in-memory fallback messages
  const fallback = messageHistory.value[targetId] || [
    {
      sender: 'them',
      text: `Hi! This is ${contact.name}. How can I assist you with your rental?`,
      timestamp: 'Just now'
    }
  ]
  currentMessages.value = [...fallback]

  try {
    const msgsColl = collection(db, 'chats', chatId, 'messages')
    messagesUnsubscribe = onSnapshot(msgsColl, (snapshot) => {
      if (!snapshot.empty) {
        const liveList = []
        snapshot.forEach(d => {
          const m = d.data()
          liveList.push({
            id: d.id,
            sender: m.senderId === myUid ? 'me' : 'them',
            text: m.text || '',
            image: m.image || null,
            timestamp: m.time || m.timestamp || 'Just now',
            rawTime: m.createdAt?.toMillis ? m.createdAt.toMillis() : (m.timestamp?.toMillis ? m.timestamp.toMillis() : 0)
          })
        })
        // Sort chronologically in memory
        liveList.sort((a, b) => a.rawTime - b.rawTime)
        currentMessages.value = liveList
        scrollToBottom()
      }
    }, (err) => {
      console.warn("Realtime message subcollection notice:", err)
    })
  } catch (err) {
    console.warn("Realtime messaging listener notice:", err)
  }
}

async function sendCustomMessage(text, image = null) {
  if (!text && !image) return
  isSending.value = true

  const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  const myUid = currentUserId.value
  const targetId = selectedContact.value.targetId || selectedContact.value.id
  const chatId = getDeterministicChatId(myUid, targetId)

  // Optimistic UI push
  const optimisticMsg = {
    sender: 'me',
    text: text || '',
    image: image || null,
    timestamp: timeStr,
    rawTime: Date.now()
  }
  currentMessages.value.push(optimisticMsg)
  scrollToBottom()

  // Update conversation preview in sidebar
  const conv = conversations.value.find(c => (c.targetId || c.id) === targetId)
  if (conv) {
    conv.preview = text ? `You: ${text}` : 'You sent an image'
    conv.time = 'Just now'
  }

  try {
    // 1. Add message to subcollection
    await addDoc(collection(db, 'chats', chatId, 'messages'), {
      senderId: myUid,
      senderName: currentUserName.value,
      text: text || '',
      image: image || null,
      time: timeStr,
      timestamp: serverTimestamp(),
      createdAt: serverTimestamp()
    })

    // 2. Update parent conversation metadata
    await setDoc(doc(db, 'chats', chatId), {
      participants: [myUid, targetId],
      participantNames: {
        [myUid]: currentUserName.value,
        [targetId]: selectedContact.value.name || 'Recipient'
      },
      participantAvatars: {
        [myUid]: currentUserAvatar.value,
        [targetId]: selectedContact.value.avatar || ''
      },
      lastMessage: text || 'Sent an image',
      lastMessageTime: serverTimestamp(),
      updatedAt: serverTimestamp()
    }, { merge: true })
  } catch (err) {
    console.warn('Notice saving message to Firestore:', err)
  } finally {
    isSending.value = false
  }
}

async function sendMessage() {
  if (!messageInput.value.trim() || isSending.value) return
  const text = messageInput.value.trim()
  messageInput.value = ''
  await sendCustomMessage(text, null)
}

function scrollToBottom() {
  nextTick(() => {
    if (messagesContainerRef.value) {
      messagesContainerRef.value.scrollTop = messagesContainerRef.value.scrollHeight
    }
  })
}

function insertEmoji() {
  messageInput.value += ' 😊 '
}

onMounted(() => {
  // Listen for auth state changes to dynamically resolve user
  onAuthStateChanged(auth, (user) => {
    currentAuthUser.value = user
    listenToUserChats()
  })

  // Deep-link query parameters
  const queryTargetId = route.query.userId || route.query.landlordId
  const queryContactName = route.query.contact

  if (queryTargetId || queryContactName) {
    const matched = conversations.value.find(c => {
      if (queryTargetId && (c.targetId === queryTargetId || c.id === queryTargetId)) return true
      if (queryContactName && c.name.toLowerCase() === queryContactName.toLowerCase()) return true
      return false
    })

    if (matched) {
      selectContact(matched)
    } else {
      const newContact = {
        id: queryTargetId || 'contact_' + Date.now(),
        targetId: queryTargetId || 'contact_' + Date.now(),
        name: queryContactName || `Host (${(queryTargetId || '').slice(0, 6)})`,
        preview: 'Start a new conversation',
        time: 'Just now',
        avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&q=80',
        email: `${(queryContactName || 'contact').toLowerCase().replace(/\s+/g, '')}@homesweet.com`,
        phone: '+855 12 888 999'
      }
      conversations.value.unshift(newContact)
      selectContact(newContact)
    }
  } else {
    selectContact(conversations.value[0])
  }
})

onUnmounted(() => {
  if (messagesUnsubscribe) {
    messagesUnsubscribe()
    messagesUnsubscribe = null
  }
  if (chatsUnsubscribe) {
    chatsUnsubscribe()
    chatsUnsubscribe = null
  }
})
</script>

<style scoped>
/* Page Layout */
.chat-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  background: #ffffff;
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #2A2421;
}

/* ------------------- Top Nav Bar ------------------- */
.top-nav-bar {
  height: 60px;
  min-height: 60px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  border-bottom: 1px solid #EDE8E3;
  background: #ffffff;
  z-index: 10;
}

.logo-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  padding: 4px;
}

.logo-btn:hover {
  opacity: 0.8;
}

.nav-user-avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid #EDE8E3;
}

.nav-user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ------------------- Main 3-Column Container ------------------- */
.chat-main-container {
  flex: 1;
  display: flex;
  height: calc(100vh - 60px);
  overflow: hidden;
}

/* ==================== COLUMN 1: SIDEBAR ==================== */
.messages-sidebar {
  width: 330px;
  min-width: 300px;
  border-right: 1px solid #EDE8E3;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  height: 100%;
}

.sidebar-header {
  padding: 24px 24px 18px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.back-circle-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1.5px solid #5C4E4E;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #5C4E4E;
  transition: all 0.15s ease;
}

.back-circle-btn:hover {
  background: #FAF8F5;
  border-color: #473B3B;
}

.sidebar-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2A2421;
  letter-spacing: -0.3px;
}

.conversations-list {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.conversation-item {
  display: flex;
  align-items: center;
  padding: 12px 24px;
  cursor: pointer;
  transition: background 0.15s ease;
  gap: 14px;
  border-left: 3px solid transparent;
}

.conversation-item:hover {
  background: #FAF8F5;
}

.conversation-item.active {
  background: #FAF8F5;
  border-left-color: #5C4E4E;
}

.conv-avatar-wrap {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
}

.conv-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.conv-details {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.conv-name {
  font-size: 0.95rem;
  font-weight: 600;
  color: #2A2421;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.conv-preview {
  font-size: 0.8rem;
  color: #8C7E7E;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.conv-time {
  font-size: 0.78rem;
  color: #8C7E7E;
  flex-shrink: 0;
  font-weight: 500;
}

/* ==================== COLUMN 2: CONVERSATION ==================== */
.chat-conversation-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100%;
  background: #ffffff;
  border-right: 1px solid #EDE8E3;
  position: relative;
}

/* Active chat header */
.active-chat-header {
  height: 64px;
  min-height: 64px;
  padding: 0 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #EDE8E3;
  background: #ffffff;
}

.chat-recipient-info {
  display: flex;
  align-items: center;
  gap: 14px;
}

.recipient-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
}

.recipient-text {
  display: flex;
  flex-direction: column;
}

.recipient-name {
  font-size: 1.05rem;
  font-weight: 700;
  color: #2A2421;
}

.recipient-email {
  font-size: 0.8rem;
  color: #8C7E7E;
}

.header-more-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #5C4E4E;
  padding: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  transition: background 0.15s;
}

.header-more-btn:hover {
  background: #FAF8F5;
}

/* Message stream */
.message-stream-body {
  flex: 1;
  overflow-y: auto;
  padding: 24px 32px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: #ffffff;
}

.message-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  width: 100%;
}

.message-row.received {
  justify-content: flex-start;
}

.message-row.sent {
  justify-content: flex-end;
}

.bubble-avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
  margin-top: 18px;
  border: 1px solid #EDE8E3;
}

.bubble-content-wrap {
  display: flex;
  flex-direction: column;
  max-width: 620px;
}

.sender-name-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: #5C4E4E;
  margin-bottom: 6px;
  margin-left: 4px;
}

.message-bubble {
  border-radius: 18px;
  padding: 14px 18px;
  font-size: 0.92rem;
  line-height: 1.45;
  word-break: break-word;
}

.received-bubble {
  background: #FAF8F5;
  color: #2A2421;
  border: 1px solid #EDE8E3;
  border-top-left-radius: 4px;
}

.sent-bubble {
  background: #5C4E4E;
  color: #ffffff;
  border-top-right-radius: 4px;
  box-shadow: 0 2px 8px rgba(92, 78, 78, 0.15);
}

.message-row.sent .bubble-content-wrap {
  align-items: flex-end;
}

.message-status {
  font-size: 0.72rem;
  color: #8C7E7E;
  margin-top: 4px;
  margin-right: 4px;
}

.centered-timestamp {
  align-self: center;
  font-size: 0.75rem;
  font-weight: 500;
  color: #8C7E7E;
  margin: 12px 0;
}

/* Chat Input Bar */
.chat-input-bar {
  padding: 16px 28px 20px;
  background: #ffffff;
  border-top: 1px solid #EDE8E3;
}

.input-form {
  display: flex;
  align-items: center;
  gap: 14px;
}

.input-pill {
  flex: 1;
  display: flex;
  align-items: center;
  border: 1.5px solid #D1D5DB;
  border-radius: 9999px;
  height: 44px;
  padding: 0 16px;
  background: #FAF8F5;
  transition: all 0.15s ease;
}

.input-pill:focus-within {
  border-color: #5C4E4E;
  background: #ffffff;
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
}

.message-input-field {
  flex: 1;
  border: none;
  outline: none;
  font-size: 0.95rem;
  font-family: inherit;
  color: #2A2421;
  background: transparent;
}

.message-input-field::placeholder {
  color: #8C7E7E;
}

.emoji-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2px;
  color: #5C4E4E;
}

.emoji-btn:hover {
  color: #2A2421;
}

.outside-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.action-icon-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #5C4E4E;
  padding: 4px;
  transition: opacity 0.15s ease;
}

.action-icon-btn:hover {
  opacity: 0.7;
}

.send-message-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: #5C4E4E;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
  flex-shrink: 0;
}

.send-message-btn:hover:not(:disabled) {
  background: #473B3B;
  transform: scale(1.05);
}

.send-message-btn:disabled {
  background: #EAE6E2;
  color: #8C7E7E;
  cursor: not-allowed;
  transform: none;
}

/* ==================== COLUMN 3: CONTACT INFO ==================== */
.contact-info-sidebar {
  width: 360px;
  min-width: 320px;
  height: 100%;
  overflow-y: auto;
  padding: 28px 24px 36px;
  background: #ffffff;
  display: flex;
  flex-direction: column;
}

.contact-info-title {
  font-size: 1.15rem;
  font-weight: 700;
  text-align: center;
  color: #2A2421;
  margin-bottom: 20px;
}

.contact-profile-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-bottom: 24px;
}

.contact-big-avatar {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 14px rgba(92, 78, 78, 0.08);
  margin-bottom: 16px;
  border: 2px solid #EDE8E3;
}

.contact-big-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2A2421;
}

.contact-phone {
  margin-top: 4px;
  font-size: 0.88rem;
  color: #8C7E7E;
  font-weight: 500;
}

/* Quick Actions (Profile, Search, Audio) */
.quick-actions-row {
  display: flex;
  justify-content: center;
  gap: 28px;
  margin-bottom: 28px;
}

.quick-action-btn {
  background: none;
  border: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.quick-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  color: #5C4E4E;
  transition: all 0.15s ease;
}

.quick-action-btn:hover .quick-icon-wrap {
  background: #F4EDEA;
  border-color: #5C4E4E;
  color: #473B3B;
}

.quick-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: #2A2421;
}

/* Action Cards */
.action-cards-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.action-card {
  width: 100%;
  height: 48px;
  border: 1.5px solid #EDE8E3;
  border-radius: 10px;
  background: #ffffff;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
}

.action-card:hover {
  background: #FAF8F5;
  border-color: #5C4E4E;
}

.card-left {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.88rem;
  font-weight: 500;
  color: #2A2421;
}

.card-right {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #8C7E7E;
}

.count-badge {
  font-size: 0.82rem;
  color: #8C7E7E;
}

/* Delete chat */
.delete-chat-footer {
  margin-top: 36px;
  display: flex;
  justify-content: center;
}

.delete-chat-btn {
  background: none;
  border: none;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  color: #DC2626;
  cursor: pointer;
  transition: opacity 0.15s ease;
}

.delete-chat-btn:hover {
  opacity: 0.8;
}

/* Responsive Handling */
@media (max-width: 1100px) {
  .contact-info-sidebar {
    display: none;
  }
}

/* In-chat search bar */
.chat-search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 24px;
  background: #FAF8F5;
  border-bottom: 1px solid #EDE8E3;
}
.chat-search-input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.9rem;
  color: #2A2421;
  font-family: inherit;
}
.close-search-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  color: #8C7E7E;
  cursor: pointer;
}

/* Header Dropdown */
.chat-more-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(92, 78, 78, 0.12);
  border: 1px solid #EDE8E3;
  width: 210px;
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  z-index: 50;
}
.chat-more-dropdown button {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: transparent;
  border: none;
  border-radius: 8px;
  font-size: 0.88rem;
  font-family: inherit;
  color: #2A2421;
  cursor: pointer;
  width: 100%;
  text-align: left;
  transition: background 0.15s;
}
.chat-more-dropdown button:hover {
  background: #FAF8F5;
  color: #5C4E4E;
}
.chat-more-dropdown button.text-danger {
  color: #DC2626;
}
.chat-more-dropdown button.text-danger:hover {
  background: #fef2f2;
}

/* Bubble image */
.chat-photo-img {
  max-width: 280px;
  max-height: 240px;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  margin-bottom: 6px;
}

/* Calling Modal */
.call-overlay {
  position: fixed;
  inset: 0;
  background: rgba(42, 36, 33, 0.7);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.call-modal-card {
  background: #2A2421;
  color: #ffffff;
  border-radius: 24px;
  border: 1px solid #5C4E4E;
  padding: 36px 32px;
  width: 360px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-shadow: 0 25px 50px -12px rgba(42, 36, 33, 0.5);
  animation: scaleIn 0.25s ease-out;
}
.call-avatar-container {
  position: relative;
  width: 96px;
  height: 96px;
  margin-bottom: 20px;
}
.call-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #5C4E4E;
}
.call-pulse-ring {
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  border: 2px solid rgba(92, 78, 78, 0.5);
  animation: pulseRing 1.5s infinite ease-out;
}
@keyframes pulseRing {
  0% { transform: scale(0.95); opacity: 1; }
  100% { transform: scale(1.3); opacity: 0; }
}
.call-name {
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 6px;
  color: #ffffff;
}
.call-status {
  font-size: 0.9rem;
  color: #8C7E7E;
  margin-bottom: 28px;
}
.call-controls {
  display: flex;
  align-items: center;
  gap: 20px;
}
.call-action-btn {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}
.call-action-btn:hover {
  background: rgba(255, 255, 255, 0.22);
}
.call-action-btn.active {
  background: #5C4E4E;
}
.call-action-btn.end-call {
  background: #DC2626;
  width: 60px;
  height: 60px;
}
.call-action-btn.end-call:hover {
  background: #B91C1C;
  transform: scale(1.05);
}
.video-preview-box {
  width: 100%;
  height: 180px;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  margin-bottom: 24px;
  background: #1C1917;
}
.video-feed-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.simulated-camera-tag {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(0, 0, 0, 0.6);
  color: #22c55e;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
}

/* Shared Modal Styles */
.shared-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(42, 36, 33, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.shared-modal-card {
  background: #ffffff;
  border-radius: 18px;
  border: 1px solid #EDE8E3;
  width: 440px;
  max-width: 90vw;
  padding: 24px;
  box-shadow: 0 20px 40px rgba(92, 78, 78, 0.2);
}
.shared-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}
.shared-modal-header h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2A2421;
  margin: 0;
}
.modal-close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #8C7E7E;
  cursor: pointer;
}
.shared-media-tabs {
  display: flex;
  gap: 16px;
  border-bottom: 1px solid #EDE8E3;
  padding-bottom: 8px;
  margin-bottom: 16px;
  font-size: 0.9rem;
  color: #8C7E7E;
}
.shared-media-tabs .active-tab {
  color: #5C4E4E;
  font-weight: 600;
  border-bottom: 2px solid #5C4E4E;
  padding-bottom: 8px;
  margin-bottom: -9px;
}
.shared-media-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}
.shared-media-grid img {
  width: 100%;
  height: 120px;
  border-radius: 10px;
  object-fit: cover;
}

/* Theme picker */
.theme-options-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.theme-pill {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid #EDE8E3;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
  color: #2A2421;
}
.theme-pill:hover, .theme-pill.selected {
  border-color: #5C4E4E;
  background: #FAF8F5;
}
.theme-circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
}
.theme-circle.default { background: #5C4E4E; }
.theme-circle.emerald { background: #10b981; }
.theme-circle.indigo { background: #4f46e5; }
.theme-circle.rose { background: #e11d48; }

/* Pinned body */
.pinned-body {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.pinned-item {
  background: #FAF8F5;
  border: 1px solid #EDE8E3;
  border-radius: 12px;
  padding: 14px;
}
.pinned-tag {
  font-size: 0.8rem;
  font-weight: 700;
  color: #5C4E4E;
  display: block;
  margin-bottom: 4px;
}
.pinned-item p {
  margin: 0;
  font-size: 0.88rem;
  color: #2A2421;
  line-height: 1.4;
}

/* Report body */
.report-body {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.report-option {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  color: #2A2421;
  cursor: pointer;
}
.btn-submit-report {
  margin-top: 10px;
  padding: 12px;
  border-radius: 10px;
  background: #DC2626;
  color: #ffffff;
  border: none;
  font-weight: 600;
  cursor: pointer;
}

/* Toast */
.chat-toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: #2A2421;
  color: #ffffff;
  padding: 12px 24px;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  box-shadow: 0 10px 25px rgba(42, 36, 33, 0.2);
  z-index: 99999;
}
.toast-fade-enter-active, .toast-fade-leave-active {
  transition: all 0.3s ease;
}
.toast-fade-enter-from, .toast-fade-leave-to {
  opacity: 0;
  transform: translate(-50%, 15px);
}
</style>
