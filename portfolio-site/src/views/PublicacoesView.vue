<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import pubs from '../data/publicacoes-ultimos-5-anos.json'

const tipos = ['artigo', 'capitulo', 'anais', 'resumo', 'resumo_expandido']
const label: Record<string, string> = {
  artigo: 'Artigos em periódicos',
  capitulo: 'Capítulos de livro',
  anais: 'Anais completos',
  resumo: 'Resumos',
  resumo_expandido: 'Resumos expandidos',
}

const grouped = computed(() => {
  const map: Record<string, any[]> = {}
  for (const t of tipos) map[t] = []
  for (const p of pubs) if (map[p.tipo]) map[p.tipo].push(p)
  return map
})

const qualisArtigos = computed(() =>
  pubs.filter((p: any) => p.tipo === 'artigo' && p.qualis !== 'N/A')
)

const qualisCount = computed(() => {
  const c: Record<string, number> = {}
  for (const a of qualisArtigos.value) {
    c[a.qualis] = (c[a.qualis] || 0) + 1
  }
  return c
})
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Publicações</h1>
  <p class="text-brand-dark/60 mb-8">Últimos 5 anos</p>

  <section class="mb-8">
    <h2 class="text-xl font-bold text-brand-dark mb-4">Qualis (artigos em periódicos)</h2>
    <div class="flex gap-4 flex-wrap">
      <GlassCard v-for="(q, label) in qualisCount" :key="label">
        <p class="text-2xl font-bold text-brand-green">{{ q }}</p>
        <p class="text-sm text-brand-dark/60">Qualis {{ label }}</p>
      </GlassCard>
    </div>
  </section>

  <section v-for="t in tipos" :key="t">
    <h2 class="text-xl font-bold text-brand-dark mb-3 mt-8">{{ label[t] }} ({{ grouped[t].length }})</h2>
    <div class="space-y-3">
      <GlassCard v-for="p in grouped[t]" :key="p.titulo">
        <p class="text-xs text-brand-green font-semibold mb-1">{{ p.ano }} {{ p.qualis !== 'N/A' ? '· Qualis ' + p.qualis : '' }}</p>
        <h3 class="font-semibold text-brand-dark">{{ p.titulo }}</h3>
        <p class="text-sm text-brand-dark/60">{{ p.autores }}</p>
        <p class="text-xs text-brand-dark/40 mt-1">{{ p.veiculo }}</p>
      </GlassCard>
    </div>
  </section>
</template>