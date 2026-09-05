<script setup lang="ts">
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="min-h-screen bg-brand-cream text-brand-dark font-sans">
    <NavBar />
    <main class="max-w-6xl mx-auto px-4 py-8">
      <router-view />
    </main>
    <Footer />
  </div>
</template>