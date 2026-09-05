<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'

const isDark = ref(false)

onMounted(() => {
  const stored = localStorage.getItem('theme')
  if (stored === 'dark' || (!stored && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true
  }
  applyTheme()
})

watch(isDark, () => {
  applyTheme()
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
})

function applyTheme() {
  document.documentElement.classList.toggle('dark', isDark.value)
}

function toggleDark() {
  isDark.value = !isDark.value
}
</script>

<template>
  <div class="font-sans transition-colors duration-300">
    <NavBar :is-dark="isDark" @toggle-dark="toggleDark" />
    <main class="max-w-6xl mx-auto px-4 py-8">
      <router-view />
    </main>
    <Footer />
  </div>
</template>