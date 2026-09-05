<script setup lang="ts">
import { computed } from 'vue'
import GlassCard from '../components/GlassCard.vue'
import QualisChart from '../components/QualisChart.vue'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import ori from '../data/orientacoes.json'

const artigos = computed(() => pubs.filter((p: any) => p.tipo === 'artigo'))
const artigosSemC = computed(() => artigos.value.filter((p: any) => p.qualis !== 'C'))
const capitulos = computed(() => pubs.filter((p: any) => p.tipo === 'capitulo'))
const anais = computed(() => pubs.filter((p: any) => ['anais', 'resumo', 'resumo_expandido'].includes(p.tipo)))

const qualisCount = computed(() => {
  const c: Record<string, number> = {}
  for (const a of artigosSemC.value) {
    c[a.qualis] = (c[a.qualis] || 0) + 1
  }
  return c
})

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

const concluidas = computed(() => ori.filter((o: any) => o.situacao === 'Concluída'))
const aIniciar = computed(() => ori.filter((o: any) => o.situacao === 'A iniciar'))
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Acadêmico</h1>
  <p class="text-brand-dark/60 mb-2">Últimos 5 anos</p>

  <section class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ artigos.length }}</p>
      <p class="text-sm text-brand-dark/60">Artigos</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ capitulos.length }}</p>
      <p class="text-sm text-brand-dark/60">Capítulos</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ anais.length }}</p>
      <p class="text-sm text-brand-dark/60">Em anais</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ concluidas.length }}</p>
      <p class="text-sm text-brand-dark/60">Orientações</p>
    </GlassCard>
  </section>

  <section class="mb-8">
    <h2 class="text-xl font-bold text-brand-dark mb-4">Qualis (artigos, exceto C)</h2>
    <QualisChart :counts="qualisCount" />
    <div class="flex gap-4 flex-wrap mt-4">
      <GlassCard v-for="(q, label) in qualisCount" :key="label">
        <p class="text-2xl font-bold text-brand-green">{{ q }}</p>
        <p class="text-sm text-brand-dark/60">Qualis {{ label }}</p>
      </GlassCard>
    </div>
  </section>

  <section class="mb-8">
    <h2 class="text-xl font-bold text-brand-dark mb-4">Orientações — Concluídas ({{ concluidas.length }})</h2>
    <div class="space-y-3">
      <GlassCard v-for="o in concluidas" :key="o.aluno">
        <p class="text-xs text-brand-green font-semibold mb-1">{{ o.ano }} · {{ o.tipo }}</p>
        <h3 class="font-semibold text-brand-dark">{{ o.aluno }}</h3>
        <p class="text-sm text-brand-dark/60">{{ o.titulo }}</p>
        <p class="text-xs text-brand-dark/40 mt-1">{{ o.programa }}</p>
      </GlassCard>
    </div>
    <div v-if="aIniciar.length" class="mt-6">
      <h3 class="text-lg font-bold text-brand-dark mb-3">Em andamento</h3>
      <GlassCard v-for="o in aIniciar" :key="o.aluno">
        <p class="text-xs text-brand-yellow font-semibold mb-1">{{ o.ano }} · {{ o.tipo }}</p>
        <h3 class="font-semibold text-brand-dark">{{ o.aluno }}</h3>
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