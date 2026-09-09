<script setup lang="ts">
import GlassCard from '../components/GlassCard.vue'
</script>

<template>
  <h1 class="text-3xl font-bold text-brand-dark mb-2">Serviços</h1>

  <section class="grid md:grid-cols-2 gap-6 mb-8 mt-6">
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Modelagem de sistemas com ontologias</h2>
      <p class="text-sm text-brand-dark/60">
        Representação formal do conhecimento com ontologias para integrar dados, padronizar o vocabulário do domínio e dar base semântica a sistemas de apoio à decisão, buscadores e agentes inteligentes.
      </p>
    </GlassCard>
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Análise de dados com ML e clustering</h2>
      <p class="text-sm text-brand-dark/60">
        Exploração de dados com aprendizado de máquina e técnicas de clustering para segmentação, detecção de padrões e geração de insights que orientam decisões em saúde, educação, transporte e mercado, incluindo coleta via crawling inteligente, dashboards e painéis de acompanhamento e sistemas neuro-fuzzy (ANFIS).
      </p>
    </GlassCard>
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Otimização combinatória e Pesquisa Operacional</h2>
      <p class="text-sm text-brand-dark/60">
        Modelagem e solução de problemas de otimização, como roteirização, dimensionamento de frotas e alocação de recursos, com algoritmos genéticos, fluxo em redes e programação matemática.
      </p>
    </GlassCard>
    <GlassCard>
      <h2 class="text-lg font-bold text-brand-dark mb-2">Multiagentes, RAG e automação de tarefas</h2>
      <p class="text-sm text-brand-dark/60">
        Desenvolvimento de sistemas multiagentes, RAG sobre bases próprias, agentes conversacionais e automação de tarefas e workflows com n8n, do protótipo à operação. Inclui plataformas de inteligência de mercado para concessões públicas, com monitoramento, prospecção e análise automatizada de editais, além de geração de conteúdo, storyboards e apresentações com IA.
      </p>
    </GlassCard>
  </section>

  <GlassCard class="mb-8">
    <h2 class="text-lg font-bold text-brand-dark mb-2">Produtos educacionais e gamificação</h2>
    <p class="text-sm text-brand-dark/60">
      Criação de ambientes de aprendizagem com storytelling, gamificação e sala de aula invertida, laboratórios virtuais, microlearning e trilhas adaptativas, do conteúdo ao sistema, com a solidez e a experiência de uma consultoria consolidada.
    </p>
  </GlassCard>

  <GlassCard>
    <h2 class="text-lg font-bold text-brand-dark mb-2">Consultoria e mentoria técnica</h2>
    <p class="text-sm text-brand-dark/60">
      Acompanhamento especializado para equipes e projetos: desenho de arquiteturas de IA, avaliação de soluções, transferência de tecnologia e mentoria em machine learning, otimização e automação.
    </p>
  </GlassCard>
</template>