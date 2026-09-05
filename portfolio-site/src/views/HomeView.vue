<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
import repos from '../data/github-repos.json'
import pubs from '../data/publicacoes-ultimos-5-anos.json'
import ori from '../data/orientacoes.json'
import projetos from '../data/projetos.json'

const artigos = pubs.filter((p: any) => p.tipo === 'artigo' && p.qualis !== 'C')
const artigosTotal = pubs.filter((p: any) => p.tipo === 'artigo').length
const capitulos = pubs.filter((p: any) => p.tipo === 'capitulo').length
const anais = pubs.filter((p: any) => ['anais', 'resumo', 'resumo_expandido'].includes(p.tipo)).length
const mestrados = ori.filter((o: any) => o.tipo === 'mestrado' && o.situacao === 'Concluída').length
const reposIA = repos.filter((r: any) => r.category === 'Machine Learning & AI').length

const ativos = projetos.filter((p: any) => p.situacao === 'Em andamento')
</script>

<template>
  <section class="mb-12">
    <GlassCard>
      <div class="flex flex-col md:flex-row gap-8 items-center">
        <div class="w-32 h-32 rounded-full bg-brand-green/20 flex items-center justify-center text-4xl font-bold text-brand-green shrink-0">
          D
        </div>
        <div>
          <h1 class="text-4xl font-bold text-brand-dark mb-2">Daniel Oliveira</h1>
          <p class="text-brand-dark/80 leading-relaxed">
            CTO e sócio-fundador da <strong>ProFuzzy</strong> (1998–atual), Professor no PPG Ensino de Ciências da Unigranrio e pesquisador no <strong>GPIAE/DEGC/UFSC</strong>. Doutor em Engenharia de Produção (UFSC/INSA-Rouen), mestre em Computação (Univali). Atua na interseção entre Inteligência Artificial, otimização combinatória e educação — com experiência em sistemas neuro-fuzzy, agentes multiagentes, LLMs, RAG, e plataformas de IA para concessões, saúde e transporte.
          </p>
        </div>
      </div>
    </GlassCard>
  </section>

  <section class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ artigosTotal }}</p>
      <p class="text-sm text-brand-dark/60">Artigos (5 anos)</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ capitulos }}</p>
      <p class="text-sm text-brand-dark/60">Capítulos</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ anais }}</p>
      <p class="text-sm text-brand-dark/60">Trabalhos em anais</p>
    </GlassCard>
    <GlassCard>
      <p class="text-3xl font-bold text-brand-green">{{ mestrados }}</p>
      <p class="text-sm text-brand-dark/60">Orientações concluídas</p>
    </GlassCard>
  </section>

  <section class="mb-12">
    <h2 class="text-2xl font-bold text-brand-dark mb-4">Projetos em Andamento</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <GlassCard v-for="p in ativos" :key="p.nome">
        <div class="flex items-start gap-2 mb-1">
          <span class="text-xs font-semibold uppercase tracking-wider"
            :class="p.tipo === 'produto' ? 'text-brand-yellow' : p.tipo === 'pesquisa' ? 'text-brand-green' : 'text-brand-dark/50'"
          >{{ p.tipo }}</span>
        </div>
        <h3 class="font-semibold text-brand-dark">{{ p.nome }}</h3>
        <p class="text-sm text-brand-dark/60 mt-1">{{ p.descricao }}</p>
      </GlassCard>
    </div>
  </section>

  <section>
    <h2 class="text-2xl font-bold text-brand-dark mb-4">Linha do Tempo</h2>
    <GlassCard>
      <div class="relative pl-6 border-l-2 border-brand-green/30 space-y-6">
        <div v-for="(p, i) in projetos" :key="i">
          <div class="absolute -left-[9px] w-4 h-4 rounded-full bg-brand-green" :style="{ top: `${i * 64 + 8}px` }"></div>
          <p class="text-xs text-brand-green font-semibold">{{ p.periodo }}</p>
          <h3 class="font-semibold text-brand-dark">{{ p.nome }}</h3>
          <p class="text-sm text-brand-dark/60">{{ p.papel }}</p>
        </div>
      </div>
    </GlassCard>
  </section>
</template>