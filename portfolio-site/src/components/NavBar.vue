<script setup lang="ts">
import { useRoute } from 'vue-router'
import { Sun, Moon } from '@lucide/vue'

defineProps<{ isDark: boolean }>()
defineEmits<{ toggleDark: [] }>()

const route = useRoute()

const links = [
  { path: '/', label: 'Início' },
  { path: '/servicos', label: 'Serviços' },
  { path: '/academico', label: 'Acadêmico' },
  { path: '/projetos', label: 'Projetos' },
  { path: '/blog', label: 'Blog' },
]
</script>

<template>
  <nav class="sticky top-0 z-50 glass">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-4 py-3">
      <router-link to="/" class="text-xl font-bold" :class="isDark ? 'text-white' : 'text-brand-dark'">
        Daniel Oliveira
      </router-link>
      <div class="flex items-center gap-6">
        <router-link
          v-for="l in links"
          :key="l.path"
          :to="l.path"
          class="text-sm font-medium transition-colors"
          :class="route.path === l.path ? 'text-brand-yellow' : 'text-brand-dark/70 hover:text-brand-dark'"
        >
          {{ l.label }}
        </router-link>
        <button
          @click="$emit('toggleDark')"
          class="glass rounded-full p-2 transition-transform hover:scale-110"
          :title="isDark ? 'Modo claro' : 'Modo escuro'"
        >
          <Sun v-if="isDark" class="w-4 h-4 text-brand-yellow" />
          <Moon v-else class="w-4 h-4 text-brand-dark" />
        </button>
      </div>
    </div>
  </nav>
</template>