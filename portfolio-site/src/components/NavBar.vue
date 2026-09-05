<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
const router = useRouter()
const route = useRoute()

const links = [
  { path: '/', label: 'Início' },
  { path: '/publicacoes', label: 'Publicações' },
  { path: '/projetos', label: 'Projetos' },
  { path: '/consultoria', label: 'Consultoria' },
  { path: '/orientacao', label: 'Orientação' },
  { path: '/blog', label: 'Blog' },
]
</script>

<template>
  <nav class="sticky top-0 z-50 glass">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-4 py-3">
      <router-link to="/" class="text-xl font-bold text-brand-dark">
        Daniel Oliveira
      </router-link>
      <div class="flex gap-6">
        <router-link
          v-for="l in links"
          :key="l.path"
          :to="l.path"
          class="text-sm font-medium transition-colors"
          :class="route.path === l.path ? 'text-brand-yellow' : 'text-brand-dark/70 hover:text-brand-dark'"
        >
          {{ l.label }}
        </router-link>
      </div>
    </div>
  </nav>
</template>