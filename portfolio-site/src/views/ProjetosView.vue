<script setup lang="ts">
import { computed } from 'vue'
import { Brain, BusFront, FlaskConical, GraduationCap, Workflow } from 'lucide-vue-next'
import GlassCard from '../components/GlassCard.vue'
import portfolioItems from '../data/portfolio.json'

const blocos = ['IA Aplicada', 'Produtos Educacionais', 'Transporte Urbano', 'Automações']

const blocoIcons: Record<string, any> = {
  'IA Aplicada': Brain,
  'Produtos Educacionais': GraduationCap,
  'Transporte Urbano': BusFront,
  'Automações': Workflow,
}

const porBloco = computed(() => {
  const map: Record<string, any[]> = {}
  for (const b of blocos) map[b] = []
  for (const r of portfolioItems) {
    if (!r.experimental && map[(r as any).bloco]) map[(r as any).bloco].push(r)
  }
  return map
})

const experimentais = computed(() => portfolioItems.filter((r) => (r as any).experimental))
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Portfólio</h1>

  <section v-for="b in blocos" :key="b" class="mt-10 first:mt-6 rounded-2xl border border-brand-green/15 overflow-hidden bg-white/40 backdrop-blur-sm dark:bg-white/[0.04] dark:border-white/10">
    <h2 class="text-xl font-bold text-brand-dark px-6 py-4 flex items-center gap-2">
      {{ b }}
      <span class="badge badge-yellow">{{ porBloco[b].length }}</span>
      <component :is="blocoIcons[b]" class="w-5 h-5 text-brand-green ml-auto shrink-0" />
    </h2>
    <div class="px-3 pb-3 border-t border-brand-green/10 dark:border-white/10 pt-3 bg-brand-green/[0.02] dark:bg-white/[0.02]">
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in porBloco[b]" :key="r.name" class="flex flex-col">
        <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
        <div v-if="(r as any).badges?.length || (r as any).periodo" class="flex flex-wrap items-center gap-1.5 mt-auto pt-5">
          <span v-for="badge in ((r as any).badges ?? [])" :key="badge" class="badge badge-green">{{ badge }}</span>
          <span v-if="(r as any).periodo" class="text-xs text-brand-dark/40 ml-auto">{{ (r as any).periodo }}</span>
        </div>
      </GlassCard>
    </div>
    </div>
  </section>

  <section v-if="experimentais.length" class="mt-10 rounded-2xl border border-brand-green/15 overflow-hidden bg-white/40 backdrop-blur-sm dark:bg-white/[0.04] dark:border-white/10">
    <h2 class="text-xl font-bold text-brand-dark px-6 py-4 flex items-center gap-2">
      Experimentais
      <span class="badge badge-yellow">{{ experimentais.length }}</span>
      <FlaskConical class="w-5 h-5 text-brand-green ml-auto shrink-0" />
    </h2>
    <div class="px-3 pb-3 border-t border-brand-green/10 dark:border-white/10 pt-3 bg-brand-green/[0.02] dark:bg-white/[0.02]">
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in experimentais" :key="r.name" class="flex flex-col">
        <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
        <div class="flex flex-wrap items-center gap-1.5 mt-auto pt-5">
          <span class="badge badge-green">{{ (r as any).bloco }}</span>
          <span v-for="badge in ((r as any).badges ?? [])" :key="badge" class="badge badge-green">{{ badge }}</span>
        </div>
      </GlassCard>
    </div>
    </div>
  </section>
</template>
