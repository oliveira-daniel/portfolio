<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Consultoria</h1>
  <p class="text-brand-dark/60 mb-8">ProFuzzy Consultoria e Sistemas Ltda — desde 1998</p>

  <section class="grid md:grid-cols-3 gap-6 mb-8">
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Saúde & Bem-estar</h2>
      <p class="text-sm text-brand-dark/60">
        Sistemas para prontuário, clínica terapêutica e oncologia. Desenvolvimento de plataformas com registro de pacientes, acompanhamento e dashboards.
      </p>
    </GlassCard>
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Transporte & Logística</h2>
      <p class="text-sm text-brand-dark/60">
        Otimização de frota mínima para transporte público, prospecção de empresas via crawling inteligente, e análise de viagens com algoritmos de rede.
      </p>
    </GlassCard>
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">IA & Automação</h2>
      <p class="text-sm text-brand-dark/60">
        Agentes de IA, LLMs, sistemas neuro-fuzzy (ANFIS), automação n8n, geração de storyboards, conteúdo e apresentações com IA.
      </p>
    </GlassCard>
  </section>

  <GlassCard>
    <h2 class="text-lg font-bold text-brand-dark mb-2">Áreas de Atuação</h2>
    <ul class="list-disc list-inside text-sm text-brand-dark/70 space-y-1">
      <li>Inteligência Artificial aplicada (ML, LLMs, agentes, RAG, busca vetorial)</li>
      <li>Otimização combinatória (GRASP, algoritmos genéticos, redes de fluxo)</li>
      <li>Plataformas de inteligência de mercado para concessões públicas</li>
      <li>Automação de workflows com n8n e pipelines de IA</li>
      <li>Desenvolvimento de frameworks e produtos educacionais</li>
    </ul>
  </GlassCard>
</template>