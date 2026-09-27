<template>
  <div ref="viewerEl" class="panorama-viewer"></div>
</template>

<script setup>
/* global defineProps */
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import 'pannellum/build/pannellum.css'
import 'pannellum/build/pannellum.js'

const props = defineProps({
  imageUrl: {
    type: String,
    required: true
  }
})

const viewerEl = ref(null)
let viewerInstance = null

function destroyViewer() {
  if (viewerInstance) {
    viewerInstance.destroy()
    viewerInstance = null
  }
}

function initViewer() {
  destroyViewer()
  if (!viewerEl.value || !window.pannellum || !props.imageUrl) return

  viewerInstance = window.pannellum.viewer(viewerEl.value, {
    type: 'equirectangular',
    panorama: props.imageUrl,
    autoLoad: true,
    autoRotate: -2,
    compass: false,
    showZoomCtrl: true,
    mouseZoom: true,
    draggable: true,
    hfov: 100
  })
}

watch(() => props.imageUrl, initViewer)
onMounted(initViewer)
onBeforeUnmount(destroyViewer)
</script>

<style scoped>
.panorama-viewer {
  width: 100%;
  height: 100%;
  min-height: 320px;
  background: #1A1512;
}
</style>
