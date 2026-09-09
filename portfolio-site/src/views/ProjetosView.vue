<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import portfolioItems from '../data/portfolio.json'

const categories = computed(() => {
  const map: Record<string, any[]> = {}
  for (const r of portfolioItems) {
    if (!map[r.category]) map[r.category] = []
    map[r.category].push(r)
  }
  return map
})
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Portfólio</h1>
  <p class="text-brand-dark/60 mb-8">{{ portfolioItems.length }} produtos de autoria ou co-autoria</p>

  <section v-for="(items, cat) in categories" :key="cat">
    <h2 class="text-xl font-bold text-brand-dark mb-3 mt-6">{{ cat }} ({{ items.length }})</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in items" :key="r.name">
        <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
        <p v-if="r.periodo" class="text-xs text-brand-dark/40 mt-1">{{ r.periodo }}</p>
      </GlassCard>
    </div>
  </section>
</template>