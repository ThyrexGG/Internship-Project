<template>
  <div 
    class="property-image-container" 
    :class="{ 
      'is-interactive': interactive,
      'is-loaded': isLoaded 
    }"
    :style="{ 
      aspectRatio: aspectRatio,
      borderRadius: borderRadius 
    }"
  >
    <!-- Skeleton Loading Shimmer -->
    <div v-if="isLoading" class="image-shimmer-placeholder">
      <div class="shimmer-wave"></div>
    </div>

    <!-- Main Image -->
    <img 
      :src="computedSrc" 
      :alt="alt || 'Property image'" 
      class="property-image-element"
      :class="{ 'visible': isLoaded }"
      loading="lazy"
      @load="onImageLoad"
      @error="onImageError"
    />

    <!-- Subtle Vignette / Depth Overlay -->
    <div class="image-depth-overlay"></div>
  </div>
</template>

<script setup>
/* global defineProps */
import { ref, computed } from 'vue'

const props = defineProps({
  src: {
    type: String,
    default: ''
  },
  alt: {
    type: String,
    default: 'Property listing'
  },
  aspectRatio: {
    type: String,
    default: '16/10'
  },
  borderRadius: {
    type: String,
    default: 'var(--radius-lg, 14px)'
  },
  interactive: {
    type: Boolean,
    default: true
  },
  fallbackSrc: {
    type: String,
    default: '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg'
  }
})

const isLoading = ref(true)
const isLoaded = ref(false)
const hasError = ref(false)

const computedSrc = computed(() => {
  if (hasError.value || !props.src) {
    return props.fallbackSrc
  }
  return props.src
})

function onImageLoad() {
  isLoading.value = false
  isLoaded.value = true
}

function onImageError() {
  if (!hasError.value) {
    hasError.value = true
    isLoading.value = false
    isLoaded.value = true
  }
}
</script>

<style scoped>
.property-image-container {
  position: relative;
  width: 100%;
  overflow: hidden;
  background-color: #EAE6E2;
  box-shadow: 0 2px 10px rgba(92, 78, 78, 0.06);
  transition: transform var(--transition-normal, 0.25s ease), box-shadow var(--transition-normal, 0.25s ease);
}

.property-image-container.is-interactive:hover {
  box-shadow: 0 6px 20px rgba(92, 78, 78, 0.12);
}

.property-image-container.is-interactive:hover .property-image-element {
  transform: scale(1.03);
}

.property-image-element {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0;
  transition: opacity 0.35s ease, transform var(--transition-normal, 0.25s ease);
}

.property-image-element.visible {
  opacity: 1;
}

/* Depth overlay */
.image-depth-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(to top, rgba(42, 36, 33, 0.12) 0%, transparent 40%);
}

/* Skeleton Shimmer */
.image-shimmer-placeholder {
  position: absolute;
  inset: 0;
  background-color: #F2EDE9;
  overflow: hidden;
}

.shimmer-wave {
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.5) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  animation: shimmer 1.6s infinite ease-in-out;
  transform: translateX(-100%);
}

@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
</style>
