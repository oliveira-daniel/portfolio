<script setup lang="ts">
import { computed } from 'vue'
import { Brain, BusFront, FlaskConical, GraduationCap, Workflow, ArrowUpRight, Star } from 'lucide-vue-next'
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
  for (const r of portfolioItems as any[]) {
    if (!r.experimental && map[r.bloco]) map[r.bloco].push(r)
  }
  return map
})

const destaques = computed(() =>
  (portfolioItems as any[]).filter((r) => r.destaque && !r.experimental),
)

const experimentais = computed(() => (portfolioItems as any[]).filter((r) => r.experimental))

function linksOf(r: any) {
  return [
    r.link_demo ? { label: 'Demo', url: r.link_demo } : null,
    r.link_repo ? { label: 'Repo', url: r.link_repo } : null,
    r.link_artigo ? { label: 'Artigo', url: r.link_artigo } : null,
    r.link_externo ? { label: 'Ver mais', url: r.link_externo } : null,
  ].filter(Boolean) as { label: string; url: string }[]
}
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Portfólio</h1>
  <p class="text-brand-dark/60 mb-2">Projetos que conectam IA aplicada, produto, automação e pesquisa com problemas reais.</p>

  <section v-if="destaques.length" class="mt-6 rounded-2xl border border-brand-yellow/40 overflow-hidden bg-brand-yellow/[0.06] dark:bg-white/[0.04] dark:border-white/10">
    <h2 class="text-xl font-bold text-brand-dark px-6 py-4 flex items-center gap-2">
      Destaques
      <span class="badge badge-yellow">{{ destaques.length }}</span>
      <Star class="w-5 h-5 text-brand-yellow ml-auto shrink-0" />
    </h2>
    <div class="px-3 pb-3 border-t border-brand-green/10 dark:border-white/10 pt-3">
      <div class="grid md:grid-cols-2 gap-4">
        <GlassCard v-for="r in destaques" :key="r.name" class="flex flex-col">
          <div class="rounded-xl overflow-hidden bg-brand-green/[0.06] border border-brand-green/15 aspect-video flex items-center justify-center mb-3">
            <img
              v-if="r.imagem"
              :src="r.imagem"
              :alt="`Print do projeto ${r.name}`"
              class="w-full h-full object-cover"
              loading="lazy"
            />
            <span v-else class="text-xs text-brand-dark/40 px-4 text-center">Espaço para print</span>
          </div>
          <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
          <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
          <div v-if="r.contexto || r.papel || r.resultado" class="text-sm mt-3 space-y-1">
            <p v-if="r.contexto" class="text-brand-dark/70"><strong>Contexto:</strong> {{ r.contexto }}</p>
            <p v-if="r.papel" class="text-brand-dark/70"><strong>Papel:</strong> {{ r.papel }}</p>
            <p v-if="r.resultado" class="text-brand-dark/70"><strong>Resultado:</strong> {{ r.resultado }}</p>
          </div>
          <div v-if="(r.stack?.length || r.badges?.length)" class="flex flex-wrap gap-1.5 mt-3">
            <span v-for="s in (r.stack ?? r.badges ?? [])" :key="s" class="badge badge-green">{{ s }}</span>
          </div>
          <div class="flex flex-wrap items-center gap-2 mt-auto pt-4">
            <a
              v-for="l in linksOf(r)"
              :key="l.label"
              :href="l.url"
              target="_blank"
              rel="noopener"
              class="inline-flex items-center gap-1 text-sm font-semibold text-brand-green hover:underline"
            >
              {{ l.label }} <ArrowUpRight class="w-3.5 h-3.5" />
            </a>
            <span v-if="r.cliente || r.instituicao" class="text-xs text-brand-dark/40 ml-auto">{{ r.cliente ?? r.instituicao }}</span>
          </div>
        </GlassCard>
      </div>
    </div>
  </section>

  <section v-for="b in blocos" :key="b" class="mt-10 first:mt-6 rounded-2xl border border-brand-green/15 overflow-hidden bg-white/40 backdrop-blur-sm dark:bg-white/[0.04] dark:border-white/10">
    <h2 class="text-xl font-bold text-brand-dark px-6 py-4 flex items-center gap-2">
      {{ b }}
      <span class="badge badge-yellow">{{ porBloco[b].length }}</span>
      <component :is="blocoIcons[b]" class="w-5 h-5 text-brand-green ml-auto shrink-0" />
    </h2>
    <div class="px-3 pb-3 border-t border-brand-green/10 dark:border-white/10 pt-3 bg-brand-green/[0.02] dark:bg-white/[0.02]">
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="r in porBloco[b]" :key="r.name" class="flex flex-col">
        <div class="rounded-xl overflow-hidden bg-brand-green/[0.06] border border-brand-green/15 aspect-video flex items-center justify-center mb-3">
          <img
            v-if="r.imagem"
            :src="r.imagem"
            :alt="`Print do projeto ${r.name}`"
            class="w-full h-full object-cover"
            loading="lazy"
          />
          <span v-else class="text-xs text-brand-dark/40 px-4 text-center">Espaço para print</span>
        </div>
        <h3 class="font-semibold text-brand-dark">{{ r.name }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ r.description || '—' }}</p>
        <div v-if="r.contexto || r.papel || r.resultado" class="text-sm mt-3 space-y-1">
          <p v-if="r.contexto" class="text-brand-dark/70"><strong>Contexto:</strong> {{ r.contexto }}</p>
          <p v-if="r.papel" class="text-brand-dark/70"><strong>Papel:</strong> {{ r.papel }}</p>
          <p v-if="r.resultado" class="text-brand-dark/70"><strong>Resultado:</strong> {{ r.resultado }}</p>
        </div>
        <div v-if="(r.stack?.length || r.badges?.length || r.periodo)" class="flex flex-wrap items-center gap-1.5 mt-3">
          <span v-for="badge in (r.stack ?? r.badges ?? [])" :key="badge" class="badge badge-green">{{ badge }}</span>
          <span v-if="r.periodo" class="text-xs text-brand-dark/40 ml-auto">{{ r.periodo }}</span>
        </div>
        <div v-if="linksOf(r).length || r.cliente || r.instituicao" class="flex flex-wrap items-center gap-2 mt-auto pt-4">
          <a
            v-for="l in linksOf(r)"
            :key="l.label"
            :href="l.url"
            target="_blank"
            rel="noopener"
            class="inline-flex items-center gap-1 text-sm font-semibold text-brand-green hover:underline"
          >
            {{ l.label }} <ArrowUpRight class="w-3.5 h-3.5" />
          </a>
          <span v-if="r.cliente || r.instituicao" class="text-xs text-brand-dark/40 ml-auto">{{ r.cliente ?? r.instituicao }}</span>
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
          <span class="badge badge-green">{{ r.bloco }}</span>
          <span v-for="badge in (r.badges ?? [])" :key="badge" class="badge badge-green">{{ badge }}</span>
        </div>
      </GlassCard>
    </div>
    </div>
  </section>
</template>
