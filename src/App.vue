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

  /* Line Heights */
  --leading-tight: 1.2;
  --leading-snug: 1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.65;

  /* Letter Spacing */
  --tracking-tight: -0.025em;
  --tracking-snug: -0.015em;
  --tracking-normal: 0em;
  --tracking-wide: 0.025em;

  /* Transitions */
  --transition-fast: 0.15s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-normal: 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-body);
  background: var(--color-bg-canvas);
  color: var(--color-text-primary);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  width: 100%;
  min-height: 100vh;
}

/* Global Typography Hierarchy */
h1, .h1 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--color-text-primary);
}

h2, .h2 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--color-text-primary);
}

h3, .h3 {
  font-family: var(--font-body);
  font-weight: 600;
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-snug);
  color: var(--color-text-primary);
}

p {
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
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

/* Elevated Surface Cards */
.surface-card {
  background: var(--color-bg-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
}

.surface-card-hover:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: #dcd6cd;
}

/* Badge System */
.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.76rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  line-height: 1;
}

.badge-emerald {
  background: #ecfdf5;
  color: #047857;
  border: 1px solid #a7f3d0;
}

.badge-neutral {
  background: #f5f4f0;
  color: #57534e;
  border: 1px solid #e7e5e4;
}

.badge-amber {
  background: #fffbeb;
  color: #b45309;
  border: 1px solid #fde68a;
}

/* Standard Form Inputs */
.input-base {
  width: 100%;
  height: 44px;
  padding: 0 16px;
  background: #ffffff;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: inherit;
  font-size: 0.92rem;
  color: var(--color-text-primary);
  outline: none;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.input-base:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(92, 78, 78, 0.12);
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