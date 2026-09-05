<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
import projetos from '../data/projetos.json'

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
          <h1 class="text-4xl font-bold text-brand-green mb-2">Daniel Oliveira</h1>
          <p class="text-brand-dark/80 leading-relaxed">
            CTO e sócio-fundador da <strong>ProFuzzy</strong> (1998–atual), Professor no PPG Ensino de Ciências da Unigranrio e pesquisador no <strong>GPIAE/DEGC/UFSC</strong>. Doutor em Engenharia de Produção (UFSC/INSA-Rouen), mestre em Computação (Univali). Atua na interseção entre Inteligência Artificial, otimização combinatória e educação — com experiência em sistemas neuro-fuzzy, agentes multiagentes, LLMs, RAG, e plataformas de IA para concessões, saúde e transporte.
          </p>
          <div class="flex gap-3 mt-4">
            <router-link to="/servicos" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-105 transition-transform">
              Ver Serviços
            </router-link>
            <router-link to="/academico" class="glass px-4 py-2 rounded-lg text-sm font-semibold text-brand-green hover:scale-105 transition-transform">
              Produção Acadêmica
            </router-link>
          </div>
        </div>
      </div>
    </GlassCard>
  </section>

  <section class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-12">
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Soluções em IA & Otimização</h3>
      <p class="text-sm text-brand-dark/60">LLMs, agentes, RAG, sistemas neuro-fuzzy, algoritmos genéticos, GRASP, redes de fluxo.</p>
    </GlassCard>
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Plataformas & Automação</h3>
      <p class="text-sm text-brand-dark/60">Desenvolvimento de plataformas web, pipelines n8n, dashboards, crawlers, storyboards com IA.</p>
    </GlassCard>
    <GlassCard>
      <h3 class="font-bold text-brand-dark mb-2">Frentes de Atuação</h3>
      <p class="text-sm text-brand-dark/60">Saúde & Bem-estar, Transporte & Logística, Concessões Públicas, Educação.</p>
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