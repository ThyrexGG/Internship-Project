<template>
  <RouterView />
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const handleSecretAdminShortcut = (e) => {
  // Secret combination: Ctrl + Shift + A (or Cmd + Shift + A on Mac)
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'A' || e.key === 'a')) {
    e.preventDefault()
    router.push('/admin')
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleSecretAdminShortcut)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleSecretAdminShortcut)
})
</script>

<style>
:root {
  /* Color Palette */
  --color-primary: #5C4E4E;
  --color-primary-hover: #473B3B;
  --color-primary-dark: #2A2421;
  --color-primary-light: #F2EDE9;
  --color-text-primary: #2A2421;
  --color-text-secondary: #5C4E4E;
  --color-text-muted: #8C7E7E;
  --color-bg-canvas: #faf8f5;
  --color-bg-surface: #ffffff;
  --color-border: #ede8e3;
  --color-border-subtle: #f2eee9;
  
  /* Status Colors */
  --color-success: #10B981;
  --color-success-bg: #ECFDF5;
  --color-warning: #F59E0B;
  --color-warning-bg: #FEF3C7;
  --color-error: #EF4444;
  --color-error-bg: #FEE2E2;
  --color-info: #3B82F6;
  --color-info-bg: #EFF6FF;

  /* Spacing Scale */
  --spacing-2xs: 2px;
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  --spacing-3xl: 64px;
  --container-max: 1280px;
  --container-gutter: 24px;

  /* Corner Radii */
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;
  --radius-2xl: 24px;
  --radius-pill: 50px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(92, 78, 78, 0.05);
  --shadow-md: 0 4px 16px rgba(92, 78, 78, 0.06);
  --shadow-lg: 0 10px 30px rgba(92, 78, 78, 0.08);
  --shadow-dropdown: 0 12px 36px rgba(42, 36, 33, 0.12), 0 4px 12px rgba(42, 36, 33, 0.06);

  /* Typography */
  --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-serif: 'DM Serif Display', Georgia, serif;

  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-normal: 0.25s ease;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-body);
  background: var(--color-bg-canvas);
  color: var(--color-text-primary);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  width: 100%;
  min-height: 100vh;
}

/* Global Container Utilities */
.app-container {
  width: 100%;
  max-width: var(--container-max);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--container-gutter);
  padding-right: var(--container-gutter);
}

/* Custom Scrollbars */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: var(--radius-pill);
}
::-webkit-scrollbar-thumb:hover {
  background: var(--color-text-muted);
}
</style>