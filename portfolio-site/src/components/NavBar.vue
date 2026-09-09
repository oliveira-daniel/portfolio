<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { Sun, Moon, Menu, X } from '@lucide/vue'
import BrandIcon from './BrandIcon.vue'
import contato from '../data/contato.json'
import brandIcons from '../data/brand-icons.json'

defineProps<{ isDark: boolean }>()
defineEmits<{ toggleDark: [] }>()

const route = useRoute()
const open = ref(false)

const links = [
  { path: '/', label: 'Início' },
  { path: '/servicos', label: 'Serviços' },
  { path: '/projetos', label: 'Portfólio' },
  { path: '/academico', label: 'Acadêmico' },
  { path: '/blog', label: 'Blog' },
]

function close() {
  open.value = false
}
</script>

<template>
  <nav class="sticky top-0 z-50 glass">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-4 py-3 gap-3">
      <router-link to="/" class="text-xl font-bold shrink-0" :class="isDark ? 'text-white' : 'text-brand-dark'" @click="close">
        Daniel de Oliveira
      </router-link>
      <div class="hidden md:flex items-center gap-6">
        <router-link
          v-for="l in links"
          :key="l.path"
          :to="l.path"
          class="text-sm font-medium transition-colors focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-green rounded"
          :class="route.path === l.path ? 'text-brand-green font-bold' : 'text-brand-dark/70 hover:text-brand-dark'"
        >
          {{ l.label }}
        </router-link>
        <a
          :href="contato.whatsappLink"
          target="_blank"
          rel="noopener"
          class="inline-flex items-center gap-1.5 bg-brand-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:scale-105 transition-transform"
        >
          <BrandIcon :path="brandIcons.whatsapp.path" hex="FFFFFF" label="WhatsApp" />
          Contato
        </a>
        <button
          @click="$emit('toggleDark')"
          class="glass rounded-full p-2 transition-transform hover:scale-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-green"
          :title="isDark ? 'Modo claro' : 'Modo escuro'"
          :aria-label="isDark ? 'Ativar modo claro' : 'Ativar modo escuro'"
        >
          <Sun v-if="isDark" class="w-4 h-4 text-brand-yellow" />
          <Moon v-else class="w-4 h-4 text-brand-dark" />
        </button>
      </div>
      <div class="flex md:hidden items-center gap-2">
        <a
          :href="contato.whatsappLink"
          target="_blank"
          rel="noopener"
          aria-label="Falar no WhatsApp"
          class="inline-flex items-center gap-1.5 bg-brand-green text-white px-3 py-2 rounded-lg text-sm font-semibold"
        >
          <BrandIcon :path="brandIcons.whatsapp.path" hex="FFFFFF" label="WhatsApp" />
          Contato
        </a>
        <button
          @click="$emit('toggleDark')"
          class="glass rounded-full p-2"
          :title="isDark ? 'Modo claro' : 'Modo escuro'"
          :aria-label="isDark ? 'Ativar modo claro' : 'Ativar modo escuro'"
        >
          <Sun v-if="isDark" class="w-4 h-4 text-brand-yellow" />
          <Moon v-else class="w-4 h-4 text-brand-dark" />
        </button>
        <button
          @click="open = !open"
          class="glass rounded-lg p-2"
          aria-label="Abrir menu de navegação"
          :aria-expanded="open"
        >
          <X v-if="open" class="w-5 h-5 text-brand-dark" />
          <Menu v-else class="w-5 h-5 text-brand-dark" />
        </button>
      </div>
    </div>
    <div v-if="open" class="md:hidden border-t border-brand-green/10 px-4 py-3">
      <div class="flex flex-col gap-1">
        <router-link
          v-for="l in links"
          :key="l.path"
          :to="l.path"
          @click="close"
          class="px-3 py-2.5 rounded-lg text-sm font-medium"
          :class="route.path === l.path ? 'bg-brand-green/15 text-brand-green font-bold' : 'text-brand-dark/70 hover:bg-brand-green/10'"
        >
          {{ l.label }}
        </router-link>
      </div>
    </div>
  </nav>
</template>
