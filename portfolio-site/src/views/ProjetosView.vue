<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import repos from '../data/github-repos.json'

const categories = computed(() => {
  const map: Record<string, any[]> = {}
  for (const r of repos) {
    if (!map[r.category]) map[r.category] = []
    map[r.category].push(r)
  }
  return map
})

const portfolio = [
  {
    nome: 'Dynamic Transport Network Prototype v2 / Dynamic Transport System Simulator Beta',
    descricao: 'Protótipo e simulador de rede dinâmica de transporte para crise rodoviária (tese de doutorado)',
    periodo: '2013–2018',
  },
]
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Portfólio</h1>
  <p class="text-brand-dark/60 mb-8">{{ repos.length }} repositórios no GitHub</p>

  <section v-if="portfolio.length" class="mb-8">
    <h2 class="text-xl font-bold text-brand-dark mb-3 mt-6">Softwares & Protótipos ({{ portfolio.length }})</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="p in portfolio" :key="p.nome">
        <div class="flex items-center gap-2 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider text-brand-yellow">software</span>
        </div>
        <h3 class="font-semibold text-brand-dark">{{ p.nome }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ p.descricao }}</p>
        <p class="text-xs text-brand-dark/40 mt-1">{{ p.periodo }}</p>
      </GlassCard>
    </div>
  </section>

  <section v-for="(items, cat) in categories" :key="cat">
    <h2 class="text-xl font-bold text-brand-dark mb-3 mt-6">{{ cat }} ({{ items.length }})</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in items" :key="r.name">
        <div class="flex items-center gap-2 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider"
            :class="r.visibility === 'public' ? 'text-brand-green' : 'text-brand-yellow'"
          >{{ r.visibility }}</span>
        </div>
        <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
      </GlassCard>
    </div>
  </section>
</template>