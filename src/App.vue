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
  --color-favorite: #E11D48;
  --color-favorite-hover: #BE123C;

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

  /* Shadows & Spatial Elevation Tiers */
  /* Level 0: Canvas Substrate (none) */
  --elevation-0: none;

  /* Level 1: Grounded Base Surfaces (Contact + Ambient + Specular Top Bevel) */
  --shadow-elevation-1: 0 1px 2px rgba(42, 36, 33, 0.04), 0 4px 12px rgba(42, 36, 33, 0.03);
  --shadow-elevation-1-specular: inset 0 1px 0 rgba(255, 255, 255, 0.85), 0 1px 2px rgba(42, 36, 33, 0.04), 0 4px 12px rgba(42, 36, 33, 0.03);

  /* Level 2: Interactive Lifted Surfaces (Hover, Active Cards, Floating Pills) */
  --shadow-elevation-2: 0 2px 6px -1px rgba(42, 36, 33, 0.05), 0 8px 24px -4px rgba(42, 36, 33, 0.08);
  --shadow-elevation-2-specular: inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 2px 6px -1px rgba(42, 36, 33, 0.05), 0 10px 24px -4px rgba(42, 36, 33, 0.08);

  /* Level 3: Floating Navigation Docks, Sticky Headers, Scrims */
  --shadow-elevation-3: 0 4px 12px -2px rgba(42, 36, 33, 0.06), 0 14px 34px -4px rgba(42, 36, 33, 0.12);

  /* Level 4: Popovers, Dropdowns, Datepickers & Flyouts */
  --shadow-elevation-4: 0 6px 16px -2px rgba(42, 36, 33, 0.08), 0 20px 44px -6px rgba(42, 36, 33, 0.16);

  /* Level 5: Modals, Dialogs, Drawers & Lightboxes */
  --shadow-elevation-5: 0 10px 24px -4px rgba(42, 36, 33, 0.10), 0 28px 64px -8px rgba(42, 36, 33, 0.22);

  /* Backward Compatibility Aliases */
  --shadow-sm: var(--shadow-elevation-1);
  --shadow-md: var(--shadow-elevation-2);
  --shadow-lg: var(--shadow-elevation-3);
  --shadow-dropdown: var(--shadow-elevation-4);

  /* Frosted Glassmorphism Tokens */
  --glass-bg: rgba(255, 255, 255, 0.88);
  --glass-border: rgba(255, 255, 255, 0.7);
  --glass-blur: blur(16px) saturate(180%);
  --scrim-backdrop: rgba(26, 22, 20, 0.45);
  --scrim-blur: blur(8px);

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
  --transition-fast: 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-normal: 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

@media (max-width: 640px) {
  :root {
    --container-gutter: 16px;
    --spacing-lg: 16px;
    --spacing-xl: 24px;
    --spacing-2xl: 32px;
  }
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  overflow-x: hidden;
  max-width: 100vw;
}

body {
  font-family: var(--font-body);
  background: var(--color-bg-canvas);
  color: var(--color-text-primary);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-bottom: env(safe-area-inset-bottom);
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

/* Spatial Layering & Elevated Surface Cards */
.surface-card {
  background: var(--color-bg-surface);
  border: 1px solid rgba(220, 214, 205, 0.7);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-elevation-1-specular);
  transition: transform var(--transition-normal), box-shadow var(--transition-normal), border-color var(--transition-normal);
}

.surface-card-hover {
  cursor: pointer;
}

.surface-card-hover:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-elevation-2-specular);
  border-color: #cfc7bc;
}

/* Explicit Spatial Elevation Utility Classes */
.elevation-0 {
  box-shadow: var(--elevation-0);
  background: transparent;
}

.elevation-1 {
  background: var(--color-bg-surface);
  border: 1px solid rgba(220, 214, 205, 0.7);
  box-shadow: var(--shadow-elevation-1-specular);
  border-radius: var(--radius-lg);
  transition: transform var(--transition-normal), box-shadow var(--transition-normal), border-color var(--transition-normal);
}

.elevation-2 {
  background: var(--color-bg-surface);
  border: 1px solid rgba(220, 214, 205, 0.75);
  box-shadow: var(--shadow-elevation-2-specular);
  border-radius: var(--radius-lg);
  transition: transform var(--transition-normal), box-shadow var(--transition-normal), border-color var(--transition-normal);
}

.elevation-3 {
  background: var(--color-bg-surface);
  border: 1px solid rgba(255, 255, 255, 0.8);
  box-shadow: var(--shadow-elevation-3);
  border-radius: var(--radius-xl);
}

.elevation-4 {
  background: var(--color-bg-surface);
  border: 1px solid rgba(220, 214, 205, 0.8);
  box-shadow: var(--shadow-elevation-4);
  border-radius: var(--radius-lg);
}

.elevation-5 {
  background: var(--color-bg-surface);
  border: 1px solid rgba(255, 255, 255, 0.6);
  box-shadow: var(--shadow-elevation-5);
  border-radius: var(--radius-2xl);
}

/* Frosted Glass Layer */
.glass-surface {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  box-shadow: var(--shadow-elevation-3);
}

/* Tactile Pill & Button Surfacing */
.tactile-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  border: 1px solid rgba(220, 214, 205, 0.75);
  border-radius: var(--radius-pill);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.95), 0 1px 3px rgba(42, 36, 33, 0.04);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
}

.tactile-pill:hover {
  transform: translateY(-1px);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.95), 0 4px 10px rgba(42, 36, 33, 0.08);
  border-color: #cfc7bc;
}

.tactile-pill:active {
  transform: translateY(0);
  box-shadow: inset 0 1px 2px rgba(42, 36, 33, 0.08);
}

/* Recessed Inset Well (For Dropzones, Empty States, Input Groups) */
.recessed-well {
  background: #f5f2ed;
  border: 1px solid rgba(220, 214, 205, 0.8);
  box-shadow: inset 0 2px 4px rgba(42, 36, 33, 0.04);
  border-radius: var(--radius-md);
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

@keyframes heartPop {
  0% { transform: scale(1); }
  35% { transform: scale(1.28); }
  65% { transform: scale(0.92); }
  100% { transform: scale(1); }
}

.heart-pop {
  animation: heartPop 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
</style>